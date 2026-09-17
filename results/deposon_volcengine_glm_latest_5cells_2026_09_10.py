# -*- coding: utf-8 -*-
"""
deposon V3.X 挂点预筛 - 火山方舟 coding-plan 'glm-latest' 别名 5 cells smoke
- 严格不重试 / 不切 model
- 不设 proxy
- key runtime 读 + 永不入 JSON
- sanity fail 立即停,只写 minimal JSON 报告失败
- sanity pass 跑 5 cells GSM8K id 1-5
"""
import os, json, time, re, sys
import urllib.request, urllib.error

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
GSM8K_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
OUTPUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_volcengine_glm_latest_5cells_2026_09_10.json'
BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
TARGET_MODEL = 'glm-latest'
SANITY_PROMPT = 'What is 1+1?'
SANITY_MAX_TOKENS = 1024
CELL_MAX_TOKENS = 2048
PROXY_KEYS = ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']

# 1) Read key (GB18030)
enc = None
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

# 2) Load GSM8K
with open(GSM8K_FILE, 'r', encoding='utf-8') as f:
    gsm8k = json.load(f)

def query_chat(prompt, model=TARGET_MODEL, max_tokens=SANITY_MAX_TOKENS, timeout=120):
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
    # find last number-like token
    m = re.findall(r'-?\d+(?:\.\d+)?', s)
    if not m:
        return None
    try:
        return float(m[-1])
    except Exception:
        return None

# 3) Sanity check
print(f'[SANITY] model={TARGET_MODEL} prompt="{SANITY_PROMPT}"')
sanity = query_chat(SANITY_PROMPT, TARGET_MODEL, SANITY_MAX_TOKENS, timeout=120)
sanity_text = extract_text(sanity['body'])
sanity_pass = (sanity['status'] == 200) and ('2' in sanity_text)
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
    print('[STOP] sanity FAILED, write minimal JSON and exit')
    out = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
        'model': TARGET_MODEL,
        'gateway': '火山方舟 Coding Plan',
        'base_url': BASE_URL,
        'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
        'sanity_check': f'{SANITY_PROMPT} -> {sanity_text!r} {"PASS" if sanity_pass else "FAIL"}',
        'sanity_log': sanity_log,
        'cells': [],
        'summary': {
            'total_cells': 0,
            'matched': 0,
            'match_rate': '0/0',
            'verdict': f'glm-latest 别名不可调 (status={sanity["status"]})'
        },
        'comparison': {
            'doubao_seed_code_preview_251028_5cells': '5/5 PASS (sanity 100%)',
            'glm_latest_5cells_smoke': '0/5 FAIL (sanity 不通)'
        }
    }
    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'[WROTE] {OUTPUT_JSON}')
    sys.exit(0)

# 4) 5 cells GSM8K
cells = []
for i in range(1, 6):
    item = gsm8k.get(str(i), {})
    question = item.get('question', '')
    expected = item.get('answer', None)
    if not question or expected is None:
        print(f'[SKIP id={i}] missing question or answer')
        continue
    prompt = f'Question: {question}\nAnswer in one number:'
    print(f'[CELL id={i}] model={TARGET_MODEL} expected={expected}')
    r = query_chat(prompt, TARGET_MODEL, CELL_MAX_TOKENS, timeout=180)
    text = extract_text(r['body'])
    pred = extract_number(text)
    is_correct = (pred is not None and abs(pred - float(expected)) < 1e-3)
    usage = (r['body'] or {}).get('usage', {}) if isinstance(r['body'], dict) else {}
    cells.append({
        'id': i,
        'question': question,
        'expected_answer': expected,
        'status': r['status'],
        'ms': r['ms'],
        'response_text': text,
        'extracted_number': pred,
        'is_correct': bool(is_correct),
        'error': r['error'] if r['status'] != 200 else None,
        'usage': usage
    })
    print(f'  status={r["status"]} ms={r["ms"]} text={text!r} pred={pred} correct={is_correct}')

matched = sum(1 for c in cells if c['is_correct'])
out = {
    'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
    'model': TARGET_MODEL,
    'gateway': '火山方舟 Coding Plan',
    'base_url': BASE_URL,
    'auth': f'{key_truncated} (key loaded from env at runtime; literal key never written to disk)',
    'sanity_check': f'{SANITY_PROMPT} -> {sanity_text!r} PASS',
    'sanity_log': sanity_log,
    'cells': cells,
    'summary': {
        'total_cells': len(cells),
        'matched': matched,
        'match_rate': f'{matched}/{len(cells)}',
        'verdict': 'glm-latest 接入成功' if matched == len(cells) else ('glm-latest 接入但 GSM8K 5 cells 部分错误' if matched > 0 else 'glm-latest 接入失败')
    },
    'comparison': {
        'doubao_seed_code_preview_251028_5cells': '5/5 PASS (sanity 100%)',
        'glm_latest_5cells_smoke': f'{matched}/{len(cells)} (sanity 100%, 5 cells {"全 PASS" if matched == len(cells) else "部分"} )'
    }
}
os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)
with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f'[WROTE] {OUTPUT_JSON}')
print(f'[DONE] sanity=PASS 5cells={matched}/{len(cells)}')
