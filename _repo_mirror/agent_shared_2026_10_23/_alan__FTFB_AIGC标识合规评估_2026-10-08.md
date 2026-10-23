# 阿兰 · FTFB 论文 AIGC 标识合规评估（2026-10-08）

- **任务来源**：群管理员 2026-10-08 13:56:56 派单（期限今日 15:30）
- **触发背景**：PI 2026-10-08 13:50 群消息转达平台 AI 标识新规四要点，问 FTFB 论文要不要更新；并确认 deposon 论文投 arXiv 时已做 AIGC 声明加科研助理署名，FTFB 是否需对齐待评估
- **方法**：盘面只读核验（各版 tex/metadata/PDF 逐版 grep+diff+sha256sum）＋群历史溯源（09-17 至 10-08 投稿链全程）＋arXiv 线上实测（2609.09001 摘要页与 HTML 全文，2026-10-08 14:05 抓取）＋FTFB 公开状态两组检索复查
- **纪律执行**：0 编造（不可确证处已列 §七 待 PI 清单）；只读 0 覆写；repos/Deposon 克隆未触碰、0 上传推送；交付仅落 shared/ 本件

---

## 〇、结论速览

**总判定：待 PI 裁（分层呈报；硬合规层面无需更新）。**

| 层面 | 判定 | 一句话依据 |
|---|---|---|
| 正文主动标注（新规要点 2） | **无需更新** | v4 上传版起**所有** FTFB 版本正文均带 AI disclosure 段（§9 结论章末、附录前），主动标注在位且详尽度不低于 deposon 先例 |
| 创作思考主体口径（要点 1） | **无需更新** | "The claims, the criteria, the mapping, and every number were specified by the authors"＋"The authors directed all work, adjudicated all findings"——创作主体=作者、AI=指令下辅助的口径句齐备 |
| arXiv 元数据 Comments | **无需更新（先例对齐已达成）** | deposon 线上版 Comments 实测**同样无** AI 标注语（"23 pages, 5 figures. Author affiliation: … Code: …"）；FTFB 各版 Comments 亦无——两文形态一致，非缺口 |
| 「科研助理署名」面 | **不缺位** | FTFB 披露段 GLM 具名（drafting model under author instruction）＝deposon 线上版 KIMI-K3 (Moonshot AI) 具名（assistance under direct instruction）的等价形态；AI 记名在正文披露内，两文均未进作者列表 |
| 形态增强对齐（可选） | **待 PI 裁** | 两候选增强项（升格独立小节／补直白否定句），见 §五更新范围；建议绑定 R4 解除挂起的下一次 replace/重投轮一并执行，不单独开轮 |

线上版态（详见 §四）：原投=09-18 R3＋KIMI 自改（提交包指纹未留档，待 PI 确认）；09-28 PI 通报已重投（提交包是否即 R4 终版待 PI 确认）；截至今日 14:05 检索无公开件；R4 提交挂起（P6/P7 待 PI 输入）。

---

## 一、FTFB 各版 AI 披露盘点（任务 1）

### 1.1 披露段正文（唯一 AI 披露落位：正文段；各版均无 Acknowledgments 节）

落位：`\textbf{AI disclosure.}` 加粗段落，位于 §9 "Conclusion: The Criteria Turned on Themselves" 章末、"Appendix: Verification Statement" 之前（v4/终版在 L418，v5 起行号移至 L480）。全文指纹实测见 §六。

各版披露段构成逐项（✔=在位）：

| 要素 | v4 上传版 (L418) | arXiv 终版 (L418) | v5 (L480) | v6 (L480) | R3 (L480) | R4 (L480) |
|---|---|---|---|---|---|---|
| 起草模型具名（GLM, drafting+revision support under author instruction） | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 创作主体句（claims/criteria/mapping/numbers specified by the authors） | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 参与全列（retrieval/matching/引用池逐条核验 ran with machine assistance） | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 脚本复核句（anchor digests＋frozen numbers re-checked by script） | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| **第三方重算系 machine agent 句**（§7.2, 2026-09-18） | ✘ | ✘ | ✘ | ✔ | ✔ | ✔ |
| 多轮独立 machine review＋作者裁决记录句 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| 作者全责句（directed all work, adjudicated all findings, bear full responsibility） | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| §7 field path 对应句 | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| identifier-pending 句（two entries flagged in §1.3(ii)） | ✔ | ✔ | ✘ | ✘ | ✘ | ✘ |

**版本间差异（两处，均已 diff 实证）**：
1. **machine agent 句**：v4/终版/v5 无 → **v6 起增补**（KIMI 验收轮 m5 修订项：如实披露 §7.2 第三方重算由 machine agent 而非人类第三方执行）。管理员锚点「R4 较 09-18 版增补第三方重算系 machine agent 条目」与实测吻合。
2. **identifier-pending 句**：v4/终版有 → **v5 起消失**（v5 起引用池标识符闭合，对应 v5 metadata Comments「pool identifiers closed as of this edition」，演进合理）。

一致性核验（diff 逐字节）：v4=终版（两者唯一差异在 L81 摘要压缩 2216→1849 字符，披露段零改动）；v6=R3=R4（L480 逐字节一致）。R4 披露段与 R3 逐字相同，与鲍勃验收报告「verdict 区块与 R3 逐字节一致」结论同向。

### 1.2 arXiv 元数据（Comments 字段，各版实测）

| 版本 | tar.gz | Comments 字段（全文） | AI 标注语 |
|---|---|---|---|
| v4 上传版 09-18 | ftfb_arxiv_2026_09_18.tar.gz (d122b737c823, 36,765 B) | `24 pages, 2 tables, no figures` | 无 |
| arXiv 终版 09-18 | ftfb_arxiv_final_2026_09_18.tar.gz (845dbe8555be, 36,701 B) | `24 pages, 2 tables, no figures` | 无 |
| v5 09-18 | ftfb_arxiv_deep_rev_2026_09_18.tar.gz (aab3243303e1) | `24 pages; deep-revision edition with verification appendix (closed reference pool of 56 entries; pool identifiers closed as of this edition)` | 无 |
| v6 09-18 | ftfb_arxiv_accept_rev_2026_09_18.tar.gz (fbb7bec73344) | `25 pages; acceptance-revision edition with verification appendix (…)（同上括注）` | 无 |
| R3 09-18 | ftfb_arxiv_r3_rev_2026_09_18.tar.gz (741c9f24b447, 444,555 B) | `24 pages; R3 revision edition with verification appendix (…)（同上括注）` | 无 |
| R4 09-27 | （戴夫编译交付无独立 tar.gz，见 §五注） | `25 pages; R4 revision edition: public-record citation switch (repository-relative paths at the frozen commit); availability terms updated; measurement anchors unchanged` | 无 |

各版作者字段均 Qihao Yuan（独作），License CC BY 4.0，无 AI 相关语。PDF 侧 hyperref 元数据 pdfauthor=Qihao Yuan（v5/R3/R4 验证链记录）。

### 1.3 盘点小结

FTFB 的 AI 披露**自 v4 上传版起全线在位、从未缺席**：落位=正文披露段（单落点）；元数据面=无（Comments 仅页数与版本说明）；无致谢节。09-17 23:51 PI「AI贡献如实披露」指示后由查理重写引入（群史溯源），此后 v4→R4 五版六件持续演进，仅 §1.1 两处差异，方向均为**更如实**（v6 增 machine agent 句）或**状态闭合**（v5 删 identifier-pending 句）。

---

## 二、deposon 先例实测与逐项对表（任务 2）

### 2.1 线上版实测（arXiv:2609.09001v1，2026-10-08 14:05 抓取摘要页+HTML 全文）

- 提交：2026-09-08 16:40:31 UTC，From: Qihao Yuan，1,598 KB，公开（cs.AI 主类；cs.LG）
- 标题：*Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths*（英文版）
- 作者：Qihao Yuan 独作（作者列表无 AI 项）；首页 \thanks 注含 "Project version: Deposon v2"
- **Comments 字段（全文）**：`23 pages, 5 figures. Author affiliation: School of Chemistry and Life Resources, 〔高校R〕 University of China. Code: this https URL` —— **无 AI 标注语**
- back-matter 结构：5 Conclusion → Acknowledgments（无编号，仅"thanks colleagues for discussions"）→ 6 Data availability → 7 Artifact availability → **8 AI use disclosure（独立编号小节）** → Appendix A → References

**「8 AI use disclosure」小节全文（线上实测逐字）**：

> The Deposon framework definition and the project's research direction were provided by the corresponding author. The core algorithm, the experimental pipeline, the data-analysis scripts, and the first draft of this manuscript were produced with the assistance of KIMI-K3 (Moonshot AI) under the author's direct instruction. The author reviewed and edited every section, verified all numerical claims against the frozen JSONs in the repository, and takes full responsibility for the entire content of this paper under arXiv's authorship and AI-use policy. No content was generated by the AI without human review, and no proprietary model weights are required to reproduce any result in this paper.

### 2.2 本地 round4 包与线上版的差异（如实登记）

本地四轮终版包实测：`deposon_arxiv_2026_cn.tar.gz`（0e652f21cbc00b80ebb7cf5cf42303cb88e1273a16886169d8ba8f89ebad60e7）与 `deposon_arxiv_2026_en.tar.gz`（fd6eafe2014af52126132f80c56d9377ec788cb736656c45c1935c24822655f6），与简报登记指纹一致。但与线上 v1 比对存在**三处实质差异**：①小节名「Project version and author declaration」→线上「AI use disclosure」；②「KIMI (Moonshot AI)」→线上「KIMI-K3 (Moonshot AI)」且范围扩至 data-analysis scripts；③线上增补「No content was generated by the AI without human review」与「no proprietary model weights」两句。另线上标题较 round4 EN tex 改写、版本号 v0.1.1→v2。**结论：PI 实际提交的是 round4 之后的再修订版，其本地对应件未在 round4 目录**（对齐基准应取线上实测形态；本地对应件位置待 PI 指认，不推定）。

### 2.3 逐项对表（重点核：科研助理署名面、Comments 字段）

| 对表维度 | deposon 线上版（实测） | FTFB R4 备投版（实测） | 缺口判定 |
|---|---|---|---|
| AIGC 声明存在性 | 有（8 AI use disclosure 独立小节） | 有（AI disclosure 加粗段） | **无缺口** |
| 落位形态 | 独立**编号小节**（back-matter，可被目录/检索定位） | **章末加粗段落**（§9 内，无节标题） | 形态差异：显著度低一档，功能等价 → §五增强项 A |
| AI 具名（「科研助理」记名） | KIMI-K3 (Moonshot AI) | GLM | **不缺位**：均以「模型名+厂商」具名；均未进作者列表 |
| AI 角色表述 | assistance under the author's direct instruction | drafting and revision support under author instruction | 等价（指令下协助/支持） |
| 创作主体句 | framework definition + research direction provided by the corresponding author | claims, the criteria, the mapping, and every number specified by the authors | 均有；FTFB 粒度更细（到数字层） |
| 直白否定句 | "No content was generated by the AI without human review" | 无字面对应句（以"specified by the authors"+"adjudicated by the authors"承担同功能） | 差异存在 → §五增强项 B |
| 责任声明 | takes full responsibility **under arXiv's authorship and AI-use policy** | bear full responsibility for the result | 均有；deposon 引政策名，FTFB 未引 |
| 超出起草的参与如实列明 | data-analysis scripts 等（范围句内） | retrieval/matching/池核验 machine assistance＋脚本复核＋machine review＋machine agent 重算（独立长句） | FTFB **更详尽** |
| 致谢节 | 有（仅谢同事，非 AI 事项） | 无致谢节 | 差异存在，非 AI 合规必需项 |
| arXiv Comments 字段 | **无 AI 标注语**（23 pages, 5 figures…） | **无 AI 标注语**（25 pages; R4 revision edition…） | **一致——对齐已达成，无缺口** |
| 作者署名 | Qihao Yuan（〔高校R〕 院内系） | Qihao Yuan（无机构行，tex \author 仅姓名） | 一致（独作） |

**两项重点核结论**：①「科研助理署名」面 FTFB **不缺位**——PI 所指先例做法（AI 以助理角色记名）在两文的实现均为「正文披露内模型具名」而非作者列表署名，FTFB 的 GLM 具名与 deposon 的 KIMI-K3 具名等价；若 PI 对「科研助理署名」另有所指（如 arXiv 表单侧、协作平台署名面），盘面无载，见 §七-4。②Comments 字段：deposon 线上实测无 AI 标注语，FTFB 各版亦无——**现状态即与先例对齐，不存在缺口**。

---

## 三、新规四要点逐条映射（任务 3）

新规原文（PI 2026-10-08 13:50 群消息转述，本评估以转述四要点为准）逐条映射 FTFB 现有披露：

| 要点 | 新规内容 | FTFB 现状映射 | 判定 |
|---|---|---|---|
| 1 | 界定标准=创作思考主体是否本人；自己思考+AI 帮忙=辅助；AI 直接生成主体内容=代写 | 对应句齐备：**创作主体**="The claims, the criteria, the mapping, and every number were specified by the authors"＋"The authors directed all work, adjudicated all findings"（主张/判据/映射/数字=作者指定）；**AI 定位**="used for drafting and revision support under author instruction"＋"machine assistance"（指令下的辅助）；且如实声明 "AI participation went beyond drafting and is stated in full"——超出纯起草的参与全部列明并由作者裁决。**口径属「本人思考+AI 辅助」档，非代写档** | 已满足 |
| 2 | AI 生成或辅助内容须主动标注 | v4 上传版起所有版本正文均带 AI disclosure 段（§一盘点），主动标注在位 | 已满足 |
| 3 | 未主动标者平台自动加标 | 前提条件不触发（要点 2 已主动标注）；且本条为平台侧机制，见下方适用性说明 | 不适用/已消解 |
| 4 | 违规限流封禁 | 同上，为平台侧处罚机制 | 不适用 |

**arXiv 预印本场景与新规内容平台场景的适用性区分（照实说明，不越界代裁）**：
- 四要点的规制工具（平台自动加标、限流、封禁）是**内容发布平台**的账号治理机制，PI 转述语境亦为「平台内容产出」（coze 提醒原文「后续如果还有其他平台的内容产出，记得按新规主动标识」）。arXiv 是学术预印本库，无自动加标/限流机制，其 AI 相关要求在投稿政策层（deposon 线上声明即引 "arXiv's authorship and AI-use policy"）。
- 两场景的交集是**内容透明度本体**：论文正文的 AI 披露在两侧都构成合规基础——FTFB 这一面已满足（如上映射）。
- **新规是否及如何在 arXiv 投稿场景延伸适用，属规则适用解释，超出本员（文献调研）评估权限，不代裁**——呈报事实（正文已主动披露、元数据与 deposon 先例同形态）供 PI 结合平台通知原文判断。若 PI 的关切点是「未来在其他内容平台传播论文/成果」的场景，则按新规主动标识的动作发生在那些平台的发布行为上，与 arXiv 投稿件本身无涉。

---

## 四、线上版态确认（任务 4）

按时间序的盘面证据链（全部有群史/交付件支撑）：

| 时点 | 事件 | 证据 |
|---|---|---|
| 09-18 00:40 | v4 上传版打包（摘要 2,216 字符超 arXiv 1,920 上限，被阻塞） | 目录＋metadata 警告行 |
| 09-18 00:53–01:25 | arXiv 终版（摘要压缩至 1,849 合规）→门审 PASS→管理员发群 tar.gz（845dbe8555be）「可直接提交 arXiv」 | 群史 09-18 01:25 |
| 09-18 12:03–16:35 | KIMI 外审驱动三轮：v5（深度修订）→v6（验收返修）→R3（排版重打包） | 三个交付目录＋群史 |
| **09-18 17:49** | **PI：「仅剩余一小问题，KIMI已自行修改，我已提交」→ 第一次实际投稿（原投）** | 群史 09-18 17:49；管理员 18:16「FTFB 已随 KIMI 自改完成提交」 |
| 09-27 00:51 | PI：「ftfb提交但被标on hold」（原投 on hold，无公开 ID） | 群史 09-27 00:51 |
| 09-27 01:23–03:17 | PI「初稿完成后请更新ftfb，以解决on hold」→ R4 交付链（查理 tex→鲍勃验收【通过】→戴夫编译 25 页） | 三个交付目录＋验收报告 |
| **09-28 16:09** | **PI：「FTFB已重投」→ 第二次实际投稿（重投）** | 群史 09-28 16:09 |
| 09-28 16:41 | 管理员请求确认「提交包是否即 R4 终版（25 页 PDF）」——**未获 PI 答复** | 群史 09-28 16:41 |
| 09-29 11:50 | PI：「理论综述类on hold卡太久了，还重投了一次」 | 群史 09-29 |
| 09-29 12:00 | arXiv 三组题名查询无公开件（上轮预案复查） | 阿兰_FTFB未公开情景引用预案_2026-09-29 |
| 10-08 14:05 | 本轮复查：web_search 两组查询（严格+宽松）**均无 FTFB 公开件** | 本报告 §六检索记录 |

**版态判定**：
1. **原投（09-18）**：基线为 R3 排版重打包版＋KIMI 自行修改；**KIMI 自改后的成品与实际提交包指纹均未在本群留档**（PI 自行操作），实际提交版本不可从盘面确证——**待 PI 确认**。
2. **重投（09-28 PI 通报）**：具体提交包未确认（管理员当日即问「是否即 R4 终版」至今未获答复）——**待 PI 确认**。若提交的即 R4 终版，则线上最新版=R4（tex 4f8c4231/PDF 0b0d9495）；若为其他包，以 PI 回指为准。
3. **公开状态**：截至今日 14:05 无公开件（on hold 持续状态与 09-29 判定一致）。
4. **R4 提交挂起态登记**：管理员 10-08 台账口径「R4 已验收通过但提交挂起（P6/P7 待 PI 输入）」——P6/P7 出自鲍勃 09-27 验收报告 §五 pending 表（P6=提交版待输入、P7=hold 意见待输入）。该口径与 09-28「已重投」通报的关系如实登记为：**重投动作已发生（PI 通报在案），但「重投版=R4」的确认链未闭环（P6 未销）**，故台账维持挂起态；两口径不矛盾，是确认颗粒度差异。

---

## 五、判定与更新范围（任务 5）

### 5.1 判定

**总判定：待 PI 裁（硬合规层面无需更新）。** 依据：
- a) 正文主动标注（新规要点 2）：v4 起全线在位，不存在「未标注」状态——**无需更新**；
- b) 创作思考主体口径（要点 1）：对应句齐备且粒度到数字层——**无需更新**；
- c) Comments 元数据面：与 deposon 线上先例**同形态**（均无 AI 标注语）——**无缺口，无需更新**；
- d) 科研助理记名面：GLM 具名在位，与 deposon KIMI-K3 具名等价——**不缺位**；
- e) 唯二剩余差异为**形态/措辞层**（独立小节 vs 加粗段；直白否定句有无），属增强对齐可选项，是否值得动稿件属 PI 权限——**待 PI 裁**。

### 5.2 若 PI 选做增强对齐，更新范围如下

**增强项 A（升格独立小节）**：R4 tex L480 的 `\textbf{AI disclosure.}` 改为 `\section*{AI use disclosure}`（或带编号，沿 deposon 线上版小节名），段落文字不动。
**增强项 B（补直白否定句）**：披露段内增一句（建议位置：作者全责句后）："No content was generated by the AI without human review."——与 deposon 线上版同款、直接对应新规要点 1 表述。

**影响面（A/B 任一或并做）**：
1. 改动面：查理 R4 tex 1–2 行（L480 段内/段头）；
2. 重编重打包：戴夫 pdflatex 三遍四零复检＋PDF 重出（页数可能 25→25 或 26，需实测登记）＋R4 尚无 tar.gz（09-27 编译交付未打包，重投轮本就需补打包步骤）＋指纹链全刷新；
3. 联动换锚：第三作 App A 的 FTFB R4 两行锚（tex 101,928/4F8C42319603＋PDF 411,782/0B0D9495508F）需同步更新——涉及第三作联动换锚清单 S 系流程；
4. 验收面：鲍勃差量验收一轮（diff 清单外零改动复核）；
5. 元数据面：Comments 字段建议同步加一句 AI 标注语（如 "AI-assisted drafting disclosed in Section AI use disclosure"）**仅当 PI 同时要求元数据层标注时**——deposon 先例未这样做，非对齐必需。

**不动对照项**：
- 已投线上版本（09-18 原投、09-28 重投）：arXiv 侧已不可改，任何更新只能走下一 replace/重投轮；
- FTFB 各版正文披露段既有文字（除 A/B 触点外零改动）；
- verdict 句、五锚、数字锚、引用池 56 条（冻结纪律面）；
- deposon 线上版（已公开，任何情形不动）；
- arXiv 元数据其余字段（Title/Authors/Subjects/License 均不受影响）。

**触发时机建议**：绑定 R4 解除挂起的下一次 replace/重投轮（P6/P7 闭环时）一并执行——理由：R4 本就缺 tar.gz 打包步骤，合并执行避免单独开轮；且 on hold 件在 arXiv 侧以 replace 更新最顺。

---

## 六、指纹登记（本报告全部实测，sha256sum/stat 本机重测）

**FTFB 各版（tex / tar.gz / 关键件）**：

| 版本 | tex SHA-256（前 12 位） | tex 字节 | tar.gz SHA-256（前 12 位） |
|---|---|---|---|
| v4 上传版 09-18 | 1e447164acc5 | 102,920 | d122b737c823 (36,765 B) |
| arXiv 终版 09-18 | 9de366a6c4d6 | 102,549 | 845dbe8555be (36,701 B) |
| v5 深度修订 09-18 | cb616abf575c | 97,965 | aab3243303e1 |
| v6 验收返修 09-18 | ec3e1a15d905 | 98,990 | fbb7bec73344 |
| R3 排版重打包 09-18 | 51f4e0c8a0f8 | 98,972 | 741c9f24b447 (444,555 B) |
| R4 备投 09-27 | 4f8c42319603 | 101,928 | （无 tar.gz；PDF 0b0d9495508f·411,782 B；arxiv_metadata.txt 0e07c7041a71） |

**deposon 先例**：round4 本地包 cn 0e652f21cbc0 / en fd6eafe2014a（与查理简报登记一致）；线上 arXiv:2609.09001v1（2026-10-08 14:05 实测：摘要页+HTML 全文抓取存私有区留档）。

**本报告**：shared/阿兰_FTFB_AIGC标识合规评估_2026-10-08.md，指纹落盘后补记于群内通报。

**检索记录**：FTFB 公开状态复查两组查询（2026-10-08 14:0x，web_search）：①`arxiv.org "Fiction That Feeds Back" Qihao Yuan`（422 无结果）；②`"Fiction That Feeds Back" arXiv non-Euclidean geometry machine worldviews`（返回均为无关第三方文献）——均未检出 FTFB 公开件。

---

## 七、待 PI 确认清单（0 编造纪律下不可确证项）

1. **原投提交包（09-18）**：R3＋KIMI 自改的成品指纹——群内未留档，请 PI 回指（或指认 KIMI 侧留档位置）；
2. **重投提交包（09-28）**：是否即 R4 终版（tex 4f8c4231 / PDF 0b0d9495·25 页）——管理员 09-28 16:41 之问延续至今，一并答复即闭环 P6；
3. **P7（hold 意见）**：arXiv on hold 的意见内容（若有回函/邮件，供团队定位修订方向）；
4. **「科研助理署名」的所指**：本报告按「AI 于正文披露内具名记名」口径评估（两文等价在位）；若 PI 另有所指（如 arXiv 表单侧协作署名、平台账号侧助理身份标注），请补充说明，盘面无载；
5. **deposon 实际提交版的本地对应件**：线上 v1 与 round4 本地包存在三处实质差异（§2.2），实际提交版本地件位置请 PI 指认（不影响本报告对齐结论——对齐基准已取线上实测）。

---

## 八、老实交代（核验边界）

- arXiv 线上抓取为单时点快照（2026-10-08 14:05），页面内容以抓取时为准；若 arXiv 侧后续更新（如 on hold 解除、版本更替），以 arXiv 实时页面为准。
- FTFB 原投/重投的实际提交动作均为 PI 在 arXiv 侧自行操作，本组工作区无提交回执，「实际提交了哪个包」只能依赖 PI 通报与确认（§七 1/2），本报告不推定。
- deposon 线上版与 round4 本地包的差异系 arXiv HTML 全文抓取比对所得；HTML 渲染与 PDF 版式存在细节差异的可能（如 \thanks 注的呈现位置），但三处实质差异（小节名/KIMI-K3/否定句）在正文层面不受版式影响。
- 平台 AI 标识新规的原始通知文本未在盘面（仅有 PI 转述四要点），本评估以转述内容为映射基准；新规原文的适用范围条款（是否含学术预印本场景）待 PI 提供后可复核。
- 本报告只评估不改稿：未触碰任何 FTFB/deposon 文件（含 repos 克隆），全部核验在只读副本/私有区完成。

—— 阿兰-文献调研员 ｜ 2026-10-08 13:57 接单，14:1x 落盘 ｜ AI 生成
