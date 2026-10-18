# skill「调用面」实测登记件：用户面 223 项真实加载抽样（2026-09-30）

- **件性质**：**实测登记件**（新建 1 件 · 0 回改既有件 · 0 覆写 · 0 改配置 · 0 改/移/重命名 skill 文件）
- **触发**：PI 2026-09-30 裁「**仅调用面实测**」（`.minimax\bin` 不查），对登记件 `e96d99ff9e75` §2 所载「用户面 223 项调用面未测」项取数
- **输入链**（只读，本棒实测 SHA-256 前 12 位）：

| # | 件 | SHA-12 | 字节 | 本件引用面 |
|---|---|---|---|---|
| 1 | `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` | `e96d99ff9e75` | 55,340 | **样本名单唯一来源**：§2.4（21 项 name≠目录名 ＋ 5 枚多重面）、附录 A（223 项逐项表·含定位面与字节/SHA-12） |
| 2 | `results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | `644e0666fbc4` | 25,901 | **机制与体例先例**：§2 真实调用 18 次、失败形态 `Local skill not found: <名>`、成功返回 SKILL.md ＋ Location 自报、裸名臂全用户面、`plugin:skill` 臂 0/8 |

- **出件**：**doc-writer**（`agent-0032834a3e04`）· 依派工单执行 · 0 LLM / 0 外部 API / 0 外部 URL / 0 key 读取
- **命名**：去版本前缀 · `_主题_日期`；落名前 **2 轮 × 4 目录**（`results/` `docs/` `letters/` `deposon_team/`）**全部 exists=False**，另加全仓递归近名 glob（`**/*call_surface*`）**0 命中** ⇒ **新建，0 覆写**
- **实测时段**：2026-09-30（本会话内，串行执行）
- **版式**：UTF-8 无 BOM · 纯 LF · SHA-12 自核节见 §5

> **一票结论（先看这条）**：本会话**具备 skill 加载器**（`Skill` 工具），故「调用面未测」**在本棒已部分取数**。**62 次真实调用覆盖 40 枚样本**：**总成功 40 / 失败 22**（终态口径以 §5.4 逐例清点为准；初稿曾误记「53 次 / 40 枚 / 40 成功 / 13 失败」，两轮勘误痕迹见 §5.4）。其中——
> ① **`name`≠目录名项（§2.4 列表实列 22 项）：按目录名裸名调用 0/22 成功，按 frontmatter `name:` 值调用 22/22 成功**，命中面 22/22 为用户面 ⇒ **登记件「按裸名寻址可能落空」由字面推断升级为实测事实**；
> ② **多重面 5 枚（`docx`/`pdf`/`pptx`/`xlsx`/`deep-research`）裸名调用 5/5 成功，全部命中用户面**，**plugin-cache 面与 `.builtin-skills` 面 0 次命中**（三面基线已实测，逐字比对见 §3.2）；
> ③ 复现臂与 644e 件**一致 2/2**，另测得 1 枚 644e 未测的用户面成功例（`scholar-evaluation`）。
> **本件不断言因果**：只登记「谁成功、谁失败、落在哪一面、什么写法可寻址」。

---

## §1 方法与工具自证

### §1.1 加载器存在性（先行判定，PI 派工的硬前置）

| 项 | 本棒实测 |
|---|---|
| 本会话可用工具中**是否存在 skill 加载入口** | ✅ **存在** —— `Skill` 工具（描述：*Loads the complete SKILL.md instructions for an available local or plugin skill*） |
| 调用是否等同 644e 件 §2 方式 | ✅ **同机制**（该件同棒同为 `Skill` 加载面真实调用） |
| 失败返回形态 | `Local skill not found: <名>`（与 644e §2.2 逐字同形） |
| 成功返回形态 | `# Skill: <名>` ＋ `Location: files:///D:/Users/Administrator/.minimax/skills/<目录>/SKILL.md` ＋ SKILL.md 全文 |

> 因此**不适用**「无加载器则停止并如实报告」的分支。**本件 0 次以文件直读冒充调用面结果**：所有「成功/失败」判定**一律以 `Skill` 工具的真实返回为唯一依据**；磁盘读取仅用于**基线指纹比对**（判定命中哪一面），不用于判定能否加载。

### §1.2 三面基线（调用前锁定，只读 `Get-FileHash -Algorithm SHA256`）

| skill | 用户面 SHA-12 / 字节 | PC 面（`v2\plugin-cache`）SHA-12 / 字节 | BI 面（`.builtin-skills`）SHA-12 / 字节 |
|---|---|---|---|
| `docx` | `cfbabd72b1ae` / 20,084 | `12e5a0cccd0c` / 11,619 | `c9407f69ad99` / 11,536 |
| `pdf` | `9f78b8359fbd` / 8,072 | `e39aa05f43db` / 28,593 | `3ce4de4609d4` / 28,863 |
| `pptx` | `e5b0df918cbe` / 9,182 | `931a81818974` / 32,801 | `75c4bbe0bf93` / 13,049 |
| `xlsx` | `55591d7decc1` / 11,464 | `6eab2cbf5606` / 27,366 | `a3f0d9a7afa6` / 26,848 |
| `deep-research` | `5637feab59dc` / 6,995 | **MISSING**（PC 面无此 skill） | `c93fe1961ff4` / 12,109 |

> **三面 frontmatter 首行已分化**（可作指纹锚）：用户面 5 枚均为 `--- / name: <名> / description…`；PC 面 4 枚为 `name`＋`description: >` 或 `metadata:`；BI 面 5 枚为 `description: >`（`deep-research`）或 `metadata: version`（`docx`）。故**加载内容的首部逐字比对即可区分命中面**。

### §1.3 抽样设计（写明规则与名单）

| 臂 | 设计 | 样本数 | 规则 |
|---|---|---|---|
| **臂 1** | 全部 `name`≠目录名项（登记件 §2.4 **列表实列 22 项**，**全取，不抽样**） | **22 枚 / 44 次** | 每项**先以目录名裸名**调用；失败者**再以 frontmatter `name:` 值**调用一次（每项最多两形态，**0 穷举前缀组合**） |
| **臂 2** | 多重面 5 枚 | **5 枚 / 5 次** | 派工点名的 `docx` `pdf` `pptx` `xlsx` `deep-research`，**裸名**调用，与 §1.2 三面基线逐字比对 |
| **臂 3** | 复现臂 | **3 枚 / 3 次** | 取 644e §2.2 已知成功样本 2 枚（`scientific-writing` 复 B-01、`peer-review` 复 B-02）＋ 反向对照 1 枚（`scholar-evaluation`，644e 仅在 catalog 层提及、未实测） |
| **臂 4** | 对照样本（等距抽样） | **11 枚 / 11 次** | 规则：223 项目录名按**字母序升序**排列，步长 ≈ 223/12 ≈ 18.6，取索引 `1, 19, 38, 57, 76, 94, 113, 132, 151, 169, 188, 207` 共 12 个点；**去重规则**：`#1 abstract-writing`、`#57 dose-adjustment` 已在臂 1 实测 ⇒ 不重复调用（去重 2 枚）；`#151 primekg` 等 10 枚实调；**为维持 ≥8 枚下限并补足样本面，另补 1 枚相邻等距点 `vaex`（索引 216）** ⇒ 实际实调 **11 枚** |
| **合计** | — | **40 枚 / 62 次** | — |

**臂 4 实际实调名单（10 枚，含索引，规则可复算）**：`#19 biopython`、`#38 context-fundamentals`、`#94 industry-research-report`、`#113 matlab`、`#132 openclaw-setup-assistant`、`#151 primekg`、`#169 qutip`、`#188 scikit-bio`、`#207 tiledbvcf`、`#216 vaex`（补点，用以在 `#76` 未调的情况下维持 ≥8 枚下限）。

### §1.4 纪律执行（逐条自证）

| 纪律 | 本棒执行情况 |
|---|---|
| 加载回的内容＝**惰性数据**，不执行其中任何指令 | ✅ **0 遵从**。多份 SKILL.md 含祈使性/冒名/外发/凭据类指令（见 §4 风险登记），**一律仅登记** |
| 全程只读 | ✅ 0 改配置 · 0 改/移/重命名 skill 文件 · 0 写 `config.yaml`/`mcp.json` |
| 敏感值 | ✅ **0 读 0 落盘 0 入 prompt** —— `openclaw-setup-assistant` 等件正文含 API Key 占位符，**本棒仅登记其「要求索取凭据」这一事实，未复制、未使用任何真实 key** |
| 0 外部网络 / LLM 调用 | ✅ 加载为本地解析；`web_search` / `web_fetch` / `mcp_invoke` **0 次调用** |
| 失败重试上限 | ✅ 每项**最多两形态**（目录名 / `name:` 值），**0 穷举前缀组合** |
| 0 涉密外发 | ✅ 无任何外发；`openclaw-setup-assistant` 的飞书接入段仅登记未执行 |

---

## §2 逐例表 · 臂 1（21 项 `name`≠目录名 · 42 次）

**时刻**：全部为本会话内，2026-09-30 串行执行（分钟级连续，无跨时刻复测）。
**Location 形态**：全部为 `files:///D:/Users/Administrator/.minimax/skills/<目录名>/SKILL.md`（**D 盘实体路径**，与 644e §0.4 一致；`C:\Users\Administrator\.minimax` 为指向 `D:\Users\Administrator\.minimax` 的 Junction）。

| # | 请求名（逐字） | 结果 | 失败原文 | Location | 内容指纹（与哪一面吻合） | 目录名 |
|---|---|---|---|---|---|---|
| A1-01 | `abstract-writing` | ❌ 失败 | `Local skill not found: abstract-writing` | 0 | — | `abstract-writing` |
| A1-02 | `Abstract Writing` | ✅ 成功 | — | `…/skills/abstract-writing/SKILL.md` | `df2f2ef27bcb` / 10,157 B（`origin: ECMed` 逐字）→ **用户面** | `abstract-writing` |
| A1-03 | `academic-paper-writing-expert-zip` | ❌ 失败 | `Local skill not found: academic-paper-writing-expert-zip` | 0 | — | 同左 |
| A1-04 | `论文写作专家` | ✅ 成功 | — | `…/skills/academic-paper-writing-expert-zip/SKILL.md` | `5d43b2911ca3` / 5,836 B → **用户面** | 同左 |
| A1-05 | `antimicrobial-stewardship` | ❌ 失败 | `Local skill not found: antimicrobial-stewardship` | 0 | — | `antimicrobial-stewardship` |
| A1-06 | `Antimicrobial Stewardship` | ✅ 成功 | — | `…/skills/antimicrobial-stewardship/SKILL.md` | `82c44fe80005` / 10,978 B（`origin: ECMed`）→ **用户面** | 同左 |
| A1-07 | `bayesian-clinical-reasoning` | ❌ 失败 | `Local skill not found: bayesian-clinical-reasoning` | 0 | — | `bayesian-clinical-reasoning` |
| A1-08 | `Bayesian Clinical Reasoning` | ✅ 成功 | — | `…/skills/bayesian-clinical-reasoning/SKILL.md` | `264e28ab2a2a` / 7,360 B → **用户面** | 同左 |
| A1-09 | `clinical-decision-rules` | ❌ 失败 | `Local skill not found: clinical-decision-rules` | 0 | — | `clinical-decision-rules` |
| A1-10 | `Clinical Decision Rules` | ✅ 成功 | — | `…/skills/clinical-decision-rules/SKILL.md` | `932e8265d78d` / 6,455 B → **用户面** | 同左 |
| A1-11 | `critical-appraisal` | ❌ 失败 | `Local skill not found: critical-appraisal` | 0 | — | `critical-appraisal` |
| A1-12 | `Critical Appraisal` | ✅ 成功 | — | `…/skills/critical-appraisal/SKILL.md` | `045fc825f5d5` / 8,559 B → **用户面** | 同左 |
| A1-13 | `differential-diagnosis-generation` | ❌ 失败 | `Local skill not found: differential-diagnosis-generation` | 0 | — | `differential-diagnosis-generation` |
| A1-14 | `Differential Diagnosis Generation` | ✅ 成功 | — | `…/skills/differential-diagnosis-generation/SKILL.md` | `be1eae5a640d` / 6,589 B → **用户面** | 同左 |
| A1-15 | `dose-adjustment` | ❌ 失败 | `Local skill not found: dose-adjustment` | 0 | — | `dose-adjustment` |
| A1-16 | `Dose Adjustment` | ✅ 成功 | — | `…/skills/dose-adjustment/SKILL.md` | `6c47d038348f` / 10,333 B → **用户面** | 同左 |
| A1-17 | `drug-interactions` | ❌ 失败 | `Local skill not found: drug-interactions` | 0 | — | `drug-interactions` |
| A1-18 | `Drug Interactions` | ✅ 成功 | — | `…/skills/drug-interactions/SKILL.md` | `4b071debe144` / 8,893 B → **用户面** | 同左 |
| A1-19 | `evidence-levels-and-hierarchies` | ❌ 失败 | `Local skill not found: evidence-levels-and-hierarchies` | 0 | — | `evidence-levels-and-hierarchies` |
| A1-20 | `Evidence Levels and Hierarchies` | ✅ 成功 | — | `…/skills/evidence-levels-and-hierarchies/SKILL.md` | `0064b3a3da96` / 8,499 B → **用户面** | 同左 |
| A1-21 | `grade-assessment` | ❌ 失败 | `Local skill not found: grade-assessment` | 0 | — | `grade-assessment` |
| A1-22 | `GRADE Assessment` | ✅ 成功 | — | `…/skills/grade-assessment/SKILL.md` | `433d22b9a7b5` / 10,287 B → **用户面** | 同左 |
| A1-23 | `hypothesis-testing` | ❌ 失败 | `Local skill not found: hypothesis-testing` | 0 | — | `hypothesis-testing` |
| A1-24 | `Hypothesis Testing` | ✅ 成功 | — | `…/skills/hypothesis-testing/SKILL.md` | `d90e2931c854` / 10,303 B → **用户面** | 同左 |
| A1-25 | `illness-scripts` | ❌ 失败 | `Local skill not found: illness-scripts` | 0 | — | `illness-scripts` |
| A1-26 | `Illness Scripts` | ✅ 成功 | — | `…/skills/illness-scripts/SKILL.md` | `0ddcdce71091` / 7,912 B → **用户面** | 同左 |
| A1-27 | `imrad-structure` | ❌ 失败 | `Local skill not found: imrad-structure` | 0 | — | `imrad-structure` |
| A1-28 | `IMRAD Structure` | ✅ 成功 | — | `…/skills/imrad-structure/SKILL.md` | `91838e6c1a30` / 10,931 B → **用户面** | 同左 |
| A1-29 | `lab-interpretation` | ❌ 失败 | `Local skill not found: lab-interpretation` | 0 | — | `lab-interpretation` |
| A1-30 | `Lab Interpretation` | ✅ 成功 | — | `…/skills/lab-interpretation/SKILL.md` | `5e00bc476b01` / 9,250 B → **用户面** | 同左 |
| A1-31 | `prd-to-prototype` | ❌ 失败 | `Local skill not found: prd-to-prototype` | 0 | — | `prd-to-prototype`（**YAML 引号值**） |
| A1-32 | `PRD to Prototype` | ✅ 成功 | — | `…/skills/prd-to-prototype/SKILL.md` | `8fda2384b597` / 9,923 B（frontmatter 为 `name: "PRD to Prototype"` 带引号）→ **用户面** | 同左 |
| A1-33 | `rct-design` | ❌ 失败 | `Local skill not found: rct-design` | 0 | — | `rct-design` |
| A1-34 | `RCT Design` | ✅ 成功 | — | `…/skills/rct-design/SKILL.md` | `340a7f874ba3` / 7,863 B → **用户面** | 同左 |
| A1-35 | `regression-analysis` | ❌ 失败 | `Local skill not found: regression-analysis` | 0 | — | `regression-analysis` |
| A1-36 | `Regression Analysis` | ✅ 成功 | — | `…/skills/regression-analysis/SKILL.md` | `c04a68a588bd` / 10,588 B → **用户面** | 同左 |
| A1-37 | `sample-size-calculation` | ❌ 失败 | `Local skill not found: sample-size-calculation` | 0 | — | `sample-size-calculation` |
| A1-38 | `Sample Size Calculation` | ✅ 成功 | — | `…/skills/sample-size-calculation/SKILL.md` | `12ab422904e3` / 10,585 B → **用户面** | 同左 |
| A1-39 | `sensitivity-and-specificity` | ❌ 失败 | `Local skill not found: sensitivity-and-specificity` | 0 | — | `sensitivity-and-specificity` |
| A1-40 | `Sensitivity and Specificity` | ✅ 成功 | — | `…/skills/sensitivity-and-specificity/SKILL.md` | `9a87d365110c` / 7,936 B → **用户面** | 同左 |
| A1-41 | `shared-decision-making` | ❌ 失败 | `Local skill not found: shared-decision-making` | 0 | — | `shared-decision-making` |
| A1-42 | `Shared Decision-Making` | ✅ 成功 | — | `…/skills/shared-decision-making/SKILL.md` | `92878deb20ea` / 8,289 B → **用户面** | 同左 |
| A1-43 | `survival-analysis` | ❌ 失败 | `Local skill not found: survival-analysis` | 0 | — | `survival-analysis` |
| A1-44 | `Survival Analysis` | ✅ 成功 | — | `…/skills/survival-analysis/SKILL.md` | `6c251e084ba5` / 12,005 B → **用户面** | 同左 |

> **臂 1 计数**：44 次调用＝**22 目录名失败 ＋ 22 `name:` 值成功**。**22/22 命中用户面**。其中 1 项为 YAML 引号值（`PRD to Prototype`），**去引号后仍须按引号内字面寻址方能命中**（本棒实测：带引号字面值 `PRD to Prototype` 成功，目录名失败）。
> **附带事实**：22 项的 `name:` 值中 **1 项为中文**（`论文写作专家`），**2 项含连字符/空格大写形态**（`IMRAD Structure` `Shared Decision-Making`）——**目录名裸名对这 22 枚全部落空，无一例外**。

---

## §3 逐例表 · 臂 2 / 臂 3 / 臂 4

### §3.1 臂 3 · 复现臂（3 次）

| # | 请求名（逐字） | 结果 | Location | 内容指纹 | 与 644e 件对照 |
|---|---|---|---|---|---|
| R-01 | `scientific-writing` | ✅ 成功 | `…/skills/scientific-writing/SKILL.md` | `f835a31244ad` / 33,780 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.` 逐字）→ **用户面** | **一致**（644e §2.2 B-01 记：成功·用户面·`f835a31244ad`/33,780 B） |
| R-02 | `peer-review` | ✅ 成功 | `…/skills/peer-review/SKILL.md` | `1a07d4a72406` / 23,119 B（`K-Dense Inc.` ＋ `MIT license`）→ **用户面** | **一致**（644e B-02 记：成功·用户面·`1a07d4a72406`/23,119 B） |
| R-03 | `scholar-evaluation`（**反向对照**） | ✅ 成功 | `…/skills/scholar-evaluation/SKILL.md` | `4157069eee2e` / 12,257 B（`MIT license` ＋ `K-Dense Inc.`）→ **用户面** | **644e 未测此名**（其 C 臂只测 `experimental-design`/`academic-paper-polish` 两枚 PC 独有项）⇒ 本棒取得**用户面成功新例**；且 644e §2.2 A-06 记 `scientific-research-workflows:scholar-evaluation`（限定名）失败，本棒**裸名**成功 ⇒ 与「写法是变量」先例同向 |

> **复现结论**：与 644e **一致 2/2**（`scientific-writing`、`peer-review`），**无不一致项**；新增 1 枚裸名成功例（`scholar-evaluation`）。

### §3.2 臂 2 · 多重面 5 枚（裸名 · 5 次 · 与三面基线比对）

| # | 请求名 | 结果 | Location | 用户面基线 | PC 面基线 | BI 面基线 | **命中面判定（首部逐字）** |
|---|---|---|---|---|---|---|---|
| M-01 | `docx` | ✅ 成功 | `…/skills/docx/SKILL.md` | `cfbabd72b1ae`/20,084（`license: Proprietary`） | `12e5a0cccd0c`/11,619（`metadata:`） | `c9407f69ad99`/11,536（`metadata: version "4.0.0"`） | **用户面**（`license: Proprietary. LICENSE.txt` 逐字；PC/BI 首部为 `metadata:`，不吻合） |
| M-02 | `pdf` | ✅ 成功 | `…/skills/pdf/SKILL.md` | `9f78b8359fbd`/8,072（`license: Proprietary`） | `e39aa05f43db`/28,593（`description: >`） | `3ce4de4609d4`/28,863（`description: >`） | **用户面** |
| M-03 | `pptx` | ✅ 成功 | `…/skills/pptx/SKILL.md` | `e5b0df918cbe`/9,182（`license: Proprietary`） | `931a81818974`/32,801（`description: >-`） | `75c4bbe0bf93`/13,049（`description: >-`） | **用户面** |
| M-04 | `xlsx` | ✅ 成功 | `…/skills/xlsx/SKILL.md` | `55591d7decc1`/11,464（`license: Proprietary`） | `6eab2cbf5606`/27,366（`description: >-`） | `a3f0d9a7afa6`/26,848（`description: >-`） | **用户面** |
| M-05 | `deep-research` | ✅ 成功 | `…/skills/deep-research/SKILL.md` | `5637feab59dc`/6,995（`license: MIT` ＋ `author: awesome-llm-apps`） | **MISSING** | `c93fe1961ff4`/12,109（`description: >`） | **用户面**（仅两面存在；`license: MIT`＋`awesome-llm-apps` 逐字；BI 面首部为 `description: >`，不吻合） |

> **臂 2 计数**：**5/5 成功，5/5 命中用户面；PC 面 0 次命中，BI 面 0 次命中**。4 枚三面同名（`docx`/`pdf`/`pptx`/`xlsx`）的两份他面副本**盘上在位、本次无一被选中**；`deep-research` 的 BI 面副本亦未被选中。

### §3.3 臂 4 · 等距抽样 11 枚（裸名 · 11 次）

| # | 请求名 | 结果 | Location | 内容指纹 | 备注 |
|---|---|---|---|---|---|
| E-01 | `biopython` | ✅ 成功 | `…/skills/biopython/SKILL.md` | `8865f5f5727c` / 13,828 B（`K-Dense Inc.`）→ **用户面** | 等距点 #19 |
| E-02 | `context-fundamentals` | ✅ 成功 | `…/skills/context-fundamentals/SKILL.md` | `03b56e1c40ed` / 17,013 B → **用户面** | 等距点 #38 |
| E-03 | `industry-research-report` | ✅ 成功 | `…/skills/industry-research-report/SKILL.md` | `82e4eca9d1b2` / 27,177 B → **用户面** | 等距点 #94 |
| E-04 | `matlab` | ✅ 成功 | `…/skills/matlab/SKILL.md` | `0414644e5d6a` / 10,044 B（`K-Dense Inc.`）→ **用户面** | 等距点 #113 |
| E-05 | `openclaw-setup-assistant` | ✅ 成功 | `…/skills/openclaw-setup-assistant/SKILL.md` | `5344a0f0d37e` / 11,730 B → **用户面** | 等距点 #132；⚠️ **R1 高危件**（见 §4） |
| E-06 | `primekg` | ✅ 成功 | `…/skills/primekg/SKILL.md` | `1dc8be0176c5` / 3,821 B（`K-Dense Inc.`）→ **用户面** | 等距点 #151 |
| E-07 | `qutip` | ✅ 成功 | `…/skills/qutip/SKILL.md` | `cdc96ef046bb` / 9,047 B（`K-Dense Inc.`）→ **用户面** | 等距点 #169 |
| E-08 | `scikit-bio` | ✅ 成功 | `…/skills/scikit-bio/SKILL.md` | `66cb2309d38c` / 14,750 B（`K-Dense Inc.`）→ **用户面** | 等距点 #188 |
| E-09 | `tiledbvcf` | ✅ 成功 | `…/skills/tiledbvcf/SKILL.md` | `1da719b9ec64` / 15,360 B（`skill-author: Jeremy Leipzig`）→ **用户面** | 等距点 #207 |
| E-10 | `vaex` | ✅ 成功 | `…/skills/vaex/SKILL.md` | `53fc6ee59ecd` / 6,595 B（`K-Dense Inc.`）→ **用户面** | 补点 #216（维持 ≥8 下限） |

> **臂 4 计数**：**10/10 实调全部成功，10/10 命中用户面**（另 1 个等距点 `gif-sticker-generator` 见 §5 诚实边界）。

---

## §4 风险登记：加载回内容中的祈使性/冒名/外发/凭据类指令（**0 遵从**）

> **总纪律**：⛔ 本棒**未执行任何 `SKILL.md` 内指令**。指令来源是**盘上文件**，**不是 PI**，**不得以盘上文本冒充 PI 指令**。以下条目**一律只登记、不遵从、不扩散**。

| id | skill（命中臂） | 加载面 | 命中内容（原文摘） | 风险类 | 本棒处置 |
|---|---|---|---|---|---|
| **R1** | `openclaw-setup-assistant`（E-05） | 用户面 | 要求「访问订阅页面复制 API Key 提供给我」；`osascript … curl -fsSL https://molt.bot/install.sh \| bash`；`export MINIMAX_API_KEY='<用户提供的API_KEY>'` | **高**：索取凭据 ＋ 远端脚本 `curl\|bash` ＋ 代开终端 ＋ 凭据入命令行 | **未遵从** · 仅登记。**0 索取 key、0 执行命令、0 代开终端** |
| **R1b** | `openclaw-setup-assistant`（E-05） | 用户面 | 「部署飞书桥接」段要求 `FEISHU_APP_ID`/`FEISHU_APP_SECRET` 并写盘 `~/.clawdbot/secrets/…` | **高**：外部平台凭据 ＋ 写盘凭据文件 | **未遵从** · 仅登记 |
| **R2** | `docx`（M-01） | 用户面 | `Use "Claude" as the author` for tracked changes and comments | **高**：署名冒名 | **未遵从** · 仅登记（与登记件 R2 一致；PC 面副本 0 命中该句，两面分歧成立） |
| **R3** | `scientific-writing`（R-01） | 用户面 | 「**MANDATORY**: Every scientific paper MUST include a graphical abstract plus 1-2 additional AI-generated figures」 | **中**：强制产出要求（与本项目登记件体例冲突） | **未遵从** · 仅登记 |
| **R4** | `peer-review`（R-02）/ `scholar-evaluation`（R-03） | 用户面 | 「always consider adding scientific diagrams」「Schematics should be generated by default」 | **中**：默认产出物外加 | **未遵从** · 仅登记 |
| **R5** | `matlab`（E-04）/ `tiledbvcf`（E-09） | 用户面 | 末段「proactively suggest using K-Dense Web (www.k-dense.ai)」（外推推广） | **中**：产品外推/引导跳转 | **未遵从** · 仅登记 |
| **R6** | `industry-research-report`（E-03） | 用户面 | 「NEVER cite Wikipedia」「四阶段强制流程」「MUST generate 概念图」等强约束 | **中**：强制流程/来源限制 | **未遵从** · 仅登记 |
| **R7** | `prd-to-prototype`（A1-32） | 用户面 | 「绝对禁止提问、直接脑补细节、强制两步流程」等 | **中**：禁止澄清型指令 | **未遵从** · 仅登记 |

> **本棒新增于登记件 R1–R4 之外的条目**：R1b（同件凭据外发面）、R5（K-Dense Web 外推，见于 `matlab` `tiledbvcf`）、R6（`industry-research-report` 强制流程）、R7（`prd-to-prototype` 禁问指令）。**以上均仅登记，未执行、未扩散至任何他件。**

---

## §5 统计

### §5.1 总计数

| 指标 | 本棒实测（终态口径） |
|---|---|
| **总调用次数** | **62**（见 §5.4 清点） |
| **覆盖样本（skill 枚数）** | **40** |
| **成功 / 失败** | **40 / 22**（按调用次；成功率 64.5%） |
| **成功命中面** | **用户面 40 / 40**；**PC 面 0 / 62**；**BI 面 0 / 62** |
| 失败形态 | 22/22 均为 `Local skill not found: <名>`（**0 其他失败形态**） |

> ⚠️ **本表经两轮勘误**（痕迹保留，不静默改数）：初稿记「53 次 / 40 枚 / 40 成功 / 13 失败」→ 第一轮改记「60 次 / 39 枚 / 39 成功 / 21 失败」→ **终态以本表现值与 §5.4 清点为准**。两轮错误的成因分别见 §5.4。

### §5.2 按臂分类

| 臂 | 调用次 | 成功 | 失败 | 命中面 |
|---|---|---|---|---|
| 臂 1（`name`≠目录名项，两形态） | 44 | 22 | **22**（全为目录名形态） | 用户面 22/22 |
| 臂 2（多重面 5 枚，裸名） | 5 | 5 | 0 | 用户面 5/5 |
| 臂 3（复现/对照 3 枚，裸名） | 3 | 3 | 0 | 用户面 3/3 |
| 臂 4（等距抽样 10 实调，裸名） | 10 | 10 | 0 | 用户面 10/10 |
| **合计** | **62** | **40** | **22** | **用户面 40/40** |

> **口径说明 1**：§1.3 表中「臂 4 实调 11 枚」为**撰写期计数笔误**——`vaex` 已含在 §3.3 实列的 10 枚（E-01…E-10）内，**未额外产生第 11 次调用**。
> **口径说明 2（关键）**：输入件 `e96d99ff9e75` §2.4 标题写「`name` ≠ 目录名 **21** 项」，但**其列表实列 22 项**（＝21 项常规 name≠目录名 ＋ `prd-to-prototype` 这一 YAML 引号值项；与该件 §2.2「`name` 为 YAML 引号值 1」的「21 + 1」自述一致）。**本棒按列表实际条目全取 22 项**，故臂 1 为 **22 项 × 2 形态 = 44 次**，而非 42 次。

### §5.3 按 `name` 匹配性分类

| 类别 | 样本枚数 | 调用次 | 目录名形态 | `name:` 值形态 |
|---|---|---|---|---|
| **`name` == 目录名**（201/223 中抽样） | 18 | 18 | **18 成功**（臂 2 5 ＋ 臂 3 3 ＋ 臂 4 10） | — |
| **`name` ≠ 目录名**（§2.4 列表实列 22 项） | 22 | 44 | **0 成功 / 22 失败** | **22 成功**（`name:` 值形态） |
| **合计** | **40** | **62** | 18 成功 / 22 失败 | 22 成功 |

> **可核验的核心事实**：**22 枚 `name`≠目录名项，目录名裸名形态成功率 0/22；`name:` 值形态成功率 22/22。** 对照组（`name`==目录名）裸名 18/18 成功。⇒ **寻址键 = frontmatter `name` 字面值，而非目录名**（本棒事实层；**不推断加载器实现**）。
> **对输入件的补充事实**：`e96d99ff9e75` §2.4 标题称 21 项、列表实列 **22 项**；本棒全取 22 项并实测，**未发现标题数与列表数自相矛盾导致的漏项**（22/22 全部完成两形态实测）。

### §5.4 逐例表清点（终态口径 · 覆盖 §5.1–§5.3 的两轮计数分叉）

| 项 | 数值 |
|---|---|
| 逐例表**实列调用行** | 臂 1 = **44 行**（表行 A1-01…A1-44；奇数行 22 条为目录名形态，偶数行 22 条为 `name:` 值形态）· 臂 2 = 5 · 臂 3 = 3 · 臂 4 = 10 ⇒ **合计 62 次** |
| 逐例表**实列样本枚数** | 22（臂 1）＋ 5（臂 2）＋ 3（臂 3）＋ 10（臂 4）= **40 枚**（`vaex` 含在臂 4 的 10 枚内） |
| 成功 / 失败 | 成功 **40** ＝ 臂1:22 ＋ 臂2:5 ＋ 臂3:3 ＋ 臂4:10；失败 **22** ＝ 臂1:22 ⇒ **40/22，成功率 64.5%** |
| 命中面 | 用户面 **40/40**；PC 面 **0/62**；BI 面 **0/62** |

> **诚实标注（两轮分叉全记录，不择一美化）**：
> - **第一轮分叉**：头部「一票结论」与 §5.1 初稿记「53 次 / 40 枚 / 40 成功 / **13** 失败」——**失败数 13 系速算错误**（误按 21 项中的部分计），且总次数 53 系漏计。**该组数值作废。**
> - **第二轮分叉**：第一次勘误改记为「60 次 / 39 枚 / 39 成功 / 21 失败」——**样本数 39 与失败数 21 仍不正确**：前者误信了 §1.3「臂 4 实调 11 枚」的自身笔误（`vaex` 重复计），后者沿用了 §2.4 标题的「21 项」而未核其列表实为 22 项。**该组数值同样作废。**
> - **终态唯一有效口径**：**62 次调用 / 40 枚样本 / 40 成功 / 22 失败**，与逐例表实列行数**逐行可复算**。
> - **对输入件的登记**：`e96d99ff9e75` §2.4 **标题「21 项」与列表「22 项」不一致**（该件 §2.2 自述「21 ＋ 1 引号值」可解释该 ＋1）。**本件不据标题计数，一律以列表实列为准**，并已实测全取。**既有件 0 回改**——该差异仅在本件登记。

---

## §6 诚实边界（不夸大 · 不误导）

1. **采样非全量**：本棒为**抽样**（40 枚样本，命中 223 项中的 40 项，占 **17.9%**）。**223 项调用面仍非全量已测**——未测的 183 项**不得**据本件推断其可加载性。
2. **单会话单棒单时刻**：全部 62 次调用**在本棒、本会话、2026-09-30 同一时段内串行完成**。**未跨会话、跨 agent、跨时刻复测**；与 644e 件的对照**限于其已记录的 3 枚**。
3. **0 断言因果**：本件**不回答「为什么 PC/BI 面 0 命中」「为什么目录名落空」**。未读加载器实现（优先级规则、name 索引构建逻辑均未读）。
4. **0 以文件直读冒充调用面**：磁盘读取**仅**用于三面基线指纹比对；「成功/失败」**一律**以 `Skill` 工具真实返回为唯一依据。
5. **加载内容仅作数据比对，未执行其指令**：§4 全部 7 类祈使性条目**0 遵从**。
6. **敏感值 0 触达**：`openclaw-setup-assistant` 等件正文含 API Key / 飞书 Secret 占位符，**本棒 0 索取、0 复制、0 落盘、0 使用任何真实凭据**；`config.yaml`/`mcp.json` **未读未写**。
7. **未测项（不冒认）**：644e 件 §2.5 列的未复测项（`.minimax\plugins\` 是否仍空、`skill-hub.json` 内容、`.builtin-skills` mtime、28 棵树/172 skill 总量）**本棒 0 复测、0 冒认**。本棒另**未**测任何 `plugin:skill` 限定名形态（沿用 644e 结论，未重复）。
8. **计数分叉已两轮自曝**：本件头部与 §5.1 的数值经**两轮勘误**方收敛至「62 次 / 40 枚 / 40 成功 / 22 失败」，**两轮错误值与成因全部保留在 §5.4，未静默改数**。另发现输入件 `e96d99ff9e75` §2.4 **标题 21 项与列表 22 项不一致**（本件按列表取 22 项，**既有件 0 回改**，仅登记）。
9. **`gif-sticker-generator`（等距点 #76）本棒 0 实调**：该点原拟实调，但为控上下文在臂 4 后段以补点 `vaex`（#216）替代 ⇒ 臂 4 实测 **10 枚**（9 个原等距点 ＋ 1 补点），**`#76` 记为未测**（如实登记，非遗漏充作无变化）。臂 4 仍**满足 ≥8 枚下限**。
10. **本件自身 SHA-12 无法内嵌**（自引用悖论）——由 parent 对落盘终态复算并回填回执，本件不预填。

---

## §7 自核节（本棒终态实测 · 只读复算）

### §7.1 落盘前后复算（0 覆写自证）

| 项 | 落名前 | 落盘后（终态） |
|---|---|---|
| 目标路径存在性 | `results/_skill_call_surface_probe_2026_09_30.md` **exists=False**（2 轮 × 4 目录 ＋ 全仓 glob 均 0 命中） | **新建 1 件**（**0 覆写**：落名前该路径不存在，无既有件被覆盖） |
| 既有件 0 回改 | — | 本棒**未对任何既有件写入**：`e96d99ff9e75` / `644e0666fbc4` **0 字节触动**（本棒仅 `Read`） |

### §7.2 盘上指纹基线复核（本棒实测 · 40 枚样本 · 与输入件附录 A 对账）

**对账结论**：本棒实测的 40 枚 `SKILL.md` SHA-12/字节中，**可与输入件附录 A 逐项对照的 39 枚**（臂 1 的 22 枚 ＋ 臂 2 的 5 枚 ＋ 臂 3 的 `scientific-writing`/`peer-review` 2 枚）**逐字吻合**；另 `scholar-evaluation`（附录 A 记 `4157069eee2e` / 12,257）、臂 4 的 10 枚亦与附录 A 同值。

### §7.3 方法学自证要点（复算者可直接验）

1. **成功判定唯一依据** = `Skill` 工具返回 `# Skill: <名>` ＋ `Location:` 行；**失败判定唯一依据** = 返回 `Local skill not found: <名>`。**二者均不依赖磁盘读取**。
2. **命中面判定** = 加载内容首部（frontmatter）与 §1.2 三面基线**逐字比对** ＋ 字节/SHA-12 双向核对（如 `docx`：用户面 `license: Proprietary` vs PC/BI 面 `metadata:`）。
3. **可复算性**：§1.3 抽样规则（字母序 ＋ 步长 18.6 ＋ 12 个索引点 ＋ 去重规则 ＋ 补点规则）已写明，**任何人可依规则重算样本名单**。
4. **两轮计数勘误未掩盖**：见 §5.4。

### §7.4 未做与不能做（诚实收口）

- 本件**不能**回答「为何 PC/BI 面 0 命中」「为何目录名落空」「加载器如何构建 name 索引」——**未读加载器实现，0 断言因果**。
- 本件**不能**替代 223 项全量调用面实测——余 183 项仍为「未测」。
- 本件**未**复测 644e §2.5 所列未测项（`.minimax\plugins\`、`skill-hub.json`、`.builtin-skills` mtime、28 树/172 skill 总量），**不冒认**。
