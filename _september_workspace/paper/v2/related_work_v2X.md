# Related Work（v2.X 论文草案，文献锚点已核验）

> 来源：reviews/literature_scan_v2X_A.md（40 条，博弈/机制/势博弈/PoA）与
> reviews/literature_scan_v2X_B.md（40 条，LLM-KGC/概念图/对抗/边界体裁），
> 全部经 scholar + web_search 交叉核验，未核实条目已标注。本节为论文 §2 草案。

## 2.1 结构驱动的链接预测

经典结构启发式构成我们基线注册表的 A 族：共同邻居、Adamic-Adar、Jaccard、
Preferential Attachment、Katz 与 Personalized PageRank——本文在 20 张图上对全部六臂
做了同协议实测（外加 degree 与 random），并补入一臂纯 numpy 浅近似 Node2Vec
（如实标注非完整实现）。可训练的 KGE 系列（TransE/ComplEx/RotatE）在 20 图规模
方可训练，列为 v2.1 排期项（注册表 ⬜，不回避）。我们的扫描显示：词法余弦
（字符 n-gram TF-IDF）这类常被忽视的零成本基线在 5/20 张图上击败了我们的主臂，
此类「潜伏 BOSS」正是注册表机制要制度性防止的（见 §4.4 的披露规则）。

## 2.2 LLM 语义先验与方向语义

LLM 用于知识图谱补全的近三年证据链给出我们数字的横向坐标：KICGPT
（Findings of EMNLP 2023）以检索+LLM 重排超过纯 LLM；KG-LLM/Yao et al.
（ICASSP 2025）显示零样本 GPT-4 弱于微调 6-7B 模型；Wadhwa et al.（ACL 2023）
表明即使精心 prompt，GPT-3 也仅接近全监督关系抽取。我们 labels-only 先验在真实
语义图上的 named Hits@3（0.484–1.000）高于上述零样本区间，但须声明两点降级：
原口径「图与先验同模型族（同源污染）」须按 GT-3b 后口径更新——跨厂商检验
已完成，E3 doubao（ByteDance）4/4、E4 deepseek（DeepSeek）6/6，三模型族
合计 0 域先验 ≤ 场（0 败绩）、全 ok 域 Kendall W=1.0（docs/Findings_GT3.md），
「同源污染 artifact」假说被实质性削弱但**未排除**（残余局限：三族均为中文优化
大模型，训练语料可能共享公开中文知识）；另一降级声明不变：图为 30–45 节点的
小规模 DAG。

方向语义上，Reversal Curse（Berglund et al., ICLR 2024）及其机制解释
（Wang & Sun, ICLR 2026）预言 LLM 对「A→B 成立」无法推出「B→A」，而我们实测
先验边与金边的方向一致率 ≥0.96、hub 反向边为 0（四图）——与反转诅咒形成对照，
我们将其单列小节并附方向翻转对照（§4.6），同时标注 v1.9 锚点图上曾观测到
系统性方向反转（占位标签特异现象），两种现象并存恰说明方向表现的条件性。
MKGL（NeurIPS 2024）关于标签文本自带结构信号的「三词语言」论证，与我们的
n-gram 词法基线获胜现象互相印证。Zhang et al.（ACL 2025）对 KGC prompt 结论
泛化性的系统复测提醒我们：prompt 相关结论的泛化面须按 GT-3b 后口径标注——
已扩展至三个模型族（Kimi 系、ByteDance doubao、DeepSeek），但三族均为
中文优化大模型，非中文模型族的检验仍为开放局限。

## 2.3 概念图与脑图：任务与评估

概念图由 Novak & Cañas（2008）定义并奠基。Ruiz-Primo & Shavelson（1996）
在三十年前即指出概念图评估的「任务-评分依赖」——得分对协议高度敏感，
这与我们 v1.9 对负采样协议的批判（采样器敏感性）构成跨三十年的同一教训，
本文评估章节以此组织叙事纵深。基准方面，KnowEdu（IEEE Access 2018）与
MOOCCube/MOOCCubeX（ACL 2020 / CIKM 2021）提供教育知识图谱参照。
**必须显式承认**：KitBuild「补全式概念图」（Pinandito et al., 2021）在任务形式上
与我们一致（给定部分概念图补全缺失关联），LLM 侧同体裁近作见 Ma & Chen
（LAK 2025）；我们与该线的区别在于：不补全人工课程图，而是用受控语料
（结构否定族 + LLM 生成族）系统扫描信号价值域，且全部判定预登记。

## 2.4 博弈论透镜：势博弈、网络形成与 PoA

把补全建模为博弈有四个理论锚点。Monderer & Shapley（GEB 1996）的势博弈框架
与 Rosenthal（1973）拥塞博弈给出势函数存在性的经典条件；Sandholm（2010）
的群体最好响应流证明：确定性最好响应动态在群体极限下沿势函数梯度上升——
这是我们把「mean-field 确定性反向 = 无噪声最好响应动态」升格为理论主张的
最近支点，GT-1 的实测收敛差（gap 0.30，20/20）与其一致。Candogan et al.
（MOR 2011）的博弈流分解与 Parise & Ozdaglar（Econometrica 2023）的 graphon
连续极限，分别提供「场=图流分量」与「大图极限」的进一步形式化路径——
我们检索确认该理论交集与扩散生成模型文献互不引用，此交叉空位是本文理论贡献
的主声称（空位 1）。网络形成与攻防方向上，Jackson & Wolinsky（1996）、
Fabrikant et al.（2003）奠基，Ma et al.（TCS 2014）「挖掘隐藏链以达均衡」
与 Waniek et al.（Nat. Hum. Behav. 2018；Stackelberg 边隐藏 2023）最接近
对抗性边操作场景；我们与 adversarial robustness 赛道显式划界：攻击者不是
扰动输入以翻转模型输出，而是在规则已知下生成语义陷阱（见 §2.5）。
PoA 方面，Koutsoupias & Papadimitriou（1999）与 Roughgarden & Tardos（2002）
的仿射拥塞 PoA=4/3 界是经典锚点。我们的实证是**分布级 PoA 报告**（应用文献
稀少，Benita 2020 为例外）：median PoA=1.5（13 张有限值图）。必须如实声明：
操作化 PoA=field_mean/max(自利臂) 与经典 worst-case-NE/社会最优比值是
**不同度量**，成本结构是否仿射/可分的前提未闭合，故中位数数值上与 Pigou 4/3
的对齐仅为**巧合性对齐，不主张「实例级复现」**；且族 L 4 张真实语义图中
2 张 PoA<1（0.5、0.75）并列披露，构成该叙事自带的边界证据。在此限定下，
我们以 Christodoulou et al.（2014）把守恒账挂接为「降低有效 PoA 的协调机制」
（空位 3 的实证叙事）。

## 2.5 机制设计、审计与自适应攻击

机制设计侧，Conitzer & Sandholm（2006）的承诺计算理论、Dekel et al.（2010）
的激励兼容机器学习、Hardt et al.（2016）的策略分类，与 Dütting et al.
（WWW 2024）的 LLM 机制设计构成上下文；审计侧 Raji et al.（2020）给出组织层
算法审计框架，Jia et al.（2021）的 Proof-of-Learning 给出密码层可验证计算。
我们的守恒账定位为**运行期逐实例不变量**（事后溯源与密码证明之间的空层，
空位 2），写作时与 PoL 显式划界。自适应攻击侧，Tramèr et al.（NeurIPS 2020）
的自适应攻击宣言与 Nasr et al.（USENIX Sec 2026）的「攻击者后手」分析提供了
方法学合法性；规则防线的失效有五条独立证据链：Gröndahl et al.（AISec 2018）、
Hosseini et al.（2017）、Kahu & Ahuja（2025）、Jain et al.（2023）与 HateBench
（USENIX Sec 2025）。我们的 GT-2 结果须按**双轨口径**如实并述：预登记主 LOO 协议
（crossval §三）的机械判定为 **no_separation**——rule_filter 仅 −7.5pp，
未达 20pp 阈值，「攻击强度未达决定性强度」如实归档；另一条题库轨
（skills §三）则为 rule=27.5%≈机会水平（25%）。故「规则防线失效」目前
仅在题库轨成立，与上述五条证据链方向一致但强度未定；GT-2 升级（多陷阱
强度）列为 v2.1 候选后再谈防御结论，此处不升级为方法学主张。

## 2.6 边界分析与阴性结果体裁

本文体裁自我声明为 boundary analysis，先例三层齐备：宣言层 Lipton &
Steinhardt（CACM 2019）与 Dodge et al.（EMNLP 2019）；顶会实证模板层
Recht（ICML 2019）、Tevet & Berant（EACL 2021）、D'Amour et al.（JMLR 2022）、
Lazaridou et al.（NeurIPS 2021）、Schaeffer et al.（NeurIPS 2023）、Mallen et al.
（ACL 2023）、Dziri et al.（NeurIPS 2023）；专门 outlet 层 Insights from Negative
Results workshop（已办六届）。Bowman（ACL 2022）「The Dangers of Underclaiming」
是我们诚实降级的自我设防参照：所有否定性主张（融合稀释、场边界、规则失效）
均以预登记判死刑则和机械判定为限，不超出数据。

## 定位声明（§1 引用）

1. **理论空位**：势博弈/随机稳定/群体极限/图流分解/graphon 极限五簇理论与
   扩散生成模型互不引用——「场=势函数最好响应极限」落于交集（A 路空位 1）。
2. **系统空位**：守恒账处于承诺计算—组织审计—可验证计算三层之间（A 路空位 2）。
3. **实证空位**：分布级 PoA 报告（median PoA=1.5，13 图有限值；操作化口径与
   经典 PoA 不同度量，与 Pigou 4/3 的对齐仅为巧合性对齐，不主张实例级复现；
   族 L 2/4 图 PoA<1 并列披露）；方向一致率 ≥0.96 与 Reversal Curse 的直接对照；
   规则防线失效在题库轨（rule=27.5%≈机会）与五条外部证据链一致，主协议
   no_separation 如实归档。
4. **体裁声明**：boundary analysis + division-of-labor，配合预登记判死刑则与
   「Dangers of Underclaiming」自我设防。

---

*修订记录（2026-08-30）：按 reviews/review_coach_v2X_outline.md 闭合 M3/M4/M5——§2.2 同源污染改「削弱但未排除（残余=三族均中文优化模型）」口径并同步 prompt 泛化面（GT-3b：doubao 4/4、deepseek 6/6、0 败绩、W=1.0，docs/Findings_GT3.md）；§2.4 PoA 撤回「median 1.33 实例级复现 Pigou 界」，改为分布级报告（median 1.5/13 图）+操作化差异声明+巧合性对齐+族 L 2/4 图 PoA<1（0.5、0.75）并列披露；§2.5 规则基线改双轨口径（主 LOO 协议 no_separation、−7.5pp / 题库轨 27.5%≈机会），不再升级为方法学主张；定位声明第 3 条同步。数字均追溯 outline_v2X.md 修订段与 docs/Findings_GT3.md。*
