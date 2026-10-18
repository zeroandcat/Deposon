# -*- coding: utf-8 -*-
"""Retry OpenAI candidates one by one to find a non-downgrading, non-hanging one."""
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

def chat(model, prompt='What is 1+1? Answer with **2** at the end.', max_tokens=32, timeout=15):
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
            content = data['choices'][0]['message']['content']
            rm = data.get('model','?')
            return {'ok': True, 'rm': rm, 'content': content[:200], 'ms': (time.time()-t0)*1000,
                    'has_2': '2' in content, 'downgrade': rm != model}
    except urllib.error.HTTPError as e:
        return {'ok': False, 'status': e.code, 'err': e.read().decode()[:150] if e.fp else ''}
    except Exception as e:
        return {'ok': False, 'err': f'{type(e).__name__}: {str(e)[:150]}'}

for cand in ['gpt-5.6-luna','gpt-5.6-terra','gpt-5.4-mini','gpt-5.5','gpt-5.6-sol']:
    print(f'\n[T] {cand}', flush=True)
    r = chat(cand, timeout=25)
    print(f'[R] {json.dumps(r, ensure_ascii=False)[:400]}', flush=True)
