# 增补实验设计提案 · Coze 方

## Deposon V3X D+0.5 · P-L v2 缺口重测 · 提案方：Coze

**提交时间**：2026-09-17（周四）CST
**主送**：Mavis（deposon V3X 1 周判死主理）
**响应邀请**：`results/_v3x_d0_5_experiment_invitation_2026_09_17.md`
**铁律声明**：本提案为设计提案，不触碰任何 frozen；正文不写任何 key；不增派 LLM。

---

## 0. 一句总结论（先给结论，不预设 PASS）

P-L v2 的 R2=1.0 **已确诊为代数恒等式伪影**：`_p_l_real_data_collapse_runner_2026_09_16_v2.py` L64–66 对同一个向量 `T_frac60` 做两个单调变换 `t**nu` 与 `t*eta` 后求 `spearmanr`——对实测 `T_frac60 ∈ [0.5333, 0.8667]`（全正、全在 (0,1)），`ν>0` 时 `t**ν`、`η>0` 时 `t*η` 均严格单调增 → 严格同序 → Spearman≡1、R2≡1，结果 JSON 也确实 25/25 网格点全 1.0。这与换不换 backbone 无关。

但根因比"统计量选错"更深一层：**P-L 把"实现多样性（backbone）"误当"尺寸（size）"套进了有限尺寸标度框架**。9 个 backbone 的 `T_frac60` 是「单一 L=60 下的 9 个实现」，不是「同一系统的 9 个尺寸」。真正的 data collapse 需要「同一系统（实为同一 backbone）在多个尺寸 L 下的序参量」。

因此 Coze 主张：**三态分离 + 分步预注册**——先把「尺寸标度 / 实现稳健性 / 标度塌缩」三个命题拆开各自判死，再谈 backbone 选择。换 backbone 不是"破 Spearman"（破不掉），而是给「实现稳健性」命题提供远端数据点。

---

## §1 Backbone 选择

推荐 **2 个 backbone**（在 1–3 上限内），**均与现有 9 model 及 Trae 方选择的正交**：

| 优先级 | Backbone | 通道（铁律 2/3/6） | 选择的理由（最大化实现分歧） |
|---|---|---|---|
| 主 | NVIDIA **Nemotron 5** | OpenRouter（非 OpenAI/Anthropic/Google） | 现有 9 model 为豆包×3 / GLM×2 / DeepSeek×2 / MiniMax×1 / Kimi×1，Trae 选 Llama/Mistral/DeepSeek V4 后仍未覆盖 NVIDIA 系；Nemotron 自研 tokenizer + 训练语料 + RLHF 奖励模型与上述全部差异最大，是实现稳健性检验的最远端探针 |
| 对照 | **Qwen3** | 火山方舟 coding-plan（国内，铁律 2，复用 ark-* key） | 阿里系，9 model 无 Qwen；tokenizer 边界（中英/代码混合分词）与豆包/GLM 不同；国内通道节省，可作"同批 cells 的次远端"对照 |

**明确声明**：这两个 backbone 的目的**不是**"破 Spearman=1"（那是代数恒等式，换任何 backbone 都破不掉），而是为 §2 的「实现稳健性」命题提供最大分歧的数据点，供塌缩残差 Q 与标度指数一致性检验使用。

---

## §2 同序单调破局方法

### 2.1 根因复核（独立、0 LLM、确定性）

- `transformed = [t**nu for t in T_frac60]`、`eta_transformed = [t*eta for t in T_frac60]`，`spearmanr(transformed, eta_transformed)`：对同一向量、两个保序变换求秩相关，恒为 1。这是**秩不变的代数事实**，与 `ν/η` 网格、与数据内容（哪个 backbone 的 T_frac60）都无关。
- 该事实可写成一个纯确定性 frozen 函数（输入任意 9 维正向量 + (ν,η) 约束，输出恒 1 的证明），**不依赖跑任何模型**即可 hashlib 复算——建议把这一条固化为本实验的前置锚，让"R2=1.0 是伪影"不再需要辩论。

### 2.2 真正的破局 = 三态分离（Coze 的增量）

Trae 方正确指出"换统计量"（Spearman → 主曲线拟合残差 Q）。Coze 再进一层：**换统计量之前必须先澄清「尺寸 L 的语义」**，否则换统计量 + 多尺寸跑出来的，仍是用"实现多样性伪装尺寸标度"。

拆成三个命题，各自独立判死：

- **P1 尺寸标度（size scaling）**：对**单一 backbone**，令 L = cells 数量，测序参量 O(L)（建议取 D_fix2_cosine 或 T_frac），检验 `O(L) ≈ c·L^{-β}` 的幂律标度。判据：log-log 线性拟合 Pearson R²。
- **P2 实现稳健性（backbone robustness）**：对**同一 L**，跨 backbone 的 O 及其标度指数 β 是否一致。判据：β 的 leave-one-backbone bootstrap CI 是否重叠 / O 的跨 backbone 离散度。
- **P3 标度塌缩（data collapse）**：**仅当 P1 成立 且 P2 的 β 跨 backbone 一致**时，多 backbone 的 O(L) 曲线才能塌缩到同一条主曲线。判据：归一化塌缩残差 `Q = RMS(O_rescaled − fit) / RMS(O_rescaled)`。

P-L v2 的错误 = 既不是 P1（无多尺寸 L）、也不是 P2（无指数一致性）、更不是 P3。

### 2.3 预期破局机制（为何 backbone 内部差异会产生真实偏移）

不碰 prompt format（那是 pass-through，禁止）。Nemotron 5 / Qwen3 通过**内部差异**改变 T/R/A 的**具体数值**，从而改变 O(L) 的拟合与标度指数 β：

- **tokenizer 边界差异**：对 GSM8K 数字 token 的切分粒度不同 → T（透射/正确率）的单元口径不同。
- **RLHF 后训练差异**：错误路径"反射 vs 透射"的倾向不同 → R/A 分配比例偏移。
- **长上下文衰减差异**：StrategyQA 推理链的指令遵循在前 60 cells 与后段衰减不同 → T(L) 的 L 依赖形态不同。

要点：即使仍用错误统计量 Spearman 恒=1，这些差异也不可见；**只有换到 O(L) 的幂律拟合 + 残差 Q，backbone 差异才会以 β 的偏移 / Q 的增大形式显现**——这正是三态分离的意义。

### 2.4 诚实边界（预先写死，禁止修饰）

若 P-L 没有可调控制参数（无"温度/失真强度"这类参量），则严格 FSS 塌缩命题可能本身定义不清：此时**只能退化为单参数幂律标度**（P1），"data collapse"措辞如实降级为"幂律标度"（P1）或"实现收敛"（P2）。此判断 Coze 不下结论，交 Mavis/用户对照 frozen `KT_C1_SPEC_V0.1` 确认。

---

## §3 测法

- **cells**：GSM8K + StrategyQA 子集，沿用现有 5 制品 cell 结构；**30 cells 起步**（判死级，邀请函要求），预算内可到 60。
- **尺寸档**：L ∈ {30, 60}（60 档复用现有 T60/R60/A60 frozen 数据），可选补 {100}；**每个 backbone × 每个 L 独立跑**。
- **0 LLM 纯 hashlib 复算层**：Q 残差、log-log 线性拟合、β 的 bootstrap CI——全部为纯确定性数值运算，可 hashlib 复算，不依赖任何 LLM call 确认结果；沿 `_verify_15frozen.py`（或 `_verify_15frozen.py` 兼容口径）的 resolve + sha256 模式。
- **baseline**：原 5 制品 baseline JSON（KIMI/GLM_1/GLM_2/coze/MiniMax）+ 现有 9 model 的 T30/T60 frozen（`deposon_v3_physical_opt_60cells_2026_09_11.json` 的 `P_C_distortion_bound_60cells.per_model`）。
- **产物**：每 (backbone, L) 一个 JSON + SHA-12；0 新 frozen 触发条件；新结果落 `results/_p_l_*` 独立子目录，**不动 18 frozen + P-G V0/V0.1 + 4 plugin spec**。

---

## §4 期望阈值（预注册三态 + 双重判据，禁止 reassign）

| 命题 | 指标 | 阈值 | 结局 / 后续 |
|---|---|---|---|
| P1 尺寸标度 | log-log `O(L)` 线性 Pearson **R²** | `R² ≥ 0.9` 幂律标度成立；`< 0.9` 无标度 | 无标度 → **P-L 证伪**，入 paper §7.2 |
| P2 实现稳健性 | 跨 backbone 标度指数 β 的 bootstrap **CI 一致性** | CI 重叠 → 稳健；不重叠 → 不稳健 | 不稳健 → "塌缩"降级为"各自标度" |
| P3 标度塌缩 | 归一化塌缩残差 **Q** | `Q < 0.05` 塌缩成立；`0.05–0.15` 边缘，补一档尺寸；`> 0.15` 无塌缩 | `> 0.15` → **P-L data collapse 主张证伪** |
| 辅助（不判塌缩） | 跨 backbone Spearman | 仅记录，`=1.0` 只说明"若沿用错误统计量仍同序" | **与 P-L 判死无关** |

**关键修正**：邀请函 §4 原表把 Spearman 作为 data collapse 判死依据。Coze 主张——**Spearman 只能判"单调"、不能判"塌缩"**；P-L 的判死依据应为 `Q`（塌缩残差）+ 幂律 `R²`（尺寸标度）+ β CI（实现稳健性）三者分离。这样即使 Spearman 仍=1，也不污染 P-L 塌缩结论。

---

## §5 风险评估

- **API 风险**：OpenRouter 免费额度限速（铁律 3：只调非 OpenAI/Anthropic/Google，避免 layer-2 user_id 门控），Nemotron 5 单 cell 延迟偏高；火山 coding-plan Qwen3 有并发上限。方案：**主 backbone 30 cells 先跑通再扩**（铁律 4 节省原则，不一次跑 300 cells）。
- **frozen 触动风险**：本实验**不应新增任何 frozen 触发**（邀请函已声明）。新产物只写 `results/_p_l_*`；若需读 frozen 文件，只读并落 SHA-12 before/after 报告（沿 Q2 reconcile 流程）。`conservation.py` V0=`4bdec2683f06` 不动，作 Q2 metadata 保留。
- **时间预算**：2 backbone × 30 cells × 30 min ≈ **60–90 min** 派 worker（邀请函估），verifier 复算 + 写 P-L v3 制品，D7 前可闭环。

---

## §6 主线上其他增补方向（Coze 附加观察，不影响 P-L 主缺口）

Coze 复读 `d7_5anchor_60cells_9model_verdict_2026_09_18.json` 时，注意到主线 P-A ~ P-G 尚有数个**未闭合点 / 交叉线索**，建议并入本轮增补（边际成本低、且与 P-L 同批 worker 跑）。按优先级列出，供 Mavis 聚合时取舍：

### 6.1（高）P-C two_phase `FAIL_H0（幂律死）` = P-L 幂律前件的负控制

- **现状**：D7 verdict 已录 `P-C_two_phase = FAIL_H0 (幂律死)`；而 P-L 正是 P-C 的有限尺寸标度（data collapse）验证。data collapse 的**数学前件是"存在幂律标度"**。
- **观察（交叉预测）**：若 P-C 两相幂律已死，P-L 的尺寸标度（§2.2 的 P1）大概率也 `FAIL_H0`（无幂律）——两个独立命题应指向同一"无幂律"结论。
- **增补动作**：在 P-L v3 判死表里显式加一条负控制：**「若 P-L P1 幂律 `R²<0.9`，判为与 P-C two_phase 一致的幂律死，而非 P-L 实验失败」**。把两个命题的张力变成 self-consistent 的交叉证伪，而非孤立的一次失败。
- **价值**：避免把"正确的证伪"误报为"实验失败"，且这是 paper 中「两个独立通道指向同一无幂律」的强证据，不需额外跑模型、只改判死措辞。

### 6.2（高）deepseek-v4-pro 跨命题一致掉队 = 现成的实现稳健性（P2）baseline 锚

- **现状**：deepseek-v4-pro 是 9 model 中最弱、且跨命题一致掉队——`T_frac60` 最低（0.5333）、`cos_sim` 最低（0.8225）、`D_fix2_cosine` 最高（0.1775）、P-A `GRAY`、P-E `FAIL`。
- **观察**：这已是**天然的实现稳健性极端样本**，无须新跑即可当作 P2 的 baseline 下界。
- **增补动作**：新 backbone（Nemotron 5 / Qwen3）的 `T_frac60 / cos_sim / D_fix2` 结果，与 deepseek-v4-pro 这个锚点对齐比较——判断新 backbone 是否落在该锚点邻域之外。
- **价值**：把「换 backbone 是否产生真实偏移」的判断，从失效的「Spearman 是否 =1」换成有效的「新 backbone 是否偏离 deepseek-v4-pro 掉队锚点」。零新增成本，直接服务 §2.2 的 P2。

### 6.3（中）P-E 3modal 的 2 GRAY + 1 FAIL 未闭合

- **现状**：`P-E_3modal` 9 model 中 6 PASS，但 `kimi-k2.7-code` **GRAY**、`doubao-seed-2.1-turbo` **GRAY**、`deepseek-v4-pro` **FAIL**。
- **增补动作**：定向复测这 3 个 model 的 P-E 3modal，判定 GRAY→PASS/FAIL；并诊断 deepseek-v4-pro 的掉队机制（长上下文衰减 vs 真实模型退化）。
- **价值**：P-E 是当前 GRAY/FAIL 最多的命题，闭合它的灰区，比只补 P-L 更能拉高「全命题无灰区」的判死完成度。

### 6.4（中）P-F `D_fix2` "A channel timing 敏感" PARTIAL_PASS 未收敛

- **现状**：`P-F_D_fix2_strict` 与 `P-F_D_fix2_loose` 均为 `8+1+0 (PARTIAL_PASS, A channel timing 敏感)`。
- **增补动作**：固定 A channel 的 timing protocol（消除时序噪声），重测 P-F，把 PARTIAL_PASS 收敛为 PASS 或暴露真实 FAIL。
- **价值**：PARTIAL_PASS 是"判死未完成"的中间态，D7 王老师推送前最好不留 PARTIAL。

### 6.5（低）P-G `dH_dE ≈ 5x`（range 4.4–8.0）区间过宽

- **现状**：`P-G_V0.1_dH_dE ≈ 5x`，但 range 4.4–8.0（近 2 倍波动）。
- **增补动作**：多 backbone / 多次 run 收窄 dH_dE 估计，判断是真实物理参数还是测量噪声。
- **价值**：若收窄到稳定值，P-G 数值锚更硬；若收不窄，如实标注为测量不确定性（诚实降级，不修饰）。

---

## 附：本提案依据的关键文件（只读，未改动）

- `deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16_v2.py`（根因 L64–66，Coze 独立复核）
- `results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json`（25/25 全 R2=1.0，坐实伪影）
- `results/deposon_v3_physical_opt_60cells_2026_09_11.json`（9 model `T_frac60`，实测 [0.5333, 0.8667]，frozen 数据源）
- `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json`（9 model 名单 + P-A/P-C/P-E/P-F/P-G verdict）

**Coze 方提交，2026-09-17。诚实降级承诺：本提案不预设 PASS，Q>0.15 / R²<0.9 / β CI 不重叠均如实入 paper 局限性。**