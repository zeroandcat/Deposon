# G-E01 数值类项 · **联网文献检索取数件**（草案·候 PI 核准）—— 2026-10-14

> **件性质**：新立**联网文献检索件**（append-only 新件 · ⛔ 0 覆写任何既有件 · ⛔ 0 回改既有件一字）。
> **派工依据**：PI 于 2026-10-14 01:33 明示「**部分数值应联网文献获得又莫名 0 联网**」⇒ 本棒为 `G-E01` 之**数值类**项作**联网文献检索**（只读面）。
> 📌 **全件贯穿标记**：本件所给之一切**候选值**均标「**候 PI 核准**」；⛔ **0 径行采认**（沿 PI 2026-10-14 01:19「⛔0 直接追认＝代裁·先斩后奏」＋ 01:3x「『直接采认』之原始射程＝PI 在岗时加速」）。
> **本棒纪律基线**（PI 2026-10-13／14 纠正后口径）：✅ **联网许可**（本棒**实际联网**检索）｜✅ **归档区可读**（本棒**未触**：`D:\私人资料\_non_upload_local_archive` 0 读 0 写 0 列目录）｜✅ **派工携带所需 skill**（本棒 0 调用 skill · 改以直连公开检索 API 完成）｜✅ **可用 LLM 调用，惟 key 永不明文**（本棒 **0 调用**、⛔ **0 读** `.env`）。⛔ **0 代 PI 裁／释／择／确认／给值**｜⛔ **0 宣告**要件闭或①毕｜⛔ **0 开跑任何实验**（含 0 跑敏感性网格）｜⛔ **0 远端写／0 上传**｜⛔ 0 经手 PAT｜⛔ 0 调和任何口径冲突。
> **仪器声明**：SHA-12 ＝ `hashlib.sha256(bytes).hexdigest()[:12]`；bytes ＝ 字节流长度。§1 指纹**为本棒实测**（⛔ 0 沿用他件自报值）。
> **署名**：`worker`（⛔ 0 用 KIMI／GLM／coze／Trae／鲍勃 名头）。

---

## §0 一句话结论

✅ **五项数值之定性问题已逐字界定；文献检索得 12 条可核出处（URL／DOI／PMID／arXiv id 齐备）。**

📌 **三条对 PI 有实质影响之发现（本棒实测·推断·候 PI 核准）**：

1. 🔴 **`ε` 之量纲已锁定为「每轨迹期望错误决策**计数**」，非概率、非比率** —— 故 DQN 式 ε-greedy（ε＝0.05／0.1）**仅类比，⛔ 不可作 `ε` 之取值依据**。
2. 🔴 **正典例锚 `ε ＝ 0.1` 把判死线映射到 ≈0.45–0.61% 之错误率**（H＝33）—— 对 T1–T5（含合成陷阱、博弈）而言**近乎不可能达成**；而**同量文献（rule of three）给出 `ε ≈ 3`（计数）**，映射到 **13.6–18.2%** 之错误率，方落在合理带内。⇒ **正典例锚与同量文献背离，须 PI 裁**（`KC-1` 之升级面，⛔ 0 自裁）。
3. 🟡 **`H` 文献不可得同量值** —— `H` 为本项目特定设计量（15 格 × 每格决策数），无任何外部标准可引；**建议走「预实验择优」**（沿 PI 2026-10-14 01:33 惯例），但其前置仍受 `R-5`（spec 包解包）牵制。

---

## §1 方法与源件回读（本棒**逐件实测** · ⛔ 0 沿用他件自报）

### §1-1 本棒逐字回读之源件 · 实测指纹

| # | 件（相对仓根） | SHA-12（本棒实测） | bytes（本棒实测） | 本棒用其何面 |
|:-:|:--|:-:|--:|:--|
| 1 | `results/_ge01_prereg_seven_requirements_draft_2026_10_13.md` | `0a031a9795a9` | 39,337 | H 之定位 / D∈[0,H] / 三入锁形态 / 区间 [28,40] / 正典四条 |
| 2 | `results/_batch9_deliberation_judgment_2026_10_14.md` | `a93cd166a83b` | 36,623 | 读法 E 之择定（H＝格级 33/格 · 按族锁 · 全盘 495） |
| 3 | `results/_ge01_epsilon_sensitivity_grid_design_r1_2026_10_13.md` | `7551c47d3ece` | 35,956 | ε 之候选域 / 正典例锚 ε=0.1 / KC-1 / 择优判据 |
| 4 | `results/_ge01_prereg_prelexp_selection_design_v2_2026_10_13.md` | `6fc11dacaf24` | 46,864 | T4 A/B、T5 A/B、轨迹加权律 A/B/C 三臂之口径 |
| 5 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15,457 | 正典口径：L12 基线失真=0、L18 N=500、L50-56 族 n 表、L61 D 式、L68 守卫式、L91 bootstrap、L103-110 判死线 |

### §1-2 本棒之方法学（逐条声明）

1. **逐字回读优先于转引**：凡落笔引用他件内容者，均已开卷回读并标行号；⛔ 0 凭记忆或臆测节号。
2. **联网检索实况**：本棒直连公开 API —— **arXiv API**（`export.arxiv.org/api/query`）、**OpenAlex API**、**Crossref REST API**、**Europe PMC REST API**、**ar5iv**（全文 HTML）；⛔ 0 需登录之通道。
3. **出处可核性门槛**：凡本件所列文献，均附 **DOI／PMID／arXiv id／URL** 四者之一；⛔ 0 编造文献；⛔ 0 列仅凭记忆之引用。
4. **阴性结论须列实搜范围与关键词**（见 §5）。
5. ⛔ **0 执行**任何 runner／实验／网格枚举；⛔ **0 建** `tools/distortion_calculator.py`；⛔ **0 采**任何读数。

### §1-3 实搜通道可用性实测（阴性面须如实登记）

| **通道** | **结果** | **处置** |
|:--|:--|:--|
| arXiv API | ✅ 可用（本棒 8 次查询全部成功） | 采用 |
| OpenAlex API | ✅ 可用 | 采用 |
| Crossref REST API | ✅ 可用 | 采用 |
| Europe PMC REST API | ✅ 可用（含全文 XML） | 采用 |
| ar5iv（全文 HTML） | ✅ 可用（DQN 全文实取成功） | 采用 |
| **Wikipedia**（`en.wikipedia.org` / `en.m.wikipedia.org` / REST API） | 🔴 **3 次尝试全部 network failure** | **该通道阴性** ⇒ 凡以 Wikipedia 为唯一出处之文献，本件**0 采**（见 §5 `KD-5`） |
| Semantic Scholar API | 🔴 HTTP 429（限流） | **该通道阴性** |

---

## §2 各数值之定义界定（逐字锚定 · ⛔ 0 凭词义猜测）

### §2-1 `H`（决策数）

| **面** | **界定** | **出处（逐字）** |
|:--|:--|:--|
| **何量** | **一格（机制 × 任务族）内所含之决策数** | `423c84de20d5` L56「3 机制 × 5 任务族 × 33 决策/任务 ≈ 500 calls」＋`a93cd166a83b` 读法 E：「`H` ＝ 一格（M×T）内所含之决策数 ＝ 33；五族同值；`H` 之计量单位 ＝ **格**」 |
| **何量纲** | **无量纲之决策计数**（整数） | `a93cd166a83b` §3-1 L140 逐字 |
| **何单位** | **决策／格**（⛔ 非任务、⛔ 非实例） | 同上；`a93cd166a83b` §2-2 L124 以 `D∈[0,H]` 反证「`D` 计决策数，决策 ⩾ 任务」 |
| **何作用** | **`D` 之量纲分母／上界**（`D∈[0,H]`）；亦为总调用预算之分母 | `0a031a9795a9` §3-2 L78 逐字「`D∈[0,H]`…反例：两个被拒二元决策 D＝2」 |
| **当前值** | **33／格**（按族锁，T1–T5 五值全等，×3 机制同值 ⇒ 15 格 × 33 ＝ 495 calls ≈ 500） | `a93cd166a83b` §0／§4-3 L205 逐字 |
| **状态** | 口径已择定；**逐格实测序列仍不在盘** ⇒ 精确值非实测 | `a93cd166a83b` §0 L18 逐字「本件 0 闭要件②：锁的是**口径**，而**逐格实测序列仍不在盘**」 |

### §2-2 `ε`（守卫常数）—— 🔴 本棒实测之关键界定面

| **面** | **界定** | **出处（逐字）** |
|:--|:--|:--|
| **正典式** | `失真倍数 = D_LLM(M,T) / max(D_Bayesian(M,T), ε)` | `423c84de20d5` **L68** 逐字（§4.1 L88 同式复述） |
| **何量纲** | 🔴 **与 `D` 同量纲 ＝ 每轨迹期望错误决策之「计数」**（`D∈[0,H]`），**非概率**、**非比率**、**非支付量** | 由 `0a031a9795a9` §6 ① L170 `D＝E[Σ_t 1{A_t∉K_t}]` ＋ `423c84de20d5` L61 `D(M,T)=E_π[Σ_t |u*(a_t)-u(a_t)|/max_u]` ＋ `c＝max_u＝1`（§6 ② L171，五族全＝1）＋二元支付域 {0,1} 共同推出 |
| **📌 本棒测算（推断·候 PI 核准·⛔ 0 自裁）** | 上述两式在**冻结之 `c＝1` ＋ 二元支付域 {0,1}** 下**逐项均为 {0,1}** ⇒ **两者量纲同构**，`ε` 之量纲**不因二式之争而变** | 📌 `7551c47d3ece` §1-4 已将二式并列为「口径冲突 · `KD-3`」；本棒**⛔ 0 调和该冲突**，仅陈述：在冻结之评分惯例下二者给出同一量纲 |
| **何约束** | **单一标量常数**，不随格变、不随 t 变，**于 prereg 固定** | `0a031a9795a9` §3-4 L95 逐字 |
| **何作用** | 🔴 **直接进入判死三分支之决策变量**：`ε → max(D_Bayesian, ε) → mean_mult → kill_decision` | `7551c47d3ece` §2-5 L129 逐字 |
| **🔴 基线之实况** | **基线失真按定义为 0**：「已知机制 + 支付 → 失真 = 0」 | `423c84de20d5` **L12** 逐字 |
| **🔴 由此之推论（本棒实测·推断·候 PI 核准）** | 若 `D_Bayesian ≡ 0`，则 `失真倍数 ＝ D_LLM/ε` ⇒ **`ε` 即整个头条指标之分母** ⇒ 判死线 2.0／1.5 **直接由 `ε` 决定**：`mean D_LLM ≥ 2ε` 判 `FAIL_H0`；`mean D_LLM ≤ 1.5ε` 判 `PASS_H1` | 由 L12 ＋ L103-110 之判死线代数推出；**⛔ 0 代 PI 认定** |

### §2-3 `T4` / `T5` 之键口径

| **面** | **T4** | **T5** |
|:--|:--|:--|
| **任务族定义** | 自定义最小博弈，**n＝10**，明确纳什均衡点（`423c84de20d5` L53 逐字） | 低资源博弈，**n＝20**，**每决策只给 3 步推理**，最小信息情境（L54 逐字） |
| **待择之键** | **best-response** ∥ **equilibrium-recognition**（择一**并按明确博弈指定**） | **完整评估状态含隐藏信息**（全信息 oracle）∥ **受限信息最优** |
| **口径出处** | `0a031a9795a9` §2 项1 L50 逐字 | `0a031a9795a9` §2 项1 L50 逐字 |
| **关键约束** | 「现 Nash 标签**不自动供给**任一键」⇒ **A 臂在「明确博弈」未指定前不可实例化** | B 臂须一并声明「**受限信息最优是另一量 · 不主张 ＝ 1**」，否则与全信息 oracle 比较器**混读** |
| **📌 本棒判定：数值性** | ⛔ **无独立数值待取**（为**判据键之择**，非数值项） | ⛔ **无独立数值待取**（为**键类型之择**，非数值项） |

### §2-4 轨迹加权律之口径

| **面** | **界定** | **出处（逐字）** |
|:--|:--|:--|
| **照录下限** | 「**权重和 ＝ 1；`D` ＝ 轨迹误差计数之加权均值**」 | `0a031a9795a9` §2 项3 L52 逐字 |
| **外源断言** | 「**For a finite empirical evaluation, those weights must be given and sum to 1; D is their weighted mean of the trajectory error counts.**」 | `0a031a9795a9` §3-3 L87 逐字引 codex 回函 `a975c7990cd8` |
| **`err_τ` 定义** | `err_τ ＝ Σ_t 1{A_t ∉ K_t}`（**计数**） | `6fc11dacaf24` §4 共同字面逐字 |
| **⛔ 禁止** | **0 以轨迹内决策数再加权**（否则 `D` 之量纲随 `H` 漂移） | 同上 |
| **三臂（PI 2026-10-13 23:56 裁「ABC 预实验择优」）** | **A** 等权 `w_τ＝1/n_τ`｜**B** 族内等权 ＋ 族间权重 `w_f`（`Σ_f w_f＝1`，既有件曾拟 `1/5`）｜**C** 按成功率／有效率加权（「有效性」0 定义 ⇒ 客观不可实例化） | `6fc11dacaf24` §4-1／§4-2 逐字 |
| **📌 本棒判定：数值性** | 🟡 **仅 B 臂含待定数值（族间权重 `w_f`）**；A 臂为 `1/n_τ`（无自由参数）；C 臂受阻于未定义自由度 | — |

---

## §3 逐项文献检索结果（**出处齐备 · 可核**）

### §3-1 `ε` —— **同量文献面（最高价值）**

| **#** | **候选值** | **出处类型** | **出处标识** | **本棒实测之原文（逐字）** | **可引性** |
|:-:|:--|:-:|:--|:--|:-:|
| **E1** | **`ε ≈ 3`（计数）** | 期刊信函（开放获取 · 全文实取） | `doi:10.2147/DDDT.S643259`｜PMID **42548974**｜PMC **13430302**｜Drug Des Devel Ther 2026;20:643259（Shen S, Wang Z） | 「The "rule of three" indicates that, after zero events among n individuals, **the approximate upper 95% confidence bound for the underlying event probability is 3/n**.」 | ✅ **同量**（结构＋量纲皆同：零基线率之 95% 上界，以**计数** 3 表达） |
| **E1-orig** | `ε ≈ 3` 之原始出处 | 期刊（JAMA） | `doi:10.1001/jama.1983.03330370053031`｜PMID **6827763**｜Hanley JA, Lippman-Hand A, JAMA 1983;249(13):1743-3 | （本棒**未实取该文全文**，其被 E1 逐字引为 rule of three 之原始出处 ⇒ 登记为**经 E1 转引**） | ✅ 同量（**转引·未本棒开卷**） |
| **E2** | **`ε ≈ 0.5`（计数）** | 统计惯例（Haldane–Anscombe 连续性校正） | — | 🔴 **本棒 0 实取可核出处**（Wikipedia 通道 3 次 network failure；见 §1-3） | 🔴 **不可引**（见 §5 `KD-5`） |
| **E3** | `ε ＝ 0.05` / `0.1` | arXiv 全文（ar5iv 实取） | **arXiv:1312.5602**｜Mnih V et al., *Playing Atari with Deep Reinforcement Learning* | Table 1 caption 逐字：「running an **ε-greedy policy with ε=0.05** for a fixed number of steps」 | ⛔ **仅类比** —— 其 `ε` 为**随机动作概率** ∈[0,1]，**非计数**；⛔ **不可作 `ε` 取值依据**（见 §4-2） |
| **E4** | 「分母可为零之比率不可估」 | arXiv 摘要 | **arXiv:2510.00389**｜Owen AB, *Zero variance self-normalized importance sampling via estimating equations* | 「**Self-normalized importance sampling uses a ratio estimate, for which the optimal sampler does not have zero variance** and so zero variance cannot even be approached in practice.」；并逐字援引 **Fieller's technique** 处理零分母 | 🟡 **近量**（同构问题：分母可为零之比率；文献之解为**重构估计量**而非就地加 `ε`） |

### §3-2 `H` —— **外部分析量（仅类比／近量）**

| **#** | **锚值** | **出处类型** | **出处标识** | **本棒实测之原文（逐字）** | **可引性** |
|:-:|:--|:-:|:--|:--|:-:|
| **H1** | **25 步／任务**（agent 动作预算） | arXiv 摘要 | **arXiv:2610.01491**｜*Auditing Web Agent Evaluation on WebArena-Lite*（NeurIPS 2026 Workshop） | 「**With a 25 step budget**, Guide Text raises corrected success with MASM from 34.55% to 38.18%.」 | 🟡 **近量**（每任务步数 ≈ 25；⛔ 其为「交互动作步」，我方 `H` 为「二元决策数」⇒ **非同量**） |
| **H2** | 端到端成功率 **14.41%**（GPT-4）vs 人类 **78.24%** | arXiv 摘要 | **arXiv:2307.13854**｜Zhou S et al., *WebArena: A Realistic Web Environment for Building Autonomous Agents* | 「our best GPT-4-based agent only achieves an end-to-end task success rate of **14.41%**, significantly lower than the human performance of **78.24%**」；任务被描述为「diverse, **long-horizon**」 | 🟡 **近量**（支持：长程任务上单任务成功率极低 ⇒ 每格决策数不宜大） |
| **H3** | 8 环境之 LLM-as-Agent 评测；失败主因 | arXiv 摘要（ICLR 2024） | **arXiv:2308.03688**｜Liu X et al., *AgentBench: Evaluating LLMs as Agents* | 「**poor long-term reasoning, decision-making, and instruction following abilities are the main obstacles** for developing usable LLM agents」 | ⟡ **仅类比** |
| **H4** | — | — | — | 🔴 **0 条**载「每格 33 个二元决策」之同量文献（实搜范围见 §5） | 🔴 **KD** |

### §3-3 `T4`（best-response ∥ equilibrium-recognition）—— **判据键之可引性**

| **#** | **支撑点** | **出处类型** | **出处标识** | **本棒实测之原文（逐字）** | **可引性** |
|:-:|:--|:-:|:--|:--|:-:|
| **T4-1** | **NE 与 level-k（最佳应对式推理）乃不同解概念、给出不同预测** | 期刊（经 arXiv 摘要实取） | `doi:10.1162/rest_a_00990`｜**arXiv:2202.12292**｜Levin D, Zhang L, *Bridging Level-K to Nash Equilibrium*, Rev. Econ. Stat. 104(6):1329-1340 (2022) | 「**NLK provides different predictions than those of the NE and Level-K**」 | ✅ **近量·强** —— 直接支持：**二键并非同一集合之别名**，`K_t` 因键而异 ⇒ A/B 之择**实质影响 `D`**，非形式之争 |
| **T4-2** | 实证：迭代推理鲜被援引；level-k 显著劣于均衡 | arXiv 摘要 | **arXiv:2111.05686**｜Rasooly I, *Going... going... wrong: a test of the level-k (and cognitive hierarchy) models of bidding behaviour* | 「when plausibly calibrated, **the level-k model substantially under-predicts the observed bids and is clearly out-performed by equilibrium**」；「subjects **almost never appeal to iterated reasoning**」 | 🟡 **近量** |
| **T4-3** | 理性层级**非单调**：较低或较高层级皆可降低绩效 | arXiv 摘要 | **arXiv:2404.19236**｜Yi L, Wei E, *On the Effect of Bounded Rationality in Electricity Markets* | 「the optimal strategy of the social planner corresponds to a particular rationality level, where **being either less or more rational may both result in reduced social welfare**」 | 🟡 **类比** —— 支持：**二键无一可先验判为「正确」** ⇒ 预实验择优**合理** |

### §3-4 `T5`（全信息 oracle ∥ 受限信息最优）—— **键口径之可引性**

| **#** | **支撑点** | **出处类型** | **出处标识** | **本棒实测之原文（逐字）** | **可引性** |
|:-:|:--|:-:|:--|:--|:-:|
| **T5-1** | **信息价值 VoI ＝ 「由对观测进行推理所得之期望绩效增益」** | arXiv 摘要 | **arXiv:2604.01434**｜Laouar Z, Ho Q H, Sunberg Z, *Leveraging the Value of Information in POMDP Planning* | 「the value of information (VOI) — **the expected performance gain from reasoning about observations**」 | ✅ **同量·概念层** —— 正是「依完整状态 vs 依受限观测」二者之差 ⇒ 佐证 `Q2` B 臂**确为另一量**、须声明「不主张 ＝ 1」 |
| **T5-2** | 信念空间中取 VoI 之启发式 | arXiv 摘要（EPTCS 391, 2023, pp. 89-101） | `doi:10.4204/EPTCS.391.11`｜**arXiv:2310.02345**｜Blumenthal O, Shani G | 「a second heuristic is computed **in belief space, taking the value of information into account**」 | 🟡 **近量** |
| **T5-3** | 逐步／全生命周期 VoI 之定义与界 | arXiv 摘要 | **arXiv:1912.12534**｜Andriotis C P, Papakonstantinou K G, Chatzi E N | 「**Step-wise and life-cycle VoI and VoSHM definitions are devised and their bounds are analyzed**」 | 🟡 **近量** |

### §3-5 轨迹加权律 —— **「权重须给定且和为 1」之出处**

| **#** | **支撑点** | **出处类型** | **出处标识** | **本棒实测之原文（逐字）** | **可引性** |
|:-:|:--|:-:|:--|:--|:-:|
| **W1** | **Horvitz–Thompson 估计量**（权重归一后和为 1 之经典母体） | 期刊（Crossref 实取元数据） | `doi:10.1080/01621459.1952.10483446`｜Horvitz D G, Thompson D J, *A Generalization of Sampling Without Replacement from a Finite Universe*, JASA 47(263):663-685 (1952) | 📌 本棒**仅实取 Crossref 元数据**（标题/作者/刊/卷/页/DOI）；正文**未开卷** | ✅ **同量·原则层** —— 「权重须给定、归一化后和为 1」之教科书出处 |
| **W2** | **自归一化 IS ＝ 权重归一化（和为 1）之比率估计** | arXiv 摘要 | **arXiv:2510.00389**（同 E4）｜**arXiv:2111.06310**｜Yang Z et al., *Self-Normalized Importance Sampling for Neural Language Modeling*（INTERSPEECH 2022） | 「the criteria considered in this work are **self-normalized**」（Yang 等逐字） | ✅ **同量·原则层** |
| **W3** | 与**分层抽样**之结合 ⇒ B 臂族间权重即层权重 | arXiv 摘要（经 JASA 2009 出版） | **arXiv:0805.3591**｜Neddermeyer J C, *Computationally Efficient Nonparametric Importance Sampling*, JASA 104(486):788-802 (2009) | 「This allows to combine our algorithms with other variance reduction techniques such as **stratified sampling**」 | ✅ **同量·B 臂面** —— **5 族 ＝ 5 层**；平衡设计下层权重取 `1/5` 即**分层估计之等权层权重**（文献常规做法） |
| **W4** | C 臂「有效性」未定义之困难 | — | — | （沿 `6fc11dacaf24` §4-2 逐字：**0 盘上字面**，本棒 0 检索到可代其定义之文献） | 🔴 **KD** |

---

## §4 可引性评估与建议（**全部标「候 PI 核准」**）

### §4-1 汇总表（逐项：数值｜候选值｜出处类型｜可引性）

| **数值** | **候选值** | **出处类型** | **可引性** |
|:--|:--|:--|:--|
| **`ε`** | **`3`（计数）** | 期刊（`doi:10.2147/DDDT.S643259`；原始 `doi:10.1001/jama.1983.03330370053031`） | ✅ **同量** |
| **`ε`** | `0.5`（计数） | Haldane–Anscombe 惯例 | 🔴 不可引（0 实取出处） |
| **`ε`** | `0.1` / `0.05` | arXiv:1312.5602 | ⛔ **仅类比**（概率 ≠ 计数） |
| **`H`** | **无同量文献值** | — | 🔴 **KD** |
| **`H`** | 25 步／任务 | arXiv:2610.01491 | 🟡 近量 |
| **`T4`** | （无待取数值；键之择获文献支撑） | `doi:10.1162/rest_a_00990` 等 | ✅ 近量·强 |
| **`T5`** | （无待取数值；键之择获文献支撑） | arXiv:2604.01434 等 | ✅ 同量·概念层 |
| **加权律 `w_f`** | **`1/5`**（B 臂族间等权） | `doi:10.1080/01621459.1952.10483446` ＋ arXiv:0805.3591 | ✅ 同量·原则层 |

### §4-2 🔴 `ε` 之判死线映射测算（本棒实算 · **推断·候 PI 核准**）

**代数**：基线按定义失真为 0（`423c84de20d5` L12）⇒ `mean_mult ＝ mean D_LLM / ε` ⇒ 判死线给出

- `FAIL_H0` ⟺ `mean D_LLM ≥ 2ε`
- `PASS_H1` ⟺ `mean D_LLM ≤ 1.5ε`

以 `H ＝ 33` 折算为**每决策错误率**：

| **`ε`（计数）** | **`FAIL_H0` 之错误率阈值** | **`PASS_H1` 之错误率阈值** | **`ε/H`** | **合理性评** |
|--:|--:|--:|--:|:--|
| **`0.1`**（正典例锚） | **0.61%** | **0.45%** | 0.30% | 🔴 **近乎不可能**（T1–T5 含合成陷阱与博弈，错误率 0.5% 量级不现实） |
| `0.5` | 3.03% | 2.27% | 1.52% | 🟡 偏严 |
| **`3`**（rule of three · 同量） | **18.18%** | **13.64%** | 9.09% | 🟢 **落在合理带内** |

📌 **本棒测算之一致性检验**：rule of three 于 `H ＝ 33` 之**率**表达为 `3/H ＝ 0.0909`；本链 `ε` 为**计数**量纲，故取其**计数**形式 `ε ≈ 3`。二者在 `H ＝ 30` 处重合：`3/0.1 ＝ 30`，即 **`ε ＝ 0.1` 恰为 `H ＝ 30` 时的 rule-of-three 计数下界**。又：PI 过渡区间 `H∈[28,40]` 对应 `3/H ∈ [0.1071, 0.0750]`，**全区间皆在 `0.1` 邻域之 ±1 阶内**。

🔴 **⚠ 此结论之射程（⛔ 0 夸大）**：本节**不断言** `ε ＝ 3` 为正解；仅指出**正典例锚 `ε ＝ 0.1` 与同量文献 `ε ≈ 3` 在判死线映射上背离约一个数量级**，且该背离之消解**属 PI 专属裁量**（`7551c47d3ece` §3-4 `KC-1` 之升级面）。

### §4-3 建议走「**预实验择优**」之项（沿 PI 2026-10-14 01:33 惯例）

| **项** | **建议** | **理由** | **前置阻断** |
|:--|:--|:--|:--|
| **`H`** | ✅ **建议走预实验择优**（以逐格决策序列之实测枚举回填） | 文献**0 同量值**（`H` 为本项目特定设计量）；外部锚（H1–H3）**仅近量／类比** ⇒ 文献不足以定值 | 🔴 受 `R-5`（spec 包 `bb66c577673b` 解包与否）牵制；`a93cd166a83b` §1-3 实测：逐格决策序列在 6 根内不存在 |
| **`ε`** | 🟡 **建议先由 PI 直问择之**（非代立） | 本棒已提供**候选**（`3` / `0.5` / `0.1`）⇒ 该项已非「须 PI 另给」之**无候选**面 ⇒ 按「代立边界纠正」（代立仅限「须 PI 另给」），**须以卡直问 PI**，⛔ 0 代立 | 网格枚举尚可作为**佐证面**（`ρ(ε)`、`φ(ε)` 全表）随卡呈 PI |
| **加权律 B 臂 `w_f`** | 🟢 **建议径采 `1/5`**（平衡 5 层之分层等权） | 文献面最完整（`W1`＋`W3`）；且五族设计均衡 ⇒ 等权层权重为标准做法 | 无（惟仍**候 PI 核准**，⛔ 0 径行采认） |
| **T4／T5 键** | ✅ **维持「预实验择优」**（PI 2026-10-13 23:56 既裁） | 本棒文献（T4-1～T4-3、T5-1～T5-3）**支持二键实质相异且无一先验正确** ⇒ 预实验择优**有据** | T4 A 臂仍受「明确博弈未指定」阻断（`6fc11dacaf24` §2-6 风险 1） |

---

## §5 遗留 / KD（如实登记 · ⛔ 0 以「不可得」掩「未搜」）

### §5-1 KD 条目

| **#** | **KD** | **性质** | **实搜范围与关键词** |
|:-:|:--|:--|:--|
| **KD-1** | **`H` 无同量文献值** | 不可得 | arXiv API：`ti:"WebArena"`、`ti:"AgentBench"`、`ti:"GSM8K"`、`abs:"level-k" AND abs:"Nash"`；OpenAlex/Crossref：agent benchmark 决策步数。**0 条**载「每格 33 个二元决策」之同量锚 |
| **KD-2** | **`ε ＝ 0.5`（Haldane–Anscombe）无可核出处** | 检索受阻 | Wikipedia 三通道（`en.wikipedia.org/wiki/Continuity_correction`、`en.m.wikipedia.org/...`、`w/api.php?action=query`）**3 次全部 network failure**；Europe PMC／Crossref 未取到可引之原始公式出处 ⇒ **本件 0 以 Wikipedia 二手陈述充作出处** |
| **KD-3** | **Fieller（1957）原始文献之 DOI 未实测确认** | 部分未验 | Crossref `GET /works/10.1093/biomet/44.1-2.109` 返回 **Resource not found** ⇒ 本件仅引 **arXiv:2510.00389 摘要中逐字援引之 "Fieller's technique"**，⛔ **0 断言 Fieller 原文之卷期页／DOI** |
| **KD-4** | **`ε` 网格之 6 个十进阶节点（N1–N5、N7）无逐点文献依据** | 不可得 | 本棒检索之同量文献**仅支持 `ε ≈ 3`（计数）**一处有公式出处 ⇒ N1–N5、N7 之取值**无文献背书**，仍属 `7551c47d3ece` 之「待核域」 |
| **KD-5** | **Wikipedia 通道整体不可用** | 检索受阻 | 同 KD-2 之三通道；**Semantic Scholar API** 亦返回 HTTP 429 ⇒ 本件全部文献面**未依赖**该二者 |
| **KD-6** | **加权律 C 臂「有效性」之定义仍 0 文献可代** | 不可得 | arXiv API：`abs:"self-normalized" AND abs:"importance sampling"`（38 命中，**0 条**涉及「成功率／有效率加权」之轨迹级定义）⇒ **源件 `6fc11dacaf24` §4-2 之 `KD-2`（「有效性」未定义自由度）未消**（⚠ 编号提醒：此为**源件编号**，与本表 `KD-1`～`KD-6` 之编号**各自独立**，勿混读） |

### §5-2 本件**⛔ 不断言**者（沿既有「射程不夸大」纪律）

| **面** | **⛔ 0 断言** |
|:--|:--|
| `ε` | ⛔ 0 断言 `ε ＝ 3` 为正解｜⛔ 0 断言正典例锚 `ε ＝ 0.1` 为误（仅指出二者映射背离） |
| `KD-3`（源件口径冲突） | ⛔ 0 **调和** `423c84de20d5` L61 差值式 vs `0a031a9795a9` §6① 指标式之冲突；本棒仅陈述在冻结之 `c＝1` ＋ 二元支付域下**二者量纲同构** |
| `H` | ⛔ 0 断言 `H ＝ 33` 已闭；⛔ 0 断言逐格序列可得 |
| 要件状态 | ⛔ 0 宣告要件②／③／④ 之闭；⛔ 0 宣告①毕 |
| 全部候选值 | ⛔ 0 径行采认；一切均标「**候 PI 核准**」 |

### §5-3 建议 PI 直问之问题（本棒 0 代问 · 供 parent 转呈）

| **#** | **问** | **备选项** |
|:-:|:--|:--|
| **Q-A** | `ε` 取值（**已由「无候选」转为「有候选」之择面** ⇒ 按「代立边界纠正」须**直问**，⛔ 0 代立） | 甲 `ε ＝ 3`（rule of three · 同量）｜乙 `ε ＝ 0.5`（Haldane·待补出处）｜丙 维持 `ε ＝ 0.1`（正典例锚）｜丁 授权跑敏感性网格以 `ρ(ε)`／`φ(ε)` 全表佐证后由 PI 择 |
| **Q-B** | `ε` 与 `H` 是否**联立冻结** | 甲 各自独立冻结｜乙 令 `ε ＝ 3/H` 随 `H` 变动（**⛔ 与「`ε` 须为单一标量常数」相冲，须 PI 明示**） |
| **Q-C** | 加权律 B 臂族间权重是否径采 `1/5` | 甲 `1/5`｜乙 另给｜丙 移出 B 臂之 prereg 面 |

---

## §6 落盘自报（本棒实测）

| **项** | **值** |
|:--|:--|
| **件名** | `results/_ge01_numeric_literature_search_2026_10_14.md` |
| **绝对路径** | `D:\私人资料\deposon-repo\results\_ge01_numeric_literature_search_2026_10_14.md` |
| **落前占用检查** | `Test-Path` ＝ **False**；`os.listdir('results')` 子串 `numeric_literature` ＝ **0 命中** ⇒ **未覆写任何既有件** |
| **⛔ SHA-12** | ⛔ **0 自指**：本件内 **0 写自身指纹**（沿 `0a031a9795a9` §3-6 拟细则①「⛔ **0 自指**：prereg 内 0 写自身指纹，另立锁记件登记」）⇒ 本件 SHA-12 之实测值**由本棒回执／另立锁记件承载**，不落本件正文 |
| **bytes** | 28399 |
| **BOM** | False |
| **行尾** | **纯 LF**；CR ＝ 0；CRLF ＝ 0 |
| **TAB** | 0 |
| **CTRL（除 LF 外之控制符）** | 0 |
| **nonAscii** | 5113（**字符**口径）／15199（**字节**口径） |
| **U+FFFD** | 0 |
| **编码写入** | `io.open(..., encoding='utf-8', newline='\n', errors='strict')`（Python 直写并回读校验，⛔ 0 经 PowerShell 管道中转正文） |

> **署名**：`worker` · 2026-10-14 ｜ 联网只读面 · ⛔ 0 远端写 · ⛔ 0 读 `.env` · ⛔ 0 径行采认
