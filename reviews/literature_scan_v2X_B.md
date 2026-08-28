# 文献地图 v2.X-B：「脑图补全的语义先验与边界刻画」四主题侦察

- **编制**：文献侦察员 B，2026-08-23
- **检索方法**：scholar 学术搜索（关键词 + 精确标题，20+ 轮，结果 CSV 存于会话临时目录 /tmp/scholar_b/）+ web_search 第三方引文交叉核验 venue/页码。所有条目均可回溯；未能完全核验的在条目内显式标注。
- **与 v19 的关系**：v19（reviews/literature_scan_v19.md）已覆盖 KGE 经典模型、评估协议陷阱、图扩散、LLM-as-prior、小样本统计。本扫描**不重复**这些条目，聚焦四个新角度：① LLM-KGC 的零样本/方向语义实证数字；② 概念图/脑图构建与补全的评估协议（教育测量学传统）；③ 规则/关键词过滤的对抗鲁棒性（GT-2 定位）；④ 「边界/阴性结果」作为贡献类型的范式先例。
- **项目对接点**：labels-only 先验在真实语义图上 named Hits@3 达 0.48–1.0、方向一致率 ≥0.96；GT-2 攻击者 100% 绕过关键词表、规则过滤降至机会水平；v2.X 主线为「分工 + 边界」。

---

## 主题 1：LLM 知识图谱补全与方向语义

**[T1-1] KG-BERT: BERT for Knowledge Graph Completion** 【经典前史】
Liang Yao, Chengsheng Mao, Yuan Luo — arXiv 2019（arXiv:1909.03193）
链接：https://arxiv.org/abs/1909.03193
相关性：「labels/文本序列做三元组分类」的源头工作——只用实体/关系描述文本微调 BERT 判边，是 Deposon labels-only 先验在方法谱系上的直系祖先；其三元组分类协议可作为 named/filler 命中率的同族参照。
注：v19 未收录；venue 保守按预印本引用。

**[T1-2] KICGPT: Large Language Model with Knowledge in Context for Knowledge Graph Completion** 【近 3 年】
Yanbin Wei, Qiushi Huang, Yu Zhang, James T. Kwok — Findings of EMNLP 2023, pp. 8667–8683（venue 经第三方引文核验）
链接：https://aclanthology.org/2023.findings-emnlp.580/
相关性：免微调「KGE 检索 + LLM 重排」框架，直击长尾实体；其 ICL「Knowledge Prompt」与 Deposon 的 labels-only prompt 同构，且论文报告 LLM 单独判断显著弱于「检索+重排」混合——为「分工」叙事提供直接实证先例。
注：与 v19 [7]（Zhang et al. ACM MM 2024）同路线但协议更轻，不重复。

**[T1-3] Exploring Large Language Models for Knowledge Graph Completion（KG-LLM）** 【近 3 年】
Liang Yao, Jiazhi Peng, Chengsheng Mao, Yuan Luo — ICASSP 2025（arXiv:2308.13916；venue 经 scholar 出版信息核验）
链接：https://ieeexplore.ieee.org/abstract/document/10889242/ （预印本 https://arxiv.org/abs/2308.13916）
相关性：把三元组当文本序列做 triple classification / relation prediction / link prediction 的系统评测；**关键发现：零样本/少样本 GPT-4 明显弱于微调 6–7B 小模型**——这是「LLM 纯语义先验有上限、需要结构配合」的同类量化证据，可与 Deposon labels-only Hits@3 0.48–1.0 的图间方差互证。

**[T1-4] MKGL: Mastery of a Three-Word Language** 【近 3 年】
Lingbing Guo, Zhongpu Bo, Zhuo Chen, Yichi Zhang, Jiaoyan Chen, 等 — NeurIPS 2024, 37:140509–140534（venue 经第三方引文核验）
链接：https://arxiv.org/abs/2402.16164
相关性：把 KG 三元组建模为「三词语言」并让 LLM 在 token 级打分，证明关系/实体标签文本本身携带强结构信号——为「labels-only 先验为何在语义图上能工作」提供机制层面的同类解释与对照。

**[T1-5] Zero-shot Link Prediction in Knowledge Graphs with Large Language Models** 【近 3 年】
Mingchen Li, Chen Ling, Rui Zhang, Liang Zhao — 2024 IEEE International Conference（ieeexplore document/10884231；会议全名 Big Data 2024 未二次核验）；扩展版 arXiv:2402.10779
链接：https://ieeexplore.ieee.org/abstract/document/10884231/ ；https://arxiv.org/abs/2402.10779
相关性：明确提出 LLM 零样本链接预测任务设定与压缩转移图框架；是 Deposon「零训练 labels-only 先验」在任务定义上的最近邻，其零样本性能数字可作横向下界参照。

**[T1-6] Revisiting Relation Extraction in the Era of Large Language Models** 【近 3 年】
Somin Wadhwa, Silvio Amir, Byron C. Wallace — ACL 2023, pp. 15566–15589（venue 经第三方引文核验）
链接：https://aclanthology.org/2023.acl-long.868/
相关性：系统比较 LLM 零/少样本关系抽取与全监督 SOTA，发现精心设计 prompt 的 GPT-3 可接近全监督——为「LLM 语义先验在关系语义任务上的强度区间」提供权威量化锚点，可直接用于 labels-only 先验强度的外部校准。

**[T1-7] GPT-RE: In-context Learning for Relation Extraction Using Large Language Models** 【近 3 年】
Zhen Wan, Fei Cheng, Zhuoyuan Mao, Qianying Liu, Haiyue Song, Jiwei Li, Sadao Kurohashi — EMNLP 2023, pp. 3534–3547（venue 经第三方引文核验）
链接：https://aclanthology.org/2023.emnlp-main.214/
相关性：指出朴素 ICL 下 LLM 的关系判别受「实体-关系相关性」误导，提出检索式示例注入修正——对应 Deposon 场景：LLM 判边易被标签表层相关性带偏，需要先验置信度建模。

**[T1-8] The Reversal Curse: LLMs Trained on "A Is B" Fail to Learn "B Is A"** 【近 3 年】
Lukas Berglund, Meg Tong, Maximilian Kaufmann, Mikita Balesni, Asa Cooper Stickland, Tomasz Korbak, Owain Evans — ICLR 2024（venue 经多处第三方引文核验；arXiv:2309.12288）
链接：https://openreview.net/forum?id=GPKTIktA0k
相关性：**方向语义的核心反例文献**——LLM 对关系的方向性泛化存在系统性失败。反衬 Deposon 方向一致率 ≥0.96 的意义：该数字高于「裸 LLM 方向泛化」的先验预期，说明 labels-only 先验 + 真实语义图的结构约束起到了方向锚定作用；引用它可把方向一致率从「顺带结果」升格为「对照反转诅咒的发现」。

**[T1-9] Is the Reversal Curse a Binding Problem? Uncovering Limitations of Transformers from a Basic Generalization Failure** 【近 3 年，最新】
Boxi Wang, Haiteng Sun — ICLR 2026（proceedings.iclr.cc，经 scholar 核验）
链接：https://proceedings.iclr.cc/paper_files/paper/2026/ （OpenReview 条目；具体 hash 未核验）
相关性：反转诅咒的机制解释（绑定问题）——为「LLM 为什么会在方向上出错」提供表征层面的理论解释，可支撑 v2.X 对方向错误的错误类型学（error taxonomy）讨论。

**[T1-10] Have We Designed Generalizable Structural Knowledge Promptings? Systematic Evaluation and Rethinking** 【近 3 年】
Yichi Zhang, Zhuo Chen, Lingbing Guo, Yajing Xu, Sirui Chen, 等 — ACL 2025 (Long), aclanthology 2025.acl-long.110（venue 经 scholar 出版信息核验）
链接：https://aclanthology.org/2025.acl-long.110/
相关性：对 LLM-KGC 结构知识 prompt 设计做系统复测，发现既往 prompt 结论泛化性差——**本身就是「评估批判/边界分析」与主题 1 的交叉点**，同时为 Deposon 把 prompt 序列化口径列为实验变量提供直接先例（比 v19 [23] 更聚焦 KGC）。

**[T1-11，备查] Large Language Models for Knowledge Graph Extraction: A Schema-Constrained Evaluation Framework** 【最新，未充分核验】
M. Ilves, E. Barbu, J. Übi — KALLM workshop 2026（aclanthology 2026.kallm-1；低引新作，细节未核验）
链接：https://aclanthology.org/2026.kallm-1.pdf#page=233
相关性：把 LLM 抽取的 KG 错误按 schema 约束分类（含结构性近错 vs 内容错误）——若需「LLM 抽取图中方向/结构错误类型学」的最新引用可用，但建议引用前精读核验。

---

## 主题 2：概念图/脑图自动构建与补全——评估协议与基准

**[T2-1] The Theory Underlying Concept Maps and How to Construct and Use Them** 【经典】
Joseph D. Novak, Alberto J. Cañas — IHMC Technical Report CmapTools 2006-01 Rev 01-2008（经 web 核验）
链接：https://cmap.ihmc.us/docs/theory-of-concept-maps.php
相关性：概念图的定义学源头（概念-连接词-命题三元结构）。脑图的「边=带连接词的命题」定义直接来自此文；v2.X 写任务定义时必须引用以区分「概念图」与「思维导图(Buzan)」。

**[T2-2] Problems and Issues in the Use of Concept Maps in Science Assessment** 【经典】
Maria Araceli Ruiz-Primo, Richard J. Shavelson — Journal of Research in Science Teaching 33(6):569–600, 1996（经 web 核验）
相关性：概念图自动评分的奠基文献，核心发现**「不同构图任务/评分口径测的是不同东西」**（task-scoring 依赖性）——与 Deposon「评估对负采样口径敏感」在精神上是同源结论，且是教育测量学 30 年前的先例，可作评估批判的历史纵深。

**[T2-3] KnowEdu: A System to Construct Knowledge Graph for Education** 【经典（领域基准）】
Penghe Chen, Yu Lu, Vincent W. Zheng, Xiyang Chen, Boda Yang — IEEE Access 6:31553–31563, 2018（venue 经多处第三方引文核验）
链接：https://doi.org/10.1109/ACCESS.2018.2839607
相关性：教育知识图谱自动构建系统的代表（K-12 学科概念抽取 + 关系识别），提供「构建侧」pipeline 与课程级基准；Deposon 脑图构建侧可对标。

**[T2-4] MOOCCube: A Large-scale Data Repository for NLP Applications in MOOCs** 【经典（领域基准）】
Jifan Yu, Gan Luo, Tong Xiao, Qingyang Zhong, Yuquan Wang, Wenzheng Feng, Junyi Luo, Chenyu Wang, Lei Hou, Juanzi Li, Zhiyuan Liu, Jie Tang — ACL 2020, pp. 3135–3142（venue 经多处第三方引文核验）
链接：https://aclanthology.org/2020.acl-main.285/
相关性：700+ 课程、10 万概念、800 万行为的教育概念图谱仓库，并定义了「先修关系发现」任务（本质上就是概念图补全/链接预测）；后续 MOOCCubeX（Yu et al., CIKM 2021:4643–4652，经 dblp 核验）扩展为知识中心仓库——是 Deposon 若想换更大、更真实语义图做外部验证的现成基准。

**[T2-5] Design and Development of Semi-Automatic Concept Map Authoring Support Tool（KitBuild 谱系）** 【近年】
Aryo Pinandito, D. D. Prasetya, Yusuke Hayashi, Tsukasa Hirashima — Research and Practice in Technology Enhanced Learning, 2021（venue 经 scholar 出版信息核验）
链接：https://link.springer.com/article/10.1186/s41039-021-00165-3 （具体卷期未核验，按出版社页面为准）
相关性：KitBuild「补全式概念图」（kit-building：给定概念/连接词骨架让学生/系统补边）是与 Deposon「脑图补全」任务形态最接近的教育技术传统；其「与专家图逐边对照」的评分协议是 LOO 之外的标准答案。

**[T2-6] Concept Maps for Formative Assessment: Creation and Implementation of an Automatic and Intelligent Evaluation Method** 【近 3 年】
T. Bleckmann, G. Friege — Knowledge Management & E-Learning, 2023（venue 经 scholar 出版信息核验）
链接：https://repo.uni-hannover.de/items/0efe1ce7-d3db-42fe-9ad2-9f534cd7fff8
相关性：概念图自动评估方法（2023 年新作），给出自动评分与人工评分的一致性数字——为 Deposon「自动补全质量如何与人判对齐」提供评估协议模板。

**[T2-7] A Framework for Constructing Concept Maps from E-Books Using Large Language Models: Challenges and Future Directions** 【近 3 年】
B. Ma, L. Chen — LAK 2025 Workshops (CEUR Vol-3995)（venue 经 scholar 出版信息核验）
链接：https://ceur-ws.org/Vol-3995/DCLAK25_paper2.pdf
相关性：LLM 从电子书构建概念图的最新框架，并**以「挑战与未来方向」为主线**——与 v2.X「分工+边界」同体裁；证明该体裁在学习分析社区（LAK）可发表。

**[T2-8] Automatic Construction of Educational Knowledge Graphs: A Word Embedding-Based Approach** 【近 3 年】
Q. U. Ain, M. A. Chatti, K. G. C. Bakar, S. Joarder, R. Alatrash — Information 14(10):526, 2023（venue 经 scholar 出版信息核验）
链接：https://www.mdpi.com/2078-2489/14/10/526
相关性：词嵌入驱动的教育 KG 自动构建（无 LLM 的对照组），可作为「LLM 前时代」构建基线；其概念抽取 F1 与关系识别数字可作 labels-only vs embedding-only 的横向参照。

**交叉引用（已在 v19，不重复列条目）**：MindMap（Wen et al., ACL 2024，v19 [30]）——LLM 时代脑图组织证据做推理；[27][28][29]（2012–2020 概念图自动构建三篇）。

---

## 主题 3：规则基线与对抗鲁棒性（GT-2 定位）

**[T3-1] Deceiving Google's Perspective API Built for Detecting Toxic Comments** 【经典】
Hossein Hosseini, Sreeram Kannan, Baosen Zhang, Radha Poovendran — arXiv 2017（arXiv:1702.08138；未见正式出版记录，保守按预印本引用）
链接：https://arxiv.org/abs/1702.08138
相关性：最早展示「商用毒性检测器可被简单字符级扰动系统性绕过」的工作——关键词/浅层分类器对自适应攻击者无效的证据链起点。

**[T3-2] All You Need is "Love": Evading Hate Speech Detection** 【经典】
Tommi Gröndahl, Luca Pajola, Mika Juuti, Mauro Conti, N. Asokan — ACM AISec 2018, pp. 2–12（venue 经第三方引文核验）
链接：https://doi.org/10.1145/3270101.3270103
相关性：**GT-2 的最直接先例**——攻击者通过插入无害词（"love"）、拼写变体、词边界操纵，把 7 个仇恨言论检测器（含字符级、词级、Google Perspective）打到接近失效；证明「攻击者知道过滤器存在」时规则/浅层模型全面失守，与 GT-2 的 100% 绕过互为印证。

**[T3-3] Universal Adversarial Triggers for Attacking and Analyzing NLP** 【经典】
Eric Wallace, Shi Feng, Nikhil Kandpal, Matt Gardner, Sameer Singh — EMNLP-IJCNLP 2019, pp. 2153–2162（venue 经第三方引文核验）
链接：https://aclanthology.org/D19-1221/
相关性：输入无关的通用触发序列即可翻转分类/生成输出——说明即使不是「关键词表」，模型内部也退化为可被触发的模式匹配；为「规则基线的失败不是实现问题而是类别问题」提供论证素材。

**[T3-4] TextAttack: A Framework for Adversarial Attacks, Data Augmentation, and Adversarial Training in NLP** 【经典（工具/协议）】
John Morris, Eli Lifland, Jin Yong Yoo, Jake Grigsby, Di Jin, Yanjun Qi — EMNLP 2020 System Demonstrations, pp. 119–126（venue 经 aclanthology 核验）
链接：https://aclanthology.org/2020.emnlp-demos.16/
相关性：标准化文本对抗攻击库（16 种攻击：同义替换、字符插入、leet 化等）；GT-2 的攻击者操作集可直接用 TextAttack 组件形式化，使「100% 绕过」可复现、可与文献数字对照。

**[T3-5] On Adaptive Attacks to Adversarial Example Defenses** 【经典（方法学）】
Florian Tramèr, Nicholas Carlini, Wieland Brendel, Aleksander Madry — NeurIPS 2020, 33:1633–1645（venue 经第三方引文核验）
链接：https://proceedings.neurips.cc/paper/2020/hash/11f38f8ecd71867b42433548d1078e38-Abstract.html
相关性：**「评估防御必须假设自适应攻击者」的方法学宣言**——13 个防御在非自适应攻击下看似有效、在自适应攻击下全部失守。GT-2 实验设计的合法性依据：我们的攻击者知晓关键词表，正是文献要求的正确评估口径；反过来，任何「规则过滤有效」的 claim 都必须过这一关。

**[T3-6] Red Teaming Language Models with Language Models** 【经典（红队范式）】
Ethan Perez, Saffron Huang, Francis Song, Trevor Cai, Roman Ring, John Aslanides, Amelia Glaese, Nat McAleese, Geoffrey Irving — EMNLP 2022, pp. 3419–3448（venue 经 aclanthology 核验）
链接：https://aclanthology.org/2022.emnlp-main.225/
相关性：用 LM 自动生成攻击样本发现目标 LM 的失败模式——「自动化红队」范式出处；为 Deposon 用 LLM 充当 GT-2 攻击者（红队 LLM 生成的标签/表述）提供方法学引用与有效性证据。

**[T3-7] Bad Characters: Imperceptible NLP Attacks** 【近 3 年】
Nicholas Boucher, Ilia Shumailov, Ross Anderson, Nicolas Papernot — IEEE S&P 2022（venue 经 scholar 出版信息核验）
链接：https://arxiv.org/abs/2106.09898
相关性：不可见字符/同形字（Unicode 控制符、homoglyph）让人眼与关键词表同时失效——「标签/关键词过滤在编码层面即可被绕过」的现代证据；直接支撑「规则防线需要语义级而非字面级」的论点。

**[T3-8] Universal and Transferable Adversarial Attacks on Aligned Language Models（GCG）** 【近 3 年】
Andy Zou, Zifan Wang, Nicholas Carlini, Milad Nasr, J. Zico Kolter, Matt Fredrikson — arXiv 2023（arXiv:2307.15043；第三方引文一致按预印本引用，ICLR 2024 收录口径未核验，保守按 arXiv 引用）
链接：https://arxiv.org/abs/2307.15043
相关性：自动优化的通用对抗后缀对开源/闭源对齐 LLM 均有高迁移成功率——把「自适应攻击 100% 级别绕过」从分类器搬到生成式 LLM；GT-2 中「LLM 生成标签被规则表拦不住」与 GCG「对齐防线被通用后缀击穿」是同一现象的两面。

**[T3-9] Baseline Defenses for Adversarial Attacks Against Aligned Language Models** 【近 3 年】
Neel Jain, Avi Schwarzschild, Yuxin Wen, Gowthami Somepalli, John Kirchenbauer, Ping-yeh Chiang, Micah Goldblum, Aniruddha Saha, Jonas Geiping, Tom Goldstein — arXiv 2023（arXiv:2309.00614；未见正式发表记录，保守按预印本引用）
链接：https://arxiv.org/abs/2309.00614
相关性：系统评测困惑度过滤、改写、重述等「简单防线」对越狱攻击的效果——**困惑度/规则类防线在非自适应攻击下尚可、自适应攻击下显著退化**，正是 GT-2「关键词表对无知攻击者有效、对知情攻击者降至机会水平」的 LLM 安全侧镜像。

**[T3-10] The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections** 【最新】
Milad Nasr, Nicholas Carlini, Chawin Sitawarin, S. V. Schulhoff, 等（含 Florian Tramèr）— USENIX Security 2026（35th USENIX Security Symposium，经 scholar 出版信息核验）
链接：https://www.usenix.org/ （会议论文集；具体页码未核验）
相关性：Tramèr 2020 自适应攻击方法论在 LLM 防线上的最新完整重演——「攻击者后手」原则：凡不假设自适应攻击者的防御评估都系统性高估。v2.X 写 GT-2 时的总纲引用。

**[T3-11，备查] HateBench: Benchmarking Hate Speech Detectors on LLM-Generated Content and Hate Campaigns** 【近 3 年】
X. Shen, Y. Wu, Y. Qu, M. Backes, S. Zannettou, Y. Zhang — USENIX Security 2025（34th，经 scholar 出版信息核验）
相关性：LLM 生成的仇恨内容/运动对现有检测器的基准测试——「LLM 生成的违规标签绕过检测」的最新系统化证据；另见 Kahu & Ahuja 2025「All You Need is 'Leet'」（arXiv:2505.16263，leet 变体绕过仇恨检测，GT-2 关键词绕过的直接同类）。

---

## 主题 4：适用边界/阴性结果论文范式（「分工+边界」体裁先例）

**[T4-1] Workshops on Insights from Negative Results in NLP（第 1–6 届系列）** 【体裁基础设施】
第 1 届 Rogers, Sedoc, Rumshisky 编 — EMNLP 2020 workshop；第 2 届 Sedoc 等 — EMNLP 2021；第 3 届 Tafreshi 等 — EMNLP 2022；第 4 届 Tafreshi 等 — EMNLP 2023；第 6 届 Drozd 等 — 2025（均经 scholar/aclanthology 核验）
链接：https://aclanthology.org/2020.insights-1.0/ （第 1 届；其余各届 aclanthology 检索 "insights from negative results"）
相关性：**「阴性结果/边界分析」在 NLP 社区已成为有正式 outlet 的贡献类型**，且连续 6 届——v2.X 可以名正言顺地把「在什么图上语义先验失效、什么攻击下规则失效」作为主贡献而非 limitation 章节；投稿叙事可引用该系列的存在。

**[T4-2] Troubling Trends in Machine Learning Scholarship** 【经典（体裁宣言）】
Zachary C. Lipton, Jacob Steinhardt — Communications of the ACM 62(6):45–53, 2019（venue 经第三方引文核验）
链接：https://dl.acm.org/doi/10.1145/3317287 （另 arXiv:1807.03341）
相关性：ML 学术写作四类弊病（解释当证据、只在成功处报告、数学滥用、术语滥用）——「诚实报告失败与适用条件」是正当学术贡献的总纲式引用；v2.X 引言立论用。

**[T4-3] Show Your Work: Improved Reporting of Experimental Results** 【经典（报告规范）】
Jesse Dodge, Suchin Gururangan, Dallas Card, Roy Schwartz, Noah A. Smith — EMNLP-IJCNLP 2019, pp. 2185–2194（venue 经多处第三方引文核验）
链接：https://aclanthology.org/D19-1224/
相关性：期望值-方差-预算三要素报告框架——v2.X 多图扩展后，「报告性能分布而非单点」的规范出处；与「边界」叙事配套（边界=性能分布的非平凡区域）。

**[T4-4] Do ImageNet Classifiers Generalize to ImageNet?** 【经典（重测范式）】
Benjamin Recht, Rebecca Roelofs, Ludwig Schmidt, Vaishaal Shankar — ICML 2019, pp. 5389–5400（venue 经多处第三方引文核验）
链接：https://proceedings.mlr.press/v97/recht19a.html
相关性：重建分布内新测试集重测整个领域，发现排名稳健但绝对性能掉落——「不发新方法、只重测并刻画结论边界」也能发 ICML 的标杆先例。

**[T4-5] Evaluating the Evaluation of Diversity in Natural Language Generation** 【经典（评估之评估）】
Guy Tevet, Jonathan Berant — EACL 2021（Proceedings of the 16th Conference of the European Chapter of the ACL；venue 经 scholar 核验）
链接：https://aclanthology.org/2021.eacl-main.199/
相关性：标题即体裁——「评估的评估」：通过可控实验揭示常用多样性指标的失真条件。v2.X 对 LOO/负采样口径的边界刻画可明确对标这一体裁命名与结构（问题设定→指标/协议的失效条件→修正建议）。

**[T4-6] Underspecification Presents Challenges for Credibility in Modern Machine Learning** 【经典（可信性边界）】
Alexander D'Amour, Katherine Heller, Dan Moldovan, 等（40+ 作者，Google）— JMLR 23(226):1–61, 2022（venue 经多处第三方引文核验）
链接：https://jmlr.org/papers/v23/20-1335.html
相关性：证明同一 pipeline 在欠规范下沿未测维度行为分叉——「结论只在被测维度上成立」的形式化；支撑 v2.X 把「在哪些图族/攻击强度下结论成立」写成贡献而非免责条款。

**[T4-7] Mind the Gap: Assessing Temporal Generalization in Neural Language Models** 【经典（边界刻画实证）】
Angeliki Lazaridou, Adhi Kuncoro, Elena Gribovskaya, 等 — NeurIPS 2021, 34:29348–29363（venue 经多处第三方引文核验）
链接：https://proceedings.neurips.cc/paper_files/paper/2021/hash/f5bf0ba0a17ef18f9607774722f5698c-Abstract.html
相关性：沿时间维度刻画 LM 泛化的系统退化——「选一个未测维度做受控扫描并报告失效曲线」的完整模板，v2.X 的图类型/难度维度扫描可直接套用此结构。

**[T4-8] Are Emergent Abilities of Large Language Models a Mirage?** 【近 3 年（结论反转型）】
Rylan Schaeffer, Brando Miranda, Sanmi Koyejo — NeurIPS 2023（papers.nips.cc 2023 hash adc98a266f45005c403b8311ca7e8bd7，经第三方引文核验）
链接：https://proceedings.neurips.cc/paper_files/paper/2023/hash/adc98a266f45005c403b8311ca7e8bd7-Abstract-Conference.html
相关性：证明「能力涌现」是度量选择的伪影——**主张「现象是度量伪影」本身可获顶会认可（该文获 NeurIPS 2023 最佳论文奖之一，奖项细节未本次核验）**；为「Hits@3/方向一致率的成立条件依赖协议口径」这类主张提供最高规格先例。

**[T4-9] When Not to Trust Language Models: Investigating Effectiveness of Parametric and Non-Parametric Memories** 【近 3 年（「何时不可」标题型）】
Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das, Daniel Khashabi, Hannaneh Hajishirzi — ACL 2023, pp. 9802–9822（venue 经多处第三方引文核验）
链接：https://aclanthology.org/2023.acl-long.549/
相关性：直接以「何时不可信任」为题，刻画参数记忆 vs 检索记忆各自的失效区域并给出可操作的选用规则——「分工 + 边界」叙事的标题级先例：v2.X 的「LLM 先验管语义、结构模型管关系、规则过滤只防无知攻击者」正是同构的三方分工主张。

**[T4-10] Faith and Fate: Limits of Transformers on Compositionality** 【近 3 年（能力边界实证）】
Nouha Dziri, Ximing Lu, Melanie Sclar, Xiang Lorraine Li, Liwei Jiang, Bill Yuchen Lin, Peter West, 等 — NeurIPS 2023, 36:70293–70332（venue 经多处第三方引文核验）
链接：https://proceedings.neurips.cc/paper_files/paper/2023/hash/deb3c28192f979302c157cb653c15e90-Abstract-Conference.html
相关性：受控乘法/逻辑任务上证明 Transformer 组合泛化随规模退化（「推理退化为何答案猜测」）——能力边界的受控实证模板；与 T1-8 反转诅咒一起构成「LLM 结构语义能力边界」的证据对。

**[T4-11] The Dangers of Underclaiming: Reasons for Caution When Reporting How NLP Systems Fail** 【近 3 年（反向校准，必读）】
Samuel R. Bowman — ACL 2022（venue 经 scholar 核验：Proceedings of the 60th ACL）
链接：https://aclanthology.org/2022.acl-long.522/
相关性：**对阴性结果体裁的元批评**——「X 不行」的结论同样常被协议伪影制造（prompt 没调好、预算不对等）。v2.X 引用它可做自我设防：我们的边界 claim（规则过滤无效、先验在 filler 上弱）必须给出对称的强基线与充分搜索，否则落入 underclaiming 陷阱。这条是写「边界」论文时最有区分度的引用。

---

## ⑤ 定位建议（给 v2.X 论文）

**定位 1（labels-only 先验强度的横向坐标）**：把 Deposon 的 named Hits@3 0.48–1.0 放进三段式坐标系——(a) 零样本/少样本纯 LLM：GPT-4 在 KG-LLM 评测中弱于微调小模型（T1-3），Wadhwa et al. 显示精心 prompt 才接近全监督（T1-6）；(b) 文本/标签基模型：KG-BERT（T1-1）与 MKGL（T1-4）证明标签文本本身携带结构信号；(c) 检索+LLM 混合：KICGPT（T1-2）显示混合优于单方。Deposon 的 0.48–1.0 图间大跨度恰好与「先验强度依赖图的语义化程度」一致——**建议把图间方差本身报告为发现**（哪些图语义先验近乎完备、哪些近乎失效），而不是只报均值；这正是 T4-4/T4-7 的体裁。

**定位 2（方向一致率 ≥0.96 的写法）**：对照反转诅咒（T1-8/T1-9）——裸 LLM 对 A→B 与 B←A 的泛化是系统性失败的，Deposon 在真实语义图 + 结构约束下达到 ≥0.96 是反直觉的正结果，值得单列小节并与 T1-8 做显式对照实验（把边的方向随机翻转后先验的方向判别准确率），同时用 T4-11 自我设防（报告充分搜索的强基线）。

**定位 3（GT-2 的体裁升级）**：GT-2「攻击者 100% 绕过关键词表」目前是实验结果；按 T3-5/T3-10 的方法学，可升级为**方法学主张**：「对知情自适应攻击者，字面级规则防线的期望效果是机会水平」——这不是 Deposon 的失败，而是该防线的类别属性（T3-2/T3-7/T3-8/T3-9 四组独立证据链）。写作上引用 T3-5 确立评估口径合法性，引用 T3-2/T3-11 说明结论与 2018–2025 年五条证据链一致，则 GT-2 从「负面消融」变为「边界定理的实证版」。

**定位 4（「分工+边界」的体裁合法性）**：三层先例齐备——(i) 体裁宣言：T4-2/T4-3（诚实报告边界是贡献）；(ii) 顶会实证模板：T4-4（重测）、T4-5（评估之评估）、T4-6（欠规范）、T4-7（失效曲线扫描）、T4-8（度量伪影，最佳论文级）、T4-9（「何时不可」标题）、T4-10（能力边界受控实证）；(iii) 专门 outlet：T4-1 六届阴性结果 workshop。建议 v2.X 引言显式声明体裁（"a boundary analysis in the tradition of [T4-4][T4-7][T4-9]"），并以 T4-11 作为自我设防引用——这是与「新方法刷分」叙事差异化、且审稿人难以用「没有 SOTA」攻击的写法。

**定位 5（脑图侧基准与教育测量纵深）**：构建/补全协议用 T2-5（KitBuild 补全式概念图，与 Deposon 任务形态最近）+ T2-4（MOOCCube/MOOCCubeX 作为外部验证图源的候选）+ T2-7（LLM 构建概念图的同体裁近作）；评估口径批判的历史纵深用 T2-2（1996 年「任务-评分依赖」），可与 v19 [10][11] 的 2017–2023 年负采样批判首尾呼应——「评估口径敏感性」横跨 30 年两个社区，是 v2.X 评估章节的强叙事。

**核验状态汇总**：venue/页码经第三方引文或 aclanthology 核验——T1-2, T1-4, T1-6, T1-7, T1-8, T1-10, T2-1, T2-2, T2-3, T2-4, T3-2, T3-3, T3-4, T3-5, T3-6, T3-7, T3-10, T4-2, T4-3, T4-4, T4-5, T4-6, T4-7, T4-8, T4-9, T4-10。经 scholar 出版信息核验（未第三方）——T1-3, T1-9, T2-5, T2-6, T2-7, T2-8, T3-11, T4-11。保守按 arXiv 预印本引用——T1-1, T3-1, T3-8, T3-9。未充分核验、引用前需精读——T1-11。T4-8 的「最佳论文奖」传闻未核验，建议正文不写奖项只写 NeurIPS 2023。

**明确负面结果**：①「LLM 抽取图谱的方向错误率」这一精确量化主题未找到专门文献（最接近的是 T1-11 的 schema 约束错误分类与 T1-8 的反转诅咒）——该空白本身可在 v2.X 中作为贡献点声称（"to our knowledge, the first quantification of direction consistency of LLM priors on real semantic maps"），但声称前建议再检索一次 2025–2026 新作。②「概念图补全（completion）作为独立任务」文献稀缺，教育技术侧主流是「构建+评分」而非「补全」——Deposon 的脑图补全任务设定确有新颖性空间，但需注意 KitBuild 的 kit-building 实质上就是补全，related work 必须承认这一点以避免被审稿人指为忽视。
