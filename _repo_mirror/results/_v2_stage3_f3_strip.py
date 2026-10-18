# -*- coding: utf-8 -*-
"""
deposon V2 阶段 3 (F-3 Prefix/Strip 差分向量)
- 22 caption 已有 prefix 版 embedding (from volcengine_22caption_embedding, 沿 V0.1 SPEC)
- 1 次 strip 版 embedding (labels-only 或结构化 JSON, 不含 prefix)
- 差分 Δ = emb_prefix - emb_strip
- 重测 Q1 的 T/R/A ratio
- 若 ≥ 1.2 = HIGH-2 根因闭环(NOISE 来自污染)
- 若仍 NOISE = vision embedding 对 graph 拓扑无区分度
"""
import os, sys, io, re, json, time, hashlib, base64
import urllib.request, urllib.error
import numpy as np
from datetime import datetime, timezone, timedelta

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
VOLC_22CAP_REF = r'D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json'

OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_v2_phase3_f3_2026_09_11.json'
OUTPUT_LOG = r'D:\私人资料\deposon-repo\results\deposon_v2_phase3_f3_2026_09_11.log'

BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
MODEL_EMB = 'doubao-embedding-vision-251215'
EMB_BATCH = 10
EMB_TIMEOUT = 30
PROXY_KEYS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']

LOG_FP = None
def log(msg):
    line = f'[{time.strftime("%H:%M:%S")}] {msg}'
    print(line, flush=True)
    if LOG_FP is not None:
        try:
            LOG_FP.write(line + '\n')
            LOG_FP.flush()
        except Exception:
            pass


def load_key():
    text = None
    for enc_name in ('gb18030', 'gbk', 'utf-8', 'utf-16'):
        try:
            text = io.open(KEY_FILE, 'r', encoding=enc_name).read()
            if 'ark-[REDACTED]' in text:
                break
        except Exception:
            pass
    if not text:
        raise RuntimeError('FATAL: key file read failed')
    m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', text)
    if not m:
        raise RuntimeError('FATAL: ark-[REDACTED]* key not found')
    api_key = m.group(0)
    key_truncated = api_key[:20] + '...' + api_key[-4:]
    os.environ['ARK_CODING_PLAN_KEY'] = api_key
    for k in PROXY_KEYS:
        os.environ.pop(k, None)
    del text
    return api_key, key_truncated


def http_post(url, payload, headers, timeout):
    data = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode('utf-8', errors='replace')
            elapsed_ms = (time.time() - t0) * 1000
            try:
                body = json.loads(raw)
            except Exception:
                body = {'_raw': raw}
            return {'status': resp.status, 'ms': round(elapsed_ms, 1), 'body': body, 'error': None}
    except urllib.error.HTTPError as e:
        elapsed_ms = (time.time() - t0) * 1000
        try:
            err_raw = e.read().decode('utf-8', errors='replace') if e.fp else ''
        except Exception:
            err_raw = ''
        return {'status': e.code, 'ms': round(elapsed_ms, 1), 'body': None, 'error': err_raw[:500]}
    except Exception as e:
        elapsed_ms = (time.time() - t0) * 1000
        return {'status': -1, 'ms': round(elapsed_ms, 1), 'body': None,
                'error': f'{type(e).__name__}: {str(e)[:300]}'}


def query_embedding_text(api_key, captions, model=MODEL_EMB, batch=EMB_BATCH):
    url = f'{BASE_URL}/embeddings'
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    chunks = [captions[i:i + batch] for i in range(0, len(captions), batch)]
    out = []
    for ci, chunk in enumerate(chunks):
        payload = {'model': model, 'input': chunk}
        res = http_post(url, payload, headers, timeout=EMB_TIMEOUT)
        if res['status'] != 200:
            raise RuntimeError(f'emb-text chunk {ci} status={res["status"]} error={res["error"][:200]}')
        data = res['body'].get('data', [])
        data.sort(key=lambda x: x.get('index', 0))
        for d in data:
            out.append(d['embedding'])
        log(f'  EMB_TEXT chunk {ci+1}/{len(chunks)} n={len(chunk)} status=200 ms={res["ms"]}')
    return out


def main():
    global LOG_FP
    os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
    LOG_FP = open(OUTPUT_LOG, 'w', encoding='utf-8')

    api_key, key_truncated = load_key()
    log(f'KEY_OK truncated={key_truncated} proxy_cleared')

    # Anchor
    anchor_path = r'D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json'
    anchor_sha = hashlib.sha256(open(anchor_path, 'rb').read()).hexdigest()[:12]
    assert anchor_sha == '03c6c01f3697', f'5 锚 SHA 变: {anchor_sha}'
    log(f'ANCHOR_OK SHA-12={anchor_sha}')

    # Read 22 captions
    idx = json.load(open(os.path.join(CORPUS_DIR, 'index.json'), 'r', encoding='utf-8'))
    assert idx['n_graphs'] == 22
    concept_ids = [g['graph_id'] for g in idx['graphs']]
    
    # Two caption variants:
    # 1) PREFIX 版: 沿 V0.1 SPEC, "Concept graph X (family, structure, N, n_named): labels"
    # 2) STRIP 版: labels-only (去除 prefix 污染)
    prefix_captions = []
    strip_captions = []
    for g in idx['graphs']:
        d = json.load(open(os.path.join(CORPUS_DIR, g['file']), 'r', encoding='utf-8'))
        labels = d.get('labels', [])
        prefix_cap = (f"Concept graph {g['graph_id']} "
                      f"(family={g['family']}, structure={g['structure']}, "
                      f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(labels))
        prefix_captions.append(prefix_cap)
        strip_cap = '; '.join(labels)  # labels-only
        strip_captions.append(strip_cap)
    log(f'CAPTIONS_BUILT n={len(prefix_captions)} prefix_avg_len={sum(len(c) for c in prefix_captions)//len(prefix_captions)} '
        f'strip_avg_len={sum(len(c) for c in strip_captions)//len(strip_captions)}')

    # Embed PREFIX
    log('EMB_PREFIX_START (re-embed, get full 2048-d)')
    t0 = time.time()
    prefix_embs = query_embedding_text(api_key, prefix_captions)
    prefix_arr = np.array(prefix_embs, dtype=np.float32)
    prefix_total_ms = round((time.time() - t0) * 1000, 1)
    log(f'EMB_PREFIX_DONE dim={prefix_arr.shape[1]} total_ms={prefix_total_ms}')

    # Embed STRIP
    log('EMB_STRIP_START (NEW, 1 batch call)')
    t0 = time.time()
    strip_embs = query_embedding_text(api_key, strip_captions)
    strip_arr = np.array(strip_embs, dtype=np.float32)
    strip_total_ms = round((time.time() - t0) * 1000, 1)
    log(f'EMB_STRIP_DONE dim={strip_arr.shape[1]} total_ms={strip_total_ms}')

    # Compute differential Δ = prefix - strip
    delta = prefix_arr - strip_arr
    delta_norm = np.linalg.norm(delta, axis=1)
    log(f'DELTA_NORM mean={delta_norm.mean():.4f} max={delta_norm.max():.4f} min={delta_norm.min():.4f}')

    # Q1: T/R/A ratio test
    # intra = mean sim within same class (kmeans_k4_labels)
    # inter = mean sim across classes
    volc_22 = json.load(open(VOLC_22CAP_REF, 'r', encoding='utf-8'))
    kmeans_labels = volc_22['kmeans_k4_labels']
    per_class = volc_22['per_class_members']
    cid_to_class = {}
    for class_id, (class_name, members) in enumerate(per_class.items()):
        for m in members:
            cid_to_class[m] = class_id
    idx_to_class = {i: cid_to_class.get(concept_ids[i], 0) for i in range(22)}

    def cos_sim_matrix(arr):
        norms = np.linalg.norm(arr, axis=1, keepdims=True)
        n = arr / (norms + 1e-12)
        return n @ n.T

    def tra_ratio(arr):
        sim = cos_sim_matrix(arr)
        n = sim.shape[0]
        idx = np.arange(n)
        # mask intra-class
        classes = [idx_to_class[i] for i in range(n)]
        intra_mask = np.zeros_like(sim, dtype=bool)
        inter_mask = np.zeros_like(sim, dtype=bool)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if classes[i] == classes[j]:
                    intra_mask[i, j] = True
                else:
                    inter_mask[i, j] = True
        intra_mean = sim[intra_mask].mean() if intra_mask.any() else 0
        inter_mean = sim[inter_mask].mean() if inter_mask.any() else 1
        ratio = intra_mean / (inter_mean + 1e-10)
        return intra_mean, inter_mean, ratio

    pi, pp, pr = tra_ratio(prefix_arr)
    si, sp, sr = tra_ratio(strip_arr)
    di, dp, dr = tra_ratio(delta)

    log(f'PREFIX:  intra={pi:.4f} inter={pp:.4f} ratio={pr:.4f}')
    log(f'STRIP:   intra={si:.4f} inter={sp:.4f} ratio={sr:.4f}')
    log(f'DELTA:   intra={di:.4f} inter={dp:.4f} ratio={dr:.4f}')

    # Convert to Python float for JSON serialization
    pi, pp, pr = float(pi), float(pp), float(pr)
    si, sp, sr = float(si), float(sp), float(sr)
    di, dp, dr = float(di), float(dp), float(dr)

    # Verdict
    # If strip ratio > 1.2 = HIGH-2 根因闭环(NOISE 来自 prefix 污染)
    # If strip ratio still NOISE = vision embedding 对 graph 拓扑无区分度
    def verdict(r):
        if r > 1.5: return 'MEANINGFUL'
        if r >= 1.2: return 'GRAY'
        return 'NOISE'

    v_prefix = verdict(pr)
    v_strip = verdict(sr)
    v_delta = verdict(dr)

    if sr >= 1.2:
        root_cause = 'HIGH-2 闭环: NOISE 来自 PREFIX 污染 (去除 prefix 后 ratio 提升到 GRAY/MEANINGFUL)'
    elif pr < 1.2 and sr < 1.2 and dr >= 1.2:
        root_cause = 'P-D V0.2 应引入 DELTA 差分(去除 prefix 后 NOISE 仍在,但差分向量含信号)'
    elif pr < 1.2 and sr < 1.2 and dr < 1.2:
        root_cause = 'Vision embedding 对 graph 拓扑 NOISE(无论 prefix/strip/delta 都无区分度)'
    else:
        root_cause = 'INDETERMINATE'

    log(f'VERDICT prefix={v_prefix} strip={v_strip} delta={v_delta} root_cause={root_cause}')

    # Output
    results = {
        'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
        'phase': 'V2 阶段 3 (F-3 Prefix/Strip 差分向量)',
        'model': MODEL_EMB,
        'n_captions': len(prefix_captions),
        'concept_ids': concept_ids,
        'prefix_total_ms': prefix_total_ms,
        'strip_total_ms': strip_total_ms,
        'delta_norm': {
            'mean': float(delta_norm.mean()),
            'max': float(delta_norm.max()),
            'min': float(delta_norm.min()),
            'per_caption': {concept_ids[i]: float(delta_norm[i]) for i in range(len(concept_ids))},
        },
        'tra_ratio': {
            'prefix': {'intra': round(pi, 4), 'inter': round(pp, 4), 'ratio': round(pr, 4), 'verdict': v_prefix},
            'strip': {'intra': round(si, 4), 'inter': round(sp, 4), 'ratio': round(sr, 4), 'verdict': v_strip},
            'delta': {'intra': round(di, 4), 'inter': round(dp, 4), 'ratio': round(dr, 4), 'verdict': v_delta},
        },
        'root_cause': root_cause,
        'constraints_honored': {
            'no_proxy': True, 'key_runtime_only': True, 'key_in_json_masked': True,
            'no_openrouter': True, 'no_teamorouter': True, 'no_v41_flash': True,
            'no_gpt6': True, 'no_agent_plan': True, 'no_retry': True,
            'no_corpus_v20_modify': True,  # 严守铁律
        },
    }
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    log(f'OUTPUT_SAVED {OUTPUT_JSON}')

    log('DONE')
    if LOG_FP is not None:
        LOG_FP.close()
    return 0


if __name__ == '__main__':
    sys.exit(main())
