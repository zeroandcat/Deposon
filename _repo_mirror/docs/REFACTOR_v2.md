# REFACTOR v2 — 候选 1（退火核心统一）+ 候选 2（实验协议库）实施记录

日期：2026-08-29。依据 docs/ARCH_AUDIT_v2.md 候选 1 / 候选 2。行为保持性重构：
所有数值结果、随机种子语义、JSON 输出结构逐位不变（证据见 §4）。
未动 GT 族常数链（候选 5）、fetch 管道（候选 3）、agents v1_3/v1_4（候选 4）。

## 1. 改动清单

### 候选 1：退火核心统一（5 份逐行复制循环 → 单入口）

| 文件 | 行级摘要 |
|---|---|
| `deposon_diffusion.py` | 新增公开入口 `denoise(WT, mask, cfg, source, target, *, init_mode="dirichlet", alpha=None, early_stop=None, record=False) -> (W_final, steps_taken, states)`（约 reverse_denoise 之后），为唯一一份退火循环体；`reverse_denoise` 改为薄转发（`denoise(...)` 取 `W_final`）。旋钮语义：`init_mode`（dirichlet/prior_mean 起点）、`alpha`（Dirichlet 浓度，None⇒ones，与旧 dirichlet 逐位一致）、`early_stop=(rel_tol, min_steps)`、`record`（记录 n_steps+1 个状态）。n_steps≤0 恒等返回语义与各旧副本一致。 |
| `run_v19_meanfield.py` | `reverse_denoise_init` 25 行循环体删除 → 薄转发 `denoise(..., init_mode=init_mode)`；私有成员 import（`_masked_row_stats/_project_masked/_walk_sums/_G_AETHER/_EPS`）移除，改 import `denoise`。`INIT_MODES` 等常量原样保留。 |
| `deposon_fast.py` | `reverse_denoise_fast` 循环体删除 → 薄转发 `denoise(..., early_stop=(rel_tol, min_steps))`，仍返回 `(W, steps_taken)`；私有成员 import 移除。`FAST_TOL/EARLY_STOP_REL/MIN_STEPS` 不变。 |
| `run_v20_gt5.py` | `reverse_denoise_traj` 循环体删除 → 薄转发 `denoise(..., record=True)`，仍返回 states 列表；私有成员 import 移除。`phi_potential/monotone_rate/gt5_verdict` 及全部 GT5_* 冻结常量一行未动。 |
| `run_v20_gt7.py` | `reverse_denoise_traj_alpha` 循环体删除 → 薄转发（`alpha=None`⇒`init_mode="prior_mean"`，否则 `dirichlet`+`alpha`，`record=True`）；alpha≤0 的 ValueError 消息原文保留。私有成员 import 移除。 |

注：`run_v20_gt6.py` 仍 import 私有 helper 计算场梯度分量 F_e（不是退火循环复制，不在候选 1 范围），未动。

### 候选 2：实验协议库

| 文件 | 行级摘要 |
|---|---|
| `deposon_protocol.py`（新增） | 集中定义 `row_normalize`、`prior_score_matrix`、`full_candidate_mask`、`gold_rank`、`field_scores_init`（逐字搬运原实现，仅 `field_scores_init` 内部改调 `denoise`）。零 I/O、无模块级实验常量、无 main()，仅依赖 numpy 与 deposon_diffusion —— import 协议不再拖入宿主脚本的模块级副作用。 |
| `run_v15_experiment.py` | `row_normalize` 定义 → `from deposon_protocol import row_normalize`（原行位薄转发）。 |
| `run_v16_llm_prior.py` | `prior_score_matrix` 定义 → 薄转发。 |
| `run_v19_fullrank.py` | `full_candidate_mask`、`gold_rank` 定义 → 薄转发。 |
| `run_v19_meanfield.py` | `field_scores_init` 定义 → 薄转发。 |
| `tests/test_protocol.py`（新增，19 个测试） | row_normalize 边界（零行/空阵/负值/NaN 行/非方阵/转发同一性）；prior_score_matrix 越界键、full_candidate_mask 自列排除、gold_rank mergesort 稳定平局；denoise 统一入口等价性（双臂逐位等于旧包装、alpha=1.0⇔dirichlet 轨迹逐点相等、record 末态=终态、早停禁用⇔完整步数逐位相等、n_steps=0 恒等、非法旋钮 ValueError）。 |

## 2. 设计决策

- **单入口签名**：`denoise` 返回三元组 `(W_final, steps_taken, states)`，5 个历史入口各保留原名与签名做薄转发，18+ 个调用点（含 tests）零改动。
- **逐位等价的实现要点**：(i) `alpha=None` 时浓度取 `np.ones(m)`，与旧代码逐字节相同的数组 ⇒ `Generator.dirichlet` 输出逐位相同；(ii) rng 调用次序、投影/收缩顺序、`n_steps<=0` 提前返回（不投影）均按旧副本保留；(iii) 旧复制版忽略 `cfg.energy_mode` 恒用 aggregate 梯度——统一入口恢复 `energy_mode` 分支（含 max_path 臂）；所有现存调用点 cfg 均为 aggregate，行为不变（max_path 仅原 `reverse_denoise` 路径使用，由 test_diffusion 锁定）。
- **薄转发而非别名删除**：保持 `from run_v15_experiment import row_normalize` 等 18/14/11/11/8 条既有 import 路径全部可用（测试中断言转发对象与新定义 `is` 同一）。
- **不引入 deposon/ 包目录**：仓库为扁平模块布局，新建单模块 `deposon_protocol.py` 为最小完整变更。

## 3. 验证证据

1. **pytest**：`python3 -m pytest tests/ -q` → **274 passed**（基线 255 + 新增 19），全绿。
2. **逐位等价性**：冻结种子小样本前后对比脚本（48 个哈希：3 组图/种子配置 × {reverse_denoise, init×2 模式, fast×2, traj×2, alpha×4, field_scores_init×2, mask, gold_rank} + row_normalize/prior_score_matrix/max_path 臂），sha256 over `.tobytes()`；重构前后 **48/48 完全一致**。
3. **复制消除 grep**：退火循环体标记 `for _t in range(cfg.n_steps, 0, -1)` 全仓仅 `deposon_diffusion.py:1` 份；`rng.dirichlet` 实际调用仅 deposon_diffusion 1 份（run_v20_gt7.py:11 为模块注释引用）；`def row_normalize` 仅 `deposon_protocol.py:23` 一处（原位置为 import 转发，不算定义）；其余 4 个协议函数 `def` 同样仅存于 deposon_protocol。
4. **密钥串 grep**：全部 10 个改动/新增文件 `sk-*`/`api_key=`/`Bearer` 模式计数 = 0。
5. **import sweep**：全部顶层模块可 import（唯一例外 `run_benchmark_v1_4_strategyqa` 因 `resolve_high_couple_config` 不存在于 deposon_agents_v1_4 而失败——**重构前即存在**，本次未触碰该两文件）。

## 4. 未做项（留给后续候选）

- **候选 3**（LLM fetch 管道 9 份复制 → 单一 fetcher + 注入 EndpointSpec/transport）：未动。
- **候选 4**（agents v1_3/v1_4 同名双层级合并）：未动。
- **候选 5**（GT 族链式 import 常数链 gt5b/gt7←gt5）：未动；本次仅替换 gt5/gt7 内的循环体，全部 GT5_*/GT7_* 冻结常量与跨文件 import 关系原样。
- 融合函数（run_v17 的 norm_hybrid/raw_hybrid/prior_only/mcnemar、run_v19_quickwins 的 sign_test 等）仍留在原脚本——扇入较小（≤4），未纳入本次最小变更，可并入后续协议库扩展。

---

# 候选④: agents v1_3/v1_4 合并（2026-08-30 追加）

依据 docs/ARCH_AUDIT_v2.md 候选 4。行为保持性重构: 同名双层级 →
单模块 `deposon_agents.py` + version 配置; 两个旧文件退化为钉定版本的薄转发。
全部既有 import 路径、默认数值行为、缓存键布局逐位不变（证据见 §C.3）。

## C.1 改动清单

| 文件 | 行级摘要 |
|---|---|
| `deposon_agents.py`（新增，约 2150 行） | 两版全部同名类/函数的唯一实现。新增 `AgentConfig(version="1.3"\|"1.4")`（非法版本 ValueError）与 `_resolve_version`（接受 str/AgentConfig/None）。版本分异全部收敛为实例/类属性 `version` 上的分支：KimiLLMBackend（PROMPT_VERSION 1.3.1/1.3.2、DECOMPOSE_PROMPT 两版原文、max_tokens 默认 4000/8000、LEGACY_PROMPT_VERSIONS、英文 mini/steps 分解链、配额 403/空 content 快速失败、timeout 下限 200s、decompose 缓存键 kind 与规则降级短路、cot_solve）；DeposonField（运算节点 g_c/g_a 0.3/0.2 vs 0.15/0.05、high_couple x3 vs E9.3 真修复、resonant/labelfree/arrhenius 仅 1.3 激活、process_path 的 delta/barrier_loss 记录键）；DeposonAgentSystem（内部字段随 version、ablation high_couple 入口）；BenchmarkEvaluator（折叠去重、computed_answer 兜底）。 |
| `deposon_agents_v1_3.py`（薄转发） | 同名共享对象 `from deposon_agents import ...` 直接转发（`is` 同一）；4 个版本分异类为单行钉定子类 `class X(deposon_agents.X): version = "1.3"`（KimiLLMBackend 另钉 PROMPT_VERSION/DECOMPOSE_PROMPT/LEGACY_PROMPT_VERSIONS 类属性，覆盖 `__new__` 旁路场景）。不定义任何方法。 |
| `deposon_agents_v1_4.py`（薄转发） | 同上，钉定 `version = "1.4"`；另转发 `HIGH_COUPLE_GAIN`/`resolve_high_couple_config`（原 v1_4 独有）。 |
| `run_benchmark_v1_4_strategyqa.py` | **顺带修复重构前缺口**：原 `sys.path.insert(0, "/mnt/agents/output")` 命中仓库外旧副本（无 `resolve_high_couple_config`）→ ImportError。改为仓库目录优先（与 run_benchmark_v1_3/gsm8k 同型），仓库内 v1_4 shim 转发该函数，脚本恢复可导入，high_couple 语义与 gsm8k runner 一致。OUT 仅为数据/结果目录，语义不变。 |
| `tests/test_agents_merge.py`（新增，52 个测试） | 转发同一性（共享名 `is` 同一、钉定类零新方法、方法级 `getattr_static` 同一、无双层级）；version 钉定公开行为（prompt/token 默认、缓存键逐位一致、绑定常数、high_couple 两版语义、process_path 记录键、v1.3 专属模式在 1.4 场 fallthrough 逐位一致、ablation 入口、E9.3 开关、evaluator 折叠去重两版）；冻结等价性（见 §C.3）；import sweep（5 个调用方模块 + strategyqa 缺口修复断言）。 |

## C.2 设计决策

- **钉定机制**：单类对象无法携带两个默认 version，故版本分异类在 shim 中以单行类属性子类钉定；全部方法为继承的同一实现（测试中 `getattr_static` 逐方法断言同一性）。共享类/函数为纯 `from ... import ...`，`is` 同一性成立。这是"旧 import 路径默认行为逐位不变"与"单实现"的唯一兼顾解；两个旧文件不再是实现副本。
- **version 解析优先级**：显式形参 > 类属性（shim 钉定） >（BenchmarkEvaluator）agent.version > "1.4"。核心模块默认 "1.4"（= 最新线），旧行为只能经 shim 或显式 `version="1.3"` 获得。
- **逐位等价要点**：v1.3 的 decompose 路径整体保留为 `_decompose_v13` 分派；`_chat` 的 403/空 content/timeout 三分支仅在 version≠"1.3" 时启用；process_path 的 v1.3 专属记录键按 version 条件构造（含键序）；v1.3 专属模式分支由 version 门控，v1.4 场对这些 mode 保持原 fallthrough（与 unified 逐位一致，有测试锁定）。
- **已知附加面（非行为变化，如实披露）**：合并后 v1.3 路径的 KimiLLMBackend 新增 `cot_solve`/`_convert_simple_spec` 方法与 `_quota_exhausted=False` 实例属性（原 v1_3 无）；均为纯附加，不改变任何既有调用路径的输出（冻结哈希覆盖证明）。

## C.3 验证证据

1. **pytest**：`python3 -m pytest tests/ -q` → **351 passed**（候选1/2 基线 274 + 本候选 52 + 并行的候选3代理新增 25），全绿。
2. **逐位等价性**：冻结种子 harness（10 类任务：后端属性、规则降级分解、mock _chat 分解轨迹（中英×DECOMPOSE_FORCE_STEPS）、legacy 缓存复用、9 模式场物理、4 模式端到端 evaluate_math、ablation（含 E9.3 alias 开关）、evaluator 边界、stub transport 的 403/空content/正常三场景、cot_solve），sha256 over 规范化 JSON。合并前原始两模块 vs 合并后两 shim：**v1.4 全部 13 项逐位一致；v1.3 行为项全部逐位一致**（仅 §C.2 披露的附加面使 3 项探测字段不同）。19 个全量哈希已固化为 tests/test_agents_merge.py 的 TestFrozenEquivalence 常数（合并前原始模块生成），CI 持续锁定。
3. **import sweep**：54 个顶层模块全过；5 个 agents 调用方模块 + 两 shim + 核心模块逐一断言；strategyqa 修复后独立进程导入通过。
4. **复制消除 grep**：`class KimiLLMBackend`/`class DeposonField`/`class DeposonAgentSystem`/`class BenchmarkEvaluator` 的实现定义仅 `deposon_agents.py` 各 1 份（shim 为无方法钉定子类）；`DECOMPOSE_PROMPT` 等版本常量按版本各 1 份。
5. **密钥 grep**：全部改动/新增文件 `sk-*`/`api_key='...'`/`Bearer <token>` 实密钥计数 = 0（tests 中 `api_key='probe-key'` 为 stub transport 占位符，非密钥）。

## C.4 未做项 / 残留

- 仓库外 `/mnt/agents/output/deposon_agents_v1_3.py` 等旧副本不属本仓库，未触碰；strategyqa 修复后即不再被该脚本引用。
- v1.3 shim 未导出 `resolve_high_couple_config`/`HIGH_COUPLE_GAIN`（忠实于原 v1_3 表面）；如需 1.3 语境引用请用 deposon_agents。
- 候选 3（fetch 管道）由另一代理并行处理；候选 5–8 未动。

---

# 候选③⑤（2026-08-30 冲刺波）实施记录

依据 docs/ARCH_AUDIT_v2.md 候选 3（LLM fetch 管道统一）与候选 5（GT 族共享
底座）。行为保持性重构：缓存文件名、prompt_sha256 落盘格式、预算计数语义、
各 GT 冻结种子输出逐位不变（证据见 §B.3）。红线遵守：所有 fetch 路径的
key 仍只从环境变量读取、经 `_sanitize`/`sanitize_secret` 兜底；无 git 操作；
paper/ 与既有 docs 未动（本节为追加）。

## B.1 改动清单

### 候选 3：LLM fetch 管道统一（9 份复制 → llm_fetch 单入口）

| 文件 | 行级摘要 |
|---|---|
| `llm_fetch.py`（新增，≈190 行） | 唯一实现：`sha`（原 7 份 `def sha` 收敛）、`sanitize_secret`（原 `llm_prior._sanitize` 逐字搬运）、`parse_json_array`（原 `llm_prior._extract_json_array` 逐字搬运转正）、`EndpointSpec`（endpoint/model/timeout/max_tokens/max_attempts + 三个历史差异旋钮：`err_text_chars` HTTP 回显截断 200/150、`err_msg_chars` 异常截断 None/120（gt3b/gt3c 加固）、`backoff_base` 退避 None/3、`empty_err` 空 content 口径）、`post_once`（单次尝试，供重试作用域含解析/校验的调用方复用）、`fetch_text`（**唯一一份 fetch 重试主循环**，返回 `FetchOutcome(content, last_err, attempts)`，不抛异常）、`is_fresh(path, sha, model=None, strict=True)`（缓存新鲜度；strict=False 保留旧 gt3/familyL/cot 的"损坏即崩溃"口径）、`save_record`（ensure_ascii=False, indent=1 统一落盘）。transport 依赖注入（默认调用时解析 `requests.post`，旧 monkeypatch 路径不破）。 |
| `llm_prior.py` | `_extract_json_array`/`_sanitize` → 薄别名（5+9 处既有 import 不破）；`call_llm_prior` 的 HTTP 机制改走 `post_once(_FETCH_SPEC)`（max_tokens=4000 钉定），重试循环保留——其重试作用域**含解析/校验/落盘**（与 fetch 脚本语义不同，见 §B.2）；新增 `transport=None` 参数；`import requests` 保留（旧测试经 `llm_prior.requests` 打桩）。record 字段与 key 序逐字不变。 |
| `run_v20_gt3_fetch.py` | 98→≈80 行。`def sha`、内联重试循环、内联新鲜度判断删除 → `GT3_SPEC.for_model(model)` + `fetch_text` + `is_fresh(strict=False, model=model)`；缓存文件名 `{model}__{domain}.json`、prompt_mismatch 记录、attempts/total 计数、print 文本逐字不变。 |
| `run_v20_gt3b_fetch.py` / `run_v20_gt3c_fetch.py` | 各 85→≈75 行。差异收敛为 `GT3B_SPEC`/`GT3C_SPEC` 各一处（endpoint/model/timeout=240/max_tokens 8000 vs 16000/`err_msg_chars=120` 加固）；ARK_ENDPOINT/ARK_MODEL/ARK_TIMEOUT 常量原样钉定在本文件。 |
| `run_v20_familyL_fetch.py` | 失败不落盘仅打印 FAILED 的旧口径保留；manifest sha 与新鲜度语义不变。 |
| `run_v20_cot_fetch.py` | `COT_SPEC`（max_tokens=2000, err_text_chars=150）。**唯一行为变化**：旧 `post()` 在"全部尝试空 content 且无异常"路径引用未赋值 `last` 崩 UnboundLocalError；统一循环后该路径抛 `RuntimeError("failed: None")`（仅崩溃类型变化，正常/重试路径逐位不变）。 |
| `run_v20_crossval_fetch.py` | `post`/`fresh` 薄转发；`API failed after {MAX_ATTEMPTS} attempts` 报错文本逐字不变。 |
| `run_v20_bigquiz_fetch.py` | `BIGQUIZ_SPEC` 钉定退避（`backoff_base=3` ⇒ sleep(3·2^i)，含末次尝试）与 `empty_err` 口径；`save()` 的 key 序（prompt_sha256/model 追加于 rec 末尾）逐位保留。 |
| `run_v20_gt8b_fetch.py` | **进程结束后才做的最小兼容修改**：实施前确认 `run_v20_gt8b_fetch.py` 进程已退出（ps 无、无锁文件、gt8b_cache 两阶段缓存已齐），随后仅将 `sha`/`fresh`/`post` 收敛为 llm_fetch 薄转发（`GT8B_SPEC`：max_tokens=8000）；公开名（CACHE_DIR/GT8B_DOMAINS/build_gt8b_prompts/gt8b_prompt_manifest/load_labels_from_graph_cache/main）与落盘/打印/fetch_failed 语义不变。results/gt8b_cache 全程未被本波读写（等价性对照在 /tmp 副本中进行）。 |
| `tests/test_llm_fetch.py`（新增，20 个测试） | 假 transport 注入：重试预算/超时透传/HTTP 错误 sanitize（含 key 回显剔除与 err_text_chars 截断）/err_msg_chars=120 加固/空 content 两种口径/退避序列 [3,6]/预算计数/缓存命中跳过（缺失·损坏 strict×2·模型不符·prompt 漂移·空响应）/save_record 落盘格式/call_llm_prior 注入 transport（含解析失败计重试预算）/8 个脚本 spec 钉定断言。 |

未动：`run_v18_api_supplements.py` 内嵌 fetch 份（E1–E4 多评估者落盘结构不同，
不在"llm_prior + 8 个 *_fetch.py"范围内）、`deposon_agents*.py` 的 `_extract_json`
（候选 4 域）、`mindmap_corpus_v20._extract_json_object`（返回 str 的对象切片，
语义不同）。

### 候选 5：GT 族共享底座 gt_common（切断 gt5→gt5b/gt7 静默传导）

| 文件 | 行级摘要 |
|---|---|
| `gt_common.py`（新增，≈90 行） | 共享函数逐字搬运自 run_v20_gt5：`phi_potential`、`reverse_denoise_traj`、`phi_trajectory`、`monotone_rate`、`graph_tasks`（原 `_graph_tasks`）；共享锚点 `GT_ENERGY_MODE="aggregate"`、`GT_MONO_TOL=1e-9`。零 I/O、无 main()。 |
| `run_v20_gt5.py` | 5 个函数定义 → gt_common 薄转发，**默认参数仍绑定本文件冻结常量**（`tol=GT5_TOL`、`energy_mode=ENERGY_MODE`）；`_graph_tasks` 别名保留；全部 GT5_* 常量、gt5_verdict、run_graph、main 一行未动；既有 import 路径（`from run_v20_gt5 import ...`，含 tests）全部不破。 |
| `run_v20_gt5b.py` | `from run_v20_gt5 import (ENERGY_MODE, GT5_TOL, ...)` **删除** → 函数改自 gt_common；新增本文件冻结副本 `GT5B_TOL=1e-9`、`GT5B_ENERGY_MODE="aggregate"` 并在全部调用点显式传参（verdict thresholds/preregistered 的 `"tol"` JSON 值不变）。 |
| `run_v20_gt7.py` | `from run_v20_gt5 import ...` **删除** → 函数改自 gt_common；新增冻结副本 `GT7_GRAPHS`/`GT7_SAMPLE_SEED=505_000`/`GT7_ENERGY_MODE`（与 GT-5 的图集/抽样种子对齐是协议要求，值不变）。 |
| `tests/test_gt_common.py`（新增，5 个测试） | 解耦断言（gt5b/gt7 不再暴露 gt5 常数名）+ 对齐显式锁定（GT5B_TOL==GT5_TOL、GT7_GRAPHS==GT5_GRAPHS、GT7_SAMPLE_SEED==GT5_SAMPLE_SEED 等——任一边改动即测试变红，替代原来的静默传导）+ monotone_rate/graph_tasks/phi_trajectory 边界 + gt5 薄转发默认绑定断言。 |

## B.2 设计决策

- **fetch 主循环只有一份**：`llm_fetch.fetch_text` 覆盖全部 8 个 fetch 脚本
  （含 gt8b）。`llm_prior.call_llm_prior` 保留自己的重试循环，因为其重试
  作用域包含 JSON 解析/校验/落盘（解析失败消耗重试预算，旧语义，已被
  test_llm_prior 与新旧对照锁定）；HTTP 单次机制经 `post_once` 单源。
- **差异全部参数化钉定**：gt3b/gt3c 的 `str(e)[:120]` 加固、bigquiz 的
  指数退避与 empty_err、cot/bigquiz 的 text[:150] 截断，分别收敛为
  EndpointSpec 的 `err_msg_chars`/`backoff_base`/`empty_err`/`err_text_chars`，
  逐脚本显式钉定（tests/test_llm_fetch.py::test_fetch_script_specs_pinned 锁定）。
- **gt_common 不复制常数表**：口径常数各脚本自持冻结副本（gt5 原样、
  gt5b/gt7 新增 GT5B_*/GT7_* 副本），共享的只有函数实现；跨脚本对齐从
  "import 旧脚本常数"改为"各自钉定 + 测试显式断言相等"，改任何一边都会
  变红而非静默漂移。
- **薄转发纪律延续①②**：`from llm_prior import _extract_json_array/_sanitize`、
  `from run_v20_gt5 import monotone_rate/...` 等全部既有 import 路径零改动。

## B.3 验证证据

1. **pytest**：`pytest tests/ -q` → **351 passed**（本波新增 25：test_llm_fetch
   20 + test_gt_common 5；其余增量为同冲刺波其他候选所加），全绿，无回退。
2. **GT 族逐位等价**（冻结种子哈希对照）：同一脚本在旧代码树（重构前快照）
   与新代码树各跑一遍——gt5.run_graph(n_tasks=3, n_seeds=3)/gt5_verdict/
   monotone_rate/phi_potential/phi_trajectory/GT5_* 常量组、gt5b.run_graph/
   gt5b_verdict/GT5B_*、gt7.run_graph(n_tasks=2, n_seeds=2, 6 温度档)/gt7_verdict/
   frontier_shape/GT7_* 共 12 组 sha256 指纹，**除新增的钉定常量条目
   （旧树为 ABSENT）外全部一致**；旧树 import 值 vs 新树钉定值逐一相等
   （1e-9/"aggregate"/图集/505_000）。
3. **fetch 管道逐位等价**（stub 传输层新旧树全 main 对照）：7 个脚本
   （bigquiz/familyL/crossval/gt3/gt3b/gt3c/cot）在 stub `requests.post` 下
   完整跑 main()，**stdout 逐字相同、生成的全部缓存目录树逐字节相同**
   （diff -r 通过，覆盖 familyL_cache/familyL_prior_cache/gt2_attacker_cache/
   gt3_prior_cache 24 文件/cot_quiz_cache/attacker_xl_cache）；llm_prior
   成功/HTTP 401 sanitize/解析失败重试三路径指纹一致；gt8b_fetch 用合法
   DAG+先验 stub 跑全两阶段，stdout 与 gt8b_cache 树（/tmp 副本）逐字节相同。
4. **复制消除 grep**：`def sha(` 全仓 1 份（llm_fetch.py:40）；fetch 重试主循环
   1 份（llm_fetch.fetch_text；llm_prior 为校验耦合变体，run_v18 内嵌份不在
   本次范围）；`_extract_json_array` 唯一实现为 llm_fetch.parse_json_array
   （`def _extract_json` 残余 3 份均在候选 3 范围外：deposon_agents.py 候选 4 域、
   mindmap_corpus_v20 与 run_v18 的对象解析器语义不同）。
5. **密钥 grep**：全部 15 个改动/新增文件 `sk-*`/`api_key=`/`Bearer <token>`/
   硬编码 token 模式计数 = 0；key 仍只从环境变量读取，sanitize 纪律含
   gt3b/gt3c 的 str(e)[:120] 截断加固（经 err_msg_chars 钉定保留）。
6. **import sweep**：全部 54 个顶层模块可 import，0 失败。

## B.4 未做项

- `run_v18_api_supplements.py` 内嵌 fetch 份与 `_extract_json_object`：E1–E4
  逐评估者落盘结构与 fetch 族不同，留待后续随 v18 族整理。
- `mindmap_corpus_v20._extract_json_object`（str 切片）与 run_v18 版（dict）
  语义不同，未强行合并。
- gt8b_fetch 的最小兼容修改在 GT-8b fetch 进程退出后实施；若该实验需复跑，
  新文件行为已经 §B.3.3 新旧对照逐位验证。
