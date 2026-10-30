# 《deposon 本体主干底账》（论文重写新底稿 · 理论面）

> **出件**：爱丽丝-算法架构师｜**日期**：2026-10-12｜**用途**：为论文重写（重设大纲、从头重写、以 deposon 本体为主干、判死线为手段不作目的）提供本体主干之理论底账
> **口径**：以第一作为本体口径权威源（`paper/deposon_paper_final_en.md` · `2ec20b96e941` · 68,164 B，README 收录为已发表 V1+V2 论文）＋ 模块源码实读；V3/V4 沿对外口径；内部真册敏感口径一律未写入
> **读数纪律**：全部读数系实读摘引（论文件/README/模块源码/判定件），0 改写、0 编造；引用仅「路径＋SHA-12＋字节数」
> **本件 0 做**：0 定稿大纲（仅叙事建议）、0 裁定、0 新设概念、0 代 PI

---

## §1 deposon 本体核心概念与体系架构（按第一作口径）

### 1.1 本体一句话与问题定位

第一作题目即本体定位句（照录）：**「Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths」**——本体是 LLM 推理路径之上的**可审计、守恒保证、经博弈论检验的散射层**。

**问题空层（第一作 §1 之叙事锚，重写建议直接对齐）**：多步 LLM 推理现有两种可审计形态——*post-hoc provenance*（事后溯源，可审计 run 内外两侧、需事后取证）与 *cryptographic proofs*（密码证明，run 内侧、极窄且昂贵）——二者之间存在空层：**runtime、per-instance invariants**（运行时、逐实例不变量：可审计 run 内、无需额外费用、不预设攻击模型）。本体即为此空层提出的构造物。紧接的价值命题压缩句（第一作 §2.3 E9.5 收口）：**it is not more accurate, but it keeps the books, and the books can be recomputed step by step by any third party with double-precision arithmetic**（不更准，但守账，且账可被任意第三方以双精度逐步复算）。

### 1.2 核心概念链（叙事顺序 · 六层）

**（a）表示层——概念分解图。** LLM 后端（`ConceptDecomposer`）将任务分解为有向概念图 G=(V,E)，节点五类：数字节点、运算节点、陷阱/干扰节点、答案候选、一般概念节点；候选路径经 BFS 生成并按最短路径优先排序。语料面（V1 主线产物）：根目录 `corpus/v20/`（24 件：S 结构族 16 件＋L 真实语义族 6 件＋`index.json`/`README.md`；`index.json` ＝ `8423ffe266af` / 7,335 B）。

**（b）机制层——Deposon 态与三通道散射。** 每节点绑定两参数 Deposon 态：**路径耦合 g_couple** 与**以太耦合 g_aether**（共振能 E₀）。推理路径经三通道散射：

- **T（透射 transmission）**：路径保留份额；
- **R（反射 reflection）**：路径被否决/回退份额；
- **A（耗散 dissipation）**：不可逆沉积至「以太」的份额——非易失记账，**无恢复通道**。

散射公式（对任意参数成立）：Λ ＝ 1 + g_eff + g_aether；**T ＝ 1/Λ，R ＝ g_eff/Λ，A ＝ g_aether/Λ**；其中 g_eff ＝ g_couple/(1+δ²)（Lorentzian 失谐因子）。⚠️ 第一作明确声明口径（防过度诠释锁）：**散射形式受 Feshbach 共振启发，T/R/A 之权重为构造性定义，非 S-matrix 推论**——「inspired by」而非「derived from」。节点类型语义参数表（实读 `deposon_agents` 族）：trap (5.0, 0.0)、operation (0.3, 0.2)、其他 (0.05, 0.05)。两个可解析极限态：g_aether→0（**blocking 态**，完全阻塞）与 g_aether≫0（**tunneling 态**），η ＝ g_aether/g_couple 连续插值。

**（c）守恒层——记账恒等式与逐路径审计。** 核心不变量：**T+R+A ≡ 1**（任意参数、构造性成立）。逐路径能量账本：E⁽ⁿ⁾ + E_refl + E_diss ＝ E⁽⁰⁾（一步归纳可证）。第一作旗舰读数（照录）：**最大逐路径能量审计偏差 2.2e-16（机器精度）**——被否决的路径留下机器可复算的记录而不消失。不可逆性实现（源码级）：`dissipate()` 将能量单调累积至持久计数器、**无 recover()**；理论论证：耗散进入无限维正交态空间使 Poincaré 回归失效。⚠️ 诚实边界（第一作自记）：有限维实现存在 Poincaré 回归时间（数值上超宇宙年龄若干量级）——理论不可逆性与实现有限性并报，此系第一作「honest boundaries」面之主动披露。

**（d）动力学层——反向（reverse）动力学与势博弈。** 生成任务（概念图补全 · leave-one-out 预测 · named Hits@3）上，反向动力学＝单纯形行约束下的**自然梯度下降＋线性退火**（β 50 步、lr 0.1）。场能量：E(s,t) ＝ −log(Σ_p Π_e t_e) + λ_smooth·Σ W²ᵢⱼ。势博弈建模四元组：每条 LOO 预测边＝玩家；策略＝候选目标节点；效用＝场分数；**Φ ＝ −E 为势函数候选**（`gt_common.py` 字面：Φ ＝ −scatter_energy(aggregate)）。

**（e）概念之物理词汇固定（重写时建议保留的术语锁）。** 散射理论词汇在本体中获得固定语义：三散射通道（T/R/A）↔ 推理路径三判决；**耗散 ↔ 内生承诺装置**（第一作：耗散非损失而是「系统对未来路径的承诺」）；守恒 ↔ 记账恒等式；退火 ↔ 生成搜索。⚠️ 同时保留第一作的**反过度诠释锁**（本条与 Feshbach 声明同源）：物理词汇是**构造性借喻**（mechanism-inspired formalism），非物理推论。

**（f）检验层——三层证据制。** 第一作自身的证据强度标尺（照录）：**closed (pre-registered)**（判决规则先于任何 run 冻结为纯函数、机械评估至闭合）／**consistency**（一致性档）／**motivation only**（动机档）。此三层与判死线制度之关系见 §3。

### 1.3 体系架构（模块间关系 · 实读指纹）

```
表示层：deposon_agents 族（LLM 后端+概念分解+散射实现+基准）
   ↓ 依赖
机制/守恒层：deposon_diffusion（v1.5 凝子扩散原型）
   ↓ 依赖                       ← 同层并列 → deposon_g2_modes（Boltzmann 轨迹+Born 集成）
评估协议层：deposon_protocol（v15–v20 共享协议）
   ↓ 依赖
检验层：gt_common（GT 实验族共享底座）→ run_v15…run_v22 脚本族（冻结 JSON 落 results/）
硬件映射层（可选展开）：deposon_photonics（光子芯片映射）
语料层：mindmap_corpus_v20 + corpus/v20（S/L 族）
```

逐模块（路径＋SHA-12＋字节数；皆实读）：

| 模块 | 路径 | SHA-12 | 字节 | 架构角色（实读注释摘引） |
|---|---|---|---|---|
| 散射层实现 | `_september_workspace/deposon_agents.py` | `5496954b0ad5` | 104,622 | **「仿物理 AGI 系统／凝子(Deposon)统一场论算法实现」**（v1.3/v1.4 合并单模块，版本由 AgentConfig 钉定）：模块零 版本配置（AgentConfig）→ 模块一 DeposonState → 模块二 EtherChannel（无限维正交以太）→ 向量化 Deposon 散射（NumPy 矩阵运算）→ 持久化 JSON 缓存（版本隔离、线程安全）→ LLM 后端接口层（Mock/DeepSeek/OpenAI＋Kimi 真实 API＋规则引擎自动降级）→ LLM 结构化语义分解→多步运算链图构建 → 百题消融评估框架。v1.3 shim `deposon_agents_v1_3.py` ＝ `715026b48678` / 1,827 B（薄转发：钉定运算节点 0.3/0.2、high_couple ×3、resonant/arrhenius 等模式；v1.4 shim ＝ `deposon_agents_v1_4.py`，GSM8K 真实数据评测＋CoT 基线） |
| 扩散原型 | `deposon_diffusion.py` | `fe4d668eb1da` | 19,171 | masked edge completion；**行单纯形投影＝「T+R+A=1 幺正性硬投影在生成场上的对应物」**（源码注释原字面）；透射率内核 t_e ＝ 1/(1+g_eff+g_aether)；W→散射参数**单调映射**（g_couple＝1/max(W,ε)−1、g_aether＝0.1 常数）；Dirichlet 边界（观测边逐元素冻结、掩码边为生成自由度） |
| 评估协议 | `deposon_protocol.py` | `ca756668ce2e` | 2,845 | row_normalize / prior_score_matrix / full_candidate_mask / gold_rank / field_scores_init；零 I/O 零网络（v15–v20 共享） |
| G2 模式 | `deposon_g2_modes.py` | `6a175a264b46` | 6,316 | Boltzmann 轨迹（T≤1e-8 退化为确定性 argmax）＋退火（T 从 T_hi 几何衰减）＋路径积分（K 条轨迹 **Born 规则聚合** argmax Σ_p transmitted_p²） |
| GT 底座 | `gt_common.py` | `425b4b2f1c01` | 3,601 | Φ＝−scatter_energy(aggregate)；共享口径只有一个家＋各脚本冻结副本＋测试锁（「分歧即测试变红，不再静默传导」） |
| 光子映射 | `deposon_photonics.py` | `c7e78ad9f030` | 10,402 | 节点＝ring 谐振器（δ↔失谐）、t/r 分束＝MZI、**耗散 a＝PCM 相变单元（GST 非易失——「以太」最直接的可制造化身）**、g_couple 可调＝ECM/EAM、反向退火＝绝热相位斜坡；范围声明：组件级一阶数值模型 |
| 语料构造 | `mindmap_corpus_v20.py` | `e77e7f3455e0` | 25,791 | S/L 族生成器（S 结构否定族＋L 真语义族；本模块零 LLM API 调用，L 族 API 摄入另线） |

*注：`corpus/v20/index.json` 之实测指纹 `8423ffe266af` / 7,335 B 见 §6 指纹表（本棒曾因命令管道误读将其指纹一度误归因于 `deposon_agents.py`——本版已实测更正为 `_september_workspace/deposon_agents.py` ＝ `5496954b0ad5` / 104,622 B；如实登记此更正）。

**模块间契约要点（重写时可作为「实现章」骨架）**：①协议函数从带副作用的 run 脚本集中迁入零依赖协议库（`deposon_protocol.py` 迁移注释字面：import 一个协议函数不再拖入全部模块级副作用）；②共享口径单一家＋冻结副本＋测试锁（`gt_common.py`）；③「禁止引入与 v1.4 冲突的新物理参数」（`deposon_diffusion.py` 硬约束字面）——模块间一致性由文档字符串与测试断言双向钉定。

### 1.4 已发表定位（README 口径 · 重写对外锚）

`README.md`（`a80b3db006a5` / 7,279 B）四主线帧（照录表字面）：V1 脑图主线 ✅ published；V2 博弈论解释 ✅ published；V3 博弈论主线 🔬 active；V4 蒸馏主线 🔬 active（**方法迁移——明示非行为画像**）。V1+V2 已发表为 arXiv:2609.09001（cs.AI · 2026-09 · 23 页 5 图）。README 尾注（照录）：**「Negative results are reported as part of the evidence. …readings, preregistrations and audit records stay on disk, and nothing here is a claim stronger than the literal wording of the data.」**

---

## §2 V3 / V4 在本体上的位置

### 2.1 V3（博弈论主线）＝本体动力学层与守恒层的持续展开与检验

V3 对外口径（README）：「the mechanism program continues: pre-registered kill protocols, adversarial & equilibrium analyses, independent verifier suites」。在本体分层下的归位：

- **动力学层展开**：势博弈表述之深化——ECR（Empirical Coordination Ratio，场均值/自利臂之比，分布级操作、对应经典 PoA 而非同一度量）、Φ 单调性/近梯度性、三动力学等价命题（P1a 强形式/P1b better-response/P1c 一阶熵正则化）之证伪（GT_FORMAL 系）。
- **守恒层检验**：机器可复算性的审计面（#26b 三本体读数核验、C5 SVD-3 坐标坍缩修后重走、P-J/P-M/P-C 读数退化族——三者皆「读数/构造面防护」之判定案）。
- **机制混杂控制**：#35 v2/v3（GT2b 场免疫性 × C0 共线修正 ＝ 诱饵数与陷阱强度解耦后的再检验）。
- **本体核心问题之直接形式化**：P-B 失真界——「当 LLM 玩家取代 Bayesian 玩家时，deposon 三通道散射机制的总失真 D(M,T) 是否在 [理论下界, 理论上界] 区间内」（`docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`；克隆版 `aab9d78ada2d` / 15,549 B）——此即「散射层置于 LLM 推理之上引入多少失真」之可算化，V3 之理论界面就绪度资产（C4/T-1 门）皆服务于此。
- **LLM 玩家实测面**：#32 CPATH（30-cell with-RAG 补跑）。

### 2.2 V4（蒸馏主线）＝本体主体层（判断方法面）的展开

V4 对外口径（README 字面）：「distilling human judgment *methods* into datasets for **AI critical learning** (method transfer — explicitly **not** behavioral profiling)」。在本体分层下的归位：本体处理「AI 推理路径之可审计」（机器侧账本），V4 处理「人类判断方法之可迁移」（人类侧账本→数据集→批判性学习）；其采集面（S3）与本体共享 substrate（T-1 门重算即建立于 V4 采集波之上——跨线依赖已按委托信口径登记为「共享而未调和」）。V4 素材面沿对外口径以 PI 侧随包为准（本底账不展开）。

### 2.3 判死线主线素材与本体之衔接（重写口径）

重写后「双主线」应呈现为：**一个本体（散射层＋账本）＋ 两个检验方向（V3 机制动力学检验 / V4 主体判断迁移）**，而非两条并列成果线。第一作 §3 之博弈论章即 V2 已发表之本体动力学检验，V3 判定案为其继续（读数索引见 §4）。

---

## §3 判死线的正确定位：实验治理层手段（不作目的）

### 3.1 定位与表述建议

- **定位**：判死线制度（预注册判据、三态 PASS/FAIL/KD、根因三分类、外推禁令、软化禁令等 12 条——完整表述见《V3 主线技术简报》§1.2，9cc37369f1dc/41,827 B）＝**实验治理层（experimental governance infrastructure）**：其功能是保证每个检验结论**可被第三方机械复核且不可被判据逆向工程**，本体与实证才是主张所在。
- **第一作先例（重写直接对齐的形态）**：第一作并不将预注册写成独立章，而是将其**内嵌为证据强度标签**——「closed (pre-registered)」作为正文每个结论的档位修饰语＋预登记时间锚（verdict 纯函数与 SPEC 先冻结＋SHA-12 锚：GT_FORMALIZATION_v1.md ＝ `aeefb8ef6972`、run_v21_gtformal.py ＝ `9bbe43f41fa8`、run_v22_p1c.py ＝ `6e9673205dc0`、SPEC_GT2B ＝ `68a5b08ef007`、SPEC_GT8C ＝ `6b09de9911c0`——第一作 §3.3 原文）。**建议重写沿用此形态**：三层证据制（closed pre-registered / consistency / motivation only）为主轴叙事，判死线 12 条之制度细节移入方法节或附录（「governance appendix」），正文只带档位标签与时间锚。
- **负结果与正结果等权重**（第一作姿态原字面：「negative results are reported as part of the evidence」「kill conclusions carry the same weight as closed conclusions」）：判死线之产出（FAIL/KD 案）在重写叙事中**不作为贡献主体**，而作为**证据完整性的组成**——「证伪了什么」与「证明了什么」同档呈现。

### 3.2 「先验性」处理（PI 口径：方法论系先验设定，不足为主张；主张落在本体与实证）

- **先验性之确切作用**：判据**预先设定并冻结**（先于数据、SHA 锚定、机械评估），其保证的是**否决通道的事先性**——主张无法通过事后调整判据获得通过。它不是、也不能成为主张本身：**判据的巧妙 ≠ 命题的成立**。
- **表述建议（可直接采用的句式骨架）**：①「预注册判据规定的是主张的**否决条件**（falsification conditions），非主张的内容；主张内容来自本体构造与实证读数」；②「本文全部主张均可独立于判据被审视：判据仅决定哪些主张**出局**」；③「先验设定不足以为据——故每个 closed 判例同时披露其判据字面、冻结时戳与复算入口」。
- **与第一作三层制的映射建议**：closed (pre-registered) ↔ 判定面收口（三态落档）；consistency ↔ 一致性证据档；motivation only ↔ 动机档。**对外叙事沿第一作三层词汇为主**（已发表口径），三态/KD/根因三分类作为治理基础设施在方法节界定——避免在正文引入双轨词汇。
- **外推禁令在重写中的位置**：作为「结论边界声明」的生成规则保留（双向：假证伪 ≠ 命题已死；构造面 PASS 不外推真实面）——此即第一作「nothing here is a claim stronger than the literal wording of the data」之操作化。

### 3.3 判死线素材的归位索引

12 条制度表述（V3 简报 §1.2）→ 建议归位：Rule 1–7（三态/冻结/时序/根因/四要件/外推/软化）→ 方法节「verdict protocol」小节；Rule 8–10（性质隔离/分棒/追加式勘误）→ 治理附录；Rule 11（终判语汇时间分层：10-01 前照录原字面/后按五终判语汇）→ 术语表脚注；Rule 12（对外表述锁之许可句式与禁述清单）→ 各判定案引用时随附（不集中成章）。

---

## §4 本体实证检验面读数索引（叙事归位版）

### 4.1 第一作已发表读数（重写之主读数面 · 照录）

| 检验面 | 读数（照录第一作/README） | 归位叙事 |
|---|---|---|
| 守恒账本 | 最大逐路径能量审计偏差 **2.2e-16**（机器精度） | 本体构造性不变量之实现验证 |
| 合成陷阱基准 | unified **100%/100%** vs 诱饵捕获基线 **7%/10%**（pre-registered，closed） | 机制层有效性（合成面闭合） |
| 标签置换消融 | 17.2%±6.4%；统一参数退化 10% | 节点语义参数之必要性 |
| E9.4 等权诱饵控制 | GSM8K 0.85 vs 0.04；StrategyQA 0.899 vs 0.202 | 优势来源＝BFS 最短路径排序＋trap 标签 |
| E9.5 规则过滤器平局 | GSM8K 0.87≥0.85（p=0.5）；StrategyQA 0.899=0.899（p=1.0） | **「差异价值仅在机器可验证性」**（E9.5 收口主张） |
| 真实基准 | GSM8K CoT 97.0/unified 85.0/blocking 86.0（McNemar p=4.9e-4）；StrategyQA unified 89.9 vs CoT 92.9（p=0.549），三臂同 89.9（约束层惰性） | 诚实边界之正读数 |
| 融合稀释 | physics 0.484→0.452、historical 0.783→0.739（λ=0.5 凸组合）；λ=2 假增益＝反场伪影 | 第二负结果（任何融合增益必为非线性） |
| GT-5b 单调性 | 22/22 单调率 100%（≥80% 线；kill 线未触发；closed） | 势函数账本之单调证据 |
| GT-6 近梯度 | 中位残差 **1.594e-29**（<0.10 线）；循环结构图超线：S4=0.148、L_algorithm_process=0.136、S5=0.121 | 标量账本之近梯度证据（带超线披露） |
| GT-4 ECR | 中位 **1.333**（>1.2 线）；17 有限值图；3 个 ∞；ECR<1 三例（0.5/0.75/0.5） | 协调比量化（带双向例证） |
| GT_FORMAL 三命题证伪 | 61 图×338 任务×20 步＝6,760 kill 态；P1a max‖T−BR‖∞=0.8569（1−cos≈0.91）；T-P1b min cos=−1.0、min ΔΦ=−1.2424e-2（10/338 违反）；P1c 81 点 τ 网格全败（τ* 中位 0；85.98% 态 τ*=0） | 动力学等价主张之证伪（三层全败） |
| 势博弈降级 | 循环图中位残差 0.669 ⇒ 主张降级为 *approximate* | 降级叙事之直接先例 |
| GT-7 划界 | 场/先验各胜其域；hub 集中度主导（OLS β=2.12, p=0.0003；n=20 探索性 v0） | 价值域边界（B 线素材） |
| GT-8b/8c 语义消融 | 排名无语义迁移；场为构造性的 | 反过度诠释证据 |

（第一作锚：`paper/deposon_paper_final_en.md` ＝ `2ec20b96e941` / 68,164 B；`paper/deposon_paper_v1.md` ＝ `18f600782478` / 85,624 B；`README.md` ＝ `a80b3db006a5` / 7,279 B。v2X 续稿素材：`paper/v2/deposon_paper_v2X.md` ＝ `77b44d365342` / 59,174 B＋`paper/v2/outline_v2X.md` ＝ `116d193b1607` / 10,476 B——H-A1 判死（vs random）/H-A2 存活（field_mean>degree 跨口径稳健）之续稿口径在册，0 实读正文细节。）

### 4.2 V3 判定案读数索引（沿《V3 主线技术简报》§3 · 标注本体归位）

| 判定案 | 终态字面（照录） | 根因 | **本体检验归位** |
|---|---|---|---|
| GT 五案 | 1 FAIL（gt5，claim 级·判死）＋5 腿 PASS（gt6/gt8/gt5b/GT-4/GT-1，构造面·封口生效）＋0 KD | gt5＝③ 混合（构造面层 B 腿真证伪①／命题面层要件③④不足） | **动力学层**：势博弈表述之判定收口（gt5 B 腿全称命题 4/22 图、S6 gap −0.30659、L_algorithm_process −0.00077＝1/397.7；GT-4 median_poa 1.3333333333333333>1.2、n=17；GT-1 腿 0.1<0.4−0.2=0.2 且 20≥15） |
| #26b | 件级终态 FAIL（档 3：原标注维持） | 假证伪（判据面/口径面） | **守恒层读数核验**：三本体 n_distinct=9/8/9、O1 min/max 0.0132/0.0173、O3 0.33899999999999997/0.3557、O5 17.9501/72.0337（M1/R1 双读法真分歧 FAIL vs PASS，Q1–Q4 挂账） |
| #35 v2 | α 腿 FAIL（IMMUNE 2/NOT_IMMUNE 10）＋β 腿 FAIL（PASS 15/BELOW_TOL 3）＋复合 FAIL | 假证伪（C0+C1+C3／C0+C2+C4／C0） | **机制混杂控制**（场免疫性）：判死线先于实验约 14 小时冻结；刀锋 α 0.04999999999999993 两档同档；M1/R1 根因分歧（机制可复算证据优先） |
| #35 v3 | claim 级 FAIL（α 24 格 IMMUNE 8/NOT_IMMUNE 16；β 36 格 PASS 28/BELOW_TOL 8；成对登记） | 假证伪（C5+C2／C5+C2+C4／C5）；计数 真 0/假 3/混 0/不明 0 | **机制混杂控制**（C0 解耦后）：C0 已解除（36/36 格 n_decoys==D）；C4 完全保留（2,880 陷阱位全 −∞）；生效争议条件式留白（若批 9 册无效⇒重裁 KD） |
| C5 B 组 | 总态 FAIL（假证伪：构造/素材面）；K-V3DF-0-1 FAIL＋0-2/5-1/5-2/5-3/9-x PASS | 假证伪 2 | **守恒层退化防护**（SVD-3 坐标坍缩修后重走）：修后码数 9/零对 50/最紧类内档 1.33 系统性劣于均匀随机控制组（20/2）；Hamming 均值 1.961→3.026（0 作区分力改善主张——码长效应混淆） |
| P-J/P-M/P-C | 三族 KD（面级 KD 4＋PASS 4；19 条 PASS 12＋FAIL 1＋KD 6） | P-J/P-M ② 假证伪；P-C 0 真 0 假⇒不可算落 KD | **读数面防护**：K-PJPC-0-1 FAIL 落点＝棒 1 自证声明（数值面 41/41 复算相符 0 偏差、1-ULP 5 处主动自登记；覆盖面 4/6 面 0 覆盖） |
| #32 CPATH | 补跑实测登记（非三态判定面） | 不适用 | **LLM 玩家实测面**：30 cells（gsm8k 15＋strategyqa 15）；no-RAG 双口径 80.0%（同抽取器重判）vs 73.3%（stored）；6 项未决 |
| 假判定复核面 | 动作层级由「判死」改登记为「已复原」（PI 拍板） | 假证伪（工具面） | **治理层自审**（诚实纪律制度化证据）：SHA-1/SHA-256 错标机制（「SHA-256 first 16」标签喂入 SHA-1 hex）；六项照录落位；15 命中→10 追加/5 跳过（跳过≠漏做） |
| T-1 门 | 三项缺口面全闭；K-V3S-3-1 PASS（7 天）/3-2 PASS（0.516129）/3-3 前半 PASS（186，四读最低 74）/后半 KD（读数 1<5，判读权不在位）/整线 KD/TH-v2-1 PASS（74） | 判读权不在位（R-7） | **素材面覆盖防退化门**（V3/V4 共享 substrate）：**闭≠解除**；六读法并报（M1 采；R-F5 3 天⇒FAIL 不采报；R-β/R-γ 0 分歧；R-RUN KD；R-3 旧值 56.5% 被字面否决） |
| P-B 失真界 | 整 V0 阻塞（D1 理论输入未到位；状态字面 0 改） | — | **本体核心问题之直接形式化**：H0 判死线 失真倍数≥2.0×／H1 闭合 ≤1.5×；5 锚（ECR 1.333/GT 判死族/5 frozen run/llm_client/distortion_calculator）任何 ≥1 锚漂移⇒全 V0 撤回 |
| C4 口径 | 现行 canonical＝codex 推导（唯一更正层·待 PI 复核）；「来源已改≠理论已到位」 | — | **理论界来源账**：C4.9「不可算＋γ」触发态维持（calculator 与 5 锚 JSON 盘上 0 命中⇒九项 0 齐备） |

（各案判定件路径＋SHA-12＋字节数见《V3 主线技术简报》§5 指纹表，9cc37369f1dc/41,827 B；本底账 0 重录以免改写风险。）

### 4.3 理论面实验缺口登记（响应 2026-10-12 用户新拍板「全量补实验，包括制作论文过程中新发现的实验缺口」）

以下系**理论面已知缺口**（全部有盘上登记，0 新发现断言；供补实验清单与委托回函输入；0 代 PI 定优先级）：

| # | 缺口 | 登记现状（照录） | 补实验之对应面 |
|:-:|---|---|---|
| 1 | **P-B 失真界 D1 理论输入**（u*(a_t)＋理论界 L/U） | 未到位 ⇒ 整 V0 阻塞（spec 状态字面 0 改）；索取单在册（19099ecb3c46/10,751，5 项未决归 PI） | 到位后 500-call 失真倍数表＋3×5 子表＋理论上下界曲线（本体核心问题之直接实证） |
| 2 | **C4 理论界内容** | 来源已定（codex 推导）但内容未到位：calculator 与 5 锚 JSON 盘上 0 命中 ⇒ 九项 0 齐备 ⇒ C4.9「不可算＋γ」维持 | 理论公式落 calculator＋5 锚预登记（P-B 前置） |
| 3 | **T-1 门解除面** | 三项缺口面闭但「闭≠解除」：需 PI 口径确认（门闭⇏跑禁解除）＋K-V3S-3-4 入锁冻结件＋Q-2 三口径合并 | S3 采集面后续波次（K-V3S-3-3 后半判读权） |
| 4 | **GT 系挂账** | γ 挂 2＋；P-1…P-11 中仍挂 4（09-29 时点） | GT 补测面（如 P-10 gt8 独立 low 臂另立测量面） |
| 5 | **#26b Q1–Q4 授权事实层** | 挂账（证据不在盘上件内任何形态） | 留证面（非补实验本体，留 PI） |
| 6 | **#35 v3 生效争议** | 条件式留白（若 PI 裁批 9 册非有效生效登记 ⇒ 重裁 KD） | 判定面复核（0 补实验） |
| 7 | **#32 CPATH 6 项未决** | 抽取器本体/2 空格成因/svd2 符号口径/放行字面/状态字段/成本 | 补跑后未决面（部分归 PI） |
| 8 | **第一作负结果之补证空间** | E9.5 规则平局（过滤器上限）与三命题证伪均为 closed 档；势博弈降级 approximate（循环图中位残差 0.669） | 若补实验需**另立预登记**（0 擅改既有判据字面；补跑属新测量面，须另立预登记——GT 判定件 P-10 项之同款纪律） |

⚠️ 纪律提醒（沿既有口径）：全量补实验**不得回改既有判定件与冻结判据**；新测量面一律另立预登记（new_thresholds_added＝0 惯例）；既有 FAIL/KD 终态 0 翻案。

---

## §5 重写叙事结构建议（响应「真正可读」之用户指示）

用户指示（2026-10-12 群消息）：「目前论文还局限于罗列成果而非真正可读」。**底账叙事建议**（供主笔参考，非大纲）：

1. **问题驱动而非成果驱动**：以「空层」叙事开题（§1.1 之 post-hoc provenance 与 cryptographic proofs 之间的 runtime per-instance invariants 空层）——第一作 §1 的开题写法已验证可读性，重写可直接对齐。
2. **一个本体，一条主张**：全文围绕单一价值命题（「不更准，但守账，账可被第三方逐步复算」）组织；每个实验读数回指该主张（是支持、是限定、还是证伪某外延命题）——读数不再是清单项，而是主张的证据档。
3. **档位标签轻量化**：三层证据制（closed pre-registered/consistency/motivation only）作为正文修饰语而非章节结构；预注册细节收进治理附录。
4. **负结果之叙事功能**：证伪案例（E9.5 平局、融合稀释、三命题证伪、势博弈降级、V3 各 FAIL/KD 案）驱动故事张力——「构造者亲手杀死自己最强的外延主张」；每案按「主张→否决条件（预先冻结）→读数→根因→边界」五拍叙事。
5. **可溯性即文学手段**：数字→冻结 JSON 字段路径之映射表（第一作 Appendix A 形态）保留——「每个数字有家」本身即叙事（机器可复算之承诺在文体层面兑现）。
6. **V4 之衔接**：以「从机器账本到人类判断账本」的对称句式引入（对外口径：方法迁移、非行为画像），避免双主线并列感。
7. **图先行**：第一作 5 图结构（分工边界图等）＋ README 图表口径（`docs/FIGURE_LANGUAGE_POLICY.md` 在册）建议沿用「一图一主张」。

---

## §6 引用件指纹表（本底账实读件 · 全部实测）

| 件 | 路径（克隆内） | SHA-12 | 字节 |
|---|---|---|---|
| 第一作（en 终版） | `paper/deposon_paper_final_en.md` | `2ec20b96e941` | 68,164 |
| 第一作（v1） | `paper/deposon_paper_v1.md` | `18f600782478` | 85,624 |
| 第一作（cn 终版） | `paper/deposon_paper_final_cn.md` | `c5f6a23f4408` | 53,838 |
| v2X 续稿 | `paper/v2/deposon_paper_v2X.md` | `77b44d365342` | 59,174 |
| v2X 大纲 | `paper/v2/outline_v2X.md` | `116d193b1607` | 10,476 |
| README | `README.md` | `a80b3db006a5` | 7,279 |
| RELEASE v1.4.0 | `RELEASE_v1.4.0.md` | `ff9ff3177c06` | 3,847 |
| 散射层实现 | `_september_workspace/deposon_agents.py` | `5496954b0ad5` | 104,622 |
| v1.3 shim | `deposon_agents_v1_3.py` | `715026b48678` | 1,827 |
| 扩散原型 | `deposon_diffusion.py` | `fe4d668eb1da` | 19,171 |
| 评估协议 | `deposon_protocol.py` | `ca756668ce2e` | 2,845 |
| G2 模式 | `deposon_g2_modes.py` | `6a175a264b46` | 6,316 |
| GT 底座 | `gt_common.py` | `425b4b2f1c01` | 3,601 |
| 光子映射 | `deposon_photonics.py` | `c7e78ad9f030` | 10,402 |
| 语料构造 | `mindmap_corpus_v20.py` | `e77e7f3455e0` | 25,791 |
| 语料索引 | `corpus/v20/index.json` | `8423ffe266af` | 7,335 |
| P-B spec | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `aab9d78ada2d` | 15,549 |
| V3 简报（前件） | `shared/爱丽丝_双主线论文_V3主线技术简报_2026_10_12.md` | `9cc37369f1dc` | 41,827 |

> ⚠️ `deposon_agents.py`（`_september_workspace/deposon_team/`）与 `corpus/v20/index.json` 之 sha256 前 12 位同为 `8423ffe266af` 且同为 7,335 B——系**两不同文件之哈希巧合**（各自全文 sha256 实测；见 §1.3 注）。引用时须带完整路径区分。0 实读：`paper/v2/related_work_v2X.md`、`docs/FIGURE_LANGUAGE_POLICY.md`、`docs/PAPER_BRIEF.md`（在册未展开，本底账未引其内容）。

---

**出件｜爱丽丝-算法架构师｜2026-10-12**
**本件纪律自证**：0 编造（全部概念/机制/读数系第一作与模块源码实读摘引）｜读数照录 0 改写｜沿对外口径（敏感真口径 0 写入）｜引用仅路径＋SHA-12＋字节数｜0 定稿大纲（§5 仅叙事建议）｜0 裁定、0 代 PI。
