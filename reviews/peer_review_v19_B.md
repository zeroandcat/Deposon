# 📋 同行评审报告（独立评审 B，v19 轮）

**评审对象**：`paper/deposon_paper_v1.md`（中文版，586 行）与 `paper/deposon_paper_v1_en.md`（英文版，511 行）
**评审标准**：高水平 ML 会议/期刊通用标准（NeurIPS/ICML 方法学审稿口径）
**评审侧重**：按委托，**维度四（写作）与维度一（原创性）最深**，方法论/结果亦评但深度次之
**核验方式**：双语全文逐节通读；程序化核验（[1]–[37] 引用完整性、表格首引顺序、摘要词数、措辞频次统计、引号/破折号密度）；抽查 `deposon_agents_v1_4.py` 源码核实真实基准图构造；附加检查单按 sci-paper-cn / research-paper-refiner / humanizer-zh 逐项执行。下文行号以 CN=中文版、EN=英文版标注。

---

## 总体评价

- **推荐决定**：**Major Revision**
- **总体评分**：**4.5 / 10**
- **一句话总结**：本文的诚实文化（根因分析、负面结果归档、预登记 SPEC、配对统计）与四脉络结构式相关工作在"物理启发 LLM"类投稿中属上乘；但**理论核心（归一化散射权重 + Feshbach 形式类比）按作者自认不产出任何非平凡预测，核心卖点"不可逆耗散通道"在全部五个实验小节中未产生一次可测的任务收益，两组能判定物理层因果贡献的平凡对照（标签规则过滤基线、合成基准直接 CoT）缺失，且双语稿件的摘要体量（EN 604 词 / CN 约 1440 字）、贯穿正文的版本考古与应答评审文体、全面乱序的表格编号**，使论文目前距投稿线尚有一次结构性改写的距离。

---

## 1. 原创性（Originality）

**评分**：**5 / 10**

**优点：**
- **问题定位有独立视角**：把"错误路径的可逆复活"识别为 CoT/ToT/SC 的结构性缺口（§1 第三段），并以"守恒律 + 不可逆淘汰 + 逐路径审计"三要素作为统一判据组织四条相关工作脉络（§2 小结）。以"淘汰机制是否可逆、是否可审计"为坐标的综述框架，在文献中确属新鲜。
- **元方法论贡献真实存在**：C3（消融失效模式根因：答案-筛选脱钩、陷阱不可达）与"诱饵基线 vs 中性基线"的区分（§4.1）是可复用的消融设计教训；"先承诺双向判读框架 + 负面结果如实报告"（§4.2）的范式对社区有示范价值。
- **自我定界罕见地清楚**："换能器而非独立判别器"（§4.1 Table 6 后）、"效应量度量同图路径筛选增量而非对 LLM 本体的超越"（§5.1）等表述，作者对自身贡献边界的认知比绝大多数投稿诚实。

**问题与建议：**

- 🔴 **Major（O1）：理论核心的原创性主张超出其实际内容，"统一极限命题"须降级或补强。** 式 (2) 的 $T=1/\Lambda,\ R=g_{\text{eff}}/\Lambda,\ A=g_{\text{aether}}/\Lambda$ 是三参数 softmax 型归一化权重；式 (1) 的 Lorentzian 只是把 Breit–Wigner 线宽取为自然单位（附录 A.2 自认"取线宽为自然标度单位 Γ/2=1"）；式 (4) 的 Feshbach 形式按 §3.1 与附录 A.3 的反复声明"提供物理动机与词汇，而非推导"。于是"统一极限"的全部数学内容是"一个双参数连续族在其参数边界上的极限行为"——这是一句话的观察，不是一个命题；其唯一可检验推论（$\eta=g_{\text{aether}}/g_{\text{couple}}$ 连续扫描，§3.1 明确"留作未来工作"）全文未做。标题、摘要与贡献 C1 目前以"physics-constrained / Feshbach 共振型"为首要卖点，与其实际理论存量不匹配。→ 修改路径（二选一）：(i) 将 C1 改写为"一种带守恒审计的参数化路径评分设计"，删除"命题""统一"等理论化措辞，压缩 §3.1 与附录 A 的类比篇幅；(ii) 若要保留理论主张，给出至少一个由 Feshbach 形式导出且非构造平凡的定量预测（最自然是 $\eta$ 扫描下的通道份额曲线与临界点），并用实验区分于"纯归一化权重"的平凡行为。
- 🔴 **Major（O2）：核心卖点"不可逆耗散"在全部实验中零可测收益，贡献主张与证据错位。** 论文的差异化主张是耗散通道的不可逆性（§1、§3.3、§5.3 的硬件映射也建立在 $g_{\text{aether}}$ 上）。但逐一核对：合成基准上 v1_blocking（无耗散通道）以**零耗散**达到同样的 100%（Table 2/3），§4.1 观察 (1) 自认"单看能量代价 v1 更优……需要迭代重搜的任务才是该差异的预期受益场景（未来工作）"；GSM8K 上 v1_blocking 86.0% ≥ unified 85.0%（Table 10）；StrategyQA 上 v1=high_couple=unified 均为 89.9%（Table 12）；§4.6 退火/集成无净收益。即**在本文任何一个任务中，开启耗散通道都未曾优于不开启**——不可逆性的价值完全寄托于未做的"迭代重搜"实验。§4.4 的审计证明的是恒等式成立（构造性平凡），不是机制有效。→ 必须修改：增加一个不可逆性产生可测收益的场景（最直接：多轮迭代搜索/重规划任务，对照"预算可回流"与"预算锁定"两种设置下的预算-准确率曲线）；若不做该实验，则摘要、§1 与结论中关于不可逆耗散的主张必须降格为"设计动机与未来验证方向"，标题层面的 "Physics-Constrained" 也应重新斟酌。
- 🟡 **Minor（O3）：相关工作对"可逆复活"缺口的措辞过强。** ToT/GoT 在**单次搜索运行内**的剪枝同样是不可逆的（被丢弃分支不复活）；"复活"只发生在跨轮采样/跨 prompt 之间，而这一场景本文从未实验（见 O2）。§1 第三段与 §2(a) 的表述会让熟悉搜索文献的审稿人认为在攻击稻草人。→ 建议精确化为"现有方法在单次运行内同样不可逆地剪枝，但其淘汰决策无可审计的守恒账；且跨轮重搜时无任何机制阻止错误模式重生"——后一分句才有实验缺口可补。
- 🟡 **Minor（O4）：与最邻近实验传统的设置级对比缺失（CN 版尤甚）。** GSM-Symbolic [36] 的"无关数字诱饵"设置与本文陷阱分类学（附录 B.2）几乎同构，EN §2(a) 已补一句（65 个百分点的 NoOp 退化），但 CN §2(a) 完全没有该讨论，且两版都未回答"自建基准相对 GSM-Symbolic 变体集的增量是什么"。另缺 verifier/PRM 引导搜索（区别于 [9] 的训练侧过程监督）与能量基重排（energy reranking）等相邻工作的引用。→ 建议在 §2(a) 增补设置级对比段，并说明自建基准的必要性。
- 🟡 **Minor（O5）：贡献 C2 中"向量化散射 <0.2 ms"（§3.2、附录 C.2/C.3）作为贡献点过弱**——1000 个标量除法的 NumPy 耗时没有信息量。→ 从贡献列表移除，降级为工程注记。

---

## 2. 方法论（Methodology）

**评分**：**4 / 10**

**优点：**
- 消融受控性意识好：五变体共享散射引擎与路径集合、仅改参数（§3.4）；label-shuffle 保持类型数量不变；labelfree 与 unified 同图同路径集合。
- 根因分析的机制链完整可复核：93 题失败 → final_score 恒 1.0 并列 → 稳定排序退化为 BFS 顺序 → 诱饵边权 0.9>0.6（§4.1），是教科书级失败归因。
- 统计实践规范：精确 McNemar 双侧、Wilson 区间、配对 bootstrap（B=20000，seed 固定），且明确拒绝用不显著 p 值做正向主张（附录 D.5 末）；敏感性分析明确标注 post-hoc（§4.2）。

**问题与建议：**

- 🔴 **Major（M1）：缺少能分离"物理层增量"与"标签信息增量"的决定性平凡基线。** Table 6 已证明准确率由类型标签承载（label-shuffle 跌至 17.2%），labelfree 只是把标签换成边权签名、而边权又是 label→weight 转写（作者如实承认）。但全篇缺一个最直接的对照：**"概念分解 + 按 trap 标签直接规则过滤候选路径 + fold"（不经过任何散射/耗散机制）**。若该基线也达 100%（几乎可预期——散射公式在 trap 节点 $g_{\text{couple}}=5$ 绑定下的效果与"过滤掉含 trap 节点的路径"在判别上等价），则三通道散射对准确率的因果贡献为零，物理层剩余的是审计表征价值——这恰应是论文的诚实结论，目前被回避。→ 必须在合成基准与 GSM8K 上各补一组 rule-based label-filtering 基线；若打平，摘要与 §5.1 的价值命题须从"路径筛选"改写为"可审计表征"。
- 🔴 **Major（M2）：合成陷阱基准的难度前提从未验证。** §4.1 的全部对照都在"概念图 + 选路"框架内，但论文从未报告**同一 LLM 后端用 CoT 直接回答这 100 道陷阱题**的准确率。若直接 CoT 也能 ~95%+（陷阱由模板生成、模式仅六类），则"陷阱集是表面关联误导的受控极限"（§5.1）的前提不成立，+0.90 是对一个对该模型并不困难的人造分布的增益；反之若 CoT 确实低，那正是"陷阱真实"的最直接证据。→ 必须补报同一后端在两基准上的 zero-shot CoT 准确率（题目与缓存体系现成，约 200 次调用），作为 §4.1 的参照行。
- 🔴 **Major（M3）：真实基准（GSM8K/StrategyQA）的概念图沿用了论文自己定性的"对抗性诱饵边权"，且 §4.2/§4.3 未按其自订标准重述。** 本文在 §4.1 已把合成基准的 no_deposon 7% 重定性为"诱饵捕获基线……不应作为通用贪心基线引用"（CN L196）。但我核对 `deposon_agents_v1_4.py`（即附录 C.4 声明的 GSM8K/StrategyQA 管线）发现同一构造：正确链 N1→OP1 边权 0.6（L848/855/862），而 LLM 自陈 trap 注入边权 0.9（L890）、Trap_Order 边权 0.85（L908）、**每题无条件注入 Trap_DeadEnd 死胡同、边权 0.8**（L916），且 L1582 注释明写"no_deposon 变体因此被诱饵捕获"。这意味着 Table 10 的 no_deposon 2.0%、Table 12 的 12.1%、以及摘要与 §4.3 的"相对无场基线保持极显著增益（$p=1.8\times10^{-16}$）"，度量的是同一种人造构造下的增量。按论文在 §4.1 自订的标准，这些数字必须同等降级。→ 必须修改：(i) §4.2/§4.3 正文与 Table 10/12 行注披露真实基准图构造含注入边权与每题强制死胡同；(ii) 摘要与 §4.3 删除或重述"相对无场基线极显著增益"的表述；(iii) 补一组**去除对抗边权**（等权或语义置信度加权）的 GSM8K 图上的 no_deposon 对照。
- 🔴 **Major（M4）：全部判定阈值与绑定参数在测试分布上手调，无 held-out、无敏感性扫描。** 路径命运阈值（$\max R>0.7$ / $\max A>0.5$ / score>0.1）、类型绑定（trap $g_{\text{couple}}=5.0$ vs 其余 0.05–0.3）、度数修正 0.02、BFS top-8/候选上限 30——全部只在 seed=42 的同一 200 题上出现一次；100% 饱和下 trap 节点 $R=0.839$ vs 阈值 0.7（Table 7）的余量恰好在测试集上"够用"，审稿人无法区分泛化能力与 design-on-test。→ 建议：(i) dev/test 分离（seed=42 调参、seed 43+ 只测）；(ii) 阈值敏感性表（R 阈值 × score 阈值 × 绑定强度的 plateau 宽度）；(iii) 至少做粗网格 $\eta$ 扫描——这是统一命题自己声明的最直接可检验推论。
- 🟡 **Minor（M5）："确定性评测"混淆了"缓存可复现"与"管线稳定"。** 零方差来自 100% 缓存命中（1678 次命中、0 次 API 调用，§4.5）；概念分解只做过一次（单一模型标识、单一日期）。→ 建议 ≥3 次独立分解运行（升温或关缓存），报告准确率与图结构变异。
- 🟡 **Minor（M6）："实验前承诺"缺可验证的预注册指针**（带哈希的提交/tag）；GSM8K 子集为 seed=42 单次抽样 100 题、无分层，CoT 97% 高于文献典型值，子集偏易的可能性未讨论；§4.7 的 E1–E4 每臂仅 1–2 次 HTTP 调用，"最强形式的支持"（E4 单次弃权）超出单次观察所能支撑的强度。→ 预注册存档；补子集难度分布对比；E 组对照每臂 ≥3–5 次独立调用。

---

## 3. 结果（Results）

**评分**：**5 / 10**

**优点：**
- 报告完整度高：分层准确率（Table 4/B1）、按步数分层（Table 11）、物理审计（Table 5）、配对统计（附录 D.4）一应俱全；预注册预言被证伪后如实报告（Table 11 与 §5.1），这在投稿中罕见。
- 敏感性口径与主口径严格区分，v1.7.1/v1.8 不回溯改写既有结论的纪律值得肯定。
- 负面结果（G2 集成、G3 势垒、v1.2 零效应、验证层误报）全部在正文给出机制归因而非一笔带过。

**问题与建议：**

- 🔴 **Major（R1）：GSM8K 主口径保留了一个已识别、已修复的 fold_chain 缺陷，把修复后的口径降为"事后敏感性"——"双面性"叙事部分是自己造成的。** §4.2 报告主口径 unified 85.0%（CoT 显著更优，$p=4.9\times10^{-4}$），而以分解器 computed_answer 修复 fold_chain 反向操作数缺陷后 unified 94.0%（$p=0.25$，不再显著）。常规做法是：识别出 pipeline bug 后，以**修复后的管线**为主结果、带 bug 的作为消融/历史记录；本文反向选择，使"约束层在真实任务付出 12 个百分点代价"的头条结论里混入了约 9 个百分点的**已定位工程缺陷**。失败归因（15 例中 10 例 fold_chain）恰好说明代价的大头不在"约束"而在"折叠器"。→ 必须修改：主/敏感性口径对调或并列头条（"修复后 94.0%，与 CoT 无显著差异；遗留缺陷口径 85.0%"），并重写 §4.2 解读、摘要与 §5.1 中"信息损失代价主导"的强度——分解（decomposer_error 3 例）与约束层本身（trap_capture 2 例）的代价才是约束-保真权衡的干净度量。
- 🟡 **Minor（R2）：Table 13 声称"六臂/six-arm"但表中只有 5 行**（field_guided、random、degree、llm_prior、hybrid；CN L352–360、EN L349–357），正文亦称"hybrid 在 overall 上为六臂最高"。→ 补第六臂行或改"五臂"；若第六臂是 v1.7.1 的 hybrid_norm，应在表中显式列出。
- 🟡 **Minor（R3）：两处结果缺机制解释。** (i) StrategyQA 上 v1_blocking=high_couple=unified=89.9% 三变体同分（Table 12）——约束层在该任务上未产生任何差异动作，这一"约束层惰性"现象未讨论；(ii) v2_tunneling 在 GSM8K 崩至 4.0%、StrategyQA 20.2%，失败归因只覆盖 unified 的 15 例，v2 的崩溃机制（全部误判 tunneling？折叠器输入为空？）未解释。→ 各补一段归因。
- 🟡 **Minor（R4）：验证层数字的叙事可对齐。** §4.5 报告验证层在合成集误报 14%/22%，§4.2 报告 GSM8K validate 层与金标准一致率 97%、§4.3 validate-v2 91.9%——三个数字并存但关系（不同 prompt？不同任务？）未说明，读者易误读为互相矛盾。→ 加一句口径说明。

---

## 4. 写作（Writing）

**评分**：**3.5 / 10**

**优点：**
- 章节骨架完整合规：漏斗型引言、按主题组织且逐段差异化的相关工作、先形式化后实现的方法章、贡献列表与路线图俱全（详见附加检查单 A 的逐项核对）。
- 术语大体一致：五变体名、$(g_{\text{couple}}, g_{\text{aether}})$、$T/R/A$ 等符号体系全文统一；"诚实声明/局限"等元信息有固定位置（§5.2 三类局限的分类法清晰）。
- 英文主体为流畅的学术英语，长句多但语法错误率低（抽查详见附加检查单 B，仅检出少量硬错误）。

**问题与建议：**

- 🔴 **Major（W1）：双语摘要严重超长且信息过载，不达任何目标 venue 的形式要求。** EN 摘要实测 **604 词**（规范 150–300 词），CN 摘要约 **1440 字**（规范约 300–500 字），均为单段落，塞入 15+ 个数字、6 组实验（合成、GSM8K、StrategyQA、label-shuffle、labelfree、共振激活）外加判读框架与局限声明。摘要目前是一篇微型论文而非摘要。→ 压缩至 EN ≤250 词 / CN ≤400 字：保留问题、方法一句话、合成主结果一组数字、GSM8K/StrategyQA 各一组数字、一句定界声明；label-shuffle/labelfree/共振/判读框架等细节全部移回正文。
- 🔴 **Major（W2）：文体是"变更日志 + 评审应答"，不是独立自洽的论文。** 正文贯穿 v1.2→v1.3→v1.3.1→v1.4→v1.5→v1.5.1→v1.6→v1.7.1→v1.8.1 的版本考古（§4.1、§4.6、§4.7、附录 C 表 C1），并多处直接应答匿名评审："该绑定回应了'物理映射是否仅为装饰'的质疑"（CN L99）、"我们因此承认评审的'反向设计'质疑成立"（CN L196）、"我们明确写出这一点，以免读者高估共振机制当前的作用"（CN L71）。元信息块还残留"目标 venue 候选""[email to be added]"等投稿占位（CN L5–8）。论文应当呈现一个方法及其证据，而非其开发史与答辩记录。→ 结构性改写：版本沿革整体移入附录（保留 Table C1 即可），正文以"当前系统 + 关键设计决策的理由"重述；删除所有指向"评审/质疑"的元叙述，把对应的实质内容（诱饵基线定性、绑定启发式）改写为论文一阶论述；移除投稿元信息块。
- 🔴 **Major（W3）：§4.7 及附录 D.4–D.6 体量与证据强度不匹配，主线被第二篇"论文"挤占。** §4.7（含 v1.5 死锁、v1.5.1 修复、v1.6 六臂、v1.7.1 融合修复、v1.8 E1–E4）加附录 D 合计约 7800 字符、占全文约 14%（程序化核验，EN 版同比例 14.5%），是单一实验小节中篇幅最大者之一，但其最强结论是"方向性、限定性、统计上不显著"（附录 D.4 自认）。扩散原型与主贡献（推理路径约束层）的关系仅是"同一场公式的生成版"，对主线主张（防捕获/可审计）没有支撑作用；且该节是版本考古文体（W2）最密集的区域。→ 二选一：(i) §4.7 压缩为半页"生成方向初步探索"，细节全部入附录；(ii) 拆分为独立短文。主文篇幅让位于 M1/M2 要求的决定性对照。
- 🔴 **Major（W4）：图表编号与排版规范系统性失守。** 程序化核验首引顺序：**Table 5 首现于 §4.4（CN L301/EN L298）、Table 9 首现于 §4.6，均在 Table 10–12（§4.2/§4.3）之后**；Table 7 在 §3.1 被前向引用（CN L71）；Table 2/3 在引言即被引用（可接受但需注意）。表格编号应按首次引用顺序编排。此外：CN 版全文用英文标签 "Table/Fig."（"Table" 出现 50 次、"表 N" 0 次）；CN Table 1 上方残留编辑批注**"（表上方为表题）"**（CN L137）；唯一的插图 Fig.1 的 CN 图题仅一行、非自含（EN 图题自含）。→ 全文重排表格编号；CN 版统一为"表 N/图 N"；删除编辑批注；补齐 CN 图题。
- 🟡 **Minor（W5）：符号 $T$ 一名二义。** 式 (2) 中 $T$ 为透射率，§3.1 参数域声明与 §4.6 中 $T$ 为温度（$T\in(0,\infty)$、$T=0.3$、$T\to0$），两处同现于 §4.6 的 Boltzmann 公式 $p_i\propto e^{(w_i-b_i)/T}$ 与透射率讨论中，极易混淆。→ 温度改用 $\tau$ 或 $\Theta$。另：TV（§4.7/附录，全变差）未定义；N_NEG、prompt_sha256、run_g2_ensemble.py 等代码标识符大量进入正文叙述，建议首次出现处说明或移入脚注。
- 🟡 **Minor（W6）：排版细节。** CN 版引号三种体系混用（直引号 `"…"` 实测 198 处、「…」5 对），应统一为中文弯引号"…"；变体名拼写不一（摘要 "no-Deposon" vs 正文 "no_deposon"，EN L11/L25 vs L138 等）；EN 参考文献压缩为单段占位并指向 references.bib（EN L419–421），需按 venue 正式排版；EN 摘要 "p=1.8e-16" 与全文 "$\times10^{-16}$" 数学格式不一。
- 🟡 **Minor（W7）：EN 版存在若干语法/用词硬伤（12 处，详见附加检查单 B）**，包括贡献 C4 句末多一个右括号、结论段同一短语重复两次、摘要名词性残句等——单看每处都是小问题，但出现在摘要/贡献列表/结论这三个审稿人必读位置，必须修复。
- 🟡 **Minor（W8）：CN 版有持续的 AI 腔/翻译腔/口语混杂（8 处，详见附加检查单 C）**："如实/诚实"全文合计 37 次的自我标榜、"这构成……的全部内容"等直译句式、"避坑""有光但色不准"等口语金句，以及全文 95 处"——"的破折号依赖。

---

## 修改优先级清单

| 优先级 | 维度 | 类型 | 修改内容 |
|--------|------|------|----------|
| 1 | 方法论/结果 | Major | 补两组决定性对照：rule-based 标签过滤基线（M1）、合成基准直接 CoT（M2）；按自订标准披露并重述 GSM8K/StrategyQA 的诱饵边权构造与 no_deposon 对比（M3） |
| 2 | 结果 | Major | GSM8K 主口径与敏感性口径对调或并列头条，以修复后 fold_chain 管线为主（R1），相应重写摘要/§4.2/§5.1 的代价叙事 |
| 3 | 原创性 | Major | 贡献重新定位：降级"统一极限命题"为参数化设计或补 $\eta$ 扫描等非平凡预测（O1）；补"不可逆性产生收益"的实验，否则全文不可逆耗散主张降格（O2） |
| 4 | 写作 | Major | 摘要压缩至规范长度（EN ≤250 词 / CN ≤400 字）（W1） |
| 5 | 写作 | Major | 去版本考古与应答评审文体，版本沿革移附录，删元信息块（W2）；§4.7 压缩为半页或拆分（W3） |
| 6 | 方法论 | Major | dev/test 分离 + 阈值/绑定/$\eta$ 敏感性扫描（M4） |
| 7 | 写作 | Major | 表格编号重排、CN 版"表/图"标签、删编辑批注、补齐图题（W4） |
| 8 | 写作 | Minor | EN 12 处语法/用词修复 + CN 8 处 humanizer 修复（检查单 B/C）；符号 $T$ 改名；引号统一（W5–W8） |
| 9 | 结果 | Minor | Table 13 "六臂"vs 5 行（R2）；StrategyQA 三变体同分与 v2 崩溃的归因（R3） |
| 10 | 方法论 | Minor | ≥3 次独立分解运行（M5）；预注册指针与子集难度刻画（M6）；验证层口径说明（R4） |
| 11 | 原创性 | Minor | "可逆复活"措辞精确化（O3）；GSM-Symbolic 设置级对比与相邻文献补齐（O4）；C2 中 0.2 ms 工程注记降级（O5） |

---

## 给作者的整体建议

这篇论文最稀缺的资产是它的**科学诚实**：根因分析、负面结果、预登记 SPEC、配对统计、明确的贡献定界——这些是审稿人愿意花力气救一篇论文的理由。但目前这份诚实主要服务于"记录开发过程"，还没有转化为"支撑核心主张的证据"。建议的改稿策略分三步：第一步是**补证据**（优先级 1–3）：标签过滤基线与直接 CoT 两个对照将决定物理层的因果贡献到底剩多少，无论结果如何，论文都应以那个结果为准重新定位价值命题——如果散射层的价值是"可审计表征"而非"准确率筛选"，这本身仍是有意义的贡献，且与本文的诚实叙事自洽。第二步是**修叙事**（优先级 4–6）：把 GSM8K 的"代价"限定在分解/折叠上游、把不可逆耗散的主张限定在有实验支撑的范围、摘要瘦身、删除开发史与答辩腔——当前版本读起来像项目 CHANGELOG 与 rebuttal 的合订本，而目标读者是第一次接触 Deposon 的审稿人。第三步是**过形式关**（优先级 7–8）：编号、符号、引号、双语对齐，这些都是低成本但会触发 desk-reject 印象分的项目。

若三步完成，本文适合的去处是：以"可审计约束层 + 消融设计方法论 + 双向判读框架"为卖点的 workshop/Findings 级投稿；若补齐不可逆性收益实验与决定性对照后证据转强，再考虑主会。目前版本直接投主会，预计会因 O1/O2（主张-证据错位）与 M1–M3（关键对照缺失）被拒。

---
---

# 附加检查单结果

## A. sci-paper-cn 投稿前 Quick Checklist（逐项）

| # | 检查项 | 判定 | 证据与说明 |
|---|--------|------|-----------|
| A1 | 标题：简洁、具体、无冗余术语 | ✅ PASS | CN 主标题"面向可审计大语言模型推理路径选择的物理约束散射层"具体达意；EN 对应。但 CN 版同时排印中英双题（L1–3），正式投稿应只保留投稿语种。 |
| A2 | 摘要：含背景、问题、方法、关键结果、意义 | ❌ FAIL | 五要素俱全但**严重超长**：EN 实测 604 词（规范 150–300）、CN 约 1440 字；单段落含 15+ 数字与 6 组实验。要素过饱和等于结构失守。 |
| A3 | 引言：领域→子域→缺口→贡献列表→路线图 | ✅ PASS | 标准漏斗：第 1 段领域现状 → 第 2 段三类结构性缺口 → 第 3 段物理直觉 → 第 4 段方法 → 第 5 段结果预览 → 贡献 C1–C4 → 路线图。 |
| A4 | 相关工作：按主题组织、显式差异化 | ✅ PASS | 四条主题脉络 (a)–(d)，每条末尾"**Deposon 的定位**"显式差异化，末有小结；非按文献罗列。为全文最强章节。 |
| A5 | 图表：引用先于出现、编号顺序、图题在下、表题在上、图题自含 | ❌ FAIL | **编号乱序**（程序化核验）：Table 5 首现 §4.4、Table 9 首现 §4.6，均在 Table 10–12 之后；Table 7 在 §3.1 前向引用。表题在上 ✅。CN 版残留编辑批注"（表上方为表题）"（L137）；唯一插图 Fig.1 的 CN 图题仅一行非自含（L93），EN 图题自含（L90）。 |
| A6 | 公式：顺序编号、符号周边定义 | △ 部分 | (1)–(6) 顺序编号 ✅；多数符号首现定义 ✅。但 $T$ 一名二义（透射率 vs 温度，见 W5）；TV 未定义；$\eta$ 在 §3.1（比值）与 §5.3（MZI 分束比）含义不同但同形——虽 §5.3 有局部定义，建议改名。 |
| A7 | 参考文献：[1]–[N] 完整编号 | △ 部分 | 程序化核验：[1]–[37] 在两版正文中**全部被引用**，无遗漏无悬空 ✅；CN 全著录 ✅。但 EN 版参考文献压缩为单段占位、注明"see references.bib"（L419–421），非可投稿形态。 |
| A8 | 方法：数学形式化先于实现；小节齐全 | ✅ PASS | §3.1 形式化 → §3.2 系统 → §3.3 理论 → §3.4 设计；§4 各小节数据集/指标/基线/消融齐全。 |
| A9 | 篇幅：匹配目标 venue | ❌ FAIL | 全文约 1.9 万汉字（CN，总 5.6 万字符）/1.67 万词（EN）级 Markdown，远超双栏 8–9 页正文容量；其中 §4.7+附录 D 占约 14% 且服务于非显著结果（见 W3），主线实验（§4.2/§4.3）反而各自只有一页量级。 |

## B. research-paper-refiner 五维规则：EN 版抽查（摘要、§1、§4.7、§5）

**五维评级（抽样段落整体）：**

| 维度 | 评级 | 主要问题 |
|------|------|---------|
| 语法 Grammar | △ 需改进 | 贡献 C4 句末多余右括号；摘要名词性残句；个别省略主谓的残句（"replaced honestly"） |
| 用词 Word Choice | △ 需改进 | 口语/非惯用词：essentially for free、checkable、suspicious、pay off、one-sided good news、avoid the pits |
| 语态 Voice & Tense | ✓ 良好 | 主被动选择合理（"We present... / Equation (3) was checked..."），时态按章节基本合规 |
| 逻辑衔接 Coherence | △ 需改进 | 摘要信息堆叠无层次；§4.7 六臂叙述与表格行数矛盾；deposition 定义句物理主语错位 |
| 句式 Sentence Structure | △ 需改进 | 名词堆砌（thermodynamic-limit idealization of...）；40+ 词长句在 §4.7 密集；破折号插入语过载（EN 全文 187 处"—"，摘要单段 9 处） |

**逐句修改（12 处，原句 → 修改 → 原因）：**

1. **原句**（§1 贡献 C4，EN L32）："...on a real GSM8K subset ($n=100$, seed=42) and a StrategyQA subset ($n=99$, seed=42); results are reported in Secs. 4.2–4.3)."
   **修改**：删去句末多余的 ")"，作 "...results are reported in Secs. 4.2–4.3."
   **原因**：标点规则——未配对括号；出现在贡献列表中，审稿人必读位置。

2. **原句**（§6，EN L415）："Long term: ... transfer to trap-dense/long-chain tasks such as long-document understanding and other trap-dense/long-chain tasks."
   **修改**："...transfer to trap-dense, long-chain tasks such as long-document understanding."
   **原因**：冗余精简规则——同一短语重复两次，且 "other" 无所指；CN 版对应句（L414）无此重复，系 EN 改写引入。

3. **原句**（摘要，EN L11）："Final results (primary protocol, pre-committed before the experiment): on the real GSM8K subset, CoT reaches 97.0% and Deposon-unified 85.0% (...)."
   **修改**："In the final evaluation (primary protocol, pre-committed), CoT reaches 97.0% and Deposon-unified 85.0% on the real GSM8K subset (...)."
   **原因**：语法规则——"名词短语 + 冒号"构成无动词残句（sentence fragment）；"pre-committed before the experiment" 冗余（pre- 已含时间义）。

4. **原句**（摘要，EN L11）："...while retaining a highly significant gain over the no-field baseline (p=1.8e-16)."
   **修改**："...($p=1.8\times10^{-16}$)."
   **原因**：术语/格式一致性——全文其余处均为 $\times10^{-16}$ 数学格式（如 $p=4.9\times10^{-4}$），此处纯文本 "1.8e-16" 不统一。

5. **原句**（摘要，EN L11）："...raises accuracy from 7% (simple) and 10% (trap) for the greedy no-Deposon baseline to 100% on both sets..."
   **修改**："...for the greedy no_deposon baseline..."（与全文变体名统一）
   **原因**：术语一致性——变体名在正文/表格中为 `no_deposon`（L138 等），摘要两处作 "no-Deposon"（L11、L25）；专有命名拼写必须全文一致。

6. **原句**（§1，EN L21）："Our position is that such intrinsic properties of physical systems ... are not decorative metaphors but structural constraints that can be built directly into an algorithm's cost and conservation structure, essentially for free."
   **修改**："...are not decorative metaphors but structural constraints that can be embedded directly in the algorithm's cost and conservation structure at no additional computational cost."
   **原因**：用词学术化——"essentially for free" 口语化且带含糊限定词 essentially；"built into"→"embedded in" 搭配更正式。

7. **原句**（§1，EN L23）："We formalize this intuition as Deposon, named after deposition: the phase transition in which energy passes directly from a gaseous to a solid phase, dispersing irreversibly into an (idealized) infinite-dimensional orthogonal reservoir."
   **修改**："...named after deposition: the phase transition in which a substance passes directly from the gaseous to the solid phase, releasing energy that disperses irreversibly into an idealized infinite-dimensional reservoir."
   **原因**：用词精确性 + 悬垂修饰——发生相变的是物质而非能量；原句 "dispersing" 的逻辑主语被误挂到 energy 上，修改后两层主语各自归位。

8. **原句**（§1，EN L21）："...once energy dissipates into an environment in the thermodynamic-limit idealization of infinitely many degrees of freedom, the Poincaré recurrence time diverges..."
   **修改**："...once energy dissipates into an idealized environment with infinitely many degrees of freedom (the thermodynamic limit), ..."
   **原因**：句式规则——"in the thermodynamic-limit idealization of infinitely many degrees of freedom" 为多层名词修饰堆叠（名词堆砌），改为主干 + 同位语。

9. **原句**（§4.1，EN L154）："...with the BFS neighbor truncation set to 4, decoy branches were absent from the candidate path set, leaving Deposon no trap to block and letting the baseline "naturally" avoid the pits."
   **修改**："...leaving Deposon no trap to block and allowing the baseline to avoid the traps by construction."
   **原因**：用词——"avoid the pits" 非英语惯用搭配（陷阱喻应作 traps）；引号强调 "naturally" 多余，"by construction" 更精确。

10. **原句**（§4.7，EN L345）："This subsection turns the roadmap outlook of Sec. 5.4 into a checkable prototype experiment."
    **修改**："...into a verifiable prototype experiment."
    **原因**：用词学术化——"checkable" 非学术惯用词；verifiable/reproducible 贴合"可复核"义。

11. **原句**（§4.7，EN L363）："Targeting the weak discrimination in D.4 and the suspicious λ-invariance, these supplementary experiments change only scoring-time fusion and null controls..."
    **修改**："To address the weak discriminative power reported in Appendix D.4 and the unexpected λ-invariance, these supplementary experiments modify only scoring-time fusion and null controls..."
    **原因**：用词精确——"suspicious" 拟人化且带主观色彩；句首 "Targeting" 动名词作目的状语欠正式，改不定式；"discrimination" 在此语境易误读，用 "discriminative power"。

12. **原句**（§5.1，EN L375）："This two-sidedness — anti-capture gains versus information-loss costs — constitutes the complete scientific profile of an "auditable constraint layer," which we consider more valuable for research than one-sided good news."
    **修改**："This duality — anti-capture gains versus information-loss costs — is, in our view, more informative than reporting only positive outcomes."
    **原因**：用词学术化 + 删除金句——"two-sidedness" 生硬名词化（→ duality）；"complete scientific profile""one-sided good news" 为宣传式表述；自我评判 "more valuable" 应弱化为 "more informative"。

（另备查：§5.2 L385 "the original one-off script was lost and its recorded numbers could not be reproduced — replaced honestly" 中 "replaced honestly" 为省略主谓的残句，宜改为 "so we replaced them with the re-implemented results"；§4.6 L341/L385 "may pay off only on unsaturated or harder tasks" 中 "pay off" 口语，宜作 "may yield gains only on..."。）

## C. humanizer-zh：CN 版抽查（对应段落）

**总体诊断**：CN 版的 AI 痕迹集中在四类——(i) **破折号依赖**（全文 "——" 实测 95 处，586 行文本密度过高，模式 13）；(ii) **自我标榜的拐杖词**（"如实"27 次 + "诚实"10 次 = 37 次，分布于各节，核心规则 1）；(iii) **否定式排比与金句**（"不是 X 而是 Y/而非 Y" 高频，"完整科学画像""单向度的报喜""有光但色不准"，模式 9 与核心规则 5）；(iv) **翻译腔句式**（"这构成……的全部内容""免费的""兑现为……结局"，模式 8）。另混入口语词（"避坑"）与三类引号体系（直引号 198 处、「」5 对）。

**逐句修改（8 处，原句 → 修改 → 原因）：**

1. **原句**（摘要，CN L12）："本文提出 Deposon（凝子）——一个将 LLM 概念分解图映射为凝子态集合、并以三通道散射（透射 / 反射 / 不可逆耗散）对推理路径施加物理约束的增强层。"
   **修改**："本文提出 Deposon（凝子）增强层：先将 LLM 概念分解图映射为凝子态集合，再以透射、反射、不可逆耗散三通道散射对推理路径施加物理约束。"
   **原因**：模式 13（破折号过度）+ 翻译式长定语——"一个将……并以……的增强层"为英文关系从句的直译结构，拆为两个动宾短句合中文节奏。

2. **原句**（摘要及全文）："如实报告、不作粉饰"／"如实披露"／"诚实声明"（"如实"27 次、"诚实"10 次）
   **修改**：在 §4 开头声明一次原则（如"本节报告全部结果，含负面结果"），其后各处直接陈述事实，删除重复标榜。
   **原因**：核心规则 1（删除填充短语/拐杖词）——同一修辞每节复现形成"诚信表演"的逆反效果；事实本身（负面结果、根因）已足够证明诚实，无需 37 次自证。

3. **原句**（§1，CN L22）："我们主张：物理系统的这类固有特性——不可逆耗散、共振增强、幺正约束——不是装饰性隐喻，而是可以直接内建于算法代价与守恒结构中的"免费的"结构性约束。"
   **修改**："我们认为，物理系统的这类固有特性（不可逆耗散、共振增强、幺正约束）可以直接写进算法的代价与守恒结构，无需额外代价，并非装饰性隐喻。"
   **原因**：模式 9（否定式排比"不是……而是……"全文高频）+ 模式 13（双破折号插入改括号）+ 翻译腔（"免费的"系 "for free" 直译）。

4. **原句**（§3.1，CN L63）："v1 与 v2 因而不是两种机制，而是同一 Deposon 实体在参数空间两个边界上的极限态；这构成"统一极限"命题的全部内容，其可检验推论是：……"
   **修改**："v1 与 v2 因此是同一 Deposon 实体在参数空间两个边界上的极限态，而非两种机制。"统一极限"命题的内容仅止于此；其可检验推论是：……"
   **原因**：模式 8（系动词回避的翻译腔）——"这构成……的全部内容"系 "this constitutes the entire content of" 直译；"仅止于此"兼收弱化主张之效（呼应 O1）。

5. **原句**（摘要 L12 与 §5.1 L378）："防捕获增益与信息损失代价共同构成可审计约束层的完整科学画像，比单向度的报喜更有研究价值。"
   **修改**："防捕获增益与信息损失代价都是评估可审计约束层必须同时报告的结果。"
   **原因**：核心规则 5（删除金句）+ 模式 1（夸大意义）——"完整科学画像""单向度的报喜"为可引用式修辞；价值评判（"更有研究价值"）应留给读者。

6. **原句**（§4.7，CN L362）："语义先验"有光但色不准"，深度融合仍待解决。"
   **修改**："语义先验提供了有效信号但主干方向错误，深度融合仍待解决。"
   **原因**：模式 4（宣传式/口语化比喻）+ 信息冗余——"有光但色不准"为口语金句，且与前句"主干方向与真实结构相反"重复，可直删。

7. **原句**（§4.1，CN L157）："……Deposon 无陷阱可挡，基线也因此"自然避坑"。"
   **修改**："……Deposon 无陷阱可挡，基线也就不会触发陷阱。"
   **原因**：语域——"避坑"为网络口语，与全文学术语体冲突；引号强调多余。

8. **原句**（§4.1，CN L209）："值得点明的是，uniform-params 与 no_deposon 在两个基准上数值重合（7%/7%、10%/10%）——机制为：……"
   **修改**："uniform-params 与 no_deposon 在两个基准上数值重合（7%/7%、10%/10%）。其机制为：……"
   **原因**：核心规则 1（填充短语）——"值得点明的是"系 "it is worth noting" 类引导语；破折号改句号断句。

（另备查：§4.1 L196 "我们因此承认评审的"反向设计"质疑成立"、§3.2 L99 "该绑定回应了'物理映射是否仅为装饰'的质疑"——此类"应答评审"元叙述不属于 humanizer 范畴但属文体问题，已在 W2 中作为 Major 处理。）

## D. 中英对等性检查（摘要 + §4.7）

**D.1 摘要（Abstract ↔ 摘要）**：数值与主张**逐项比对全部一致**——7%/10%→100%、+0.93/+0.90、六类 100%、$2.2\times10^{-16}$、GSM8K 97.0%/85.0%（$p=4.9\times10^{-4}$）、StrategyQA 89.9%/92.9%（$p=0.549$、$p=1.8\times10^{-16}$）、label-shuffle 17.2%±6.4%、uniform-params 10%、诱饵边权 0.9/0.6、labelfree 25/25、双向判读框架。但存在 **4 处信息差**：

| # | 差异 | 位置 | 处理建议 |
|---|------|------|---------|
| D1-a | EN 多"极限态耗散率 0%/86.92%/8.63% 与理论预言一致"一句 | EN L11；CN 摘要无 | 压缩摘要时两版同步取舍，建议删（细节归正文） |
| D1-b | EN 给出 StrategyQA 的 n=99，CN 摘要未给 n | EN L11 vs CN L12 | 补齐或同步删除 |
| D1-c | EN 末句"verifier false positives ... first-class part of the contribution" CN 无对应 | EN L11 末句 | 同步删除或 CN 补译 |
| D1-d | 关键词 CN 6 个 / EN 7 个（EN 多 auditability） | CN L14 vs EN L13 | 统一关键词集合 |

**D.2 §4.7（脑图补全）**：全部数值对齐——Table 13 五行数字、hybrid_norm@2 的 0.471(8/17)、fixed_sampler 的 0.286/0.388/0.327、E1 Pearson=0.724、E3 Jaccard=0.692 与 13/9/100%、E4 弃权、HTTP 尝试次数（E1=1/E2=1/E3=2/E4≤2）均一致；结构差异仅一处：CN 引"§5.3"、EN 引"Sec. 5.4"（因 EN 版多出 §5.3 Ethics statement，CN 版无伦理节），各自内部自洽。**1 处表述质量差**：CN"在候选负边……中把真实边排入 top-3"清晰，EN"rank the true edge into the top-3 among candidate negative edges"有歧义（真实边不是负边，应改 "rank the true edge among the top 3 of the candidate set (1 true + 10 negatives)"）。**1 处共同缺陷**（非翻译偏差）：两版 Table 13 均称"六臂/six-arm"但仅 5 行（见 R2）。

**D.3 抽查中发现的其他不对等（附加，超出委托范围但建议一并修）**：(i) EN §2(a) 多 GSM-Symbolic 65pp 退化一句，CN §2(a) 无；(ii) EN §1 多 "formal mapping with an explicit mathematical boundary" 声明句，CN §1 无；(iii) EN 贡献 C4 含 StrategyQA 子集，CN C4 仅 GSM8K；(iv) EN §1 路线图写 "limitations, ethics, and a hardware-isomorphism outlook"，CN 写"局限与硬件同构展望"（与两版 §5 结构差异对应）；(v) EN §3.1 多 "(T,R,A) 为经典概率权重、不主张量子相干性"的边界声明，CN 对应处无。

---

## 附：与独立评审 A 的关系说明

本评审独立完成于对双语全文、技能清单与部分源码的核验。在方法论维度，本评审的 M3（真实基准沿用对抗性诱饵边权且未按自订标准重述）与评审 A 的 M1 结论一致，且本评审已**独立复核代码证据**（`deposon_agents_v1_4.py` L848/855/862 正确边 0.6、L890 陷阱边 0.9、L908 顺序陷阱 0.85、L916 每题强制 Trap_DeadEnd 0.8、L1582 注释"no_deposon 变体因此被诱饵捕获"），两位评审结论收敛，该项应视为最高优先级的共识问题。本评审的新增价值主要在：写作维度的 4 条 Major（摘要体量、变更日志/应答文体、§4.7 失衡、图表编号）与全部语言层面的具体修改例（检查单 B/C）、中英对等性核对（检查单 D）、原创性维度 O2（不可逆耗散零可测收益）与结果维度 R1（主口径保留已修复缺陷）的独立论证。

*（评审 B 报告完）*
