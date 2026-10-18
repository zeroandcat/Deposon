# V3-R 补审改判件 #8 · BOSS-PC-3（A3 N 范围裁剪）（rescript）

> **性质**：V3 假象类补审改判件（9 条系列之第 8 条）；**V3 原报告 byte 0 触动**，本件与原标注**并列**登记
> **依据**：`results/_v3_recheck_prereg_v1_2026_09_27.md`（实测 SHA-12 `88052d7db895`，37,346 B）§1.2 #8 / §2.2 K-V3R-8 / §2.3 改判规则表 / §3.2 执行棒守则 / §4 改判登记规则
> **A3 语义锚**：`docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` §5 字面 —— 「A3：N 范围裁剪：去掉 N=10 和 N=1000 两端，看 R² 是否仍 > 0.7（"幂律非端点驱动"）」；R² 沿同 spec §3.3 + §4.1 幂律 OLS 字面
> **配套三件套**：executor `results/_v3_recheck_08_executor_2026_09_27.py` ｜ result `results/_v3_recheck_08_result_2026_09_27.json` ｜ 本 rescript
> **勘误链位**：E-41.x 系（沿既有 E-1…E-16 链追加，0 覆盖原条目）
> **PI 复核栏**：待 PI 签字生效即锁

---

## 1. 原 V3 标注（沿 Trae v3 回函 §1.2 #8 字面 + boss_pc_3 JSON 字面）

| 项 | 字面 |
|---|---|
| 对象 | BOSS-PC-3 · Attack A3 — N 范围裁剪 |
| 原结论 | **FAIL**（`worst_clipped_r2 = 0.3362 < clip_r2_min = 0.7`） |
| 死因（预登记 §1.2 #8 字面） | 3 trial `r2_delta_full_minus_clipped ≡ 0.0`（full r2 = clipped r2 逐 trial 一致）→ clipping 为 no-op |
| 类型 | **假证伪**（Trae 回函 §1.2 #8） |
| 盘上实测复核 | 3/3 trial `r2_delta_full_minus_clipped == 0.0`；`r2_full_N7` = [0.6197, 0.3362, 0.5444]；`r2_clipped_N5` 逐 trial 逐字相同；`pre_registered_threshold` = {clip_r2_min 0.7, n_full 7 档, n_clipped 5 档}；`data_source` = `deposon_v3_physical_opt_60cells_2026_09_11.json` |
| 旁证（Trae 回函 L225） | 「未见 P-C 规范对此的预注册定义，故标假证伪而非『构造无效』」——**本 worker 实测后此保留意见已可结清，见 §3.1** |

## 2. 素材面探测（判定的决定性环节 —— 本条与另两条不同，**卡在这里**）

K-V3R-8 要求在冻结的 N 阶梯上算 `r2_delta_full_minus_clipped`。实测盘上素材：

| 探测项 | 实测结果 |
|---|---|
| 原 JSON 自报 `data_source` | `deposon_v3_physical_opt_60cells_2026_09_11.json` |
| 该源是否含任何 N 阶梯字段 | **否**（`declared_data_source_has_N_ladder_field = false`） |
| 冻结阶梯需要的 N（TH-V3R-8） | `[10, 20, 50, 100, 200, 500, 1000]`（7 档） |
| 盘上可提供的真实 (N, P) 幂律观测对 | **0 对**（`N_levels_coverable = []`，`n_distinct_real_N_levels = 0`） |
| 该源真实可提供的量级 | **cell 计数** {30, 60, 540}（每 model 30/60 cells，合计 540 cells） |
| 为何不顶替 | cell 计数的语义是「分类 cell 数」，**不是** spec §3.1 的「图族规模」；顶替即等于**擅调 TH-V3R-8 阈值**，违 K-V3R-0-B |
| 原始 A3 执行器 | `attack_pc_a3_clipping.py` —— 3 个候选路径**均不在盘**（`docs/V3X/REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` L131 记其存在并 PASS） |
| P-C V0 真实扫描产物 | `results/v3x_pc_v0/`（spec §7 交付路径）、`docs/V3X/P_C_V0_RESULTS_2026_09_09_mavis.md`、`tools/scaling_probe.py`（spec §2 锚）—— **均不在盘** |
| 已查并否决的替代源 | `results/deposon_benchmark_v1_4_gsm8k_details.json`（含 N 键 {10,20,50,100}，但非 P-C 命中率/失真率序列，且缺 3 档）；`results/deposon_gsm8k_stratified.json §per_question_steps`（N 键为步数分布，非 P(N) 幂律观测，缺 3 档） |

**K-V3R-0-A 退化门**：`n_distinct_real_N_levels = 0 ≤ 3` → **`degenerate_alarm_hit = true`**。按预登记 §3.2 执行棒守则「任意不达 = 退化警报，**改构造或判「不明」，不许带病开跑**」→ **本条判「不明」**，K-V3R-8 判死线**不可判**（既非 PASS 亦非 FAIL）。

## 3. 补审 result（K-V3R-0-C 双口径）

### 3.1 溯源缺口（provenance gap）—— 本条最硬的发现

| 项 | 内容 |
|---|---|
| 事实 | 原 JSON 自报 `data_source`（60cells 件）**不含任何 N 阶梯字段** |
| 推论 | 原 `r2_full_N7` / `r2_clipped_N5` 数值（0.6197 / 0.3362 / 0.5444）**无法从其自报数据源复算** |
| 叠加事实 | 原始 A3 执行器 `attack_pc_a3_clipping.py` 不在盘，无法逐行复核其计算 |
| 结论 | 原 BOSS-PC-3 的 3 个 R² 数值**溯源链断裂**；在补审拿到真实 P(N) 序列前，任何「delta ≡ 0 是 no-op」的论断都**缺可复算基础** |
| 对 Trae 保留意见的结清 | Trae L225 曾称「未见预注册定义，故标假证伪而非构造无效」。本 worker 实测后：spec §5 A3 **确有**冻结语义（去 N=10 / N=1000 两端），但**冻结语义与原执行器/原数据源之间无桥接件** —— 故 Trae 的保留意见**方向正确、理由需修正**（不是「规范未定义」，而是「规范已定义但执行器与数据源缺件」） |

### 3.2 构造自检（synthetic fixture，**仅验证执行器非退化，不作判定证据**）

> 全部字段带 `SYNTHETIC_CONSTRUCTION_SELF_TEST` 标签。夹具 = `P(N) = 2.0·N^(−0.45) + 0.02` × 乘性高斯噪声（σ = 0.05，seeded）。**这不是观测数据，不参与 K-V3R-8 判定。**

| trial seed | r2_full（7 档） | r2_clipped（5 档） | **delta** | delta == 0？ |
|---|---|---|---|---|
| 42 | 0.992779 | 0.989944 | **+0.002836** | 否 |
| 137 | 0.998349 | 0.999458 | **−0.001108** | 否 |
| 256 | 0.989587 | 0.986800 | **+0.002787** | 否 |

- `executor_non_degenerate = true`（3/3 格 delta ≠ 0）→ 执行器**能分辨**去端点前后的 R² 差异
- **V3 缺陷复现（no-op emulation）**：把 clipped 阶梯错算成 full 阶梯（复现 V3 的 no-op 形态）→ 3/3 格 delta = **0.0**（`no_op_emulation_reproduces_zero_delta = true`）
- **由此可结清的机制问题**：`delta ≡ 0.0` **不是幂律的性质，而是「用同一阶梯算两遍」的构造缺陷**。V3 的 3/3 delta ≡ 0.0 与此 no-op 形态**完全一致**（但因原执行器缺件，此为机制层面的**相容性证明**，非对原脚本的逐行归因）
- bootstrap（n = 1000，seed = 42，**synthetic**）：delta 均值 = −0.003512，std = 0.003278，95% CI = [−0.011706, +0.000705]，`fraction_of_resamples_with_delta_zero = 0.0`

### 3.3 双口径判定

| 口径 | verdict | 依据 |
|---|---|---|
| **新构造 verdict** | **不明**（`kill_line_decidable = false`） | K-V3R-0-A 退化警报：真实 N 档 n_distinct = **0** ≤ 3，素材面不足，按 §3.2 不许带病开跑 → 判死线**不可判** |
| **沿原 V3 阈值字面 verdict** | **FAIL**（`worst_clipped_r2 = 0.3362 < clip_r2_min = 0.7`；3/3 trial `r2_delta_full_minus_clipped == 0.0`） | 沿 `pre_registered_threshold` 字面复算，逐字复现 |
| **一致性** | **不一致**（新构造不可判 vs 原口径 FAIL） | — |
| γ 标 | γ = **素材面不足**：真实 P(N) 7 档序列与原始 A3 执行器**双缺件**；且原 R² 数值溯源链断裂（无法从自报 data_source 复算） |

### 3.4 K-V3R-8 触发状态

| 判据 | 状态 |
|---|---|
| `delta` 至少一档 ≠ 0.0 | **不可判**（无真实 P(N) 序列；synthetic 自检虽 3/3 ≠ 0，但不作证据） |
| 3 trial 仍 ≡ 0 → FAIL | **不适用**（走 §3.2 退化门 → 判「不明」，不落 FAIL 档） |
| `kill_line_hit`（触发 FAIL / 警报） | **true**（退化警报触发） |
| `kill_line_pass` | **false**（未开跑，无 PASS 可言） |

## 4. 改判动作（沿预登记 §2.3 改判规则表 + §4）

| 项 | 结论 |
|---|---|
| 命中档位 | **§2.3 第 4 行：不明**（构造素材面不足） |
| 改判动作 | **维持原 V3 标注（不动）** + **显式登记 γ**；归「V4 收尾整理」待拍板桶 |
| γ 标 | γ = 素材面不足 + 原 R² 数值溯源链断裂（详见 §3.1 / §3.3） |
| V3 原报告 | **byte 0 触动**（boss_pc_3 JSON 与 spec 均未写） |
| 是否翻案 | **否** |
| 桶位 | 「V4 收尾整理」待拍板桶（沿 PI 2026-09-27 不可判项统一处置口径） |
| 解除条件（交 PI 拍板） | 补齐任一即可解锁 K-V3R-8：① P-C V0 真实 7 档 P(N) 扫描结果（`results/v3x_pc_v0/` 或 `P_C_V0_RESULTS_*.md`）；或 ② 原始 `attack_pc_a3_clipping.py` 执行器（可据其锁定 r2 的可复算口径）；或 ③ PI 另行拍板以 cell 计数档 {30,60,540} 顶替 N 阶梯（**属新阈值提案，违 K-V3R-0-B，须显式拍板**） |

## 5. 老实交代段

1. **输入链 SHA 口径不符（如实登记，不代为修订预登记）**：预登记 §0.2 记 #8 BOSS-PC-3 JSON 实测 SHA-12 = `717C26DF5A00`，本 worker 按 `hashlib.sha256(bytes).hexdigest()[:12]` 实测 = **`d74d6b39d1b0`**（字节数 1,265 与预登记**逐字一致**）。同口径下预登记 §0.2 表内 **12/12 件全部不符**，系统性差异指向哈希输入约定不同或转写前移，**非内容变更**。**内容侧已逐字复核**：预登记 §0.2 对 #8 的描述（3/3 delta == 0.0、clipping 为 no-op）与盘上 JSON **逐字吻合**。未修改预登记任何 byte。
2. **构造自检用的 synthetic 夹具不是观测**：`P(N) = 2.0·N^(−0.45) + 0.02` + seeded 噪声，**全部字段带 `SYNTHETIC_CONSTRUCTION_SELF_TEST` 标签**，仅用于证明执行器非退化 + 复现 V3 no-op 形态。**未用于任何判定**；`kill_line_decidable = false`。
3. **本条未跑真判死线**：与 #26 / #28 不同，#8 **没有**产出 PASS 或 FAIL。派工单「#8 clip_r2_min 0.3/0.5/0.7 扫描 + 真 N 范围裁剪 + bootstrap」的**扫描与 bootstrap 机制已实现并自检通过**，但**素材面（真实 P(N) 序列）缺件，故不开真跑**。如实交代：**9 件已落盘，但 #8 是「executor + 不可判判定」，不是「补审完成」**。
4. **0 新设阈值**：`clip_r2_min` 扫描严格按派工单 {0.3, 0.5, 0.7}；`n_full` / `n_clipped` 严格按 `pre_registered_threshold` 字面；bootstrap n = 1000 / seed = 42 沿预登记 §1.2 #5 字面同款。
5. **未编造观测**：0 外部文献号新增；未修改 spec / JSON / 任何既有件。
6. **succeeded ≠ 跑完**：本件以 result JSON 落盘 + hashlib SHA-12 复算为准（见最终汇报核验值）。

---

**PI 复核栏**：☐ 通过（按 §2.3 第 4 行登记生效，γ 入桶）　☐ 打回（补素材后重跑）　签字：__________　日期：__________

出证｜Mavis 团队 worker 出件｜2026-09-27
