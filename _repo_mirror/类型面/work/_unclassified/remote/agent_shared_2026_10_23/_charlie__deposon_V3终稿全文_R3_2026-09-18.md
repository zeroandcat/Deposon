# 判死作为资产：deposon V3 博弈论转向的一周预登记判死实验

**The Kill as an Asset: A Pre-Registered One-Week Kill Experiment on the Game-Theoretic Turn of deposon V3**

> 双盲版说明：本文为双盲评审版；作者身份、协作通道与仓库路径均已匿名化，冻结制品的 SHA-12 指纹不因匿名化而改变。本文一切数字均可对回到冻结 JSON 字段与核验记录（披露见第 9 节）。

---

## 摘要

在可审计性与可证伪性的五线坐标系中，本文报告 deposon V3 博弈论转向的一周判死实验（D0–D7）。实验以预登记纪律执行：判死线与判定函数先行冻结为 SHA-256 锚，判定为纯函数机械复算，全程零 LLM 判定调用。四路径终局拍板：P-A 均衡稳定化 PASS（60 cells 复现率 51/60＝85.0%，540 账目守恒（构造性））；P-C 跨模态幂律 FAIL_H0（R²＝0.1986/0.2670 双低于阈值）；P-E 物理公式 PARTIAL_PASS（A 通道独立三层判据）；P-F 观察者 PASS（45/45 守恒）。P-L v3 三态分离：尺寸缩放 FAIL（R²＝0.7447）、跨主干 β 置信区间重叠 PASS（开源 3/3、闭源 3/3；主跑 5 主干仅 3/5 完整，其余 INCOMPLETE／不可达）、判官误报率 4.4%（2/45）GRAY；17 项补测生态按状态口径为 11 PASS（含 1 项附 UNVERIFIED 勘误注记）、2 GRAY、1 UNVERIFIED、2 PARTIAL、1 FAIL。资产层（18 冻结锚、5 制品、schema 21/21、22 题注双指纹 22/22）全程零触动。负结果、灰区与叙述层数字漂移修正均如实入文；另报告零 LLM 文献检索基础设施（DAS-2M）的可用性与四条边界。

**关键词**：可审计性；可证伪性；预登记判死；LLM 评测完整性；博弈论验证；守恒不变量

## Abstract

In the five-line coordinate system of auditability and falsifiability, this paper reports the one-week kill experiment (D0–D7) on the game-theoretic turn of deposon V3. The experiment ran under pre-registration discipline: kill lines and verdict functions were frozen first as SHA-256 anchors; adjudication was pure-function mechanical recomputation, with zero LLM judging calls throughout. The final adjudication of the four paths reads: P-A (equilibrium stabilization) PASS, with a 60-cell reproduction rate of 51/60 = 85.0% and full conservation of the 540-account ledger (a constructive identity); P-C (cross-modal power law) FAIL_H0, with R² = 0.1986 / 0.2670 both below the pre-registered threshold; P-E (physical formula, D_fix2) PARTIAL_PASS, resting on an independent channel-A three-layer criterion; P-F (the observer) PASS, with 45/45 conservation. P-L v3 adjudicates three separated states: size scaling FAIL (R² = 0.7447); cross-backbone β-confidence-interval overlap PASS (3/3 open-source and 3/3 closed-source), with cross-backbone robustness assessed as grouped confidence-interval testing under a main run of 3/5 completed backbones (the remainder incomplete or unreachable); judge false-positive rate 4.4% (2/45) GRAY. The 17-item adendum ecosystem (adendum: the repository's native spelling for pre-registered supplementary test items) resolves, by status, to 11 PASS (one carrying an UNVERIFIED erratum note), 2 GRAY, 1 UNVERIFIED, 2 PARTIAL, and 1 FAIL. The asset layer—18 frozen anchors, 5 artifacts, a 21/21 schema check, and 22/22 caption dual fingerprints—remained untouched. Negative results, gray zones, and narrative-layer number corrections are reported as they occurred, together with the usability and four boundaries of a zero-LLM literature-retrieval infrastructure (DAS-2M).

**Keywords**: auditability; falsifiability; pre-registered kill experiment; evaluation integrity; game-theoretic verification; conservation invariants

---

## 1 Introduction: A One-Week Kill Promise on a Game-Theoretic Turn

大型语言模型的推理能力经历了一个以性能为中心的时代：思维链提示让推理过程本身成为机器生成的产物 [1]；随后，忠实性研究破坏了「解释即计算」的默认假设——模型给出的解释并不总是产生答案的真实计算过程 [2, 3]。当推理性能不再稀缺，问题从「多好」转向「第三方能复算什么」。本文所在的研究线将这个问题操作化：可审计性（auditability）＝第三方可复算性；可证伪性（falsifiability）＝预登记判定的可执行性；记账（bookkeeping）＝承诺–执行–验证闭环 [4]。沿这一坐标系，一条综述线把外部工作组织为五条审计线：过程验证（process verification，审计步骤）、思维链忠实性（chain-of-thought faithfulness，解释不是计算）、评测完整性（evaluation integrity，基准自身的账本）、博弈论验证（game-theoretic verification，激励使诚实可查）与守恒和物理先验（conservation and physical priors，不变量作为担保）[4]。

前作 [5] 在 LLM 推理路径之上构建了一个可审计、守恒保证、经博弈论测试的散射层，并以其冻结 JSON 账本演示了「逐字段可复算」的记账形态。deposon V3 是该线向博弈论中心的重建；V3X 则是它的判死程序：在 D0（2026-09-11），项目作出一周判死承诺——七天之内，预登记的判死线对转向的核心假设作出终局拍板，零结果与负结果同样作为交付物。

本文报告这次判死的全部结果。其主张链是：**判死是资产**——零结果经预登记（判死线先冻结＋纯函数判定＋SHA-256 锚）后成为可复算、可追加、可外部审计的记录；**四路径终局拍板**给出混合判定（PASS / FAIL_H0 / PARTIAL_PASS / PASS）且不作粉饰；**P-L v3 三态分离**把一个曾被误读为「通过」的统计量修正为代数恒等式伪影，并以三态独立判死重建该方向——跨主干稳健性为主跑 5 主干仅 3/5 完整（其余 INCOMPLETE／不可达）下的分组置信区间检验；**17 项补测生态**以状态与成本双口径如实分解；**资产层**（18 冻结锚、5 制品、schema 21/21、22 题注双指纹 22/22）全程零触动；全部实验方向在五线坐标系中获得映射定位（第 2.8 节）；另附**零 LLM 文献检索基础设施**（DAS-2M）的可用性与边界（第 6 节），以及**两层 AI 使用披露**（第 9 节）。

本文遵循三档证据语言 [4]：closed（预登记档）、consistency（一致性证据档）、motivation only（仅动机档）。四路径预登记判定为 closed 档运行实例（P-G 为 consistency 档，17 项补测生态含 GRAY/UNVERIFIED/PARTIAL 终态）；PASS、FAIL_H0、PARTIAL_PASS、GRAY 等标签是判定函数在冻结判死线上的取值，而非叙述层修辞。

---

## 2 Related Work: The Five-Line Coordinate System of Auditability

### 2.1 Operational Definitions and the Three-Tier Register

本文的文献坐标系来自同作者线的综述工作 [4]（双盲版以第三人称引用，关系在第 9 节披露）。其三个操作定义为：可审计性＝「一个主张的支持是冻结记录，声明资源条件的审计者可以机械复核」；可证伪性＝「预登记判定可以执行并给出二值或多值裁决」；记账＝「承诺–执行–验证的闭环」。其三轴分类为：组织轴（衍生任务／输出选择／重算成本）、属性轴（①主张及其推导 ②主张者的编辑与选择 ③重算成本 ④人类审计接口 ⑤预登记 ⑥支撑范围）、证据强度轴（closed／consistency／motivation 三档）[4]。该综述在已核验文献库内组织了 60 件外部工作并声明其定位主张可被单一发现证伪；本文继承其词汇与判档语言，并按下文五线逐线浓缩（译述改写，非搬运）。

### 2.2 Line 1: Process Verification（过程验证）

过程验证把「步骤」作为审计单元：训练验证器以解决数学应用题 [6]、对逐步推理做过程级奖励 [7]，以及围绕测试时扩展的验证设计综述 [8]。L1 的失败模式是「奖励了错误步骤」与「验证器与被验证者共谋」。V3X 与 L1 的接触点在判定层：四条路径的判死函数以冻结插件脚本执行（第 3 节），判定即步骤审计——每个判定可由第三方以同一脚本复跑。

### 2.3 Line 2: Chain-of-Thought Faithfulness（CoT 忠实性）

L2 的记账单元是「给出的解释」与「产生答案的计算」之间的关系。扰动协议（截断、改写、填充思维链后观察答案是否变化）与偏置植入协议（诱导偏置答案后观察解释是否事后合理化）是两条主流测量机制 [2, 3]。第二个时代抬高了赌注：强化学习直接训练思维链本身 [9]，监控推理模型行为与奖励促成的遮蔽随之成为活跃方向 [10, 11]。V3X 与 L2 的接触点是 P-K（判官研究）：当评测制品本身是 LLM 生成物，「证词」与「计算」的区分同样适用于判定通道（第 5.5 节）。

### 2.4 Line 3: Evaluation Integrity（评测完整性）

L3 审计「基准自身的账本」：LLM-as-a-judge 与大模型评测的两条综述线 [12, 13]、泄漏与复现性危机 [14]、数据污染检测族——含改写样本下的污染重思 [15]、黑盒污染证明 [16]、检测假设的系统审计 [17]、基于性能的 ConStat [18]、RL 后训练污染检测 [19] 与推理模型下检测器的脆弱性 [20]。判官可靠性是 L3 在本项目的直接落点：可靠性不等于效度（大规模系统审计发现一致率并不蕴含度量效度）[21]；自偏好证据（「评估者自恋」命题的健全性检验 [22]、同族评审偏置的基础实证 [23]）共同表明 LLM 判官的偏向必须被预登记协议显式约束。P-K 的误报率灰区（第 5.5 节）与 P-L v2 的代数恒等式伪影（第 5.1 节）正是两类被 L3 式审计捕获的 L3 式失败；复现性纲领 [24]（NeurIPS 复现性计划的报告）则为「0-LLM 可复算」提供了制度先例。

### 2.5 Line 4: Game-Theoretic Verification（博弈论审计）

L4 是本转向的近邻线，篇幅也最重。传统背景：以辩论做 AI 安全验证 [25]、合作 AI 与机制设计基础 [26]。当代工作把「谁来验证基准」变成机制设计问题：机制设计中的概率化验证 [27]；去中心化 LLM 评测信任 [28]；基于区块链的去中心化协同评测框架 [29]；去中心化评测协议 DEP [30]；以及激励侧风险——RLVR 可使模型博弈验证器、走向奖励黑客 [31]。面向代理行为的执行层：以保证金追索权结算代理副作用 [32]；代理行为治理框架 [33]；鲁棒代理补偿（RAC）[34]；工程标准层的信任无关代理注册（ERC-8004 草案，非同行评审 [35]）。与本转向直接同域的工作池内登记仅此一件——以博弈论框架使 LLM 评估与人类偏好对齐 [36]；其为评估侧设计，而 V3 是其实验侧对应。V3X 的 P-A（均衡稳定化）与 P-F（观察者）在第 4 节给出 L4 主张的判死实例。

### 2.6 Line 5: Conservation and Physical Priors（守恒与物理先验）

L5 把不变量作为担保：哈密顿神经网络以守恒结构约束学习动力学 [37]；物理先验嵌入机器学习的系统纲领 [38]；对物理信息网络失败模式的系统刻画 [39]。综述矩阵中「运行时不变量审计」的机器学习实例目前只登记了本线第一作 [4, 5]。V3X 与 L5 的接触面最宽：P-A 的 540 账目守恒、P-E 的物理公式检验与 P-G 的双曲输运几何（第 4 节）。

### 2.7 Anchoring the First Work（前作锚定）

第一作 [5] 在综述 [4] 中以披露自引进入同一矩阵、同一判档与同一登记规范，其冻结数字按「引用而非复测」（quote-not-remeasure）纪律转录：空间主张的最大偏离 0.8569（O(1) 量级偏离）；方向余弦最小值 −1.0；分布级协调比（ECR，distribution-level coordination ratio——注意非 price of anarchy 口径）中位数 1.333（覆盖 20/22 图，分母 22）；逐路径审计偏离最大值 2.220446049250313×10⁻¹⁶（容差 10⁻⁶）。三项主张在该矩阵下被证伪并作为内容保留——这为本文提供了方法论先例：判死记录本身是可复算资产，而非附属品。

### 2.8 Mapping V3X Directions onto the Five Lines

下表把 V3X 的实验方向映射入五线坐标系（主／次线与判档沿架构蓝图建议，依据列由本稿填写）：

| 方向 | 主线 | 次线 | 判档 | 映射依据（本稿填写） |
|---|---|---|---|---|
| P-A 均衡稳定化 | L4 | L5 | closed | KT_A1 SPEC（SHA-12 78b71d404366）预登记；540 账目守恒（9/9 模型残差为零；构造性恒真，见第 4.1 节注）＋BOSS-P-A1/2/3 三重可分性（倍数均值 145.8182×（口径见第 4.1 节注）、PG 形式占比 13.6%（3/22，分母 22）、ESS 重合 0%（0/22，分母 22）） |
| P-C 跨模态 dpath | L3 | L2 | closed | KT_C1 SPEC（59d8f56347d5）预登记；两相划分下幂律 FAIL_H0（R²＝0.1986/0.2670）＋dpath 判定 8/9（分母 9 模型） |
| P-E 物理公式（D_fix2） | L5 | L3 | closed | spec 五锚沿锚注册表（03c6c01f3697）派生；D_fix2 分布 8/1/0（分母 9 模型）＋逐模型 Spearman −0.832／+0.941＋A 通道独立三层判据 |
| P-F 观察者 | L1 | L4 | closed | P_F_V0_1_UPGRADE（b10fae0da66d）预登记；9 模型×5 cells 45/45 守恒＋4 BOSS INLINE（NBS 实算未拍平＋Shapley／Nash-Q／Habermas 退化协同） |
| P-L v3（含 P-K） | L3 | — | closed（多值运行：FAIL／PASS／GRAY 并存） | 三态分离（判死线沿 D6 提案预期表冻结）；Phase 1 R²＝0.7447／Q＝0.1929 FAIL；Phase 2 开源 3/3、闭源 3/3 PASS；P-K FPR 4.4%（2/45）GRAY；OR 组 1/6 GRAY |
| P-G V0.1 双曲输运 | L5 | — | consistency 起步 | d_H/d_E 放大比 ≈5×（区间 4.4–8.0）＋ρ_H,vs,E＝1.0000（伪影排查注见第 4.5 节）＋5 锚真值 5/5 PASS；经裁决暂不定位进 V4 议程 |

映射表各格不含排他性措辞，下列两处均为同域关系陈述：L4 内评估侧的博弈论对齐工作 [36] 与本转向同域而形态不同；L5 内运行时不变量审计在综述 [4] 的已核验库内目前登记了本线第一作 [5] 一件机器学习实例。

---

## 3 The Kill Architecture: Pre-Registration and the Asset Layer

### 3.1 Pre-Registration Discipline

判死程序的四条纪律先于一切数据冻结：

1. **判死线先冻结**。四条路径各绑定一份 SPEC 制品，其 SHA-12 锚在数据产生前登记（P-A：78b71d404366；P-C：59d8f56347d5；P-F：b10fae0da66d；P-E 的五枚锚沿锚注册表 03c6c01f3697 派生）。阈值与判定规则写入 SPEC，事后不得为新数据调整阈值。
2. **判定为纯函数**。全部判定由冻结插件脚本机械评估，判定层 LLM 调用次数为 0（D7 终局报告铁律 1：0 LLM 调用）；判定可由第三方以同一脚本与同一冻结数据复跑。正文所用判定量在此集中定义：T/R/A＝抽取值与 gold 严格相等／不等／缺失弃权（skill_a 源 L55–69）；Q＝尺寸塌缩归一化残差；D_fix2／dpath 判定见 KT-C1 SPEC 与 P-C 冻结 JSON；定义逐项挂对应冻结插件／SPEC 源。
3. **退化预检横切**。委托链继承四类退化预检（常量向量、检测率与 SECURE 并存、逐模型逐字相同、闭合计数出入），并落为横切检查：输入向量方差＞0、秩不恒同、标签非硬编码、检测率不低于随机基线，任一失败即记 UNVERIFIED。
4. **复现前提冻结**。随机种子、超平面参数、编码规则与汉明阈值在各通道 SPEC 中冻结；三态分离语言（尺寸缩放／跨主干／崩溃残差）独立判死，不得合并陈述。

四个外部 LLM 协作通道（双盲版匿名；下称通道甲–丁）对 P-L v2 的根因给出完全收敛的独立诊断（第 5.1 节），并合并出 P-L v3 方案；其产物与全部实验制品以内容寻址方式冻结（下节）。写作与判定的分工纪律沿既有惯例：起草、数字核验、文献核验与双审由不同通道承担（第 9 节）。

### 3.2 The Asset Layer

资产层在 D0–D7 全程零触动，并在 D7 复验（自验清单八件）：

| 资产 | 复验结果 | 锚（SHA-12） |
|---|---|---|
| 18 冻结锚 | 18 条全 PASS、0 fail、0 missing（2026-09-16T23:32 复测）；「零触动」机读标记为真 | 沿 schema v1 |
| 5 制品 JSON | 五件 SHA-12 全命中（四个外部 LLM 协作通道与一个任务派发通道的产物） | efe05ad775de／268ab1239a8a／39732a92b5c9／fee04170aa73／9e1ccbdceacc |
| schema v1 | 16 文件锚＋5 P-G 种子占位锚＝21 枚全量复算 21/21 MATCH（分母 21 锚）；schema 自身 9e99dcc4d920 | 9e99dcc4d920 |
| 4 插件 SPEC | 4/4 命中（分母 4 插件） | b1463bb24403／e5a299f69a22／e19e76c5da7e／3e369a1f6171 |

16 文件锚含外部账本移交的 KT 系列五枚（KT_ABC1 03c6c01f3697、KT_A1 78b71d404366、KT_B1 0410ca0fbdae、KT_C1 59d8f56347d5、KT_D0 cce8e9a1b00e）与本项目 v19/v21/corpus/P_F 系列等；锚注册表文件本身即 KT-D0 主锚（SHA-12 03c6c01f3697，一手小写十六进制同值）。表注：schema v1 的 5 枚 P-G 锚为占位值（sha256("P_G_V0_PLACEHOLDER_{id}_2026_09_15")[:12]）的自匹配校验，属恒真检查，仅证 schema 完整性；锚级真值核验见第 4.5 节的 V0→V0.1 五锚 5/5。

### 3.3 Narrative-Layer Corrections（叙述层漂移修正）

五项独立审计的聚合结论为：**资产层一致完好；叙述层三处数字漂移与一处判定矛盾复发，均已修正或如实登记**。三处漂移是：一处对外文稿曾把 60 cells 复现率误写为 87.0%（实为 51/60＝85.0%，分母 60）；补测项总数曾误写为 16（实为 17）；跨主干稳健性曾被表述为「强稳健」（实为降格：主跑 5 个主干仅 3/5 完整，分母 5＝主跑计划主干数；OR 组重叠 1/6，分母 6＝4 种实现的两两组合数）。判定矛盾复发指 Adendum C（「Adendum」沿用仓库工件 _adendum_* 系列的原生拼写，指预登记补测项）一度出现的「检测率 0.0 与 PASS 并存」：经外部勘误注记将原 verdict 字段值原样保留，detection_rate 与 caught_rate 的字段语义矛盾至今未经生产方核对（erratum 状态 UNVERIFIED），本稿按字段值记录并标注该未决矛盾。全部修正以核验事实表为数字通道执行；本节亦为 C3 诚实降级主张的正文落点。

---

## 4 Four Paths, One Adjudication: The D7 Verdicts

每条路径按同一格式报告：SPEC 锚→D1–D3 阶段判定→D7 终局判定→关键指标→挂点对照（挂点对照集中于第 4.7 节）。四路径判定独立陈述：P-C 实测 FAIL_H0，P-D 以 22 题注双指纹独立单列（第 4.6 节），不与任何路径捆绑。

### 4.1 P-A: Equilibrium Stabilization（均衡稳定化）

SPEC 锚 KT_A1（78b71d404366）。D1–D3 PASS；D7 五锚终极实算 PASS。关键指标：9 模型×60 cells＝540 账目守恒（T＝384＋R＝78＋A＝78＝540，残差 0，9/9 模型守恒通过，分母 9 模型）；60 cells 复现率 51/60＝85.0%（existing_30：T＝25/R＝5；new_30：T＝26/R＝4；合计 T＝51/R＝9/A＝0；机读判定 STRONG_PASS）；BOSS 三重可分性——倍数均值 145.8182×、PG 形式占比 13.6%（3/22，分母 22 cells）、ESS 重合 0%（0/22）；9 模型终判 8 PASS＋1 GRAY（deepseek-v4-pro，分母 9 模型）。注：540 账目守恒为分类函数穷尽互斥的构造性恒真（每 cell 必落 T/R/A 恰一档，残差恒 0），仅证计数完整性、不含独立信息量；账目的证据力在 T_frac 分布（9 模型均值 0.7111）而非守恒残差本身。倍数均值 145.8182× 为截断口径下的统计量：22 图中 16 图 rbr_multiplier＝200（median＝max＝200，与 200 次迭代上限相撞），其余 6 图为 1–2×；同一指标在 KT-B1 返工报告（2026-09-10）中为 22×，两口径不同，不可直接比较。

### 4.2 P-C: Cross-Modal d-Path and the Two-Phase Division（跨模态 dpath 与两相划分）

SPEC 锚 KT_C1（59d8f56347d5）。**消歧**：本仓 KT_C1 与外部账本侧的「KT-C1」为同名异物——后者是外部侧的幂律主张（其侧源件载 R²＝0.0007，判死的是该外部主张本身）；本仓 KT_C1 是跨模态 dpath 实验，两者数字不得混写。D1–D3 FAIL_H0；D7 终局 FAIL_H0（幂律主张判死）。关键指标：log-log 双口径 R²＝0.1986／0.2670，双双低于判死线；两相划分（非「相变」口径）下的 dpath 判定 8/9 通过（分母 9 模型），作为派生方向保留。幂律线死亡，dpath 线存续——判死的是主张，不是方向。

### 4.3 P-E: Physical Formula and D_fix2（物理公式）

SPEC 五锚沿锚注册表（03c6c01f3697）派生。D1–D3 PASS；D7 PARTIAL_PASS（经裁决接受）。关键指标：9 模型终判 6 PASS＋2 GRAY＋1 FAIL（deepseek-v4-pro，分母 9 模型）；D_fix2 分布 8/1/0；逐模型 Spearman(D_fix2, T_frac)＝−0.832、Spearman(D_fix2, A_frac)＝+0.941；cell 级 −0.986／+0.506；BOSS-PE-3 三层判据 PASS，其中 A 通道独立性判据成立。PARTIAL_PASS 的含义如实陈述：判死线未全过，经裁决按部分通过接受，不以「PASS」粉饰。「经裁决」指人类决策层的部分接受，位于纯函数判定输出之外，判定函数取值不受其影响。

### 4.4 P-F: The Observer（观察者）

SPEC 锚 P_F_V0_1_UPGRADE（b10fae0da66d）。D1–D3 PASS；D7 PASS。关键指标：9 模型×5 cells 45/45 守恒（T＝41、R＝0、A＝4，残差 0，分母 45 cells）；生成层含 6 次新建 LLM 调用（fresh 调用，如实计入实验层披露）；4 项 BOSS INLINE——NBS 在 1 模型×5 cells 上实算（未拍平），Shapley／Nash-Q／Habermas 三者在 9 模型协同下退化，均按预登记判定记录。

### 4.5 P-G V0.1: Hyperbolic Transport（双曲输运，新增线）

P-G V0.1 的关键指标：双曲与抛物距离放大比 d_H/d_E ≈5×（区间 4.4–8.0）；秩相关 ρ_H,vs,E＝1.0000；5 锚 V0→V0.1 真值复验 5/5 PASS（分母 5 锚：9c3c50005103／8ff586b2722e／0130d179059e／27419597798b／9205c1168e59）。ρ_H,vs,E＝1.0000 与 P-G 冻结报告自述「双曲距离保持欧氏距离的秩关系（完美排序）」同型于第 5.1 节 P-L v2 的保序陷阱，应先按伪影假设排查（需原始嵌入点对向量，冻结件不含，本文不可本地判定）；该值不构成几何主张的独立证据，P-G 维持 consistency 档判位。按裁决，非欧几何作为方法论资产保留，暂不定位进 V4 议程。

### 4.6 P-D: 22-Caption Dual Fingerprints（单列小节）

P-D 以 22 题注双指纹单独成节。关键指标：b3 merkle root 75596bbabdb8（独立重走验证通过）；锚链 c4cae1ed9ee5（即三锚字符串的 SHA-256 前 12 位，与 BOSS 记录逐字符一致）；22 条 caption 的 dual_24bit 指纹与双指纹记录逐条一致 22/22（分母 22 题注）；编号对应关系判定 PASS。dual_24bit 为同一 SHA-256 摘要的 6+6 截段（纯截段），非两枚独立指纹；该实现与 P-O V0.2 spec 的语义层口径分叉，项目内曾判非标并经外部裁决通道裁定 spec 优先；22/22 为复算–记录一致性校验，非独立验证。

### 4.7 Four Hooks: The External Ledger in Parallel（四挂点对照）

一位外部研究者维护着与本实验同命题的并行账本（双盲版匿名，下称「外部账本」）。四组对照构成方法论层面的呼应，数字各按其源件与核验表取值：

**挂点 1（9 模型×60 题账本 ↔ P-L v3 Phase 2 跨主干）**。外部账本侧：9 模型全量账目轧平（T＝384＋R＝78＋A＝78＝540，残差 0；构造性口径见第 4.1 节注）＋双主线精确重合（两个主干各 T＝26/30，分母 30 cells；T_frac 均为 0.867，融合值 0.8667）＋均衡带（T_frac∈[0.80, 0.90]）内恰 2 个模型。我方侧：P-L v3 Phase 2 以分组置信区间检验同一命题（开源 3/3、闭源 3/3 重叠；OR 组 1/6 GRAY；豆包结构性发现见第 5.4 节）。同一命题、两种呈现：全量账本与置信区间分组。两族 β 数值域并列注明：豆包 vision 族 4 端点 β CI 为负值域（绝对值 0.0016–0.0029）；开源 3 主干 β CI 为 [−0.0369, +0.0080] 域（三区间并集）——两组数值不可互相替代。

**挂点 2（5 锚＋双指纹 ↔ 冻结资产层）**。外部账本侧：KT-D0 主锚（锚注册表文件，SHA-12 03c6c01f3697）为 0 号锚，KT_ABC1 五锚系列，字节级＋语义级双指纹。我方侧：18 冻结锚＋5 制品＋schema v1 21/21＋22 题注双指纹 22/22＋b3 root 与锚链。共同模式：内容寻址＋根指纹＋追加链。

**挂点 3（「挂上也是交付」 ↔ 三态混合判定）**。外部账本侧：KT-C1 幂律主张在其判死线下死亡（R²＝0.0007，死的是外部侧自己的主张；其 KT-B1 判死线走正面结果）。我方侧：Phase 1 FAIL＋Phase 2 PASS＋P-K FPR 4.4% GRAY＋OR 1/6 GRAY。共同方法论：诚实降级，挂上（失败记录）也是交付。

**挂点 4（多观察者聚合 ↔ 多通道收敛）**。外部账本侧：9 模型跨主干。我方侧：4 个协作通道独立诊断完全收敛＋多工作单元跨主干执行＋制品／冻结锚／schema 零触动＋0 LLM 判定调用。共同方法论：多观察者聚合收敛＋诚实降级＋机械复算。

---

## 5 P-L v3: Three States, Seventeen Adendum Items

### 5.1 Root Cause: An Algebraic-Identity Artifact

P-L v2 报告了 Spearman＝1、R²＝1 的「通过」。四个协作通道的独立诊断完全收敛：该统计量把**同一向量的两个保序变换**作 Spearman 相关——对全正向量二者严格同序，故相关系数恒为 1、R² 恒为 1，与数据无关（代数恒等式伪影）。仅换主干不能破除；修复方案为同时替换统计量、增加多尺寸数据并跨主干验证。预跑工作单元实测（单主干、30 cells）Spearman＝0.3750（L＝30），表明主干差异足以打破同序。P-L v3 由此以三态分离重建：P1 尺寸缩放、P2 跨主干、P3 崩溃残差，三态独立判死。

### 5.2 Phase 1: FAIL（尺寸缩放）

载体为单一主干（Mistral Large 2512），尺寸 30/45/100。关键指标：R²＝0.7447（判死阈值 ≥0.9，沿 D6 四提案预期表冻结于 Phase 1 finalize 脚本，P-L v3 任务 spec 预登记的阈值族为 Spearman 口径、两载体并列如实披露；FAIL）；Q＝0.1929（判死区间沿同一载体冻结：>0.15 判 FAIL，0.05–0.15 记 GRAY；本值落入 FAIL）。综合判定 FAIL：尺寸缩放主张判死。

### 5.3 Phase 2: PASS with a Downgraded P2（跨主干，降格）

开源 3 主干各 30 cells（n_boot＝1000）：glm53 β＝[−0.0262, +0.0080]；qwen3 β＝[−0.0369, +0.0001]；mistral β＝[−0.0315, −0.0033]；3 对置信区间全部重叠（3/3，分母 3 对），判定 PASS。闭源 3 主干（经加速器 v2 补跑）：gpt-5.6-sol β＝[−0.027453, +0.006577]；claude-sonnet-5 β＝[−0.039812, −0.001869]；gemini-3.7-flash β＝[−0.030946, −0.002754]；3 对全部重叠（3/3，分母 3 对），判定 PASS。

P2 的覆盖如实降格：主跑计划 5 个主干（qwen3/glm53/mistral/doubao-seed-2.0-lite/GPT-4o）中仅 3/5 完整（分母 5＝主跑计划主干数）——doubao-seed-2.0-lite 在 cell 11 后服务端挂起（>9 分钟）记 10/30 INCOMPLETE（分母 30 cells）；GPT-4o 因路由 DNS 不可达与上游 403 记 UNAVAILABLE。双审建议措辞如实引用：「P2 PASS（β CI 3/3 重叠，mistral/qwen3/glm53；doubao 10/30 INCOMPLETE＋GPT-4o UNAVAILABLE；β 为 cell-level 代理斜率）」。β 的 cell 级代理斜率性质一并披露。

### 5.4 OR×OR and the Doubao Structural Finding（跨实现灰区与结构性发现）

4 种 OR embedding 实现的两两 6 对中仅 1 对 β CI 重叠（1/6，分母 6＝两两组合数）：qwen3-emb-8b [0.00147, 0.00430]、bge-large [0.000245, 0.002217]、e5-multi [−0.001073, −0.000445]、gte-large [−0.000333, 0.000176]；判定 GRAY，分裂模式呈架构相关（symbol-split by architecture）。豆包侧的结构性发现：4 个 vision 端点 β CI＝[−0.0029261, −0.0015507]（负值域，绝对值 0.0016–0.0029）呈端点内收敛；交叉架构对照 qwen3-emb-4b β CI＝[−0.0024525, −0.0001876] 打破该收敛。结论口径：豆包族为**端点内收敛**而非跨架构收敛，不得表述为跨实现稳健。

### 5.5 P-K: Judge False-Positive Rate（判官误报率）

三方盲测构成本方 26 件、通道乙 23 件、通道甲 22 件（外部参照合计 45 件）。混淆矩阵：通道乙制品误判为本方 2 件、误判为他方 21 件；通道甲制品误判为本方 0 件。严格通过率 SP_t＝1.0、漏报率 FNR＝0.0；误报率 FPR＝2/45＝4.4%（分母 45＝外部参照制品总数），未过预登记阈值 <1%，判定 GRAY。判官为 LLM 时的偏向边界与 L3 判官可靠性文献一致（第 2.4 节 [22, 23]）；本项不粉饰为 PASS。

### 5.6 The 17 Adendum Items（17 项补测生态）

17 项补测以状态口径为主：**11 PASS＋2 GRAY（H、O）＋1 UNVERIFIED（A）＋2 PARTIAL（F、G）＋1 FAIL_NO_MODEL（K）＝17**（分母 17）。其中 M＝PASS_for_death_theorem、N＝PASS_for_pn_death 为限定性 PASS，按原字符串记录。成本口径备述：10 零成本＋7 中成本（B/C/D/E/M/N/O）＝17（分母 17）；10 项零成本中 7 件为非 LLM 终态（5 PASS：I/J/L/P/Q；1 GRAY：H；1 UNVERIFIED：A），3 件为 LLM 后派（F/G/K）。逐项如下：

| 项 | 主题 | 终态（实测字符串） |
|---|---|---|
| A | 退化预检 | UNVERIFIED |
| B | π 真实标签 | PASS |
| C | P-M 攻击面 | PASS（字段值原样保留；detection_rate／caught_rate 语义矛盾 UNVERIFIED，见第 3.3 节） |
| D | P-C 逐模型 R² | PASS |
| E | P-D 补充 | PASS |
| F | P-E 三模态 | COMPLETED（2/3 模型，分母 3，计 PARTIAL） |
| G | P-F D_fix2 暴露 | FAIL_EXPOSURE_PARTIAL（计 PARTIAL） |
| H | P-G d_H/d_E 收缩 | GRAY |
| I | P-O 题注闭合 | PASS |
| J | 仓库 Spearman 健康 | PASS |
| K | qwen3-0.87 聚类 | FAIL_NO_QWEN3_MODEL |
| L | 验证器双实现差异 | PASS |
| M | P-J 收敛盆地 | PASS_for_death_theorem |
| N | P-N 耦合 | PASS_for_pn_death |
| O | P-K 三方重跑 | GRAY |
| P | P-C 两相 FAIL_H0 | PASS |
| Q | deepseek-v4-pro 锚 | PASS |

一处早期叙述层的算术出入如实登记：委托链曾把 17 项按「零成本 7＋中成本 6＋LLM 3＋F/G/K 1＋豆包 1」字面加总为 18（≠17）；同表修正列 11＋2＋1＋2＋1＝17 成立且与逐件实测一致，本文按修正列与实测口径取数。

### 5.7 Execution Record, Honestly Stated（执行记录如实披露）

工作单元记录存在一处口径并列：叙述层记 8 个工作单元（5 完成＋1 失败＋2 补测完成），任务表实际列 9 行后台任务（含 P-D V0.3 实测与 OR 重试各 1 行）——两处口径如实并列，不作合并修饰。失败记录一并如实：豆包旧版 vector_embedding 任务 4 类端点全部 REJECTED，记 INCOMPLETE；doubao-seed-2.0-lite 会话通道 10/30 INCOMPLETE（第 5.3 节）；豆包补测 v2 的 6 端点中 5/6 EMBEDDED（分母 6 端点）、1 端点 UnsupportedModel 404 记 FAILED；加速器 v2 补跑 3 闭源 3/3 完成（30/30）。另一处叙述出入照录：委托链一处曾称「7 制品」，资产层可数制品为 5 件（第 3.2 节），本文按 5 件口径。

---

## 6 The Literature Infrastructure: Zero-LLM Retrieval over DAS-2M

机器生成的知识主张进入人类记录时，需要与人类主张相同的记账闭环 [40, 41]；判死式研究因此需要一条 0-LLM、可复算的文献基线。本节评估 DAS 开放组件作为该基线的可用性：DAS 论文提出面向发表级学术综述自动生成的有状态代理闭环框架 [42]；DAS-2M 为约 200 万篇文献的持久元数据湖（HF 数据集，CC-BY-4.0）[43]；DAS-Bench 为 30 主题多领域综述生成基准，配 16 判据的 DAS-Eval 评测套件（GitHub，Apache-2.0；两套许可不可混引）[44]。

实测结果（全库、0-LLM 脚本）：7 个分卷（2020-01 至 2026-07）1,471,166 条下载解压，分卷 SHA256 7/7 校验一致（分母 7 分卷）；BM25＋semantic_text 全库打分 14 秒/轮；查询精度（precision@20）：Q3 严格 0.85、Q6 0.75、Q2 0.75、Q1 0.65，均值 0.575（6 查询全口径均值，含 Q4＝0.10、Q5＝0.35）；方法论域查询在扩量后修正为 strict 0.35／lenient 0.60（此前「方法论域错配」结论系词法打分与单年卷的伪象，予以撤销）；产出相关工作候选池 52 条（A19＋B8＋C8＋D9＋E8，程序清点；早一版备忘所记 40 条为笔误）；入池核验 15/15 零幻觉（13＋2 条 arXiv abs 页逐条比对，分母 15）。

**四条边界**（全部如实入文）：① DAS 核心生成代码未发布（README「To be released」）——本项目未用 DAS 生成任何综述文本，仅用其开放数据与工具，不存在「跑 DAS 生成对比件」的可能；② 元数据为 LLM 提取产物，publication_date 噪声严重（1,471,166 条实测记录中仅 55.9% 为 2026 年，含 1828/2029 等异常年份），日期一律以 arXiv 编号前缀为准；③ semantic_text 含模板短语污染（「backbone model:」类占 32% 文档），与模板词碰撞的查询被严重稀释（一查询域因此失效），检索词须避开模板词组；④ 候选不等于证据——候选池仅作发现线索，入池须人工一手核验。对 DAS 论文的引用限于摘要级事实（正文细节未逐页核验）。方法学同构一句话：DAS 的「主张–引用规划＋确定性验证门＋范围化审修」与本稿的池纪律同构。

---

## 7 Limitations

**数据与判定层**。5 件制品 schema 互异（结构性缺陷，判定层如实记为互异而非统一）；P-K FPR 4.4% GRAY（第 5.5 节）；OR 组 1/6 GRAY（第 5.4 节）；Phase 1 FAIL（第 5.2 节）；加速器代理不稳（闭源补跑经代理通道，稳定性有限）；4 个 vector_embedding 大文件处理策略未定型；deepseek-v4-pro 在 P-A 记 GRAY、在 P-E 记 FAIL（分母各 9 模型），跨路径复现其异常；工作单元计数 8（叙述）与 9（任务表行）并列（第 5.7 节）。P-C 幂律主张 FAIL_H0 与 P-E PARTIAL_PASS 为路径级限制项，负结果同时为交付物；数据生成侧失败如实：豆包旧版 4 端点全拒、会话通道 10/30 中断、补测 1 端点 404；8 工作单元含 1 失败，17 项补测含 1 UNVERIFIED／2 PARTIAL／1 FAIL_NO_MODEL。

**叙述层**。三处数字漂移与一处判定矛盾已修正（第 3.3 节）；公开 readme 层四处口径出入（含 D_fix2 部分暴露、P-K 总体判定标注、schema 互异标注与一处过期引用）已如实登记修正。

**检索基础设施**。DAS 四边界（第 6 节）：生成代码未发布；元数据日期噪声；模板词污染；候选须人工核验。

**文献坐标系**。本文直引综述核验池 61 条中的 32 条随行子集＋4 条增补（哲学／史学／科幻线未随行）；池外补 4 条判官可靠性条目与 3 条 DAS 题录；邻近综述为角点式子线综述，全栈重算轴综述在已核验库内未发现（该定位主张可被单一发现证伪 [4]）。与综述 [4] 的文本重合经 8-gram 机械复算：111 段重合全部为参考文献题录（论题名与作者名），正文零搬运。P-D 22 题注双指纹为指纹级一致，不蕴含语义级等价。

**判定语言**。PARTIAL_PASS 为经裁决的部分接受，非完全通过；「已闭合」指预登记判定的执行完毕，非「已证」；两处三值并列（11/2/1/2/1 与 10/7）各以 17 为分母，口径互斥不混用。

---

## 8 Conclusion and the V4 Outlook

一周判死实验的结论按主张链回收：判死是资产——混合判定（PASS／FAIL_H0／PARTIAL_PASS／PASS）与全部灰区、失败记录以冻结锚保存，第三方可复算；P-L v3 部分拒绝——尺寸缩放主张判死（Phase 1 FAIL），跨主干稳健性在降格口径下保留（Phase 2 开源 3/3、闭源 3/3，P2 覆盖 3/5）；资产层零触动（18 冻结锚、5 制品、schema 21/21、22 题注 22/22）；P-C 幂律判死而 dpath 8/9 存续；P-G 双曲输运作为 consistency 档新线保留。

派生路线：V4 将派生 8 题×4 闭源主干的测试题集（计划性数字，非实验结果）；全部制品以公开仓库 release 形式发布（tag 与冻结锚对应，落地状态以实际为准）；非欧几何按裁决作为方法论资产缓定位。五条线以不同货币记账——步骤、解释、基准、均衡、不变量——本文沿用的汇率只有一条 [4]：关于推理的主张，其价值以陌生人能复算的部分计价。

---

## 9 AI-Use Disclosure（两层披露）

**实验层**：数据由多主干 LLM 生成（9 模型，含开源与闭源通道及 embedding 端点；生成层调用如实计入各 phase 记录，如 P-F 的 6 次 fresh 调用与 P-L 各 phase 的主干运行）；**判定层零 LLM 调用**——全部判定为冻结脚本上的纯函数机械评估，判定记录可由第三方复跑。数据生成由 8 个后台工作单元执行（5 完成、1 失败如实记录、2 补测完成，明细见第 5.7 节）。

**写作层**：本文初稿由 AI 撰写助手在人类作者直接指令下起草（模型名称于录用后恢复）；全部数字经独立数字事实核验通道逐行对表（本稿的数字通道）；全部文献题录经独立文献核验通道逐条一手核验后入池，零字段凭记忆补写；全稿已完成两路独立 LLM 双审（R1／R2 记录见附录 A）。全部内容的最终责任由人类作者承担。

**同线作品披露**：同作者线前作（双盲匿名，关系与实名于录用后恢复）[5] 与综述 [4] 均以第三人称引用，特此披露。本文无其他利益冲突申报。

---

## References

[1] Wei et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022. arXiv:2201.11903.
[2] M. Turpin, J. Michael, E. Perez, and S. R. Bowman. "Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting." NeurIPS 2023. arXiv:2305.04388.
[3] T. Lanham et al. "Measuring Faithfulness in Chain-of-Thought Reasoning." TMLR 2023. arXiv:2307.13702.（30 作者，沿核验记录。）
[4] Anonymous. "Keep the Books: A Survey of Auditability and Falsifiability in LLM Reasoning." Manuscript under review, 2026.（同作者线综述，双盲匿名引用；关系见第 9 节披露。）
[5] Anonymous. "Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths." arXiv:2609.09001, 2026.（同作者线第一作，双盲匿名关系见第 9 节披露。）
[6] K. Cobbe et al. "Training Verifiers to Solve Math Word Problems." arXiv:2110.14168, 2021.（12 作者，沿核验记录。）
[7] H. Lightman et al. "Let's Verify Step by Step." ICLR 2024. arXiv:2305.20050.（10 作者，沿核验记录。）
[8] R. Venktesh, N. Rathee, and M. Anand. "Trust but Verify! A Survey on Verification Design for Test-time Scaling." arXiv:2508.16665, 2025.
[9] D. Guo et al. (DeepSeek-AI). "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning." arXiv:2501.12948, 2025.（Nature 2025 同期发表。）
[10] B. Baker, J. Huizinga, L. Gao, et al. (OpenAI). "Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation." arXiv:2503.11926, 2025.
[11] T. Korbak et al. "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety." arXiv:2507.11473, 2025.（position paper，沿核验记录。）
[12] Gu et al. "A Survey on LLM-as-a-Judge." arXiv:2411.15594, 2024.（期刊版 2026：The Innovation。）
[13] Chang et al. "A Survey on Evaluation of Large Language Models." ACM TOIS 15(3):1–45, 2024. DOI 10.1145/3641289.
[14] S. Kapoor and A. Narayanan. "Leakage and the Reproducibility Crisis in Machine-Learning-Based Science." Patterns 4(9):100804, 2023. DOI 10.1016/j.patter.2023.100804.
[15] S. Yang, W.-L. Chiang, L. Zheng, J. E. Gonzalez, and Stoica. "Rethinking Benchmark and Contamination for Language Models with Rephrased Samples." arXiv:2311.04850, 2023.（5 作者已核验，沿核验记录。）
[16] Oren, Meister, Chatterji, Ladhak, and Hashimoto. "Proving Test Set Contamination in Black Box Language Models." ICLR 2024. arXiv:2310.17623.（5 作者已核验，沿核验记录。）
[17] Y. Fu, O. Uzner, M. Yetisgen, and F. Xia. "Does Data Contamination Detection Work (Well) for LLMs? A Survey and Evaluation on Detection Assumptions." Findings of NAACL 2025, pp. 5250–5271. DOI 10.18653/v1/2025.findings-naacl.291.
[18] J. Dekoninck, M. Müller, and M. Vechev. "ConStat: Performance-Based Contamination Detection in Language Models." NeurIPS 2024, Datasets and Benchmarks Track.
[19] Y. Tao, T. Wang, Y. Dong, et al. "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models." arXiv:2510.09259, 2025.
[20] Wang, Li, Ko, and Zhang. "On the Fragility of Benchmark Contamination Detection in Reasoning Models." CoRR abs/2510.02386, 2025.（ICLR 版在案。）
[21] Norman, Rivera, and Hughes. "Reliability without Validity: A Systematic, Large-Scale Evaluation of LLM-as-a-Judge." arXiv:2606.19544, 2026.
[22] Roytburg, Bozoukov, Nguyen, et al. "Are LLM Evaluators Really Narcissists? Sanity Checking Self-Preference Evaluations." arXiv:2601.22548, 2026.（ICML 2026 Main。）
[23] Wataoka, Takahashi, and Ri. "Self-Preference Bias in LLM-as-a-Judge." arXiv:2410.21819, 2024.（NeurIPS 2024 Safe GenAI Workshop。）
[24] Pineau, Vincent-Lamarre, Sinha, Lariviere, Beygelzimer, d'Alche-Buc, Fox, and Larochelle. "Improving Reproducibility in Machine Learning Research (A Report from the NeurIPS 2019 Reproducibility Program)." JMLR 22(164):1–20, 2021.（副标题已核验，沿核验记录。）
[25] G. Irving, P. Christiano, and D. Amodei. "AI Safety via Debate." arXiv:1805.00899, 2018.
[26] V. Conitzer et al. "Foundations of Cooperative AI." AAAI 2023.
[27] I. Ball and D. Kattwinkel. "Probabilistic Verification in Mechanism Design." Theoretical Economics 20(4):1247–1284, 2025. DOI 10.3982/TE6266.
[28] S. Pardasani and M. Singh. "Who Verifies the Benchmark? Decentralizing Trust in Large Language Model Evaluation." arXiv:2608.07762, 2026.（QASC 2026 接收。）
[29] Y. Yang, J. Li, K. Li, et al. "InfiCoEvalChain: A Blockchain-Based Decentralized Framework for Collaborative LLM Evaluation." arXiv:2602.08229, 2026.
[30] J. Peng. "DEP: A Decentralized Large Language Model Evaluation Protocol." arXiv:2603.01167, 2026.
[31] Helff et al. "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking." arXiv:2604.15149, 2026.
[32] L. Bindschaedler, Q. Botha, and C. Siebenbrunner. "Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects." arXiv:2609.01939, 2026.（BCCA 2026。）
[33] A. Kaul, Q. Lan, and P. Gupta. "Behavioral Governance for Autonomous AI Agents: The AgentBound Framework." arXiv:2606.30970v2, 2026.
[34] S. Perera, K. Hapuarachchi, F. Leymann, and R. Khalaf. "Robust Agent Compensation (RAC): Teaching AI Agents to Compensate." arXiv:2605.03409, 2026.
[35] ERC-8004: Trustless Agents. Ethereum Improvement Proposal draft, created 2025-08-13.（工程标准草案，非同行评审。）
[36] Yang, Liu, Miao, et al. "LLMs Judge Themselves: A Game-Theoretic Framework for Human-Aligned Evaluation." arXiv:2510.15746, 2025.
[37] S. Greydanus, M. Dzamba, and J. Yosinski. "Hamiltonian Neural Networks." NeurIPS 2019. arXiv:1906.01563.
[38] G. E. Karniadakis, I. G. Kevrekidis, L. Lu, P. Perdikaris, S. Wang, and L. Yang. "Physics-Informed Machine Learning." Nature Reviews Physics 3:422, 2021. DOI 10.1038/s42254-021-00314-5.
[39] A. S. Krishnapriyan, A. Gholami, S. Zhe, R. M. Kirby, and M. W. Mahoney. "Characterizing Possible Failure Modes in Physics-Informed Neural Networks." arXiv:2109.01050, 2021.
[40] C. Lu et al. (Sakana AI). "The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery." arXiv:2408.06292, 2024.（venue 以 arXiv 为准。）
[41] S. Schmidgall et al. "Agent Laboratory: Using LLM Agents as Research Assistants." arXiv:2501.04227, 2025.（venue 以 arXiv 为准。）
[42] Z. Xu, Z. Xue, T. Hu, Y. Wang, Y. Liu, and J. Zhang. "Deep Academic Survey: Stateful Agentic Closed-Loop Paradigm for Academic Survey Automation." arXiv:2608.18034, 2026.
[43] DAS-2M: A persistent and dynamically updated literature metadata lake (~2 million papers). Hugging Face Datasets (ZhikaiXu24/DAS-2M), released 2026-08-08. License CC-BY-4.0.
[44] DAS-Bench: A 30-topic multi-domain benchmark for academic survey generation, with DAS-Eval (16-criterion suite). GitHub (ZhikaiXu24/DAS component), released 2026-08-08; HF publication 2026-08-20. License Apache-2.0.

---

*（正文完；本双盲版不含作者与致谢信息。若获录用后按恢复机制还原实名与致谢。）*

---

## 附录 A：修订与双审记录

**R1 修订**：本稿按汇总裁决清单完成 R1 修订（阻塞 1＋Major 7＋Minor 7＋建议 3，另 1 项归排版轮），除清单 19 处外正文零改动。逐项定位、改动与依据见随稿《V3 R1 修订响应》。

**R2 双审**：两路独立 LLM 复审已完成，判定为 R2 通过（双路均无阻塞、无 Major），评审记录与汇总裁决随稿存档。
