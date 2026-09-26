# V4 T1.5r2 探针判定收口 · T1.5 扩样修订 N_min≥10 字面满足 · 裁因确认（2026-09-26）

> **本件性质**：verdict-keeper 判定收口（裁因专职）；T1.5r2 产物链末件（沿 `_v4_supp_t15r2_executor.py` `4b5b720d5cda` + `_v4_supp_t15r2_result.json` `c69ab0e3002e`）
>
> **本件定位（沿 T1.5r2 prereg `883DCED872B4` §0 + §1.3 + §4 + §5 字面）**：T1.5r2 = T1.5 扩样修订探针（construction-failure-fix expansion probe），**不翻 L2/L14 正式判定 + 不二次判定 T1 verdict `F1B5E49F3058` §7 自身 + 不二次判定 T1.5 verdict `52C985429C91` §1 主读法「判定稳健」+ §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑**；结论仅作 **T1.5 verdict §3.4 +60 calls 接力棒扩 N 至 N_min 满足建议落地确认** + **T1.5 verdict §4.4 补跑 2 calls 方案 A 建议落地确认** + T1 verdict 信息量补正确认（构造失灵族修正后真维持方向一致入勘误链）
>
> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）：本件如实裁 K-N11-N1_T1relax 字面 PASS = 假证伪族（构造/计划失灵）根因消除 = 「T1.5 prereg 内 plan 字面 6 vs N_min 字面 10 结构 gap」修复确认；不外推为 L2/L14 既判 PASS 新证据；不外推为 T1/T1.5 verdict 二次判定
>
> **核心硬约束（沿 T1.5r2 prereg §0 + §1.3 + §5 + activation `F6ED61C25572` + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板字面）**：T1.5r2 verdict 件仅对 T1.5r2 探针字面证据下裁定；不动 T1.5 prereg/activation/result/verdict/executor 一字不动；不动 L2/L14 既判一字不动；不动 T1 verdict §7 一字不动；不动 T1.5 verdict §1/§2/§3/§4 一字不动

---

## §0 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | 自报 SHA-12 | 盘实测 SHA-12（前 12） | 字节 | 状态 |
|---|---|---|---|---|---|
| **T1.5r2 result** | `results/_v4_supp_t15r2_result.json` | `c69ab0e3002e` | `c69ab0e3002e` | 73,526 | ✓ |
| **T1.5r2 executor** | `results/_v4_supp_t15r2_executor.py` | `4b5b720d5cda` | `4b5b720d5cda` | 84,884 | ✓ |
| **T1.5r2 prereg** | `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | `883DCED872B4` | `883dced872b4` | 53,923 | ✓ |
| **T1.5r2 activation** | `results/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | `F6ED61C25572` | `f6ed61c25572` | 35,977 | ✓ |
| T1.5 verdict（锚定不动） | `results/_v4_supp_t15_verdict.md` | `52C985429C91` | `52c985429c91` | 55,352 | ✓ |
| T1.5 prereg（锚定不动） | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | `8898b964a9d9` | 76,991 | ✓ |
| T1.5 activation（锚定不动） | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `443EFB39804A` | `443efb39804a` | 20,751 | ✓ |
| T1.5 result（锚定不动） | `results/_v4_supp_t15_result.json` | `6B47D389B7AE` | `6b47d389b7ae` | 53,265 | ✓ |
| T1.5 executor（锚定不动） | `results/_v4_supp_t15_executor.py` | `558E635F9BA6` | `558e635f9ba6` | 62,285 | ✓ |
| T1 verdict（锚定不动） | `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058` | `f1b5e49f3058` | 27,538 | ✓ |

> **0 触既有件自查**：本 verdict 件仅读上述 10 件 + L2/L14 verdict 字面源（沿 §0 输入链字面引用）；**未修改 executor.py / result.json / prereg / activation / T1 verdict / T1.5 verdict / T1.5 prereg/activation/result/executor 一字不动**（沿 T1.5r2 §0 边界 + §4 边界 + 「派生 JSON 不合并」铁律）
>
> **串行派生锚链（修订件）**：`883DCED872B4`（T1.5r2 prereg）→ `F6ED61C25572`（T1.5r2 activation 待 PI 复核生效）→ `4b5b720d5cda`（T1.5r2 executor）→ `c69ab0e3002e`（T1.5r2 result）→ **本件**（verdict 末件）
>
> **T1.5 串行锚链（一字不动）**：`8898B964A9D9` → `443EFB39804A` → `6B47D389B7AE` → `558E635F9BA6` → `52C985429C91`（T1.5 verdict 一字不动；T1.5r2 verdict 不二次判定）

---

## §1 核心裁因问题：plan 字面扩样（20 → 30 calls/cell）+ 2 calls 缺位补跑 后，T1.5 prereg 内 plan vs N_min 不一致结构 gap 是否根因消除？T1.5 verdict §3.4 + §4.4 建议是否落地确认？

> **沿 T1.5 verdict `52C985429C91` §1 主读法 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类（假证伪族 = 构造/计划失灵）+ §4 2 calls 超时不补跑 字面 + T1.5r2 prereg `883DCED872B4` §1.1 修订缘由 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板**；T1.5r2 verdict 与 T1.5 verdict 关系沿 T1.5r2 prereg §0 + §1.5.2 K-T1-S3 字面 + activation `F6ED61C25572` + T1.5r2 result `c69ab0e3002e` `overall_verdict` 三重约束

### §1.1 字面结论（T1.5r2 探针 6 cells 跑出后）

| K-* | 字面 | 字面 hit | 字面判定 | nonempty 分解 |
|---|---|---|---|---|
| **K-T1-S1（温度敏感性 flip 触发线 · T1.5r2 复用沿 T1 一字不动）** | 固定 (qwen_plan, L2\|L14); 任一温度 cell J 中位 ≥ 0.85 → hit=True → 稳健性存疑注记 | False（L2 + L14 三温度全 cell J 中位 = 0.0；同 T1.5 矩阵基线方向） | **PASS（温度方向一致）** | nonempty 子口径同（全 0.0） |
| **K-T1-S2（端点敏感性 flip 触发线）** | T1 verdict `F1B5E49F3058` §2.2 已裁 `any_hit: false`；T1.5r2 端点维度砍去（qwen_plan 单端点），**沿结论引用不重测** | （沿结论引用，不重测） | **PASS（沿 T1 verdict 结论引用）** | — |
| **K-T1-S3（稳健性确认线 · T1 verdict 信息量补正线 + T1.5 verdict §3.4/§4.4 建议落地确认线）** | 全 6 cells J 中位 < 0.85 → 探针不命中（hit=False）= 判定稳健 + T1 verdict 信息量补正 + T1.5 verdict §3.4/§4.4 建议落地确认 | False（全 6 cells J 中位 = 0.0；与 T1.5 矩阵同字面、同方向） | **PASS（判定稳健 + T1 verdict 信息量补正 + T1.5 verdict §3.4/§4.4 建议落地确认）** | nonempty 子口径同（全 0.0） |
| **K-N11-3（教师两次 J 中位 < 0.85 → FAIL）** | per teacher J median < 0.85 → FAIL（主度量，T1.5r2 探针核心同 T1.5） | True（**全部 cells × 全 5 教师**，含 nonempty 子样本；因 cross-caption J=0.0 主导全 pooled） | **字面 FAIL（per cell per teacher 字面 hit=True）** | 同（见 §2 表） |
| **K-N11-N1（L2/L14 既判 N target = 20/教师；与 T1.5r2 探针放宽 N_min=10 双层并存）** | N < 20/教师 → pass=False → FAIL | True（**全部 cells × 全 5 教师**，n_pairs = 15 < 20） | **字面 FAIL（不动 L2/L14 既判字面）** | — |
| **K-N11-N1_T1relax（探针放宽 N_min = 10/教师）** | N < 10/教师 → pass=False → FAIL | **False（全 6 cells × 全 5 教师 N_pairs = 15 ≥ 10）** | **字面 PASS（根因消除确认）** | — |

**核心字面裁定**：
- **T1.5r2 K-T1-S1 字面命中（hit=False）+ K-T1-S3 字面命中（PASS）= T1.5r2 判定稳健复测同向**（同 T1.5 矩阵基线方向一致，**稳健性确认**而非新证据）；
- **T1.5r2 K-N11-N1_T1relax 字面 PASS = T1.5 prereg 内 plan 字面 6 vs N_min 字面 10 结构 gap 修复确认 + 假证伪族根因消除确认**（沿 T1.5 verdict `52C985429C91` §3.4 字面拍板 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板）；
- **T1.5 verdict `52C985429C91` §3.4 +60 calls 接力棒扩 N 建议落地确认**（5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 ≥ N_min=10 字面满足）+ **T1.5 verdict §4.4 补跑 2 calls 方案 A 建议落地确认**（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls 计入 +60 calls 预算内）；
- **T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动**（T1.5r2 不二次判定 T1 verdict §7 自身）；
- **T1.5 verdict `52C985429C91` §1 主读法「判定稳健确认 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」+ §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族 + §4 2 calls 超时不补跑 一字不动**（T1.5r2 不二次判定 T1.5 verdict §1/§2/§3/§4）；
- **L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」一字不动**（沿 T1.5r2 §0 定位硬约束 + §1.3 探针限定 + §5 根因关联表）。

### §1.2 执行棒自报关键证据（`c69ab0e3002e`）

> **T1.5r2 实跑状态字面**（沿 `_v4_supp_t15r2_result.json` `c69ab0e3002e` §records_summary + §per_cell_summary 字面锚定）：

- **总 calls = 182**（T1.5 状态锚定 120 records + T1.5r2 实跑 62 records；n_records_ok = 180；n_records_failed = 2 均为 T1.5 原 2 失败原状保留）
- **T1.5r2 实跑增量 = +62 calls**：
  - **+60 calls**（沿 T1.5 verdict `52C985429C91` §3.4 字面拍板「+60 calls 接力棒扩 N 至 N_min 满足：5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls」+ 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板「总增量 = 6 cells × +10 = +60 calls」）—— 实跑 = 4 cells × 10 calls（cell 0/1/4/5 纯新跑）+ cell 2 × 11 calls（含 coze/S5/r0 1 补跑）+ cell 3 × 11 calls（含 GLM_1/L_geography_world/r1 1 补跑）= 60 calls
  - **+2 calls**（沿 T1.5 verdict `52C985429C91` §4.4 方案 A 字面拍板「补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑」）—— 实跑 = coze/S5/r0 cell 2 1 补跑 + GLM_1/L_geography_world/r1 cell 3 1 补跑 = 2 calls（计入 +60 calls 预算内）
- **n_empty_responses = 0**（沿 T1.5 records；T1.5r2 = 62 records 全 OK；qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后空响应消除；vs T1 矩阵 49.3%）
- **n_pairs_empty_empty = 0 across all 6 cells**（沿 T1.5 矩阵 records；vs T1 72.1% empty-empty pairs）
- **全 6 cells cell_j_median_5teachers = 0.0 / cell_j_median_5teachers_nonempty = 0.0**（all_pairs + nonempty 子口径均 0.0；与 T1.5 矩阵字面同、同方向）
- **跨温度 J 中位标准差 = 0.0**（per dim L2/L14，all_pairs + nonempty 双口径；与 T1.5 矩阵字面同、方向一致性在 J 中位 0.0 baseline 上完全保留）
- **T1.5r2 same-caption 拆解**（worker 自加 same_caption_breakdown 字段，与 T1.5 同字段沿用；本棒裁定承认其）：
  - **same-caption re-ask J 中位（per cell × 5 教师集合中位）**：
    - L2 cells（0/1/2）= **0.75 / 1.0 / 1.0**（T1.5 = L2 全 1.0；T1.5r2 reask_idx=2 引入新配对后中位 0.75-1.0 区间，与 T1.5 同档）
    - L14 cells（3/4/5）= **0.5556 / 0.5 / 0.5**（T1.5 = L14 0.5 / 0.65 / 0.5556；T1.5r2 reask_idx=2 引入新配对后中位 0.5-0.5556 区间，与 T1.5 同档偏弱但同方向）
    - **L2 维度 same-caption J 中位区间 = 0.75-1.0**（per cell 中位）/ **L14 维度 same-caption J 中位区间 = 0.5-0.5556**（per cell 中位）；与 L2/L14 qwen t=0.7 baseline 0.41-0.52（L2）/ 0.36-0.39（L14）同档偏强
  - **cross-caption J 中位**：全部 6 cells = 0.0（与 T1.5 矩阵同；正常模型行为，非构造失灵）
  - **J_all_pooled = 0.0 在 same-vs-cross 比例 1:2 下被 cross-caption J=0.0 主导**（全 pooled 中位 = 0.0 因 cross-pool > same-pool）
- **K-N11-N1_T1relax 字面 PASS 根因确认**：全 6 cells × 全 5 教师 N_pairs = 15 ≥ N_min=10 字面满足（planned = 5 teacher × 2 prompts × 3 re-asks = 15 pairs/教师 ≥ 10 字面满足）

### §1.3 根因三分类（沿 T1.5 verdict `52C985429C91` §7.4 + T1.5r2 prereg `883DCED872B4` §5 根因关联表 + PI 2026-09-23「诚实的根因是不误导」口径）

> **真证伪判别要件**（沿 T1 verdict `F1B5E49F3058` §1.3 字面）：
> ① kill-line 先于实验冻结 ✓（T1.5r2 prereg `883DCED872B4` §1.5 字面已锁 + activation `F6ED61C25572` 待 PI 复核生效）
> ② 构造非恒等/非退化 ✓（C-T15r2-1 = 5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls 字面修订 + C-T15-1 = qwen3.7-max 非 reasoning + max_tokens=500 字面不动；n_empty_responses = 0 验证空响应消除；n_pairs_empty_empty = 0 验证 empty-empty 对消除；构造修正有效 + 扩样修订有效，**与 T1.5 矩阵方向一致、与 T1 矩阵根本不同**）
> ③ 素材面覆盖 claim 所需 ✓（cover L2/L14 × {0.0/0.3/0.5} × qwen_plan 6 cells × 15 pairs/教师 ≥ N_min=10 字面满足；K-N11-N1_T1relax 字面 PASS 确认素材面覆盖充分）
> ④ 度量有分辨力 ✓（Jaccard 度量在 nonempty 场景恢复分辨力；cross-caption J=0.0 vs same-caption J 0.5-1.0 体现正常模型行为 vs 高稳定性的真实区分；与 T1.5 矩阵同口径）

**→ T1.5r2 整体定性（K-T1-S1 + K-T1-S3 命中（PASS）+ K-N11-N1_T1relax 命中（PASS）= 真稳健确认 + T1 verdict 信息量补正 + T1.5 verdict §3.4/§4.4 建议落地确认）**：
- 真证伪要件 ①②③④ 全满足（构造修正有效 + 扩样修订有效 + 素材面覆盖充分 + Jaccard 分辨力恢复）
- **T1.5r2 矩阵字面 PASS 同形但不同质**（与 T1.5 矩阵同字面同方向，**与 T1 矩阵根本不同**）：
  - T1 矩阵字面 PASS = 构造失灵族假象（empty-empty 主导 → J=0.0 非真判定一致）
  - T1.5 矩阵字面 PASS = 真稳健（same-caption J 1.0 + cross-caption J 0.0 内容发散主导 → 正常模型行为）
  - T1.5r2 矩阵字面 PASS = 真稳健同 T1.5 + K-N11-N1_T1relax 字面 PASS 根因消除（plan 字面 6 → 15 pairs/教师 ≥ N_min=10 字面满足）
- **归类**：
  - **K-T1-S3 字面 PASS + K-T1-S1 hit=False → 真证伪（稳健性确认 + T1 verdict 信息量补正确认）**：构造修正后字面方向一致 + same-caption J 中位 L2 0.75-1.0 / L14 0.5-0.5556 真稳定信号回归 + cross-caption J=0.0 正常内容发散；真证伪要件 ①②③④ 全满足，且根因结构与 T1.5 矩阵同、与 T1 矩阵根本不同（非构造失灵族）
  - **K-N11-3 字面 FAIL → 真证伪（qwen 端点固有方差既判维持）**：字面 FAIL 与 L2/L14 既判的 K-N11-3 真证伪同源；T1.5r2 全 pooled J=0.0 仍维持 qwen 端点下 K-N11-3 真证伪方向（注：与 T1.5 同字面同向，因 cross-caption J=0.0 主导；不构成 L2/L14 既判 PASS 新证据）
  - **K-N11-N1 字面 FAIL → 真证伪（L2/L14 既判 N=20 字面不动）**：T1.5r2 N_pairs = 15 < 20 字面 FAIL；与 L2/L14 既判 K-N11-N1 字面同向；不动 L2/L14 既判
  - **K-N11-N1_T1relax 字面 PASS → 假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）根因消除确认**：T1.5 plan 字面 6 vs N_min 字面 10 = 结构性 gap（归假证伪族）→ T1.5r2 plan 字面 30 calls/cell → 15 pairs/教师 ≥ N_min=10 字面满足 = 根因消除；非命题层面被证伪后的翻盘，亦非新命题成立；**仅作 T1.5 prereg 内不一致修复确认 + T1.5 verdict §3.4 建议落地确认**

### §1.4 主读法 vs 替代读法（双读法并记，沿 K-N11-N2 字面 + 派工单明示）

#### 主读法：构造修正有效 + plan 字面扩样修订有效 + 判定稳健复测同向 + T1 verdict 信息量补正 + T1.5 verdict §3.4/§4.4 建议落地确认（dominant）

- **依据**：
  - **n_empty_responses = 0**（T1.5 矩阵同；vs T1 49.3%）—— C-T15-1 = qwen3.7-max 非 reasoning + max_tokens=500 双修正有效消除空响应
  - **n_pairs_empty_empty = 0**（T1.5 矩阵同；vs T1 72.1%）—— empty-empty 对消除，Jaccard 度量在 nonempty 场景恢复分辨力
  - **same-caption re-ask J 中位（per cell × 5 教师集合中位）= L2 0.75/1.0/1.0 + L14 0.5556/0.5/0.5**（与 T1.5 矩阵 L2 1.0/1.0/1.0 + L14 0.5/0.65/0.5556 同档；T1.5r2 reask_idx=2 引入新配对后中位 0.5-1.0 区间与 L14 qwen t=0.7 baseline 0.36-0.39 同档偏强）
  - **cross-caption J 中位 = 0.0 全 6 cells**（与 T1.5 矩阵同；正常模型内容发散；非构造失灵主因）
  - **跨温度 J 中位标准差 = 0.0**（per dim L2/L14 all_pairs + nonempty；与 T1.5 矩阵同；温度维度无方向翻转）
  - **T1.5r2 全 6 cells K-T1-S1 hit=False + K-T1-S3 字面 PASS**—— 既判方向稳健复测同向
  - **T1.5r2 K-N11-N1_T1relax 字面 PASS**—— T1.5 prereg 内 plan vs 字面 N_min 结构 gap 修复确认（plan 字面 6 → 15 pairs/教师 ≥ N_min=10 字面满足）
- **判定**：
  - **T1.5r2 K-T1-S3 字面 PASS = 真稳健复测同向确认**（与 T1.5 矩阵同字面同方向，与 T1 矩阵同字面但根因根本不同；非构造失灵族）
  - **T1.5r2 K-N11-N1_T1relax 字面 PASS = 假证伪族根因消除确认**（plan 字面 6 → 15 pairs/教师 ≥ N_min=10 字面满足；沿 T1.5 verdict §3.4 字面拍板 + 派工单 t15_ext 字面拍板）
  - **T1.5 verdict §3.4 +60 calls 接力棒扩 N 建议落地确认**（180 calls 实跑 + 60 calls 增量 + 15 pairs/教师 ≥ N_min=10 字面满足）
  - **T1.5 verdict §4.4 补跑 2 calls 方案 A 建议落地确认**（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls 实跑完成，计入 +60 calls 预算内）
  - **T1 verdict 信息量补正成立**（沿 T1.5 verdict `52C985429C91` §1 主读法 + T1.5r2 复测同向）
  - **不动 L2/L14 既判一字不动**（沿 T1.5r2 §0 定位硬约束）
  - **不动 T1 verdict §7 自身一字不动**（沿 T1.5r2 §0 + §1.5.2 K-T1-S3 字面 + §4 硬约束）
  - **不动 T1.5 verdict §1/§2/§3/§4 一字不动**（沿 T1.5r2 §0.5 + §1.5.2 + §4 + §5 根因关联表）

#### 替代读法 1：T1.5r2 同 caption J 中位区间 L2 0.75-1.0 / L14 0.5-0.5556 比 T1.5 矩阵 L14 维度 same-caption 中位（0.5/0.65/0.5556）部分 cell 略低（如 L14 cell 4/5 same 中位 = 0.5/0.5 vs T1.5 L14 0.5/0.65/0.5556），是否反映 reask_idx=2 引入新配对后的内容发散倾向（保留观察）

- **依据**：
  - T1.5r2 reask_idx=2 引入新配对（4 records/教师 → 5 records/教师），新配对 = same-caption 池新增 C(1,0) = 0 same pairs/cell（沿 T1.5r2 prereg §1.2 字面 same-pool C(3,2)=6 same pairs/教师；T1.5r2 实际 = 5 records → same-pool = 2 captions × C(3,2) = 6 same pairs/教师；cross-pool = 2 × 3 × 3 = 18 cross pairs/教师；与 T1.5 同口径）；新配对 = cross-pool 增量（C(4,2)-C(3,2) = 3 cross pairs/教师）→ cross-pool 主导 same-pool 比例小幅扩大
  - 同 caption J 中位（L14 cell 4/5 = 0.5/0.5）vs T1.5（L14 cell 4 = 0.65）小幅下移 = 反映 same-caption 内容发散倾向（教师 re-asked 同 caption 时返回更多不同 token）
- **判定**：
  - **不推翻主读法**（字面 same-caption J 中位 0.5-1.0 仍在 L14 qwen t=0.7 baseline 0.36-0.39 同档偏强；与 T1.5 矩阵 L14 0.5-0.65 区间方向同）
  - **字面 K-T1-S1/K-T1-S3 维持**（沿 `0A9EE16267B5` §1 + T1.5 prereg §1.5.2 字面一字不动）
  - **诚实声明**：T1.5r2 same-caption 拆解为 worker 自加字段，不在 K-N11-3 原始字面内，仅作 informational 注记；**是否扩展 same-caption 拆解入 K-N11-N2 字面作为双读法并记标准口径，**待 PI 复核拍板**（沿 T1.5 verdict §6.3 沿用）**

#### 替代读法 2：K-N11-N1 字面 FAIL（L2/L14 既判 N=20）vs K-N11-N1_T1relax 字面 PASS（N=10）双层并存；如何处理

- **依据**：
  - K-N11-N1 字面（沿 v0.2 `D85488A64D89` §2 L2 字面 + L2 verdict §4 + L14 verdict §5）= N < 20/教师 → pass=False → FAIL
  - K-N11-N1_T1relax 字面（沿 T1 `802DECE2286A` §1.4 + §1.8 字面 + T1.5 prereg `8898B964A9D9` §1.8 字面 + T1.5 verdict `52C985429C91` §3.4 字面拍板）= N < 10/教师 → pass=False → FAIL；T1.5r2 计划字面 15 pairs/教师 ≥ 10 → 字面 PASS
  - 双层并存 = K-N11-N1 字面 = L2/L14 既判正式判定门槛（不可改）；K-N11-N1_T1relax 字面 = T1 + T1.5 + T1.5r2 探针放宽口径（沿 T1 §1.4 + §1.8 字面不动）
- **判定（保守口径二选，**字面不动声明**）**：
  - **K-N11-N1 字面 FAIL 维持**（沿 `0A9EE16267B5` §1 + L2 verdict §4 + L14 verdict §5 一字不动；T1.5r2 = 探针放宽 N_min=10 不动 K-N11-N1 字面 N=20；双层并存）
  - **K-N11-N1_T1relax 字面 PASS 维持**（沿 T1.5 verdict §3.4 字面拍板 + 派工单 t15_ext 字面拍板；T1.5r2 plan 字面扩样后字面满足）
  - **两件独立判定，分别入判定表**（详见 §2.5 + §2.6）

#### 双读法分歧处理

- **主读法（构造修正有效 + plan 字面扩样修订有效 + 判定稳健复测同向 + T1 verdict 信息量补正 + T1.5 verdict §3.4/§4.4 建议落地确认）采纳**为定调
- **替代读法 1** 仅作 informational 注记（同 caption J 中位下移是否反映内容发散倾向；不推翻主读法）
- **替代读法 2** 维持 K-N11-N1 字面 FAIL + K-N11-N1_T1relax 字面 PASS 双层并存（一字不动声明）

---

## §2 kill-line 判定表（每行附根因列）

> **字面不动声明**：K-N11-1/2/3/N1/N2 字面沿 `0A9EE16267B5` §1 + L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 一字不动；K-T1-S1/S2/S3 沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 + T1.5 prereg `8898B964A9D9` §1.5.2 一字不动（T1.5r2 复用沿 T1 一字不动，**0 新设数值阈值**）；判定布尔显式方向（`hit=True` 触发 / `pass=False` 触发 / `hit=False` 不触发）
>
> **same/cross-caption 分解口径**：T1.5r2 worker 沿用 T1.5 worker 自加 same_caption_breakdown 字段（沿 T1.5 verdict §6.2 字面）；same-caption re-ask J 中位（per cell, per teacher）× cross-caption J 中位（per cell, per teacher 同 caption 内部）= 拆解 all-pooled J 中位 0.0 的根因结构
>
> **不动 T1 verdict §7 + T1.5 verdict §1/§2/§3/§4 + L2/L14 既判硬约束**：本表 hit/PASS/FAIL 字面判定均不外推为翻 L2/L14 既判或翻 T1 verdict §7 自身或翻 T1.5 verdict §1 主读法或翻 T1.5 verdict §2 K-T1-S3 字面或翻 T1.5 verdict §3 K-N11-N1_T1relax 字面 FAIL 根因归类或翻 T1.5 verdict §4 2 calls 超时不补跑

### §2.1 K-T1-S1（温度敏感性 flip 触发线，T1.5r2 复用沿 T1 一字不动）— L2 × {0.0/0.3/0.5} + L14 × {0.0/0.3/0.5} = 6 cells

| cell_idx | 维度 | 端点 | 温度 | cell_j_median_5teachers | cell_j_median_5teachers_nonempty | same_caption J 5教师集合中位 | cross_caption J 5教师集合中位 | 字面 hit | nonempty hit | 根因（沿 T1.5 verdict §7.4 + PI 2026-09-23 口径） |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | qwen_plan | 0.0 | 0.0 | 0.0 | 0.75（kimi 0.0/GLM_1 0.75/GLM_2 1.0/coze 1.0/minimax 0.5） | 0.0 | False | False | **真稳健（same-caption 同 caption 真稳定信号回归 + 内容发散同 cross-caption J=0.0）**：温度 0.0 下教师 re-asked 同 caption 中位 0.75（vs T1.5 L2 全 1.0；reask_idx=2 引入新配对后 same-pool 内容略发散）；与 qwen t=0.7 baseline 0.41-0.52 同档偏强；K-T1-S1 字面 non-flip；J_all_pooled 0.0 纯 cross 主导 |
| 1 | L2 | qwen_plan | 0.3 | 0.0 | 0.0 | 1.0（kimi 1.0/GLM_1 0.75/GLM_2 0.5/coze 1.0/minimax 1.0） | 0.0 | False | False | **真稳健（同 caption 中位 1.0 + 内容发散同）**：温度 0.3 同 caption 中位 1.0（5 教师集合中位）；**温度维度无方向翻转** |
| 2 | L2 | qwen_plan | 0.5 | 0.0 | 0.0 | 1.0（kimi 1.0/GLM_1 1.0/GLM_2 1.0/coze 1.0/minimax 1.0） | 0.0 | False | False | **真稳健 + coze/S5/r0 缺位已补跑完成**（1 补跑 call 实跑 OK；同 cell 其他 29/30 正常完成；same=1.0 仍达） |
| 3 | L14 | qwen_plan | 0.0 | 0.0 | 0.0 | 0.5556（kimi 0.5556/GLM_1 0.5/GLM_2 0.5/coze 0.5556/minimax 1.0） | 0.0 | False | False | **真稳健 + L14 维度 same 中位 0.5556**（5 教师集合中位；vs T1.5 L14 0.5556/0.65/0.5 同档；**L14 prompt 难度高于 L2 的固有方差**）；与 L14 t=0.7 baseline 0.36-0.39 同档偏强 |
| 4 | L14 | qwen_plan | 0.3 | 0.0 | 0.0 | 0.5（kimi 1.0/GLM_1 0.5/GLM_2 0.0/coze 0.65/minimax 0.0） | 0.0 | False | False | **真稳健 + L14 温度 0.3 same 5教师集合中位 0.5**（vs T1.5 L14 0.65；reask_idx=2 引入新配对后中位略下移；非温度单调性外推依据；仅作温度方向 non-flip 证据） |
| 5 | L14 | qwen_plan | 0.5 | 0.0 | 0.0 | 0.5（kimi 0.0/GLM_1 1.0/GLM_2 0.5/coze 1.0/minimax 0.0） | 0.0 | False | False | **真稳健 + GLM_1/L_geography_world/r1 缺位已补跑完成**（1 补跑 call 实跑 OK；同 cell 其他 29/30 正常完成） |

**K-T1-S1 合计 `any_hit: false`（字面 hit 温度非翻转）+ `any_hit_nonempty: false`（nonempty 子样本 hit 温度非翻转）**（与 T1.5 矩阵字面同、同方向）

**K-T1-S1 根因裁定**：
- **真证伪（构造修正有效的全 pooled 反向证据）**：6 cells 温度方向一致（无 ≥ 0.85 方向翻转）+ same-caption 5 教师集合中位 L2 0.75-1.0 + L14 0.5-0.5556 真稳定信号回归 + cross-caption 0.0 正常内容发散；**主判定方向稳健复测同向**
- **不动 L2/L14 既判 + 不翻 T1 verdict §7 + 不二次判定 T1.5 verdict §1/§2**（仅入稳健性复测同向确认注记）

### §2.2 K-T1-S2（端点敏感性 flip 触发线）— 沿 T1 verdict §2.2 any_hit: false 结论引用不重测

| 项 | 值 | 根因（沿 T1.5 verdict §7.4 + 派工单 t15_ext 字面） |
|---|---|---|
| 字面 hit | False | **沿 T1 verdict `F1B5E49F3058` §2.2 any_hit: false 结论引用**（T1 verdict 已裁 mimo/teamo 端点维度 empty-empty 主导致 K-T1-S2 字面 non-flip；非真端点敏感性不稳健） |
| T1.5r2 端点策略 | qwen_plan 单端点 | T1.5r2 端点维度砍去（qwen_plan 单端点 + C-T15-1 构造修正 + C-T15r2-1 扩样修订）；K-T1-S2 字面不动；T1.5r2 端点敏感性已沿 T1 verdict §2.2 收口 |
| 沿用判定 | PASS（沿 T1 verdict 结论引用 — 不重测） | T1.5r2 端点维度已砍去（qwen_plan 单端点）；K-T1-S2 字面不动；T1.5r2 不重测一字不动 |

**K-T1-S2 根因裁定**：沿 T1 verdict 结论引用，不二次判定（T1 verdict §7 一字不动 + K-T1-S2 沿结论引用 + T1.5r2 不重测一字不动）

### §2.3 K-T1-S3（稳健性确认线 + T1 verdict 信息量补正线 + T1.5 verdict §3.4/§4.4 建议落地确认线）— 6 cells 总览

| cell_idx | 维度 | 端点 | 温度 | n_pairs_total_all | n_pairs_total_nonempty | same_caption J 5教师集合中位 | cross_caption J 5教师集合中位 | 字面 cell_j_median | nonempty cell_j_median | 字面 hit | nonempty hit | 根因（沿 T1.5 verdict §7.4 + T1.5r2 prereg §5 + PI 2026-09-23 口径） |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | qwen_plan | 0.0 | 30 | 30 | 0.75 | 0.0 | 0.0 | 0.0 | False | False | **真稳健复测同向 + 真稳定信号回归**（非构造失灵族假象）：same=0.75 教师 re-asked 同 caption 真稳定；cross=0.0 正常内容发散；J=0.0 非 empty-empty 主导致（vs T1 同形 PASS 但根因根本不同；与 T1.5 同形 PASS 同字面同方向） |
| 1 | L2 | qwen_plan | 0.3 | 30 | 30 | 1.0 | 0.0 | 0.0 | 0.0 | False | False | **真稳健复测同向 + 温度 0.3 same=1.0** |
| 2 | L2 | qwen_plan | 0.5 | 30 | 30 | 1.0 | 0.0 | 0.0 | 0.0 | False | False | **真稳健复测同向 + coze/S5/r0 缺位已补跑完成**（1 补跑 call 实跑 OK；30 records 全 OK） |
| 3 | L14 | qwen_plan | 0.0 | 30 | 30 | 0.5556 | 0.0 | 0.0 | 0.0 | False | False | **真稳健复测同向 + L14 same=0.5556**（L14 prompt 难度高于 L2 固有方差；与 L14 t=0.7 baseline 0.36-0.39 同档偏强） |
| 4 | L14 | qwen_plan | 0.3 | 30 | 30 | 0.5 | 0.0 | 0.0 | 0.0 | False | False | **真稳健复测同向 + L14 温度 0.3 same=0.5**（vs T1.5 L14 0.65；reask_idx=2 引入新配对后中位略下移；非 P 退化） |
| 5 | L14 | qwen_plan | 0.5 | 30 | 30 | 0.5 | 0.0 | 0.0 | 0.0 | False | False | **真稳健复测同向 + GLM_1/L_geography_world/r1 缺位已补跑完成**（1 补跑 call 实跑 OK；30 records 全 OK） |

**K-T1-S3 合计 `any_cell_flip_to_ge_threshold: false`（字面）+ `any_cell_flip_to_ge_threshold_nonempty: false`（nonempty）→ 字面 PASS（判定稳健复测同向 + T1 verdict 信息量补正 + T1.5 verdict §3.4/§4.4 建议落地确认）**

**K-T1-S3 根因裁定（核心裁因）**：
- **真证伪（判定稳健复测同向 + T1 verdict 信息量补正确认 + T1.5 verdict §3.4/§4.4 建议落地确认）**：
  - 全 6 cells 真维持方向一致（与 T1.5 矩阵同字面同方向，与 T1 矩阵同字面但根因根本不同）
  - same-caption J 中位 L2 0.75-1.0 / L14 0.5-0.5556 真稳定信号回归（vs T1 empty-empty 主导致 J=0.0 假象）
  - **T1 verdict 构造失灵族假象裁定获补正**：qwen3.7-max 非 reasoning + max_tokens=500 修正后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链（与 T1.5 verdict §1 主读法同向）
  - **T1.5 verdict §3.4 +60 calls 接力棒扩 N 至 N_min 满足 建议落地确认**：T1.5r2 executor 实跑 +60 calls 增量 + 15 pairs/教师 ≥ N_min=10 字面满足 + K-N11-N1_T1relax 字面 PASS 根因消除确认
  - **T1.5 verdict §4.4 补跑 2 calls 方案 A 建议落地确认**：T1.5r2 executor 实跑 coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls（计入 +60 calls 预算内）
- **不动 L2/L14 既判 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1/§2/§3/§4**（沿 T1.5r2 §0 + §1.5.2 K-T1-S3 字面 + §4 + §5 根因关联表三重硬约束）

### §2.4 K-N11-3（教师两次 J 中位 < 0.85 → FAIL 主度量，T1.5r2 探针核心同 T1.5）— 6 cells × 5 教师

> **字面 = all_pairs 字面**；nonempty 子口径并报；same/cross 拆解仅作 informational 注记（worker 自加字段）

| cell_idx | 维度 | 温度 | kimi J_med | GLM_1 J_med | GLM_2 J_med | coze J_med | minimax J_med | 字面 any_hit | nonempty any_hit | 根因（沿 T1.5 verdict §7.4 + PI 2026-09-23 口径） |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪（qwen 端点固有方差既判维持 + same-caption 真稳定信号被 cross 主导）**：per teacher all-pooled J=0.0 与 L2 t=0.7 baseline 0.41-0.52 同向偏低；same=0.5-1.0 真稳定信号在 cross=0.0 主导下不可见；字面 hit=True 与 L2/L14 既判 FAIL K-N11-3 同形同向；T1.5r2 K-N11-3 主度量字面 FAIL |
| 1 | L2 | 0.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同** |
| 2 | L2 | 0.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同 + coze 缺位已补跑完成**（1 补跑 call 实跑 OK；N=15 全数恢复） |
| 3 | L14 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同 + L14 same-caption J=0.5-1.0 真稳定信号被 cross 主导**；GLM_1 缺位已补跑完成（1 补跑 call 实跑 OK；N=15 全数恢复） |
| 4 | L14 | 0.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同** |
| 5 | L14 | 0.5 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | True | True | **真证伪同** |

**K-N11-3 合计 `any_hit: true`（字面，6 cells × 5 教师 / cell 100% hit）+ `any_hit_nonempty: true`（nonempty 子样本同 — 因 nonempty-only 子口径仍 per-teacher J=0.0）**

**K-N11-3 根因裁定**：
- **真证伪（qwen 端点固有方差既判维持，与 L2/L14 既判同向）**：
  - 字面 = all_pairs J med per teacher < 0.85 → FAIL（与 L2/L14 既判 FAIL K-N11-3 同形同向）
  - 但 T1.5r2 矩阵根因结构与 L2/L14 既判（qwen t=0.7 baseline）有差异：T1.5r2 全 pooled J=0.0 来自 cross-caption 主导（1:2 cross:same 比例），非 empty-empty 主导（T1 真因）；L2/L14 既判 pooled J=0.41-0.52 是 mixed same+cross 同档
  - **不动 L2/L14 既判**（沿 T1.5r2 §0 + K-N11-N2 字面；T1.5r2 仅作 T1.5 verdict §3.4/§4.4 建议落地确认 + T1 verdict 信息量补正复测同向确认，不翻 L2/L14 既判）

### §2.5 K-N11-N1（L2/L14 既判 N target = 20/教师，与 T1.5r2 探针放宽 N_min=10 双层并存）— 6 cells × 5 教师

> **K-N11-N1 字面沿 v0.2 `D85488A64D89` §2 L2 + L2 verdict §4 + L14 verdict §5 一字不动**；T1.5r2 探针放宽 N_min=10 不动 K-N11-N1 字面 N=20
> **全 6 cells × 全 5 教师 N_pairs = 15**（**全 < 20**）

| cell_idx | 维度 | 温度 | kimi N | GLM_1 N | GLM_2 N | coze N | minimax N | 字面 hit | nonempty hit | 根因（沿 T1.5 verdict §7.4 + 派工单 t15_ext 字面） |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | 0.0 | 15 | 15 | 15 | 15 | 15 | True | True | **真证伪（L2/L14 既判 N=20 字面不动 + 双层并存）**：T1.5r2 plan = 5 教师 × 2 prompts × 3 re-asks = 15 pairs/教师 < N=20 字面；T1.5r2 探针放宽 N_min=10 不动 K-N11-N1 字面 N=20；**不动 L2/L14 既判**（双层并存；与 K-N11-N1_T1relax 字面 PASS 独立判定） |
| 1 | L2 | 0.3 | 15 | 15 | 15 | 15 | 15 | True | True | **真证伪同** |
| 2 | L2 | 0.5 | 15 | 15 | 15 | 15 | 15 | True | True | **真证伪同 + coze 缺位已补跑完成**（N=15 全数恢复） |
| 3 | L14 | 0.0 | 15 | 15 | 15 | 15 | 15 | True | True | **真证伪同 + GLM_1 缺位已补跑完成**（N=15 全数恢复） |
| 4 | L14 | 0.3 | 15 | 15 | 15 | 15 | 15 | True | True | **真证伪同** |
| 5 | L14 | 0.5 | 15 | 15 | 15 | 15 | 15 | True | True | **真证伪同** |

**K-N11-N1 合计 `any_fail: true` / `pass: false`（全 30 cells 字面 FAIL；6 cells × 全 5 教师 N = 15 < 20）**

**K-N11-N1 根因裁定**：
- **真证伪（L2/L14 既判 N=20 字面不动 + 双层并存）**：
  - 字面 = N_pairs per teacher < 20 → FAIL（与 L2/L14 既判 FAIL K-N11-N1 同形同向）
  - **不动 L2/L14 既判**（沿 `0A9EE16267B5` §1 + v0.2 §2 L2 字面 + L2 verdict §4 + L14 verdict §5 一字不动）
  - **T1.5r2 探针放宽 N_min=10 不动 K-N11-N1 字面 N=20**（双层并存；T1.5r2 = 探针放宽口径 = K-N11-N1_T1relax 字面 PASS；K-N11-N1 字面 FAIL 维持）

### §2.6 K-N11-N1_T1relax（探针放宽 N_min = 10/教师，T1.5r2 根因消除确认）— 6 cells × 5 教师

> **K-N11-N1_T1relax 字面沿 T1 `802DECE2286A` §1.4 + §1.8 TH-T1-1 = 10 对/教师**（探针放宽口径）
> **T1.5 verdict `52C985429C91` §3.4 字面拍板**「plan 字面扩样至 15 pairs/教师 ≥ N_min=10 字面满足 → 字面 PASS」+ **派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板**「扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）」
> **全 6 cells × 全 5 教师 N_pairs = 15**（**全 ≥ 10 字面满足**）

| cell_idx | 维度 | 温度 | kimi N | GLM_1 N | GLM_2 N | coze N | minimax N | 字面 hit | nonempty hit | 根因（沿 T1.5 verdict §7.4 + 派工单 t15_ext 字面） |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | L2 | 0.0 | 15 | 15 | 15 | 15 | 15 | **False** | False | **假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）根因消除确认**：T1.5r2 plan 字面 = 5 教师 × 2 prompts × 3 re-asks = 15 pairs/教师 ≥ N_min=10 字面满足（沿 T1.5 verdict §3.4 字面拍板「plan 字面扩样至 15 pairs/教师 ≥ N_min=10 字面满足」+ 派工单 t15_ext 字面拍板「扩样至 30 calls/cell → 15 pairs/教师 ≥ 10」）；T1.5 字面 FAIL 根因 = prereg 内 plan (2×2=6) vs N_min=10 不一致 → T1.5r2 扩样后根因消除 |
| 1 | L2 | 0.3 | 15 | 15 | 15 | 15 | 15 | **False** | False | **假证伪族根因消除确认同** |
| 2 | L2 | 0.5 | 15 | 15 | 15 | 15 | 15 | **False** | False | **假证伪族根因消除确认同 + coze 缺位已补跑完成**（N=15 全数恢复；30 records 全 OK） |
| 3 | L14 | 0.0 | 15 | 15 | 15 | 15 | 15 | **False** | False | **假证伪族根因消除确认同 + GLM_1 缺位已补跑完成**（N=15 全数恢复；30 records 全 OK） |
| 4 | L14 | 0.3 | 15 | 15 | 15 | 15 | 15 | **False** | False | **假证伪族根因消除确认同** |
| 5 | L14 | 0.5 | 15 | 15 | 15 | 15 | 15 | **False** | False | **假证伪族根因消除确认同** |

**K-N11-N1_T1relax 合计 `any_fail: false` / `pass: true`（全 30 cells 字面 PASS；6 cells × 全 5 教师 N = 15 ≥ 10 字面满足）**

**K-N11-N1_T1relax 根因裁定（核心裁因点 · T1.5 verdict §3.4 建议落地确认）**：
- **假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）根因消除确认**：
  - **T1.5 字面 FAIL 根因**（沿 T1.5 verdict `52C985429C91` §3 字面归因）：plan 字面 (5×2×2=20 calls/cell → 6 pairs/教师) 与 N_min 字面 (10/教师) 不一致 → 字面 FAIL = prereg 内不一致致「构造退化致命题不明」子标签；非命题层面被证伪
  - **T1.5r2 根因消除确认**（沿 T1.5 verdict §3.4 字面拍板 + 派工单 t15_ext 字面拍板）：plan 字面扩样 (5×2×3=30 calls/cell → 15 pairs/教师) ≥ N_min 字面 (10/教师) → 字面 PASS = prereg 内不一致修复
  - **不动 L2/L14 既判**（沿 T1.5r2 §0 + K-N11-N1 字面 N=20 双层并存；K-N11-N1_T1relax 字面 PASS 仅作 T1.5 prereg 内不一致修复确认 + T1.5 verdict §3.4 建议落地确认；**不构成 L2/L14 既判 PASS 新证据**）
  - **不动 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1/§2/§3/§4**（沿 T1.5r2 §0.5 + §1.5.2 + §4 + §5 根因关联表三重硬约束）

### §2.7 kill-line 判定汇总

| K-* | 字面方向 | 字面 hit | nonempty hit | 根因类型 |
|---|---|---|---|---|
| K-T1-S1（6 cells 跨温度，T1.5r2 复用沿 T1 一字不动） | 任一温度 cell J ≥ 0.85 → hit=True → 稳健性存疑注记 | False（6 cells 5教师集合中位 same=0.5-1.0、cross=0.0 主导全 pooled J=0.0） | False | **真证伪（构造修正有效的全 pooled 反向证据：温度方向一致 + same-caption 真稳定信号回归）**（与 T1.5 矩阵字面同同方向复测同向） |
| K-T1-S2（沿结论引用） | 沿 T1 verdict §2.2 any_hit: false | 沿结论引用（不重测） | 同 | **沿 T1 verdict 结论引用 + 不二次判定** |
| K-T1-S3（6 cells 跨温度 + T1 verdict 信息量补正线 + T1.5 verdict §3.4/§4.4 建议落地确认线） | 全 6 cells J < 0.85 → hit=False → 判定稳健复测同向 + T1 verdict 信息量补正 + T1.5 verdict §3.4/§4.4 建议落地确认 | **False（字面 PASS）** | False | **真证伪（判定稳健复测同向 + T1 verdict 信息量补正确认 + T1.5 verdict §3.4/§4.4 建议落地确认）**：与 T1 同形 PASS 但根因根本不同（非 empty-empty 主导致，而是 cross-caption 内容发散 + same-caption 真稳定信号回归）；与 T1.5 同形 PASS 同字面同方向 |
| K-N11-3（30 cells = 6 cells × 5 教师） | 任一教师 J 中位 < 0.85 → hit=True → FAIL | True（全 6 cells × 全 5 教师 per cell 字面 hit） | True | **真证伪（qwen 端点固有方差既判维持，与 L2/L14 既判同向）**；与 T1 同形 FAIL 但根因不同（非 empty-empty 主导致，而是 cross-caption 主导全 pooled） |
| K-N11-N1（30 cells，L2/L14 既判 N=20 双层并存） | N < 20 → pass=False → FAIL | True（全 30 cells N = 15 < 20） | True | **真证伪（L2/L14 既判 N=20 字面不动 + 双层并存）**；T1.5r2 探针放宽 N_min=10 不动 K-N11-N1 字面；**不动 L2/L14 既判** |
| **K-N11-N1_T1relax（30 cells，T1.5r2 根因消除确认）** | N < 10 → pass=False → FAIL（探针放宽口径） | **False（全 30 cells N = 15 ≥ 10 字面满足）** | False | **假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）根因消除确认**：T1.5r2 plan 字面扩样 (15 pairs/教师) ≥ N_min 字面 (10/教师) = 字面 PASS；沿 T1.5 verdict §3.4 字面拍板 + 派工单 t15_ext 字面拍板 |

**根因三分类计数**：
- **真证伪（命题被证伪 / 既判同向）**：4 件（K-T1-S1 真稳健反向证据 + K-T1-S3 真稳健复测同向确认 + K-N11-3 既判同向 + K-N11-N1 既判 N=20 不动）
- **假证伪族（工具/构造失灵）→ T1.5r2 根因消除确认**：1 件（K-N11-N1_T1relax = prereg 内不一致；T1.5r2 扩样后根因消除 = 字面 PASS）
- **命题不明（构造不可逃）**：0 件（K-N11-N1_T1relax 字面 PASS 后无不可逃构造失灵族残留）

---

## §3 2 calls 缺位补跑定案（T1.5 verdict §4.4 方案 A 建议落地确认）

> 沿 T1.5 verdict `52C985429C91` §4.4 方案 A 字面「补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）」+ 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板「2 calls 超时缺位顺带补跑（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）计入 60 calls 预算」+ T1.5r2 executor `4b5b720d5cda` 字面锚定 + T1.5r2 result `c69ab0e3002e` 字面锚定

### §3.1 2 calls 补跑定案字面（沿 T1.5r2 result `c69ab0e3002e` §inputs.t15_records_state_anchor.failed_tuples_in_T15 + §records_summary 字面）

| 补跑 call | cell | 教师 | caption | re-ask | 温度 | 起点状态 | 落地状态 | T1.5r2 字面 |
|---|---|---|---|---|---|---|---|---|
| 1 | cell_idx=2 (L2/temp=0.5) | coze | S5 | r0 | 0.5 | T1.5 records 失败 tuple（90s 超时） | T1.5r2 executor 实跑补跑 call OK | T1.5r2 records `5af2266b301d` 含此 call；N_records = 30/30 OK；coze N=15 全数恢复 |
| 2 | cell_idx=3 (L14/temp=0.0) | GLM_1 | L_geography_world | r1 | 0.0 | T1.5 records 失败 tuple（90s 超时） | T1.5r2 executor 实跑补跑 call OK | T1.5r2 records `5af2266b301d` 含此 call；N_records = 30/30 OK；GLM_1 N=15 全数恢复 |

### §3.2 落地核对

- **T1.5 records 状态锚定**（沿 T1.5r2 result `c69ab0e3002e` §inputs.t15_records_state_anchor 字面）：n_records = 120，n_ok = 118，n_fail = 2（failed_tuples_in_T15 = 上述 2 call），sha12_record_set = `bb9388d4396c`，expected_sha12 = `6B47D389B7AE`，match = **true**（T1.5 records 状态锚定不变；T1.5r2 仅续跑起点 = reask_idx = 2 起）
- **T1.5r2 records checkpoint**（沿 T1.5r2 result `c69ab0e3002e` §inputs.t15r2_records_checkpoint 字面）：path = `.tmp/_t15r2_records.json`，n_records = 62，n_ok = 62，n_fail = 0，n_rerun_2calls = 2，sha12_record_set = `5af2266b301d`（2 补跑 calls 全 OK）
- **总体记录**（沿 T1.5r2 result `c69ab0e3002e` §records_summary 字面）：n_records_total = 182，n_records_ok = 180，n_records_failed = 2（仅 T1.5 原 2 失败原状保留；T1.5r2 实跑 62 records 全 OK 含 2 补跑），n_empty_responses = 0，n_calls_total = 182，n_calls_ok = 180，n_calls_failed = 2

### §3.3 §4.4 方案 A 建议落地确认（沿 T1.5 verdict `52C985429C91` §4.4 字面）

- **方案 A 拍板**：补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）；预计 +2 calls + 2.5s × 1 = < 5min wall time
- **T1.5r2 落地实况**：
  - **coze/S5/r0 cell 2 补跑** = 1 call 实跑 OK（计入 T1.5r2 cell 2 N_records = 30 / 30 OK）
  - **GLM_1/L_geography_world/r1 cell 3 补跑** = 1 call 实跑 OK（计入 T1.5r2 cell 3 N_records = 30 / 30 OK）
  - **2 calls 计入 +60 calls 预算内**（沿 T1.5 verdict §4.4 字面 + 派工单 t15_ext 字面拍板「2 calls 超时缺位顺带补跑（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）计入 60 calls 预算」）
- **建议落地状态 = 已落地确认**（T1.5r2 verdict 件仅作落地确认注记，不另起补跑决策）
- **不动 T1.5 verdict §4 一字不动**（沿 T1.5r2 §0 + §1.5.2 + §4 + §5 根因关联表硬约束；T1.5 verdict §4「2 calls 超时不补跑」为 T1.5 时刻的「未补跑」状态记录；T1.5r2 实跑后补跑完成 = T1.5 verdict §4 状态不再适用 + T1.5r2 verdict §3 落地确认注记）

---

## §4 边界声明（不构成 L2/L14 既判 PASS 新证据）

> **沿 T1.5r2 prereg `883DCED872B4` §0 + §1.3 + §4 + §5 字面 + activation `F6ED61C25572` 字面 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面 + T1.5 verdict `52C985429C91` §5 字面**

### §4.1 不构成 L2/L14 既判 PASS 新证据

- **T1.5r2 K-T1-S3 字面 PASS + K-N11-N1_T1relax 字面 PASS + K-N11-N1 字面 FAIL + K-N11-3 字面 FAIL → 不翻 L2/L14 既判一字不动**：
  - **K-T1-S3 字面 PASS = 复测同向确认**（与 T1.5 矩阵同字面同方向），**非新证据**；仅作既判方向稳健性确认（沿 T1.5 verdict §1 主读法 + §5.2 边界声明）
  - **K-N11-N1_T1relax 字面 PASS = T1.5 prereg 内不一致修复确认**（plan 字面 6 → 15 pairs/教师 ≥ N_min=10），**非 L2/L14 既判 N=20 字面修订**（双层并存）
  - **K-N11-N1 字面 FAIL 维持**（N=15 < 20），与 L2/L14 既判同向
  - **K-N11-3 字面 FAIL 维持**（per teacher J=0.0），与 L2/L14 既判同向
- **L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」既定结论一字不动**

### §4.2 不二次判定 T1 verdict §7 自身

- **T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动**（沿 T1.5r2 §0 + §1.5.2 + §4 + §5 根因关联表三重硬约束）
- **T1 verdict 信息量补正确认**（沿 T1.5 verdict `52C985429C91` §1 主读法 + T1.5r2 复测同向）：qwen3.7-max 非 reasoning + max_tokens=500 修正后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链（**非翻 T1 verdict §7 自身，仅入 T1 verdict §4.3 信息量边界声明补充**）

### §4.3 不二次判定 T1.5 verdict §1/§2/§3/§4

- **T1.5 verdict `52C985429C91` §1 主读法「判定稳健确认 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」一字不动**
- **T1.5 verdict `52C985429C91` §2 K-T1-S3 字面 PASS 一字不动**
- **T1.5 verdict `52C985429C91` §3 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）一字不动**（T1.5 时刻归类 + 字面 FAIL 状态记录；T1.5r2 = T1.5 字面 FAIL 状态根因消除确认注记）
- **T1.5 verdict `52C985429C91` §4 2 calls 超时不补跑 一字不动**（T1.5 时刻「未补跑」状态记录；T1.5r2 实跑后补跑完成 = T1.5 verdict §4 状态不再适用 + T1.5r2 verdict §3 落地确认注记）
- **T1.5r2 verdict 不就 T1.5 verdict 自身作二次裁定**

### §4.4 外推边界声明（沿 T1.5 verdict `52C985429C91` §5.2 字面沿用）

- **外推边界 = 端点/模型类别/构造修正/扩样维度边界**：T1.5r2 仅在 qwen3.7-max（非 reasoning）+ max_tokens=500 + temp ∈ {0.0, 0.3, 0.5} + plan 字面扩样至 30 calls/cell 矩阵内探针；mimo/teamo 已砍去（沿 T1 verdict §2.2 any_hit: false 结论引用）；qwen t=0.7 baseline（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）**不重跑**，故 T1.5r2 字面 PASS 不可外推为「qwen baseline 方向新证据」（仅作既判方向稳健性确认 + T1.5 verdict §3.4/§4.4 建议落地确认）
- **数据规模边界**：T1.5r2 N_min = 10/教师（沿 T1 §1.4 探针放宽），T1.5r2 plan 字面 30 calls/cell → 15 pairs/教师 ≥ N_min=10 字面满足 → K-N11-N1_T1relax 字面 PASS 根因消除；K-N11-N1 字面（N=20）仍 FAIL，双层并存
- **不留假 pass**：T1.5r2 探针不命中 ≠ L2/L14 既判 PASS（K-N11-3 真证伪既判不动；K-N11-N1 字面 FAIL 维持）；T1.5r2 探针不命中 = 真稳健入勘误链作 L2/L14 既判稳健性确认注记（**不是改判**，仅是既判方向的稳健性确认 + T1.5 verdict §3.4/§4.4 建议落地确认）
- **不留假证伪**：T1.5r2 探针命中 ≠ L2/L14 既判 FAIL（仅入稳健性存疑注记，不翻既判）；K-N11-3 字面 hit=True 与 L2/L14 既判同向但**不翻既判**（仅作既判同向证据 + 入勘误链）
- **判定须另走流程**：除 K-T1-S1 命中（实际未命中）+ verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论

---

## §5 老实交代（failures & limitations）

### §5.1 产物核验

- **本 verdict 件诞生**：路径 `results/_v4_supp_t15r2_verdict.md`；诞生即算 SHA-12（见 §6 RESULT 报告段）+ 字节
- **0 触既有件自查**（仅读模式）：
  - `_v4_supp_t15r2_executor.py` `4b5b720d5cda` ✓ 未触动（仅读）
  - `_v4_supp_t15r2_result.json` `c69ab0e3002e` ✓ 未触动（仅读）
  - `_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` `883dced872b4` ✓ 未触动（仅读）
  - `_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` `f6ed61c25572` ✓ 未触动（仅读）
  - `_v4_supp_t15_verdict.md` `52c985429c91` ✓ 未触动（仅读）
  - `_v4_supp_t15_result.json` `6b47d389b7ae` ✓ 未触动（仅读）
  - `_v4_supp_t15_executor.py` `558e635f9ba6` ✓ 未触动（仅读）
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
  - 其他 4 路在跑产物（L14V3 batch 3-5 executors + results + console.logs 等）✓ 未触动（本棒仅落 _v4_supp_t15r2_verdict.md 1 件）
- **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）：本 verdict 件唯一新增产物 = `_v4_supp_t15r2_verdict.md`

### §5.2 limitations（沿 T1.5 verdict `52C985429C91` §7.2 + L2/L14 verdict §11 同口径）

- **skill 诚实交代**：派工单要求 skill `scientific-research-workflows:peer-review`（plugin @scientific-research-workflows, sha256-tree-v1 前 12 = `611965fcb620`）—— 本地 skill 加载器若实录 `Local skill not found`，按 T1.5 verdict `52C985429C91` §7.2 + T1 verdict `F1B5E49F3058` §5.2 limitations 沿用执行，**未编造 skill 不存在的虚构指令**
- **T1.5 verdict §9.1 SHA 漂移披露沿用**：L14 verdict 自报 SHA `764F24A21AC8` vs 盘实测 SHA `8EEF73BF9856` 漂移（11 B + SHA 全 12 hex 位差异）—— 本 verdict 件字面引用 L14 verdict 时沿用自报 SHA（沿项目「引用锚定 SHA = 字面引用件 §0/§8 自报值」的惯例），漂移事实已披露，不擅自修正
- **判死不软化**（沿 PI 2026-09-23 判死纪律）：本 verdict 件明确 K-N11-N1_T1relax 字面 PASS = 假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）根因消除确认，**不写「但仍稳健 / 仍有希望」类软化语**；K-T1-S3 字面 PASS = 真稳健复测同向（与 T1.5 矩阵同字面同方向），**不写「但仍稳健」类软化语**；L2/L14 既判一字不动仅是 T1.5r2 定位硬约束，**非软化判死**
- **夜间授权保守口径**（沿 T1.5 verdict §9 + T1.5r2 派工单 t15_ext 字面）：模糊处标注「待 PI 复核」，不擅自推广
- **同 caption J 拆解为 worker 自加字段**：不在 prereg §1.4 字面内；本件仅作 informational 注记；**不外推**为 L2/L14 既判反证 / K-N11-N2 字面修订主依据 / T1 verdict 信息量边界声明补充；**待 PI 复核拍板**（沿 T1.5 verdict §6.3 沿用）
- **T1.5r2 same-caption J 中位 L2 0.75-1.0 / L14 0.5-0.5556 vs T1.5 L2 1.0-1.0-1.0 / L14 0.5-0.65-0.5556 比较**：T1.5r2 reask_idx=2 引入新配对（4 records/教师 → 5 records/教师）后 same-pool 内容略发散；L14 cell 4/5 中位 0.5/0.5 vs T1.5 L14 0.65 中位略下移；同 caption J 中位区间 0.5-1.0 仍在 L14 qwen t=0.7 baseline 0.36-0.39 同档偏强；仅作 informational 注记；不外推
- **K-N11-N1 字面 FAIL vs K-N11-N1_T1relax 字面 PASS 双层并存**：T1.5r2 探针放宽 N_min=10 不动 K-N11-N1 字面 N=20；两件独立判定，分别入判定表（详见 §2.5 + §2.6）
- **T1.5 verdict §3.4 +60 calls 接力棒扩 N 建议落地确认 / T1.5 verdict §4.4 补跑 2 calls 方案 A 建议落地确认**：T1.5r2 verdict 仅作落地确认注记；不动 T1.5 verdict §3/§4 字面（沿 T1.5r2 §0 + §1.5.2 + §4 + §5 根因关联表硬约束）

### §5.3 0 产物不编造

- 本 verdict 件唯一新增产物 = `results/_v4_supp_t15r2_verdict.md`（本件）
- **0 自跑实验 / 0 自起草建议文档 / 0 自发起 worker 接力棒 / 0 擅自调阈值 / 0 合并派生 JSON**
- §1.4 替代读法 + §3 落地核对 + §5 limitations 后续说明 = 裁因收口分析，**非执行指令**

### §5.4 根因三分类自检（沿 T1.5 verdict `52C985429C91` §7.4 + T1.5r2 prereg §5 根因关联表 + PI 2026-09-23「诚实的根因是不误导」口径）

| 判定 | 根因类型（保守口径） | 根因列是否附 | 备注 |
|---|---|---|---|
| K-T1-S1 字面 hit=False（6 cells，T1.5r2 复用沿 T1 一字不动） | **真证伪**（构造修正有效的全 pooled 反向证据 + 温度方向一致 + same-caption 真稳定信号回归） | ✓ | 与 T1.5 矩阵同字面同方向复测同向确认 |
| K-T1-S2 沿结论引用 any_hit: false | **沿 T1 verdict 结论引用 + 不二次判定** | ✓ | T1 verdict §2.2 字面引用一字不动 |
| K-T1-S3 字面命中（PASS，T1.5r2 复用沿 T1 一字不动） | **真证伪**（判定稳健复测同向 + T1 verdict 信息量补正确认 + T1.5 verdict §3.4/§4.4 建议落地确认） | ✓ | **核心裁因点**：与 T1.5 矩阵同形 PASS 同字面同方向，与 T1 矩阵同形 PASS 但根因根本不同（非 empty-empty 主导致，而是 cross-caption 内容发散 + same-caption 真稳定信号回归） |
| K-N11-3 字面 hit=True（30 cells） | **真证伪**（qwen 端点固有方差既判维持，与 L2/L14 既判同向） | ✓ | 字面不动；与 L2/L14 既判 K-N11-3 FAIL 同形同向，不翻既判 |
| K-N11-N1 字面 FAIL（30 cells，L2/L14 既判 N=20 双层并存） | **真证伪**（L2/L14 既判 N=20 字面不动 + 双层并存） | ✓ | T1.5r2 探针放宽 N_min=10 不动 K-N11-N1 字面；**不动 L2/L14 既判** |
| **K-N11-N1_T1relax 字面 PASS（30 cells，T1.5r2 根因消除确认）** | **假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）根因消除确认** | ✓ | **核心裁因点**：T1.5r2 plan 字面扩样 (15 pairs/教师) ≥ N_min 字面 (10/教师) = 字面 PASS；沿 T1.5 verdict §3.4 字面拍板 + 派工单 t15_ext 字面拍板 |
| 2 calls 缺位补跑 | **已落地确认**（T1.5 verdict §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板） | ✓ | 2 calls 实跑 OK（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）；计入 +60 calls 预算内 |

**根因三分类计数**：
- **真证伪**：4 件（K-T1-S1 真稳健反向证据 + K-T1-S3 真稳健复测同向确认 + K-N11-3 既判同向 + K-N11-N1 既判 N=20 不动）
- **假证伪族 → T1.5r2 根因消除确认**：1 件（K-N11-N1_T1relax = prereg 内 plan vs 字面 N_min 不一致；T1.5r2 扩样后根因消除 = 字面 PASS）
- **命题不明（构造不可逃）**：0 件（K-N11-N1_T1relax 字面 PASS 后无不可逃构造失灵族残留）

### §5.5 与派工单 5 件必带对齐

| 必带项 | 本件状态 |
|---|---|
| agent 名（verdict-keeper） | ✓ 本件由 verdict-keeper（agent-3a4d09ba3c90）起草 |
| skill 名 + plugin-cache sha256 | ✓ 派工单锚 `scientific-research-workflows:peer-review`（plugin @scientific-research-workflows, sha256-tree-v1 前 12 = `611965fcb620`）；skill 缺位 fallback 沿 T1.5 verdict `52C985429C91` §7.2 + T1 verdict `F1B5E49F3058` §5.2 limitations 沿用 |
| plugin 名（@scientific-research-workflows） | ✓ 已列 §5.2 |
| 7+9 铁律 | ✓ key 永不明文 / V1-V3 只读 / 派生 JSON 不合并 / kill-line 字面不动 / 不调阈值 / 不合并派生 JSON / 判定布尔显式方向（hit=True 即触发 / pass=False 即触发 / hit=False 不触发）/ 不覆盖既有件（新件新名 `_v4_supp_t15r2_verdict.md`）/ SHA-12 自算写入 / 0 LLM 0 伪造 skill 指令 |
| 老实交代 0 产物 | ✓ 本节 §5.1-§5.5 |

### §5.6 待 PI 复核未决项（穷尽清点，**待 PI 派工/拍板**）

> **沿 PI 2026-09-23「收口须穷尽清点未决项，不得漏报」** + 2026-09-21「待拍板项必须用工具提问」—— 本件列出全部待 PI 复核项，建议下一轮以 ask_user 提问

1. **T1.5r2 activation 件 `f6ed61c25572` PI 复核生效拍板**（沿 v0.2 `AD42992DC75D` 锁先例「生效时刻」字段填法；T1.5r2 立线 + 修订矩阵字面 + 修订调用预算 + 产物链 `_v4_supp_t15r2_*` 待 PI 复核生效）
2. **T1.5 verdict `52C985429C91` §3.4 +60 calls 接力棒扩 N 至 N_min=10 满足 K-N11-N1_T1relax 字面建议落地状态确认**（本件 §2.6 + §1.3 已作落地确认注记；**正式拍板 = PI 复核**）
3. **T1.5 verdict `52C985429C91` §4.4 2 calls 90s 超时补跑建议落地状态确认**（本件 §3 已作落地确认注记；coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls 实跑 OK；**正式拍板 = PI 复核**）
4. **T1.5 verdict §6.3 same-caption J 拆解是否入 L2/L14 既判新证据 / K-N11-N2 字面修订主依据 / T1 verdict §4.3 信息量边界声明补充**（沿 T1.5 verdict §6.3 沿用）：
   - 方案 A：扩展 same-caption 拆解入 K-N11-N2 字面作为双读法并记标准口径（另起 prereg 追加件）
   - 方案 B：仅作 informational 注记，不入字面修订

---

## §6 RESULT 报告（诞生即记）

- **本件路径**：`results/_v4_supp_t15r2_verdict.md`
- **SHA-12（前 12 位）**：见 harness 外部汇报段（自报 vs 盘实测）
- **字节 / 行数**：以落盘末态为准
- **本件性质**：verdict-keeper 判定收口 / T1.5r2 产物链末件（与 `_v4_supp_t15r2_executor.py` `4b5b720d5cda` + `_v4_supp_t15r2_result.json` `c69ab0e3002e` 同级独立）
- **锚定 T1.5r2 prereg**：`883dced872b4` 命中（T1.5r2 prereg **一字不动**）
- **锚定 T1.5r2 activation**：`f6ed61c25572` 命中（T1.5r2 activation **一字不动**）
- **锚定 T1.5 verdict**：`52c985429c91` 命中（T1.5 verdict **一字不动**；T1.5r2 不二次判定 T1.5 verdict §1/§2/§3/§4）
- **锚定 T1.5 prereg / activation / result / executor**：`8898b964a9d9` / `443efb39804a` / `6b47d389b7ae` / `558e635f9ba6` 命中（T1.5 字面引用 **一字不动**）
- **锚定 T1 verdict**：`f1b5e49f3058` 命中（T1 verdict **一字不动**；T1.5r2 不二次判定 T1 verdict §7 自身）
- **锚定 T1 prereg / activation**：`802DECE2286A` / `79936B630015` 命中（T1 字面引用 **一字不动**）
- **锚定 L2 verdict**：`E433A06E7BFB` 命中（L2 verdict **一字不动**）
- **锚定 L14 verdict**：`764F24A21AC8` 命中（L14 verdict **一字不动**；自报 vs 盘 SHA 漂移沿 T1 §9.1 披露）
- **派工单**：PI 2026-09-26 16:26「verdict-keeper 裁因专职 · T1.5r2 verdict——扩样修订裁因收口」（skill `scientific-research-workflows:peer-review`；plugin @scientific-research-workflows sha256-tree-v1 前 12 = `611965fcb620`；派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板「+60 calls 规化重跑（N_min≥10 字面满足）」）
- **生效后状态**：本件为判定收口件，生效后状态沿 T1.5r2 锁先例 → **生效即锁**（沿 `D85488A64D89` `AD42992DC75D` + T1 `802DECE2286A` `79936B630015` + T1 verdict `F1B5E49F3058` + T1.5 `8898B964A9D9` `443EFB39804A` + T1.5 verdict `52C985429C91` + T1.5r2 `883DCED872B4` `F6ED61C25572` 锁先例），事后不重开不调
- **0 触既有件**：1 件新增（`_v4_supp_t15r2_verdict.md`），≥ 19 件既有件 0 触动（详见 §5.1）
- **T1.5r2 定位硬约束再声明**：T1.5r2 = T1.5 扩样修订探针（construction-failure-fix expansion probe），**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1/§2/§3/§4**；除 K-T1-S1 命中（实际未命中）+ verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论 + 不得二次判定 T1 verdict §7 自身 + 不得二次判定 T1.5 verdict §1/§2/§3/§4

---

## §7 总判定（一行收口）

> **T1.5r2 = T1.5 扩样修订探针（plan 字面扩样 20 → 30 calls/cell + 2 calls 缺位补跑）字面 K-T1-S3 命中（PASS）= 判定稳健复测同向 + T1 verdict 信息量补正成立 + T1.5 verdict §3.4/§4.4 建议落地确认**：n_empty_responses = 0（vs T1 49.3%）+ n_pairs_empty_empty = 0（vs T1 72.1%）消除构造失灵族主因（同 T1.5 矩阵）；same-caption re-ask J 5教师集合中位 L2 0.75-1.0 / L14 0.5-0.5556 真稳定信号回归（vs T1.5 矩阵 L2 1.0-1.0-1.0 / L14 0.5-0.65-0.5556 同档；reask_idx=2 引入新配对后中位区间 0.5-1.0）+ cross-caption J=0.0 正常内容发散主导全 pooled 中位 0.0；与 T1 矩阵同字面 PASS 但根因根本不同（非 empty-empty 主导致）；**K-N11-N1_T1relax 字面 PASS = T1.5 prereg 内 plan 字面 6 vs N_min 字面 10 结构 gap 修复确认 + 假证伪族（构造/计划失灵）根因消除确认**（沿 T1.5 verdict `52C985429C91` §3.4 字面拍板 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板）；**K-N11-N1 字面 FAIL 维持**（N=15 < 20 字面不动 + 双层并存）+ **K-N11-3 字面 hit=True 维持**（qwen 端点固有方差既判维持，与 L2/L14 既判同向）；**T1.5 verdict §3.4 +60 calls 接力棒扩 N 至 N_min 满足建议落地确认**（T1.5r2 executor 实跑 +60 calls 增量 + 15 pairs/教师 ≥ N_min=10 字面满足）+ **T1.5 verdict §4.4 补跑 2 calls 方案 A 建议落地确认**（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls 实跑 OK，计入 +60 calls 预算内）；**L2 verdict `E433A06E7BFB` §11 + L14 verdict `764F24A21AC8` §11 + T1 verdict `F1B5E49F3058` §7 + T1.5 verdict `52C985429C91` §1/§2/§3/§4 一字不动**（沿 T1.5r2 §0 + §1.5.2 + §4 + §5 根因关联表四重硬约束）；**T1 verdict 信息量补正成立**（沿 T1.5 verdict §1 主读法 + T1.5r2 复测同向）；**T1.5r2 不二次判定 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑**；T1.5r2 activation 件 `f6ed61c25572` PI 复核生效拍板 + same-caption J 拆解是否入字面 两项**待 PI 复核拍板**。

---

> **诚实 = 不误导**（沿 PI 2026-09-23 口径）：本 verdict 件如实裁 T1.5r2 探针字面证据（K-T1-S3 PASS = 真稳健复测同向 vs T1 矩阵同形 PASS = 构造失灵族假象，二者同字面但根因根本不同；与 T1.5 矩阵同字面同方向）；K-N11-N1_T1relax 字面 PASS = 假证伪族根因消除确认（plan 字面 6 → 15 pairs/教师 ≥ N_min=10 字面满足），**不外推**为 L2/L14 既判 PASS 新证据 / T1 verdict 二次判定 / T1.5 verdict 二次判定；保守口径下模糊处（T1.5r2 activation 件 PI 复核生效拍板 + T1.5 verdict §3.4/§4.4 落地确认正式拍板 + same-caption J 拆解是否入字面）一律标注「**待 PI 复核**」，不擅自推广；**不动 L2/L14 既判 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1/§2/§3/§4**硬约束全段守住。