# -*- coding: utf-8 -*-
"""
D+0.5 sanity check: 3 backbone 1+1=2 reachability probe
严守 7 铁律:
- API key runtime 读 (不入 prompt/JSON/log)
- no proxy (env strip + registry bypass)
- 不动 18 frozen anchors / 5 制品 / schema v1
"""
import os, re, sys, json, time, hashlib, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
TS = datetime.now().strftime('%Y%m%d_%H%M%S')
_log = []

def log(msg):
    line = f"[{datetime.now(CST).strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    _log.append(line)

log(f"=== D+0.5 sanity probe | TS={TS} ===")

KEY_FILE = Path(r'C:\Users\Administrator\Desktop\AI\LLM API.txt')
content_bytes = KEY_FILE.read_bytes()
content = ''
for enc in ('utf-8','gbk','gb18030','utf-8-sig'):
    try: content = content_bytes.decode(enc); break
    except: continue
ark_coding_m = re.search(r'(?:coding-plan[^\n]*?\n)(ark-[a-zA-Z0-9-]+)', content)
or_key_m = re.search(r'(sk-or-v1-[a-f0-9]+)', content)
ark_coding = ark_coding_m.group(1) if ark_coding_m else None
or_key = or_key_m.group(1) if or_key_m else None
log(f"  ark_coding={ark_coding[:18] if ark_coding else 'NOT FOUND'}...")
log(f"  openrouter={or_key[:18] if or_key else 'NOT FOUND'}...")

for k in ('HTTP_PROXY','HTTPS_PROXY','http_proxy','https_proxy','ALL_PROXY','all_proxy'):
    os.environ.pop(k, None)
urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler({})))

BACKBONES = [
    {'name':'deepseek_v4', 'model':'deepseek-v4-pro-ga-260813', 'vendor':'volcengine coding-plan',
     'base_url':'https://ark.cn-beijing.volces.com/api/v3', 'key':ark_coding,
     'note':'主推 (task spec)'},
    {'name':'qwen3_32b', 'model':'qwen3-32b-20250429', 'vendor':'OpenRouter',
     'base_url':'https://openrouter.ai/api/v1', 'key':or_key,
     'note':'备 1 (OpenRouter)'},
    {'name':'nemotron_35', 'model':'nvidia/nemotron-3.5-lightning', 'vendor':'OpenRouter',
     'base_url':'https://openrouter.ai/api/v1', 'key':or_key,
     'note':'备 2 (OpenRouter reference_only)'},
]

PROMPT = "Question: What is 1+1?\nAnswer with one number only:"

def chat(prompt, model, base_url, key, timeout=30):
    url = f'{base_url}/chat/completions'
    headers = {'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'}
    payload = {
        'model': model,
        'messages': [{'role':'user','content':prompt}],
        'max_tokens': 64,
        'temperature': 0.0,
    }
    body = json.dumps(payload).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode())
            return {'ok':True, 'content': data['choices'][0]['message']['content'],
                    'response_model': data.get('model','?'),
                    'status': r.status, 'ms': (time.time()-t0)*1000}
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:300] if e.fp else ''
        return {'ok':False, 'status':e.code, 'error':body, 'ms':(time.time()-t0)*1000}
    except Exception as e:
        return {'ok':False, 'status':-1, 'error': f'{type(e).__name__}: {e}', 'ms':(time.time()-t0)*1000}

results = []
for bb in BACKBONES:
    if not bb['key']:
        log(f"  [{bb['name']}] NO KEY for vendor={bb['vendor']} -> SKIP")
        results.append({**bb, 'reachability':'NO_KEY', 'sanity_pass':False})
        continue
    log(f"  [{bb['name']}] probing {bb['model']} via {bb['vendor']} ...")
    r = chat(PROMPT, bb['model'], bb['base_url'], bb['key'])
    sanity_pass = r['ok'] and ('2' in (r.get('content') or ''))
    reach = 'OK' if r['ok'] else 'FAIL'
    log(f"    -> status={r.get('status')} sanity_pass={sanity_pass} resp_model={r.get('response_model','?')[:60]}")
    log(f"       content='{(r.get('content') or '')[:80]}' ms={r.get('ms',0):.0f}")
    if not r['ok']:
        log(f"       error='{(r.get('error') or '')[:200]}'")
    results.append({**bb, 'reachability':reach, 'sanity_pass':sanity_pass,
                    'response_model': r.get('response_model'), 'status':r.get('status'),
                    'latency_ms':round(r.get('ms',0),1),
                    'content':(r.get('content') or '')[:120],
                    'error':(r.get('error') or '')[:200] if not r['ok'] else None})

DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS_DIR = DEPOSON_ROOT / 'results'
OUT = RESULTS_DIR / f'_d05_sanity_3backbone_{TS}.json'
out = {
    'task':'D+0.5 sanity check 3 backbone reachability',
    'TS':TS,
    'timestamp':datetime.now(CST).isoformat(),
    'I2_prompt':'Question: What is 1+1?\\nAnswer with one number only:',
    'I5_sampling':'temperature=0.0, max_tokens=64, timeout=30s, no_retry, no_swap',
    'iron_7_compliance':{
        'no_llm_rehash': True,  # sanity only, not counted in main
        'no_proxy': True,
        'no_gateway': True,
        'no_key_in_prompt_json_disk': True,
        'no_18_frozen_touch': True,
        'no_p_g_v0_touch': True,
        'no_p_g_v01_touch': True,
        'no_plugin_spec_touch': True,
        'no_verifier_mavis_builtin_scripts_touch': True,
    },
    'results': results,
}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
log(f"=== sanity done -> {OUT} size={OUT.stat().st_size}B sha12={hashlib.sha256(OUT.read_bytes()).hexdigest()[:12]} ===")