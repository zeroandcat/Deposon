# -*- coding: utf-8 -*-
"""
DEEPSEEK-V41-60CELLS-V2-STARTUP (max_tokens=1024)
- V2 真实 2 周工作量 - 启动阶段
- 严格只跑 deepseek/deepseek-v4.1-flash
- 60 cells = 15 GSM8K (id 1-15) + 15 StrategyQA (id 1-15) + 30 额外 GSM8K (id 16-45)
- max_tokens=1024 (沿用 v2 baseline) + reasoning={max_tokens:0, exclude:true}
- 边际验证: 30 -> 60 cells 稳定性
- verdict: PASS if >=48/60 (80%), MARGINAL if 36-47 (60-79%), REGRESSION if <36
- key 永远 runtime 读,永不落盘
"""
import os
import re
import sys
import json
import time
import io
import urllib.request
import urllib.error
import datetime

# Force UTF-8 stdout to avoid GBK encoding crashes
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

# ---------------- 0. 加载 key (GB18030) ----------------
key_file = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
content = open(key_file, 'r', encoding='gb18030').read()
m = re.search(r'sk-or-v1-[a-f0-9]{64}', content)
if not m:
    print("[FATAL] no sk-or-v1-... in LLM API.txt", file=sys.stderr)
    sys.exit(1)
api_key = m.group(0)
os.environ['OPENROUTER_API_KEY'] = api_key

# 显式清空 proxy (DeepSeek 国内模型)
for p in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(p, None)


def mask_key(k):
    return f"{k[:12]}...{k[-4:]}"


print(f"[INIT] key loaded: {mask_key(api_key)}")
print(f"[INIT] proxy cleared: HTTP_PROXY/HTTPS_PROXY etc all popped")
print(f"[INIT] V2 启动阶段 (60 cells, max_tokens=1024, reasoning stripped)")

SELECTED_MODEL = 'deepseek/deepseek-v4.1-flash'
MAX_TOKENS = 1024
SLEEP_BETWEEN = 0.5

# ---------------- 1. 1-cell sanity check ----------------
def sanity_check(model_id, prompt="What is 1+1?", max_tokens=MAX_TOKENS):
    url = 'https://openrouter.ai/api/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': model_id,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0,
        'reasoning': {'max_tokens': 0, 'exclude': True}
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode())
            return body, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ''
        return None, e.code, err


print("\n[STEP 1] 1-cell sanity check (max_tokens=1024, reasoning stripped) ...")
body, status, err = sanity_check(SELECTED_MODEL, "What is 1+1?")
sanity_ok = False
if status == 200 and body and body.get('choices'):
    msg = body['choices'][0].get('message', {})
    ans = msg.get('content', '') or ''
    print(f"  [OK] {SELECTED_MODEL} -> status=200, content[0:80]={ans[:80]!r}")
    sanity_ok = True
else:
    print(f"  [FAIL] {SELECTED_MODEL} -> status={status}, err={(err or '')[:300]}", file=sys.stderr)

if not sanity_ok:
    print("\n[FATAL] sanity check FAILED for strict v4.1-flash. Per user hard rule: NO fallback to v4* submodels.", file=sys.stderr)
    sys.exit(4)

# ---------------- 2. query + extract helpers ----------------
def query_llm(prompt, model, max_tokens=MAX_TOKENS):
    url = 'https://openrouter.ai/api/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': model,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': 0.0,
        'reasoning': {'max_tokens': 0, 'exclude': True}
    }
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode())
            return body, (time.time() - t0) * 1000, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err


def extract_number(text):
    """从文本里提取最后一个浮点数(GSM8K 用)"""
    if not text:
        return None
    boxed = re.findall(r'\\boxed\{([-+]?\d+\.?\d*)\}', text)
    if boxed:
        try:
            return float(boxed[-1])
        except ValueError:
            pass
    hash_match = re.findall(r'####\s*([-+]?\d+\.?\d*)', text)
    if hash_match:
        try:
            return float(hash_match[-1])
        except ValueError:
            pass
    nums = re.findall(r'[-+]?\d+\.?\d*', text)
    if nums:
        try:
            return float(nums[-1])
        except ValueError:
            return None
    return None


def extract_yes_no(text):
    """提取 Yes/No 答案(StrategyQA 用)"""
    if not text:
        return None
    t = text.strip().lower()
    first_line = t.split('\n')[0].strip()
    if first_line in ('yes', 'no'):
        return first_line[0].upper() + first_line[1:]
    boxed = re.findall(r'\\boxed\{(yes|no)\}', t)
    if boxed:
        return boxed[-1][0].upper() + boxed[-1][1:]
    for word in re.findall(r'\b(yes|no)\b', t):
        return word[0].upper() + word[1:]
    return None


# 加载 benchmark 数据
gsm8k_path = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
strategyqa_path = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'

with open(gsm8k_path, 'r', encoding='utf-8') as f:
    gsm8k_data = json.load(f)
with open(strategyqa_path, 'r', encoding='utf-8') as f:
    strategyqa_data = json.load(f)

print(f"[INIT] GSM8K dataset: {len(gsm8k_data)} cells (need 45)")
print(f"[INIT] StrategyQA dataset: {len(strategyqa_data)} cells (need 15)")

# ---------------- 3. 60 cells 全量 (max_tokens=1024) ----------------
cells = []
print("\n[STEP 2] Running 60 cells (15 GSM8K + 15 StrategyQA + 30 额外 GSM8K, max_tokens=1024) ...")
print("=" * 80)

t_start = time.time()


def run_gsm8k_cell(cell_id, item):
    question = item['question']
    gold = item['answer']
    prompt = f"Question: {question}\nAnswer in one number:"
    body, latency_ms, status, err = query_llm(prompt, SELECTED_MODEL, max_tokens=MAX_TOKENS)
    if status != 200 or not body:
        return {
            'cell_id': cell_id,
            'task': 'gsm8k',
            'question': question,
            'gold_answer': gold,
            'llm_raw_response': None,
            'llm_extracted': None,
            'is_correct': False,
            'latency_ms': round(latency_ms, 1),
            'http_status': status,
            'error': (err[:300] if err else 'unknown')
        }
    msg = body['choices'][0].get('message', {})
    content = msg.get('content', '') or ''
    extracted = extract_number(content)
    is_correct = (extracted is not None and abs(extracted - gold) < 1e-3)
    usage = body.get('usage', {})
    completion_tokens = usage.get('completion_tokens')
    note = 'clean'
    if completion_tokens is not None and completion_tokens >= MAX_TOKENS:
        note = f'**truncated** (completion_tokens={completion_tokens}, hit max_tokens={MAX_TOKENS})'
    elif extracted is None:
        note = '**no_number_extracted**'
    return {
        'cell_id': cell_id,
        'task': 'gsm8k',
        'question': question,
        'gold_answer': gold,
        'llm_raw_response': content[:500],
        'llm_extracted': extracted,
        'is_correct': is_correct,
        'latency_ms': round(latency_ms, 1),
        'http_status': status,
        'prompt_tokens': usage.get('prompt_tokens'),
        'completion_tokens': completion_tokens,
        'reasoning_tokens': usage.get('reasoning_tokens'),
        'note': note,
        'error': None
    }


def run_strategyqa_cell(cell_id, item):
    question = item['question']
    gold = item['answer']
    prompt = f"Question: {question}\nAnswer Yes or No:"
    body, latency_ms, status, err = query_llm(prompt, SELECTED_MODEL, max_tokens=MAX_TOKENS)
    if status != 200 or not body:
        return {
            'cell_id': cell_id,
            'task': 'strategyqa',
            'question': question,
            'gold_answer': gold,
            'llm_raw_response': None,
            'llm_extracted': None,
            'is_correct': False,
            'latency_ms': round(latency_ms, 1),
            'http_status': status,
            'error': (err[:300] if err else 'unknown')
        }
    msg = body['choices'][0].get('message', {})
    content = msg.get('content', '') or ''
    extracted = extract_yes_no(content)
    is_correct = (extracted is not None and extracted.lower() == gold.lower())
    usage = body.get('usage', {})
    completion_tokens = usage.get('completion_tokens')
    note = 'clean'
    if completion_tokens is not None and completion_tokens >= MAX_TOKENS:
        note = f'**truncated** (completion_tokens={completion_tokens}, hit max_tokens={MAX_TOKENS})'
    elif extracted is None:
        note = '**no_yes_no_extracted**'
    elif not is_correct:
        note = '**semantic_misjudge** (model本体能力, 与 max_tokens 无关)'
    return {
        'cell_id': cell_id,
        'task': 'strategyqa',
        'question': question,
        'gold_answer': gold,
        'llm_raw_response': content[:500],
        'llm_extracted': extracted,
        'is_correct': is_correct,
        'latency_ms': round(latency_ms, 1),
        'http_status': status,
        'prompt_tokens': usage.get('prompt_tokens'),
        'completion_tokens': completion_tokens,
        'reasoning_tokens': usage.get('reasoning_tokens'),
        'note': note,
        'error': None
    }


# 15 GSM8K (id 1-15)
print("\n--- Part 1: GSM8K id 1-15 ---")
for i in range(1, 16):
    cell_id = f"gsm8k_{i}"
    item = gsm8k_data[str(i)]
    cell = run_gsm8k_cell(cell_id, item)
    cells.append(cell)
    mark = 'OK' if cell['is_correct'] else 'FAIL'
    err = cell.get('error') or ''
    print(f"  [{cell_id}] gold={cell['gold_answer']} extracted={cell['llm_extracted']} [{mark}] latency={cell['latency_ms']:.0f}ms note={cell['note']}{(' err=' + err[:100]) if err and cell['is_correct'] is False and not cell['note'] else ''}")
    time.sleep(SLEEP_BETWEEN)

# 15 StrategyQA (id 1-15)
print("\n--- Part 2: StrategyQA id 1-15 ---")
for i in range(1, 16):
    cell_id = f"strategyqa_{i}"
    item = strategyqa_data[str(i)]
    cell = run_strategyqa_cell(cell_id, item)
    cells.append(cell)
    mark = 'OK' if cell['is_correct'] else 'FAIL'
    err = cell.get('error') or ''
    print(f"  [{cell_id}] gold={cell['gold_answer']} extracted={cell['llm_extracted']} [{mark}] latency={cell['latency_ms']:.0f}ms note={cell['note']}{(' err=' + err[:100]) if err and cell['is_correct'] is False and not cell['note'] else ''}")
    time.sleep(SLEEP_BETWEEN)

# 30 额外 GSM8K (id 16-45)
print("\n--- Part 3: 额外 GSM8K id 16-45 ---")
extra_max = min(45, len(gsm8k_data))
for i in range(16, extra_max + 1):
    cell_id = f"gsm8k_extra_{i}"
    item = gsm8k_data[str(i)]
    cell = run_gsm8k_cell(cell_id, item)
    cells.append(cell)
    mark = 'OK' if cell['is_correct'] else 'FAIL'
    err = cell.get('error') or ''
    print(f"  [{cell_id}] gold={cell['gold_answer']} extracted={cell['llm_extracted']} [{mark}] latency={cell['latency_ms']:.0f}ms note={cell['note']}{(' err=' + err[:100]) if err and cell['is_correct'] is False and not cell['note'] else ''}")
    time.sleep(SLEEP_BETWEEN)

t_total = time.time() - t_start

# ---------------- 4. 汇总 + 写 JSON ----------------
gsm8k_passed = sum(1 for c in cells if c['task'] == 'gsm8k' and c['cell_id'].startswith('gsm8k_') and not c['cell_id'].startswith('gsm8k_extra') and c['is_correct'])
strategyqa_passed = sum(1 for c in cells if c['task'] == 'strategyqa' and c['is_correct'])
extra_passed = sum(1 for c in cells if c['cell_id'].startswith('gsm8k_extra') and c['is_correct'])
total_passed = gsm8k_passed + strategyqa_passed + extra_passed
n_total = len(cells)
pass_rate = total_passed / n_total if n_total > 0 else 0

# V2 启动阈值: PASS if >=48/60 (80%), MARGINAL if 36-47 (60-79%), REGRESSION if <36
if total_passed >= 48:
    verdict = 'PASS'
elif total_passed >= 36:
    verdict = 'MARGINAL'
else:
    verdict = 'REGRESSION'

# 截断 / 判错归因
truncated_cells = [c['cell_id'] for c in cells if c.get('note', '').startswith('**truncated**')]
misjudge_cells = [c['cell_id'] for c in cells if 'semantic_misjudge' in c.get('note', '')]
no_extract_cells = [c['cell_id'] for c in cells if 'no_' in c.get('note', '') and 'extracted' in c.get('note', '')]

ts = datetime.datetime.now().astimezone().isoformat(timespec='seconds')

output = {
    "timestamp": ts,
    "phase": "V2 真实 2 周工作量 - 启动阶段(60 cells)",
    "model": SELECTED_MODEL,
    "gateway": "OpenRouter",
    "user_billing_address": "user 已换新 key (前 12 位 sk-or-v1-4490c2e2)",
    "auth": f"{api_key[:12]}...{api_key[-4:]} (key loaded from env at runtime; literal key never written to disk)",
    "max_tokens": MAX_TOKENS,
    "reasoning": "{max_tokens:0, exclude:true}",
    "proxy_cleared": True,
    "total_runtime_seconds": round(t_total, 1),
    "sanity_check": {
        "model": SELECTED_MODEL,
        "prompt": "What is 1+1?",
        "max_tokens": MAX_TOKENS,
        "status": status,
        "response_preview": (body['choices'][0].get('message', {}).get('content', '')[:80] if body and body.get('choices') else None)
    },
    "cells": cells,
    "summary": {
        "total_cells": n_total,
        "gsm8k_passed": gsm8k_passed,
        "gsm8k_total": 15,
        "strategyqa_passed": strategyqa_passed,
        "strategyqa_total": 15,
        "extra_gsm8k_passed": extra_passed,
        "extra_gsm8k_total": len([c for c in cells if c['cell_id'].startswith('gsm8k_extra')]),
        "total_passed": total_passed,
        "pass_rate": round(pass_rate, 4),
        "verdict": verdict,
        "verdict_rule": "PASS if >=48/60 (80%), MARGINAL if 36-47 (60-79%), REGRESSION if <36 (60%)",
        "truncated_cells": truncated_cells,
        "misjudge_cells": misjudge_cells,
        "no_extract_cells": no_extract_cells
    },
    "comparison": {
        "kt_a1_llm_30cells_v0_2026_09_09": "7/30 (Doubao 退化 random)",
        "v4_1_flash_30cells_v3_max2048": "25/30 = 83.3% MARGINAL",
        "v4_1_flash_60cells_v2_startup_max1024": f"{total_passed}/{n_total} = {pass_rate*100:.1f}% (verdict={verdict}, trunc={len(truncated_cells)}, misjudge={len(misjudge_cells)})"
    },
    "next_phase": {
        "phase_2_300_cells": "5-6h(若 60 cells ≥ 51/60 = 85%,启动)",
        "phase_3_bootstrap_10k": "2-3h",
        "phase_4_bpa_real": "2-3h"
    },
    "constraints_honored": {
        "no_proxy": True,
        "key_runtime_only": True,
        "key_in_json_masked": True,
        "no_model_switch": True,
        "no_retry": True,
        "no_v4_fallback": True,
        "anchors_5json_untouched": True,
        "spec_v01_untouched": True
    }
}

out_path = r'D:\私人资料\deposon-repo\results\deposon_v41_flash_60cells_v2_2026_09_10.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 80)
print(f"[STEP 3] JSON written: {out_path}")
print(f"[STEP 3] summary: gsm8k={gsm8k_passed}/15, strategyqa={strategyqa_passed}/15, extra={extra_passed}/{len([c for c in cells if c['cell_id'].startswith('gsm8k_extra')])}, total={total_passed}/{n_total}, verdict={verdict}")
print(f"[STEP 3] total_runtime: {t_total:.1f}s (avg {t_total/n_total:.1f}s/cell)")
print(f"[STEP 3] truncations: {truncated_cells}")
print(f"[STEP 3] semantic_misjudge: {misjudge_cells}")
print(f"[STEP 3] no_extract: {no_extract_cells}")
print(f"[STEP 3] key in JSON: {mask_key(api_key)} (masked)")
print(f"[DONE] model={SELECTED_MODEL} max_tokens={MAX_TOKENS} reasoning stripped")
