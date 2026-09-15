# KT-A1 LLM 30 cells Mini Test (2026-09-09)

> **作者**: Mavis(root session, V1 折中补 Phase B 真实跑)
> **位置**: `docs/V3X/KT_A1_LLM_30_CELLS_2026_09_09_mavis.md`
> **说明**: 用 M4_LLM_Doubao 真实调 API(不是简化版 random)

## 1. 一句话结果

- 7/30 正确 = 23.3%
- 30 cells: 3 任务族(GSM8K / StrategyQA / Trap) × 10 决策

## 2. 关键数字

| 任务族 | 正确数 / 总数 | 准确率 |
|---|---|---|
| T1_GSM8K | 1/10 | 10.0% |
| T2_StrategyQA | 1/10 | 10.0% |
| T3_Trap | 5/10 | 50.0% |

- 总: 7/30 = 23.3%

## 3. 已知边界(诚实声明)

- 30 cells 仅 mini test, 完整 300 cells 沿用 V1 折中补 D3-D4(6-12 小时 API)
- M1_Deposon_TRA 暂退化 random(无 scatter_weight 字段), 此处用 M4_LLM_Doubao 替代
- 7 条铁律: API key runtime 读, 不入 prompt

## 4. 与 7 条铁律兼容性

- 数据从 frozen JSON 字段路径引
- /tmp 副本可重跑
- 不碰 HANDOFF_MACHINE_READABLE.json
