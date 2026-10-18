# Findings GT-8b：「领域鉴定器 v0」real_semantics 轴预登记复现（含修正案 B1）

> 预登记：docs/SPEC_GT8B.md（先于任何 GT-8b 数据写盘；修正案 B1 写于
> 240s 重试之前，理由与预算修正如实登记）。
> 结果：results/deposon_v20_gt8b.json（eval 零 API，runtime 2.83s）；
> 摄入：results/deposon_v20_gt8b_ingest.json；
> 缓存：results/gt8b_cache/（原始响应 + graphs/ 独立目录）。
> **2026-08-30 翻转注记：verdict 已由 inconclusive 翻转为
> supports_H_GT8B，见 §7；§1–§6 为历史记录，不回溯改写。**

## 1. 结果

**verdict = inconclusive**（机械求值，非手写；见 §2）。

| 域 | 图 | N | E | named | llm_prior | field_mean | random | degree | 逐域判定 |
|---|---|---|---|---|---|---|---|---|---|
| chinese_dynasties | L_chinese_dynasties | 45 | 57 | 41 | **0.7805** | 0.0732 | 0.0244 | 0.0488 | **满足**（≥0.6 且 > field+0.2） |
| chemical_elements | L_chemical_elements | 37 | 63 | 28 | — | — | — | — | **fetch_failed**（先验臂无缓存，不计分母） |

- L_chinese_dynasties（named Hits@3，raw 口径 full_candidate_mask）：
  llm_prior 0.7805 / field_mean 0.0732 / random 0.0244 / degree 0.0488。
  prior−field = **+0.7073**，prior−random = **+0.7561**（后者按 SPEC §1
  如实双报，非判定条件）。满足预登记阈值（prior_named ≥ 0.6 且
  prior_named > field_named + 0.2）。
- L_chemical_elements：**图生成成功**（N=37 / E=63 / named=28，
  real_semantics=1，摄入校验通过），但**先验臂 fetch_failed**——
  prior_chemical_elements.json 缓存缺失，该域无法评分。

## 2. verdict 的机械原因（如实，不美化）

按 SPEC_GT8B §5：支持需 2/2 有效域满足阈值；判死需 2/2 全不满足；
其余落 inconclusive。本轮 **n_valid_domains = 1 < min_domains = 2**
（fetch_failed 不计入判定分母），domains_satisfied =
[chinese_dynasties]，domains_unsatisfied = []——既不满足「支持」的
2/2，也不满足「判死」的 2/2，故机械落 **inconclusive**。

方向性观察（如实陈述，非结论）：在**唯一有效域**上先验碾压
（0.7805 vs field 0.0732 / random 0.0244 / degree 0.0488），与族 L
既有 4 图 real_semantics=1 模式（llm_prior 0.484–1.000 全部显著高于
field/random）**同向**；缺失的 chemical_elements 域无先验数据，无法
计入任何方向的证据。

## 3. fetch_failed 完整披露

- **现象**：chemical_elements 先验臂连续 **3 次运行、共 6 次尝试**
  全部 ReadTimeout(120s)（llm_prior.TIMEOUT 默认值）；chinese_dynasties
  先验臂一次成功；两域图生成均一次成功。
- **修正案 B1 处置**：TIMEOUT 提至 **240s 重试一次**（单次运行
  MAX_ATTEMPTS=2），结果**仍失败**——返回错误为**空 content**
  （响应体内容为空，非解析失败）。该域按 SPEC §5 记 fetch_failed，
  不计入分母；缺失文件清单已逐字写入结果 JSON 的 cache_missing 字段。
- **可比性**：失败与成功臂使用**同一模型**（llm_prior.MODEL）与
  **同一 endpoint**（llm_prior.ENDPOINT），与族 L 既有先验完全一致；
  模型/endpoint 配置全程未变（修正案 B1 明确冻结）。
- **类比（标注为推测）**：与 GT-3 时代 deepseek max_tokens=8000 被
  reasoning 耗尽返回空内容的现象相似——一种假设是 chemical_elements
  标签集触发了更长的内部 reasoning，在 120s/240s 内未产出可见 content。
  **此解释仅为推测**，未做对照验证，如实标注。
- **纪律**：绝不重试超预算、绝不伪造响应；fetch 脚本本身未改
  （超时由运行时 monkeypatch，脚本 provenance 保持冻结）。

## 4. 预算台账（与修正案 B1 一致）

| 用途 | 尝试次数 | 结果 |
|---|---|---|
| 图生成 chemical_elements | 1 | 成功 |
| 图生成 chinese_dynasties | 1 | 成功 |
| 先验臂 chinese_dynasties | 1 | 成功 |
| 先验臂 chemical_elements（3 次运行 + B1 重试） | 6 | 全部失败 |
| **合计 HTTP** | **9** | = 修正案 B1 预算上限（≤9） |

原预登记预算 ≤8（4 prompt × MAX_ATTEMPTS 2）；修正案 B1 修正为 ≤9
（已用 7，重试最多 +2），实际总 HTTP = 9，恰达修正后上限，未超支。
key 仅从环境变量读取，不打印不落盘；错误信息经 _sanitize 兜底剔除。

## 5. 局限性

1. **单有效域方向性证据非结论**：inconclusive 如实落盘；0.78 vs 0.07
   的差距只在 1 张新图上成立，不构成 H_GT8B 的 2/2 支持。
2. **自选择偏差风险（如实讨论）**：timeout 失败本身可能并非随机事故——
   chemical_elements 的标签集（元素/周期/族）对模型而言可能更难生成
   labels-only 先验，导致长 reasoning 与超时。若失败概率与「先验任务
   难度」相关，则「唯一有效域上先验碾压」存在幸存者偏差：恰好是
   先验容易成功的域被观测到。本设计无法区分「网络事故」与「难度相关
   失败」，如实披露。
3. **样本仅 2 张新图**（评审要求的下限设计）：即便 2/2 有效，也只是
   方向性证据；0.6/0.2 阈值为预登记工作阈值，非统计显著性检验。
4. **real_semantics 轴复现仍待后续预算**：chemical_elements 先验臂
   需在后续预算窗口补 fetch（或换域重试并如实登记新修正案）。
5. 先验臂与生成臂同模型族 ⇒ 同源污染风险在案（与 SPEC v2.0 §1
   及 SPEC_GT8B §6 声明一致）。

## 6. 复现性

- 缓存结构（results/gt8b_cache/）：
  - `chemical_elements.json`（图生成原始缓存，文件 sha256 =
    7250d55070b866ae8bbfe63799af9a8680b8c1c4f6f48989df6fb40f6e24d1b8，
    prompt_sha256 = f668d326…5a049bb）
  - `chinese_dynasties.json`（图生成原始缓存，文件 sha256 =
    8460cf6ef12cfa8ac90a5ef39dcb48e480f48db872b90b63b275f165f4743c0f，
    prompt_sha256 = 35cf271a…4caf7b8798f）
  - `prior_chinese_dynasties.json`（先验臂缓存，文件 sha256 =
    d7ac5a401aa71304d8ba42877bc53fef4fa4bb1d35de8dbc741ff84b24c40a04，
    prompt_sha256 = d3874fb599faf1709e3de8b77e30731e17ec8553889b1b2fe22ff6f18332435d）
  - `prior_chemical_elements.json` **缺失**（fetch_failed，如实披露）
  - `graphs/L_chemical_elements.json`（sha256 =
    021ded78803b16036c6a3673f93fed591d121a59396019b130bde4e72598d3ec）
  - `graphs/L_chinese_dynasties.json`（sha256 =
    7a7b397c2ca6bd6ed3fd6e9bba302a377c6011f5f6aecc192cdf5cc6ee462168）
  - 每缓存含 domain / kind / prompt_sha256 / model / response_text /
    note 六字段；prompt 全文不落本文档，经 prompt_sha256 锚定。
- 种子与评分协议：config seed=0；每边 rng =
  default_rng(g_seed·100003+ei)；场实例种子 = g_seed+ei（与
  run_v20_corpus_eval 逐行同式）；全边留一、全候选 raw 口径。
- 测试：tests/test_v20_gt8b.py 9 项（冻结域名哨兵等）；全套
  **pytest 255 passed**（36.73s），无回归。

## 7. 更正/翻转注记（2026-08-30）：verdict 由 inconclusive 翻转为 supports_H_GT8B

§1–§6 为初轮（修正案 B1 为止）历史记录，如实保留、不回溯改写；本节追加
补数后的最终口径。

- **补数经过**：chemical_elements 先验臂经修正案 B2（TIMEOUT 300s、
  MAX_ATTEMPTS=3 诊断性重试）仍返回空 content，诊断证据落盘——响应 usage
  显示 completion_tokens 全耗于 reasoning_tokens、finish_reason=length，
  根因定位为推理模型 reasoning 耗尽 max_tokens（默认 4000）；修正案 B3 仅
  放宽 max_tokens=32000，**一次成功**（response_text 长 1510），缓存落盘
  results/gt8b_cache/prior_chemical_elements.json（文件 sha256 =
  68abf13024673d3e9300352b4e58770d7e8abac75274a6fe8f94c9625acf5b05，
  prompt_sha256 = a1f01ba0…721a1f）。追加预算经用户授权适当放宽，如实
  登记。随后重跑 ingest+eval（全程零 API，只读缓存），结果覆写
  results/deposon_v20_gt8b.json。
- **最终判定**（机械求值，非手写）：**verdict = supports_H_GT8B**，
  n_valid_domains = 2/2，domains_satisfied = [chemical_elements,
  chinese_dynasties]，domains_unsatisfied = []：

  | 域 | llm_prior | field_mean | random | degree | prior−field | 逐域判定 |
  |---|---|---|---|---|---|---|
  | chemical_elements | **0.6429** | 0.1429 | 0.0357 | 0.0000 | **+0.5000** | **满足**（≥0.6 且 > field+0.2） |
  | chinese_dynasties | **0.7805** | 0.0732 | 0.0244 | 0.0488 | **+0.7073** | **满足**（≥0.6 且 > field+0.2） |

  两域均满足 SPEC §1 冻结阈值（prior_named ≥ 0.6 且 prior_named >
  field_named + 0.2），2/2 有效域 ⇒ 按 SPEC §5 机械落
  **supports_H_GT8B**；结果 JSON 的 cache_missing 字段现已为空（{}）。
- **对 §2/§5 历史讨论的处置**：初轮 inconclusive 的机械原因
  （n_valid=1<2）随补数不再成立；§5.2 的幸存者偏差讨论针对「失败可能
  与难度相关」的假设，B2/B3 诊断把失败归因于 max_tokens 耗尽的截断事故
  （finish_reason=length），而非先验臂在该域系统性更弱——补数后该域
  prior_named=0.6429 同样越过阈值，与「难度相关失败」假设不同向。§5.2
  原文保留为历史记录。
- **仍有效的限定**：样本仅 2 张新图，方向性证据非效应量估计；0.6/0.2
  阈值为预登记工作阈值，非统计显著性检验；同源污染风险在案（§5.5）。
- **纪律复核**：补数全程 key 仅从环境变量读取、labels-only 零泄漏
  prompt、缓存带 prompt_sha256 落盘；fetch 脚本未改（参数运行时
  monkeypatch）；eval 零 API；tests/test_v20_gt8b.py 9 项全绿。
