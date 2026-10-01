# #26b（`K-V3R-26` literal-gap）· **正式判定件**（三态落档 + 根因三分类） · verdict-keeper · 2026-10-01

> **性质**：判定面材料件 `results/_v3_recheck_26b_verdict_prep_2026_10_01.md`（`3aab3f7660fc` / 36,133 B）之上的**判定面收口件**。
> **本棒身份**：**verdict-keeper**（Mavis 团队 verdict-keeper，agent-3a4d09ba3c90）。**0 代跑**：0 跑实验本体、0 改任何既有件 1 字节、0 合并派生 JSON、0 读 key（R4）、0 擅调任何阈值或判死线字面、0 代 evidence-auditor 审链、0 代 verifier 独立复核、0 代 protocol-keeper 改线、0 代 PI 裁授权事实。
> **铁律自证**：三态落档（PASS / FAIL / KD，0 模糊态措辞）｜0 判死纪律软化（「但/然而/仍有希望/不排除/有待观察」0 使用）｜0 新设数值切点｜0 编造（引件指纹 0 自写入的 22 件全部本人盘上实测）｜派生 JSON 0 合并｜**skill：派工单未指定 ⇒ 本棒 0 加载任何 skill**。
> **纪律自证**：UTF-8 无 BOM · LF；SHA-12 ＝ `sha256(全文)[:12]` 小写、**盘上终态实测**；0 撞名实测后落盘；**本件为唯一新建件**。

---

## §0 输入件 · 盘上实测哈希（本人 `Get-FileHash SHA256` 实测 · 非引派工单字面）

| # | 件 | 盘上路径 | 实测 sha12 | 实测 bytes | 与材料件／派工单字面 |
|---|---|---|---|---|---|
| 1 | 判定面材料件 | `results/_v3_recheck_26b_verdict_prep_2026_10_01.md` | `3aab3f7660fc` | 36,133 | **一致**（派工单字面同值） |
| 2 | ★ **现行执行面 r3** | `results/_v3_recheck_26b_executor_r3_2026_09_29.py` | `6c83e7a7ca2e` | 64,959 | 一致 |
| 3 | ★ **现行读法乙读数** | `results/_v3_recheck_26b_r3_result_2026_09_29.json` | `c9d3c9f819f1` | 54,294 | 一致 |
| 4 | 历史执行面（读法甲） | `results/_v3_recheck_26b_executor_2026_09_27.py` | `5c906113a210` | 43,171 | 一致 |
| 5 | 历史读法甲读数 | `results/_v3_recheck_26b_result_2026_09_27.json` | `49c6e5a07732` | 44,379 | 一致（本人开读，见 §1 双读法） |
| 6 | r2 修订执行面 | `results/_v3_recheck_26b_executor_r2_2026_09_28.py` | `0808af6212c5` | 52,272 | 一致 |
| 7 | ★ **判死线字面锚** | `results/_v3_recheck_prereg_v1_2026_09_27.md` | `88052d7db895` | 37,346 | 一致（本人开读 §2.1） |
| 8 | 读法乙定义件 | `results/_v5_c3_reading_b_prereg_2026_09_28.md` | `8dcf5e1e6dde` | 32,178 | 一致（材料件 §7.1 第 3 项滞后件终态） |
| 9 | ★ **读法乙生效登记件** | `results/_v5_bulk_activation_2026_09_28.md` | `b5a50447b4da` | 39,378 | 一致（材料件 §7.1 第 4 项滞后件终态） |
| 10 | 归属终局表 v1（已失效 · 快照） | `results/_v5_item26b_attribution_effective_2026_09_28.md` | `c353fbcdc753` | 35,261 | 一致 |
| 11 | F2/F1/F3 端点定义件 | `results/_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | `5e59a11466db` | 38,939 | 一致 |
| 12 | ★ **23:01 追认落册件** | `results/_f2_closeout_note_2026_09_29.md` | `1599cb99abf3` | 16,317 | 一致（本人开读 §2.3） |
| 13 | F2 修复棒登记件 | `results/_f2_branch_fix_register_2026_09_29.md` | `a0cab58c032e` | 22,940 | 一致 |
| 14 | #26b rescript | `results/_v3_recheck_26b_rescript_2026_09_27.md` | `ae81d9b59054` | 30,552 | 一致（材料件 §7.1 第 2 项滞后件终态） |
| 15 | #26b 判定登记表 | `results/_v3_recheck_verdict_register_2026_09_27.md` | `d9b6b974cfc1` | 112,085 | 一致（本人开读 §2.4） |
| 16 | 体例参考件 | `results/_v5_item35_v2_verdict_2026_09_29.md` | `b59bef293712` | 26,232 | 体例来源（派工单指定） |

**冻结时序（判别要件①的盘上依据 · mtime 实测）**：`88052d7db895`（prereg v1，09-27 13:33:20）＜ `5c906113a210`（原件 executor，09-27 15:51:38）＜ `49c6e5a07732`（读法甲读数，09-27 15:52:40）＜ `0808af6212c5`（r2，09-28 22:47:39）＜ `6c83e7a7ca2e`（r3，09-29 10:50:41）＜ `c9d3c9f819f1`（读法乙读数，09-29 19:08:57）⇒ **时序层：判死线字面锚早于一切测量 2h18m、早于现行读数 2 天 5h35m**。**⚠ 但时序成立 ≠ 冻结生效**，见 §2.1 语义层判定。

---

## §1 三态落档（三态 · 每行附根因列 · 阈值 0 调整）

| 项 | 落态 | 判据（`K-V3R-26` 字面，逐字照录） | 盘上实测读数（0 改写） | **根因（三分类）** |
|---|---|---|---|---|
| **O1_discrete_cell_redistribution** | **FAIL** | 字面支：仍 `n_distinct ≤ 1` → FAIL；字面支：`n_distinct > 3 + std > 0` → **PASS（改判）** | `rates.n_distinct = 9`、`std = 0.0012788884062167251` ⇒ **落在字面的 PASS 支**；r3 记 `new_verdict = FAIL`、`kill_line_fail_hit = true`、`kill_line_branch_id = READING_B_V2_ROW3_ND_GT_3_AND_STD_GT_0` | **假证伪（判据面/口径面）** —— 见 §3 根因 `D0`–`D2` |
| **O3_logit_normal_form** | **FAIL** | 同上 | `rates.n_distinct = 8`、`std = 0.0044661691265184735` ⇒ **落在字面的 PASS 支**；r3 同记 FAIL | **假证伪（判据面/口径面）** |
| **O5_replicator_ode_softlimit** | **FAIL** | 同上 | `rates.n_distinct = 9`、`std = 16.980008842717528` ⇒ **落在字面的 PASS 支**；r3 同记 FAIL | **假证伪（判据面/口径面）** |
| **#26b 件级终态** | **FAIL**（档 3：原标注维持） | `revise_tier_4_docket` 档 3 字面：「FAIL（即原标注维持）⇒ 0 改判动作；原报告 byte 0 触动」 | `three_ontology_summary.verdicts` 三体全 FAIL；`same_direction = true`；`hit_tier_all_same = true`；`hit_tier` = 3× 「档 3：FAIL（原标注维持）」 | **假证伪（判据面/口径面）** |

**落档依据一句话（0 模糊）**：本轮 FAIL **不是**「P-J 构造后 convergence_rate 分布不达标」这一命题被证伪；它是**判据侧改档**的结果——r3 把 `K-V3R-26` 字面对本读数实际所落之域（`n_distinct > 3 ∧ std > 0`）给出的 **PASS** 改判为 **FAIL**。**读数面事实 0 变**（同一批 `n_distinct`／`std` 逐值同于读法甲 `49c6e5a07732`），**变的是该域的输出档位**。

**判死纪律声明（0 软化）**：本件**直书「#26b 三本体 FAIL 落档成立，但该 FAIL 为假证伪（判据面/口径面失灵）」**；⛔ **0** 写「P-J 重构造命题成立」；⛔ **0** 写「P-J 重构造命题已死」；⛔ **0** 由本 FAIL 反推真实面（真实语料/真实世界 convergence 行为）的任何方向主张。

---

## §2 判别要件逐条核验（真证伪四要件 · 全满足才算真证伪）

| 要件 | 结论 | 盘上证据（本人读盘） |
|---|:--:|---|
| ① kill-line 先于实验冻结 | **部分满足 · 0 满足** | **时序层 ✔**（§0：字面锚 09-27 13:33:20 早于一切测量）；**语义层 ✘** —— prereg v1 **自身**载两句并存字面：L118 载 K-V3R-26 完整字面（`n_distinct > 3 + std > 0 → PASS`；`n_distinct ≤ 1 → FAIL`），但 L152 载「本预登记对此为**占位，待 PI 复核生效拍板形式后冻结**」、L274 载「§2.4 新阈值提案三处（K-V3R-26/27/28 占位）—— worker 跑前 PI 拍板形式后冻结」、L8 件头载「**待 PI 复核生效，生效即锁**」、L217 载「PI 复核栏（待 PI 签字生效即锁）」⇒ **PI 签字在盘 0 留痕**。**「时序早」不等于「已冻结生效」** |
| ② 构造非恒等 / 非退化 | **满足** | `pre_run_degenerate_gate.degenerate_alarm_hit = false`；门内逐字段 `n_distinct` 7/8/8/7（`pj_legacy_convergence_rates_CONTROL` 1 为对照组、`gate_pass = false`、**不计入 gate_alarm**）；三本体读数 `n_distinct = 9/8/9`、`std > 0` 全域；`c4_in_process_full_recompute_identical = true` |
| ③ 素材面覆盖 claim 所需 | **满足（本项无缺口）** | 3 本体 × 9 模型（doubao-seed-2.0-lite／glm-5.3／deepseek-v4-flash／doubao-seed-evolving／minimax-m3／glm-5.3-flash／kimi-k2.7-code／doubao-seed-2.1-turbo／deepseek-v4-pro）；`construct.paired_sampling` 三本体共用同一批扰动抽样（`perturbation_table_sha12 = 0b23943c898c`）⇒ 配对比较成立；`consistency_with_preexp_and_26` 逐体 `vs_preexp_per_model_rate_identical = true` |
| ④ 度量有分辨力 | **满足** | 三本体 `rates` 均 `n ≥ 8` 且 `n_distinct` 全互异（O1 `min/max = 0.0132/0.0173`、O3 `0.33899999999999997/0.3557`、O5 `17.9501/72.0337`）；无 `std = 0` 格、无 `n_distinct ≤ 1` 格 |

⇒ **① 0 满足（语义层）⇒ 真证伪要件不全 ⇒ 不得归真证伪**。**且 ②③④ 满足 ⇒ 失败面不在读数/构造侧 ⇒ 归「假证伪（判据面/口径面）」而非「不明」**（根因已由盘上代码与读数逐行定位、可复算，故**不归不明**）。

---

## §3 判据面根因清单（`D0`–`D2` · 全部可复算 · 本人读盘定位）

| ID | 根因 | 盘上依据 |
|---|---|---|
| **`D0`** | **字面自相矛盾：判死线字面对本读数实际所落之域给出 PASS，而现行执行面对该域输出 FAIL。** `KILL_LINE_LITERAL`（`6c83e7a7ca2e` L129–L131，逐字照录）明写「`convergence_rate n_distinct > 3 + std > 0 → PASS（改判）；仍 n_distinct ≤ 1 → FAIL（维持假证伪）`」；而 `judge_K_V3R_26`（同件 L370–L389）**首个分支**即 `if nd > 3 and std > 0.0:` ⇒ 直接 `return {"new_verdict": "FAIL", "kill_line_fail_hit": True, ...}`。**实测 `nd = 9/8/9`、`std > 0` ⇒ 100% 命中该分支** ⇒ 三本体的 FAIL 全部由「字面 PASS 域被改判为 FAIL」产生，**0 由 `n_distinct ≤ 1` 支产生** | `6c83e7a7ca2e` L129–L131 ／ L362–L389；`c9d3c9f819f1` `per_ontology.*.kill_line_branch_id`（三体同 = `READING_B_V2_ROW3_ND_GT_3_AND_STD_GT_0`，**0 命中 `ND_LE_1` 支**） |
| **`D1`** | **γ 根因自陈为「判别力归零」＝ 判据面失灵的自认，但该自认被写进 γ 栏（根因栏）而非落进判据裁定本身。** 三体 `gamma_root_cause` 逐字：「判据面恒定 ⇒ **PASS 侧全域消失 ⇒ 判别力归零**（读法乙结构性来源）」；`gamma_source` 逐字指向「归属表 **v2**（读法乙 · 现行）—— 7e2b0bb39cfe §1.1 第 3 行 + _v5_bulk_activation_2026_09_28.md §3.1（K-V5RB-E-3 四要素齐备，起算 2026-09-28 23:42 GMT+8）」。**判别力归零的判据在读数未变的情况下得出三体同档 FAIL** ⇒ 判据 0 区分任何读数（构造面恒为 FAIL），此即 `D0` 的机制层表述 | `c9d3c9f819f1` `per_ontology.*.gamma_root_cause` / `.gamma_source`；`b5a50447b4da` L122（归属表 v1 失效 / v2 全域 FAIL 生效）、L161（第 3 行 `n ≥ 4 ∧ s > 0` PASS→**FAIL**）、L163（全域 `V ≡ FAIL`） |
| **`D2`** | **改档的授权原始记录在盘 0 原件形态（U-6 及其扩面）。** 改 F2 分支的授权回执 `ask_90009bd33020f0b43a270672` **q1**（PI 09-29 10:44）在盘上 10 件命中**全为自载或转述**（executor L6/L357/L829/L848、result L7/L28、登记件 L4/L182、收口册 L115、F2 登记件 L189、F2 收口件 L70、材料件 §6.2、本棒 §5）⇒ **0 件问卷原件形态**；22:44 `ask_1aca8ed0bef608fff8298b2c`（6 件命中）与 23:01 `ask_79496aa9b225033bdd1fb829`（2 件命中，**仅 `1599cb99abf3` + 材料件**）同样 0 原件。`1599cb99abf3` §5 自陈分级：23:01 = **E-A 但「据派工单转供逐字照录」**、22:44 与 10:44 = **E-B 盘上件内转述**、23:01 盘上无 L1 直录载体 = **E-C** | 本人独立复测三回执全仓命中（§5 表）＋ `1599cb99abf3` L72 / L88 / L111–L113；⛔ **本棒 0 推断任一授权真伪、0 以转述充原件** |

**⇒ 归因结论**：#26b 的 FAIL **是 `D0`（字面 PASS 域被改判为 FAIL）＋ `D1`（该改判导致判别力归零）＋ `D2`（改档授权链 0 原始记录）共同构成的判据面失灵**。**不是**命题面被证伪，**不是**构造/读数面失灵（②③④ 满足），**不是**不明（根因逐行可定位）。

---

## §4 双读法（主读法 + 替代读法 · 分歧如实写明）

| 读法 | 内容 | O1 | O3 | O5 | 件级 | **分歧点** |
|---|---|---|---|---|---|---|
| **M1（主读法 · 判据优先 + 机制可复算）** | 依 §2 判别要件：①语义层 0 满足 ⇒ 不得真证伪；②③④ 满足 ⇒ 失败面不在读数/构造侧 ⇒ 归**假证伪（判据面/口径面）**；依 §1 依 `revise_tier_4_docket` 档 3 落 **FAIL** | FAIL | FAIL | FAIL | **FAIL** | **根因 = 假证伪（判据面）** |
| **R1（替代读法 · 纯 K-V3R-26 字面，0 引入任何归属表）** | 只按 prereg v1 L118 字面逐本体求值：`n_distinct = 9/8/9 > 3` 且 `std > 0` ⇒ **命中 PASS 支（改判）** ⇒ 三本体落 **PASS**，件级落 **档 1**（「PASS + 一致 ⇒ 原 V3 报告不动；立改判件入勘误链 E-41.x 系」） | PASS | PASS | PASS | **PASS** | **终态分歧：FAIL vs PASS** |
| **R2（替代读法 · 承认 PI 23:01 追认为已闭环授权）** | 若 PI 径认「23:01 追认 r3」已覆盖 `D2` 授权链缺口（即 `D2` 消解）⇒ 根因仍为**假证伪（判据面）**（`D0`／`D1` 不受 `D2` 影响）⇒ 终态**仍 FAIL** | FAIL | FAIL | FAIL | **FAIL** | **0 分歧**（终态稳健，根因分类不变） |
| **R3（替代读法 · 剔 `D0` 改档面，只看读法甲同读数）** | 读法甲 `49c6e5a07732` 对**逐值相同**的读数（`n_distinct = 9/8/9`、`std` 同值）落 **3/3 PASS** ⇒ 同一读数在两执行面得**相反**档位（PASS vs FAIL）⇒ 反证 `D0`（分歧源于判据改档，0 源于读数） | PASS | PASS | PASS | **PASS** | **终态分歧：FAIL vs PASS**（但 R3 之 PASS 是**读法甲已废止面**的历史档，仅作 `D0` 之佐证，**不构成本轮终态**） |

- **分歧如实写明**：**M1 与 R1／R3 在件级终态上真分歧（FAIL vs PASS）**；M1 与 R2 终态无分歧。
- **本棒裁 M1，裁据**：
  1. **R1 之所以不采为终态**：`K-V3R-26` 字面在 prereg v1 中**自陈为「占位，待 PI 复核生效拍板形式后冻结」**（L152／L274），件头 L8 亦载「待 PI 复核生效，生效即锁」，L217 载「PI 复核栏（待 PI 签字生效即锁）」⇒ **该字面在盘 0 冻结生效留痕**。以一个**盘上未生效留痕**的字面单独推翻 PI 09-28 23:42 拍板并经 `b5a50447b4da` 登记生效的归属表 v2，属**以未冻结字面压生效裁定**。**但 R1 的存在必须保留**——它证明 M1 的 FAIL **不是**从字面自然落出的，而是判据改档的结果（这正是 `D0` 的独立佐证）。
  2. **R3 之所以不采为终态**：读法甲档位已被归属表 v2 逐行取代（`b5a50447b4da` L161–L163 逐行对照表），且 `c9d3c9f819f1` `iron_rules.no_retrospection_asrun_3_3_PASS_intact = true` 明载 as-run PASS 维持原判、0 回溯。**R3 的价值在证明读数 0 变、档位变**。
  3. **M1 之所以必须裁而非落 KD**：根因（`D0`／`D1`／`D2`）**已由盘上代码与读数逐行定位且可复算**，`②③④` 三要件**满足**，`①` 的 0 满足**只排除真证伪、不排除假证伪**。落 KD 会把一个**根因已明确**的结论压回不明态，**违反「诚实的根因是不误导」**。**KD 只留给根因不可定位或须 PI 先行的项**——本件的 KD 面在 §6 单列（Q1–Q4 与 `γ-VK-4`），**不吞掉件级终态**。
- **0 掩盖 R1／R3 的存在**：二读法已在本表全文列示，0 删除、0 静默择一。

---

## §5 kill-line 逐条裁定（对照预登记字面 · 阈值 0 调整）

| 判死线 | value（盘上实测） | hit | verdict |
|---|---|:--:|---|
| `K-V3R-26` 字面（prereg v1 L118 逐字） | 三本体 `n_distinct = 9/8/9`、`std > 0` ⇒ 落在「`n_distinct > 3 + std > 0`」域 | **字面支 ≠ 执行支** | **字面支应落 PASS（改判）；执行面落 FAIL ⇒ 记 `D0`（判据改档）** |
| `K-V3R-26` 字面（现行执行面 `6c83e7a7ca2e` L129–L131） | 与 prereg v1 L118 **逐字全等**（本人开读核对） | ✔ | **满足**（字面 3 执行面全等，0 擅调） |
| `K-V3R-26` `TH-V3R-26` 形式 | `th_form_frozen = "convergence_rate_m = mean_j(n_iter_j) / n_budget, j=1..100"`；实测逐模型 `convergence_rate` 与 `n_iter_mean` 逐值对应（O1 例：doubao-seed-2.0-lite `n_iter_mean = 1.58` ↔ `convergence_rate = 0.0158`） | ✔ | **满足**（0 新设数值切点） |
| `K-V3R-0-A` 防退化门 | `degenerate_alarm_hit = false`；门内逐字段 `n_distinct` 7/8/8/7（对照组 1 为 `gate_pass = false`、0 计入 alarm） | ✔（门达） | **满足**（门不达面 0 触发） |
| `K-V3R-0-C` 双口径成对 | `dual_caliber_pair_complete = true`（三体）；`dual_caliber_consistency` 逐字「系统性不一致（读法乙 v2：new_verdict ≡ FAIL vs legacy_verdict = UNVERIFIED（判据退化）⇒ K-V3R-0-C「维持原标注 + γ 升级」路径必然触发；沿 K-V5RB-0-L **0 豁免并报**）」 | ✔ | **满足**（0 豁免并报） |
| `K-V5RB-E-3` F2 废止四要素 | 哪件 `_v5_item26b_endpoint_definition_prereg_2026_09_28.md`（`5e59a11466db`）／哪行 §1.2 三条表第 2 行／起算 2026-09-28 23:42 GMT+8／哪次复核 `ask_c7f297823ff964c19ca89aa1`（q2） | ✔ | **形式满足**（四要素齐备） |
| `K-V5RB-0-D` γ 强制改写 | `gamma_root_cause_rewritten_per_K_V5RB_0_D = true`；`gamma_root_cause` 逐字非构造类（禁记构造常量／弱分布／方差恒同） | ✔ | **满足**（0 记构造类根因） |
| `K-V5RB-0-J` 0 回改既有件 | as-run `49c6e5a07732` 3/3 PASS 维持、源件 `5c906113a210` byte 0 触动 | ✔ | **满足** |
| `K-V5RB-0-L` 双口径不一致 0 豁免 | `dual_caliber_consistency` 明载「0 豁免并报」 | ✔ | **满足** |
| **0 新设阈值** | 9 项常量三执行面全等（`KV3R_26_PASS_N_DISTINCT_MIN = 4`、`KV3R_26_FAIL_N_DISTINCT_MAX = 1`、`DEGEN_N_DISTINCT_MIN / DEGEN_STD_MIN_EXCL = 4 / 0.0`、`SEED = 20260927`、`N_BUDGET = 100`、`JITTER = 0.05` 等）；`iron_rules.0_new_numeric_threshold = true` | ✔ | **满足**（**0 调阈值**） |
| **0 私设条款** | `kill_line.no_private_clause_added = true` | ✔ | **满足** |
| **执行面唯一性** | r3 唯一（`1599cb99abf3` §1 表 1：PI 23:01「追认 r3：0 动作结项」；§1.1 第 4 项：⛔ 另立重名 runner **不落**） | ✔ | **满足** |
| **派生 JSON 不合并** | r3 读数 = 新名独立件 `c9d3c9f819f1`；**⚠ r2 无对应派生读数件落盘**（本人实测：全仓 `*26b*r2*` 仅命中 executor 1 件）⇒ **面缺口**（成因 0 推断，记 `γ-VK-5`） | ✔（r3 面） | **满足（r2 面缺口另记）** |
| **16 项 iron_rules** | 逐项全 `true`（含 `kill_line_K_V3R_26_literal_untouched`、`source_executor_byte_0_touched`、`reading_b_in_force_F2_abolished`、`derived_json_not_merged`、`formal_verdict_this_piece`） | ✔ | **满足** |

---

## §6 待裁清册（**PI 专属事实层 · 本棒 0 代裁** · 穷尽）

> **本棒立场**：件级终态已收口（§1 FAIL ＋ §3 根因）。以下 4 项**均属「PI 是否曾授权／追认／拍板」的授权事实层**——该层证据不在盘上件内任何形态中，**verdict-keeper 无权以转述充原件、亦无权代 PI 追认**。故**逐条挂账、0 自行闭合**。

| ID | 待裁事项 | 归属 | 对本件终态的影响 |
|---|---|---|---|
| **Q1** | 派工单两处前提不吻合（①「修复棒产物在盘未见」实为已见 `a0cab58c032e`／`1599cb99abf3`；② 兜底动作「另立新名 runner」已被 PI 23:01 裁定明文禁绝）⇒ 是否确认 **② 号任务 0 触发**、#26b 沿 r3 现状入判定面 | **PI** | **0 影响终态**（① 属派工单叙述纠正；② 的禁绝已使「另立 runner」0 可能，且本棒 0 另立） |
| **Q2** | 23:01「追认 r3」的档位映射（`1599cb99abf3` §1.2 自陈为**落册层对齐**、非 PI 原字）⇒ 是否需 PI 明示措辞 | **PI** | **0 影响终态**（映射为落册层，PI 原字「追认 r3：0 动作结项」已足证执行面唯一性） |
| **Q3** | prereg v1「占位待 PI 拍板后冻结」（L152／L274／L8／L217）vs rescript「跑前已冻结」＋ rescript **PI 复核栏未签** 之歧义如何了 | **PI / verdict-keeper** | **0 影响终态**，但**直接影响 §2 要件①的表述强度**：若 PI 追认 v1 已生效冻结 ⇒ 要件①升为**满足**（终态仍 FAIL、根因分类不变，因 `D0`／`D1` 不受要件①影响）；若 PI 维持「占位」⇒ 要件①**维持 0 满足**（真证伪永久排除） |
| **Q4** | U-6（10:44 授权 `ask_90009bd33020f0b43a270672` **q1** 盘上 0 原始记录）之补齐 or 径认 | **PI** | **0 影响终态**（`D2` 属证据链缺口，0 属判定要件；但**留痕完整性属 evidence-auditor 域，我 0 代审**） |
| **`γ-VK-4`（本棒新登记）** | **本棒实测扩面**：`D2` 缺口不限于 q1 —— 22:44 `ask_1aca8ed0bef608fff8298b2c`（6 件命中）与 23:01 `ask_79496aa9b225033bdd1fb829`（**2 件命中**）在盘上亦 0 原件形态；且 `1599cb99abf3` §5 自陈 23:01 系**「据派工单转供逐字照录」**、盘上无 L1 直录载体 | **PI / evidence-auditor** | **0 影响终态**（如实登记，0 推断真伪，0 冒充原始记录） |
| **`γ-VK-5`（本棒新登记）** | **r2 派生读数件 0 落盘面缺口**：本人实测全仓 `*26b*r2*` 仅命中 executor 1 件 ⇒ r2 的正式读数面在盘**不存在**；成因（未跑／跑了未落／并入 r3）**0 推断** | **PI / protocol-keeper** | **0 影响终态**（r3 为现行面，r2 已被取代） |
| **`γ-VK-6`（本棒新登记）** | **#26b 判定登记表现行性缺口**：本人实测 `_v3_recheck_verdict_register_2026_09_27.md`（`d9b6b974cfc1`）L83 载 #26b 落「**第 2 行：PASS + 不一致**（3/3 同向 PASS，`hit_tier_all_same = true`）」——**注：该处「PASS + 不一致」与 `hit_tier_all_same = true` 自身并列矛盾**（材料件 §6.1 记为读法甲档 2 面）⇒ 判定登记表与 r3 读数（档 3 FAIL）**并存两个已登记面** | **PI / verdict-keeper** | **0 影响本件终态**（本件为新名判定件，0 回改登记表；登记表处置 0 代裁） |

---

## §7 结论上限与外推边界（冻结，防误导）

- **可判域（构造面）**：`3 本体（O1 离散胞元再分配 / O3 logit-normal / O5 replicator-ODE 软限）× 9 模型 × 配对扰动（`perturbation_table_sha12 = 0b23943c898c`）`；唯一判据切点 = `K-V3R-26` 字面 `n_distinct > 3` ∧ `std > 0`。
- **0 外推**：①0 真实语料 / 真实世界 convergence 行为主张；②0 其他 seed / 其他扰动幅度 / 其他 `n_budget`；③0 其他本体或模型；④0 r2 面（0 读数落盘，成因未裁）；⑤0 PI 授权链真伪（`D2`／`γ-VK-4` 0 推断）；⑥0 #26b 判定登记表之历史档位（并存面 0 合并、0 择一改写）。
- **双口径并报**（沿 `K-V3R-0-C`）：`new_verdict ≡ FAIL` vs `legacy_verdict = UNVERIFIED（判据退化）` **系统性不一致**，`dual_caliber_pair_complete = true` ⇒ **0 豁免、0 择一**，两面同读。
- **机制披露随结论同读**：`γ_root_cause` 自陈「**判别力归零**（读法乙结构性来源）」⇒ 在归属表 v2 之下，本判据域**恒为 FAIL、不区分任何读数**。**此即 FAIL 的来源披露**，读本结论者须同读此句，否则会误读为「读数不达标」。

---

## §8 老实交代

1. **本棒跑了什么**：**0 跑实验**。0 跑 executor 本体、0 调 `main()`、0 复算读数、0 复跑任何面。§1 全部读数系**本人 `json.load` 只读取原值**（未四舍五入、0 单位换算、0 重算、0 补位）；§5 常量与字面系**本人逐行读盘核对**。
2. **0 复算声明**：`c9d3c9f819f1` 的 `reproducibility.payload_sha12 = 1630d518b7d9`（件内未给 `payload_core` 序列化口径）⇒ **0 复算、0 推断**。
3. **引件纪律**：§0 表 16 件全部**本人盘上实测** `Get-FileHash SHA256`，与派工单／材料件字面**逐值一致**（0 处不一致）。**0 编造**外部文献号／法条号／专有名词。
4. **skill**：派工单未指定 ⇒ **0 加载任何 skill**，0 编造 skill 指令。
5. **0 产品面显式列出**：①0 新实验产物（0 落任何 result/JSON）；②0 新阈值（唯一判据切点仍 `K-V3R-26` 字面 `n_distinct > 3`）；③0 新判据（`D0`–`D2` 均为**既有字面的机制层归因**，非新规）；④0 改写既有件（**本件为唯一新建件**，其余 16 件全程只读）；⑤0 回改 `d9b6b974cfc1` 登记表（`γ-VK-6` 仅登记不代裁）；⑥0 独立复核他人判定（`γ-VK-6` 的「PASS + 不一致 vs `hit_tier_all_same = true`」矛盾**仅如实登记**，0 重裁读法甲面）。
6. **本件自指 SHA-12 不自写入**（沿体例，避自指悖论）⇒ 由本棒回执自报盘上实测值。
7. **succeeded ≠ 跑完**：本件以「落盘 + SHA-12 实测」为准。
8. **一处我必须承认的判断分量**：**M1 vs R1 的件级终态分歧（FAIL vs PASS）不由机械判据唯一决定**，由「盘上未生效留痕的字面 0 推翻 PI 已登记生效的裁定」这一裁量决定。**该裁量已全文列示（§4），供 PI / verifier 独立推翻**。若 PI 裁 Q3 为「v1 字面已生效冻结」且裁 Q4 为「23:01 追认未覆盖读法乙改档」，则 R1 有可能成为终态——**但那需要 PI 同时处置 `D2`，单凭字面效力不足以翻转 `D0`**。
9. **Q1–Q4 我未闭合的理由**：四项均属「PI 是否曾授权／追认／拍板」之**授权事实层**，证据不在盘上件内任何形态（本人全仓复测确认 0 原件）。**verdict-keeper 以转述充原件 ＝ 伪造证据链；以推定充授权 ＝ 越权**。故逐条挂账（§6），**0 自行闭合**。

---

## §9 落盘回执

| 产物 | 路径 | sha12 | bytes |
|---|---|---|---|
| **判定件（本件 · 唯一新建件）** | `results/_v3_recheck_26b_verdict_2026_10_01.md` | **见本棒回执（自指指纹 0 自写入）** | — |
| 判定输入（0 改动） | 见 §0 表 16 件 | 见 §0 | 见 §0 |

---

出件｜**verdict-keeper**（Mavis 团队 verdict-keeper，agent-3a4d09ba3c90；非 PI / protocol-keeper / worker / evidence-auditor / verifier / doc-writer / Trae code）｜2026-10-01
