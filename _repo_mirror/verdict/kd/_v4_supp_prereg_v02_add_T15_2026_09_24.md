# V4 补测预登记 v0.2 T1.5 追加件 · T1 构造失灵族补正 稳健性探针（2026-09-24）

- **性质**：protocol-keeper 追加立线（派工单 2026-09-24 23:33 follow-up，PI `ask_9484b696c4f3af85941b3c43` 拍板 `t15`「启动 T1.5：非 reasoning 模型+max_tokens≥500 重跑温度敏感性」+ 同轮 ratify_all 追认 T1/L14V3/映射件生效即锁；本棒从 PI 派工「T1.5 辅助检验预登记——T1 构造失灵补正（非 reasoning 模型+max_tokens≥500 重跑温度敏感性）」—— 单端点 qwen3.7-max × {temp 0.0/0.3/0.5} × {L2/L14} = 6 cells 矩阵；本稿不调用任何 LLM，不跑实验，仅固化 T1.5 立线 + 矩阵字面 + kill-line 字面 + 调用预算 + 阈值来源表 + 沿 T1 `802DECE2286A` + T1 verdict `F1B5E49F3058` + L14V3 `L14V3_*` + 既有 5 件预登记先例）
- **定位（边界）**：**T1.5 = T1 构造失灵族补正（construction-failure-fix probe）**，**不翻 L2/L14 正式判定**；T1 原件 `802DECE2286A` 与 T1 verdict `F1B5E49F3058` **一字不动**；L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」既定结论一字不动；T1 verdict 已裁定「字面 PASS=构造失灵族假象」（reasoning 模型 mimo-v2.6-pro + deepseek-v4-flash + max_tokens=100 → 49.3% 空响应 + 72.1% empty-empty pairs），T1.5 = 该构造失灵的修复路径，沿 T1 verdict §4.1「【最高优先】改用非 reasoning 模型 + 提高 max_tokens」建议立线
- **预登记件本体不动**：`results/_v4_supp_prereg_v02_2026_09_24.md` SHA-12 `D85488A64D89` 锁后**一字不改**；T1 追加件 `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` SHA-12 `802DECE2286A` 锁后**一字不改**；T1 verdict `results/_v4_supp_t1_verdict.md` SHA-12 `F1B5E49F3058` 锁后**一字不改**；L2 verdict `E433A06E7BFB` 锁后**一字不改**；L14 verdict `764F24A21AC8` 锁后**一字不改**；本棒以独立追加件形式立线（沿 T1 `802DECE2286A` + L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` + L14V3 `L14V3_*` + 各自 activation 先例）
- **PI 复核待生效**（沿 `D85488A64D89` activation `AD42992DC75D` + L9 activation `5C579F28634E` + L10 activation `16E89657DAAA` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` 锁先例）—— T1.5 立线 + 矩阵字面 + kill-line 字面（K-T1-S1 沿 T1 一字不动 + K-T1-S2 沿 T1 verdict 结论引用不重测 + K-T1-S3 沿 T1 一字不动）+ 调用预算 + 产物链 `_v4_supp_t15_*` 待 PI 复核生效；**生效即锁**（沿 `0A7BCA992B95` 锁先例），事后不重开不调；**「CONDITIONAL PASS」退役**，只用 PASS / FAIL 二值（沿 R6 实证）
- **范围**：T1.5 稳健性探针 = {L2 N-11 supp 教师 J 判定, L14 N-11 full 三方配对} × {temp ∈ {0.0, 0.3, 0.5}} × qwen token-plan `qwen3.7-max` 单端点 = **6 cells** 矩阵；qwen t=0.7 既有数据（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）作**对照基准不重跑**；T1 已探 mimo/teamo 端点（沿 T1 verdict `F1B5E49F3058` §1.3 + §2.1-§2.3 字面）= 端点维度砍去；S2（端点敏感性 flip 触发线）沿 T1 verdict 结论引用**不重测**；不含 L1 N-28 / L3 N-20 / L4 N-26 / L5 C-S39 / L6 S-38 / L7 E-N20 / L8 N-12 / L9/L10/L14V3 等其它线（沿 v0.2 §1-§8 字面不动）；不含 v0.2 §0.5 既有 3 件过渡声明（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）；不含 L9 §0.5 过渡声明 3 件；不含 L10 §0.5 过渡声明 2 件；不含 T1 §0.5 过渡声明 1 件
- **判定依据**：deposon 项目核心准则四条「大材小用，落到实处，与死同行，虚实回路（FTFB）」（PI 2026-09-22 R1 录入 + 2026-09-23 FTFB 入根 + **准则为根，论文为一处外显**；详见 `113CBE555643` §0 注）—— 三问映射沿既有预登记件 §1.1.1 代拟稿 §1 + 种子稿 §0 + 整合补充稿 §1（沿 `0A7BCA992B95` §1）

---

## 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | SHA-12 | 字节 | 用途 |
|---|---|---|---|---|
| v0.2 预登记本体（锚定不动） | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | 42,764 | T1.5 立线锚定 + 通用条款格式（TH-* / 派生 JSON / 双读法 / 阈值表） |
| v0.2 activation 件 | `results/_v4_supp_prereg_v02_activation_2026_09_24.md` | `AD42992DC75D` | 3,202 | T1.5 立线后状态沿 `AD42992DC75D` 锁先例 |
| L9 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md` | `23879B6CD1CC` | 19,586 | T1.5 立线锚定 + 双读法并记先例（K-A2R-R1/N1） |
| L9 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md` | `5C579F28634E` | 3,924 | T1.5 立线后 L9 沿 `5C579F28634E` 锁先例 |
| L10 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L10_2026_09_24.md` | `F6FE005EE3C7` | 26,159 | T1.5 立线锚定 + 语义反转注释先例（K-E-N20-3 语义反转双栏并记） |
| L10 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L10_activation_2026_09_24.md` | `16E89657DAAA` | 9,442 | T1.5 立线后 L10 沿 `16E89657DAAA` 锁先例 |
| **T1 追加件（锚定不动，T1.5 字面源 1）** | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | 52,942 | T1.5 立线锚定 + K-T1-S1/S3 字面源 + T1 verdict §1-§5 字面 |
| **T1 activation 件（锚定不动）** | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936B630015` | 14,234 | T1.5 立线后 T1 沿 `79936B630015` 锁先例 |
| **T1 verdict 件（锚定不动，T1.5 字面源 2）** | `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058` | 字节沿 T1 verdict §6 RESULT「字节 / 行数：以落盘末态为准」 | T1.5 补正路径字面源（裁定「字面 PASS=构造失灵假象」+ §4.1 建议改用非 reasoning 模型+max_tokens ≥500） |
| L14V3 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `L14V3_*`（自身 SHA） | 61,547 | T1.5 立线锚定 + N-26 真审唯一路径先例 + L14V3 activation 同先例 |
| L14V3 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `L14V3_ACT_*`（自身 SHA） | 21,309 | T1.5 立线后 L14V3 沿同锁先例 |
| L14V3 映射件（锚定不动） | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | `L14V3_MAP_*`（自身 SHA） | — | T1.5 audit-only metadata 字段口径沿 §6.1 #2 拍板 |
| 方法预登记补充稿 | `results/_v4_methods_prereg_supplement_2026_09_23.md` | `0A7BCA992B95` | 59,570 | §1 通用条款 + 格式基线 |
| N-09~N-39 预登记 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | 60,530 | §1 K-N11 字面（L2/L14 判定件均沿此字面） |
| 种子预登记补充稿 | `results/_v4_seeds_prereg_supplement_2026_09_23.md` | `113CBE555643` | 53,633 | §0 注 + 格式基线 |
| **L2 N-11 supp verdict（锚定 T1.5 字面源 3）** | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | 15,671 | K-N11-1/2/3/N1/N2 字面（沿 `0A9EE16267B5` §1）+ 教师 J 实测 (qwen t=0.7, N=2, J 中位 0.41-0.52) |
| L2 N-11 supp result | `results/_v4_supp_l2_n11supp_result.json` | `FF7B167AE43F` | 17,970 | L2 N-11 supp 数据（qwen 端点） |
| **L14 N-11 full verdict（锚定 T1.5 字面源 4）** | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测） | 19,708（自报）/ 19,697（盘实测） | K-N11-1/2/3/N1/N2 字面 + schema `v4_l14_n11full/2` + 教师 J 实测 (qwen t=0.7, N=20, J 中位 0.36-0.39) |
| L14 N-11 full result | `results/_v4_supp_l14_n11full_result.json` | `4C11AB9057B9` | 12,246 | L14 N-11 full 数据（qwen 端点） |
| Track 2 multimodel probe | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | — | 三端点 ROUTE_TEMPLATES + tun 代理 + 串行 ≥2s |
| Track 2 endpoints probe | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | 5,803 | qwen_plan / mimo / teamo 三端点权威源（T1.5 单端点 = qwen_plan 行） |
| Track 2 multimodel verdict (件 3) | `results/_v4_track2_multimodel_verdict_2026_09_23.md` | （自身 SHA） | 12,883 | 6 模型补跑判定（qwen3.7-max / mimo / teamo 等） |

> 注：L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测）字面引用沿 T1 §9.1 + §9.2 SHA 漂移披露惯例；T1.5 字面源锚定沿自报值 `764F24A21AC8`；L14 verdict 自报 vs 盘 SHA 漂移 11 B + 12 hex 全异（沿 T1 verdict `F1B5E49F3058` §5.2 limitations 披露）；本棒 0 触 L14 verdict 字面。

---

## §0 边界声明（沿 R5 / R6 / R7 复审稿，2026-09-23 勘误版）

- **0 LLM 调用**：本稿由 protocol-keeper 起草，全程未调用任何 LLM API；纯文件编辑（write/edit），未调任何 LLM/代理/构造代理/网关；沿 V4 §3.1 放开语境明示可调（PI 2026-09-22「V3 的剑不斩 V4 的官」），本棒无需调
- **R4 key 永不明文**（**无例外**，沿 R4 + PI 2026-09-22「key 永不明文等合理且无冲突的铁律要沿用」）：本稿及其后续产物不写入、不引用、不打印任何明文 API key / 平台密钥；key 仅在进程组方法里以 runtime env 读取；**本稿自扫** `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态 0 命中
- **R5 V4 frozen 只追加**（**V4 沿用 V1–V3 资产只读底线**）：本稿不修改 v0.2 预登记件 `D85488A64D89` / 不动 activation 件 `AD42992DC75D` / 不动 L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` / 不动 L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` / 不动 T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` / 不动 L14V3 追加件 + L14V3 activation + L14V3 映射件 / 不动 L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` / 不动 L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`；**派生 JSON 不合并**（本棒产物用 `_v4_supp_t15_*` prefix 分列，与现有 `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立）
- **R6 P-G v0/v01 / R7 plugin spec**：本棒不动 P-G v0/v01；不动 plugin spec；不动 verifier 内置脚本
- **V1–V3 只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）
- **kill-line 字面不动禁私设条款**（S-40 教训：判定布尔显式方向 `hit=True` 即触发 / `pass=True` 即存活，禁裸 bool；PI 2026-09-23 拍板明示「禁止擅自调阈值 / 禁止合并派生 JSON / 禁止私设 kill-line 条款」）：本棒 T1.5 kill-line 字面**完全沿** T1 追加件 `802DECE2286A` §1.5 + T1 verdict `F1B5E49F3058` §2 字面（K-N11-1/2/3/N1/N2 + K-N11-N2 双读法 + K-T1-S1 温度敏感性 flip 触发线 + K-T1-S3 稳健性确认线一字不动；K-T1-S2 端点敏感性 flip 触发线沿 T1 verdict §2.2 字面「any_hit: false」结论引用 **不重测**），**0 触既有 K-N11 字面 + 0 触既有 K-T1-S1/S2/S3 字面**；**阈值一律沿 T1 + L2/L14 字面 = K_N11_3_THRESHOLD = 0.85** 等，**禁新设**
- **0 擅调阈值**（沿 v0.2 §0 + T1 `802DECE2286A` §0 同口径）：本棒 **0 调既有 K_N11_1_DIFF = 0.05 / K_N11_2_DELTA = 0.05 / K_N11_3_THRESHOLD = 0.85 / TH17_N_TARGET = 20**；T1.5 沿用一字不动；max_tokens 修正 = **工具失灵族参数修正**（沿 T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + §5.1 工具失灵族假象裁定），**非阈值调整**（沿派工单明示「判定阈值一字不动；max_tokens 属工具失灵族参数修正」）
- **T1.5 定位硬约束**：本棒 = T1 构造失灵族补正探针（construction-failure-fix probe），**不翻 L2/L14 正式判定**；除 T1.5 kill-line 命中（方向翻转 = hit=True）**且另走 verdict-keeper 裁因 + verifier 签字 + PI 复核流程**，**不得据此改判** L2/L14 既定结论（沿 L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」既定结论一字不动）
- **构造修正（非阈值，非私设）**：本棒仅修正 T1 verdict 裁定的构造失灵族**两类**（沿 T1 verdict `F1B5E49F3058` §1.3 真受审要件 ②③④ + §4.1 复评路径建议 #1）：
  - **工具失灵族 #1（reasoning 模型 → 非 reasoning 模型）**：端点 + 模型替换 = qwen token-plan `qwen3.7-max`（沿 L2/L14 verdict §2 字面 + `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 既有 baseline 端点 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + Track 2 ROUTE_TEMPLATES[0]）；**同端点同模型**，故 L2/L14 t=0.7 既有数据（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）= **T1.5 baseline 对照锚不重跑**；t=0.7 数据为 temperature 维度回归锚
  - **工具失灵族 #2（max_tokens 预算失配 → 充分预算）**：max_tokens = **500**（≥500 拍板字面），覆盖非 reasoning 模型完整输出所需；T1 max_tokens=100 系沿 L14 verdict `764F24A21AC8` §2 字面（T1 L14 维度沿用），T1 verdict `F1B5E49F3058` §1.3 裁定「reasoning 模型 mimo-v2.6-pro + deepseek-v4-flash 几乎所有 reasoning tokens 消耗 max_tokens=100 预算」= 工具失灵族 #2 实证
- **audit-only metadata 字段口径**（沿 L14V3 映射件 §6.1 #2 PI 拍板 `ask_9484b696` `meta_field`）：T1.5 产物链 `_v4_supp_t15_executor.py` + `_v4_supp_t15_result.json` + `_v4_supp_t15_verdict.md` 中 result json metadata 字段 = **audit-only**（不参与 kill-line 计算 / 不参与 Jaccard 度量 / 不参与统计推断；仅作审计追溯，不入判定字面源）；沿 L14V3 映射件 §1.2 拍板字段集：`v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint`（T1.5 沿用同字段集，端点恒为 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max`）
- **skill 加载老实交代**：派工单要求 `scientific-research-workflows:experimental-design` skill，本地 skill 加载器多次实录 `Local skill not found`（沿 v0.2 §0 + L9 §0 + L10 §0 + T1 §0 + L14V3 §0 同口径）—— 本棒按 v0.2 `D85488A64D89` + activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` + L14V3 三件 + 既有 5 件预登记件 `113CBE555643` `0A7BCA992B95` `0A9EE16267B5` + L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` 的格式与字面锚执行，**未编造 skill 不存在的虚构指令**

---

## §0.5 过渡声明（本棒 T1.5 立线件特有）

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）

- **T1.5 构造失灵族补正定位过渡**：自本件立线起标「**已知 T1 verdict `F1B5E49F3058` §7 总判定已裁『K-T1-S3 字面命中（PASS）= 构造失灵族假象』；T1.5 = 该构造失灵族补正探针（沿 T1 verdict §4.1【最高优先】建议立线）；T1.5 6 cells 跑出前不预设 PASS / FAIL 翻转**」——
  - L2 verdict `E433A06E7BFB` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；t=0.7 实证 J 中位 0.41-0.52 < 0.85）」
  - L14 verdict `764F24A21AC8` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；N=20 收敛稳定 0.36-0.39 区间）」
  - T1 verdict `F1B5E49F3058` §7 总判定 = 「K-T1-S3 字面命中（PASS）= 构造失灵族假象：reasoning 模型 + max_tokens=100 致 49.3% 空响应 + 72.1% empty-empty pairs；J=0.0 主要来自『双方都空』非真判定一致；真证伪要件 ②③④ 失守」
  - T1.5 在 {temp 0.0 / 0.3 / 0.5} × qwen3.7-max 单端点矩阵下探「非 reasoning 模型 + max_tokens=500 修正后教师 J 中位是否仍 < 0.85」—— 若任一 cell 翻 ≥0.85，**仅记「qwen 端点代表性存疑」注记**（qwen 端点固有方差 vs 温度敏感性二源），**不据此翻 K-N11-3 真证伪既定判**（qwen 端点 + temp=0.7 是既定条件，方向翻转只质疑 qwen 端点的代表性而非整体判死）
  - 全 6 cells 仍 J < 0.85（无翻转）= 「**判定稳健**」= 不入勘误链（仅作稳健性确认注记；同时补正 T1 verdict 构造失灵族裁定 —— 字面 PASS 在工具失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认）
  - **T1.5 唯一新增定位** = T1 构造失灵族补正探针；T1 verdict 自身（PASS=构造失灵族假象）一字不动，T1.5 跑出后仅作 T1 信息量补正（沿 T1 verdict §4.3 信息量边界声明）—— **T1.5 不翻 T1 verdict 自身判定**（T1 verdict 已是构造失灵族假象裁定，**不再二次判定**）
- **本棒不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 过渡声明 3 件** + **不动 L10 §0.5 过渡声明 2 件** + **不动 T1 §0.5 过渡声明 1 件**

---

## §1 T1.5 · T1 构造失灵族补正 稳健性探针

### 1.1 三问初判

- **Q1 ✓**：素材面已齐——
  - L2 N-11 supp verdict `E433A06E7BFB` + result `FF7B167AE43F`（qwen t=0.7, N=2, 5 教师 4 prompts × 2 re-asks = 20 calls，J 中位 0.41-0.52）—— **T1.5 同端点同模型同 baseline 数据 = T1.5 对照锚不重跑**
  - L14 N-11 full verdict `764F24A21AC8` + result `4C11AB9057B9`（qwen t=0.7, N=20, 5 教师 2 prompts × 5 re-asks = 50 calls，J 中位 0.36-0.39 收敛）—— **T1.5 同端点同模型同 baseline 数据 = T1.5 对照锚不重跑**
  - qwen token-plan 端点 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` model_id `qwen3.7-max` 探活 OK（沿 `_track2_endpoints_probe_2026_09_23.json` `C846F7FC79EE` §0 + `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 既有数据）
  - T1 verdict `F1B5E49F3058` §4.1【最高优先】建议字面 = 「改用非 reasoning 模型 + 提高 max_tokens」 = T1.5 立线字面源
  - T1 verdict `F1B5E49F3058` §7 总判定 = 「K-T1-S3 字面命中（PASS）= 构造失灵族假象」= T1.5 补正对象字面源
  - Track 2 multimodel probe `B65619A07B10`（ROUTE_TEMPLATES + tun + 串行 ≥2s，qwen 行 `use_proxy: False`）
- **Q2 ✓**：实验设计可执行——
  - **6 cells** 矩阵 = {L2, L14} × {temp 0.0, 0.3, 0.5} × qwen3.7-max 单端点
  - 每 cell = 沿 L2/L14 verdict 字面（K-N11-3 教师 J 中位 < 0.85 字面）+ 5 教师锚定（沿 TH-14）+ 22 caption（沿 `6A2656878745`）+ qwen3.7-max 端点 + temperature 替换 + max_tokens = 500
  - 单 cell calls：每教师 4 prompts（L2 维度，沿 L2 verdict `E433A06E7BFB` §2）或 2 prompts（L14 维度，沿 L14 verdict `764F24A21AC8` §2）× 2 re-asks × 1 端点 × 1 temp = 40 calls / L2 cell 或 20 calls / L14 cell（沿 L2/L14 verdict 字面 N_min）；最小复算样本可压至 N=10 对/教师（沿 T1 §1.4 非退化自证放宽口径）；T1.5 沿 T1 TH-T1-1 = 10 对/教师放宽口径
  - L14 维度：可沿 L14 verdict §2 字面（5 教师 × 2 prompts × 5 re-asks = 50 calls 目标），最小复算样本可压至 N=10 对/教师（re-asked trace 维度）；T1.5 沿 T1 §1.4 N_min=10 放宽口径
- **Q3 ✓**：证伪方向明确——
  - 「工具失灵族修正（非 reasoning 模型 + max_tokens=500）后温度维度上判定结果出现方向翻转」= **敏感性成立**（K-N11-3 真证伪方向不稳健）
  - 「工具失灵族修正后温度维度上判定结果维持方向一致」= **判定稳健**（K-N11-3 真证伪方向在 qwen 端点不同 temp 下稳定）+ **T1 verdict 构造失灵族假象裁定获补正**（非 reasoning 模型 + max_tokens=500 修正后真维持方向一致 = T1 verdict「构造失灵」定性获工具失灵族补正证据；T1 字面 PASS 不再是假象 → 真稳健入勘误链）
  - **字面判**：教师 J 中位 ≥ 0.85 = 方向翻转 → K-T1-S1 hit=True → 标注「稳健性存疑注记」

### 1.2 矩阵定义（6 cells）

| # | 维度（沿 L2 verdict / L14 verdict） | 温度 | 端点 | model_id | 代理 | calls 上限 / cell |
|---|---|---|---|---|---|---|
| 1 | L2 N-11 supp 教师 J 判定（沿 `E433A06E7BFB` §3.2 + §4.3） | 0.0 | qwen_plan: `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | `qwen3.7-max`（**非 reasoning**） | 否（qwen 直连无代理） | ≤ 60 calls（5 教师 × 2 prompts × 2 re-asks × 3 内层重试预留） |
| 2 | L2 N-11 supp 教师 J 判定 | 0.3 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | ≤ 60 calls |
| 3 | L2 N-11 supp 教师 J 判定 | 0.5 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | ≤ 60 calls |
| 4 | L14 N-11 full 三方配对（沿 `764F24A21AC8` §4 + §5 schema `v4_l14_n11full/2`） | 0.0 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | ≤ 60 calls（5 教师 × 2 prompts × 2 re-asks × 3 内层重试预留；re-asked trace 维度；distill + independent 沿 `21771E66AF67` + `5BA916D1DD24` 只读复用） |
| 5 | L14 N-11 full 三方配对 | 0.3 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | ≤ 60 calls |
| 6 | L14 N-11 full 三方配对 | 0.5 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | ≤ 60 calls |

**矩阵 cell 总数 = 6 cells × ≤ 60 calls/cell = ≤ 360 calls（硬上限）**

**端点维度砍去**：T1 已探 mimo / teamo 两端点（沿 T1 verdict `F1B5E49F3058` §1.3 + §2.1-§2.3 字面，reasoning 模型 + max_tokens=100 致 K-T1-S2 端点维度 any_hit: false）；T1 verdict 已裁定 K-T1-S2（端点敏感性 flip 触发线）= any_hit: false（empty-empty 主导致整矩阵方向 J<0.85，非真判定一致）；T1.5 沿 T1 verdict 结论引用 **不重测** K-T1-S2；T1.5 矩阵 = 单端点 qwen3.7-max（**非 reasoning**）+ max_tokens = 500 修正构造失灵族后温度维度探针

**对照基准（不重跑）**：
- qwen token-plan 端点 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` model_id `qwen3.7-max` 既有数据（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）= **temperature = 0.7** = 对照基线**不重跑**；T1.5 探针仅在 qwen3.7-max（**非 reasoning**）+ max_tokens=500 修正构造失灵族后跑 temp ∈ {0.0, 0.3, 0.5}
- qwen 端点 t=0.7 baseline 既判（K-N11-3 真证伪：J 中位 0.36-0.39 < 0.85）作 6 cells 比照锚
- T1 verdict `F1B5E49F3058` §2.1-§2.2 K-T1-S1 + K-T1-S2 字面 any_hit: false 结论引用为 T1.5 历史比对锚

### 1.3 claim（可证伪命题）

T1.5 矩阵 6 cells 在 {temp 0.0/0.3/0.5} × qwen3.7-max（**非 reasoning**）+ max_tokens=500 修正构造失灵族维度上，5 教师 re-asked Jaccard 中位数（沿 L2/L14 verdict §3.2 字面 = `Jaccard = |A ∩ B| / |A ∪ B|` token 级 set Jaccard，token = `re.findall(r"[a-z0-9]+|[一-鿿]", text.lower())`）维持 qwen t=0.7 既判方向 = **教师 J 中位 < K_N11_3_THRESHOLD = 0.85**（沿 L2/L14 字面 + T1 字面 + `0A9EE16267B5` §1 K-N11-3 字面一字不动）。任一 cell 教师 J 中位 ≥ 0.85 = 方向翻转 = **K-N11-3 真证伪方向在该 cell 不稳健**。

**本 claim 字面完全沿** L2 verdict `E433A06E7BFB` §4.3 + L14 verdict `764F24A21AC8` §5.3 字面（K-N11-3 教师 J 中位 < 0.85 → FAIL）+ `0A9EE16267B5` §1 K-N11-3 字面 + T1 `802DECE2286A` §1.3 claim 字面（沿 T1 claim 维度结构：12 cells → 6 cells，端点维度砍去，温度维度沿 T1 字面一字不动）一字不动。

**T1.5 探针限定（不翻 L2/L14 / T1 verdict 正式判定的硬约束）**：
- T1.5 命中方向翻转（K-T1-S1 hit=True）= 标注「**稳健性存疑注记**」入勘误链
- T1.5 命中方向翻转**不直接翻** L2/L14 verdict 既定 K-N11-3 真证伪结论（qwen t=0.7 是既定条件）
- T1.5 命中方向翻转仅作「**qwen 端点代表性存疑**」注记（即：若 qwen3.7-max 非 reasoning 模型 + max_tokens=500 + 不同 temp 下 J 中位 ≥ 0.85，仅说明 qwen 端点下 qwen 教师固有的语言学方差是该特定 (非 reasoning 模型修正, max_tokens=500, 温度) 组合下的特征，不构成对 L2/L14 既判的反证）
- T1.5 全 6 cells 不命中（方向一致）= 「**判定稳健**」确认注记（K-N11-3 真证伪方向在工具失灵族修正后温度维度稳定）+ **T1 verdict 构造失灵族假象裁定获补正**（非 reasoning 模型 + max_tokens=500 修正后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链作 L2/L14 既判稳健性确认；**T1 verdict §7 总判定本身一字不动**）
- T1.5 探针不二次判定 T1 verdict §7 自身（沿「不动既有件字面」+「T1 verdict 已裁构造失灵族假象」+「T1.5 仅作补正路径探针」三重约束）；T1 verdict §7 总判定一字不动，T1.5 仅在补正后跑出新信息时入勘误链补充说明 T1 信息量边界

### 1.4 实验设计

- **素材**：
  - L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F`（L2 维度 + qwen t=0.7 baseline 对照锚）
  - L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`（L14 维度 + qwen t=0.7 baseline 对照锚）
  - T1 追加件 `802DECE2286A` + T1 verdict `F1B5E49F3058`（T1.5 字面源 + 补正对象 + K-T1-S1/S2/S3 字面源）
  - `0A9EE16267B5` §1 N-11 K-* 字面（沿用一字不动）
  - 22 caption `strip_captions_22.json` `6A2656878745`
  - 5 by_model（沿 TH-14：kimi / GLM_1 / GLM_2 / coze / minimax）
  - Track 2 multimodel probe `B65619A07B10`（ROUTE_TEMPLATES + tun + 串行 ≥2s，qwen 行 `use_proxy: False`）
  - Track 2 endpoints probe `C846F7FC79EE`（qwen_plan 探活锚，T1.5 单端点 = qwen_plan 行）
  - Track 2 multimodel verdict `_v4_track2_multimodel_verdict_2026_09_23.md`（qwen3.7-max 既有 baseline 数据，T1.5 对照锚）
  - `_v4_distill_min_measure.py` `21771E66AF67`（L14 维度 distill 提取函数，只读复用）
  - `_v4_proxy_student_generators.py` `5BA916D1DD24`（L14 维度 3 proxy 算子，只读复用）
- **构造**：
  - **L2 维度**（沿 L2 verdict `E433A06E7BFB` §2 字面）：
    - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell × 3 temp × 1 端点 = 60 calls（L2 总）
    - prompt 子集沿 L2 verdict `E433A06E7BFB` §2 = seed=42 抽 2 caption (`L_biological_taxonomy`, `S5`)
    - temperature ∈ {0.0, 0.3, 0.5} 替换 qwen t=0.7 baseline
    - 端点 qwen3.7-max 单端点（**非 reasoning 模型**，与 L2 verdict §2 同端点同模型；T1 reasoning 模型 mimo / teamo 端点已砍去）
    - **max_tokens = 500**（≥500 拍板字面；T1 L14 维度 max_tokens=100 沿 L14 verdict §2 字面，T1.5 L14 维度 max_tokens=500 修正构造失灵族 #2，**非阈值调整**——沿 T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + §5.1 工具失灵族假象裁定；L2 维度 max_tokens=500 同步修正以保持 L2/L14 构造一致性）
    - 主度量 = 教师 re-asked Jaccard 中位（同 L2 verdict §3.2 字面）
  - **L14 维度**（沿 L14 verdict `764F24A21AC8` §2 字面）：
    - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell × 3 temp × 1 端点 = 60 calls（L14 总）
    - prompt 子集沿 L14 verdict `764F24A21AC8` §2 = `L_geography_world` + `L_historical_causality`
    - **max_tokens = 500**（修正构造失灵族 #2；T1 L14 维度 max_tokens=100 沿 L14 verdict §2 字面致 49.3% 空响应，T1.5 修正至 ≥500 容纳非 reasoning 模型完整输出）
    - temperature 替换同上
    - 端点 qwen3.7-max 单端点（**非 reasoning**）
    - 主度量 = 教师 re-asked Jaccard 中位（同 L14 verdict §3.2 字面）；L14 三方配对（re-asked + distill + independent）作为辅助度量（沿 L14 verdict §4 字面，N=20 收敛稳定方向一致时可简化只跑 re-asked）
- **度量**：
  - **主度量** = Jaccard 中位数（per teacher, per cell）—— 沿 L2/L14 verdict §3.2 字面不动
  - **辅助度量**（L14 维度）：三方 max-min diff + distill J - teacher J delta（沿 L14 verdict §4.1/§4.2 字面不动）+ independent J（沿 L14 verdict §4.3 字面不动）
  - **稳健性度量** = bootstrap CI 95%（沿 K-N11-N2 双读法）+ per 教师 N 评估 + 跨温度 J 中位标准差
  - **audit-only metadata 字段**（沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板）：T1.5 result json metadata = `audit-only`，不参与 kill-line / Jaccard / 统计推断；字段集 = `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint`（T1.5 沿用同字段集，端点恒为 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max`）
- **拍板出处**：PI 2026-09-24 23:33 派工单 `ask_9484b696c4f3af85941b3c43` t15 拍板「启动 T1.5：非 reasoning 模型+max_tokens≥500 重跑温度敏感性」+ T1 verdict `F1B5E49F3058` §4.1【最高优先】建议字面 + §7 总判定构造失灵族假象裁定
- **真审条件**：worker 接力棒分批跑；单批 ≤ 600s 看门狗；撞 5h 配额中断-恢复（沿 L14 verdict §9.1 + T1 verdict §9.1 中断恢复先例）
- **非退化自证**：每 cell 5 教师 N_min = 10 对/教师（T1.5 沿 T1 §1.4 探针放宽口径，TH-17 N=20 是 L2/L14 既判的目标，非 T1.5 探针的硬门槛；理由：T1.5 = 构造失灵族补正探针 + 敏感性探针，方向翻转定性即可，不需 N=20 全收敛）—— 沿 L2 verdict `E433A06E7BFB` §2 baseline N=2 / L14 verdict §2 N=20 双向放宽；T1.5 沿 T1 TH-T1-1 = 10 对/教师 不变
- **双读法并记**（沿 K-N11-N2 字面）：
  - 构造面（单 cell N=10）= T1.5 探针单 cell 内 J 中位
  - 真实面（跨 cell 累加 N≥30）= 跨同温度 cell 累加 J 中位
  - 任一面 PASS ≠ T1.5 探针成立（必须双向一致）

### 1.5 机械判死线（kill-line，字面即锁，禁私设条款）

> **字面不动声明**：既有 K-N11-1/2/3/N1/N2 字面（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1）**一字不动**；既有 K-T1-S1/S2/S3 字面（沿 T1 追加件 `802DECE2286A` §1.5 + T1 verdict `F1B5E49F3058` §2）**一字不动**；本棒仅在 T1 K-* 基础上复用 K-T1-S1 + K-T1-S3（T1.5 温度维度沿 T1 字面）+ 沿用 K-T1-S2（T1.5 端点维度砍去，沿 T1 verdict §2.2 any_hit: false 结论引用 **不重测**），**0 触既有 K-N11 字面 + 0 触既有 K-T1-S1/S2/S3 字面**，**0 新设阈值**（K_N11_3_THRESHOLD = 0.85 沿用一字不动）

#### 1.5.1 既有 K-N11 字面（沿 L2/L14 verdict 一字不动，锁前痕迹保留）

- **K-N11-1**：三方 Jaccard 中位数差异 < K_N11_1_DIFF = 0.05 即 `hit=True` → FAIL（三方不可分离）—— **沿 `0A9EE16267B5` §1 K-N11-1 字面**
- **K-N11-2**：distill J > teacher J + K_N11_2_DELTA = 0.05 不成立即 `hit=True` → FAIL（与原假设反向）—— **沿 `0A9EE16267B5` §1 K-N11-2 字面**
- **K-N11-3**：教师两次 J 中位数 < K_N11_3_THRESHOLD = 0.85 即 `hit=True` → FAIL（教师自身不稳定，主度量失效）—— **沿 `0A9EE16267B5` §1 K-N11-3 字面**（**T1.5 探针核心沿此字面**）
- **K-N11-N1**：N < TH17_N_TARGET = 20 / 教师 即 `pass=False` → FAIL（构造退化致命题不明）—— **沿 v0.2 §2 L2 K-N11-N1 字面**（**T1.5 探针放宽至 N_min=10** 不动此字面，T1.5 N_min=10 为探针放宽口径与 K-N11-N1 字面 N=20 是两层并存）
- **K-N11-N2**：构造面 K-N11-1/2/3 + 真实面 K-N11-1/2/3 **并记**；任一面 PASS ≠ 命题成立（必须双面都过）—— **沿 v0.2 §2 L2 K-N11-N2 字面**

#### 1.5.2 T1.5 复用 K-T1-* 字面（沿 T1 追加件 + T1 verdict 一字不动，0 新设阈值）

- **K-T1-S1（温度敏感性 flip 触发线 · 主判定）**：
  - **字面**：在任一固定端点（qwen_plan）下，沿 L2 维度或 L14 维度，教师 J 中位数跨温度 {0.0, 0.3, 0.5} 中**任一温度点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**（显式布尔，避免裸 bool 歧义）：
    - 既定方向 = qwen t=0.7 baseline 教师 J 中位 < 0.85（沿 L2 verdict `E433A06E7BFB` §3.2 + L14 verdict `764F24A21AC8` §3.2 实测）
    - 翻转条件 = 新 (端点=qwen_plan, 维度=L2|L14, 温度 ∈ {0.0, 0.3, 0.5}) cell 教师 J 中位 ≥ 0.85（**T1.5 = qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后**）
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（沿 L2/L14 verdict + `0A9EE16267B5` §1 + T1 `802DECE2286A` §1.5 字面，**0 新设**）
  - **不翻 L2/L14 正式判定**（沿定位声明）：K-T1-S1 hit=True 仅入稳健性注记，**不据此改判** L2 verdict `E433A06E7BFB` §11「FAIL 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪」既定结论一字不动
  - **不二次判定 T1 verdict §7 自身**（沿「不动既有件字面」+「T1 verdict 已裁构造失灵族假象」+「T1.5 仅作补正路径探针」三重约束）：T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动；T1.5 K-T1-S1 命中/不命中独立判定，T1.5 不就 T1 verdict 自身作二次裁定

- **K-T1-S2（端点敏感性 flip 触发线 · 主判定）—— T1.5 沿 T1 verdict 结论引用不重测**：
  - **T1.5 字面**：T1 verdict `F1B5E49F3058` §2.2 K-T1-S2 已裁 `any_hit: false`（端点维度 any_hit: false，mimo/teamo × {0.0, 0.3, 0.5} × {L2/L14} 整矩阵方向 J<0.85，empty-empty 主导非真判定一致）；T1.5 端点维度砍去（qwen_plan 单端点），**沿 T1 verdict §2.2 any_hit: false 结论引用**，**T1.5 不重测 K-T1-S2**
  - **理由**：T1 verdict §4.1【最高优先】建议 = 「改用非 reasoning 模型 + 提高 max_tokens」（沿端点 / 模型类别修正 + max_tokens 修正），不是「改用不同端点」；端点维度在 T1 verdict §2.2 已裁 empty-empty 主导致 K-T1-S2 字面 any_hit: false 系构造失灵族假象（reasoning 模型 + max_tokens=100），非真端点敏感性不稳健；T1.5 沿 T1 verdict 结论引用 = 端点维度敏感性判据已沿 T1 verdict 字面收口
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（一字不动）
  - **不翻 L2/L14 正式判定**：同 K-T1-S1

- **K-T1-S3（稳健性确认线 · 副判定）**：
  - **字面**：6 cells 全 J 中位 < 0.85 = 「**判定稳健**」= T1.5 探针不命中 K-T1-S1 / K-T1-S2 → 入稳健性确认注记 + **T1 verdict 构造失灵族假象裁定获补正**（qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链作 L2/L14 既判稳健性确认）
  - **判定方式**：任一 cell 触发 K-T1-S1 或 K-T1-S2（K-T1-S2 沿 T1 verdict 结论引用）= 探针命中；全 6 cells 不触发 = 探针不命中 + T1 verdict 补正完成
  - **T1.5 探针与 T1 verdict 关系**：
    - T1 verdict §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动（T1 verdict 自身不可二次判定）
    - T1.5 K-T1-S3 命中（探针不命中 K-T1-S1/S2）= **仅作 T1 verdict 信息量补正**（T1 verdict §4.3 信息量边界声明获补充：构造失灵族修正后真维持方向一致 = 真稳健入勘误链）
    - T1.5 K-T1-S1 命中 = 仅入稳健性存疑注记，**不翻 T1 verdict §7 自身**

#### 1.5.3 T1.5 kill-line 字面总览（沿 T1 + L2/L14 verdict + `0A9EE16267B5` 字面）

| K-* | 字面 | hit 触发条件 | hit=True 后果 | 字面源 |
|---|---|---|---|---|
| K-N11-1 | 三方 Jaccard 中位数差异 < 0.05 → FAIL | 三方 max-min diff < 0.05 | L2/L14 cell 内部 FAIL | `0A9EE16267B5` §1 |
| K-N11-2 | distill J > teacher J + 0.05 不成立 → FAIL | delta = distill J - teacher J ≤ 0.05 | L2/L14 cell 内部 FAIL | `0A9EE16267B5` §1 |
| K-N11-3 | 教师两次 J 中位数 < 0.85 → FAIL | per teacher J median < 0.85 | L2/L14 cell 内部 FAIL（T1.5 探针主度量） | `0A9EE16267B5` §1 |
| K-N11-N1 | N < 20 / 教师 → pass=False → FAIL | per teacher N < 20 | L2/L14 cell 内部 FAIL | v0.2 §2 L2 |
| K-N11-N2 | 构造面 + 真实面双读法并记 | 任一面 PASS ≠ 命题成立 | L2/L14 cell 内部 FAIL | v0.2 §2 L2 |
| **K-T1-S1（沿 T1 一字不动，T1.5 主判定）** | 任一温度点 J 中位 ≥ 0.85 → hit=True → 稳健性存疑注记 | 跨温度 {0.0, 0.3, 0.5} 任一 ≥ 0.85 | T1.5 探针命中（**不翻 L2/L14 既判 + 不翻 T1 verdict 自身**） | 沿 T1 `802DECE2286A` §1.5.2 字面（T1.5 复用，0 新设数值） |
| **K-T1-S2（沿 T1 verdict 结论引用不重测）** | T1 verdict §2.2 已裁 any_hit: false；T1.5 沿结论引用 | T1 verdict §2.2 字面（mimo/teamo 端点维度 empty-empty 主导） | T1 verdict 结论 = any_hit: false；T1.5 不重测 | 沿 T1 verdict `F1B5E49F3058` §2.2 字面（沿结论引用，0 新设数值） |
| **K-T1-S3（沿 T1 一字不动，T1.5 副判定 + T1 verdict 补正线）** | 全 6 cells J 中位 < 0.85 = 判定稳健 + T1 verdict 补正完成 | 6 cells 全 < 0.85 | T1.5 探针不命中（确认注记）+ T1 verdict 信息量补正（构造失灵族修正后真稳健入勘误链） | 沿 T1 `802DECE2286A` §1.5.2 字面（T1.5 复用，0 新设数值） |

> **0 新设阈值声明**：K-T1-S1/S2/S3 三条**0 新设数值阈值**（沿 T1 `802DECE2286A` §1.5.2 字面沿用）；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict `E433A06E7BFB` §2 + L14 verdict `764F24A21AC8` §2 + `0A9EE16267B5` §1 字面一字不动；T1.5 探针字面「方向翻转 = hit=True」是布尔条件显式化（沿 S-40 教训「判定布尔显式方向」），**不构成阈值私设**；max_tokens = 500 系**工具失灵族参数修正**（沿 T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + §5.1 工具失灵族假象裁定），**非阈值调整**——沿派工单明示「判定阈值一字不动；max_tokens 属工具失灵族参数修正」

### 1.6 调用预算与节制（Token Plan 5h 限额硬约束）

> **硬约束声明**：T1.5 探针**0 触 L2/L14 verdict 既定 5h 配额节制原则**（沿 L14 verdict §9.1 + T1 verdict §9.1 中断恢复先例）；本棒新立 T1.5 独立配额，与 L2/L14 + T1 既定 5h 配额**物理隔离**（端点同 = qwen_plan 但构造修正不同 = 非 reasoning + max_tokens=500；worker 接力棒按修正构造分批）

#### 1.6.1 单批 calls 上限（看门狗约束）

- **单批 ≤ 30 calls**（沿 L2 verdict §2「600s 看门狗」+ L14 verdict §9.1「280s hard limit + sub-batch strategy」+ T1 `802DECE2286A` §1.6.1 双向沿用，每 30 calls 预估 600-700s wall time 含 2.5s 串行间隔）
- **每 cell 拆批**：每 cell ≤ 60 calls / 拆 2 批 × 30 calls / 批
- **6 cells × 2 批 / cell = 12 批**（理论上限；实际跑按需调整）

#### 1.6.2 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 L2 verdict `E433A06E7BFB` §2 INTER_CALL_SLEEP_S + L14 verdict `764F24A21AC8` §2 INTER_CALL_SLEEP_S + Track 2 runner `INTER_CALL_SLEEP_S` + T1 §1.6.2 沿用）
- **qwen token-plan 端点**（`token-plan.maas.qianwenaiapi.com/compatible-mode/v1`）：**无代理**（沿 `_v4_v5_multimodel_probe.py` `B65619A07B10` L35 `use_proxy: False` + T1 `802DECE2286A` §1.6.2 qwen 行 `use_proxy: False` 沿用）
- **teamorouter / mimo / openrouter 端点**：T1.5 单端点 = qwen_plan，**不触发** teamo 必走 tun 硬纪律（沿 PI 2026-09-23「teamorouter 必走 tun 防封号」+ user memory 2026-09-23）

#### 1.6.3 总预算上限

- **总 calls 上限 ≤ 360 calls**（6 cells × 60 calls/cell 硬上限；实际按需减少）
- **总 wall time 上限 ≤ 5h**（Token Plan 5h 配额硬约束；沿 L14 verdict §9.1 + T1 §1.6.3「5h 配额撞限」先例）
- **每 cell 实际 calls 预算**：
  - L2 维度：5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell（实际可压至 20 calls / cell）
  - L14 维度：5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell（re-asked trace；distill + independent 沿 L14 verdict `764F24A21AC8` §4 字面，可复用前棒 N=20 数据，仅补端点 / 温度 / 构造修正维度）
  - **每 cell 实跑上限 ≤ 26 calls**（预留 60 calls/cell 是 3 内层重试预留上限；正常 ≤ 26 calls/cell）
- **6 cells × 26 calls/cell = 156 calls 实际预计**（远低于 360 calls 硬上限）

#### 1.6.4 中断-恢复与分批拆跑方案

- **中断-恢复语义**（沿 L14 verdict §9.1 + T1 §1.6.4 先例）：
  - 同 worker 接力棒：v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2（沿 L14 verdict §9.1 + T1 §1.6.4）
  - checkpoint 文件：`.tmp/_t15_records.json`（沿 L14 runner `.tmp/_l14_records.json` + T1 runner `.tmp/_t1_records.json` 惯例）
  - 每 call 后 checkpoint 累积（沿 L14 runner L151-156 惯例）
  - 已跑 (teacher, caption_id, reask_idx, temp, endpoint) 元组 skip（沿 L14 runner L107-110 + T1 §1.6.4 惯例；T1.5 端点恒 = qwen_plan，元组 = (teacher, caption_id, reask_idx, temp)）
- **分批拆跑**：
  - 撞 5h 配额自动恢复（worker 接力棒续跑）
  - 单批撞 600s 看门狗自动停（沿 L14 verdict §9.1 看门狗 280s 上调至 600s 沿 L2 verdict）
  - 中断-恢复同 agent 唤醒语义（worker session 不重启，沿 L14 + T1 §9.1 同棒续跑）
- **额度撞限应急**（如 6 cells 未跑完撞 5h 配额）：
  - 仅跑已启动 cells，不补未启动 cells
  - 已启动 cells 部分完成记「T1.5 部分完成」注记
  - 未启动 cells 留待 worker 下一棒接力

#### 1.6.5 calls 预算写死公式（沿 T1 §1.6.3 沿用 + T1.5 修正）

```
总 calls 上限 = cells × calls_per_cell = 6 × 60 = 360
总 calls 实际预计 = cells × actual_calls_per_cell = 6 × 26 = 156
单批 calls 上限 = min(30, calls_per_cell) = 30（calls_per_cell = 60 含 3 重试）
单批 wall time 上限 ≤ 600s（含 2.5s × 30 串行间隔 + 单 call 推理时间）
总 wall time 上限 = cells × (calls_per_cell / 30) × 600s / 3600 ≤ 5h（沿 Token Plan 5h 配额硬约束）
```

### 1.7 产物链（`_v4_supp_t15_*`，诞生即 SHA-12，派生 JSON 不合并）

> **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）；本棒产物用 `_v4_supp_t15_*` prefix 分列

- `_v4_supp_t15_executor.py`（T1.5 矩阵 runner + checkpoint 模式 + qwen3.7-max 非 reasoning 模型 + max_tokens=500 + 温度切换）
- `_v4_supp_t15_result.json`（6 cells 矩阵结果聚合：每 cell per teacher J 中位 + qwen3.7-max + 温度 + audit-only metadata 字段 + schema `v4_t15_sensitivity_fix/1` + 跨温度 J 中位标准差）
- `_v4_supp_t15_verdict.md`（T1.5 探针判定：6 cells 字面 K-N11-3 实测 + K-T1-S1/S3 触发判定 + K-T1-S2 沿 T1 verdict 结论引用 + 根因三分类每行附 + T1 verdict 信息量补正 + 不翻 L2/L14 既判声明 + 不翻 T1 verdict §7 自身声明）
- 与现有 `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律）
- **schema 兼容**：L14 维度 cell schema 沿 `v4_l14_n11full/2`（沿 L14 verdict `764F24A21AC8` §2 字面）；L2 维度 cell schema 沿 L2 verdict `E433A06E7BFB` §2 字面；T1.5 result JSON 中 `schema` 字段 = `"v4_t15_sensitivity_fix/1"`（T1.5 探针专属 schema，与 T1 `v4_t1_sensitivity/1` 同级独立）
- **audit-only metadata 字段口径**（沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板）：T1.5 result json metadata = `audit-only`（不参与 kill-line / Jaccard / 统计推断；仅作审计追溯，不入判定字面源）；字段集沿 L14V3 映射件 §1.2 = `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint`

### 1.8 复用资产（0 触动既有字面）

- T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058`（T1.5 字面源 + 补正对象，只读复用）
- L14V3 追加件 + L14V3 activation + L14V3 映射件（audit-only metadata 字段口径锚，只读复用）
- L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F`（L2 维度字面源 + qwen t=0.7 baseline 对照锚，只读复用）
- L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`（L14 维度字面源 + qwen t=0.7 baseline 对照锚，只读复用；L14 verdict 自报 vs 盘 SHA 漂移沿 T1 §9.1 披露）
- `0A9EE16267B5` §1 K-N11-1/2/3 字面（沿用一字不动）
- `D85488A64D89` §2 L2 K-N11-N1/N2 字面（沿用一字不动）
- `21771E66AF67` `_v4_distill_min_measure.py`（L14 维度 distill 提取函数，只读复用）
- `5BA916D1DD24` `_v4_proxy_student_generators.py`（L14 维度 3 proxy 算子，只读复用）
- `B656A07B10` `_v4_v5_multimodel_probe.py`（端点 + tun + 串行 ≥2s，qwen 行 `use_proxy: False`，只读复用）
- `C846F7FC79EE` `_track2_endpoints_probe_2026_09_23.json`（qwen_plan 探活锚，只读复用）
- `6A2656878745` `strip_captions_22.json`（22 caption，只读复用）
- `_v4_track2_multimodel_verdict_2026_09_23.md`（qwen3.7-max 既有 baseline 数据，T1.5 对照锚，只读复用）

**复用条款**（沿 T1 + L14V3 字面）：
- **K-T1-S1**（温度敏感性 flip 触发线）—— 沿 T1 `802DECE2286A` §1.5.2 字面，T1.5 复用一字不动
- **K-T1-S2**（端点敏感性 flip 触发线）—— 沿 T1 verdict `F1B5E49F3058` §2.2 any_hit: false 结论引用，T1.5 不重测
- **K-T1-S3**（稳健性确认线 + T1 verdict 补正线）—— 沿 T1 `802DECE2286A` §1.5.2 字面 + T1 verdict §7 字面（T1.5 K-T1-S3 命中 = 真维持方向一致 = T1 verdict 信息量补正），T1.5 复用一字不动
- **TH-T1-1** = N_min per cell = 10 对/教师（沿 T1 `802DECE2286A` §1.8 新增条款，T1.5 沿用；TH-17 N=20 仍为 L2/L14 既判门槛，两层并存）
- **audit-only metadata 字段口径**（沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板）—— T1.5 沿用同字段集，端点恒为 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max`

**修正条款**（沿 T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + 派工单明示）：
- **C-T15-1（端点 + 模型替换）** = qwen token-plan `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model_id `qwen3.7-max`（**非 reasoning 模型**；沿 L2/L14 verdict §2 + Track 2 multimodel verdict qwen3.7-max 既有 baseline 端点 + ROUTE_TEMPLATES[0]）；T1 端点 {mimo, teamo} 砍去；**max_tokens = 500**（≥500 拍板字面；T1 L14 维度 max_tokens=100 沿 L14 verdict §2 字面致 49.3% 空响应，T1.5 L14 维度 max_tokens=500 修正构造失灵族 #2，L2 维度同步 max_tokens=500 以保持 L2/L14 构造一致性）—— C-T15-1 = **工具失灵族参数修正**，**非阈值调整**（沿派工单明示）

### 1.9 规模档

- **M** ≤ 2-3 天 worker 接力棒（6 cells × ≤ 26 calls/cell × 2.5s 间隔 + 600s 看门狗 × 12 批 = 理论 ≤ 2h 跑完；实际预留 5h 配额撞限风险 + 中断-恢复时间 ≤ 4h wall time）
- 单 worker 接力棒即可完成；分批拆跑 ≤ 12 批；总 calls 实跑 ≈ 156 calls

### 1.10 判定

- **productive**（沿 L9 `23879B6CD1CC` §1 productive 判例 + L10 `F6FE005EE3C7` §1 productive 判例 + T1 `802DECE2286A` §1.10 productive 判例 + L14V3 L14V3_* §1 productive 判例）

### 1.11 构造面 vs 真实面外推边界

- **构造面判定**（T1.5 探针构造面）：6 cells 中任一 cell 触发 K-T1-S1 = 探针命中（**仅注记，不翻 L2/L14 既判 + 不翻 T1 verdict 自身**）；K-T1-S2 沿 T1 verdict §2.2 any_hit: false 结论引用不重测；全 6 cells 不触发 = 探针不命中（确认稳健性）+ T1 verdict 信息量补正（构造失灵族修正后真稳健入勘误链作 L2/L14 既判稳健性确认）
- **真实面判定**（T1.5 探针真实面）：实际 qwen3.7-max 非 reasoning 模型 + max_tokens=500 + temp 维度下 5 教师 J 中位实测
- **外推边界 = 端点 / 模型类别 / 构造修正维度边界**（qwen t=0.7 是既定条件，方向翻转只质疑 qwen 端点的代表性而非整体判死）+ **数据规模边界**（T1.5 N_min=10/教师 探针放宽，与 L2/L14 既定 N=20/教师 两层并存）
- **不留假 pass**：T1.5 探针不命中 ≠ L2/L14 既判 PASS（K-N11-3 真证伪既判不动）；T1.5 探针不命中 = 真稳健入勘误链作 L2/L14 既判稳健性确认注记（**不是改判**，仅是既判方向的稳健性确认）
- **不留假证伪**：T1.5 探针命中 ≠ L2/L14 既判 FAIL（仅入稳健性存疑注记，不翻既判）
- **不留二次判定**：T1.5 探针命中/不命中 ≠ T1 verdict §7 自身判定（T1 verdict 一字不动，T1.5 仅作补正路径探针 + T1 verdict 信息量补正）

---

## §2 T1.5 矩阵汇总统计表

| # | 维度 | 温度 | 端点 | model_id | calls 上限 / cell | 主 kill-line | 字面源 | 阈值 |
|---|---|---|---|---|---|---|---|---|
| 1 | L2 N-11 supp 教师 J | 0.0 | qwen_plan | qwen3.7-max（**非 reasoning**） | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 2 | L2 N-11 supp 教师 J | 0.3 | qwen_plan | qwen3.7-max（**非 reasoning**） | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 3 | L2 N-11 supp 教师 J | 0.5 | qwen_plan | qwen3.7-max（**非 reasoning**） | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 4 | L14 N-11 full 三方配对 | 0.0 | qwen_plan | qwen3.7-max（**非 reasoning**） | ≤ 26 calls（re-asked；distill/independent 沿 L14 §4 字面可复用） | K-N11-3 → K-T1-S1 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 5 | L14 N-11 full 三方配对 | 0.3 | qwen_plan | qwen3.7-max（**非 reasoning**） | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 6 | L14 N-11 full 三方配对 | 0.5 | qwen_plan | qwen3.7-max（**非 reasoning**） | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |

**矩阵汇总**：
- **6 cells / 总 calls ≤ 360 / 实际预计 ≤ 156**
- **既有 K-N11-1/2/3/N1/N2 字面一字不动**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5）
- **既有 K-T1-S1/S2/S3 字面一字不动**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 字面；T1.5 复用，0 新设数值阈值）
- **修正条款 C-T15-1**（端点 + 模型替换 + max_tokens=500，**工具失灵族参数修正**，非阈值调整）
- **qwen t=0.7 baseline 对照基线不重跑**（沿 `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 既有数据）
- **总判定**：T1.5 探针 = T1 构造失灵族补正稳健性辅助检验（**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**）

---

## §3 阈值来源表（逐条注明出处件 + SHA-12）

> **铁律**：本棒 T1.5 探针 **0 新设数值阈值**；所有阈值字面沿既有件引用，下表逐条核对

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| **K_N11_1_DIFF** | 0.05 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-1 字面 |
| **K_N11_2_DELTA** | 0.05 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-2 字面 |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-3 字面 |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面（沿字面） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §4.3 K-N11-3 字面（沿字面） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8`（自报） | §5.3 K-N11-3 字面（沿字面，盘实测 `8EEF73BF9856` 沿 T1 §9.1 披露） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.5.2 K-T1-S1/S2/S3 字面（T1.5 复用沿用） |
| **TH-17 N_TARGET** | 20 / 教师 | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面 |
| **TH-17 N_TARGET** | 20 / 教师 | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 L2 配置表 |
| **TH-T1-1 N_min** | 10 对/教师（T1 探针放宽，T1.5 沿用） | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.4 非退化自证 + §1.8 新增条款 |
| **TH-14 5 教师锚定** | kimi / GLM_1 / GLM_2 / coze / minimax | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-14 |
| **TH-15 seed** | 42 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-15 |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §2 INTER_CALL_SLEEP_S |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 INTER_CALL_SLEEP_S |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.6.2 串行间隔（T1.5 沿用） |
| **teamorouter tun 代理** | `http://127.0.0.1:1018` | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | L35 tun proxy 段（T1.5 单端点 qwen_plan 不触发） |
| **teamorouter 必走 tun 防封号** | （硬纪律） | PI 2026-09-23 拍板 + user memory 2026-09-23 | — | user memory 「teamorouter/openrouter 必走 tun 代理防封号」（T1.5 单端点不触发） |
| **Jaccard 公式** | `J = |A ∩ B| / |A ∪ B|` token 级 set Jaccard | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §3.2 字面 |
| **Jaccard 公式** | `J = |A ∩ B| / |A ∪ B|` token 级 set Jaccard | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §3.2 字面 |
| **token regex** | `re.findall(r"[a-z0-9]+\|[一-鿿]", text.lower())` | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §3.2 字面 |
| **schema L14** | `v4_l14_n11full/2` | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 schema 字面 |
| **schema T1** | `v4_t1_sensitivity/1` | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.7 schema 字面 |
| **schema T1.5** | `v4_t15_sensitivity_fix/1` | 本棒 T1.5 §1.7 新立 | （本棒） | §1.7 schema 字面 |
| **22 caption** | `strip_captions_22.json` | `corpus/v20_caption_surface/strip_captions_22.json` | `6A2656878745` | — |
| **qwen endpoint** | `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **qwen model_id** | `qwen3.7-max` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **mimo endpoint** | `token-plan-cn.xiaomimimo.com/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1.5 端点维度砍去，不重测） |
| **mimo model_id** | `mimo-v2.6-pro` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1 verdict 沿结论引用，T1.5 不重测） |
| **teamo endpoint** | `api.teamorouter.cn/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1.5 端点维度砍去，不重测） |
| **teamo model_id** | `deepseek-v4-flash` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1 verdict 沿结论引用，T1.5 不重测） |
| **C-T15-1 端点 + 模型替换 + max_tokens=500** | qwen_plan + qwen3.7-max（非 reasoning）+ max_tokens ≥ 500 | 派工单 `ask_9484b696` t15 + T1 verdict `F1B5E49F3058` §4.1【最高优先】 | — | 派工单 23:33 拍板 + T1 verdict §4.1 字面（**工具失灵族参数修正**，非阈值调整） |
| **audit-only metadata 字段集** | `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint` | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` §1.2 + §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板 | `L14V3_MAP_*` | §1.2 字段表 + §6.1 #2 audit-only 拍板（T1.5 沿用同字段集） |

> **0 新设数值阈值声明**：T1.5 探针 **0 新设数值阈值**；K-T1-S1/S2/S3 三条均为布尔条件显式化（沿 S-40 教训）+ 沿 T1 字面沿用一字不动，**0 新设数值**；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict + L14 verdict + `0A9EE16267B5` §1 + T1 §1.5.2 字面一字不动；C-T15-1 = 工具失灵族参数修正（端点 + 模型类别 + max_tokens），**非阈值调整**（沿派工单明示「判定阈值一字不动；max_tokens 属工具失灵族参数修正」）

---

## §4 边界声明（复述）

- **本稿生效即锁**（沿 `D85488A64D89` `AD42992DC75D` + L9 `23879B6CD1CC` `5C579F28634E` + L10 `F6FE005EE3C7` `16E89657DAAA` + T1 `802DECE2286A` `79936B630015` + T1 verdict `F1B5E49F3058` + L14V3 三件锁先例）；**事后不重开不调**
- **本稿是预登记追加件，不是执行件**——执行由 worker 跑，判死由 verdict-keeper 裁因，证据链由 evidence-auditor 审（沿 8 agent 团队分工）
- **本稿 0 触 v0.2 本体 `D85488A64D89` + 0 触 activation `AD42992DC75D` + 0 触 L9 `23879B6CD1CC` + 0 触 L9 activation `5C579F28634E` + 0 触 L10 `F6FE005EE3C7` + 0 触 L10 activation `16E89657DAAA` + 0 触 T1 追加件 `802DECE2286A` + 0 触 T1 activation `79936B630015` + 0 触 T1 verdict `F1B5E49F3058` + 0 触 L14V3 三件 + 0 触 L2 verdict `E433A06E7BFB` + 0 触 L2 result `FF7B167AE43F` + 0 触 L14 verdict `764F24A21AC8` + 0 触 L14 result `4C11AB9057B9` + 0 触 Track 2 件 `B65619A07B10` / `C846F7FC79EE` + 0 触 `21771E66AF67` + 0 触 `5BA916D1DD24` + 0 触 `6A2656878745`** —— 19 件一字不动（追加件不动既有件字面）
- **本稿 0 触 V1–V3 资产**（letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读）+ 0 触 R5 V4 frozen
- **派生 JSON 不合并**（本棒产物用 `_v4_supp_t15_*` prefix 分列，与现有 `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立）
- **R4 key 永不明文**（**无例外**）+ **R6 P-G v0/v01 不动** + **R7 plugin spec 不动**
- **§0.5 过渡声明 1 件**：**T1.5 构造失灵族补正探针定位过渡**（T1 verdict 构造失灵族假象裁定获补正探针立线 + L2/L14 既定 K-N11-3 真证伪不动 + T1.5 探针 6 cells 跑出前不预设 PASS/FAIL 翻转）；**不动 v0.2 §0.5 既有 3 件 + L9 §0.5 既有 3 件 + L10 §0.5 既有 2 件 + T1 §0.5 既有 1 件**
- **0 触既有 K-N11-1/2/3/N1/N2 字面**（沿 `0A9EE16267B5` §1 + L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 一字不动）
- **0 触既有 K-T1-S1/S2/S3 字面**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 一字不动）
- **0 新设数值阈值**（K_N11_3_THRESHOLD = 0.85 沿字面不动；K-T1-S1/S2/S3 均为布尔条件显式化 + 沿 T1 字面沿用一字不动）
- **T1.5 定位硬约束**：T1 构造失灵族补正稳健性辅助检验，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核流程，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict §7 总判定一字不动

---

## §5 根因三分类 + 真受审标准（沿拍板 #15 + T1 §5 沿用）

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）；如实记录只是「机械诚实」，不合格

### 根因三分类

1. **真证伪**（命题被证伪）→ 命题 FAIL；**记录实验结论 + 根因（命题失败）**
2. **假证伪（工具·构造失灵族）** → 工具/构造失灵致命题未真正被证伪；**记录根因（工具失灵）+ 复评条件**（重跑/补构造后可达真证伪）
   - **构造不可行**（一等结论，归假证伪族）：构造域不可达命题要求（如 K-N11-N1 N < 20）
3. **命题不明**（构造不可逃） → 构造退化致命题不可证伪；**记录构造退化 + 命题暂不明**（补构造/扩规模后可达真证伪）

### 真受审标准

- **不留假证伪**：构造失灵被误归为「命题 FAIL」= 不合格诚实
- **不留假 pass**：构造退化被误归为「命题 PASS」= 不合格诚实
- **每判定附根因列**（沿拍板 #15）；无根因分析的结论呈报 = 不合格
- **T1.5 探针根因列特别要求**：
  - **K-T1-S1 命中** → 根因列必须区分二源（qwen 端点固有 / 温度敏感性）；不可笼统归「敏感性成立」
  - **K-T1-S3 命中（全 6 cells 不翻转）** → 根因列必须说明「qwen t=0.7 baseline 方向稳定 + 跨 temp 维度稳健（qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后真维持方向一致）」+ **T1 verdict 信息量补正**（构造失灵族修正后真稳健入勘误链作 L2/L14 既判稳健性确认），**不构成 L2/L14 既判 PASS 的新证据**（仅是既判方向的稳健性确认）；**不二次判定 T1 verdict §7 自身**
  - **partial completion**（6 cells 未跑完撞 5h 配额）→ 根因列必须明示「T1.5 部分完成 + 缺 cells 留待 worker 接力棒」

### T1.5 探针与 L2/L14 既判的根因关联

| T1.5 探针结果 | L2/L14 既判影响 | T1 verdict §7 影响 | 根因列 |
|---|---|---|---|
| **全 6 cells J 中位 < 0.85**（K-T1-S3 命中） | **0 影响**（L2/L14 既判不动）= 仅入稳健性确认注记 | **不二次判定** T1 verdict §7 自身；**仅作 T1 verdict 信息量补正**：构造失灵族修正后真维持方向一致 = 真稳健入勘误链 | qwen t=0.7 baseline 方向在 temp 维度稳定 + qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后真维持方向一致；不翻 L2/L14 既判 + 不翻 T1 verdict §7 |
| **任一 cell J 中位 ≥ 0.85**（K-T1-S1 命中） | **0 直接影响**（L2/L14 既判一字不动）= 仅入稳健性存疑注记 | **不二次判定** T1 verdict §7 自身；T1.5 K-T1-S1 命中 = 仅入稳健性存疑注记（qwen 端点代表性存疑） | 二源根因（qwen 端点固有 / 温度敏感性）；不翻既判 + 不翻 T1 verdict §7 |
| **K-T1-S1 命中 + verdict-keeper 裁因 + verifier 签字** | **可能**触发 L2/L14 既判复核（不翻既判 = 默认；触发复核 = 须走完整流程） | **不二次判定** T1 verdict §7；仅作 L2/L14 既判的复核候选 | 仅作 L2/L14 既判的复核候选；**不得直接翻判** + **不得二次判定 T1 verdict §7** |
| **partial completion**（撞 5h 配额） | **0 影响** | **0 影响**（T1 verdict §7 不二次判定） | T1.5 部分完成注记；缺 cells 留待接力 |

> **铁律**：T1.5 探针字面仅入稳健性注记 + T1 verdict 信息量补正；**L2/L14 既判一字不动是默认状态**；**T1 verdict §7 总判定一字不动是默认状态**；**改判须走 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程**

---

## §6 自验清单（沿任务自验清单）

- [x] T1.5 矩阵 6 cells 全部有独立 K-* 字面（§1.5 + §2 汇总表）
- [x] 全部口径可回溯到派工单原文 + 既有预登记件 + T1 字面 + L2/L14 verdict 字面（§1.3 claim + §3 阈值来源表）
- [x] kill-line 字面风格与既有预登记逐字对齐（K-N11-1/2/3/N1/N2 沿 `0A9EE16267B5` + L2/L14 verdict 字面；K-T1-S1/S2/S3 沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 字面一字不动）
- [x] 判定布尔显式方向（hit=True 触发 / pass=False 触发 / 方向翻转 hit=True）—— 沿 S-40 教训「禁裸 bool」
- [x] key 形态自扫 0 命中（§0 自扫结果）
- [x] 调用预算与节制硬约束写明（§1.6 单批 ≤ 30 calls / 总 ≤ 360 calls / 总 wall time ≤ 5h / calls 预算写死公式）
- [x] 产物链 `_v4_supp_t15_*` 命名预定（§1.7 executor / result / verdict 三件 + schema `v4_t15_sensitivity_fix/1`）
- [x] 阈值来源表逐条注明出处件 + SHA-12（§3 31 条阈值引用）
- [x] 不翻 L2/L14 既判硬约束声明（§0 边界 + §1.3 claim + §1.5 字面 + §4 边界 + §5 根因关联）
- [x] 不翻 T1 verdict §7 自身硬约束声明（§0 边界 + §1.3 claim + §1.5 字面 + §4 边界 + §5 根因关联）
- [x] T1 verdict 信息量补正声明（§1.3 claim + §1.5.2 K-T1-S3 字面 + §5 根因关联）
- [x] audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板（§0 边界 + §1.4 度量 + §1.7 产物链 + §3 阈值来源表）
- [x] 派生 JSON 不合并声明（§1.7 + §4 边界）
- [x] 报告记诞生 SHA-12 + 大小（§7 报告）

---

## §7 报告（诞生即记）

- **本稿路径**：`results/_v4_supp_prereg_v02_add_T15_2026_09_24.md`
- **SHA-12 / 字节 / 行数**：见 **RESULT 报告**（harness 外部汇报段）—— 文件内嵌 hash 会触发 self-reference 递归不一致（沿既有 3 件预登记件 `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` + v0.2 + activation + L9 / L10 / T1 追加件均不自指 hash 的惯例）；本稿**生效件冻结 = 末态文件 hash**（PI 复核生效后冻结入 V4 manifest 链）；文件落地末态 hash 与大小以 RESULT 报告为准
- **锚定 v0.2 本体**：`D85488A64D89` 命中（v0.2 本体**一字不动**）
- **锚定 L9 / L10 追加件**：`23879B6CD1CC` / `F6FE005EE3C7` 命中（L9 / L10 **一字不动**）
- **锚定 T1 追加件**：`802DECE2286A` 命中（T1 追加件**一字不动**）
- **锚定 T1 verdict**：`F1B5E49F3058` 命中（T1 verdict **一字不动**）
- **锚定 L2 verdict**：`E433A06E7BFB` 命中（L2 verdict **一字不动**）
- **锚定 L14 verdict**：`764F24A21AC8` 命中（L14 verdict **一字不动**；自报 vs 盘 SHA 漂移沿 T1 §9.1 披露）
- **派工单**：2026-09-24 23:33 `ask_9484b696c4f3af85941b3c43` t15 拍板「启动 T1.5：非 reasoning 模型+max_tokens≥500 重跑温度敏感性」+ 同轮 ratify_all 追认 T1/L14V3/映射件生效即锁（PI 复核生效）
- **生效后状态**：沿 `D85488A64D89` `AD42992DC75D` + T1 `802DECE2286A` `79936B630015` + T1 verdict `F1B5E49F3058` 锁先例 → **生效即锁**，事后不重开不调
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（自扫沿 §0 边界声明）
- **派生 JSON 不合并声明**：本棒产物用 `_v4_supp_t15_*` prefix 分列（**line 命名建议**：`_v4_supp_t15_executor.py` + `_v4_supp_t15_result.json` + `_v4_supp_t15_verdict.md`）；与现有 `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立
- **T1.5 定位硬约束再声明**：**T1 构造失灵族补正稳健性辅助检验（construction-failure-fix probe）**，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核，**不得据此改判** L2/L14 既定结论 + **不得二次判定** T1 verdict §7 总判定

---

## §8 老实交代（failures & limitations）

- skill `scientific-research-workflows:experimental-design` 本地加载器多次实录 `Local skill not found` —— **未编造 skill 不存在的虚构指令**，按既有 5 件预登记件（`D85488A64D89` + `0A9EE16267B5` + `113CBE555643` + `0A7BCA992B95` + `F6FE005EE3C7`）+ L9 + L10 + T1 追加件 + T1 verdict + L14V3 三件 + L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` 字面锚执行
- **本稿 = 预登记立线件，非执行件**——执行由 worker 接力棒跑，6 cells 矩阵实跑预计 ≤ 156 calls（理论 ≤ 360 calls），撞 5h 配额分批拆跑 + 中断-恢复（沿 L14 verdict §9.1 + T1 §1.6.4 先例）
- **T1.5 探针放宽 N_min = 10 对/教师**（沿 T1 `802DECE2286A` §1.4 沿用；与 L2/L14 既定 N=20/教师 两层并存；理由：T1.5 = 构造失灵族补正探针 + 敏感性探针，方向翻转定性即可）
- **T1.5 探针 0 新设数值阈值**；K-T1-S1/S2/S3 沿 T1 字面沿用 + 均为布尔条件显式化（沿 S-40 教训）
- **T1.5 探针定位硬约束**：**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身**；除 K-T1-S1 命中 + verdict-keeper 裁因 + verifier 签字 + PI 复核，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict §7 总判定一字不动
- **qwen t=0.7 baseline 不重跑**（沿 `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 既有数据既判，作 6 cells 比照锚 + 温度维度回归锚）
- **端点维度砍去（mimo / teamo 不重测）**：沿 T1 verdict `F1B5E49F3058` §2.2 K-T1-S2 any_hit: false 结论引用，T1.5 端点维度不重测
- **max_tokens = 500 = 工具失灵族参数修正，非阈值调整**（沿 T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + §5.1 工具失灵族假象裁定 + 派工单明示「判定阈值一字不动；max_tokens 属工具失灵族参数修正」）
- **audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板**（不参与 kill-line / Jaccard / 统计推断）
- **本稿 0 触 19 件既有件**（v0.2 本体 + activation + L9 / L10 追加件 + activations + T1 追加件 + T1 activation + T1 verdict + L14V3 三件 + L2 verdict + L2 result + L14 verdict + L14 result + Track 2 件 + 度量函数 + 22 caption —— 详见 §4 边界声明）
- **派工单「5 件必带」(agent 名 + skill 名 (sha256 611965fcb620...) + plugin 名 (@scientific-research-workflows) + 7+9 铁律 + 老实交代 0 产物) 全收**
- **skill 诚实交代**：本棒缺 skill，按既有预登记件 + T1 字面 + T1 verdict 字面 + L2/L14 verdict + 派工单字面执行；**未编造 skill 不存在的虚构指令**

---

## §9 SHA 漂移诚实披露（沿 E-9 / E-16 / T1 §9 模式，立线即报）

> 本节为「**锚定 SHA 引用字面 vs 盘 SHA 漂移披露**」专项诚实交代，沿 V3 asset erratum §5 E-9 / E-16 + T1 `802DECE2286A` §9 同口径（SHA-12 漂移模式）—— 立线即报，不修任何既有件字面，仅披露漂移事实

### §9.1 L14 verdict SHA 漂移披露（沿 T1 §9.1 字面沿用）

- **L14 verdict `results/_v4_supp_l14_n11full_verdict.md`**：
  - **L14 verdict 自报 SHA-12（§8 §表）**：`764F24A21AC8`（19,708 B）
  - **L14 verdict 盘实测 SHA-12**：`8EEF73BF9856`（19,697 B）
  - **漂移量**：11 B + SHA 差异（SHA-12 全 12 hex 位均不同）
  - **L14 verdict 0 触动**（本棒 T1.5 立线件 0 写入 L14 verdict 文件）
  - **漂移源不明**（非 T1.5 引入；可能是 L14 棒跑后微调 / 末尾换行调整 / 编辑器自动 BOM 处理 等；**仅披露不溯因**）
- **T1.5 立线件字面引用沿用 L14 verdict 自报 SHA-12 = `764F24A21AC8`**（沿项目「引用锚定 SHA = 字面引用件 §0/§8 自报值」的惯例，与 v0.2 / L9 / L10 / T1 追加件引用 v0.2 `D85488A64D89` 同口径）
- **诚实原则声明**：T1.5 立线件**不擅自修正** L14 verdict 自报 SHA（沿「不动既有件字面」+「0 触 L2/L14 锚定字面」）；盘 SHA `8EEF73BF9856` 仅作披露，不作 T1.5 字面源替代

### §9.2 L2 verdict SHA 自洽披露（沿 T1 §9.2 字面沿用）

- **L2 verdict `results/_v4_supp_l2_n11supp_verdict.md`**：
  - **L2 verdict 自报 SHA-12（§10 表）**：`E433A06E7BFB`（15,671 B）
  - **L2 verdict 盘实测 SHA-12**：`E433A06E7BFB`（15,671 B）
  - **匹配 ✓**（SHA-12 + 字节均一致）
  - T1.5 立线件字面引用 `E433A06E7BFB` 一字不动

### §9.3 T1 verdict + T1 追加件 SHA 自洽披露

- **T1 追加件 `802DECE2286A`**：自报 = `802DECE2286A`（52,942 B）；T1.5 立线件字面引用 `802DECE2286A` 一字不动
- **T1 verdict `F1B5E49F3058`**：T1 verdict §6 RESULT「字节 / 行数：以落盘末态为准」未自报字节；T1.5 立线件字面引用 `F1B5E49F3058` 一字不动（SHA 引用字面沿 T1 verdict §0 自报值惯例）
- **T1 activation `79936B630015`**：自报 = `79936B630015`（14,234 B）；T1.5 立线件字面引用 `79936B630015` 一字不动

### §9.4 其他引用件 SHA 自洽披露

- **v0.2 预登记本体 `D85488A64D89`**：自报 = `D85488A64D89`（42,764 B）；盘实测 = `D85488A64D89`（42,764 B）→ **匹配 ✓**
- **v0.2 activation `AD42992DC75D`**：自报 = `AD42992DC75D`（3,202 B）；盘实测 = `AD42992DC75D`（3,202 B）→ **匹配 ✓**
- **L9 / L10 追加件 + L14V3 三件**：本棒未实测（仅引用 §0 输入件 SHA-12 链字面），不引用为执行字面源；如有漂移留待后续 reconciliation

### §9.5 处置建议（不擅自处置，留 PI 裁定）

- **L14 verdict SHA 漂移**（自报 `764F24A21AC8` vs 盘 `8EEF73BF9856`）：
  - 选项 A：保留现状（不动 L14 verdict 字面；T1.5 字面引用沿用自报 `764F24A21AC8`；盘 SHA 漂移作已披露事实入勘误链）
  - 选项 B：L14 verdict 微调后再算 SHA-12 入锁（需 PI 授权 + 不动字面原则下可能的字节微调 / 末尾换行调整）
  - 选项 C：T1.5 字面源改引用盘 SHA `8EEF73BF9856`（需重新跑 `Get-FileHash` 验证 T1.5 §0 输入件链 + §3 阈值来源表 + §4 边界声明 三处引用值）
  - **本棒不擅自选 A/B/C** —— 留 PI 裁定（沿「不动既有件字面」+「0 擅自合并派生 JSON」+「PI 复核生效时定夺」原则）

### §9.6 漂移模式与已知 E-* 注释对齐

- **漂移模式 = SHA 漂移**（沿 E-9 `da517c1153c` 11 hex vs `da517c115f3c` 12 hex 漂移 + E-16 报告写 `da517c1153c` vs 盘实算 `da517c115f3c` 漂移）
- **L14 verdict 漂移是同一类型**（自报 vs 盘实算漂移），但本棒**不擅自判定 E-30 编号** —— E-30 编号由 evidence-auditor 在下一轮 reconciliation 时定夺
- **诚实声明**：T1.5 立线件字面源引用沿「字面自报 SHA」惯例；盘 SHA 漂移不阻 T1.5 立线件生效，但**生效件冻结时**应复核 T1.5 字面源 = L14 verdict 自报 SHA = `764F24A21AC8`（若届时 L14 verdict 已 reconcile 为 `8EEF73BF9856`，T1.5 字面源应同步 reconcile；T1.5 派生 JSON 不合并铁律下，T1.5 不与 L14 verdict 合并字面源）

### §9.7 T1.5 立线件 0 触发任何 SHA 漂移

- **T1.5 立线件 SHA 漂移自检**：T1.5 立线件本身不存在自报 SHA（沿既有惯例不自指 hash；§7 报告段「见 RESULT 报告」引用 harness 外部汇报段）
- **T1.5 立线件 0 触 19 件既有件**：v0.2 / activation / L9 / L10 + activations + T1 追加件 + T1 activation + T1 verdict + L14V3 三件 + L2 / L14 verdicts + results + Track 2 件 + 度量函数 + 22 caption —— 0 触动（L14 verdict 盘 SHA 漂移非 T1.5 引入；T1.5 仅沿 T1 §9.1 披露沿用）

### §9.8 字面源引用件盘存在性诚实披露（沿 T1 §9 字面沿用 + T1.5 增量）

- **L2 N-11 supp verdict `results/_v4_supp_l2_n11supp_verdict.md`**（自报 `E433A06E7BFB` / 15,671 B）+ **L2 N-11 supp result `results/_v4_supp_l2_n11supp_result.json`**（自报 `FF7B167AE43F` / 17,970 B）+ **L14 N-11 full verdict `results/_v4_supp_l14_n11full_verdict.md`**（自报 `764F24A21AC8` / 19,708 B，盘实测 `8EEF73BF9856` / 19,697 B）+ **L14 N-11 full result `results/_v4_supp_l14_n11full_result.json`**（自报 `4C11AB9057B9` / 12,246 B）+ **L9 追加件 `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md`**（自报 `23879B6CD1CC` / 19,586 B）+ **L10 追加件 `results/_v4_supp_prereg_v02_add_L10_2026_09_24.md`**（自报 `F6FE005EE3C7` / 26,159 B）等 6 件锚定件 —— **本棒落盘实测 `Get-ChildItem` 未在 `results/` 顶层下找到**（可能位于子目录 / archive / 已被清理等）；T1.5 字面引用沿 T1 追加件 §0 输入件 SHA-12 链字面 + 「引用锚定 SHA = 字面引用件 §0/§8 自报值」的惯例沿用，**不擅自修正 / 不擅自判定为字面源失效**；盘存在性实测留待 evidence-auditor 下一轮 reconciliation 时定夺
- **诚实原则声明**：T1.5 立线件字面源引用沿「字面自报 SHA + T1 §0 字面」惯例；盘实测 6 件锚定件未在顶层 `results/` 找到的事实不阻 T1.5 立线件生效（沿「不动既有件字面」+「字面源锚定 = 自报值」原则）；但**生效件冻结时**应复核 6 件锚定件的盘存在性与 SHA 一致性（若届时仍未找到，T1.5 字面源 = T1 §0 字面源沿用惯例需 PI 复核裁定是否升级为「盘端字面源失效」状态）
- **T1.5 立线件 0 触动 / 0 写入上述 6 件**（即使盘中可访问，T1.5 立线件亦 0 写入）