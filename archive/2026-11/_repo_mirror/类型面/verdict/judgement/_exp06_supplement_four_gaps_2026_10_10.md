# EXP-06 · 四项缺位补齐件（派生列⑤／恒等校验字段／runner 源码／独立 JSON 件）· evidence-auditor · 2026-10-10

> **触发**：PI 2026-10-10 10:22「轮 33」卡（`ask_6795cd7e87a63fd8bfce8f4c` step `exp06_gaps`）裁「**派棒补齐四项**」。
> **补齐对象**：`088ba3d58c0f`（`results/_exp06_kcf4_check_bit_landing_2026_10_10.md`）§0／§3.2／§6／§7／§9 所登记之**四项缺位**。
> **输入件**：`c4e3338619c6` ＝ `results/_criterion_application_scope_prereg_2026_10_01.md` §3.1–§3.3（分层裁定表／双用途分离／强制配套校验位落面规格）｜产出件 `33ad1c01f745`（自定位）｜runner 源码（自定位——落面件所引，实为两支，见 §3.3）。
> **runtime**：纯本机只读实测（`Get-FileHash`／`python3` `hashlib`／`json`／`Select-String`／`Test-Path`／`glob`）＋ **2 次 `write`**（本件 ＋ 独立 JSON 件）。⛔ **0 网络**／⛔ **0 skill**／⛔ **0 LLM 代答**／⛔ **0 读 key**（R4）。
> **配套工具**：`.tmp/exp06_supplement_probe_2026_10_10.py`／`.tmp/exp06_independent_json_gen_2026_10_10.py`（工具件，**0 属证据面**；沿先例 `.tmp/c5_guard_minmaxstd_2026_10_01.py`）。

---

## §0 结论摘要（**先读此节**）

| # | 缺位（落面件所登记） | 补齐状态 | 承载位置 | 关键实测 |
|:-:|---|:-:|---|---|
| **①** | 派生列⑤**分量四项读数未落** | ✅ **已补齐**（§2.1） | 本件 §2.1 ＋ 独立 JSON 件 | 三分量各 `n=1`／`n_distinct=1`／`min=max=值`／`std` 未定义（如实记 `null`，**0 伪填 0.0**） |
| **②** | **产出件内恒等校验字段本身缺位** | ✅ **已补齐**（§2.2） | 独立 JSON 件 `item_2_identity_check_field_now_landed` | 22/22 ＝ 11、`violations=[]`、`representation_drift_alarm_fired=false`；**择另立件路径**（§2.2 理由三条） |
| **③** | **runner 源码 0 核读** | ✅ **已核读**（§2.3） | 本件 §2.3 ＋ 独立 JSON 件 `item_3_runner_source_evidence` | **置位者错挂已勘正**；6 字段逐条落「置位者／置位时机／依据件／是否硬写」 |
| **④** | 独立性未达「另立独立 JSON 件」层 | ✅ **已升格**（§2.4） | `results/_exp06_independent_check_2026_10_10.json` | 三环**独立重走** `all_three_rings_match=true`、22 节点逐条重算全同 |

**⚠️ 本轮三项重要发现（皆为如实登记，0 翻案、0 篡改）**：
1. **产出件 bytes 登记矛盾**：落面件 §1 登记 `40,053`，终态实测 `20,398`；而 SHA-12 `33ad1c01f745` **MATCH** ⇒ **身份无问题，是登记数字错**（§3.1）。
2. **置位者错挂**：落面件 §2 登记置位者为 `_2026_10_09.py`，实为 `_2026_09_29.py`（§2.3.1）。
3. **`self_verified_only` 系源码硬写字面量**：`L232` 无条件赋 `True` ⇒ 该位**独立性在实现级未满足**（§2.3.3）。**⚠️ 0 改读数、0 判档、0 改 runner**。

**⛔ 0 判档（铁律）**：本件**0 判 `K-CF-4` 任何档位**、⛔ **0 出 `PASS`／`FAIL`／`KD`**、⛔ **0 断「豁免成立否」** —— **判定归口＝verdict-keeper**。

---

## §1 输入件与锚链复算（**逐件 MATCH／MISMATCH**）

**复算方式**：`SHA256(全文字节)` 小写取前 12 位（`Get-FileHash -Algorithm SHA256`；⛔ **0 用内建 `hash()`**）。JSON 内复算走 `hashlib.sha256`（沿预登记件口径）。

| # | 件 | 路径 | 登记 SHA-12 | 终态实测 SHA-12 | 判定 | bytes（登记 → 实测） |
|:-:|---|---|---|---|:-:|---|
| 1 | 落面件（本棒补齐对象） | `results/_exp06_kcf4_check_bit_landing_2026_10_10.md` | `088ba3d58c0f` | `088ba3d58c0f` | ✅ **MATCH** | 20,709 → 20,709 ✅ |
| 2 | 落面规格源 | `results/_criterion_application_scope_prereg_2026_10_01.md` | `c4e3338619c6` | `c4e3338619c6` | ✅ **MATCH** | 50,322 → 50,322 ✅ |
| 3 | **产出件面** | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | `33ad1c01f745` | ✅ **MATCH** | **40,053 → 20,398 ⚠** |
| 4 | 索引件面 | `corpus/v20/index_v3_2026_10_09.json` | `74b27393574f` | `74b27393574f` | ✅ **MATCH** | 24,837 → 24,837 ✅ |
| 5 | 索引件面（历史同族） | `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | `3ba2449cf986` | ✅ **MATCH** | 24,421 → 24,421 ✅ |
| 6 | 码本出处冻结件 | `docs/SPEC_v2.0.md` | （落面件 §5.3 实测） | `bac61d51fd20` | ✅ 实测取得 | 5,333 → 5,333 ✅ |
| 7 | 档位字面源 | `results/_k_cf_4_effectivity_register_2026_10_09.md` | `edc6a548e3ca` | `edc6a548e3ca` | ✅ **MATCH** | 35,872 → 35,872 ✅ |
| 8 | 逐字段读数面源（事实源） | `results/c5_guard_0_1_recheck_verdict_2026_10_01.md` | `24418fa60ede` | `24418fa60ede` | ✅ **MATCH** | 33,287 → 33,287 ✅ |
| 9 | 补报件（派生列⑤口径源） | `results/c5_guard_minmaxstd_report_2026_10_01.md` | `f465fbdb7579`（引用） | 本轮**未复算**（0 引用为锚） | ⏸ 未取 | — |
| 10 | **置位者 runner（本轮核读对象）** | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | （本轮实测） | **`de16bc002198`** | ✅ 实测取得 | 20,322 |
| 11 | 落面件所引 runner（**实为索引件之置位者**） | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | （落面件 §2 所引） | **`7c095c54fb99`** | ⚠ **归口错挂**（§2.3.1） | 21,826 |

**✅ 8/8 可对锚件 MATCH，0 MISMATCH，0 断链。** 唯一异常＝第 3 行 **bytes 登记矛盾**（哈希同值 ⇒ 身份确认，数字登记有误）⇒ **勘误登记**（§3.1），⛔ **0 回改落面件**。

---

## §2 四项缺位 · 逐项补齐

### §2.1 缺位① · 派生列⑤ 分量四项读数（✅ **已补落**）

**规格出处**：`c4e3338619c6` §3.3 ⑤「报**各分量自身**的 `n_distinct`／`min`／`max`／`std` 四项 ＋ 标注**非被测读数列**之依据（**0 以合并列代替**）」；§5.1 第 **7** 项；§4.2「根三环并作一列 ｜ 计 **1 个辅助派生列** ＋ **3 个分量**」。

**列之定义（沿 `f465fbdb7579` §2.2 与产出件实测，三分量之确切字段）**：`chain_summary` 之 `state_22_after_22_captions` ／ `ext_1_after_anchor2` ／ `b3_merkle_root` —— **三个标量合并作一列**。

| 分量（JSON 路径） | `n` | `n_distinct` | `min` | `max` | `std` | 盘上值 | **本棒独立重算** | 同值 |
|---|:-:|:-:|---|---|---|---|---|:-:|
| `chain_summary.state_22_after_22_captions` | **1** | **1** | `bbd61495cb5d` | `bbd61495cb5d` | **未定义**（`n=1`） | `bbd61495cb5d` | `bbd61495cb5d` | ✅ |
| `chain_summary.ext_1_after_anchor2` | **1** | **1** | `bf492f1c8424` | `bf492f1c8424` | **未定义**（`n=1`） | `bf492f1c8424` | `bf492f1c8424` | ✅ |
| `chain_summary.b3_merkle_root` | **1** | **1** | `45ef859b2be9` | `45ef859b2be9` | **未定义**（`n=1`） | `45ef859b2be9` | `45ef859b2be9` | ✅ |

- **`min`／`max` 口径**：字符串列 ⇒ **字典序**（沿 `f465fbdb7579` §1 口径）；三者皆单值 ⇒ `min == max`。
- **`std` 处置**：**如实记「未定义」并附 `hex→int` 数值代理读数，⛔ 0 伪填 `0.0`**（沿 `24418fa60ede` `γ-R-3` 之既有裁定）；本棒另记 `std(ddof=0)` 数值代理 ＝ **0.0**（`n=1` 之算术值，**非 `std` 之报出值**）。
- **`hex→int` 代理读数（本棒现算）**：`state_22` ＝ **206,528,142,756,701**｜`ext_1` ＝ **210,321,043,915,812**｜`b3_merkle_root` ＝ **76,895,041,039,337**（三者 hex 宽度皆 **12**）。

**非被测读数列之依据（`c4e3338619c6` §3.3 ⑤ 之第二要件）**：
三者皆为 **22 节 caption 链之根摘要标量**（根值链之末端摘要），**非被测读数量本身** —— 本资产之**被测读数**在 caption 级指纹列（`dual`／`semantic_hash`／`byte_hash`／`coords_k`）上，根三环属**辅助／展示型派生列**（`c4e3338619c6` §3.1 派生列行二分准绳「该列**是否为被测读数列**」＋ §5.1 第 7 项；并沿 `24418fa60ede` `γ-R-5`「root 三环并作一列系**补报自建派生列**，非原始字段」）⇒ 故归退出轨（仅退出「构造退化」用途），**但分量四项读数仍须报** —— 本节即该报。

**⚠️ 本节 0 做**：⛔ **0 以合并列代替分量读数**（合并列读数仅作**参照**并列于独立 JSON 件 `merged_column_reference_only`，并明标 `for_reference_only`）；⛔ **0 新设任何数值阈值**；⛔ **0 判该列是否触发退化警报**（沿 `c4e3338619c6` §3.0 切点表 ＋ §8 风险面，**判归 verdict-keeper**）。

---

### §2.2 缺位② · 恒等校验字段（✅ **已补齐 · 择「另立独立件承载」**）

**规格出处**：`c4e3338619c6` §3.3 ④「**任一行 ≠ 11 ⇒ 表示法漂移警报**（**0 记为通过、0 静默**）＋ 报定义决定出处」；§3.3 末段「**替代校验位 0 落产出件面**……**落面属 worker 执行面 · 待本件生效后**」；§5.1 第 **8** 项。

**缺位之事实确认（落面件 §6 所陈，本棒逐项复证）**：
- ✅ **读数面已满足**：`per_caption[].dual_hex_width` **22/22 ＝ 11**、`n_distinct=1`、`min=max=11`、`std(ddof=0)=0.0`、**违例行 ＝ `[]`** ⇒ **0 表示法漂移**。
- ✅ **交叉互证**：22/22 满足 `dual_hex_width == len(dual)` ⇒ 该字段**由实际串长求值**（非硬写，见 §2.3.4）。
- ✅ **字段本身确缺位**：产出件全文正则扫描 —— `identity` **0 命中**、`identity_check` **0 命中**、`恒等` **0 命中**（`ident` 之 **92** 命中全部来自 `*_identical` 键名之子串，**非**恒等校验字段）⇒ **「读数面满足」≠「字段已落」**，落面件 §6 之判断**本棒复证成立**。

**本棒补落之字段（承载于独立 JSON 件 · 非读数面而是**真字段**）**：

| 字段键 | 值 | 意义 |
|---|---|---|
| `identity_check_dual_hex_width_equals_11` | 对象 | 恒等校验**字段本体** |
| `representation_drift_alarm_fired` | **`false`** | `c4e3338619c6` §3.3 ④ 之**判定位**（**0 记为通过**、**0 静默** —— 此键即「不静默」之载体） |
| `violation_rows` | **`[]`** | **违例行清单**（空 ＝ 0 漂移；非空即漂移） |
| `cross_check_field_equals_len_dual` | **`true`** | 该字段确由实际串长求值之旁证 |
| `identity_value_source` | `index_v3_meta.dual_rule` ＋ `3fbf6b38a383` §4.1‑3 | **定义决定出处**（§3.3 ④ 之第二要件） |

**⚠️ 择法之理由（为何取「另立独立件」而非「补落产出件」）—— 三条，逐条有实测支撑**：

| # | 理由 | 实测证据 |
|:-:|---|---|
| **1** | **回改既有登记资产（R5）** | 产出件 `33ad1c01f745` 之 SHA-12 被**至少 5 件**盘上文件引用（`088ba3d58c0f` §1／`24418fa60ede` §0／`f465fbdb7579` §0／索引件 metadata／…）⇒ 追加任一字节即改其 SHA-12 ⇒ **构成回改** |
| **2** | **必破其自校验链（本棒实测）** | 产出件自带三条自校验摘要，**当前三条全部 MATCH**：`content_sha256` ＝ `57c2fc71b3d1…`（**复算同值 ✅**）、`path_sha256` ✅、`anchor_sha256` ✅；而 `content_hash_scope` 逐字为「**full file bytes** with integrity.content_sha256 set to empty string」⇒ **追加任一字段必改 `content_sha256`** ⇒ `self_check.integrity_results_ok` 将由 `true` **翻为 `false`**，且 runner 自带 `verify_integrity()` 将返回 `false` |
| **3** | **派生 JSON 不合并** | 就地给已交付 JSON 打补丁 ＝ 对派生资产之**合并形态操作**，为铁律所禁 |

⇒ **故取「另立独立件承载」**；**与缺位④（独立性升格）合流为同一件** `results/_exp06_independent_check_2026_10_10.json` —— **一石二鸟，0 重复计数**。
**⛔ 本棒 0 向产出件写入任一字节。**

---

### §2.3 缺位③ · runner 源码核读（✅ **已核读 · 置位者错挂已勘正**）

#### §2.3.1 置位者归口（**落面件 §2 之登记有误 · 本棒勘正**）

| 项 | 落面件 `088ba3d58c0f` §2 之登记 | **本棒实测之正解** |
|---|---|---|
| 置位者 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | **`deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py`**（`de16bc002198`） |
| 依据 | 「`index_v3_meta.generator` 所载生成脚本」 | **产出件顶层 `generator` 字段自载** ＝ `…_v0_4_2026_09_29.py` |

**错挂根因（本棒定位）**：落面件读的是 **`index_v3_meta.generator`** —— 而 **`index_v3_meta` 根本不在产出件内**。产出件顶层键实测为：`task`／`task_id`／`date`／`generator`／`method`／`caliber`／`input_selfcheck`／`id_correspondence`／`frozen_proof`／`zero_overwrite_proof`／`anchors`／`chain_convention`／`per_caption`／`diff_registration`／`chain_summary`／`decision_lines_36_substitute`／`cross_source_2model_087`／`self_check`／`no_verdict_notice`／`integrity` —— **0 含 `index_v3_meta`**。该键位于**索引件** `corpus/v20/index_v3_2026_10_09.json` 内，其 `generator` ＝ `…_2026_10_09.py` ⇒ **落面件把「索引件的置位者」错安到了「产出件的置位者」头上**。

**双证（路径常量互证）**：

| runner | 输出路径常量 | 实产之件 | 是否产出 `33ad1c01f745` |
|---|---|---|:-:|
| `…_2026_09_29.py` **L62‑L63** | `corpus/v20/index_v3_2026_09_29.json` ＋ `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `3ba2449cf986` ＋ **`33ad1c01f745`** | ✅ **是** |
| `…_2026_10_09.py` **L72‑L73** | `corpus/v20/index_v3_2026_10_09.json` ＋ `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `74b27393574f` ＋ `95f3f0957be8` | ❌ **否** |

⚠️ **诚实限度**：产出件 mtime ＝ **2026‑10‑01 09:43:44**，晚于其自载 `date=2026-09-29` ⇒ 该件**曾于 10‑01 被重跑／重写**；但**置位者归属不受影响**（自载 `generator` 字段 ＋ 路径常量双证同指 09‑29 runner）。**重跑之触发原因本棒 0 推断**。

#### §2.3.2 六字段 · 置位者／置位时机／依据件／**是否硬写**（`c4e3338619c6` §3.3 ① 之三要素 ＋ 本棒新增之「是否硬写」实现级列）

| 字段 | 置位者（行号） | 置位时机 | 依据件 | **求值性质** |
|---|---|---|---|---|
| `chain.link_verified` | 09‑29 runner **L230‑L231** | 22 节点建毕（L211‑L216）**且**独立重走毕（L220‑L229）之后 | `chain_convention` 四式 ＋ `anchors.values` | ✅ **真求值** —— `rewalk_ok` 初值 `True`（L222），任一 `node_state` 不符即翻 `False`（L223‑L226），再与重导 `ext_1`／`root` 比对 AND（L229）；**0 字面量** |
| `chain.self_verified_only` | 09‑29 runner **L232** | 同循环，紧随 `link_verified` | ⚠️ **无求值依据** | ⚠️ **硬写字面量** —— `c["chain"]["self_verified_only"] = True`，**无条件**、**不依赖** `rewalk_ok`、**无任何比较** |
| `dual_hex_width` | 09‑29 runner **L194** | 每 caption 记录构造时 | `index_v3_meta.dual_rule` | ✅ **真求值** —— `len(dual)`；本棒交叉互证 22/22 满足 `== len(dual)` |
| `diff_registration_vs_f4.*`（×2） | 09‑29 runner **L199‑L200** | 落盘时与参照件逐条比对 | `results/deposon_v2_phase4_f4_2026_09_11.json`（`cf7682348617`） | ✅ **真求值** —— 真实相等比较 |
| `diff_registration_vs_v3phys.*`（×2） | 09‑29 runner **L203‑L204** | 同上 | `results/deposon_v3_physical_opt_2026_09_11.json`（`27f9bd5cc260`） | ✅ **真求值** —— 真实相等比较 |
| `chain_summary.independent_rewalk_ok` | 09‑29 runner（`chain_summary` 装配段，重走之后） | 三环比毕 | 同 `chain_convention` | ✅ **真求值** |

#### §2.3.3 ⚠️ 规格与实现之张力（如实登记 · **0 判 · 0 改码**）

`c4e3338619c6` §3.3 布尔位②要求：全 `true` 字段须附**独立验证件**，且「**0 预置为 `true`**」。
**实测**：`self_verified_only` 在源码中**即被预置为 `true`**（L232 字面量；10‑09 runner **L248** 同形）。

| 项 | 如实登记 |
|---|---|
| **读数是否改变** | ❌ **0 改变** —— 仍为 22/22 `true` |
| **独立性是否满足** | ❌ **该位之独立性在实现级未满足**（值非由任何独立验证面求出） |
| **与落面件 §3.2 之关系** | 落面件 §3.2 曾载「三个 `true` 均**由公式面与根值链可复算，非硬写**」⇒ **本棒就 `self_verified_only` 一位提出勘正**：`link_verified` 与 `independent_rewalk_ok` **确为真求值**（✅ 成立），但 `self_verified_only` **确为硬写**（❌ 该表述不成立于该字段） |
| **本棒处置** | ⛔ **0 改 runner**（改运行语义**不属**资产缺陷层，超本棒边界）｜⛔ **0 判档**｜✅ **勘误登记**（§3.3），**PI 另行处置** |
| **诚实限度** | 该硬写**是否为有意设计**，源码**0 陈述**，**本棒 0 推断** |

#### §2.3.4 其余诚实限度（沿用并更新）

- ⛔ **冻结升级件正文仍 0 核读**：`docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md`（`b10fae0da66d`）**存在性与哈希已核**，但**§2.3 B3 Merkle 正文本棒仍未逐字核读**（沿落面件 §2 同款限度）⇒ 如实登记。
- ⚠️ **runner 本棒 0 执行**：仅**静态核读**（读源码、求值性质判定），**0 运行** ⇒ 运行时行为未证。
- ⚠️ **测量仪器自审**：本棒 `python` stdout 之 `§`／`恒` 在 PowerShell 控制台曾显示为替换字符 —— 经字节级复核，**系终端代码页渲染问题，非文件编码缺陷**（同族于落面件 §5.4 之自审登记）。

---

### §2.4 缺位④ · 独立性升格为独立 JSON 件（✅ **已另立**）

**新件**：`results/_exp06_independent_check_2026_10_10.json`

| 项 | 内容 |
|---|---|
| **独立性依据** | ① 读数**自产出件自身数据**（`per_caption[].dual` ＋ `anchors.values`）**现算**，**0 重跑任一 runner**；② **0 于验证时调用** `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_*.py`；③ **复算配方逐字载于件内** `independence_statement.recompute_recipe_verbatim`（＝产出件 `chain_convention` 四式），第三方**不读本棒代码**即可复现；④ ⛔ **0 合并任何既有派生 JSON**（新立件，**非合并目标**） |
| **承载之独立读数** | 三环 `state_22`／`ext_1`／`b3_merkle_root` **全部独立重算并与盘上同值**（`all_three_rings_match=true`）；22 节点 `node_state` 逐条重算**全同** |
| **锚绑定** | `anchors.values[0]` ＝ `7d6d3d39fad8` ＝ `anchor0_equals_existing_chain_current_root.existing_current_root` ✅；`verifier/runs/2026-09-04_pd_v0.jsonl`（`5042869bdf85`）**在盘** |
| **产出件自校验复证** | `content_sha256`／`path_sha256`／`anchor_sha256` **三条全 MATCH**、`self_check.integrity_results_ok=true` ⇒ 即 §2.2 择另立件之实测依据 |
| **标签位复认** | `graphs[].family` ＝ `{L,S}`｜`captions[].family` ＝ `{L,S}`｜`graphs[].source` ＝ `{0,1}`；期望 ⊆ 实到 ✅（**仅集合包含判，0 引入新阈值**） |
| **⛔ 0 做** | ⛔ **0 自写本件 SHA-256**（自指回环）｜⛔ **0 判档**｜⛔ **0 合并派生 JSON** |

---

## §3 勘误登记（**⛔ 0 回改任何既有件**）

> **处置原则**：哈希链断裂／数字矛盾／frozen 内缺陷 ⇒ **勘误登记**，**0 回改历史行**（R5）。

| id | 类型 | 件 | 登记值 | 终态实测 | 影响 | 处置 |
|---|---|---|---|---|---|---|
| **`E-EXP06-S1`** | **数字矛盾（登记 vs 终态）** | 产出件 `33ad1c01f745` | bytes ＝ **40,053**（落面件 §1 第 1 行） | bytes ＝ **20,398**；CR ＝ **736**、LF ＝ **736**、**无 BOM** | **身份无问题**（SHA-12 **MATCH**）；仅登记数字有误。**旁证**：事实源 `24418fa60ede` §0 第 6 行独立登记 `33ad1c01f745`／**20,398**／736 行／CRLF=736 —— 与本棒实测**逐项一致**。⚠️ **错因本棒 0 推断** | **勘误登记**；⛔ **0 回改落面件**；PI 另行处置 |
| **`E-EXP06-S2`** | **归口错挂（实现级）** | 产出件置位者 | 落面件 §2 登记 ＝ `…_2026_10_09.py` | **正解 ＝ `…_2026_09_29.py`**（自载 `generator` ＋ 路径常量双证） | 该位**三要素之第一要素（置位者）**原登记有误 | **勘误登记**（§2.3.1）；⛔ **0 回改落面件** |
| **`E-EXP06-S3`** | **规格与实现之张力** | 09‑29 runner **L232**（10‑09 runner L248 同形） | §3.3 ②要求「**0 预置为 `true`**」 | `self_verified_only` **无条件赋 `True`** | 该位**独立性实现级未满足**；**读数 0 改变** | **登记 · 0 判档 · 0 改码**（超资产缺陷层）；PI 另行处置 |
| **`E-EXP06-S4`** | **落面件表述之局部勘正** | 落面件 §3.2 | 「三个 `true` 均由公式面与根值链可复算，**非硬写**」 | `link_verified`／`independent_rewalk_ok` **✅ 成立**；`self_verified_only` **❌ 确为硬写** | 该表述**对一位不成立** | **勘误登记**（§2.3.3）；⛔ **0 回改落面件** |

---

## §4 幽灵引用对账（三方比对 · 五分支判定）

**方法**：所引路径 vs 盘上实存；仓外目录本轮**未扩搜**（全部引用均指仓内路径，无仓外绝对路径依赖）⇒ 无 `GHOST_REF_OUTSIDE`。

| # | 被引路径 | 盘上实存 | 判定 | SHA-12 |
|:-:|---|---|:-:|---|
| 1 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | ✅ | **FOUND_IN_REPO** | `33ad1c01f745` |
| 2 | `corpus/v20/index_v3_2026_10_09.json` | ✅ | **FOUND_IN_REPO** | `74b27393574f` |
| 3 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | ✅ | **FOUND_IN_REPO** | `de16bc002198` |
| 4 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | ✅ | **FOUND_IN_REPO** | `7c095c54fb99` |
| 5 | `results/deposon_v2_phase4_f4_2026_09_11.json` | ✅ | **FOUND_IN_REPO** | `cf7682348617` |
| 6 | `results/deposon_v3_physical_opt_2026_09_11.json` | ✅ | **FOUND_IN_REPO** | `27f9bd5cc260` |
| 7 | `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` | ✅ | **FOUND_IN_REPO**（**正文 0 核读**） | `b10fae0da66d` |
| 8 | `verifier/runs/2026-09-04_pd_v0.jsonl` | ✅ | **FOUND_IN_REPO** | `5042869bdf85` |
| 9 | `docs/SPEC_v2.0.md` | ✅ | **FOUND_IN_REPO** | `bac61d51fd20` |
| 10 | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | ✅ | **FOUND_IN_REPO** | `c13449101ab3` |
| 11 | `corpus/v20/index.json` | ✅ | **FOUND_IN_REPO** | `8423ffe266af` |
| 12 | `corpus/v20/strip_captions_22.json` | ✅ | **FOUND_IN_REPO** | `6a2656878745` |

**五分支汇总**：`FOUND_IN_REPO` **12** ｜ `GHOST_REF_OUTSIDE` **0** ｜ `MISSING_TRUE`（真缺件）**0** ｜ `SAME_IDENTITY`（同哈希多份，不重复计数）**0** ｜ `CONFLICT`（同名不同哈希）**0**。

**✅ 元数据交叉互证**：索引件 `index_v3_meta.base_index_sha256` ＝ `8423ffe266af…` ⇔ 第 11 行实测；`caption_source_sha256` ＝ `6a2656878745…` ⇔ 第 12 行实测 ⇒ **两条上游引用链亦在盘且一致**。
⚠️ **未核面（如实登记）**：`corpus/v20/index_v3_2026_09_29.json` 之 `index_v3_meta` 本棒**未逐项展开**（仅取其文件哈希作同族比对面）；`P_D_FINGERPRINT_V0_4_SPEC.md` **仅核存在性与哈希，0 读正文**。

---

## §5 0 回改确认（本棒之核心纪律）

| 项 | 状态 |
|---|---|
| **既有件写入** | **0** |
| **既有件编辑／覆写／追加** | **0** |
| **既有件删除／改名／移动** | **0** |
| **产出件 `33ad1c01f745`** | **byte 0 触动**（仅 `json.load` 只读解析 ＋ 哈希复算） |
| **runner 两支源码** | **byte 0 触动**（仅静态读取） |
| **索引件／冻结件／判据源** | **byte 0 触动** |
| **本棒写动作** | **新增 2 件**：`results/_exp06_supplement_four_gaps_2026_10_10.md`（本件）＋ `results/_exp06_independent_check_2026_10_10.json`；另 **2 件工具脚本**于 `.tmp/`（**0 属证据面**） |
| **碰写规避** | 恒等校验字段**未回写产出件**（若回写必破其三条自校验链 ＋ 构成回改 ⇒ 见 §2.2 三条理由） |

---

## §6 0 做与限制声明

- ⛔ **0 判档**：**0 判 `K-CF-4` 档位**、⛔ 0 出 `PASS`／`FAIL`／`KD`、⛔ 0 断「豁免成立否」—— **判定归口＝verdict-keeper**。
- ⛔ **0 改 runner 源码**：改运行语义**不属**资产缺陷层，超本棒边界 ⇒ 仅登记（`E-EXP06-S3`）。
- ⛔ **0 回改任何既有件**：四条勘误一律**另立登记**，历史行 **0 触动**（R5）。
- ⛔ **0 新设任何数值阈值**：退化阈值 `n_distinct ≤ 3`、门槛 `≥ 4` 且 `std > 0`、布尔域上界 `2`、恒等兜底值 `11` —— **全部逐字沿既有件**（沿 `c4e3338619c6` §3.0）。
- ⛔ **0 以合并列代替分量读数**；⛔ **0 自行扩类**（`graphs[].structure` 7 类仍**未**落覆盖校验，沿落面件 §5.5 未覆盖面之登记）。
- ⛔ **0 合并派生 JSON**；⛔ **0 读 key**（R4）；⛔ **0 读 `.env`**。
- ⛔ **0 网络** ／ ⛔ **0 skill** ／ ⛔ **0 LLM 代答**。
- ⛔ **0 改实验结论本体**：⛔ **0 触碰** `24418fa60ede` 任何结论、⛔ **0 翻案**、⛔ **0 篡改**；**标注 ≠ 篡改**。
- ⚠️ **已知未覆盖面（如实登记，非掩饰）**：冻结升级件正文 0 核读；runner 0 执行；`E-EXP06-S1` 错因 0 推断；`self_verified_only` 硬写**是否有意** 0 推断。

---

## §7 落盘自证

| 项 | 内容 |
|---|---|
| **落前撞名实测** | `Test-Path 'results/_exp06_supplement_four_gaps_2026_10_10.md'` ＝ **False**；`Test-Path 'results/_exp06_independent_check_2026_10_10.json'` ＝ **False**；`results/` 内 `*exp06_supplement*`／`*exp06_independent*` glob **0 命中** ⇒ ✅ **新名新建 · 0 覆写** |
| **命名合规** | `_exp06_supplement_four_gaps_2026_10_10.md`／`_exp06_independent_check_2026_10_10.json` ＝ `_主题_日期` 形态；⛔ **0 V-阶段前缀**（沿 `57024f2cd30a` §1.2②）；**0 `_v5_` 类前缀** |
| **编码／行尾** | 两件皆 **UTF-8 无 BOM · LF**（落盘后按字节实测复核，见交付回执） |
| **网络／skill／LLM** | **0 网络** ｜ **0 skill** ｜ **0 LLM 代答** |
| **本件自身指纹** | ⛔ **不自写入本件**（自指回环）⇒ **随交付回执回报终态 SHA-256／SHA-12／bytes／BOM／CRLF**；外部观测者请以 `Get-FileHash -Algorithm SHA256` 独立复算 |