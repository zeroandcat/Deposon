# 外委回件 · E（第四批·事一 归因判据与登记面五口径 ／ 事二 交付包与回执形态 ／ 事三 OSF 同一性候选）

> 📌 **来源**：外委会话 `mvs_cd51c4b0cb2a49379acb0e71e629feea`（模型 `k3.1-pro`）· 任务号 `DEPOSON-EXT-20261026-04`·`turn_7b835cbd`
> 📌 **取得**：2026-10-26 23:5x–00:0x 由主代理（mavis）经**跨会话消息**收到；正文**原样照录**，仅前置本头
> 📌 **性质**：外委回件——⛔0 视为五终判之词、⛔0 视为 PI 之采认；其末自书「不判断你方任何位之词，不代为采认；最终权属仍归 PI」，本部**承此界**
> 📌 **本部未核**：其所述各标准条款、页码、检索式与正控，本部**未独立复核**；凡引须并书此限
> 📌 **与我方卡点之对应（本部速记·非其原文）**：事一之「登记面五口径」对应 `E-07` 之四候选（A≈甲登记面命中／B≈乙载荷件／C≈丙双层／E≈丁授权效力与正身分问）｜事一之「归因三层 L2」对应 `E-06` 之「归因面未解 vs 已辨明」｜事二对应 `项24` 之回执形态｜事三对应 `件-1` 之同一性

---

## 总结论

- **事一：无跨域统一的"归因已辨明／登记面"判据**；可以拆成可机械核的三层归因判据与五种登记面口径。
- **事二：无跨域统一的 closeout package／receipt 模板**；科研归档、软件交付、行政审批各有可援要件，不能互相冒充。
- **事三：有 3 条候选**，但没有一条在本轮公开射程内同时命中 `initial inventory`、`kv3s`、`_s4`、`readings`；**不得据此断言你方文件属于任何一条**。

以下 `C←A/B` 表示"我的综合／映射，支撑证据为 A／B"。

---

## 事一：`归因已辨明` 与 `登记面`

### 1. 归因：先分三层，不能把"有断言""原因辨明""CAPA 闭环"混为一谈

| 层级 | 可机械核的判据（C） | 与 `not yet determined` 的分界 | 级别与出处 |
|---|---|---|---|
| **L1：归因断言存在** | 能指出 `entity`、`agent` 及 `wasAttributedTo` 关系；若还要核"谁在陈述"，须有可归因的 bundle 及其 agent／生成时点。 | 无此关系即未达 L1；但**有断言不等于断言为真，更不等于根因已证**。 | C←A：W3C *PROV-DM* §2.1.3："Attribution is the ascribing of an entity to an agent"；§2.2.2：bundle 是 "a named set of provenance descriptions"，其自身亦为 entity。§2.1.2 另明说 PROV 不规定 derivation 在何种条件下成立。 |
| **L2：调查支持的原因结论** | 记录中可逐项核到：问题／结果边界、证据来源、因果因素（可为多个）、从因素到根本原因的理由链、结论及其不确定边界、调查活动与结果。 | 若记录仍写"原因未定／尚无证据支持的因素"，则未达 L2，当然构成该层"已辨明"的反面。若只是某个子问题未解，而主结论及其边界已满足预定判据，则不能机械把全部"未解"都等同于反面，须先核该"面"的预定完成条件。 | C←A+B：A＝21 CFR §820.100 (a)(1)–(2) 要求分析并调查原因，(b) 要求全部活动及结果记录；B＝DOE-NE-STD-1004-92, *Root Cause Analysis Guidance Document*, §1 Summary，要求识别问题、重要性、前因及其为何存在，并以"若纠正可防复发"的根本原因为分析终点。 |
| **L3：纠正措施闭环** | 已有措施、已实施并记录变更，且有有效性验证／确认及结果记录。 | 措施未验证不等于 L2 原因未辨；但若把"已辨明"当"CAPA 已闭合"，则未达 L3。 | C←A：同 CFR §820.100(a)(3)–(5)、(b)。 |

**是否必须"单一原因／有限集合／可重现／排除他因"？**
- **单一原因不是统一必要件**：CFR 原文用 `causes`、`action(s)`，并未限定唯一根因；有限候选集合可作为本地判据，但不能冒充统一要求（C←A）。
- **可重现也不是统一必要件**：所核 CFR 要求的是措施有效性的验证／确认，而非一律重现实验故障（C←A）。
- **排除或区分其他因素**是增强 L2 可辩护性的良好判据，但不是所核文本的统一字面要件；若采用，应写成"候选集合＋逐项证据＋残余不确定性"，不能伪造"已排除全部他因"（C）。

### 2. `登记面`：无统一所指，至少有五种可区分口径

| 候选口径 | 谁在陈述、登在何处 | 可机械核的生效要件 | 级别与出处 |
|---|---|---|---|
| **A. 登记条目为本** | 登记行为人／系统在登记册或业务系统中给记录一个条目。 | 条目存在、对象有唯一标识，并可核到条目所载发送者、动作、附件、分类号及承办机构等元数据。 | C←B：InterPARES, *Preservation of e-Protocol Registers*, PDF p.17–18。p.17 转引 ISO 15489："Registration: The act of giving a record a unique identifier on its entry into a system"；p.18 列 protocol register 字段。**这是转引，故为 B。** |
| **B. 载荷件为本** | 生产者提交实际文件／字节，载体是 `data/` 载荷。 | 文件及其字节存在；但"有载荷"不自动等于"已有登记条目"。完整与有效另核：BagIt 的 complete 要全部必需件及清单所列文件在场，valid 还须全部校验通过。 | C←A：RFC 8493, *The BagIt File Packaging Format (V1.0)*, DOI `10.17487/RFC8493`, §1.3、§2.1.2、§3。 |
| **C. 内容＋登记／包描述双层** | Producer 提供 Content Information，Archive 维护 PDI、Packaging Information 与 Package Descriptions；双方由 SIP／receipt 连接。 | 内容、PDI（Reference／Provenance／Context／Fixity／Access Rights）、包装及包描述均可回指；接收确认存在。OAIS 的确认可含错误重提请求，且**收到不当然等于验收或法律托管转移**。 | C←A：CCSDS 650.0-M-2, *OAIS*：Receive Submission, p.50／印刷 4-6；PDI §4.2.1.4.2, p.73–74；Packaging §4.2.1.4.3, p.76；Information Package §4.2.2.1, p.77。 |
| **D. 陈述／溯源面为本** | 某个 agent 对某个 entity 作归因陈述；陈述集合自身作为 bundle 再被归因。 | 能指出 entity、agent、bundle 及其生成时点／派生关系；这只证明"谁说了什么"，不自动证明官方登记、法律生效或陈述为真。 | C←A：W3C *PROV-DM* §2.1.3、§2.2.2。 |
| **E. 授权效力与正身为问** | 有法定职权的行政机关，以书面决定／专用印章／注明日期对外发生效力。 | 核决定主体是否有权、是否为书面、是否有印章与日期；准予／不予及证件类型是否一致；不能拿申请人自己的载荷件冒充行政机关的有效决定。 | C←A：中国〔高校R〕网《中华人民共和国行政许可法》第 32、38、39、56 条；第 8 条另涉已生效许可的保护。 |

---

## 事二：交付包／回执之形态惯例

**无跨域统一模板。** 最接近的可机械汇总（**C，非标准原文**）是六类：①包标识／版本；②实例与清单；③算法、校验值及验证结果；④来源、构建与依赖；⑤移交双方、时点、状态与异常；⑥验收准则、结果及授权签发人。各类是否必备，须回到具体域，不能把这六类冒充统一必填表。

### 1. 科研数据归档：OAIS＋BagIt
- **交付包（A）**：OAIS Information Package 含 Content Information 与 PDI，并可关联 Packaging Information、Package Descriptions。PDI 最小概念类为 Reference、Provenance、Context、Fixity、Access Rights；OAIS 明说这些类**不规定具体数据结构**。出处同上。
- **BagIt 必备（A）**：`bagit.txt`（`BagIt-Version`＋`Tag-File-Character-Encoding`）、`data/`、至少一个 `manifest-<algorithm>.txt`；每个载荷文件在清单中恰出现一次；清单行是 `checksum filepath`。有效包＝complete＋全部校验通过（RFC 8493 §2.1.1–2.1.3、§3）。
- **可选但鼓励（A）**：`bag-info.txt` 之 `Source-Organization`／`Contact-Name`／`Contact-Email`／`External-Description`／`Bagging-Date`／`External-Identifier`／`Bag-Size`／`Payload-Oxum`／`Bag-Group-Identifier`／`Bag-Count`／`Internal-Sender-Identifier/Description`；另有可选 `tagmanifest` 与 `fetch.txt`。⇒ **签发人、时点、包标识并非 BagIt 之必备回执字段**，只是可选元数据（§2.2.1–2.2.3）。
- **回执（A）**：OAIS Receive Submission 是 Archive 向 Producer 给出 SIP 的 `confirmation of receipt`，可含错误后的 resubmit 请求；"may represent a legal transfer of custody"是**可而非必然**。它**也没有统一规定回执抬头或签字人**（p.50）。

### 2. 软件交付：SPDX＋SLSA＋放行记录
- **包清单（A）**：SPDX v2.3.1 文档字段含 `SPDXVersion`／`DataLicense`／`SPDXID`／`DocumentName`／`DocumentNamespace`／`Creator`／`Created`；包字段含 `PackageName`／`SPDXID`／`PackageVersion`／`PackageSupplier`／`PackageOriginator`／`PackageDownloadLocation`／`PackageVerificationCode`／`PackageChecksum`／许可与外部引用等。⚠ `PackageVersion` 为 0..1，**非所有场景必填**；DocumentNamespace 若更新版本则须换 URI（Clause 6、7；按公开行业规范引用，**不把 v2.3.1 与 ISO/IEC 5962 版次混写**）。
- **构建与来源（A）**：SLSA v1.2 Build Provenance 以 `subject` 标识产物；`buildDefinition` 记 `buildType`／`externalParameters`／`resolvedDependencies`；`runDetails` 记 `builder.id`。`BuildMetadata.invocationId/startedOn/finishedOn` 在该节标为 `REQUIRED: (none)` ⇒ **可选而非普遍必填**（状态 Approved·**行业规范·非 ISO 强制标准**）。
- **验收／放行（B）**：GB/T 19001-2016 §8.6 要求保留放行成文信息，含"符合接收准则的证据"与"可追溯到授权放行人员的信息"；策划安排圆满完成前，除非获授权人员批准（适用时获顾客批准），否则不应放行。该条**不要求统一的人名签字形式或统一回执抬头**（镜像全文·故 B）。
- **C 级综合**：实际软件 closeout 可把"二进制／源包＋SPDX/SBOM＋SLSA 构建来源＋测试与验收记录＋校验清单＋授权放行信息"组成一包；此是组合方案，**非三者共同规定之统一包形**。

### 3. 行政审批：受理凭证与许可决定必须分开（A）
- **受理／不予受理回执**：《行政许可法》第 32 条要求出具"**加盖本行政机关专用印章和注明日期的书面凭证**"。直接法定要件是处理结果、专用印章、日期；该条**没有统一的申请人签名或校验值字段**。
- **准予许可**：第 38 条要求**书面决定**；不予许可亦须书面、说明理由、告知复议／诉讼权利。
- **证件与送达**：第 39 条列许可证／执照、资格／资质证、批准或证明文件等，须加盖行政机关印章；第 44 条规定决定后十日内颁发、送达。
- **登记事项**：第 56 条对材料齐全、符合法定形式的特定事项要求当场登记。

---

## 事三：OSF 预登记候选与同一性定位

### 1. 候选（只给候选与判据，**不判定你方文件归属**）

| 候选与级别 | 相关公开证据 | 注册时点（API 原样） | DOI／版本链 |
|---|---|---|---|
| **① `27nmp`：关键词覆盖最全** — *SR-D18: Inventory-norm sizing & excess-inventory decomposition for urban fresh / quick-commerce dark-stores — systematic review*（A） | Open-Ended Registration；元数据含 `(s,S)`、safety stock、reorder point、base-stock；附件 `extraction.csv` 含 `system dynamics` 1 处、`bullwhip` 6 处。**未命中** `initial inventory`、`kv3s`、`_s4`、`readings` | `2026-07-08T18:14:02.631860` | DOI `10.17605/OSF.IO/27NMP`；`schema_responses` 仅 1 件（original＝latest）；`ia_url` `...27nmp-v1`；**未见独立 Update 节点**；其 `date_modified=2026-07-11T05:05:50` ⇒ **不能写成"从未修改"** |
| **② `89qfe`：题名与模型主题最直接** — *INFORMATION LATENCY, SIGNAL RELIABILITY, AND THE BULLWHIP EFFECT: A GENERALIZED LATENCY-ADJUSTED ORDER-UP-TO FRAMEWORK*（A） | OSF Preregistration；题名／描述直接命中 bullwhip、order-up-to；附件 PDF 16 页中 bullwhip 34 处、order-up-to 11 处、base-stock 1 处。`initial inventory`／`(s,S)`／`system dynamics`／`kv3s`／`_s4`／`readings` **均 0** | `2026-08-29T07:00:40.083687` | DOI `10.17605/OSF.IO/89QFE`；仅 1 件 schema_response；`ia_url` `...89qfe-v1`；未见独立 Update；`date_modified=2026-09-01T05:09:19` |
| **③ `s5vc2`：弱一档候选** — *Artificial Intelligence and Big Data in Inventory Management for E-commerce: A Systematic Review (2021-2026)*（A） | Generalized Systematic Review Registration；元数据含 `(s,S)`；DOCX 含 bullwhip 2 处、XLSX 5 处；**未命中** `system dynamics`／`initial inventory`／`kv3s`／`_s4`／`readings` | `2026-06-19T03:18:56.352014` | DOI `10.17605/OSF.IO/S5VC2`；仅 1 件；`ia_url` `...s5vc2-v1`；未见独立 Update；`date_modified=2026-06-21T05:07:14` |

**候选排序是 C 级关键词覆盖排序，不是归属判断。** 三条的公开附件均未发现 exact `initial inventory` 或所给文件名组成词；亦未见 `_s4_kv3s_4_123_readings_<日期>.json` 同名公开附件。

### 2. 检索式、射程、零命中与正控
**时间窗**：2026-10-26 23:20–23:52（+08:00）。
**OSF API v2（A）**：
- `filter[title]`：`bullwhip`→1（`89qfe`）；`order-up-to`→1（同）；`system dynamics`→9；`inventory`→216（**216 条公开 attributes 已逐页扫描**）；`base-stock`→0；`initial inventory`→0；`(s,S)`→0；`inventory policy`→0；`kv3s`→0。扩检：`supply chain`→69；`stock`→139（仅首 100，**未用于否定**）；`latency`→38（仅题名扩检，未用于否定）。
- `filter[description]`：`bullwhip`→1；`initial inventory`／`(s,S)`／`kv3s` 均 0。⚠ **description 过滤不覆盖附件全文**，故另做附件扫描。
- `identifiers/` 实取三条 DOI；`schema_responses/` 实取版本链；`files/` 递归只读公开目录。
**附件全文（A）**：`89qfe` 16 页 PDF 全文检索｜`27nmp` 之 `protocol.md`／`draft.md`／`screening.md`／`synthesis.md`／`appraisal.md`／`extraction.csv`／`RESUME.md` 全部检索｜`s5vc2` 之 DOCX／PDF／2 XLSX 全部检索（XLSX 以压缩包内 sharedStrings／worksheets 文本为射程）。三者所有附件中 `initial inventory`／`kv3s`／`_s4`／`readings` **均 0**。**此结论只限这些候选及已解析公开附件，不外推为 OSF 全库无此物。**
**网页补检（B）**：六式（含 `site:osf.io "kv3s"`、`"_s4_kv3s_4_123_readings"`）；结果有子串误中，均未提供更强同族候选；**检索引擎之分词与子串命中不当作 exact 证据**。
**正控**：同一 API 方法对已知存在之 `89qfe` 以 `bullwhip`／`order-up-to` 均命中；`system dynamics` 9、`inventory` 216。PDF 正控：`89qfe` bullwhip 34 处、`27nmp` 6 处、`s5vc2` DOCX 2／XLSX 5。⇒ 相关零命中**非伪零**。
**访问与版本边界**：FDA 端点反爬、eCFR API 对指定日期无匹配 ⇒ CFR 采 Cornell LII 全文镜像；MoReq2 与 NAA 部分页面失败 ⇒ **未冒充已开卷 A 级**；OAIS／ISO 版本更新检索两次工具失败 ⇒ **只声称所引版本已核，不声称最新**。

---

以上均为外部判据、候选与检索证据，不判断你方任何位之词，不代为采认；最终权属仍归 PI。
