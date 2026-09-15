# KT-C1 报告 — D1 跑 (2026-09-09)

> **作者**: Mavis(root session, 一周判死自由推进)
> **状态**: V0(草稿)
> **位置**: `docs/V3X/KT_C1_REPORT_2026_09_09_mavis.md`
> **锚**: `KT_C1_V21_FROZEN` = `9d9ae5001c57` (SHA-256 前 12 位)

---

## 1. 一句话结果

**死 (幂律不成立)**

- N = 328 cyclic tasks
- 斜率 b = 0.2838
- R^2 = 0.0007
- b 95% bootstrap CI: [-0.8523, 1.5760]
- 判死线 1 (R^2<0.3): True
- 判死线 2 (b CI 含 0): True

## 2. 数据

- 源: `results/deposon_v21_gtformal.json`(frozen, 锚 `9d9ae5001c57`)
- 样本: 含环 cyclic=True 且 r > 0 的 task
- 总状态: 6760, 含环任务: 328

## 3. d 代理方法

按 KT_C1_SPEC_V0 §3 "d = |E| - |V| + c" 标准公式, 但 v21 frozen JSON 未显式提供 |E|, |V| 字段.
**本报告用 d = n_nodes(节点数)作为 d 的代理**(沿用 SPEC §12 已知未决项, D1 pilot n=20 待 v3x 子代理锁定更精确的 d 计算方法).

| 图族 | n 范围 | task 数 |
|---|---|---|
| chain | n=2 | 2 |
| chain | n=3 | 3 |
| chain | n=4 | 4 |
| chain | n=5 | 5 |
| chain | n=6 | 6 |
| chain | n=7 | 7 |
| chain | n=8 | 8 |
| cyclic | n=3 | 15 |
| cyclic | n=4 | 20 |
| cyclic | n=5 | 10 |
| cyclic | n=6 | 18 |
| cyclic | n=7 | 14 |
| cyclic | n=8 | 24 |
| dag | n=4 | 12 |
| dag | n=5 | 5 |
| dag | n=6 | 6 |
| dag | n=7 | 42 |
| dag | n=8 | 24 |
| star | n=3 | 6 |
| star | n=4 | 8 |
| star | n=5 | 10 |
| star | n=6 | 12 |
| star | n=7 | 14 |
| star | n=8 | 16 |
| tree | n=4 | 12 |
| tree | n=6 | 12 |
| tree | n=7 | 7 |
| tree | n=8 | 16 |


## 4. 拟合模型

```
log10(r) = b * log10(d) + a + eps   (OLS)
d = n_nodes
```

## 5. 关键数字

| 数字 | 值 |
|---|---|
| N | 328 |
| 斜率 b | 0.2838 |
| 截距 a | -0.5765 |
| R^2 | 0.0007 |
| b 95% parametric CI | [-0.9180, 1.4856] |
| b 95% bootstrap CI | [-0.8523, 1.5760] |
| Bootstrap 样本 | 10000 / 10000 |
| 中位 r | 0.6689 |
| r > 0.30 占比 | 0.9238 |

## 6. 判死裁定

- **判死线 1 (R^2 < 0.3)**: True - R^2 = 0.0007
- **判死线 2 (b 95% CI 含 0)**: True - b CI = [-0.8523, 1.5760]
- **最终**: 死 (幂律不成立)

## 7. 已知边界

- d = n_nodes 是代理, 非严格循环空间维数(SPEC §12 已知未决项)
- bootstrap seed = 210021(沿用 v21 frozen seed)
- 数据已冻结, D1 末可重跑(锚 `9d9ae5001c57` 验证)
- 若 d 用 |E|-|V|+c 严格推, 结果可能不同(待 v3x 子代理 D1 pilot 锁定)

## 8. 与 7 条铁律的兼容性

- 数据已冻结, 零 LLM API 调用
- 锚 SHA-256 前 12 位预登记
- /tmp 副本可重跑(沿用 verifier 纪律)
- 不签 18 月 / 多论文规划
- 不上生产
- 不重做王老师已有工作
- 数字全部从冻结 JSON 字段路径引

---

**Mavis(root session) — 2026-09-09 D1**
