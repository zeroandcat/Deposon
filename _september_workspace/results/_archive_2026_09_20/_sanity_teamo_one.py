# -*- coding: utf-8 -*-
"""Faster sanity test — one model at a time, short timeout, full flushing."""
import os, re, json, sys, time, urllib.request, urllib.error
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
print(f'[KEY] teamo={KEY[:18]}...', flush=True)

BASE = 'https://api.teamorouter.com/v1'

def chat(model, prompt='What is 1+1? Answer with **2** at the end.', max_tokens=32, timeout=20):
    url = f'{BASE}/chat/completions'
    body = json.dumps({'model': model, 'messages':[{'role':'user','content':prompt}],
                       'max_tokens': max_tokens, 'temperature': 0.0}).encode()
    req = urllib.request.Request(url, data=body,
                                 headers={'Authorization': f'Bearer {KEY}',
                                          'Content-Type':'application/json'},
                                 method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode())
            return {'ok': True, 'rm': data.get('model','?'),
                    'content': data['choices'][0]['message']['content'],
                    'ms': (time.time()-t0)*1000}
    except urllib.error.HTTPError as e:
        return {'ok': False, 'status': e.code,
                'err': e.read().decode()[:200] if e.fp else ''}
    except Exception as e:
        return {'ok': False, 'err': f'{type(e).__name__}: {str(e)[:200]}'}

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'gpt-5.5'
    print(f'[T] Testing model: {target}', flush=True)
    r = chat(target)
    print(f'[R] {json.dumps(r, ensure_ascii=False)[:400]}', flush=True)
