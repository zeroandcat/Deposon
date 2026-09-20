#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quick test: just read key + 1 sanity call to verify env works"""
import os, json, time, urllib.request, urllib.error, re

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
content = open(KEY_FILE, 'r', encoding='gb18030').read()
m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', content)
if not m:
    raise SystemExit('FATAL: no key')
api_key = m.group(0)
os.environ['ARK_CODING_PLAN_KEY'] = api_key

for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(k, None)

BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
ENDPOINT = f'{BASE_URL}/chat/completions'

def query(prompt, model, max_tokens=128, timeout=30):
    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    data = {'model': model, 'messages': [{'role': 'user', 'content': prompt}], 'max_tokens': max_tokens, 'temperature': 0.0}
    req = urllib.request.Request(ENDPOINT, data=json.dumps(data, ensure_ascii=False).encode('utf-8'), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read().decode('utf-8', errors='replace'))
            text = body['choices'][0]['message']['content'] if 'choices' in body else ''
            return {'ok': True, 'status': resp.status, 'ms': int((time.time()-t0)*1000), 'text': text, 'body': body}
    except urllib.error.HTTPError as e:
        err = ''
        try: err = e.read().decode('utf-8', errors='replace')[:500]
        except: pass
        return {'ok': False, 'status': e.code, 'ms': int((time.time()-t0)*1000), 'error': err}
    except Exception as e:
        return {'ok': False, 'status': -1, 'ms': int((time.time()-t0)*1000), 'error': str(e)[:500]}

print('key prefix:', api_key[:25])
print('endpoint:', ENDPOINT)
print('---')

# Test 1 model first
r = query('What is 1+1? Answer with just the number in bold.', 'kimi-k2.7-code')
print('Test 1 (kimi-k2.7-code):', r.get('status'), r.get('ms'), 'ms')
print('  text:', r.get('text', '')[:200])
if not r.get('ok'):
    print('  ERR:', r.get('error', '')[:300])
print('---')
# Test 2 different model
r2 = query('What is 1+1? Answer with just the number in bold.', 'doubao-seed-2.0-lite')
print('Test 2 (doubao-seed-2.0-lite):', r2.get('status'), r2.get('ms'), 'ms')
print('  text:', r2.get('text', '')[:200])
if not r2.get('ok'):
    print('  ERR:', r2.get('error', '')[:300])
