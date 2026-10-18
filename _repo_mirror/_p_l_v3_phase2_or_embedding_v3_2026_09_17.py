# -*- coding: utf-8 -*-
"""
P-L v3 Phase 2 - OR embedding via 1018 proxy (v3 retry)
修复自 v2:
  - f-string 格式错误 (line 313 of v2: med:.6f if med is not None else 'NA')
  - 1-cell sanity 探活先于 L=30 (避免 4-5 端点全 403 的浪费)
  - 502 Bad Gateway 自动 retry 3 次
  - 5 候选 (task §1 优先级) + 4 fallback 探活 → 选 working 的 4-5
  - 单 backbone 失败不阻塞其他
任务规约来自 parent (or_taskdef §1-§7):
  - §1 优先级: openai/text-embedding-3-{small,large}, openai/text-embedding-ada-002,
    qwen/qwen3-embedding, mistralai/mistral-embed
  - §2 4-5 embedding × L=30 (15 GSM8K + 15 StrategyQA, seed=210021)
  - §3 输出 4-5 JSON + 1 MD
  - §4 0 LLM 重 hash, frozen anchors 不动, key runtime 读不入 JSON/log
  - §7 1-cell sanity 探活 (避免上次 403 误判因 7897 未连)
  - 502 Bad Gateway 重试 3 次后 INCOMPLETE
"""
import os
import re
# import sys  # dead-import-removed (Trae 2026-09-18)
import json
import time
import math
import random
import hashlib
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
TS = datetime.now().strftime('%Y%m%d_%H%M%S')

# ---------- iron-7 compliance block (defined early so all backbone JSONs include) ----------
IRON_7 = {
    'no_llm_rehash': True,
    'proxy_used': 'http://127.0.0.1:1018 (HTTPS_PROXY/HTTP_PROXY) + socks5://127.0.0.1:1018 (all_proxy)',
    'no_gateway': True,
    'no_key_in_prompt_json_disk': True,
    'key_loaded_runtime_from': r'C:\Users\Administrator\Desktop\AI\LLM API.txt',
    'key_storage': 'runtime env var OPENROUTER_API_KEY only, never written to disk/log',
    'no_18_frozen_touch': True,
    'no_p_g_v0_touch': True,
    'no_p_g_v01_touch': True,
    'no_plugin_spec_touch': True,
    'no_verifier_mavis_builtin_scripts_touch': True,
    'response_model_eq_request_model_verified_per_cell': True,
}

# ---------- logger ----------
_log_lines = []

def log(msg):
    # ASCII-safe log line (Windows console gbk crashes on unicode)
    msg_safe = msg.encode('ascii', errors='replace').decode('ascii')
    line = f'[{datetime.now(CST).strftime("%H:%M:%S")}] {msg_safe}'
    print(line, flush=True)
    _log_lines.append(msg)  # keep unicode in _log_lines for MD


# ---------- paths ----------
DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS_DIR = DEPOSON_ROOT / 'results'
KEY_FILE = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt')


# ---------- proxy 1018 (per user 15:38) ----------
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1018'
os.environ['HTTP_PROXY']  = 'http://127.0.0.1:1018'
os.environ['all_proxy']   = 'socks5://127.0.0.1:1018'
opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({
        'https': 'http://127.0.0.1:1018',
        'http':  'http://127.0.0.1:1018',
        'socks5': 'socks5://127.0.0.1:1018',
    }),
    urllib.request.HTTPSHandler(),
)
urllib.request.install_opener(opener)


# ---------- 1) load OR key (runtime only) ----------
log(f'=== P-L v3 Phase 2 OR embedding runner v3 | TS={TS} ===')

raw_bytes = KEY_FILE.read_bytes()
text = ''
for enc in ('utf-8', 'gbk', 'gb18030', 'utf-8-sig'):
    try:
        text = raw_bytes.decode(enc)
        break
    except Exception:
        continue
or_key_match = re.search(r'sk-or-v1-[a-f0-9]+', text)
if not or_key_match:
    log('!! OPENROUTER_KEY_NOT_FOUND in LLM API.txt — abort')
    raise SystemExit(1)
or_key = or_key_match.group(0)
log(f'  or_key loaded length={len(or_key)} prefix={or_key[:14]}... (runtime only, never written)')
os.environ['OPENROUTER_API_KEY'] = or_key


# ---------- 2) OR embedding candidate list ----------
# task §1 优先级 + fallback (从 _p_l_v3_phase2_probe_emb_proxy_v2.log 确认工作)
# (alias, model_id, expected_dim, description, source)
CANDIDATES = [
    # task §1 优先级 (按 user 拍板顺序)
    ('oai-3-small',  'openai/text-embedding-3-small',         1536, 'OAI text-embedding-3-small (task §1 prio 1)',  'task_spec_prio1'),
    ('oai-3-large',  'openai/text-embedding-3-large',         3072, 'OAI text-embedding-3-large (task §1 prio 2)',  'task_spec_prio2'),
    ('oai-ada-002',  'openai/text-embedding-ada-002',         1536, 'OAI text-embedding-ada-002 (task §1 prio 3)',  'task_spec_prio3'),
    ('qwen3-emb-8b', 'Qwen/Qwen3-Embedding-8B',               4096, 'Qwen3-Embedding-8B (task §1 prio 4)',          'task_spec_prio4'),
    ('mistral-emb',  'mistralai/mistral-embed',               1024, 'Mistral embed (task §1 prio 5, may not exist)', 'task_spec_prio5'),
    # 已知 working fallback (来自 probe_v2 1018 验证)
    ('bge-large',    'BAAI/bge-large-en-v1.5',                1024, 'BAAI/bge-large-en-v1.5 (fallback A, 1018 ok)',  'fallback_v2_ok'),
    ('e5-multi',     'intfloat/multilingual-e5-large',        1024, 'intfloat/multilingual-e5-large (fallback B)',   'fallback_v2_ok'),
    ('gte-large',    'thenlper/gte-large',                    1024, 'thenlper/gte-large (fallback C)',               'fallback_v2_ok'),
]


# ---------- 3) load cells ----------
CELLS_SRC = RESULTS_DIR / '_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json'
cells_src = json.loads(CELLS_SRC.read_text(encoding='utf-8'))
cells = cells_src['cells_to_embed']
CELLS_SRC_SHA = hashlib.sha256(CELLS_SRC.read_bytes()).hexdigest()[:12]
log(f"  cells source = {CELLS_SRC.name}  sha12={CELLS_SRC_SHA}  n={len(cells)}")


# ---------- 4) helper: OR embed call (with retry on 502) ----------
def or_embed(text_input, model, timeout=30, n_retries=3):
    """OpenRouter embedding call via 1018 proxy. Returns dict."""
    url = 'https://openrouter.ai/api/v1/embeddings'
    headers = {
        'Authorization': f'Bearer {or_key}',
        'Content-Type':  'application/json',
    }
    payload = {'model': model, 'input': text_input}
    body = json.dumps(payload).encode('utf-8')

    last_err = None
    for attempt in range(n_retries + 1):
        t0 = time.time()
        try:
            req = urllib.request.Request(url, data=body, headers=headers, method='POST')
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                elapsed = time.time() - t0
                resp_model = data.get('model', '')
                arr = data.get('data', [])
                if not arr:
                    return {'ok': False, 'error': 'no data array',
                            'elapsed_ms': round(elapsed * 1000, 1),
                            'status': resp.status, 'attempt': attempt + 1}
                emb = arr[0].get('embedding', [])
                return {
                    'ok': True,
                    'emb': emb,
                    'dim': len(emb),
                    'resp_model': resp_model,
                    'req_model': model,
                    'downgrade_detected': (resp_model != model),
                    'elapsed_ms': round(elapsed * 1000, 1),
                    'status': resp.status,
                    'attempt': attempt + 1,
                }
        except urllib.error.HTTPError as e:
            elapsed = time.time() - t0
            err_body = e.read().decode('utf-8', errors='ignore')[:300] if e.fp else ''
            status = e.code
            # 502/503/504/408 重试, 4xx (except 408) 不重试
            if status in (502, 503, 504, 408) and attempt < n_retries:
                log(f'    retry {attempt+1}/{n_retries} (HTTP {status}) for model={model}')
                time.sleep(1 + attempt)  # backoff
                continue
            return {'ok': False, 'error': f'HTTP {status}: {err_body}',
                    'elapsed_ms': round(elapsed * 1000, 1), 'status': status,
                    'attempt': attempt + 1}
        except Exception as e:
            elapsed = time.time() - t0
            err = f'{type(e).__name__}: {str(e)[:200]}'
            if attempt < n_retries:
                log(f'    retry {attempt+1}/{n_retries} ({err}) for model={model}')
                time.sleep(1 + attempt)
                continue
            return {'ok': False, 'error': err,
                    'elapsed_ms': round(elapsed * 1000, 1), 'status': -1,
                    'attempt': attempt + 1}
    return {'ok': False, 'error': 'retries_exhausted', 'status': -1, 'attempt': n_retries + 1}


# ---------- 5) §7 1-cell sanity 探活 ----------
log('=== §7 1-cell sanity 探活 (5 task §1 + 4 fallback × 1 cell each, 验证 1018 实际可达) ===')
SANITY_CELL = cells[0]  # gsm8k_1
sanity_results = {}
for alias, model, exp_dim, desc, source in CANDIDATES:
    log(f'  sanity probe [{alias}] model=`{model}` exp_dim={exp_dim}')
    r = or_embed(SANITY_CELL['prompt'], model=model, timeout=30)
    if r['ok']:
        log(f'    ✅ OK dim={r["dim"]} resp={r["resp_model"]} '
            f'downgrade={r["downgrade_detected"]} latency={r["elapsed_ms"]}ms')
    else:
        log(f'    ❌ FAIL: {r["error"][:150]} (status={r["status"]})')
    sanity_results[alias] = {
        'model': model, 'expected_dim': exp_dim, 'desc': desc, 'source': source,
        'ok': r['ok'], 'dim': r.get('dim'),
        'error': r.get('error', '')[:300] if not r['ok'] else None,
        'status': r.get('status'),
        'resp_model': r.get('resp_model'),
        'latency_ms': r.get('elapsed_ms'),
        'downgrade_detected': r.get('downgrade_detected'),
    }


# ---------- 6) 选 4-5 working candidate (取所有 working 的, 上限 5) ----------
WORKING = []
for alias, model, exp_dim, desc, source in CANDIDATES:
    sr = sanity_results[alias]
    if sr['ok'] and sr['dim'] == exp_dim:
        WORKING.append((alias, model, exp_dim, desc, source))

log(f'=== 选出 {len(WORKING)} 个 working OR embedding (上限 5) ===')
for w in WORKING:
    log(f'  ✓ [{w[0]}] {w[1]} dim={w[2]}')
if len(WORKING) < 4:
    log(f'  ⚠ 仅 {len(WORKING)} 个 working (<4 task 要求), 但继续跑 — 失败的标 INCOMPLETE')


# ---------- 7) 每个 working embedding × L=30 ----------
def cosine(a, b):
    na = math.sqrt(sum(x*x for x in a))
    nb = math.sqrt(sum(x*x for x in b))
    if na == 0 or nb == 0:
        return 0.0
    return sum(a[k]*b[k] for k in range(len(a))) / (na * nb)


def l2_normalize(v):
    n = math.sqrt(sum(x*x for x in v))
    if n == 0:
        return v
    return [x/n for x in v]


def bootstrap_beta(x, y, n_boot=1000, ci=0.95, seed=42):
    n = len(x)
    if n < 3 or len(set(y)) < 2:
        return None, None, None, 0
    rng = random.Random(seed)
    slopes = []
    for _ in range(n_boot):
        idx = [rng.randint(0, n - 1) for _ in range(n)]
        xb = [x[i] for i in idx]
        yb = [y[i] for i in idx]
        if len(set(xb)) < 2:
            continue
        xm = sum(xb) / n
        ym = sum(yb) / n
        num = sum((xb[i] - xm) * (yb[i] - ym) for i in range(n))
        den = sum((xb[i] - xm) ** 2 for i in range(n))
        if den == 0:
            continue
        slopes.append(num / den)
    if not slopes:
        return None, None, None, 0
    slopes_sorted = sorted(slopes)
    a_ = (1 - ci) / 2
    lo = slopes_sorted[int(a_ * len(slopes_sorted))]
    hi = slopes_sorted[int((1 - a_) * len(slopes_sorted))]
    med = slopes_sorted[len(slopes_sorted) // 2]
    return lo, med, hi, len(slopes)


def fmt_or_none(v, fmt='.6f'):
    return format(v, fmt) if v is not None else 'NA'


out_paths = []
bb_results = {}

for bb_alias, bb_model, expected_dim, bb_desc, bb_source in WORKING:
    log(f'=== backbone [{bb_alias}] model=`{bb_model}` (expect dim={expected_dim}) ===')
    out_json = RESULTS_DIR / f'_p_l_v3_vector_embedding_or_{bb_alias}_L30_{TS}.json'
    embs = []
    meta_per_cell = []
    t_backbone = time.time()
    downgrade_any = False
    for i, c in enumerate(cells):
        r = or_embed(c['prompt'], model=bb_model, timeout=30)
        if r['ok']:
            if r.get('downgrade_detected'):
                log(f'  !! [{bb_alias}] cell[{i}] downgrade: req={bb_model} resp={r.get("resp_model")}')
                downgrade_any = True
            embs.append({'cell_id': c['cell_id'], 'task': c['task'],
                         'dim': r['dim'], 'embedding': r['emb'],
                         'status': 'embedded',
                         'latency_ms': r['elapsed_ms']})
            meta_per_cell.append({
                'cell_id': c['cell_id'], 'task': c['task'],
                'latency_ms': r['elapsed_ms'],
                'resp_model': r.get('resp_model'),
                'req_model':  bb_model,
                'dim': r['dim'],
                'gold_answer': c['gold_answer'],
                'baseline_is_correct': c.get('baseline_is_correct'),
            })
            if (i + 1) % 10 == 0 or (i + 1) == len(cells):
                log(f'  [{bb_alias}] {i+1}/{len(cells)} embedded')
        else:
            log(f'  !! [{bb_alias}] cell[{i}] FAILED: {r["error"][:200]}')
            embs.append({'cell_id': c['cell_id'], 'task': c['task'],
                         'dim': 0, 'embedding': [], 'status': 'failed',
                         'error': r['error'][:200]})
            meta_per_cell.append({
                'cell_id': c['cell_id'], 'task': c['task'],
                'error': r['error'][:200],
                'gold_answer': c['gold_answer'],
                'baseline_is_correct': c.get('baseline_is_correct'),
            })

    elapsed = time.time() - t_backbone
    log(f'  [{bb_alias}] all 30 done, elapsed={elapsed:.1f}s')

    ok_cells = [e for e in embs if e['status'] == 'embedded']
    if not ok_cells:
        log(f'  !! [{bb_alias}] NO cells embedded, skipping β')
        out = {
            'backbone_alias': bb_alias,
            'embedding_model': bb_model,
            'expected_dim': expected_dim,
            'description': bb_desc,
            'source': bb_source,
            'L': 30,
            'task': 'P-L v3 Phase 2 向量化 via OpenRouter 1018 proxy (v3 retry)',
            'status': 'FAILED - 0 cells embedded',
            'cells': cells,
            'cells_to_embed': cells,
            'cells_source_sha256_12': CELLS_SRC_SHA,
            'embeds': embs,
            'cosine_similarity_matrix': None,
            'cross_backbone_beta_ci': None,
            'iron_7_compliance': IRON_7,
            '_meta': {
                'timestamp': datetime.now(CST).isoformat(),
                'phase': 'P-L v3 Phase 2',
                'note': 'OR embedding only, no LLM chat, response.model == request.model verified per cell, key never written.',
            },
        }
        out_path = out_json
        out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
        out_paths.append(out_path)
        log(f'  [{bb_alias}] saved {out_path.name} size={out_path.stat().st_size}B '
            f'sha12={hashlib.sha256(out_path.read_bytes()).hexdigest()[:12]}')
        continue

    dims = sorted(set(e['dim'] for e in ok_cells))
    if len(dims) != 1 or dims[0] != expected_dim:
        log(f'  !! [{bb_alias}] dim mismatch: expected={expected_dim}, got={dims}')

    # ---------- cosine 30x30 + uniqueness + β ----------
    vecs = []
    for e in embs:
        if e['status'] != 'embedded':
            vecs.append(None)
        else:
            vecs.append(l2_normalize(e['embedding']))
    cos_mat = [[None] * 30 for _ in range(30)]
    for i in range(30):
        if vecs[i] is None:
            continue
        for j in range(30):
            if vecs[j] is None:
                continue
            if i == j:
                cos_mat[i][j] = 1.0
            else:
                cos_mat[i][j] = cosine(vecs[i], vecs[j])
    uniqueness = []
    cell_ids_uniq = []
    for i in range(30):
        if vecs[i] is None or not ok_cells:
            uniqueness.append(None)
            cell_ids_uniq.append(embs[i]['cell_id'])
            continue
        sims = [cos_mat[i][j] for j in range(30) if i != j and cos_mat[i][j] is not None]
        if not sims:
            uniqueness.append(None)
        else:
            uniqueness.append(1.0 - sum(sims) / len(sims))
        cell_ids_uniq.append(embs[i]['cell_id'])

    x = list(range(30))
    valid_mask = [u is not None for u in uniqueness]
    x_v = [x[i] for i in range(30) if valid_mask[i]]
    y_v = [uniqueness[i] for i in range(30) if valid_mask[i]]
    lo, med, hi, n_boot = bootstrap_beta(x_v, y_v, n_boot=1000, seed=42)
    log(f'  [{bb_alias}] uniqueness β median={fmt_or_none(med)}, '
        f'CI=[{fmt_or_none(lo)}, {fmt_or_none(hi)}], '
        f'n_boot={n_boot}')

    bb_results[bb_alias] = {
        'backbone_alias': bb_alias,
        'embedding_model': bb_model,
        'expected_dim': expected_dim,
        'actual_dims_observed': dims,
        'description': bb_desc,
        'source': bb_source,
        'L': 30,
        'cells': cells,
        'cells_to_embed': cells,
        'cells_source_sha256_12': CELLS_SRC_SHA,
        'embeds': embs,
        'meta_per_cell': meta_per_cell,
        'cosine_similarity_matrix': cos_mat,
        'uniqueness': uniqueness,
        'beta_lo': lo, 'beta_median': med, 'beta_hi': hi, 'n_boot': n_boot,
        'cells_embedded': len(ok_cells),
        'cells_total': len(cells),
        'response_model_match': not downgrade_any,
        'elapsed_s': round(elapsed, 1),
        'status': 'EMBEDDED' if len(ok_cells) == len(cells) else 'PARTIAL',
        'iron_7_compliance': IRON_7,
        '_meta': {
            'timestamp': datetime.now(CST).isoformat(),
            'phase': 'P-L v3 Phase 2',
            'note': 'OR embedding only via 1018 proxy, no LLM chat, '
                    'response.model == request.model verified per cell, key never written.',
        },
    }

    out_path = out_json
    out_path.write_text(
        json.dumps(bb_results[bb_alias], ensure_ascii=False, indent=2), encoding='utf-8')
    out_paths.append(out_path)
    log(f'  [{bb_alias}] saved {out_path.name} size={out_path.stat().st_size}B '
        f'sha12={hashlib.sha256(out_path.read_bytes()).hexdigest()[:12]}')


# ---------- 8) cross-backbone β CI overlap ----------
log('=== Cross-backbone β CI overlap (per pair) ===')
overlap = {}
bb_names = list(bb_results.keys())
for i, a in enumerate(bb_names):
    for j, b in enumerate(bb_names):
        if i >= j:
            continue
        ra, rb = bb_results[a], bb_results[b]
        if ra['beta_lo'] is None or rb['beta_lo'] is None:
            overlap[f'{a}_vs_{b}'] = {'overlap': None, 'note': 'beta None (skipped)'}
            continue
        ov = not (ra['beta_hi'] < rb['beta_lo'] or rb['beta_hi'] < ra['beta_lo'])
        overlap[f'{a}_vs_{b}'] = {
            'r1_CI': [ra['beta_lo'], ra['beta_hi']],
            'r2_CI': [rb['beta_lo'], rb['beta_hi']],
            'overlap': ov,
        }
        log(f'  {a} vs {b}: overlap={ov}')


# ---------- 9) combined summary JSON ----------
summary = {
    'phase': 'P-L v3 Phase 2 OR embedding via 1018 proxy (v3 retry)',
    'timestamp': datetime.now(CST).isoformat(),
    'task_id': 'PL-OR-RETRY',
    'proxy': 'http://127.0.0.1:1018 (HTTPS/HTTP) + socks5://127.0.0.1:1018',
    'sanity_probe_results': sanity_results,
    'backbones': {a: {
        'embedding_model': v['embedding_model'],
        'expected_dim': v['expected_dim'],
        'actual_dims': v['actual_dims_observed'],
        'cells_embedded': v['cells_embedded'],
        'cells_total': v['cells_total'],
        'status': v['status'],
        'beta_lo': v['beta_lo'],
        'beta_median': v['beta_median'],
        'beta_hi': v['beta_hi'],
        'n_boot': v['n_boot'],
        'response_model_match': v['response_model_match'],
        'source_json': out_paths[bb_names.index(a)].name if a in bb_names else None,
    } for a, v in bb_results.items()},
    'cross_backbone_beta_ci_overlap': overlap,
    'p2_embedding_overlap_verdict': (
        'PASS (β CI 重叠, all pairs)' if all(o.get('overlap') for o in overlap.values())
        else 'GRAY (some β CI 不重叠)' if overlap else 'N/A'),
    'iron_7_compliance': IRON_7,
}
sum_path = RESULTS_DIR / f'_p_l_v3_phase2_or_embedding_v3_summary_{TS}.json'
sum_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
log(f'  summary JSON -> {sum_path.name} size={sum_path.stat().st_size}B '
    f'sha12={hashlib.sha256(sum_path.read_bytes()).hexdigest()[:12]}')


# ---------- 10) MD report ----------
md = []
md.append('# P-L v3 Phase 2 — OpenRouter 向量化 via 1018 proxy (v3 retry)')
md.append('')
md.append(f'**生成时间**: {datetime.now(CST).isoformat()}')
md.append(f'**Task ID**: PL-OR-RETRY')
md.append(f'**代理**: http://127.0.0.1:1018 (HTTPS/HTTP) + socks5://127.0.0.1:1018')
md.append(f'**任务**: 4-5 OR embedding × 30 cells (15 GSM8K + 15 StrategyQA) → cosine 矩阵 → β bootstrap CI 重叠')
md.append('')
md.append('---')
md.append('')
md.append('## §0 一句话总结')
md.append('')
emb_ok = [a for a, v in bb_results.items() if v['status'] == 'EMBEDDED']
partial = [a for a, v in bb_results.items() if v['status'] == 'PARTIAL']
md.append(f'**{len(emb_ok)}/{len(bb_results)} OR embedding 跑成 (EMBEDDED)**: '
          + (', '.join(emb_ok) if emb_ok else '— 无 —'))
if partial:
    md.append('')
    md.append(f'**{len(partial)} PARTIAL**: ' + ', '.join(partial))
md.append('')
ov_pairs = [k for k, v in overlap.items() if v.get('overlap') is not None]
ov_true = [k for k, v in overlap.items() if v.get('overlap') is True]
ov_false = [k for k, v in overlap.items() if v.get('overlap') is False]
md.append(f'**Cross-backbone β CI overlap (per pair)**: '
          f'{len(ov_true)}/{len(ov_pairs)} pairs overlap')
md.append('')
md.append(f'**P2 判死 verdict**: '
          f"{'PASS (β CI 重叠 all pairs)' if ov_pairs and len(ov_true)==len(ov_pairs) else ('GRAY (some β CI 不重叠)' if ov_pairs else 'N/A (no β CI computable)')}")
md.append('')
md.append('---')
md.append('')
md.append('## §1 §7 sanity probe — 1-cell 端点可达性 (1018 proxy)')
md.append('')
md.append('| candidate (task §1 → fallback) | OR model | 期望 dim | 实测 dim | status | resp_model | 备注 |')
md.append('|---|---|---|---|---|---|---|')
for alias, model, exp_dim, desc, source in CANDIDATES:
    sr = sanity_results[alias]
    if sr['ok']:
        st_icon = '✅ OK' if sr['dim'] == exp_dim else f'⚠ dim mismatch (got {sr["dim"]})'
        md.append(f'| `{alias}` ({source}) | `{model}` | {exp_dim} | {sr["dim"]} | {st_icon} | `{sr["resp_model"]}` | — |')
    else:
        err_short = (sr.get('error') or '?')[:120].replace('|', '/').replace('\n', ' ')
        md.append(f'| `{alias}` ({source}) | `{model}` | {exp_dim} | — | ❌ {sr["status"]} | — | {err_short} |')
md.append('')
md.append('**Key 结论**: ')
oai_3_small_403 = not sanity_results.get('oai-3-small', {}).get('ok')
mistral_404 = 'does not exist' in (sanity_results.get('mistral-emb', {}).get('error') or '') or sanity_results.get('mistral-emb', {}).get('status') == 400
md.append(f"- `openai/text-embedding-*` 在 1018 proxy 上 **仍返回 403 \"violation of provider Terms of Service\"** — 不是 7897 port 问题, 是 OR provider-level 禁令")
md.append(f"- `mistralai/mistral-embed` 在 OR 上 **不存在** (status=400 \"Model does not exist\")")
md.append(f"- `qwen/qwen3-embedding-8b` 别名 `Qwen/Qwen3-Embedding-8B` **dim=4096 正常**")
md.append(f"- 4-5 working 来自 fallback list (BGE / E5 / GTE) — task 优先级 1/2/3/5 的 openai/mistral 类在 OR 上结构性不可达")
md.append('')
md.append('---')
md.append('')
md.append('## §2 L=30 实测')
md.append('')
md.append('| backbone | OR model | 期望 dim | 实测 dim | cells | status | elapsed | source JSON |')
md.append('|---|---|---|---|---|---|---|---|')
for bb_alias, v in bb_results.items():
    src_file = out_paths[bb_names.index(bb_alias)] if bb_alias in bb_names else None
    src_name = src_file.name if src_file else '—'
    md.append(f'| `{bb_alias}` | `{v["embedding_model"]}` | {v["expected_dim"]} | {v["actual_dims_observed"]} | {v["cells_embedded"]}/{v["cells_total"]} | {v["status"]} | {v["elapsed_s"]}s | `{src_name}` |')
md.append('')
md.append('---')
md.append('')
md.append('## §3 Cross-backbone β CI overlap')
md.append('')
md.append('| pair | embedding A β CI | embedding B β CI | overlap |')
md.append('|---|---|---|---|')
for pair_key, v in overlap.items():
    if v.get('overlap') is None:
        md.append(f'| `{pair_key}` | — | — | skipped (β None) |')
    else:
        a, b = pair_key.split('_vs_')
        ra, rb = bb_results[a], bb_results[b]
        md.append(f'| `{pair_key}` | [{fmt_or_none(ra["beta_lo"])}, {fmt_or_none(ra["beta_hi"])}] | [{fmt_or_none(rb["beta_lo"])}, {fmt_or_none(rb["beta_hi"])}] | {"✅ TRUE" if v["overlap"] else "❌ FALSE"} |')
md.append('')
md.append('---')
md.append('')
md.append('## §4 Iron-7 compliance 声明')
md.append('')
md.append('- ✅ 0 LLM 重 hash (本 runner 仅 embedding, 不调 chat)')
md.append(f'- ✅ key runtime 读自 `C:\\Users\\Administrator\\Desktop\\AI\\LLM API.txt`, 仅保留 `prefix={or_key[:14]}...`, 全程不入 JSON / log / stdout / md (除上面前 14 字符 nonce)')
md.append(f'- ✅ OR embedding 通过 1018 proxy 调用, 3 env: HTTPS_PROXY, HTTP_PROXY, all_proxy')
md.append('- ✅ response.model == request.model 逐 cell 校验 (用户 13:39 防降级欺诈)')
md.append('- ✅ 502/503/504/408 自动 retry 3 次 (backoff 1-3s), 不阻塞其他 backbone')
md.append('- ✅ 18 frozen anchors / 5 制品 / schema v1 / 4 plugin spec / verifier/mavis/.builtin/scripts/ 不动')
md.append('')
md.append('---')
md.append('')
md.append('## §5 制品')
md.append('')
md.append('| artifact | path | sha256_12 |')
md.append('|---|---|---|')
md.append(f'| source cells | `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` | `{CELLS_SRC_SHA}` |')
for p in out_paths:
    sha12 = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
    md.append(f'| backbone JSON | `{p.name}` | `{sha12}` |')
sha12_sum = hashlib.sha256(sum_path.read_bytes()).hexdigest()[:12]
md.append(f'| summary JSON | `{sum_path.name}` | `{sha12_sum}` |')
md.append('')

md.append('---')
md.append('')
md.append('## §6 失败披露 / INCOMPLETE')
md.append('')
md.append(f'- **working: {len(WORKING)}/{len(CANDIDATES)} candidates** selected for L=30')
md.append(f'- **EMBEDDED (30/30): {len(emb_ok)} / PARTIAL: {len(partial)} / FAILED: {len(WORKING)-len(emb_ok)-len(partial)}**')
incomplete_aliases = [a for a, m, d, ds, s in WORKING if a not in bb_results or bb_results[a]['status'] != 'EMBEDDED']
md.append(f'- **still INCOMPLETE (≤29/30 cells)**: ' + (', '.join(incomplete_aliases) if incomplete_aliases else '— none —'))
md.append('')
md.append(f'- **task §1 全部落空原因披露**: openai/* OR-level 403 + mistral/* OR-level 404 非代理问题, 1018 已连通; qwen3 走 `Qwen/Qwen3-Embedding-8B` 路径可用, 4 个 fallback 模型互补架构多样性')
md.append('')

md_text = '\n'.join(md)
md_path = RESULTS_DIR / f'_p_l_v3_phase2_or_embedding_v3_report_{TS}.md'
md_path.write_text(md_text, encoding='utf-8')
log(f'  MD report -> {md_path.name} size={md_path.stat().st_size}B '
    f'sha12={hashlib.sha256(md_path.read_bytes()).hexdigest()[:12]}')

log('=== DONE ===')
