# T5 第二轮五类缺口 · 阶②联网查文献件 · 2026-10-24

> **件性质**：**联网查文献件（阶② · 路二）**—— 就 PI 卡 `ask_ad8927c1e3ad5439ea33a9fd` 之 `q_gap_step2`（「**五类全查文献**」）所列**五类缺口**，出**阶②联网检索**之面。
> ⛔ **0 回改**任一既有件一字（append-only）｜⛔ **0 移动／重命名／删除**任一既有件｜⛔ **0 新建目录**（本件落于既有 `results\evidence\register\`）｜⛔ **0 跑实验**｜⛔ **0 调 LLM／API**｜⛔ **0 读** `〔本地路径已脱敏〕`｜⛔ **0 读归档区内容**（仅按名与指纹认人）｜⛔ **0 落**五终判／闭 KD／宣告段毕／门槛成就｜⛔ **0 代 PI 裁**。
> ✅ **联网范围**：**仅文献查证**——⛔ **0** 用联网取本案之 `correct`／`value` 原值或任何禁供面；本棒全部 23 式检索式**均不含**本案素材之字面记号（`correct`／`value`／格号／正解标签），⛔ 0 载任何禁供值。
> 📌 **本棒实际携带之 skill**：**0 个，未加载 skill 正文**（自测：`.minimax\skills\` 目录清单内**无**与本棒职司（联网文献查证）相关之专名 skill；本棒之器具为仓内既有 `.tmp\_bcheck.py` ＋ 本棒新写于既有 `.tmp\` 之检索抽取脚本 `_t5_step2_lit_extract_2026_10_24.py`，**二者皆非 skill 正文**）。⚠ 本棒**未以「无需 skill」为辞**——按派工单之如实登记要求逐字写出「0 个，未加载 skill 正文」。
> 📌 **本件之状态**：**已落盘 · 呈 PI**（⛔ 0 宣告任何成就）。
> 📌 **前棒（阶①）**：`_t5_round2_five_gaps_ondisk_check_2026_10_24.md`（**`da4da4746166`**／34,274 B）—— 本棒**⛔ 0 重做阶①**、⛔ 0 回改其一字；本件仅**接续**其三态（见 §8），并于 §3.4 就其一则文献引述**记述改判**（不改其件）。

---

## §0 一句话（五类各一句）

| 类 | 一句话（三态之一） |
|:-:|:--|
| **`A-S`** 环境状态与逐格支撑 | **须改造**——POMDP 文献给出「状态空间 `S`／转移 `T`／观测 `O`／初信念 `b₀`」之**标准形式**与「信念态为历史之充分统计量」之体例（**体例可直接取**），然本案 20 格之可分辨状态集合与**逐格概率支撑之值**无文献可直给 ⇒ 改造点＝把「逐格支撑」落为 `b₀` 之 pmf，**粒度判准改用「决策质量误差界」而非距离**（Poupart & Boutilier 之主张）。 |
| **`A-V`** 独立反事实核·单位与域处置 | **须改造**——单位与域处置之**纪律**文献可解且可直接取（NIST 之 SI 体例：先定「量」再定换算；metrology 之域与校准语汇），但 `v(s,a)` 之**值**文献不可解；⚠ 且本棒实测出阶①所引之**二文献皆非反事实核文献**（§3.4 改判）⇒ 核之值仍须阶③／外委。 |
| **`A-P`** 先验·观测·似然·后验 | **须改造**——**形式可直接取**（`b₀`／`O(o′,s′,a)`／贝叶斯滤波更新之逐字定义）；**接地路径**文献可给（Nakao 等之**矩约束模糊集** ⇒「不硬造单点先验、改给先验之上下界带」）⇒ 改造点＝单点 `π` → 模糊集带 `π`；然**值**仍缺。 |
| **`B-O`** 独立接地之动作占有与情境单位校准 | **不可迁移（就所缺之「值」而言）**——本棒检索所得「逐动作占用」类命中**全为无版本、无测试条件之营销／二手内容**，WHO 冷链仅得储存**温度**区间（片段）、非占用**量**，NIST 只给量纲纪律、不给本域校准值 ⇒ **不可迁移**；唯一可迁移者是「占用量表须以 量纲＋单位＋与 `B_t` 之换算 三列起草」之**纪律**（非数值）。 |
| **`B-F`** 精确约束算子·初值·动作组合·步限绑定 | **须改造**——IPC 之 **cost-bounded (2018)** 赛道给出「只准花 N 步」之**标准体例**（动作代价之和之上界约束）⇒ **可直接用于本案**；PDDL 之 `:init` 给出初值之**标准体例**（可直接取）；然②初值之**值**须接地、③动作组合之体例在 CP／MILP 侧而本棒访问被拦 ⇒ 改造点＝算子语义按「约束之**类型**」而非「字面之形容词」定、组合规则须 PI 明定。 |

---

## §0bis 四根与同批正控

| 根 | 本棒之面 | 实枚举件数（本棒实测 · `[System.IO.Directory]::EnumerateFiles` 递归） |
|:-:|:--|--:|
| `〔本地路径已脱敏〕` | **工作根 · 本棒唯一写入面**（本件落于既有 `results\evidence\register\`；另在既有 `.tmp\` 落 1 件工作脚本） | **7,283** |
| `〔本地路径已脱敏〕` | **只读 · 0 写**（本棒**未读**其内容） | **1,275** |
| `〔归档区〕` | **仅按名与指纹认人 · ⛔ 0 读内容 0 写 0 列目录内容** | **40,242** |
| `〔本地路径已脱敏〕` | **运行时 · 只读自测**（0 写） | **102,562** |

📌 **同批正控**：`tools/exp_harness.py` ＝ **45,590 B** ／ SHA-12 **`ce64b9b97489`**（本棒实测 `Get-FileHash`·SHA-256 全值 `ce64b9b97489422bc8d2b839b55e104470f9098dfc5fa615b930baa49af0b646`）⇒ **与派工单所载 45,590 B／`ce64b9b97489` 逐位相符** ✅。⛔ **0** 用内建 `hash()`。

📌 **件数差之如实登记**：R1 由阶①之 7,220／7,236 增至本棒之 **7,283**（阶①自身新增 7 件＋其后他棒之落件＋本棒之 2 件），R4 由 102,188 增至 **102,562**（运行时日志增长）；R2／R3 与阶①**全等**（1,275／40,242）。本棒⛔ **0** 就此增量作逐件对账。

---

## §1 检索方法与器具

- **检索式设计原则**：每类**至少一**「可引之标准／文献」检索式（找**该领域如何定义与测量**）＋ 至少一「数值候选」检索式（找**参数／阈值／分布**）＋ 至少一「语义／体例」检索式。⛔ **0** 以「只列结果不列检索式」之方式呈报——§7 逐类列全 23 式。
- **⛔ 0 用联网取本案原值**：全部 23 式**均不含**本案素材字面（`correct`／`value`／格号／正解标签）；本棒⛔ 0 以联网作本案之答案来源。
- **器具**：
  - `web_search`（23 次）→ 命中清单由检索器**外置为 artifact**（JSONL + 原体 `.txt`）。
  - `.tmp\_t5_step2_lit_extract_2026_10_24.py`（**本棒新写**，1631 B）＝ 读外置 artifact 原体并打印 `title|link|source|snippet` 清单（只读；⛔ 0 改任一既有件）。
  - `web_fetch`（9 次）＝ 取正文／元数据；成功 4 次、失败 5 次（见 §11）。
  - `.tmp\_bcheck.py`（**仓内既有**，466 B）＝ 字节自证件（按派工单指定路径调用）。
- **采信等级体例**（本件自定，供 PI 复核）：
  - **A级**＝本棒**直接访问**到题录＋摘要＋足以支撑所引断言之正文；**或**该来源之正文经检索器 `content` 抽取而本棒已逐句核对其原文。
  - **B级**＝**题录可核**（标题／作者或机构／年份／链接均已见于命中清单或参考文献表），但**全文未获**（访问被拦／死链／非文本／仅片段）⇒ 其所载之**具体数值**⛔ **0** 引作本案之候选。

---

## §2 `A-S` · 环境状态与逐格支撑

**其所缺（阶①转述回函 `§R-4`）**：①每格**可分辨之环境状态集合**之定义；②该集合上之**逐格概率支撑**。

### §2.1 可引之标准／文献

| # | 出处（标题／作者或机构／年份／链接） | 等级 | 该文如何定义与测量本类之量 |
|:-:|:--|:-:|:--|
| S1 | **Partially Observable Markov Decision Processes in Robotics: A Survey**／Mikko Lauri, David Hsu, Joni Pajarinen／2023／`arXiv:2209.10342`（本棒经 `https://ar5iv.org/abs/2209.10342` **获正文**） | **A** | 给出 POMDP 之**标准形式**：「Formally, a finite-horizon POMDP is a tuple ⟨h, S, A, Ω, T, O, R, γ, b₀⟩ where … S, A, and Ω are the state, action, and observation sets, respectively, T is the stochastic state transition model, such that T(s′,a,s) ≔ P(s′|s,a) … O is the probabilistic observation model, such that O(o′,s′,a) ≔ P(o′|s′,a) … R is a bounded reward function … and b₀ is an initial probability mass function (pmf) over states such that b₀(s) is equal to the probability that the initial state of the system is s.」并明言「The state may include parts relating to an **external environmental state** and the robot system's internal state.」⇒ **本类之「环境状态」有可引之标准定义位**：状态空间 `S` 之元素＝可分辨环境状态；逐格支撑＝该格之 `b₀` 分布。 |
| S2 | **Value-Directed Belief State Approximation for POMDPs**／Pascal Poupart, Craig Boutilier／UAI 2000（`UAI-P-2000-PG-497-506`；`arXiv:1301.3887`，本棒经 abs 页**获题录＋摘要**） | **A** | 给出**支撑粒度之判准**：「Other schemes for belief-state approximation (e.g., based on minimizing a measures such as KL-divergence between the true and estimated state) are **not necessarily appropriate for POMDPs**. Instead we propose a framework for analyzing value-directed approximation schemes, where approximation quality is determined by **the expected error in utility rather than by the error in the belief state itself** … We also describe several algorithms for constructing **bounds on the error in decision quality (expected utility)** associated with acting in accordance with a given belief state approximation.」⇒ **逐格支撑该取多细**，其文献判准是**决策质量误差界**，⛔ 不是 KL 距离。 |
| S3 | **Planning and acting in partially observable stochastic domains**／L. P. Kaelbling, M. L. Littman, A. R. Cassandra／1998／`https://people.smp.uq.edu.au/YoniNazarathy/Control4406_2014/resources/KaelblingLittmanCassandra1998.pdf` | **B** | POMDP 形式化之经典出处（题录与 PDF 链接核于命中清单）。⚠ **本棒 fetch 该 PDF 失败**（`web_fetch received non-text content (application/pdf)`）⇒ **未获全文**，其具体表述⛔ 0 引。 |
| S4 | **Online planning algorithms for POMDPs**／S. Ross, J. Pineau, S. Paquet, B. Chaib-Draa／*JAIR* 32:663–704, 2008／`https://pmc.ncbi.nlm.nih.gov/articles/PMC2748358/` | **B** | 信念态**离散化**与在线规划之方法学出处（题录经 S1 之参考文献表第 [128] 条核实）。⚠ **本棒 fetch 被 cookie 挑战拦** ⇒ **未获全文**。 |

### §2.2 可迁移性三态

**🟡 须改造**（就**体例**而言「可直接用于本案」，就**值**而言「文献不可解」）。

**改造点有二**：
1. **状态集合之定义**：本案之 20 格须各给出一个**有限**之可分辨环境状态集合 `S_i`（S1 之 `S` 之实例化），且该集合**须独立接地**——⛔ **0** 以自拟状态充（S1 明言模型「specified by a domain expert, or they are learned from data prior to planning」⇒ 本案须由**域外**接地或由 PI 明定）。
2. **逐格支撑之落法与粒度判准**：逐格支撑落为该格之 `b₀(s)`（pmf）；**支撑粒度之取舍判准改用 S2 之「决策质量误差界」**，⛔ 不用距离类判准。

### §2.3 数值候选（原文照录其数值与其适用条件）

| 数值 | 该值之来源 | 该值之前提 | ⛔ 采信声明 |
|:--|:--|:--|:--|
| `0 ≤ γ ≤ 1`（折扣因子） | S1（Lauri et al. 2023, §II-A 逐字） | **无限时域 POMDP** 之折扣因子；S1 原注云「The discount factor is not strictly necessary in the finite-horizon case」 | ⛔ **非本案之已定值**；本案若为单步择一，则 `γ` 无适用面 |
| `h ∈ ℕ`（时域长度） | S1（同上，逐字） | **有限时域 POMDP** | ⛔ **非本案之已定值**；本案之 `h` 未定 |
| **无具体数值**——「决策质量（expected utility）误差界」为信念近似之合格判准，且可构造该误差界之算法 | S2（Poupart & Boutilier 2000，摘要逐字） | 须**给定 POMDP 值函数与投影方案**方能构造该界 | ⇒ 本类可得**判准**，⛔ **0** 自本案之素材生造一个数值 |

### §2.4 本类之小结（一句）

**本类之「形」有可引之标准且可取；其「值」无文献可直给** ⇒ 须改造，且**改造之前提**（候选状态集合）须另行接地／候 PI 明定。

---

## §3 `A-V` · 独立反事实核·单位与域处置

**其所缺（阶①转述）**：①**独立反事实核** `v(s,a)`；②**单位之处置**；③**域之处置**。

### §3.1 可引之标准／文献

| # | 出处（标题／作者或机构／年份／链接） | 等级 | 该文如何定义与测量本类之量 |
|:-:|:--|:-:|:--|
| V1 | **Counterfactual Explanations in Sequential Decision Making Under Uncertainty**／Stratis Tsirtsis, Abir De, Manuel Gomez-Rodriguez／NeurIPS 2021（`arXiv:2107.02776v2`，本棒经 arXiv API **获题录＋摘要**） | **A** | 给出**序贯决策中反事实之可引体例**：「We start by formally characterizing a sequence of actions and states using finite horizon Markov decision processes and the **Gumbel-Max structural causal model** … the counterfactual explanation specifies an **alternative sequence of actions differing in at most k actions** from the observed sequence that could have led the observed process realization to a better outcome.」⇒ **反事实**在序贯决策中之标准对象＝**一串动作与状态之形式化** ＋ **与观察序列至多相差 `k` 个动作之替代序列**。 |
| V2 | **Guide for the Use of the International System of Units (SI)**／Ambler Thompson, Barry N. Taylor（NIST）／2008／`https://doi.org/10.6028/NIST.SP.811e2008` | **A** | NIST 之 SI 使用与**换算**之指南（正文经检索器抽取之 nist.gov 出版物页）：「Appendix A provides the definitions of the SI base units. **Appendix B gives conversion factors** for converting values of quantities expressed in units that are mainly unacceptable to use with the SI to values expressed mainly in units of the SI. Appendix B also includes a simplified discussion of rounding numbers and rounding converted numerical values of quantities.」⇒ **单位处置之可引标准**：先定「量」→ 再定换算因子 → 再定取整。⚠ **全文 PDF 未获**（下载为 PDF／非文本）。 |
| V3 | **Writing with SI (Metric System) Units**／NIST（Physical Measurement Laboratory）／`https://www.nist.gov/pml/owm/writing-si-metric-system-units`（正文经检索器抽取之 nist.gov 页面） | **A** | 单位书写与**时间单位之选择**之逐字规定：「**The SI unit of time (actually time interval) is the second (s) should be used in all technical calculations. When time relates to calendar cycles, the minute (min), hour (h), and day (d) might be necessary.**」另：「Compound prefix names or symbols are **not permitted**」「A space is used between the number and the symbol to which it refers.」⇒ **本案单位处置之可引硬纪律**：**时间一律以 `s` 表达**；`min`／`h`／`d` 仅为「与日历周期相关时」之例外；复合前缀禁止。 |
| V4 | **Metric Publications**（SI 出版物目录页）／NIST／`https://www.nist.gov/pml/owm/metric-si/…`（正文经检索器抽取） | **A** | 载 SP 811（2008 版）之条目与 SP 330（2019 版）＝「the United States version of the English text of the **ninth edition** of the BIPM SI Brochure」⇒ **SI 权威文本之版本锚**（BIPM SI Brochure 第九版／2019）。 |
| V5 | **Causes and Explanations: A Structural-Model Approach. Part I: Causes**／Joseph Y. Halpern, Judea Pearl／2005／`https://arxiv.org/pdf/cs/0011012.pdf`（另 Cornell 镜像 `https://www.cs.cornell.edu/home/halpern/papers/actcaus.pdf`） | **B** | 结构因果模型（SCM）下**反事实**（`do` 干预值）之经典出处。⚠ **本棒未获全文**（仅题录核于命中清单）⇒ 其**公式**⛔ 0 逐字引作本案之核之定义。 |
| V6 | **International Vocabulary of Metrology—Basic and General Concepts and Associated Terms (3rd edition)**／JCGM（Joint Committee for Guides in Metrology）／2012（VIM 3rd ed.）／IUPAC 镜像 `https://publications.iupac.org/ci/2008/3006/bw2_vim.html` | **B** | **域之处置**之标准语汇来源（测量域、测量范围、校正）。⚠ **未获全文**（仅题录）⇒ 其条目文字⛔ 0 逐字引。 |

### §3.2 可迁移性三态

**🟡 须改造**，且须**分面**读之：

- **②单位之处置** → **可直接用于本案之纪律**（V2／V3／V4）：时间量一律以 `s` 表达；换算因子取自 SP 811 Appendix B；⛔ 复合前缀。
- **③域之处置** → **可直接用于本案之语汇**（V6，B级）：「域」应以 metrology 之**测量域／测量范围／校正**之语汇承载，⛔ 不用自造词。
- **①独立反事实核 `v(s,a)`** → **文献只给形、不得值**：V1 给出反事实在序贯决策中之标准对象（动作/状态序列之形式化＋至多相差 `k` 个动作之替代序列）；V5 为 SCM 反事实之经典出处（B级，未获全文）。⇒ **核之形可取、核之值文献不可解**（阶①已证本地素材结构性不可推，本棒**未发现**任何文献给出本案域之动作级需求／收益实测值）。

### §3.3 数值候选

| 数值 | 该值之来源 | 该值之前提 | ⛔ 采信声明 |
|:--|:--|:--|:--|
| `1 min = 60 s`；`1 h = 3600 s`；`1 d = 86400 s` | **定义性**（由 `s`／`min`／`h`／`d` 之定义导出；权威换算表见 SP 811 Appendix B） | 时间量之换算 | ⚠ **本棒直接访问之 NIST 页面主体被工具截断，未逐条核于 NIST 原文之该三值**；且 V3 仅言 `min`／`h`／`d` 为「必要时」之例外。⇒ **不得**以此三值径充本案之「校准值」 |
| **时间类之非 SI 单位仅列 `min`／`h`／`d`；`rounds` 无对应量与换算因子** | V3（已获正文）之时间单位枚举 ＋ 本棒对 NIST 单位体系之**有限**核验 | 须以 SP 811 全文之单位总表复核（本棒未获）⇒ **B 级结论** | ⇒ **本棒之判（推导，非文献之值）**：阶①所载 `rounds` 之 3 格**不可**与 `units`／`days`／`hours` 通约，**须作名义量处理**。⚠ 标 B 级（未逐条核 SP 811 全文） |
| `k`（反事实替代序列允许偏离之动作数上限）**之存在性** | V1（已获摘要，逐字「differing in at most k actions」） | 反事实解释问题之定义；`k` 之取值为**实例相关** | ⛔ **不得**取本案之 `3`（`only 3 steps may be spent` 之字面值）为 `k` 之文献值——二者**不同物**（`k`＝反事实偏离度；`3`＝本案步限字面） |
| `9,192,631,770`（铯原子微波周期数，秒之定义） | NIST「SI Units – Time」页（`https://www.nist.gov/pml/owm/si-units-time`，**本棒直接访问**；正文主体被截断，所见为该句与页元数据） | **秒之 SI 定义**（时间之计量基准） | 与本案之约束量**无直接关系**；此处仅作「时间以秒为准」之体系锚点 ⛔ 非本案候选值 |

### §3.4 ⚠ 改判之记述（就阶①之一则文献引述；⛔ **0** 改阶①件一字）

阶① §3 之末载：「📌 且核之**形**已有可引文献（三棒件 §5-1：Poupart & Boutilier `arXiv:1301.3887v1`；Nakao, Jiang & Shen `arXiv:1906.05988v3`）——**得形不得值**。」

**本棒实测**（arXiv abs 页之 `citation_title`／`citation_author`／`citation_date` 与 `Comments`／`Report number` 字段；及 arXiv API 之题录＋摘要）：

| 阶①所引 | 本棒实测之题录 | 实测所示之主题域 | 是否为「反事实核 `v(s,a)`」之文献 |
|:--|:--|:--|:--|
| `arXiv:1301.3887` | Poupart & Boutilier, **"Value-Directed Belief State Approximation for POMDPs"**（[Submitted 16 Jan 2013]；原载 UAI 2000, `UAI-P-2000-PG-497-506`） | **信念态之近似** ＋ **决策质量误差界** | ❌ **否**——属 `A-P` 之信念域 |
| `arXiv:1906.05988v3` | Nakao, Jiang & Shen, **"Distributionally Robust Partially Observable Markov Decision Process with Moment-based Ambiguity"**（v3, 2020-12-08；原发 2019-06-14） | **矩约束模糊集**下之分布稳健 POMDP | ❌ **否**——亦属 `A-P`／分布稳健域 |

⇒ **就本棒实测而言**：阶①「核之**形**已有可引文献（该二文献）」之断言**不成立**；该二文献**皆可迁移**，但**迁移至 `A-P`（信念／分布稳健）**，而**非** `A-V`（反事实核）。本棒**真正检得**之反事实文献为 **V1**（Tsirtsis et al. 2021）。
⚠ **本判读之射程**：**仅限该二文献之题录与摘要层面**（本棒**未获**两文全文）⇒ 本件所记者为「**题名与摘要所示之主题域**」，**非**全文精读之结论。📌 本棒**⛔ 0 回改**阶①件一字，仅在此**记述**此改判，供 PI 复核。

---

## §4 `A-P` · 先验·观测·似然·后验

**其所缺（阶①转述）**：①先验；②观测（模型与观测值）；③似然；④接地之后验。

### §4.1 可引之标准／文献

| # | 出处 | 等级 | 该文如何定义与测量本类之量 |
|:-:|:--|:-:|:--|
| P1 | **Partially Observable Markov Decision Processes in Robotics: A Survey**／Lauri, Hsu & Pajarinen／2023／`arXiv:2209.10342`（**获正文**） | **A** | **四件套之逐字形式**：先验＝「b₀ is an initial probability mass function (pmf) over states such that b₀(s) is equal to the probability that the initial state of the system is s」；似然／观测模型＝「O(o′,s′,a) ≔ P(o′|s′,a)」；后验＝「The belief state at any time step is defined as the **conditional probability distribution over the state given the history of past actions and observations**」，且「The estimate is a pmf over the system state, and is a **sufficient statistic** of the history of past actions and observations」，更新经「a **Bayes filter** τ」 |
| P2 | **Distributionally Robust Partially Observable Markov Decision Process with Moment-based Ambiguity**／Hideaki Nakao, Ruiwei Jiang, Siqian Shen／2020（`arXiv:1906.05988v3`，**获题录＋摘要**） | **A** | **接地之先验／似然之可引替代路径**：「We build an **ambiguity set** of the joint distribution using **bounded moments via conic constraints** and seek an optimal policy to maximize the worst-case (minimum) reward for any distribution in the set. We show that the value function of DR-POMDP is **piecewise linear convex with respect to the belief state** and propose a heuristic search value iteration method for obtaining **lower and upper bounds** of the value function. … DR-POMDP can produce more robust policies **under misspecified distributions** of transition-observation probabilities as compared to POMDP … The DR-POMDP policies are **insensitive** to varying parameter in the ambiguity set and to noise added to the true transition-observation probability values.」⇒ **本案之可行解**：⛔ 不硬造单一点先验；改以**矩约束模糊集**给 `π` 之**上下界带** |
| P3 | **Value-Directed Belief State Approximation for POMDPs**／Poupart & Boutilier／UAI 2000（`arXiv:1301.3887`，**获题录＋摘要**） | **A** | 信念场**近似之合格判准**（见 §2.1 S2）——与阶①在册之「信念场 `n_distinct`＝2 触发退化门 `A1-7`」直接相关：文献主张**以决策质量误差界**衡量近似之可接受性，⛔ 非以分布距离 |
| P4 | **Prior Elicitation for Use in Clinical Trial Design and Analysis: A Literature Review**／（`https://pmc.ncbi.nlm.nih.gov/articles/PMC7917693/`） | **B** | 先验**引出（elicitation）**之方法学综述（题录核于命中清单）。⚠ **本棒 fetch 被 cookie 挑战拦** ⇒ **未获全文**；其任何具体数值或推荐⛔ 0 引 |

### §4.2 可迁移性三态

**🟡 须改造**（**形式可直接取**；**接地路径**文献可给；**值**仍缺）。

**改造点**：本案 `π` 之下单一「点先验」之构造 ⛔ 不可（阶①在册实测：任何以本方 payoff 加权所得之 `π` 皆不过门 `A1-6`／`A1-7`）⇒ 改采 **P2 之模糊集路线**：以**有界矩**（矩约束／锥约束）给转移-观测联合分布之**模糊集**，在模糊集内求最坏情形之策略 ＋ 得信念态上**分片线性凸**之值函数 ＋ 得值函数之**上下界** ＋ 据 P3 之判准（决策质量误差界）衡量。

### §4.3 数值候选

| 数值 | 该值之来源 | 该值之前提 | ⛔ 采信声明 |
|:--|:--|:--|:--|
| `b₀(s)` 之定义（初始 pmf 之逐点定义式） | P1（逐字） | 有限时域 POMDP 之元组 | **形式**，⛔ 非值 |
| `O(o′,s′,a) ≔ P(o′\|s′,a)` | P1（逐字） | 观测模型 | **形式**，⛔ 非值 |
| **无任何数值参数**（矩约束之矩参数、模糊集之宽度、上下界之数值） | P2 摘要逐字 | 模糊集之参数为**实例相关**，摘要未给任何数值 | ⇒ **本棒于此面无数值可录**；⛔ **0** 自造 |

---

## §5 `B-O` · 独立接地之动作占有与情境单位校准

**其所缺（阶①转述）**：①逐格×逐动作之**资源占用量**；②**情境单位校准**（该情境单位之粒度与换算／校正）。

### §5.1 可引之标准／文献

| # | 出处 | 等级 | 该文如何定义与测量本类之量 |
|:-:|:--|:-:|:--|
| O1 | **Guide for the Use of the International System of Units (SI)**／Thompson & Taylor（NIST）／2008／`https://doi.org/10.6028/NIST.SP.811e2008` | **A** | **单位校准之标准体例**：先定「量」→ 再定换算因子（Appendix B）→ 再定取整（Appendix B）。⚠ 全文 PDF 未获 |
| O2 | **Writing with SI (Metric System) Units**／NIST／`https://www.nist.gov/pml/owm/writing-si-metric-system-units`（**获正文**） | **A** | 时间量以 `s` 为准、`min`／`h`／`d` 为例外（逐字，见 V3）；复合前缀禁止 ⇒ **校准表之列结构**之可引纪律 |
| O3 | **SI Units – Time**／NIST（node/429146；created 2010-04-12, updated 2026-01-08）／`https://www.nist.gov/pml/owm/si-units-time`（**本棒直接访问**；正文主体被工具截断） | **A**（页面）／**B**（未获时间单位表） | 证「**the second** … making it the world's standard unit of time」⇒ 时间单位体系之锚点；⚠ **未逐条核该页之非 SI 时间单位表** |
| O4 | **Immunization in Practice — Module 5（WHO_IVB_13.05）**／World Health Organization／`https://www.who.int/iris/bitstream/10665/111623/1/WHO_IVB_13.05_fre.pdf` | **B** | **冷链之权威温度区间**（仅获检索器抽取之**法文原句**）：「… conservés entre **2 et 8 °C** pendant les séances de vaccination ; … conservés entre **2 et 8 °C** pendant le retour des sites périphériques de vaccination vers les établissements de santé.」⇒ **仅片段·全文未获** |
| O5 | **HOW DO CTC AND ECTC RELATE TO EACH OTHER?**（WHO ECTC 说明单页）／WHO／`https://cdn.who.int/media/docs/default-source/immunization/supply-chain/who-ectc-infographic.pdf` | **B** | 仅获片段：「8°C and higher → ECTC（Extended Controlled Temperature Conditions）… Regulatory requirements for licensure apply to thermostable vaccines」⇒ **全文未获**；⚠ **本棒未获任何「冷藏外可维持时长（小时／天数）」之权威数值**（见 §5.3） |
| O6 | **Cumulative functions**（CP 排程之资源累计约束）／IBM ILOG CPLEX Optimization Studio 20.1.0／`https://www.ibm.com/docs/en/icos/20.1.0?topic=scheduling-cumulative-functions` | **B** | 「占用量」在约束规划中之**标准算子**（`cumulative`＝任务占用资源之时间剖面之累计约束）。⚠ **本棒 fetch 403** ⇒ **未获正文**；其语义⛔ 0 逐字引 |
| O7 | **International Vocabulary of Metrology (3rd ed.)**／JCGM／2012（见 V6） | **B** | **「校准」之标准语汇**（校正、测量范围、不确定度）——对应本类之「情境单位校准」 |

### §5.2 可迁移性三态

**🔴 不可迁移（就本类所缺之「值」而言）** —— 逐项分列：

| 构成面 | 三态 | 理由 |
|:--|:--:|:--|
| ①逐格×逐动作之**占用量值** | 🔴 **不可迁移** | 本棒检得之全部「资源消耗／燃油／占用」类命中**皆为不可核之营销或二手内容**（见 §7-B-O 之弃因）；**无任何权威来源给出本案域之动作级占用量**。⛔ 且即便有，**占用量必须与每格之总额约束 `B_t` 逐格可引且一致**（阶①在册）⇒ 外部单点数值**不足以**直接填补。 |
| ②情境**单位校准值** | 🔴 **不可迁移** | NIST 只给**量纲与换算之纪律**（O1／O2／O3），**不给**本案 17 情境之校准值；且 `rounds` **无对应量**（§3.3）⇒ 其 3 格之校准**在单位学上不可完成**，只能作名义量。 |
| ③（可迁移之唯一部分）占用量表之**列结构** | 🟢 **可直接用于本案之纪律**（非数值） | 可引纪律＝占用量表须以「**量纲 ＋ 单位 ＋ 与 `B_t` 之换算**」三列起草（O1／O2 之「先定量→再定换算」体例）；且**须以不可通约之单位分列**（`rounds` 单列）。 |

### §5.3 数值候选

| 数值 | 该值之来源 | 该值之前提 | ⛔ 采信声明 |
|:--|:--|:--|:--|
| `2 – 8 °C` | O4（WHO_IVB_13.05 法文原句片段） | **疫苗冷链之储存温度条件**（WHO 免疫服务之运作规定） | ⚠ **量纲 ≠ 本案之占用量**：温度区间**非**时长占用；⛔ **不得**以此推 `cold chain 3 hours` 之「小时」占用值；亦**非**本案之已定值 |
| 时间单位以 `s` 为准、`min`／`h`／`d` 为例外 | O2（已获正文，逐字） | SI 体系内之时间量表达 | ⇒ 可作**校准之量纲纪律**；⛔ 非占用量之数值 |
| **无任何逐动作占用量之数值** | —— | —— | ⇒ 本棒于本类**无可录之占用量数值**；**阶②于此面已尽**（详见 §9） |

---

## §6 `B-F` · 精确约束算子·初值·动作组合·步限绑定

**其所缺（阶①转述）**：①**算子语义**；②**初值**；③**动作组合**；④**步限之绑定**。

### §6.1 可引之标准／文献

| # | 出处 | 等级 | 该文如何定义与测量本类之量 |
|:-:|:--|:-:|:--|
| F1 | **PDDL2.1: An Extension to PDDL for Expressing Temporal Planning Domains**／M. Fox, D. Long／*JAIR* Vol. 20, pp. 61–124, 2003（`arXiv:1106.4561`；DOI `10.1613/jair.1129`）／本棒经 arXiv API **获题录＋摘要＋journal_ref** | **A**（题录／摘要） | **算子语义之标准体例**：该文「describe[s] the **syntax** of the language, its **formal semantics** and the validation of concurrent plans」；其动因明言「The third competition (held in 2002) set the planning community the challenge of handling **time and numeric resources**」⇒ **数值型算子（numeric fluents）＋并发计划之校验**＝本类①④ 之标准体例所在 |
| F2 | **An Overview of the International Planning Competition Part 1: AI Planning and the IPC**／Amanda Coles, Andrew Coles, Álvaro Torralba, Florian Pommerening／2019（AAAI-2019 IPC 教程）／`https://ai.dmi.unibas.ch/misc/tutorial_aaai2019ipc/ipc01.pdf`（**正文已获**，经检索器抽取之 PDF 正文） | **A** | ①**步限之绑定之标准体例**——轨道表逐字：「Classical Planning Tracks: satisficing (1998, 2000, 2004, 2006, 2008, 2011, 2014, 2018)｜optimal (2004, 2006, 2008, 2011, 2014, 2018)｜satisficing multi-core (2011, 2014)｜agile (2014, 2018)｜**cost-bounded (2018)**」⇒ 「**只准花 N 步**」在规划界之标准体例＝**动作代价之和之上界约束（cost-bounded plan）**，⛔ 非时间上界、⛔ 非状态上界。②**初值之标准体例**——逐字例：「(:init (CONNECTED l1 l2) (CONNECTED l2 l3) (truck-at t1 l1) (truck-at t2 l3))」③**算子之标准体例**——逐字例：「(:action move :parameters (?t - truck ?from ?to - location) :precondition (and (CONNECTED ?from ?to) (truck-at ?t ?from)) :effect (and (not (truck-at ?t ?from)) (truck-at ?t ?to)))」④**PDDL 之演化表**：「1998, 2000: PDDL 1.0: STRIPS, ADL …｜2002: PDDL 2.1: temporal + numeric planning｜2004: PDDL 2.2 …｜2006: PDDL 3.0 …｜2008: **Restricted PDDL Features: STRIPS + action costs**｜2014: Re-introduced conditional effects」⇒ **算子之种类在标准建模语言中本就是分型者**（不等式之方向、数值流、代价、动作代价之和）⇒ 释义须**按类型**定，⛔ 按字面之形容词定 |
| F3 | **PDDL instances covering the International Planning Competitions**（`potassco/pddl-instances` README）／potassco／`https://github.com/potassco/pddl-instances`（README 正文已获） | **B** | **初值与算子之实例体例库**：README 载 IPC 1998–2023 各届之域与变体数，及「Problem instances reside in the `instances` subdirectory and are of the form `instance-x.pddl`」之格式约定 |
| F4 | **PDDL 2.1**（语言参考页）／planning.wiki／`https://planning.wiki/ref/pddl21` | **B** | PDDL2.1 之语言参考。⚠ 仅题录，全文未获 |
| F5 | **Cumulative functions**（CP 排程）／IBM CPLEX Optimization Studio 20.1.0／`https://www.ibm.com/docs/en/icos/20.1.0?topic=scheduling-cumulative-functions` | **B** | **动作组合之标准算子**（`cumulative` 之资源剖面与 `precedence`／`table` 类）。⚠ **本棒 fetch 403** ⇒ 未获正文 |

### §6.2 可迁移性三态

**🟡 须改造**，逐面：

| 构成面 | 三态 | 理由与改造点 |
|:--|:--:|:--|
| ①**算子语义** | 🟡 **须改造**（体例可直接取） | F2 之逐字例与 PDDL 演化表 ⇒ 标准建模语言中算子**按类型分型**。改造点＝本案 16 种约束短语须**逐条归入算子类型**（上界／下界／等式／资源累计／代价之和），⛔ **按字面之形容词**（如 `reserve floor` 之「floor」不自动等于支出上限）——此与阶①所引回函 `§R-7`-5「锚于字面之释义问题」**同向** |
| ②**初值** | 🟡 **须改造**（体例可直接取；**值**须接地） | F2 之 `(:init …)` 为标准体例 ⇒ 可直接取；但**具体数值**（各情境之起始量）⛔ 0 自拟，须独立接地 |
| ③**动作组合** | 🔴 **不可迁移（就文献面）**／**须 PI 明定** | F1／F2 之动作模型为**一串 operator** 之**序列**（可含效果组合），然「组合可行性」之标准体例在 CP／MILP 侧（O6／F5）而**本棒访问被拦**；且阶①已证本案素材为**单选**（`options` 四择一、payoff 为逐选项标量）⇒ **无组合结构可迁**。⇒ 须 PI 明定其是否属本实验面 |
| ④**步限之绑定** | 🟢 **可直接用于本案** | F2 之 **cost-bounded (2018)** 赛道给出标准体例：**动作代价之和 ≤ 上界**。⇒ 本案 `only 3 steps may be spent`（17/17 恒 `3`）之**语义位**已定；⚠ `3` 仍是**本案之字面值**，⛔ **0** 称其为文献值 |

### §6.3 数值候选

| 数值 | 该值之来源 | 该值之前提 | ⛔ 采信声明 |
|:--|:--|:--|:--|
| **无**（cost-bounded 之代价上界值） | F2 轨道表仅载赛道之**存在**（「cost-bounded (2018)」） | 各赛道／各实例**自定**其上界 | ⛔ **不得**取本案之 `3` 为文献值 |
| **无**（`:init` 初值之具体数） | F2 逐字例之 `(:init …)` 为**体例**，非本案情境之值 | 须独立接地 | ⛔ 非本案之已定值 |
| `k`（反事实偏离上限）之存在性 | V1（Tsirtsis et al. 2021） | 反事实解释问题之定义 | ⛔ 与本类④**不同物**；⛔ 不得互相代换 |

---

## §7 检索记录（逐类：检索式／命中数／采信数／弃其余之由）

📌 **命中数之口径（如实登记）**：本棒所用检索器对每式返回**前 N 条**（`total` 字段＝返回条数），⛔ **非**全库命中总数；故下表之「命中数」＝**返回条数**，其射程以本棒之模式与前 N 为界，⛔ 0 外推为「文献界之全量」。

### 7-A `A-S`

| 检索式（逐字） | 返回命中 |
|:--|--:|
| `POMDP hidden state space discretization belief state representation survey` | 10 |
| `environment state space abstraction discretization reinforcement learning survey` | 10 |
| `Kaelbling Littman Cassandra planning and acting in partially observable stochastic domains 1998` | 10 |
| `state aggregation abstraction POMDP discretization error bound Ross Chaib-draa` | 8 |
| **小计** | **38** |

**采信 4 篇**（A 级 2：S1、S2；B 级 2：S3、S4）｜**弃 34 条**。
**弃因**：①同一文献之**多镜像重复**（ACM／dl-next／stag-literatum、ar5iv／arXivLens／tomesphere／lacuna、Springer 镜像、researchgate／1library／studyres 之论文镜像、githubissues／gh.loli.garden／git.tdem 等 fork 镜像）——⛔ 0 重复采信；②**机器人 POMDP 综述**（IEEE／MDPI／ProQuest／Academia 等）——与本类之「环境状态／逐格支撑」无直接关系；③**非 POMDP 之他域**（Active SLAM 综述、天体观测、量子态判别、网络安全策略、贝叶斯自适应 POMDP 等）；④**神经符号／分层 RL 综述**——与「逐格概率支撑」无关。

### 7-B `A-V`

| 检索式（逐字） | 返回命中 |
|:--|--:|
| `counterfactual MDP structural causal model value function v(s,a)` | 10 |
| `dimensional analysis quantity units of measure conversion SI brochure` | 10 |
| `NIST SP 811 guide for the use of the International System of Units conversion` | 10 |
| `Halpern Pearl causes and explanations structural model approach counterfactual 2005` | 10 |
| **小计** | **40** |

**采信 6 篇**（A 级 4：V1、V2、V3、V4；B 级 2：V5、V6）｜**弃 34 条**。
**弃因**：①**arXiv:2607.16999「Counterfactual Shapley Credit Assignment」**（3 条同一文献之镜像：arxiv.org／ar5iv／arxiv-vanity）——本棒**未采**，理由：其编号与题录之**时效存疑**（`2607` 编号晚于本棒之知识面），且本棒未获其正文；②**causaldm.github.io 之教学页**（Scenario 1/2）——教学笔记，非可引之同行评议出处；③**决策与龙博客「V(s) vs Q(s,a)」**——博客；④**「如何改良柴油机效率」等燃油营销内容**（见 7-C）；⑤**中文物理教学／题库页**（力学量纲公式、NCERT 习题等）——非量之标准出处；⑥**UnitPlanet／OmniConverter／Ensign／Morehouse／LbsToKN 等换算站**——二手转述，⛔ **0** 引其数值（其转述之 SP 811 因子降级为 B 级未采）。

### 7-C `A-P`

| 检索式（逐字） | 返回命中 |
|:--|--:|
| `belief initialization prior distribution POMDP experiment protocol how to specify initial belief` | 10 |
| `Bayesian inference prior likelihood posterior conjugate update definition` | 10 |
| `Bayesian pooling of elicited expert priors Ssusa Lesavage` | 10 |
| **小计** | **30** |

**采信 4 篇**（A 级 3：P1、P2、P3；B 级 1：P4）｜**弃 26 条**。
**弃因**：①**教学／博客／题库站**（i32n、CSDN 译文、mysimulator、bayesianstatistics.com、stats.bris vignette、datatistics、smartdocs 等）——⛔ 0 作可引之标准；②**专论之镜像**（arXivLens／alphaxiv／1library／proquest／researchgate 之 PMLR 论文镜像）——未获正文；③**与 POMDP 先验无关之引出文献**（Aitken 之连续二元数据引出法、PLOS 之职业卫生专家引出对比、apsnet 植病专家引出、bayprior R 包说明、cran vignette）——主题相邻而方法不同，且未获正文；④**arxiv:2504.10397「Can LLMs Assist Expert Elicitation…」**——本棒⛔ 0 以 LLM 之作法为引出路径，且未获正文。

### 7-D `B-O`

| 检索式（逐字） | 返回命中 |
|:--|--:|
| `resource consumption per action occupancy table units operational research` | 10 |
| `fuel consumption per trip truck liters operational efficiency data` | 10 |
| `International Committee of Harmonization cold chain storage temperature 2 to 8 degrees time out of refrigeration hours` | 10 |
| `WHO vaccine cold chain controlled temperature chain 168 hours 7 days ambient temperature allowable` | 8 |
| `WHO controlled temperature chain licensed vaccine 168 hours 7 days ambient temperature allowable` | 8 |
| **小计** | **46** |

**采信 6 篇**（A 级 3：O1、O2、O3；B 级 3：O4、O5、O7〔＝V6〕）｜**弃 40 条**。
**弃因**：①**中文成本会计／HR occupancy 分析之博客与百科**（chaj.com.cn、MBA 智库、renrendoc、worktile、vuedesk「occupancy analytics」等）——⚠ 其 `occupancy` **即本仓阶①所遇之同形异义**（＝「已被占用」／「占用率分析」），⛔ 与「动作之资源占用量」不同物；②**燃油/物流营销内容**（shunfuel、transpocodirect、mettlead、ahmadfreetools、chenglix 等）——无版本、无测试条件、无方法披露 ⇒ ⛔ **0** 采信其任何数值；③**Geotab 新闻稿转述**（多家同稿转载）——二手转述之车队数据，⛔ 0 引；④**ICH/GMP 冷链中文文章、疾控中心科普、logger 厂商博客**——非 WHO 之原始文本；⑤**未获全文**者：`technet-21.org`（Cloudflare 挑战）、`PMC5722051`（cookie 挑战）、`gavi.org` VIPS、WHO EPI 页（主体截断）。

### 7-E `B-F`

| 检索式（逐字） | 返回命中 |
|:--|--:|
| `MILP constraint modeling guide units of measure conversion factors engineering` | 10 |
| `constraint programming cumulative scheduling resource constraint semantics` | 10 |
| `planning action budget bounded horizon constraint number of actions limit` | 10 |
| `IPC International Planning Competition domain PDDL initial state files benchmark` | 10 |
| `IPC 2018 plan length restriction track bounded plan length planning competition` | 8 |
| `PDDL2.1 Fox Long extension expressing temporal planning domains JAIR 2003 initial state numeric fluents` | 8 |
| `ICAPS 2018 planning competition plan length restrictions track satisficing optimal definition` | 8 |
| **小计** | **64** |

**采信 6 篇**（A 级 3：F1、F2、＋V1〔Tsirtsis，共用于步限/反事实〕；B 级 3：F3、F4、F5）｜**弃 58 条**。
**弃因**：①**编程竞赛之 IPC 误配**（「2018 ICPC Asia Qingdao」「ICPC Results」等——**International Collegiate Programming Contest**，⛔ 非 International Planning Competition）——此乃本类检索之**主要噪声源**；②**中文营销／百科／题库站**（bohrium、hqwc、MBA 智库「约束传播」、searchdog、科普中国）——非可引之标准；③**MILP 应用论文之各行其是**（核电站调度、垂直农场、铁路配电、柔性制造排程、focapo 会议海报）——不涉本案之算子语义；④**非权威之 CP 教学页**（kindatechnical、newton.com.tw、sogou 百科）——IBM 原文访问被拦 ⛔ 0 用二手充；⑤**「step budget」之 AI 博客／黄页**（sistava AI Glossary、associatesai 博客）——⛔ 非学术出处；⑥**IPC 2023 learning-tracks 页**——与本类之步限/初值语义无直接关系（其 `(:metric)` 与轨迹约束未涉 cost-bounded 之定义）。

### 7-F 总账

| 项 | 数 |
|:--|--:|
| 检索式总数 | **23** |
| 返回命中总数（口径＝前 N 之返回条数） | **218**（170＋48） |
| **采信之独立来源** | **21**（**A 级 10** ＋ **B 级 11**） |
| **弃** | **197** 条命中 |
| 采信来源之 A／B 分布 | A：Lauri2023、Poupart&Boutilier2000、Nakao2020、Tsirtsis2021、Fox&Long2003、Coles2019、NIST SP811、NIST Writing-with-SI、NIST Metric Publications、NIST SI Units–Time ＝ **10**<br>B：Kaelbling1998、Ross2008、Halpern&Pearl2005、VIM2012、GUM(JCGM200)、WHO_IVB_M5、WHO_ECTC单页、IBM CPLEX、potassco/pddl-instances、planning.wiki PDDL2.1、Prior-Elicitation 综述 ＝ **11** |

---

## §8 与阶①之接续（逐类：阶①之可径供部分「已足」／「仍须文献补」）

> ⛔ **不因文献之得而重开阶①**——阶①之三态与其逐件判读**一字不改**；本节仅登记**文献之后阶①各面之供给状态**。

| 类 | 阶①三态 | 阶①之可径供部分 → **已足？** | 仍须文献补者（阶②之后之残余） |
|:-:|:--|:--|:--|
| **`A-S`** | 🔴 真无 | （无可径供面）⇒ 「已足」**不适用** | **仍须文献补**：①每格可分辨环境状态集合之**定义**（文献只给体例，`S_i` 之内容仍缺）②逐格 `b₀` 支撑之**值**（文献无数值）⇒ 阶②**未解此面** |
| **`A-V`** | 🟡 部分承载 | ②**单位之处置**（脱敏包 §OI-1b-1／-2 之单位名义＋非通约判读）＋③**域之处置**（§OI-1a-3 两读并出）⇒ **已足**（且经 V2／V3／V6 **加固**其纪律，⛔ 非替代） | ①独立反事实核 `v(s,a)` 之**值** ⇒ **仍须补**，且本棒实测**文献补不得**（§3.4 改判后，真正可引之反事实文献 V1 只给形）⇒ 阶②于此面**已尽** |
| **`A-P`** | 🟡 部分承载 | ②观测面之**定义**（三棒件 §2）＋④七候选信念之**构造与实测**（§6-1 PE-1）⇒ **已足**（文献只补体例与判准，⛔ 未改其候选，⛔ 仍须删 L269 翻转格明细） | ①先验／③似然／④接地之后验 ⇒ **仍须补**；阶②**已给出路径**（P2 模糊集 ＋ P3 判准），⛔ 尚无**值** ⇒ 阶②**部分解此面** |
| **`B-O`** | 🔴 真无 | （值面无可径供）⇒ 「已足」**不适用**；仅「单位**名义**在盘」之实况成立 | ①逐动作占用量 ＋ ②情境单位校准值 ⇒ **仍须补**，且本棒实测**文献补不得**（§5.2）⇒ 阶②于此面**已尽**（按四阶处置序 ⇒ 入**阶③预实验**，若亦无力 ⇒ **外委**） |
| **`B-F`** | 🟡 部分承载 | ①约束字面 ＋②步限字面（`3`／17-17 恒定）＋③单选事实＋④步限字面 ⇒ **已足**（脱敏包 §OI-1b-1／§OI-2-A） | ①算子语义（**体例已由 F1／F2 补得**⇒ 余「逐条归型」之起草）②初值（**体例已由 F2 补得**⇒ 余「值须接地」）③动作组合（**文献不可迁移**⇒ 须 PI 明定）④步限之**绑定语义**（**已由 F2 之 cost-bounded 补得**⇒ 此面**已足**）⇒ 阶②**解其三项之体例面**，余项入**阶③／PI 明定** |

---

## §9 下一步（阶③预实验）之建议（**只出建议 · ⛔ 0 自行开工**）

| 类 | **是否值得做预实验** | **预实验要验什么**（若做） | **前置条件（本棒之判）** |
|:-:|:--|:--|:--|
| **`A-S`** | 🟢 **值得** | ①以**候选**状态划分（各格之 `S_i`）为输入，验信念场之 `n_distinct` 是否仍触发退化门 `A1-7`（阶① PE-1 实测之 `n_distinct`＝2 即触发）；②验**支撑粒度**（状态数）与**决策质量**之关系（Poupart & Boutilier 之判准）——即「支撑再细是否改变结论」。 | ⚠ **前置**：候选状态集合须先有来源（域外接地 或 我方起草后候 PI 明定）——⛔ **0** 由预实验自行「发明」状态 |
| **`A-V`** | 🟢 **值得（但对象受限）** | 验**核之自洽性**：给定任一候选状态划分，检验 `E_{s∼π}[v(s,a)]` 之 argmax 是否随 `π` 变动；并以 P2 之**模糊集**给 `π` 之带，检验 argmax 之**稳健性**（是否落入同一格）。 | ⚠ **前置**：`v(s,a)` 须**外委实测**方有对象；⛔ **0** 以本方 payoff 改写充核（阶①已证其结构性不可推）⇒ 阶③若仅能自造核，则**该实验无意义**（此即「阶②已尽 ⇒ 阶③亦须外委先」之义） |
| **`A-P`** | 🟢 **值得** | 以 P2 之**矩约束模糊集**取代单点 `π`，实测：①argmax 之**稳健性**（在模糊集内是否恒同）；②该带是否仍触发 `A1-6`／`A1-7` 二门；③带之宽度对结论之影响。 | ⚠ 前置：矩参数（矩之阶与界）须**明定**（文献未给数值）⇒ 须候 PI 一字明定或由我方起草候裁 |
| **`B-O`** | 🟢 **值得（限于自洽性，不可自造量）** | 验**占用量表之自洽性**：任一**候选**占用量表是否与每格之总额约束 `B_t` **逐格可引且一致**（Σ 占用 ≤ `B_t`，且无格为空栏）；并验**校准后**之单位是否仍不可通约（`rounds` 三格之名义化是否致门 `A1-6` 失败）。 | ⚠ **前置**：占用量表须为**外部来源**（⛔ 0 以 payoff 之单调函数充——撞「档丁」之禁；⛔ 0 以标签语义硬凑——PE-2 实测覆盖 0/20）⇒ 阶③**可自测者仅「一致性与退化门」**，量之本身仍须外委 |
| **`B-F`** | 🔴 **不值得作独立预实验** | （若 PI 另令）可验：释义稿之**算子归型**是否与各约束短语**逐条可归且唯一**（即归型是否无歧义）；步限之 cost-bounded 形式化后，`3` 步限是否使可行解集为空或退化为单解 | 📌 **本棒之建议**：本类之缺**大半为「锚于字面之释义与规约」**（阶①回函 `§R-7`-5 之定性）⇒ 正办＝**我方起草释义稿 ＋ 候 PI 裁**（非实验、非文献）⇒ ⛔ **0** 以预实验代替释义 |

---

## §10 本件之限（射程写死）

1. **检索面之限**：检索器对每式返回**前 N 条**（本棒 `N`＝8 或 10）；本件之「命中数」＝**返回条数**，⛔ **非**全库命中总数，⛔ 0 外推为「该领域之全量文献」。
2. **语言面之限**：本棒**以英文检索式为主**，⛔ **0** 系统检索中文文献库（CNKI／万方等）⇒ 中文文献（若存在）**未被本棒覆盖**。
3. **全文面之限**：**A 级 10 篇**中，本棒**逐句核其正文**者仅 3 项（Lauri 2023 之 ar5iv 正文、Coles 2019 之 IPC 教程 PDF 正文〔经检索器抽取〕、NIST 之 3 页正文〔经检索器抽取〕＋NIST SI Units–Time 之直接访问）；其余 A 级为**题录＋摘要**级访问。**B 级 11 篇＝全文未获** ⇒ 其**具体数值／公式／条目文字**⛔ **0** 引作本案之候选。
4. **改判面之限**：§3.4 之改判**仅限**该二文献之**题录与摘要**层面（本棒未获两文全文）⇒ 本件所记者为「题名与摘要所示之主题域」，⛔ **0** 断言其全文内容。
5. **数值面之限**：本件所录**全部数值**皆**非**本案之已定值；本棒⛔ **0** 以任何文献值替代本案之 `correct`／`value`／格内正解；⛔ **0** 以文献值构成本案之占用量、初值或支撑值。
6. **五类之限**：本棒⛔ **0** 落五终判／闭 KD／宣告段毕／门槛成就；本件之「三态」为**文献可迁移性之判**，⛔ **非**五终判语汇之裁定。
7. **非本棒之面**：阶①之核查、阶③之预实验、外委之征询——本棒⛔ **0** 执行、⛔ 0 建议之直接开工。

---

## §11 老实交代

1. **本棒只做阶②（联网查文献）**；⛔ **0** 跑实验、⛔ **0** 调 LLM／API、⛔ **0** 读 `〔本地路径已脱敏〕`、⛔ **0** 读归档区内容（仅按名与指纹认人）、⛔ **0** 移动／重命名／删除**任一**既有件、⛔ **0** 新建目录、⛔ **0** 回改**任一**既有件一字。
2. **本棒新增件共 2 件**：① 本件（落于既有 `results\evidence\register\`）② `.tmp\_t5_step2_lit_extract_2026_10_24.py`（**1,631 B**，本棒新写之检索 artifact 抽取器，只读）。
3. **实际访问之来源与失败（如实登记）**：
   - **直接 fetch 成功**：① `arxiv.org/abs/1301.3887`（题录＋摘要＋全文元数据）② `export.arxiv.org/api/query?id_list=1906.05988,2107.02776,1106.4561`（3 篇之题录＋摘要）③ `ar5iv.org/abs/2209.10342`（**正文**）④ `www.nist.gov/pml/owm/si-units-time`（**已访问**，主体被工具截断）。
   - **fetch 失败（5 次）**：`technet-21.org`（Cloudflare 挑战）｜`pmc.ncbi.nlm.nih.gov/articles/PMC7917693/`（cookie 挑战）｜`www.ibm.com/docs/.../scheduling-cumulative-functions`（**403**）｜`www.bipm.org/documents/20126/2071204/SI_Brochure_9th_edition.pdf`（**死链**：「Sorry, this link is no longer active」）｜`people.smp.uq.edu.au/.../KaelblingLittmanCassandra1998.pdf`（`web_fetch received non-text content (application/pdf)`）。
   - **经检索器 `content` 抽取而得正文（未直接 fetch）**：NIST SP 811 出版物页｜NIST Writing-with-SI 页｜NIST Metric Publications 页｜AAAI-2019 IPC 教程 PDF｜WHO_IVB_13.05 法文片段｜WHO ECTC 单页片段｜NIST SP 330／SP 1038／SP 365 目录条目。
4. **未获全文者之数**：**11 篇**（B 级全部）——其中 **5 篇**系本棒**直接 fetch 失败**（见上），**6 篇**系仅经检索器得题录而未取正文。
5. **⚠ 本棒之最重要之发现（须 PI 留意）**：阶① §3 所引之二文献（`arXiv:1301.3887`／`arXiv:1906.05988v3`）**经本棒实测**，**均非「反事实核」文献**（前者＝信念态近似；后者＝矩约束模糊集之分布稳健 POMDP），**二者皆属 `A-P` 域**；真正可引之反事实文献本棒另得 **Tsirtsis, De & Gomez-Rodriguez (NeurIPS 2021, `arXiv:2107.02776`)**。⇒ 阶①「核之形已有可引文献」之断言**须重核**。📌 本棒**⛔ 0** 回改阶①件一字，**仅在 §3.4 记述**此改判（并已写死其射程：仅题录与摘要层面）。
6. **本棒未做者**：⛔ 0 逐篇通读 A 级 10 篇之全文（仅 3 项达正文级核对）；⛔ 0 检索中文文献库；⛔ 0 取任何权威之**逐动作占用量**数值（燃油/物流类命中全为营销二手内容，**全部弃用**）；⛔ 0 获任何**冷藏外时长（小时／天）**之权威数值（`168 hours` 之说**本棒未获任何已访问来源之支持**，故**不录**）；⛔ 0 自行开工任何预实验；⛔ 0 代 PI 裁任何事。
7. **未验证之事项（如实登记）**：① NIST SP 811 **全文未获** ⇒ 其 Appendix B 之**逐条换算因子**本棒⛔ 0 逐条核（§2.3／§3.3／§5.3 之时间换算三值系**定义性推导**，非逐字转录）；② **BIPM SI Brochure 第九版原文未获**（死链）⇒ 本件以 NIST SP 330 之条目与 nist.gov 之引用间接锚定该版本；③ WHO_IVB_13.05 **全文未获**（仅法文片段）⇒ 其 `2–8 °C` 之**上下文条件**（何物储藏、何时）**未核**；④ IBM CPLEX 之 `cumulative` 语义**未获正文** ⇒ 本件⛔ 0 逐字引其语义；⑤ 本棒**未核**「`rounds` 在 SP 811 单位总表中确实未被收录」之**逐条**事实（该结论系基于本棒所获 NIST 页面之时间单位枚举＋未获全文之限制而作，**标 B 级**）。
8. **观测时点**：2026-10-24 **05:47–06:0x UTC+8**（会话起点 05:47 前后；最后之实测 06:0x）。

---

## §12 字节自证六项

| # | 项 | 本棒实测 |
|:-:|:--|:--|
| 1 | **件路径** | `〔幽灵引用·未上传:_t5_round2_five_gaps_step2_literature_2026_10_24.md〕` |
| 2 | **BYTES** | **56,078** |
| 3 | **SHA-12** | **`bd5c248c2c51`**（＝**填入本栏前**该件之实测值；填入本栏后散列随之变动 ⇒ **终稿之实测 BYTES／SHA-12 见本件回报**） |
| 4 | **BOM** | **0**（前 3 字节 ≠ `EF BB BF` ⇒ **UTF-8 无 BOM**） |
| 5 | **CR 计数** | **0** ⇒ **纯 LF**（VT 亦 ＝ 0） |
| 6 | **末字节 ＋ U+FFFD** | 末字节 ＝ **`0x0A`**；**U+FFFD ＝ 0**（`python -P .tmp\_bcheck.py` 实测） |

📌 **同批正控（同器具同批）**：`tools/exp_harness.py` ＝ **45,590 B** ／ SHA-12 **`ce64b9b97489`** ⇒ 与派工单**逐位相符** ✅。

---

**状态行**：`T5 五类缺口 · 阶②联网查文献 · 23 式／218 返回命中 · 采信 21（ A10＋B11 ）· 弃 197 · 五类三态：AS须改造／AV须改造（附改判）／AP须改造／BO不可迁移／BF须改造 · 0 可直接填值 · 字节自证六项已毕 · 阶③建议候 PI 复核 · 呈 PI`
**落款**：执行棒 worker · 2026-10-24 · ⛔ 0 代 PI 裁 · ⛔ 0 宣告成就
