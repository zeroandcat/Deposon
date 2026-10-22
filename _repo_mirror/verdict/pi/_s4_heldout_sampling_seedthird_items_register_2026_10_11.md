# 向-1 第三集 held-out 抽取登记件（`seed″` ＝ `3223484571`）· 2026-10-11

- **件性质**：**worker 执行面 · 抽取＋登记**（**⛔ 非 protocol 面 · ⛔ 非判定面**）—— 依已生效之冻结规格抽取第三集 26 件，并落逐件表、三集对照、可动件实测、`in_heldout` 重算
  ｜ ⛔ **0 判档**（0 出 `pass`／`af`／`kd`／`fail`／`give-up` 五终判之一）｜ ⛔ **0 代裁／0 代择**｜ ⛔ **0 换 seed 重抽**（PI 定「一次抽取」）｜ ⛔ **0 回改任何既有件一字**｜ ⛔ **0 改 `K-RJ-8′`／`K-RJ-9′` 条文**
- **授权锚**：PI 2026-10-11 收官卡 `f4_second` ＝ **甲·复核并闭（解锁）**｜规则与种子先于抽取落定（FTFB 已守）
- **规格源**：`fb1b696de1d6` §5 伪码（0 改一字）＋ `ab1a07ae2fd1` §4-1 之 R0–R7｜`seed″` 落定于 `6904852f8ceb`（`λ` ＝ `fd4ec7559342`，菜单 N ＝ 1）｜`S0′` 生效于 `fd4ec7559342`
- **产出 3 件（皆新名新建 · 0 覆写）**：
  1. **可审脚本** `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`
  2. **新集 JSON** `results/_s4_heldout_sampling_seedthird_items_2026_10_11.json`
  3. **本登记件** `results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md`
- **出件**：**worker**（向-1 第三集抽取批 · 分支会话 `mvs_544437291b604723b1f8a991c7e717e4`｜**署名如实** · ⛔ 0 冒充 PI／parent／verifier／verdict-keeper／protocol-keeper／evidence-auditor／doc-writer）
- **版式**：UTF-8 **无 BOM** · **LF（CRLF ＝ 0）**｜**R4**：key 永不明文（0 读 key／0 读 `.env`／0 落盘凭据）｜**0 网络 ／ 0 skill ／ 0 LLM ／ 0 跑 executor ／ 0 跑 S4′ 读数面**｜⛔ **0 触及 `〔归档件引用·未上传:〔归档区〕〕`**
- **命名合规**：`_主题_日期` 三段式；首段 `_s4_heldout_sampling_` ＝ 步骤标识非阶段号 ⇒ 合 PI 2026-09-29 命名裁（`57024f2cd30a` §1.2②）；⛔ `_v5_`／`_v4_`／`_v3_`

> 📌 **状态栏**：🟢 **第三集已抽出（一次抽取 · 26 件 · `FP3` 已生成并登记）** ＋ 🟢 **自审双门通过**（seed42 逐件全等 ＋ seed′ 逐件全等）＋ 📌 **`FP3` 待 PI 面以另立登记承载**（⛔ 0 回改 `fd4ec7559342` 一字）＋ ⛔ **0 判档 · 0 宣告过门与否 · 0 宣告 `K-RJ-5` 闭／开 · 0 宣告新链可开跑**

---

## §0 一句话结论

**以 `seed″` ＝ `3223484571` 依 R0–R7 冻结规格抽出第三集 held-out 26 件，`FP3` ＝ **`c34835ad59cf**；抽取前双门自审通过（以 `seed=42` 与现集 `6a670e629dca` **逐件全等**、以 `seed′` 与第二集 `6cbb8ba01bfb` **逐件全等**）；可动件实测 ＝ **1** 件（判据 ＝ `seq_t1_only` 与 `seq_v31` 之**逐位序列比对**）；`in_heldout` 重算（面 II 24 件）＝ **新内 5 ／新外 19**（第一集 9／15、第二集 4／20）。** ⛔ 本件仅提供机械事实，⛔ 0 判档、⛔ 0 宣告过门与否、⛔ 0 代改任何判死线条文。**

---

## §1 ★ `FP3`（**`K-RJ-8′` 之锚值 · 待填槽之填**）

| 项 | 值 |
|:--|:--|
| **`FP3`（＝ `K-RJ-8′` 之锚值字面）** | **`c34835ad59cf`** |
| 算法（R6 · 0 改） | `sha256( R1 键字节序之 "file#idx" 以 "|" 连接 )[:12]`（小写 hex） |
| 全 64 hex | `c34835ad59cf75a75fcfbdbb61480c1ed7cb2cfc3b9a8dbac4c2f7c0d2c786b5` |
| 长度（可核） | **1417 字符**（26 条） |
| 载体 | `results/_s4_heldout_sampling_seedthird_items_2026_10_11.json` |
| `match`／**26／26** | 复算同值 ✅ ／ 件数 **26**（两两互异） |
| 与前两集 | 异于 `acedff01d18c`（第一集）、异于 `3c25e1a2ea94`（第二集）⇒ **三集互不可比**（`fd4ec7559342` §5 · PI 已明示承受） |

📌 **承载纪律**：`K-RJ-8′` 之**判据形式**已冻于 `fd4ec7559342` §3；本件**仅以另立登记承载新值**，⛔ **0 回改** `fd4ec7559342` 一字、⛔ **0 改** `04495ef4b343` 一字。** `FP3` 之正式生效归 PI／protocol 面。**

---

## §2 ★ 自审双门（**抽取前 · FTFB 之等价实现**）

| 门 | 种子 | 对照集 | 件数全等 | 逐格全等 | 指纹全等 | 复算指纹 | 判定 |
|:-:|:--|:--|:-:|:--:|:--:|:--|:--|
| **B** | `42` | `6a670e629dca`（第一集） | True | True | True | `acedff01d18c` | **✅ 通过** |
| **B′** | `1830975565` | `6cbb8ba01bfb`（第二集） | True | True | True | `3c25e1a2ea94` | **✅ 通过** |

> 📌 **门 B 之意义**：同一实现以现集之种子复跑须**逐件全等** ⇒ 实现无偏；不等即 ⛔ 停手（⛔ **0 产出新集**）。
> 📌 **门 B′ 之意义**（本棒自加之控制核）：同一实现以第二集之种子复跑亦**逐件全等** ⇒ 实现对「换 seed」族**普适**，非恰性拟合。
> 📌 **两门皆在第三集抽取之前执行** ⇒ 任一失败即 `sys.exit`，⛔ **0 产出新集实体**。

---

## §3 ★ 逐件表（**26 件 · R1 键字节序**）

| 序 | `file#idx` | `q_id` | 格 `(b,s,o)` | 位移型 | `seq_t1_only` | `seq_v31` | 逐位相等 | **可动** |
|:-:|:--|:--|:-:|:-:|:--|:--|:-:|:-:|
| 0 | `_s4_substrate_topup_addendum_2026_10_09.json#14` | `S4T-15` | `0,6,3` | — | `CRITERIA` | `CRITERIA` | ＝ | 否 |
| 1 | `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json#0` | `Q40` | `0,0,1` | — | `DELEGATE,TIMING` | `DELEGATE,TIMING` | ＝ | 否 |
| 2 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json#0` | `Q44` | `0,5,3` | — | `DELEGATE` | `DELEGATE` | ＝ | 否 |
| 3 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json#2` | `Q46` | `0,5,3` | — | `DELEGATE,RISK` | `DELEGATE,RISK` | ＝ | 否 |
| 4 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json#3` | `Q47` | `0,1,1` | — | `TIMING` | `TIMING` | ＝ | 否 |
| 5 | `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json#1` | `Q49` | `0,7,1` | — | `∅` | `∅` | ＝ | 否 |
| 6 | `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json#1` | `null` | `0,0,1` | — | `CRITERIA,RISK,COST,DELEGATE` | `CRITERIA,RISK,COST,DELEGATE` | ＝ | 否 |
| 7 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json#0` | `null` | `0,0,3` | — | `RISK,CRITERIA,KILL_LINE` | `RISK,CRITERIA,KILL_LINE` | ＝ | 否 |
| 8 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json#3` | `null` | `0,0,3` | T1 | `COST,KILL_LINE,RISK,TIMING` | `COST,KILL_LINE,RISK,TIMING` | ＝ | 否 |
| 9 | `_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json#0` | `DF6-1` | `0,4,3` | — | `∅` | `∅` | ＝ | 否 |
| 10 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#6` | `D8-07` | `0,1,3` | — | `∅` | `∅` | ＝ | 否 |
| 11 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#16` | `D8-17` | `0,7,1` | — | `RISK` | `RISK` | ＝ | 否 |
| 12 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#20` | `D8-21` | `0,0,3` | T3 | `RISK` | `RISK` | ＝ | 否 |
| 13 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#23` | `D8-24` | `0,6,3` | — | `RISK` | `RISK` | ＝ | 否 |
| 14 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#27` | `D8-28` | `0,0,1` | — | `RISK` | `RISK` | ＝ | 否 |
| 15 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#29` | `D8-30` | `0,6,7` | — | `RISK` | `RISK` | ＝ | 否 |
| 16 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#30` | `D8-31` | `0,5,7` | — | `CRITERIA` | `CRITERIA` | ＝ | 否 |
| 17 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#34` | `D8-35` | `0,1,7` | — | `∅` | `∅` | ＝ | 否 |
| 18 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#39` | `D8-40` | `0,4,3` | T1 | `RISK,CRITERIA` | `RISK,CRITERIA` | ＝ | 否 |
| 19 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#40` | `D8-41` | `0,7,3` | — | `CRITERIA` | `CRITERIA` | ＝ | 否 |
| 20 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#62` | `D8-63` | `0,3,3` | T3 | `∅` | `CRITERIA` | ≠ | **是** |
| 21 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#65` | `D8-66` | `0,4,3` | T1 | `TIMING,RISK` | `TIMING,RISK` | ＝ | 否 |
| 22 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#75` | `D8-76` | `0,2,3` | — | `∅` | `∅` | ＝ | 否 |
| 23 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#83` | `SQ-04` | `0,7,0` | — | `CRITERIA,RISK` | `CRITERIA,RISK` | ＝ | 否 |
| 24 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#87` | `SQ-08` | `0,2,0` | — | `∅` | `∅` | ＝ | 否 |
| 25 | `_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json#0` | `DF6-4` | `0,0,1` | — | `∅` | `∅` | ＝ | 否 |

---

## §4 ★ 可动件实测（**逐位序列比对 · ⛔ 0 以「含 9 词」径判**）

| 项 | 内容 |
|:--|:--|
| **判据** | ★ `movable` ⇔ **`extract_sequence(reasoning_full, KEYWORDS_T1)` ≠ `extract_sequence(reasoning_full, KEYWORDS_V31)`**（**逐位序列比对**） |
| **⛔ 禁用判据** | 「语料含 `KEYWORDS_V31 − KEYWORDS_T1` 之 9 词中任一」—— 依 `e7fcbc290a7e` §3-1 之「当且仅当」条件 ＋ §7 之 **B-8** 实测反例（`d3c#1` 含「后面」而序列**未变**，因同层 `TIMING` 已被共有词 `补一晚` 触发） |
| `KEYWORDS_T1` | `KEYWORDS_V3` ＋ `{CRITERIA: 复核/质量/保证, RISK: 回退/遗忘, KILL_LINE: 推翻}`（逐字转录自 `.tmp/prep.py` L8–L9；⛔ **0 import** `prep.py`） |
| `KEYWORDS_V31` | `KEYWORDS_V3` ＋ 15 个 V3.1 新词（`.tmp/s4_regen_runner.py` L54–L64） |
| `KEYWORDS_V31 − KEYWORDS_T1` | **9 词** ＝ `后面`／`噪声`／`失实`／`对齐`／`挂起`／`检验`／`缺陷`／`观察者效应`／`记忆效应` |
| **可动件数（逐位比对）** | **1** ／ 26 |
| 含 ≥1 个 V31-only 词之件数 | 1（**⛔ 诊断面 · 非判据**） |
| 两判据之分歧件（`含词≠可动` 或 `不含词却可动`） | **0 件** |

📌 **控制核（第二集 26 件逐位复算）**：True —— 逐件 `seq_t1_only`／`seq_v31`／相等性三项与在册补层件**逐位全等**（26／26 件），可动件数复算 **0** ＝ 在册 **0** ⇒ 本棒之可动机制与盘上已登记机制**同源**。

🔴 **诚实边界**：本节**仅给出可动件数之机械事实**。⛔ **0 据以判档**；⛔ **0 宣告 `n_distinct` 过门与否**（`fd4ec7559342` §7 明载：可动件 ≥1 亦**不保证**过门，且若为 **0** 件则**不重抽** ⇒ 出口归向-2～向-5／`give-up` 由 PI 择）；⛔ **0 跑 `S4′` 读数面**（`pred_model_side`、逐件贡献、五线读数 ＋ CI **均未产出**）。

---

## §5 ★ 新旧三集对照（**交集／对称差**）

| 集 | 种子 | 指纹 | 件数 |
|:--|:--|:--|--:|
| 第一集 | `42` | `acedff01d18c` | 26 |
| 第二集 | `1830975565` | `3c25e1a2ea94` | 26 |
| **第三集（本件）** | **`3223484571`** | **`c34835ad59cf`** | **26** |

| 对照 | 交集 | 仅 A | 仅 B | **对称差** | 并集 |
|:--|--:|--:|--:|--:|--:|
| **第三集 ∩ 第一集** | 6 | 20 | 20 | **40** | 46 |
| **第三集 ∩ 第二集** | 7 | 19 | 19 | **38** | 45 |
| 第一集 ∩ 第二集（对照） | 8 | 18 | 18 | **36** | 44 |

> 📌 **三集互不可比**（`fd4ec7559342` §5 · PI 已明示承受）⇒ 上列**仅载成员关系之机械计数**，⛔ **0 混用三面读数**、⛔ **0 直接比大小**。

---

## §6 ★ `in_heldout` 逐件重算（**对照面 ＝ 面 II 24 件**）

**口径**（依 `26c8278e3552` §4 步 10 · 0 改判据）：面 II 位移面 24 件之 R1 键（`file` ＋ `src_idx`）是否属**第三集 26 条**之一。**分母 ＝ 24**（⛔ 非 179 行全域）。

| 计数 | 第一集（旧） | 第二集 | **第三集（新）** |
|:--|--:|--:|--:|
| **内** | 9 | 4 | **5** |
| **外** | 15 | 20 | **19** |
| 合计 | 24 | 24 | **24** |

### §6-1 控制核（**第一集复算 ＝ 在册字段**）

以第一集 `acedff01d18c` 独立复算面 II 24 件之 `in_heldout` ＝ **内 9 ／外 15**，与 `6f020c03e52c` 在册字段（内 9／外 15）**全等** ⇒ 本棒判定式与产出在册 9／15 之口径**同源**（24／24 逐件相符）。

### §6-2 逐件表（面 II 24 件 · 旧 → 新）

| # | `q_id` | R1 键 | 位移型 | 旧 `in_heldout` | **新 `in_heldout`** | 依据（格） |
|:-:|:--|:--|:-:|:-:|:-:|:--|
| 1 | `S4Q-04` | `_s4_open_questions_addendum_2026_10_09.json#3` | T3 | `true` | **`false`** | 外 |
| 2 | `S4T-08` | `_s4_substrate_topup_addendum_2026_10_09.json#7` | T3 | `true` | **`false`** | 外 |
| 3 | `S4T-11` | `_s4_substrate_topup_addendum_2026_10_09.json#10` | T3 | `true` | **`false`** | 外 |
| 4 | `S4T-12` | `_s4_substrate_topup_addendum_2026_10_09.json#11` | T3 | `false` | **`false`** | 外 |
| 5 | `S4T-13` | `_s4_substrate_topup_addendum_2026_10_09.json#12` | T3 | `false` | **`false`** | 外 |
| 6 | `S4T-14` | `_s4_substrate_topup_addendum_2026_10_09.json#13` | T3 | `false` | **`false`** | 外 |
| 7 | `Q10_third_read` | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json#3` | T1 | `false` | **`true`** | 内 · 格 `0,0,3` |
| 8 | `D8-21` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#20` | T3 | `true` | **`true`** | 内 · 格 `0,0,3` |
| 9 | `D8-27` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#26` | T3 | `true` | **`false`** | 外 |
| 10 | `D8-34` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#33` | T3 | `false` | **`false`** | 外 |
| 11 | `D8-38` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#37` | T3 | `true` | **`false`** | 外 |
| 12 | `D8-40` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#39` | T1 | `true` | **`true`** | 内 · 格 `0,4,3` |
| 13 | `D8-47` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#46` | T3 | `false` | **`false`** | 外 |
| 14 | `D8-49` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#48` | T1 | `false` | **`false`** | 外 |
| 15 | `D8-52` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#51` | T3 | `true` | **`false`** | 外 |
| 16 | `D8-53` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#52` | T3 | `false` | **`false`** | 外 |
| 17 | `D8-55` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#54` | T1 | `false` | **`false`** | 外 |
| 18 | `D8-57` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#56` | T3 | `false` | **`false`** | 外 |
| 19 | `D8-62` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#61` | T1 | `false` | **`false`** | 外 |
| 20 | `D8-63` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#62` | T3 | `false` | **`true`** | 内 · 格 `0,3,3` |
| 21 | `D8-64` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#63` | T3 | `false` | **`false`** | 外 |
| 22 | `D8-66` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#65` | T1 | `true` | **`true`** | 内 · 格 `0,4,3` |
| 23 | `D8-75` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#74` | T3 | `false` | **`false`** | 外 |
| 24 | `SQ-07` | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#86` | T1 | `false` | **`false`** | 外 |

### §6-3 迁移矩阵（**第一集 → 第三集**）

| 迁移类 | 件数 | `q_id` |
|:--|--:|:--|
| `in` → `out` | **6** | `S4Q-04`／`S4T-11`／`S4T-08`／`D8-27`／`D8-38`／`D8-52` |
| `out` → `in` | **2** | `Q10_third_read`／`D8-63` |
| 稳定 `in` | **3** | `D8-21`／`D8-40`／`D8-66` |
| 稳定 `out` | **13** | 其余 |
| 合计 | **24** | ✅ |

**对账恒等式**：旧内 `9` − 迁出 `6` ＋ 迁入 `2` ＝ **新内 `5`**；旧外 `15` ＋ `6` − `2` ＝ **新外 `19`**。

> 🔴 **`K-RJ-9′` 之重述义务（归 PI／protocol 面）**：`fd4ec7559342` §4 载 `N_in3`／`N_out3` 待抽取后重算 ⇒ 本件**提供该二值之机械事实**（`N_in3` ＝ **5**、`N_out3` ＝ **19**；**分母 24 不变**）；⛔ **0 代拟条文**、⛔ **0 回改** `04495ef4b343` 一字、⛔ **0 宣告**重述已生效。

---

## §7 逐格落面（**16 贡献格 · R4 消耗序 `b→s→o`**）

| 格 `(b,s,o)` | `n` | `k` | `selected`（R1 键字节序） |
|:-:|--:|--:|:--|
| `0,0,1` | 16 | 4 | `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json#0`、`_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json#1`、`_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#27`、`_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json#0` |
| `0,0,3` | 13 | 3 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json#0`、`_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json#3`、`_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#20` |
| `0,1,1` | 4 | 1 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json#3` |
| `0,1,3` | 4 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#6` |
| `0,1,7` | 5 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#34` |
| `0,2,0` | 6 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#87` |
| `0,2,3` | 6 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#75` |
| `0,3,3` | 6 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#62` |
| `0,4,3` | 10 | 3 | `_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json#0`、`_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#39`、`_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#65` |
| `0,5,3` | 7 | 2 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json#0`、`_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json#2` |
| `0,5,7` | 4 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#30` |
| `0,6,3` | 9 | 2 | `_s4_substrate_topup_addendum_2026_10_09.json#14`、`_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#23` |
| `0,6,7` | 4 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#29` |
| `0,7,0` | 4 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#83` |
| `0,7,1` | 9 | 2 | `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json#1`、`_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#16` |
| `0,7,3` | 4 | 1 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json#40` |

**构成报**：「分层含纠正」—— 留出集内 `b=1` 件数 = **0**（**含 0 成立之明文**；规则内生：`b=1` 各占格 `n ≤ 2` ⇒ `floor(0.30·n) = 0`，换任何 seed 仍为 0）。


---

## §8 诚实限制（如实列明 · **0 掩饰**）

1. 🔴 **0 判档／0 代裁** —— ⛔ 0 出五终判之一；⛔ 0 赋任一 `k_v3s_4_*` 布尔；⛔ **0 宣告** `P-0` 过／不过、⛔ **0 宣告** `K-RJ-5` 闭／开、⛔ **0 宣告**新链可开跑、⛔ **0 宣告**第三集可动件数「够／不够」。
2. 🔴 **可动件数 ≠ 过门** —— 本件 §4 之 **1** 件仅为**逐位比对之机械事实**；`fd4ec7559342` §7 明载：可动件 ≥1 **不保证**过门（`n_distinct` 须 `S3′` 实测 ＋ 定义性退化 0 解）。
3. 🔴 **`S4′` 读数面未跑** —— ⛔ 0 产出 `pred_model_side`、⛔ 0 产出逐件贡献、⛔ 0 产出五线读数 ＋ CI ＋ bootstrap ⇒ §4 之可动件数**不可**外推为任何触发量。
4. 🔴 **一次抽取之界** —— 第三集**仅抽一次**（`fd4ec7559342` §7）；⛔ **0 换 seed 重抽**、⛔ **0 择其过门者**。本脚本只跑一个 `seed″`。
5. 🟡 **三面不可比** —— 旧两集面（`acedff01d18c`／`3c25e1a2ea94`）之读数与逐件层须**物理分离**保留；⛔ 0 视作已废，⛔ 0 混用三面读数（PI 已明示承受 · §5）。
6. 🟡 **0 贴语料内部文本** —— 依 `fb1b696de1d6` §5.6 登记面规定，产出件⛔ **0** 载 `reasoning_full`／`scene_verbatim`／`pi_answer_verbatim`；§3 只载序列层（层名）＋ 计数 ⇒ 语料本身须第三方另行取自 21 件域件。
7. 🟡 **可动机制之依赖** —— 复用 `.tmp/s4_regen_runner.py`（只读 import）与 executor `8a81d90c69ba` 之词表与纯函数；`KEYWORDS_T1` 为逐字转录（⛔ 0 import `prep.py`，其 import 期即跑 `S4′` 读数面）。本件**0 新造**任何机制。

---

## §9 0 回改确认 ＋ 落前撞名实测 ＋ 纪律对照

| 纪律 | 自证 |
|:--|:--|
| ⛔ **0 回改任何既有件** | ✅ 本棒**唯一写动作 ＝ 新建 3 件**（脚本 ＋ JSON ＋ 本登记件），皆新名；既有件 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除（`6a670e629dca`／`6cbb8ba01bfb`／`6f020c03e52c`／`4125cb2df92b`／`26c8278e3552`／`fb1b696de1d6`／`ab1a07ae2fd1`／`fd4ec7559342`／`6904852f8ceb` **0 字节改动**） |
| ⛔ **0 改 `K-RJ-8′`／`K-RJ-9′` 条文** | ✅ 新值（`FP3`／`N_in3`／`N_out3`）**以本登记件另立承载**；⛔ 0 回改 `fd4ec7559342` 一字 |
| ⛔ **0 换 seed 重抽** | ✅ 抽取段只以 `seed″` ＝ `3223484571` 跑**一次**；门 B／B′ 之 `42`／`seed′` 复算**仅供自审**，不产生任何新集实体 |
| ⛔ **0 回写派生面** | ✅ ⛔ 0 回写 `6f020c03e52c` 之 `in_heldout` 字段；新值**仅存于**本产出 2 件 |
| **R4** | ✅ key 永不明文；0 读 key／0 读 `.env`／0 落盘凭据 |
| **0 网络／0 skill／0 LLM** | ✅ 纯本机只读计算；⛔ 0 端点调用／0 LLM 代答 |
| ⛔ **0 触及禁区** | ✅ `〔归档件引用·未上传:〔归档区〕〕` **0 读、0 写、0 列目录** |
| 编码 | ✅ UTF-8 **无 BOM** · **LF（CRLF ＝ 0）** |


---

## §10 报回项（**⛔ 0 代裁 · 0 代立 · 0 自判闭**）

| # | 事项 | 本件处置 |
|:-:|:--|:--|
| **R-1** | **`FP3` ＝ `c34835ad59cf`** 已生成并登记（`K-RJ-8′` 之待填槽） | 📋 已落 §1／JSON；⛔ **0 回改** `fd4ec7559342`；**生效归 PI／protocol 面** |
| **R-2** | 可动件 **1** 件（逐位比对判据） | 📋 已落 §3／§4；⛔ 0 判过门与否（§7 之「若」分支为**规则层出口约定**，非结果预测） |
| **R-3** | `N_in3` ＝ **5**／`N_out3` ＝ **19**（分母 24 不变） ⇒ `K-RJ-9′` 之**重述义务** | 📋 **仅提供数值事实**；⛔ 0 代拟条文、⛔ 0 回改 `04495ef4b343`、⛔ 0 宣告重述已生效 |
| **R-4** | 三集关系（交集／对称差，见 §5） | 📋 仅机械计数；⛔ 0 混用三面读数 |
| **R-5** | `S4′` 读数面（`pred_model_side`／逐件贡献／五线 ＋ CI） | 🔴 **未跑 · 0 产出**；候 `S4′` 正式开跑后另棒产出 |
| **R-6** | 面 I（26 件全量漂移 · `E-4` 未决）之 `in_heldout` | 📌 **如实登记为未闭**；⛔ 0 自行扩域、⛔ 0 并入本批分母（分母 ＝ 24） |
| **R-7** | 独立复核签字 | 📋 核归 verifier／verdict-keeper；**⛔ 本件 0 自签核** |

> ⛔ **本件 0 主张**：①`FP3` 已生效或已采认；②第三集已被独立复核；③可动件数足以过门；④`K-RJ-9′` 重述已生效；⑤`K-RJ-5` 可闭。
> 📌 **本件所主张者 ＝ 唯一**：**依已生效之冻结规格（R0–R7 ＋ `seed″` ＝ `3223484571`）抽出第三集 26 件，`FP3` ＝ `c34835ad59cf`，可动件 1 件，`in_heldout` 新内 5／新外 19** —— 其**归置、重述与效力判定皆不在本棒**。
