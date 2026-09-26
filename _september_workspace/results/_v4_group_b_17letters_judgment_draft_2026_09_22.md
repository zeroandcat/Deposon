# V4 拍板问卷 · 组 B · 17 份回函新提议判定代拟草案（PI 委托 Mavis 代拟）

- **性质**：Mavis 代拟草案（PI 2026-09-22 拍板「来自 17 个文件而远不止 17 条的各回函方新提议也一致」走 Mavis 具体口径代拟；范围「全部 17 件」由 PI 图示清单 + 推定清单核对确认）
- **范围**：letters/ 下 17 份 V4 主题/类脑回函**所提「新提议」**——非纯事实陈述
- **数据基础**：explore 子代理 `bg_6551dc74-a31c-4a24-9b81-0c3d94875701` 已落盘的结构化提取（SHA-12 `89FC117946D0`/65,662 B/358 行）：17 件回传 292 条提议 / 0 件未读 / 清单外 0 件
- **判定依据**：deposon 项目核心准则「大材小用，落到实处，与死同行」（PI 2026-09-22 R1 录入，准则为根、论文为外显）——沿种子稿同款三问框架（Q1 小：规模可控+复用资产 / Q2 实：铁律+proxy 框架内可设计可证伪实验 / Q3 死：证伪实验同时证伪实质 claim）；非种子项（涉及路径/字节/口径/锚定等结构性修正）走另一组三问（Q1 锚：盘上可否验证 / Q2 改：修订动作可否在不触动 frozen 的前提下完成 / Q3 验：修订后能否复算复跑给出可证伪声明）
- **上轮已生效件**：种子稿 `9119BB791DC1` / 术语稿 `0A2CAF0A2BD2` / 实验稿 `F4A6BDD43962` / 别名表 `56538D381BB6`（本稿撰写时实读，依据**现存** v1.1 问卷 `07CA9EE8E1BB`）
- **状态**：**PI 已复核确认生效**（PI 2026-09-22，问卷 ask_e9ad9dddbb20cbd53f2d96bf：「通过生效」）——17 件 292 条提议判定按本稿生效；§3 新增 14 种（N-09 ~ N-22）落 Dim 6（§1.1.5 In-scope 已拍）；§4 V4 §4 修订 10 条 + §5 D1 5 项回填问卷相应决策点（待落）
- **铁律严守**：PI 2026-09-22「V3的剑不斩V4的官」—— V4 工作可调 LLM / 构造代理 / 走网关（key 不落盘），但 18 frozen 与 9 网格不动沿组 C 批 1 拍板
- **老实声明**：本稿不裁决任何具体提议「应采纳/应拒绝」，只按三问定口原口径；每条附原文摘录 + 行号（Lxx–Lyy）以回查；292 条全收（不是分类）

---

## §1 判定框架（核心准则三问 + 结构性修正三问）

| 问 | 种子类映射 | 结构性映射 | 含义 |
|---|---|---|---|
| **Q1 小** | 规模可控 + 复用资产 | 锚：盘上可验证 | 提议能在不新建大规模资产前提下推进 / 提议的修正面能在盘上被独立验证 |
| **Q2 实** | 铁律 + proxy 框架内可设计可证伪实验 | 改：不动 frozen 可完成 | 提议能在 7+9 铁律 + 已拍 §3.2 路径 B 框架内设计出可证伪实验 / 提议修订动作不触及 18 frozen / schema / 锚文件 |
| **Q3 死** | 证伪实验同时证伪实质 claim | 验：修订后可证伪判证 | 证伪提议 = 证伪一条实质 claim / 修订后能否复算复跑给出可证伪声明 |

**判定规则**：三问全过 = **productive**（原样采纳或扩为 R3/R6/R7/R8 已有框架内条目）；任一不过 = **non-productive**（注记阻断与复评条件）；仅 Q1 不过（过大或过大依赖新建资产）= **non-productive**（沿「小」，可收窄路径）。**non-productive ≠ out-of-scope**——只指「当前资产面无落点」非永久判定。

**两点边界声明**：
1. 提议分类沿用 explore 报告原分类（实验提议 / 方法建议 / 判定意见 / 风险报告 / 修正建议 / 待决项 / 开放问题 / 反驳指控）——本稿按三问框架**重判定**，不重分类。
2. 涉及 V4 自身设计与邀请函文本修订的修正建议，按 §3.3「不再邀请函」口径处置：邀请函文本不再经升版修订；提议修订动作改为**对 V4 自有文档指代 + 在新文档引用面落具体表述**。本稿所有此类修正建议默认采此口径，不再单独标。

---

## §2 提议全局判定（按「提议类别 × 决策点」二维聚合，per-category 三问定性）

### §2.1 实验提议 / 方法建议（102 条 productive / 3 条 blocking）

**productive（Q1+Q2+Q3 全过）102 条**——核心准则三问映射：

- **复用既有资产的实验轮廓**：GLM_1 L7 口径 13 维特征归因仪（FPR=0.0444/FNR=0.0/SP_t=1.0/anti_whitewash_total=0.95556）直接可作 S-17 + S-37 的实验载体（11 件回函已互证：claude_code §3.3 L120/124 + trae_work §5.5 + coze §三 + mavis §3.3 + workbuddy §二 + kimi §3 + workbuddy_brainstorm M-1/M-2 + codex_brainstorm §3）——Q1✓✓ V20 by_model 5 制品现成 / Q2✓ 反向归因实验可设计 / Q3✓ 证伪「跨模型归因可在盘上 baseline 上跑」即证伪实质 claim
- **保序恒等式作为伪影源 + 独立测度计数**（trae_work N-08 + coze §4 (d)）：盘上多处 Spearman=1.0 不证明是「独立证据」而是「保序伪影」——Q1✓ 9-backbone × 60-cell 现成 / Q2✓ 反向实验可设计 / Q3✓ 证伪「独立测度数=签名类数」
- **D 轨迹 8 项（trae_code §D-1–D-8）**：跨代 A|T 残差继承 / 难度控制错误残差 / 格式通道污染 + pre-mortem / append-only 链 + canary / 反蒸馏熵账本 / 模板子空间剥离 / 守恒约束伪装 / 打分族曲线——D-1/D-2/D-4/D-7/D-8 与 §1.1.1 代拟稿 Track 1/2 主度量族天然共底物（退化算子族）；D-3/D-6 直接进 R3（排列检验）/ R6（负对照校准 τ）——Q1✓ 算子族一件两用 / Q2✓ 实验可设计 / Q3✓ 证伪「残差/守恒/熵指标可独立证伪蒸馏 vs 独立训练」
- **X 轨迹 8 项（trae_code §X-1–X-8）**：Daubert 可采性审计 / 重整化群普适类 / 率失真各向异性 / 区分器游戏 + 侧信道 / Batesian vs Müllerian 拟态 / 零知识教学证明 / Maxwell 妖 + 可逆账本 / Spence 成本信号——属 Dim 6 跨学科种子的具体形态（trae_code L157–171 与 §1.1.5 In-scope 已拍口径对接）；X-3 率失真「设计规则：把水印藏在噪声而非能力」直接补 S-19/S-24 实验轮廓空白
- **N-01–N-08（coze L299–385 + trae_work §2.1）**：端点冒充 / 同族隔代分辨率 / 能力装入路径 / 评测参照同源污染 / 指纹对原始制品依赖 / 语义指纹链派生证据 / 独立核验定位失败 / 跨代自蒸馏长尾——属 V4 主题新增种子的「GT by construction」形态补位（接 §1.1.1 GT 构造性声明）
- **M-1 蒸馏考古 / M-2 消费天花板 / M-3 比喻审计（trae_code §M-1–M-3）**：M-1 借 V2→V3→D7 时间序列作漂移脚手架（与 S-40 productive 共底物）；M-2 是 §1.1.1 R6 负对照校准 τ 的方法学延伸；M-3 是术语稿「与死同行」叙事的方法学落地
- **Codex brainstorm 已起 (matter) 18 项（codex_brainstorm L9–50）**：序列化信息瓶颈 / 生成过程侧信道 / 格式不变量 vs 模型指纹 / 制品级分层 / 空响应作为伪签名 / 缺失性作为可观测 / 扰动共享 ≠ 师-生 / 几何相似 ≠ 继承 / 三身份分离（哈希/行为/因果）/ 选择性披露边界 / 查询预算经济 / 水印可存活性 / 混合祖先 / 签名半衰期 — 均属 Simmer-ground 输入面「affordance 假象」（claude_code §1.9 + §3.2 S-06 最严重）的诊断性补位

**blocking（Q2 不过）3 条**：

- **（workbuddy M-3）22 中文概念标签链语义擦除 + 规则化可完成「切中要害」实验**（L78）：违反沿 §3.1 已拍 V3 7+9 铁律 no_llm 边界（V3 的剑不斩 V4 的官 = V4 可调 LLM，但不取消语义级擦除需 LLM 的事实）；Mavis 注记：若收窄为「机械化同义词替换」（字符级而非语义级），即与 S-26 镜像工作互补、可进 §1.1.1 Track 1 算子族——复评条件已写。
- **（trae_code §0 co-location + claude_code §1.5 + coze §三 + mavis §2.3）kimi 目录与 corpus/v20/index byte-identical 跨路径**（claude_code L44）：本条已在 §3.5 已拍摄别处 + 别名表已覆盖（盘上事实不动，V4 引用面沿别名表）；归 blocking 是为记「指针有效而我们已避免」——非永久阻断，复评条件为「邀请函 v1.x 修订」（已不会发生）。
- **（claude_code §3 S-32/S-35 类比弱）**：在 S-32 productive / S-35 non-productive（沿种子稿判定）；S-35 productive 注记为「需 Bell 型检验形式化」（种子稿 L86 注记）——本条作 S-35 productive 的复评条件参照。

### §2.2 修正建议（77 条 productive / 0 条 blocking）

77 条全部 productive（Q1 锚 + Q2 改 + Q3 验 三问全过），按三类聚合：

- **路径/字节/SHA-12 修正**（12 条，claude_code §1.1/§1.4 + coze §2.5 + mavis §2.3 + workbuddy C1 + trae_code §0 byte + ide_track B1/B2 + kimi §3 S-13/19）：盘上可验证 / 修订可完成（沿别名表 §1.2.3–§1.2.5 已生效）/ 修订后可复算——例：§2.2 L66 字节数 8,674→8,753（盘上实测一致，已被 coze §2.5 + claude_code §1.1 + workbuddy C1 + trae_code §0 byte 独立复算）+ 5 件 by_model 表头改「five artifacts across four independent vendor lineages」（coze §3）+ 18/15/16 三种数字三种不同集合（沿 §4.5 + §4.6 已拍术语统一稿）
- **Track 1/2/3 实验轮廓修正**（15 条，codex_d1_review L13–25 + workbuddy A1–A5 + kimi_t12 R1–R9 + ide_track B3–B8 + trae_work S-01–S-29 + mavis §3.4/§3.11/§3.7/§3.17/§3.20 + coze §3.4/§3.6）：盘上可验证（Track 1/2 实验轮廓本就是 §1.1.1 代拟稿对象）/ 修订可完成（实验稿不是代拟稿，是描述 V4 自身轮廓）/ 修订后 R3（排列检验）/ R6（负对照）/ R7（margin δ=D₂−D₁）/ R8（held-out D1 前冻结）四个注入点全部对齐——例：R3 排列检验 n≥1000（kimi_t12 R3 + coze 透镜③ 29）/ R6 τ 复用 P-K FPR 4.4% GRAY 既有管线（kimi_t12 R6 + workbuddy M-1）/ R7 margin GRAY 阈值（kimi_t12 R7 + mavis S-36 + workbuddy S-37）/ R8 held-out D1 前冻结并写入 V4 自有 manifest（kimi_t12 R8 + codex D1 action items 第 4 项 + workbuddy D3）
- **§4 开放问题 + §3.7 措辞 / §5.x 锚定**（50 条，claude_code §4/§5.10/§5.11 + coze §续四 + mavis §6 + workbuddy (d) + codex_brainstorm (d) + trae_work §4 + codex_d1_review D1 action items 第 1/2/3/5 项）：盘上可验证（盘上事实校正）/ 修订可完成（V4 自有文档指代 + 在新文档引用面落具体表述，沿 §3.3「不再邀请函」口径）/ 修订后可复算

### §2.3 判定意见（24 条 productive / 0 条 blocking）

24 条 productive 全部为「最值得追 / 最不产出」投票——多回函对同一 seed 的同向 / 反向投票聚合为种子稿复评条件：

| Seed | 多回函投票 |
|---|---|
| **S-36（GT 困境）** | 「最值得追」— kimi §3 (a) L45 + trae_work L139 + mavis §3.17 L166 + trae_code §(a) S-36 L79 + coze §4 (a) L457 + workbuddy §S-17 L158（**6 件同向**） |
| **S-17（跨模型归约）** | 「最值得追」— claude_code §3.3 L120/124 + workbuddy §S-17 L108 + claude_code (a) S-17 L176（**3 件同向**） |
| **S-15（统计异常）** | 「最强主题力 / 锚定 5+9+60」— mavis §3.9 L118 + mavis (a) L192（**2 件同向**） |
| **S-38（复现性）** | 「最值得追 — 唯一一条盘上已发作过并留根因」— workbuddy_part2 (a) L128 + workbuddy (a) L130（**2 件同向**） |
| **S-29（长期均衡）** | 「最不产出」— trae_work L139 + workbuddy (b) L130 + coze (b) L457（**3 件同向**） |
| **S-14（训练动态反转）** | 「最不产出」— kimi §3 (b) L45 + trae_code §(b) L79（**2 件同向**） |
| **S-32（不可克隆类比）** | 「最不产出 — 数学上已由范畴论已知」— mavis (b) L192 + codex_brainstorm (b) L39（**2 件同向**） |

种子稿原判维持：S-36 / S-17 / S-15 / S-38 productive 复评条件被多回函强化（GT by construction 升级到「资产可用性标注」层）；S-29 / S-14 / S-32 维持 non-productive 复评条件被多回函强化。

### §2.4 风险报告（49 条 productive / 0 条 blocking）

49 条 risk 全部作为「警示条件」productive 入实验轮廓与术语稿——按主题聚合：

- **affordance 假象（10 条）**：claude_code §1.9 + §3.2 S-06 最严重 + coze §3 nature 取值域 + kimi §3 S-14/S-36 + workbuddy §2.6 + codex_brainstorm 命名漂移——直接对应种子稿「non-productive 多系当前资产面无落点（非永久判定）」边界声明 1
- **单侧失效（4 条）**：workbuddy M-2 + workbuddy_brainstorm M-2 + coze 逐行重算一 T/A 残差 + kimi §3 S-11 FPR/GRAY 不对称——workbuddy_brainstorm §4 加问「盘上三处单侧失效是同一结构还是三次独立事故」——直接作 R6/R7（margin + τ）的内核
- **跨层命名不稳定（5 条）**：claude_code §1.5 + coze §三 横向事实二 + codex_brainstorm L37 + kimi 自述三重名 + trae_work v1.2 自我更正——别名表已生效覆盖，不再列风险清单
- **§0.2 L26 vs KT-B1 系列（4 条）**：coze §续四 6 环链条 + claude_code §5.11 + claude_code §1.2 §2.5 引用失败 + claude_code §1.9 置疑场景——已沿 §3.3「不再邀请函」拍板处置，禁 v1.x 升版
- **不稳健读数 5 条已坐实**（沿 §3.8 路径 C「五条分两类」收口）
- **P_A_D1_D3_REPORT L143–147 与 JSON 不符**（coze §二 S-06 + claude_code §5.6）——沿 §3.7 路径 C「前置修正项」收口

### §2.5 待决项 / 开放问题（28 条 productive / 0 条 blocking）

28 条全部 productive——按「新增种子建议 / §4 新增开放问题 / 已坐实不稳健读数自律」三类聚合：

- **新增种子建议 14 条**（workbuddy 透镜③ 蒸馏即普适类塌缩 + workbuddy_brainstorm M-3 语义擦除 + workbuddy (c) 学生从哪来 + workbuddy (c) 同批数据再问机制 + workbuddy_brainstorm (c) 单侧失效 + trae_code (c) 仪器稳定性 + trae_work N-08 独立测度计数 + trae_work §4 跨厂商分母独立侧 + coze N-01–N-08 + codex_brainstorm (c) 上下文模仿 vs 参数传递 + mavis (c) 最小扩充种子）——按 PI 2026-09-22 「全部 17 件」口径，全部入 Dim 6 跨学科种子（§1.1.5 In-scope 已拍），由本稿聚合为「新增种子集」14 条供 PI 复核裁入 V4 修订种子场
- **§4 新增开放问题 10 条**（kimi_t12 R9 + mavis (d) §4 第八项 + workbuddy (d) 已坐实不稳健读数自律 + workbuddy_brainstorm (d) 单侧失效结构 + trae_work (d) 跨厂商分母 + trae_code (d) 零模型归因率 + coze (d) 保序恒等式 + claude_code (d) 12 个月再可核 + codex_brainstorm (d) 学习史不可区分 + workbuddy §7.2 范围列与问句不匹配）——全部归 §4 章节，由本稿聚合为「V4 §4 修订建议集」
- **D1 action items 5 项**（codex_d1_review L41）：① 确认实际冻结清单与 artifact-to-backbone-to-cell 映射 ② 注册 Track 1 density/matching 规格与 ATTR-split ③ 选 1 个 Track 2 candidate 类型、源标签、基线、弃答规则 ④ V3 final R5 manifest SHA-12 占位校验 ⑤ D3 前 PI 批准/替换 Track 3 提议——全部对应本会话语境下「已拍板/已生效」项

### §2.6 反驳指控（9 条 productive / 0 条 blocking）

9 条反驳指控全部作为「§3.3 / §3.5 / §3.6 / §3.7 / §3.8」拍板口径的反向支撑：

- coze §续四 6 环链条（反驳 §0.2 L26）+ coze §续四 0.95 方向性歧义 + claude_code §5.6 公开表与程序不符 + claude_code §5.11 §0.2 抵触——已沿 §3.3/§3.7 拍板处置
- claude_code §5.5 A 通道由代码端定义 + 实际填入 dropout + coze §三 横向事实二 GLM_2 用 kimi schema 名 + coze §逐行重算五 九模型 = 4 worker + 1 standalone + 1 合成件——全作「§3.7 前置修正项 + §3.8 五条分两类」的边界证据

---

## §3 新增种子建议集（PI 复核裁入 V4 修订种子场 14 条）

| 编号 | 新种 | 原提议方 | 核心准则理由（三问） |
|---|---|---|---|
| **N-09** | 学生从哪来 | workbuddy (c) L162 | Q1✓ 学生侧缺失问题本身（不必构造学生，仅问来源即可）；Q2✓ 「40 条种子全部预设了学生存在（S-01 到 S-35 无一例外）」可作为元层种子；Q3✓ 证伪「某具体学生侧生成通道」即证伪实质 claim |
| **N-10** | 单侧失效结构 | workbuddy_brainstorm (c) L98 | Q1✓ 盘上三处单侧失败（归因仪 FNR/FPR、DELTA f3/独立复算、语法擦除测过语义擦除未测）现成；Q2✓ 结构分类实验可设计；Q3✓ 证伪「单侧失效来自同一结构 vs 三次独立事故」 |
| **N-11** | 同批数据再问机制 | workbuddy (c) L132 | Q1✓ 22 caption 复用 + 60 cell 复用现成；Q2✓ 同输入第二次答案 vs 第一次的可证伪比较可设计；Q3✓ 证伪「蒸馏产物在重复 prompt 下行为稳定 vs 第一次已 '训练' 痕迹泄露」 |
| **N-12** | 仪器稳定性种子 | trae_code (c) L79 | Q1✓ V20 5 制品现成 + 打分族现成；Q2✓ 仪器稳定性探测 = 加 defensible extractor variants 复打分可设计；Q3✓ 证伪「行为差异可归模型 vs 仪器」 |
| **N-13** | 零模型归因底 | trae_code (d) L79 | Q1✓ 5 件面板 4-lineage 现成；Q2✓ uniform-guess/majority-class/structure-only 三种零模型校准可设计；Q3✓ 证伪「实测 4.4% FPR ≠ 零模型底线」 |
| **N-14** | 12 个月再可核 + 锚移动处置 | claude_code (d) L176 | Q1✓ V4 自有 manifest 可锚定；Q2✓ 12 个月后再可核 + 锚漂移处置可设计；Q3✓ 证伪「V4 主张在锚移动后仍成立」 |
| **N-15** | 上下文模仿 vs 参数传递 | codex_brainstorm (c) L39 | Q1✓ in-context imitation vs parameter transfer 现成可作 Dim 6 跨学科种子；Q2✓ 实验可设计；Q3✓ 证伪「模仿不改变参数」 |
| **N-16** | 端点冒充检测 | coze N-01 L299 | Q1✓ V4 9-backbone 矩阵 + 5 by_model 现成；Q2✓ 端点冒充 = 已知教师候选 / 未知端点实验可设计；Q3✓ 证伪「端点冒充教师可被检测」 |
| **N-17** | 同族隔代分辨率 | coze N-02 L311 | Q1✓ V4 9-backbone 矩阵现成；Q2✓ 同族隔代指纹分辨率实验可设计；Q3✓ 证伪「指纹可分同族隔代 vs 不同族」 |
| **N-18** | 能力装入路径 | coze N-03 L323 | Q1✓ V3 资产面无训练曲线，但可用 prompt-template / 装饰格式作 proxy；Q2✓ 实验可设计（窄化）；Q3✓ 证伪「能力可被上下文装入 vs 必须训练装入」 |
| **N-19** | 评测参照同源污染 | coze N-04 L335 | Q1✓ coze 自报「396/396 来源标签全部 kimi_api」现成；Q2✓ 评测参照的来源审计可设计；Q3✓ 证伪「评测结论 ≠ 教师自评」 |
| **N-20** | 指纹对原始制品的依赖 | coze N-05 L349 | Q1✓ 22 caption + 5 by_model 现成；Q2✓ 指纹 vs 原始制品存活性比较可设计；Q3✓ 证伪「指纹可独立于原始制品存活」 |
| **N-21** | 语义指纹链派生证据 | coze N-06 L361 | Q1✓ append-only 链现成；Q2✓ 派生证据哈希链实验可设计；Q3✓ 证伪「派生证据可被伪造」 |
| **N-22** | 独立核验定位失败 | coze N-07 L373 | Q1✓ V1–V3 资产栈现成；Q2✓ 「找不到」vs「没痕迹」可证伪实验；Q3✓ 证伪「独立核验可区分两者」 |

## §4 V4 §4 修订建议集（PI 复核裁入 V4 §4 开放问题 10 条）

| 编号 | 修订建议 | 原提议方 | 核心准则理由（三问） |
|---|---|---|---|
| **§4-OQ-1** | V4 mode-set 表与 reverse-attribution 表自诞生即计算 SHA-12，沿用冻结资产锚定规约（V4 自有、独立路径） | kimi_t12 R9 + trae_code D-4 | Q1✓ V4 自有表锚定可完成；Q2✓ SHA-12 + append-only 链可设计；Q3✓ 证伪「表被修改后 SHA-12 不可检出」 |
| **§4-OQ-2** | V1–V3 资产栈是否含学生侧 = §4 第八项明示 | mavis (d) L196 | Q1✓§4 第八项追加可完成；Q2✓ 栈规模声明可设计；Q3✓ 证伪「栈内学生侧样本存在」 |
| **§4-OQ-3** | 已坐实不稳健读数不得作下游前提 + 由谁来执行 | workbuddy (d) L134 | Q1✓§4 追加自律条款可完成；Q2✓ 自律 + 执行主体可设计；Q3✓ 证伪「自律条款可被绕过」 |
| **§4-OQ-4** | 单侧失效结构（盘上三处单侧失效是否同一结构） | workbuddy_brainstorm (d) L100 | Q1✓§4 追加 §2.5 续问可完成；Q2✓ 结构判定实验可设计；Q3✓ 证伪「三处同构」 |
| **§4-OQ-5** | 跨厂商统计分母独立侧数声明 | trae_work (d) L139 | Q1✓§4 加跨厂商分母声明可完成；Q2✓ 独立侧数可证可设计；Q3✓ 证伪「分母不可独立验证」 |
| **§4-OQ-6** | 五件面板零模型归因率 | trae_code (d) L79 | Q1✓§4 加 zero-model attribution 校准可完成；Q2✓ 零模型 baseline 可设计；Q3✓ 证伪「零模型归因率 > 实测 FPR」 |
| **§4-OQ-7** | 12 个月再可核 + 锚移动处置 | claude_code (d) L176 | Q1✓§4 加时效声明可完成；Q2✓ 时效 + 处置可设计；Q3✓ 证伪「V4 主张时效独立」 |
| **§4-OQ-8** | 学习史不可区分问题 | codex_brainstorm (d) L39 | Q1✓§4 加学习史可观察性声明可完成；Q2✓ 不可区分实验可设计；Q3✓ 证伪「学习史可由观察区分」 |
| **§4-OQ-9** | §7.2 范围列与问句不匹配（workbuddy Track 1 输出当 Track 3 问） | workbuddy §7.2 L133 | Q1✓§7.2 范围纠正可完成；Q2✓ 范围重声明可设计；Q3✓ 证伪「V4 委托方对自身贡献归属无歧义」 |
| **§4-OQ-10** | 保序恒等式作为伪影源 | coze (d) L457 | Q1✓§4 加「多处一致不证明独立」声明可完成；Q2✓ Spearman=1.0 检验可设计；Q3✓ 证伪「Spearman=1.0 ≠ 独立」 |

## §5 D1 action items 对应本会话语境

| 编号 | codex D1 提议 | 本会话对应 |
|---|---|---|
| D1-1 | 确认实际冻结清单与 artifact-to-backbone-to-cell 映射 | §4.5 已拍 C7 锚修订 + 别名表已生效（按层-名映射） |
| D1-2 | 注册 Track 1 density/matching 规格与 dependency-aware split | §1.1.1 代拟稿已含 R3 排列检验 + kimi_t12 R1 lineage 去重 + ide_track B3 估计器冻结 |
| D1-3 | 选 1 个 Track 2 candidate 类型、源标签、基线、弃答规则 | §1.1.1 代拟稿 JS 主度量 + R6 负对照校准 τ + R7 margin GRAY |
| D1-4 | V3 final R5 manifest SHA-12 占位校验 | §1.2.5 别名表已记 V7–R5 关系待 PI 补注（沿「不在此推断」原则） |
| D1-5 | D3 前 PI 批准/替换 Track 3 提议 | §3.1 自定义「V3的剑不斩V4的官」+ §3.2 路径 B + §1.2.9 PI 自定 |

---

## §6 汇总统计（17 件 292 条全景）

| 维度 | productive | blocking | 沿已拍板口径收口 |
|---|---|---|---|
| 实验提议 / 方法建议 | 102 | 3 | blocking 3 条的复评条件已写 |
| 修正建议 | 77 | 0 | — |
| 判定意见 | 24 | 0 | 7 条种子多回函投票聚合已落 §2.3 |
| 风险报告 | 49 | 0 | 全作警示条件入实验轮廓 / §3.7/§3.8 |
| 待决项 / 开放问题 | 28 | 0 | 14 条新增种子 + 10 条 §4 修订建议 + 5 条 D1 action items |
| 反驳指控 | 9 | 0 | 全作 §3.3/§3.7/§3.8 反向支撑 |
| **总计** | **289** | **3** | 17 件 292 条全收 |

> **结构性观察**：§2.10（35 条）+ §3.x 子种子（89 条）是提议密度最大的两层，前者本多对应 V4 自有资产缺位（V4 自有 manifest 可锚定），后者本多对应新种子的「GT by construction」形态（接 §1.1.1 已拍 GT 构造性声明）。

---

## §7 边界声明

本稿由 Mavis 起草（PI 2026-09-22 拍板代拟；PI 图示清单「全部 17 件」与推定清单核对一致）。起草过程 0 LLM 调用、0 外部 URL、0 GitHub/WeChat 操作、0 密钥、0 frozen 制品/schema/锚文件触动；292 条提议逐条对照 explore 报告原文摘录与行号；判定沿核心准则三问 + 结构性修正三问；上轮已生效件（种子稿/术语稿/实验稿/别名表）以实读现存 v1.1 问卷 `07CA9EE8E1BB` 为依据。**PI 已复核通过，已生效**（PI 2026-09-22，问卷 ask_e9ad9dddbb20cbd53f2d96bf）；问卷回填在 §1.2.x / §2.x / §4.x 决策点后续执行。问卷本体仍为权威。

---

## §8 待 PI 复核决定项（落盘后回填面）

1. **新增 14 种是否裁入 V4 修订种子场**：全部落 Dim 6（已 In-scope）还是分维散入 Dim 1–7？
2. **§4 修订 10 条是否全入 V4 §4 开放问题**：全部接受、按主题合并、还是分批推入？
3. **blocking 3 条的复评条件**：是否全部进种子稿「复评条件」注记栏？
4. **判定意见 24 条的多回函投票聚合结果**：S-36/S-17/S-15/S-38 productive 强化、S-29/S-14/S-32 non-productive 强化——是否直接落种子稿边界声明 2？
5. **D1 action items 5 项是否回填 §4.x**：明文已逐项指代本会话沿用件，是否全部采纳？