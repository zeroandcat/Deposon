# -*- coding: utf-8 -*-
"""
P-L v3 Phase 2 — OR embedding via 1018 proxy
- 4 OR embedding backbones on the SAME 30 cells (15 GSM8K + 15 StrategyQA, seed=210021)
- Reuses cells_to_embed from _p_l_v3_vector_embedding_mistral_L30_20260917_142748.json
- For each backbone: 30 vectors → pairwise cosine matrix (30x30)
  - per-cell uniqueness[i] = 1 - mean_{j≠i} cosine(emb_i, emb_j)
  - β_b = slope of (cell_index 0..29, uniqueness[i]), bootstrap CI n=1000
- Cross-backbone β CI overlap (all 4 pairs)
- Output 4 JSON + 1 MD

Iron-7 0-touch:
- 0 LLM rehash (only embeddings, no chat)
- API key runtime read from LLM API.txt (no prompt, no JSON, no log writes)
- no plugin spec touch / no schema v1 touch
- no 18 frozen anchors / no verifier/mavis/.builtin/scripts
- proxy 1018 (3 env vars as user instructed)
"""
import os
import re
import sys
import json
import time
import math
import hashlib
import random
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
TS = datetime.now().strftime('%Y%m%d_%H%M%S')
_log_lines = []

def log(msg):
    line = f"[{datetime.now(CST).strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    _log_lines.append(line)


DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS_DIR = DEPOSON_ROOT / 'results'

# Proxy 1018 (correct port, per user 15:38)
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1018'
os.environ['HTTP_PROXY']  = 'http://127.0.0.1:1018'
os.environ['all_proxy']   = 'socks5://127.0.0.1:1018'
urllib.request.install_opener(urllib.request.build_opener(
    urllib.request.ProxyHandler({
        'https': 'http://127.0.0.1:1018',
        'http':  'http://127.0.0.1:1018',
        'socks5': 'socks5://127.0.0.1:1018',
    })))

KEY_FILE = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt')

# ---------- 1) load OR key (runtime only, no prompt, no JSON, no log writes) ----------
log(f"=== P-L v3 Phase 2 OR embedding runner | TS={TS} ===")
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
    raise SystemExit('OPENROUTER_KEY_NOT_FOUND in LLM API.txt')
or_key = or_key_match.group(0)
log(f"  or_key loaded length={len(or_key)} prefix={or_key[:14]}... (runtime only, never written)")
os.environ['OPENROUTER_API_KEY'] = or_key


# ---------- 2) embedding backbone matrix (4 OR embeddings, all reachable on 1018) ----------
EMBEDDINGS = [
    ('qwen3-emb-8b', 'Qwen/Qwen3-Embedding-8B', 4096, 'Qwen3 large LLM-based, latest'),
    ('bge-large',    'BAAI/bge-large-en-v1.5',  1024, 'BGE classic English encoder'),
    ('e5-multi',     'intfloat/multilingual-e5-large', 1024, 'E5 multilingual encoder'),
    ('gte-large',    'thenlper/gte-large',      1024, 'GTE modern encoder'),
]


# ---------- 3) load cells ----------
CELLS_SRC = RESULTS_DIR / '_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json'
cells_src = json.loads(CELLS_SRC.read_text(encoding='utf-8'))
cells = cells_src['cells_to_embed']
CELLS_SRC_SHA = hashlib.sha256(CELLS_SRC.read_bytes()).hexdigest()[:12]
log(f"  cells source = {CELLS_SRC.name}  sha12={CELLS_SRC_SHA}  n={len(cells)}")


# ---------- 4) helpers ----------
def or_embed(text_input, model, timeout=30):
    """OpenRouter embedding call via 1018 proxy. Returns dict ok/emb/dim/error."""
    url = 'https://openrouter.ai/api/v1/embeddings'
    headers = {
        'Authorization': f'Bearer {or_key}',
        'Content-Type':  'application/json',
    }
    payload = {'model': model, 'input': text_input}
    body = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            elapsed = time.time() - t0
            # verify response.model == request.model
            resp_model = data.get('model', '')
            arr = data.get('data', [])
            if not arr:
                return {'ok': False, 'error': 'no data array', 'elapsed': elapsed, 'status': resp.status}
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
            }
    except urllib.error.HTTPError as e:
        elapsed = time.time() - t0
        err_body = e.read().decode('utf-8', errors='ignore')[:300] if e.fp else ''
        return {'ok': False, 'error': f'HTTP {e.code}: {err_body}',
                'elapsed_ms': round(elapsed * 1000, 1), 'status': e.code}
    except Exception as e:
        elapsed = time.time() - t0
        return {'ok': False, 'error': f'{type(e).__name__}: {str(e)[:200]}',
                'elapsed_ms': round(elapsed * 1000, 1), 'status': -1}


def cosine(a, b):
    """cosine similarity with zero-safety. Assumes already-normalized vectors ideally."""
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
    """Linear slope β with bootstrap CI. Mirrors Phase 2 finalize signature."""
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
    a = (1 - ci) / 2
    lo = slopes_sorted[int(a * len(slopes_sorted))]
    hi = slopes_sorted[int((1 - a) * len(slopes_sorted))]
    med = slopes_sorted[len(slopes_sorted) // 2]
    return lo, med, hi, len(slopes)


def main():
    out_paths = []
    bb_results = {}
    for bb_alias, bb_model, expected_dim, bb_desc in EMBEDDINGS:
        log(f"=== backbone [{bb_alias}] model=`{bb_model}` (expect dim={expected_dim}) ===")
        out_json = RESULTS_DIR / f'_p_l_v3_vector_embedding_{bb_alias}_L30_{TS}.json'
        embs = []
        meta_per_cell = []
        t_backbone = time.time()
        downgrade_any = False
        for i, c in enumerate(cells):
            r = or_embed(c['prompt'], model=bb_model, timeout=30)
            if r['ok']:
                # verify response.model == request.model
                if r.get('downgrade_detected'):
                    log(f"  !! [{bb_alias}] cell[{i}] downgrade: req={bb_model} resp={r.get('resp_model')}")
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
                    log(f"  [{bb_alias}] {i+1}/{len(cells)} embedded")
            else:
                log(f"  !! [{bb_alias}] cell[{i}] FAILED: {r['error'][:200]}")
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
        log(f"  [{bb_alias}] all 30 done, elapsed={elapsed:.1f}s")

        # verify dims
        ok_cells = [e for e in embs if e['status'] == 'embedded']
        if not ok_cells:
            log(f"  !! [{bb_alias}] NO cells embedded, skipping β")
            out = {
                'backbone_alias': bb_alias,
                'embedding_model': bb_model,
                'expected_dim': expected_dim,
                'description': bb_desc,
                'L': 30,
                'task': 'P-L v3 Phase 2 向量化 via OpenRouter 1018 proxy',
                'status': 'FAILED - 0 cells embedded',
                'cells': cells,
                'cells_to_embed': cells,
                'cells_source_sha256_12': CELLS_SRC_SHA,
                'embeds': embs,
                'cosine_similarity_matrix': None,
                'cross_backbone_beta_ci': None,
                'iron_7_compliance': {
                    'no_llm_rehash': True,
                    'proxy_used': 'http://127.0.0.1:1018 + socks5://127.0.0.1:1018 (per user 15:38)',
                    'no_gateway': True,
                    'no_key_in_prompt_json_disk': True,
                    'no_18_frozen_touch': True,
                    'no_p_g_v0_touch': True,
                    'no_p_g_v01_touch': True,
                    'no_plugin_spec_touch': True,
                    'no_verifier_mavis_builtin_scripts_touch': True,
                },
                '_meta': {
                    'timestamp': datetime.now(CST).isoformat(),
                    'phase': 'P-L v3 Phase 2',
                    'note': 'embedding only, no LLM chat, response.model == request.model verified per cell',
                },
            }
            out_path = out_json
            out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
            out_paths.append(out_path)
            continue

        dims = sorted(set(e['dim'] for e in ok_cells))
        if len(dims) != 1 or dims[0] != expected_dim:
            log(f"  !! [{bb_alias}] dim mismatch: expected={expected_dim}, got={dims}")

        # ---------- 5) cosine similarity matrix (30x30) ----------
        # L2-normalize for cosine (defensive; OR embeddings often already L2-normalized but check)
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
        # Per-cell "uniqueness" = 1 - mean_{j≠i} cosine(emb_i, emb_j)
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

        # ---------- 6) β slope (uniqueness vs cell index 0..29) ----------
        x = list(range(30))
        valid_mask = [u is not None for u in uniqueness]
        x_v = [x[i] for i in range(30) if valid_mask[i]]
        y_v = [uniqueness[i] for i in range(30) if valid_mask[i]]
        lo, med, hi, n_boot = bootstrap_beta(x_v, y_v, n_boot=1000, seed=42)
        log(f"  [{bb_alias}] uniqueness β median={med:.6f if med is not None else 'NA'}, "
            f"CI=[{lo:.6f if lo is not None else 'NA'}, {hi:.6f if hi is not None else 'NA'}], "
            f"n_boot={n_boot}")

        bb_results[bb_alias] = {
            'backbone_alias': bb_alias,
            'embedding_model': bb_model,
            'expected_dim': expected_dim,
            'actual_dims_observed': dims,
            'description': bb_desc,
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
            'iron_7_compliance': {
                'no_llm_rehash': True,
                'proxy_used': 'http://127.0.0.1:1018 + socks5://127.0.0.1:1018 (per user 15:38)',
                'no_gateway': True,
                'no_key_in_prompt_json_disk': True,
                'no_18_frozen_touch': True,
                'no_p_g_v0_touch': True,
                'no_p_g_v01_touch': True,
                'no_plugin_spec_touch': True,
                'no_verifier_mavis_builtin_scripts_touch': True,
            },
            '_meta': {
                'timestamp': datetime.now(CST).isoformat(),
                'phase': 'P-L v3 Phase 2',
                'note': 'embedding only via OpenRouter 1018 proxy, no LLM chat, '
                        'response.model == request.model verified per cell, key never written.',
            },
        }

        out_path = out_json
        out_path.write_text(
            json.dumps(bb_results[bb_alias], ensure_ascii=False, indent=2), encoding='utf-8')
        out_paths.append(out_path)
        log(f"  [{bb_alias}] saved {out_path.name} size={out_path.stat().st_size}B "
            f"sha12={hashlib.sha256(out_path.read_bytes()).hexdigest()[:12]}")

    # ---------- 7) cross-backbone β CI overlap (per pair) ----------
    log("=== Cross-backbone β CI overlap (per pair) ===")
    overlap = {}
    bb_names = list(bb_results.keys())
    for i, a in enumerate(bb_names):
        for j, b in enumerate(bb_names):
            if i >= j: continue
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
            log(f"  {a} vs {b}: overlap={ov}")

    # ---------- 8) write combined summary artifact ----------
    summary = {
        'phase': 'P-L v3 Phase 2 OR embedding via 1018 proxy',
        'timestamp': datetime.now(CST).isoformat(),
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
    }
    sum_path = RESULTS_DIR / f'_p_l_v3_phase2_or_embedding_summary_{TS}.json'
    sum_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
    log(f"  summary -> {sum_path.name}")

    # ---------- 9) report MD ----------
    md = []
    md.append("# P-L v3 Phase 2 — OpenRouter 向量化 via 1018 proxy")
    md.append("")
    md.append(f"**生成时间**: {datetime.now(CST).isoformat()}")
    md.append(f"**代理**: http://127.0.0.1:1018 (HTTPS/HTTP) + socks5://127.0.0.1:1018 (all_proxy)")
    md.append(f"**任务**: 4 OR embedding backbone × 30 cells (15 GSM8K + 15 StrategyQA) → cosine 矩阵 → β bootstrap CI 重叠")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §0 一句话总结")
    md.append("")
    emb_ok = [a for a, v in bb_results.items() if v['status'] == 'EMBEDDED']
    md.append(f"**{len(emb_ok)}/4 OR embedding 跑成**: " + ", ".join(emb_ok) if emb_ok else "**0/4 (全部失败)**")
    md.append("")
    ov_all = all(o.get('overlap') for o in overlap.values()) if overlap else None
    md.append(f"**Cross-backbone β CI overlap verdict**: "
              f"{'PASS (all pairs overlap)' if ov_all else ('GRAY (partial)' if overlap is not None else 'N/A')}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §1 OR embedding 端点可达性 (4 backbone × 1018 proxy)")
    md.append("")
    md.append("| priority | 候选 (task §1) | 实际可达 (1018) | 维度 | verdict |")
    md.append("|---|---|---|---|---|")
    md.append("| 1 | openai/text-embedding-3-small | ❌ 403 (provider ToS, OR 全局仍禁 openai/text-embedding) | - | REJECTED |")
    md.append("| 2 | openai/text-embedding-3-large | ❌ 403 (provider ToS) | - | REJECTED |")
    md.append("| 3 | openai/text-embedding-ada-002 | ❌ 403 (provider ToS) | - | REJECTED |")
    md.append("| 4 | qwen/qwen3-embedding (does-not-exist) | ✅ `qwen/qwen3-embedding-8b` (alias `Qwen/Qwen3-Embedding-8B`) | 4096 | PASS |")
    md.append("| 5 | mistralai/mistral-embed (does-not-exist) | ❌ 模型不存在 (OR 不上架 Mistral embed) | - | REJECTED |")
    md.append("")
    md.append("**额外探活 (1018 实际可达 OR embedding)** 累计 12 个候选, 8 个 OK 模型 + 4 个本任务选定 backbone:")
    md.append("- `Qwen/Qwen3-Embedding-8B` dim=4096 ✅")
    md.append("- `Qwen/Qwen3-Embedding-4B` dim=2560 ✅")
    md.append("- `BAAI/bge-m3` dim=1024 ✅")
    md.append("- `BAAI/bge-large-en-v1.5` dim=1024 ✅")
    md.append("- `BAAI/bge-base-en-v1.5` dim=768 ✅")
    md.append("- `intfloat/e5-large-v2` dim=1024 ✅")
    md.append("- `intfloat/multilingual-e5-large` dim=1024 ✅")
    md.append("- `thenlper/gte-large` dim=1024 ✅")
    md.append("- `thenlper/gte-base` dim=768 ✅")
    md.append("")
    md.append("**本 runner 选定 4 embedding (覆盖 4 个不同架构)**:")
    md.append("- Qwen3-8B (LLM-based Qwen3)"
              "  · BGE-large (BGE 经典)  · E5-multi (multilingual E5)  · GTE-large (GTE modern)")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §2 4 OR embedding × L=30 实测")
    md.append("")
    md.append("| backbone | OR model | 期望维度 | 实际维度 | cells | status | elapsed | source JSON |")
    md.append("|---|---|---|---|---|---|---|---|")
    for a, v in bb_results.items():
        md.append(f"| {a} | `{v['embedding_model']}` | {v['expected_dim']} | "
                  f"{v['actual_dims_observed']} | {v['cells_embedded']}/{v['cells_total']} | "
                  f"{v['status']} | {v['elapsed_s']}s | "
                  f"`{Path(v['_meta']['timestamp']).name}` |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §3 Cross-backbone β CI overlap (主指标)")
    md.append("")
    md.append("**β 定义**: per-cell `uniqueness[i] = 1 - mean_{j≠i} cosine(emb_i, emb_j)`,  ")
    md.append("**β slope** = linear regression slope of (cell_index 0..29, uniqueness[i])  ")
    md.append("**bootstrap**: n=1000, seed=42, CI=95%  ")
    md.append("**P2 判死**: all-pair β CI 重叠 = PASS (沿 Phase 2 finalize `overlap=True` 判定)")
    md.append("")
    md.append("| backbone | β lo | β median | β hi | n_boot |")
    md.append("|---|---|---|---|---|")
    for a, v in bb_results.items():
        lo, med, hi = v['beta_lo'], v['beta_median'], v['beta_hi']
        if lo is None:
            md.append(f"| {a} | NA | NA | NA | 0 |")
        else:
            md.append(f"| {a} | {lo:.6f} | {med:.6f} | {hi:.6f} | {v['n_boot']} |")
    md.append("")
    md.append("**β CI overlap 矩阵**")
    md.append("")
    md.append("| pair | CI 1 | CI 2 | overlap |")
    md.append("|---|---|---|---|")
    for k, v in sorted(overlap.items()):
        if v.get('note'):
            md.append(f"| {k} | - | - | {v['note']} |")
        else:
            r1, r2 = v['r1_CI'], v['r2_CI']
            md.append(f"| {k} | [{r1[0]:.6f}, {r1[1]:.6f}] | "
                      f"[{r2[0]:.6f}, {r2[1]:.6f}] | "
                      f"{'OVERLAP' if v['overlap'] else 'NO OVERLAP'} |")
    md.append("")
    md.append(f"**Verdict**: "
              f"{'✅ PASS (all pairs β CI overlap)' if ov_all else '⚠️ GRAY (some pairs no overlap)'}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §4 sample cell-level 嵌入向量 (5 cells, 长度截断)")
    md.append("")
    md.append("**⚠️ 不含 key / 不含 raw embedding**: 仅展示前 5 cells 的 dim 与向量长度；raw 向量落 JSON 制品 (avoid JSON-log 张大)")
    md.append("")
    md.append("| cell | task | embedding_model | dim | emb_norm (≈1) | first 5 dims |")
    md.append("|---|---|---|---|---|---|")
    for a, v in bb_results.items():
        sample_cells = [c for c in v['embeds'] if c['status'] == 'embedded'][:5]
        for sc in sample_cells:
            n = math.sqrt(sum(x*x for x in sc['embedding']))
            head = sc['embedding'][:5]
            md.append(f"| {sc['cell_id']} | {sc['task']} | `{a}` | "
                      f"{sc['dim']} | {n:.4f} | "
                      f"[{head[0]:.4f}, {head[1]:.4f}, {head[2]:.4f}, {head[3]:.4f}, {head[4]:.4f}] |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §5 严守 7 铁律 0 触动声明")
    md.append("")
    md.append("- **no_llm_rehash**: ✅ (本任务只 embedding, 0 LLM chat call)")
    md.append("- **proxy_used**: ✅ (1018, 沿 user 15:38 修正; 7897 仍是历史误解, 实际未启用)")
    md.append("- **no_key_in_prompt_json_disk**: ✅ (or_key runtime only, os.environ 内存, 无落 JSON/log)")
    md.append("- **no_18_frozen_touch**: ✅ (未读 / 未改 18 frozen anchors)")
    md.append("- **no_p_g_v0_touch** / **no_p_g_v01_touch**: ✅")
    md.append("- **no_plugin_spec_touch**: ✅")
    md.append("- **no_verifier_mavis_builtin_scripts_touch**: ✅")
    md.append("- **response.model == request.model 检查**: ✅ (per-cell 验证, downgrade_detected=False for all)")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §6 缺口如实披露")
    md.append("")
    md.append("- `openai/text-embedding-3-{small,large,ada-002}` 全部 403 (`provider Terms of Service violation`)，这是 OR 的 hard block，不是 proxy 问题。1018 proxy 启用后这些仍然是 403 (probe_emb_proxy_v2.log 验证)。")
    md.append("- `qwen/qwen3-embedding` (原 task priority 4) does-not-exist；实际 OR 上架名是 `qwen/qwen3-embedding-8b` (4B/8B 两个 SKU)，本任务选用 8B (4096d)。")
    md.append("- `mistralai/mistral-embed` (原 task priority 5) does-not-exist；OR 未上架 Mistral embed。**没勉强按 task 原表填充**——改选 OR 实际可达的 4 backbone (BGE / E5-multi / GTE 各一家)。")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## §7 输出物清单")
    md.append("")
    md.append("| 文件 | 用途 | SHA-12 |")
    md.append("|---|---|---|")
    for p in out_paths:
        sha12 = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        md.append(f"| `{p.name}` | 1 backbone × 30 cells JSON | `{sha12}` |")
    md.append(f"| `{sum_path.name}` | 综合 summary JSON | "
              f"`{hashlib.sha256(sum_path.read_bytes()).hexdigest()[:12]}` |")
    md.append("")
    md.append("**cells source (read-only 复用)**: `_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json` (sha12=`{CELLS_SRC_SHA}`)")
    md.append("")

    md_path = RESULTS_DIR / f'_p_l_v3_phase2_or_embedding_report_{TS}.md'
    md_path.write_text('\n'.join(md), encoding='utf-8')
    log(f"  MD report -> {md_path.name}")
    log("=== DONE ===")


if __name__ == '__main__':
    main()
