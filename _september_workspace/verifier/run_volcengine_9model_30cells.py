#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 model × 30 cells 完整横向对比
Volcengine Coding Plan
- 9 models × (15 GSM8K + 15 StrategyQA) = 270 calls
- max_tokens=2048, temperature=0.0, timeout=60s/cell
- No proxy, no retries, no model switch
"""
import sys
# Force UTF-8 stdout for Windows GBK safety
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')
import os, json, time, urllib.request, urllib.error, re, sys
from datetime import datetime, timezone, timedelta

# === 1. Read key from GB18030 file (never write to disk) ===
KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
content = open(KEY_FILE, 'r', encoding='gb18030').read()
m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', content)
if not m:
    raise SystemExit('FATAL: ark-[REDACTED] key not found in LLM API.txt')
api_key = m.group(0)
os.environ['ARK_CODING_PLAN_KEY'] = api_key

# === 2. Clear any proxy (火山国内) ===
for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(k, None)

BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
ENDPOINT = f'{BASE_URL}/chat/completions'
MAX_TOKENS = 2048
TIMEOUT_S = 60
TEMPERATURE = 0.0

MODELS = [
    "doubao-seed-2.0-lite",
    "kimi-k2.7-code",
    "minimax-m3",
    "doubao-seed-2.1-turbo",
    "deepseek-v4-flash",
    "glm-5.3",
    "doubao-seed-evolving",
    "glm-5.3-flash",
    "deepseek-v4-pro"
]

# === 3. Query function ===
def query_chat(prompt, model, max_tokens=MAX_TOKENS, timeout=TIMEOUT_S):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': TEMPERATURE
    }
    req = urllib.request.Request(ENDPOINT,
                                  data=json.dumps(data, ensure_ascii=False).encode('utf-8'),
                                  headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body_bytes = resp.read()
            body = json.loads(body_bytes.decode('utf-8', errors='replace'))
            return {
                'ok': True,
                'status': resp.status,
                'ms': int((time.time() - t0) * 1000),
                'body': body,
                'text': extract_text(body)
            }
    except urllib.error.HTTPError as e:
        err_body = ''
        try:
            err_body = e.read().decode('utf-8', errors='replace')[:500]
        except: pass
        return {'ok': False, 'status': e.code, 'ms': int((time.time() - t0) * 1000), 'error': err_body}
    except Exception as e:
        return {'ok': False, 'status': -1, 'ms': int((time.time() - t0) * 1000), 'error': str(e)[:500]}

def extract_text(body):
    try:
        return body['choices'][0]['message']['content']
    except (KeyError, IndexError, TypeError):
        return ''

# === 4. Improved extractor (priority **N** then last number) ===
def extract_number(text):
    if not text:
        return None
    # 优先 **N** 粗体数字
    m = re.search(r'\*\*([\d,.]+)\*\*', text)
    if m:
        try:
            return float(m.group(1).replace(',', ''))
        except: pass
    # fallback: 找最后数字
    nums = re.findall(r'-?\d+\.?\d*', text)
    if nums:
        try:
            return float(nums[-1])
        except: pass
    return None

def extract_yes_no(text):
    """Extract Yes/No from text, case-insensitive, prefer 'boxed' or 'answer is' patterns"""
    if not text:
        return None
    t = text.strip()
    # 优先 **Yes/No** 粗体
    m = re.search(r'\*\*(Yes|No)\*\*', t, re.IGNORECASE)
    if m:
        return m.group(1).capitalize()
    # 优先 "answer is Yes/No" 或 "the answer is Yes/No"
    m = re.search(r'(?:answer\s+is|answer:\s*)\s*(Yes|No)', t, re.IGNORECASE)
    if m:
        return m.group(1).capitalize()
    # 优先找最后一个 Yes/No
    yn = re.findall(r'\b(Yes|No)\b', t, re.IGNORECASE)
    if yn:
        return yn[-1].capitalize()
    return None

# === 5. Load 30 cells (15 GSM8K + 15 StrategyQA) ===
gsm8k_data = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json', 'r', encoding='utf-8'))
stq_data = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json', 'r', encoding='utf-8'))

gsm8k_cells = []
for i in range(1, 16):
    cell = gsm8k_data[str(i)]
    gsm8k_cells.append({
        'id': i,
        'type': 'gsm8k',
        'question': cell['question'],
        'expected': float(cell['answer'])
    })

stq_cells = []
for i in range(1, 16):
    cell = stq_data[str(i)]
    stq_cells.append({
        'id': i,
        'type': 'strategyqa',
        'question': cell['question'],
        'expected': cell['answer'].strip().capitalize()
    })

# === 6. Sanity check (1-cell per model, 30s timeout) ===
print('=' * 70, flush=True)
print('STEP 1: 9 model 1-cell sanity check (30s timeout)', flush=True)
print('=' * 70, flush=True)

sanity_results = {}
for model in MODELS:
    r = query_chat('What is 1+1? Answer with just the number in bold, e.g. **2**.', model, max_tokens=128, timeout=30)
    text = r.get('text', '')
    sanity_ok = ('2' in text) and r.get('ok', False)
    sanity_results[model] = {
        'http_status': r.get('status'),
        'ok': r.get('ok', False),
        'latency_ms': r.get('ms', 0),
        'response_head': text[:200],
        'sanity_pass': sanity_ok
    }
    flag = 'OK ' if sanity_ok else 'ERR'
    print(f'  {flag} {model:30s} http={r.get("status")} ms={r.get("ms", 0):>5d} sanity={sanity_ok}', flush=True)

# === 7. Main run: 9 model × 30 cells ===
print(flush=True)
print('=' * 70, flush=True)
print('STEP 2: 9 model × 30 cells (15 GSM8K + 15 StrategyQA, 60s timeout)', flush=True)
print('=' * 70, flush=True)

t_start = time.time()
all_models_results = []

for mi, model in enumerate(MODELS, 1):
    print(flush=True)
    print(f'[{mi}/9] {model}', flush=True)
    t_model = time.time()
    gsm_passed = 0
    stq_passed = 0
    total_latency = 0
    cell_count = 0
    cells_log = []

    # 15 GSM8K
    for cell in gsm8k_cells:
        prompt = f"{cell['question']}\n\nShow your reasoning then give the final answer in bold, e.g. **42**."
        r = query_chat(prompt, model)
        cell_count += 1
        if r.get('ok'):
            text = r.get('text', '')
            pred = extract_number(text)
            passed = (pred is not None and abs(pred - cell['expected']) < 0.01)
            if passed: gsm_passed += 1
            total_latency += r.get('ms', 0)
            cells_log.append({
                'id': cell['id'], 'type': 'gsm8k',
                'http': r.get('status'), 'ms': r.get('ms', 0),
                'expected': cell['expected'], 'predicted': pred, 'passed': passed,
                'resp_head': text[:120]
            })
            print(f'  GSM#{cell["id"]:02d} http={r.get("status")} ms={r.get("ms", 0):>5d} exp={cell["expected"]} pred={pred} {"PASS" if passed else "FAIL"}', flush=True)
        else:
            cells_log.append({
                'id': cell['id'], 'type': 'gsm8k',
                'http': r.get('status'), 'ms': r.get('ms', 0),
                'expected': cell['expected'], 'predicted': None, 'passed': False,
                'error': r.get('error', '')[:200]
            })
            print(f'  GSM#{cell["id"]:02d} http={r.get("status")} ms={r.get("ms", 0):>5d} ERROR: {r.get("error", "")[:80]}', flush=True)

    # 15 StrategyQA
    for cell in stq_cells:
        prompt = f"{cell['question']}\n\nThink step by step then give the final answer as **Yes** or **No**."
        r = query_chat(prompt, model)
        cell_count += 1
        if r.get('ok'):
            text = r.get('text', '')
            pred = extract_yes_no(text)
            passed = (pred is not None and pred == cell['expected'])
            if passed: stq_passed += 1
            total_latency += r.get('ms', 0)
            cells_log.append({
                'id': cell['id'], 'type': 'strategyqa',
                'http': r.get('status'), 'ms': r.get('ms', 0),
                'expected': cell['expected'], 'predicted': pred, 'passed': passed,
                'resp_head': text[:120]
            })
            print(f'  STQ#{cell["id"]:02d} http={r.get("status")} ms={r.get("ms", 0):>5d} exp={cell["expected"]} pred={pred} {"PASS" if passed else "FAIL"}', flush=True)
        else:
            cells_log.append({
                'id': cell['id'], 'type': 'strategyqa',
                'http': r.get('status'), 'ms': r.get('ms', 0),
                'expected': cell['expected'], 'predicted': None, 'passed': False,
                'error': r.get('error', '')[:200]
            })
            print(f'  STQ#{cell["id"]:02d} http={r.get("status")} ms={r.get("ms", 0):>5d} ERROR: {r.get("error", "")[:80]}', flush=True)

    total_passed = gsm_passed + stq_passed
    avg_ms = int(total_latency / cell_count) if cell_count else 0
    model_elapsed = int(time.time() - t_model)
    print(f'  >>> {model} done in {model_elapsed}s | GSM={gsm_passed}/15 STQ={stq_passed}/15 Total={total_passed}/30 avg_ms={avg_ms}', flush=True)

    all_models_results.append({
        'model': model,
        'gsm8k_passed': gsm_passed,
        'strategyqa_passed': stq_passed,
        'total_passed': total_passed,
        'pass_rate': round(total_passed / 30.0, 4),
        'avg_ms': avg_ms,
        'elapsed_s': model_elapsed,
        'sanity': sanity_results[model],
        'cells': cells_log
    })

# === 8. Build summary ===
best = max(all_models_results, key=lambda m: m['total_passed'])
best_count = best['total_passed']
total_elapsed = int(time.time() - t_start)

now_iso = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')

output = {
    'timestamp': now_iso,
    'gateway': '火山方舟 Coding Plan',
    'base_url': 'https://ark.cn-beijing.volces.com/api/coding/v3',
    'auth': 'ark-[REDACTED]... (key loaded from env at runtime; literal key never written to disk)',
    'max_tokens': MAX_TOKENS,
    'timeout_s': TIMEOUT_S,
    'temperature': TEMPERATURE,
    'total_elapsed_s': total_elapsed,
    'cells_per_model': 30,
    'total_calls': 9 * 30,
    'models': all_models_results,
    'best_model': best['model'],
    'best_pass_rate': f'{best_count}/30',
    'summary': {
        'total_models_tested': 9,
        'best_pass_count': best_count,
        'best_pass_rate': f'{best_count}/30',
        'best_model': best['model'],
        'runner_up': sorted(all_models_results, key=lambda m: -m['total_passed'])[1]['model'],
        'runner_up_count': sorted(all_models_results, key=lambda m: -m['total_passed'])[1]['total_passed'],
        'total_cells_attempted': 9 * 30,
        'total_cells_passed': sum(m['total_passed'] for m in all_models_results),
        'total_elapsed_s': total_elapsed
    }
}

# === 9. Write JSON ===
out_json = r'D:\私人资料\deposon-repo\results\deposon_volcengine_9model_30cells_2026_09_10.json'
parent_dir = os.path.dirname(out_json)
if not os.path.isdir(parent_dir):
    raise SystemExit(f'FATAL: parent dir missing: {parent_dir}')

with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(flush=True)
print('=' * 70, flush=True)
print(f'DONE in {total_elapsed}s', flush=True)
print(f'Best: {best["model"]} {best_count}/30 (pass_rate={best["pass_rate"]})', flush=True)
print(f'JSON: {out_json}', flush=True)
print('=' * 70, flush=True)
