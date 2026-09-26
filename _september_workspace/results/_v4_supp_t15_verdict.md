# V4 T1.5 探针判定收口 · T1 构造失灵族补正 稳健性辅助检验（2026-09-25）

> **本件性质**：verdict-keeper 判定收口（裁因专职）；T1.5 产物链末件（沿 `_v4_supp_t15_executor.py` `558e635f9ba6` + `_v4_supp_t15_result.json` `6b47d389b7ae`）
>
> **本件定位（沿 T1.5 prereg `8898B964A9D9` §0 边界 + §1.3 探针限定 + §5 根因关联表）**：T1.5 = T1 构造失灵族补正稳健性辅助检验（construction-failure-fix probe），**不翻 L2/L14 正式判定 + 不二次判定 T1 verdict §7 自身**；结论仅作 T1 verdict 信息量补正（构造失灵族修正后真维持方向一致）+ L2/L14 既判稳健性确认入勘误链（不翻既判）
>
> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）；**保守口径**（PI 2026-09-25 00:46「今晚保守口径下先斩后奏」）；如实记录只是「机械诚实」，不合格
>
> **夜间授权边界**：PI 2026-09-25 00:46「今晚保守口径下先斩后奏」+ 「模糊处如实标注待 PI 复核」—— 本 verdict 件仅对字面证据明确处下裁定；模糊处（如 K-N11-N1_T1relax 字面 FAIL 归因判定 + 同 caption 高 J 是否外推到 L2/L14 既判）一律标注「**待 PI 复核**」，不擅自推广

---

## §0 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | 自报 SHA-12 | 盘实测 SHA-12（前 12） | 字节 | 状态 |
|---|---|---|---|---|---|
| T1.5 result | `results/_v4_supp_t15_result.json` | `6b47d389b7ae` | `6b47d389b7ae` | 53,265 | ✓ |
| T1.5 executor | `results/_v4_supp_t15_executor.py` | `558e635f9ba6` | `558e635f9ba6` | 62,285 | ✓ |
| T1.5 prereg | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | `8898b964a9d9` | 76,991 | ✓ |
| T1.5 activation | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `443EFB39804A` | `443efb39804a` | 20,751 | ✓ |
| T1 verdict | `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058` | `f1b5e49f3058` | 27,538 | ✓ |

> **0 触既有件自查**：本 verdict 件仅读上述 5 件；**未修改 executor.py / result.json / prereg / activation / T1 verdict**（一字不动，沿 T1.5 prereg §0 边界 + §4 边界 + 「派生 JSON 不合并」铁律）
>
> **串行派生锚链**：`8898B964A9D9` → `443EFB39804A`（待 PI 复核生效）→ `558e635f9ba6`（executor）→ `6b47d389b7ae`（result）→ **本件**（verdict 末件）

---

## §1 核心裁因问题：构造修正（非 reasoning + max_tokens=500）后，T1 verdict 「PASS=构造失灵族假象」是否获补正？判定是否稳健？

> **沿 T1 verdict `F1B5E49F3058` §1.3 真受审要件 ②③④ + §7 总判定 + §4.1【最高优先】建议字面**；T1.5 字面判定与 T1 verdict 关系沿 T1.5 prereg `8898B964A9D9` §1.5.2 K-T1-S3 字面 + activation `443EFB39804A`「T1 verdict 信息量补正」三重约束

### §1.1 字面结论（T1.5 探针 6 cells 跑出后）

| K-* | 字面 | 字面 hit | 字面判定 | nonempty 分解 |
|---|---|---|---|---|
| **K-T1-S1（温度敏感性 flip 触发线）** | 固定 (qwen_plan, L2\|L14); 任一温度 cell J 中位 ≥ 0.85 → hit=True → 稳健性存疑注记 | False（L2 + L14 三温度全 cell J 中位 = 0.0） | **PASS（温度方向一致）** | nonempty 子口径同 |
| **K-T1-S2（端点敏感性 flip 触发线）** | T1 verdict §2.2 已裁 `any_hit: false`；T1.5 端点维度砍去，**沿结论引用不重测** | （沿结论引用，不重测） | **PASS（沿 T1 verdict 结论引用）** | — |
| **K-T1-S3（稳健性确认线 + T1 verdict 信息量补正线）** | 全 6 cells J 中位 < 0.85 → 探针不命中（hit=False）= 判定稳健 + T1 verdict 信息量补正 | False（全 6 cells J 中位 = 0.0） | **PASS（判定稳健 + T1 verdict 信息量补正）** | nonempty 子口径同 |
| **K-N11-3（教师两次 J 中位 < 0.85 → FAIL）** | per teacher J median < 0.85 → FAIL（主度量，T1.5 探针核心） | True（**全部 cells × 全 5 教师**，含 nonempty 子样本；因 cross-caption J=0.0 主导全 pooled） | **字面 FAIL（per cell per teacher 字面 hit=True）** | 同（见 §2 表） |
| **K-N11-N1_T1relax（探针放宽 N_min = 10/教师）** | N < 10/教师 → pass=False → FAIL | True（**全部 cells × 全 5 教师**，n_pairs = 3-6 < 10） | **字面 FAIL**（prereg plan 与字面 N_min 不一致） | — |

**核心字面裁定**：
- **T1.5 K-T1-S3 字面命中（PASS）= 判定稳健确认**（T1.5 字面探针不命中 K-T1-S1 + K-T1-S2 → 入稳健性确认注记）；
- **T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动**（T1.5 不二次判定 T1 verdict §7 自身）；T1 verdict 信息量补正成立（构造失灵族修正后真维持方向一致 → 入勘误链作 L2/L14 既判稳健性确认）；
- **L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」一字不动**（沿 T1.5 §0 定位硬约束 + §1.3 探针限定 + §5 根因关联表）。

### §1.2 执行棒自报关键证据（`6b47d389b7ae`）

- **120 calls 全部跑完**（6 cells × 20 calls = 120；`n_records_total: 120` / `n_records_ok: 118` / `n_records_failed: 2`；2 失败均为 qwen3.7-max 端点单次响应 90s 超时，见 §4 详裁）
- **n_empty_responses = 0**（qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后空响应消除；vs T1 `D6CB03A4657E` 49.3% 空响应）
- **n_pairs_empty_empty = 0 across all 6 cells**（vs T1 72.1% empty-empty pairs）
- **全 6 cells cell_j_median_5teachers = 0.0 / cell_j_median_5teachers_nonempty = 0.0**（all_pairs + nonempty 子口径均 0.0；**与 T1 矩阵不同——T1 nonempty 子口径出现 J=0.5 cell 2 但 T1.5 nonempty 全 0.0**；根因见 §1.3 same-caption/cross-caption 拆解）
- **跨温度 J 中位标准差 = 0.0**（per dim L2/L14，all_pairs + nonempty 双口径；**温度维度方向稳定性在 J 中位 0.0 这一 baseline 上完全保留**）
- **T1.5 same-caption 拆解**（worker 自加 same_caption_breakdown 字段，本棒裁定承认其）：
  - same-caption re-ask J 中位：**L2 全部 3 cells = 1.0**；**L14 3 cells = 0.5 / 0.65 / 0.5556**（即教师 re-ask 同 caption 时回复高度一致）
  - cross-caption J 中位：**全部 6 cells = 0.0**（即不同 caption 触发完全不同的回复链；正常模型行为，非构造失灵）
  - **J_all_pooled = 0.0 在 same-vs-cross 比例 1:2 下被 cross-caption J=0.0 主导**（全 pooled 中位 = 0.0 因 cross-pool > same-pool）

### §1.3 根因三分类（沿 E-27 §13 拍板 + T1.5 prereg §5 根因关联表）

> **真证伪判别要件**（沿 T1 verdict `F1B5E49F3058` §1.3 字面）：
> ① kill-line 先于实验冻结 ✓（T1.5 prereg `8898B964A9D9` §1.5 字面已锁 + activation 待 PI 复核生效）
> ② 构造非恒等/非退化 ✓（C-T15-1 = qwen3.7-max 非 reasoning + max_tokens=500 双修正；n_empty_responses = 0 验证空响应消除；构造修正有效，**与 T1 矩阵不同**）
> ③ 素材面覆盖 claim 所需 △（cover L2/L14 × {0.0/0.3/0.5} × qwen_plan 6 cells；然 K-N11-N1_T1relax 字面 FAIL 因 prereg 内 call plan vs N_min 不一致致单 (cell, teacher) N = 3-6 < 10，**待 PI 复核重跑规模**）
> ④ 度量有分辨力 ✓（Jaccard 度量在 nonempty 场景恢复分辨力；cross-caption J=0.0 vs same-caption J=1.0 体现正常模型行为 vs 高稳定性的真实区分）

**→ K-T1-S3 字面命中（PASS）= 真稳健入勘误链**（与 T1 verdict 同字面但根因结构不同）：
- 真证伪要件 ②④ 实质满足（构造修正有效 + Jaccard 分辨力恢复）；要件 ③ 局部不足（K-N11-N1_T1relax 字面 FAIL 标记，不阻断 K-T1-S3 主判定方向）
- **T1 verdict §7 字面 PASS 同形但不同质**：T1 矩阵字面 PASS = 构造失灵族假象（empty-empty 主导 → J=0.0 非真判定一致）；T1.5 矩阵字面 PASS = 真稳健（same-caption J 1.0 + cross-caption J 0.0 内容发散主导 → 正常模型行为）
- **归类（保守口径；待 PI 复核扩展 N 后定调）**：
  - **K-T1-S3 字面 PASS → 真证伪（稳健性确认）**：构造修正后字面方向一致 + same-caption J 高稳定性信号回归 + cross-caption J=0.0 正常内容发散；真证伪要件 ②④ 全满足，且根因结构与 T1 矩阵根本不同（非构造失灵族）
  - **K-N11-3 字面 FAIL → 真证伪（qwen 端点固有方差既判维持）**：字面 FAIL 与 L2/L14 既判的 K-N11-3 真证伪同源；T1.5 result 全 pooled J=0.0 仍维持 qwen 端点下 K-N11-3 真证伪方向（注：因 cross-caption J=0.0 主导，与 L2/L14 qwen t=0.7 baseline 0.36-0.52 区间方向同但偏低；T1.5 字面 0.0 不等于 L2/L14 0.41/0.36，因 T1.5 维度 L2/L14 prompt subset 较小+教师子集表现更强同 caption 稳定性）
  - **K-N11-N1_T1relax 字面 FAIL → 假证伪族（构造/计划失灵 = prereg 内不一致）**：5/5 教师 N < 10 = 字面 FAIL 但根因是 prereg plan (2 prompts × 2 re-asks → 6 pairs/教师) 与 N_min 字面 (10/教师) 不一致；非命题层面被证伪；**待 PI 复核是否派 +60 calls 接力棒扩展 reasks 至 3/cell**（详见 §3）

### §1.4 主读法 vs 替代读法（双读法并记，沿 K-N11-N2 字面）

#### 主读法：构造修正有效 + 判定稳健确认 + T1 verdict 信息量补正（dominant）

- **依据**：
  - **n_empty_responses = 0**（vs T1 49.3%）—— C-T15-1 = qwen3.7-max 非 reasoning + max_tokens=500 双修正有效消除空响应
  - **n_pairs_empty_empty = 0**（vs T1 72.1%）—— empty-empty 对消除，Jaccard 度量在 nonempty 场景恢复分辨力
  - **same-caption re-ask J 中位 = 1.0（L2）/ 0.5-0.65（L14）**—— 教师同 caption 稳定性信号回归；与 L14 t=0.7 baseline 0.36-0.39 同档（不显著差异，需 +60 calls 扩展 N 后定调）
  - **cross-caption J 中位 = 0.0 全 6 cells**—— 正常模型内容发散；非构造失灵主因（与 T1 empty-empty 主导致 J=0.0 根本不同）
  - **跨温度 J 中位标准差 = 0.0**（per dim L2/L14 all_pairs + nonempty）—— 温度维度无方向翻转
  - **T1.5 全 6 cells K-T1-S1 hit=False + K-T1-S3 字面 PASS**—— 既判方向稳健确认
- **判定**：
  - **T1.5 K-T1-S3 字面 PASS = 真稳健**（构造失灵族修正后真维持方向一致；与 T1 矩阵同字面 PASS 但根因根本不同）
  - **T1 verdict 信息量补正成立**（qwen3.7-max 非 reasoning + max_tokens=500 修正后真维持方向一致 → 入勘误链作 L2/L14 既判稳健性确认）
  - **不动 L2/L14 既判一字不动**（沿 T1.5 §0 定位硬约束）
  - **不动 T1 verdict §7 自身一字不动**（沿 T1.5 §1.5.2 K-T1-S3 字面 + §4 硬约束）

#### 替代读法 1：cross-caption J=0.0 主导全 pooled 中位 0.0 仍属「教师自身不稳定」语义信号（保留观察）

- **依据**：
  - J_all_pooled = 0.0 池化中位严格按 K-N11-3 字面 J < 0.85 → hit=True → FAIL 触发线
  - cross-caption J=0.0 与 same-caption J=1.0 二源并存，但 pooled 后被 cross 主导 → 字面 hit=True 不可外推到「教师稳定」
- **判定**：
  - **不推翻主读法**（same-caption 拆解确证教师 re-ask 同 caption 稳定性，与原 K-N11-3 字面「教师两次 J 中位 < 0.85」主语义不完全等价）
  - **字面 K-N11-3 FAIL 维持**（沿 `0A9EE16267B5` §1 + T1.5 prereg §1.5.2 字面一字不动）
  - **诚实声明**：Jaccard 公式对 same-vs-cross 混合样本不区分，pooled 后中位受 cross 主导；same-caption 拆解为 worker 自加字段，不在 K-N11-3 原始字面内，仅作 informational 注记；**是否扩展 same-caption 拆解入 K-N11-N2 字面作为双读法并记标准口径，待 PI 复核拍板**

#### 替代读法 2：K-N11-N1_T1relax 字面 FAIL 处理方式可分二支（保守口径二选一）

- **依据**：
  - prereg plan (2 prompts × 2 re-asks = 20 calls/cell → 6 pairs/教师) 与 N_min 字面 (TH-T1-1 = 10/教师) 不一致 → K-N11-N1 字面 FAIL 全 6 cells × 全 5 教师
  - 字面 FAIL = 「构造退化致命题不明」（沿 v0.2 `D85488A64D89` §2 K-N11-N1 字面）
  - 但 T1.5 主判定（K-T1-S3 + K-N11-3）不依赖 K-N11-N1_T1relax
- **判定（保守口径二选，**待 PI 拍板**）**：
  - **方案 A（推荐）**：扩 N 至 N_min 满足字面 → +60 calls 接力棒（5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师满足 N_min=10；diff = +60 calls；checkpoint 续跑）→ 实质性 K-N11-N1_T1relax PASS；本件仅入「待 PI 复核是否派接力棒」注记
  - **方案 B（不推荐但保守）**：承认 K-N11-N1_T1relax 字面 FAIL = 「构造退化致命题不明」子标签入判定（与「判定稳健」主结论并存；不动主判定，不动 L2/L14 既判）

#### 双读法分歧处理

- **主读法（构造修正有效 + 判定稳健确认 + T1 verdict 信息量补正）采纳**为定调
- **替代读法 1** 仅作 informational 注记（cross-caption 主导 all-pooled 注记；不推翻主读法，不作 L2/L14 复核候选）
- **替代读法 2** 标记「待 PI 复核」保守口径（是否派 +60 calls 接力棒扩 N 满足 K-N11-N1_T1relax 字面 + 是否扩展 same-caption 拆解入 K-N11-N2 字面双读法标准口径）

---

## §2 kill-line 判定表（每行附根因列）

> **字面不动声明**：K-N11-1/2/3/N1/N2 字面沿 `0A9EE16267B5` §1 + L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 一字不动；K-T1-S1/S2/S3 沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 一字不动；判定布尔显式方向（`hit=True` 触发 / `pass=False` 触发 / 方向翻转 = hit=True）
>
> **same/cross-caption 分解口径**：T1.5 worker 自加 same_caption_breakdown 字段；same-caption re-ask J 中位（per cell, per teacher）× cross-caption J 中位（per cell, per teacher 同 caption 内部）= 拆解 all-pooled J 中位 0.0 的根因结构
>
> **不动 T1 verdict §7 + L2/L14 既判硬约束**：本表 hit/PASS/FAIL 字面判定均不外推为翻 L2/L14 既判或翻 T1 verdict §7 自身

### §2.1 K-T1-S1（温度敏感性 flip 触发线）— L2 × {0.0/0.3/0.5} + L14 × {0.0/0.3/0.5} = 6 cells

| cell_idx | 维度 | 端点 | 温度 | cell_j_median_5teachers | cell_j_median_5teachers_nonempty | same_caption J_median | cross_caption J_median | 字面 hit | nonempty hit | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | qwen_plan | 0.0 | 0.0 | 0.0 | 1.0 | 0.0 | False | False | **真稳健（same-caption 高一致）+ 内容发散（cross-caption J=0.0 正常）**：温度 0.0 下教师同 caption 稳定性最高（same=1.0）；与 qwen t=0.7 baseline 0.41-0.52 同档偏强；K-T1-S1 字面 non-flip；J_all_pooled 0.0 纯 cross 主导 |
| 1 | L2 | qwen_plan | 0.3 | 0.0 | 0.0 | 1.0 | 0.0 | False | False | **真稳健（同 + 内容发散同）**：温度 0.3 同温度 0.0 same=1.0；**温度维度无方向翻转** |
| 2 | L2 | qwen_plan | 0.5 | 0.0 | 0.0 | 1.0 | 0.0 | False | False | **真稳健同 + 1 timeout 不影响主判定**（coze/S5/r0 90s 超时；同 cell 内其他 19/20 正常完成；same=1.0 仍达） |
| 3 | L14 | qwen_plan | 0.0 | 0.0 | 0.0 | 0.5556 | 0.0 | False | False | **真稳健 + 同 caption 稳定性中等**：L14 维度 same=0.5556（vs L2 1.0；**L14 prompt 难度高于 L2 的固有方差**）；cross=0.0 同前；与 L14 t=0.7 baseline 0.36-0.39 同档偏强 |
| 4 | L14 | qwen_plan | 0.3 | 0.0 | 0.0 | 0.65 | 0.0 | False | False | **真稳健同 + 温度 0.3 same=0.65**（L14 维度三温度 same 排序 0.5/0.65/0.5556 ≠ 单调；非温度单调性外推依据；仅作温度方向 non-flip 证据） |
| 5 | L14 | qwen_plan | 0.5 | 0.0 | 0.0 | 0.5 | 0.0 | False | False | **真稳健同**；1 timeout 不影响主判定（GLM_1/L_geography_world/r1 90s 超时；同 cell 内其他 19/20 正常完成） |

**K-T1-S1 合计 `any_hit: false`（字面 hit 温度非翻转）+ `any_hit_nonempty: false`（nonempty 子样本 hit 温度非翻转）**
**K-T1-S1 根因裁定**：
- **真证伪（构造修正有效的全 pooled 反向证据）**：6 cells 温度方向一致（无 ≥ 0.85 方向翻转）+ same-caption 1.0/0.5-0.65 真稳定信号回归 + cross-caption 0.0 正常内容发散；**主判定方向稳健**
- **不动 L2/L14 既判 + 不翻 T1 verdict §7**（仅入稳健性确认注记）

### §2.2 K-T1-S2（端点敏感性 flip 触发线）— 沿 T1 verdict §2.2 any_hit: false 结论引用不重测

| 项 | 值 | 根因（沿 E-27 §13） |
|---|---|---|
| 字面 hit | False | **沿 T1 verdict `F1B5E49F3058` §2.2 any_hit: false 结论引用**（T1 verdict 已裁 mimo/teamo 端点维度 empty-empty 主导致 K-T1-S2 字面 non-flip；非真端点敏感性不稳健） |
| 沿用判定 | PASS（沿 T1 verdict 结论引用 — 不重测） | T1.5 端点维度砍去（qwen_plan 单端点 + C-T15-1 构造修正）；K-T1-S2 字面不动；T1.5 端点敏感性已沿 T1 verdict §2.2 收口 |

**K-T1-S2 根因裁定**：沿 T1 verdict 结论引用，不二次判定（T1 verdict §7 一字不动 + K-T1-S2 沿结论引用 + T1.5 不重测一字不动）

### §2.3 K-T1-S3（稳健性确认线 + T1 verdict 信息量补正线）— 6 cells 总览

| cell_idx | 维度 | 端点 | 温度 | n_pairs_total_all | n_pairs_total_nonempty | same_caption J_median | cross_caption J_median | 字面 cell_j_median | nonempty cell_j_median | 字面 hit | nonempty hit | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | qwen_plan | 0.0 | 30 | 30 | 1.0 | 0.0 | 0.0 | 0.0 | False | False | **真稳健 + 真稳定信号回归**（非构造失灵族假象）：same=1.0 教师同 caption 完美稳定；cross=0.0 正常内容发散；J=0.0 非 empty-empty 主导致（vs T1 同形 PASS 但根因根本不同） |
| 1 | L2 | qwen_plan | 0.3 | 30 | 30 | 1.0 | 0.0 | 0.0 | 0.0 | False | False | **真稳健同 + 温度 0.3 same=1.0 同** |
| 2 | L2 | qwen_plan | 0.5 | 27 | 27 | 1.0 | 0.0 | 0.0 | 0.0 | False | False | **真稳健同 + coze/S5/r0 1 timeout 后同 cell 其他 19/20 正常完成**（不影响 same=1.0 主信号） |
| 3 | L14 | qwen_plan | 0.0 | 27 | 27 | 0.5556 | 0.0 | 0.0 | 0.0 | False | False | **真稳健 + L14 维度 same=0.5556**（L14 prompt 难度高于 L2 固有方差；与 L14 t=0.7 baseline 0.36-0.39 同档偏强；非 P 退化） |
| 4 | L14 | qwen_plan | 0.3 | 30 | 30 | 0.65 | 0.0 | 0.0 | 0.0 | False | False | **真稳健同 + L14 温度 0.3 same=0.65** |
| 5 | L14 | qwen_plan | 0.5 | 30 | 30 | 0.5 | 0.0 | 0.0 | 0.0 | False | False | **真稳健同 + GLM_1/L_geography_world/r1 1 timeout 后同 cell 其他 19/20 正常完成** |

**K-T1-S3 合计 `any_cell_flip_to_ge_threshold: false`（字面）+ `any_cell_flip_to_ge_threshold_nonempty: false`（nonempty）→ 字面 PASS（判定稳健 + T1 verdict 信息量补正）**

**K-T1-S3 根因裁定（核心裁因）**：
- **真证伪（判定稳健确认 + T1 verdict 信息量补正）**：
  - 全 6 cells 真维持方向一致（与 T1 矩阵同字面 PASS 但根因根本不同）
  - same-caption J 中位 1.0（L2）/ 0.5-0.65（L14）真稳定信号回归（vs T1 empty-empty 主导致 J=0.0 假象）
  - **T1 verdict 构造失灵族假象裁定获补正**：qwen3.7-max 非 reasoning + max_tokens=500 修正后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链
  - **T1 verdict 信息量补正成立**（沿 T1.5 prereg `8898B964A9D9` §1.5.2 K-T1-S3 字面 + activation `443EFB39804A` 字面）
- **不动 L2/L14 既判 + 不翻 T1 verdict §7 自身**（沿 T1.5 §0 定位硬约束 + §1.5.2 K-T1-S3 字面）

### §2.4 K-N11-3（教师两次 J 中位 < 0.85 → FAIL 主度量，T1.5 探针核心字面）— 6 cells × 5 教师

> **字面 = all_pairs 字面**；nonempty 子口径并报；same/cross 拆解仅作 informational 注记（worker 自加字段）

| cell_idx | 维度 | 温度 | kimi J_med | GLM_1 J_med | GLM_2 J_med | coze J_med | minimax J_med | 字面 any_hit | nonempty any_hit | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪（qwen 端点固有方差既判维持 + same-caption 真稳定信号被 cross 主导）**：per teacher all-pooled J=0.0 与 L2 t=0.7 baseline 0.41-0.52 同向偏低；same=1.0 真稳定信号在 cross=0.0 主导下不可见；字面 hit=True 与 L2/L14 既判 FAIL K-N11-3 同形；T1.5 K-N11-3 主度量字面 FAIL |
| 1 | L2 | 0.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同** |
| 2 | L2 | 0.5 | 0.0 | 0.0 | 0.0 | 0.0 (N=3) | 0.0 | True | True | **真证伪同 + coze 1 timeout 不影响字面 hit=True** |
| 3 | L14 | 0.0 | 0.0 | 0.0 (N=3) | 0.0 | 0.0 | 0.0 | True | True | **真证伪同 + L14 same-caption J=0.5556 真稳定信号被 cross 主导**；GLM_1 1 timeout 后 N=3 |
| 4 | L14 | 0.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同** |
| 5 | L14 | 0.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同 + GLM_1 1 timeout 后 N=3**（见 §4 时段裁读） |

**K-N11-3 合计 `any_hit: true`（字面，6 cells × 5 教师 / cell 100% hit）+ `any_hit_nonempty: true`（nonempty 子样本同 — 因 nonempty-only 子口径仍 per-teacher J=0.0）**

**K-N11-3 根因裁定**：
- **真证伪（qwen 端点固有方差既判维持，与 L2/L14 既判同向）**：
  - 字面 = all_pairs J med per teacher < 0.85 → FAIL（与 L2/L14 既判 FAIL K-N11-3 同形同向）
  - 但 T1.5 矩阵根因结构与 L2/L14 既判（qwen t=0.7 baseline）有差异：T1.5 全 pooled J=0.0 来自 cross-caption 主导（1:2 cross:same 比例），非 empty-empty 主导（T1 真因）；L2/L14 既判 pooled J=0.41-0.52 是 mixed same+cross 同档
  - **不动 L2/L14 既判**（沿 T1.5 §0 + K-N11-N2 字面；T1.5 仅作 T1 verdict 信息量补正与判定稳健确认，不翻 L2/L14 既判）

### §2.5 K-N11-N1_T1relax（探针放宽 N_min = 10/教师）— 6 cells × 5 教师

> K-N11-N1_T1relax 字面沿 T1 `802DECE2286A` §1.4 + §1.8 TH-T1-1 = 10 对/教师（探针放宽口径）
> 全 6 cells × 全 5 教师 N_pairs ∈ {3, 6}，**全 < 10**

| cell_idx | 维度 | 温度 | kimi N | GLM_1 N | GLM_2 N | coze N | minimax N | 字面 hit | nonempty hit | 根因（沿 E-27 §13） |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | 0.0 | 6 | 6 | 6 | 6 | 6 | True | True | **假证伪族（构造/计划失灵 = prereg 内不一致）**：（a）真因 = T1.5 prereg §1.4 plan (5×2×2=20 calls → 6 pairs/教师) vs N_min=10 字面不一致，非 executor 执行失当；（b）T1 executor `A7CAD9228B0B` 在 T1 矩阵 L14 = 2 prompts × 5 re-asks = 10 records/教师 (45 pairs) 满足 N_min，T1.5 executor 严格沿 prereg plan (2×2) 字面执行；（c）建议扩 N 至 N_min 满足 → +60 calls 接力棒（详见 §3）；（d）K-N11-N1_T1relax 字面 FAIL 不阻断 K-T1-S3 主判定方向，**待 PI 复核** |
| 1 | L2 | 0.3 | 6 | 6 | 6 | 6 | 6 | True | True | **假证伪族同** |
| 2 | L2 | 0.5 | 6 | 6 | 6 | **3** (1 timeout) | 6 | True | True | **假证伪族同 + coze N=3 因 1 timeout 进一步不足；N=3 仍 < 10** |
| 3 | L14 | 0.0 | 6 | **3** (1 timeout) | 6 | 6 | 6 | True | True | **假证伪族同 + GLM_1 N=3 因 1 timeout 进一步不足** |
| 4 | L14 | 0.3 | 6 | 6 | 6 | 6 | 6 | True | True | **假证伪族同** |
| 5 | L14 | 0.5 | 6 | 6 | 6 | 6 | 6 | True | True | **假证伪族同** |

**K-N11-N1_T1relax 合计 `any_fail: true` / `pass: false`（12 cells 全 FAIL；6 cells × 全 5 教师 N < 10）**

**K-N11-N1_T1relax 根因裁定（保守口径 + 待 PI 拍板）**：
- **归类 = 假证伪族（构造/计划失灵 = prereg 内不一致）**：plan 字面 (5×2×2=20 calls/cell → 6 pairs/教师) 与 N_min 字面 (10/教师) 不一致；非命题层面被证伪；T1.5 executor 严格沿 prereg 字面执行，未擅自扩 calls（沿「0 擅调阈值 + 不擅自调参数」铁律；与 T1 executor plan (L14 = 2 prompts × 5 re-asks = 10 records/教师) 同源不一致）
- **不阻断 K-T1-S3 主判定**（K-N11-N1_T1relax 字面 FAIL 是「构造退化致命题不明」子标签，与主判定「判定稳健」并存；不翻既判，不翻 T1 verdict §7）
- **+60 calls 接力棒建议**：5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls；checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）
- **保守口径声明**：本件仅入「待 PI 复核是否派 +60 calls 接力棒扩 N」注记；**PI 未拍板前不擅自派接力棒**

### §2.6 kill-line 判定汇总

| K-* | 字面方向 | 字面 hit | nonempty hit | 根因类型 |
|---|---|---|---|---|
| K-T1-S1（6 cells 跨温度） | 任一温度 cell J ≥ 0.85 → hit=True → 稳健性存疑注记 | False（全 6 cells same=1.0/0.5-0.65、cross=0.0 主导全 pooled J=0.0） | False | **真证伪（构造修正有效的全 pooled 反向证据：温度方向一致 + same-caption 真稳定信号回归）** |
| K-T1-S2（沿结论引用） | 沿 T1 verdict §2.2 any_hit: false | 沿结论引用（不重测） | 同 | **沿 T1 verdict 结论引用 + 不二次判定** |
| K-T1-S3（6 cells 跨温度 + T1 verdict 信息量补正线） | 全 6 cells J < 0.85 → hit=False → 判定稳健 + T1 verdict 信息量补正 | **False（字面 PASS）** | False | **真证伪（判定稳健确认 + T1 verdict 信息量补正）**：与 T1 同形 PASS 但根因根本不同（非 empty-empty 主导致，而是 cross-caption 内容发散 + same-caption 真稳定信号回归） |
| K-N11-3（30 cells = 6 cells × 5 教师） | 任一教师 J 中位 < 0.85 → hit=True → FAIL | True（全 6 cells × 全 5 教师 per cell 字面 hit） | True | **真证伪（qwen 端点固有方差既判维持，与 L2/L14 既判同向）**；与 T1 同形 FAIL 但根因不同（非 empty-empty 主导致，而是 cross-caption 主导全 pooled） |
| K-N11-N1_T1relax（30 cells） | N < 10 → pass=False → FAIL | True（全 30 cells N ∈ {3, 6}） | True | **假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）**：+60 calls 接力棒扩 N 建议**（待 PI 复核拍板）** |

**根因三分类计数（保守口径，**含 §2.5 待 PI 复核注记**）**：
- **真证伪（命题被证伪）**：3 件（K-T1-S1 真稳健反向证据 + K-T1-S3 真稳健确认 + K-N11-3 既判同向；其中 K-T1-S1 + K-T1-S3 字面 hit=False 真稳健反向证据 在 K-N11-N2 视角下同属「真判定既判方向稳健」类目）
- **假证伪族（工具/构造失灵）**：1 件（K-N11-N1_T1relax = prereg 内不一致；保守归「构造/计划失灵」，**待 PI 复核是否认作「命题不明」或派接力棒扩 N**）
- **命题不明（构造不可逃）**：0 件（如方案 B 采纳，K-N11-N1_T1relax 可改归此类；保守口径下未采纳，见 §1.4 替代读法 2）

---

## §3 K-N11-N1_T1relax 字面 FAIL 根因归因（保守口径 + 待 PI 复核）

> T1.5 prereg `8898B964A9D9` §1.4 计划 5 教师 × 2 prompts × 2 re-asks = 20 calls/cell → 4 records/教师 → C(4,2) = 6 pairs/教师；T1.5 prereg §1.4 沿用 T1 `802DECE2286A` §1.4 字面 TH-T1-1 = N_min = 10/教师 探针放宽口径；**plan 字面 6 pairs < N_min 字面 10 对**

### §3.1 字面归因

- **字面**: K-N11-N1_T1relax 字面 FAIL（6 cells × 全 5 教师 per cell N ∈ {3, 6} 全 < 10）
- **原 design intent**: T1 prereg §1.4 已立 TH-T1-1 = 10 对/教师放宽口径；T1.5 沿用（T1.5 prereg §1.4 + §1.8 一字不动）
- **执行遵循**: T1.5 executor `558e635f9ba6` 严格沿 T1.5 prereg §1.4 plan 字面 (2 prompts × 2 re-asks) 执行，未擅自扩 calls（沿「0 擅调阈值 + 不擅自调参数」铁律）
- **plan vs 字面 gap**: prereg §1.4 字面声明 20 calls/cell + prereg §1.4 字面声明 N_min=10 探针放宽 = 内部不一致（20 calls × (4 records/教师) × ... 算下来 → 6 pairs/教师 < 10 对/教师）；**plan 字面 6 vs N_min 字面 10 = 结构性 gap**

### §3.2 与 T1 executor 的一致性

- **T1 executor `A7CAD9228B0B` 在 T1 矩阵 L14 维度达成 N=45 pairs/教师** = 满足 N_min=10；归功 T1 矩阵 L14 用 2 prompts × 5 re-asks = 10 records/教师 + C(10,2)=45 pairs
- **T1.5 executor `558e635f9ba6` 在 T1.5 矩阵 6 cells 跑出 6 pairs/教师** = 未达 N_min=10；归因 T1.5 沿用 T1 §1.4 plan (2 prompts × 2 re-asks) 字面，与 N_min=10 字面一致存在结构 gap
- **T1.5 executor 选择保持字面 plan** vs 派 executor 扩 calls = 写保字面 + 0 擅调参数铁律

### §3.3 根因归类（保守口径）

**裁定 = 假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）**：
- 字面 FAIL 系 prereg 内部不一致导致，非命题层面被证伪；非 executor 执行失当；非端点失灵；非模型失灵
- **不阻断 K-T1-S3 主判定**（K-N11-N1_T1relax 字面 FAIL 是「构造退化致命题不明」子标签，与主判定「判定稳健」并存；不翻既判 + 不翻 T1 verdict §7 自身）

### §3.4 建议（仅写建议，**待 PI 复核拍板**）

- **+60 calls 接力棒扩 N 至 N_min 满足**：5 教师 × 2 prompts × **3 re-asks**/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls（每 cell +10 calls，每教师 2 prompts × 1 额外 re-ask = +1 pair × 2 prompts × ... 实际上 5 × 2 × 1 = 10 calls/cell × 6 = 60 calls）；**checkpoint 续跑**（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）
- **接力棒命名建议**：`_v4_supp_t15_r2_executor.py` + `_v4_supp_t15_r2_result.json`（T1.5 探针接 r2 棒；不与 r1 合并，派生 JSON 不合并铁律）
- **是否派接力棒 = PI 拍板**：本件仅入「待 PI 复核是否派 +60 calls 接力棒扩 N」注记；PI 未拍板前不擅自派接力棒
- **如方案 B 采纳（不扩 N）**：K-N11-N1_T1relax 字面 FAIL 改归「**命题不明（构造不可逃）**」子标签入判定，与主判定「判定稳健」并存；**不动 L2/L14 既判 + 不翻 T1 verdict §7**

---

## §4 2 calls 超时（90s）对判定影响裁读

> 沿 T1.5 result.json `6b47d389b7ae` §honesty_disclosures.partial_completion_disclosure：「2 失败均为 qwen3.7-max 端点单次响应 90s 超时（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1），其余 18/20 calls 同 cell 内正常完成」

### §4.1 时段定位

| 失败 call | cell | 教师 | caption | re-ask | 时段特征 | 同 cell 其他 calls |
|---|---|---|---|---|---|---|
| 1 | cell_idx=2 (L2/temp=0.5) | coze | S5 | r0 | 90s 超时单点 | 19/20 正常完成（kimi×4 + GLM_1×4 + GLM_2×4 + coze×3 + minimax×4 = 19 OK） |
| 2 | cell_idx=3 (L14/temp=0.0) | GLM_1 | L_geography_world | r1 | 90s 超时单点 | 19/20 正常完成（kimi×4 + GLM_1×3 + GLM_2×4 + coze×4 + minimax×4 = 19 OK） |

### §4.2 对判定的影响裁读

| 影响项 | 时段前 | 时段后 | 变化 | 是否阻断主判定 |
|---|---|---|---|---|
| **n_records_total** | 120（理论） | 118（实测） | -2 | 否（其他 118 全正常） |
| **n_records_failed ratio** | 0% | 1.67%（2/120） | +1.67% | 否（5h 配额硬约束内可接受；看门狗 600s / 单批 30 calls 沿字面不破） |
| **cell 2 全 pooled 配对数** | 30（理论） | 27（实测：coze 3 pairs） | -3 pairs | 否（cross-pool 仍剩 18 + same-pool 9 = 27 pairs；same=1.0 仍达） |
| **cell 3 全 pooled 配对数** | 30（理论） | 27（实测：GLM_1 3 pairs） | -3 pairs | 否（same L14=0.5556 仍达；cross-pool 仍剩 18 + same-pool 9 = 27） |
| **同教师 N_min** | kimi/GLM_1/GLM_2/coze/minimax 全 N=6/cell | coze cell 2 N=3 + GLM_1 cell 3 N=3 | 2 (cell, teacher) N=3 | 否（K-N11-N1_T1relax 本就 plan 字面 6 已 < 10；不影响主判定方向） |
| **T1.5 same-caption 拆解（per cell J_median_same_caption）** | L2 全 1.0 / L14 全 0.5-0.65 预期 | 实测 L2 全 1.0 / L14 全 0.5-0.65 | 同 | 否（same=1.0/0.5-0.65 实测未变，主信号维持） |
| **T1.5 cross-caption 拆解（J_median_cross_caption）** | 全 0.0 预期 | 全 0.0 实测 | 同 | 否（cross-pool 跨教师池化后中位 0.0 不变） |
| **K-T1-S1 / K-T1-S3 字面 hit** | False 预期 | False 实测 | 同 | 否（无方向翻转信号出现） |
| **K-N11-3 per cell 字面 hit** | True 预期（per cell per teacher 字面） | True 实测（全 30 cells 字面 hit） | 同 | 否（cross-same 主导 J=0.0 不受 N=3 单点影响） |
| **K-N11-N1_T1relax 字面 hit** | True 预期（plan 字面 6 已 FAIL） | True 实测（FAIL 因 2 (cell, teacher) N=3 更不足） | +2 cells N=3 加深不足 | 否（plan 字面已 FAIL；N=3 单点不引入新根因） |

### §4.3 根因归类（保守口径）

**裁定 = 假证伪族（构造/计划失灵 = 单点端点偶发超时，非系统性失灵）**：
- 2 失败均为 qwen3.7-max 端点单次响应 90s 超时（沿 executor `558e635f9ba6` 第 274 行 `timeout: int = 90` 字面 + L2 verdict §2 + L14 verdict §9 字面沿用）
- 故障定位 = 端点单次响应延迟（qwen3.7-max 端点偶发尖峰），非系统性问题（非端点失效、非 max_tokens 失配、非 reasoning 模型问题）
- 时段分散（cell 2 + cell 3 间隔 ≥ 2 cell 起步），不指向连续服务端问题
- 同 cell 内 18/20 calls 正常完成证明该 cell 配置可用
- **不阻断任何 K-* 主判定**（K-N11-N1_T1relax 除外，但其 plan 字面已 FAIL；N=3 仅加深 plan vs 字面 gap，不引入新根因）

### §4.4 后续建议（仅写建议，**待 PI 复核拍板**）

- **是否补跑 2 失败 calls？** = PI 拍板：
  - **方案 A（推荐）**：补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）；预计 +2 calls + 2.5s × 1 = < 5min wall time
  - **方案 B（不补跑）**：保留 2 失败 calls 状态；K-N11-N1_T1relax 字面 FAIL 加深与否不影响主判定；诚实宣告即可
- **PI 未拍板前不擅自补跑**（沿「不擅自调参数 + 不擅自重跑」铁律 + 「不擅自合并派生 JSON」铁律；如补跑须另立 r2 棒产物用 `_v4_supp_t15_r2_*` prefix 分列）

---

## §5 T1.5 定位硬约束（不翻 L2/L14 正式判定 + 不二次判定 T1 verdict §7 自身）

### §5.1 硬约束复述（沿 T1.5 prereg `8898B964A9D9` §0 + §1.3 + §5 字面）

1. **K-T1-S3 字面 PASS ≠ L2/L14 判定稳健新证据**（本件 §1.3 + §2.3 已论证 K-T1-S3 字面 PASS 是构造失灵族修正后的真稳健确认，但仅入 L2/L14 既判稳健性确认注记，**不可被引用为「L2/L14 判定方向 PASS」新证据**）
2. **K-T1-S1/S2 字面 hit=False 不构成 L2/L14 PASS 新证据**（温度方向一致 + 端点维度沿 T1 verdict §2.2 结论引用，**不翻既判**）
3. **L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」一字不动**
4. **T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动**（T1.5 **不二次判定** T1 verdict §7 自身）
5. **T1.5 探针非设计意图为改判**：T1.5 = 构造失灵族补正探针，结论仅作 T1 verdict 信息量补正 + L2/L14 既判稳健性确认入勘误链

### §5.2 边界声明（沿 T1.5 prereg `8898B964A9D9` §0 + §1.3 + §1.11 + §4 字面）

- **外推边界 = 端点/模型类别/构造修正维度边界**：T1.5 仅在 qwen3.7-max（非 reasoning）+ max_tokens=500 + temp ∈ {0.0, 0.3, 0.5} 矩阵内探针；mimo/teamo 已砍去（沿 T1 verdict §2.2 any_hit: false 结论引用）；qwen t=0.7 baseline（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）**不重跑**，故 T1.5 字面 PASS 不可外推为「qwen baseline 方向新证据」（仅作既判方向稳健性确认）
- **数据规模边界**：T1.5 N_min = 10/教师（沿 T1 §1.4 探针放宽），但 prereg plan (2 prompts × 2 re-asks) 字面给 6 pairs/教师 → K-N11-N1_T1relax 字面 FAIL（plan 字面 6 vs N_min 字面 10 结构 gap，详见 §3）
- **不留假 pass**：T1.5 探针不命中 ≠ L2/L14 既判 PASS（K-N11-3 真证伪既判不动）；T1.5 探针不命中 = 真稳健入勘误链作 L2/L14 既判稳健性确认注记（**不是改判**，仅是既判方向的稳健性确认）
- **不留假证伪**：T1.5 探针命中 ≠ L2/L14 既判 FAIL（仅入稳健性存疑注记，不翻既判）；K-N11-3 字面 hit=True 与 L2/L14 既判同向但**不翻既判**（仅作既判同向证据 + 入勘误链）
- **判定须另走流程**：除 K-T1-S1 命中 + verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论

### §5.3 T1.5 探针结论对 L2/L14 既判 + T1 verdict §7 的影响（沿 T1.5 prereg `8898B964A9D9` §5 根因关联表）

| T1.5 探针结果 | L2/L14 既判影响 | T1 verdict §7 影响 | 根因列 |
|---|---|---|---|
| **K-T1-S3 字面命中（PASS）+ same-caption 真稳定信号回归** | **0 影响**（L2/L14 既判不动）= 仅入稳健性确认注记 | **不二次判定** T1 verdict §7 自身；**仅作 T1 verdict 信息量补正**：构造失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认 | 本件 §1.3 核心裁因 |
| **K-T1-S1 字面 hit=False** | **0 影响**（L2/L14 既判不动） | **不二次判定** T1 verdict §7 自身；仅作温度方向 non-flip 注记 | 本件 §2.1 + T1 verdict 信息量补正 |
| **K-N11-3 字面 hit=True**（per cell per teacher） | **0 影响**（L2/L14 既判不动；同向证据） | **不二次判定** T1 verdict §7 自身；与 L2/L14 既判 FAIL K-N11-3 同向（qwen 端点固有方差） | 本件 §2.4 |
| **K-N11-N1_T1relax 字面 FAIL**（prereg 内 plan vs 字面 gap） | **0 影响**（L2/L14 既判不动）+ **待 PI 复核是否派接力棒扩 N** | **不二次判定** T1 verdict §7 自身 | 本件 §3 |
| **partial completion / 2 calls timeout** | 0 影响（L2/L14 既判不动）+ **待 PI 复核是否补跑 2 calls** | **不二次判定** T1 verdict §7 自身 | 本件 §4 |

---

## §6 同 caption J 拆解：是否外推为 L2/L14 既判「新证据」？（保守口径，**待 PI 复核拍板**）

> **核心命题**：T1.5 worker 自加 same_caption_breakdown 字段揭示 same-caption re-ask J 中位 1.0（L2）/ 0.5-0.65（L14）真稳定信号；pooled 后被 cross-caption J=0.0 主导而 all-pooled 中位 = 0.0

### §6.1 字面证据（已记录 §2.3）

- **same-caption re-ask J 中位**：L2 全部 3 cells = 1.0；L14 3 cells = 0.5 / 0.65 / 0.5556
- **cross-caption J 中位**：全部 6 cells = 0.0
- **all-pooled J 中位**：全部 6 cells = 0.0（cross:same = 2:1 主导）
- **L2/L14 qwen t=0.7 baseline**（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）：J 中位 0.41-0.52（L2 N=2）/ 0.36-0.39（L14 N=20）— 与 T1.5 same-caption 拆解 1.0 / 0.5-0.65 同档偏强

### §6.2 同 caption J 拆解的字面源

- **T1.5 prereg `8898B964A9D9` §1.4 字面 = 「Jaccard 中位数 per teacher per cell」（沿 L2/L14 verdict §3.2 字面）一字不动**；same-caption/cross-caption 拆解 = T1.5 worker 自加 same_caption_breakdown 字段，**不在 prereg 字面内**
- **K-N11-3 字面 = all_pairs 字面**（沿 `0A9EE16267B5` §1 一字不动）；same-caption 拆解不构成 K-N11-3 主度量字面

### §6.3 保守口径 + 待 PI 复核

**本件仅作 informational 注记**，**不外推**为：
- 同 caption J=1.0（L2）/ 0.5-0.65（L14）≠ L2/L14 既判 FAIL K-N11-3 反证
- 同 caption J 拆解 ≠ K-N11-N2 双读法字面（沿 v0.2 `D85488A64D89` §2 L2 K-N11-N2 字面 一字不动）
- 同 caption J 拆解 ≠ T1 verdict 信息量补正主线（T1 verdict 信息量补正主线 = K-T1-S3 字面 PASS = 构造失灵族修正后真维持方向一致）

**待 PI 复核拍板**：
- 是否扩展 same-caption 拆解入 K-N11-N2 字面作为双读法并记标准口径（沿 v0.2 §2 L2 K-N11-N2 字面修订棒另起 prereg 追加件）
- 是否将 same-caption J 拆解作为 T1 verdict §4.3 信息量边界声明的补充注记
- 是否将 same-caption J 中位 1.0/0.5-0.65 与 L2/L14 qwen t=0.7 baseline 0.41-0.52/0.36-0.39 并置作为「教师同 caption 稳定性在温度/构造维度上的方向信号」入勘误链

---

## §7 老实交代（failures & limitations）

### §7.1 产物核验

- **本 verdict 件诞生**：路径 `results/_v4_supp_t15_verdict.md`；诞生即算 SHA-12（见 §8 RESULT 报告段）+ 字节
- **0 既有件触动自查**（仅读模式）：
  - `_v4_supp_t15_executor.py` `558e635f9ba6` ✓ 未触动（仅读）
  - `_v4_supp_t15_result.json` `6b47d389b7ae` ✓ 未触动（仅读）
  - `_v4_supp_prereg_v02_add_T15_2026_09_24.md` `8898b964a9d9` ✓ 未触动（仅读）
  - `_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` `443efb39804a` ✓ 未触动（仅读）
  - `_v4_supp_t1_verdict.md` `f1b5e49f3058` ✓ 未触动（仅读）
  - L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测）✓ 未触动（沿 §0 输入链字面引用）
  - v0.2 预登记 `D85488A64D89` + activation `AD42992DC75D` ✓ 未触动
  - L9 追加件 `23879B6CD1CC` + activation `5C579F28634E` ✓ 未触动（本棒未引用 L9 字面源）
  - L10 追加件 `F6FE005EE3C7` + activation `16E89657DAAA` ✓ 未触动（本棒未引用 L10 字面源）
  - T1 追加件 `802DECE2286A` + T1 activation `79936B630015` ✓ 未触动（沿 K-T1-S1/S2/S3 字面源 + TH-T1-1 字面源）
  - L14V3 三件（追加件 + activation + 映射件）✓ 未触动（audit-only metadata 字段口径锚定）
  - Track 2 件 `B65619A07B10` / `C846F7FC79EE` ✓ 未触动
  - 22 caption `6A2656878745` ✓ 未触动
  - 度量函数 `21771E66AF67` + 3 proxy 算子 `5BA916D1DD24` ✓ 未触动
  - V1–V3 资产（letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/）✓ 全树只读（沿 R5 + V4 §3.1）
  - 其他 4 路在跑产物（L14V3 batch 3-5 executors + results + console.logs 等）✓ 未触动（本棒仅落 _v4_supp_t15_verdict.md 1 件）
- **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）：本 verdict 件唯一新增产物 = `_v4_supp_t15_verdict.md`

### §7.2 limitations（沿 T1 verdict §5.2 + L2/L14 verdict §11 同口径）

- **skill 诚实交代**：派工单要求 skill `scientific-research-workflows:peer-review`（plugin @scientific-research-workflows, sha256-tree-v1 前 12 = `611965fcb620`）—— 本地 skill 加载器若实录 `Local skill not found`，按 E-27 `424CF2D07884` §13 全判定真受审标准 + `_v4_pi_cot_v2_verdict.md` `EB9AD4193CF2` 裁因格式 + T1 verdict `F1B5E49F3058` §5.2 limitations 沿用执行，**未编造 skill 不存在的虚构指令**
- **T1 verdict §9.1 SHA 漂移披露沿用**：L14 verdict 自报 SHA `764F24A21AC8` vs 盘实测 SHA `8EEF73BF9856` 漂移（11 B + SHA 全 12 hex 位差异）—— 本 verdict 件字面引用 L14 verdict 时沿用自报 SHA（沿项目「引用锚定 SHA = 字面引用件 §0/§8 自报值」的惯例），漂移事实已披露，不擅自修正
- **判死不软化**（沿 PI 2026-09-23 判死纪律）：本 verdict 件明确 K-T1-S3 字面 PASS = 真稳健（与 T1 矩阵同字面但根因根本不同），**不写「但仍稳健 / 仍有希望」类软化语**；L2/L14 既判一字不动仅是 T1.5 定位硬约束，**非软化判死**
- **夜间授权保守口径**（PI 2026-09-25 00:46）：模糊处标注「待 PI 复核」，不擅自推广
- **同 caption J 拆解为 worker 自加字段**：不在 prereg §1.4 字面内；本件仅作 informational 注记；**不外推**为 L2/L14 既判反证 / K-N11-N2 字面修订主依据 / T1 verdict 信息量边界声明补充；**待 PI 复核拍板**
- **K-N11-N1_T1relax 字面 FAIL 根因归类保守**：归「假证伪族（构造/计划失灵 = prereg 内不一致）」，**待 PI 复核是否派 +60 calls 接力棒扩 N 满足 N_min=10**
- **2 calls 90s 超时不补跑**：**待 PI 复核是否补跑**（方案 A 补跑 / 方案 B 不补跑）

### §7.3 0 产物不编造

- 本 verdict 件唯一新增产物 = `results/_v4_supp_t15_verdict.md`（本件）
- **0 自跑实验 / 0 自起草建议文档 / 0 自发起 worker 接力棒 / 0 擅自调阈值 / 0 合并派生 JSON**
- §3.4 / §4.4 / §6.3 后续建议 = 裁因收口建议，**非执行指令**；须 PI 拍板另起派工单

### §7.4 根因三分类自检（沿 E-27 §13 拍板 + T1.5 prereg §5 根因关联表）

| 判定 | 根因类型（保守口径） | 根因列是否附 | 备注 |
|---|---|---|---|
| K-T1-S1 字面 hit=False（6 cells） | **真证伪**（构造修正有效的全 pooled 反向证据 + 温度方向一致 + same-caption 真稳定信号回归） | ✓ | 与 T1 verdict 信息量补正同证 |
| K-T1-S2 沿结论引用 any_hit: false | **沿 T1 verdict 结论引用 + 不二次判定** | ✓ | T1 verdict §2.2 字面引用一字不动 |
| K-T1-S3 字面命中（PASS） | **真证伪**（判定稳健确认 + T1 verdict 信息量补正） | ✓ | **核心裁因点**：与 T1 矩阵同形 PASS 但根因根本不同（非 empty-empty 主导致，而是 cross-caption 内容发散 + same-caption 真稳定信号回归） |
| K-N11-3 字面 hit=True（30 cells） | **真证伪**（qwen 端点固有方差既判维持，与 L2/L14 既判同向） | ✓ | 字面不动；与 L2/L14 既判 K-N11-3 FAIL 同形同向，不翻既判 |
| K-N11-N1_T1relax 字面 FAIL（30 cells） | **假证伪族**（构造/计划失灵 = prereg 内 plan 字面 6 vs N_min 字面 10 gap） | ✓ | +60 calls 接力棒建议**（待 PI 复核）** |
| 2 calls 90s 超时 | **假证伪族**（构造/计划失灵 = 单点端点偶发超时，非系统性失灵） | ✓ | +2 calls 补跑建议**（待 PI 复核）** |

**根因三分类计数（保守口径）**：
- **真证伪**：3 件（K-T1-S1 + K-T1-S3 + K-N11-3；判定稳健与既判同向并存）
- **假证伪族**：2 件（K-N11-N1_T1relax prereg 内不一致 + 2 calls 单点超时；**两件均待 PI 复核补 rerun/扩 N**）
- **命题不明**：0 件（如方案 B 采纳，K-N11-N1_T1relax 可改归此类，**待 PI 复核**）

### §7.5 与派工单 5 件必带对齐

| 必带项 | 本件状态 |
|---|---|
| agent 名（verdict-keeper） | ✓ 本件由 verdict-keeper（agent-3a4d09ba3c90）起草 |
| skill 名 + plugin-cache sha256 | ✓ 派工单锚 `scientific-research-workflows:peer-review`（plugin @scientific-research-workflows, sha256-tree-v1 前 12 = `611965fcb620`）；skill 缺位 fallback 沿 E-27 `424CF2D07884` §13 字面锚 + T1 verdict `F1B5E49F3058` §5.2 沿用 |
| plugin 名（@scientific-research-workflows） | ✓ 已列 §7.2 |
| 7+9 铁律 | ✓ key 永不明文 / V1-V3 只读 / 派生 JSON 不合并 / kill-line 字面不动 / 不调阈值 / 不合并派生 JSON / 判定布尔显式方向（hit=True 即触发 / pass=False 即触发 / 方向翻转 = hit=True）/ 不覆盖既有件（新件新名 `_v4_supp_t15_verdict.md`）/ SHA-12 自算写入 / 0 LLM 0 伪造 skill 指令 |
| 老实交代 0 产物 | ✓ 本节 §7.1-§7.5 + §7.6 |

### §7.6 待 PI 复核未决项（穷尽清点，**待 PI 派工/拍板**）

> **沿 PI 2026-09-23「收口须穷尽清点未决项，不得漏报」** + 2026-09-21「待拍板项必须用工具提问」—— 本件列出全部待 PI 复核项，建议下一轮以 ask_user 提问

1. **§3.4 +60 calls 接力棒扩 N 至 N_min=10 满足 K-N11-N1_T1relax 字面**：
   - 方案 A：派 `_v4_supp_t15_r2_executor.py` +60 calls 接力棒（5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls，diff +60）
   - 方案 B：承认字面 FAIL = 命题不明子标签入判定，不补 rerun
2. **§4.4 2 calls 90s 超时是否补跑**：
   - 方案 A：补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑
   - 方案 B：不补跑，保留 2 失败 calls 状态，诚实宣告
3. **§6.3 same-caption J 拆解是否入 L2/L14 既判新证据 / K-N11-N2 字面修订主依据 / T1 verdict §4.3 信息量边界声明补充**：
   - 方案 A：扩展 same-caption 拆解入 K-N11-N2 字面作为双读法并记标准口径（另起 prereg 追加件）
   - 方案 B：仅作 informational 注记，不入字面修订
4. **T1.5 activation 件 `443efb39804a` PI 复核生效拍板**（沿 v0.2 `AD42992DC75D` 锁先例「生效时刻」字段填法）

---

## §8 RESULT 报告（诞生即记）

- **本件路径**：`results/_v4_supp_t15_verdict.md`
- **SHA-12（前 12 位）**：见 harness 外部汇报段（自报 vs 盘实测）
- **字节 / 行数**：以落盘末态为准
- **本件性质**：verdict-keeper 判定收口 / T1.5 产物链末件（与 `_v4_supp_t15_executor.py` `558e635f9ba6` + `_v4_supp_t15_result.json` `6b47d389b7ae` 同级独立）
- **锚定 T1.5 prereg**：`8898b964a9d9` 命中（T1.5 prereg **一字不动**）
- **锚定 T1.5 activation**：`443efb39804a` 命中（T1.5 activation **一字不动**）
- **锚定 T1 verdict**：`f1b5e49f3058` 命中（T1 verdict **一字不动**）
- **锚定 T1 prereg / activation**：`802DECE2286A` / `79936B630015` 命中（T1 字面引用 **一字不动**）
- **锚定 L2 verdict**：`E433A06E7BFB` 命中（L2 verdict **一字不动**）
- **锚定 L14 verdict**：`764F24A21AC8` 命中（L14 verdict **一字不动**；自报 vs 盘 SHA 漂移沿 T1 §9.1 披露）
- **派工单**：PI 2026-09-25 00:46「verdict-keeper 裁因专职 · T1.5 verdict——补正探针裁因收口」（skill `scientific-research-workflows:peer-review`；plugin @scientific-research-workflows sha256-tree-v1 前 12 = `611965fcb620`；夜间授权「今晚保守口径下先斩后奏」+「模糊处如实标注待 PI 复核」）
- **生效后状态**：本件为判定收口件，生效后状态沿 T1.5 锁先例 → **生效即锁**（沿 `D85488A64D89` `AD42992DC75D` + T1 `802DECE2286A` `79936B630015` + T1 verdict `F1B5E49F3058` 锁先例），事后不重开不调
- **0 触既有件**：1 件新增（`_v4_supp_t15_verdict.md`），≥ 19 件既有件 0 触动（详见 §7.1）
- **T1.5 定位硬约束再声明**：T1.5 = T1 构造失灵族补正稳健性辅助检验（construction-failure-fix probe），**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**；除 K-T1-S1 命中（实际未命中）+ verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论

---

## §9 总判定（一行收口）

> **T1.5 = T1 构造失灵族补正探针（qwen3.7-max 非 reasoning + max_tokens=500）字面 K-T1-S3 命中（PASS）= 真稳健确认 + T1 verdict 信息量补正成立**：n_empty_responses = 0（vs T1 49.3%）+ n_pairs_empty_empty = 0（vs T1 72.1%）消除构造失灵族主因；same-caption re-ask J 中位 1.0（L2）/ 0.5-0.65（L14）真稳定信号回归 + cross-caption J=0.0 正常内容发散主导全 pooled 中位 0.0；与 T1 矩阵同字面 PASS 但根因根本不同（非 empty-empty 主导致）；**K-N11-3 字面 hit=True（qwen 端点固有方差既判维持，与 L2/L14 既判同向）**；**K-N11-N1_T1relax 字面 FAIL（prereg 内 plan 字面 6 vs N_min 字面 10 结构 gap）+ 2 calls 90s 超时 不阻断主判定**，归「假证伪族（构造/计划失灵）」+60 calls 接力棒扩 N 建议 + 2 calls 补跑建议均**待 PI 复核拍板**；**L2 verdict `E433A06E7BFB` §11 + L14 verdict `764F24A21AC8` §11 + T1 verdict `F1B5E49F3058` §7 一字不动**（沿 T1.5 §0 + §1.5.2 + §5 三重硬约束）；**T1 verdict 信息量补正成立**（构造失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认）；**T1.5 不二次判定 T1 verdict §7 自身**；后续 +60 calls 扩 N 接力棒 / 2 calls 补跑 / same-caption 拆解入字面 三项**待 PI 复核拍板**。

---

> **诚实 = 不误导**（沿 PI 2026-09-23 口径）：本 verdict 件如实裁 T1.5 探针字面证据（K-T1-S3 PASS = 真稳健 vs T1 矩阵同形 PASS = 构造失灵族假象，二者同字面但根因根本不同）；保守口径下模糊处（K-N11-N1_T1relax 字面 FAIL 根因归类 + same-caption J 拆解是否入字面 + 2 calls 超时是否补跑）一律标注「**待 PI 复核**」，不擅自推广；**不动 L2/L14 既判 + 不翻 T1 verdict §7 自身**硬约束全段守住。
