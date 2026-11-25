# #26b（`K-V3R-26` literal-gap）判定面准备件 · worker · 2026-10-01

> **本件性质**：**判定面材料件**（**0 判定**）。为 verdict-keeper 备齐 ①件族清单 ②读数摘引 ③`K-V3R-26` 判死线字面 ④前置/冻结状态 ⑤可判性声明。
> **棒别**：deposon · #26b 判定面准备棒（worker 执行面）｜**出证方**：**worker**（session `mvs_125db22bb46b4fedb0272380d71bb84e`）。⛔ **0 冒充** PI / verdict-keeper / evidence-auditor / protocol-keeper / verifier / doc-writer。
> **件名**：`results/_v3_recheck_26b_verdict_prep_2026_10_01.md`（**新名**；落盘前实测 ＝ 不存在 ⇒ **0 覆写任何既有件**）。
> **纪律**：0 编造｜**0 改任何既有件 1 字节**（全部只读）｜**0 调阈值**｜**0 出判定**｜**0 擅调判死线**｜R4（key 永不明文）｜UTF-8 无 BOM · LF｜SHA-12 ＝ `sha256(全文)[:12]` 小写、**盘上终态实测**｜**0 网络外呼 / 0 LLM / 0 proxy / 0 key 读取**。

---

## §0 一句话交底 ＋ **②号任务触发判定：不触发（0 动作）**

**交底**：#26b 现行执行面 ＝ **r3**（`6c83e7a7ca2e`），其读法乙读数（`c9d3c9f819f1`）三本体同向 `FAIL`；**本棒 0 判定**，只备料。核验中发现**派工单两处前提与盘上终态不吻合**，均如实登记（§0.1），**本棒据此 0 动作**。

### §0.1 派工单前提与盘上终态的两处不吻合（如实登记 · **0 调和**）

| # | 派工单字面 | 盘上实测（终态） | 本棒处置 |
|---:|---|---|---|
| 1 | 「当晚有修复棒在跑，**其产物在盘未见**」 | **产物在盘已见**：`results/_f2_branch_fix_register_2026_09_29.md`（`a0cab58c032e` / 22,940 B / 09-29 22:57:03）＋ `results/_f2_closeout_note_2026_09_29.md`（`1599cb99abf3` / 16,317 B / 09-29 23:05:32）＋ `.tmp/f2_branch_fix_transform_2026_09_29.py`（18,152 B，**该棒自陈已中止**）＋ `.tmp/f2_branch_selftest_2026_09_29.py`（7,377 B） | **前提不成立** ⇒ 派工单 ② 的触发条件（「若修复棒产物 0 落盘」）**不满足** |
| 2 | ② 的兜底动作「**另立新名 runner**（照读法乙修 F2 分支）并复跑产出终态读数」 | **该动作已被 PI 23:01 裁定明文禁绝**：`1599cb99abf3` §1.1 第 4 项逐字「另立重名 runner ⛔ **不落**。同一判据面 0 允许并存两件「现行」runner（防双执行面）」；PI 23:01 答文逐字「**追认 r3：0 动作结项**」（回执 `ask_79496aa9b225033bdd1fb829` · ts `1790694082078`） | **兜底动作已被 0 授权** ⇒ **本棒 0 另立 runner、0 复跑、0 产新派生 JSON** |

**⇒ ② 号任务（另立新名 runner ＋ 复跑）本棒判定为「0 触发」**：触发条件不成立（#1），且其规定动作已被现行 PI 裁定禁绝（#2）。本棒**只出本件 1 件材料件**，0 伴生 JSON（材料面无需机读件）。**0 自行调和**该两处不吻合，交 PI／verdict-keeper 复核。

---

## §1 判定面件族清单（**全名面检索 `*26b*` ＋ 近名面** · 盘上实测）

**检索法**：`Get-ChildItem -Recurse -Filter "*26b*"`（全仓，含 `.tmp/`、`.mavis/`）＋ 正则名面检索 `K.V3R.26|kv3r|V3R.26|26b`。⇒ **件族恰 9 件**（与派工单件数一致），**0 近名漏检**。

### §1.1 #26b 件族（9 件 · 按 mtime 升序）

| # | 件（repo 相对路径） | SHA-12（实测） | 字节 | mtime | 角色 | 现行性 |
|---:|---|---|---:|---|---|---|
| 1 | `results/_v3_recheck_26b_executor_2026_09_27.py` | `5c906113a210` | 43,171 | 09-27 15:51:38 | **executor 原件**（`K-V5RB-0-K` 点名被修源件）；L307 `judge_K_V3R_26`；L309–L310 F2 域 `→ "PASS"` | **历史执行面**（读法甲）· byte 0 触动 |
| 2 | `results/_v3_recheck_26b_result_2026_09_27.json` | `49c6e5a07732` | 44,379 | 09-27 15:52:40 | **as-run 派生件**（读法甲 3/3 PASS） | **历史读数** · 沿 0 回溯口径**维持原判** |
| 3 | `results/_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | `bb0a211fa675` | 38,885 | 09-28 20:24:02 | 预登记族 · **字面空档 v2** | 预登记面（历史件） |
| 4 | `results/_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | `5e59a11466db` | 38,939 | 09-28 21:32:27 | 预登记族 · **F1/F2/F3 端点定义**（F2 废止登记义务载体，§1.2 第 2 行） | 预登记面（历史件） |
| 5 | `results/_v5_item26b_attribution_effective_2026_09_28.md` | `c353fbcdc753` | 35,261 | 09-28 22:29:35 | 预登记族 · **归属终局表 v1**（读法甲） | **已失效**（沿读法乙 v2 取代）· 留历史快照 |
| 6 | `results/_v3_recheck_26b_executor_r2_2026_09_28.py` | `0808af6212c5` | 52,272 | 09-28 22:47:39 | **r2 修订件**（空档两枝终局化） | **已被 r3 取代**（非现行） |
| 7 | `results/_v3_recheck_26b_executor_r3_2026_09_29.py` | `6c83e7a7ca2e` | 64,959 | 09-29 10:50:41 | **r3 修订件**（F2 分支读法乙实现面） | ★ **现行执行面**（PI 09-29 23:01 追认） |
| 8 | `results/_v3_recheck_26b_r3_result_2026_09_29.json` | `c9d3c9f819f1` | 54,294 | 09-29 19:08:57 | **r3 派生读数件**（读法乙首读数） | ★ **现行读数**（唯一读法乙读数面） |
| 9 | `results/_v3_recheck_26b_rescript_2026_09_27.md` | `ae81d9b59054` | 30,552 | 09-30 16:15:20 | **改判件 rescript**（原标注 + 档位字面来源） | 面在盘（PI 复核栏**未签**，见 §5.3） |

**⇒ 全 9 件指纹与派工单字面逐值一致**（`5c906113a210` / `43,171 B`、`0808af6212c5`、`6c83e7a7ca2e` / `64,959 B`、`c9d3c9f819f1` / `54,294 B` / `09-29 19:08`）。

### §1.2 近名／邻域件（判定面须一并在视野内 · 盘上实测）

| # | 件 | SHA-12 | 字节 | mtime | 与 #26b 的关系 |
|---:|---|---|---:|---|---|
| 1 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | `88052d7db895` | 37,346 | **09-27 13:33:20** | ★ **判死线字面锚**（§2.2 K-V3R-26 / §2.4 TH-V3R-26 / §2.3 四档）— **早于一切测量** |
| 2 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | `bcc3cee23e82` | 42,970 | — | 预登记 v1.1 |
| 3 | `results/_v3_recheck_prereg_v1p2_2026_09_27.md` | `9da148037744` | 38,932 | 09-30 16:15:20 | 预登记 v1.2（**空档归独立 UNDECIDED 档**提案来源） |
| 4 | `results/_v3_recheck_prereg_v1p3_2026_09_27.md` | `272ed65bf50e` | 35,200 | 09-30 16:15:20 | 预登记 v1.3 |
| 5 | `results/_v5_c3_reading_b_prereg_2026_09_28.md` | **`8dcf5e1e6dde`** | 32,178 | 09-30 17:02:47 | ★ **读法乙定义件**（r3 读数自陈 prereg_source；F2 废止提案） |
| 6 | `results/_v5_bulk_activation_2026_09_28.md` | **`b5a50447b4da`** | 39,378 | 09-30 17:02:47 | ★ **读法乙生效登记件**（K-V5RB-E-1/2/3 生效事实唯一盘上来源） |
| 7 | `results/_v5_exec_f2_r3_register_2026_09_29.md` | `9d64ee1d6996` | 24,177 | 09-29 10:54:17 | r3 改造登记件（他人棒） |
| 8 | `results/_f2_branch_fix_register_2026_09_29.md` | `a0cab58c032e` | 22,940 | 09-29 22:57:03 | ★ **F2 修复棒登记件**（结论「已修 · 本棒 0 修复动作」＋ 差异面板） |
| 9 | `results/_clearance_evening_round_register_2026_09_29.md` | `9c5543961e27` | 18,201 | 09-29 22:49:26 | 22:44「授权改实现」L1 直录载体 ＋ **§4.3 张力登记面** |
| 10 | `results/_f2_closeout_note_2026_09_29.md` | `1599cb99abf3` | 16,317 | 09-29 23:05:32 | ★ **23:01「追认 r3」收口落册件**（现行执行面唯一性来源） |
| 11 | `results/_v5_clearance_mr14_rerun_note_2026_09_29.md` | `f3dd5efd3e34` | 22,894 | 09-29 19:12:01 | `K-V5RB-0-L` 双口径不一致登记面（U-4 已登记项） |
| 12 | `results/_v3_recheck_verdict_register_2026_09_27.md` | `d9b6b974cfc1` | 112,085 | 09-30 16:15:20 | ⚠ **#26b 判定登记表**（**读法甲 档 2 面**，见 §6.1） |
| 13 | `.tmp/f2_branch_fix_transform_2026_09_29.py` | — | 18,152 | 09-29 22:53:30 | scratch · 该棒自陈**已中止**、**0 产出半成品 runner** |
| 14 | `.tmp/f2_branch_selftest_2026_09_29.py` | — | 7,377 | 09-29 22:54:26 | scratch · 自测脚本 |

> **面完整性如实交代**：**r2 修订件无对应派生读数件落盘**（件族内 0 件 `*26b_r2_*result*`）⇒ r2 的正式读数面在盘**不存在**。**本棒 0 推断**其成因（未跑／跑了未落／并入 r3），如实登记为**面缺口**。

---

## §2 「最新有效执行面」认定 ＋ `K-V3R-26` 判死线字面（**0 擅调 · 先冻后读**）

### §2.1 现行执行面 ＝ **r3**（认定依据逐条可核）

| # | 依据 | 出处 |
|---:|---|---|
| 1 | PI 09-29 **23:01** 答文逐字「**追认 r3：0 动作结项（推荐）**」（回执 `ask_79496aa9b225033bdd1fb829` · ts `1790694082078`） | `1599cb99abf3` §1 表 1 |
| 2 | 落册语义：r3 ＝ **F2 线程唯一现行执行面**；「F2 分支修复」项**即结**；⛔ **0 另立 runner** | `1599cb99abf3` §1.1 表 1–4 |
| 3 | r3 读法乙读数**已落盘并与执行面自证一致**（19:08 三本体全落 `READING_B_V2_ROW3_ND_GT_3_AND_STD_GT_0`） | `c9d3c9f819f1` `per_ontology` 三体（§3.2） |
| 4 | 档位映射的诚实边界：PI 23:01 **未**重述三档枚举、**未**使用「对 ③ 的追认确认」措辞 ⇒ 映射属**落册层对齐**，非 PI 原字 | `1599cb99abf3` §1.2（**本棒照录该边界，0 升格**） |

### §2.2 判死线字面（**逐字照录 · 0 改写 · 0 擅调**）

**现行执行面 r3 的字面常量**（`6c83e7a7ca2e` L129–L133 逐字）：

```
KILL_LINE_LITERAL = "K-V3R-26: P-J 重构造（真 convergence_rate 定义 + 真 perturbation ±0.05×100）后
                     convergence_rate n_distinct > 3 + std > 0 → PASS（改判）；
                     仍 n_distinct ≤ 1 → FAIL（维持假证伪）"
TH_LITERAL         = "TH-V3R-26: convergence_rate 形式（无预注册阈值，由 K-V3R-26 重定义）= n_iter / n_budget"
```

**r3 读数件内登记的同名字面**（`c9d3c9f819f1` `kill_line` 节）：`id = "K-V3R-26"`；`literal` ＝ 上记逐字（**逐值一致**）；`th_literal` ＝ 上记逐字；`th_form_frozen = "convergence_rate_m = mean_j(n_iter_j) / n_budget, j=1..100"`；`per_ontology_independent = True`；`no_private_clause_added = True`。

**先冻后读 · 事后 0 调的实测证据（本棒 L3 独立复算 · `ast` 字面量提取 · 0 import · 0 exec）**：

| 项 | 原件 `5c906113a210` | r2 `0808af6212c5` | r3 `6c83e7a7ca2e` | 三面全等 |
|---|---|---|---|:--:|
| `KILL_LINE_LITERAL` | L80–L82 | ＝ | L129–L131 | ✅ |
| `TH_LITERAL` | L83 | ＝ | L132–L133 | ✅ |
| `KV3R_26_PASS_N_DISTINCT_MIN` | 4 | 4 | 4 | ✅ |
| `KV3R_26_FAIL_N_DISTINCT_MAX` | 1 | 1 | 1 | ✅ |
| `DEGEN_N_DISTINCT_MIN` / `DEGEN_STD_MIN_EXCL` | 4 / 0.0 | 4 / 0.0 | 4 / 0.0 | ✅ |
| `SEED` / `N_BUDGET` / `JITTER` | 20260927 / 100 / 0.05 | 同 | 同 | ✅ |

> **结论（限于字面层）**：**判死线字面与全部阈值常量在三个执行面逐字全等** ⇒ **0 擅调、0 事后调**成立。**r3 唯一改动面是 F2 分支的**输出档位**（`PASS` → `FAIL` ＋ γ 改写），不是判死线字面本体**（沿 `K-V5RB-0-J` 0 回改既有件）。
> **⛔ 本棒 0 推断**：r3 的 F2 分支输出语义**是否恰当**属判定面事项，**本棒 0 评价**（已在 §6 归入可判性两态）。

**冻结时序（判死线先于测量 · mtime 实测）**：

```
09-27 13:33:20  88052d7db895  prereg v1（判死线/TH/四档字面锚）   ← 最早
09-27 15:51:38  5c906113a210  26b executor 原件落盘
09-27 15:52:40  49c6e5a07732  26b as-run 读数落盘（读法甲）
09-28 22:47:39  0808af6212c5  r2 修订件
09-28 23:42（时刻字面）      读法乙 F2 废止起算（PI 拍板转录）
09-29 10:50:41  6c83e7a7ca2e  r3 修订件落盘
09-29 19:08:57  c9d3c9f819f1  r3 读法乙读数落盘              ← 最晚
```

**⇒ 判死线字面锚（prereg v1）早于 26b 一切测量 2h18m，早于 r3 读数 2 天 5h35m** ⇒ **「先冻后读」在时序层成立**。

**⚠️ 冻结状态的一处如实登记（⛔ 本棒 0 调和）**：prereg v1 **自身**对 K-V3R-26 的冻结状态有两句并存字面——
- L152：「K-V3R-26 「convergence_rate 重定义」属 worker 落地时新设 … **本预登记对此为占位，待 PI 复核生效拍板形式后冻结**」
- L274：「**§2.4 新阈值提案三处**（K-V3R-26/27/28 占位）—— worker 跑前 PI 拍板形式后冻结」

而 26b rescript §3 标题自陈「K-V3R-26 / TH-V3R-26 字面（**0 擅调；判据面跑前即冻结**）」，其件头 L9 又载「**PI 复核栏：待 PI 签字生效即锁**」（盘上未签）。⇒ **「prereg 自陈占位待 PI 拍板冻结」vs「rescript 自陈跑前已冻结 ＋ PI 复核栏未签」并存**；本棒**0 判定何者为准**，如实列入待 PI 复核（§6.3 Q3）。

---

## §3 读数摘引（**自 `c9d3c9f819f1` 逐字摘引 · 0 改写任何数值**）

> **摘引纪律**：以下全部字段与数值**逐字取自** `results/_v3_recheck_26b_r3_result_2026_09_29.json`（`c9d3c9f819f1`）；**0 四舍五入、0 单位换算、0 重算、0 补位**。本棒**0 调用 `main()`、0 复跑 executor、0 复算读数**。

### §3.1 件级元数据（逐字）

| 字段 | 逐字值 |
|---|---|
| `schema` | `v3_recheck_formal_data/26b_p_j_three_ontology/1` |
| `nature` | 正式判定档：逐本体出 K-V3R-26 正式 verdict（区别于 26 preexp = 探索性档 verdict=null） |
| `date` / `date_r2` / `date_r3` | `2026-09-27` / `2026-09-28` / `2026-09-29` |
| `revision` | r3 · 读法乙生效 ⇒ F2 字面废止 ⇒ 归属表 v2 全域 FAIL；真分布域（n_distinct>3 且 std>0）PASS 翻 FAIL + γ 沿 K-V5RB-0-D 强制改写（PI 2026-09-29 10:44 ask_90009bd33020f0b43a270672 q1 授权改 F2 分支，承接 K-V5RB-0-K 另案授权；0 新设阈值、0 新增第四态、0 回溯、0 回改既有件） |
| `produced_by_r3` | Mavis 团队 worker（session mvs_ce8c37cbf1944b19800d7c3a28543591；PI 2026-09-29 10:44 ask_90009bd33020f0b43a270672 q1 授权改 F2 分支；如实署名，不冒充 PI / protocol-keeper / verdict-keeper / evidence-auditor / verifier） |
| `runtime` | 0 LLM; numpy + hashlib + json only; no network; read-only inputs; 0 改动既有件（r3：源件 5c906113a210、r2 件 0808af6212c5、26b 原派生件与 r2 派生件均 byte 0 触动，本件落新名派生件 _v3_recheck_26b_r3_result_2026_09_29.json） |

### §3.2 三本体读数（**判据证据面** · 逐字）

| 字段 | O1_discrete_cell_redistribution | O3_logit_normal_form | O5_replicator_ode_softlimit |
|---|---|---|---|
| `n_iter_cap` | 60 | 100000 | 200000 |
| **`new_verdict`** | **FAIL** | **FAIL** | **FAIL** |
| `kill_line_fail_hit` | True | True | True |
| `kill_line_pass` | False | False | False |
| `kill_line_branch_id` | `READING_B_V2_ROW3_ND_GT_3_AND_STD_GT_0` | 同左 | 同左 |
| **`rates.n_distinct`** | **9** | **8** | **9** |
| **`rates.std`** | **0.0012788884062167251** | **0.0044661691265184735** | **16.980008842717528** |
| `rates.rel_std` | 0.08641137879842738 | 0.01290551664376365 | 0.4128045508003189 |
| `rates.min` / `max` | 0.0132 / 0.0173 | 0.33899999999999997 / 0.3557 | 17.9501 / 72.0337 |
| `rates.mean` / `median` / `iqr` | 0.014799999999999999 / 0.0149 / 0.0020999999999999994 | 0.34606666666666663 / 0.3454 / 0.0037000000000000366 | 41.13328888888889 / 35.767399999999995 / 25.152900000000002 |
| `draw_level.n_iter_n_distinct` | 4 | 20 | 784 |
| `draw_level.total_steps` | 1332 | 31146 | 3701996 |
| **`legacy_verdict`** | UNVERIFIED（判据退化） | UNVERIFIED（判据退化） | UNVERIFIED（判据退化） |
| `dual_caliber_pair_complete` | True | True | True |
| **`gamma_root_cause`** | 判据面恒定 ⇒ PASS 侧全域消失 ⇒ 判别力归零（读法乙结构性来源） | 同左 | 同左 |

**分支字面（三体逐字同）**：`kill_line_branch_literal = "n_distinct>3 且 std>0 → FAIL（归属表 v2 现行 · 读法乙全域 V ≡ FAIL；F2 字面「n≥4 且 std>0 → PASS」已废止，起算 2026-09-28 23:42 GMT+8；v1 同域 PASS 留历史快照）"`

**双口径一致性（三体逐字同）**：`dual_caliber_consistency = "系统性不一致（读法乙 v2：new_verdict ≡ FAIL vs legacy_verdict=UNVERIFIED（判据退化） ⇒ K-V3R-0-C 「维持原标注 + γ 升级」路径必然触发；沿 K-V5RB-0-L **0 豁免并报**）"`

### §3.3 三本体汇总（逐字）

| 字段 | 逐字值 |
|---|---|
| `same_direction` | True |
| `agreement_statement` | 同向（3/3 本体新构造 verdict 一致 = FAIL） |
| `hit_tier` | `["档3：FAIL（原标注维持）", "档3：FAIL（原标注维持）", "档3：FAIL（原标注维持）"]` |
| `hit_tier_all_same` | True |
| `rule_literal` | 派工单：三本体同向 ⇒ 改判建议按同向给；分歧 ⇒ 维持原标注＋登记分歧＋γ（不择优不聚合掩盖，逐本体并报） |
| `summary_branch` | 三本体同向 FAIL ⇒ 0 改判动作；原 V3 标注（UNVERIFIED/假证伪）维持，V3 原报告 byte 0 触动。**r3 读法乙注记**：此 FAIL 依**归属表 v2**（全域 V ≡ FAIL；F2 字面已废止，起算 2026-09-28 23:42 GMT+8），γ 根因沿 **K-V5RB-0-D** 记「判据面恒定 ⇒ PASS 侧全域消失 ⇒ 判别力归零（读法乙结构性来源）」，**禁**记为构造类根因；**0 回溯** —— as-run 既有 PASS 登记维持原判，本件只约束起算时刻之后的读数 |
| `verdict`（件级） | `{"O1_discrete_cell_redistribution": "FAIL", "O3_logit_normal_form": "FAIL", "O5_replicator_ode_softlimit": "FAIL"}` |
| `verdict_note` | 正式判定档：本件出 K-V3R-26 逐本体正式 verdict（3 本体独立判定）+ 双口径并报。**r3 读法乙注记**：本读数域内 PASS 档已全域消失（归属表 v2）⇒ new_verdict 预期恒为 FAIL；若出现 PASS 即为异常取值，须 γ 升级（K-V5RB-0-K 已授权改实现，本件为授权后首个实现面）。 |

### §3.4 构造面 / 门 / 自证面（逐字，供判定面核「0 新设阈值」）

| 字段 | 逐字值 |
|---|---|
| `construct.n_budget` / `seed` / `priority` | `100` / `20260927` / `surplus_first` |
| `construct.jitter` | `+-0.05 uniform on T_frac60 (clip [0,1])` |
| `construct.tolerance` | `TOL = 1e-6（O3/O5 统一；O1 为整数精确命中）` |
| `construct.paired_sampling` | 3 本体共用同一批扰动抽样（rng 流与第一梯队 / preexp 逐字同）=> 配对比较成立 |
| `construct.perturbation_table_sha12` | `0b23943c898c` |
| `construct.literal_source` | O1/O3/O5 构造与实现常数逐字沿 results/_v3_recheck_26_preexp_executor_2026_09_27.py（775217a462f5） |
| `pre_run_degenerate_gate.gate_literal` | `K-V3R-0-A：n_distinct > 3 + std > 0；任一输入字段 n_distinct ≤ 3 = 退化警报` |
| `pre_run_degenerate_gate.degenerate_alarm_hit` | **False** |
| 门内逐字段 `n_distinct`/`std` | `pj_T_frac60` 7 / 0.10659488672794401；`60cells_cos_sim` 8 / 0.06006708800773012；`60cells_D_fix2_cosine` 8 / 0.060067088007730106；`60cells_T30` 7 / 3.197221015541813；`pj_legacy_convergence_rates_CONTROL` 1 / 0.0（`gate_pass = false`，对照组，**不计入 gate_alarm**） |
| `legacy_face` | `convergence_rates = [0.1]×9`；`n_distinct = 1`；`std = 0.0`；`verdict = "UNVERIFIED（判据退化）"`；`ontology_independent = True` |
| `consistency_with_preexp_and_26.O1` | `vs_preexp_per_model_rate_identical = True`；`vs_preexp_rates_n_distinct = 9`；`vs_26_landed_result_identical = True`；`vs_preexp_verdict = "n/a（preexp 探索性档，verdict = null）"` |
| `consistency_with_preexp_and_26.O3` / `.O5` | `vs_preexp_per_model_rate_identical = True`；`vs_preexp_rates_n_distinct = 8` / `9`；verdict 同为 `n/a` |
| `reproducibility_in_process` | `c4_in_process_full_recompute_identical = True`；逐体 True |
| `reproducibility.payload_sha12` | `1630d518b7d9`（件内注：`hashlib.sha256(canonical json of payload_core).hexdigest()[:12]`）—— **⛔ 本棒 0 复算**（件内未给 `payload_core` 的序列化口径，0 推断） |
| `iron_rules` | 16 项全 `True`（含 `kill_line_K_V3R_26_literal_untouched`、`source_executor_byte_0_touched`、`reading_b_in_force_F2_abolished`、`0_new_numeric_threshold`、`derived_json_not_merged`、`formal_verdict_this_piece`） |

---

## §4 前置／冻结状态表（判定面须逐项过）

| # | 前置项 | 盘上状态 | 依据 |
|---:|---|---|---|
| 1 | **判死线字面锚先于测量** | ✅ 成立（prereg v1 09-27 13:33:20 早于 26b 读数 15:52:40） | §2.2 时序表 |
| 2 | **判死线字面事后 0 调** | ✅ 三执行面 `ast` 字面量**逐字全等**（9/9 常量） | §2.2 全等表 |
| 3 | **0 新设阈值** | ✅ 9 项常量三面全等；`iron_rules.0_new_numeric_threshold = True` | §2.2 ＋ §3.4 |
| 4 | **0 私设条款** | ✅ `kill_line.no_private_clause_added = True` | `c9d3c9f819f1` |
| 5 | **执行面唯一性** | ✅ r3 唯一（PI 23:01 追认；⛔ 0 并存第二现行 runner） | `1599cb99abf3` §1.1 |
| 6 | **读法乙生效登记** | ✅ K-V5RB-E-1/2/3 三门齐备（登记面字面，件已回填注记） | `b5a50447b4da` |
| 7 | **F2 废止四要素** | ✅ 已登记（哪件/哪行/起算 2026-09-28 23:42 GMT+8/哪次复核 `ask_c7f297823ff964c19ca89aa1`） | `c9d3c9f819f1` `kill_line.f2_literal_abolition_registration` |
| 8 | **0 回溯** | ✅ as-run 3/3 PASS（`49c6e5a07732`）维持原判、byte 0 触动 | `c9d3c9f819f1` `iron_rules` ＋ §1.1 第 2 行 |
| 9 | **防退化门跑前自证** | ✅ `degenerate_alarm_hit = False` | §3.4 |
| 10 | **0 网络 / 0 LLM / 0 key** | ✅ 件内自陈 ＋ 本棒独立同守 | §3.1 `runtime` |
| 11 | **派生件不合并** | ✅ r2/r3 各落新名 JSON ＋ as-run 原件维持（**但 r2 无派生件落盘**，面缺口见 §1.2 注） | §1.1 ＋ §1.2 |
| 12 | ⚠ **判死线冻结形态的 PI 拍板直录** | ❓ **并存两说**（prereg v1 自陈「占位待 PI 拍板后冻结」vs rescript 自陈「跑前已冻结」）；rescript **PI 复核栏未签** | §2.2 ⚠ 段 |
| 13 | ⚠ **读法乙实现面的授权原始记录** | ❌ **盘上 0 原始记录**（U-6，见 §6.2） | §6.2 |
| 14 | ⚠ **#26b 判定登记面现行性** | ⚠ 登记表 `d9b6b974cfc1` 仍为**读法甲 档 2 面**（见 §6.1） | §6.1 |

---

## §5 可判性声明（**本棒 0 判定**）

### §5.1 声明

**本棒 0 对 #26b 出任何判定。** 本件只提供判定面材料：件族清单（§1）、读数摘引（§3）、判死线字面（§2.2）、前置/冻结状态（§4）。**档位归属、是否翻案、是否改判、桶位落点一概 0 判**——四档（`c9d3c9f819f1` `revise_tier_4_docket`）的落档属 verdict-keeper 职权。⛔ **0 复跑、0 改实现、0 调阈值、0 调和张力**。

### §5.2 两态建议（**建议，非判定** · 供 PI／verdict-keeper 取向）

| 态 | 成立条件 | 说明 |
|---|---|---|
| **可判** | ① PI 认可 §2.2 ⚠ 项之歧义（占位 vs 已冻结）已由某件闭环，**或**径认 rescript §3 的跑前冻结自陈；② PI 就 U-6 缺口表态（补原始记录 or 径认 23:01 追认已覆盖） | 则 #26b 具备**单一读法乙读数面 ＋ 唯一执行面 ＋ 判死线字面三面全等**的判定面 ⇒ 可进入档位落档 |
| **不可判** | ① 冻结形态歧义 ＋ ② U-6 缺口 **两项均未闭环** | 则判据面存在**授权链原始记录缺口 ＋ 前置冻结态歧义** ⇒ 建议先补前置、**0 先出判定** |

**本棒倾向（如实标注为倾向 · 非判定）**：**倾向「不可判」**——理由是 §4 第 12／13 两项前置未闭环，且 §6.1 的登记表现行性问题未处理。⛔ **本棒不代裁、不代 PI 勾选**。

### §5.3 待 PI 复核清单（4 项 · 本棒 0 代裁）

| ID | 事项 | 归属 |
|---:|---|---|
| **Q1** | 派工单两处前提不吻合（修复棒产物「在盘未见」实为已见；「另立新名 runner」已被 23:01 裁定禁绝）⇒ 是否确认 **② 号任务 0 触发**、#26b 沿 r3 现状入判定面 | **PI** |
| **Q2** | 23:01「追认 r3」的档位映射（`1599cb99abf3` §1.2 自陈为**落册层对齐**、非 PI 原字）⇒ 是否需 PI 明示措辞 | **PI** |
| **Q3** | prereg v1「占位待 PI 拍板后冻结」vs rescript「跑前已冻结 ＋ PI 复核栏未签」之歧义如何了 | **PI / verdict-keeper** |
| **Q4** | U-6（10:44 授权 `ask_90009bd33020f0b43a270672` **q1** 盘上 0 原始记录）之补齐或径认 | **PI** |

---

## §6 判定面须知的两处既存面状态（如实登记 · **0 调和**）

### §6.1 #26b 判定登记表仍为**读法甲 档 2 面**（⚠ 现行性缺口）

`results/_v3_recheck_verdict_register_2026_09_27.md`（`d9b6b974cfc1`）L51 载 #26b 行：`rescript c300e74a082c / 29,349 B` ＋ `result 49c6e5a07732 / 44,379 B`；L83 载 26b 落「**第 2 行：PASS + 不一致**（26b 三本体 O1/O3/O5 3/3 同向 PASS，`hit_tier_all_same = true`）」；L251 载 `γ₂₆₃` 双口径不一致。

**本棒全仓检索实测**：该登记表内 **0 命中**「读法乙」／「READING_B」／「归属表」／「r3」⇒ **登记表未纳入 r3／读法乙面**，与 r3 读数的**档 3（FAIL · 原标注维持）**并存。

⇒ **判定面存在两件并存的「已登记读法甲面」与「现行读法乙读数面」**。本棒**0 改登记表、0 判定何者为准**，如实登记（Q1 相邻事项）。

### §6.2 U-6 授权原始记录缺口（**本棒独立复测 · 维持挂账 · 0 推断真伪**）

**复测法**：全仓 `grep` 三个回执标识 —— `ask_90009bd33020f0b43a270672`（10:44）／`ask_1aca8ed0bef608fff8298b2c`（22:44）／`ask_79496aa9b225033bdd1fb829`（23:01）。

| 回执 | 盘上命中形态 | 是否有**问卷原件**（原始回执／答文记录件） |
|---|---|---|
| `ask_90009bd33020f0b43a270672` **q1**（10:44 授权改 F2 分支） | 件内自载（r3 executor L6/L357/L829/L848、r3 result L7/L28、r3 登记件 L4/L182）＋ 他件转述（收口册 L115、F2 登记件 L189、F2 收口件 L70）；同 id 另有 **q2**（`_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` L37/L38/L58/L170）＋ **q3**（`_v5_gamma_r1_v2_withdraw_2026_09_29.md` L41/L117/L230） | ❌ **0 件原件形态**（q1 命中全为自载或转述） |
| `ask_1aca8ed0bef608fff8298b2c`（22:44 授权改实现） | 收口册 L23/L29/L35 自称 L1 直录；F2 登记件 L7／收口件 L71 标注为**盘上件内转述（E-B）** | ❌ **0 件原件形态** |
| `ask_79496aa9b225033bdd1fb829`（23:01 追认 r3） | 收口件 L13/L72 载回执 id ＋ ts，§5 自陈「**本册据派工单转供逐字照录**」 | ❌ **0 件原件形态**（**转供**，非直录） |

**⇒ 本棒实测补充（0 擅自扩大 U-6 范围，仅如实登记）**：U-6 原登记仅限 `q1` 题位；本棒复测显示 **22:44 与 23:01 两回执在盘上亦 0 原件形态**。⛔ **0 推断任一授权的真伪、0 冒充原始问卷记录、0 以转述充原始**。归属 **PI**（Q2／Q4）。

---

## §7 指纹实测总表（**盘上终态 · `sha256(全文)[:12]` 小写**）

| # | 件 | 件内/他件登记值 | **本棒实测** | 字节 | 结论 |
|---:|---|---|---|---:|---|
| 1 | `_v3_recheck_26b_executor_2026_09_27.py` | `5c906113a210` | `5c906113a210` | 43,171 | ✅ 一致 |
| 2 | `_v3_recheck_26b_executor_r2_2026_09_28.py` | `0808af6212c5` | `0808af6212c5` | 52,272 | ✅ 一致 |
| 3 | `_v3_recheck_26b_executor_r3_2026_09_29.py` | `6c83e7a7ca2e` | `6c83e7a7ca2e` | 64,959 | ✅ 一致 |
| 4 | `_v3_recheck_26b_r3_result_2026_09_29.json` | `c9d3c9f819f1` | `c9d3c9f819f1` | 54,294 | ✅ 一致 |
| 5 | `_v3_recheck_26b_result_2026_09_27.json` | `49c6e5a07732` | `49c6e5a07732` | 44,379 | ✅ 一致 |
| 6 | `_v3_recheck_26b_rescript_2026_09_27.md` | `ae81d9b59054` | `ae81d9b59054` | 30,552 | ✅ 一致 |
| 7 | `_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | `bb0a211fa675` | `bb0a211fa675` | 38,885 | ✅ 一致 |
| 8 | `_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | `5e59a11466db` | `5e59a11466db` | 38,939 | ✅ 一致 |
| 9 | `_v5_item26b_attribution_effective_2026_09_28.md` | `c353fbcdc753` | `c353fbcdc753` | 35,261 | ✅ 一致 |
| 10 | `_v3_recheck_prereg_v1_2026_09_27.md` | `88052d7db895` | `88052d7db895` | 37,346 | ✅ 一致 |
| 11 | `_v3_recheck_26_preexp_executor_2026_09_27.py` | `775217a462f5` | `775217a462f5` | 38,726 | ✅ 一致 |
| 12 | `_v3_recheck_26_executor_2026_09_27.py` | `46c326c756c3` | `46c326c756c3` | 15,056 | ✅ 一致 |
| 13 | `_v3_recheck_26_result_2026_09_27.json` | `eb6a99dd46dd` | `eb6a99dd46dd` | 11,994 | ✅ 一致 |
| 14 | `_v3_recheck_26_rescript_2026_09_27.md` | `6b86576146a3` | `6b86576146a3` | 13,747 | ✅ 一致 |
| 15 | `_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | `a9ad1de618f5` | `a9ad1de618f5` | 1,669 | ✅ 一致 |
| 16 | `deposon_v3_physical_opt_60cells_2026_09_11.json` | `c659695aa23c` | `c659695aa23c` | 17,732 | ✅ 一致 |
| 17 | `_v5_exec_f2_r3_register_2026_09_29.md` | `9d64ee1d6996` | `9d64ee1d6996` | 24,177 | ✅ 一致 |
| 18 | `_f2_branch_fix_register_2026_09_29.md` | `a0cab58c032e` | `a0cab58c032e` | 22,940 | ✅ 一致 |
| 19 | `_clearance_evening_round_register_2026_09_29.md` | `9c5543961e27` | `9c5543961e27` | 18,201 | ✅ 一致 |
| 20 | `_f2_closeout_note_2026_09_29.md` | （无他件登记值） | `1599cb99abf3` | 16,317 | **本棒新增实测** |
| 21 | `_v5_clearance_mr14_rerun_note_2026_09_29.md` | （无他件登记值） | `f3dd5efd3e34` | 22,894 | **本棒新增实测** |
| 22 | `_v3_recheck_verdict_register_2026_09_27.md` | （无他件登记值） | `d9b6b974cfc1` | 112,085 | **本棒新增实测** |

### §7.1 4 处**登记滞后**（stale reference）—— **均已在案登记 · 非破链 · 非篡改**

| # | 引用方所记值 | **盘上终态实测** | 滞后机制 ＋ 在案登记出处 |
|---:|---|---|---|
| 1 | r3 result `dispatch_inputs` 记 preexp 报告 `0a2b5c837c83`（21,855 B） | **`a46230e344af` / 23,048 B**（mtime 09-30 16:15:20） | **纯文末追加**（skill 引用面复核注记，「0 删改历史字面」）⇒ 登记于 `_skill_reference_update_and_user_surface_survey_2026_09_30.md`（`cb7b7ec9ebcd`）L76 第 10 行 |
| 2 | 26b rescript §2 记自身 `c300e74a082c` / 29,349 B（＝判定登记表 L51 同记） | **`ae81d9b59054` / 30,552 B** | **纯文末追加**（同上技能注记）⇒ 同件 L77 第 11 行（`c300e74a082c → ae81d9b59054`，29,349 → 30,552） |
| 3 | r3 result 记读法乙定义件 `7e2b0bb39cfe`（31,333 B） | **`8dcf5e1e6dde` / 32,178 B**（mtime 09-30 17:02:47） | **文末「指纹口径校正」注记**（自陈「纯文末追加、0 删改上文任何原行」）⇒ `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`（`41d7b76ea4d6`）L161 第 8 项 **✅ PASS**（前缀 `==` 逐件自证） |
| 4 | r3 result／F2 登记件记生效登记件 `92ac9a956bd3`（38,533 B） | **`b5a50447b4da` / 39,378 B**（mtime 09-30 17:02:47） | 同上注记形态 ⇒ 同件 L160 第 7 项 **✅ PASS** |

**⇒ 核法与定性（本棒如实交代）**：四件滞后件 mtime **全部晚于** r3 读数落盘（09-29 19:08:57），且全部落在 09-30 两次批量 mtime 簇（16:15:20 / 17:02:47）内；**先行排查「快照／登记后被追加而未复测」机制**（**0 直接归因破链或篡改**）。四件的追加形态、字节增量与在案登记**逐条可核**。⛔ **本棒 0 回改任何引用方**（沿 0 回改既有件纪律）——残留引用交 evidence-auditor／统一更正批。

---

## §8 0 覆写 ／ 0 触自证

| 项 | 状态 |
|---|---|
| **既有件修改** | **0 字节**。§1／§1.2／§7 所列 22 件指纹**落盘后复测全部复现**（见交付回执） |
| **写入句柄** | 本棒**未对任何既有件取得写入句柄**；全部既有件经 `read`／`grep`／只读 `hashlib` 打开 |
| **本棒唯一写入** | **1 件新名件**＝ 本件（`results/_v3_recheck_26b_verdict_prep_2026_10_01.md`） |
| **伴随 JSON** | **0 件**（判定面材料无需机读派生件；材料数值已逐字摘引于本件 §3） |
| **新名 runner** | **0 件**（§0.1 判定 ② 不触发；PI 23:01 裁定禁绝并存第二现行执行面） |
| **复跑** | **0 次**（0 调 `main()`、0 跑任何 executor、0 产新读数） |
| **scratch（非交付）** | 3 件：`.tmp/_26b_verdict_prep_hashcheck_2026_10_01.py`、`.tmp/_26b_verdict_prep_literalcheck_2026_10_01.py`、`.tmp/_26b_verdict_prep_validate_2026_10_01.py`（**纯只读校验脚本**：指纹复算／`ast` 字面量提取（**0 import 目标模块、0 exec**）／落盘后 0 触自证） |
| **0 网络 / 0 LLM / 0 proxy / 0 key** | ✅ 全部 0（本地 `python` 单脚本 ＋ 只读检索） |
| **编码** | 本件 UTF-8 **无 BOM** · **LF**（落盘后实测） |
| **自指指纹** | **不自写入本件**（自指口径）—— 指纹／字节记入**交付回执** |

## §9 老实交代（本棒 0 做与 0 复算面）

| 项 | 如实交代 |
|---|---|
| 0 复算 | `c9d3c9f819f1` 的 `reproducibility.payload_sha12 = 1630d518b7d9`（件内未给 `payload_core` 序列化口径）⇒ **0 复算、0 推断** |
| 0 复算 | 三本体读数**0 复跑、0 重算**；§3 全部为**逐字摘引**（`json.load` 只读 ＋ 逐字段取原值） |
| 0 复算 | `_v5_item26b_*` 三件**正文 0 开读**（仅取指纹／字节／mtime；其语义系**转引** r3 读数件与 F2 登记件的引用字面） |
| 0 复算 | `_f2_branch_fix_register_2026_09_29.md` §4 差异面板 ＋ §5 八侧自测**正文 0 独立复算**（本棒只核其**落册结论**并独立验证判死线三面全等） |
| 0 开读 | **0 开问卷原件**（三回执均只在盘上件内以转述形态出现，见 §6.2） |
| 0 检索 | **0 检索**仓外／会话侧路径 |
| 0 评价 | r3 的 F2 分支输出语义（读法乙）**是否恰当**、#26b **应落何档**、登记表与 r3 **何者为准** ⇒ **本棒一概 0 判** |
| 未闭环 | §5.3 **Q1–Q4** 四项待 PI 复核；§7.1 四处残留引用交 evidence-auditor；§1.2 **r2 派生件缺失**成因 0 推断 |

## §10 交付核验（**诞生即报** · 自指指纹不自写入本件）

| 项 | 值 |
|---|---|
| 产出路径 | `results/_v3_recheck_26b_verdict_prep_2026_10_01.md`（本件 · **新名** · 落盘前实测不存在） |
| 产出件数 | **1 件**（达成即停） |
| 性质 | **判定面材料件 · 0 判定** |
| 状态 | 材料齐备（清单／读数／判死线字面／前置冻结／可判性声明）｜**判定待 verdict-keeper**｜**Q1–Q4 待 PI 复核** |
| 复核状态 | ☐ **待 PI 复核**（本件 0 增 0 减任何 PI 裁定的效力） |

**本件三行收口**：
1. **② 号任务 0 触发**：修复棒产物**在盘已见**（`a0cab58c032e` ＋ `1599cb99abf3`），且「另立新名 runner」**已被 PI 23:01「追认 r3：0 动作结项」明文禁绝** ⇒ 本棒 **0 另立 runner、0 复跑、0 产新读数**，**0 调和**派工单与盘上的两处不吻合。
2. **判定面已备齐**：件族 9 件＋邻域 14 件全指纹实测；`K-V3R-26` 判死线字面在**三个执行面逐字全等**（9/9 常量）且**时序早于测量**；r3 读法乙读数**逐字摘引 0 改写**；前置 14 项逐项过（2 项 ❓／❌ 未闭环）。
3. **可判性 0 代裁**：两态建议（可判／不可判）**倾向不可判**（Q3 冻结态歧义 ＋ Q4 U-6 授权原始记录缺口未闭环，＋ §6.1 登记表仍为读法甲面）—— 倾向**如实标注为倾向**，**0 判定、0 代 PI 勾选**。

## §11 PI 复核栏

☐ 确认 Q1（② 号任务 0 触发 · 沿 r3 现状入判定面）　☐ 就 Q2 明示「追认 r3」措辞或径认落册层对齐　☐ 裁 Q3（判死线冻结形态歧义：占位 vs 跑前已冻结）　☐ 裁 Q4（U-6 授权原始记录缺口：补齐 or 径认）　☐ 就 §6.1 裁定 #26b 登记表（读法甲 档 2 面）与 r3 读数（读法乙 档 3 面）的关系处置　☐ 裁 §1.2「r2 派生读数件 0 落盘」面缺口处置

签字：__________　日期：__________
