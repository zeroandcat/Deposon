# -*- coding: utf-8 -*-
"""Probe volcengine embedding endpoints via 1018 proxy."""
import os, re, json, time, urllib.request, urllib.error
from pathlib import Path

# Set 1018 proxy
os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1018'
os.environ['HTTP_PROXY']  = 'http://127.0.0.1:1018'
os.environ['ALL_PROXY']   = 'socks5://127.0.0.1:1018'

opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({
        'http':  'http://127.0.0.1:1018',
        'https': 'http://127.0.0.1:1018',
    })
)
urllib.request.install_opener(opener)

KEY_FILE = Path(r'C:/Users/Administrator/Desktop/AI/LLM API.txt')
content_bytes = KEY_FILE.read_bytes()
text = None
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: text = content_bytes.decode(enc); break
    except: continue

ark_matches = list(re.finditer(r'ark-[a-zA-Z0-9-]+', text))
# coding-plan key (2nd)
key = ark_matches[1].group(0)
print(f'[KEY] using coding-plan key: {key[:18]}...')
print(f'[PROXY] 1018 set (HTTPS/HTTP/ALL)\n')

# Verify proxy is reachable first
import socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    s.connect(('127.0.0.1', 1018))
    s.close()
    print('[PROXY] 1018 reachable')
except Exception as e:
    print(f'[PROXY] 1018 FAIL: {e}')

# Test via coding endpoint which was OK for vision
URL = 'https://ark.cn-beijing.volces.com/api/coding/v3/embeddings'
MODELS = [
    'doubao-embedding-vision-241215',  # we know this works
    'doubao-embedding-vision-250328',
    'doubao-embedding-vision-250615',
    'doubao-embedding-vision-251215',
    'doubao-embedding-text-240715',
    'doubao-embedding-large-text-240515',
    'doubao-embedding',
]

print(f'\n=== URL: {URL} (via 1018 proxy) ===')
for m in MODELS:
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
    data = {'model': m, 'input': 'What is 2+2?'}
    req = urllib.request.Request(URL, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            body = json.loads(r.read().decode())
            dim = len(body.get('data', [{}])[0].get('embedding', []))
            print(f'  [OK]   {m:<48s} {(time.time()-t0)*1000:.0f}ms model={body.get("model", "?")} dim={dim}')
    except urllib.error.HTTPError as e:
        err = e.read().decode()[:120] if e.fp else ''
        print(f'  [HTTP{e.code}] {m:<48s} {(time.time()-t0)*1000:.0f}ms err={err[:100]}')
    except Exception as e:
        print(f'  [ERR]  {m:<48s} {type(e).__name__}: {e}')

print('\nDONE')
