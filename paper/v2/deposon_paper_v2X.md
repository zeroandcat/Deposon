# 结构还是语义？物理场信号与 LLM 先验在概念图补全上的价值域划界

**Structure or Semantics? Mapping the Domains of Physical-Field and LLM-Prior Signals for Concept-Map Completion**

> v2.X 论文中文初稿（2026-08-30）。体裁声明：boundary analysis / division-of-labor 划界研究。
> 本稿是独立新稿，引用 1.X 论文（deposon_paper_v1.md / _en.md，冻结于 v1.9 状态）作为前序工作。
> 全部实验判定为预登记后的机械规则求值；所有数字可追溯至 `results/` 下冻结 JSON 的具体字段
> （逐字段出处见附录 A 与文末成稿修订记录）。

## 摘要

脑图/概念图补全位于教育知识工程与大模型推理审计的交叉地带：给定一张残缺概念图，
判断缺失边应指向何处。现有工作或依赖结构启发式，或依赖 LLM 语义先验，二者的价值域
从未被系统划界。本文以预登记判死刑则（kill criteria 先于数据冻结）对比两类极端信号：
物理约束散射层的均值场反向（场，纯结构信号）与 labels-only LLM 先验（纯语义信号），
在三大规律设计的 22 图语料（结构否定族 S×16 + 真实语义族 L×6，以最终语料快照 sha 为准）
上以全候选排序协议实测。结果：① 场对 random 的预登记析取斩杀线 **H-A1 判死**
（冻结 JSON `H_A_dead.triggered=true`；22 图口径 p=0.0118、Holm 过，但反转图达 4 张且
全部位于语义/低枢纽图——斩杀线触发本身即分工边界的直接证据）；存活表述收缩为
「field_mean > degree 跨口径稳健」（22 图 p=4.0e-5）与高 hub 图局部优势（S6 族
named Hits@3 0.471）；枢纽集中度是场效力的主导预测子（OLS β=+2.12，p=0.00028，
n=20，**探索性** v0）。② 先验在真实语义图上碾压全部臂（named Hits@3 0.484–1.000）；
可比口径为 CoT 92.5%（带选项文本的 4 选 1）vs 先验开放 top-1 67.5% / top-3 82.5%——
题库轨 92.5% 系陷阱选项非图节点导致的 2 选 1 退化口径，「先验=CoT」宣称已按修正案
C2 正式撤回。③ 融合在所测 λ 档上均不增（稀释效应）。④ 自适应攻击者 100% 绕过关键词
规则基线，两条证据轨判定不同：预登记主 LOO 协议为 **no_separation**（rule_filter
−7.5pp，未达 20pp 阈值，如实归档）；题库轨 rule_filter=27.5%≈机会水平（25%）。
场对语义陷阱机制性免疫（不读标签，注入下 −0.0pp）。⑤ 噪声反向动态相对确定性极限
的收敛差（gap 0.30，20/20）与势博弈解读**一致**（consistent with a potential-game
reading；一致性证据而非证明），全语料势轨迹单调性 22/22（GT-5b）、非势残余中位数
≈1.6e-29（GT-6，3 图例外如实披露）。结论：结构场与语义先验的价值域正交互补，
我们给出两特征领域鉴定器 v0（hub_concentration, real_semantics；hub 轴已在 2 对语料外
新图上预登记复现，GT-8 2/2 同向）与全套可复现预登记工件。GT-3b 跨厂商检验完成
（doubao 4/4、deepseek 6/6、三族 0 败绩、全 ok 域 Kendall W=1.0），「同源污染
artifact」假说被实质性削弱（残余局限：三族均为中文优化大模型）。

**关键词**：概念图补全；边界分析；势博弈；预登记；阴性结果；领域鉴定器；自适应攻击

## 1 引言

### 1.1 问题：两类信号，一个未被划分的价值域

概念图补全（给定部分概念图，预测缺失关联的目标节点）同时暴露给两类截然不同的信号。
其一是**结构信号**：图拓扑本身携带的汇聚、层级与路径信息，可被共同邻居、度、PageRank
等经典启发式利用，也可被本文的物理约束散射层（场）利用。其二是**语义信号**：节点
标签文本携带的领域知识，可被 LLM 先验直接读取。两条研究线各自积累，却很少有工作
回答一个更基础的问题：**各自的价值域在哪里、边界由什么决定？** 不划界的后果是
双向的过度宣称——结构方法在语义图上虚报，语义方法在结构任务上错配。

### 1.2 与前序工作（1.X）的关系：否定之否定作为方法论

1.X 论文建立了散射层框架与基准纪律，并在整改中证明：基准效应量结构性不可归因、
规则基线可追平管线（v1.9）。v2.X 把这些阴性结果转化为研究问题本身——信号的价值域
在哪里？1.X 为正题，v1.9 的整改为反题，本稿的分工与边界为合题。本文不重复 1.X 的
框架细节，只继承其全候选排序协议（E9.2 口径）、预登记纪律与缓存幂等工程。

### 1.3 贡献

1. **划界实证**：在 22 图语料（族 S 结构否定 ×16 + 族 L 真实语义 ×6）上，以同一
   全候选协议对比两类极端信号，给出「场管结构、先验管语义」的跨图证据，并把
   斩杀线触发（H-A1 判死，4 张反转图全部分布于语义/低枢纽图）本身用作边界证据。
2. **领域鉴定器 v0**：两特征规则（hub_concentration、real_semantics），OLS 探索性
   证据（hub β=+2.12，p=0.00028，n=20）+ 语料外 2 对新图预登记复现（GT-8，
   2/2 对同向），并如实披露 degree 基线在高 hub 图饱和的边界。
3. **博弈论一致性解释**：散射层反向动态与势博弈解读一致的六条证据链（GT-1 收敛差、
   GT-5/5b 势轨迹单调 22/22、GT-6 非势残余中位口径完备、GT-7 温度-探索语义、
   GT-4 分布级 PoA 报告、GT-2/GT-3b 边界），全部为一致性证据而非形式化证明。
4. **方法论工件**：预登记 SPEC 与修正案、独立多角色评审（M1–M5/m1–m7 闭合记录）、
   版本化 verifier、基线注册表（含 BOSS 门槛）、缓存 provenance，全部随稿发布。

## 2 相关工作

> 本节整体沿用 `paper/v2/related_work_v2X.md`（文献锚点经 scholar + web_search 交叉核验，
> 来源 reviews/literature_scan_v2X_A.md 40 条与 _B.md 40 条），仅作衔接性微调。

### 2.1 结构驱动的链接预测

经典结构启发式构成我们基线注册表的 A 族：共同邻居、Adamic-Adar、Jaccard、
Preferential Attachment、Katz 与 Personalized PageRank——本文在 20 张图上对全部六臂
做了同协议实测（外加 degree 与 random），并补入一臂纯 numpy 浅近似 Node2Vec
（如实标注非完整实现）。可训练的 KGE 系列（TransE/ComplEx/RotatE）在 20 图规模
方可训练，列为 v2.1 排期项（注册表 ⬜，不回避）。词法余弦（字符 n-gram TF-IDF）这类
常被忽视的零成本基线在 5/20 张图上击败了我们的主臂，此类「潜伏 BOSS」正是注册表
机制要制度性防止的（披露规则见 §4.4）。

### 2.2 LLM 语义先验与方向语义

LLM 用于知识图谱补全的近三年证据链给出我们数字的横向坐标：KICGPT
（Findings of EMNLP 2023）以检索+LLM 重排超过纯 LLM；KG-LLM/Yao et al.
（ICASSP 2025）显示零样本 GPT-4 弱于微调 6-7B 模型；Wadhwa et al.（ACL 2023）
表明即使精心 prompt，GPT-3 也仅接近全监督关系抽取。我们 labels-only 先验在真实
语义图上的 named Hits@3（0.484–1.000）高于上述零样本区间，但须声明两点降级：
其一按 GT-3b 后口径更新——跨厂商检验已完成，E3 doubao（ByteDance）4/4、
E4 deepseek（DeepSeek）6/6，三模型族合计 0 域先验 ≤ 场（0 败绩）、全 ok 域
Kendall W=1.0（docs/Findings_GT3.md），「同源污染 artifact」假说被实质性削弱但
**未排除**（残余局限：三族均为中文优化大模型，训练语料可能共享公开中文知识）；
其二：图为 30–45 节点的小规模 DAG。

方向语义上，Reversal Curse（Berglund et al., ICLR 2024）及其机制解释
（Wang & Sun, ICLR 2026）预言 LLM 对「A→B 成立」无法推出「B→A」，而我们实测
先验边与金边的方向一致率 ≥0.96、hub 反向边为 0（四图）——与反转诅咒形成对照
（§4.7），同时标注 v1.9 锚点图上曾观测到系统性方向反转（占位标签特异现象），
两种现象并存恰说明方向表现的条件性。MKGL（NeurIPS 2024）关于标签文本自带结构
信号的「三词语言」论证，与我们的 n-gram 词法基线获胜现象互相印证。Zhang et al.
（ACL 2025）对 KGC prompt 结论泛化性的系统复测提醒我们：prompt 相关结论的泛化面
按 GT-3b 后口径标注——已扩展至三个模型族，但三族均为中文优化大模型，非中文模型族
的检验仍为开放局限。

### 2.3 概念图与脑图：任务与评估

概念图由 Novak & Cañas（2008）定义并奠基。Ruiz-Primo & Shavelson（1996）指出概念图
评估的「任务-评分依赖」——得分对协议高度敏感，这与我们 v1.9 对负采样协议的批判
构成跨三十年的同一教训。基准方面，KnowEdu（IEEE Access 2018）与
MOOCCube/MOOCCubeX（ACL 2020 / CIKM 2021）提供教育知识图谱参照。**必须显式承认**：
KitBuild「补全式概念图」（Pinandito et al., 2021）在任务形式上与我们一致，
LLM 侧同体裁近作见 Ma & Chen（LAK 2025）；我们与该线的区别在于：不补全人工课程图，
而是用受控语料（结构否定族 + LLM 生成族）系统扫描信号价值域，且全部判定预登记。

### 2.4 博弈论透镜：势博弈、网络形成与 PoA

把补全建模为博弈有四个理论锚点。Monderer & Shapley（GEB 1996）的势博弈框架与
Rosenthal（1973）拥塞博弈给出势函数存在性的经典条件；Sandholm（2010）的群体最好
响应流证明确定性最好响应动态在群体极限下沿势函数梯度上升——这是我们把
「mean-field 确定性反向 = 无噪声最好响应动态」作为理论解读的最近支点，GT-1 的实测
收敛差（gap 0.30，20/20）与其一致。Candogan et al.（MOR 2011）的博弈流分解与
Parise & Ozdaglar（Econometrica 2023）的 graphon 连续极限，分别提供「场=图流分量」
与「大图极限」的进一步形式化路径——我们**尚未发现**该理论交集与扩散生成模型文献
之间的相互引用，此潜在交叉空位是本文理论叙事的动机之一（阴性文献宣称口径，见 §7）。
网络形成与攻防方向上，Jackson & Wolinsky（1996）、Fabrikant et al.（2003）奠基，
Ma et al.（TCS 2014）与 Waniek et al.（2018/2023）最接近对抗性边操作场景；我们与
adversarial robustness 赛道显式划界：攻击者不是扰动输入以翻转模型输出，而是在规则
已知下生成语义陷阱（§2.5）。PoA 方面，Koutsoupias & Papadimitriou（1999）与
Roughgarden & Tardos（2002）的仿射拥塞 PoA=4/3 界是经典锚点。我们的实证是
**分布级 PoA 报告**（应用文献稀少）：median PoA=1.5（族 S 13 张有限值图）。
必须如实声明：操作化 PoA=field_mean/max(自利臂) 与经典 worst-case-NE/社会最优比值是
**不同度量**，成本结构是否仿射/可分的前提未闭合，故数值上与 Pigou 4/3 的对齐仅为
**巧合性对齐，不主张「实例级复现」**；且族 L 真实语义图中 2 张 PoA<1（0.5、0.75）
并列披露，构成该叙事自带的边界证据。

### 2.5 机制设计、审计与自适应攻击

机制设计侧，Conitzer & Sandholm（2006）、Dekel et al.（2010）、Hardt et al.（2016）
与 Dütting et al.（WWW 2024）构成上下文；审计侧 Raji et al.（2020）给出组织层算法
审计框架，Jia et al.（2021）的 Proof-of-Learning 给出密码层可验证计算。我们的守恒账
定位为**运行期逐实例不变量**（事后溯源与密码证明之间的空层），写作时与 PoL 显式划界。
自适应攻击侧，Tramèr et al.（NeurIPS 2020）与 Nasr et al.（USENIX Sec 2026）提供
方法学合法性；规则防线的失效有五条独立证据链（Gröndahl et al. 2018；Hosseini et al.
2017；Kahu & Ahuja 2025；Jain et al. 2023；HateBench, USENIX Sec 2025）。我们的
GT-2 结果按**双轨口径**如实并述：预登记主 LOO 协议的机械判定为 **no_separation**
（rule_filter −7.5pp，未达 20pp 阈值）；题库轨 rule_filter=27.5%≈机会水平（25%）。
故「规则防线失效」目前仅在题库轨成立，与上述五条证据链方向一致但强度未定；
GT-2 多陷阱升级（GT-2B）已执行并判 inconclusive（§4.4），不升级为方法学主张。

### 2.6 边界分析与阴性结果体裁

本文体裁自我声明为 boundary analysis，先例三层齐备：宣言层 Lipton & Steinhardt
（CACM 2019）与 Dodge et al.（EMNLP 2019）；顶会实证模板层 Recht（ICML 2019）、
Tevet & Berant（EACL 2021）、D'Amour et al.（JMLR 2022）、Lazaridou et al.
（NeurIPS 2021）、Schaeffer et al.（NeurIPS 2023）、Mallen et al.（ACL 2023）、
Dziri et al.（NeurIPS 2023）；专门 outlet 层 Insights from Negative Results workshop
（已办六届）。Bowman（ACL 2022）「The Dangers of Underclaiming」是我们诚实降级的
自我设防参照：所有否定性主张（融合稀释、场边界、规则失效）均以预登记判死刑则和
机械判定为限，不超出数据。

## 3 方法

### 3.1 场：物理约束散射层的均值场反向

散射层沿用 1.X 框架：在图上定义能量 E（含散射强度、平滑项与先验项），反向过程
以退火调度（β 线性、50 步、lr=0.1、λ_smooth=0.01、uniform_out 先验）把能量梯度
转化为候选目标的排序信号。**均值场反向**（field_mean）是取 Dirichlet 起点分布均值
的确定性极限——全程无采样噪声；对照臂 **dirichlet 噪声反向**在起点引入采样（浓度
参数 α 为等效温度）。场不读节点标签文本，只读拓扑：这是它与一切语义臂的机制性分界，
也是它对语义陷阱免疫的来源（§4.4）。配置字段冻结于各结果 JSON 的 `config` 节。

### 3.2 先验：labels-only LLM 先验

先验臂以零样本 prompt 让 LLM 仅凭节点标签文本预测每条 named 边的目标节点
（开放候选，非选项制），输出 top-k 候选；全部调用经内容寻址缓存
（prompt_sha256 在案），预算预登记且 attempts 全落盘。族 S 标签与结构脱钩（合成
占位标签），先验在其上无意义，故先验臂只在族 L 主报（预登记口径）。

### 3.3 全候选排序协议

沿用 1.X E9.2 口径：对每张图的全部 named 边做留一（leave-one-out）任务化，每任务
以全部图节点为候选排序，指标为 named/filler Hits@3。所有臂（场、random、degree、
共同邻居、Adamic-Adar、Jaccard、Katz、PPR、Node2Vec 浅近似、ngram_tfidf、
rule_filter、llm_prior、hybrid）跑同一协议；random 与场实例均种子化
（rng=g_seed·100003+ei）。

### 3.4 语料：三大规律设计的 22 图

- **族 S（结构否定族，16 张）**：S1 单链、S2 平衡树、S3 多 hub、S4 跨链 DAG、
  S5 无枢纽随机 DAG、S6 辐条汇聚，含 S1/S2/S6 的 N∈{20,35,45,60} 尺寸扫描档；
  标签为合成占位符（real_semantics=0），用于否定「场=通用骨架检测器」的强主张。
- **族 L（真实语义族，6 张）**：biological_taxonomy、historical_causality、
  algorithm_process、physics_concepts、geography_world、project_management，
  由 LLM 生成，按方向语义配对（抽象→具体 ×3 / 过程→结果 ×3），30–45 节点。
- 语料快照以 index sha256 钉定；20→22 图的快照漂移已归档（corrections E1）。

### 3.5 预登记与统计

全部假设与判死刑则先于数据写入 SPEC（v2.0 及修正案 1、SPEC_GT2B、SPEC_GT3、
SPEC_GT8）；判定由脚本从结果 JSON 机械读取，禁止手写（corrections C1 教训制度化）。
多重性控制用 Holm（m=4，α=0.05）；配对比较用符号检验，另以 Wilcoxon/配对 t 作
第二意见复核（skills §一：field>random Wilcoxon p=0.0031，|r|=0.83；field>degree
配对 t p<0.0001，Cohen's d=2.05）。

## 4 实验

### 4.1 场 vs 结构基线：H-A1 判死与存活表述

22 图口径（results/deposon_v20_corpus_eval.json）：

- **H-A1（field_mean > random）**：符号检验 16+/4−/2 平，p=0.0118，Holm 过——
  但预登记斩杀线为析取规则（不显著 **或** ≥3 张图反转），反转图达 4 张
  （L_historical_causality、L_physics_concepts、L_project_management、S2_n45），
  故 `H_A_dead.triggered=true`，**H-A 头条主张正式判死**（corrections C1）。
  反转图全部位于语义/低枢纽图——斩杀线触发本身就是分工边界的直接证据，
  与 H-B1 违规图、PoA<1 图同构。
- **存活表述①**：H-A2（field_mean > degree）跨口径稳健：22 图 19+/1−/2 平，
  p=4.0e-5，Holm 过；20 图子集经 Wilcoxon/配对 t 复核大效应（§3.5）。
- **存活表述②**：高 hub 结构图的局部优势——S6 族 named Hits@3 = 0.471，
  逐位复现 v1.9 E9.2 同协议锚点 0.470588（未达 0.8 旧协议阈值如实记「不支持」，
  两口径并列不互抵）。
- **H-B1（filler < 0.15 的骨架边界）**：支持但出现 2 例违规
  （L_algorithm_process 0.158、L_historical_causality 0.344），斩杀线（3 例）未触发；
  下次新增图若再出现 1 例违规即触发边界主张撤回。

**相变阴性**：S1/S2/S6 三族 N∈{20,35,45,60} 扫描，named 随 N 平滑衰减
（相邻档差均 <0.3），未检出相变点——规模不是场效应的相变旋钮，阴性结果归档。

### 4.2 先验 vs 全部臂：族 L 碾压与 H-C 成立域收缩

族 L 全候选协议（deposon_v20_crossval.json `prior_arm_eval`）：llm_prior 在 4/4 图
（初批）named Hits@3 第一——biological_taxonomy 1.000、historical_causality 0.783、
algorithm_process 0.690、physics_concepts 0.484；结构与物理臂全部 ≤0.22。
v1.9 的 H-C（先验零增量）成立域随之收缩：在对抗构造图（标签脱钩）为零增量，
在真实语义图为碾压级正增量——分界线是**图是否携带真实语义**。

**GT-3b 跨厂商复核**（deposon_v20_gt3.json）：五个评估者（Kimi 系 E0–E2、
ByteDance doubao E3、DeepSeek E4）在 Kimi 生成的图上复现同等量级优势；
E3 doubao 4/4、E4 deepseek 6/6 通过判据，三模型族合计 0 域先验 ≤ 场（0 败绩），
全 ok 域 Kendall W=1.0（逐域排序完全一致）。「先验优势是同厂商同源污染 artifact」
假说被实质性削弱；残余局限如实声明：三族均为中文优化大模型，共享中文语料不可排除，
最彻底检验需非中文模型族或人工标注图。

### 4.3 融合稀释：在所测 λ 档上不增

hybrid（λ·场 + (1−λ)·先验）在所有实测档上不超过先验：v1.6 单图扫描
λ∈{0.25,0.5,1,2}，λ=0.25 即量纲饱和；v2.0 族 L 四图 λ=0.5 档
（`hybrid_lambda_convex=0.5`）：physics 0.484→0.452、historical 0.783→0.739，
另两图持平——场对真语义先验只有稀释，v1.9「融合故事终结」在真实语义图上复现。
我们如实限定「稀释」成立域为所测 λ 档，不外推为全 λ 空间定理。

### 4.4 GT-2 自适应攻击者与 GT-2B 多陷阱升级

**GT-2（主 LOO 协议，crossval §三）**：攻击者知道关键词表后 100% 生成绕过规则的
语义陷阱标签（evasion_rate=1.000，4/4 图，如「以太假说」「原生生物界」式误导，
标签均不在图节点集内）；注入 10 个陷阱节点/图后，rule_filter 平均 −7.5pp
（三图各 −10pp），field_mean **−0.0pp（四图全零）**。预登记机械判定：
**no_separation**——rule 塌陷未达 20pp 阈值，攻击强度（每行 1 个陷阱候选，
~35 选 1）未达决定性强度，如实归档。场不读标签 ⇒ 对语义陷阱机制性免疫，
此方向性信号在案。

**题库轨（skills §三）**：40 题（bloom L4 × 自适应干扰项）下 rule_filter=27.5%
≈机会水平 25%——规则防御对自适应陷阱基本无效的直观证据。

**GT-2B 多陷阱强度升级**（deposon_v20_gt2b.json，T∈{1,2,3}，固定 4 选项）：
rule_filter 准确率 0.150/0.275/0.200，**非单调**（T=1→2 上升反转）⇒ 预登记判
**inconclusive**，不判死也不支持——n=40/格下 ±1 题=±2.5pp 的波动与机会噪声同阶，
统计功效不足。同时**场免疫判据被破坏（如实披露）**：|acc_field(T)−acc_field(1)|
最大 0.625（0.375/0.525/1.000），远超 ±0.05 容差；机制是固定 4 选项设计下 T 越大
图内竞争者越少（陷阱 −inf + 3−T 个随机节点），准确率随 T 机械上升——这不是语义
能力提升，而是选项构成假象对判据的破坏（判据设计缺陷）。与题库轨锚点兼容：
T=2 同种子复现 0.275 逐点一致。定性结论「规则三档均在机会水平附近（0.15–0.275）」
依旧成立。

### 4.5 领域鉴定器 v0：OLS 与 GT-8 语料外复现

**OLS（探索性）**（v20_regression_field_v2.json，n=20）：
field_named ~ density + hub_concentration + real_semantics，R²=0.628（调整 0.559，
F p=0.001）；**hub_concentration β=+2.12（p=0.00028）** 为场效力主导预测子，
real_semantics β=−0.16（p=0.012）显著压低场表现，density 不显著（p=0.13）；
VIF<4。n=20 小样本，标记**探索性 v0**，v2.1 扩图后重估。

**GT-8 语料外预登记复现**（deposon_v20_gt8.json，SPEC_GT8 先于数据提交）：
2 对配对新图（N 与边数逐对对配，real_semantics=0）上，高 hub 图的场优势
（field_named−random_named）一致大于低 hub 图（对 A：+0.7917 > +0.1333；
对 B：+0.0526 > −0.0833）⇒ **verdict=supports_H_GT8（2/2 同向）**，hub 轴方向
复现成功。如实披露：degree 基线在两高 hub 图上饱和（degree_named=1.0000，
diff_fm_deg 为 0.0 与 −0.9474）——hub 轴鉴别的是**结构信号整体可利用性**而非场
独有优势；B_low 上场被 random 反超（单图小样本波动，如实披露）。real_semantics
轴本轮 deferred（需 LLM 先验 API 预算，零 API 实验不测）。鉴定器 v0 规则：
hub_concentration 高 → 用结构信号（场/degree 同场竞技）；real_semantics=1 → 用先验。

### 4.6 题库效度与 field_mean 52.5% 的口径裁定（m6）

题库横向验证（deposon_v20_quiz_eval.json，40 题）：llm_prior 92.5%、field_mean 52.5%、
rule_filter 27.5%、random 25%；大题库扩至 157 题 × 6 域后方向全部复现
（deposon_v20_bigquiz_eval.json：prior 89.5%、ngram_tfidf 54.2% **击败**
field_mean 50.9%、rule_filter 19.6% 低于机会）。

field_mean 52.5% 曾有两种口径：skills 文档记「2×机会、结构信号部分迁移」；
corrections C2 记「2 选 1 机会水平，不携带信息」。**本稿裁定采用 C2 口径**，
理由有二（修订记录 M-1）：（i）机制在案——陷阱标签非图节点，field/prior 对其打
−inf（quiz_eval records note 字段逐题在案），39/40 题有效任务退化为「金边 +
1 图内随机节点」的 2 选 1，2 选 1 机会期望 ≈50%，52.5% 与之不可区分；
「2×机会」是按 4 选 1 机会 25% 计算的口径，忽略了 −inf 机制对有效选项数的改变。
（ii）GT-2B 提供独立佐证：场准确率随图内候选数减少而机械上升（0.375→1.000），
证明该通道上的场分数被选项构成自由度主导，不构成「语义迁移」证据。
故本稿统一表述为：**field_mean 题库 52.5% 为 2 选 1 退化口径下的机会水平，
不携带结构信号向语义任务迁移的信息。**

### 4.7 CoT 收编与方向对照

**CoT 收编**（deposon_v20_cot_quiz.json）：带选项文本的直接 CoT 问答 92.5%
（40 题子集），作为 CoT 收编证据按 CoT 轨自身口径报告。先验题库轨的 92.5%
按题库轨自身口径报告，两轨口径不同（先验题库因陷阱 −inf 退化为 2 选 1，
2 选 1 期望 94.4% 完全解释观测 92.5%；94.4% 为**文档级口径**，出处 corrections
C2，附录 A 降级项），二者数值关系不作对比陈述——按修正案 C2，「先验=CoT」
宣称**已正式撤回**。可比口径为：CoT 92.5%（带选项文本的 4 选 1）vs 先验开放
候选 top-1 67.5% / top-3 82.5%。禁止任何将两者直接并列等值的表述（C2 已撤回）。

**方向对照**（crossval `direction_kind_summary`）：族 L 四图先验边与金边方向一致率
≥0.96（抽象→具体 1.000、过程→结果 0.963），hub 反向边 = 0——与 Reversal Curse
的预言形成直接对照。v1.9 锚点图上的系统性方向反转（2/9 正确）判定为该重建图
（78% 占位标签 + 特定枢纽结构）的特异现象，非普遍方向语义缺陷；方向主张保留但
限真实语义图。

## 5 博弈论分析

本节把散射层反向动态置于势博弈透镜下解读。全稿采用 **consistency 口径**：
以下证据与势博弈解读**一致**（consistent with a potential-game reading），是一致性
证据而非形式化证明；除非另有注明（GT-5b/GT-6 为已闭合的预登记判定），不声称
证明了任何定理。

### 5.1 重构命题与建模选择

把每条留一预测边视为一个玩家，策略为候选目标节点，效用为场得分；确定性
mean-field 反向对应无噪声最好响应动态；物理能量的负值 Φ=−E 是势函数候选。
「每个任务是独立玩家」的分解是建模选择而非唯一（GT_RECONSTRUCTION §3 如实声明）；
Φ=−E 有解析依据（反向退火梯度即 −∇E）。Sandholm（2010）群体最好响应流为该
对应提供最近理论支点。

### 5.2 证据矩阵（六条，全部机械求值）

| 证据 | 实验 | 结果 | 判定 |
|---|---|---|---|
| ① 噪声动态严格劣于确定性极限（命中率口径） | GT-1 | dirichlet 均值 0.10 vs mean-field 0.40，gap=0.30 ≥ 0.2，20/20 运行严格劣 | ✅ 与势博弈解读一致 |
| ② 势函数轨迹单调不减 | GT-5b（收窄预登记） | **22/22 图 mean-field Φ 轨迹单调率=100%**（预登记线 ≥80%，斩杀线 0 触发） | ✅ supports_narrowed_monotonicity |
| ③ 场有协调价值（分布级 PoA） | GT-4 | 族 S median PoA=1.5 > 1.2（族 S 子集口径：13 图有限值，median 1.5，见 §5.4）；族 L 2 图 PoA<1 并列披露 | ✅ 支持（口径限定见 §5.3） |
| ④ 规则防御被自适应攻击瓦解、场机制性免疫 | GT-2 | evasion=1.0；场塌陷 −0.0pp | ✅ 支持（no_separation 限定） |
| ⑤ 信号优势跨厂商稳健 | GT-3b | 三模型族 0 败绩、全 ok 域 W=1.0 | ✅ 支持（中文优化族残余局限） |
| ⑥ 非势残余 | GT-6 | 边效用向量向梯度空间投影，残余中位数 ≈1.6e-29 < 0.10 预登记线 | ✅ potential_game_explanation_complete（3 图例外） |

### 5.3 GT-5 反转、GT-6 例外与 GT-7 温度前沿：意外如实呈现

- **GT-5 反转（不回溯改写）**：初版 GT-5 的终点条件未通过并判 inconclusive——
  3/4 图上 dirichlet 噪声臂终点 Φ **高于** mean-field（S6 gap=−0.31）。解读：
  噪声在命中率上有害（GT-1），在全局势上却有益——噪声是探索者、mean-field 是
  利用者，与 log-linear learning（Blume 1993）和确定性最好响应的经典分工一致。
  Deposon 的「温度」（噪声强度）由此获得博弈论语义而非调参旋钮。收窄后的
  单调性主张由新版预登记 GT-5b 闭合（22/22）；GT-5 终点反转保留于案。
- **GT-6 例外（并列披露）**：22 图中 3 张循环结构图残余越线——S4=0.148、
  L_algorithm_process=0.136、S5=0.121，其上势解释为**近似**。honesty 注明本分解
  是 Candogan 流分解的可操作类比（分解边效用向量，未沿轨迹积分）。
- **GT-7 温度前沿（判 mixed）**：α∈{0.3,…,20} × 4 图 × 5 seed——GT-5 反转
  可复现且系统化（同 3/4 图高温档终点 Φ > mean-field，Φ 增益集中在高温端，
  corr −0.87），温度确实控制全局势探索收益；但「双赢前沿」**不成立**（S6 高温档
  Φ 升而命中率 0.4→0.08），势与命中率是两个目标，本文不暗示「升温既提势又提质」。
  边界情形披露：命中率=0 的图（L_physics）使条件退化恒真，未回溯改规则。

### 5.4 PoA 的口径限定（防 overclaim）

PoA 只作分布级报告：操作化定义 PoA=field_mean/max(自利臂)（自利臂集 {random, degree}；
预登记的 llm_prior 臂在族 S 不可得，退化为弱化口径——分母只可能更小、PoA 只可能
偏大，如实披露）。族 S 13 张有限值图 median PoA=1.5 > 1.2 预登记线（3 张
PoA=∞ 单独计数：自利臂 named=0 而场>0）。该度量与经典 worst-case-NE/社会最优
比值**不是同一度量**，成本结构仿射/可分前提未闭合；median 数值与 Pigou 4/3 的
对齐仅为**巧合性对齐**，不主张实例级复现。族 L 2 张图 PoA<1（L_historical 0.5、
L_physics 0.75）——场在语义域为**负协调**，与分工叙事自洽：场只在结构域创造
协调价值，势博弈解释的适用域与分工边界一致，理论不自相矛盾。

### 5.5 守恒账与机制设计

守恒账（运行期逐实例不变量）定位为机制设计中的承诺装置（§2.5 空层），GT-2 实证
其必要性：规则防线在自适应攻击下渗漏（题库轨 27.5%≈机会），而机制性免疫
（不读标签）的臂不受影响。形式化命题（小图类「mean-field 反向=无噪声最好响应
动态」）尚未补齐，为投稿前 kill list 项；未补则全稿维持本节 consistency 口径。

## 6 边界与讨论

1. **场的边界**：H-A1 判死后，场的成立域收缩为「相对平凡结构基线的稳健优势 +
   高 hub 图局部优势」；H-B1 两例违规（L_algorithm_process 0.158、
   L_historical_causality 0.344）显示汇聚偏置与因果链结构反对齐；绝对命中率随
   结构否定大幅塌缩，「场=通用骨架检测器」已被本设计自身否定。
2. **先验的边界**：碾压结论限真实语义小图（30–45 节点 DAG）；GT-3b 后同源污染
   口径为「跨厂商削弱、中文优化族残余局限」（doubao 4/4、deepseek 6/6、0 败绩、
   W=1.0；三族均为中文优化大模型，共享中文语料不可排除）。
3. **BOSS 基线**：ngram_tfidf 在大题库击败 field_mean（54.2% vs 50.9%），
   L_project_management 上 PA/n2v/tfidf 三臂同图击败场（margin 6 边）——
   结构域内场并非无对手，领域鉴定器的结构分支应理解为「结构信号整体」。
4. **相变阴性**：规模扫描未检出相变点；质变发生在 n=1→n=20 的语料化而非 N 增长。
5. **鉴定器适用范围**：v0 为探索性（n=20 OLS + 2 对语料外方向复现）；hub 轴
   鉴别结构信号可利用性而非场独有优势（degree 高 hub 饱和）；real_semantics 轴
   仍 deferred；不外推至族 L 之外任务或更大规模图。
6. **理论空位口径**：本稿不附可审计检索协议，故全部空位表述统一为「尚未发现」
   的阴性口径（评审 m3），不宣称排他性空白。

## 7 方法论工件

本文同时交付一套科研工程工件，作为可审计性贡献本身：

- **预登记与修正案**：SPEC_v2.0.md、SPEC_v2.0_amendment1.md、SPEC_GT2B/GT3/GT8；
  判死刑则先于数据冻结，判定由脚本机械读取结果 JSON（kill_lines 类字段强制对照
  已列入 verifier v21）。
- **独立多角色评审**：M1–M5 主线裁定与 m1–m7 细则全部闭合于 outline 修订记录
  （reviews/review_coach_v2X_outline.md），含最高严重度的 C1 斩杀线触发与 C2
  「先验=CoT」撤回。
- **阴性结果归档**：相变阴性、GT-5 反转、GT-2B inconclusive、GT-7 mixed、
  no_separation 全部如实呈现，不美化、不回溯改写。
- **工程**：内容寻址缓存（sha256 + prompt 哈希 + attempts 落盘）、语料快照 sha 钉定、
  断点续传幂等设计、版本化 verifier（冻结文件走 erratum 不覆写）、
  全套 pytest（GT-8 批次 237 passed 无回归）。
- **教训复盘**（corrections §D）：「文档手写 vs 数据机械」是最富矿 bug 类别
  （本项目三次中镖）；单位与截断是第二富矿；冻结数据可信、散文不可信。

## 附录

### 附录 A：摘要数字机械追溯清单

| 数字 | 出处（JSON 路径与字段） |
|---|---|
| H-A1 判死 | `deposon_v20_corpus_eval.json` → `verdicts.kill_lines.H_A_dead.triggered=true` |
| p=0.0118（22 图） | 同上 → `verdicts.H_A1_field_mean_gt_random.sign_test.p_exact=0.011818` |
| 反转 4 图 | 同上 → `verdicts.kill_lines.H_A_dead.reversals_vs_random`（4 项） |
| field>degree p=4.0e-5 | 同上 → `verdicts.H_A2_field_mean_gt_degree.sign_test.p_exact=4.005e-05` |
| S6 族 0.471 | 同上 → `verdicts.H_S6_anchor_reproduction.S6_named_hits3=0.470588` |
| OLS β=2.12 / p=0.00028 / n=20 | `v20_regression_field_v2.json` → `coefficients.hub_concentration`（coefficient 2.1177, p_value 0.000279）、`n_observations=20` |
| 先验 named Hits@3 0.484–1.000 | `deposon_v20_crossval.json` → `prior_arm_eval.*.llm_prior.named`（0.4839–1.0） |
| CoT 92.5% | `deposon_v20_cot_quiz.json` → `overall_cot_accuracy=0.925` |
| 先验开放 top-1 67.5% / top-3 82.5%、2 选 1 期望 94.4% | `docs/Findings_v2.0_corrections.md` C2（开放候选实测口径） |
| no_separation / −7.5pp | `deposon_v20_crossval.json` → `gt2_verdict.rule_collapse_mean_pp=0.075`、`verdict="no_separation_adaptive_attack_not_decisive"` |
| 题库轨 rule 27.5% | `deposon_v20_quiz_eval.json` → `overall.rule_filter=0.275` |
| evasion 100% | `deposon_v20_crossval.json` → `gt2_attacker_meta.*.evasion_rate=1.0` |
| GT-1 gap 0.30、20/20 | `deposon_v20_gt.json` → `GT1_potential_game_convergence.verdict`（gap=0.30, n_runs_below_meanfield=20） |
| GT-5b 22/22 | `deposon_v20_gt5b.json` → `per_graph_summary.*.meanfield_monotone_rate=1.0`（22 图） |
| GT-6 残余中位 ≈1.6e-29、3 例外 | `deposon_v20_gt6.json` → `verdict.median_residual_ratio=1.594e-29`；例外 `per_graph_summary`（S4 0.148 / L_algorithm_process 0.136 / S5 0.121） |
| GT-7 mixed、corr −0.87、S6 0.4→0.08 | `deposon_v20_gt7.json` → `per_graph`（verdict mixed，见 GT_RECONSTRUCTION §7） |
| PoA median 1.5 / 13 图；族 L PoA<1（0.5、0.75） | `deposon_v20_gt.json` → `GT4_price_of_anarchy.poa_per_graph_finite` 族 S 13 项中位数 1.5；`L_historical_causality=0.5`、`L_physics_concepts=0.75` |
| GT-8 2/2 同向 | `deposon_v20_gt8.json` → `verdict.verdict="supports_H_GT8"`、`pairs_concordant`（2 对） |
| GT-2B 0.15/0.275/0.20 inconclusive | `deposon_v20_gt2b.json` → `verdict="inconclusive"`、`per_T.*.per_domain.*.accuracy.rule_filter` 聚合 |
| GT-3b doubao 4/4、deepseek 6/6、W=1.0 | `deposon_v20_gt3.json` → `verdict.H_GT3_supported=true`；逐域矩阵见 `docs/Findings_GT3.md` |
| Wilcoxon p=0.0031 / 配对 t p<0.0001 | `v20_statcheck_fm_vs_rand.json`（p_value=0.003052）、`v20_statcheck_fm_vs_deg.json`（p_value=2.13e-08） |
| 大题库 89.5%/54.2%/50.9%/19.6% | `deposon_v20_bigquiz_eval.json` → `overall`（prior 0.8947、tfidf 0.5417、field 0.5091、rule 0.1964） |
| 方向一致率 ≥0.96、hub 反向 0 | `deposon_v20_crossval.json` → `direction_kind_summary`（1.0 / 0.9627，total_hub_reversed=0） |

### 附录 B：基线注册表（摘要）

A 族结构启发式六臂 + degree + random（同协议 20 图实测）；B 族浅近似 Node2Vec
（如实标注非完整实现）；C 族直接 CoT 大 BOSS（92.5%）；BOSS 门槛 margin ≥3 金边
（C3 修正案；门槛后 BOSS 6 事件，含 L_project_management 三臂同图击败场）。
完整注册表见 docs/BASELINE_REGISTRY.md。

### 附录 C：缓存 provenance 与预算

族 L 获取、先验臂、GT-2 攻击者、GT-3 五评估者全部缓存内容寻址（prompt_sha256 在案、
attempts 落盘）；各轮 API 消耗与预算例外（PM 推理溢出、超登记 1 次）如实登记于
各 Findings 与修正案 A5。

### 附录 D：图（待中文版制作）

按 paper/FIGURE_LANGUAGE_POLICY.md，本稿为中文稿只引用中文图；下列图仅有英文版或
尚未绘制，初稿一律以文字表格替代，正式版补绘中文版（命名 `_cn` 后缀）：

1. 图 1：分工边界总览（22 图场-先验胜负地图）——图待中文版制作。
2. 图 2：H-A1 斩杀线与反转图分布（22 图符号检验散点）——图待中文版制作。
3. 图 3：领域鉴定器 v0 散点（hub_concentration × real_semantics 着色 field_named）——图待中文版制作。
4. 图 4：GT-7 温度前沿逐图形态（hits 与 Φ 双轴）——图待中文版制作。
5. 图 5：分布级 PoA 全 22 图条形（含 PoA<1 两图与 ∞ 计数）——图待中文版制作。

## 参考文献（占位，沿用 related_work_v2X.md 清单，正式版以 bib 落库）

1. Monderer & Shapley, GEB 1996（势博弈）。2. Rosenthal 1973（拥塞博弈）。
3. Sandholm 2010（群体最好响应流）。4. Candogan et al., MOR 2011（博弈流分解）。
5. Parise & Ozdaglar, Econometrica 2023（graphon 极限）。6. Jackson & Wolinsky 1996；
7. Fabrikant et al. 2003；8. Ma et al., TCS 2014；9. Waniek et al., Nat. Hum. Behav. 2018
   及 Stackelberg 边隐藏 2023。10. Koutsoupias & Papadimitriou 1999；
11. Roughgarden & Tardos 2002（仿射拥塞 PoA=4/3）。12. Christodoulou et al. 2014；
13. Benita 2020（分布级 PoA 先例）。14. Conitzer & Sandholm 2006；
15. Dekel et al. 2010；16. Hardt et al. 2016；17. Dütting et al., WWW 2024；
18. Raji et al. 2020；19. Jia et al. 2021（Proof-of-Learning）。
20. Tramèr et al., NeurIPS 2020（自适应攻击）；21. Nasr et al., USENIX Sec 2026；
22. Gröndahl et al., AISec 2018；23. Hosseini et al. 2017；24. Kahu & Ahuja 2025；
25. Jain et al. 2023；26. HateBench, USENIX Sec 2025。
27. KICGPT, Findings of EMNLP 2023；28. KG-LLM/Yao et al., ICASSP 2025；
29. Wadhwa et al., ACL 2023；30. Berglund et al., ICLR 2024（Reversal Curse）；
31. Wang & Sun, ICLR 2026；32. MKGL, NeurIPS 2024；33. Zhang et al., ACL 2025。
34. Novak & Cañas 2008；35. Ruiz-Primo & Shavelson 1996；36. KnowEdu, IEEE Access 2018；
37. MOOCCube/MOOCCubeX, ACL 2020 / CIKM 2021；38. Pinandito et al. 2021（KitBuild）；
39. Ma & Chen, LAK 2025。
40. Lipton & Steinhardt, CACM 2019；41. Dodge et al., EMNLP 2019；42. Recht, ICML 2019；
43. Tevet & Berant, EACL 2021；44. D'Amour et al., JMLR 2022；
45. Lazaridou et al., NeurIPS 2021；46. Schaeffer et al., NeurIPS 2023；
47. Mallen et al., ACL 2023；48. Dziri et al., NeurIPS 2023；
49. Bowman, ACL 2022（Dangers of Underclaiming）；50. Blume 1993（log-linear learning）。
51. Deposon 1.X 论文（v1.9 冻结稿），前序工作。

---

## 成稿修订记录（2026-08-30，初稿执笔）

1. **M-1（m6 裁定）**：§4.6 field_mean 题库 52.5% 采用 corrections C2 口径
   （「2 选 1 机会水平，不携带信息」），放弃 skills 的「2×机会 部分迁移」。
   证据锚：deposon_v20_quiz_eval.json records note 字段（陷阱 −inf 机制逐题在案）+
   deposon_v20_gt2b.json 场准确率随图内候选数机械上升（0.375/0.525/1.000）的独立佐证。
   理由：C2 为修正案登记的后更正口径且为机制级实锤，skills 口径按 4 选 1 机会 25%
   计算、忽略 −inf 对有效选项数的改变；52.5%≈2 选 1 机会 50%，不可区分于噪声。
2. **M-2**：H-A1 一律标注判死（triggered），22 图口径 p=0.0118 与斩杀线并存、
   以预登记斩杀线为准；全文未出现将 CoT 与先验题库准确率并列等值的对比表述（C2 已撤回，§4.7 禁用）。
3. **M-3**：GT-2 双轨并述——主 LOO 协议 no_separation（−7.5pp）/ 题库轨 27.5%≈机会；
   GT-2B 多陷阱 inconclusive 与场免疫判据设计缺陷如实归档于 §4.4。
4. **M-4**：PoA 仅作分布级报告（族 S median 1.5、13 图有限值），族 L 2 图 PoA<1
   （0.5、0.75）并列披露；与 Pigou 4/3 仅为巧合性对齐，无实例级复现措辞。
   说明：median 1.5/13 图为族 S 子集口径（deposon_v20_gt.json
   `poa_per_graph_finite` 族 S 13 项中位）；全 17 有限值图口径中位为 1.333，
   按评审 M4 纪律采用前者并在 §5.4 注明口径构成。
5. **M-5**：势博弈全稿 consistency 口径；仅 GT-5b（22/22 单调）与 GT-6
   （残余中位口径完备 + 3 图例外）作为已闭合预登记判定引用；不声称证明。
6. **GT-3b 后口径**：同源污染统一为「跨厂商削弱、中文优化族残余局限」。
7. **m3**：理论空位统一为「尚未发现」阴性口径（§2.4、§6.6），未附检索协议。
8. **OLS 探索性限定**已加（§4.5 与摘要）。
9. **GT-8 回填**：§4.5 写入 2/2 同向 supports_H_GT8、degree 高 hub 饱和披露、
   real_semantics 轴 deferred。
10. **图纪律**：全部图以文字表格替代并注明「图待中文版制作」（附录 D）。
11. **降级处理声明**：先验开放 top-1/top-3（67.5%/82.5%）与 2 选 1 期望 94.4%
    的原始 JSON 字段未在 results/ 独立文件中定位到（仅存于 corrections C2 文档），
    附录 A 已如实标注其出处为文档级；GT-7 的 corr −0.87 与逐图数字以
    GT_RECONSTRUCTION §7 为叙事锚，deposon_v20_gt7.json per_graph 字段支持
    hits/Φ 走向但相关系数为文档汇总值。

12. **复核返工记录（2026-08-30）**：按 `reviews/post_draft_verification_v2X.md`
    复核报告返工，2 Major + 4 Minor 全部闭合：
    - Major-1：§4.7 删除两 92.5% 并列等值表述（outline M1 禁用对比），
      改为两轨各自口径独立报告；94.4% 就近标注「文档级口径（corrections C2，附录 A 降级项）」。
    - Major-2：outline_v2X.md kill list「领域鉴定器 v0 新图复现」勾选闭合
      （GT-8 完成，2/2 同向 supports_H_GT8，见 docs/Findings_GT8.md）。
    - Minor-1：附录 A PoA 路径修正为 `GT4_price_of_anarchy.verdict.poa_per_graph_finite`。
    - Minor-2：§4.4「三图各 −10pp」补第四图 0pp 的如实并列。
    - Minor-3：§4.7 94.4% 就近加文档级口径指引（随 Major-1 一并闭合）。
    - Minor-4：§5.2 表 ③ PoA 行注明「族 S 子集口径（13 图有限值，median 1.5）」。
