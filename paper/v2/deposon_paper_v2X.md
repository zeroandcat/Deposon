# 可审计优势的博弈论实证：物理约束散射层的势、协调价值与审计边界

**Game-Theoretic Evidence for the Auditability Advantage: Potential, Price of Anarchy, and Audit Boundaries of a Physics-Constrained Scattering Layer**

> v2.X 论文中文稿（2026-08-30 结构标准化版）。体裁声明：实证性机制研究——对前序工作
> 「可审计表征与守恒保证」价值命题的动力学层实证；领域划界作为该主线的推论呈现。
> 本稿是独立新稿，引用 1.X 论文（deposon_paper_v1.md / _en.md，冻结于 v1.9 状态）作为前序工作。
> 全部实验判定为预登记后的机械规则求值；所有数字可追溯至 `results/` 下冻结 JSON 的具体字段
> （逐字段出处见附录 A）。

## 摘要

前序工作把散射层的价值命题定位于可审计表征与守恒保证，但守恒账只经静态核验：反向动力学是否真有一个可对标审计的标量，未曾实证。本文在同一预登记协议与二十二张受控概念图上给出博弈论证据链：留一边为玩家、场得分为效用、能量负值为势候选。结论有三：势轨迹全图单调不减、非势残差中位近零（例外在案），每步演化可审计为势下降，审计标量实证成立；无政府代价把审计定量化，自利动力学离最优多远可以算出，语义图上小于一并列披露；温度前沿划定审计边界，升温只提势探索不兼提命中率。两臂可审计性成立域互不重叠，作为划界推论给出。预登记文件、判定脚本与追溯清单随稿交付。

**关键词**：可审计性；势博弈；无政府代价；预登记；阴性结果；概念图补全

## 1. Introduction（引言）

本节按「领域背景 → 子领域趋势 → 问题与缺口 → 缺口的实证证据 → 方案高层 → 贡献列表 → 路线图」的漏斗结构组织。

物理约束散射层（下称「场」）是一类把图补全表述为能量弛豫的链接预测机制：在图邻接权矩阵上定义路径聚合能量，反向退火给出候选目标节点的排序。概念图作为教育与知识表征的经典体裁由 Novak & Cañas 定义并奠基 [34]，其补全任务的评估对协议高度敏感 [35]；前序工作（1.X，v1.9 冻结稿）[51] 已在该任务上建立了散射层框架与基准纪律。这一方向之所以重要，在于图补全系统越来越多地承担可追责的筛选与拦截职能，其决策过程本身需要被复核，而非只被采信。

子领域层面的趋势有二。其一，结构信号的价值域由图属性决定，这一点已被同质性/异质性（homophily/heterophily）研究线系统回答：结构归纳偏置在同配图上有益、在异配图上失效，标签与特征信号接管 [52][53][54][55]。其二，在准确率维度难以拉开差距的背景下，前序工作把散射层的价值命题从筛选性能迁往**可审计表征与守恒保证**：任意参数下逐路径 $T+R+A=1$ 守恒账（机器精度 $2.2\times10^{-16}$）、每次阻断留下可复核的能量记录、淘汰决策可逐节点归因 [51]。

但该命题有一个尚未补齐的层次。守恒账是对每一次散射的**静态数值核验**：它证明每一步能量去向合规，却没有回答动力学问题——场的反向演化作为一个整体过程，是否真有一个可对标的标量，使「每一步该往哪走、走了多远、离最优还有多远」都可被同一本账审计？如果这样的标量不存在，可审计性就退化为逐步合规性检查，审计者面对的是一串彼此无关的守恒断言，而非一条可整体复核的轨迹。本文的研究问题是：**可审计优势命题能否获得动力学层实证**——反向动力学是否真有一个可对标审计的标量，该标量把审计定量化到什么程度，以及审计的边界在哪里。

这一缺口有实证依据而非修辞。三稿构成一条「出题 → 定命题 → 给实证」的链条：1.X 出题，建立散射层框架与基准纪律，并在整改中证明基准效应量结构性不可归因、规则基线可追平管线（v1.9）；v1.9 定命题，价值定位于可审计表征与守恒保证，准确率优势被显式放弃。换言之，准确率层的退路已被前序工作自身的阴性结果封死，可审计性命题成为唯一存续的价值主张，而它至今只有静态核验支撑，动力学层证据完全缺位。本文（v2.X）给机制层实证：用同一协议下的博弈论证据链回答上述动力学问题。本文不重复 1.X 的框架细节，只继承其全候选排序协议（E9.2 口径）、预登记纪律与缓存幂等工程；为保证独立可读，场、先验与协议的操作化定义在 §3 自足给出。

方案的高层思想是：把反向动力学建模为图上势博弈——每条留一预测边为一个玩家，候选目标为策略，场得分为效用，物理能量的负值 $\Phi=-E$ 为势函数候选。在此建模下，「每步演化可审计为势下降」成为可检验命题，「自利动力学离协调最优多远」成为可计算量（无政府代价，Price of Anarchy，PoA），「温度」则获得博弈论语义并暴露审计的边界。全部判定为预登记后的机械规则求值。

本文贡献如下：

1. **审计标量的存在性实证**：把反向动力学建模为图上势博弈（每条留一预测边为玩家，
   候选目标为策略，场得分为效用，物理能量负值 $\Phi=-E$ 为势函数候选）。两条预登记判定
   闭合：势轨迹在 22/22 图单调不减（GT-5b，收窄主张，预登记线 ≥80%，斩杀线 0 触发）；
   非势残差中位数 ≈1.6e-29 低于 0.10 预登记线（GT-6，3 张循环结构图例外如实披露）。
   合起来，每步演化可审计为势下降（consistency 口径，§5）。
2. **审计的定量化**：分布级 PoA 报告给出「自利动力学离协调最优多远」的可计算答案——
   全 17 张有限值图 median PoA=1.333 > 1.2 预登记线（族 S 子集 13 图 median 1.5
   并列），族 L 2 图 PoA<1 并列披露；该操作化度量与经典 worst-case PoA 不是同一
   度量，口径限定见 §5.4。
3. **审计边界的诚实声明**：温度前沿扫描（GT-7，判 mixed）表明升温提高全局势探索
   收益但不兼提命中率，「双赢前沿」不成立——势与命中率是两个目标，审计承诺
   只覆盖前者（§5.5）。
4. **划界推论（观察性规律，非主线）**：可审计优势的成立域按信号臂划界——场结构臂
   与先验语义臂各有其可审计性成立域，由图的两个可计算特征（hub_concentration 与
   real_semantics）方向性预测；该规律以观察性证据提出（探索性回归 + 小样本语料外
   复现，§4.4），不作为已确立的判别器贡献，其适用边界随证据一并给出。
5. **方法论工件**：预登记文件、版本化判定脚本（verifier）、基线注册表
   （含潜伏强基线披露门槛）、缓存 provenance，全部随稿发布（§6.4）。

路线图：§2 按主题定位相关工作；§3 自足给出场、先验、协议与语料的操作化定义；§4 报告 22 图语料上的预登记实验与划界推论；§5 给出博弈论证据链这一主线分析；§6 讨论边界、局限与随稿交付的方法论工件；§7 总结并列出 Limitations。

## 2. Related Work（相关工作）

本节按七个主题组织文献定位：结构基线、结构信号价值域、LLM 语义先验、概念图任务、博弈论基础、机制设计与审计、边界分析体裁。文献锚点来自 reviews/literature_scan_v2X_A.md 与 _B.md（各 40 条，经检索交叉核验）；本节新扩展的条目逐条标注核实状态。

### 2.1 结构驱动的链接预测

经典结构启发式构成我们基线注册表的 A 族：共同邻居、Adamic-Adar、Jaccard、Preferential Attachment、Katz 与 Personalized PageRank。本文在 20 张图上对全部六臂做了同协议实测（外加 degree 与 random），并补入一臂纯 numpy 浅近似 Node2Vec（标注为非完整实现）。可训练的 KGE 系列（TransE/ComplEx/RotatE）在 20 图规模方可训练，列为 v2.1 排期项（注册表 ⬜）。词法余弦（字符 n-gram TF-IDF）这类常被忽视的零成本基线在 5/20 张图上击败了我们的主臂，此类「潜伏强基线」正是注册表披露机制要制度性防止的（§4.3）。

### 2.2 结构信号何时有用：同质性谱系与启发式—可训练划界

「结构信号的价值域由图属性决定」在 GNN 文献中已被同质性/异质性（homophily /
heterophily）研究线系统回答：结构归纳偏置在同配图上有益、在异配图上失效，标签与
特征信号接管（同质性概念的社会学源流见 McPherson et al. 2001 [52] [待核：条目需文献核实]；
方法线代表为 Geom-GCN, ICLR 2020 [53] [待核：条目需文献核实] 与 H2GCN, NeurIPS 2020
[54] [待核：条目需文献核实]；综述见 Zheng et al. 2022 [55] [待核：条目需文献核实]）。后续
工作进一步表明同质性并非唯一旋钮，结构-特征互补的中间体制同样存在（Luan et al.,
NeurIPS 2022 [56] [待核：条目需文献核实]），且结构差异（structural disparity）本身可
预测 GNN 相对 MLP 的优劣（Mao et al., NeurIPS 2023 [59] [待核：条目需文献核实]）。
链接预测侧，SEAL（Zhang & Chen, NeurIPS 2018 [57] [待核：条目需文献核实]）证明可训练
模型学习的恰是启发式可表达的局部结构，Srinivasan & Ribeiro（ICLR 2020
[58] [待核：条目需文献核实]）给出位置嵌入与结构表示的等价性分析；「启发式何时足够」
同样已有系统答案。

与上述文献的关系须讲清楚。本文的 hub_concentration 不是同质性的替身：同质性是
**标签-结构一致性**度量（需要已知标签上的相似性），hub_concentration 是纯拓扑量
（最大入度与边数之比），二者回答的问题不同：前者问「邻居是否同类」，本文问
「结构信号本身是否可被利用」。本文的增量在于任务与信号对的极端性：概念图补全上，
一个不读标签的物理场与一个只看标签的 LLM 先验，在同一预登记协议下的划界未被做
过；同质性文献的划界对象是可训练 GNN 与标签特征的配比，而非这种机制上互盲的
极端信号对。

### 2.3 LLM 语义先验与方向语义

LLM 用于知识图谱补全的近三年证据链给出我们数字的横向坐标：KICGPT（Findings of
EMNLP 2023）[27] 以检索+LLM 重排超过纯 LLM；KG-LLM/Yao et al.（ICASSP 2025）[28] 显示
零样本 GPT-4 弱于微调 6-7B 模型；Wadhwa et al.（ACL 2023）[29] 表明即使精心 prompt，
GPT-3 也仅接近全监督关系抽取。我们 labels-only 先验在真实语义图上的 named Hits@3
（0.484–1.000）高于上述零样本区间，但有两点限定：其一，跨厂商检验后「同源污染
artifact」假说被实质性削弱但未排除（残余局限：三个受测模型族均为中文优化大模型，
训练语料可能共享公开中文知识，§4.2）；其二，图为 30–45 节点的小规模 DAG。

方向语义上，Reversal Curse（Berglund et al., ICLR 2024）[30] 及其机制解释（Wang & Sun,
ICLR 2026）[31] 预言 LLM 对「A→B 成立」无法推出「B→A」。我们在 labels-only 补全设定下
未观测到反转诅咒（先验边与金边方向一致率 ≥0.96，§4.3）；这是任务设定差异
（小规模 DAG 上的标签推理 vs 大规模预训练记忆提取），不构成对反转诅咒机制的反驳；
v1.9 锚点图上亦曾观测到系统性方向反转（占位标签特异现象），两种现象并存恰
说明方向表现的条件性。MKGL（NeurIPS 2024）[32] 关于标签文本自带结构信号的「三词语言」
论证，与我们的 n-gram 词法基线获胜现象互相印证。Zhang et al.（ACL 2025）[33] 对 KGC
prompt 结论泛化性的系统复测提醒我们标注泛化面：跨厂商检验已扩展至三个模型族，
但均为中文优化大模型，非中文模型族的检验仍为开放局限。

### 2.4 概念图：任务与评估

概念图由 Novak & Cañas（2008）[34] 定义并奠基。Ruiz-Primo & Shavelson（1996）[35] 指出概念
图评估的「任务-评分依赖」，即得分对协议高度敏感，这与 v1.9 对负采样协议的批判构成
跨三十年的同一教训。基准方面，KnowEdu（IEEE Access 2018）[36] 与 MOOCCube/MOOCCubeX
（ACL 2020 / CIKM 2021）[37] 提供教育知识图谱参照。KitBuild「补全式概念图」
（Pinandito et al., 2021）[38] 在任务形式上与我们一致，LLM 侧同体裁近作见 Ma & Chen
（LAK 2025）[39]；区别之处在于：本文不补全人工课程图，而是用受控语料（结构否定族 +
LLM 生成族）系统扫描信号价值域，且全部判定预登记。

### 2.5 博弈论基础：势博弈、网络形成与 PoA

把补全建模为博弈有四个理论锚点。Monderer & Shapley（GEB 1996）[1] 的势博弈框架与
Rosenthal（1973）[2] 拥塞博弈给出势函数存在性的经典条件；Sandholm（2010）[3] 的群体最好
响应流证明确定性最好响应动态在群体极限下沿势函数梯度上升，这是我们把「均值场
确定性反向 = 无噪声最好响应动态」作为解释性解读的最近支点。Candogan et al.
（MOR 2011）[4] 的博弈流分解与 Parise & Ozdaglar（Econometrica 2023）[5] 的 graphon 连续
极限，分别提供「场=图流分量」与「大图极限」的进一步形式化路径；我们尚未发现该
理论交集与扩散生成模型文献之间的相互引用（阴性文献口径，未附可审计检索协议，
见 §6）。网络形成与攻防方向上，Jackson & Wolinsky（1996）[6]、Fabrikant et al.（2003）[7]
奠基，Ma et al.（TCS 2014）[8] 与 Waniek et al.（2018/2023）[9] 最接近对抗性边操作场景；
我们与对抗鲁棒性赛道显式划界：本文攻击者不是扰动输入以翻转模型输出，而是在规则
已知下生成语义陷阱（§2.6）。PoA 方面，Koutsoupias & Papadimitriou（1999）[10] 与
Roughgarden & Tardos（2002）[11] 的仿射拥塞 $\mathrm{PoA}=4/3$ 界是经典锚点；我们的实证是分布级
PoA 报告（§5.4），操作化定义与经典 worst-case 比值不是同一度量。

### 2.6 机制设计、审计与自适应攻击

机制设计侧，Conitzer & Sandholm（2006）[14]、Dekel et al.（2010）[15]、Hardt et al.（2016）[16]
与 Dütting et al.（WWW 2024）[17] 构成上下文；审计侧 Raji et al.（2020）[18] 给出组织层
算法审计框架，Jia et al.（2021）[19] 的 Proof-of-Learning 给出密码层可验证计算。我们的
守恒账定位为运行期逐实例不变量，即事后溯源与密码证明之间的空层，写作时与 PoL
显式划界。自适应攻击侧，Tramèr et al.（NeurIPS 2020）[20] 与 Nasr et al.（USENIX Sec
[21] [待核：年份需核实，应为 2025 或 in-press]）提供方法学合法性；规则防线的失效有五条
独立证据链（Gröndahl et al. 2018 [22]；Hosseini et al. 2017 [23]；Kahu & Ahuja 2025 [24]；
Jain et al. 2023 [25]；HateBench, USENIX Sec 2025 [26]）。本文 GT-2 结果按双轨口径并述：
预登记主协议判 no_separation，题库轨规则基线塌陷至机会水平（§4.3）；「规则防线
失效」目前仅在题库轨成立，与上述五条证据链方向一致但强度未定。

### 2.7 边界分析与阴性结果体裁

本文主线是对前序价值命题的实证化，其中划界推论及其证据（§4.4、§6）的体裁自我声明为 boundary analysis，先例三层齐备：宣言层 Lipton & Steinhardt
（CACM 2019）[40] 与 Dodge et al.（EMNLP 2019）[41]；顶会实证模板层 Recht（ICML 2019）[42]、
Tevet & Berant（EACL 2021）[43]、D'Amour et al.（JMLR 2022）[44]、Lazaridou et al.
（NeurIPS 2021）[45]、Schaeffer et al.（NeurIPS 2023）[46]、Mallen et al.（ACL 2023）[47]、
Dziri et al.（NeurIPS 2023）[48]；专门 outlet 层 Insights from Negative Results workshop
（已办六届）。Bowman（ACL 2022）[49]「The Dangers of Underclaiming」是我们诚实降级的
自我设防参照：所有否定性主张（融合稀释、场边界、规则失效）均以预登记判死规则和
机械判定为限，不超出数据。

## 3. Method（方法）

本节自足给出全部操作化定义，不依赖 1.X 阅读：§3.1 给出场能量的核心形式化，§3.2 给出先验到全候选排序的关键机制，§3.3 给出协议与图特征设计，§3.4 给出语料与统计的实现细节。记号：图为有向图 $G=(V,E)$，$N=|V|$；任务为对每条金边的留一预测。

### 3.1 核心形式化：场能量与确定性反向

散射层在图邻接权矩阵 $W$（行随机）上定义能量。对留一任务 $(s,t)$，场引导能量为

$$
E(s,t) = -\log\Big( \sum_{p:\, s\rightsquigarrow t} \prod_{e\in p} t_e \Big) + \lambda_{\mathrm{smooth}}\cdot \sum_{ij} W_{ij}^{2}
$$

其中 $t_e$ 为边透射率（aggregate 模式），第一项是所有 $s\to t$ 路径聚合透射率的负对数，
第二项为平滑正则。反向过程以退火调度（$\beta$ 线性、50 步、lr=0.1、$\lambda_{\mathrm{smooth}}=0.01$、
uniform_out 先验）对掩码位置做单纯形自然梯度下降，结束后掩码行上的分布给出候选
目标的排序分数，即 field 臂得分。**field_mean（确定性反向）**取 Dirichlet 起点分布
均值，全程无采样噪声；对照臂 dirichlet 噪声反向在起点引入采样，其浓度参数 $\alpha$ 扮演
等效温度。场只读拓扑、不读节点标签文本——这是它与一切语义臂的机制性分界，也是
它对语义陷阱免疫的来源（§4.3）。配置字段冻结于各结果 JSON 的 `config` 节。

### 3.2 关键机制：labels-only LLM 先验到全候选排序的映射

先验臂的输入只有节点标签列表（带整数索引），prompt 中不存在任何索引对形式的结构
暗示；模型输出严格 JSON 数组 `[{parent, child, confidence}]`，即它认为最可能成立的
父→子语义边及置信度。响应经解析与校验：索引越界拒绝、自指忽略、confidence 截断
至 [0,1]。全部调用经内容寻址缓存（prompt_sha256 在案），预算预登记且 attempts
全落盘。

**开放输出到全候选排序的映射规则（机械，无人工裁定）**：对留一任务 $(u, \cdot)$，候选
为全部图节点 $v$。映射分三步：

1. 先验声明边 $(u,v)$ 的候选得分 = $\mathrm{confidence}(u,v)$；
2. 先验未声明的候选得分 = 0；
3. 同分（包括全体 0 分候选之间）以 1e-6 级确定性微扰破平局，微扰由实例种子
   rng 产生，与 random/degree 等所有臂同一破平局口径；掩码外位置恒为 $-\infty$。

因此先验声明的目标按 confidence 排在前列，未声明目标以种子化随机次序排在 0 分档；
不存在字符串匹配、Embedding 最近邻或人工裁定环节，映射失败（解析错误、索引越界）
直接以 fetch_failed/校验失败计入预算台账而不进入评分。族 S 标签为合成占位符、与
结构脱钩，先验在其上无意义，故先验臂只在族 L 主报（预登记口径）。

### 3.3 设计：全候选排序协议与图特征操作化

对每张图的全部 named 边做留一任务化，每任务以全部图节点为候选排序，指标为
named/filler Hits@3。所有臂（场、random、degree、共同邻居、Adamic-Adar、Jaccard、
Katz、PPR、Node2Vec 浅近似、ngram_tfidf、rule_filter、llm_prior、hybrid）跑同一
协议；random 与场实例均种子化（rng=g_seed·100003+ei）。

图特征的操作化定义如下：

- **named / filler 边**：named 为各图族的主干结构边（如链的全部链边、树的内部
  父子边、DAG 的最长路径族、辐条族的骨架汇聚边；逐族规则冻结于语料生成脚本与
  SPEC），filler 为其余结构边（多为叶部挂载）。族 L 中 named 为有语义内容的金边。
- **hub_concentration（枢纽集中度）**$=$ 最大入度 $/$ 边数。取值越高，图的入度质量
  越集中于少数枢纽。
- **real_semantics（真实语义标记）**：二值。标签为合成占位符（与结构脱钩）记 0；
  标签为真实领域概念、由 LLM 按领域主题生成记 1。标注在图生成时确定，非事后判读。
- **density（边密度）**：边数相对图规模的密度度量，语料设计变量之一；回归中的
  逐图取值冻结于 `v20_regression_field_v2.json` 的特征表。

### 3.4 实现细节：语料、预登记与统计

语料按「结构否定 × 真实语义」两族设计（这是本文的语料设计原则，全文不再使用其他
概括表述）：

- **族 S（结构否定族，16 张）**：S1 单链、S2 平衡树、S3 多 hub、S4 跨链 DAG、
  S5 无枢纽随机 DAG、S6 辐条汇聚，含 S1/S2/S6 的 $N\in\{20,35,45,60\}$ 尺寸扫描档；
  标签为合成占位符（real_semantics=0），用于否定「场=通用骨架检测器」的强主张。
- **族 L（真实语义族，6 张）**：biological_taxonomy、historical_causality、
  algorithm_process、physics_concepts、geography_world、project_management，
  由 LLM 生成，按方向语义配对（抽象→具体 ×3 / 过程→结果 ×3），30–45 节点。

语料快照以 index sha256 钉定；20→22 图的快照漂移已在工程记录中归档（§6.4）。

全部假设与判死规则先于数据写入预登记文件（主假设及后续各批次 GT 实验各有独立
预登记文档）；判定由脚本从结果 JSON 机械读取，禁止手写。多重性控制用 Holm
（m=4，α=0.05）；配对比较用符号检验，另以 Wilcoxon/配对 t 作第二意见复核
（field>random Wilcoxon p=0.0031，|r|=0.83；field>degree 配对 t p<0.0001，
Cohen's d=2.05）。

## 4. Experiments（实验）

本节各实验共享同一预登记协议与 22 图语料，为 §4.4 划界推论与 §5 主线提供共用证据底座，逐字段追溯见附录 A。§4.1 报告主基准（场 vs 结构基线），§4.2 报告次基准（先验 vs 全部臂）与融合稀释分析，§4.3 报告扩展实验（自适应攻击、题库效度与方向观察），§4.4 给出划界推论。

### 4.1 主基准：场 vs 结构基线——H-A1 判死、存活表述与一个 post-hoc 边界观察

22 图口径（results/deposon_v20_corpus_eval.json）：

- **H-A1（field_mean > random）**：符号检验 16+/4−/2 平，p=0.0118，Holm 过，但预登记斩杀线为析取规则（不显著或 ≥3 张图反转），反转图达 4 张
  （L_historical_causality、L_physics_concepts、L_project_management、S2_n45），
  故 `H_A_dead.triggered=true`，**H-A 头条主张判死**。
- **存活表述①**：H-A2（field_mean > degree）跨口径稳健：22 图 19+/1−/2 平，
  p=4.0e-5，Holm 过；20 图子集经 Wilcoxon/配对 t 复核为大效应（§3.4）。
- **存活表述②**：高枢纽结构图的局部优势：S6 族 named Hits@3 = 0.471，逐位复现
  v1.9 E9.2 同协议锚点 0.470588；按旧协议 0.8 阈值该数值本身记「不支持」，两口径
  并列不互抵。
- **H-B1（filler < 0.15 的骨架边界）**：支持但出现 2 例违规（L_algorithm_process
  0.158、L_historical_causality 0.344），斩杀线（3 例）未触发；下次新增图若再出现
  1 例违规即触发边界主张撤回。在此动态斩杀线生效前，当前主张强度为「22 图口径下
  支持、已有 2/3 额度被消耗的有条件成立」。

**事后边界观察（post-hoc，显式标注）**。4 张反转图全部位于语义/低枢纽图，这一
「斩杀线触发⇒分工边界」的推论**不是预登记内容**，是事后观察。我们补一个零假设
检验：把「语义/低枢纽」操作化为 real_semantics=1 的 6 张族 L 图 ∪ 语料设计中最大
入度为 1 的无枢纽子族 S1/S2 共 9 张（合计 15/22），4 张反转图全部落入该类的单边
超几何 p=0.187，**未达显著**；作为补充，反转在族 L 内部的富集（3/4 张落入 6/22）
p=0.046，达边界显著。因此本文把该推论降为「**与边界假设一致的事后方向性观察**」，
不作直接证据引用；可复算代码见附录 E。它与 H-B1 违规图、PoA<1 图同向，三条独立
事后线索共同指向同一边界，但均不单独构成决定性证据。

**相变阴性**：S1/S2/S6 三族 N∈{20,35,45,60} 扫描，named 随 N 平滑衰减（相邻档差
均 <0.3），未检出相变点；规模不是场效应的相变旋钮，阴性结果归档。

### 4.2 次基准与分析：先验 vs 全部臂、H-C 成立域收缩与融合稀释

族 L 全候选协议（deposon_v20_crossval.json `prior_arm_eval`）：llm_prior 在 4/4 图
named Hits@3 名列第一：biological_taxonomy 1.000、historical_causality 0.783、
algorithm_process 0.690、physics_concepts 0.484；同图结构与物理臂全部 ≤0.22。
v1.9 的 H-C（先验零增量）成立域随之收缩：在对抗构造图（标签脱钩）为零增量，在
真实语义图为大幅正增量，分界线是图是否携带真实语义。

**跨厂商复核（GT-3b）**（deposon_v20_gt3.json）：五个评估者（Kimi 系 E0–E2、
ByteDance doubao E3、DeepSeek E4）在 Kimi 生成的图上复现同等量级优势；E3 doubao
4/4、E4 deepseek 6/6 通过判据，三模型族合计 0 域先验 ≤ 场，全 ok 域 Kendall W=1.0
（逐域排序完全一致）。「先验优势是同厂商同源污染 artifact」假说被实质性削弱；
残余局限：三族均为中文优化大模型，共享中文语料不可排除，最彻底检验需非中文模型族
或人工标注图。

**融合稀释：在所测 λ 档上不增。** hybrid（λ·场 + (1−λ)·先验的凸组合）在所有实测档上不超过先验：v1.6 单图扫描
λ∈{0.25,0.5,1,2}，λ=0.25 即量纲饱和；v2.0 族 L 四图 λ=0.5 档
（`hybrid_lambda_convex=0.5`）：physics 0.484→0.452、historical 0.783→0.739，
另两图持平；场对真语义先验只有稀释，v1.9「融合故事终结」在真实语义图上复现。
这一结果排除了「互补（complementary）」措辞的最低可操作含义（组合有增益）：
本文证据支持的是**价值域互不重叠的分工**，不支持互补。稀释结论的成立域限于所测
λ 档，不外推为全 λ 空间定理。

### 4.3 扩展与应用：自适应攻击、题库效度与方向观察

本小节把协议扩展到对抗与小样本应用设定，回答两个问题：规则防线与场在自适应攻击下的行为是否可分（GT-2/GT-2B），以及题库轨数字应如何解读（效度口径与 CoT/方向参照）。

**GT-2（主留一协议，见附录 A 追溯清单）**：攻击者知道关键词表后 100% 生成绕过规则的
语义陷阱标签（evasion_rate=1.000，4/4 图，如「以太假说」「原生生物界」式误导，
标签均不在图节点集内）；注入 10 个陷阱节点/图后，rule_filter 平均 −7.5pp
（三图各 −10pp，第四图 0pp），field_mean −0.0pp（四图全零）。预登记机械判定：
**no_separation**：rule 塌陷未达 20pp 阈值，攻击强度（每行 1 个陷阱候选，
约 35 选 1）未达决定性强度。场不读标签，对语义陷阱机制性免疫，此方向性
信号在案。

**题库轨（quiz 协议）**：40 题（bloom L4 × 自适应干扰项）下 rule_filter=27.5%，
与机会水平 25% 不可区分，是规则防御对自适应陷阱基本无效的直观证据。注意本轨
n=40/格，±1 题即 ±2.5pp，与机会噪声同阶，本轨全部数字（含先验 92.5%、场 52.5%）
应一律按小样本宽区间解读。

**GT-2B 多陷阱强度升级**（deposon_v20_gt2b.json，T∈{1,2,3}，固定 4 选项）：
rule_filter 准确率 0.150/0.275/0.200，**非单调**（T=1→2 上升反转），预登记判
**inconclusive**，不判死也不支持：n=40/格下 ±1 题=±2.5pp 的波动与机会噪声同阶，
统计功效不足。场免疫判据亦被破坏：|acc_field(T)−acc_field(1)| 最大
0.625（0.375/0.525/1.000），远超 ±0.05 容差；机制是固定 4 选项设计下 T 越大图内
竞争者越少（陷阱 −inf + 3−T 个随机节点），准确率随 T 机械上升，这不是语义能力
提升，而是选项构成假象对判据的破坏（判据设计缺陷）。与题库轨锚点兼容：T=2 同种子
复现 0.275 逐点一致。定性结论「规则三档均在机会水平附近（0.15–0.275）」依旧成立。

**题库效度：field_mean 52.5% 的口径。** 题库横向验证（deposon_v20_quiz_eval.json，40 题）：llm_prior 92.5%、field_mean
52.5%、rule_filter 27.5%、random 25%；大题库扩至 157 题 × 6 域后方向全部复现
（deposon_v20_bigquiz_eval.json：prior 89.5%、ngram_tfidf 54.2% 击败 field_mean
50.9%、rule_filter 19.6% 低于机会）。

field_mean 52.5% 的口径判定为「**2 选 1 机会水平，不携带结构信号向语义任务迁移的
信息**」，依据有二：（i）机制在案：陷阱标签非图节点，field/prior 对其打 −inf
（quiz_eval records 的 note 字段逐题在案），39/40 题有效任务退化为「金边 + 1 图内
随机节点」的 2 选 1，其机会期望约 50%，52.5% 与之不可区分；按 4 选 1 机会 25% 计
的「两倍于机会」读法忽略了 −inf 机制对有效选项数的改变。（ii）GT-2B 提供独立
佐证：场准确率随图内候选数减少而机械上升（0.375→1.000），证明该通道上的场分数被
选项构成自由度主导，不构成语义迁移证据。题库轨各数字均为 n=40/格小样本口径
（±1 题=±2.5pp），宽区间解读。

**CoT 参照**（deposon_v20_cot_quiz.json）：带选项文本的直接 CoT 问答 92.5%
（40 题子集），按 CoT 轨自身口径报告。先验在题库轨的 92.5% 按题库轨自身口径报告，该口径因陷阱 −inf 退化为 2 选 1，2 选 1 期望 94.4%（文档级口径，见附录 A 降级
项）完全解释观测 92.5%。两轨口径不同，数值不作对比陈述，「先验=CoT」不作宣称。
可比口径为：CoT 92.5%（带选项文本的 4 选 1）vs 先验开放候选 top-1 67.5% /
top-3 82.5%（文档级口径，同见附录 A）。

**方向观察**（crossval `direction_kind_summary`）：族 L 四图先验边与金边方向一致率
≥0.96（抽象→具体 1.000、过程→结果 0.963），hub 反向边 = 0；在 labels-only 补全
任务设定下未观测到反转诅咒（任务难度与机制均不同于大规模预训练记忆设定，不构成
机制反驳，见 §2.3）。v1.9 锚点图上的系统性方向反转（2/9 正确）判定为该重建图
（78% 占位标签 + 特定枢纽结构）的特异现象，非普遍方向语义缺陷；方向主张保留但限
真实语义图。

### 4.4 划界推论：一条观察性分工规律（枢纽集中度与真实语义）

本节的地位是主线的**推论**而非独立贡献：§5 的博弈论证据链回答「场的可审计性是否
成立」，本节回答「它在哪些图上成立」——「hub 集中度高的图用结构信号、有真实语义
的图用语义先验」实为可审计优势价值域的划界：场结构臂与先验语义臂各有其可审计性
成立域。我们把该规律定位为**观察性规律（v0）而非判别器贡献**，理由随证据一并给出。

**探索性回归**（v20_regression_field_v2.json，n=20）：field_named ~ density +
hub_concentration + real_semantics，R²=0.628（调整 0.559，F p=0.001）；
hub_concentration β=+2.12（p=0.00028）为场效力最强相关子，real_semantics β=−0.16
（p=0.012）显著压低场表现，density 不显著（p=0.13）；VIF<4。两点限定必须随数字
同行：其一，n=20、3 预测子，小样本，标记**探索性**，v2.1 扩图后重估；其二，特征
本身是语料设计变量（S6 族就是按高枢纽构造的），用参与语料设计的特征去「预测」该
语料上的效应存在准循环性，回归系数只能说明方向性关联，不能作因果或外推解读。

**hub 轴语料外复现（GT-8）**（deposon_v20_gt8.json，预登记先于数据提交）：2 对配对
新图（N 与边数逐对对配，real_semantics=0）上，高 hub 图的场优势
（field_named−random_named）一致大于低 hub 图（对 A：+0.7917 > +0.1333；对 B：
+0.0526 > −0.0833），判定 **supports_H_GT8（2/2 同向）**。两点限定：degree
基线在两高 hub 图上饱和（degree_named=1.0000，field 相对 degree 的差为 0.0 与
−0.9474）；hub 轴鉴别的是**结构信号整体可利用性**而非场独有优势；B_low 上场被
random 反超（单图小样本波动）。功效说明：2 对配对只能分辨极大效应（对 A 差
0.66），对 B 量级（约 0.14）的差已接近该设计的分辨极限；要分辨 0.1 量级的 diff
差异，按观察到的图间方差粗估需 ≥6–8 对配对图，列为 v2.1 排期。

**real_semantics 轴语料外复现（GT-8b）**（deposon_v20_gt8b.json，预登记先于数据，
含一次先于重试的预算修正登记）：chinese_dynasties 域满足预登记阈值：先验
named Hits@3 0.7805，远高于 field 0.0732、random 0.0244、degree 0.0488
（先验−场 = +0.7073）；chemical_elements
域图生成成功但先验臂取数失败（连续尝试全部超时/空响应，HTTP 预算 9 次用尽后按
预登记记 fetch_failed，不计入判定分母）。有效域 1 < 2，机械判定 **inconclusive**。
方向性观察（非结论）：唯一有效域上先验大幅领先，与族 L 既有 4 图模式（先验
0.484–1.000 全部显著高于 field/random）同向。两点限定：其一，取数失败可能与
先验任务难度相关（元素周期类标签触发更长推理），若是，则「唯一有效域上先验领先」
存在幸存者偏差，本设计无法区分网络事故与难度相关失败；其二，0.6/0.2 阈值为预登记
工作阈值，非统计显著性检验。该域先验臂留待后续预算窗口补取。

**规律表述与适用边界**：hub_concentration 高 → 结构信号（场与 degree 同场竞技）
可用；real_semantics=1 → 用语义先验。结构分支应理解为「结构信号整体」而非场独占
（§6 的 BOSS 基线证据同向）；语义分支目前只有一个新域的方向性证据，inconclusive
在案。

## 5. Game-Theoretic Evidence（可审计优势的博弈论实证，核心节）

本节是本文主线：对 1.9 可审计性命题的动力学层实证，按四步组织——命题承接
（§5.1，1.9 命题的动力学化）→ 审计标量存在性（§5.2/§5.3，GT-5b 单调性与 GT-6
非势残差）→ 审计定量化（§5.4，分布级 PoA）→ 审计边界（§5.5，GT-7 温度前沿）。
**全节采用 consistency 口径，此口径不放松**：以下证据与势博弈解读一致，是一致性
证据而非形式化证明；除已闭合的预登记判定（GT-5b、GT-6）外，不声称证明了任何定理。

### 5.1 命题承接（1.9 → 动力学化）与建模选择

1.9 命题说守恒账使每条路径可审计；本节把它动力学化：若反向演化存在一个势标量，
则整条轨迹可审计为势下降，审计从逐步合规检查升级为整体可复核的标量账。建模上，
把每条留一预测边视为一个玩家，策略为候选目标节点，效用为场得分；确定性均值场
反向对应无噪声最好响应动态；物理能量的负值 $\Phi=-E$（$E$ 见 §3.1）是势函数候选。
「每个任务是独立玩家」的分解是建模选择而非唯一；$\Phi=-E$ 有解析依据（反向退火梯度
即 $-\nabla E$）。Sandholm（2010）[3] 群体最好响应流为该对应提供最近理论支点。

### 5.2 证据矩阵（六条，按判定强度三档标注）

判定列分三档：✅ 闭合（预登记判定通过）、🟡 受限一致（方向一致但有口径限定）、
❌ 弱一致或未决（鉴别力低或 inconclusive）。六条证据汇总于表 1。

**表 1：博弈论证据矩阵（六条证据，判定按强度三档标注）**

| 证据 | 实验 | 结果 | 判定 |
|---|---|---|---|
| ① 噪声动态劣于确定性极限（命中率口径） | GT-1 | dirichlet 均值 0.10 vs mean-field 0.40，gap=0.30 ≥ 0.2，20/20 运行严格劣 | ❌ 弱一致：任何噪声劣化都满足此模式，鉴别力低，仅作背景一致性 |
| ② 势函数轨迹单调不减 | GT-5b（收窄预登记） | 22/22 图 mean-field Φ 轨迹单调率=100%（预登记线 ≥80%，斩杀线 0 触发） | ✅ 闭合（supports_narrowed_monotonicity） |
| ③ 场有协调价值（分布级 PoA） | GT-4 | 全 17 张有限值图 median PoA=1.333 > 1.2（族 S 子集 13 图 median 1.5，见 §5.4）；族 L 2 图 PoA<1 并列披露 | 🟡 受限一致（操作化口径与经典 PoA 不同度量，§5.4） |
| ④ 规则防御被自适应攻击瓦解、场机制性免疫 | GT-2 | evasion=1.0；场塌陷 −0.0pp；主协议判定 no_separation | 🟡 受限一致（no_separation：攻击强度未达决定性，不升级为防御失效主张） |
| ⑤ 信号优势跨厂商稳健 | GT-3b | 三模型族 0 败绩、全 ok 域 W=1.0 | 🟡 受限一致（与势博弈解读无直接推论关系，列为分工叙事的稳健性证据；中文优化族残余局限） |
| ⑥ 非势残余 | GT-6 | 边效用向量向梯度空间投影，残余中位数 ≈1.6e-29 < 0.10 预登记线 | ✅ 闭合（potential_game_explanation_complete；3 图例外与数值精度说明见 §5.3） |

### 5.3 审计标量存在性：意外、例外与数值精度

GT-5 的终点条件未通过并判 inconclusive（不回溯改写）：3/4 图上 dirichlet 噪声臂
终点 Φ 高于 mean-field（S6 gap=−0.31）。解读：噪声在命中率上有害（GT-1），在全局
势上却有益：噪声是探索者、mean-field 是利用者，与 log-linear learning（Blume
1993 [50]）和确定性最好响应的经典分工一致；散射层的「温度」（噪声强度）由此获得博弈
论语义而非调参旋钮。收窄后的单调性主张由新版预登记 GT-5b 闭合（22/22），终点
反转保留于案。

GT-6 有 3 张循环结构图残余越线：S4=0.148、L_algorithm_process=0.136、S5=0.121，
其上势解释为近似。另需说明数值精度口径：中位残余 1.6e-29 处于双精度浮点下溢
量级，反映的是「边效用向量几乎完全落在梯度子空间内」这一结构性事实（投影归一化
后的相对残余），不应按绝对量级解读为物理量；3 张例外图的 0.12–0.15 残余才是有
信息量的非势分量。本分解是 Candogan 流分解 [4] 的可操作类比（分解边效用向量，未沿
轨迹积分）。

### 5.4 审计的定量化：PoA 的口径限定

PoA 只作分布级报告：操作化定义 $\mathrm{PoA}=\mathrm{field\_mean}/\max(\text{自利臂})$，自利臂集 $\{\mathrm{random},
\mathrm{degree}\}$（预登记的 llm_prior 臂在族 S 不可得，分母只可能更小、PoA 只可能偏大，
如实披露）。**主报全 17 张有限值图口径：median PoA=1.333 > 1.2 预登记线**；族 S
子集 13 张有限值图 median 1.5 作为补充口径并列；3 张 PoA=∞ 单独计数（自利臂
named=0 而场>0）。该度量与经典 worst-case-NE/社会最优比值不是同一度量，成本结构
仿射/可分前提未闭合；均衡效率的经典分析见 [12]，分布级 PoA 报告的口径先例见 [13]。子集中位数与 Pigou 4/3 的数值接近仅为巧合，不主张实例级
复现，全 17 图口径 1.333 亦低于 4/3。族 L 2 张图 PoA<1（L_historical 0.5、
L_physics 0.75）；场在语义域为负协调，与分工叙事自洽：场只在结构域创造协调
价值，势博弈解释的适用域与分工边界一致，理论不自相矛盾。

### 5.5 审计边界：温度前沿（GT-7）

GT-7 温度前沿判 mixed：α∈{0.3,…,20} × 4 图 × 5 seed。GT-5 反转可复现且系统化
（同 3/4 图高温档终点 Φ > mean-field，Φ 增益集中在高温端，corr −0.87），温度确实
控制全局势探索收益；但「双赢前沿」不成立（S6 高温档 Φ 升而命中率 0.4→0.08），
势与命中率是两个目标，本文不暗示升温既提势又提质。边界情形披露：命中率=0 的图
（L_physics）使条件退化恒真，未回溯改规则。对审计主线的含义：审计承诺只覆盖势
这一本账——温度不能同时改善势与命中，审计边界由此划定。

### 5.6 守恒账与机制设计

守恒账（运行期逐实例不变量）定位为机制设计中的承诺装置（§2.6 空层），GT-2 实证
其必要性：规则防线在自适应攻击下渗漏（题库轨 27.5%，与机会不可区分），而机制性
免疫（不读标签）的臂不受影响。小图类「均值场反向=无噪声最好响应动态」的形式化
命题尚未补齐；补齐前本节维持 consistency 口径。

## 6. Discussion & Boundary（边界与讨论）

本节限定的是划界推论（§4.4）的成立范围，并集中交代方法学局限与随稿交付的工程工件；主线结论（§5 的审计标量存在性与定量化）的口径限定已在各节随行给出。

### 6.1 成立域与边界

场的成立域在 H-A1 判死后收缩为「相对平凡结构基线的稳健优势 + 高枢纽图局部优势」。
H-B1 两例违规（L_algorithm_process 0.158、L_historical_causality 0.344）显示汇聚
偏置与因果链结构反对齐；绝对命中率随结构否定大幅塌缩，「场=通用骨架检测器」已被
本设计自身否定。先验的结论限真实语义小图（30–45 节点 DAG）；跨厂商检验后同源
污染的口径为「实质性削弱、中文优化族残余局限」（doubao 4/4、deepseek 6/6、0 败绩、
W=1.0；三族均为中文优化大模型，共享中文语料不可排除）。

结构域内场并非无对手：ngram_tfidf 在大题库击败 field_mean（54.2% vs 50.9%），
L_project_management 上 PA/n2v/tfidf 三臂同图击败场（margin 6 边）。因此分工规律
的结构分支应理解为「结构信号整体」的可利用性，而非场独占。规模扫描未检出相变点；
质变发生在 n=1→n=20 的语料化而非 N 增长。

### 6.2 分工规律的适用范围

分工规律（§4.4）的适用范围需逐项限定：回归为 n=20 探索性且存在特征-设计循环性；
hub 轴语料外复现仅 2 对、方向-only，且鉴别的是结构信号整体而非场独有优势；
real_semantics 轴复现判 inconclusive（单有效域方向性证据 + 幸存者偏差风险在案）。
不外推至族 L 之外任务或更大规模图。

### 6.3 方法学局限

两条方法学局限单列。其一，族 L 图由单一厂商 LLM（Kimi 系）生成；评估者跨厂商
问题已由 GT-3b 处理，但图生成器单一厂商的问题未闭合；人工标注图被公认为最彻底
检验，尚未排期。其二，题库轨 n=40/格（±1 题=±2.5pp）与机会噪声同阶，该轨全部
数字按小样本宽区间解读。理论空位表述统一为「尚未发现」的阴性口径（未附可审计
检索协议，列为投稿前待办），不宣称排他性空白。

### 6.4 方法论工件

本文还交付一套科研工程工件，作为可审计性贡献本身。全部写作过程元信息（内部
裁定、修订编年）集中收于本小节与 paper/v2/REVISION_LOG_v2X.md（过程工件，非论文正文），正文叙事只陈述最终口径。

- **预登记与修正案**：SPEC_v2.0.md、SPEC_v2.0_amendment1.md、SPEC_GT2B/GT3/GT8/
  GT8B；判死规则先于数据冻结，判定由脚本机械读取结果 JSON（kill_lines 类字段强制
  对照已列入 verifier v21）。
- **独立多角色评审与裁定史**：M1–M5 主线裁定与 m1–m7 细则闭合于
  reviews/review_coach_v2X_outline.md；corrections 文档记录了两次高严重度口径更正
  （C1：H-A1 斩杀线触发后头条判死的落实；C2：「先验=CoT」宣称的撤回与题库 2 选 1
  退化口径的确立，§4.3 的最终口径即由此而来）；20→22 图快照漂移归档于
  corrections E1。
- **阴性结果归档**：相变阴性、GT-5 反转、GT-2B inconclusive、GT-7 mixed、
  no_separation、GT-8b inconclusive 全部如实呈现，不美化、不回溯改写。
- **工程**：内容寻址缓存（sha256 + prompt 哈希 + attempts 落盘）、语料快照 sha
  钉定、断点续传幂等设计、版本化 verifier（冻结文件走 erratum 不覆写）、全套
  pytest（最新批次 255 passed 无回归）。
- **教训复盘**（corrections §D）：「文档手写 vs 数据机械」是最富矿 bug 类别；单位
  与截断是第二富矿；冻结数据可信、散文不可信。

## 7. Conclusion（结论）

本节总结全文并给出 Limitations。本文把前序工作「可审计表征与守恒保证」的价值命题推进到动力学层：在同一预登记协议与 22 张受控概念图上，反向动力学被建模为图上势博弈，势轨迹全图单调不减、非势残差中位近零（例外在案），每步演化可审计为势下降；分布级 PoA 把「自利动力学离协调最优多远」变为可计算量；温度前沿划定审计边界——升温只提势探索不兼提命中率。两臂可审计性成立域互不重叠的划界推论，以观察性规律随证据一并给出。

### 7.1 Limitations

本工作的主要局限有四（详述见 §6）：其一，consistency 口径——除已闭合的预登记判定（GT-5b、GT-6）外，证据为一致性证据而非形式化证明，「均值场反向=无噪声最好响应动态」的小图类形式化命题尚未补齐；其二，族 L 图由单一厂商 LLM 生成，非中文模型族与人工标注图的检验仍为开放局限；其三，题库轨 n=40/格，与机会噪声同阶，全部数字按小样本宽区间解读；其四，划界规律的证据为探索性回归与 2 对配对复现，real_semantics 轴判 inconclusive，不外推至族 L 之外任务或更大规模图。

未来工作：KGE 可训练基线（v2.1 排期）、扩图后重估探索性回归、≥6–8 对配对图的 hub 轴功效升级，以及上述形式化命题的补齐。

## References（参考文献）

> 占位稿，正式版以 bib 落库；[待核] 标注保留于条目上。

[1] Monderer & Shapley, GEB 1996（势博弈）。
[2] Rosenthal 1973（拥塞博弈）。
[3] Sandholm 2010（群体最好响应流）。
[4] Candogan et al., MOR 2011（博弈流分解）。
[5] Parise & Ozdaglar, Econometrica 2023（graphon 极限）。
[6] Jackson & Wolinsky 1996。
[7] Fabrikant et al. 2003。
[8] Ma et al., TCS 2014。
[9] Waniek et al., Nat. Hum. Behav. 2018 及 Stackelberg 边隐藏 2023。
[10] Koutsoupias & Papadimitriou 1999。
[11] Roughgarden & Tardos 2002（仿射拥塞 PoA=4/3）。
[12] Christodoulou et al. 2014。
[13] Benita 2020（分布级 PoA 先例）。
[14] Conitzer & Sandholm 2006。
[15] Dekel et al. 2010。
[16] Hardt et al. 2016。
[17] Dütting et al., WWW 2024。
[18] Raji et al. 2020。
[19] Jia et al. 2021（Proof-of-Learning）。
[20] Tramèr et al., NeurIPS 2020（自适应攻击）。
[21] Nasr et al., USENIX Sec [待核：年份需核实，应为 2025 或 in-press]。
[22] Gröndahl et al., AISec 2018。
[23] Hosseini et al. 2017。
[24] Kahu & Ahuja 2025。
[25] Jain et al. 2023。
[26] HateBench, USENIX Sec 2025。
[27] KICGPT, Findings of EMNLP 2023。
[28] KG-LLM/Yao et al., ICASSP 2025。
[29] Wadhwa et al., ACL 2023。
[30] Berglund et al., ICLR 2024（Reversal Curse）。
[31] Wang & Sun, ICLR 2026。
[32] MKGL, NeurIPS 2024。
[33] Zhang et al., ACL 2025。
[34] Novak & Cañas 2008。
[35] Ruiz-Primo & Shavelson 1996。
[36] KnowEdu, IEEE Access 2018。
[37] MOOCCube/MOOCCubeX, ACL 2020 / CIKM 2021。
[38] Pinandito et al. 2021（KitBuild）。
[39] Ma & Chen, LAK 2025。
[40] Lipton & Steinhardt, CACM 2019。
[41] Dodge et al., EMNLP 2019。
[42] Recht, ICML 2019。
[43] Tevet & Berant, EACL 2021。
[44] D'Amour et al., JMLR 2022。
[45] Lazaridou et al., NeurIPS 2021。
[46] Schaeffer et al., NeurIPS 2023。
[47] Mallen et al., ACL 2023。
[48] Dziri et al., NeurIPS 2023。
[49] Bowman, ACL 2022（Dangers of Underclaiming）。
[50] Blume 1993（log-linear learning）。
[51] Deposon 1.X 论文（v1.9 冻结稿），前序工作。
[52] McPherson, Smith-Lovin & Cook 2001（同质性综述）[待核：条目需文献核实]。
[53] Pei et al., Geom-GCN, ICLR 2020 [待核：条目需文献核实]。
[54] Zhu et al., H2GCN（Beyond Homophily）, NeurIPS 2020 [待核：条目需文献核实]。
[55] Zheng et al., 异配图 GNN 综述, 2022 [待核：条目需文献核实]。
[56] Luan et al., Revisiting Heterophily, NeurIPS 2022 [待核：条目需文献核实]。
[57] Zhang & Chen, SEAL, NeurIPS 2018 [待核：条目需文献核实]。
[58] Srinivasan & Ribeiro, 位置嵌入与结构表示等价性, ICLR 2020 [待核：条目需文献核实]。
[59] Mao et al., Demystifying Structural Disparity, NeurIPS 2023 [待核：条目需文献核实]。

## Appendix（附录）

### 附录 A：数字机械追溯清单

| 数字 | 出处（JSON 路径与字段） |
|---|---|
| H-A1 判死 | `deposon_v20_corpus_eval.json` → `verdicts.kill_lines.H_A_dead.triggered=true` |
| p=0.0118（22 图，16+/4−/2 平） | 同上 → `verdicts.H_A1_field_mean_gt_random.sign_test.p_exact=0.011818` |
| 反转 4 图 | 同上 → `verdicts.kill_lines.H_A_dead.reversals_vs_random`（4 项：L_historical_causality、L_physics_concepts、L_project_management、S2_n45） |
| field>degree p=4.0e-5（19+/1−/2 平） | 同上 → `verdicts.H_A2_field_mean_gt_degree.sign_test.p_exact=4.005e-05` |
| S6 族 0.471 / 锚点 0.470588 | 同上 → `verdicts.H_S6_anchor_reproduction.S6_named_hits3=0.470588` |
| 反转图超几何 p=0.187 / 族 L 富集 p=0.046 | 本文现算（scipy hypergeom，附录 E）；输入：语料 22 图（`corpus/v20/index.json`）、反转 4 图（同上字段）、复合类构成 6 张族 L + 9 张 S1/S2（语料设计最大入度=1 子族） |
| OLS β=2.12 / p=0.00028 / n=20 / R²=0.628 | `v20_regression_field_v2.json` → `coefficients.hub_concentration`（coefficient 2.1177, p_value 0.000279）、`n_observations=20`、`r_squared=0.628226` |
| 先验 named Hits@3 0.484–1.000（四图逐值），同图臂 ≤0.22 | `deposon_v20_crossval.json` → `prior_arm_eval.*.llm_prior.named`（0.4839–1.0） |
| CoT 92.5% | `deposon_v20_cot_quiz.json` → `overall_cot_accuracy=0.925` |
| 先验开放 top-1 67.5% / top-3 82.5%、2 选 1 期望 94.4% | `docs/Findings_v2.0_corrections.md` C2（开放候选实测口径；**文档级**，results/ 下无独立 JSON 字段） |
| no_separation / −7.5pp（三图 −10pp、第四图 0pp） | `deposon_v20_crossval.json` → `gt2_verdict.rule_collapse_mean_pp=0.075`、`verdict="no_separation_adaptive_attack_not_decisive"`；per_graph rule 0.1/0.0/0.1/0.1 |
| 题库轨 rule 27.5% / field 52.5% / prior 92.5% / random 25% | `deposon_v20_quiz_eval.json` → `overall`（0.275/0.525/0.925/0.25） |
| evasion 100% | `deposon_v20_crossval.json` → `gt2_attacker_meta.*.evasion_rate=1.0` |
| GT-1 gap 0.30、20/20（0.10 vs 0.40） | `deposon_v20_gt.json` → `GT1_potential_game_convergence.verdict`（gap=0.30, n_runs_below_meanfield=20） |
| GT-5b 22/22 | `deposon_v20_gt5b.json` → `per_graph_summary.*.meanfield_monotone_rate=1.0`（22 图） |
| GT-5 终点反转 S6 gap=−0.31（3/4 图 inconclusive） | **文档级**：`docs/GT_RECONSTRUCTION.md` §2（results/ 下无 `deposon_v20_gt5.json`，历史结果保留在案；标注方式与 GT-7 corr −0.87 文档级条目对齐） |
| GT-6 残余中位 ≈1.6e-29、3 例外 | `deposon_v20_gt6.json` → `verdict.median_residual_ratio=1.594e-29`；例外 `per_graph_summary.*.residual_ratio_mean`（S4 0.148 / L_algorithm_process 0.136 / S5 0.121） |
| GT-7 mixed、corr −0.87、S6 0.4→0.08 | `deposon_v20_gt7.json` → `per_graph`（hits/Φ 走向支持；corr −0.87 为文档汇总值，叙事锚 GT_RECONSTRUCTION §7） |
| PoA median 1.333（全 17 有限值图）/ 1.5（族 S 13 图）；族 L PoA<1（0.5、0.75）；∞×3 | `deposon_v20_gt.json` → `GT4_price_of_anarchy.verdict.poa_per_graph_finite`（族 S 13 项中位 1.5，全 17 项中位 1.333；`L_historical_causality=0.5`、`L_physics_concepts=0.75`；∞ 3 张单独计数） |
| GT-8 2/2 同向（对 A +0.7917>+0.1333；对 B +0.0526>−0.0833；degree 饱和 diff 0.0/−0.9474） | `deposon_v20_gt8.json` → `verdict.verdict="supports_H_GT8"`、`pairs_concordant`（2 对）、`per_pair.*` |
| GT-8b inconclusive；chinese_dynasties 0.7805 vs 0.0732/0.0244/0.0488；+0.7073/+0.7561 | `deposon_v20_gt8b.json` → `gt8b_verdict`（verdict="inconclusive"、n_valid_domains=1、min_domains=2）、`per_domain.L_chinese_dynasties.named_summary`（llm_prior 0.7805 / field_mean 0.0732 / random 0.0244 / degree 0.0488）、`per_domain.L_chinese_dynasties.prior_named_minus_field_named=0.7073`、`per_domain.L_chinese_dynasties.prior_named_minus_random_named=0.7561` |
| GT-8b fetch_failed（9 次 HTTP 预算用尽） | `docs/Findings_GT8B.md` §3–§4；`deposon_v20_gt8b.json` → `cache_missing`（prior_chemical_elements.json 缺失在案） |
| GT-2B 0.15/0.275/0.20 inconclusive；场 0.375/0.525/1.000 | `deposon_v20_gt2b.json` → `verdict="inconclusive"`、`per_T.*.per_domain.*.accuracy` 聚合 |
| GT-3b doubao 4/4、deepseek 6/6、0 败绩、W=1.0 | `deposon_v20_gt3.json` → `verdict.H_GT3_supported=true`、顶层 `kendall_W=1.0`（位于 `verdict` 之外）；逐域矩阵见 `docs/Findings_GT3.md` |
| Wilcoxon p=0.0031 / \|r\|=0.83；配对 t p<0.0001 / d=2.05 | `v20_statcheck_fm_vs_rand.json`（p_value=0.003052）、`v20_statcheck_fm_vs_deg.json`（p_value=2.13e-08, d=2.0478） |
| 大题库 89.5%/54.2%/50.9%/19.6% | `deposon_v20_bigquiz_eval.json` → `overall`（prior 0.8947、tfidf 0.5417、field 0.5091、rule 0.1964） |
| 方向一致率 ≥0.96、hub 反向 0 | `deposon_v20_crossval.json` → `direction_kind_summary`（1.0 / 0.9627，total_hub_reversed=0） |
| 融合稀释（0.484→0.452、0.783→0.739） | `deposon_v20_crossval.json` → hybrid λ=0.5 档 `hybrid_lambda_convex=0.5` 逐图字段 |

### 附录 B：基线注册表（摘要）

A 族结构启发式六臂 + degree + random（同协议 20 图实测）；B 族浅近似 Node2Vec
（标注为非完整实现）；C 族直接 CoT 强基线（92.5%）；潜伏强基线披露门槛 margin
≥3 金边（门槛后 6 事件，含 L_project_management 三臂同图击败场）。完整注册表见
docs/BASELINE_REGISTRY.md。

### 附录 C：缓存 provenance 与预算

族 L 获取、先验臂、GT-2 攻击者、GT-3 五评估者、GT-8b 两域全部缓存内容寻址
（prompt_sha256 在案、attempts 落盘）；各轮 API 消耗与预算例外如实登记于各
Findings 与修正案（GT-8b 总 HTTP=9，恰达修正后预算上限，未超支；fetch_failed
域缺失文件清单逐字写入结果 JSON 的 cache_missing 字段）。

### 附录 D：图（待中文版制作）

按 paper/FIGURE_LANGUAGE_POLICY.md，本稿为中文稿只引用中文图；下列图仅有英文版或
尚未绘制，初稿一律以文字表格替代，正式版补绘中文版（命名 `_cn` 后缀）：

1. 图 1：分工边界总览（22 图场-先验胜负地图），图待中文版制作。
2. 图 2：H-A1 斩杀线与反转图分布（22 图符号检验散点），图待中文版制作。
3. 图 3：分工规律散点（hub_concentration × real_semantics 着色 field_named），图待中文版制作。
4. 图 4：GT-7 温度前沿逐图形态（hits 与 Φ 双轴），图待中文版制作。
5. 图 5：分布级 PoA 全 22 图条形（含 PoA<1 两图与 ∞ 计数），图待中文版制作。

### 附录 E：反转图富集检验（可复算）

§4.1 的两个单边超几何检验用 scipy 现算，输入全部为冻结字段（语料清单
`corpus/v20/index.json`、反转图清单 `deposon_v20_corpus_eval.json`
`verdicts.kill_lines.H_A_dead.reversals_vs_random`）：

```python
from scipy.stats import hypergeom
# 检验一（复合类）：N=22 图；K=15（real_semantics=1 的 6 张族 L
#   ∪ 语料设计中最大入度=1 的无枢纽子族 S1/S2 共 9 张）；n=4 张反转图
p_composite = hypergeom.sf(3, 22, 15, 4)   # P(X>=4) = 0.1866，未达显著
# 检验二（族 L 富集，补充）：K=6（族 L）；4 张反转中 3 张在族 L
p_familyL  = hypergeom.sf(2, 22, 6, 4)     # P(X>=3) = 0.0458，边界显著
```

结论：复合类检验不显著 ⇒ 「斩杀线触发即边界直接证据」降级为与边界假设一致的
事后方向性观察（§4.1）。

---
修订记录见 paper/v2/REVISION_LOG_v2X.md（过程工件，非论文正文）
