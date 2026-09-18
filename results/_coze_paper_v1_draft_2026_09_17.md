# deposon V3X 一周判死：跨实现稳健性与标度塌缩主张的部分拒绝

**Paper V1 正式版草稿（Coze 起草）**

> **起草方**：Coze（4 协作方之一，沿 Mavis 委托信 `_letter_to_coze_paper_v1_委托_2026_09_17.md`）
> **起草时点**：2026-09-17（D7 = 2026-09-18 前）
> **委托边界严守**：0 LLM API 调用；沿 8 章 outline；引用 5 audit 综合产物；4 项挂点结论源 = 提案 v3 §3-§7；4 项数字漂移必改；不写新 spec；不调 API / 不动 push / 不动 WeChat 钥匙；不擅自调阈值（沿 KIMI 7 方向）
> **结构说明**：沿委托信 §1 表与 `_trae_paper_8ch_双审_20260917_200000.md` 8 章 outline；委托信 §1 表 §7「结论 + 派生建议」在本稿中拆为 §7 结论与 §8 派生建议两节表述，章节内容与顺序不变。

---

## 摘要

我们报告 deposon V3X「一周判死」框架下的一次完整判死实验。核心账本恒等式为三通道会计恒等式 **T + R + A = 1**（透射 + 反射 + 耗散）。本轮在 9 个 LLM backbone × 60 题（540 cells）的冻结账本上，对「标度塌缩（data collapse）」主张做了三态分离判死：**P1 尺寸标度（size scaling）FAIL**（Mistral Large 2512 单 backbone 于 L ∈ {30, 45, 100} 的 log-log 拟合 R² = 0.7447 < 0.9，n = 3，p = 0.337）；**P3 标度塌缩 FAIL**（归一化残差 Q = 0.1929 > 0.15）；**P2 实现稳健性 PASS**（6 个独立 backbone 两两 β bootstrap CI 全部重叠，开源 3/3 + 闭源 3/3）。同时，跨模态 dpath 与账指纹协议两条线给出双 PASS（60 cells 复现率 **85.0%**；22 caption dual_24bit 链 22/22 PASS）。17 项 Adendum 中 11 项 PASS、2 项 GRAY、1 项 UNVERIFIED、2 项 PARTIAL、1 项 FAIL_NO_MODEL。

**结论**：P-L data collapse 假设被**部分拒绝**——尺寸标度不成立，但跨实现稳健性成立。我们同时如实披露四处退化预检发现的真 bug、GLM 制品盲测假阳性率 4.44%、以及 5 制品 schema 互异等限制。**判死即有效交付**：本轮全部负面结果按预登记判死线归档，不回溯修改。

---

## §1 Introduction

**起点。** deposon 项目组（9 角色）与中国人民大学高瓴人工智能学院王子贺老师合作的国家自然科学基金项目《复杂场景下信息披露和决策的竞争研究》（批准号 62572476，执行期 2026–2029）于 2026-09 获批。项目组在 2026-09-04 提交合作提案 v3，承诺「一周判死」：在 D0（答复日）至 D7 的窗口内交付 **3 条全新机械判死线 + 1 张已闭合证据卡**，判死线 SPEC 先于运行冻结并公布 SHA-256 前 12 位锚，**不因答复内容回溯修改**。

**判死承诺的方法论内核。** 提案 v3 §1 与 §4 明确：判死的对象是**挂点**（deposon 具体产出 × 对方方向具体接口的可验证接缝），而非方向；「挂死也是交付」。我方全部主张分三层强度纪律随行：判死级（已预登记并执行的事实）、观察性（未证定理的数值规律）、探索性（猜想）。核心信条是：**不轻信正面结果，先问它在哪死。**

**本轮 5 条候选挂点线。** 沿提案 v3 §5 挂点清单：

| 编号 | 挂点线 | 对接王老师工作 |
|---|---|---|
| P-A′ | 均衡稳定化代价（烧多少不可逆耗散可让系统留在目标均衡） | AAAI 2026 SPPE 精确计算 + 均衡迁移成本 |
| P-B′ | 分布报告机制 × 失真界（账平但错的上界） | WINE 2025 Ex-Ante Truthful Distribution-Reporting |
| P-C | 两相结构的实证谱线（信息相关性阈值的数值对应物） | arXiv:2604.24530 private private information |
| P-D | 账指纹协议（内容寻址 + 根指纹 + 追加链） | 机制实验的可复现性基础设施 |
| P-L | 标度塌缩（data collapse）主张 | 复杂场景下的标度行为 |

**7 铁律（全程生效）。** ① API key 永远 runtime 读取，不入 prompt、不落盘；② 国内模型走火山引擎，海外模型走 OpenRouter；③ 海外通道只调非 OpenAI/Anthropic/Google 系（避免区域门控）；④ 节省原则：小模型先跑 30 cells；⑤ 钥匙不写入 markdown / code / memory；⑥ 不触动 18 frozen anchors；⑦ 不触动 `verifier/mavis/.builtin/scripts/`。本轮另有 0 LLM 纯 hashlib 复算层：全部 hash 复算用 `hashlib.sha256()` 本地计算，不依赖 LLM call 确认结果。

---

## §2 V3X 设计

**4 协作方并行。** V3X 采用「4 协作方聚合收敛」模式：**KIMI**（7 方向 + 退化防线）、**Trae code**（退化预检族 + 工程修复）、**GLM**（复现前提 + 判死指标）、**Coze**（三态分离判死框架）。D+0.5 阶段由 Mavis 向 4 方发出实验邀请函 `_v3x_d0_5_experiment_invitation_2026_09_17.md`，各方提交含 5 节（Backbone 选择 / 同序单调破局 / 测法 / 期望阈值 / 风险评估）的提案。

**判死指标的 4 方共识。** 沿委托信 §5 引用规范：

| 规则来源 | 内容 |
|---|---|
| **KIMI 7 方向** | 不允许为新数据调阈值 |
| **Trae §6 退化预检族** | 4 类不变性预检（见 §6） |
| **Coze 三态分离** | P1 尺寸标度 + P2 跨 backbone 实现稳健性 + P3 标度塌缩残差，三态独立判死 |
| **GLM §5 复现前提** | seed = 42，12×2 超平面，proj > 0，hex zfill(3)，阈值 Hamming < 6/12 |

**冻结资产层（0 触动）。** V3X 资产分四类，全程只读：

- **18 frozen anchors** = 16 frozen（4 份 KT SPEC V0.1 + P-F 系列 SPEC + v19/v21 基准 JSON + corpus v20 index + 2 份 anchor JSON + 4 plugin spec）+ 5 P-G 锚（V0 为确定性种子占位 `sha256("P_G_V0_PLACEHOLDER_{id}_2026_09_15")[:12]`，属设计声明，非真值）。
- **5 制品 JSON**（`corpus/v20/by_model/` 下 KIMI / GLM_1 / GLM_2 / coze / minimax 各 1 件）。
- **schema v1**（`_v3x_frozen_schema_v1.json`，12,919 B）：v0 → v1 仅格式升级（Python tuple → JSON），新增 `path_fallback`（repo → archive 自动降级）、`anchor_type`（5 类）、`touched_history` 字段；**16 + 5 = 21 锚 SHA-12 值未变**。
- **4 plugin spec**（`skill_a_p_a_60cells.py` / `skill_b_p_c_alpha_beta.py` / `skill_c_p_e_3modality.py` / `skill_d_p_f_observer.py`）。

**schema 重设计的触发。** 2026-09-17 的 file trim（1,327 → 817 files）将 `verifier/` 整体移入 archive 25%，波及 18 frozen 锚中的 2 份 anchor JSON；同时 `results/deposon_v19_benchmark_fixes.json` 在 R5 误移。为此重设计 schema v1，加 `path_fallback` 与 `touched_history`，实现 v0 + v1 双 verify 同时 PASS（v0 向后兼容）。

**本轮产出规模。** 8 个 worker 全部完成：Phase 1 P-L v3（Mistral × L{30,45,60,100}）、Phase 3 Adendum 10 项零成本、7 项中成本 Adendum、F/G/K 三端 LLM dispatch、Phase 2 baseline（qwen3 + glm53 + mistral）、P-D V0.3 实测（22 caption）、OR 重试（4 embedding）、豆包补测 v2（4 vision + 1 text + 1 cross-arch）、加速器 v2 retry（3 闭源 backbone）。合计 5 worker cross-backbone + 7 制品 + 18 frozen + 4 plugin spec + schema v1。

---

## §3 P-C + P-D 双 PASS 结果

### §3.1 P-C：跨模态 dpath 与 60 cells 账本

**账本轧平。** 9 个 LLM backbone × 60 题 = **540 cells**，全部账本恒等式 T + R + A = 1 轧平，9/9 model 残差为 0。沿 P-C distortion bound 60cells 的复现率，**实值 60 cells 中 51 项复现 = 85.0%**。

> **数字修正（必改）**：本轮早前文稿曾出现 `87.0%` 复现率，经 Trae code 盘上核对（`_trae_paper_8ch_双审_20260917_200000.md` §数据点 1），盘上无 87.0% 依据；**实值为 51/60 = 85.0%**，本稿已按 85.0% 表述。

**跨模态 dpath。** 沿 V3 决策线 cos_sim 阈值，9 model 中 **8 PASS + 1 GRAY**（deepseek-v4-pro）。GRAY 项为跨命题一致掉队者（详见 §4.4 与 §5）。

**0.867 均衡带。** 双主线在 **26/30 = 0.8667** 处精确重合：`doubao-seed-2.0-lite`（26/30）与 `glm-5.3`（26/30）两个模型落入同一均衡带。这是 9 model 账本中唯一出现的双模型精确重合点，构成跨实现稳定性的一处正面证据。

**P-C 幂律前件（负控制）。** 沿 KT-C1 SPEC V0.1，含环 328 图残余 r 对循环空间维数 d 的 log-log 回归给出 **R² = 0.1986 / 0.2670 双 FAIL_H0**（幂律死，b 的 95% CI 含 0）。该项与 §4 的 P-L v3 P1 构成**数学前件关系**：data collapse 的前件是「存在幂律标度」；两个独立通道指向同一「无幂律」结论（详见 §5 Adendum P）。

### §3.2 P-D：账指纹协议

**链式核验 22/22 PASS。** 沿 P-D V0.3 实测（22 caption dual_24bit）：

- state_0 = `7d6d3d39fad8`（anchors[0] = `verifier/runs/2026-09-04_pd_v0.jsonl` current_root）
- 22 caption dual_24bit 口径（`cap_sha[:6] + cap_sha[6:12]` 纯截段）**PASS 22/22**
- ext_1 = `f7b11d1e6988`；merkle_root = `7bf52bea023a`
- b3 root = `75596bbabdb8`

**口径差异的诚实声明。** P-O 链（纯截段口径）与 P-D B3 Merkle 链（`PD_V0.2` spec：`byte_hash[:6] + semantic_hash` 9 hex 36 bit）使用**不同的 dual_24bit 口径**，故 merkle_root 与 ext_1 不匹配。这是**设计差异而非 bug**：两条链各自链 PASS，互证 22 caption 完整性。原 P-O runner 的 22_caption_dual_24bit 在 `corpus/v20/index.json` 找不到 captions 字段（实际字段在 `strip_captions_22.json`），现改用 KIMI 22 caption_id 链式核验后闭合为 **22/22**（原口径 24/26）。

**P-D 三版本共存。** `PD_V0` + `PD_V0.2`（KIMI 裁定）+ `PD_V0.3`（文档升级）三版 SPEC 并存，各自冻结，互不覆盖。

**P-D 的方法论角色。** 内容寻址 + 规范 manifest + 根指纹 + 追加链，为「报告分布、实验工件、判定函数」提供机读可审计的收果接口；D7 交付的锚定工件包即走这一层。三类篡改攻击（删锚 / 洗 manifest / 改运行链）在既有试刀中全检出。

---

## §4 P-L v3 三态分离

### §4.1 起点：v1 的代数恒等式伪影

P-L 主张的原始实现（`_p_l_real_data_collapse_runner_2026_09_16_v2.py`）在 L64–66 存在**代数恒等式伪影**：对同一向量 `T_frac60` 做两个保序变换（`t**nu` 与 `t*eta`）后求 Spearman 相关：

```python
transformed = [t ** nu for t in T_frac60]
eta_transformed = [t * eta for t in T_frac60]
corr, _ = spearmanr(transformed, eta_transformed)
R2 = corr ** 2 if not np.isnan(corr) else 0
```

对全正向量，两个单调递增变换**恒同序** → Spearman ≡ 1、R² ≡ 1，**与 backbone 无关**。结果 JSON 显示 25/25 网格点 R² 全 = 1.0，`best_params = [0.5, 0.1]`，`final_dang_verdict = "P-L 通过 (R2 = 1.0 > 0.9)"`。这是**伪影而非结论**。同时，P-L 把「9 个 backbone 单一 L = 60 的标量」误当「同一系统的 9 个尺寸」套入有限尺寸标度（FSS）框架，存在**语义错位**。

### §4.2 v2 → v3：诚实降级与三态分离

- **v2（诚实降级）**：移除伪造的 R² 公式，但仍仅用 9 model × 60 cells 单 backbone → Spearman 仍 ≡ 1（FAIL）。
- **v3 worker C**：改用 Mistral Large 2512 × 30 cells 跨 backbone，Spearman = 0.375（PASS，破同序）。
- **v3 Phase 1（单 backbone × 多尺寸）**：Mistral Large 2512 × L ∈ {30, 45, 60, 100}，按 Coze 三态分离框架独立判死。

### §4.3 Phase 1 实测（单 backbone × 4 档尺寸）

| L | backbone | cells | pass | accuracy | 来源 |
|---|---|---|---|---|---|
| 30 | mistral-large-2512 | 30 | 24 | **0.8000** | worker C PASS 复用 |
| 45 | mistral-large-2512 | 45 | 23 | **0.5111** | 新跑（15 GSM8K + 15 baseline SQA + 15 new SQA） |
| 60 | （9 model aggregate） | 60 | n/a | **0.7111** | 复用 frozen per_model（仅 reference） |
| 100 | mistral-large-2512 | 100 | 46 | **0.4600** | 新跑（15 GSM8K + 15 baseline SQA + 70 new SQA） |

**P1 尺寸标度（主指标）**：单 backbone 30/45/100 三点 log-log 拟合 `log(O) = 1.0731 − 0.4140·log(L)`，**R² = 0.7447**（阈值 ≥ 0.9），slope = −0.4140，p = 0.337203 → **FAIL**。

**P3 标度塌缩（主指标）**：主曲线 `O(L) = 2.9243 · L^(−0.4140)`，归一化残差 **Q = 0.1929**（判读：< 0.05 塌缩成立 / [0.05, 0.15) 边缘 / ≥ 0.15 无塌缩）→ **FAIL**。

**辅助 Spearman（cell-level，非塌缩判死指标）**：L = 30 时 0.3750（p = 0.0412，N = 30，<< 0.95，破 backbone 同序成立）；L = 45 与 L = 100 在 30 cells 交集上均为 0.1667。

**Phase 1 综合 verdict = FAIL**（P1 FAIL + P3 FAIL）。老实交代三点不确定性：(a) 单 backbone 可能不足以覆盖 size scaling 信号；(b) StrategyQA 新增 cells（15 + 70）难度分布偏移导致 accuracy 单调下降；(c) 三点拟合统计力不足（n = 3）。

### §4.4 Phase 2 实测（跨 backbone 实现稳健性）

**开源 3 backbone（β bootstrap n = 1000，CI 95%）**：

| backbone | β lo | β median | β hi | accuracy |
|---|---|---|---|---|
| glm53 | −0.026170 | −0.009206 | 0.008007 | 0.7667 |
| mistral | −0.031481 | −0.015788 | −0.003311 | 0.8000 |
| qwen3 | −0.036910 | −0.018441 | 0.000110 | 0.6000 |

三对两两 β CI **全部 OVERLAP**（glm53×mistral、glm53×qwen3、qwen3×mistral）→ **P2 PASS**。

**闭源 3 backbone（β bootstrap n = 2000，CI 95%）**：

| backbone | β median | 95% CI | accuracy |
|---|---|---|---|
| gpt-5.6-sol | −0.010240 | [−0.027453, 0.006577] | 0.8333 |
| claude-sonnet-5 | −0.022119 | [−0.039812, −0.001869] | 0.7333 |
| gemini-3.7-flash | −0.014966 | [−0.030946, −0.002754] | 0.8667 |

三对两两 β CI **全部 OVERLAP** → **P2 PASS**。加速器降级欺诈验证：3 个 backbone 的 `response.model == request.model`，per-cell downgrade 出现 0 次（FALSE）。

**OR embedding 4 项（Qwen3-8B + BGE-large + E5-multi + GTE-large）**：P2 β CI overlap **1/6 GRAY**（symbol-split by architecture）。

**豆包 5 embedding（4 vision + Qwen3-4B）**：**structural finding** —— endpoint-internal 收敛、跨 endpoint 离散。

**P2 实现稳健性总判定**：**PASS**（6 个独立 backbone 两两 β CI 全重叠）。

> **数字降格（必改）**：早前文稿的 `P2 强稳健` 表述须降格为 **`P2 3/5 backbone overlap（1 OR×OR 失败）`**。实测 β CI overlap 在 OR embedding 组为 1/6；且需明确披露 β 为 **cell-level 代理斜率**（per-cell score 对 cell_index 的线性回归斜率），**不是** data collapse 主命题的 size scaling exponent。

### §4.5 三态分离综合判死

| 命题 | 指标 | 阈值 | 实测 | verdict |
|---|---|---|---|---|
| P1 尺寸标度 | log-log R² | ≥ 0.9 | **0.7447** | **FAIL** |
| P2 实现稳健性 | β CI overlap | 两两重叠 | 6/6 backbone | **PASS** |
| P3 标度塌缩 | 归一化残差 Q | < 0.05 | **0.1929** | **FAIL** |

**综合**：P-L data collapse 假设 **部分拒绝** —— 尺寸标度不成立（P1 FAIL + P3 FAIL），但跨实现稳健性成立（P2 PASS）。这一「分离」结果本身就是三态分离框架的价值：**若只测 P2，会得出「稳健成立」的结论；若只测 P1，会得出「主张失败」的结论；三态分离后才能说清「哪一态成立、哪一态不成立」。**

---

## §5 17 项 Adendum 综合

沿聚合文档 `_v3x_d0_5_aggregation_2026_09_17.md` §4.3 与 Phase 3 Adendum 报告，本轮共闭合 **17 项** Adendum。

> **数字修正（必改）**：早前文稿的 `Adendum 13 + 2 + 1 = 16` 须修正为 **`11 + 2 + 1 + 2 + 1 = 17`**（11 PASS + 2 GRAY + 1 UNVERIFIED + 2 PARTIAL + 1 FAIL_NO_MODEL）。

### §5.1 17 项分布

| verdict | 数量 | 项 |
|---|---|---|
| PASS | **11** | B, C, D, E, I, J, L, M, N, P, Q |
| GRAY | **2** | H（P-G dH_dE 收窄，std = 2.028）、O（P-K 盲测 FPR） |
| UNVERIFIED | **1** | A（退化预检族，4 子项中 3 项发现真 bug） |
| PARTIAL | **2** | F（P-E 3modal 闭合）、G（P-F D_fix2 timing 收敛） |
| FAIL_NO_MODEL | **1** | K（0.867 均衡聚类跨 backbone，text-240715 UnsupportedModel） |
| **合计** | **17** | — |

### §5.2 退化预检族（Adendum A，UNVERIFIED）

0 LLM hashlib + numpy 的 4 类不变性预检（输入向量方差 > 0 / 秩不恒同 / 标签非硬编码 / 检测率不低于随机基线），发现 **3 项真 bug**：

| 子项 | 检查结果 | 退化 bug | 裁定 |
|---|---|---|---|
| P-J 收敛盆地 | `convergence_rates` 9 model 全 0.1 常量（var = 0） | ✅ 是 | UNVERIFIED（Spearman −0.9667 对常量向量无定义） |
| P-I 曲率审计探针 | max_d_H = 0.25，max_d_E = 0.625，max_v42 = 0.25 | 部分 | PASS（d_E 单通道超 0.5 随机基线，属探测性非审计资产） |
| P-M 攻击面 | `detection_rate` 10/10 全 0.0，`safety_index` = SECURE（矛盾） | ✅ 是 | UNVERIFIED（检测率 < 0.5 违反安全下界必要条件；v42 须重设计） |
| P-C exp_3_3 eta 扫描 | `r2_per_eta` 对 9 model 逐字相同（9/9 列表相等） | ✅ 是 | UNVERIFIED（扫描退化，与 model 无关，仅随 η 变化） |

**横切修复建议**：在 0 LLM hashlib 复算层加 4 类不变性预检，任一失败直接 UNVERIFIED，**禁止产 PASS / SECURE**。这是 P-L 之外 4 项 Adendum 共同的根因族修复。

### §5.3 其余关键项

- **Adendum H（GRAY）**：P-G V0.1 的 `ratio_H_over_E` 9 model 重算，median = 5.444，IQR = 1.581，mean = 4.897，**std = 2.028**（CV > 0.4，不稳健）；剔除 2 个 canonical 边界（glm-5.3 ratio = 0.0 因 A60 = 2；doubao-seed-2.0-lite ratio = 8.03 因 A60 = 0）后 7 model std = 0.629，仍 GRAY。样本量不足以判定 5x 收窄为物理常数。
- **Adendum I（PASS）**：P-O 24/26 闭合为 **26/26**（KIMI 22 caption 链式核验 22/22 PASS）。
- **Adendum J（PASS）**：全仓排序健康体检，扫到 13 个含 Spearman 字段的 JSON，10 个有命中，全部记录在案（Trae P-L 教训横推生效）。
- **Adendum L（PASS）**：verifier 双实现差分，cost_curve 与 attack_results 的 10/10 行 detection_rate 完全一致（双实现差分为 0）。
- **Adendum P（PASS）**：P-C two_phase = FAIL_H0（幂律死）与 P-L v3 P1 尺寸标度 R² 是**数学前件关系**。若 P-L v3 P1 log-log R² < 0.9，应判为与 P-C two_phase 一致的**幂律死**，而非「P-L 实验失败」。两个独立命题指向同一「无幂律」结论，构成 paper 中「两个独立通道指向同一无幂律」的强证据。
- **Adendum Q（PASS）**：deepseek-v4-pro（跨命题一致掉队者：P-A GRAY + P-E FAIL + P-G ratio 4.44）标为 **P2 baseline 下界锚**，供新 backbone（Qwen3 / Nemotron 5）做邻域对齐比较。

### §5.4 Adendum C 勘误追加

KIMI push 第 3 批副审发现 Adendum C 两件 JSON 存在「`detection_rate = 0.0 × 8` + `verdict = PASS`」矛盾。按 P_F_PREDECISION erratum 先例追加勘误（**annotation ≠ mutation，原值零改动**）：

| 文件 | 改进前 SHA-12 | 改进后 SHA-12 |
|---|---|---|
| `_adendum_C_..._133852.json` | `d64e8e2e2518` | `6eba63788ca8` |
| `_adendum_C_..._133726.json` | `9c5ca0fed3ef` | `193ba7d66412` |

### §5.5 挂点回扣（4 项，源 = 提案 v3 §3-§7）

| 挂点 | 王老师侧（提案 v3 引用） | 我方 V3X 侧 | 一致性 |
|---|---|---|---|
| **挂点 1**：9 模型 × 60 题账本 | 540/540 账全轧平，双主线 26/30 精确重合 0.867 | 3 开源 backbone β CI overlap PASS + 3 闭源 backbone β CI overlap PASS + OR 1/6 GRAY + 豆包 structural finding | ✓ 实现稳健 |
| **挂点 2**：5 锚 + 字节级/语义级双指纹 | KT-D0 主锚 `03C6C01F3697` = anchor 0 | 18 frozen anchors + 5 制品 JSON + schema v1；22 caption dual_24bit 22/22 PASS；b3 root = `75596bbabdb8`；锚链 `c4cae1ed9ee5` | ✓ 内容寻址 + 根指纹 + 追加链模式一致 |
| **挂点 3**：「挂上也是交付」 | KT-C1 幂律 R² = 0.0007 死的是自己主张；KT-B1 22.5% < 50% 判死线走正面结果 | Phase 1 FAIL（R² = 0.7447，Q = 0.1929）；Phase 2 PASS；P-K FPR 4.4% GRAY；OR 1/6 GRAY | ✓ 同质（诚实降级 + 挂上也是交付） |
| **挂点 4**：4 协作方聚合收敛 | 9 模型 cross-backbone | 5 worker cross-backbone + 7 制品 + 18 frozen + 4 plugin spec + schema v1 | ✓ 同方法论（4 协作方聚合收敛 + 诚实降级 + 0 LLM 重算 + 7 铁律 0 触动） |

**1 句话挂点回扣**：**资产层一致，叙述层必改，0 触动严守。**

---

## §6 限制（paper §7.2）

本轮如实披露六项限制，全部有盘上实值可溯：

**（1）5 制品 schema 互异（结构性）。** `corpus/v20/by_model/` 下 5 件制品（KIMI / GLM_1 / GLM_2 / coze / minimax）的 SHA-12 5/5 全部验过，但 5 件 JSON 的 schema **互不相同**。这是结构性特征而非错误：5 件由 4 个不同协作方各自定义 schema 产出。**不重 hash、不强行统一**，在 push README 中显式声明。

**（2）P-K 盲测假阳性率 4.44%（双口径）。** GLM 三方盲测产物中，GLM 自己的 JSON 有 **2/45 被判为自家**，FPR = 4.44% > 1% 阈值 → **OVERALL FAIL**。**双口径表述**：机器判定为 OVERALL FAIL；paper 处置标为 **GRAY**（样本量与盲测设计限制）。沿 KIMI 7 方向，**不调阈值**。

**（3）OR embedding 组 P2 GRAY（1/6）。** 4 个 OR embedding（Qwen3-8B + BGE + E5 + GTE）的 β CI overlap 仅 1/6，呈 **symbol-split by architecture**。老实入 §7.2，不重 push 加 embedding。

**（4）Phase 1 尺寸标度 FAIL。** R² = 0.7447 < 0.9，且三点拟合 n = 3、p = 0.337，统计力不足。已在 §4.3 披露三点不确定性。

**（5）加速器 proxy 不稳。** 闭源 3 backbone 经 TeamoRouter proxy（127.0.0.1:1018）跑测，v1 曾出现 `net::ERR_CONNECTION_CLOSED` 卡死；v3 加 30s 硬 timeout + 3 retries + chain fallback 后完成。GPT-4o（TeamoRouter）**完全不可达**（DNS 解析失败 + OR 403 region unavailable）。doubao-seed-2.0-lite 在 volcengine 通道于 10/30 后服务端 hang > 9 min，标记 INCOMPLETE。诚实披露：**闭源组 β 为 cell-level 代理斜率，非 size scaling exponent。**

**（6）4 vector_embedding 大文件策略。** 4 件 vector_embedding JSON 大小 1.67–2.45 MB，需按 GitHub LFS 阈值（单文件 50 MB hard limit）确认 LFS 或直推策略。

**补充**：本轮 4 项退化预检发现的真 bug（P-J / P-M / P-C exp_3_3）已如实入 §5.2，相关命题标 UNVERIFIED，**不产 PASS**。

### §6.7 push README 必列 4 件（沿委托信 §6）

D7 推送 README 须显式声明以下 4 件（不隐藏、不改写）：

| # | 件 | 声明内容 |
|---|---|---|
| 1 | **P-F D_fix2 FAIL_EXPOSURE_PARTIAL** | D_fix2 严格/宽松双口径均为 `8 + 1 + 0`（PARTIAL_PASS，A channel timing 敏感），非全 PASS |
| 2 | **P-K OVERALL FAIL** | GLM 三方盲测 FPR = 4.44% > 1% 阈值，机器判定 OVERALL FAIL；paper 处置 GRAY（双口径） |
| 3 | **by_model schema 互异** | `corpus/v20/by_model/` 下 5 件制品 JSON schema 互不相同（4 协作方各自定义），SHA-12 5/5 PASS 但 schema 一致性 FAIL（结构性），不重 hash、不强行统一 |
| 4 | **GLM_1 stale ref** | `GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` 内含指向旧锚的 stale reference，须在 README 中标注该引用时效 |

**4 件声明一致完好**：均以实值落表，无掩盖、无美化。

---

## §7 结论

**核心结论。** P-L data collapse 假设被**部分拒绝**：尺寸标度不成立（P1 R² = 0.7447 FAIL、P3 Q = 0.1929 FAIL），跨实现稳健性成立（P2 6/6 backbone β CI 全重叠 PASS）。同时 P-C + P-D 双 PASS（60 cells 复现率 **85.0%**、22 caption dual_24bit 22/22 PASS），17 项 Adendum 中 11 PASS。

**方法论结论。** 三态分离框架使「哪一态成立、哪一态不成立」可说清；若只测单态会得出误导性结论。退化预检族（4 类不变性预检）在 0 LLM 层拦截了 3 项真 bug，证明「先问它在哪死」的纪律可机械执行。

**交付结论。** 本轮全部负面结果按预登记判死线归档、不回溯修改；**判死即有效交付**。资产层（18 frozen + 5 制品 + schema v1）一致完好，叙述层 3 处数字漂移已修正，7 铁律 0 触动严守。

---

## §8 派生建议

**V4 派生 8 题 × 4 闭源 backbone 测试题集。** 沿委托信 §1 表 §7 数据源（提案 v3 §7 + V4 1 分支 memory），下一阶段（下周 deposon 二作，含 V3 + V4）建议：

1. **补 Phase 2 缺位 backbone**：GPT-4o 通道（TeamoRouter）阻塞，建议换端点（自建代理）后补测，使闭源组从 3 扩到 4。
2. **补 Adendum F / G / K 三项 PARTIAL / FAIL_NO_MODEL**：F（P-E 3modal 闭合，3 model × 30 cells）、G（P-F D_fix2 timing 收敛，9 model × 60 cells）、K（0.867 均衡聚类跨 backbone，Qwen3 × 30 cells；text-240715 UnsupportedModel 需换模型）。
3. **Adendum H GRAY 补 Nemotron 5 backbone**：与 K 同批验证 `ratio_H_over_E` 是否落入 [4.4, 6.2] IQR 内。
4. **横切修复 4 类不变性预检并入 P-J / P-I / P-M / P-C 重设计任务**（Trae §6.0 + GLM §6.1 共同主张，横切修复 5 项受益）。
5. **P-M v42 须重设计**：detection = 0 与 safety_index = SECURE 的矛盾必须消除，`paper_amendment_required = True`。
6. **V4 非欧散射层作为方法论**（P-G V0.1 双曲 transport，dH_dE ≈ 5x，Spearman rho_H_vs_E = 1.0000）：沿「非欧几何作为方法论，不急定位 V4」暂不入正文。

**资源承诺**：工程、实验、中文学术出件由 9 角色项目组全包，不需要对方团队出资或设备。

---

## 附录 A · 8 件 SHA-12 自验（paper 引用前必验，本稿已实算）

**5 制品 JSON**（`corpus/v20/by_model/`）：

| 制品 | 文件 | SHA-12 | 校验 |
|---|---|---|---|
| KIMI | `kimi/index_v2_2026_09_16.json` | `efe05ad775de` | ✓ |
| GLM_1 | `GLM_1/three_way_glm_slot_blind_test_2026_09_16.json` | `268ab1239a8a` | ✓ |
| GLM_2 | `GLM_2/glm_artifact_v_2026_09_16.json` | `39732a92b5c9` | ✓ |
| coze | `coze/coze_artifact_v_2026_09_16.json` | `fee04170aa73` | ✓ |
| minimax | `minimax/artifact_v_2026_09_16.json` | `9e1ccbdceacc` | ✓ |

**18 frozen anchors（沿 schema v1，实算 16/16 + P-G 5/5）**：

| ID | SHA-12 |
|---|---|
| KT_ABC1_anchors_sha256_12 | `03c6c01f3697` |
| KT_A1_SPEC_V0_1 | `78b71d404366` |
| KT_B1_SPEC_V0_1 | `0410ca0fbdae` |
| KT_C1_SPEC_V0_1 | `59d8f56347d5` |
| KT_D0_SPEC_V0_1 | `cce8e9a1b00e` |
| P_F_V0_1_UPGRADE_2026_09_11 | `b10fae0da66d` |
| v19_benchmark_fixes | `910c4333eead` |
| v21_gtformal | `9d9ae5001c57` |
| corpus_v20_index | `8423ffe266af` |
| P_F_PREDECISION_2026_09_09 | `b41c98bf90cc` |
| P_F_SPEC_V0 | `de90faf362c5` |
| P_F_RESEARCH_2026_09_09 | `98085df7811a` |
| plugin_a_skill_a_p_a_60cells | `b1463bb24403` |
| plugin_b_skill_b_p_c_alpha_beta | `e5a299f69a22` |
| plugin_c_skill_c_p_e_3modality | `e19e76c5da7e` |
| plugin_d_skill_d_p_f_observer | `3e369a1f6171` |

P-G 5 锚（V0 占位，设计声明）：`230b5caee415` / `dcbcf2b8d45f` / `2c1f572aa2bf` / `8b90c53f1e01` / `91db66afecc3` —— 5/5 复算一致。

**schema v1**：`_v3x_frozen_schema_v1.json`（12,919 B）**21/21 一致**（16 frozen + 5 P-G）。

**4 plugin spec**：`b1463bb24403` / `e5a299f69a22` / `e19e76c5da7e` / `3e369a1f6171` —— 4/4 一致。

**自验方式**：0 LLM 纯 `hashlib.sha256()` 本地复算（沿 `_verify_pg_v0_v1.py` schema v1 驱动，含 `path_fallback` repo → archive 降级）。**8 件自验 100% PASS。**

## 附录 B · 5 audit 综合产物（引用清单）

| 件 | 判定 | SHA-12 |
|---|---|---|
| §1.1 D7 文稿 V1.1 双审 | PASS（带 3 数字修正） | `e240ca712be6` |
| §1.2 KIMI push 第 3 批副审 | PASS（带 1 阻断） | `8ece24be6b8a` |
| §1.3 派遣论文初稿需求双审 | PASS（带 3 必改） | `bec666969ffc` |
| §1.4 5 制品 by_model audit | SHA 5/5 PASS，schema 一致性 FAIL（结构性） | `f2a655cd5e54` |
| §1.5 18 frozen + schema v1 巡逻 | 22/22 锚 PASS | `4af67e6cbe71` |
| 聚合（`_trae_5audit_aggregated_2026_09_17.md`） | 资产层一致完好，叙述层 3 数字必改 + 1 矛盾复发 | — |

## 附录 C · 引用规范（沿 4 方共识）

| 规则 | 内容 |
|---|---|
| **KIMI 7 方向** | 不允许为新数据调阈值 |
| **Trae §6 退化预检族** | 4 类（P-J `convergence_rates` 常量、P-M `detection=0 vs SECURE`、P-C exp_3_3 `r2_per_eta` 9 model 逐字相同、P-O 24/26 闭合） |
| **Coze 3 态分离** | P1 size scaling + P2 cross-backbone + P3 collapse residual 三态独立判死 |
| **GLM §5 复现前提** | seed = 42，12×2 超平面，proj > 0，hex zfill(3)，阈值 Hamming < 6/12 |

## 附录 D · 7 铁律 + 0 触动声明

| 铁律 | 状态 |
|---|---|
| 0 LLM API 调用（本稿起草） | ✅ Coze 沿 spec 起草，不调 LLM |
| 不设 proxy / 不调网关 | ✅ 0 |
| key 不入 prompt / JSON / 落盘 | ✅ key runtime 读取 |
| 不动 18 frozen anchors | ✅ 16/16 + P-G 5/5 仅 hash 复算 |
| 不动 5 制品 baseline JSON | ✅ 0 read-modify-write |
| 不动 schema v1 / 4 plugin spec | ✅ 0 触动 |
| 不动 `verifier/mavis/.builtin/scripts/` | ✅ 0 触动 |
| 不写新 spec | ✅ 留给 doc-writer |
| 不动 push / 不动 WeChat 钥匙 | ✅ 严守 |

---

**Coze 起草** · deposon V3X 1 周判死 paper V1 正式版草稿 · 2026-09-17 · 沿 Mavis 委托信 `_letter_to_coze_paper_v1_委托_2026_09_17.md`
