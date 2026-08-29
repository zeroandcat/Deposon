# ARCH_AUDIT v2 — Deposon 核心实现架构审计（code-arch-optimizer / 只读探索）

日期：2026-08-29。范围：`deposon_diffusion.py`、`deposon_fast.py`、`deposon_agents_v1_3/v1_4.py`、`deposon_g2_modes.py`、`deposon_photonics.py`、`llm_prior.py`、`mindmap_corpus_v20.py`、`run_v15`–`run_v20_*` 实验族（41 个顶层脚本，其中 25+ 个 run_v20_*）。审计为只读；未改任何代码。

## 总体判断

仓库有一个真正深的核心（`deposon_diffusion.py`，370 行，forward/reverse/complete 三入口）和一圈**把实验脚本当库用**的浅壳。最大的架构摩擦不在核心内部，而在接缝上：

1. **同一段反向退火循环被逐行复制了 5 份**（每份只加一个旋钮：早停 / 轨迹记录 / α 浓度）。
2. **"场评估协议函数" 没有家**——`row_normalize`、`field_scores_init`、`full_candidate_mask`、`prior_score_matrix` 等事实上的公共协议定义在 `run_v15/v16/v17/v19` 等**实验脚本**里，被 18 个下游脚本跨文件 import，import 一个协议函数就拖入该脚本的全部模块级常量与 `main()`。
3. **LLM 先验获取管道被复制了 9 份**（`llm_prior.py` + 8 个 `*_fetch.py`），因为端点/模型被硬编码成模块常量，换模型只能整文件复制。
4. `deposon_agents_v1_3.py` 与 `v1_4.py` 是两棵 1800 行的同名类层级 fork（diff ≈400 行），概念上是一个系统。

理解一个核心概念需要跳的文件数（实测）：
- "场分 field_scores 协议"：`run_v20_crossval_eval.py` 一个 eval 脚本就要打开 8 个模块（deposon_diffusion、mindmap_corpus_v20、llm_prior、run_v15、run_v16、run_v17、run_v19_fullrank、run_v19_meanfield、run_v20_corpus_eval）。
- "反向退火更新规则"：要看 deposon_diffusion.py:290 + run_v19_meanfield.py:31 + deposon_fast.py:32 + run_v20_gt5.py:79 + run_v20_gt7.py:66 共 5 处逐行相同的循环，才能确认"它们真的等价"。

---

## 实验脚本复制网（grep 级量化）

### A. 协议函数跨文件 import 扇入（importing 脚本数，含 tests/）

| 协议函数 | 定义位置 | 被 import 的脚本数 |
|---|---|---|
| `row_normalize` | run_v15_experiment.py:47 | **18** |
| `full_candidate_mask` | run_v19_fullrank.py:24 | **14** |
| `field_scores_init` | run_v19_meanfield.py:78 | **11** |
| `prior_score_matrix` | run_v16_llm_prior.py:55 | **11** |
| `gold_rank` | run_v19_fullrank.py:44 | 8 |
| `mean_std` | run_v15_experiment.py:117 | 7 |
| `arm_scores` | run_v15_experiment.py:77 | 6 |
| `minmax_mask` | run_v17_fusion_fix.py:27 | 4 |
| `reconstruct_mindmap` | run_v15_experiment.py:237 | 3 |
| `sign_test` | run_v19_quickwins.py:28 | 1 |
| `eval_prior_arm` | run_v20_crossval_eval.py | 1 |

run_v20_* 中单个脚本最多 13 条非标准库 import（crossval_eval / bigquiz_eval / gt8b_eval），其中 5–6 条指向其他 run_* 脚本。

### B. 反向退火主循环复制（"既有文件一行不动"惯例的产物）

逐行相同（仅增 1 个参数）的 25 行退火循环共 **5 份**：

1. `deposon_diffusion.py:290 reverse_denoise`（原版）
2. `run_v19_meanfield.py:31 reverse_denoise_init`（+init_mode 双起点）
3. `deposon_fast.py:32 reverse_denoise_fast`（+收敛早停）
4. `run_v20_gt5.py:79 reverse_denoise_traj`（+轨迹记录）
5. `run_v20_gt7.py:66 reverse_denoise_traj_alpha`（+Dirichlet 浓度 α）

配套私有成员跨模块 import：`_walk_sums`、`_masked_row_stats`、`_project_masked`、`_G_AETHER`、`_EPS` 被 deposon_fast、run_v19_meanfield、run_v20_gt5/gt6/gt7 共 5 个文件 import——私有接口已事实公开，deposon_diffusion 内部重构会静默波及 5 处。

### C. LLM fetch 管道复制

- `requests.post` 重试/缓存/落盘循环出现在 **9 个文件**：llm_prior.py:112 + run_v20_bigquiz_fetch / cot_fetch / crossval_fetch / familyL_fetch / gt3_fetch / gt3b_fetch / gt3c_fetch / gt8b_fetch（8 个 fetch 脚本合计 ≈1636 行，另有 run_v18_api_supplements 内嵌一份）。
- `def sha(...)`（一行 sha256）复制 **7 份**。
- `run_v20_gt3b_fetch.py` 与 `run_v20_gt3c_fetch.py`：各 85 行，diff 仅 30 行（≈65% 逐字节相同，只差 endpoint/key 环境变量）。
- 复制根因：`llm_prior.py` 把 `ENDPOINT`/`MODEL`/`TIMEOUT` 写成模块常量，`call_llm_prior` 不可参数化，换模型/换厂商只能整文件 fork。
- `_extract_json*` 解析器 **5 份独立实现**：deposon_agents_v1_3:616、deposon_agents_v1_4:713、llm_prior:56、mindmap_corpus_v20:434、run_v18_api_supplements:187。
- llm_prior 私有成员 `_extract_json_array`、`_validate_prior`、`_sanitize` 被 8 个脚本 import；mindmap_corpus 私有成员 `_assign_labels`、`_canonical_sha256`、`_PROMPT_TEMPLATE` 被 run_v20_gt8 / gt8b_fetch import。

### D. 其他复制与并行实现

- `deposon_agents_v1_3.py`（1772 行）vs `deposon_agents_v1_4.py`（1875 行）：同名类层级（DeposonState/EtherChannel/VectorizedDeposonScatter/PersistentCache/LLMBackend/KimiLLMBackend/ConceptDecomposer/DeposonField/DeposonAgentSystem/BenchmarkEvaluator/HundredQuestionBenchmark/TrapBenchmark 全部同名双份），全文 diff ≈400 行。v1_3 仍被 run_benchmark_v1_3、run_g2_ensemble、tests/test_new_modes 使用——两套都不能删。
- `HERE = os.path.dirname(...)` + RESULTS 目录样板：**36/36 个 run_* 脚本**每个一份。
- benchmark harness 并行 4 份：run_benchmark_v1_3 / v1_4_gsm8k / v1_4_strategyqa / run_g2_ensemble。
- `verifier/v1..v22/check.py`：22 份 per-version 校验脚本，md5 全不同（非复制），但无共享校验框架。
- GT 实验族链式 import：run_v20_gt5b ← run_v20_gt5（ENERGY_MODE/GT5_TOL/monotone_rate/phi_trajectory），run_v20_gt7 ← run_v20_gt5（常数表 + 函数 6 项），run_v20_gt8b_eval ← gt8b_fetch + gt8b_ingest。改 gt5 的常数会静默改 gt5b/gt7 的行为口径。

### E. 测试缺口

15 个测试文件、约 2650 行。**无测试覆盖**：run_v16_llm_prior、run_v17_fixed_sampler、run_v17_fusion_fix、run_v17_multigraph、run_v18_api_supplements、run_v20_baselines、run_v20_bigquiz_eval、run_v20_quizbank、run_v20_gt3_eval、run_v20_crossval_eval、run_v20_photonics、run_v20_vector_audit、run_v20_fastcheck，以及整个 `deposon_photonics.py`（232 行硬件模型，0 测试）。deposon_g2_modes 仅经 test_new_modes 间接触及。讽刺的是被 18 个脚本依赖的 `row_normalize` 没有针对它自身的边界测试——它的"测试"分散在各 eval 脚本的结果断言里。

---

## 编号深化候选清单

### 候选 1：退火核心统一（5 份复制循环 → deposon_diffusion 深模块）
- **聚类**：deposon_diffusion.reverse_denoise、run_v19_meanfield.reverse_denoise_init/field_scores_init、deposon_fast.reverse_denoise_fast/field_scores_fast、run_v20_gt5.reverse_denoise_traj、run_v20_gt7.reverse_denoise_traj_alpha。
- **耦合原因**：同一更新规则 + 同一组私有 helper（_walk_sums/_masked_row_stats/_project_masked）；每个调用方要的只是多一个旋钮（init_mode / early_stop / record_traj / alpha），但惯例是"旧文件一行不动"→ 整段复制。
- **依赖类别**：1 进程内（纯 numpy 计算，无 I/O）——始终可以深化。
- **测试影响**：tests/test_fast.py（早停等价性）、test_v19.py、test_v20_gt5/gt5b/gt7（轨迹/α 回归断言）从"断言 4 个私有实现彼此等价"收敛为对单一公开接口的边界测试；原有等价性测试可删除（替代而非叠加）。
- **深化草图**：`denoise(WT, mask, cfg, source, target, *, init="dirichlet"|"prior_mean", alpha=None, early_stop=None, record=False) -> DenoiseResult(W_final, steps, states?)`，私有 helper 收回模块内部，5 个调用方各删 25–50 行。

### 候选 2：实验协议库（run-as-library 反模式 → deposon_protocol 模块）
- **聚类**：run_v15(row_normalize/arm_scores/mean_std/reconstruct_mindmap)、run_v16(prior_score_matrix/hybrid_scores)、run_v17(minmax_mask/norm_hybrid/raw_hybrid/prior_only/mcnemar)、run_v19_meanfield(field_scores_init/is_placeholder)、run_v19_fullrank(full_candidate_mask/gold_rank/rank_metrics)、run_v19_quickwins(sign_test)。
- **耦合原因**：这些是 v15–v20 全部实验共享的"评估协议"，但定义在带 main() 和模块级实验常量的脚本里；import 协议即 import 实验。GT 族链式 import（gt5b/gt7←gt5）是同病第二层。
- **依赖类别**：1 进程内。
- **测试影响**：为 row_normalize / full_candidate_mask / gold_rank / 融合函数 / 统计检验建边界测试（目前 0 个直接测试）；tests/test_v19*.py、test_v20*.py 中对协议行为的间接断言可收敛到协议边界。
- **深化草图**：`deposon/protocol.py`（掩码/归一化/排名指标）+ `deposon/fusion.py`（先验融合与显著性检验）；run_* 脚本只留参数扫描与打印。

### 候选 3：LLM 先验获取管道（9 份 fetch 复制 → 单一 fetcher + 注入配置）
- **聚类**：llm_prior.call_llm_prior + 8 个 run_v20_*_fetch.py + run_v18 内嵌份；_extract_json_array/_validate_prior/_sanitize 私有外泄。
- **耦合原因**：端点/模型/key 环境变量全部硬编码为模块常量，缓存布局（sha 校验、prompt_sha256 匹配、attempts 落盘）逻辑相同却只有复制版。
- **依赖类别**：4 真正的外部依赖（LLM API）——边界 Mock `requests` 或注入 transport callable；缓存目录属 2 本地可替代（tmp 目录）。
- **测试影响**：目前 9 份 fetch 全部无测试（网络依赖没法测）。深化后：内存 transport + tmp 缓存目录下测重试预算、prompt_mismatch 短路、缓存新鲜度判断——这些是真实 bug 藏身地（gt3b/gt3c 的 TIMEOUT 修正即为一例）。
- **深化草图**：`fetch_prior(spec: EndpointSpec, prompts, cache_dir, transport=requests.post) -> FetchReport`，9 个脚本各退化为 3–5 行 spec 定义；`_extract_json_array` 转正为公开 `parse_json_array`。

### 候选 4：agents v1_3 / v1_4 合并（同名双层级 → 单模块 + 版本配置）
- **聚类**：deposon_agents_v1_3.py（1772 行）与 deposon_agents_v1_4.py（1875 行）的全部同名类；调用方 run_benchmark_v1_3 / v1_4_* / run_g2_ensemble / run_v19_benchmark_fixes。
- **耦合原因**：v1_4 是 v1_3 的 fork（diff ≈400 行/3600 行），两版都活着且都被 import；修一个共享 bug 要改两处，理解任一概念要同时读两份。
- **依赖类别**：主体 1 进程内；KimiLLMBackend 为 4（外部 LLM，Mock 边界，已有 LLMBackend 抽象可复用为端口）。
- **测试影响**：test_new_modes.py 同时 import 两版；合并后以 DeposonAgentSystem 公开接口为边界，行为差异由 `version="1.3"|"1.4"` 配置锁定，旧的双份浅测试删除。
- **深化草图**：单 `deposon_agents.py`，`DeposonAgentSystem(llm_backend, mode, version=...)`；版本差异收敛为 1–2 个策略类。

### 候选 5：v20 GT 实验族共享底座（链式 import → gt_common）
- **聚类**：run_v20_gt, gt2b, gt3_eval, gt5, gt5b, gt6, gt7, gt8, gt8b_fetch/ingest/eval（11 个脚本）；被当库 import 的常数表（GT5_TOL/GT5_GRAPHS/GT7_ALPHAS/GT8_PAIRS/GT8B_DOMAINS…）与 verdict/monotone_rate/phi_trajectory。
- **耦合原因**：每个 GT 是上一个 GT 的参数化变体，惯例"不改旧文件"导致直接 import 旧脚本的常数与函数——gt5 的常数变更会静默改 gt5b/gt7 口径，回归测试（test_v20_gt5b/gt7）锁定的其实是跨文件耦合本身。
- **依赖类别**：1 进程内（gt8b_fetch 的 LLM 部分随候选 3 走）。
- **测试影响**：现有 8 个 test_v20_gt* 文件从"锁定跨脚本 import 的常数"改为对 gt_common 边界的断言；测试数量可减半。
- **深化草图**：`gt_common.py` 暴露 `GTRun(spec) -> verdict dict`；每个 GT 脚本退化为 spec + main。

### 候选 6：deposon_photonics 孤岛（232 行，0 测试，唯一调用方是薄脚本 run_v20_photonics）
- **聚类**：deposon_photonics（网表编译/损耗/退火斜坡）+ run_v20_photonics（140 行薄驱动）。
- **耦合原因**：硬件模型与扩散核心概念上同属"场→路径评分"家族（hardware_scores 对标 field_scores），但完全独立、无测试、无协议复用。
- **依赖类别**：1 进程内。
- **测试影响**：无旧测试可删；新增边界测试（netlist→loss/transmission 的物理不变量）。
- **深化草图**：要么并入 protocol 家族实现统一的 `scores(adj, source, target, backend="field"|"hardware")`，要么确认其为一次性实验并归档。

### 候选 7：verifier/v1..v22 校验脚本族（22 份无共享框架）
- **聚类**：verifier/vN/check.py ×22（md5 全不同，61 行/份左右）。
- **耦合原因**：每版一个校验脚本，结构相同（读 results JSON、断言阈值），无共享 runner。
- **依赖类别**：2 本地可替代（读本地 results/）。
- **测试影响**：本身即校验；深化价值在于"一个 `verify(version)` 入口 + 声明式阈值表"，新版本不再新增文件。
- **优先级低**：它们不互相 import，摩擦有限。

### 候选 8：deposon_g2_modes 浅模块（140 行薄包装）
- **聚类**：deposon_g2_modes（boltzmann_walk/boltzmann_annealed/path_integral_born/majority_vote，接口≈实现）+ 唯一调用方 run_g2_ensemble。
- **耦合原因**：四个函数都是"nodes/edges dict + field_factory 回调"的薄循环；field_factory 协议未文档化，与 DeposonField 的对应关系只能读 run_g2_ensemble 才能拼出来。
- **依赖类别**：1 进程内（LLM 部分经 agents 走类别 4）。
- **测试影响**：test_new_modes 浅测试可替换为模式边界测试。
- **深化草图**：并入 agents 体系或收敛为单一 `run_mode(mode, graph, field)` 入口。

---

## Top-5 深化候选（按收益×风险排序）

1. **候选 1 退火核心统一** — 消除 5 份逐行复制 + 5 处私有 import；纯进程内，现有等价性测试可直接转边界测试，风险最低收益最直接。
2. **候选 2 实验协议库** — 解除 18 脚本对 run_* 的 run-as-library 依赖网，给被 18 个脚本依赖却无直接测试的协议函数一个家。
3. **候选 3 LLM fetch 管道** — 消除 9 份复制（≈1600 行），首次让重试/缓存逻辑可测（Mock transport）。
4. **候选 4 agents v1_3/v1_4 合并** — 消除 3600 行同名双层级；工作量最大，建议候选 1–3 落地后做。
5. **候选 5 GT 族共享底座** — 切断 gt5→gt5b→gt7 常数链式耦合，防止口径静默漂移。
