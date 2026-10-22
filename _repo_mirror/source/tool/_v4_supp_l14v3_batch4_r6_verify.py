import re, hashlib, json

raw = open('results/_v4_supp_l14v3_batch4_r6_result.json', 'r', encoding='utf-8').read()
patterns = [
    ('api_key_literal', r'(?i)api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{8,}'),
    ('sk_literal', r'(?i)sk-[A-Za-z0-9_\-]{8,}'),
    ('Bearer_token', r'(?i)Bearer\s+[A-Za-z0-9_\-\.]{20,}'),
    ('tp_token', r'(?i)tp-[A-Za-z0-9]{8,}'),
    ('sp_key', r'(?i)sk-sp-[A-Za-z0-9_\-\.]{8,}'),
    ('sk_teamo', r'(?i)sk-teamo-[A-Za-z0-9]{8,}'),
]
print('=== key leak self-scan (r6 result) ===')
for n, p in patterns:
    c = len(re.findall(p, raw))
    label = "FOUND" if c > 0 else "CLEAN"
    print(f'  {label} {c}: {n}')

prior = [
    'results/_v4_supp_l14v3_batch4_r5_executor.py',
    'results/_v4_supp_l14v3_batch4_r5_result.json',
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
    print(f'  PRESERVED {sha} {len(d)}B {f}')

new = [
    'results/_v4_supp_l14v3_batch4_r6_executor.py',
    'results/_v4_supp_l14v3_batch4_r6_result.json',
    'results/_v4_supp_l14v3_batch4_r6_verify.py',
]
print()
print('=== new r6 products ===')
for f in new:
    with open(f, 'rb') as fp:
        d = fp.read()
    sha = hashlib.sha256(d).hexdigest()[:12]
    print(f'  NEW {sha} {len(d)}B {f}')

print()
print('=== finish block (r6) ===')
r = json.loads(raw)
f = r['coze_teacher_side_finish']
print(f"all_22_captions_met_target: {f['all_22_captions_met_target']}")
print(f"met_target_count: {f['met_target_count']}/{f['total_captions']}")
print(f"met_target_percentage: {f['met_target_percentage']}%")
print(f"finish_status: {f['finish_status']}")
print(f"cumulative_calls_total: {f['cumulative_calls_total']}")
print(f"cumulative_ok: {f['cumulative_ok']}")
print(f"cumulative_empty: {f['cumulative_empty']}")
print(f"cumulative_empty_rate: {f['cumulative_empty_rate']}")
print(f"rounds_used: {f['rounds_used']}")
print(f"finish_verdict_trigger_for_verdict_keeper: {f['finish_verdict_trigger_for_verdict_keeper']}")

print()
print('=== r6 disposition ===')
disp = r['r6_disposition']
print(f"r6_call_target: {disp['r6_call_target']}")
print(f"r6_call_result: {disp['r6_call_result']}")
print(f"r6_call_structural_failure_confirmed: {disp['r6_call_structural_failure_confirmed']}")
print(f"r6_hard_stop_engaged: {disp['r6_hard_stop_engaged']}")
print(f"r6_hard_stop_reason: {disp['r6_hard_stop_reason']}")
print(f"r6_disposition: {disp['r6_disposition']}")

print()
print('=== S6_n60 per_caption after r6 ===')
s6 = r['per_caption_successful_calls']['S6_n60']
print(f"succ_count: {s6['succ_count']}/5")
print(f"need_more_to_target: {s6['need_more_to_target']}")
print(f"met_target: {s6['met_target']}")
print(f"total_calls_so_far: {s6['total_calls_so_far']}")
print(f"empty_count_so_far: {s6['empty_count_so_far']}")
print(f"round6_updated: {s6['round6_updated']}")

print()
print('=== S6_n60 quadruple (r6 call) ===')
for q in r['quadruples']:
    cm = q['per_call_metadata']
    print(f"prompt_id: {q['prompt_id']}")
    print(f"response_text preview: {(q['response_text'] or '')[:80]!r}")
    print(f"ok: {cm['ok']}, empty_response: {cm['empty_response']}")
    print(f"latency_ms: {cm['latency_ms']}")
    print(f"model_returned: {cm['model_returned']}")
    print(f"usage: prompt={cm['usage'].get('prompt_tokens')} completion={cm['usage'].get('completion_tokens')} reasoning={cm['usage'].get('completion_tokens_details',{}).get('reasoning_tokens',0)}")
    print(f"retry_count: {cm['retry_count']}")
    print(f"reask_idx: {cm['reask_idx']}")
    print(f"round_index: {cm['round_index']}")
    print(f"phase_label: {cm['phase_label']}")
    print(f"temperature: {cm['temperature']}, max_tokens: {cm['max_tokens']}")