import json
r = json.load(open('results/_v4_supp_t15_result.json', encoding='utf-8'))

print('=== records_summary ===')
for k,v in r['records_summary'].items():
    print(f'  {k}: {v}')
print()

print('=== per_cell_summary ===')
for ci in sorted(r['per_cell_summary'].keys(), key=lambda x: int(x)):
    cs = r['per_cell_summary'][ci]
    j_all = cs['cell_j_median_5teachers']
    j_ne = cs['cell_j_median_5teachers_nonempty']
    n_rec = cs['n_records']
    n_ee = cs['n_pairs_total_empty_empty']
    k3 = cs['kill_lines']['K-N11-3']['any_hit']
    k1 = cs['kill_lines']['K-N11-N1_T1relax']['any_fail']
    print(f'  cell{ci} {cs["dim"]}/t={cs["temperature"]}/qwen_plan: '
          f'J_all={j_all}, J_ne={j_ne}, '
          f'n_records={n_rec}, n_pairs_empty_empty={n_ee}, '
          f'K-N11-3 hit={k3}, K-N11-N1 fail={k1}')
print()

print('=== per_teacher (cell 0) ===')
cs0 = r['per_cell_summary']['0']
for tp in cs0['per_teacher']:
    print(f'  {tp["teacher"]}: j_median={tp["j_median"]}, j_median_nonempty={tp["j_median_nonempty"]}, '
          f'n_pairs={tp["n_pairs"]}, n_pairs_empty_empty={tp["n_pairs_empty_empty"]}, n_records={tp["n_records"]}')
print()

print('=== per_teacher (cell 5) ===')
cs5 = r['per_cell_summary']['5']
for tp in cs5['per_teacher']:
    print(f'  {tp["teacher"]}: j_median={tp["j_median"]}, j_median_nonempty={tp["j_median_nonempty"]}, '
          f'n_pairs={tp["n_pairs"]}, n_pairs_empty_empty={tp["n_pairs_empty_empty"]}, n_records={tp["n_records"]}')
print()

print('=== K-T1-S1 per_dim ===')
s1 = r['kill_lines_T15']['K-T1-S1_temperature_flip_T15reuse']
for dim, d in s1['per_dim'].items():
    print(f'  {dim}: temps={d["temps_cell_j_median"]}, hit={d["hit"]}, verdict={d["verdict"]}')
print(f'  any_hit: {s1["any_hit"]}')
print()

print('=== K-T1-S3 ===')
s3 = r['kill_lines_T15']['K-T1-S3_robustness_confirm_T15reuse']
print(f'  all_cells_below_threshold: {s3["all_cells_below_threshold"]}')
print(f'  any_cell_flip_to_ge_threshold: {s3["any_cell_flip_to_ge_threshold"]}')
print(f'  hit: {s3["hit"]}')
print(f'  verdict: {s3["verdict"]}')
print()

print('=== K-T1-S2 (referenced from T1 verdict, not retested) ===')
s2 = r['kill_lines_T15']['K-T1-S2_endpoint_flip_T15_reference']
print(f'  any_hit: {s2["any_hit"]}')
print(f'  verdict: {s2["verdict"]}')
print(f'  literal_source: {s2["literal_source"][:100]}')
print()

print('=== overall_verdict ===')
ov = r['overall_verdict']
for k,v in ov.items():
    if isinstance(v,str):
        print(f'  {k}: {v[:300]}')
    else:
        print(f'  {k}: {v}')
print()

print('=== cross_temp_std_per_dim ===')
print(f'  all_pairs: {r["cross_temp_std_per_dim"]["all_pairs"]}')
print(f'  nonempty: {r["cross_temp_std_per_dim"]["nonempty_pairs"]}')