# V3-02 覆裁执行准备 · 口径与登记面（2026-10-09 · 乙档「授权改码＋新名」）

- **件性质**：**覆裁登记 ＋ 新名规格 ＋ kill-line／pre-reg 补记面 ＋ 派工规格**（protocol-keeper 口径面）｜**状态：待 PI 复核生效，生效即锁**
- **出件**：**protocol-keeper**（`agent-3e0c193da529`·本棒 session `mvs_ff5c197d80c44b1ba8750e13a6f67f84`）｜⛔ 0 冒充 PI／worker／verdict-keeper／evidence-auditor
- **授权锚**：PI 2026-10-09 S4 卷5 卡（`ask_aca3a25c244aa405e60eb22c`）**第 4 题之裁** —— 选**乙（授权改码＋新名）**，理由逐字「**不误导**」
- **上游语境**：PI 2026-10-09 卷⑨卡 Q1「五段全开·批准后当日即办」＋ W4 波许可（`results/_closing_round_8_decisions_register_2026_10_09.md`〔`a28a478e14a8`〕§1 Q4①「W4 产出链重走**许可**✓」）；本棒承接 `results/_protocol_version_landing_status_2026_10_09.md`（`1d1895489d17`）§5 候呈之**乙档**
- **本棒边界**：⛔ **0 改码**、⛔ **0 跑产出链**、⛔ **0 改任何既有件**（改码与执行归后续 worker）｜本棒**只出「口径 ＋ 登记」**
- **版式**：UTF-8 无 BOM · LF｜**件名**：`results/_v3_02_override_register_2026_10_09.md`（`_主题_日期`，⛔ 无 V-阶段前缀、⛔ 无 `_v5_` 类字样；沿命名裁定 `57024f2cd30a` §1.2②）
- **撞名实测（落盘前）**：`Test-Path` 拟落名 ＝ **`False`**；全仓递归 glob `*override*` ＝ **0 命中**、`*v3_02*` ＝ **0 命中**；另测同族备选名 2 个均 `False` ⇒ **新建，0 覆写**

---

## §0 三问初判 ＋ 状态一句话

| 问 | 初判 | 依据 |
|---|---|---|
| **Q1 素材面可得？** | ✅ **可得** | runner 三件输入料**逐件在盘实测在位**：`corpus/v20/index.json` `8423ffe266af`／`corpus/v20/strip_captions_22.json` `6a2656878745`／`results/_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` `1088fdd2b197`；阻断**0 源于缺料**（沿 `1d1895489d17` §2） |
| **Q2 实验可设计？** | ✅ **可设计** | 两处改码点、写出目标、完整性自检、0 覆写 pin、终验断言**均在盘上逐行可核**（`de16bc002198` L62-65／L110-126／L391-418／L445-448；`191efa7fe0b6` L42／L205-254） |
| **Q3 命题可证伪？** | ✅ **可证伪** | 验收字面可机械赋布尔：`protocol_version` **键级**命中 ＝ 1/件且值逐字 `"V0.4"`；测量面零漂移；⛔ 但**命题存亡 0 由本棒判**（归 verdict-keeper） |

**状态一句话**：**乙档已获 PI 明文覆裁 ⇒ 唯一合规实现 ＝「新建脚本副本改码 ＋ 新名输出 ＋ 测量面零漂移」；本棒已把新名、键位、kill-line、漂移注记、派工规格逐项冻结为可机械执行之规格，等 PI 复核生效后即可照规格发棒。**

---

## §1 来源等级与诚实边界

| 等级 | 含义 | 本件用法 |
|---|---|---|
| **L1 直录** | PI 亲笔字面 | ⛔ **本棒 0 件 L1**（见下方诚实边界） |
| **L2 转供** | **parent 派工单转录**之 PI 新裁（乙档＋理由「不误导」） | §2.1 照录，**如实标注为转录**，⛔ 不冒充问卷原件复算 |
| **L3 本棒盘上实测** | 本棒本 Turn `Get-FileHash`／`Select-String`／`Get-Content`／`Test-Path`／glob 可复核 | §3 全部指纹、§4 全部键位与行号、§5 全部读数、§8 回执行 |
| **L4 既有件字面引用** | 沿既有件原文口径，**必给件名＋sha12，0 改述** | `1d1895489d17`／`4daaf68cbf0e`／`c13449101ab3` 等 |

**⚠️ 诚实边界（三条 · 逐条声明）**

1. **PI 新答之回执原件，本棒 0 自读**：卡 `ask_aca3a25c244aa405e60eb22c` 的 `reply_payload` 属 `ask_user` 存储面，**本棒 0 网络 0 读该面** ⇒ §2.1 之乙档字面系**派工单转录（L2）**。
2. **盘上可核的旁证（非答复原件）**：`results/_pending_pi_items_master_register_2026_10_09.md`（`87ab4929477f`／35,258 B）§5 载该卡 **Q4 两档原题面** —— opt1「**甲 维持 10-01 原裁**」（对应 `1d1895489d17` §5-甲）、opt2「**乙 授权改码＋新名**」（对应 §5-乙），并记「root 漂移已登记：`reproduce_within_4dp=false`、偏差 `8.98e-03`」；同件记该卡**彼时 `status=pending`** ⇒ **PI 新答系该卡落册之后新增**，本棒 **0 以该件冒充答复原件**。
3. **本棒 0 独立复算 PI 择档之依据**：PI 择「乙」之权衡过程本棒 0 得知，**0 代拟理由链**；仅登记其已给出的理由字面「不误导」，并在下文把该字面**落为可机械执行的规格条款**（这是本棒口径面之职责，非代裁）。

---

## §2 覆裁登记

### §2.1 PI 新裁照录（L2 · 派工单转录 · 照录 0 改写 0 润色）

> **卡**：`ask_aca3a25c244aa405e60eb22c`（2026-10-09 S4 卷5）｜**第 4 题**
> **PI 实裁**：**乙**（＝ 授权改码 ＋ 新名输出）
> **PI 给出的理由（逐字）**：「**不误导**」
> **档位性质**：**覆裁**（supersede）——覆 2026-10-01 之「非补跑／非改码」之裁

### §2.2 被覆之原裁（L4 · 逐字）

`results/_mini_round_3_decisions_register_2026_10_01.md`（`bff06d3b3f97`／44,308 B）§1 Q1② 逐字：

> 「② `protocol_version` 缺口 ⇒ **另立补记件**（**非补跑／非改码**）」

- **回执标识**：`ask_d50c961a307949025a7b8d2d`｜提交 ts `1790820969861`（＝ 2026-10-01 10:16:09 +08:00）｜**原件盘上 0 命中**（该批录件 §0.3 自陈，L1 实为「派工单转录之回执字面」）
- **原裁承载件**：`results/c5_protocol_version_annex_2026_10_01.md`（`2593ea7b93cf`／18,558 B／mtime 2026-10-01 10:25:17）——**已在盘**，为原裁之唯一承载

### §2.3 覆裁关系登记（supersede · ⛔ 0 回改任何既有件）

| 项 | 登记 |
|---|---|
| **覆裁范围（唯一）** | **仅** V3-02「`protocol_version` **产出层**载体缺口」（`U-V04-01` 之产出层半） |
| **⛔ 覆裁范围外（本裁 0 触）** | ① 原裁之**方法面**结论（「另立补记件已落 `2593ea7b93cf`」）**继续有效**；② Q1① `dual_hex_width` 甲档豁免备案**继续有效**；③ Q2／Q3／Q4 四事分裁**继续有效**；④ V0.4 spec（`c13449101ab3`）之规则面**继续有效** |
| **⛔ 0 回改声明** | 本棒及后续 worker 均 **0 回改**：`bff06d3b3f97`／`2593ea7b93cf`／`1d1895489d17`／`87ab4929477f`／`c13449101ab3`／三件产出件／两处脚本 —— **byte 0 触动**（§8 回执行） |
| **W-5 之有限覆裁（关键）** | root 候选件 `2fd8946cfe80` §8 **W-5** 原文含「⛔ **0 改 runner 既有字面**（含 `SPEC_REF_V04`）」，`1d1895489d17` §3② 之停手依据之一即此条。**本裁仅在以下三面有限解除 W-5**：① 产出件**新增** `protocol_version` 键；② 出处字段（`generator`／`date`／`task_id`／`REL_*`／输出路径）**随新名同步**；③ `SPEC_REF_V04` 字面之**过时残留处置**（见 §4 `K-PV02-04`）。**W-5 其余面（V0.3／V0.2 spec 任一字、构造常数、`ANCHORS`、`FORBIDDEN_TOKENS`、判定逻辑）维持全部禁止，一字不得改** |
| **甲档（维持原裁）** | **已被 PI 覆裁取代** ⇒ `U-V04-01` 之产出层**不再按甲档销项**；但**销项字面之改述**（验收由「产出件写入该键」改述）**随乙档作废**，0 并行执行 |
| **丙档（授权补跑）** | **逻辑不成立**（`1d1895489d17` §3①：不 concomitant 改码则键仍不落）⇒ **归入乙档实现之必要步骤**（改码后**必跑**），**不另立档** |
| **丙档之次序性（本棒固化）** | **改码 → 跑 → 落新名** 三步**不可颠倒**；⛔ **0 先跑后补键**（先跑则产出仍 0 命中，等于原样重跑并覆写面，违 0 回改） |
| **0 代裁声明** | 本棒 **0 择档、0 代裁「乙档之内 PI 未明示之细节」**；凡本棒所立之**新增停手条件**均于 §4 明标「**新增**」，**⛔ 不冒充 PI 裁、⛔ 不改任何既有阈值字面** |

---

## §3 新名规格

### §3.1 产出件三件（改码后之新输出名 · ⛔ 0 覆写既有路径）

| # | 既有路径（**0 覆写**） | 本棒实测指纹 | **新输出名（新名 · 唯一）** |
|:-:|---|---|---|
| ① | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745`／20,398 B | **`results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json`** |
| ② | `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986`／24,421 B | **`corpus/v20/index_v3_2026_10_09.json`** |
| ③ | `results/c5_b_group_fix_readings_2026_10_01.json` | `2a7749da7c4d`／9,996 B | **`results/c5_b_group_fix_readings_2026_10_09.json`** |

**命名口径声明（三条 · 防误读）**

1. **仅换日期段、0 换词干**：三件新名之**词干与既有产出件逐段相同**，**唯一差异 ＝ 日期段 `_2026_09_29`／`_2026_10_01` → `_2026_10_09`**（＝ 实际修订跑日）。理由：① 最小改动面 ＝ 最不易引入新误导；② 沿既有产出命名体例（`191efa7fe0b6` L41 逐字自陈「件名沿 PI 命名裁 `57024f2cd30a` §1.2② + root 候选件 §4.4」）。
2. **`v0_4`／`v3` token ＝ 存量协议版本标识，⛔ 非阶段名、非本棒新造**：`deposon_..._v0_4_...` 之 `v0_4` 指 **P-D 指纹协议版本**（spec `c13449101ab3`）；`index_v3_...` 之 `v3` 指 **index 迭代版本**且**非首段**（命名裁定 §1.2② 之禁项为「`_v5_`/`_v4_`/`_v3_` 等 **V-阶段前缀**」及「文件名**不得含阶段号作为首段**」）⇒ 沿用存量词干**不违裁**，且**本棒 0 新造任何 V-阶段名、0 自升阶段**。
3. **⛔ 0 新增语义后缀**：**不**加 `_pv04_`／`_revised_`／`_r2_` 等新造 token —— 新造 token 须经命名权（PI）授权，本棒 **0 自造**；日期段已足以唯一标识。

### §3.2 脚本副本二件（改码载体 · **必须新建副本，0 触既有脚本**）

| # | 既有脚本（**0 覆写**） | 本棒实测指纹 | **新副本名（新名 · 唯一）** |
|:-:|---|---|---|
| R | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | `de16bc002198`／20,322 B／453 LF 行 | **`deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py`** |
| G | `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` | `191efa7fe0b6`／12,014 B | **`.tmp/_c5_b_group_fix_readings_2026_10_09.py`** |

- **为何必须「新建副本」而非原地改码**：`0 回改任何既有件` 系本棒与后续棒的**硬约束**（且 `de16bc002198` 乃 09-29 产出件之**出处载体**，原地改码将使既有件 `generator` 字段所指之脚本**内容漂移** ⇒ 反而构成误导）⇒ **唯一合规实现 ＝ 复制为新副本后改副本**。
- **副本名去 `_v5_`**：原 G 名含 `_v5_` 前缀（**存量历史档案字面**，沿命名裁定 §1.2① **0 回改、0 追认**）⇒ **新副本名 0 沿用该前缀**（§1.2② 管增量：⛔ 新件一律不得再带）。
- **落位面**：R 落 `deposon_team/plugins/`（与原件同面，体例一致）；G 落 `.tmp/`（与原件同面；⚠️ **`.tmp` 具临时区属性** —— worker 须在回执中登记该位置事实，⛔ 0 声称「已入册件」）。

### §3.3 键位规格（`protocol_version` 落哪 —— 本棒口径固化）

**规则面唯一载体**：`docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md`（`c13449101ab3`）§2.4 L116 逐字 —— **`protocol_version`｜`"V0.4"`｜字符串｜⚠️ 规则面已定 ＋ 载体缺口：本 spec 是唯一载体**；§2 表 L105 同载「**常量 `"V0.4"`**」。

| 件 | **落位（本棒固化 · 键位即口径）** | 值 | 禁写面 |
|:-:|---|---|---|
| ①  | **顶层键** `protocol_version`（与 `task_id`／`date`／`chain_summary` 同级；`chain_summary` 为 spec §2.4 表列 `b3_merkle_root` 之实际落面，同属**顶层字段面**族） | `"V0.4"` | ⛔ **0 塞入 `caliber`**（`caliber` ＝ 构造参数面，键面已实测：`n_components`／`planes_per_dim`／`hyperplanes_shape`／`code_len_bit`／`hex_width`／`d_over_2_reference`／`d_over_2_note`／`semantic_hash`／`byte_hash`／`dual`／`spec_ref_pending`）；⛔ 0 双写 |
| ②  | **顶层键** `protocol_version`（与 `corpus`／`generator_version`／`spec`／`index_v3_meta` 同级）＋ **伴生键** `protocol_version_axis`（见下） | `"V0.4"` | 同上 ⛔ 0 塞入 `index_v3_meta` |
| ③  | **顶层键** `protocol_version`（与 `task_id`／`caliber`／`input_selfcheck`／`degradation_guard` 同级） | `"V0.4"` | 同上 ⛔ 0 塞入 `input_selfcheck`（该面为**输入料自证面**，`191efa7fe0b6` L218-231） |

**⚠️ `protocol_version_axis` 伴生键之必要性（② 专属 · 「不误导」之直接落实）**

② 实测顶层并存**两条互不相干的版本轴**：`generator_version` ＝ `"v2.0.0"`、`spec` ＝ `"docs/SPEC_v2.0.md §1"`（**corpus 工具／corpus 规范轴**），而 `index_v3_meta.spec_ref_pending`／`spec_ref_base` 指向 P-D 指纹协议（**协议轴**）。**若只写入 `protocol_version="V0.4"` 而不声明其轴**，读者极可能将其误读为 corpus 版本 ⇒ **静默误导**。

⇒ **本棒口径固化**：② 新件**必须**伴生 `protocol_version_axis`，值为**明示 P-D 指纹协议轴**、并**明示与 `generator_version`／corpus `spec` 分属不同轴、互不覆盖**之声明串（**具体串文属 worker 拟定面，⛔ 0 由本棒代拟**；惟**声明义务与轴归属属本棒固化，不得省略**）。

> **若 PI/verdict 另裁「仅写单键、不加轴声明」** ⇒ 属**口径变更**，须走**口径固化流程**另立注记，⛔ 0 由 worker 现场自行简化。

### §3.4 出处字段联动表（改码**必改**之清单 · 与新名强耦合）

> **原理**：产出件之出处字段若仍指旧名/旧日期/旧脚本，产出件自身即成误导源（「不误导」之反面）。

| 字段 | 所在件 | 现值（实测） | **改码后必须为** | 行号锚 |
|---|---|---|---|---|
| `P_OUT_INDEX_V3` / `P_OUT_RESULTS` | R | 硬编码旧路径 | **新路径 ②①** | `de16bc002198` L62-63 |
| `REL_INDEX_V3` / `REL_RESULTS` | R | 旧相对路径 | **新相对路径**（②①） | 同上 L64-65；**二者喂入 `attach_integrity` ⇒ 0 改则 `integrity.path_hashed` 将记旧路径 ＝ 误导** |
| `DATE` | R | `"2026-09-29"`（**常量、0 wall-clock**） | **`"2026-10-09"`** | 同上 L49；写入 ①`date`／②`index_v3_meta.date` |
| `GENERATOR` | R | 旧脚本路径 | **新副本路径** | 同上 L78；写入 ①`generator`／②`index_v3_meta.generator` |
| `task_id` | R | `"V3X-C5B-RUNNER-2026-09-29-A1"` | **新档位标识**（含 10-09） | 同上 L283 |
| `index_v3_meta.spec_ref_pending` | R→② | 过时字面（见 §4 `K-PV02-04`） | **二择一，须跑前声明** | 同上 L76／L257 |
| `OUT` | G | 旧输出名 | **新输出名 ③** | `191efa7fe0b6` L42 |
| `generator` | G | 硬编码旧脚本名 | **新副本路径** | 同上 L209 |
| `task_id` | G | `"V3X-C5B-FIX-2026-10-01-A1"` | **新档位标识**（含 10-09） | 同上 L206 |
| `date` | G | **wall-clock**（L208 `datetime.now(...)`） | **保持 wall-clock**（⛔ 0 改为常量）⇒ 与旧件必不等，属**预期差异**，见 §4 `K-PV02-09` | 同上 L208 |

---

## §4 kill-line ／ pre-reg 补记面（**判死线先于实验 · 测量前冻结 · 事后 0 调**）

> **冻结声明**：本节全部判死线于**测量前**冻结（FTFB 内核）。跑毕**事后 0 调阈值、0 改判据、0 补判据**；若某条在跑前判定有歧义，**须在跑前提出并停手候裁**，⛔ 0 边跑边定。
> **编号自检**：全仓检索 `K-PV02` ＝ **0 命中** ⇒ **0 撞既有 `K-CF-1…6`（`4daaf68cbf0e` §4）／`K-V3DF-*`／`K-V3S-*` 族**。

### §4.1 沿用判死线（**全沿预登记字面 · 0 新设 0 改 0 调**）

| id | 判死线（沿用） | 来源 | 本次修订跑之适用 |
|---|---|---|---|
| `U-V04-01` | `protocol_version` 产出层缺口 —— 补齐归属 **verdict-keeper／PI** | `c13449101ab3` §2.4 L124／§7 L371 | **本次为其产出层半之执行面**；⚠️ **规则面 0 触**，且 **0 由本棒/worker 判其闭合** |
| 看护项 1/3/4/5 | `n_distinct ≤ 3` 退化警报（字段：`dual`／`semantic_hash`、`dual_hex_width`、`byte_hash`、`node_state`） | `2fd8946cfe80` §9 | 沿 `191efa7fe0b6` L194-203 之既有 guard 面；**判据字面 0 动** |
| 看护项 2 | 新 `b3_merkle_root` **等于** `75596bbabdb8` ⇒ 触「构造未变／未换坐标空间」警报 ⇒ **0 记为已修好**，判「不明」待核 | `2fd8946cfe80` §9 项 2 | 见 §5.3 双读法登记 |
| W-1…W-4／W-6／W-7 | （0 编造占位 root／**0 判档位**／缺 B 组原料时 0 强跑等） | `2fd8946cfe80` §8 | **维持全部**；⚠️ W-5 之有限解除见 §2.3 |
| W-5（余面） | ⛔ 改 V0.3／V0.2 任一字、⛔ 改 `ANCHORS`／构造常数／判定逻辑 | `2fd8946cfe80` §8 | **一字不得改** |
| 禁述六条 | ①0 说「C5 已修好／修好成立／坍缩已解除」②0 说「SVD-3 坐标坍缩命题已死」③0 以 `K-V3DF-5-1` PASS 外推「修好成立」④0 以均值 1.961→3.026 作「区分力改善」主张 ⑤**0 说「0 退化警报＝门通过」** ⑥**0 声称 `protocol_version` 键已写入产出件** | `0fd7a26fc339` L326（终稿 v0.3 L453 同） | **全条继承**；⚠️ **⑥ 之解除条件**：仅当 `K-PV02-01…09` **逐条 PASS 且以实测读数为证**时方可陈述「产出层新件已含该键」——**且须逐件点名新名**；⛔ 0 提前宣告、⛔ 0 以「新件已生成」代「键已写入且验收通过」 |

### §4.2 本次新立判死线（**新立 · 非阈值 · 停手条件**）

| id | 机械判据（可赋值） | 触发后处置 |
|:-:|---|---|
| **K-PV02-01** | 三件**新产出件**各 `protocol_version` **键级**命中 ＝ **1/件**，值逐字 ＝ `"V0.4"`（须以 `json.loads` 取键，⛔ **0 以子串命中充数**） | 任一件不满足 ⇒ **FAIL 停手**（沿 `4daaf68cbf0e` §4 `K-CF-3`「子串命中 ＝ 回显污染、0 采信」同族口径） |
| **K-PV02-02** | **出处面一致性**：①`generator`／`date`／`task_id`、②`index_v3_meta.generator`／`date`、②`integrity.path_hashed`、①`integrity.path_hashed` **六处**须全指**新**值；且 `integrity.path_sha256` ＝ `sha256(<新 relpath>)` **独立复算一致** | 任一处仍指旧值 ⇒ **判误导 ⇒ FAIL 停手**；⛔ 0 以「覆写旧件」补救 |
| **K-PV02-03** | **0 覆写面**：跑前对 **6 件**（①②③＋R＋G＋`c13449101ab3`）取 SHA-12 pin 并登记；跑后**逐件复算同值** | 任一漂移 ⇒ **停手**（⚠️ 原 `PINNED` 仅 pin 09-16 三件 `efe05ad775de`／`b5873afb9d29`／`d2cd7acb29a1`，**不覆盖 ①②③** ⇒ 本条为**新增 pin 面**） |
| **K-PV02-04** | **过时残留处置（跑前声明制）**：`SPEC_REF_V04`／`spec_ref_pending` 现值含「**(待 doc-writer 棒 2b 新增, 本件 0 代拟正文)**」，而该 spec **已在盘**（`c13449101ab3`／34,367 B）⇒ 跑前须**书面声明二择一**：① 去掉过时括注、改指在册 spec（建议附 SHA-12）；② 逐字沿用并**在回执登记为「过时残留」** | **0 声明而开跑** ＝ 静默沿用 ⇒ **判误导 ⇒ 停手** |
| **K-PV02-05** | **测量面零漂移（只许加键）**：新件 vs 旧件逐字段比对 —— **测量面**（① `per_caption[*].byte_hash/semantic_hash/dual/chain`、`chain_summary`、`caliber` 各数值项；② `captions`／`graphs`／`n_captions`／`fingerprint_anchors`／`index_v3_meta` 各**数值/内容**项；③ `per_caption`／`readings`／`cross_seed_control`／`degradation_guard`）**必须逐字相同**；**允许差异集合** ＝ ｛新增 `protocol_version`（＋②`protocol_version_axis`）、`date`、`task_id`、`generator`、`integrity.*`、`boundary.no_existing_file_modified` 同值不改｝ | 任一测量面字段变化 ⇒ **停手**，判「构造已变，**0 归因于改键**」，须回报 root/坐标面漂移嫌疑 |
| **K-PV02-06** | **drift 面 · 输入携带 0 重算**：新③件 `input_selfcheck.reproduce_max_abs_dev_vs_stored_svd2` ＝ `0.0089821568`、`reproduce_within_4dp` ＝ `false`，二者须**自 raw 原料件逐字携带**（`191efa7fe0b6` L224-225 读 `raw["reproduction_selfcheck"]`；raw 件 SHA-12 `1088fdd2b197`） | ⛔ 本次跑 **0 API／0 重取嵌入／0 重算 SVD**（`191efa7fe0b6` docstring L24 逐字「raw 22×2048 向量为上游 fetch 产物，本脚本只读」）⇒ **声称「drift 已消／已复测／已复现」＝ 误导 ⇒ FAIL** |
| **K-PV02-07** | **完整性自证面**：新①② `integrity.content_sha256` 按 `verify_integrity`（`de16bc002198` L122-126）口径复算 ＝ **True**；`self_check.integrity_index_v3_ok` ＝ `true`、`integrity_results_ok` ＝ `true`；`frozen_proof.unchanged` ＝ `true`；`zero_overwrite_proof.unchanged` ＝ `true`；术语红线 8 项 **0 命中** | 任一 false/命中 ⇒ **停手**（沿 runner 终验断言 L445-448） |
| **K-PV02-08** | **退化看护面**：新③件 `degradation_guard` **逐项与旧件同值**（实测旧值：`threshold_n_distinct_le`＝3、`semantic_hash_codelen_n_distinct`＝**9**、`root_predup_dual_n_distinct`＝**22**、`byte_hash_primary_n_distinct`＝**22**、`any_alarm`＝**false**） | 任一不等 ⇒ **停手**。⚠️ **口径澄清（禁述⑤ 之守护）**：`any_alarm=false` **仅覆盖该 guard 之 3 项**，⛔ **0 外推为「0 退化警报」** —— 10-01 已实测 **7 项 `n_distinct ≤ 3`** 命中项（`source`(2)／`captions[].family`(2)／`link_verified`(1)／`self_verified_only`(1)／`diff_*`(1×2)／root 三环并列(3)），见 `bff06d3b3f97` L146 |
| **K-PV02-09** | **时间面非确定性之诚实登记**：新③件 `date` ＝ **wall-clock**（必 ≠ 旧值 `2026-10-01T09:25:22+08:00`）⇒ ③ 新件 **byte 必变**、`content_sha256` 必变；此属 `K-PV02-05` **允许差异集**内 | ⛔ **0 以「③ byte 不等」推论「构造已变」**（反之亦然：⛔ 0 以「byte 相等」推论「构造未变」） |
| **K-PV02-10** | **root 面双读**：**(a)** 沿用看护项 2：新 `b3_merkle_root` **≠** `75596bbabdb8`；**(b)** 本次**新增停手条件**：新件 `b3_merkle_root` 须逐字 ＝ **`45ef859b2be9`**、`chain_summary.state_22_after_22_captions` ＝ **`bbd61495cb5d`**、`ext_1_after_anchor2` ＝ **`bf492f1c8424`**（三者皆为旧①件实测值） | (b) 任一不等 ⇒ **停手**，报「坐标面漂移嫌疑」。**口径声明**：(b) 系**新增停手条件**，**⛔ 不是阈值调整**、**⛔ 不改看护项 2 之字面**、**⛔ 不与看护项 2 混为一谈** |
| **K-PV02-11** | **禁触面**：⛔ 0 改 `c13449101ab3` 任一字（含 §2.4／§7 `U-V04-01` 字面）；⛔ 0 触 `2593ea7b93cf`、`bff06d3b3f97`、`1d1895489d17`、`87ab4929477f`；⛔ 0 跑 `.tmp/_v5_c5_b_fetch_raw_embeddings.py`（**0 API、0 key、0 网络**）；⛔ 0 合并任何派生 JSON；⛔ 0 判档位（PASS/FAIL/KD 归 verdict-keeper） | 任一触发 ⇒ **停手回报**；0 自行「顺手修正」 |

### §4.3 验收读数与停止条件（**收口判据 · 一句话可判**）

- **全部 PASS 之判据（且仅当）**：`K-PV02-01`…`K-PV02-11` **逐条 PASS**，且 `K-PV02-05` 之**测量面逐字比对表**已随回执落盘（⛔ 0 只报「已加键」而 0 交比对表）。
- **任一条 FAIL 之处置**：**立即停手 ＋ 如实回报 FAIL id ＋ 0 补救性覆写 ＋ 0 事后调判据 ＋ 0 改既有件**。
- **交棒边界**：本节 PASS ⇔ **仅**意味着「`protocol_version` 产出层载体在新名下**已落位且测量面未漂移**」；⛔ **0 由此外推**「`U-V04-01` 已闭合」「缺口已闭合」「C5 已修好」——**闭合判定归 verdict-keeper**。

---

## §5 root 漂移注记规格

### §5.1 读数口径定义（**口径定义 ≠ 阈值调整**）

| 项 | 定义与实测 |
|---|---|
| `reproduce_max_abs_dev_vs_stored_svd2` | ＝ 新调 API 之 SVD-2 与**盘上存储 `svd2_coords`**（源件 `c4b774c8e34c`）之**最大绝对偏差**；载体 ＝ raw 原料件 `reproduction_selfcheck.max_abs_dev_vs_stored_svd2`；**实测 `0.0089821568`**（raw 件 `1088fdd2b197` L264） |
| `reproduce_within_4dp` | 判据 ＝ `.tmp/_v5_c5_b_fetch_raw_embeddings.py` L134 字面 **`max_abs_dev <= 5e-4`**；实测 `8.98e-03 > 5e-4` ⇒ **`false`**（同件 L289） |
| **三形同值（计数/口径差登记）** | 同一读数在三处以**不同形**出现：① clue book `0fd7a26fc339` 条 4.27 ＝ `8.98e-03`；② 终稿 `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` L450 ＝ `8.98e-03`；③ raw 件精确值 `0.0089821568`。⇒ **三者同值不同形，⛔ 0 当作三个不同读数、⛔ 0 混列比较** |
| **⚠️ 容差名实不完全对齐（口径差登记 · ⛔ 0 据此改判）** | 字段名 `within_4dp`（4 位小数级）对应之**半 ULP 应为 `5e-5`**，而代码字面为 **`5e-4`**（**宽 10 倍**），且同行注释亦写「容差 **5e-5** 量级」⇒ **代码字面与注释字面亦不一致**。**方向性结论：本例 `8.98e-03` 对 `5e-4` 与 `5e-5` 均 > 阈值 ⇒ 两种口径下 `reproduce_within_4dp` 同为 `false`，故本注记成立性不依赖该差**；⛔ **0 据此改判、0 擅改该脚本**（属 W-5 面） |

### §5.2 登记口径（**写何处 · 怎么写 · 禁写什么**）

1. **载体位置**：漂移读数**已在**①（`input_selfcheck.raw_embedding_reproduction_max_abs_dev_vs_stored_svd2`／`raw_embedding_reproduces_stored_svd2`）与③（`input_selfcheck.reproduce_max_abs_dev_vs_stored_svd2`／`reproduce_within_4dp`）中**逐字在册** ⇒ 本次修订跑 **0 新增漂移字段、0 改漂移值**（`K-PV02-05` 测量面已含之）。
2. **⚠️ 键名别名之口径声明（易误读点）**：① 之键名 ＝ `raw_embedding_reproduces_stored_svd2`，③ 之键名 ＝ `reproduce_within_4dp`，**二者同指一读数**（别名，非两读数）⇒ 引用时**须注明取自哪件**，⛔ 0 跨件并列为两条独立证据。
3. **禁写清单（禁述④⑤ 之延伸）**：⛔ 0 写「复现稳定性已恢复」；⛔ 0 写「偏差已消／已收敛」；⛔ 0 因本次重跑而声称「跨棒复现稳定性 0 保证」之**反义**（即 0 声称「本次已重新验证稳定性」）；⛔ 0 将 `reproduce_within_4dp=false` 表述为「本次新增之失败读数」——**它是 2026-10-01 之既有读数之原样携带**。
4. **下游禁述继承**：`0fd7a26fc339` L326 禁述六条（含 ④「0 以均值 1.961→3.026 作『区分力改善』主张（**码长效应混淆**）」）**对本次新件一律继承**；新件 0 生成、0 引用任何「改善/修好」主张。

### §5.3 root 候选件 §9 看护项 2 之**双读法登记**（**本节为口径固化，防误读**）

| 读法 | 字面 | 本次修订跑之判定 |
|:-:|---|---|
| **（i）机械判据读法** | 看护项 2 字面：「新 `b3_merkle_root` **等于** `75596bbabdb8`」⇒ 触警报 | 新 root 逐字 ＝ **`45ef859b2be9`**（≠ `75596bbabdb8`）⇒ **不触发** |
| **（ii）风险面读法** | 10-01 之「非补跑」理由（`bff06d3b3f97` L160 逐字）：「补跑将重走 B3 chain 并**可能改写 root**（root 由 `dual` 派生）⇒ 触发 root 候选件 §9 看护项 2 之『构造未变／未换坐标空间』**警报面**」 | 本次为**覆裁后之定向修订跑**（构造面**不变**），其 root 是否逐字复现**由 `K-PV02-10(b)` 机械锁定**；若不等 ⇒ 即为坐标面漂移 ⇒ 停手 |

- ⛔ **0 把「（i）不触发」外推为「构造风险已排除」**；⛔ **0 记为「修好成立」**（禁述①）。
- ⚠️ 两读法**并存登记**，**不合并、不互相取消**；本棒 **0 裁定何者为 PI 所采**。

---

## §6 后续 worker 派工规格（**供 parent 照发派工单 · 本棒 0 派工**）

> **一句话规格**：**新建 R/G 两副本（0 触既有脚本），仅在产出字典新增 `protocol_version="V0.4"`（②另加 `protocol_version_axis`），把 5 类出处字段与写出路径随新名同步，跑两链（R 产出①②、G 产出③）落 2026-10-09 新名，6 件 pin 跑前跑后同值，交付测量面逐字比对表，按 `K-PV02-01…11` 逐条报读数，任一 FAIL 立即停手，0 判档位、0 回改、0 声称缺口闭合。**

| 项 | 规格（照此发单） |
|---|---|
| **棒别** | **worker**（执行棒）｜⛔ 0 由 protocol-keeper 代跑、⛔ 0 判档位 |
| **改何物** | ① **新建副本** `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py`（源 `de16bc002198`）② **新建副本** `.tmp/_c5_b_group_fix_readings_2026_10_09.py`（源 `191efa7fe0b6`）③ 于副本内：新增 `protocol_version` 键（②另加 `protocol_version_axis`）＋ 改 §3.4 表列 **5 类出处字段/路径** ＋（R）扩 `PINNED` 至 ①②③＋R 旧本＋G 旧本 |
| **⛔ 禁改** | 既有脚本 2 件、既有产出件 3 件、`c13449101ab3`、`2593ea7b93cf`、`bff06d3b3f97`、`1d1895489d17`；`ANCHORS`／`LSH_SEED`／`K_COMPONENTS`／`N_PLANE`／`HEX_WIDTH`／`FORBIDDEN_TOKENS`／判定逻辑，**一字不得改** |
| **跑法** | 先 R（缺 B 组原料即 `return 2` —— 属**预期**守卫，⛔ 0 绕过、0 造替代输入，W-7）→ 再 G；**0 跑 fetch 脚本**（0 API／0 key／0 网络）；G 须 0 网络 0 读 key（沿 `191efa7fe0b6` L24） |
| **新名落盘面** | ① `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json`｜② `corpus/v20/index_v3_2026_10_09.json`｜③ `results/c5_b_group_fix_readings_2026_10_09.json`（三新名落前 `Test-Path=False` ＋ glob 0 命中，**须回报实测**） |
| **验收口径** | `K-PV02-01…11` **逐条报读数**（PASS/FAIL ＋ 实测值 ＋ 实测命令）＋ **交测量面逐字比对表**（新 vs 旧，列出 0 差异项与允许差异项）＋ **6 件 pin 前后同值表** ＋ 3 新件 SHA-256／SHA-12／bytes／CRLF **自报**（写入方实测，0 自指） |
| **回执须含** | ① 每条 K-线之**实测读数**（⛔ 0 只报「已加键」）② `spec_ref_pending` 过时残留之**跑前二择一声明**（`K-PV02-04`）③ 0 回改自证（6 件 pin ＋ 3 件既有产出件）④ 0 网络／0 key／0 判档位自陈 ⑤ **未做面显式列出**（沿项目既有诚实体例） |
| **停手条件** | `K-PV02-01…11` 任一 FAIL ⇒ **立即停手回报**（0 补救性覆写、0 事后调判据、0 改既有件） |
| **交棒** | 产物交 **verdict-keeper** 判 `U-V04-01` 产出层之闭合与否；⛔ worker 与本棒均 **0 判** |

---

## §7 附记（口径/引用差登记 · ⛔ 0 回改母件）

1. **缺口排期母件 V3-02 行引用错件（沿 `1d1895489d17` §4）**：`results/_v34_experiment_gap_plan_2026_10_08.md`（`996feb1db9cb`／36,066 B）L78 载「已由 **`423c84de20d5`** §2.4 承载规则」，而 **`423c84de20d5` ＝ `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`**（P-B 失真界 V0 规格件／15,457 B），该件 `protocol_version` 命中 **0**、其 §2 为「锚点（pre-registered SHA-256 前 12 位）」**无 protocol_version 规则面** ⇒ **V3-02 行所引非规则载体**；规则面真实唯一载体为 **`c13449101ab3` §2.4**。⚠️ **本次修订跑之规则依据必须取 `c13449101ab3`**（本件 §3.3 已取对）⇒ **该母件之错引 0 追改，仅登记**，供 parent 择机并入勘误链。
2. **`W-5` 之既有依赖面**：W-5 原字面含「（含 `SPEC_REF_V04`）」，与 `K-PV02-04` 之过时残留处置**同指一字面** ⇒ 本次对该字面的处置**已由 PI 覆裁有限解除**（§2.3），**其余 W-5 面维持**。
3. **本棒 0 自造任何外部专有名词/文献号/定理名**：全件所引均为**盘上件之字面与行号**，0 引任何外部定理或文献。

---

## §8 0 回改与纪律自查

- **写入面 ＝ 仅本件 1 件（新名）**；既有件 **byte 0 触动**（§8.2 回执行）。
- **0 改码 · 0 跑产出链**：本棒 **未修改任何脚本**、**未执行 runner／生成器**；§3–§4 全部为**规格与判死线**，非已执行之动作。
- **0 判档位 · 0 代裁**：PI 择档已定（乙）；本棒 0 择档、0 代裁其未明示之细节、0 宣告缺口闭合、0 判 C5 生死。
- **0 编造**：全部指纹/字节/行号/键名/读数 均为本 Turn 实测；PI 新裁字面**如实标注为派工单转录（L2）**并声明回执原件 0 自读（§1）。
- **0 网络 · 0 端点 · 0 key**：0 网络调用、0 读 `.env`／key，**R4 key 永不明文**；⛔ 未打开 `config.yaml`／`mcp.json`／任何凭据面。
- **0 合并派生 JSON · 0 触 frozen**：本件 0 产出／0 合并任何 JSON；⛔ 0 触 `corpus/v20/index.json`（frozen base，实测 `8423ffe266af`）。
- **0 阶段名自升**：全件 `V0.4`／`V3-02`／`v0_4`／`v3` 字样**均为既有件既有字面之引用**；本件名 0 含 V-阶段前缀，**0 新造任何阶段名/版本号**。
- **预登记状态**：**待 PI 复核生效，生效即锁**（跑前若有歧义 ⇒ 提出并停手，⛔ 0 边跑边定）。

### §8.2 本棒实测指纹回执行（供 parent 复核 · 本件 0 自指 SHA）

| 路径 | SHA-12 | 字节 | 本棒读法 |
|---|---|---:|---|
| `results/_protocol_version_landing_status_2026_10_09.md` | `1d1895489d17` | 11,562 | 全文读（§4–§5 重点）· CRLF 0 |
| `results/_g4_reproduction_execution_register_2026_10_09.md` | `4daaf68cbf0e` | 20,414 | §4 判死线体例／§5.2 改前清单体例（只读引用） |
| `results/_pending_pi_items_master_register_2026_10_09.md` | `87ab4929477f` | 35,258 | §5 Q4 原题面（只读引用） |
| `results/_mini_round_3_decisions_register_2026_10_01.md` | `bff06d3b3f97` | 44,308 | §1 Q1②／§2.1.2 原裁字面 |
| `results/c5_protocol_version_annex_2026_10_01.md` | `2593ea7b93cf` | 18,558 | 原裁承载件（0 触） |
| `results/c5_b_group_root_candidate_2026_10_01.md` | `2fd8946cfe80` | 28,867 | §9 看护项全表／§8 W-1…W-7／§11 口径声明 |
| `results/_naming_ruling_note_2026_09_29.md` | `57024f2cd30a` | 7,843 | §1.2①②命名口径 |
| `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | `c13449101ab3` | 34,367 | §2 表 L105／§2.4 L109-L126（规则面唯一载体） |
| `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | `de16bc002198` | 20,322 | **只读**：L40-126／L222-263／L262-318／L332-453 |
| `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` | `191efa7fe0b6` | 12,014 | **只读**：L1-60／L190-273 |
| `.tmp/_v5_c5_b_fetch_raw_embeddings.py` | `8e4f2ae63de3` | 9,476 | **只读**：L132-137（容差字面） |
| `results/_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | `1088fdd2b197` | 744,352 | **只读**：`reproduction_selfcheck`（L262-290） |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | 20,398 | 顶层键面／`chain_summary`／`caliber` 键／`spec_ref_pending` L21 |
| `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | 24,421 | 顶层键面／`index_v3_meta`／`spec_ref_pending` L549 |
| `results/c5_b_group_fix_readings_2026_10_01.json` | `2a7749da7c4d` | 9,996 | `degradation_guard`／`input_selfcheck`／`boundary` |
| `corpus/v20/index.json`（frozen base） | `8423ffe266af` | 7,335 | 存在性（0 触） |
| `corpus/v20/strip_captions_22.json` | `6a2656878745` | 12,798 | 存在性（0 触） |
| `results/deposon_v2_phase4_f4_2026_09_11.json` | `cf7682348617` | 5,212 | 存在性（0 触） |
| `results/_v34_experiment_gap_plan_2026_10_08.md` | `996feb1db9cb` | 36,066 | §7 附记 1（0 触） |
| `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15,457 | §7 附记 1（0 触） |

**自报值对账（0 信自报 · 本棒独立复算）**：③件 `input_selfcheck` 自报之输入 SHA-12 ＝ `1088fdd2b197`（raw）／`cf7682348617`（f4）／`6a2656878745`（captions），**本棒逐件 `Get-FileHash` 复算，三项逐字吻合** ✅。

> 本件落盘后自身 SHA-256／SHA-12／字节／行尾（UTF-8 无 BOM · LF）**由写入方实测回报**（0 自指）。