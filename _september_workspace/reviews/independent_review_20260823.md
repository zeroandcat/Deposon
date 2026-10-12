# 独立审校与补实验建议汇总（2026-08-23）

来源：两个互不知情的子代理（论文审校 reviewer / 实验方案 explore）。本文件为 Orchestrator 汇总，不改写其结论。

## 论文审校要点
- 最大退稿点：§4.7“优势成立”与 D.4“非统计显著”口径张力；overall 优势实为 2/49 边，named 5/17 vs 3/17。
- 单图 n=1、留一边共享 48 观测边导致边相关；人工单人转译且 named/filler 切分人工；λ 四档全等同可疑；先验方向反转；零泄漏只覆盖 prompt 层，不能排除训练污染。
- 建议：Table 13 加命中计数；正文首句改“描述性最优/非显著”；逐 λ 或机制说明；补负采样规程、prompt 全文、commit/日期列；局限加单图/边相关/人工切分。

## 实验方案要点
- 多负采样只能降 Monte Carlo 误差，不能把 49 边当 980 独立任务；W_done 不能跨负采样组精确复用（mask 改变扩散自由度），全候选超集复用属另一协议。
- λ 根因：field 量纲小 + 先验稀疏；0.25×0.95≈0.238 已覆盖行内 field 范围中位 0.053/最大 0.224。
- 发现 legacy 负采样池未显式排除金边 v：抽中 v 时实际少一个独特负样本；须标 legacy_sampler 并做 fixed_sampler 敏感性。
- 校准只能无真值相对归一/方向敏感性；不得按真边重合做 Platt/isotonic，否则偷看结构。

## 已执行（零 API）
- v1.7.1 同协议归一融合 + 阴性对照（results/deposon_v17_fusion_fix.json）；tie-artifact 首轮归档并修复。
- fixed_sampler 敏感性（results/deposon_v17_fixed_sampler.json）。
- 20 图 filler 随机重挂稳健性（results/deposon_v17_multigraph.json）。
