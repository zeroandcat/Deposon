# -*- coding: utf-8 -*-
"""1-cell sanity check for 3 TeamoRouter frontier candidates.
- gpt-5.5 (OpenAI frontier)
- claude-sonnet-5 (Anthropic frontier, 3.5 sonnet 角色)
- gemini-3.1-pro-preview (Google frontier, 1.5-pro 角色)
"""
import os, re, json, time, urllib.request, urllib.error
from pathlib import Path

for k in ('HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy'):
    os.environ.pop(k, None)
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1018'
os.environ['HTTP_PROXY']  = 'http://127.0.0.1:1018'

raw = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt').read_bytes()
text = ''
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: text = raw.decode(enc); break
    except: continue
KEY = re.search(r'(sk-teamo-[a-f0-9]+)', text).group(1)
# 仅向日志/stdout 输出前 18 字符用于人眼确认存在
print(f'[KEY] teamo={KEY[:18]}...', flush=True)

BASE = 'https://api.teamorouter.com/v1'

def chat(model, prompt, max_tokens=64, timeout=30):
    url = f'{BASE}/chat/completions'
    headers = {'Authorization': f'Bearer {KEY}', 'Content-Type': 'application/json'}
    payload = {'model': model, 'messages': [{'role':'user','content':prompt}],
               'max_tokens': max_tokens, 'temperature': 0.0}
    body = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode())
            content = data['choices'][0]['message']['content']
            rm = data.get('model', '?')
            return {'ok': True, 'content': content, 'rm': rm, 'ms': (time.time()-t0)*1000,
                    'usage': data.get('usage', {}), 'raw_keys': list(data.keys())}
    except urllib.error.HTTPError as e:
        return {'ok': False, 'status': e.code, 'err': e.read().decode()[:300] if e.fp else ''}
    except Exception as e:
        return {'ok': False, 'err': f'{type(e).__name__}: {e}'}


PROMPT = "What is 1+1? Answer with the final number in **bold** at the end."

# 排序: OpenAI 先, 然后 Anthropic, 然后 Google (按 user 拍板的优先级顺序)
candidates = [
    ('openai', ['gpt-5.5', 'gpt-5.4', 'gpt-5.6-sol', 'gpt-6-astra']),
    ('anthropic', ['claude-sonnet-5', 'claude-opus-5', 'claude-opus-4-8', 'claude-sonnet-4-6']),
    ('google', ['gemini-3.1-pro-preview', 'gemini-3.5-flash', 'gemini-3.7-flash']),
]

print('\n=== 1-Cell sanity (response.model == request.model?) ===')
verdict = {}
for vendor, models in candidates:
    print(f'\n[{vendor}]')
    verdict[vendor] = {'passed': False, 'model': None}
    for m in models:
        r = chat(m, PROMPT)
        if r['ok']:
            content_head = (r['content'] or '')[:60].replace('\n',' ')
            rm = r['rm']
            match = (rm == m)
            print(f"  [{'OK' if match else 'MISMATCH'}] {m:30s} -> rm={rm:30s} ({r['ms']:.0f}ms) '{content_head}'")
            if match and '2' in (r['content'] or ''):
                verdict[vendor] = {'passed': True, 'model': m, 'rm': rm,
                                   'content': r['content'], 'latency_ms': round(r['ms'],1),
                                   'usage': r['usage'], 'raw_keys': r['raw_keys']}
                break
        else:
            print(f"  [FAIL] {m:30s} {r.get('status','?')} {r.get('err','')[:200]}")

print('\n=== Verdict ===')
for v, x in verdict.items():
    print(f"  {v}: PASSED={x['passed']} model={x.get('model','-')}")

print('\nDONE')
