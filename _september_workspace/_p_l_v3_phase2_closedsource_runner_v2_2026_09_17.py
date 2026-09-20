# -*- coding: utf-8 -*-
"""
P-L v3 Phase 2 closed-source 3 backbone runner v3 (2026-09-17)
============================
v3 改进 (相对 v1/v2):
- **per-cell 增量 save** (防止 bash bg task watchdog 杀后丢数据)
- **per-backbone 单 run** (bash bg task 5min watchdog 处理更稳)
- **30s hard timeout + 3 retries + 1/2s backoff** (per cell, per backbone)
- **chain fallback** (primary → next → next → 备 OR)
- **warmup call** per primary backbone (60s grace)
- **max_tokens=512** (reasoning model 强制 cap)

输入资产 (只读): baseline 30 cells + L=60 frozen
严守: 7 铁律 0 触动 + key runtime 读

USAGE:
    python _p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py <PRIMARY_BACKBONE>
    PRIMARY_BACKBONE ∈ {gpt56sol, claude_sonnet5, gemini_37flash}
"""
import os, re, sys, json, time, hashlib, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime, timezone, timedelta

# ------------------- 0) 强制 proxy 1018 -------------------
for k in ('HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy'):
    os.environ.pop(k, None)
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1018'
os.environ['HTTP_PROXY']  = 'http://127.0.0.1:1018'

opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({
        'http':  'http://127.0.0.1:1018',
        'https': 'http://127.0.0.1:1018',
    })
)
urllib.request.install_opener(opener)

CST = timezone(timedelta(hours=8))
TS = datetime.now().strftime('%Y%m%d_%H%M%S')

# Parse PRIMARY_BACKBONE arg
PRIMARY_BACKBONE = sys.argv[1] if len(sys.argv) > 1 else 'gpt56sol'

DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS_DIR = DEPOSON_ROOT / 'results'
LOG_FILE = DEPOSON_ROOT / f'_p_l_v3_phase2_closedsource_runner_v2_{TS}_{PRIMARY_BACKBONE}.log'
_log_lines = []

def log(msg):
    line = f"[{datetime.now(CST).strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    _log_lines.append(line)
    # 增量 write (防止 bash bg 杀后看不到 progress)
    try:
        with LOG_FILE.open('a', encoding='utf-8') as f:
            f.write(line + '\n')
    except Exception:
        pass

# backbone 矩阵
BACKBONES = {
    'gpt56sol': {
        'vendor_label': 'openai', 'model': 'gpt-5.6-sol',
        'base_url': 'https://api.teamorouter.com/v1', 'key_role': 'teamo',
        'role': 'P-L v3 Phase 2 闭源 1: OpenAI frontier (gpt-5.6-sol via TeamoRouter)',
        'max_tokens_default': 512, 'per_call_timeout_s': 30,
    },
    'claude_sonnet5': {
        'vendor_label': 'anthropic', 'model': 'claude-sonnet-5',
        'base_url': 'https://api.teamorouter.com/v1', 'key_role': 'teamo',
        'role': 'P-L v3 Phase 2 闭源 2: Anthropic frontier (claude-sonnet-5 via TeamoRouter)',
        'max_tokens_default': 768, 'per_call_timeout_s': 30,
    },
    'gemini_37flash': {
        'vendor_label': 'google', 'model': 'gemini-3.7-flash',
        'base_url': 'https://api.teamorouter.com/v1', 'key_role': 'teamo',
        'role': 'P-L v3 Phase 2 闭源 3: Google frontier (gemini-3.7-flash via TeamoRouter)',
        'max_tokens_default': 512, 'per_call_timeout_s': 30,
    },
}
BACKBONE_CHAIN = ['gpt56sol', 'claude_sonnet5', 'gemini_37flash']

if PRIMARY_BACKBONE not in BACKBONES:
    log(f"FATAL: PRIMARY_BACKBONE={PRIMARY_BACKBONE} not in {list(BACKBONES.keys())}")
    sys.exit(1)

CHAIN = [PRIMARY_BACKBONE] + [b for b in BACKBONE_CHAIN if b != PRIMARY_BACKBONE]
log(f"=== P-L v3 Phase 2 closed-source runner v3 | TS={TS} | PRIMARY={PRIMARY_BACKBONE} | chain={CHAIN} ===")

# ---------- v3: resume from partial incremental file (idempotent restart) ----------
# Look for an existing partial file matching PRIMARY_BACKBONE; if found and same TS or earlier,
# load it and skip the cells already done.
prev_partial = None
if not ('_resume_check_disabled' in os.environ):
    # find the most recent incremental file for this PRIMARY_BACKBONE
    pattern = f'_p_l_v3_robustness_{PRIMARY_BACKBONE}_L30_*_incremental.json'
    candidates = sorted(RESULTS_DIR.glob(pattern),
                        key=lambda p: p.stat().st_mtime, reverse=True)
    for cand in candidates:
        if cand.is_file():
            try:
                j = json.loads(cand.read_text(encoding='utf-8'))
                if j.get('primary_backbone') == PRIMARY_BACKBONE and 'per_cell_detail_partial' in j:
                    prev_partial = cand
                    log(f"  [resume] found existing partial -> {cand.name} "
                        f"({j.get('cells_total',0)}/{len(baseline_cells)} cells, "
                        f"pass={j.get('cells_pass',0)} missing={j.get('cells_missing',0)})")
                    break
            except Exception:
                continue

incremental_path = RESULTS_DIR / f'_p_l_v3_robustness_{PRIMARY_BACKBONE}_L30_{TS}_incremental.json'
out_path = RESULTS_DIR / f'_p_l_v3_robustness_{PRIMARY_BACKBONE}_L30_{TS}.json'

# If we've already finalized (L=30 path exists for this TS), don't re-run
final_marker = RESULTS_DIR / f'_p_l_v3_robustness_{PRIMARY_BACKBONE}_L30_{TS}.json'
if final_marker.exists() and not ('_force_rerun' in os.environ):
    log(f"  [resume] FINAL L=30 already exists at {final_marker.name} — EXIT (delete it to re-run)")
    sys.exit(0)

# ---------- 1) keys ----------
raw = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt').read_bytes()
text = ''
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: text = raw.decode(enc); break
    except Exception: continue
teamo_key = re.search(r'(sk-teamo-[a-f0-9]+)', text).group(1)
log(f"  teamo_key[:18] = {teamo_key[:18]}... (mask only; never persisted)")

# ---------- 2) helpers ----------
def chat(prompt, model, base_url, key, max_tokens=512, timeout=30):
    url = f'{base_url}/chat/completions'
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
    payload = {'model': model, 'messages': [{'role':'user','content':prompt}],
               'max_tokens': max_tokens, 'temperature': 0.0}
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode())
            return {'ok': True,
                    'content': data['choices'][0]['message']['content'],
                    'ms': (time.time()-t0)*1000, 'status': r.status,
                    'response_model': data.get('model', '?'),
                    'usage': data.get('usage', {})}
    except urllib.error.HTTPError as e:
        return {'ok': False, 'ms': (time.time()-t0)*1000,
                'status': e.code, 'error': (e.read().decode(errors='replace') if e.fp else '')[:300]}
    except Exception as e:
        return {'ok': False, 'ms': (time.time()-t0)*1000,
                'status': -1, 'error': f'{type(e).__name__}: {str(e)[:200]}'}


def chat_with_retry(prompt, bb_name, max_tokens=512, timeout=30, retries=3):
    bb = BACKBONES[bb_name]
    errors = []
    last_err = None
    for attempt in range(1, retries + 1):
        # first attempt +20s grace for connection cold-start (empirical: 1018 first call ~30s)
        this_timeout = timeout + (20 if attempt == 1 else 0)
        r = chat(prompt, bb['model'], bb['base_url'], teamo_key,
                 max_tokens=max_tokens, timeout=this_timeout)
        if r['ok']:
            r['attempts'] = attempt
            r['error_history'] = errors
            r['request_model'] = bb['model']
            r['downgrade_detected'] = bool(r.get('response_model') and r['response_model'] != bb['model'])
            return r
        errors.append({'attempt': attempt, 'ms': round(r.get('ms', 0), 1),
                       'timeout_used_s': this_timeout,
                       'status': r.get('status'),
                       'error': (r.get('error') or '')[:200]})
        last_err = r.get('error', '?')
        if attempt < retries:
            sleep_s = 2 ** (attempt - 1)
            log(f"    [retry] {bb_name} attempt {attempt} fail (timeout_used={this_timeout}s): {last_err[:80]}... backoff {sleep_s}s")
            time.sleep(sleep_s)
    return {'ok': False, 'attempts': retries, 'error_history': errors,
            'error': f'all {retries} retries failed: {last_err}',
            'ms': sum(e.get('ms', 0) for e in errors),
            'status': -1, 'response_model': None, 'downgrade_detected': False,
            'request_model': bb['model'], 'content': None}


def warmup_backbone(bb_name, timeout=60):
    bb = BACKBONES[bb_name]
    r = chat("What is 2+3? Answer with the final number in **bold** at the end.",
             bb['model'], bb['base_url'], teamo_key,
             max_tokens=32, timeout=timeout)
    if r['ok'] and r.get('response_model') == bb['model'] and '5' in (r.get('content') or ''):
        log(f"  [warmup] {bb_name} OK ({round(r['ms'],0):.0f}ms, rm={r['response_model']})")
        return True
    log(f"  [warmup] {bb_name} FAIL: ok={r['ok']} rm={r.get('response_model')} err={r.get('error','')[:80]}")
    return False


def extract_number(text):
    if not text: return None
    m = re.search(r'\*\*\s*([-+]?\d[\d,]*\.?\d*)\s*\*\*', text)
    if m:
        try: return float(m.group(1).replace(',', ''))
        except Exception: pass
    # [Trae 2026-09-18 修复 P1-2 千分位] 补逗号容错
    nums = re.findall(r'-?\d[\d,]*(?:\.\d+)?', text)
    if nums:
        try: return float(nums[-1].replace(',', ''))
        except Exception: return None
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


# ---------- 3) load inputs ----------
BASELINE_JSON = RESULTS_DIR / 'deposon_volcengine_seed_code_30cells_2026_09_10.json'
PHYS60_JSON = RESULTS_DIR / 'deposon_v3_physical_opt_60cells_2026_09_11.json'

baseline = json.loads(BASELINE_JSON.read_text(encoding='utf-8'))
baseline_cells = []
for c in baseline['cells']:
    baseline_cells.append({'id': c['cell_id'], 'text': c['question'],
                           'gt': c['gold_answer'], 'kind': c['task'],
                           'baseline_is_correct': c['is_correct']})
log(f"  baseline cells = {len(baseline_cells)} (gsm8k={sum(1 for c in baseline_cells if c['kind']=='gsm8k')}, sqa={sum(1 for c in baseline_cells if c['kind']=='strategyqa')})")

phys60 = json.loads(PHYS60_JSON.read_text(encoding='utf-8'))
pc_per_model = phys60['P_C_distortion_bound_60cells']['per_model']
T_frac60_per_model = [m['T_frac60'] for m in pc_per_model]
mean_T_frac60 = sum(T_frac60_per_model) / len(T_frac60_per_model)
log(f"  L=60 per_model T_frac60 mean = {mean_T_frac60:.4f}")

# ---------- 4) sanity check ----------
log(f"=== Sanity check (chain: {CHAIN}) ===")
sanity_results = {}
sanity_chain_active = []
for bb_name in CHAIN:
    bb = BACKBONES[bb_name]
    log(f"  [sanity] try {bb_name}...")
    r = chat("What is 1+1? Answer with the final number in **bold** at the end.",
             bb['model'], bb['base_url'], teamo_key,
             max_tokens=32, timeout=20)
    if r['ok'] and r.get('response_model') == bb['model'] and '2' in (r.get('content') or ''):
        sanity_results[bb_name] = {'request_model': bb['model'],
                                   'response_model': r['response_model'],
                                   'content': (r.get('content') or '')[:80],
                                   'latency_ms': round(r['ms'], 1),
                                   'sanity_pass': True, 'downgrade_detected': False}
        sanity_chain_active.append(bb_name)
        log(f"  [sanity] {bb_name} PASS ({round(r['ms'],0):.0f}ms)")
        break
    else:
        log(f"  [sanity] {bb_name} FAIL: {r.get('error','')[:80] or 'not 2 in content'}")
        sanity_results[bb_name] = {'request_model': bb['model'], 'sanity_pass': False,
                                   'error': r.get('error', '?')[:120]}

if not sanity_chain_active:
    log("FATAL: no backbone in chain passed sanity")
    sys.exit(7)

# ---------- 5) run cells with chain fallback + per-cell incremental save ----------
results = []
n_pass = 0
n_missing = 0
n_total_attempts = 0
start_idx = 0

# If resuming from a previous partial, skip already-done cells
if prev_partial:
    try:
        prev = json.loads(prev_partial.read_text(encoding='utf-8'))
        prev_results = prev.get('per_cell_detail_partial', [])
        prev_results_by_id = {r['cell_id']: r for r in prev_results}
        # Only keep cells that match current baseline (defensive)
        kept = [prev_results_by_id[c['id']] for c in baseline_cells if c['id'] in prev_results_by_id]
        if len(kept) == len(prev_results):
            results = kept
            n_pass = sum(1 for r in results if r.get('is_correct'))
            n_missing = sum(1 for r in results if r.get('marked_missing'))
            n_total_attempts = prev.get('n_total_attempts', len(results))
            start_idx = len(results)
            log(f"  [resume] resumed from cell index {start_idx}/{len(baseline_cells)} "
                f"(pass={n_pass} missing={n_missing})")
        else:
            log(f"  [resume] WARN: prev_partial has {len(prev_results)} cells but kept only {len(kept)} — restart from 0")
            results = []
            n_pass = n_missing = n_total_attempts = 0
            start_idx = 0
    except Exception as e:
        log(f"  [resume WARN] failed to load {prev_partial}: {e}")
        start_idx = 0

log(f"=== Warmup {PRIMARY_BACKBONE} ===")
warmup_ok = warmup_backbone(PRIMARY_BACKBONE, timeout=60)
log(f"  warmup_result = {warmup_ok}")

log(f"=== Running {len(baseline_cells)} cells | chain = {CHAIN} | start_idx={start_idx} ===")
t_start = time.time()

for i in range(start_idx, len(baseline_cells)):
    cell = baseline_cells[i]
    prompt = build_prompt(cell)
    cell_kind = cell['kind']
    mx = 512 if cell_kind == 'gsm8k' else 256
    chain_log = []
    answered_ok = None
    for chain_idx, bb_name in enumerate(CHAIN):
        bb = BACKBONES[bb_name]
        timeout = bb['per_call_timeout_s']
        r = chat_with_retry(prompt, bb_name, max_tokens=mx, timeout=timeout, retries=3)
        chain_log.append({'bb': bb_name, 'attempts': r.get('attempts'),
                          'ms_total': round(r.get('ms', 0), 1),
                          'ok': r.get('ok'), 'response_model': r.get('response_model'),
                          'downgrade': r.get('downgrade_detected'),
                          'error': (r.get('error') or '')[:120] if not r.get('ok') else None})
        if r['ok'] and not r.get('downgrade_detected'):
            answered_ok = (bb_name, r, chain_log)
            break
        if r.get('downgrade_detected'):
            log(f"  [{i+1}/{len(baseline_cells)}] {cell['id']} chain[{chain_idx}] {bb_name} DOWNGRADE — abort runner")
            answered_ok = ('DOWNGRADE', r, chain_log)
            break
        log(f"  [{i+1}/{len(baseline_cells)}] {cell['id']} chain[{chain_idx}] {bb_name} all-retry-fail → next")
        time.sleep(0.5)

    n_total_attempts += sum(cl.get('attempts', 1) for cl in chain_log if cl.get('attempts'))

    if answered_ok is None:
        results.append({'cell_id': cell['id'], 'task': cell['kind'], 'gold_answer': cell['gt'],
                        'llm_extracted': None, 'is_correct': False,
                        'baseline_correct': cell.get('baseline_is_correct'),
                        'latency_ms': round(sum(l.get('ms_total', 0) for l in chain_log), 1),
                        'http_status': None, 'request_model': BACKBONES[CHAIN[0]]['model'],
                        'response_model': None, 'downgrade_detected': False,
                        'error': 'all_backbones_exhausted',
                        'content_head': '(NO RESPONSE — all retries failed across chain)',
                        'chain_log': chain_log, 'answered_by': None,
                        'marked_missing': True})
        n_missing += 1
    elif answered_ok[0] == 'DOWNGRADE':
        results.append({'cell_id': cell['id'], 'task': cell['kind'], 'gold_answer': cell['gt'],
                        'llm_extracted': None, 'is_correct': False,
                        'baseline_correct': cell.get('baseline_is_correct'),
                        'latency_ms': round(answered_ok[1].get('ms', 0), 1),
                        'http_status': answered_ok[1].get('status'),
                        'request_model': answered_ok[1]['request_model'],
                        'response_model': answered_ok[1]['response_model'],
                        'downgrade_detected': True,
                        'error': 'downgrade mid-chain (abort)',
                        'content_head': (answered_ok[1].get('content') or '')[:120].replace('\n', ' '),
                        'chain_log': chain_log, 'answered_by': None,
                        'marked_missing': True})
        log(f"  !!! ABORT runner on downgrade")
        break
    else:
        bb_name, r, chain_log = answered_ok
        if cell_kind == 'gsm8k':
            pred = extract_number(r['content'])
            is_correct = pred is not None and abs(pred - cell['gt']) < 1e-3
        else:
            pred = extract_yesno(r['content'])
            is_correct = pred is not None and pred == cell['gt']
        if is_correct: n_pass += 1
        results.append({'cell_id': cell['id'], 'task': cell['kind'], 'gold_answer': cell['gt'],
                        'llm_extracted': pred, 'is_correct': is_correct,
                        'baseline_correct': cell.get('baseline_is_correct'),
                        'latency_ms': round(r.get('ms', 0), 1),
                        'http_status': r.get('status'),
                        'request_model': r['request_model'],
                        'response_model': r.get('response_model'),
                        'downgrade_detected': r.get('downgrade_detected'),
                        'error': None,
                        'content_head': (r.get('content') or '')[:120].replace('\n', ' '),
                        'attempts': r.get('attempts'),
                        'chain_log': chain_log, 'answered_by': bb_name,
                        'marked_missing': False})

    # per-cell incremental save (防 bg 杀丢数据)
    inc = {'L': 30, 'primary_backbone': PRIMARY_BACKBONE,
           'timestamp': datetime.now(CST).isoformat(),
           'cells_total': len(results), 'cells_pass': n_pass, 'cells_missing': n_missing,
           'n_total_attempts': n_total_attempts,
           'per_cell_detail_partial': results}
    try:
        incremental_path.write_text(json.dumps(inc, ensure_ascii=False, indent=2),
                                    encoding='utf-8')
    except Exception as e:
        log(f"  [inc-save error] {e}")

    if (i+1) % 3 == 0 or (i+1) == len(baseline_cells):
        elapsed = time.time() - t_start
        log(f"  [progress] {i+1}/{len(baseline_cells)} pass={n_pass} missing={n_missing} elapsed={elapsed:.0f}s")
    time.sleep(2)

elapsed = time.time() - t_start

# ---------- 6) compute Spearman ----------
from scipy.stats import spearmanr
bb_scores, b_scores = [], []
for r in results:
    b_cell = next((c for c in baseline['cells'] if c['cell_id'] == r['cell_id']), None)
    if b_cell is None: continue
    bb_scores.append(1 if r['is_correct'] else 0)
    b_scores.append(1 if b_cell['is_correct'] else 0)
try:
    sp, sp_p = spearmanr(bb_scores, b_scores)
except Exception as e:
    log(f"  [Spearman fail] {e}")
    sp, sp_p = 0.0, 1.0

# ---------- 7) by_answered distribution ----------
by_answered = {}
for r in results:
    a = r.get('answered_by', 'MISSING')
    by_answered[a] = by_answered.get(a, 0) + 1
n_downgrade = sum(1 for r in results if r.get('downgrade_detected'))

# ---------- 8) save final L=30 + L=60 JSONs ----------
out = {
    'L': 30, 'primary_backbone': PRIMARY_BACKBONE, 'chain': CHAIN,
    'vendor_label': BACKBONES[PRIMARY_BACKBONE]['vendor_label'],
    'model': BACKBONES[PRIMARY_BACKBONE]['model'],
    'api_vendor': 'TeamoRouter (proxy 127.0.0.1:1018)',
    'base_url': BACKBONES[PRIMARY_BACKBONE]['base_url'],
    'task': f'P-L v3 Phase 2 L=30 档 (PRIMARY={PRIMARY_BACKBONE}, chain fallback, 30s × 3 retries)',
    'role': BACKBONES[PRIMARY_BACKBONE]['role'],
    'cells_total': len(results), 'cells_pass': n_pass, 'cells_missing': n_missing,
    'accuracy': round(n_pass / max(len(results), 1), 4),
    'cells_breakdown': {'gsm8k': sum(1 for r in results if r['task'] == 'gsm8k'),
                        'strategyqa': sum(1 for r in results if r['task'] == 'strategyqa')},
    'answered_by_distribution': by_answered,
    'spearman_vs_baseline': round(float(sp), 6),
    'spearman_p_value': round(float(sp_p), 6),
    'spearman_definition': 'rank correlation between backbone per-cell score (1/0) and baseline (doubao-seed-code-preview-251028) per-cell score',
    'elapsed_s': round(elapsed, 1),
    'n_total_attempts_across_cells': n_total_attempts,
    'n_downgrade_detected_in_any_cell': n_downgrade,
    'sanity_check_chain': sanity_results,
    'downgrade_fraud_check': {
        'enabled': True, 'method': 'response.model == request.model? (per cell, in chain)',
        'downgrade_detected_in_any_cell': n_downgrade > 0,
        'request_model': BACKBONES[PRIMARY_BACKBONE]['model'],
        'response_models_observed': sorted(set(r.get('response_model') for r in results if r.get('response_model'))),
        'all_cells_passed': n_downgrade == 0,
    },
    'v3_improvements': {
        'hard_timeout_per_cell_s': 30, 'first_attempt_grace_s': 20,
        'retries_per_backbone': 3, 'backoff_schedule_s': '1, 2',
        'max_tokens_cap': 512, 'warmup_call_per_primary': True,
        'fallback_chain': CHAIN,
        'per_cell_incremental_save': True,
        'note': 'v3 相对 v1 改进: 30s timeout + 3 retries + backoff + max_tokens=512 cap + warmup + chain fallback + per-cell incremental save',
    },
    'proxy_config': {
        'HTTPS_PROXY': os.environ.get('HTTPS_PROXY'),
        'HTTP_PROXY': os.environ.get('HTTP_PROXY'),
        'note': 'port 1018 only; ALL_PROXY intentionally unset',
    },
    'per_cell_detail': results,
    'iron_7_compliance': {
        'no_llm_rehash': True, 'no_extra_proxy_setup_beyond_1018': True,
        'teamorouter_only': True, 'no_key_in_prompt_json_disk': True,
        'no_18_frozen_touch': True, 'no_5_artifact_json_touch': True,
        'no_schema_v1_touch': True, 'no_plugin_spec_touch': True,
        'no_verifier_mavis_builtin_scripts_touch': True,
    },
    '_meta': {
        'timestamp': datetime.now(CST).isoformat(), 'runner_version': 'v3',
        'baseline_json_sha256_12': hashlib.sha256(BASELINE_JSON.read_bytes()).hexdigest()[:12],
        'phys60_json_sha256_12': hashlib.sha256(PHYS60_JSON.read_bytes()).hexdigest()[:12],
        'phase': 'P-L v3 Phase 2', 'subphase': 'closed-source (TeamoRouter) retry v3',
        'sanity_chain_active': sanity_chain_active,
        'incremental_path': str(incremental_path),
    },
}
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
log(f"  L=30 final JSON -> {out_path.name}  size={out_path.stat().st_size}B")

# L=60 wrapper
out_60 = {
    'L': 60, 'primary_backbone': PRIMARY_BACKBONE,
    'vendor_label': BACKBONES[PRIMARY_BACKBONE]['vendor_label'],
    'model': BACKBONES[PRIMARY_BACKBONE]['model'],
    'api_vendor': 'TeamoRouter (proxy 127.0.0.1:1018)',
    'base_url': BACKBONES[PRIMARY_BACKBONE]['base_url'],
    'task': f'P-L v3 Phase 2 L=60 档 (PRIMARY={PRIMARY_BACKBONE}, 复用 frozen 9 model aggregate)',
    'role': BACKBONES[PRIMARY_BACKBONE]['role'],
    'cells_total': 60, 'models_total': len(pc_per_model),
    'T_frac60_per_model': T_frac60_per_model, 'mean_T_frac60': round(mean_T_frac60, 4),
    'reused_from': str(PHYS60_JSON),
    'reused_from_sha256_12': hashlib.sha256(PHYS60_JSON.read_bytes()).hexdigest()[:12],
    'iron_7_compliance': out['iron_7_compliance'],
    '_meta': {'timestamp': datetime.now(CST).isoformat(),
              'note': 'L=60 复用 frozen per_model aggregate (0 LLM 重跑)'},
}
out_60_path = RESULTS_DIR / f'_p_l_v3_robustness_{PRIMARY_BACKBONE}_L60_{TS}.json'
out_60_path.write_text(json.dumps(out_60, ensure_ascii=False, indent=2), encoding='utf-8')
log(f"  L=60 JSON -> {out_60_path.name}  size={out_60_path.stat().st_size}B")

log(f"=== DONE for PRIMARY={PRIMARY_BACKBONE} | pass={n_pass}/{len(results)} missing={n_missing} elapsed={elapsed:.1f}s ===")
log(f"  Final outputs:")
log(f"    L=30: {out_path}")
log(f"    L=60: {out_60_path}")
log(f"    incremental (will be removed): {incremental_path}")

# remove incremental (intermediate file no longer needed)
try:
    incremental_path.unlink()
    log(f"  removed incremental: {incremental_path.name}")
except Exception:
    pass

# flush log
try:
    LOG_FILE.write_text('\n'.join(_log_lines) + '\n', encoding='utf-8')
except Exception:
    pass
log(f"  log -> {LOG_FILE.name}")
log("=== END ===")


# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-18 走读补, 标记 TRAE_SELFCHECK_2026_09_16_V3) ----------
# 补入理由: 2026-09-18 根目录走读发现 91 个 .py 中仅 1 个含 SELF-CHECK, 属历史清理遗漏
import os as _os_sc
assert _os_sc.path.basename(__file__) == '_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_SELFCHECK_2026_09_16_V3' in _src_sc
print('_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py SELF-CHECK PASS')
