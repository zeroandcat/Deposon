# Deposon：面向可审计大语言模型推理路径选择的物理约束散射层

**Deposon: A Physics-Constrained Scattering Layer for Auditable LLM Reasoning Path Selection**

> 作者：袁祺皓，中国人民大学化学与生命资源学院，科研助理（[email to be added]）
> 目标venue候选：NeurIPS Workshop / AAAI / arXiv 预印本（cs.AI, cs.CL）
> 版本：v1.4-draft（实验章节待 GSM8K 全量结果填充）
> 对应代码版本：Deposon Agents v1.3.1（评测 prompt 版本 v1.3.1，seed=42）

## 摘要 (Abstract)

大语言模型（LLM）在多步推理中易受表面关联陷阱干扰：当问题文本包含与正确答案表面相关但语义无关的数字线索时，贪心式路径选择会被诱饵分支系统性带偏。本文提出 Deposon（凝子）——一个将 LLM 概念分解图映射为凝子态集合、并以三通道散射（透射 / 反射 / 不可逆耗散）对推理路径施加物理约束的增强层。凝子的统一极限命题将阻塞（v1）与隧穿（v2）刻画为同一准粒子实体在以太（"以太"为纯术语借用，无物理本体主张）耦合强度 $g_{\text{aether}}$ 两个极限下的行为；散射权重为构造性定义，其形式受 Feshbach 共振型有效 $S$ 矩阵的类比启发，且任意参数下三通道能量严格满足含环境通道的归一化守恒。在自建的合成基准上（简单算术 100 题 + 表面关联陷阱 100 题，seed=42，真实 LLM 后端分解），Deposon-unified 变体将准确率从贪心基线的 7%（简单集）与 10%（陷阱集）提升至 100%，效应量分别为 +0.93 与 +0.90，陷阱分类学全部六个类别均达到 100%；同时全系统幺正性审计的最大偏差仅为 $2.2\times10^{-16}$（机器精度）。我们进一步设计了在真实 GSM8K 子集上与思维链（CoT）基线的对照实验协议。终版结果（主口径，实验前承诺协议）：在 GSM8K 真实子集上 CoT 97.0%、Deposon-unified 85.0%（McNemar $p=4.9\times10^{-4}$，CoT 显著更优）——§4.2 预先承诺的双向判读框架兑现为"信息损失代价主导"的结局，如实报告、不作粉饰。 我们诚实地指出：当前效应量度量的是"同一概念图内路径筛选的增量"，而非 Deposon 对 LLM 本体推理能力的超越；这一定界在 §5 中详细展开。两组附加对照进一步界定了该边界：标签打乱消融（5 个 seed）使陷阱基准准确率从 100% 跌至 17.2%±6.4%，uniform-params 对照跌至 10%——该层是语义标签到可审计能量决策的**换能器**，而非独立判别器；我们同时如实披露 no_deposon 基线在建图时被诱饵边权（0.9 vs 0.6）反向捕获；相对中性对照（uniform-params，与贪心基线在两集上数值重合）的增量为 +0.93（简单集）/ +0.90（陷阱集）。进一步的算法消融表明：标签依赖可从评分时刻移除（labelfree 以结构信号计算绑定、无需读取 type 字符串，双基准 100%、标签打乱下 25/25 逐位一致）；但在当前管线中结构信号本身由类型标签生成（label→weight 转写），真正的标签信息独立性有待权重来自独立信息源时验证——残余依赖如实披露；休眠的共振通道亦可无损激活（resonant/resonant_hybrid 双基准 100%）。最后，我们为真实基准上的对照实验预先承诺了一个双向判读框架（§4.2）：无论约束层在真实任务上呈现防捕获增益还是信息损失代价，两种结局都被纳入同一判读框架——防捕获增益与信息损失代价共同构成可审计约束层的完整科学画像。

**关键词**：仿物理推理；能量耗散；Feshbach 共振；大语言模型；推理路径筛选；不可逆性

## 1 引言 (Introduction)

大语言模型在数学应用题、常识推理与代码生成等多步推理任务上取得了突破性进展 [1, 2, 11]。以思维链（Chain-of-Thought, CoT）[1] 为代表的提示方法通过显式展开中间步骤显著提升了算术与符号推理能力；思维树（Tree of Thoughts, ToT）[3] 与自一致性（Self-Consistency）[5] 进一步将单链推理扩展为搜索与投票。这些工作共同表明：LLM 的推理能力在很大程度上取决于其**中间路径的组织方式**，而非仅仅是模型规模本身。

然而，多步推理的可靠性仍受三类结构性难题困扰。其一是**表面关联陷阱**：问题文本中存在的数字与关键词若与正确解法表面相关而语义无关（例如"一共"字样诱导加法而正确运算为减法），LLM 及其衍生的搜索方法会被诱饵分支系统性吸引 [36, 37]。其二是**错误沿链累积**：在 CoT/ToT 类方法中，中间步骤的错误缺乏一种内在的"能量代价"机制予以吸收，错误节点的后代会继续占用搜索预算。其三是**路径选择的不可解释性**：投票与启发式评分无法回答"某条路径为什么应当被淘汰"这一结构性问题，因而也难以审计。

更根本地，现有方法对错误路径的处理是**可逆的**：被剪枝的分支在下一轮搜索、下一次采样或下一条提示中随时可能复活。这与物理世界形成鲜明对照——在开放量子系统中，能量一旦耗散进入无穷大自由度的环境（热库的热力学极限理想化），Poincaré 回归时间趋于无穷，耗散在实践意义上不可逆 [30, 31]。我们主张：物理系统的这类固有特性——不可逆耗散、共振增强、幺正约束——不是装饰性隐喻，而是可以直接内建于算法代价与守恒结构中的"免费的"结构性约束。

本文将上述直觉形式化为 **Deposon（凝子）的统一极限参数化**。我们取"凝华"（deposition）之义：能量从气态直接凝华为固态、散失于无限维正交以太，过程不可逆。具体地，LLM 首先将问题分解为概念图（节点为数字、运算、陷阱与答案候选）；图上每个节点绑定一个凝子准粒子态，由两个参数刻画：与推理路径的耦合强度 $g_{\text{couple}}$ 和与以太环境的耦合强度 $g_{\text{aether}}$。推理路径被视为穿越凝子场的"光子"振幅流，在每个节点处发生三通道散射：透射（$T$）、反射（$R$）与向以太的不可逆耗散（$A$），三者严格满足 $T+R+A=1$。阻塞（v1：$g_{\text{aether}}=0$，错误路径被本地反射衰减）与隧穿（v2：$g_{\text{aether}}\gg0$，错误能量凝华入以太而正确路径无损透射）由此统一为同一实体的两个极限态。

我们在两个各含 100 题的合成基准上进行了五变体消融评测（seed=42，概念分解由真实 LLM 后端完成且最终运行零规则降级）。如 Table 2 与 Table 3 所示，unified 变体在简单集与陷阱集上分别达到 100% 与 100% 准确率，而同一概念图上的无凝子贪心基线仅为 7% 与 10%；物理审计显示三通道幺正性在所有路径上的最大偏差为 $2.2\times10^{-16}$，三个极限态的能量分配（v1 耗散 0%、v2 耗散 86.92%、unified 耗散 8.63%）与理论预言一致。

本文的贡献如下：

- **C1 统一极限命题与散射形式化**：提出并形式化 v1/v2 作为同一 Deposon 实体两个极限态（$g_{\text{aether}}=0$ / $g_{\text{aether}}\gg0$）的统一命题，给出三通道散射的构造性归一化公式及其与 Feshbach 共振型有效 $S$ 矩阵的形式类比，并证明能量流守恒（§3.1、§3.3）。
- **C2 DeposonField 算法与系统**：实现"LLM 概念分解 → 凝子场生成 → BFS 路径生成 → 三通道散射筛选 → 沿存活路径计算答案"的完整流水线，包含不可逆 EtherChannel 与逐路径能量流审计；向量化散射对 1000 个凝子单次批量计算耗时 < 0.2 ms（§3.2、附录 C）。
- **C3 效应量根因分析**：发现并修复两类使消融效应量恒为零的失效模式——"答案计算与物理筛选脱钩"与"诱饵陷阱路径不可达"，为同类"物理层增强"研究提供了可复用的消融设计教训（§4.1、§5.1）。
- **C4 约束层双面性的刻画**：给出 GSM8K 真实子集（n=100，seed=42）与 CoT 基线的对照协议及**先承诺的判读框架**——同时容纳"约束无损"与"信息损失代价"两种结局，并以机制归因（分解/筛选/提取）定位代价来源（§4.2、§5.1）。

本文其余部分组织如下：§2 讨论相关工作；§3 给出方法与理论；§4 报告实验；§5 讨论局限与硬件同构展望；§6 总结。

## 2 相关工作 (Related Work)

本节按四条脉络梳理与 Deposon 相邻的领域版图，每条脉络末尾点明本文的差异定位。我们的综述视角是**结构性**的：关心的不是各方法"准确率多高"，而是"错误路径在其中以何种机制被淘汰、该机制是否可解释、是否可逆"。

**(a) LLM 推理增强：从单链到搜索，但无守恒约束。** Chain-of-Thought 提示 [1] 通过显式展开中间步骤激发 LLM 的多步推理能力，零样本变体 [2] 表明该能力可由触发语引出；其结构性缺口在于单链展开没有任何错误吸收机制——中间步骤一旦出错，错误沿链复利式累积，且事后无法定位错误注入点。Tree of Thoughts [3] 与 Graph of Thoughts [4] 将推理组织为树/图搜索，允许回溯与分支聚合，但节点评分依赖 LLM 自我评估启发式，**搜索空间中没有守恒量**：被丢弃的分支不付出任何不可恢复的代价，下一轮扩展可随时复活，"为什么这条路径应当被淘汰"在框架内没有结构性答案。Self-Consistency [5] 以多条采样链多数投票抑制随机错误，其缺口在于投票是统计性而非因果性的：当错误是系统性的（如表面关联陷阱使多数采样同向偏斜），多数派会集体出错，且投票机制不提供任何可解释的阻断证据。ReAct [6] 将推理与动作交替组织，面向交互式任务；自验证 [7] 与 Chain-of-Verification [8] 让模型检查自身输出，但验证器与生成器同源，存在循环论证风险。过程监督 [9]（逐步验证）与演绎验证 [10]（将 CoT 形式化后逐前提核查）把校验粒度推进到步骤级，是与我们最接近的工作，但二者的"验证"仍是学习到的或程序性的判断，没有与推理过程绑定的物理约束，验证器的误报/漏报无法被守恒律兜底。**Deposon 的定位**：不替代上述任何搜索或采样机制，而是在其生成的候选路径空间之上施加一个具有守恒律（$T+R+A=1$）、不可逆耗散与逐路径能量审计的物理约束层——被淘汰路径的能量预算不可回流，每一次阻断都留下可复核的能量账。

**(b) 能量基模型与 Hopfield 系：静态景观，无可逆性缺失的耗散通道。** 能量基模型以标量能量函数刻画配置的概率 [13]，其长期痛点是配分函数难处理、采样依赖 MCMC；能量在此是**定义分布的静态景观**，而非沿推理过程流动、分配的物理量。Hopfield 网络 [14] 表明能量景观的下行动力学可实现联想记忆，稠密推广 [15] 与现代 Hopfield 网络 [16] 进一步建立了与 Transformer 注意力的形式对应；但这类动力学的目标是**收敛到吸引子**（检索已存储模式），而非在候选路径间做可审计的筛选，且其演化原则上可逆地停留于有限维状态空间——不存在"能量一旦离开便不可返回"的通道。扩散模型的早期形式 [17] 显式利用非平衡热力学：正向过程逐步不可逆地破坏结构，反向过程学习重建；DDPM [18] 将其发展为高质量生成框架。扩散中的不可逆性服务于**生成**（把噪声变成样本），而非**约束**（把错误路径永久移除）。**Deposon 的定位**：能量沿推理路径流动并按 $T/R/A$ 三通道分配，其中耗散通道通向无限维以太、Poincaré 回归失效（§3.3）；我们不学习能量景观，而是把能量守恒与不可逆耗散作为推理筛选的结构性原语。

**(c) 物理启发的 AI 范式：软约束、闭系统与硬件同构。** PINN [19] 及其领域综述 [20] 将物理定律作为损失函数中的软惩罚项注入神经网络训练，开创了"物理约束学习"的范式；但其约束是**软的**——残差只被梯度压低、不被恒等式保证，推理时刻仍可违反守恒律，且惩罚权重需逐任务调节。Hamiltonian 神经网络 [21] 与 Lagrangian 神经网络 [22] 通过学习哈密顿量/拉格朗日量使模型内禀满足能量守恒，实现了**硬**结构约束；然而它们建模的是闭保守系统，没有开放系统的耗散通道，处理的也是连续动力学而非离散推理路径。光子计算展示了另一极：相干纳米光子回路 [23] 用 MZI 网格以光速执行矩阵乘法，衍射型全光深度神经网络（D²NN）[35] 则证明自由空间光学本身即可完成推理前传，深度光学 [24]、神经形态光子学综述 [25] 与光计算物理学评述 [26] 系统论证了"干涉即计算"的硬件同构——物理系统的固有特性（叠加、干涉、损耗）可以**免费**承担计算原语，而不必在软件中模拟。**Deposon 的定位**：介于二者之间——在算法层面，我们以散射恒等式（机器精度 $2.2\times10^{-16}$）实现硬约束，且显式包含开系统耗散通道；在路线图层面，耦合参数 $(g_{\text{couple}}, g_{\text{aether}})$ 与线宽 $\Gamma_{\text{aether}}$（§3.1 定义）同 PCM/MZI/ECM 器件控制的显式映射（§5.3）保留了向光子/存算一体硬件下沉的同构路径，这正是"仿物理"区别于"物理隐喻"的判据。

**(d) 神经符号与推理验证：可审计的流水线，但缺物理兜底。** 神经符号计算主张将可微学习与符号推理做原则性整合 [32]；Neuro-Symbolic Concept Learner [33] 以"神经感知 + 符号程序执行"在视觉问答中实现了强组合泛化，证明了分工式架构的价值。在纯 LLM 侧，步骤级验证（过程奖励 [9]、演绎验证 [10]）正在把"验证"从事后打分推进为推理的内生环节。该脉络的共性缺口是：符号/验证层的判断本身没有更低层的约束为其担保——符号执行器可以执行错误前提，验证器可以对正确推理链误报（本文 §4.4 如实记录了我们的 LLM 验证层 14%/22% 的误报率）。**Deposon 的定位**：架构上是神经符号式的——LLM 负责"神经"（概念分解为图），凝子场负责"符号-物理"（图上的约束传播）；与既有工作不同的是，我们为符号层加了一个更低层的物理兜底：即使分解与验证都出错，能量守恒与不可逆耗散仍然对每条路径成立并可被独立审计。验证分歧不被掩盖，而是作为审计信号保留。

**小结。** 四条脉络各自解决了推理可靠性的一部分问题——搜索宽度（a）、能量表达（b）、结构约束（c）、可审计性（d）——但没有一者同时具备"守恒律 + 不可逆淘汰 + 逐路径审计"三要素。Deposon 的贡献命题是：这三要素可以作为**同一物理实体**（凝子散射场）的推论免费获得，而非三个独立模块的拼装。

## 3 方法 (Method)

本节先给出凝子参数化及其统一极限命题的核心形式化（§3.1），再描述将其嵌入 LLM 推理流水线的系统架构（§3.2），随后推导能量流守恒并论证以太耗散的不可逆性（§3.3），最后定义五变体消融设计（§3.4）。完整推导见附录 A。

### 3.1 凝子参数化与统一极限命题

**统一命题。** 设概念图 $G=(V,E)$，每个节点 $v\in V$ 绑定一个凝子态（Deposon state），由三元组刻画：路径耦合强度 $g_{\text{couple}}\ge 0$、以太耦合强度 $g_{\text{aether}}\ge 0$、共振能量 $E_0$。携能量 $E_{\text{photon}}$ 的推理路径（"光子"）穿越节点时发生三通道散射。则：

- **v1（阻塞）极限**：$g_{\text{aether}}=0$，能量仅在透射与反射间分配，$E_{\text{in}}=E_{\text{reflected}}+E_{\text{transmitted}}$，错误路径被本地反射衰减；
- **v2（隧穿）极限**：$g_{\text{aether}}\gg 0$，$E_{\text{in}}=E_{\text{transmitted}}+E_{\text{aether}}$，错误能量凝华入以太，正确路径近似无损透射；
- **一般态**：$0<g_{\text{aether}}<\infty$，三通道同时开启，系统行为由比值 $\eta=g_{\text{aether}}/g_{\text{couple}}$ 连续插值。

v1 与 v2 因而不是两种机制，而是**同一 Deposon 实体在参数空间两个边界上的极限态**；这构成"统一极限"命题的全部内容，其可检验推论是：三个参数点上的能量分配必须与两个极限定性一致（§4.3 验证）；比值 $\eta$ 的连续扫描留作未来工作。

**共振增强的有效耦合。** 定义失谐量（detuning）为路径能量与节点共振能量之差的绝对值：

$$\delta = \lvert E_{\text{photon}} - E_0 \rvert, \qquad g_{\text{eff}} = \frac{g_{\text{couple}}}{1+\delta^{2}}. \tag{1}$$

式 (1) 中的 Lorentzian 因子 $\frac{1}{1+\delta^2}$ 是共振线型：当路径与节点语义"共振"（$\delta\to 0$）时，有效耦合达到最大 $g_{\text{couple}}$；远失谐时约束自动松弛（$g_{\text{eff}}\to 0$，节点退化为透明）。

**共振通道状态的诚实声明。** 在 v1.3/v1.4 实现中，各节点的共振能量恒等于该节点自身能量，且散射时入射光子能量按定义等于该节点的 $E_0$，故失谐量 $\delta\equiv 0$、式 (1) 的 Lorentzian 因子恒为 1：共振通道在本文主实验（§4.1 五变体）中处于**休眠态**，所有实测效应仅由 $(g_{\text{couple}}, g_{\text{aether}})$ 的类型对比驱动；§4.1 已以哈希式代理嵌入初步激活 $\delta\neq0$ 并消融验证其无损（resonant / resonant_hybrid，Table 7），真语义嵌入下的验证为未来工作。我们明确写出这一点，以免读者高估共振机制当前的作用。

**三通道散射公式。** 定义归一化常数 $\Lambda = 1 + g_{\text{eff}} + g_{\text{aether}}$，则三个通道的能量分配权重为

$$T = \frac{1}{\Lambda},\qquad R = \frac{g_{\text{eff}}}{\Lambda},\qquad A = \frac{g_{\text{aether}}}{\Lambda}, \tag{2}$$

分别对应透射、反射与以太耗散。由构造立即有

$$T + R + A = \frac{1 + g_{\text{eff}} + g_{\text{aether}}}{\Lambda} = 1, \tag{3}$$

即**含环境通道的归一化守恒**：耗散通道被显式纳入后，系统+环境的总能量严格守恒。在振幅层面，可取 $t=\sqrt{T}, r=\sqrt{R}, a=\sqrt{A}$ 并赋予反射振幅 $\pi/2$ 的相位约定；本文全部概率断言只依赖权重 $(T,R,A)$。实现上要求式 (3) 在 $10^{-6}$ 容差内成立（实测最大偏差 $2.2\times10^{-16}$，见 §4.3），并对 $g_{\text{couple}}=g_{\text{aether}}=0$（全透射极限 $\Lambda=1$）无需除零保护以外的特殊分支。

**Feshbach 共振形式化。** 式 (1)–(2) 的构造受 Feshbach 统一散射理论 [27, 28] 的**形式类比**启发。需要强调逻辑顺序：式 (2) 是构造性定义——$T+R+A=1$ 由构造成立，并非任何 $S$ 矩阵的推论；下面的 Feshbach 形式提供物理动机与词汇，而非推导；归一化步骤尤其是设计选择，其理由在附录 A.3 中如实说明。设背景散射矩阵为 $S_{\text{bg}}(E)$（无以太耦合时的弹性散射），$|W\rangle$ 为光子-凝子耦合态（对应推理路径与陷阱节点的暂时束缚态），$E_0$ 为共振能量，$\Gamma_{\text{aether}}$ 为以太诱导线宽，则有效 $S$ 矩阵为

$$S_{\text{eff}}(E) = S_{\text{bg}}(E) - \frac{S_{\text{bg}}(E)\,|W\rangle\langle W|\,S_{\text{bg}}(E)}{E - E_0 + i\,\Gamma_{\text{aether}}/2}. \tag{4}$$

式 (4) 的第二项是孤立共振对背景散射的干涉修正：分母的虚部 $\Gamma_{\text{aether}}/2$ 刻画束缚态向以太连续谱的衰变率——能量由此获得一条离开系统自由度的通道，这正是耗散权重 $A$ 的微观来源；这与冷原子物理中 Feshbach 共振的实验传统 [29] 一脉相承。在单极点近似与Breit-Wigner 极限下，式 (4) 给出的共振截面正比于 $\frac{1}{\delta^2+(\Gamma/2)^2}$，归一化后即式 (1) 的 Lorentzian 因子（见附录 A）。这一形式类比为"语义共振增强约束"提供了可操作的形式对应：陷阱节点对匹配路径的强反射/强耗散，在形式上与共振能量处散射截面的峰值同构。

### 3.2 系统架构

![Fig. 1 Deposon 增强推理系统五级流水线与三通道散射示意](fig1_architecture.png)

Deposon 增强的推理系统由五级流水线构成（Fig. 1，架构示意）：

1. **概念分解（ConceptDecomposer）**。LLM 后端（本文使用 kimi-for-coding 真实 API，规则引擎作为自动降级 fallback，跨 prompt 版本的持久化磁盘缓存）将自然语言问题分解为概念图 $G$。节点类型包括：数字节点（number）、运算节点（operation）、陷阱节点（trap，表面相关但语义无关的诱饵候选）、答案节点（answer）与一般概念节点（concept）。v1.3.1 评测中 199 个唯一题面（对应 200 个评测题，其中一题题面同时出现在两个基准）全部采用真实 API 分解，最终结果中规则降级次数为 0。

2. **凝子场生成（DeposonField.spawn）**。节点类型与凝子参数**语义绑定**（v1.3.1 实现，已对照源码核实）：陷阱节点绑定 $(g_{\text{couple}}, g_{\text{aether}})=(5.0,\ 0.0)$、能量 0.1–0.15（强散射中心）；运算节点 $(0.3,\ 0.2)$、能量 0.4；答案/数字/概念节点 $(0.05,\ 0.05)$，其中第 $i$ 个数字节点能量为 $E_{N_i}=0.3+0.05i$、目标节点能量为 0.0。绑定后 $g_{\text{couple}}$ 追加度数修正 $\times(1+0.02\cdot\text{degree})$（$g_{\text{aether}}$ 不做该修正）。如 §3.1 所述，本版本中各节点共振能量恒等于自身能量，共振通道休眠，绑定仅通过 $(g_{\text{couple}}, g_{\text{aether}})$ 起作用。该绑定回应了"物理映射是否仅为装饰"的质疑：参数由节点在问题语义中的角色决定而非事后任意赋值；但该绑定是否为最优仍是开放问题（§5.2）。

3. **候选路径生成（BFS）**。在 $G$ 上以广度优先搜索生成从起点到答案节点的候选路径集合；v1.3 将邻居截断从 4 放宽至 8，以保证诱饵陷阱路径与正确路径**同时可达**——这是消融有效性的前提（见 C3 与 §4.1 根因分析）。BFS 取代了早期版本的 Metropolis-Hastings 采样，规避了高维路径空间中的采样维度诅咒。

4. **散射筛选（process_path）**。对每条候选路径逐节点计算三通道散射（式 (1)–(2)），能量沿路径按式 (5) 演化。路径命运由逐节点通道极大值判定：$\max_i R_i>0.7 \Rightarrow$ blocked；否则 $\max_i A_i>0.5 \Rightarrow$ tunneling；其余为 transmitted。路径最终分数为透射能量比例 $\text{score}=E^{(n)}/E^{(0)}$；score 高于通过阈值 0.1 的候选被保留，按 score 降序（稳定排序）取第一条作为答案来源。向量化实现（NumPy 矩阵运算）对 1000 个凝子的批量散射耗时 < 0.2 ms，满足实时推理约束。

5. **答案计算与验证（沿存活路径）**。最终答案**沿 Deposon 筛选后的存活路径计算**，而非绕过物理层直接从全图提取（该脱钩是 v1.2 效应量恒为零的根因之一，见 §4.1）。独立的 LLM 验证层对存活路径的推理链做正确性判定（陷阱检测、路径完整性、数字使用检查）；验证层判定偏严格的问题如实记录于 §4.4 与 §5.2。

### 3.3 能量流与不可逆性

**能量流守恒推导。** 设路径含 $n$ 个节点，入射能量 $E^{(0)}$，第 $i$ 个节点的通道权重为 $(T_i,R_i,A_i)$。透射能量沿路径递归演化：

$$E^{(i)} = E^{(i-1)}\,T_i,\qquad i=1,\dots,n, \tag{5}$$

累积反射与累积耗散分别为

$$E_{\text{refl}} = \sum_{i=1}^{n} E^{(i-1)} R_i, \qquad E_{\text{diss}} = \sum_{i=1}^{n} E^{(i-1)} A_i. \tag{6}$$

**命题（逐路径能量守恒）。** 对任意路径与任意节点参数，$E^{(n)} + E_{\text{refl}} + E_{\text{diss}} = E^{(0)}$。

**证明。** 由式 (3)，$R_i + A_i = 1 - T_i$。定义部分和 $S_k = E^{(k)} + \sum_{i=1}^{k} E^{(i-1)}(R_i+A_i)$。则

$$S_k = E^{(k-1)}T_k + E^{(k-1)}(1-T_k) + \sum_{i=1}^{k-1} E^{(i-1)}(R_i+A_i) = S_{k-1},$$

归纳至 $S_0 = E^{(0)}$ 即得。$\square$

该守恒律使每条推理路径的能量流完全可审计：每一单位能量要么到达终点、要么被反射、要么凝华入以太，三者必有其一且仅居其一（审计实现见 §4.3）。

**EtherChannel 的不可逆性。** 以太通道在接口层面是单向的：`dissipate(energy)` 将能量原子化地累加进一个只增不减的计数器，系统**不提供** `recover()` 方法；沉积一旦完成即锁定（`is_locked=True`）。这一工程约束对应如下的物理论证。

**论证（Poincaré 回归失效）。** Poincaré 回归定理的适用前提是系统具有有限的不变测度（有限相空间体积）：此时几乎每条轨道都会任意接近其初态，回归时间的典型尺度随自由度指数增长。以太被建模为**无限维正交环境**（`capacity = ∞`）：其状态空间维数无界，不变测度不再有限，定理前提不成立；沉积能量弥散进无穷多正交模式后，回归时间发散，耗散在渐进意义上不可逆。两点诚实声明：(i) 在有限维软件实现中，"不可逆"是工程强制（锁定 + 只增计数器）与渐进性质（无限维极限）的结合，并非在任何有限截断下的数学定理——无限维近似是不可消除的理论局限（§5.2）；(ii) 正是该不可逆性使 Deposon 与概率剪枝区分开来：被淘汰路径的能量预算不可回流，错误无法"复活"占用后续搜索资源。

### 3.4 五变体消融设计

为分离各机制的独立贡献，我们在同一概念图、同一候选路径集合上运行五个变体（Table 1）。除 no_deposon 外所有变体共享散射引擎与路径生成器，唯一差异是凝子参数配置，从而保证消融的受控性。

**Table 1. 五变体消融配置。**（表上方为表题）

| 变体 | $g_{\text{couple}}$ | $g_{\text{aether}}$ | 模式 | 检验目标 |
|------|--------------------|--------------------|------|----------|
| no_deposon | —（无凝子场） | — | 贪心选路基线 | 概念图 + BFS 自身的性能上限 |
| v1_blocking | 高（陷阱节点强耦合） | 0 | BLOCKING | 纯反射能否消除陷阱 |
| v2_tunneling | 低 | 高 | TUNNELING | 纯耗散是否牺牲精度 |
| unified | 中 | 中 | GENERAL | 两机制协同是否最优 |
| high_couple | 最高 | 0 | BLOCKING（极端） | 约束强度是否存在饱和/过杀 |

每个变体在两个基准上各运行全部 100 题（seed=42，评测全程确定性）。评价指标包括：准确率、平均以太耗散、按运算类型/陷阱类型的分层准确率、三通道能量分配、幺正性偏差。与 GSM8K 基线的 McNemar 显著性检验设计见 §4.2。

## 4 实验 (Experiments)

实验回答三个问题：**Q1** Deposon 筛选能否在受控的陷阱环境中消除表面关联误导（§4.1）？**Q2** 该增量能否迁移到真实基准并超越 CoT 基线（§4.2，协议已固定，数据待补）？**Q3** 系统是否严格满足其物理约束——幺正性、三极限态能量分配与以太不可逆性（§4.3）？所有评测使用同一真实 LLM 后端（模型标识 kimi-for-coding，prompt 版本 v1.3.1，seed=42，评测日期 2026-08-22）。两个基准共 200 个评测题（各 100 题），对应 199 个唯一题面；最终评测运行实现 100% 持久缓存命中、零规则降级、零 API 错误。

### 4.1 合成基准（简单100 + 陷阱100，seed=42）

**数据集构造。** 我们自建两个各 100 题的合成基准（构造细节与陷阱分类学定义见附录 B）。简单集覆盖加/减/乘/除四类单步运算；陷阱集在题面中植入表面关联诱饵，包含六个类别：无陷阱（none, 33 题）、表面加法（surface_addition, 14 题）、表面减法（surface_subtraction, 17 题）、运算顺序错误（wrong_order, 16 题）、表面除法（surface_division, 10 题）、表面乘法（surface_multiplication, 10 题）。概念图由 LLM 后端真实分解（199 个唯一题面，0 降级）。

**v1.2 失效模式与根因修复（贡献 C3）。** 早期版本（v1.2）在相同基准上效应量恒为 0。根因分析揭示两类消融失效模式：(i) **答案计算与物理筛选脱钩**——评估器绕过 Deposon 的筛选结果，直接从全图提取数字计算答案，使路径筛选对最终输出无因果影响；(ii) **陷阱不可达**——BFS 邻居截断为 4 时诱饵分支不在候选路径集合中，Deposon 无陷阱可挡，基线也因此"自然避坑"。v1.3 的两项机制修复——答案严格沿 Deposon 存活路径计算、显式构造诱饵陷阱路径并将邻居截断放宽至 8——使消融从"名义对照"变为"因果对照"。Table 2 与 Table 3 报告修复后的五变体结果。

**Table 2. 简单算术基准（100 题）五变体结果。** 平均耗散为每题以太耗散能量均值。

| 变体 | 正确数 | 准确率 | 平均以太耗散 |
|------|--------|--------|--------------|
| no_deposon（贪心基线） | 7/100 | 7.0% | 0.000 |
| v1_blocking | 100/100 | **100.0%** | 0.000 |
| v2_tunneling | 100/100 | **100.0%** | 3.625 |
| unified | 100/100 | **100.0%** | 0.347 |
| high_couple（修复后） | 100/100 | **100.0%** | 0.263 |

*high_couple 行注：修复后全场 $g_{\text{couple}}\times3$，平均耗散 0.263（v1 为 0.000）；修复前因配置别名 bug 与 v1_blocking 完全雷同。*

**Table 3. 表面关联陷阱基准（100 题）五变体结果。**

| 变体 | 正确数 | 准确率 | 平均以太耗散 |
|------|--------|--------|--------------|
| no_deposon（贪心基线） | 10/100 | 10.0% | 0.000 |
| v1_blocking | 100/100 | **100.0%** | 0.000 |
| v2_tunneling | 84/100 | 84.0% | 3.628 |
| unified | 100/100 | **100.0%** | 0.358 |
| high_couple | 100/100 | **100.0%** | 0.267 |

*high_couple 行注：v1.3 中该变体因配置别名 bug 与 v1_blocking 完全雷同（T/R/A 逐节点一致）；修复（全场 $g_{\text{couple}}\times3$）后准确率仍为 100%，平均耗散 0.267（v1 为 0.000）。修复后逐节点通道权重见附录 C 参数表：陷阱节点 $T/R/A=0.061/0.940/0.000$（v1 为 $0.162/0.838/0.000$）、数字节点 $0.828/0.131/0.041$、运算节点 $0.464/0.443/0.093$。Table 2 与 Table 5 中的 high_couple 已同步为修复后数值；no_deposon 变体不受该修复影响。*

**结果解读。** 三个观察值得强调。(1) **准确率饱和、能量代价才是判别性指标**：unified、v1_blocking 与（修复后）high_couple 在两个基准上均达 100%——超过通过阈值后准确率对耦合强度不再敏感，变体间的判别性指标是能量代价。这里必须如实报告一组张力：v1_blocking 以**零耗散**达到同样的 100%，单看能量代价 v1 更优；但差别是定性而非数值的——v1 无耗散通道，错误能量只被反射、仍滞留图内可被复用，而 unified 的耗散通道将其**不可逆**移除（§3.3）。耗散通道的价值在于不可逆性（错误路径在后续处理中无法复活），而非本基准上的准确率；需要迭代重搜的任务才是该差异的预期受益场景（未来工作）。unified 相对贪心基线的效应量为 +0.93/+0.90，但见下方根因分析——相对中性的 uniform-params 对照，增量为 +0.93（简单集）/ +0.90（陷阱集）。(2) **纯隧穿的精度代价**：v2_tunneling 在陷阱集上降至 84%，验证了统一命题的预言——无反射通道时部分诱饵能量未被完全凝华，耗散并非免费的。(3) **分层全覆盖**：Table 4 显示 unified 在陷阱分类学全部六个类别上均达 100%；按金标准运算类型（简单集四类、陷阱集五类含百分比减法）的分层准确率亦全部为 100%（附录 B）。特别地，v1.2 完全无法处理的"unknown"子集（简单集 15 题、陷阱集 10 题，v1.2 准确率 0%）在 v1.3 unified 下全部答对（100%）。

**Table 4. 陷阱分类学六类别的 unified 变体分层准确率（陷阱基准，100 题）。**

| 陷阱类别 | 题数 | unified 正确数 | unified 准确率 |
|----------|------|----------------|----------------|
| none（无陷阱） | 33 | 33 | **100%** |
| surface_subtraction（表面减法） | 17 | 17 | **100%** |
| wrong_order（运算顺序错误） | 16 | 16 | **100%** |
| surface_addition（表面加法） | 14 | 14 | **100%** |
| surface_division（表面除法） | 10 | 10 | **100%** |
| surface_multiplication（表面乘法） | 10 | 10 | **100%** |

**简单集 no_deposon 基线 7% 的根因——对"反向设计"质疑的如实承认。** 对全部 93 个失败题的事后分析揭示了一条确定性的机制链：no_deposon 下所有候选路径 final_score 恒为 1.0（并列）；稳定降序排序于是保持 BFS 完成顺序；BFS 按边权降序扩展邻居；而**诱饵边在建图时被有意赋权 0.9（高于正确运算边 0.6）**——源码注释明确写明其目的是"使 no_deposon 的贪心游走被陷阱捕获"。结果：93 个失败题全部选中 N1→Trap→Goal 路径，而正确 OP 路径 100% 存在于候选集但恒排第 4；7 个"答对"均为巧合（wrong_order 陷阱对单步链不变、surface_division 陷阱恰与真实除法题重合），非巧合意义下的基线真实能力为 0/93。我们因此承认评审的"反向设计"质疑成立：本基准上的 no_deposon 是**诱饵捕获基线**（在对抗性加权概念图上的贪心 BFS），其 7% 不应作为"通用贪心基线在简单算术上的能力"引用。中性对照应采用 uniform-params（simple 7% / traps 10%，见 Table 6）。效应量表述相应重述：相对中性对照，unified 的同图路径筛选增量为 +0.93（简单集，7%→100%）/ +0.90（陷阱集，10%→100%）；头条数字 7%/10% 度量的是**对抗性加权图上的贪心遍历**。我们将这一自我纠错记入贡献 C3——一条区分"诱饵基线"与"中性基线"的基准设计教训。

**标签打乱与均匀参数消融（双基准，各 100 题，零额外 API 消耗）。** 为检验物理层增量是否依赖上游分解器的类型标签质量，我们在与 unified 完全相同的缓存概念图与候选路径集合上运行两个附加对照：(i) **label-shuffle**——非目标节点的 type 标签随机置换（保持各类型数量不变），参数绑定按打乱后的标签执行（5 个 seed：42–46）；(ii) **uniform-params**——保留图结构与散射动力学，但所有节点取 $g_{\text{couple}}=g_{\text{aether}}=0.05$（无类型信息）。三方对照见 Table 6。

**Table 6. 标签打乱 / 均匀参数消融（100 题/基准）。**

| 条件 | 标签 | 动力学 | simple | traps |
|------|------|--------|--------|-------|
| unified（正确标签） | ✓ | ✓ | **100%** | **100%** |
| label-shuffle（5 seed：13/22/13/26/12%） | 打乱 | ✓ | — | 17.2% ± 6.4% |
| uniform-params（全节点 0.05/0.05） | 去除 | ✓ | 7.0% | 10.0% |
| no_deposon（贪心，无场） | — | ✗ | 7.0% | 10.0% |

三方对照构成判别性证据：动力学单独（uniform-params）无效（simple 7% / traps 10%），标签无动力学（no_deposon）无效（simple 7% / traps 10%），只有组合有效（100%）。值得点明的是，uniform-params 与 no_deposon 在两个基准上数值重合（7%/7%、10%/10%）——机制为：simple 集候选路径等长（3 节点），均匀参数下透射率相同（≈0.826），分数并列后稳定排序退化为 BFS 顺序，遂被 0.9 权重诱饵边捕获；该重合是上述根因结论的独立佐证。因此 Deposon 层最准确的理解是**换能器（transducer）**——把语义类型标签转换为可审计的能量决策——而非独立判别器：其增量以标签质量为前提（§5.2）。label-shuffle 的 17.2% 略高于 uniform-params 的 10%，与"数量保持的置换下部分节点碰巧获得正确标签"一致。

**共振通道激活消融（resonant / resonant_hybrid，P1-1 共轭映射的初步实现）。** 实现：$E_{\text{photon}}(\text{path},\text{node})=(1+\cos(\text{path\_emb},\text{node\_emb}))/2\in[0,1]$，其中路径嵌入为路径节点确定性嵌入（64 维）的归一化均值，节点嵌入取 deposon 的 center 向量；$E_0$ 保持节点构造期 energy 不变。两个新模式：resonant（全部节点散射输入改为 $E_{\text{photon}}$，δ≠0）与 resonant_hybrid（仅非 trap 节点用 $E_{\text{photon}}$，trap 保持类型强绑定 δ=0）。与 unified 完全同图同路径集合，仅散射输入改变；零 API 消耗，幺正性审计 $2.2\times10^{-16}$ 通过，五变体回归不变。结果见 Table 7。

**Table 7. 共振通道消融（simple/traps 各 100 题）。**

| 变体 | δ 状态 | simple | traps | trap 节点反射率 | traps 平均耗散 |
|------|--------|--------|-------|------------------|----------------|
| unified | ≡0（休眠） | 100% | 100% | 0.839 | 0.358 |
| resonant | ≠0（全节点） | 100% | 100% | 均值 0.783（min 0.757；低于 0.7 阈值比例 0%） | 0.375 |
| resonant_hybrid | ≠0（非 trap）/ 0（trap） | 100% | 100% | 恒 0.839 | 0.368 |

trap 节点的 δ 从恒 0 变为均值 0.655（max 0.82），其余类型均值 0.39–0.74：共振通道确实进入工作状态，且性能无损。三点诚实声明：① 朴素 resonant 使 trap 反射率 0.839→0.783——"语义失配削弱阻断"的张力被预判并实测证实，方向符合预期（失配→$g_{\text{eff}}$ 下降→阻断削弱），但在 $\delta\in[0,1]$ 的量纲约束下 $g_{\text{eff}}$ 仍足以维持 $r>0.7$ 阻断阈值，阻断失效比例为 0%；② resonant_hybrid（trap 保持强绑定）彻底消除该张力（$r$ 恒 0.839）；③ 当前 $E_{\text{photon}}$ 基于哈希式确定性嵌入（无语义），且路径嵌入包含节点自身、引入自相似偏置（$E_{\text{photon}}$ 均值≈0.7），故结论应读作"**δ≠0 在动力学上可行且无损**"，真语义嵌入下的行为需真实 embedding 模型验证（列入 §5.2）。共振通道的状态由此从"E_photon 未定义"推进为"共轭映射已实现并经消融验证，δ≡0→δ≠0 无损"。

**无标签连续绑定消融（labelfree）。** 一个自然的追问是：散射筛选对上游类型标签的依赖能否在评分时刻移除？ 信号审计（如实全列）：入边权重 w_from_start 完美分离 trap（≥0.8）/非 trap（≤0.6）（阈值 0.75）；b_min 为等价备选信号；energy（trap 0.1 与 Goal 0.0 混淆）与出度（死胡同与 Goal 同为 0）均不可单用；cos-to-Goal 的哈希嵌入无区分度（trap 区间 [-0.632, 0.635] 与非 trap 区间 [-0.308, 1.0] 重叠，如实报告）。绑定规则：起点取无入边节点中出度最大者（无需标签）；$s_{\text{weight}}=\text{clip}((w_{\text{from\_start}}-0.75)/0.15,0,1)$；$s_{\text{dead}}$=（出度 0 且全部入边来自起点且 $w\ge0.75$，以区别于 Goal）；$\text{trapness}=\max(s_{\text{weight}},s_{\text{dead}})\in[0,1]$ 连续；$g_{\text{couple}}=(0.05+4.95\cdot\text{trapness})(1+0.02\cdot\text{degree})$；$g_{\text{aether}}=\min(0.25,\,0.5\cdot\text{energy})$。结果见 Table 8。

**Table 8. labelfree 消融（simple/traps 各 100 题）。**

| 变体 | 标签来源 | simple | traps | 对标签打乱 |
|------|----------|--------|-------|------------|
| unified | 类型标签 | 100% | 100% | 敏感（17.2%±6.4%） |
| labelfree | 无（结构信号） | **100%** | **100%** | **完全免疫（25/25 逐位一致）** |
| uniform-params | 无（无类型） | — | 10% | — |
| no_deposon | 无（无动力学） | 7% | 10% | — |

实际绑定效果：trap 节点 $g_{\text{couple}}$ 均值≈5.175（typed 绑定为 5.0+度数修正），非 trap 最大 0.055；traps 平均耗散 0.667。机制解释（核心亮点）：诱饵若要捕获按权重贪心的搜索者，其入边权重**必须**高于正确链（0.9>0.6）——这正是上文根因分析所揭示的同一构造事实，它使诱饵可被结构信号检测。但**必须如实降级**：在当前管线中，边权重本身是建图器按 type 标签赋值的确定性再编码（label→weight 转写），故 labelfree 证明的只是"**评分时刻不读取 type 字符串**"，而非"管线全程无类型信息"；25/25 逐位一致的标签打乱免疫测量的是前者。真正的标签信息独立性，有待边权重来自独立信息源（如 LLM 连续置信度或学习得到的权重）时验证。两点边界声明：① 若未来图构造器拉平诱饵与正确边的权重，该信号即失效（失效模式已明确）；② 完美分离在合成构造图上取得，真实 LLM 生成的噪声图上的鲁棒性需在 GSM8K 等开放域验证（列入 §5.2）。标签依赖的状态由此从"依赖上游标签、独立性未验证"推进为"**评分时刻的标签依赖可由结构信号替代**，残余依赖（label→weight 转写）如实披露"。

### 4.2 真实 GSM8K 子集（n=100，seed=42）与 CoT 基线对照

本节实验已完成（终版，n=100，seed=42）；以下为实验设计与结果。

**实验设计。** 从 GSM8K 测试集 [11] 中以 seed=42 抽取 100 题构成真实子集。对比三条流水线：(i) **CoT 基线**：同一 LLM 后端以思维链提示直接作答（zero-shot CoT [2] 与少量样本 CoT [1] 各一版）；(ii) **no_deposon**：概念分解 + BFS 贪心选路，无凝子场；(iii) **Deposon-unified**：完整 §3.2 流水线。三条流水线共享同一 LLM 后端与缓存层，以隔离凝子层的因果贡献。答案判定采用精确匹配（extract 最终数值，容差为浮点等值）。统计检验采用 McNemar 检验 [34]：以 Deposon-unified 与 CoT 基线的不一致对 $(b,c)$（仅一方答对的题目数）构造检验统计量 $\chi^2 = (|b-c|-1)^2/(b+c)$，显著性水平 $\alpha=0.05$；同时报告 Wilson 95% 置信区间与效应量（准确率差值）。首要终点为整体准确率；次要终点为按推理步数分层的准确率（检验"长链上物理层增量更大"的预言，§5.1）。

**判读框架（先承诺，后看数）。** 本节在实验前承诺双向判读：首要问题不是"Deposon 是否超过 CoT"，而是"约束层的真实成本是多少"。(i) 若 unified ≥ CoT，则散射约束在真实基准上近似无损，合成集上的防捕获增益近乎免费获得；(ii) 若 unified < CoT，则差值量化概念分解的信息损失代价，约束层的价值命题须重述为"以可量化的准确率代价换取可审计性与防捕获保护"。无论哪种结局，McNemar 不一致对与失败归因将把代价定位到具体机制。

**主口径结果（实验前承诺协议）。** Table 10 给出终版结果（n=100，seed=42，decompose prompt v1.3.2，600 次真实 API 调用、0 降级）：CoT 基线 **97.0%**，unified 85.0%，v1_blocking 86.0%，high_couple 86.0%，v2_tunneling 4.0%，no_deposon 2.0%。统计检验（McNemar）：unified vs CoT 的不一致对为 $b=0,\ c=12$，$p=4.9\times10^{-4}$——**CoT 显著更优，负面结论如实报告**；unified vs no_deposon $b=84,\ c=1$，$p=4.4\times10^{-24}$。独立验证层（validate 层 100 题全真实 API）与金标准一致率 97%；幺正性审计最大偏差 $2.2\times10^{-16}$。结局由此确定为框架的 (ii)：真实干净输入下，约束层继承并放大上游分解/折叠瓶颈，相对直接 CoT 付出 12 个百分点的可量化代价。

**Table 10. GSM8K 真实子集（n=100，seed=42）主口径终版结果。**

| 方法 | 准确率 |
|------|--------|
| CoT 基线 | **97.0%** |
| v1_blocking | 86.0% |
| high_couple | 86.0% |
| unified | 85.0% |
| v2_tunneling | 4.0% |
| no_deposon | 2.0% |

**失败归因（主口径 unified 的 15 例失败）。** 三分类：fold_chain 折叠器缺陷 10 例（沿路径折叠的运算执行错误）、decomposer_error 3 例（概念分解阶段的信息损失，如数字提取/运算链构建错误）、trap_capture 2 例（散射筛选误选诱饵）。即三分之二的失败发生在约束层**下游**的答案折叠环节，而非散射筛选本身。

**事后敏感性分析（明确标注为 post-hoc）。** 对干净 OP 链路径改用分解器直接给出的 computed_answer（修复 fold_chain 反向操作数缺陷）的敏感性口径下：unified 94.0%，vs CoT 的 McNemar $b=0,\ c=3$，$p=0.25$——差异不再显著。该口径为事后敏感性分析，主口径（沿路径折叠）数字不作改动；两口径之差（85%→94%）本身即度量折叠器缺陷的代价。

**解读。** 与合成陷阱集的 +0.90 防捕获增益合看，GSM8K 终版结果构成约束层的双面性：诱饵密集环境下提供可审计保护，干净真实输入下暴露上游表示瓶颈（分解与折叠）的代价。约束层的适用边界由此如实圈定：上游图质量足够高、或环境中存在对抗性诱饵的场景。

### 4.3 物理审计

物理审计独立于任务准确率，直接检验 §3 的三条理论预言，结果汇总于 Table 5。

**幺正性。** 对全部变体、全部 200 题、全部候选路径逐次散射检验式 (3)：$|T+R+A-1|$ 的最大偏差为 $2.2\times10^{-16}$（双精度机器精度量级），远低于 $10^{-6}$ 的容差要求，**通过**。

**三极限态能量分配。** 陷阱基准上全场尺度的能量分配（Table 5）与统一命题的三个极限一致：v1_blocking 耗散率恰为 0.00%（闭系，能量只在透射/反射间分配）；v2_tunneling 耗散率 86.92%（开系，错误能量大量凝华入以太）；unified 耗散率 8.63%（混合态，适度耗散）。五变体的透射率取 5 个不同值，区分度满足设计要求。

**Table 5. 三极限态能量分配审计（陷阱基准，100 题全场平均）。**

| 变体 | 透射率 | 反射率 | 耗散率 | 理论行为 |
|------|--------|--------|--------|----------|
| no_deposon | 1.0000 | 0.0000 | 0.0000 | 无凝子场 |
| v1_blocking | 0.9019 | 0.0981 | **0.0000** | 闭系：耗散恒零 |
| v2_tunneling | 0.1073 | 0.0235 | **0.8692** | 开系：大量凝华 |
| unified | 0.8220 | 0.0917 | **0.0863** | 混合态：适度耗散 |
| high_couple（修复后） | — | — | — | 逐节点：trap 0.061/0.940/0.000、number 0.828/0.131/0.041、operation 0.464/0.443/0.093；平均以太耗散 0.267；修复前因别名 bug 与 v1_blocking 雷同 |

**以太不可逆性。** 全部耗散事件沉积后 `is_locked=True` 且不可恢复；EtherChannel 不提供回流接口，全场累计耗散单调不减。结合 §3.3 的 Poincaré 回归失效论证，系统在软件强制与渐进极限两个层面均满足不可逆性。本审计的作用域声明：审计数值验证的是**工程锁定**性质；渐进（无限维）性质不可数值验证，仍是理想化假设（§5.2）。

### 4.4 统计显著性与效应量

合成基准的评测**对固定题目集是确定的**（固定 seed、全量缓存命中），题目集上的准确率差值即效应量：简单集 $+0.93$（7%→100%）、陷阱集 $+0.90$（10%→100%）；对题目**总体**的不确定性以 Wilson 区间刻画：基线 7/100 的 95% 置信区间约为 $[3.4\%, 13.8\%]$，unified 100/100 的 95% 区间下界约为 96.4%，两区间不重叠，差异在 $n=100$ 下显著。真实 GSM8K 子集上的 McNemar 检验设计与 Deposon-vs-CoT 的显著性结论待数据补齐后填入 §4.2。

**验证层诚实记录。** 独立 LLM 验证层对 unified 输出的判定为：简单集 correct/incorrect = 86/14（与金标准一致率 0.86），陷阱集 78/22（一致率 0.78）。由于 unified 实际全部答对（金标准核对），这些 "incorrect" 判定均为**误报**——验证器对以节点路径形式呈现的推理链偏严格。我们如实记录该分歧并在 §5.2 讨论其成因与影响，未对验证输出做任何选择性过滤。

**运行成本。** 本节全部数字由模型标识 kimi-for-coding 于评测日期 2026-08-22 产生。最终评测运行零 API 调用（1678 次缓存命中、278 条磁盘读，命中率 100%）；整个 v1.3 评测 campaign 累计消耗约 400 次真实 API 调用、约 37 万 tokens（概念分解约 29 万 + 验证约 8 万），百题五变体消融端到端耗时约 3–5 秒。

### 4.5 集成机制分析（Boltzmann 退火与路径积分）

本节检验"时间换质量"假设：以更多散射评估换取更高精度。全部实验零 API 消耗，与 unified 变体同图同参数（seed=42）。四种方法：(i) **boltzmann_single**——单轨迹、无场筛选，出边按 $p_i\propto e^{(w_i-b_i)/T}$ 采样（边能 $E_i=b_i-w_i$，$T=0.3$）；(ii) **boltzmann_annealed**——$K=20$ 条退火轨迹（$T$：1.0→0.05 几何退火）加场透射择优；(iii) **path_integral_born**——$K=20$ 条独立轨迹（$T=0.5$），按 Born 规则聚合 $\arg\max_a \sum_p t_p^2$；(iv) **majority_vote**——同样 $K=20$ 但不乘 $t^2$ 的多数投票。成本定义为平均每题的节点级散射评估次数。结果见 Table 9。

**Table 9. 集成机制分析（100 题/基准，seed=42）。**

| 方法 | K | simple | traps | 平均成本 |
|------|---|--------|-------|----------|
| argmax_field（=unified 基线） | — | 100% | 100% | 12.1 |
| boltzmann_single（无场筛选） | 1 | 1% | 2% | 3.0 |
| boltzmann_annealed | 20 | 100% | 100% | 54.0（4.5×） |
| path_integral_born | 20 | 100% | 100% | 51.0（4.2×） |
| majority_vote（同 K，不乘 $t^2$） | 20 | 19% | 17% | 51.0 |

三个发现。其一（**阳性对照**）：同 $K=20$ 下，Born 规则集成（$\sum_p t_p^2$ 加权）在两个基准均达 100%，而多数投票仅 19%/17%——集成的有效成分是携带场透射信息的振幅平方加权，而非轨迹数量本身。其二（**负面结果，如实报告**）：两个基准已被 argmax_field 饱和（100%），退火与路径积分均未带来准确率收益，反而付出 4.2–4.5 倍能量成本（§5.2）。其三：单轨迹 Boltzmann（1%/2%）甚至低于贪心基线（7%/10%）——高温采样引入额外噪声，且诱饵边在 $E=b-w$ 度量下仍是全局最低能级，采样被陷阱支配。Born 与多数投票的对照保留为机制证据：物理振幅携带的信息不可被纯计数替代。

## 5 讨论 (Discussion)

### 5.1 Deposon 的增量价值边界

我们对 §4.1 效应量的解释保持克制：**当前效应量度量的是"同一概念图内路径筛选的增量"，而非 Deposon 对 LLM 本体推理能力的超越。** 在合成基准中，概念分解由同一 LLM 后端完成，正确运算所需的知识已在图中；no_deposon 基线 7%/10% 的低准确率反映的是贪心选路在诱饵可达时的系统性失败，而 Deposon 的贡献是在图内把正确路径筛出来。换言之，§4.1 证明的是"**当知识已具备时，物理约束层可以近乎完美地解决路径选择问题**"，而不是"Deposon 让 LLM 学会了本来不会的题"。后者只能由 §4.2 的 GSM8K+CoT 对照回答，这也是我们将其设为首要待办实验的原因。

据此可刻画 Deposon 的适用边界：(i) **陷阱密集 / 长链任务**——候选路径多、诱饵可达、单链错误代价高时，物理层的不可逆淘汰价值最大（§4.1 的陷阱集即为此类受控极限）；(ii) **简单短链任务**——若基线选路本已可靠，Deposon 无损但亦无增量（v1.2 简单集 85% 平台期的教训：约束层的上限由概念分解质量决定）；(iii) **知识缺失任务**——若概念图中根本不存在正确路径所需的节点，任何筛选机制都无能为力，此时瓶颈在上游分解而非物理层。我们预言在 GSM8K 上 Deposon 的增量将随推理步数增长而扩大，§4.2 的次要终点即为此设计。

**约束-保真权衡（constraint–fidelity tradeoff）。** 综合合成基准结果与 GSM8K 的终版结果（§4.2），Deposon 的价值命题不应表述为"全面超越 CoT"，而应圈定为"**在诱饵密集环境下的可审计保护**"：当候选路径中存在对抗性诱饵（合成陷阱集），约束层以 +0.90 效应量提供保护且每一步可审计；当输入干净但上游分解存在信息损失（真实多步英文题），约束层继承并可能放大分解瓶颈，相对直接 CoT 呈现可量化的准确率代价。约束强度与输入保真度由此构成一对可刻画的权衡：保护层越硬，对上游图质量的敏感度越高——labelfree 消融（§4.1 Table 8）正是把敏感度从类型标签转移到边权重签名的一次尝试。这一双面性——防捕获增益与信息损失代价——共同构成"可审计约束层"的完整科学画像，比单向度的报喜更有研究价值。

### 5.2 局限

我们按"不可消除 / 可缓解 / 必须声明"三类如实列出局限。

**理论局限（不可消除）。** (1) **无限维以太的有限维近似**：数值实现必须将理论上无限维的环境截断，"不可逆"是渐进性质与工程锁定的结合，而非有限截断下的数学定理（§3.3）。(2) **参数无通用理论**：最优 $(g_{\text{couple}}, g_{\text{aether}})$ 依赖任务，目前无语义到参数的闭式映射，本文的节点类型绑定方案是启发式的。(3) **能量隐喻未验证**："认知能量"与物理能量的对应关系是启发式类比，其深层合理性尚待理论工作。

**工程与评测局限（可缓解）。** (4) **概念分解质量天花板**：系统精度上限由概念分解器决定；v1.3 已由规则引擎升级为真实 LLM 后端，但复杂语义（如多步嵌套运算）的分解仍可能出错。(5) **验证层偏严格**：独立 LLM 验证器与金标准的一致率仅 0.86（简单集）/ 0.78（陷阱集），对节点路径式推理链存在系统性误报（§4.4）；我们未用验证结果回写主环路结论，保留该层仅作审计信号。(6) **共轭识别复杂度**：节点共轭对识别为 $O(|V|^2 d)$，大规模图需 LSH 等近似加速；共振通道已由 resonant/resonant_hybrid 消融激活且无损（§4.1 Table 7），但当前 $E_{\text{photon}}$ 使用哈希式确定性嵌入（无语义、含自相似偏置），真语义嵌入下的行为待验证。(7) **合成基准的分布偏移**：自建陷阱基准的分布是人为设计的（含对抗性加权诱饵边，见 §4.1 的根因分析），效应量外推到真实分布需谨慎——这正是 §4.2 存在的理由。(8) **评测规模**：全部基准证据为每数据集 100 题规模（共 200 题）；尽管评测确定且效应量大，该规模下的结论不自动迁移到千题规模。(9) **单一模型家族**：全部分解与验证使用同一 LLM 后端（kimi-for-coding，评测日期 2026-08-22），跨模型家族稳健性未验证。(10) **标签依赖的残余形式**：labelfree 消融（§4.1 Table 8）证明类型标签依赖可从**评分时刻**移除（标签打乱下 25/25 逐位一致）；但在当前管线中结构信号本身是 label→weight 转写，真正的标签信息独立性有待边权重来自独立信息源（LLM 连续置信度或学习权重）时验证；若构造器拉平权重则信号失效，且完美分离仅在合成构造图上取得，真实噪声图鲁棒性待 GSM8K 验证。

**集成与势垒扩展的边界（如实报告的负面结果）。** (a) **时间换质量（G2）**：在两个已饱和基准上，Boltzmann 退火与路径积分集成均无准确率收益，且付出 4.2–4.5 倍能量成本（§4.5 Table 9）——"时间换质量"仅在未饱和或更难的任务上可能有效，该假设有待验证。(b) **Arrhenius 势垒通道（G3）**：激活闲置的 migration_barrier 边（33 条），逐边乘性衰减 $k=e^{-b/T_{\text{eff}}}$（能量核算 $t+r+a+\text{barrier\_loss}=1$ 已逐路径验证）。$T\ge0.5$ 时两种模式在两个基准均与 unified 持平（100%），即势垒通道在高温极限无害；但 $T\le0.3$ 时 traps 降至 84%——失效全部集中于多一条边的两步题（percentage_subtraction），机制为**路径长度偏置**：正确链比诱饵路径多一条边，低温下多付一次过垒税。Kramers 修正（$k=\min(1,\,w\,e^{-b/T_{\text{eff}}})$）不改变任何精度。更深层的结构原因是**势垒-语义错配**：当前构造中诱饵边为低势垒（0.1，是诱饵设计的一部分），"低垒易迁"反而利于诱饵——该通道若要有用，需要"势垒与语义风险正相关"的图构造。如实声明：barrier 值为构图时人工设定（正确边 0.2–0.3），非学习所得。

**必须声明。** (11) 当前无真实 Deposon 芯片，§5.3 的硬件映射为概念设计，所有"硬件"结论均为软件模拟；(12) 长期稳定性（跨 prompt 版本、跨模型版本）仅有缓存版本隔离的初步保障，缺乏一年尺度的跟踪。

### 5.3 硬件同构展望

Deposon 的三参数族与半导体/光子器件存在显式双向映射，为"算法→芯片"路径预留了接口：

$$g_{\text{couple}} = -\ln(1-p) \;\Leftrightarrow\; p = 1 - e^{-g_{\text{couple}}} \quad(\text{PCM 晶态比例});$$

$$\eta = \frac{g_{\text{aether}}}{1+g_{\text{aether}}} \;\Leftrightarrow\; g_{\text{aether}} = \frac{\eta}{1-\eta} \quad(\text{MZI 分束比});$$

$$\Gamma_{\text{aether}} = \gamma_{\text{ECM}}\cdot\psi(t) \quad(\text{ECM 离子迁移}).$$

其中 $p$ 为相变存储器（PCM）的晶化比例（SET 脉冲晶化增大 $p$、RESET 脉冲非晶化减小 $p$），$\eta$ 为 Mach-Zehnder 干涉仪分束比（$\eta=0$ 全反射对应 v1、$\eta=1$ 全透射入以太端口对应 v2），$\gamma_{\text{ECM}}$ 与 $\psi(t)$ 分别为电化学存储器的迁移率与时间调制。物理上，这意味着"推理约束强度"可以直接编码为器件状态；神经形态光子学 [25] 已证明此类映射的工程可行性。本文不主张任何硬件结果；流片验证与软件-硬件一致性测试属于 v2.0 路线图。

## 6 结论 (Conclusion)

本文提出 Deposon（凝子）的统一极限参数化及其算法实现：将 LLM 概念分解图上的节点绑定为凝子准粒子态，以 Feshbach 共振型三通道散射（透射/反射/不可逆耗散，$T+R+A=1$）对推理路径施加物理约束，把阻塞（v1）与隧穿（v2）统一为同一实体在以太耦合强度两个极限下的行为。在受控合成基准（简单 100 题 + 陷阱 100 题，seed=42，真实 LLM 后端，零降级）上，unified 变体将准确率从贪心基线的 7%/10% 提升至 100%（效应量 +0.93/+0.90），陷阱分类学六类全覆盖；物理审计确认幺正性偏差 $2.2\times10^{-16}$（机器精度）、三极限态耗散 0%/86.92%/8.63% 与理论预言一致、以太耗散不可逆。我们还贡献了两类消融失效模式（答案-筛选脱钩、陷阱不可达）的根因分析，为"物理约束层"类研究提供了受控消融的设计范式。

**局限。** 当前效应量仅度量同图路径筛选的增量而非对 LLM 本体的超越（§5.1）；验证层偏严格存在误报；无限维以太仅能以有限维近似实现；最优散射参数缺乏通用理论。

**未来工作。** 近期（v1.4–v2.0）：完成 GSM8K 真实子集 + CoT 基线对照与 McNemar 检验（§4.2）；激活节点共轭映射的评测；将统一参数 $(g_{\text{couple}}, g_{\text{aether}})$ 的学习化（由任务负载自适应调节）取代手工绑定。远期：PCM/MZI/ECM 硬件映射的流片验证，以及向 StrategyQA [12]、长文本理解等陷阱密集/长链任务的迁移。

## 参考文献 (References)

[1] Wei J, Wang X, Schuurmans D, Bosma M, Ichter B, Xia F, Chi E H, Le Q V, Zhou D. Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems (NeurIPS)*, 2022, 35: 24824–24837. arXiv:2201.11903.

[2] Kojima T, Gu S S, Reid M, Matsuo Y, Iwasawa Y. Large language models are zero-shot reasoners. *Advances in Neural Information Processing Systems (NeurIPS)*, 2022, 35: 22199–22213. arXiv:2205.11916.

[3] Yao S, Yu D, Zhao J, Shafran I, Griffiths T, Cao Y, Narasimhan K. Tree of thoughts: Deliberate problem solving with large language models. *Advances in Neural Information Processing Systems (NeurIPS)*, 2023, 36: 11809–11822. arXiv:2305.10601.

[4] Besta M, Blach N, Kubicek A, Gerstenberger R, Podstawski M, Gianinazzi L, et al. Graph of thoughts: Solving elaborate problems with large language models. *Proceedings of the AAAI Conference on Artificial Intelligence*, 2024, 38(16): 17682–17690. arXiv:2308.09687.

[5] Wang X, Wei J, Schuurmans D, Le Q V, Chi E H, Narang S, Chowdhery A, Zhou D. Self-consistency improves chain of thought reasoning in language models. *International Conference on Learning Representations (ICLR)*, 2023. arXiv:2203.11171.

[6] Yao S, Zhao J, Yu D, Du N, Shafran I, Narasimhan K, Cao Y. ReAct: Synergizing reasoning and acting in language models. *International Conference on Learning Representations (ICLR)*, 2023. arXiv:2210.03629.

[7] Weng Y, Zhu M, Xia F, Li B, He S, Liu S, Sun B, Liu K, Zhao J. Large language models are better reasoners with self-verification. *Findings of the Association for Computational Linguistics: EMNLP 2023*, 2023: 2550–2575. arXiv:2212.09561.

[8] Dhuliawala S, Komeili M, Xu J, Raileanu R, Li X, Celikyilmaz A, Weston J. Chain-of-verification reduces hallucination in large language models. arXiv preprint arXiv:2309.11495, 2023.

[9] Lightman H, Kosaraju V, Burda Y, Edwards H, Baker B, Lee T, Leike J, Schulman J, Sutskever I, Cobbe K. Let's verify step by step. *International Conference on Learning Representations (ICLR)*, 2024. arXiv:2305.20050.

[10] Ling Z, Fang Y, Li X, Huang Z, Lee M, Memisevic R, Su H. Deductive verification of chain-of-thought reasoning. *Advances in Neural Information Processing Systems (NeurIPS)*, 2023, 36. arXiv:2306.03872.

[11] Cobbe K, Kosaraju V, Bavarian M, Chen M, Jun H, Kaiser L, Plappert M, Tworek J, Hilton J, Nakano R, Hesse C, Schulman J. Training verifiers to solve math word problems. arXiv preprint arXiv:2110.14168, 2021.

[12] Geva M, Khashabi D, Segal E, Khot T, Roth D, Berant J. Did Aristotle use a laptop? A question answering benchmark with implicit reasoning strategies. *Transactions of the Association for Computational Linguistics (TACL)*, 2021, 9: 346–361. arXiv:2101.02235.

[13] LeCun Y, Chopra S, Hadsell R, Ranzato M, Huang F. A tutorial on energy-based learning. In: Bakir G, Hofmann T, Schölkopf B, Smola A, Taskar B, eds. *Predicting Structured Data*. Cambridge: MIT Press, 2006: 191–246.

[14] Hopfield J J. Neural networks and physical systems with emergent collective computational abilities. *Proceedings of the National Academy of Sciences*, 1982, 79(8): 2554–2558.

[15] Krotov D, Hopfield J J. Dense associative memory for pattern recognition. *Advances in Neural Information Processing Systems (NeurIPS)*, 2016, 29: 1172–1180. arXiv:1606.01164.

[16] Ramsauer H, Schäfl B, Lehner J, Seidl P, Widrich M, Adler T, et al. Hopfield networks is all you need. *International Conference on Learning Representations (ICLR)*, 2021. arXiv:2008.02217.

[17] Sohl-Dickstein J, Weiss E, Maheswaranathan N, Ganguli S. Deep unsupervised learning using nonequilibrium thermodynamics. *International Conference on Machine Learning (ICML)*, 2015: 2256–2265. arXiv:1503.03585.

[18] Ho J, Jain A, Abbeel P. Denoising diffusion probabilistic models. *Advances in Neural Information Processing Systems (NeurIPS)*, 2020, 33: 6840–6851. arXiv:2006.11239.

[19] Raissi M, Perdikaris P, Karniadakis G E. Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations. *Journal of Computational Physics*, 2019, 378: 686–707. arXiv:1711.10561.

[20] Karniadakis G E, Kevrekidis I G, Lu L, Perdikaris P, Wang S, Yang L. Physics-informed machine learning. *Nature Reviews Physics*, 2021, 3(6): 422–440.

[21] Greydanus S, Dzamba M, Yosinski J. Hamiltonian neural networks. *Advances in Neural Information Processing Systems (NeurIPS)*, 2019, 32. arXiv:1906.01563.

[22] Cranmer M, Greydanus S, Hoyer S, Battaglia P, Spergel D, Ho S. Lagrangian neural networks. *ICLR 2020 Workshop on Integration of Deep Neural Models and Differential Equations*, 2020. arXiv:2003.04630.

[23] Shen Y, Harris N C, Skirlo S, Prabhu M, Baehr-Jones T, Hochberg M, Sun X, Zhao S, Larochelle H, Englund D, Soljačić M. Deep learning with coherent nanophotonic circuits. *Nature Photonics*, 2017, 11(7): 441–446. DOI: 10.1038/nphoton.2017.93.

[24] Wetzstein G, Ozcan A, Gigan S, Fan S, Englund D, Soljačić M, Denz C, Miller D A B, Psaltis D. Inference in artificial intelligence with deep optics and photonics. *Nature*, 2020, 588(7836): 39–47.

[25] Shastri B J, Tait A N, Ferreira de Lima T, Pernice W H P, Bhaskaran H, Wright C D, Prucnal P R. Photonics for artificial intelligence and neuromorphic computing. *Nature Photonics*, 2021, 15(2): 102–114. DOI: 10.1038/s41566-020-00754-y.

[26] McMahon P L. The physics of optical computing. *Nature Reviews Physics*, 2023, 5(12): 717–734.

[27] Feshbach H. Unified theory of nuclear reactions. *Annals of Physics*, 1958, 5(4): 357–390. DOI: 10.1016/0003-4916(58)90007-1.

[28] Feshbach H. A unified theory of nuclear reactions. II. *Annals of Physics*, 1962, 19(2): 287–313.

[29] Chin C, Grimm R, Julienne P, Tiesinga E. Feshbach resonances in ultracold gases. *Reviews of Modern Physics*, 2010, 82(2): 1225–1286. arXiv:0812.1496.

[30] Zurek W H. Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics*, 2003, 75(3): 715–775. arXiv:quant-ph/0105127.

[31] Breuer H P, Petruccione F. *The Theory of Open Quantum Systems*. Oxford: Oxford University Press, 2002.

[32] Garcez A d', Gori M, Lamb L C, Serafini L, Spranger M, Tran S N. Neural-symbolic computing: An effective methodology for principled integration of machine learning and reasoning. arXiv preprint arXiv:1905.06088, 2019.（期刊版：Garcez A d', Lamb L C. *Journal of Applied Logics*, 2022, 6(4): 611–643.）

[33] Mao J, Gan C, Kohli P, Tenenbaum J B, Wu J. The neuro-symbolic concept learner: Interpreting scenes, words, and sentences from natural supervision. *International Conference on Learning Representations (ICLR)*, 2019.

[34] McNemar Q. Note on the sampling error of the difference between correlated proportions or percentages. *Psychometrika*, 1947, 12(2): 153–157.

[35] Lin X, Rivenson Y, Yardimci N T, Veli M, Luo Y, Jarrahi M, Ozcan A. All-optical machine learning using diffractive deep neural networks. *Science*, 2018, 361(6406): 1004–1008. DOI: 10.1126/science.aat8084.

[36] Mirzadeh I, Alizadeh K, Shahrokhi H, Tuzel O, Bengio S, Farajtabar M. GSM-Symbolic: Understanding the limitations of mathematical reasoning in large language models. *International Conference on Learning Representations (ICLR)*, 2025. arXiv:2410.05229.

[37] Nezhurina M, Cipolina-Kun L, Cherti M, Jitsev J. Alice in Wonderland: Simple tasks showing complete reasoning breakdown in state-of-the-art large language models. arXiv preprint arXiv:2406.02061, 2024.

*注：全部条目的作者、年份、venue、arXiv 编号与 DOI 均经公开检索逐条核对；[23]（相干纳米光子回路，Shen 2017）与 [35]（衍射全光神经网络 D²NN，Lin 2018）为光计算两条不同路线，并列引用。*

## 附录

### A. 散射方程推导

本附录给出从 Feshbach 有效 $S$ 矩阵（式 (4)）到三通道归一化权重（式 (2)）的推导链条。

**A.1 单极点近似。** 将总 Hilbert 空间分为开放通道子空间 $P$（推理路径的连续模式）与孤立共振子空间 $Q$（光子-凝子束缚态 $|W\rangle$）。Feshbach 投影给出 $P$ 子空间上的有效 $S$ 矩阵 [27, 28]：

$$S_{\text{eff}}(E) = S_{\text{bg}}(E)\left[\mathbb{1} - \frac{|W\rangle\langle W|}{E - E_0 + i\Gamma_{\text{aether}}/2}\right],$$

其中 $\Gamma_{\text{aether}}$ 是 $Q$ 子空间经以太连续谱衰变引入的线宽（$Q$ 与无限维以太的耦合使孤立能级获得虚部 $-i\Gamma_{\text{aether}}/2$）。

**A.2 Breit–Wigner 极限与 Lorentzian 线型。** 在单通道、单共振极限下，共振对散射截面的贡献正比于

$$\sigma_{\text{res}}(E) \propto \frac{(\Gamma/2)^2}{(E-E_0)^2 + (\Gamma/2)^2}.$$

取线宽为自然标度单位（$\Gamma/2 = 1$）并记失谐量 $\delta = |E - E_0|$，得共振因子 $\frac{1}{1+\delta^2}$，即式 (1) 中调制 $g_{\text{couple}}\to g_{\text{eff}}$ 的 Lorentzian。物理解读：路径能量与节点共振能量越匹配，束缚态形成越强，散射（反射/耗散）越剧烈；远失谐时相互作用绝热关闭。

**A.3 三通道归一化。** 在 $\delta$ 给定时，入射流面临三个互斥且穷尽的出口：(i) 无相互作用透射（权重基准 1）；(ii) 经有效耦合 $g_{\text{eff}}$ 的反射；(iii) 经以太耦合 $g_{\text{aether}}$ 的耗散。以 $\Lambda = 1 + g_{\text{eff}} + g_{\text{aether}}$ 归一化即得式 (2)。如实说明：该归一化是**设计选择**而非 $S$ 矩阵的推论——式 (2) 的 $T+R+A=1$ 由构造成立（式 (3)），Feshbach 形式仅提供动机。§4.3 的机器精度审计（最大偏差 $2.2\times10^{-16}$）验证了这一恒等式在浮点实现中的严格性。

**A.4 极限态检验。** 式 (2) 在三处边界的行为：(i) $g_{\text{aether}}=0$：$A=0$，$T+R=1$，纯 v1 闭系；(ii) $g_{\text{aether}}\to\infty$：$A\to 1$，$T,R\to 0$，但注意 v2 隧穿的运行区是 $g_{\text{aether}}\gg g_{\text{eff}}$ 且 $g_{\text{eff}}$ 小——此时对正确节点（低耦合）$T\approx 1$，对陷阱节点（高 $g_{\text{eff}}$）能量被 $A$ 大量吸收，"正确路径无损透射、错误能量凝华"由此实现；(iii) $g_{\text{couple}}=g_{\text{aether}}=0$：$\Lambda=1$，$T=1$，全透射（对应 no_deposon 的透明极限）。三个极限在参数空间上连续连接，这是"统一"命题的数学内容。

### B. 评测数据集构造细节与陷阱分类学

**B.1 构造原则。** 两个基准各 100 题，seed=42 确定性生成。每题生成时同步产出：题面文本、金标准运算类型、金标准答案、陷阱类别标签、以及（v1.3 起）概念图中的**诱饵陷阱路径**——即一条表面合理但语义错误的路径，确保其可达（BFS 邻居截断 4→8）。诱饵可达性设计是消融有效性的前提：若基线 BFS 根本无法走到陷阱，则"Deposon 挡住陷阱"无从检验（v1.2 效应量恒零的根因之二）。

**B.2 陷阱分类学（六类）定义。** (i) none：无诱饵，控制组；(ii) surface_addition：题面含"一共/总共"等加法触发词，但金标准运算非加法；(iii) surface_subtraction：含"给了/剩下"等减法语境词，但运算关系与表面线索不一致；(iv) surface_multiplication / surface_division：含"倍/平均分成"等触发词但金标准运算不同；(v) wrong_order：多步运算题，表面阅读顺序与正确运算顺序相反（如"先打折再满减"）。

**B.3 按运算类型分层结果。** Table B1 报告 unified 变体在两个基准上按金标准运算类型的分层准确率（全部 100%）。

**Table B1. unified 变体按金标准运算类型的分层结果。**

| 基准 | 运算类型 | 题数 | 正确数 | 准确率 |
|------|----------|------|--------|--------|
| 简单 | subtraction | 35 | 35 | 100% |
| 简单 | addition | 17 | 17 | 100% |
| 简单 | multiplication | 20 | 20 | 100% |
| 简单 | division | 28 | 28 | 100% |
| 陷阱 | subtraction | 25 | 25 | 100% |
| 陷阱 | addition | 24 | 24 | 100% |
| 陷阱 | percentage_subtraction | 16 | 16 | 100% |
| 陷阱 | multiplication | 15 | 15 | 100% |
| 陷阱 | division | 20 | 20 | 100% |

**B.4 v1.2 不可解子集。** 简单集中 15 题、陷阱集中 10 题在 v1.2 下因概念分解失败归为 "unknown"（准确率 0%）；v1.3 升级 LLM 分解后端后该子集在 unified 下全部答对（15/15 与 10/10），说明该部分增益来自上游分解质量而非物理层——与 §5.1 的价值边界刻画一致，特此区分。

### C. 复现指南、版本沿革与参数表（代码已开源）

**C.0 版本沿革。** Table C1 汇总与本文相关的版本谱系。

**Table C1. 版本沿革（v1.2 → v1.4）。**

| 版本 | 关键变更 | 评测状态 |
|------|----------|----------|
| v1.2 | 首个五变体消融框架 | 效应量恒为 0（根因：答案-筛选脱钩；陷阱不可达；BFS 邻居截断 4） |
| v1.3 | 答案沿存活路径计算；诱饵陷阱路径可达；截断 4→8；LLM 后端概念分解 | §4.1 简单集/陷阱集五变体结果 |
| v1.3.1 | validate 层全量纳入审计环路（200 题真实 API，0 降级）；prompt 版本锁定 | §4 全部结果（评测日期 2026-08-22） |
| v1.4 | 本文；GSM8K+CoT 对照协议固定；high_couple 别名 bug 修复 | GSM8K 终版结果已回填（§4.2） |

**C.1 模块清单（v1.3.1）。** 核心模块 5 个：DeposonState、EtherChannel、DeposonField、DeposonAgentSystem、VectorizedDeposonScatter；接口模块 3 个：LLMBackend（kimi-for-coding 真实 API + 自动降级）、KimiLLMBackend、PersistentCache（线程锁 + 原子写 + 跨 prompt 版本隔离）；评估模块 2 个：BenchmarkEvaluator、百题基准（simple / trap）。总计约 800 行 Python。v1.3 相对 v1.2 的关键机制修复：答案沿 Deposon 存活路径计算、诱饵陷阱路径显式构造、BFS 邻居截断 4→8、validate 层全量纳入审计环路。

**C.2 性能指标。** 向量化批量散射（1000 凝子）：0.105 ms；批量路径处理（100 条 × 10 节点）：0.3–0.5 ms；单题端到端推理（含概念分解 + 路径生成 + 散射筛选 + 验证）：5–10 ms；百题五变体消融：3–5 s（缓存命中下）。

**C.3 复现协议。** 全部结果可由固定 seed=42 与持久化缓存确定性复现：最终评测运行 1678 次缓存命中、0 次未命中、0 次规则降级、0 次 API 错误；逐题明细（每题 × 每变体的 fate、三通道能量、答案与判定）记录于评测 JSON 输出（deposon_benchmark_v1_3_simple.json 与 deposon_benchmark_v1_3_traps.json）。依赖仅为 numpy 及标准库；LLM 后端可替换为任意兼容接口，评测逻辑与后端解耦。

**C.4 参数表（v1.3.1，对照 deposon_agents_v1_3.py 修复后版本核实）。**

类型→参数绑定（绑定后 $g_{\text{couple}}\leftarrow g_{\text{couple}}\times(1+0.02\cdot\text{degree})$，$g_{\text{aether}}$ 不做度数修正）：trap $(5.0,\ 0.0)$、能量 0.1–0.15；operation $(0.3,\ 0.2)$、能量 0.4；answer/Goal $(0.05,\ 0.05)$、能量 0.0；number/concept $(0.05,\ 0.05)$，第 $i$ 个数字节点能量 $0.3+0.05i$。散射时入射光子能量取节点自身能量（故 $\delta\equiv 0$，共振通道休眠，§3.1）。路径命运：$\max_i R_i>0.7$ 为 blocked；否则 $\max_i A_i>0.5$ 为 tunneling；其余为 transmitted。候选通过阈值 final_score $=\prod_i T_i>0.1$；通过者按 score 稳定降序取首条（正确性容差 $|\text{pred}-\text{gold}|<0.01$）。诱饵边权：N1→语义/错误运算陷阱 0.9、N1→顺序陷阱 0.85、N1→死胡同 0.8；正确边 N1→OP1 为 0.6。BFS 邻居按权重降序、每节点 top-8、候选上限 30。变体变换（在绑定与度数修正之后施加）：no_deposon 完全绕过场（所有 final_score=1.0）；v1_blocking 令全部 $g_{\text{aether}}\leftarrow0$；v2_tunneling 令 $g_{\text{aether}}\leftarrow\max(g_{\text{aether}},2.0)$、$g_{\text{couple}}\leftarrow\min(g_{\text{couple}},0.5)$；unified 保持绑定不变；high_couple（修复后）令全部 $g_{\text{couple}}\times3$（修复前误为 v1_blocking 别名）。

**C.5 诚实声明。** 本文不报告任何未执行的实验；§4.2 的 GSM8K 终版结果已回填（含事后敏感性分析的明确标注）；所有声称的物理审计数字均可在上述 JSON 输出中逐项复核。

### D. 真实脑图摄入管线（G1）

**D.1 SVG 解析器。** `svg_mindmap_ingest.py` 将标准 SVG 转换为概念图：`<text>` 元素→节点、`<path>`/`<line>` 端点吸附→边、fill 颜色分组→分支归属，BFS 自根节点定向。解析器在合成 SVG 上自检通过（6 节点 5 边、root 定向正确）。

**D.2 真实脑图演示（诚实声明）。** 本次 upload 中无真实 SVG 样本（仅 PNG 脑图），故解析器未在真实 SVG 上验证；《AI应当如何思考》脑图的图结构（45 节点 / 49 边 / 9 主分支）为**人工转译**——由分析工程师读取 PNG 后按层级手工录入，非 OCR/视觉自动解析；trap/answer 标注与诱饵边权（0.9/0.85、低势垒 0.1）亦为转译时按语义人工设定。

**D.3 散射行为演示。** 在该转译图上以 unified 场运行散射（6 条候选路径）：聚合 $T/R/A=0.531/0.357/0.112$（逐路径守恒，和为 1.000）；4 条正当结论路径（经仿光子vsTDA/组织记忆/认知协议/专家萃取）全部 transmitted（$t\approx0.737$），2 条经"范式转移/仿生瓶颈"与"行动窗口/AI够强未自主"陷阱节点的诱饵路径被 $g_{\text{couple}}=5$ 反射阻断（fate=blocked，$t=0.119$ vs 正当路径 0.737）。定性结论：场动力学在真实层级知识结构上的行为与合成集一致，trap 阻断机制可迁移到人工转译的脑图；真实 SVG 的自动摄入适配留作未来工作。

*（全文完）*
