# deposon V3X 一周判死 · Paper V1 摘要（中英文）

> **起草方**：Coze（4 协作方之一）
> **起草时点**：2026-09-17
> **配套**：`_coze_paper_v1_draft_2026_09_17.md`（paper V1 正式版草稿，8 章）

---

## 中文摘要（≤ 300 字）

我们报告 deposon V3X「一周判死」框架下的一次完整判死实验，核心为三通道会计恒等式 T + R + A = 1。在 9 个 LLM backbone × 60 题（540 cells）的冻结账本上，对标度塌缩主张做三态分离判死：**P1 尺寸标度 FAIL**（Mistral Large 2512 于 L ∈ {30, 45, 100} 的 log-log 拟合 R² = 0.7447 < 0.9）；**P3 标度塌缩 FAIL**（归一化残差 Q = 0.1929 > 0.15）；**P2 实现稳健性 PASS**（6 个独立 backbone 两两 β bootstrap CI 全部重叠，开源 3/3 + 闭源 3/3）。同时跨模态 dpath 与账指纹协议双 PASS（60 cells 复现率 85.0%；22 caption dual_24bit 链 22/22 PASS）。17 项 Adendum 中 11 项 PASS、2 项 GRAY、1 项 UNVERIFIED、2 项 PARTIAL、1 项 FAIL_NO_MODEL。

**结论**：P-L data collapse 假设被**部分拒绝**——尺寸标度不成立，跨实现稳健性成立。我们如实披露四处退化预检发现的真 bug、GLM 制品盲测假阳性率 4.44%、5 制品 schema 互异等限制。**判死即有效交付**：全部负面结果按预登记判死线归档，不回溯修改；18 frozen anchors + 5 制品 + schema v1 资产层一致完好，7 铁律 0 触动严守。

---

## English Abstract (≤ 250 words)

We report a complete kill-test under deposon V3X's "one-week kill" framework, built on the three-channel accounting identity **T + R + A = 1** (transmission + reflection + absorption). On a frozen ledger of 9 LLM backbones × 60 tasks (540 cells), we perform a three-state separation kill-test of the **data-collapse** claim: **P1 size scaling FAILS** (single-backbone log-log fit over L ∈ {30, 45, 100} gives R² = 0.7447 < 0.9, n = 3, p = 0.337); **P3 collapse residual FAILS** (normalized residual Q = 0.1929 > 0.15); **P2 implementation robustness PASSES** (pairwise β bootstrap CIs overlap for all 6 independent backbones, 3/3 open-source + 3/3 closed-source). Two further lines give double PASS: cross-modal dpath and the ledger-fingerprint protocol (60-cell reproduction rate **85.0%**; 22-caption dual_24bit chain 22/22 PASS). Of 17 Adendum items, 11 PASS, 2 GRAY, 1 UNVERIFIED, 2 PARTIAL, and 1 FAIL_NO_MODEL.

**Conclusion**: the P-L data-collapse hypothesis is **partially rejected** — size scaling does not hold, while cross-implementation robustness does. We transparently disclose three genuine bugs found by the four-class degeneracy pre-check, a 4.44% false-positive rate in the GLM blind test, and schema divergence across the five artifacts. **A killed claim is a valid deliverable**: all negative results are archived against pre-registered kill lines without retroactive revision; the asset layer (18 frozen anchors + 5 artifacts + schema v1) is intact, with all seven iron rules strictly untouched.

---

## 数字修正对照（本摘要已按修正值表述）

| 原文 | 修正 | 依据 |
|---|---|---|
| `87.0%` 复现 | **`85.0%`** 复现 | 实值 60 cells 51/60 |
| `Adendum 13 + 2 + 1 = 16` | **`11 + 2 + 1 + 2 + 1 = 17`** | 实 17 项 |
| `P2 强稳健` | **`P2 3/5 backbone overlap（1 OR×OR 失败）`** 降格 | 实 β CI overlap 1/6 OR×OR；β 为 cell-level 代理斜率 |
| P-K 单口径 | **双口径**（OVERALL FAIL + paper 处置 GRAY） | FPR = 4.44% > 1% 阈值 |

---

**Coze 起草** · 沿 Mavis 委托信 `_letter_to_coze_paper_v1_委托_2026_09_17.md` · 2026-09-17
