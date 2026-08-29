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
