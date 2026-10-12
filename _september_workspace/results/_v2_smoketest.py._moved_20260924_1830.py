"""Smoke test: 1 chat call + 1 embed call to verify the API works."""
import os, sys, io, re, json, time, urllib.request, urllib.error

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'

text = io.open(KEY_FILE, 'r', encoding='gb18030').read()
m = re.search(r'ark-[REDACTED][a-zA-Z0-9-]+', text)
api_key = m.group(0)
print(f'KEY: {api_key[:18]}... (len={len(api_key)})')

# Clear proxies
for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy']:
    os.environ.pop(k, None)

# Test 1: chat
print('--- chat test ---')
body = json.dumps({
    "model": "doubao-seed-2.0-lite",
    "messages": [{"role": "user", "content": "What is 1+1? Answer with single digit."}],
    "max_tokens": 16,
    "temperature": 0.0,
}).encode('utf-8')
req = urllib.request.Request(
    f'{BASE_URL}/chat/completions', data=body,
    headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
    method='POST',
)
t0 = time.time()
with urllib.request.urlopen(req, timeout=30) as resp:
    data = resp.read().decode('utf-8')
    j = json.loads(data)
    print(f'chat: http={resp.status} ms={int((time.time()-t0)*1000)} content="{j["choices"][0]["message"]["content"]}"')

# Test 2: text embed
print('--- text embed test ---')
body = json.dumps({
    "model": "doubao-embedding-vision-251215",
    "input": ["Concept graph S1 (family=S, structure=chain): sample label"],
}).encode('utf-8')
req = urllib.request.Request(
    f'{BASE_URL}/embeddings', data=body,
    headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
    method='POST',
)
t0 = time.time()
with urllib.request.urlopen(req, timeout=30) as resp:
    data = resp.read().decode('utf-8')
    j = json.loads(data)
    emb = j['data'][0]['embedding']
    print(f'embed: http={resp.status} ms={int((time.time()-t0)*1000)} dim={len(emb)} first4={emb[:4]}')

print('--- smoke test passed ---')
