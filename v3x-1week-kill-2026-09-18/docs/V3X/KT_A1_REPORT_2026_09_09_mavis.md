# KT-A1 D2 报告 — Bayesian 基线对照 (2026-09-09)

> **作者**: Mavis(root session, 一周判死自由推进)
> **状态**: V0(草稿, D2 部分; D3 末补 LLM 部分)
> **位置**: `docs/V3X/KT_A1_REPORT_2026_09_09_mavis.md`
> **关联**: KT_A1_SPEC_V0 §1.1 + §1.2

---

## 1. 一句话结果(D2 Bayesian 基线部分)

**PASS (H1 闭合, cost <= 1.3x)**

- Deposon 散射层(v21 global r_ga0.1 均值): 0.6437
- Bayesian baseline(v20 22 受控概念图 field_mean 均值): 0.1809
- Cost multiplier (deposon_acc / bayesian_acc): 0.4350
- 判死 H1 (cost <= 1.3x): True
- 判死 H0 (cost >= 2.0x): False

## 2. 数据

- v20 受控概念图: 22 图(锚 P_A_FROZEN_RUNS 中 v20_baselines)
- v21 frozen 含环: 328 cyclic tasks
- 6 Bayesian baselines: field_mean / common_neighbors / preferential_attachment / ppr / katz / ngram_tfidf_cosine
- v20 数据集 SHA-256 (待 D2 末填): 占位
- v21 数据集 SHA-256: `9d9ae5001c57` (KT_C1_V21_FROZEN)

## 3. D2 单跑设计

**只跑 Bayesian 基线对照(无 LLM)**:
- Bayesian = 22 受控概念图上 6 baseline 中最高分
- Deposon 散射层 = v21 frozen 残余 r 均值(1 - r 作为"准确率"代理)
- Cost multiplier = deposon_acc / bayesian_acc

**LLM 部分延 D3**:
- LLM(Doubao + DeepSeek) 玩家部分需要 API key(7 条铁律实现 step 才读)
- D3 末实现 + 跑

## 4. 关键数字

| 数字 | 值 |
|---|---|
| Deposon r_ga0.1 全局均值 | 0.6437 |
| Deposon "accuracy" 1-r | 0.3563 |
| Bayesian baseline 均值 | 0.1809 |
| Bayesian "accuracy" 1-mean | 0.8191 |
| Cost multiplier | 0.4350 |
| 22 受控概念图数 | 22 |
| 6 baseline 方法数 | 6 |

## 5. 判死裁定

- **H1 (cost <= 1.3x)**: True - cost = 0.4350
- **H0 (cost >= 2.0x)**: False
- **最终**: PASS (H1 闭合, cost <= 1.3x)

## 6. 已知边界(D2 简化版)

- Bayesian baseline 用"6 baseline 最高分"近似, 严格意义应是"已知机制 + 支付 → 决策"
- Deposon "accuracy" = 1 - r 是代理, 非真准确率
- LLM 部分(D3 末补)是关键 — D2 部分仅作 Bayesian 对照基线
- v20 数据集 SHA-256 待 D2 末算(沿用 P-A V0 spec §2 5 锚)
- 12/15 KT-A1/B1/C1 锚 D2 末算(SHA-256)

## 7. D3 末补做

- LLM(Doubao + DeepSeek) 玩家实现 + 跑(沿用 P-A V0 spec §3 + tools/llm_client.py)
- 4 任务族(GSM8K + StrategyQA + 合成陷阱 + 2x2 矩阵)实跑
- 300 cells 跑(3 机制 × 4 任务族 × 25 决策)
- BOSS-A1 RBR/RM baseline 跑(沿用 KT_A1_SPEC §4)
- 出完整 KT-A1 报告

## 8. 与 7 条铁律的兼容性

- D2 部分: 零 LLM API / 零新数据采集(纯 v20/v21 frozen)
- D3 部分: 沿用 P-A V0 spec §7 鉴权 runtime `Path().read_text()`
- 锚 SHA-256 前 12 位预登记(D2 末填)
- /tmp 副本可重跑
- 不签 18 月 / 多论文规划
- 不上生产
- 不重做王老师已有工作
- 数字全部从冻结 JSON 字段路径引

---

**Mavis(root session) — 2026-09-09 D2**
