# -*- coding: utf-8 -*-
"""Probe whether 4 vision variants return the same or different embeddings."""
import os, re, json, time, urllib.request, urllib.error
from pathlib import Path
import math

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
key = list(re.finditer(r'ark-[a-zA-Z0-9-]+', text))[1].group(0)

URL = 'https://ark.cn-beijing.volces.com/api/coding/v3/embeddings'
TEST_INPUT = 'What is 2+2?'

def get_emb(model, text):
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
    data = {'model': model, 'input': text}
    req = urllib.request.Request(URL, data=json.dumps(data).encode(), headers=headers, method='POST')
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=15) as r:
        body = json.loads(r.read().decode())
        return body['data'][0]['embedding'], body.get('model'), (time.time()-t0)*1000

MODELS = [
    'doubao-embedding-vision-241215',
    'doubao-embedding-vision-250328',
    'doubao-embedding-vision-250615',
    'doubao-embedding-vision-251215',
]

results = {}
print(f'=== Test if 4 vision variants give identical embeddings ===\n')
for m in MODELS:
    emb, rmodel, ms = get_emb(m, TEST_INPUT)
    results[m] = (emb, rmodel, ms)
    print(f'  {m:<46s} -> resp_model={rmodel}, dim={len(emb)}, {ms:.0f}ms')

print(f'\n=== Pairwise cosine similarity between 4 versions ===')
keys = list(results.keys())
for i in range(len(keys)):
    for j in range(i+1, len(keys)):
        a = results[keys[i]][0]
        b = results[keys[j]][0]
        dot = sum(x*y for x, y in zip(a, b))
        na = math.sqrt(sum(x*x for x in a))
        nb = math.sqrt(sum(x*x for x in b))
        cos = dot / (na * nb)
        print(f'  cos({keys[i][-6:]} <-> {keys[j][-6:]}) = {cos:.6f}')

# Save probe log
out = {
    'test': '4 vision variants === ?',
    'input_text': TEST_INPUT,
    'results': {m: {'response_model': v[1], 'dim': len(v[0]), 'latency_ms': v[2], 'first5': v[0][:5]} for m, v in results.items()},
}
Path('results/_probe_doubao_4versions_diff_2026_09_17.json').write_text(json.dumps(out, ensure_ascii=False, indent=2))
print(f'\nSaved results/_probe_doubao_4versions_diff_2026_09_17.json')
