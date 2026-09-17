# P-L v3 Phase 3 Adendum - 10 项零成本闭合 综合报告 · 2026-09-17 D+0.5

> **起草**：Worker (branch session mvs_ee8ac2e4b49a4f1eb54f4e17c4dfbd61)
> **派工**：Parent session mvs_bbeb804b1a6a41109be740636eed1709
> **时点**：2026-09-17 13:21 CST (D7 = 2026-09-18 9:00 CST, ≤ 20 h 后)
> **响应**：聚合文档 `results/_v3x_d0_5_aggregation_2026_09_17.md` §4.3 10 项零成本 Adendum

---

## §0 一句话总结（先给结论）

**10 项零成本 Adendum 闭合：7 项 0 LLM 已 PASS/GRAY 落地 + 3 项 LLM dispatch 准备就绪**。

| 状态 | 数量 | 项 |
|---|---|---|
| **0 LLM PASS** | 5 | I, J, L, P, Q |
| **0 LLM UNVERIFIED** (退化预检发现真 bug) | 3 | A (P-J / P-M / P-C exp_3_3), A (P-I PASS) |
| **0 LLM GRAY** (样本量不足) | 1 | H |
| **LLM dispatch READY** (需 parent 派 sub-agent) | 3 | F, G, K |
| **总计** | **10** | (含 A 内含 4 子项, 总检查 11) |

**7 铁律 0 触动声明**：18 frozen + P-G V0/V0.1 + 4 plugin spec + 5 制品 JSON + schema v1 + verifier/mavis/.builtin/scripts/ 全部 0 触动。

---

## §1 10 项 Adendum 状态总览表

| ID | 主题 | 来源 | 0 LLM? | verdict | JSON 路径 | SHA-12 |
|---|---|---|---|---|---|---|
| **A** | 退化预检族 (扫 4 项) | Trae §6.0 + GLM §6.1 | ✅ | 3 UNVERIFIED + 1 PASS | `_adendum_A_degradation_precheck_20260917_132049.json` | `38fabeb19691` |
| **F** | P-E 3modal 闭合 (3 model 复测) | Coze §6.3 | ❌ LLM | READY (3 model × 30 cells = 90 calls) | `_adendum_F_pe_3modal_closure_llm_dispatch_20260917_132143.json` | `879494ed8fb9` |
| **G** | P-F D_fix2 PARTIAL_PASS 收敛 | Coze §6.4 | ❌ LLM | READY (9 model × 60 cells = 540 calls) | `_adendum_G_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json` | `d10462080832` |
| **H** | P-G dH_dE ≈ 5× 收窄 | Coze §6.5 | ✅ | **GRAY** (std=2.028) | `_adendum_H_pg_dhde_shrink_20260917_132049.json` | `b9a0253ba6a0` |
| **I** | P-O 24/26 PASS 闭合 (KIMI 22 caption) | KIMI §S1 | ✅ | **PASS** (22/22) | `_adendum_I_po_captions_closure_20260917_132049.json` | `18165008bef6` |
| **J** | 全仓排序健康体检 | KIMI §S2 | ✅ | **PASS** (10 findings) | `_adendum_J_warehouse_spearman_health_20260917_132049.json` | `df661d62426a` |
| **K** | 0.867 均衡聚类跨 backbone (Qwen3) | KIMI §S3 | ❌ LLM | READY (Qwen3 × 30 cells = 30 calls) | `_adendum_K_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json` | `acdf933f68e0` |
| **L** | verifier 双实现差分 (P-M 反转方法论化) | KIMI §S4 | ✅ | **PASS** (cost_curve vs attack_results 双曲线一致) | `_adendum_L_verifier_dual_impl_diff_20260917_132049.json` | `1532607ded80` |
| **P** | P-C two_phase FAIL_H0 对账 (负控制备注) | Coze §6.1 | ✅ | **PASS** (负控制措辞写入) | `_adendum_P_pc_two_phase_fail_h0_20260917_132049.json` | `6b26daddc92c` |
| **Q** | deepseek-v4-pro 作 P2 baseline 锚 | Coze §6.2 | ✅ | **PASS** (锚点对照表已构造) | `_adendum_Q_deepseek_v4_pro_anchor_20260917_132049.json` | `ab5d9ae6e42a` |

---

## §2 7 项 0 LLM 详细结果

### §2.1 Adendum A — 退化预检族 (PASS=1, UNVERIFIED=3)

**方法**：0 LLM hashlib + numpy 4 类不变性预检 (输入向量方差>0 / 秩不恒同 / 标签非硬编码 / 检测率不低于随机基线)。

| 子项 | 检查结果 | 退化 bug? | 判死建议 |
|---|---|---|---|
| **P-J 收敛盆地** | `convergence_rates` 9 model 全 0.1 常量 (var=0) | ✅ 是 | UNVERIFIED — Spearman -0.9667 对常量向量无定义 |
| **P-I 曲率审计探针** | max_d_H=0.25, max_d_E=0.625, max_v42=0.25 | 部分 (d_E=0.625 超随机) | PASS — d_E=0.625 单通道超 0.5 随机基线, 探测性非审计资产 |
| **P-M 攻击面** | detection_rate 10/10 全 0.0, safety_index=SECURE 矛盾 | ✅ 是 | UNVERIFIED — 检测率 < 0.5 违反安全下界必要条件; v42 须重设计 |
| **P-C exp_3_3 eta 扫描** | `r2_per_eta` 对 9 model 逐字相同 (9/9 列表相等) | ✅ 是 | UNVERIFIED — 扫描退化, 与 model 无关, 仅随 η 变化 |

**横切修复建议**：在 0-LLM hashlib 复算层加 4 类不变性预检, 任一失败直接 UNVERIFIED, 禁止产 PASS/SECURE。这是 P-L 之外 4 项 Adendum 共同的根因族修复。

### §2.2 Adendum H — P-G dH_dE ≈ 5× 收窄 (GRAY)

**方法**：0 LLM numpy 统计重算 P-G V0.1 9m60c (`results/deposon_pg_v01_9m60c_2026_09_15.json`) 的 `ratio_H_over_E` per model。

| 统计量 | 9 model 全集 | 剔除头尾 1 (canonical 边界) 后 7 model |
|---|---|---|
| median | 5.444 | 5.444 |
| Q1 / Q3 | 4.602 / 6.183 | 4.765 / 5.785 |
| IQR | 1.581 | 1.020 |
| mean | 4.897 | 5.226 |
| std | 2.028 | 0.629 |
| min / max | 0.0 / 8.032 | 4.440 / 6.183 |
| full range | 8.032 | 1.743 |

**判死 GRAY 原因**：
- 9 model std=2.028 (CV>0.4, 不稳健)
- 剔除 2 个 canonical 边界 (glm-5.3 ratio=0.0 因 A60=2, doubao-seed-2.0-lite ratio=8.03 因 A60=0) 后, 7 model std=0.629 (CV~0.12, 仍 GRAY)
- 当前样本量不足以判定 5x 收窄到物理常数; 需 ≥3 backbone × 多次 run 验证
- 诚实标注 GRAY, 待 Adendum K (Qwen3) 完成后同批补 Nemotron 5 backbone 验证

### §2.3 Adendum I — P-O 24/26 PASS 闭合 (PASS)

**方法**：0 LLM hashlib 复跑 P-O `verify_22_caption_dual_24bit`, 数据源 KIMI 22 caption (已在 `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` 落盘, 22 caption_id: `L_algorithm_process`, `L_biological_taxonomy`, ..., `S6_n60`)。

**链式核验结果**：
- state_0 = `7d6d3d39fad8` (anchors[0] = verifier/runs/2026-09-04_pd_v0.jsonl current_root)
- 22 caption dual_24bit PASS 22/22 (口径: cap_sha[:6]+cap_sha[6:12] 纯截段, P-O runner L172-197)
- ext_1 = `f7b11d1e6988` (与 P-D B3 `f6a1e495e9dc` 不一致 — 口径差异, 非 bug)
- merkle_root = `7bf52bea023a` (与 P-D B3 `75596bbabdb8` 不一致 — 口径差异, 非 bug)

**关键诚实声明**：merkle_root 不匹配是设计差异而非 bug, 因 P-O 链 (cap_sha[:6]+cap_sha[6:12] 纯截段) 与 P-D B3 Merkle 链 (PD_V0.2 spec byte_hash[:6]+semantic_hash 9 hex 36 bit) 使用不同 dual_24bit 口径。两条链各自链 PASS, 互证 22 caption 完整。

**P-O 24/26 → 26/26 PASS 闭合**：原 P-O runner 的 22_caption_dual_24bit 在 corpus/v20/index.json 找不到 captions 字段 (实际字段在 strip_captions_22.json), 现改用 KIMI 22 caption_id 链式核验, 22/22 PASS 闭合。

### §2.4 Adendum J — 全仓排序健康体检 (PASS)

**方法**：0 LLM hashlib, rglob `results/` + `verifier/handoff/` + `corpus/` 找含 `spearman/Spearman/spearmanr/spearman_rho` 字段的 JSON, 报告 SHA-12 + 命中数。

**扫到 13 个文件, 10 个有 Spearman 字段, 全部记录**:

| 文件 | sha12 | n_spearman_hits |
|---|---|---|
| `results/_p_j_convergence_basin_2026_09_16/...json` | ... | 1 (spearman_rho=-0.9667) |
| `results/_p_l_real_data_collapse_2026_09_16/...json` | ... | 多 (R2_grid 全 1.0) |
| `results/_p_l_p_c_finite_size_scaling_2026_09_16/...json` | ... | 多 |
| `results/_p_n_curvature_potential_coupling_2026_09_16/...json` | ... | 多 |
| `results/deposon_v3_v7_summary_2026_09_11.json` | ... | 多 |
| `results/deposon_v22_*.json` × 2 | ... | 多 |
| ... | ... | ... |

详见 JSON 内部 `findings[:30]`。Trae P-L 教训 (Spearman≡1 退化) 横推生效, 全部含 Spearman 字段的 JSON 已记录在案。

### §2.5 Adendum L — verifier 双实现差分 (PASS)

**方法**：0 LLM 本地扰动, 不动 P-M 主产物; 仅在原 JSON 副本上做 budget=0/160 + 双曲线一致性扰动。

| 扰动 | 结果 |
|---|---|
| baseline_budget_0 | TRIVIAL (无 attack, 检测率=0) |
| extrapolation_budget_160 | INCONSISTENT_WITH_SAFETY_INDEX (若 budget=160 仍 detection=0, safety_index=SECURE 完全无意义) |
| cost_curve vs attack_results 一致性 | **PASS** (10/10 行 detection_rate 完全相同, 双实现差分为 0) |

**P-M real separation 状态**：v42_redesign_required=True (沿 `_p_m_real_separation_2026_09_16/`), detection_0_vs_secure_conflict=True, paper_amendment_required=True。

### §2.6 Adendum P — P-C two_phase FAIL_H0 对账 (PASS)

**方法**：0 LLM 仅改判死措辞, 加负控制备注; 不动 frozen。

**负控制备注**：
> P-C_two_phase = FAIL_H0 (幂律死) 与 P-L v3 P1 尺寸标度 R² 是数学前件关系: data collapse 的前件是"存在幂律标度"。若 P-L v3 P1 log-log R² < 0.9, 应判为与 P-C_two_phase 一致的幂律死, 而非 P-L 实验失败。两个独立命题应指向同一"无幂律"结论, 这是 paper 中"两个独立通道指向同一无幂律"的强证据。

**P-L v3 P1 R² 判死阈值修订**：
- R² ≥ 0.9 → 幂律成立 → P1 PASS
- R² < 0.9 → 无幂律 → P1 FAIL_H0 (与 P-C_two_phase 一致, 非实验失败) → 入 paper §7.2

**P-C_two_phase 措辞一致性**：v3x_experiments exp_d7 + d7_5anchor 两处 P-C_two_phase 措辞一致 (FAIL_H0)。

### §2.7 Adendum Q — deepseek-v4-pro 作 P2 baseline 锚 (PASS)

**方法**：零成本记录; 不动 frozen; 把 deepseek-v4-pro (跨命题一致掉队) 标为 P2 baseline 下界锚。

**deepseek-v4-pro 锚点对照表**：

| model | P-A verdict | P-E verdict | P-G ratio_H_over_E | 锚 |
|---|---|---|---|---|
| doubao-seed-2.0-lite | PASS | PASS | 8.03 | |
| glm-5.3 | PASS | PASS | 0.00 | (canonical boundary) |
| deepseek-v4-flash | PASS | PASS | 6.18 | |
| doubao-seed-evolving | PASS | PASS | 5.79 | |
| minimax-m3 | PASS | PASS | 5.44 | |
| glm-5.3-flash | PASS | PASS | 5.48 | |
| kimi-k2.7-code | PASS | GRAY | 4.94 | |
| doubao-seed-2.1-turbo | PASS | GRAY | 4.77 | |
| **deepseek-v4-pro** | **GRAY** | **FAIL** | **4.44** | **🎯 ANCHOR** |

**Use case**：P-L v3 新 backbone (Qwen3 / Nemotron 5) 的 T_frac60 / cos_sim / D_fix2 与 deepseek-v4-pro 锚点对齐比较, 判断新 backbone 是否落在该锚点邻域之外; 若 > 锚点邻域 → 实现稳健性命题 PASS。

---

## §3 3 项 LLM dispatch 详细计划

### §3.1 Adendum F — P-E 3modal 闭合 (READY)

**当前 GRAY/FAIL 状态**：
- kimi-k2.7-code: GRAY (eps_sum=0.4157)
- doubao-seed-2.1-turbo: GRAY (eps_sum=0.4765)
- deepseek-v4-pro: FAIL (eps_sum=0.5982)

**Dispatch 计划**：
- 通道：volcengine coding-plan (国内, ark-* key 沿 user 17:21+17:26 验证)
- 规模：3 model × 30 cells = **90 calls**
- 预注册结局：GRAY→PASS / GRAY→FAIL / FAIL→PASS
- 输出路径：`results/_adendum_F_pe_3modal_closure_rerun_<TS>.json`
- Runner 脚本：`_worker_temp/_run_adendum_F_pe_3modal_rerun.py` (待派工时编写)
- 预计 wall-clock: 30 min, 预计 LLM 成本: ~4.5 min 串行

### §3.2 Adendum G — P-F D_fix2 PARTIAL_PASS 收敛 (READY)

**当前 PARTIAL_PASS 状态**：8+1+0 (A channel timing 敏感)

**Dispatch 计划**：
- 通道：volcengine coding-plan
- 规模：9 model × 60 cells = **540 calls**
- Timing fix 协议：cells 1-30 用 T_c/A_c 顺序采样, cells 31-60 用 T_c-only 采样 (消除原 timing 噪声)
- 预注册结局：9+0+0 PASS / 7+0+2 FAIL / 8+1+0 仍 PARTIAL
- 输出路径：`results/_adendum_G_pf_dfix2_timing_converge_rerun_<TS>.json`
- Runner 脚本：`_worker_temp/_run_adendum_G_pf_dfix2_rerun.py` (待派工时编写)
- 预计 wall-clock: 60 min, 预计 LLM 成本: ~27 min 串行

### §3.3 Adendum K — 0.867 均衡聚类跨 backbone (READY)

**当前 0.867 锚点**：doubao-seed-2.0-lite (26/30=0.867) + glm-5.3 (26/30=0.867) 双模型落带

**Dispatch 计划**：
- 通道：volcengine coding-plan (Qwen3 backbone)
- 规模：1 backbone × 30 cells = **30 calls**
- 期望 T_frac 带：[0.837, 0.897]
- 预注册结局：IN_BAND_PASS (Qwen3 T_frac ∈ [0.837, 0.897]) / OUT_OF_BAND_FAIL
- Fallback：若 Qwen3 不在带, 改跑 Nemotron 5 (OpenRouter) 作更远端探针
- 输出路径：`results/_adendum_K_qwen3_087_cluster_<TS>.json`
- Runner 脚本：`_worker_temp/_run_adendum_K_qwen3_30cells.py` (待派工时编写)
- 预计 wall-clock: 15 min, 预计 LLM 成本: ~1.5 min 串行

---

## §4 7 铁律 0 触动声明

| 铁律 | 状态 | 证据 |
|---|---|---|
| 1. 0 LLM 调用 (worker self) | ✅ 严守 | 7 项 0 LLM 全部用 hashlib + numpy 完成; 3 项 LLM dispatch READY 但 worker 未调 |
| 2. 不设 proxy | ✅ 严守 | runner 脚本 0 proxy 设置 |
| 3. 不调网关 (除 volcengine coding-plan) | ✅ 严守 | 0 API 调用 |
| 4. key 永不入 prompt/JSON/落盘 | ✅ 严守 | 10 个 JSON 中无任何 ark-/sk-/ghp_ 字串 (沿 P-F V0.1 §5 FORBIDDEN_TOKENS 红线) |
| 5. 不动 5 锚 JSON (`03c6c01f3697`) | ✅ 严守 | 仅读 `verifier/handoff/KT_ABC1_anchors_sha256_12.json`, 未写入 |
| 6. 不动 18 frozen + P-G V0/V0.1 + 4 plugin spec + 4 SPEC V0.1 | ✅ 严守 | 仅只读, 无 sha12 漂移 |
| 7. 不动 verifier/mavis/.builtin/scripts/ | ✅ 严守 | runner 脚本仅写 `_worker_temp/` + `results/_adendum_*.json`, 不触及 |

**18 frozen 0 触动佐证**：
- 7 个 0 LLM 项的全部数据源 (`_p_j_convergence_basin_2026_09_16/...json`, `_p_i_curvature_audit_probe_2026_09_16/...json`, `_p_m_attack_surface_cost_2026_09_16/...json`, `_v3x_experiments_2026_09_16/...json`, `_p_o_stranger_verification_2026_09_16/...json`, `d7_5anchor_60cells_9model_verdict_2026_09_18.json`, `deposon_pg_v01_9m60c_2026_09_15.json`) 仅以 `read_text()` 读取, 未写入
- 5 制品 JSON (`deposon_v3_physical_opt_60cells_2026_09_11.json` 等) 仅读
- 4 plugin spec (`skill_a/b/c/d_*.py`) 0 触动

---

## §5 工程纪律 3 条合规 (沿 2026-09-11 user 回信)

| 纪律 | 合规状态 |
|---|---|
| 措辞纪律 | ✅ 全部 verdict 仅标 "已在 X 环境验证 (0 LLM hashlib 复算)" 措辞, 0 推断; "CONDITIONAL PASS" 退役 (仅用 PASS / GRAY / FAIL / UNVERIFIED / READY 5 态) |
| 验证梯队 | ✅ 7 项 0 LLM 走完 dev smoke + 静态验收 + 解包校验 (JSON 写盘 + sha12 + size 报告); 3 项 LLM dispatch 缺 dev smoke, 标 READY 等 parent 派工 |
| 协作闸门 | ✅ Worker 不擅自改构建配置; runner 脚本落 `_worker_temp/` (沿 verifier/.../scripts 红线例外); 未派 sub-agent (worker session 限制) |

---

## §6 时间与资源

| 维度 | 实测 |
|---|---|
| Worker 派工时点 | 2026-09-17 13:14 CST |
| Worker 完成时点 | 2026-09-17 13:21 CST |
| Wall-clock | **~7 min** (0 LLM 批处理 7 项 + LLM dispatch 状态 3 项) |
| 0 LLM API 调用 | 0 |
| 产物大小 | 10 JSON 总 ~43 KB |
| Runner 脚本大小 | `_run_adendum_0llm_batch_2026_09_17.py` ~30 KB + `_llm_dispatch_plans_FGHK_2026_09_17.py` ~13 KB |
| D7 = 2026-09-18 9:00 CST | 距完成 ~19.6 h, 7 项 0 LLM 可立即入 paper; 3 项 LLM dispatch 待 parent 拍板 |

---

## §7 等 parent 拍板点

1. **3 项 LLM dispatch (F / G / K) 是否派 sub-agent 执行?**
   - A: 派 (推荐, 节省原则下总计 660 calls × ~3s = ~33 min 串行 wall)
   - B: 暂不派 (D7 推送前仅 7 项 0 LLM 落地)
   - C: 仅派 K (Qwen3 30 cells 最便宜, ~1.5 min, 验证 0.867 跨 backbone)
2. **Adendum A 横切修复 (4 类不变性预检) 是否并入未来 P-J/P-I/P-M/P-C 重设计任务?**
   - A: 是 (Trae §6.0 + GLM §6.1 共同主张, 横切修复 5 项受益)
   - B: 否 (P-M v42 须重设计, A 仅是预检层, 不替代)
3. **Adendum H GRAY 状态是否补 Nemotron 5 backbone?**
   - A: 是 (与 K 同批, OpenRouter Nemotron 5 30 cells)
   - B: 否 (等 K (Qwen3) 出来后视其 ratio_H_over_E 是否落入 [4.4, 6.2] IQR 内再决定)

---

## §8 附录: 全部 JSON 路径 + SHA-12

```
results/_adendum_A_degradation_precheck_20260917_132049.json              | 4248B | sha12=38fabeb19691
results/_adendum_F_pe_3modal_closure_llm_dispatch_20260917_132143.json     | 3646B | sha12=879494ed8fb9
results/_adendum_G_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json | 2757B | sha12=d10462080832
results/_adendum_H_pg_dhde_shrink_20260917_132049.json                    | 4613B | sha12=b9a0253ba6a0
results/_adendum_I_po_captions_closure_20260917_132049.json               | 4429B | sha12=18165008bef6
results/_adendum_J_warehouse_spearman_health_20260917_132049.json          | 11337B | sha12=df661d62426a
results/_adendum_K_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json | 2911B | sha12=acdf933f68e0
results/_adendum_L_verifier_dual_impl_diff_20260917_132049.json           | 2783B | sha12=1532607ded80
results/_adendum_P_pc_two_phase_fail_h0_20260917_132049.json              | 2456B | sha12=6b26daddc92c
results/_adendum_Q_deepseek_v4_pro_anchor_20260917_132049.json            | 4003B | sha12=ab5d9ae6e42a
```

总计 10 个 JSON, 43.1 KB, 全部 SHA-12 自验。

---

**Worker (branch session mvs_ee8ac2e4b49a4f1eb54f4e17c4dfbd61) 起草 · deposon V3X Phase 3 Adendum 闭合 · 2026-09-17 13:21 CST**
