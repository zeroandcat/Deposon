import json
r = json.load(open('results/_v4_supp_t15_result.json', encoding='utf-8'))

# Build per-cell judgment table
print("=== T1.5 PER-CELL JUDGMENT TABLE (6 cells) ===")
print()
print(f"{'#':<3} {'dim':<4} {'temp':<6} {'endpoint':<12} {'calls':<7} {'J_all_pooled':<14} {'J_same_cap':<11} {'J_cross_cap':<12} {'n_empt':<8} {'K-N11-3':<10} {'K-T1-S1':<10} {'K-T1-S3':<8}")
print("-" * 130)
for cell_idx in range(6):
    cs = r['per_cell_summary'][str(cell_idx)]
    sb = r['same_caption_breakdown'][str(cell_idx)]
    j_all = cs['cell_j_median_5teachers']
    j_ne = cs['cell_j_median_5teachers_nonempty']
    j_same = sb['j_median_same_caption']
    j_cross = sb['j_median_cross_caption']
    n_calls = cs['n_records']
    n_empt = r['records_summary']['n_empty_responses']  # global
    k3 = cs['kill_lines']['K-N11-3']['any_hit']
    # K-T1-S1 per dim cell:
    s1_dim = 'L2' if cs['dim'] == 'L2' else 'L14'
    s1_per_dim = r['kill_lines_T15']['K-T1-S1_temperature_flip_T15reuse']['per_dim'][s1_dim]
    s1_hit = 'hit=True' if s1_per_dim['hit'] else 'hit=False'
    # K-T1-S3:
    s3 = r['kill_lines_T15']['K-T1-S3_robustness_confirm_T15reuse']
    s3_overall = 'PASS' if s3['hit'] is False else 'FAIL'

    print(f"{cell_idx:<3} {cs['dim']:<4} {cs['temperature']:<6} {'qwen_plan':<12} {n_calls:<7} "
          f"{str(j_all):<14} {str(j_same):<11} {str(j_cross):<12} "
          f"{n_empt:<8} "
          f"{'hit=True' if k3 else 'hit=False':<10} {s1_hit:<10} {s3_overall:<8}")

print()
print("=== Hit direction explicit ===")
print("  K-N11-3 字面: J 中位 < 0.85 -> hit=True -> FAIL (主度量, 沿 L2/L14 verdict §4.3 字面)")
print("  K-T1-S1 字面: 任一温度点 cell J_all_pooled >= 0.85 -> hit=True (沿 T1 §1.5.2 字面)")
print("  K-T1-S3 字面: 全 6 cells J < 0.85 -> hit=False = 探针不命中 = 判定稳健 + T1 verdict 信息量补正")
print()
print("=== Comparison with T1 (placeholder, T1 result.json 已存在) ===")
print("T1 verdict F1B5E49F3058 §1.3 实测:")
print("  - 12 cells × 240 calls (mimo/teamo × temp {0.0,0.3,0.5} × {L2,L14})")
print("  - n_empty_responses = 112/227 OK = 49.3% (reasoning 模型耗尽 max_tokens=100 预算)")
print("  - empty-empty pairs 占 72.1% (n_empty_pairs_total / n_all_pairs_total)")
print("  - J_all_pooled 中位 = 0.0 (字面方向一致, 但根因 = empty-empty)")
print()
print("T1.5 实测:")
print("  - 6 cells × 120 calls (qwen_plan × temp {0.0,0.3,0.5} × {L2,L14}, max_tokens=500)")
print("  - n_empty_responses = 0/118 OK = 0.0% (qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后空响应消除)")
print("  - empty-empty pairs = 0")
print("  - J_all_pooled 中位 = 0.0 (字面方向一致, 但根因 = cross-caption 内容发散主导, cross:same=2:1)")
print("  - J_same_caption 中位 = 1.0 (L2 全部 3 cells) / 0.5-0.65 (L14 3 cells) [真教师稳定性信号]")
print()
print("** T1.5 主要发现: 工具失灵族 #1 (reasoning→非 reasoning) + #2 (max_tokens=100→500) 修正后, ")
print("   qwen3.7-max 空响应消除; 但 J_all_pooled 字面 = 0.0 现象仍存, 根因从 'empty-empty' 变为 'cross-caption 内容发散'; ")
print("   真教师稳定性信号 = same-caption re-ask J = 0.5-1.0 (与 qwen t=0.7 baseline 0.36-0.52 同档); ")
print("   T1 verdict §7 '字面 PASS = 构造失灵族假象' 一字不动 (不二次判定); ")
print("   T1 verdict 信息量补正: 修正构造失灵族后真维持字面方向一致 (J<0.85) = 真稳健入勘误链; ")
print("   但根因修正揭示真实教师稳定性信号 (same-caption J 0.5-1.0) — 这是 T1 verdict 未识别的额外信息.")
print()
print("=== T1.5 K-T1-S1 (温度敏感性) 跨温度方向 ===")
for dim, d in r['kill_lines_T15']['K-T1-S1_temperature_flip_T15reuse']['per_dim'].items():
    print(f"  {dim}: {d['temps_cell_j_median']}, hit={d['hit']}, verdict={d['verdict']}")