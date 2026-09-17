# FTFB 外审二轮（R2）综合元审报告 —— 《Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews》

**评审轮次**：External Review Round 2（双盲）
**评审对象**：`ftfb_external_review_v2_20260917.tar.gz`（v2 外审包，6 件）
**评审日期**：2026-09-17
**组织方**：Trae code（编排/编辑角色，兼职团队制）
**评审人**：RB-1、RB-2（两名相互独立的兼职评审者，双盲代号；全程离线，互不可见，未见任何工作侧文件）

---

## §0 执行摘要

**一致裁定：Minor Revision（两票一致），Overall 均 7/10。**

内容层问题全部为有界、可修的文本项，无需新实验。但本轮**发现并经编排方机械核实一处交付级排版阻断缺陷**：tex 源的 `\end{abstract}` 误置于 L408，导致**摘要段 + 全部正文（§1–§9）+ AI 披露段均被排入 abstract 环境**，仅 References 在环境外——交付 PDF 的 20 页实为"摘要格式包裹全文"的渲染。该缺陷被双方评审独立发现、编排方字节级确认，且**现有全部编译质量门（Z1–Z4/S1–S6，含金标准复现）均为文本层/日志层检查，结构性无法捕获此类视觉语义缺陷**（确定性复现 ≠ 正确性）。修复属一行移动 + 重编译 + 补一道视觉门。

| 维度 | RB-1（方法论/定量） | RB-2（科学史哲/科幻研究） |
|---|---|---|
| B Significance & originality | 4/5 | 4/5 |
| C Soundness | 4/5 | 3/5 |
| D Literature coverage | 4/5 | 4/5 |
| E Clarity & presentation | 4/5 | 4/5 |
| F Verifiability & reproducibility | 3/5 | 4/5 |
| G Research integrity | 5/5 | 5/5 |
| **H Overall** | **7/10** | **7/10** |
| **I 建议** | **Minor Revision** | **Minor Revision** |

C/F 的 4 vs 3 分歧为**视角互补**（RB-1 从第三方可复算性压 F/C，RB-2 从史学论证密度压 C），非事实冲突；按预注册冲突规则（建议类别一致 → 直接合并，无需 RB-3 仲裁）。

---

## §1 评审系统与双盲机制（对应委托要求 1/2/4/5）

| 要素 | 实施 |
|---|---|
| **技能与专家配置** | 编排方：安全解包/路径穿越检查/监管链/机械核验（Python + hashlib，0 LLM）；评审方：两名兼职评审代理，分别携带「定量方法论/AI 评估/可复现性」与「科学史与科学哲学/科幻研究」专家视角，均按 `tashan-research-skills:academic-writing` 同行评审规范执行 |
| **双盲** | 作者侧：包内论文三件经编排方独立 token 扫描（12 个身份 token × md/tex 双文件 = 0 命中；PDF /Author 空；GLM 仅 1 次 = 已声明的 AI 披露句）。评审侧：评审者只见论文与评审表；工作侧文件（简报/编译验证/manifest）明令禁读且未入包；全程禁用 WebSearch/WebFetch（禁止去匿名化）；评审者互不可见、隔离目录、独立派发 |
| **标准化** | 同一份评审表（字节一致，SHA-12 `34211db5b623`）：A–O 十五节、B–H 锚定量表、评分锚点、强制行号证据锚定、缺节即无效 |
| **独立评估** | ≥2 名评审者：实际 2 名，并行独立完成，均提交完整 A–O |
| **冲突解决** | 预注册规则：同类别→合并；相邻类别→元审判定；非相邻→RB-3 仲裁。本轮触发"同类别→合并"分支 |
| **保密与学术诚信** | 评审文件以代号落盘；报告披露评审者为 AI 兼职代理（沿论文自身 AI 披露规范的对称诚实）；原包与工作侧文件零改动 |

**监管链**：tar.gz（417,674 B）→ 解压 6 件 → 包内 `SHA256_MANIFEST.txt` 校验 **5/5 MATCH** → 评审表/评审件 SHA-256 全记录（见 §8）。

---

## §2 编排方独立机械核验（不信任任何自报声明）

| 核验项 | 结果 | 与工作侧声明的关系 |
|---|---|---|
| 身份 token 扫描（deposon/keep-the-books/zhipu/智谱/清言/ChatGLM/bigmodel/Coze/扣子/Qihao/Yuan，md+tex） | **0/12 命中** | 与简报 D1 一致 ✅ |
| PDF `/Author` 元数据 | 空 | 一致 ✅ |
| tex `\author{}`/`\date{}` | 均空 | 一致 ✅ |
| GLM 出现次数（md/tex） | 恰 1（AI 披露句） | 一致 ✅ |
| 冻结数字（0.8569 / 2.220446049250313 / 6,760 / 0.899×2 / 0.97 / 0.452 / 0.739 / 4/3 / 338×3 / kT·ln2×2） | **逐项计数吻合** | 与简报"红线三代存活"一致 ✅ |
| 五锚（GT_FORMALIZATION/run_v21/run_v22/SPEC_GT2B/SPEC_GT8C） | md/tex/编译验证三方均为各恰 1，第 5 锚实为 `6b09de9911c0` | 一致 ✅（注：编排方首轮目视转写为 5b09 产生 0 命中假警，机械 grep 复核后纠正——取证过程如实记录） |
| 引用池 R01–R52 | md 0 缺失；`[IDENTIFIER-PENDING]` 恰 2（R13/R14） | 一致 ✅ |
| md CJK 字符 | 0 | 一致 ✅ |
| **tex CJK 字符** | **110（5 行排版工作注释，L42/47/56-58，无任何身份信息）** | **简报 D1"tex CJK 0"字面不实** ⚠（F-1，工作侧记录瑕疵，不构成泄密、不阻断） |
| **abstract 环境位置** | `\begin{abstract}` L69 → `\end{abstract}` **L408**，跨度 ~340 行 | **工作侧全部质量门未覆盖** 🔴（详见 §5） |

评审引用锚点抽查：RB-1/RB-2 所引 25 个 md 行号**逐一经机械核对全部真实**（两份评审非幻觉，证据锚定可靠）。

---

## §3 双评审收敛发现（合并后的共识）

### 共识优点（双方独立指出，各附代表锚点）

1. **D 四档 disposition dictionary 一次声明、全文逐行执行**（md L36；§2–§5 及 §7 各计分行吻合 L81/109/133/167/245）——评分装置可由第三方逐行复核。
2. **两层证据严格分离，supply-level discipline 全程成立**：史学层从不借 §7 预注册层的裁决权威（L170/273/400），对己不利的年代学如实自降（L81/132）。
3. **负面结果全量披露 + 用论文自己的检查给自身打分**（三命题预注册被证伪 L231；capability channel 读零 L239；kill lines 预录 L294/302-304；selection effect 自认 L298/400）——诚信实践完整闭环（双方 G=5/5 的依据）。

### 共识弱点（双盲下一票方法论、一票史学，同一病灶两种透镜）

1. **§7 实例在盲审期第三方可验证性为零**（无公开 repo/全量摘要/时间戳，M4 走保密通道，md L229/231/245）：RB-1 压 F=3，RB-2 提"录用前编辑侧核验"。编排方注：该限制系论文**自行声明**（§7.1），属评审过程限制而非隐瞒；处置见 §6 C-5。
2. **三检查对四通道的区分度不足**：T/R 在 §9.1 全行通过系 selection 所致（论文自认 L298/400），F-C1（L25）从未被任何 worked negative case 触发；主表 I/II 仅差 D 标签、III/IV 仅差 T scoping（L285–288）——"separate" 的分离度目前是薄的。RB-1 从"通道级证伪被钝化"切入，RB-2 从"无负例展示判别力"切入，同源。
3. **abstract 环境错位（排版阻断，双方独立发现，编排方确认）**：见 §5。

---

## §4 各自独有发现（保留入修订清单）

**RB-1**：
- M4 行左列（diegetic prototype 的工程承诺实践，L189）超出 §6.1 声明的"exactly these four demands and nothing else"（L176）范围——映射 kill condition（L217）的承重弱点。

**RB-2**：
- Channel II translatability 判据内部张力：L100"verify a limiting case" vs "re-derivable from the reconstruction alone"两支不兼容，牵连 Brown–Norton 不变性主张（L109）与 §8.3 判据（L267）。
- §6.1 对 [R36]/[R37] 四项 genre 判据仅作无引号转述（L176）且 R37 无访问日期——mapping 忠实性前提暂不可复核。
- Channel I"long period referred to nothing physical"（L62 附近）忽视 Riemann 1854/Helmholtz 1870/Clifford 的物理所指猜测，史学口径偏紧。

---

## §5 经核实的交付级缺陷（阻断项 T-1）

**缺陷**：`fiction_that_feeds_back.tex` L69 `\begin{abstract}` ↔ L408 `\end{abstract}`。abstract 段落（L72）之后，`\section{Introduction}`（L74）直至 §9 AI 披露段（L406）全部位于 abstract 环境内；仅 `\section*{References}`（L410）在外。

**后果**：交付 PDF（20 页）以 abstract 环境（类 quotation 窄栏缩进）渲染全文正文；v1→v2 的 17→20 页增量很可能主要来自该缩进而非 R46–R52 补源。

**为何全部质量门漏网**：Z1–Z4/S1–S6 检查的是错误/文本层/收敛性/锚计数；金标准复现证明的是**同源确定性**（同一份 tex 必然复现同一缺陷）。视觉语义层无任何门覆盖。

**修复**（一行移动）：将 `\end{abstract}` 移至 L72 abstract 段落之后、L74 `\section{Introduction}` 之前；pdflatex ×3 重编译；**新增视觉门**：abstract 块必须止于第 1 页（如"第 2 页起不得处于 abstract 环境排版"的探针），否则此类缺陷在 v3 仍会带病放行。

**连带核查（工作侧）**：v1 PDF（17 页）是否同样存在此环境错位——若是，则该缺陷自 v1 起被两轮"全零绿"掩盖；若否，则系 v2 重排（F1 标题消费/B2 修复）期间引入，可精确定位回归点。

---

## §6 修订清单（优先级排序，供作者侧执行）

| # | 级别 | 事项 | 锚点 |
|---|---|---|---|
| T-1 | 🔴 阻断（排版） | 移动 `\end{abstract}` 至摘要段后；重编译；补"abstract 止于第 1 页"视觉门 | tex L69/72/74/408 |
| C-1 | 🟡 内容 | §6.1 判据范围句与 M4 行左列二选一对齐（放宽"exactly these four"或收窄 M4 左列） | md L176/189/217 |
| C-2 | 🟡 内容 | 统一 Channel II translatability 判据口径，并同步 L109/L267 | md L100/109/267 |
| C-3 | 🟡 内容 | [R36]/[R37] genre 判据加引号直引 + 补 R37 访问日期 | md L176 |
| C-4 | 🟡 内容 | Channel I"无物理所指"表述补 Riemann 1854/Helmholtz 1870/Clifford 限定 | md L62 |
| C-5 | 🟡 编辑侧 | 录用前经保密通道完成 §7 frozen record 编辑侧核验（评审包未随附工件，本轮 §7 评的是内部一致性+已声明限制） | md L229/245 |
| W-1 | ⚪ 工作侧 | 简报"tex CJK 0"表述修正（实为 110 字符/5 行排版注释，无身份信息） | tex L42/47/56-58 |
| W-2 | ⚪ 工作侧 | 回溯 v1 PDF 是否共享 abstract 错位（版本链取证） | — |

R13/R14 identifier-pending 与 novelty 二轮检索：论文已自行排期（md L400/412），双方评审均不将其计为缺陷。

---

## §7 学术诚信与保密记录

- 双向匿名维持：作者侧信息对评审零暴露（§2 token 扫描 + 禁读清单 + 离线评审）；评审身份以代号呈现，作者侧不可见。
- 评审者披露：RB-1/RB-2 为 AI 兼职评审代理（multi-agent 兼职评审团队制），以标准化表单+强制证据锚执行；本报告按论文自身 AI 披露规范的对称诚实原则如实声明。
- 编排验证层 0 LLM（纯 hashlib/regex 机械核验）；原包、工作侧文件、被审论文零改动。
- 评审件只读原稿，未执行 M4、未外联、未尝试去匿名化（两份评审 O 节声明齐备）。

---

## §8 交付物与监管链

| 件 | 路径 | 指纹 |
|---|---|---|
| 本报告 | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/META_REVIEW_REPORT_2026_09_17.md` | 本文件 |
| RB-1 完整评审（A–O） | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/REVIEW_RB1.md` | sha256 `3594378e7d1d…8210907`（22,982 B） |
| RB-2 完整评审（A–O） | `docs/FTFB_EXTERNAL_REVIEW_R2_2026_09_17/REVIEW_RB2.md` | sha256 `d8eafdd67119…462f72a`（27,839 B） |
| 评审表（双盲同一份） | `C:\tmp\review_ftfb_2026_09_17\packet_RB{1,2}\REVIEW_FORM.md` | sha256 前 12 位 `34211db5b623`（字节一致） |
| 原包 | `C:\Users\Administrator\Downloads\ftfb_external_review_v2_20260917.tar.gz` | 417,674 B，成员 7，路径穿越 NONE |
| 解压件 5/5 vs 包内 manifest | `C:\tmp\review_ftfb_2026_09_17\ftfb_external_review_v2_20260917\` | ALL MATCH |

**最终建议（编辑部口径）**：Minor Revision。内容层可达 accept-track（双方 H=7）；T-1 排版阻断项必须在下一轮交付前闭合，并为其建立视觉层质量门，防止"全零绿但全页摘要"再次带病放行。

—— Trae code（编排/编辑），2026-09-17
