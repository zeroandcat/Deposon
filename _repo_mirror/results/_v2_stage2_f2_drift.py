# -*- coding: utf-8 -*-
"""
deposon V2 阶段 2 (F-2 漂移=epsilon 底)
- 用 doubao-embedding-vision-251215 重嵌 22 caption 2-3 次
- 算 ||emb_i - emb_j||₂ 分布 → 守恒律在 embedding 层的"实际下界"
- 若 1e-8 ~ 1e-6 → P-B 守恒审计在语义空间需用更松阈值
- 严守 7 铁律
"""
import os, sys, io, re, json, time, hashlib, base64
import urllib.request, urllib.error
import numpy as np
from datetime import datetime, timezone, timedelta

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
CORPUS_DIR = r'D:\私人资料\deposon-repo\corpus\v20'
VOLC_22CAP_REF = r'D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json'

OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_v2_phase2_f2_2026_09_11.json'
OUTPUT_LOG = r'D:\私人资料\deposon-repo\results\deposon_v2_phase2_f2_2026_09_11.log'

BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
MODEL_EMB = 'doubao-embedding-vision-251215'
EMB_BATCH = 10
EMB_TIMEOUT = 30
N_REPEATS = 3  # 2-3 次,选 3 次更稳
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
    captions = []
    for g in idx['graphs']:
        d = json.load(open(os.path.join(CORPUS_DIR, g['file']), 'r', encoding='utf-8'))
        labels = d.get('labels', [])
        cap = (f"Concept graph {g['graph_id']} "
               f"(family={g['family']}, structure={g['structure']}, "
               f"N={g['N']}, n_named={g['n_named']}): " + '; '.join(labels))
        captions.append(cap)
    log(f'CAPTIONS_BUILT n={len(captions)}')

    # N_REPEATS runs of 22 caption embedding
    runs = []  # list of 22x2048 np.arrays
    for r_idx in range(N_REPEATS):
        log(f'RUN_START [{r_idx+1}/{N_REPEATS}]')
        t0 = time.time()
        embs = query_embedding_text(api_key, captions)
        arr = np.array(embs, dtype=np.float32)
        runs.append(arr)
        log(f'RUN_DONE [{r_idx+1}/{N_REPEATS}] dim={arr.shape[1]} ms={round((time.time()-t0)*1000,1)}')

    # Compute pairwise L2 distance distribution
    # Per-caption drift: ||emb_run1 - emb_run2||, ||emb_run1 - emb_run3||, etc.
    # Cross-caption baseline: ||emb_i - emb_j|| for i != j in same run
    n_captions = len(captions)
    n_runs = len(runs)
    log(f'COMPUTING_DRIFT n_captions={n_captions} n_runs={n_runs}')

    per_caption_drift = {}  # concept_id -> list of L2 to other runs
    for c_idx in range(n_captions):
        cid = concept_ids[c_idx]
        drifts = []
        for r_a in range(n_runs):
            for r_b in range(r_a + 1, n_runs):
                d = float(np.linalg.norm(runs[r_a][c_idx] - runs[r_b][c_idx]))
                drifts.append(d)
        per_caption_drift[cid] = drifts

    # Pool all drifts
    all_drifts = []
    for cid, ds in per_caption_drift.items():
        all_drifts.extend(ds)
    all_drifts = np.array(all_drifts)

    # Cross-caption baseline (run 0): 22×22 L2 matrix
    base = runs[0]
    cross = []
    for i in range(n_captions):
        for j in range(i+1, n_captions):
            d = float(np.linalg.norm(base[i] - base[j]))
            cross.append(d)
    cross = np.array(cross)

    # Stats
    drift_stats = {
        'n_pairs': int(len(all_drifts)),
        'min': float(all_drifts.min()) if len(all_drifts) else None,
        'max': float(all_drifts.max()) if len(all_drifts) else None,
        'mean': float(all_drifts.mean()) if len(all_drifts) else None,
        'median': float(np.median(all_drifts)) if len(all_drifts) else None,
        'p95': float(np.percentile(all_drifts, 95)) if len(all_drifts) else None,
        'p99': float(np.percentile(all_drifts, 99)) if len(all_drifts) else None,
        'std': float(all_drifts.std()) if len(all_drifts) else None,
    }
    cross_stats = {
        'n_pairs': int(len(cross)),
        'min': float(cross.min()) if len(cross) else None,
        'max': float(cross.max()) if len(cross) else None,
        'mean': float(cross.mean()) if len(cross) else None,
        'median': float(np.median(cross)) if len(cross) else None,
        'p95': float(np.percentile(cross, 95)) if len(cross) else None,
        'p99': float(np.percentile(cross, 99)) if len(cross) else None,
        'std': float(cross.std()) if len(cross) else None,
    }

    log(f'DRIFT_STATS mean={drift_stats["mean"]:.4e} p99={drift_stats["p99"]:.4e} max={drift_stats["max"]:.4e}')
    log(f'CROSS_STATS mean={cross_stats["mean"]:.4e} p95={cross_stats["p95"]:.4e}')

    # Verdict
    drift_mean = drift_stats['mean'] or 0
    cross_mean = cross_stats['mean'] or 1
    ratio_drift_to_cross = drift_mean / cross_mean  # how much drift vs natural cross-caption distance
    
    # epsilon floor interpretation:
    # If drift_mean < 1e-6, very stable (good for P-B conservation)
    # If drift_mean in 1e-6 ~ 1e-4, moderate
    # If drift_mean > 1e-4, high drift (P-B conservation needs very loose threshold)
    if drift_mean < 1e-6:
        verdict = 'EXCELLENT (drift < 1e-6, P-B 守恒审计可严阈值)'
    elif drift_mean < 1e-4:
        verdict = 'GOOD (drift < 1e-4, P-B 守恒审计需中等阈值)'
    elif drift_mean < 1e-2:
        verdict = 'MODERATE (drift < 1e-2, P-B 守恒审计需松阈值)'
    else:
        verdict = 'POOR (drift >= 1e-2, P-B 守恒审计需重审)'
    
    log(f'VERDICT drift_mean={drift_mean:.4e} → {verdict}')

    # Output
    results = {
        'timestamp': datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds'),
        'phase': 'V2 阶段 2 (F-2 漂移=epsilon 底)',
        'model': MODEL_EMB,
        'n_repeats': N_REPEATS,
        'n_captions': n_captions,
        'concept_ids': concept_ids,
        'per_caption_drift_stats': {
            cid: {
                'n': len(ds),
                'min': float(min(ds)) if ds else None,
                'max': float(max(ds)) if ds else None,
                'mean': float(sum(ds)/len(ds)) if ds else None,
            } for cid, ds in per_caption_drift.items()
        },
        'pooled_drift_stats': drift_stats,
        'cross_caption_baseline_stats': cross_stats,
        'drift_to_cross_ratio': round(ratio_drift_to_cross, 6),
        'verdict': verdict,
        'constraints_honored': {
            'no_proxy': True, 'key_runtime_only': True, 'key_in_json_masked': True,
            'no_openrouter': True, 'no_teamorouter': True, 'no_v41_flash': True,
            'no_gpt6': True, 'no_agent_plan': True, 'no_retry': True,
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
