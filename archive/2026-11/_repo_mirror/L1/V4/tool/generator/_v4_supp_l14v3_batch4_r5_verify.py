import re, hashlib, json

raw = open('results/_v4_supp_l14v3_batch4_r5_result.json', 'r', encoding='utf-8').read()
patterns = [
    ('api_key_literal', r'(?i)api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{8,}'),
    ('sk_literal', r'(?i)sk-[A-Za-z0-9_\-]{8,}'),
    ('Bearer_token', r'(?i)Bearer\s+[A-Za-z0-9_\-\.]{20,}'),
    ('tp_token', r'(?i)tp-[A-Za-z0-9]{8,}'),
    ('sp_key', r'(?i)sk-sp-[A-Za-z0-9_\-\.]{8,}'),
    ('sk_teamo', r'(?i)sk-teamo-[A-Za-z0-9]{8,}'),
]
print('=== key leak self-scan ===')
for n, p in patterns:
    c = len(re.findall(p, raw))
    label = "FOUND" if c > 0 else "CLEAN"
    print(f'{label} {c}: {n}')

prior = [
    'results/_v4_supp_l14v3_batch4_r4_executor.py',
    'results/_v4_supp_l14v3_batch4_r4_result.json',
    'results/_v4_supp_l14v3_batch4_r3_executor.py',
    'results/_v4_supp_l14v3_batch4_r3_result.json',
    'results/_v4_supp_l14v3_batch4_r2_executor.py',
    'results/_v4_supp_l14v3_batch4_r2_result.json',
    'results/_v4_supp_l14v3_batch4_r1_executor.py',
    'results/_v4_supp_l14v3_batch4_r1_result.json',
    'results/_v4_supp_l14v3_batch2_r4_result.json',
    'results/_v4_supp_l14v3_batch2_r3_result.json',
    'results/_v4_supp_l14v3_batch2_r2_result.json',
    'results/_v4_supp_l14v3_batch2_r2_executor.py',
    'results/_v4_supp_l14v3_batch2_r1_result.json',
    'results/_v4_supp_l14v3_batch2_r2_models_probe.json',
    'results/_v4_supp_l14v3_batch1_r6_result.json',
    'results/_v4_supp_l14v3_batch1_r6_executor.py',
    'results/_v4_supp_l14v3_model_mapping_2026_09_24.md',
    'results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md',
]
print()
print('=== preserved prior files (no overwrite) ===')
for f in prior:
    with open(f, 'rb') as fp:
        d = fp.read()
    sha = hashlib.sha256(d).hexdigest()[:12]
    print(f'PRESERVED {sha} {len(d)}B {f}')

new = [
    'results/_v4_supp_l14v3_batch4_r5_executor.py',
    'results/_v4_supp_l14v3_batch4_r5_result.json',
    'results/_v4_supp_l14v3_batch4_r5_run.log',
    'results/_v4_supp_l14v3_batch4_r5_verify.py',
]
print()
print('=== new r5 products ===')
for f in new:
    with open(f, 'rb') as fp:
        d = fp.read()
    sha = hashlib.sha256(d).hexdigest()[:12]
    print(f'NEW {sha} {len(d)}B {f}')

print()
print('=== finish block (r5) ===')
r = json.loads(raw)
f = r['coze_teacher_side_finish']
print(f"all_22_captions_met_target: {f['all_22_captions_met_target']}")
print(f"met_target_count: {f['met_target_count']}/{f['total_captions']}")
print(f"met_target_percentage: {f['met_target_percentage']}%")
print(f"finish_status: {f['finish_status']}")
print(f"cumulative_calls_total: {f['cumulative_calls_total']}")
print(f"cumulative_empty_rate: {f['cumulative_empty_rate']}")
print(f"rounds_used: {f['rounds_used']}")

print()
print('=== per_caption 不达标列表 ===')
for cid, info in r['per_caption_successful_calls'].items():
    if not info['met_target']:
        print(f"  {cid}: succ={info['succ_count']}/5 total_calls={info['total_calls_so_far']} empty={info['empty_count_so_far']} need_more={info['need_more_to_target']}")