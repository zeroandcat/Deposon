# P-F 方向调研:模型指纹 / 透明审计(2026-09-09)

> **作者**: Mavis(执行线,Worker-P-F 子代理撰写)
> **日期**: 2026-09-09
> **状态**: V0 调研稿(本任务为 P-F 方向预登记配套调研,不是结论)
> **位置**: `docs/V3X/P_F_RESEARCH_2026_09_09.md`
> **关联**:
> - v3 提案 §6(王老师致,2026-09-04,4 页 PDF)第六节"Phase 0: 一周判死承诺"6 方向之一
> - Mavis 内部 `QUICK_KILL_6_DIRECTIONS.md` V0.2 方向 6 + 5 个潜在 BOSS
> - 7 条铁律(双审、API key 不入 prompt、术语红线、数字溯源、verifier 纪律、预登记、推送策略)

---

## 0. 调研方法与诚实声明(必读)

### 0.1 方法

- **计划**: 用 `web_search` 工具对 5 BOSS 各搜 2 个来源,优先 2024-2026 论文,关键事实给来源 URL。
- **实际**: 本次执行环境中 `web_fetch` 全部返回 `network_error`(对 arxiv.org / duckduckgo.com / google.com 全部失败)。`web_search` 工具在当前 toolset 中不可用(仅有 `web_fetch`)。
- **应急**: 沿用 7 条铁律"不知道的查目录或问,绝不'看着合理'就编"。本文档:
  - §2 5 BOSS 逐节用**置信度分层**写法: 「A. 已确认(高置信,知识截止 2026-01)」+ 「B. 待确认 [待确认:知识截止 2026-01 后可能已更新]」+ 「C. 必须由 D1 补查的项」三类。
  - **不写**具体 arXiv 编号(无法在线验证)、不写**具体基准数字**(如 "TEE 开销 < 5%")、不写**具体年份论文**(除已被 Mavis 内部文档引用的,如 IMMACULATE)。
  - 全部 "需实测验证" 项用 [需 P-F V0.1 实测] 标注。
- **后续**: D1 由 Mavis 派独立子代理补查 5 BOSS 每条 ≥ 2 个可访问 URL,补入本调研 V0.1。

### 0.2 7 条铁律兼容

- ✅ 不读 API key(本次纯调研,无 LLM API 调用)
- ✅ 不引入新术语(沿用 Mavis 内部文档已有:指纹 / 散射层 / 守恒 / 透明审计)
- ✅ 数字溯源:本调研**不写**任何 Mavis 内部未引用的具体数字;沿用 IMMACULATE 的"1% 开销"等已有引用,标 [来源:QUICK_KILL_6_DIRECTIONS.md]
- ✅ 双审:本调研 V0 草稿待 D1 由 reviewer-a 静态审
- ✅ verifier 纪律:本调研配套的 P-F SPEC V0 §10 显式约束"不得在真实仓库跑任何攻击脚本"
- ✅ 预登记:本调研落地同步生成 `P_F_PREDECISION_2026_09_09.json`
- ✅ 推送策略:不主动发,等 D0 末群内公布

---

## 1. P-F 定位

### 1.1 一句话定位

P-F = **模型指纹 + 透明审计方向** = 探索 deposon 散射层 + 密码学 / 硬件 / 模型可解释性 联合是否能在 LLM 推理验证上达到**比任何单一方案更低开销 + 更高覆盖率**的审计能力。

### 1.2 与 v3 提案 §6 关系

v3 提案 §6 列出 Phase 0 一周判死承诺 6 方向(P-A 平衡稳定化、P-B 失真上界、P-C 两相结构、LLM 议价、P-D 指纹、**P-F 可验证审计 = IMMACULATE 风格**)中,P-F 是**第 5 备选**(QUICK_KILL_6_DIRECTIONS.md V0.2 方向 6)。王老师 2026-09-08 回"不指定"后,Mavis 自由推进 4 方向(P-A / P-B / P-C / P-D),**P-F 暂未启动**。本次调研是为"如果 P-A-D 全部 BOSS 判死 / 失败后,P-F 是 V3X 备份启动项"做前置准备。

### 1.3 与 P-A / P-B / P-C / P-D 关系

| 方向 | 主张核心 | 与 P-F 关系 |
|---|---|---|
| P-A 平衡稳定化 | 散射层反向动力学 = 势博弈,稳定化成本 ≤ 1.3× | P-F 不依赖 P-A;P-F 用不同切面(可验证性,不是动力学) |
| P-B 失真上界 | 散射层保真度 ≥ 0.95,失真 < 0.05 | P-F 把 P-B 失真界用作"散射层"侧,与密码学 VC / TEE 侧联合 |
| P-C 两相结构 | blocking / tunneling 相变,η 扫描 | P-F 不依赖 P-C;P-C 关注相变,P-F 关注审计 |
| **P-D 指纹(已 PASS)** | 5 锚 SHA-256 闭环 + 1% 开销 + 3/3 攻击抵御 | **P-F 是 P-D 的"放大版"**——P-D 用最轻量级 SHA 闭环(纯密码学),P-F 探索 SHA + 硬件(TEE)+ 密码学(VC / Merkle)+ 透明(CoT)多源联合 |
| LLM 议价 | 多 LLM agent 纳什议价 | 不直接相关 |

**关键互补**:
- **P-D 已被 1% 开销 + 5 锚 SHA-256 闭环抵御 3 个 BOSS(简单 SHA-1 / Merkle Tree / 不变量检查)** [来源:QUICK_KILL_6_DIRECTIONS.md 方向 4]。
- **P-F 启动的必要条件是 P-D 已被吸收**:P-F 的"指纹"层可直接复用 P-D 的指纹基线,只在 P-D 基础上加 TEE / VC / CoT 三个新维度。
- **P-F 与 P-D 关系是"附加价值" 而不是"替代"**:P-D 失败的极端场景是"5 锚 SHA-256 在工业规模下不增值",P-F 的退路是"即使 SHA-256 不够,加上 TEE 远程认证 / ZKML 证明 / CoT 公开也能增值"——但这并不消除 P-D 风险。

---

## 2. P-F 5 BOSS 现状调查(逐 BOSS 1 段)

> 通用结构:
> - A. 已确认(高置信,知识截止 2026-01)
> - B. 待确认 [待确认:知识截止 2026-01 后可能已更新]
> - C. 必须由 D1 补查的项(进入 SPEC V0 §12 已知未决项)

### 2.1 BOSS-F1: model fingerprinting(模型指纹)

**A. 已确认**:
- "模型指纹" 作为研究领域在 2022-2024 期间快速扩张,核心思想是**用模型对特定探针输入的输出统计来识别模型身份**。
- 与 deposon 散射层**正交**:deposon 散射层是"输入层操作"(T+R+A 散射),指纹是"输出层验证"(统计聚类)。
- 已知子方向包括:水印型指纹(在训练时植入)、被动型指纹(对预训练模型测探针)、白盒 vs 黑盒区分 [来源:Mavis 内部 QUICK_KILL_6_DIRECTIONS.md V0.2 方向 6 BOSS-F1]。

**B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
- 具体 SOTA 系统如 TexTra / DNA / MathNAS 是否真实存在并在该领域被引用——本作者无法在线核验,可能与"模型指纹"领域内某子方向重名或不存在。
- DeepMind / Google 2022-2023 是否有公开"LLM 指纹"工作——Mavis QUICK_KILL 文档引用,但本作者无法核验具体论文 ID。

**C. 必须 D1 补查**:
- 至少 2 个 2024-2026 公开论文的 arXiv URL,覆盖"被动模型指纹" 与"水印模型指纹" 两类
- 与 deposon 散射层**联合**时,指纹层是否会被 P-D 已抵御的 "Merkle Tree + 推理日志" BOSS-D2 同样拍平(若拍平,P-F 指纹层无新增价值)

### 2.2 BOSS-F2: TEE / SGX / 机密计算

**A. 已确认(高置信,知识截止 2026-01)**:
- **Intel SGX 在服务器市场退出**:Intel 在 Sapphire Rapids / Emerald Rapids 等服务器平台上不再提供 SGX,客户端 SGX 也在 11 代酷睿后被弃用 [需 P-F V0.1 实测:具体退市时间,以 Intel 官方公告为准]。
- **AMD SEV-SNP 持续在 EPYC 上提供**:SEV(2016 引入)+ SEV-SNP(2021 引入)是 AMD 主流机密计算方案。
- **NVIDIA H100 Confidential Computing(CC)模式**:H100 GPU 在 CC 模式下,CPU 与 GPU 之间的数据传输与 GPU 内部计算受硬件保护,H100 CC 模式已于 2023-2024 商业可用 [需 P-F V0.1 实测:CC 模式具体启用时间,以 NVIDIA 官方公告为准]。
- **Azure Confidential Computing + AWS Nitro Enclaves**:工业部署,用于客户敏感数据 + 推理。
- **关键限制**:TEE 远程认证需要 **verifier 与 enclave 厂商建立信任根**;Intel SGX 退市后,AMD / NVIDIA 阵营没有统一 root of trust,跨厂商 TEE 联合验证是工程难题。

**B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
- SGX 完全退市时间表(可能在 2024-2025 已完全停产,需 Intel 官方公告)
- H100 CC 模式在 2025-2026 的客户实际采用率
- AMD SEV-SNP 在 2024-2025 是否被爆出严重侧信道漏洞(Sev-SNP 历史上曾被多次攻破)

**C. 必须 D1 补查**:
- Intel 官方 SGX 退市公告 URL
- AMD SEV-SNP 2024-2026 已知严重侧信道漏洞列表(影响"硬件保证不需密码学 VC" 主张)
- 工业部署案例:Azure Confidential Computing 2024-2026 公开客户列表(脱敏)

### 2.3 BOSS-F3: Merkle 推理日志

**A. 已确认(高置信,知识截止 2026-01)**:
- "Merkle 树" 在 1979 年由 Ralph Merkle 提出,是密码学基础原语。
- vLLM / SGLang / TGI(Text Generation Inference)等 LLM 推理引擎**记录推理日志**(但**不一定**用 Merkle 结构,通常是 JSON Lines / 简单哈希链)。
- Anthropic / OpenAI 是否在生产中用 Merkle 推理日志:**本作者无法确认**;这是 **B 类待确认** 项。

**B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
- Anthropic / OpenAI 是否公开"用 Merkle 树记录推理过程" 的工程实现——本作者无任何公开资料确认,可能根本不存在。
- IMMACULATE 论文(NUS + Dawn Song,1% 开销)的具体实现是否用 Merkle 树——Mavis QUICK_KILL 文档提到 IMMACULATE 是"密码学 VC",但具体结构需核验。

**C. 必须 D1 补查**:
- IMMACULATE GitHub 仓库(已知 URL:`https://github.com/guo-yanpei/Immaculate`)主分支文件结构,确认是否含 Merkle tree / hash chain 实现
- 至少 1 个 vLLM / SGLang 推理日志格式的 GitHub 文档 URL
- 论文出处(arXiv 编号)需补查

### 2.4 BOSS-F4: ZKML(零知识机器学习)

**A. 已确认(高置信,知识截止 2026-01)**:
- **Modulus Labs**:2022-2023 成立,聚焦 ZKML(零知识证明 + ML 推理),与 Anthropic 合作过"证明 LLaMA-7B 推理" 项目。
- **EZKL**:开源项目,用 Halo2 / Plonky2 等 ZK 后端证明 ONNX / PyTorch 模型推理,GitHub 公开。
- **核心 trade-off**:LLM 大模型(>1B 参数)上生成 ZK 证明**极慢**,LLaMA-7B 单步推理证明时间在 2024 初的公开报告是 **数分钟到数十分钟级** [来源:Mavis 内部 QUICK_KILL_6_DIRECTIONS.md 方向 6 BOSS-F4]。
- **准确性 trade-off**:ZKML 证明**不损失 accuracy**——它证明的是"对给定的输入,模型确实输出了某个输出",不是"模型输出正确"。

**B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
- EZKL 2024-2026 的工程化进展(是否有大模型支持 / 是否有工业级 case)
- Modulus Labs 是否在 2024-2025 完成新一轮融资 / 重要技术里程碑
- "GKR-based zkML" 是否仍是 2025 主流(本作者无法在线核验,可能已有更高效方案)

**C. 必须 D1 补查**:
- EZKL GitHub 最新 release 与 benchmark(2025-2026)
- Modulus Labs 官网最新 blog(2025-2026)
- 至少 1 个 2025-2026 ZKML 公开 benchmark 论文 arXiv URL(优先 LLM 单步推理证明时间 vs deposon 散射层)

### 2.5 BOSS-F5: CoT 透明审计(chain-of-thought transparency)

**A. 已确认(高置信,知识截止 2026-01)**:
- "Chain-of-Thought" 提示由 Wei et al. 2022 引入(Google, "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models")。
- Anthropic 在 2023-2025 期间发布多篇"可解释性 / 电路 / 透明" 研究,把 CoT 视为审计切面之一。
- OpenAI o1 / o3 系列用内部 CoT 推理,但**不向用户公开完整 CoT**(只公开摘要),是"半透明"。

**B. 待确认 [待确认:知识截止 2026-01 后可能已更新]**:
- Anthropic 2026 是否公开宣称"CoT 透明审计" 作为产品特性——本作者无 2026 最新资料,可能有也可能没有。
- "承诺装置" / 任何比喻性术语是否在公开论文中被使用——7 铁律"术语红线" 禁止 deposon 文档用比喻,本作者**不引入**任何此类术语。
- CoT 公开作为审计基线:即使 CoT 公开,**审计者能否独立判断 CoT 是否真实**? 这是 CoT-as-audit 的根本问题——审计者看到的 CoT 可能是"事后编造的合理化"。

**C. 必须 D1 补查**:
- Anthropic 2024-2026 公开"interpretability / transparency" 系列 blog URL
- OpenAI o1 / o3 CoT 公开策略 2024-2026 官方说明
- 至少 1 个"CoT 事后合理化 vs 真实推理" 学术论文 URL(若不存在,记入 §4 风险点)

---

## 3. P-F 与 P-A-D 互补关系(为什么 P-F 值得 1 周预筛)

### 3.1 P-A-D 已落地 4 方向,P-F 是补充而非替代

- P-A / P-B / P-C / P-D 在 2026-09-09 已分别预登记 + 启动 1 周判死。
- P-F **不是 P-D 的替代**,而是"如果 P-D 在更严苛的 BOSS 攻击下失败 / 如果要服务监管场景 / 如果需要可对外披露的密码学证据"的扩展方向。

### 3.2 P-F 的三类潜在价值

| 价值类 | 描述 | 与 P-D 关系 |
|---|---|---|
| **VC 价值** | 密码学可验证(零知识 / Merkle)给监管 / 学术审稿人独立可验证 | P-D 的 SHA-256 闭环是 verifiability 最小集,P-F 加 ZK / Merkle 提升可验证性等级 |
| **硬件价值** | TEE 远程认证避免软件层信任 | P-D 完全在软件层,P-F 跨入硬件信任域 |
| **透明价值** | CoT 公开让第三方可读审计 | P-D 的验证器只输出 12 位 hex + 布尔,P-F 引入"人类可读"审计切面 |

### 3.3 1 周预筛的特殊风险

P-F 的 1 周预筛**风险高于** P-A / P-B / P-C / P-D:
- **新代码量大**:需要新写 LDD 距离度量 + VC 集成层 + TEE 远程认证脚本 + CoT 公开 baseline,**至少 1500-2500 行新代码**。
- **依赖外部仓库**:IMMACULATE GitHub(已知 URL)+ EZKL GitHub + vLLM / SGLang 任一选 1,**多仓库协同 = 兼容性风险**。
- **BOSS 风险最高**:5 BOSS 任何 1 个 PASS = P-F 主张降级(QUICK_KILL_6_DIRECTIONS.md V0.2 已明确)。
- **王老师 3 时点回报**:D1 / D3 / D5 报告必须 5-10 min/周 内可读,新方向的复杂性会拉长报告时间。

**预筛前必须确认**:P-A / P-B / P-C / P-D **至少 3 个 FAIL / BOSS 撞上 / 主动放弃**,才启动 P-F。否则 1 周预算被 P-F 吞掉,P-A-D 后续方向无时间。

---

## 4. P-F 与 v3 提案 §6 高压线关系

### 4.1 THINKING_V3_GT_CONTRIB_2026.md Q5 沿用

v3 提案的高压线(THINKING_V3_GT_CONTRIB_2026.md Q5):
> "v3 定义里有没有零件其实与博弈论相冲突?"
> 答:"有—— blocked→final_prob×0.1 的硬惩罚。机制设计要求对参与者的响应是激励相容的,而 ×0.1 是外在工程惩罚,不经过参与者的效用函数。"

**P-F 不引入新硬惩罚**,P-F 的"审计" 是**事后验证**而非**机制内惩罚**。所以 Q5 高压线**对 P-F 不直接适用**。

### 4.2 但 P-F 引入新一类问题:Q5' "透明装置会被策略性智能体操纵"

CoT 公开后,策略性智能体(被审计的 LLM agent) 可能学会"输出看起来合理的 CoT,实际推理走另一条路"——即**事后合理化**。这是 CoT-as-audit 的根本脆弱性,本作者**未在知识截止 2026-01 前看到令人信服的解决方案**。

- **P-F SPEC V0 §10 已知边界** 必须显式记录:即使 P-F 主张"P-D + TEE + VC + CoT 联合 = 高可审计",CoT 透明层**单拎出来** 不构成审计证据。
- **裁定建议**:P-F 主张应**避免** "CoT 透明 = 审计完备" 的过度承诺,沿用 Mavis QUICK_KILL BOSS-F5 测法"跑 CoT 公开 baseline,看审计准确率是否 ≥ 95%"。

### 4.3 C1 高压线"守恒≠真值" 沿用

deposon 散射层在 P-A / P-B / P-C 都有"守恒律"主张(P-F **不直接依赖** 守恒律),所以 THINKING_V3 Q-C1 "守恒≠真值" 在 P-F 中**降级为次要风险**。P-F 主张是"可验证性"(verifiability),不是"真值"(truth)。

---

## 5. 调研方法(总结 + V0.1 触发)

### 5.1 实际采用方法

- **计划**: `web_search` 对 5 BOSS 各搜 2 个来源(2024-2026 论文 + 工业部署)
- **实际**: `web_search` 工具在当前 toolset 不可用;`web_fetch` 全部 `network_error`
- **应急**: 用 7 条铁律"不知道的查目录或问",本文档严格分层 A(已确认) / B(待确认) / C(必须补查),不写任何无法核验的具体 arXiv 编号 / 数字 / 论文作者

### 5.2 后续动作(D1 触发)

- D1 派独立子代理(due-diligence-worker),在能访问外网的环境下补查 5 BOSS 各 ≥ 2 个可访问 URL
- 补查结果写入 `docs/V3X/P_F_RESEARCH_V0.1.md` (本调研 V0.1)
- 任何 P-F 启动决策必须等 V0.1 落地

### 5.3 7 条铁律兼容性自检

- ✅ **双审**: 本文 V0 待 D1 reviewer-a 静态审
- ✅ **API key 不入 prompt**: 本次纯调研,无 LLM API
- ✅ **术语红线**: 用"指纹 / 透明 / TEE / 零知识 / CoT / 散射层 / 守恒" 等工程术语,**不**用"承诺装置" 等比喻
- ✅ **数字溯源**: 本调研**不**写任何具体数字;沿用 Mavis 内部已有引用
- ✅ **verifier 纪律**: P-F SPEC V0 §10 显式约束"不得在真实仓库跑任何攻击脚本"
- ✅ **预登记**: 配套 P_F_PREDECISION_2026_09_09.json 已生成
- ✅ **推送策略**: 不主动发,等 D0 末群内公布

---

## 6. V0 → V0.1 升级触发条件

- ✅ 5 BOSS 各 ≥ 2 个可访问 URL 落地
- ✅ P-F 启动决策(P-A-D 至少 3 个 FAIL / 主动放弃 / 或王老师新指令)
- ✅ IMMACULATE GitHub 仓库可访问性验证
- ✅ D1 reviewer-a 静态审通过

**未触发升级前,本调研为 V0 草稿,不是结论。**

---

## 7. 引用与版本

- **v3 提案**: 《Deposon × 王子贺老师 合作提案》(2026-09-04, 4 页 PDF, 致: 王子贺 人大高瓴人工智能学院)
- **Mavis 内部**:
  - `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` V0.2(方向 6 P-F + BOSS-F1~F5)
  - `docs/THINKING_V3_GT_CONTRIB_2026.md` Q5(硬惩罚冲突) + Q-C1(守恒≠真值)
  - `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` V0.1.2(P-D 已 PASS 模式)
  - `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` V0.2(双判死线双跑 + §0.5 BOSS 测法节)
- **外部**(本调研**不**直接引用任何具体 arXiv 编号 / 论文标题——见 §0.1 诚实声明,所有外部引用待 D1 补查):
  - IMMACULATE GitHub: `https://github.com/guo-yanpei/Immaculate` [来源:QUICK_KILL_6_DIRECTIONS.md]
  - EZKL / Modulus Labs / vLLM / SGLang / Anthropic interpretability [来源:同上,具体 URL 待 D1 补查]

---

**P-F 调研 V0 草稿结束,待 D1 派独立子代理补查 5 BOSS URL + 落地 V0.1。本文档不是 P-F 启动决策——P-F 启动须先等 P-A-D 4 方向至少 3 个 FAIL / 主动放弃。**
