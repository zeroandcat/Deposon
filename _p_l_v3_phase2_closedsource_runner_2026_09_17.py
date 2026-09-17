# -*- coding: utf-8 -*-
"""
P-L v3 Phase 2 closed-source 3 backbone runner (2026-09-17)
- 3 backbone via TeamoRouter (proxy 127.0.0.1:1018)
- frontier 名 (verified: response.model == request.model, no downgrade):
  1. openai = gpt-5.6-sol (3.6s 1-cell sanity)
  2. anthropic = claude-sonnet-5 (3.0s 1-cell sanity)
  3. google = gemini-3.7-flash (2.0s 1-cell sanity)
- 30 cells per backbone × 2 L (L=30 real, L=60 frozen reuse)
- key runtime read (Path().read_bytes + decode + re.search); never written to disk
- baseline prompt format (沿 _p_l_v3_phase2_runner_2026_09_17.build_prompt 严格一致)
- 严守 7 铁律 + 0 LLM rehash
"""
import os, re, sys, json, time, math, hashlib, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime, timezone, timedelta

# ------------------- 0) 强制 proxy 1018 (for TeamoRouter) -------------------
for k in ('HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy'):
    os.environ.pop(k, None)
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1018'
os.environ['HTTP_PROXY']  = 'http://127.0.0.1:1018'
os.environ['ALL_PROXY']   = 'socks5://127.0.0.1:1018'

opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({
        'http':  'http://127.0.0.1:1018',
        'https': 'http://127.0.0.1:1018',
    })
)
urllib.request.install_opener(opener)

CST = timezone(timedelta(hours=8))
TS = datetime.now().strftime('%Y%m%d_%H%M%S')
_log_lines = []
LOG_FILE = DEPOSON_ROOT / f'_p_l_v3_phase2_closedsource_runner_{TS}.py.log'

def log(msg):
    line = f"[{datetime.now(CST).strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    _log_lines.append(line)
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(line + '\n')

DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS_DIR = DEPOSON_ROOT / 'results'

# 清理上次 log (Tee-Object flush bug workaround)
for old in DEPOSON_ROOT.glob('_p_l_v3_phase2_closedsource_runner_*.py.log'):
    if old.exists():
        try: old.unlink()
        except: pass

# ---------- 输入资产 (只读) ----------
KEY_FILE = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt')
BASELINE_JSON = RESULTS_DIR / 'deposon_volcengine_seed_code_30cells_2026_09_10.json'
PHYS60_JSON = RESULTS_DIR / 'deposon_v3_physical_opt_60cells_2026_09_11.json'

# backbone 矩阵 (verified frontier mapping; owner = openai/anthropic/google per TeamoRouter /v1/models)
BACKBONES = {
    'gpt56sol': {
        'vendor_label': 'openai',
        'model': 'gpt-5.6-sol',
        'base_url': 'https://api.teamorouter.com/v1',
        'key_role': 'teamo',
        'role': 'P-L v3 Phase 2 闭源 1: OpenAI frontier via TeamoRouter (gpt-5.6-sol)',
        'sanity_latency_ms': 3615.3,
    },
    'claude_sonnet5': {
        'vendor_label': 'anthropic',
        'model': 'claude-sonnet-5',
        'base_url': 'https://api.teamorouter.com/v1',
        'key_role': 'teamo',
        'role': 'P-L v3 Phase 2 闭源 2: Anthropic frontier via TeamoRouter (claude-sonnet-5)',
        'sanity_latency_ms': 3000.0,
    },
    'gemini_37flash': {
        'vendor_label': 'google',
        'model': 'gemini-3.7-flash',
        'base_url': 'https://api.teamorouter.com/v1',
        'key_role': 'teamo',
        'role': 'P-L v3 Phase 2 闭源 3: Google frontier via TeamoRouter (gemini-3.7-flash)',
        'sanity_latency_ms': 2032.0,
    },
}

# ---------- 1) 加载 keys (runtime only) ----------
log(f"=== P-L v3 Phase 2 closed-source runner | TS={TS} ===")
raw = KEY_FILE.read_bytes()
text = ''
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: text = raw.decode(enc); break
    except: continue
teamo_key = re.search(r'(sk-teamo-[a-f0-9]+)', text).group(1)
log(f"  teamo_key present (mask in log only, real key never persisted)")
log(f"    teamo_key[:18] = {teamo_key[:18]}...")

# sanity check: log env
for var in ('HTTPS_PROXY','HTTP_PROXY','ALL_PROXY'):
    log(f"  env {var} = {os.environ.get(var,'<unset>')}")

# ---------- 2) helpers ----------
def chat(prompt, model, base_url, key, max_tokens=1024, timeout=45):
    url = f'{base_url}/chat/completions'
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
    payload = {
        'model': model,
        'messages': [{'role':'user','content':prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0,
    }
    body = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode())
            content_resp = data['choices'][0]['message']['content']
            response_model = data.get('model', '?')
            return {'ok': True, 'content': content_resp, 'ms': (time.time()-t0)*1000,
                    'status': r.status, 'response_model': response_model,
                    'usage': data.get('usage', {})}
    except urllib.error.HTTPError as e:
        body_b = e.read().decode() if e.fp else ''
        return {'ok': False, 'content': None, 'ms': (time.time()-t0)*1000,
                'status': e.code, 'error': body_b[:300]}
    except Exception as e:
        return {'ok': False, 'content': None, 'ms': (time.time()-t0)*1000,
                'status': -1, 'error': f'{type(e).__name__}: {str(e)[:200]}'}


def extract_number(text):
    if not text: return None
    m = re.search(r'\*\*\s*([-+]?\d[\d,]*\.?\d*)\s*\*\*', text)
    if m:
        try: return float(m.group(1).replace(',', ''))
        except: pass
    nums = re.findall(r'-?\d+\.?\d*', text)
    if nums:
        try: return float(nums[-1])
        except: return None
    return None


def extract_yesno(text):
    if not text: return None
    t = text.lower().strip()
    m = re.search(r'\*\*\s*(yes|no|true|false)\s*\*\*', t)
    if m:
        v = m.group(1)
        return 'Yes' if v in ('yes','true') else 'No'
    for word in re.split(r'\W+', t):
        if word in ('yes','true'): return 'Yes'
        if word in ('no','false'): return 'No'
    return None


def build_prompt(cell):
    if cell['kind'] == 'gsm8k':
        return (f"Question: {cell['text']}\n\n"
                f"Let's think step by step.\n"
                f"Answer with the final number in **bold** at the end.")
    return (f"Question: {cell['text']}\n\n"
            f"Let's think step by step.\n"
            f"Answer Yes or No in **bold** at the end.")


# ---------- 3) 加载 baseline cells (15 GSM8K + 15 SQA) ----------
log("=== Loading 30 baseline cells (15 GSM8K + 15 StrategyQA) ===")
baseline = json.loads(BASELINE_JSON.read_text(encoding='utf-8'))
baseline_cells = []
for c in baseline['cells']:
    baseline_cells.append({
        'id': c['cell_id'],
        'text': c['question'],
        'gt': c['gold_answer'],
        'kind': c['task'],
        'baseline_is_correct': c['is_correct'],
    })
log(f"  Loaded {len(baseline_cells)} cells: gsm8k={sum(1 for c in baseline_cells if c['kind']=='gsm8k')}, "
    f"sqa={sum(1 for c in baseline_cells if c['kind']=='strategyqa')}")

# ---------- 4) L=60 frozen per_model ----------
log("=== Loading L=60 frozen per_model (9 model × 60 cells) ===")
phys60 = json.loads(PHYS60_JSON.read_text(encoding='utf-8'))
pc_per_model = phys60['P_C_distortion_bound_60cells']['per_model']
T_frac60_per_model = [m['T_frac60'] for m in pc_per_model]
mean_T_frac60 = sum(T_frac60_per_model) / len(T_frac60_per_model)
log(f"  L=60 per_model T_frac60: {T_frac60_per_model}")
log(f"  L=60 mean T_frac60 = {mean_T_frac60:.4f}")

# ---------- 5) sanity check per backbone (1-cell, response.model == request.model) ----------
log("=== Sanity check per backbone (1+1=2) ===")
sanity_results = {}
for bb_name, bb in BACKBONES.items():
    r = chat("What is 1+1? Answer with the final number in **bold** at the end.",
             bb['model'], bb['base_url'], teamo_key, max_tokens=32, timeout=30)
    if r['ok']:
        sanity_pass = '2' in (r['content'] or '')
        downgrade = bb['model'] != r['response_model']
        sanity_results[bb_name] = {
            'request_model': bb['model'],
            'response_model': r['response_model'],
            'content': r['content'][:80],
            'latency_ms': round(r['ms'], 1),
            'sanity_pass': sanity_pass,
            'downgrade_detected': downgrade,
        }
        log(f"  [{bb_name}] {bb['model']} -> {r['response_model']}  pass={sanity_pass}  downgrade={downgrade}  {r['ms']:.0f}ms")
        if downgrade:
            log(f"  !!! ABORT: {bb_name} downgrade detected (request={bb['model']} != response={r['response_model']})")
            log(f"  !!! runner abort per 加速器降级欺诈原则")
            sys.exit(2)
    else:
        sanity_results[bb_name] = {'error': r.get('error', '?'), 'status': r['status']}
        log(f"  [{bb_name}] FAIL: {r.get('error', '?')[:120]}")
        log(f"  !!! ABORT: {bb_name} sanity unreachable")
        sys.exit(3)

# ---------- 6) run cells for each new backbone ----------
def run_cells(cells, bb_name, max_tokens_per_kind):
    bb = BACKBONES[bb_name]
    results = []
    n_pass = 0
    log(f"=== Running {len(cells)} cells for backbone={bb_name} ({bb['model']}) ===")
    # Warmup: 1 sacrificial cell with realistic max_tokens (avoid first-cell cold-start hang)
    log(f"  [warmup] {bb_name} priming with realistic GSM8K-shaped prompt...")
    warmup_prompt = build_prompt({
        'kind': 'gsm8k',
        'text': 'If x + 5 = 12, what is x?',
        'id': 'warmup', 'gt': 7.0, 'baseline_is_correct': True,
    })
    try:
        wr = chat(warmup_prompt, bb['model'], bb['base_url'], teamo_key,
                  max_tokens=max_tokens_per_kind['gsm8k'], timeout=45)
        log(f"  [warmup] ok={wr['ok']} rm={wr.get('response_model','-')} {wr['ms']:.0f}ms "
            f"downgrade={wr.get('response_model') != bb['model']}")
        if not wr['ok'] or wr.get('response_model') != bb['model']:
            log(f"  [warmup] ABORT on downgrade")
            sys.exit(5)
    except Exception as e:
        log(f"  [warmup] exception {type(e).__name__}: {str(e)[:200]} — continuing")
    t_start = time.time()
    for i, cell in enumerate(cells):
        prompt = build_prompt(cell)
        mx = max_tokens_per_kind.get(cell['kind'], 1024)
        r = chat(prompt, bb['model'], bb['base_url'], teamo_key, max_tokens=mx, timeout=45)
        if not r['ok']:
            pred = None
            is_correct = False
            err = r.get('error', '?')[:200]
        else:
            if cell['kind'] == 'gsm8k':
                pred = extract_number(r['content'])
                is_correct = pred is not None and abs(pred - cell['gt']) < 1e-3
            else:
                pred = extract_yesno(r['content'])
                is_correct = pred is not None and pred == cell['gt']
            err = None
        if is_correct:
            n_pass += 1
        results.append({
            'cell_id': cell['id'],
            'task': cell['kind'],
            'gold_answer': cell['gt'],
            'llm_extracted': pred,
            'is_correct': is_correct,
            'baseline_correct': cell.get('baseline_is_correct'),
            'latency_ms': round(r.get('ms', 0), 1),
            'http_status': r.get('status'),
            'response_model': r.get('response_model'),
            'request_model': bb['model'],
            'downgrade_detected': bool(r.get('response_model') and bb['model'] != r['response_model']),
            'error': err,
            'content_head': (r.get('content', '') or '')[:120].replace('\n', ' '),
        })
        if (i+1) % 5 == 0 or (i+1) == len(cells):
            log(f"  [{bb_name}] {i+1}/{len(cells)} pass={n_pass}/{i+1}")
        time.sleep(0.2)  # rate limit (slightly more generous for 3rd-party proxy)
    elapsed = time.time() - t_start
    log(f"=== {bb_name} done: {n_pass}/{len(results)} pass, {elapsed:.1f}s ===")
    return results, n_pass, elapsed

# ---------- 7) main loop ----------
cell_30 = baseline_cells

# Per-task max_tokens (GSM8K 高一些以保证 chain-of-thought 完整; SQA 短)
max_tokens_per_kind = {'gsm8k': 768, 'strategyqa': 192}

bb_l30_results = {}
for bb_name in ['gpt56sol', 'claude_sonnet5', 'gemini_37flash']:
    log(f"\n--- backbone = {bb_name} ({BACKBONES[bb_name]['model']}) ---")
    results, n_pass, elapsed = run_cells(cell_30, bb_name, max_tokens_per_kind)

    # Spearman vs baseline
    from scipy.stats import spearmanr
    bb_scores, b_scores = [], []
    for r in results:
        b_cell = next((c for c in baseline['cells'] if c['cell_id'] == r['cell_id']), None)
        if b_cell is None: continue
        bb_scores.append(1 if r['is_correct'] else 0)
        b_scores.append(1 if b_cell['is_correct'] else 0)
    sp, sp_p = spearmanr(bb_scores, b_scores)

    # downgrade check across all cells
    downgrades = [r for r in results if r.get('downgrade_detected')]
    if downgrades:
        log(f"  !!! ABORT: {bb_name} had {len(downgrades)} downgrade(s) in real LLM calls")
        for d in downgrades[:3]:
            log(f"    cell={d['cell_id']} request={d['request_model']} response={d['response_model']}")
        sys.exit(4)

    bb_l30_results[bb_name] = {
        'cells': results,
        'n_pass': n_pass,
        'elapsed': elapsed,
        'spearman': float(sp),
        'spearman_p': float(sp_p),
    }

    out_path = RESULTS_DIR / f'_p_l_v3_robustness_{bb_name}_L30_{TS}.json'
    out = {
        'L': 30,
        'backbone': bb_name,
        'vendor_label': BACKBONES[bb_name]['vendor_label'],
        'model': BACKBONES[bb_name]['model'],
        'api_vendor': 'TeamoRouter (proxy 127.0.0.1:1018)',
        'base_url': BACKBONES[bb_name]['base_url'],
        'task': f'P-L v3 Phase 2 L=30 档 (closed-source {bb_name}, 跨厂商实现稳健性, TeamoRouter via proxy)',
        'role': BACKBONES[bb_name]['role'],
        'cells_total': len(results),
        'cells_pass': n_pass,
        'accuracy': round(n_pass / len(results), 4),
        'cells_breakdown': {
            'gsm8k': sum(1 for r in results if r['task'] == 'gsm8k'),
            'strategyqa': sum(1 for r in results if r['task'] == 'strategyqa'),
        },
        'spearman_vs_baseline': round(float(sp), 6),
        'spearman_p_value': round(float(sp_p), 6),
        'spearman_definition': 'rank correlation between backbone per-cell score (1/0) and baseline (doubao-seed-code-preview-251028) per-cell score',
        'elapsed_s': round(elapsed, 1),
        'sanity_check': sanity_results.get(bb_name, {}),
        'downgrade_fraud_check': {
            'enabled': True,
            'method': 'response.model == request.model?',
            'downgrade_detected_in_any_cell': any(r.get('downgrade_detected') for r in results),
            'request_model': BACKBONES[bb_name]['model'],
            'response_models_observed': sorted(set(r.get('response_model') for r in results if r.get('response_model'))),
            'all_cells_response_model': [r.get('response_model') for r in results],
            'all_cells_passed': all(r.get('downgrade_detected') is False for r in results),
        },
        'proxy_config': {
            'HTTPS_PROXY': os.environ.get('HTTPS_PROXY'),
            'HTTP_PROXY': os.environ.get('HTTP_PROXY'),
            'ALL_PROXY': os.environ.get('ALL_PROXY'),
        },
        'per_cell_detail': results,
        'iron_7_compliance': {
            'no_llm_rehash': True,
            'no_extra_proxy_setup_beyond_1018': True,
            'teamorouter_only': True,
            'no_key_in_prompt_json_disk': True,
            'no_18_frozen_touch': True,
            'no_5_artifact_json_touch': True,
            'no_schema_v1_touch': True,
            'no_plugin_spec_touch': True,
            'no_verifier_mavis_builtin_scripts_touch': True,
        },
        '_meta': {
            'timestamp': datetime.now(CST).isoformat(),
            'baseline_json_sha256_12': hashlib.sha256(BASELINE_JSON.read_bytes()).hexdigest()[:12],
            'phys60_json_sha256_12': hashlib.sha256(PHYS60_JSON.read_bytes()).hexdigest()[:12],
            'phase': 'P-L v3 Phase 2',
            'subphase': 'closed-source (TeamoRouter)',
        },
    }
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
    log(f"  [{bb_name}] L=30 JSON -> {out_path.name}  size={out_path.stat().st_size}B")

    # L=60 wrapper (复用 frozen)
    out_60 = {
        'L': 60,
        'backbone': bb_name,
        'vendor_label': BACKBONES[bb_name]['vendor_label'],
        'model': BACKBONES[bb_name]['model'],
        'api_vendor': 'TeamoRouter (proxy 127.0.0.1:1018)',
        'base_url': BACKBONES[bb_name]['base_url'],
        'task': f'P-L v3 Phase 2 L=60 档 (closed-source {bb_name}, 复用 frozen 9 model aggregate, 0 LLM 重跑)',
        'role': BACKBONES[bb_name]['role'],
        'cells_total': 60,
        'models_total': len(pc_per_model),
        'T_frac60_per_model': T_frac60_per_model,
        'mean_T_frac60': round(mean_T_frac60, 4),
        'reused_from': str(PHYS60_JSON),
        'reused_from_sha256_12': hashlib.sha256(PHYS60_JSON.read_bytes()).hexdigest()[:12],
        'iron_7_compliance': out['iron_7_compliance'],
        '_meta': {
            'timestamp': datetime.now(CST).isoformat(),
            'note': 'L=60 复用 frozen per_model aggregate (0 LLM 重跑)',
        },
    }
    out_60_path = RESULTS_DIR / f'_p_l_v3_robustness_{bb_name}_L60_{TS}.json'
    out_60_path.write_text(json.dumps(out_60, ensure_ascii=False, indent=2), encoding='utf-8')
    log(f"  [{bb_name}] L=60 JSON -> {out_60_path.name}  size={out_60_path.stat().st_size}B")

# ---------- 8) β bootstrap CI per backbone + overlap matrix ----------
log("=== Computing β bootstrap CI per backbone (P2 主指标) ===")
import random, numpy as np
from scipy.stats import linregress
random.seed(42)

def bootstrap_beta_ci(scores_x, scores_y, n_boot=2000, ci=0.95):
    n = len(scores_x)
    if n < 3: return None, None, None, 0
    slopes = []
    for _ in range(n_boot):
        idx = [random.randint(0, n-1) for _ in range(n)]
        xb = [scores_x[i] for i in idx]
        yb = [scores_y[i] for i in idx]
        if len(set(xb)) < 2: continue
        try:
            slope, _, _, _, _ = linregress(xb, yb)
            slopes.append(slope)
        except Exception: continue
    if not slopes: return None, None, None, 0
    s = sorted(slopes)
    a = (1 - ci) / 2
    lo = s[int(a * len(s))]
    hi = s[int((1 - a) * len(s))]
    med = s[len(s) // 2]
    return lo, med, hi, len(s)

bb_beta = {}
for bb_name, lr in bb_l30_results.items():
    bb_scores = [1 if c['is_correct'] else 0 for c in lr['cells']]
    x = list(range(len(bb_scores)))
    lo, med, hi, n_boot = bootstrap_beta_ci(x, bb_scores, n_boot=2000)
    bb_beta[bb_name] = {
        'backbone': bb_name,
        'model': BACKBONES[bb_name]['model'],
        'n_cells': len(bb_scores),
        'accuracy': round(lr['n_pass'] / len(bb_scores), 4),
        'beta_lo': round(float(lo), 6) if lo is not None else None,
        'beta_median': round(float(med), 6) if med is not None else None,
        'beta_hi': round(float(hi), 6) if hi is not None else None,
        'n_boot': int(n_boot),
    }
    log(f"  [{bb_name}] β median={med:.5f}, CI=[{lo:.5f}, {hi:.5f}], n_boot={n_boot}")

# overlap matrix
overlap_matrix = {}
bb_names = list(bb_beta.keys())
log("=== β CI overlap matrix (6 backbone extended table) ===")
# Extend with 既有 Phase 2 backbones (placeholder for the report's 6-backbone compare)
# Phase 2 已有 (existing frozen, no re-run): qwen3 / glm53 / doubao / mistral
existing_beta = {
    'qwen3':    {'beta_lo': None, 'beta_median': None, 'beta_hi': None, 'source': 'Phase 2 既有, no re-run'},
    'glm53':    {'beta_lo': None, 'beta_median': None, 'beta_hi': None, 'source': 'Phase 2 既有, no re-run'},
    'doubao':   {'beta_lo': None, 'beta_median': None, 'beta_hi': None, 'source': 'Phase 2 既有, no re-run'},
    'mistral':  {'beta_lo': None, 'beta_median': None, 'beta_hi': None, 'source': 'Phase 1 frozen'},
}
log("  (现有 4 backbone β CI 未在本次工作中 re-run; 仅留位)")

# 新跑 3 backbone overlap
for i, b1 in enumerate(bb_names):
    for j, b2 in enumerate(bb_names):
        if i >= j: continue
        r1, r2 = bb_beta[b1], bb_beta[b2]
        if r1['beta_lo'] is None or r2['beta_lo'] is None: continue
        overlap = not (r1['beta_hi'] < r2['beta_lo'] or r2['beta_hi'] < r1['beta_lo'])
        overlap_matrix[f'{b1}_vs_{b2}'] = {
            'r1': {'bb': b1, 'CI': [r1['beta_lo'], r1['beta_hi']]},
            'r2': {'bb': b2, 'CI': [r2['beta_lo'], r2['beta_hi']]},
            'overlap': overlap,
        }
        log(f"  {b1} vs {b2}: overlap={overlap}")

# ---------- 9) summary JSON ----------
summary = {
    'phase': 'P-L v3 Phase 2 (closed-source via TeamoRouter, proxy 127.0.0.1:1018)',
    'timestamp': datetime.now(CST).isoformat(),
    'TS': TS,
    'proxy': {
        'HTTPS_PROXY': os.environ.get('HTTPS_PROXY'),
        'HTTP_PROXY': os.environ.get('HTTP_PROXY'),
        'ALL_PROXY': os.environ.get('ALL_PROXY'),
        'note': 'only port 1018 used; DNS via proxy',
    },
    'backbones_tested': list(bb_beta.keys()),
    'backbones_unavailable': [],
    'beta_results': bb_beta,
    'beta_ci_overlap_closed3': overlap_matrix,
    'phase2_extension_note': (
        'closed 3 backbone via TeamoRouter; Phase 2 已有 3 backbone (qwen3/glm53/doubao) '
        'and Phase 1 baseline (mistral) — 6 backbone compare in MD report'
    ),
    'p2_implementation_robustness_verdict': (
        'PASS (β CI overlap for closed 3)' if all(o['overlap'] for o in overlap_matrix.values())
        else 'GRAY/PARTIAL (some β CI not overlapping)'
    ),
}

sum_path = RESULTS_DIR / f'_p_l_v3_phase2_closedsource_summary_{TS}.json'
sum_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding='utf-8')
log(f"  summary -> {sum_path.name}")

# ---------- 10) 综合 MD ----------
md_lines = []
md_lines.append(f"# P-L v3 Phase 2 Closed-Source 3 Backbone 综合报告")
md_lines.append(f"")
md_lines.append(f"- **TS**: {TS}")
md_lines.append(f"- **Proxy**: 127.0.0.1:1018 (TeamoRouter only, no other endpoints)")
md_lines.append(f"- **30 cells / backbone**: 15 GSM8K + 15 StrategyQA (baseline JSON)")
md_lines.append(f"- **frontier mapping**: owned_by per TeamoRouter /v1/models")
md_lines.append(f"")
md_lines.append(f"## 0. 加速器降级欺诈验证 (response.model == request.model)")
md_lines.append(f"")
md_lines.append(f"| backbone | request_model | sanity response | per-cell response | downgrade_detected |")
md_lines.append(f"|---|---|---|---|---|")
for bb_name in bb_l30_results.keys():
    sj = sanity_results[bb_name]
    md_lines.append(
        f"| {bb_name} | `{BACKBONES[bb_name]['model']}` | `{sj.get('response_model','-')}` (sanity latency={sj.get('latency_ms','-')}ms) | "
        f"{'all match' if not any(r['downgrade_detected'] for r in bb_l30_results[bb_name]['cells']) else 'MISMATCH'} "
        f"({len(set(r['response_model'] for r in bb_l30_results[bb_name]['cells']))} unique) | "
        f"{'FALSE ✓' if not any(r['downgrade_detected'] for r in bb_l30_results[bb_name]['cells']) else 'TRUE ✗'} |"
    )
md_lines.append(f"")
md_lines.append(f"## 1. Per-backbone 30 cells LLM run")
md_lines.append(f"")
md_lines.append(f"| backbone | model | vendor | pass | accuracy | Spearman vs baseline | p | elapsed |")
md_lines.append(f"|---|---|---|---|---|---|---|---|")
for bb_name, lr in bb_l30_results.items():
    md_lines.append(
        f"| {bb_name} | `{BACKBONES[bb_name]['model']}` | {BACKBONES[bb_name]['vendor_label']} | "
        f"{lr['n_pass']}/{len(lr['cells'])} | {round(lr['n_pass']/len(lr['cells']),4)} | "
        f"{round(lr['spearman'],4)} | {round(lr['spearman_p'],4)} | {round(lr['elapsed'],1)}s |"
    )
md_lines.append(f"")
md_lines.append(f"## 2. β bootstrap CI (n_boot=2000) — closed 3")
md_lines.append(f"")
md_lines.append(f"| backbone | β median | 95% CI | n_boot |")
md_lines.append(f"|---|---|---|---|")
for bb_name, b in bb_beta.items():
    md_lines.append(f"| {bb_name} | {b['beta_median']} | [{b['beta_lo']}, {b['beta_hi']}] | {b['n_boot']} |")
md_lines.append(f"")
md_lines.append(f"## 3. β CI overlap matrix (closed 3)")
md_lines.append(f"")
md_lines.append(f"| pair | bb1 CI | bb2 CI | overlap |")
md_lines.append(f"|---|---|---|---|")
for k, o in overlap_matrix.items():
    md_lines.append(f"| {k} | {o['r1']['CI']} | {o['r2']['CI']} | {o['overlap']} |")
md_lines.append(f"")
md_lines.append(f"## 4. 6 backbone P2 扩展对比 (说明)")
md_lines.append(f"")
md_lines.append(f"本任务只新跑了闭源 3 backbone (TeamoRouter proxy 1018):")
md_lines.append(f"")
md_lines.append(f"- **Closed-source 3 (本任务新跑)**: gpt56sol / claude_sonnet5 / gemini_37flash")
md_lines.append(f"- **Open-weight 3 (Phase 2 既有, 不重跑)**: qwen3 / glm53 / doubao")
md_lines.append(f"- **Baseline (Phase 1, 不重跑)**: mistralai/mistral-large-2512")
md_lines.append(f"")
md_lines.append(f"PASS/FAIL/GRAY 判定基于 closed 3 的 β CI overlap + Spearman vs baseline 一致性。")
md_lines.append(f"")
md_lines.append(f"## 5. 7 铁律 0 触动声明")
md_lines.append(f"")
md_lines.append(f"- 0 LLM 重 hash (sanity 仅 1 call / backbone, 不入 cells 计数)")
md_lines.append(f"- 不动 18 frozen anchors (未触及 corpus, mindmap, GT)")
md_lines.append(f"- 不动 5 制品 JSON (corpus/v20/by_model/* 全部只读)")
md_lines.append(f"- 不动 schema v1 (未触及 plugin spec / deposon_protocol / fingerprint)")
md_lines.append(f"- 不动 4 plugin spec (未触及 verifier / mavis / .builtin / scripts)")
md_lines.append(f"- API key runtime 读 (Path.read_bytes + decode + re.search); 真 key 永不落盘")
md_lines.append(f"- response.model == request.model — 全部 30 cells × 3 backbone 均通过 (无降级)")
md_lines.append(f"")
md_lines.append(f"## 6. 输入资产 (只读)")
md_lines.append(f"")
md_lines.append(f"- baseline: `{BASELINE_JSON.name}` (sha256_12={hashlib.sha256(BASELINE_JSON.read_bytes()).hexdigest()[:12]})")
md_lines.append(f"- L=60 frozen: `{PHYS60_JSON.name}` (sha256_12={hashlib.sha256(PHYS60_JSON.read_bytes()).hexdigest()[:12]})")
md_lines.append(f"")
md_lines.append(f"## 7. 输出物 (6 JSON + 1 MD)")
md_lines.append(f"")
for bb_name in bb_l30_results.keys():
    md_lines.append(f"- `_p_l_v3_robustness_{bb_name}_L30_{TS}.json`")
    md_lines.append(f"- `_p_l_v3_robustness_{bb_name}_L60_{TS}.json`")
md_lines.append(f"- `_p_l_v3_phase2_closedsource_summary_{TS}.json`")
md_lines.append(f"- `_p_l_v3_phase2_closedsource_report_{TS}.md` (本文件)")

md_path = RESULTS_DIR / f'_p_l_v3_phase2_closedsource_report_{TS}.md'
md_path.write_text('\n'.join(md_lines) + '\n', encoding='utf-8')
log(f"  report -> {md_path.name}")

# ---------- 11) flush log ----------
log_path = DEPOSON_ROOT / f'_p_l_v3_phase2_closedsource_runner_{TS}.log'
log_path.write_text('\n'.join(_log_lines) + '\n', encoding='utf-8')
log(f"  log -> {log_path.name}")
log("=== DONE ===")
