# 数据集健康审计 v2（dataset-health-audit）

- 日期：2026-08-28
- 工具：`/app/.agents/skills/dataset-health-audit/scripts/data_quality_checker.py`（12 维质检，pandas/numpy）
- 对象：results/ 主要 CSV/JSON 数据集 + corpus/ 语料索引；嵌套 JSON 已用 `pandas.json_normalize` 抽取为表格后审计（quizbank items / deposon_v20_* 顶层对象）。

## 1. 总览评分表

| 数据集 | 行×列 | 总分 | 等级 | 主要扣分维度 |
|---|---|---|---|---|
| results/v20_graph_features.csv | 20×14 | 90.48 | A | 缺失值(94.3)、数值范围(16.7)、列名(93.3) |
| results/v19_edges_audit_input.csv | 49×18 | 94.78 | A | 数值范围(83.3)、列名(79.0)、基数(50.0) |
| results/quizbank_v20.json（items 抽取） | 40×15 | 98.33 | A+ | 常量列(66.7) |
| results/quizbank_v20_big.json（items 抽取） | 157×11 | 97.73 | A+ | 常量列(72.7)、基数(81.8) |
| results/deposon_v20_gt.json（抽样①，扁平化） | 1×76 | 94.94 | A | 常量列*（单行工件固有） |
| results/deposon_v20_gt3.json（抽样②，扁平化） | 1×39 | 92.25 | A | 常量列*；per_domain 内含 fetch_failed |
| results/deposon_v20_bigquiz_eval.json（抽样③，扁平化） | 1×67 | 95.0 | A+ | — |
| results/deposon_v20_corpus_eval.json（抽样④，扁平化） | 1×491 | 93.9 | A | 常量列* |
| results/deposon_v20_baselines.json（抽样⑤，扁平化） | 1×357 | 93.81 | A | 常量列* |
| corpus/v20/ 语料索引（23 文件汇总表） | 23×3 | 90.0 | A | — |

\* 单行实验结果 JSON 扁平化后"常量列"是方法学固有产物（单行必然每列常量），不计真实问题。

## 2. 12 维要点（按真实问题维度）

| 维度 | 状态 | 说明 |
|---|---|---|
| 缺失值 | ⚠️ | v20_graph_features.csv `prior_named` 缺失 16/20（80%）——**结构性缺失**：S 族 16 图本无 LLM 先验，L 族 4 图 100% 齐全。非数据损坏。 |
| 重复行 | ✅ | 全部数据集 0 完全重复行；quizbank_big item_id 157/157 唯一。 |
| 类型一致性 | ✅ | 各列无混杂类型。 |
| 数值范围/异常值 | ⚠️(多为良性) | v20_graph_features 的 real_semantics/diff 类列 IQR 越界系 0/1 指示变量与稀疏计数所致；v19_edges 的 *_hit 二值列同理。hub_concentration 1-2 个真离群点（max 0.25），建议人工确认对应图。 |
| 格式合规 | ✅ | 无需格式校验字段异常。 |
| 唯一性 | ✅ | quizbank item_id 全唯一。 |
| 空白字符串 | ✅ | 0 命中。 |
| 常量列 | ℹ️ | quizbank 两库中 bloom_level/question_type/difficulty 等为设计性常量（规范固定值），非缺陷；单行 JSON 见上注。 |
| 分布偏斜 | ℹ️ | 二值/命中率列天然偏斜，无需处理。 |
| 列名规范 | ⚠️ | v19_edges 含 `hybrid_norm@0.5_hit` 等特殊字符列名（4 列）；v20_graph_features 大小写风格混用（graph_id vs N）。 |
| 基数异常 | ℹ️ | v19_edges 二值列基数=2 被工具标记（50 分），系指标列固有。 |
| 跨列一致性 | ✅ | 未发现逻辑矛盾。 |

## 3. 问题清单（按优先级）

1. **DQ-1（info/结构性）** v20_graph_features.csv `prior_named` 80% 缺失：仅 L 族有值。建议：S 族显式填 `NA` 语义标记或拆列注释，避免下游 pandas 均值被静默稀释。
2. **DQ-2（low）** deposon_v20_gt3.json per_domain 内存在 4 处评估者 `fetch_failed`（algorithm_process×2、historical_causality×1、project_management×2 中各 1-2 个评估者，named_hits3=null）。建议：重跑 fetch 补齐或在评估汇总中显式标注缺失评估者。
3. **DQ-3（low）** v19_edges_audit_input.csv 4 列列名含 `@` 特殊字符，部分下游工具/SQL 不友好。建议改名为 `hybrid_norm_0p5_hit` 风格（迁移成本高则维持并文档化）。
4. **DQ-4（info）** v20_graph_features.csv `hub_concentration` 2 个 IQR 离群点（含 max=0.25），建议确认对应图为真实 hub 结构而非生成错误。
5. **DQ-5（info）** quizbank 常量列为规范设计，建议在 schema 文档中注明，避免后续审计重复标记。

## 4. 与既有 audits_dataset_health.json 增量对比

- 基线仅覆盖 `v19_edges.csv`（94.78/A）。本轮同一文件（v19_edges_audit_input.csv）得分 **94.78，完全一致，无回归**。
- 本轮新增覆盖 9 个数据集，全部 ≥90 分（A/A+），无 C 级以下数据集。
- 无新增重复行/类型混乱/空白字符串问题；唯一新增实质项为 DQ-2（gt3 fetch_failed 评估者缺口）。

## 5. 修复建议汇总

| 优先级 | 项 | 动作 |
|---|---|---|
| P2 | DQ-2 | 重跑 run_v20_gt3b/c_fetch 补齐 4 个 fetch_failed 评估者，或在汇总 JSON 标注 missing_evaluators |
| P3 | DQ-1 | prior_named 缺失语义文档化（S 族无先验属设计） |
| P3 | DQ-3/DQ-4/DQ-5 | 列名规范化与 schema 注释，低优先 |
