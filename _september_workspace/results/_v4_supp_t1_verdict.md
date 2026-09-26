# V4 补测 T1 探针判定收口 · L2/L14 温度敏感性 + mimo/teamo 端点补测（2026-09-24）

> **本件性质**：verdict-keeper 判定收口（裁因专职）；T1 产物链末件（沿 `_v4_supp_t1_executor.py` + `_v4_supp_t1_result.json`）
>
> **本件定位（沿 T1 prereg `802DECE2286A` §0 边界 + §1.3 探针限定 + §5 根因关联表）**：T1 = 稳健性辅助检验（sensitivity probe），**不翻 L2/L14 正式判定**；结论仅作稳健性注记入勘误链；除 K-T1-S1/S2 命中 + verdict-keeper 裁因 + verifier 签字，**不得据此改判** L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」既定结论一字不动
>
> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）；如实记录只是「机械诚实」，不合格

---

## §0 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | 自报 SHA-12 | 盘实测 SHA-12（前 12） | 字节 | 状态 |
|---|---|---|---|---|---|
| T1 result | `results/_v4_supp_t1_result.json` | `D6CB03A4657E` | `D6CB03A4657E` | 82,365 | ✓ |
| T1 executor | `results/_v4_supp_t1_executor.py` | `A7CAD9228B0B` | `A7CAD9228B0B` | 59,967 | ✓ |
| T1 prereg | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | `802DECE2286A` | 52,942 | ✓ |
| T1 activation | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936B630015` | `79936B630015` | 14,234 | ✓ |

> **0 触既有件自查**：本 verdict 件仅读上述 4 件；**未修改 executor.py / result.json / prereg / activation**（一字不动，沿 T1 prereg §4 边界 + 「派生 JSON 不合并」铁律）

---

## §1 核心裁因问题：字面 PASS（K-T1-S3 命中）是真稳健，还是构造失灵族假象？

### §1.1 字面结论（K-T1-S3 命中）

- **K-T1-S1（温度敏感性 flip 触发线）**：`any_hit: false`；mimo/L2 + mimo/L14 + teamo/L2 + teamo/L14 四个 (端点, 维度) 跨 {0.0, 0.3, 0.5} 三温度 cell J 中位**全 < 0.85**
- **K-T1-S2（端点敏感性 flip 触发线）**：`any_hit: false`；0.0/L2 + 0.0/L14 + 0.3/L2 + 0.3/L14 + 0.5/L2 + 0.5/L14 六个 (温度, 维度) 跨 {mimo, teamo} 两端点 cell J 中位**全 < 0.85**
- **K-T1-S3（稳健性确认线）**：`any_cell_flip_to_ge_threshold: false` → `hit: false` → **PASS（判定稳健，不入勘误链）**（沿 T1 §1.5.2 K-T1-S3 字面 + T1 §1.3 探针限定）
- **overall_verdict**：`t1_overall_verdict: "PASS (判定稳健)"`

### §1.2 执行棒自报关键证据（`D6CB03A4657E` §honesty_disclosures）

- **240 calls 全部跑完**（12 cells × 20 calls = 240；`n_records_total: 240` / `n_calls_ok: 227` / `n_calls_failed: 13`）
- **n_empty_responses = 112（49.3% of total calls）**：reasoning 模型 mimo-v2.6-pro（mimo 端点）+ deepseek-v4-flash（teamo 端点）几乎所有 reasoning tokens 消耗 max_tokens=100 预算，content 字段为空
- **empty-vs-empty 对占 total pairs = 233/323 = 72.1%**：12 cells 中 empty_vs_empty_pairs 是 nonempty_pairs 的 ~3 倍
- **cell_j_median_5teachers_nonempty 分布**：12 cells 中仅 cell 2 (L2/mimo/temp=0.3) nonempty 中位 = 0.5；其余 11 cells nonempty 中位 = 0.0

### §1.3 根因三分类（沿 E-27 §13 拍板 + T1 §5 根因关联表）

> **真证伪判别要件全满足才算真证伪**：
> ① kill-line 先于实验冻结 ✓（T1 prereg `802DECE2286A` §1.5 字面已锁）
> ② 构造非恒等/非退化 **✗**（reasoning 模型 + max_tokens=100 → 多数调用产出空 content，构造退化）
> ③ 素材面覆盖 claim 所需 **✗**（49.3% 空响应 + 72.1% empty-empty pairs → J=0.0 主要来自「双方都空」而非真判定）
> ④ 度量有分辨力 **✗**（Jaccard 在双方都空时返回 0.0 系代码字面，无法区分「判定一致」vs「双方都没产出」）

**→ K-T1-S3 字面命中（PASS）= 不构成真稳健（要件 ②③④ 失守）= 构造失灵族假象**：

- **真证伪要件全满足才算真证伪；要件 ②③④ 失守 → K-T1-S3 字面 PASS ≠ 真稳健**
- **归类 = 假证伪族（构造失灵）**：工具/构造（reasoning 模型 + max_tokens=100 预算失配）失灵致 J=0.0 不再是「教师稳定」信号而是「双方都没产出」信号
- **「双方都输出空」 ≠ 「判定一致」**（核心命题层面混淆禁止；沿诚实=不误导）

### §1.4 主读法 vs 替代读法（双读法并记，沿 K-N11-N2 字面）

#### 主读法：构造失灵族假象（dominant）

- **依据**：49.3% 空响应 + 72.1% empty-empty + reasoning 模型 + max_tokens=100 预算失配 = 构造退化致实验结论失效
- **判定**：K-T1-S3 字面 PASS = 假稳健（informational 价值有限；不可外推为 L2/L14 既判稳健）

#### 替代读法 1：非退化子口径 partial 稳健（inconclusive positive）

- **依据**：nonempty-only 子口径下，cell 2 (L2/mimo/temp=0.3) cell_j_median_5teachers_nonempty = 0.5 ≥ 0.85 半数 → 单一 cell nonempty 子样本方向翻转
- **判定**：单一 cell 翻转 ≠ 整体稳健；但也不能排除「nonempty 子样本下确有方向翻转」的弱信号
- **诚实声明**：样本量过薄（cell 2 nonempty pairs = 1 / total 30 = 3.3%），统计意义不足

#### 替代读法 2：qwen baseline 不重跑锁定（orthogonal）

- **依据**：T1 prereg §1.2 对照基准不重跑（沿 `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 既有数据），故 K-T1-S3 PASS 无法直接与 qwen baseline 做并置核证
- **判定**：T1 PASS 只能证「mimo/teamo × {0.0, 0.3, 0.5} 矩阵内方向一致」≠ 证「qwen t=0.7 baseline 方向稳健」

#### 双读法分歧处理

- **主读法（构造失灵族假象）采纳**为定调
- **替代读法 1** 仅作 informational 注记（不推翻主读法；不作为 L2/L14 复核候选）
- **替代读法 2** 入诚实交代（qwen baseline 不重跑锁定是 T1 设计本身约束）

---

## §2 kill-line 判定表（每行附根因列）

> **字面不动声明**：K-N11-3 字面沿 `0A9EE16267B5` §1 + L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 一字不动；K-T1-S1/S2/S3 沿 T1 §1.5.2 字面；判定布尔显式方向（`hit=True` 即触发）
>
> **nonempty-only 子口径并报**：T1 §1.4 非退化自证口径；nonempty 子样本下 J 中位单独计算（`cell_j_median_5teachers_nonempty`）

### §2.1 K-T1-S1（温度敏感性 flip 触发线）— 4 (端点, 维度) 组合 × 3 温度

| 端点 | 维度 | 温度 | cell_idx | cell_j_median_5teachers | cell_j_median_5teachers_nonempty | 字面 hit | nonempty hit | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|---|
| mimo | L2 | 0.0 | 0 | 0.0 | 0.0 | False | False | **构造失灵族假象**：reasoning 模型 mimo-v2.6-pro + max_tokens=100 → 21/30 pairs empty-empty（70%）；J=0.0 主要来自「双方都空」非真判定 |
| mimo | L2 | 0.3 | 2 | 0.0 | 0.5 | False | False | **构造失灵族假象**：29/30 pairs empty-empty（96.7%）；nonempty 子样本仅 1 pair → J_nonempty=0.5 样本量不足 |
| mimo | L2 | 0.5 | 4 | 0.0 | 0.0 | False | False | **构造失灵族假象**：27/30 pairs empty-empty（90%）；nonempty 子样本 3 pairs 全 J=0.0 |
| mimo | L14 | 0.0 | 6 | 0.0 | 0.0 | False | False | **构造失灵族假象**：16/27 pairs empty-empty（59.3%）；nonempty 子样本 11 pairs 多为 J=0.0，GLM_2 单 pair=1.0 噪声 |
| mimo | L14 | 0.3 | 8 | 0.0 | 0.0 | False | False | **构造失灵族假象**：22/30 pairs empty-empty（73.3%）；nonempty 子样本 8 pairs 多为 J=0.0 |
| mimo | L14 | 0.5 | 10 | 0.0 | 0.0 | False | False | **构造失灵族假象**：20/30 pairs empty-empty（66.7%）；nonempty 子样本 10 pairs 全 J=0.0 |
| teamo | L2 | 0.0 | 1 | 0.0 | 0.0 | False | False | **构造失灵族假象**：18/19 pairs empty-empty（94.7%）；nonempty 子样本仅 1 pair（kimi），样本量不足 |
| teamo | L2 | 0.3 | 3 | 0.0 | 0.0 | False | False | **构造失灵族假象**：23/24 pairs empty-empty（95.8%）；nonempty 子样本仅 1 pair（kimi） |
| teamo | L2 | 0.5 | 5 | 0.0 | 0.0 | False | False | **构造失灵族假象**：16/19 pairs empty-empty（84.2%）；nonempty 子样本 3 pairs 全 J=0.0 |
| teamo | L14 | 0.0 | 7 | 0.0 | 0.0 | False | False | **构造失灵族假象**：18/27 pairs empty-empty（66.7%）；nonempty 子样本 9 pairs 多为 J=0.0 |
| teamo | L14 | 0.3 | 9 | 0.0 | 0.0 | False | False | **构造失灵族假象**：11/27 pairs empty-empty（40.7%）；nonempty 子样本 16 pairs 多为 J=0.0，GLM_2 单 pair=1.0 噪声 |
| teamo | L14 | 0.5 | 11 | 0.0 | 0.0 | False | False | **构造失灵族假象**：12/30 pairs empty-empty（40%）；nonempty 子样本 18 pairs 全 J=0.0 |

**K-T1-S1 合计 `any_hit: false`（字面 hit；temperature 非翻转）**
**K-T1-S1 nonempty-only `any_hit_nonempty: false`（nonempty hit；仅 cell 2 单 pair 翻 0.5 < 0.85，未达触发线）**

### §2.2 K-T1-S2（端点敏感性 flip 触发线）— 6 (温度, 维度) 组合 × 2 端点

| 温度 | 维度 | 端点 | cell_idx | cell_j_median_5teachers | cell_j_median_5teachers_nonempty | 字面 hit | nonempty hit | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|---|
| 0.0 | L2 | mimo | 0 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 0） |
| 0.0 | L2 | teamo | 1 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 1） |
| 0.0 | L14 | mimo | 6 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 6） |
| 0.0 | L14 | teamo | 7 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 7） |
| 0.3 | L2 | mimo | 2 | 0.0 | 0.5 | False | False | **构造失灵族假象**（同 §2.1 cell 2；nonempty 单 pair 翻 0.5 不达触发线） |
| 0.3 | L2 | teamo | 3 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 3） |
| 0.3 | L14 | mimo | 8 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 8） |
| 0.3 | L14 | teamo | 9 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 9） |
| 0.5 | L2 | mimo | 4 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 4） |
| 0.5 | L2 | teamo | 5 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 5） |
| 0.5 | L14 | mimo | 10 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 10） |
| 0.5 | L14 | teamo | 11 | 0.0 | 0.0 | False | False | **构造失灵族假象**（同 §2.1 cell 11） |

**K-T1-S2 合计 `any_hit: false`（字面 hit；endpoint 非翻转）**
**K-T1-S2 nonempty-only `any_hit_nonempty: false`（nonempty hit；端点维度无 ≥ 0.85 cell）**

### §2.3 K-T1-S3（稳健性确认线）— 12 cells 总览

| 维度 | cell_idx | n_pairs_total_all | n_pairs_total_nonempty | empty_empty_ratio | 字面 cell_j_median | nonempty cell_j_median | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|
| L2 | 0 | 30 | 9 | 70.0% | 0.0 | 0.0 | **构造失灵族假象**（empty-empty 主导） |
| L2 | 1 | 19 | 1 | 94.7% | 0.0 | 0.0 | **构造失灵族假象**（empty-empty 极主导） |
| L2 | 2 | 30 | 1 | 96.7% | 0.0 | 0.5 | **构造失灵族假象 + informational**：empty-empty 96.7%；nonempty 单 pair 翻 0.5（样本量极薄，不构成 trigger） |
| L2 | 3 | 24 | 1 | 95.8% | 0.0 | 0.0 | **构造失灵族假象** |
| L2 | 4 | 30 | 3 | 90.0% | 0.0 | 0.0 | **构造失灵族假象** |
| L2 | 5 | 19 | 3 | 84.2% | 0.0 | 0.0 | **构造失灵族假象** |
| L14 | 6 | 27 | 11 | 59.3% | 0.0 | 0.0 | **构造失灵族假象**（empty-empty 较高，但 nonempty 11 pairs 相对多） |
| L14 | 7 | 27 | 9 | 66.7% | 0.0 | 0.0 | **构造失灵族假象** |
| L14 | 8 | 30 | 8 | 73.3% | 0.0 | 0.0 | **构造失灵族假象** |
| L14 | 9 | 27 | 16 | 40.7% | 0.0 | 0.0 | **构造失灵族假象**（empty-empty 最低但仍 40.7%；nonempty 16 pairs 中 GLM_1 j_med=0.1, GLM_2 单 pair=1.0） |
| L14 | 10 | 30 | 10 | 66.7% | 0.0 | 0.0 | **构造失灵族假象** |
| L14 | 11 | 30 | 18 | 40.0% | 0.0 | 0.0 | **构造失灵族假象**（nonempty 18 pairs 但全 J=0.0） |

**K-T1-S3 合计 `hit: false`（字面） / `hit_nonempty: false`（nonempty） → 字面 PASS（方向一致）**
**根因裁定：构造失灵族假象**（真证伪要件 ②③④ 失守）

### §2.4 K-N11-N1_T1relax（探针放宽 N_min）— 12 cells × 5 教师

> K-N11-N1_T1relax 字面沿 T1 §1.4 + §1.8 TH-T1-1 = 10 对/教师（探针放宽口径）
> 全 12 cells 全 5 教师 N_pairs ∈ {1, 3, 6}，**全 < 10**

| cell_idx | 维度 | 端点 | 温度 | kimi N | GLM_1 N | GLM_2 N | coze N | minimax N | 字面 hit | nonempty hit | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | mimo | 0.0 | 6 | 6 | 6 | 6 | 6 | False | False | **构造失灵族假象**：N < 10 致 K-N11-N1_T1relax FAIL → 探针放宽口径下仍不达最小样本；统计量不足，命题不可证伪 |
| 1 | L2 | teamo | 0.0 | 1 | 3 | 3 | 6 | 6 | False | False | **构造失灵族假象**：N ∈ {1,3} 致命题不可证伪 |
| 2 | L2 | mimo | 0.3 | 6 | 6 | 6 | 6 | 6 | False | False | **构造失灵族假象**：N=6 < 10 |
| 3 | L2 | teamo | 0.3 | 6 | 3 | 3 | 6 | 6 | False | False | **构造失灵族假象**：N ∈ {3,6} |
| 4 | L2 | mimo | 0.5 | 6 | 6 | 6 | 6 | 6 | False | False | **构造失灵族假象**：N=6 |
| 5 | L2 | teamo | 0.5 | 6 | 1 | 6 | 3 | 3 | False | False | **构造失灵族假象**：N ∈ {1,3,6} |
| 6 | L14 | mimo | 0.0 | 6 | 6 | 6 | 6 | 3 | False | False | **构造失灵族假象**：minimax N=3 |
| 7 | L14 | teamo | 0.0 | 3 | 6 | 6 | 6 | 6 | False | False | **构造失灵族假象**：kimi N=3 |
| 8 | L14 | mimo | 0.3 | 6 | 6 | 6 | 6 | 6 | False | False | **构造失灵族假象**：N=6 |
| 9 | L14 | teamo | 0.3 | 6 | 6 | 3 | 6 | 6 | False | False | **构造失灵族假象**：GLM_2 N=3 |
| 10 | L14 | mimo | 0.5 | 6 | 6 | 6 | 6 | 6 | False | False | **构造失灵族假象**：N=6 |
| 11 | L14 | teamo | 0.5 | 6 | 6 | 6 | 6 | 6 | False | False | **构造失灵族假象**：N=6 |

**K-N11-N1_T1relax 合计 `any_fail: true` / `pass: false`（12 cells 全 FAIL）**
**根因裁定：构造失灵族假象（N 不足致命题不可证伪）**

### §2.5 kill-line 判定汇总

| K-* | 字面方向 | 字面 hit | nonempty hit | 根因类型 |
|---|---|---|---|---|
| K-N11-3（12 cells） | 任一教师 J 中位 < 0.85 → hit=True → FAIL | True（全部） | True（全部，但 nonempty 子样本极薄） | **构造失灵族假象**（empty-empty 主导 J=0.0） |
| K-T1-S1 | 任一温度 cell J ≥ 0.85 → hit=True → 稳健性存疑注记 | False | False | **构造失灵族假象**（empty-empty 致整矩阵方向 J<0.85） |
| K-T1-S2 | 任一端点 cell J ≥ 0.85 → hit=True → 稳健性存疑注记 | False | False | **构造失灵族假象**（同 K-T1-S1） |
| K-T1-S3 | 全 12 cells J < 0.85 → hit=False → 判定稳健 | **False（字面 PASS）** | **False** | **构造失灵族假象**（PASS ≠ 真稳健；要件 ②③④ 失守） |
| K-N11-N1_T1relax | N < 10 → pass=False → FAIL | True（12 cells 全 FAIL） | True | **构造失灵族假象**（N 不足致命题不可证伪） |

**根因三分类计数**：
- **真证伪（命题被证伪）**：0 件
- **假证伪族（工具/构造失灵）**：5/5 K 件全归此类
- **命题不明（构造不可逃）**：0 件（已归入假证伪族，因 T1 设计本身是辅助检验探针）

---

## §3 T1 定位硬约束（不翻 L2/L14 正式判定）

### §3.1 硬约束复述（沿 T1 prereg §0 + §1.3 + §5 字面）

1. **K-T1-S3 字面 PASS ≠ L2/L14 判定稳健**：本件 §1.3 已论证 K-T1-S3 字面 PASS 是构造失灵族假象，**不可被引用为「L2/L14 判定稳健」的证据**
2. **K-T1-S1/S2 字面 hit=False 不构成 L2/L14 PASS**：12 cells 方向一致源于 empty-empty 主导，非真判定一致
3. **L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」一字不动**
4. **T1 探针非设计意图为改判**：T1 = 稳健性辅助检验（sensitivity probe），结论仅作稳健性注记入勘误链

### §3.2 边界声明（沿 T1 §1.3 + §1.11 + §4 字面）

- **外推边界 = 端点/温度维度边界**：T1 仅在 mimo/teamo × {0.0, 0.3, 0.5} 矩阵内探针；qwen t=0.7 baseline（沿 `_v4_track2_multimodel_verdict_2026_09_23.md`）**不重跑**，故 T1 字面 PASS 不可外推为「qwen baseline 方向稳健」
- **数据规模边界**：T1 N_min = 10/教师探针放宽（与 L2/L14 既定 N=20/教师 两层并存）；实测 N ∈ {1, 3, 6} 致 K-N11-N1_T1relax 全 FAIL
- **不留假 pass**：T1 探针不命中 ≠ L2/L14 既判 PASS
- **不留假证伪**：T1 探针命中 ≠ L2/L14 既判 FAIL
- **判定须另走流程**：除 K-T1-S1/S2 命中 + verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论

### §3.3 T1 探针结论对 L2/L14 既判的影响（沿 T1 §5 根因关联表）

| T1 探针结果 | L2/L14 既判影响 | 根因列 |
|---|---|---|
| K-T1-S3 字面 PASS | **0 影响**（L2/L14 既判不动） | **本件裁定**：构造失灵族假象，PASS ≠ 真稳健；不作 L2/L14 既判 PASS 新证据；仅作「构造失灵注记」入勘误链 |
| K-T1-S1/S2 字面 hit=False | **0 影响**（L2/L14 既判不动） | empty-empty 主导致整矩阵 J<0.85；非真判定一致 |
| K-T1-S1/S2 命中（实际未命中） | **可能**触发 L2/L14 既判复核 | 不翻既判 = 默认；触发复核 = 须走完整流程（本棒未触发） |
| partial completion（实际未发生） | 0 影响 | 12 cells 全跑完（240 calls） |

---

## §4 后续建议（仅写建议，不执行）

> **诚实声明**：本节为「T1 当前 informational 价值有限」的复评路径建议；**本 verdict 件不执行任何重跑/补跑/调阈值**；建议仅作 PI 派工参考，**须另起 T1.5 / T2 立线棒走 prereg 修订流程**

### §4.1 复评路径建议（按优先级）

1. **【最高优先】改用非 reasoning 模型 + 提高 max_tokens**（不调阈值，仅调构造）：
   - 当前 mimo-v2.6-pro（reasoning 模型）+ deepseek-v4-flash（reasoning 模型）+ max_tokens=100 → 49.3% 空响应
   - 建议路径：换 qwen3.7-max（non-reasoning；沿 `_v4_track2_multimodel_verdict_2026_09_23.md` 既有 baseline 端点 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1`）+ max_tokens ≥ 500（容纳完整输出；**0 触 L2/L14 verdict 字面**）
   - 预期：消除 empty-empty 主导；J=0.0 不再源自「双方都空」；Jaccard 度量恢复分辨力

2. **【次优先】走 prereg 修订棒调整 max_tokens 字面条款**：
   - 现状：T1 prereg §1.4「L14 max_tokens = 100 沿 L14 verdict §2 字面」+ executor.py `MAX_TOKENS = 100`（沿 L14 verdict §2 字面锚）
   - 修订路径：另起 T1.5 prereg 追加件（沿 L9/L10/T1 追加件先例）→ 调整 T1 探针专属 max_tokens（如 500）→ 0 触 L14 verdict §2 字面（仅 T1 探针放宽）
   - 须 PI 复核生效（沿 T1 §0.6 锁先例）

3. **【辅助】重跑 nonempty 子样本下 Jaccard 度量**：
   - 现状：nonempty 子样本下多数 cells J_nonempty = 0.0；cell 2 (L2/mimo/temp=0.3) J_nonempty = 0.5 但样本量 1
   - 建议：仅在 nonempty 子样本上做统计推断（per-cell N ≥ 10 后再触发 K-N11-N1_T1relax）

4. **【最低优先】降 temperature 范围重跑**（信息量最小）：
   - 当前 temp ∈ {0.0, 0.3, 0.5}；若仅消除 reasoning 干扰已能恢复方向 → 不必降 temp
   - 若改用非 reasoning 模型后仍 J 翻转 → 再降 temp（如 temp ∈ {0.0, 0.2}）

### §4.2 禁止项（沿 7+9 铁律 + T1 §0 边界）

- **0 调阈值**：K_N11_3_THRESHOLD = 0.85 / K_N11_1_DIFF = 0.05 / K_N11_2_DELTA = 0.05 / TH17_N_TARGET = 20 字面不动
- **0 触既有件**：L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` + 22 caption `6A2656878745` + Track 2 件 `B65619A07B10` / `C846F7FC79EE` 一字不动
- **0 合并派生 JSON**：复评产物须用 `_v4_supp_t1_*` prefix 分列；不得与 L2/L14 verdict 合并字面源
- **0 自跑 / 0 自起草**：本 verdict 件不发起任何 worker 接力棒 / doc-writer 草稿；建议留 PI 派工

### §4.3 信息量边界声明

- T1 当前 informational 价值 = 揭示 reasoning 模型 + max_tokens=100 预算失配是构造失灵主因
- T1 当前不能提供 = 「qwen t=0.7 baseline 方向稳健 / 不稳健」的独立证据（baseline 不重跑）
- T1 当前不能提供 = 「mimo / teamo 端点下真判定一致 / 不一致」的证据（empty-empty 主导）
- T1 当前不能提供 = 「温度敏感性成立 / 不成立」的证据（构造退化致温度维度的差异被噪声淹没）

---

## §5 老实交代（failures & limitations）

### §5.1 产物核验

- **本 verdict 件诞生**：路径 `results/_v4_supp_t1_verdict.md`；诞生即算 SHA-12（见 RESULT 报告段）+ 字节
- **0 既有件触动自查**：
  - `_v4_supp_t1_executor.py` `A7CAD9228B0B` ✓ 未触动（仅读）
  - `_v4_supp_t1_result.json` `D6CB03A4657E` ✓ 未触动（仅读）
  - `_v4_supp_prereg_v02_add_T1_2026_09_24.md` `802DECE2286A` ✓ 未触动（仅读）
  - `_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` `79936B630015` ✓ 未触动（仅读）
  - L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` ✓ 未触动（仅读）
  - v0.2 预登记 `D85488A64D89` + activation `AD42992DC75D` ✓ 未触动
  - L9 追加件 `23879B6CD1CC` + activation `5C579F28634E` ✓ 未触动
  - L10 追加件 `F6FE005EE3C7` + activation `16E89657DAAA` ✓ 未触动（本棒未引用 L10 字面源）
  - Track 2 件 `B65619A07B10` / `C846F7FC79EE` ✓ 未触动
  - 22 caption `6A2656878745` ✓ 未触动
  - **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）
- **key 形态自扫**：本 verdict 件正文 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**

### §5.2 limitations（沿 T1 §8 + L14 verdict §11 同口径）

- **skill 诚实交代**：派工单要求 skill `scientific-research-workflows:peer-review`（plugin @scientific-research-workflows, sha256-tree-v1 = `611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb`）+ skill `superpowers:verification-before-completion`（plugin @superpowers, sha256-tree-v1 前 12 = `ade95665080e`）—— 本地 skill 加载器若实录 `Local skill not found`，按 E-27 `424CF2D07884` §13 全判定真受审标准 + `_v4_pi_cot_v2_verdict.md` `EB9AD4193CF2` 裁因格式执行，**未编造 skill 不存在的虚构指令**
- **fallback 字面引用诚实交代**：派工单「fallback = `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` `424CF2D07884` 系 E-27 §13 全判定真受审标准 + `_v4_pi_cot_v2_verdict.md` `EB9AD4193CF2` 裁因格式」按字面锚执行；**未编造不存在的引用**
- **T1 prereg §9 SHA 漂移披露沿用**：L14 verdict 自报 SHA `764F24A21AC8` vs 盘实测 SHA `8EEF73BF9856` 漂移（11 B + SHA 全 12 hex 位差异）—— 本 verdict 件字面引用 L14 verdict 时沿用自报 SHA（沿项目「引用锚定 SHA = 字面引用件 §0/§8 自报值」的惯例），漂移事实已披露，不擅自修正
- **判死不软化**（沿 PI 2026-09-23 判死纪律）：本 verdict 件明确 K-T1-S3 字面 PASS = 构造失灵族假象，**不写「仍有希望 / 但仍稳健」类软化语**；L2/L14 既判一字不动仅是 T1 定位硬约束，**非软化判死**

### §5.3 0 产物不编造

- 本 verdict 件唯一新增产物 = `results/_v4_supp_t1_verdict.md`（本件）
- **0 自跑实验 / 0 自起草建议文档 / 0 自发起 worker 接力棒**
- §4 后续建议 = 裁因收口建议，**非执行指令**；须 PI 拍板另起派工单

### §5.4 根因三分类自检（沿 E-27 §13 拍板）

| 判定 | 根因类型 | 根因列是否附 | 备注 |
|---|---|---|---|
| K-N11-3 全 cells hit=True（12 cells） | 假证伪族（构造失灵） | ✓ | empty-empty 主导致 J=0.0 |
| K-T1-S1 hit=False | 假证伪族（构造失灵） | ✓ | empty-empty 致温度维度方向一致 |
| K-T1-S2 hit=False | 假证伪族（构造失灵） | ✓ | 同 K-T1-S1 |
| K-T1-S3 字面 PASS | **假证伪族（构造失灵）** | ✓ | **核心裁因点**：PASS ≠ 真稳健 |
| K-N11-N1_T1relax 全 cells FAIL | 假证伪族（构造失灵） | ✓ | N ∈ {1,3,6} 致命题不可证伪 |

**根因三分类计数**：
- **真证伪**：0 件
- **假证伪族**：5/5 件
- **命题不明**：0 件

### §5.5 与派工单 5 件必带对齐

| 必带项 | 本件状态 |
|---|---|
| agent 名（verdict-keeper） | ✓ 本件由 verdict-keeper 起草 |
| skill 名 + plugin-cache sha256 | ✓ 引用 `scientific-research-workflows:peer-review` + `superpowers:verification-before-completion`（sha256 已列 §5.2）；skill 缺位 fallback 沿 E-27 §13 字面锚 |
| plugin 名（@scientific-research-workflows / @superpowers） | ✓ 已列 §5.2 |
| 7+9 铁律 | ✓ key 永不明文 / V1-V3 只读 / 派生 JSON 不合并 / kill-line 字面不动 / 不调阈值 / 不合并派生 JSON / 判定布尔显式方向 / 不覆盖既有件（新件新名 `_v4_supp_t1_verdict.md`）/ SHA-12 自算写入 / 0 LLM 0 伪造 skill 指令 |
| 老实交代 0 产物 | ✓ 本节 §5.1-§5.4 + §5.5 |

---

## §6 RESULT 报告（诞生即记）

- **本件路径**：`results/_v4_supp_t1_verdict.md`
- **SHA-12（前 12 位）**：见 harness 外部汇报段（自报 vs 盘实测）
- **字节 / 行数**：以落盘末态为准
- **本件性质**：verdict-keeper 判定收口 / T1 产物链末件（与 `_v4_supp_t1_executor.py` `A7CAD9228B0B` + `_v4_supp_t1_result.json` `D6CB03A4657E` 同级独立）
- **锚定 prereg**：`802DECE2286A` 命中（T1 prereg **一字不动**）
- **锚定 activation**：`79936B630015` 命中（T1 activation **一字不动**）
- **锚定 L2 verdict**：`E433A06E7BFB` 命中（L2 verdict **一字不动**）
- **锚定 L14 verdict**：`764F24A21AC8` 命中（L14 verdict **一字不动**；自报 SHA 漂移沿 T1 §9.1 披露）
- **生效后状态**：本件为判定收口件，生效后状态沿 T1 锁先例 → **生效即锁**（沿 `D85488A64D89` `AD42992DC75D` + T1 `802DECE2286A` `79936B630015` 锁先例），事后不重开不调
- **0 触既有件**：1 件新增（`_v4_supp_t1_verdict.md`），16 件既有件 0 触动（详见 §5.1）
- **T1 定位硬约束再声明**：T1 = 稳健性辅助检验（sensitivity probe），**不翻 L2/L14 正式判定**；除 K-T1-S1/S2 命中（实际未命中）+ verdict-keeper 裁因 + verifier 签字，**不得据此改判** L2/L14 既定结论

---

## §7 总判定（一行收口）

> **K-T1-S3 字面命中（PASS）= 构造失灵族假象**：reasoning 模型 mimo-v2.6-pro + deepseek-v4-flash + max_tokens=100 致 49.3% 空响应 + 72.1% empty-empty pairs，J=0.0 主要来自「双方都空」非真判定一致；真证伪要件 ②③④ 失守 → K-T1-S3 字面 PASS ≠ 真稳健；T1 informational 价值 = 揭示构造失灵主因，不可外推为「L2/L14 判定稳健」证据；L2 verdict `E433A06E7BFB` §11 + L14 verdict `764F24A21AC8` §11 一字不动；后续复评须另起 T1.5 / T2 立线棒走 prereg 修订流程，**本 verdict 件不执行任何重跑/补跑/调阈值**。