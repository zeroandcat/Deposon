# -*- coding: utf-8 -*-
"""Manual test: gpt-5.6-sol with full GSM8K prompt (1024 tokens)."""
import os, re, json, time, urllib.request, urllib.error
from pathlib import Path

os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:1018'
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:1018'

raw = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt').read_bytes()
text = ''
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: text = raw.decode(enc); break
    except: continue
KEY = re.search(r'(sk-teamo-[a-f0-9]+)', text).group(1)
print(f'[KEY] teamo={KEY[:18]}...', flush=True)

prompt = ("Question: Melanie is a door-to-door saleswoman. She sold a third of her "
          "vacuum cleaners at the green house, 2 more to the red house, and half of "
          "what was left at the orange house. If Melanie has 5 vacuum cleaners left, "
          "how many did she start with?\n\n"
          "Let's think step by step.\n"
          "Answer with the final number in **bold** at the end.")

body = json.dumps({'model':'gpt-5.6-sol', 'messages':[{'role':'user','content':prompt}],
                   'max_tokens':1024, 'temperature':0.0}).encode()
req = urllib.request.Request('https://api.teamorouter.com/v1/chat/completions',
                             data=body,
                             headers={'Authorization': f'Bearer {KEY}',
                                      'Content-Type':'application/json'},
                             method='POST')

print(f'[T0] {time.time():.0f}', flush=True)
try:
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode())
        c = data['choices'][0]['message']['content']
        print(f'OK status={r.status} content_len={len(c)} rm={data.get("model")}')
        print(f'usage: {data.get("usage")}')
        print(f'content_tail: ...{c[-200:]}')
except urllib.error.HTTPError as e:
    print(f'HTTP {e.code} {e.read().decode()[:300] if e.fp else ""}')
except Exception as e:
    print(f'ERR {type(e).__name__}: {str(e)[:200]}')

print(f'[T1] {time.time():.0f}', flush=True)
