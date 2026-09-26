# V4 拍板问卷 · 组 A 批 3 · S-05–S-40 种子生产性判定代拟草案（36 条）

- **性质**：Mavis 代拟草案（PI 明示授权：问卷 `ask_a1eec04a2c64280da45c9cc4` 选项 opt_mavis_draft，PI 2026-09-22 拍板）
- **状态**：**PI 已复核确认生效**（PI 2026-09-22，问卷 `ask_f0ae3cf32f0bc8c83a1a8870`：「确认生效且前2条也补为你的具体口径而非模糊的deposon准则」；同日数字更正：「前4条都补为你的具体口径，而非模糊的deposon准则，之前输错数字了」）——36 条判定按本稿生效；R1 批 4 条（S-01–S-04）已全部按 PI 指示补具体口径（见文末「R1 补充」节）；**V1–V2 方法学底物注记已补录**（PI 2026-09-22 拍板「维持判定 + 补注记」+ 注记文本过目通过，判定不变，见「V1–V2 博弈论方法学底物注记」节）
- **判定依据**：deposon 项目核心准则「大材小用，落到实处，与死同行」（PI 原文，2026-09-22，R1 批录入）+ 邀请函 §4.9 生产性定义原文（"Productivity here means: would a concrete, falsifiable experiment that falsifies the question also falsify a substantive claim?"）
- **种子文本源**：邀请函 `letters/_v4_distillation_invitation_2026_09_20_v1.0.md`（SHA-12 `3D9F73519F6C`）§3 种子场 L131–L245，逐条对照起草
- **前序已答**：R1（S-01–S-04）PI 原答均「沿用deposon核心准则」（问卷 `5A0EBFD61AA0` L586；后经 PI 2026-09-22 数字更正，前 4 条均已补为具体口径，见文末「R1 补充」节）

## 判定框架（核心准则三问映射）

核心准则拆为三问，每条种子按三问过：

| 问 | 映射 | 含义 |
|---|---|---|
| **Q1 小** | 大材小用 | 实验规模可控？能否复用既有 V1–V3 资产而非从零造？ |
| **Q2 实** | 落到实处 | 在 §3.1 铁律现状 + §3.2 路径 B（proxy student 构造集）框架内，能否设计出具体的可证伪实验？ |
| **Q3 死** | 与死同行 | 证伪该实验是否同时证伪一条实质 claim（而非只证明「测不了」）？ |

**判定规则**：三问全过 = **productive**；Q2 或 Q3 不过 = **non-productive**；仅 Q1 不过（实验过大）= **non-productive**（沿「小」），注记可收窄路径。边界情形在判定内注记（borderline: 条件）。

**两点边界声明**：
1. 本稿 non-productive 多数指「**当前资产面上无落点**」（§3.1 铁律现状 + §3.2 路径 B proxy 框架内），非永久判定；括号内注记复评条件。
2. **non-productive ≠ out-of-scope**：Dimension 6 跨学科种子已按 §1.1.5 拍板 In-scope（主题自然词汇）；范围裁定与生产性判定是两个不同问题。

## 判定草案表（36 条）

### Dimension 1（S-05–S-06，转移内容）

| Seed | 原名 | 判定草案 | 核心准则理由（三问映射） |
|---|---|---|---|
| S-05 | Calibration and confidence transfer | **productive**（borderline：无 logprobs 时观测面由置信分布降级为拒答率） | Q2✓ proxy 构造集内可设计 proxy student vs 教师「拒答率/置信代理」对比；Q3✓ 证伪「置信差异可从输出面测量」即证伪实质 claim；Q1✓ V20 5 制品作行为面参考 |
| S-06 | Refusal-boundary transfer | **productive** | Q2✓ 可设计输入强度梯度 × 拒答率的边界曲线对比（proxy vs 教师）；Q3✓ 证伪「拒答边界可迁移且可测」；Q1✓ V2 phase1 60-cell（51/60 STRONG_PASS）判别面可复用为参考 |

### Dimension 2（S-07–S-12，可观测信号）

| Seed | 原名 | 判定草案 | 核心准则理由（三问映射） |
|---|---|---|---|
| S-07 | Output-distribution fingerprints | **productive**（最清晰，§1.1.1 实验轮廓主干已含） | Q1✓✓ V20 5 制品即输出分布基线；Q2✓ JS 主度量 + 对称 KL 稳健性已在实验轮廓；Q3✓ 证伪「输出分布可区分蒸馏产物」 |
| S-08 | Embedding-geometry alignment | **non-productive**（当前资产面；若开放嵌入导出通道可复评） | Q2✗ 冻结制品为纯文本，无嵌入导出通道；P-G v01 为脚手架层（verdict_pending=true）不能作校准发现 |
| S-09 | Logit shifts and temperature response | **non-productive**（当前资产面） | Q2✗ 邀请函原文明示 deposon 不存 logit 级制品，实验无从起步 |
| S-10 | Disturbance sensitivity | **productive** | Q1✓ V7 扰动实验协议可复用；Q2✓ proxy student 在扰动协议（错字/注入/模板切换）下与教师的响应对比可设计；Q3✓ 证伪「扰动响应收敛可作蒸馏信号」 |
| S-11 | Long-tail consistency | **productive** | Q1✓ 18 frozen + 22 caption + 5 KT 锚现成长尾探针集；Q2✓ proxy vs 教师长尾一致性对比可设计；Q3✓ 证伪「长尾一致性可作蒸馏深度代理」 |
| S-12 | Temporal correlation and pattern drift | **non-productive**（borderline） | Q2✗ 无行为时间序列样本（V2→V3→D7 是判别 verdict 时间序列，非教师行为时间序列）；知识截止注入式 proxy 可构造但基底弱 |

### Dimension 3（S-13–S-18，逆向蒸馏检测侧）

| Seed | 原名 | 判定草案 | 核心准则理由（三问映射） |
|---|---|---|---|
| S-13 | Steganographic fingerprints | **productive**（borderline；独立于 §1.1.3 关闭裁定——该裁定系 §4.4 复用特定 22-caption 作水印，本条为通用隐写指纹实验） | Q2✓ proxy 框架内可设计「教师输出注入统计标记 → 退化式蒸馏 → 标记留存率」实验；Q3✓ 证伪「植入指纹可在退化迁移中存活」 |
| S-14 | Training-dynamics inversion | **non-productive**（当前资产面） | Q2✗ 退化算子族 training-free，无训练曲线可反演；盘上无训练动力学记录 |
| S-15 | Output statistical anomalies | **productive** | Q1✓✓ V20 基线 + 实验轮廓 Track 1 算子（n-gram 截断/词表收缩）天然产出候选异常；Q2✓ 稀有 n-gram/句法多样性/困惑度长尾可测；Q3✓ 证伪「统计异常可区分蒸馏产物」 |
| S-16 | Membership inference | **non-productive** | Q3✗ proxy 构造集隶属关系按构造已知，对其做成员推断是构造上平凡为真，证伪不证伪实质 claim；且种子自述「最昂贵」——违「小」 |
| S-17 | Cross-model provenance | **productive** | Q1✓✓ 5 模型盲测制品结构即现成「已知教师候选」原型；Q2✓ proxy 输出归属判定实验可设计；Q3✓ 证伪「from-whom 归属可行/不可行」 |
| S-18 | Statistical signatures of distillation traces | **productive**（borderline：规避稳健性须进证伪条件） | Q2✓ 特征检索（退化输出 vs 独立对照）+ held-out 验证可设计；Q3✓ 证伪「存在独立训练几乎无法产生的特征」 |

### Dimension 4（S-19–S-24，反蒸馏防御侧）

| Seed | 原名 | 判定草案 | 核心准则理由（三问映射） |
|---|---|---|---|
| S-19 | Output watermarks | **productive**（独立于 §1.1.3 关闭裁定，理由同 S-13） | Q2✓ 与 S-13 共底物（标记注入 → 退化 → 留存）另加质量退化度量进证伪条件（张力即判死线）；Q3✓ 证伪「水印提高蒸馏代价而不显著降质」 |
| S-20 | Training-data poisoning | **non-productive**（当前资产面；且种子自注伦理/法律敏感） | Q2✗ 投毒需要训练型蒸馏器；退化算子 training-free 无从「中毒」；attacks/ 目录系判别用途，另需独立评估 |
| S-21 | Information bottleneck | **productive** | Q2✓ 退化算子族本身即信息瓶颈操作（n-gram 截断/词表收缩 = 主动限信息），可设计「瓶颈强度 × 输出保真」对比；Q3✓ 证伪「瓶颈强度与可蒸馏性负相关」；Q1✓ 算子族一件两用（既是 proxy 手段又是瓶颈自变量） |
| S-22 | Capability isolation / sub-model slicing | **non-productive**（当前资产面） | Q2✗ 能力切片是教师侧结构设计，超出输出信号可观测面；proxy 框架不可模拟 |
| S-23 | Adversarial perturbation | **non-productive**（borderline） | Q2✗ 种子原文主张「扰乱蒸馏**收敛**」需训练型蒸馏器，退化算子无收敛过程；可收窄为「扰动 → 退化输出保真降级」实验（S-13/S-19 同族），但已改换种子原主张 |
| S-24 | Behavioural-signature induction | **productive** | Q2✓ 固定短语标记注入 → 退化 → 留存率 + 擦除成本（用另一退化算子尝试擦除）实验可设计；Q3✓ 证伪「行为标记无法在不破坏整体行为前提下擦除」；可与 S-13/S-19 共底物 |

### Dimension 5（S-25–S-29，反-反蒸馏）

| Seed | 原名 | 判定草案 | 核心准则理由（三问映射） |
|---|---|---|---|
| S-25 | Adversarial escalation | **non-productive** | Q2✗ 需多轮迭代对抗方，超一次性 proxy 框架；无资产落点，过大 |
| S-26 | Watermark erasure | **productive** | Q2✓ 标记注入 → 擦除操作（paraphrase/采样可用另一退化算子实现）→ 残留率实验可设计；Q3✓ 证伪「何种粒度标记真正不可擦除」；与 S-13/S-19/S-24 共底物 |
| S-27 | Defense probing | **non-productive**（当前资产面） | Q2✗ 探测需带防御的 API 作为对象；当前资产面无防御侧 API |
| S-28 | Distiller-defender game | **non-productive** | Q2✗ 双方持续学习需仿真环境，过大；合理时间尺度内不可证伪 |
| S-29 | Long-horizon equilibrium | **non-productive** | Q2✗ 种子原文即 5 年尺度成本收益判断，合理时间尺度内不可证伪；过大 |

### Dimension 6（S-30–S-35，跨学科种子——§1.1.5 已拍 In-scope，下列判定为生产性判定，与范围裁定无关）

| Seed | 原名 | 判定草案 | 核心准则理由（三问映射） |
|---|---|---|---|
| S-30 | Hyperbolic geometry / curvature differential | **non-productive**（当前资产面；嵌入通道开放可复评） | Q2✗ 曲率计算需嵌入通道，冻结制品纯文本；P-G v01 为脚手架层（verdict_pending）不能作校准发现 |
| S-31 | Observer effect / measurement-as-perturbation | **non-productive**（当前资产面） | Q2✗ 「检测行为改变模型行为」需有状态被测对象；冻结制品为无状态一次性样本；盘上无观察者效应框架制品 |
| S-32 | No-cloning-theorem analogy | **non-productive** | Q3✗ 形式化/定理证明不是实验可证伪工作；类比可作论文概念词汇（In-scope 语境下），不作实验条目 |
| S-33 | Entanglement / context coupling | **non-productive**（当前资产面） | Q2✗ 多轮/检索/工具使用能力制品盘上不存在；proxy 框架内无底物 |
| S-34 | Decoherence / reasoning collapse | **non-productive**（borderline：长链任务集若建构可复评） | Q2✗ 盘上无推理链样本（V7 是 verdict 非推理链）；长链任务 proxy 可构造但无现成资产 |
| S-35 | Bell-inequality analogy | **non-productive**（borderline） | Q2✗ 尚无具体 Bell 型检验形式；但若形式化成立可直接作 §4.1 最小 claim 的证伪工具——注记形式关联（非排序，仅记连线） |

### Dimension 7（S-36–S-40，评估科学）

| Seed | 原名 | 判定草案 | 核心准则理由（三问映射） |
|---|---|---|---|
| S-36 | The ground-truth dilemma | **productive**（已入实验轮廓） | 已按 §1.1.1 拍板锁定 GT 来源 = 构造性声明（正类 = proxy 构造集，负类 = 独立对照，不外推真实学生）；Q2✓ Q3✓ 均满足 |
| S-37 | False-positive / false-negative cost structure | **productive** | Q1✓ D7 verdict + 540（9 backbone × 60 cell）判别矩阵骨架；Q2✓ proxy 构造集 + 独立对照内 FP/FN 成本曲线与阈值倾斜分析可设计，可直接进实验轮廓 R6（冻结集外负对照校准 τ）；Q3✓ 证伪「最优阈值倾斜方向」 |
| S-38 | Reproducibility / cross-laboratory consistency | **productive**（borderline：须收窄） | Q2✓（收窄后）字面跨实验室过大；收窄为跨算子/跨骨干一致性（实验轮廓 R3 排列检验部分覆盖）可设计；Q1✓ V2/V3 多骨干 × 多 cell 设计本身即复现友好 |
| S-39 | Evaluation-of-the-evaluated recursion | **non-productive**（当前资产面） | Q2✗ 「被评模型知道被评」需有状态被测对象（与 S-31 同阻断）；冻结制品无状态 |
| S-40 | Long-term validity and drift | **productive**（borderline） | Q1✓ V2（09-11）→ V3（09-11）→ D7（09-18）判别制品时间序列作漂移脚手架；Q2✓（borderline）3 时点小样本但可做首轮漂移检查；Q3✓ 证伪「检测信号跨版本稳定」；「持续服务」定位与「与死同行」同构 |

## 汇总统计（S-05–S-40，36 条；40 条全景见文末「R1 补充」节后统计）

| 维度 | productive | non-productive |
|---|---|---|
| Dim 1（S-05–S-06） | 2 | 0 |
| Dim 2（S-07–S-12） | 3（S-07/S-10/S-11） | 3（S-08/S-09/S-12） |
| Dim 3（S-13–S-18） | 4（S-13/S-15/S-17/S-18） | 2（S-14/S-16） |
| Dim 4（S-19–S-24） | 3（S-19/S-21/S-24） | 3（S-20/S-22/S-23） |
| Dim 5（S-25–S-29） | 1（S-26） | 4（S-25/S-27/S-28/S-29） |
| Dim 6（S-30–S-35） | 0 | 6 |
| Dim 7（S-36–S-40） | 4（S-36/S-37/S-38/S-40） | 1（S-39） |
| **合计** | **17**（S-05, 06, 07, 10, 11, 13, 15, 17, 18, 19, 21, 24, 26, 36, 37, 38, 40） | **19**（S-08, 09, 12, 14, 16, 20, 22, 23, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39） |

## 底物共离观察（事实陈述，非排序、非推荐）

- §1.1.1 实验轮廓直连：S-07 / S-15（可观测层）、S-36（GT 已锁定）、S-37（R6 负对照校准 τ）
- proxy 标记留存率共底物：S-13 / S-19 / S-24 / S-26
- 退化算子一件两用（proxy 手段 + 瓶颈自变量）：S-21
- 现成资产直接复用：S-10（V7 扰动协议）、S-11（锚库长尾探针）、S-17（5 模型盲测结构）、S-40（判别制品时间序列）

## R1 补充：S-01–S-04 具体口径（PI 复核指示 2026-09-22 + 同日数字更正）

PI 复核指示原文：「确认生效且前2条也补为你的具体口径而非模糊的deposon准则」；同日更正原文：「前4条都补为你的具体口径，而非模糊的deposon准则，之前输错数字了」。R1 批 S-01–S-04 原答均「沿用deposon核心准则」，4 条现已全部补为具体口径（S-01/S-02 先补，S-03/S-04 随更正补齐）。

| Seed | 原名 | 判定（具体口径） | 核心准则理由（三问映射） |
|---|---|---|---|
| S-01 | Weight-level transfer | **non-productive**（当前资产面；权重/LoRA 白盒访问通道开放可复评） | Q2✗ 权重级操作（参数拷贝 / LoRA 抽取 / 蒸馏初始化）需白盒权重访问；deposon 冻结制品全为黑盒文本输出 + verdict JSON，proxy 框架（输出面退化算子）不可模拟权重操作 |
| S-02 | Representation-level transfer | **non-productive**（当前资产面；嵌入导出通道开放可复评——与 S-08 / S-30 同阻断、同复评条件） | Q2✗ 表示级几何（嵌入 / 流形 / 距离）需嵌入通道，冻结制品纯文本；P-G v01 系脚手架层（verdict_pending=true），可借形不可作校准发现 |
| S-03 | Behaviour-level transfer | **productive**（borderline：操作化收窄——停顿节奏等时间维度在冻结纯文本制品上不可观测，行为指纹收窄为措辞偏好/词频/句法层面；与 S-07/S-21 共底物） | Q1✓✓ V20 5 制品（corpus/v20/by_model/ 5 模型）即现成跨模型行为样本基线（种子自引 related asset）；Q2✓ proxy 框架内可设计「退化算子强度 × 行为指纹留存率」实验（措辞偏好/词频分布/句法多样性随算子强度的衰减曲线）；Q3✓ 证伪「行为指纹在退化迁移中按可测规律衰减」即证伪实质 claim |
| S-04 | Reasoning-chain transfer | **non-productive**（当前资产面；推理链形态样本若可得可复评——与 S-34 同阻断、同复评条件） | Q2✗ 冻结制品中无以推理链为主要形态的样本：V20 5 制品系盲测判别输出（非 CoT 形态），V7 系 verdict JSON（种子自述「is a verdict, not a reasoning-chain sample」）；proxy 退化算子无推理链底物可作用 |

## 汇总统计（40 条全景，含 R1 补充）

- **productive**：18 条（S-03【R1 具体口径】, 05, 06, 07, 10, 11, 13, 15, 17, 18, 19, 21, 24, 26, 36, 37, 38, 40）
- **non-productive**：22 条（S-01, 02, 04【R1 具体口径】, 08, 09, 12, 14, 16, 20, 22, 23, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 39）
- **沿用核心准则（PI 原答，未给二值）**：0 条（S-03/S-04 已随 PI 2026-09-22 数字更正补为具体口径）

## V1–V2 博弈论方法学底物注记（2026-09-22 PI 拍板补录）

- **拍板依据**：PI 2026-09-22 问卷 `ask_5b15ae2e55eb7c84f405f1d4`——「维持判定 + 补方法学底物注记」；注记文本过目通过（同日问卷 `ask_ecd9aa4264fba3e90ce9f1f8`）。本节为纯增补注记，36 条判定与 40 条全景统计均不变。
- **V1–V2 仓内博弈论资产（read-only 定位，未触动）**：`docs/GT_FORMALIZATION_v1.md`（预登记锚 SHA-12 `aeefb8ef6972`）；`run_v21_gtformal.py`（`9bbe43f41fa8`）/ `run_v22_p1c.py`（`6e9673205dc0`）/ `run_v22_e95ci.py` / `run_v20_gt*.py` 脚本家族；系统采样协议 61 图 × 338 任务 × 20 步 = 6760 状态枚举；GT4_ECR 标量账（median=4/3，覆盖 20/22 图）与 GT6 近梯度性检验；E9_5 非配对 Newcombe CI；P1a/P1b/T-P1c 三层级判死 + mechanical kill-lines 方法学；脑图方向 88 文件（`mindmap_corpus_v20.py`、`docs/SYNTHESIS_mind_game.md`、`docs/CLOSURE_v19_and_v2X_gametheory.md` 等）。
- **与 Dim 5 判定的关系**：上述资产属**静态、一次性、系统采样**的博弈结构分析（冻结制品上一次算完、pytest 可复算）；S-25/S-28 种子原文要求的是**动态持续对抗**（iterative escalation / distiller-defender 共同进化），两者不同——维持 non-productive 的判定理由不变。
- **S-25 复评条件扩写**：原注记仅「过大」；若收窄为**静态博弈形式化版本**（如教师-防御者一次性博弈矩阵的构造与求解），则 `GT_FORMALIZATION_v1` 形式化框架 + ECR 型标量账 + 系统采样协议即现成方法学底物，「大」可变「小」——届时可复评。
- **S-28 复评条件扩写**：同理，若收窄为「一次性 distiller-defender 博弈的形式化」（非持续学习仿真），同一套底物适用，可复评。
- **S-27 / S-29 不变**：V1–V2 资产无助于解除各自阻断（S-27 需带防御侧 API 作为对象；S-29 系 5 年尺度成本收益预测，合理时间尺度内不可证伪）——复评条件维持原判。
- **准则口径（随录）**：deposon 核心准则「大材小用，落到实处，与死同行」为**根准则**，先于并贯穿 V1–V2 论文实践；V1–V2 论文「与死同行」章节等成果是准则的**一处外显**（PI 口径 2026-09-22：「准则才是根，已发表论文的章节只是一处外显」）。

## 边界声明

本稿由 Mavis 起草（PI 明示授权代拟）。起草过程 0 LLM 调用、0 外部 URL、0 GitHub/WeChat 操作、0 密钥、0 frozen 制品/schema/锚文件触动；种子文本逐条对照邀请函本体（`3D9F73519F6C`）§3 L131–L245。36 条判定 + S-01–S-04 具体口径（PI 复核指示补录，S-03/S-04 随同日数字更正补齐）**已经 PI 复核确认生效**（2026-09-22）；V1–V2 方法学底物注记节同经 PI 拍板补录 + 注记文本过目通过（2026-09-22）；问卷 §1.1.6 已同步回填。问卷本体仍为权威。
