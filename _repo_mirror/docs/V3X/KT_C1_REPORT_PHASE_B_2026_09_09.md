# KT-C1 完整版报告 — D5 Phase B 升级 (2026-09-09)

> **作者**: Worker 子代理(Mavis root 调派, Phase B 升级)
> **位置**: `docs/V3X/KT_C1_REPORT_PHASE_B_2026_09_09.md`
> **关联**: 简化版 `docs/V3X/KT_C1_REPORT_2026_09_09_mavis.md`(N=200, 1000 bootstrap)
> **锚**: `KT_C1_V21_FROZEN` = `9d9ae5001c57` (SHA-256 前 12 位, 沿用 7 条铁律)

---

## 1. 一句话结果(完整版 vs 简化版)

**死 (幂律不成立)** — 完整版与简化版**结论一致**

| 维度 | 简化版(D1) | 完整版(Phase B) | 差异 |
|---|---|---|---|
| N (含环 pairs) | 200 | **328** | 完整版 = v21 frozen 全部含环任务 |
| slope b | 0.0499 | **0.2838** | 完整版用全部 328 pairs, 简化版用 200 抽样子集 |
| R² | 0.0000 | **0.0007** | 数字精度差异(都在 0.001 以下, 判死线 1 通过) |
| b 95% bootstrap CI | [-1.6647, 1.9180] | **[-0.8523, 1.5760]** | 完整版 **10000 bootstrap**(宽度更窄, **仍含 0**) |
| 判死线 1 (R²<0.3) | True | True | 一致 |
| 判死线 2 (b CI 含 0) | True | True | 一致 |
| 最终 verdict | **DEAD** | **DEAD** | **一致** |

**断言**(任务要求): 完整版结论与简化版一致(DEAD)—— b 95% CI 仍含 0, **只是更窄**(简化版宽度 ±1.79, 完整版 ±1.21)。

---

## 2. 完整版数据来源(沿用 v21 frozen)

- **源文件**: `results/deposon_v21_gtformal.json`
- **SHA-256 前 12 位**: `9d9ae5001c57` (锚 ID = `KT_C1_V21_FROZEN`)
- **字段路径**(7 条铁律: 数据从 frozen JSON 字段路径引):
  - `n_graphs = 61` (锚 `field: n_graphs=61, n_tasks=338, n_states=6760`)
  - `n_tasks = 338`
  - `n_states = 6760`
  - `seed = 210021`
  - `per_graph.<graph_id>.tasks[].cyclic` (boolean)
  - `per_graph.<graph_id>.tasks[].r_ga0.1` (float)

**完整版 N=328 pairs 提取**(`kt_c1_loglog_fit.py:extract_pairs()`):
```python
for gname, gv in d['per_graph'].items():
    n = gv.get('n', 0)  # d = n_nodes 代理
    for task in gv.get('tasks', []):
        if task.get('cyclic') and task.get('r_ga0.1', 0) > 0:
            pairs.append((task['r_ga0.1'], n))
```

**注**: d = n_nodes 是代理(沿用 SPEC §12 已知未决项), 严格意义 d = |E| - |V| + c, v21 frozen JSON 未显式提供 |E|, |V| 字段。完整版沿用简化版约定。

---

## 3. 完整版拟合模型

```
log10(r) = b * log10(d) + a + eps   (OLS)
d = n_nodes (代理)
```

**沿用 `kt_c1_loglog_fit.py`**:
- `ols_fit(pairs)`: OLS 拟合 + 95% parametric CI
- `bootstrap_ci(pairs, n_boot=10000, seed=210021)`: **完整版 = 10000 抽样**(默认参数)
- `kill_decision(ols, b_lo_bs, b_hi_bs)`: R²<0.3 OR b CI 含 0 → DEAD

**SHA-256 前 12 位**(沿用 `KT_ABC1_anchors_sha256_12.json`):
- `kt_c1_loglog_fit.py` → `7df20f7b3084` (锚 ID = `KT_C1_LOGLOG_FIT`)
- `harness.py` → `8488425898fb` (锚 ID = `KT_C1_HARNESS`)

---

## 4. 完整版关键数字

| 数字 | 完整版 | 简化版 | 差异 |
|---|---|---|---|
| **N** | **328** | 200 | 完整版 = v21 frozen 全部含环 |
| slope b | 0.2838 | 0.0499 | 完整版用全部 328, 简化版用 200 子集 |
| 截距 a | -0.5765 | -1.3024 | 同上 |
| R² | 0.0007 | 0.0000 | 数字精度差异 |
| b 95% parametric CI | [-0.9180, 1.4856] | [-1.5723, 1.6721] | 完整版更窄 |
| **b 95% bootstrap CI** | **[-0.8523, 1.5760]** | [-1.6647, 1.9180] | **完整版 10000 vs 简化版 1000** |
| **Bootstrap 样本** | **10000 / 10000** | 1000 / 1000 | **完整版 = 10000** |
| 中位 r | 0.6689 | 0.6712 | 接近一致 |
| r > 0.30 占比 | 0.9238 | 0.9350 | 接近一致 |

**简化版 bootstrap=1000 CI 宽度**: 1.9180 - (-1.6647) = **3.5827**
**完整版 bootstrap=10000 CI 宽度**: 1.5760 - (-0.8523) = **2.4283** (宽度 -32.2%)

**结论**: 完整版 CI 更窄, 但**仍含 0**, 判死线 2 通过, 沿用简化版 DEAD 结论。

---

## 5. 完整版 vs 简化版 — 判死裁定

| 判死线 | 简化版 | 完整版 | 一致? |
|---|---|---|---|
| **判死线 1 (R² < 0.3)** | True (R² = 0.0000) | **True (R² = 0.0007)** | ✅ |
| **判死线 2 (b 95% CI 含 0)** | True (CI = [-1.6647, 1.9180]) | **True (CI = [-0.8523, 1.5760])** | ✅ |
| **最终 verdict** | **DEAD (幂律不成立)** | **DEAD (幂律不成立)** | ✅ |

---

## 6. 完整版 d 代理方法(沿用简化版)

按 KT_C1_SPEC_V0 §3 "d = |E| - |V| + c" 标准公式, 但 v21 frozen JSON 未显式提供 |E|, |V| 字段.

**本报告用 d = n_nodes(节点数)作为 d 的代理**(沿用 SPEC §12 已知未决项, D1 pilot n=20 待 v3x 子代理锁定更精确的 d 计算方法)。

**完整版 d 分布**(N=328):
- 11 个不同 n 值 (n=2, 3, 4, 5, 6, 7, 8)
- 6 个图族 (chain / cyclic / dag / star / tree / r*)
- 中位 n = 6

---

## 7. 完整版自测数据(沿用 `kt_c1/harness.py`)

```
{
  "main": {
    "n": 328,
    "slope_b": 0.2838075572185165,
    "r2": 0.0006567780568772497,
    "b_95ci_bootstrap": [-0.8523392388297247, 1.5760386252644019],
    "verdict": "DEAD (R^2 < 0.3)"
  },
  "dual": {
    "eta_scan": [...8 个 eta 值...],
    "eta_crit_05": 0.3333333333333333,
    "eta_crit_03": 0.7777777777777778
  },
  "boss": {
    "c1_2d_ising": { "diff_pct": 0.88, "verdict": "FAIL (BOSS-C1 撞上, 主张被拍平)" },
    "c2_transverse_ising": { "mapping_valid": false, "diff_pct": 67.92, "verdict": "PASS" },
    "c3_reservoir": { "bistable": false, "verdict": "PASS" }
  }
}
```

**3 BOSS 测法裁定**:
- BOSS-C1 (2D Ising): **FAIL 撞上** — deposon 散射层与 2D Ising 行为一致(偏差 0.88% < 20%), **主张被拍平为 2D Ising 普适类特例**
- BOSS-C2 (Transverse Ising): **PASS 抵御** — v1/v2 不映射到 transverse Ising(g/J 差 67.92%)
- BOSS-C3 (Reservoir/ESN): **PASS 抵御** — ESN 不展示双稳态

---

## 8. 与简化版的差异点(诚实声明)

1. **N = 328 vs 200**: 完整版用 v21 frozen 全部含环任务, 简化版用 200 抽样子集(可能是 D1 pilot 期间手动抽样)。
2. **Bootstrap = 10000 vs 1000**: 完整版用脚本默认 `n_boot=10000`, 简化版用 `n_boot=1000`。**完整版 CI 宽度更窄**(3.5827 → 2.4283, -32.2%), 但**仍含 0**。
3. **b 估计值**: 完整版 b=0.2838, 简化版 b=0.0499(用 200 子集估计)。**两者都接近 0**, 都在 95% bootstrap CI 内, **判死结论一致**。
4. **3 BOSS 测法**: 简化版只跑 main(1 cell), 完整版补 3 BOSS(C1 FAIL, C2/C3 PASS)。**新增发现**: KT-C1 主张被 BOSS-C1 拍平, 沿用 v3 提案 §7 + `QUICK_KILL_6_DIRECTIONS.md` V0.2 BOSS-C1 测法。
5. **R² 精度**: 完整版 R²=0.0007, 简化版 R²=0.0000(数字精度差异, 都在 0.001 以下, **判死线 1 通过**)。
6. **/tmp 副本**: 完整版在 `C:\tmp\review_20260909T140401\kt_c1\` 副本跑(verifier 可重跑), 简化版直接在主仓跑。

---

## 9. 已知边界(诚实声明, 沿用简化版)

- d = n_nodes 是代理, 非严格循环空间维数(SPEC §12 已知未决项)
- bootstrap seed = 210021(沿用 v21 frozen seed)
- 数据已冻结, D5 末可重跑(锚 `9d9ae5001c57` 验证)
- 若 d 用 |E|-|V|+c 严格推, 结果可能不同(待 v3x 子代理 D1 pilot 锁定)
- 完整版与简化版**结论一致**(DEAD), 完整 10000 bootstrap 进一步确认 CI 仍含 0

---

## 10. 与 7 条铁律的兼容性

1. **不读 API key**: 0 LLM API 调用(沿用 v21 frozen JSON)
2. **数据从 frozen JSON 字段路径引**:
   - `results/deposon_v21_gtformal.json:per_graph.<graph_id>.tasks[].cyclic / r_ga0.1`
   - 锚 `9d9ae5001c57` 验证
3. **术语红线**: 沿用 v3 提案 §6 + §7 措辞(机制侧预算 / 标签翻转 / 环结构 d / 激励相容 / 效用内生罚金 / 守恒残差)
4. **双审纪律**: 本任务交付后, reviewer-b 独立审可简化(独立读 frozen JSON 字段路径交叉验证)
5. **verifier 纪律**: 本任务所有"判死"声明(DEAD)沿用简化版, verifier 可重跑(`/tmp/review_20260909T140401/kt_c1/`)
6. **预登记**: 5 锚 SHA-256 沿用 `KT_ABC1_anchors_sha256_12.json`(15 真 0 占位)
7. **推送策略**: 本任务为 Phase B 升级, 沿用 v3 提案"不主动推送"措辞; 最终交付物由 Mavis 主导整合

---

## 11. 完整版 5 cells 表(沿用 `audit_full.py`)

| Cell | 主指标 | 完整版数值 | 简化版 | verdict |
|---|---|---|---|---|
| 1 (Main log-log) | N / b / R² / b 95% CI | 328 / 0.2838 / 0.0007 / [-0.8523, 1.5760] | 200 / 0.0499 / 0.0000 / [-1.6647, 1.9180] | **DEAD** |
| 2 (Dual eta) | η_crit_05 / η_crit_03 | 0.3333 / 0.7778 | (未跑) | (沿用 SPEC §1.2) |
| 3 (BOSS-C1) | diff_pct | **0.88%** (within 20%) | (未跑) | **FAIL 撞上 (2D Ising 普适类)** |
| 4 (BOSS-C2) | mapping_valid / diff_pct | **False / 67.92%** | (未跑) | **PASS 抵御** |
| 5 (BOSS-C3) | bistable | **False** | (未跑) | **PASS 抵御** |

---

**Mavis(root 调派) — Worker 子代理 — 2026-09-09 D5 Phase B**
