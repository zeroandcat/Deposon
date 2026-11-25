# deposon V3 阶段终稿素材包（蓝图 §8 接口聚焦版）

- 撰写：阿兰-文献调研员 · 2026-09-18
- 任务来源：管理员 03:41 重派（上轮超时，本轮按爱丽丝蓝图 §8 收窄聚焦）
- 接口：蓝图 `shared/爱丽丝_V3阶段终稿大纲蓝图_2026-09-18.md` §3.3（引用分层）/§4.3（DAS 题录）；数字唯一通道＝`shared/鲍勃_deposon_V3终稿数字事实核验包_2026-09-18.md`（本包只供题录与叙事，零数字供给）
- 纪律：挂载仓全程只读（本轮仅 Read/Grep/Glob＋sha256sum 实算）；零编造；核不到标 pending；本轮无新网络检索——全部结论溯源自既有留档（citefix20260916/ 与 das_check/，清单见 §5），题录字段为留档程序化再提取

---

## §1 v9 引用随行清单（61 条全对账：随行 32＋增补候选 5＋覆盖组 24）

对象：`shared/dave-survey2-arxiv-20260915/keep_the_books_arxiv_2026_09_16_v9/keep_the_books_survey.tex`（61 条 bibitem 实数复核 ✓）。分层按蓝图 §3.3。

### 1.1 a 组·必随行直引（32 条，落在蓝图预估带 25–35 内）

**L4 博弈论审计线全量（9 条，V3 转向近邻，均无 pending）**

| key | 题录（沿 v9） | pending 状态 |
|---|---|---|
| key43 | Ball & Kattwinkel. Probabilistic Verification in Mechanism Design. Theoretical Economics 20(4):1247–1284, 2025. DOI 10.3982/TE6266 | — |
| key44 | Pardasani & Singh. Who Verifies the Benchmark? Decentralizing Trust in LLM Evaluation. arXiv:2608.07762, 2026（QASC 2026 接收） | — |
| key45 | Yang et al. InfiCoEvalChain: A Blockchain-Based Decentralized Framework for Collaborative LLM Evaluation. arXiv:2602.08229, 2026 | — |
| key46 | Peng. DEP: A Decentralized LLM Evaluation Protocol. arXiv:2603.01167, 2026 | — |
| key47 | Helff et al. LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking. arXiv:2604.15149, 2026 | — |
| key48 | Bindschaedler, Botha & Siebenbrunner. Bonded Recourse for Smart-Contract Settlement of Compensable Agent Side Effects. arXiv:2609.01939, 2026（BCCA 2026） | — |
| key49 | Kaul, Lan & Gupta. Behavioral Governance for Autonomous AI Agents: The AgentBound Framework. arXiv:2606.30970v2, 2026 | — |
| key50 | Perera et al. Robust Agent Compensation (RAC). arXiv:2605.03409, 2026 | — |
| key51 | ERC-8004: Trustless Agents. EIP draft, created 2025-08-13 | 工程标准草案，非同行评审（v9 已标注，沿用） |

**L3 评测完整性线（8 条）**

| key | 题录（沿 v9） | pending 状态 |
|---|---|---|
| key16 | Gu et al. A Survey on LLM-as-a-Judge. arXiv:2411.15594, 2024（期刊版 2026: The Innovation） | — |
| key17 | Chang et al. A Survey on Evaluation of LLMs. ACM TOIS 15(3):1–45, 2024. DOI 10.1145/3641289 | — |
| key36 | Yang, Chiang, Zheng, Gonzalez & Stoica. Rethinking Benchmark and Contamination for Language Models with Rephrased Samples. arXiv:2311.04850, 2023 | 原「作者待补」→ **已闭合**（5 作者全列，citefix 留档一手核验） |
| key37 | Oren, Meister, Chatterji, Ladhak & Hashimoto. Proving Test Set Contamination in Black Box Language Models. ICLR 2024. arXiv:2310.17623 | 原「作者待补」→ **已闭合**（5 作者全列） |
| key39 | Fu, Uzner, Yetisgen & Xia. Does Data Contamination Detection Work (Well) for LLMs? NAACL 2025 Findings, pp.5250–5271. DOI 10.18653/v1/2025.findings-naacl.291 | — |
| key40 | Dekoninck, Müller & Vechev. ConStat: Performance-Based Contamination Detection in Language Models. NeurIPS 2024 D&B | — |
| key41 | Tao et al. Detecting Data Contamination from RL Post-training for LLMs. arXiv:2510.09259, 2025 | — |
| key42 | Wang, Li, Ko & Zhang. On the Fragility of Benchmark Contamination Detection in Reasoning Models. CoRR abs/2510.02386, 2025（ICLR 版在案） | — |

**L1 过程验证线（3 条）**

| key | 题录 | pending 状态 |
|---|---|---|
| key05 | Cobbe et al.（12 作者）. Training Verifiers to Solve Math Word Problems. arXiv:2110.14168, 2021 | — |
| key06 | Lightman et al. Let's Verify Step by Step. ICLR 2024. arXiv:2305.20050 | 原「作者+venue 待核」→ **已闭合**：10 作者（Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe）＋ICLR 2024（arXiv abs 页＋ICLR Proceedings 页双留档；作者拼写以 arXiv 页 Harri Edwards 为准） |
| key15 | Venktesh, Rathee & Anand. Trust but Verify! A Survey on Verification Design for Test-time Scaling. arXiv:2508.16665, 2025 | — |

**L5 守恒与物理先验线（3 条）**：key11（Greydanus et al., Hamiltonian Neural Networks, NeurIPS 2019）／key12（Karniadakis et al., Physics-informed ML, Nature Reviews Physics 3:422, 2021）／key13（Krishnapriyan et al., arXiv:2109.01050, 2021）——均无 pending。

**自引（1 条）**：key04（Yuan, Deposon…, arXiv:2609.09001, 2026；身份披露在 §9.3＋AI-use disclosure）。**入终稿 register 须按蓝图 §6 红线变更：自引→前作**。

**CoT／推理模型代表（3 条）**：key01（Wei et al., CoT Prompting, NeurIPS 2022）／key29（DeepSeek-AI, DeepSeek-R1, arXiv:2501.12948, 2025；Nature 2025 同发表）／key30（Baker et al., Monitoring Reasoning Models…, arXiv:2503.11926, 2025）——均无 pending。

**L2 CoT 忠实性代表（3 条，key30 已计上组）**：key02（Turpin et al., NeurIPS 2023）／key03（Lanham et al., TMLR 2023, 30 作者）／key33（Korbak et al., CoT Monitorability, arXiv:2507.11473, 2025，position paper 沿 v9 标注）——均无 pending。

**AI 科学家线（2 条）**

| key | 题录 | pending 状态 |
|---|---|---|
| key59 | Lu, Lu, Lange, Foerster, Clune & Ha (Sakana AI). The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery. arXiv:2408.06292, 2024 | 原「venue 待核」→ 作者已闭合（6 人全列）；venue 按 v9 口径以 arXiv 为准（「arXiv cited」写法不变） |
| key60 | Schmidgall et al.（10 作者全列）. Agent Laboratory: Using LLM Agents as Research Assistants. arXiv:2501.04227, 2025 | 同上，venue 以 arXiv 为准 |

### 1.2 a′ 组·增补候选（5 条，交查理按篇幅与 claim 需要取舍；全取则 35 条卡上限）

| key | 题录 | 定位 | 建议 |
|---|---|---|---|
| key07 | Kapoor & Narayanan. Leakage and the reproducibility crisis in ML-based science. Patterns 4(9):100804, 2023 | L3 入口经典（数据泄漏） | §2.3 L3 叙事需要入口锚时取 |
| key08 | Pineau, Vincent-Lamarre, Sinha, Lariviere, Beygelzimer, d'Alche-Buc, Fox & Larochelle. Improving Reproducibility in ML Research (A Report from the NeurIPS 2019 Reproducibility Program). JMLR 22(164):1–20, 2021 | L3 复现性锚，与 DAS-2M/0-LLM 可复算叙事同构 | 原「subtitle 待核」→ **已闭合**（JMLR 页一手：subtitle＋卷期页） |
| key09 | Irving, Christiano & Amodei. AI Safety via Debate. arXiv:1805.00899, 2018 | L4 传统锚（debate 验证；v9 L4 矩阵行在列） | §2.3 L4 需博弈论验证传统背景时取 |
| key10 | Conitzer et al. Foundations of Cooperative AI. AAAI 2023 | L4 传统锚（合作 AI／机制设计） | 同上 |
| key61 | Boiko et al. Autonomous chemical research with LLMs. Nature 624:570, 2023 | AI 科学家线唯一正式期刊锚 | §2.5 DAS 背景需期刊级锚时取 |

注：key09/10 属 v9 §6.1 矩阵 L4 行（\cite{key09,key10}），但蓝图 §3.3.a 条带仅列 key43–51；此处按「L4 传统锚」列增补，定夺权在查理／管理员。

### 1.3 b 组·不随行→「整体引用覆盖」（24 条）

- 邻接综述锚（1）：key14（Jaulmes et al., HAL: hal-05448955，**venue 仍 pending**，HAL 抓取空——综述锚功能由 key15 承担）
- 历史／哲学／科幻线（7）：key18（非欧几何）、key19（Jaynes）、key20（Wigner）、key21（Landauer）、key22（科幻计算分析）、key23（SF Prototyping）、key24（Technovation）
- 批判／可证伪性线（4）：key25（Wagstaff）、key26（Lipton & Steinhardt）、key27（Nielson）、key28（Buchholz & Raidl）——**对账注记**：key26 v9 记 arXiv:1706.06569，我 2026-09-16 FTFB 轮一手核验为 arXiv:1807.03341；因不随行不影响终稿，仅留档备查
- L2 非代表（3）：key31（Anthropic 机构报告，非同行评审）／key32（Young）／key34（Zolkowski et al., arXiv:2510.19851）
- L3 未选（2）：key35（Sculley et al., ICML 2025 Position）／key38（Ravaut et al., TMLR 2025 污染检测综述；作者 9 人已闭合）——若查理需要污染综述总锚可由 key38 替代 key39
- L5 形式验证扩展（3）：key52（OVERT, **JMLR 23(117):1–45, 2022 已闭合**，本轮留档一手）／key53（zkLLM, CCS 2024）／key54（zkML survey, AIR 59:157, 2026，09-17 已核验）
- 世界模型线（4）：key55／key56／key57／key58（作者 15 人已闭合）

**对账总式：32（随行）＋5（增补候选）＋24（覆盖组）＝61 ✓ 池封闭。**

---

## §2 DAS 题录 3 条（一手核验级；引用范围限摘要级事实——沿挂限 §8.1：论文正文细节未逐页核验，全部断言依据＝arXiv abs 页＋GitHub README＋项目页＋HF 数据集页五源留档）

**① DAS 论文**
> Zhikai Xu, Zhucun Xue, Teng Hu, Yabiao Wang, Yong Liu, Jiangning Zhang. "Deep Academic Survey: Stateful Agentic Closed-Loop Paradigm for Academic Survey Automation." arXiv:2608.18034 [cs], submitted 2026-08-18. DOI: 10.48550/arXiv.2608.18034.

- 6 作者；abs 页主类 cs（CVPR 类目页显示）；官方 README BibTeX 标「arXiv preprint, 2026」——终稿引用按 arXiv 预印本口径。
- 摘要级可用事实：stateful agentic 闭环框架、面向发表级学术综述自动生成；DAS-2M／DAS-Bench 为其开放组件。
- 边界（入稿限制句素材）：方法代码截至 2026-09-18 未发布（README "To be released"）；正文内部细节（judge 配置、backbone 敏感性数值等）未逐页核验，引用不得超出摘要级。

**② DAS-2M 数据集**
> ZhikaiXu24/DAS-2M, Hugging Face Datasets, released 2026-08-08. License: CC-BY-4.0.

- README 口径：「a persistent and dynamically updated literature metadata lake that provides reusable, survey-oriented representations of approximately 2 million papers」。
- HF 页标注：Tasks Text Retrieval/Text Generation；Format json；Size 1M–10M；关联 arXiv:2608.18034；两子集（metadata/retrieval）。
- 引用注意：HF viewer 服务端预览报 DatasetGenerationError（schema cast），系预览管线问题非数据缺位；本项目实测下载全 7 卷（2020-01–2026-07）1,471,166 条、分卷 SHA256 7/7 校验一致（实测明细以鲍勃通道与我方 das_check 留档为准）。

**③ DAS-Bench**
> DAS-Bench, component of ZhikaiXu24/DAS, GitHub (repository license Apache-2.0), 2026. Evaluation toolkit released 2026-08-08; published on Hugging Face 2026-08-20.

- README 口径：「a 30-topic multi-domain benchmark for academic survey generation, paired with DAS-Eval, a 16-criterion evaluation suite designed specifically for publication-oriented academic surveys, covering scholarly citation, taxonomic synthesis, hierarchical discourse, and manuscript reliability」。
- 许可边界（README 明示）：仓库代码与文档 Apache-2.0；**DAS-2M 单独分发、以 HF 数据集页条款为准**——两条许可不可混引。
- 仓库快照：latest commit 24fa88b（2026-08-20），33 commits。

---

## §3 挂点叙事源锚定

### 3.1 定案：「提案 v3」＝`results/_v3x_d0_5_aggregation_2026_09_17.md`

SHA-12 本轮实算 `ddf0d1aa96d2`，与委托信 §9 第 8 件记录一致（在位 ✓）。**排除候选** `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md`（SHA-12 `3d847f9f3151`，亦在位）。

**依据（五点）**：
1. **§4 ↔ 17 Adendum 精确对应（决定性）**：委托信 §5 章数据源「提案 v3 §4」→ 聚合文档 §4 缺口清单恰 17 项（A–Q），且「零成本 10＋中成本 7」分档与委托信 §5 章口径逐项吻合；挂载仓 17 件 `_adendum_{A..Q}_*.json` 的命名直接继承该清单 ID。FULL_EXPERIMENT_DESIGN（09-16 12:27）不含 17 Adendum 内容——该文档早于 Adendum 17 件的产生。
2. **§3 ↔ P-L v3 精确对应**：委托信 §4 章数据源「提案 v3 §3」→ 聚合文档 §3＝「Worker C P-L v3 数据合并」（文档标题即含「P-L v3」）；三态分离判死口径在聚合文档 §2。FULL_DESIGN 无 P-L v3 内容（09-16 时该实验尚不存在）。
3. **§1 ↔ 4 协作方收敛**：挂点 4「4 协作方聚合收敛」↔ 聚合文档 §0/§1「4 个独立观察者（GLM／Trae code+work／KIMI／Coze）对 P-L v2 根因完全收敛诊断」。
4. **§7 ↔ 拍板点**：委托信 §7 章「结论＋派生建议」源「提案 v3 §7＋V4 1 分支 memory」↔ 聚合文档 §7 用户拍板点（P-L v3 终局走法等 4 项决策）。
5. **清单与双审佐证**：委托信（09-17 21:35）§9 必读清单含聚合文档、不含 FULL_DESIGN；Trae 双审 §1.3 亦确认「8 章 outline 与 §1–§5 提案一致」。

**如实标注**：挂点 2 的「18 frozen＋5 制品＋22 caption」完整素材不在聚合文档（其间接出现：frozen 数据引用＋§4.2 E/K 两项），直接源为 5 audit 件（§1.5 18 frozen 巡逻 22/22 锚 PASS、§1.4 5 制品 audit）。委托信将挂点 2 归入「源＝提案 v3 §3–§7」是章级归并；终稿写挂点 2 时建议叙事源标「聚合文档 §4.2（间接）＋5 audit 件（直接）」。

### 3.2 4 挂点叙事段要点（只供叙事引用；一切数字以鲍勃核验表为准）

**挂点 1（9 模型×60 题账本 ↔ P-L v3 Phase 2 跨 backbone）**
- 双侧结构：〔W老师〕侧 9 模型全量账本轧平＋双主线精确重合（均衡带）；我方侧 P-L v3 Phase 2 跨 backbone β CI overlap（开源/闭源分组）＋OR embedding GRAY＋豆包 structural finding。
- 叙事主张：两线同为 cross-backbone 实现稳健性检验——「同一命题、两种呈现：对方以全量账本，我方以置信区间极窄带」，指向分布级协调比的跨实现稳定性。
- 锚：聚合文档 §2（判死指标）/§3（Worker C 实测）/§5.2（Phase 2 方案）＋委托信 §4 章。

**挂点 2（5 锚＋双指纹 ↔ 18 frozen＋5 制品）**
- 双侧结构：〔W老师〕侧 KT-D0 主锚＝anchor 0＋5 锚系列＋字节级/语义级双指纹；我方侧 18 frozen anchors＋5 制品 JSON＋schema v1＋caption 双指纹闭合＋根指纹/锚链。
- 叙事主张：内容寻址＋根指纹＋追加链的模式一致性——第三方可复算的制品锚定纪律是两线的共同底座。
- 锚：聚合文档 §4.2（间接）＋5 audit 件（直接）＋委托信 §2 章。

**挂点 3（「挂上也是交付」↔ P-L v3 Phase 1 FAIL＋GRAY＋FPR）**
- 双侧结构：〔W老师〕侧 KT-C1 幂律判死（死的是自己主张）＋KT-B1 判死线走正面结果；我方侧 Phase 1 FAIL（size scaling 失败）＋Phase 2 PASS＋P-K FPR 超阈 GRAY＋OR 1/6 GRAY。
- 叙事主张：共同方法论「诚实降级＋挂上也是交付」——负结果与灰区如实入稿，判死预设于实验前（判死指标先行）。
- 锚：聚合文档 §2（期望判死指标预设 FAIL/GRAY 路径）＋委托信 §6 章（audit PASS/FAIL/GRAY 老实入限制节）。

**挂点 4（4 协作方聚合收敛 ↔ 8 worker cross-backbone）**
- 双侧结构：〔W老师〕侧 9 模型 cross-backbone；我方侧多 worker cross-backbone＋制品＋frozen＋plugin spec＋schema。
- 叙事主张：共同方法论「多观察者聚合收敛＋诚实降级＋0 LLM 重算＋铁律零触动」——独立诊断收敛是结论强度的来源。
- 锚：聚合文档 §0/§1（4 观察者完全收敛）＋委托信 §2 章。

---

## §4 DAS 候选池 LLM-as-judge 域精选（终稿 §2 Related Work 用）

口径勘误（沿上轮素材包 §2.0）：扩量备忘所记「40 条」为笔误，程序清点候选池实为 52 条（A19＋B8＋C8＋D9＋E8）；本轮按管理员口径取 **A 组 LLM-as-judge 可靠性域全集 19 条，全部一手核验 ✓**（arXiv abs 页留档＋题录程序化提取）。与 v9 61 条池无同文；兼跨输出一致性的 3 条已互见标注。

**自偏好/偏差族（6）**
| arXiv | 题录（前三位作者＋et al.；venue 一律沿 abs 页 Comments，无则如实标无） | 一句话定位 | v9 池外补充直引 |
|---|---|---|---|
| 2601.22548 | Roytburg, Bozoukov, Nguyen et al. — ICML 2026 Main | LLM 评估者「自恋」命题的健全性检验：自偏好量级与任务/模型强相关 | ★（P-K 判官偏差背景） |
| 2410.21819 | Wataoka, Takahashi, Ri — NeurIPS 2024 Safe GenAI Workshop | 同族评审偏置的基础实证 | ★ |
| 2604.11589 | （abs 页无 venue 标注） | 多模态判官的模型偏好偏差 | — |
| 2606.16682 | （无 venue 标注） | 自演化回路中评估者偏好崩塌（EPC）机制 | — |
| 2505.19176 | （Under review） | 引导式 assistant 缓解教师偏好偏置 | — |
| 2505.17100 | （NeurIPS 2025 Camera-Ready） | 推理式去偏：任意 LLM 判官可改造得更可靠（「可治理」侧） | — |

**可靠性审计族（8）**
| arXiv | 题录 | 一句话定位 | v9 池外补充直引 |
|---|---|---|---|
| 2606.19544 | Norman, Rivera, Hughes —（无 venue 标注） | 大规模系统审计：可靠性≠效度，exact-match 校验须经机会校正 | ★★（P-K 判据效度叙事直接同族） |
| 2512.16041 | Feng, Wang, Cheng et al. —（无 venue 标注） | LLM-as-judge 基准本身的构造缺陷评估 | — |
| 2503.09347 | （ACL 2025） | 安全评估者对数据伪象不鲁棒（「更安全」可能只是运气） | ★（P-K FPR 控制叙事） |
| 2601.17312 | （无 venue 标注） | 「评估评估者」（meta-judging）二阶审查框架 | — |
| 2510.15746 | Yang, Liu, Miao et al. —（无 venue 标注） | **博弈论框架用于 LLM 评估的人类对齐——V3 博弈论化转向的直接同行，池内唯一** | ★★★（首选） |
| 2602.05110 | （无 venue 标注） | 支付风险域多评估者结构化框架 | — |
| 2511.20604 | （NeurIPS 2025 Camera Ready） | 「以 judge 评对齐」的循环结构分析 | — |
| 2409.20565 | （无 venue 标注） | 以排名代替评分的评测方法学——与本项目秩统计路线（Spearman/φ 并列校正）同族 | ★ |

**非传递性/一致性族（5）**
| arXiv | 题录 | 一句话定位 | v9 池外补充直引 |
|---|---|---|---|
| 2505.17691 | （venue 标注为接收信息） | 成对评估非传递偏好＋判官训练数据自净化 | — |
| 2310.02174 | （ACL 2024 main） | 追问下 LLM 判断动摇（vacillation）系统实证 | — |
| 2601.06118 | （无 venue 标注） | 确定性配置下 token 概率仍暴露非确定性（P-K 可重复性同源） | — |
| 2605.28840 | （无 venue 标注） | LLM 智能体多步执行行为可复现性测量——与 P-K 跨主体行为指纹直接同域 | ★ |
| 2607.18828 | （无 venue 标注，GitHub 链接） | 医疗域「同提供方评审」可行性边界 | — |

**补充直引优先级**（供查理 §2 取用，全取建议 ≤4 条控篇幅）：2510.15746（博弈论×judge，V3 转向近邻，池内无同文）＞ 2606.19544（效度方法学）＞ 2409.20565（秩统计）≈ 2605.28840（行为指纹）＞ 2601.22548 / 2410.21819（自偏好实证）＞ 2503.09347（伪象鲁棒性）。

---

## §5 pending 申报与留档

**pending（4 项，如实）**：
1. key14 venue 仍 pending（HAL 抓取空页）→ 已按默认剔除，综述锚由 key15 承担。
2. key59/60 会议接收状态未查（作者列表已闭合）→ 按v9 口径「arXiv cited」引用，不影响随行。
3. DAS 论文正文细节未逐页核验（沿挂限 §8.1）→ 引用限摘要级事实。
4. key26 arXiv 号 v9 记录疑误（1706.06569 vs 09-16 一手核验 1807.03341）→ 不随行、不影响终稿，对账留档备查。

**留档（本轮零新增网络检索，全部结论溯源自既有留档再提取）**：
- `citefix20260916/`：key06（abs＋ICLR Proceedings）、key08（JMLR）、key22/24/28（Crossref）、key36/37/38/58/59/60（arXiv abs）、key43/44/48/51/52/54 等 JSON——pending 闭合证据源。
- `das_check/`：p01（arXiv:2608.18034 abs）、p02（GitHub README）、p04（HF 数据集页）、abs_*.html（69 条候选核验）——§2/§4 题录证据源。
- 挂载仓本轮只读操作：委托信、聚合文档、FULL_DESIGN 三件 Read＋sha256sum 实算（ddf0d1aa96d2 / 3d847f9f3151 / 6d72e74b3482 委托信——与鲍勃核验包一致）。

---

**使用说明（给查理）**：§1.1 的 32 条为必随行底池（蓝图门审④的对账基准）；§1.2 增补 5 条按篇幅取用；§2 三条题录可直接进引用列表（注意两套许可不可混引）；§3.2 挂点叙事按「只供叙事、数字走鲍勃通道」执行；§4 补充直引建议全取 ≤4 条。

—— 阿兰-文献调研员 · 2026-09-18
