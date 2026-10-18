# -*- coding: utf-8 -*-
"""List all 41 TeamoRouter models."""
import os, re, json, urllib.request
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

opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({'https':'http://127.0.0.1:1018','http':'http://127.0.0.1:1018'}))
urllib.request.install_opener(opener)

req = urllib.request.Request('https://api.teamorouter.com/v1/models',
                            headers={'Authorization': f'Bearer {KEY}'})
data = json.loads(urllib.request.urlopen(req, timeout=15).read().decode())
mods = sorted([m.get('id','?') for m in data.get('data', [])])
print(f'COUNT: {len(mods)}')
for m in mods:
    print(' -', m)
print('\n=== Raw sample (first 3 with full structure) ===')
for m in data.get('data', [])[:3]:
    print(json.dumps(m, ensure_ascii=False, indent=2)[:400])
