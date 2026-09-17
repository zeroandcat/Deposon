# -*- coding: utf-8 -*-
"""
Volcengine /api/coding/v3 + doubao-embedding-vision-251215 embedding 测试
- key 从 LLM API.txt (GB18030) 读 → os.environ['ARK_API_KEY'], 永不入 prompt/JSON/盘
- 不设 proxy
- 1 sanity + 3 cells = 4 次 POST /embeddings
"""
import os, re, json, time, urllib.request, urllib.error

KEY_FILE = r'C:\Users\Administrator\Desktop\AI\LLM API.txt'
TARGET_KEY_PREFIX = 'ark-[REDACTED]'  # user 17:15 指定的那个
BASE_URL = 'https://ark.cn-beijing.volces.com/api/coding/v3'
MODEL = 'doubao-embedding-vision-251215'
ENDPOINT = f'{BASE_URL}/embeddings'

GSM8K_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_gsm8k_details.json'
SQA_FILE = r'D:\私人资料\deposon-repo\results\deposon_benchmark_v1_4_strategyqa_details.json'
OUT_JSON = r'D:\私人资料\deposon-repo\results\deposon_volcengine_doubao_embedding_2026_09_10.json'


def load_key():
    c = open(KEY_FILE, 'r', encoding='gb18030').read()
    ms = re.findall(r'ark-[a-zA-Z0-9-]+', c)
    for m in ms:
        if m.startswith(TARGET_KEY_PREFIX):
            return m
    raise RuntimeError(f'未找到前缀 {TARGET_KEY_PREFIX} 的 key,实际找到: {[x[:12] for x in ms]}')


def kill_proxy():
    for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy',
              'ALL_PROXY', 'all_proxy']:
        os.environ.pop(k, None)


def call_embed(text, model=MODEL, timeout=30):
    headers = {
        'Authorization': f'Bearer {os.environ["ARK_API_KEY"]}',
        'Content-Type': 'application/json',
    }
    data = json.dumps({'model': model, 'input': text}).encode('utf-8')
    req = urllib.request.Request(ENDPOINT, data=data, headers=headers, method='POST')
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode('utf-8')
            return {
                'status': resp.status,
                'latency_ms': round((time.time() - t0) * 1000, 1),
                'body': json.loads(body),
                'raw': body[:500],
            }
    except urllib.error.HTTPError as e:
        err = e.read().decode('utf-8', errors='replace') if e.fp else ''
        return {
            'status': e.code,
            'latency_ms': round((time.time() - t0) * 1000, 1),
            'body': None,
            'raw': err[:500],
        }
    except Exception as e:
        return {
            'status': -1,
            'latency_ms': round((time.time() - t0) * 1000, 1),
            'body': None,
            'raw': f'{type(e).__name__}: {e}',
        }


def main():
    api_key = load_key()
    os.environ['ARK_API_KEY'] = api_key
    kill_proxy()

    # 不打 key 字面值,只打前缀
    print(f'[init] key prefix = {api_key[:12]}… len={len(api_key)}')
    print(f'[init] endpoint   = {ENDPOINT}')
    print(f'[init] model      = {MODEL}')
    print(f'[init] proxy env  = HTTP_PROXY={os.environ.get("HTTP_PROXY")} HTTPS_PROXY={os.environ.get("HTTPS_PROXY")} (空=无)')
    print()

    # 1) sanity
    print('--- Step 1: 1-cell sanity ---')
    s = call_embed('What is 2+2?')
    print(f'  status={s["status"]}  latency={s["latency_ms"]}ms')
    sanity_dim = None
    sanity_status = s['status']
    if s['body'] and 'data' in s['body'] and s['body']['data']:
        sanity_dim = len(s['body']['data'][0].get('embedding', []))
        print(f'  dim={sanity_dim}  first5={s["body"]["data"][0].get("embedding", [])[:5]}')
        print(f'  usage={s["body"].get("usage")}')
    else:
        print(f'  raw={s["raw"]}')

    # 2) 3 cells
    print()
    print('--- Step 2: 3 cells ---')
    gsm = json.load(open(GSM8K_FILE, 'r', encoding='utf-8'))
    sqa = json.load(open(SQA_FILE, 'r', encoding='utf-8'))
    cells_spec = [
        ('GSM8K_id1', gsm['1']['question']),
        ('GSM8K_id2', gsm['2']['question']),
        ('StrategyQA_id1', sqa['1']['question']),
    ]
    cells = []
    for name, text in cells_spec:
        r = call_embed(text)
        rec = {
            'name': name,
            'input_chars': len(text),
            'input_preview': text[:160].replace('\n', ' '),
            'http_status': r['status'],
            'latency_ms': r['latency_ms'],
        }
        if r['body'] and 'data' in r['body'] and r['body']['data']:
            emb = r['body']['data'][0].get('embedding', [])
            rec['embedding_dim'] = len(emb)
            rec['embedding_first5'] = emb[:5]
            rec['embedding_last5'] = emb[-5:]
            rec['embedding_norm'] = round(sum(x*x for x in emb) ** 0.5, 4)
            rec['usage'] = r['body'].get('usage')
            rec['model_returned'] = r['body'].get('model')
            rec['passed'] = r['status'] == 200 and len(emb) > 0
        else:
            rec['passed'] = False
            rec['error_raw'] = r['raw']
        cells.append(rec)
        print(f'  {name}: status={rec["http_status"]} dim={rec.get("embedding_dim")} latency={rec["latency_ms"]}ms passed={rec["passed"]}')

    # 3) verdict
    passed_count = sum(1 for c in cells if c['passed'])
    if passed_count == 3 and sanity_status == 200 and sanity_dim:
        verdict = 'PASS'
    elif passed_count >= 1:
        verdict = 'GRAY'
    else:
        verdict = 'FAIL'

    out = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
        'model': MODEL,
        'gateway': '火山方舟 Coding Plan (/api/coding/v3)',
        'base_url': BASE_URL,
        'auth': f'{api_key[:12]}…(key loaded from env; literal key never written to disk)',
        'sanity_check': {
            'input': 'What is 2+2?',
            'http_status': sanity_status,
            'embedding_dim': sanity_dim,
            'latency_ms': s['latency_ms'],
            'passed': sanity_status == 200 and sanity_dim is not None and sanity_dim > 0,
        },
        'cells': cells,
        'summary': {
            'total_cells': 3,
            'passed': passed_count,
            'verdict': verdict,
            'sanity_passed': sanity_status == 200 and sanity_dim is not None and sanity_dim > 0,
        },
        'comparison': {
            'volcengine_v3_endpoint_wrong_8_models_404': '0/3 (wrong endpoint /v3)',
            'volcengine_coding_v3_endpoint_correct': f'{passed_count}/3 (this run)',
        },
    }
    with open(OUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print()
    print(f'[done] verdict={verdict}  passed={passed_count}/3')
    print(f'[done] wrote {OUT_JSON}')


if __name__ == '__main__':
    main()
