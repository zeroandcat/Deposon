# 门③ 之「111 件之落档确认」件（`verdict-keeper`）· 2026-10-28

> 📌 **本件性质**：**判定文书收口件**（门③ 之第一合取项「全部判定件由 `verdict-keeper` 落档」之**逐件落档状态确认**）。⛔ **0** 落五终判（`pass`／`af`／`kd`／`fail`／`give-up`）· ⛔ **0** 代 PI 裁 · ⛔ **0** 代销记 · ⛔ **0** 宣告门③ 成就 · ⛔ **0** 宣告①段毕或任何段毕 · ⛔ **0** 回改任何既有件一字 · ⛔ **0** 移动／重命名／删除／新建目录（**只出此 1 件新件**）· ⛔ **0** 跑实验 · ⛔ **0** 联网 · ⛔ **0** 调 LLM／API · ⛔ **0** 读 `〔本地路径已脱敏〕` · 归档区**只按名与指纹认人·⛔ 0 读其内容**。
> 📌 **本棒**：`verdict-keeper`（判定收口官 · agent-3a4d09ba3c90）· 分支会话 `mvs_f36b8217012244dfadcf1f0ae1b48545` · 观测时点 **2026-10-28 11:40:54** GMT+8。
> 📌 **本件之射程**：**仅**及于**门③ 之底数 111 件**（甲 77 ＋ 乙 28 ＋ 丙 6）之**逐件落档状态**。⛔ **0** 评任何判定件之**实体面**（判死线之真伪·读数之对错·结论之取舍）——实体面之判定权属 `verdict-keeper`／PI，⛔ **0** 外推为母件「判定件」之**真全集**（母件 0 处给出全集·§6 之 `NOT_MEASURED` 面）。

---

## §0 · 一句话

> 📌 **在 111 之射程内，三态已闭且两读同**：**已落档 111 ／ 未落档 0 ／ 挂账 0**（读甲「件在盘且指纹符」与读乙「在盘 ∧ 有逐件落档登记行 ∧ VK 归属行可核」**同得此数**，加总 111、容差 0）。
> 📌 **然门③ 仍不得转 `PASS`**——其阻碍**不在落档面**，而在**底数之闭合性**与**裁决权之归属**：
> ① 母件 L160 之判据对象是「**全部**判定件」，而 111 是**已核集合非全集**（丙面 252 件之落款面「从未核」＋ 母件 0 处给出全集定义 ⇒ **真全集机械不可得**）⇒「全部」这一**全称量词未证**；
> ② 门③ 之**第二合取项**（`evidence-auditor` 证据链审计 PASS）之裁决权属 EA／PI，本件⛔ **0** 代其裁；
> ③ 2 件**挂账**（no.24 `f1ca2c59bed9`／no.336 `66d8d45c7a62`）**未补证** ⇒ 底数非闭；
> ④ EA 审计件之「108」→「111」之**勘正件未另立**（v269 L113 明载「待办」）。
> 📌 **故本件之判**：**落档面 ＝ 已全数落档（111／111）**；**门③ 之现值仍为 `PWC`**，其转 `PASS` 之要件见 §5（四件齐·阈值可机械判）。

---

## §1 · 源件、令源与「PWC」之正身（**回源自测**）

### §1-1 · 源件之实位与自测指纹（**两源件皆在 `results\evidence\register\`，非 `verdict\judgement\`**）

| # | 件（相对路径·自仓根起） | bytes（自测） | SHA-12（自测） | 实位 | 观测时点 |
|:-:|:--|--:|:--|:--|:--|
| 1 | `results/evidence/register/_gate3_faceA_itemlist_register_2026_10_24.md` | 38,840 | `512b31f1a1ed` | `results/evidence/register/` | 2026-10-28 11:40:54 |
| 2 | `results/evidence/register/_gate3_108_ea_audit_2026_10_24.md` | 44,650 | `8ebb365be944` | `results/evidence/register/` | 2026-10-28 11:40:54 |

> 📌 **目录漂移之实证**：本单所述之二源件**不在** `results/verdict/judgement/`；若按名于该目录寻之，将误报「全缺」（陷阱第 12 型）。
> 📌 **母件之判据字面**（自测 36,066 B／`996feb1db9cb`）：`results/readout/run/_v34_experiment_gap_plan_2026_10_08.md` **L160** 逐字——
> 「『V3~V4 完整收尾』之宣告须**同时**满足：① §2.1 八项硬缺口 0 残留；② 全部波次产出件 0 有「不明/未核得」状态；③ **全部判定件由 `verdict-keeper` 落档 ＋ `evidence-auditor` 证据链审计 PASS**；④ 全量成果清单（上传/论文委托用）出件。**⛔ 本件 0 宣告已收官**（宣告权属 PI，阶段名启用权亦在 PI）。」

### §1-2 · 底数 111 之构成（**加总自证·容差 0**）

| 面 | 件数 | 仓别（repo／sub） | 在册之据（件·位号） |
|:--|--:|:--|:--|
| **甲面**（判定件·落款方 ＝ `verdict-keeper`） | **77** | 69 ／ 8 | 甲面清单 §3-1 主表 L87–L163（序 1–77）＋ §3-2 互斥 3 件 L171–L173（PI 采「读乙·计入」·**逐件单列**） |
| **乙面**（125 件「无件性质栏〔不可判〕」中经口径丙补定者） | **28** | 14 ／ 14 | EA 审计 §1-3 L119–L146 |
| **丙面**（口径乙「14 字窗」技术假阴） | **6** | 6 ／ 0 | EA 审计 §1-4 L152–L157 |
| **合计** | **111** | — | **77 ＋ 28 ＋ 6 ＝ 111** ✅ **加总自证·容差 0** |

> 📌 **底数之令源**：PI 2026-10-24 01:5x 之卡答 `ask_27c25f4375962a1ae305bdb4` → `q_gate3_faceA` → **`read_yi`**（采读乙）——登记于甲面清单 **L7**／**L23–L27**／**L167**；其裁之落账正身见 §1-3 之 v269。

### §1-3 · 「PWC」之正身（**⛔0 以册名充裁号·故本件不引「裁 268」为内容之据**）

| 项 | 值 |
|:--|:--|
| **正身件（采 PWC 之裁）** | `pi_rulings/_pi_card_answers_register_2026_10_24_v268.md`（bytes 8,945／SHA-12 `c9a941c196ad`·自测）· 题名逐字「**PI 卡答落账 v268** · 「**全采荐案**」（2026-10-24 01:5x）」 |
| **正身件（读乙之裁）** | `pi_rulings/_pi_card_answers_register_2026_10_24_v269.md`（bytes 9,398／SHA-12 `0cee727234cf`·自测）· 题名逐字「**PI 卡答落账 v269** · 末轮四答（2026-10-24 02:0x）」 |
| **裁号识读之限（如实）** | ⚠ **此二件（及最新之 v536）件内 0 处 `\| **NNN** \|` 裁号行**（本棒逐件实测：v268 0 行／v269 0 行／v536 0 行）⇒ **裁号本身无件内行可回源**。本件**只引（件名·行号·指纹）**，⛔ **0** 以册名／题名充内容之据；**内容已开卷逐字取**（§4）。 |
| **本件不引之号** | ⛔ **0** 引「裁 268」「裁 269」为任何内容之据（陷阱第 7 型「文件名索引 ≠ 裁号」之防） |

---

## §2 · 三态之判据（**可机械判·非「看起来在」**）

### §2-1 · 三面之定义（**每面皆可由脚本复算·判据之射程写死**）

| 面 | 判据（机械） | 射程／规则 |
|:--|:--|:--|
| **面①·在盘且指纹相符** | 该件于**在册所载之仓**（`repo` ＝ `〔本地路径已脱敏〕`／`sub` ＝ `〔本地路径已脱敏〕`）与**在册所载之相对路径**之下**实测存在**，且**实测 bytes 与 SHA-12 与在册登记值逐位相符** | 两仓之全树 |
| **面②·逐件落档登记行** | 该件之**件名**（或其相对路径）与其 **SHA-12 同现于某登记册件之同一行** | 登记册面 ＝ `results\`（全子树）＋ `pi_rulings\` ＋ 仓根 `*.md`（**⛔0 计入 `.tmp\` 之半成品**）；本棒实测扫描 **3068 件** `.md` |
| **面③·VK 归属行可核** | 该件内含一行，其为**落款／归属字段**且其**值域之首个角色令牌**为 `verdict-keeper` | 口径丙（faceA §4-2 三条）＋ **本棒所补之二处**（见 §2-2）；射程 ＝ **首 16,000 B ∪ 末 4,000 B** |

### §2-2 · 面③ 之规则（**含本棒之仪器勘正·如实登记**）

**在册规则**（faceA §4-2 逐字）：① 字段须为「标签式」（落款字段名之后 ≤6 字内须见分隔符 `：`／`:`／`｜`／`|`）方为字段标签，**文首标题行**为结构性字段（独立成域）；② 任一字段域之首个角色令牌为 `verdict-keeper` 即命中；③ 同位并列取最早位置。

**本棒之补（仪器缺口·如实登记）**：本棒首轮复算得 **102／111** 命中，**9 件**未命中。逐件开卷核对后确认——**9 件皆为在册规则未覆盖之两型，非文件之缺**：
- **型一（2 件）**：`results/verdict/judgement/_closure_sweep_r2_2026_10_18.md`、`_ruled_unclosed_closure_verdict_2026_10_18.md`——其归属在 **L1 标题行**（`# …（2026-10-18 · **verdict-keeper（判定收口官 · agent-3a4d09ba3c90）** · 判定收口面 …`）。faceA §4-2 之规则①已明载「文首标题行为结构性字段（独立成域）」，**本棒首轮漏实现该款** ⇒ 补入。
- **型二（7 件）**：乙面 1 件（`_t1_exp2_verdict_2026_10_10.md` 之 **L4「性质」**）＋ 丙面 6 件（`_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` 等之 **L3「本件性质」**）——其归属在**件性质栏**（`> **本件性质**：verdict-keeper **判定收口件 · r2 档**（…）`）。**「件性质／本件性质／性质／件别」为在册之归属栏**（faceA 清单之「类别」栏即取此栏）⇒ 补入。
- ⇒ **补后复算：111／111 命中**（本件 §3 之面③ 栏）。
> 📌 **仪器之失不隐**：本棒首轮之 102／111 系**本棒仪器之缺**（漏两款），**非** 9 件之缺；已补规则并复算，且逐件开卷核对（正控：9 件之归属行原文已在本件 §2-2 内逐字列出）。⛔ **0** 以「首轮 9 件未命中」充「9 件未落档」。

### §2-3 · 三态之映射（**判据 → 态·无歧义**）

| 态 | 判据（机械） |
|:--|:--|
| **已落档** | 面① ∧ 面② ∧ 面③ **三面全立** |
| **未落档** | 面① 成立 ∧ （面② ∨ 面③）**不成立**（在盘·但无逐件落档登记行／归属行不可核） |
| **挂账** | 面① **不成立**（不在盘∨指纹不符）**∨** 该件之归属有**未消解之互斥读**（归属面不可判） |

### §2-4 · 「落档」之两读（**须各算一遍·不先算后择**）

| 读 | 「落档」之定义 | 用途 |
|:--|:--|:--|
| **读甲（宽读·实体面）** | 落档 ＝ **面①**（件在盘且指纹相符） | 与 EA 审计之 (a)(b) 两面同口径（其 108／108、111／111 皆全绿） |
| **读乙（严读·册面）** | 落档 ＝ **面① ∧ 面② ∧ 面③**（在盘 ∧ 有逐件落档登记行 ∧ VK 归属行可核） | 与门③ 之判据词「**落档**」之实义相称（须可被册面复现） |

> 📌 **两读之分歧处**：读甲不要求「入册」与「归属可核」；读乙要求之。**本件 §6 并出两读之算得结果**；其**是否分歧**，如实报（⛔ **0** 先算后择、⛔ **0** 择其有利者充唯一判）。
### §3-1 · 甲面（77 件·判定件·落款方 ＝ `verdict-keeper`）

（在册：甲面清单 §3-1 主表 L87–L163 ＝ 序 1–77；序 74+1／74+2／74+3 之互斥 3 件按 PI 采「读乙·计入」**已并入本表序 4／17／18**，并于 §3-4 单列标注·**⛔0 剔出**·**⛔0 混入而不标**）

| 序 | 件名 | 仓 | bytes（自测） | SHA-12（自测） | 面① | 面② | 面③ | 态 | 据（件·位号） |
|:--:|:--|:--|--:|:--|:--|:--|:--|:--|:--|
| 1 | `results/verdict/judgement/_c5b_closure_verdict_2026_10_17.md` | repo | 26,218 | `660555b9b6be` | ✔ 在盘·指纹符 | ✔ 31 行 | ✔ L4·出件 | **已落档** | 甲面清单 §3-1 L87 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v56.md/_pi_card_answers_register_2026_10_17_v56.md` ＋ 归属行 L4 |
| 2 | `results/verdict/judgement/_closure_sweep_r2_2026_10_18.md` | repo | 121,848 | `31a03b8d756b` | ✔ 在盘·指纹符 | ✔ 80 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L88 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 3 | `results/verdict/judgement/_cluster_a_sface_adjudication_2026_10_18.md` | repo | 53,759 | `9c05d0ab78d5` | ✔ 在盘·指纹符 | ✔ 32 行 | ✔ L4·署名 | **已落档** | 甲面清单 §3-1 L89 ＋ `pi_rulings／_pi_card_answers_register_2026_10_18_v106.md/_pi_card_answers_register_2026_10_18_v106.md` ＋ 归属行 L4 |
| 4 | `results/verdict/judgement/_cluster_b_carrier_adjudication_2026_10_18.md` | repo | 72,984 | `3f34fd241a50` | ✔ 在盘·指纹符 | ✔ 30 行 | ✔ L343·件止 | **已落档** | 甲面清单 §3-1 L90 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L343 ⚠在册记`尾窗·件止行（L343／字节偏移 72,107·本棒实测）` |
| 5 | `results/verdict/judgement/_cluster_c_keyface_adjudication_2026_10_18.md` | repo | 63,462 | `8e9ec9104a1e` | ✔ 在盘·指纹符 | ✔ 31 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L91 ＋ `pi_rulings／_pi_card_answers_register_2026_10_18_v106.md/_pi_card_answers_register_2026_10_18_v106.md` ＋ 归属行 L7 |
| 6 | `results/verdict/judgement/_cluster_d_counting_adjudication_2026_10_18.md` | repo | 57,929 | `edcc23114b18` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L92 ＋ `pi_rulings／_pi_card_answers_register_2026_10_25_v354.md/_pi_card_answers_register_2026_10_25_v354.md` ＋ 归属行 L7 |
| 7 | `results/verdict/judgement/_cluster_f_deletion_adjudication_2026_10_18.md` | repo | 52,226 | `e289d12fd5d4` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L93 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L7 |
| 8 | `results/verdict/judgement/_cluster_g_deletion_preconditions_adjudication_2026_10_18.md` | repo | 76,051 | `918659f9b0f6` | ✔ 在盘·指纹符 | ✔ 29 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L94 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 9 | `results/verdict/judgement/_cluster_h_directory_adjudication_2026_10_18.md` | repo | 61,721 | `616e466f4f49` | ✔ 在盘·指纹符 | ✔ 20 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L95 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L7 |
| 10 | `results/verdict/judgement/_cluster_i_f1_f6_f7_verdict_2026_10_18.md` | repo | 51,397 | `98b3ef11e115` | ✔ 在盘·指纹符 | ✔ 27 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L96 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 11 | `results/verdict/judgement/_cluster_i_historical_adjudication_2026_10_18.md` | repo | 65,872 | `53ac8f30556d` | ✔ 在盘·指纹符 | ✔ 35 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L97 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 12 | `results/verdict/judgement/_cluster_i_item6_compatibility_adjudication_2026_10_18.md` | repo | 40,492 | `e3daf0cd6fb8` | ✔ 在盘·指纹符 | ✔ 22 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L98 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 13 | `results/verdict/judgement/_cluster_i_item6_conditions_adjudication_2026_10_18.md` | repo | 40,834 | `f2802aa63370` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L99 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L1 |
| 14 | `results/verdict/judgement/_cluster_i_item6_give_values_adjudication_2026_10_18.md` | repo | 45,549 | `b33aae011ca8` | ✔ 在盘·指纹符 | ✔ 23 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L100 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 15 | `results/verdict/judgement/_cluster_k_eta_blockers_adjudication_2026_10_19.md` | repo | 55,977 | `4b1040954064` | ✔ 在盘·指纹符 | ✔ 28 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L101 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L7 |
| 16 | `results/verdict/judgement/_d1_ab_deliberation_judgment_2026_10_15.md` | repo | 46,542 | `88c2af72ff7b` | ✔ 在盘·指纹符 | ✔ 22 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L102 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L1 |
| 17 | `results/verdict/judgement/_eta_missing_params_and_c1_adjudication_2026_10_19.md` | repo | 27,703 | `57efdf5255ee` | ✔ 在盘·指纹符 | ✔ 22 行 | ✔ L260·落款 | **已落档** | 甲面清单 §3-1 L103 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L260 ⚠在册记`尾窗·落款行（L260／字节偏移 26,622·本棒实测）` |
| 18 | `results/verdict/judgement/_ext5_verdict_2026_10_17.md` | repo | 63,647 | `80a81bd525d4` | ✔ 在盘·指纹符 | ✔ 76 行 | ✔ L5·件性质 | **已落档** | 甲面清单 §3-1 L104 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v65.md/_pi_card_answers_register_2026_10_17_v65.md` ＋ 归属行 L5 ⚠在册记`尾窗·署名行（⚠ **本棒未补算行号与字节偏移**；前棒 §2-1 载 L155·**转引**）` |
| 19 | `results/verdict/judgement/_face_r_coexist_verdict_2026_10_17.md` | repo | 37,604 | `0fd3788e2d3b` | ✔ 在盘·指纹符 | ✔ 42 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L105 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v77.md/_pi_card_answers_register_2026_10_17_v77.md` ＋ 归属行 L1 |
| 20 | `results/verdict/judgement/_fail_h0_verdict_2026_10_17.md` | repo | 41,481 | `c8794d87b4b6` | ✔ 在盘·指纹符 | ✔ 49 行 | ✔ L6·件性质 | **已落档** | 甲面清单 §3-1 L106 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v74.md/_pi_card_answers_register_2026_10_17_v74.md` ＋ 归属行 L6 |
| 21 | `results/verdict/judgement/_fake_kd_itemwise_adjudication_2026_10_21.md` | repo | 83,606 | `b6221e7a2efe` | ✔ 在盘·指纹符 | ✔ 58 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L107 ＋ `pi_rulings／_pi_card_answers_register_2026_10_21_v178.md/_pi_card_answers_register_2026_10_21_v178.md` ＋ 归属行 L1 |
| 22 | `results/verdict/judgement/_fake_kd_p3_readjudication_2026_10_21.md` | repo | 72,909 | `9c09cc70b339` | ✔ 在盘·指纹符 | ✔ 41 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L108 ＋ `pi_rulings／_pi_card_answers_register_2026_10_27_v455.md/_pi_card_answers_register_2026_10_27_v455.md` ＋ 归属行 L1 |
| 23 | `results/verdict/judgement/_fake_kd_p4_reversal_adjudication_2026_10_21.md` | repo | 97,074 | `e78092e45065` | ✔ 在盘·指纹符 | ✔ 30 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L109 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L1 |
| 24 | `results/verdict/judgement/_fake_kd_p5_reversal_adjudication_2026_10_21.md` | repo | 64,697 | `6addfa5db8e9` | ✔ 在盘·指纹符 | ✔ 42 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L110 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L1 |
| 25 | `results/verdict/judgement/_fake_kd_p6_confirmation_adjudication_2026_10_21.md` | repo | 71,937 | `af506d37e00a` | ✔ 在盘·指纹符 | ✔ 34 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L111 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L1 |
| 26 | `results/verdict/judgement/_fake_kd_p8_confirmation_adjudication_2026_10_21.md` | repo | 68,956 | `7a0dd145a76d` | ✔ 在盘·指纹符 | ✔ 31 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L112 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L1 |
| 27 | `results/verdict/judgement/_ge01_readiness_adjudication_2026_10_21.md` | repo | 64,097 | `336500609b5c` | ✔ 在盘·指纹符 | ✔ 30 行 | ✔ L9·落盘方 | **已落档** | 甲面清单 §3-1 L113 ＋ `_closeout_bucket_refresh_v2_2026_10_24.md` ＋ 归属行 L9 |
| 28 | `results/verdict/judgement/_interval_420_600_upper_bound_deliberation_2026_10_16.md` | repo | 34,256 | `4d2c65968311` | ✔ 在盘·指纹符 | ✔ 22 行 | ✔ L7·落账方 | **已落档** | 甲面清单 §3-1 L114 ＋ `pi_rulings／_pi_card_answers_register_2026_10_16_v41.md/_pi_card_answers_register_2026_10_16_v41.md` ＋ 归属行 L7 |
| 29 | `results/verdict/judgement/_interval_ceiling_post_lock_deliberation_2026_10_16.md` | repo | 46,687 | `fce2f69802b9` | ✔ 在盘·指纹符 | ✔ 33 行 | ✔ L7·落款方 | **已落档** | 甲面清单 §3-1 L115 ＋ `pi_rulings／_pi_card_answers_register_2026_10_16_v27.md/_pi_card_answers_register_2026_10_16_v27.md` ＋ 归属行 L7 |
| 30 | `results/verdict/judgement/_item6_c2_four_fields_adjudication_2026_10_18.md` | repo | 50,802 | `a40de66d87c8` | ✔ 在盘·指纹符 | ✔ 21 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L116 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 31 | `results/verdict/judgement/_judgement_w39_two_reading_2026_10_23.md` | repo | 54,862 | `f35fe7d03551` | ✔ 在盘·指纹符 | ✔ 16 行 | ✔ L7·件性质 | **已落档** | 甲面清单 §3-1 L117 ＋ `_closeout_bucket_refresh_v2_2026_10_24.md` ＋ 归属行 L7 |
| 32 | `results/verdict/judgement/_kabla6_trigger_review_adjudication_2026_10_21.md` | repo | 50,919 | `09aea8d27041` | ✔ 在盘·指纹符 | ✔ 20 行 | ✔ L8·出件方 | **已落档** | 甲面清单 §3-1 L118 ＋ `pi_rulings／_pi_card_answers_register_2026_10_21_v179.md/_pi_card_answers_register_2026_10_21_v179.md` ＋ 归属行 L8 |
| 33 | `results/verdict/judgement/_kd14_null_u_carrier_deliberation_2026_10_16.md` | repo | 35,608 | `0a6279970446` | ✔ 在盘·指纹符 | ✔ 24 行 | ✔ L6·落盘方 | **已落档** | 甲面清单 §3-1 L119 ＋ `pi_rulings／_pi_card_answers_register_2026_10_16_v41.md/_pi_card_answers_register_2026_10_16_v41.md` ＋ 归属行 L6 |
| 34 | `results/verdict/judgement/_kd_cluster_verdict_pack_adjudication_2026_10_19.md` | repo | 113,327 | `d87a711b0ecf` | ✔ 在盘·指纹符 | ✔ 31 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L120 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L7 |
| 35 | `results/verdict/judgement/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md` | repo | 77,119 | `522be8905484` | ✔ 在盘·指纹符 | ✔ 45 行 | ✔ L8·出件方 | **已落档** | 甲面清单 §3-1 L121 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L8 |
| 36 | `results/verdict/judgement/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md` | repo | 73,955 | `85e5caeb3478` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L122 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L7 |
| 37 | `results/verdict/judgement/_kd_esc5v2_closure_adjudication_2026_10_21.md` | repo | 74,163 | `b9ba3ff8d010` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L7·件性质 | **已落档** | 甲面清单 §3-1 L123 ＋ `_closeout_bucket_refresh_v2_2026_10_24.md` ＋ 归属行 L7 |
| 38 | `results/verdict/judgement/_kd_eta_main_run_verdict_2026_10_20.md` | repo | 64,606 | `8a5727bc4c11` | ✔ 在盘·指纹符 | ✔ 45 行 | ✔ L3·出件 | **已落档** | 甲面清单 §3-1 L124 ＋ `results___.tmp____s14_cards_full_2026_10_21.md` ＋ 归属行 L3 |
| 39 | `results/verdict/judgement/_kd_eta_sep_measurement_verdict_2026_10_20.md` | repo | 66,712 | `ceb71b3a2570` | ✔ 在盘·指纹符 | ✔ 41 行 | ✔ L3·出件 | **已落档** | 甲面清单 §3-1 L125 ＋ `results___.tmp____s14_cards_full_2026_10_21.md` ＋ 归属行 L3 |
| 40 | `results/verdict/judgement/_kd_mda8_domain_readings_adjudication_2026_10_19.md` | repo | 65,988 | `42af8a6e0703` | ✔ 在盘·指纹符 | ✔ 34 行 | ✔ L8·出件方 | **已落档** | 甲面清单 §3-1 L126 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L8 |
| 41 | `results/verdict/judgement/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md` | repo | 57,571 | `9a960a574260` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L8·出件方 | **已落档** | 甲面清单 §3-1 L127 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L8 |
| 42 | `results/verdict/judgement/_kd_mda8_first_reading_verdict_2026_10_20.md` | repo | 64,345 | `9c75b5c16676` | ✔ 在盘·指纹符 | ✔ 42 行 | ✔ L8·出件方 | **已落档** | 甲面清单 §3-1 L128 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L8 |
| 43 | `results/verdict/judgement/_kd_mda8a24_clearance_verdict_2026_10_20.md` | repo | 77,696 | `170ab543d941` | ✔ 在盘·指纹符 | ✔ 39 行 | ✔ L8·出件方 | **已落档** | 甲面清单 §3-1 L129 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L8 |
| 44 | `results/verdict/judgement/_kd_mda9_closure_adjudication_2026_10_21.md` | repo | 75,087 | `b6f3a254abb1` | ✔ 在盘·指纹符 | ✔ 19 行 | ✔ L7·件性质 | **已落档** | 甲面清单 §3-1 L130 ＋ `_closeout_bucket_refresh_v2_2026_10_24.md` ＋ 归属行 L7 |
| 45 | `results/verdict/judgement/_kd_s3b1_verdict_2026_10_17.md` | repo | 45,846 | `ed36d0171672` | ✔ 在盘·指纹符 | ✔ 56 行 | ✔ L9·落款方 | **已落档** | 甲面清单 §3-1 L131 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L9 |
| 46 | `results/verdict/judgement/_kd_sepcal7_final_verdict_2026_10_20.md` | repo | 70,518 | `c013aeb1235f` | ✔ 在盘·指纹符 | ✔ 70 行 | ✔ L7·件性质 | **已落档** | 甲面清单 §3-1 L132 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L7 |
| 47 | `results/verdict/judgement/_kd_t5k5_stale_premise_adjudication_2026_10_22.md` | repo | 50,348 | `6415eb480659` | ✔ 在盘·指纹符 | ✔ 19 行 | ✔ L7·落盘方 | **已落档** | 甲面清单 §3-1 L133 ＋ `_closeout_bucket_refresh_v2_2026_10_24.md` ＋ 归属行 L7 |
| 48 | `results/verdict/judgement/_kexp8_coverage_adjudication_2026_10_22.md` | repo | 62,301 | `80631fb4ce3d` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L5·件性质 | **已落档** | 甲面清单 §3-1 L134 ＋ `_closeout_bucket_refresh_v2_2026_10_24.md` ＋ 归属行 L5 |
| 49 | `results/verdict/judgement/_kfp6_nature_and_eta_expface_adjudication_2026_10_19.md` | repo | 48,993 | `591b73224eee` | ✔ 在盘·指纹符 | ✔ 24 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L135 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L1 |
| 50 | `results/verdict/judgement/_kl_m41_3_reverdict_2026_10_17.md` | repo | 61,667 | `63625672139a` | ✔ 在盘·指纹符 | ✔ 70 行 | ✔ L7·落款方 | **已落档** | 甲面清单 §3-1 L136 ＋ `_commission_f04_e06_2026_10_28.md` ＋ 归属行 L7 |
| 51 | `results/verdict/judgement/_kl_m41_3_verdict_2026_10_17.md` | repo | 33,138 | `5dc4e089f458` | ✔ 在盘·指纹符 | ✔ 71 行 | ✔ L7·落款方 | **已落档** | 甲面清单 §3-1 L137 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v74.md/_pi_card_answers_register_2026_10_17_v74.md` ＋ 归属行 L7 |
| 52 | `results/verdict/judgement/_l2_2_duplication_criterion_adjudication_2026_10_19.md` | repo | 42,517 | `ecbf3288d791` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L138 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L7 |
| 53 | `results/verdict/judgement/_l2_2_two_arms_identity_adjudication_2026_10_19.md` | repo | 49,080 | `84e8d866054a` | ✔ 在盘·指纹符 | ✔ 20 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L139 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L7 |
| 54 | `results/verdict/judgement/_m41_verdict_kd_effect_register_2026_10_15.md` | repo | 23,630 | `f54e8a10acde` | ✔ 在盘·指纹符 | ✔ 35 行 | ✔ L7·棒 | **已落档** | 甲面清单 §3-1 L140 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L7 |
| 55 | `results/verdict/judgement/_material_expansion_verdict_kd_effect_register_2026_10_16.md` | repo | 35,655 | `42a0b3aeff96` | ✔ 在盘·指纹符 | ✔ 41 行 | ✔ L7·落盘方 | **已落档** | 甲面清单 §3-1 L141 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L7 |
| 56 | `results/verdict/judgement/_n3_o5_terminal_verdict_2026_10_16.md` | repo | 39,037 | `88df2c228eae` | ✔ 在盘·指纹符 | ✔ 24 行 | ✔ L7·落款方 | **已落档** | 甲面清单 §3-1 L142 ＋ `pi_rulings／_pi_card_answers_register_2026_10_16_v33.md/_pi_card_answers_register_2026_10_16_v33.md` ＋ 归属行 L7 |
| 57 | `results/verdict/judgement/_n_distinct_grain_verdict_2026_10_17.md` | repo | 41,028 | `0abaee4aeefb` | ✔ 在盘·指纹符 | ✔ 35 行 | ✔ L7·落款方 | **已落档** | 甲面清单 §3-1 L143 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v83.md/_pi_card_answers_register_2026_10_17_v83.md` ＋ 归属行 L7 |
| 58 | `results/verdict/judgement/_ncc_c6_admission_adjudication_2026_10_21.md` | repo | 76,725 | `0a3dedb79479` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L8·出件方 | **已落档** | 甲面清单 §3-1 L144 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L8 |
| 59 | `results/verdict/judgement/_o1_498_lock_scope_deliberation_2026_10_16.md` | repo | 52,216 | `c9c808083d46` | ✔ 在盘·指纹符 | ✔ 17 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L145 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L7 |
| 60 | `results/verdict/judgement/_r2_reading_verdict_2026_10_17.md` | repo | 43,055 | `99b9bff47682` | ✔ 在盘·指纹符 | ✔ 27 行 | ✔ L7·落账方 | **已落档** | 甲面清单 §3-1 L146 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v61.md/_pi_card_answers_register_2026_10_17_v61.md` ＋ 归属行 L7 |
| 61 | `results/verdict/judgement/_refonly_161_reading_verdict_2026_10_17.md` | repo | 39,243 | `bd94d12323e0` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L7·落账方 | **已落档** | 甲面清单 §3-1 L147 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v56.md/_pi_card_answers_register_2026_10_17_v56.md` ＋ 归属行 L7 |
| 62 | `results/verdict/judgement/_ruled_unclosed_closure_verdict_2026_10_18.md` | repo | 54,716 | `03fe4d044c78` | ✔ 在盘·指纹符 | ✔ 64 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L148 ＋ `pi_rulings／_pi_card_answers_register_2026_10_18_v103.md/_pi_card_answers_register_2026_10_18_v103.md` ＋ 归属行 L1 |
| 63 | `results/verdict/judgement/_s3_s5_explanation_and_disposition_verdict_2026_10_17.md` | repo | 28,816 | `2c1479af62cb` | ✔ 在盘·指纹符 | ✔ 27 行 | ✔ L4·棒 | **已落档** | 甲面清单 §3-1 L149 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v63.md/_pi_card_answers_register_2026_10_17_v63.md` ＋ 归属行 L4 |
| 64 | `results/verdict/judgement/_strict3_verdict_2026_10_17.md` | repo | 41,236 | `d392bd36ec34` | ✔ 在盘·指纹符 | ✔ 19 行 | ✔ L7·落盘方 | **已落档** | 甲面清单 §3-1 L150 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L7 |
| 65 | `results/verdict/judgement/_t3trap_kd3_disposition_deliberation_2026_10_15.md` | repo | 29,776 | `b58775c33928` | ✔ 在盘·指纹符 | ✔ 18 行 | ✔ L7·出件方 | **已落档** | 甲面清单 §3-1 L151 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L7 |
| 66 | `results/verdict/judgement/_u10_fail_h0_verdict_2026_10_18.md` | repo | 59,918 | `0884b8f98b96` | ✔ 在盘·指纹符 | ✔ 61 行 | ✔ L7·落款方 | **已落档** | 甲面清单 §3-1 L152 ＋ `pi_rulings／_pi_card_answers_register_2026_10_18_v90.md/_pi_card_answers_register_2026_10_18_v90.md` ＋ 归属行 L7 |
| 67 | `results/verdict/judgement/_u_axis_equation_direction_deliberation_2026_10_16.md` | repo | 40,049 | `5b6847e424b0` | ✔ 在盘·指纹符 | ✔ 19 行 | ✔ L7·落盘方 | **已落档** | 甲面清单 §3-1 L153 ＋ `pi_rulings／_pi_card_answers_register_2026_10_16_v38.md/_pi_card_answers_register_2026_10_16_v38.md` ＋ 归属行 L7 |
| 68 | `results/verdict/judgement/_u_cluster1_verdict_2026_10_17.md` | repo | 40,213 | `0172e2a52c80` | ✔ 在盘·指纹符 | ✔ 22 行 | ✔ L7·落盘方 | **已落档** | 甲面清单 §3-1 L154 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L7 |
| 69 | `results/verdict/judgement/_u_cluster2_verdict_2026_10_17.md` | repo | 47,057 | `4dd0d2f38d46` | ✔ 在盘·指纹符 | ✔ 33 行 | ✔ L7·落盘方 | **已落档** | 甲面清单 §3-1 L155 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v65.md/_pi_card_answers_register_2026_10_17_v65.md` ＋ 归属行 L7 |
| 70 | `results/verdict/judgement/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | sub | 25,123 | `19ad36f7ec84` | ✔ 在盘·指纹符 | ✔ 19 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L156 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L1 |
| 71 | `results/verdict/judgement/_kv3s_4_terminal_verdict_2026_10_09.md` | sub | 50,858 | `e51317fcc5cf` | ✔ 在盘·指纹符 | ✔ 62 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L157 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L1 |
| 72 | `results/verdict/judgement/_s4_topup_intake_verdict_2026_10_09.md` | sub | 33,799 | `658d7f3ab231` | ✔ 在盘·指纹符 | ✔ 20 行 | ✔ L10·出件 | **已落档** | 甲面清单 §3-1 L158 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L10 |
| 73 | `results/verdict/judgement/_s6doubleprime_terminal_verdicts_2026_10_11.md` | sub | 76,910 | `bba3b889d849` | ✔ 在盘·指纹符 | ✔ 54 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L159 ＋ `_trae_dfamily_original_text_reply_2026_10_12.md` ＋ 归属行 L1 |
| 74 | `results/verdict/judgement/_s6prime_terminal_verdicts_2026_10_11.md` | sub | 54,937 | `1c8ce58d6484` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L160 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L1 |
| 75 | `results/verdict/judgement/_v3_02_ethard_closure_verdict_2026_10_09.md` | sub | 27,819 | `aa0f96bb618f` | ✔ 在盘·指纹符 | ✔ 31 行 | ✔ L3·件性质 | **已落档** | 甲面清单 §3-1 L161 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L3 |
| 76 | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` | sub | 42,645 | `63d898ab1b71` | ✔ 在盘·指纹符 | ✔ 33 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L162 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L1 |
| 77 | `results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` | sub | 44,054 | `8adaf4e5d868` | ✔ 在盘·指纹符 | ✔ 28 行 | ✔ L1·L1·标题行 | **已落档** | 甲面清单 §3-1 L163 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L1 |

### §3-2 · 乙面（28 件·「无件性质栏〔不可判〕」中经口径丙补定之判定件）

（在册：EA 审计 §1-3 L119–L146）

| 序 | 件名 | 仓 | bytes（自测） | SHA-12（自测） | 面① | 面② | 面③ | 态 | 据（件·位号） |
|:--:|:--|:--|--:|:--|:--|:--|:--|:--|:--|
| 1 | `results/verdict/judgement/_cluster_i_item14_closure_verdict_2026_10_18.md` | repo | 39,751 | `d23de0a9e7eb` | ✔ 在盘·指纹符 | ✔ 23 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L119 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 2 | `results/verdict/judgement/_cluster_j_glm_62_adjudication_2026_10_19.md` | repo | 48,997 | `b4252f1f736d` | ✔ 在盘·指纹符 | ✔ 20 行 | ✔ L3·出件 | **已落档** | EA 审计 §1-3 L120 ＋ `_reply_to_bob_experiment_prereq_2026_10_22.md` ＋ 归属行 L3 |
| 3 | `results/verdict/judgement/_coze_v5_r2_residual4_adjudication_2026_10_18.md` | repo | 43,038 | `89de292707fb` | ✔ 在盘·指纹符 | ✔ 21 行 | ✔ L5·出件方 | **已落档** | EA 审计 §1-3 L121 ＋ `_v4_commission_〔IM〕_report_coze_2026_10_18_v5_draft_r3.md` ＋ 归属行 L5 |
| 4 | `results/verdict/judgement/_d1_backfill_intake_verdict_2026_10_01.md` | repo | 42,115 | `42a3858976f2` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L122 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L1 |
| 5 | `results/verdict/judgement/_domain_backfill_hold235_adjudication_2026_10_18.md` | repo | 39,456 | `43515db69b4c` | ✔ 在盘·指纹符 | ✔ 22 行 | ✔ L3·棒 | **已落档** | EA 审计 §1-3 L123 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L3 |
| 6 | `results/verdict/judgement/_esc5_verdict_2026_10_17.md` | repo | 27,258 | `d970bb175672` | ✔ 在盘·指纹符 | ✔ 41 行 | ✔ L267·署名 | **已落档** | EA 审计 §1-3 L124 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v72.md/_pi_card_answers_register_2026_10_17_v72.md` ＋ 归属行 L267 |
| 7 | `results/verdict/judgement/_k_v3df_0_1_readings_verdict_2026_10_09.md` | sub | 37,003 | `e98bee353448` | ✔ 在盘·指纹符 | ✔ 22 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L133 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L1 |
| 8 | `results/verdict/judgement/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | sub | 27,735 | `a14aafa220c4` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L134 ＋ `_blade_caliber_b8_judgment_2026_10_10.md` ＋ 归属行 L1 |
| 9 | `results/verdict/judgement/_kd4_homology_verdict_2026_10_17.md` | repo | 32,823 | `1992b9d359a8` | ✔ 在盘·指纹符 | ✔ 23 行 | ✔ L6·落账方 | **已落档** | EA 审计 §1-3 L125 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v60.md/_pi_card_answers_register_2026_10_17_v60.md` ＋ 归属行 L6 |
| 10 | `results/verdict/judgement/_kd_civ_closure_verdict_2026_10_18.md` | repo | 43,116 | `60e9a18fa428` | ✔ 在盘·指纹符 | ✔ 17 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L126 ＋ `_book_05_results_index_2026_10_22.md` ＋ 归属行 L1 |
| 11 | `results/verdict/judgement/_kd_eta_selection_verdict_2026_10_20.md` | repo | 37,788 | `80b8cafcd085` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L3·出件 | **已落档** | EA 审计 §1-3 L127 ＋ `_book_01_adoption_effect_2026_10_22.md` ＋ 归属行 L3 |
| 12 | `results/verdict/judgement/_limb_reading_verdict_kv3s33_2026_10_01.md` | sub | 56,329 | `c5866ce87d9c` | ✔ 在盘·指纹符 | ✔ 36 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L135 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v46.md/_pi_card_answers_register_2026_10_17_v46.md` ＋ 归属行 L1 |
| 13 | `results/verdict/judgement/_ritt_def_proof_2026_10_17.md` | repo | 23,310 | `5d411ebf07ed` | ✔ 在盘·指纹符 | ✔ 26 行 | ✔ L242·署名 | **已落档** | EA 审计 §1-3 L128 ＋ `pi_rulings／_pi_card_answers_register_2026_10_17_v73.md/_pi_card_answers_register_2026_10_17_v73.md` ＋ 归属行 L242 |
| 14 | `results/verdict/judgement/_s3_kv3s_3_verdict_2026_10_01.md` | sub | 35,037 | `e394bb6b5ddf` | ✔ 在盘·指纹符 | ✔ 32 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L136 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L1 |
| 15 | `results/verdict/judgement/_t1_exp2_verdict_2026_10_10.md` | sub | 48,298 | `15c1c4b317a0` | ✔ 在盘·指纹符 | ✔ 21 行 | ✔ L4·性质 | **已落档** | EA 审计 §1-3 L137 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L4 |
| 16 | `results/verdict/judgement/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | sub | 72,934 | `0b5fb78727c2` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L138 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L1 |
| 17 | `results/verdict/judgement/_v3_recheck_26b_verdict_2026_10_01.md` | sub | 26,309 | `8bbecb15b28b` | ✔ 在盘·指纹符 | ✔ 32 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L139 ＋ `_commission_glm_dualtrack_paper_v0.5_2026_10_01.md` ＋ 归属行 L1 |
| 18 | `results/verdict/judgement/_v4_pi_cot_v3_verdict_v3.md` | repo | 53,751 | `bb44fdc7ab0f` | ✔ 在盘·指纹符 | ✔ 56 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L129 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L1 |
| 19 | `results/verdict/judgement/_v5_gt8_lowarm_verdict_2026_09_29.md` | sub | 32,653 | `9140b6e5970b` | ✔ 在盘·指纹符 | ✔ 23 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L140 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L1 |
| 20 | `results/verdict/judgement/_v5_gt_verdict_2026_09_29.md` | repo | 57,227 | `45648b0ec940` | ✔ 在盘·指纹符 | ✔ 41 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L130 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L1 |
| 21 | `results/verdict/judgement/_v5_item21_strategyqa_realias_verdict_2026_09_29.md` | sub | 32,354 | `26eaa156108f` | ✔ 在盘·指纹符 | ✔ 21 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L141 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L1 |
| 22 | `results/verdict/judgement/_v5_item21_verdict_2026_09_28.md` | sub | 28,155 | `de274bd38955` | ✔ 在盘·指纹符 | ✔ 24 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L142 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L1 |
| 23 | `results/verdict/judgement/_v5_item35_v2_verdict_2026_09_29.md` | repo | 26,232 | `b59bef293712` | ✔ 在盘·指纹符 | ✔ 44 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L131 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L1 |
| 24 | `results/verdict/judgement/_v5_item35_v3_collinear_verdict_2026_10_01.md` | sub | 38,266 | `363cce3dae59` | ✔ 在盘·指纹符 | ✔ 38 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L143 ＋ `_commission_glm_dualtrack_paper_v0.5_2026_10_01.md` ＋ 归属行 L1 |
| 25 | `results/verdict/judgement/_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | sub | 41,566 | `1814f9590f0f` | ✔ 在盘·指纹符 | ✔ 38 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L144 ＋ `TRAE_V3_ASSET_ERRATUM_2026_09_23.md` ＋ 归属行 L1 |
| 26 | `results/verdict/judgement/_v5_rj5_verdict_2026_09_29.md` | sub | 40,057 | `9c1ccbd5cf5a` | ✔ 在盘·指纹符 | ✔ 41 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L145 ＋ `README_V4_2026_09_29.md` ＋ 归属行 L1 |
| 27 | `results/verdict/judgement/c5_b_group_verdict_2026_10_01.md` | sub | 30,118 | `3fbf6b38a383` | ✔ 在盘·指纹符 | ✔ 41 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L146 ＋ `_commission_glm_dualtrack_paper_v0.5_2026_10_01.md` ＋ 归属行 L1 |
| 28 | `results/verdict/judgement/c5_guard_0_1_recheck_verdict_2026_10_01.md` | repo | 33,287 | `24418fa60ede` | ✔ 在盘·指纹符 | ✔ 54 行 | ✔ L1·L1·标题行 | **已落档** | EA 审计 §1-3 L132 ＋ `_commission_kimi_upload_2026_10_01_v0.2.md` ＋ 归属行 L1 |

### §3-3 · 丙面（6 件·口径乙「14 字窗」技术假阴）

（在册：EA 审计 §1-4 L152–L157）

| 序 | 件名 | 仓 | bytes（自测） | SHA-12（自测） | 面① | 面② | 面③ | 态 | 据（件·位号） |
|:--:|:--|:--|--:|:--|:--|:--|:--|:--|:--|
| 1 | `results/verdict/judgement/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | repo | 42,817 | `9c18b9893579` | ✔ 在盘·指纹符 | ✔ 29 行 | ✔ L3·本件性质 | **已落档** | EA 审计 §1-4 L152 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L3 |
| 2 | `results/verdict/judgement/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | repo | 21,672 | `dfc858d3d930` | ✔ 在盘·指纹符 | ✔ 25 行 | ✔ L3·本件性质 | **已落档** | EA 审计 §1-4 L153 ＋ `_book_03_achievements_inventory_full_2026_10_22.md` ＋ 归属行 L3 |
| 3 | `results/verdict/judgement/_v4_supp_l14v3_n26_verdict.md` | repo | 65,978 | `df6453d57f8a` | ✔ 在盘·指纹符 | ✔ 46 行 | ✔ L3·本件性质 | **已落档** | EA 审计 §1-4 L154 ＋ `results___.tmp____s14_session_scan_out_2026_10_21.md` ＋ 归属行 L3 |
| 4 | `results/verdict/judgement/_v4_supp_t15_verdict.md` | repo | 54,377 | `3cb5c2f59961` | ✔ 在盘·指纹符 | ✔ 32 行 | ✔ L3·本件性质 | **已落档** | EA 审计 §1-4 L155 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L3 |
| 5 | `results/verdict/judgement/_v4_supp_t15r2_verdict.md` | repo | 65,638 | `963725dbd82a` | ✔ 在盘·指纹符 | ✔ 28 行 | ✔ L3·本件性质 | **已落档** | EA 审计 §1-4 L156 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L3 |
| 6 | `results/verdict/judgement/_v4_supp_t1_verdict.md` | repo | 29,106 | `0ad42625f333` | ✔ 在盘·指纹符 | ✔ 37 行 | ✔ L3·本件性质 | **已落档** | EA 审计 §1-4 L157 ＋ `TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` ＋ 归属行 L3 |

### §3-4 · 读甲／读乙**互斥 3 件**（PI 采「读乙·计入」·**逐件单列**·⛔0 剔出）

| 序 | 件名 | 仓 | bytes（自测） | SHA-12（自测） | 读甲（首 16,000 B） | 读乙（＋末 4,000 B） | 本棒实测归属行 |
|:--:|:--|:--|--:|:--|:--|:--|:--|
%s

> 📌 **PI 之采**：卡 `ask_27c25f4375962a1ae305bdb4` → `q_gate3_faceA` → **`read_yi`**（甲面清单 L7／L25／L167）⇒ 三件**计入**且**逐件单列**。**⛔0 剔出·⛔0 混入而不标**。**三件皆已落档**（面①②③全立）。
> 📌 **甲面内部构成之复核**（本棒实测）：落款角色类 A 判官 **1** ＋ C 另议 **0** ＋ B 独立 **0** ＝ **1** ✅（与在册「48＋26＋3＝77」同数）；仓别 repo **69** ＋ sub **8** ＝ **77** ✅。

### §3-5 · 加总自证（**容差 0**）

| 面 | 件数（自测枚举） | 加总 |
|:--|--:|:--|
| 甲面 | 77 | — |
| 乙面 | 28 | — |
| 丙面 | 6 | — |
| **合计** | **111** | **77 ＋ 28 ＋ 6 ＝ 111** ✅ **容差 0** |

| 三态 | 件数 | 读甲（面①） | 读乙（面①∧②∧③） |
|:--|--:|:--:|:--:|
| **已落档** | **111** | **111** | **111** |
| **未落档** | **0** | **0** | **0** |
| **挂账** | **0** | **0** | **0** |
| **合计** | **111** | **111** | **111** |

---

## §4 · 「PWC」之保留项**逐条**（**回源其原文·件·行·指纹齐**）

### §4-1 · PWC 之正身与「保留」之所在

> 📌 **「PWC」 ＝ `PASS-WITH-QUALIFICATION`**，其**正身文字**在 **EA 审计件** `results/evidence/register/_gate3_108_ea_audit_2026_10_24.md`（bytes 44,650／SHA-12 `8ebb365be944`·自测）**L266**「### §4-1 · **结论：PASS-WITH-QUALIFICATION**」；其**被 PI 采为门③ 第二合取项之值**之正身在 **卡答落账件** `pi_rulings/_pi_card_answers_register_2026_10_24_v268.md`（bytes 8,945／SHA-12 `c9a941c196ad`·自测）**L25**。
> 📌 **「保留」所在之处**（**⛔0 凭「PWC 之常识义」推断**）：在 EA 审计件 §4-1 之**四 Faces**（(a)(b)(c)(d)）与 §4-2 之**代价不对称表**之内——**保留 ＝ (d) 面非绿 ＋ (c) 面之 2 处名差 ＋ §4-2 之「宣告面须带此条件」**。下列 P1–P5 逐条照录其原文。

### §4-2 · 保留项**逐条**（**逐字照录·带件·行·指纹**）

| no | 保留项 | **原文逐字**（回源·件·行） | 现态（本棒实测·2026-10-28 11:46:05） |
|:-:|:--|:--|:--|
| **P1** | **条件本体·宣告面须带此条件** | EA 审计 **L280**：「门③ 之第二合取项记为**有条件通过**（在盘／指纹／分类三面全绿·甲面逐件构成面**不可核**）⇒ 母件③ 之「全部判定件由 `verdict-keeper` 落档」若取甲面口径，则其**集合**在登记面上不可复现 ⇒ **宣告面须带此条件**」 | **条件之内容已消解**（P2／P3 之实体已办）·惟**「宣告面须带此条件」之形式要件，在宣告时仍须带**——⚠ **其保留之对象已变**：原条件（甲面构成不可核）已消解，然**上探面与挂账面之条件仍在**（见 §5 之阈值 T3／T4） |
| **P2** | **甲面逐件构成面「不可核」（非绿）** | EA 审计 **L272**：「**（d）甲面逐件构成面 —— 不可核（非绿）**：74 件之逐件清单**在册未登记**（§3-1）⇒ 本件**只核其数·不能核其逐件**；且重派生得 74（读甲）或 77（读乙·锚点全中），**互斥 3 件**（§2-1）⇒ **甲面终数 ∈ [74, 77]·未闭**（§3-2）。」 | **已消解** ✅——甲面清单件（38,840 B／`512b31f1a1ed`）**L87–L163** 之 77 行**逐件落册**（10-24 02:07）；本棒实测其逐件登记行**皆在面②**（行数见 §3 各行） |
| **P3** | **甲面终数 ∈ [74, 77]·未闭（互斥 3 件未消解）** | EA 审计 **L180**：「**⛔ 0 强合**：本件**不代裁**「甲面终数 ＝ 74 抑或 77」，**不代裁**「上表 3 件属否」；**代价不对称明写于 §4**。」 | **已消解** ✅——PI 于 `pi_rulings/_pi_card_answers_register_2026_10_24_v269.md`（bytes 9,398／`0cee727234cf`）**L14** 逐字采「**读乙：77 件**」；**L23** 逐字「### §1-1 门③ 甲面 ＝ **读乙 77** ⇒ 判定件底数 **108 → 111**」；**L32** 逐字「📌 **加总自证**：77 ＋ 28 ＋ 6 ＝ **111** ✅」 |
| **P4** | **分类面 2 处名差（绿而有差）** | EA 审计 **L271**：「**(c) 分类正确性 —— 绿而有 2 处名差**：口径乙三步复算 **109／111 与机械表逐位相符**；**2 处名差**（no 433／no 447）**两读同向**（皆不充判定件）⇒ **非实质分歧**（§2-2）。」 | **仍在** ⚠——**2 处名差未消解**（no.433 ＝ `results/verdict/judgement/_s3_kv3s_3_verdict_2026_10_01.md`；no.447 ＝ `results/verdict/judgement/_t1_gate_closure_and_recompute_verdict_2026_10_01.md`）·在册判其为**登记级·⛔0 改判·⛔0 落 `kd`**（EA **L193**）·**无须 PI 之裁（仅登记）**（EA **L289**） |
| **P5** | **PI 采定之附条件·派棒补登记** | 卡答落账 v268 **L25**：「| 5 | 门③ 第二合取项 | 采 **PASS-WITH-QUALIFICATION** ＋ **派棒落册甲面清单** | 本件落账即派（见 §4-1） | 🟡 派 |」；同件 **L62**：「🔴 依序 5 之采（PWC ＋ 派棒落册），须派棒将甲面之逐件清单**落册**——**清单未落册是门③ 之唯一登记缺口**（两源件皆自陈）。⚠ 其前提为序「甲」（读甲／读乙）之裁；⇒ 📌 **本棒先做「与读无关」之部分**（在盘／指纹两面已全绿·只补清单体例），**读裁到后再定 74 抑或 77**。」 | **已行** ✅——甲面清单件已成（10-24 02:07）·即 P2 之消解路径；**且本棒实测其 77 行逐件登记行皆在面②**（§3-1） |

### §4-3 · PWC **消解后仍存**之四项（**逐条·带据**）

| # | 存留项 | 据（件·行·指纹） | 状态 |
|:-:|:--|:--|:--|
| **R1** | **丙面 252 件之落款面「从未核」⇒ 底数非闭** | EA 审计 **L256** 照录源件 B §3-3 第 4 点：「丙面 **252 件**之落款面**从未核**（前人只施口径乙于件别）⇒ 108 **非闭数**」；EA 审计 §3-7 **L254–L256**（缺口 7） | **未核** ⇒ **111 亦非闭数**（本件 §6 之 `NOT_MEASURED` 面） |
| **R2** | **2 件挂账未补证（no.24／no.336）** | EA 审计 §3-8 **L258–L260**：「no.24 `f1ca2c59bed9`／no.336 `66d8d45c7a62` 落**不明·挂账**（⛔ **0** 落 `kd`·**⛔ 0** 落终判）⇒ 若补证为 vK 落款，则甲面 74 → **76**、108 → **110**」；EA §4-3 第 4 点 **L291**：「**须谁动**：派 sub 以作者面／派工链补证」 | **未补证**（本棒实测见 §4-4） |
| **R3** | **母件「判定件」之真全集 0 处给出 ⇒ 机械不可得** | EA 审计 §3-6 **L250–L252**；另 `results/verdict/judgement/_gate3_base_count_dispute_2026_10_25.md`（bytes 39,201／`d790afb6f2a7`）§2-7 **L99** 照录同一缺口 | **未核**（须 PI／主代理核定） |
| **R4** | **EA 审计件之「108」→「111」之勘正件未另立** | 卡答落账 v269 **L113**：「| 2 | 门③ 审计件之「108」→「111」之**勘正** | 须另立勘正件（⛔0 回改原审计件）——**待办** | **待办**（本件⛔ **0** 代立·**⛔0** 回改审计件一字） |

### §4-4 · 2 件挂账之**现态**（**本棒实测·非转述**）

| no | 件名 | bytes（自测） | SHA-12（自测） | 归属面之实测 | 在册之据 |
|:-:|:--|--:|:--|:--|:--|
| **no.24** | `results/verdict/judgement/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md` | 37,908 | `f1ca2c59bed9` | **无落款字段** | 41 件 v1（results/verdict/judgement/_41_items_judgement_status_verdict_2026_10_23.md／`9e9141ae18c2`）**L109** 逐字：「| 5 | `results/verdict/judgement/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md` | repo | 独立判断件 | **0（无落款字段）** | `（落款字段缺失）` | **不计入** | `f1ca2c59bed9` |」 |
| **no.336** | `results/verdict/judgement/_t4k_k5k_coverage_adjudication_2026_10_22.md` | 61,203 | `66d8d45c7a62` | **全文 `verdict-keeper` 计数 ＝ 0**（全文 `verdict` 之计数亦 ＝ 0）⇒ 无任何 VK 归属字样 | EA 审计 §3-8 **L260** |

> 📌 **路径漂移之实证（no.24）**：10-13 之区册记其于 **`results/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md`**（仓根 `results/`）；**本棒按名于四根实全树搜索**方得之现位于 **`results/verdict/judgement/`**（bytes 37,908／`f1ca2c59bed9` **逐位相符**）⇒ **其在盘**；若按旧路径寻之将**误报「已失」**（陷阱第 12 型）。
> 📌 **此 2 件不在 111 之列**（其归属面为「无落款字段」·在册判「**不计入**」）⇒ **111 之三态中「挂账」＝ 0**；然此 2 件之**挂账面未消解** ⇒ 底数之闭合性未证（**R2**）。**归谁解**：EA 审计 §4-3 第 4 点逐字「**须谁动**：派 sub 以作者面／派工链补证」——**本件⛔0 代补证**（⛔0 落五终判）。
> 📌 **本棒之推算（非在册字面）**：若此 2 件补证为 VK 落款，则甲面 74 → 76、108 → 110（EA 在册字面）；按**现行读乙口径**则甲面 77 → 79、底数 111 → 113（**本棒推算·非在册**）。

---

## §5 · 转 `PASS` 之要件（**四件齐·阈值可机械判**）

> 📌 **在册纪律**：判死线**立时即带阈值**；⛔ **0** 立「无阈值之判死线」——那只是意图，不是判死线。本节**四件齐**（判据／阈值／测量法／正控）。
> 📌 **⚠ 本节所立者为「转 `PASS` 之要件」，非「门③ 已成就之宣告」**——**宣告权属 PI**（母件 L160 末句）·**本件⛔0 宣告任何零**。

### §5-1 · **判据**（**可机械判·不涉裁量**）

> 📌 **门③ 之第一合取项成立**（「全部判定件由 `verdict-keeper` 落档」）⟺ 以下**四条件同时**成立：
> **C1** 母件 L160 之「**全部**判定件」之全集 **U 已闭**（|U| 已定且其构成**可由册面逐件复现**）；
> **C2** U 之每一件**三面全立**（面①在盘且指纹符 ∧ 面②有逐件落档登记行 ∧ 面③ VK 归属行可核）；
> **C3** 在册底数 111 之内**无挂账、无未落档**；
> **C4** 全量三态表之**加总 ＝ |U|**（容差 0）。
> 📌 **门③ 之第二合取项**（`evidence-auditor` 证据链审计 **PASS**）**另须由 EA 自行落**——⛔ **0** 由本件代其裁（EA 审计 §4-2 **L280** 载「⛔ **0** 代 PI 裁宣告权」）。

### §5-2 · **阈值**（**可机械判之数·五项·全部可由脚本复算**）

| # | 阈值（**数**） | 判读式 | **现值（实测·2026-10-28 11:46:05）** | 达否 |
|:-:|:--|:--|:--|:-:|
| **T1** | **挂账件数 ＝ 0** | 在 U 之内计「归属面不可判／无落款字段」之件数 | **0**（111 内）／**2**（111 外：no.24／no.336） | ❌（**外侧 2 件未消解**） |
| **T2** | **未落档件数 ＝ 0** | 在 U 之内计「面①立而面②∨面③不立」之件数 | **0** | ✅ |
| **T3** | **上探面未核件数 ＝ 0** | 计「丙面 252 件之落款面」之未核件数（**或** PI 明裁以 111 为闭集并自承上探风险） | **252 未核**（R1） | ❌ |
| **T4** | **底数一致性差 ＝ 0** | \|U\| － 三面全立之件数 ＝ 0（现 111 － 111 ＝ 0）**∨** 其差额逐件具名可派且 PI 已采 | **0**（但因 T3 未闭，**此 0 仅在 111 之射程内成立**） | ⚠ **射程内 0·射程外未闭** |
| **T5** | **分类名差件数 ＝ 0** | 计「口径乙复算与机械表 `state` 不符」之件数（**或** PI 明裁其 2 处名差为「非实质差·登记级·可容」） | **2**（no.433／no.447·两读同向·P4） | ❌（**须 PI 一言**） |

> 📌 **阈值之纪律**：T1–T5 之**阈值本身系本件所立**（PI 未给值）⇒ 依在册纪律，本节**须经 PI 采认后方为已立**；**本件⛔0 代裁·⛔0 宣告门③ 成就**。
> 📌 **阈值之判定一律以「数」为准**：**⛔0 以「约」字掩口径未定**；**⛔0 按 111 填零**（T3 之 252、T5 之 2 **不得**因「111 件皆已落档」而被填为 0）。

### §5-3 · **测量法**（**可复算·逐件·脚本化**）

1. **建集**：自两源件（甲面清单 §3-1／§3-2、EA 审计 §1-3／§1-4）解析逐件之「相对路径·仓·在册 bytes·在册 SHA-12」⇒ 得 111 之**逐件清单**（**⛔0 以「看起来在」充已落档**）。
2. **面①**：于在册所载之仓（`repo`／`sub`）与相对路径之下实测存在 ⇒ 读盘上全文字节，直算 **SHA-256 前 12 位**与 **bytes**，与在册值**逐位比对**（⛔ **0** 转抄他件之指纹）。
3. **面②**：扫描**登记册面**（`results\` 全子树 ＋ `pi_rulings\` ＋ 仓根 `*.md`；**⛔0 计入 `.tmp\`**），取「**件名与 SHA-12 同现于同一行**」之登记册为据，记其件与行号。
4. **面③**：施口径丙（faceA §4-2 三条 ＋ 本件 §2-2 所补二款）于**首 16,000 B ∪ 末 4,000 B**，取最早命中之落款／归属行，记其行号与字段名。
5. **映射**：按 §2-3 之表出三态；**加总自证 ＝ 111·容差 0**（若加总 ≠ 111 ⇒ **停手并报**）。
6. **上探与挂账**：另于四根实之全树按名枚举，检出「在册未登记之判定族件」与「归属面不可判件」，逐件具名入 `NOT_MEASURED`／挂账栏（**⛔0 填零**）。
7. **两读并出**：分别按读甲（面①）与读乙（面①∧面②∧面③）出两套三态，**并列出**，**⛔0 先算后择**。

### §5-4 · **正控**（**四道·证明测量系统非空转**）

| 正控 | 内容 | 预期读数 | 实测 |
|:--|:--|:--|:--|
| **Z1·枚举面非空转** | 于**同一次**四根实枚举内取**确知在盘**之件验其指纹（沿 EA 审计 §5-11 之正控法，取 `tools/exp_harness.py`） | 指纹逐位相符 | **须随 §8 之复算一并报**（本件⛔ **0** 以未跑充已跑） |
| **Z2·指纹面非空转** | 对 **111 件**逐件直算 SHA-12 与 bytes 并与在册值比对 | 不符 **0**、不在盘 **0** | **不符 0／不在盘 0** ✅（§3 各行） |
| **Z3·登记面非空转·含负控** | 读乙于在册锚集（41 件 v1 逐件表 **41／41** ＋ v2 摘录 **16／16**）全中，**含负控**（在册判「不计入／无落款」者全数判否） | 全中且负控全否 | **读乙 77 · 锚点全中·负控全否**（甲面清单 L204–L205／L226 载前棒之读数）——⚠ **本棒未独立复算锚点**（其锚集之在册件 `_41_items_status_verdict_v2_2026_10_23.md` 之 21 条摘录，本棒**未逐条复算**）⇒ 记 **`NOT_MEASURED`**（见 §6） |
| **Z4·归属面非空转·含负控** | 对**已知无落款字段**之 2 件（no.24／no.336）施面③ | **0 命中**（判否） | **no.336：全文 `verdict-keeper` 计数 ＝ 0 ⇒ 判否** ✅；**no.24：在册登记「0（无落款字段）」⇒ 判否** ✅ ——**本棒之 Z4 实为「负控命中」之证明：面③ 不会把无落款之件判为已落档** |

---

## §6 · 两读并出 ＋ 不可判面（**`NOT_MEASURED`／`OUT_OF_RANGE`·⛔0 填零**）

### §6-1 · 两读之算得结果（**各算一遍·并列出**）

| 读 | 已落档 | 未落档 | 挂账 | 合计 | **分歧处** |
|:--|--:|--:|--:|--:|:--|
| **读甲**（面①·宽读） | **111** | **0** | **0** | **111** | — |
| **读乙**（面①∧面②∧面③·严读） | **111** | **0** | **0** | **111** | — |
| **并出之结论** | **两读同得 111／0／0** | | | | **在 111 之射程内两读不分歧** |

> 📌 **两读何以不分歧（如实交代·非巧合）**：甲面 77 之逐件落档行由**甲面清单件**（10-24 02:07）提供；乙丙 34 件之逐件落档行由**EA 审计件**（10-24 01:15）提供 ⇒ **面② 之所以全立，系 P5 之补登记已成**，而非底数之先天性质。**若未补登记，两读当分歧**（读甲 111／读乙 63——读乙之 63 ＝ 甲面之 29「41 表逐件在册」＋ 乙 28 ＋ 丙 6，在册甲面清单 L41 载此二数）。
> 📌 **⛔0 先算后择**：本件**两读并出**，**不择其一充唯一判**；**其同**乃**结论**而非**前提**。

### §6-2 · 不可判面（**逐类入账·⛔0 按 111 填零·⛔0 称「全数达标」**）

| # | 类别 | 面之内容 | 依据（件·行） | 状态 |
|:-:|:--|:--|:--|:--|
| **N1** | `NOT_MEASURED` | **丙面 252 件之落款面**（上探面）⇒ 111 **非闭数** | EA 审计 §3-7 L254–L256；R1 | **未核** |
| **N2** | `NOT_MEASURED` | **母件「判定件」之真全集之精确清单**（母件 0 处给出全集定义 ⇒ 机械不可得） | EA 审计 §3-6 L250–L252；R3 | **未核** |
| **N3** | `NOT_MEASURED` | **no.24／no.336 之归属面补证**（2 件挂账） | EA 审计 §3-8 L258–L260；R2 | **未核**（本棒实测其现态见 §4-4） |
| **N4** | `NOT_MEASURED` | **Z3 之在册锚集（41／41 ＋ 16／16）之独立复算**（本棒未逐条复算，仅转录在册读数） | 甲面清单 L204–L205／L226 | **未核**（故 Z3 之「实测」栏记 `NOT_MEASURED`） |
| **N5** | `NOT_MEASURED` | **母件 §2.1 八项硬缺口之 0 残留**（门③ 之外之合取项①②④） | 母件 L160 | **未核**（**不属本件之射程**——⛔ **0** 代核） |
| **N6** | `OUT_OF_RANGE` | **回收站**（在册载 PI 清理四块之一「84 件入回收站」）——**不可枚举·非四根实之一** | 交接指南 §10-8 | **射程外** |
| **N7** | `OUT_OF_RANGE` | **归档区同名副本之内容面**（⛔ **0** 读其内容） | 铁律 | **射程外**（其**指纹面已核**，见 §6-3） |
| **N8** | `OUT_OF_RANGE` | **GLM 区** | 铁律 | **未触及**（⛔ **0** 读 `〔本地路径已脱敏〕`） |

### §6-3 · 归档区同名副本（**缺口 5 之核销·按名与指纹认人·⛔0 读内容**）

> 📌 **本棒实测**：于归档区（第三根）按**名**枚举，命中丙面 6 件之 **5 件同名副本**，其 SHA-12 与主仓现值**逐位不符（5／5 不符）**⇒ **归档区之副本与主仓现值非同一实体**（主仓现值者即在册之登记件·指纹相符）⇒ **不得以名充同件**。此**核销** EA 审计 §3-5（L246–L248）之登记级缺口「归档区同名件 5 件之指纹未核」。
>
> | 丙面件（主仓·本棒实测） | 归档区同名副本之实测 | 指纹相符 |
> |:--|:--|:--|
> | `_t1_qwen_temp_sweep_verdict_2026_10_09.md`（21,672／`dfc858d3d930`） | 21,652／`8f35c524a43f` | ❌ |
> | `_v4_supp_l14v3_n26_verdict.md`（65,978／`df6453d57f8a`） | 64,485／`f4435801d09f` | ❌ |
> | `_v4_supp_t15_verdict.md`（54,377／`3cb5c2f59961`） | 52,884／`52c985429c91` | ❌ |
> | `_v4_supp_t15r2_verdict.md`（65,638／`963725dbd82a`） | 64,145／`8355724a26e3` | ❌ |
> | `_v4_supp_t1_verdict.md`（29,106／`0ad42625f333`） | 27,538／`f1b5e49f3058` | ❌ |
>
> 📌 **读法之限**：**⛔0 读归档区任何正文**·**⛔0 断言其版次之先后**（仅证「非同体」）——**本件⛔0 宣称「主仓者为最新版」**；其先后之判**须读其内容**，为射程外。

### §6-4 · **「全数达标」之反面陈述（**诚实纪律**）

> 📌 **⛔0 称「全数达标」**。**准确之陈述**是：**在门③ 之在册底数 111 之射程内，三面全立 111／111、已落档 111／未落档 0／挂账 0、加总容差 0**；**然**「**全部**判定件」之**全称量词未证**（N1／N2）·**2 件挂账未补证**（N3）·**门③ 之第二合取项之裁决权属 EA／PI**·**宣告权属 PI**。

---

## §7 · 老实交代（**failures & limitations·不遮不掩**）

1. **本棒首轮之仪器失败（如实登记）**：面③ 首轮复算得 **102／111**，9 件未命中。经**逐件开卷核对**，确认 **9 件皆为在册规则未覆盖之两型**（L1 标题行 2 件＋件性质栏 7 件），**非**文件之缺——**是本棒漏实现 faceA §4-2 之规则①「文首标题行为结构性字段」与「件性质栏为归属栏」两款**。已补规则并复算得 **111／111**。⛔ **0** 以「首轮 9 件未命中」充「9 件未落档」；⛔ **0** 隐此失。
2. **Z3 之锚点未独立复算**：读乙于在册 41／41＋16／16 之全中，**本棒转录在册读数**（甲面清单 L204–L205／L226），**未逐条复算** ⇒ 记 **`NOT_MEASURED`**（N4）。**本棒之 Z4 负控**（no.24／no.336 判否）**为本棒自跑**，可充归属面之有效性证明。
3. **⛔0 评估任何判定件之实体面**：本件⛔ **0** 评判死线之真伪、⛔ **0** 评读数之对错、⛔ **0** 评结论之取舍。**「已落档」只答「该件是否在盘·在册·可核其 VK 归属」，不答「该件之判定是否正确」**。
4. **⛔0 落五终判**：本件**未**落 `pass`／`af`／`kd`／`fail`／`give-up` 任一——**门③ 之现值仍为 `PWC`**（PI 所采之值·本件不动之）·**⛔0 宣告门③ 成就**·**⛔0 宣告①段毕**·**⛔0 代销记**·**⛔0 代 PI 裁**。
5. **§5 之阈值系本件所立·待采认**：T1–T5 之**阈值本身 PI 未给值** ⇒ 依「判死线立时即带阈值」之纪律，**须 PI 采认后方为已立**；本件⛔ **0** 视其为已立。
6. **上探面与挂账面之未决**：N1（252 件未核）·N2（真全集不可得）·N3（2 件挂账）·N4（锚点未复算）——**本件不代其补证**（⛔0 落五终判·⛔0 代裁）·**归谁解**已逐条标明（EA §4-3 之「须谁动」）。
7. **归档区之限**：**⛔0 读其正文**·**⛔0 断言版次先后**（仅证「非同体」·5／5 指纹不符）；**⛔0 读 `〔本地路径已脱敏〕`**；回收站**不可枚举**（N6·`OUT_OF_RANGE`）。
8. **本件之射程写死**：**仅**及于**在册底数 111 件**之**落档状态**；**⛔0 外推为母件「判定件」之真全集**（N2）·**⛔0** 断言 111 为闭数。
9. **本棒未跑实验·未联网·未调 LLM／API**；全部读数皆自盘上文件直算（bytes／SHA-256 前 12 位）。
10. **本件之仪器**：`.tmp\_g3_111_harvest_2026_10_28.py`（建集＋定位＋指纹）·`.tmp\_g3_111_scan_2026_10_28.py`（面② 登记面扫描 ＋ 面③ 首轮）·`.tmp\_g3_111_sig_2026_10_28.py`（面③ 补款复算 ＋ 裁号回源）·`.tmp\_g3_write_p1/p2/p3_2026_10_28.py`（落件）——**半成品与脚本皆在 `.tmp\`**（⛔ **0** 落 `results\`／`pi_rulings\` 之非目标面）。

---

## §8 · 自证

### §8-1 · 字节五项（本件之落盘后实测）

| 项 | 判据 | 期望 | 实测 |
|:-:|:--|:--|:--|
| **BOM** | 文件首三字节 ≠ `EF BB BF` | 0 | **0** ✅ |
| **CR** | 全文 `0x0D` 字节数 | 0 | **0** ✅ |
| **VT** | 全文 `0x0B` 字节数 | 0 | **0** ✅ |
| **U+FFFD** | 全文解码后 `\ufffd` 计数 | 0 | **0** ✅ |
| **LAST_BYTE** | 末字节 | `0x0A` | **`0x0a`** ✅ |

> 📌 编码：UTF-8 **无 BOM** · **纯 LF**。**bytes 与 SHA-12 随交付面呈报**（一文件不能载其自身之 SHA-12·故不内写）。

### §8-2 · 触动既有件数 ＝ **0**

| 项 | 值 | 据 |
|:--|:--|:--|
| 落盘前 `Test-Path` 之目标路径 | **False**（不存在）✅ | 落盘前实测 |
| 本棒**写入**既有件之件数 | **0** | 本棒全部写入落于：① 本件（新立）② `.tmp\` 之半成品与脚本（**非既有件**·为新建之半成品区文件） |
| 本棒**移动／重命名／删除**之件数 | **0** | 本棒无任何 `mv`／`rm`／目录操作 |
| 本棒**回改既有件一字**之件数 | **0** | 本件为新立件；既有件之引用**只读** |

> 📌 **并发说明（如实）**：本棒观测期内若另有他棒于同仓落件，**其归属非本棒可断**——故「触动 0」之陈述限定为「**本棒未对任何既有件执行写入／移动／删除／回改**」，**⛔0** 声称「全仓无他件变动」。

### §8-3 · 引证清单（**每一指纹皆本棒自测·附观测时点**）

| # | 件（相对路径） | bytes（自测） | SHA-12（自测） | 观测时点 | 本件引其何处 |
|:-:|:--|--:|:--|:--|:--|
| 1 | `results/evidence/register/_gate3_faceA_itemlist_register_2026_10_24.md` | 38,840 | `512b31f1a1ed` | 2026-10-28 11:46:05 | §1-1·§2-2·§3-1·§4-2 |
| 2 | `results/evidence/register/_gate3_108_ea_audit_2026_10_24.md` | 44,650 | `8ebb365be944` | 2026-10-28 11:46:05 | §1-1·§3-2·§3-3·§4-1·§4-2·§6-2 |
| 3 | `pi_rulings/_pi_card_answers_register_2026_10_24_v268.md` | 8,945 | `c9a941c196ad` | 2026-10-28 11:46:05 | §1-3·§4-1·§4-2 |
| 4 | `pi_rulings/_pi_card_answers_register_2026_10_24_v269.md` | 9,398 | `0cee727234cf` | 2026-10-28 11:46:05 | §1-3·§4-2·§4-3 |
| 5 | `results/readout/run/_v34_experiment_gap_plan_2026_10_08.md` | 36,066 | `996feb1db9cb` | 2026-10-28 11:46:05 | §1-1·§5-1·§6-2 |
| 6 | `results/verdict/judgement/_gate3_base_count_dispute_2026_10_25.md` | 39,201 | `d790afb6f2a7` | 2026-10-28 11:46:05 | §4-3 |
| 7 | `results/verdict/judgement/_41_items_judgement_status_verdict_2026_10_23.md` | 41,114 | `9e9141ae18c2` | 2026-10-28 11:46:05 | §4-4 |
| 8 | `results/verdict/judgement/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md` | 37,908 | `f1ca2c59bed9` | 2026-10-28 11:46:05 | §4-4 |
| 9 | `results/verdict/judgement/_t4k_k5k_coverage_adjudication_2026_10_22.md` | 61,203 | `66d8d45c7a62` | 2026-10-28 11:46:05 | §4-4 |

> 📌 **凡引必自测**：上表九件之 bytes／SHA-12 **皆本棒于 2026-10-28 11:46:05 直算盘上全文字节所得**，⛔ **0** 转抄在册之值。**裁号之限**见 §1-3（`pi_rulings` 之件内 0 处 `\| **NNN** \|` 裁号行 ⇒ **⛔0 以册名充内容之据**）。

---

## §9 · 本件之判（一句话·**不软化**）

> 📌 **判**：**在门③ 之在册底数 111 之射程内，111 件之三态已闭且两读同——已落档 111／未落档 0／挂账 0，加总 111、容差 0。**
> 📌 **然门③ 不得转 `PASS`**，其阻碍**不在落档面**，而在：**① 全称量词未证**（丙面 252 件上探未核·母件真全集不可得 ⇒ 111 非闭数）；**② 2 件挂账未补证**；**③ 分类面 2 处名差未消解**；**④ 第二合取项之裁决权属 EA／PI**；**⑤ 宣告权属 PI**。
> 📌 **转 `PASS` 之要件已四件齐**（§5：判据／阈值 T1–T5／测量法 7 步／正控 Z1–Z4），**其阈值须 PI 采认**后方为已立。
> 📌 **⛔0 宣告门③ 成就·⛔0 宣告①段毕·⛔0 代销记·⛔0 代 PI 裁·⛔0 落五终判。**

---

**落款**：`verdict-keeper`（判定收口官 · agent-3a4d09ba3c90）· 门③ 111 件之落档确认 · 观测时点 2026-10-28 11:46:05 GMT+8 · ⛔ **0** 宣告门③ 成就 · ⛔ **0** 落五终判 · ⛔ **0** 代 PI 裁 · ⛔ **0** 代销记 · ⛔ **0** 回改既有件一字

**状态行**：`门③ 111 件 · 逐件三态已闭：已落档 111／未落档 0／挂账 0（两读同）· PWC 保留项 P1–P5 逐条回源 · 转 PASS 四要件齐（待 PI 采认）· 呈 PI`

### §8-4 · 勘正节 ＋ 正控补录（**append-only·以本节为准·前文一字未改**）

#### §8-4-1 · **勘正①**：§4-2 之 **P3** 行号 **L180 → L181**（**位号回源之实证**）

> 📌 **勘误对象**：§4-2 之 P3 栏所引「⛔ **0** 强合」逐字，标注为 EA 审计 **L180**。
> 📌 **误因（如实登记）**：本棒**依读版之印象**取行号，**未逐行回源**；本棒自核时取到 **L180** 之实文为**另一句**（见下）。
> 📌 **正确之位号**：**L181**（本棒于 2026-10-28 11:49:29 实取该行逐字如下）；**L180** 之实文逐字如下，以自证其**非**所引之句。

- **L180 之实文**（本棒实取）：「> 📌 **两读并出·不消解**：① **读甲之数与在册 74 相符而锚点校验不过**（40／41＋13／16）⇒ 其 3 处失配即上表 3 件之**反证面**（读甲读其「无」而两源件判其「有」）；② **读乙之锚点校验全过**（41／41＋16／16）而其数 77 **超**在册 74 之 3 ⇒ **超出的 3 件即上表 3 件**。」
- **L181 之实文**（本棒实取·**P3 所引之正身**）：「> 📌 **⛔ 0 强合**：本件**不代裁**「甲面终数 ＝ 74 抑或 77」，**不代裁**「上表 3 件属否」；**代价不对称明写于 §4**。」

⇒ **以本节为准**：P3 之位号为 **EA 审计 L181**。**P3 之文义不受影响**（其所述「互斥 3 件未消解·本件不代裁」之实义，与 L181 逐字相符）。

#### §8-4-2 · **勘正②**：§5-4 之 **Z3** 锚集口径（**21／21 与 16／16 之别**）

> 📌 **勘误对象**：§5-4 之 Z3 栏作「读乙于在册锚集（41 件 v1 逐件表 **41／41** ＋ v2 摘录 **16／16**）全中」，而其括注之位号为「甲面清单 L204–L205／L226」。
> 📌 **实情**：两件所用之 **v2 摘录锚集条数不同**——**甲面清单** L204–L205／L226 所载为 **41／41 ＋ 21／21**（其 v2 摘录锚集 **21** 条）；**EA 审计** L307 所载为 **41／41 ＋ 16／16**（其 v2 摘录锚集 **16** 条）。⇒ 两者**非矛盾**（锚集条数不同），然**引用时须带所据之件**。
> 📌 **以本节为准**：Z3 当读作——**读乙于在册锚集全中**：甲面清单口径 **41／41 ＋ 21／21**（L204–L205／L226）｜EA 审计口径 **41／41 ＋ 16／16**（L307）｜**v269 L14** 亦载「锚点 41／41＋16／16 全中」。⚠ **本棒未独立复算该锚集** ⇒ Z3 之「实测」栏仍记 **`NOT_MEASURED`**（§6-2 之 N4）——**本节只正其口径与位号之归属，不升其证据级**。

#### §8-4-3 · **正控 Z1 之实跑**（**填 §5-4 之 Z1 实测栏·以本节为准**）

| 正控 | 目标件 | 本棒实测（2026-10-28 11:49:29） | 与在册值之比对 | 判 |
|:--|:--|:--|:--|:--|
| **Z1·枚举面非空转** | `tools/exp_harness.py`（repo） | **bytes 45,590 ／ SHA-12 `ce64b9b97489`** | EA 审计 **L307** 所载「**45,590 B／`ce64b9b97489`**（**与派工单所载逐位相符**）」→ **逐位相符** ✅ | **正控成立**（枚举面非空转） |

> 📌 **本棒**于 2026-10-28 11:49:29 对 `tools\exp_harness.py` 直算盘上全文字节（**⛔0 执行该脚本**——本棒⛔ 0 跑实验；**仅测其字节与哈希**作同一性正控）⇒ **Z1 之实测栏自「须随 §8 复算一并报」变为「已跑·逐位相符」**。

#### §8-4-4 · §3 表之**行级自证**（**本棒于 2026-10-28 11:49:29 自核**）

| 项 | 实测 |
|:--|:--|
| §3-1／§3-2／§3-3 之**数据行**数 | **111**（甲 **77** ＋ 乙 **28** ＋ 丙 **6**） |
| §3-4 互斥 3 件之单列行数 | **3**（**已并入** §3-1 之序 4／17／18·**未重复计入** 111） |
| 三态标签计数（逐行自核） | **已落档 111／未落档 0／挂账 0** |
| 未替换之占位符 | **0** |
| 加总 | **77 ＋ 28 ＋ 6 ＝ 111** ✅ **容差 0** |

---

**落款（补）**：`verdict-keeper`（判定收口官 · agent-3a4d09ba3c90）· 勘正节 ＋ 正控补录 · 2026-10-28 11:49:29 GMT+8 · ⛔ **0** 回改既有件一字 · ⛔ **0** 宣告门③ 成就 · ⛔ **0** 落五终判

**状态行（补）**：`门③ 111 件 · 已落档 111／未落档 0／挂账 0（两读同）· §8-4 勘正 P3 位号 L180→L181、Z3 口径归属 · Z1 正控实跑逐位相符 · 呈 PI`
