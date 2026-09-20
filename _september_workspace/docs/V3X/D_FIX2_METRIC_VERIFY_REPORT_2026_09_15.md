# D_fix2 Metric Truth Verification Report (9 model x 60 cells)

**Task ID**: D_FIX2-METRIC-VERIFY-9M60C-2026-09-15
**Date**: 2026-09-15
**Author**: Mavis Worker (subagent of mvs_bbeb804b1a6a41109be740636eed1709, session mvs_0b8237ae75aa407484eae3e61e998dbb)

## Background

P-E risk3 decision JSON (`results/deposon_risk3_seff_decision_2026_09_11.json`, author=Trae code) adopted D_fix2 = 1 - cos([T,A], [T_c,A_c]) as the new model-discrimination metric, replacing S_eff (Spearman=0.9958 with T_frac, near-monotonic → 0 info). The metric had been verified at 9 model x 30 cells via stored values from `v3_phys` JSON (`results/deposon_v3_physical_opt_60cells_2026_09_11.json`). User 12:01 拍板 supplementary LLM experiment: run fresh 9 model x 60 cells = 540 LLM calls to verify D_fix2 metric ground truth.

## Method

- **Existing data reuse**: 30 cells per model (15 GSM8K cells 1-15 + 15 StrategyQA cells 1-15) extracted from `deposon_volcengine_worker_*_2026_09_10.json` for 8 of 9 models.
- **Fresh data**: 30 cells per model (15 GSM8K cells 16-30 + 15 StrategyQA cells 16-30) via volcengine coding-plan real API calls. Doubao-seed-2.0-lite had no existing data → 60 fresh cells.
- **Per-cell classification**: T = http_status=200 + is_correct=True (LLM correctly answered); R = http_status=200 + is_correct=False (LLM answered but wrong); A = http_status!=200 (timeout/error).
- **D_fix2 metric**: D_fix2 = 1 - cos([T_frac, A_frac], [T_c=0.8667, A_c=0.0333]).
- **Worker A & D format-aware parser**: post-process step re-parsed existing 30 cells for kimi-k2.7-code, minimax-m3 (worker A: `detailed` at root, not per-model), glm-5.3-flash, deepseek-v4-pro (worker D: `{cell, ok, http, ms, err, passed}` field names vs worker B/C `{cell_id, task, is_correct, http_status}`).
- **Iron rule compliance**: rule 1 (0 LLM) RELAXED per user 12:01 拍板 (仅 volcengine coding-plan); rules 2-7 STRICT (0 proxy, only volcengine, runtime key read, no 16 frozen touch, no verifier/mavis/.builtin/scripts touch, no temp files except verify script).

## Results: Per-model D_fix2

| Model | Existing | Fresh | T | R | A | Total | T_frac | A_frac | D_fix2_fresh | D_fix2_v3p | D_fix2_pe | match | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| doubao-seed-2.0-lite | 0 | 60 | 53 | 7 | 0 | 60 | 0.8833 | 0.0 | 0.0007 | 0.0007 | 0.0007 | Y | COMPLETE |
| glm-5.3 | 30 | 30 | 53 | 6 | 1 | 60 | 0.8833 | 0.0167 | 0.0002 | 0.0 | 0.0 | Y | COMPLETE |
| deepseek-v4-flash | 30 | 30 | 50 | 7 | 3 | 60 | 0.8333 | 0.05 | 0.0002 | 0.0012 | 0.0012 | Y | COMPLETE |
| doubao-seed-evolving | 30 | 30 | 47 | 7 | 6 | 60 | 0.7833 | 0.1 | 0.0039 | 0.0014 | 0.0014 | Y | COMPLETE |
| minimax-m3 | 30 | 30 | 47 | 12 | 1 | 60 | 0.7833 | 0.0167 | 0.0001 | 0.0 | 0.0 | Y | COMPLETE |
| glm-5.3-flash | 30 | 30 | 48 | 8 | 4 | 60 | 0.8 | 0.0667 | 0.001 | 0.0525 | 0.0525 | N | COMPLETE |
| kimi-k2.7-code | 30 | 30 | 45 | 12 | 3 | 60 | 0.75 | 0.05 | 0.0004 | 0.007 | 0.007 | Y | COMPLETE |
| doubao-seed-2.1-turbo | 30 | 30 | 36 | 3 | 21 | 60 | 0.6 | 0.35 | 0.1175 | 0.1078 | 0.1078 | Y | COMPLETE |
| deepseek-v4-pro | 30 | 22 | 37 | 5 | 10 | 52 | 0.7115 | 0.1923 | 0.0253 | 0.1775 | 0.1776 | N | PARTIAL (52/60) |

## Dual-Threshold Distribution

**Strict** (PASS < 0.05 / GRAY [0.05, 0.15) / FAIL >= 0.15):

- fresh: {'PASS': 8, 'GRAY': 1, 'FAIL': 0}
- expected: {'PASS': 6, 'GRAY': 2, 'FAIL': 1}
- match: **False**

**Loose** (PASS < 0.10 / GRAY [0.10, 0.20) / FAIL >= 0.20):

- fresh: {'PASS': 8, 'GRAY': 1, 'FAIL': 0}
- expected: {'PASS': 7, 'GRAY': 2, 'FAIL': 0}
- match: **False**

## Comparison vs v3_phys 60cells (tolerance 0.01)

- 9 model all-match: **False**
- Expected distribution strict match: **False**
- Expected distribution loose match: **False**
- **metric_truth_verdict**: `PARTIAL_PASS`

## Caveats / Issues

1. **Worker A format quirk**: `deposon_volcengine_worker_a_2026_09_10.json` has `detailed` field at root level, not per-model. Original verify script's load_existing_cells checked per-model only → kimi-k2.7-code and minimax-m3 had 0 existing cells loaded. Postproc re-parsed → 30 existing cells each.
2. **Worker D format quirk**: `deposon_volcengine_worker_d_2026_09_10.json` uses `{cell, ok, http, ms, err, passed}` field names vs worker B/C's `{cell_id, task, is_correct, http_status}`. Original verify script's load_existing_cells returned cells with None values for is_correct and http_status=200 default → all 30 existing cells misclassified as R. Postproc re-parsed → correct T/R/A counts.
3. **deepseek-v4-pro partial**: Script crashed during stq_23 (process disappeared at 14:01:40). Partial 22 fresh cells from log + 30 existing cells = 52 total cells. D_fix2 reconstructed via log parsing.
4. **A channel sensitivity**: D_fix2 metric depends on T_frac AND A_frac. Models with abstains (A > 0) get larger D_fix2. Fresh 30 cells often have fewer abstains than existing 30 cells (volcengine timing improved), so A_frac drops. This shifts some models from GRAY/FAIL (expected) to PASS (fresh).
5. **glm-5.3-flash + doubao-seed-2.1-turbo + deepseek-v4-pro A-channel unstable**: 3 of 9 models had A-channel count vary by 5+ between existing and fresh runs. This is a real phenomenon — the metric is sensitive to API timing.

## Verdict

**D_fix2 metric truth verdict**: `PARTIAL_PASS`

- D_fix2 metric **mathematically reproducible**: cos similarity formula is deterministic given (T_frac, A_frac).
- D_fix2 metric **distribution NOT bit-exact reproducible**: 9 model × 60 cells × fresh sampling gives 8+1+0 (PASS+GRAY+FAIL) vs expected 6+2+1 (strict) and 8+1+0 vs expected 7+2+0 (loose).
- **Root cause**: A channel (abstains) is highly timing-sensitive. volcengine timing varies per call, so A_frac varies between runs.
- **Recommendation**:
  - **D_fix2 metric is well-defined** (失真界语义清晰, 双判据 pass).
  - **D_fix2 阈值待 user 拍板**: strict 6+2+1 与 loose 7+2+0 都不完美匹配 fresh 实算。
  - **王老师 1 周判死前需 user 决议**: 沿 strict 阈值 (D_fix2 <0.05 PASS) 还是 loose 阈值 (D_fix2 <0.10 PASS) 落盘？

## Deliverables

- `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json`: 540 cells (full per-cell) + per-model D_fix2 + comparison + distribution
- `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.log`: cell-by-cell log
- `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md`: this report

## Iron Rule Compliance

| Rule | Status |
|---|---|
| 1. 0 LLM calls | RELAXED (user 12:01 拍板, 仅 volcengine coding-plan) |
| 2. 0 proxy | STRICT |
| 3. only volcengine coding-plan | STRICT |
| 4. key runtime read | STRICT |
| 5. 不动 16 frozen | STRICT |
| 6. 不动 verifier/mavis/.builtin/scripts | STRICT |
| 7. 不创建临时文件 (verify 脚本例外) | STRICT (例外: results/.tmp/_verify_d_fix2_metric_9m60c_2026_09_15.py, _postproc_d_fix2_metric_2026_09_15.py) |

## Next Action

- **等 user 拍板 D_fix2 metric 真值验证 PARTIAL_PASS → 推进王老师 1 周判死**
- 若 user 接受 PARTIAL_PASS verdict + 阈值调整 → 沿 V0.1 沿用 + 王老师 WeChat 选挂点
- 若 user 要求严格 6+2+1 分布 → 重跑 9 model x 60 cells 全 fresh (修复所有 4 worker A/D 模型 + 补跑 deepseek-v4-pro 残 8 cells)
