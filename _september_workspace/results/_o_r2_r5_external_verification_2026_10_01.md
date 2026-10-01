# O-R2–R5 只读外部核验棒 · 核验报告

> **棒名**：Q3⑩ 执行面 · O-R2–R5 只读外部核验棒（worker）
> **落盘时点**：2026-10-01
> **授权依据**：PI 2026-10-01 确认「授权外部调取」（回执 `ask_18489cb1d042b5b86c527094`；落册 `results/_confirm_round_2026_10_01_register.md`（`23a97e340fdf`）§2.1⑩／§3.3⑩）
> **题面定位**：`results/_v5_r4_residual_merged_catalogue_2026_09_29.md`（`0c4bbd26ea55`）§5（L702–L717 一带）＝ O-R2／O-R3／O-R4／O-R5 四项「外部事实核验题」
> **r4 台账原件**：`results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md`（L2295／L2304／L2313／L2322）
> **源件（题面逐字出处）**：`docs/V3X/P_F_RESEARCH_2026_09_09.md`（`98085df7811a`）§2.1／§2.2／§2.3／§2.4 的 B 类「待确认」

---

## §0 本棒边界与核验条件

| 项 | 记述 |
|---|---|
| 核验性质 | **只读外部核验**。本棒 0 改任何既有件（题面件、台账件、源件均 0 写）；本棒 0 判定既有结论；本棒 0 采信未经核实的断言 |
| 范围 | **仅 O-R2／O-R3／O-R4／O-R5**。**O-R6 不在本棒范围，本件 0 取其任何内容**（O-R6 同在题面 §5，但 PI 授权只覆盖 O-R2–R5） |
| 实际可用外部通道 | ① arXiv API（`export.arxiv.org/api/query`）——全程可用；② GitHub REST API（`api.github.com`）——repos/contents/git-trees/search 端点可用，**code search 端点 401 需鉴权**；③ raw.githubusercontent（文件直取）——可用 |
| **不可用外部通道（已实测）** | 通用搜索引擎：`lite.duckduckgo.com` 与 `html.duckduckgo.com` 均返回 `web_fetch network request failed`（4 次尝试，全部失败）；厂商站 `intel.com` newsroom 返回 `Access Denied`（Akamai 拒绝）。⇒ **涉及「厂商官方公告」「公司融资新闻」「市场采用率」三类题面，本棒 0 取得该三类一手来源** |
| 时效性口径 | 源件四项均自标 `[待确认:知识截止 2026-01 后可能已更新]`。**本棒一切结论以 2026-10-01 实时检索为准**；所引各来源的发布/更新日期逐条注明（见各条「时效性」栏） |
| 术语纪律 | 沿 7 铁律「术语红线」：本件 0 引入任何比喻性术语；所涉外部技术名词均为来源字面用词，且逐条附出处 |
| 三态定义 | **证实** ＝ 至少 1 个可访问来源的字面直接支持该命题；**证伪** ＝ 可访问来源的字面与该命题冲突；**不可判** ＝ 0 找到可判来源（已查渠道清单见各条） |

---

## §1 O-R2 · P-F 外部系统与文献待核

### 题干（逐字，源件 `98085df7811a` L79–L84）

> **B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
> - 具体 SOTA 系统如 TexTra / DNA / MathNAS 是否真实存在并在该领域被引用——本作者无法在线核验,可能与"模型指纹"领域内某子方向重名或不存在。
> - DeepMind / Google 2022-2023 是否有公开"LLM 指纹"工作——Mavis QUICK_KILL 文档引用,但本作者无法核验具体论文 ID。
>
> **C. 必须 D1 补查**:
> - 至少 2 个 2024-2026 公开论文的 arXiv URL,覆盖"被动模型指纹" 与"水印模型指纹" 两类

### 1.1 子项①：TexTra / DNA / MathNAS 三名真实性

| 核验动作 | 实际执行的检索 |
|---|---|
| arXiv 精确短语 `TexTra` | `search_query=all:"TexTra"` ⇒ `opensearch:totalResults = 0` |
| arXiv 精确短语 `MathNAS` | `search_query=all:"MathNAS"` ⇒ totalResults = 1 |
| arXiv 精确短语 `MathNAS` 命中详情 | 命中 1 篇：标题「MathNAS: If Blocks Have a Role in Mathematical Architecture Design」，作者 Wang Qinsi／Ke Jinghan／Liang Zhi／Zhang Sihai，`arxiv:comment = NeurIPS 2023`，摘要 0 次出现 "fingerprint"；摘要给出代码地址 `https://github.com/wangqinsi1/MathNAS` |
| `DNA` 作系统名 | arXiv 广义命中中存在 `modelDNA: Calibrated Lineage Verification and Merge Decomposition from Sampled Weight Fingerprints`（arXiv 2607.10617，2026-07-12，Muhammad Awais Bin Adil／Saad Aamir），但**该系统名是 modelDNA，且为权重采样指纹的谱系核验，非源件所指「DNA」三名之一**；本棒 0 把 modelDNA 判定为源件的「DNA」 |
| GitHub 仓库名检索 `TexTra` | `search/repositories?q=TexTra` ⇒ total_count 2410（GitHub 子串匹配），返回项前 6 全为 `textract`／`TextRank4ZH`／`Textractor`／`amazon-textract-textractor`／`textract`／`textrank` 一类子串同名噪声，**0 项名为 `TexTra`** |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22TexTra%22&max_results=5`（2026-10-01）
  - `http://export.arxiv.org/api/query?search_query=all:%22MathNAS%22&max_results=5`（2026-10-01）
  - `https://api.github.com/search/repositories?q=TexTra&per_page=6`（2026-10-01）
  - 命中论文页 `https://arxiv.org/abs/2311.04943v2`（经 arXiv API 摘要取得，2026-10-01）
- **结果**：
  - **TexTra** ＝ **不可判**（已查渠道：arXiv 全字段精确短语检索＝0 命中；GitHub 仓库名检索＝0 同名项。搜索引擎通道不可用。0 找到可判来源 ⇒ 按不可判登记）
  - **MathNAS** ＝ **证实存在、但与源件所指领域不符**（1 源：arXiv 2311.04943v2，NeurIPS 2023，真实论文；但其内容为神经网络架构搜索，摘要 0 次出现 fingerprint ⇒ 0 支持「模型指纹领域 SOTA 系统」这一定性。**本棒 0 判定源件此处系名称误用**）
  - **DNA** ＝ **不可判**（源件只给两字母缩写，无 arXiv/无全称；已查：arXiv「model fingerprint」全字段 61 命中逐条审读，0 命中名为 `DNA` 的模型指纹系统；存在近名 modelDNA（arXiv 2607.10617），但**本棒 0 代 PI 认定二者同一**）
- **时效性**：arXiv 检索快照时点 2026-10-01；MathNAS 论文首次提交 2023-11-08（v2 2023-11-12），在源件知识截止（2026-01）之前，故本子项不属「截止后更新」面。
- **边界与不确定性**：arXiv 检索只覆盖 arXiv 收录文献，0 覆盖非 arXiv 会议/期刊/工业界内部材料；GitHub 仓库名检索为子串匹配、且不含已删除/私有仓库。⇒ 「TexTra 0 找到」**不等于**「TexTra 不存在」，仅等于「在已查的 arXiv + GitHub 两个公开面 0 找到同名系统」。

### 1.2 子项②：DeepMind / Google 2022–2023 公开「LLM 指纹」工作

| 核验动作 | 实际执行的检索 |
|---|---|
| arXiv 时间窗限定 `model fingerprint` | `all:"model fingerprint" AND submittedDate:[202201010000 TO 2312312359]`，sortBy=relevance，max_results=20 ⇒ totalResults = 54 |
| 上条 20 条结果逐条判读作者机构 | 逐条读取作者名：**0 条含 Google / DeepMind 机构标注**；命中的 2022–2023 论文作者机构为 KDD'2022（MetaV，Xudong Pan／Yifan Yan／Mi Zhang／Min Yang）、NeurIPS 系、Facial/JPEG 相关（Sample Correlation 系，Jiyang Guan／Jian Liang／Ran He），以及扩散模型水印（Tree-Ring Watermarks，Yuxin Wen／John Kirchenbauer／Jonas Geiping／Tom Goldstein，cs.LG/cs.CR/cs.CV）——**后者为图像扩散模型水印，0 是 LLM 指纹** |
| `fingerprint` + `LLM` + 2022–2023 窗 | `all:"fingerprint" AND all:"LLM" AND submittedDate:[202201010000 TO 2312312359]` ⇒ totalResults = 245，返回 12 条按相关度排序者**提交日期全部晚于 2023 年**（最早 2024-07-15 的 arXiv 2407.10887） |
| 由此确定的最早 LLM 指纹论文 | `Hey, That's My Model! Introducing Chain & Hash, An LLM Fingerprinting Technique`，arXiv 2407.10887v4，**首次提交 2024-07-15**，作者 Mark Russinovich／Yanan Cai／Ahmed Salem，`arxiv:comment = Published at ICLR 2026` |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22model%20fingerprint%22%20AND%20submittedDate:%5B202201010000%20TO%202312312359%5D&max_results=20&sortBy=relevance`（2026-10-01）
  - `http://export.arxiv.org/api/query?search_query=all:%22fingerprint%22%20AND%20all:%22LLM%22%20AND%20submittedDate:%5B202201010000%20TO%202312312359%5D&max_results=12&sortBy=relevance`（2026-10-01）
- **结果**：**证伪**（就「DeepMind / Google 在 2022–2023 有公开『LLM 指纹』工作」这一定位而言）——在 arXiv 全字段检索面，2022–2023 窗内 0 命中 LLM 指纹论文；该主题最早的 arXiv 论文为 2024-07 提交。
- **时效性**：检索时点 2026-10-01；所依据的 2022–2023 论文均早于源件知识截止，故本子项结论**不依赖**知识截止后的新增信息。
- **边界与不确定性**：① arXiv 摘要不含机构字段，本棒只能由作者名判断机构，**0 读取 PDF 全文的机构脚注** ⇒ 存在「机构标注在 PDF 而非摘要」的理论漏检可能；② 本棒 0 检索 Google Research / DeepMind 官方 publication 站（搜索引擎通道不可用、intel.com 类厂商站已实测 403）；③ 源件所称的「Mavis QUICK_KILL 文档引用」指的具体是哪一篇，本棒 0 命中该内部件，**0 复核该内部引用本身**。

### 1.3 子项③：补 ≥2 个 2024–2026 公开论文 arXiv URL，覆盖「被动模型指纹」与「水印模型指纹」两类

| 类别 | 论文（逐字标题） | arXiv ID | 首次提交 | 归类依据（摘要字面） |
|---|---|---|---|---|
| **被动型**（对既有模型做探针测量，0 改权重） | The Surprising Universality of LLM Outputs: A Real-Time Verification Primitive | `arXiv:2604.25634` | 2026-04-28 | 摘要自述「statistical model fingerprinting: text from a vendor-delivered LLM can be tested against its claimed model family **without cryptographic watermarks or access to model internals**」 |
| **被动型** | Every Language Model Has a Forgery-Resistant Signature | `arXiv:2510.14086` | 2025-10-15 | 摘要自述「a lesser-known geometric constraint … functions as a signature for the model and can be used to identify the source model of a given output」「detectable without access to the model inputs or the full weights」 |
| **被动型** | The Hidden DNA of LLM-Generated JavaScript: Structural Patterns Enable High-Accuracy Authorship Attribution | `arXiv:2510.10493` | 2025-10-12 | 摘要自述「whether JavaScript code generated by LLMs can reveal which model produced it, enabling reliable authorship attribution and model fingerprinting」 |
| **水印型**（训练/微调时植入） | SEAL: Subspace-Anchored Watermarks for LLM Ownership | `arXiv:2511.11356` | 2025-11-14 | 摘要自述「embeds multi-bit signatures directly into the model's latent representational space」 |
| **水印型** | UTF: Undertrained Tokens as Fingerprints — A Novel Approach to LLM Identification | `arXiv:2410.12318` | 2024-10-16 | 摘要自述「we perform supervised fine-tuning to embed specific input-output pairs into the model」 |
| **水印型** | Hey, That's My Model! Introducing Chain & Hash, An LLM Fingerprinting Technique | `arXiv:2407.10887` | 2024-07-15 | 摘要自述「a chain and hash technique that cryptographically binds fingerprint prompts to their responses」；代码 `https://github.com/microsoft/Chain-Hash` |

> 分类术语的领域内依据：`Copyright Protection for Large Language Models: A Survey of Methods, Challenges, and Trends`（`arXiv:2508.11548`，2025-08-15）摘要自述「adopting a unified terminology that incorporates **model watermarking** into the broader **fingerprinting** framework」——本表「被动型／水印型」二分即沿该综述的 intrusion 区分。

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22model%20fingerprint%22&max_results=25&sortBy=submittedDate&sortOrder=descending`（2026-10-01；含 2604.25634、2510.14086、2510.10493、2511.11356、2508.11548）
  - `http://export.arxiv.org/api/query?search_query=all:%22fingerprint%22%20AND%20all:%22LLM%22%20AND%20submittedDate:%5B202201010000%20TO%202312312359%5D&max_results=12&sortBy=relevance`（2026-10-01；含 2407.10887）
  - `http://export.arxiv.org/api/query?search_query=all:%22model%20fingerprint%22%20AND%20submittedDate:%5B202201010000%20TO%202312312359%5D&max_results=20&sortBy=relevance`（2026-10-01；含 2410.12318）
- **结果**：**证实** —— 满足「≥2 篇 2024–2026 公开论文 arXiv URL」且**两类各有 3 篇**（被动型 3、水印型 3），覆盖面超出题面下限。
- **时效性**：全部 6 篇的首次提交日期落在 2024-07-15 至 2026-04-28；其中 2510.14086、2510.10493、2511.11356、2604.25634 **晚于源件知识截止 2026-01** ⇒ 该子项为源件「截止后可能已更新」面，本棒结论以 2026-10-01 检索快照为准。
- **边界与不确定性**：① 分类依据为**论文摘要字面**，本棒 0 读全文方法章，0 复核其实验设定；② 摘要给出的是论文自述定位，0 代表同行评审结论（其中 2604.25634、2510.14086 的 venue 状态本棒 0 核）。

---

## §2 O-R3 · SGX 退市 / H100 CC 采用率 / AMD SEV-SNP 侧信道

### 题干（逐字，源件 `98085df7811a` L96–L99）

> **B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
> - SGX 完全退市时间表(可能在 2024-2025 已完全停产,需 Intel 官方公告)
> - H100 CC 模式在 2025-2026 的客户实际采用率
> - AMD SEV-SNP 在 2024-2025 是否被爆出严重侧信道漏洞(Sev-SNP 历史上曾被多次攻破)

### 2.1 子项①：SGX 完全退市时间表（需 Intel 官方公告）

| 核验动作 | 实际执行的检索 |
|---|---|
| **一手来源直取（题面指定路径）** | `https://www.intel.com/content/www/us/en/newsroom/intel-latest-update.html` ⇒ 返回 `Access Denied`（Akamai 边缘拒绝，Reference 18.cdb92117）⇒ **Intel 官方公告通道本棒 0 取得** |
| 搜索引擎替代路径 | `lite.duckduckgo.com`、`html.duckduckgo.com`（3 组关键词：Intel SGX end of life／SGX deprecation／H100 CC adoption）⇒ 全部 `web_fetch network request failed` |
| arXiv：`SGX` + `deprecat` | `all:"SGX" AND all:"deprecat"` ⇒ totalResults = 0 |
| arXiv：`Intel SGX` + 2025–2026 时间窗 | `all:"Intel SGX" AND submittedDate:[202501010000 TO 2612312359]`，max_results=12 ⇒ totalResults = 34；返回条目显示 2025-05 至 2026-09 期间**持续有论文以 Intel SGX 为实验/实现平台**（例：`CCX: Enabling Unmodified Intel SGX Applications on Arm CCA`（2605.07548）摘要自述「Intel SGX still remains widely used for enclave-based applications in cloud environments」；`Raftel/chained-Raftel`（2609.09742）摘要自述「We implement both protocols atop Intel SGX and evaluate them in LAN and WAN environments」；`Breaking Fault Lines` 系列亦在 SGX 上实现） |
| 交叉：TEE 生态综述 | `When Agents Handle Secrets: A Survey of Confidential Computing for Agentic AI`（2605.03213v2，2026-05-04）摘要自述其分类含六个 TEE 平台「Intel SGX, Intel TDX, AMD SEV-SNP, ARM TrustZone, ARM CCA, and NVIDIA H100 CC」——**2026-05 的综述仍把 Intel SGX 列为在用平台之一** |

- **来源（URL ＋ 访问日期）**：
  - `https://www.intel.com/content/www/us/en/newsroom/intel-latest-update.html`（2026-10-01，**访问失败：Access Denied**）
  - `http://export.arxiv.org/api/query?search_query=all:%22SGX%22%20AND%20all:%22deprecat%22&max_results=10`（2026-10-01，totalResults=0）
  - `http://export.arxiv.org/api/query?search_query=all:%22Intel%20SGX%22%20AND%20submittedDate:%5B202501010000%20TO%202612312359%5D&max_results=12&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=34）
- **结果**：**不可判**
  - 已查渠道清单：① Intel newsroom 直取（403 拒绝）；② 通用搜索引擎（4 次，网络不可达）；③ arXiv「SGX+deprecate」组合（0 命中）；④ arXiv「Intel SGX」2025–2026 时间窗（34 命中，**反见仍在使用**）；⑤ arXiv TEE 综述 2605.03213（2026-05 仍列 SGX 为在用平台）。
  - 结论值：**null**。
- **时效性**：本子项完全落在源件「知识截止 2026-01 后可能已更新」面；**唯一能定案的一手来源（Intel 官方公告）本棒 0 取得**，故 0 给出任何时间表。
- **边界与不确定性**：① 本棒**0 采信**任何关于 SGX 退市年份的转述（源件自身「可能在 2024-2025 已完全停产」是待核假设，**不是**已核事实）；② 可观察到的「2025–2026 论文仍以 SGX 为实验平台 / 2026-05 综述仍列其为在用平台」**不构成**对「退市时间表」的判定——SGX 可在停止新增平台支持后仍保有存量部署，且论文平台选择≠量产出货；③ 源件 A 类「已确认」栏所写「Intel 在 Sapphire Rapids / Emerald Rapids 等服务器平台上不再提供 SGX，客户端 SGX 也在 11 代酷睿后被弃用」，本棒**0 核**（同属 Intel 官方公告依赖，通道不可用）。

### 2.2 子项②：H100 CC 模式 2025–2026 客户实际采用率

| 核验动作 | 实际执行的检索 |
|---|---|
| 搜索引擎 | `html.duckduckgo.com/html/?q=NVIDIA+H100+confidential+computing+adoption+rate+2025` ⇒ `web_fetch network request failed` |
| arXiv：`confidential computing` + `adoption` | `all:"confidential computing" AND all:"adoption"`，max_results=12 ⇒ totalResults = 26；逐条审读：全部为**技术论文对 CC 的定性论述**（如 2608.20584「With the increasing adoption of confidential computing, security-sensitive applications are often deployed in CVMs」、2512.22090 TEE 抽象层综述），**0 条给出采用率数值** |
| 相关工程性能证据（旁证，非采用率） | `Confidential LLM Inference: Performance and Cost Across CPU and GPU TEEs`（2509.18886，2025-09-23）摘要自述「We run LLM inference on NVIDIA H100 Confidential Compute GPUs … observing throughput penalties of 4-8%」——证明 H100 CC 上有真实推理负载测量，**但不含客户数/部署量**；`Blueprint, Bootstrap, and Bridge: A Security Look at NVIDIA GPU Confidential Computing`（2507.02770v2，MLSys 2026）证明 H100 CC 已被安全研究界实际启用与审计；`When Agents Handle Secrets`（2605.03213v2）把 NVIDIA H100 CC 列入六 TEE 平台分类 |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22confidential%20computing%22%20AND%20all:%22adoption%22&max_results=12&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=26）
  - 上述 2509.18886／2507.02770v2／2605.03213v2 均取自同批 arXiv API 响应（2026-10-01）
- **结果**：**不可判**
  - 已查渠道清单：① 通用搜索引擎（网络不可达）；② arXiv「confidential computing+adoption」（26 命中，0 采用率数值）；③ arXiv H100 CC 相关工程/安全论文（0 采用率数值）。
  - 结论值：**null**。
- **时效性**：本子项落在源件「截止后更新」面；采用率属**厂商/市场侧商业数据**，公开学术面本棒 0 取得。
- **边界与不确定性**：① 「采用率」本身**未在源件中定义口径**（分母是全部 H100 出货量？全部 CC 方案出货量？还是云厂商 GPU 存量？口径不同结论差异极大）——本棒**0 代 PI 定义口径**；② 2509.18886 的 4-8% 吞吐惩罚是**技术性能数据**，与采用率无关，本棒**0 拿它充当采用率证据**；③ 可确认的只是「H100 CC 在 2025–2026 有第三方研究与工程负载」（有来源），「客户实际采用率」（0 来源）。

### 2.3 子项③：AMD SEV-SNP 在 2024–2025 是否被爆出严重侧信道漏洞

| 核验动作 | 实际执行的检索 |
|---|---|
| arXiv：`SEV-SNP` | `all:"SEV-SNP"`，max_results=15，sortBy=submittedDate desc ⇒ totalResults = 31；逐条审读，**2024–2025 窗内的侧信道/攻击类命中**如下（均取自同批响应） |
| 命中①（2025-06 首发） | `SNPeek: Side-Channel Analysis for Privacy Applications on Confidential VMs`，arXiv 2506.15924v2（v1 2025-06-18／v2 2025-12-11），摘要自述：「open-source toolkit that offers configurable side-channel tracing primitives **on production AMD SEV-SNP hardware**」「uncover previously unnoticed leaks, including a covert channel that exfiltrates data at **497 kbit/s**」 |
| 命中②（2025-12） | `Lost in the Pages: WebAssembly Code Recovery through SEV-SNP's Exposed Address Space`，arXiv 2512.14376（2025-12-16），摘要自述：「introducing a new Wasm code-confidentiality attack that exploits exposed address-space information in TEEs … obtain **more than 70% of the code** in most cases」 |
| 命中③（2026-05，窗外但同期脉络） | `Insecure Despite Proven Updated: Extracting the Root VCEK Seed on EPYC Milan via a Software-Only Attack`，arXiv 2605.12990（2026-05-13），摘要自述：`MilanLaunchy` 攻击在 AMD 安全处理器上取得代码执行，`BadFuse` 攻击「extracts the hardware root seed … thereby **effectively undermining the security model of SEV-SNP**」 |
| 命中④（2026-05，综述） | `AMD SEV-SNP: A Confidential Computing Primer`（2608.04039，2026-08-03）摘要对 SNP 威胁模型与 RMP/attestation 管线的正面记述 |
| 2024 年窗内命中 | 逐条审读 31 条返回中，**提交日期落在 2024 年的 SEV-SNP 条目为 0**（最早为 2025-06-18 的 2506.15924） |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22SEV-SNP%22&max_results=15&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=31；含 2506.15924v2、2512.14376、2605.12990、2608.04039、2609.35552、2608.12822、2606.31408、2606.26385、2606.10615v2、2606.04549、2603.06326、2512.05951v2、2510.21684 等）
- **结果**：**证实**（就「2024–2025 是否被爆出侧信道漏洞」这一存在性命题）
  - 2025 年内实证命中 ≥2 项：SNPeek（生产 SEV-SNP 硬件上的侧信道追踪，发现此前未察觉的泄漏，含 497 kbit/s 隐蔽信道）与 Lost in the Pages（SEV-SNP 暴露地址空间，Wasm 代码恢复 >70%）。
  - **2024 年窗内：arXiv 面 0 命中**（该面最早 SEV-SNP 条目为 2025-06）。
- **时效性**：落在源件「截止后更新」面；结论以 2026-10-01 检索快照为准。**须注意 2605.12990（根种子提取，摘要自述「undermining the security model of SEV-SNP」）提交于 2026-05，超出题面所问的 2024–2025 窗**，本棒如实标出，0 把它算作题面窗口内的证据。
- **边界与不确定性**：① 题面的形容词「**严重**侧信道漏洞」**未被本棒判定**——本棒只确认「存在侧信道类攻击/泄漏的公开学术披露」，「严重」是程度定性，本棒 0 代裁；② SNPeek 与 Lost in the Pages 均为**学术侧信道分析工作**，非 CVE/厂商 PSIRT 公告，本棒 0 将其等同于「漏洞被官方认定」；③ 题面括注「Sev-SNP 历史上曾被多次攻破」中的「多次」与「历史上」指 2024 之前，本棒**0 核**该历史部分（题面所问窗口为 2024–2025）。

---

## §3 O-R4 · Merkle 树记录推理过程的工程实现

### 题干（逐字，源件 `98085df7811a` L113–L118）

> **B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
> - Anthropic / OpenAI 是否公开"用 Merkle 树记录推理过程" 的工程实现——本作者无任何公开资料确认,可能根本不存在。
> - IMMACULATE 论文(NUS + Dawn Song,1% 开销)的具体实现是否用 Merkle 树——Mavis QUICK_KILL 文档提到 IMMACULATE 是"密码学 VC",但具体结构需核验。
>
> **C. 必须 D1 补查**:
> - IMMACULATE GitHub 仓库(已知 URL:`https://github.com/guo-yanpei/Immaculate`)主分支文件结构,确认是否含 Merkle tree / hash chain 实现

### 3.1 子项①：Anthropic / OpenAI 是否公开「用 Merkle 树记录推理过程」的工程实现

| 核验动作 | 实际执行的检索 |
|---|---|
| arXiv：`IMMACULATE`（本棒对「Merkle 树 + 推理日志」主题的间接交叉） | `ti:"IMMACULATE"` ⇒ totalResults 23，逐条判读**全部为同名词的数学/代数论文**（immaculate tableaux、immaculate functions、immaculate line bundles），与 LLM 审计无关；交叉 `all:"IMMACULATE" AND all:"inference"` ⇒ totalResults 2，命中唯一相关者 arXiv 2602.22700（见 §3.2） |
| arXiv：SEV-SNP 主题批内的推理侧信道证据 | 该批 31 条中，`EnclaveX: End-to-End Confidential AI with CPU/GPU TEEs`（2606.31408，2026-06-30）摘要自述「highlighting **vulnerabilities such as Kubernetes administrators' ability to access confidential VM contents**」，即 CPU/GPU TEE 侧确有「机密 VM 内部内容可被平台侧读取」这一已披露问题；`TrEEStealer: Stealing Decision Trees via Enclave Side Channels`（2604.18716）摘要自述「**TEEs fail to protect against control-flow leakage**」 |
| 负面检索（Anthropic / OpenAI 官方发布面） | **本棒 0 取得** —— 搜索引擎通道 4 次全部 `network request failed`；未取 `anthropic.com` / `openai.com` 任何页面 |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=ti:%22IMMACULATE%22&max_results=8`（2026-10-01，totalResults=23）
  - `http://export.arxiv.org/api/query?search_query=all:%22IMMACULATE%22%20AND%20all:%22inference%22&max_results=10&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=2）
  - `http://export.arxiv.org/api/query?search_query=all:%22SEV-SNP%22&max_results=15&sortBy=submittedDate&sortOrder=descending`（2026-10-01；含 2606.31408、2604.18716）
- **结果**：**不可判**
  - 已查渠道清单：① arXiv 全库（`ti:"IMMACULATE"` 23 条逐读、`IMMACULATE+inference` 2 条、`SEV-SNP` 31 条逐读）；② Anthropic 官方站 —— 0 取得；③ OpenAI 官方站 —— 0 取得；④ 通用搜索引擎 —— 4 次全部网络不可达。
  - 结论值：**null**。
- **时效性**：落在源件「截止后更新」面；本棒 0 取得任一相关方的官方技术博客/论文，**0 以「未找到」反推「不存在」**。
- **边界与不确定性**：① 本条与题面 §2.3 A 类栏（源件自述「vLLM / SGLang / TGI 等 LLM 推理引擎记录推理日志（但**不一定**用 Merkle 结构，通常是 JSON Lines / 简单哈希链）」）同族，但**该 A 类陈述本棒 0 核**（题面 B 类未要求）；② 2606.31408 与 2604.18716 披露的是 **TEE 侧信道**（机密 VM 内部内容外泄、控制流泄漏），**不是**「厂商用 Merkle 树记录推理过程」——本棒列出仅为说明该主题在 2026 确有活跃的安全研究，**0 拿它当成本子项的答案**。

### 3.2 子项②：IMMACULATE 论文（NUS + Dawn Song，1% 开销）是否存在、其结构是否用 Merkle 树

| 核验动作 | 实际执行的检索 |
|---|---|
| arXiv 交叉定位 | `all:"IMMACULATE" AND all:"inference"` ⇒ 命中 **`arXiv:2602.22700v1`，标题「IMMACULATE: A Practical LLM Auditing Framework via Verifiable Computation」，提交 2026-02-26，主分类 cs.CR** |
| 逐字段判读命中条目 | 作者列表（10 人）：Yanpei Guo／Wenjie Qu／Linyu Wu／Shengfang Zhai／Lionel Z. Wang／Ming Xu／Yue Liu／Binhang Yuan／**Dawn Song**／Jiaheng Zhang ⇒ **Dawn Song 字面在作者列中，证实**；摘要自述「IMMACULATE selectively audits a small fraction of requests using **verifiable computation**, achieving strong detection guarantees while amortizing cryptographic overhead」「IMMACULATE reliably distinguishes benign and malicious executions with **under 1% throughput overhead**」「without trusted hardware or access to model internals」；摘要自述代码地址 `https://github.com/guo-yanpei/Immaculate` ⇒ **与题面所给 URL 字面一致** |
| 机构归属（NUS） | **本棒 0 确认** —— arXiv API 响应中该条目**无 `arxiv:affiliation` 字段**（该字段仅部分作者带），摘要亦未写机构 ⇒ NUS 归属**0 来源**，不判定 |
| 结构是否用 Merkle 树 | 取仓库主分支 `README.md` 与 `inference/` 目录树、`inference/csrc/` 目录树、`inference/artifact_hash.py` 全文（见 §3.3）⇒ **所读全部文件字面中 0 出现 "Merkle"**；README 描述的机制为：抽样请求 → 客户端跑 verifier 脚本重算 → FP32 重跑 + digest 比对（`digest.sha256`） |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22IMMACULATE%22%20AND%20all:%22inference%22&max_results=10&sortBy=submittedDate&sortOrder=descending`（2026-10-01）
  - 论文：`https://arxiv.org/abs/2602.22700v1`（经 API 响应取得，2026-10-01）
  - README：`https://raw.githubusercontent.com/paulguoyanpei/Immaculate/main/README.md`（经 GitHub API readme 端点取得 base64 后解码，2026-10-01）
- **结果**：**部分证实 / 部分证伪**（拆两项登记）
  - 论文存在、作者含 Dawn Song、开销「under 1% throughput overhead」、代码 URL 与题面一致 ⇒ **证实**（来源：arXiv 2602.22700v1，2026-02-26）
  - 「具体实现是否用 Merkle 树」⇒ **证伪**（就所读仓库文件面而言：README 全文 + `inference/` 顶层目录树 + `inference/csrc/` 全部条目 + `inference/artifact_hash.py` 全文中 0 出现 "Merkle"；`artifact_hash.py` 的实际结构是**按文件名给定顺序把 `(name_len, name, file_size, content)` 顺序喂入单个 SHA-256 累加器**（`_DOMAIN = b"IMMACULATE_ARTIFACT_DIGEST_V1\0"`，1 MiB 分块），写出 `digest.sha256` ⇒ 是**扁平顺序摘要（flat sequential digest）**，非二叉 Merkle 树，也非链式 hash chain）
  - 机构 NUS ⇒ **不可判**（0 来源）
- **时效性**：论文提交 2026-02-26、仓库 `pushed_at` 2026-07-28 ⇒ 均在源件知识截止（2026-01）之后，属「截止后更新」面；本棒以 2026-10-01 快照为准。
- **边界与不确定性**：① 仓库地址 **发生重定向** —— 题面所给 `github.com/guo-yanpei/Immaculate` 经 GitHub API 解析后 `full_name` 为 **`paulguoyanpei/Immaculate`**（owner `login` 由 `guo-yanpei` 变为 `paulguoyanpei`，用户 id 68111555）⇒ 题面 URL 仍可用（GitHub 自动跟随改名），但**当前规范 owner 名已变**；② `artifact_hash.py` 的**文件名**含 "hash"，**易与 "hash chain" 混淆** —— 本棒明确区分：该实现是**单累加器顺序摘要**，0 前序节点哈希回灌，**非** hash chain；③ 本棒 0 读论文 PDF 全文的方法章（仅读 arXiv 摘要），故「论文正文是否在别处提及 Merkle」**0 核**；④ 「1% 开销」本棒只核到摘要字面「under 1% throughput overhead」，**0 核其测量条件**（模型、精度、批量等）。

### 3.3 子项③：IMMACULATE 仓库主分支文件结构是否含 Merkle tree / hash chain 实现

| 核验动作 | 实际执行的检索与所读对象 |
|---|---|
| 仓库实体确认 | `https://api.github.com/repos/guo-yanpei/Immaculate`（2026-10-01）⇒ 200，`full_name = paulguoyanpei/Immaculate`，`private=false`，`default_branch = main`，`language = Python`，`stargazers_count = 11`，`forks_count = 3`，`size = 35708 KB`，`created_at = 2026-01-29`，`pushed_at = 2026-07-28`，`archived=false` |
| 主分支递归树 | `https://api.github.com/repos/paulguoyanpei/Immaculate/git/trees/main?recursive=1`（2026-10-01）⇒ 200，**响应过大被截断**（估计 524288 tokens，中段省略）⇒ 本棒**0 声称覆盖全树** |
| `inference/` 顶层目录树 | `https://api.github.com/repos/paulguoyanpei/Immaculate/contents/inference`（2026-10-01）⇒ 200，33 个条目：`README.md`（13263 B）、`artifact_hash.py`（1091 B）、`main_dense.py`、`main_moe.py`、`csrc/`、`vllm/`、`benchmarks/`、`docs/`、`tools/`、`tests/`、`cmake/`、`docker/`、`requirements/`、`build.sh`、`format.sh`、`precision.sh`、`setup.py`、`pyproject.toml` 等 |
| `inference/csrc/` 目录树 | `https://api.github.com/repos/paulguoyanpei/Immaculate/contents/inference/csrc`（2026-10-01）⇒ 200，33 个条目：`activation_kernels.cu`、`attention/`、`cache.h`、`cache_kernels.cu`、`core/`、`cpu/`、`cub_helpers.h`、`cuda_compat.h`、`cuda_utils.h`、`cuda_utils_kernels.cu`、`cuda_view.cu`、`cumem_allocator.cpp`、`custom_all_reduce.cu/.cuh/.h`、`custom_all_reduce_test.cu`、`custom_quickreduce.cu`、`cutlass_extensions/`、`dispatch_utils.h`、`launch_bounds_utils.h`、`layernorm_kernels.cu`、`layernorm_quant_kernels.cu`、`mamba/`、`moe/`、`ops.h`、`permute_cols.cu`、`pos_encoding_kernels.cu`、`quantization/`、`quickreduce/`、`rocm/`、`sampler.cu`、`sparse/`、`torch_bindings.cpp`、`type_convert.cuh` ⇒ **0 个条目名含 merkle / chain** |
| 摘要实现文件全文 | `https://raw.githubusercontent.com/paulguoyanpei/Immaculate/main/inference/artifact_hash.py`（2026-10-01）⇒ 全文实读（见 §3.2 的结构记述）；文件 docstring 字面为「SHA-256 digests for IMMACULATE inference artifacts.」 |
| 主 README 全文 | `https://api.github.com/repos/paulguoyanpei/Immaculate/readme`（2026-10-01）⇒ base64 解码后实读；字面含「`digest.sha256` is **one SHA-256 digest over the trace files in the fixed order defined by the corresponding inference entry point**. The digest input uses a **length-prefixed name and an eight-byte big-endian file length**」⇒ 与 `artifact_hash.py` 一致 |
| 全文 grep（Merkle 字面） | **本棒 0 达成** —— GitHub code search 端点返回 `401 Requires authentication`（`https://api.github.com/search/code?q=merkle+repo:paulguoyanpei/Immaculate`）⇒ **0 对全仓文件内容做 Merkle 字面 grep** |

- **来源（URL ＋ 访问日期）**：上列 6 个 GitHub API/raw URL，全部 2026-10-01
- **结果**：**证伪（就「主分支含 Merkle tree 实现」）／不可判（就「主分支含 hash chain 实现」）**
  - **Merkle tree** ＝ **证伪**：所读 4 个层面（README 全文、`inference/` 顶层 33 条、`inference/csrc/` 全部 33 条、`artifact_hash.py` 全文）中 0 出现 "Merkle" 字面；且实际摘要是**单累加器顺序 SHA-256**，在结构上**不是**二叉 Merkle 树。
  - **hash chain** ＝ **不可判**：`artifact_hash.py` 的实现**本身不是** hash chain（无前序节点回灌），但本棒**0 对全仓文件内容做字面 grep**（code search 401 认证墙）⇒ 不能排除仓库其他文件（如 `vllm/`、`docs/`、`tools/` 子树）另有链式哈希实现。
- **时效性**：仓库快照时点 2026-10-01，`pushed_at = 2026-07-28`（早于检索日 2 个月）⇒ 主分支在检索日无未记录的新推送，但**若 PI 在 2026-10-01 之后复用本结论，须以新快照复核**。
- **边界与不确定性**：① 递归树响应被截断 ⇒ 本棒**0 声称穷尽全树**；② `transformer-4.57.3/` 为 vendored 第三方 transformers 整树（递归树中段可见），本棒**0 核**其中是否含 Merkle 字符串（第三方 vendored 代码与 IMMACULATE 自身实现应区分，但本棒未核）；③ GitHub code search 401 属**通道限制**（匿名鉴权），非「不存在」的证据；④ 仓库 owner 改名事实已如实登记（`guo-yanpei` → `paulguoyanpei`）。

---

## §4 O-R5 · zkML 工程化进展

### 题干（逐字，源件 `98085df7811a` L130–L133）

> **B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
> - EZKL 2024-2026 的工程化进展(是否有大模型支持 / 是否有工业级 case)
> - Modulus Labs 是否在 2024-2025 完成新一轮融资 / 重要技术里程碑
> - "GKR-based zkML" 是否仍是 2025 主流(本作者无法在线核验,可能已有更高效方案)

### 4.1 子项①：EZKL 2024–2026 工程化进展

| 核验动作 | 实际执行的检索 |
|---|---|
| 仓库路径纠正 | `https://api.github.com/repos/ezkl/ezkl` ⇒ **404 Not Found**（该 `ezkl` 用户名下是 `sniffles`/`capit`/`ziptastic`/`go-amazon-mws-api` 等无关仓库）；`https://api.github.com/repos/zksecurity/ezkl` ⇒ **404**；经 `search/repositories?q=ezkl+in:name&sort=stars` ⇒ 正确主体为 **`zkonduit/ezkl`**（`full_name=zkonduit/ezkl`，`language=Rust`，`stargazers_count=1223`，`forks_count=212`，`topics=[ai, cryptography, zero-knowledge, zkml]`，`homepage=https://docs.ezkl.xyz/`，`created_at=2022-07-05`，`pushed_at=2026-02-20`）⇒ **题面「EZKL GitHub 公开」成立，但主体 org 为 `zkonduit`（0 不是 `ezkl`）** |
| Release 序列（工程化活跃度） | `https://api.github.com/repos/zkonduit/ezkl/releases?per_page=6` ⇒ 返回 6 条，按发布时序倒序：v22.2.1（2025-07-30）、v22.2.2（2025-10-26）、v22.2.4（2025-10-07）、v22.3.0（2025-10-08）、v23.0.2（2025-10-26）、v23.0.3（2025-10-26）、v23.0.5（2026-02-20，latest，含 linux-gnu／linux-aarch64／linux-musl／linux-gpu／windows-msvc 五平台产物）⇒ **2024–2026 期间持续发版，最近一次 2026-02-20** |
| 第三方以 ezkl 为「生产框架」评测 | arXiv `all:"EZKL"` ⇒ totalResults 2：① `Sound Debloating of Redundant Checks in Zero-Knowledge Machine-Learning Circuits`（arXiv 2609.10149，2026-09-09）摘要自述「circuits … generated by **two production frameworks (ezkl and zkml)**」，评测覆盖 MLP／CNN／RNN／transformer，最大 25.3M constraints；② `Bionetta: Efficient Client-Side Zero-Knowledge Machine Learning Proving`（arXiv 2510.06784v2，2025-10-08／v2 2025-12-08）摘要自述与「EZKL, Lagrange's deep-prove, or zkml」对比 |
| 工业级 case | **本棒 0 找到** —— arXiv 两篇均为学术评测，0 提及工业客户/生产部署；搜索引擎通道不可用，`docs.ezkl.xyz` 与公司站 0 取得 |

- **来源（URL ＋ 访问日期）**：
  - `https://api.github.com/search/repositories?q=ezkl+in:name&sort=stars&per_page=5`（2026-10-01）
  - `https://api.github.com/repos/zkonduit/ezkl/releases?per_page=6`（2026-10-01）
  - `http://export.arxiv.org/api/query?search_query=all:%22EZKL%22&max_results=10&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=2；含 2609.10149、2510.06784v2）
  - `https://api.github.com/repos/ezkl/ezkl/releases?per_page=8`（2026-10-01，**404**）；`https://api.github.com/repos/zksecurity/ezkl`（2026-10-01，**404**）
- **结果**：**部分证实 / 部分不可判**（按题面两小问拆开）
  - 「2024–2026 的工程化进展」＝ **证实**（有来源：GitHub release 序列，2025-07 至 2026-02 持续发版；且 2025-10 与 2026-09 两篇第三方论文把 ezkl 称为 production framework 之一）
  - 「是否有大模型支持」＝ **不可判**（release 序列 0 提及模型规模；两篇第三方论文的评测对象为 MLP／CNN／RNN／transformer 架构，**0 出现具体参数规模标注**）⇒ 0 找到可判来源
  - 「是否有工业级 case」＝ **不可判**（已查：arXiv EZKL 全部 2 命中、GitHub releases 全部 6 条、搜索引擎不可用）⇒ 结论值 **null**
- **时效性**：release 时点（latest 2026-02-20）与两篇第三方论文（2025-10、2026-09）**均晚于源件知识截止 2026-01**（部分）⇒ 属「截止后更新」面，结论以 2026-10-01 快照为准。
- **边界与不确定性**：① **主体名修正**是本条最实质的发现：EZKL 的 GitHub org 是 `zkonduit`，而 `github.com/ezkl` 是一个**同名的无关个人用户**（其下 `sniffles` 是 2018 年停更的 Ruby 嗅探器、`capit` 是 Ruby 截图库）——若后续棒按 `ezkl/ezkl` 取源会 404；② GitHub `stargazers_count` 与 `forks_count` **不构成工业级采用的证据**，本棒未将其当作 case 证据；③ 「工业级」的判定标准（生产 SLA？付费客户？公开 case study？）**未在题面中定义**，本棒 0 代 PI 定义。

### 4.2 子项②：Modulus Labs 2024–2025 融资 / 技术里程碑

| 核验动作 | 实际执行的检索 |
|---|---|
| arXiv：`Modulus Labs` | `all:"Modulus Labs"` ⇒ **totalResults = 0** |
| arXiv：`Modulus` + `zero knowledge` | `all:"Modulus" AND all:"zero knowledge"` ⇒ totalResults 5，逐条判读**全部为同名词噪声**（如 `CRT-Decomposed Σ-Protocols for CSIDH` 中的数学「模数」用法、`I-(OT)^2` 中的 RSA 模数用法），**0 命中 Modulus Labs 公司** |
| GitHub 组织 | `https://api.github.com/orgs/ModulusLabs` ⇒ **404 Not Found** |
| 搜索引擎 / 公司站 | `lite.duckduckgo.com`、`html.duckduckgo.com` ⇒ 网络不可达；`moduluslabs` 官网 0 取得 |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22Modulus%20Labs%22&max_results=10&sortBy=submittedDate&sortOrder=descending`（2026-10-01，**totalResults=0**）
  - `http://export.arxiv.org/api/query?search_query=all:%22Modulus%22%20AND%20all:%22zero%20knowledge%22&max_results=10&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=5，全为同名词噪声）
  - `https://api.github.com/orgs/ModulusLabs`（2026-10-01，**404**）
- **结果**：**不可判**
  - 已查渠道清单：① arXiv 精确短语「Modulus Labs」＝0 命中；② arXiv「Modulus + zero knowledge」＝5 命中，全为同名词数学用法；③ GitHub org API＝404；④ 搜索引擎＝网络不可达；⑤ 公司官网＝0 取得。
  - 结论值：**null**。
- **时效性**：完全落在源件「截止后更新」面；融资信息属**商业新闻面**，本棒 0 取得该面任何来源。
- **边界与不确定性**：① arXiv 0 收录公司融资新闻，**该 0 命中不构成任何关于其融资/无融资的推断**；② 源件 A 类栏（未列入本棒范围）曾称 Modulus Labs「与 Anthropic 合作过『证明 LLaMA-7B 推理』项目」——本棒**0 核**该 A 类陈述（且据本棒 arXiv 检索面，0 命中 Modulus Labs 名下的 LLM 推理证明论文，**但本棒 0 据此判定该 A 类陈述为伪**）。

### 4.3 子项③：「GKR-based zkML」是否仍是 2025 主流

| 核验动作 | 实际执行的检索 |
|---|---|
| arXiv：`GKR` + `zkML` | `all:"GKR" AND all:"zkML"` ⇒ **totalResults = 0** |
| arXiv：`GKR` + `zero knowledge` + `neural network` | `all:"GKR" AND all:"zero knowledge" AND all:"neural network"` ⇒ **totalResults = 0** |
| arXiv：`GKR protocol` | `all:"GKR protocol"` ⇒ totalResults 2：① `Agree on the Model, Verify the Inference: GKR Protocols for HND-Based Transformer Inference`（arXiv 2607.21162，**2026-07-23**，24 页，作者 Xiaolong Liang／Juanjuan Li／Rui Qin／Yisheng Lv）——摘要自述「verifying the polynomial backbone of Homomorphic–Nonhomomorphic Decomposition Transformers」「The retained verifier checks the GKR transcript」；② `A Survey of Interactive Verifiable Computing: Utilizing Low-degree Polynomials`（arXiv 2501.05500，**2025-01-09**，29 页，作者 Angold Wang）——摘要自述 GKR protocol 是「a foundation for contemporary verifiable computing models」 |
| 「GKR-based zkML 是否主流」的正面证据搜索 | arXiv `all:"zkML" AND all:"LLM"`（max_results=15，desc）⇒ totalResults 3，返回：**0 条**以 GKR 为主力方案的论文；实际返回的是 ① `Repeated-Game Security for Restaking-Based Verifiable Inference`（2608.09055，2026-08-10）摘要自述其动机是「verifiable LLM inference **without the high proving cost of zkML**」；② `NanoZK: Privacy-Preserving Verifiable Inference for Large Language Models via Layerwise Zero-Knowledge Proofs`（2603.18046v2，2026-07-18，ICICS 2026 / ICLR 2026 VeriFAI Workshop）——摘要自述其机制为「decomposes transformer inference into independently provable layers **linked by a SHA-256 commitment chain**」，子电路证明 3.5–3.7 KB、总计约 83 KB，对比「prior ZKML's monolithic 101–126 KB proofs」；③ `Optimistic TEE-Rollups`（2512.20176，2025-12-23）——摘要自述用 NVIDIA H100 CC TEE ＋ 随机 ZK spot-checks |

- **来源（URL ＋ 访问日期）**：
  - `http://export.arxiv.org/api/query?search_query=all:%22GKR%22%20AND%20all:%22zkML%22&max_results=15&sortBy=submittedDate&sortOrder=descending`（2026-10-01，**totalResults=0**）
  - `http://export.arxiv.org/api/query?search_query=all:%22GKR%22%20AND%20all:%22zero%20knowledge%22%20AND%20all:%22neural%20network%22&max_results=15&sortBy=submittedDate&sortOrder=descending`（2026-10-01，**totalResults=0**）
  - `http://export.arxiv.org/api/query?search_query=all:%22GKR%20protocol%22&max_results=15&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=2；含 2607.21162、2501.05500）
  - `http://export.arxiv.org/api/query?search_query=all:%22zkML%22%20AND%20all:%22LLM%22&max_results=15&sortBy=submittedDate&sortOrder=descending`（2026-10-01，totalResults=3；含 2608.09055、2603.18046v2、2512.20176）
- **结果**：**不可判**
  - 已查渠道清单：① arXiv「GKR+zkML」＝0 命中；② arXiv「GKR+zero knowledge+neural network」＝0 命中；③ arXiv「GKR protocol」＝2 命中（1 篇 2026-07 的 GKR-HND Transformer 验证协议 ＋ 1 篇 2025-01 的可验证计算综述）；④ arXiv「zkML+LLM」＝3 命中，**0 条**以 GKR 为主力。
  - 结论值：**null**。
- **时效性**：落在源件「截止后更新」面；所引 2607.21162（2026-07）与 2603.18046v2（2026-07）**均晚于源件知识截止 2026-01**，本棒结论以 2026-10-01 快照为准。
- **边界与不确定性**：① **「主流」是程度/生态定性，本棒 0 找到任何可支撑或否证该定性的量化来源**（如综述中的方案占比、方法族计数、基准采用率）⇒ 故判不可判而非证伪；② 可陈述的事实是：GKR protocol 作为可验证计算的基础协议在 2025–2026 仍有综述与新协议工作（2501.05500、2607.21162 有来源）；而 2025–2026 的 LLM 可验证推理方向中，arXiv 命中的三条（2608.09055／2603.18046v2／2512.20176）**均不以 GKR 命名**——**「0 命中 GKR」不等于「GKR 已被取代」**，本棒**0 作出该推断**；③ 题面括注「可能已有更高效方案」：NanoZK 摘要自述其相对「prior ZKML」的证明体积与并行度优势（83 KB vs 101–126 KB、子电路 3.5–3.7 KB），但**0 提及 GKR**，故**0 用它作「GKR 被更高效方案取代」的证据**。

---

## §5 未核项清单（本棒 0 取得可判来源者，如实登记）

| # | 所属 | 未核项（题面字面） | 状态 | 0 取得的原因（已实测） |
|---:|---|---|---|---|
| 1 | O-R2① | TexTra 是否真实存在并被引用 | 不可判 | arXiv 精确短语 0 命中；GitHub 仓库名 0 同名项；搜索引擎通道不可达 |
| 2 | O-R2① | DNA 是否真实存在并被引用 | 不可判 | 源件只给两字母缩写；arXiv「model fingerprint」61 命中逐读 0 命中名为 DNA 的系统（存在近名 modelDNA，本棒 0 代 PI 认定同一）；搜索引擎不可达 |
| 3 | O-R2① | MathNAS 的**领域归属** | 已证「论文存在」·**未证**「模型指纹 SOTA 系统」 | arXiv 2311.04943 摘要 0 出现 fingerprint ⇒ 存在性证实、领域定性未证实 |
| 4 | O-R2② | DeepMind / Google 2022–2023 公开「LLM 指纹」工作的**具体论文 ID** | 证伪（该定位） | arXiv 2022–2023 窗 0 命中 LLM 指纹论文；官方 publication 站 0 取得 |
| 5 | O-R3① | SGX 完全退市时间表 | 不可判 | Intel newsroom 403 Access Denied；搜索引擎 4 次网络失败；arXiv「SGX+deprecat」0 命中 |
| 6 | O-R3② | H100 CC 2025–2026 客户实际采用率 | 不可判 | 搜索引擎不可达；arXiv「confidential computing+adoption」26 命中 0 采用率数值；采用率口径本身未定义 |
| 7 | O-R3③ | SEV-SNP 侧信道漏洞的**「严重」程度定性** | 存在性**证实**·程度**未判** | arXiv 仅能支撑「存在公开披露的侧信道攻击」，0 官方 CVE/PSIRT 公告，0 程度判据 |
| 8 | O-R3③ | 2024 年（全年）SEV-SNP 漏洞 | **arXiv 面 0 命中** | 该面最早 SEV-SNP 条目为 2025-06-18 ⇒ 2024 年无 arXiv 侧记录 |
| 9 | O-R4① | Anthropic / OpenAI 是否公开「用 Merkle 树记录推理过程」 | 不可判 | 两方官方站 0 取得；搜索引擎不可达 |
| 10 | O-R4② | IMMACULATE 的 **NUS 机构归属** | 不可判 | arXiv 响应无 affiliation 字段、摘要 0 写机构 |
| 11 | O-R4③ | IMMACULATE 仓库是否含 **hash chain** 实现 | 不可判 | `artifact_hash.py` 本身**非** hash chain（已证），但 GitHub code search 401 ⇒ 0 全仓字面 grep；递归树响应被截断 |
| 12 | O-R5① | EZKL 是否有**大模型支持** | 不可判 | release 序列 0 提模型规模；第三方论文 0 标参数规模 |
| 13 | O-R5① | EZKL 是否有**工业级 case** | 不可判 | arXiv EZKL 全部 2 命中、GitHub releases 全部 6 条 0 工业客户；搜索引擎不可达 |
| 14 | O-R5② | Modulus Labs 2024–2025 融资 / 里程碑 | 不可判 | arXiv「Modulus Labs」0 命中；GitHub org 404；搜索引擎不可达；官网 0 取得 |
| 15 | O-R5③ | 「GKR-based zkML 是否 2025 主流」 | 不可判 | arXiv「GKR+zkML」0 命中、「GKR protocol」仅 2 命中（1 综述 ＋ 1 2026 新协议）、「zkML+LLM」3 命中 0 条以 GKR 为主力；「主流」0 量化判据 |

**通道级未核项**（影响面覆盖上表 #1／#2／#5／#6／#9／#13／#14）：
- 通用搜索引擎（`lite.duckduckgo.com`、`html.duckduckgo.com`）：**4 次调用全部 `web_fetch network request failed`**
- 厂商官方站（`intel.com` newsroom）：**`Access Denied`（Akamai）**
- GitHub code search（匿名）：**`401 Requires authentication`**
- ⇒ 凡结论依赖上述三面的子项，本棒一律登记为**不可判（null）**，**0 用「未找到」反推「不存在」**。

---

## §6 0 代裁声明

1. **0 判定既有结论**：本棒 0 判定、0 修改、0 回写 `98085df7811a`（源件）、r4 台账件、残余清册件、确认回执册中的任何既有结论。§3.2 对 IMMACULATE 结构的「证伪」仅指**本棒所读仓库文件面的字面核验结果**，不构成对源件 A/B 类任何既有判断的改判。
2. **0 采信未经核实的断言**：源件四项的自述性断言（TexTra/DNA/MathNAS 三名、「Sev-SNP 历史上曾被多次攻破」、Modulus Labs 与 Anthropic 合作证明 LLaMA-7B 推理、源件 L90／L92 的 A 类陈述等）**本棒一律 0 采信**；凡无来源者，本件只如实登记为「未核」或「不可判」。
3. **0 编造**：本件所列全部 arXiv ID、论文标题、作者名、GitHub 仓库主体名、release tag、URL，均为 2026-10-01 经 arXiv API / GitHub API / raw.githubusercontent 实际访问响应中的字面。**0 出现任何未经实际访问的来源、URL、文献号、人名**；0 出现凭记忆补写的条目。
4. **0 引入比喻性术语**（沿 7 铁律术语红线）：本件所用外部技术名词（Merkle tree、hash chain、verifiable computation、side channel、SEV-SNP、fp16/fp32、digest 等）**均为来源字面用词并附出处**；本棒自身 0 造任何比喻性表述。
5. **0 越界取 O-R6**：O-R6 同在题面 §5，但 PI 本次授权只覆盖 O-R2–R5 ⇒ 本件 0 记录、0 核验、0 推断 O-R6 的任何内容。
6. **0 定义未定义口径**：题面未定义的「采用率」「工业级 case」「严重」「主流」四项口径，本棒 0 代 PI 定义，故相关子项一律登记为不可判，而非按某一读法给结论。
7. **时效性总则**：本件全部结论的检索快照时点为 **2026-10-01**。源件四项均自标「知识截止 2026-01 后可能已更新」，本件所引 2026 年的来源（如 arXiv 2602.22700、2603.18046v2、2604.25634、2605.12990、2607.21162、2609.10149）**均为源件知识截止之后的新增事实**。⇒ 知识截止后信息以实时检索为准，PI 复用本件结论时须以新的检索时点复核。
8. **0 声称穷尽**：本件对 IMMACULATE 仓库的覆盖为「README 全文 ＋ `inference/` 顶层 ＋ `inference/csrc/` 全部 ＋ `artifact_hash.py` 全文」四层，**0 声称覆盖全仓**（递归树响应被截断、code search 401）；对 `vllm/`、`docs/`、`tools/`、`benchmarks/`、`tests/` 子树 0 做 Merkle/hash-chain 字面检索。

---

## §7 核验动作台账（本棒实际访问的外部来源清单）

> 全部访问日期：**2026-10-01**。以下 URL 均为本棒**实际发出并取得响应**者（失败者亦如实列出）。

| # | URL | 响应 | 支撑子项 |
|---:|---|---|---|
| 1 | `http://export.arxiv.org/api/query?search_query=all:%22model%20fingerprint%22&max_results=25&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 61） | O-R2①③、O-R2② |
| 2 | `http://export.arxiv.org/api/query?search_query=all:%22TexTra%22&max_results=5` | 200（**totalResults 0**） | O-R2① |
| 3 | `http://export.arxiv.org/api/query?search_query=all:%22MathNAS%22&max_results=5` | 200（totalResults 1） | O-R2① |
| 4 | `http://export.arxiv.org/api/query?search_query=all:%22model%20fingerprint%22%20AND%20submittedDate:%5B202201010000%20TO%202312312359%5D&max_results=20&sortBy=relevance` | 200（totalResults 54） | O-R2①③、O-R2② |
| 5 | `http://export.arxiv.org/api/query?search_query=all:%22fingerprint%22%20AND%20all:%22LLM%22%20AND%20submittedDate:%5B202201010000%20TO%202312312359%5D&max_results=12&sortBy=relevance` | 200（totalResults 245） | O-R2②③ |
| 6 | `http://export.arxiv.org/api/query?search_query=ti:%22IMMACULATE%22&max_results=8` | 200（totalResults 23，全为同名数学论文） | O-R4① |
| 7 | `http://export.arxiv.org/api/query?search_query=all:%22IMMACULATE%22%20AND%20all:%22inference%22&max_results=10&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 2） | O-R4①② |
| 8 | `http://export.arxiv.org/api/query?search_query=all:%22SEV-SNP%22&max_results=15&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 31） | O-R3③、O-R4① |
| 9 | `http://export.arxiv.org/api/query?search_query=all:%22SGX%22%20AND%20all:%22deprecat%22&max_results=10` | 200（**totalResults 0**） | O-R3① |
| 10 | `http://export.arxiv.org/api/query?search_query=all:%22Intel%20SGX%22%20AND%20submittedDate:%5B202501010000%20TO%202612312359%5D&max_results=12&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 34） | O-R3① |
| 11 | `http://export.arxiv.org/api/query?search_query=all:%22confidential%20computing%22%20AND%20all:%22adoption%22&max_results=12&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 26） | O-R3② |
| 12 | `http://export.arxiv.org/api/query?search_query=all:%22GKR%22%20AND%20all:%22zkML%22&max_results=15&sortBy=submittedDate&sortOrder=descending` | 200（**totalResults 0**） | O-R5③ |
| 13 | `http://export.arxiv.org/api/query?search_query=all:%22GKR%22%20AND%20all:%22zero%20knowledge%22%20AND%20all:%22neural%20network%22&max_results=15&sortBy=submittedDate&sortOrder=descending` | 200（**totalResults 0**） | O-R5③ |
| 14 | `http://export.arxiv.org/api/query?search_query=all:%22GKR%20protocol%22&max_results=15&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 2） | O-R5③ |
| 15 | `http://export.arxiv.org/api/query?search_query=all:%22zkML%22%20AND%20all:%22LLM%22&max_results=15&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 3） | O-R5③ |
| 16 | `http://export.arxiv.org/api/query?search_query=all:%22EZKL%22&max_results=10&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 2） | O-R5① |
| 17 | `http://export.arxiv.org/api/query?search_query=all:%22Modulus%20Labs%22&max_results=10&sortBy=submittedDate&sortOrder=descending` | 200（**totalResults 0**） | O-R5② |
| 18 | `http://export.arxiv.org/api/query?search_query=all:%22Modulus%22%20AND%20all:%22zero%20knowledge%22&max_results=10&sortBy=submittedDate&sortOrder=descending` | 200（totalResults 5，全为同名词噪声） | O-R5② |
| 19 | `https://api.github.com/repos/guo-yanpei/Immaculate` | 200（`full_name=paulguoyanpei/Immaculate`） | O-R4②③ |
| 20 | `https://api.github.com/repos/paulguoyanpei/Immaculate/git/trees/main?recursive=1` | 200（**响应过大被截断**） | O-R4③ |
| 21 | `https://api.github.com/repos/paulguoyanpei/Immaculate/contents/inference` | 200（33 条） | O-R4③ |
| 22 | `https://api.github.com/repos/paulguoyanpei/Immaculate/contents/inference/csrc` | 200（33 条） | O-R4③ |
| 23 | `https://api.github.com/repos/paulguoyanpei/Immaculate/readme` | 200（base64，实读解码） | O-R4②③ |
| 24 | `https://api.github.com/search/code?q=merkle+repo:paulguoyanpei/Immaculate` | **401 Requires authentication** | O-R4③（通道限制） |
| 25 | `https://raw.githubusercontent.com/paulguoyanpei/Immaculate/main/inference/artifact_hash.py` | 200（全文实读） | O-R4②③ |
| 26 | `https://api.github.com/search/repositories?q=ezkl+in:name&sort=stars&per_page=5` | 200（`zkonduit/ezkl`） | O-R5① |
| 27 | `https://api.github.com/repos/ezkl/ezkl/releases?per_page=8` | **404 Not Found** | O-R5①（路径纠正） |
| 28 | `https://api.github.com/repos/zksecurity/ezkl` | **404 Not Found** | O-R5①（路径纠正） |
| 29 | `https://api.github.com/repos/zkonduit/ezkl/releases?per_page=6` | 200（latest v23.0.5，2026-02-20） | O-R5① |
| 30 | `https://api.github.com/search/repositories?q=TexTra&per_page=6` | 200（total_count 2410，0 同名） | O-R2① |
| 31 | `https://api.github.com/orgs/ModulusLabs` | **404 Not Found** | O-R5② |
| 32 | `https://www.intel.com/content/www/us/en/newsroom/intel-latest-update.html` | **Access Denied（Akamai）** | O-R3①（通道限制） |
| 33 | `https://lite.duckduckgo.com/lite/?q=Intel+SGX+end+of+life+deprecation+official+notice` | **network request failed** | 通道限制 |
| 34 | `https://html.duckduckgo.com/html/?q=Modulus+Labs+funding+round+zero+knowledge+machine+learning` | **network request failed** | 通道限制 |
| 35 | `https://html.duckduckgo.com/html/?q=Intel+SGX+end+of+life+Sapphire+Rapids+deprecation+2023+2024` | **network request failed** | 通道限制 |
| 36 | `https://html.duckduckgo.com/html/?q=NVIDIA+H100+confidential+computing+adoption+rate+2025` | **network request failed** | 通道限制 |

**通道可用性小结**（供后续棒直接取用，0 重复试错）：
- ✅ arXiv API（`export.arxiv.org/api/query`）——**全程稳定**，可作文献面主通道；支持 `all:`／`ti:`／`submittedDate:[TO]`／`sortBy`／`max_results`。
- ✅ GitHub REST API——repos／contents／git-trees／readme／search-repositories 可用；**search-code 需鉴权（401）**。
- ✅ raw.githubusercontent——文件直取可用。
- ⛔ 通用搜索引擎（duckduckgo html／lite）——**网络不可达**。
- ⛔ intel.com——**Akamai 拒绝**。
- ⚠️ arXiv API 响应**体积大**：`all:"model fingerprint"` 类宽查询会触发截断，`git/trees?recursive=1` 对大仓库必然截断 ⇒ 应优先用精确短语 ＋ 小 `max_results`，并优先用 `contents` 分层取目录而非递归树。

---

**本棒产出 1 件**（`results/_o_r2_r5_external_verification_2026_10_01.md`），0 改既有件。
