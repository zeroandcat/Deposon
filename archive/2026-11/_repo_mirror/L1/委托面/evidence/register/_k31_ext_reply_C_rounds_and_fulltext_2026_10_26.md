# 外委回件 · C（第三批·事 1 `rounds` 换算之证伪 ／ 事 2 `V5`·`V6` 全文）

> 📌 **来源**：外委会话 `mvs_cd51c4b0cb2a49379acb0e71e629feea`（模型 `k3.1-pro`）· 其 turn `turn_59167ba4-…` · 其自报任务号 `DEPOSON-EXT-20261026-03`
> 📌 **取得**：2026-10-26 22:4x 由主代理（mavis）自该会话记录 `messages.jsonl`（**2,853,661 B／SHA-12 `4785d53074de`**）取出，只取正文（滤 thinking 与工具回执）
> 📌 **本件之界**：正文**原样照录**，未删改一词；**仅前置本头**。
> 📌 **未完成之一事**：其自报「事 3（八字段映射、单位精度与缺值惯例）」**本轮未交**，自陈「下一轮给」——故本件只含事 1、事 2。
> 📌 **性质**：外委回件——⛔0 视为五终判之词、⛔0 视为 PI 之采认；个案适用与最终判定仍归 PI。
> 📌 **正文实测**：6,927 B

---

<PROGRESS>
任务:DEPOSON-EXT-20261026-03 场景:通用·换算证伪／全文 retrieve／字段惯例 进度:3% 当前:在册缺口与文献标识定位(1/6)
待办:[核 rounds 定义与单位总表；查 V5/V6 全文或受限证据；核八字段惯例；分级整合] 状态:进行中
</PROGRESS>
本批预计超过 5 轮，按四模块推进：A 换算证伪、B 全文 retrieve、C 八字段惯例、D 分级回件。先定位在册的准确题名与缺口，外部检索不预设 `round` 可换算。

两处实况须先校正：指定 `_z4_37needpi...` 路径不存在；另一补件实测为 **19,243 B／`1a9fe7b85a67`**，不是 14,362 B。先按文件名定位并读取最新件，后续不沿用旧体积作证据。

在册已确认两点：SP 811 只能证明其体系内无 `round` 词条，不能外推一切文献；八字段是既有“最低证据链”方案，不应先验冒充行业标准。现在定位 V5／V6 的准确题名再取全文。

V5／V6 已定位为 Halpern–Pearl 的因果论文与 JCGM VIM 第三版，均有公开全文候选。下一步同时取全文，并查“轮次是程序步还是物理时间量”的独立定义。

两件全文均有公开渠道：V5 为 arXiv v3，V6 为 BIPM/JCGM 官方 PDF。字段侧我改查测量与临床数据类型标准，重点看“必填项、精度、缺值原因”，不拼出伪统一八项。

全文核验完成：V5 为 42 页、V6 为 108 页且含“2008 version with minor corrections”。我再补一轮 SI 第九版与数据类型条款，避免把 SP 811 的单点零命中误当成跨体系结论。

目前证据更支持“`round` 是程序性计数，不是通用时间单位”，但仍只限所核文献。字段方面已取得缺值惯例：FHIR 用 `dataAbsentReason`，openEHR 用 null marker／叙述，而非默认填值。

字段精度也已核实：openEHR 要求 `magnitude` 与 `units`，`precision` 是小数位定义且可缺省；未知准确度须显式标未知，不可当作零误差。SP330 的 guessed URL 不成立，我改从 DOI 落地页核正身，不重试该地址。

检索射程已扩到三套一手文本：SP 811、SP 330 第九版、VIM。三者均无 `round` 时间单位词条；接着只取表号和定义锚，随后分两轮回件，先换算与全文，再字段。

<PROGRESS>
任务:DEPOSON-EXT-20261026-03 场景:通用·换算证伪／全文 retrieve／字段惯例 进度:72% 当前:三事证据齐合与分级回件(5/6)
待办:[先交付 rounds 与 V5/V6；再交付八字段映射及检索射程] 状态:进行中
</PROGRESS>
三事证据已齐。按篇幅拆两轮：本轮先给换算与全文，下一轮给八字段；每条分别标 A／B／C，不把推断升格。

<PROGRESS>
任务:DEPOSON-EXT-20261026-03 场景:通用·换算证伪／全文 retrieve／字段惯例 进度:72% 当前:事1、事2回件(5/6)
待办:[事3 八字段映射、单位精度与缺值惯例] 状态:进行中
</PROGRESS>

## 事1｜`rounds` 与时间单位的换算

**结论（C级·限所核文献）：未发现有通用常数可使 `1 round = x seconds`。现有证据更支持 `round` 是程序性计数，而非通用物理时间单位；但具体模型仍可自行规定每轮时长，不能反过来说一切 `rounds` 永不可换算。**

直接证据：

- **B级｜SP 811 登记件逐字转引：**90 页全文中 `\bround\b` 为 0；27 处 `round*` 全是 `rounding/rounded`（数值修约）。`revolution` 的换算落角度而非时间。见登记件 §4-1-1／L109–116、§4-1-2／L120–149、§4-1-3／L151–165。其射程仅是 SP 811 内。
- **A级｜NIST SP 330, 2019：**Table 8 的时间项只列 `minute/hour/day`，没有 `round`。全 138 页中 `\bround\b` 与 `\bround\w*` 均为 0。见 *The International System of Units (SI)*，DOI [10.6028/NIST.SP.330-2019](https://doi.org/10.6028/NIST.SP.330-2019)，PDF p.41（印刷页25），Table 8。
- **A级｜JCGM VIM 第三版：**108 页中 `\bround\b` 为 0；`round*` 仅 p.54 的 `rounded`，并非轮次。VIM 1.8 把实体计数列为无量纲量，1.9 则要求同类量才能借单位作比值。见 *International Vocabulary of Metrology – Basic and general concepts and associated terms (VIM), 3rd edition*，DOI [10.59161/JCGM200-2012](https://doi.org/10.59161/JCGM200-2012)，PDF p.22（印刷页6）§1.8–1.9。
- **A级｜程序步定义：**Fox–Tishby 以 `W_1,…,W_n` 的离散时间随机过程及逐步 `t` 定义模型，并未给每步配置物理时长。见 *Bounded Planning in Passive POMDPs*，DOI [10.48550/arXiv.1206.6405](https://arxiv.org/abs/1206.6405)，会议页75，§1.1。Gymnasium 的 [`Env.step`](https://gymnasium.farama.org/api/env/#gymnasium.Env.step)  likewise 是“执行一次环境动力学更新”，不是固定秒数。

**可机械执行的换算边界（C级）：**只有当模型另给每轮起讫或时长 \(\tau_j\)（含单位）时，才可计算 \(T=\sum_j\tau_j\) 或 \(t^{end}_j-t^{start}_j\)。只有 `rounds` 字面、没有该映射时，只能记“换算输入未获得”，不能默认每轮等时，更不能借用 `day/hour` 的系数。

**射程记录：**本轮实取时点为 **2026-10-26 22:10（GMT+0800）**；覆盖 SP 811（登记件90页）、SP 330（138页）、VIM（108页）、Fox–Tishby（8页）及 Gymnasium 官方文档。检索形为 `\bround\b`、`\bround\w*`；同时以 `day/hour/minute` 表和 VIM 的 `rounded` 作正控，排除“扫描器无命中即无此义”的错误读法。

## 事2｜V5／V6 全文

两件均已取得公开全文，**不存在需要以“不可公开取得”结案的情形**：

- **A级｜V5 全文：**Halpern & Pearl, *Causes and Explanations: A Structural-Model Approach. Part I: Causes*，arXiv v3（2005-11-07），42页。全文：[arXiv PDF](https://arxiv.org/pdf/cs/0011012v3)；DOI [10.48550/arXiv.cs/0011012](https://doi.org/10.48550/arXiv.cs/0011012)。实测 SHA-256：`73207c0e41866b44f6bafbcee54df9154ae08e3869568fd93343712b55e9e883`。
  **B级｜出版版本元数据：**British Journal for the Philosophy of Science 56(4):843–887，DOI [10.1093/bjps/axi147](https://doi.org/10.1093/bjps/axi147)。此处仅据 Crossref 元数据，不冒充出版方 PDF 已开卷。
- **A级｜V6 全文：**JCGM 200:2012, *International Vocabulary of Metrology – Basic and general concepts and associated terms (VIM)*，第三版、**2008 version with minor corrections**，BIPM 官方 PDF 共108页。DOI [10.59161/JCGM200-2012](https://doi.org/10.59161/JCGM200-2012)。实测 SHA-256：`8a603e99d236a65d771f38b6dcf627953146fe023a5266b3307681ada30f4fe7`。可直接用于 §1.8–1.9、§2.1、§2.15、§4.6–4.7 的逐字核。

<PROGRESS>
任务:DEPOSON-EXT-20261026-03 场景:通用·换算证伪／全文 retrieve／字段惯例 进度:76% 当前:事1、事2已交付(5/6)
待办:[事3 八字段映射、单位精度与缺值惯例] 状态:进行中
</PROGRESS>
