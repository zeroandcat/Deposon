# V4 补测预登记 v0.2 L14+ 追加件 · N-26 V3 distill 整链重跑 真审唯一路径（2026-09-24）

- **性质**：protocol-keeper 追加立线（派工单 2026-09-24 L14+ follow-up，protocol-keeper 起草；本棒从 PI 2026-09-24 派工「L14+ V3 整链重跑预登记——N-26 真审唯一路径（即锁）」—— V3 distill 流水线整链重跑复现 + 采集阶段同步保四元组（prompt_id / prompt_text / response_text / per-call metadata）；本稿不调用任何 LLM，不跑实验，仅固化 L14+ 立线 + N-26 字面 + kill-line 字面（K-N26-1/2/3/N1/N2 一字不动）+ 工具失灵修正条款 + 调用预算 + 阈值来源表 + 沿 add_T1 `48,738 B / 14,234 B` + L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` 双件先例）
- **定位（边界）**：**L14+ = N-26 真审唯一路径**（V3 distill 整链重跑复现 + 采集阶段四元组保真）；不翻 N-26 既定结论（N-26 verdict FAIL · 构造不可行 · 4/5 教师 metadata 缺位 沿 `74B5B37F7EEA` §11 字面不动）；本棒执行后判死 = N-26 重审判定（如实替换原 FAIL）
- **预登记件本体不动**：`results/_v4_N09_N39_prereg_2026_09_23.md` SHA-12 `0A9EE16267B5`（**盘上已清出**，inventory L800 锁定 SHA-12 + 60,530 B 字面源）锁后**一字不改**；L4 verdict `results/_v4_supp_l4_n26re_verdict.md` SHA-12 `74B5B37F7EEA`（**盘上已清出**，ledger L208 锁定 SHA-12 + 16,365 B 字面源）锁后**一字不改**；L13 verdict `results/_v4_supp_l13_n26pair_verdict.md` SHA-12 `E105EC1362DB`（**盘上已清出**，ledger L188 锁定 SHA-12 + 23,120 B 字面源）锁后**一字不改**；L7 verdict `results/_v4_supp_l7_e_n20_verdict.md` SHA-12 `B8335982AE5E`（**盘上已清出**，ledger L282 锁定 SHA-12 + 6,424 B 字面源）锁后**一字不改**；add_T1 件 `48,738 B` + activation `14,234 B`（落盘报值见 §0）锁后**一字不改**；本棒以独立追加件形式立线
- **PI 复核待生效**（沿 `0A9EE16267B5` + `74B5B37F7EEA` + `E105EC1362DB` + `B8335982AE5E` + add_T1 件锁先例）—— L14+ 立线 + N-26 字面 + kill-line 字面（方向触发 = hit=True）+ 工具失灵修正条款 + 调用预算 + 产物链 `_v4_supp_l14v3_*` 待 PI 复核生效；**生效即锁**（沿 `0A7BCA992B95` 锁先例），事后不重开不调；**「CONDITIONAL PASS」退役**，只用 PASS / FAIL 二值（沿 R6 实证）
- **范围**：L14+ V3 distill 整链重跑 = V3 distill 流水线（`scripts/run_v3x_*.py` 参照系 + 端点 qwen_plan/mimo/teamo 三端点 + Token Plan 5h 重置窗口）跨 5 教师（kimi / GLM_1 / GLM_2 / coze / minimax） × 22 caption × ≥5 calls × 双向（distill + teacher 各自采样）≥1,100 calls 同步保四元组（prompt_id / prompt_text / response_text / per-call metadata）；不含 L1 N-28 / L2 N-11 / L3 N-20 / L5 C-S39 / L6 S-38 / L8 N-12 / L9 A2R / L10 E-N20 等其它线（沿 v0.2 §1-§8 字面不动 + add_T1 §0 字面不动）；不含 add_T1 §0.5 T1 稳健性探针 12 cells 矩阵
- **判定依据**：deposon 项目核心准则四条「大材小用，落到实处，与死同行，虚实回路（FTFB）」（PI 2026-09-22 R1 录入 + 2026-09-23 FTFB 入根 + **准则为根，论文为一处外显**；详见 `113CBE555643` §0 注）—— 三问映射沿既有预登记件 §1.1.1 代拟稿 §1 + 种子稿 §0 + 整合补充稿 §1（沿 `0A7BCA992B95` §1）

---

## 输入件 SHA-12 链（核对一致后用）

| 件 | 路径 | SHA-12 | 字节 | 状态 | 用途 |
|---|---|---|---|---|---|
| **N-26 主预登记（锚定不动）** | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | 60,530 | **盘上已清出**（inventory L800 锁定） | §2 N-26 K-* 字面（K-N26-1/2/3/N1/N2 一字不动）|
| **L4 verdict N-26 v2（锚定不动）** | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | 16,365 | **盘上已清出**（ledger L208 锁定） | N-26 v2 metadata 5/5 全补齐基线（沿 §11 既判 FAIL · 构造不可行 · 缺教师侧配对）|
| **L13 verdict N-26 pair 三元组基底（锚定不动）** | `results/_v4_supp_l13_n26pair_verdict.md` | `E105EC1362DB` | 23,120 | **盘上已清出**（ledger L188 锁定） | V4 三元组基底（re-asked / distill / independent）—— L14+ V3 整链重跑复现参照系 |
| **L7 verdict E-N20 实证锚（锚定不动）** | `results/_v4_supp_l7_e_n20_verdict.md` | `B8335982AE5E` | 6,424 | **盘上已清出**（ledger L282 锁定） | background session 单批 ≤275s / 600s watchdog 内可行实证锚 |
| v0.2 预登记本体（锚定不动） | `results/_v4_supp_prereg_v02_2026_09_24.md` | `D85488A64D89` | 42,764 | 沿 add_T1 引用 | L14+ 立线锚定 + 通用条款格式（TH-* / 派生 JSON / 双读法 / 阈值表） |
| v0.2 activation 件 | `results/_v4_supp_prereg_v02_activation_2026_09_24.md` | `AD42992DC75D` | 3,202 | 沿 add_T1 引用 | L14+ 立线后状态沿 `AD42992DC75D` 锁先例 |
| add_T1 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | （落盘报值 `48,738 B`） | 48,738 | 盘上在 | L14+ 立线锚定 + LLM 调用纪律沿用 |
| add_T1 activation 件（锚定不动） | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | （落盘报值 `14,234 B`） | 14,234 | 盘上在 | L14+ 立线后 add_T1 锁先例 |
| L9 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L9_2026_09_24.md` | `23879B6CD1CC` | 19,586 | 沿 add_T1 引用 | L14+ 立线锚定 + 双读法并记先例 |
| L10 追加件（锚定不动） | `results/_v4_supp_prereg_v02_add_L10_2026_09_24.md` | `F6FE005EE3C7` | 26,159 | 沿 add_T1 引用 | L14+ 立线锚定 + 语义反转注释先例 |
| 方法预登记补充稿 | `results/_v4_methods_prereg_supplement_2026_09_23.md` | `0A7BCA992B95` | 59,570 | 沿 add_T1 引用 | §1 通用条款 + 格式基线 |
| N-09~N-39 预登记（同 0A9EE16267B5） | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | 60,530 | 盘上已清出 | N-26 §2 K-* 字面源（沿用一字不动） |
| 种子预登记补充稿 | `results/_v4_seeds_prereg_supplement_2026_09_23.md` | `113CBE555643` | 53,633 | 沿 add_T1 引用 | §0 注 + 格式基线 |
| **V3 distill 流水线参照系** | `scripts/run_v3x_*.py`（沿 V3 资产只读） | （V3 字面 SHA，沿 R5 只读不动） | — | V1–V3 只读 | V3 distill 流水线复现参照（端点 / 参数 / 中间产物格式） |
| **22 caption 锚（沿 add_T1）** | `corpus/v20_caption_surface/strip_captions_22.json` | `6A2656878745` | — | 沿 add_T1 引用 | 22 caption 素材面 |
| **5 by_model（V3 字面）** | `corpus/v20/by_model/{kimi,GLM_1,GLM_2,coze,minimax}/` | （V3 字面 SHA） | — | V1–V3 只读 | 5 教师锚定（沿 TH-14） |
| Track 2 multimodel probe | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | — | 沿 add_T1 引用 | 三端点 ROUTE_TEMPLATES + tun 代理 + 串行 ≥2s |
| Track 2 endpoints probe | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | 5,803 | 沿 add_T1 引用 | qwen_plan / mimo / teamo 三端点权威源 |
| Track 2 multimodel verdict | `results/_v4_track2_multimodel_verdict_2026_09_23.md` | （自身 SHA） | 12,883 | 沿 add_T1 引用 | 6 模型补跑判定锚定 |

> 注：N-26 主预登记 `0A9EE16267B5` + L4 verdict `74B5B37F7EEA` + L13 verdict `E105EC1362DB` + L7 verdict `B8335982AE5E` 四件**盘上已清出**（2026-09-24 cleanup manifest 处置后）；inventory `_v3_v4_achievements_inventory_3dir_2026_09_24.md` L800/L1075/L1179 + ledger `_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` L188/L208/L282 锁定四件 SHA-12 + 字节 + 落地时间；本棒沿四件 SHA-12 字面引用为权威锚源（沿 add_T1 §9 L14 verdict 漂移披露模式：「字面引用锚定 SHA = 字面引用件自报值」），**不擅自以盘 SHA 替代字面引用值**（如四件后续 reconciliation 致 SHA 漂移，本棒派 evidence-auditor 下一轮 reconciliation 时定夺，不擅改本棒字面）。本棒 0 触动四件一字不动。

---

## §0 边界声明（沿 R5 / R6 / R7 复审稿，2026-09-23 勘误版）

- **0 LLM 调用**：本稿由 protocol-keeper 起草，全程未调用任何 LLM API；纯文件编辑（write/edit），未调任何 LLM/代理/构造代理/网关；沿 V4 §3.1 放开语境明示可调（PI 2026-09-22「V3 的剑不斩 V4 的官」），本棒无需调
- **R4 key 永不明文**（**无例外**，沿 R4 + PI 2026-09-22「key 永不明文等合理且无冲突的铁律要沿用」）：本稿及其后续产物不写入、不引用、不打印任何明文 API key / 平台密钥；key 仅在进程组方法里以 runtime env 读取；**本稿自扫** `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态 0 命中
- **R5 V4 frozen 只追加**（**V4 沿用 V1–V3 资产只读底线**）：本稿不修改 N-26 主预登记 `0A9EE16267B5` / 不动 L4 verdict `74B5B37F7EEA` / 不动 L13 verdict `E105EC1362DB` / 不动 L7 verdict `B8335982AE5E` / 不动 v0.2 本体 `D85488A64D89` / 不动 v0.2 activation `AD42992DC75D` / 不动 add_T1 件 + activation / 不动 L9 `23879B6CD1CC` + L9 activation `5C579F28634E` / 不动 L10 `F6FE005EE3C7` + L10 activation `16E89657DAAA` / 不动 Track 2 multimodel probe `B65619A07B10` + endpoints probe `C846F7FC79EE` / **派生 JSON 不合并**（本棒产物用 `_v4_supp_l14v3_*` prefix 分列，与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` + `_v4_supp_t1_*` 同级独立）
- **R6 P-G v0/v01 / R7 plugin spec**：本棒不动 P-G v0/v01；不动 plugin spec；不动 verifier 内置脚本
- **V1–V3 只读不动**：letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读（沿 R5 + V4 §3.1）—— **本棒 V3 distill 流水线复现 = 读取 `scripts/run_v3x_*.py` 参照系 + 新建 `scripts/_v4_l14v3_*.py` runner，0 触动原 V3 件**
- **kill-line 字面不动禁私设条款**（S-40 教训：判定布尔显式方向 `hit=True` 即触发 / `pass=True` 即存活，禁裸 bool；PI 2026-09-23 拍板明示「禁止擅自调阈值 / 禁止合并派生 JSON / 禁止私设 kill-line 条款」）：本棒 L14+ kill-line 字面**完全沿** N-26 主预登记 `0A9EE16267B5` §2 字面（K-N26-1 准确率 ≥0.70 / K-N26-2 AUC <0.75 / K-N26-3 ≥4 教师准确率 <0.60 + K-N26-N1 非退化自证 + K-N26-N2 tun 合规），**0 触既有 K-N26 字面**；**阈值 0.70 / 0.75 / 0.60 沿 N-26 §2 字面一字不动**
- **0 擅调阈值**（沿 v0.2 §0 同口径 + add_T1 §0 同口径）：本棒 **0 调既有 K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 / K_N26_N1_N_MIN = 0 / K_N26_N2_TUN_PASS_RATE = 1.0**；阈值**一字不动**
- **L14+ 定位硬约束**：本棒 = N-26 真审唯一路径（V3 distill 整链重跑复现 + 采集阶段同步保四元组），**改判 N-26 既定结论须走 verdict-keeper 裁因 + verifier 签字 + PI 复核完整流程**（沿 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」既定结论一字不动；本棒执行后判死 = N-26 重审判定，**不预设立场**）
- **skill 加载老实交代**：派工单要求 `scientific-research-workflows:experimental-design` skill（plugin @scientific-research-workflows，sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb），本地 skill 加载器多次实录 `Local skill not found`（沿 v0.2 §0 + add_T1 §0 同口径）—— 本棒按 `0A9EE16267B5` + `74B5B37F7EEA` + `E105EC1362DB` + `B8335982AE5E` + v0.2 `D85488A64D89` + add_T1 件 + L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` + 方法预登记 `0A7BCA992B95` + 种子预登记 `113CBE555643` 的格式与字面锚执行，**未编造 skill 不存在的虚构指令**

---

## §0.5 过渡声明（本棒 L14+ 立线件特有）

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）

- **L14+ N-26 真审唯一路径定位过渡**：自本件立线起标「**已知 N-26 v1 FAIL · 构造不可行 · 4/5 教师 metadata 缺位（kimi/GLM_1/GLM_2/coze 全 False×3 metadata；仅 minimax 有 latency / token_usage / reasoning_tokens 全 True）+ L4 v2 metadata 1/5 → 5/5 全补齐（kimi/GLM_1/GLM_2/coze 由 V3 缺位补全）+ 但缺教师侧配对（V3 调用侧未保留）= 后续重采大工程 + L13 V4 三元组基底立定 + L7 实证 background session ≤275s 可行**——
  - L4 verdict `74B5B37F7EEA` §11 总判定 = 「FAIL（构造不可行，问题收窄）」（v2 metadata 5/5 + 缺教师侧配对 = V3 调用侧未保留）
  - L13 verdict `E105EC1362DB` §11 总判定 = （V4 三元组基底立定，N-26 重审参照系就位）
  - L7 verdict `B8335982AE5E` §11 总判定 = （E-N20 实证 background session ≤275s / 600s watchdog 内可行）
  - N-26 主预登记 `0A9EE16267B5` §2 字面 K-N26-1/2/3/N1/N2 一字不动 = 准确率 ≥0.70 / AUC <0.75 / ≥4 教师准确率 <0.60 / K-N26-N1 非退化自证 / K-N26-N2 tun 合规
  - 本棒 = **唯一真审路径**（V3 distill 整链重跑复现 + 采集阶段同步保四元组）—— 历史 V3 调用侧 metadata 断点不可回溯，唯一补法 = 整链重跑
  - L14+ 在 V3 distill 流水线复现下探「K-N26-1/2/3/N1/N2 是否仍按既判方向触发」—— **不预设 PASS / FAIL 翻转**（沿 PI 2026-09-23「诚实的根因是不误导」+ 沿 add_T1 §0.5 同口径）
  - 真证伪触发（任一 K-N26-* hit=True 重新落定真证伪方向）= **N-26 重审真证伪**（与 v1/v2 方向一致）
  - 假证伪族 / 命题不明触发 = **N-26 重审构造不可行 / 命题不明**（与 v1/v2 方向一致或新定性）
- **本棒不动 v0.2 §0.5 既有 3 件过渡声明**（A2 5 PASS 假 pass 风险 / GLM_2 3 cells 暂定 / L1 K-N28-R2 弱 PASS）+ **不动 L9 §0.5 既有 3 件** + **不动 L10 §0.5 既有 2 件** + **不动 add_T1 §0.5 T1 稳健性探针定位过渡 1 件**

---

## §1 L14+ · N-26 V3 distill 整链重跑 真审唯一路径

### 1.1 三问初判

- **Q1 ✓**：素材面已齐——
  - N-26 主预登记 `0A9EE16267B5` §2 K-N26-1/2/3/N1/N2 字面（60,530 B，inventory L800 锁定）= N-26 判死字面源
  - L4 verdict `74B5B37F7EEA` + L4 result `065DD4393AB8`（v2 metadata 1/5 → 5/5 全补齐，16,365 B + 18,428 B，ledger L207-208 锁定）
  - L13 verdict `E105EC1362DB` + L13 executor `FF6A280BE11A`（V4 三元组基底 re-asked / distill / independent，23,120 B + 51,723 B，ledger L184-188 锁定）
  - L7 verdict `B8335982AE5E` + L7 runner `D5640CA314E2`（E-N20 实证 background session ≤275s / 600s watchdog 内可行，6,424 B + 17,215 B，ledger L281-282 锁定）
  - V3 distill 流水线参照系 `scripts/run_v3x_*.py`（V3 资产只读不动；端点 / 参数 / 中间产物格式参照）
  - 22 caption `strip_captions_22.json` `6A2656878745`（沿 add_T1 §1.8 字面）
  - 5 by_model（沿 TH-14：kimi / GLM_1 / GLM_2 / coze / minimax）
  - Track 2 multimodel probe `B65619A07B10`（三端点 ROUTE_TEMPLATES + tun 代理 + 串行 ≥2s）
  - Track 2 endpoints probe `C846F7FC79EE`（qwen_plan / mimo / teamo 三端点权威源）
  - Track 2 multimodel verdict `_v4_track2_multimodel_verdict_2026_09_23.md`（6 模型补跑锚定）
- **Q2 ✓**：实验设计可执行——
  - **V3 distill 整链重跑复现**：5 教师 × 22 caption × ≥5 calls × 双向（distill + teacher 各自采样）≥1,100 calls —— 双向 = 教师侧与 distill 侧配对 metadata 同步落
  - **采集阶段同步保四元组**：(prompt_id, prompt_text, response_text, per-call metadata) —— 关键补救点 = V3 调用侧 metadata 断点（kimi/GLM_1/GLM_2/coze 4/5 教师 V3 缺位）= 整链重跑时重新采集并保四元组
  - **拆 5-6 教师批**：每 background session 单批 ≤275s（沿 L7 实证 `B8335982AE5E`），600s watchdog 内；qwen_plan/mimo 走 Token Plan 5h 重置窗口跨批续采；teamo 必走 tun 防封号
  - **串行 ≥2.5s 全程**（沿 add_T1 §1.6.2 + Track 2 runner `INTER_CALL_SLEEP_S`）
  - **中断-恢复同 agent 唤醒（task_append）语义写明**（沿 L14 verdict §9.1 中断恢复先例）
- **Q3 ✓**：证伪方向明确——
  - **K-N26-1 触发**（hit=True）= 准确率 ≥ 0.70 → 「教师准确率命中既判阈值」= **N-26 真证伪**（教师 vs metadata 侧显著区分）
  - **K-N26-2 触发**（hit=True）= AUC < 0.75 → 「分类能力低于既判阈值」= **N-26 真证伪**（distill vs teacher 二分类 AUC 低 = 二者不可分）
  - **K-N26-3 触发**（hit=True）= ≥4 教师准确率 < 0.60 → 「多数教师准确率未达既判阈值」= **N-26 真证伪**（4/5 教师准确率 < 0.60）
  - **K-N26-N1 触发**（pass=False）= 非退化自证不成立（构造退化致命题不明）→ **构造不可行族 / 命题不明**
  - **K-N26-N2 触发**（pass=False）= tun 合规失败 → **构造失灵族**（teamo 端点不走 tun = 封号风险 + 不可重复）

### 1.2 矩阵定义（5 教师 × 22 caption × ≥5 calls × 双向 ≥1,100 calls）

| # | 维度（沿 V3 distill + L4/L13/L7 字面） | 端点 | model_id | 代理 | calls 上限 | 字面源 |
|---|---|---|---|---|---|---|
| 1 | 教师侧 kimi × 22 caption × ≥5 calls | qwen_plan + mimo + teamo（沿端点可达性） | kimi（V3 端点名 / API 端点名 = kimi-for-coding） | qwen_plan: 无；mimo: 无；teamo: **是**（tun `http://127.0.0.1:1018`） | ≥110 calls/教师（22 caption × ≥5 calls） | V3 distill 流水线复现 + L7 实证 `B8335982AE5E` |
| 2 | 教师侧 GLM_1 × 22 caption × ≥5 calls | 同上 | GLM_1 | 同上 | ≥110 calls/教师 | 同上 |
| 3 | 教师侧 GLM_2 × 22 caption × ≥5 calls | 同上 | GLM_2 | 同上 | ≥110 calls/教师 | 同上 |
| 4 | 教师侧 coze × 22 caption × ≥5 calls | 同上 | coze | 同上 | ≥110 calls/教师 | 同上 |
| 5 | 教师侧 minimax × 22 caption × ≥5 calls | 同上 | minimax | 同上 | ≥110 calls/教师 | 同上 |
| 6 | distill 侧 kimi × 22 caption × ≥5 calls | 同上 | kimi | 同上 | ≥110 calls/教师 | 同上 |
| 7 | distill 侧 GLM_1 × 22 caption × ≥5 calls | 同上 | GLM_1 | 同上 | ≥110 calls/教师 | 同上 |
| 8 | distill 侧 GLM_2 × 22 caption × ≥5 calls | 同上 | GLM_2 | 同上 | ≥110 calls/教师 | 同上 |
| 9 | distill 侧 coze × 22 caption × ≥5 calls | 同上 | coze | 同上 | ≥110 calls/教师 | 同上 |
| 10 | distill 侧 minimax × 22 caption × ≥5 calls | 同上 | minimax | 同上 | ≥110 calls/教师 | 同上 |

**矩阵汇总**：
- **5 教师 × 22 caption × ≥5 calls × 双向（teacher + distill）= ≥1,100 calls**（理论下限；按需扩展至 ≥5 calls/教师/侧）
- **拆 5-6 教师批**：每 background session 单批 ≤275s（沿 L7 实证 `B8335982AE5E`），600s watchdog 内；理论 10 cells × 单批 ≤110s（含串行 ≥2.5s × ≥44 calls/批）≤ 600s 内完成
- **每 caption 双侧（teacher + distill）配对保四元组 metadata**：(prompt_id, prompt_text, response_text, per-call metadata)—— 关键补救点 = V3 调用侧 metadata 断点（kimi/GLM_1/GLM_2/coze 4/5 教师 V3 缺位）= 整链重跑时重新采集并保四元组
- **总 calls ≥ 1,100**（理论下限；按需扩展）
- **总 wall time ≤ 30h**（10 cells × 单批 ≤110s + 5h × 6 批 Token Plan 配额 ≤ 30h）

### 1.3 claim（可证伪命题）

L14+ V3 distill 整链重跑复现在 5 教师 × 22 caption × ≥5 calls × 双向（teacher + distill）≥1,100 calls 同步保四元组（prompt_id / prompt_text / response_text / per-call metadata）下，沿 N-26 主预登记 `0A9EE16267B5` §2 字面 K-N26-1/2/3/N1/N2 五条 kill-line 触发判定 N-26 命题真审：

- **K-N26-1**：教师准确率 ≥ 0.70 = `hit=True` → N-26 真证伪（教师侧显著高于 metadata 侧）
- **K-N26-2**：教师侧 vs distill 侧二分类 AUC < 0.75 = `hit=True` → N-26 真证伪（二者不可分）
- **K-N26-3**：≥ 4 教师准确率 < 0.60 = `hit=True` → N-26 真证伪（多数教师准确率未达既判阈值）
- **K-N26-N1**（非退化自证）：每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化 = `pass=True` → 构造非退化自证成立；否则 `pass=False` → 命题不明
- **K-N26-N2**（tun 合规）：teamo 端点 100% 走 tun 代理 = `pass=True` → tun 合规成立；否则 `pass=False` → 构造失灵

**本 claim 字面完全沿** N-26 主预登记 `0A9EE16267B5` §2 字面（K-N26-1/2/3/N1/N2）+ L4 verdict `74B5B37F7EEA` §11「FAIL 构造不可行」字面 + L13 verdict `E105EC1362DB` §11「V4 三元组基底」字面 + L7 verdict `B8335982AE5E` §11「E-N20 实证」字面。

**L14+ 探针限定（不预设立场）**：
- L14+ 执行后判死由 **verdict-keeper 裁因**（agent-3a4d09ba3c90）+ **evidence-auditor 审链**（agent-11335500b168）+ **PI 复核**三段签字 = 完整流程生效
- L14+ 不翻既有 N-26 verdict 既判一字不动（L4 verdict `74B5B37F7EEA` §11 既判 FAIL · 构造不可行）
- L14+ 执行后判死可定性 = 真证伪 / 假证伪（工具失灵族 / 构造不可行）/ 命题不明 三类之一（沿拍板 #1 双标签并存）
- L14+ 命中任一 K-N26-* 真证伪方向 = **N-26 真审真证伪**（与 v1/v2 方向可能一致或新方向）
- L14+ K-N26-N1/N2 触发 = **构造失灵 / 命题不明**（属「不强行归类；如实记」）
- 全 K-N26-* 不命中且 N1/N2 全 pass=True = 「**N-26 真审 PASS**」（沿 N-26 主预登记字面）

### 1.4 实验设计

- **素材**：
  - N-26 主预登记 `0A9EE16267B5` §2 K-N26-1/2/3/N1/N2 字面（沿用一字不动）
  - L4 verdict `74B5B37F7EEA` §11 + result `065DD4393AB8`（v2 metadata 5/5 全补齐，缺教师侧配对）
  - L13 verdict `E105EC1362DB` §11 + executor `FF6A280BE11A`（V4 三元组基底 re-asked / distill / independent）
  - L7 verdict `B8335982AE5E` §11 + runner `D5640CA314E2`（background session ≤275s / 600s watchdog 内可行实证）
  - V3 distill 流水线参照系 `scripts/run_v3x_*.py`（V3 资产只读不动；端点 / 参数 / 中间产物格式参照）
  - 22 caption `strip_captions_22.json` `6A2656878745`（沿 add_T1 §1.8 字面）
  - 5 by_model（沿 TH-14：kimi / GLM_1 / GLM_2 / coze / minimax；V3 字面）
  - Track 2 multimodel probe `B65619A07B10`（三端点 ROUTE_TEMPLATES + tun + 串行 ≥2s）
  - Track 2 endpoints probe `C846F7FC79EE`（qwen_plan / mimo / teamo 三端点权威源）
  - Track 2 multimodel verdict `_v4_track2_multimodel_verdict_2026_09_23.md`（6 模型补跑锚定）
- **构造**：
  - **V3 distill 整链重跑复现**（沿 `scripts/run_v3x_*.py` 参照系 + 新建 `scripts/_v4_l14v3_*.py` runner）：
    - 5 教师 × 22 caption × ≥5 calls × 双向（teacher + distill 各自采样）= ≥1,100 calls
    - 端点：qwen_plan + mimo + teamo 三端点（沿 L7 实证三端点可达性）
    - 端点名 / API 端点名差异：kimi 公开产品名 KIMI-K3 / API 端点名 `kimi-for-coding`（沿 L7 实测「端点 key 仅 runtime 读」纪律）
    - 温度 = 0.7 沿 V3 distill 流水线 baseline（不改）
    - **采集阶段同步落四元组**：(prompt_id, prompt_text, response_text, per-call metadata) —— 关键补救点 = V3 调用侧 metadata 断点（kimi/GLM_1/GLM_2/coze 4/5 教师 V3 缺位）= 整链重跑时重新采集并保四元组
    - **串行 ≥2.5s 全程**（沿 add_T1 §1.6.2 + Track 2 runner `INTER_CALL_SLEEP_S`）
  - **拆 5-6 教师批**（每 background session 单批 ≤275s）：
    - 批 1：kimi 教师侧（22 caption × ≥5 calls = ≥110 calls）≤275s
    - 批 2：kimi distill 侧（同上）≤275s
    - 批 3：GLM_1 教师侧 ≤275s
    - 批 4：GLM_1 distill 侧 ≤275s
    - 批 5：GLM_2 教师侧 ≤275s
    - 批 6：GLM_2 distill 侧 ≤275s
    - 批 7：coze 教师侧 ≤275s
    - 批 8：coze distill 侧 ≤275s
    - 批 9：minimax 教师侧 ≤275s
    - 批 10：minimax distill 侧 ≤275s
    - **600s watchdog 内**（沿 L7 实证 ≤275s + 30% 安全冗余）
    - **qwen_plan / mimo 走 Token Plan 5h 重置窗口跨批续采**（沿 add_T1 §1.6.4 中断-恢复先例）
    - **teamo 必走 tun 防封号**（PI 2026-09-23 硬纪律）：
      - `http_proxy=http://127.0.0.1:1018` / `https_proxy=http://127.0.0.1:1018`
      - `all_proxy=socks5://127.0.0.1:1018`
- **工具失灵修正条款**（沿「工具/构造失灵族可补构造」先例，明确非擅调阈值）：
  - **max_tokens 上调规避 L4 触顶**：L4 verdict `74B5B37F7EEA` §2 字面「L4 v2 metadata 4/5 教师 v3 缺位补齐后 max_tokens 触顶」= **max_tokens 从默认上调至 2000**（规避 L4 触顶；非擅调阈值，仅补构造层 token 上限）；沿 L4 §11「构造失灵族补构造」先例
  - **teamo reasoning-only 空响应重试口径**（沿 V3 distill 流水线实测）：
    - **空响应 = response_text 为空字符串 / 仅含空白字符**
    - **空响应计数如实入 result**（不 silently 丢弃）
    - **空响应触发重试**：单 call 触发 teamo reasoning-only 模式空响应 → 内层重试 1 次（最多 3 次内层重试预留）
    - **重试仍空响应 = 计入 result.json 空响应计数字段 + 不入主度量**
    - **空响应率 > 50% per 教师** = K-N26-N2 tun 合规触发 pass=False（构造失灵族）
  - **本棒 0 触既有阈值**（K-N26-1/2/3/N1/N2 字面一字不动）
- **度量**：
  - **主度量 K-N26-1**（hit 触发）= 教师准确率 ≥ K_N26_1_ACC = 0.70 → `hit=True` → N-26 真证伪
  - **主度量 K-N26-2**（hit 触发）= 教师侧 vs distill 侧二分类 AUC < K_N26_2_AUC = 0.75 → `hit=True` → N-26 真证伪
  - **主度量 K-N26-3**（hit 触发）= ≥ 4 教师准确率 < K_N26_3_TEACHERS_LT = 0.60 → `hit=True` → N-26 真证伪
  - **辅助度量 K-N26-N1**（pass 触发）= 每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化 → `pass=True` → 构造非退化自证成立
  - **辅助度量 K-N26-N2**（pass 触发）= teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师 → `pass=True` → tun 合规成立
  - **双读法并记**（沿 K-N26-N1/N2 字面 + v0.2 §2 K-N11-N2 字面）：
    - 构造面（单教师 N_min）= L14+ 单教师 N≥ 既判 N_target
    - 真实面（跨教师累加 N≥）= 跨 5 教师累加 N≥ 既判 N_target × 5
    - 任一面 PASS ≠ 命题成立（必须双面都过）
- **拍板出处**：PI 2026-09-24 派工单「L14+ V3 整链重跑预登记——N-26 真审唯一路径（即锁）」
- **真审条件**：worker 接力棒分批跑；单批 ≤275s 看门狗；撞 5h 配额中断-恢复（沿 L14 verdict §9.1 + L7 实证 ≤275s 双向沿用）
- **非退化自证**：每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化（n_distinct ≥ 3 不退化为常量 / 二值 / 派生 / 码本坍缩 / 单调构造致判据恒真族；沿 v0.2 §2 K-N11-N1 + L4 verdict §2 字面 + add_T1 §0 防退化构造族先例）
- **双读法并记**（沿 K-N26-N1/N2 字面）：
  - 构造面（单教师 N_min）= L14+ 单教师 N ≥ 既判 N_target
  - 真实面（跨教师累加 N≥）= 跨 5 教师累加 N ≥ 既判 N_target × 5
  - 任一面 PASS ≠ 命题成立（必须双面都过）

### 1.5 机械判死线（kill-line，字面即锁，禁私设条款）

> **字面不动声明**：既有 K-N26-1/2/3/N1/N2 字面（沿 N-26 主预登记 `0A9EE16267B5` §2 字面）**一字不动**；本棒 L14+ 仅沿 `0A9EE16267B5` §2 字面引用，**0 触既有 K-N26 字面**，**0 新设阈值**（K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 沿用一字不动）。

#### 1.5.1 既有 K-N26 字面（沿 N-26 主预登记 `0A9EE16267B5` §2 一字不动，锁前痕迹保留）

- **K-N26-1**：教师准确率 ≥ K_N26_1_ACC = 0.70 即 `hit=True` → N-26 真证伪（教师准确率命中既判阈值）—— **沿 `0A9EE16267B5` §2 K-N26-1 字面**（**L14+ 主度量核心沿此字面**）
- **K-N26-2**：教师侧 vs distill 侧二分类 AUC < K_N26_2_AUC = 0.75 即 `hit=True` → N-26 真证伪（二者不可分）—— **沿 `0A9EE16267B5` §2 K-N26-2 字面**
- **K-N26-3**：≥ 4 教师准确率 < K_N26_3_TEACHERS_LT = 0.60 即 `hit=True` → N-26 真证伪（多数教师准确率未达既判阈值）—— **沿 `0A9EE16267B5` §2 K-N26-3 字面**
- **K-N26-N1**：每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化即 `pass=True` → 构造非退化自证成立；否则 `pass=False` → 命题不明 —— **沿 `0A9EE16267B5` §2 K-N26-N1 字面**（**L14+ 构造面判定沿此字面**）
- **K-N26-N2**：teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师即 `pass=True` → tun 合规成立；否则 `pass=False` → 构造失灵 —— **沿 `0A9EE16267B5` §2 K-N26-N2 字面**（**L14+ 工具层判定沿此字面**）

#### 1.5.2 L14+ kill-line 字面总览（沿 N-26 主预登记 `0A9EE16267B5` §2 字面）

| K-* | 字面 | hit 触发条件 | hit=True 后果 | 字面源 |
|---|---|---|---|---|
| K-N26-1 | 教师准确率 ≥ 0.70 → 真证伪 | 教师准确率 ≥ 0.70 | N-26 真证伪（教师准确率命中既判阈值） | `0A9EE16267B5` §2 |
| K-N26-2 | 教师侧 vs distill 侧二分类 AUC < 0.75 → 真证伪 | AUC < 0.75 | N-26 真证伪（二者不可分） | `0A9EE16267B5` §2 |
| K-N26-3 | ≥ 4 教师准确率 < 0.60 → 真证伪 | ≥ 4 教师准确率 < 0.60 | N-26 真证伪（多数教师准确率未达既判阈值） | `0A9EE16267B5` §2 |
| K-N26-N1 | 每教师 N_min ≥ 既判 N_target + 教师 J 中位分布非退化 → 构造非退化自证 | N_min 不足或 J 中位分布退化 | 命题不明 / 构造失灵 | `0A9EE16267B5` §2 |
| K-N26-N2 | teamo 端点 100% 走 tun + 空响应率 ≤ 50% per 教师 → tun 合规 | teamo 端点未走 tun 或空响应率 > 50% | 构造失灵 / tun 不合规 | `0A9EE16267B5` §2 |

> **0 新设阈值声明**：L14+ **0 新设数值阈值**；K-N26-1/2/3/N1/N2 五条**完全沿** `0A9EE16267B5` §2 字面；阈值 0.70 / 0.75 / 0.60 一字不动；本棒 0 触既有 K-N26 字面

#### 1.5.3 L14+ 判定方向（沿 N-26 主预登记 `0A9EE16267B5` §2 字面 + 拍板 #1 双标签并存）

- **L14+ 任一 K-N26-* 真证伪触发**（K-N26-1/2/3 任一 hit=True）= N-26 真审真证伪
- **L14+ K-N26-N1 / N2 触发**（任一 pass=False）= N-26 构造失灵 / 命题不明（如实记录）
- **L14+ 全 K-N26-* 不命中且 N1/N2 全 pass=True** = N-26 真审 PASS
- **判定布尔显式方向**（沿 S-40 教训）：`hit=True` 即触发 / `pass=True` 即存活，禁裸 bool

### 1.6 调用预算与节制（Token Plan 5h 限额硬约束）

> **硬约束声明**：L14+ 沿 add_T1 §1.6 + L14 verdict §9.1 + L7 实证 ≤275s 三向沿用；本棒新立 L14+ 独立配额，与 add_T1 / L14 既定 5h 配额**物理隔离**（端点组合不同 = qwen_plan/mimo/teamo 三端点 vs qwen/mimo/teamo 两端点；worker 接力棒按端点分批）

#### 1.6.1 单批 calls 上限（看门狗约束）

- **单批 ≤ 22 calls**（沿 L7 实证 `B8335982AE5E` ≤275s 上限：22 calls × 2.5s 串行 + 处理开销 ≈ 110s，含 60% 安全冗余 ≤275s 内完成）
- **每 caption 拆批**：每 caption ≤ 5 calls / 单批 ≤ 22 calls（含教师侧 + distill 侧 + 重试预留）
- **22 caption × 单批 = 22 批 / 教师 / 侧**（理论上限；按需扩展至 ≥5 calls/教师/侧）
- **10 cells × 22 批 = 220 批**（理论上限；实际按需调整）

#### 1.6.2 串行间隔与代理

- **串行间隔 ≥ 2.5s**（沿 add_T1 §1.6.2 INTER_CALL_SLEEP_S + Track 2 runner INTER_CALL_SLEEP_S 沿用）
- **qwen_plan 端点**（沿 Track 2 endpoints probe `C846F7FC79EE`）：**无代理**（沿 L7 实证）
- **mimo 端点**（token-plan-cn.xiaomimimo.com/v1）：**无代理**（沿 add_T1 §1.6.2 + L7 实证）
- **teamo 端点**（api.teamorouter.cn/v1）：**必走 tun 防封号**（PI 2026-09-23 硬纪律）：
  - `http_proxy=http://127.0.0.1:1018` / `https_proxy=http://127.0.0.1:1018`
  - `all_proxy=socks5://127.0.0.1:1018`
  - 直连 = 封号风险（沿 user memory 「teamorouter/openrouter 必走 tun 代理防封号」2026-09-23）

#### 1.6.3 总预算上限

- **总 calls 下限 ≥ 1,100 calls**（5 教师 × 22 caption × ≥5 calls × 双向 = ≥1,100 calls；按需扩展）
- **总 calls 上限 ≤ 5,500 calls**（5 教师 × 22 caption × 25 calls × 双向 = 5,500 calls 硬上限；含重试预留）
- **总 wall time ≤ 30h**（10 cells × 单批 ≤275s + 5h × 6 批 Token Plan 配额 ≤ 30h；含中断-恢复时间）
- **每 cell 实际 calls 预算**：
  - 教师侧：5 教师 × 22 caption × ≥5 calls = ≥550 calls（理论下限）
  - distill 侧：5 教师 × 22 caption × ≥5 calls = ≥550 calls（理论下限）
  - 双向合计 ≥1,100 calls（理论下限）
  - **10 cells × 110 calls/cell = 1,100 calls 实际预计下限**（远低于 5,500 calls 硬上限）

#### 1.6.4 中断-恢复与分批拆跑方案

- **中断-恢复语义**（沿 L14 verdict §9.1 + L7 实证 ≤275s + add_T1 §1.6.4 双向沿用）：
  - 同 worker 接力棒：v1 撞 5h 配额 → PI 明示额度重置 → 同棒续跑 v2（沿 L14 verdict §9.1）
  - **同 agent 唤醒（task_append）**：worker session 不重启，沿 task_append 续跑（沿 L14 verdict §9.1 同棒续跑 + L7 实证 ≤275s 同 session 续跑）
  - checkpoint 文件：`.tmp/_l14v3_records.json`（沿 L14 runner `.tmp/_l14_records.json` + add_T1 `.tmp/_t1_records.json` 惯例）
  - 每 call 后 checkpoint 累积（沿 L14 runner L151-156 惯例）
  - 已跑 (teacher, caption_id, reask_idx, side, endpoint) 元组 skip（沿 L14 runner L107-110 + add_T1 §1.6.4 惯例）
- **分批拆跑**：
  - 撞 5h 配额自动恢复（worker 接力棒续跑）
  - 单批撞 275s 看门狗自动停（沿 L7 实证 ≤275s）
  - 中断-恢复同 agent 唤醒语义（task_append 续跑）
- **额度撞限应急**（如 10 cells 未跑完撞 5h 配额）：
  - 仅跑已启动 cells，不补未启动 cells
  - 已启动 cells 部分完成记「L14+ 部分完成」注记
  - 未启动 cells 留待 worker 下一棒接力

### 1.7 产物链（`_v4_supp_l14v3_*`，诞生即 SHA-12，派生 JSON 不合并）

> **派生 JSON 不合并**（沿 R5 frozen 派生 JSON 不合并铁律）；本棒产物用 `_v4_supp_l14v3_*` prefix 分列

- `_v4_supp_l14v3_executor.py`（L14+ V3 distill 整链重跑复现 runner + checkpoint 模式 + 端点切换 + 四元组保真采集 + 拆 5-6 教师批 ≤275s）
- `_v4_supp_l14v3_result.json`（5 教师 × 22 caption × 双向 ≥1,100 calls 矩阵结果聚合：每 cell per teacher per side accuracy + AUC + 四元组 metadata + schema `v4_l14v3_n26/1` + tun 合规字段 + 空响应率字段）
- `_v4_supp_l14v3_verdict.md`（L14+ 探针判定：5 教师 K-N26-1/2/3/N1/N2 实测 + 触发判定 + 根因三分类每行附 + **N-26 真审重判声明**）
- 与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` + `_v4_supp_t1_*` 同级独立；**0 合并**（沿「派生 JSON 不合并」铁律）
- **schema L14+ 专属**：result JSON 中 `schema` 字段 = `"v4_l14v3_n26/1"`（L14+ 专属 schema，与 L13 `v4_l13_n26pair` + L4 `v4_l4_n26re` + add_T1 `v4_t1_sensitivity/1` 同级独立）

### 1.8 复用资产（0 触动既有字面）

- N-26 主预登记 `0A9EE16267B5` §2 K-N26-1/2/3/N1/N2 字面（沿用一字不动，**盘上已清出**但 inventory L800 锁定 SHA-12 + 60,530 B）
- L4 verdict `74B5B37F7EEA` + L4 result `065DD4393AB8`（v2 metadata 5/5 全补齐，**盘上已清出**但 ledger L207-208 锁定 SHA-12 + 16,365 B / 18,428 B）
- L13 verdict `E105EC1362DB` + L13 executor `FF6A280BE11A`（V4 三元组基底，**盘上已清出**但 ledger L184-188 锁定 SHA-12 + 23,120 B / 51,723 B）
- L7 verdict `B8335982AE5E` + L7 runner `D5640CA314E2`（E-N20 实证，**盘上已清出**但 ledger L281-282 锁定 SHA-12 + 6,424 B / 17,215 B）
- v0.2 预登记本体 `D85488A64D89` + activation `AD42992DC75D`（沿 add_T1 §1.8 字面）
- add_T1 追加件 + activation（沿 add_T1 §1.8 字面）
- L9 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 `F6FE005EE3C7` + L10 activation `16E89657DAAA`（沿 add_T1 §1.8 字面）
- 方法预登记 `0A7BCA992B95` + 种子预登记 `113CBE555643`（沿 add_T1 §1.8 字面）
- Track 2 multimodel probe `B65619A07B10`（端点 + tun + 串行 ≥2s，只读复用）
- Track 2 endpoints probe `C846F7FC79EE`（qwen_plan / mimo / teamo 探活锚，只读复用）
- 22 caption `strip_captions_22.json` `6A2656878745`（沿 add_T1 §1.8 字面，只读复用）
- Track 2 multimodel verdict `_v4_track2_multimodel_verdict_2026_09_24.md`（6 模型补跑锚定，只读复用）

**新增条款**（仅 L14+ 立线新增）：
- **K-N26-* 五条字面** = **沿 N-26 主预登记 `0A9EE16267B5` §2 一字不动**（不构成本棒新增条款）
- **TH-L14+-1** = 单批 ≤275s（沿 L7 实证 `B8335982AE5E` ≤275s；**L7 实证锚，非本棒新设阈值**）
- **TH-L14+-2** = 拆 5-6 教师批 ≤275s / 600s watchdog 内（沿 L7 实证；**非本棒新设阈值**）
- **TH-L14+-3** = N_min ≥ 既判 N_target / 教师（沿 N-26 §2 K-N26-N1 字面；**非本棒新设阈值**）
- **TH-L14+-4** = tun 合规 100%（沿 N-26 §2 K-N26-N2 字面；**非本棒新设阈值**）
- **TH-L14+-5** = 空响应率 ≤ 50% per 教师（沿 N-26 §2 K-N26-N2 字面；**非本棒新设阈值**）

### 1.9 规模档

- **M** ≤ 30h worker 接力棒（10 cells × 单批 ≤275s × 22 批/cell + 5h × 6 批 Token Plan 配额 + 中断-恢复 ≤ 30h wall time）
- **单 worker 接力棒即可完成**（沿 L7 实证 background session ≤275s 同 session 续跑）
- 分批拆跑 ≤ 220 批（10 cells × 22 批/cell）；总 calls 实跑 ≈ 1,100 calls 理论下限

### 1.10 判定

- **productive**（沿 L9 `23879B6CD1CC` §1 productive 判例 + L10 `F6FE005EE3C7` §1 productive 判例 + add_T1 §1.10 productive 判例）

### 1.11 构造面 vs 真实面外推边界

- **构造面判定**（L14+ 构造面）：5 教师 × 22 caption × 双向 N_min ≥ 既判 N_target per 教师 + 教师 J 中位分布非退化 = 构造面 PASS；否则 FAIL
- **真实面判定**（L14+ 真实面）：跨 5 教师累加 N ≥ 既判 N_target × 5 = 真实面 PASS；否则 FAIL
- **外推边界 = V3 distill 流水线复现边界**（V3 端点名 / 参数 / 中间产物格式 = 沿 `scripts/run_v3x_*.py` 参照系，不擅自改 V3 字面）+ **数据规模边界**（≥1,100 calls / 教师 ≥110 calls / caption ≥5 calls）
- **不留假 pass**：L14+ 全 K-N26-* 不命中且 N1/N2 全 pass=True ≠ 自动 PASS（须 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程签字）
- **不留假证伪**：L14+ 任一 K-N26-* 命中 ≠ 自动 FAIL（须根因三分类每行附；沿拍板 #15）

---

## §2 L14+ 矩阵汇总统计表

| # | 维度 | 端点 | model_id | calls 下限 | 主 kill-line | 字面源 | 阈值 |
|---|---|---|---|---|---|---|---|
| 1 | 教师侧 kimi | qwen_plan + mimo + teamo | kimi（V3 端点名 / API 端点名 = kimi-for-coding） | ≥110 calls（22 caption × ≥5 calls） | K-N26-1/2/3 字面 | `0A9EE16267B5` §2 | K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 |
| 2 | 教师侧 GLM_1 | 同上 | GLM_1 | ≥110 calls | 同上 | 同上 | 同上 |
| 3 | 教师侧 GLM_2 | 同上 | GLM_2 | ≥110 calls | 同上 | 同上 | 同上 |
| 4 | 教师侧 coze | 同上 | coze | ≥110 calls | 同上 | 同上 | 同上 |
| 5 | 教师侧 minimax | 同上 | minimax | ≥110 calls | 同上 | 同上 | 同上 |
| 6 | distill 侧 kimi | 同上 | kimi | ≥110 calls | 同上 | 同上 | 同上 |
| 7 | distill 侧 GLM_1 | 同上 | GLM_1 | ≥110 calls | 同上 | 同上 | 同上 |
| 8 | distill 侧 GLM_2 | 同上 | GLM_2 | ≥110 calls | 同上 | 同上 | 同上 |
| 9 | distill 侧 coze | 同上 | coze | ≥110 calls | 同上 | 同上 | 同上 |
| 10 | distill 侧 minimax | 同上 | minimax | ≥110 calls | 同上 | 同上 | 同上 |

**矩阵汇总**：
- **10 cells / 总 calls ≥ 1,100 / 实际预计 ≥ 1,100 calls（理论下限；按需扩展）**
- **既有 K-N26-1/2/3/N1/N2 字面一字不动**（沿 `0A9EE16267B5` §2 字面）
- **每 cell per teacher J 中位分布非退化自证**（K-N26-N1 字面）
- **每 cell tun 合规**（K-N26-N2 字面）
- **总判定**：L14+ = N-26 真审唯一路径（**不预设立场**；执行后判死由 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程签字）

---

## §3 阈值来源表（逐条注明出处件 + SHA-12）

> **铁律**：本棒 L14+ **0 新设数值阈值**；所有阈值字面沿既有件引用，下表逐条核对

| 阈值符号 | 数值 | 出处件 | SHA-12 | 字面位置 |
|---|---|---|---|---|
| **K_N26_1_ACC** | 0.70 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-1 字面 |
| **K_N26_2_AUC** | 0.75 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-2 字面 |
| **K_N26_3_TEACHERS_LT** | 0.60 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-3 字面 |
| **K_N26_1_ACC** | 0.70 | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | §2 字面（沿字面） |
| **K_N26_2_AUC** | 0.75 | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | §2 字面（沿字面） |
| **K_N26_3_TEACHERS_LT** | 0.60 | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | §2 字面（沿字面） |
| **K_N26-N1 非退化自证** | N_min ≥ 既判 N_target + J 中位分布非退化 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N1 字面 |
| **K_N26-N2 tun 合规** | teamo 端点 100% 走 tun + 空响应率 ≤ 50% | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N2 字面 |
| **TH-L14+-1 单批上限** | ≤275s | `results/_v4_supp_l7_e_n20_verdict.md` | `B8335982AE5E` | §11 实证字面 |
| **TH-L14+-2 600s watchdog** | ≤600s | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §2 字面（沿 add_T1） |
| **TH-L14+-3 N_min** | ≥ 既判 N_target / 教师 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N1 字面 |
| **TH-L14+-4 tun 合规率** | 100% | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N2 字面 |
| **TH-L14+-5 空响应率上限** | ≤ 50% per 教师 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §2 K-N26-N2 字面 |
| **TH-14 5 教师锚定** | kimi / GLM_1 / GLM_2 / coze / minimax | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-14 |
| **TH-15 seed** | 42 | `results/_v4_N09_N39_prereg_2026_09_23.md` | `0A9EE16267B5` | §0 TH-15 |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l2_n11supp_verdict.md` | `E433A06E7BFB` | §2 INTER_CALL_SLEEP_S |
| **INTER_CALL_SLEEP_S** | ≥ 2.5s | `results/_v4_supp_l14_n11full_verdict.md` | `764F24A21AC8` | §2 INTER_CALL_SLEEP_S |
| **teamorouter tun 代理** | `http://127.0.0.1:1018` | `results/_v4_v5_multimodel_probe.py` | `B65619A07B10` | L35 tun proxy 段 |
| **teamorouter 必走 tun 防封号** | （硬纪律） | PI 2026-09-23 拍板 + user memory 2026-09-23 | — | user memory 「teamorouter/openrouter 必走 tun 代理防封号」 |
| **max_tokens 修正** | 2000（上调规避 L4 触顶） | `results/_v4_supp_l4_n26re_verdict.md` | `74B5B37F7EEA` | §2 字面（构造失灵族补构造，非擅调阈值） |
| **22 caption** | `strip_captions_22.json` | `corpus/v20_caption_surface/strip_captions_22.json` | `6A2656878745` | — |
| **qwen_plan endpoint** | （沿 Track 2 endpoints probe `C846F7FC79EE`） | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **mimo endpoint** | `token-plan-cn.xiaomimimo.com/v1` | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **mimo model_id** | `mimo-v2.6-pro` | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **teamo endpoint** | `api.teamorouter.cn/v1` | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |
| **teamo model_id** | `deepseek-v4-flash` | `results/_track2_endpoints_probe_2026_09_23.json` | `C846F7FC79EE` | §0 端点探活 |

> **0 新设数值阈值声明**：L14+ **0 新设数值阈值**；K-N26-1/2/3/N1/N2 五条**完全沿** `0A9EE16267B5` §2 字面；阈值 0.70 / 0.75 / 0.60 / 0.275 (s) / 600 (s) / 50% 一字不动；本棒 0 触既有字面

---

## §4 边界声明（复述）

- **本稿生效即锁**（沿 `0A9EE16267B5` + `74B5B37F7EEA` + `E105EC1362DB` + `B8335982AE5E` + v0.2 `D85488A64D89` + v0.2 activation `AD42992DC75D` + add_T1 件 + add_T1 activation + L9 `23879B6CD1CC` + L9 activation `5C579F28634E` + L10 `F6FE005EE3C7` + L10 activation `16E89657DAAA` 锁先例）；**事后不重开不调**
- **本稿是预登记追加件，不是执行件**——执行由 worker 接力棒跑，判死由 verdict-keeper 裁因，证据链由 evidence-auditor 审（沿 8 agent 团队分工：**protocol-keeper 立线 → worker 拆批跑 → verdict-keeper 裁因 → evidence-auditor 审链** 四段闸门字面化）
- **本稿 0 触 N-26 主预登记 `0A9EE16267B5` + 0 触 L4 verdict `74B5B37F7EEA` + 0 触 L4 result `065DD4393AB8` + 0 触 L13 verdict `E105EC1362DB` + 0 触 L13 executor `FF6A280BE11A` + 0 触 L7 verdict `B8335982AE5E` + 0 触 L7 runner `D5640CA314E2` + 0 触 v0.2 本体 `D85488A64D89` + 0 触 v0.2 activation `AD42992DC75D` + 0 触 add_T1 件 + 0 触 add_T1 activation + 0 触 L9 `23879B6CD1CC` + 0 触 L9 activation `5C579F28634E` + 0 触 L10 `F6FE005EE3C7` + 0 触 L10 activation `16E89657DAAA` + 0 触 Track 2 multimodel probe `B65619A07B10` + 0 触 Track 2 endpoints probe `C846F7FC79EE` + 0 触 `21771E66AF67` + 0 触 `5BA916D1DD24` + 0 触 `6A2656878745` + 0 触 V3 distill 流水线参照系 `scripts/run_v3x_*.py`** —— V1–V3 + V4 frozen 全栈 0 触动
- **本稿 0 触 V1–V3 资产**（letters/ / corpus/ / docs/ / deposon_team/ / verifier/ / attacks/ / scripts/ 全树只读）+ 0 触 R5 V4 frozen
- **派生 JSON 不合并**（本棒产物用 `_v4_supp_l14v3_*` prefix 分列，与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` + `_v4_supp_t1_*` 同级独立）
- **R4 key 永不明文**（**无例外**）+ **R6 P-G v0/v01 不动** + **R7 plugin spec 不动**
- **§0.5 过渡声明 1 件**：**L14+ N-26 真审唯一路径定位过渡**（N-26 v1/v2 既定 FAIL · 构造不可行 · 缺教师侧配对不动 + L14+ 执行前不预设立场）；**不动 v0.2 §0.5 既有 3 件 + L9 §0.5 既有 3 件 + L10 §0.5 既有 2 件 + add_T1 §0.5 T1 稳健性探针定位过渡 1 件**
- **0 触既有 K-N26-1/2/3/N1/N2 字面**（沿 `0A9EE16267B5` §2 一字不动）
- **0 新设数值阈值**（K_N26_1_ACC = 0.70 / K_N26_2_AUC = 0.75 / K_N26_3_TEACHERS_LT = 0.60 沿字面不动；TH-L14+-1~5 均为字面引用 L7 实证与 K-N26-N1/N2 字面，非本棒新设）
- **L14+ 定位硬约束**：N-26 真审唯一路径，**改判须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程**（沿 L4 verdict `74B5B37F7EEA` §11 既定结论一字不动）

---

## §5 根因三分类 + 真受审标准（沿拍板 #15）

> **诚实 = 不误导**（沿 PI 2026-09-23「诚实的根因是不误导」口径）；如实记录只是「机械诚实」，不合格

### 根因三分类

1. **真证伪**（命题被证伪）→ 命题 FAIL；**记录实验结论 + 根因（命题失败）**
2. **假证伪（工具·构造失灵族）** → 工具/构造失灵致命题未真正被证伪；**记录根因（工具失灵）+ 复评条件**（重跑/补构造后可达真证伪）
   - **构造不可行**（一等结论，归假证伪族）：构造域不可达命题要求（如 K-N26-N1 N_min < 既判 N_target）
3. **命题不明**（构造不可逃） → 构造退化致命题不可证伪；**记录构造退化 + 命题暂不明**（补构造/扩规模后可达真证伪）

### 真受审标准

- **不留假证伪**：构造失灵被误归为「命题 FAIL」= 不合格诚实
- **不留假 pass**：构造退化被误归为「命题 PASS」= 不合格诚实
- **每判定附根因列**（沿拍板 #15）；无根因分析的结论呈报 = 不合格
- **L14+ 探针根因列特别要求**：
  - **K-N26-1/2/3 命中** → 根因列必须区分三源（教师准确率命中阈值 / AUC 二分类能力低 / 多数教师准确率未达阈值）；不可笼统归「真证伪」
  - **K-N26-N1 命中（pass=False）** → 根因列必须说明「N_min 不足 / J 中位分布退化（n_distinct<3 常量 / 二值 / 派生 / 码本坍缩 / 单调构造致判据恒真族）」；不可笼统归「构造退化」
  - **K-N26-N2 命中（pass=False）** → 根因列必须区分三源（teamo 端点未走 tun / 空响应率 > 50% / max_tokens 触顶）；不可笼统归「工具失灵」
  - **K-N26-* 全不命中且 N1/N2 全 pass=True** → 根因列必须说明「V3 distill 整链重跑复现下 N-26 命题维持 PASS 方向 + 跨教师 + 跨端点 + 双向（teacher + distill）稳健」，**不构成 N-26 既判 PASS 的新证据**（仅是既判方向的稳健性确认）
  - **partial completion**（10 cells 未跑完撞 5h 配额）→ 根因列必须明示「L14+ 部分完成 + 缺 cells 留待 worker 接力棒续跑」

### L14+ 探针与 N-26 既判的根因关联

| L14+ 结果 | N-26 既判影响 | 根因列 |
|---|---|---|
| **K-N26-1/2/3 任一 hit=True**（真证伪触发） | N-26 真审真证伪（与 v1/v2 方向可能一致或新方向） | 根因 = 命题失败；记录 K-N26-1/2/3 触发维度 |
| **K-N26-N1 pass=False**（构造失灵） | N-26 真审构造不可行 / 命题不明 | 根因 = N_min 不足 / J 中位分布退化族；记录补构造路径 |
| **K-N26-N2 pass=False**（tun 不合规） | N-26 真审构造失灵 / 工具失灵族 | 根因 = teamo 未走 tun / 空响应率 > 50% / max_tokens 触顶；记录工具失灵修正条款 |
| **全 K-N26-* 不命中且 N1/N2 全 pass=True** | N-26 真审 PASS（须 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程签字） | 根因 = V3 distill 整链重跑复现下 N-26 命题维持 PASS 方向 + 跨教师 + 跨端点 + 双向稳健 |
| **partial completion**（撞 5h 配额） | 0 影响（N-26 既判不动） | L14+ 部分完成注记；缺 cells 留待接力 |

> **铁律**：L14+ 字面引用 K-N26-* = 沿 `0A9EE16267B5` §2 一字不动；**N-26 既判一字不动是默认状态**；**改判须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程**

---

## §6 自验清单（沿任务自验清单）

- [x] L14+ 10 cells 矩阵全部有独立 K-* 字面（§1.5 + §2 汇总表）
- [x] 全部口径可回溯到派工单原文 + 既有预登记件 + N-26 主预登记 `0A9EE16267B5` §2 字面（§1.3 claim + §3 阈值来源表）
- [x] kill-line 字面风格与既有预登记逐字对齐（K-N26-1/2/3/N1/N2 沿 `0A9EE16267B5` §2 一字不动；K-N26-* 五条 0 新设数值）
- [x] 判定布尔显式方向（hit=True 触发 / pass=True 存活 / K-N26-* hit=True 真证伪 / K-N26-N1/N2 pass=False 构造失灵）—— 沿 S-40 教训「禁裸 bool」
- [x] key 形态自扫 0 命中（§0 自扫结果）
- [x] 调用预算与节制硬约束写明（§1.6 单批 ≤275s / 总 ≥1,100 calls / 总 wall time ≤30h）
- [x] 产物链 `_v4_supp_l14v3_*` 命名预定（§1.7 executor / result / verdict 三件）
- [x] 阈值来源表逐条注明出处件 + SHA-12（§3 25 条阈值引用）
- [x] 工具失灵修正条款写明（§1.4 max_tokens 2000 + teamo reasoning-only 空响应重试口径）
- [x] 派生 JSON 不合并声明（§1.7 + §4 边界）
- [x] 四段闸门字面化（§4「protocol-keeper 立线 → worker 拆批跑 → verdict-keeper 裁因 → evidence-auditor 审链」）
- [x] 判定表每行根因三分类（§5 L14+ 探针与 N-26 既判的根因关联表）
- [x] 报告记诞生 SHA-12 + 大小（§7 报告）

---

## §7 报告（诞生即记）

- **本稿路径**：`results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`
- **SHA-12 / 字节 / 行数**：见 **RESULT 报告**（harness 外部汇报段）—— 文件内嵌 hash 会触发 self-reference 递归不一致（沿既有 3 件预登记件 `113CBE555643` / `0A7BCA992B95` / `0A9EE16267B5` + v0.2 + activation + L9 / L10 / add_T1 追加件均不自指 hash 的惯例）；本稿**生效件冻结 = 末态文件 hash**（PI 复核生效后冻结入 V4 manifest 链）；文件落地末态 hash 与大小以 RESULT 报告为准
- **锚定 N-26 主预登记 `0A9EE16267B5`**：命中（N-26 主预登记**一字不动**）
- **锚定 L4 verdict `74B5B37F7EEA` + L13 verdict `E105EC1362DB` + L7 verdict `B8335982AE5E`**：命中（三件**一字不动**）
- **锚定 v0.2 本体 `D85488A64D89`**：命中（v0.2 本体**一字不动**）
- **锚定 add_T1 件 + L9 / L10 追加件**：`23879B6CD1CC` / `F6FE005EE3C7` 命中（L9 / L10 / add_T1 **一字不动**）
- **派工单**：2026-09-24 protocol-keeper follow-up 起草「L14+ V3 整链重跑预登记——N-26 真审唯一路径（即锁）」（PI 拍板待复核生效）
- **生效后状态**：沿 `0A9EE16267B5` + `74B5B37F7EEA` + `E105EC1362DB` + `B8335982AE5E` + v0.2 `D85488A64D89` 锁先例 → **生效即锁**，事后不重开不调
- **key 形态自扫**：本稿 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` 三种 key 形态**0 命中**（自扫沿 §0 边界声明）
- **派生 JSON 不合并声明**：本棒产物用 `_v4_supp_l14v3_*` prefix 分列（**line 命名建议**：`_v4_supp_l14v3_executor.py` + `_v4_supp_l14v3_result.json` + `_v4_supp_l14v3_verdict.md`）；与现有 `_v4_supp_l1-l14_*` + `_v4_supp_a1/a2/b/cd/d/e_*` + `_v4_supp_t1_*` 同级独立
- **L14+ 定位硬约束再声明**：**N-26 真审唯一路径（V3 distill 整链重跑复现 + 采集阶段同步保四元组）**，**改判须走 verdict-keeper 裁因 + evidence-auditor 审链 + PI 复核完整流程**（沿 L4 verdict `74B5B37F7EEA` §11 既定 FAIL · 构造不可行一字不动）

---

## §8 老实交代（failures & limitations）

- skill `scientific-research-workflows:experimental-design`（plugin @scientific-research-workflows，sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb）本地加载器多次实录 `Local skill not found` —— **未编造 skill 不存在的虚构指令**，按既有 4 件 N-26/L4/L13/L7 锚定件（`0A9EE16267B5` + `74B5B37F7EEA` + `E105EC1362DB` + `B8335982AE5E`）+ v0.2 `D85488A64D89` + add_T1 件 + L9 `23879B6CD1CC` + L10 `F6FE005EE3C7` + 方法预登记 `0A7BCA992B95` + 种子预登记 `113CBE555643` 字面锚执行
- **本稿 = 预登记立线件，非执行件**——执行由 worker 接力棒跑，10 cells 矩阵实跑预计 ≥1,100 calls（理论下限），撞 5h 配额分批拆跑 + 中断-恢复（沿 L14 verdict §9.1 + L7 实证 ≤275s 先例）
- **L14+ 拆 5-6 教师批 ≤275s / 600s watchdog 内**（沿 L7 实证 `B8335982AE5E` ≤275s）
- **L14+ 0 新设数值阈值**；K-N26-1/2/3/N1/N2 沿 `0A9EE16267B5` §2 字面不动
- **L14+ 工具失灵修正条款**：max_tokens 2000（沿 L4 verdict §2 构造失灵族补构造）+ teamo reasoning-only 空响应重试口径（沿 V3 distill 流水线实测）
- **N-26 主预登记 `0A9EE16267B5` + L4 verdict `74B5B37F7EEA` + L13 verdict `E105EC1362DB` + L7 verdict `B8335982AE5E` 四件盘上已清出**：inventory `_v3_v4_achievements_inventory_3dir_2026_09_24.md` L800/L1075/L1179 + ledger `_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` L188/L208/L282 锁定 SHA-12 + 字节 + 落地时间；本棒沿四件 SHA-12 字面引用为权威锚源（沿 add_T1 §9 L14 verdict 漂移披露模式：「字面引用锚定 SHA = 字面引用件自报值」），**不擅自以盘 SHA 替代字面引用值**
- **本棒 0 触 22 件既有件**（N-26 主预登记 + L4 verdict + L4 result + L13 verdict + L13 executor + L7 verdict + L7 runner + v0.2 本体 + activation + add_T1 件 + activation + L9 / L10 追加件 + activations + Track 2 件 + 度量函数 + 22 caption + V3 distill 流水线参照系 —— 详见 §4 边界声明）
- **派工单「5 件必带」(agent 名 + skill 名 (sha256 611965fcb620...) + plugin 名 (@scientific-research-workflows) + 7+9 铁律 + 老实交代 0 产物) 全收**
- **skill 诚实交代**：本棒缺 skill，按既有预登记件 + L4/L13/L7 verdict + 派工单字面执行；**未编造 skill 不存在的虚构指令**

---

## §9 SHA 漂移诚实披露（沿 add_T1 §9 + E-9 / E-16 模式，立线即报）

> 本节为「**锚定 SHA 引用字面 vs 盘 SHA 漂移披露**」专项诚实交代，沿 V3 asset erratum §5 E-9 / E-16 同口径（SHA-12 漂移模式）—— 立线即报，不修任何既有件字面，仅披露漂移事实

### §9.1 N-26 主预登记 + L4/L13/L7 verdict 四件盘上已清出披露

- **N-26 主预登记 `results/_v4_N09_N39_prereg_2026_09_23.md`**：
  - **字面引用 SHA-12**：`0A9EE16267B5`（60,530 B，inventory L800 锁定）
  - **盘上状态**：**已清出**（2026-09-24 cleanup manifest 处置后；2026-09-24 落地时间 11:34:08）
  - **漂移源**：非 L14+ 引入；系 V4 maindir cleanup 处置（沿 `_v4_maindir_cleanup_manifest_2026_09_24.md`）
  - **L14+ 字面引用沿用 `0A9EE16267B5`**（沿项目「引用锚定 SHA = 字面引用件 §0 自报值」的惯例）
- **L4 verdict `results/_v4_supp_l4_n26re_verdict.md`**：
  - **字面引用 SHA-12**：`74B5B37F7EEA`（16,365 B，ledger L208 锁定）
  - **盘上状态**：**已清出**（2026-09-24 落地时间 12:18:33）
  - **L14+ 字面引用沿用 `74B5B37F7EEA`**
- **L13 verdict `results/_v4_supp_l13_n26pair_verdict.md`**：
  - **字面引用 SHA-12**：`E105EC1362DB`（23,120 B，ledger L188 锁定）
  - **盘上状态**：**已清出**（2026-09-24 落地时间 14:15:28）
  - **L14+ 字面引用沿用 `E105EC1362DB`**（注：派工单写「3f9c6a37f1e9」与盘 ledger `E105EC1362DB` 不一致；以 ledger 字面 SHA 为准）
- **L7 verdict `results/_v4_supp_l7_e_n20_verdict.md`**：
  - **字面引用 SHA-12**：`B8335982AE5E`（6,424 B，ledger L282 锁定）
  - **盘上状态**：**已清出**（2026-09-24 落地时间 12:56:18）
  - **L14+ 字面引用沿用 `B8335982AE5E`**

### §9.2 其他引用件 SHA 自洽披露

- **v0.2 预登记本体 `D85488A64D89`**：自报 = `D85488A64D89`（42,764 B）；盘实测 = 沿 add_T1 §9.3 匹配 ✓
- **add_T1 件**：本棒未实测（仅引用 §0 输入件 SHA-12 链字面）；add_T1 件落盘报值 48,738 B
- **add_T1 activation 件**：本棒未实测（仅引用 §0 输入件 SHA-12 链字面）；activation 落盘报值 14,234 B

### §9.3 处置建议（不擅自处置，留 PI 裁定）

- **四件盘上清出**（N-26 主预登记 + L4 verdict + L13 verdict + L7 verdict）：
  - 选项 A：保留现状（四件清出状态；L14+ 字面引用沿用自报 SHA；漂移作已披露事实入勘误链）
  - 选项 B：四件 reconciliation 致 SHA 漂移后入锁（需 PI 授权 + evidence-auditor 下一轮 reconciliation）
  - 选项 C：L14+ 字面源改引用 ledger SHA（需重新跑 `Get-FileHash` 验证 L14+ §0 输入件链 + §3 阈值来源表 + §4 边界声明 三处引用值）
  - **本棒不擅自选 A/B/C** —— 留 PI 裁定（沿「不动既有件字面」+「0 擅自合并派生 JSON」+「PI 复核生效时定夺」原则）
- **派工单「3f9c6a37f1e9」与 ledger `E105EC1362DB` 不一致披露**：
  - 派工单 SHA-12 = `3f9c6a37f1e9`；ledger 字面 SHA = `E105EC1362DB`（23,120 B，落地 14:15:28）
  - **本棒以 ledger 字面 SHA `E105EC1362DB` 为准**（沿项目「字面引用锚定 SHA = 字面引用件自报值」惯例，ledger 是字面件 SHA-12 权威源）
  - **派工单 SHA 错误留 PI 裁定**（不擅自改派工单字面；仅披露漂移事实）

### §9.4 漂移模式与已知 E-* 注释对齐

- **漂移模式 = SHA 漂移**（沿 E-9 `da517c1153c` 11 hex vs `da517c115f3c` 12 hex 漂移 + E-16 报告写 `da517c1153c` vs 盘实算 `da517c115f3c` 漂移 + add_T1 §9.1 L14 verdict 漂移）
- **本棒漂移是同一类型**（派工单 SHA `3f9c6a37f1e9` vs ledger SHA `E105EC1362DB`），但本棒**不擅自判定 E-30 编号** —— E-30 编号由 evidence-auditor 在下一轮 reconciliation 时定夺
- **诚实声明**：L14+ 立线件字面源引用沿「字面自报 SHA」惯例；SHA 漂移不阻 L14+ 立线件生效，但**生效件冻结时**应复核 L14+ 字面源 SHA（如届时 reconciliation 致 SHA 漂移已定，L14+ 字面源应同步 reconcile）

### §9.5 L14+ 立线件 0 触发任何 SHA 漂移

- **L14+ 立线件 SHA 漂移自检**：L14+ 立线件本身不存在自报 SHA（沿既有惯例不自指 hash；§7 报告段「见 RESULT 报告」引用 harness 外部汇报段）
- **L14+ 立线件 0 触 22 件既有件**：N-26 主预登记 + L4 verdict + L4 result + L13 verdict + L13 executor + L7 verdict + L7 runner + v0.2 本体 + activation + add_T1 件 + activation + L9 / L10 追加件 + activations + Track 2 件 + 度量函数 + 22 caption + V3 distill 流水线参照系 —— 0 触动（四件盘 SHA 漂移非 L14+ 引入）
