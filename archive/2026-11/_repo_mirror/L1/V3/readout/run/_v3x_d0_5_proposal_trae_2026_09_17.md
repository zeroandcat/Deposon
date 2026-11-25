# 增补实验设计提案 · Trae code 方

## Deposon V3X D+0.5 · P-L v2 缺口重测 · 提案方：Trae code

**提交时间**：2026-09-17（周四）14:00 CST 前
**主送**：Mavis（deposon V3X 1 周判死主理）
**响应邀请**：`results/_v3x_d0_5_experiment_invitation_2026_09_17.md`
**铁律声明**：本提案为设计提案，不触碰任何 frozen；正文不写任何 key；不增派 LLM。

---

## 0. 一句总结论（先给结论，不预设 PASS）

P-L v2 的 Spearman=1 **不是**"5 制品 backbone 同序单调"造成的，而是 `_p_l_real_data_collapse_runner_2026_09_16_v2.py` L64–66 把**同一个向量的两个单调变换**（`t**nu` vs `t*eta`）做秩相关——对 `nu>0, eta>0, t>0` 两者严格同序，Spearman 恒等于 1 是代数恒等式，与换不换 backbone 无关。

**因此：仅换 backbone 无法破局。** 本提案分两层：① 换统计量（必要）② 加多尺寸数据（充分），后端多样性（§1/§2）只作为第三层锦上添花。以下按邀请函 5 节展开。**另见 §6：本提案并入主线上我注意到的 5 个同类缺口（P-J / P-I / P-M / P-C / P-D）与统一"退化统计量预检"。**

---

## §1 Backbone 选择

**推荐 2 个 backbone（在 1–3 个上限内），1 主 1 对照：**

| 优先级 | Backbone | 通道（铁律2/3/6） | 选它的理由（破同序的内部机制） |
|---|---|---|---|
| 主 | Meta **Llama 3.4**（或 Mistral Large 2） | OpenRouter（非 OpenAI/Anthropic/Google） | 与现存 9 model（全为豆包/GLM/DeepSeek/Kimi/MiniMax 系）tokenizer 边界与 RLHF 奖励模型差异最大，T30/R30/A30 切分预期显著偏移 |
| 对照 | **DeepSeek V4**（全量，非 flash） | 火山方舟 coding-plan | 现有 9 model 里只有 `deepseek-v4-flash`/`deepseek-v4-pro`，flash 与全量 V4 长上下文衰减本征不同，可做"同族内部差异"对照 |
| 备选 | MiniMax M3 | minimax.chat 官方 API | 仅作内部对照（邀请函已声明不作主 backbone） |

**为何这样选**：主 backbone 走 Llama/Mistral 系，其 tokenizer 会改变"路径→token"的边界，RLHF 后训练改变 error-path 反射 vs 透射倾向，从而在**同一批 cells 上产生不同的 T/R/A 排序**——这是 backbone 内部差异，不是换 prompt format（遵守 §2 禁止 pass-through 的约束）。

## §2 同序单调破局方法

### 2.1 根因修正（本提案最诚实、也最重要的一条）

现有 `_p_l_real_data_collapse_runner_2026_09_16_v2.py` 的 R2_grid 逻辑：

```python
transformed      = [t ** nu for t in T_frac60]   # 严格单调增（nu>0）
eta_transformed  = [t * eta for t in T_frac60]   # 严格单调增（eta>0）
corr, _ = spearmanr(transformed, eta_transformed)  # 恒 =1.0
```

`T_frac60` 是 9 model 各自的单值标量（`deposon_v3_physical_opt_60cells_2026_09_11.json` L106–227 的 `P_C_distortion_bound_60cells.per_model`）。对同一个非负向量先 `**nu` 再 `*eta`，两者的秩序**严格相同**，Spearman 恒为 1，与 25 个网格参数无关。故 `p_l_real_data_collapse_results_v2_2026_09_16.json` 全网格 R2=1.0 是统计伪影，**不是** data collapse 拟合。

### 2.2 破局方法（分三层，缺一不可）

- **L1（必要）换统计量**：data collapse 检验的是"不同尺寸的点是否塌缩到同一条主曲线上"，这是**点态重合**问题，不是**秩相关**问题。秩相关（Spearman）在此处的测度对象是"单调性"，而两变换单调性是构造保证的，测它没有信息量。改用**主曲线拟合残差**：对每个 (ν, η) 做尺度变换后，用平滑主曲线（三次样条或幂律）拟合，报 `Q = RMS(y_rescaled - fit) / RMS(y_rescaled)` 归一化塌缩残差。
- **L2（充分）多尺寸数据**：真正的有限尺寸标度需要**同一观测量在 ≥3–4 个尺寸档**下测量。现有 `T_frac60` 只有单尺寸（60 cells）、且是 per-model 标量（9 个点），无法支撑塌缩检验。必须跑 L ∈ {30, 45, 60, 100}（60 档可复用现有 frozen 结果，其余新测）。
- **L3（锦上添花）backbone 内部差异**：在 L1/L2 修好后，若跨 backbone 的观测量仍同序，再靠 §1 的 backbone 内部差异（RLHF 后训练 / attention head 分布 / tokenizer 边界 / 长上下文衰减）产生排序偏移。**注意到此层，换 backbone 才真正有破局作用**。

### 2.3 诚实边界（预先写死，禁止修饰）

若 P-L 没有可调控制参数（例如没有"温度/失真强度"这类参数），严格 FSS 塌缩命题可能本身定义不清；此时只能退化为**单参数幂律有限尺寸标度** `O_L ~ L^{-β/ν}`（log-log 线性拟合的 Pearson R² + 残差），并把"塌缩"措辞如实降级为"幂律标度"。这一判断本提案不下结论，交 Mavis/用户对照 frozen `KT_C1_SPEC_V0.1` 确认。

---

## §3 测法

- **cells**：GSM8K + StrategyQA 子集（沿现有 5 制品 cell 结构），L ∈ {30, 45, 60, 100}，每 backbone × 每 L 独立跑；≥30 cells 满足判死级统计（邀请函要求），预算内最多 60 cells。
- **0 LLM 纯 hashlib 复算层**：沿 `_verify_15frozen.py` 的 resolve + sha256 模式，读 frozen `P_C_distortion_bound_60cells` 公式（`D_fix2 = 1 - cos([T,A],[T_c,A_c])`）重算 T/R/A 与 `T_frac(L)`、`D_fix2_cosine`，不依赖任何 LLM call 确认结果。
- **baseline**：原 5 制品 baseline JSON（KIMI/GLM_1/GLM_2/coze/MiniMax）+ 现有 9 model `T_frac60` 作 frozen 对照；新结果落入 `results/_p_l_*` 独立子目录，**不动 18 frozen + P-G V0/V0.1 + 4 plugin spec**。
- **产物**：每 (backbone, L) 一个 JSON + SHA-12；0 新 frozen 触发条件；不写临时文件（直接落 `results/` 子目录）。

## §4 期望阈值（预注册，禁止 reassign）

| 指标 | 判定 | 含义 |
|---|---|---|
| 塌缩残差 `Q`（主曲线拟合，归一化） | `Q < 0.05` 塌缩成立；`0.05 ≤ Q ≤ 0.15` 边缘态，补一档尺寸；`Q > 0.15` 无塌缩 → **P-L 数据塌缩主张证伪**入 paper §7.2 | 这是 P-L 的真正判死指标 |
| 单参数幂律退路 `R²(log-log)` | `≥0.9` 接受幂律标度；`<0.9` 连幂律都不成立 → P-L 更强证伪 | 仅当无控制参数时启用 |
| 跨 backbone 排序 `Spearman` | `< 0.95` 破同序成立；`[0.95,1)` 部分破单调需补测；`=1.0` 仍同序（**但此时已不影响 P-L 塌缩判死**，只说明 backbone 排序未被打破） | 邀请函原表的 Spearman 阈值仅作为"破局是否成功"的辅助栏 |

**关键修正**：邀请函 §4 原表把 Spearman 作为 data collapse 判死依据。本提案主张：**Spearman 只能判定"backbone 排序是否同序"，不能判定"数据是否塌缩"**；判死塌缩的应该是 `Q`（或幂律退路的 R²）。两者分离后，即使 Spearman 仍=1，也不污染 P-L 塌缩结论。

## §5 风险评估

- **API 风险**：OpenRouter 免费额度限速（铁律3：只调非 OpenAI/Anthropic/Google，避免 layer-2 user_id 门控）；Llama 3.4 / Mistral Large 2 单 cell 延迟大；火山 coding-plan 有并发上限；MiniMax M3 聊天额度受限——方案：30 cells × 1 backbone 先跑主 backbone，跑通再扩。
- **frozen 触动风险**：本实验**不应当再触动任何新 frozen**（邀请函已声明）。新产物只写 `results/_p_l_*`；若需读 frozen 文件，只读并落 SHA-12 before/after 报告（沿 Q2 reconcile 流程）。`conservation.py` V0=`4bdec2683f06` 不动，作 Q2 metadata 保留。
- **时间预算**：1 backbone × 3 尺寸 × 30 cells ≈ 30–60 min 派 worker 可完成（邀请函估），2 backbone ≈ 1.5–2 h wall + verifier 复算，D7 前可闭环。

---

## §6 主线其他未提增补方向（并入本提案，供 Mavis 聚合）

审查 `results/_v3x_*` 与 `results/_p_*` 落盘结果后，我注意到主线上另有 5 处与 P-L 同类/相邻的缺口，且共享同一**根因族**，一并并入。每处按"缺口 → 证据 → 增补实验 → 复用"四段给出。

### 6.0 根因族：退化统计量仍产 PASS/SECURE

P-L 之外，P-J、P-I、P-M、P-C(exp_3_3) 存在同一类 bug：**指标退化到常量/硬编码，判死管线仍产出 PASS 或 SECURE**。建议在 0-LLM hashlib 复算层加一道**退化预检**：判死前断言 ①输入向量方差>0 ②秩不恒同 ③标签非硬编码 ④检测率不低于随机基线；任一失败 → 直接 UNVERIFIED，禁止产 PASS。这是横切修复，五项 Adendum 均受益。

### 6.1 Adendum A — P-J 收敛盆地（convergence_rate 占位）

- 缺口：收敛盆地判"P-J 通过(单调关系)"，但依据是占位常量。
- 证据：`_p_j_convergence_basin_2026_09_16` `convergence_rates` 9 model 全为 `0.1`（常量无方差），却报 `spearman_rho = -0.9667` —— 常量向量上 Spearman 无定义，-0.9667 不可能由全 0.1 产生。closeout §0.1 item14 已标"简化模型 bug"。
- 增补实验：用 GSM8K/StrategyQA 真实收敛曲线测 per-model 收敛率（非抄 0.1），再算 `T_frac60` vs 收敛率的 Spearman（先过方差预检）。
- 复用：与 §1/§3 同一批 backbone×多尺寸 cells，同一 0-LLM 复算层，0 额外 API。

### 6.2 Adendum B — P-I 曲率审计探针（true_labels 占位）

- 缺口：P-I 的 detection AUC 依赖 true_labels，仍无真实标签。
- 证据：`_p_i_curvature_audit_probe` 旧 AUC 最高 0.625；`_p_i_real_labels_2026_09_16` 诚实降级移除 hardcode 后 `d_h_auc`/`d_e_auc` 全 0，判"UNVERIFIED(true_labels 占位, AUC 不可信)"。
- 增补实验：产出真实"审计资产 vs 非资产"二分类标签（用 §3 同一批 cells 的探针输出 + 规则标定），重算 d_h/d_e/v42 fingerprint 三通道 ROC-AUC。
- 阈值：AUC>0.5（超随机）才可判"审计资产"；否则 P-I 判死入 paper §7.2。

### 6.3 Adendum C — P-M 攻击面（detection=0 vs SECURE 矛盾）

- 缺口：攻击面成本下界的"SECURE"判定与 0% 检出率自相矛盾；诚实降级版已判 v42 须重设计。
- 证据：`_p_m_attack_surface_cost` 全 budget `detection_rate = 0.0`（8/8 miss）、`miss_rate = 1.0`，却报 `safety_budget_lower_bound = 80`、`v42_safety_index = "SECURE"`；`_p_m_real_separation` 已更正为 `v42_redesign_required = true`（强制修正案）。
- 增补实验：v42 重设计后重跑 attack-surface cost 曲线；前提声明"检测率 ≥ 随机猜测(0.5)"是安全下界成立的必要条件。
- 阈值：各 budget 下 detection_rate 若仍 <0.5，撤销 v42 安全主张入 paper；无需新 backbone，纯本地扰动 + 0-LLM 复算。

### 6.4 Adendum D — P-C eta 扫描退化（r2_per_eta 与 model 无关）

- 缺口：P-C 的 R2-η 扫描未真正 fit 各 model 数据；且"P-C 双 PASS"与"P-C_two_phase FAIL_H0"口径需对账。
- 证据：`_v3x_experiments_2026_09_16` `exp_3_3_p_c_supplement` 的 `r2_per_eta` 对 9 个 model **逐字相同**（9 个值完全一致），R2 仅随 η 变、不随 model 的 `t_frac` 变 → 扫描是退化的；同文件 `exp_d7` 记 `P-C_two_phase = "FAIL_H0 (幂律死)"`，与邀请函"P-C+P-D 双 PASS"疑似不同子指标。
- 增补实验：重做 per-model R2（让 η 扫描真作用于各 model 的 (t_frac, D_fix2)）；并在 frozen `KT_C1_SPEC` 口径下对"P-C PASS vs P-C_two_phase FAIL_H0"做一次对账，避免口径混用。
- 复用：与 §4 的"塌缩(Q) vs 幂律(R²)"口径分离思路一致，不新增指标。

### 6.5 Adendum E — P-D supplement（0 captions 未实跑）

- 缺口：P-D supplement 曾因缺 caption 失败，证据链可能缺一环。
- 证据：`exp_3_4_p_d_supplement = "error: only 0 captions, need 22"`；closeout 记 KIMI 已补 22 caption 做 P-D B3 Merkle，但 exp_3_4 落盘仍为 error 状态。
- 增补实验：用 KIMI 22 caption 重跑 exp_3_4，补齐 P-D supplement 产物并落 SHA-12，确认与"P-D 双 PASS"口径一致。

---

## 附：本提案依据的关键文件（只读，未改动）

- `deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16_v2.py`（P-L 根因 L64–66）
- `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json`（全网格 R2=1.0）
- `results/deposon_v3_physical_opt_60cells_2026_09_11.json`（9 model `T_frac60`，frozen 数据源）
- `deposon_team/plugins/_verify_15frozen.py`（0 LLM hashlib 复算 + resolve/archive fallback 模式）
- `deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md`（§0.1/§2.4 各实验 UNVERIFIED 披露）
- `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json`（P-J 占位）
- `results/_p_i_curvature_audit_probe_2026_09_16/`、`results/_p_i_real_labels_2026_09_16/`（P-I AUC 标签占位）
- `results/_p_m_attack_surface_cost_2026_09_16/`、`results/_p_m_real_separation_2026_09_16/`（P-M detection=0 vs SECURE / v42 须重设计）
- `results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json`（exp_3_3 R2 同表复读、exp_3_4 0-caption error、exp_d7 P-C_two_phase FAIL_H0）

**Trae code 方提交，2026-09-17。诚实降级承诺：本提案不预设 PASS；P-L 的 Q>0.15 / R²<0.9、P-I 的 AUC≤0.5、P-M 的 detection<0.5 等负结果均如实入 paper 局限性。**