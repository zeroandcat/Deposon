# Deposon v2.X 文献侦察报告 A：物理约束扩散场 × 博弈论重构

**侦察员**：Agent A（文献方向）
**检索工具**：scholar 插件（Google Scholar 类检索，结果存于 `reviews/data/*.csv`）+ web_search 交叉核实
**核实原则**：以下条目全部来自真实检索结果（scholar 命中或 arXiv 论文参考文献列表中的规范引用），DOI 仅收录在检索结果中亲眼见到的。个别线索标「未核实」。Scholar 返回的 2026 年条目多为预印本/低可见度 venue，原则上不收入主表。
**图例**：[经典] = 奠基性/高被引文献；[近3年] = 2023 及以后。

---

## 主题 1：势博弈与图上的学习动态（理论锚点）

**用途**：为「确定性反向扩散（mean-field）= 无噪声最好响应动态，收敛于势函数极值」提供理论锚。

1. **Potential Games** — D. Monderer, L. S. Shapley, 1996, *Games and Economic Behavior* 14(1):124–143. [经典]
   势博弈奠基文献：纯纳什均衡存在、有限改进性质（FIP）保证最好/更优响应动态收敛到势函数局部极值。我们「反向场 = 势函数上升流」的第一锚点。
   DOI: 10.1006/game.1996.0044
2. **A Class of Games Possessing Pure-Strategy Nash Equilibria** — R. W. Rosenthal, 1973, *International Journal of Game Theory* 2(1):65–67. [经典]
   拥塞博弈源头（Rosenthal 势函数），所有拥塞博弈是势博弈；边-资源代价结构与图上扩散重构直接类比。（经多篇 arXiv 参考文献列表核实引文；DOI 未核实）
3. **The Statistical Mechanics of Strategic Interaction** — L. E. Blume, 1993, *Games and Economic Behavior* 5(3):387–424. [经典]
   逻辑特（logit）响应 → 吉布斯测度，噪声→0 时质量集中于势函数极大点。这是「有噪声扩散采样 ↔ 无噪声最好响应」极限关系的最早博弈论表述。
4. **The Evolution of Conventions** — H. P. Young, 1993, *Econometrica* 61(1):57–84. [经典]
   带小扰动的最好响应动态的随机稳定性分析框架（KMR/Young 传统），支撑「噪声退火 → 均衡选择」叙事。DOI: 10.2307/2951778
5. **Revisiting Log-Linear Learning: Asynchrony, Completeness and Payoff-Based Implementation** — J. R. Marden, J. S. Shamma, 2012, *Games and Economic Behavior* 75(2):788–808. [经典]
   对数线性学习在势博弈中收敛到势函数最大化者的严格刻画；「噪声最好响应 → 势极值」最常被引的现代版本。
6. **Population Games and Evolutionary Dynamics** — W. H. Sandholm, 2010, MIT Press. [经典（专著）]
   大群体极限下最好响应动态是确定性 ODE（mean-field），势博弈中该 ODE 是势函数的梯度流——与我们 mean-field 反向场论证几乎逐条对应。
7. **Flows and Decompositions of Games: Harmonic and Potential Games** — O. Candogan, I. Menache, A. Ozdaglar, P. A. Parrilo, 2011, *Mathematics of Operations Research* 36(3):474–503. [经典]
   把博弈分解为图上「势分量 + 调和分量」（Hodge 分解）——用图流/扩散语言刻画博弈，是「扩散场 × 势函数」最直接的形式化先例。DOI: 10.1287/moor.1110.0500
8. **Sink Equilibria and Convergence** — M. Goemans, V. Mirrokni, A. Vetta, 2005, FOCS, pp. 142–151. [经典]
   最好响应动态不收敛时（非势博弈）如何度量动态吸引子的效率；为我们「确定性反向收敛性失败模式」提供对照文献。
9. **Graphon Games: A Statistical Framework for Network Games and Interventions** — F. Parise, A. Ozdaglar, 2023, *Econometrica* 91(1):191–225. [近3年]
   大网络博弈的 graphon（连续极限）框架：有限图上的纳什均衡收敛到 mean-field 极限均衡——「图上博弈的场极限」的当代标准文献。DOI: 10.3982/ECTA17564
10. **Characterizing the Convergence of Game Dynamics via Potentialness** — M. Bichler, D. Legacci, P. Mertikopoulos 等, 2025, arXiv:2503.16285（TMLR 投稿状态，见交叉引用）。 [近3年]
    以「离势博弈多远」参数化各类学习动态的收敛性，可引用为我们收敛性主张的边界条件。
    链接: https://arxiv.org/abs/2503.16285

**PageRank/扩散交叉线索（补充）**：S.-H. Teng, *Network Essence: PageRank Completion and Centrality-Conforming Markov Chains*, 2017（Springer 文集章节，arXiv:1708.07906）——把 PageRank 补全与马尔可夫链中心性联系起来，是「链接预测/图补全 × PageRank 扩散」少见的直接桥梁。另有 Hopcroft & Sheldon「Network Reputation Games」（PageRank 操纵博弈，约 2008 手稿）**[未核实]**，检索中仅见二手提及，建议需要时向 eCommons/Cornell 核实。

---

## 主题 2：博弈论视角的链接预测 / 图补全

**用途**：把边预测建模为博弈或对抗过程的相关工作定位。

1. **A Strategic Model of Social and Economic Networks** — M. O. Jackson, A. Wolinsky, 1996, *Journal of Economic Theory* 71(1):44–74. [经典]
   战略网络形成奠基文献：pairwise stability = 「哪些边存在」的均衡概念，可表述「图补全 = 网络形成博弈的均衡求解」的世界观。DOI: 10.1006/jeth.1996.0108
2. **On a Network Creation Game** — A. Fabrikant, A. Luthra, E. Maneva, C. H. Papadimitriou, S. Shenker, 2003, PODC, pp. 347–351. [经典]
   单边付费建边博弈，把「补全一条边」显式建模为成本-收益决策；网络形成博弈 PoA 研究起点。
3. **A Game-Theoretic Framework to Identify Overlapping Communities in Social Networks** — W. Chen, Z. Liu, X. Sun, Y. Wang, 2010, *Data Mining and Knowledge Discovery* 21(2)（Springer）。 [经典]
   把社区发现（隐含补全）表述为局部均衡搜索的博弈；均衡刻画与算法一体。链接: https://link.springer.com/article/10.1007/s10618-010-0186-6
4. **Mining Hidden Links in Social Networks to Achieve Equilibrium** — H. Ma, Z. Lu, D. Li, Y. Zhu, L. Fan, W. Wu, 2014, *Theoretical Computer Science*（Elsevier）。 [经典]
   直接把「挖掘隐藏链接」表述为达均衡过程——与本论文「补全=均衡重构」定位最接近的早期工作之一。链接: https://www.sciencedirect.com/science/article/pii/S0304397514006136
5. **Hiding Individuals and Communities in a Social Network** — M. Waniek, T. P. Michalak, M. J. Wooldridge, T. Rahwan, 2018, *Nature Human Behaviour* 2(2):139–147. [经典]
   「链接预测的对手」视角：节点战略性增删边以躲避链路预测/社区检测，是边预测作为对抗博弈的高显示度代表作。DOI: 10.1038/s41562-017-0290-3
6. **Adversarial Attacks on Neural Networks for Graph Data (Nettack)** — D. Zügner, A. Akbarnejad, S. Günnemann, 2018, KDD, pp. 2847–2856. [经典]
   图结构对抗扰动开山作：攻击者编辑边以操纵 GNN 预测；边级攻击-防御循环可视为零和图博弈。DOI: 10.1145/3219819.3220078
7. **Target Defense Against Link-Prediction-Based Attacks via Evolutionary Perturbations** — S. Yu, M. Zhao, C. Fu, J. Zheng, H. Huang 等, 2019, *IEEE Transactions on Knowledge and Data Engineering*。 [经典]
   防御方以少量扰动边反制基于链路预测的隐私攻击——攻防对抗的边预测博弈。链接: https://ieeexplore.ieee.org/abstract/document/8792200/
8. **A Node Representation Learning Approach for Link Prediction in Social Networks Using Game Theory and K-Core Decomposition** — E. Nasiri, A. Bouyer, E. Nourani, 2019, *The European Physical Journal B*（Springer）。
   把节点当玩家、用博弈采样策略做链路预测的表示学习——「博弈论链接预测」最直接命中的应用型文献。链接: https://link.springer.com/article/10.1140/epjb/e2019-100225-8
9. **Time-Aware Gradient Attack on Dynamic Network Link Prediction** — J. Chen, J. Zhang, Z. Chen, M. Du, Q. Xuan, 2021, *IEEE TKDE* 35(2):2091–2102.
   对动态网络链路预测的梯度攻击；把时序维度加入边预测对抗博弈。
10. **Hiding from Centrality Measures: A Stackelberg Game Perspective** — M. Waniek, J. Woźnica, K. Zhou 等, 2023, *IEEE TKDE*。 [近3年]
    显式 Stackelberg 博弈（隐藏者先行、探测者跟随）刻画结构隐藏 vs 链路预测——「边预测 = 序贯博弈」的最新代表。链接: https://ieeexplore.ieee.org/abstract/document/10103670/

**空位观察**：既有工作要么是「边存在性=均衡」（1–4），要么是「边预测攻防对抗」（5–10）；尚无人把**生成式图补全过程本身**写成带势函数的场上博弈（参与者=节点/边候选，动态=最好响应流）。这正是我们的切入点。

---

## 主题 3：机制设计与可审计 AI（守恒账 = 承诺装置）

1. **Computing the Optimal Strategy to Commit to** — V. Conitzer, T. Sandholm, 2006, ACM EC, pp. 82–90. [经典]
   「承诺」的计算理论奠基：先动承诺严格优于同时行动——我们把守恒账定位为承诺装置时，这篇是「承诺价值」的标准引用。
2. **Incentive Compatible Regression Learning** — O. Dekel, F. Fischer, A. D. Procaccia, 2010, *Journal of Computer and System Sciences* 76(8):759–777. [经典]
   激励兼容 ML 的早期理论：当数据由策略性主体提供时如何让学习规则说真话。DOI: 10.1016/j.jcss.2010.03.003
3. **Strategic Classification** — M. Hardt, N. Megiddo, C. Papadimitriou, M. Wootters, 2016, ITCS, pp. 111–122. [经典]
   分类器与被分类者的 Stackelberg 博弈；incentive-aware ML 的标志性文献。
4. **Optimal Auctions Through Deep Learning (RegretNet)** — P. Dütting, Z. Feng, H. Narasimhan, D. C. Parkes, S. S. Ravindranath, 2019, ICML, pp. 1706–1715；期刊版 *Journal of the ACM* 71(1):1–53, 2024. [经典]
   用神经网络做自动化机制设计（近似激励兼容）——「可微经济学」路线，说明机制约束可以嵌入训练目标（与我们把守恒约束嵌入重构目标同构）。
5. **Incomplete Contracting and AI Alignment** — D. Hadfield-Menell, G. Hadfield, 2019, AAAI/ACM AIES, pp. 417–422.
   把 AI 对齐表述为人-AI 之间的不完备契约问题；为「算法内承诺/契约装置」提供概念框架。
6. **Closing the AI Accountability Gap: Defining an End-to-End Framework for Internal Algorithmic Auditing** — I. D. Raji 等, 2020, ACM FAT*, pp. 33–44. [经典]
   内部算法审计的端到端框架；守恒账作为「可审计内部工件（artifact）」挂接此脉络。DOI: 10.1145/3351095.3372873
7. **Proof-of-Learning: Definitions and Practice** — H. Jia, M. Yaghini, C. A. Choquette-Choo, N. Dullerud, A. Thudi, V. Chandrasekaran, N. Papernot, 2021, IEEE S&P, pp. 1039–1056.
   学习过程的可验证记录：最接近「守恒账」的已有概念——但它是事后溯源证明，不是运行期守恒约束；差异即我们的增量。
8. **Mechanism Design for Large Language Models** — P. Dütting, V. Mirrokni, R. Paes Leme, H. Xu, S. Zuo, 2024, ACM Web Conference (WWW), pp. 144–155. [近3年]
   把机制设计引入生成式模型输出（token 拍卖/聚合），机制×生成模型交叉的最新坐标。DOI: 10.1145/3589334.3645511
9. **Mechanism Design for Alignment via Human Feedback** — J. Manyika, M. Wooldridge, J. Gan, 2025, OpenReview（Workshop on Human Feedback for AI）。 [近3年]
   用机制设计保证人类反馈环节的激励兼容；「对齐=机制设计」的最新表述。链接: https://openreview.net/forum?id=0Z9VJgaebN
10. **Multi-Agent Systems Should be Treated as Principal-Agent Problems** — P. Rauba, S. Cepenas, M. van der Schaar, 2026, arXiv:2601.23211（预印本，注意时效）。 [近3年]
    主张用委托-代理/机制设计框架治理多智能体系统可靠性——与「守恒账作为委托方可审计的承诺」叙事同向。链接: https://arxiv.org/abs/2601.23211

**空位观察**：承诺装置文献（1, 5）谈博弈层；审计/可验证文献（6, 7）谈组织与密码层；**「物理守恒律作为算法内自我承诺、且可低成本事后审计」这一中间层无人占据**。Proof-of-Learning（7）是最邻近竞争概念，需在论文中显式区分。

---

## 主题 4：Price of Anarchy 在图算法 / 路由中的应用（median PoA=1.33 的坐标）

1. **Worst-Case Equilibria** — E. Koutsoupias, C. H. Papadimitriou, 1999, STACS, pp. 404–413. [经典]
   PoA（coordination ratio）的提出。DOI: 10.1007/3-540-49116-3_38
2. **How Bad is Selfish Routing?** — T. Roughgarden, É. Tardos, 2002, *Journal of the ACM* 49(2):236–259. [经典]
   仿射延迟下 nonatomic 路由 PoA = 4/3（Pigou 界）——**我们 median PoA=1.33 几乎精确落在该经典界上，是论文里最有故事性的对齐点**，需讨论我们的成本结构是否「仿射型」。
3. **The Price of Anarchy is Independent of the Network Topology** — T. Roughgarden, 2002, STOC, pp. 428–437. [经典]
   拓扑无关性结果：PoA 由延迟函数类决定而非图结构；若我们的 PoA 随图族变化，反而是新闻（见 10）。
4. **Bounding the Inefficiency of Equilibria in Nonatomic Congestion Games** — T. Roughgarden, É. Tardos, 2004, *Games and Economic Behavior* 47(2):389–403.
   拥塞博弈 PoA 的统一界定技术（variational inequality），可作为我们证明技术参照。
5. **The Price of Selfish Behavior in Bilateral Network Formation** — J. Corbo, D. Parkes, 2005, ACM EC, pp. 93–102（DOI: 10.1145/1073814.1073833）。
   双边网络形成博弈的 PoA/PoS 分析；边决策需要双方同意，更接近「边预测需两端协调」的设定。
6. **The Price of Stability for Network Design with Fair Cost Allocation** — E. Anshelevich, A. Dasgupta, J. Kleinberg, É. Tardos, T. Wexler, T. Roughgarden, 2008, *SIAM Journal on Computing* 38(4):1602–1623. [经典]
   PoS 概念的核心文献（公平分摊网络设计 PoS=H(n)）；「协调后能改善多少」的对偶度量——支撑我们「PoA 的协调价值」主张。DOI: 10.1137/070680096
7. **The Price of Anarchy in Network Creation Games** — E. D. Demaine, M. T. Hajiaghayi, H. Mahini, M. Zadimoghaddam, 2012, *ACM Transactions on Algorithms*。 [经典]
   网络创建博弈 PoA 的系统结果。链接: https://dl.acm.org/doi/abs/10.1145/2151171.2151176
8. **Improving the Price of Anarchy for Selfish Routing via Coordination Mechanisms** — G. Christodoulou, K. Mehlhorn, E. Pyrga, 2014, *Algorithmica* 70(3).
   通过协调机制（修改代价函数）降低 PoA——**「守恒账 = 协调机制以降低有效 PoA」的现成理论挂钩**。链接: https://link.springer.com/article/10.1007/s00453-013-9753-8
9. **Intrinsic Robustness of the Price of Anarchy** — T. Roughgarden, 2015, *Journal of the ACM* 62(5). [经典]
   光滑性（smoothness）框架：PoA 界自动推广到相关均衡/无后悔结果；若我们的 PoA 论证走光滑性路线，可获鲁棒性加成。DOI: 10.1145/2806883
10. **Methodologies for Quantifying and Optimizing the Price of Anarchy** — R. Chandan, D. Paccagnan, J. R. Marden, 2024, *IEEE Transactions on Automatic Control* 69(11). [近3年]
    PoA 的系统性量化与优化方法论（含分布/中位数视角之外的参数化工具）；报告 median PoA 的当代方法论参照。
    补充：F. Benita, V. Bilò, B. Monnot, G. Piliouras 等, 2020, WINE——数据驱动显示真实路由 PoA **依赖**网络拓扑，与 3 形成张力，可作为「实例级 PoA 报告」的正当性引用（链接: https://link.springer.com/chapter/10.1007/978-3-030-64946-3_18）。

---

## 定位建议：我们的贡献在文献地图中的空位

**空位 1（理论核心）：扩散场 = 势博弈最好响应的 mean-field 极限。**
Sandholm（主题1-6）建立了「群体极限 = 确定性 BR 流 = 势梯度流」，Blume（1-3）/Young（1-4）/Marden-Shamma（1-5）建立了「噪声→0 选择势极值」，Candogan（1-7）建立了「博弈 = 图上势流 + 调和流」的分解语言，Parise-Ozdaglar（1-9）建立了大网络博弈的连续极限。**但这四簇文献从未与生成式扩散模型（score field / reverse diffusion）对接**；扩散模型文献（本报告范围外）也不使用博弈论语言。我们的命题「确定性反向扩散场 ≡ 无噪声最好响应动态收敛于势函数极值」恰好落在四簇经典理论的交集处——该交集目前为空。这是全文最强的定位声明，建议作为引言主图（四象限：势博弈 / 学习动态 / 图流分解 / 扩散生成）。

**空位 2（系统贡献）：守恒账 = 运行期算法内承诺装置。**
承诺装置文献（Conitzer-Sandholm 06）是博弈层的先动优势；审计文献（Raji 20）是组织层的流程；可验证计算文献（Jia 21）是密码/溯源层。**把物理守恒律（账本闭合）作为生成过程的自我承诺、并可直接供第三方审计，属于「机制设计 × 可审计 AI」的中间层，无直接竞争者**。写作时必须与 Proof-of-Learning 显式区分：PoL 证明「训练发生过」，守恒账证明「本次重构满足约束」——一个事后溯源、一个逐实例不变量。

**空位 3（实证叙事）：PoA 的实例级报告与协调价值。**
PoA 文献以 worst-case 界为主（KP99、RT02 的 4/3），中位数/分布级 PoA 报告在应用文献中很少见（Benita 2020 是少数例外）。**median PoA=1.33 紧贴 Roughgarden-Tardos 的 4/3 仿射界**——两个用法：(a) 若我们的重构博弈代价结构可解释为仿射/可分拥塞型，则 1.33 是「理论界的实例级复现」，可引 2、4、9 做支撑；(b) 进一步把守恒账定位成 Christodoulou 等（4-8）意义上的**协调机制**：承诺装置的作用是把系统从「最坏均衡」推向 PoS 一侧（Anshelevich 等，4-6），「PoA 的协调价值」由此获得理论挂点。

**写作风险提示**：
- 主题 2 的「博弈论链接预测」文献以攻防对抗为主（Nettack、Waniek 系），我们是**生成/重构**而非对抗，需避免被审稿人归入 adversarial robustness 赛道；建议在 related work 中主动划界。
- 拥塞博弈 ↔ PageRank/扩散的直接桥梁文献稀缺（仅 Teng 2017 命中，Hopcroft-Sheldon 未核实）——这本身是空位，但若论文要强宣称「congestion–PageRank 对应」，需自证而非依赖引用。
- 引用 2026 年预印本（主题3-10 等）时注意时效标注；主论据全部锚定在 1–9 号经典/正式发表条目上。

**检索过程工件**：原始 scholar 结果 CSV 存于 `reviews/data/`（t1_potential, t1b_classics, t1c_loglinear, t1d_pagerank, t2_linkpred, t2b_linkpred, t2c_advlink, t2d_hiding, t2e_nettack, t2f_waniek, t3_mechdesign, t3b_verifiable, t3d_llmmd, t3e_commit, t4_poa）。
