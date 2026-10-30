# 查理 · v9 正文 AI 披露节起草件（Deposon II v9 · 2026-10-14）

> **承办**：查理-论文主笔 ｜ **性质**：正文 AI 披露节字面起草（新名新件；**0 改任何既有件**，植入归戴夫下轮，本席 0 改 tex）
> **任务链**（PI 十令照序）：**00:26:51**（四项事实＋体裁授权「正文披露节之改版轮」）→ 管理员派单 00:28:46 → **00:29:36**（KIMI 上传／各类 agent 参与 V4 创题脑暴／「要符合 arxiv 相关要求而非照录」）→ **00:33:35**（「应为 trae 而非 trea」／workbuddy·豆包·千问参与脑暴／「各 agent 均是创建自身子代理自行头脑风暴而 minimax 汇总」）→ **00:35:22**（「写 ftfb 论文时不是创建了一套纪律吗怎么没沿用？」，处置见 §⑤）→ **00:41:19**（coze 负责与合作方联系与汇报所用 PDF＋亦参与脑暴）→ **00:42:19**（「我记得人类贡献也要披露」）→ **00:44:39**（「沿用前两作，加上多 agent 传递与协调等，其中 letter 是重要形式」）→ **00:45:08**（「此外 github 地址披露了吗？」）→ **00:47:35**（「确应为 claude，此外 KIMI 创建的第一作基础不可忽视」）→ **00:48:14**（「简单推理由 minimax 完成」）→ 本件。
> **事实基准**：与前令「AI 披露处置要如实」（00:12:11）同一事实基准（戴夫 MOD-108421 收口件在案）。

---

## 〇、语言与体裁实测（任务 1 先行项）

- **v9 main.tex 实测**：`8fa073e35fe0` · 179,926 B（同指纹两处：`戴夫_arXiv预印本_v9_2026_10_12/latex源包/main.tex` 与 `戴夫_GLM回函交付包_2026_10_13/arXiv提交四件套/latex源包/main.tex`）。
- **正文语言＝英文**：题名／摘要／Keywords／§1–§7／附录 A–G／thebibliography 全英文；CJK 环境仅为容器，服务全文 19 处引文式登记字面（如 L215「我的思维方式可以被 AI 批判性学习……」、L753「来源已改」≠「理论已到位」等）。⇒ **披露节语言＝英文，随正文。**
- **体裁**：沿前两作正文披露节先例——survey（`keep_the_books_survey.tex` L514 `\section*{AI use disclosure}`）／FTFB（`fiction_that_feeds_back.tex` L418 `\textbf{AI disclosure.}` 段）。本稿取 **survey 形（`\section*`）**，理由见 §②。
- **GitHub 地址实测（00:45:08 问）**：v9 main.tex **0 URL 命中**（全文仅 `\urlstyle/\UrlBreaks` 宏行）；第一作在案披露形态＝题头「Repository: \url{https://github.com/zeroandcat/Deposon}」行＋`\section*{Artifact availability}` 节——逐字稿已补仓库地址句（§①），availability 独立节列为植入轮备选（§②）。
- **FTFB 纪律集**（PI 00:35:22 所指「一套纪律」）：在案于阿兰《FTFB AIGC 标识合规评估_2026-10-08》§1.1 八要素表＋FTFB tex 字面——本稿逐要素沿用＋PI 增补面，映射见 §⑤。

---

## ① 披露节逐字稿（LaTeX 即用字面，植入驻戴夫下轮）

**逐字稿（`\section*` 标题＋整段＝1 段；纯 ASCII；源 375 词／2,567 字符，渲染层 375 词／2,560 字符；段落自身 sha256[:12]＝`25674ce47e83`）：**

```latex
\section*{AI use disclosure}

The framework and the research direction were provided by the principal investigator, the criteria were pre-registered before the runs, and every disposition was adjudicated under the principal investigator's direction. This manuscript was then prepared with AI assistance, and the AI participation is stated in full. The drafting model is GLM; the manuscript was drafted, reviewed, and verified by a multi-agent pipeline under that direction. All experimental readings, verdict literals, thresholds, counts, and fingerprints reported in this paper are transcribed from sealed on-repository artifacts and were mechanically re-verified; they are not AI-generated content. AI participation went beyond drafting: the V4 (distillation) line of this work was created in a multi-agent brainstorm in which agents of every role in the team took part, together with Workbuddy, Doubao, Qianwen, and coze, among others; each agent spawned its own sub-agents to brainstorm independently, and minimax consolidated the results. The experimental line was run in the minimax code client: the main agent dispatched sub-agents to execute the experiments, the sub-agents being all minimax models, while the main agent itself used minimax, MiMo, and DeepSeek, among others. Codex and Claude both participated in the theoretical derivations, and the simple reasoning was completed by minimax. Bug fixing during development was handled by GLM through the Trae client. The PDF files used for partner contact and reporting were handled by coze, and upload-side operations were handled with the assistance of Kimi. This work builds on the program's first paper, whose foundation (the core algorithm, the experimental pipeline, the data-analysis scripts, and the first draft) was produced with the assistance of KIMI-K3 under the author's direct instruction, as that paper's own disclosure records. Across these faces, work was transmitted and coordinated between agents, with letters as an important form of that transmission and coordination. The draft was examined by multiple independent rounds of machine review, with each finding adjudicated by the team and its disposition recorded in the appendices' governance and repair-round registers (Appendices B and G) rather than silently absorbed; each number in the text maps to its sealed artifact, cited in place and registered in the evidence ledger (Appendix A); the program's public repository is \path{github.com/zeroandcat/Deposon}. The author reviewed the manuscript and takes full responsibility for the entire content of this paper.
```

**事实覆盖面对照（逐项＝PI 十令字面）**：

⓪ 人类贡献面（框架＋研究方向＝PI 提供；准则预注册；裁决于 PI 指挥下）〔00:42:19〕
① 撰写线（多 Agent 流水线·PI 指挥·GLM 起草方）〔00:26:51「你们写论文」＋委托书 v0.6〕
② 数据排除面（封存件转引＋机械复验·非 AI 生成）
③ V4 创题脑暴（各类 agent＋Workbuddy/Doubao/Qianwen/coze 等·各 agent 自建子代理自行脑暴·minimax 汇总）〔00:29:36／00:33:35／00:41:19〕
④ 实验线（minimax code 客户端主代理派遣子代理·子代理均 minimax·主代理曾用 minimax/MiMo/DeepSeek 等）〔00:26:51〕
⑤ 理论推导（Codex 与 Claude 均参与）＋简单推理（minimax 完成）〔00:26:51／00:48:14〕
⑥ 修 bug（Trae 客户端 GLM）〔00:26:51〕
⑦ 合作方联系与汇报 PDF（coze）〔00:41:19〕
⑧ 上传（Kimi）〔00:29:36〕
⑨ 第一作基础（KIMI-K3 产核心算法/实验管线/数据分析脚本/初稿）〔00:47:35〕
⑩ 多 agent 传递与协调（letter 为重要形式）〔00:44:39〕
⑪ 评审裁决记录面（App B/G·不静默吸收）
⑫ 数字锚定面（App A）＋公开仓库地址（github.com/zeroandcat/Deposon）〔00:45:08〕
⑬ 作者终审负全文全责（第一作「entire content」形）

**PI 可选变体（0 径行；择一告知戴夫即可，其余不进稿）**：

- **V1（责任句单复数）**：本稿默认单数（独作在案「Qihao Yuan」＋survey 先例单数）；若与表单层三件式对齐取复数，换为 `The authors reviewed the manuscript and take full responsibility for the entire content of this paper.`（表单层单复数漂移系戴夫收口件已登记之悬置项，归 PI）。
- **V2（第一作句式增强，沿 arXiv:2609.09001 线上 §8 既有形态）**：政策锚句 `...takes full responsibility for the entire content of this paper under arXiv's authorship and AI-use policy.`＋直白否定句 `No content was generated by the AI without human review.`（＝阿兰评估件「增强项 B」同款；第一作线上版在案，FTFB 未采，故列变体不进主稿）。

**拼字处置表（草案用形 ← PI 字面 ← 盘内在案名）**：

| 草案用形 | PI 字面 | 盘内在案 | 备注 |
| :-- | :-- | :-- | :-- |
| minimax | minimax | 全案小写（minimax 委托信族／coze weekly） | 客户端名「minimax code」整名照用 |
| MiMo | mimo | `or_models_snapshot_2026_09_17.json`「Xiaomi: MiMo-V2.5-Pro」 | 案内大小写两见（weekly「mimo」），取产品名形 |
| DeepSeek | deepseek | P-A 主干 `deepseek-v4-pro` 在案 | — |
| GLM | GLM | 全案大写 | — |
| Trae | tra（00:26:51）→ **trae（00:33:35 PI 自正）** | 盘内「Trae」（minimax 委托信 §3「Trae/D 族处置」等） | PI 拼字更正已在案，登记字面两存 |
| Codex | codex | 回函自报「Model actually used: Codex」 | — |
| Claude | cloud（00:26:51）→ **claude（00:47:35 PI 确认）** | 回函自报「Claude, made by Anthropic」 | PI 两次字面均照录登记；案内名取 Claude |
| Kimi | KIMI | 上传侧回函具名 Kimi（v0.6 委托书 §1 引） | 上传面用 Kimi |
| KIMI-K3 | KIMI（00:47:35） | 第一作线上 §8 字面「KIMI-K3 (Moonshot AI)」 | 第一作基础面沿用其已发表字面 KIMI-K3 |
| Workbuddy | workbuddy | coze weekly L76「WorkBuddy」 | 大小写取 weekly 形 |
| Doubao | 豆包 | V4 D1 件「VS/workbuddy/豆包」＋主干 `doubao-seed-*` 在案 | 中文→罗马化 Doubao |
| Qianwen | 千问 | 盘内 0 直接命中（qwen3＝实验主干，另一面） | 千问→罗马化 Qianwen；PI 字面唯一源 |
| coze | coze | 全案小写（coze weekly／委托书「以供 coze 与 GLM 使用」） | 案内形即小写，照用 |

---

## ② 置入位置建议（沿 v9 结构）

**主案（推荐）**：插入于 **v9 main.tex（8fa073e35fe0）L757 尾注段之后、L759 `\pdfbookmark[0]{References}{bmrefs}` 之前**（即「End of draft v9…」登记段与 References 书签之间），形制：

```latex
\pdfbookmark[0]{AI use disclosure}{bmaidisc}
\section*{AI use disclosure}

（逐字稿段落）
```

**理由**：
1. **先例槽位保真**：两先例披露节均落「全文内容之末、参考文献紧前」——survey L514 `\section*{AI use disclosure}` → L518 thebibliography；FTFB L418 披露段 → L420 `\section*{References}`。v9 的同构槽位＝附录 G 之后、thebibliography 之前；L757 尾注系版本登记性元注（非读者面内容），其后本为 back-matter（参考文献紧随其后），披露节入该区间即「紧贴参考文献前」之精确先例槽位。
2. **形制取 survey 形**（`\section*`）而非 FTFB 加粗段形：v9 参考文献前最后内容是登记体附录 G，无节标题的裸段落将成附录 G 流内孤儿段；`\section*` 干净收束附录并启 back matter。程序内在案先例 3 作中 2 作取独立小节形（第一作线上版编号小节 §8＋survey），小节形为多数形。
3. **0 扰动**：尾注段（「End of draft v9…」身份匿名惯例登记）0 改动，其「draft 内容止于此」语义保持（披露节与参考文献同属其后 back-matter）；`\pdfbookmark` 书签键 `bmaidisc` 全文唯一，沿 v9 每节配书签之既有体例。

**备选（登记不推荐）**：(a) 尾注段之前（附录 G 自检段后）——披露节成正文末节，尾注退居其后；两可，但先例槽位保真度低半档。(b) FTFB 加粗段形——见上理由 2，弃。

**植入轮备选（第一作形态，归 PI＋戴夫，超出本轮披露节射程）**：另立 `\section*{Artifact availability}` 节（第一作 round-4 在案形态：「All code, frozen JSONs, verdict pure functions, and the test suite ship inside the repository…」——v9 对应表述须按本作实况重铸，非照搬）＋题头 Repository 行；若立，位置紧邻披露节前后由戴夫排版定。

**植入轮注意（归戴夫）**：①页数将从 54 页起浮（本稿约 +0.4 页），Comments 字段页数须植入后实测重登；②尾注段之轮次描述（G.2–G.9）届时由戴夫按改版轮体例更新，归戴夫；③除插入区间外 0 改一字（diff 面即「L757/L759 间新增一节」）。

---

## ③ 与表单层三件式（元数据件 §6）并立关系与一致性登记

**并立关系**：同一生产事实之两个披露载体——**正文披露节**（读者面·逐项全列·PI 00:26:51 改版轮授权）与**表单层三件式**（提交元数据·压缩形·元数据件 §6 在案，454 B／sha12 `45de44ebc4da`）。先例对照：前两作＝正文披露节＋表单层无动作；本作＝表单三件式先在案＋正文披露节本轮授权补齐——两层自此并立。

**逐句一致性映射**：

| 披露节句 | 表单三件式句 | 一致性 |
| :-- | :-- | :-- |
| 「This manuscript was then prepared with AI assistance」＋「drafted, reviewed, and verified by a multi-agent pipeline under that direction」 | 「prepared with AI assistance (a multi-agent drafting, review, and verification pipeline operating under the direction of the principal investigator)」 | **实质同一**（管线短语逐词对齐；方向句前移至首句＝人类贡献面，表单层括注内的方向语义不减） |
| 「all experimental readings, verdict literals, thresholds, counts, and fingerprints … transcribed from sealed on-repository artifacts and were mechanically re-verified; they are not AI-generated content」 | 同款句（454 B 件第二句） | **逐项同一**（本稿仅加 `reported in this paper` 限定） |
| 「The author reviewed the manuscript and takes full responsibility for the entire content of this paper.」 | 「The authors reviewed the manuscript and take full responsibility for its content.」 | **两处差异＝单复数＋entire content 升格**（后者＝第一作 §8 形）。单复数对齐二途：表单层改单数，或本稿取 V1 复数变体——**归 PI 择**；entire content 形沿第一作在案口径，0 新创 |
| 工具逐项点名（minimax/MiMo/DeepSeek/GLM/Trae/Codex/Claude/Kimi/KIMI-K3/Workbuddy/Doubao/Qianwen/coze＋脑暴机制＋letter 形式） | 表单层不携带（压缩为 multi-agent pipeline） | **互补非矛盾**：正文层全列、表单层压缩，同一事实两种粒度 |

**表单层处置衔接**：戴夫收口件 §③ 选项（A／B1／B2／C）仍归 PI；正文披露节在位后，B2（表单层留档、以正文披露承担合规面）成为自然择项——仅作观察登记，**0 代裁**。

---

## ④ 事实源与佐证链登记

**唯一主源＝PI 十令字面（照录）**：

1. **00:26:51**：「正文无披露节怎么能行呢？minimax code客户端主代理派遣子代理实验、子代理均minimax，主代理曾用minimax与mimo及deepseek等，trea客户端GLM修bug，你们写论文，codex与cloud均参与理论推导」
2. **00:29:36**：「此外KIMI上传，各类agent均参与V4创题的头脑风暴，要符合arxiv相关要求而非照录」
3. **00:33:35**：「应为trae而非trea，workbuddy与豆包及千问等都参与了头脑风暴，各agent均是创建自身子代理自行头脑风暴而minimax汇总」
4. **00:35:22**：「写ftfb论文时不是创建了一套纪律吗怎么没沿用？」（质询，处置见 §⑤，非新增事实）
5. **00:41:19**：「此外coze负责与合作方联系与汇报所用的pdf文件，也参与了头脑风暴」
6. **00:42:19**：「我记得人类贡献也要披露」
7. **00:44:39**：「沿用前两作，加上多agent传递与协调等，其中letter是重要形式」
8. **00:45:08**：「此外github地址披露了吗？」
9. **00:47:35**：「确应为claude，此外KIMI创建的第一作基础不可忽视」
10. **00:48:14**：「简单推理由minimax完成」

**逐项佐证交叉（可选件实测）**：

| 项 | PI 字面要点 | 盘内佐证 | 判定 |
| :-- | :-- | :-- | :-- |
| ①实验线 | minimax code 客户端·主代理遣子代理·子代理均 minimax·主代理曾用 minimax/mimo/deepseek 等 | `upload/6accd9993fbf9a6239c93c54`（minimax 委托面承接＋R4 解除登记，2026-10-12）：minimax 实验线在案（G-E01/G-E07/G-E08；该面 R4 三解除后 ≈500 LLM calls 可行）。**如实注记**：该件登记「承接≠开跑·三条件前置未满足」（10-12 时点）——与 v9 摘要自陈 distortion-bound 实验「stands blocked」一致，无矛盾；执行线之配置（主代理遣子代理）以 PI 字面为主源。MiMo＝V4 蒸馏线端点在案（coze weekly 挂点4）；DeepSeek＝P-A 主干在案 | 一致；范围差如实登记归 PI |
| ②修 bug | trae 客户端 GLM | 指定佐证集内无直接件；Trae 拼写盘内在案（minimax 委托信 §3）。**PI 字面＝唯一源（派单即如此设计），如实登记** | 无佐证、无矛盾；不编造 |
| ③撰写线 | 本团队（多 Agent 流水线·PI 指挥）·GLM 起草方 | `upload/6acc7ebc08dbe77367b425fd`（委托书 v0.6，2026-10-12）：「致：GLM（论文终稿起草方；沿 2026-09-24 起既有委托线）」——直接佐证 | 一致 ✓ |
| ④理论推导 | codex 与 claude 均参与 | `upload/6accd5a39202e63821b6074b`（codex 回函，2026-10-10）：自报「Model actually used: Codex; based on GPT-6」，函内引 09-30 推导回函族；`upload/6accd58c4053fcb739ad7e33`（claude 回函，2026-10-11）：自报「Claude Code — Claude, made by Anthropic」，七缺口类收口（理论线处置）。Claude 拼字＝PI 00:47:35 确认「确应为claude」 | 一致 ✓ |
| ⑤KIMI 上传 | KIMI 上传 | 委托书 v0.6 §1 引上传侧回函（Kimi→PI，`fcb0a673ee5c`·461 脱敏件远端 SHA 登记·2026-10-12）；W3 上传委托在案（`shared/鲍勃_KIMI上传委托_W3归仓_2026-09-28.md`）。**如实注记**：本作自身 arXiv 仪表板动作系 PI 侧（MOD-108421 轮五步）——披露稿取「upload-side operations」中性表述，具体射程以 PI 字面为准 | 一致；射程归 PI |
| ⑥V4 创题脑暴 | 各类 agent＋workbuddy/豆包/千问/coze 等·各 agent 自建子代理自行脑暴·minimax 汇总 | 四角色件在案（查理贡献形状／爱丽丝理论新种子／鲍勃证据新种子／阿兰文献新种子，2026-09-20）＝「各类 agent 参与」；coze weekly L76「多 agent（Mavis／TRAE／Kimi／Claude Code／Codex／WorkBuddy 等）回函与接受函全部落盘」＋ coze 自身 V4 回函在案（`letters/_v4_distillation_reply_coze_2026_09_20.md`·71,084 B）；豆包＝V4 D1 件在案（「VS/workbuddy/豆包」）；**千问＝盘内 0 直接命中（qwen3 系实验主干，另一面），PI 字面唯一源**；「自建子代理＋minimax 汇总」机制＝PI 字面，佐证集内无反向证据 | 主体一致；千问与机制面如实登记 |
| ⑦合作方联系与汇报 PDF | coze 负责 | coze 汇报线在案（coze-v3x-weekly 报告体＝coze 产出；calibration-note 族）；「与合作方联系所用 PDF」具体件佐证集内未定位——**PI 字面＝主源，如实登记** | 无矛盾；不编造 |
| ⑧人类贡献面 | 人类贡献也要披露 | 第一作线上 §8 在案（阿兰评估件 §2.1 转录）：「The Deposon framework definition and the project's research direction were provided by the corresponding author」＋「The author reviewed and edited every section」；v9 自身内证：证据强度约定（closed＝pre-registered）＋B 族 resolution／G 族处置（「ruled by the team resolution」）——逐字稿首句（框架/方向＝PI 提供·准则预注册·裁决于 PI 指挥下）即此形 | 一致 ✓（第一作直证＋v9 内证） |
| ⑨多 agent 传递协调＋letter 形式 | letter 是重要形式 | 函件族在案＝本作生产链传递载体：codex/claude/minimax 回函、V4 邀请函＋各 agent 回函/接受函（coze weekly L76「回函与接受函全部落盘」）、委托书族（v0.5/v0.6）、对齐函（`letters/_alignment_reply_crossface_three_items_2026_10_12.md`） | 一致 ✓ |
| ⑩GitHub 地址 | 披露了吗？ | **实测答复：v9 0 URL**（全文仅 `\urlstyle` 宏）。第一作在案形态＝题头 Repository 行＋`\section*{Artifact availability}`（round-4 README 载「byte-for-byte」升节史）；公开地址 `github.com/zeroandcat/Deposon`（clue book 族/鲍勃上传执行记录在案）。逐字稿补仓库地址句：scope＝「the program's public repository」在案事实＋App A 锚定指针，**0 逐件入仓主张**（v9 App A 之 deposon_team/ 族系 workspace 路径，故不主张全链入公开仓）。`zeroandcat`＝第一作 arXiv 已公开之仓库属主 handle（非团队成员名，无新增暴露面；〔W老师〕暴露面管理系仓内容面，与地址公开性无涉——鲍勃盘点件在案） | v9 未披露（如实）→ 已补；scope 收敛如实登记 |
| ⑪第一作基础＝KIMI-K3 | KIMI 创建的第一作基础不可忽视 | 第一作线上 §8 字面（直接佐证）：「The core algorithm, the experimental pipeline, the data-analysis scripts, and the first draft of this manuscript were produced with the assistance of KIMI-K3 (Moonshot AI) under the author's direct instruction」——逐字稿该句即其沿用（括注四件套＋`under the author's direct instruction`＋`as that paper's own disclosure records` 指回） | 一致 ✓（直证沿用） |
| ⑫简单推理＝minimax | 简单推理由 minimax 完成 | 指定佐证集内无直接件；minimax 实验线参与在案（①行）。**PI 字面＝唯一源，如实登记** | 无佐证、无矛盾；不编造 |
| ⑬体例令 | 「符合 arxiv 相关要求而非照录」 | 两先例披露节均经 arXiv 提交通道在案（survey 通道件／FTFB 提交链）；学术散文体、非聊天照录 | 按令执行 ✓ |

**0 团队成员人名自查**：逐字稿 13 工具名＋「principal investigator／the team／the author／zeroandcat（第一作已公开仓库 handle）」，**0 团队成员人名** ✓。
**总纪律自查**：0 编造（修 bug／汇报 PDF／千问／脑暴机制／简单推理五面如实标注「PI 字面唯一源」）·0 美化 ·0 合并 ·0 扩射程（「等」译「among others」，列名以 PI 点名为限；coze weekly 名单中的 Mavis/TRAE/VS 等未点名项不进稿）·0 披露未经 PI 声明之事实。

---

## ⑤ FTFB 纪律集沿用对照（回应 PI 00:35:22 质询）

**质询直答**：FTFB 轮创建的披露纪律集（在案：FTFB tex L418–419 字面＋阿兰 AIGC 合规评估件 §1.1 八要素表）**本稿已逐要素沿用**；v9 起草当时正文未置披露节，该缺口系戴夫 MOD-108421 收口件 §⑤ 已如实登记之「改版轮事项」——PI 00:26:51 令即该改版轮授权，本轮补齐，纪律自本稿起沿用入正文。

| FTFB 要素（阿兰评估件 §1.1） | FTFB 字面 | 本稿对应句 | 判定 |
| :-- | :-- | :-- | :-- |
| E1 起草模型具名 | The drafting model is GLM, used for drafting and revision support under author instruction | The drafting model is GLM … under that direction | ✓ 沿用 |
| E2 创作主体句 | The claims, the criteria, the mapping, and every number were specified by the authors | 首句：框架/研究方向＝PI 提供＋准则预注册＋裁决于 PI 指挥下（v9 之更强形：pre-registered 而非仅 specified） | ✓ 沿用（按本作实际纪律升格） |
| E3 参与全列 | retrieval/matching/… ran with machine assistance | 「AI participation went beyond drafting」＋七面逐项（脑暴/实验/理论＋简单推理/修 bug/汇报 PDF/上传/第一作基础） | ✓ 沿用＋按 PI 现令点名工具（见下「唯一泛化」） |
| E4 脚本复核句 | anchor digests and frozen numbers re-checked by script | mechanically re-verified | ✓ 沿用 |
| E5 第三方重算系 machine agent 句（v6 增） | （machine agent 如实披露） | multiple independent rounds of **machine** review（机械复核＋机审主体明示） | ✓ 沿用 |
| E6 评审裁决记录句 | each review finding adjudicated by the authors and its resolution recorded in the revision record rather than silently absorbed | adjudicated by the team and its disposition recorded in the appendices' governance and repair-round registers (Appendices B and G) rather than silently absorbed | ✓ 沿用（v9 之修订记录＝附录 B/G） |
| E7 作者全责句 | The authors directed all work, adjudicated all findings, and bear full responsibility for the result | The author reviewed the manuscript and takes full responsibility for the entire content of this paper.（entire content＝第一作形；单复数变体 V1 在案） | ✓ 沿用（数＝独作在案；形＝第一作升格） |
| E8 field path 对应句 | Each number in §7 maps to a field path in the frozen artifact cited in place | each number in the text maps to its sealed artifact, cited in place and registered in the evidence ledger (Appendix A) | ✓ 沿用（v9 之对应件＝附录 A） |
| E9 identifier-pending 句（v5 起随池闭合而删） | （状态依存件） | n/a——v9 参考文献自有体例，0 强制移植 | 依状态不沿用 ✓ |

**PI 增补面（前两作未含、PI 十令新增，如实分层登记）**：

| 增补面 | PI 令 | 逐字稿句 | 性质 |
| :-- | :-- | :-- | :-- |
| 人类贡献面 | 00:42:19 | 首句（框架/方向/准则/裁决）＋末句（作者终审负全文全责） | ＝第一作 §8 首句形之回摆＋FTFB E2/E7 人类侧面，纪律集内在要素显式化 |
| 多 agent 传递协调＋letter 形式 | 00:44:39 | Across these faces, work was transmitted and coordinated between agents, with letters as an important form… | PI 增补（先例未含） |
| 仓库地址句 | 00:45:08 | the program's public repository is \path{github.com/zeroandcat/Deposon} | ＝第一作题头/availability 形之内嵌版 |
| 第一作基础＝KIMI-K3 | 00:47:35 | This work builds on the program's first paper, whose foundation (…) was produced with the assistance of KIMI-K3 under the author's direct instruction, as that paper's own disclosure records | ＝第一作 §8 既有披露之沿用（直证） |
| 简单推理＝minimax | 00:48:14 | the simple reasoning was completed by minimax | PI 增补（先例未含） |

**唯一有意泛化（如实登记，归 PI 终裁）**：FTFB E3 以功能式「machine assistance」表述、不点名工具；本稿按 PI 五令（00:26:51／00:29:36／00:33:35／00:41:19／00:48:14）**逐项点名工具**。此系 PI 现令授权之射程（「逐项点名」＋「符合 arxiv 相关要求」）；若 PI 择 FTFB 功能式收敛，替换为一单句即可（`The brainstorming, experiments, theory work and simple reasoning, engineering fixes, reporting, and upload operations described above ran with machine assistance under the team's direction.`），逐字稿其余 0 动。

**第一作（arXiv:2609.09001 线上 §8）要素**：政策锚句＋直白否定句以 V2 变体在案（§①），0 径行入主稿；KIMI-K3 基础句已按 00:47:35 令入主稿（直证沿用）。

---

## 纪律回执

- **0 改任何既有件**：本件为 shared/ 新名新件；v9 tex（8fa073e35fe0）、元数据件、戴夫收口件、全部佐证件 0 动。
- **0 远端**：全程盘内只读取证（含第一作 en 包本地解包核字面），0 网络 0 推送 0 上传。
- **植入归戴夫下轮**：本席 0 改 tex；逐字稿＋插入位点（§②）移交。
- 悬置归 PI（0 代裁）：V1 单复数对齐／V2 第一作增强／FTFB 式功能收敛／表单层处置衔接／availability 独立节（§② 备选）。
- 本件自身指纹不在件内，落盘后以群回执钉定。

—— 查理-论文主笔 · 2026-10-14 · 任务链十令在案（§④）
