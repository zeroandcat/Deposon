# `U-V04-01-新`／`U-V04-02` 配套校验位 · 落面登记件 · worker · 2026-10-09

> **一句话**：本件依 PI 2026-10-09 两裁（卡 `ask_ced8de9fd514ccc30f4e16e2` 第 3 题 ＋ 卡 `ask_69d695f301f12d158e102652` 第 3 题），**以实体字面 `c4e3338619c6` §3.1–§3.3 逐字执行**，为「豁免成立所必需之配套校验位」**逐字段落面**；落面数据由本包新件 `_u04_1_exemption_precondition_verification_2026_10_09.json`（`bddfeac3ee2f`）承载。**⛔ 0 回改任何既有件、⛔ 0 代裁豁免范围本身、⛔ 0 新设阈值、⛔ 0 网络、⛔ 0 读 R4 key。**

## §0 输入件 · 本人盘上终态实测 SHA-256／SHA-12／bytes（**0 复用自报值**）

| # | 路径 | SHA-12 | bytes | 本件采信面 |
|:-:|---|---|---:|---|
| 1 | `results/_criterion_application_scope_prereg_2026_10_01.md` | **`c4e3338619c6`** | 50,322 | **§3.1 分层裁定／§3.2 双用途分离／§3.3 落面规格**（本包规格源） |
| 2 | `results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | **`e98bee353448`** | 37,003 | §3.1 A–G 族 22 项字段清单（落面范围源） |
| 3 | `results/_k_cf_4_effectivity_register_2026_10_09.md` | **`edc6a548e3ca`** | 35,872 | §B‑2／§B‑3 生效字面、§A‑2 G1–G6 对接 |
| 4 | `results/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md` | **`618280cb8cfd`** | 31,801 | §4.4‑M3 来源修正（G1／G2 ≙ §3.3 配套位）、§5 档 1 四要件 |
| 5 | `results/_k_v3df_0_1_four_readings_2026_10_09.md` ＋ `.json` | **`53c28ca1ae3d`**／**`e87937d55471`** | 46,522／65,507 | 22 项读数面（校验对象） |

**读数源三件（落面复算之事实源 · 本人独立复算 · 0 复用）**：`corpus/v20/index_v3_2026_09_29.json`（`3ba2449cf986`）／`results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json`（`33ad1c01f745`）／`results/c5_b_group_fix_readings_2026_10_01.json`（`2a7749da7c4d`）。

---

## §1 PI 裁登记（**照录 · 来源等级 L2 · 0 代裁**）

### §1‑1 `U-V04-01-新` 生效字面裁（卡 `ask_ced8de9fd514ccc30f4e16e2` 第 3 题）

> **U-V04-01-新 生效字面以实体字面为准**（`c4e3338619c6` §3.1）——「布尔位整类豁免（强制配套校验位：① 取值语义声明〔谁置位/何时置位/依据件〕；② 全 `true` 须附独立验证件；③ ⛔0 声称『豁免＝该位无缺陷』）＋ 标签位**仅豁免于构造退化用途**（强制配套：① 码本覆盖校验〔报『期望类别全集』与『实到类别』，判『实到 ⊊ 期望 ⇒ 素材面覆盖缺口』；② 报编码表出处；③ ⛔0 因豁免而放弃覆盖检查）＋ 常量/派生列⛔0整类豁免·二分＋保留面继续受门」，**「缺位即豁免不成立」**。

**本件对该裁之执行边界**：⛔ **0 取宽、0 取窄** —— 逐字执行实体字面 §3.1 五轨；⛔ 0 将「布尔位整类豁免」外推至非布尔对象；⛔ 0 将「标签位豁免」外推至「素材面覆盖」用途；⛔ 0 宣告任何字段已豁免（豁免成立与否须待缺口闭合，本件仅落面）。

### §1‑2 `U-V04-02` 条件核准裁（卡 `ask_69d695f301f12d158e102652` 第 3 题 · 17:18）

> **U-V04-02 ＝ 条件核准（须先补落该校验位）**。① `dual_hex_width`（表示法常量·族 B）之配套校验位纳入本包范围（沿 `c4e3338619c6` §3.2 用途③「定义／表示法一致性 → 恒等校验」＋§3.3 规格）；② 登记该条件裁（其**备案自该校验位落位时生效**——「缺位即豁免不成立」）；③ 若此项超出范围或无法落位 ⇒ 列入候呈，⛔ 0 硬改。

**条件状态（本人实测 · 如实登记）**：✅ **条件已满足** —— 该恒等校验位已于本包落位（§4 轨 ③，22/22 = 11、漂移行 0）。⚠ **但备案「生效时点」属 PI 面**：本件**0 宣告 `U-V04-02` 已结、0 代裁备案生效**（`edc6a548e3ca` §C‑3 载 PI 面边界原样保留）。

---

## §2 落面范围之界定（**0 自设边界**）

| 范围面 | 本包处置 | 依据 |
|---|---|---|
| **V3-04 面**（`e98bee353448` §3.1 A–G 族 22 项所指字段） | **逐字段落面** | 本包任务书 ＋ 派工锚 |
| **K-CF-4 档 1 适用面** | **以盘上为准**：档 1 之强制配套位（G1–G6）经 `618280cb8cfd` §4.4‑M3 判定 ≙ `c4e3338619c6` §3.3 ①②③ ⇒ **与本包同源同向，无二义**（`edc6a548e3ca` §B‑3 末）；**盘上尚无任何字段被判入档 1**（`edc6a548e3ca` §A‑4 ⛔「0 声称任何字段已落档」）⇒ 本包**0 代判档位**，仅落 §3.3 之配套位 | `edc6a548e3ca` §A‑2／§A‑4 |
| **保留面**（变值指纹列等） | **⛔ 0 落面、0 豁免**；仅登记「未落面且不应落面」 | `c4e3338619c6` §3.1 保留面 |
| **`E3` 面** | **⛔ 0 触及**（G6 配套位仅登记为义务，非设计） | `edc6a548e3ca` §C‑1／§C‑2 |

---

## §3 **逐字段落面表**（**字段名／类别／所需校验位／现状／落面产物**）

**「落面产物」列之 `D` 指本包数据件 `results/_u04_1_exemption_precondition_verification_2026_10_09.json`（`bddfeac3ee2f`）之对应节。**

### §3‑A **轨 ① 布尔位**（整类豁免 · 所需：① 取值语义声明 ＋ ② 全 `true` 独立验证件）

| 字段 | 类别 | 所需校验位 | 现状（本人实测） | 落面产物 |
|---|---|---|---|:-:|
| `B3.per_caption[].chain.link_verified` | 布尔位 | ①② | **22/22 `true`** ⇒ ②**触发**；① 未见于既有件 | ✅ **`D.bool_track`**：①三要素已声明（置位者＝B3 runner；时机＝逐节重算比对通过时；依据件＝`chain_convention` ＋ `index_v3` 独立源）；②**已落** —— 以 `index_v3`（与被验件 B3 **非同件**）重算全链：`node_state` 22/22、`parent_state` 22/22、`link_input` 22/22 吻合，`state_22`／`ext_1`／`b3_merkle_root` 三分量逐字复现 ⇒ **PASS，0 分歧** |
| `B3.per_caption[].chain.self_verified_only` | 布尔位 | ①② | **22/22 `true`** ⇒ ②**触发** | ✅ **`D.bool_track`**：同上（共用同一次非同源重算，22/22 吻合） |
| `B3.per_caption[].diff_registration_vs_f4.dual_identical` | 布尔位 | ①（②不触发） | **22/22 `false`** | ✅ **`D.bool_track`**：①已声明（置位者＝B3 runner 差异登记面；时机＝逐条比对后；依据件＝`diff_registration.note` ＋ 两参照件）⇒ 按**取值语义声明轨**落面（恒 `false` 之依据） |
| `B3.per_caption[].diff_registration_vs_f4.semantic_hash_identical` | 布尔位 | ①（②不触发） | **22/22 `false`** | ✅ 同上 |
| `B3.per_caption[].diff_registration_vs_v3phys.dual_identical` | 布尔位 | ①（②不触发） | **22/22 `false`** | ✅ 同上 |
| `B3.per_caption[].diff_registration_vs_v3phys.semantic_hash_identical` | 布尔位 | ①（②不触发） | **22/22 `false`** | ✅ 同上 |
| `B3.id_correspondence.positional_match` / `.raw_concept_ids_match` | 布尔位（标量登记位） | ①（②不触发） | 各为单值 `true`（`n=1` 标量） | ✅ **`D.bool_track`**：①已声明；⛔ 非 22 项警报面内字段 |

**③「⛔ 0 声称『豁免＝该位无缺陷』」之遵守登记**：本件**通篇未作该声称**；对 `link_verified` 之独立验证仅覆盖**哈希链接关系**（`node_state`／`parent_state`／`link_input`／root 三环），**⛔ 0 声称该位无缺陷、0 声称 semantic_hash 之 LSH 语义正确**（见 §5 `G-U04-2` 缺口）。

### §3‑B **轨 ② 标签位**（仅豁免于「构造退化」用途 · 所需：① 码本覆盖校验 ＋ ② 编码表出处）

| 字段 | 类别 | 所需校验位 | 现状（本人实测） | 落面产物 |
|---|---|---|---|:-:|
| `index_v3.captions[].family` | 标签位 | ①② | 实到 `{L,S}`，`L`=6／`S`=16，`n_distinct`=2 | ✅ **`D.label_track`**：①期望全集 `{L,S}`＋实到＋计数已报 ⇒ **实到 = 期望 ⇒ 无覆盖缺口（PASS）**；②编码表出处＝`corpus/v20/` 目录枚举（`L_*.json` 6 件 ＋ `S*.json` 16 件 ＝ 22 源文件）＋ 冻结引用 `index_v3.spec = "docs/SPEC_v2.0.md §1"` |
| `index_v3.graphs[].family` | 标签位 | ①② | 实到 `{L,S}`，`L`=6／`S`=16，`n_distinct`=2 | ✅ 同上（family 由 `graph_id` 前缀派生，同源枚举） |
| `index_v3.graphs[].source` | 标签位 | ①② | 实到 `{0,1}`，0=21／1=1（唯一 `source=1` ＝ `S5.json`），`n_distinct`=2 | ⚠ **部分**：①期望全集 `{0,1}`＋实到＋覆盖判定 **PASS**；②编码表出处**「未核得」** —— 盘上 0 有 `source` 编码表冻结件字面 ⇒ 见 §5 `G-U04-1` |

**③「⛔ 0 因豁免而放弃覆盖检查」之遵守登记**：三个标签位**全部实际执行**了覆盖检查（期望全集 vs 实到），**0 跳过**；且 `graphs[].source` 虽采标签位严轨（沿 `c4e3338619c6` §5.2 之分类判断，来源等级 B），其覆盖检查**照样执行**。

### §3‑C **轨 ③ 定义型常量**（⛔ 0 整类豁免 · 二分 · 所需：④ 恒等校验位 ＋ 定义决定出处）—— **`U-V04-02` 条件核准项**

| 字段 | 类别 | 所需校验位 | 现状（本人实测） | 落面产物 |
|---|---|---|---|:-:|
| `B3.per_caption[].dual_hex_width` | 常量（定义／表示法决定） | ④ | **22/22 = 11**，`n_distinct`=1 | ✅ **`D.const_track`**：④恒等校验位**已落** —— 逐行比对 22 行，**漂移行数 = 0** ⇒ 无「表示法漂移」警报；**0 记为通过、0 静默之要求已履行**（判定为逐行实测 ＋ 显式记录漂移计数） |
| ↳ 定义决定出处 | — | 出处 | — | ✅ `caliber.dual` 字面＝「`byte_hash[:6] + semantic_hash` = 11 hex (42 bit)」；`caliber.byte_hash`＝「SHA-256(caption_id)[0:12]」；`caliber.semantic_hash`＝「18-bit LSH on SVD-3 coords × 18 hyperplanes（seed=42），sign bits → 5 hex」；**规范件 `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md`（盘上存在）** C2/C3 表（18 bit ＝ 6 面/维 × 3；`.zfill(5)`，`ceil(18/4)=5`）＋ `dual` 行；**算术复核 6+5 = 11**；**跨源佐证**：`index_v3` 实测 `byte_hash` 长度集 = {12}、`semantic_hash` 长度集 = {5} |

**⚠ 二分准绳之登记（本件 0 自行归类）**：`dual_hex_width` 归「定义决定」轨之依据＝其取值由**表示法**（6 hex ＋ 5 hex）决定，**非行为决定**（沿 `c4e3338619c6` §3.1 二分准绳表）。⛔ **0 扩至 `rm_iter`／`bayes_iter` 型（行为决定，继续受门）、0 扩至码长类指纹**（沿 §3.5 锚定）。

### §3‑D **轨 ④ 辅助派生列**（⛔ 0 整类豁免 · 二分 · 所需：⑤ 分量四项读数 ＋ 非被测读数列依据）

| 派生列 | 所需校验位 | 现状（本人实测） | 落面产物 |
|---|---|---|:-:|
| `B3.chain_summary`（root 三环并作一列） | ⑤ | 3 分量皆 `n=1` 标量 | ✅ **`D.derived_track.groups[0]`**：三分量**各自**四项读数已报（⛔ **0 以合并列代替**）；**非被测读数列依据**已标注；**跨源验证**：三分量值已由 §3‑A 之非同源重算逐字复现 |
| `B3.input_selfcheck` | ⑤ | 3 分量（偏差 0.0089821568／`False`／0.792848） | ✅ `groups[1]`：各分量四项读数已报；⚠ **0 独立复算**（依赖 0 落盘之 raw embeddings）⇒ 转引源件，来源等级 A（如实登记为强度限度） |
| `B3.anchors.values`（3 hex 锚点列） | ⑤ | 3 分量皆标量 | ✅ `groups[2]`：各分量读数已报 ＋ 出处＝`docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md §2.3 B3 Merkle` |
| `R.cross_seed_control` | ⑤ | `n_distinct`=20／`hamming_mean`=9.147／`hamming_zero_count`=2 | ✅ `groups[3]`：三分量读数已报；⚠ **0 重跑** `RandomState(210021)` 构造 ⇒ 转引源件 |

**⑤ 之「非被测读数列」依据登记**：三环/锚点/自检各组**均已标注**该列非输出读数测量列之依据（输出读数列见 `R.readings`／`cross_seed_control`）。

### §3‑E **保留面**（继续受门）

| 面 | 本包处置 |
|---|---|
| 变值指纹列等（`dual`／`semantic_hash`／`byte_hash`／`coords_k`／`node_state`／`parent_state`／`link_input`／`caption_id` 等） | ⛔ **0 落面、0 豁免**。`D.retained_face` 仅登记抽样实测（`dual` 22／`semantic_hash` 9／`byte_hash` 22／`caption_id` 22／`coords_k[0..2]` 各 22／`node_state` 22／`parent_state` 22／`link_input` 22）以佐证其未落入豁免族；⛔ 本包**0 判定其档位** |

---

## §4 「全 `true` 独立验证件」之落面详情（**§3.3 轨 ② · 本包核心交付**）

**方法（⛔ 0 与被验证件同源）**：以 `B3.chain_convention` 字面为准，**独立源取 `index_v3`（`3ba2449cf986`）之 `caption_id` 与 `dual_v04`** —— 该件与被验证件 B3（`33ad1c01f745`）**非同件**，构成非同源复算。

| 核验项 | 结果 |
|---|---|
| `anchors` 两件一致（`index_v3.fingerprint_anchors` ＝ B3） | ✅ `True` |
| `node_state`（22 节）重算吻合 | ✅ **22/22** |
| `parent_state`（22 节）重算吻合 | ✅ **22/22** |
| `link_input`（22 节）重算吻合 | ✅ **22/22** |
| `dual`：`index_v3.dual_v04` ＝ B3 `dual` | ✅ **22/22** |
| `state_22_after_22_captions` | 重算 `bbd61495cb5d` ＝ 件内 `bbd61495cb5d` |
| `ext_1_after_anchor2` | 重算 `bf492f1c8424` ＝ 件内 `bf492f1c8424` |
| `b3_merkle_root` | 重算 `45ef859b2be9` ＝ 件内 `45ef859b2be9` |
| `byte_hash` ＝ `SHA-256(caption_id)[0:12]` | ✅ **22/22** |
| **总分歧** | **NONE** |

**⚠ 如实登记之限度（⛔ 0 声称已验证语义正确性）**：上述验证覆盖**哈希链接关系与 `byte_hash` 生成规则**；`dual` 后 6 hex（`semantic_hash`）所依 **18 hyperplanes 权重矩阵未随件落盘** ⇒ 该段**不可由盘上件非同源重算**（见 §5 `G-U04-2`）。

---

## §5 缺口 · 候呈项（**缺位即豁免不成立 · 本件 0 掩饰**）

| id | 项 | 状态 | 后果 | 归属／候呈 |
|---|---|---|---|---|
| **`G-U04-1`** | `graphs[].source` 之编码表**穷尽性声明出处** | ⚠ **部分缺位** —— 期望全集 `{0,1}` 已报、实到已报、覆盖判定 PASS；但盘上 0 有 `source` 编码表冻结件字面 ⇒ **出处为「未核得」** | 若严格要求「出处须为冻结件」，此字段之 ② 视为部分缺位 ⇒ 该字段豁免不成立 | **候呈 PI**：是否以 `index_v3` 字段定义本体为编码表出处，或另立冻结件 |
| **`G-U04-2`** | `semantic_hash` 之 LSH 独立复算依据 | ⚠ **限度** —— 18 hyperplanes 权重矩阵 0 随件落盘 | `link_verified` ②之验证范围限于哈希链接关系；⛔ 0 声称 semantic 正确性 | **候呈 PI／parent**：是否要求落 hyperplanes 权重矩阵（**须改既有产出件或另立伴随件 ⇒ 本件 0 硬改**） |
| **`G-U04-3`** | `input_selfcheck` 三分量之独立复算 | ✅ 读数面已落面；⚠ 复算强度为转引（A 级） | 不影响「分量读数在位」之判定 | 如实登记为强度限度，**非缺位** |

**另列「无法落面项」（本包 0 落面者 · 如实列明）**：

| 项 | 为何无法落面 | 本件处置 |
|---|---|---|
| **保留面（变值指纹列等）之豁免落面** | 沿 `c4e3338619c6` §3.1，保留面 **⛔ 0 豁免** ⇒ 无配套校验位可落 | ⛔ 0 落面、0 豁免；仅登记抽样实测 |
| **`E3` 面之 G6 配套位** | 沿 `edc6a548e3ca` §C‑1／§C‑2，该校验位**仅登记为义务、非设计**；且 `E3` 择档未由本裁消解（`E3-②` 未闭） | ⛔ 0 起草、0 择档 |
| **K-CF-4 档 1 之实际适用字段** | 盘上**尚无任何字段被判入档 1**（`edc6a548e3ca` §A‑4）⇒ 无具体字段可落其 G1–G6 | ⛔ 0 代判档位；本包仅落 §3.3 同源配套位 |
| **`semantic_hash` 权重矩阵之落位** | 须改既有产出件或另立伴随件 ⇒ 触发「若判定某项必须改既有数据才能落位 ⇒ **停手，列候呈**，0 硬改」 | ⛔ **停手列候呈**（`G-U04-2`） |

---

## §6 诚实边界（`γ` 老实交代 · failures & limitations）

| id | 内容 |
|---|---|
| **`γ-U04-1`** | **0 判定任何字段「豁免成立」** —— 本件仅落面配套校验位；「缺位即豁免不成立」之终判属 PI／判定面。`G-U04-1` 未闭 ⇒ `graphs[].source` 之标签位豁免**尚不成立**。 |
| **`γ-U04-2`** | **0 代裁 `U-V04-02` 备案生效时点** —— 恒等校验位落位为**本人实测事实**；备案生效属 PI 面（沿 `edc6a548e3ca` §C‑3 原样保留）。 |
| **`γ-U04-3`** | **复算强度分级如实标注**：`index_v3`／B3 之链与 `byte_hash` 读数＝**本人独立复算**；`input_selfcheck`／`cross_seed_control` 数值＝**转引源件**（A 级，本件 0 重跑）。**本件 0 声称对全部落面数据完成独立复算。** |
| **`γ-U04-4`** | **外推边界 ＝ 22 caption 构造域**（沿 `c4e3338619c6` §4.3）；⛔ 0 作任何修前／修后同口径等效比较主张。 |
| **`γ-U04-5`** | **分类归类沿既有准绳**：标签位／布尔位／定义型常量／辅助派生列之归类沿 `c4e3338619c6` §3.1 二分准绳与 `e98bee353448` §3.1 A–G 族；⛔ **0 自创新分类口径、0 自行扩类**（沿 `γ-PK-2` 继承：四类口径须 PI 复核之限度原样保留）。 |
| **`γ-U04-6`** | **`graphs[].source` 双归之处理**：沿 `c4e3338619c6` §5.2 采**标签位严轨**（码本覆盖校验），**0 沿用该件所载来源等级 B 之自认限度**。 |

---

## §7 落盘自证（**0 回改 · SHA-256／SHA-12／bytes／UTF-8 无 BOM／CRLF = 0**）

| 项 | 值 |
|---|---|
| 本件路径 | `results/_u04_1_exemption_precondition_verification_2026_10_09.md` |
| 本件 SHA-256 | `0c818a1a617577fdb97e165d7fcaa9c01910ed1c6f394381f8cabae03762591f` |
| 本件 SHA-12 | **`0c818a1a6175`**（⚠ 本行回填后本件哈希随之变更，最终值以 §8 指令③ 复算为准 —— 沿既有件「0 内写自哈希」例外体例） |
| 本件 bytes | 21,063（回填前） |
| 编码／换行 | UTF-8 **无 BOM**；**CRLF = 0**（纯 LF） |
| 落面数据件 | `results/_u04_1_exemption_precondition_verification_2026_10_09.json` · SHA-256 `bddfeac3ee2fe051114c6fa7ba5dd74e0380bbe7ad5cddaf1353e29da1c54b68` · SHA-12 **`bddfeac3ee2f`** · bytes **21,862** · UTF-8 无 BOM · CRLF = 0 |

**⛔ 0 回改确认（输入五件 ＋ 读数源三件 · 落盘前后逐件复算一致）**：见 §8 复算指令；本包**0 编辑／0 覆写／0 改名／0 移动／0 删除**任何既有件；临时件仅置于 `.tmp/`。

---

## §8 复算指令（**他人可原样复跑** · 0 网络、0 读 key）

```powershell
# 工作目录 = 仓根 _september_workspace
# ① 输入件指纹（应与 §0 表逐字一致 ⇒ 即 0 回改之证）
python -X utf8 .tmp/u04_1_chain_verify.py     # 独立源重算全链 + 布尔实测 + 码本覆盖 + 恒等校验 + 分量读数
python -X utf8 .tmp/u04_1_dual_verify.py      # byte_hash / semantic_hash 可复算性判定 + 出处溯源
python -X utf8 .tmp/u04_1_make_data.py        # 重新生成 D 件（0 改既有件）

# ② 0 回改核验（落盘前后应完全一致）
python -X utf8 -c "import hashlib;[print(hashlib.sha256(open(p,'rb').read()).hexdigest()[:12],p) for p in ['results/_criterion_application_scope_prereg_2026_10_01.md','results/_k_v3df_0_1_readings_verdict_2026_10_09.md','results/_k_cf_4_effectivity_register_2026_10_09.md','results/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md','results/_k_v3df_0_1_four_readings_2026_10_09.md','results/_k_v3df_0_1_four_readings_2026_10_09.json','corpus/v20/index_v3_2026_09_29.json','results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json','results/c5_b_group_fix_readings_2026_10_01.json']]"

# ③ 本包两件指纹
python -X utf8 -c "import hashlib,os;[print(hashlib.sha256(open(p,'rb').read()).hexdigest(),os.path.getsize(p),p) for p in ['results/_u04_1_exemption_precondition_verification_2026_10_09.md','results/_u04_1_exemption_precondition_verification_2026_10_09.json']]"
```

---

## §9 回执

*出证 = worker／`U04-1`｜2026-10-09｜PI 2026-10-09 两裁（`ask_ced8de9fd514ccc30f4e16e2` 第 3 题 ＋ `ask_69d695f301f12d158e102652` 第 3 题）之**配套校验位落面**｜规格源 `c4e3338619c6` §3.1–§3.3（**实体字面逐字执行 · 0 取宽 0 取窄**）｜落面范围源 `e98bee353448` §3.1 A–G 族 22 项 ＋ K-CF-4 档 1 适用面（以盘上为准）｜**8 件输入盘上终态实测指纹全部登记**｜产出 **2 件新件**（本登记件 ＋ 数据件 `bddfeac3ee2f`）｜**布尔位轨 ①①②全落（②经非同源重算 22/22 吻合）· 标签位轨 ①②落（3/3 覆盖检查 PASS，其中 `graphs[].source` 出处部分缺位）· 常量轨 ④落（22/22=11，漂移 0 ⇒ `U-V04-02` 条件已满足）· 派生列轨 ⑤落（四组分量四项读数齐备）· 保留面 0 落面**｜**缺口 3 项**（`G-U04-1` source 编码表出处未核得 · `G-U04-2` hyperplanes 权重矩阵 0 落盘 ⇒ 停手候呈 · `G-U04-3` 复算强度限度）｜**0 回改任何既有件、0 代裁豁免范围、0 代裁备案生效时点、0 新设阈值、0 判定任何字段豁免成立、0 触及 `E3`、0 网络、0 读 key、0 编造**｜临时件仅 `.tmp/`｜状态「**落面完成 · 缺口在册 · 待 PI 处置候呈项**」*