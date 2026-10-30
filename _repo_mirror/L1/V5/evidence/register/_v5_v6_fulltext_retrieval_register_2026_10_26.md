# `V5`／`V6` 全文取回落盘登记件（2026-10-26）

> 📌 **本件性质**：**登记件**（新件）——载两件本体之落盘事实、来源、版次、页数、字节指纹与比对结果。
> 📌 **令源**：PI 之**裁 312**（「**取回落盘作本体（推荐）**」）·见 `pi_rulings\_pi_card_answers_register_2026_10_26_v419.md` **L31**（该件 **7,321／`f11cf8368057`**·本部实测·落盘时点 2026-10-26 22:36:00）。
> 📌 **裁 312 之界（v419 L34 逐字）**：「取回者为**本体**（PDF），非转引；落盘后凡引 `V5`／`V6` 者**须引本体**（件名＋节号／页码），⛔ 再引外委之二手描述。」
> 📌 **外委值之来源**：`results\evidence\register\_k31_ext_reply_C_rounds_and_fulltext_2026_10_26.md`（**7,844／`78802a737774`**·本部实测）**L64**（`V5`）与 **L66**（`V6`）。
> 📌 **本件之界**：⛔0 落五终判｜⛔0 代 PI 裁｜⛔0 代销记｜⛔0 改／移／重命名／删任何既有件｜⛔0 改本体一字节。

---

## §0 一句话

`V5`（arXiv `cs/0011012v3`·42 页）与 `V6`（JCGM 200:2012 VIM 第三版·108 页）之**本体**已取回落盘于 `results\evidence\sources\`，两件**自测 SHA-256 与外委所给逐位相符（MATCH）**，并已由本体首页／元数据自证身份；**后引须用件名＋页码／节号**。

---

## §1 两件本体之登记

| 项 | `V5` | `V6` |
|:--|:--|:--|
| **件名（仓相对）** | `results\evidence\sources\V5_Halpern_Pearl_Causes_and_Explanations_PartI_causes_arXiv_cs0011012v3.pdf` | `results\evidence\sources\V6_JCGM_200_2012_VIM_3rd_edition_2008_corr_BIPM_official.pdf` |
| **来源 URL** | `https://arxiv.org/pdf/cs/0011012v3`（DOI `10.48550/arXiv.cs/0011012`） | `https://www.bipm.org/utils/common/documents/jcgm/JCGM_200_2012.pdf`（等价官方址 `https://www.bipm.org/documents/20126/2071204/JCGM_200_2012.pdf`；DOI `10.59161/JCGM200-2012`） |
| **题名** | *Causes and Explanations: A Structural-Model Approach. Part I: Causes* | *International vocabulary of metrology — Basic and general concepts and associated terms (VIM)* |
| **著者** | Joseph Y. Halpern（J. Y. Halpern）· Judea Pearl | JCGM／BIPM |
| **版本／版次** | arXiv **`cs/0011012v3`**（**2005-11-07**·首页逐字） | **JCGM 200:2012**·**第三版**·**「2008 version with minor corrections」**（首页逐字） |
| **页数（`pypdf` 实测）** | **42** | **108** |
| **字节** | **356,520** | **4,019,623** |
| **SHA-256（本棒自测全值）** | `73207c0e41866b44f6bafbcee54df9154ae08e3869568fd93343712b55e9e883` | `8a603e99d236a65d771f38b6dcf627953146fe023a5266b3307681ada30f4fe7` |
| **取回时点（文件 mtime）** | **2026-10-26 22:37:23** | **2026-10-26 22:39:57** |
| **落盘前 `Test-Path`** | `False`（新件） | `False`（新件） |

> 📌 **目录**：`results\evidence\sources\` 本棒新建（此前不存在）——⛔0 落入 `results\evidence\register\`（彼处放登记件）。

---

## §2 SHA-256 逐位比对（三方并列）

| 件 | 外委所给（回函 L64／L66） | 本棒自测（`Get-FileHash`·stdlib `hashlib` 亦同） | 本部复测 | **比对** |
|:--|:--|:--|:--|:--|
| `V5` | `73207c0e41866b44f6bafbcee54df9154ae08e3869568fd93343712b55e9e883` | `73207c0e41866b44f6bafbcee54df9154ae08e3869568fd93343712b55e9e883` | 同左 | **MATCH**（64 位全等·无差异） |
| `V6` | `8a603e99d236a65d771f38b6dcf627953146fe023a5266b3307681ada30f4fe7` | `8a603e99d236a65d771f38b6dcf627953146fe023a5266b3307681ada30f4fe7` | 同左 | **MATCH**（64 位全等·无差异） |

> 📌 **比对之法**：`Get-FileHash -Algorithm SHA256`（⛔0 用内建 `hash()`）＋ Python `hashlib.sha256`（`_bcheck.py` 亦输出 SHA-256 全值）——两法独立同值。
> 📌 **`V6` 之取回径之复现性**：两个官方址（`utils/common/documents/jcgm/…` 与 `documents/20126/2071204/…`）**取回同一字节**（同 bytes·同 SHA-256）⇒ 非某址之偶然而为本体之稳定字节。

---

## §3 身份自证（由**本体自身**，非转引二手）

| 件 | 证据面 | 逐字／实测 |
|:--|:--|:--|
| `V5` | 首页（PDF p.1） | 「`arXiv:cs/0011012v3  [cs.AI]  7 Nov 2005`」／「`Causes and Explanations: A Structural-Model Approach. Part I: Causes`」／「`Joseph Y. Halpern`（Cornell University, Dept. of Computer Science）· `Judea Pearl`（UCLA）」 |
| `V6` | PDF 元数据 | TITLE ＝「`JCGM 200:2012 International vocabulary of metrology - Basic and general concepts and associated terms (VIPM)`」；AUTHOR ＝「`BIPM`」；CREATOR ＝「`PScript5.dll Version 5.2.2`」 |
| `V6` | 首页（PDF p.1） | 「`JCGM 200 :2012`」／「`3rd edition`」／「`2008 version with minor corrections`」／「`© JCGM 2012`」 |

⇒ 二者与外委所记之**题名·著者·版次·页数·日期**四项**逐项相符**（`V5` 之 arXiv 号与 2005-11-07 之日期，系**本棒自本体首页读出**，非仅据外委）。

---

## §4 内锚（供后引「件名＋页码／节号」）

| 锚 | 本体位置 | 逐字（节题／要点） |
|:--|:--|:--|
| `V6` §**1.8** | **PDF p.22** | 「`1.8 (1.6) quantity of dimension one / dimensionless quantity`」——量纲指数皆零者 |
| `V6` §**1.9** | **PDF p.22** | 「`1.9 (1.7) measurement unit`」——「`unit of measurement … defined and adopted by convention`」 |
| `V6`「量之同类」 | **PDF p.19／p.21（NOTE 4）／p.22（NOTE 3）** | 「`quantities of the same kind have the same quantity dimension`」；「`Some quantities of dimension one are defined as the ratios of two quantities of the same kind`」；「`special measurement unit names are restricted to be used with quantities of a specific kind only`」 |
| `V6` 术语索引 | **PDF p.104** | 「`1.7 dimension of a quantity`／`1.8 dimensionless quantity`」 |
| `V5` | **PDF p.1** | 题名·著者·arXiv 号·日期（见 §3） |

> 📌 **锚位之一注（回源之精确·非翻案）**：外委回函 **L53** 将「`VIM 1.8 把实体计数列为无量纲量，1.9 则要求同类量才能借单位作比值』」系于 §1.8–1.9；本棒自本体实测——**§1.8**（无量纲量）与 **§1.9**（measurement unit）**同在 PDF p.22**，而「量之同类（`quantities of the same kind`）／专用单位名之限用」之措辞**位于同页 NOTE 3 之区**（另见 p.19／p.21 NOTE 4），**不属 §1.9 词条本身**。⇒ 结论不因此动，**唯引文锚位宜按本表精确**。

---

## §5 边界与老实交代

1. **二进制件不适用文本之五项字节纪律**：`V5`／`V6` 为 **PDF 二进制**（`%PDF-1.4`／`%PDF-1.6` 起首），故「UTF-8 无 BOM／纯 LF／末字节 0x0a／U+FFFD 0」之文本项**不适用**（`_bcheck.py` 以 `decode("utf-8","replace")` 读之，U+FFFD 必非零、末字节亦非 0x0a）。**本棒以「字节数＋SHA-256 全值＋页数＋首页／元数据可读」四项代之**，并将 `_bcheck.py` 之实输出抄于本件之回报中，**不伪称五项全过**。
2. **`SP 811` 之原件仍未落盘**：其登记件 `results\evidence\register\_nist_sp811_fulltext_retrieval_2026_10_25.md`（**28,684／`5447ecd37faf`**）**§1-3／L39** 逐字载「取官方 PDF 全本（90 物理页）＋官方 HTML 分章版，**内存抽取，零落盘**」·状态「**已取回**」⇒ **原件未落盘**（其 §2-1／L57 复载「全本内存抽取，**⛔ 0 落盘**」）。⛔ 本棒**未再联网重取 SP 811**。
3. **出版版本之元数据（B 级·未开卷）**：外委回函 **L65** 载 `V5` 之出版版本为 BJPS 56(4):843–887·DOI `10.1093/bjps/axi147`，并自陈「此处仅据 Crossref 元数据，不冒充出版方 PDF 已开卷」——本棒**未开卷出版方 PDF**，故此条**照录为 B 级·未复核**。
4. **本棒未取他件**：联网仅用于 `V5`／`V6` 之取回（`V6` 之址之寻觅含一次网页检索）；⛔0 取他文献、⛔0 跑实验、⛔0 调 LLM／API、⛔0 读归档区正文、⛔0 读 GLM 面。
5. **既有件触动数 ＝ 0**：本棒之写动作 ＝ ①新建目录 `results\evidence\sources\` ②落两件**新**本体 ③落本件（**新**件）。既有件**未改一字节**（活一之两件本体亦未于本棒复活后重取——本部已独立复测相符，故⛔0 重取、⛔0 重下、⛔0 改其字节）。

---

**状态行**：`V5／V6 取回落盘登记（登记件·新件）· V5 arXiv cs/0011012v3·42 页·356,520 B·SHA-256 73207c0e…·22:37:23 · V6 JCGM 200:2012 VIM 第三版·108 页·4,019,623 B·SHA-256 8a603e99…·22:39:57 · 两件与外委值**逐位 MATCH**·本部复测同值 · 身份由本体首页／元数据自证 · 内锚：V6 §1.8 p.22／§1.9 p.22／量之同类 p.19·p.21·p.22 · SP 811 原件仍未落盘（登记件 §1-3／L39）· 既有件触动数 0 · ⛔0 代裁·⛔0 代销记`
**落款**：**证据链审计官**（`evidence-auditor`）· deposon 证据链审计棒 · 2026-10-26 夜（取回 22:37–22:40·登记 22:4x）GMT+8
