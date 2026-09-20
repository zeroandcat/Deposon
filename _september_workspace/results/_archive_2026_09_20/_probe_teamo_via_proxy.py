# -*- coding: utf-8 -*-
"""Probe TeamoRouter 端点/模型 (proxy 1018). key runtime read only. 2026-09-17."""
import os, re, json, socket, urllib.request, urllib.error, time
from pathlib import Path

# 强制 proxy (env 强制 + urllib handler)
for k in ('HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy'):
    os.environ.pop(k, None)
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

KEY_FILE = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt')
content = KEY_FILE.read_bytes()
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: text = content.decode(enc); break
    except: continue

m_teamo = re.search(r'(sk-teamo-[a-f0-9]+)', text)
teamo_key = m_teamo.group(1) if m_teamo else None
print(f"[KEY] teamo={teamo_key[:18]}..." if teamo_key else "[KEY] teamo NOT FOUND")

# 候选 endpoint
endpoints = [
    ('https://api.teamo.ai/v1', 'teamo.ai'),
    ('https://api.teamo.io/v1', 'teamo.io'),
    ('https://api.teamorouter.ai/v1', 'teamorouter.ai'),
    ('https://api.teamorouter.com/v1', 'teamorouter.com'),
    ('https://api.gpt.teamo.io/v1', 'gpt.teamo.io'),
    ('https://router.teamo.io/v1', 'router.teamo.io'),
    ('https://openrouter.teamo.io/api/v1', 'openrouter.teamo.io'),
    ('https://teamo.ai/api/v1', 'teamo.ai/v1 alt'),
]

print("\n=== DNS + HTTPS connect via proxy ===")
for url, lbl in endpoints:
    host = url.split('//',1)[1].split('/',1)[0]
    try:
        ip = socket.gethostbyname(host)
        dns_ok = True
    except Exception as e:
        ip, dns_ok = f'ERR({e})', False
    print(f"  DNS {host:30s} -> {ip}  {'OK' if dns_ok else 'FAIL'}")

print("\n=== Probe each endpoint (GET /models or /v1/models) ===")
for url, lbl in endpoints:
    t0 = time.time()
    try:
        req = urllib.request.Request(f'{url}/models',
            headers={'Authorization': f'Bearer {teamo_key}'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
            nmod = len(data.get('data', []))
            sample = [m.get('id','?') for m in data.get('data',[])][:5]
            print(f"  [OK] {lbl:25s} {url}/models  n={nmod}  sample={sample}  {(time.time()-t0)*1000:.0f}ms")
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:200] if e.fp else ''
        print(f"  [HTTP{e.code}] {lbl:25s} {url}/models  {(time.time()-t0)*1000:.0f}ms  {body}")
    except Exception as e:
        print(f"  [ERR] {lbl:25s} {url}/models  {(time.time()-t0)*1000:.0f}ms  {type(e).__name__}: {e}")

print("\nDONE")
