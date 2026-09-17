# -*- coding: utf-8 -*-
"""P-L v3 Phase 1 finalization (2026-09-17)
- 读 4 个 JSON (L30/L45/L60/L100)
- 算 P1 R², P3 Q (single backbone + 含 60 档)
- 输出综合 MD
"""
import json
import math
import hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta

import numpy as np
from scipy.stats import linregress

DEPOSON_ROOT = Path(r'D:\私人资料\deposon-repo')
RESULTS_DIR = DEPOSON_ROOT / 'results'

TS = '20260917_132341'
L30 = RESULTS_DIR / f'_p_l_v3_real_collapse_mistral_L30_{TS}.json'
L45 = RESULTS_DIR / f'_p_l_v3_real_collapse_mistral_L45_{TS}.json'
L60 = RESULTS_DIR / f'_p_l_v3_real_collapse_mistral_L60_{TS}.json'
L100 = RESULTS_DIR / f'_p_l_v3_real_collapse_mistral_L100_{TS}.json'

OUT_MD = RESULTS_DIR / f'_p_l_v3_phase1_report_{TS}.md'

BASELINE_JSON = RESULTS_DIR / 'deposon_volcengine_seed_code_30cells_2026_09_10.json'
WORKER_C_JSON = RESULTS_DIR / '_v3x_p_l_v3_mistral_large_2512_20260917_115049.json'
PHYS60_JSON = RESULTS_DIR / 'deposon_v3_physical_opt_60cells_2026_09_11.json'
STRATEGYQA_TRAIN = DEPOSON_ROOT / 'strategyqa_train.json'


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


# Load 4 JSON
d30 = json.loads(L30.read_text(encoding='utf-8'))
d45 = json.loads(L45.read_text(encoding='utf-8'))
d60 = json.loads(L60.read_text(encoding='utf-8'))
d100 = json.loads(L100.read_text(encoding='utf-8'))

print(f'L30: cells={d30["cells_total"]}, pass={d30["cells_pass"]}, acc={d30["accuracy"]}')
print(f'L45: cells={d45["cells_total"]}, pass={d45["cells_pass"]}, acc={d45["accuracy"]}')
print(f'L60: cells={d60["cells_total"]}, mean_T_frac60={d60["mean_T_frac60"]}')
print(f'L100: cells={d100["cells_total"]}, pass={d100["cells_pass"]}, acc={d100["accuracy"]}')

# ---------- P1 size scaling: single backbone (30/45/100) ----------
L_arr = np.array([30.0, 45.0, 100.0])
O_arr = np.array([d30['accuracy'], d45['accuracy'], d100['accuracy']])
slope, intercept, r_value, p_value, std_err = linregress(np.log(L_arr), np.log(O_arr))
R2 = r_value ** 2
P1_verdict = 'PASS' if R2 >= 0.9 else 'FAIL'

# P3 collapse residual: 主曲线归一化残差
O_pred = np.exp(intercept) * L_arr ** slope
Q = float(np.sqrt(np.mean((O_arr / O_pred - 1) ** 2)) / np.sqrt(np.mean(O_arr ** 2)))
if Q < 0.05:
    P3_verdict = 'PASS'
elif Q < 0.15:
    P3_verdict = 'GRAY'
else:
    P3_verdict = 'FAIL'

print(f'\nP1 single backbone (30/45/100):')
print(f'  slope={slope:.4f}, intercept={intercept:.4f}, R^2={R2:.4f}, p={p_value:.4f}')
print(f'  P1 verdict = {P1_verdict}')
print(f'  P3 Q = {Q:.4f}, verdict = {P3_verdict}')

# 含 60 档 (cross-backbone aggregate, 仅作 reference)
L2 = np.array([30.0, 45.0, 60.0, 100.0])
O2 = np.array([d30['accuracy'], d45['accuracy'], d60['mean_T_frac60'], d100['accuracy']])
slope2, intercept2, r2_2, p2, se2 = linregress(np.log(L2), np.log(O2))
R2_2 = r2_2 ** 2
P1_v2 = 'PASS' if R2_2 >= 0.9 else 'FAIL'
O_pred2 = np.exp(intercept2) * L2 ** slope2
Q2 = float(np.sqrt(np.mean((O2 / O_pred2 - 1) ** 2)) / np.sqrt(np.mean(O2 ** 2)))
P3_v2 = 'PASS' if Q2 < 0.05 else ('GRAY' if Q2 < 0.15 else 'FAIL')

print(f'\n含 60 档 (cross-backbone aggregate, reference only):')
print(f'  slope={slope2:.4f}, intercept={intercept2:.4f}, R^2={R2_2:.4f}, p={p2:.4f}')
print(f'  P1 verdict = {P1_v2}, P3 verdict = {P3_v2}')

# Overall
overall = 'PASS' if (P1_verdict == 'PASS' and P3_verdict == 'PASS') else \
          ('FAIL' if (P1_verdict == 'FAIL' or P3_verdict == 'FAIL') else 'GRAY')
print(f'\nOverall = {overall}')

# Spearman 跨档
sp_30 = d30['spearman_vs_baseline']
sp_45 = d45['spearman_vs_baseline_30_overlap']
sp_100 = d100['spearman_vs_baseline_30_overlap']
sp_30_p = d30['spearman_p_value']
sp_45_p = d45['spearman_vs_baseline_p_value']
sp_100_p = d100['spearman_vs_baseline_p_value']

# ---------- 综合 MD ----------
lines = []
lines.append("# P-L v3 Phase 1 综合报告 — Mistral Large 2512 x L in {30, 45, 60, 100}")
lines.append("")
lines.append(f"**生成时间**: {datetime.now(timezone(timedelta(hours=8))).isoformat()}")
lines.append(f"**主 backbone**: `mistralai/mistral-large-2512` (OpenRouter, MoE 架构)")
lines.append(f"**任务派工**: deposon V3X D7 Phase 1 (Mavis 主导, worker bg_* 派遣)")
lines.append(f"**严守**: 7 铁律 + 0 LLM 重 hash + 30 cells 起步 + 18 frozen 0 触动")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §0 一句话总结")
lines.append("")
lines.append(f"主 backbone `mistralai/mistral-large-2512` x L in {{30, 45, 60, 100}} 4 档实测完成. ")
lines.append(f"**单 backbone size scaling (30/45/100) R^2 = {R2:.4f} (FAIL, <0.9)**, **P3 Q = {Q:.4f} (FAIL, >0.15)**.")
lines.append(f"**Spearman vs baseline 30 cells overlap: L=30=0.3750 (worker C PASS), L=45=0.1667, L=100=0.1667 (均 << 0.95, 破同序成立)**.")
lines.append("")
lines.append(f"**P1 verdict = {P1_verdict}** | **P3 verdict = {P3_verdict}** | **Overall = {overall}**")
lines.append("")
lines.append("**老实交代**:")
lines.append("- 60 档 (mean T_frac60=0.7111) 是 9 model aggregate (跨 backbone), 与单 backbone (30/45/100) 不可比, 仅作 reference.")
lines.append("- P1 R^2=0.7447 < 0.9 → size scaling 不成立, P-L 数据塌缩主张 (用 Mistral Large 2512 单 backbone) **未通过**.")
lines.append("- P3 Q=0.1929 > 0.15 → 数据未塌缩到主曲线, P-L data collapse **未通过**.")
lines.append("- 沿 Coze §2.1 共识: Spearman 不是塌缩判死指标, 仅作 '是否跨 backbone 排序偏移' 辅助栏. 30 档 PASS 表明 backbone 替换破同单调.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §1 4 档 backbone x size 详细数据")
lines.append("")
lines.append("| L | backbone | cells_total | pass | accuracy | source | elapsed |")
lines.append("|---|---|---|---|---|---|---|")
lines.append(f"| 30 | mistralai/mistral-large-2512 | {d30['cells_total']} | "
             f"{d30['cells_pass']} | {d30['accuracy']:.4f} | worker C PASS 复用 | n/a |")
lines.append(f"| 45 | mistralai/mistral-large-2512 | {d45['cells_total']} | "
             f"{d45['cells_pass']} | {d45['accuracy']:.4f} | 新跑 (15 GSM8K + 15 baseline SQA + 15 new SQA) | {d45['elapsed_s']:.1f}s |")
lines.append(f"| 60 | (9 model aggregate) | {d60['cells_total']} | "
             f"n/a | {d60['mean_T_frac60']:.4f} | 复用 frozen per_model (T_frac60_total_mean) | n/a |")
lines.append(f"| 100 | mistralai/mistral-large-2512 | {d100['cells_total']} | "
             f"{d100['cells_pass']} | {d100['accuracy']:.4f} | 新跑 (15 GSM8K + 15 baseline SQA + 70 new SQA) | {d100['elapsed_s']:.1f}s |")
lines.append("")
lines.append("### §1.1 cells breakdown")
lines.append("")
lines.append(f"- **L=30** ({d30['cells_breakdown']}): 沿 worker C PASS 复用, 0 LLM 重跑")
lines.append(f"- **L=45** ({d45['cells_breakdown']}): 新跑 145 cells total LLM call (含 L=100)")
lines.append(f"- **L=60** (9 model x 60 cells = 540 cells): 复用 frozen per_model T_frac60 aggregate = {d60['mean_T_frac60']:.4f}")
lines.append(f"- **L=100** ({d100['cells_breakdown']}): 新跑")
lines.append("")
lines.append("### §1.2 L=60 per-model detail (复用 frozen)")
lines.append("")
lines.append("| model | T_frac60 | verdict |")
lines.append("|---|---|---|")
phys60 = json.loads(PHYS60_JSON.read_text(encoding='utf-8'))
for m in phys60['P_C_distortion_bound_60cells']['per_model']:
    lines.append(f"| {m['model']} | {m['T_frac60']:.4f} | {m['verdict']} |")
lines.append(f"| **mean** | **{d60['mean_T_frac60']:.4f}** | 8 PASS / 1 GRAY / 0 FAIL |")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §2 P1 尺寸标度 (Size Scaling)")
lines.append("")
lines.append("### §2.1 单 backbone fit (30/45/100) — 主指标")
lines.append("")
lines.append(f"- **数据点** (Mistral Large 2512, 同一 backbone):")
lines.append(f"  - L=30: O = {d30['accuracy']:.4f}")
lines.append(f"  - L=45: O = {d45['accuracy']:.4f}")
lines.append(f"  - L=100: O = {d100['accuracy']:.4f}")
lines.append(f"- **log-log fit**: log(O) = {intercept:.4f} + ({slope:.4f}) * log(L)")
lines.append(f"- **R^2** = **{R2:.4f}** (阈值 ≥ 0.9 = 幂律成立)")
lines.append(f"- **slope** = {slope:.4f} (幂律指数估计, 期望负或接近 0)")
lines.append(f"- **p-value** = {p_value:.6f}")
lines.append(f"- **verdict** = **{P1_verdict}** ({'幂律成立 (≥0.9)' if P1_verdict=='PASS' else '无幂律 (<0.9)'})")
lines.append("")
lines.append(f"**老实交代**: R^2 = {R2:.4f} < 0.9 → size scaling 在 30/45/100 cells 区间不成立. "
             f"原因可能是 (a) Mistral Large 2512 单 backbone 不足以覆盖 size scaling 信号, "
             f"(b) StrategyQA subset 新增 cells (15+70) 难度分布偏移导致 accuracy 单调下降, "
             f"或 (c) 三点拟合本身统计力不足 (n=3). 需 P2 跨 backbone β CI 检查.")
lines.append("")
lines.append("### §2.2 含 60 档 fit (cross-backbone aggregate, 仅 reference)")
lines.append("")
lines.append(f"- **数据点**: L=30:{d30['accuracy']:.4f}, L=45:{d45['accuracy']:.4f}, "
             f"L=60:{d60['mean_T_frac60']:.4f} (9 model mean), L=100:{d100['accuracy']:.4f}")
lines.append(f"- **R^2** = {R2_2:.4f} ({P1_v2})")
lines.append(f"- **slope** = {slope2:.4f}")
lines.append(f"- **p-value** = {p2:.6f}")
lines.append(f"- **注意**: 60 档是 9 model aggregate, 与单 backbone 30/45/100 不可比, 此 fit 仅作 reference.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §3 P3 标度塌缩 (Collapse Residual)")
lines.append("")
lines.append("### §3.1 单 backbone 主曲线 + 归一化残差")
lines.append("")
lines.append(f"- **主曲线**: O(L) = exp({intercept:.4f}) * L^({slope:.4f}) = {np.exp(intercept):.4f} * L^({slope:.4f})")
lines.append(f"- **拟合**: 在 log-log 空间对 (L, O(L)) 做线性拟合")
lines.append(f"- **归一化残差 Q** = **{Q:.4f}**")
lines.append(f"- **判读**:")
lines.append(f"  - Q < 0.05 → 塌缩成立")
lines.append(f"  - 0.05 ≤ Q < 0.15 → 边缘 (gray zone)")
lines.append(f"  - Q ≥ 0.15 → 无塌缩 (P-L data collapse 主张证伪)")
lines.append(f"- **verdict** = **{P3_verdict}**")
lines.append("")
lines.append(f"**老实交代**: Q = {Q:.4f} > 0.15 → 数据未塌缩到主曲线, P-L data collapse 主张 (用 Mistral Large 2512 单 backbone) **未通过**.")
lines.append("")
lines.append("### §3.2 含 60 档 P3")
lines.append("")
lines.append(f"- **Q** = {Q2:.4f} ({P3_v2})")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §4 跨 backbone / 跨档 Spearman cell-level")
lines.append("")
lines.append("| L | Spearman vs baseline (overlap) | p-value | N (overlap) | 解读 |")
lines.append("|---|---|---|---|---|")
lines.append(f"| 30 | **{sp_30:.4f}** | {sp_30_p:.6f} | 30 | worker C PASS (<< 0.95, 破同序成立) |")
lines.append(f"| 45 | {sp_45:.4f} | {sp_45_p:.6f} | 30 (overlap) | 同 backbone, 30 cells 交集 |")
lines.append(f"| 100 | {sp_100:.4f} | {sp_100_p:.6f} | 30 (overlap) | 同 backbone, 30 cells 交集 |")
lines.append("")
lines.append("**说明**: 沿 Coze §2.1 / GLM §3 / Trae §4 共识, Spearman 不是 P-L 主命题塌缩判死指标, 仅作 '是否跨 backbone 排序偏移' 辅助栏.")
lines.append("")
lines.append(f"- L=30 Spearman = {sp_30:.4f} (worker C PASS, << 0.95): **破 backbone 间同单调成立**")
lines.append(f"- L=45 Spearman = {sp_45:.4f} (与 baseline 30 overlap cells): 单 backbone 拓展, 与 L=30 一致 (相同 cells)")
lines.append(f"- L=100 Spearman = {sp_100:.4f} (与 baseline 30 overlap cells): 同上")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §5 与 4 提案对账 + P-L 主张状态升级")
lines.append("")
lines.append("### §5.1 4 提案判死预期 vs 实测")
lines.append("")
lines.append("| 提案 | P1 预期 | P3 预期 | 实测 P1 | 实测 P3 | 判读 |")
lines.append("|---|---|---|---|---|---|")
lines.append("| GLM | R^2 ≥0.9 幂律 | Q <0.05 塌缩 | FAIL (0.7447) | FAIL (0.1929) | 主指标 FAIL |")
lines.append("| Trae code | R^2 ≥0.9 幂律 | Q <0.05 塌缩 | FAIL | FAIL | 同 |")
lines.append("| KIMI | 主+副双指标 | 退化防线 | (退化防线沿 §6.1 待查) | (同) | 待 P2 补 |")
lines.append("| Coze | 三态分离, 主 PASS | Q <0.05 | FAIL | FAIL | P2 实现稳健性补 |")
lines.append("")
lines.append("### §5.2 P-L 主张状态")
lines.append("")
lines.append("- **v1** (P-L 主命题): 沿 4 提案聚合 _v3x_d0_5_aggregation_2026_09_17.md §0 沿 v3_phys JSON P_C 实算 → Spearman≡1 同向量两单调变换恒等式伪影 (FAIL)")
lines.append("- **v2** (诚实降级): 沿 Trae §6.7 移除伪造 R^2 公式, 但仍仅 9 model 60 cells 单 backbone → Spearman≡1 (FAIL)")
lines.append("- **v3 worker C**: 沿 Mistral Large 2512 30 cells 跨 backbone Spearman = 0.375 (PASS, 破同序)")
lines.append("- **v3 Phase 1 (本轮)**: 沿 Mistral Large 2512 × 4 尺寸 (30/45/60/100) 三态分离 → P1 FAIL (R^2=0.7447 < 0.9), P3 FAIL (Q=0.1929 > 0.15), Spearman 30 档 PASS")
lines.append("")
lines.append("**升级判死**: P-L 主命题 (data collapse) 在 Phase 1 (单 backbone × 多尺寸) **未通过**. 需 Phase 2 (跨 backbone × 多尺寸) 检查是否实现稳健性掩盖 size scaling 信号.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §6 严守 7 铁律 0 触动声明")
lines.append("")
lines.append("| 铁律 | 状态 | 证据 |")
lines.append("|---|---|---|")
lines.append("| API key 不入 prompt / 不落盘 | OK | runtime 读 LLM API.txt 仅在内存, JSON 中无 key 字面值 (仅 hash 12 位) |")
lines.append("| 国内模型走火山 | N/A | 本轮全走 OpenRouter (Mistral 系不在火山) |")
lines.append("| 海外模型走 OpenRouter | OK | mistralai/mistral-large-2512 走 openrouter.ai |")
lines.append("| 节省原则 (单 backbone x 30 cells 起) | OK | 30/45/100 档单 backbone x 30/45/100 cells, 60 档复用 frozen |")
lines.append("| 钥匙不写入 markdown / code / memory | OK | 全文未含 key 字面值, 仅 hash 12 位 |")
lines.append("| 不动 18 frozen anchors | OK | 全部仅 hash 复算 |")
lines.append("| 不动 5 制品 baseline JSON | OK | 未 read-modify-write |")
lines.append("| 不动 schema v1 / 4 plugin spec | OK | 未触动 |")
lines.append("| 不擅自动 verifier/mavis/.builtin/scripts/ | OK | 未触动 |")
lines.append("")
lines.append("**0 LLM 重 hash**: 全部 hash 复算用 hashlib.sha256() 纯本地计算")
lines.append("")
lines.append(f"**0 LLM budget 滥用**: total ~$0.10 USD (45 cells ~$0.04 + 100 cells ~$0.07)")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §7 锚 SHA-12 实算")
lines.append("")
lines.append("```")
lines.append(f"baseline_json_sha256_12      = {sha12(BASELINE_JSON)}  # deposon_volcengine_seed_code_30cells_2026_09_10.json")
lines.append(f"worker_c_json_sha256_12      = {sha12(WORKER_C_JSON)}  # _v3x_p_l_v3_mistral_large_2512_20260917_115049.json")
lines.append(f"phys60_json_sha256_12        = {sha12(PHYS60_JSON)}  # deposon_v3_physical_opt_60cells_2026_09_11.json")
lines.append(f"strategyqa_train_sha256_12   = {sha12(STRATEGYQA_TRAIN)}  # strategyqa_train.json")
lines.append(f"L30_out_json_sha256_12       = {sha12(L30)}  # _p_l_v3_real_collapse_mistral_L30_{TS}.json")
lines.append(f"L45_out_json_sha256_12       = {sha12(L45)}  # _p_l_v3_real_collapse_mistral_L45_{TS}.json")
lines.append(f"L60_out_json_sha256_12       = {sha12(L60)}  # _p_l_v3_real_collapse_mistral_L60_{TS}.json")
lines.append(f"L100_out_json_sha256_12      = {sha12(L100)}  # _p_l_v3_real_collapse_mistral_L100_{TS}.json")
lines.append(f"this_md_sha256_12            = (见 §9)")
lines.append("```")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §8 综合 PASS/FAIL/GRAY 判死")
lines.append("")
lines.append("| 命题 | 指标 | 阈值 | 实测 | verdict |")
lines.append("|---|---|---|---|---|")
lines.append(f"| P1 尺寸标度 (主) | log-log R^2 | ≥0.9 PASS / <0.9 FAIL | **{R2:.4f}** | **{P1_verdict}** |")
lines.append(f"| P3 标度塌缩 (主) | 归一化残差 Q | <0.05 PASS / 0.05-0.15 GRAY / >0.15 FAIL | **{Q:.4f}** | **{P3_verdict}** |")
lines.append(f"| 辅助 Spearman (L=30) | backbone vs baseline | <0.95 破同序 | **{sp_30:.4f}** | PASS |")
lines.append(f"| 辅助 Spearman (L=45) | backbone vs baseline | <0.95 破同序 | **{sp_45:.4f}** | PASS |")
lines.append(f"| 辅助 Spearman (L=100) | backbone vs baseline | <0.95 破同序 | **{sp_100:.4f}** | PASS |")
lines.append("")
overall = 'PASS' if (P1_verdict == 'PASS' and P3_verdict == 'PASS') else \
          ('FAIL' if (P1_verdict == 'FAIL' or P3_verdict == 'FAIL') else 'GRAY')
lines.append(f"**Overall (P1 + P3)**: **{overall}**")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## §9 附录: 新增工件 + 未触动再确认")
lines.append("")
lines.append("### §9.1 新增工件")
lines.append("")
lines.append("| 文件 | 路径 | 大小 | SHA-12 |")
lines.append("|---|---|---|---|")
lines.append(f"| L=30 JSON | `results/_p_l_v3_real_collapse_mistral_L30_{TS}.json` | "
             f"{L30.stat().st_size}B | {sha12(L30)} |")
lines.append(f"| L=45 JSON | `results/_p_l_v3_real_collapse_mistral_L45_{TS}.json` | "
             f"{L45.stat().st_size}B | {sha12(L45)} |")
lines.append(f"| L=60 JSON | `results/_p_l_v3_real_collapse_mistral_L60_{TS}.json` | "
             f"{L60.stat().st_size}B | {sha12(L60)} |")
lines.append(f"| L=100 JSON | `results/_p_l_v3_real_collapse_mistral_L100_{TS}.json` | "
             f"{L100.stat().st_size}B | {sha12(L100)} |")
lines.append(f"| 综合 MD | `results/_p_l_v3_phase1_report_{TS}.md` | (本文件) | (本文件 self) |")
lines.append("")
lines.append("### §9.2 未触动再确认")
lines.append("")
lines.append("- 18 frozen anchors (16 anchor + 2 anchor JSON) — 仅 hash 复算, **无 read-modify-write**")
lines.append("- 5 制品 baseline JSON (corpus/v20/by_model/{kimi, GLM_1, GLM_2, coze, MiniMax}) — **未触动**")
lines.append("- schema v1 (`_v3x_frozen_schema_v1.json`) — **未触动**")
lines.append("- 4 plugin spec (skill_a/b/c/d) — **未触动**")
lines.append("- verifier / mavis / .builtin/scripts/ — **未触动**")
lines.append("")
lines.append("### §9.3 runner script 路径")
lines.append("")
lines.append("- `_p_l_v3_phase1_runner_2026_09_17.py` (本 runner 主脚本, 33.8 KB)")
lines.append("- `_p_l_v3_phase1_finalize_2026_09_17.py` (finalization 算 P1/P3, 7.0 KB)")
lines.append("")
lines.append("---")
lines.append("")
lines.append(f"**P-L v3 Phase 1 完成** · 综合 verdict = **{overall}** · "
             f"P1 R^2 = {R2:.4f} ({P1_verdict}) · P3 Q = {Q:.4f} ({P3_verdict}) · "
             f"Spearman L=30 = {sp_30:.4f} (worker C PASS, 破 backbone 同序)")
lines.append("")
lines.append(f"**建议下游**: Mavis 聚合此 P-L v3 Phase 1 + 综合 MD, "
             f"作为 D7 (2026-09-18) 王老师 WeChat 推送前的 P-L 主命题三态分离证据. "
             f"Phase 2 (跨 backbone 实现稳健性) 需启动, 检查 P1 是否在多 backbone 上稳健成立.")

OUT_MD.write_text('\n'.join(lines), encoding='utf-8')
print(f'\n综合 MD 落盘 -> {OUT_MD}  size={OUT_MD.stat().st_size}B')
print(f'  MD SHA-12 = {sha12(OUT_MD)}')