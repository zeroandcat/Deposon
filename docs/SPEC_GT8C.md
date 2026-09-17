# SPEC GT-8c：「领域鉴定器 v0」real_semantics 轴扩样（Ark 后端）预登记

> 本文档先于 GT-8c 任何实验数据写盘（预登记证据）。
> 本轮含 LLM API 预算（预登记于 §4）；fetch 由主代理执行（密钥运行时
> 内联注入，脚本只从环境变量 ARK_API_KEY 读取），ingest/eval 全程零 API，
> 缓存缺失即停并清晰报告，绝不伪造数据。
> GT-8c 是 GT-8b（docs/SPEC_GT8B.md，含修正案 B1–B3）的修正案式扩展：
> 未显式改写的条款（协议、阈值、判读规则、零泄漏纪律、如实声明）逐字
> 沿用 SPEC_GT8B。

## 1. 背景与假设

GT-8b 在 2 个新真实语义域（chemical_elements / chinese_dynasties，Kimi
后端）上复现了 v0 规则「real_semantics=1 ⇒ 先验强」。本轮沿 real_semantics
轴扩样，并将后端切换为火山引擎 Ark（vendor=volces_ark_bytedance，
model=doubao-seed-evolving），同时检验「先验强」模式的跨后端稳健性
（与 GT-3b 跨厂商动机一致，docs/SPEC_GT3.md 修正案 A2）。

**H_GT8C**：在 2 张**新真实语义域**脑图（Ark 后端生成 + Ark 先验）上，
llm_prior 的 named Hits@3 显著高于 field 与 random，复现族 L / GT-8b
模式。逐域判定阈值（冻结，机械求值，与 GT-8b 完全同口径）：

    prior_named ≥ 0.6  且  prior_named > field_named + 0.2

（同时如实双报 prior_named − random_named，非判定条件。）

## 2. 新域选择（冻结）

| 域 | 主题 brief（冻结，逐字写入 prompt） | 方向语义 |
|---|---|---|
| biological_taxonomy | 生物分类（抽象→具体：从「生物分类」逐层细化到界/门/纲/目/科/属/种与代表物种，方向语义 = 类别指向其成员） | 类别指向其成员 |
| programming_concepts | 编程概念（抽象→具体：从编程范式细化到语言特性再到具体语言/构造，方向语义 = 概念指向其实例） | 概念指向其实例 |

注意（如实声明）：biological_taxonomy 与既有族 L 域名相同，但 GT-8c 的
图由 **Ark 后端重新生成**，先验亦由 Ark 给出——全部产物（图、先验、
缓存）均为新数据，与族 L 既有 Kimi 产物不共享任何缓存；本轮同时构成
「同域换后端」的稳健性对照。programming_concepts 为全新域。

生成 prompt 模板逐字沿用 mindmap_corpus_v20._PROMPT_TEMPLATE（只换域
brief）；prompt_sha256 由 run_v20_gt8c_fetch.gt8c_prompt_manifest() 落盘，
tests/test_v20_gt8c.py 作冻结域名哨兵。新图 real_semantics=1。

## 3. 协议（沿用 GT-8b，仅改后端与目录）

- 图摄入：仿 run_v20_gt8b_ingest.py——缓存 → parse_familyL_response
  校验（30–45 节点 DAG）→ named/filler 按族 L 冻结口径（DAG 最长路径
  族=named，其余=filler）→ 图 JSON 写入 results/gt8c_cache/graphs/
  **独立目录**（不污染 corpus/v20，不动 results/gt8b_cache）。
- 先验臂：labels-only 零泄漏，同构造器 llm_prior.build_prior_prompt
  （prompt 只含标签列表）；后端 = Ark（见 §4）。
- 评分：仿 run_v20_gt8b_eval.py / run_v20_crossval_eval.py 全边留一、
  全候选协议（raw 口径，full_candidate_mask）；臂 = field_mean
  （prior_mean 起点）/ random / degree / llm_prior 四臂；每边
  rng = default_rng(g_seed·100003+ei)，场实例种子 = g_seed+ei；
  指标 = named Hits@3（gold_rank < 3）。
- eval 零 API：只读 results/gt8c_cache/；任一缓存缺失 → 该域记
  fetch_failed/cache_missing，不计入判定分母，如实披露缺失文件清单。

## 4. 后端与 API 预算（预登记）

- 后端：**火山引擎 Ark**，endpoint =
  https://ark.cn-beijing.volces.com/api/v3/chat/completions，
  model = **doubao-seed-evolving**，vendor 字段 =
  volces_ark_bytedance（落盘于每条缓存记录）。
- 图生成 2 prompt（每域 1）+ 先验臂 2 prompt（每域 1）= **4 prompt**；
  每 prompt ≤ MAX_ATTEMPTS 次尝试，MAX_ATTEMPTS = **2**；
  总 HTTP 尝试 ≤ 4 × 2 = **8**。
- **预登记 max_tokens = 32000、timeout = 300s**（吸收 GT-8b 修正案
  B2/B3 教训：doubao 系推理模型 reasoning_tokens 可耗尽 max_tokens，
  finish_reason=length 而 content 为空；直接按 B3 成功参数登记，避免
  重蹈 B1/B2 的预算追加）。
- key 仅从环境变量 **ARK_API_KEY** 读取，不打印不落盘；错误经
  llm_fetch.sanitize_secret（llm_prior._sanitize 同式）兜底剔除；
  缓存带 prompt_sha256，新鲜即跳过；预算计数（total_http_attempts）
  落盘 results/gt8c_cache/budget.json。
- 超时/失败如实记 fetch_failed（沿用 GT-3/GT-8b 披露纪律），绝不重试
  超预算、绝不伪造响应。

## 5. 成功标准（预登记，机械求值，纯函数 gt8c_verdict，先承诺）

- **支持**：2/2 有效新域满足 §1 阈值 ⇒ verdict = `supports_H_GT8C`；
- **混合**：恰好 1/2 有效域满足 ⇒ verdict = `mixed`，如实报；
- **判死**：2/2 有效域全不满足 ⇒ verdict = `H_GT8C_dead`，如实宣布；
- **其余**（有效域数 < 2，含全部 fetch_failed）：`inconclusive`，如实报；
- fetch_failed 的域不计入分母，缺失文件清单逐字披露于结果 JSON。
- 实现：run_v20_gt8c_eval.gt8c_verdict 为纯函数，判定常量
  GT8C_PRIOR_MIN=0.6 / GT8C_MARGIN=0.2 / GT8C_MIN_DOMAINS=2 冻结于代码，
  由 tests/test_v20_gt8c.py 锁定边界（含阈值恰等情形）。

## 6. 如实声明

- 样本仅 2 张新图（评审要求的下限设计），方向性证据，非效应量估计；
  0.6/0.2 阈值为复现族 L/GT-8b 模式的预登记工作阈值，非统计显著性检验。
- 图生成臂与先验臂同后端同模型（doubao-seed-evolving）⇒ 同源污染风险
  在案（与 SPEC v2.0 §1、SPEC_GT8B §6 声明一致）；与 GT-8b（Kimi 后端）
  的跨后端一致性为次要观察，非判定条件。
- 仅真实语义域（族 L 口径）；结论不外推至族 S 合成图。
- 语料只读加载；既有 gt8b 系列文件、results/gt8b_cache、paper/ 一行不动
  （协议函数经只读 import 复用）；不做 git 操作。
- 密钥纪律：脚本与文档不含任何明文密钥；key 仅在主代理执行 fetch 时经
  环境变量 ARK_API_KEY 注入。
