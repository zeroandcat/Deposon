# 双主线融合范本拆解与 v0.5 诊断（2026-09-29）

撰写：查理-论文主笔。派单：群管理员 2026-09-29。本轮只诊断与方向，不重写稿件。锚记：**一作**＝`repos/Deposon/paper/deposon_paper_final_en.md`（L**）；**F**＝FTFB R4 `fiction_that_feeds_back.tex`（L**）；**v0.5**＝`shared/_v3v4_merged_paper_2026_09_27_v0.5.md`（L**）。两范本对象只读零改动。

## 一、范本手法拆解

**第一作（v1 脑图主线×v2 博弈论解释主线）——手法：同一对象、两个问法**

1. **标题一体定语**：标题把两线写成同一名词短语（"Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer"，一作 L4），非「A × B」并列拼接。对照 v0.5 标题「Walking with the Verdicts, Keeping the Books: …Coordinate System and a …Program That Formally Failed」为双动宾并列。
2. **交接句在对象层**：§3 开篇一句话把 §2 的账本变成 §3 的研究对象：「The conservation ledger of §2 is verified only statically… does not answer the dynamical question—does the reverse evolution…possess a scalar?」（一作 L73）。主线的交接不靠分区标题，靠「同一张图、同一本账，换一个问题」。
3. **概念共生（一词双语义）**：dissipation 在物理层是不可逆凝聚，在博弈层被赋予「endogenous commitment device——no player can undo an elimination by rewriting the books」（一作 L79）；守恒账升级为「scalar ledger」（L79）；Dirichlet α 的「temperature acquires game-theoretic semantics」（L139）。明说的融合宣言：「two successive tightenings of the same entity」（L18）。
4. **博弈数字长在图上**：博弈四元组全部取自散射层既有对象——玩家＝留一预测边、策略＝候选节点、效用＝场分、Φ=−E（一作 L75）；ECR 的分子分母就是散射层两个 arm（L91）。判死线（P1a 0.8569 / P1b −1.0 / T-P1c）杀的恰是「两线之间的桥」本身（L107）——负结果也发生在融合层，不在博弈专属区。
5. **一套证据语言贯穿两线**：closed/consistency/motivation 三档同用于 E9.x 与 GT-x（一作 L29、L73「never blend tiers」）；§4 把两线的负结果按性质统一处置（L149–151）；结论以「one empty layer…along two equally weighted lines」（L163）收束——问题单一，两线是解法的两面。

**FTFB（历史主线×判定主线）——手法：判据作为贯穿镜头，吃掉所有素材**

6. **方法加工数据**：T/D/R 三查在 §2–§5 每个历史通道上反复施用（F L253 各通道逐条 Pass/Indeterminate）；判定主线是镜头，历史主线是胶片，不存在「历史区×判定区」。
7. **映射表=概念翻译器**：§6 mapping table 把硬科幻纪律逐行译成 AI 判定纪律（F L268 起）；§6.3 四段流水线（S/F/P/E）与 §7「The chain, replayed end to end」（F L323）把 deposon 数字重演为流水线产出——数字被叙事消化，不是被引用。
8. **自反闭环**：§9 用论文自己的判据给自己的案例打分（F L441–447 主表）——「A paper that lives by criteria should be willing to die by them」，方法最终吃掉实例，两线再不可分。
9. **素材身份主动抹除**：§7 工程实例匿名（F L603 [R56] withheld）——融合后素材不再携带来源标签；范本正文表面零「我来自另一篇文档」注记。

## 二、v0.5 缝合诊断（三区制在五个维度是缝合而非融合）

1. **分区标记断裂（结构）**：Paper scope 自称三区（v0.5 L5「Part III (Sections 17–24, the synthesis zone)」），但正文只落地两区标记——L75 `# Part I · …`、L288 `# Part II · …` 各带斜体来源注记（L77、L290），**§17 起无 `# Part III` 标题、无来源注记、连 `---` 分隔线也缺**（L488 边界注记直接跳 L490 `## 17`）。合题区寄生在 Part II 尾部，读者在正文里找不到 Part III 起点：蓝图三区制执行不完整。
2. **表面来源标签（结构）**：Part I/II 开头的斜体 Provenance 注记把素材身份暴露在正文表面；App C 自述其功能即「让读者查明每句话是 survey 材料、V4 材料还是合并合成材料」（L952）。可审计纪律与无痕融合的价值冲突直接落在正文表面。
3. **摘要三段拼接（结构）**：摘要以「The first is…/The second is…/The synthesis maps…」（L16）陈列双主线，是两篇摘要＋一句缝合句，非单流叙事。
4. **编号体系多源并存（编号）**：①引用统一序列需要三处修补性说明向读者解释（L10 conventions、L684 References note、L997 C.2）；②双 L 系统并存——survey 五线 L1–L5 vs 程序内部 verdict ladder L1–L3，需 §17.2 专门一段「Two numbering disciplines guard the mapping」（L508）＋C.4 声明不混写；③K-N26-*/K-N11-*、TH-v2-*、E-1..E-37、T1/T1.5r2、V1–V4、G1、GLM_2 等编号族全部原样迁移，读者须同持六套以上编号地图。冻结纪律（v1.1 字面迁移）是根因，编号无法统一重设计。
5. **文体断层（文体）**：Part I 是 survey 体（X.1 机制/X.2 证据/X.3 矩阵行固定模板，表格收尾，「not located in the verified base」口癖，全文几乎无 SHA-12 锚）；Part II 是 verdict 叙事体（path/bytes/SHA-12 三元组高密度句式＋字面 verdict＋勘误链叙事）。两区节奏迥异。
6. **概念体系声明并存而非融合（文体）**：§16.2 明说两个 tier 系统「related but not identical in semantics…deliberately not merged into a single definition」（L482）——纪律正确，但暴露双源概念没有融合，只是声明共存。范本一作是单一 tier 系统贯穿两线（对照手法 5）。
7. **两区关系单向（关系）**：Part I 全文对 Part II 零感知（survey 写作时 V4 链不存在），互引仅 Part II→Part I 单向回指；Part I 收束于 §8.3 表格后无任何过渡即被 `# Part II` 切断（L283–290）。对照一作 §2↔§3 密集互引（手法 2）。
8. **合题区复读化（合题）**：冻结纪律下合题区被禁做新主张——「the mapping adds no fact beyond Part II's records」（L521）、R7「adds no measurement」（L1007）、§18.2「adds no numbers and restates no verdicts」（L579）；§19 四条教训全部是「survey 段＋*V4 anchor* 段」固定二段式（L591–605）；§17.1 开场是解释合并的元层语句「The two closures meet in one observation and one fact」（L494）。约 190 行合题区中，新写作集中于「复述＋填表＋纪律声明」。
9. **缝合工作集中成区（合题）**：C.1 表显示 new composition/rewritten 几乎全部落在 §17、§18.2、§20.3、§24（L977–987），融合不是弥散在全文，而是尾部集中处理；§21 之 (8)(9)、§22.4–22.5、§23 披露段、§24 首句「This paper merged two lines」（L674）全为 merge 特有器官。范本的融合发生在每个素材点上（手法 6–8）。
10. **元层主张占据结论**：结论第一主张是「合并」本身（L674），而非一个研究问题的答案；对照一作「one empty layer, two lines」（手法 5）。

诊断结论：v0.5 是**对象层陈列**（两源各自完整＋映射桥），范本是**对象层消化**（概念互译、数字长在对方结构上、单一证据语言）。冻结纪律并不禁止后者——一作/FTFB 同样冻结数字——它约束的只是数字与字面，不要求「来源标签＋集中合题」的缝合形态。

## 三、初步重设计候选骨架（硬前提：F 系冻结数字与 verdict 字面不动、O 系零收束、双盲与保密纪律不变）

**候选 B「对称三区＋去表面标签」（最小手术，v0.6 级）**：①补 `# Part III · The Synthesis` 分区标记与 `---`（与 L75/L288 对称）；②两处斜体 Provenance 注记降格为 App C 登记项，正文表面去来源标签；③Part I 尾增前瞻合页（⑤ 列之空预告 Part II 之填，把 §17.1 的回望改成双向）；④摘要改单流叙事；⑤§17.1 元层开场改对象层开场。**复用度极高**：v0.1–v0.5 全部审读/验证成果（锚表、引用统一、双盲卫生、五族频次核验、C.0.x 注册链）原样保留，仅新增约 10–15 位点；8-gram 需按新基线重测。**量级：小。局限：治标**——Part I 零感知、合题集中、文体断层仍在，得到的是「整齐的缝合」而非融合。

**候选 A「单流重叙」（一作式，v1.0 级）**：弃三区，改「一个空层、两个问法」：引言从「reasoning claim 缺 run-level 判定协议」出发；五线压缩为文献测绘；V4 六块拆到对应线后紧随（L3 线后接 Task B FAIL、L2 线后接 N-26/GLM_2），「文献行×程序行」在每线内互文；Table 4/5 前移为贯穿工作台；§18 案例对等、§19 教训拆散重安；App A/引用编号/双盲成果全复用；C.1 需按新 provenance 重写。**量级：大**（Part I 压缩重写、Part II 重排、合题拆散；survey 唯一公开载体地位 R2 需 PI 重裁——压缩即不再全量承载；Part I 字节级成果失效）。**收益：唯一达到范本「对象层消化」标准的骨架。**

**候选 C「判据贯穿」（FTFB 式，备选）**：把五线六格从「被展示的坐标系」改为「加工所有素材的判据装置」：V4 六块被五线判据逐格检查、打 tier、留边界声明，矩阵前移为全篇节奏。**复用度中高**（F 系/App A/引用/双盲全保留，Table 4/5 内容大半重排）。**量级：中。主要风险**：V4 链的时序叙事被格子切断，六块的链条感与 O 系「开放相位」的整体呈现可能受损；v1.1 的链叙事是按程序时序组织的，拆散需爱丽丝轮先确认实验叙事安全。

**推荐**：B 先行（低成本恢复三区对称与正文洁净，可即时并入下一轮注册）；A 作为投稿级融合的候选主骨架，R2 载体裁量留 PI；C 挂起待爱丽丝轮链叙事评估。三个候选均不触碰 F 系数字、verdict 字面、O 系开放表述与保密纪律。

## 边界与移交

凝子定义与 FTFB 内容要义归阿兰轮，实验设计对表归爱丽丝轮——本件只取公开件；C 候选的链叙事安全项已标注移交爱丽丝。字数申报（双口径）：中文正文 1,929 字；连英文术语与行号锚记合计约 3,100 字符——锚记密度源自派单「逐条给出处位置」的要求，英文为两范本/v0.5 原文术语，未转写以免失锚。

（查理 2026-09-29）
