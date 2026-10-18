# -*- coding: utf-8 -*-
"""
deposon V3.X worker C 补测 - 2 model x 30 cells (60 LLM calls)
models: glm-5.3, doubao-seed-evolving
strict: no retry / no model switch / no proxy
key: runtime read from GB18030 file, never written to JSON
"""
import os, json, time, re, sys
import urllib.request, urllib.error

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
GSM8K_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STQ_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_volcengine_worker_c_2026_09_10.json'
OUTPUT_LOG = r'D:\私人资料\deposon-repo\results\deposon_volcengine_worker_c_2026_09_10.log'
BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
MODELS = ['glm-5.3', 'doubao-seed-evolving']
SANITY_PROMPT = 'What is 1+1?'
SANITY_MAX_TOKENS = 1024
SANITY_TIMEOUT = 20
CELL_MAX_TOKENS = 1024
CELL_TIMEOUT = 30
PROXY_KEYS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']
N_GSM8K = 15
N_STQ = 15

# ---- log helper ----
_log_fp = None
def log(msg):
    global _log_fp
    line = f'[{time.strftime("%H:%M:%S")}] {msg}'
    print(line, flush=True)
    if _log_fp is not None:
        _log_fp.write(line + '\n')
        _log_fp.flush()

# 1) Read key (GB18030)
enc = None
text = None
for enc_name in ('gb18030', 'gbk', 'utf-8', 'utf-16'):
    try:
        text = open(KEY_FILE, 'r', encoding=enc_name).read()
        if 'ark-[REDACTED]' in text:
            enc = enc_name
            break
    except Exception:
        pass
if not enc:
    print('FATAL: key file read failed for all encodings')
    sys.exit(2)
m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', text)
if not m:
    print('FATAL: ark-[REDACTED]* key not found')
    sys.exit(2)
api_key = m.group(0)
key_truncated = api_key[:20] + '...' + api_key[-4:]
os.environ['ARK_CODING_PLAN_KEY'] = api_key
for k in PROXY_KEYS:
    os.environ.pop(k, None)
log(f'KEY_OK enc={enc} truncated={key_truncated} proxy_cleared')

# 2) Load benchmarks
with open(GSM8K_FILE, 'r', encoding='utf-8') as f:
    gsm8k = json.load(f)
with open(STQ_FILE, 'r', encoding='utf-8') as f:
    stq = json.load(f)
log(f'BENCHMARK_LOADED gsm8k={len(gsm8k)} stq={len(stq)}')

# 3) HTTP helper
def query_chat(prompt, model, max_tokens, timeout):
    url = f'{BASE_URL}/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers=headers,
        method='POST'
    )
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
        err_raw = e.read().decode('utf-8', errors='replace') if e.fp else ''
        return {'status': e.code, 'ms': round(elapsed_ms, 1), 'body': None, 'error': err_raw[:500]}
    except Exception as e:
        elapsed_ms = (time.time() - t0) * 1000
        return {'status': -1, 'ms': round(elapsed_ms, 1), 'body': None, 'error': f'{type(e).__name__}: {str(e)[:300]}'}

def extract_text(body):
    if not body or not isinstance(body, dict):
        return ''
    try:
        return body['choices'][0]['message']['content'] or ''
    except Exception:
        return ''

def extract_number(s):
    """Priority: **N** bold, then last number-like token."""
    if s is None:
        return None
    s = str(s)
    # 1) bold number: **N** or **N.N**
    m = re.findall(r'\*\*\s*(-?\d+(?:\.\d+)?)\s*\*\*', s)
    if m:
        try:
            return float(m[-1])
        except Exception:
            pass
    # 2) last number-like token in whole string
    m = re.findall(r'-?\d+(?:\.\d+)?', s)
    if m:
        try:
            return float(m[-1])
        except Exception:
            return None
    return None

def extract_yesno(s):
    """Return 'Yes' or 'No' (or None). Bold priority then last token."""
    if s is None:
        return None
    s = str(s).strip()
    # bold: **Yes** / **No**
    m = re.findall(r'\*\*\s*(Yes|No|yes|no)\s*\*\*', s, re.IGNORECASE)
    if m:
        return m[-1].capitalize()
    # last Yes/No token (case-insensitive word boundary)
    tokens = re.findall(r'\b(Yes|No|yes|no)\b', s)
    if tokens:
        return tokens[-1].capitalize()
    return None

# 4) Pre-build cell set
cells_meta = []
for i in range(1, N_GSM8K + 1):
    item = gsm8k.get(str(i), {})
    cells_meta.append({
        'cell_id': f'gsm8k_{i}',
        'task': 'gsm8k',
        'question': item.get('question', ''),
        'gold': item.get('answer', None),
        'prompt': f"Question: {item.get('question', '')}\nAnswer with one number only:"
    })
for i in range(1, N_STQ + 1):
    item = stq.get(str(i), {})
    cells_meta.append({
        'cell_id': f'stq_{i}',
        'task': 'strategyqa',
        'question': item.get('question', ''),
        'gold': item.get('answer', None),
        'prompt': f"Question: {item.get('question', '')}\nAnswer with Yes or No only:"
    })
log(f'CELLS_BUILT total={len(cells_meta)} (gsm8k={N_GSM8K} stq={N_STQ})')

# 5) Open log file
os.makedirs(os.path.dirname(OUTPUT_LOG), exist_ok=True)
_log_fp = open(OUTPUT_LOG, 'w', encoding='utf-8')
log(f'OUTPUT_JSON={OUTPUT_JSON}')
log(f'OUTPUT_LOG={OUTPUT_LOG}')

# 6) Main loop: 2 models x 30 cells
results = {'models': []}
overall_t0 = time.time()
for model in MODELS:
    log(f'=== MODEL {model} START ===')
    # 6a) sanity
    s = query_chat(SANITY_PROMPT, model, SANITY_MAX_TOKENS, SANITY_TIMEOUT)
    s_text = extract_text(s['body'])
    s_pass = (s['status'] == 200) and ('2' in s_text)
    log(f'  SANITY status={s["status"]} ms={s["ms"]} text={s_text!r} pass={s_pass}')
    sanity_log = {
        'status': s['status'],
        'ms': s['ms'],
        'response_text': s_text,
        'error': s['error'] if s['status'] != 200 else None
    }
    if not s_pass:
        log(f'  [SANITY FAIL] skip 30 cells for {model}')
        results['models'].append({
            'model': model,
            'sanity': sanity_log,
            'sanity_pass': False,
            'cells': [],
            'gsm8k_passed': 0,
            'gsm8k_attempted': 0,
            'strategyqa_passed': 0,
            'strategyqa_attempted': 0,
            'total_passed': 0,
            'cells_done': 0,
            'pass_rate_30': 0.0,
            'avg_ms': 0,
            'status': 'SANITY_FAIL',
            'elapsed_s': 0
        })
        continue
    # 6b) 30 cells
    model_t0 = time.time()
    cells = []
    gsm8k_passed = 0
    gsm8k_attempted = 0
    stq_passed = 0
    stq_attempted = 0
    total_ms = 0
    for cm in cells_meta:
        cid = cm['cell_id']
        task = cm['task']
        q = cm['question']
        gold = cm['gold']
        if not q or gold is None:
            log(f'  [SKIP {cid}] missing question/gold')
            cells.append({
                'cell_id': cid, 'task': task, 'question': q, 'gold_answer': gold,
                'llm_raw_response': None, 'llm_extracted': None, 'is_correct': None,
                'latency_ms': 0, 'http_status': -1, 'note': 'skipped (no q/gold)', 'error': 'missing_input'
            })
            continue
        r = query_chat(cm['prompt'], model, CELL_MAX_TOKENS, CELL_TIMEOUT)
        text = extract_text(r['body'])
        usage = (r['body'] or {}).get('usage', {}) if isinstance(r['body'], dict) else {}
        if task == 'gsm8k':
            pred = extract_number(text)
            is_correct = (pred is not None and abs(pred - float(gold)) < 1e-3)
            gsm8k_attempted += 1
            if is_correct:
                gsm8k_passed += 1
        else:
            pred = extract_yesno(text)
            gold_str = str(gold).strip().capitalize()
            is_correct = (pred is not None and pred == gold_str)
            stq_attempted += 1
            if is_correct:
                stq_passed += 1
        total_ms += r['ms']
        note = 'clean' if r['status'] == 200 else f'http_{r["status"]}'
        if r['status'] == 200 and text and '**' in text:
            note = 'bold_used'
        cells.append({
            'cell_id': cid,
            'task': task,
            'question': q,
            'gold_answer': gold,
            'llm_raw_response': text,
            'llm_extracted': pred,
            'is_correct': bool(is_correct),
            'latency_ms': r['ms'],
            'http_status': r['status'],
            'usage': usage,
            'note': note,
            'error': r['error'] if r['status'] != 200 else None
        })
        log(f'  CELL {cid} status={r["status"]} ms={r["ms"]} pred={pred!r} gold={gold!r} correct={is_correct}')
    elapsed_s = round(time.time() - model_t0, 1)
    cells_done = gsm8k_attempted + stq_attempted
    total_passed = gsm8k_passed + stq_passed
    avg_ms = round(total_ms / cells_done, 1) if cells_done else 0
    pass_rate = round(total_passed / 30, 4) if cells_done else 0.0
    log(f'  MODEL {model} DONE gsm={gsm8k_passed}/{gsm8k_attempted} stq={stq_passed}/{stq_attempted} avg_ms={avg_ms} elapsed_s={elapsed_s}')
    results['models'].append({
        'model': model,
        'sanity': sanity_log,
        'sanity_pass': True,
        'cells': cells,
        'gsm8k_passed': gsm8k_passed,
        'gsm8k_attempted': gsm8k_attempted,
        'strategyqa_passed': stq_passed,
        'strategyqa_attempted': stq_attempted,
        'total_passed': total_passed,
        'cells_done': cells_done,
        'pass_rate_30': pass_rate,
        'avg_ms': avg_ms,
        'status': 'COMPLETE' if cells_done == 30 else f'PARTIAL ({cells_done}/30)',
        'elapsed_s': elapsed_s
    })

overall_elapsed = round(time.time() - overall_t0, 1)
results['timestamp'] = time.strftime('%Y-%m-%dT%H:%M:%S+08:00')
results['worker_id'] = 'C'
results['gateway'] = '火山方舟 Coding Plan'
results['base_url'] = BASE_URL
results['auth'] = f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)'
results['max_tokens'] = CELL_MAX_TOKENS
results['timeout_s'] = CELL_TIMEOUT
results['temperature'] = 0.0
results['proxy_cleared'] = True
results['overall_elapsed_s'] = overall_elapsed
results['note'] = 'Worker C 补测 (concurrent with worker A/B/D); models=glm-5.3+doubao-seed-evolving; 30 cells each (15 GSM8K + 15 StrategyQA)'

# 7) Write JSON
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
log(f'[WROTE] {OUTPUT_JSON}')

# 8) Summary
log(f'[DONE] overall_elapsed_s={overall_elapsed}')
for m in results['models']:
    log(f'  {m["model"]}: {m["total_passed"]}/{m["cells_done"]} pass_rate={m["pass_rate_30"]} avg_ms={m["avg_ms"]} status={m["status"]}')
_log_fp.close()
