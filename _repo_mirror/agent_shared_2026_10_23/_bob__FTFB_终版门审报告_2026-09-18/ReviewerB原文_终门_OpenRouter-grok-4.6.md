# Reviewer B 终门评审原文（arXiv 上传前最后一关）

- 通路代号：OpenRouter
- 模型：x-ai/grok-4.6
- 会话：单轮独立会话（不与 Reviewer A 共享任何上下文）
- 框架：沿 R2 增强评审框架；唯一框架性调整＝上传定位口径（实名上传，双盲维改为 anon 自洽＋token 零泄漏），已在提示词显式声明
- 请求参数：temperature=0.4, max_tokens=16000, attempt=2, 耗时291.6s
- token 用量：prompt=59991, completion=17509
- finish_reason=stop

---

# 上传前终门结果与可复算性审计报告（审稿人 B）

材料范围：PAPER_MD / PAPER_TEX / COMPILE_CV / METADATA / REVISION_NOTES。本轮定位＝arXiv 实名上传（作者实名、致谢、公开指针不构成问题）。证据分层：渲染层（METADATA 摘要与正文口径）／源层（TEX）／构建记录层（CV）。

---

## 1. 总表

| 维度 | 判定 | 🔴Major | 🟡Minor |
|---|---|---|---|
| 维度一【结果】 | PASS | 0 | 1 |
| 维度二【讨论】 | PASS | 0 | 0 |
| 维度三【局限】 | PASS | 0 | 1 |
| 维度四【五锚不变式】 | PASS | 0 | 0 |
| 维度五【可复现性与上传定位合规】 | PASS | 0 | 2 |
| **总体** | **PASS** | **0** | **4** |

阻断级：0。P0 残留：0。

---

## 2. 逐维详审

### 维度一【结果】

**【结论】** PASS

**【定位与证据】**

守恒与容差（L239 / T335）：

> The conservation identity survives audit: the maximum per-path deviation across all variants and benchmarks is 2.220446049250313×10⁻¹⁶ — the scale of double-precision machine epsilon, against an implementation tolerance of 10⁻⁶ — closed (pre-registered) (results/anon_benchmark_v1_4_gsm8k.json · physics_audit.t_plus_r_plus_a_max_deviation).

构造恒等式（L235 / T331）：

> traversing reasoning paths undergo three-channel scattering obeying the constructive identity T+R+A=1 for arbitrary parameters

ECR 与缺失披露（L239 / T335）：

> median ECR = 4/3 over the 17 finite-valued graphs, with coverage of 20 of 22 graphs — three graphs read Infinity, two graphs lack arm data, both disclosed as-is (frozen handoff artifact, field headline_results.GT4_ECR)

判死线与三项否证（L239 / T335）：

> all three formalized dynamical-equivalence propositions are falsified — P1a: maximum deviation 0.8569, an O(1) gap that does not vanish with step size; T-P1b: minimum directional cosine −1.0; T-P1c: killed on both lines, with an 81-point grid over τ∈[0,4] reaching minimum cosine −1.0 at the best global τ and per-state optimal τ∗ again reaching −1.0, the per-state τ∗ median being 0

枚举范围（L239 / T335）：

> 61 graphs in five families … all 6,760 states of the 338-task corpus, 20 steps each — frozen handoff artifact, field headline_results.enumeration_scope

滤波对照与 McNemar（L247 / T343）：

> on GSM8K the filter scores 0.87 against the layer's 0.85 (McNemar p=0.5), on StrategyQA 0.899 against 0.899 (p=1.0) — and at these sample sizes the detectable-difference threshold is roughly ±10 percentage points, so smaller increments are not excluded

负面结果（L247 / T343）：

> Plain chain-of-thought significantly outperforms the layer on GSM8K, 0.97 versus 0.85 … Fusion with a semantic prior dilutes rather than helps: physics 0.484→0.452 and historical 0.783→0.739

§4 公式口径（L134 / T214）：

> the same functional form — H = -Σ p·log p — up to a positive multiplicative constant (Boltzmann's k, with its physical units) and the choice of logarithm base

**【分析】**  
§7.1 数字在 MD/TEX 逐项同文；守恒偏差与双精度 ε 同量级、相对 10⁻⁶ 容差闭合，与预登记“closed”口径一致。动力学三命题均被否证，ECR 的 Infinity／缺臂、滤波无差、融合稀释均原文披露，未把负面结果改写成正面。§4 将“same one”收窄为“same functional form … up to exactly those factors”，与 Channel III 的 isomorphism 保留用法一致。实验真值本身需冻结仓库外部核验（论文已把 M4 第三方复算降为 standing demand）；材料内可证的是口径自洽与字段路径闭合，不是数据现场重跑。

🟡Minor（措辞张力，非数值矛盾）：L243「an independent rerun passed with bit-identical recomputation」与 L239「to date no independent party has executed the recomputation」并置；后文「re-kept by a second pair of hands」表明前者为内部第二操作者。不构成推翻，但“independent”一词易被读成第三方。

---

### 维度二【讨论】

**【结论】** PASS

**【定位与证据】**

Master table 分档（L297 / T400）：

> Pipeline instance (§7) | Provisional pass (author-attested freeze; pre-registered tier — §7.4) | Out of scope (no indispensability claim) | Pass

§7.4 与表一致（L253 / T349）：

> The instance is therefore scored T as a provisional pass — the anchor is author-attested, of lesser independence than the historical rows, and not yet backed by a trusted time-stamp, a third-party archive, or any independent submission-time proof; the upgrade path is named, not executed — and R as a pass, on the pre-registered tier, with D out of scope

反向通道不主张（L257 / T353）：

> This section is an open-question agenda. It is not an empirical claim, and it makes no prediction

方法主张收窄（L225 / T321）：

> demonstrated on one artifact on the given benchmarks at the stated statistical power (§7.3), not as a general working methodology

映射强度（L200 / T294）：

> The table claims a constructed structural parallel — row-wise pairing of criteria with shared failure modes — and nothing stronger; the word isomorphism is reserved in this paper for the formula-level identity of Channel III

**【分析】**  
§5／§7.2–§7.4／§9.1 的导出与表内分档一致：历史通道供给级、D 四处置词典与各行一一对应；§7 为 Provisional pass 而非 Pass；§8 三格 Not applicable。未把 mid-strength 实例抬到非欧量级，未宣称反向通道已打开，未把 M1–M5 写成等价定理。讨论未超出证据范围。

---

### 维度三【局限】

**【结论】** PASS

**【定位与证据】**

§9.2（L306 / T412）：

> Selection effect: the four channels are visible because their cases left anchors … Scale: each channel carries a small number of flagship cases, and the pipeline has one engineering-grade instance; no prevalence claim is made anywhere in this paper. Magnitude: structural parallel to the non-Euclidean pattern does not make the engineering instance comparable to it in scale … Tiers: the historical tier and the pre-registered tier are different instruments … the reference pool is closed at fifty-six items … novelty statements rest on the three-line search recorded in §1.3(iv) — a single-engine, non-systematic retrieval record … with the second-round check scheduled before submission.

自披露另见：R13/R14 `[IDENTIFIER-PENDING]`（L332–L333）；R56 author-attested（L60／L396）；[R36] 无直引（L184）；M4 第三方复算未执行（L239）。

**【分析】**  
选择效应、规模、量级、双层证据、闭池、单引擎检索均明文。应披露项（pending 标识符、自证条目、保密渠道仅为 offered、冻结为 author-attested）均已披露。诚实性充分。

🟡Minor：§1.3(iv)／§9.2 仍写 “A second-round novelty check is scheduled before submission, and those statements carry that gate.” 本包已是 arXiv 提交版；若“submission”仅指期刊投稿则自洽，若涵盖本上传则门未闭。不推翻“相对三线检索”的主限定。

---

### 维度四【五锚不变式】

**【结论】** PASS

**【定位与证据】**

印刷点（L237 / T333）——五前缀各出现一次：

> GT_FORMALIZATION_v1.md aeefb8ef6972; run_v21_gtformal.py 9bbe43f41fa8; run_v22_p1c.py 6e9673205dc0; SPEC_GT2B.md 68a5b08ef007; SPEC_GT8C.md 6b09de9911c0 (frozen handoff artifact, field preregistration_anchors_sha256_12)

构建记录（C31）：

> Five frozen hash anchors, each exactly once      : PASS (all on p16)

冻结地位（L253 / T349；摘要 L13 / T81 / M12）：

> this is an author-attested freeze … scored T as a provisional pass
> the instance's temporal anchor is an author-attested freeze, recorded as provisional (§7.4).

**【分析】**  
五枚 SHA-12 在 MD 仅 L237、在 TEX 仅 T333 各印一次；后文只称 “the five anchors above”／“five printed anchor prefixes”，不重印前缀。与 CV「各恰好一次、均在 p16」互证。Provisional／author-attested 口径在摘要、§7.4、§9.1 三处同向，未把内部冻结写成独立时间戳或第三方档案。

---

### 维度五【可复现性与上传定位合规】

**【结论】** PASS

**【定位与证据】**

anon 范围声明（L229 / T325）：

> The anonymization covers the project's name, the name of its fictitious entity, and the project-name tokens inside artifact basenames (replaced below by the marker "anon") … The token "GT" that remains inside some artifact basenames below is the field-generic abbreviation of "ground truth," not a project-name token

落版路径确用 `anon_` 与 `GT_`／`gtformal`（L239 / T335），与声明相符。

offered 非 provided（L239 / T335）：

> are offered to the editors and reviewers through a confidential channel … is not claimed to have occurred, and to date no independent party has executed the recomputation.

池闭合（L60 / T136；L316 / T422）：

> The reference pool is closed: fifty-six items, cited by pool number [R01]–[R56]

实名上传（T67 / M4；C37）：

> \author{Qihao Yuan}
> Author      : Qihao Yuan
> \author{Qihao Yuan}, \date{2026-09-18}; PDF /Author="Qihao Yuan" (by design)

卫生（C36–C42）：

> Workflow/identity tokens (internal list, not reproduced): 0 hits
> CJK characters in PDF text layer                 : 0
> E-mail addresses in source or PDF                : 0
> Hygiene scan result                              : PASS

**【分析】**  
(i) §7 自称匿名化范围（项目名／虚构实体名／基名中的项目名 token→`anon`；GT＝ground truth）与落版一致，未改五锚、数字、field-path。(ii) TEX/CV/METADATA 未见评审模型／平台／内部昵称／本地路径泄漏；GLM 仅出现在 AI 披露句（L312），属作者声明的起草模型。实名作者块按本轮定位不构成问题。R56 仍标 double-blind／camera-ready，与 TEX 注释 “anonymized companion-study entry kept as-is until camera-ready restoration”（T64–T65）自洽。

🟡Minor-1：正文仍称 “blind-review version”（L223／L239），而本包是 named arXiv preprint（T63）。匿名化机制未破，但版本标签与上传定位不完全同名。  
🟡Minor-2：TEX 源注释残留排版工单号 `F4`/`F7`/`F8`/`F10`（T27、T42、T47、T56）；CV C4 含 `chain-head manuscript`。非评审模型代号，属源层痕迹。

---

### 法证总表（材料内可复算项）

| 检查项 | 声明值 | 实测值 | 判定 | 证据与方法 |
|---|---|---|---|---|
| 五锚 SHA-12 各出现次数 | 各恰好 1 次（N169；C31） | MD：仅 L237 各 1；TEX：仅 T333 各 1；CV：p16 各 1 | PASS | 材料内可证：全文检索五前缀 `aeefb8ef6972` `9bbe43f41fa8` `6e9673205dc0` `68a5b08ef007` `6b09de9911c0` |
| 五锚上下文 | 冻结裁决函数印刷前缀，author-attested | P 段印刷；§7.4/§9.1 Provisional | PASS | 材料内可证 |
| 池号闭合 [R01]–[R56] | 56 entries | 题录分组 15+14+10+2+4+7+2+2＝56；CV C32–C33「56 / Unique Rnn. labels: 56」 | PASS | 材料内可证（计数）；条目是否均一手核验需外部核验 |
| 53+1+2 算术 | 53 verified + R56 attested + R13/R14 pending ＝56 | 53+1+2＝56 | PASS | 材料内可证 |
| fifty-six 三处 | §1.3 / §9.2 / References | L60、L306、L316（TEX T136、T412、T422）均为 fifty-six | PASS | 材料内可证 |
| 摘要字符 1849 三处互证 | 1849 chars / 266 words；byte-identical（M16–M19；N193） | MD L13 ＝ TEX T81 ＝ METADATA M12 正文一致；N193 分句 375+52+440+549+117+312＝**1845**≠1849 | GRAY（正文三处一致 PASS；1849 vs 分句和差 4） | 材料内可证：三处逐字对照 PASS；精确字符数需脚本复算（本会话未跑计数器）；差 4 在修订说明算术，非三处正文互歧 |
| 主张句摘要≡§1.2 | 逐字一致（N163） | L13 首句 ≡ L27 ≡ T81 首句 ≡ T97 | PASS | 材料内可证 |
| 守恒偏差 | 2.220446049250313×10⁻¹⁶ vs 10⁻⁶ | MD L239＝TEX T335 | PASS | 材料内可证（口径）；真值需外部核验 |
| ECR | 4/3；17 finite；20 of 22 | 同文 | PASS | 材料内可证（口径） |
| 判死线数字 | 0.8569；−1.0；81-point；τ∈[0,4]；τ∗ median 0；0.669；6760；338；61 | MD＝TEX | PASS | 材料内可证（口径） |
| 滤波/McNemar | 0.87/0.85 p=0.5；0.899/0.899 p=1.0；±10；0.97 vs 0.85；0.484→0.452；0.783→0.739 | MD L247＝TEX T343 | PASS | 材料内可证（口径） |
| isomorphism 残留 | 仅 Channel III 公式用法 | §4 L130/L134 保留；§6.2 L200 声明 reserved；无 structurally isomorphic | PASS | 材料内可证 |
| provided→offered | offered，非 provided | 摘要 L13、§7.1 L239 均为 offered | PASS | 材料内可证 |
| METADATA Title | Fiction That Feeds Back: … | M3＝T66＝L9 | PASS | 材料内可证 |
| METADATA Author | Qihao Yuan | M4＝T67＝C37 | PASS | 材料内可证（实名上传，合规） |
| METADATA Subjects | cs.AI；physics.hist-ph；cs.CY | M6＝T73 | PASS | 材料内可证 |
| METADATA License | CC BY 4.0 | M8＝T73 | PASS | 材料内可证 |
| METADATA Comments | 24 pages, 2 tables, no figures | CV C10：24 pages；正文 2 表（M1–M5、master table）；无 figure 环境 | PASS | 材料内可证 |
| METADATA Date | 2026-09-18 | M1＝T68＝T73 | PASS | 材料内可证 |
| CV four-zero | errors/overfull/missing char/undef ref = 0 | C17–C20 均为 0；C50 ALL GATES PASS | PASS | 构建记录层；需外部核验日志原件，记录内自洽 |
| CV 源指纹 | tex SHA-256 `9de366a6…81f9`；PDF `cc155e19…e74d` | 本包 TEX 带 `Tn=` 前缀，无法对原字节复哈希 | 需外部核验 | 不能用带行号文本复算无前缀源哈希 |
| 工作流 token | 0 hits（C36） | TEX/METADATA 无评审模型／昵称／本地路径；GLM 仅 AI 披露；TEX 注释有 F4/F7/F8/F10；CV 有 chain-head | PASS（主项）＋源层痕迹见 Minor | 材料内可证 |
| CJK / email | 0 | C39–C41：0 | PASS | 构建记录层 |

---

## 3. R1+R2 合并清单 18 项逐项验收表

| 项号 | 验收结论 | 证据 |
|---|---|---|
| ① M10 自引占位→[R56] | 已落实 | L202/T296：「cited here as the anonymized pool entry [R56]: title, authors, and identifiers withheld for double-blind review… attested by the authors… rather than independently verified」；L279/T375：「companion study [R56]」；L60 池扩至 fifty-six；L395–L396 R55/R56 题录 |
| ② M4 行重写（import 声明） | 已落实 | L184/T268：「Row M4 is declared rather than smuggled in: the genre's distilled record contains no freeze-before-the-run demand, so M4's criterion is imported from the pre-registration… ([R47]–[R50])」；表行 L197/T288 左格「imported, not mapped」 |
| ③ structural isomorphism 降级 | 已落实 | L200/T294：「constructed structural parallel… the word isomorphism is reserved… for the formula-level identity of Channel III」；L225「structurally parallel」；L249「runs structurally parallel」；摘要 L13「constructed structural parallel」；全文无 structurally isomorphic |
| ④ §7 保密记录 offered 降格 | 已落实 | L239/T335：「are offered to the editors and reviewers」＋「not claimed to have occurred, and to date no independent party has executed the recomputation」＋「standing demand rather than an executed fact」；摘要 L13：「confidential channel offered to the editors」 |
| ⑤ Helmholtz R55 入池 | 已落实 | L68/T144 四段直引＋「[R55]」；L395/T524 题录 Gutenberg eBook no. 77725，retrieved 2026-09-17（引文对捕获件一致需外部核验） |
| ⑥ author-attested→Provisional pass | 已落实 | L253/T349：「scored T as a provisional pass」；L297/T400 表：「Provisional pass」；L237「printed here as twelve-character prefixes」（非 published） |
| ⑦ three-line search 协议公开 | 已落实 | L60/T136：「sixty-four query groups on a single commercial web-search engine — … twenty-three … fourteen … twenty-seven…」；L212、L306 回指 §1.3(iv) |
| ⑧ 熵公式 same functional form | 已落实 | L134/T214：「the same functional form — H = -Σ p·log p — up to a positive multiplicative constant… and the choice of logarithm base」；L144「sameness of functional form」 |
| ⑨ GT/anon 范围澄清 | 已落实 | L229/T325：「The token "GT" … is the field-generic abbreviation of "ground truth," not a project-name token」 |
| ⑩ F-C1–F-C4 Operational reading | 已落实 | L33–L36/T104–T107 四条均含 Operational reading；L310/T416「in substance unchanged from §1.2, operational readings included」 |
| ⑪ formal fiction 定义与 Riemann 口径 | 已落实 | L68/T144：「not adopted, and not coordinated, as the language of any physical theory at the time of its construction」＋「What its constructors intended and speculated is recorded, not erased」 |
| ⑫ [R36] 零直引＋标注 | 已落实 | L184/T268：「their framing is used here as paraphrase, not quotation — the anthology's full text was not captured… [R36] carries no direct quotation anywhere in this paper」 |
| ⑬ R13/R14 等维持 pending | 已落实 | L332–L333 `[IDENTIFIER-PENDING]`；L390–L391 R53/R54 保持捕获粒度；与「零补、宁缺毋滥」裁决一致 |
| ⑭ reads zero / working methodology 收窄 | 已落实 | L247/T343：「shows no detectable difference at the stated power」；L225/T321：「a worked method… not as a general working methodology」 |
| ⑮ R12 计数口径 | 已落实 | L60/T136 与 L316/T422：「Pool numbers count entries, not works — [R12] carries two primary texts under one entry」 |
| ⑯ 摘要与 §6.2 口径对齐 | 已落实 | 摘要 L13：「constructed structural parallel — criteria with shared failure modes, one row an import from the pre-registration literature, declared as such」；与 L200 主张句同向（R4 删 “row-wise pairing” 属字符削减，import 声明仍在） |
| ⑰ AI 披露如实重写 | 已落实 | L312/T418：「used for drafting and revision support under author instruction… retrieval, matching, and the entry-by-entry verification… ran with machine assistance… The authors directed all work… bear full responsibility」 |
| ⑱ 主张句摘要/§1.2 逐字一致 | 已落实 | L13 首句与 L27 斜体主张句逐字相同（止于 “we specify.”） |

18/18 已落实。无未落实项。

---

## 4. 修订引入新问题专项扫描

**（1）摘要削减后主张句与可证伪条件（对照 REVISION_NOTES 材料二）**  
句1 主张句零改动，与 §1.2 一致。三检验名称仍在主张句内。句5 保留 “The reverse channel is not asserted; an adjudication agenda states what would count as feedback and how it would die.” 句6 保留 offered／camera-ready／author-attested freeze／provisional（§7.4）。R4 压缩的是例证从句与重复限定（“row-wise pairing”“on the given benchmarks”“and reviewers”），未删可证伪条件。**未引入主张膨胀。**

**（2）R55/R56 入池后引用池闭合与计数口径**  
题录有 R55、R56；正文引用 R55（§2.1）、R56（§1.3／§6.2／§8.3）；闭池声明三处 fifty-six；53+1+2 算术闭合；CV 56 条。**池闭合 PASS。**

**（3）信息行落版（METADATA vs 论文）**  
Title／Author／Subjects／License／Date／Conflicts／Abstract 与 TEX 首页信息行（T73）及摘要环境一致。Comments「24 pages, 2 tables, no figures」与 CV 页数、正文表数一致。**落版 PASS。**

**（4）B01 修复后 TEX/CV 卫生**  
CV 为 neutralized edition，宣称 workflow token 0 hits、CJK 0、email 0。TEX 注释已英文化。残留：工单标签 F4/F7/F8/F10；CV「chain-head」。**主卫生 PASS，源层痕迹见 Minor，不构成阻断。**

---

## 5. 问题清单

### 阻断级
无。

### 🔴Major
无。元声明（闭池 56、D 词典、M4 import、Provisional pass、offered 非 provided、isomorphism 保留域、双层证据不混合）均被自身正文执行，未被推翻。

### 🟡Minor
1. **摘要字符声明算术** — N193 写 1849 且分句 375+52+440+549+117+312，加总为 1845。MD/TEX/METADATA 摘要正文三处一致。建议：用同一脚本对三处做字符计数，使「1849」与分句和一致（或更正分句表）。  
2. **“independent rerun” vs “no independent party”** — L243 vs L239。建议：将 L243 改为 `an internal second-operator rerun`（或等价），与 “second pair of hands” 对齐。  
3. **“second-round novelty check is scheduled before submission”** — L60／L306。本包已是 arXiv 提交。建议：或改为 journal-submission gate，或补一句已执行／仍待期刊投稿。  
4. **版本标签与上传定位** — L223／L239 仍写 blind-review version；T63 为 arXiv preprint edition。建议：把可用性句改为 `in this preprint, third-party executability remains an offer… public pointer deferred to camera-ready`，避免“盲审版”标签。源层 F4/F7/F8/F10 与 CV `chain-head` 可在不改正文的前提下从注释/记录剥离。

---

## 6. 终门判定

**判据复核：** P0 零残留（B01 主项已中性化；M10 已入 [R56]；M4 已声明 import；isomorphism 已降级；§7 已 offered／standing demand）。R2 全部 Major 已闭环或如实挂限（Provisional pass、第三方复算未执行）。无新增阻断级。18 项验收全部已落实。

**终判：PASS**（可上传；上列 🟡Minor 不阻断，建议在 v2 或 camera-ready 顺手清理）。

FAIL 整改清单：无。

---

## 7. 总体判定

**建议级：Accept**（就本 arXiv 实名上传终门而言；非期刊录用决定）

**总评分（10 分制）**  
- 原创性：8  
- 方法论：8  
- 结果与论证：8  
- 写作与一致性：8  

**总评：**  
这是一篇把“虚构作为可检验输入”做成可评分装置的立场论文：四通道、三检验、D 处置词典、双层证据、M1–M5（含一行公开 import）和四阶段流水线在文本层执行了自己宣布的协议；§7 把守恒通过、ECR 缺测、动力学三项杀死、滤波无差和融合稀释写在同一冻结口径下，并主动把 T 降为 Provisional pass、把 M4 第三方复算降为 standing demand。闭池 56、五锚各一、主张句摘要≡§1.2、offered≠provided、实名上传与 §7 anon 范围自洽，均在材料内可证。实验数字的真值与五锚全摘要无法在本包重跑（论文已如实写出），不与“审稿可复算／作者已披露限度”混同。残留均为文档算术、措辞歧义与盲审版标签，不推翻元声明。按本轮终门标准，**PASS，建议接受上传。**