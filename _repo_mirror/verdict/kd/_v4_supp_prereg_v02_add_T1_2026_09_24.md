# V4 补测预登记 v0.2 T1 追加件 · L2/L14 温度敏感性 + mimo/teamo 端点补测 稳健性探针（2026-09-24）

- **性质**：protocol-keeper 追加立线（派工单 2026-09-24 follow-up，protocol-keeper 起草；本棒从 PI 2026-09-24 派工「T1 辅助检验预登记」—— L2/L14 温度敏感性（temp=0.0/0.3/0.5）+ mimo/teamo 端点补测 稳健性探针；本稿不调用任何 LLM，不跑实验，仅固化 T1 立线 + 矩阵字面 + kill-line 字面 + 调用预算 + 阈值来源表 + 沿 L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` 双件先例）
- **定位（边界）**：**T1 = 稳健性辅助检验（sensitivity probe）**，**不翻 L2/L14 正式判定**；结论仅作**稳健性注记**入勘误链。除非 T1 kill-line 命中（方向翻转）**且另走 verdict-keeper 裁因 + verifier 签字流程**，**不得据此改判** L2/L14 既定结论。
- **预登记件本体不动**：`results/_v4_supp_prereg_v02_2026_09_24.md` SHA-12 `D85488A64D89` 锁后**一字不改**；L2 verdict `_v4_supp_l2_n11supp_verdict.md` SHA-12 `E433A06E7BFB` 锁后**一字不改**；L14 verdict `_v4_supp_l14_n11full_verdict.md` SHA-12 `764F24A21AC8` 锁后**一字不改**；本棒以独立追加件形式立线（沿 L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` + 各自 activation 先例）
- **PI 复核待生效**（沿 `D85488A64D89` activation `AD42992DC75D` + L9 activation `5C579F28634E` + L10 activation `16E89657DAAA` 锁先例）—— T1 立线 + 矩阵字面 + kill-line 字面（方向翻转 = hit=True）+ 调用预算 + 产物链 `_v4_supp_t1_*` 待 PI 复核生效；**生效即锁**（沿 `0A7BCA992B95` 锁先例），事后不重开不调；**「CONDITIONAL PASS」退役**，只用 PASS / FAIL 二值（沿 R6 实证）
- **范围**：T1 稳健性探针 = {L2 N-11 supp 教师 J 判定, L14 N-11 full 三方配对} × {temp ∈ {0.0, 0.3, 0.5}} × {mimo: token-plan-cn.xiaomimimo.com, teamo: api.teamorouter.cn} = 12 cells 矩阵；qwen token-plan 端点既有数据（沿 `B65619A07B10` ROUTE_TEMPLATES[0]，temp=0.7）作对照基准**不重跑**；不含 L1 N-28 / L3 N-20 / L4 N-26 / L5 C-S39 / L6 S-38 / L7 E-N20 / L8 N-12 等其它线（沿 v0.2 §1-§8 字面不动）；不含 v0.2 §0.5 既有 3 件过渡声明（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）；不含 L9 §0.5 过渡声明 3 件；不含 L10 §0.5 过渡声明 2 件
- **判定依据**：deposon 项目核心准则四条「大材小用，落到实处，与死同行，虚实回路（FTFB）」（PI 2026-09-22 R1 录入 + 2026-09-23 FTFB 入根 + **准则为根，论文为一处外显**；详见 `113CBE555643` §0 注）—— 三问映射沿既有预登记件 §1.1.1 代拟稿 §1 + 种子稿 §0 + 整合补充稿 §1（沿 `0A7BCA992B95` §1）

---

## 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | SHA-12 | 字节 | 用途 |
|---|---|---|---|---|
| v0.2 预登记本体（锚定不动） | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | 42,764 | T1 立线锚定 + 通用条款格式（TH-* / 派生 JSON / 双读法 / 阈值表） |
| v0.2 activation 件 | `results/_v4_supp_prereg_v02_activation_2026_09_24.md` | `AD42992DC75D` | 3,202 | T1 立线后状态沿 `AD42992DC75D` 锁先例 |
| L9 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md` | `23879B6CD1CC` | 19,586 | T1 立线锚定 + 双读法并记先例（K-A2R-R1/N1） |
| L9 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L9_activation_2026_09_24.md` | `5C579F28634E` | 3,924 | T1 立线后 L9 沿 `5C579F28634E` 锁先例 |
| L10 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L10_2026_09_24.md` | `F6FE005EE3C7` | 26,159 | T1 立线锚定 + 语义反转注释先例（K-E-N20-3 语义反转双栏并记） |
| L10 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_L10_activation_2026_09_24.md` | `16E89657DAAA` | 9,442 | T1 立线后 L10 沿 `16E89657DAAA` 锁先例 |
| 方法预登记补充稿 | `results/_v4_methods_prereg_supplement_2026_09_23.md` | `0A7BCA992B95` | 59,570 | §1 通用条款 + 格式基线 |
| N-09~N-39 预登记 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | 60,530 | §1 K-N11 字面（L2/L14 判定件均沿此字面） |
| 种子预登记补充稿 | `results/_v4_seeds_prereg_supplement_2026_09_23.md` | `113CBE555643` | 53,633 | §0 注 + 格式基线 |
| **L2 N-11 supp verdict（锚定 T1 字面源 1）** | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | 15,671 | K-N11-1/2/3/N1/N2 字面（沿 `0A9EE16267B5` §1）+ 教师 J 实测 (qwen t=0.7, N=2, J 中位 0.41-0.52) |
| L2 N-11 supp result | `results/_v4_supp_l2_n11supp_result.json` | `FF7B167AE43F` | 17,970 | L2 N-11 supp 数据（qwen 端点） |
| **L14 N-11 full verdict（锚定 T1 字面源 2）** | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | 19,708 | K-N11-1/2/3/N1/N2 字面 + schema `v4_l14_n11full/2` + 教师 J 实测 (qwen t=0.7, N=20, J 中位 0.36-0.39) |
| L14 N-11 full result | `results/_v4_supp_l14_n11full_result.json` | `4C11AB9057B9` | 12,246 | L14 N-11 full 数据（qwen 端点） |
| Track 2 multimodel probe | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | — | 三端点 ROUTE_TEMPLATES + tun 代理 + 串行 ≥2s |
| Track 2 endpoints probe | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | 5,803 | qwen_plan / mimo / teamo 三端点权威源 |
| Track 2 multimodel verdict (件 3) | `results/_v4_track2_multimodel_verdict_2026_09_23.md` | （自身 SHA） | 12,883 | 6 模型补跑判定（qwen3.7-max / mimo / teamo 等） |

> 注：L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` 两件 SHA-12 已实测（沿 L14 verdict §0 自核表），T1 字面沿此两件 + `0A9EE16267B5` §1 N-11 字面；本棒 0 触动此两件（一字不动）。

---

## §0 边界声明（沿 R5 / R6 / R7 复审稿，2026-09-23 勘误版）

- **0 LLM 调用**：本稿由 protocol-keeper 起草，全程未调用任何 LLM API；纯文件编辑（write/edit），未调任何 LLM/代理/构造代理/网关；沿 V4 §3.1 放开语境明示可调（PI 2026-09-22「V3 的剑不斩 V4 的官」），本棒无需调
- **R4 key 永不明文**（**无例外**，沿 R4 + PI 2026-09-22「key 永不明文等合理且无冲突的铁律要沿用」）：本稿及其后续产物不写入、不引用、不打印任何明文 API key / 平台密钥；key 仅在进程组方法里以 runtime env 读取；**本稿自扫** `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态 0 命中
- **R5 V4 frozen 只追加**（**V4 沿用 V1–V3 资产只读底线**）：本稿不修改 v0.2 预登记件 `D85488A64D89` / 不动 activation 件 `AD42992DC75D` / 不动 L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` / 不动 L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` / 不动 L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F` / 不动 L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`；**派生 JSON 不合并**（本棒产物用 `_v4_supp_t1_*` prefix 分列，与现有 `_v4_supp_l1-l10_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立）
- **R6 P-G v0/v01 / R7 plugin spec**：本棒不动 P-G v0/v01；不动 plugin spec；不动 verifier 内置脚本
- **V1–V3 只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）
- **kill-line 字面不动禁私设条款**（S-40 教训：判定布尔显式方向 `hit=True` 即触发 / `pass=True` 即存活，禁裸 bool；PI 2026-09-23 拍板明示「禁止擅自调阈值 / 禁止合并派生 JSON / 禁止私设 kill-line 条款」）：本棒 T1 kill-line 字面**完全沿** L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 字面（K-N11-1/2/3/N1/N2 + K-N11-N2 双读法），**0 触既有 K-N11 字面**；**T1 新增 K-T1-S1（敏感性 flip 触发线）**：方向翻转即 `hit=True` → 标注「稳健性存疑注记」，但**不据此翻 L2/L14 正式判定**（沿定位声明 + §1.5 双向门槛）；**阈值一律沿 L2/L14 字面 = K_N11_3_THRESHOLD = 0.85** 等，**禁新设**
- **0 擅调阈值**（沿 v0.2 §0 同口径）：本棒 **0 调既有 K_N11_1_DIFF = 0.05 / K_N11_2_DELTA = 0.05 / K_N11_3_THRESHOLD = 0.85 / TH17_N_TARGET = 20**；T1 沿用一字不动
- **T1 定位硬约束**：本棒 = 稳健性辅助检验（sensitivity probe），**不翻 L2/L14 正式判定**；除 T1 kill-line 命中（方向翻转 = hit=True）**且另走 verdict-keeper 裁因 + verifier 签字流程**，**不得据此改判 L2/L14 既定结论**（沿 L2 verdict `E433A06E7BFB` §11 总判定「K-N11-3 真证伪」+ L14 verdict `764F24A21AC8` §11 总判定「K-N11-3 真证伪」既定结论一字不动）
- **skill 加载老实交代**：派工单要求 `scientific-research-workflows:experimental-design` skill，本地 skill 加载器多次实录 `Local skill not found`（沿 v0.2 §0 + L9 §0 + L10 §0 同口径）—— 本棒按 v0.2 `D85488A64D89` + activation `AD42992DC75D` + L9 追加件 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 追加件 `F6FE005EE3C7` + L10 activation `16E89657DAAA` + 既有 3 件预登记件 `113CBE555643` `0A7BCA992B95` `0A9EE16267B5` + L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` 的格式与字面锚执行，**未编造 skill 不存在的虚构指令**

---

## §0.5 过渡声明（本棒 T1 立线件特有）

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）

- **T1 稳健性探针定位过渡**：自本件立线起标「**已知 L2 N-11 supp（qwen t=0.7, N=2）教师 J 中位 0.41-0.52 + L14 N-11 full（qwen t=0.7, N=20）教师 J 中位 0.36-0.39 均 < 0.85 = K-N11-3 真证伪既判；T1 矩阵 12 cells 跑出前不预设 PASS / FAIL 翻转**」——
  - L2 verdict `E433A06E7BFB` §11 总判定 = 「FAIL（构造不可行 — 一等结论，归假证伪族）」（前棒 N=2 致 K-N11-N1 FAIL，但 K-N11-3 字面真证伪方向一致）
  - L14 verdict `764F24A21AC8` §11 总判定 = 「FAIL（K-N11-3 真证伪 qwen 固有方差；N=20 收敛稳定 0.36-0.39 区间）」
  - T1 在 {temp 0.0 / 0.3 / 0.5} × {mimo / teamo} 矩阵下探「教师 J 中位是否仍 < 0.85」—— 若任一 cell 翻 ≥0.85，**仅记「稳健性存疑」注记**（qwen 固有方差 vs 教师端点固有 vs 温度敏感性三源），**不据此翻 K-N11-3 真证伪既定判**（qwen 端点 + temp=0.7 是既定条件，方向翻转只质疑 qwen 端点的代表性而非整体判死）
  - 全 12 cells 仍 J < 0.85（无翻转） = 「**判定稳健**」 = 不入勘误链（仅作稳健性确认注记）
- **本棒不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 过渡声明 3 件** + **不动 L10 §0.5 过渡声明 2 件**

---

## §1 T1 · L2/L14 温度敏感性 + mimo/teamo 端点补测 稳健性探针

### 1.1 三问初判

- **Q1 ✓**：素材面已齐——
  - L2 N-11 supp verdict `E433A06E7BFB` + result `FF7B167AE43F`（qwen t=0.7, N=2, 5 教师 4 prompts × 2 re-asks = 20 calls，J 中位 0.41-0.52）
  - L14 N-11 full verdict `764F24A21AC8` + result `4C11AB9057B9`（qwen t=0.7, N=20, 5 教师 2 prompts × 5 re-asks = 50 calls，J 中位 0.36-0.39 收敛）
  - mimo 端点 `token-plan-cn.xiaomimimo.com/v1` model_id `mimo-v2.6-pro` 探活 OK（沿 `_track2_endpoints_probe_2026_09_23.json` `C846F7FC79EE` §0）
  - teamo 端点 `api.teamorouter.cn/v1` model_id `deepseek-v4-flash` 探活 OK（沿 `C846F7FC79EE` §0）+ PI 2026-09-23 硬纪律「teamorouter 必走 tun 防封号」
  - Track 2 多端点判定件 `_v4_track2_multimodel_verdict_2026_09_23.md` 6 模型补跑锚定（qwen3.7-max / mimo-v2.6-pro / deepseek-v4-flash-teamo 等）
- **Q2 ✓**：实验设计可执行——
  - 12 cells 矩阵 = {L2, L14} × {temp 0.0, 0.3, 0.5} × {mimo, teamo}
  - 每 cell = 沿 L2/L14 verdict 字面（K-N11-3 教师 J 中位 < 0.85 字面）+ 5 教师锚定（沿 TH-14）+ 22 caption（沿 `6A2656878745`）+ 端点替换 + 温度替换
  - 单 cell calls：每教师 4 prompts × 2 re-asks × 1 端点 × 1 temp = 40 calls（沿 L2 baseline 口径）；最小复算样本可压至 N=10 对/教师（沿 L2 baseline N=2 上调，但 TH-17 N=20 仍是最终目标；T1 探针允许最小 N=10 对/教师起步）
  - L14 维度：可沿 L14 verdict §2 字面（5 教师 × 2 prompts × 5 re-asks = 50 calls 目标），最小复算样本可压至 N=10 对/教师（re-asked trace 维度）
- **Q3 ✓**：证伪方向明确——
  - 「温度 / 端点维度上判定结果出现方向翻转」= **敏感性成立**（K-N11-3 真证伪方向不稳健）
  - 「温度 / 端点维度上判定结果维持方向一致」= **判定稳健**（K-N11-3 真证伪方向在不同 temp / 端点下稳定）
  - **字面判**：教师 J 中位 ≥ 0.85 = 方向翻转 → K-T1-S1 hit=True → 标注「稳健性存疑注记」

### 1.2 矩阵定义（12 cells）

| # | 维度（沿 L2 verdict / L14 verdict） | 温度 | 端点 | model_id | 代理 | calls 上限 / cell |
|---|---|---|---|---|---|---|
| 1 | L2 N-11 supp 教师 J 判定（沿 `E433A06E7BFB` §3.2 + §4.3） | 0.0 | mimo: token-plan-cn.xiaomimimo.com/v1 | mimo-v2.6-pro | 否 | ≤ 60 calls（5 教师 × 2 prompts × 2 re-asks × 3 内层重试预留） |
| 2 | L2 N-11 supp 教师 J 判定 | 0.0 | teamo: api.teamorouter.cn/v1 | deepseek-v4-flash | **是**（tun `http://127.0.0.1:1018`） | ≤ 60 calls |
| 3 | L2 N-11 supp 教师 J 判定 | 0.3 | mimo | mimo-v2.6-pro | 否 | ≤ 60 calls |
| 4 | L2 N-11 supp 教师 J 判定 | 0.3 | teamo | deepseek-v4-flash | 是 | ≤ 60 calls |
| 5 | L2 N-11 supp 教师 J 判定 | 0.5 | mimo | mimo-v2.6-pro | 否 | ≤ 60 calls |
| 6 | L2 N-11 supp 教师 J 判定 | 0.5 | teamo | deepseek-v4-flash | 是 | ≤ 60 calls |
| 7 | L14 N-11 full 三方配对（沿 `764F24A21AC8` §4 + §5 schema `v4_l14_n11full/2`） | 0.0 | mimo | mimo-v2.6-pro | 否 | ≤ 60 calls（5 教师 × 2 prompts × 2 re-asks × 3 内层重试预留；re-asked trace 维度；distill + independent 沿 `21771E66AF67` + `5BA916D1DD24` 只读复用） |
| 8 | L14 N-11 full 三方配对 | 0.0 | teamo | deepseek-v4-flash | 是 | ≤ 60 calls |
| 9 | L14 N-11 full 三方配对 | 0.3 | mimo | mimo-v2.6-pro | 否 | ≤ 60 calls |
| 10 | L14 N-11 full 三方配对 | 0.3 | teamo | deepseek-v4-flash | 是 | ≤ 60 calls |
| 11 | L14 N-11 full 三方配对 | 0.5 | mimo | mimo-v2.6-pro | 否 | ≤ 60 calls |
| 12 | L14 N-11 full 三方配对 | 0.5 | teamo | deepseek-v4-flash | 是 | ≤ 60 calls |

**矩阵 cell 总数 = 12 cells × ≤ 60 calls/cell = ≤ 720 calls（硬上限）**

**对照基准（不重跑）**：
- qwen token-plan 端点 `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` model_id `qwen3.7-max` 既有数据（沿 L2 verdict `E433A06E7BFB` §3 + L14 verdict `764F24A21AC8` §3）= **temperature = 0.7** = 对照基线**不重跑**；T1 探针仅在 mimo / teamo 两端点下跑 temp ∈ {0.0, 0.3, 0.5}
- qwen 端点 t=0.7 baseline 既判（K-N11-3 真证伪：J 中位 0.36-0.39 < 0.85）作 12 cells 比照锚

### 1.3 claim（可证伪命题）

T1 矩阵 12 cells 在 {temp 0.0/0.3/0.5} × {mimo, teamo} 维度上，5 教师 re-asked Jaccard 中位数（沿 L2/L14 verdict §3.2 字面 = `Jaccard = |A ∩ B| / |A ∪ B|` token 级 set Jaccard，token = `re.findall(r"[a-z0-9]+|[一-鿿]", text.lower())`）维持 qwen t=0.7 既判方向 = **教师 J 中位 < K_N11_3_THRESHOLD = 0.85**（沿 L2/L14 字面一字不动）。任一 cell 教师 J 中位 ≥ 0.85 = 方向翻转 = **K-N11-3 真证伪方向在该 cell 不稳健**。

**本 claim 字面完全沿** L2 verdict `E433A06E7BFB` §4.3 + L14 verdict `764F24A21AC8` §5.3 字面（K-N11-3 教师 J 中位 < 0.85 → FAIL）+ `0A9EE16267B5` §1 K-N11-3 字面一字不动。

**T1 探针限定（不翻 L2/L14 正式判定的硬约束）**：
- T1 命中方向翻转（K-T1-S1 hit=True）= 标注「**稳健性存疑注记**」入勘误链
- T1 命中方向翻转**不直接翻** L2/L14 verdict 既定 K-N11-3 真证伪结论（qwen t=0.7 是既定条件）
- T1 命中方向翻转仅作「**qwen 端点代表性存疑**」注记（即：若 mimo / teamo / 不同 temp 下 J 中位 ≥ 0.85，仅说明 qwen 端点下 qwen 教师固有的语言学方差是该特定 (端点, temp) 组合下的特征，不构成对 L2/L14 既判的反证）
- T1 全 12 cells 不命中（方向一致）= 「**判定稳健**」确认注记（K-N11-3 真证伪方向在 temp / 端点维度稳定）

### 1.4 实验设计

- **素材**：
  - L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F`（L2 维度）
  - L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`（L14 维度）
  - `0A9EE16267B5` §1 N-11 K-* 字面（沿用一字不动）
  - 22 caption `strip_captions_22.json` `6A2656878745`
  - 5 by_model（沿 TH-14：kimi / GLM_1 / GLM_2 / coze / minimax）
  - Track 2 multimodel probe `B65619A07B10`（ROUTE_TEMPLATES + tun + 串行 ≥2s）
  - Track 2 endpoints probe `C846F7FC79EE`（mimo / teamo 探活锚）
  - Track 2 multimodel verdict `_v4_track2_multimodel_verdict_2026_09_23.md`（6 模型补跑锚定：mimo-v2.6-pro / deepseek-v4-flash-teamo / qwen3.7-max 等）
  - `_v4_distill_min_measure.py` `21771E66AF67`（L14 维度 distill 提取函数，只读复用）
  - `_v4_proxy_student_generators.py` `5BA916D1DD24`（L14 维度 3 proxy 算子，只读复用）
- **构造**：
  - **L2 维度**（沿 L2 verdict `E433A06E7BFB` §2 字面）：
    - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell × 3 temp × 2 端点 = 240 calls（L2 总）
    - prompt 子集沿 L2 verdict `E433A06E7BFB` §2 = seed=42 抽 2 caption (`L_biological_taxonomy`, `S5`)
    - temperature ∈ {0.0, 0.3, 0.5} 替换 qwen t=0.7 baseline
    - 端点 mimo / teamo 替换 qwen_plan baseline
    - 主度量 = 教师 re-asked Jaccard 中位（同 L2 verdict §3.2 字面）
  - **L14 维度**（沿 L14 verdict `764F24A21AC8` §2 字面）：
    - 5 教师 × 2 prompts × 2 re-asks = 20 calls / cell × 3 temp × 2 端点 = 240 calls（L14 总）
    - prompt 子集沿 L14 verdict `764F24A21AC8` §2 = `L_geography_world` + `L_historical_causality`
    - max_tokens = 100（沿 L14 verdict `764F24A21AC8` §2；L14 已沿用）
    - temperature / 端点替换同上
    - 主度量 = 教师 re-asked Jaccard 中位（同 L14 verdict §3.2 字面）；L14 三方配对（re-asked + distill + independent）作为辅助度量（沿 L14 verdict §4 字面，N=20 收敛稳定方向一致时可简化只跑 re-asked）
- **度量**：
  - **主度量** = Jaccard 中位数（per teacher, per cell）—— 沿 L2/L14 verdict §3.2 / §3.2 字面不动
  - **辅助度量**（L14 维度）：三方 max-min diff + distill J - teacher J delta（沿 L14 verdict §4.1/§4.2 字面不动）+ independent J（沿 L14 verdict §4.3 字面不动）
  - **稳健性度量** = bootstrap CI 95%（沿 K-N11-N2 双读法）+ per 教师 N 评估 + 跨温度 / 跨端点 J 中位标准差
- **拍板出处**：PI 2026-09-24 派工单「T1 辅助检验预登记——L2/L14 温度敏感性 + mimo/teamo 端点补测（即锁）」
- **真审条件**：worker 接力棒分批跑；单批 ≤ 600s 看门狗；撞 5h 配额中断-恢复（沿 L14 §9.1 中断恢复先例）
- **非退化自证**：每 cell 5 教师 N_min = 10 对/教师（T1 探针放宽，TH-17 N=20 是 L2/L14 既判的目标，非 T1 探针的硬门槛；理由：T1 = 敏感性探针，方向翻转定性即可，不需 N=20 全收敛）—— 沿 L2 verdict `E433A06E7BFB` §2 baseline N=2 / L14 verdict §2 N=20 双向放宽
- **双读法并记**（沿 K-N11-N2 字面）：
  - 构造面（单 cell N=10）= T1 探针单 cell 内 J 中位
  - 真实面（跨 cell 累加 N≥30）= 跨同端点 / 同温度 cell 累加 J 中位
  - 任一面 PASS ≠ T1 探针成立（必须双向一致）

### 1.5 机械判死线（kill-line，字面即锁，禁私设条款）

> **字面不动声明**：既有 K-N11-1/2/3/N1/N2 字面（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 + `0A9EE16267B5` §1）**一字不动**；本棒仅在 K-N11-3 基础上加 T1 字面敏感性触发线（**K-T1-S1** + **K-T1-S2**），**0 触既有 K-N11 字面**，**0 新设阈值**（K_N11_3_THRESHOLD = 0.85 沿用一字不动）。

#### 1.5.1 既有 K-N11 字面（沿 L2/L14 verdict 一字不动，锁前痕迹保留）

- **K-N11-1**：三方 Jaccard 中位数差异 < K_N11_1_DIFF = 0.05 即 `hit=True` → FAIL（三方不可分离）—— **沿 `0A9EE16267B5` §1 K-N11-1 字面**
- **K-N11-2**：distill J > teacher J + K_N11_2_DELTA = 0.05 不成立即 `hit=True` → FAIL（与原假设反向）—— **沿 `0A9EE16267B5` §1 K-N11-2 字面**
- **K-N11-3**：教师两次 J 中位数 < K_N11_3_THRESHOLD = 0.85 即 `hit=True` → FAIL（教师自身不稳定，主度量失效）—— **沿 `0A9EE16267B5` §1 K-N11-3 字面**（**T1 探针核心沿此字面**）
- **K-N11-N1**：N < TH17_N_TARGET = 20 / 教师 即 `pass=False` → FAIL（构造退化致命题不明）—— **沿 v0.2 §2 L2 K-N11-N1 字面**（**T1 探针放宽至 N_min=10** 不动此字面，T1 N_min=10 为探针放宽口径与 K-N11-N1 字面 N=20 是两层并存）
- **K-N11-N2**：构造面 K-N11-1/2/3 + 真实面 K-N11-1/2/3 **并记**；任一面 PASS ≠ 命题成立（必须双面都过）—— **沿 v0.2 §2 L2 K-N11-N2 字面**

#### 1.5.2 T1 新增 kill-line（敏感性 flip 触发线 + 稳健性确认线，0 新设阈值）

- **K-T1-S1（温度敏感性 flip 触发线 · 主判定）**：
  - **字面**：在任一固定端点（mimo 或 teamo）下，沿 L2 维度或 L14 维度，教师 J 中位数跨温度 {0.0, 0.3, 0.5} 中**任一温度点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**（显式布尔，避免裸 bool 歧义）：
    - 既定方向 = qwen t=0.7 baseline 教师 J 中位 < 0.85（沿 L2 verdict `E433A06E7BFB` §3.2 + L14 verdict `764F24A21AC8` §3.2 实测）
    - 翻转条件 = 新 (端点, 维度, 温度) cell 教师 J 中位 ≥ 0.85
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（沿 L2/L14 verdict + `0A9EE16267B5` §1 字面，**0 新设**）
  - **不翻 L2/L14 正式判定**（沿定位声明）：K-T1-S1 hit=True 仅入稳健性注记，**不据此改判** L2 verdict `E433A06E7BFB` §11「FAIL 真证伪」+ L14 verdict `764F24A21AC8` §11「FAIL K-N11-3 真证伪」既定结论一字不动
- **K-T1-S2（端点敏感性 flip 触发线 · 主判定）**：
  - **字面**：在任一固定温度（0.0 / 0.3 / 0.5）下，沿 L2 维度或 L14 维度，教师 J 中位数跨端点 {mimo, teamo} 中**任一端点 J 中位 ≥ K_N11_3_THRESHOLD = 0.85** 即 `hit=True` → 「**K-N11-3 真证伪方向在该 (温度, 维度) 上不稳健**」= 标注「**稳健性存疑注记**」入勘误链
  - **方向翻转定义**：同 K-T1-S1，仅 (端点) 维度替换 (温度) 维度
  - **阈值沿用**：K_N11_3_THRESHOLD = 0.85（一字不动）
  - **不翻 L2/L14 正式判定**：同 K-T1-S1
- **K-T1-S3（稳健性确认线 · 副判定）**：
  - **字面**：12 cells 全 J 中位 < 0.85 = 「**判定稳健**」= T1 探针不命中 K-T1-S1 / K-T1-S2 → 仅入稳健性确认注记，**不入勘误链**（K-N11-3 真证伪方向在 temp / 端点维度稳定）
  - **判定方式**：任一 cell 触发 K-T1-S1 或 K-T1-S2 = 探针命中；全 12 cells 不触发 = 探针不命中

#### 1.5.3 T1 kill-line 字面总览（沿 L2/L14 verdict + `0A9EE16267B5` 字面）

| K-* | 字面 | hit 触发条件 | hit=True 后果 | 字面源 |
|---|---|---|---|---|
| K-N11-1 | 三方 Jaccard 中位数差异 < 0.05 → FAIL | 三方 max-min diff < 0.05 | L2/L14 cell 内部 FAIL | `0A9EE16267B5` §1 |
| K-N11-2 | distill J > teacher J + 0.05 不成立 → FAIL | delta = distill J - teacher J ≤ 0.05 | L2/L14 cell 内部 FAIL | `0A9EE16267B5` §1 |
| K-N11-3 | 教师两次 J 中位数 < 0.85 → FAIL | per teacher J median < 0.85 | L2/L14 cell 内部 FAIL（T1 探针主度量） | `0A9EE16267B5` §1 |
| K-N11-N1 | N < 20 / 教师 → pass=False → FAIL | per teacher N < 20 | L2/L14 cell 内部 FAIL | v0.2 §2 L2 |
| K-N11-N2 | 构造面 + 真实面双读法并记 | 任一面 PASS ≠ 命题成立 | L2/L14 cell 内部 FAIL | v0.2 §2 L2 |
| **K-T1-S1（新增）** | 任一温度点 J 中位 ≥ 0.85 → hit=True → 稳健性存疑注记 | 跨温度 {0.0, 0.3, 0.5} 任一 ≥ 0.85 | T1 探针命中（**不翻 L2/L14 既判**） | 本棒新增（阈值沿 `0A9EE16267B5` §1 K-N11-3 字面） |
| **K-T1-S2（新增）** | 任一端点 J 中位 ≥ 0.85 → hit=True → 稳健性存疑注记 | 跨端点 {mimo, teamo} 任一 ≥ 0.85 | T1 探针命中（**不翻 L2/L14 既判**） | 本棒新增（阈值沿 `0A9EE16267B5` §1 K-N11-3 字面） |
| **K-T1-S3（新增）** | 全 12 cells J 中位 < 0.85 = 判定稳健 | 12 cells 全 < 0.85 | T1 探针不命中（确认注记，**不入勘误链**） | 本棒新增 |

> **0 新设阈值声明**：K-T1-S1/S2/S3 三条**0 新设数值阈值**；K_N11_3_THRESHOLD = 0.85 沿 L2 verdict `E433A06E7BFB` §2 + L14 verdict `764F24A21AC8` §2 + `0A9EE16267B5` §1 字面一字不动；T1 探针字面「方向翻转 = hit=True」是布尔条件显式化（沿 S-40 教训「判定布尔显式方向」），**不构成阈值私设**

### 1.6 调用预算与节制（Token Plan 5h 限额硬约束）

> **硬约束声明**：T1 探针**0 触 L2/L14 verdict 既定 5h 配额节制原则**（沿 L14 verdict §9.1 中断恢复先例）；本棒新立 T1 独立配额，与 L2/L14 既定 5h 配额**物理隔离**（端点不同 = qwen vs mimo/teamo；worker 接力棒按端点分批）

#### 1.6.1 单批 calls 上限（看门狗约束）

- **单批 ≤ 30 calls**（沿 L2 verdict §2「600s 看门狗」+ L14 verdict §9.1「280s hard limit + sub-batch strategy」双向沿用，每 30 calls 预估 600-700s wall time 含 2.5s 串行间隔）
- **每 cell 拆批**：每 cell ≤ 60 calls / 拆 2 批 × 30 calls / 批
- **12 cells × 2 批 / cell = 24 批**（理论上限；实际跑按需调整）

#### 1.6.2 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 L2 verdict `E433A06E7BFB` §2 INTER_CALL_SLEEP_S + L14 verdict `764F24A21AC8` §2 INTER_CALL_SLEEP_S + Track 2 runner `INTER_CALL_SLEEP_S` 沿用）
- **mimo 端点**（token-plan-cn.xiaomimimo.com/v1）：**无代理**（沿 `_v4_v5_multimodel_probe.py` `B65619A07B10` L35 `use_proxy: False`）
- **teamo 端点**（api.teamorouter.cn/v1）：**必走 tun 防封号**（PI 2026-09-23 硬纪律）：
  - `http_proxy=http://127.0.0.1:1018` / `https_proxy=http://127.0.0.1:1018`
  - `all_proxy=socks5://127.0.0.1:1018`
  - 直连 = 封号风险（沿 user memory 「teamorouter/openrouter 必走 tun 代理防封号」2026-09-23）

#### 1.6.3 总预算上限

- **总 calls 上限 ≤ 720 calls**（12 cells × 60 calls/cell 硬上限；实际按需减少）
- **总 wall time 上限 ≤ 5h**（Token Plan 5h 配额硬约束；沿 L14 verdict §9.1「5h 配额撞限」先例）
- **每 cell 实际 calls 预算**：
  - L2 维度：5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell（实际可压至 20 calls / cell）
  - L14 维度：5 教师 × 2 prompts × 2 re-asks = 20 calls / cell + 3 内层重试预留 = ≤ 26 calls / cell（re-asked trace；distill + independent 沿 L14 verdict `764F24A21AC8` §4 字面，可复用前棒 N=20 数据，仅补端点 / 温度维度）
  - **每 cell 实跑上限 ≤ 26 calls**（预留 60 calls/cell 是 3 内层重试预留上限；正常 ≤ 26 calls/cell）
- **12 cells × 26 calls/cell = 312 calls 实际预计**（远低于 720 calls 硬上限）

#### 1.6.4 中断-恢复与分批拆跑方案

- **中断-恢复语义**（沿 L14 verdict §9.1 先例）：
  - 同 worker 接力棒：v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2（沿 L14 verdict §9.1）
  - checkpoint 文件：`.tmp/_t1_records.json`（沿 L14 runner `.tmp/_l14_records.json` 惯例）
  - 每 call 后 checkpoint 累积（沿 L14 runner L151-156 惯例）
  - 已跑 (teacher, caption_id, reask_idx, temp, endpoint) 元组 skip（沿 L14 runner L107-110 惯例）
- **分批拆跑**：
  - 撞 5h 配额自动恢复（worker 接力棒续跑）
  - 单批撞 600s 看门狗自动停（沿 L14 verdict §9.1 看门狗 280s 上调至 600s 沿 L2 verdict）
  - 中断-恢复同 agent 唤醒语义（worker session 不重启，沿 L14 §9.1 同棒续跑）
- **额度撞限应急**（如 12 cells 未跑完撞 5h 配额）：
  - 仅跑已启动 cells，不补未启动 cells
  - 已启动 cells 部分完成记「T1 部分完成」注记
  - 未启动 cells 留待 worker 下一棒接力

### 1.7 产物链（`_v4_supp_t1_*`，诞生即 SHA-12，派生 JSON 不合并）

> **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）；本棒产物用 `_v4_supp_t1_*` prefix 分列

- `_v4_supp_t1_executor.py`（T1 矩阵 runner + checkpoint 模式 + 端点 / 温度切换）
- `_v4_supp_t1_result.json`（12 cells 矩阵结果聚合：每 cell per teacher J 中位 + 端点 + 温度 + schema `v4_l14_n11full/2` 兼容 + 跨端点 / 跨温度 J 中位标准差）
- `_v4_supp_t1_verdict.md`（T1 探针判定：12 cells 字面 K-N11-3 实测 + K-T1-S1/S2/S3 触发判定 + 根因三分类每行附 + 不翻 L2/L14 既判声明）
- 与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律）
- **schema 兼容**：L14 维度 cell schema 沿 `v4_l14_n11full/2`（沿 L14 verdict `764F24A21AC8` §2 字面）；L2 维度 cell schema 沿 L2 verdict `E433A06E7BFB` §2 字面；T1 result JSON 中 `schema` 字段 = `"v4_t1_sensitivity/1"`（T1 探针专属 schema，与 L14 `v4_l14_n11full/2` 同级独立）

### 1.8 复用资产（0 触动既有字面）

- L2 verdict `E433A06E7BFB` + L2 result `FF7B167AE43F`（L2 维度字面源，只读复用）
- L14 verdict `764F24A21AC8` + L14 result `4C11AB9057B9`（L14 维度字面源，只读复用）
- `0A9EE16267B5` §1 K-N11-1/2/3 字面（沿用一字不动）
- `D85488A64D89` §2 L2 K-N11-N1/N2 字面（沿用一字不动）
- `21771E66AF67` `_v4_distill_min_measure.py`（L14 维度 distill 提取函数，只读复用）
- `5BA916D1DD24` `_v4_proxy_student_generators.py`（L14 维度 3 proxy 算子，只读复用）
- `B65619A07B10` `_v4_v5_multimodel_probe.py`（端点 + tun + 串行 ≥2s，只读复用）
- `C846F7FC79EE` `_track2_endpoints_probe_2026_09_23.json`（mimo / teamo 探活锚，只读复用）
- `6A2656878745` `strip_captions_22.json`（22 caption，只读复用）
- `_v4_track2_multimodel_verdict_2026_09_23.md`（6 模型补跑锚定，只读复用）

**新增条款**（仅 T1 探针新增）：
- **K-T1-S1**（温度敏感性 flip 触发线）—— 字面沿 K-N11-3 阈值 0.85 一字不动
- **K-T1-S2**（端点敏感性 flip 触发线）—— 字面沿 K-N11-3 阈值 0.85 一字不动
- **K-T1-S3**（稳健性确认线）—— 字面「全 12 cells < 0.85」系布尔条件显式化，**0 新设数值阈值**
- **TH-T1-1** = N_min per cell = 10 对/教师（T1 探针放宽；TH-17 N=20 仍为 L2/L14 既判门槛，两层并存）

### 1.9 规模档

- **M** ≤ 2-3 天 worker 接力棒（12 cells × ≤ 26 calls/cell × 2.5s 间隔 + 600s 看门狗 × 24 批 = 理论 ≤ 4h 跑完；实际预留 5h 配额撞限风险 + 中断-恢复时间 ≤ 8h wall time）
- 单 worker 接力棒即可完成；分批拆跑 ≤ 24 批；总 calls 实跑 ≈ 312 calls

### 1.10 判定

- **productive**（沿 L9 `23879B6CD1CC` §1 productive 判例 + L10 `F6FE005EE3C7` §1 productive 判例）

### 1.11 构造面 vs 真实面外推边界

- **构造面判定**（T1 探针构造面）：12 cells 中任一 cell 触发 K-T1-S1 / K-T1-S2 = 探针命中（**仅注记，不翻 L2/L14 既判**）；全 12 cells 不触发 = 探针不命中（确认稳健性）
- **真实面判定**（T1 探针真实面）：实际 mimo / teamo 端点 + temp 维度下 5 教师 J 中位实测
- **外推边界 = 端点 / 温度维度边界**（qwen t=0.7 是既定条件，方向翻转只质疑 qwen 端点的代表性而非整体判死）+ **数据规模边界**（T1 N_min=10/教师 探针放宽，与 L2/L14 既定 N=20/教师 两层并存）
- **不留假 pass**：T1 探针不命中 ≠ L2/L14 既判 PASS（K-N11-3 真证伪既判不动）
- **不留假证伪**：T1 探针命中 ≠ L2/L14 既判 FAIL（仅入稳健性存疑注记，不翻既判）

---

## §2 T1 矩阵汇总统计表

| # | 维度 | 温度 | 端点 | model_id | calls 上限 / cell | 主 kill-line | 字面源 | 阈值 |
|---|---|---|---|---|---|---|---|---|
| 1 | L2 N-11 supp 教师 J | 0.0 | mimo | mimo-v2.6-pro | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 2 | L2 N-11 supp 教师 J | 0.0 | teamo | deepseek-v4-flash | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 3 | L2 N-11 supp 教师 J | 0.3 | mimo | mimo-v2.6-pro | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 4 | L2 N-11 supp 教师 J | 0.3 | teamo | deepseek-v4-flash | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 5 | L2 N-11 supp 教师 J | 0.5 | mimo | mimo-v2.6-pro | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 6 | L2 N-11 supp 教师 J | 0.5 | teamo | deepseek-v4-flash | ≤ 26 calls | K-N11-3 → K-T1-S1 字面 | L2 verdict `E433A06E7BFB` §4.3 | K_N11_3_THRESHOLD = 0.85 |
| 7 | L14 N-11 full 三方配对 | 0.0 | mimo | mimo-v2.6-pro | ≤ 26 calls（re-asked；distill/independent 沿 L14 §4 字面可复用） | K-N11-3 → K-T1-S2 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 8 | L14 N-11 full 三方配对 | 0.0 | teamo | deepseek-v4-flash | ≤ 26 calls | K-N11-3 → K-T1-S2 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 9 | L14 N-11 full 三方配对 | 0.3 | mimo | mimo-v2.6-pro | ≤ 26 calls | K-N11-3 → K-T1-S2 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 10 | L14 N-11 full 三方配对 | 0.3 | teamo | deepseek-v4-flash | ≤ 26 calls | K-N11-3 → K-T1-S2 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 11 | L14 N-11 full 三方配对 | 0.5 | mimo | mimo-v2.6-pro | ≤ 26 calls | K-N11-3 → K-T1-S2 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |
| 12 | L14 N-11 full 三方配对 | 0.5 | teamo | deepseek-v4-flash | ≤ 26 calls | K-N11-3 → K-T1-S2 字面 | L14 verdict `764F24A21AC8` §5.3 | K_N11_3_THRESHOLD = 0.85 |

**矩阵汇总**：
- **12 cells / 总 calls ≤ 720 / 实际预计 ≤ 312**
- **既有 K-N11-1/2/3/N1/N2 字面一字不动**（沿 L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5）
- **新增 K-T1-S1/S2/S3 字面（0 新设数值阈值）**
- **qwen t=0.7 baseline 对照基线不重跑**（沿 `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 数据）
- **总判定**：T1 探针 = 稳健性辅助检验（**不翻 L2/L14 正式判定**）

---

## §3 阈值来源表（逐条注明出处件 + SHA-12）

> **铁律**：本棒 T1 探针 **0 新设数值阈值**；所有阈值字面沿既有件引用，下表逐条核对

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| **K_N11_1_DIFF** | 0.05 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-1 字面 |
| **K_N11_2_DELTA** | 0.05 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-2 字面 |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §1 K-N11-3 字面 |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面（沿字面） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §4.3 K-N11-3 字面（沿字面） |
| **K_N11_3_THRESHOLD** | 0.85 | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §5.3 K-N11-3 字面（沿字面） |
| **TH-17 N_TARGET** | 20 / 教师 | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | §2 L2 K-N11-N1 字面 |
| **TH-17 N_TARGET** | 20 / 教师 | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 L2 配置表 |
| **TH-T1-1 N_min** | 10 对/教师（T1 探针放宽） | 本棒 T1 §1.4 新立 | （本棒） | §1.4 非退化自证 + §1.8 新增条款 |
| **TH-14 5 教师锚定** | kimi / GLM_1 / GLM_2 / coze / minimax | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-14 |
| **TH-15 seed** | 42 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-15 |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §2 INTER_CALL_SLEEP_S |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 INTER_CALL_SLEEP_S |
| **teamorouter tun 代理** | `http://127.0.0.1:1018` | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | L35 tun proxy 段 |
| **teamorouter 必走 tun 防封号** | （硬纪律） | PI 2026-09-23 拍板 + user memory 2026-09-23 | — | user memory 「teamorouter/openrouter 必走 tun 代理防封号」 |
| **Jaccard 公式** | `J = |A ∩ B| / |A ∪ B|` token 级 set Jaccard | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §3.2 字面 |
| **Jaccard 公式** | `J = |A ∩ B| / |A ∪ B|` token 级 set Jaccard | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §3.2 字面 |
| **token regex** | `re.findall(r"[a-z0-9]+\|[一-鿿]", text.lower())` | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §3.2 字面 |
| **schema L14** | `v4_l14_n11full/2` | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 schema 字面 |
| **22 caption** | `strip_captions_22.json` | `corpus/v20_caption_surface/strip_captions_22.json` | `6A2656878745` | — |
| **mimo endpoint** | `token-plan-cn.xiaomimimo.com/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **mimo model_id** | `mimo-v2.6-pro` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **teamo endpoint** | `api.teamorouter.cn/v1` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **teamo model_id** | `deepseek-v4-flash` | `_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |

> **0 新设数值阈值声明**：T1 探针 **0 新设数值阈值**；K-T1-S1/S2/S3 三条均为布尔条件显式化（沿 S-40 教训），**0 新设数值**

---

## §4 边界声明（复述）

- **本稿生效即锁**（沿 `D85488A64D89` `AD42992DC75D` + L9 `23879B6CD1CC` `5C579F28634E` + L10 `F6FE005EE3C7` `16E89657DAAA` 锁先例）；**事后不重开不调**
- **本稿是预登记追加件，不是执行件**——执行由 worker 跑，判死由 verdict-keeper 裁因，证据链由 evidence-auditor 审（沿 8 agent 团队分工）
- **本稿 0 触 v0.2 本体 `D85488A64D89` + 0 触 activation `AD42992DC75D` + 0 触 L9 `23879B6CD1CC` + 0 触 L9 activation `5C579F28634E` + 0 触 L10 `F6FE005EE3C7` + 0 触 L10 activation `16E89657DAAA` + 0 触 L2 verdict `E433A06E7BFB` + 0 触 L2 result `FF7B167AE43F` + 0 触 L14 verdict `764F24A21AC8` + 0 触 L14 result `4C11AB9057B9` + 0 触 Track 2 件 `B65619A07B10` / `C846F7FC79EE` + 0 触 `21771E66AF67` + 0 触 `5BA916D1DD24` + 0 触 `6A2656878745`** —— 16 件一字不动（追加件不动既有件字面）
- **本稿 0 触 V1–V3 资产**（letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读）+ 0 触 R5 V4 frozen
- **派生 JSON 不合并**（本棒产物用 `_v4_supp_t1_*` prefix 分列，与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立）
- **R4 key 永不明文**（**无例外**）+ **R6 P-G v0/v01 不动** + **R7 plugin spec 不动**
- **§0.5 过渡声明 1 件**：**T1 稳健性探针定位过渡**（L2/L14 既定 K-N11-3 真证伪不动 + T1 探针 12 cells 跑出前不预设 PASS/FAIL 翻转）；**不动 v0.2 §0.5 既有 3 件 + L9 §0.5 既有 3 件 + L10 §0.5 既有 2 件**
- **0 触既有 K-N11-1/2/3/N1/N2 字面**（沿 `0A9EE16267B5` §1 + L2 verdict `E433A06E7BFB` §4 + L14 verdict `764F24A21AC8` §5 一字不动）
- **0 新设数值阈值**（K_N11_3_THRESHOLD = 0.85 沿字面不动；K-T1-S1/S2/S3 均为布尔条件显式化）
- **T1 定位硬约束**：稳健性辅助检验，**不翻 L2/L14 正式判定**；除 K-T1-S1/S2 命中且 verdict-keeper 裁因 + verifier 签字，**不得据此改判 L2/L14 既定结论**（沿 L2 verdict `E433A06E7BFB` §11 + L14 verdict `764F24A21AC8` §11 一字不动）

---

## §5 根因三分类 + 真受审标准（沿拍板 #15）

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
- **T1 探针根因列特别要求**：
  - **K-T1-S1 / K-T1-S2 命中** → 根因列必须区分三源（qwen 端点固有 / 教师端点固有 / 温度敏感性）；不可笼统归「敏感性成立」
  - **K-T1-S3 命中（全 12 cells 不翻转）** → 根因列必须说明「qwen t=0.7 baseline 方向稳定 + 跨 temp / 端点稳健」，**不构成 L2/L14 既判 PASS 的新证据**（仅是既判方向的稳健性确认）
  - **partial completion**（12 cells 未跑完撞 5h 配额）→ 根因列必须明示「T1 部分完成 + 缺 cells 留待 worker 接力棒」

### T1 探针与 L2/L14 既判的根因关联

| T1 探针结果 | L2/L14 既判影响 | 根因列 |
|---|---|---|
| **全 12 cells J 中位 < 0.85**（K-T1-S3 命中） | **0 影响**（L2/L14 既判不动） | qwen t=0.7 baseline 方向在 temp / 端点维度稳定；不翻既判 |
| **任一 cell J 中位 ≥ 0.85**（K-T1-S1 / K-T1-S2 命中） | **0 直接影响**（L2/L14 既判一字不动） | 仅入稳健性存疑注记（qwen 端点代表性存疑）；不翻既判 |
| **K-T1-S1 命中 + verdict-keeper 裁因 + verifier 签字** | **可能**触发 L2/L14 既判复核（不翻既判 = 默认；触发复核 = 须走完整流程） | 仅作 L2/L14 既判的复核候选；**不得直接翻判** |
| **partial completion**（撞 5h 配额） | **0 影响** | T1 部分完成注记；缺 cells 留待接力 |

> **铁律**：T1 探针字面仅入稳健性注记；**L2/L14 既判一字不动是默认状态**；**改判须走 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程**

---

## §6 自验清单（沿任务自验清单）

- [x] T1 矩阵 12 cells 全部有独立 K-* 字面（§1.5 + §2 汇总表）
- [x] 全部口径可回溯到派工单原文 + 既有预登记件 + L2/L14 verdict 字面（§1.3 claim + §3 阈值来源表）
- [x] kill-line 字面风格与既有预登记逐字对齐（K-N11-1/2/3/N1/N2 沿 `0A9EE16267B5` + L2/L14 verdict 字面；K-T1-S1/S2/S3 新增 0 新设数值）
- [x] 判定布尔显式方向（hit=True 触发 / pass=False 触发 / 方向翻转 hit=True）—— 沿 S-40 教训「禁裸 bool」
- [x] key 形态自扫 0 命中（§0 自扫结果）
- [x] 调用预算与节制硬约束写明（§1.6 单批 ≤ 30 calls / 总 ≤ 720 calls / 总 wall time ≤ 5h）
- [x] 产物链 `_v4_supp_t1_*` 命名预定（§1.7 executor / result / verdict 三件）
- [x] 阈值来源表逐条注明出处件 + SHA-12（§3 22 条阈值引用）
- [x] 不翻 L2/L14 既判硬约束声明（§0 边界 + §1.3 claim + §1.5 字面 + §4 边界 + §5 根因关联）
- [x] 派生 JSON 不合并声明（§1.7 + §4 边界）
- [x] 报告记诞生 SHA-12 + 大小（§7 报告）

---

## §7 报告（诞生即记）

- **本稿路径**：`results/_v4_supp_prereg_v02_add_T1_2026_09_24.md`
- **SHA-12 / 字节 / 行数**：见 **RESULT 报告**（harness 外部汇报段）—— 文件内嵌 hash 会触发 self-reference 递归不一致（沿既有 3 件预登记件 `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` + v0.2 + activation + L9 / L10 追加件均不自指 hash 的惯例）；本稿**生效件冻结 = 末态文件 hash**（PI 复核生效后冻结入 V4 manifest 链）；文件落地末态 hash 与大小以 RESULT 报告为准
- **锚定 v0.2 本体**：`D85488A64D89` 命中（v0.2 本体**一字不动**）
- **锚定 L9 / L10 追加件**：`23879B6CD1CC` / `F6FE005EE3C7` 命中（L9 / L10 **一字不动**）
- **锚定 L2 verdict**：`E433A06E7BFB` 命中（L2 verdict **一字不动**）
- **锚定 L14 verdict**：`764F24A21AC8` 命中（L14 verdict **一字不动**）
- **派工单**：2026-09-24 protocol-keeper follow-up 起草（PI 拍板待复核生效）
- **生效后状态**：沿 `D85488A64D89` `AD42992DC75D` 锁先例 → **生效即锁**，事后不重开不调
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（自扫沿 §0 边界声明）
- **派生 JSON 不合并声明**：本棒产物用 `_v4_supp_t1_*` prefix 分列（**line 命名建议**：`_v4_supp_t1_executor.py` + `_v4_supp_t1_result.json` + `_v4_supp_t1_verdict.md`）；与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` 同级独立
- **T1 定位硬约束再声明**：**稳健性辅助检验（sensitivity probe）**，**不翻 L2/L14 正式判定**；结论仅入稳健性注记；除 K-T1-S1/S2 命中且 verdict-keeper 裁因 + verifier 签字，**不得据此改判 L2/L14 既定结论**

---

## §8 老实交代（failures & limitations）

- skill `scientific-research-workflows:experimental-design` 本地加载器多次实录 `Local skill not found` —— **未编造 skill 不存在的虚构指令**，按既有 5 件预登记件（`D85488A64D89` + `0A9EE16267B5` + `113CBE555643` + `0A7BCA992B95` + `F6FE005EE3C7`）+ L2 verdict `E433A06E7BFB` + L14 verdict `764F24A21AC8` 字面锚执行
- **本稿 = 预登记立线件，非执行件**——执行由 worker 接力棒跑，12 cells 矩阵实跑预计 ≤ 312 calls（理论 ≤ 720 calls），撞 5h 配额分批拆跑 + 中断-恢复（沿 L14 verdict §9.1 先例）
- **T1 探针放宽 N_min = 10 对/教师**（与 L2/L14 既定 N=20/教师 两层并存；理由：T1 = 敏感性探针，方向翻转定性即可）
- **T1 探针 0 新设数值阈值**；K-T1-S1/S2/S3 均为布尔条件显式化（沿 S-40 教训）
- **T1 探针定位硬约束**：**不翻 L2/L14 正式判定**；除 K-T1-S1/S2 命中 + verdict-keeper 裁因 + verifier 签字 + PI 复核，**不得据此改判** L2/L14 既定结论一字不动
- **qwen t=0.7 baseline 不重跑**（沿 `_v4_track2_multimodel_verdict_2026_09_23.md` qwen3.7-max 数据既判，作 12 cells 比照锚）
- **本稿 0 触 16 件既有件**（v0.2 本体 + activation + L9 / L10 追加件 + activations + L2/L14 verdicts + results + Track 2 件 + 度量函数 + 22 caption —— 详见 §4 边界声明）
- **派工单「5 件必带」(agent 名 + skill 名 (sha256 611965fcb620...) + plugin 名 (@scientific-research-workflows) + 7+9 铁律 + 老实交代 0 产物) 全收**
- **skill 诚实交代**：本棒缺 skill，按既有预登记件 + L2/L14 verdict + 派工单字面执行；**未编造 skill 不存在的虚构指令**

---

## §9 SHA 漂移诚实披露（沿 E-9 / E-16 模式，立线即报）

> 本节为「**锚定 SHA 引用字面 vs 盘 SHA 漂移披露**」专项诚实交代，沿 V3 asset erratum §5 E-9 / E-16 同口径（SHA-12 漂移模式）—— 立线即报，不修任何既有件字面，仅披露漂移事实

### §9.1 L14 verdict SHA 漂移披露

- **L14 verdict `results/_v4_supp_l14_n11full_verdict.md`**：
  - **L14 verdict 自报 SHA-12（§8 §表）**：`764F24A21AC8`（19,708 B）
  - **L14 verdict 盘实测 SHA-12**：`8EEF73BF9856`（19,697 B）
  - **漂移量**：11 B + SHA 差异（SHA-12 全 12 hex 位均不同）
  - **L14 verdict 0 触动**（本棒 T1 立线件 0 写入 L14 verdict 文件）
  - **漂移源不明**（非 T1 引入；可能是 L14 棒跑后微调 / 末尾换行调整 / 编辑器自动 BOM 处理 等；**仅披露不溯因**）
- **T1 立线件字面引用沿用 L14 verdict 自报 SHA-12 = `764F24A21AC8`**（沿项目「引用锚定 SHA = 字面引用件 §0/§8 自报值」的惯例，与 v0.2 / L9 / L10 追加件引用 v0.2 `D85488A64D89` 同口径）
- **诚实原则声明**：T1 立线件**不擅自修正** L14 verdict 自报 SHA（沿「不动既有件字面」+「0 触 L2/L14 锚定字面」）；盘 SHA `8EEF73BF9856` 仅作披露，不作 T1 字面源替代

### §9.2 L2 verdict SHA 自洽披露

- **L2 verdict `results/_v4_supp_l2_n11supp_verdict.md`**：
  - **L2 verdict 自报 SHA-12（§10 表）**：`E433A06E7BFB`（15,671 B）
  - **L2 verdict 盘实测 SHA-12**：`E433A06E7BFB`（15,671 B）
  - **匹配 ✓**（SHA-12 + 字节均一致）
  - T1 立线件字面引用 `E433A06E7BFB` 一字不动

### §9.3 其他引用件 SHA 自洽披露

- **v0.2 预登记本体 `D85488A64D89`**：自报 = `D85488A64D89`（42,764 B）；盘实测 = `D85488A64D89`（42,764 B）→ **匹配 ✓**
- **v0.2 activation `AD42992DC75D`**：自报 = `AD42992DC75D`（3,202 B）；盘实测 = `AD42992DC75D`（3,202 B）→ **匹配 ✓**
- **L9 / L10 追加件**：本棒未实测（仅引用 §0 输入件 SHA-12 链字面），不引用为执行字面源；如有漂移留待后续 reconciliation
- **L9 / L10 activations**：同上

### §9.4 处置建议（不擅自处置，留 PI 裁定）

- **L14 verdict SHA 漂移**（自报 `764F24A21AC8` vs 盘 `8EEF73BF9856`）：
  - 选项 A：保留现状（不动 L14 verdict 字面；T1 字面引用沿用自报 `764F24A21AC8`；盘 SHA 漂移作已披露事实入勘误链）
  - 选项 B：L14 verdict 微调后再算 SHA-12 入锁（需 PI 授权 + 不动字面原则下可能的字节微调 / 末尾换行调整）
  - 选项 C：T1 字面源改引用盘 SHA `8EEF73BF9856`（需重新跑 `Get-FileHash` 验证 T1 §0 输入件链 + §3 阈值来源表 + §4 边界声明 三处引用值）
  - **本棒不擅自选 A/B/C** —— 留 PI 裁定（沿「不动既有件字面」+「0 擅自合并派生 JSON」+「PI 复核生效时定夺」原则）

### §9.5 漂移模式与已知 E-* 注释对齐

- **漂移模式 = SHA 漂移**（沿 E-9 `da517c1153c` 11 hex vs `da517c115f3c` 12 hex 漂移 + E-16 报告写 `da517c1153c` vs 盘实算 `da517c115f3c` 漂移）
- **L14 verdict 漂移是同一类型**（自报 vs 盘实算漂移），但本棒**不擅自判定 E-30 编号** —— E-30 编号由 evidence-auditor 在下一轮 reconciliation 时定夺
- **诚实声明**：T1 立线件字面源引用沿「字面自报 SHA」惯例；盘 SHA 漂移不阻 T1 立线件生效，但**生效件冻结时**应复核 T1 字面源 = L14 verdict 自报 SHA = `764F24A21AC8`（若届时 L14 verdict 已 reconcile 为 `8EEF73BF9856`，T1 字面源应同步 reconcile；T1 派生 JSON 不合并铁律下，T1 不与 L14 verdict 合并字面源）

### §9.6 T1 立线件 0 触发任何 SHA 漂移

- **T1 立线件 SHA 漂移自检**：T1 立线件本身不存在自报 SHA（沿既有惯例不自指 hash；§7 报告段「见 RESULT 报告」引用 harness 外部汇报段）
- **T1 立线件 0 触 16 件既有件**：v0.2 / activation / L9 / L10 + activations + L2 / L14 verdicts + results + Track 2 件 + 度量函数 + 22 caption —— 0 触动（L14 verdict 盘 SHA 漂移非 T1 引入）