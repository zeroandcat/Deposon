# -*- coding: utf-8 -*-
"""Probe volcengine /api/v3/embeddings (direct, no proxy) - 4 doubao-embedding endpoints."""
import os, re, json, time, urllib.request, urllib.error
from pathlib import Path

# Force NO proxy for direct test
for k in ('HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy', 'ALL_PROXY', 'all_proxy'):
    os.environ.pop(k, None)
import urllib.request as ur
ur.install_opener(ur.build_opener(ur.ProxyHandler({})))

KEY_FILE = Path(r'C:/Users/Administrator/Desktop/AI/LLM API.txt')
content_bytes = KEY_FILE.read_bytes()
text = None
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: text = content_bytes.decode(enc); break
    except: continue

ark_matches = list(re.finditer(r'ark-[a-zA-Z0-9-]+', text))
print(f'[KEY] {len(ark_matches)} ark- keys found, prefix:')
for i, m in enumerate(ark_matches):
    print(f'  [{i}] {m.group(0)[:18]}...')
# coding-plan key (the 2nd ark- per file layout)
key = ark_matches[1].group(0)
print(f'[KEY] using coding-plan key: {key[:18]}...\n')

URLS = [
    'https://ark.cn-beijing.volces.com/api/v3/embeddings',   # the standard endpoint
    'https://ark.cn-beijing.volces.com/api/coding/v3/embeddings',  # try coding path
]

MODELS = [
    'doubao-embedding-text-240715',
    'doubao-embedding-large-text-240515',
    'doubao-embedding-vision-241215',
    'doubao-embedding',  # base fallback
]

for url in URLS:
    print(f'\n=== URL: {url} ===')
    for m in MODELS:
        headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
        data = {'model': m, 'input': 'What is 2+2?'}
        req = urllib.request.Request(url, data=json.dumps(data).encode(), headers=headers, method='POST')
        t0 = time.time()
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                body = json.loads(r.read().decode())
                print(f'  [OK] {m:<48s} status={r.status} {(time.time()-t0)*1000:.0f}ms '
                      f'model={body.get("model", "?")} '
                      f'dim={len(body.get("data", [{}])[0].get("embedding", []))}')
        except urllib.error.HTTPError as e:
            err = e.read().decode()[:120] if e.fp else ''
            print(f'  [HTTP{e.code}] {m:<48s} {(time.time()-t0)*1000:.0f}ms err={err}')
        except Exception as e:
            print(f'  [ERR] {m:<48s} {type(e).__name__}: {e}')

print('\nDONE')
