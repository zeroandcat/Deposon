<!-- REFS_USED: [1, 2, 3, 4, 10, 11, 12, 13, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 34, 35, 40, 41, 44, 49, 50, 52, 55, 60, 61, 62, 63, 64]（编号体系与项目文献库一致） -->

# 凝子散射层：大语言模型推理路径的可审计表征、守恒保证与博弈论化实证

**Deposon: Auditable Representation, Conservation Guarantees, and Game-Theoretic Evidence for a Physics-Constrained Scattering Layer over LLM Reasoning Paths**

> **数据可用性与证据强度约定**。全部实验数字可追溯至 `results/` 目录下冻结 JSON 的具体字段；全部统计判定为预登记后的机械规则求值。证据强度分三档标注：**已闭合（预登记判定）**（判定纯函数于运行前冻结、机械求值闭合）、**一致性证据**（方向吻合但未达预登记强判据）、**仅有动机**（理论直觉，无实证）。

## 摘要

大语言模型的多步推理缺乏一本机器可复核的账：路径被淘汰时不留可审计记录。本文提出 Deposon（凝子）散射层：把 LLM 概念分解图上的节点绑定为双参数凝子态，推理路径穿越时发生透射、反射、不可逆耗散三通道散射，任意参数下严格满足会计恒等式 T+R+A=1，逐路径能量审计最大偏差 2.2×10⁻¹⁶（双精度机器精度）。我们如实报告证据强度的全部三档：合成陷阱基准上路径筛选增益已闭合（预登记判定）（unified 100%，诱饵捕获基线 7%/10%），但真实基准上散射层与一个仅读标签字符串的 6 关键词规则过滤器不可区分（GSM8K 0.87≥0.85，McNemar p=0.5；StrategyQA 0.899=0.899）——在该样本量下未检出差异：GSM8K 差值 −2pp（95% CI [−11.8pp, +7.8pp]，Newcombe-Wilson）、StrategyQA 差值 0pp（95% CI [−8.8pp, +8.8pp]），两者均为非配对 Newcombe 混合区间（保守上界；配对不和谐对仅 0/2 与 0/0，配对区间退化；计算工件 `deposon_v22_e95ci.json`）；不和谐对仅 2/0 对，可检出差阈值约 ±10pp，更小的增量无法排除——故主张精确化为「差异价值只在机器可核验性」，由 E9.4 归因机制支撑，而非由本检验的强形式支撑。融合实验给出另一条阴性结论：场与语义先验的凸组合在所测全部 λ 档上不增（physics 0.484→0.452），λ=2 的表观增益被证实为反场伪影；融合增益若存在，只能来自非线性机制。在此静态守恒账之上，本文进一步把反向动力学建模为图上势博弈，给出审计标量的单调性与近梯度性实证与分布级协调比（empirical coordination ratio, ECR）定量化，并划定其边界。三条形式化动态等价命题（P1a/P1b/T-P1c）在判死协议下全部被证伪，势博弈主张降级为近似（含环图残余中位 0.669）——动力学层面仅保留一致性级证据。

**关键词**：可审计性；守恒恒等式；物理约束层；势博弈；预登记；阴性结果

## 1 引言

思维链 [60] 及其衍生方法——搜索式分解 [61]、自洽投票 [62]——把 LLM 的推理组织为显式的中间步骤并扩展为候选路径的空间；但思维链文本本身不必忠实于内部计算 [63]，忠实性需专门评测 [64]。多步推理的可靠性受三类结构性难题困扰：题面中的表面关联诱饵会系统性吸引搜索分支；中间步骤的错误没有内在的吸收机制，沿链复利式累积；而路径选择的依据不可解释，事后无法回答"这条路径为什么应当被淘汰"。然而无论哪种组织方式，一个结构性问题始终悬置：某条路径被淘汰时，系统拿不出一本可复核的账。剪枝、投票与启发式评分都在做淘汰决策，但淘汰本身不留下守恒记录——被丢弃的分支消耗了多少预算、为何应当被丢弃、该决策能否被第三方逐步重算，框架内没有答案。算法审计研究在组织层给出了问责框架 [18]，密码层的可验证计算 [19] 与差分隐私审计的精确化 [21] 则证明"可核验性"本身可以成为一等设计目标；但落实到 LLM 推理路径这一层，事后溯源与密码证明之间存在一个空层——运行期逐实例的不变量——就我们所知尚无先占工作。

本文的出发点是用一个物理构造占据这个空层。所需的词汇可以直接从散射理论借来，此处一次说清，后文不再复述：三态裁决（透射/阻断/隧穿）对应散射的三通道；耗散对应承诺装置——能量一旦凝华入无限维以太便不可回流，被淘汰路径的预算不可复活；守恒对应会计恒等式——每单位能量必有且仅有一个去向。本项目前身设计阶段（冻结管线构建之前）的设计目标给出了这一构造的雏形：双参数凝子态（路径耦合 g_couple、以太耦合 g_aether）、受 Feshbach 共振启发的散射形式、"耗散=凝华不可逆"的公理化规定。从该雏形到可审计表征与守恒保证、再到把反向动力学博弈论化，是同一实体的两次收紧，细节分别留给表征与守恒主线（§2）与博弈论化主线（§3）。

把物理性质写进算法并不是新想法，但多数先例注入的是软约束：残差只被梯度压低，推理时刻仍可违反。本文的构造走另一极——守恒由构造成立，不依赖训练、不依赖调参，审计者只需要双精度算术即可复核。这决定了本文证据的形态：最强的主张（守恒、审计）不依赖任何基准准确率，而最弱的主张（耗散通道的收益）则被我们自己的实验显式降格为"仅有动机"。

需要立即声明的是，这条研究线的产出除机制本身外，还包括一组阴性结果划出的诚实边界；后者与前者同等分量。本文以预登记对照实验证明：散射层的表观准确率优势部分来自基准构造偏置（等权拉平诱饵边后优势的归因随之改变），且在两个真实基准上与一个平凡规则过滤器不可区分。这类"效应量归零"的整改并不丢人——低估与高估主张同样有害 [49]，规范化的报告纪律 [40, 41] 与对欠指定（underspecification）效应的系统记录 [44] 正是本文遵循的体裁。我们把价值命题因此定位于可审计表征与守恒保证，并把全部主张按三档强度标注。

本文贡献如下：

- **C1 可审计表征与会计恒等式（已闭合（预登记判定））**：三通道散射的构造性定义使 T+R+A=1 对任意参数成立，逐路径能量审计残差 2.2×10⁻¹⁶，淘汰决策可逐节点归因（§2）。
- **C2 证据强度的三档定位（已闭合（预登记判定）/一致性/动机并列）**：合成基准的路径筛选增益、真实基准的规则过滤器打平（E9.5）、耗散通道的零收益声明，全部如实并列（§2.3–§2.4）。
- **C3 融合稀释的排除性结论（已闭合（预登记判定）于所测 λ 档）**：凸组合 hybrid 在全部实测档上不超过任一单臂，λ=2 表观增益为反场伪影；增益只能来自非线性融合（§2.5）。
- **C4 博弈论化实证（已闭合（预登记判定））**：反向动力学存在可对标审计的标量（势），分布级协调比（ECR）把"离最优多远"定量化，温度前沿划定审计边界（§3）。

路线图：§2 给出表征构造、守恒恒等式、逐路径审计与证据强度的全部三档；§3 给出博弈论化证据链；§4 汇总诚实边界；§5 总结；附录给出数字追溯清单。

## 2 可审计表征与守恒保证

本节自足给出散射层的构造与守恒性质，并按预登记判定的机械求值报告证据强度。§2.1 表征构造；§2.2 会计恒等式与逐路径审计；§2.3 路径筛选增益及其归因边界；§2.4 规则过滤器打平与价值重定位；§2.5 融合稀释。

### 2.1 表征构造：从概念图到凝子态

给定自然语言问题，LLM 后端先将其分解为有向概念图 G=(V,E)：节点包括数字、运算、陷阱（表面相关但语义无关的诱饵候选）、答案候选与一般概念；BFS 在图上生成从起点到答案节点的候选路径集合。散射层在每个节点 v 上绑定一个凝子态，由路径耦合强度 g_couple≥0、以太耦合强度 g_aether≥0 与共振能量 E₀ 三参数刻画。参数不是事后任意赋值，而是按节点类型语义绑定：陷阱节点取 (5.0, 0.0)（强散射中心），运算节点取 (0.3, 0.2)，其余节点取 (0.05, 0.05)，g_couple 再乘以小度数修正。路径能量与节点共振能量之差定义失谐量 δ，经 Lorentzian 因子 1/(1+δ²) 调制有效耦合 g_eff=g_couple/(1+δ²)；散射公式受 Feshbach 共振形式的启发，但我们明确声明：下文的 T/R/A 权重是构造性定义，其归一化是设计选择而非任何 S 矩阵的推论。主实验中各节点共振能量恒等于自身能量，δ≡0，共振通道休眠，全部实测效应由 (g_couple, g_aether) 的类型对比驱动——我们写出这一点，以免读者高估共振机制当前的作用。

初始定义中的两个工作模式由此统一为同一实体的极限态：g_aether=0 时能量只在透射与反射间分配（阻塞态，错误路径本地反射衰减）；g_aether≫0 时错误能量凝华入以太、正确路径近似无损透射（隧穿态）；一般参数下三通道同开，行为由比值 η=g_aether/g_couple 连续插值。这一统一的内容仅止于"双参数连续族在参数边界上的极限行为"，其一致性检验是三个参数点上的能量分配须与两个极限定性一致（§2.2 正文验证）。

### 2.2 会计恒等式与逐路径审计

定义归一化常数 Λ=1+g_eff+g_aether，三通道能量分配权重为 T=1/Λ、R=g_eff/Λ、A=g_aether/Λ，分别对应透射、反射与向以太的不可逆耗散。由构造立即有 T+R+A=1——耗散通道被显式纳入后，系统加环境的总能量严格守恒。透射能量沿路径递归 E⁽ⁱ⁾=E⁽ⁱ⁻¹⁾T_i，累积反射与累积耗散为逐节点份额之和；对任意路径与任意参数，E⁽ⁿ⁾+E_refl+E_diss=E⁽⁰⁾（归纳一步即证）。这条恒等式的意义不在数学难度，而在可审计性：每一单位能量要么到达终点、要么被反射、要么凝华入以太，三者必有其一且仅居其一，第三方可对每条路径独立重算。

审计是实测而非承诺。对全部变体、全部 200 道合成题、全部候选路径逐次散射检验，|T+R+A−1| 的最大偏差为 2.220446049250313×10⁻¹⁶——恰为双精度机器精度量级，远低于 10⁻⁶ 的实现容差（已闭合（预登记判定）；`results/deposon_v19_benchmark_fixes.json` 的 `physics_audit` 字段，passed=true）。陷阱基准上三极限态逐路径平均耗散分别为 0 / 3.63 / 0.358（能量单位，`deposon_benchmark_v1_3_traps.json → variant_results.{v1_blocking,v2_tunneling,unified}.avg_ether_dissipated`），与理论预言定性一致：阻塞态不耗散（闭系），隧穿态大量耗散（开系，错误能量大量凝华），混合态适度耗散。以太通道在接口层面单向：`dissipate()` 把能量原子化累加进只增计数器，系统不提供 `recover()`；这对应无限维正交环境下 Poincaré 回归前提失效的物理论证。诚实声明：有限维软件实现中"不可逆"是工程锁定与渐进性质的结合，无限维近似不可数值验证，属于不可消除的理想化假设。

守恒审计还承担了一处错误更正的担保角色。冻结管线构建中 high_couple 变体实为 v1_blocking 的纯别名（配置 bug），其当时报告的 GSM8K 数字 0.86 因此错误；真修复（全场 g_couple×5、g_aether=0）后离线重跑为 0.82，4 题翻转，McNemar vs v1_blocking p=0.125，不显著（E9.3，`deposon_v19_benchmark_fixes.json`）；StrategyQA 上修复后预测向量与 v1_blocking 逐位相同（p=1.0）——物理扰动真实发生，但在 3 步浅图上不改变贪心排序。两次重跑的守恒审计均以 2.2×10⁻¹⁶ 通过：同一本账既约束物理层，也约束我们自己的更正流程。

### 2.3 路径筛选增益及其归因边界

在两个各 100 题的受控合成基准上（seed=42，真实 LLM 后端分解，最终运行零降级），完整管线（unified 变体）在简单集与陷阱集均达 100%，而同图无场贪心基线仅 7%/10%（`deposon_benchmark_v1_3_simple.json` / `_traps.json` 的 `variant_results`）。两个定界必须随数字同行。其一，该基线是诱饵捕获基线：概念图构造时诱饵边被有意赋权 0.9（高于正确运算边 0.6），93 个失败题全部选中诱饵路径；效应量 +0.93/+0.90 度量的是对抗性加权图上的同图路径筛选增量，不是通用能力提升。其二，三方消融显示增量来自标签与动力学的组合：类型标签随机置换后陷阱集准确率跌至 17.2%±6.4%（± 为 5 seeds 样本标准差，ddof=1；t95 半宽 7.9pp），全节点均匀参数下陷阱集退化为 10%（与无场基线数值重合；`deposon_benchmark_v1_3_labelshuffle.json` → `uniform_params.accuracy`）。散射层最准确的理解是换能器，把语义类型标签转换为可审计的能量决策，其增量以标签质量为前提。

真实基准上的图景更克制。GSM8K 子集（n=100，seed=42）：CoT 基线 97.0%，unified 85.0%，v1_blocking 86.0%，unified vs CoT 的精确 McNemar p=4.9×10⁻⁴，CoT 显著更优，负面结论如实报告（`deposon_benchmark_v1_4_gsm8k.json`）。85% vs 97% 的 95% 差值置信区间为 [−20.5pp, −4.1pp]（非配对 Newcombe 混合区间，与 §2.4 同一口径；`deposon_v22_e95ci.json` → `unified_vs_cot`），二项置信区间亦以 Newcombe-Wilson 方法计算。StrategyQA（n=99）：unified 89.9% vs CoT 92.9%，p=0.549，无显著差异（`deposon_benchmark_v1_4_strategyqa.json`）；且 v1_blocking、high_couple、unified 三臂同分 89.9%，约束层在该任务上未产生任何差异动作——一种"约束层惰性"，如实记录。两个真实基准合看给出约束-保真权衡的任务依赖：GSM8K 的干净长链上信息损失代价主导，StrategyQA 的短链隐式推理上约束层与 CoT 打平，约束层代价随链长与分解保真度变化。等权诱饵对照（E9.4，预登记）进一步切断错误归因：把同一缓存概念图的全部边权拉平为 0.7 后，unified 优势不消失（GSM8K 0.85 vs no_deposon 0.04，p=1.7×10⁻²³；StrategyQA 0.899 vs 0.202，p=7.5×10⁻¹⁵；`deposon_v19_benchmark_fixes.json` 的 E9.4 字段），但优势来源被定位为 BFS 短路径优先与物理层免费获得 type='trap' 标签，而非散射机制本身。因此主口径下 unified vs no_deposon 的表观效应量是结构性偏置下的不可归因数字，本文不作为防捕获价值引用。

### 2.4 E9.5 打平：差异价值只在机器可核验性

最锋利的对照是一个平凡基线。构造纯确定性规则过滤器：在同样的贪心路径生成后，丢弃经过标签命中 6 关键词表 {trap, dead, end, impossible, guess, wrong} 之节点的路径——只读标签字符串，不读类型元数据，不经过任何散射机制。结果（E9.5，预登记后机械判定）：GSM8K 上规则过滤器 0.87 ≥ unified 0.85（McNemar b=0, c=2, p=0.5）；StrategyQA 上 0.899 = 0.899（b=0, c=0, p=1.0）。在两个真实基准上，三通道散射管线与一个 6 关键词过滤器在准确率维度不可区分。功效诚实表述：在该样本量下未检出差异——GSM8K 差值 −2pp（95% CI [−11.8pp, +7.8pp]，Newcombe-Wilson）、StrategyQA 差值 0pp（95% CI [−8.8pp, +8.8pp]），两者均为非配对 Newcombe 混合区间（保守上界；配对不和谐对仅 0/2 与 0/0，配对区间退化；计算工件 `deposon_v22_e95ci.json`）；不和谐对仅 2/0 对，可检出差阈值约 ±10pp，更小的增量无法排除。故主张精确化为「差异价值只在机器可核验性」，由 E9.4 归因机制支撑，而非由本检验的强形式支撑。

打平的机制并不神秘：散射参数由节点类型标签驱动，而规则过滤器读的正是同一标签的字符串形式——信息源相同，判别能力自然相同。散射层没有从标签中榨出更多判别信息，它做的是把同一份信息转写进一个带守恒账的表示。

这一阴性结果不是失败注脚，而是价值命题的重定位依据，本论文按预登记判死规则执行，不超出数据 [49]。规则过滤器没有、散射层独占的是：任意参数下逐路径 T+R+A=1 守恒账（机器精度残差）、每次阻断留下可复核的能量记录、淘汰决策可逐节点归因到具体 (T,R,A) 份额。换言之，散射层的差异价值只在机器可核验性，不在筛选性能。与之并列的另一条零收益声明：不可逆耗散通道在全部已测任务上从未优于不开启（合成基准 v1_blocking 与 unified 同分；GSM8K 86.0% ≥ 85.0%；StrategyQA 三臂同分 89.9%），其收益主张目前仅有理论动机——单次运行内错误能量不可复活——验证需要迭代重搜场景，列为未来工作。LLM 语义信号在图任务上的条件性价值与既有证据链方向一致 [27, 28, 29]；概念图评估对协议的敏感性则是一条三十年的旧教训 [34, 35]，E9.4/E9.5 是它的当代实例。

### 2.5 融合稀释：凸组合全档不增，增益只能来自非线性融合

散射层之外，同一概念图补全任务上还有一臂语义先验（labels-only LLM 先验，零泄漏：提示词只含节点标签）。一个自然的假设是二者互补：场管结构、先验管语义，凸组合 hybrid=λ·场+(1−λ)·先验应各取所长。预登记扫描否定了这一假设的最低可操作含义。四 λ 档单图扫描 λ∈{0.25,0.5,1,2} 四档全等同（λ=0.25 即量纲饱和），named Hits@3 恒为 0.294，`any_lambda_pass=false`（`deposon_v16_llm_prior.json` 的 `success_evaluation`）；族 L 四图全候选协议 λ=0.5 档（`deposon_v20_crossval.json`，`hybrid_lambda_convex=0.5`）：physics 0.484→0.452、historical 0.783→0.739，另两图持平——hybrid 在所有实测档上不超过先验单臂，场对真语义先验只有稀释。

更进一步的消融揭示了表观增益可以如何造假。λ=2 档（场系数为 −1，先验空行等价按场降序排反）曾在归一化变体下给出 named Hits@3=0.471 的"融合增益"（`deposon_v17_fusion_fix.json` 的 `hybrid_norm@2.0` 臂）；E9.6 阴性消融把端点固定、仅打乱置信度数值后，named 与真实先验完全相等（0.1176=0.1176，随机边零假设 5 次全 0；`deposon_v19_quickwins.json` 的 `E9_6c_lambda2_null_ablation`）——该命中不可归因于语义置信度，仅能归因于端点位置与反场伪影，逐边标注在案。两条证据合起来构成排除性结论（已闭合（预登记判定）于所测 λ 档，不外推为全 λ 空间定理）：凸组合通道已关闭，场与先验的增益若存在，只能来自非线性融合机制。结构信号与语义信号的价值域划分在 GNN 文献中已有系统回答——结构偏置的有效域由图属性决定，标签信号在异配图上接管 [52, 55]——本文的稀释结论与之同向，且把划界推进到"机制上互盲的极端信号对"这一更尖锐的设定。

## 3 博弈论化：势、分布级协调比（ECR）与审计边界

§2 的守恒账只经静态核验：它证明每一次散射的能量去向合规，却没有回答动力学问题——场的反向演化作为一个整体过程，是否真有一个可对标的标量，使"每步该往哪走、走了多远、离最优还有多远"都可被同一本账审计？本节把反向动力学建模为图上势博弈，在同一预登记协议与 22 张受控概念图上给出回答。先声明口径：本节正向叙事采用 consistency 口径——证据与势博弈解读一致，是一致性证据而非形式化证明；凡预登记判定闭合（GT-5b、GT-6）或形式化判死检验闭合（GT_FORMAL、T-P1c）者，单独标注"已闭合（预登记判定）"档，不混档。本节自足给出操作化定义，不依赖其他文档。

任务与场的定义如下。任务为概念图补全：对每条金边做留一预测，候选为全部图节点，指标为 named Hits@3。散射层在图邻接权矩阵 W（行随机）上定义留一任务 (s,t) 的场引导能量 E(s,t)=−log(Σ_p Π_e t_e)+λ_smooth·Σ W²_ij，第一项为所有 s→t 路径聚合透射率的负对数，第二项为平滑正则；反向过程以退火调度（β 线性、50 步、lr=0.1）对掩码位置做单纯形自然梯度下降，其更新规则形式化为 w_{t+1}∝(1−lr)·w_t∘exp(lr·w_t∘∇Φ)，逐步投影回单纯形；结束后掩码行上的分布给出候选目标排序，即场得分。确定性均值场反向（field_mean）取 Dirichlet 起点分布均值，全程无采样噪声；对照臂在起点引入 Dirichlet 采样，浓度参数 α 扮演等效温度。语料按"结构否定 × 真实语义"两族设计：族 S（16 张，合成占位标签、与结构脱钩）用于否定"场=通用骨架检测器"的强主张；族 L（6 张，真实领域概念标签，LLM 生成，30–45 节点 DAG）承载语义臂检验。

### 3.1 建模：有限图上的势博弈

建模四元组一次给定：每条留一预测边为一个参与人（玩家），策略为候选目标节点，效用为场得分，物理能量的负值 Φ=−E 为势函数候选。势博弈的经典存在性条件由 Monderer & Shapley [1] 与 Rosenthal 拥塞博弈 [2] 给出；Sandholm [3] 的群体最好响应流证明确定性最好响应动态在群体极限下沿势函数梯度上升，是"均值场确定性反向对应无噪声最好响应动态"这一解读的最近理论支点；Candogan 等人的博弈流分解 [4] 则提供"场=图流分量"的可操作类比（本文分解边效用向量，未沿轨迹积分）。"每个任务是独立玩家"的分解是建模选择而非唯一；Φ=−E 有解析依据——反向退火梯度即 −∇E。一点必须说清：各留一任务相互独立（各有自己的 (s,t) 与各自的能量函数），故博弈层面的精确势存在性是平凡的——Φ=Σu_i 即证，无需任何检验。因此 GT-6 的贡献不在博弈势存在的非平凡证据，而在于「单任务能量函数作为标量账本的近梯度性」：在边效用向量空间（欧氏内积）中把边效用向量 F 向梯度子空间投影，p=pinv(B)F，残差比 r=‖F−Bp‖/‖F‖；r≈0 意味着该标量账本几乎完整解释边效用（§3.2）。Candogan 流分解 [4] 在此仅作操作性类比：本文分解的是边效用向量，未沿轨迹积分。

这一建模给三个概念以新语义。其一，耗散是内生承诺装置：g_a>0 时能量凝华入以太不可回流，被淘汰分支的预算不可复活，任何参与人无法通过事后改账撤销淘汰——承诺不是外部规则，而是动力学本身的性质。其二，可审计性从逐步合规检查升级为标量账：若势存在，整条轨迹可审计为一条标量曲线 Φ(t) 的逐步上升（等价地 E(t) 逐步下降），第三方无需复算每一步的全部能量分量，只需复核一条标量序列是否单调——这是守恒账在动力学层的对应物。其三，"离协调最优多远"成为可计算量：本文定义分布级协调比（empirical coordination ratio, ECR）把自利动力学与场基准的 gap 定量化。ECR 是经典 worst-case PoA（Koutsoupias & Papadimitriou 口径 [10]，Roughgarden & Tardos 仿射拥塞 PoA=4/3 界 [11]）的分布级操作化对应物，非同一度量；就我们所知，此类分布级操作化对应物此前少有系统报告（分布级报告的先例见 [13]，均衡效率的经典分析见 [12]）。口径限定见 §3.2。

### 3.2 判定性证据：审计标量的单调性、近梯度性与定量化（已闭合（预登记判定）档）

两条预登记判定闭合，一条受限一致，合起来回答"标量是否存在、定量到什么程度"。

**GT-5b 势轨迹单调性（已闭合（预登记判定），收窄主张）**：mean-field 反向的 Φ 轨迹在 22/22 张图上单调不减，单调率 100%，高于预登记线 80%，斩杀线（0 张图触发即死）未触发，判定 supports_narrowed_monotonicity 闭合（`deposon_v20_gt5b.json` → `per_graph_summary.*.meanfield_monotone_rate=1.0`）。该主张是收窄后的版本：原 GT-5 终点条件未通过（3/4 图噪声臂终点 Φ 反超，判 inconclusive，见 §3.5），单调性主张由新版预登记独立闭合，终点反转保留于案、不回溯改写。口径限定必须随行：22/22 单调是"单边留出掩码 × 语料图"口径下的冻结事实，不外推为 better-response 证据——一般掩码结构下该动态已被判死（§3.3）。

**GT-6 非势残差（已闭合（预登记判定），近梯度性口径）**：残差比 r 按 §3.1 定义（边效用向量 F 向梯度子空间的投影残差，此处只引用不重述）；非势残余中位数 1.594×10⁻²⁹，远低于 0.10 预登记线，判定 potential_game_explanation_complete 闭合（`deposon_v20_gt6.json` → `verdict.median_residual_ratio`）。重定位声明（见 §3.1）：博弈层面的精确势存在性因任务独立而平凡（Φ=Σu_i 即证），GT-6 检验的不是它，而是单任务能量函数作为标量账本的近梯度性。两处如实披露：其一，3 张循环结构图残余越线——S4=0.148、L_algorithm_process=0.136、S5=0.121，其上势解释仅为近似；其二，数值精度口径——中位残余处于双精度浮点下溢量级，反映的是"边效用向量几乎完全落在梯度子空间内"这一结构性事实，不应按绝对量级解读为物理量，3 张例外图的 0.12–0.15 残余才是有信息量的非势分量。该分解是 Candogan 流分解 [4] 的可操作类比。

**GT-4 分布级协调比 ECR（受限一致，口径限定随行）**：操作化定义 ECR=field_mean/max(自利臂)，自利臂集 {random, degree}（预登记的 llm_prior 臂在族 S 不可得，分母只可能更小、ECR 只可能偏大，如实披露）。主报全 17 张有限值图口径：median ECR=1.333 > 1.2 预登记线；族 S 子集 13 张有限值图 median 1.5 作为补充口径并列；3 张 ECR=∞ 图按既定处理规则单独计数、不入中位数（自利臂 named=0 而场>0）。GT-4 覆盖 20/22 图：L_geography_world 与 L_project_management 两域因冻结运行中臂数据缺失未评测（非 ∞、非有限值），如实交代，不影响中位数口径。两点限定：其一，ECR 是经典 worst-case-NE/社会最优比值（PoA）的分布级操作化对应物而非同一度量，成本结构仿射/可分前提未闭合，本文只作分布级报告，且不与 4/3 等任何经典 worst-case 界做数值并置——度量不同，数值接近不构成证据。其二，ECR<1 全部并列披露：族 L 两张（L_historical_causality 0.5、L_physics_concepts 0.75），族 S 中另有 S2_n45=0.5——场在语义域为负协调，与 §3.4 的分工边界自洽：场只在结构域创造协调价值，势博弈解释的适用域与该边界一致，理论不自相矛盾。冻结口径声明：判定 JSON 中的字段名（`GT4_price_of_anarchy`、`field_coordination_value_supported`）为运行前冻结口径，本文不改名；正文一律使用 ECR。

![图5：分布级协调比（ECR）全图条形（含 ECR<1 红框图与 ∞ 单独计数；中位数 1.3333、通过线 1.2 均读冻结 verdict 字段）](../figures/fig5_poa_distribution_cn.png)

（图序说明：图 5 于本节首次引用，先于 §3.4 的图 1–4 出现，系先置交叉引用；图号保持与冻结图文件命名一致，不重编。）

三条证据合看：每步演化可审计为势上升（GT-5b+GT-6，已闭合（预登记判定）于各自口径），自利动力学离协调最优的距离可计算（GT-4，受限一致）。审计标量的单调性与近梯度性实证至此成立。

### 3.3 形式化判死检验：动态等价三层级全部判死（已闭合（预登记判定），系统采样图族 × 状态全穷举口径）

§3.1 的建模包含一个解释性对应关系：确定性均值场反向 = 无噪声最好响应动态。这一对应的最强形式化版本由 GT_FORMAL 判死检验系统否定（`deposon_v21_gtformal.json`，seed=210021，判读纯函数先于运行承诺）：61 张 n≤8 系统采样小图（链/星/树/随机 DAG/含环五族）× 其上 338 个单节点全候选掩码任务 × 20 步 mean-field = 6760 个判死状态的全穷举——即穷举作用于任务/状态层，图族为系统采样。强度档为"已闭合（预登记判定）（系统采样图族 × 状态全穷举口径）"——已闭合（预登记判定）的是各强式表述在该口径下不成立这一否定性事实本身，判死即答案，强度不向上取整。判死逻辑不依赖穷举完备性：全称命题一个反例即死，10/338 违例已充分。

- **P1a 强式动态等价：证伪**。max‖T−BR‖∞=0.8569；lr 扫描显示方向偏差 1−cos≈0.91 不随 lr 消失——O(1) 偏差而非 O(lr²) 离散误差，不是步长问题。
- **T-P1b better-response 版：判死**。min 方向余弦 −1.0、min ΔΦ=−1.2424×10⁻²（判死线 −1e−9），10/338 任务违例、全部位于循环空间非空的支持图。机制一句话：复合算子 T=Π∘C∘M 的不动点不是 Φ 的行约束极大点，轨迹过峰后继续推进（过冲），过极大点后 ΔΦ<0。
- **P1c 残余熵正则刻画：判死（T-P1c，`deposon_v22_p1c.json`，同一系统采样-状态穷举口径，判定函数先于运行预登记）**。残余主张为"一阶更新方向 = 熵正则势 Φ_τ=Φ+τH 的镜像上升方向"（τ>0 时熵项或可修复过冲）。双判死线双杀：强式要求全局统一 τ 下 min 方向余弦 ≥0.999——τ∈[0,4] 81 档网格全灭，最优全局 τ 处 min cos=−1.0；弱式允许 τ 逐状态自选（τ*）要求 min cos≥0.99——min cos=−1.0，存在过冲状态与任意熵正则镜像方向严格反向；逐状态 τ* 中位数=0（85.98% 状态 τ*=0），熵项无修复力。判定函数由 11 项测试锁定，同种子复跑逐字节一致。

三层级——P1a 强式、P1b better-response、P1c 一阶熵正则刻画——全部判死后，博弈论主线不再保留动态等价残余主张。需要澄清的是口径关系：GT-5b 的 22/22 单调（单边留出掩码 × 语料图）不受影响，仍是闭合的冻结事实；本检验在"全候选掩码 × 小图系统采样"强化口径下证明一般掩码结构中该动态不是 better-response。两个口径各自在案，不互抵。

**预登记时间锚**：判定纯函数与 SPEC 在运行前冻结，SHA-256 锚点（前 12 位）：GT_FORMALIZATION_v1.md = aeefb8ef6972；run_v21_gtformal.py = 9bbe43f41fa8；run_v22_p1c.py = 6e9673205dc0；SPEC_GT2B = 68a5b08ef007；SPEC_GT8C = 6b09de9911c0。任何人可用锚点核对冻结版本后机械复跑判定。

**P2 势完备性：降级为近似势博弈**。无环（无向森林）支持图残余 r≤5.9×10⁻¹⁶（数值零）；含循环空间支持图 r 中位 0.669、r>0.30 占比 0.924 > 1/3 预登记降级线，触发降级判定 downgraded_to_approximate_potential_game——与 GT-6 三张循环结构图例外方向一致且量级更高（全候选掩码支持图更密）。

**P3 耗散通道：双向皆死，但换来首个机制性前提证据**。"耗散只是支付重参数化"判死（max|r(0.1)−r(0)|=0.1585 > 1e−9）；"均衡集不变"同样判死（三档 g_a 的最好响应不动点 max 差异 0.8442）——耗散非纯重参数化，真实移动均衡位置。附带发现改变了耗散通道的证据格局：58/338 任务在 g_a=0 且支持含环时 ρ(G)=1 使 (I−G) 奇异，闭式动力学发散；而收敛的谱条件 ρ(G)<1 恰由耗散 g_a>0 保证——这是 g_a>0 的构造内嵌性质，作为机制性前提证据归档（此前仅有"无租金"的阴性口径，§4 再议）。

### 3.4 划界与边界规律：可审计优势的成立域（方向性证据，不升级）

审计标量存在之后，下一个问题是"它在哪些图上成立"。本小节给出划界规律及其全部限定，定位为观察性规律（方向性证据），不作为已确立的判别器贡献。

**成立域收缩（预登记判定）**：主基准 H-A1（field_mean > random）判死——22 图符号检验 16+/4−/2 平、p=0.0118 过 Holm，但预登记斩杀线为析取规则（不显著或 ≥3 张图反转），反转图达 4 张（L_historical_causality、L_physics_concepts、L_project_management、S2_n45），斩杀线触发，头条主张判死。存活表述为 H-A2（field_mean > degree）跨口径稳健：22 图 19+/1−/2 平，p=4.0×10⁻⁵，Holm 过；20 图子集经 Wilcoxon（p=0.0031，|r|=0.83，r=Z/√N）与配对 t（p<0.0001，d=2.05，Cohen's dz）复核为大效应；Hits@3 为有界离散量，以 Wilcoxon 为主判据、配对 t 仅为参照。多重性声明：Holm 修正仅施加于 H-A1/H-A2 同族；各 GT 实验各自独立预登记、独立判定，跨族不做合并修正，如实声明。场的成立域由此收缩为"相对平凡结构基线的稳健优势 + 高枢纽图局部优势"。

![图1：分工边界总览（22 图场-先验胜负地图；场臂条形 + 族 L 先验臂条形 + random/degree 参考散点，逐图第一名以 ★ 标注）](../figures/fig1_boundary_map_cn.png)

![图2：H-A1 斩杀线与反转图分布（22 图符号检验散点，n_pos=16/n_neg=4/n_tie=2，反转四图红框标注）](../figures/fig2_killsign_scatter_cn.png)

**跨厂商稳健性（GT-3b，受限一致）**：五个评估者（三模型族）在 Kimi 生成的图上复现先验优势——doubao 4/4、deepseek 6/6 通过判据，三模型族合计 0 域先验 ≤ 场，全 ok 域 Kendall W=1.0（逐域排序完全一致）。"先验优势是同厂商同源污染 artifact"假说被实质性削弱；残余局限：三族均为中文优化大模型，共享中文语料不可排除。

**划界规律**：探索性回归（n=20）显示 hub_concentration（最大入度/边数）与场效力同向且是最强相关子（正向，p=2.8×10⁻⁴），real_semantics 显著压低场表现（负向，p=0.012），R²=0.628；系数点估计移至附录 A 归档，正文只保留方向与显著性；两点限定——n=20 小样本标记探索性，特征本身是语料设计变量、存在准循环性，系数只说明方向性关联。语料外复现：hub 轴 2 对配对新图 2/2 同向（仅方向，功效只够分辨极大效应）；real_semantics 轴合计 3/4 域满足"先验强"——GT-8b 两个新域 2/2 通过 0.6/0.2 预登记阈值（chinese_dynasties 先验 0.7805 vs 场 0.0732；chemical_elements 0.6429 vs 0.1429；初判 inconclusive 经预登记修正案补数转正，链条在案），GT-8c 跨后端复测判 mixed——biological_taxonomy 先验 1.000 vs 场 0.075（diff +0.925）过线，programming_concepts 先验 0.500 vs 场 0.3333（diff +0.1667）未达 margin 阈值，且 GT-8c 图生成臂与先验臂同后端同模型，同源污染风险在案。规律表述：hub_concentration 高 → 结构信号整体可用（非场独占）；real_semantics=1 → 用语义先验。域间异质性在案，强度档维持方向性证据，不外推至族 L 之外任务或更大规模图。

![图3：分工规律散点（hub_concentration × real_semantics 着色 field_named，20 图样本，回归系数读冻结字段）](../figures/fig3_division_scatter_cn.png)

### 3.5 一致性证据与 inconclusive 归档

主线判定之外，四条弱证据如实归档，不升级、不删除。

**GT-1（一致性，弱鉴别力）**：Dirichlet 噪声反向在命中率口径下全面劣于确定性极限——dirichlet 均值 0.10 vs mean-field 0.40，gap=0.30 ≥ 0.2 预登记线，20/20 运行严格劣。鉴别力声明：任何噪声劣化都满足此模式，该证据只作背景一致性，不单独支撑势博弈解读。

**GT-2（受限一致，no_separation）**：攻击者知道关键词表后 100% 生成绕过规则的语义陷阱标签（evasion_rate=1.000，4/4 图）；注入 10 个陷阱节点/图后 rule_filter 平均 −7.5pp（三图各 −10pp，第四图 0pp），field_mean −0.0pp（四图全零）。预登记机械判定 no_separation：规则塌陷未达 20pp 阈值，攻击强度未达决定性，不升级为"规则防御失效"主张；场不读标签、对语义陷阱机制性免疫的方向性信号在案。规则防线失效的文献证据链 [22, 23, 24, 25, 26] 与自适应攻击方法学 [20] 与该方向一致，但本文不据此定强度。

**GT-5 与 GT-2B（inconclusive 归档）**：GT-5 终点条件未通过——3/4 图上噪声臂终点 Φ 高于 mean-field（S6 gap=−0.31），判 inconclusive，不回溯改写；解读为"噪声是探索者、mean-field 是利用者"，与 log-linear learning [50] 和确定性最好响应的经典分工一致，散射层的"温度"由此获得博弈论语义而非调参旋钮，收窄后的单调性主张已由 GT-5b 独立闭合（§3.2）。GT-2B 多陷阱强度升级（T∈{1,2,3}）判 inconclusive：rule_filter 0.150/0.275/0.200 非单调，且固定 4 选项设计使图内候选数随 T 反比变化，场免疫判据被选项构成污染（场准确率 0.375/0.525/1.000 机械上升）——设计教训归档为"免疫判据须对选项自由度稳健"。

**GT-7 温度前沿（mixed，审计边界）**：α∈{0.3,…,20} × 4 图 × 5 seed。GT-5 反转可复现且系统化（同 3/4 图高温档终点 Φ 反超，Φ 增益集中在高温端，corr=−0.87），温度确实控制全局势探索收益；但"双赢前沿"不成立——S6 高温档 Φ 升而命中率 0.4→0.08。势与命中率是两个目标，审计承诺只覆盖前者：升温只提势探索、不兼提命中率，审计边界由此划定。边界情形披露：命中率=0 的图使条件退化恒真，未回溯改规则。

![图4：GT-7 温度前沿逐图形态（命中率与终点 Φ 双轴，4 图 × 6 温度档 × 5 seed，verdict=mixed）](../figures/fig4_gt7_frontier_cn.png)

## 4 诚实边界

本文证据强度的三档不混档，局限集中声明如下，每条均可追溯至前文判定记录。

**其一，形式化等价三层级全部判死——最明确的局限**。"均值场反向 = 无噪声最好响应动态"的强式表述在系统采样图族 × 状态全穷举判死检验（61 图/338 任务/6760 状态）下被明确否定：P1a O(1) 偏差 0.8569、P1b min 余弦 −1.0（过冲机制在案）、T-P1c 在 τ∈[0,4] 81 档网格与逐状态自选 τ* 下双杀（min cos=−1.0，τ* 中位 0）。这意味着本文全部博弈论解读不能以"动态实现了最好响应"为依据；GT-5b/GT-6 原口径外不再保留残余主张，博弈论主线的正向叙事只有 consistency 口径。判死方向不软化：被否定的不是某个参数配置，而是对应关系本身。

**其二，consistency 口径**。除已闭合的预登记判定（GT-5b、GT-6）与判死结论外，正向证据为一致性证据而非形式化证明——轨迹与势博弈解读吻合，不等于证明了势函数定理。该口径不放松，但也不升级为定理；读者应据此校准对 §3.2 合取陈述的信任度。

**其三，族 L 图由单一厂商 LLM 生成**。评估者跨厂商问题已由 GT-3b 处理（0 败绩、W=1.0），但图生成器单一厂商问题未闭合：图的结构与标签分布携带生成模型的偏好。三受测族均为中文优化大模型，共享中文语料的同源污染不可排除，非中文模型族与人工标注图的检验仍为开放局限。

**其四，题库轨 n=40/格小样本**。±1 题=±2.5pp，与机会噪声同阶，该轨全部数字（含先验 92.5%、场 52.5%、规则 27.5%）按小样本宽区间解读，不作效应量引用。

**其五，划界规律为探索性证据**。n=20 回归存在特征-设计循环性（预测子本身参与语料设计）；hub 轴 2 对配对仅方向、功效只够分辨极大效应；real_semantics 轴 3/4 域满足但域间异质性在案（GT-8c mixed，programming_concepts 未过线）。规律不作为判别器贡献，不外推至族 L 之外任务或更大规模图。

**另加一条：耗散通道的收益仍仅有动机**。GT_FORMAL 的附带发现给出耗散的机制性前提证据——这是 g_a>0 的构造内嵌性质（保证谱条件 ρ<1、避免 58/338 任务发散），但任务级租金在全部已测任务上仍为阴性——合成基准 v1_blocking 与 unified 同分，GSM8K 86.0%≥85.0%，StrategyQA 三臂同分 89.9%。机制性前提（保证收敛存在，构造内嵌性质）与任务级租金（带来准确率收益）是两件事：前者已闭合（预登记判定），后者在本文全部已测任务上为零，其验证需要迭代重搜场景，列为未来工作。

## 5 结论

本文围绕一个空层——运行期逐实例不变量——给出两条并重的成果线。可审计表征与守恒保证（§2）：三通道散射的构造使 T+R+A=1 对任意参数成立，逐路径审计残差 2.2×10⁻¹⁶，淘汰决策可逐节点归因；同时以预登记对照判死了表观准确率优势的可归因性（E9.4/E9.5），把价值定位于机器可核验性。博弈论化（§3）：审计标量的单调性与近梯度性实证闭合（GT-5b 22/22 单调、GT-6 残余中位 1.594×10⁻²⁹），分布级协调比 ECR=1.333 把"离协调最优多远"定量化，温度前沿划定审计边界；同时以最明确的判死结论封死了"动态=最好响应"的全部三层级形式化表述，并以 P2 降级与 P3 双向判死划清势解释的适用域，附带获得耗散保证收敛的机制性前提证据（g_a>0 的构造内嵌性质）。两条线共同的体裁纪律是：判死结论与已闭合（预登记判定）结论同等分量，三档强度不混档，阴性结果全部归档不美化。散射层在该样本量下未检出准确率差异（E9.5：GSM8K −2pp，95% CI [−11.8pp, +7.8pp]；StrategyQA 0pp，95% CI [−8.8pp, +8.8pp]，均为非配对 Newcombe 混合区间（保守上界；配对不和谐对仅 0/2 与 0/0，配对区间退化；`deposon_v22_e95ci.json`）；±10pp 以下的增量无法排除，差异价值主张由 E9.4 归因机制支撑），凸组合融合在所测 λ 档上只有稀释（E9.6），"动态=最好响应"被系统采样图族 × 状态全穷举判死——这三类否定与守恒账、势单调性、ECR 定量化三类肯定一样，都是本文的结论而非注脚。散射层的价值命题因此收束为一句话：它不更准，但它记账，且账可被任何持有双精度算术的第三方逐步重算。

未来工作仅列以下各项：可训练 KGE 基线（TransE/ComplEx/RotatE，20 图规模排期）；扩图后重估探索性回归；hub 轴升级至 ≥6–8 对配对图以提升功效；题库轨对照 SPEC_GT2C、单调终点重测 SPEC_GT5C 已预登记待执行。动态等价三层级均已判死，不再列入未来工作。

## 附录 A：数字追溯表

全部关键数字逐一对应 `results/` 下冻结 JSON 的具体字段（判定由脚本机械读取，禁止手写）。

| 数字 | 源 JSON → 字段路径 |
|---|---|
| 守恒审计残差 2.220446049250313×10⁻¹⁶，passed=true，容差 1e-6 | `deposon_v19_benchmark_fixes.json` → `physics_audit.t_plus_r_plus_a_max_deviation`、`physics_audit.passed`、`physics_audit.tolerance` |
| E9.3 修复后 GSM8K 0.82，4 题翻转，McNemar p=0.125；StrategyQA p=1.0 | `deposon_v19_benchmark_fixes.json` → `experiments['E9.3_high_couple_fix']` |
| E9.4 等权对照 GSM8K 0.85 vs 0.04（p=1.7e-23）、StrategyQA 0.899 vs 0.202（p=7.5e-15） | 同上 → `experiments['E9.4_equal_weight_decoy_control'].benchmarks` |
| E9.5 规则过滤器 GSM8K 0.87 vs 0.85（b=0,c=2,p=0.5）、StrategyQA 0.899=0.899（p=1.0） | 同上 → `experiments['E9.5_rule_baseline'].benchmarks` |
| E9.5 差值 95% CI：GSM8K [−11.8,+7.8]pp / StrategyQA [−8.8,+8.8]pp（非配对 Newcombe，保守口径）；unified vs CoT（GSM8K）−12pp，CI [−20.5,−4.1]pp | `deposon_v22_e95ci.json` → `gsm8k`/`strategyqa`/`unified_vs_cot`（`method`/`ci`） |
| 合成基准 unified 100%/100% vs 诱饵捕获基线 7%/10%（seed=42） | `deposon_benchmark_v1_3_simple.json` / `deposon_benchmark_v1_3_traps.json` → `variant_results` |
| 标签置换消融 17.2%±6.4%；均匀参数退化 10%（陷阱集） | `deposon_benchmark_v1_3_labelshuffle.json` → `label_shuffle` / `uniform_params` |
| GSM8K：CoT 97.0%、unified 85.0%、v1_blocking 86.0%，p=4.9e-4 | `deposon_benchmark_v1_4_gsm8k.json` |
| StrategyQA：unified 89.9% vs CoT 92.9%（p=0.549），三臂同分 89.9% | `deposon_benchmark_v1_4_strategyqa.json` |
| 融合稀释：physics 0.484→0.452、historical 0.783→0.739（λ=0.5 凸组合） | `deposon_v20_crossval.json` → `hybrid_lambda_convex=0.5` 逐图字段 |
| 四 λ 档单图扫描四档全等同，named Hits@3=0.294，any_lambda_pass=false | `deposon_v16_llm_prior.json` → `success_evaluation` |
| λ=2 归一化变体表观 0.471；E9.6 阴性消融 0.1176=0.1176、随机边 5 次全 0 | `deposon_v17_fusion_fix.json` → `hybrid_norm@2.0`；`deposon_v19_quickwins.json` → `E9_6c_lambda2_null_ablation` |
| H-A1 判死：16+/4−/2，p=0.0118，斩杀线触发，反转 4 图 | `deposon_v20_corpus_eval.json` → `verdicts.H_A1_field_mean_gt_random.sign_test`、`verdicts.kill_lines.H_A_dead` |
| H-A2 存活：19+/1−/2，p=4.0e-5 | 同上 → `verdicts.H_A2_field_mean_gt_degree.sign_test.p_exact=4.005e-05` |
| Wilcoxon p=0.0031/\|r\|=0.83；配对 t p<0.0001/d=2.05 | `v20_statcheck_fm_vs_rand.json`（p_value=0.003052）、`v20_statcheck_fm_vs_deg.json`（p=2.13e-08，d=2.0478） |
| 回归 β(hub)=2.12（p=2.8e-4）、β(real_sem)=−0.16（p=0.012）、R²=0.628、n=20 | `v20_regression_field_v2.json` → `coefficients.*`、`r_squared=0.628226`、`n_observations=20` |
| GT-1 gap=0.30（0.10 vs 0.40），20/20 运行严格劣 | `deposon_v20_gt.json` → `GT1_potential_game_convergence.verdict` |
| GT-4 ECR median 1.333（17 图）/ 1.5（族 S 13 图）；族 L 0.5/0.75；∞×3 单独计数不入中位；S2_n45=0.5（字段名 `GT4_price_of_anarchy` 与 `field_coordination_value_supported` 为冻结口径，不改名；覆盖 20/22 图：L_geography_world 与 L_project_management 臂数据缺失未评测，非 ∞、非有限值） | 同上 → `GT4_price_of_anarchy.verdict.poa_per_graph_finite`、`n_poa_inf=3` |
| GT-5b 22/22 单调（单调率 100%，预登记线 80%） | `deposon_v20_gt5b.json` → `per_graph_summary.*.meanfield_monotone_rate=1.0` |
| GT-5 终点反转 S6 gap=−0.31（3/4 图 inconclusive） | `deposon_v20_gt5.json` → `per_graph_detail.S6` |
| GT-6 残余中位 1.594e-29；例外 S4=0.148 / L_algorithm_process=0.136 / S5=0.121 | `deposon_v20_gt6.json` → `verdict.median_residual_ratio`、`per_graph_summary.*.residual_ratio_mean` |
| GT-7 mixed：corr −0.87；S6 命中率 0.4→0.08 | `deposon_v20_gt7.json` → `per_graph`（corr −0.87 为文档汇总值（GT_RECONSTRUCTION §7），非字段直读） |
| GT-2 no_separation：rule −7.5pp（0.1/0.0/0.1/0.1）、field −0.0pp、evasion=1.0 | `deposon_v20_crossval.json` → `gt2_verdict`、`gt2_attacker_meta.*.evasion_rate=1.0` |
| GT-2B inconclusive：rule 0.150/0.275/0.200；场 0.375/0.525/1.000 | `deposon_v20_gt2b.json` → `verdict`、`per_T.*.per_domain.*.accuracy` |
| GT-3b：doubao 4/4、deepseek 6/6、0 败绩、Kendall W=1.0 | `deposon_v20_gt3.json` → `verdict.H_GT3_supported=true`、顶层 `kendall_W=1.0` |
| GT-8 2/2 同向（对 A +0.7917>+0.1333；对 B +0.0526>−0.0833） | `deposon_v20_gt8.json` → `verdict.verdict="supports_H_GT8"`、`per_pair.*` |
| GT-8b supports_H_GT8B：chinese_dynasties 0.7805 vs 0.0732（diff +0.7073）；chemical_elements 0.6429 vs 0.1429（diff +0.5000） | `deposon_v20_gt8b.json` → `gt8b_verdict`、`per_domain.*.named_summary`、`prior_named_minus_field_named` |
| GT-8c mixed：biological_taxonomy 1.000 vs 0.075（diff +0.925）过线；programming_concepts 0.500 vs 0.3333（diff +0.1667）未过线；vendor=volces_ark_bytedance | `deposon_v20_gt8c.json` → `gt8c_verdict`、`per_domain.*.named_summary`、`backend.*` |
| GT_FORMAL：P1a max‖T−BR‖∞=0.8569、1−cos≈0.91 不随 lr 消失；P1b min cos=−1.0、min ΔΦ=−1.2424e−2；P2 无环 r≤5.9e−16、含环中位 0.669、占比 0.924；P3 max r 差异 0.1585、不动点差异 0.8442、g_a=0 发散 58 任务；61 图/338 任务/6760 状态 | `deposon_v21_gtformal.json`（seed=210021）→ `verdict.T_P1b`、`verdict.P1a_deviation`、`verdict.T_P2`、`verdict.T_P3`、`residuals.dag`、`residuals.cyclic`、`n_graphs/n_tasks/n_states` |
| T-P1c 判死：τ∈[0,4] 81 档全灭、min cos=−1.0（强式与逐状态 τ* 双杀）、τ* 中位 0（frac_at_tau0=0.8598） | `deposon_v22_p1c.json`（seed=210021）→ `verdict`、`descriptive.tau_star_per_state`、`tau_grid` |
| 三极限态逐路径平均耗散 0 / 3.63 / 0.358（能量单位） | `deposon_benchmark_v1_3_traps.json` → `variant_results.{v1_blocking,v2_tunneling,unified}.avg_ether_dissipated` |

**Artifact availability**：全部代码、冻结 JSON、判定纯函数与测试套件均在仓库内，可按 §3.3 的 SHA-256 锚点核对冻结版本后机械复跑全部判定。

## 参考文献

> 编号沿用统一外部文献体系；核实标注见 docs/REF_VERIFICATION_v2.md（[21] 修正、[52]–[59] 核实，2026-08-30）。部分编号为体系完整性保留。

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
[21] Nasr, M., Jagielski, M., Carlini, N., Tramèr, F. 等，"Tight Auditing of Differentially Private Machine Learning"，USENIX Security 2023, pp. 1631–1648（已核实并修正 2026-08-30：原标注 USENIX Security 2025 不存在，核实结论 CORRECTED，见 docs/REF_VERIFICATION_v2.md）。
[22] Gröndahl et al., AISec 2018。
[23] Hosseini et al. 2017。
[24] Kahu & Ahuja 2025。
[25] Jain et al. 2023。
[26] HateBench, USENIX Sec 2025。
[27] KICGPT, Findings of EMNLP 2023。
[28] KG-LLM/Yao et al., ICASSP 2025。
[29] Wadhwa et al., ACL 2023。
[30] Berglund et al., ICLR 2024（Reversal Curse）。
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
[52] McPherson, Smith-Lovin & Cook 2001（同质性综述）（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[53] Pei et al., Geom-GCN, ICLR 2020（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[54] Zhu et al., H2GCN（Beyond Homophily）, NeurIPS 2020（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[55] Zheng et al., 异配图 GNN 综述, 2022（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[56] Luan et al., Revisiting Heterophily, NeurIPS 2022（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[57] Zhang & Chen, SEAL, NeurIPS 2018（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[58] Srinivasan & Ribeiro, 位置嵌入与结构表示等价性, ICLR 2020（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[59] Mao et al., Demystifying Structural Disparity, NeurIPS 2023（已核实 2026-08-30，见 docs/REF_VERIFICATION_v2.md）。
[60] Wei et al., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", NeurIPS 2022。
[61] Yao et al., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", NeurIPS 2023。
[62] Wang et al., "Self-Consistency Improves Chain of Thought Reasoning in Language Models", ICLR 2023。
[63] Turpin et al., "Language Models Don't Always Say What They Think", NeurIPS 2023。
[64] Lanham et al., "Measuring Faithfulness in Chain-of-Thought Reasoning", TMLR 2023。
（[31] 写作时点可查性未能确认，已删除；正文未引用该条，无需同步修改。）
