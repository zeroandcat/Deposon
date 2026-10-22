# V4 T1.5 追加件生效留痕（draft，2026-09-24，待 PI 复核生效）

- **追加件**：`results/_v4_supp_prereg_v02_add_T15_2026_09_24.md`（T1.5 · T1 构造失灵族补正 稳健性探针），SHA-12 见落盘报值（**末态文件 hash = `8898B964A9D9`（76,991 B）**）——**待 PI 复核生效，生效即锁，一字不改**
- **PI 拍板**：待 `ask_T15_*` 问卷（PI 2026-09-24 23:33 派工单 `ask_9484b696c4f3af85941b3c43` t15 拍板「启动 T1.5：非 reasoning 模型+max_tokens≥500 重跑温度敏感性」+ 同轮 ratify_all 追认 T1/L14V3/映射件生效即锁待复核生效）
- **生效时刻**：待 PI 复核生效时填入（沿 `AD42992DC75D` 锁先例「生效时刻」字段填法）
- **T1.5 探针定位硬约束**（沿 T1.5 §0 + §1.3 + §4 边界声明）：
  - **T1.5 = T1 构造失灵族补正稳健性辅助检验（construction-failure-fix probe）**，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**
  - 结论仅作**稳健性注记**入勘误链（K-T1-S1 命中）+ **T1 verdict 信息量补正**（K-T1-S3 命中，构造失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认）
  - 除 K-T1-S1 命中（方向翻转 = hit=True）**且另走 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程**，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict `F1B5E49F3058` §7 总判定一字不动
  - L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」既定结论一字不动
  - T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动（T1.5 不二次判定 T1 verdict 自身）

---

## T1.5 探针字面（沿 T1.5 §1.5，0 新设数值阈值）

### 既有 K-N11 字面（沿 L2/L14 verdict 一字不动，锁前痕迹保留）

- **K-N11-1**：三方 Jaccard 中位数差异 < K_N11_1_DIFF = 0.05 即 `hit=True` → FAIL（三方不可分离）—— **沿 `0A9EE16267B5` §1 K-N11-1 字面**
- **K-N11-2**：distill J > teacher J + K_N11_2_DELTA = 0.05 不成立即 `hit=True` → FAIL（与原假设反向）—— **沿 `0A9EE16267B5` §1 K-N11-2 字面**
- **K-N11-3**：教师两次 J 中位数 < K_N11_3_THRESHOLD = 0.85 即 `hit=True` → FAIL（教师自身不稳定，主度量失效）—— **沿 `0A9EE16267B5` §1 K-N11-3 字面**（**T1.5 探针核心沿此字面**）
- **K-N11-N1**：N < TH17_N_TARGET = 20 / 教师 即 `pass=False` → FAIL（构造退化致命题不明）—— **沿 v0.2 §2 L2 K-N11-N1 字面**（**T1.5 探针放宽至 N_min=10** 不动此字面）
- **K-N11-N2**：构造面 K-N11-1/2/3 + 真实面 K-N11-1/2/3 **并记**；任一面 PASS ≠ 命题成立（必须双面都过）—— **沿 v0.2 §2 L2 K-N11-N2 字面**

### T1.5 复用 K-T1-* 字面（沿 T1 追加件 + T1 verdict 一字不动，0 新设数值阈值）

- **K-T1-S1（温度敏感性 flip 触发线 · 主判定，T1.5 复用沿 T1 一字不动）**：
  - **字面**：在 qwen_plan 端点下，沿 L2 维度或 L14 维度，教师 J 中位数跨温度 {0.0, 0.3, 0.5} 中**任一温度点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**（显式布尔）：
    - 既定方向 = qwen t=0.7 baseline 教师 J 中位 < 0.85（沿 L2 verdict `E433A06E7BFB` §3.2 + L14 verdict `764F24A21AC8` §3.2 实测）
    - 翻转条件 = 新 (端点=qwen_plan, 维度=L2|L14, 温度 ∈ {0.0, 0.3, 0.5}) cell 教师 J 中位 ≥ 0.85（**T1.5 = qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后**）
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（沿 L2/L14 verdict + `0A9EE16267B5` §1 + T1 `802DECE2286A` §1.5.2 字面，**0 新设**）
  - **不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**：K-T1-S1 hit=True 仅入稳健性注记，**不据此改判** L2 verdict `E433A06E7BFB` §11 + L14 verdict `764F24A21AC8` §11 既定结论一字不动；**不二次判定** T1 verdict `F1B5E49F3058` §7 总判定一字不动

- **K-T1-S2（端点敏感性 flip 触发线 · 主判定，T1.5 沿 T1 verdict 结论引用不重测）**：
  - **T1.5 字面**：T1 verdict `F1B5E49F3058` §2.2 K-T1-S2 已裁 `any_hit: false`（端点维度 mimo/teamo × {0.0, 0.3, 0.5} × {L2/L14} 整矩阵方向 J<0.85，empty-empty 主导非真判定一致）；T1.5 端点维度砍去（qwen_plan 单端点），**沿 T1 verdict §2.2 any_hit: false 结论引用**，**T1.5 不重测 K-T1-S2**
  - **理由**：T1 verdict §4.1【最高优先】建议 = 「改用非 reasoning 模型 + 提高 max_tokens」（沿端点 / 模型类别修正 + max_tokens 修正），不是「改用不同端点」；端点维度在 T1 verdict §2.2 已裁 empty-empty 主导致 K-T1-S2 字面 any_hit: false 系构造失灵族假象（reasoning 模型 + max_tokens=100），非真端点敏感性不稳健；T1.5 沿 T1 verdict 结论引用 = 端点维度敏感性判据已沿 T1 verdict 字面收口
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（一字不动）
  - **不翻 L2/L14 正式判定**：同 K-T1-S1

- **K-T1-S3（稳健性确认线 · 副判定 + T1 verdict 信息量补正线，T1.5 复用沿 T1 一字不动）**：
  - **字面**：6 cells 全 J 中位 < 0.85 = 「**判定稳健**」= T1.5 探针不命中 K-T1-S1 / K-T1-S2 → 入稳健性确认注记 + **T1 verdict 构造失灵族假象裁定获补正**（qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链作 L2/L14 既判稳健性确认）
  - **判定方式**：任一 cell 触发 K-T1-S1 或 K-T1-S2（K-T1-S2 沿 T1 verdict 结论引用）= 探针命中；全 6 cells 不触发 = 探针不命中 + T1 verdict 信息量补正
  - **T1.5 探针与 T1 verdict §7 关系**：T1 verdict §7 总判定一字不动（T1 verdict 自身不可二次判定）；T1.5 K-T1-S3 命中（探针不命中 K-T1-S1/S2）= **仅作 T1 verdict 信息量补正**（T1 verdict §4.3 信息量边界声明获补充：构造失灵族修正后真维持方向一致 = 真稳健入勘误链）；T1.5 K-T1-S1 命中 = 仅入稳健性存疑注记，**不翻 T1 verdict §7 自身**

### T1.5 探针阈值一览

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| K_N11_1_DIFF | 0.05 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-1 字面 |
| K_N11_2_DELTA | 0.05 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-2 字面 |
| K_N11_3_THRESHOLD | 0.85 | `_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-3 字面 |
| K_N11_3_THRESHOLD | 0.85 | `_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.5.2 K-T1-S1/S2/S3 字面（T1.5 复用沿用） |
| TH-17 N_TARGET | 20 / 教师 | `_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面 |
| **TH-T1-1 N_min** | **10 对/教师**（T1 探针放宽，T1.5 沿用） | `_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.4 非退化自证 + §1.8 新增条款 |
| **C-T15-1 端点 + 模型替换 + max_tokens=500** | qwen_plan + qwen3.7-max（非 reasoning）+ max_tokens ≥ 500 | 派工单 `ask_9484b696` t15 + T1 verdict `F1B5E49F3058` §4.1【最高优先】 | — | 派工单 23:33 拍板 + T1 verdict §4.1 字面（**工具失灵族参数修正**，非阈值调整） |
| **audit-only metadata 字段集** | `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint` | `_v4_supp_l14v3_model_mapping_2026_09_24.md` §1.2 + §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板 | `L14V3_MAP_*` | §1.2 字段表 + §6.1 #2 audit-only 拍板（T1.5 沿用同字段集） |

> **0 新设数值阈值声明**：K-T1-S1/S2/S3 三条**0 新设数值阈值**；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict `E433A06E7BFB` §2 + L14 verdict `764F24A21AC8` §2 + `0A9EE16267B5` §1 + T1 `802DECE2286A` §1.5.2 字面一字不动；T1.5 探针字面「方向翻转 = hit=True」是布尔条件显式化（沿 S-40 教训「判定布尔显式方向」），**不构成阈值私设**；max_tokens = 500 系**工具失灵族参数修正**（沿 T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + §5.1 工具失灵族假象裁定），**非阈值调整**——沿派工单明示「判定阈值一字不动；max_tokens 属工具失灵族参数修正」

---

## 锁定范围

> 沿 R5 frozen 只追加 + 锁后不改字面 + 派生 JSON 不合并

- **§0 输入件 SHA-12 链 19 件**（既有 3 件预登记 `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` + v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` + L14V3 追加件 + L14V3 activation + L14V3 映射件 + L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` + L14 verdict `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测）+ L14 result `4C11AB9057B9` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 22 caption `6A2656878745`）
- **§1 T1.5 矩阵 6 cells**（{L2, L14} × {temp 0.0/0.3/0.5} × qwen_plan 单端点）+ K-N11-1/2/3/N1/N2 字面不动 + K-T1-S1/S2/S3 沿 T1 字面沿用（0 新设数值阈值）+ TH-T1-1 = 10 对/教师（T1.5 沿 T1 沿用）+ C-T15-1 = 端点 + 模型替换 + max_tokens=500（**工具失灵族参数修正**，非阈值调整）+ audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 拍板
- **§0.5 过渡声明 1 件**：T1.5 构造失灵族补正探针定位过渡（T1 verdict 构造失灵族假象裁定获补正探针立线 + L2/L14 既定 K-N11-3 真证伪不动 + T1 verdict §7 一字不动 + T1.5 探针 6 cells 跑出前不预设 PASS/FAIL 翻转）
- **§5 根因三分类 + T1.5 探针与 L2/L14 既判 + T1 verdict §7 的根因关联**（沿拍板 #15 + T1 §5 沿用 + T1.5 增量「不二次判定 T1 verdict §7」+「T1 verdict 信息量补正」三栏）
- **既有 K-N11-1/2/3/N1/N2 字面锁前痕迹保留**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1 + v0.2 `D85488A64D89` §2 L2 一字不动）
- **既有 K-T1-S1/S2/S3 字面锁前痕迹保留**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 一字不动；T1.5 复用一字不动，0 新设数值）
- **T1.5 探针定位硬约束**：T1 构造失灵族补正稳健性辅助检验，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict §7 总判定一字不动

---

## 过渡声明 1 件随生效继续有效

- **T1.5 构造失灵族补正探针定位过渡**：自 T1.5 件立线起标「**已知 T1 verdict `F1B5E49F3058` §7 总判定已裁『K-T1-S3 字面命中（PASS）= 构造失灵族假象』；T1.5 = 该构造失灵族补正探针（沿 T1 verdict §4.1【最高优先】建议立线）；T1.5 6 cells 跑出前不预设 PASS / FAIL 翻转**」——
  - L2 verdict `E433A06E7BFB` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；t=0.7 实证 J 中位 0.41-0.52 < 0.85）」
  - L14 verdict `764F24A21AC8` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；N=20 收敛稳定 0.36-0.39 区间）」
  - T1 verdict `F1B5E49F3058` §7 总判定 = 「K-T1-S3 字面命中（PASS）= 构造失灵族假象：reasoning 模型 + max_tokens=100 致 49.3% 空响应 + 72.1% empty-empty pairs；J=0.0 主要来自『双方都空』非真判定一致；真证伪要件 ②③④ 失守」
  - T1.5 在 {temp 0.0 / 0.3 / 0.5} × qwen3.7-max 单端点矩阵下探「非 reasoning 模型 + max_tokens=500 修正后教师 J 中位是否仍 < 0.85」—— 若任一 cell 翻 ≥0.85，**仅记「qwen 端点代表性存疑」注记**（qwen 端点固有方差 vs 温度敏感性二源），**不据此翻 K-N11-3 真证伪既定判**（qwen 端点 + temp=0.7 是既定条件，方向翻转只质疑 qwen 端点的代表性而非整体判死）；**不二次判定** T1 verdict §7 自身
  - 全 6 cells 仍 J < 0.85（无翻转）= 「**判定稳健**」= 不入勘误链（仅作稳健性确认注记；同时补正 T1 verdict 构造失灵族裁定 —— 字面 PASS 在工具失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认；**T1 verdict §7 自身一字不动**）
- **本件不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 过渡声明 3 件** + **不动 L10 §0.5 过渡声明 2 件** + **不动 T1 §0.5 过渡声明 1 件**

---

## 起跑条件（T1.5 接力 worker · T1 构造失灵族补正 稳健性探针）

> 沿 T1.5 §1.4 启动条件 + §1.6 调用预算与节制

### 6 cells 矩阵执行（worker 接力棒）

- **L2 维度**（沿 L2 verdict `E433A06E7BFB` §2 字面）：
  - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell
  - 3 cells（L2 × {temp 0.0/0.3/0.5} × qwen_plan）= ≤ 78 calls / L2 维度
- **L14 维度**（沿 L14 verdict `764F24A21AC8` §2 字面）：
  - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell
  - 3 cells（L14 × {temp 0.0/0.3/0.5} × qwen_plan）= ≤ 78 calls / L14 维度
- **总 cells = 6 cells × ≤ 26 calls/cell = ≤ 156 calls**（理论 ≤ 360 calls 硬上限，按需减少）

### 小→大序列（worker 第 1 棒接力，先行 sanity check）

1. **单 cell sanity check**：L2 维度 × temp=0.3 × qwen_plan = 1 cell × ≤ 26 calls（**先行探活 + 非 reasoning 模型 + max_tokens=500 可行性验证**）
2. **维度扩展**：L2 维度 × {temp 0.0/0.3/0.5} × qwen_plan = 3 cells × ≤ 26 calls（**L2 维度温度敏感性**）
3. **全集**：L14 维度 × {temp 0.0/0.3/0.5} × qwen_plan = 3 cells × ≤ 26 calls（**L14 维度温度敏感性**）

### 单批 calls 上限（看门狗约束）

- **单批 ≤ 30 calls**（沿 L2 verdict §2「600s 看门狗」+ L14 verdict §9.1「sub-batch strategy」+ T1 `802DECE2286A` §1.6.1 双向沿用）
- **每 cell 拆批**：每 cell ≤ 26 calls / 单批（≤ 30 calls 看门狗内）
- **6 cells × 单批 = 6 批**（理论；按需拆 12 批按 L14 §9.1 280s hard limit 模式）

### 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 L2 verdict §2 + L14 verdict §2 + Track 2 runner `INTER_CALL_SLEEP_S` + T1 §1.6.2 沿用）
- **qwen token-plan 端点**（`token-plan.maas.qianwenaiapi.com/compatible-mode/v1`）：**无代理**（沿 `_v4_v5_multimodel_probe.py` `B65619A07B10` L35 `use_proxy: False` + T1 `802DECE2286A` §1.6.2 qwen 行 `use_proxy: False` 沿用）
- **teamorouter / mimo / openrouter 端点**：T1.5 单端点 = qwen_plan，**不触发** teamo 必走 tun 硬纪律（沿 PI 2026-09-23「teamorouter 必走 tun 防封号」+ user memory 2026-09-23）

### 构造修正（沿 T1 verdict §4.1【最高优先】建议 + 派工单明示）

- **端点 + 模型替换** = qwen token-plan `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model_id `qwen3.7-max`（**非 reasoning 模型**）
- **max_tokens = 500**（≥500 拍板字面；L2/L14 维度同步修正以保持 L2/L14 构造一致性；T1 L14 维度 max_tokens=100 沿 L14 verdict §2 字面致 49.3% 空响应，T1.5 修正至 ≥500 容纳非 reasoning 模型完整输出）
- **max_tokens = 500 = 工具失灵族参数修正，非阈值调整**（沿派工单明示）

### 总预算上限

- **总 calls 上限 ≤ 360 calls**（6 cells × 60 calls/cell 硬上限）
- **总 wall time 上限 ≤ 5h**（Token Plan 5h 配额硬约束）
- **实际预计 ≤ 156 calls**（沿 §1.4 + §1.6 字面）

### 中断-恢复与分批拆跑

- **同 worker 接力棒**：v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2（沿 L14 verdict §9.1 + T1 §1.6.4 先例）
- **checkpoint 文件**：`.tmp/_t15_records.json`（沿 L14 runner `.tmp/_l14_records.json` + T1 runner `.tmp/_t1_records.json` 惯例）
- **元组 skip**：(teacher, caption_id, reask_idx, temp) 已跑 skip（端点恒 = qwen_plan，元组比 T1 少 endpoint 维度）
- **撞限应急**：已启动 cells 部分完成记「T1.5 部分完成」注记；未启动 cells 留待 worker 下一棒接力

---

## 产物链

> 派生 JSON 不合并（沿 R5 frozen 派生 JSON 不合并铁律）；本棒产物用 `_v4_supp_t15_*` prefix 分列

- `_v4_supp_t15_executor.py`（T1.5 矩阵 runner + checkpoint 模式 + qwen3.7-max 非 reasoning 模型 + max_tokens=500 + 温度切换）
- `_v4_supp_t15_result.json`（6 cells 矩阵结果聚合：每 cell per teacher J 中位 + qwen3.7-max + 温度 + audit-only metadata 字段 + schema `v4_t15_sensitivity_fix/1` + 跨温度 J 中位标准差）
- `_v4_supp_t15_verdict.md`（T1.5 探针判定：6 cells 字面 K-N11-3 实测 + K-T1-S1/S3 触发判定 + K-T1-S2 沿 T1 verdict 结论引用 + 根因三分类每行附 + **T1 verdict 信息量补正** + **不翻 L2/L14 既判声明** + **不二次判定 T1 verdict §7 自身声明**）
- 与现有 `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律）

---

## 边界

> 沿 V1–V3 资产只读不动 + R4 key 永不明文 + R5 V4 frozen 只追加 + R6 P-G 不动 + R7 plugin spec 不动

- **V1–V3 资产只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）
- **R4 key 永不明文**（**无例外**）
- **R5 V4 frozen 只追加**：v0.2 本体 `D85488A64D89` + v0.2 activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` + L14V3 三件 + L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` + L14 verdict `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测）+ L14 result `4C11AB9057B9` + Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE` + 度量函数 `21771E66AF67` + 3 proxy 算子 `5BA916D1DD24` + 22 caption `6A2656878745` **19 件一字不改**
- **R6 P-G v0/v01 不动**
- **R7 plugin spec 不动**
- **生效即锁不重开不调**
- **T1.5 追加件正文「待 PI 复核生效」字样保留不删**（沿「锁后不改字面」+ 留锁前痕迹纪律；本 activation 件由 draft 转生效时，PI 复核通过状态以本 activation 件为准）
- **派生 JSON 不合并**
- **论文 §4 去向未拍板**（沿拍板 #9 缓定；本棒产物不进 §4，K-N11-N2 字面 + T1.5 探针稳健性注记 + T1 verdict 信息量补正沿 L2/L14 + T1 verdict 既定路径）
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（沿 v0.2 + L9 + L10 + T1 + L14V3 同惯例；sk- / AIza / Bearer 三模式自扫 0 hit）
- **T1.5 探针定位硬约束再声明**：**T1 构造失灵族补正稳健性辅助检验（construction-failure-fix probe）**，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict §7 总判定一字不动
- **0 新设数值阈值声明**：K_N11_3_THRESHOLD = 0.85 沿字面不动；K-T1-S1/S2/S3 沿 T1 字面沿用 + 均为布尔条件显式化；TH-T1-1 = 10 对/教师为 T1 探针放宽口径（T1.5 沿用），与 L2/L14 既定 N=20/教师 两层并存
- **C-T15-1 = 工具失灵族参数修正，非阈值调整**（端点 + 模型替换 + max_tokens=500；沿 T1 verdict §4.1【最高优先】建议 + 派工单明示）
- **0 触既有 K-N11-1/2/3/N1/N2 字面**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1 + v0.2 `D85488A64D89` §2 L2 一字不动）
- **0 触既有 K-T1-S1/S2/S3 字面**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 一字不动）
- **audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板**（不参与 kill-line / Jaccard / 统计推断）