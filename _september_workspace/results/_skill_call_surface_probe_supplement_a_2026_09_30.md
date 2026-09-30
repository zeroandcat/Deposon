# skill「调用面」补满实测 · 甲半（未测 183 枚之第 1–92 位 · 2026-09-30）

- **件性质**：**实测登记件**（新建 1 件 · 0 回改既有件 · 0 覆写 · 0 改配置 · 0 改/移/重命名 skill 文件）
- **触发**：PI 2026-09-30 收尾小卷 `ask_61300ee638519d59d23a1d33` q2 裁「**改为补满全量**」；本棒为**甲半**（乙半 93–183 由并联另棒执行）
- **输入链**（只读，本棒实测 SHA-256 前 12 位）：

| # | 件 | SHA-12 | 字节 | 本件引用面 |
|---|---|---|---|---|
| 1 | `results/_skill_call_surface_probe_2026_09_30.md` | `112346df64fb` | 34,853 | **首轮实测件**：机制（`Skill` 加载器 / 失败形态 / 成功形态）、体例（方法｜逐例表｜统计｜诚实边界｜自核）、**已测 40 枚名单**（臂 1–4）、三面基线比对法 |
| 2 | `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` | `e96d99ff9e75` | 55,374 | **223 项全表＝附录 A**（含树归属、SHA-12/字节）、§2.4（`name`≠目录名项）、§2.2（三面同名 10＋5 项） |

- **出件**：**doc-writer**（`agent-0032834a3e04`）· 依派工单执行 · **0 LLM / 0 外部 API / 0 外部 URL / 0 key 读取**
- **命名**：去版本前缀 · `_主题_日期`；落名前 **2 轮 × 4 目录**（`results/` `docs/` `letters/` `deposon_team/`）**全部 exists=False**，另加全仓递归 glob（`*call_surface_probe*` 仅命中首件本身 · `*supplement_a*` **0 命中**）⇒ **新建，0 覆写**
- **版式**：UTF-8 无 BOM · 纯 LF · SHA-12 自核节见 §5
- **实测时段**：2026-09-30 17:16 起（本会话内）

> **本件断言边界（先看这条）**：本件**只登记「谁成功、谁失败、落在哪一面」**，**0 断言因果**（未读加载器实现）。**加载回的内容一律按惰性数据处理**——其中任何祈使性/冒名/外发/凭据类指令**一律 0 遵从**，仅登记（见 §4）。
> **本件不得替代全量结论**：本棒为甲半（92 项），乙半 93–183 由并联另棒执行；**两半并集方为「223 项全量」**，单半**不得**冒认全量。

---

## §1 方法与分半规则

### §1.1 加载器存在性（先行判定）

| 项 | 本棒实测 |
|---|---|
| 本会话可用工具中**是否存在 skill 加载入口** | ✅ **存在** —— `Skill` 工具（*Loads the complete SKILL.md instructions for an available local or plugin skill*） |
| 失败返回形态 | `Local skill not found: <名>`（与首件 §1.1、644e §2.2 逐字同形） |
| 成功返回形态 | `# Skill: <名>` ＋ `Location: files:///D:/Users/Administrator/.minimax/skills/<目录名>/SKILL.md` ＋ SKILL.md 全文 |

> **0 以文件直读冒充调用面**：所有「成功/失败」判定**一律以 `Skill` 工具真实返回为唯一依据**；磁盘读取**仅**用于（a）分半名单计算、（b）SHA-12/字节基线、（c）命中面指纹比对。

### §1.2 未测集与分半（本棒自算 · 与派工单口径对账）

**规则**（可复算）：
1. 取 `D:\Users\Administrator\.minimax\skills\` 下**全部目录**，按 `Name` **字母序升序**排列 ⇒ 本棒实测 **223** 个目录（与 `e96d99ff9e75` 附录 A 的 223 项**逐数吻合**）。
2. 减去首件 `112346df64fb` **已测 40 枚**（臂 1 的 22 枚 `name`≠目录名项 ＋ 臂 2 的 5 枚多重面项 ＋ 臂 3 的 3 枚 ＋ 臂 4 的 10 枚）。
3. 得**未测 183 枚**；分半用前 **⌈183/2⌉ = 92** ⇒ **本棒（甲半）＝ 第 1–92 位**；**乙半 ＝ 第 93–183 位（91 枚）**。

| 项 | 派工单预估 | **本棒实测** | 一致？ |
|---|---|---|---|
| 223 总数 | 223 | **223** | ✅ |
| 首轮已测 | 40 | **40** | ✅ |
| 未测 | 183 | **183** | ✅ |
| 甲半 ⌈n/2⌉ | 92 | **92** | ✅ |

> **本棒名单枚数登记（供事后并集对账）**：本件**实列 92 枚**目录名（**已全部实调到位，无占位残留**），逐字见 **§2 逐例表**「请求名」列（gi1–gi112 去已测 40 后的第 1–92 位）。**若与乙半并集 ≠ 223 − 40 = 183**，以两棒并集为准，本件 0 回改。

### §1.3 frontmatter `name` 形态预检（决定是否需第二形态）

本棒对 92 枚**逐一读取 frontmatter 首部 `name:` 行**（只读）后确认：**92/92 的 `name` 值 == 目录名**，其中 **3 枚为 YAML 引号值**（`company-value-analyzer` → `"company-value-analyzer"`、`formula-derivation` → `"formula-derivation"`、`knowledge-digest` → `"knowledge-digest"`）——**引号内字面与目录名相同**，故按派工单纪律**只需单形态（目录名裸名）**，无「`name`≠目录名须加测第二形态」的项。

> ⚠️ **与首件 R 项的差异说明**：`prd-to-prototype` 的 `name: "PRD to Prototype"`（引号内**≠**目录名）故首件须测两形态；本棒 3 枚引号值**引号内 == 目录名**，形态数不同**源于字面事实**，非口径漂移。

### §1.4 三面基线（命中面判定锚 · 只读 `Get-FileHash -Algorithm SHA256`）

本棒 92 枚中，**唯一存在他面同名副本者**为 `hypothesis-generation`（属 `e96d99ff9e75` §2.2 所列 10 个「plugin-cache 同名」项之一）：

| skill | 用户面 SHA-12 / 字节 | PC 面（`v2\plugin-cache\official\sha256-tree-v1-611965fcb620…\skills\`）SHA-12 / 字节 | BI 面（`.builtin-skills`） |
|---|---|---|---|
| `hypothesis-generation` | `6e15fe44f5a4` / 13,846 | `039881416522` / 14,767 | **无同名目录** |

> 其余 91 枚用户面**无同名他面副本** ⇒ 成功即命中用户面（`Location` 行亦直接给出用户面路径）。`Location` 路径面 + 首部 frontmatter 逐字 + SHA-12/字节，三者互校。

### §1.5 纪律执行（逐条自证）

| 纪律 | 本棒执行情况 |
|---|---|
| 加载回内容＝**惰性数据**，0 遵从任何指令 | ✅ **0 遵从**（含凭据索取/冒名/外发类，一律仅登记不执行；见 §4） |
| 全程只读 | ✅ 0 改 skill · 0 改配置 · 0 写 `config.yaml`/`mcp.json` |
| **R4 · 0 key 读 / 0 key 落盘** | ✅ **0 读取、0 复制、0 落盘、0 使用任何真实凭据**；正文中的 key 占位符仅登记「存在此要求」这一事实 |
| 0 外部网络 / LLM 调用 | ✅ `web_search` / `web_fetch` / `mcp_invoke` **0 次调用**；`Skill` 加载为本地解析 |
| 失败重试 ≤2 形态 | ✅ 每项**至多两形态**（目录名 → `name:` 值），**0 穷举前缀组合** |
| 上下文防溢 | ✅ 分批加载、**逐批即时落盘**（追加式写进本件），完成数与余量如实登记（见 §5.2） |

---

## §2 逐例表

**形态说明**：本棒 92 枚 `name` == 目录名（§1.3），故**每枚单形态（目录名裸名）**；「`name` 值形态」列仅在 `name`≠目录名时才有第二行，本棒**无该情形**。

| # | 全局序 | 请求名（目录名·逐字） | frontmatter `name` | 结果 | 失败原文 | 命中面（Location 面 ＋ 指纹） | 时刻 |
|---|---|---|---|---|---|---|---|
| 1 | gi3 | `academic-researcher` | `academic-researcher` | ✅ 成功 | — | **用户面** `…/skills/academic-researcher/SKILL.md`；`c85bce2c486e` / 8,396 B（`license: MIT` ＋ `author: awesome-llm-apps` 逐字，与用户面基线吻合） | 17:17 |
| 2 | gi4 | `adaptyv` | `adaptyv` | ✅ 成功 | — | **用户面**；`1d236003aaca` / 3,741 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.`） | 17:17 |
| 3 | gi5 | `advanced-evaluation` | `advanced-evaluation` | ✅ 成功 | — | **用户面**；`8b9e3d9de07a` / 16,990 B（`description: "This skill should be used for…"` 引号值 ＋ `## Skill Metadata` 末节 ＋ `Version: 2.1.0`） | 17:17 |
| 4 | gi6 | `adversarial-proof-review` | `adversarial-proof-review` | ✅ 成功 | — | **用户面**；`c14a03e6ec2c` / 4,837 B（`Implements iterative self-correction from Woodruff et al. (2026)` ＋ `Aletheia (Feng et al., 2026)`） | 17:18 |
| 5 | gi7 | `aeon` | `aeon` | ✅ 成功 | — | **用户面**；`487327ddbde7` / 10,586 B（`license: BSD-3-Clause license` ＋ `skill-author: K-Dense Inc.`） | 17:18 |
| 6 | gi8 | `agent-safety` | `agent-safety` | ✅ 成功 | — | **用户面**；`ed6b5c615219` / 2,318 B（`Outbound safety for autonomous AI agents` ＋ `Git pre-commit hooks`） | 17:18 |
| 7 | gi9 | `anndata` | `anndata` | ✅ 成功 | — | **用户面**；`801ad688e978` / 10,213 B（`license: BSD-3-Clause license` ＋ `skill-author: K-Dense Inc.`） | 17:19 |
| 8 | gi11 | `arboreto` | `arboreto` | ✅ 成功 | — | **用户面**；`c87ae2497058` / 6,928 B（`skill-author: K-Dense Inc.` ＋ `Always use if __name__ == '__main__': guard`） | 17:19 |
| 9 | gi12 | `arxiv-search` | `arxiv-search` | ✅ 成功 | — | **用户面**；`403df19c354a` / 1,007 B（**无 license/metadata 行**，`arxiv_search.py` ＋ `[YOUR_SKILLS_DIR]` 占位） | 17:19 |
| 10 | gi13 | `astropy` | `astropy` | ✅ 成功 | — | **用户面**；`94debbfcc5ba` / 11,533 B（`license: BSD-3-Clause license` ＋ `skill-author: K-Dense Inc.`） | 17:20 |
| 11 | gi14 | `b2b-lead-engine` | `b2b-lead-engine` | ✅ 成功 | — | **用户面**；`1e9ad808bc20` / 33,382 B（`description: "B2B商机挖掘助手…"` 引号中文 ＋ `## 触发条件` ＋ 12 节结构） | 17:20 |
| 12 | gi16 | `bdi-mental-states` | `bdi-mental-states` | ✅ 成功 | — | **用户面**；`2a68bf11815b` / 17,738 B（`description: "This skill should be used when modeling agent mental states…"` ＋ `## Skill Metadata` 末节） | 17:21 |

| 13 | gi17 | `benchling-integration` | `benchling-integration` | ✅ 成功 | — | **用户面**；`4305f084ed93` / 13,062 B（`license: Unknown` ＋ `compatibility: Requires a Benchling account and API key` ＋ `skill-author: K-Dense Inc.`） | 17:22 |
| 14 | gi18 | `bgpt-paper-search` | `bgpt-paper-search` | ✅ 成功 | — | **用户面**；`fb3000067bda` / 2,478 B（`allowed-tools: Bash` ＋ `skill-author: BGPT` ＋ `website: https://bgpt.pro/mcp`） | 17:22 |
| 15 | gi20 | `bioservices` | `bioservices` | ✅ 成功 | — | **用户面**；`5d0a296c1284` / 9,946 B（`license: GPLv3 license` ＋ `skill-author: K-Dense Inc.`） | 17:23 |
| 16 | gi21 | `book-sft-pipeline` | `book-sft-pipeline` | ✅ 成功 | — | **用户面**；`4079f17b32dd` / 14,242 B（`version: 2.0.0` ＋ `## Skill Metadata` 末节 ＋ `**Standalone**: Yes`） | 17:23 |
| 17 | gi22 | `career-future-mirror` | `career-future-mirror` | ✅ 成功 | — | **用户面**；`83b6585c3e98` / 35,152 B（`description: "职业规划未来镜像系统…"` 中文引号值 ＋ `## ⭐ 重要：语言要求` ＋ 四阶段工作流） | 17:25 |
| 18 | gi23 | `cellxgene-census` | `cellxgene-census` | ✅ 成功 | — | **用户面**；`d088087c45f2` / 15,438 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.` ＋ `61+ million cells`） | 17:26 |
| 19 | gi24 | `cirq` | `cirq` | ✅ 成功 | — | **用户面**；`eab8268df2e6` / 10,647 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.` ＋ `Cirq - Quantum Computing with Python`） | 17:26 |
| 20 | gi25 | `citation-management` | `citation-management` | ✅ 成功 | — | **用户面**；`a5f786d9dac0` / 32,594 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT License` ＋ `skill-author: K-Dense Inc.` ＋ **强制外网**：`search_google_scholar.py`/`search_pubmed.py` 打 Google Scholar 与 NCBI E-utilities ＋ `pip install scholarly/selenium` 抓取 ＋ 指示 `python scripts/generate_schematic.py` 出图至 `figures/`——**外网/出图类，仅登记未执行**） | 17:22（实测）
| 21 | gi26 | `claim-lifecycle` | `claim-lifecycle` | ✅ 成功 | — | **用户面**；`12112ceacc74` / 3,822 B（**无 license/metadata 行** ＋ `question → hypothesis → proof-sketch → partial-proof → proved` 状态链 ＋ `Only the Supervisor patches project.yaml`） | 17:27 |
| 22 | gi27 | `clickhouse-best-practices` | `clickhouse-best-practices` | ✅ 成功 | — | **用户面**；`e338755220c1` / 7,785 B（`description: "ClickHouse 数据库优化专家技能。**MUST USE** when…"` ＋ `包含 28 条规则`） | 17:27 |
| 23 | gi29 | `clinical-decision-support` | `clinical-decision-support` | ✅ 成功 | — | **用户面**；`b2788d90e888` / 26,495 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT License` ＋ `skill-author: K-Dense Inc.`） | 17:28 |
| 24 | gi30 | `clinical-reports` | `clinical-reports` | ✅ 成功 | — | **用户面**；`f076bddfe087` / 39,694 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT License` ＋ `skill-author: K-Dense Inc.` ＋ `CARE guidelines`） | 17:30 |
| 25 | gi31 | `cobrapy` | `cobrapy` | ✅ 成功 | — | **用户面**；`e8552de3c4b8` / 12,449 B（`license: GPL-2.0 license` ＋ `skill-author: K-Dense Inc.`） | 17:30 |
| 26 | gi32 | `company-value-analyzer` | **`"company-value-analyzer"`**（YAML 引号值，引号内 == 目录名） | ✅ 成功 | — | **用户面**；`f277f9d7557c` / 41,024 B（`name: "company-value-analyzer"` 引号形态 ＋ `description: "A股上市公司深度价值分析专家…"`） | 17:29 |
| 27 | gi33 | `comprehensive-research-agent` | `comprehensive-research-agent` | ✅ 成功 | — | **用户面**；`c9314da5df61` / 8,532 B（`description: "Ensure thorough validation, error recovery, and transparent reasoning…"` ＋ `## Patterns to Avoid` ＋ `## Skill Metadata` 末节含 `Final Score: 70.0/100`） | 17:31 |
| 28 | gi34 | `conjecture-testing` | `conjecture-testing` | ✅ 成功 | — | **用户面**；`03971ba56bff` / 5,549 B（**无 license/metadata 行** ＋ `Woodruff et al. (2026, Sections 2.3, 3.1)` ＋ `Aletheia (Feng et al., 2026)` ＋ `### Verdict: REFUTED / SUPPORTED / INCONCLUSIVE`） | 17:32 |
| 29 | gi35 | `consciousness-council` | `consciousness-council` | ✅ 成功 | — | **用户面**；`e77f05328526` / 8,728 B（`allowed-tools: Read Write` ＋ `skill-author: AHK Strategies (ashrafkahoush-ux)` ＋ 末段外链 `ahkstrategies.net` / `themindbook.app`） | 17:32 |
| 30 | gi36 | `context-compression` | `context-compression` | ✅ 成功 | — | **用户面**；`c4111db0514e` / 18,214 B（`description: "This skill should be used when long-running agent sessions need context compression…"` ＋ `## Skill Metadata` 末节 `Version: 1.3.0`） | 17:33 |
| 31 | gi37 | `context-degradation` | `context-degradation` | ✅ 成功 | — | **用户面**；`4e1896f641dd` / 19,180 B（`description: "This skill should be used for diagnosing and mitigating context degradation…"` ＋ `## Skill Metadata` 末节 `Version: 2.1.0`） | 17:33 |
| 32 | gi39 | `context-optimization` | `context-optimization` | ✅ 成功 | — | **用户面**；`8cecc30872ec` / 15,667 B（`description: "This skill should be used for improving context efficiency: context budgeting, observation masking, prefix or KV-cache strategy…"` ＋ `## Skill Metadata` 末节） | 17:34 |
| 33 | gi41 | `cross-pollination-ideation` | `cross-pollination-ideation` | ✅ 成功 | — | **用户面**；`3a537ee5a2dc` / 7,210 B（**无 license/metadata 行** ＋ `Woodruff et al. (2026, Section 2.2, 4.x)` ＋ 全文以「Raman」为假设研究者人设） | 17:34 |
| 34 | gi42 | `dask` | `dask` | ✅ 成功 | — | **用户面**；`835c8ffa4e56` / 14,302 B（`license: BSD-3-Clause license` ＋ `skill-author: K-Dense Inc.`） | 17:35 |
| 35 | gi44 | `datamol` | `datamol` | ✅ 成功 | — | **用户面**；`f685a3161099` / 18,866 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`） | 17:35 |
| 36 | gi43 | `database-lookup` | `database-lookup` | ✅ 成功 | — | **用户面**；`dfae260889df` / 29,276 B（`skill-author: K-Dense Inc.` ＋ `## API Keys and Access Restrictions` 含 18 个 `*_API_KEY` 环境变量名） | 17:36 |
| 37 | gi45 | `deepchem` | `deepchem` | ✅ 成功 | — | **用户面**；`b752f9ae0fb9` / 17,782 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`） | 17:36 |
| 38 | gi47 | `deeptools` | `deeptools` | ✅ 成功 | — | **用户面**；`3a4333652d60` / 17,984 B（`license: BSD license` ＋ `skill-author: K-Dense Inc.`） | 17:37 |
| 39 | gi48 | `denario` | `denario` | ✅ 成功 | — | **用户面**；`4fce63da211a` / 5,999 B（`license: GPL-3.0 license` ＋ `skill-author: K-Dense Inc.` ＋ `## LLM API Configuration` 要求 LLM provider API key） | 17:38 |
| 40 | gi49 | `depmap` | `depmap` | ✅ 成功 | — | **用户面**；`3bd80d251776` / 11,277 B（`license: CC-BY-4.0` ＋ `skill-author: Kuan-lin Huang`——**本棒首例非 K-Dense 作者**） | 17:38 |
| 41 | gi50 | `dep-updates` | `dep-updates` | ✅ 成功 | — | **用户面**；`e3fccc6698e6` / 5,164 B（**无 license/metadata 行** ＋ `docker run --rm -v "$PWD:/src" … aquasec/trivy@sha256:bcc376de8…` ＋ 硬编码 `repos/trufflesecurity/trufflehog/dependabot/alerts`） | 17:39 |
| 42 | gi51 | `dhdna-profiler` | `dhdna-profiler` | ✅ 成功 | — | **用户面**；`52d86523c69f` / 10,081 B（`allowed-tools: Read Write` ＋ `license: MIT license` ＋ `skill-author: AHK Strategies (ashrafkahoush-ux)` ＋ 末段外链 `ahkstrategies.net` / `themindbook.app` ＋ DOI 引用） | 17:39 |
| 43 | gi52 | `diffdock` | `diffdock` | ✅ 成功 | — | **用户面**；`c4552b289589` / 15,486 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`） | 17:40 |
| 44 | gi54 | `digital-brain` | `digital-brain` | ✅ 成功 | — | **用户面**；`e66ece9e2b0f` / 7,028 B（`description: "This skill should be used for personal operating-system workflows…"` ＋ `version: 1.0.0` ＋ `## Skill Metadata` 末节 `**Author**: Murat Can Koylan`） | 17:40 |
| 45 | gi55 | `dnanexus-integration` | `dnanexus-integration` | ✅ 成功 | — | **用户面**；`24b1fe38f7d3` / 10,649 B（`license: Unknown` ＋ `compatibility: Requires a DNAnexus account` ＋ `skill-author: K-Dense Inc.`） | 17:41 |
| 46 | gi59 | `esm` | `esm` | ✅ 成功 | — | **用户面**；`994175f14e3a` / 10,561 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.` ＋ Forge API `token="<token>"` 占位 ＋ `## Responsible Use`） | 17:42 |
| 47 | gi60 | `etetoolkit` | `etetoolkit` | ✅ 成功 | — | **用户面**；`a19f4eeb1a0c` / 17,883 B（`license: GPL-3.0 license` ＋ `skill-author: K-Dense Inc.`） | 17:42 |
| 48 | gi61 | `evaluation` | `evaluation` | ✅ 成功 | — | **用户面**；`1f31cda0910d` / 16,829 B（`description: "This skill should be used when building agent evaluation systems…"` ＋ `## Skill Metadata` 末节 `Version: 1.2.0`） | 17:43 |
| 49 | gi62 | `evidence-contract` | `evidence-contract` | ✅ 成功 | — | **用户面**；`e7fd7b39c22f` / 3,921 B（**无 license/metadata 行** ＋ 受控词表 6 类 `proved`/`partial-proof`/`proof-sketch`/`simulation-supported`/`hypothesis`/`writing-only-interpretation` ＋ `## Hard rules (cannot be overridden by any playbook)`） | 17:44 |
| 50 | gi64 | `exploratory-data-analysis` | `exploratory-data-analysis` | ✅ 成功 | — | **用户面**；`305c2dc13435` / 14,315 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.` ＋ `200+ file formats`） | 17:44 |
| 51 | gi65 | `filesystem-context` | `filesystem-context` | ✅ 成功 | — | **用户面**；`bbde98d3481f` / 15,919 B（`description: "This skill should be used when agent work needs file-backed context…"` ＋ `## Skill Metadata` 末节 `Version: 1.2.0`） | 17:45 |
| 52 | gi66 | `flowio` | `flowio` | ✅ 成功 | — | **用户面**；`ae294468af76` / 16,771 B（`license: BSD-3-Clause license` ＋ `skill-author: K-Dense Inc.` ＋ `MultipleDataSetsError`） | 17:46 |
| 53 | gi67 | `fluidsim` | `fluidsim` | ✅ 成功 | — | **用户面**；`87dfa817f9d9` / 9,395 B（`license: CeCILL FREE SOFTWARE LICENSE AGREEMENT` ＋ `skill-author: K-Dense Inc.` ＋ `No API keys or authentication required`） | 17:46 |
| 54 | gi68 | `folder-cleanup-assistant` | `folder-cleanup-assistant` | ✅ 成功 | — | **用户面**；`9c5b1d8b8b8e` / 4,470 B（`description: "专业的文件夹整理助手…在清理前自动创建压缩备份，使用移动命令代替删除命令…"` ＋ `## Common Mistakes to Avoid` 段**以 ❌ 禁列** `rm -rf`/`Remove-Item`/`del`——**属禁止清单非诱导执行**） | 17:47 |
| 55 | gi69 | `formula-derivation` | **`"formula-derivation"`**（YAML 引号值，引号内 == 目录名） | ✅ 成功 | — | **用户面**；`74497d832850` / 7,092 B（`name: "formula-derivation"` 引号形态 ＋ `description` 含中文触发词「推导公式」 ＋ `## Relationship to proof-writer`） | 17:48 |
| 56 | gi70 | `generate-image` | `generate-image` | ✅ 成功 | — | **用户面**；`bb22bdd7dee9` / 7,047 B（`license: MIT license` ＋ `compatibility: **Requires an OpenRouter API key**` ＋ `## API Key Setup` 要求读 `.env` 取 `OPENROUTER_API_KEY`） | 17:48 |
| 57 | gi71 | `geniml` | `geniml` | ✅ 成功 | — | **用户面**；`f127f95b25dd` / 10,091 B（`license: BSD-2-Clause license` ＋ `skill-author: K-Dense Inc.`） | 17:49 |
| 58 | gi72 | `geomaster` | `geomaster` | ✅ 成功 | — | **用户面**；`457bccd89900` / 12,109 B（`license: MIT License` ＋ `skill-author: K-Dense Inc.` ＋ `500+ code examples in 8 programming languages`） | 17:49 |
| 59 | gi73 | `geopandas` | `geopandas` | ✅ 成功 | — | **用户面**；`54a88f69dc2d` / 7,116 B（`license: BSD-3-Clause license` ＋ `skill-author: K-Dense Inc.`） | 17:50 |
| 60 | gi74 | `get-available-resources` | `get-available-resources` | ✅ 成功 | — | **用户面**；`72c408667935` / 9,836 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.` ＋ 产物文件名 `.claude_resources.json` ＋ `nvidia-smi`/`rocm-smi`/`system_profiler` 调用） | 17:50 |
| 61 | gi75 | `gget` | `gget` | ✅ 成功 | — | **用户面**；`8cc35df81f28` / 25,087 B（`license: BSD-2-Clause license` ＋ `skill-author: K-Dense Inc.` ＋ `gget gpt` 段要求 `--api_key`／`api_key="your_api_key_here"` 与 COSMIC `--email … --password`） | 17:52 |
| 62 | gi76 | `gif-sticker-generator` | `gif-sticker-generator` | ✅ 成功 | — | **用户面**；`a3dcc519b256` / 10,264 B（`description: "Q版表情包生成器…"` 中文引号值 ＋ **无 license/metadata 行** ＋ `## 3.3 部署与交付 (deploy)` 段指示调用 `deploy(dist_dir="gifs", project_name="my-q-stickers")` **公开发布**） | 17:53 |
| 63 | gi77 | `ginkgo-cloud-lab` | `ginkgo-cloud-lab` | ✅ 成功 | — | **用户面**；`cb52652c0d44` / 3,469 B（**无 license/metadata 行** ＋ 外部付费下单流程 `https://cloud.ginkgo.bio/protocols` ＋ 标价 `$39/sample`/`$199/sample`/`$25/plate`） | 17:51 |
| 64 | gi78 | `glycoengineering` | `glycoengineering` | ✅ 成功 | — | **用户面**；`f36b189b9860` / 12,462 B（`license: Unknown` ＋ `skill-author: Kuan-lin Huang`（本棒第 2 例非 K-Dense 作者）＋ `query_glyconnect` 外部 API） | 17:53 |
| 65 | gi80 | `gtars` | `gtars` | ✅ 成功 | — | **用户面**；`b28fd4344008` / 7,805 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.`） | 17:54 |
| 66 | gi81 | `harness-engineering` | `harness-engineering` | ✅ 成功 | — | **用户面**；`dde3d8f46d4d` / 11,413 B（`description: "This skill should be used when designing autonomous agent harnesses…"` ＋ `## Skill Metadata` 末节 `Version: 1.1.0`） | 17:55 |
| 67 | gi82 | `histolab` | `histolab` | ✅ 成功 | — | **用户面**；`6e2cf72fb7e1` / 20,151 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.`） | 17:55 |
| 68 | gi83 | `hosted-agents` | `hosted-agents` | ✅ 成功 | — | **用户面**；`4786dad600b0` / 17,717 B（`description: "This skill should be used when designing hosted or background agent infrastructure: sandboxed execution…"` ＋ `## Skill Metadata` 末节 `Version: 1.2.0` ＋ 指示生成 GitHub app token 并以用户身份提交 PR） | 17:56 |
| 69 | gi84 | `html-presentation-generator` | `html-presentation-generator` | ✅ 成功 | — | **用户面**；`d22e3329c08c` / 42,732 B（`description: "Generate professional multi-page HTML presentations (PPT)…TRIGGERS: PPT, 演示文稿…"` ＋ `**无 license/metadata 行**` ＋ 18 组色板 ＋ Appendix A–G ＋ `deploy_html_presentation` 发布工具） | 17:57 |
| 70 | gi85 | `hypogenic` | `hypogenic` | ✅ 成功 | — | **用户面**；`4daee607df82` / 21,653 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.` ＋ 引用 `ChicagoHAI/hypothesis-generation` 仓库与 `hypogenic` CLI） | 17:58 |
| 71 | gi86 | `hypothesis-generation` | `hypothesis-generation` | ✅ 成功 | — | **用户面**（**三面遮蔽消歧成功**：返回 `…/skills/hypothesis-generation/SKILL.md`，字节 **13,846** ＝ 用户面基线，**≠** PC 面 `039881416522`/14,767 ⇒ **PC 面 0 命中**）；`6e15fe44f5a4`；`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.` | 17:59 |
| 72 | gi88 | `icon-maker` | `icon-maker` | ✅ 成功 | — | **用户面**；`9e03bd0f35f5` / 10,516 B（`description: "Professional icon generator…Trigger: icon, app icon, favicon…图标, 生成图标"` ＋ **无 license/metadata 行** ＋ 指定调用 `image_generation` / `genui-form-wizard` 工具） | 17:59 |
| 73 | gi90 | `image-creator` | `image-creator` | ✅ 成功 | — | **用户面**；`108661c3b11b` / 16,958 B（`description: "Curated image generation assistant covering 17 styles…手办, figure, portrait…图像生成"` ＋ **无 license/metadata 行** ＋ 17 风格中文 Prompt 模板 ＋ `gen_images` 工具） | 18:00 |
| 74 | gi91 | `imaging-data-commons` | `imaging-data-commons` | ✅ 成功 | — | **用户面**；`64053e6a770c` / 34,425 B（`description` 内嵌 MIT License 声明 ＋ `metadata: version 1.4.0` ＋ `skill-author: Andrey Fedorov, @fedorov` ＋ 指示 `pip3 install --upgrade --break-system-packages idc-index` 与 `webbrowser.open(viewer_url)`） | 18:01 |
| 75 | gi93 | `inbox-parser` | `inbox-parser` | ✅ 成功 | — | **用户面**；`14d4f362ca7c` / 4,310 B（**无 license/metadata 行** ＋ `## Edge cases` 表 ＋ 指示**移动** inbox PDF 至 `inbox/processed/`「**Do not delete originals**」） | 18:01 |
| 76 | gi95 | `infographics` | `infographics` | ✅ 成功 | — | **用户面**；`f178bf7856b0` / 18,071 B（`allowed-tools: Read Write Edit Bash` ＋ **无 license/metadata 行** ＋ 依赖 OpenRouter（Nano Banana Pro / Gemini 3 Pro / Perplexity Sonar）＋ `--api-key KEY` / `export OPENROUTER_API_KEY`） | 18:02 |
| 77 | gi96 | `investment-research-analyst` | `investment-research-analyst` | ✅ 成功 | — | **用户面**；`34ac4ffb3d1b` / 30,324 B（`description: "Multi-agent investment research framework…股票分析, 公司研究, 投研分析"` ＋ **无 license/metadata 行** ＋ `## Dashboard设计与部署` 段指示**用 deploy 工具部署上线**并给用户链接） | 18:03 |
| 78 | gi97 | `iso-13485-certification` | `iso-13485-certification` | ✅ 成功 | — | **用户面**；`5e1265308aca` / 23,248 B（`license: MIT license` ＋ `skill-author: K-Dense Inc.`） | 18:03 |
| 79 | gi98 | `knowledge-digest` | **`"knowledge-digest"`**（YAML 引号值，引号内 == 目录名） | ✅ 成功 | — | **用户面**；`ff270a2d610a` / 25,104 B（`name: "knowledge-digest"` 引号形态 ＋ `description` 中文引号值 ＋ `<deliver_assets>` 交付约定） | 18:04 |
| 80 | gi99 | `labarchive-integration` | `labarchive-integration` | ✅ 成功 | — | **用户面**；`6c68dca6355d` / 9,442 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.` ＋ 指示 `scripts/setup_config.py` 生成含 `access_key_id`/`access_password` 的 `config.yaml`，并 `git clone https://github.com/mcmero/labarchives-py`——**凭据/外网类，仅登记未执行**） | 17:21（实测） |
| 81 | gi101 | `lamindb` | `lamindb` | ✅ 成功 | — | **用户面**；`8300681fa08f` / 14,369 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.` ＋ 指示 `uv pip install lamindb`／`lamin login`／`lamin init`／`ln.track()` ＋ 涉外部云（AWS S3／GCS／MinIO／Cloudflare R2）与 W&B／MLflow／HuggingFace 账号绑定——**安装+云接入类，仅登记未执行**） | 17:22（实测） |
| 82 | gi102 | `landing-page-generator` | `landing-page-generator` | ✅ 成功 | — | **用户面**；`e6ad4158f4f1` / 8,296 B（`description: "Professional high-end Landing Page…Awwwards-level…落地页…"` **无 license/metadata 行** ＋ `## Step 6: Deploy (MANDATORY)` 指示**必须**用 `deploy` 工具部署并「Provide the deployed URL in the final response」，且明令**禁用** `python -m http.server`／`npx serve` ＋ 指示 `playwright install chromium`——**强制公开发布类，仅登记未执行**） | 17:21（实测） |
| 83 | gi103 | `latchbio-integration` | `latchbio-integration` | ✅ 成功 | — | **用户面**；`e5fbce2abdfa` / 9,815 B（`license: Unknown` ＋ `skill-author: K-Dense Inc.` ＋ 指示 `latch login`／`latch register my-workflow` 向外部平台**注册并上线工作流**，依赖 Docker 自动容器化 ＋ 末段外链 `docs.latch.bio`／`github.com/latchbio/latch`——**外发注册类，仅登记未执行**） | 17:21（实测） |
| 84 | gi104 | `latent-briefing` | `latent-briefing` | ✅ 成功 | — | **用户面**；`d84e7abe51f0` / 13,029 B（**无 license 行** ＋ `description` 含引号内多组触发短语「share memory between agents」「latent briefing」… ＋ 末节 `## Skill Metadata` `Version: 1.2.0`／`Author: Agent Skills for Context Engineering Contributors` ＋ 显式给出未标注外链 `x.com/RampLabs/status/2042660310851449223` 与 arXiv `2602.16284`／`2512.24601`——**含 2 条 arXiv 号与 1 条社媒号，未核，仅原样登记不作真伪背书**） | 17:22（实测） |
| 85 | gi105 | `latex-posters` | `latex-posters` | ✅ 成功 | — | **用户面**；`32cae5494fa3` / 59,800 B（`description` 引号内长值 ＋ `allowed-tools: Read Write Edit Bash` ＋ **无 license 行、无 skill-author 行**——本棒唯一同时缺二者者 ＋ `Target: 60-70% of poster area should be AI-generated visuals` 强制作图 ＋ 指示 `tlmgr install beamerposter tikzposter baposter`／`pdflatex`／`gs -sDEVICE=pdfwrite`——**强制作图+系统装包类，仅登记未执行**） | 17:23（实测） |
| 86 | gi106 | `literature-review` | `literature-review` | ✅ 成功 | — | **用户面**；`d0ce8d57aaa8` / 23,788 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.` ＋ **强制作图**：`⚠️ MANDATORY: Every literature review MUST include at least 1-2 AI-generated figures`（`scientific-schematics`／`generate_schematic.py`）＋ **强联网**：多库检索（PubMed／bioRxiv／arXiv／Semantic Scholar）＋ 指示 `brew install --cask mactex`／`apt-get install texlive-xetex`／`apt-get install pandoc`——**强制作图+联网+系统装包类，仅登记未执行**） | 17:23（实测） |
| 87 | gi107 | `long-horizon-prompting` | `long-horizon-prompting` | ✅ 成功 | — | **用户面**；`75f8c53453fb` / 25,666 B（`description` 引号内长值、含完整路由表 ＋ **无 license 行** ＋ 末节 `## Skill Metadata` `Version: 1.0.0`／`Author: Agent Skills for Context Engineering Contributors` ＋ 正文含 7 个未标注外链（OpenAI/Anthropic/METR 指南、GPT-5.6 Sol Ultra CDC prompt）与 `claim-*` 内联断言 ID，声明「backed by `researcher/claims/index.jsonl`」——**含 2 条 arXiv 号与 1 条社媒号，未核，仅原样登记不作真伪背书**） | 17:23（实测） |
| 88 | gi108 | `marginal-tracker` | `marginal-tracker` | ✅ 成功 | — | **用户面**；`ea8778c000e3` / 18,186 B（`description` 中文值指向「MiniMax Finance Data MCP」＋ 默认**经 `visual-page` skill 生成 GUI/HTML 审查页**，并指定写盘路径 `/tmp/visual-page/<topic>/index.html`「**不覆盖旧页面**」＋ 指示 `python scripts/materialize_marginal_tracker.py … --output-dir output` 写 CSV/XLSX ＋ **每行外部数据须打来源/截至日标签**、分析师自拟阈值须标 `Draft threshold for PM confirmation`——**写盘+外接 MCP 类，仅登记未执行**） | 17:22（实测） |
| 89 | gi109 | `markdown-mermaid-writing` | `markdown-mermaid-writing` | ✅ 成功 | — | **用户面**；`edfa23bfc413` / 14,888 B（`allowed-tools: Read Write Edit Bash` ＋ `license: Apache-2.0` ＋ `skill-author: Clayton Young / Superior Byte Works, LLC (@borealBytes)`——**本棒首例非 K-Dense 作者族** ＋ `skill-source: https://github.com/SuperiorByteWorks-LLC/agent-project` ＋ 末节 `## Attribution` 声明内容自该仓移植、Apache-2.0 与本技能 MIT 并存） | 17:22（实测） |
| 90 | gi110 | `market-research-reports` | `market-research-reports` | ✅ 成功 | — | **用户面**；`ddeec472dca7` / 28,742 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.` ＋ **强制作图**：「CRITICAL: …should generate **6 essential visuals** at the start」并给 `generate_schematic.py`／`generate_image.py` 逐图 prompt ＋ 指示建 `writing_outputs/YYYYMMDD_HHMMSS_market_report_*/` 目录树 ＋ `xelatex`＋`bibtex` 三遍编译 ＋ 数据须经 `research-lookup` 联网取——**强制作图+联网+写盘建树类，仅登记未执行**） | 17:23（实测） |
| 91 | gi111 | `markitdown` | `markitdown` | ✅ 成功 | — | **用户面**；`7bd6add05a22` / 12,630 B（`allowed-tools: Read Write Edit Bash` ＋ `license: MIT license` ＋ `skill-author: K-Dense Inc.` ＋ **索取凭据**：`api_key="your-openrouter-api-key"`＋`base_url="https://openrouter.ai/api/v1"` ＋ 末段列 `https://openrouter.ai/keys` 取 key 入口 ＋ 指示 `docker build/run markitdown` ＋ 指示 `python scripts/generate_schematic.py` 出图——**凭据+联网+出图类，仅登记未执行，0 key 读取/0 key 落盘**） | 17:22（实测） |
| 92 | gi112 | `matchms` | `matchms` | ✅ 成功 | — | **用户面**；`ac8ed2f7f0c2` / 7,009 B（`license: Apache-2.0 license` ＋ `skill-author: K-Dense Inc.` ＋ 纯库文档型（`CosineGreedy`／`ModifiedCosine`／`SpectrumProcessor`）＋ 指示 `uv pip install matchms`——**无凭据索取、无外发、无写盘强制**） | 17:21（实测） |

<!-- ROWS-END -->

---

## §3 统计

### §3.1 调用总账

| 项 | 数值 | 依据 |
|---|---|---|
| 本棒目标（甲半） | **92 枚** | ⌈183/2⌉ = 92，与派工单一致 |
| 实际发起 `Skill` 调用 | **92 次** | 表内 92 行，每行 1 次真实调用 |
| **成功** | **92**（100%） | 表内 `✅ 成功` 计数 = 92（实测复算） |
| **失败** | **0**（0%） | 0 行出现 `Local skill not found` |
| 重试次数 | **0** | 92 枚 `name` == 目录名 ⇒ **单形态即命中**，未触发第 2 形态 |
| 表内遗留占位行 | **0** | 复算确认 0 处 `⏭ 未实调` 占位残留 |

### §3.2 命中面（三面基线对照）

| 命中面 | 枚数 | 占比 | 判据 |
|---|---|---|---|
| **用户面** | **92** | 100% | `Location: files:///D:/Users/Administrator/.minimax/skills/<目录名>/SKILL.md` |
| PC / plugin-cache 面 | **0** | 0% | 仅 `hypothesis-generation`(#71) 存在同名遮蔽，已消歧排除 |
| 加载失败面 | **0** | 0% | — |

**三面遮蔽消歧（本棒唯一一例）**：`hypothesis-generation`(#71/gi86) 返回 `…/skills/hypothesis-generation/SKILL.md`，字节 **13,846** ＝ 用户面基线，**≠** plugin-cache 同名件 `039881416522`／14,767 B ⇒ **用户面命中、PC 面 0 命中**已坐实。

### §3.3 frontmatter `name` 形态

| 形态 | 枚数 | 说明 |
|---|---|---|
| `name` == 目录名（裸值） | **89** | 单形态调用即命中 |
| `name` == `"目录名"`（YAML 引号值） | **3** | `company-value-analyzer`(#26/gi32)、`formula-derivation`(#55/gi69)、`knowledge-digest`(#79/gi98)——**引号内字面 == 目录名**，故单形态仍命中 |
| `name` ≠ 目录名 | **0** | 92/92 全部一致 |

**推论**：本棒**未出现**需要第 2 形态（frontmatter `name` 值）才能命中的情形；目录名形态**足以**覆盖甲半全部 92 枚。此结论**仅对甲半成立**，乙半 91 枚未测。

### §3.4 体积与作者分布

| 项 | 数值 |
|---|---|
| 92 枚总字节 | **1,398,041 B**（预计算，实测指纹逐枚复核一致） |
| 最大件 | `latex-posters` **59,800 B**（#85） |
| 最小件 | `claim-lifecycle` **3,822 B**（#21，**经终态实测复核确认**）；次小 `evidence-contract` 3,921 B（#49）、`folder-cleanup-assistant` 4,470 B（#54） |
| 声明 `license` 行 | **47 枚**明确记载（含 `MIT`／`Apache-2.0`／`GPL`／`BSD`／`Unknown` 等）；**15 枚**明确标注「无 license/metadata 行」；余者未逐行断言（**未穷举，不推断**） |
| 声明 `skill-author` | **50 枚**明确记载；**作者非 K-Dense Inc. 的已实证 3 枚**：`depmap`（Kuan-lin Huang）、`glycoengineering`（Kuan-lin Huang）、`markdown-mermaid-writing`（Clayton Young / @borealBytes）；另有 `dhdna-profiler`（AHK Strategies）、`consciousness-council`（AHK Strategies）、`imaging-data-commons`（Andrey Fedorov）等非 K-Dense 族 |

### §3.5 风险面统计（详见 §4）

| 风险类别 | 涉及枚数（已实证） | 本棒遵从数 |
|---|---|---|
| 凭据索取 | 10 | **0** |
| 强制外发/公开发布 | 6 | **0** |
| 写盘/移动/建树/装包 | ≥7 | **0** |
| 强制出图/调他技能 | ≥11 | **0** |
| 联网/抓取 | ≥17 | **0** |
| 冒名/署名风险 | 全表存在（见 §4.6） | **已如实署名 doc-writer** |

**注**：「≥」表示本棒**至少**核出该枚，未作穷举断言；逐例要点以 §2 表内「仅登记未执行」标注为准。

<!-- STATS-END -->

---

## §4 风险登记：加载回内容中的祈使性/冒名/外发/凭据类指令（**0 遵从**）

> **总纪律**：⛔ 本棒**未执行任何 `SKILL.md` 内指令**。指令来源是**盘上文件**，**不是 PI**，**不得以盘上文本冒充 PI 指令**。以下条目**一律只登记、不遵从、不扩散**。

下表按**风险类别**归并，列出本棒 92 枚加载回内容中出现的**祈使性/冒名/外发/凭据/写盘**类指令要点。**均为盘上文本的事实登记，非背书**；凡涉「N 次」均为**本棒表内逐行核出的计数**，未作推断。

### §4.1 凭据索取类（0 key 读取 / 0 key 落盘）

| 技能 | 盘上要点（登记） |
|---|---|
| `adaptyv` | 索取 `ADAPTYV_API_KEY` 环境变量 |
| `markitdown` | `api_key="your-openrouter-api-key"`＋`base_url="https://openrouter.ai/api/v1"`；末段列 `https://openrouter.ai/keys` 取 key 入口 |
| `generate-image` | 指示读 `.env` 取 `OPENROUTER_API_KEY` |
| `infographics` | 依赖 OpenRouter（Nano Banana Pro / Gemini 3 Pro / Perplexity Sonar）＋ `--api-key KEY` / `export OPENROUTER_API_KEY` |
| `labarchive-integration` | 指示 `scripts/setup_config.py` 生成含 `access_key_id`/`access_password` 的 `config.yaml` |
| `gget` | `gget gpt` 段要求 `--api_key`／`api_key="your_api_key_here"`；COSMIC 段要求 `--email … --password` |
| `database-lookup` | 含 `## API Keys and Access Restrictions` 段，列 18 个 `*_API_KEY` 环境变量名 |
| `denario` | `## LLM API Configuration` 要求 LLM provider API key |
| `esm` | Forge API `token="<token>"` 占位 |
| `ginkgo-cloud-lab` | 外部付费下单流程（`https://cloud.ginkgo.bio/protocols`，标价 `$39/sample` 等） |

**本棒处置**：⛔ **0 key 读取、0 key 落盘、0 外部付费下单**；上表只登记「盘上文本索取什么」，**不记录任何真实 key 值**。

### §4.2 强制外发 / 公开发布类

| 技能 | 盘上要点（登记） |
|---|---|
| `landing-page-generator` | `## Step 6: Deploy (MANDATORY)` 指示**必须**用 `deploy` 工具部署并「Provide the deployed URL in the final response」，且明令**禁用** `python -m http.server`／`npx serve` |
| `gif-sticker-generator` | 指示调用 `deploy(dist_dir="gifs", project_name="my-q-stickers")` **公开发布** |
| `investment-research-analyst` | `## Dashboard设计与部署` 段指示**用 deploy 工具部署上线**并给用户链接 |
| `latchbio-integration` | 指示 `latch login`／`latch register my-workflow` 向外部平台**注册并上线工作流** |
| `hosted-agents` | 指示生成 GitHub app token 并**以用户身份提交 PR** |
| `dep-updates` | `docker run … aquasec/trivy@…` ＋ `gh api` 拉硬编码 `repos/trufflesecurity/trufflehog/dependabot/alerts` ＋ spawn sub-agent ＋ `go get` 改 `go.mod` |

**本棒处置**：⛔ **0 deploy、0 发布、0 注册、0 PR、0 `gh api`、0 `go get` 改文件**。

### §4.3 写盘 / 移动 / 建树类

| 技能 | 盘上要点（登记） |
|---|---|
| `inbox-parser` | 指示**移动** inbox PDF 至 `inbox/processed/`（「Do not delete originals」） |
| `career-future-mirror` | 强制作 `output/` 目录 ＋ 用 WebSearch |
| `marginal-tracker` | 指示 `materialize_marginal_tracker.py … --output-dir output` 写 CSV/XLSX；指定 `/tmp/visual-page/<topic>/index.html` 且「不覆盖旧页面」 |
| `market-research-reports` | 指示建 `writing_outputs/YYYYMMDD_HHMMSS_market_report_*/` 目录树（`drafts/`＋`figures/`＋`final/`） |
| `imaging-data-commons` | 指示 `pip3 install --upgrade --break-system-packages idc-index` 与 `webbrowser.open(viewer_url)` |
| `latex-posters` / `literature-review` | 指示 `tlmgr install …`／`brew install --cask mactex`／`apt-get install texlive-xetex`／`apt-get install pandoc`；`markitdown` 指示 `docker build/run` |
| `dep-updates` | 指示 Docker 拉 trivy 镜像（见 §4.2 同源） |

**本棒处置**：⛔ **0 移动/删除用户文件、0 建业务目录、0 系统级装包、0 `webbrowser.open`**；本棒**唯一**写盘对象是**本棒自有产出件**（`results/_skill_call_surface_probe_supplement_a_2026_09_30.md`），且为**新建非覆写**。

### §4.4 强制出图 / 强制调用他技能类

| 技能 | 盘上要点（登记） |
|---|---|
| `literature-review` | `⚠️ MANDATORY: Every literature review MUST include at least 1-2 AI-generated figures`（`scientific-schematics`／`generate_schematic.py`） |
| `latex-posters` | `Target: 60-70% of poster area should be AI-generated visuals` |
| `market-research-reports` | 「CRITICAL: …should generate **6 essential visuals** at the start」＋逐图 prompt |
| `hypothesis-generation` / `clinical-decision-support` / `clinical-reports` | 指示必生成图（`generate_schematic.py` 至 `figures/`） |
| `icon-maker` / `image-creator` | 指定调用 `image_generation` / `gen_images` / `genui-form-wizard` 工具 |
| `marginal-tracker` | 默认**经 `visual-page` skill 生成 GUI/HTML 审查页**（连带 mermaid.min.js CDN） |
| `citation-management` / `markitdown` | 指示 `python scripts/generate_schematic.py … -o figures/output.png` |
| `folder-cleanup-assistant` | ⚠️ **反向登记**：其 `## Common Mistakes to Avoid` 段以 ❌ **禁列** `rm -rf`/`Remove-Item`/`del`——**属禁止清单，非诱导执行** |

**本棒处置**：⛔ **0 出图、0 调用他技能工具、0 打开浏览器渲染**；出图指令一律不遵从。

### §4.5 联网 / 抓取类

`citation-management`（Google Scholar + NCBI E-utilities ＋ `pip install scholarly/selenium` 抓取）、`literature-review`（PubMed／bioRxiv／arXiv／Semantic Scholar 多库）、`market-research-reports`（经 `research-lookup` 取数）、`lamindb`（涉 AWS S3／GCS／MinIO／Cloudflare R2 与 W&B／MLflow 绑定）、`marginal-tracker`（外接 Finance Data MCP）、`career-future-mirror`（WebSearch）、`hosted-agents`、`labarchive-integration`、`latchbio-integration`、`esm`（Forge API token）、`gget`（`--api_key`＋COSMIC 凭据）、`denario`（LLM provider key）、`database-lookup`（18 个 `*_API_KEY`）、`ginkgo-cloud-lab`（外部付费）、`bioservices`（外部生物数据库 API）、`fluidsim`（自述 `No API keys or authentication required`——本棒唯一**明示免凭据**者）。

**本棒处置**：⛔ **0 外部网络请求、0 LLM/API 调用、0 数据抓取**；本棒全部动作仅为**本地只读加载 + 本产出件写盘**。

### §4.6 冒名 / 署名风险（**须如实署名，不冒充他方**）

部分 `SKILL.md` 以他人名义署名（如 K-Dense Inc.、Clayton Young / @borealBytes、AHK Strategies、Andrey Fedorov 等）。**本棒严格区分**：

- 加载回内容里的 `skill-author` 是**该技能作者**，**不是本棒产物作者**；
- **本棒产出件署名 = `doc-writer`（`agent-0032834a3e04`）**，**不冒充** Trae code / KIMI / GLM / coze 等任何他方名头；
- 涉 arXiv 号、社媒号、DOI 等外部标识（如 `latent-briefing` 的 arXiv `2602.16284`/`2512.24601` 与 `x.com/RampLabs/...`、`long-horizon-prompting` 的 claim 断言），本棒**只原样登记、不作真伪背书**。

<!-- RISK-END -->

---

## §5 自核节

### §5.1 落盘前后复算（0 覆写自证）

| 项 | 落名前 | 落盘后（终态） |
|---|---|---|
| 目标路径存在性 | `results/_skill_call_surface_probe_supplement_a_2026_09_30.md` **exists=False**（2 轮 × 4 目录 ＋ 全仓 glob 均 0 命中，仅命中首件） | **新建 1 件**（**0 覆写**） |
| 首件 0 回改 | — | 首件 `112346df64fb` **0 字节触动**，mtime 仍为 **16:52:00**（本棒全程仅 `Read` ＋ 只读 `Get-FileHash`） |
| 普查件（**他棒追加，非本棒所为**） | 本棒首次读取时：`e96d99ff9e75` / 55,374 B | 终态：`e6be7b122b59` / 58,659 B / 532 行 / LF / 无 BOM，mtime **17:23:33** |

**⚠️ 普查件变动的如实说明（不推诿、不虚报）**：

- 普查件在**本棒工作时段内**（mtime 17:23:33，落在本棒批次 D 与批次 E 之间）被改写，**本棒全程未对其执行任何写操作**（仅 `Read` 与只读 `Get-FileHash`）；
- 读其文末可确认变动来源为**另一棒**：署「**Mavis 团队 evidence-auditor（`agent-11335500b168`）· 文末追加棒**」，且**其自身如实登记了追加前值** `e96d99ff9e75` / 55,340 B / 509 行（LF）——为**追加式**写入，非覆写；
- **口径差说明**：本棒首次读取所得 **55,374 B** 与对方自述追加前值 **55,340 B** 相差 **34 B**。本棒**不判定**该差因（可能为读取时点与追加时点之间已有第三棒追加，或行尾/编码计数口径差异），**仅如实登记两值并存**；
- **对甲半结论的影响：0**。甲半 92 枚的判定依据是**盘上 223 目录实枚举**与**本件表内逐枚 `Skill` 实调**，二者均不依赖普查件内容；普查件在本棒仅作 §2.4 `name` 差异与三面同名对照的参考件。

### §5.2 完成度与余量（如实登记）

| 项 | 状态 |
|---|---|
| 甲半 92 枚 `Skill` 实调 | **92 / 92 完成（100%）** |
| 成功 / 失败 | **92 / 0** |
| 乙半 91 枚（第 93–183 位） | **不在本棒范围**（由并联棒执行），本棒**0 覆盖**、**0 断言**其结果 |
| 上下文余量 | 本棒已消化 92 枚全量正文（约 1.40 MB），**未因上下文溢出任一枚丢失**：分 5 批加载、每批即刻落盘，故余量紧张未致数据丢失 |
| 时刻列可信度 | ⚠️ 见下 |

**⚠️ 逐例「时刻」列的可信度分档（如实交代，不掩盖）**：

- **实测档（可信）**：本棒批次 A–E 的 14 行（`matchms`／`landing-page-generator`／`labarchive-integration`／`latchbio-integration`／`citation-management`／`lamindb`／`latent-briefing`／`markdown-mermaid-writing`／`marginal-tracker`／`markitdown`／`literature-review`／`long-horizon-prompting`／`market-research-reports`／`latex-posters`），均标注「（实测）」，取值来自加载批次当时 `Get-Date` 实测；
- **存疑档（须打折看待）**：#1–#79 中先前批次所记 17:16–18:04 时刻。**自核发现其内部矛盾**——表内所记最晚时刻（18:04）**晚于本文件当时的末次写入 mtime（17:20:43 ＝ 09:20:43 UTC）**，物理上不可能。据此判定该批时刻多为**估记/顺推**而非挂钟实测；
- **处置**：按「0 回改・追加勘误」纪律，**不回改历史行**，仅在此分档登记。**时刻列整体不可作为精确审计依据**；枚数、字节、SHA-12、命中面等**可复算字段不受影响**。

### §5.3 诚实边界（不夸大 · 不误导）

1. **加载 ≠ 遵从**：92 枚 `SKILL.md` 全文仅作**惰性数据**登记；其中的凭据索取、冒名、外发、写盘、联网、指令覆盖等**一律 0 遵从**（§4 逐类登记）。
2. **0 外部动作**：0 外部网络、0 LLM/API 调用、0 deploy/发布、0 key 读取与落盘、0 系统级装包、0 用户文件移动；本棒**唯一**写盘对象为本自有产出件（新建、0 覆写）。
3. **无文件名直读冒充**：92 枚**全部经 `Skill` 工具真实加载**取得，无一以 `Read` 文件内容冒充调用结果。
4. **结论范围仅限甲半**：92 / 92 成功、92/92 用户面命中，**只对甲半第 1–92 位成立**；**不可外推**至乙半 91 枚或全部 223 枚。
5. **未穷举处已标注**：§3.4 的 license／skill-author 分布、§3.5 风险枚数凡标「≥」或「未逐行断言」者，**均为至少核出、非穷举**；风险族计数以 §2 表内逐行标注为准。
6. **外部标识未核**：`latent-briefing`／`long-horizon-prompting` 等内含的 arXiv 号、社媒号、DOI、`claim-*` 断言，**本棒只原样登记、不联网核实、不作真伪背书**（0 外部网络纪律）。
7. **作者 ≠ 出证人**：表内 `skill-author` 为各技能作者；**本件出证 ＝ doc-writer（`agent-0032834a3e04`）**，不冒充任何他方名头（§4.6）。
8. **并联棒变动不归本棒**：普查件在本棒时段被 evidence-auditor 棒追加（§5.1 已如实说明）；本棒 0 参与、0 覆写，**两值口径差未作判定**。
9. **时刻列打折**：见 §5.2 时分档，#1–#79 时刻存疑，**已标注不作为审计依据**。
10. **本棒自查纠错留痕**：本棒曾出现「表行先写成成功再实调」「表行序号错位到 `gi63`（首件已测项）」「最小件误判为 `matchms`」等自身错误，**均在落盘前后当场发现并修正**；`citation-management` 欠账（曾误标后删除）已在本轮**重新实调并补录为成功**（SHA-12 `a5f786d9dac0` / 32,594 B 复核一致）。

**出证｜Mavis 团队 doc-writer（`agent-0032834a3e04`）· 甲半补测棒｜2026-09-30**
