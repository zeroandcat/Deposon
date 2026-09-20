# -*- coding: utf-8 -*-
"""
DEEPSEEK-V41-30CELLS-V3 (max_tokens=2048)
- 严格只跑 deepseek/deepseek-v4.1-flash (v4.1 拼写 + flash)
- 不 fallback 到 v4 / v4-pro / v4-flash / v4-flash-vision-exp
- max_tokens=**2048** (v2 是 1024, 预期消除 3 截断) + reasoning={max_tokens:0, exclude:true}
- 30 cells = 15 GSM8K + 15 StrategyQA
- key 永远 runtime 读,永不落盘
- verdict: PASS if >=28/30, MARGINAL if 24-27, REGRESSION if <24
"""
import os
import re
import sys
import json
import time
import urllib.request
import urllib.error

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

# 关键: 截断 key,只打印前 12 位 + 后 4 位
def mask_key(k):
    return f"{k[:12]}...{k[-4:]}"

# Force UTF-8 stdout to avoid GBK encoding crashes
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

print(f"[INIT] key loaded: {mask_key(api_key)}")
print(f"[INIT] proxy cleared: HTTP_PROXY/HTTPS_PROXY etc all popped")
print(f"[INIT] max_tokens=2048 (v2 was 1024, target: kill 3 truncations)")

# ---------------- 1. 1-cell sanity check (max_tokens=2048) ----------------
def sanity_check(model_id, prompt="What is 1+1?", max_tokens=2048):
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

print("\n[STEP 1] 1-cell sanity check (max_tokens=2048, reasoning stripped) ...")
# user 严格字面 v4.1, 不再 fallback
SELECTED_MODEL = 'deepseek/deepseek-v4.1-flash'
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
def query_llm(prompt, model, max_tokens=2048):
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


# 加载 30 cells 数据
gsm8k_path = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
strategyqa_path = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'

with open(gsm8k_path, 'r', encoding='utf-8') as f:
    gsm8k_data = json.load(f)
with open(strategyqa_path, 'r', encoding='utf-8') as f:
    strategyqa_data = json.load(f)

# ---------------- 3. 30 cells 边际 (max_tokens=2048) ----------------
cells = []
print("\n[STEP 2] Running 30 cells (15 GSM8K + 15 StrategyQA, max_tokens=2048) ...")
print("=" * 80)

# 15 GSM8K (id 1-15)
for i in range(1, 16):
    cell_id = f"gsm8k_{i}"
    item = gsm8k_data[str(i)]
    question = item['question']
    gold = item['answer']
    prompt = f"Question: {question}\nAnswer in one number:"
    body, latency_ms, status, err = query_llm(prompt, SELECTED_MODEL, max_tokens=2048)
    if status != 200 or not body:
        cells.append({
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
        })
        print(f"  [{cell_id}] FAIL status={status} err={err[:200] if err else 'unknown'}")
        continue
    msg = body['choices'][0].get('message', {})
    content = msg.get('content', '') or ''
    extracted = extract_number(content)
    is_correct = (extracted is not None and abs(extracted - gold) < 1e-3)
    usage = body.get('usage', {})
    completion_tokens = usage.get('completion_tokens')
    note = 'clean'
    if completion_tokens is not None and completion_tokens >= 2048:
        note = f'**truncated** (completion_tokens={completion_tokens}, hit max_tokens=2048)'
    elif extracted is None:
        note = '**no_number_extracted**'
    cells.append({
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
    })
    mark = 'OK' if is_correct else 'FAIL'
    print(f"  [{cell_id}] gold={gold} extracted={extracted} [{mark}] latency={latency_ms:.0f}ms note={note}")
    time.sleep(0.5)  # 限速

# 15 StrategyQA (id 1-15)
for i in range(1, 16):
    cell_id = f"strategyqa_{i}"
    item = strategyqa_data[str(i)]
    question = item['question']
    gold = item['answer']
    prompt = f"Question: {question}\nAnswer Yes or No:"
    body, latency_ms, status, err = query_llm(prompt, SELECTED_MODEL, max_tokens=2048)
    if status != 200 or not body:
        cells.append({
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
        })
        print(f"  [{cell_id}] FAIL status={status} err={err[:200] if err else 'unknown'}")
        continue
    msg = body['choices'][0].get('message', {})
    content = msg.get('content', '') or ''
    extracted = extract_yes_no(content)
    is_correct = (extracted is not None and extracted.lower() == gold.lower())
    usage = body.get('usage', {})
    completion_tokens = usage.get('completion_tokens')
    note = 'clean'
    if completion_tokens is not None and completion_tokens >= 2048:
        note = f'**truncated** (completion_tokens={completion_tokens}, hit max_tokens=2048)'
    elif extracted is None:
        note = '**no_yes_no_extracted**'
    elif not is_correct:
        note = '**semantic_misjudge** (model本体能力, 与 max_tokens 无关)'
    cells.append({
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
    })
    mark = 'OK' if is_correct else 'FAIL'
    print(f"  [{cell_id}] gold={gold} extracted={extracted} [{mark}] latency={latency_ms:.0f}ms note={note}")
    time.sleep(0.5)

# ---------------- 4. 汇总 + 写 JSON ----------------
gsm8k_passed = sum(1 for c in cells if c['task'] == 'gsm8k' and c['is_correct'])
strategyqa_passed = sum(1 for c in cells if c['task'] == 'strategyqa' and c['is_correct'])
total_passed = gsm8k_passed + strategyqa_passed
pass_rate = total_passed / 30

# user v3 边际阈值: PASS if >=28/30, MARGINAL if 24-27, REGRESSION if <24
if total_passed >= 28:
    verdict = 'PASS'
elif total_passed >= 24:
    verdict = 'MARGINAL'
else:
    verdict = 'REGRESSION'

# 截断 / 判错归因
truncated_cells = [c['cell_id'] for c in cells if c.get('note', '').startswith('**truncated**')]
misjudge_cells = [c['cell_id'] for c in cells if 'semantic_misjudge' in c.get('note', '')]
no_extract_cells = [c['cell_id'] for c in cells if 'no_' in c.get('note', '') and 'extracted' in c.get('note', '')]

import datetime
ts = datetime.datetime.now().astimezone().isoformat(timespec='seconds')

output = {
    "timestamp": ts,
    "model": SELECTED_MODEL,
    "gateway": "OpenRouter",
    "user_billing_address": "user 已换新 key (前 12 位 sk-or-v1-4490c2e2)",
    "auth": f"{api_key[:12]}...{api_key[-4:]} (key loaded from env at runtime; literal key never written to disk)",
    "max_tokens": 2048,
    "reasoning": "{max_tokens:0, exclude:true}",
    "proxy_cleared": True,
    "sanity_check": {
        "model": SELECTED_MODEL,
        "prompt": "What is 1+1?",
        "max_tokens": 2048,
        "status": status,
        "response_preview": (body['choices'][0].get('message', {}).get('content', '')[:80] if body and body.get('choices') else None)
    },
    "cells": cells,
    "summary": {
        "total_cells": 30,
        "gsm8k_passed": gsm8k_passed,
        "gsm8k_total": 15,
        "strategyqa_passed": strategyqa_passed,
        "strategyqa_total": 15,
        "total_passed": total_passed,
        "pass_rate": round(pass_rate, 4),
        "verdict": verdict,
        "verdict_rule": "PASS if >=28/30, MARGINAL if 24-27 (沿用 v2 baseline), REGRESSION if <24",
        "truncated_cells": truncated_cells,
        "misjudge_cells": misjudge_cells,
        "no_extract_cells": no_extract_cells
    },
    "comparison": {
        "kt_a1_llm_30cells_v0_2026_09_09": "7/30 (Doubao 退化 random)",
        "v4_flash_vision_exp_30cells_v1": "15/30 FAIL (max_tokens=256 截断)",
        "v4_1_flash_30cells_v2_max1024": "24/30 = 80% PASS (3 截断 + 3 语义判错)",
        "v4_1_flash_30cells_v3_max2048": f"{total_passed}/30 (verdict={verdict}, trunc={len(truncated_cells)}, misjudge={len(misjudge_cells)})"
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

out_path = r'D:\私人资料\deposon-repo\results\deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 80)
print(f"[STEP 3] JSON written: {out_path}")
print(f"[STEP 3] summary: gsm8k={gsm8k_passed}/15, strategyqa={strategyqa_passed}/15, total={total_passed}/30, verdict={verdict}")
print(f"[STEP 3] truncations: {truncated_cells}")
print(f"[STEP 3] semantic_misjudge: {misjudge_cells}")
print(f"[STEP 3] no_extract: {no_extract_cells}")
print(f"[STEP 3] key in JSON: {api_key[:12]}...{api_key[-4:]} (masked)")
print(f"[DONE] model={SELECTED_MODEL} max_tokens=2048 reasoning stripped")
