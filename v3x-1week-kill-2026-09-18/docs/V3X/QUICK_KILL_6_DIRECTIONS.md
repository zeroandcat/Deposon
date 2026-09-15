# V3.X 6 方向 Quick-Kill 模板(防 BOSS 突袭判死)

> **背景**: 王老师不指定挂点。用户希望"先调研后开工,防突然出现 BOSS 来判死"。
> **重要概念 — BOSS 的定义**: **BOSS = 竞品拍平算法 = 用低成本方法把 deposon 主张拍平**。V1 V1~V2 论文已经撞过一个 BOSS: **六关键词规则过滤器** (six-keyword rule filter) 在 GSM8K / StrategyQA 上与 deposon 散射层 accuracy 不可区分 (0.87 vs 0.85, 0.899 = 0.899),把"散射层筛选性能优于平凡基线"的主张降级为 0(论文 V1 §2.4 报告)。论文 V1 因此把主张精确化为"差异价值只在机器可核验性"。**V3X 任何方向都必须预先识别潜在 BOSS,1 周判死时主动测 BOSS 是否再次出现**。
> **本文档目的**: 6 个候选方向各自给出 1 句 spec + 1 句 BOSS 预判 + 1 句判死线 + 1 句 verdict 模板, BOSS 来时 5 分钟内出判死结果。
> **状态**: V0.2(2026-09-09,加每方向 BOSS 列表)
> **位置**: `docs/V3X/QUICK_KILL_6_DIRECTIONS.md`
> **更新**: V0.1 → V0.2 增加 6 个方向的"潜在 BOSS 列表"(V0.1 只在文档头说"BOSS = 竞品拍平算法",没逐方向列出)

---

## 通用约束(所有方向共享)

- 7 条铁律: 双审、API key 不入 prompt、术语红线、数字溯源、verifier 纪律、预登记、推送策略
- 1 周判死模式: 1 个方向 PASS/FAIL 后再开下一个
- 数据集: 100-200 节点起步(1 周内跑完)
- 钥匙安全: runtime `Path().read_text()`,永不落盘
- API 沿用之前(同 KIMI/GLM 鉴权),只换模型 ID
- 王老师 = WeChat 顾问(等他回,不主动推)

---

## 方向 1: P-A 平衡稳定化(博弈论转向 — 已知主线)

- **1 句 spec**: deposon 散射层的反向动力学 = 节点-图上的势博弈,验证 P-A 主张(平衡点稳定,审计标量单调)。
- **1 句判死线**: 200 节点 22 受控概念图上,审计标量单调 GT-5b ≥ 22/22 + 残余中位 < 1e-29 + 势近似判死 GT_FORMAL 闭合(已预登记)。
- **1 句 verdict 模板**: "P-A 在 100-200 节点 22 图上 GT-5b X/22 单调、GT-6 残余中位 Y、GT_FORMAL 闭合/未闭合 → PASS/FAIL"。
- **预期**: 大概率 PASS(论文 v2 已含数据);风险是 Trae 优化时引入 race condition。
- **资源**: V3X 已有 P-D PASS 模式,直接复用 spec/impl/attack 模板。
- **潜在 BOSS 列表**(V3X 启动后 1 周内必跑,防 V1 六关键词规则重演):
  - **BOSS-A1**: 简单势博弈算法(Repeated Best Response / Regret Matching, Hart & Mas-Colell 2000)→ 不需要 deposon 散射层就能在 22 节点上单调收敛 → deposon 平衡点"无差异化"。**测法**: 同样的 22 受控概念图,直接跑 RBR/RM,看 GT-5b 单调性是否依然 ≥ 22/22。如是 → 主张降级为"工程化系统"。
  - **BOSS-A2**: 经典 Potential Game 理论(Monderer & Shapley 1996) → 直接给出 GT-5b 单调性证明,deposon 散射层是包装。**测法**: 不跑 deposon,直接在势博弈框架下证明 P-A 主张 → 如能证明,deposon 散射层"无新增理论价值"。
  - **BOSS-A3**: Replicator Dynamics 单纯形 + 进化稳定策略(ESS, Smith 1973 / Taylor & Nowak 2006)→ 在 22 节点小图上,任意两策略博弈都会收敛到 ESS, deposon 无差异化。**测法**: 用 Replicator Dynamics 跑 22 图,看 ESS 点是否与 deposon 平衡点重合。如重合 → 主张被拍平。

## 方向 2: P-B 失真上界(博弈论转向 — 已知主线)

- **1 句 spec**: deposon 散射层保真度 = 输入路径到输出路径的失真上界,以相对熵或 L2 度量。
- **1 句判死线**: 200 节点 v19 冻结管线保真度 ≥ 0.95,失真上界 1-真实分布。
- **1 句 verdict 模板**: "P-B 失真上界 = X(200 节点平均),< 0.05 → PASS;否则 FAIL"。
- **预期**: 中等概率 PASS,需 V3X 实际跑。
- **资源**: 沿用 P-D 测试基础设施。
- **潜在 BOSS 列表**:
  - **BOSS-B1**: 经典 Optimal Transport / Wasserstein distance (Cuturi 2013, Sinkhorn) → 已经在 LLM 推理优化里被广泛用, deposon 散射层"无新增信息"。**测法**: 同样 200 节点 v19 数据,直接跑 Sinkhorn OT,看保真度是否也 ≥ 0.95。如是 → 失真上界不特殊。
  - **BOSS-B2**: KL 散度 + softmax 平滑(Knowledge Distillation, Hinton 2015) → 200 节点上保真度 0.95 是这类工作的默认下限。**测法**: KD baseline,看 0.95 是否是默认下限。如是 → deposon 失真上界无差异化。
  - **BOSS-B3**: 简单提示词压缩(LLMLingua, Microsoft 2023 / LLMLingua-2) → 200 节点上失真上界 < 0.05 已经是教科书水平。**测法**: 跑 LLMLingua 压缩 prompt 到同样保留率,看失真是否 < 0.05。如是 → 主张被拍平。

## 方向 3: P-C 两相结构(博弈论转向 — 已知主线)

- **1 句 spec**: deposon 散射层两极限态 v1 blocking + v2 tunneling 之间有相变,η = g_aether/g_couple 在临界值处行为相变。
- **1 句判死线**: η 扫描 0.01-100,相变点位置在理论预言 ± 20% 内,平均耗散曲线在 blocking/tunneling/中间三态符合理论。
- **1 句 verdict 模板**: "P-C 相变点在 η = X,理论预言 Y,相对偏差 Z% → PASS/FAIL"。
- **预期**: 中等概率 PASS,需要新实现 η 扫描脚本。
- **资源**: 沿用 v19 冻结 JSON,新增 η 扫描 harness。
- **潜在 BOSS 列表**:
  - **BOSS-C1**: 经典相变理论(2D Ising 模型临界指数 β=1/8) → η 扫描的相变点位置和临界行为完全可由 Ising 普适类预测。**测法**: 用经典 2D Ising universality class 预测相变点,看 deposon 实测相变点是否在理论 ± 20% 内 → 如是,deposon 散射层与 Ising 行为一致,无新增信息。
  - **BOSS-C2**: Quantum Phase Transition 在 transverse field Ising 模型中已被研究透了(Sachdev 1999) → v1 blocking / v2 tunneling 二相在文献中是已知量子相变。**测法**: 引用 Sachdev 教科书,直接把 v1 ↔ v2 映射到 transverse field g ↔ J 比 → 如映射成立,deposon 散射层"无新物理"。
  - **BOSS-C3**: Reservoir Computing + 调谐参数(临界点附近,Jaeger & Haas 2004) → 任何含可调参数的双稳态系统都展示相变, deposon 散射层不特殊。**测法**: 用 echo state network + 调参数,看是否也展示 v1 ↔ v2 行为切换 → 如是,deposon 散射层被拍平为通用双稳态。

## 方向 4: P-D 指纹(已 PASS,接近收尾)

- **1 句 spec**: 内容寻址 + Manifest + 根指纹 + 追加链 + 验证器安全边界(5 锚 SHA-256 闭环)。
- **1 句判死线**: 5 锚 SHA-256 复现 + 3/3 攻击脚本 PASS + A1 CLI 衔接 P1 修(若未修则 FAIL)。
- **1 句 verdict 模板**: "P-D 5 锚 SHA-256 复现 + 3/3 攻击 PASS + A1 CLI 衔接 P1 修(已 Trae 优化) → PASS/FAIL"。
- **预期**: **PASS**(Trae V0.1.2 已优化,根指纹 7d6d3d39fad8 复现,5 锚 SHA-256 全 PASS)。
- **资源**: 现有 `fingerprint_v0.py` + 6 tests + 3 attacks,直接复跑。
- **潜在 BOSS 列表**(P-D 已 PASS,这些 BOSS 已被 1% 开销 + 5 锚 SHA-256 闭环抵御,**保留作为复跑核查项**):
  - **BOSS-D1**: Git 自身 SHA-1 内容寻址 → deposon 指纹不增值。**抵御证据**: P-D 不只是 SHA-1 哈希,还有"验证器安全边界"(Merkle-like 验证器状态机),Git 自身不验证推理计算图。复跑时核查: 验证 5 锚 SHA-256 是否覆盖到验证器状态转移 + 中间推理节点,而不是仅仓库根。
  - **BOSS-D2**: 简单 Merkle Tree + 哈希链 → 不需要 deposon 也能搭出来。**抵御证据**: P-D 有"追加链"(append-only chain with cryptographic sequence),单纯 Merkle 树做不到,必须用 deposon 散射层生成的序列号。复跑时核查: 攻击脚本 A1 试图重放历史节点,验证器能否拒绝(预期拒绝)。
  - **BOSS-D3**: 不变量检查(invariant checking) → 任何 LLM 推理框架都能加。**抵御证据**: P-D 1% 开销指标(在标准 LLM 推理管线中增量 1% 性能) 优于"全量不变量检查"(典型 10-20% 开销)。复跑时核查: 实测端到端延迟增量是否 ≤ 1.5%。

## 方向 5: LLM 议价(博弈论转向 — 已知主线)

- **1 句 spec**: 多 LLM agent 在 deposon 散射层下的纳什议价 + 收益分配,验证 P-A 议价版本。
- **1 句判死线**: 2-player 纳什议价 200 节点上,deposon 散射后的收益分配符合 Shapley 值 ± 5%。
- **1 句 verdict 模板**: "LLM 议价 200 节点,deposon 散射后收益分配 vs Shapley X% 偏差 → PASS/FAIL"。
- **预期**: 中等概率 PASS,需要新实现多 LLM 议价 harness。
- **资源**: 沿用 v19 冻结管线 + 新增 LLM API harness。
- **潜在 BOSS 列表**:
  - **BOSS-L1**: 经典 Nash Bargaining Solution(NBS, Nash 1950)闭式解已知 → 2-player 纳什议价在 cooperative game theory 中是教科书内容。**测法**: 同样 200 节点数据,直接套 NBS 闭式解 (u₁ - d₁)(u₂ - d₂) → 看收益分配是否也满足 ± 5% Shapley。如是 → deposon 散射层"无新增议价机制"。
  - **BOSS-L2**: Cooperative Game Theory + Shapley Value(Shapley 1953) 已经有现成库(pyspiel, open_spiel DeepMind) → "200 节点上 ± 5% 偏差"对 Shapley 估计是默认指标。**测法**: 用 open_spiel 库直接跑 Shapley,看是否一致 → 一致则 deposon 散射层"无差异化"。
  - **BOSS-L3**: Multi-Agent RL + Nash-Q(Hu & Wellman 2003) → 已经在博弈论+RL 文献里被广泛用。**测法**: 跑 Nash-Q 200 节点,看是否收敛到与 deposon 议价相同的均衡 → 如是,deposon 散射层"无新增 RL 价值"。
  - **BOSS-L4**: LLM 群体审议(Habermas Machine, DeepMind 2024 / 其他 2025 multi-agent deliberation) → 多 LLM 协商已经不是 deposon 独家。**测法**: 跑 Habermas Machine 风格审议 harness,看群体决策质量是否在 ± 5% 内一致 → 一致则 deposon 散射层"无差异化"。

## 方向 6: P-F(新)= IMMACULATE 风格可验证审计 vs deposon 物理守恒(其他潜力方向)

- **1 句 spec**: 在 deposon 散射层 + IMMACULATE LDD(logit distance distribution)审计之间,对比 GSM8K/StrategyQA 上的 accuracy-perf-cost。deposon 用物理守恒律,IMMACULATE 用密码学 VC。
- **1 句判死线**: 100-200 节点上,deposon + IMMACULATE 联合 vs 单 deposon vs 单 IMMACULATE,在 95% CI 内 baseline 一致 → FAIL;>+5pp(任一)→ PASS。
- **1 句 verdict 模板**: "P-F GSM8K X% (CI ± Y),StrategyQA Z% (CI ± W),deposon 物理 + IMMACULATE VC 联合 vs 单 deposon 单 IMMACULATE 偏差 <5pp → FAIL;>+5pp → PASS"。
- **预期**: 中等概率 PASS,但**风险高**(新方向,需新代码 + IMMACULATE GitHub 集成)。
- **资源**: 
  - IMMACULATE GitHub: https://github.com/guo-yanpei/Immaculate
  - deposon 现有 v19 冻结管线
  - 需要新写 LDD 距离度量 + VC 集成层
- **潜在 BOSS 列表**(P-F 是新方向,BOSS 风险最高,必跑):
  - **BOSS-F1**: 简单 model fingerprinting(DeepMind 2022 model fingerprinting / Google 2023 LLM 指纹) → 1% 开销的可验证审计可能已经被其他轻量级指纹方法覆盖。**测法**: 跑 model fingerprinting baseline,看是否也能在 1% 开销内完成 95% 准确率审计 → 如是,IMMACULATE + deposon 联合方案"无差异化"。
  - **BOSS-F2**: Trusted Execution Environment(TEE)/ Intel SGX / NVIDIA H100 远程认证 → 工业界已部署(微软 Azure Confidential Computing, AWS Nitro Enclaves),硬件保证不需密码学 VC。**测法**: 对比 TEE-only 方案 vs deposon + IMMACULATE 联合方案,看 accuracy-perf-cost 5pp 优势是否还在 → 如不在,联合方案"输给硬件"。
  - **BOSS-F3**: Merkle Tree + 推理日志(类似 vLLM/SGLang 现有推理日志) → 在 LLM 推理验证上与 IMMACULATE 一样能做,1% 开销不是唯一指标。**测法**: 跑 vLLM 推理日志 + 简单哈希链,看是否也满足 1% 开销 + 95% 审计率 → 如是,IMMACULATE 被拍平为"通用日志哈希"。
  - **BOSS-F4**: 零知识证明(ZKML, Modulus Labs 2023 / EZKL 2024 / GKR-based zkML) → 在可验证 LLM 推理上是直接竞品, 5pp 优势可能被 ZKML 的密码学保证吞没。**测法**: 跑 EZKL 证明 LLaMA-7B 单步推理,对比证明时间 + accuracy → 如 ZKML 证明时间 ≤ deposon+IMMACULATE 联合, 5pp 优势不足以差异化。
  - **BOSS-F5**: 简单半诚实模型审计(半透明推理 / chain-of-thought 公开) → 不需要密码学或物理守恒,直接公开 CoT 让第三方审。**测法**: 跑 CoT 公开 baseline,看审计准确率是否 ≥ 95% → 如是,deposon+IMMACULATE"输给透明 CoT"。

---

## 1 周判死排程(若 BOSS 突袭)

| Day | 任务 | 输出 |
|---|---|---|
| **Day 0(BOSS 来)** | 5 分钟内选 1 方向(用户决定) | 选定方向 spec 引用本文件 |
| **Day 1** | 沿方向 spec 重写 V0(已有 P-D P-A 等 spec 可直接套) | `docs/V3X/P_X_..._SPEC.md` |
| **Day 2-3** | 实现 + 单元测试(在 .mavis/scripts/) | impl + tests |
| **Day 4** | 派独立子代理双审(reviewer-a 静态 + reviewer-b /tmp 重跑) | 两份审查报告 |
| **Day 5-6** | 跑 100-200 节点实验 | 性能对比表 |
| **Day 7** | 判死 → 出 verdict → 报告 → 王老师 | 1 周判死结果 |

---

## BOSS 突袭快速响应流程(5 分钟)

1. BOSS 出现(WeChat/邮件)→ 用户转给我
2. 我读本文件,选 1 方向(用户拍板)
3. 立即写 `docs/V3X/P_X_..._SPEC_V0_SPEC.md`(沿用 P-D 模板,基于 quick-kill 1 句 spec)
4. 启动 1 周判死倒计时
5. 王老师照常 WeChat 通知(等他回)

---

## 历史调研(2026-09-09)

- **arXiv + GitHub 调研 11 个工作**(Step 1, 详见 FMT-059 报告)
- **关键竞品**: IMMACULATE(NUS + Dawn Song, 可验证计算审计, 1% 开销)
- **关键相关**: Game Theory LLM Agents(arXiv 2512.07462, FAIRGAME 框架)
- **deposon 框架新颖性**: 2026 公开工作无"物理守恒律 + 散射层 + T+R+A=1"完整方案
- **差异化机会**: deposon 物理守恒 vs IMMACULATE 密码学 VC 互补

## V0.1 → V0.2 升级记录(2026-09-09)

- **V0.1**: 6 方向 quick-kill 模板,只在文档头说"BOSS = 竞品拍平算法",没逐方向列出
- **V0.2**: 加 6 方向的"潜在 BOSS 列表"(共 19 个具体 BOSS,类比 V1 六关键词规则):
  - P-A: 3 个 BOSS(RBR/RM, Potential Game, Replicator Dynamics)
  - P-B: 3 个 BOSS(Sinkhorn OT, Knowledge Distillation, LLMLingua)
  - P-C: 3 个 BOSS(2D Ising universality, Transverse field Ising, Reservoir Computing)
  - P-D: 3 个 BOSS(Git SHA-1, Merkle Tree, Invariant checking) — 已抵御,作为复跑核查
  - LLM 议价: 4 个 BOSS(NBS 闭式解, Shapley Value, Nash-Q, Habermas Machine)
  - P-F (新): 5 个 BOSS(model fingerprinting, TEE/SGX, Merkle 推理日志, ZKML, CoT 透明审计)
- **触发**: 用户要求"先调研,后开工,防突然出现 BOSS 来判死",并明确 BOSS 定义
- **下次升级触发**: V3X 任何方向 1 周判死 PASS/FAIL 后,记录该方向是否真的撞到 BOSS,回写到对应 BOSS 列表作为"实测记录"

---

锚点 SHA-256[0:12] 沿用 P-D §1 5 锚(不变)。判死线以每方向"1 句 spec + 1 句判死线 + 1 句 verdict 模板"为唯一依据。

**Quick-kill 文档结束,BOSS 来时 5 分钟内可启动任何方向。**
