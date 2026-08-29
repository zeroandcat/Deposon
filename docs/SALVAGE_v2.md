# SALVAGE_v2 — Deposon 可利用废稿成果清单

> 调查日期：2026-08-30。调查角色：只读 explore 子代理（未改仓库、无 git 操作）。
> 背景：仓库现行论文主线为 `paper/v2/deposon_paper_v2X.md`（博弈论转向），`paper/deposon_paper_v1_en.md` 为 v1.9 整改稿，`_paper_backup_v181/` 是其前版。

## 使用矩阵（results/ 下 JSON × 引用方）

| JSON | v2X 论文 | v1.9 论文 | docs | 状态 |
|---|---|---|---|---|
| deposon_v20_gt/gt2b/gt3/gt5b/gt6/gt7/gt8/gt8b | ✅ | — | ✅ | 已用 |
| deposon_v20_gt5.json | ⚠️ 仅文档级引用（附录 A 注明"results/ 下无 deposon_v20_gt5.json"——但**文件实际存在**，含 per_graph_detail） | — | GT_RECONSTRUCTION | 部分闲置 |
| deposon_v20_photonics.json | ❌ | ❌（§5.4 仅概念性表述） | Findings_v2.0_photonics（**已过期**：仍写 14/22） | 高价值闲置 |
| deposon_v20_vector_audit.json（1740 任务 0 违规） | ❌ | — | Findings_v2.0_boss | 闲置 |
| deposon_v15_diffusion_maxpath_negativeresult.json | ❌ | ❌ | SPEC_v1.5 | 闲置 |
| deposon_v16_llm_prior(_summary)、v17_fixed_sampler、v17_tieartifact_negativeresult | ❌ | ❌ | — | 闲置 |
| v1_3 labelfree/labelshuffle/resonant | — | ✅（正文以实验名引用，非文件名） | — | 已用（内容层） |
| v20_regression_field.json（v1 版） | ❌（v2X 引用 v2 版） | — | — | 被取代，闲置 |
| v19_quickwins/fullrank/meanfield、v20_baselines、fastcheck | ❌ | ✅（v19 三个） | ✅ | v2X 未承接 |
| gsm8k_details / strategyqa_details / Deposon_评估汇总 | ❌ | ❌ | 验证报告 | 细节级闲置 |
| corpus/v20：22 图 | ✅（经 corpus_eval） | — | — | **无未入语图**（阴性结论：22/22 全用） |

## Top-10（按价值×成本排序）

1. **Photonics 18/22 损耗预算 + 拓扑优化（P1–P4）** — `results/deposon_v20_photonics.json`、`deposon_photonics.py`。原始结论：18/22 图可探测、~2.9dB/跳、P1 公式级等价、P4 退火=相位斜坡可实现。闲置原因：v2X 博弈论转向后整条硬件线被砍，且 Findings 文档停留在 NEP 单位 bug 更正前的 14/22。用法：入 v2X §6 或附录（"硬件同构可行性"一段，直接呼应 v1.9 §5.4 的空头前瞻）；**顺手修正 Findings_v2.0_photonics.md 的 14/22→18/22（LESSON #19 的活案例）**。成本：低。
2. **GT-7 温度前沿全量数据** — `results/deposon_v20_gt7.json`（α∈{0.3..20}×4图×5seed，per_graph_detail）。v2X §5.5 只有一段话。用法：前沿曲线图 + 附录表，把"审计承诺只覆盖势"的边界定量化；是"win-win 被否"最完整的阴性数据集。成本：低。
3. **GT-5 反转 per-graph 明细** — `results/deposon_v20_gt5.json`（v2X 附录 A 误称文件不存在）。用法：① 更正附录 A 标注；② S6 gap=−0.31 等逐图数据入附录，支撑 log-linear learning / 探索-利用分工段（§5.2）；③ 直接成为下一轮 SPEC（GT-5c：温度-命中率-势三变量扫描已预写在 GT_RECONSTRUCTION §5）。成本：低。
4. **vector_audit（1740 任务、V1–V4 全 0 违规）** — 单纯形/非负/无 NaN 全链路审计，v2X 一字未提。用法：§5.6 守恒账/机制设计节加一句 + 附录一行（"分值域 [0,1] 单纯形，1740 任务 0 违规"）——低成本增强"可审计"主张。成本：低。
5. **GT-2B inconclusive 的设计失败分析** — `docs/Findings_GT2B.md` §4：固定 4 选项 ⇒ 图内候选数随 T 反比变化，"场免疫"判据被选项构成污染。用法：① 入方法工件（剂量-反应实验设计 checklist：免疫判据须对选项自由度稳健）；② 直接生成 GT-2C SPEC（可变选项数 + 配对检验 + 更大题库）。成本：低-中。
6. **λ=2 阴性消融的"反场 artifact"机制（E9.6）** — v1.9 §4.8/论文已录，但 v2X 未承接；机制（融合系数出凸包 ⇒ λ=2 时场系数 −1，先验空行按场降序排反）是可泛化教训。用法：入方法工件"融合权重审计"条款；或 v2X §6.3 局限补一句。成本：低。
7. **v1.5 maxpath 阴性 + G2 ensemble 阴性 + G3 Arrhenius 路径长度偏置** — `deposon_v15_diffusion_maxpath_negativeresult.json`、`g2_boltzmann_pathintegral_rewrite.json`、`g3_arrhenius.json`；v1.9 §5.2 有散文但 v2X 全砍。用法：v2X 阴性结果附录（"time-for-quality 无增益""barrier-语义失配"两条有独立方法论价值）；G3 的"barrier 高度须与语义风险正相关"是下一轮图构造 SPEC 的直接输入。成本：中。
8. **strategyqa_train.json（2290 例完整 BigBench 格式，仅 99 例入 v1.4）** — 可用性已验证（JSON 合法、examples=2290）。R2 指出未推送且获取路径未写。用法：① 入库/写获取命令修冷启动复现；② 支撑 v1 线"StrategyQA 扩样重测"SPEC（n=99→1000+，统计功效直接升级）。成本：低。
9. **deep_probe R1/R2 的可产品化协议** — R1 的"tiebreak 彩票归因法"（标签置换×tiebreak 种子零分布模拟）、零信号检测流程（LESSON #22）；R2 的冷克隆复现 checklist（9 条工程缺口）。v2X §6.4 只概述。用法：抽出为独立可复用《深探协议.md》（probe protocol：先复现后质疑 + 三类归因检验），作为方法论工件单独交付/入附录。成本：中。
10. **v181 被砍表述** — `_paper_backup_v181/deposon_paper_v1_en.md`：v1.9 压缩摘要砍掉了 (a) 双向解读框架的完整陈述、(b) label-shuffle 17.2%±6.4% / uniform-params 10% 的摘要级披露、(c) Related Work (a) 段对 ToT/GoT/Self-Consistency 的系统性 gap 分析。用法：workshop 长版/审稿 rebuttal 素材库；其中 (b) 的"transducer not discriminator"框架可回灌 v2X §6。成本：低。

## 边缘资产
- `audits_security.json`：已被 CLOSURE 引用，MD5 残留已裁定，无新增价值。
- `audits_outliers.json`：49 行 v19 边数据的异常扫描（284 异常 / 19 需注意），再生脚本在仓库外（R2 #5）——要么脚本入库要么弃；19 条 needs_attention 从未被逐条处置，是悬而未决的小账。成本：低。
- `audits_dataset_health.json`：同上，一次性产物。
- `quizbank_v20(_big).json`：已被 Findings 引用，v2X §4.3 已用，不闲置。

## 汇报用 Top-5
1. **Photonics 18/22**（含 Findings 文档 14/22 过期修正）→ v2X §6/附录，低成本高显示度。
2. **GT-7 温度前沿全量数据** → 附录图 + 审计边界定量化。
3. **GT-5 反转明细**（顺带更正 v2X 附录 A"文件不存在"的错误标注）→ 附录表 + GT-5c SPEC。
4. **vector_audit 1740 任务 0 违规** → 一句话进 §5.6，直接强化"可审计"主张。
5. **GT-2B 设计失败分析** → 方法工件 checklist + GT-2C SPEC。

## 重要负面/更正发现
1. corpus/v20 无未使用的图（22/22 全入 corpus_eval）。
2. v2X 附录 A 称"results/ 下无 deposon_v20_gt5.json"——**文件实际存在**，属 LESSON #19 类文档-数据漂移，建议优先修正。
3. Findings_v2.0_photonics.md 的 14/22 与"14 跳规则"是 NEP 单位 bug 更正前的旧值，JSON 已更正为 18/22（阈值 ≈27 跳），文档未跟进。
4. 调查未对仓库做任何修改、未执行 git 操作。
