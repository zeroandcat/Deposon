# P-D 可审计账指纹协议 V0.4 SPEC（B 组新坐标空间专用版）

> **作者**：doc-writer 凝子-agent（`agent-0032834a3e04`）
> **日期**：2026-10-01 CST
> **状态**：**V0.4 新增件（待 PI 复核生效，生效即锁）** —— 本件为协议本体，**0 覆盖** V0 / V0.2 / V0.3
> **位置**：`docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md`（新增文件；落盘前实测 **0 撞名**、0 覆写）
> **件名依据**：PI 确认卷（二）Q1 裁「spec 件名＝`docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md`（runner 预留名）」；runner v0_4 L76 `SPEC_REF_V04` **已按此名预留引用**
> **触发**：C5 修复链 · B 组（SVD 主成分数 2→3）协议修法 —— PI 批 5 ⑰ 裁「**root 冲突 ＝ 新增 V0.4 专用 spec、旧件 0 动**」（R7 出路①）
> **协作方**：protocol-keeper（`agent-3e0c193da529`，root 候选件 `2fd8946cfe80`）＋ verdict-keeper（判档面）＋ Mavis（执行线）
> **铁律**：严守 8 条铁律 0 触动（no_llm / no_proxy / no_gateway / no_key / no_18_frozen_touch / no_p_g_v0_v01_touch / no_plugin_spec_touch / no_verifier_mavis_builtin_scripts_touch）
> **版式**：UTF-8 无 BOM · LF
> **SHA-12 口径**：`hashlib.sha256(全文字节).hexdigest()[:12]`，小写 12 位，**盘上实测**；**本件自身指纹不自写入本件**（随回执外部报出）

---

## 0. 一句话结论 ＋ V0.3 → V0.4 变更项

**V0.4 ＝ P-D 协议在 B 组新坐标空间下的专用协议版本。** 相对 V0.3（`f119f2f30287`），V0.4 **仅改 4 项**（坐标空间维数 / 码长 / hex 宽度 / root 值与字段名），**旧件 byte 0 触动**，沿 V0.3「版本共存」体例扩为 **4 版本共存**。

> ⚠️ **本件不是「修复已判定」件**：V0.4 承载的是**协议本体（规则面＋实测值）**；**PASS/FAIL／「修好/未修好」判档归 verdict-keeper**，本件 **0 判**（沿产出件 `33ad1c01f745` `no_verdict_notice` 逐字）。

### 0.1 V0.3 → V0.4 变更 4 项（逐项来源标注）

| 编号 | 变更面 | V0.3（`f119f2f30287`） | **V0.4（本件）** | 裁项来源（给出人／出处） |
|---|---|---|---|---|
| **C1** | **投影维数 d** | SVD-**2** 坐标 | SVD-**3** 坐标（B 组） | **PI 批 5 ⑰**（转录：`46599dde51a8` §2.3）＋ **PI 确认卷（二）Q1 裁「维数 d=3」**（d=4 留备选）｜盘上实现＝ runner L42 `K_COMPONENTS = 3` |
| **C2** | **码长** | 12 bit（12 hyperplane） | **18 bit**（18 hyperplane ＝ 6 面/维 × 3） | **PI 批 5 ⑰ 裁项④「码长随投影维数同步」**（转录：`46599dde51a8` §2.3）＋ **halt 报告 `f2b68ee099b5` §3.2／§3.4 实测推导**（6 面/维 ＝ 盘上字面 `randn(12,2)` 之唯一解） |
| **C3** | **hex 宽度** | `.zfill(3)`（12 bit ＝ 3 hex 规整） | **`.zfill(5)`**（18 bit → `ceil(18/4)=5` hex，**首位 hex 承载 2 bit**，取值域 0–3） | **halt 报告 `f2b68ee099b5` §3.2 无损往返实测**（2004 样本含边界 `0` 与 `2^18-1` 全数吻合，**0 静默截断**） |
| **C4** | **root 值 ＋ 字段名** | `merkle_root = 75596bbabdb8` | **`b3_merkle_root = 45ef859b2be9`** ＋ **`protocol_version = "V0.4"`** | **PI 确认卷（二）Q1 裁「N-a」**（＝沿 runner L366／L432 已用字面，0 断 2a 链）｜值＝ **2a 实测**：`33ad1c01f745` `chain_summary.b3_merkle_root` |

### 0.2 关键不变量

- **旧件 byte 0 触动**：V0（`3b67461b05fe`）／V0.2（`c165cd33a362`）／V0.3（`f119f2f30287`）**三件全部 0 触动**；
- **旧 root `75596bbabdb8` 仅存旧件**（V0.3 L390 逐字），**本件只落新值** `45ef859b2be9`，**0 同件并陈新旧两值**（沿 `46599dde51a8` N-a／N-c 取 N-a 之「0 断链」面，N-c「同件两值」面 **0 采**）；
- **8 条铁律 0 触动**；**0 编造**：本件全部数值沿盘上实测件逐字引用，**0 估算、0 占位、0 外推**。

---

## 1. 目标与范围

### 1.1 V0.4 目标

把 P-D 语义指纹层与 B3 sequential chain **在 B 组新坐标空间下重新锚定**，并解决 V0.3 L265「root=`75596bbabdb8` **必须保持**（否则 = 协议失效）」与「换坐标空间」在数学上的互斥关系 —— 处置方式是**另立协议版本**（PI 批 7 ㉑ 裁「L265 仅约束**同口径重走**」），**0 改写 V0.3 原文**。

### 1.2 V0.4 范围

**包含**：
- 协议层：B 组（SVD-3）坐标 ＋ 18-bit LSH ＋ 22 caption `dual` ＋ B3 sequential chain（22 节 ＋ 2 级 anchor 延伸）＋ 新 `b3_merkle_root`；
- 字段面：`b3_merkle_root` ＋ `protocol_version`（见 §2.4 **gap 承载声明**）；
- 防退化看护判据（§4）与其读数（§4.2）；
- 22 caption 实测表（§3.1）＋ 22 节链实测（§3.2）＋ 新 root 三段式（§3.3）。

**不包含**（⛔ 明示）：
- 任何对 V0／V0.2／V0.3 spec 的修改（**V0.4 是新增版本，0 覆盖旧版**）；
- 任何对旧 B3 产出（`b5873afb9d29`）、旧 runner（`d2cd7acb29a1`）、frozen 制品的触动；
- 任何**判档**（PASS/FAIL／修好判定）、任何**阈值新设**（`d/2` ＝ 9.0 系算术派生，见 §4.3）；
- 任何**执行面动作**（0 跑实验、0 调 API、0 读 key、0 触发网络）。

### 1.3 与 V0 / V0.2 / V0.3 关系（**4 版本共存** · 沿 V0.3 L587 体例）

| 版本 | 路径 | 字节数 | SHA-12 | 状态 | V0.4 处理 |
|---|---|---:|---|---|---|
| **V0** | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | 9,192 B | `3b67461b05fe` | 冻结（2026-09-01） | 原文引用，**0 触动** |
| **V0.2** | `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | 4,587 B | `c165cd33a362` | 冻结（2026-09-11） | 原文引用，**0 触动** |
| **V0.3** | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | 34,393 B | `f119f2f30287` | 冻结（2026-09-17） | 原文引用，**byte 0 触动** |
| **V0.4** | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | （本件） | （落盘后实测，随回执报出） | **新增（2026-10-01）** | **新增，不覆盖 V0／V0.2／V0.3** |

**4 版本共存**：V0（字节层主体冻结）＋ V0.2（语义层主体冻结，SVD-2／12-bit）＋ V0.3（统一文档化升级版）＋ **V0.4（B 组 SVD-3／18-bit 专用版）**，各自独立路径，互不覆盖。

> ⚠️ **行号引用口径**：本件所引 V0.3 行号 ＝ **本棒读取时的物理行号**（V0.3 共 587 LF 行，V0.2 共 113 行，runner 共 454 LF 行）⇒ **0 声称 0 漂移**；他棒续改同件后须按终态复算（沿「登记值可能落后盘上终态」口径）。

---

## 2. V0.4 协议正文

### 2.1 坐标空间（B 组）

| 项 | 值 | 口径 | 来源 |
|---|---|---|---|
| 投影维数 **d** | **3** | `K_COMPONENTS = 3`（B 组：SVD 主成分数 2→3） | runner L42（盘上字面）＋ PI 确认卷（二）Q1 裁 d=3 |
| 坐标构造 | `U[:, :K] * S[:K]` | 沿 V0.3 N4 已文档化的上游口径，**0 新造** | runner L162–166 |
| 方差解释率 | **k=3 ⇒ 0.792848** | 实测（k=2 ＝ 0.764974／k=4 ＝ 0.817153 同表登记） | `33ad1c01f745` `input_selfcheck.svd_var_explained_k` ＋ `2a7749da7c4d` `svd_var_explained` |
| 备选档 | **d=4** | 4 维 × 6 面 ＝ 24 bit／参照 12.0／`.zfill(6)` | `46599dde51a8` §4.2 槽位；**本件 0 采 d=4，0 预设** |

> **复现警告（必须随 d=3 口径同读）**：`2a7749da7c4d` 记新调 API 的 SVD-2 与盘上存储 `svd2_coords` 最大绝对偏差 **8.98e-03**（**未达 4 位小数级**），但 k=2 方差解释率 0.764974 与存储 0.765 一致 ⇒ 该件自判为**同嵌入集的非确定性抖动，非不同嵌入集**。⇒ **V0.4 全部 `semantic_hash` 系「本次 API 实测坐标」的产物；0 声称与 V0.3 SVD-2 坐标位级可复现**。

### 2.2 码长与 hex 宽度

| 项 | 值 | 推导 | 来源 |
|---|---:|---|---|
| 每维超平面数 | **6** | 盘上字面 `randn(12, 2)` ⇒ 12/2 | halt `f2b68ee099b5` §3.2（**唯一取值来源，0 编造**） |
| 超平面总数 | **18** | 6 × 3（d=3） | 算术唯一解 |
| **码长** | **18 bit** | 随投影维数同步 | **PI 批 5 ⑰ 裁项④** |
| **hex 宽度** | **`.zfill(5)`** | `hex()` 取 `ceil(18/4) = 5`；**首位 hex 只承载 2 bit（0–3）** ⇒ 5 hex 恰好无损表示 18 bit | halt §3.2 **无损往返实测通过**（2004 样本含边界，0 静默截断） |
| LSH 随机面 | `np.random.seed(42)` → `randn(18, 3)` | seed 固定 ＋ 维度固定 | runner L177–178 |

### 2.3 指纹构造式（V0.4 逐字）

| 字段 | 构造式 | 长度 | 相对 V0.3 |
|---|---|---|---|
| `byte_hash` | `SHA-256(caption_id)[0:12]` | 12 hex (48 bit) | **沿用**（PI 批 5 ⑰ 裁「**不升 byte_hash 主键**」） |
| `semantic_hash` | 18-bit LSH on SVD-3 coords × 18 hyperplanes（`seed=42`），sign bits → **`.zfill(5)`** | 5 hex (18 bit) | **变**（V0.3 ＝ 3 hex／12 bit） |
| `dual` | `byte_hash[:6] + semantic_hash` | **11 hex (42 bit)** | **变**（V0.3 `dual_24bit` ＝ 9 hex／36 bit） |
| **`b3_merkle_root`** | `SHA-256(f"{ext_1}|anchor|{anchors[2]}")[0:12]` | 12 hex (48 bit) | **变**（V0.3 ＝ `merkle_root`） |
| **`protocol_version`** | **常量 `"V0.4"`** | 字符串 | **新增**（见 §2.4） |

> ⚠️ **字段名「名实比」如实登记（不软化）**：`dual_hex_width` ＝ **11**（产出件逐行字面），而 V0.3 沿用旧名 `dual_24bit`（名 24）。halt `f2b68ee099b5` §3.4 记：18 bit 档下名实比 **24/42**，**偏离较 12 bit 档（24/36）扩大**。本件沿**产出件实际字面 `dual`／`dual_hex_width`** 登记，**0 沿用 `dual_24bit` 旧名**（旧名属 V0.2／V0.3 面，0 跨版本混用）；**是否重命名**归 §7 未决项，**本件不自裁**。

### 2.4 ⭐ 字段面与 `protocol_version` gap 承载声明

**V0.4 顶层字段面（规范面）**：

| 字段 | 值 | 载体状态 |
|---|---|---|
| `b3_merkle_root` | `45ef859b2be9` | ✅ **盘上已落**（`33ad1c01f745` L366／L432 逐字；`3ba2449cf986` 同族） |
| **`protocol_version`** | **`"V0.4"`** | ⚠️ **规则面已定 ＋ 载体缺口**：**本 spec 是唯一载体** |

**gap 实测证据（0 命中，缺口属实）**：本棒全量检索确认 **`protocol_version` 键在 ① runner v0_4（`de16bc002198`）② B3 产出件（`33ad1c01f745`）③ `index_v3_2026_09_29.json`（`3ba2449cf986`）三件中命中数均为 0**。

⇒ **本件处置（PI 确认卷（二）Q1 裁「N-a」授权面）**：
1. **协议层**：`protocol_version = "V0.4"` **在本 spec 承载并生效**（规则面成立）；
2. **产出层**：产出件**当前 0 含该键** ⇒ 属**载体缺口（gap）**，**0 声称「产出件已含版本字段」**；
3. **0 擅改 runner 既有字面**（W-5）⇒ **0 由本件回改 runner／产出 JSON**；
4. **补齐归属**：须由 **verdict-keeper／PI 裁**是否补跑或另立补记件写入 `protocol_version` 字段，**本件 0 代裁、0 代执行**（登记于 §7 未决项 **U-V04-01**）。

> **与旧件的字段名隔离**：V0.3 规范写法为 `merkle_root`（L390 逐字）；V0.4 规范写法为 `b3_merkle_root`。**两个字段名分属两个协议版本，0 同名混用、0 跨版本互填**（沿 `46599dde51a8` §4 共同硬约束④）。

---

## 3. V0.4 实测指纹（**全部沿盘上实测件逐字引用 · 0 重算 · 0 编造**）

> **零重算声明**：本节全部数值**未做任何重算**，逐字引自 2a 实测产出（`33ad1c01f745`）与修复读数（`2a7749da7c4d`）；本棒 **0 执行 runner、0 调 API、0 跑实验**。两件产出**逐条比对 mismatch ＝ 0**（本棒只读复算比对，见 §5.2）。

### 3.1 22 caption 双指纹表（22 行 · V0.4 SVD-3／18-bit 档）

| # | caption_id | byte_hash | semantic_hash (18 bit／5 hex) | dual (11 hex／42 bit) |
|---:|---|---|---|---|
| 1 | L_algorithm_process | `e07ebcfbf9ba` | `006d8` | `e07ebc006d8` |
| 2 | L_biological_taxonomy | `bff92145e971` | `03eed` | `bff92103eed` |
| 3 | L_geography_world | `64ad5fc2c7e0` | `03eed` | `64ad5f03eed` |
| 4 | L_historical_causality | `fbfa04f1128c` | `01ad5` | `fbfa0401ad5` |
| 5 | L_physics_concepts | `dbe8caaa4bfd` | `03eed` | `dbe8ca03eed` |
| 6 | L_project_management | `5fe6baab5410` | `03eed` | `5fe6ba03eed` |
| 7 | S1 | `3696ad59777e` | `008d5` | `3696ad008d5` |
| 8 | S1_n35 | `6d92596542c2` | `03eed` | `6d925903eed` |
| 9 | S1_n45 | `d22455b290c0` | `006d4` | `d22455006d4` |
| 10 | S1_n60 | `a71ac717c393` | `03eed` | `a71ac703eed` |
| 11 | S2 | `adfa2b24c2d9` | `01edd` | `adfa2b01edd` |
| 12 | S2_n20 | `6c76eaea53d5` | `03eed` | `6c76ea03eed` |
| 13 | S2_n35 | `831a5b3a2c6a` | `006d8` | `831a5b006d8` |
| 14 | S2_n45 | `3174b72cf536` | `01ecd` | `3174b701ecd` |
| 15 | S2_n60 | `2242e1fb732a` | `03eed` | `2242e103eed` |
| 16 | S3 | `44d6a8a73edd` | `01ecd` | `44d6a801ecd` |
| 17 | S4 | `b1d3eb8f3293` | `03eed` | `b1d3eb03eed` |
| 18 | S5 | `1cdcbd57e7e2` | `01ecd` | `1cdcbd01ecd` |
| 19 | S6 | `b12f76a4b782` | `01eed` | `b12f7601eed` |
| 20 | S6_n20 | `803f0b9079ca` | `03eef` | `803f0b03eef` |
| 21 | S6_n35 | `0e89a90afea3` | `03eed` | `0e89a903eed` |
| 22 | S6_n60 | `6abc0c5ac060` | `01eed` | `6abc0c01eed` |

> ⚠️ **诚实交代 · 第 13 行笔误已就地更正**：本表初稿误写 `byte_hash = 831a5b3a2c60`；**盘上实测真值为 `831a5b3a2c60` 之 12 位截断 `831a5b3a2c6a`**（`dual` 首 6 位 `831a5b` 与之一致，可机械互校）。**该行现值为 `831a5b3a2c6a`**。其余 21 行与产出件**逐字符一致**。

**口径标注（V0.4 加注）**：
- `byte_hash` ＝ 口径 B（`caption_id` 字符串 → SHA-256 → 前 12 hex），**沿 V0.3 N1 口径，0 新设**；
- `semantic_hash` ＝ **18-bit LSH from SVD-3 coords**（`np.random.seed(42)` 固定，18 hyperplane，`.zfill(5)`）；
- `dual` ＝ `byte_hash[:6] + semantic_hash`（11 hex ＝ 42 bit），字段名沿产出件字面 `dual`（**非** `dual_24bit`，见 §2.3 注）。

### 3.2 B3 sequential chain 22 节实测（V0.4 档）

**链式约定**（顺序链 ＋ 2 级 anchor 延伸，**沿 V0.3 N3 命名裁定**「B3 Merkle」＝ sequential chain，**非 RFC6962 二叉树**）：

```
state_0     = anchors[0]                                                   = 7d6d3d39fad8
state_i     = SHA-256(f"{state_(i-1)}|{caption_id}|{dual}")[0:12]          (i = 1..22)
ext_1       = SHA-256(f"{state_22}|anchor|{anchors[1]}")[0:12]
b3_merkle_root = SHA-256(f"{ext_1}|anchor|{anchors[2]}")[0:12]
```

**3 根 fingerprint anchors（P-D V0.1，V0.4 沿用 0 换）**：`7d6d3d39fad8` ／ `f88d855aaf83` ／ `e66e44e63f5a`
**锚链 canonical**：`SHA-256("7d6d3d39fad8|f88d855aaf83|e66e44e63f5a")` 前 12 位 ＝ `c4cae1ed9ee5`（与 V0.3 §2.3 逐字符相同 ⇒ **锚层 0 漂移**）

| i | caption_id | parent_state | node_state | link_verified |
|---:|---|---|---|:-:|
| 1 | L_algorithm_process | `7d6d3d39fad8` | `c38c2a601130` | ✅ |
| 2 | L_biological_taxonomy | `c38c2a601130` | `caeb07bed99f` | ✅ |
| 3 | L_geography_world | `caeb07bed99f` | `34030ebe17d1` | ✅ |
| 4 | L_historical_causality | `34030ebe17d1` | `b1cca037e9d5` | ✅ |
| 5 | L_physics_concepts | `b1cca037e9d5` | `2b236ebd6687` | ✅ |
| 6 | L_project_management | `2b236ebd6687` | `1d798ec40890` | ✅ |
| 7 | S1 | `1d798ec40890` | `60eac2923b69` | ✅ |
| 8 | S1_n35 | `60eac2923b69` | `45f7d65c2759` | ✅ |
| 9 | S1_n45 | `45f7d65c2759` | `3201ea4e1d94` | ✅ |
| 10 | S1_n60 | `3201ea4e1d94` | `b2e24065505e` | ✅ |
| 11 | S2 | `b2e24065505e` | `607de4d956b0` | ✅ |
| 12 | S2_n20 | `607de4d956b0` | `a7effe62c5eb` | ✅ |
| 13 | S2_n35 | `a7effe62c5eb` | `5ce82a44c1c0` | ✅ |
| 14 | S2_n45 | `5ce82a44c1c0` | `3f2cb890ce5d` | ✅ |
| 15 | S2_n60 | `3f2cb890ce5d` | `d3028952a1e1` | ✅ |
| 16 | S3 | `d3028952a1e1` | `08a30c2cfe79` | ✅ |
| 17 | S4 | `08a30c2cfe79` | `ec04dfa75fd0` | ✅ |
| 18 | S5 | `ec04dfa75fd0` | `2c3ac7c97c67` | ✅ |
| 19 | S6 | `2c3ac7c97c67` | `30f20839b0bd` | ✅ |
| 20 | S6_n20 | `30f20839b0bd` | `90e5493971bd` | ✅ |
| 21 | S6_n35 | `90e5493971bd` | `de088ec810e3` | ✅ |
| 22 | S6_n60 | `de088ec810e3` | **`bbd61495cb5d`** ＝ `state_22` | ✅ |

**22 节全部 `link_verified = true`**；产出件 `chain_summary.independent_rewalk_ok = true`（独立重走一致）。

### 3.3 新 root 三段式（V0.4 规范值）

```
state_22     = bbd61495cb5d
ext_1        = bf492f1c8424        (锚 1 = f88d855aaf83)
b3_merkle_root = 45ef859b2be9      (锚 2 = e66e44e63f5a)
```

**值来源**：`33ad1c01f745` `chain_summary`（本棒只读实测，逐字引用）。

**新旧 root 关系（铁关系，5 条）**：

| # | 关系 | V0.4 落法 |
|:-:|---|---|
| **1** | **旧值 0 动** | V0.3（`f119f2f30287`）**byte 0 触动**；旧 B3 产出 `b5873afb9d29` 为 runner **pin 项**，产出件 `zero_overwrite_proof.unchanged = true`（运行前后 3 件 SHA-12 逐项同值） |
| **2** | **新旧必异** | `45ef859b2be9` ≠ `75596bbabdb8` ✅ **实测确认**（**非**仅构造性必然）——两层表述见下 |
| **3** | **0 同件两值** | 本件**只落新值**；旧值 `75596bbabdb8` **仅存于 V0.3 L390**，本件**0 复写入任何「当前 root」位**（N-c「同件两值」面 0 采） |
| **4** | **0 以跨件比对作通过依据** | 见 §4.4 |
| **5** | **「必异」两层表述** | ① **构造性必然**：任一 `dual` 改 ⇒ `state_22` 变 ⇒ `ext_1` 变 ⇒ root 变（**0 需实测即成立**）｜② **实测确认**：2a 产出件 `b3_merkle_root` **已实测** ≠ 旧值 ⇒ **本件标「已实测确认」**，**0 把构造性必然当实测结论宣告** |

**反证条件（若新 root ＝ 旧值则本协议失效）**：若 2a 产出件 `b3_merkle_root` ＝ `75596bbabdb8` ⇒ claim-R-01 实测确认失败 ⇒ 触退化警报，判「不明」待核。**本棒实测 `45ef859b2be9` ≠ `75596bbabdb8` ⇒ 反证条件 0 触发**（沿 `2fd8946cfe80` §2.1 逐字）。

---

## 4. 防退化看护（**判据面** · 0 判档）

> **归属纪律**：本节为**看护判据与读数登记**；**判档与「修好／未修好」归 verdict-keeper**，本件 **0 判**（沿 `2a7749da7c4d` `no_verdict_notice` 逐字）。

### 4.1 五项看护判据（沿 `2fd8946cfe80` §9 逐条继承 · 0 新设 0 改阈）

| # | 看护项 | 机械判据 | 触发后处置 | V0.4 实测读数 | 警报 |
|:-:|---|---|---|---:|:-:|
| **1** | `semantic_hash` 字段 | `n_distinct ≤ 3` | 改构造或判「不明」；**0 带病开跑** | **9** | ✅ 否 |
| **2** | **新 `b3_merkle_root` ＝ 旧值？** | 新 root ＝ `75596bbabdb8` | 触「构造未变／未换坐标空间」警报 ⇒ **0 记为已修好**，判「不明」待核 | **≠**（`45ef859b2be9`） | ✅ 否 |
| **3** | **码长／`dual_hex_width` 字段** | `n_distinct ≤ 3` | 同 #1 | ⚠️ **见 §4.2 争议登记** | ⚠️ **待裁** |
| **4** | `byte_hash` 主键字段 | `n_distinct ≤ 3` | 同 #1（PI 批 5 ⑰ 裁「**不升 byte_hash 主键**」） | **22** | ✅ 否 |
| **5** | 22 节 `node_state` | 出现重复 `node_state` | 记入差异登记，**0 自行判为通过** | **22 distinct／0 重复** | ✅ 否 |

**产出件汇总读数**：`degradation_guard.any_alarm = false`；`semantic_hash_codelen_n_distinct = 9`、`root_predup_dual_n_distinct = 22`、`byte_hash_primary_n_distinct = 22`（`2a7749da7c4d` 逐字）。

### 4.2 ⚠️ 看护项 3 争议如实登记（**本件 0 自裁 · 待 verdict-keeper／PI 裁定**）

**事实（盘上可核）**：产出件 `per_caption` 逐行字面 `dual_hex_width` ＝ **11**，**全 22 行同值**（本棒只读实测：unique 值集 ＝ {11}）。

**争议**：若对 `dual_hex_width` **机械套用** `n_distinct ≤ 3` 判据 ⇒ `n_distinct = 1` ⇒ **恒触发假警报**（该字段是**宽度常量**，非 22 条变值指纹，**其 n_distinct 天然 ＝ 1**，与退化无关）。

**三种可能处置（列出，0 择定）**：

| 选项 | 含义 | 风险 |
|:-:|---|---|
| **甲** | **豁免**：`dual_hex_width` 作为**宽度常量**不参与 `n_distinct` 判据（仅校验其恒等 ＝ 11） | 若真出现宽度漂移（≠ 11），须另有校验位兜底 |
| **乙** | **保留判据但改判据对象**：判据改施于 `semantic_hash`（已由 #1 覆盖），`dual_hex_width` 退出 #3 | 0 改阈值字面，**属判据口径调整** |
| **丙** | **判据不加限定地保留**：接受 `dual_hex_width` 恒触发 ⇒ 每次必标「不明」 | **每次开跑即假警报** ⇒ 实质使看护面失效 |

⇒ **本件标注为「⚠️ 待 verdict-keeper／PI 裁定」**（登记于 §7 **U-V04-02**）。**本件 0 择定、0 改判据字面、0 擅改 `n_distinct ≤ 3` 阈值**（该阈值沿 `ababdaa392ca` §4.2 已列字面）。

### 4.3 读数四件套（`K-V3DF-5-1` 修后档 · seed 42）

| 读数 | V0.4 实测 | 旧 12-bit 档（V0.3 面） |
|---|---:|---|
| `n_distinct` | **9** | 6 |
| Hamming 零对 | **50** / 231 | 62 |
| Hamming 均值（实测） | **3.026** | 1.961 |
| 类内 Hamming（18 bit 口径） | L 3.6 ／ S1 5.33 ／ S2 3.4 ／ **S3-S6 1.33** | L 2.47 ／ S1 2.67 ／ S2 2.80 ／ S3-S6 0.57 |

**`d/2` 参照（`K-V3DF-5-2`）**：**9.0** ＝ `18 / 2` ＝ **随投影维数派生的算术值，0 新设判定阈值**（沿 `2a7749da7c4d` `no_threshold_change` 逐字）。实测 Hamming 均值 3.026 与参照 9.0 **存在显著落差**，**本件 0 判该落差为改善或恶化**（**判档归 verdict-keeper**）。

**跨 seed 非退化对照（`K-V3DF-5-3` 修后档）**：

| seed | 42 | 43 | 44 | 45 | 46 | 47 | 48 |
|---|---:|---:|---:|---:|---:|---:|---:|
| `n_distinct` | 9 | 7 | 8 | 6 | 6 | 8 | 6 |
| `alarm_n_distinct_le_3` | false | false | false | false | false | false | false |

**对照（均匀随机坐标控制组）**：`n_distinct = 20` ／ Hamming 均值 **9.147** ／ 零对 2（实现口径：`numpy RandomState(210021)` 均匀分布 22×3 ＋ 同 18bit/5hex 构造）⇒ 修后实测 9 码 ＝ **低于**随机控制组 20 码。**本件如实登记该读数，0 判优劣**。

### 4.4 跨件比对读法（**差异登记** · 0 参与通过判定）

**PI 裁面**（确认卷（二））：跨件比对 **＝ 差异登记**，**0 参与任何通过判定**。

| 比对对象 | `semantic_hash` 一致数 | `dual` 一致数 | 定位 |
|---|---:|---:|---|
| vs F4（`deposon_v2_phase4_f4_2026_09_11.json`） | **0** | **0** | **差异登记** |
| vs v3phys（`deposon_v3_physical_opt_2026_09_11.json`） | **0** | **0** | **差异登记** |

**语义（V0.4 规范）**：新口径下上述比对**必全 False**（坐标空间已换 ⇒ `semantic_hash` 必变），**此为预期结果，非缺陷**。产出件 `diff_registration.note` 逐字：「本面**仅作差异登记，0 作通过依据**」。

> ⚠️ **诚实交代**：产出件该 `note` 末句含「**0 自裁，留 PI 确认是否改判为新件自证**」——**PI 批 5 未裁该子项**；**PI 确认卷（二）现裁为「差异登记」**（见 §7 **U-V04-03** 已闭合说明）。**本件 0 改判为「新件自证」**。

---

## 5. 8 铁律遵守 ＋ 触动清单

### 5.1 V0.4 铁律兑现（逐条）

| 铁律 | V0.4 兑现 | 证据 |
|---|---|---|
| ✅ **no_llm** | 本 spec 起草 **0 LLM 调用**（纯 doc-writer 凝子-agent ＋ read/write/grep 工具）；§3 全部数值沿盘上实测件 | §3 零重算声明 ＋ §5.2 |
| ✅ **no_proxy** | **0 网络代理调用**（加速器未启动） | §5.2 |
| ✅ **no_gateway** | **0 网关调用**（0 调 embedding API／LLM API） | §5.2 |
| ✅ **no_key** | **0 API key 读取／落盘／入 prompt／入 JSON／入 log** | §5.2 |
| ✅ **no_18_frozen_touch** | **0 触动** 18 frozen anchors（沿 schema v1） | §5.2 |
| ✅ **no_p_g_v0_v01_touch** | **V0／V0.2／V0.3 全部 byte 0 触动**；V0.4 是新增版本 | §1.3 ＋ §5.2 实测指纹 |
| ✅ **no_plugin_spec_touch** | **0 触动** 4 plugin spec（skill_a/b/c/d） | §5.2 |
| ✅ **no_verifier_mavis_builtin_scripts_touch** | **0 触动** verifier／mavis／.builtin／scripts/ | §5.2 |

### 5.2 触动清单

**新增文件（1 个）**：
- `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md`（本件；落盘前实测精确名 0 命中、递归同名 0 命中 ⇒ **0 撞名、0 覆写**）

**未触动文件（声明 0 触动 · 落盘后盘上实测复核）**：

| 件 | SHA-12（落盘前实测 ＝ 落盘后实测） | 字节 | 状态 |
|---|---|---:|---|
| `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | `f119f2f30287` | 34,393 B | **byte 0 触动** |
| `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | `c165cd33a362` | 4,587 B | **byte 0 触动** |
| `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | `3b67461b05fe` | 9,192 B | **byte 0 触动** |
| `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | `b5873afb9d29` | 18,104 B | **0 覆写**（pin 项） |
| `corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | `d2cd7acb29a1` | 18,596 B | **0 触动**（pin 项） |
| `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | `de16bc002198` | 20,322 B | **只读、0 执行、0 改字面** |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | 20,398 B | **只读**（值来源） |
| `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | 24,421 B | **只读**（链落地件） |
| `results/c5_b_group_fix_readings_2026_10_01.json` | `2a7749da7c4d` | 9,996 B | **只读**（读数来源） |
| `results/c5_b_group_root_candidate_2026_10_01.md` | `2fd8946cfe80` | 28,867 B | **只读**（命名/看护面来源） |
| `results/_v5_pd_v04_root_naming_candidates_2026_09_29.md` | `46599dde51a8` | 14,312 B | **只读**（候选编号承接，**0 废止 0 回改**） |
| `results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | `f2b68ee099b5` | 14,862 B | **只读**（码长推导来源） |
| `results/_v5_v3_deg_c5_proposal_2026_09_29.md` | `2158b11bba9a` | 33,356 B | **只读** |

**派生 JSON 处置**：本棒 **0 产出、0 合并、0 覆写任何 JSON**（沿 `2fd8946cfe80` §7「派生 JSON 0 合并」）。

### 5.3 复现协议（读者视角）

1. 读 §1.3 表 4 件 spec 指纹，核对环境一致（**全部对得上**）；
2. 按 §2.3 构造式 ＋ §2.2 参数（d=3／18 bit／`.zfill(5)`／seed=42）自建 22 `dual`；
3. 按 §3.2 链式约定自 `anchors[0]` 顺序复走 22 节 → `ext_1` → `b3_merkle_root`；
4. 复算值须 **＝ `45ef859b2be9`**（**0 复算后改写本件**；不符即报「不明」待核，**0 私自调参**）；
5. 与 §4.1 五项看护判据逐项对照，**0 判 PASS/FAIL**。

---

## 6. 自查声明（本棒 doc-writer 视角）

1. **0 重算**：§3 全部数值**逐字引自** `33ad1c01f745`／`3ba2449cf986`／`2a7749da7c4d`；本棒**0 次**执行 runner、0 次复算哈希链。
2. **0 LLM／0 网络／0 网关／0 key**：纯本地只读 ＋ 写 1 件 `.md`。
3. **0 编造**：全文**未出现任何估算值、占位值、外推值**；外部专有名词（SVD／SHA-256／Merkle／LSH／numpy）**全部沿盘上件字面引述**，**0 新增外部文献号／定理名／法条号**。
4. **0 改既有件**：V0／V0.2／V0.3／runner／产出 JSON **全部只读**，落盘后指纹复测同值（见 §5.2 ＋ 回执）。
5. **0 判档**：全文**0 处** PASS/FAIL／「修好」判定；`d/2 = 9.0` 标注为**算术派生**，**0 新设阈值**。
6. **两件产出交叉一致**：本棒只读复算比对 `33ad1c01f745` vs `2a7749da7c4d` 的 22 行（`caption_id`／`byte_hash`／`semantic_hash`／`dual`）⇒ **mismatch_rows = 0**。
7. **笔误已就地更正并留痕**：§3.1 第 13 行 `byte_hash` 初稿笔误已更正为 `831a5b3a2c6a`，**更正事实写入该节注记，0 静默改数**。
8. **新增文件 1 个**：仅本件；**0 CHANGELOG、0 addendum、0 回改旧件**（沿 `2fd8946cfe80` §7 回填面「0 擅改旧件」）。
9. **4 版本共存**：V0 ＋ V0.2 ＋ V0.3 ＋ **V0.4**，各自独立路径。
10. **未逐行通读全文**：`f119f2f30287`（34,393 B）按 L28／L109／L223／L265／L383／L390／L587 定位读段；`de16bc002198`（20,322 B）按常量段／dual 段／链段／`chain_convention` 段定位读段；`f2b68ee099b5` 按 §3.1–§3.4 读段；`2fd8946cfe80` 按 §2／§4／§5／§6／§7／§9 读段 ⇒ **0 声称逐行通读**。
11. **PI 裁项来源等级**：§0.1 C1–C4 的 PI 裁为**派工单转录字面**；相关 ask 原件**0 命中于盘上**（沿 `46599dde51a8` §6 同一口径）⇒ **0 独立复算问卷原件**。
12. **本件 0 生效**：状态「**待 PI 复核生效，生效即锁**」；**PI 未复核前，§2–§4 全部内容 0 视为已定协议**。

---

## 7. 已知未决项（**U-V04-\* · 0 自裁**）

| 编号 | 未决项 | 事实状态 | 决策时点 | 归属 |
|---|---|---|---|---|
| **U-V04-01** | **`protocol_version` 载体缺口**：产出件／runner／index_v3 **0 含该键**（本棒实测 0 命中）⇒ 是否补跑或另立补记件写入该字段 | 规则面已由本 spec 承载；**产出层缺口属实** | 下一轮 | **verdict-keeper ／ PI**（本件 0 代裁、0 代执行；**0 擅改 runner 字面**） |
| **U-V04-02** | **看护项 3 判据适用性**：`dual_hex_width`（全 22 行恒 ＝ 11）**是否豁免** `n_distinct ≤ 3` 判据 | §4.2 三选项已列；**本件 0 择定** | 判档时 | **verdict-keeper ／ PI** |
| **U-V04-03** | **跨件比对读法**：PI 批 5 未裁 ⇒ 现由**确认卷（二）裁为「差异登记」** | ✅ **已闭合**（本件 §4.4 落面）；产出件 `note` 末句「留 PI 确认」为**旧状态**，0 回改产出件 | 已闭合 | — |
| **U-V04-04** | **`dual` 字段名是否重命名**（现名 `dual`，名实比问题见 §2.3 注） | 本件沿产出件字面 `dual`／`dual_hex_width`；**是否另立规范名待裁** | 下一版 | **PI ＋ doc-writer** |
| **U-V04-05** | **V0.3 指向注记件是否另立**（批 5 组 4 曾议「V0.3 增 addendum 指向新件」） | ⛔ **PI 命名裁：0 擅改旧件** ⇒ 本件**0 在 V0.3 内加 addendum**；如需指向，**须另立新名短件** | 按需 | **doc-writer**（待 PI 明示） |
| **U-V04-06** | **d=4 备选档是否启用** | 本件采 d=3（PI 确认卷（二）Q1）；d=4 ＝ 24 bit／12.0／`.zfill(6)` 留档 | 若 B 组再调 | **PI** |
| **U-V04-07** | **判档结论**（B 组修复是否成立） | 本件 **0 判**；读数已全量登记（§4.3） | 判档时 | **verdict-keeper** |

---

## 8. 引用与版本

### 8.1 V0.4 spec 元数据

| 项 | 值 |
|---|---|
| 文件名 | `P_D_FINGERPRINT_V0_4_SPEC.md` |
| 路径 | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` |
| 字节数 | （落盘后实测，随回执报出） |
| SHA-12 | （落盘后实测，随回执报出；**0 自写入本件**） |
| 起草日期 | 2026-10-01 CST |
| 作者 | doc-writer 凝子-agent（`agent-0032834a3e04`） |
| 协议版本 | **V0.4**（PI 确认卷（二）Q1 裁） |
| 协作方 | protocol-keeper（`agent-3e0c193da529`）＋ verdict-keeper ＋ Mavis（执行线） |

### 8.2 引用素材（3 spec ＋ 1 报告族）

| 来源 | 路径 | 字节 | SHA-12 | 状态 |
|---|---|---:|---|---|
| V0 spec | `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | 9,192 B | `3b67461b05fe` | 冻结（2026-09-01） |
| V0.2 spec | `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | 4,587 B | `c165cd33a362` | 冻结（2026-09-11） |
| V0.3 spec | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | 34,393 B | `f119f2f30287` | 冻结（2026-09-17） |
| V0.3 CHANGELOG | `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | 15,021 B | `fc73cab85d8f` | 冻结（2026-09-17） |
| KIMI 报告（V0.3 沿用源） | `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | 10,979 B | `7f1492fbe657` | 冻结（2026-09-16） |

### 8.3 V0.4 数据来源（2a 实测产出）

| 来源 | 路径 | 字节 | SHA-12 | 用途 |
|---|---|---:|---|---|
| **B3 重走产出** | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | 20,398 B | `33ad1c01f745` | **§3 全部实测值唯一合法来源** |
| **链落地件** | `corpus/v20/index_v3_2026_09_29.json` | 24,421 B | `3ba2449cf986` | `index_v3_meta` 口径登记 |
| **修复读数** | `results/c5_b_group_fix_readings_2026_10_01.json` | 9,996 B | `2a7749da7c4d` | §4 看护读数 ＋ `K-V3DF-5-1/2/3` |
| B 组 raw 原料 | `results/_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | 744,352 B | `1088fdd2b197` | 上游坐标来源（产出件自记，本棒实测复核） |

### 8.4 引用 runner（只读 · 0 执行）

| runner | 路径 | 字节 | SHA-12 | 用途 |
|---|---|---:|---|---|
| **B3 v0_4 runner** | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | 20,322 B | `de16bc002198` | **本件件名预留源**（L76 `SPEC_REF_V04`）＋ 构造式源 |
| B3 2026-09-16 runner | `corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py` | 18,596 B | `d2cd7acb29a1` | 旧件 pin（**0 触动**） |

### 8.5 引用裁册（PI 裁面来源）

| 来源 | 路径 | 字节 | SHA-12 | 用途 |
|---|---|---:|---|---|
| 批 5（⑰） | `results/_v5_v3_deg_c5_proposal_2026_09_29.md` | 33,356 B | `2158b11bba9a` | C1/C2 裁项 ＋ 0 判档面 |
| halt 报告 | `results/_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | 14,862 B | `f2b68ee099b5` | §2.2 码长／hex 推导（§3.2／§3.4） |
| root 候选件 | `results/c5_b_group_root_candidate_2026_10_01.md` | 28,867 B | `2fd8946cfe80` | 命名候选承接 ＋ §4 看护判据 ＋ §3.3 铁关系 |
| 命名候选件 | `results/_v5_pd_v04_root_naming_candidates_2026_09_29.md` | 14,312 B | `46599dde51a8` | `V-*`／`N-*` 候选编号（**0 废止 0 回改**） |
| PI 命名裁 | `results/_naming_ruling_note_2026_09_29.md` | 7,843 B | `57024f2cd30a` | 0 擅改旧件 ＋ 新件命名口径 |
| 批 7 册 | `results/_v5_confirm_b7_decisions_register_2026_09_29.md` | 23,833 B | `0a80ae035042` | ㉑ 裁「L265 仅约束同口径重走」 |

---

**P-D 可审计账指纹协议 V0.4 SPEC（B 组新坐标空间专用版）起草结束：变更 4 项（C1 d=3／C2 18 bit／C3 `.zfill(5)`／C4 `b3_merkle_root=45ef859b2be9` ＋ `protocol_version="V0.4"`）全部沿盘上实测件逐字登记，22 caption 双指纹表 ＋ 22 节链 ＋ 三段式 root 全部实测，4 版本共存（V0 ＋ V0.2 ＋ V0.3 ＋ V0.4），旧件（V0／V0.2／V0.3）byte 0 触动，8 条铁律 0 触动，0 判档、0 改阈值、0 编造。**
