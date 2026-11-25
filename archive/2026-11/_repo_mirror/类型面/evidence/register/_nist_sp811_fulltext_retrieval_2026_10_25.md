# NIST SP 811 全文联网取回登记（2026-10-25）

> 📌 **代号首现之白话**：`SP 811`（NIST 之《国际单位制（SI）使用指南》·官方出版物编号）｜`round`（本案之轮次单位字面）｜`rounds`（本案之轮次单位复数形）｜`day`／`hour`（日／小时之时间单位）｜`B 级`（文献核验未逐条完成之等级）｜`KD`（已知缺陷登记册·**非**五终判语汇）。
>
> 📌 **本件面**：联网取回 NIST SP 811 正本全文，就 `round`／`day`／`hour` 三事取逐字引与检索证据。**⛔ 0 校准、⛔ 0 判定、⛔ 0 落任一终判用语、⛔ 0 修改任何既有件一字、⛔ 0 移动／重命名／删除／新建目录。**

---

## §0 一句话

**取到**：NIST SP 811 正本全文（官方 PDF 90 物理页，2,027,518 B，SHA-256 `788dd8f0bcb0…`，DOI 解析终址即 nvlpubs.nist.gov）；**`round` 一词在全文中作独立词命中 0 次**（27 处 `round*` 全为 `rounding`／`rounded`，义为「数值修约」）；**`day`／`hour` 之换算逐字见于 Table 6（印刷页 8）**：`1 h = 60 min = 3600 s`、`1 d = 24 h = 86 400 s`，并于 Appendix B.8（页 48）／B.9（页 67）以 `8.64 E+04`／`3.6 E+03` 复载。

---

## §1 令源

### §1-1 PI 之裁

- PI 于 **2026-10-25 01:1x** 裁 **「甲：联网取 SP 811 全文」**（本棒派工单一字载：本棒明确许联网，限取 SP 811 及其官方附录）。
- 本棒据此**仅**取 SP 811 及其官方附录；**⛔ 0 跑实验｜⛔ 0 调 LLM／API｜⛔ 0 读 GLM｜⛔ 0 读 `〔归档区〕` 正文**。

### §1-2 辨明件之自陈（PI 所指件 · 实测指纹相符）

- 派工单所指：`results\verdict\judgement\_ledger_landed_definition_dispute_2026_10_25.md`。
- **本棒实测**：该路径**不存在**；按名检索得实名 **`_ledger_landed_definition_disputation_2026_10_25.md`**（`disputation`）——派工单少 `ation`。二者指纹与派工单所载**一致**：
  - `results\verdict\judgement\_ledger_landed_definition_disputation_2026_10_25.md` — **32,434 B／SHA-12 `62424c42401b`**（本棒 `Get-FileHash` 实测一次）。
- 该件 **L131** 逐字（PI 所据之自陈）：

  > 「且其 **L370** 自陈「**NIST SP 811 全文未获**」与「**未核**『`rounds` 在 SP 811 单位总表中确实未被收录』之**逐条**事实」⇒ 裁 29 之「逐字明证」**未达成**（其结论系推导·自标 B 级）。」

- 该件所指之 B 级件 **`results\evidence\register\_t5_round2_five_gaps_step2_literature_2026_10_24.md`**（本棒实测 **56,078 B／SHA-12 `c6d2e7dbb004`**），其 **L370** 逐字：

  > 「① NIST SP 811 **全文未获** ⇒ 其 Appendix B 之**逐条换算因子**本棒⛔ 0 逐条核（§2.3／§3.3／§5.3 之时间换算三值系**定义性推导**，非逐字转录）；… ⑤ 本棒**未核**「`rounds` 在 SP 811 单位总表中确实未被收录」之**逐条**事实（该结论系基于本棒所获 NIST 页面之时间单位枚举＋未获全文之限制而作，**标 B 级**）。」

### §1-3 本棒之取回缺口（对应上列两处「未获／未核」）

| 缺口（辨明件所载） | 本棒处置 | 状态 |
|:--|:--|:--|
| SP 811 全文未获 | 取官方 PDF 全本（90 物理页）＋官方 HTML 分章版，**内存抽取，零落盘** | **已取回** |
| 未逐条核 `rounds` 在 SP 811 单位总表中是否被收录 | 全本正则 `\bround\b` 命中 **0**；逐字核 Table 6／B.8／B.9 时间类单位枚举 | **已逐条核**（见 §4-1） |
| Appendix B 换算因子未逐条核 | 逐条引 B.8（页 48）／B.9（页 67）之 `day`／`hour` 行 | **已逐条核**（见 §4-3） |

---

## §2 检索式与命中（逐条）

**检索时点**：2026-10-25 **01:16–01:35（GMT+0800）**。全部经本棒 `web_search`／`web_fetch`／`Invoke-WebRequest`／`requests` 实取。

### §2-1 检索式逐条

| # | 检索式／URL | 命中 | 处置 |
|:--|:--|:--|:--|
| R1 | `web_search`: `NIST Special Publication 811 Guide for the Measurement of Environmental Quantities official nist.gov` | 首命中即 `https://www.nist.gov/pml/pubs/sp811/indexfull.cfm`（标题 `Special Publication 811 (Extended Contents)`·source `nist.gov`）；另命中 `https://www.nist.gov/pml/special-publication-811/special-publication-811-extended-contents` 及 NIST Metric Publications 页（载 `Guide for the Use of International System of Units (SI) NIST SP 811 Edition: 2008 … This 2008 edition supersedes NIST Special Publication 811, 1995 Edition, April 1995.`） | 采信之 nist.gov 条目 **3** 条 |
| R2 | `web_fetch` `https://www.nist.gov/pml/pubs/sp811/indexfull.cfm` | HTML 全文分章版首页（载作者行 `A. Thompson and B. N. Taylor`、PDF 链接 `https://doi.org/10.6028/NIST.SP.811e2008`、章节目录含 `B.7 Rules for rounding numbers…`／`B.8 Factors for units listed alphabetically`／`B.9 Factors for units listed by kind of quantity`） | 全取 |
| R3 | `web_fetch` `https://www.nist.gov/pml/special-publication-811/special-publication-811-extended-contents` | Extended Table of Contents 全 **12 章＋4 附录＋Footnotes**（`Created July 2, 2009, Updated December 8, 2025`） | 全取（作 HTML 之目录对照） |
| R4 | `Invoke-WebRequest` 分章抓取 `https://www.nist.gov/physical-measurement-laboratory/nist-guide-si-{version-history, preface, check-list-reviewing-manuscripts, chapter-1-introduction, chapter-2…chapter-10, appendix, appendix-b, appendix-c, appendix-d, footnotes}`（**18** 个 URL） | **15** 页取到；**3** 页取页中断（`preface`／`check-list-reviewing-manuscripts`／`chapter-1-introduction`，重试亦中断） | 见 §5-1 诚实交代 |
| R5 | `requests` 取官方 PDF `https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication811e2008.pdf` | **HTTP 200**·**2,027,518 B**·`application/pdf`；**90 物理页**（`pypdf`）；文本层 **321,986 字符** | 全本内存抽取，**⛔ 0 落盘** |
| R6 | `requests` GET `https://doi.org/10.6028/NIST.SP.811e2008` | **200**；终址 `https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication811e2008.pdf`；`Content-Length` **2027518**；`Content-Type` `application/pdf` | DOI→PDF 链路证实 |
| R7 | `requests` HEAD 同 DOI | **404**（doi.org 对 HEAD 之处理差异） | 见 §5-5 诚实交代 |

### §2-2 全文词频检索（PDF 全本 90 页 · 321,986 字符 · 大小写不敏感）

| 检索式（正则） | 命中数 | 语义判读 |
|:--|--:|:--|
| `\bround\b` | **0** | **全文无以 `round` 为词形之量／单位／词条** |
| `\bround\w*` | **27** | 全为 `rounding`（17）＋ `rounded`（10）＝「数值修约」，**非「轮次」**；分布：PDF 物理页 11(3)／13(2)／52(1)／53(1)／55(15)／56(5) |
| `\bhours?\b` | **85** | — |
| `\bdays?\b` | **14** | — |
| `\brevolution\w*` | **9** | 「转／周」之最近义项（见 §4-2） |
| `\brotations?\b` | 1 | — |
| `\bturns?\b` | 1 | — |
| `\bcycles?\b` | 1 | — |

**HTML 分章面交叉核对（18 URL，见 R4）**：`\bround\b` 于**全 18 页皆 0**；`\bround\w*` 仅 Appendix B 页为 **22**（PDF 版 27 与 HTML 版 22 之差，因 HTML 版表格折叠，见 §5-3）。

---

## §3 `SP811` 正身（全名·版次·URL·时点）

| 项 | 值（逐字／实测） |
|:--|:--|
| **全名** | **Guide for the Use of the International System of Units (SI)** |
| **编号·版次** | **NIST Special Publication 811, 2008 Edition**（`SP 811e2008`）；PDF 元数据 `Title`＝`Guide for the Use of the International System of Units (SI)`；`Author`＝`Ambler Thompson`；`Creator`＝`Acrobat PDFMaker 8.1 for Word`；`Producer`＝`Acrobat Distiller 8.1.0 (Windows)`；`CreationDate`＝**2008-05-19** |
| **作者** | **Ambler Thompson**（Technology Services）and **Barry N. Taylor**（Physics Laboratory） |
| **发布机构** | **National Institute of Standards and Technology**, Gaithersburg, MD 20899（Physical Measurement Laboratory） |
| **日期·版次沿革** | **March 2008**；**2nd printing November 2008**（`Note on 2nd printing: This 2nd printing dated November 2008 of NIST SP811 corrects a number of minor typographical errors present in the 1st printing dated March 2008.`） |
| **引用式（逐字）** | `Natl. Inst. Stand. Technol. Spec. Publ. 811, 2008 Ed., 85 pages (March 2008; 2nd printing November 2008)`；`CODEN: NSPUE3` |
| **所supersede之版** | `(Supersedes NIST Special Publication 811, 1995 Edition, April 1995)` |
| **官方 URL · PDF（DOI 解析终址）** | `https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication811e2008.pdf` |
| **官方 URL · DOI** | `https://doi.org/10.6028/NIST.SP.811e2008`（GET → 200 → 终址同上） |
| **官方 URL · HTML 落地页** | `https://www.nist.gov/pml/special-publication-811` |
| **官方 URL · HTML 全文目录（Extended Contents）** | `https://www.nist.gov/pml/special-publication-811/special-publication-811-extended-contents`（另旧址 `https://www.nist.gov/pml/pubs/sp811/indexfull.cfm`） |
| **检索时点** | **2026-10-25 01:16–01:35（GMT+0800）**（本棒 `web_search`／`web_fetch`／HTTP 实取时窗） |
| **本棒实测指纹** | PDF **2,027,518 B**；SHA-256 `788dd8f0bcb0ec06e40c300690266742532a7e760a93be57764b77ed0ef3482f`；**90 物理页**（`pypdf` 计）；文本层 **321,986 字符** |

> 📌 **页码体例**：本件引文之页码为**该 PDF 印刷页码**（页眉数字），并附 **PDF 物理页**对照（印刷页 ＝ 物理页 − 12；正文起于物理页 13＝印刷页 1）。
> 📌 **85 页 vs 90 页**：引用式载 `85 pages`（正文印刷页码口径），PDF 文件实含 **90 物理页**（含封面／题名页／版权页／罗马数字目录页等前置件）。二者口径不同，非矛盾。

---

## §4 三事之逐字引

### §4-1 第一事：`round`／轮次 之换算定义

**结论（文献面）**：**SP 811 正本全文中不存在以 `round` 为词形之量／单位／词条**——正则 `\bround\b` 于全文 90 页（321,986 字符）命中 **0**；于官方 HTML 分章 18 页亦全为 **0**。故 **`round`／`rounds` 在 SP 811 内无换算定义可引**。**「轮次」之最近义项在 SP 811 为 `revolution`（转），其换算对象为角度而非时间。**

#### §4-1-1 检索证据（逐条）

| 面 | 检索式 | 命中数 |
|:--|:--|--:|
| PDF 全本（90 页／321,986 字符） | `\bround\b`（case-insensitive） | **0** |
| PDF 全本 | `\bround\w*` | **27**（逐处核：全为 `rounding`／`rounded`） |
| PDF 全本 | `\brotations?\b`／`\bturns?\b`／`\bcycles?\b` | 1／1／1 |
| PDF 全本 | `\brevolution\w*` | **9** |
| 官方 HTML 分章（18 URL） | `\bround\b` | **全 18 页皆 0** |
| 官方 HTML 分章 | `\bround\w*` | 仅 Appendix B 页 **22** |

#### §4-1-2 `round*` 之 27 处逐处归属（PDF 物理页）

- 物理页 **11**（罗马页 ix，目录）：3 处 — 目录条目 `B.7 Rules for rounding numbers and converted numerical values of quantities`／`B.7.1 Rounding numbers`／`B.7.2 Rounding converted numerical values of quantities`。
- 物理页 **13**（印刷页 1，§1.2）：2 处 — 逐字（§1.2 Outline of Guide）：

  > `Appendix B also includes a simplified discussion of rounding numbers and rounding converted numerical values of quantities.`

- 物理页 **52**（印刷页 40，§B.4 Organization of entries and style）：1 处 — 逐字：

  > `A factor in boldface is exact. All other factors have been rounded to the significant digits given in accordance with accepted practice (see Secs. 7.9, B.7.2, and Refs. [4: ISO 31-0] and [6]).`

- 物理页 **53**（印刷页 41，B.8 表注 1）：1 处 — 逐字：

  > `1. Guidance on rounding converted numerical values of quantities is given in Sec. B.7.2.`

- 物理页 **55**（印刷页 43，§B.7／§B.7.1 Rounding numbers）：15 处 — 逐字（§B.7.1 首句）：

  > `B.7.1 Rounding numbers`
  >
  > `To replace a number having a given number of digits with a number (called the rounded number) having a smaller number of digits, one may follow these rules:`
  >
  > `1. If the digits to be discarded begin with a digit less than 5, the digit preceding the 5 is not changed.`
  >
  > `Example: 6.974 951 5 rounded to 3 digits is 6.97`

- 物理页 **56**（印刷页 44，§B.7.2 Rounding converted numerical values of quantities）：5 处 — 逐字（§B.7.2 首句）：

  > `B.7.2 Rounding converted numerical values of quantities`
  >
  > `The use of the factors given in Secs. B.8 and B.9 to convert values of quantities was demonstrated in Sec. B.3.`

**⇒ 判读（文献面·非本案判定）**：SP 811 之 `round*` 全部 27 处皆为「**数值修约**（rounding numbers／rounded number／rounding error）」之义，**无一为「轮次」之量或单位**。

#### §4-1-3 「轮次」之最近义项（`revolution`）· 逐字

- **§8.1 Time and rotational frequency**（印刷页 **23**／PDF 物理页 **35**）逐字：

  > `8.1 Time and rotational frequency`
  >
  > `The rotational frequency n of a rotating body is defined to be the number of revolutions it makes in a time interval divided by that time interval [4: ISO 80000-3]. The SI unit of this quantity is thus the reciprocal second (s−1). However, as pointed out in Ref. [4: ISO 80000-3], the designations "revolutions per second" (r/s) and "revolutions per minute" (r/min) are widely used as units for rotational frequency in specifications on rotating machinery.`

- **Appendix B.8**（印刷页 **54**／PDF 物理页 **66**）逐字换算行：

  > `revolution (r) ........................................................ radian (rad) .......................................... . 6.283 185 E+00`
  >
  > `revolution per minute (rpm) (r / min) ................... radian per second (rad / s) .................... 1.047 198 E−01`

**⇒ 即：SP 811 之「转」之换算为「角度（radian）」，其时间侧为 `r/s`、`r/min`；`revolution` 本身不作时间量之单位列出。**

### §4-2 第二事（第一）：`day`／`hour` 之换算 —— 逐字

#### §4-2-1 §5.1.1 与 Table 6（印刷页 **8**／PDF 物理页 **20**）

§5.1.1 节名逐字（HTML 与 PDF 两面一致）：

> `5.1.1 Hour, degree, liter, and the like`
>
> `Certain units that are not part of the SI are essential and used so widely that they are accepted by the CIPM, and thus by this Guide, for use with the SI [2, 3]. These units are given in Table 6.`

**Table 6 之时间三行（PDF 文本层逐字，照录其空格与列序）**：

> `Table 6. Non-SI units accepted for use with the SI by the CIPM and this Guide`
>
> `Name  Symbol  Value in SI units`
>
> `minute—time  min  1 min = 60 s`
>
> `hour—time  h  1 h = 60 min = 3600 s`
>
> `day—time  d  1 d = 24 h  =  86 400 s`

**（HTML 版同一表之逐字，列序略异，供交叉核对）**：

> `minute—time min 1 min = 60 s`
>
> `hour—time h 1 h = 60 min = 3600 s`
>
> `day—time d 1 d = 24 h = 86 400s`

#### §4-2-2 §8.1 Time and rotational frequency（印刷页 **23**／PDF 物理页 **35**）逐字

> `The SI unit of time (actually time interval) is the second (s) and should be used in all technical calculations. When time relates to calendar cycles, the minute (min), hour (h), and day (d) might be necessary. For example, the kilometer per hour (km/h) is the usual unit for expressing vehicular speeds. Although there is no universally accepted symbol for the year, Ref. [4: ISO 80000-3] suggests the symbol a.`

#### §4-2-3 §6.2.8（印刷页 **15**／PDF 物理页 **27**）逐字

> `However, to avoid confusion, prefix symbols (and prefix names) are not used with the time-related unit symbols (names) min (minute), h (hour), d (day); nor with the angle-related symbols (names) ° (degree), ′ (minute), and ″ (second) (see Table 6).`

### §4-3 第三事：Appendix B 之逐条换算因子（`day`／`hour`）

#### §4-3-1 Appendix B.8 — Factors for units listed alphabetically（印刷页 **48**／PDF 物理页 **60**）逐字

> `To convert from  to  Multiply by`
>
> `day (d) .................................................................. second (s) ............................................. ........ 8.64   E+04`
>
> `day (sidereal) ....................................................... second (s) ..............................................  8.616 409   E+04`

#### §4-3-2 Appendix B.9 — 按量类编排之 TIME 段（印刷页 **67**／PDF 物理页 **79**）逐字

> `TIME`
>
> `day (d) ................................................................. second (s) .............................................. ........ 8.64   E+04`
>
> `day (sidereal) ....................................................... second (s) .............................................  8.616 409   E+04`
>
> `hour (h) ................................................................ second (s) ............................................... ......... 3.6   E+03`
>
> `hour (sidereal) ...................................................... second (s) .............................................  3.590 170   E+03`
>
> `minute (min) ........................................................ second (s) ..................................................... ... 6.0   E+01`
>
> `minute (sidereal) .................................................. second (s) .............................................  5 .983 617   E+01`
>
> `year (365 days) ..................................................... second (s) ................................................... 3.1536   E+07`

#### §4-3-3 Appendix B 表注 18（印刷页 **51**／PDF 物理页 **63**）逐字

> `18 This conversion factor is based on 1 d = 86 400 s; and 1 Julian century = 36 525 d. (See The Astronomical Almanac for the Year 1995, page K6, U.S. Government Printing Office, Washington, DC, 1994).`

### §4-4 三事之合观（文献面·仅陈述，不涉本案取值）

| 问 | SP 811 全文之字面 |
|:--|:--|
| `round`／轮次 有无换算定义？ | **无此词**（`\bround\b` 命中 0）；全文 `round*` 27 处皆「数值修约」义。`revolution` 为最近义项，其换算对象为**角度**（`r` → `rad`，`6.283 185 E+00`；`rpm` → `rad/s`，`1.047 198 E−01`） |
| `day` 之换算 | **1 d = 24 h = 86 400 s**（Table 6，页 8）；B.8／B.9 作 `8.64 E+04`（`day (sidereal)` → `8.616 409 E+04`） |
| `hour` 之换算 | **1 h = 60 min = 3600 s**（Table 6，页 8）；B.9 作 `3.6 E+03`（`hour (sidereal)` → `3.590 170 E+03`） |

**⇒ 与本案之字面值之关系（⛔ 0 混同）**：SP 811 之 `86 400 s`／`3600 s` 为**文献值**；本案 `3` 为**本案字面值**。**二者不相等、本棒不以其一推导其二、亦不以其一校准其一。**

---

## §5 老实交代

1. **HTML 分章面有三页未取到**：R4 之 18 个 URL 中，`preface`、`check-list-reviewing-manuscripts`、`chapter-1-introduction` 三页**取页连接被关闭**，重试仍中断。⇒ **本件不主张「HTML 版逐章完备」**。该三章之内容**由官方 PDF 全本覆盖**（同一出版物、同一 2008 版），故 §4 之逐字引不受此缺影响；然「两独立载体互证」于此三页**不成立**，如实登记。
2. **PDF 文本层之抽取形态**：Table 6／B.8／B.9 为表格，PDF 文本层将其线性化（名称列与数值列分离），本件按文本层**逐字照录**并保留其空格（如 `86 400 s` 中之千分位空格、`1 d = 24 h  =  86 400 s` 之双空格）。**表格之版面列对齐系文本层重建，非版面原样**；若需版面原样，须以 PDF 渲染图为准。
3. **PDF 版 `round*` 27 与 HTML 版 22 之差**：因 HTML 版折叠表格（Table 6 数值列未逐行展开），**非两版文字有别**；二者于 `\bround\b` 均 **0**。
4. **本棒之射程**：**仅**核「SP 811 有无 `round` 一词」与「`day`／`hour` 换算之逐字」。**⛔ 0 校准本案任何值、⛔ 0 主张 `rounds` 不可通约（或可通约）、⛔ 0 落任一终判用语、⛔ 0 闭任何 KD、⛔ 0 宣告任何段落之毕或门槛成就、⛔ 0 代 PI 裁**。B 级件之结论**是否随之升格，属判读面，非本棒所出**。
5. **DOI 之 HEAD 为 404**：R7 中 `HEAD https://doi.org/10.6028/NIST.SP.811e2008` 返 **404**，而同址 **GET 返 200** 并正确解析至官方 PDF。⇒ 本件仅以 **GET** 路径为证；**不主张 DOI 对 HEAD 之行为**，亦不据此推断链死。
6. **派工单所载辨明件路径少 `ation`**：派工单作 `_ledger_landed_definition_dispute_2026_10_25.md`，盘上实名为 `_ledger_landed_definition_disputation_2026_10_25.md`。本棒按**盘上实名**引用，指纹（32,434 B／`62424c42401b`）与派工单所载一致，故**据实认定二者所指同一件**；该路径差异**如实登记**，**⛔ 0 擅改派工单、⛔ 0 重命名盘上件**。
7. **页码换算之自证**：印刷页 ＝ PDF 物理页 − 12，系逐页读取页眉数字实测所得（物理页 13→1、20→8、27→15、35→23、48→48 于物理页 60、51 于物理页 63、54 于物理页 66、67 于物理页 79、43 于物理页 55、44 于物理页 56），**非按偏移推算**。
8. **未触他面**：**⛔ 0** 跑实验、**⛔ 0** 调 LLM／API、**⛔ 0** 读 GLM、**⛔ 0** 读 `〔归档区〕` 正文、**⛔ 0** 移动／重命名／删除任何件、**⛔ 0** 新建目录、**⛔ 0** 回改任何既有件一字；**仅新增本件 1 件**（新件落盘前 `Test-Path`／`os.path.exists` 双核其不存在）。

### §5-9 落盘自证（六项 · 字节层）

| 项 | 值 |
|:--|:--|
| BOM（`EF BB BF`） | **0** |
| CR（`\r`） | **0** |
| VT（`\x0B`） | **0** |
| U+FFFD（解码替换符） | **0** |
| 末字节 | **0x0A** |
| 非 ASCII 字节数 | **9463** |
| LF（`\n`）计数 | **292** |
| 编码 | UTF-8（无 BOM）· 纯 LF |

> 📌 **本件终态指纹（BYTES／SHA-12／SHA-256）由落盘后实测给出，载于派工回报面**——本节不嵌自身哈希（自指悖论，遵本仓既有登记体例：指纹外置于回报面，节内不填）。

### §5-10 0 触动自证

- **写前基线**：`results\evidence\register` 目录文件数 **361**（`Get-ChildItem` 实测）；正控 `tools\exp_harness.py`＝**45,590 B／SHA-256 `ce64b9b97489…`**（本棒实测一次，与派工单所载正控相符）。
- **写后**：目录文件数 **362**；**新增者仅本件 1 件**；**既有 361 件之文件名／大小／修改时间戳无一变动**（逐件前后快照对比，差异条目 0）。
- **本棒 0 修改既有件一字**（append-only 之单向新增面）。

### §5-11 key 形态自扫（落盘后 · 本件全文）

- 扫描式（词边界）：`\bsk-[A-Za-z0-9_\-]{8,}`、`\btp-[A-Za-z0-9_\-]{8,}`、`\bark-[A-Za-z0-9_\-]{8,}`、`\bAPI_KEY\s*=`、`\bAuthorization\s*:\s*Bearer\b`、`\bSECRET\s*=`、`\bTOKEN\s*=`。
- 扫描对象：本件全文字节。**命中 0** ⇒ CLEAN。

---

## §6 留痕与边界

- **本棒产出**：本件（`results\evidence\register\_nist_sp811_fulltext_retrieval_2026_10_25.md`）——**唯一新增件**。
- **本棒 0 产出**：判定件、校准件、任何对辨明件／B 级件之回改或升格。
- **候读面**：§4-1 之「`round` 无此词」与 §4-2／§4-3 之逐字换算，可供 PI 与判读面取用；**其是否升格 B 级、由谁裁，本棒 ⛔ 0 代裁**。

---

## §7 勘误（落盘后自审追加 · append-only · ⛔ 0 回改上文任何一行）

> 📌 本节为**落盘后自审**所出之勘误：上文 §2-2／§4-1-1／§4-1-2／§5-2 段／§5-7 段／§5-10 段**一字未改**，仅在此**追加**更正（遵本仓 append-only 勘误体例）。上段原文**照录留存**，其与本节冲突处**以本节为准**。

### §7-1 勘误一：写前基线之件数（§5-10 段）

- 上文 §5-10 段载「写前基线 **361**／写后 **362**」——**此二数为两次不同基线读取之混用，本棒自审即予更正**。
- **本棒落盘脚本内、写入前瞬间之目录快照实为 362 件**；写入后 **363 件**；`ADDED`＝**仅本件 1 件**；`REMOVED`＝**空**；`CHANGED_COUNT`＝**0**。
- 361 与 362 之差 ＝ **他棒并发落盘**：`_mirror_count_discrepancy_check_2026_10_25.md`（22,510 B·01:31:32）落于本棒「早读基线」（01:27:07）与「落盘脚本基线」之间。
- **⇒ 0 触动之结论不变**：既有件**文件名／大小／修改时间戳逐件无变动**（差异条目 0）；本棒新增者**仅本件 1 件**。

### §7-2 勘误二：HTML 核面之页数（§2-2 段末、§4-1-1 表末行）

- 上文作「`\bround\b` 于**全 18 页皆 0**」——**措辞过宽，本棒自审即予收紧**。
- **实况**：HTML 分章面 **18 个 URL 中取到 15 页**（`preface`／`check-list-reviewing-manuscripts`／`chapter-1-introduction` 三页取页中断，见 §5-1 段）；`\bround\b` 于**所取 15 页皆 0**；**另 3 页未取到、未核**。
- ⇒ 「HTML 侧交叉核对」之覆盖面为 **15 页**（非 18 页）。此缺口**未**影响 §4 之逐字引（逐字引全部出自官方 PDF 全本）。

### §7-3 勘误三：PDF 27 处与 HTML 22 处之差额成因（§2-2 段末）

- 上文作「因 HTML 版**表格折叠**」——**此因由经复核不成立，本棒自审即予更正**。
- **实况（逐处归并）**：PDF 全本 27 处 ＝ HTML `appendix-b` 页之 **22 处** ＋ 目录页（PDF 物理页 11／罗马页 ix）之 **3 处** ＋ §1.2（PDF 物理页 13／印刷页 1）之 **2 处**。
- ⇒ 差额 **5 处** 之成因 ＝ **目录页无对应 HTML 分章页**（3 处）＋ **§1.2 所在 `chapter-1-introduction` 取页中断**（2 处）；**与「表格折叠」无关**。
- 逐字可核之两端：**PDF 侧 27 处之分布**＝物理页 11(3)／13(2)／52(1)／53(1)／55(15)／56(5)；**HTML 侧 22 处**之全量皆在 Appendix B 页。

### §7-4 勘误四：两处引文之节名归属（§4-1-2 段内第 3、4 两个 bullet）

- **物理页 52（印刷页 40）**之引文 `A factor in boldface is exact. All other factors have been rounded to the significant digits given in accordance with accepted practice (see Secs. 7.9, B.7.2, and Refs. [4: ISO 31-0] and [6]).` —— 上文归属作「§**B.4** Organization of entries and style」，**归属有误**：该页实含 `Appendix B. Conversion Factors`／`B.1 Introduction`／`B.2 Notation`／`B.3` 之起首，而该句**属 §B.2 Notation 之末**。**正确归属＝§B.2**（印刷页 40／物理页 52，页码不变）。
- **物理页 53（印刷页 41）**之引文 `1. Guidance on rounding converted numerical values of quantities is given in Sec. B.7.2.` —— 上文归属作「**B.8 表注 1**」，**归属有误**：该组 Notes 位于 `B.3 Use of conversion factors` 之末（其下即接 `B.4` 之标题），**属 §B.3 之 Notes**。**正确归属＝§B.3 之 Notes**（印刷页 41／物理页 53，页码不变）。
- **引文文字本身经复核逐字无误**，**仅归属标签更正**；两句之「舍入」义**未变**。

### §7-5 勘误五：印刷页与物理页对照之正述（§5-7 段括注）

- 上文括注之列次错乱，本棒自审即予正述。
- **正述**：**印刷页 ＝ PDF 物理页 − 12**（正文起于物理页 13 ＝ 印刷页 1；前置封面／题名页／版权页／罗马数字目录页不计入正文页码）。此换算系**逐页读取页眉数字实测**所得，**非按偏移推算**。
- **实测对照（物理页 → 印刷页）**：13→1、20→8、27→15、35→23、51→39、52→40、53→41、55→43、56→44、60→48、63→51、66→54、79→67。
- **附录节首实测**：§B.1／B.2／B.3 起于物理页 52（印刷页 40）；§B.4 起于物理页 53（印刷页 41）；§B.5／B.6 起于物理页 54（印刷页 42）；§B.7／B.7.1／B.7.2 起于物理页 55（印刷页 43）；§B.8 起于物理页 57（印刷页 45）；§B.9 起于物理页 69（印刷页 57）。

### §7-6 本勘误节之自证

- 追加方式：**append-only**（以二进制追加模式写入原文之后）；**上文历史行 0 修改**。
- 本节落盘后，本件终态之 **BYTES／SHA-12／SHA-256** 与**字节六项自证**（BOM／CR／VT／U+FFFD／末字节／非 ASCII 计数／LF 计数）**以外置实测报于派工回报面**（遵本仓「指纹外置于回报面·节内不填自哈希」之体例）。
- 本件**仍为唯一新增件**；既有件 **0 改动**（他棒并发落盘之件**非本棒所为**，§7-1 段已逐条区分）。
