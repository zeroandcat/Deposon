# 文献地图 v19：Deposon「脑图（知识图谱）补全」文献扫描

- **编制**：独立文献研究助手 R2，2026-08-23
- **检索方法**：以 scholar 学术搜索为主（关键词 + 精确标题检索，共 20 余次查询，检索结果 CSV 存档于会话临时目录），辅以 web_search 交叉核验发表 venue。所有条目均来自实际检索结果，未编造；venue/年份经第三方引文交叉确认的在条目内标注。
- **项目对接点**：固定节点集上的边权场补全（扩散式）、LLM 语义先验融合、留一边（LOO）预测评估（top-3 命中率、named/filler 分层、负采样 N_NEG=10）；已知痛点：评估对负采样口径敏感（legacy sampler 未排除金边 v）、LOO 边间依赖（49 条边共享 48 条观测边）、单图 n=1 样本量不足。

---

## ① 文献地图（按主题分组）

### 主题 1a：Knowledge Graph Completion 经典模型

**[1] Translating Embeddings for Modeling Multi-relational Data (TransE)**
Antoine Bordes, Nicolas Usunier, Alberto Garcia-Durán, Jason Weston, Oksana Yakhnenko — NeurIPS 2013
链接：https://proceedings.neurips.cc/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html
与本项目的关系：KGE 链接预测的开山基线；同时是 filtered/raw 排名评估协议（hits@k、mean rank）的出处——Deposon 的 LOO top-3 命中评估在谱系上直接继承该协议。
可借鉴点：①将"边是否存在/边权高低"化为打分排序问题，TransE 可在 Deposon 的 48 条观测边上训练，作为结构-only 基线；②其 filtered 设置（从负样本中剔除已知真边）正是修复 legacy sampler 未排除金边 v 的标准做法。

**[2] Complex Embeddings for Simple Link Prediction (ComplEx)**
Théo Trouillon, Johannes Welbl, Sebastian Riedel, Éric Gaussier, Guillaume Bouchard — ICML 2016
链接：http://proceedings.mlr.press/v48/trouillon16.html
与本项目的关系：复数嵌入张量分解，能处理对称/反对称关系；适合脑图中"方向性"边。
可借鉴点：作为第二个结构-only 基线；其 1-vs-all 打分方式提示 Deposon 可把 N_NEG=10 小池评估升级为全候选排序以消除负采样方差。

**[3] RotatE: Knowledge Graph Embedding by Relational Rotation in Complex Space**
Zhiqing Sun, Zhi-Hong Deng, Jian-Yun Nie, Jian Tang — ICLR 2019
链接：https://arxiv.org/abs/1902.10197
与本项目的关系：旋转建模可表达组合/逆/对称关系模式；self-adversarial 负采样权重影响巨大。
可借鉴点：其附录的 self-adversarial negative sampling 说明负样本"难度"本身是超参数——直接支撑 Deposon 把负采样难度作为实验变量而非固定管道。

**[4] Convolutional 2D Knowledge Graph Embeddings (ConvE)**
Tim Dettmers, Pasquale Minervini, Pontus Stenetorp, Sebastian Riedel — AAAI 2018
链接：https://ojs.aaai.org/index.php/AAAI/article/view/11573
与本项目的关系：卷积打分模型；1-N 高速评分范式。
可借鉴点：ConvE 的 1-N scoring 同时对所有候选节点打分，天然避免负采样口径问题；Deposon 可借鉴其"全候选一次打分"的评估实现。

**[5] Composition-based Multi-relational Graph Convolutional Networks (CompGCN)**
Shikhar Vashishth, Soumya Sanyal, Vikram Nitin, Partha Talukdar — ICLR 2020（arXiv 2019）
链接：https://arxiv.org/abs/1911.03082
与本项目的关系：在图卷积中联合嵌入节点与关系，是"结构消息传递 + 打分解码器"的代表。
可借鉴点：Deposon 的边权场补全可视为"节点固定、边属性回归"的结构消息传递问题；CompGCN 的 encoder-decoder 分解为"扩散场 encoder + 边打分 decoder"设计提供模板。

### 主题 1b：LLM 时代的 KGC（LLM as prior / KG-LM 融合）

**[6] Unifying Large Language Models and Knowledge Graphs: A Roadmap**
Shirui Pan, Linhao Luo, Yufei Wang, Chen Chen, Jiapu Wang, Xindong Wu — IEEE TKDE 2024
链接：https://ieeexplore.ieee.org/abstract/document/10387715/
与本项目的关系：LLM⊗KG 融合路线的权威综述（LLM-augmented KGC 三分法）。
可借鉴点：为论文 related work 提供分类框架——Deposon 属"LLM as prior/encoder 注入结构学习"一支，引用它可定位自身坐标。

**[7] Making Large Language Models Perform Better in Knowledge Graph Completion**
Yichi Zhang, Zhuo Chen, Lingbing Guo, Yajing Xu, Wen Zhang, Huajun Chen — ACM MM 2024（venue 经第三方引文核验：Proc. 32nd ACM Int. Conf. on Multimedia, pp. 233–242）
链接：https://dl.acm.org/doi/abs/10.1145/3664647.3681327
与本项目的关系：直接用 LLM 做 KGC 的代表方法（检索+重排式）。
可借鉴点：其"候选召回 → LLM 重排"两阶段可作为 Deposon 的 LLM-only 基线协议。

**[8] Multi-perspective Improvement of Knowledge Graph Completion with Large Language Models**
Derong Xu, Zi Zhang, Zhen Lin, Xian Wu, Zhihong Zhu, Tong Xu, Xiangyu Zhao, Yefeng Zheng, Enhong Chen — LREC-COLING 2024
链接：https://aclanthology.org/2024.lrec-main.1044/
与本项目的关系：用 LLM 查询扩充稀疏图结构（尤其长尾节点），与"脑图补全"任务同构。
可借鉴点：filler/长尾节点的 LLM 语义补边策略，可直接映射到 Deposon 的 filler 分层处理。

**[9] KEPLER: A Unified Model for Knowledge Embedding and Pre-trained Language Representation**
Xiaozhi Wang, Tianyu Gao, Zhaocheng Zhu, Zhengyan Zhang, Zhiyuan Liu, Juanzi Li, Jian Tang — TACL 2021
链接：https://direct.mit.edu/tacl/article-abstract/doi/10.1162/tacl_a_00360/98089
与本项目的关系：KG 嵌入与语言模型联合训练的经典"语义-结构融合"范式。
可借鉴点：证明"文本语义目标与结构目标可共享表示空间"——为 Deposon 的 LLM 语义先验与扩散场融合提供理论先例与引用锚点。

### 主题 2：链接预测评估协议陷阱（本项目最相关主题）

**[10] Analysis of the Impact of Negative Sampling on Link Prediction in Knowledge Graphs**
Bhushan Kotnis, Vivi Nastase — arXiv 2017（AKBC 投稿版本；workshop venue 未能核验，按预印本引用）
链接：https://arxiv.org/abs/1708.06816
与本项目的关系：**直接命中 Deposon 痛点**——系统证明负样本数量/构成改变会压缩甚至反转模型间差距，小负样本池下结论不可靠。
可借鉴点：①报告 N_NEG ∈ {1, 10, 50} 及全候选排序多档结果；②负样本难度分层（同类型节点 vs 随机节点）；③把 legacy/fixed sampler 差异作为协议变量写进正文而非脚注。

**[11] Evaluating Graph Neural Networks for Link Prediction: Current Pitfalls and New Benchmarking (HeaRT)**
Juanhui Li, Harry Shomer, Haitao Mao, Shenglai Zeng, Yao Ma, Neil Shah, Jiliang Tang, Dawei Yin — NeurIPS 2023 (Datasets and Benchmarks)
链接：https://proceedings.neurips.cc/paper_files/paper/2023/hash/0be50b4590f1c5fdf4c8feddd63c4f67-Abstract-Datasets_and_Benchmarks.html
与本项目的关系：指出当前链路预测评估的系统性陷阱（评估设置单一、负样本过于简单），并给出按"现实/对抗"分档的评估协议。
可借鉴点：①同一模型在不同评估设置下排名可反转——Deposon 应报告 ≥2 种负采样设置；②"现实负样本"（与真边同分布的难负样本）设计可直接用于 named/filler 分层负采样。

**[12] Realistic Re-evaluation of Knowledge Graph Completion Methods: An Experimental Study**
Farahnaz Akrami, Mohammed Samiul Saeef, Qingheng Zhang, Wei Hu, Chengkai Li — SIGMOD 2020
链接：https://dl.acm.org/doi/abs/10.1145/3318464.3380599
与本项目的关系：揭示 KGC 基准中训练-测试冗余（逆关系泄漏）导致指标虚高，清洗后排名大变。
可借鉴点：脑图 LOO 评估需检查"可逆推边"（如对称表述、同义边）造成的泄漏；Deposon 人工转译脑图尤其要查 named 边的文本-结构重复。

**[13] On the Ambiguity of Rank-Based Evaluation of Entity Alignment or Link Prediction Methods**
Max Berrendorf, Evgeniy Faerman, Laurent Vermue, Volker Tresp — arXiv 2020
链接：https://arxiv.org/abs/2002.06914
与本项目的关系：指出 hits@k/MRR 在**分数打平（ties）**时结果取决于实现细节，给出 optimistic/pessimistic/realistic 三档口径。
可借鉴点：Deposon 边权场已出现 tie-artifact 问题——必须显式声明平局处理口径（建议 realistic/平均排名），否则 top-3 命中率不可复现。

**[14] A Unified Framework for Rank-Based Evaluation Metrics for Link Prediction in Knowledge Graphs**
Charles Tapley Hoyt, Max Berrendorf, Mikhail Galkin, Volker Tresp, Benjamin M. Gyori — arXiv 2022
链接：https://arxiv.org/abs/2203.07544
与本项目的关系：把 hits@k/MRR/MR 统一为"排序期望值的变换"，给出各指标适用性与方差分析。
可借鉴点：为 Deposon 选择 top-k 命中而非 MRR 提供理论辩护/反驳依据；提示小样本下 hits@k 的方差特性。

**[15] Observed versus Latent Features for Knowledge Base and Text Inference**
Kristina Toutanova, Danqi Chen — CVSC Workshop @ NAACL 2015
链接：https://aclanthology.org/W15-4007.pdf
与本项目的关系：最早系统指出 FB15k 测试集可被逆关系规则"背答案"，是评估批判的源头文献。
可借鉴点：Deposon 若引入多图，应检查图间/边间可逆推性；引用它说明"结构泄漏"不是新问题。

**[16] Knowledge Graph Embedding for Link Prediction: A Comparative Analysis**
Andrea Rossi, Denilson Barbosa, Donatella Firmani, Antonio Matinata, Paolo Merialdo — ACM TKDD 15(2), 2021（venue 经第三方引文核验）
链接：https://dl.acm.org/doi/abs/10.1145/3424672
与本项目的关系：在统一协议下大规模复测 KGE 模型，量化"评估口径变化 → 结论变化"的幅度。
可借鉴点：其复测方法学（统一 filtered 设置、报告置信区间）是 Deposon 重跑基线的操作手册。

### 主题 3：图上的扩散生成模型（edge/graph generation）

**[17] Denoising Diffusion Probabilistic Models (DDPM)**
Jonathan Ho, Ajay Jain, Pieter Abbeel — NeurIPS 2020
链接：https://proceedings.neurips.cc/paper_files/paper/2020/hash/4c5bcfec8584af0d967f1ab10179ca4b-Abstract.html
与本项目的关系：扩散式生成的根文献；Deposon"边权场扩散补全"的方法学祖先。
可借鉴点：前向加噪/反向去噪的形式化可迁移为"观测边权场 → 掩蔽边去噪重建"的掩码扩散目标。

**[18] DiGress: Discrete Denoising Diffusion for Graph Generation**
Clément Vignac, Igor Krawczuk, Antoine Siraudin, Bohan Wang, Volkan Cevher, Pascal Frossard — ICLR 2023
链接：https://arxiv.org/abs/2209.14734
与本项目的关系：在离散节点/边类别空间做扩散，直接生成邻接结构。
可借鉴点：①"边"作为离散类别变量的扩散转移矩阵设计；②用图级统计量（度分布、聚类系数）做生成质量评估——Deposon 可借作"补全后脑图结构合理性"的指标。

**[19] Score-based Generative Modeling of Graphs via the System of Stochastic Differential Equations (GDSS)**
Jaehyeong Jo, Seul Lee, Sung Ju Hwang — ICML 2022
链接：https://proceedings.mlr.press/v162/jo22a.html
与本项目的关系：邻接矩阵连续 SDE 扩散的代表，可同时扩散节点特征与邻接。
可借鉴点：把边权场视作连续邻接张量进行扩散的形式化路径；其置换不变性讨论对"固定节点集"设定有简化意义。

**[20] Efficient and Degree-Guided Graph Generation via Discrete Diffusion Modeling (EDGE)**
Xiaohui Chen, Jiaxing He, Xu Han, Li-Ping Liu — ICML 2023（PMLR v202, pp. 4585–4610，经第三方引文核验）
链接：https://arxiv.org/abs/2305.04111
与本项目的关系：揭示图扩散生成的信息量高度集中于**度序列**，以度引导大幅提升效率与质量。
可借鉴点：①"度先验"应成为 Deposon 的免费强基线/正则项；②度保持扰动（degree-preserving rewiring）可生成与真边同度分布的难负样本，直接回应评估对负采样敏感的问题。

**[21] Generative Diffusion Models on Graphs: Methods and Applications（综述）**
Chengyi Liu, Wenqi Fan, Yunqing Liu, Jiatong Li, Hang Li, Hui Liu, Jiliang Tang, Qing Li — arXiv 2023
链接：https://arxiv.org/abs/2302.02591
与本项目的关系：图扩散方法与应用（分子、社交网、推荐、结构预测）的整理。
可借鉴点：快速定位"图补全/链接预测视角的扩散"相关工作段落，补充 related work 覆盖面。

### 主题 4：LLM 引导的图补全/结构预测与语义先验

**[22] Can Language Models Solve Graph Problems in Natural Language? (NLGraph)**
Heng Wang, Shangbin Feng, Tianxing He, Zhaoxuan Tan, Xiaochuang Han, Yulia Tsvetkov — NeurIPS 2023
链接：https://proceedings.neurips.cc/paper_files/paper/2023/hash/622afc4edf2824a1b6aaf5afe153fa93-Abstract-Conference.html
与本项目的关系：系统评测 LLM 直接对图结构问题（连通性、最短路等）作答的能力与局限。
可借鉴点：为"LLM 语义先验能提供多强的结构信号"提供量化预期与 prompt 设计参照；也是 LLM-only 基线的协议来源。

**[23] Talk Like a Graph: Encoding Graphs for Large Language Models**
Bahare Fatemi, Jonathan Halcrow, Bryan Perozzi — ICLR 2024
链接：https://proceedings.iclr.cc/paper_files/paper/2024/hash/bf72f65f30eedf5d48da6980ee02b589-Abstract-Conference.html
与本项目的关系：系统研究图→文本序列化方式对 LLM 图推理的影响。
可借鉴点：Deposon 的 LLM 先验提取必然涉及脑图序列化——本文提示序列化口径是系统性偏差来源，应做序列化方式敏感性分析。

**[24] Large Language Models are Effective Priors for Causal Graph Discovery**
Victor-Alexandru Darvariu, Stephen Hailes, Mirco Musolesi — arXiv 2024
链接：https://arxiv.org/abs/2405.13551
与本项目的关系：**与 Deposon 最同构**——把 LLM 的逐边判断作为软先验注入连续结构学习（NOTEARS 式），而非让 LLM 直接决定结构。
可借鉴点：①先验强度参数化的做法可对应 Deposon 的 λ 融合系数；②其"LLM 先验有噪声仍有效"的证据为先验翻转/随机化阴性对照设计提供模板。

**[25] Causal Structure Learning Supervised by Large Language Model**
Taiyu Ban, Lyuzhou Chen, Derun Lyu, Xiangyu Wang, Huanhuan Chen — arXiv 2023
链接：https://arxiv.org/abs/2311.11689
与本项目的关系：同一研究组后续还发表了"缓解 LLM 先验错误"的工作，构成"LLM 先验 + 错误建模"的小系列。
可借鉴点：先验错误建模（prior error mitigation）思想——Deposon 可对 LLM 先验估计置信度并按置信度加权融合，而非均匀 λ。

**[26] GraphGPT: Graph Instruction Tuning for Large Language Models**
Jiabin Tang, Yuhao Yang, Wei Wei, Lei Shi, Lixin Su, Suqi Cheng, Dawei Yin, Chao Huang — SIGIR 2024（venue 经第三方引文核验）
链接：https://dl.acm.org/doi/abs/10.1145/3626772.3657775
与本项目的关系：图指令微调让 LLM 显式对齐图结构语义，含链接预测任务。
可借鉴点：若后续允许训练/微调，"结构-文本对齐"路线是把语义先验内化的方向；当前可作为 prompting 路线的对照讨论。

### 主题 5：脑图/概念图自动构建与补全（教育技术侧）

**[27] The Automatic Creation of Concept Maps from Documents Written Using Morphologically Rich Languages**
Kristina Zubrinic, Damir Kalpic, Mario Milicevic — Expert Systems with Applications 2012
链接：https://www.sciencedirect.com/science/article/pii/S0957417412006628
与本项目的关系：从文本自动抽取概念与关系构建概念图的经典管线。
可借鉴点：概念图构建的"概念抽取 → 关系标注 → 图成形"三段式为 Deposon 脑图构建侧提供术语与流程对照。

**[28] Concept Map Construction from Text Documents Using Affinity Propagation**
Iqra Qasim, Jin-Woo Jeong, Joon-Uh Heu, Dong-Ho Lee — Journal of Information Science 2013
链接：https://journals.sagepub.com/doi/abs/10.1177/0165551513494645
与本项目的关系：用聚类（affinity propagation）组织概念层级再连边，是"先分层后建图"的代表。
可借鉴点：named/filler 分层可借鉴其层级组织思路；聚类质量评估方法可参考。

**[29] Research on a New Automatic Generation Algorithm of Concept Map Based on Text Analysis and Association Rules Mining**
Zequn Shao, Yafang Li, Xiao Wang, Xu Zhao, Ying Guo — Journal of Ambient Intelligence and Humanized Computing 2020
链接：https://link.springer.com/article/10.1007/s12652-018-0934-9
与本项目的关系：文本分析 + 关联规则挖掘生成概念图，含与人工概念图的对比评估。
可借鉴点：其"生成图 vs 专家图"的对比评估设计（边重合度类指标）是 Deposon 除 LOO 外的补充评估思路。

**[30] MindMap: Knowledge Graph Prompting Sparks Graph of Thoughts in Large Language Models**
Yilin Wen, Zifeng Wang, Jimeng Sun — ACL 2024
链接：https://aclanthology.org/2024.acl-long.558/
与本项目的关系：LLM 时代以"思维脑图"组织知识图谱证据进行推理——与 Deposon"脑图辅助 LLM 推理"的定位最直接相关。
可借鉴点：脑图作为 LLM 推理脚手架的收益/成本分析框架；其证据图构建-检索-推理三段流程可与 Deposon 主环路对照。

### 主题 6：小样本图评估的统计方法

**[31] Note on the Sampling Error of the Difference between Correlated Proportions or Percentages (McNemar 检验)**
Quinn McNemar — Psychometrika 1947
链接：https://www.cambridge.org/core/journals/psychometrika/article/note-on-the-sampling-error-of-the-difference-between-correlated-proportions-or-percentages/698C2461BE63F5848763502D54E534FD
与本项目的关系：配对二分类结果（命中/未命中）差异检验的原典；Deposon 已在 GSM8K 侧使用 McNemar，应延伸到 LOO 边命中比较。
可借鉴点：两方法在同一 49 条边上的命中是天然配对样本，McNemar 的 discordant pairs（b, c）正是审稿人要求的"命中计数"表。

**[32] Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithms**
Thomas G. Dietterich — Neural Computation 1998
链接：https://direct.mit.edu/neco/article-abstract/10/7/1895/6224
与本项目的关系：系统比较 5x2cv、McNemar、重采样 t 检验等在相关样本下比较学习算法的 I 类错误率。
可借鉴点：权威论证"重采样/交叉验证拆分产生相关样本，朴素 t 检验 I 类错误膨胀"——直接支撑 Deposon 不能把 49×10 当 490 独立样本的立场，并给出替代检验选型。

**[33] A Practitioner's Guide to Cluster-Robust Inference**
A. Colin Cameron, Douglas L. Miller — Journal of Human Resources 2015
链接：https://jhr.uwpress.org/content/50/2/317.short
与本项目的关系：簇相关数据推断的操作手册（簇数少时的偏差与修正）。
可借鉴点：Deposon 的"同一图内 49 条边"= 单簇/少簇情形；文中 few-cluster 的注意事项（wild bootstrap 等）是方法学依据。

**[34] Bootstrap-Based Improvements for Inference with Clustered Errors**
A. Colin Cameron, Jonah B. Gelbach, Douglas L. Miller — Review of Economics and Statistics 2008
链接：https://direct.mit.edu/rest/article-abstract/90/3/414/57731
与本项目的关系：wild cluster bootstrap 的出处，少簇下显著优于常规簇稳健标准误。
可借鉴点：为 Deposon 提供可执行的"边级 cluster bootstrap"实现路线：以图（或共享观测边集）为簇重采样命中率。

**[35] Bootstrapping Exchangeable Random Graphs**
Alden Green, Cosma Rohilla Shalizi — Electronic Journal of Statistics 2022
链接：https://projecteuclid.org/journals/electronic-journal-of-statistics/volume-16/issue-1/Bootstrapping-exchangeable-random-graphs/10.1214/21-EJS1896.short
与本项目的关系：网络数据的合法重采样理论（换元图模型的子图 bootstrap）；同谱系先声为 Bhattacharyya & Bickel, "Subsampling Bootstrap of Count Features of Networks", Annals of Statistics 2015（https://projecteuclid.org/journals/annals-of-statistics/volume-43/issue-6/Subsampling-bootstrap-of-count-features-of-networks/10.1214/15-AOS1338.short）。
可借鉴点：严格化"为什么对边做普通 bootstrap 在网络中不合法"；给出图级重采样的正确单元。

**[36] Evaluating Overfit and Underfit in Models of Network Community Structure**
Amir Ghasemian, Homa Hosseinmardi, Aram Galstyan, Edoardo M. Airoldi, Aaron Clauset — IEEE TKDE 2019（另有 PRX 版本）
链接：https://ieeexplore.ieee.org/abstract/document/8692626/
与本项目的关系：网络模型选择与过/欠拟合的边交叉验证（edge-CV）框架，讨论边非独立性与 K 折划分在网络中的含义。
可借鉴点：为 Deposon 的 LOO 协议提供网络统计视角的合法性讨论与替代拆分（如分层边抽样）设计空间。

---

## ② 「必须对比的基线」清单

按"成本从低到高、缺一不可"排序。所有基线必须与 Deposon 共用**同一** LOO 协议、同一负样本池、同一 tie 处理口径，否则对比无效（依据 [10][11][13]）。

| # | 基线 | 出处 | 回答的问题 | 实现要点 |
| --- | --- | --- | --- | --- |
| B1 | 度先验 / 度引导基线 | [20] EDGE | "扩散场是否只是学到了度分布？" | 用观测边度序列直接给候选边打分；度保持重连可同时充当难负样本生成器 |
| B2 | 经典链接预测启发式（共同邻居 / Adamic-Adar / 优先连接） | 常识基线，可引 [11] 的协议 | "是否需要学习模型？" | 零训练成本，必须在结果表中占位 |
| B3 | TransE | [1] | "结构嵌入能补多少？" | 在 48 条观测边上训练，边打分排序；小规模下注意欠拟合 |
| B4 | ComplEx 或 RotatE | [2][3] | "方向/对称模式是否有用？" | 与 B3 二选一以上，报告两者差异 |
| B5 | ConvE 或 CompGCN（encoder-decoder 型） | [4][5] | "消息传递是否优于纯分解？" | 49 节点小图可全量 1-N 打分，兼作全候选排序口径的实现 |
| B6 | LLM-only（检索+重排 / 直接判断） | [7][22][23] | "LLM 语义先验单独有多强？" | 同一候选集让 LLM 排序；记录序列化方式（[23]）作为协议字段 |
| B7 | 消融：扩散-only（λ=0）、先验-only（无扩散场）、随机/翻转先验（阴性对照） | 本项目内部 + [24][25] | "融合是否带来增量、增量来自先验质量还是噪声？" | 阴性对照已部分存在于 v17 fusion_fix；补齐"翻转先验"档 |
| B8（可选） | 文本编码器打分（KG-BERT/SimKGC 式） | 见 [6] 综述分类 | "句义编码是否强于生成式 LLM 判断？" | 若 API/算力预算允许再补 |

## ③ 「必须引用的评估协议文献」清单

论文评估章节（或附录协议小节）中**必须**出现，否则评估结论在审稿视角下不可辩护：

1. **[10] Kotnis & Nastase 2017** —— 负采样数量/构成影响结论：为"N_NEG 作为实验变量、多档报告"提供依据。
2. **[11] Li et al. NeurIPS 2023 (HeaRT)** —— 链路预测评估陷阱与现实负采样：为"负样本难度分层、named/filler 分层负采样"提供依据。
3. **[12] Akrami et al. SIGMOD 2020** —— 训练-测试冗余/泄漏导致虚高：为 LOO 泄漏检查（含逆关系、同义边）提供依据。
4. **[13] Berrendorf et al. 2020 + [14] Hoyt et al. 2022** —— 排名评估的平局歧义与统一框架：为"显式声明 tie 口径（realistic/平均排名）、报告指标定义"提供依据；直接回应已发生的 tie-artifact。
5. **[1] Bordes et al. 2013（TransE）** —— filtered vs raw 协议出处：为"负样本池排除金边及已知真边"（修复 legacy sampler）提供依据。
6. **[15] Toutanova & Chen 2015** —— 结构泄漏批判的源头：为"可逆推边"讨论提供依据。
7. **[31] McNemar 1947 + [32] Dietterich 1998** —— 配对样本比较与相关样本下检验选择：为 LOO 边命中的显著性检验提供依据。
8. **[33] Cameron & Miller 2015 / [34] Cameron-Gelbach-Miller 2008 / [35] Green & Shalizi 2022** —— 簇相关/网络数据推断：为"49 条边不是 490 个独立样本"及图级 bootstrap 提供依据。
9. **[16] Rossi et al. TKDD 2021** —— 统一协议复测方法学：为多基线重跑的口径统一提供模板。

---

## ④ 对本项目算法与实验设计的具体启示

**启示 1（负采样升级为实验变量，且负样本要"难度分层 + 度匹配"）**
[10][11][20] 共同指向：N_NEG=10 的 top-3 命中率同时受 (a) 负样本数量、(b) 负样本难度、(c) 负样本与真边的分布差异三重影响，且三者都会改变方法间排序。建议协议改为：N_NEG ∈ {1, 10, 50} 三档 + 全候选排序一档；负样本分两档难度（随机节点对 vs 度保持重连的难负样本）；named/filler 各层分别报告。预期工作量小（复用现有 sampler 接口），但能把"评估对负采样口径敏感"从弱点改写为系统性发现。

**启示 2（显式声明排名口径：filtered + realistic ties）**
[13][14] 证明 hits@k 在分数打平时随实现细节漂移，Deposon 已实际遭遇 tie-artifact。建议在论文中固定并声明：①filtered 设置（负样本池剔除金边 v 与所有已知真边——同时固化 legacy→fixed sampler 的修复）；②tie 处理采用 realistic（平均排名）口径，并在附录给 optimistic/pessimistic 两档作为敏感性；③报告命中计数表（b, c discordant pairs），与审稿意见对齐。

**启示 3（统计口径：边是相关样本，图是簇；显著性走 McNemar + cluster bootstrap）**
[31][32][33][34][35][36] 给出的合法路径：49 条 LOO 边共享 48 条观测边，且全部来自单图——有效样本量接近 n=1 图。建议：①方法间比较用逐边配对的 McNemar（命中/未命中），报告 b/c 与精确 p；②置信区间用图级/簇级 bootstrap（多图后按图重采样；单图情形诚实标注为描述性结果）；③引用 [32] 说明为何不做朴素独立样本 t 检验；④多图扩展（v17 已做 20 图 filler 重挂）应优先增加**真实脑图**数量而非仅扰动 filler——这才是把 n 做大的唯一途径。

**启示 4（先验融合对标 LLM-as-prior 结构学习：软先验 + 先验噪声建模 + 置信度加权）**
[24][25] 与 Deposon 的 λ 融合同构：LLM 逐边判断作为可错的软先验注入结构学习。可借鉴三点：①λ 不应只是标量，可按 LLM 判断置信度逐边加权（先验强度参数化）；②设置"先验翻转 / 随机先验 / 无关主题先验"三档阴性对照，证明增量来自先验质量而非正则化效应；③按 [23]，把脑图→prompt 的序列化方式列为协议字段并做敏感性分析（至少 2 种序列化口径），排除"先验差是序列化伪影"。

**启示 5（扩散补全机制对标图扩散生成：离散化边权 + 掩码扩散 + 度引导正则）**
[17][18][19][20] 提示三条可落地的机制改造：①把连续边权场离散化为有限类别（有/无/强/弱）后做离散扩散（DiGress 式），可天然规避连续场上的 tie-artifact 与量纲问题（呼应 λ 根因中"field 量纲小"的发现）；②训练目标改为掩码扩散（随机掩蔽观测边 → 去噪重建），与 LOO 评估同分布，减少训练-评估失配；③引入度序列作为辅助监督/正则（EDGE 式度引导），既稳定小图上的扩散训练，又免费获得 B1 基线的对照解释力。

---

## 附：检索与核验记录

- scholar 检索 20 余轮（主题关键词 + 精确标题），结果 CSV 存于会话临时目录（/tmp/scholar/t*.csv），本文件条目均可回溯。
- venue/年份交叉核验（web_search）：[7] ACM MM 2024、[16] ACM TKDD 15(2) 2021、[20] ICML 2023 (PMLR v202)、[26] SIGIR 2024、[1] NeurIPS 2013 canonical URL。
- 按保守口径标注为 arXiv 预印本的条目：[10]（workshop 版本未能核验）、[13][14][21][24][25]。
- 明确负面结果：McNemar 1947 首轮关键词检索未命中，改用精确标题命中；Kotnis & Nastase 的 workshop 出处两轮检索均未确认，故按预印本引用。
