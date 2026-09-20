# P-A 均衡稳定化成本 V0 规范

> **版本**: V0(冻结)+ §0.5 BOSS 测法节补丁(2026-09-09 加, V0 时期无 BOSS 维度)
> **状态**: V0 主体不动,只加 §0.5 + §10 D5/D6 微调
> **位置**: `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md`

## §0.5 已知陷阱 + 本次如何避开(2026-09-09 BOSS 经验固化)

V0 主体(§1-§9)在 2026-09-09 前已冻结,2026-09-09 用户明确 BOSS = 竞品拍平算法(V1 案例: 六关键词规则过滤器在 GSM8K/StrategyQA 上把 deposon 散射层 accuracy 主张拍平到 0)。V0 必须显式预判并跑通 BOSS-A1/A2/A3 baseline,否则"deposon 散射层稳定化成本低"主张可能与 RBR/RM / Potential Game / Replicator Dynamics 行为不可区分而被拍平。

**V0 已知陷阱**(从 P-D P1 教训 + V1 六关键词规则撞 BOSS 经验固化):

- **P-D P1 教训**:A1 攻击脚本 CLI 模式与 spec §6 判死命令衔接缺口 + 诱导操作者在真实仓库删除冻结锚。**本次避开**: P-A §5 A1 攻击在 `/tmp/deposon_pa_audit_<timestamp>/` 副本中跑,不碰真实仓库; 5 锚 SHA-256 闭环在 P-A §2 预登记。
- **V1 六关键词规则撞 BOSS**: GSM8K/StrategyQA accuracy 0.87 vs 0.85, deposon 散射层主张被拍平。**本次避开**: P-A §4 主要指标是"稳定化成本倍数"不是 accuracy,即使 LLM 玩家 accuracy 与 Bayesian 相同,只要收敛快 ≤ 1.3× 仍可 PASS。

**BOSS 列表**(对应 `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` V0.2 BOSS-A1/A2/A3):

- **BOSS-A1**: 简单势博弈算法(Repeated Best Response / Regret Matching, Hart & Mas-Colell 2000) → 不需要 deposon 散射层就能在 22 节点上单调收敛 → deposon 平衡点"无差异化"。**测法**: 同样的 22 受控概念图,直接跑 RBR/RM,看 P-A §4.1 成本倍数 ≤ 1.3× 是否依然成立。如 RBR/RM 也 ≤ 1.3× → 主张降级为"工程化系统"; 若 RBR/RM > 2.0× → deposon 散射层有差异化。
- **BOSS-A2**: 经典 Potential Game 理论(Monderer & Shapley 1996) → 直接给出 P-A 主张的理论证明,deposon 散射层是包装。**测法**: 不跑 deposon,直接套 Potential Game 框架, 看能否闭式证明 P-A §1 H1 主张(LLM 与 Bayesian 几乎无差)→ 如能,deposon 散射层"无新增理论价值"。
- **BOSS-A3**: Replicator Dynamics 单纯形 + 进化稳定策略(ESS, Smith 1973 / Taylor & Nowak 2006) → 在 22 节点小图上,任意两策略博弈都会收敛到 ESS,deposon 无差异化。**测法**: 用 Replicator Dynamics 跑 22 图,看 ESS 点是否与 deposon 散射层平衡点重合。如重合 → 主张被拍平。

**禁止条款**:
- **不得**只跑 P-A §3 实验而跳过 BOSS-A1/A2/A3 baseline(防 V1 撞 BOSS 重演)
- **不得**在 BOSS 测法跑通前宣称 P-A 方向 PASS(防 P-D P1 复现:判死过早)
- **不得**在真实仓库跑 BOSS baseline(必须 `/tmp/deposon_pa_audit_<timestamp>/` 副本)
- **不得**让 BOSS 测法脚本诱导删除 P-A §2 预登记 5 锚(无参 + 临时副本,沿用 P-D V0.1.2 修复模式)

**V0 主体保持冻结,§0.5 + §10 D5/D6 微调 = 唯一升级**(详见 V0.1 → V0.2 升级记录节)。

## 1. 目标与范围

V0 把现有「静态单期 ECR=1.333 协调比」指标升级为**动态均衡稳定化成本的度量化协议**。锚定对象固定为 5 个冻结工件：本文 §3 的 ECR 基线、本文 §3 的判死裁定族（GT-1/GT-2/GT-3/GT-4/GT-5b/GT-6/GT-7/GT-8/GT-8B/GT-8C）、deposon 仓库 `verifier/runs/` 下 5 个 frozen run、deposon 仓库 `tools/llm_client.py`（runtime 读取火山引擎 key，**不**入 prompt）、deposon 仓库 `tools/exp_harness.py`（机制 + LLM + 判死 cell 注入）。

V0 的核心问题：**当 LLM 玩家进入 deposon 博弈时，纳什均衡的稳定化需要多少次迭代 + 多少 cost 才能收敛**？基线是 Bayesian-rational 玩家（已知机制，最优响应）；V0 测 LLM 玩家相对基线的**稳定化成本倍数**（cost multiplier = LLM 玩家达到 ε-纳什均衡所需的总迭代次数 / Bayesian 基线）。

V0 的判死线（**预登记**，本 spec 冻结）：
- **H0（判死）**：稳定化成本倍数 ≥ 2.0×（LLM 玩家是 Bayesian 的 2× 慢，机制不可行）
- **H1（闭合）**：稳定化成本倍数 ≤ 1.3×（LLM 玩家与 Bayesian 几乎无差，机制可商用）

V0 的输出 = 一张 N=300 决策的 cost 倍数表（含 95% bootstrap CI）+ 3 机制 × 4 任务族的子表。

## 2. 锚点（pre-registered SHA-256 前 12 位）

D1 由 successor 子代理计算，路径 `verifier/handoff/P_A_V0_anchors_sha256_12.json`：

| 锚 ID | 对象 | 算法 | 字段 |
|---|---|---|---|
| `P_A_ECR_BASELINE` | 本文 §3 ECR=1.333 基线 | SHA-256 全文 → 前 12 位 | `ecr_median=1.333` |
| `P_A_KILL_LINE` | GT 判死裁定族（10 个）| SHA-256 全文 → 前 12 位 | `kills={"GT-1":true, ...}` |
| `P_A_FROZEN_RUNS` | 5 个 frozen run JSON | SHA-256 各 → 前 12 位 | `runs=["v20_gt", ...]` |
| `P_A_LLM_CLIENT` | `tools/llm_client.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |
| `P_A_HARNESS` | `tools/exp_harness.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |

任何 ≥ 1 锚漂移 → 全 V0 撤回。

## 3. 实验设计

### 3.1 玩家

- **LLM 玩家**：Doubao (volces_ark_bytedance) + DeepSeek，按本仓库现有 `llm_client.py` 协议
- **Bayesian 基线玩家**：理论最优响应计算器（已知机制 + 支付 → 决策）
- **统一决策空间**：4 选 1（与 deposon 概念图同结构）

### 3.2 机制（3 个，独立实现 + 比对）

- **M1：Deposon T+R+A 三通道**（移植 deposon 散射层）
- **M2：纯 Greedy 贪心**（无场，无守恒约束）
- **M3：Random 随机基线**（均匀采样决策）

### 3.3 任务族（4 个）

- **T1：GSM8K 风格多步算术**（n=20，源自 v1_4_gsm8k 子集）
- **T2：StrategyQA 风格隐式推理**（n=20，源自 v1_4_strategyqa 子集）
- **T3：合成陷阱**（n=20，源自 v1_3_traps）
- **T4：自定义最小博弈**（n=10，2×2 矩阵，明确纳什均衡点）

总 cell = 3 机制 × 4 任务族 × 25 决策/任务 = 300 calls

### 3.4 收敛判据

- **ε-纳什**：任一玩家单独改策略的支付增量 < ε=0.01
- **最多迭代**：50 轮（防无限循环）
- **测量**：每轮记录所有玩家的策略 + 支付

## 4. 度量

### 4.1 主要指标：稳定化成本倍数

```
cost_multiplier(M, T) = total_iterations_LLM(M, T) / total_iterations_Bayesian(M, T)
```

跨 (M, T) 算 mean + 95% bootstrap CI（10k resamples）。

### 4.2 副指标

- **收敛成功率**：LLM 玩家在 ≤ 50 轮内达到 ε-纳什 的 cell 占比
- **均衡点偏移**：LLM 玩家最终策略 vs Bayesian 真实纳什的 Hamming 距离
- **支付 gap**：LLM 玩家平均支付 vs Bayesian 平均支付

### 4.3 判死裁定

```python
def kill_decision(mean_mult, ci_lo, ci_hi):
    if mean_mult >= 2.0:
        return "FAIL_H0"  # 机制不可行
    elif mean_mult <= 1.3 and ci_hi <= 1.5:
        return "PASS_H1"  # 机制可商用
    else:
        return "GRAY"  # 1.3 < mean < 2.0 或 CI 跨边界
```

## 5. 抗攻击检查（v3x reviewer-b 准备）

- **A1：提示词扰动**：调换 system prompt 中机制描述顺序 3 次，重跑 10 cell，看 cost 倍数变化 > 50% 则报"不稳定"
- **A2：温度敏感性**：LLM temperature 0.0/0.5/1.0 三档，看 cost 倍数 > 30% 变化则报"温度敏感"
- **A3：种子复现**：seed=42, 123, 456 三套，看 cost 倍数 std/mean > 0.2 则报"种子敏感"

## 6. 复现协议（reviewer-b 独立 /tmp 副本审计）

- 复制仓库到 `/tmp/deposon_pa_audit_<timestamp>/`
- 读 `verifier/handoff/P_A_V0_anchors_sha256_12.json` 验 5 锚
- 选 1 cell（e.g. M1×T1）重跑 100 决策 × 5 seed = 500 calls
- 验 cost 倍数与原值 ± 5% 内
- 任意超差 → 撤回整 V0

## 7. 交付

- D5：`docs/V3X/P_A_V0_RESULTS_2026_09_09_mavis.md`（含成本倍数表 + 95% CI + 判死裁定 + 攻击结果）
- D7：`docs/V3X/P_A_V0_PAPER_zh.md`（中文短稿 ≤ 8 页）
- 全程：所有脚本 + handoff 锚点 + 复跑日志落仓库 `results/v3x_pa_v0/`

## 8. 失败模式（与王老师 WeChat 同步）

- 5 锚漂移 ≥ 1 → 全 V0 撤回
- 判死 H0（H_mult ≥ 2.0）→ P-A 方向 FAIL，撤 V3.X 整个 P-A 候选
- 判死 GRAY（1.3 < H_mult < 2.0）→ Mavis 自主扩 cell（n=300 → n=900）重判，王老师仅 ack
- 攻击 A1/A2/A3 任一不通过 → 重审实现，王老师 ack 是否撤回

## 9. 与 deposon 铁律的兼容性

- ✅ 不改 P-D V0.1.1
- ✅ 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/
- ✅ key 安全：runtime `Path(file).read_text()` 读取，不入 prompt
- ✅ /tmp 副本做所有重跑
- ✅ 不签 18 月 / 多论文规划
- ✅ 不上生产
- ✅ 不重做王老师已有工作

## 10. 时间线（D1-D7）

| Day | 任务 | 派给 |
|---|---|---|
| D1 | 出本 spec + 5 锚预登记 + §0.5 BOSS 测法节 | v3x + successor |
| D2 | 实现 LLM 玩家 + 3 机制 + 4 任务族 harness + BOSS-A1 RBR/RM baseline 占位 | data |
| D3 | pilot 50 calls (5 cells) 跑通，触发 WeChat 1 + BOSS-A1 baseline 跑通 | data + v3x |
| D4 | 全 300 calls + 初步 cost 表 + BOSS-A2 Potential Game 闭式证明 + BOSS-A3 Replicator Dynamics 跑通 | data |
| D5 | reviewer-b 判死 + 3 攻击 + **BOSS-A1/A2/A3 测法 + P-A 判死裁定对照** + D5 报告 | reviewer-b + data |
| D6 | 失败模式处理 / GRAY 扩 cell（如需）/ **若 BOSS 测法全 PASS 则 P-A 方向 PASS；任一 BOSS 测法撞上则降级主张** | Mavis + v3x |
| D7 | 中文短稿 + 全 handoff 归档 + BOSS 测法结果回写到 QUICK_KILL_6_DIRECTIONS.md V0.3 | paper-cn + successor |

## V0.1 → V0.2 升级记录（2026-09-09 BOSS 经验固化）

- **V0.1**: §1-§9 主体,§10 D1-D7 排程(2026-09-09 前冻结)
- **V0.2 增量**:
  - 加 §0.5 BOSS 测法节(5 个禁止条款 + BOSS-A1/A2/A3 测法)
  - §10 D5 加 "BOSS-A1/A2/A3 测法 + P-A 判死裁定对照"
  - §10 D6 加 "若 BOSS 测法全 PASS 则 P-A 方向 PASS；任一 BOSS 测法撞上则降级主张"
  - §10 D7 加 "BOSS 测法结果回写到 QUICK_KILL_6_DIRECTIONS.md V0.3"
- **V0 主体保持冻结**: §1-§9 + 5 锚预登记不动
- **下次升级触发**: D5/D6 跑出 BOSS 测法结果,回写到 QUICK_KILL_6_DIRECTIONS.md 对应 BOSS 列表,作为"实测记录"
