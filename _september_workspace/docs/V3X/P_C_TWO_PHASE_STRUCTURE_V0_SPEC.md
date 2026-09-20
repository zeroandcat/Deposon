# P-C 两相结构 V0 规范

> ⚠️ **D1 启动阻塞**（低风险）："两相边界"具体位置需 v3x 子代理在 D1 末做 pilot (n=20) 锁定，再写完整 spec。spec 框架已就绪。

## 1. 目标与范围

V0 验证 deposon 散射层在**两相结构**图族上是否呈现**标度律**：phase I（小图族，g_aether 占优）vs phase II（大图族，g_eff 占优）的相变点 + 幂律指数 β。锚定对象固定为 5 个冻结工件：本文 §3 的 ECR=1.333 基线、本文 §3 的 GT_FORMAL P1a/P1b/P2/P3 判死族、deposon 仓库 `verifier/runs/` 下 5 个 frozen run、deposon 仓库 `tools/llm_client.py`、deposon 仓库 `tools/scaling_probe.py`（**D1 由 data 实现**）。

V0 的核心问题：**在图族规模 N 扫描下，散射层的命中率/失真率是否呈现幂律 P(N) = A·N^(-β) + C**？基线是 ECR=1.333（V2 已有）；V0 测幂律指数 β 是否落在 [0.3, 0.7] 区间。

V0 的判死线（**预登记**，本 spec 冻结）：
- **H0（判死）**：R² < 0.3 或 幂律指数 CI 含 0（无标度律）
- **H1（闭合）**：R² > 0.7 且 幂律指数 CI ⊂ [0.3, 0.7]（标度律成立）

V0 的输出 = 一张 N=100 图 × N=10 任务族扫描表 + 幂律回归 β 估计 + 95% CI + 相变点位置。

## 2. 锚点（pre-registered SHA-256 前 12 位）

D1 由 successor 子代理计算，路径 `verifier/handoff/P_C_V0_anchors_sha256_12.json`：

| 锚 ID | 对象 | 算法 | 字段 |
|---|---|---|---|
| `P_C_ECR_BASELINE` | 本文 §3 ECR=1.333 基线 | SHA-256 全文 → 前 12 位 | `ecr_median=1.333` |
| `P_C_GT_FORMAL_KILLS` | GT_FORMAL P1a/P1b/P2/P3 判死族 | SHA-256 全文 → 前 12 位 | `kills={"P1a":true, ...}` |
| `P_C_FROZEN_RUNS` | 5 个 frozen run JSON | SHA-256 各 → 前 12 位 | `runs=["v21_gtformal", ...]` |
| `P_C_LLM_CLIENT` | `tools/llm_client.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |
| `P_C_SCALING_PROBE` | `tools/scaling_probe.py` | SHA-256 全文 → 前 12 位 | `version=2026-09-11` |

任何 ≥ 1 锚漂移 → 全 V0 撤回。

## 3. 实验设计

### 3.1 图族规模扫描

- **N ∈ {10, 20, 50, 100, 200, 500, 1000}**（7 档）
- 每档 N 张图，每张图跑 deposon 三通道散射，记录 (命中率, 失真率, 收敛步数)
- 总图 = ΣN = 10+20+50+100+200+500+1000 = 1880 张
- 每图 ≤ 5 min 跑完（单核 + LLM 决策）

### 3.2 任务族（10 个）

1. GSM8K 风格多步算术
2. StrategyQA 风格隐式推理
3. 合成陷阱
4. 自定义最小博弈
5. 低资源博弈
6. 路径唯一图（deposon 强约束）
7. 路径多样图（deposon 弱约束）
8. 随机图
9. 网格图
10. 树图

每图 1 任务族，共 1880 calls。

### 3.3 标度律拟合

```
log10(P(N)) = β · log10(N) + log10(A) + ε
```

用 OLS 拟合，得 β 估计 + 95% CI。

### 3.4 相变点检测

观察 (命中率, 失真率) 在 N 上的导数突变点 → 候选相变点 N_c。Pilot (n=20) 锁定后，正式实验再确认。

## 4. 度量

### 4.1 主要指标：幂律拟合 R²

```
R² = 1 - Σ(P_obs - P_pred)² / Σ(P_obs - P_mean)²
```

跨 7 档 N 算，R² 越接近 1 标度律越强。

### 4.2 副指标

- **β 估计**：幂律指数（核心）
- **β CI**：95% 置信区间
- **相变点 N_c**：导数突变点（如果存在）
- **任务族特异**：每个 T 单独算 R²，识别标度律最稳健的任务

### 4.3 判死裁定

```python
def kill_decision(r_squared, beta_lo, beta_hi):
    if r_squared < 0.3:
        return "FAIL_H0"  # 无标度律
    elif 0 in [beta_lo, beta_hi] or (beta_lo < 0 < beta_hi):
        return "FAIL_H0"  # CI 含 0 = 不显著
    elif r_squared > 0.7 and 0.3 <= beta_lo and beta_hi <= 0.7:
        return "PASS_H1"  # 标度律成立且 β 在合理区间
    else:
        return "GRAY"  # R² 0.3-0.7 或 β 越界但 CI 紧
```

## 5. 抗攻击检查（v3x reviewer-b 准备）

- **A1：图族重采样**：用不同 seed 重采样图族，重跑拟合，看 R² 变化 > 0.15 则报"图族不稳"
- **A2：拟合函数对抗**：用指数拟合 P(N) = A·exp(-βN) + C 重跑，看 R² 超过幂律拟合的 90% 则报"幂律非唯一"
- **A3：N 范围裁剪**：去掉 N=10 和 N=1000 两端，看 R² 是否仍 > 0.7（"幂律非端点驱动"）

## 6. 复现协议（reviewer-b 独立 /tmp 副本审计）

- 复制仓库到 `/tmp/deposon_pc_audit_<timestamp>/`
- 读 `verifier/handoff/P_C_V0_anchors_sha256_12.json` 验 5 锚
- 选 N=100 档 50 张图重跑，看 R² 与原值 ± 0.05 内
- 任意超差 → 撤回整 V0

## 7. 交付

- D5：`docs/V3X/P_C_V0_RESULTS_2026_09_09_mavis.md`（含 N 扫描表 + β 估计 + 95% CI + R² + 判死裁定 + 攻击结果）
- D7：`docs/V3X/P_C_V0_PAPER_zh.md`（中文短稿 ≤ 8 页）
- 全程：所有脚本 + handoff 锚点 + 复跑日志落仓库 `results/v3x_pc_v0/`

## 8. 失败模式（与王老师 WeChat 同步）

- 5 锚漂移 ≥ 1 → 全 V0 撤回
- 判死 H0（R² < 0.3 或 CI 含 0）→ P-C 方向 FAIL，撤 V3.X 整个 P-C 候选
- 判死 GRAY（0.3 ≤ R² ≤ 0.7）→ Mavis 自主扩图族（n=100 → n=300）重判，王老师仅 ack
- 攻击 A1/A2/A3 任一不通过 → 重审实现，王老师 ack 是否撤回
- **D1 pilot 后相变点未锁定** → v3x 子代理返工，王老师 ack 是否需要改 spec

## 9. 与 deposon 铁律的兼容性

- ✅ 不改 P-D V0.1.1
- ✅ 不碰 HANDOFF_MACHINE_READABLE.json / results/*.json / verifier/vN/
- ✅ key 安全：runtime `Path(file).read_text()` 读取，不入 prompt
- ✅ /tmp 副本做所有重跑
- ✅ 不签 18 月 / 多论文规划
- ✅ 不上生产
- ✅ 不重做王老师已有工作
- ✅ 相变点定位由 v3x 子代理 D1 pilot 锁定（不在 P-C 内自创）

## 10. 时间线（D1-D7）

| Day | 任务 | 派给 |
|---|---|---|
| D1 | pilot n=20 锁相变点 + 出本 spec final + 5 锚预登记 | v3x + successor |
| D2 | 实现 scaling_probe + 7 档 N × 10 任务 harness | data |
| D3 | pilot 50 calls (1 个 N 档 × 5 图) 跑通，触发 WeChat 1 | data + v3x |
| D4 | 全 1880 calls + 幂律回归 + R² 报告 | data |
| D5 | reviewer-b 判死 + 3 攻击 + D5 报告 | reviewer-b + data |
| D6 | 失败模式处理 / GRAY 扩 cell（如需）| Mavis + v3x |
| D7 | 中文短稿 + 全 handoff 归档 | paper-cn + successor |
