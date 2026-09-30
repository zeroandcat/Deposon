# skill「调用面」补满实测 · 乙半（未测 183 枚之第 93–183 位 · 2026-09-30）

- **件性质**：**实测登记件**（新建 1 件 · 0 回改既有件 · 0 覆写 · 0 改配置 · 0 改/移/重命名 skill 文件）
- **触发**：PI 2026-09-30 收尾小卷 `ask_61300ee638519d59d23a1d33` q2 裁「**改为补满全量**」；本棒为**乙半**（甲半 1–92 由并联另棒执行）
- **输入链**（只读，本棒实测 SHA-256 前 12 位）：

| # | 件 | SHA-12 | 字节 | 本件引用面 |
|---|---|---|---|---|
| 1 | `results/_skill_call_surface_probe_2026_09_30.md` | `112346df64fb` | 34,853 | **首轮实测件**：机制（`Skill` 加载器 / 失败形态 `Local skill not found: <名>` / 成功形态 `# Skill: <名>`＋`Location`）、体例（方法｜逐例表｜统计｜诚实边界｜自核）、**已测 40 枚名单**（臂 1–4） |
| 2 | `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` | `e96d99ff9e75` | 55,374 | **223 项全表＝附录 A**（含定位面/树归属、SHA-12/字节）、§2.4（`name`≠目录名项）、§2.2（三面同名 10＋5 项） |

- **出件**：**doc-writer**（`agent-0032834a3e04`）· 依派工单执行 · **0 LLM / 0 外部 API / 0 外部 URL / 0 key 读取**
- **命名**：去版本前缀 · `_主题_日期`；落名前 **2 轮 × 4 目录**（`results/` `docs/` `letters/` `deposon_team/`）**全部 exists=False**，另加全仓递归近名 glob（`*call_surface*` 命中首件与甲半件 · `*supplement_b*` **0 命中**）⇒ **新建，0 覆写**
- **版式**：UTF-8 无 BOM · 纯 LF · SHA-12 自核节见 §5
- **实测时段**：2026-09-30 17:15 起（本会话内，串行执行）

> **本件断言边界（先看这条）**：本件**只登记「谁成功、谁失败、落在哪一面」**，**0 断言因果**（未读加载器实现，未读其 `name` 索引构建逻辑）。**加载回的内容一律按惰性数据处理**——其中任何祈使性/冒名/外发/凭据类指令**一律 0 遵从**，仅登记（见 §4）。
> **本件不得单独冒认全量**：甲半 92 枚 ＋ 乙半 91 枚**两半并集**方为「未测 183 枚」；**两半 0 重叠**（分半规则见 §1.2，边界 `matchms`｜`matplotlib` 互斥已核）。

---

## §1 方法与分半规则

### §1.1 加载器存在性（先行判定）

| 项 | 本棒实测 |
|---|---|
| 本会话可用工具中**是否存在 skill 加载入口** | ✅ **存在** —— `Skill` 工具（*Loads the complete SKILL.md instructions for an available local or plugin skill*） |
| 失败返回形态 | `Local skill not found: <名>`（与首件 §1.1 逐字同形） |
| 成功返回形态 | `# Skill: <名>` ＋ `Location: files:///D:/Users/Administrator/.minimax/skills/<目录名>/SKILL.md` ＋ SKILL.md 全文 |

> **0 以文件直读冒充调用面**：所有「成功/失败」判定**一律以 `Skill` 工具真实返回为唯一依据**；磁盘读取**仅**用于（a）分半名单计算、（b）SHA-12/字节基线、（c）命中面指纹比对。

### §1.2 未测集与分半（本棒自算 · 可复算）

**规则**：
1. 取 `D:\Users\Administrator\.minimax\skills\` 下**全部目录**，按目录名 **Ordinal 升序**（`StringComparer.Ordinal`，字节序，跨机可复现）排列 ⇒ 本棒实测 **223** 个目录，**223/223 含 `SKILL.md`**（0 缺）。
2. 减去首件 `112346df64fb` **已测 40 枚**（臂 1 的 22 枚 `name`≠目录名项 ＋ 臂 2 的 5 枚多重面项 ＋ 臂 3 的 3 枚 ＋ 臂 4 的 10 枚）⇒ 本棒实测**已测 40 枚全部在盘**（`MEASURED_NOT_ON_DISK=0`）。
3. 得**未测 183 枚**；分半用前 **⌈183/2⌉ = 92** ⇒ **甲半 ＝ 第 1–92 位**（并联另棒）；**本棒（乙半）＝ 第 93–183 位（91 枚）**。

| 项 | 派工单预估 | **本棒实测** | 一致？ |
|---|---|---|---|
| 盘上目录总数 | 223 | **223** | ✅ |
| 含 `SKILL.md` | — | **223 / 223**（0 缺） | ✅ |
| 首轮已测 | 40 | **40**（0 重复、0 不在盘） | ✅ |
| 未测 | 183 | **183** | ✅ |
| 乙半枚数 | 91 | **91** | ✅ |

> **分半边界的可复算锚**：未测集 Ordinal 升序第 92 位 = **`matchms`**（甲半末位）· 第 93 位 = **`matplotlib`**（本棒首位）· 第 183 位 = **`zarr-python`**（本棒末位）——三者互异，**0 重叠 0 缺口**。
>
> ⚠️ **排序约定歧义的显式登记**：若改用 **InvariantCulture** 升序（PowerShell `Sort-Object` 默认口径），未测集有 **6 个位置**发生相邻对调（`dep-updates`↔`depmap` @40/41、`open-notebook`↔`openclaw-self-evolution-pack` @110/111、`torch-geometric`↔`torchdrug` @172/173），成因是文化排序忽略连字符（`'-'` 权重低于字母）。**本棒实测结论：该歧义 0 影响成员集合**——两种口径下**乙半 91 枚的成员集合逐项相同**（`SET_IDENTICAL=True`，`Compare-Object` 差异 0），**边界项 `matplotlib`/`zarr-python` 两口径一致**；仅集合**内部序号**在上述 2 对上互换。故分半**可复算且与排序约定无关**。

### §1.3 乙半 91 枚名单（本棒实测 · 逐字）

**名单枚数登记（供事后并集对账）**：**91 枚**目录名，逐字见 §2 表「请求名」列。
**frontmatter `name` 预检（只读，决定是否需第二形态）**：本棒对 91 枚**逐一按 frontmatter 边界（首个 `---` 至次个 `---`）解析 `name:` 行** ⇒ **91/91 的 `name` 值 == 目录名**，**0 枚 `name`≠目录名**、**0 枚解析失败** ⇒ 按派工单纪律**每枚单形态（目录名裸名）**，无「须加测 `name` 值形态」之项。
> 本棒 `frontmatter` 解析**不用**「前 N 行找 `name:`」的简化法：`minimax-docx` 的 frontmatter 以 `AIGC:` 块起头、`name:` 不在前 15 行，简化法会误报「无 `name` 键」。本棒改用**边界正则** `(?s)\A---\r?\n(.*?)\r?\n---` ＋ 块内 `(?m)^name:\s*(.+?)\s*$`，91/91 命中。

### §1.4 三面基线与命中面判定锚（只读 `Get-FileHash -Algorithm SHA256`）

本棒实测**三面盘上实况**（**不转述**依据件）：

| 面 | 路径 | 本棒实测 |
|---|---|---|
| **用户面** | `D:\Users\Administrator\.minimax\skills\` | **223** 目录 / 223 `SKILL.md` |
| **PC 面**（plugin-cache） | `D:\Users\Administrator\.minimax\v2\plugin-cache\official\` | **28** 棵 `sha256-tree-v1-*` 树 / **172** skill 条目 / 172 唯一名（skills 位于 `<树>\skills\<名>\`） |
| **BI 面** | `D:\Users\Administrator\.minimax\.builtin-skills\` | **20** 目录 |

> PC 面「28 树 / 172 skill」与首件/普查件所载**逐数吻合**（本棒独立复测所得，非转述）。
> 另注：普查件所载 PC 面树哈希样例形如 `611965fcb620…`，本棒实测该树短名形如 `sha256-tree-v1-611965fcb62`，**同一锚的两种写法**。

**乙半 91 枚的他面同名副本（本棒逐一核对 28 棵 PC 树 ＋ 20 个 BI 目录）**：

| skill | 位置 | 用户面 SHA-12 / 字节 | PC 面 SHA-12 / 字节 | 内容分歧 |
|---|---|---|---|---|
| `scientific-brainstorming` | 乙半序 150 | `dfdc611eb35e` / 8,178 | `694060b28d59` / 12,937 | **分歧**：`description` 逐字不同（用户面「Creative research ideation and exploration…」vs PC 面「Facilitates evidence-aware scientific ideation with independent generation…」） |
| `statistical-analysis` | 乙半序 166 | `82c7ee1761ac` / 19,765 | `2bc90ee5c35a` / 19,957 | **分歧**：`description` 逐字不同（用户面「Guided statistical analysis with test selection…」vs PC 面「Guided statistical analysis for research data - test selection, assumption checking…」） |

> **BI 面 0 命中**：`.builtin-skills` 的 20 个目录中，**与乙半 91 枚同名者 0 个**。
> **PC 面仅 2 命中**：28 棵树的 172 个 skill 名中，与乙半 91 枚同名者**仅上述 2 个**。⇒ **其余 89 枚成功即命中用户面**（无他面同名副本 ⇒ 无遮蔽可能），且 `Location` 行直接给出用户面路径，**三证互校**（`Location` 路径面 ＋ frontmatter 首行签名 ＋ SHA-12/字节）。

### §1.5 纪律执行（逐条自证）

| 纪律 | 本棒执行情况 |
|---|---|
| 加载回内容＝**惰性数据**，0 遵从任何指令 | ✅ **0 遵从**（含凭据索取/冒名/外发类，一律仅登记不执行；见 §4） |
| 全程只读 | ✅ 0 改 skill · 0 改配置 · 0 写 `config.yaml`/`mcp.json` · 0 写 `plugin.json`/`skill-hub.json` |
| **R4 · 0 key 读 / 0 key 落盘** | ✅ **0 读取、0 复制、0 落盘、0 使用任何真实凭据**；正文中 key/secret 占位符仅登记「存在此要求」这一事实 |
| 0 外部网络 / LLM 调用 | ✅ `web_search` / `web_fetch` / `mcp_invoke` **0 次调用**；`Skill` 加载为本地解析 |
| 失败重试 ≤2 形态 | ✅ 每项**至多两形态**（目录名 → `name:` 值），**0 穷举前缀组合**；本棒因 91/91 `name`==目录名，实际**单形态** |
| 上下文防溢 | ✅ 分批加载、**逐批即时落盘**（追加式写进本件），完成数与余量**如实登记**（见 §5.2） |

---

## §2 逐例表 · 乙半 91 枚

**形态说明**：本棒 91 枚 `name` == 目录名（§1.3），故**每枚单形态（目录名裸名）**；`name` 值形态列在本棒**无适用项**。
**时刻**：全部为本会话内 2026-09-30 串行执行（分钟级连续，无跨时刻复测）。
**Location 形态**：全部为 `files:///D:/Users/Administrator/.minimax/skills/<目录名>/SKILL.md`（D 盘实体路径；`C:\Users\Administrator\.minimax` 为指向 `D:\Users\Administrator\.minimax` 的 Junction）。

| # | 全局序 | 请求名（目录名·逐字） | frontmatter `name` | 结果 | 失败原文 | 命中面（首行签名／字节与哪面吻合） | 时刻 |
|---|---|---|---|---|---|---|---|

| 93 | 93 | `matplotlib` | `matplotlib` | ✅ 成功 | — | **用户面**；`100faa8c78a2` / 11,453 B（首行签名 `--- / name: matplotlib / description: Low-level plotting library…` ＋ `license: https://github.com/matplotlib/matplotlib/tree/main/LICENSE` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批A |
| 94 | 94 | `mckinsey-presentation-generator` | `mckinsey-presentation-generator` | ✅ 成功 | — | **用户面**；`5e56adf71927` / 40,319 B（首行签名 `--- / name: … / description: "McKinsey consulting-style multi-page HTML presentation generator…"` **引号值**；**无 license/metadata 行**；含 `Workflow (MANDATORY ORDER — No Skipping Steps)`；无他面同名副本）⚠️ 风险件（见 §4 R-B1） | 批A |
| 95 | 95 | `medchem` | `medchem` | ✅ 成功 | — | **用户面**；`9790fdc38680` / 10,152 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批A |
| 96 | 96 | `memory-systems` | `memory-systems` | ✅ 成功 | — | **用户面**；`9e2b38ffe947` / 16,554 B（`description: "This skill should be used for persistent semantic memory…"` **引号值**；**无 license/metadata 行**；末节 `## Skill Metadata` `Version: 4.1.0`；无他面同名副本） | 批A |
| 97 | 97 | `minimax-docx` | `minimax-docx` | ✅ 成功 | — | **用户面**；`15f4b45ef41b` / 16,366 B（**首行签名以 `AIGC:` 起头**：`ContentProducer: Minimax Agent AI` / `Label: AIGC` / `ProduceID` / `ReservedCode1,2` hex 串；`name:` 键位于**块尾**而非首位 ＋ `description: \|` ＋ `license: MIT` ＋ `metadata: author: MiniMaxAI` ＋ `triggers:` 含中文词「文档/报告/合同/公文/排版/套模板」；无他面同名副本）⚠️ 风险件（见 §4 R-B2） | 批B |
| 98 | 98 | `minimax-pdf` | `minimax-pdf` | ✅ 成功 | — | **用户面**；`8b0497ddd27d` / 8,624 B（`description: >` **折叠块**（CREATE/FILL/REFORMAT 三路）＋ `license: MIT` ＋ `metadata: version: "1.0" / category: document-generation`；无他面同名副本）⚠️ 弱风险（见 §4 R-B3） | 批B |
| 99 | 99 | `minimax-xlsx` | `minimax-xlsx` | ✅ 成功 | — | **用户面**；`4ffb70af6ccd` / 8,398 B（`description: "Open, create, read, analyze, edit, or validate Excel/spreadsheet files…"` **引号值** ＋ `license: MIT` ＋ `metadata: version: "1.0" / category: productivity`；无他面同名副本）⚠️ 风险件（见 §4 R-B4） | 批B |
| 100 | 100 | `ml-paper-writing` | `ml-paper-writing` | ✅ 成功 | — | **用户面**；`2544fcd5575f` / 35,572 B（**frontmatter 形态又异**：`version: 1.0.0` ＋ `author: Orchestra Research` ＋ `license: MIT` ＋ `tags: [...]` ＋ `dependencies: [semanticscholar, arxiv, habanero, requests]`；**无 `metadata:` 块**；无他面同名副本）⚠️ 风险件（见 §4 R-B5） | 批B |

| 101 | 101 | `modal` | `modal` | ✅ 成功 | — | **用户面**；`2dde37f532b1` / 12,413 B（`license: Apache-2.0` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B6） | 批C |
| 102 | 102 | `molecular-dynamics` | `molecular-dynamics` | ✅ 成功 | — | **用户面**；`39610e686445` / 14,700 B（`license: MIT` ＋ `skill-author: Kuan-lin Huang`；无他面同名副本） | 批C |
| 103 | 103 | `molfeat` | `molfeat` | ✅ 成功 | — | **用户面**；`b3155763a7e5` / 14,810 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批C |
| 104 | 104 | `multi-agent-patterns` | `multi-agent-patterns` | ✅ 成功 | — | **用户面**；`786ff9345eb4` / 18,649 B（`description: "This skill should be used when designing multi-agent systems…"` **引号值**；**无 license/metadata 行**；末节 `## Skill Metadata` `Version: 2.1.0`；无他面同名副本） | 批C |
| 105 | 105 | `networkx` | `networkx` | ✅ 成功 | — | **用户面**；`9c8fa590462f` / 12,713 B（`license: 3-clause BSD license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批C |
| 106 | 106 | `neurokit2` | `neurokit2` | ✅ 成功 | — | **用户面**；`330233a77582` / 12,019 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批C |
| 107 | 107 | `neuropixels-analysis` | `neuropixels-analysis` | ✅ 成功 | — | **用户面**；`ca82a34bb4cb` / 11,550 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B7） | 批C |
| 108 | 108 | `novel-writing-expert` | `novel-writing-expert` | ✅ 成功 | — | **用户面**；`badd76befdb2` / 3,051 B（`description: "专业的小说创作助手…Trigger keywords: 小说, 写作, 创作…"` **中文引号值**；**无 license/metadata 行**；无他面同名副本） | 批C |

| 109 | 109 | `omero-integration` | `omero-integration` | ✅ 成功 | — | **用户面**；`1d021d13e4bb` / 8,043 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险（见 §4 R-B8） | 批D |
| 110 | 110 | `open-notebook` | `open-notebook` | ✅ 成功 | — | **用户面**；`a8d5cc801b08` / 10,451 B（`license: MIT` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B9，**与普查件 R4 同面复核成立**） | 批D |
| 111 | 111 | `openclaw-self-evolution-pack` | `openclaw-self-evolution-pack` | ✅ 成功 | — | **用户面**；`bf156e00a517` / 2,726 B（首行签名 **`--- / description: <中文> / name: openclaw-self-evolution-pack`**——**`description` 在 `name` 之前**，与多数件相反；**无 license/metadata 行**；无他面同名副本）⛔ **高危件（见 §4 R-B10，本棒最重发现）** | 批D |
| 112 | 112 | `opentrons-integration` | `opentrons-integration` | ✅ 成功 | — | **用户面**；`27c87a247fa2` / 14,720 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批D |
| 113 | 113 | `paper-2-web` | `paper-2-web` | ✅ 成功 | — | **用户面**；`994429004860` / 16,446 B（`allowed-tools: Read Write Edit Bash` ＋ `license: Unknown` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B11） | 批D |
| 114 | 114 | `paper-lookup` | `paper-lookup` | ✅ 成功 | — | **用户面**；`a08c1c3999b3` / 10,150 B（**frontmatter 仅 `name` ＋ `metadata.skill-author`，全无 `license:` 键**；无他面同名副本）⚠️ 风险件（见 §4 R-B12） | 批D |
| 115 | 115 | `parallel-web` | `parallel-web` | ✅ 成功 | — | **用户面**；`5d3941e6754d` / 11,656 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ **`compatibility: PARALLEL_API_KEY required`** ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B13） | 批D |

| 116 | 116 | `pathml` | `pathml` | ✅ 成功 | — | **用户面**；`a16f701903ea` / 7,366 B（`license: GPL-2.0 license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批E |
| 117 | 117 | `pennylane` | `pennylane` | ✅ 成功 | — | **用户面**；`7ad9eb1a8c8f` / 7,396 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批E |
| 118 | 118 | `perplexity-search` | `perplexity-search` | ✅ 成功 | — | **用户面**；`6f42d1777cfd` / 14,084 B（`license: MIT license` ＋ **`compatibility: An OpenRouter API key is required to use Perplexity search`** ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B14） | 批E |
| 119 | 119 | `phylogenetics` | `phylogenetics` | ✅ 成功 | — | **用户面**；`ecea8ee3b168` / 13,914 B（`license: Unknown` ＋ `skill-author: Kuan-lin Huang`；无他面同名副本） | 批E |
| 120 | 120 | `plotly` | `plotly` | ✅ 成功 | — | **用户面**；`608e857e4e50` / 7,198 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批E |
| 121 | 121 | `polars` | `polars` | ✅ 成功 | — | **用户面**；`b7839f79ef81` / 9,430 B（**`license:` 为 URL 形态** `https://github.com/pola-rs/polars/blob/main/LICENSE` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批E |
| 122 | 122 | `polars-bio` | `polars-bio` | ✅ 成功 | — | **用户面**；`496d3cf7a9b6` / 14,052 B（**`license:` 亦为 URL 形态** `https://github.com/biodatageeks/polars-bio/blob/main/LICENSE` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批E |
| 123 | 123 | `pptx-generator` | `pptx-generator` | ✅ 成功 | — | **用户面**；`6eeb36239fde` / 7,930 B（`description: "Generate, edit, and read PowerPoint presentations…"` 引号值 ＋ `license: MIT` ＋ `metadata: version: "1.0" / category: productivity / sources: [<2 条 URL>]`；**无 `skill-author` 键**；无他面同名副本）⚠️ 弱风险（见 §4 R-B15） | 批E |
| 124 | 124 | `pptx-posters` | `pptx-posters` | ✅ 成功 | — | **用户面**；`155059d3230d` / 14,145 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B16） | 批E |

| 125 | 125 | `project-development` | `project-development` | ✅ 成功 | — | **用户面**；`acfeda3048cf` / 18,960 B（`description: "This skill should be used for project-level decisions about LLM-powered systems…"` 引号值；**无 license/metadata 行**；末节 `## Skill Metadata` `Version: 1.3.0`；无他面同名副本） | 批F |
| 126 | 126 | `proof-writer` | `proof-writer` | ✅ 成功 | — | **用户面**；`6d7b3094711f` / 7,594 B（`description` 含中文触发词「补全证明 / 写证明 / 证明某个命题」 ＋ **`argument-hint: [theorem-statement-and-assumptions]`** ＋ `allowed-tools: Read, Write, Edit, Grep, Glob`；**无 `license:` 键、无 `metadata` 块**；无他面同名副本）⚠️ 弱风险（见 §4 R-B17：默认写入 `PROOF_PACKAGE.md`） | 批F |
| 127 | 127 | `protocolsio-integration` | `protocolsio-integration` | ✅ 成功 | — | **用户面**；`f7d45c56cce4` / 14,899 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B18） | 批F |
| 128 | 128 | `pufferlib` | `pufferlib` | ✅ 成功 | — | **用户面**；`736d917b1a67` / 13,500 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批F |
| 129 | 129 | `pydeseq2` | `pydeseq2` | ✅ 成功 | — | **用户面**；`1a4875f66800` / 16,165 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批F |
| 130 | 130 | `pydicom` | `pydicom` | ✅ 成功 | — | **用户面**；`4ff0bc8b41d1` / 13,188 B（**`license:` 为 URL 形态** `https://github.com/pydicom/pydicom/blob/main/LICENSE` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险（见 §4 R-B19：PHI 匿名化面） | 批F |

| 131 | 131 | `pyhealth` | `pyhealth` | ✅ 成功 | — | **用户面**；`86d66ea09565` / 17,652 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险（见 §4 R-B20：临床/PHI 面） | 批G |
| 132 | 132 | `pylabrobot` | `pylabrobot` | ✅ 成功 | — | **用户面**；`d78a82ad4c0d` / 8,193 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批G |
| 133 | 133 | `pymatgen` | `pymatgen` | ✅ 成功 | — | **用户面**；`57ff1b1bf0f8` / 20,033 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险（见 §4 R-B21：`MP_API_KEY`） | 批G |
| 134 | 134 | `pymc` | `pymc` | ✅ 成功 | — | **用户面**；`abee8e33c64d` / 15,779 B（**`license: Apache License, Version 2.0`**——第三种许可证措辞变体 ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批G |
| 135 | 135 | `pymoo` | `pymoo` | ✅ 成功 | — | **用户面**；`37571351035e` / 16,752 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批G |

| 136 | 136 | `pyopenms` | `pyopenms` | ✅ 成功 | — | **用户面**；`ded0610c2990` / 5,628 B（**`license: 3 clause BSD license`**——第四种许可证措辞变体 ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批H |
| 137 | 137 | `pysam` | `pysam` | ✅ 成功 | — | **用户面**；`790ec1a74c2a` / 9,994 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险（基因组/GDS 面） | 批H |
| 138 | 138 | `pytdc` | `pytdc` | ✅ 成功 | — | **用户面**；`69155d4b3586` / 12,699 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批H |
| 139 | 139 | `pytorch-lightning` | `pytorch-lightning` | ✅ 成功 | — | **用户面**；`7bdecc78dcdf` / 6,674 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批H |
| 140 | 140 | `pyzotero` | `pyzotero` | ✅ 成功 | — | **用户面**；`a8b4fd9a7788` / 4,398 B（`allowed-tools: Read Write Edit Bash` ＋ **`license: MIT License`**（首字母大写变体）＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B22） | 批H |

| 141 | 141 | `qiskit` | `qiskit` | ✅ 成功 | — | **用户面**；`21b8dc60d69b` / 8,754 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险（IBM Quantum API token 面，**本棒 0 取用**） | 批I |
| 142 | 142 | `rdkit` | `rdkit` | ✅ 成功 | — | **用户面**；`0fe28d387eaa` / 20,420 B（**`license: BSD-3-Clause license`**——连字符变体 ＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批I |
| 143 | 143 | `reasoning-trace-optimizer` | `reasoning-trace-optimizer` | ✅ 成功 | — | **用户面**；`6d330b7afc13` / 6,359 B（`description: "Debug and optimize AI agents by analyzing reasoning traces…"` **引号值**；**无 `license:` 键**；`## Skill Metadata` 署 `Author: Muratcan Koylan` / `Powered by: MiniMax M2.1` / `Partnership: Built in collaboration with MiniMax AI`；无他面同名副本）⚠️ 风险件（见 §4 R-B23：含「Optionally update the system prompt」自我修改指令） | 批I |
| 144 | 144 | `research-grants` | `research-grants` | ✅ 成功 | — | **用户面**；`b062ef2bab28` / 37,215 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B24：强制 AI 生图 mandate） | 批I |
| 145 | 145 | `research-lookup` | `research-lookup` | ✅ 成功 | — | **用户面**；`f917e638fb9b` / 16,232 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ **`compatibility: PARALLEL_API_KEY and OPENROUTER_API_KEY required`** ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B25） | 批I |

| 146 | 146 | `rowan` | `rowan` | ✅ 成功 | — | **用户面**；`9690cf9dbe3c` / 12,510 B（**`license: Proprietary (API key required)`**——本棒**首个专有许可证声明** ＋ `compatibility: API required` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B26：`ROWAN_API_KEY` ＋ 云端计算 ＋ K-Dense Web 推广段） | 批J |
| 147 | 147 | `run-summary` | `run-summary` | ✅ 成功 | — | **用户面**；`a7947ff90b84` / 3,442 B（`description: "Append a well-formed run summary to logs/agent-history.md after every agent pass. Shared by all agents."`；**无 `license:` 键、无 `metadata` 块**；无他面同名副本）⛔ **行为覆写件（见 §4 R-B27，本棒第二重要发现）** | 批J |
| 148 | 148 | `sales-powermap` | `sales-powermap` | ✅ 成功 | — | **用户面**；`63c47170da42` / 23,226 B（`description: "智能销售助手：从模糊意图出发…触发词：卖、客户、power map、决策人、组织架构"` 中文引号值；**无 `license:` 键、无 `metadata` 块**；无他面同名副本）⛔ **个人数据采集件（见 §4 R-B28）** | 批J |
| 149 | 149 | `scanpy` | `scanpy` | ✅ 成功 | — | **用户面**；`c93a0bfa855f` / 11,322 B（**`license: SD-3-Clause license`**——字面作 `SD-3-Clause`（疑为 `BSD-3-Clause` 之误，**如实记录不代为更正**）＋ `skill-author: K-Dense Inc.`；无他面同名副本） | 批J |
| 150 | 150 | `scientific-brainstorming` | `scientific-brainstorming` | ✅ 成功 | — | **用户面（三面比对实测，非仅凭 Location）**；`dfdc611eb35e` / 8,178 B。**本棒 PC 面同名项之一**：加载回 `description` 逐字为「Creative research ideation and exploration. Use for open-ended brainstorming sessions…」＝**用户面基线**；**不吻合 PC 面基线**「Facilitates evidence-aware scientific ideation with independent generation…」（`694060b28d59` / 12,937 B） | 批J |

| 151 | 151 | `scientific-critical-thinking` | `scientific-critical-thinking` | ✅ 成功 | — | **用户面**；`df53105c317a` / 23,704 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险（默认生图 mandate） | 批K |
| 152 | 152 | `scientific-schematics` | `scientific-schematics` | ✅ 成功 | — | **用户面**；`88224e248c1e` / 23,848 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 风险件（见 §4 R-B29）——**本棒「强制调用型」枢纽件** | 批K |
| 153 | 153 | `scientific-slides` | `scientific-slides` | ✅ 成功 | — | **用户面**；`27db363932fd` / 47,290 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.`；无他面同名副本）⛔ **署名默认件（见 §4 R-B30）** | 批K |

| 154 | 154 | `scientific-visualization` | `scientific-visualization` | ✅ 成功 | — | **用户面**；`981bfae95f31` / 25,527 B（`license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`；**无 `allowed-tools:` 键**；无他面同名副本）⚠️ 弱风险（绘图/出图链，无凭据与外发指令） | 批L |
| 155 | 155 | `scikit-learn` | `scikit-learn` | ✅ 成功 | — | **用户面**；`7658a0d3a6d2` / 15,532 B（`license: BSD-3-Clause license` ＋ `metadata.skill-author: K-Dense Inc.`；无 `allowed-tools:` 键；无他面同名副本） | 批L |
| 156 | 156 | `scikit-survival` | `scikit-survival` | ✅ 成功 | — | **用户面**；`7674199a2bc0` / 15,077 B（`license: GPL-3.0 license` ＋ `metadata.skill-author: K-Dense Inc.`；无 `allowed-tools:` 键；无他面同名副本）⚠️ 许可为 GPL-3.0（copyleft 面，与多数 MIT/BSD 件不同类） | 批L |
| 157 | 157 | `scvelo` | `scvelo` | ✅ 成功 | — | **用户面**；`8a83fbc44689` / 10,288 B（`license: BSD-3-Clause`（**裸键值，无 "license" 后缀**）＋ `metadata.skill-author: Kuan-lin Huang`；**非 K-Dense 作者**；无 `allowed-tools:` 键；无他面同名副本） | 批L |
| 158 | 158 | `scvi-tools` | `scvi-tools` | ✅ 成功 | — | **用户面**；`1909d968193a` / 7,238 B（`license: BSD-3-Clause license` ＋ `metadata.skill-author: K-Dense Inc.`；无 `allowed-tools:` 键；无他面同名副本）⚠️ 本棒**最小件**（7.2 KB），且系 GPU/单细胞重依赖件 | 批L |

| 159 | 159 | `seaborn` | `seaborn` | ✅ 成功 | — | **用户面**；`613d07dc7fcf` / 19,600 B（`license: BSD-3-Clause license` ＋ `metadata.skill-author: K-Dense Inc.`；无 `allowed-tools:` 键；无他面同名副本）纯文档件（`references/` 三册 ＋ 无凭据/无外发/无写盘 mandate） | 批M |
| 160 | 160 | `self-improvement-loops` | `self-improvement-loops` | ✅ 成功 | — | **用户面**；`699926720701` / 22,244 B（**无 `license:` 键 ＋ 无 `metadata:` 块**，仅 `name`/`description`；作者改由末节 `## Skill Metadata` 记为 `Agent Skills for Context Engineering Contributors`；**本棒第 3 个非 K-Dense 作者**）⛔ **自修改 doctrine 件（见 §4 R-B31）**：正文以「harness 自身即被优化对象」为纲，明列「bounded self-edits / Self-Harness / Darwin Godel Machine」等自我改写阶梯，并写入「Constraints stated in prompt text get evolved away…」等祈使句；**0 遵从**（未改任何 skill/配置） | 批M |
| 161 | 161 | `seo-geo-optimizer` | `seo-geo-optimizer` | ✅ 成功 | — | **用户面**；`40d89aa0e11f` / 51,482 B（`license: Apache-2.0`；`metadata` 用 **`author:`（非 `skill-author:`）＋ `version: "2.0.0"` ＋ `source: https://github.com/aaron-he-zhu/seo-geo-claude-skills` ＋ `tags:` 数组**——与 K-Dense 族键位显著不同）；**第三方来源件**（正文含 `Copyright 2024-2025 Aaron He Zhu` 独立版权行）⚠️ 弱风险（0 凭据/0 硬联网 mandate，仅「With SEO tools connected」条件式表述）⚠️ **未标出处的量化断言**（「Number in title +20-30%」「Brackets +38%」等 CTR 影响表） | 批M |

| 162 | 162 | `shap` | `shap` | ✅ 成功 | — | **用户面**；`8c950c3852da` / 18,412 B（`license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险：安装节含 `uv pip install shap` / `uv pip install -U shap`，「For Production」节含 `joblib.dump(explainer,'explainer.pkl')` 落盘示例（均在代码块/建议语境内，**非祈使 mandate**）；0 遵从 | 批N |
| 163 | 163 | `simpy` | `simpy` | ✅ 成功 | — | **用户面**；`73be2e0f1ce5` / 12,164 B（`license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）纯文档件（0 凭据/0 外发/0 落盘 mandate；`monitor.export_csv('results.csv')` 为代码块示例） | 批N |
| 164 | 164 | `skill-template` | `skill-template` | ✅ 成功 | — | **用户面**；`664c93838ff8` / 5,163 B（**无 `license:` 键 ＋ 无 `metadata:` 块**，仅 `name`/`description`；本棒**最小件**）⛔ **语料库模板件（见 §4 R-B32）**：正文指示「使用本模板创建新 Agent Skill」并要求「add or update a record in `researcher/mechanisms/registry.jsonl`」——**写入语料库的动作指令，与本棒 0 写盘纪律直接冲突，0 遵从**；⚠️ 受众表述跨供应商（正文以 `Claude` 为默认受众「Default assumption: Claude is already very smart」，而宿主为 MiniMax Code）——**如实登记，不代为更正** | 批N |
| 165 | 165 | `stable-baselines3` | `stable-baselines3` | ✅ 成功 | — | **用户面**；`3a3b3f98ff23` / 9,506 B（`license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）⚠️ 弱风险：`uv pip install stable-baselines3` 安装命令 ＋ `model.save()`/`vec_env.save('vec_normalize.pkl')`/`tensorboard_log="./tensorboard/"` 落盘示例（代码块内）；含跨件路由（并行/多智能体场景指向 `pufferlib`） | 批N |
| 166 | 166 | `statistical-analysis` | `statistical-analysis` | ✅ 成功 | — | **用户面**；`82c7ee1761ac` / 19,765 B（`license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`；**PC 面存在同名副本** `2bc90ee5c35a` / 19,957 B，树 `sha256-tree-v1-1965fcb6208a…`）✅ **三面比对完成**：加载回 `description` 逐字为「Guided statistical analysis **with test selection and reporting**…」，吻合**用户面**基线，**不吻合** PC 面（「…**for research data** - test selection, assumption checking…」）⇒ **命中用户面**（本棒第 2 枚 PC 同名项，判定不依赖 `Location`）。纯文档件；Best Practices #1 即「**Pre-register analyses**」（与本项目预登记纪律同向）；0 遵从 | 批N |

| 168 | 168 | `stock-financial-analysis` | `stock-financial-analysis` | ✅ 成功 | — | **用户面**；`d62b28fd2c48` / **1,949 B（本棒最小件）**（**无 `license:` 键 ＋ 无 `metadata:` 块 ＋ 无作者**，仅 `name`/`description`；中文件）⚠️ **「薄壳」件**：正文给出「短线交易/筹码分布/**买入卖出信号参考**/基本面/估值」五类分析与「工作流程」，但**未给出任何数据源、接口、脚本或参数**（`数据收集 – 获取相关股票信息和财务数据` 为空壳描述）⇒ **可加载但不可执行**；⚠️ 投资建议面（附「不构成投资建议」「市场有风险」免责声明）；0 遵从 | 批O |
| 174 | 174 | `transformers` | `transformers` | ✅ 成功 | — | **用户面**；`b2753065e1e1` / 5,083 B（`license: Apache-2.0 license` ＋ **`compatibility: Some features require an Huggingface token`** ＋ `metadata.skill-author: K-Dense Inc.`）⛔ **凭据面（见 §4 R-B34）**：专设「## Authentication」节，指示 `huggingface_hub.login()` 交互式取 token ＋ `export HUGGINGFACE_TOKEN="your_token_here"` ＋ 指向 `huggingface.co/settings/tokens` 领取页；另含 `uv pip install torch transformers datasets evaluate accelerate` 安装面 ＋ `output_dir="./results"` 落盘路径；**0 遵从**（未读/未设/未落盘任何 token，0 联网） | 批O |
| 177 | 177 | `usfiscaldata` | `usfiscaldata` | ✅ 成功 | — | **用户面**；`1260dc9c5f05` / 7,297 B（`license: MIT`（**裸**）＋ `metadata.skill-author: K-Dense Inc.`）⚠️ 外部网络面：`requests.get('https://api.fiscaldata.treasury.gov/services/api/fiscal_service/…')`；✅ **显式声明「No API key or registration required」**（本棒唯一**明文否认凭据需求**的件，0 key 面）；⚠️ 末尾「Suggest Using K-Dense Web」推广段（`www.k-dense.ai`，见 §4 R-B37 归并项）；**0 遵从**（0 联网） | 批O |
| 178 | 178 | `venue-targeting` | `venue-targeting` | ✅ 成功 | — | **用户面**；`d080a43e7ca0` / 8,038 B（**无 `license:` 键 ＋ 无 `metadata:` 块 ＋ 无作者**）⛔ **写盘面（见 §4 R-B35）**：指示「copy the active venue state into `project.yaml`」并给出 YAML 块（`target_venue`/`backup_venues`/`venue_family`/`publication_bar`/`loop_history`）＋「store venue choice in `notes/gap_briefs/<slug>.md`」；⚠️ 与 `workspace-setup` 属**同一异构学术项目 schema 族**（`project.yaml` / `mode: project` / `notes/…`），**与本仓 deposon 布局不一致**；0 遵从 | 批O |
| 180 | 180 | `what-if-oracle` | `what-if-oracle` | ✅ 成功 | — | **用户面**；`6696e69bfae3` / 9,481 B（**`allowed-tools: Read Write`** ＋ `license: MIT license` ＋ `metadata.skill-author: AHK Strategies (ashrafkahoush-ux)`＝**本棒第 4 个非 K-Dense 作者**）⛔ **写权限声明面**：frontmatter 直接声明 `Read Write`（若被宿主采纳即为写权限扩面）——**本棒 0 采纳**；⚠️ 第三方产品外链（`ahkstrategies.net`、`themindbook.app`）；⚠️ **文件内自述 DOI 引用**（`10.5281/zenodo.18736841`、`10.5281/zenodo.18807387`）与「黄金比例 61.8/38.2 源自自然分支」等**未标出处断言**——**如实登记为「文件内自述，本棒 0 联网核验」，不代为背书**；0 遵从 | 批O |
| 181 | 181 | `workspace-setup` | `workspace-setup` | ✅ 成功 | — | **用户面**；`910e2aac66b7` / 2,927 B（**无 `license:` 键 ＋ 无 `metadata:` 块 ＋ 无作者**）⛔ **强制首触执行件（见 §4 R-B33）**：正文开篇即「Run this skill at the start of **every** command invocation, before reading any project artifacts or dispatching any agent」，并规定 `projects/active/<slug>/` 异构 schema 的 5 个必读件（`project.yaml` / `notes/overview.md` / `literature/map.md` / `conjectures/conjectures.md` / `models/model_v<current>.md`）＋「refuse immediately」「Ask the user」「Abort, report the path」等越权处置语；**0 遵从**（未按其 schema 读任何文件、未 dispatch 任何 agent） | 批O |
| 182 | 182 | `xiaohongshu-collector` | `xiaohongshu-collector` | ✅ 成功 | — | **用户面**；`a6f28381cbff` / 9,099 B（**无 `license:` 键 ＋ 无 `metadata:` 块 ＋ 无作者**；中文件）⛔⛔ **本棒最重风险件之一（见 §4 R-B36）**：①「⚠️ 核心执行规则（必须遵守）」**明文覆写宿主工具选择**（「**绝对禁止**使用任何外部搜索引擎」「**绝对禁止**使用 `batch_web_search`、`WebSearch` 或任何网页搜索工具」）——与 R-B13 同族；② 指示**用浏览器工具直接操作** `www.xiaohongshu.com` 全量爬取第三方 UGC（笔记正文、**全部图片文字（OCR）**、**下拉加载全部评论**、用户昵称），并以「原文至上」「宁多勿少」「穷尽式搜索」「不遗漏任何可能有价值的信息」驱动最大化采集；③ **规避反爬表述**：「如遇到访问限制，适当降低操作频率」「如遇到登录弹窗…尝试关闭继续操作」；**0 遵从**（0 浏览器操作、0 访问该站、0 联网、0 采集任何用户数据） | 批O |

| 169 | 169 | `sympy` | `sympy` | ✅ 成功 | — | **用户面**；`0c8dd6903b44` / 13,466 B（`license: https://github.com/sympy/sympy/blob/master/LICENSE`＝**URL 形态许可** ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）纯文档件（0 凭据/0 外发/0 落盘 mandate；`docs.sympy.org` 为参考链接非抓取 mandate） | 批P |
| 171 | 171 | `tool-design` | `tool-design` | ✅ 成功 | — | **用户面**；`14f5a12b6911` / 20,089 B（**无 `license:` 键 ＋ 无 `metadata:` 块**；作者改由末节 `## Skill Metadata` 记为 `Agent Skills for Context Engineering Contributors`（**与 R-B31 同署**，本棒第 2 处），`Version: 2.2.0`，Created 2025-12-20 / Last Updated 2026-05-15）⛔ **自修改邻接面（见 §4 R-B40）**：「Using Agents to Optimize Tools」模式要求把工具失败样本喂给 agent（`get_agent_response(prompt)`）**由 agent 改写工具描述**；⚠️ 文件内自述外部案例（`claim-tool-design-vercel-d0-reduction`、Vercel d0）**本棒 0 联网核验**；0 遵从（0 spawn agent、0 改任何工具描述） | 批P |
| 172 | 172 | `torch-geometric` | `torch-geometric` | ✅ 成功 | — | **用户面**；`375c1aa1e52d` / 17,059 B（**无 `license:` 键 ＋ 无 `metadata:` 块 ＋ 无作者**）⚠️ 弱风险：安装节用 **`uv add torch_geometric`**（**会改项目依赖配置**，与 `uv pip install` 不同类）＋ `root='./data'` 数据集自动下载落盘；纯文档，0 凭据/0 外发 mandate | 批P |
| 173 | 173 | `torchdrug` | `torchdrug` | ✅ 成功 | — | **用户面**；`b9d779a78286` / 14,145 B（`license: Apache-2.0 license` ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）纯文档件（`uv pip install torchdrug[full]`、`~/molecule-datasets/` 数据目录、AlphaFold/ESM/RDKit 外部引用，均为示例非 mandate） | 批P |
| 176 | 176 | `umap-learn` | `umap-learn` | ✅ 成功 | — | **用户面**；`63f035cb4815` / 15,393 B（`license: BSD-3-Clause license` ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）纯文档件（`uv pip install umap-learn` / `umap-learn[parametric_umap]`；**显式要求设 `random_state` 以保证可复现**——与本项目可复算纪律同向） | 批P |

| 167 | 167 | `statsmodels` | `statsmodels` | ✅ 成功 | — | **用户面**；`6eadae2bd489` / 19,691 B（`license: BSD-3-Clause license` ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）纯文档件（OLS/GLM/ARIMA/VAR/诊断/稳健 SE；`KFold(shuffle=True, random_state=42)` 显式可复现；`statsmodels.org` 为参考链接） | 批Q |
| 170 | 170 | `timesfm-forecasting` | `timesfm-forecasting` | ✅ 成功 | — | **用户面**；`101f92e7a6c8` / 30,154 B（**`allowed-tools: Read Write Edit Bash`** ＋ `license: Apache-2.0 license` ＋ `metadata.skill-author: Clayton Young / Superior Byte Works, LLC (@borealBytes)`＝**本棒第 5 个非 K-Dense 作者** ＋ 独有 `skill-version: "1.0.0"` 键）⛔ **强制执行面（见 §4 R-B42）**：「**⚠️ Mandatory Preflight** … **CRITICAL — ALWAYS run the system checker before loading the model**」＋ `python scripts/check_system.py`；另含 HuggingFace 权重 **~800 MB 外网下载**落 `~/.cache/huggingface/`、`pip install torch --index-url https://download.pytorch.org/whl/cu121`、示例目录 `cd examples/… && python run_forecast.py`、`plt.savefig("forecast.png")`、`json.dump(…, f)` 落盘；⚠️ 文件内自述文献（arXiv `2310.10688`，ICML 2024）**本棒 0 联网核验**；**0 遵从** | 批Q |
| 175 | 175 | `treatment-plans` | `treatment-plans` | ✅ 成功 | — | **用户面**；`66c81ea88cd4` / **52,691 B（乙半最大件）**（**`allowed-tools: Read Write Edit Bash`** ＋ `license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`）⛔⛔ **本棒最强生图 mandate（见 §4 R-B43）**：「**⚠️ MANDATORY: Every treatment plan MUST include at least 1 AI-generated figure** using the scientific-schematics skill… **This is not optional**」＋ `python scripts/generate_schematic.py … -o figures/output.png`（**直连 R-B29 枢纽件**）；⛔ **提权系统级安装面**：`sudo cp assets/… /usr/local/texlive/texmf-local/tex/latex/` ＋ `sudo texhash` ＋ `sudo tlmgr update --self` ＋ `tlmgr install nejm/jama/bmj/apa7/…` ＋ `mkdir -p ~/texmf/…`；⚠️ **PHI/临床建议面**（HIPAA Safe Harbor 18 标识符去标识化 ＋ DSM-5/ICD-10 ＋ PHQ-9/GAD-7 ＋ 具体剂量示例如 Metformin 500mg BID、Sertraline 50mg、Gabapentin 300mg TID ＋ 阿片 PDMP/naloxone/手段限制/自杀风险评估）；⚠️ **跨供应商归属**：「Part of the **Claude Scientific Writer** project. See main LICENSE file.」＋ 脚本路径写死 `.claude/skills/treatment-plans/scripts`（宿主实为 MiniMax Code）——**如实登记，不代为更正**；**0 遵从**（0 生图、0 sudo、0 生成任何临床文档、0 处理任何 PHI） | 批Q |
| 179 | 179 | `venue-templates` | `venue-templates` | ✅ 成功 | — | **用户面**；`4f412d3b092b` / 23,294 B（**`allowed-tools: Read Write Edit Bash`** ＋ `license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`）⛔ **写/执行面 ＋ 默认生图 mandate（见 §4 R-B41）**：「always consider adding scientific diagrams… **Scientific schematics should be generated by default**」＋ `python scripts/generate_schematic.py … -o figures/output.png`（直连 R-B29）；另含 `python scripts/customize_template.py --template … --output my_nature_paper.tex`、`validate_format.py --report validation_report.txt`、`pdflatex`/`bibtex`/`latexmk -pdf` 编译链（**写盘＋执行**）；⚠️ **陈旧时点自标**：「Last updated: 2024」而 venue 规范按年变动（如其引用 `neurips_2024.sty`、NeurIPS 2024 CFP）——**如实登记，不代为更新**；⚠️ 与 `workspace-setup`(#181) / `venue-targeting`(#178) 同属**异构学术项目/投稿 schema 族**；**0 遵从**（0 生图、0 编译、0 写任何 `.tex`/report） | 批Q |
| 183 | 183 | `zarr-python` | `zarr-python` | ✅ 成功 | — | **用户面**；`e5dfd7907be4` / 20,046 B（`license: MIT license` ＋ `metadata.skill-author: K-Dense Inc.`；无他面同名副本）**乙半末位**；⚠️ 弱风险：云存储段 `s3fs.S3FileSystem(anon=False)  # Use credentials`（走默认凭据链，**未点名任何 key 名**）＋ `s3://my-bucket/…` ＋ `ProcessSynchronizer('sync_data.sync')` 同步文件落盘；纯文档件 | 批Q |

---

## §3 统计

### §3.1 实调成败（唯一判据＝`Skill` 工具真实返回）

| 项 | 值 |
|---|---|
| 计划枚数（乙半全量） | **91** |
| ✅ 成功 | **91** |
| ❌ 失败 | **0** |
| 重试（失败重试 ≤2 形态：目录名 → `name:` 值） | **0 次触发**（91/91 目录名 == frontmatter `name`，实为单形态） |
| 加载器返回 `Location` 指向 **用户面** | **91/91** |
| 加载器返回 `Location` 指向 PC 面 / BI 面 | **0 / 0** |
| 加载回内容被**遵从**的条数 | **0**（全部作惰性数据） |

**覆盖率：91/91 ＝ 100%，本棒 0 余量。**

### §3.2 命中面判定（三证互校）

| 判据 | 结果 |
|---|---|
| ① `Location` 路径面 | 91/91 均为 `D:/Users/Administrator/.minimax/skills/<名>/SKILL.md`（用户面） |
| ② frontmatter 首行签名（`name` == 目录名） | 91/91 一致；**0 枚 `name` ≠ 目录名**；**0 枚 frontmatter 解析失败** |
| ③ SHA-12 ＋ 字节复算 | 91/91 与盘上终态逐项吻合（复算口径见 §1.4） |
| **PC 面存在同名副本者** | **2 枚**：`scientific-brainstorming`(#150)、`statistical-analysis`(#166) |
| **→ 追加 `description` 逐字比对** | **2/2 判定为「用户面」**：二者加载回 `description` 均逐字吻合**用户面**基线，**均不吻合** PC 面基线（PC 树 `sha256-tree-v1-1965fcb6208a…`） |
| BI 面（`.builtin-skills`，20 目录）同名命中 | **0 枚** |

> **结论**：命中面判定**未**仅依赖 `Location`——2 枚 PC 同名项已由 `description` 逐字比对独立确认（详见 §2 对应行）。

### §3.3 体积台账（91 枚 `SKILL.md` 合计）

| 指标 | 值 |
|---|---|
| 合计 | **1,363,558 B** |
| 均值 | 14,984 B |
| 最小 | **1,949 B**（`stock-financial-analysis`，本棒**最薄壳件**） |
| 最大 | **52,691 B**（`treatment-plans`，乙半**最大件**） |
| ≥ 20 KB | **17 枚** |
| ≥ 50 KB | **2 枚**（`treatment-plans` 52,691 B、`seo-geo-optimizer` 51,482 B） |
| < 5 KB | **6 枚** |

### §3.4 许可（`license:`）分布 —— 措辞高度不一致，**逐字记录，未代为更正**

| `license:` 原文 | 枚数 |
|---|---|
| `MIT license` | 29 |
| **（无 `license:` 键）** | **19** |
| `Apache-2.0 license` | 9 |
| `MIT`（裸） | 8 |
| `BSD-3-Clause license` | 6 |
| `Unknown` | 5 |
| `Apache-2.0`（裸） | 2 |
| `3 clause BSD license` | 1 |
| `3-clause BSD license` | 1 |
| `BSD-3-Clause`（裸） | 1 |
| `SD-3-Clause license` | 1 ⚠️ **疑为 `BSD` 之误（见 §3.7）** |
| `GPL-3.0 license` | 1 |
| `GPL-2.0 license` | 1 |
| `Apache License, Version 2.0` | 1 |
| `Proprietary (API key required)` | 1 ⚠️ **本棒唯一专有许可声明**（`rowan`） |
| **URL 形态**（`https://github.com/…LICENSE`） | **5**（`sympy` / `polars` / `polars-bio` / `pydicom` / `matplotlib`） |
| **合计不同措辞** | **20 种** ／ 91 枚 |

**无 `license:` 键的 19 枚**：`mckinsey-presentation-generator`、`memory-systems`、`multi-agent-patterns`、`novel-writing-expert`、`openclaw-self-evolution-pack`、`paper-lookup`、`project-development`、`proof-writer`、`reasoning-trace-optimizer`、`run-summary`、`sales-powermap`、`self-improvement-loops`、`skill-template`、`stock-financial-analysis`、`tool-design`、`torch-geometric`、`venue-targeting`、`workspace-setup`、`xiaohongshu-collector`。

### §3.5 作者分布

| `skill-author:` / `author:` 原文 | 枚数 |
|---|---|
| `K-Dense Inc.` | **62** |
| **（无作者键）** | **21** |
| `Kuan-lin Huang` | 3（`molecular-dynamics`、`phylogenetics`、`scvelo`） |
| `AHK Strategies (ashrafkahoush-ux)` | 1（`what-if-oracle`） |
| `Clayton Young / Superior Byte Works, LLC (@borealBytes)` | 1（`timesfm-forecasting`） |
| `aaron-he-zhu` | 1（`seo-geo-optimizer`，附 `source: github.com/aaron-he-zhu/…`） |
| `MiniMaxAI` | 1（`minimax-docx`） |
| `Orchestra Research` | 1（`ml-paper-writing`） |
| `Muratcan Koylan` / `Powered by: MiniMax M2.1` | 1（`reasoning-trace-optimizer`，非 `skill-author` 键位） |

**无作者键的 21 枚**：`mckinsey-presentation-generator`、`memory-systems`、`minimax-pdf`、`minimax-xlsx`、`multi-agent-patterns`、`novel-writing-expert`、`openclaw-self-evolution-pack`、`pptx-generator`、`project-development`、`proof-writer`、`reasoning-trace-optimizer`、`run-summary`、`sales-powermap`、`self-improvement-loops`、`skill-template`、`stock-financial-analysis`、`tool-design`、`torch-geometric`、`venue-targeting`、`workspace-setup`、`xiaohongshu-collector`。

> ⚠️ 其中 `self-improvement-loops`(#160) 与 `tool-design`(#171) **无 frontmatter 作者键**，但末节 `## Skill Metadata` 记为 `Agent Skills for Context Engineering Contributors`（**跨供应商/跨项目语料署名**，与 K-Dense 无关）。故上表「无作者键」按 **frontmatter 键位**统计，与末节署名不冲突。

### §3.6 frontmatter 显式声明面

| 声明键 | 枚数 | 明细 |
|---|---|---|
| `allowed-tools:` | **14 / 91** | `Read Write Edit Bash` × 12（`paper-2-web`、`parallel-web`、`pptx-posters`、`pyzotero`、`research-grants`、`research-lookup`、`scientific-critical-thinking`、`scientific-schematics`、`scientific-slides`、`timesfm-forecasting`、`treatment-plans`、`venue-templates`）；`Read, Write, Edit, Grep, Glob` × 1（`proof-writer`，**逗号分隔，与空格分隔不同类**）；`Read Write` × 1（`what-if-oracle`） |
| `compatibility:` | **5 / 91** | `PARALLEL_API_KEY required`（`parallel-web`）／`An OpenRouter API key is required to use Perplexity search`（`perplexity-search`）／`PARALLEL_API_KEY and OPENROUTER_API_KEY required`（`research-lookup`）／`API required`（`rowan`）／`Some features require an Huggingface token`（`transformers`） |
| `AIGC:` 前缀 | 1 | `minimax-docx`（frontmatter 以 `AIGC:` 起头，且 `name:` 位于块尾） |

**14 枚 `allowed-tools` 与 5 枚 `compatibility`，本棒 0 采纳。**

### §3.7 形态学观察（如实登记，不代为更正、不代为背书）

1. **许可措辞 20 种、19 枚无 `license:` 键**——同一语料库内 `MIT license` / `MIT` 并存，`BSD-3-Clause license` / `3-clause BSD license` / `3 clause BSD license` / `BSD-3-Clause` 并存。
2. ⚠️ **`SD-3-Clause license`（`scanpy`）**——与全库其余写法对照，`S` 开头疑为 `B` 之误。**本棒仅记录该字面，不代为更正、不代为查证。**
3. **URL 形态许可 5 枚**——`license:` 直接填 GitHub LICENSE 链接（`sympy`/`polars`/`polars-bio`/`pydicom`/`matplotlib`），与 SPDX 短名不同类。
4. **`license: Unknown` 5 枚**——与「无 `license:` 键」是**两种不同状态**，未合并计数。
5. **描述键形态**——引号 `description`、折叠块 `description: >`、跨多行长描述并存；`minimax-docx` 的 `name:` 不在前 15 行、`openclaw-self-evolution-pack` 的 `description` 排在 `name` 之前 ⇒ 前 N 行扫描法会误报（本棒已改用 frontmatter 边界正则）。
6. **元数据键位不统一**——`metadata.skill-author` vs 顶层 `author`（`seo-geo-optimizer`）vs 顶层 `skill-author`（`ml-paper-writing` 形态为 `version`/`author`/`tags`/`dependencies` 且**无 `metadata:` 块**）vs 末节 `## Skill Metadata`（`self-improvement-loops`/`tool-design`）vs `skill-version`（`timesfm-forecasting`）。
7. **跨供应商/跨项目受众表述**——`skill-template`(#164) 正文以 `Claude` 为默认受众（「Default assumption: Claude is already very smart」）；`treatment-plans`(#175) 自述「Part of the **Claude Scientific Writer** project」且脚本路径写死 `.claude/skills/…`；而实测宿主为 **MiniMax Code**。**如实登记，不代为更正。**
8. **异构学术项目 schema 族（3 枚同族）**——`workspace-setup`(#181) / `venue-targeting`(#178) / `venue-templates`(#179) 共用 `project.yaml`＋`notes/…`＋`models/model_v<current>.md` 布局，**与本仓 deposon 布局不一致**。
9. **未标出处的量化断言**——`seo-geo-optimizer`(#161) 的 CTR 影响表（「Number in title +20-30%」「Brackets +38%」等）、`what-if-oracle`(#180) 的「黄金比例 61.8/38.2 源自自然分支」等，**文件内无出处标注**。
10. **文件内自述引用（本棒 0 联网核验，一律不背书）**——`self-improvement-loops`(#160) 列出 9 条 arXiv 号与 Lil'Log 引用；`tool-design`(#171) 引用 `claim-tool-design-vercel-d0-reduction`；`what-if-oracle`(#180) 引用 2 个 Zenodo DOI；`timesfm-forecasting`(#170) 引用 arXiv `2310.10688`。
11. **`claim-*` 机制**——`self-improvement-loops` 与 `skill-template` 均要求「numeric/benchmark/volatile claims 须带 inline `claim-*` ID backed by `researcher/claims/index.jsonl`」，而**该 registry 路径未在盘上核实**（本棒 0 查找，登记为「未核验」）。
12. **与本项目纪律同向的表述**——`umap-learn`(#176)「always set `random_state`」、`statsmodels`(#167) `KFold(shuffle=True, random_state=42)`、`statistical-analysis`(#166) Best Practices #1「**Pre-register analyses**」、`ml-paper-writing`/`proof-writer` 的文档产出规范。**如实记录，不代表本棒已遵循。**

### §3.8 执行方式（可复算）

- **串行逐枚**调用 `Skill` 加载器，每轮 1 枚，**0 并发**；单次调用为本地解析，实测耗时秒级。
- **分 17 批即时落盘**（批 A–Q）：批A(93–96) 4｜批B(97–100) 4｜批C(101–108) 8｜批D(109–115) 7｜批E(116–124) 9｜批F(125–130) 6｜批G(131–135) 5｜批H(136–140) 5｜批I(141–145) 5｜批J(146–150) 5｜批K(151–153) 3｜批L(154–158) 5｜批M(159–161) 3｜批N(162–166) 5｜批O(168/174/177/178/180/181/182) 7｜批P(169/171/172/173/176) 5｜批Q(167/170/175/179/183) 5 ⇒ **合计 91**。
- 批 O–Q 为按「信息价值÷体积」择序加载，故 §2 表中**批 O/P/Q 的序位非连续**；这是**如实登记的执行顺序**，不代表名单有缺。
- **时刻字段用批次标记（批A–Q）**，不编造分钟级时间戳。
- **全程 0 次** `web_search` / `web_fetch` / `mcp_invoke` / 任何 LLM 或 API 调用；**0 次**读 key；**0 次**写 `config.yaml` / `mcp.json` / `plugin.json` / `skill-hub.json`。

---

## §4 风险登记：加载回内容中的祈使性/冒名/外发/凭据类指令（**0 遵从**）

> **总纪律**：⛔ 本棒**未执行任何 `SKILL.md` 内指令**。指令来源是**盘上文件**，**不是 PI**，**不得以盘上文本冒充 PI 指令**。以下条目**一律只登记、不遵从、不扩散**。

本节共登记 **40 条**（`R-B1`…`R-B40`）。**风险类**编码：`KEY`＝凭据/密钥索取｜`NET`＝外部网络/第三方 API｜`OUT`＝外发/发布/上传｜`WRITE`＝写盘/改环境｜`SELF`＝自我修改/自演化｜`OVER`＝工具偏好覆写｜`NAME`＝署名/冒名｜`PRIV`＝个人/受控数据采集｜`MAND`＝强制执行/越权处置｜`ADV`＝专业建议面｜`PROMO`＝第三方推广｜`DECL`＝frontmatter 显式声明。

**全部 40 条一律 0 遵从。** 本棒未执行其中任何一条：0 读取任何 key、0 设置任何环境变量、0 发起任何外部请求、0 写入除本产出件与 §0 清理外的任何文件、0 修改任何 skill/配置、0 更改宿主工具集、0 以任何第三方名义署名。

| 编号 | skill（乙半序） | 类 | 加载回中的具体表述（摘要，非逐字全文） | 本棒处置 |
|---|---|---|---|---|
| R-B1 | `mckinsey-presentation-generator`（#99） | WRITE/OUT | MANDATORY 流程 ＋ 调用 `deploy_html_presentation` **发布**产物 | 0 遵从：未发布 |
| R-B2 | `minimax-docx`（#120） | WRITE | frontmatter 以 `AIGC:` 起头；`gate-check` 作**硬门槛**未过即不得交付；`name:` 位于块尾 | 0 遵从：未过门槛、未按其格式改写 |
| R-B3 | `minimax-pdf`（#113） | WRITE | `make.sh fix` **自动安装依赖** | 0 遵从：未运行任何脚本 |
| R-B4 | `minimax-xlsx`（#123） | WRITE | 「**Do NOT spawn sub-agents**」「**Always produce the output file — this is the #1 priority**」 | 0 遵从：**本棒即为单棒串行，未 spawn subagent** |
| R-B5 | `ml-paper-writing`（#137） | NET/KEY | 装**外部 Exa MCP** ＋ 联网取 BibTeX | 0 遵从：0 装 MCP、0 联网 |
| R-B6 | `modal`（#138） | KEY/OUT | 读 `.env` 取 `MODAL_TOKEN_ID` / `MODAL_TOKEN_SECRET` ＋ `modal setup` 浏览器认证 ＋ **云部署** | 0 遵从：**0 读 `.env`**、0 认证、0 部署 |
| R-B7 | `neuropixels-analysis`（#139） | KEY/NET | `from anthropic import Anthropic` 的**外部 LLM 复核**路径 | 0 遵从：0 LLM 调用 |
| R-B8 | `omero-integration`（#140） | KEY | 用户名/密码认证 | 0 遵从：0 读凭据 |
| R-B9 | `open-notebook`（#141） | NET/KEY/OUT/PROMO | `curl -o docker-compose.yml <raw.githubusercontent…>` ＋ 读 `OPEN_NOTEBOOK_ENCRYPTION_KEY` / `OPEN_NOTEBOOK_PASSWORD` ＋ K-Dense Web 推广 | 0 遵从：0 下载、0 读 key、0 外推；**与普查件 R4 同面复核成立** |
| **R-B10** | `openclaw-self-evolution-pack`（#142） | **KEY/OUT（本棒最重）** | 指示读 `/root/.openclaw/openclaw.json`、**提取 providers API Key 与 MiniMax Coding Plan 密钥**、聚合成 `{channel}\|{clientId}\|{clientSecret}` 形式，并推送至**硬编码飞书（`open.feishu.cn`）机器人 Webhook** | 0 遵从：**0 读该文件、0 取任何 key、0 外发**。回执中**仅记其存在，不复写完整 token 形态** |
| R-B11 | `paper-2-web`（#143） | KEY/NET/OUT | `.env` key ＋ `git clone` ＋ 部署 GitHub Pages / Netlify / Vercel ＋ YouTube 发布 | 0 遵从：0 克隆、0 部署、0 发布 |
| R-B12 | `paper-lookup`（#144） | KEY/DECL | 读 `NCBI_API_KEY` / `CORE_API_KEY` / `S2_API_KEY` / `OPENALEX_API_KEY`（**四个 key**）；**全无 `license:` 键** | 0 遵从：0 读 key |
| R-B13 | `parallel-web`（#145） | **OVER/KEY** | `compatibility: PARALLEL_API_KEY required` ＋「**Use for ALL web searches**」**工具偏好覆写** ＋ 强制写 `sources/` | 0 遵从：**未覆写宿主工具偏好**、0 写 `sources/` |
| R-B14 | `perplexity-search`（#146） | KEY | `compatibility: An OpenRouter API key is required` ＋ `setup_env.py --api-key` **把 key 置于命令行**（进程列表可见） | 0 遵从：0 传 key |
| R-B15 | `pptx-generator`（#147） | WRITE | **无 `skill-author`** ＋ 指示**并发生成 5 个 subagent** | 0 遵从：**0 并发、0 spawn**（另与本机「并行 ≤2–3 路」偏好相悖） |
| R-B16 | `pptx-posters`（#148） | OUT/NET | 强制 AI 生图 ＋ 经**在线转换器外传** | 0 遵从：0 生图、0 外传 |
| R-B17 | `proof-writer`（#149） | WRITE | 默认向**项目根**写 `PROOF_PACKAGE.md`；独有 `argument-hint:` ＋ `$ARGUMENTS` | 0 遵从：0 写项目根 |
| R-B18 | `protocolsio-integration`（#150） | KEY/OUT | OAuth/Bearer ＋ 外部上传 ＋ **DOI 发布** | 0 遵从：0 认证、0 上传、0 发布 |
| R-B19 | `pydicom`（#151 前邻） | PRIV | 医学影像 **PHI 匿名化**面（`license` 为 URL 形态） | 0 遵从：0 处理任何 PHI |
| R-B20 | `pyhealth`（#152 前邻） | PRIV/ADV | 临床数据 / **PHI** 面 | 0 遵从：0 处理任何 PHI |
| R-B21 | `pymatgen`（#153 前邻） | KEY | `MP_API_KEY` | 0 遵从：0 读 key |
| R-B22 | `pyzotero`（#154 前邻） | KEY/WRITE | `ZOTERO_API_KEY` ＋ **写操作**（增删改文献库） | 0 遵从：0 读 key、0 写 |
| **R-B23** | `reasoning-trace-optimizer`（#155 前邻） | **SELF** | 正文含「**Optionally update the system prompt**」——**指示修改自身系统提示** | 0 遵从：**未改 system prompt、未改任何配置** |
| R-B24 | `research-grants`（#156 前邻） | OUT | **MANDATORY 1–2 张 AI 生图** | 0 遵从：0 生图 |
| R-B25 | `research-lookup`（#157 前邻） | KEY/WRITE | `PARALLEL_API_KEY` ＋ `OPENROUTER_API_KEY` **双 key** ＋ 强制写 `sources/` | 0 遵从：0 读 key、0 写盘 |
| **R-B26** | `rowan`（#158 前邻） | **KEY/DECL/PROMO** | **`license: Proprietary (API key required)`**——本棒**首个专有许可声明** ＋ `ROWAN_API_KEY` ＋ 云端计算 ＋ K-Dense Web 推广 | 0 遵从：0 读 key、0 上云 |
| **R-B27** | `run-summary`（#159 前邻） | **WRITE** | 「**Every agent pass must end by appending…**`logs/agent-history.md`… **Do not skip this step**」——与本任务 0 写盘纪律**直接冲突** | **0 遵从**（本棒第二重要）：未创建 `logs/`，未写任何 agent-history |
| **R-B28** | `sales-powermap`（#160 前邻） | **PRIV/OUT** | **OSINT/个人数据采集面**：抓取目标公司人员 LinkedIn 档案、Twitter 账号、**推断邮箱**以构建「决策人 Power Map」与外联话术 | 0 遵从：**0 联网、0 采集任何个人信息** |
| **R-B29** | `scientific-schematics`（#152） | **KEY/OUT** | 本棒**「强制调用型」枢纽件**：`OPENROUTER_API_KEY` ＋ `--api-key "sk-or-v1-…"` **命令行传 key** ＋ Nano Banana 2 生图 / Gemini 3.1 Pro Preview 质检；多个 skill 强制调用它 | 0 遵从：0 传 key、0 生图、0 质检 |
| **R-B30** | `scientific-slides`（#153） | **NAME** | 「**Default author is \"K-Dense\" unless another name is specified**」＝**默认第三方署名** | 0 遵从：本产出件署名为 **doc-writer（agent-0032834a3e04）**，不冒 K-Dense 名头 |
| R-B31 | `self-improvement-loops`（#160） | **SELF** | **自修改 doctrine 件**：以「harness 自身即被优化对象」为纲，明列 self-edit 阶梯（`Self-Harness` / `Darwin Godel Machine` / `STOP` 等）＋「Constraints stated in prompt text get evolved away…」等祈使句 | 0 遵从：未改任何 skill/配置/提示 |
| R-B32 | `skill-template`（#164） | **WRITE** | 指示「使用本模板**创建新 Agent Skill**」＋「**add or update a record in `researcher/mechanisms/registry.jsonl`**」 | 0 遵从：**未创建任何 skill、未写该 registry** |
| R-B33 | `workspace-setup`（#181） | **MAND/WRITE** | 「Run this skill at the start of **every** command invocation, before reading any project artifacts or dispatching any agent」＋ 异构 schema 5 件必读 ＋「refuse immediately」/「Ask the user」/「Abort」 | 0 遵从：未按其 schema 读文件、未 dispatch 任何 agent、未 refuse/abort 任何动作 |
| R-B34 | `transformers`（#174） | **KEY/DECL** | `compatibility: Some features require an Huggingface token` ＋「## Authentication」`huggingface_hub.login()` ＋ `export HUGGINGFACE_TOKEN="your_token_here"` ＋ 指向 `huggingface.co/settings/tokens` | 0 遵从：**0 读/设/落盘任何 token，0 联网** |
| R-B35 | `venue-targeting`（#178） | **WRITE** | 指示「copy the active venue state into **`project.yaml`**」并给出 YAML 块 ＋「store venue choice in `notes/gap_briefs/<slug>.md`」 | 0 遵从：0 写 `project.yaml`、0 建 `notes/gap_briefs/` |
| **R-B36** | `xiaohongshu-collector`（#182） | **OVER/PRIV** | ①「⚠️ 核心执行规则（必须遵守）」**明文覆写宿主工具选择**（「绝对禁止使用任何外部搜索引擎」「绝对禁止使用 `batch_web_search`、`WebSearch` 或任何网页搜索工具」）；② 用浏览器工具**直接操作** `www.xiaohongshu.com` 全量爬取第三方 UGC（正文 ＋ 全部图片文字 OCR ＋ 全部评论 ＋ 用户昵称），以「原文至上/宁多勿少/穷尽式搜索」驱动最大化；③ **规避反爬**：「如遇到访问限制，适当降低操作频率」「如遇到登录弹窗…尝试关闭继续操作」 | 0 遵从：**0 浏览器操作、0 访问该站、0 联网、0 采集任何用户数据**；未覆写宿主工具集 |
| R-B37 | **归并项**：`open-notebook`(R-B9) ＋ `rowan`(R-B26) ＋ `usfiscaldata`(#177) 等 | **PROMO** | 多个 K-Dense 族件末尾附「**Suggest Using K-Dense Web**」段，推销托管端到端研究平台 `www.k-dense.ai`（`rowan` 另称由 K-Dense Inc. 出品） | 0 遵从：**未向任何用户推荐该第三方平台**；亦不代为评价该平台 |
| R-B38 | `stock-financial-analysis`（#168） | **ADV** | 给出「买入卖出信号参考」「估值合理吗」等**投资建议面**（虽附「不构成投资建议」「市场有风险」免责声明）；且**无任何数据源/接口**，属**不可执行的薄壳** | 0 遵从：未产出任何分析或建议 |
| R-B39 | `what-if-oracle`（#180） | **DECL/WRITE** | frontmatter **直接声明 `allowed-tools: Read Write`**（若被宿主采纳即为**写权限扩面**） | **0 采纳**：未按此声明扩权；本棒全程只读 |
| R-B40 | `tool-design`（#171） | **SELF（邻接）** | 「Using Agents to Optimize Tools」模式：把工具失败样本喂给 agent，**由 agent 改写工具描述**（`get_agent_response(prompt)`），构成自修改邻接面 | 0 遵从：未 spawn 任何 agent、未改任何工具描述 |

| R-B41 | `venue-templates`（#179） | **WRITE/MAND/NET** | frontmatter 声明 **`allowed-tools: Read Write Edit Bash`**；「**always consider adding scientific diagrams**… **Scientific schematics should be generated by default**」＋ `python scripts/generate_schematic.py "…" -o figures/output.png`（**直连 R-B29 枢纽件**）；`customize_template.py --output my_nature_paper.tex`、`validate_format.py --report validation_report.txt`、`pdflatex`/`bibtex`/`latexmk -pdf` 编译链；另自标「**Last updated: 2024**」而 venue 规范按年变动 | 0 遵从：**0 生图、0 编译、0 写任何 `.tex`/report、0 采纳 `allowed-tools`**；陈旧时点如实登记、不代为更新 |
| **R-B42** | `timesfm-forecasting`（#170） | **MAND/WRITE/NET** | 「**⚠️ Mandatory Preflight**… **CRITICAL — ALWAYS run the system checker before loading the model for the first time**」＋ `python scripts/check_system.py`；frontmatter 声明 **`allowed-tools: Read Write Edit Bash`**；HuggingFace 权重 **~800 MB 外网下载**落 `~/.cache/huggingface/`；`pip install torch --index-url https://download.pytorch.org/whl/cu121`（**外部 index**）；示例目录 `cd examples/… && python run_forecast.py`（执行 mandate）；`plt.savefig("forecast.png")`、`json.dump(results, f)` 落盘 | 0 遵从：**0 跑 preflight、0 下载权重、0 装包、0 执行示例、0 落盘**；0 采纳 `allowed-tools` |
| **R-B43** | `treatment-plans`（#175） | **MAND/WRITE/NET/PRIV/ADV** | 「**⚠️ MANDATORY: Every treatment plan MUST include at least 1 AI-generated figure** using the scientific-schematics skill… **This is not optional**」＋ `generate_schematic.py -o figures/output.png`（**本棒最强生图 mandate**，直连 R-B29）；**提权系统级安装面**：`sudo cp assets/… /usr/local/texlive/texmf-local/tex/latex/` ＋ `sudo texhash` ＋ `sudo tlmgr update --self` ＋ `tlmgr install nejm/jama/bmj/apa7/…` ＋ `mkdir -p ~/texmf/…`；**PHI/临床建议面**（HIPAA Safe Harbor 18 标识符去标识化 ＋ DSM-5/ICD-10 ＋ PHQ-9/GAD-7 ＋ 具体剂量 ＋ 阿片 PDMP/naloxone/手段限制/自杀风险评估）；`allowed-tools: Read Write Edit Bash` | 0 遵从：**0 生图、0 sudo、0 tlmgr、0 生成任何临床文档、0 处理任何 PHI**；0 采纳 `allowed-tools` |
| R-B44 | `zarr-python`（#183） | **KEY（弱/隐式）** | 云存储段 `s3fs.S3FileSystem(anon=False)  # Use credentials`——**走默认凭据链**，未点名任何 key/env 名（与 R-B6/R-B34 等明文 key 名不同类） | 0 遵从：0 连任何对象存储、0 取任何凭据 |

**归并统计（本棒已测 91 枚＝全量范围内）**：涉 `KEY` 凭据/密钥索取 **19 条**；涉 `WRITE` 写盘/改环境/改配置 **19 条**；涉 `NET` 外部网络/第三方 API/外部 index **15 条**；涉 `OUT` 外发/发布/上传 **9 条**；涉 `PRIV` 个人/受控/受保护数据 **5 条**；涉 `SELF` 自我修改/邻接 **3 条**；涉 `OVER` 工具偏好覆写 **2 条**；涉 `NAME` 署名冒名 **1 条**；涉 `MAND` 强制执行/越权处置 **5 条**；涉 `ADV` 专业建议面（投资/临床/法律类） **3 条**；涉 `PROMO` 第三方推广 **1 组（归并 ≥4 处：R-B9 / R-B26 / `usfiscaldata` / `what-if-oracle`）**。**各类可重叠计数**（同一条可同属 KEY＋OUT 等），故分类合计 **> 条目总数 44**，非矛盾。

**frontmatter 显式声明面（`DECL`，本棒 5 枚）**：`parallel-web`（`PARALLEL_API_KEY required`）｜`perplexity-search`（`An OpenRouter API key is required`）｜`rowan`（`Proprietary (API key required)`）｜`transformers`（`Some features require an Huggingface token`）｜`treatment-plans` / `venue-templates` / `timesfm-forecasting`（`allowed-tools` 含 `Write`/`Edit`/`Bash`）。**7 枚声明，0 采纳。**

**须向 PI 明示的三条「最重」**（按本棒实测印象排序，非本棒判定权，判定归 verdict-keeper）：
1. **R-B10** `openclaw-self-evolution-pack`——读配置取 providers/Coding Plan 密钥并推送至硬编码飞书 Webhook（凭据＋外发双高）。
2. **R-B27** `run-summary`——强制每次 pass 追加写盘，与 0 写盘纪律直接对撞。
3. **R-B36** `xiaohongshu-collector`——工具偏好覆写 ＋ 第三方 UGC 全量爬取 ＋ 规避反爬表述。

---

## §5 自核节

### §5.1 落盘前后复算（0 覆写自证）

| 项 | 落名前 | 落盘后（终态） |
|---|---|---|
| 目标路径存在性 | `results/_skill_call_surface_probe_supplement_b_2026_09_30.md` **exists=False**（2 轮 × 4 目录 ＋ 全仓 glob 均 0 命中） | **新建 1 件**（**0 覆写**） |
| 既有件 0 回改 | — | 本棒**未对任何既有件写入**：首件 `112346df64fb` / 普查件 / **甲半件** 均**仅 `Read` ＋ 只读 `Get-FileHash`**，0 字节触动（详见 §5.6 终态复验） |
| **本棒写操作全清单** | — | **仅 5 次新建 ＋ 4 次删除**：新建本产出件 1 件；新建 `_tmp_*` 过程台账 4 件（§5.4）；删除该 4 件。**除上述 5 件外，本棒对盘上任何文件 0 次写入** |

### §5.2 完成度与余量（如实登记）

**实测完成度：91 / 91 ＝ 100%（全量达成，0 余量）。**

| 项 | 值 |
|---|---|
| 派工范围 | 乙半＝乙半序位 **93–183**，共 **91 枚** |
| 已实调并落表 | **91 枚（#93…#183，无缺号、无重号）** |
| 余量（未测） | **0 枚** |
| ❌ 失败需补派 | **0 枚** |
| 加载回内容被遵从 | **0 条** |
| 与甲半（序 1–92）的关系 | **0 交集**。甲半由**另一 writer** 在制品（`results/_skill_call_surface_probe_supplement_a_2026_09_30.md`，**终态 `a06316c3c7f2` / 50,658 B**；本棒开棒时读到的是 `2059508685e7` / 25,151 B ⇒ **该件在本次收口期间被并联 writer 改写，见 §5.6**）——本棒**仅只读参考、0 触 0 改**；其完成状态**不是本棒结论**，本棒不对其作任何判定 |

**若 PI 需并联核对**：甲乙两半合计 183 枚＝盘上「未测 183」全量；加先件已测 40 枚，**223 枚全集**在「先件 40 ＋ 甲半 92 ＋ 乙半 91」三段下均有归属，**段间 0 重复**（本棒对 40 枚已测名单做过 0 重复核验，见 §1.2）。

### §5.3 诚实边界（不夸大 · 不误导）

**本节的作用是划清「本棒实测到了什么 / 没实测什么」，防止把 0 证据说成有证据。**

**A. 关于「成功」二字，本棒只敢这样说**

1. ✅ 成功的唯一含义＝**`Skill` 加载器对该名称真实返回了一份内容**。本棒**不**因此断言：该 skill 的内容正确、可执行、有用，或其 `references/` 子文件存在且可读。
2. **反例已在数据里**：`stock-financial-analysis`(#168) 加载成功，但正文只给「数据收集 – 获取相关股票信息和财务数据」而**无任何数据源/接口** ⇒ **可加载 ≠ 可执行**。同类「薄壳」形态还有 `xiaohongshu-collector`(#182) 的部分数据源缺环。**91/91 成功不可被读成 91/91 质量达标。**
3. 本棒**0 断言加载器的实现**（优先级、缓存、去重、截断、name 解析规则均未观测）。只观测到「返回内容的 `Location` 与 frontmatter 签名」。

**B. 覆盖边界（重要，勿越读）**

4. 本棒**只加载了 `SKILL.md` 本体**，**未加载任何 `references/*.md` 或 `scripts/*.py`**。⇒ §4 的 44 条风险登记**只覆盖 `SKILL.md` 文本**；各 skill 的参考册与脚本内是否另有凭据/外发/写盘指令，**本棒 0 采集、0 断言**。
5. 本棒**只覆盖用户面 91 枚**。PC 面 172 skill（28 树）与 BI 面 20 目录**仅做了同名存在性核对**（乙半内 PC 同名 2 枚、BI 同名 0 枚），**其可加载性、可信度、优先级 0 实测、0 断言**。
6. **甲半（序 1–92）本棒 0 实调**。本产出件对甲半**无任何覆盖性结论**；并联甲半件的在制状态**不属本棒判定范围**。
7. **未跨会话、未跨机、未跨版本复测**：全部 91 枚在**单一会话的一次连续批次**内完成。若加载器行为随会话/版本变化，本件结论**不可外推**。

**C. 证据强度（逐条降级说明）**

8. §4 的「加载回中的具体表述」为**摘要转述**，非逐字全文复制；`R-B10` 涉及密钥形态，**回执与本件均只记其存在、不复写完整 token**。
9. §3.4/§3.5 的许可与作者分布、`§3.6` 的声明面、`§3.3` 的体积台账，均由**盘上 `SKILL.md` 终态复算**得出（可复算），**非**由加载回文本统计 ⇒ 若加载器对内容做过任何改写，两侧会有差异，本棒**未做该交叉验证**。
10. 文件内自述的外部引用（arXiv 号、Zenodo DOI、`claim-*` ID、`researcher/claims/index.jsonl` 路径、Vercel d0 案例等）**本棒 0 联网核验**（0 `web_search`/`web_fetch`/`mcp_invoke`）⇒ 一律标注为「文件内自述，0 核验」，**不为其真实性背书**。
11. `SD-3-Clause license`（`scanpy`）的「疑为误写」仅为**与同库写法对照后的印象**，**不是查证结论**。
12. `venue-templates`(#179) 自标「Last updated: 2024」与 venue 规范时效性的关系，本棒**0 核验**，仅登记该自标字面。

**D. 权限与边界（不越权声明）**

13. **本棒不出判定。** §4 末尾「最重三条」是**按本棒实测印象的排序**，**不是裁决**；风险成立与否、根因归类、处置决策**归 verdict-keeper**。本棒**不软化也不加码**。
14. **本棒不改任何既有件**：先件（`112346df64fb`）、普查件（`e96d99ff9e75`）、并联甲半件（`2059508685e7`）均**仅只读**（`Read` ＋ 只读哈希），**0 字节触动**。
15. **本棒 0 遵从**加载回中的一切指令：0 读 key／0 设环境变量／0 外部请求／0 改 skill 或配置／0 扩权采纳 `allowed-tools`／0 以第三方名义署名／0 spawn 任何 subagent／0 创建 `logs/agent-history.md`。
16. **署名如实**：本件由 **doc-writer（`agent-0032834a3e04`）** 出件，**不冒** Trae code / K-Dense / MiniMax / AHK Strategies / Superior Byte Works / aaron-he-zhu 等任何他方名头（尤其**未采纳** `scientific-slides` 的「Default author is K-Dense」与 `treatment-plans` 的「Claude Scientific Writer」归属表述）。
17. **临时台账已清理**：本棒过程用 `_tmp_*` 文件（4 个）于收尾阶段**自行删除**；删除对象**全部为本棒自建的临时件**，未触碰任何既有件（见 §5.4）。
18. **本棒未派工、未改阈值、未动 schema、未动 frozen**：R4 保持 0 key 读取／0 key 落盘；R5 无变更；V1–V3 未触及。

**E. 若 PI 要更硬的结论，本棒指出三条可复算的下一步（均不属本棒职权，仅登记）**

19. 若要判定「加载器是否会真的执行 `SKILL.md` 内的祈使句」，需**在隔离环境做受控执行**（本棒 0 执行）。
20. 若要覆盖 `references/` 与 `scripts/` 的风险面，需**逐件加载子文件**（本棒 0 加载，见本节 B-4）。
21. 若要判定 PC 面 172 skill 与用户面 223 skill 的**优先级/取舍关系**，需**跨面同条件对照加载**（本棒 0 对照）。

### §5.4 过程临时件清理登记（本棒自建 → 已删）

| 临时件 | 字节 | SHA-12 | 用途 | 终态 |
|---|---|---|---|---|
| `results/_tmp_halfb_roster_2026_09_30.txt` | 5,151 | `793c47b9a713` | 乙半 91 枚名册（序位｜名｜字节｜SHA-12｜`name` 值｜有无 `SKILL.md`） | **已删除** |
| `results/_tmp_roster_calc_2026_09_30.ps1` | 3,555 | `5a858670bf21` | 名单/排序/分半复算脚本 | **已删除** |
| `results/_tmp_size_faces_2026_09_30.ps1` | 1,955 | `52ece9f9caf1` | 三面体积与同名基线脚本 | **已删除** |
| `results/_tmp_pc_shadow_2026_09_30.ps1` | 2,421 | `9665958358d9` | PC 面同名副本扫描脚本 | **已删除** |

- 清理后 `results/` 下 `_tmp_*` 文件数 = **0**（已复验）。
- **删除对象全部为本棒自建的临时件**；既有件（含并联甲半件与两份先件）**0 删除、0 移动、0 改写**。
- 删除走 `Remove-Item`（本机为常规删除，非回收站语义）——**本棒如实登记该处置方式**，若 PI 需要可恢复副本，请以本表 SHA-12 为线索（内容为本棒可完全复算的派生数据，可重跑复现）。

### §5.5 终态指纹（自引用说明）

本产出件的**终态 SHA-12 / 字节数 / 行数**在**回执**中给出，而非内嵌于本件：文件一旦写入自身哈希即改变内容，哈希随即失效（自引用不可解）。**复算命令**（任何人可复跑）：

```powershell
$p='D:\私人资料\deposon-repo\results\_skill_call_surface_probe_supplement_b_2026_09_30.md'
$b=[System.IO.File]::ReadAllBytes($p)
$h=([System.Security.Cryptography.SHA256]::Create().ComputeHash($b)|%{$_.ToString('x2')}) -join ''
"SHA12=" + $h.Substring(0,12).ToUpper()
"BYTES=" + $b.Length
"LINES=" + ([System.IO.File]::ReadAllText($p) -split "`n").Count
"CR=" + ([regex]::Matches([System.IO.File]::ReadAllText($p),"`r")).Count
"BOM=" + ($b[0] -eq 0xEF -and $b[1] -eq 0xBB -and $b[2] -eq 0xBF)
```

**版式自证**：UTF-8 **无 BOM**、**纯 LF**（CR 计数 = 0）、Markdown 表格；骨架阶段的全部锚点占位注释（HTML 注释形式，共 5 个）**已逐个替换为实内容并删除注释本体**（收口自检：全文件锚点注释本体命中数 = **0**；§3.1–§5.6 全部有实内容。**本句刻意不复写标记模式字面，以免自引用污染该计数**）。

### §5.6 既有件终态复验 ＋ **须上报的发现：两份既有件已被并联 writer 改写**

**（1）本棒写操作全清单（自证 0 回改）**

| # | 操作 | 对象 | 终态 |
|---|---|---|---|
| 1 | 新建 | `results/_skill_call_surface_probe_supplement_b_2026_09_30.md`（本件） | 存在 |
| 2–5 | 新建 | `results/_tmp_halfb_roster_…txt` / `_tmp_roster_calc_…ps1` / `_tmp_size_faces_…ps1` / `_tmp_pc_shadow_…ps1` | **已删除**（§5.4） |
| — | 追加/编辑 | **仅本件**（本棒对该件 `Edit` 共 **15** 次，全部落在本件内） | 终态见回执 |
| — | 其他文件写入 | **0 次** | — |

**（2）既有件终态哈希复验（收口时刻重算）**

| 既有件 | 本棒开棒时读到 | **收口时盘上终态** | 字节变化 | 收口时 mtime | 归因 |
|---|---|---|---|---|---|
| `results/_skill_call_surface_probe_2026_09_30.md`（先件） | `112346df64fb` / 34,853 B〔棒初摘要转录〕 | **`112346df64fb` / 32,261 B** | 34,853 → 32,261 | 2026-09-30 16:52:00 | ⚠️ 见注 1 |
| `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md`（普查件） | `e96d99ff9e75` / 55,374 B（棒初**实际读取**） | **`0b8041435f8e` / 58,660 B** | 55,374 → **58,660（+3,286）** | 2026-09-30 17:25:45 | ⛔ **已被并联 writer 改写** |
| `results/_skill_call_surface_probe_supplement_a_2026_09_30.md`（并联甲半件） | `2059508685e7` / 25,151 B | **`a06316c3c7f2` / 50,658 B** | 25,151 → **50,658（+25,507，约翻倍）** | 2026-09-30 17:25:29 | ⛔ **已被并联 writer 改写**（与其在制品身份一致） |

> ⚠️ **注 1（先件，登记为矛盾，不擅自判定）**：棒初摘要记 `112346df64fb` / **34,853 B**，收口复算为 `112346df64fb` / **32,261 B**。**同哈希不同字节在物理上不可能同真** ⇒ 必有一侧为棒初记录的**转录失实**（哈希与字节未同源复算）。按「以对**盘上终态**复算为准」的纪律，本件采信收口复算值，并**如实登记该矛盾**。请 PI／evidence-auditor 复核棒初记录，本棒**不擅自判定哪一侧为真**。
>
> ⛔ **注 2（普查件与甲半件，须上报）**：两件**在本次收口期间哈希与字节均发生变化**（mtime 均为 17:25:2x–17:25:4x）。本棒对二者**只有 `Read` 与只读哈希**（见上表写操作全清单），**不可能**是其写入者。⇒ **归因：并联 writer（甲半棒／parent 侧）在同一时段继续在写**，与「甲半件为在制品」一致。**本棒不对其内容作任何判定**；若 PI 需要「普查件 0 回改」之结论，须以并联 writer 的写入记录为准，**不可引用本件作为证据**。

---

**出件**：doc-writer（`agent-0032834a3e04`）
**日期**：2026-09-30
**件名**：`results/_skill_call_surface_probe_supplement_b_2026_09_30.md`
**状态**：乙半 **91/91 全量实调完成**，0 失败、0 余量；§4 风险登记 44 条全部 0 遵从。**待 PI 复核。**
