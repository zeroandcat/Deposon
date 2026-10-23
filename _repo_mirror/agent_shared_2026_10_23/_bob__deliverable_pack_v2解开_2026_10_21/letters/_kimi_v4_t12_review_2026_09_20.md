# KIMI-K3 Response to V4 Experiment Design Invitation (draft v0.1, 2026-09-20)

**From:** KIMI-K3（凝子-agent, paper-track reviewer, V1–V3）
**To:** Principal Investigator（and Mavis `doc-writer` for record）
**Re:** Track 1 (distillation) + Track 2 (reverse-distillation) — pre-D1 design review
**Verdict on the draft:** 条件性接受评审委托（Accept review assignment, conditional）。Track 1/2 结构成立、冻结资产边界清晰（§1.5/§2.7 值得肯定）；但下列 R1/R2/R6/R7 为 **invalidate-level**，不解决则 Track 1/2 的结论不可检验。本文遵循 §7.4 论文轨 Markdown 格式。

---

## A. Track 1 — Distillation（forward）

### 🔴 R1（Blocker）· 五件冻结 artifact 的供应商重复计数

§2.1 稳定性规则为「≥3 of 5 frozen artifacts」，但五件 artifact（KIMI / GLM_1 / GLM_2 / coze / M3）只覆盖约 4 个 vendor lineage，GLM_1 与 GLM_2 同源。一个 mode 若仅出现于 GLM_1 + GLM_2 + 任一其他，即达 3/5，却仅代表 2 个血统——「跨骨干稳定」被系统性高估。**建议**：稳定性按 vendor lineage 去重计数，要求 mode ≥3 artifacts **且** ≥2 distinct vendor lineages；并在 mode-set 表中为每个 mode 标注血统覆盖（哪几家 vendor）。另请 PI 在 D1 前明确：V2 的 9 backbone → 5 frozen artifacts 的映射表，否则审稿侧无法复算该规则。

### 🔴 R2（Blocker）· 「high-density region」无可检验规范

§2.1 第 2 步未指定密度估计器与半径 ε，§2.1 末尾却承诺「same protocol yields same mode set」。可复现性承诺目前不可检验。**建议**：预注册（a）密度估计器（固定半径邻域 or k-NN 密度，二选一）；（b）ε / k 的数值及其校准来源（建议用 held-out cells 校准，而非全量 60 cells）；（c）三个嵌入帧的**融合规则**——逐帧取 mode 再取交集，还是联合嵌入后取 mode？两者不等价，必须选定其一写入协议。

### 🟡 R3（Major）· 失败阈值的 null-model 地板缺失

FAIL_DISTILLATION_HOMOGENEOUS（≤2 modes）与 FRAGMENTED（one mode per cell）目前是拍脑袋边界。**建议**：对 cell 标签做排列检验（permutation, n≥1000），导出 mode 数量的零分布，把两个 FAIL 阈值锚定在零分布的分位点上（如 <5% 与 >95% 分位）；60 cells 样本量小，另需 bootstrap 报告 mode 数量的置信区间。

### 🟢 R4（Minor）· 复制轴的嵌套关系需澄清

§2.1 要求 mode 同时 ≥3/21 caption pairs 与 ≥3/18 anchors。若 18 anchors 是 60 cells（或其子集）的重测，则这两个「≥3」不是独立复制证据，而是同一信号的两次计数。**建议**：在 mode-set 表中明示 caption / anchor / cell 的嵌套关系，并在显著性陈述中只把真正独立的轴计入证据强度。

---

## B. Track 2 — Reverse-distillation

### 🔴 R5（Blocker）· 嵌入点 ≠ 分布，对称 KL 无从算起

§2.2 第 2 步默认「symmetric KL on per-cell embedding distributions」，但 Track 1 产出的是嵌入**点集**，不是分布。必须先规定点→分布的构造（KDE 带宽 h，或 Voronoi 直方图），否则 divergence 不可复算。**建议**：主度量改用 Jensen–Shannon divergence（有界、对称、对零概率稳健），对称 KL 降为稳健性检查；点→分布构造与 h 一并预注册。

### 🔴 R6（Blocker）· 无 reject 选项，归因被迫强行着陆

§2.2 第 3 步为 argmin 归因：即使候选输出与所有冻结输入都不像，也会强行给出「最一致者」。FAIL_REVERSE_INFORMATIVE（均匀分布）只覆盖极端情形。**建议**：加入 reject 选项——全部 divergence 高于阈值 τ 则「不归因」；τ 用**冻结集以外的负对照骨干输出**校准，直接沿用 V3 P-K 的 FPR 校准法（P-K FPR 4.4% GRAY 的既有管线可复用，无需新协议）。此项同时也回应 §4.3 已承认的 distillation asymmetry 风险。

### 🟡 R7（Major）· argmin 需配 margin 规则

top-1 与 top-2 divergence 接近时归因不可靠。**建议**：margin = D₂ − D₁ < δ 时判 GRAY 并在 reverse-attribution 表中并列 top-2；δ 随 τ 一起校准。

### 🟡 R8（Major）· D3 held-out 集合需预先冻结

§2.6 D3 要求 recipient 在 held-out candidate 上跑归因。「held-out」的构成（哪些 cells / anchors / caption pairs 留出）必须在 D1 前冻结并写入 V4 自有 manifest，否则存在选择性报告空间。

---

## C. 跨轨（Track-agnostic）

### 🟡 R9（Major）· V4 自有资产自诞生即锚定

mode-set 表是 Track 2 的输入，若其内容在 D1→D5 间漂移，归因结论不可复核。**建议**：V4 mode-set 表与 reverse-attribution 表自诞生即计算 SHA-12，沿用冻结资产的锚定规约（V4 自有、独立路径，不触碰 §2.7 左列）。

### 🟢 R10（Minor）· Track 3 placeholder 的可证伪性验收要求

按 §7.3，本评审不定义 anti-distillation 机制。仅提一条验收要求供 PI 参考：任何操作定义须能在一周节奏（D1/D3/D5）内产出 PASS/FAIL 信号，且不引入新嵌入协议、不触碰冻结资产——与 §2.3 既有约束一致。

### 🟢 R11（Minor，增补实验方向 · 主线上未提及）

按惯例并入我注意到的增补方向，均为 Track 1/2 的低成本加固，不新增协议：

1. **Backbone leave-one-out 稳定性**：每次剔除一件 frozen artifact 重算 mode set，报告 mode 保留率——量化 mode set 对单一血统的敏感度（与 R1 联动）。
2. **逐帧消融归因**：Track 2 分别只用 Poincaré / observer / Bell 单帧做归因，比较三帧一致率；三帧不一致的候选输出自动 GRAY。
3. **Caption 指纹排列地板**：Track 1 的 caption 轴显著性直接复用 R3 的排列检验输出，零额外实验成本。

### 🟢 R12（Minor）· §6 SHA-12 与 §5.4 占位符

确认 §9/§12 的 circulation blocker 清单；R9 落地后，V4 自有表也应进入同一核验闸。

---

## D. 结论

Track 1/2 设计骨架成立，冻结/自有边界（§2.7）与失败模式命名（§2.1/§2.2）是该草案的亮点。R1、R2、R5、R6 解决后，我可按 D1 节奏对 mode-set 表与归因程序做实质评审；R3/R4/R7/R8/R9 强烈建议同周期并入，否则 PASS 结论的证据强度会受质疑。预计 D1 评审耗时符合 5–10 分钟节奏。

---

*KIMI-K3（凝子-agent）· paper-track · 2026-09-20 · 本回复为评审意见，不构成对冻结资产的任何修改；AI 不作作者（遵循邀请函 §8）。*
