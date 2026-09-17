# -*- coding: utf-8 -*-
"""
deposon V3.X 挂点预筛 - 火山方舟 coding-plan 'glm-latest' 别名 30 cells V2 改进重试
- 严格不重试 / 不切 model / 不设 proxy
- key runtime 读 + 永不入 JSON
- 渐进式 3 阶段: 1-cell sanity (30s) -> 5 cells (60s) -> 30 cells (90s)
- 每阶段独立落盘 final path(不创建 _ 前缀临时文件)
- 详细日志: http_status / latency / error 不抑制
- 失败立即标 fail 但继续(不阻塞)
"""
import os, json, time, re, sys
import urllib.request, urllib.error

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
GSM8K_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
STRATEGYQA_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
TARGET_MODEL = 'glm-latest'
SANITY_PROMPT = 'What is 1+1?'
SANITY_MAX_TOKENS = 1024
CELL_MAX_TOKENS = 2048
PROXY_KEYS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']

OUTPUT_5 = r'D:\私人资料\deposon-repo\results\deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json'
OUTPUT_30 = r'D:\私人资料\deposon-repo\results\deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json'
DOC_30 = r'D:\私人资料\deposon-repo\docs\V3X\VOLCENGINE_GLM_LATEST_30CELLS_V2_2026_09_10.md'

# ============== 1) Read key (GB18030) ==============
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
    print('FATAL: ark-[REDACTED]* key not found in key file')
    sys.exit(2)
api_key = m.group(0)
key_truncated = api_key[:20] + '...' + api_key[-4:]
os.environ['ARK_CODING_PLAN_KEY'] = api_key
for k in PROXY_KEYS:
    os.environ.pop(k, None)
print(f'[KEY] encoding={enc} key_truncated={key_truncated}')

# ============== 2) Load benchmarks ==============
with open(GSM8K_FILE, 'r', encoding='utf-8') as f:
    gsm8k = json.load(f)
with open(STRATEGYQA_FILE, 'r', encoding='utf-8') as f:
    strategyqa = json.load(f)
print(f'[BENCH] gsm8k_ids={len(gsm8k)} strategyqa_ids={len(strategyqa)}')


# ============== 3) HTTP query ==============
def query_chat(prompt, model=TARGET_MODEL, max_tokens=CELL_MAX_TOKENS, timeout=90):
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
            return {
                'status': resp.status,
                'ms': round(elapsed_ms, 1),
                'body': body,
                'error': None
            }
    except urllib.error.HTTPError as e:
        elapsed_ms = (time.time() - t0) * 1000
        err_raw = e.read().decode('utf-8', errors='replace') if e.fp else ''
        return {
            'status': e.code,
            'ms': round(elapsed_ms, 1),
            'body': None,
            'error': err_raw[:500]
        }
    except Exception as e:
        elapsed_ms = (time.time() - t0) * 1000
        return {
            'status': -1,
            'ms': round(elapsed_ms, 1),
            'body': None,
            'error': f'{type(e).__name__}: {str(e)[:300]}'
        }


def extract_text(body):
    if not body or not isinstance(body, dict):
        return ''
    try:
        return body['choices'][0]['message']['content']
    except Exception:
        return ''


def extract_number(s):
    if s is None:
        return None
    s = str(s).strip()
    m = re.findall(r'-?\d+(?:\.\d+)?', s)
    if not m:
        return None
    try:
        return float(m[-1])
    except Exception:
        return None


def extract_yesno(s):
    if s is None:
        return None
    s = str(s).lower().strip()
    # Find first yes/no token
    yes_match = re.search(r'\b(yes|true|correct)\b', s)
    no_match = re.search(r'\b(no|false|incorrect)\b', s)
    if yes_match and no_match:
        # ambiguous, pick whichever appears first
        if yes_match.start() < no_match.start():
            return 'Yes'
        return 'No'
    if yes_match:
        return 'Yes'
    if no_match:
        return 'No'
    return None


# ============== STAGE 1: 1-cell sanity (30s) ==============
print('=' * 60)
print('[STAGE 1] 1-cell sanity (30s timeout)')
print('=' * 60)
t_stage1 = time.time()
sanity = query_chat(SANITY_PROMPT, TARGET_MODEL, SANITY_MAX_TOKENS, timeout=30)
sanity_text = extract_text(sanity['body'])
sanity_pass = (sanity['status'] == 200) and (sanity_text and '2' in sanity_text)
sanity_log = {
    'model': TARGET_MODEL,
    'prompt': SANITY_PROMPT,
    'status': sanity['status'],
    'ms': sanity['ms'],
    'response_text': sanity_text,
    'error': sanity['error'] if sanity['status'] != 200 else None
}
print(f'  status={sanity["status"]} ms={sanity["ms"]} text={sanity_text!r} pass={sanity_pass}')

if not sanity_pass:
    print('[STOP] sanity FAILED -> write sanity_failed 5cells JSON then exit')
    elapsed_s1 = round(time.time() - t_stage1, 1)
    out = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
        'stage': 'stage1_sanity_failed_aborted',
        'model': TARGET_MODEL,
        'gateway': '火山方舟 Coding Plan',
        'base_url': BASE_URL,
        'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
        'sanity_check': f'{SANITY_PROMPT} -> {sanity_text!r} FAIL',
        'sanity_log': sanity_log,
        'cells': [],
        'summary': {
            'total_cells': 0,
            'matched': 0,
            'match_rate': '0/0',
            'elapsed_s_stage1': elapsed_s1,
            'verdict': f'glm-latest 别名不可调 (status={sanity["status"]}, error={sanity["error"][:200] if sanity["error"] else "none"})'
        }
    }
    os.makedirs(os.path.dirname(OUTPUT_5), exist_ok=True)
    with open(OUTPUT_5, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'[WROTE] {OUTPUT_5} (size={os.path.getsize(OUTPUT_5)}B)')
    print(f'[ABORTED] elapsed_stage1={elapsed_s1}s')
    sys.exit(0)

print(f'[STAGE 1 OK] sanity PASS in {sanity["ms"]}ms')


# ============== STAGE 2: 5 cells GSM8K id 1-5 (60s) ==============
print('=' * 60)
print('[STAGE 2] 5 cells GSM8K id 1-5 (60s timeout each)')
print('=' * 60)
t_stage2 = time.time()
cells_5 = []
for i in range(1, 6):
    item = gsm8k.get(str(i), {})
    question = item.get('question', '')
    expected = item.get('answer', None)
    if not question or expected is None:
        print(f'[SKIP id={i}] missing question or answer')
        continue
    prompt = f'Question: {question}\nAnswer in one number:'
    print(f'[CELL id={i}] expected={expected} q_len={len(question)}')
    r = query_chat(prompt, TARGET_MODEL, CELL_MAX_TOKENS, timeout=60)
    text = extract_text(r['body'])
    pred = extract_number(text)
    is_correct = (pred is not None and abs(pred - float(expected)) < 1e-3)
    usage = (r['body'] or {}).get('usage', {}) if isinstance(r['body'], dict) else {}
    cells_5.append({
        'id': i,
        'benchmark': 'gsm8k',
        'question': question,
        'expected_answer': expected,
        'prompt': prompt,
        'status': r['status'],
        'ms': r['ms'],
        'response_text': text,
        'extracted_number': pred,
        'is_correct': bool(is_correct),
        'error': r['error'] if r['status'] != 200 else None,
        'usage': usage
    })
    print(f'  status={r["status"]} ms={r["ms"]} pred={pred} correct={is_correct}')

matched_5 = sum(1 for c in cells_5 if c['is_correct'])
elapsed_s2 = round(time.time() - t_stage2, 1)
out_5 = {
    'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
    'stage': 'stage2_5cells_passed',
    'model': TARGET_MODEL,
    'gateway': '火山方舟 Coding Plan',
    'base_url': BASE_URL,
    'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
    'sanity_check': f'{SANITY_PROMPT} -> {sanity_text!r} PASS',
    'sanity_log': sanity_log,
    'cells': cells_5,
    'summary': {
        'total_cells': len(cells_5),
        'matched': matched_5,
        'match_rate': f'{matched_5}/{len(cells_5)}',
        'elapsed_s_stage2': elapsed_s2,
        'verdict': 'glm-latest 接入 + GSM8K 5 cells 全 PASS' if matched_5 == len(cells_5) else (
            'glm-latest 接入 + GSM8K 5 cells 部分 PASS' if matched_5 > 0 else 'glm-latest 接入但 GSM8K 0/5')
    }
}
os.makedirs(os.path.dirname(OUTPUT_5), exist_ok=True)
with open(OUTPUT_5, 'w', encoding='utf-8') as f:
    json.dump(out_5, f, ensure_ascii=False, indent=2)
print(f'[WROTE] {OUTPUT_5} (size={os.path.getsize(OUTPUT_5)}B)')


# ============== STAGE 3: 30 cells (15 GSM8K + 15 StrategyQA) (90s) ==============
print('=' * 60)
print('[STAGE 3] 30 cells (15 GSM8K + 15 StrategyQA) (90s timeout each)')
print('=' * 60)
t_stage3 = time.time()
cells_30 = []
# 15 GSM8K (id 1-15)
for i in range(1, 16):
    item = gsm8k.get(str(i), {})
    question = item.get('question', '')
    expected = item.get('answer', None)
    if not question or expected is None:
        print(f'[SKIP gsm8k id={i}] missing')
        cells_30.append({
            'id': i, 'benchmark': 'gsm8k', 'skipped': True, 'reason': 'missing data',
            'is_correct': False
        })
        continue
    prompt = f'Question: {question}\nAnswer in one number:'
    print(f'[GSM8K id={i}] expected={expected}')
    r = query_chat(prompt, TARGET_MODEL, CELL_MAX_TOKENS, timeout=90)
    text = extract_text(r['body'])
    pred = extract_number(text)
    is_correct = (pred is not None and abs(pred - float(expected)) < 1e-3)
    usage = (r['body'] or {}).get('usage', {}) if isinstance(r['body'], dict) else {}
    cells_30.append({
        'id': i,
        'benchmark': 'gsm8k',
        'question': question,
        'expected_answer': expected,
        'prompt': prompt,
        'status': r['status'],
        'ms': r['ms'],
        'response_text': text,
        'extracted_number': pred,
        'is_correct': bool(is_correct),
        'error': r['error'] if r['status'] != 200 else None,
        'usage': usage
    })
    print(f'  status={r["status"]} ms={r["ms"]} pred={pred} correct={is_correct}')

# 15 StrategyQA (id 1-15)
for i in range(1, 16):
    item = strategyqa.get(str(i), {})
    question = item.get('question', '')
    expected = item.get('answer', None)
    if not question or expected is None:
        print(f'[SKIP strategyqa id={i}] missing')
        cells_30.append({
            'id': i, 'benchmark': 'strategyqa', 'skipped': True, 'reason': 'missing data',
            'is_correct': False
        })
        continue
    prompt = f'Question: {question}\nAnswer in Yes or No:'
    print(f'[StrategyQA id={i}] expected={expected}')
    r = query_chat(prompt, TARGET_MODEL, CELL_MAX_TOKENS, timeout=90)
    text = extract_text(r['body'])
    pred = extract_yesno(text)
    is_correct = (pred is not None and pred.lower() == str(expected).lower())
    usage = (r['body'] or {}).get('usage', {}) if isinstance(r['body'], dict) else {}
    cells_30.append({
        'id': i,
        'benchmark': 'strategyqa',
        'question': question,
        'expected_answer': expected,
        'prompt': prompt,
        'status': r['status'],
        'ms': r['ms'],
        'response_text': text,
        'extracted_label': pred,
        'is_correct': bool(is_correct),
        'error': r['error'] if r['status'] != 200 else None,
        'usage': usage
    })
    print(f'  status={r["status"]} ms={r["ms"]} pred={pred} correct={is_correct}')

# 30 cells summary
gsm_total = sum(1 for c in cells_30 if c.get('benchmark') == 'gsm8k')
gsm_pass = sum(1 for c in cells_30 if c.get('benchmark') == 'gsm8k' and c.get('is_correct'))
sq_total = sum(1 for c in cells_30 if c.get('benchmark') == 'strategyqa')
sq_pass = sum(1 for c in cells_30 if c.get('benchmark') == 'strategyqa' and c.get('is_correct'))
total_pass = gsm_pass + sq_pass
http_200 = sum(1 for c in cells_30 if c.get('status') == 200)
total_tokens = sum((c.get('usage') or {}).get('total_tokens', 0) for c in cells_30)
total_latency = sum(c.get('ms', 0) for c in cells_30)
elapsed_s3 = round(time.time() - t_stage3, 1)
total_elapsed = round(time.time() - t_stage1, 1)

if total_pass >= 24:  # 80% threshold
    verdict = 'PASS (30 cells V2 接入成功,可挂 deposon V3.X 候选池)'
elif total_pass >= 18:  # 60% threshold
    verdict = 'PARTIAL (30 cells V2 接入但准确率 <80%,需人工复审)'
elif http_200 == 30:
    verdict = 'FAIL (30 cells V2 接入但准确率 <60%,不挂候选池)'
else:
    verdict = f'FAIL (30 cells V2 部分 HTTP 失败 {http_200}/30, 准确率 {total_pass}/30,需排查)'

out_30 = {
    'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
    'stage': 'stage3_30cells_done',
    'model': TARGET_MODEL,
    'gateway': '火山方舟 Coding Plan',
    'base_url': BASE_URL,
    'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
    'sanity_check': f'{SANITY_PROMPT} -> {sanity_text!r} PASS',
    'sanity_log': sanity_log,
    'stage2_5cells_summary': {
        'matched': matched_5,
        'total': len(cells_5),
        'rate': f'{matched_5}/{len(cells_5)}',
        'elapsed_s': elapsed_s2
    },
    'cells': cells_30,
    'summary': {
        'total_cells': len(cells_30),
        'gsm8k_passed': gsm_pass,
        'gsm8k_total': gsm_total,
        'strategyqa_passed': sq_pass,
        'strategyqa_total': sq_total,
        'total_passed': total_pass,
        'pass_rate': round(total_pass / max(1, len(cells_30)), 4),
        'http_200': http_200,
        'total_tokens': total_tokens,
        'total_latency_ms': round(total_latency, 1),
        'avg_latency_ms': round(total_latency / max(1, len(cells_30)), 1),
        'elapsed_s_stage3': elapsed_s3,
        'elapsed_s_total': total_elapsed,
        'verdict': verdict
    }
}
os.makedirs(os.path.dirname(OUTPUT_30), exist_ok=True)
with open(OUTPUT_30, 'w', encoding='utf-8') as f:
    json.dump(out_30, f, ensure_ascii=False, indent=2)
print(f'[WROTE] {OUTPUT_30} (size={os.path.getsize(OUTPUT_30)}B)')


# ============== STAGE 4: V3X doc (3-5 KB) ==============
doc_content = f"""# 火山方舟 glm-latest 别名 30 cells V2 报告(2026-09-10)

## 1. 任务背景

deposon V3.X 挂点预筛 - 复审 **火山方舟 Coding Plan** 下 `glm-latest` 别名的 30 cells 真实能力。
上次 `bg_2e977e76` succeeded 但 0 output 异常(无详细日志、无失败标记、无落盘)。
本轮采用 **渐进式 3 阶段 + 详细日志 + 直接落盘 final path** 重试。

## 2. 关键改进(V1 -> V2)

| 维度 | V1 (上次) | V2 (本轮) |
|---|---|---|
| sanity timeout | 120s | **30s(快失败)** |
| 5 cells timeout | 180s | **60s(短超时)** |
| 30 cells timeout | 120s | **90s(适中,避免 2h 卡死)** |
| 执行模式 | 单次 | **3 阶段渐进:1 -> 5 -> 30** |
| 日志详细度 | 抑制 | **http_status / latency / error 全开** |
| 落盘方式 | 临时 + 改名 | **直接落盘 final path(不创建 _ 前缀)** |
| 失败处理 | 卡死 | **立即标 fail 但继续(不阻塞)** |

## 3. 执行配置

- **模型别名**: `{TARGET_MODEL}`(严格,未切 model)
- **Endpoint**: `{BASE_URL}/chat/completions`
- **Key 来源**: `C:\\Users\\Administrator\\Desktop\\AI\\LLM API.txt` GB18030 -> `os.environ['ARK_CODING_PLAN_KEY']`(**永不入 JSON**)
- **Proxy**: **不设**(火山国内)
- **temperature**: 0.0(全 benchmark 严格)
- **max_tokens**: sanity=1024, cell=2048
- **Benchmark 题集**:
  - GSM8K id 1-15(15 题,答案数字)
  - StrategyQA id 1-15(15 题,答案 Yes/No)

## 4. 三阶段结果

### 4.1 阶段 1:sanity (30s)

- **Prompt**: `{SANITY_PROMPT}`
- **Expected**: 包含 `2`
- **实际**: status=`{sanity_log['status']}` ms=`{sanity_log['ms']}` text=`{sanity_log['response_text']!r}` error=`{sanity_log['error']}`
- **结论**: **{'PASS' if sanity_pass else 'FAIL'}**

### 4.2 阶段 2:5 cells (60s/题, GSM8K id 1-5)

- **匹配**: **{matched_5}/{len(cells_5)}** ({round(matched_5/max(1,len(cells_5))*100, 1)}%)
- **耗时**: {elapsed_s2}s
- **结果**: 详细见 `{OUTPUT_5}`

### 4.3 阶段 3:30 cells (90s/题, 15 GSM8K + 15 StrategyQA)

| 维度 | 值 |
|---|---|
| 总题数 | {len(cells_30)} |
| GSM8K 通过 | {gsm_pass}/{gsm_total} ({round(gsm_pass/max(1,gsm_total)*100, 1)}%) |
| StrategyQA 通过 | {sq_pass}/{sq_total} ({round(sq_pass/max(1,sq_total)*100, 1)}%) |
| **总通过** | **{total_pass}/{len(cells_30)}** ({round(total_pass/max(1,len(cells_30))*100, 1)}%) |
| HTTP 200 比例 | {http_200}/{len(cells_30)} |
| 总 tokens | {total_tokens} |
| 总 latency | {round(total_latency, 1)}ms |
| 平均 latency | {round(total_latency/max(1,len(cells_30)), 1)}ms/题 |
| 阶段 3 耗时 | {elapsed_s3}s |
| **总耗时** | **{total_elapsed}s** |

### 4.4 最终 verdict

**{verdict}**

## 5. 已知约束

- 严格 7 条铁律全部满足:不重试 / 不切 model / 不设 proxy / key 永不入盘 / 不动 5 锚 JSON / 不动 SPEC V0.1 / 不动 v19 / v21 frozen JSON
- 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan
- 模型别名严格 `glm-latest`(不替换为具体 GLM-5.x 版本号)

## 6. 输出文件

- `results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json`
- `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json`
- `docs/V3X/VOLCENGINE_GLM_LATEST_30CELLS_V2_2026_09_10.md`(本文件)

## 7. 后续动作

- **PASS (≥24/30)**: glm-latest 挂入 deposon V3.X 候选池,可参与王老师 WeChat 5 候选(连同 P-A/B/C/D + V4.1-Flash)挂点讨论
- **PARTIAL (18-23/30)**: 留待人工复审,2 周后可再跑 1 次
- **FAIL (<18/30)**: 排除出 V3.X 候选池,记录 1 周判死 FAIL 原因
"""
os.makedirs(os.path.dirname(DOC_30), exist_ok=True)
with open(DOC_30, 'w', encoding='utf-8') as f:
    f.write(doc_content)
print(f'[WROTE] {DOC_30} (size={os.path.getsize(DOC_30)}B)')

print('=' * 60)
print(f'[ALL DONE] verdict={verdict}')
print(f'  5cells:  {matched_5}/{len(cells_5)}')
print(f'  30cells: {total_pass}/{len(cells_30)} (gsm8k={gsm_pass}/{gsm_total}, strategyqa={sq_pass}/{sq_total})')
print(f'  http_200: {http_200}/{len(cells_30)}')
print(f'  total_elapsed: {total_elapsed}s')
print('=' * 60)
