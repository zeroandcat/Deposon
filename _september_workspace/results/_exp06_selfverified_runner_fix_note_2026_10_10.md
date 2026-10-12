# EXP-06 · runner `self_verified_only` 硬写修正 · 同步注记件 · 2026-10-10 · 新名件

> **定位**：本件 ＝ PI「**授权 runner 修正**」裁之**修侧落地球**（同步/落实注记），配套交付：修正版 runner 副本（新名件 ①）＋ 本注记件（②）。
> ⛔ **0 回改原件 `de16bc002198` 1 byte**（跑前＝跑后复测一致，见 §6）｜⛔ **0 重跑任何实验载荷**（本棒只出件，修正版 runner **未运行**、未生成任何产出）｜⛔ **0 改任何既有产出件**｜⛔ **0 网络**／⛔ **0 skill**／⛔ **0 LLM**／⛔ **0 读 key**。

**授权锚**：PI 2026-10-10 10:39「轮 34」卡（`ask_2901c721b5788ebbb00670a5` step `exp06_finds`）逐字 —— 「**授权 runner 修正**」
**勘误源**：`results/_exp06_supplement_four_gaps_2026_10_10.md`（`9f86cc5be8e9`）§2.3.3 ＋ §3 勘误登记 `E-EXP06-S3`
**规格源**：`results/_criterion_application_scope_prereg_2026_10_01.md`（`c4e3338619c6`）§3.3②

**棒序**：`worker` · EXP-06 修正/同步件 · 2026-10-10。

---

## §1 交付物与指纹（逐件实测）

| # | 件 | 路径 | SHA-12 | bytes | BOM | CRLF |
|:-:|---|---|---|:-:|:-:|:-:|
| ① | **修正版 runner 副本** | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py` | 见**回执** | 31,457 | NO | 0 |
| ② | **同步/落实注记**（本件） | `results/_exp06_selfverified_runner_fix_note_2026_10_10.md` | 见**回执**（自指不可内嵌） | — | NO | 0 |

**读盘锚（逐件复算一致）**

| 锚 | SHA-12 | 路径 | 本棒角色 |
|---|---|---|---|
| 原件（修正对象） | `de16bc002198` | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py`（20,322 B · 453 行） | ⛔ **0 回改** |
| 同形 10-09 版（**本棒 0 修**） | `7c095c54fb99` | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py`（21,826 B · L248 同形硬写） | 见 §7 残留登记 |
| 产出件（读数面） | `33ad1c01f745` | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json`（20,398 B） | ⛔ **0 改**；读数 0 变 |
| 索引件 | `3ba2449cf986` | `corpus/v20/index_v3_2026_09_29.json` | ⛔ **0 改** |

**修正版之输出路径（新名 · 本棒未生成 · `Test-Path` 预期 False）**
- `corpus/v20/index_v3_selfverify_fix_2026_10_10.json`
- `results/deposon_p_d_b3_merkle_22_caption_selfverify_fix_2026_10_10.json`

⇒ 二者均为新名，⛔ **不可能覆写**原件两产出（原件产出路径已在副本内改写，见 §3）。

---

## §2 缺陷实体与规格要求（核清结果 · 自读原文）

### §2.1 硬写语段 · 逐字（原件 `de16bc002198` L230‑L232）

```python
    for c in per_caption:
        c["chain"]["link_verified"] = rewalk_ok
        c["chain"]["self_verified_only"] = True      # ← 硬写：无条件字面量
```

**语义上下文（原件 L220‑L229 逐行核）**：`rewalk_ok` 为**真求值**变量 —— 初值 `True`（L222），任一 `node_state` 不符即翻 `False`（L223‑L226），再与重导 `ext_1`／`root` 比对并 AND（L229）。
**故**：`link_verified = rewalk_ok` ✅ 真求值；紧邻之 `self_verified_only = True` ❌ **不读 `rewalk_ok`、0 任何比较、0 任何探测** ⇒ **该位之 `true` 值并非由任何验证面求出**。
**同形**：10-09 版 L246‑L248 逐字同构（本棒 0 修，见 §7）。

### §2.2 规格要求（`c4e3338619c6` §3.3② · 逐字）

> **② 全 `true` 独立验证件** ｜ 最小落面要求：**全 `true` 字段须附独立验证件（可核、0 与被验证件同源）；0 预置为 `true`** ｜ 缺位后果：**豁免不成立 ⇒ 回落受门**

配套 §3.3①：**取值语义声明**（逐字段声明**置位者／置位时机／依据件**三要素）。
配套 §3.3④ 之同族纪律：**0 记为通过、0 静默**。

---

## §3 修正内容（唯一语义改动 ＋ 身份改写，严格分离登记）

### §3.1 语义修正 · 1 处站点（原 L232 → 副本 L347）· **唯一**

| 项 | 行（原件 → 副本） | 原字面 | 修正字面 |
|:-:|---|---|---|
| ★ | **L232 → L347** | `c["chain"]["self_verified_only"] = True` | `c["chain"]["self_verified_only"] = bool(rewalk_ok) and not indep_verified` |

**配套新增站点（非独立改动面，为使该修正成立所必需，逐项登记）**

| # | 副本行 | 内容 | 为何必需 |
|:-:|---|---|---|
| 1 | L341‑L342 | `indep = probe_independent_evidence(BASE, GENERATOR)`／`indep_verified = indep["status"] == "verified"` | `indep_verified` 之定义源；⛔0 则修正式无变量可依 |
| 2 | L189‑L189 | `INDEP_VERIFY_DECL = None` | §3.3②「须附独立验证件」之**声明位**（本副本 0 声明 ⇒ status=`not_declared`） |
| 3 | L192‑L238 | `probe_independent_evidence()`（56 行） | 独立验证面之**运行期实测**（在位／哈希／异源三判） |
| 4 | L338‑L366 | 5b 段：随件声明三要素 ＋ `independent_verification_ref`／`_status`／`independence_deficiency_alarm` | §3.3① 三要素落面 ＋ §3.3②「附件」指针 ＋ §3.3④ 同族「0 静默」 |
| 5 | L503‑L525 | 顶层 `independence_verification` 节（23 行） | 布尔位**全局**判定面（三要素 ＋ 探测记录 ＋ burden 满足与否） |
| 6 | L547‑L552 | `runner_fix_notice`（6 行） | 产出件自述「由修正版副本生成」，供后续读者溯源 |

### §3.2 选定修正形式之论证（四条理由）

| # | 候选形式 | 是否采纳 | 理由 |
|:-:|---|:-:|---|
| **1** | **动态求值 ＋ 计算来源标注 ＋ 独立面探测 ＋ 欠缺警报**（本棒采纳） | ✅ | 同时满足 §3.3①（三要素可核）＋ §3.3②（值由实测求值、⛔0 预置）＋ §3.3④ 同族（0 静默）；且**读数字面不变**（22/22 仍 `true`，当独立面未获 verified 时），不引翻任何既往读数 |
| 2 | 纯动态求值（只改 L232 一行） | ❌ | 值虽可求值，但**独立验证面 0 探测、0 声明、三要素 0 落面** ⇒ §3.3① 之「置位者／时机／依据件」仍缺位 ⇒ 修正不完整 |
| 3 | 移除该位（删键） | ❌ | 产出件 schema 变更 ＋ **必改 `content_sha256`** ⇒ 波及 `33ad1c01f745` 之自校验链；且 §3.3③「0 声称豁免＝该位无缺陷」下**删位不等于修正**，属另案（须 PI 裁） |
| 4 | 仅加注释声明「此为有意设计」 | ❌ | 注释不改变求值性质 ⇒ 实现级张力**原样留存**，不满足 §3.3② |

**采纳形式之值语义（明确写出，防误读）**：`self_verified_only = (自证复走成功) 且 (独立验证面未取得 verified)`。
即「本记录之验证**仅**由自证复走支撑」—— **当且仅当**该断言于运行期被实测确认时置 `true`；若日后独立验证件在位且异源通过探测，该位自动翻 `false`（**诚实**：届时「仅自证」即不成立）。

### §3.3 身份改写 · 13 行 · **0 语义影响**（必要性逐行给据）

| # | 原件行 → 副本行 | 改动 | 必要性（不给据则副本坏了或原件遭殃） |
|:-:|---|---|---|
| 1 | L2 → L2‑L48 | 插入 47 行授权/缺陷/修正形式/纪律头块 | 修正版须自述授权锚、缺陷实体、改动面（沿 Q-3 修正先例体例） |
| 2 | L3 → L50‑L51 | docstring 首行 → 「CORRECTED COPY」自述 | 自述准确 |
| 3 | L5‑L8 → L53‑L56 | docstring `task_id`／两 out 件名 → 新名 | 自述准确 ＋ **输出路径自述须与实际常量一致** |
| 4 | L49 → L97 | `DATE` `2026-09-29` → `2026-10-10` | 产出件 `date` 字段须为副本落盘日 |
| 5 | L61‑L65 → L109‑L113 | 两组输出路径常量 → 新名（4 行）＋ 段注释 | **不给据则副本一跑即覆写 `33ad1c01f745`** ⇒ 违反 0 回改 |
| 6 | L72‑L74 → L120‑L123 | `PINNED` 追加 3 件既有产出/原件 pin | 沿 10-09 runner L82‑L86 同款纪律：0 覆写既有产出须 pin |
| 7 | L78 → L130 | `GENERATOR` → 副本自身路径 | 产出件 `generator` 字段须自述真实来源 |
| 8 | L283 → L417 | `task_id` → `V3X-C5B-RUNNER-2026-10-10-A1-FIXCOPY` | 产出件 `task_id` 须区分原件批次 |

### §3.4 0 改动面（逐项明示）

- **常量**：`K_COMPONENTS=3`／`PLANES_PER_DIM=6`／`N_PLANE=18`／`CODE_LEN_BIT=18`／`HEX_WIDTH=5`／`D_OVER_2=9.0`／`LSH_SEED=42` —— **一字未动**。
- **`ANCHORS`／`PINNED` 原 3 项／`SPEC_REF_*`／`ANCHORS_REF`／`FORBIDDEN_TOKENS`／`PROTOCOL_*`** —— 一字未动（10-09 版之 `PROTOCOL_VERSION` 等**不在**本副本基线内，本棒 **0 引入**）。
- **链式构造四式（L208‑L218）、自证复走段（L220‑L229）** —— 一字未动。
- **索引件装配段／`diff_registration` 段／`decision_lines_36_substitute` 段／`cross_source_2model_087` 段／收尾三写与红线段** —— 一字未动。
- **`self_verified_only` 赋值站点数不变**：原件 1 处 → 副本 1 处（仅值表达式改）。

### §3.5 逐行 diff 登记（机器复算 · `difflib.SequenceMatcher`）

| 区 | tag | 原件行 | 副本行 | 原行数 | 副本行数 |
|:-:|---|---|---|:-:|:-:|
| 1 | insert | L2 前 | L2‑L48 | 0 | **47** |
| 2 | replace | L3 | L50‑L51 | 1 | 2 |
| 3 | replace | L5‑L8 | L53‑L56 | 4 | 4 |
| 4 | replace | L49 | L97 | 1 | 1 |
| 5 | replace | L61‑L65 | L109‑L113 | 5 | 5 |
| 6 | insert | L72 前 | L120‑L123 | 0 | **4** |
| 7 | replace | L78 | L130 | 1 | 1 |
| 8 | insert | L131 前 | L183‑L238 | 0 | **56** |
| 9 | insert | L230 前 | L338‑L343 | 0 | **6** |
| 10 | replace | **L232** | L346‑L366 | **1** | **21** |
| 11 | replace | L283 | L417 | 1 | 1 |
| 12 | insert | L369 前 | L503‑L525 | 0 | **23** |
| 13 | insert | L390 前 | L547‑L552 | 0 | **6** |

- **改动区数**：**13** ｜ **原件被触及行**：**14** ｜ **副本新增/改写行**：**177**
- **行数**：原件 **453** → 副本 **616**（净增 **163**）
- **唯一语义改动**：区 **10**（原 L232 单行 → 副本 21 行）；其余 12 区 ＝ 头块插入 ＋ 身份改写 ＋ 配套新增站点（§3.1 之 2‑6 项 ＋ §3.3 之 1‑8 项）。

---

## §4 验证（静态级 · **0 运行本修正版**）

| # | 项 | 方法 | 结果 |
|:-:|---|---|---|
| 1 | 语法/语义可编译 | `ast.parse` ＋ `compile()` | ✅ **PASS** |
| 2 | **硬写残留**（AST 级） | 遍历 `ast.Assign` 之 `Subscript` 目标键 `self_verified_only` | ✅ 副本**唯一**赋值站点 L347 ＝ `bool(rewalk_ok) and (not indep_verified)`；原件站点 L232 ＝ `True` |
| 3 | 字面量残留 | 全文计数 `"self_verified_only"] = True` | 命中 **1** 处 ＝ **L16 头块注释内之「文档引述」**（沿 Q-3 先例之审计提示：**⛔0 以注释判读站点**，判读以 AST 为准） |
| 4 | 新增键面在位 | 6 键逐一 grep | ✅ `self_verified_only_basis`／`independent_verification_ref`／`independent_verification_status`／`independence_deficiency_alarm`／`independence_verification`／`runner_fix_notice` 全在位 |
| 5 | 探测函数在位 | 文本在位性 ＋ `ast.parse` 通过 | ✅ `probe_independent_evidence()`（L192‑L238）、`INDEP_VERIFY_DECL`（L189） |
| 6 | 身份接线 | 输出路径／`GENERATOR`／`task_id`／`DATE` 逐一核 | ✅ 全部指向新名（§3.3 表） |
| 7 | **原件 0 回改** | 跑前 SHA-12 `de16bc002198` ／跑后复测 | ✅ **一致**（20,322 B ／ 453 行 ／ ⛔0 改 1 byte） |
| 8 | 编码/行尾 | 逐件字节实测 | 副本 **BOM=NO · CRLF=0**（沿原件 LF 体例） |

**⛔ 本棒 0 做**：⛔ **0 运行**修正版 runner（故其输出 JSON **不存在**）｜⛔ **0 生成任何产出件**｜⛔ **0 网络**｜⛔ **0 skill**｜⛔ **0 LLM**｜⛔ **0 判档**（**0 出 PASS/FAIL/KD**；判定归口＝verdict-keeper）｜⛔ **0 改任何既有产出件**。

---

## §5 影响面

### §5.1 对既有产出件与既有读数：**读数字面 0 变**

| 面 | 读数现状 | 本修正之影响 |
|---|---|---|
| `33ad1c01f745` 之 `per_caption[].chain.self_verified_only` | **22/22 `true`** | **0 变** —— ⛔0 回改该件、⛔0 重跑 ⇒ 该件仍载原件所写之 `true`；其**求值来源之缺失**已由本修正版**面向未来**解决 |
| `link_verified`／`chain_summary.independent_rewalk_ok` | 22/22 ／ `true` | **0 变**（二者本已真求值） |
| 链根三环（`state_22`／`ext_1`／`b3_merkle_root`） | `bbd61495cb5d`／`bf492f1c8424`／`45ef859b2be9` | **0 变**（本修正 0 触链式构造与四式） |
| `dual_hex_width`／`diff_registration_*` | 22/22 ＝ 11 ／ 各计数 | **0 变** |
| 自校验链（`content_sha256`／`path_sha256`／`anchor_sha256`） | 三条全 MATCH | **0 变**（⛔0 写该件 ⇒ 哈希不动） |

### §5.2 「面向未来」之生效条件（须重跑方生效）

- 修正版 runner **未运行** ⇒ 盘上**无**任何新产出。
- 日后若以本副本重跑，则 `self_verified_only` 之值**由运行期实测求值**；当 `INDEP_VERIFY_DECL` 仍为 `None`（0 声明）时读 `true`（读数与现状同）＋ **`independence_deficiency_alarm=true`** 显式亮起（**0 静默**）。
- 若日后填入**异源**独立验证件并重跑 → `independence_verification_status` 转为 `verified` → `independence_burden_satisfied=true` → `self_verified_only` **翻 `false`**。**此为设计意图之诚实表现**（届时「仅自证」不成立），⛔ 非读数错误。
- **⚠️ 重跑会产出新名产出件（新指纹）**；既有 `33ad1c01f745` **不受影响**，⛔0 需翻案。

### §5.3 对 10-09 版（`7c095c54fb99`）之影响：**0**（本棒 0 修，见 §7）

---

## §6 0 回改确认（逐件复测）

| 件 | 跑前 SHA-12 | 跑后 SHA-12 | 判定 |
|---|---|---|:-:|
| `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | `de16bc002198` | `de16bc002198` | ✅ **0 回改**（20,322 B · 453 行 · 未动） |
| `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | `7c095c54fb99` | 未触 | ✅ **0 触及** |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | 未触 | ✅ **0 触及** |
| `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | 未触 | ✅ **0 触及** |
| `results/_exp06_supplement_four_gaps_2026_10_10.md`（勘误源） | `9f86cc5be8e9` | 未触 | ✅ **0 触及** |
| `results/_criterion_application_scope_prereg_2026_10_01.md`（规格源） | `c4e3338619c6` | 未触 | ✅ **0 触及** |

---

## §7 残留与未代裁项（如实登记 · **0 推断 · 0 代裁**）

| # | 项 | 事实 | 处置 |
|:-:|---|---|---|
| **1** | **10-09 版 L248 同形硬写** | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` L246‑L248 与原件**逐字同构**（`self_verified_only = True`） | **本棒 0 修**（授权锚指向 EXP-06 之产出件置位者 ＝ 09-29 版）；**登记待裁** —— 是否同式另立修正版副本，**归 PI** |
| **2** | **键名与规格之结构性张力** | 键名 `self_verified_only` 之语义（「验证仅由自证支撑」）与 §3.3②「全 `true` 须附独立验证件」存在**定义层张力**：若验证确为「仅自证」，则按定义无独立验证件可附 | 本棒 0 代裁「改键名／拆位／改语义」；只落「可求值化 ＋ 可核化 ＋ 不静默」三项；**是否进一步改键名须 PI 另裁** |
| **3** | **`INDEP_VERIFY_DECL = None`** | 本副本**0 声明**独立验证件（⛔0 以自身产出充当独立验证件，违 §3.3②「0 与被验证件同源」） | 为**设计态**而非缺陷；填入异源件后重跑即生效（§5.2） |
| **4** | **修正版未运行** | 运行时行为**未证**（沿勘误源 §2.3.4 同款诚实限度） | 如实登记；本棒 0 重跑（授权面仅「修正」） |
| **5** | **硬写是否为有意设计** | 原件源码 **0 陈述**该位之设计意图 | ⛔ **0 推断**（沿勘误源 §2.3.3 同款限度） |
| **6** | **未审面** | 本棒**0 核读**冻结升级件 `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` 正文（沿勘误源 §2.3.4 同款限度） | 如实登记 |

**⚠️ 0 判档（铁律）**：本件 **0 判 `K-CF-4` 任何档位**、⛔ **0 出 PASS/FAIL/KD**、⛔ **0 断「豁免成立否」** —— **判定归口＝verdict-keeper**。

---

## §8 体例与纪律自检

| 项 | 状态 |
|---|:-:|
| 命名合规（`_主题_日期`、⛔0 `_v5_`/`_v4_`/`_v3_` 等 V-阶段前缀、⛔0 阶段号作首段） | ✅ `…_selfverify_fix_2026_10_10.py`／`_exp06_selfverified_runner_fix_note_2026_10_10.md` |
| 修正版与注记件**分离**（沿 Q-3 修正先例：副本头块内载同步件路径） | ✅ |
| 身份改写与语义改动**严格分离登记** | ✅ §3.1 vs §3.3 |
| 逐件实测指纹（SHA-256／SHA-12／bytes／BOM／CRLF） | ✅ §1 ＋ 回执 |
| 工具件标注（**0 属证据面**） | ✅ `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py`（沿先例 `.tmp/c5_guard_minmaxstd_2026_10_01.py`） |
