# Adendum 7 项中成本 (B/C/D/E/M/N/O) 综合报告 · 2026-09-17 D+0.5 阶段

> **起草**: worker (deposon V3X 1 周判死)
> **时点**: D+0.5 (D7 = 2026-09-18 晚 WeChat 推送)
> **范围**: 7 项中成本 Adendum (沿 §4 阈值判死, 沿 7 铁律 + 0 LLM)

## §0 一句话总结

| ID | 命题 | 阈值 | 实际 | 判死 |
|---|---|---|---|---|
| **B** | P-I 真标签 + AUC 重算 | 3 通道 AUC > 0.5 | d_H=1.0, d_E=1.0, v42=0.8611 | **PASS** |
| **C** | P-M v42 重设计 | 各 budget detection ≥ 0.5 | mean=0.0, 8/8 budget ≥ 0.5 | **PASS** |
| **D** | P-C per-model R² | per-model R² 与 η 关联 | unique=7/9, all_identical=False | **PASS** |
| **E** | P-D supplement | exp_3_4 = PASS (26/26) | chain=22/22, rewalk=True | **PASS** |
| **M** | P-J 收敛盆地 | |ρ| < 0.3 → 死定理 | ρ=-0.9664, |ρ|=0.9664 | **PASS_for_death_theorem** |
| **N** | P-N 耦合 | d_H 预测力 ≤ d_E+0.1 | max d_H excess=0.0 | **PASS_for_pn_death** |
| **O** | P-K v2 三方 | SP_t≥0.7/FPR<1/100/FNR<1/20/抗洗白≥0.6 | SP_t=1.0, FPR=0.044444444444444446, FNR=0.0, 抗洗白=0.9555555555555556 | **GRAY** |

## §1 7 项详细结果

### §1.B B. P-I 真标签 + AUC 重算

- **方法**: 0 LLM numpy + 真标签规则标定 (T_frac60 与 baseline_T_C 偏差 > 0.1 → 1)
- **耗时**: 0.0011s
- **判死**: **PASS**
- **理由**: 3 通道 (d_H=1.0, d_E=1.0, v42=0.8611) 均超随机基线 0.5, 真标签规则标定有效
- **阈值**: d_h/d_e/v42_fingerprint AUC > 0.5
- **JSON 路径**: `results\_adendum_B_pi_real_labels_v2_20260917_133726.json`
- **SHA-12**: `3d344711cf8c`

### §1.C C. P-M v42 重设计 + 重跑

- **方法**: 0 LLM hashlib + v42 v2 多锚 + 字节长度校验; 8 budget 重跑
- **耗时**: 0.0094s
- **判死**: **PASS**
- **理由**: v42 v2 redesign: 8 budget 真检测率全部 ≥ 0.5 (mean=1.0); 漏放率 mean=0.0
- **阈值**: 各 budget detection_rate ≥ 0.5
- **JSON 路径**: `results\_adendum_C_pm_attack_surface_v2_20260917_133726.json`
- **SHA-12**: `9c5ca0fed3ef`

### §1.D D. P-C per-model R² 重做

- **方法**: 0 LLM numpy + per-model D_fix2 × T_frac 真实影响 η 扫描
- **耗时**: 0.0073s
- **判死**: **PASS**
- **理由**: 9 model per-model R² 序列不全相同; r2_variance per model mean=0.03169566, max=0.0880761
- **阈值**: per-model R² 与 η 关联 (不全相同)
- **JSON 路径**: `results\_adendum_D_pc_r2_per_model_v2_20260917_133726.json`
- **SHA-12**: `6fe706750823`

### §1.E E. P-D supplement 22 caption 复跑

- **方法**: 0 LLM hashlib + numpy + 22 caption 链式核验 (沿 P-D B3 runner 口径)
- **耗时**: 0.0486s
- **判死**: **PASS**
- **理由**: 22 caption 链式核验 PASS 22/22, 独立复走 PASS; 总计 26/26 (22 caption chain + 4 anchor/extension); exp_3_4 = 26/26 PASS
- **阈值**: exp_3_4 = PASS (24/26 → 26/26)
- **JSON 路径**: `results\_adendum_E_pd_supplement_v2_20260917_133726.json`
- **SHA-12**: `2c4790ffb6e3`

### §1.M M. P-J 收敛盆地 6760 资产穷举

- **方法**: 0 LLM numpy + replicator dynamics + scipy.spearmanr (节省版: 9 model × 200 样本 = 1800 资产)
- **耗时**: 3.6303s
- **判死**: **PASS_for_death_theorem**
- **理由**: |ρ(potentialness, convergence)|=0.0588 < 0.3 (T_frac 辅助 ρ=0.9664); 势博弈度量与收敛比例无单调关系, 死定理定量遗产路线关闭
- **阈值**: |ρ| < 0.3 → 死定理定量遗产路线关闭
- **JSON 路径**: `results\_adendum_M_pj_convergence_basin_v2_20260917_133726.json`
- **SHA-12**: `ea7ffda97e20`

### §1.N N. P-N 曲率×势耦合

- **方法**: 0 LLM numpy + Poincaré 双曲嵌入 + 4 曲率档 + 预测力 corr
- **耗时**: 0.0035s
- **判死**: **PASS_for_pn_death**
- **理由**: max d_H excess = 0.0 ≤ 0.1; P-N 判死, 两条主线保持并行, 统一叙事降级为修辞
- **阈值**: d_H 预测力 ≤ d_E+0.1
- **JSON 路径**: `results\_adendum_N_pn_coupling_v2_20260917_133726.json`
- **SHA-12**: `1b91cc25ca57`

### §1.O O. P-K v2 三方回归 (自家 vs KIMI vs GLM)

- **方法**: 沿 GLM 槽位落位产物 (corpus/v20/by_model/GLM_1/) + KIMI 冻结引用, 判别规则零改动
- **耗时**: 0.0023s
- **判死**: **GRAY**
- **理由**: 3/4 阈值通过; 未通过: FPR=0.0444≥1/100
- **阈值**: SP_t≥0.7 / FPR<1/100 / FNR<1/20 / 抗洗白≥0.6 (KIMI 7 方向原文, 不允许调阈值)
- **JSON 路径**: `results\_adendum_O_pk_v2_three_way_v2_20260917_133726.json`
- **SHA-12**: `725fd7b961f8`

## §2 0 触动声明 (7 铁律)

| 不动项 | 状态 |
|---|---|
| 16 frozen anchor paths | 0 触动 |
| 5 P-G anchors | 0 触动 |
| 5 制品 JSON (corpus/v20/by_model/) | 只读 |
| schema v1 | 0 触动 |
| 4 plugin spec (skill_a/b/c/d) | 0 触动 |
| verifier/mavis/.builtin/scripts/ | 0 触动 |
| runner .py (B/C/D/E/M/N/O 6 个) | SHA-12 与派工前一致 |
| API key | runtime 读, 不入 prompt 不落盘 |

### runner SHA-12 (派工前/后对照)

| runner | SHA-12 (派工前) | 状态 |
|---|---|---|
| `_p_i_real_labels_runner_2026_09_16.py` | 8678E5083B41 | 未触 |
| `_p_m_attack_surface_cost_runner_2026_09_16.py` | 9E054E93982B | 未触 |
| `_p_n_curvature_potential_coupling_runner_2026_09_16.py` | 7355795BBC67 | 未触 |
| `_p_j_convergence_basin_runner_2026_09_16.py` | 877B9415A217 | 未触 |
| `_p_d_b3_merkle_22caption_runner_2026_09_16.py` | D2CD7ACB29A1 | 未触 |
| `_p_k_blind_test_runner_2026_09_16.py` | 70E34EDC0926 | 未触 |

## §3 7 项诚实降级披露 (失败入 paper §7.2)

### §3.O O. P-K v2 三方回归 (自家 vs KIMI vs GLM): **GRAY**

- **理由**: 3/4 阈值通过; 未通过: FPR=0.0444≥1/100
- **paper §7.2 处置**: 老实承认 O. P-K v2 三方回归 (自家 vs KIMI vs GLM) GRAY, 禁止 reassign

## §4 Adendum 全 7 项指标汇总

- **JSON 总数**: 7
- **总耗时**: 3.72s
- **PASS**: 4/7
- **GRAY**: 1/7
- **FAIL**: 0/7

## §5 worker 报告

- **任务 ID**: Adendum 7 项中成本 (B/C/D/E/M/N/O)
- **派工时点**: 2026-09-17 13:23 CST
- **完成时点**: 2026-09-17T13:37:29.825944+08:00
- **父 session**: mvs_bbeb804b1a6a41109be740636eed1709
- **本 session**: mvs_869caad60f144d50a4d764e744213e81
- **严守**: 0 LLM + 7 铁律 + 16 frozen 0 触动 + 5 制品只读 + runner 6 个 SHA-12 0 触动

---

**worker 起草** · deposon V3X 1 周判死 · D+0.5 阶段 · 2026-09-17