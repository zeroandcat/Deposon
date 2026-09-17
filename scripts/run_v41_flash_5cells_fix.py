# -*- coding: utf-8 -*-
"""
DEEPSEEK-V41-FLASH 5-CELLS FIX 2026-09-10
- Task A: re-run 5 failing cells with 3 fix-prompt strategies
  - Fix A (gsm8k_7 算错): "Let's think step by step" CoT 强制
  - Fix B (strategyqa_9 死循环): max_tokens=512 + 简短 prompt
  - Fix C (strategyqa_7/10/14 语义判错): "Answer Yes or No. Ignore the question's rhetorical framing. Be direct."
- 1-cell sanity check first (3 cells)
- 严格 v4.1-flash, 不切 model
- 7 铁律: key runtime, no proxy, masked JSON, no retry, no fallback
"""
import os
import re
import sys
import json
import time
import urllib.request
import urllib.error
import datetime

# ---------------- 0. 加载 keys (GB18030) ----------------
key_file = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
content = open(key_file, 'r', encoding='gb18030').read()

# OpenRouter key
or_match = re.search(r'sk-or-v1-[a-f0-9]{64}', content)
if not or_match:
    print("[FATAL] no sk-or-v1-... in LLM API.txt", file=sys.stderr)
    sys.exit(1)
openrouter_key = or_match.group(0)
os.environ['OPENROUTER_API_KEY'] = openrouter_key

# Ark key (火山方舟 coding-plan, 第 2 个 ark-)
ark_matches = list(re.finditer(r'ark-[a-zA-Z0-9-]+', content))
if len(ark_matches) < 2:
    print("[FATAL] need 2 ark- keys (agent-plan + coding-plan), found " + str(len(ark_matches)), file=sys.stderr)
    sys.exit(1)
ark_coding_plan_key = ark_matches[1].group(0)  # 第 2 个 = coding-plan
os.environ['ARK_API_KEY'] = ark_coding_plan_key

# TeamoRouter key
teamo_match = re.search(r'sk-teamo-[a-zA-Z0-9]+', content)
if not teamo_match:
    print("[FATAL] no sk-teamo-... in LLM API.txt", file=sys.stderr)
    sys.exit(1)
teamorouter_key = teamo_match.group(0)
os.environ['TEAMOROUTER_API_KEY'] = teamorouter_key

# 显式清空 proxy
for p in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(p, None)

# 截断显示
def mask_key(k, head=12, tail=4):
    return f"{k[:head]}...{k[-tail:]}"

# Force UTF-8 stdout
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', line_buffering=True)
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', line_buffering=True)

print(f"[INIT] OR key: {mask_key(openrouter_key)}")
print(f"[INIT] ARK key (coding-plan): {mask_key(ark_coding_plan_key)}")
print(f"[INIT] TeamoRouter key: {mask_key(teamorouter_key)}")
print(f"[INIT] proxy cleared")

# ---------------- 1. query helpers ----------------
def query_v41_flash(prompt, max_tokens=512, stop=None, temperature=0.0):
    """Task A: DeepSeek V4.1-Flash via OpenRouter"""
    url = 'https://openrouter.ai/api/v1/chat/completions'
    headers = {
        'Authorization': f'Bearer {openrouter_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': 'deepseek/deepseek-v4.1-flash',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens,
        'temperature': temperature,
        'reasoning': {'max_tokens': 0, 'exclude': True}
    }
    if stop:
        data['stop'] = stop
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode())
            return body, (time.time() - t0) * 1000, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err


def query_ark_embedding(text, model='doubao-embedding-vision'):
    """Task B: 火山方舟 doubao-embedding-vision"""
    url = 'https://ark.cn-beijing.volces.com/api/v3/embeddings'
    headers = {
        'Authorization': f'Bearer {ark_coding_plan_key}',
        'Content-Type': 'application/json'
    }
    data = {'model': model, 'input': text}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode())
            return body, (time.time() - t0) * 1000, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err


def query_teamorouter_embedding(text, model='text-embedding-3-large'):
    """Task B: TeamoRouter text-embedding-3-large"""
    url = 'https://api.teamorouter.com/v1/embeddings'
    headers = {
        'Authorization': f'Bearer {teamorouter_key}',
        'Content-Type': 'application/json'
    }
    data = {'model': model, 'input': text}
    req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode())
            return body, (time.time() - t0) * 1000, resp.status, None
    except urllib.error.HTTPError as e:
        err = e.read().decode() if e.fp else ''
        return None, (time.time() - t0) * 1000, e.code, err


# ---------------- 2. extract helpers ----------------
def extract_number(text):
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


# ---------------- 3. 加载 5 failing cells 数据 ----------------
gsm8k_path = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
strategyqa_path = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'

with open(gsm8k_path, 'r', encoding='utf-8') as f:
    gsm8k_data = json.load(f)
with open(strategyqa_path, 'r', encoding='utf-8') as f:
    strategyqa_data = json.load(f)

# 5 failing cells (per v3 report):
# - gsm8k_7: 模型算错 (Fix A: CoT)
# - strategyqa_7, 10, 14: 语义判错 (Fix C: direct)
# - strategyqa_9: 死循环 (Fix B: max_tokens=512 + short prompt)
TARGET_CELLS = [
    {'cell_id': 'gsm8k_7',        'task': 'gsm8k',      'fix': 'A', 'idx': '7'},
    {'cell_id': 'strategyqa_7',   'task': 'strategyqa', 'fix': 'C', 'idx': '7'},
    {'cell_id': 'strategyqa_9',   'task': 'strategyqa', 'fix': 'B', 'idx': '9'},
    {'cell_id': 'strategyqa_10',  'task': 'strategyqa', 'fix': 'C', 'idx': '10'},
    {'cell_id': 'strategyqa_14',  'task': 'strategyqa', 'fix': 'C', 'idx': '14'},
]

# ---------------- 4. 1-cell sanity check (3 representative fails) ----------------
print("\n[STEP 1] 1-cell sanity: 3 representative failing cells (verify still fail) ...")
sanity_results = []

# Sanity 1: gsm8k_7 (with original prompt - should still fail)
g7_item = gsm8k_data['7']
g7_prompt_orig = f"Question: {g7_item['question']}\nAnswer in one number:"
body, lat, status, err = query_v41_flash(g7_prompt_orig, max_tokens=2048)
if status == 200 and body:
    content = body['choices'][0].get('message', {}).get('content', '') or ''
    extracted = extract_number(content)
    sanity_results.append({
        'sanity_cell': 'gsm8k_7',
        'prompt_style': 'original',
        'gold': 36.0,
        'extracted': extracted,
        'raw': content[:200],
        'is_correct': extracted is not None and abs(extracted - 36.0) < 1e-3,
        'latency_ms': round(lat, 1),
        'note': 'sanity: still fail' if (extracted is None or abs(extracted - 36.0) > 1e-3) else 'sanity: pass unexpectedly'
    })
else:
    sanity_results.append({
        'sanity_cell': 'gsm8k_7',
        'prompt_style': 'original',
        'error': (err or '')[:300] if err else 'unknown',
        'latency_ms': round(lat, 1)
    })
print(f"  [gsm8k_7 sanity] status={status} extracted={sanity_results[-1].get('extracted')} note={sanity_results[-1].get('note','')}")
time.sleep(0.5)

# Sanity 2: strategyqa_9 (with original prompt - should still loop/truncate)
s9_item = strategyqa_data['9']
s9_prompt_orig = f"Question: {s9_item['question']}\nAnswer Yes or No:"
body, lat, status, err = query_v41_flash(s9_prompt_orig, max_tokens=2048)
if status == 200 and body:
    content = body['choices'][0].get('message', {}).get('content', '') or ''
    extracted = extract_yes_no(content)
    usage = body.get('usage', {})
    completion_tokens = usage.get('completion_tokens')
    sanity_results.append({
        'sanity_cell': 'strategyqa_9',
        'prompt_style': 'original',
        'gold': 'Yes',
        'extracted': extracted,
        'raw': content[:200],
        'completion_tokens': completion_tokens,
        'is_correct': extracted is not None and extracted.lower() == 'yes',
        'latency_ms': round(lat, 1),
        'note': 'sanity: still loop' if (completion_tokens is not None and completion_tokens >= 2048) else 'sanity: pass unexpectedly'
    })
else:
    sanity_results.append({
        'sanity_cell': 'strategyqa_9',
        'prompt_style': 'original',
        'error': (err or '')[:300] if err else 'unknown',
        'latency_ms': round(lat, 1)
    })
print(f"  [strategyqa_9 sanity] status={status} extracted={sanity_results[-1].get('extracted')} completion_tokens={sanity_results[-1].get('completion_tokens')} note={sanity_results[-1].get('note','')}")
time.sleep(0.5)

# Sanity 3: strategyqa_14 (with original prompt - should still misjudge)
s14_item = strategyqa_data['14']
s14_prompt_orig = f"Question: {s14_item['question']}\nAnswer Yes or No:"
body, lat, status, err = query_v41_flash(s14_prompt_orig, max_tokens=2048)
if status == 200 and body:
    content = body['choices'][0].get('message', {}).get('content', '') or ''
    extracted = extract_yes_no(content)
    sanity_results.append({
        'sanity_cell': 'strategyqa_14',
        'prompt_style': 'original',
        'gold': 'Yes',
        'extracted': extracted,
        'raw': content[:200],
        'is_correct': extracted is not None and extracted.lower() == 'yes',
        'latency_ms': round(lat, 1),
        'note': 'sanity: still misjudge' if (extracted is None or extracted.lower() != 'yes') else 'sanity: pass unexpectedly'
    })
else:
    sanity_results.append({
        'sanity_cell': 'strategyqa_14',
        'prompt_style': 'original',
        'error': (err or '')[:300] if err else 'unknown',
        'latency_ms': round(lat, 1)
    })
print(f"  [strategyqa_14 sanity] status={status} extracted={sanity_results[-1].get('extracted')} note={sanity_results[-1].get('note','')}")
time.sleep(0.5)


# ---------------- 5. 5 cells fix 重跑 ----------------
print("\n[STEP 2] Running 5 cells with fix-prompt strategies ...")
print("=" * 80)

cells = []
for tgt in TARGET_CELLS:
    cell_id = tgt['cell_id']
    task = tgt['task']
    fix = tgt['fix']
    idx = tgt['idx']

    if task == 'gsm8k':
        item = gsm8k_data[idx]
        question = item['question']
        gold = item['answer']
    else:
        item = strategyqa_data[idx]
        question = item['question']
        gold = item['answer']

    # 构造 fix prompt
    if fix == 'A':  # CoT for gsm8k
        prompt = f"Question: {question}\nLet's think step by step.\nAnswer in one number at the end:"
        max_tokens = 1024
        stop = None
    elif fix == 'B':  # strategyqa_9 short + max_tokens=512
        prompt = f"Question: {question}\nAnswer Yes or No in one word. Do not explain."
        max_tokens = 512
        stop = ['\n', '.', ',', '!', '?']
    elif fix == 'C':  # direct for strategyqa 7/10/14
        prompt = f"Question: {question}\nAnswer Yes or No. Ignore the question's rhetorical framing. Be direct."
        max_tokens = 512
        stop = None
    else:
        raise ValueError(f"unknown fix: {fix}")

    body, lat, status, err = query_v41_flash(prompt, max_tokens=max_tokens, stop=stop)

    if status != 200 or not body:
        cells.append({
            'cell_id': cell_id,
            'task': task,
            'fix_prompt_style': fix,
            'question': question,
            'gold_answer': gold,
            'llm_raw_response': None,
            'llm_extracted': None,
            'is_correct': False,
            'latency_ms': round(lat, 1),
            'http_status': status,
            'note': f'API_ERROR',
            'error': (err[:300] if err else 'unknown')
        })
        print(f"  [{cell_id}] FAIL status={status} err={err[:200] if err else 'unknown'}")
        continue

    msg = body['choices'][0].get('message', {})
    content = msg.get('content', '') or ''
    usage = body.get('usage', {})
    completion_tokens = usage.get('completion_tokens')

    if task == 'gsm8k':
        extracted = extract_number(content)
        is_correct = (extracted is not None and abs(extracted - gold) < 1e-3)
    else:
        extracted = extract_yes_no(content)
        is_correct = (extracted is not None and extracted.lower() == gold.lower())

    note_parts = []
    if completion_tokens is not None and completion_tokens >= max_tokens:
        note_parts.append(f'**truncated** (completion_tokens={completion_tokens} hit max={max_tokens})')
    if extracted is None:
        note_parts.append('**no_extract**')
    if is_correct and completion_tokens and completion_tokens < 200:
        note_parts.append('**fast_pass** (<200 tok)')
    note = ' | '.join(note_parts) if note_parts else 'clean'

    cells.append({
        'cell_id': cell_id,
        'task': task,
        'fix_prompt_style': fix,
        'fix_prompt': prompt,
        'question': question,
        'gold_answer': gold,
        'llm_raw_response': content[:500],
        'llm_extracted': extracted,
        'is_correct': is_correct,
        'latency_ms': round(lat, 1),
        'http_status': status,
        'prompt_tokens': usage.get('prompt_tokens'),
        'completion_tokens': completion_tokens,
        'reasoning_tokens': usage.get('reasoning_tokens'),
        'max_tokens_used': max_tokens,
        'stop_used': stop,
        'note': note,
        'error': None
    })
    mark = 'OK' if is_correct else 'FAIL'
    print(f"  [{cell_id}] fix={fix} gold={gold} extracted={extracted} [{mark}] lat={lat:.0f}ms ctk={completion_tokens} note={note}")
    time.sleep(0.5)


# ---------------- 6. summary + JSON 落盘 ----------------
gsm8k_passed = sum(1 for c in cells if c['task'] == 'gsm8k' and c['is_correct'])
strategyqa_passed = sum(1 for c in cells if c['task'] == 'strategyqa' and c['is_correct'])
total_passed = gsm8k_passed + strategyqa_passed

# 对比 v3: 5/5 = 100% 边际 = PASS
if total_passed == 5:
    verdict = 'ALL_PASS'
elif total_passed >= 4:
    verdict = 'MOSTLY_PASS'
elif total_passed >= 2:
    verdict = 'PARTIAL'
else:
    verdict = 'FAIL'

ts = datetime.datetime.now().astimezone().isoformat(timespec='seconds')

output = {
    "timestamp": ts,
    "model": "deepseek/deepseek-v4.1-flash",
    "gateway": "OpenRouter",
    "auth": f"{mask_key(openrouter_key)} (key loaded from env at runtime; literal key never written to disk)",
    "proxy_cleared": True,
    "task": "Task A: V4.1-Flash 5 failing cells (v3) fix with 3 prompt strategies",
    "fix_strategies": {
        "A_cot_gsm8k": "Question: {q}\\nLet's think step by step.\\nAnswer in one number at the end: [max=1024, no stop]",
        "B_short_strategyqa9": "Question: {q}\\nAnswer Yes or No in one word. Do not explain. [max=512, stop=['\\n','.',',','!','?']]",
        "C_direct_strategyqa_rhetorical": "Question: {q}\\nAnswer Yes or No. Ignore the question's rhetorical framing. Be direct. [max=512, no stop]"
    },
    "sanity_3cells_original_prompt": sanity_results,
    "cells": cells,
    "summary": {
        "total_cells": 5,
        "passed": total_passed,
        "failed": 5 - total_passed,
        "pass_rate": round(total_passed / 5, 4),
        "verdict": verdict,
        "by_fix": {
            "A_gsm8k_7": cells[0].get('is_correct') if len(cells) > 0 else None,
            "B_strategyqa_9": cells[2].get('is_correct') if len(cells) > 2 else None,
            "C_strategyqa_7": cells[1].get('is_correct') if len(cells) > 1 else None,
            "C_strategyqa_10": cells[3].get('is_correct') if len(cells) > 3 else None,
            "C_strategyqa_14": cells[4].get('is_correct') if len(cells) > 4 else None
        }
    },
    "comparison_v3": {
        "v3_5_fails": ["gsm8k_7", "strategyqa_7", "strategyqa_9", "strategyqa_10", "strategyqa_14"],
        "v3_fixes": "5/5 fixed? see summary"
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

out_path = r'D:\私人资料\deposon-repo\results\deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print("\n" + "=" * 80)
print(f"[STEP 3] JSON written: {out_path}")
print(f"[STEP 3] summary: passed={total_passed}/5, verdict={verdict}")
print(f"[STEP 3] by_fix: {output['summary']['by_fix']}")
print(f"[DONE] Task A complete.")
