import sys, time
sys.path.insert(0, 'results')
from _v4_supp_l14_n11full_executor import read_api_key, call_chat, ROUTES, unset_proxy_for_qwen_mimo

route = ROUTES[0]
unset_proxy_for_qwen_mimo()
key = read_api_key(route['key_index_1based'])

for max_tok in [50, 100, 150, 200]:
    t0 = time.time()
    resp = call_chat(
        key, route['endpoint'], route['model_id'],
        [{'role': 'user', 'content': 'Say hi in 5 words.'}],
        max_tokens=max_tok, timeout=20, use_proxy=False,
    )
    elapsed = time.time() - t0
    ok = resp.get('ok')
    print(f'max_tokens={max_tok}: elapsed={elapsed:.1f}s ok={ok}')