# 世界观-几何回路：AI 时代硬科幻作为认知空间实验田——一份立场声明与一个实例

**Worldview–Geometry Loop: Hard Science Fiction as the Experimental Field of AI's Cognitive Space — A Position Statement with One Instance**

**性质声明**：本文是立场声明（position statement），不是经验论文。它提出一个可判死的命题，并以 deposon 项目（arXiv:2609.09001）作为该回路的首个完整实例。文中所有阴性结果照实呈现，不做任何拔高。

---

## 摘要（Abstract）

We propose the *Worldview–Geometry Loop*: AI enables hard science-fiction worldbuilding, and such worldviews will in turn reshape AI's cognitive and representational space—as non-Euclidean geometry reshaped geometry. The precedent: variants of the parallel postulate were first imagined as fiction, then built into consistent formal systems, and finally conscripted by general relativity; Lobachevskian space was dignified mathematics before Einstein, so exploratory value does not depend on conscription. Hard-SF worldbuilding—the systematic variation of constraint axioms with rigorous deduction of consequences—is the geometry of possibility space. The loop runs both ways: AI makes worldviews enumerable and consistency-checkable; LLM reasoning paths—high-dimensional, discrete, dissipative, metricless—may demand geometries invented by precisely the hard-SF method. The deposon project (arXiv:2609.09001) is the first complete instance: its conservation ledger survived a pre-registered falsification protocol while its dynamical-equivalence part was killed. We register falsification deadlines for the loop itself.

---

## 一、命题

开门见山：**AI 成就硬科幻世界观构建，而硬科幻世界观将如非欧几何之于几何学那样，对 AI 自身的认知与表征空间产生重要影响。我们称这一双向循环为「世界观-几何回路」（Worldview–Geometry Loop）。**

这不是一句比喻修辞，而是一个可以判死的工程命题。本文给出它的先例、机制、第一个完整实例，以及为它自己配置的判死线。

## 二、非欧几何先例：虚构的公理如何获得尊严

十九世纪之前，平行公设是几何学的"世界观设定"：过直线外一点，有且只有一条平行线。罗巴切夫斯基与鲍耶做了一件在当时的知识秩序里近乎科幻的事——他们想象这个设定不成立。

注意这个操作的次序。第一步是**想象**：公理变体先作为"虚构"被提出，它的合法性在当时并不比小说设定更高。第二步是**建构**：变体被推演成一致的形式系统——内角和小于一百八十度、平行线有无穷多条，全部推论无一矛盾。第三步才是**征用**：近一个世纪后，爱因斯坦在广义相对论中让物理空间实际住进了非欧几何。

关键事实在于：**罗巴切夫斯基空间在被爱因斯坦采用之前，就已经是有尊严的数学。**它的价值不依赖最终的物理征用。如果一个公理变体被推演得足够严格，那么无论它是否被现实征用，推演本身就是知识。探索价值不依赖征用结果——这是本文全部论证的地基。

## 三、硬科幻 = 可能性空间的几何学

硬科幻世界观构建做的正是同一件事：**系统性地变换"约束公理"，然后严格推演其推论。**

把光速从无穷改为有限且不可逾越，整个因果结构、星际政治、信息经济学随之重写。把意识上传设为可行，身份、死亡、产权、犯罪的定义全部需要重新推导。给一组散射过程配上守恒账，每一笔能量收支都必须对平——这就是 deposon 的设定方式。

硬科幻与软幻想的区别不在题材硬度，而在**公理纪律**：设定是公理而非装饰，推论必须闭合，不允许在情节需要时偷偷改账。所以硬科幻世界观构建本质上是**可能性空间的几何学**——它研究"若这组约束成立，则何种结构必然成立"。

本文后文所说的"可居住"，操作性定义为：**一个公理变体可居住 := 它的至少一条推论在预登记判死协议下存活**；后文"住进了现实"即指可居住的推论进入了真实计算过程。

## 四、回路的双向机制

**正向：AI → 硬科幻。**大模型把世界观构建从手工艺变成工程。公理变体可以被批量生成，推论可以被一致性检查，设定全集可以在给定枚举粒度下被穷举式搜索。过去一个作者一生只能认真推演三五个世界观；现在，"变换一条公理、推演全部推论、检查内部矛盾"成为可调用的工序。科幻的供给侧被改变了。

**反向：硬科幻 → AI。**这一向更深，也更不显然。LLM 的推理路径是一种奇特的对象：高维、离散、带耗散（信息在生成中不可逆地坍缩为词元）、且没有现成的度量。对于连续欧氏空间、对于图、对于流形，我们有几何；对于"推理路径"这种对象，**很可能没有现成几何可用，必须发明。**已有研究并非空白——信息几何、transformer 表征几何等工作确实在度量 LLM 的既有表征；但它们的对象是给定的表示，方法论缺口在于：为"带耗散的离散推理路径"这类新对象发明新本体（新几何），而不仅是度量旧对象，这一缺口仍在。

而发明新几何的方法论，恰恰就是硬科幻式的方法论：设定守恒律（什么量在推理中必须对平）、设定不可逆性（哪些操作不可撤销）、设定审计公理（每一步必须可被外部核验），然后推演它们的全部推论。非欧几何是这样被发明的；AI 认知空间的几何，若会被发明，也将这样被发明。硬科幻因此不是 AI 的娱乐部门，而是它的几何学预科。

必须如实标注：反向（硬科幻 → AI 认知几何）目前实例数为零——尚未有任何虚构世界观公理变体被征用进 AI 表征或度量。因此回路命题现阶段是"一条腿实证（正向已可由 deposon 式工序展示）+ 一条腿宣言（反向仅有先例论证）"；deposon 实例化的是中间环节——对虚构几何执行可居住性检验——而非反向的完成。

## 五、实例：deposon

回路不是空谈。deposon 项目（arXiv:2609.09001）是它的第一个完整实例。

**词源与史前史。**"凝子"（deposon）一词源自 deposition——沉积/散射的物理隐喻。项目的史前史是一个"仿物理"世界观设定：从仿生向切换为仿物理向，这本身就是一次公理切换——不再模仿生物智能的外观，而是模仿物理过程的约束结构。

**关键第二步：可居住性检验。**deposon 没有停留在设定美学上，而是对其虚构几何执行了预登记判死协议——先登记判死标准，再跑实验，不允许事后挪动球门。结果诚实地一分为二：

- **守恒账部分住进了现实。** T+R+A=1 在机器精度 2.2e-16 下成立。这组虚构的守恒律被证明可以承载真实的计算过程——这一垄有收成。
- **动力学等价部分被判死驱逐。** P1a/P1b/T-P1c 全灭，但死因需逐一归因：P1a 死于 O(1) 偏差（max dev = 0.8569）；P1b 死于穷举集上的过冲（min cos = −1.0，方向完全相反）；τ∈[0,4] 的 81 档扫描仅对应 T-P1c 的判死，同样无任何拯救余地。这一垄绝收，如实标注。

此外，三项外部检验（E9.4 等权对照、E9.5 六关键词规则基线、E9.6 融合稀释）中，E9.5 与提案方法打平，E9.6 为阴性。这些阴性结果不削弱实例的地位，反而是它的核心证据——**与非欧几何的命运同构：一个世界观的价值不在于整体存活，而在于被检验得足够严格，以至于存活部分可以被信任地征用。**deposon 的守恒账之所以可信，恰恰因为同一协议杀死了它的动力学等价部分。

## 六、可证伪的开放问题：给回路自身配判死线

一个立场声明若不为自己配置判死标准，就只是修辞。我们照 deposon 的规矩，给回路命题本身登记判死线：

1. **十年判死线。**若十年内没有任何 AI 表征或度量上的创新可以追溯至某个虚构世界观的公理变体，则"硬科幻 → AI"一向判死，回路命题降级为单向修辞。
2. **可居住率判死线。**若一批仿物理世界观设定经预登记判死协议检验后，可居住（存活）部分的比例为零——即所有虚构几何在接触现实时整体崩解——则"可能性空间的几何学"一说判死：虚构公理变体对现实计算无产出。
3. **穷举性检验。**AI 辅助的世界观穷举必须能产出人类独立创作者未曾想到且经得起推演的公理变体；若穷举结果全部落在人类既有想象力包络之内，则"AI → 硬科幻"一向仅为提速，不构成质变。

三条判死线现在全部开放。这正是本声明愿意承担的风险形态。

## 七、收束

**科幻负责提出公理变体，科学负责判定哪些变体可居住，AI 同时强化两端。这个循环，我们称之为世界观-几何回路。**

AI 时代的硬科幻不再是科学的预告片——预告片只承诺未来，不承担判死。它是 AI 认知空间的实验田：在这里，公理变体被成片播种，被严格检验，被如实收获或如实标注绝收。deposon 是这块田里第一株有产量记录的作物——它诚实标注了哪几垄绝收，因此它有收成的垄才值得称重。

---

## 事实锚（Fact Anchors）

- **论文**：arXiv:2609.09001（https://arxiv.org/abs/2609.09001）。
- **三档证据一句话**：守恒账 T+R+A=1 以机器精度 2.2e-16 闭合，构成可直接征用的正证据；三项外部检验（E9.4 等权对照、E9.5 六关键词规则基线、E9.6 融合稀释）中 E9.5 打平、E9.6 阴性，构成如实报告的中性/负证据。
- **判死三行一句话**：P1a 死于 O(1) 偏差（max dev = 0.8569），P1b 死于穷举集 min cos = −1.0 过冲，T-P1c 死于 τ∈[0,4] 的 81 档扫描，动力学等价部分按预登记协议判死并驱逐出设定。
- **仓库**：https://github.com/zeroandcat/Deposon 。
