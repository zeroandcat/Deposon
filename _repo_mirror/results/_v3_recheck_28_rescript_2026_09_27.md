# V3-R 补审改判件 #28 · P-M attack surface cost（rescript）

> **性质**：V3 假象类补审改判件（9 条系列之第 28 条）；**V3 原报告 byte 0 触动**，本件与原标注**并列**登记
> **依据**：`results/_v3_recheck_prereg_v1_2026_09_27.md`（实测 SHA-12 `88052d7db895`，37,346 B）§1.2 #28 / §2.2 K-V3R-28 / §2.4 TH-V3R-28 / §2.3 改判规则表 / §4 改判登记规则
> **配套三件套**：executor `results/_v3_recheck_28_executor_2026_09_27.py` ｜ result `results/_v3_recheck_28_result_2026_09_27.json` ｜ 本 rescript
> **勘误链位**：E-41.x 系（沿既有 E-1…E-16 链追加，0 覆盖原条目）
> **PI 复核栏**：待 PI 签字生效即锁

---

## 1. 原 V3 标注（沿 Trae v3 回函 §1.2 #28 字面 + P-M JSON 字面）

| 项 | 字面 |
|---|---|
| 对象 | P-M 攻击面成本下界（attack surface cost） |
| 原结论 | **UNVERIFIED** |
| 死因（预登记 §1.2 #28 字面） | 10 档 budget（8…80）`detection_rate ≡ 0.0`（全低于随机猜测 0.5）→ 判据退化 |
| 类型 | **假证伪**（Trae 回函 §1.2 #28） |
| 盘上实测复核 | 10/10 档 `detection_rate == 0.0`（n_distinct = 1，std = 0）、`detected_count == 0`、`missed_count == 8`；`safety_budget_lower_bound = 80`；`random_guess_rate = 0.5`；`v42_safety_index = "SECURE"` |

**根因（本条已定位到具体机制，比预登记「判据退化」更细）**：原 `detection_rate ≡ 0.0` **不是检测能力缺失，而是计数语义反转**。盘上证据 `results/deposon_v42_v2_miss_rate_curve_2026_09_16.json` §`counting_inversion_recount`（n_trials = 2000，seed = 20260916）明载：原口径 `is_valid=True → detected`（**记反**，verifier 拒绝反而算「漏检」），更正为「检出 = verifier 拒绝（is_valid=False）；漏检 = 篡改后仍通过」后，单 bit 翻转检出率 = **1.0**。本件 §3.4 用新数据**独立复现**了该反转（见下）。

## 2. 补审构造（沿 TH-V3R-28 派工单冻结形式，0 私设阈值）

```
算子（3 类型，TH-V3R-28 冻结）：one_bit_flip / two_bit_flip / contig_flip
budget 档（9 档，TH-V3R-28 冻结）：1 / 2 / 3 / 4 / 8 / 16 / 32 / 64 / 80
budget 语义：每文件翻转位点数（sites）；沿原 P-M 字面 unit_perturbation_count = attack_budget × 8 files
主检测器（真 detection 算法）：v42_v2 L1 内容寻址合约
        sha12(tampered) != manifest.sha12  ->  检出（verifier 拒绝）
        sha12(tampered) == manifest.sha12  ->  漏检（篡改后仍通过）
副检测器：逐字节汉明距离 > 0（最小非平凡阈值，0 可调参数）
ground truth：v42_v2 baseline manifest 8 件真 SHA-12（含 5 锚件 03c6c01f3697）
每格 trials = 50 × 8 文件 = 400 次篡改；篡改仅在内存副本，0 写盘
```

- **唯一实现自由度** = `contig_flip` 的连续翻转长度（主跑 = 8 bit）。附 run ∈ {4, 8, 16, 32} 敏感性网格。
- **0 新设阈值**：`safety_budget_lower_bound = 80` 沿 V3 既有字面（TH-V3R-28），本件只**重测**不新设。
- seed = 20260927，0 LLM，输入全只读。

## 3. 补审 result（K-V3R-0-C 双口径）

### 3.1 防退化门自证（K-V3R-0-A，跑前对盘上输入字段）

| 输入字段 | n | n_distinct | std | 门（>3 且 >0） |
|---|---|---|---|---|
| v42_v2 manifest 真 SHA-12（8 件，逐文件） | 8 | **8** | 72.227（按前 2 hex 估计） | **pass** |
| 受保护文件字节数（8 件，逐文件） | 8 | **8** | 130,850.37 | **pass** |
| budget 阶梯（TH-V3R-28 冻结 9 档） | 9 | **9** | 27.829 | **pass** |
| *（对照）P-M 原 `detection_rate`（10 档）* | *10* | *1* | *0.0* | *退化（预期）* |

`degenerate_alarm_hit = false` ｜ `manifest_vs_measured_all_match = true`（8/8 件盘上实测 SHA-12 与 manifest 逐字一致）｜ 5 锚件实测 `03c6c01f3697` 与 P-M JSON 记录**一致**

**豁免登记（如实）**：`5_anchor_json_sha12` 为**标识符**字段（单值锚 ID），n_distinct = 1 属设计预期；K-V3R-0-A 门槛按预登记 §1.2 辅助说明只对「真分布」输入字段生效，此处豁免并入表。

**输出为天花板序列的说明（如实）**：新构造 `detection_rate` 27 格全 = 1.0（n_distinct = 1，std = 0）——这是**检测器饱和**，不是判据退化；判据非退化性由上方 input_fields 承担。与原 10 档 ≡ 0.0 的对照见 §3.3。

### 3.2 真 attack 算子 × budget 档矩阵（每格 400 次篡改）

| 算子 \ budget | 1 | 2 | 3 | 4 | 8 | 16 | 32 | 64 | 80 |
|---|---|---|---|---|---|---|---|---|---|
| **one_bit_flip**（bit/文件 = budget） | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| **two_bit_flip**（bit/文件 = 2×budget） | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| **contig_flip**（连续 8 bit × budget） | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

- `detected_count` 每格 = 400，`missed_count` 每格 = **0**；`no_op_tamper_count` 每格 = **0**（无「篡改后字节不变」的无效操作）
- 副检测器（逐字节汉明）检出率同样每格 = 1.0000（两检测器一致）
- **敏感性**：contig run ∈ {4, 8, 16, 32} 四档 `detection_rate` 全部 = 1.0 → 判定不随实现自由度变化

### 3.3 双口径判定

| 口径 | verdict | 依据 |
|---|---|---|
| **新构造 verdict** | **PASS** | K-V3R-28：至少 1 档 `detection_rate > 0`（27/27 格 = 1.0）**且** `safety_budget_lower_bound` 重测 = **80 ≥ 80** |
| **沿原 V3 阈值字面 verdict** | **UNVERIFIED（判据退化）** | 原 10 档 `detection_rate` 全 = 0.0（n_distinct = 1，std = 0，低于随机猜测 0.5）；`safety_budget_lower_bound` 记 80，`v42_safety_index` 记 `SECURE` |
| **一致性** | **不一致** | 新构造 PASS vs 原口径 UNVERIFIED/判据退化，不同向 |
| `safety_budget_lower_bound` 重测 | **80**（0 漏检的最大 budget 档）= 原记 80，**下界成立** | — |

### 3.4 根因证伪实验（计数反转复现）

| 项 | 结果 |
|---|---|
| 方法 | 把原 P-M 的反转计数口径（`is_valid=True → detected`）套到**本次新构造的真实篡改数据**上重算 |
| 结果 | 27 格 `detection_rate` **全 = 0.0**（n_distinct = 1，std = 0）→ `reproduces_original_zero_pattern = true` |
| 结论 | 原 `detection_rate ≡ 0.0` **可由计数反转完整解释**，无需引入「检测能力不足」假设 —— 与盘上 v42_v2 复算记录（更正后检出率 = 1.0）**独立一致** |

### 3.5 K-V3R-28 触发状态

| 判据 | 状态 |
|---|---|
| 至少 1 档 `detection_rate > 0` | **触发**（27/27 格 = 1.0） |
| `safety_budget_lower_bound` 重测 ≥ 80 | **触发**（= 80） |
| `kill_line_pass` | **true**（存活） |
| `kill_line_hit`（触发 FAIL） | **false** |

## 4. 改判动作（沿预登记 §2.3 改判规则表 + §4）

| 项 | 结论 |
|---|---|
| 命中档位 | **§2.3 第 2 行：PASS + 不一致**（新构造 PASS + 原阈值 UNVERIFIED） |
| 改判动作 | **维持原 V3 标注（不动）** + **显式登记**新构造 verdict；归「不明」分支 |
| γ 标 | γ₁ = 原 `detection_rate ≡ 0.0` 的根因为**计数语义反转**（盘上 v42_v2 报告 + 本件 §3.4 双重证据），非检测能力缺失；γ₂ = 原判据覆盖面仅 5 文件、单值比对无定位能力（v42_v2 已扩至 8 文件 + 逐层定位），原 `UNVERIFIED` 标注在其自身口径下**不可直接引用为安全结论** |
| V3 原报告 | **byte 0 触动**（P-M JSON 与 v42_v2 报告均未写） |
| 是否翻案 | **否** —— 本件只改「结论-证据关系」的登记，不重裁命题存亡（沿预登记 §5.1） |
| 桶位 | 「V4 收尾整理」待拍板桶 |

## 5. 老实交代段

1. **输入链 SHA 口径不符（如实登记，不代为修订预登记）**：预登记 §0.2 记 #28 P-M JSON 实测 SHA-12 = `1F11ED31273D`，本 worker 按 `hashlib.sha256(bytes).hexdigest()[:12]` 实测 = **`fbcb60cf5102`**（字节数 5,266 与预登记**逐字一致**）。同口径下预登记 §0.2 表内 **12/12 件全部不符**，系统性差异指向哈希输入约定不同或转写前移，**非内容变更**。**内容侧已逐字复核**：预登记 §0.2 对 #28 的描述（10 档 budget、`detection_rate ≡ 0.0`、8–80）与盘上 JSON **逐字吻合**。未修改预登记任何 byte。
2. **原始执行器缺件（如实登记）**：`deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py`（v42_v2 报告 L30-45 / L82-87 引用）**在盘上不存在**，无法逐行复核其计数反转代码。本件的根因结论因此建立在**盘上 v42_v2 复算记录 + 本件独立复现实验**两条证据上，**不是**对原脚本的逐行审计。
3. **TH-V3R-28 算子集的落地形式**：预登记 §2.4 把「真 attack 算子三类型」标为**占位待 PI 拍板**；PI 2026-09-27 派工单冻结了算子**类型名**（1-bit / 2-bit / contig flip）与 budget 档，但未冻结「contig 连续长度」与「budget = sites 语义」；本件的落地选择已逐项登记并附 4 档敏感性网格，**留 PI 复核**。
4. **E-15 锚链 fallback 状态**：预登记 §1.2 #28 记「5 锚 JSON 真值 `03c6c01f3697`，但 E-15 锚链断裂需 fallback §0.1」。本 worker 实测 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` **在盘且 SHA-12 = `03c6c01f3697`**，与 P-M JSON 与 60cells JSON 两处记录**三向一致**；本条**未触发 fallback**。（`deposon-sub/` 与 `_archive_deposon_2026_09_17/` 两个 fallback 根目录**不在本仓**，故 E-15 相关的 #5 / #12 fallback 仍待处理。）
5. **未编造观测**：全部 10,800 次篡改均为内存内真实位翻转 + 真实 SHA-256 复算；0 外部文献号新增；0 新设阈值。
6. **succeeded ≠ 跑完**：本件以 result JSON 落盘 + hashlib SHA-12 复算为准（见最终汇报核验值）。

---

**PI 复核栏**：☐ 通过（按 §2.3 第 2 行登记生效）　☐ 打回（退回重跑 / 需补构造）　签字：__________　日期：__________

出证｜Mavis 团队 worker 出件｜2026-09-27
