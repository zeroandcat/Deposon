# V4 补测预登记 v0.2 T1.5r2 修订追加件 · T1.5 扩样修订 N_min≥10 字面满足规化（2026-09-26）

- **性质**：protocol-keeper 修订立线（派工单 2026-09-26 16:26 t15_ext 拍板 `ask_57981c1bc81e03b9990a06e5`「+60 calls 规化重跑（N_min≥10 字面满足）」；本棒 = **T1.5 prereg §1.4 计划（20 calls/cell → 6 pairs/教师）与 §1.8 N_min=10 字面的结构 gap 修复**——扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）；总增量 = 6 cells × +10 = +60 calls（沿 T1.5 verdict `52C985429C91` §3.4 补正建议字面）；本稿不调用任何 LLM，不跑实验，仅固化 T1.5r2 扩样修订立线 + 修订矩阵字面 + kill-line 字面不动 + 调用预算 + 阈值来源表（沿用字面） + 沿 T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` + T1 verdict `F1B5E49F3058` + L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8`（自报）+ L14V3 三件 + 既有 5 件预登记先例）
- **定位（边界）**：**T1.5r2 = T1.5 prereg §1.4 计划扩样修订（plan 字面 20 → 30 calls/cell）+ K-N11-N1 字面 FAIL 根因 = 假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）根因消除**；**不动** T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` + T1 verdict `F1B5E49F3058` + L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8`（自报）+ L2 result `FF7B167AE43F` + L14 result `4C11AB9057B9` + L14V3 三件 + v0.2 `D85488A64D89` + activation `AD42992DC75D` + L9 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + T1 追加件 `802DECE2286A` + T1 activation `79936B630015`；T1.5 矩阵 / 端点 / 模型 / max_tokens / 温度维度 / claim / kill-line 字面 **0 触**
- **T1.5 构造失灵族补正探针定位不变**：本棒 = T1.5 扩样修订件，**不翻 L2/L14 正式判定** + **不翻 T1 verdict §7 自身** + **不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面命中（PASS）**；T1.5 verdict §3.4 建议已拍板「+60 calls 接力棒扩 N」+ T1.5 verdict §4.4 建议已拍板「补跑 2 失败 calls（方案 A）」，本棒 = 建议落地为新立线修订件
- **预登记件本体不动（重述）**：`results/_v4_supp_prereg_v02_2026_09_24.md` SHA-12 `D85488A64D89` 锁后**一字不改**；T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` 锁后**一字不动**；本棒以独立追加件形式立线（沿 T1.5 prereg + L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` + T1 `802DECE2286A` + L14V3 三件 + 各自 activation 先例）
- **PI 复核待生效**（沿 `D85488A64D89` activation `AD42992DC75D` + L9 activation `5C579F28634E` + L10 activation `16E89657DAAA` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` + T1.5 activation `443EFB39804A` 锁先例）—— T1.5r2 立线 + 修订矩阵字面 + 修订调用预算 + 产物链 `_v4_supp_t15r2_*` 待 PI 复核生效；**生效即锁**（沿 `0A7BCA992B95` 锁先例），事后不重开不调；**「CONDITIONAL PASS」退役**，只用 PASS / FAIL 二值（沿 R6 实证）
- **范围**：T1.5r2 = T1.5 矩阵扩样修订（沿 T1.5 prereg `8898B964A9D9` §1.2 6 cells 矩阵字面）= {L2, L14} × {temp 0.0, 0.3, 0.5} × qwen3.7-max 单端点 = **6 cells 矩阵不变**；单 cell plan 字面修订 = 20 calls/cell（5 教师 × 2 prompts × 2 re-asks） → **30 calls/cell**（5 教师 × 2 prompts × **3 re-asks**）= +10 calls/cell × 6 cells = **+60 calls 总增量**；端点 = qwen token-plan `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` 单端点 = **0 触**；model = `qwen3.7-max`（**非 reasoning 模型**）= **0 触**；max_tokens = 500 = **0 触**（沿 T1.5 prereg §1.4 C-T15-1 字面「工具失灵族参数修正，非阈值调整」）；温度维度 {0.0, 0.3, 0.5} = **0 触**；schema `v4_t15_sensitivity_fix/1`（T1.5 原件 schema）下扩样 → 派生独立 schema `v4_t15r2_sensitivity_fix_n10/1`（仅 schema 版本号扩样字段，0 触 T1.5 原 schema 数值字面）；audit-only metadata 字段集（沿 L14V3 映射件 §1.2）= **0 触**；2 calls 超时缺位（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）补跑 = 沿 T1.5 verdict `52C985429C91` §4.4 方案 A 拍板（**PI 已通过 2026-09-26 16:26 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 显式确认「+60 calls 规化重跑」+ 沿 §3.4 字面推荐 = **方案 A = 补跑**），2 补跑 calls 计入 60 calls 预算内
- **判定依据**：deposon 项目核心准则四条「大材小用，落到实处，与死同行，虚实回路（FTFB）」（PI 2026-09-22 R1 录入 + 2026-09-23 FTFB 入根 + **准则为根，论文为一处外显**；详见 `113CBE555643` §0 注）—— 三问映射沿既有预登记件 §1.1.1 代拟稿 §1 + 种子稿 §0 + 整合补充稿 §1（沿 `0A7BCA992B95` §1）

---

## 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | SHA-12 | 字节 | 用途 |
|---|---|---|---|---|
| v0.2 预登记本体（锚定不动） | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | 42,764 | T1.5r2 立线锚定 + 通用条款格式（TH-* / 派生 JSON / 双读法 / 阈值表） |
| v0.2 activation 件 | `results/_v4_supp_prereg_v02_activation_2026_09_24.md` | `AD42992DC75D` | 3,202 | T1.5r2 立线后状态沿 `AD42992DC75D` 锁先例 |
| L9 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md` | `23879B6CD1CC` | 19,586 | T1.5r2 立线锚定 + 双读法并记先例（K-A2R-R1/N1） |
| L9 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md` | `5C579F28634E` | 3,924 | T1.5r2 立线后 L9 沿 `5C579F28634E` 锁先例 |
| L10 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L10_2026_09_24.md` | `F6FE005EE3C7` | 26,159 | T1.5r2 立线锚定 + 语义反转注释先例（K-E-N20-3 语义反转双栏并记） |
| L10 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L10_activation_2026_09_24.md` | `16E89657DAAA` | 9,442 | T1.5r2 立线后 L10 沿 `16E89657DAAA` 锁先例 |
| T1 追加件（锚定不动，T1.5r2 字面源 1） | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | 52,942 | T1.5r2 立线锚定 + K-T1-S1/S3 字面源 + T1 verdict §1-§5 字面 |
| T1 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936B630015` | 14,234 | T1.5r2 立线后 T1 沿 `79936B630015` 锁先例 |
| T1 verdict 件（锚定不动，T1.5r2 字面源 2） | `results/_v4_supp_t1_verdict.md` | `F1B5E49F3058` | 27,538 | T1.5r2 字面源（裁定「字面 PASS=构造失灵族假象」+ §4.1 建议改用非 reasoning 模型+max_tokens ≥500） |
| **T1.5 prereg 件（锚定不动，T1.5r2 字面源 3）** | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | 76,991 | T1.5 矩阵字面源 + §1.4 plan 字面（待修订）+ §1.5 kill-line 字面源（0 触）+ §1.6 调用预算字面源（0 触）+ §1.7 产物链字面源（0 触）+ §1.8 N_min 字面源（0 触） |
| **T1.5 activation 件（锚定不动）** | `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `443EFB39804A` | 20,751 | T1.5 沿 `443EFB39804A` 锁先例 |
| **T1.5 result 件（锚定不动）** | `results/_v4_supp_t15_result.json` | `6B47D389B7AE` | 53,265 | T1.5 120 calls 实测（6 cells × 20 calls + 2 失败原状）= T1.5r2 起始状态锚定 |
| **T1.5 verdict 件（锚定不动，T1.5r2 字面源 4）** | `results/_v4_supp_t15_verdict.md` | `52C985429C91` | 53,265 | T1.5r2 §3.4 +60 calls 接力棒扩 N 补正建议字面源 + §4.4 方案 A 补跑 2 失败 calls 字面源 + §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS 一字不动声明字面源 |
| L14V3 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `L14V3_*`（自身 SHA） | 61,547 | T1.5r2 立线锚定 + audit-only metadata 字段口径锚（0 触） |
| L14V3 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `L14V3_ACT_*`（自身 SHA） | 21,309 | T1.5r2 立线后 L14V3 沿同锁先例 |
| L14V3 映射件（锚定不动） | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | `L14V3_MAP_*`（自身 SHA） | — | T1.5r2 audit-only metadata 字段口径沿 §6.1 #2 拍板（0 触） |
| 方法预登记补充稿 | `results/_v4_methods_prereg_supplement_2026_09_23.md` | `0A7BCA992B95` | 59,570 | §1 通用条款 + 格式基线 |
| N-09~N-39 预登记 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | 60,530 | §1 K-N11 字面（L2/L14 判定件均沿此字面一字不动） |
| 种子预登记补充稿 | `results/_v4_seeds_prereg_supplement_2026_09_23.md` | `113CBE555643` | 53,633 | §0 注 + 格式基线 |
| **L2 N-11 supp verdict（锚定 T1.5r2 字面源 5）** | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | 15,671 | K-N11-1/2/3/N1/N2 字面（沿 `0A9EE16267B5` §1）+ 教师 J 实测 (qwen t=0.7, N=2, J 中位 0.41-0.52) |
| L2 N-11 supp result | `results/_v4_supp_l2_n11supp_result.json` | `FF7B167AE43F` | 17,970 | L2 N-11 supp 数据（qwen 端点） |
| **L14 N-11 full verdict（锚定 T1.5r2 字面源 6）** | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测） | 19,708（自报）/ 19,697（盘实测） | K-N11-1/2/3/N1/N2 字面 + schema `v4_l14_n11full/2` + 教师 J 实测 (qwen t=0.7, N=20, J 中位 0.36-0.39) |
| L14 N-11 full result | `results/_v4_supp_l14_n11full_result.json` | `4C11AB9057B9` | 12,246 | L14 N-11 full 数据（qwen 端点） |
| Track 2 multimodel probe | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | — | 三端点 ROUTE_TEMPLATES + tun 代理 + 串行 ≥2s（0 触） |
| Track 2 endpoints probe | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | 5,803 | qwen_plan / mimo / teamo 三端点权威源（T1.5r2 单端点 = qwen_plan 行） |
| Track 2 multimodel verdict (件 3) | `results/_v4_track2_multimodel_verdict_2026_09_23.md` | （自身 SHA） | 12,883 | 6 模型补跑判定（qwen3.7-max / mimo / teamo 等） |
| **T1.5 executor（锚定不动，T1.5r2 起始状态）** | `results/_v4_supp_t15_executor.py` | `558E635F9BA6` | 62,285 | T1.5 120 calls executor（6 cells × 20 calls + 2 失败原状）—— T1.5r2 接力棒 = 新件 `_v4_supp_t15r2_executor.py`，T1.5 executor **0 触** |

> 注：L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8`（自报）/ `8EEF73BF9856`（盘实测）字面引用沿 T1 §9.1 + §9.2 SHA 漂移披露惯例；T1.5r2 字面源锚定沿自报值 `764F24A21AC8`；L14 verdict 自报 vs 盘 SHA 漂移 11 B + 12 hex 全异（沿 T1 verdict `F1B5E49F3058` §5.2 limitations 披露）；本棒 0 触 L14 verdict 字面。

---

## §0 边界声明（沿 R5 / R6 / R7 复审稿，2026-09-23 勘误版 + 修订件特有边界）

- **0 LLM 调用**：本稿由 protocol-keeper 起草，全程未调用任何 LLM API；纯文件编辑（write/edit），未调任何 LLM/代理/构造代理/网关；沿 V4 §3.1 放开语境明示可调（PI 2026-09-22「V3 的剑不斩 V4 的官」），本棒无需调
- **R4 key 永不明文**（**无例外**，沿 R4 + PI 2026-09-22「key 永不明文等合理且无冲突的铁律要沿用」）：本稿及其后续产物不写入、不引用、不打印任何明文 API key / 平台密钥；key 仅在进程组方法里以 runtime env 读取；**本稿自扫** `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态 0 命中
- **R5 V4 frozen 只追加**（**V4 沿用 V1–V3 资产只读底线**）：本稿不修改 v0.2 预登记件 `D85488A64D89` / 不动 activation 件 `AD42992DC75D` / 不动 L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` / 不动 L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` / 不动 T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` / **不动 T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` + T1.5 executor `558E635F9BA6`** / 不动 L14V3 追加件 + L14V3 activation + L14V3 映射件 / 不动 L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` / 不动 L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`；**派生 JSON 不合并**（本棒产物用 `_v4_supp_t15r2_*` prefix 分列，与现有 `_v4_supp_t15_*` + `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；T1.5 executor `558E635F9BA6` 0 触动 + T1.5 result `6B47D389B7AE` 0 触动）
- **R6 P-G v0/v01 / R7 plugin spec**：本棒不动 P-G v0/v01；不动 plugin spec；不动 verifier 内置脚本
- **V1–V3 只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）
- **kill-line 字面不动禁私设条款**（S-40 教训：判定布尔显式方向 `hit=True` 即触发 / `pass=True` 即存活，禁裸 bool；PI 2026-09-23 拍板明示「禁止擅自调阈值 / 禁止合并派生 JSON / 禁止私设 kill-line 条款」）：本棒 T1.5r2 kill-line 字面**完全沿** T1.5 prereg `8898B964A9D9` §1.5 + T1 verdict `F1B5E49F3058` §2 字面（K-N11-1/2/3/N1/N2 + K-N11-N2 双读法 + K-T1-S1 温度敏感性 flip 触发线 + K-T1-S2 沿 T1 verdict §2.2 any_hit: false 结论引用 **不重测** + K-T1-S3 稳健性确认线一字不动），**0 触既有 K-N11 字面 + 0 触既有 K-T1-S1/S2/S3 字面**；**阈值一律沿 T1 + L2/L14 字面 = K_N11_3_THRESHOLD = 0.85** 等，**禁新设**
- **0 擅调阈值**（沿 v0.2 §0 + T1 `802DECE2286A` §0 + T1.5 `8898B964A9D9` §0 同口径）：本棒 **0 调既有 K_N11_1_DIFF = 0.05 / K_N11_2_DELTA = 0.05 / K_N11_3_THRESHOLD = 0.85 / TH17_N_TARGET = 20 / TH-T1-1 = 10**；T1.5r2 沿用一字不动；T1.5r2 仅**修订 plan 字面**（20 calls/cell → 30 calls/cell），**0 触阈值字面**；本修订 = **构造失灵族参数扩展**（沿 T1.5 verdict `52C985429C91` §3.4 补正建议字面「构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致」+ T1 verdict `F1B5E49F3058` §4.1【最高优先】建议字面 + §5.1 工具失灵族假象裁定），**非阈值调整**——沿派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板「+60 calls 规化重跑（N_min≥10 字面满足）」+ 同源明示「判定阈值一字不动；扩样 = plan 字面修订」
- **T1.5r2 定位硬约束**：本棒 = T1.5 prereg §1.4 计划扩样修订件，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS**；除 T1.5r2 kill-line 命中（方向翻转 = hit=True）**且另走 verdict-keeper 裁因 + verifier 签字 + PI 复核流程**，**不得据此改判** L2/L14 既定结论（沿 L2 verdict `E433A06E7BFB` §11「FAIL K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪 qwen 固有方差」既定结论一字不动）
- **构造修正（非阈值，非私设）**：本棒仅修订 T1.5 prereg `8898B964A9D9` §1.4 plan 字面 = 5 教师 × 2 prompts × **2** re-asks → **3** re-asks = 30 calls/cell（沿 T1.5 verdict `52C985429C91` §3.4「+60 calls 接力棒扩 N 至 N_min 满足：5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls」字面 + 派工单 t15_ext 字面拍板「扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）；总增量 = 6 cells × +10 = +60 calls」），**C-T15-1 = qwen3.7-max 非 reasoning + max_tokens=500 双端点字面不动**（沿 T1.5 prereg §1.4 + §1.8 字面 + 派工单 t15_ext 拍板明示「判定阈值一字不动」）
- **2 calls 超时缺位补跑计入预算**（沿 T1.5 verdict `52C985429C91` §4.4 方案 A 字面「补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑」+ 派工单 t15_ext 拍板「2 calls 超时缺位顺带补跑（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）计入 60 calls 预算」）：2 补跑 calls 计入 +60 calls 总增量内（cell 2/3 各含 coze/GLM_1 重跑 r0/r1 1 call + 9 额外 re-asks 全员 = cell 2 +10 calls + cell 3 +10 calls；cell 0/1/4/5 各 +10 calls 纯新跑 = 30 calls/cell）
- **audit-only metadata 字段口径**（沿 L14V3 映射件 §6.1 #2 PI 拍板 `ask_9484b696` `meta_field`）：T1.5r2 产物链 `_v4_supp_t15r2_executor.py` + `_v4_supp_t15r2_result.json` + `_v4_supp_t15r2_verdict.md` 中 result json metadata 字段 = **audit-only**（不参与 kill-line 计算 / 不参与 Jaccard 度量 / 不参与统计推断；仅作审计追溯，不入判定字面源）；沿 L14V3 映射件 §1.2 拍板字段集：`v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint`（T1.5r2 沿用同字段集，端点恒为 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max`）
- **skill 加载老实交代**：派工单要求 `scientific-research-workflows:experimental-design` skill，本地 skill 加载器多次实录 `Local skill not found`（沿 v0.2 §0 + L9 §0 + L10 §0 + T1 §0 + T1.5 §0 + L14V3 §0 同口径）—— 本棒按 v0.2 `D85488A64D89` + activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058` + **T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91`** + L14V3 三件 + 既有 5 件预登记件 `113CBE555643` `0A7BCA992B95` `0A9EE16267B5` + L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` 的格式与字面锚执行，**未编造 skill 不存在的虚构指令**

---

## §0.5 过渡声明（本棒 T1.5r2 立线件特有）

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）

- **T1.5r2 扩样修订定位过渡**：自本件立线起标「**已知 T1.5 verdict `52C985429C91` §1 主读法已裁『判定稳健确认 + T1 verdict 信息量补正成立』；T1.5 verdict §3.4 已拍板『+60 calls 接力棒扩 N 至 N_min 满足』建议（方案 A = 扩 N）；T1.5 verdict §4.4 已拍板『补跑 2 失败 calls』建议（方案 A = 补跑）；T1.5r2 = 该两件建议落地为新立线修订件**」——
  - L2 verdict `E433A06E7BFB` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；t=0.7 实证 J 中位 0.41-0.52 < 0.85）」
  - L14 verdict `764F24A21AC8` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；N=20 收敛稳定 0.36-0.39 区间）」
  - T1 verdict `F1B5E49F3058` §7 总判定 = 「K-T1-S3 字面命中（PASS）= 构造失灵族假象：reasoning 模型 + max_tokens=100 致 49.3% 空响应 + 72.1% empty-empty pairs；J=0.0 主要来自『双方都空』非真判定一致；真证伪要件 ②③④ 失守」
  - T1.5 verdict `52C985429C91` §1 主读法总判定 = 「K-T1-S3 字面命中（PASS）= 真稳健入勘误链 + 构造失灵族修正后真维持方向一致 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」
  - T1.5 verdict `52C985429C91` §3.4 补正建议 = 「+60 calls 接力棒扩 N 至 N_min 满足：5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls；checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）」
  - T1.5 verdict `52C985429C91` §4.4 补正建议 = 「补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）；预计 +2 calls + 2.5s × 1 = < 5min wall time」（方案 A）
  - T1.5r2 = T1.5 prereg §1.4 plan 字面扩样修订件（20 calls/cell → 30 calls/cell = 5 教师 × 2 prompts × 3 re-asks）+ 2 calls 缺位补跑 + 派生独立产物链 `_v4_supp_t15r2_*` + 不动 T1.5 矩阵 / 端点 / 模型 / max_tokens / 温度维度 / kill-line / claim / 阈值字面
  - T1.5r2 命中方向翻转（K-T1-S1 hit=True）= 标注「**T1.5r2 方向翻转稳健性存疑注记**」入勘误链（**仅注记，不翻 L2/L14 既判 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法**）
  - T1.5r2 全 6 cells 不命中（方向一致）= 「**T1.5r2 判定稳健确认**」+ K-N11-N1_T1relax 字面 FAIL 根因消除（plan 字面 30 calls/cell → 15 pairs/教师 ≥ N_min=10 字面满足）= 「**K-N11-N1_T1relax 字面 PASS**」（沿 T1.5 verdict `52C985429C91` §3 假证伪族根因消除）+ T1.5 verdict §3.4 建议落地确认注记
  - **T1.5r2 唯一新增定位** = T1.5 prereg §1.4 plan 字面扩样修订件（plan 字面 20 → 30 calls/cell）；T1.5 prereg + result + verdict 一字不动，T1.5r2 跑出后仅作 T1.5 verdict §3.4 + §4.4 建议落地确认（T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 PASS 一字不动，T1.5r2 不二次判定）
- **本棒不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 过渡声明 3 件** + **不动 L10 §0.5 过渡声明 2 件** + **不动 T1 §0.5 过渡声明 1 件** + **不动 T1.5 §0.5 过渡声明 1 件**（T1.5 构造失灵族补正定位过渡）

---

## §1 T1.5r2 · T1.5 扩样修订 N_min≥10 字面满足规化

### 1.1 修订缘由（K-N11-N1 字面 FAIL 根因消除）

- **T1.5 prereg `8898B964A9D9` §1.4 plan 字面**：5 教师 × 2 prompts × **2** re-asks = 20 calls/cell → 4 records/教师 → C(4,2) = **6 pairs/教师** < N_min=10 字面（沿 T1.5 prereg §1.4 + §1.8 TH-T1-1 = 10 对/教师探针放宽口径字面）
- **T1.5 prereg `8898B964A9D9` §1.8 N_min 字面**：TH-T1-1 = N_min = **10 对/教师**（沿 T1 `802DECE2286A` §1.4 + §1.8 字面沿用，T1.5 prereg §1.8 字面一字不动）
- **plan 字面 6 vs N_min 字面 10 = 结构性 gap**（plan 配对数 < N_min 字面门槛）—— T1.5 verdict `52C985429C91` §3.4 沿 T1.5 prereg §1.4 字面识别为「假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）」根因（**非命题层面被证伪**）
- **T1.5 verdict `52C985429C91` §3.4 拍板补正建议**：
  > 「**+60 calls 接力棒扩 N 至 N_min 满足**：5 教师 × 2 prompts × **3 re-asks**/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls（每 cell +10 calls，每教师 2 prompts × 1 额外 re-ask = +1 pair × 2 prompts × ... 实际上 5 × 2 × 1 = 10 calls/cell × 6 = 60 calls）；**checkpoint 续跑**（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）」
- **T1.5 verdict `52C985429C91` §4.4 拍板补正建议**：
  > 「**方案 A（推荐）**：补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）→ checkpoint 续跑（沿 L14 verdict §9.1 + T1 verdict §9.1 中断-恢复先例）；预计 +2 calls + 2.5s × 1 = < 5min wall time」
- **派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板**（2026-09-26 16:26）：
  > 「+60 calls 规化重跑（N_min≥10 字面满足）」
  > 拍板依据：
  > 1. **修订定位** = T1.5 prereg §1.4 计划（20 calls/cell → 6 pairs/教师）与 §1.8 N_min=10 字面的结构 gap 修复
  > 2. **扩样至 30 calls/cell**（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）
  > 3. **总增量 = 6 cells × +10 = +60 calls**（沿 verdict `52C985429C91` §3.4 建议字面）
  > 4. **kill-line 一字不动**（K-T1-S1/S3 + K-N11-3 + 0.85 沿字面）
  > 5. **2 calls 超时缺位顺带补跑**（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）计入 60 calls 预算
  > 6. **预算/节制** = qwen token-plan 5h 节制、串行 ≥2.5s、600s watchdog 拆批、中断-恢复同 agent 唤醒
  > 7. **产物链 `_v4_supp_t15r2_*` 系**（executor/result）；**verdict 留 verdict-keeper**
  > 8. **T1.5 原件 + T1.5 result + verdict 一字不动**

### 1.2 修订字面（30 calls/cell = 5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ N_min=10）

- **修订前（T1.5 prereg §1.4 字面）**：5 教师 × 2 prompts × **2** re-asks = 20 calls/cell → 4 records/教师 → C(4,2) = **6 pairs/教师** < N_min=10 字面
- **修订后（T1.5r2 §1.4 字面）**：5 教师 × 2 prompts × **3** re-asks = **30 calls/cell** → 5 records/教师 → 实际配对 = same-caption 池（2 captions × C(3,2) = 6 same-pool pairs/教师）+ cross-caption 池（2 × 3 × 3 = 18 cross-pool pairs/教师）= **24 same+cross pairs/教师**（实际字面）；**沿 T1.5 verdict `52C985429C91` §3.4 字面简化拍板 = 15 pairs/教师 ≥ N_min=10 字面满足**
- **修订字段**（**仅 1 字段修订**，其余沿用 T1.5 prereg 字面不动）：
  - **L2 维度**（沿 L2 verdict `E433A06E7BFB` §2 字面 + T1.5 prereg §1.4 字面）：
    - **修订**：5 教师 × 2 prompts × **2** re-asks = 20 calls/cell → **5 教师 × 2 prompts × 3 re-asks = 30 calls/cell**
    - prompt 子集沿 T1.5 prereg §1.4 字面 = seed=42 抽 2 caption (`L_biological_taxonomy`, `S5`)
    - temperature ∈ {0.0, 0.3, 0.5} 替换 qwen t=0.7 baseline（沿 T1.5 prereg §1.4 字面不动）
    - 端点 qwen3.7-max 单端点（**非 reasoning 模型**）（沿 T1.5 prereg §1.4 字面不动）
    - **max_tokens = 500**（沿 T1.5 prereg §1.4 C-T15-1 字面不动，**工具失灵族参数修正，非阈值调整**）
    - 主度量 = 教师 re-asked Jaccard 中位（沿 T1.5 prereg §1.4 字面不动）
  - **L14 维度**（沿 L14 verdict `764F24A21AC8` §2 字面 + T1.5 prereg §1.4 字面）：
    - **修订**：5 教师 × 2 prompts × **2** re-asks = 20 calls/cell → **5 教师 × 2 prompts × 3 re-asks = 30 calls/cell**
    - prompt 子集沿 T1.5 prereg §1.4 字面 = `L_geography_world` + `L_historical_causality`
    - **max_tokens = 500**（沿 T1.5 prereg §1.4 C-T15-1 字面不动）
    - temperature 替换 / 端点 / 主度量同上
    - L14 三方配对（re-asked + distill + independent）作为辅助度量（沿 T1.5 prereg §1.4 字面不动）
- **总增量**：
  - 6 cells × +10 calls/cell = **+60 calls**（沿 T1.5 verdict `52C985429C91` §3.4 字面 + 派工单 t15_ext 字面）
  - **6 cells × 30 calls/cell = 180 calls**（T1.5r2 总 calls 上限 = T1.5 prereg §1.6.3 360 calls 硬上限的 50%；实际跑 ≤ 180 calls 计入 5h Token Plan 配额节制）

### 1.3 修订矩阵（6 cells × 30 calls/cell）

| # | 维度（沿 L2 verdict / L14 verdict） | 温度 | 端点 | model_id | 代理 | calls 上限 / cell |
|---|---|---|---|---|---|---|
| 1 | L2 N-11 supp 教师 J 判定（沿 `E433A06E7BFB` §3.2 + §4.3） | 0.0 | qwen_plan: `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | `qwen3.7-max`（**非 reasoning**） | 否（qwen 直连无代理） | **30 calls**（5 教师 × 2 prompts × **3 re-asks**） |
| 2 | L2 N-11 supp 教师 J 判定 | 0.3 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | **30 calls** |
| 3 | L2 N-11 supp 教师 J 判定 | 0.5 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | **30 calls**（含 coze/S5/r0 1 补跑 call + 9 额外 re-asks 全员） |
| 4 | L14 N-11 full 三方配对（沿 `764F24A21AC8` §4 + §5 schema `v4_l14_n11full/2`） | 0.0 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | **30 calls**（含 GLM_1/L_geography_world/r1 1 补跑 call + 9 额外 re-asks 全员；re-asked trace 维度；distill + independent 沿 `21771E66AF67` + `5BA916D1DD24` 只读复用） |
| 5 | L14 N-11 full 三方配对 | 0.3 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | **30 calls** |
| 6 | L14 N-11 full 三方配对 | 0.5 | qwen_plan | `qwen3.7-max`（**非 reasoning**） | 否 | **30 calls** |

**矩阵 cell 总数 = 6 cells × 30 calls/cell = 180 calls（硬上限）**

**端点维度砍去**（沿 T1.5 prereg `8898B964A9D9` §1.2 字面不动）：T1 已探 mimo / teamo 两端点（沿 T1 verdict `F1B5E49F3058` §1.3 + §2.1-§2.3 字面，reasoning 模型 + max_tokens=100 致 K-T1-S2 端点维度 any_hit: false）；T1 verdict 已裁定 K-T1-S2（端点敏感性 flip 触发线）= any_hit: false（empty-empty 主导致整矩阵方向 J<0.85，非真判定一致）；T1.5r2 沿 T1.5 prereg + T1 verdict 结论引用 **不重测** K-T1-S2；T1.5r2 矩阵 = 单端点 qwen3.7-max（**非 reasoning**）+ max_tokens = 500 修正构造失灵族后温度维度探针（**0 触**）

**对照基准（不重跑）**（沿 T1.5 prereg §1.2 字面不动）：
- qwen token-plan 端点 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` model_id `qwen3.7-max` 既有数据（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）= **temperature = 0.7** = 对照基线**不重跑**；T1.5r2 探针仅在 qwen3.7-max（**非 reasoning**）+ max_tokens=500 修正构造失灵族后跑 temp ∈ {0.0, 0.3, 0.5}
- qwen 端点 t=0.7 baseline 既判（K-N11-3 真证伪：J 中位 0.36-0.39 < 0.85）作 6 cells 比照锚
- T1 verdict `F1B5E49F3058` §2.1-§2.2 K-T1-S1 + K-T1-S2 字面 any_hit: false 结论引用为 T1.5r2 历史比对锚
- T1.5 矩阵 120 calls 实测（6 cells × 20 calls + 2 失败原状）= T1.5r2 起始状态锚定（沿 T1.5 result `6B47D389B7AE` 字面不动 + T1.5 verdict `52C985429C91` §2 字面不动）

### 1.4 修订实验设计（仅 plan 字段修订，其余沿用 T1.5 prereg §1.4 字面）

- **素材**（沿 T1.5 prereg `8898B964A9D9` §1.4 字面不动）：
  - L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F`（L2 维度 + qwen t=0.7 baseline 对照锚）
  - L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`（L14 维度 + qwen t=0.7 baseline 对照锚）
  - T1 追加件 `802DECE2286A` + T1 verdict `F1B5E49F3058`（T1.5r2 字面源 + 补正对象 + K-T1-S1/S2/S3 字面源）
  - **T1.5 prereg `8898B964A9D9` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91`**（T1.5r2 字面源 3/4 + K-N11-N1_T1relax 根因消除字面源）
  - `0A9EE16267B5` §1 N-11 K-* 字面（沿用一字不动）
  - 22 caption `strip_captions_22.json` `6A2656878745`
  - 5 by_model（沿 TH-14：kimi / GLM_1 / GLM_2 / coze / minimax）
  - Track 2 multimodel probe `B65619A07B10`（ROUTE_TEMPLATES + tun + 串行 ≥2s，qwen 行 `use_proxy: False`）
  - Track 2 endpoints probe `C846F7FC79EE`（qwen_plan 探活锚，T1.5r2 单端点 = qwen_plan 行）
  - Track 2 multimodel verdict `_v4_track2_multimodel_verdict_2026_09_23.md`（qwen3.7-max 既有 baseline 数据，T1.5r2 对照锚）
  - `_v4_distill_min_measure.py` `21771E66AF67`（L14 维度 distill 提取函数，只读复用）
  - `_v4_proxy_student_generators.py` `5BA916D1DD24`（L14 维度 3 proxy 算子，只读复用）
- **构造**（**仅 plan 字面修订 1 字段：re-asks 2 → 3**）：
  - **L2 维度**（沿 L2 verdict `E433A06E7BFB` §2 字面 + T1.5 prereg `8898B964A9D9` §1.4 字面）：
    - **修订**：5 教师 × 2 prompts × **3 re-asks** = **30 calls / cell** × 3 temp × 1 端点 = **90 calls（L2 总）**
    - prompt 子集沿 L2 verdict `E433A06E7BFB` §2 = seed=42 抽 2 caption (`L_biological_taxonomy`, `S5`)
    - temperature ∈ {0.0, 0.3, 0.5} 替换 qwen t=0.7 baseline（沿 T1.5 prereg §1.4 字面不动）
    - 端点 qwen3.7-max 单端点（**非 reasoning 模型**），与 L2 verdict §2 同端点同模型（沿 T1.5 prereg §1.4 字面不动）
    - **max_tokens = 500**（沿 T1.5 prereg §1.4 C-T15-1 字面不动）
    - 主度量 = 教师 re-asked Jaccard 中位（同 L2 verdict §3.2 字面不动）
    - **沿 T1.5 verdict `52C985429C91` §3.4 字面简化 = 15 pairs/教师 ≥ N_min=10 字面满足**（实际配对数 = 24 same+cross pairs/教师 > N_min=10）
  - **L14 维度**（沿 L14 verdict `764F24A21AC8` §2 字面 + T1.5 prereg `8898B964A9D9` §1.4 字面）：
    - **修订**：5 教师 × 2 prompts × **3 re-asks** = **30 calls / cell** × 3 temp × 1 端点 = **90 calls（L14 总）**
    - prompt 子集沿 L14 verdict `764F24A21AC8` §2 = `L_geography_world` + `L_historical_causality`
    - **max_tokens = 500**（沿 T1.5 prereg §1.4 C-T15-1 字面不动）
    - temperature 替换同上 / 端点同上 / 主度量同上
    - L14 三方配对（re-asked + distill + independent）作为辅助度量（沿 T1.5 prereg §1.4 字面不动）
    - **沿 T1.5 verdict `52C985429C91` §3.4 字面简化 = 15 pairs/教师 ≥ N_min=10 字面满足**
  - **2 calls 缺位补跑计入 +60 calls 预算内**（沿 T1.5 verdict `52C985429C91` §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板）：
    - **cell 2（L2/temp=0.5）coze/S5/r0 缺位补跑** = 1 call（coze r0 重跑） + 9 额外 re-asks 全员（5 教师 × 2 prompts × 1 re-ask = 10 - coze r0 已含 = 9 净增） = **cell 2 = 10 calls**（与 T1.5 prereg §1.6.3 字面每 cell +10 calls 一致）
    - **cell 3（L14/temp=0.0）GLM_1/L_geography_world/r1 缺位补跑** = 1 call（GLM_1 r1 重跑） + 9 额外 re-asks 全员 = **cell 3 = 10 calls**
    - **cell 0/1/4/5 纯新跑** = 5 教师 × 2 prompts × 1 re-ask = **10 calls/cell**
    - **总增量 = 6 cells × 10 calls/cell = +60 calls**（与 T1.5 verdict `52C985429C91` §3.4 字面 + 派工单 t15_ext 字面拍板一致）
- **度量**（沿 T1.5 prereg `8898B964A9D9` §1.4 字面不动）：
  - **主度量** = Jaccard 中位数（per teacher, per cell）—— 沿 L2/L14 verdict §3.2 字面不动
  - **辅助度量**（L14 维度）：三方 max-min diff + distill J - teacher J delta（沿 L14 verdict §4.1/§4.2 字面不动）+ independent J（沿 L14 verdict §4.3 字面不动）
  - **稳健性度量** = bootstrap CI 95%（沿 K-N11-N2 双读法）+ per 教师 N 评估 + 跨温度 J 中位标准差
  - **audit-only metadata 字段**（沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板）：T1.5r2 result json metadata = `audit-only`，不参与 kill-line / Jaccard / 统计推断；字段集 = `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint`（T1.5r2 沿用同字段集，端点恒为 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max`）
  - **same-caption / cross-caption 拆解**（沿 T1.5 verdict `52C985429C91` §1.2 + §6 同 caption J 拆解字面 + §6.3 保守口径）：T1.5r2 worker 沿用 T1.5 worker 自加 same_caption_breakdown 字段（**沿用字面**），仅作 informational 注记；**不外推**为 L2/L14 既判反证 / K-N11-N2 字面修订主依据 / T1 verdict 信息量边界声明补充；**待 PI 复核拍板**
- **拍板出处**：PI 2026-09-26 16:26 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板「+60 calls 规化重跑（N_min≥10 字面满足）」+ T1.5 verdict `52C985429C91` §3.4「+60 calls 接力棒扩 N」字面 + §4.4「补跑 2 calls（方案 A）」字面 + T1 verdict `F1B5E49F3058` §4.1【最高优先】建议字面 + §7 总判定构造失灵族假象裁定
- **真审条件**（沿 T1.5 prereg §1.4 + T1 verdict §1.6.4 + L14 verdict §9.1 字面不动）：worker 接力棒分批跑；单批 ≤ 600s 看门狗；撞 5h 配额中断-恢复（沿 L14 verdict §9.1 + T1 verdict §9.1 中断恢复先例）；T1.5r2 executor = 新件 `_v4_supp_t15r2_executor.py`，沿 T1.5 executor `558E635F9BA6` § checkpoint 模式续跑（**T1.5 executor 一字不动**）
- **非退化自证**（沿 T1.5 prereg §1.4 字面不动）：每 cell 5 教师 N_min = 10 对/教师（沿 T1 §1.4 探针放宽口径 TH-T1-1 = 10 对/教师 = 字面满足条件）；T1.5r2 plan 字面 = 5 教师 × 2 prompts × 3 re-asks = **15 pairs/教师 ≥ N_min=10 字面满足**（沿 T1.5 verdict `52C985429C91` §3.4 字面简化 + 实际配对数 = 24 same+cross pairs/教师）；T1.5 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）= **T1.5r2 plan 字面扩样后根因消除**（plan 字面 6 → 15 pairs/教师 ≥ N_min=10 字面满足）
- **双读法并记**（沿 T1.5 prereg §1.4 + K-N11-N2 字面不动）：
  - 构造面（单 cell N=10/15）= T1.5r2 探针单 cell 内 J 中位
  - 真实面（跨 cell 累加 N≥45）= 跨同温度 cell 累加 J 中位
  - 任一面 PASS ≠ T1.5r2 探针成立（必须双向一致）

### 1.5 修订 kill-line（**一字不动**）

> **字面不动声明（修订件硬约束）**：既有 K-N11-1/2/3/N1/N2 字面（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1）**一字不动**；既有 K-T1-S1/S2/S3 字面（沿 T1 追加件 `802DECE2286A` §1.5 + T1 verdict `F1B5E49F3058` §2）**一字不动**；T1.5r2 = 沿 T1.5 prereg `8898B964A9D9` §1.5 字面一字不动（**0 新设 kill-line 条款 + 0 新设数值阈值**）；**K_N11_3_THRESHOLD = 0.85 沿 L2/L14 verdict + `0A9EE16267B5` §1 + T1 `802DECE2286A` §1.5 字面一字不动**；T1.5r2 修订仅扩 plan 字面（20 → 30 calls/cell）= K-N11-N1_T1relax 字面 FAIL 根因消除 = 假证伪族根因消除，**0 触 K-* 字面**

#### 1.5.1 既有 K-N11 字面（沿 L2/L14 verdict 一字不动，锁前痕迹保留）

- **K-N11-1**：三方 Jaccard 中位数差异 < K_N11_1_DIFF = 0.05 即 `hit=True` → FAIL（三方不可分离）—— **沿 `0A9EE16267B5` §1 K-N11-1 字面**
- **K-N11-2**：distill J > teacher J + K_N11_2_DELTA = 0.05 不成立即 `hit=True` → FAIL（与原假设反向）—— **沿 `0A9EE16267B5` §1 K-N11-2 字面**
- **K-N11-3**：教师两次 J 中位数 < K_N11_3_THRESHOLD = 0.85 即 `hit=True` → FAIL（教师自身不稳定，主度量失效）—— **沿 `0A9EE16267B5` §1 K-N11-3 字面**（**T1.5r2 探针核心沿此字面**）
- **K-N11-N1**：N < TH17_N_TARGET = 20 / 教师 即 `pass=False` → FAIL（构造退化致命题不明）—— **沿 v0.2 §2 L2 K-N11-N1 字面**（**T1.5r2 探针放宽至 N_min=10** 不动此字面，T1.5r2 N_min=10 为探针放宽口径与 K-N11-N1 字面 N=20 是两层并存）
- **K-N11-N1_T1relax（探针放宽 N_min = 10/教师）**：N < TH-T1-1 = 10 对/教师 即 `pass=False` → FAIL（沿 T1.5 prereg §1.8 字面不动 + T1 verdict `F1B5E49F3058` §2 字面 + T1.5 verdict `52C985429C91` §3.4 拍板「plan 字面扩样至 15 pairs/教师 ≥ N_min=10 字面满足 → 字面 PASS」）—— **T1.5r2 plan 字面扩样后根因消除**（沿 T1.5 verdict `52C985429C91` §3.4 字面拍板 + 派工单 t15_ext 字面拍板）
- **K-N11-N2**：构造面 K-N11-1/2/3 + 真实面 K-N11-1/2/3 **并记**；任一面 PASS ≠ 命题成立（必须双面都过）—— **沿 v0.2 §2 L2 K-N11-N2 字面**

#### 1.5.2 T1.5r2 复用 K-T1-* 字面（沿 T1 追加件 + T1 verdict 一字不动，0 新设阈值）

- **K-T1-S1（温度敏感性 flip 触发线 · 主判定）**：
  - **字面**：在任一固定端点（qwen_plan）下，沿 L2 维度或 L14 维度，教师 J 中位数跨温度 {0.0, 0.3, 0.5} 中**任一温度点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**（显式布尔，避免裸 bool 歧义）：
    - 既定方向 = qwen t=0.7 baseline 教师 J 中位 < 0.85（沿 L2 verdict `E433A06E7BFB` §3.2 + L14 verdict `764F24A21AC8` §3.2 实测）
    - 翻转条件 = 新 (端点=qwen_plan, 维度=L2|L14, 温度 ∈ {0.0, 0.3, 0.5}) cell 教师 J 中位 ≥ 0.85（**T1.5r2 = qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后 + plan 字面扩样至 30 calls/cell**）
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（沿 L2/L14 verdict + `0A9EE16267B5` §1 + T1 `802DECE2286A` §1.5 字面，**0 新设**）
  - **不翻 L2/L14 正式判定**（沿定位声明）：K-T1-S1 hit=True 仅入稳健性注记，**不据此改判** L2 verdict `E433A06E7BFB` §11「FAIL 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪」既定结论一字不动
  - **不二次判定 T1 verdict §7 自身**（沿「不动既有件字面」+「T1 verdict 已裁构造失灵族假象」+「T1.5r2 仅作扩样修订探针」三重约束）：T1 verdict `F1B5E49F3058` §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动；T1.5r2 K-T1-S1 命中/不命中独立判定，T1.5r2 不就 T1 verdict 自身作二次裁定
  - **不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面**（沿 T1.5 verdict `52C985429C91` §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS 一字不动声明）：T1.5 verdict §1 主读法「K-T1-S3 字面命中（PASS）= 真稳健入勘误链 + 构造失灵族修正后真维持方向一致 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」一字不动；T1.5r2 K-T1-S1 命中/不命中独立判定，T1.5r2 不就 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面作二次裁定

- **K-T1-S2（端点敏感性 flip 触发线 · 主判定）—— T1.5r2 沿 T1 verdict 结论引用不重测**：
  - **T1.5r2 字面**：T1 verdict `F1B5E49F3058` §2.2 K-T1-S2 已裁 `any_hit: false`（端点维度 any_hit: false，mimo/teamo × {0.0, 0.3, 0.5} × {L2/L14} 整矩阵方向 J<0.85，empty-empty 主导非真判定一致）；T1.5r2 端点维度砍去（qwen_plan 单端点），**沿 T1 verdict §2.2 any_hit: false 结论引用**，**T1.5r2 不重测 K-T1-S2**
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（一字不动）
  - **不翻 L2/L14 正式判定**：同 K-T1-S1

- **K-T1-S3（稳健性确认线 · 副判定）**：
  - **字面**：6 cells 全 J 中位 < 0.85 = 「**判定稳健**」= T1.5r2 探针不命中 K-T1-S1 / K-T1-S2 → 入稳健性确认注记 + **T1 verdict 构造失灵族假象裁定获补正**（qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正构造失灵族后真维持方向一致 = T1 字面 PASS 不再是假象 → 真稳健入勘误链作 L2/L14 既判稳健性确认）
  - **判定方式**：任一 cell 触发 K-T1-S1 或 K-T1-S2（K-T1-S2 沿 T1 verdict 结论引用）= 探针命中；全 6 cells 不触发 = 探针不命中 + T1 verdict 补正完成
  - **T1.5r2 探针与 T1 verdict / T1.5 verdict 关系**：
    - T1 verdict §7 总判定「K-T1-S3 字面命中（PASS）= 构造失灵族假象」一字不动（T1 verdict 自身不可二次判定）
    - T1.5 verdict §1 主读法「判定稳健确认 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」一字不动（T1.5 verdict §1 主读法自身不可二次判定）
    - T1.5r2 K-T1-S3 命中（探针不命中 K-T1-S1/S2）= 仅作 T1.5 verdict §3.4 + §4.4 建议落地确认注记 + K-N11-N1_T1relax 字面 PASS 注记（**T1.5 verdict §1 主读法「判定稳健」既判方向同向确认 + K-N11-N1 字面 FAIL 根因消除确认**）
    - T1.5r2 K-T1-S1 命中 = 仅入稳健性存疑注记，**不翻 T1 verdict §7 自身 + 不翻 T1.5 verdict §1 主读法**

#### 1.5.3 T1.5r2 kill-line 字面总览（沿 T1 + L2/L14 verdict + `0A9EE16267B5` 字面 + T1.5 verdict §3.4 字面）

| K-* | 字面 | hit 触发条件 | hit=True 后果 | 字面源 |
|---|---|---|---|---|
| K-N11-1 | 三方 Jaccard 中位数差异 < 0.05 → FAIL | 三方 max-min diff < 0.05 | L2/L14 cell 内部 FAIL | `0A9EE16267B5` §1 |
| K-N11-2 | distill J > teacher J + 0.05 不成立 → FAIL | delta = distill J - teacher J ≤ 0.05 | L2/L14 cell 内部 FAIL | `0A9EE16267B5` §1 |
| K-N11-3 | 教师两次 J 中位数 < 0.85 → FAIL | per teacher J median < 0.85 | L2/L14 cell 内部 FAIL（T1.5r2 探针主度量） | `0A9EE16267B5` §1 |
| K-N11-N1 | N < 20 / 教师 → pass=False → FAIL | per teacher N < 20 | L2/L14 cell 内部 FAIL | v0.2 §2 L2 |
| K-N11-N1_T1relax | N < 10 / 教师 → pass=False → FAIL（探针放宽口径） | per teacher N < 10 | T1.5 探针内部 FAIL（沿 T1 §1.8 字面）；**T1.5r2 plan 字面扩样至 15 pairs/教师 ≥ N_min=10 → 字面 PASS**（沿 T1.5 verdict `52C985429C91` §3.4 字面 + 派工单 t15_ext 字面拍板） | T1 `802DECE2286A` §1.8 + T1.5 prereg `8898B964A9D9` §1.8 + T1.5 verdict `52C985429C91` §3.4 |
| K-N11-N2 | 构造面 + 真实面双读法并记 | 任一面 PASS ≠ 命题成立 | L2/L14 cell 内部 FAIL | v0.2 §2 L2 |
| **K-T1-S1（沿 T1 一字不动，T1.5r2 主判定）** | 任一温度点 J 中位 ≥ 0.85 → hit=True → 稳健性存疑注记 | 跨温度 {0.0, 0.3, 0.5} 任一 ≥ 0.85 | T1.5r2 探针命中（**不翻 L2/L14 既判 + 不翻 T1 verdict 自身 + 不翻 T1.5 verdict §1 主读法**） | 沿 T1 `802DECE2286A` §1.5.2 字面（T1.5r2 复用，0 新设数值） |
| **K-T1-S2（沿 T1 verdict 结论引用不重测）** | T1 verdict §2.2 已裁 any_hit: false；T1.5r2 沿结论引用 | T1 verdict §2.2 字面（mimo/teamo 端点维度 empty-empty 主导） | T1 verdict 结论 = any_hit: false；T1.5r2 不重测 | 沿 T1 verdict `F1B5E49F3058` §2.2 字面（沿结论引用，0 新设数值） |
| **K-T1-S3（沿 T1 一字不动，T1.5r2 副判定 + T1 verdict 补正线）** | 全 6 cells J 中位 < 0.85 = 判定稳健 + T1 verdict 补正完成 | 6 cells 全 < 0.85 | T1.5r2 探针不命中（确认注记）+ T1 verdict 信息量补正（构造失灵族修正后真稳健入勘误链） | 沿 T1 `802DECE2286A` §1.5.2 字面（T1.5r2 复用，0 新设数值） |

> **0 新设阈值声明（修订件硬约束）**：K-T1-S1/S2/S3 三条**0 新设数值阈值**（沿 T1 `802DECE2286A` §1.5.2 字面沿用）；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict `E433A06E7BFB` §2 + L14 verdict `764F24A21AC8` §2 + `0A9EE16267B5` §1 字面一字不动；T1.5r2 探针字面「方向翻转 = hit=True」是布尔条件显式化（沿 S-40 教训「判定布尔显式方向」），**不构成阈值私设**；T1.5r2 plan 字面修订（20 → 30 calls/cell）系**构造失灵族参数扩展**（沿 T1.5 verdict `52C985429C91` §3.4 补正建议字面「构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致」+ T1 verdict `F1B5E49F3058` §4.1【最高优先】建议 + §5.1 工具失灵族假象裁定），**非阈值调整**——沿派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板明示「判定阈值一字不动；扩样 = plan 字面修订」

### 1.6 修订调用预算与节制（Token Plan 5h 限额硬约束，**沿 T1.5 prereg §1.6 字面 + 派工单 t15_ext 字面**）

> **硬约束声明**：T1.5r2 探针**0 触 L2/L14 verdict 既定 5h 配额节制原则**（沿 L14 verdict §9.1 + T1 verdict §9.1 + T1.5 prereg §1.6.1 中断恢复先例）；本棒新立 T1.5r2 独立配额，与 T1.5 既定 5h 配额**物理隔离**（端点同 = qwen_plan 但构造扩展 + plan 扩样；worker 接力棒按修订构造分批）

#### 1.6.1 单批 calls 上限（看门狗约束）

- **单批 ≤ 30 calls**（沿 L2 verdict §2「600s 看门狗」+ L14 verdict §9.1「280s hard limit + sub-batch strategy」+ T1 `802DECE2286A` §1.6.1 + T1.5 prereg `8898B964A9D9` §1.6.1 双向沿用，每 30 calls 预估 600-700s wall time 含 2.5s 串行间隔）
- **每 cell 拆批**：每 cell ≤ 30 calls / 拆 1 批 × 30 calls / 批（沿 T1.5 prereg §1.6.1 字面 + T1.5r2 plan 字面修订：cell 上限 = 30 calls）
- **6 cells × 1 批 / cell = 6 批**（理论上限；实际跑按需调整）

#### 1.6.2 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 L2 verdict `E433A06E7BFB` §2 INTER_CALL_SLEEP_S + L14 verdict `764F24A21AC8` §2 INTER_CALL_SLEEP_S + Track 2 runner `INTER_CALL_SLEEP_S` + T1 §1.6.2 + T1.5 prereg `8898B964A9D9` §1.6.2 沿用 + 派工单 t15_ext 字面拍板）
- **qwen token-plan 端点**（`token-plan.maas.qianwenaiapi.com/compatible-mode/v1`）：**无代理**（沿 `_v4_v5_multimodel_probe.py` `B65619A07B10` L35 `use_proxy: False` + T1 `802DECE2286A` §1.6.2 + T1.5 prereg `8898B964A9D9` §1.6.2 沿用）
- **teamorouter / mimo / openrouter 端点**：T1.5r2 单端点 = qwen_plan，**不触发** teamo 必走 tun 硬纪律（沿 PI 2026-09-23「teamorouter 必走 tun 防封号」+ user memory 2026-09-23）

#### 1.6.3 总预算上限（**修订**）

- **总 calls 上限 ≤ 180 calls**（6 cells × **30 calls/cell** 硬上限；T1.5 prereg §1.6.3「360 calls 硬上限」**0 触**——本棒独立修订预算；T1.5 120 calls 实测 + T1.5r2 +60 calls 增量 = 180 calls 总预算）
- **总 wall time 上限 ≤ 5h**（Token Plan 5h 配额硬约束；沿 L14 verdict §9.1 + T1 §1.6.3 + T1.5 prereg `8898B964A9D9` §1.6.3「5h 配额撞限」先例 + 派工单 t15_ext 字面拍板）
- **每 cell 实际 calls 预算**（**修订**）：
  - L2 维度：5 教师 × 2 prompts × **3 re-asks** = **30 calls / cell**（含 cell 2 coze/S5/r0 1 补跑 call）
  - L14 维度：5 教师 × 2 prompts × **3 re-asks** = **30 calls / cell**（含 cell 3 GLM_1/L_geography_world/r1 1 补跑 call）
  - **每 cell 实跑上限 ≤ 30 calls**（T1.5 prereg §1.6.3「≤ 26 calls/cell」**0 触**——本棒独立修订；T1.5r2 = 30 calls/cell 字面满足）
- **6 cells × 30 calls/cell = 180 calls 实际预计**（远低于 T1.5 prereg §1.6.3「360 calls 硬上限」）

#### 1.6.4 中断-恢复与分批拆跑方案（沿 T1.5 prereg §1.6.4 字面 + 派工单 t15_ext 字面）

- **中断-恢复语义**（沿 L14 verdict §9.1 + T1 §1.6.4 + T1.5 prereg §1.6.4 先例 + 派工单 t15_ext 字面「中断-恢复同 agent 唤醒」）：
  - 同 worker 接力棒：v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2（沿 L14 verdict §9.1 + T1 §1.6.4 + T1.5 prereg §1.6.4）
  - checkpoint 文件：`.tmp/_t15r2_records.json`（沿 L14 runner `.tmp/_l14_records.json` + T1 runner `.tmp/_t1_records.json` + T1.5 runner `.tmp/_t15_records.json` 惯例；**T1.5 runner checkpoint 文件不动**）
  - 每 call 后 checkpoint 累积（沿 L14 runner L151-156 惯例）
  - 已跑 (teacher, caption_id, reask_idx, temp, endpoint) 元组 skip（沿 L14 runner L107-110 + T1 §1.6.4 + T1.5 prereg §1.6.4 惯例；T1.5r2 端点恒 = qwen_plan，元组 = (teacher, caption_id, reask_idx, temp)；**T1.5 120 calls 已跑 (teacher, caption_id, reask_idx 0/1, temp) 元组全部 skip = 续跑起点 = reask_idx = 2 起**）
- **分批拆跑**（沿 T1.5 prereg §1.6.4 字面 + 派工单 t15_ext 字面「600s watchdog 拆批」）：
  - 撞 5h 配额自动恢复（worker 接力棒续跑）
  - 单批撞 600s 看门狗自动停（沿 L14 verdict §9.1 看门狗 280s 上调至 600s 沿 L2 verdict）
  - 中断-恢复同 agent 唤醒语义（worker session 不重启，沿 L14 + T1 §9.1 + T1.5 prereg §1.6.4 同棒续跑）
- **额度撞限应急**（如 6 cells 未跑完撞 5h 配额）：
  - 仅跑已启动 cells，不补未启动 cells
  - 已启动 cells 部分完成记「T1.5r2 部分完成」注记
  - 未启动 cells 留待 worker 下一棒接力
- **2 calls 缺位补跑语义**（沿 T1.5 verdict `52C985429C91` §4.4 方案 A 字面 + 派工单 t15_ext 字面）：
  - **cell 2（L2/temp=0.5）coze/S5/r0** = 缺位补跑 call（沿 T1.5 verdict §4.1 时段定位字面「90s 超时单点；同 cell 其他 19/20 calls 正常完成」）
  - **cell 3（L14/temp=0.0）GLM_1/L_geography_world/r1** = 缺位补跑 call（沿 T1.5 verdict §4.1 时段定位字面「90s 超时单点；同 cell 其他 19/20 calls 正常完成」）
  - 2 补跑 calls 计入 +60 calls 预算内（cell 2 +10 calls + cell 3 +10 calls = +20 calls 含 2 补跑 + 18 额外 re-asks 全员；cell 0/1/4/5 各 +10 calls 纯新跑 = +40 calls；总增量 = +20 + +40 = +60 calls 字面满足）
  - 2 补跑 calls 沿 T1.5 executor `558E635F9BA6` §checkpoint 模式续跑（**T1.5 executor 一字不动**）

#### 1.6.5 calls 预算写死公式（沿 T1.5 prereg §1.6.5 字面 + T1.5r2 修订）

```
总 calls 上限 = cells × calls_per_cell = 6 × 30 = 180（T1.5 prereg §1.6.3「360」0 触；T1.5r2 修订为 180）
总 calls 实际预计 = cells × actual_calls_per_cell = 6 × 30 = 180（含 2 补跑 calls）
单批 calls 上限 = min(30, calls_per_cell) = 30（calls_per_cell = 30 字面满足）
单批 wall time 上限 ≤ 600s（含 2.5s × 30 串行间隔 + 单 call 推理时间）
总 wall time 上限 = cells × (calls_per_cell / 30) × 600s / 3600 ≤ 5h（沿 Token Plan 5h 配额硬约束）
T1.5r2 增量 = 180 - 120（T1.5 实测）= +60 calls（沿 T1.5 verdict §3.4 字面 + 派工单 t15_ext 字面拍板）
```

### 1.7 修订产物链（`_v4_supp_t15r2_*`，诞生即 SHA-12，派生 JSON 不合并）

> **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律 + 派工单 t15_ext 字面拍板）；本棒产物用 `_v4_supp_t15r2_*` prefix 分列，与现有 `_v4_supp_t15_*` + `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立

- `_v4_supp_t15r2_executor.py`（T1.5r2 矩阵 runner + checkpoint 模式 + qwen3.7-max 非 reasoning 模型 + max_tokens=500 + 温度切换 + plan 字面扩样至 30 calls/cell；**沿 T1.5 executor `558E635F9BA6` checkpoint 模式续跑**，T1.5 executor 一字不动）
- `_v4_supp_t15r2_result.json`（6 cells 矩阵结果聚合：每 cell per teacher J 中位 + qwen3.7-max + 温度 + audit-only metadata 字段 + schema `v4_t15r2_sensitivity_fix_n10/1`（**沿 T1.5 schema `v4_t15_sensitivity_fix/1` 扩样版本**；仅 schema 版本号扩样字段 = /1 → /n10/1 字面，0 触 T1.5 原 schema 数值字面）+ 跨温度 J 中位标准差 + K-N11-N1_T1relax 字面 PASS 标注（N=15 ≥ N_min=10）+ 2 calls 缺位补跑标注）
- `_v4_supp_t15r2_verdict.md`（T1.5r2 探针判定：6 cells 字面 K-N11-3 实测 + K-T1-S1/S3 触发判定 + K-T1-S2 沿 T1 verdict 结论引用 + K-N11-N1_T1relax 字面 PASS 根因消除标注 + 根因三分类每行附 + T1.5 verdict §3.4 + §4.4 建议落地确认 + 不翻 L2/L14 既判声明 + 不翻 T1 verdict §7 自身声明 + **不翻 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS 自身声明**——**T1.5r2 verdict 留 verdict-keeper 起草**，本 prereg 件 0 起草 verdict；沿 8 agent 团队分工）
- 与现有 `_v4_supp_t15_*`（T1.5 executor + result + verdict）+ `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律 + 派工单 t15_ext 字面拍板）
- **schema 兼容**：L14 维度 cell schema 沿 `v4_l14_n11full/2`（沿 L14 verdict `764F24A21AC8` §2 字面不动）；L2 维度 cell schema 沿 L2 verdict `E433A06E7BFB` §2 字面不动；T1.5r2 result JSON 中 `schema` 字段 = `"v4_t15r2_sensitivity_fix_n10/1"`（T1.5r2 探针专属 schema；沿 T1.5 schema `v4_t15_sensitivity_fix/1` 扩样版本仅 schema 版本号 = /1 → /n10/1 字面修订，0 触 T1.5 原 schema 数值字面）
- **audit-only metadata 字段口径**（沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板）：T1.5r2 result json metadata = `audit-only`（不参与 kill-line / Jaccard / 统计推断；仅作审计追溯，不入判定字面源）；字段集沿 L14V3 映射件 §1.2 = `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint`（T1.5r2 沿用同字段集，端点恒为 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max`）

### 1.8 复用资产（0 触动既有字面）

- T1 追加件 `802DECE2286A` + T1 activation `79936B630015` + T1 verdict `F1B5E49F3058`（T1.5r2 字面源 + 补正对象，只读复用）
- L14V3 追加件 + L14V3 activation + L14V3 映射件（audit-only metadata 字段口径锚，只读复用）
- L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F`（L2 维度字面源 + qwen t=0.7 baseline 对照锚，只读复用）
- L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`（L14 维度字面源 + qwen t=0.7 baseline 对照锚，只读复用；L14 verdict 自报 vs 盘 SHA 漂移沿 T1 §9.1 披露）
- **T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` + T1.5 executor `558E635F9BA6`**（T1.5r2 字面源 3/4 + 起始状态锚定 + checkpoint 模式锚定，只读复用 + **0 触**）
- `0A9EE16267B5` §1 K-N11-1/2/3 字面（沿用一字不动）
- `D85488A64D89` §2 L2 K-N11-N1/N2 字面（沿用一字不动）
- `21771E66AF67` `_v4_distill_min_measure.py`（L14 维度 distill 提取函数，只读复用）
- `5BA916D1DD24` `_v4_proxy_student_generators.py`（L14 维度 3 proxy 算子，只读复用）
- `B656A07B10` `_v4_v5_multimodel_probe.py`（端点 + tun + 串行 ≥2s，qwen 行 `use_proxy: False`，只读复用）
- `C846F7FC79EE` `_track2_endpoints_probe_2026_09_23.json`（qwen_plan 探活锚，只读复用）
- `6A2656878745` `strip_captions_22.json`（22 caption，只读复用）
- `_v4_track2_multimodel_verdict_2026_09_23.md`（qwen3.7-max 既有 baseline 数据，T1.5r2 对照锚，只读复用）

**复用条款**（沿 T1 + L14V3 字面）：
- **K-T1-S1**（温度敏感性 flip 触发线）—— 沿 T1 `802DECE2286A` §1.5.2 字面，T1.5r2 复用一字不动
- **K-T1-S2**（端点敏感性 flip 触发线）—— 沿 T1 verdict `F1B5E49F3058` §2.2 any_hit: false 结论引用，T1.5r2 不重测
- **K-T1-S3**（稳健性确认线 + T1 verdict 补正线）—— 沿 T1 `802DECE2286A` §1.5.2 字面 + T1 verdict §7 字面（T1.5r2 K-T1-S3 命中 = 真维持方向一致 = T1 verdict 信息量补正 + T1.5 verdict §3.4 + §4.4 建议落地确认），T1.5r2 复用一字不动
- **TH-T1-1** = N_min per cell = 10 对/教师（沿 T1 `802DECE2286A` §1.8 新增条款，T1.5r2 沿用；TH-17 N=20 仍为 L2/L14 既判门槛，两层并存；**T1.5r2 plan 字面扩样至 15 pairs/教师 ≥ TH-T1-1 = N_min=10 字面满足**）
- **audit-only metadata 字段口径**（沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板）—— T1.5r2 沿用同字段集，端点恒为 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max`

**修正条款**（沿 T1.5 verdict `52C985429C91` §3.4 + §4.4 补正建议字面 + 派工单 t15_ext 字面拍板）：
- **C-T15r2-1（plan 字面扩样修订）** = 5 教师 × 2 prompts × **3 re-asks**/cell × 6 cells = **180 calls**（沿 T1.5 prereg `8898B964A9D9` §1.4 字面 5 教师 × 2 prompts × 2 re-asks = 20 calls/cell → 修订为 30 calls/cell；总增量 = +60 calls；2 calls 缺位补跑计入预算）—— C-T15r2-1 = **构造失灵族参数扩展**（沿 T1.5 verdict §3.4 补正建议字面「构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致」），**非阈值调整**——沿派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板明示「判定阈值一字不动；扩样 = plan 字面修订」
- **C-T15-1（端点 + 模型替换 + max_tokens=500，沿 T1.5 prereg §1.4 字面不动）** = qwen token-plan `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model_id `qwen3.7-max`（**非 reasoning 模型**）+ **max_tokens = 500**（≥500 拍板字面；T1 L14 维度 max_tokens=100 沿 L14 verdict §2 字面致 49.3% 空响应，T1.5 + T1.5r2 max_tokens=500 修正构造失灵族 #2，L2 维度同步 max_tokens=500 以保持 L2/L14 构造一致性）—— C-T15-1 = **工具失灵族参数修正**，**非阈值调整**（沿派工单 t15 + T1 verdict `F1B5E49F3058` §4.1【最高优先】建议字面沿用）

### 1.9 规模档（修订）

- **M** ≤ 2-3 天 worker 接力棒（6 cells × **30 calls/cell** × 2.5s 间隔 + 600s 看门狗 × 6 批 = 理论 ≤ 1.5h 跑完；实际预留 5h 配额撞限风险 + 中断-恢复时间 ≤ 3h wall time；**沿 T1.5 prereg `8898B964A9D9` §1.9 字面「≤ 2-3 天」不动**）
- 单 worker 接力棒即可完成；分批拆跑 ≤ 6 批（**沿 T1.5 prereg §1.9 字面「12 批」修订为 6 批**——T1.5r2 每 cell ≤ 30 calls = 1 批/cell = 6 cells × 1 批 = 6 批）；总 calls 实跑 = **180 calls**（沿 T1.5 prereg §1.9 字面「156 calls」**修订为 180 calls**）

### 1.10 判定

- **productive**（沿 L9 `23879B6CD1CC` §1 productive 判例 + L10 `F6FE005EE3C7` §1 productive 判例 + T1 `802DECE2286A` §1.10 productive 判例 + T1.5 prereg `8898B964A9D9` §1.10 productive 判例 + L14V3 L14V3_* §1 productive 判例）

### 1.11 构造面 vs 真实面外推边界（沿 T1.5 prereg §1.11 字面不动）

- **构造面判定**（T1.5r2 探针构造面）：6 cells 中任一 cell 触发 K-T1-S1 = 探针命中（**仅注记，不翻 L2/L14 既判 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面**）；K-T1-S2 沿 T1 verdict §2.2 any_hit: false 结论引用不重测；全 6 cells 不触发 = 探针不命中（确认稳健性）+ T1 verdict 信息量补正（构造失灵族修正后真稳健入勘误链作 L2/L14 既判稳健性确认）+ T1.5 verdict §3.4 + §4.4 建议落地确认 + K-N11-N1_T1relax 字面 PASS 根因消除注记
- **真实面判定**（T1.5r2 探针真实面）：实际 qwen3.7-max 非 reasoning 模型 + max_tokens=500 + plan 字面扩样至 30 calls/cell + temp 维度下 5 教师 J 中位实测（N=15/教师 ≥ N_min=10 字面满足）
- **外推边界 = 端点 / 模型类别 / 构造修正维度边界**（qwen t=0.7 是既定条件，方向翻转只质疑 qwen 端点的代表性而非整体判死）+ **数据规模边界**（T1.5r2 N_min=10/教师探针放宽 + plan 字面扩样至 15 pairs/教师 字面满足，与 L2/L14 既定 N=20/教师 两层并存）
- **不留假 pass**：T1.5r2 探针不命中 ≠ L2/L14 既判 PASS（K-N11-3 真证伪既判不动）；T1.5r2 探针不命中 = 真稳健入勘误链作 L2/L14 既判稳健性确认注记（**不是改判**，仅是既判方向的稳健性确认）
- **不留假证伪**：T1.5r2 探针命中 ≠ L2/L14 既判 FAIL（仅入稳健性存疑注记，不翻既判）
- **不留二次判定**：T1.5r2 探针命中/不命中 ≠ T1 verdict §7 自身判定 + ≠ T1.5 verdict §1 主读法自身判定（T1 verdict + T1.5 verdict 一字不动，T1.5r2 仅作扩样修订探针 + T1.5 verdict §3.4 + §4.4 建议落地确认 + K-N11-N1_T1relax 字面 PASS 根因消除注记）

---

## §2 T1.5r2 矩阵汇总统计表（修订）

| # | 维度 | 温度 | 端点 | model_id | calls 上限 / cell | 主 kill-line | 字面源 | 阈值 |
|---|---|---|---|---|---|---|---|---|
| 1 | L2 N-11 supp 教师 J | 0.0 | qwen_plan | qwen3.7-max（**非 reasoning**） | **30 calls**（5 教师 × 2 prompts × **3 re-asks**） | K-N11-3 → K-T1-S1 字面 + K-N11-N1_T1relax 字面（plan 字面扩样至 15 pairs/教师 ≥ N_min=10 → PASS） | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 2 | L2 N-11 supp 教师 J | 0.3 | qwen_plan | qwen3.7-max（**非 reasoning**） | **30 calls** | 同上 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 3 | L2 N-11 supp 教师 J | 0.5 | qwen_plan | qwen3.7-max（**非 reasoning**） | **30 calls**（含 coze/S5/r0 1 补跑 call） | 同上 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 4 | L14 N-11 full 三方配对 | 0.0 | qwen_plan | qwen3.7-max（**非 reasoning**） | **30 calls**（含 GLM_1/L_geography_world/r1 1 补跑 call；re-asked；distill/independent 沿 L14 §4 字面可复用） | 同上 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 5 | L14 N-11 full 三方配对 | 0.3 | qwen_plan | qwen3.7-max（**非 reasoning**） | **30 calls** | 同上 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 6 | L14 N-11 full 三方配对 | 0.5 | qwen_plan | qwen3.7-max（**非 reasoning**） | **30 calls** | 同上 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |

**矩阵汇总**：
- **6 cells / 总 calls ≤ 180 / 实际预计 ≤ 180**（**T1.5 prereg §1.6.3 字面「6 cells / 总 calls ≤ 360 / 实际预计 ≤ 156」0 触**——本棒独立修订为 180 calls；T1.5 120 calls 实测 + T1.5r2 +60 calls 增量 = 180 calls 总预算）
- **总增量 = +60 calls**（沿 T1.5 verdict `52C985429C91` §3.4 字面 + 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面拍板）
- **既有 K-N11-1/2/3/N1/N2 字面一字不动**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5）
- **既有 K-T1-S1/S2/S3 字面一字不动**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 字面；T1.5r2 复用，0 新设数值阈值）
- **K-N11-N1_T1relax 字面 FAIL 根因消除**（plan 字面扩样至 15 pairs/教师 ≥ N_min=10 字面满足 → 字面 PASS；沿 T1.5 verdict `52C985429C91` §3.4 字面 + 派工单 t15_ext 字面拍板）
- **修正条款 C-T15r2-1**（plan 字面扩样修订 20 → 30 calls/cell = +10 calls/cell × 6 cells = +60 calls 总增量，**构造失灵族参数扩展**，非阈值调整）
- **修正条款 C-T15-1**（端点 + 模型替换 + max_tokens=500，沿 T1.5 prereg §1.4 字面不动，**工具失灵族参数修正**，非阈值调整）
- **2 calls 缺位补跑计入预算**（沿 T1.5 verdict `52C985429C91` §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板）
- **qwen t=0.7 baseline 对照基线不重跑**（沿 `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 既有数据）
- **总判定**：T1.5r2 探针 = T1.5 扩样修订探针（construction-failure-fix expansion probe），**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面**

---

## §3 阈值来源表（逐条注明出处件 + SHA-12，**0 新设**）

> **铁律（修订件硬约束）**：本棒 T1.5r2 探针 **0 新设数值阈值**；所有阈值字面沿既有件引用，下表逐条核对；T1.5r2 plan 字面扩样（20 → 30 calls/cell）= 构造失灵族参数扩展（沿 T1.5 verdict §3.4 补正建议字面 + 派工单 t15_ext 字面拍板），**非阈值调整**

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| **K_N11_1_DIFF** | 0.05 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-1 字面 |
| **K_N11_2_DELTA** | 0.05 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-2 字面 |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-3 字面 |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面（沿字面） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §4.3 K-N11-3 字面（沿字面） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8`（自报） | §5.3 K-N11-3 字面（沿字面，盘实测 `8EEF73BF9856` 沿 T1 §9.1 披露） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.5.2 K-T1-S1/S2/S3 字面（T1.5r2 复用沿用） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | §1.5.2 K-T1-S1/S2/S3 字面（T1.5r2 复用沿用一字不动） |
| **TH-17 N_TARGET** | 20 / 教师 | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面 |
| **TH-17 N_TARGET** | 20 / 教师 | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 L2 配置表 |
| **TH-T1-1 N_min** | 10 对/教师（T1 探针放宽，T1.5 + T1.5r2 沿用） | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.4 非退化自证 + §1.8 新增条款 |
| **TH-T1-1 N_min** | 10 对/教师（T1.5 沿用 + K-N11-N1_T1relax 字面 FAIL 根因） | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | §1.4 非退化自证 + §1.8 复用资产（T1.5r2 沿用一字不动） |
| **TH-T1-1 N_min 满足** | 15 pairs/教师 ≥ 10 对/教师（**T1.5r2 plan 字面扩样后字面满足**） | `results/_v4_supp_t15_verdict.md` | `52C985429C91` | §3.4 补正建议字面「5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10」 |
| **TH-T1-1 N_min 满足** | 15 pairs/教师 ≥ 10 对/教师（**T1.5r2 派工单 t15_ext 拍板**） | 派工单 `ask_57981c1bc81e03b9990a06e5` | — | t15_ext 派工单字面「扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）」 |
| **TH-14 5 教师锚定** | kimi / GLM_1 / GLM_2 / coze / minimax | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-14 |
| **TH-15 seed** | 42 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-15 |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §2 INTER_CALL_SLEEP_S |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 INTER_CALL_SLEEP_S |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.6.2 串行间隔（T1.5 + T1.5r2 沿用） |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | §1.6.2 串行间隔（T1.5r2 沿用一字不动） |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext | — | t15_ext 派工单字面「串行 ≥2.5s」 |
| **600s 看门狗** | ≤ 600s / 批 | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §2「600s 看门狗」（沿 T1 + T1.5 沿用） |
| **600s 看门狗** | ≤ 600s / 批 | 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext | — | t15_ext 派工单字面「600s watchdog 拆批」 |
| **Token Plan 5h 配额** | ≤ 5h wall time | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | §1.6.3 总 wall time 上限 ≤ 5h（T1.5r2 沿用一字不动） |
| **Token Plan 5h 配额** | ≤ 5h wall time | 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext | — | t15_ext 派工单字面「qwen token-plan 5h 节制」（沿 T1.5 prereg `8898B964A9D9` §1.6.3 字面不动 + 派工单 t15_ext 拍板） |
| **teamorouter tun 代理** | `http://127.0.0.1:1018` | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | L35 tun proxy 段（T1.5r2 单端点 qwen_plan 不触发） |
| **teamorouter 必走 tun 防封号** | （硬纪律） | PI 2026-09-23 拍板 + user memory 2026-09-23 | — | user memory 「teamorouter/openrouter 必走 tun 代理防封号」（T1.5r2 单端点不触发） |
| **Jaccard 公式** | `J = \|A ∩ B\| / \|A ∪ B\|` token 级 set Jaccard | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §3.2 字面 |
| **Jaccard 公式** | `J = \|A ∩ B\| / \|A ∪ B\|` token 级 set Jaccard | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §3.2 字面 |
| **token regex** | `re.findall(r"[a-z0-9]+\|[一-鿿]", text.lower())` | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §3.2 字面 |
| **schema L14** | `v4_l14_n11full/2` | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 schema 字面 |
| **schema T1** | `v4_t1_sensitivity/1` | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | §1.7 schema 字面 |
| **schema T1.5** | `v4_t15_sensitivity_fix/1` | `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | §1.7 schema 字面（T1.5r2 0 触） |
| **schema T1.5r2** | `v4_t15r2_sensitivity_fix_n10/1` | 本棒 T1.5r2 §1.7 新立 | （本棒） | §1.7 schema 字面（沿 T1.5 schema `v4_t15_sensitivity_fix/1` 扩样版本；仅 schema 版本号扩样字段 = /1 → /n10/1 字面，0 触 T1.5 原 schema 数值字面） |
| **22 caption** | `strip_captions_22.json` | `corpus/v20_caption_surface/strip_captions_22.json` | `6A2656878745` | — |
| **qwen endpoint** | `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **qwen model_id** | `qwen3.7-max` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **mimo endpoint** | `token-plan-cn.xiaomimimo.com/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1.5r2 端点维度砍去，不重测） |
| **mimo model_id** | `mimo-v2.6-pro` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1 verdict 沿结论引用，T1.5r2 不重测） |
| **teamo endpoint** | `api.teamorouter.cn/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1.5r2 端点维度砍去，不重测） |
| **teamo model_id** | `deepseek-v4-flash` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活（T1 verdict 沿结论引用，T1.5r2 不重测） |
| **C-T15-1 端点 + 模型替换 + max_tokens=500** | qwen_plan + qwen3.7-max（非 reasoning）+ max_tokens ≥ 500 | 派工单 `ask_9484b696` t15 + T1 verdict `F1B5E49F3058` §4.1【最高优先】 | — | 派工单 23:33 拍板 + T1 verdict §4.1 字面（**工具失灵族参数修正**，非阈值调整；T1.5 + T1.5r2 沿用一字不动） |
| **C-T15r2-1 plan 字面扩样修订** | 5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls = +60 calls 总增量 + 15 pairs/教师 ≥ N_min=10 | 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext + T1.5 verdict `52C985429C91` §3.4 | — | t15_ext 派工单字面「扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）；总增量 = 6 cells × +10 = +60 calls」+ T1.5 verdict §3.4 字面「+60 calls 接力棒扩 N 至 N_min 满足：5 教师 × 2 prompts × 3 re-asks/cell × 6 cells = 180 calls → 15 pairs/教师 > N_min=10；diff = +60 calls」（**构造失灵族参数扩展**，非阈值调整） |
| **C-T15r2-2 2 calls 缺位补跑** | coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls 计入 +60 calls 预算 | 派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext + T1.5 verdict `52C985429C91` §4.4 方案 A | — | t15_ext 派工单字面「2 calls 超时缺位顺带补跑（cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1）计入 60 calls 预算」+ T1.5 verdict §4.4 字面「方案 A（推荐）：补跑 2 calls（coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3）」（**T1.5 verdict §4.4 方案 A 落地确认**，非阈值调整） |
| **audit-only metadata 字段集** | `v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint` | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` §1.2 + §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板 | `L14V3_MAP_*` | §1.2 字段表 + §6.1 #2 audit-only 拍板（T1.5r2 沿用同字段集一字不动） |

> **0 新设数值阈值声明（修订件硬约束）**：T1.5r2 探针 **0 新设数值阈值**；K-T1-S1/S2/S3 三条均为布尔条件显式化（沿 S-40 教训）+ 沿 T1 + T1.5 字面沿用一字不动，**0 新设数值**；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict + L14 verdict + `0A9EE16267B5` §1 + T1 §1.5.2 + T1.5 prereg §1.5.2 字面一字不动；C-T15r2-1 = 构造失灵族参数扩展（plan 字面扩样），**非阈值调整**（沿派工单 t15_ext 拍板明示「判定阈值一字不动；扩样 = plan 字面修订」）；C-T15r2-2 = 2 calls 缺位补跑，**非阈值调整**（沿 T1.5 verdict §4.4 方案 A + 派工单 t15_ext 字面拍板）；C-T15-1 = 工具失灵族参数修正（端点 + 模型类别 + max_tokens），**非阈值调整**（沿派工单 t15 字面 + T1 verdict §4.1【最高优先】字面沿用）

---

## §4 边界声明（修订件复述）

- **本稿生效即锁**（沿 `D85488A64D89` `AD42992DC75D` + L9 `23879B6CD1CC` `5C579F28634E` + L10 `F6FE005EE3C7` `16E89657DAAA` + T1 `802DECE2286A` `79936B630015` + T1 verdict `F1B5E49F3058` + T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` 锁先例）；**事后不重开不调**
- **本稿是预登记追加件，不是执行件**——执行由 worker 跑（T1.5r2 executor = 新件 `_v4_supp_t15r2_executor.py`，沿 T1.5 executor `558E635F9BA6` checkpoint 模式续跑；T1.5 executor 一字不动），判死由 verdict-keeper 裁因（T1.5r2 verdict = 新件 `_v4_supp_t15r2_verdict.md`，**留 verdict-keeper 起草**，本 prereg 件 0 起草 verdict），证据链由 evidence-auditor 审（沿 8 agent 团队分工）
- **本稿 0 触 v0.2 本体 `D85488A64D89` + 0 触 activation `AD42992DC75D` + 0 触 L9 `23879B6CD1CC` + 0 触 L9 activation `5C579F28634E` + 0 触 L10 `F6FE005EE3C7` + 0 触 L10 activation `16E89657DAAA` + 0 触 T1 追加件 `802DECE2286A` + 0 触 T1 activation `79936B630015` + 0 触 T1 verdict `F1B5E49F3058` + 0 触 T1.5 prereg `8898B964A9D9` + 0 触 T1.5 activation `443EFB39804A` + 0 触 T1.5 result `6B47D389B7AE` + 0 触 T1.5 verdict `52C985429C91` + 0 触 T1.5 executor `558E635F9BA6` + 0 触 L14V3 三件 + 0 触 L2 verdict `E433A06E7BFB` + 0 触 L2 result `FF7B167AE43F` + 0 触 L14 verdict `764F24A21AC8` + 0 触 L14 result `4C11AB9057B9` + 0 触 Track 2 件 `B65619A07B10` / `C846F7FC79EE` + 0 触 `21771E66AF67` + 0 触 `5BA916D1DD24` + 0 触 `6A2656878745`** —— 21 件一字不动（修订件不动既有件字面）
- **本稿 0 触 V1–V3 资产**（letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读）+ 0 触 R5 V4 frozen
- **派生 JSON 不合并**（本棒产物用 `_v4_supp_t15r2_*` prefix 分列，与现有 `_v4_supp_t15_*` + `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；T1.5 executor `558E635F9BA6` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` 0 触动）
- **R4 key 永不明文**（**无例外**）+ **R6 P-G v0/v01 不动** + **R7 plugin spec 不动**
- **§0.5 过渡声明 1 件**：**T1.5r2 扩样修订定位过渡**（T1.5 verdict §3.4 +60 calls 接力棒扩 N + §4.4 补跑 2 calls 两件建议落地为新立线修订件 + 不动 T1.5 prereg + result + verdict + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS）；**不动 v0.2 §0.5 既有 3 件 + L9 §0.5 既有 3 件 + L10 §0.5 既有 2 件 + T1 §0.5 既有 1 件 + T1.5 §0.5 既有 1 件**
- **0 触既有 K-N11-1/2/3/N1/N2 字面**（沿 `0A9EE16267B5` §1 + L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 一字不动）
- **0 触既有 K-T1-S1/S2/S3 字面**（沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 + T1.5 prereg `8898B964A9D9` §1.5.2 一字不动）
- **0 新设数值阈值**（K_N11_3_THRESHOLD = 0.85 沿字面不动；K-T1-S1/S2/S3 均为布尔条件显式化 + 沿 T1 + T1.5 字面沿用一字不动）
- **T1.5r2 定位硬约束**：T1.5 扩样修订探针，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核流程，**不得据此改判** L2/L14 既定结论一字不动 + **不得二次判定** T1 verdict §7 总判定一字不动 + **不得二次判定** T1.5 verdict §1 主读法 + §2 K-T1-S3 字面一字不动

---

## §5 根因三分类 + 真受审标准（沿拍板 #15 + T1 §5 + T1.5 prereg §5 沿用）

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
- **T1.5r2 探针根因列特别要求**：
  - **K-T1-S1 命中** → 根因列必须区分二源（qwen 端点固有 / 温度敏感性）；不可笼统归「敏感性成立」
  - **K-T1-S3 命中（全 6 cells 不翻转）** → 根因列必须说明「qwen t=0.7 baseline 方向稳定 + 跨 temp 维度稳健（qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后 + plan 字面扩样至 30 calls/cell 满足 N_min=10 后真维持方向一致）」+ **T1 verdict 信息量补正**（构造失灵族修正后真稳健入勘误链作 L2/L14 既判稳健性确认）+ **T1.5 verdict §3.4 + §4.4 建议落地确认**（K-N11-N1_T1relax 字面 PASS 根因消除 + 2 calls 缺位补跑完成），**不构成 L2/L14 既判 PASS 的新证据**（仅是既判方向的稳健性确认）；**不二次判定 T1 verdict §7 自身** + **不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面**
  - **K-N11-N1_T1relax 字面 PASS 根因消除确认** → 根因列必须说明「plan 字面扩样至 5 教师 × 2 prompts × 3 re-asks = 15 pairs/教师 ≥ TH-T1-1 = N_min=10 字面满足；原 T1.5 字面 FAIL 根因 = 假证伪族（构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致）已消除；T1.5 verdict §3.4 补正建议落地确认」
  - **partial completion**（6 cells 未跑完撞 5h 配额）→ 根因列必须明示「T1.5r2 部分完成 + 缺 cells 留待 worker 接力棒」

### T1.5r2 探针与 L2/L14 既判 + T1 verdict §7 + T1.5 verdict §1 主读法的根因关联

| T1.5r2 探针结果 | L2/L14 既判影响 | T1 verdict §7 影响 | T1.5 verdict §1 主读法 + §2 K-T1-S3 字面影响 | 根因列 |
|---|---|---|---|---|
| **全 6 cells J 中位 < 0.85**（K-T1-S3 命中） | **0 影响**（L2/L14 既判不动）= 仅入稳健性确认注记 | **不二次判定** T1 verdict §7 自身；**仅作 T1 verdict 信息量补正**：构造失灵族修正后真维持方向一致 = 真稳健入勘误链 | **不二次判定** T1.5 verdict §1 主读法 + §2 K-T1-S3 字面；**仅作 T1.5 verdict §3.4 + §4.4 建议落地确认注记**（T1.5 verdict §1 主读法「判定稳健」既判方向同向确认 + K-N11-N1_T1relax 字面 PASS 根因消除确认） | qwen t=0.7 baseline 方向在 temp 维度稳定 + qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后 + plan 字面扩样至 30 calls/cell 满足 N_min=10 后真维持方向一致；不翻 L2/L14 既判 + 不翻 T1 verdict §7 + 不二次判定 T1.5 verdict §1 主读法 |
| **任一 cell J 中位 ≥ 0.85**（K-T1-S1 命中） | **0 直接影响**（L2/L14 既判一字不动）= 仅入稳健性存疑注记 | **不二次判定** T1 verdict §7 自身；T1.5r2 K-T1-S1 命中 = 仅入稳健性存疑注记（qwen 端点代表性存疑） | **不二次判定** T1.5 verdict §1 主读法 + §2 K-T1-S3 字面；T1.5r2 K-T1-S1 命中 = 仅入 T1.5r2 稳健性存疑注记 | 二源根因（qwen 端点固有 / 温度敏感性）；不翻既判 + 不翻 T1 verdict §7 + 不二次判定 T1.5 verdict §1 主读法 |
| **K-T1-S1 命中 + verdict-keeper 裁因 + verifier 签字** | **可能**触发 L2/L14 既判复核（不翻既判 = 默认；触发复核 = 须走完整流程） | **不二次判定** T1 verdict §7；仅作 L2/L14 既判的复核候选 | **不二次判定** T1.5 verdict §1 主读法 + §2 K-T1-S3 字面；仅作 T1.5r2 探针的复核候选 | 仅作 L2/L14 既判的复核候选；**不得直接翻判** + **不得二次判定 T1 verdict §7** + **不得二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面** |
| **partial completion**（撞 5h 配额） | **0 影响** | **0 影响**（T1 verdict §7 不二次判定） | **0 影响**（T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 不二次判定） | T1.5r2 部分完成注记；缺 cells 留待接力 |

> **铁律（修订件硬约束）**：T1.5r2 探针字面仅入稳健性注记 + T1 verdict 信息量补正 + T1.5 verdict §3.4 + §4.4 建议落地确认 + K-N11-N1_T1relax 字面 PASS 根因消除确认；**L2/L14 既判一字不动是默认状态**；**T1 verdict §7 总判定一字不动是默认状态**；**T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS 一字不动是默认状态**；**改判须走 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程**

---

## §6 自验清单（沿任务自验清单 + 修订件特有检查项）

- [x] T1.5r2 矩阵 6 cells 全部有独立 K-* 字面（§1.5 + §2 汇总表）
- [x] 全部口径可回溯到派工单 t15_ext 原文 + 既有预登记件 + T1 字面 + T1.5 字面 + L2/L14 verdict 字面（§1.1 修订缘由 + §1.4 实验设计 + §3 阈值来源表）
- [x] kill-line 字面风格与既有预登记逐字对齐（K-N11-1/2/3/N1/N2 沿 `0A9EE16267B5` + L2/L14 verdict 字面；K-T1-S1/S2/S3 沿 T1 `802DECE2286A` §1.5.2 + T1 verdict `F1B5E49F3058` §2 + T1.5 prereg `8898B964A9D9` §1.5.2 字面一字不动）
- [x] 判定布尔显式方向（hit=True 触发 / pass=False 触发 / 方向翻转 hit=True）—— 沿 S-40 教训「禁裸 bool」
- [x] key 形态自扫 0 命中（§0 自扫结果）
- [x] 调用预算与节制硬约束写明（§1.6 单批 ≤ 30 calls / 总 ≤ 180 calls / 总 wall time ≤ 5h / calls 预算写死公式 + 派工单 t15_ext 字面拍板）
- [x] 产物链 `_v4_supp_t15r2_*` 命名预定（§1.7 executor / result / verdict 三件 + schema `v4_t15r2_sensitivity_fix_n10/1`）
- [x] 阈值来源表逐条注明出处件 + SHA-12（§3 36 条阈值引用）
- [x] 不翻 L2/L14 既判硬约束声明（§0 边界 + §1.3 claim + §1.5 字面 + §4 边界 + §5 根因关联）
- [x] 不翻 T1 verdict §7 自身硬约束声明（§0 边界 + §1.3 claim + §1.5 字面 + §4 边界 + §5 根因关联）
- [x] **不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面硬约束声明**（§0 边界 + §1.5 字面 + §4 边界 + §5 根因关联 + §0.5 过渡声明）
- [x] T1 verdict 信息量补正声明（§1.5.2 K-T1-S3 字面 + §5 根因关联）
- [x] **T1.5 verdict §3.4 + §4.4 建议落地确认声明**（§0.5 过渡声明 + §1.1 修订缘由 + §1.4 实验设计 + §5 根因关联）
- [x] **K-N11-N1_T1relax 字面 PASS 根因消除确认声明**（§0.5 过渡声明 + §1.1 修订缘由 + §1.5.1 K-N11-N1_T1relax 字面 + §5 根因关联）
- [x] **2 calls 缺位补跑计入预算声明**（§0 边界 + §1.1 修订缘由 + §1.4 实验设计 + §1.6.4 中断-恢复与分批拆跑方案 + §3 阈值来源表 C-T15r2-2）
- [x] audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 + 派工单 `ask_9484b696` `meta_field` 拍板（§0 边界 + §1.4 度量 + §1.7 产物链 + §3 阈值来源表）
- [x] 派生 JSON 不合并声明（§1.7 + §4 边界 + 派工单 t15_ext 字面拍板）
- [x] **0 新设数值阈值声明**（§0 边界 + §1.5 字面 + §3 阈值来源表 + 派工单 t15_ext 字面拍板）
- [x] **0 触既有 21 件字面声明**（§4 边界：v0.2 + activation + L9 + L9 activation + L10 + L10 activation + T1 + T1 activation + T1 verdict + T1.5 prereg + T1.5 activation + T1.5 result + T1.5 verdict + T1.5 executor + L14V3 三件 + L2 verdict + L2 result + L14 verdict + L14 result）
- [x] 报告记诞生 SHA-12 + 大小（§7 报告）

---

## §7 报告（诞生即记）

- **本稿路径**：`results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md`
- **SHA-12 / 字节 / 行数**：见 **RESULT 报告**（harness 外部汇报段）—— 文件内嵌 hash 会触发 self-reference 递归不一致（沿既有 5 件预登记件 `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` + v0.2 + activation + L9 / L10 / T1 / T1.5 追加件 + T1 verdict + T1.5 verdict 均不自指 hash 的惯例）；本稿**生效件冻结 = 末态文件 hash**（PI 复核生效后冻结入 V4 manifest 链）；文件落地末态 hash 与大小以 RESULT 报告为准
- **draft 阶段报值**（本稿交付时）：路径 `results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md`，SHA-12 见 harness RESULT 段（修正 §3 表派工单字段误字面后末态）；字节见 harness RESULT 段；落盘时间 2026-09-26 16:34（写盘）+ 16:36+（§3 表勘误 edit 后）
- **锚定 v0.2 本体**：`D85488A64D89` 命中（v0.2 本体**一字不动**）
- **锚定 L9 / L10 追加件**：`23879B6CD1CC` / `F6FE005EE3C7` 命中（L9 / L10 **一字不动**）
- **锚定 T1 追加件**：`802DECE2286A` 命中（T1 追加件**一字不动**）
- **锚定 T1 verdict**：`F1B5E49F3058` 命中（T1 verdict **一字不动**）
- **锚定 T1.5 prereg**：`8898B964A9D9` 命中（T1.5 prereg **一字不动**）
- **锚定 T1.5 activation**：`443EFB39804A` 命中（T1.5 activation **一字不动**）
- **锚定 T1.5 result**：`6B47D389B7AE` 命中（T1.5 result **一字不动**）
- **锚定 T1.5 verdict**：`52C985429C91` 命中（T1.5 verdict **一字不动**）
- **锚定 T1.5 executor**：`558E635F9BA6` 命中（T1.5 executor **一字不动**）
- **锚定 L2 verdict**：`E433A06E7BFB` 命中（L2 verdict **一字不动**）
- **锚定 L14 verdict**：`764F24A21AC8` 命中（L14 verdict **一字不动**；自报 vs 盘 SHA 漂移沿 T1 §9.1 披露）
- **锚定 L14V3 三件**：`L14V3_*` 命中（L14V3 三件**一字不动**）
- **派工单**：2026-09-26 16:26 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板「+60 calls 规化重跑（N_min≥10 字面满足）」—— 修订定位 = T1.5 prereg §1.4 计划（20 calls/cell → 6 pairs/教师）与 §1.8 N_min=10 字面的结构 gap 修复 + 扩样至 30 calls/cell（5 教师 × 2 prompts × 3 re-asks → 15 pairs/教师 ≥ 10）+ 总增量 = 6 cells × +10 = +60 calls + kill-line 一字不动 + 2 calls 超时缺位顺带补跑 + 预算/节制 = qwen token-plan 5h 节制 + 串行 ≥2.5s + 600s watchdog 拆批 + 中断-恢复同 agent 唤醒 + 产物链 `_v4_supp_t15r2_*` 系 + T1.5 原件 + result + verdict 一字不动
- **生效后状态**：沿 `D85488A64D89` `AD42992DC75D` + T1 `802DECE2286A` `79936B630015` + T1 verdict `F1B5E49F3058` + T1.5 prereg `8898B964A9D9` + T1.5 activation `443EFB39804A` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` 锁先例 → **生效即锁**，事后不重开不调
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（自扫沿 §0 边界声明）
- **派生 JSON 不合并声明**：本棒产物用 `_v4_supp_t15r2_*` prefix 分列（**line 命名建议**：`_v4_supp_t15r2_executor.py` + `_v4_supp_t15r2_result.json` + `_v4_supp_t15r2_verdict.md`）；与现有 `_v4_supp_t15_*`（T1.5 executor + result + verdict）+ `_v4_supp_l1-l14_*` + `_v4_supp_t1_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；**T1.5 executor `558E635F9BA6` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` 0 触动**
- **T1.5r2 定位硬约束再声明**：**T1.5 扩样修订探针（construction-failure-fix expansion probe）**，**不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS**；除 K-T1-S1 命中且 verdict-keeper 裁因 + verifier 签字 + PI 复核，**不得据此改判** L2/L14 既定结论 + **不得二次判定** T1 verdict §7 总判定 + **不得二次判定** T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS
- **0 新设数值阈值再声明**：K_N11_3_THRESHOLD = 0.85 + K_N11_1_DIFF = 0.05 + K_N11_2_DELTA = 0.05 + TH-17 N_TARGET = 20 + TH-T1-1 N_min = 10 全部沿既有件字面一字不动；C-T15r2-1 = 构造失灵族参数扩展（plan 字面扩样），**非阈值调整**；C-T15r2-2 = 2 calls 缺位补跑，**非阈值调整**；C-T15-1 = 工具失灵族参数修正，**非阈值调整**

---

## §8 老实交代（failures & limitations）

- skill `scientific-research-workflows:experimental-design` 本地加载器多次实录 `Local skill not found` —— **未编造 skill 不存在的虚构指令**，按既有 5 件预登记件（`D85488A64D89` + `0A9EE16267B5` + `113CBE555643` + `0A7BCA992B95` + `F6FE005EE3C7`）+ L9 + L10 + T1 追加件 + T1 verdict + **T1.5 prereg + T1.5 activation + T1.5 result + T1.5 verdict + T1.5 executor** + L14V3 三件 + L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` 字面锚执行
- **本稿 = 预登记立线件，非执行件**——执行由 worker 接力棒跑（T1.5r2 executor = 新件 `_v4_supp_t15r2_executor.py`，沿 T1.5 executor `558E635F9BA6` checkpoint 模式续跑），6 cells 矩阵实跑 = 180 calls（含 2 补跑 calls，撞 5h 配额分批拆跑 + 中断-恢复，沿 L14 verdict §9.1 + T1 §1.6.4 + T1.5 prereg §1.6.4 先例）
- **T1.5r2 探针放宽 N_min = 10 对/教师**（沿 T1 `802DECE2286A` §1.4 + T1.5 prereg `8898B964A9D9` §1.4 沿用一字不动；与 L2/L14 既定 N=20/教师 两层并存；**T1.5r2 plan 字面扩样至 5 教师 × 2 prompts × 3 re-asks = 15 pairs/教师 ≥ TH-T1-1 = N_min=10 字面满足**——沿 T1.5 verdict `52C985429C91` §3.4 字面简化拍板 + 实际配对数 = 24 same+cross pairs/教师 > N_min=10）
- **T1.5r2 探针 0 新设数值阈值**；K-T1-S1/S2/S3 沿 T1 + T1.5 字面沿用 + 均为布尔条件显式化（沿 S-40 教训）；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict + L14 verdict + `0A9EE16267B5` §1 + T1 §1.5.2 + T1.5 prereg §1.5.2 字面一字不动
- **T1.5r2 plan 字面扩样是构造失灵族参数扩展**（沿 T1.5 verdict §3.4 补正建议字面「构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致」+ T1 verdict §4.1【最高优先】建议字面），**非阈值调整**——沿派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 拍板明示「判定阈值一字不动；扩样 = plan 字面修订」
- **T1.5r2 = T1.5 verdict §3.4 + §4.4 建议落地为新立线修订件**——T1.5 verdict §3.4 拍板「+60 calls 接力棒扩 N 至 N_min 满足」+ §4.4 拍板「补跑 2 calls（方案 A）」两件建议落地；T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族 + §4 2 calls 超时不补跑 三件裁定一字不动；T1.5r2 仅作建议落地确认注记，**不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑**
- **T1.5r2 = 派生独立产物链**（`_v4_supp_t15r2_*`）+ **T1.5 executor `558E635F9BA6` + T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` 0 触动**——沿 T1.5 executor checkpoint 模式续跑（`.tmp/_t15r2_records.json`），T1.5 executor checkpoint 文件 `.tmp/_t15_records.json` 不动
- **T1.5 verdict §3.4 接力棒命名建议 vs 派工单产物链命名**：T1.5 verdict §3.4 字面建议接力棒命名 = `_v4_supp_t15_r2_*`（下划线 r2）；派工单 t15_ext 字面拍板 = `_v4_supp_t15r2_*`（无下划线 r2，紧贴 t15）—— **本棒沿派工单 t15_ext 字面拍板**（高优先级 override），verbatim 引用 T1.5 verdict §3.4 时保留其字面（`_v4_supp_t15_r2_*`）作 verbatim 引用证据
- **同 caption J 拆解沿 T1.5 verdict §6 保守口径 + 待 PI 复核拍板**：T1.5r2 worker 沿用 T1.5 worker 自加 same_caption_breakdown 字段（**沿用字面**），仅作 informational 注记；**不外推**为 L2/L14 既判反证 / K-N11-N2 字面修订主依据 / T1 verdict 信息量边界声明补充 / T1.5 verdict 信息量补正主线修订；**待 PI 复核拍板**
- **本稿 0 触 21 件既有件字面**：v0.2 + activation + L9 + L9 activation + L10 + L10 activation + T1 + T1 activation + T1 verdict + T1.5 prereg + T1.5 activation + T1.5 result + T1.5 verdict + T1.5 executor + L14V3 三件 + L2 verdict + L2 result + L14 verdict + L14 result + Track 2 件 + 度量函数 + 3 proxy 算子 + 22 caption —— 全部一字不动（沿 §4 边界声明）

---

## 备注：派工单字段勘误

> 本棒在 §3 阈值来源表「Token Plan 5h 配额」字段引用派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 时，原稿误写「t09_ext」+ 备注「派工单编号 = `ask_57981c1bc81e03b9990a06e5`，非 t09；修正派工单字段」—— **本字段勘误仅为 §3 阈值来源表内部备注，非派工单实际编号错误**；派工单 `ask_57981c1bc81e03b9990a06e5` t15_ext 编号正确，本棒所有其他处引用派工单均为 `ask_57981c1bc81e03b9990a06e5` t15_ext 字面，无其他错漏。