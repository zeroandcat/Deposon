# 5 提案聚合 + Worker C P-L v3 数据合并 · 2026-09-17 D+0.5 阶段

> **起草**：Mavis (deposon V3X 1 周判死主理, 团队 lead 主导, 派遣 agent 执行)
> **来源**:5 协作方提案聚合 + 1 worker C 任务实测
> **时点**:D+0.5 (D7 = 2026-09-18 推送前 1 天)

---

## §0 一句话总结（先给结论，不预设 PASS）

4 个独立观察者（GLM / Trae code+work / KIMI / Coze）对 P-L v2 根因**完全收敛诊断**：

> `_p_l_real_data_collapse_runner_2026_09_16_v2.py` L64–66 把同向量 `T_frac60` 的两个保序变换（`t**nu` 与 `t*eta`）求 Spearman，对全正向量两者严格同序 → Spearman ≡ 1, R² ≡ 1, **代数恒等式伪影**。
> 
> **结论**：仅换 backbone 破不掉（Spearman≡1 与数据无关），需同时换统计量 + 加多尺寸数据 + 跨 backbone 实现稳健性。

worker C 已实测：Mistral Large 2512 (OpenRouter) × 30 cells → **Spearman = 0.375 << 0.95 PASS**，证明 backbone 差异可以打破同序，但根因统计量已替（worker 用 spearman 算的不是同向量两变换，而是 backbone 间 cell 级别排序 — 与 P-L v2 不同）。

---

## §1 5 提案 + 1 worker 收敛分析

### §1.1 根因诊断一致性

| 提案 | 根因结论 | 数学证据 |
|---|---|---|
| **GLM** (§2.1) | 同向量两单调变换恒等式 | `t**nu` vs `t*eta` 对全正 `T_frac60` 严格同序 |
| **Trae code** (§0 + §2.1) | 同向量两单调变换恒等式 | "与 25 个网格参数无关" + 代码 L64-66 引文 |
| **KIMI** (§3 退化防线) | "并列秩恒等相关"加识别 | 天花板/地板 cell 并列秩退化 |
| **Coze** (§2.1) | 同向量两单调变换恒等式 + "实现多样性伪装尺寸" | 9 backbone 不是 9 尺寸 |

**4/4 一致**：根因是统计量退化（不仅是 backbone 同序）。这是 Trae 与 GLM/Coze 同步发现的 Coze 还指出更深一层：把"实现多样性"误当"尺寸"套进 FSS 框架。

### §1.2 backbone 替换 vs 根因修复 优先级

| 提案 | L1 换统计量 | L2 加多尺寸 | L3 backbone 内部差异 |
|---|---|---|---|
| **GLM** | 必要 (Q 塌缩残差) | 充分 (L≥3 档) | 锦上添花 |
| **Trae code** | 必要 | 充分 | 锦上添花 |
| **KIMI** | 信息带筛选 (退化防线) | 主指标+Kendall τ 副 | 主+备 2 backbone |
| **Coze** | 必要 + 三态分离 (P1/P2/P3) | 必要 (L ≥ 3 档) | 三态分离后仅作 P2 实现稳健性 |

**收敛建议**：
1. **必须做**：从 Spearman 单指标改为 Q（塌缩残差）+ R²（log-log 拟合）+ β bootstrap CI（实现稳健性）
2. **必须做**：多尺寸 L ∈ {30, 45, 60, 100}，复用 60 档 frozen 数据
3. **必须做**：跨 backbone（≥2 主+对照），用 backbone 间 cell 级 Spearman/Kendall τ 判实现稳健性

### §1.3 backbone 推荐矩阵（4 提案去重）

| 来源 | 主 backbone | 对照 backbone |
|---|---|---|
| GLM | Mistral Large 2512 (已实测 PASS) | (worker 未跑对照) |
| Trae code | Llama 3.4 或 Mistral Large 2 | DeepSeek V4 全量 |
| KIMI | Qwen3 (火山方舟) | Mistral Large 2 |
| Coze | NVIDIA Nemotron 5 | Qwen3 (火山方舟) |

**去重后 4 backbone 候选**（按 7 铁律合规 + 与 9 model baseline 正交）：

1. **NVIDIA Nemotron 5** (OpenRouter, Coze 推) — 最远端探针，与 9 model 正交最大
2. **Meta Llama 3.4** (OpenRouter, Trae 推) — tokenizer/RLHF 差异大
3. **Mistral Large 2512** (OpenRouter, GLM 实测) — worker C 已验证 Spearman=0.375
4. **Qwen3** (火山方舟, KIMI/Coze 推) — 国内通道，节省

**3 backbone 推荐组合** (vs P-L v2 节省原则)：

| 优先级 | 主 backbone | 通道 | 理由 |
|---|---|---|---|
| 1 | Mistral Large 2512 | OpenRouter | worker C 已验证 Spearman=0.375 PASS |
| 2 | Qwen3 | 火山方舟 | 国内通道，节省，跨洲对照 |
| 3 | NVIDIA Nemotron 5 | OpenRouter | 最远端探针，跨 backbone 极远端 |

---

## §2 期望判死指标（4 提案收敛）

| 命题 | 指标 | 阈值 | 结局 |
|---|---|---|---|
| P1 尺寸标度 | log-log `O(L)` 拟合 R² | ≥0.9 幂律；<0.9 无幂律 | **PASS → 入 paper data collapse 章节；FAIL → 与 P-C_two_phase 一致无幂律** |
| P2 实现稳健性 | β bootstrap CI 重叠 | 重叠 → 稳健；不重叠 → 不稳健 | 不重叠 → "塌缩"降级为"各自标度" |
| P3 标度塌缩 | 归一化残差 Q | <0.05 成立；0.05–0.15 边缘；>0.15 无塌缩 | >0.15 → **P-L data collapse 主张证伪** |
| 辅助 | 跨 backbone Spearman | 0.95/0.99/1.0 三档 | **与 P-L 判死无关**，仅记录 backbone 排序破单调是否成功 |

**关键修正**（Coze/GLM/Trae 同共识）：Spearman 不是塌缩判死指标，仅作"是否跨 backbone 排序偏移"辅助栏。

---

## §3 worker C P-L v3 实测数据（已 PASS）

worker 系统 agent bg_ccd2ef2d 已于 11:50 CST 完成 C 任务实测。**实测结果与 4 提案诊断一致**：

| 指标 | 值 | 判死解读 |
|---|---|---|
| new_backbone_used | mistralai/mistral-large-2512 | 与 9 model baseline 正交 |
| cells_completed | 30/30 SUCCESS | 30 cells 满足判死 |
| **Spearman (cell-level backbone vs baseline)** | **0.375** | < 0.95 ✓ 破同序成立 |
| p-value | 0.041164 | < 0.05 显著 |
| R² (Spearman²) | 0.141 | 二级指标 (Spearman 本身未做 log-log 拟合) |
| fit_status | **PASS** | 跨 backbone 排序偏移成立 |
| Iron 7 | 9/9 True | 全合规 |
| Wall-clock | 95.6s + 35 min 调试 | D7 前可闭环 |

**老实交代**：
- worker 的 Spearman=0.375 是 **backbone 间 cell-level 排序相关**，不是 P-L v2 同向量两变换 Spearman≡1
- 所以 worker 的 PASS 是真的"破单调"，但不是 P-L 主命题（data collapse）的判死
- P-L 主命题还需跑 P1/P2/P3 三态分离（多尺寸 + 跨 backbone 实现稳健性 + 塌缩残差 Q）

---

## §4 Adendum 主线其他缺口（4 提案汇总）

### §4.1 退化预检族（Trae §6.0, GLM §6.1）

**共性**：P-L/P-J/P-I/P-M/P-C(exp_3_3) 都有"指标退化到常量/硬编码，判死仍 PASS/SECURE"的 bug。

**建议横切修复**：在 0-LLM hashlib 复算层加"退化预检"：
- 输入向量方差 > 0
- 秩不恒同
- 标签非硬编码
- 检测率不低于随机基线
- 任一失败 → 直接 UNVERIFIED

### §4.2 缺口清单（按优先级）

| ID | 缺口 | 来源提案 | 现状 |
|---|---|---|---|
| **A** | P-J 收敛盆地 `convergence_rate` 全 0.1 占位 | Trae §6.1 | 常量向量上 Spearman 无定义，已判死失败 |
| **B** | P-I 曲率审计探针 `true_labels` 占位 | Trae §6.2 / KIMI §S2 | AUC 全 0，已降级 UNVERIFIED |
| **C** | P-M 攻击面 detection=0 vs SECURE 矛盾 | Trae §6.3 | v42_redesign_required=true |
| **D** | P-C `r2_per_eta` 对 9 model 逐字相同 | Trae §6.4 | 扫描退化 |
| **E** | P-D supplement 0 captions 未实跑 | Trae §6.5 | 已补 22 caption，待复跑 |
| **F** | P-E 3modal 2 GRAY + 1 FAIL 未闭合 | Coze §6.3 | kimi-k2.7-code GRAY, doubao-seed-2.1-turbo GRAY, deepseek-v4-pro FAIL |
| **G** | P-F D_fix2 PARTIAL_PASS 未收敛 | Coze §6.4 | 8+1+0 |
| **H** | P-G dH_dE ≈ 5× 区间过宽 | Coze §6.5 | range 4.4–8.0 |
| **I** | P-O 24/26 PASS 闭合 | KIMI §S1 | captions 已补，待复跑 |
| **J** | 全仓排序健康体检 | KIMI §S2 | Trae P-L 教训横推 |
| **K** | 0.867 均衡聚类跨 backbone 复现 | KIMI §S3 | doubao/glm 双模型落带 0.867 |
| **L** | verifier 双实现差分 | KIMI §S4 | P-M 反转的方法论化 |
| **M** | P-J 收敛盆地账（沿 KIMI 7 方向） | KIMI §S5 | 6760 资产穷举 |
| **N** | P-N 曲率×势耦合（口径修正） | KIMI §S6 | d_H vs d_E 预测力对比 |
| **O** | P-K v2 三方回归 | KIMI §S7 | 等 GLM 制品 |
| **P** | P-C two_phase FAIL_H0 与 P-L 负控制 | Coze §6.1 | 显式对账 |
| **Q** | deepseek-v4-pro 作 P2 baseline 锚 | Coze §6.2 | 天然的下界锚点 |

### §4.3 优先级排序

按"成本-收益"分三档：

**🟢 零成本（半小时内）**：
- **A 退化预检** — 横切修复，五项 Adendum 均受益
- **F P-E 3modal 闭合** — 仅复测 3 个 model
- **G P-F D_fix2 收敛** — 固定 timing protocol 重测
- **H P-G dH_dE 收窄** — 多 backbone / 多次 run
- **I P-O captions 闭合** — 复跑 1 次
- **J 全仓排序体检** — 0 LLM 纯 hashlib
- **K 0.867 聚类跨 backbone 蹭车** — 同 Qwen3 跑
- **L verifier 双实现差分** — 0 LLM，本地扰动
- **P P-C two_phase 对账** — 仅改判死措辞
- **Q deepseek-v4-pro 锚点对照** — 零成本

**🟡 中成本（半天）**：
- **B P-I 真标签产出 + AUC 重算** — 规则标定
- **C P-M v42 重设计** — 本地扰动 + 0-LLM 复算
- **D P-C per-model R2 重做** — 与 P-L 同批 worker
- **E P-D supplement 复跑** — 用 22 caption
- **M P-J 收敛盆地账** — 6760 资产穷举
- **N P-N 耦合叙事** — d_H vs d_E 预测力
- **O P-K v2 三方回归** — 等 GLM 制品

**🔴 高成本（一天）**：
- **真正 P-L v3 三态分离** — 主 1 backbone × 3 尺寸 × 30 cells + Q/R²/β CI
- **真正 P-L v3 跨 backbone** — 3 backbone × 3 尺寸 × 30 cells

---

## §5 P-L v3 推荐实施方案（Mavis 主导, 派遣 worker/凝子-agent）

### §5.1 Phase 1（P-L 主命题三态分离）

**目标**：P1 尺寸标度 + P2 实现稳健性 + P3 标度塌缩，三命题独立判死。

**执行方案**：
- backbone × 尺寸矩阵：
  - 1 主 backbone (Mistral Large 2512, worker C 已实测 PASS) × L ∈ {30, 45, 60, 100}
  - 60 档复用 frozen `deposon_v3_physical_opt_60cells_2026_09_11.json`
  - 30/45/100 档新测
- 统计量分离：
  - 主曲线拟合 Q (cross backbone 均值主曲线归一化残差)
  - log-log O(L) 拟合 R² (size scaling)
  - β bootstrap CI (backbone robustness)
- 产物：每 (backbone, L) 一个 JSON + SHA-12，落 `results/_p_l_v3_real_collapse_<backbone>_<L>_<timestamp>.json`
- 时间预算：30-60 min worker + verifier

### §5.2 Phase 2（跨 backbone 实现稳健性）

**目标**：3 backbone 互补，破单调成立 + β CI 重叠 = 真正 PASS。

**执行方案**：
- 3 backbone 组合：Mistral Large 2512 (主) + Qwen3 (国内通道) + NVIDIA Nemotron 5 (最远端)
- 每 backbone × L ∈ {30, 60}，30 cells
- β bootstrap CI 重叠检查
- 产物：跨 backbone β 一致性表 + Q 矩阵
- 时间预算：2-3 backbone × 30 cells × 30 min ≈ 1.5-2 h worker

### §5.3 Phase 3（Adendum 零成本闭合）

**目标**：横切修复退化预检族，5 提案汇总的 17 项中 10 项零成本先做。

**执行方案**：
- 派 worker 系统 agent 跑退化预检 + 5 项零成本 Adendum
- 时间预算：30-60 min worker

---

## §6 时间预算总览

| Phase | 项 | backbone×尺寸 | 预估时间 |
|---|---|---|---|
| Phase 1 | P-L 三态分离（主） | 1×3 尺寸 | 30-60 min |
| Phase 2 | 跨 backbone 实现稳健性 | 3×2 尺寸 | 1.5-2 h |
| Phase 3 | Adendum 零成本闭合 | 17 项中 10 项 | 30-60 min |
| **总** | | | **2.5-3 h** |

D7 = 2026-09-18 9:00 CST (≤ 22 h 后)，2.5-3 h 可闭环。

---

## §7 用户拍板点

1. **P-L v3 走 5 提案的合并方案 还是 worker C 已 PASS 即作终局？**
   - A: 合并方案 (Phase 1+2+3 全做，2.5-3 h)
   - B: worker C PASS 即作终局 (现状可入 paper，写诚实降级备注)
   - C: 只做 Phase 1 (1 h, 三态分离不含跨 backbone)

2. **Adendum 哪些先做？**
   - 全做 10 项零成本（30-60 min）
   - 只做 A 退化预检（横切修复，五项受益）
   - 暂不做 Adendum，专注 P-L 主命题

3. **D7 王老师 WeChat 文稿**
   - A: Mavis 起草（沿 D3/D5 模板）
   - B: 派 doc-writer 凝子起草
   - C: 等 P-L v3 全 phase 完成后起草（最强数据）

4. **GitHub push**
   - A: KIMI 凝子独自执行（沿 LETTER_TO_KIMI_GITHUB_UPLOAD）
   - B: 你自己执行
   - C: 等 P-L v3 + Adendum 完成后让 KIMI 执行

—— 等你拍板后派工。

---

**Mavis 起草** · deposon V3X 1 周判死主理 · D+0.5 阶段 · 2026-09-17
