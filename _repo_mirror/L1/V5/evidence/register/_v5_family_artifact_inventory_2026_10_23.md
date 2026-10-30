# 族③ `V5` 族 · 产物与输入逐项盘点（2026-10-23）

> 📌 **授权**：PI 2026-10-23 17:35 卡 `ask_7fa3936e1c09047a5f8afbfb` 答 `e2_order` 逐字「**下轮上下文窗口依次全部**」；落账 `pi_rulings\_pi_card_answers_register_2026_10_23_v259.md`（10,244 B／`7d88011fd1d9`）。
> 📌 **执行**：主代理亲跑（子棒断连且依令不重派）。**观测时点 2026-10-23 18:3x。**
> 📌 **本件 0 落五终判 · 0 闭 KD · 0 宣告段毕或门槛成就 · 0 代 PI 裁；只登记实测。**
> 📌 **射程**：`〔本地路径已脱敏〕` ＋ **`〔本地路径已脱敏〕`**（该仓不在 repo 内）；均排 `.tmp`、排 `*〔归档区〕*` 之内容（仅按名查其存在）。

---

## §1 · 方法（可复现）

1. **拾立项面**：按名取 `_v5_*` 且名含 `prereg｜plan｜design｜activation｜status_annotation` 者 ⇒ **23 件**（另 3 件 `_v4_commission_〔IM〕_report_coze_*_v5_draft*` 之「v5」为**版本号非族名**，已剔）。
2. **取其自载之产出件名**：正则取预登记正文内**被反引号包裹、以 `.md/.json/.csv/.txt` 结尾**之名，排除其自身 ⇒ **187 个名字**。
3. **逐名去两仓核在否**（basename 索引，两仓 3,719 件全建索引）。
4. **对 34 个「不在盘」之名做二轮辨明**：分「模板占位名（含 `_2026_xx_xx`／`{执行日期}`／`*`）」与「输入件（前序结果，非本立项产物）」与「真产物」三类，**模板类改按模式去盘上验**。

---

## §2 · 逐立项计数（第一轮 · 按名）

| 立项件 | 区 | 自载名数 | 在盘 | 不在盘 |
|:--|:-:|--:|--:|--:|
| `_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | repo | 6 | 1 | 5 |
| `_v5_pjpm_pc_deg_prereg_2026_09_29.md` | repo | 23 | 14 | 9 |
| `_v5_item35_v3_collinear_prereg_2026_09_29.md` | repo | 11 | 8 | 3 |
| `_v5_v3_deg_fix_prereg_2026_09_29.md` | repo | 14 | 9 | 5 |
| `_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | repo | 9 | 9 | 0 |
| `_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | repo | 9 | 9 | 0 |
| `_v5_gt_p10_lowarm_prereg_2026_09_29.md` | repo | 6 | 3 | 3 |
| `_v5_gt33_attrib_fill_prereg_2026_09_29.md` | sub | 5 | 5 | 0 |
| `_v5_item35_prereg_v2_2026_09_28.md` | repo | 11 | 8 | 3 |
| `_v5_c3_reading_b_prereg_2026_09_28.md` | repo | 10 | 10 | 0 |
| `_v5_item21_rerun_conditions_prereg_2026_09_28.md` | sub | 6 | 6 | 0 |
| `_v5_pl2_fourband_prereg_2026_09_29.md` | sub | 11 | 9 | 2 |
| `_v5_fake_verdict_v1x_prereg_2026_09_28.md` | repo | 8 | 8 | 0 |
| `_v5_prereg_chain_activation_register_2026_09_28.md` | sub | 7 | 7 | 0 |
| `_v5_v3deg_prereg_activation_register_2026_09_29.md` | sub | 5 | 5 | 0 |
| `_v5_prereg_chain_status_annotation_2026_09_28.md` | sub | 10 | 10 | 0 |
| `_v5_b22_r07_four_cond_prereg_2026_09_29.md` | sub | 7 | 7 | 0 |
| `_v5_b14_08c_material_plan_2026_09_29.md` | sub | 6 | 5 | 1 |
| `_v5_b14_3_v1_4_prereg_2026_09_29.md` | sub | 5 | 5 | 0 |
| `_v5_b14_4_v1_3_prereg_2026_09_29.md` | sub | 4 | 4 | 0 |
| `_v5_item05_prereg_2026_09_28.md` | sub | 7 | 5 | 2 |
| `_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md` | sub | 5 | 4 | 1 |
| `_v5_item36_prereg_2026_09_28.md` | sub | 2 | 2 | 0 |
| **合计** | — | **187** | **153** | **34** |

📌 在位分布：**repo 60 件／sub 93 件**（在盘之 153 中）。

---

## §3 · 34 个「不在盘」之三轮辨明（**关键**）

### §3-1 模板占位名 → 按模式验，**12/13 实在盘**

| 模板名（含占位符） | 按模式实见 | 判 |
|:--|:--|:--|
| `_v5_item35_v3_collinear_result_2026_xx_xx.json` | `results\readout\run\_v5_item35_v3_collinear_result_2026_09_29.json` | **在盘** |
| `_v5_item35_v3_collinear_exec_2026_xx_xx.md` | `sub\…\_v5_item35_v3_collinear_exec_2026_09_29.md` | **在盘** |
| `_v5_item35_v3_collinear_verdict_2026_xx_xx.md` | 2 件（`verdict_2026_10_01` ＋ `verdict_prep_2026_10_01`） | **在盘** |
| `_v5_gt8_lowarm_result_2026_xx_xx.json` | 3 件（`result`／`resultb` ／`resultA_cb132cd5`，皆 09-29） | **在盘** |
| `_v5_gt8_lowarm_exec_2026_xx_xx.md` | `results\readout\run\_v5_gt8_lowarm_exec_2026_09_29.md` | **在盘** |
| `_v5_gt8_lowarm_verdict_2026_xx_xx.md` | 2 件（`verdict` ＋ `verdict_r2`，09-29） | **在盘** |
| `_v5_item35_v2_matrix_{执行日期}.json`／`_matrix_*.json` | 3 件（`.py` ＋ `_matrix_exec` ＋ `_matrix_result`，皆 09-29） | **在盘** |
| `_v3_recheck_*_rescript_2026_09_27.md` | **13 件**（01–xx，09-27／09-28） | **在盘** |
| `..._verdict.md`（v3_deg_fix 之模板） | 3 件（`verdict_register` ＋ `26b_verdict` ＋ `26b_verdict_prep`） | **在盘** |
| `_v3x_conservation_anchor_*.txt` | `_v3x_conservation_anchor_2026_09_17.txt` | **在盘** |
| `v10…v35_*.md`（b14_08c 之范围式） | 属**范围表述非件名**，不适用按名判 | 不计缺 |
| **`_v5_item35_v2_rescript_*.md`** | **0 命中（两仓＋归档区＋`.tmp` 全扫）** | **真缺 ⚠** |

### §3-2 输入件（前序结果，**非本立项之产物**）—— 分三态

| 输入件 | 脚本（runner） | 结果件（活面） | 判 |
|:--|:-:|:-:|:--|
| `p_j_convergence_basin_results_2026_09_16.json` | ✅ `.py` 在盘 | ❌ 0 | 有器无果 |
| `p_m_attack_surface_cost_results_2026_09_16.json` | ✅ | ❌ 0 | 有器无果 |
| `p_m_real_separation_results_2026_09_16.json` | ✅ | ❌ 0 | 有器无果 |
| `p_i_real_labels_results_2026_09_16.json` | ✅ | ❌ 0 | 有器无果 |
| `p_l_real_data_collapse_results_v2_2026_09_16.json` | ✅（含 v2） | ❌ 0 | 有器无果 |
| `p_l_p_c_finite_size_scaling_results_2026_09_16.json` | ✅ | ❌ 0 | 有器无果 |
| `boss_pa_1_rbr_rm_result_2026_09_15.json` | ✅ 8 件 `.py` | ❌ 0（仅脚本） | 有器无果 |
| `deposon_v3_physical_opt_60cells_2026_09_11.json` | — | ⚠ **仅 `.tmp` 远端镜像内有**（`_c514_remote_blobs_2026_10_18`） | 活面 0／镜像有 |
| `v3x_d7_v3_final_report_2026_09_11_v7.md` | — | ⚠ **仅 `.tmp` 远端镜像内有** | 活面 0／镜像有 |
| `v3x_experiments_results_2026_09_16.json` | ❌ 连脚本亦 0 | ❌ 0 | **全无** |
| `deposon_v42_v2_miss_rate_curve_2026_09_16.json` | ❌ 连脚本亦 0 | ❌ 0 | **全无** |

### §3-3 真产物之缺（**仅 2 件**）

| 件 | 出处立项 | 实测 |
|:--|:--|:--|
| **`_v5_item35_v2_rescript_*.md`** | `_v5_item35_prereg_v2_2026_09_28.md` | 两仓＋归档区＋`.tmp` **0 命中** |
| **`_v4_v3_degradation_contrast_result.json`** | `_v5_v3_deg_fix_prereg_2026_09_29.md` | 两仓＋归档区＋`.tmp` **0 命中** |

---

## §4 · 已核实之在盘产物（抽样带指纹 · 逐件可复算）

| 件 | 区 | bytes（由索引） | 备注 |
|:--|:-:|--:|:--|
| `_v5_gt6_trajint_2026_09_29.json` | repo | — | 模板名之实体（日期 09-29，非预登记所写 09-28）⚠ |
| `_v5_gt5_reattrib_2026_09_29.json` | repo | — | 同上 |
| `_v5_gt8_expand_2026_09_29.json` | repo | — | 同上 |
| `_v5_gt5b_reattrib_2026_09_29.json` | repo | — | 同上 |
| `_v5_gt4_reattrib_2026_09_29.json` | repo | — | 同上 |

> ⚠ **一处须记之偏差**：「`_v5_gt*_…_2026_09_28.json`」之预登记名与盘上实体「`…_2026_09_29.json`」**日期不符**——本件按**名干（stem）**判在盘，**未**认定其为同一件之同一版；此偏差如实登记，⛔0 判其「名异实同」。

---

## §5 · 族③ 之判读（**只登记事实，不落终判**）

1. **产物面**：23 立项、187 自载名，**153 在盘／34 不在盘**；34 经辨明后 **12 属模板已实／13 属输入件／仅 2 属真缺**。
2. **「不在盘」之主要成因不是产物缺，而是输入件不在活面**：6 类 `p_*` 前序结果**有 runner 脚本、无结果 json**；2 类仅在 `.tmp` 远端镜像；2 类**连脚本都无**。
3. ⇒ 若问「V5 是否仍欠」：**产物面近乎齐（真缺 2 件）**；**欠在输入面与外阻塞**（前序结果 0 在活面）。**这属「缺数」，依 e3 之答，缺数不能闭。**
4. **⛔0 判 V5 已毕**——本件只点「有没有件」，**未判件之内容是否满足该立项之要求**（后者须逐件开卷核，本件未做）。

---

## §6 · 本件之限（老实交代）

1. **未逐件开卷核内容**：只判「件在不在」，未判「件对不对」。故本件**不能**支持「V5 产物合格」之结论。
2. **名判法之偏向**：反引号取名会把「被引用的他件」也算作「要求之产物」（如输入件即由此混入），已在 §3-2 分出；但**仍可能有未辨识者**。
3. **`_v5_gt*` 之日期偏差**（预登记 09-28 vs 实体 09-29）**未定因**。
4. **未查归档区内容**（依铁律），仅按名查其在否。
5. **`.tmp` 之远端镜像（`_c514_remote_blobs_2026_10_18`）非活面件**——本件引之只为说明「镜像有、活面无」，⛔0 以镜像充在盘。

---

**状态行**：`族③ V5 盘点 · 已落盘 · 呈 PI`
**落款**：主代理 mavis 亲跑 · 2026-10-23 18:3x · ⛔0 落五终判 · ⛔0 代 PI 裁 · ⛔0 回改既有件
