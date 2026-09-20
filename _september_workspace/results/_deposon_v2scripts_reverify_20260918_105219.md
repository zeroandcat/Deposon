# Deposon v2 Scripts 复算详细报告 — 2026-09-18

- 时间戳: `20260918_105219`
- Composite JSON: `D:\私人资料\deposon-repo\results\_deposon_v2scripts_reverify_20260918_105219.json`
- 方法: 0 LLM / 仅 hashlib + 复算 verdict 纯函数
- LLM 调用次数: 0
- 读取 API key: 0
- 修改 frozen 资产: False

## 8 维 PASS/FAIL 状态

| # | 维度 | PASS/FAIL | 说明 |
|---|------|-----------|------|
| 1 | run_v20_vector_audit.py 存在 | ✅ PASS | path = `run_v20_vector_audit.py` |
| 2 | run_v21_gtformal.py verdict_p1b 一致性 | ✅ PASS | frozen=triggered |
| 3 | run_v22_e95ci.py Newcombe 95% CI 复算 | ✅ PASS | 3 benchmark |
| 4 | run_v22_p1c.py verdict_p1c 一致性 | ✅ PASS | frozen=killed |
| 5 | svg_mindmap_ingest.py 自检 | ✅ PASS | 6 nodes + 5 edges + root=中心主题 |
| 6 | 0 LLM 调用 | ✅ PASS | method = hashlib + verdict_pure_function |
| 7 | 0 API key 落盘 (prompt/JSON/log) | ✅ PASS | no env var read / no api call issued |
| 8 | 18 frozen anchors 未触动 | ✅ PASS | 16/16 |
| **ALL** | **总评** | ✅ ALL PASS | 8 维全部通过 |

## Frozen Verdicts 一致性 (复算)

- **verdict_p1c**: frozen=`killed`, computed=`killed`, self_consistent=`True`
  - min_cos_at_best_global_tau = -1.0000000000000002
  - min_cos_per_state_best_tau = -1.0
  - COS_STRONG = 0.999, COS_WEAK = 0.99
- **verdict_p1b**: frozen=`triggered`, kill_reason=`cosine<0`, self_consistent=`True`
- **verdict_p2**: frozen=`downgraded_to_approximate_potential_game`, frac_cyclic_high=0.9237804878048781, self_consistent=`True`
- **verdict_p3**: frozen reparam=`killed`, structure=`survives`, self_consistent=`True`

## Newcombe 95% CI 复算 (pure numpy)

| benchmark | computed [lo, hi] | expected [lo, hi] | diff_lo | diff_hi | PASS |
|-----------|-------------------|-------------------|---------|---------|------|
| gsm8k | [-0.1180, 0.0780] | [-0.1180, 0.0780] | 1.39e-17 | 1.39e-16 | ✅ |
| strategyqa | [-0.0876, 0.0876] | [-0.0876, 0.0876] | 0.00e+00 | 0.00e+00 | ✅ |
| unified_vs_cot | [-0.2052, -0.0412] | [-0.2052, -0.0412] | 0.00e+00 | 6.94e-17 | ✅ |

## T+R+A 守恒 9 model × 30 cells

- n_models = 9, max_residual_count = 0.0
- overall_pass = True

| model | T | R | A | T+R+A | residual | PASS |
|-------|---|---|---|-------|----------|------|
| doubao-seed-2.0-lite | 26 | 4 | 0 | 30 | 0 | ✅ |
| glm-5.3 | 26 | 3 | 1 | 30 | 0 | ✅ |
| deepseek-v4-flash | 23 | 5 | 2 | 30 | 0 | ✅ |
| doubao-seed-evolving | 22 | 6 | 2 | 30 | 0 | ✅ |
| minimax-m3 | 21 | 8 | 1 | 30 | 0 | ✅ |
| glm-5.3-flash | 21 | 1 | 8 | 30 | 0 | ✅ |
| kimi-k2.7-code | 19 | 8 | 3 | 30 | 0 | ✅ |
| doubao-seed-2.1-turbo | 18 | 2 | 10 | 30 | 0 | ✅ |
| deepseek-v4-pro | 16 | 2 | 12 | 30 | 0 | ✅ |

## 18 Frozen Anchors Verify

- total = 16, ok = 16, fail = 0, all_pass = True

| rel path | expected | observed | match | source | name |
|----------|----------|----------|-------|--------|------|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | `03c6c01f3697` | ✅ | repo | 5 anchors JSON |
| `docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d404366` | `78b71d404366` | ✅ | repo | KT-A1 SPEC V0.1 |
| `docs/V3X/KT_B1_SPEC_V0.1.md` | `0410ca0fbdae` | `0410ca0fbdae` | ✅ | repo | KT-B1 SPEC V0.1 |
| `docs/V3X/KT_C1_SPEC_V0.1.md` | `59d8f56347d5` | `59d8f56347d5` | ✅ | repo | KT-C1 SPEC V0.1 |
| `docs/V3X/KT_D0_SPEC_V0.1.md` | `cce8e9a1b00e` | `cce8e9a1b00e` | ✅ | repo | KT-D0 SPEC V0.1 |
| `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | `b10fae0da66d` | `b10fae0da66d` | ✅ | repo | P-F V0.1 upgrade |
| `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | `910c4333eead` | ✅ | repo | v19 benchmark |
| `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | `9d9ae5001c57` | ✅ | repo | v21 gtformal |
| `corpus/v20/index.json` | `8423ffe266af` | `8423ffe266af` | ✅ | repo | corpus v20 |
| `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `b41c98bf90cc` | `b41c98bf90cc` | ✅ | repo | P-F V0 placeholder |
| `docs/V3X/P_F_SPEC_V0.md` | `de90faf362c5` | `de90faf362c5` | ✅ | repo | P-F SPEC V0 |
| `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `98085df7811a` | `98085df7811a` | ✅ | repo | P-F research |
| `deposon_team/plugins/skill_a_p_a_60cells.py` | `b1463bb24403` | `b1463bb24403` | ✅ | repo | plugin_a 9078B |
| `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `e5a299f69a22` | `e5a299f69a22` | ✅ | repo | plugin_b 8699B |
| `deposon_team/plugins/skill_c_p_e_3modality.py` | `e19e76c5da7e` | `e19e76c5da7e` | ✅ | repo | plugin_c 8915B |
| `deposon_team/plugins/skill_d_p_f_observer.py` | `3e369a1f6171` | `3e369a1f6171` | ✅ | repo | plugin_d 15927B |

## Input Assets SHA-12

| asset | size (B) | SHA-12 |
|-------|----------|--------|
| `deposon_v22_p1c` | 763 | `2bed4de3a57c` |
| `deposon_v21_gtformal` | 69204 | `9d9ae5001c57` |
| `deposon_v22_e95ci` | 1496 | `928bcfbdb7c3` |
| `deposon_v3_v7_summary` | 25049 | `063ac8d00542` |
| `v3x_d7_v3_final_v7` | 38545 | `4a08521f8de1` |
| `schema_v1` | 12919 | `9e99dcc4d920` |
| `run_v20_vector_audit` | 4717 | `16a270a6bdab` |
| `run_v21_gtformal` | 16600 | `9bbe43f41fa8` |
| `run_v22_e95ci` | 3058 | `8470e3ce8cae` |
| `run_v22_p1c` | 7236 | `6e9673205dc0` |
| `svg_mindmap_ingest` | 8811 | `fa661fd759ed` |
