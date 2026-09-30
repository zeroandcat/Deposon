# V3 假象类补审改判系列预登记 v1（protocol-keeper · 2026-09-27）

> **性质**：V3 假象类 9 条补审改判系列预登记 v1（不覆盖 V3 既有任何件）
> **派工单字面**：本件由 Mavis root session 派工单「V3-R 补审系列预登记」触发（PI 2026-09-27 问卷 `ask_0ec0da85da47b18a9696065e` Q1 = 补审后改判 / Q2 = 全部假象类 9 条）
> **判死先于实验**：本件 §2 全 9 条 kill-line 一次性冻结，0 私设条款（冻结后执行棒只准按字面跑，0 擅调）
> **构造非退化自证**：本件 §1.2 每条补审构造在数据面 §0.3 落位登记，n_distinct 全 > 3 + 退化警报机制同步纳入
> **0 LLM**：补审为本地机械（博弈/物理模拟/统计复算），0 LLM 调用；构造可行性查不到的如实登记未决
> **状态**：**待 PI 复核生效，生效即锁**；冻后 v1.x 修订须另立预登记
> **沿用边界**：判死线先于实验 / 0 擅调阈值 / 派生 JSON 不合并 / key 永不明文 / V1–V3 frozen 0 触动

---

## §0 输入件 SHA-12 核验（只读，先核后用）

### §0.1 派工单指定核心 3 件（frozen 不触动，全做只读核验）

| # | 件 | 派工字面 SHA | 实测 SHA-12 | 字节 | 状态 |
|---|---|---|---|---|---|
| 0-A | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | 派工单未列 SHA | **`24EAFC05A217`** | 28,207 | ✓ 在盘（Trae v3 回函 §1.2 标注表 39 行 + §2 回审表 21 行 + §3 走读 + §6 老交代） |
| 0-B | `results/_v3_supplement_verdict_2026_09_23.md` | 派工单未列 SHA | **`9421E78B7E3C`** | 15,247 | ✓ 在盘（Worker 补实验判决摘要，C1–C5 诊断） |
| 0-C | `results/_v4_pi_cot_v3_prereg.md`（fallback 锚） | `B7547329AF2E`（**派工单字面**） | **`1A90FD8F385A`** | 27,223 | ⚠ 派工单 SHA 与盘上不符——派工单给 `B7547329AF2E`，全仓扫 0 命中，盘上实测为 `1A90FD8F385A`；本件以盘上实测为准（fallback 锚结构字面 §1 / §2 / §4 / §5 / §8 / §9 与派工单描述完全吻合） |

> **派工单 SHA 不符老实交代**：派工单 `B7547329AF2E` 在 `D:/私人资料/deposon-repo/` 全仓扫 0 命中，盘上 `_v4_pi_cot_v3_prereg.md` 实测 SHA-12 = `1A90FD8F385A`。本件**不代为修订派工单**，仅在 §0 表如实登记，并以下列三条交叉证伪/证实为据：
> (a) 文件名、章节结构、§10 生效登记段全部与派工单描述一致；
> (b) §0 输入件 SHA-12 表格式、§4 kill-line 字面引用格式、§9 老交代格式均与 v3 锚件字面同款；
> (c) 派工单既给失效 SHA 又给结构字面，说明 SHA 字段为转写错位，结构字面为真指令。本件按结构字面执行。

### §0.2 9 条各自原结论所在的 V3 报告 / JSON（frozen 不触动，全做只读核验）

| # | 对象 | 原始结论所在 V3 件 | 实测 SHA-12 | 字节 | 核心判据字段 | 状态 |
|---|---|---|---|---|---|---|
| 1 | BOSS-P-A1 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | `D9E14ED29FB9` | 8,753 | `rbr_iters_per_graph[22]`、`rm_iters_per_graph[22]`、`bayes_iters_per_graph[22]`、`rbr_multiplier_mean=145.8182` | ✓ 在盘；22/22 实测 `rm_iter=6` 全常量（Trae §1.2 #1 / C1 一致） |
| 1-r | BOSS-P-A1 runner | `deposon_team/plugins/boss_pa_1_rbr_rm.py` | `1935F164D5F3` | 17,743 | `simulate_rm` / `simulate_rbr` / `bayesian_nash_iter` 三函数 | ✓ 在盘（frozen 范围内 §5「不动」仅作只读核验源） |
| 1-rep | P-A 1 周判死 | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | `A3FA45E7D121` | 19,751 | L270「540 cells (9 model × 60 cells) 守恒 PASS residual = 0」 | ✓ 在盘（frozen 报告正文，本件不动） |
| 4 | BOSS-P-A3 | `results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `18C9C370A6AE` | 9,098 | 22 graph_results × {ess_freq, is_ess, ess_match} | ✓ 在盘；22/22 实测 `ess_freq=0.5` / `is_ess=True` / `ess_match=false` 全常量 |
| 4-r | BOSS-P-A3 runner | `deposon_team/plugins/boss_pa_3_replicator_dynamics.py` | `268F708B96AE` | 12,900 | `ess_freq` 派生 + `is_ess` Smith 1973 判据 | ✓ 在盘 |
| 5 | 540 cells 守恒审计 | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` §`v3_540_conservation_check` | (`D9E14ED29FB9` 同 #1) | — | T540_sum=384 / R540_sum=78 / A540_sum=78 / `conservation_residual_540=0` / `conservation_pass=true` | ✓ 在盘；residual=0（整数严格），但 Trae 记 max dev 2.22e-16 系浮点逐项求和形式（§0.4 注） |
| 5-anc | 540 cells 守恒锚 | `results/_v3x_conservation_anchor_2026_09_17.txt` | `425507BB555B` | 940 | V0 锚路径 = `_archive_deposon_2026_09_17/verifier/audit/conservation.py` V0 SHA-256[12] = `4bdec2683f06`（22,105 B） | ✓ 在盘；写明「verifier/audit/ NTFS ACL 阻回写，B 路径可用」 |
| 5-rep | P-F 1 周判死 | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` L106 「conservation_status PASS（整数严格守恒）」 | `BA8F3894969D` | 15,985 | 同 #5 字段 | ✓ 在盘（frozen 报告正文，本件不动） |
| 8 | BOSS-PC-3 | `results/boss_pc_3_a3_clipping_2026_09_15.json` | `717C26DF5A00` | 1,265 | `trials[3].r2_delta_full_minus_clipped` | ✓ 在盘；3/3 实测 delta ≡ **0.0**，clipping 为 no-op |
| 10 | P-C exp_3_3 | `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json` §`exp_3_3_p_c_supplement.per_model_per_eta.{model}.r2_per_eta[7]` | `05B4649985B5` | 17,053 | η 扫 [0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 100.0] × 9 model | ✓ 在盘；9/9 模型 `r2_per_eta[7]` 元素逐字同（model 间无 variation，**唯一变量是真 T_frac**），但逐 model 内 η 扫描有真分布 |
| 12 | BOSS-PE-2 | `results/boss_pe_2_real_transverse_ising_2026_09_15.json` | `04CEDB126B98` | 3,553 | `per_model[9].h_c_at_T` / `transverse_ising_region` / `dist_to_h_c_T` / `D_fix2` | ✓ 在盘；`h_c_at_T ≡ 0.5 (9/9)`、`transverse_ising_region ≡ false (9/9)` 全常量；`dist_to_h_c_T` 与 `D_fix2` 有真分布 |
| 12-rep | P-E 1 周判死 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `664DD320F549` | 13,109 | §1.2 risk3 「D_fix2 ADOPTED, S_eff REJECT」 | ✓ 在盘（frozen） |
| 26 | P-J | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | `19F0A2CB8CEF` | 1,669 | `convergence_rates` 9 model | ✓ 在盘；9/9 实测 `convergence_rate = 0.1` 全常量；Spearman ρ = -0.9667 立在常量 vector 上 |
| 27 | P-L P-C FSS | `results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json` | `00DF93A112F7` | 9,076 | `data_collapse_R2_grid_scan.max_R2` / `best_params = [1.5, 0.1]` | ✓ 在盘；max_R2 = 0.327492（ν=1.5, η=0.1 单点），verdict `PARTIAL_FAIL_H0`；R2 网格内有跨 (ν, η) 真分布（非单一常量） |
| 28 | P-M attack surface | `results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json` | `1F11ED31273D` | 5,266 | `attack_results[10].detection_rate` × budget ∈ {8,16,24,...,80} | ✓ 在盘；10/10 实测 `detection_rate ≡ 0.0` 全常量 |
| — | V3X 1 周判死 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `AFD2161E6544` | 8,526 | 4 路径总分（与 §1.2 #38 标注表对应） | ✓ 在盘（frozen 报告正文，本件不动） |

### §0.3 输入链核验小结（沿 V3 既有派工 5 件 + 上表 16 件 = 实核 21 件，全部 0 触动）

- 21 件输入**全部只读核验**，未触动任何 byte（SHA-12 与目录扫描基线一致；frozen 件沿 §5「不动」边界一律只读）
- 派工单 SHA 字面 `B7547329AF2E` 与盘上 `_v4_pi_cot_v3_prereg.md` 实测 `1A90FD8F385A` 不符 → §0.1 老交代段登记，未代为修订派工单
- 派生 JSON 件：仅 `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json`（P-C exp_3_3）+ `_p_j/_p_l/_p_m` 三个目录下的 results JSON 在 09-16/09-17 期间有派生补采；本件只读不并——派生 JSON 不合并沿用

### §0.4 #5 540 cells 守恒审计的关键事实澄清（实测登记）

- boss_pa_1 JSON 写 `conservation_residual_540 = 0`（整数严格守恒形式：`T540_sum + R540_sum + A540_sum = 384 + 78 + 78 = 540`）
- P-F 1 周报告 §6 写「PASS（整数严格守恒）」
- Trae 回函 §1.2 #5 记「max dev 2.22e-16」系浮点逐项求和形式（IEEE 754 双精度机器 epsilon，2⁻⁵²）
- **两种形式同机制**：residual ≈ 0 是**构造恒等**——每 cell 一次性归类为 T/R/A 三态之一（per_cell 指示函数 0/1），9 model × 60 cells 求和 = 总 cell 数 N = 540，**残差即浮点舍入极限**，与实验观测无关；Trae 的 `T+R+A=1`（frac 形式）与其整数形式互补同源
- 本件以「结构性恒等（不构成实验证据）」登记 #5，与 Trae §1.2 一致

---

## §1 9 条假象类补审清单表（沿 Trae §1.2 + C1–C5 诊断派生）

### §1.1 三类假象的机制归类（先声明，后逐条）

- **假成立（3 条：#1, #4, #12）**：原结论为存活型 PASS / DIFFERENTIATED；构造使判据输入为常量，结论落在常量读数上，未受真审；补审以**重构造 + 真分布** 为方向
- **假证伪（5 条：#8, #10, #26, #27, #28）**：原结论为证伪型 FAIL / UNVERIFIED；构造使判据退回为 no-op 或判据恒同，结论未真受审；补审以**重构造 + 真判据分布** 或**判据物理量重定义** 为方向
- **结构性恒等（1 条：#5）**：原结论为 STRICT_CONSERVATION；T+R+A=N 是构造恒等，残差是浮点舍入极限，无实验鉴别力；补审以**非恒等审计面**（如 per-cell pairwise 偏离 + bootstrap CI 跨真实扰动）为方向

### §1.2 全表（9 条逐条）

| # | 对象 | 原结论字面 | 类型 | 死因（一句话） | 补审构造方向 | 数据面可得性 | 改判规则 |
|---|---|---|---|---|---|---|---|
| 1 | BOSS-P-A1（RBR/RM 倍数） | DIFFERENTIATED（rbr_multiplier_mean=145.8182 ≥ 2.0×） | 假成立 | `simulate_rm` 22/22 `rm_iter ≡ 6`（构造 L176 `if max(R_A)<1e-3 and t>5: return t` 触发）+ `bayesian_nash_iter` 22/22 ∈ {1, 200}（构造 L189 `return 1 if nash else 200` 二值） | (a) `simulate_rm` 阈值由 1e-3 → 1e-9 或改用真迭代 `t = n_iter`；(b) `bayesian_nash_iter` 改真 best-response 跑至收敛（最大迭代 2000 + ε=1e-9）；(c) `rbr_multiplier = rbr_t / bayes_t` 跟随 (a)+(b) 派生 | boss_pa_1 JSON `D9E14ED29FB9` + runner `1935F164D5F3` + 22 graphs（D7_WANG · `0EDB2AEC1660` v20 baselines 真缺件，沿 C2 路径用 stored 22 graphs seed=210021 reweight）；9 model 沿 V2 阶段 2 dual mainline | 补审通过 → 改判「真成立」（差异有真分布）；补审证伪 → 改判「真证伪」（结构性差异不成立）；仍不可行 → 维持「假成立」+ 沿勘误链 E-41.x 标注 γ=构造性常量 |
| 4 | BOSS-P-A3（Replicator/ESS） | DIFFERENTIATED（0/22 ESS 重合） | 假成立 | `ess_freq ≡ 0.5`、`is_ess ≡ True`、`ess_match ≡ False` 三项 22/22 全常量 → ESS 判据恒同 | (a) `ess_freq` 计算不绑死 0.5 起点（重参数：起频扫描 or 随机 0.3~0.7）；(b) `is_ess` Smith 1973 判据按 Taylor & Nowak 2006 ESS 完整定义（邻域 ≤ ε 全检验 ε=0.1 → 1e-3 → 1e-6 三档）；(c) `ess_match` 阈值 0.1 与真实 `deposon_freq` 离散度联动（22 graph × 3 ε） | boss_pa_3 JSON `18C9C370A6AE` + runner `268F708B96AE` + v20 baselines 真缺件（同 #1） + 9 model 真实 graph 邻域扰动 | 同 #1（同机制：构造性常量） |
| 5 | 540 cells 守恒审计 | STRICT_CONSERVATION（residual ≈ 0 / max dev 2.22e-16） | 结构性恒等 | T/R/A per-cell 指示函数求和 = N 是构造恒等；残差是浮点舍入极限，无实验鉴别力 | (a) 非恒等审计面：per-cell pairwise T↔R / T↔A / R↔A 偏离度 + bootstrap CI（n=1000, seed=42）跨真实扰动（每个 cell 强制重抽分类 β 次）；(b) per_model 守恒面异质性：9 model 的 T/R/A 分布均值/方差差，证「守恒」是否为普遍物理现象 | conservation anchor `425507BB555B` + boss_pa_1 `D9E14ED29FB9` §`v3_540_conservation_check`（T540_sum/R540_sum/A540_sum）+ P-F 1 周报告 §6 | 重构造给出非平凡 bootstrap CI 上界 / per-model 异质性差异 → 改判「真成立」（守恒审计有物理意义）；CI 仍 trivial → 维持「结构性恒等」+ γ=构造恒等 |
| 8 | BOSS-PC-3（A3 clipping） | FAIL（worst_clipped_r2 = 0.3362 < 0.7） | 假证伪 | 3 trial `r2_delta_full_minus_clipped ≡ 0.0`（full r2 = clipped r2 逐 trial 一致）→ clipping 为 no-op | (a) `clip_r2_min = 0.7` 阈值改为更激进（如 0.3/0.5/0.7 扫描），并加 per-trial seed-differ 重抽；(b) 真引入 N 范围裁剪：在裁剪前后用 bootstrap（n=1000）算 r2 比（裁剪变 + delta ≠ 0 才叫真裁剪）；(c) `pre_registered_threshold.n_full` 与 `n_clipped` 重设（7 vs 5 → 7 vs 4 vs 3 扫描） | boss_pc_3 JSON `717C26DF5A00` + spec `P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md §5 攻击 A3` + 9 model real data | 真裁剪使 delta ≡ 0.0 至少被打破一次 → 改判「真证伪」或「真成立」视裁剪后 r2；仍 ≡ 0 → 维持「假证伪」+ γ=no-op |
| 10 | P-C exp_3_3（r2_per_eta） | 该维度 UNVERIFIED | 假证伪 | 9 model `r2_per_eta[7]` 逐字相同（实测前 6 个 model 元素 [.1984, .1966, .1889, .1797, .1626, ...]，完全一致）→ model 维无 variation，仅 `t_frac` 是真变量 | (a) 真引入 model 维 variation：每次扫描抽 model-specific 子集重算 R²（不沿用 V2 阶段 5 全 dataset）；(b) 真 η 物理意义：η 解释为温度抖动（real Langevin-style），而非单纯 scaling；(c) 加 per-model-confidence-interval bootstrap（n=1000） | v3x_experiments JSON `05B4649985B5` §`exp_3_3_p_c_supplement` + 9 model data | η 扫与 model 至少有一个维度有真 variation → 改判「真成立」或「真证伪」视 verdict；两维仍 trivial → 维持「假证伪」+ γ=τ恒同 |
| 12 | BOSS-PE-2（real transverse Ising） | PASS（9/9 model 显著偏离，distance_distribution.outside_gt_0.15 = 9） | 假成立 | `h_c_at_T ≡ 0.5`（Pfeuty 1D chain 简化，构造恒同）+ `transverse_ising_region ≡ false`（同）→ 判据输入恒同；判据分母是常量，分子 `dist_to_h_c_T` 有真分布但**判据本身退化为 downstream 标签** | (a) `h_c_at_T` 真随机化：从 Pfeuty Phase Diagram 抽样 h_c（T, J）连续分布，至少 100 个 sample/model；(b) `transverse_ising_region` 用真 phase boundary 测试（沿 Jordan-Sucher-Votek 1999 数值解 + per-model empirical 散点）；(c) 主判据换成 `D_fix2`（P-E 报告 §1.2 risk3 已 ADOPTED）——既有真分布，与 BOSS-PE-1/3 一致 | boss_pe_2 JSON `04CEDB126B98` + 9 model D_fix2 真分布 + P-E 报告 `664DD320F549` §1.2 risk3 | 重构造 verdict 与 D_fix2 真分布一致 → 改判「真成立」（与 D_fix2 同源）；verdict 与 D_fix2 仍冲突 / 判据输入仍恒同 → 维持「假成立」+ γ=判据恒同 |
| 26 | P-J（convergence basin） | UNVERIFIED | 假证伪 | 9 model `convergence_rate ≡ 0.1`（var = 0.0，n_distinct = 1）→ 对常量 vector 算 Spearman 无定义（ρ=-0.9667 系 spurious） | (a) 重定义 convergence_rate：真迭代次数 / perturbation budget（如 N_iterations / N_attempts 或 best_response_until_eps）；(b) 真引入 per-model perturbation：每 model 在 T_frac60 附近 ±0.05 抖动 100 次，统计收敛率真分布 | p_j JSON `19F0A2CB8CEF` + 9 model `T_frac60` 真分布（0.5333–0.8667） | 真 convergence_rate 分布非 trivial（n_distinct > 3，std > 0）→ 改判「真成立」或「真证伪」；仍 trivial → 维持「假证伪」+ γ=常量 |
| 27 | P-L P-C finite-size scaling | UNVERIFIED | 假证伪 | `max_R2 = 0.327492` 恒 < 0.9 → `final_dang_verdict ≡ PARTIAL_FAIL_H0` → 数据坍缩判据恒同 | (a) 真 finite-size scaling：跨 N = 20/40/60/80/120 cells 重展 data collapse，每 N 各跑 R²（避免单点 (ν=1.5, η=0.1) 的 hidden fitting）；(b) `data_collapse_R2_grid_scan.max_R2` 之上加 scaling exponent ν 的 bootstrap CI（n=1000） | p_l_p_c JSON `00DF93A112F7` + 9 model 真分布（p_c per_model_verdict 8 PASS + 1 GRAY；p_e per_model_verdict 6 PASS + 2 GRAY + 1 FAIL）+ D7 60cells 真 dataset | 跨 N scaling exponent 真有 τ（CI 跨零）→ 改判「真证伪」（FAIL 成立）；max_R2 仍 < 0.9 → 维持「假证伪」+ γ=τ hidden fitting |
| 28 | P-M attack surface | UNVERIFIED | 假证伪 | 10 budget × `detection_rate ≡ 0.0`（8–80 全部 0/8 detected）→ 检测率全低于随机猜测 0.5，判据退化 | (a) 真 budget 扫描：8/16/24/.../80 → 加 1/2/3/4 真边界 budget + 真攻击模型（如 one-bit swap / two-bit swap / contiguous flip 三类型）；(b) 真 detection 算法：per-cell 距离阈值 + 5 锚真值作 ground truth；(c) safety_budget_lower_bound 重测：≥ 80 是否真满足 | p_m JSON `1F11ED31273D` + 5 锚 JSON 真值（`03c6c01f3697`，但 E-15 锚链断裂需 fallback §0.1） | 至少一个 budget 档 detection_rate > 0 + 真 detection 算法非 trivial → 改判「真成立」或「真证伪」视 safety_bound；仍 ≡ 0 → 维持「假证伪」+ γ=detection 退化 |

**辅助说明**：
- `n_distinct > 3` 为本表「真分布」构造的最低门槛 —— 任一输入字段 n_distinct ≤ 3 = 退化警报（沿 protocol-keeper 防退化构造审查 §4）；详 §3.1 难度分层
- 「补审构造方向」中 (a)/(b)/(c) 表示三个递进构造层；worker 跑前须验证**至少 (a) 不退化**才能开跑 (b)/(c)
- 「数据面可得性」中 v20 baselines 真缺件沿 #1 V3 review §3.4 E-15 已登记；stored 22 graphs seed=210021 为本件主证据面，沿 V3 补实验判决 §0

---

## §2 判死线（一次性冻结，冻后 0 私设）

### §2.1 总判死线 K-V3R-0（9 条共同遵守）

> **本节为本预登记最严纪律**：

- **K-V3R-0-A 防退化门**：每条补审构造在 worker 跑前须在盘上数据面自证非退化（n_distinct > 3 + std > 0 + min-max 跨 grid 至少 3 档），任一输入字段 n_distinct ≤ 3 = **退化警报** —— 须换构造或判「不明」，不许带病开跑；这是构造非退化自证的最低门槛
- **K-V3R-0-B 沿用阈值**：补审沿用 V3 既有阈值字面（pre_registered_threshold.*，pre_registered_constants.*）；0 新设阈值；确需新阈值的条目显式列「新阈值提案」于 §1.2 补审构造方向的备注，留 PI 拍板
- **K-V3R-0-C 双口径**：9 条中任一条补审给出 verdict 时，须附 1）**重构造 verdict**（沿新构造算）+ 2）**沿原 V3 阈值字面算 verdict** —— 两口径**一致** ⇒ 改判成立；**不一致** ⇒ 维持「假象」原标注 + γ 升级（沿 §2.3 改判规则表）
- **K-V3R-0-D 派生 JSON 不合并**：补审过程中每条产出一独立 JSON（如 `results/_v3_recheck_NN_*.json`），不并入既有 _p_* / boss_* JSON
- **K-V3R-0-E 0 LLM**：补审为本地机械（博弈/物理模拟/统计复算），0 LLM 调用；若某条构造经勘察必须 LLM 辅助，停下如实报 PI 拍板（V4 no_llm 放开边界需明示）
- **K-V3R-0-F 锚链 fallback**：#5（540 cells 守恒）落入 §0.4 / §1.1 已登记的 E-15 锚链断裂 —— 补审主证据面沿 `_archive_deposon_2026_09_17/verifier/audit/conservation.py` 备份路径（沿 `_v3x_conservation_anchor_2026_09_17.txt` 字面）；冻结主路径不可用时**不擅自重写**主路径，改沿 B 路径
- **K-V3R-0-G 仅追加冻结**：冻结后 v1.x 修订须另立预登记；本件 §2 表 + §2.4 TH-* + §1.2 全表 0 触动

### §2.2 逐条 kill-line（K-V3R-N，N=1, 4, 5, 8, 10, 12, 26, 27, 28）

| ID | kill-line 字面（冻后 0 擅调） |
|---|---|
| K-V3R-1 | BOSS-P-A1 重构造（真 `simulate_rm` + 真 `bayesian_nash_iter`）后 `rbr_multiplier` n_distinct ≥ 4 + 真分布（std > 0）→ **PASS（新构造 PASS）**；n_distinct ≤ 3 或 std = 0 → **FAIL**（维持假成立） |
| K-V3R-4 | BOSS-P-A3 重构造（真 ESS 邻域检验 ε=1e-6）后 `ess_match` n_distinct ≥ 4（≥ 4/22 真有 match，≠ 0/22 全 not-match）→ **PASS（新构造 PASS）**；仍 n_distinct ≤ 2 → **FAIL**（维持假成立） |
| K-V3R-5 | 540 cells 守恒重构造（per-cell pairwise + bootstrap CI n=1000）后 CI 上界 > 0（非 trivial）→ **PASS（非恒等成立）**；CI 上界 ≤ 1e-15 → **FAIL**（维持结构性恒等） |
| K-V3R-8 | BOSS-PC-3 重构造（真 clip_r2_min 扫描 + 真 N 范围 + bootstrap）后 `r2_delta_full_minus_clipped` 至少一档 ≠ 0.0 → **PASS / 真裁剪有判据**；3 trial 仍 ≡ 0 → **FAIL**（维持假证伪） |
| K-V3R-10 | P-C exp_3_3 重构造（真 model 维 variation + 真 η 物理意义 + per-model bootstrap）后 ≥ 1 个 η 档下 `r2_per_eta` 跨 model n_distinct > 3 → **PASS**；仍 n_distinct = 1 → **FAIL**（维持假证伪） |
| K-V3R-12 | BOSS-PE-2 重构造（真 h_c(T) 抽样 + 真 phase boundary + 主判据换 D_fix2）后 verdict 与 D_fix2 真分布一致 → **PASS**；不一致 / 判据输入仍恒同 → **FAIL**（维持假成立） |
| K-V3R-26 | P-J 重构造（真 convergence_rate 定义 + 真 perturbation ±0.05×100）后 convergence_rate n_distinct > 3 + std > 0 → **PASS**；仍 n_distinct ≤ 1 → **FAIL**（维持假证伪） |
| K-V3R-27 | P-L P-C FSS 重构造（跨 N = 20/40/60/80/120 scaling + bootstrap CI）后 scaling exponent ν 跨 N bootstrap CI 跨零 → **FAIL（真证伪，与 PARTIAL_FAIL_H0 同方向）**；CI 上界 ≤ 0 → **PASS（结构性恒等成立）**；max_R2 仍 < 0.9 → **FAIL**（维持假证伪） |
| K-V3R-28 | P-M attack 重构造（真 budget 扫描 + 真 attack 算子 + 真 detection 算法）后至少 1 档 detection_rate > 0 + safety_budget_lower_bound 重测 ≥ 80 → **PASS（真成立 PASS）**；仍 ≡ 0 → **FAIL**（维持假证伪） |

> **0 擅调阈值（9 条 kill-line 不动声明）**：上表字面为本预登记 §2.2 一次性冻结，冻后不擅自调换；任一条修订须另立预登记 v1.x

### §2.3 改判规则表（双口径 K-V3R-0-C 派生）

| 补审结果（沿 K-V3R-N） | 与原 V3 标注一致性 | 改判动作（沿 D5-Q2 PI 拍板口径「内参可直接改，已扩散则不得不A」） |
|---|---|---|
| **PASS** | 一致（沿新构造 verdict PASS + 沿原 V3 阈值字面 verdict 同向） | 原 V3 报告**不动**；立**改判件** `results/_v3_recheck_NN_rescript_*.md`，与原标注**并列**写入勘误链 **E-41.x 系** —— 沿 Trae V3 报告已扩散的现状，「不得不 A」（立改判件 = 广而告之），但 V3 原报告 byte 0 触动 |
| **PASS** | 不一致（新构造 PASS + 原阈值 FAIL / UNVERIFIED） | 维持原 V3 标注（不动），但**显式登记**新构造 verdict；归「不明」分支 |
| **FAIL**（即原标注维持） | — | 0 改判动作；原 V3 标注维持，原报告 byte 0 触动 |
| **不明**（构造本身不可行或素材面不足） | — | 维持原 V3 标注（不动），**显式登记 γ = 不可行/不明原因**于改判件；归「V4 收尾整理」待拍板桶（沿 PI 2026-09-27 文件数类账目统一处置原则） |

### §2.4 TH-* 预注册阈值（即锁；沿 V3 既有字面，0 新设）

| # | 来源 | 阈值字面 | 备注 |
|---|---|---|---|
| TH-V3R-1 | boss_pa_1 `pre_registered_threshold` | pa_h1_threshold ≤ 1.3×；pa_h0_threshold ≥ 2.0×；rbr/rm ≥ 2.0× | V3 既有字面 |
| TH-V3R-4 | boss_pa_3 `ess_match_threshold` | = 0.1；replicator dt=0.01, n_iter=500 | V3 既有字面 |
| TH-V3R-5 | conservation.py V0 | 不变量 §3（保守不变，结构恒等） | V0 锚字面 |
| TH-V3R-8 | boss_pc_3 `pre_registered_threshold` | clip_r2_min = 0.7；n_full = [10,20,50,100,200,500,1000]；n_clipped = [20,50,100,200,500] | V3 既有字面 |
| TH-V3R-10 | exp_3_3 `eta_scan` | [0.01, 0.1, 0.5, 1.0, 5.0, 10.0, 100.0] | V3 既有字面 |
| TH-V3R-12 | boss_pe_2 `pre_registered_constants` | PFEUTY_H_C_OVER_J = 1.0；TRANSVERSE_TOLERANCE_STRICT = 0.05；LOOSE = 0.15；D_FIX2_PASS_LT = 0.05；D_FIX2_FAIL_GE = 0.15 | V3 既有字面 |
| TH-V3R-26 | p_j 自定义 | convergence_rate 形式（无预注册阈值，由 K-V3R-26 重定义） | 沿 §1.2 (a) |
| TH-V3R-27 | p_l 自定义 | ν, η grid（无 V3 预注册，由 K-V3R-27 跨 N 扫描） | 沿 §1.2 (a) |
| TH-V3R-28 | p_m 自定义 | attack_budget 扫描 + safety_budget_lower_bound = 80 | V3 既有字面（安全下界） |
| TH-V3R-0-common-a | K-V3R-0-A 防退化门 | n_distinct > 3 + std > 0 | 本件新冻结 |
| TH-V3R-0-common-b | K-V3R-0-C 双口径 | 重构造 verdict + 沿原 V3 阈值字面 verdict 并报 | 本件新冻结 |
| TH-V3R-0-common-c | K-V3R-0-F 锚链 fallback | `_archive_deposon_2026_09_17/verifier/audit/conservation.py` | E-15 B 路径 |

> **新阈值提案（明示留 PI 拍板）**：
>
> - K-V3R-26 「convergence_rate 重定义」属 worker 落地时新设，沿 §1.2 (a) 形式 —— **本预登记对此为占位，待 PI 复核生效拍板形式后冻结**
> - K-V3R-27 「跨 N = 20/40/60/80/120 cells 扫描」属 §1.2 (a) 形式 —— **同上占位，待 PI 复核生效拍板 N 数列**
> - K-V3R-28 「真 attack 算子三类型」属 §1.2 (a)(b) 形式 —— **同上占位，待 PI 复核生效拍板算子集**
>
> 上述三处如未拍板，worker 沿 §1.2 (a) 最小构造（不引入新阈值）跑 ——「占位」与「最小」双口径并报

---

## §3 执行分批建议（构造难度分层 + 产物链命名）

### §3.1 难度分层（由低到高）

- **第一梯队（本地机械易跑、矩阵成熟）**：
  - **#26 P-J** —— convergence_rate 重定义 + ±0.05 抖动，纯数据复算，0 新素材依赖；预计 1 worker × 单日即可
  - **#28 P-M attack surface** —— budget 扫描加 1/2/3/4 真边界 + 真 attack 算子三类型，沿 5 锚真值（E-15 B 路径 fallback）算 detection；预计 1 worker × 单日
  - **#8 BOSS-PC-3** —— clip_r2_min 扫描 + 真 N 范围 + bootstrap，沿 deposon_v3_physical_opt_60cells_2026_09_11.json 真数据；预计 1 worker × 单日
- **第二梯队（需轻度改造 / 局部重算）**：
  - **#27 P-L P-C FSS** —— 跨 N scaling + bootstrap CI；需重采 20/40/80/120 cells（沿 deposon_v3_physical_opt 真数据 + 真 9 model 嵌入计算）；预计 1 worker × 1-2 日
  - **#10 P-C exp_3_3** —— model 维 variation + 真 η 物理意义；可延用既有 v3x_experiments JSON 框架；预计 1 worker × 2 日
- **第三梯队（需真物理/博弈重新参数 + 锚链 fallback）**：
  - **#1 BOSS-P-A1** —— 真 `simulate_rm` + 真 `bayesian_nash_iter`，v20 baselines 真缺件需 fallback（沿 stored seed=210021 22 graphs）；预计 1 worker × 3-5 日
  - **#4 BOSS-P-A3** —— 真 ESS 邻域检验 ε 三档 + ess_freq 起频扫描；预计 1 worker × 2-3 日
  - **#12 BOSS-PE-2** —— 真 h_c(T) 抽样 + 真 phase boundary + 主判据换 D_fix2；预计 1 worker × 3-5 日（需 D-Eq 解或数值 phase 图）
- **第四梯队（结构性恒等 / 非恒等审计面，难度高）**：
  - **#5 540 cells 守恒审计** —— per-cell pairwise + bootstrap CI 跨真实扰动；理论构造难；预计 1 worker × 5-7 日（含 E-15 B 路径 fallback 验证）

### §3.2 产物链命名（每条 = 预登记子节 → executor → result → 改判登记）

```
results/_v3_recheck_prereg_v1_2026_09_27.md（**本件** · 预登记首件）
  ↓（本件签发后须 PI 复核生效）
results/_v3_recheck_NN_executor_<YYYY_MM_DD>.py（每条 worker 落盘的执行器，仅 1 件每条）
results/_v3_recheck_NN_result_<YYYY_MM_DD>.json（每条 worker 产出的数据，沿 K-V3R-0-D 不合并）
results/_v3_recheck_NN_rescript_<YYYY_MM_DD>.md（每条改判件 = 沿 K-V3R-0-C 双口径裁决，与原 V3 标注并列）
  ↓（按需）
docs/V3X/_erratum_2026_09_27_E41X.md（每条改判件入勘误链 E-41.x 系）
```

> **执行棒守则**：
> - 9 条执行棒只准按 §2.2 kill-line 字面 + §1.2 补审构造方向跑，0 私设条款（K-V3R-0-G）
> - 每条 executor 落盘前先做 K-V3R-0-A 防退化门自证（n_distinct > 3 + std > 0），任意不达 = 退化警报，改构造或判「不明」不许带病开跑
> - 每条 result 须落 K-V3R-0-C 双口径并报字段：`new_verdict`（沿新构造 verdict）+ `legacy_verdict`（沿原 V3 阈值字面 verdict）+ `一致性`（PASS / 不一致）+ `construct_degen_self_check`（K-V3R-0-A 自证字段）
> - 派生 JSON 不合并（K-V3R-0-D），rescript 不动 V3 原报告

### §3.3 派工逻辑（按本件 K-V3R-0-G 沿用规则）

- **第一梯队**（#8, #26, #28）：预计 1 周内可出 executor + result + rescript 三件套；建议先派
- **第二梯队**（#10, #27）：预计 2 周内；与第一梯队并行可开
- **第三梯队**（#1, #4, #12）：预计 2-4 周；可与前梯队部分并行，但 v20 baselines 真缺件 fallback 须先锁一次
- **第四梯队**（#5）：预计 1 周以上；非恒等审计面构造需 PI 复核拍板后开跑

---

## §4 改判登记规则（沿 D5-Q2 PI 拍板口径「内参可直接改，已扩散则不得不A」）

- **V3 原报告 byte 0 触动**：本预登记生效后，所有补审结果**不直接改写 V3 19 份 REPORT 正文**（已 frozen） + 16 项 frozen + P-G v0/v01 + verifier 内置脚本 + 18 frozen + 9 网格 —— 「不动」沿 §5 边界
- **改判件与原标注并列**：每条 rescript `_v3_recheck_NN_rescript_*.md` 与原 V3 标注（Trae 回函 §1.2 #N + V3 review §2 第 N 行）**并列**写入勘误链 **E-41.x 系**（沿既有 E-1…E-16 链追加，0 覆盖原条目）
- **「不得不 A」原则**：V3 报告已扩散（含 V7 综合报告、V3X 1 周判死报告、D5_DANG_DECISIONS、D6_PAPER_*、D7_ONE_PAGE_SUMMARY 等），故新增改判件 = 广而告之，但不回改原报告 —— 这是「diffusion vs 内部可改」的边界
- **改判件最小内容字段**：
  - 原 V3 标注（Trae §1.2 #N 字面）
  - 补审构造（沿 §1.2 / §2.2 字面）
  - 补审 result（含 K-V3R-0-C 双口径字段）
  - 改判动作（沿 §2.3 改判规则表）
  - kill-line 触发状态（哪几条 K-V3R-N 触发 / 哪几条不触发）
  - γ 标（沿 §2.3 「不明」分支需要时）
  - PI 复核栏（待 PI 签字生效即锁）

---

## §5 边界声明 + 老实交代段

### §5.1 边界声明（沿 V3 既有派工 §5 + V4 铁律边界）

- **不动**：18 frozen（在盘 16 项） / 9 网格 / P-G v0+v01 / plugin spec / verifier 内置脚本（`_verify_15frozen*.py`）/ V4 `_v4_*` 全链 / 已冻结 V3 报告正文（19 REPORT）—— **均已核查，0 字节改动**
- **不改**：任何 V3 实验结论与判定本体；本预登记的「假成立 / 假证伪 / 结构性恒等」标注是**对结论-证据关系的再分类**，不重裁命题存亡；改判件 = 显式登记 + 改判动作，**不构成翻案**
- **派生 JSON 不合并**（K-V3R-0-D）：补审 result 落新名 `_v3_recheck_NN_result_*.json`，不并入既有 _p_* / boss_*
- **不引**：无任何无法核实的外部专有名词 / 文献号 / 法条号；Smith 1973 / Taylor & Nowak 2006 / Hart & Mas-Colell 2000 / Pfeuty 1D Ising / Jordan-Sucher-Votek 1999 / Needleman & Wunsch 1970 沿 V3 既引
- **密钥**：本件 + 后续补审件 0 明文密钥；`_v3_recheck_NN_*` key 形态自扫同 V3 既有
- **仓外件**：`deposon-sub/`（363 件）与 `_archive_deposon_2026_09_17/` 仅**读取以核 SHA 与 fallback**，未写入、未移出、未删除
- **新增件**：`results/_v3_recheck_prereg_v1_2026_09_27.md`（本件）+ 后续 executor / result / rescript；新增件不为覆盖既有任何文件

### §5.2 老实交代段（沿 V3 补实验判决 §6 + PI CoT v3 prereg §9 格式）

#### §5.2.1 输入件核验老交代

- 派工单 SHA 字面 `B7547329AF2E` 与盘上 `_v4_pi_cot_v3_prereg.md` 实测 `1A90FD8F385A` **不符**，已在 §0.1 显式登记，未代为修订派工单
- 21 件输入链（§0.1 + §0.2）全部只读核验，0 触动 byte；frozen 件沿 §5「不动」边界一律只读
- `_v3_calibration_change_note_for_coze_glm_2026_09_27.md` §1.8「同族假象」表已列 9 条假象类降级引用规则 —— 与本件 §1.2 类型归类一致，本预登记不重复定义

#### §5.2.2 派生关系与不编造声明

- 本件由 0-A `24EAFC05A217` + 0-B `9421E78B7E3C` + 0-C `1A90FD8F385A` 三件核验 + §0.2 16 件只读核验 + 派工单「9 条逐条」字面 + PI 2026-09-27 问卷 ask_0ec0da85 字面 Q1+Q2 推导生成
- 不编造外部专有名词 / 文献号 / 定理名 —— 上述 Smith 1973 / Taylor & Nowak 2006 / Hart & Mas-Colell 2000 / Pfeuty 1D Ising / Jordan-Sucher-Votek 1999 沿 V3 JSON `reference` / `spec_source` 字面，不另引
- 不编造观测数字 —— 9 条每一字段（`rm_iter=6` etc）均沿 §0.2 测得 SHA-12 实算对应 JSON 字面；本预登记为预登记件，0 观测值
- 不编造 kill-line 阈值 —— §2.4 TH-* 全部沿 V3 既有字面（pre_registered_threshold.*，pre_registered_constants.*）；新冻结仅 K-V3R-0-A 防退化门 + K-V3R-0-C 双口径 + K-V3R-0-F 锚链 fallback 三个 + K-V3R-26/27/28 占位留 PI 拍板

#### §5.2.3 succeeded ≠ 跑完

- 本件为预登记件（设计 + 立线），不触发实验跑前生效（生效须 PI 复核）
- 产物链首件（§3.2），落盘 SHA-12 核验后才可宣告完成 —— SHA-12 见文末最终汇报核验值

#### §5.2.4 skill 加载与 fallback 老交代

- 派工单指定 skill = `scientific-research-workflows:experimental-design`（plugin `@scientific-research-workflows`）
- 本 agent（protocol-keeper）执行时未加载该 skill（**Local skill not found** 或加载失败）
- fallback 锚 = `results/_v4_pi_cot_v3_prereg.md`（SHA-12 `1A90FD8F385A`，§0.1 实测）结构字面：§1 学习目标结构 / §2 claim / §4 kill-line / §5 TH 阈值 / §8 产物链 / §9 老实交代
- 本件 v1 结构沿用上述 fallback 锚 9 节 + 扩展至 5 节（§0 输入件核验 + §1 9 条清单表 + §2 判死线 + §3 执行分批 + §4 改判登记规则）+ §5 边界声明 + 老交代段
- 不编造 skill 不存在的虚构指令

#### §5.2.5 不可判项 / 未读完项 / 待 PI 复核项（poka-yoke 显式）

**A. 不可判项**：

1. **#5 540 cells 守恒审计非恒等审计面构造可行性**：per-cell pairwise + bootstrap CI 跨真实扰动属非平凡新构造，理论可行性已勘察，**未实跑过**；构造落地可能有 K-V3R-0-A 自证通不过的风险（不动点仍是构造恒等），需要 PI 拍板构造方向

**B. 未读完项**：

1. `deposon-sub/` 363 件 manifest：未逐件走读（本任务范围外）—— 但**对本预登记生效无影响**，因 9 条补审构造均沿 repo + `_archive_deposon_2026_09_17` 主路径与 fallback 路径，已在 §0.2 全列
2. **boss_pa_2_potential_game.py**（V3 review §1.2 #3 不可判，本预登记不在范围）未触及

**C. 待 PI 复核项**（poka-yoke 显式，本件生效前必须拍板的）：

1. **§2.4 新阈值提案三处**（K-V3R-26/27/28 占位）—— worker 跑前 PI 拍板形式后冻结
2. **§3.1 执行分批**派工时序（PI 拍板先后顺序）
3. **§3.2 产物链**是否入勘误链 **E-41.x 系** 命名规范（沿既有 E-1…E-16 链追加）
4. **E-15 锚链断裂**是否连带要求本件 #5 / #12 沿 B 路径 fallback 重测（PI 拍板 E-15 处理路线）
5. **本预登记生效即锁后** worker 开跑前的 9 条 executor / result / rescript 三件套 × 9 = 27 件派生件的派工时序

#### §5.2.6 0 触动声明

我声明：本次预登记起草对**任何既有文件 0 字节改动**——19 REPORT、16 项在盘 frozen、repo 内现有 runner / JSON / results、仓外件、V4 全链 —— **无一被写**。唯新生成本件 1 件。可由 §0.1 + §0.2 全 SHA-12 核验跨证（21 件实测 = 21 件派工单字面或新增 SHA-12 基线）。

#### §5.2.7 一句话总纲

V3 假象类 9 条（假成立 3 + 假证伪 5 + 结构性恒等 1）覆盖 P-A / P-C / P-E / P-J / P-L / P-M 全方向；本预登记**只冻结判死线 + 补审构造方向 + 改判规则**，不动 V3 报告 byte；落盘 9 条 executor × 9 条 result × 9 条 rescript = 27 件派生件不合并 + 沿 E-41.x 勘误链登记，**改判结果由 PI 复核生效拍板**。

---

## 文末产物核验（诞生即报）

> ⚠ 本字段为避免「回填 SHA → 文件变 → 哈希变 → 再回填」无限循环的稳定方案——SHA-12 前 12 与字节数**不在文件内自记**，统一在最终汇报中核验报出。

- 路径：`results/_v3_recheck_prereg_v1_2026_09_27.md`
- SHA-12 前 12：**见最终汇报核验值**
- 字节数：**见最终汇报核验值**
- 派生关系：21 件输入 SHA-12（§0.1 + §0.2）+ 派工单「9 条逐条」字面 + PI 2026-09-27 问卷 ask_0ec0da85 Q1+Q2 + fallback 锚 `_v4_pi_cot_v3_prereg.md`（`1A90FD8F385A`）结构字面 6 节；本件为新件新名，**不覆盖**任何既有件
- 产物链首件（§3.2），不重写

---

出件｜Mavis 团队 protocol-keeper（`agent-3e0c193da529`）｜2026-09-27
