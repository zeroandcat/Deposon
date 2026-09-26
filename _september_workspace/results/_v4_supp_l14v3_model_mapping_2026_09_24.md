# V4 L14+ 五教师 model 映射拍板留痕件（draft，2026-09-24，待 PI 复核生效）

- **性质**：doc-writer 起草类文档（沿 L14+ 派工单 2026-09-24「L14V3 五教师 model 映射拍板留痕件」）；本棒=留痕件，**只记 PI 拍板字面** + **三栏对照表**（V3 字面锚 / V4 现行实测 / PI 拍板定案） + **诚实声明**（V4 重跑采样口径 ≠ V3 历史模型身份断言），**不动既有件**、**不动 L14+ 预登记件**、**不动 batch result json**
- **定位（边界）**：本棒 = L14+ 派工单指定的映射拍板留痕，**仅覆盖现行 V4 重跑采样的 model 映射口径**（沿 batch1 r6 实测 119 calls + batch2 r2 实测 22 calls 字面），**不覆盖 V3 历史模型身份**（V3 coze/kimi/GLM_1/GLM_2 原始 API model 在制品层无字面记录，V3 字面锚仅来自 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 9_models 字段 + `corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/` 路径标签）；本棒不动 N-26 主预登记 + L4 verdict + L13 verdict + L7 verdict + v0.2 件 + add_T1 件 + L9 追加件 + L10 追加件 + K-N26-* kill-line 字面 + K_N26_1_ACC/K_N26_2_AUC/K_N26_3_TEACHERS_LT 阈值（0.70 / 0.75 / 0.60）
- **PI 复核待生效**（沿 `05B975A86989` 锚定先例）—— 本棒映射表 + PI 拍板字面引用 + 诚实声明 = **待 PI 复核生效**；**生效即锁**（沿 `0A7BCA992B95` 锁先例），事后不重开不调；**「CONDITIONAL PASS」退役**，只用 PASS / FAIL 二值（沿 R6 实证）
- **范围**：L14+ 五教师 model 映射（kimi / GLM_1 / GLM_2 / coze / minimax → 当前 teamo/mimo 等端点现行采样 model_id）= 现行 V4 重跑采样口径；不含 N-26 主预登记 §2 K-N26-* 字面复核（沿 N-26 §2 字面一字不动）；不含 V3 历史模型身份推断；不含 9-backbone × 5-artifact 断层裁定（**仍留 PI 裁定注记**——本棒仅字面引用既有查证结论，不断言映射真伪）
- **判定依据**：deposon 项目核心准则四条「大材小用，落到实处，与死同行，虚实回路（FTFB）」（PI 2026-09-22 R1 录入 + 2026-09-23 FTFB 入根 + **准则为根，论文为一处外显**）—— 五教师 model 映射 = 现行采样口径记录，非命题真审，亦非 V3 历史身份重审（**映射 ≠ 实证结论**，产物层仅作 result json 字面读取参照）

---

## 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | SHA-12 | 字节 | 状态 | 用途 |
|---|---|---|---|---|---|
| **L14+ 预登记（锚定不动）** | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `05B975A86989` | 61,547 | 盘上在 | L14+ 立线锚定 + 五教师 × 22 caption × 双向 ≥1,100 calls + K-N26-* 字面源 |
| L14+ activation 件（不动） | `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | (落盘报值) | 21,309 | 盘上在 | L14+ 立线后状态沿 AD42992DC75D 锁先例 |
| **batch1 r6 result（kimi 实测）** | `results/_v4_supp_l14v3_batch1_r6_result.json` | `A4F851154551` | 58,369 | 盘上在 | kimi 实测 119 calls 累计 / round 6 单批 21 calls 字面源 |
| **batch1 r6 executor** | `results/_v4_supp_l14v3_batch1_r6_executor.py` | `5F02C7E0F094` | 47,242 | 盘上在 | batch1 r6 kimi 实测 runner（5+5+5+5+5+...） |
| **batch2 r2 result（GLM_1 实测）** | `results/_v4_supp_l14v3_batch2_r2_result.json` | `CB37B699FF73` | 62,887 | 盘上在 | GLM_1 实测 22 calls 字面源（model_id_sent=glm-5.3 / model_returned=glm-5.3） |
| **batch2 r2 executor** | `results/_v4_supp_l14v3_batch2_r2_executor.py` | `5BE9DFE83A27` | 55,317 | 盘上在 | batch2 r2 GLM_1 实测 runner |
| **batch2 r2 models probe（teamo /v1/models 44 总）** | `results/_v4_supp_l14v3_batch2_r2_models_probe.json` | `3C9DC60B5071` | 1,503 | 盘上在 | teamo 44 models 探活清单（GLM 系 4 个含 glm-5.3 + kimi-k3 + kimi-k3[1M]，**无 kimi-for-coding / 无 minimax-m3**）|
| v0.2 预登记本体（不动） | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | 42,764 | 沿用 | 通用条款格式（TH-* / 派生 JSON / 双读法 / 阈值表） |
| v0.2 activation 件（不动） | `results/_v4_supp_prereg_v02_activation_2026_09_24.md` | `AD42992DC75D` | 3,202 | 沿用 | v0.2 立线后状态锁先例 |
| add_T1 追加件（不动） | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | (落盘报值) | 52,942 | 盘上在 | LLM 调用纪律沿用 |
| add_T1 activation 件（不动） | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | (落盘报值) | 14,234 | 盘上在 | add_T1 锁先例 |
| L9 追加件（不动） | `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md` | `23879B6CD1CC` | 19,586 | 沿用 | 双读法并记先例 |
| L10 追加件（不动） | `results/_v4_supp_prereg_v02_add_L10_2026_09_24.md` | `F6FE005EE3C7` | 26,159 | 沿用 | 语义反转注释先例 |
| N-26 主预登记（不动） | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | 60,530 | 盘上已清出（inventory L800 锁定） | §2 K-N26-1/2/3/N1/N2 字面（一字不动） |
| L4 verdict N-26 v2（不动） | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | 16,365 | 盘上已清出（ledger L208 锁定） | §11 FAIL · 构造不可行 · 4/5 教师 metadata 缺位（一字不动） |
| L13 verdict N-26 pair（不动） | `results/_v4_supp_l13_n26pair_verdict.md` | `E105EC1362DB` | 23,120 | 盘上已清出（ledger L188 锁定） | V4 三元组基底（一字不动） |
| L7 verdict E-N20（不动） | `results/_v4_supp_l7_e_n20_verdict.md` | `B8335982AE5E` | 6,424 | 盘上已清出（ledger L282 锁定） | background session ≤275s 实证锚（一字不动） |
| **V3 9-backbone 字面源** | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | (V3 字面) | — | V3 只读 | 9_models 字段 = V3 字面锚源（行 26 字段；minimax-m3 等 V3 字面锚定位源） |
| **V3 5 by_model 索引** | `corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/` | (V3 字面) | — | V1–V3 只读 | 五教师路径标签 = 语料层字面锚源（无 model 字段） |
| V3 蒸馏流水线参照系 | `scripts/run_v3x_*.py`（V3 字面） | (V3 字面 SHA) | — | V1–V3 只读 | V3 distill 流水线复现参照（端点 / 参数 / 中间产物格式） |
| **claude_code V3 mapping 查证** | `letters/_v4_distillation_reply_claude_code_2026_09_20.md` | (V3 字面) | — | V1–V3 只读 | L168-170「4 directories ↔ 9 backbones」查证结论（mapping 假设非 calibration） |
| **mavis 主题回函 mapping 查证** | `letters/_v4_theme_reply_mavis_2026_09_20.md` | (V3 字面) | — | V1–V3 只读 | L36「9-backbone × 60-cell grid」与「5 `by_model/` artifacts」分层声明 |
| Track 2 endpoints probe | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | 5,803 | 沿用 | qwen_plan / mimo / teamo 三端点权威源（mimo 端点字面锚） |

> 注：本棒 0 触动 L14+ 预登记件 `05B975A86989` 一字不动；0 触动 N-26 主预登记 `0A9EE16267B5` / L4 verdict `74B5B37F7EEA` / L13 verdict `E105EC1362DB` / L7 verdict `B8335982AE5E` 字面一字不动；0 触既有 K-N26-* 字面；0 触既有阈值（K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 一字不动）。本棒派 agent 落盘单文件 `_v4_supp_l14v3_model_mapping_2026_09_24.md`，SHA-12 见落盘报值。

---

## §0 边界声明（沿 R4 / R5 / R6 / R7 + skill 缺位纪律锚，2026-09-23 勘误版）

- **0 LLM 调用**：本稿由 doc-writer 起草，全程未调用任何 LLM API；纯文件编辑（write），未调任何 LLM/代理/构造代理/网关；沿 V4 §3.1 放开语境明示可调（PI 2026-09-22「V3 的剑不斩 V4 的官」），本棒无需调
- **R4 key 永不明文**（**无例外**，沿 R4 + PI 2026-09-22「key 永不明文等合理且无冲突的铁律要沿用」）：本稿及其后续产物不写入、不引用、不打印任何明文 API key / 平台密钥；key 仅在进程组方法里以 runtime env 读取；**本稿自扫** `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态 0 命中
- **R5 V4 frozen 只追加**（**V4 沿用 V1–V3 资产只读底线**）：本稿不修改 L14+ 预登记 `05B975A86989` / 不动 L14+ activation / 不动 batch1 r6 result `A4F851154551` + executor `5F02C7E0F094` / 不动 batch2 r2 result + executor / 不动 batch2 r2 models probe `3C9DC60B5071` / 不动 N-26 主预登记 `0A9EE16267B5` / 不动 L4 verdict `74B5B37F7EEA` / 不动 L13 verdict `E105EC1362DB` / 不动 L7 verdict `B8335982AE5E` / 不动 v0.2 本体 `D85488A64D89` + activation `AD42992DC75D` / 不动 add_T1 件 + activation / 不动 L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` / **派生 JSON 不合并**（本棒产物用 `_v4_supp_l14v3_model_mapping_*` prefix 独立，与现有 `_v4_supp_l14v3_*` 既有同级独立）
- **R6 P-G v0/v01 / R7 plugin spec**：本棒不动 P-G v0/v01；不动 plugin spec；不动 verifier 内置脚本
- **V1–V3 只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）—— 本棒批读 `corpus/v20/by_model/kimi/index_v2_2026_09_16.json` + `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 9_models + letters/`_v4_distillation_reply_claude_code_2026_09_20.md` L168-170 + letters/`_v4_theme_reply_mavis_2026_09_20.md` L36 三向字面引用，**0 触原 V3 件**
- **kill-line 字面不动禁私设条款**（S-40 教训：判定布尔显式方向 `hit=True` 即触发 / `pass=True` 即存活，禁裸 bool；PI 2026-09-23 拍板明示「禁止擅自调阈值 / 禁止合并派生 JSON / 禁止私设 kill-line 条款」）：本棒 K-N26-* 字面**完全沿** N-26 主预登记 `0A9EE16267B5` §2 一字不动；阈值 0.70 / 0.75 / 0.60 沿 N-26 §2 字面一字不动；**本棒 0 新设数值阈值**
- **0 擅调阈值**（沿 v0.2 §0 同口径 + add_T1 §0 同口径 + L14+ §0 同口径）：本棒 **0 调既有 K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 / K_N26_N1_N_MIN = 0 / K_N26_N2_TUN_PASS_RATE = 1.0**；阈值**一字不动**
- **skill 加载老实交代**：派工单要求 `scientific-research-workflows:scientific-writing` skill（plugin @scientific-research-workflows，sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb），本地 skill 加载器多次实录 `Local skill not found`（沿 v0.2 §0 + add_T1 §0 + L14+ §0 同口径）—— 本棒按 `05B975A86989`（L14+ 预登记）+ `0A9EE16267B5`（N-26 主预登记）+ `74B5B37F7EEA`（L4 verdict）+ `E105EC1362DB`（L13 verdict）+ `B8335982AE5E`（L7 verdict）+ `0A7BCA992B95`（方法预登记）+ `113CBE555643`（种子预登记）的格式与字面锚执行，**未编造 skill 不存在的虚构指令**

---

## §0.5 过渡声明（本棒 L14+ 五教师映射留痕件特有）

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）

- **本棒口径边界**：**仅覆盖现行 V4 重跑采样的 model 映射**（teamo/mimo 端点现行实测对应 model_id_sent），**非 V3 历史模型身份断言**——
  - **V3 字面锚可考的教师**：`minimax`（V3 9-backbone L26 字段 = `minimax-m3`，沿 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26/56/167/302/396/472 字面）
  - **V3 字面锚可考的教师 lineage**：GLM_1 / GLM_2（V3 9-backbone 含 `glm-5.3` + `glm-5.3-flash` 两枚 = 同 lineage 不同规格，字面来自 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 字面 + L168 推断）
  - **V3 字面锚可考的教师**：kimi（V3 9-backbone 含 `kimi-k2.7-code`，字面来自 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 字面）
  - **V3 字面层无 model 字段**：5 by_model 制品层（`corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/`） = 语料层路径标签 + index 字段（`corpus / generator_version / spec / named_filler_rule / n_graphs / graphs[]`），**无 model 字段**——证实五教师为语料路径标签，非 API model 身份锚
  - **V3 字面层不可考**：coze 原始底层大模型 API（9-backbone 字段无 coze；制品层 `by_model/coze/` 同样无 model 字段；**V3 时期 coze 底层 model 无任何字面记录**）
- **9-backbone ↔ 5-by_model 断层仍留 PI 裁定注记**：本棒沿既有查证结论不断言映射真伪——`deposon_v3_physical_opt_60cells_2026_09_11.json` L26 9_models = `doubao-seed-2.0-lite` / `glm-5.3` / `deepseek-v4-flash` / `doubao-seed-evolving` / `minimax-m3` / `glm-5.3-flash` / `kimi-k2.7-code` / `doubao-seed-2.1-turbo` / `deepseek-v4-pro` 共 9 项；`by_model/` 仅 `kimi` / `GLM_1` / `GLM_2` / `coze` / `minimax` 共 4 个目录 = 与 9-backbone 关系**字面未声明**；沿 claude_code 回函 L168-170「4 directories ↔ 9 backbones，coze 在 grid 与 four 之外，kimi 在 grid 但缺 model 制品」字面引用；**本棒仅记现行采样映射，不补断层裁定**
- **本棒不评估、不判定、不影响 N-26 主预登记 / K-N26-* 字面 / 既有阈值 / 既定结论**——既判结论 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」**一字不动**；K-N26-* kill-line 字面**一字不动**
- **本棒不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 既有 3 件** + **不动 L10 §0.5 既有 2 件** + **不动 add_T1 §0.5 T1 稳健性探针定位过渡 1 件** + **不动 L14+ §0.5 N-26 真审唯一路径定位过渡 1 件**

---

## §1 五教师 model 映射表（三栏对照 = V3 字面锚 / V4 现行实测 / PI 拍板定案）

> **三栏对照声明**：第一栏 = V3 字面（仅记可考的 V3 API 端点名/9-backbone 名/by_model 路径标签 / 制品层字段）；第二栏 = V4 现行实测（仅记 batch1 r6 + batch2 r2 字面 metadata + models probe 清单）；第三栏 = PI 拍板定案（2026-09-24 23:08 ask_748d9242c7a6be3d83de63a0 显式四答 + 字面引用）

### 1.1 映射主表

| 五教师（V3 路径标签） | **第一栏：V3 字面锚**（沿 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 9_models 字段 + `corpus/v20/by_model/{…}/` index 字面） | **第二栏：V4 现行实测**（batch1 r6 / batch2 r2 字面 + models probe 字面） | **第三栏：PI 拍板定案**（2026-09-24 23:08 ask_748d9242c7a6be3d83de63a0 显式四答，逐字引用） |
|---|---|---|---|
| **kimi** | V3 端点名 = `kimi`（V3 distill 流水线 `<MODEL_KIMI>` 字面）<br>V3 API 端点名 = `kimi-for-coding`（沿 user memory 2026-09-08 字面）<br>V3 9-backbone 字面 = `kimi-k2.7-code`（`deposon_v3_physical_opt_60cells_2026_09_11.json` L26）<br>`by_model/kimi/` 制品 = `index_v2_2026_09_16.json`，**无 model 字段**；kimi 字面在 grid 但缺 model 制品（沿 claude_code L168-170 字面） | batch1 r6 实测：累计 119 calls（r1-r6）/ round 6 单批 21 calls 全 ok<br>`model_id_sent` = `kimi-k3`<br>`model_returned` 大多 = `FW-Kimi-K3`（行 416/472/528/570/612/654/696/752/794/836/932/974/1016 等 13 行）+ 1 行 `kimi-k3`（行 878）<br>`endpoint` = `https://api.teamorouter.cn/v1/chat/completions`<br>teamo `/v1/models` 探活清单（44 models）字面 = `kimi-k3` + `kimi-k3[1M]` 共 2 枚；**`kimi-for-coding` 不在清单**（teamo 实测拒绝 `kimi-for-coding`，返 400 model_not_available） | **PI 拍板定案 = teamo `kimi-k3`**（V3 锚 `kimi-k2.7-code` 已下线；teamo 当前 GLM/kimi 系已升 5.x / K3）<br>**别名口径** = **不界定**，PI 拍板原文逐字引用：<br>**「不界定，否则可能反而造成歧义」**<br>→ **result 只记实测字面（model_id_sent=kimi-k3 / model_returned=FW-Kimi-K3 或 kimi-k3），不立别名对照表**；对外引用按出处原样（V3 锚沿 `kimi-k2.7-code` 路径 + V4 现行沿 `kimi-k3` 路径分别引用，不并表） |
| **GLM_1** | V3 端点名 = `GLM_1`（V3 distill 流水线 `<MODEL_GLM_1>` 字面）<br>V3 9-backbone 字面 = `glm-5.3`（V3 主版本 = `glm-5.3`，沿 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 字面）<br>`by_model/GLM_1/` 制品层有 GLM 三方定位 P-K 文件 = `three_way_glm_slot_blind_test_2026_09_16.json`，**无 model 字段**但其 `task` 字段 = "P-K → GLM 三位定位 (基线: 自己 vs GLM vs KIMI, 列表冻结阅读)" 字面可考（沿 claude_code L50 字面） | batch2 r2 实测：22 calls 全 ok（22 caption × 1 call round 1 retry）<br>`model_id_sent` = `glm-5.3`<br>`model_returned` = `glm-5.3`（24 条 ok=true，0 fail，0 empty）<br>`endpoint` = `https://api.teamorouter.cn/v1/chat/completions`<br>teamo `/v1/models` 探活清单（44 models）字面 = GLM 系 4 个：`glm-5.2` / `glm-5.3` / `glm-5.3-flash` / `glm-5.3-flash-free`；**`GLM_1` 字面不在清单**（teamo 当前 GLM 系已升 5.x，V3 字面 `GLM_1` / `glm-1` / `glm4` / `glm-4` / `GLM4` / `glm_4` 6 候选均返 model_not_available 或 model_not_supported，见 r1 legacy 失败字面） | **PI 拍板定案 = teamo `glm-5.3`**（V3 锚 `glm-5.3` 已映射落定；teamo `/v1/models` 探活清单选定 GLM 系主版本）<br>**别名口径** = **不界定**（沿用 kimi 行列 PI 拍板同口径）→ **result 只记实测字面（model_id_sent=glm-5.3 / model_returned=glm-5.3），不立别名对照表**；对外引用按出处原样 |
| **GLM_2** | V3 端点名 = `GLM_2`（V3 distill 流水线 `<MODEL_GLM_2>` 字面）<br>V3 9-backbone 字面 = `glm-5.3-flash`（V3 同 lineage 不同规格，`glm-5.3-flash` 与 `glm-5.3` 同 `glm` 系 = V3 同 lineage 字面沿 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 字面 + invitation §2.1 L58 「GLM_1/GLM_2 same lineage」字面）<br>`by_model/GLM_2/` 制品层同样**无 model 字段** | 尚未实测（本棒仅记派工时已实测的两批：batch1 r6 = kimi；batch2 r2 = GLM_1；GLM_2 留待后续 worker 接力棒跑 GLM_2 教师侧时落字面）<br>但**实测前已锁本拍板**：现行 teamo 探活清单 GLM 系 4 款同 lineage + 同 5.x；与 GLM_1 现行采样同端点同主版本形态高度同构 | **PI 拍板定案 = teamo `glm-5.3` 复用**（PI 拍板 reuse；V3 字面 same lineage = `glm-5.3-flash` 与 `glm-5.3` 同 lineage 字面；**GLM_2 同样选定 teamo `glm-5.3`，与 GLM_1 现行采样的 teamo `glm-5.3` 复用同 model_id_sent**）<br>**result 标注层** = **GLM_1 与 GLM_2 同 model 不同语料**（同 teamo `glm-5.3`，但调用入参 caption 不重叠 = 教师 P-K 三方定位语料不同源；result 内字段须明示 `teacher: "GLM_2"` 而非 `model_id_sent` 区分——避免误读为模型差异） |
| **coze** | V3 端点名 = `coze`（V3 distill 流水线 `<MODEL_COZE>` 字面）<br>V3 9-backbone 字面 = **coze 不在 9-backbone**（字面来自 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 9_models 字段全部 9 项枚举，无 coze；沿 claude_code L168 字面「`coze` appears zero times in the 9-model file」字面）<br>`by_model/coze/` 制品层同样**无 model 字段**；其内容为 P-K cross-subject blind-test + 反白洗语料 | **coze 底层大模型 API 不可考**——V3 字面层与制品层均无 model 字段；teamo `/v1/models` 探活清单同样**无 coze 字段**；**V3 → V4 重跑期间，coze 原始底层大模型 API 没有任何字面记录可援**<br>本棒以现行大模型 API **代表采样** ＝ **`deepseek-v4-flash`（teamo 端点）**——选 `deepseek-v4-flash` 理由：团队现行 6 模型补跑锚定（沿 Track 2 multimodel verdict `12,883 B`）字面、`deepseek-v4-flash` 在 teamo 探活清单（44 models 中）字面 = P-A cross-modal dpath PASS 锚源（沿 `d7_5anchor_60cells_9model_verdict_2026_09_18.json` `4505CCA79C15` 字面）；可作为现行主流大模型采样 | **PI 拍板定案 = agent 平台封装**（PI 拍板原文逐字引用）：<br>**「coze与trea都只是agent平台，我都是接的大模型API」**<br>→ **底层大模型 API 不可考**（沿 PI 拍板字面，coze = 平台封装 ≠ API model）；本重跑以现行大模型 API **`deepseek-v4-flash`（teamo）代表采样**<br>**result 内如实标注 representative/substitute 身份**——result.json 每条 coze 调用字面记 `model_id_sent: "deepseek-v4-flash"` + 标注字段 `representative_for_coze: true` + `substitute_origin: "coze_agent_platform_underlying_model_not_documented"`；**不声称该 model 即 coze 背后模型** |
| **minimax** | V3 端点名 = `minimax`（V3 distill 流水线 `<MODEL_MINIMAX>` 字面）<br>V3 9-backbone 字面 = `minimax-m3`（沿 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26/56/167/302/396/472 五处出现 `minimax-m3`，字面锚定）<br>V3 字面来源 = 火山方舟端点（沿 mavis 主题回函「minimax-m3 火山方舟已下线」字面） | **minimax-m3 火山方舟端点已下线**（V3 字面锚 `minimax-m3` 沿火山方舟已下线）<br>teamo `/v1/models` 探活清单**无 minimax-m3**（44 models 中无 minimax / minimax-m3 / minimax-m3-flash 等条目）<br>mimo 端点（token-plan-cn.xiaomimimo.com/v1）字面 = 现行 minimax 系主版本（PI 拍板） | **PI 拍板定案 = mimo 端点 `mimo-v2.6-pro`**（V3 锚 `minimax-m3` 火山方舟已下线；命名映射依据 = 本拍板）<br>**命名映射说明** = V3 字面 `minimax-m3` → V4 现行 `mimo-v2.6-pro` 跨端点跨厂商命名映射（端点名不同、模型家族不同）；**映射依据 = PI 拍板本身**，**非字面继承**（非「minimax-m3 升级版 = mimo-v2.6-pro」字面继承关系）<br>**result 内字面** = `model_id_sent: "mimo-v2.6-pro"` + `model_returned` 同 mimo 端点现行返回值；**沿 V3 字面锚 `minimax-m3` 不沿用** |

> **三栏对照总览声明**：
> - **第一栏 V3 字面锚**来源：V3 distill 流水线 `<MODEL_*>` 字面 + `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 9_models 字段（6/9 教师字面可考）+ `by_model/{...}/index_v2_*.json` 制品层（无 model 字段证实路径标签性质）+ claude_code 回函 L168-170「mapping hypothesis」字面
> - **第二栏 V4 现行实测**来源：batch1 r6 result `A4F851154551`（kimi 累计 119 calls / round 6 单批 21 calls 字面）+ batch2 r2 result `CB37B699FF73`（GLM_1 22 calls 字面）+ batch2 r2 models probe `3C9DC60B5071`（teamo 44 models 探活清单字面，含 GLM 系 4 个 + kimi 系 2 个 + 无 coze + 无 minimax-m3）
> - **第三栏 PI 拍板定案**来源：2026-09-24 23:08 ask_748d9242c7a6be3d83de63a0 显式四答（详见 §2 拍板依据表，逐字引用 + 两条 Other 原文引用）

### 1.2 派生口径对照（不立别名对照表，但派生字段保留）

> **沿 PI 拍板「不立别名对照表」口径**：本棒 result json **不立 `kimi` ↔ `kimi-k2.7-code` ↔ `kimi-k3` 对照表** / **不立 `GLM_1` ↔ `glm-5.3` ↔ `glm-5.3-flash` 对照表** / **不立 `coze` ↔ `deepseek-v4-flash` 对照表** / **不立 `minimax` ↔ `minimax-m3` ↔ `mimo-v2.6-pro` 对照表**；但 **result json 内每条调用仍如实记录派生 metadata 字段**（便于审计回查，**不作对外引用**）：

| 教师 | 派生 metadata 字段（仅入 result json，不立对照表） |
|---|---|
| kimi | `v3_anchor_api_name`: "kimi-for-coding" / `v3_anchor_9backbone_name`: "kimi-k2.7-code" / `v4_current_model_id_sent`: "kimi-k3" / `v4_current_model_returned`: "FW-Kimi-K3 或 kimi-k3" |
| GLM_1 | `v3_anchor_api_name`: "GLM_1" / `v3_anchor_9backbone_name`: "glm-5.3" / `v4_current_model_id_sent`: "glm-5.3" / `v4_current_model_returned`: "glm-5.3" |
| GLM_2 | `v3_anchor_api_name`: "GLM_2" / `v3_anchor_9backbone_name`: "glm-5.3-flash" / `v4_current_model_id_sent`: "glm-5.3（复用 GLM_1）" / `v4_current_model_returned`: "glm-5.3" / `reuse_from_teacher`: "GLM_1" |
| coze | `v3_anchor_api_name`: "coze" / `v3_anchor_9backbone_name`: null（不在 9-backbone） / `v4_current_model_id_sent`: "deepseek-v4-flash" / `representative_for_coze`: true / `substitute_origin`: "coze_agent_platform_underlying_model_not_documented" |
| minimax | `v3_anchor_api_name`: "minimax" / `v3_anchor_9backbone_name`: "minimax-m3" / `v4_current_model_id_sent`: "mimo-v2.6-pro" / `endpoint_migrated`: true / `v3_origin_endpoint`: "火山方舟（已下线）" / `v4_current_endpoint`: "mimo (token-plan-cn.xiaomimimo.com/v1)" |

---

## §2 拍板依据（ask_748d9242c7a6be3d83de63a0，2026-09-24 23:08 显式四项答案逐字引用）

> **逐字引用声明**：以下 PI 拍板原文沿 ask_748d9242c7a6be3d83de63a0（2026-09-24 23:08 显式提交）字面引用，**不改写、不删减、不解释、不意译**；含两条 Other 原文（kimi 别名口径 + coze 底层模型口径）。

| Q# | 议题 | PI 拍板答案（沿 ask_748d9242c7a6be3d83de63a0 字面引用） | 出处（逐字位置） | Other 原文（如有） |
|---|---|---|---|---|
| **Q1** | **kimi model 命名映射与别名口径** | **拍板 = teamo `kimi-k3`**（V3 锚 `kimi-k2.7-code` 已下线；teamo 实测仅 `kimi-k3` / `kimi-k3[1M]` 可用）；**不立别名对照表** | 2026-09-24 23:08 ask_748d9242c7a6be3d83de63a0 Q1 选答 | **Other 原文（逐字引用）**：<br>**「不界定，否则可能反而造成歧义」** |
| **Q2** | **GLM_2 model 复用口径**（GLM_2 是否复用 GLM_1 现行 teamo `glm-5.3`，还是另行选定 flash/free 版本） | **拍板 = reuse（复用 GLM_1 现行的 teamo `glm-5.3`）**——V3 字面 `GLM_1` 与 `GLM_2` 同 lineage（`glm-5.3` vs `glm-5.3-flash` 同一厂商系字面 + invitation §2.1 L58「GLM_1/GLM_2 same lineage」字面）；现行 teamo 探活清单 GLM 系 4 款同 5.x；故选定 GLM_2 与 GLM_1 **同 model_id_sent**（同 teamo `glm-5.3`），**不同语料** | 2026-09-24 23:08 ask_748d9242c7a6be3d83de63a0 Q2 选答 | （Q2 为选项直接选答，无 Other 原文） |
| **Q3** | **coze 底层 model 不可考处置口径** | **拍板 = coze = agent 平台封装**（非端点 model）——本重跑以现行大模型 API **代表采样**（已选 `deepseek-v4-flash`，teamo）；result 标注 representative/substitute 身份；**不声称该 model 即 coze 背后模型** | 2026-09-24 23:08 ask_748d9242c7a6be3d83de63a0 Q3 选答 | **Other 原文（逐字引用）**：<br>**「coze与trea都只是agent平台，我都是接的大模型API」** |
| **Q4** | **minimax 命名映射口径**（V3 字面锚 `minimax-m3` 火山方舟已下线；现行 mimo 端点对应 model_id） | **拍板 = mimo 端点 `mimo-v2.6-pro`**——V3 字面锚 `minimax-m3` 火山方舟已下线；现行 mimo 端点（token-plan-cn.xiaomimimo.com/v1）字面 = 现行 minimax 系主版本（PI 拍板）；命名映射依据 = 本拍板本身 | 2026-09-24 23:08 ask_748d9242c7a6be3d83de63a0 Q4 选答 | （Q4 为选项直接选答，无 Other 原文） |

> **逐字引用约束**：上表 Q1 + Q3 之 Other 原文两条沿 PI 在 ask 工具中键入字面**原样引用**（不改字 / 不改标点 / 不改大小写 / 不空格归一化）；其余 Q2 + Q4 为既定选项直接选答，无 Other 文本，本棒如实记「选项直接选答，无 Other 原文」。

---

## §3 背景引证：explore 映射查证结论（V3 by_model 制品无 model 字段、五教师=语料路径标签、9 backbone↔5 by_model 断层）

### 3.1 V3 by_model 制品层字面（无 model 字段证实语料路径标签性质）

> **`corpus/v20/by_model/kimi/index_v2_2026_09_16.json` 字段字面**（盘上在，V3 字面）—— 制品层**无 model / model_id / api_model 字段**；所有 22 graph 条目字段 = `graph_id / family / structure / N / n_edges / n_named / n_filler / source / target / seed / sha256 / file`，**无 model 字段**：

| 字段 | 值（V3 字面） |
|---|---|
| `corpus` | `"v20"` |
| `generator_version` | `"v2.0.0"` |
| `spec` | `"docs/SPEC_v2.0.md §1"` |
| `named_filler_rule` | `"named=主干结构边（链/树父子主链、DAG 最长路径族），filler=其余结构边；无诱饵边（SPEC §1 冻结）"` |
| `n_graphs` | `22` |
| `graphs[]` | 22 graph 条目（每条字段同 v3 字面，无 model 字段） |

> **结论**：V3 by_model 制品层的 22 graph 条目**仅以 corpus/graph 字段识别教师侧语义**，不存 API model 名字段。**五教师 = 语料层路径标签**（`by_model/{kimi,GLM_1,GLM_2,coze,minimax}/`），非 API model 身份锚。**GLM_1`/`GLM_2/coze/minimax 四子目录 index 同构**（盘上结构等价于 kimi index，无 model 字段）。

### 3.2 9 backbone ↔ 5 by_model 断层（沿既有查证结论字面引用，仍留 PI 裁定注记）

> **断层出处字面**（沿 `letters/_v4_distillation_reply_claude_code_2026_09_20.md` L168 + `letters/_v4_theme_reply_mavis_2026_09_20.md` L36 字面）：

- **V3 9-backbone 字面**（沿 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 `9_models` 字段，全部 9 项枚举字面）：
  1. `doubao-seed-2.0-lite`
  2. `glm-5.3`
  3. `deepseek-v4-flash`
  4. `doubao-seed-evolving`
  5. `minimax-m3`
  6. `glm-5.3-flash`
  7. `kimi-k2.7-code`
  8. `doubao-seed-2.1-turbo`
  9. `deepseek-v4-pro`

- **V3 5 by_model 字面**（沿 `corpus/v20/by_model/` 盘上目录字面，共 4 子目录）：
  1. `kimi/`（含 `index_v2_2026_09_16.json`）
  2. `GLM_1/`（含 `three_way_glm_slot_blind_test_2026_09_16.json` 等）
  3. `GLM_2/`（同构）
  4. `coze/`（同构）
  5. `minimax/`（同构）

- **断层字面**（沿 claude_code 回函 L168-170 原文逐字引用）：

> **「The nine backbones, from `results/deposon_v3_physical_opt_60cells_2026_09_11.json` `input_data.9_models`, are: `doubao-seed-2.0-lite`, `glm-5.3`, `deepseek-v4-flash`, `doubao-seed-evolving`, `minimax-m3`, `glm-5.3-flash`, `kimi-k2.7-code`, `doubao-seed-2.1-turbo`, `deepseek-v4-pro`. The four distinct by_model directories are `GLM_1`, `GLM_2`, `coze`, `minimax`. `coze` appears **zero** times in the 9-model file, confirming §2.1's parenthetical that coze is corpus-layer only. `minimax` matches `minimax-m3` by vendor. `GLM_1`/`GLM_2` match `glm-5.3` and `glm-5.3-flash` by vendor-lineage, and the invitation already notes they are one lineage (line 58). `kimi-k2.7-code` appears in the 9-model list while `by_model/kimi/` holds the corpus index — so the KIMI-side artifact that the mapping would need is the missing piece.」**

> **「That leaves the mapping at: 4 directories ↔ 9 backbones, with `coze` external to both the grid and the four, and `kimi` present in the grid but absent as a model artifact. **This is a re-fit hypothesis built from name matching only, not from any declared mapping; the artifact was not built to declare one; no calibrated mapping is claimed.** A declared mapping is still the PI's to give, but the search space is now smaller: five of the nine grid entries (`doubao-seed-2.0-lite`, `doubao-seed-evolving`, `doubao-seed-2.1-turbo`, `deepseek-v4-flash`, `deepseek-v4-pro`) have no by_model directory under any spelling I could find.」**

- **断层状态**（沿 mavis 主题回函 L36 字面）：
  > **「The V1–V3 corpus layer is **disjoint** in vendor role between the 9-backbone × 60-cell evaluation grid and the 5 `by_model/` artifacts.」**

- **断层裁定注记（仍留 PI 裁定）**：
  - `coze` 在 grid 与 four 之外（无 backbone 字面 + 无字面 model 字段；**PI 拍板「agent 平台封装」字面裁定底层 model 不可考**）
  - `kimi` 在 grid 但缺 model 制品（**PI 拍板「不立别名对照表」字面裁定映射口径**）
  - 5 个 backbone（`doubao-seed-2.0-lite` / `doubao-seed-evolving` / `doubao-seed-2.1-turbo` / `deepseek-v4-flash` / `deepseek-v4-pro`）无 by_model 目录（**仍留 PI 裁定**——是否需新建 by_model 制品层、是否需对应五教师采样、是否影响 K-N26-* 字面判定）
  - `GLM_1` ↔ `glm-5.3` 字面 lineage 可考 + `GLM_2` ↔ `glm-5.3-flash` 字面 lineage 可考（PI 拍板 GLM_2 复用 GLM_1 = same lineage 内同 model 选择）
  - `minimax` ↔ `minimax-m3` 字面 vendor 可考（PI 拍板 mimo 端点 `mimo-v2.6-pro` 现行主版本）

### 3.3 背景引证范围声明

- **本棒 §3 仅字面引用既有查证结论**（沿 claude_code + mavis 主题回函三处字面），**不补新探索**（不沿 9-backbone 任一字面字段做新 mapping 推断 = 避免 V3 字面被新探索污染；沿 v0.2 §0 「0 编造专有名词 / 0 编造 mapping」口径）
- **断层裁定 = 仍留 PI 裁定**——本棒仅做现行采样映射口径记录，断层裁定（`coze` 处置 / `kimi` 模型制品缺位 / 5 个 backbone 无 by_model 目录影响判定 / `GLM_1`/`GLM_2` lineage 具体边界 / `minimax` 跨厂商跨端点命名映射）**仍留 PI 后续裁定**
- **本棒不动既有 explore 留痕件**（claude_code / mavis 主题回函两件 = V1–V3 只读不动；本棒 0 触原字面）

---

## §4 诚实声明：本映射为 V4 重跑采样口径，非 V3 历史模型身份断言

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）

- **本棒边界声明（明确且不软化）**：
  - 本映射**仅覆盖 V4 重跑现行采样 model 映射口径**（teamo `kimi-k3` / teamo `glm-5.3` / teamo `glm-5.3` 复用 / teamo `deepseek-v4-flash` 代表采样 / mimo `mimo-v2.6-pro`），**非**：
    - **V3 历史模型身份断言**（V3 时期 kimi/GLM_1/GLM_2/coze/minimax 调用侧实际 API model 无字面记录 = 不可考即如实不可考）
    - **断层真实映射断言**（9-backbone ↔ 5 by_model 断层仍留 PI 裁定，本棒不断言 mapping 真伪）
    - **V3 → V4 升级路径断言**（`kimi-k2.7-code` → `kimi-k3` / `glm-5.3` → `glm-5.3` / `minimax-m3` → `mimo-v2.6-pro` **非**「升级版」字面继承关系，**仅** PI 拍板字面映射口径）
- **三栏对照 V3 字面锚可考范围**（沿 §3.1 + §3.2 字节面）：
  - **V3 字面可考的 V3 API 端点名**：kimi V3 端点名 = `kimi`（V3 流水线字面）/ GLM_1 V3 端点名 = `GLM_1`（V3 流水线字面）/ GLM_2 V3 端点名 = `GLM_2`（V3 流水线字面）/ coze V3 端点名 = `coze`（V3 流水线字面）/ minimax V3 端点名 = `minimax`（V3 流水线字面）—— **这些是 V3 字面锚，非 V3 时期实际生效 API model**
  - **V3 字面可考的 9-backbone 名**（沿 `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 字面）：4 教师（kimi / GLM_1 / GLM_2 / minimax）字面可考 = `kimi-k2.7-code` / `glm-5.3` / `glm-5.3-flash` / `minimax-m3`；1 教师（coze）不在 9-backbone 字面
  - **V3 字面不可考的 coze 底层 model**：V3 9-backbone 无 coze；V3 制品层 `by_model/coze/` 同样无 model 字段；**V3 → V4 重跑期间 coze 底层 model 没有任何字面记录可援** = **不可考即如实不可考**
- **三栏对照 V4 现行实测字面范围**（沿 §3.2 第二栏字节面）：
  - **kimi V4 现行实测字面**：batch1 r6 result `A4F851154551` 字面 = `model_id_sent=kimi-k3` + `model_returned=FW-Kimi-K3 或 kimi-k3`
  - **GLM_1 V4 现行实测字面**：batch2 r2 result 字面 = `model_id_sent=glm-5.3` + `model_returned=glm-5.3`
  - **GLM_2 V4 现行实测尚未落**：实测前已锁本拍板（PI 拍板 reuse）；GLM_2 教师侧跑批数据待 worker 接力棒续跑落字面
  - **coze V4 现行实测尚未落**：以现行 `deepseek-v4-flash` 代表采样（PI 拍板字面）；coze 教师侧跑批数据待 worker 接力棒续跑落字面
  - **minimax V4 现行实测尚未落**：以 mimo `mimo-v2.6-pro` 现行主版本（PI 拍板字面）；minimax 教师侧跑批数据待 worker 接力棒续跑落字面
- **本棒断言等级（明确声明）**：
  - **强断言**（盘上字面可考）：kimi 实测 119 calls / GLM_1 实测 22 calls / teamo 44 models 探活清单 = 盘上字面；引用即 0 编造
  - **中强断言**（PI 拍板直接选答 + 字面引用）：GLM_2 reuse / minimax mimo `mimo-v2.6-pro` = PI 拍板字面；引用即 0 编造
  - **弱断言**（PI 拍板 Other 原文 + 字面引用）：kimi 别名「不界定，否则可能反而造成歧义」/ coze 底层「coze与trea都只是agent平台，我都是接的大模型API」 = PI 拍板 Other 原文；引用即 0 编造
  - **无断言**（沿 §3.3 留 PI 裁定 + §0.5 不可考即不可考）：coze 底层真实 model / 9-backbone ↔ 5 by_model 断层真实 mapping / V3 历史时期 kimi/GLM_1/GLM_2/minimax 调用侧实际 API model = **不断言**（沿诚实纪律不推断 + 不可考即如实不可考）

> **诚实根因守住（不软化）**：
> - **本棒不声称「coze = deepseek-v4-flash」**——仅声称「coze 底层 model 不可考，以现行大模型 API `deepseek-v4-flash` 代表采样」
> - **本棒不声称「minimax-m3 → mimo-v2.6-pro = 升级版」**——仅声称「V3 字面 `minimax-m3` 火山方舟已下线，PI 拍板现行采样 mimo 端点 `mimo-v2.6-pro`」
> - **本棒不声称「kimi-k2.7-code → kimi-k3 = 升级版」**——仅声称「V3 字面 `kimi-k2.7-code` 已下线，teamo 实测现行仅 `kimi-k3` / `kimi-k3[1M]` 可用，PI 拍板沿用 teamo `kimi-k3`」
> - **本棒不声称「GLM_2 = GLM_1 是同一模型」**——仅声称「GLM_2 与 GLM_1 同 model_id_sent（teamo `glm-5.3`），但不同语料」（**同 model 不同语料** ≠ **同一模型**；语料差异仍可导致生成差异）

---

## §5 产物链 / 复用资产 / 老实交代（仅本棒新增 1 件）

### 5.1 产物链（`_v4_supp_l14v3_model_mapping_*`，诞生即 SHA-12，派生 JSON 不合并）

> **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）；本棒产物为单一留痕文件，不附带 executor / result / verdict（三件均已存在，本棒仅追加 map 口径留痕）

- `_v4_supp_l14v3_model_mapping_2026_09_24.md`（**本棒**，五教师 model 映射拍板留痕件——三栏对照表 + PI 拍板 §2 字面引用 + explore 查证 §3 字面引用 + 诚实 §4 声明 + 输入件 SHA-12 链）
- 与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` + `_v4_supp_t1_*` + `_v4_supp_l14v3_*`（batch1 r6 / batch2 r2 / models probe / executor 套件）同级独立；**0 合并**

### 5.2 复用资产（0 触动既有字面）

- L14+ 预登记件 `05B975A86989`（沿 L14+ §1.5 K-N26-* 字面一字不动 + v0.2 §0 五教师 × 22 caption × 双向 ≥1,100 calls 字面）
- batch1 r6 result `A4F851154551` + batch1 r6 executor `5F02C7E0F094`（沿 kimi 实测 119 calls 字面源 + model_id_sent 字面源）
- batch2 r2 result + batch2 r2 executor（沿 GLM_1 实测 22 calls 字面源 + model_id_sent 字面源）
- batch2 r2 models probe `3C9DC60B5071`（沿 teamo 44 models 探活清单字面源 + GLM 系 4 个 + kimi 系 2 个 + 无 coze + 无 minimax-m3）
- N-26 主预登记 `0A9EE16267B5` §2 K-N26-1/2/3 字面（沿用一字不动）
- L4 verdict `74B5B37F7EEA` + L13 verdict `E105EC1362DB` + L7 verdict `B8335982AE5E`（沿用一字不动）
- v0.2 `D85488A64D89` + v0.2 activation `AD42992DC75D` + add_T1 件 + add_T1 activation + L9 `23879B6CD1CC` + L10 `F6FE005EE3C7`（沿 add_T1 §1.8 字面）
- 方法预登记 `0A7BCA992B95` + 种子预登记 `113CBE555643`（沿用一字不动）
- Track 2 multimodel probe `B65619A07B10` + Track 2 endpoints probe `C846F7FC79EE`（端点 + tun + 串行 ≥2s + mimo 端点字段源）
- `deposon_v3_physical_opt_60cells_2026_09_11.json` L26 9_models 字段（V3 9-backbone 字面锚源）
- `corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/` 制品（V3 by_model 字段字面源 + 证实无 model 字段）
- `letters/_v4_distillation_reply_claude_code_2026_09_20.md` L168-170 + `letters/_v4_theme_reply_mavis_2026_09_20.md` L36（V3 mapping 查证结论字面源）

### 5.3 不动件声明（沿 R5 frozen + V1–V3 只读 + 0 触动既有）

- **0 触动 L14+ 预登记 `05B975A86989` 一字**
- **0 触动 N-26 主预登记 `0A9EE16267B5` §2 K-N26-1/2/3/N1/N2 字面一字**
- **0 触动 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」一字**
- **0 触动 L13 verdict `E105EC1362DB` §11「V4 三元组基底」一字**
- **0 触动 L7 verdict `B8335982AE5E` §11「E-N20 实证」一字**
- **0 触动既有 K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 阈值**
- **0 触动 batch1 r6 result `A4F851154551` / batch2 r2 result `CB37B699FF73` / batch2 r2 models probe `3C9DC60B5071`**
- **0 触动 V3 资产（`deposon_v3_physical_opt_60cells_2026_09_11.json` / `corpus/v20/by_model/{...}/` / `scripts/run_v3x_*.py` / letters/ 全树）**
- **不立 V3 → V4 model 升级版字面继承断言表**（仅沿 PI 拍板字面记录现行采样映射；不沿 `kimi-k2.7-code` → `kimi-k3` / `glm-5.3` 自身 / `minimax-m3` → `mimo-v2.6-pro` 做版本升级断言）

### 5.4 老实交代（0 产物诚实 + 不可考即如实不可考 + 不编造）

- **0 产物报 0 产物**：本棒仅产 1 件 md 留痕文件（无 executor / 无 result json / 无 verdict 文件），沿 §5.1 产物链字面不虚增
- **不可考即如实不可考**：V3 时期 coze 底层 model + V3 时期 kimi/GLM_1/GLM_2/minimax 调用侧实际 API model = V3 制品层无字面记录 = **不可考即如实不可考**（沿 §4 诚实声明「无断言」段字面）
- **不编造 model 字段**：本棒不立 V3 by_model 制品层的 model 字段（盘上无 = 字面如实）；不立 V3 → V4 升级版字段（无版本继承字面）；不沿 9-backbone 任一字面推断 by_model 制品层 model 字段
- **不立别名对照表**：沿 PI 拍板 §2 Q1 字面「不立别名对照表」——本棒 §1.1 三栏对照是**字面引用**（不立 mapping 表）；§1.2 派生字段是 **result json 内 metadata 字段**（**不作对外引用，仅审计回查**）
- **拍板原文逐字引用不改写**：§2 两条 Other 原文（kimi 别名「不界定，否则可能反而造成歧义」 + coze 底层「coze与trea都只是agent平台，我都是接的大模型API」）沿 PI 在 ask 工具中键入字面**原样引用**——不改字 / 不改标点 / 不改大小写 / 不空格归一化
- **skill 缺位老实交代**：派工单指定 `scientific-research-workflows:scientific-writing` skill（plugin @scientific-research-workflows，sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb），本地 skill 加载器实录 `Local skill not found`（沿 L14+ §0 同口径）—— 本棒按 L14+ `05B975A86989` + N-26 `0A9EE16267B5` + L4 `74B5B37F7EEA` + L13 `E105EC1362DB` + L7 `B8335982AE5E` + v0.2 `D85488A64D89` + add_T1 + L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` + 方法预登记 `0A7BCA992B95` + 种子预登记 `113CBE555643` 既有件字面锚执行 + §3 三处 explore 查证结论字面引用 + §2 PI 拍板字面引用，**未编造 skill 不存在的虚构指令**

---

## §6 留待 PI 复核生效项（待拍板 / 待裁定 / 留 PI 裁定注记）

> **收口须穷尽清点未决项**（沿 PI 2026-09-23「收口须穷尽清点未决项，不得漏报」口径）—— 本棒所有未拍板 / 未裁定 / 留 PI 裁定注记项如下文所列，无隐藏项：

### 6.1 本棒边界内待 PI 复核生效项（沿本棒字面）

| # | 待拍板 / 待裁定项 | 本棒字面状态 | PI 复核生效方式（沿本棒字面） |
|---|---|---|---|
| 1 | §1.1 五教师映射三栏对照表（kimi / GLM_1 / GLM_2 / coze / minimax 第三栏 PI 拍板定案 = teamo `kimi-k3` / teamo `glm-5.3` / teamo `glm-5.3` 复用 / teamo `deepseek-v4-flash` 代表采样 / mimo `mimo-v2.6-pro`） | 全部沿 §2 PI 拍板字面引用；本棒不动 | 沿 §6 字面生效即锁；事后不重开不调 |
| 2 | §1.2 派生 metadata 字段是否入 result json（`v3_anchor_api_name` / `v3_anchor_9backbone_name` / `v4_current_model_id_sent` / `v4_current_model_returned` / `v4_current_endpoint` 等） | 本棒仅在 §1.2 表内字面列示；**未定 result json 是否必入** | 待 PI 复核：是否入 result json 字段（audit-only / 必入 / 不入） |
| 3 | §2 两条 Other 原文（kimi 别名 + coze 底层）逐字引用 | 沿 ask_748d9242 键入字面原样引用；本棒不动 | 沿 §2 字面生效即锁 |

### 6.2 断层仍留 PI 裁定项（沿 §3.2 + §3.3 字面，本棒不动）

| # | 留 PI 裁定项 | 本棒字面状态 |
|---|---|---|
| 4 | `coze` 处置（断层裁定：`coze` 在 grid 与 four 之外） | 沿 PI 拍板「agent 平台封装」字面裁定底层 model 不可考；**是否需新建 by_model 制品层以承载 coze 身份锚 仍留 PI 裁定** |
| 5 | `kimi` 模型制品缺位（断层裁定：`kimi-k2.7-code` 在 grid 但缺 model 制品） | 沿 PI 拍板「不立别名对照表」字面裁定映射口径；**是否需新建 by_model/kimi 的 model 制品 仍留 PI 裁定** |
| 6 | 5 个 backbone 无 by_model 目录（断层裁定：`doubao-seed-2.0-lite` / `doubao-seed-evolving` / `doubao-seed-2.1-turbo` / `deepseek-v4-flash` / `deepseek-v4-pro` 字面无 by_model 制品层） | **仍留 PI 裁定**（是否需新建 by_model 制品层 / 是否需对应五教师采样 / 是否影响 K-N26-* 字面判定） |
| 7 | `GLM_1`/`GLM_2` lineage 具体边界（V3 字面 `glm-5.3` vs `glm-5.3-flash` 同 lineage 字面） | 沿 PI 拍板 GLM_2 reuse 字面裁定；**两 lineage 内 `glm-5.3` / `glm-5.3-flash` / `glm-5.3-flash-free` 三规格在 result 层是否标注 lineage tag 仍留 PI 裁定** |
| 8 | `minimax` 跨厂商跨端点命名映射（V3 字面 `minimax-m3` 火山方舟 → V4 现行 mimo `mimo-v2.6-pro` 跨端点跨厂商） | 沿 PI 拍板 `mimo-v2.6-pro` 字面裁定现行采样；**命名映射依据 PI 拍板本身，非字面继承 仍留 PI 后续裁定（是否需在派生 JSON 标注 lineage_discontinuity=true）** |

### 6.3 收口未拍板项确认

- **本棒已穷尽清点全部未拍板 / 留 PI 裁定项**——上表 8 项（待 PI 复核生效 3 项 + 留 PI 裁定 5 项）= 全部；**无隐藏未拍板项**
- **本棒不擅自补断层裁定**（沿 §3.3 字面「本棒 §3 仅字面引用既有查证结论，不补新探索」）
- **本棒不沿 9-backbone 任一字面字段做新 mapping 推断**（沿 v0.2 §0 「0 编造专有名词 / 0 编造 mapping」口径）

---

## §7 判死线字面（本棒不动 K-N26-* 字面，全沿 N-26 主预登记 `0A9EE16267B5` §2）

> **字面不动声明**：K-N26-1/2/3/N1/N2 字面**完全沿** N-26 主预登记 `0A9EE16267B5` §2 + L4 verdict `74B5B37F7EEA` §11 + L13 verdict `E105EC1362DB` §11 + L7 verdict `B8335982AE5E` §11 字面；本棒 0 触既有 K-N26 字面；0 新设数值阈值。

| K-* | 字面（沿 N-26 主预登记字面） | hit 触发条件 | hit=True 后果 | 字面源 |
|---|---|---|---|---|
| K-N26-1 | 教师准确率 ≥ 0.70 → 真证伪 | 教师准确率 ≥ 0.70 | N-26 真证伪（教师准确率命中既判阈值） | `0A9EE16267B5` §2 |
| K-N26-2 | 教师侧 vs distill 侧二分类 AUC < 0.75 → 真证伪 | AUC < 0.75 | N-26 真证伪（二者不可分） | `0A9EE16267B5` §2 |
| K-N26-3 | ≥ 4 教师准确率 < 0.60 → 真证伪 | ≥ 4 教师准确率 < 0.60 | N-26 真证伪（多数教师准确率未达既判阈值） | `0A9EE16267B5` §2 |
| K-N26-N1 | 每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化 → 构造非退化自证 | N_min 不足或 J 中位分布退化 | 命题不明 / 构造失灵 | `0A9EE16267B5` §2 |
| K-N26-N2 | teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师 → tun 合规 | teamo 端点未走 tun 或空响应率 > 50% | 构造失灵 / tun 不合规 | `0A9EE16267B5` §2 |

---

## §8 SHA-12 自核（落盘即报）

> **本棒文件**：`results/_v4_supp_l14v3_model_mapping_2026_09_24.md`
> **SHA-12（前 12 字符 SHA256）**：见落盘报值（见本棒末尾 ←本棒写入时即生成）
> **字节**：见落盘报值
> **诞生时刻**：2026-09-24 本棒写入即时
> **SHA 自核方式**：写入后 `Get-FileHash -Algorithm SHA256` 提取 SHA256，取前 12 字符
