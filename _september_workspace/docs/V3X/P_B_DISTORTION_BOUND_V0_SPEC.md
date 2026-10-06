# P-B 失真界 V0 规范

> ⚠️ **D1 启动阻塞**：本 spec 的"理论最优响应"与"理论失真界"公式需**外部顾问 D1 线上 给 1-page theory** 落地。spec 框架已就绪，等理论输入即可激活 v0 全部 cell。
>
> 〔**2026-09-30 口径变更 · C4 理论界来源（铁律级）**〕**本行「来源」归属已作废**：「外部顾问 D1 线上 给 1-page theory」⇒ **新口径：理论界来源 ＝ GLM 推导**（PI 2026-09-30 采认，问卷 `ask_3b8a6489fb38917e42a69ecd` q1「改：以 GLM 推导为准充作理论界」，**该选即视为明示**；连带面＝spec §9／C4.7 来源标注／论文口径）。**本行原文一字不动、历史留痕**；**「理论输入未到位 ⇒ 整 V0 仍阻塞」这一状态字面 0 改**（到位性另论，不随来源改）。勘误件＝`results/_c4_theory_source_caliber_correction_2026_09_30.md`。

## 1. 目标与范围

V0 解决：**当 LLM 玩家取代 Bayesian 玩家时，deposon 三通道散射机制的总失真 D(M, T) 是否在 [理论下界, 理论上界] 区间内**。锚定对象固定为 5 个冻结工件：本文 §3 的 ECR 基线、本文 §3 的判死裁定族（GT-1 到 GT-8C）、deposon 仓库 `verifier/runs/` 下 5 个 frozen run、deposon 仓库 `tools/llm_client.py`、deposon 仓库 `tools/distortion_calculator.py`（**D1 由 data 实现**）。

V0 的核心问题：**LLM 玩家的有限理性导致多少额外失真**？基线是 Bayesian 玩家（已知机制 + 支付 → 失真 = 0）；V0 测 LLM 玩家相对基线的**失真倍数** D 倍数 = D_LLM / D_Bayesian（数值 ≥ 1）。

V0 的判死线（**预登记**，本 spec 冻结）：
- **H0（判死）**：失真倍数 ≥ 2.0×（LLM 玩家引入 2× 失真，机制不可行）
- **H1（闭合）**：失真倍数 ≤ 1.5×（LLM 玩家引入 ≤ 50% 失真，机制可商用）

V0 的输出 = 一张 N=500 决策的失真倍数表（含 95% bootstrap CI）+ 3 机制 × 5 任务族子表 + 理论上下界曲线。

## 2. 锚点（pre-registered SHA-256 前 12 位）

D1 由 successor 子代理计算，路径 `verifier/handoff/P_B_V0_anchors_sha256_12.json`：

| 锚 ID | 对象 | 算法 | 字段 |
|---|---|---|---|
| `P_B_ECR_BASELINE` | 本文 §3 ECR=1.333 基线 | SHA-256 全文 → 前 12 位 | `ecr_median=1.333` |
| `P_B_KILL_LINE` | GT 判死裁定族（10 个）| SHA-256 全文 → 前 12 位 | `kills={"GT-1":true, ...}` |
| `P_B_FROZEN_RUNS` | 5 个 frozen run JSON | SHA-256 各 → 前 12 位 | `runs=["v20_gt", ...]` |
| `P_B_LLM_CLIENT` | `tools/llm_client.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |
| `P_B_DISTORTION_CALC` | `tools/distortion_calculator.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |

任何 ≥ 1 锚漂移 → 全 V0 撤回。

## 3. 实验设计

### 3.1 玩家

- **LLM 玩家**：Doubao (volces_ark_bytedance) + DeepSeek（与 P-A 共用 `llm_client.py`）
- **Bayesian 基线玩家**：理论最优响应计算器（已知机制 + 支付 → 失真 = 0）
- **统一决策空间**：4 选 1（与 deposon 概念图同结构）

### 3.2 机制（3 个，独立实现 + 比对）

- **M1：Deposon T+R+A 三通道**（移植 deposon 散射层）
- **M2：纯 Greedy 贪心**（无场，无守恒约束）
- **M3：Random 随机基线**（均匀采样决策）

### 3.3 任务族（5 个，比 P-A 多 1 个）

- **T1：GSM8K 风格多步算术**（n=20）
- **T2：StrategyQA 风格隐式推理**（n=20）
- **T3：合成陷阱**（n=20）
- **T4：自定义最小博弈**（n=10，明确纳什均衡点）
- **T5：低资源博弈**（n=20，每决策只给 3 步推理，最小信息情境）

总 cell = 3 机制 × 5 任务族 × 33 决策/任务 ≈ 500 calls

### 3.4 失真度量 D(M, T)

```
D(M, T) = E_π[ Σ_t |u*(a_t) - u(a_t)| / max_u ]
```

- `u*(a_t)`: 理论最优决策的支付
- `u(a_t)`: 实际玩家决策的支付
- `max_u`: 支付上界（任务族归一化常数）

失真倍数 = D_LLM(M, T) / max(D_Bayesian(M, T), ε)

### 3.5 理论界（**需外部顾问 D1 线上 输入**）

> 〔**2026-09-30 口径变更 · C4**〕**本标题「来源」已作废** ⇒ **新口径：理论界来源 ＝ GLM 推导**（PI 2026-09-30 采认，`ask_3b8a6489fb38917e42a69ecd` q1，**本选即视为明示**）。**标题原文一字不动**；**「理论界未到位 ⇒ 内部判死线阻塞」状态字面 0 改**。

- **下界 L(M, T)**：LLM 信息瓶颈下的最低可能失真（由 IC 容量 + 机制可辨识性推出）
- **上界 U(M, T)**：机制可承受的最高失真（机制收敛性条件推出）

D1 由 v3x 子代理根据外部顾问理论给具体公式，落到 `tools/distortion_calculator.py`。

> 〔**2026-09-30 口径变更 · C4**〕**本行「来源」已作废**：「根据外部顾问理论」⇒ **GLM 推导**（同上前注，`ask_3b8a6489fb38917e42a69ecd` q1）。**本行原文一字不动**；**「公式落位 `tools/distortion_calculator.py`」之落位路径字面 0 改**（与来源归属是两件事，0 混同）。

## 4. 度量

### 4.1 主要指标：失真倍数

```
distortion_multiplier(M, T) = D_LLM(M, T) / max(D_Bayesian(M, T), ε)
```

跨 (M, T) 算 mean + 95% bootstrap CI（10k resamples）。

### 4.2 副指标

- **理论下界命中率**：D_LLM ≤ L(M, T) 的 cell 占比
- **理论上界越界率**：D_LLM > U(M, T) 的 cell 占比
- **任务族特异**：每个 T 单独算 mean，识别最易/最难任务
- **机制特异**：每个 M 单独算 mean，对比三通道散射 vs 贪心 vs 随机的相对失真

### 4.3 判死裁定

```python
def kill_decision(mean_mult, ci_lo, ci_hi, theory_U_hit_rate):
    if mean_mult >= 2.0 or theory_U_hit_rate >= 0.3:
        return "FAIL_H0"  # 机制不可行 或 30%+ cell 超理论界
    elif mean_mult <= 1.5 and ci_hi <= 1.8 and theory_U_hit_rate <= 0.1:
        return "PASS_H1"  # 机制可商用
    else:
        return "GRAY"  # 1.5 < mean < 2.0 或 CI 跨边界
```

## 5. 抗攻击检查（v3x reviewer-b 准备）

- **A1：理论界对抗**：v3x reviewer-b 用一个明显错误的理论界公式重跑 10 cell，看判死结果是否翻转（>30% 翻转则报"理论界不稳"）
- **A2：任务族偏差**：调换 T1-T5 顺序重跑，看失真倍数变化 > 40% 则报"任务族顺序敏感"
- **A3：种子复现**：seed=42, 123, 456 三套，看 std/mean > 0.2 则报"种子敏感"

## 6. 复现协议（reviewer-b 独立 /tmp 副本审计）

- 复制仓库到 `/tmp/deposon_pb_audit_<timestamp>/`
- 读 `verifier/handoff/P_B_V0_anchors_sha256_12.json` 验 5 锚
- 选 1 cell（e.g. M1×T1）重跑 100 决策 × 5 seed = 500 calls
- 验失真倍数与原值 ± 5% 内
- 任意超差 → 撤回整 V0

## 7. 交付

- D5：`docs/V3X/P_B_V0_RESULTS_2026_09_09_mavis.md`（含失真倍数表 + 95% CI + 理论界 + 判死裁定 + 攻击结果）
- D7：`docs/V3X/P_B_V0_PAPER_zh.md`（中文短稿 ≤ 8 页）
- 全程：所有脚本 + handoff 锚点 + 复跑日志落仓库 `results/v3x_pb_v0/`

## 8. 失败模式（与外部顾问 线上 同步）

- 5 锚漂移 ≥ 1 → 全 V0 撤回
- 判死 H0（D_mult ≥ 2.0）→ P-B 方向 FAIL，撤 V3.X 整个 P-B 候选
- 判死 GRAY（1.5 < D_mult < 2.0）→ Mavis 自主扩 cell（n=500 → n=1500）重判，外部顾问仅 ack
- 攻击 A1/A2/A3 任一不通过 → 重审实现，外部顾问 ack 是否撤回
- **D1 外部顾问未给理论公式** → 整 V0 阻塞，v3x 子代理无法继续

> 〔**2026-09-30 口径变更 · C4**〕**本行「来源」已作废**：「外部顾问未给理论公式」⇒ **理论界来源 ＝ GLM 推导**（PI 2026-09-30 采认，`ask_3b8a6489fb38917e42a69ecd` q1，**本选即视为明示**）。**本行原文一字不动**；**「理论未到位 ⇒ 整 V0 阻塞」之状态字面 0 改**。
>
> 〔**同批扫描 · §8 内 0 受影响处**〕**本节标题「（与外部顾问 线上 同步）」、「判死 GRAY …外部顾问仅 ack」、「攻击 A1/A2/A3 任一不通过 → …外部顾问 ack 是否撤回」三处属**失败模式通报 / ack 协作面**，**非理论界来源归属** ⇒ **本次 0 受影响、字面 0 改**；登记于此以免下游误读为「§8 整节已随 C4 变更」。

## 9. 与 deposon 铁律的兼容性

- ✅ 不改 P-D V0.1.1
- ✅ 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/
- ✅ key 安全：runtime `Path(file).read_text()` 读取，不入 prompt
- ✅ /tmp 副本做所有重跑
- ✅ 不签 18 月 / 多论文规划
- ✅ 不上生产
- ✅ 不重做外部顾问已有工作
- ✅ **理论界由外部顾问给定**（不在 P-B 内自创）

> 〔**2026-09-30 口径变更 · C4 理论界来源（铁律级）· §9 主口径行〕**
>
> - **已作废者（逐字界定）**：**「由外部顾问给定」之来源归属** ⇒ **新口径：理论界来源 ＝ GLM 推导**（PI 2026-09-30 采认合并卷 `ask_3b8a6489fb38917e42a69ecd` q1「改：以 GLM 推导为准充作理论界」，选项原文含「铁律级：连带改 spec §9、C4.7 来源标注与论文口径；**本选即视为明示**」⇒ **本行即铁律级明示来源**）。
> - **仍然有效者（⛔ 0 随来源变更而解除）**：**「不在 P-B 内自创」＝ 0 自创 / 0 自拟公式**之约束，**沿 C4.9 归零纪律字面继续有效**（`4185bdad6df5` §2.4.2「0 以估计值 / 替代值 / 自拟公式填充」）。⛔ 本次来源变更 **0 扩权、0 收权、0 改 C4.9 字面**；**「GLM 推导」之授权边界（可推导到何种程度、产出物是否算「自拟」）＝ 待核项，见勘误件 §4-a，0 由本行代替 PI 解释**。
> - **本行原文一字不动、历史留痕**（沿「口径反转型修正」纪律：**活文档逐处加注，实录件 0 回改**）。勘误件＝`results/_c4_theory_source_caliber_correction_2026_09_30.md`。
> - **相邻行「不重做外部顾问已有工作」（上 1 行）**：**本次 0 受影响**——该行约束的是**0 重做其既有工作**（WINE 2025 分布报告 / arXiv:2507.04030 一系），**非理论界来源归属**；**其字面 0 改**，此处登记以免下游误读为「已随 §9 一并作废」。

## 10. 时间线（D1-D7）

| Day | 任务 | 派给 |
|---|---|---|
| D1 | 等外部顾问 线上 理论公式 → 出本 spec final + 5 锚预登记 | v3x + successor |
| D2 | 实现 distortion_calculator + LLM 玩家 + 3 机制 + 5 任务族 harness | data |
| D3 | pilot 50 calls (5 cells) 跑通，触发 线上 1 | data + v3x |
| D4 | 全 500 calls + 初步失真表 | data |
| D5 | reviewer-b 判死 + 3 攻击 + D5 报告 | reviewer-b + data |
| D6 | 失败模式处理 / GRAY 扩 cell（如需）| Mavis + v3x |
| D7 | 中文短稿 + 全 handoff 归档 | paper-cn + successor |

> 〔**2026-09-30 口径变更 · C4**〕**上表 D1 行「来源」已作废**：「等外部顾问 线上 理论公式」⇒ **理论界来源 ＝ GLM 推导**（`ask_3b8a6489fb38917e42a69ecd` q1，**本选即视为明示**）。**上表 D1–D7 七行原文一字不动**；**D1 时点编排、5 锚预登记、「出本 spec final」字面 0 改**——⚠️ **0 代 PI 重排时间线**（改来源 ≠ 改时点；时点面如需动，列待核项）。
