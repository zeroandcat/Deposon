# -*- coding: utf-8 -*-
"""Test all 3 backbones with real cell + varying max_tokens to find hang pattern."""
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

# short SQA cell (yes/no)
prompt_sqa = ("Question: Is Lord Voldemort associated with a staff member of Durmstrang?\n\n"
              "Let's think step by step.\n"
              "Answer Yes or No in **bold** at the end.")

prompt_gsm_short = "Question: Janet buys a brooch for her daughter. She pays $500 for the material to make it and then another $800 for the jeweler to construct it. After that, she pays 10% of that to get it insured. How much did she pay?\n\nLet's think step by step.\nAnswer with the final number in **bold** at the end."

def chat(model, prompt, max_tokens, timeout=25):
    body = json.dumps({'model':model,'messages':[{'role':'user','content':prompt}],
                       'max_tokens':max_tokens,'temperature':0.0}).encode()
    req = urllib.request.Request('https://api.teamorouter.com/v1/chat/completions',
                                 data=body,
                                 headers={'Authorization': f'Bearer {KEY}','Content-Type':'application/json'},
                                 method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode())
            return {'ok':True,'rm':data.get('model'),'status':r.status,
                    'content_len':len(data['choices'][0]['message']['content']),
                    'usage':data.get('usage'),
                    'ms':(time.time()-t0)*1000}
    except urllib.error.HTTPError as e:
        return {'ok':False,'status':e.code,'err':e.read().decode()[:200] if e.fp else ''}
    except Exception as e:
        return {'ok':False,'err':f'{type(e).__name__}:{str(e)[:200]}','ms':(time.time()-t0)*1000}

# Test matrix: 3 models × 2 prompts × 2 max_tokens
tests = [
    # (model, prompt, max_tokens, label)
    ('gpt-5.6-sol',       prompt_sqa,        128, 'gpt-sqa-128'),
    ('gpt-5.6-sol',       prompt_gsm_short,  256, 'gpt-gsm-256'),
    ('gpt-5.6-sol',       prompt_gsm_short,  512, 'gpt-gsm-512'),
    ('gpt-5.6-sol',       prompt_gsm_short, 1024, 'gpt-gsm-1024'),
    ('claude-sonnet-5',   prompt_sqa,        128, 'claude-sqa-128'),
    ('claude-sonnet-5',   prompt_gsm_short,  256, 'claude-gsm-256'),
    ('claude-sonnet-5',   prompt_gsm_short,  512, 'claude-gsm-512'),
    ('claude-sonnet-5',   prompt_gsm_short, 1024, 'claude-gsm-1024'),
    ('gemini-3.7-flash',  prompt_sqa,        128, 'gemini-sqa-128'),
    ('gemini-3.7-flash',  prompt_gsm_short,  256, 'gemini-gsm-256'),
    ('gemini-3.7-flash',  prompt_gsm_short,  512, 'gemini-gsm-512'),
    ('gemini-3.7-flash',  prompt_gsm_short, 1024, 'gemini-gsm-1024'),
]

for m, p, mx, lbl in tests:
    print(f'\n[{lbl}] model={m} max_tokens={mx}', flush=True)
    r = chat(m, p, mx, timeout=30)
    if r['ok']:
        print(f"  [OK] rm={r['rm']} status={r['status']} content_len={r['content_len']} {r['ms']:.0f}ms usage={r['usage']}", flush=True)
    else:
        print(f"  [FAIL] {r}", flush=True)
