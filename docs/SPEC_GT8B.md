# SPEC GT-8b：「领域鉴定器 v0」real_semantics 轴的预登记复现

> 本文档先于 GT-8b 任何实验数据写盘（预登记证据）。
> 本轮含 LLM API 预算（预登记于 §4）；fetch 由主代理执行，
> ingest/eval 全程零 API，缓存缺失即停并清晰报告，绝不伪造数据。

## 1. 背景与假设

GT-8（docs/SPEC_GT8.md）复现了领域鉴定器 v0 的 hub_concentration 轴；
real_semantics 轴因需 LLM 先验 API 预算当时 deferred（SPEC_GT8 §6 如实
声明）。本轮补复现该轴。

既有语料证据（results/v20_graph_features.csv，族 L 4 图，
real_semantics=1）：llm_prior 的 named Hits@3（prior_named）=
0.484 / 0.690 / 0.783 / 1.000，全部 ≥0.48，且三张图显著高于
field_named（0.043–0.136）与 random_named（0.034–0.136）。

**H_GT8B**：v0 规则「real_semantics=1 ⇒ 先验强」在语料外成立——在
≥2 张**新真实语义域**脑图上，llm_prior 的 named Hits@3 显著高于
field 与 random，复现族 L 模式。逐域判定阈值（冻结，机械求值）：

    prior_named ≥ 0.6  且  prior_named > field_named + 0.2

（同时蕴含 prior_named > random_named + 0.2 需如实双报，但非判定条件；
族 L 既有 4 图中 3/4 满足该阈值，physics_concepts 0.484 为边界例外。）

## 2. 新域选择（冻结）

与既有族 L 全部 6 域（physics_concepts / biological_taxonomy /
algorithm_process / historical_causality / geography_world /
project_management）不同的真实语义域，冻结 2 个：

| 域 | 主题 brief（冻结，逐字写入 prompt） | 方向语义 |
|---|---|---|
| chemical_elements | 化学元素与周期律（抽象→具体：从「化学元素」逐层细化到周期/族/具体元素） | 类别指向其成员 |
| chinese_dynasties | 中国历史朝代（过程→结果：从早期朝代经关键制度/事件指向后继朝代与影响） | 前朝/原因指向后继/结果 |

生成 prompt 模板逐字沿用 mindmap_corpus_v20._PROMPT_TEMPLATE（与
build_familyL_prompts 同款，只换域 brief）；prompt_sha256 由
run_v20_gt8b_fetch.gt8b_prompt_manifest() 落盘，tests/test_v20_gt8b.py
作冻结域名哨兵。新图 real_semantics=1（真实语义标签，族 L 同口径）。

## 3. 协议

- 图摄入：仿 run_v20_familyL_ingest.py——缓存 → parse_familyL_response
  校验（30–45 节点 DAG）→ named/filler 按族 L 冻结口径（DAG 最长路径
  族=named，其余=filler）→ 图 JSON 写入 results/gt8b_cache/graphs/
  **独立目录**（不污染 corpus/v20，不进既有语料索引）。
- 先验臂：labels-only 零泄漏，与族 L 既有先验同一构造器
  llm_prior.build_prior_prompt，同模型 llm_prior.MODEL、同 endpoint
  llm_prior.ENDPOINT（保证与族 L 先验可比）。
- 评分：仿 run_v20_crossval_eval.py 全边留一、全候选协议（raw 口径，
  full_candidate_mask）；臂 = field_mean（prior_mean 起点）/ random /
  degree / llm_prior 四臂；每边 rng = default_rng(g_seed·100003+ei)，
  场实例种子 = g_seed+ei；指标 = named Hits@3（gold_rank < 3）。
- eval 零 API：只读 results/gt8b_cache/；任一缓存缺失 → 该域记
  fetch_failed/cache_missing，不计入判定分母，如实披露缺失文件清单。

## 4. API 预算（预登记）

- 族 L 图生成 2 prompt（每域 1）+ 先验臂 2 prompt（每域 1）= **4 prompt**；
- 每 prompt ≤ MAX_ATTEMPTS 次尝试，MAX_ATTEMPTS 照抄 llm_prior.MAX_ATTEMPTS
  = **2**；总 HTTP 尝试 ≤ 4 × 2 = **8**；
- key 仅从环境变量 KIMI_API_KEY 读取，不打印不落盘；错误经
  llm_prior._sanitize 兜底剔除；缓存带 prompt_sha256，新鲜即跳过；
- 超时/失败如实记 fetch_failed（沿用 GT-3 披露纪律），绝不重试超预算、
  绝不伪造响应。

## 5. 成功标准（预登记，机械求值）

- **支持**：2/2 有效新域满足 §1 阈值 ⇒ verdict = `supports_H_GT8B`；
- **判死**：2/2 有效新域全不满足 ⇒ verdict = `H_GT8B_dead`，如实宣布；
- **其余**（1/2，或有效域数 <2 含全部 fetch_failed）：
  `inconclusive`，如实报；
- fetch_failed 的域不计入分母，缺失文件清单逐字披露于结果 JSON。

## 6. 如实声明

- 样本仅 2 张新图（评审要求的下限设计），方向性证据，非效应量估计；
  0.6/0.2 阈值为复现族 L 模式的预登记工作阈值，非统计显著性检验。
- 先验臂与生成臂同模型族（kimi-for-coding）⇒ 同源污染风险在案
  （与 SPEC v2.0 §1 声明一致）。
- 仅真实语义域（族 L 口径）；结论不外推至族 S 合成图。
- 语料只读加载；既有 run_v20 系列文件一行不动（协议函数经只读
  import 复用）；不碰 paper/，不做 git 操作。

## 修正案 B1（2026-08-30，数据后登记、理由如实）

- 现象：chemical_elements 先验臂连续 3 次运行（共 6 次尝试）ReadTimeout(120s)，
  chinese_dynasties 先验一次成功；图生成两域均一次成功。
- 裁定：TIMEOUT 由 120s 提至 240s 重试一次（对超时域单次运行内 MAX_ATTEMPTS=2 次
  尝试）；预算修正为总 HTTP ≤ 9（已用 7，本次最多 +2）。模型与 endpoint 不变
  （保证与族 L 既有先验可比）。若仍失败，该域记 fetch_failed 不计入分母，
  verdict 按 SPEC §5 落 inconclusive，如实披露。
- 纪律：本修正案写于重试之前；run_v20_gt8b_fetch.py 文件本身不改（由主代理
  运行时 monkeypatch llm_prior.TIMEOUT，脚本 provenance 保持冻结）。
