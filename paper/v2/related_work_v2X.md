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
图与先验同模型族（同源污染），且图为 30–45 节点的小规模 DAG。

方向语义上，Reversal Curse（Berglund et al., ICLR 2024）及其机制解释
（Wang & Sun, ICLR 2026）预言 LLM 对「A→B 成立」无法推出「B→A」，而我们实测
先验边与金边的方向一致率 ≥0.96、hub 反向边为 0（四图）——与反转诅咒形成对照，
我们将其单列小节并附方向翻转对照（§4.6），同时标注 v1.9 锚点图上曾观测到
系统性方向反转（占位标签特异现象），两种现象并存恰说明方向表现的条件性。
MKGL（NeurIPS 2024）关于标签文本自带结构信号的「三词语言」论证，与我们的
n-gram 词法基线获胜现象互相印证。Zhang et al.（ACL 2025）对 KGC prompt 结论
泛化性的系统复测提醒我们：所有 prompt 相关结论都限定在单模型族内。

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
的仿射拥塞 PoA=4/3 界是经典锚点——**我们实测 median PoA=1.33 几乎精确落在
Pigou 界上**，并以 Christodoulou et al.（2014）把守恒账挂接为「降低有效 PoA
的协调机制」（空位 3 的实证叙事）。

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
（USENIX Sec 2025）。我们的 GT-2（攻击者 100% 绕过关键词表、规则基线降至
机会水平 27.5%）与该证据链一致，按 Tramèr/Nasr 口径升级为方法学主张。

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
3. **实证空位**：median PoA=1.33 为 Pigou 4/3 界的实例级复现；方向一致率 ≥0.96
   与 Reversal Curse 的直接对照；规则防线在自适应攻击下失效的第六个独立实例。
4. **体裁声明**：boundary analysis + division-of-labor，配合预登记判死刑则与
   「Dangers of Underclaiming」自我设防。
