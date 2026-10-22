# V4 T1.5r2 追加件生效留痕（draft，2026-09-26，待 PI 复核生效）

- **追加件**：`results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md`（T1.5r2 · T1.5 扩样修订 N_min≥10 字面满足规化），SHA-12 见落盘报值（**末态文件 hash = `5841CEBAC094`（96,767 B）**）——**待 PI 复核生效，生效即锁，一字不改**
- **PI 拍板**：待 `ask_T15r2_*` 问卷（PI 2026-09-26 16:26 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板「+60 calls 规化重跑（N_min≥10 字面满足）」——修订定位 = T1.5 prereg §1.4 计划（20 calls/cell → 6 pairs/教师）与 §1.8 N_min=10 字面的结构 gap 修复 + 扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）+ 总增量 = 6 cells × +10 = +60 calls + kill-line 一字不动 + 2 calls 超时缺位顺带补跑（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）计入 60 calls 预算 + 预算/节制 = qwen token-plan 5h 节制 + 串行 ≥2.5s + 600s watchdog 拆批 + 中断-恢复同 agent 唤醒 + 产物链 `_v4_supp_t15r2_*` 系 + T1.5 原件 + result + verdict 一字不动 + 沿 T1.5 verdict `52C985429C91` §3.4「+60 calls 接力棒扩 N 至 N_min 满足：5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls」字面 + §4.4 方案 A「补跑 2 calls」字面）
- **生效时刻**：待 PI 复核生效时填入（沿 `AD42992DC75D` 锁先例「生效时刻」字段填法 + T1.5 `443EFB39804A` 锁先例）
- **T1.5r2 探针定位硬约束**（沿 T1.5r2 §0 + §1.3 + §4 边界声明）：
  - **T1.5r2 = T1.5 扩样修订探针（construction-failure-fix expansion probe）**，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面**
  - 结论仅作**稳健性注记**入勘误链（K-T1-S1 命中）+ **T1 verdict 信息量补正**（K-T1-S3 命中，构造失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认）+ **T1.5 verdict §3.4 + §4.4 建议落地确认**（K-N11-N1_T1relax 字面 PASS 根因消除 + 2 calls 缺位补跑完成）
  - 除 K-T1-S1 命中（方向翻转 = hit=True）**且另走 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程**，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict `F1B5E49F3058` §7 总判定一字不动 + **不得二次判定** T1.5 verdict `52C985429C91` §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS 一字不动
  - L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」既定结论一字不动
  - T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动（T1.5r2 不二次判定 T1 verdict 自身）
  - **T1.5 verdict `52C985429C91` §1 主读法「判定稳健确认 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」+ §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族 + §4 2 calls 超时不补跑 三件裁定一字不动**（T1.5r2 不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑）

---

## T1.5r2 探针字面（沿 T1.5r2 §1.5 + T1.5 prereg §1.5，0 新设数值阈值）

### 既有 K-N11 字面（沿 L2/L14 verdict 一字不动，锁前痕迹保留）

- **K-N11-1**：三方 Jaccard 中位数差异 < K_N11_1_DIFF = 0.05 即 `hit=True` → FAIL（三方不可分离）—— **沿 `0A9EE16267B5` §1 K-N11-1 字面**
- **K-N11-2**：distill J > teacher J + K_N11_2_DELTA = 0.05 不成立即 `hit=True` → FAIL（与原假设反向）—— **沿 `0A9EE16267B5` §1 K-N11-2 字面**
- **K-N11-3**：教师两次 J 中位数 < K_N11_3_THRESHOLD = 0.85 即 `hit=True` → FAIL（教师自身不稳定，主度量失效）—— **沿 `0A9EE16267B5` §1 K-N11-3 字面**（**T1.5r2 探针核心沿此字面**）
- **K-N11-N1**：N < TH17_N_TARGET = 20 / 教师 即 `pass=False` → FAIL（构造退化致命题不明）—— **沿 v0.2 §2 L2 K-N11-N1 字面**（**T1.5r2 探针放宽至 N_min=10** 不动此字面）
- **K-N11-N1_T1relax（探针放宽 N_min = 10/教师）**：N < TH-T1-1 = 10 对/教师 即 `pass=False` → FAIL（沿 T1 `802DECE2286A` §1.8 + T1.5 prereg `8898B964A9D9` §1.8 字面不动）；**T1.5r2 plan 字面扩样后字面 PASS**（沿 T1.5 verdict `52C985429C91` §3.4 字面「plan 字面扩样至 15 pairs/教师 ≥ N_min=10 字面满足」+ 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板）
- **K-N11-N2**：构造面 K-N11-1/2/3 + 真实面 K-N11-1/2/3 **并记**；任一面 PASS ≠ 命题成立（必须双面都过）—— **沿 v0.2 §2 L2 K-N11-N2 字面**

### T1.5r2 复用 K-T1-* 字面（沿 T1 追加件 + T1 verdict 一字不动，0 新设数值阈值）

- **K-T1-S1（温度敏感性 flip 触发线 · 主判定，T1.5r2 复用沿 T1 一字不动）**：
  - **字面**：在 qwen_plan 端点下，沿 L2 维度或 L14 维度，教师 J 中位数跨温度 {0.0, 0.3, 0.5} 中**任一温度点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**（显式布尔）：
    - 既定方向 = qwen t=0.7 baseline 教师 J 中位 < 0.85（沿 L2 verdict `E433A06E7BFB` §3.2 + L14 verdict `764F24A21AC8` §3.2 实测）
    - 翻转条件 = 新 (端点=qwen_plan, 维度=L2|L14, 温度 ∈ {0.0, 0.3, 0.5}) cell 教师 J 中位 ≥ 0.85（**T1.5r2 = qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后 + plan 字面扩样至 30 calls/cell**）
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（沿 L2/L14 verdict + `0A9EE16267B5` §1 + T1 `802DECE2286A` §1.5.2 字面，**0 新设**）
  - **不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法**：K-T1-S1 hit=True 仅入稳健性注记，**不据此改判** L2 verdict `E433A06E7BFB` §11 + L14 verdict `764F24A21AC8` §11 既定结论一字不动；**不二次判定** T1 verdict `F1B5E49F3058` §7 总判定一字不动；**不二次判定** T1.5 verdict `52C985429C91` §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS 一字不动

- **K-T1-S2（端点敏感性 flip 触发线 · 主判定，T1.5r2 沿 T1 verdict 结论引用不重测）**：
  - **T1.5r2 字面**：T1 verdict `F1B5E49F3058` §2.2 K-T1-S2 已裁 `any_hit: false`（端点维度 mimo/teamo × {0.0, 0.3, 0.5} × {L2/L14} 整矩阵方向 J<0.85，empty-empty 主导非真判定一致）；T1.5r2 端点维度砍去（qwen_plan 单端点），**沿 T1 verdict §2.2 any_hit: false 结论引用**，**T1.5r2 不重测 K-T1-S2**
  - **理由**：T1 verdict §4.1【最高优先】建议 = 「改用非 reasoning 模型 + 提高 max_tokens」（沿端点 / 模型类别修正 + max_tokens 修正），不是「改用不同端点」；端点维度在 T1 verdict §2.2 已裁 empty-empty 主导致 K-T1-S2 字面 any_hit: false 系构造失灵族假象（reasoning 模型 + max_tokens=100），非真端点敏感性不稳健；T1.5r2 沿 T1 verdict 结论引用 = 端点维度敏感性判据已沿 T1 verdict 字面收口
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（一字不动）
  - **不翻 L2/L14 正式判定**：同 K-T1-S1

- **K-T1-S3（稳健性确认线 · 副判定 + T1 verdict 信息量补正线 + T1.5 verdict §3.4 + §4.4 建议落地确认线，T1.5r2 复用沿 T1 一字不动）**：
  - **字面**：6 cells 全 J 中位 < 0.85 = 「**判定稳健**」= T1.5r2 探针不命中 K-T1-S1 / K-T1-S2 → 入稳健性确认注记 + **T1 verdict 构造失灵族假象裁定获补正**（qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链作 L2/L14 既判稳健性确认）+ **T1.5 verdict §3.4 + §4.4 建议落地确认**（K-N11-N1_T1relax 字面 PASS 根因消除 + 2 calls 缺位补跑完成）
  - **判定方式**：任一 cell 触发 K-T1-S1 或 K-T1-S2（K-T1-S2 沿 T1 verdict 结论引用）= 探针命中；全 6 cells 不触发 = 探针不命中 + T1 verdict 信息量补正 + T1.5 verdict §3.4 + §4.4 建议落地确认 + K-N11-N1_T1relax 字面 PASS 根因消除确认
  - **T1.5r2 探针与 T1 verdict §7 + T1.5 verdict §1 主读法关系**：
    - T1 verdict §7 总判定一字不动（T1 verdict 自身不可二次判定）
    - T1.5 verdict §1 主读法「判定稳健确认 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」+ §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族 + §4 2 calls 超时不补跑 三件裁定一字不动（T1.5 verdict 自身不可二次判定）
    - T1.5r2 K-T1-S3 命中（探针不命中 K-T1-S1/S2）= **仅作 T1 verdict 信息量补正** + **T1.5 verdict §3.4 + §4.4 建议落地确认**（T1 verdict §4.3 信息量边界声明获补充：构造失灵族修正后真维持方向一致 = 真稳健入勘误链；T1.5 verdict §3.4 补正建议落地确认 + §4.4 补跑建议落地确认）
    - T1.5r2 K-T1-S1 命中 = 仅入稳健性存疑注记，**不翻 T1 verdict §7 自身 + 不翻 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑**

### T1.5r2 探针阈值一览（沿 T1.5 prereg `8898B964A9D9` §3 + T1.5r2 §3，0 新设数值阈值）

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| K_N11_1_DIFF | 0.05 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-1 字面 |
| K_N11_2_DELTA | 0.05 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-2 字面 |
| K_N11_3_THRESHOLD | 0.85 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-3 字面 |
| K_N11_3_THRESHOLD | 0.85 | `_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.5.2 K-T1-S1/S2/S3 字面（T1.5 + T1.5r2 复用沿用） |
| K_N11_3_THRESHOLD | 0.85 | `_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | §1.5.2 K-T1-S1/S2/S3 字面（T1.5r2 复用沿用一字不动） |
| TH-17 N_TARGET | 20 / 教师 | `_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面 |
| **TH-T1-1 N_min** | **10 对/教师**（T1 探针放宽，T1.5 + T1.5r2 沿用） | `_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.4 非退化自证 + §1.8 新增条款 |
| **TH-T1-1 N_min 满足** | **15 pairs/教师 ≥ 10 对/教师**（**T1.5r2 plan 字面扩样后字面满足**） | `_v4_supp_t15_verdict.md` §3.4 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext | `52C985429C91` / — | T1.5 verdict §3.4 字面「5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10」+ t15_ext 派工单字面「扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）」 |
| **C-T15-1 端点 + 模型替换 + max_tokens=500** | qwen_plan + qwen3.7-max（非 reasoning）+ max_tokens ≥ 500 | 派工单 `ask_9484b696` t15 + T1 verdict `F1B5E49F3058` §4.1【最高优先】 | — | 派工单 23:33 拍板 + T1 verdict §4.1 字面（**工具失灵族参数修正**，非阈值调整；T1.5 + T1.5r2 沿用一字不动） |
| **C-T15r2-1 plan 字面扩样修订** | 5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls = +60 calls 总增量 + 15 pairs/教师 ≥ N_min=10 | 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext + T1.5 verdict `52C985429C91` §3.4 | — / `52C985429C91` | t15_ext 派工单字面「扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）；总增量 = 6 cells × +10 = +60 calls」+ T1.5 verdict §3.4 字面（**构造失灵族参数扩展**，非阈值调整） |
| **C-T15r2-2 2 calls 缺位补跑** | coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls 计入 +60 calls 预算 | 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext + T1.5 verdict `52C985429C91` §4.4 方案 A | — / `52C985429C91` | t15_ext 派工单字面「2 calls 超时缺位顺带补跑（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）计入 60 calls 预算」+ T1.5 verdict §4.4 字面「方案 A（推荐）：补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）」（**T1.5 verdict §4.4 方案 A 落地确认**，非阈值调整） |
| **audit-only metadata 字段集** | `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint` | `_v4_supp_l14v3_model_mapping_2026_09_24.md` §1.2 + §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板 | `L14V3_MAP_*` | §1.2 字段表 + §6.1 #2 audit-only 拍板（T1.5r2 沿用同字段集一字不动） |

> **0 新设数值阈值声明（修订件硬约束）**：K-T1-S1/S2/S3 三条**0 新设数值阈值**；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict `E433A06E7BFB` §2 + L14 verdict `764F24A21AC8` §2 + `0A9EE16267B5` §1 + T1 `802DECE2286A` §1.5.2 + T1.5 prereg `8898B964A9D9` §1.5.2 字面一字不动；T1.5r2 探针字面「方向翻转 = hit=True」是布尔条件显式化（沿 S-40 教训「判定布尔显式方向」），**不构成阈值私设**；max_tokens = 500 系**工具失灵族参数修正**（沿 T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + §5.1 工具失灵族假象裁定），**非阈值调整**——沿派工单明示「判定阈值一字不动；max_tokens 属工具失灵族参数修正」；T1.5r2 plan 字面扩样（20 → 30 calls/cell）系**构造失灵族参数扩展**（沿 T1.5 verdict `52C985429C91` §3.4 补正建议字面「构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致」+ 派工单 t15_ext 拍板明示「判定阈值一字不动；扩样 = plan 字面修订」），**非阈值调整**

---

## 锁定范围

> 沿 R5 frozen 只追加 + 锁后不改字面 + 派生 JSON 不合并 + 派工单 t15_ext 字面拍板「T1.5 原件 + result + verdict 一字不动」

- **§0 输入件 SHA-12 链 21 件**（既有 3 件预登记 `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` + v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` + **T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` + T1.5 executor `558E635F9BA6`** + L14V3 追加件 + L14V3 activation + L14V3 映射件 + L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` + L14 verdict `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测）+ L14 result `4C11AB9057B9` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 22 caption `6A2656878745`）—— **21 件一字不动**（沿 T1.5r2 §4 边界声明）
- **§1 T1.5r2 矩阵 6 cells**（{L2, L14} × {temp 0.0/0.3/0.5} × qwen_plan 单端点；6 cells 矩阵与 T1.5 prereg §1.2 一字不动）+ **plan 字面修订 1 字段**（20 → 30 calls/cell = 5 教师 × 2 prompts × **3** re-asks = +60 calls 总增量 = 15 pairs/教师 ≥ N_min=10 字面满足）+ K-N11-1/2/3/N1/N2 字面不动 + **K-N11-N1_T1relax 字面 PASS**（沿 T1.5 verdict §3.4 字面拍板 + 派工单 t15_ext 字面拍板）+ K-T1-S1/S2/S3 沿 T1 字面沿用（0 新设数值阈值）+ TH-T1-1 = 10 对/教师（T1.5 + T1.5r2 沿 T1 沿用）+ C-T15-1 = 端点 + 模型替换 + max_tokens=500（**工具失灵族参数修正**，非阈值调整）+ **C-T15r2-1 = plan 字面扩样修订**（**构造失灵族参数扩展**，非阈值调整）+ **C-T15r2-2 = 2 calls 缺位补跑**（沿 T1.5 verdict §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板，**非阈值调整**）+ audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 拍板
- **§0.5 过渡声明 1 件**：T1.5r2 扩样修订定位过渡（T1.5 verdict §3.4 +60 calls 接力棒扩 N + §4.4 补跑 2 calls 两件建议落地为新立线修订件 + 不动 T1.5 prereg + result + verdict + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑）
- **§5 根因三分类 + T1.5r2 探针与 L2/L14 既判 + T1 verdict §7 + T1.5 verdict §1 主读法的根因关联**（沿拍板 #15 + T1 §5 + T1.5 prereg §5 沿用 + T1.5r2 增量四栏：「不翻 L2/L14 既判」+「不二次判定 T1 verdict §7」+「不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面」+「T1.5 verdict §3.4 + §4.4 建议落地确认」）
- **既有 K-N11-1/2/3/N1/N2 字面锁前痕迹保留**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1 + v0.2 `D85488A64D89` §2 L2 一字不动）
- **既有 K-T1-S1/S2/S3 字面锁前痕迹保留**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 + T1.5 prereg `8898B964A9D9` §1.5.2 一字不动；T1.5r2 复用一字不动，0 新设数值）
- **K-N11-N1_T1relax 字面 FAIL 根因消除**（沿 T1.5 verdict `52C985429C91` §3.4 字面拍板「+60 calls 接力棒扩 N 至 N_min 满足：plan 字面 6 → 15 pairs/教师 ≥ N_min=10 字面满足」+ 派工单 t15_ext 字面拍板）
- **T1.5r2 探针定位硬约束**：T1.5 扩样修订探针，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict §7 总判定一字不动 + **不得二次判定** T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑

---

## 过渡声明 1 件随生效继续有效

- **T1.5r2 扩样修订定位过渡**：自 T1.5r2 件立线起标「**已知 T1.5 verdict `52C985429C91` §1 主读法已裁『判定稳健确认 + T1 verdict 信息量补正成立』；T1.5 verdict §3.4 已拍板『+60 calls 接力棒扩 N 至 N_min 满足』建议（方案 A = 扩 N）；T1.5 verdict §4.4 已拍板『补跑 2 失败 calls』建议（方案 A = 补跑）；T1.5r2 = 该两件建议落地为新立线修订件**」——
  - L2 verdict `E433A06E7BFB` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；t=0.7 实证 J 中位 0.41-0.52 < 0.85）」
  - L14 verdict `764F24A21AC8` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；N=20 收敛稳定 0.36-0.39 区间）」
  - T1 verdict `F1B5E49F3058` §7 总判定 = 「K-T1-S3 字面命中（PASS）= 构造失灵族假象：reasoning 模型 + max_tokens=100 致 49.3% 空响应 + 72.1% empty-empty pairs；J=0.0 主要来自『双方都空』非真判定一致；真证伪要件 ②③④ 失守」
  - T1.5 verdict `52C985429C91` §1 主读法总判定 = 「K-T1-S3 字面命中（PASS）= 真稳健入勘误链 + 构造失灵族修正后真维持方向一致 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」
  - T1.5 verdict `52C985429C91` §3.4 补正建议 = 「+60 calls 接力棒扩 N 至 N_min 满足：5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls；checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）」
  - T1.5 verdict `52C985429C91` §4.4 补正建议 = 「补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）；预计 +2 calls + 2.5s × 1 = < 5min wall time」（方案 A）
  - T1.5r2 = T1.5 prereg §1.4 plan 字面扩样修订件（20 calls/cell → 30 calls/cell = 5 教师 × 2 prompts × 3 re-asks）+ 2 calls 缺位补跑 + 派生独立产物链 `_v4_supp_t15r2_*` + 不动 T1.5 矩阵 / 端点 / 模型 / max_tokens / 温度维度 / kill-line / claim / 阈值字面
  - T1.5r2 命中方向翻转（K-T1-S1 hit=True）= 标注「**T1.5r2 方向翻转稳健性存疑注记**」入勘误链（**仅注记，不翻 L2/L14 既判 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面**）
  - T1.5r2 全 6 cells 不命中（方向一致）= 「**T1.5r2 判定稳健确认**」+ K-N11-N1_T1relax 字面 FAIL 根因消除（plan 字面 30 calls/cell → 15 pairs/教师 ≥ N_min=10 字面满足）= 「**K-N11-N1_T1relax 字面 PASS**」（沿 T1.5 verdict `52C985429C91` §3 假证伪族根因消除）+ T1.5 verdict §3.4 + §4.4 建议落地确认注记
  - **T1.5r2 唯一新增定位** = T1.5 prereg §1.4 plan 字面扩样修订件（plan 字面 20 → 30 calls/cell）；T1.5 prereg + result + verdict + executor 一字不动，T1.5r2 跑出后仅作 T1.5 verdict §3.4 + §4.4 建议落地确认（T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑 一字不动，T1.5r2 不二次判定）
- **本件不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 过渡声明 3 件** + **不动 L10 §0.5 过渡声明 2 件** + **不动 T1 §0.5 过渡声明 1 件** + **不动 T1.5 §0.5 过渡声明 1 件**

---

## 起跑条件（T1.5r2 接力 worker · T1.5 扩样修订 N_min≥10 字面满足规化）

> 沿 T1.5r2 §1.4 + §1.6 启动条件与调用预算 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板

### 6 cells 矩阵执行（worker 接力棒）

- **L2 维度**（沿 L2 verdict `E433A06E7BFB` §2 字面）：
  - **修订**：5 教师 × 2 prompts × **3 re-asks** = **30 calls / cell**
  - 3 cells（L2 × {temp 0.0/0.3/0.5} × qwen_plan）= **90 calls / L2 维度**（含 cell 2 coze/S5/r0 1 补跑 call）
- **L14 维度**（沿 L14 verdict `764F24A21AC8` §2 字面）：
  - **修订**：5 教师 × 2 prompts × **3 re-asks** = **30 calls / cell**
  - 3 cells（L14 × {temp 0.0/0.3/0.5} × qwen_plan）= **90 calls / L14 维度**（含 cell 3 GLM_1/L_geography_world/r1 1 补跑 call）
- **总 cells = 6 cells × 30 calls/cell = 180 calls**（T1.5 prereg §1.6.3「360 calls 硬上限」**0 触**；T1.5r2 修订为 180 calls 上限；T1.5 120 calls 实测 + T1.5r2 +60 calls 增量 = 180 calls 总预算）

### 小→大序列（worker 第 1 棒接力，沿 T1.5 executor `558E635F9BA6` checkpoint 模式续跑）

1. **续跑起点**：T1.5 已跑元组 (teacher, caption_id, reask_idx 0/1, temp) 全部 skip；T1.5r2 续跑起点 = reask_idx = 2 起（沿 L14 runner L107-110 + T1 §1.6.4 + T1.5 prereg §1.6.4 惯例；T1.5r2 端点恒 = qwen_plan，元组 = (teacher, caption_id, reask_idx, temp)）
2. **单 cell sanity check**：L2 维度 × temp=0.0 × qwen_plan = 1 cell × 30 calls（**T1.5r2 续跑第 1 棒先行探活 + 非 reasoning 模型 + max_tokens=500 可行性验证 + plan 字面扩样后 N=15 字面满足可行性验证**）
3. **维度扩展**：L2 维度 × {temp 0.0/0.3/0.5} × qwen_plan = 3 cells × 30 calls（**L2 维度温度敏感性**；含 cell 2 coze/S5/r0 1 补跑 call）
4. **全集**：L14 维度 × {temp 0.0/0.3/0.5} × qwen_plan = 3 cells × 30 calls（**L14 维度温度敏感性**；含 cell 3 GLM_1/L_geography_world/r1 1 补跑 call）

### 单批 calls 上限（看门狗约束）

- **单批 ≤ 30 calls**（沿 L2 verdict §2「600s 看门狗」+ L14 verdict §9.1「sub-batch strategy」+ T1 `802DECE2286A` §1.6.1 + T1.5 prereg `8898B964A9D9` §1.6.1 + 派工单 t15_ext 字面「600s watchdog 拆批」双向沿用）
- **每 cell 拆批**：每 cell ≤ 30 calls / 单批（≤ 30 calls 看门狗内）
- **6 cells × 单批 = 6 批**（T1.5 prereg §1.6.1 字面「12 批」**0 触**——T1.5r2 每 cell ≤ 30 calls = 1 批/cell = 6 cells × 1 批 = 6 批）

### 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 L2 verdict §2 + L14 verdict §2 + Track 2 runner `INTER_CALL_SLEEP_S` + T1 §1.6.2 + T1.5 prereg `8898B964A9D9` §1.6.2 + 派工单 t15_ext 字面拍板「串行 ≥2.5s」沿用）
- **qwen token-plan 端点**（`token-plan.maas.qianwenaiapi.com/compatible-mode/v1`）：**无代理**（沿 `_v4_v5_multimodel_probe.py` `B65619A07B10` L35 `use_proxy: False` + T1 `802DECE2286A` §1.6.2 + T1.5 prereg `8898B964A9D9` §1.6.2 沿用）
- **teamorouter / mimo / openrouter 端点**：T1.5r2 单端点 = qwen_plan，**不触发** teamo 必走 tun 硬纪律（沿 PI 2026-09-23「teamorouter 必走 tun 防封号」+ user memory 2026-09-23）

### 构造修正（沿 T1 verdict §4.1【最高优先】建议 + 派工单 t15 + t15_ext 明示）

- **端点 + 模型替换** = qwen token-plan `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model_id `qwen3.7-max`（**非 reasoning 模型**）
- **max_tokens = 500**（≥500 拍板字面；L2/L14 维度同步修正以保持 L2/L14 构造一致性；T1 L14 维度 max_tokens=100 沿 L14 verdict §2 字面致 49.3% 空响应，T1.5 + T1.5r2 max_tokens=500 修正构造失灵族 #2，容纳非 reasoning 模型完整输出）
- **max_tokens = 500 = 工具失灵族参数修正，非阈值调整**（沿派工单明示 + T1 verdict §4.1【最高优先】建议字面沿用）

### 构造扩展（**T1.5r2 修订特有**）

- **plan 字面扩样修订** = 5 教师 × 2 prompts × **3 re-asks** = **30 calls/cell** × 6 cells = **180 calls**（沿 T1.5 verdict `52C985429C91` §3.4 字面 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板）
- **2 calls 缺位补跑** = coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3（沿 T1.5 verdict `52C985429C91` §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板；2 补跑 calls 计入 +60 calls 预算内）
- **plan 字面扩样 + 2 calls 缺位补跑 = 构造失灵族参数扩展，非阈值调整**（沿派工单 t15_ext 拍板明示「判定阈值一字不动；扩样 = plan 字面修订」）

### 总预算上限

- **总 calls 上限 ≤ 180 calls**（6 cells × 30 calls/cell 硬上限；T1.5 prereg §1.6.3「360 calls」**0 触**——本棒独立修订）
- **总 wall time 上限 ≤ 5h**（Token Plan 5h 配额硬约束；沿 L14 verdict §9.1 + T1 §1.6.3 + T1.5 prereg `8898B964A9D9` §1.6.3「5h 配额撞限」先例 + 派工单 t15_ext 字面拍板「qwen token-plan 5h 节制」）
- **总增量 = +60 calls**（T1.5 120 calls 实测 + T1.5r2 +60 calls 增量 = 180 calls 总预算；沿 T1.5 verdict `52C985429C91` §3.4 字面 + 派工单 t15_ext 字面拍板）

### 中断-恢复与分批拆跑（沿 T1.5 prereg §1.6.4 字面 + 派工单 t15_ext 字面「中断-恢复同 agent 唤醒」）

- **同 worker 接力棒**：v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2（沿 L14 verdict §9.1 + T1 §1.6.4 + T1.5 prereg §1.6.4 先例 + 派工单 t15_ext 字面「中断-恢复同 agent 唤醒」）
- **checkpoint 文件**：`.tmp/_t15r2_records.json`（沿 L14 runner `.tmp/_l14_records.json` + T1 runner `.tmp/_t1_records.json` + T1.5 runner `.tmp/_t15_records.json` 惯例；**T1.5 runner checkpoint 文件 `.tmp/_t15_records.json` 不动**）
- **元组 skip**：(teacher, caption_id, reask_idx, temp) 已跑 skip（端点恒 = qwen_plan，元组比 T1 少 endpoint 维度）；T1.5 已跑 reask_idx 0/1 元组全部 skip，T1.5r2 续跑起点 = reask_idx = 2
- **2 calls 缺位补跑语义**：coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 沿 T1.5 executor `558E635F9BA6` §checkpoint 模式续跑（**T1.5 executor 一字不动**）
- **撞限应急**：已启动 cells 部分完成记「T1.5r2 部分完成」注记；未启动 cells 留待 worker 下一棒接力

---

## 产物链

> 派生 JSON 不合并（沿 R5 frozen 派生 JSON 不合并铁律 + 派工单 t15_ext 字面拍板）；本棒产物用 `_v4_supp_t15r2_*` prefix 分列

- `_v4_supp_t15r2_executor.py`（T1.5r2 矩阵 runner + checkpoint 模式 + qwen3.7-max 非 reasoning 模型 + max_tokens=500 + 温度切换 + plan 字面扩样至 30 calls/cell；**沿 T1.5 executor `558E635F9BA6` checkpoint 模式续跑**，T1.5 executor 一字不动）
- `_v4_supp_t15r2_result.json`（6 cells 矩阵结果聚合：每 cell per teacher J 中位 + qwen3.7-max + 温度 + audit-only metadata 字段 + schema `v4_t15r2_sensitivity_fix_n10/1`（**沿 T1.5 schema `v4_t15_sensitivity_fix/1` 扩样版本**；仅 schema 版本号扩样字段 = /1 → /n10/1 字面，0 触 T1.5 原 schema 数值字面）+ 跨温度 J 中位标准差 + K-N11-N1_T1relax 字面 PASS 标注（N=15 ≥ N_min=10）+ 2 calls 缺位补跑标注）
- `_v4_supp_t15r2_verdict.md`（T1.5r2 探针判定：6 cells 字面 K-N11-3 实测 + K-T1-S1/S3 触发判定 + K-T1-S2 沿 T1 verdict 结论引用 + K-N11-N1_T1relax 字面 PASS 根因消除标注 + 根因三分类每行附 + T1.5 verdict §3.4 + §4.4 建议落地确认 + 不翻 L2/L14 既判声明 + 不翻 T1 verdict §7 自身声明 + **不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑** ——**T1.5r2 verdict 留 verdict-keeper 起草**，本 activation 件 0 起草 verdict；沿 8 agent 团队分工）
- 与现有 `_v4_supp_t15_*`（T1.5 executor + result + verdict）+ `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律 + 派工单 t15_ext 字面拍板）

---

## 边界

> 沿 V1–V3 资产只读不动 + R4 key 永不明文 + R5 V4 frozen 只追加 + R6 P-G 不动 + R7 plugin spec 不动 + 派工单 t15_ext 字面「T1.5 原件 + result + verdict 一字不动」

- **V1–V3 资产只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）
- **R4 key 永不明文**（**无例外**）
- **R5 V4 frozen 只追加**：v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` + **T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` + T1.5 executor `558E635F9BA6`** + L14V3 追加件 + L14V3 activation + L14V3 映射件 + L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` + L14 verdict `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测）+ L14 result `4C11AB9057B9` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 度量函数 `21771E66AF67` + 3 proxy 算子 `5BA916D1DD24` + 22 caption `6A2656878745` **21 件一字不改**（T1.5r2 修订件比 T1.5 件新增锁定 2 件：T1.5 result `6B47D389B7AE` + T1.5 executor `558E635F9BA6`）
- **R6 P-G v0/v01 不动**
- **R7 plugin spec 不动**
- **生效即锁不重开不调**
- **T1.5r2 追加件正文「待 PI 复核生效」字样保留不删**（沿「锁后不改字面」+ 留锁前痕迹纪律；本 activation 件由 draft 转生效时，PI 复核通过状态以本 activation 件为准）
- **派生 JSON 不合并**
- **论文 §4 去向未拍板**（沿拍板 #9 缓定；本棒产物不进 §4，K-N11-N2 字面 + T1.5r2 探针稳健性注记 + T1 verdict 信息量补正 + T1.5 verdict §3.4 + §4.4 建议落地确认沿 L2/L14 + T1 verdict + T1.5 verdict 既定路径）
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（沿 v0.2 + L9 + L10 + T1 + T1.5 + L14V3 同惯例；sk- / AIza / Bearer 三模式自扫 0 hit）
- **T1.5r2 探针定位硬约束再声明**：**T1.5 扩样修订探针（construction-failure-fix expansion probe）**，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict §7 总判定一字不动 + **不得二次判定** T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑
- **0 新设数值阈值声明**：K_N11_3_THRESHOLD = 0.85 沿字面不动；K-T1-S1/S2/S3 沿 T1 + T1.5 字面沿用 + 均为布尔条件显式化；TH-T1-1 = 10 对/教师为 T1 探针放宽口径（T1.5 + T1.5r2 沿用），与 L2/L14 既定 N=20/教师 两层并存；**T1.5r2 plan 字面扩样 + 2 calls 缺位补跑 = 构造失灵族参数扩展，非阈值调整**（沿派工单 t15_ext 拍板明示）
- **C-T15-1 = 工具失灵族参数修正，非阈值调整**（端点 + 模型替换 + max_tokens=500；沿 T1 verdict §4.1【最高优先】建议 + 派工单 t15 + t15_ext 明示）
- **C-T15r2-1 = 构造失灵族参数扩展，非阈值调整**（plan 字面扩样 20 → 30 calls/cell = +60 calls 总增量；沿 T1.5 verdict §3.4 字面 + 派工单 t15_ext 字面拍板）
- **C-T15r2-2 = 2 calls 缺位补跑，非阈值调整**（沿 T1.5 verdict §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板）
- **0 触既有 K-N11-1/2/3/N1/N2 字面**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1 + v0.2 `D85488A64D89` §2 L2 一字不动）
- **0 触既有 K-T1-S1/S2/S3 字面**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 + T1.5 prereg `8898B964A9D9` §1.5.2 一字不动）
- **audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板**（不参与 kill-line / Jaccard / 统计推断）