# deposon V3 终稿数字事实核验包（Bob 只读实测版）

- **执行**: 鲍勃-实验分析师（本轮全部只读核验，挂载仓零写入/零移动/零重命名）
- **时点**: 2026-09-18 03:10–03:4x CST
- **挂载仓**: `/home/z/my-project/upload/mount_agent_directory/deposon-repo/`（对应委托信中 `_repo_mirror/`）
- **方法**: 每一个数字均对回挂载仓一手文件（JSON/MD/代码/锚文件）读取 + SHA-256 前 12 位（SHA-12）本轮实算；零推断；核不到即标 pending（本轮 **无 pending 项**）
- **委托信本体**: `results/_letter_to_coze_paper_v1_委托_2026_09_17.md`，208 行，SHA-12 `6d72e74b3482`，在位
- **用途**: 查理撰写终稿的唯一数字依据（只报事实，不作内容判断）

---

## ① 委托信 3 处必改项正确值

| # | 断言（必改项） | 正确值（本轮实测） | 一手源文件 | 指纹(SHA-12) |
|---|---|---|---|---|
| 1 | 87.0% → 85.0% | **60 cells 51/60 = 85.0%**：existing_30（T=25/R=5）+ new_30（T=26/R=4）→ total_60 T=51/R=9/A=0，residual=0，T_frac60=51/60=85.0%（机读值 pass_rate_60=0.85，verdict STRONG_PASS） | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` §2.1<br>`results/deposon_v3_v7_summary_2026_09_11.json` phase_1 | `977fe1b48f75`<br>`063ac8d00542` |
| 2 | Adendum 13 → 17 | **17 个**（仓库实测三种口径，全部 = 17）：<br>① 文件口径：`results/_adendum_{{A..Q}}_*.json` 唯一字母 **A–Q 共 17 个**（B/C/D/E/F/G/K/M/N/O 存在 v2 重跑双版本，按最新计）<br>② 状态口径：**11 PASS + 2 GRAY(H,O) + 1 UNVERIFIED(A) + 2 PARTIAL(F,G) + 1 FAIL_NO_MODEL(K) = 17**（逐件读 verdict 实测：B/C/D/E/I/J/L/P/Q=PASS，M=PASS_for_death_theorem，N=PASS_for_pn_death，H=GRAY，O=GRAY，A=UNVERIFIED，F=COMPLETED(2/3 model)，G=FAIL_EXPOSURE_PARTIAL，K=FAIL_NO_QWEN3_MODEL）<br>③ 成本口径：**10 零成本 + 7 中成本 = 17**（中成本 7 项 = B/C/D/E/M/N/O，见 7 项中成本综合报告标题） | 17 个 `_adendum_*.json` 逐件<br>`results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md`（"7 项中成本 (B/C/D/E/M/N/O)"） | 逐件指纹见附录 B<br>`54859cf2217a` |
| 3 | P2 强稳健 → 降格 | **P2 仅 3/5 backbone 完整**：qwen3/glm53/mistral 各 30/30、β CI pairwise overlap **3/3 TRUE**（P2 PASS）；doubao-seed-2.0-lite **10/30 INCOMPLETE**（cell 11 后 server hang >9 min）；GPT-4o **UNAVAILABLE**（TeamoRouter DNS 不可达 + OpenRouter 403）。**OR×OR β CI overlap 1/6 TRUE（5 FALSE）→ verdict "GRAY (some β CI 不重叠)"**。Trae 8 章双审建议措辞：`P2 PASS（β CI 3/3 重叠，mistral/qwen3/glm53；doubao 10/30 INCOMPLETE + GPT-4o UNAVAILABLE；β 为 cell-level 代理斜率）` | `results/_p_l_v3_phase2_beta_summary_20260917_142748.json`<br>`results/_p_l_v3_phase2_report_20260917_142748.md`（L27/L95）<br>`results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json` | `86d4cb146241`<br>`58e15c07af33`<br>`21c9f23699a8` |

**旧错误值出处（供查理对照）**：`87.0%` 与 `Adendum 13 PASS + 2 GRAY/UNVERIFIED + 1 FAIL_NO_MODEL`（13+2+1=16）仅存于 `results/_d7_external_advisor_〔IM〕_publish_v1_20260918.md` L32/L152 及委托信转述；挂载仓全部一手数据文件均为 51/60=85.0% 与 17 项。

---

## ② 4 挂点结论全数字

| 断言 | 正确值（本轮实测） | 一手源文件 | 指纹(SHA-12) |
|---|---|---|---|
| 540/540 账全轧平 | 9 model × 60 cells = 540：T540=384 + R540=78 + A540=78 = 540，residual=0（整数守恒，9/9 model 全 PASS 守恒） | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` §2.2 | `977fe1b48f75` |
| 双主线 26/30 精确重合 | glm-5.3 T=26/30（T_frac 0.867）；doubao-seed-2.0-lite T=26/30（T_frac 0.867）；merged T_frac=0.8667 | `results/deposon_v3_v7_summary_2026_09_11.json` phase_2_dual_mainline | `063ac8d00542` |
| 0.867 均衡带 | 均衡带定义 T_frac∈[0.80,0.90]；exact_equilibrium_score=0.867；带内 2 model（doubao-seed-2.0-lite、glm-5.3 各 0.867） | 同上 v3_equilibrium_band | `063ac8d00542` |
| β CI 0.0016–0.0029 极窄 | 该数值域实测对应 **豆包 vision 族 4 端点 β CI：[-0.0029261, -0.0015507]**（241215: [-0.0029008,-0.0015507]；250328: [-0.0029261,-0.0015719]；250615: [-0.0029161,-0.0015815]；251215: [-0.0029261,-0.0015918]；绝对值域 ≈0.0016–0.0029，qwen3-emb-4b 交叉架构对照 [-0.0024525,-0.0001876]）。注意：**开源 3 backbone（qwen3/glm53/mistral）β CI 实测为 [-0.0369, +0.0001] 域**，与 0.0016–0.0029 不同域（挂点 1 原文表述见附录 A-5） | `results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json`<br>`results/_p_l_v3_phase2_beta_summary_20260917_142748.json` | `e3dccddaed87`<br>`86d4cb146241` |
| KT-D0 主锚 03C6C01F3697 | 锚文件 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 本轮实算 SHA-12 = **03c6c01f3697**（一手源为小写；信/D7 报告写大写 03C6C01F3697，十六进制不区分大小写，同值） | `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（6680 B，挂载仓在位） | `03c6c01f3697`（即锚文件自身指纹） |
| b3 root 75596bbabdb8 | chain_summary.b3_merkle_root = **75596bbabdb8**；independent_rewalk_ok=true | `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | `b5873afb9d29` |
| 锚链 c4cae1ed9ee5 | integrity.anchor_sha256 = **c4cae1ed9ee5**43a1…（前 12 位 c4cae1ed9ee5）= SHA-256("7d6d3d39fad8\|f88d855aaf83\|e66e44e63f5a")[:12]，与 P-F V0.1 5 锚 canonical 中 PF_BOSS_03_merkle 值逐字符一致（交叉确认） | 同上 + `docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` L107 | `b5873afb9d29`<br>`7f1492fbe657` |
| 22 caption 22/22 | b3 链 chain_pass_count = **22/22**；P-D V0.3 实测 per_caption 22 条，dual_24bit 与 KIMI 双指纹逐条一致 **22/22**（本轮程序化逐条比对）；id_correspondence verdict=PASS；caption 22 个 ID 顺序清单见 JSON | `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json`<br>`results/_p_d_v03_22caption_verification_20260917_163757.json` | `b5873afb9d29`<br>`dfbcc5d6fc34` |

---

## ③ P-L v3 三态

| 断言 | 正确值（本轮实测） | 一手源文件 | 指纹(SHA-12) |
|---|---|---|---|
| Phase 1 R²=0.7447 / Q=0.1929 FAIL | R²=**0.7447**（阈值 ≥0.9，FAIL）；归一化残差 Q=**0.1929**（阈值 >0.15 FAIL，0.05–0.15 GRAY）；综合 verdict=FAIL；载体=Mistral Large 2512 单 backbone，尺寸 30/45/100（Spearman L=30=0.3750 PASS） | `results/_p_l_v3_phase1_report_20260917_132341.md`（L13/L68/L91/L184-185/L221） | `b41a17eda169` |
| Phase 2 β CI overlap 3/3 开源 | glm53 β=[-0.0262,+0.0080]；qwen3 β=[-0.0369,+0.0001]；mistral β=[-0.0315,-0.0033]；3 对 overlap 全 **true**，verdict "PASS (β CI 重叠)"（n_cells=30 each，n_boot=1000） | `results/_p_l_v3_phase2_beta_summary_20260917_142748.json` | `86d4cb146241` |
| Phase 2 β CI overlap 3/3 闭源 | gpt-5.6-sol β=[-0.027453,+0.006577]；claude-sonnet-5 β=[-0.039812,-0.001869]；gemini-3.7-flash β=[-0.030946,-0.002754]；3 对 overlap 全 **True**，verdict "PASS (β CI overlap for closed 3)"（= 加速器 v2 retry 产物） | `results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json` | `a3eafaf9ba03` |
| OR 1/6 GRAY | 4 OR embedding（qwen3-emb-8b [0.00147,0.00430] / bge-large [0.000245,0.002217] / e5-multi [-0.001073,-0.000445] / gte-large [-0.000333,0.000176]）6 对两两比对 **1 true + 5 false**，verdict "GRAY (some β CI 不重叠)" | `results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json`（+ 同名 report MD §3 表） | `21c9f23699a8` |
| P-K FPR 4.4% = 2/45 | FPR=**0.044444…**（=2/45，即 4.4%）；threshold "FPR<1/100" 未过（false）；三方构成 own=26/GLM=23/KIMI=22，foreign 合计 45；confusion matrix glm_to_own=**2**（2 件 GLM JSON 被判自家）、glm_to_foreign=21、kimi_to_own=0；SP_t=1.0、FNR=0.0 | `results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json`<br>`results/_adendum_O_pk_v2_three_way_v2_20260917_133852.json` | `05ff758ae921`<br>`a30ff093305d` |

---

## ④ 资产层

| 断言 | 正确值（本轮实测） | 一手源文件 | 指纹(SHA-12) |
|---|---|---|---|
| 8 worker 状态 5 done + 1 failed + 2 done | **"1 failed 豆包旧版"实锤**：`_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json` status = **"INCOMPLETE - no embedding endpoint available"**（4 类 endpoint 全 REJECTED；另 doubao-seed-2.0-lite chat 通道 10/30 INCOMPLETE）。**"2 done"实锤**：豆包补测 v2（172206：6 端点中 **5/6 EMBEDDED** + 1 FAILED= doubao-embedding-text-240715 UnsupportedModel 404）＋加速器 v2（175544：3 闭源 3/3 30/30，β CI overlap 3/3 PASS）。**计数事实**：委托信 §0 称 "8 worker（5 done+1 failed+2 done）"；Trae 聚合表 §3 表头亦写 "8 worker 全部完成"，但表体实列 **9 行 bg task**：bg_23aa1031 / bg_f2fd0574 / bg_3e071c03 / bg_224d01a6 / bg_f688bdba / bg_a93672e9 / bg_a87339c8 / bg_62ffa890 / bg_6c848f0c（两处口径出入如实并列，不作判断） | `results/_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json`<br>`results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json`<br>`results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json`<br>`results/_trae_5audit_aggregated_2026_09_17.md` §3 | `b9488e2b01ae`<br>`e3dccddaed87`<br>`a3eafaf9ba03`<br>`43265e4bf2be` |
| 18 frozen | 18 frozen 复算（2026-09-16T23:32）：all_results **18 条、18 PASS、0 fail、0 missing**（summary: total=18/pass=18/fail=0/missing=0）；iron_7_compliance no_18_frozen_touch=true | `results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json` | `928794710241` |
| 5 制品 SHA-12 | 本轮逐件实算，**5/5 全部命中**：<br>KIMI `efe05ad775de` = `corpus/v20/by_model/kimi/index_v2_2026_09_16.json`<br>GLM_1 `268ab1239a8a` = `corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json`<br>GLM_2 `39732a92b5c9` = `corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json`<br>coze `fee04170aa73` = `corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json`<br>minimax `9e1ccbdceacc` = `corpus/v20/by_model/minimax/artifact_v_2026_09_16.json` | `corpus/v20/by_model/*`（5 件，全在位） | 各值即左列（实测=声明值） |
| schema v1 21/21 | `_v3x_frozen_schema_v1.json`（schema_version=1.0）：**16 文件锚 + 5 P-G 锚 = 21 枚，本轮全量复算 21/21 MATCH**——16 文件锚逐件实算全一致（KT_ABC1=03c6c01f3697 / KT_A1 78b71d404366 / KT_B1 0410ca0fbdae / KT_C1 59d8f56347d5 / KT_D0 cce8e9a1b00e / P_F_V0_1_UPGRADE b10fae0da66d / v19 910c4333eead / v21 9d9ae5001c57 / corpus_v20_index 8423ffe266af / P_F_PREDECISION b41c98bf90cc / P_F_SPEC_V0 de90faf362c5 / P_F_RESEARCH 98085df7811a / skill_a–d 4 枚）；5 P-G 种子占位锚 sha256("P_G_V0_PLACEHOLDER_{id}_2026_09_15")[:12] 逐枚复算 5/5 一致。schema 文件自身 SHA-12=`9e99dcc4d920`（与 Trae 审计 B1 记录一致）。注：Trae 审计称 #1/#10 仓库缺失经归档区闭合；本轮挂载仓内 16 锚文件**全部在位且一致** | `deposon_team/plugins/_v3x_frozen_schema_v1.json` + 16 个锚路径文件 | `9e99dcc4d920` |
| 4 plugin spec SHA-12 | 本轮逐件实算，**4/4 全部命中**：skill_a `b1463bb24403` / skill_b `e5a299f69a22` / skill_c `e19e76c5da7e` / skill_d `3e369a1f6171` | `deposon_team/plugins/skill_a_p_a_60cells.py` 等 4 件 | 各值即左列（实测=声明值） |

---

## ⑤ D7 终局四路径 verdict + P-G V0.1 关键数

（源：`docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` §1/§2，与 `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` 交叉一致）

| 路径 | D1-D3 verdict | D7 5 锚终极 verdict | 关键数（实测原文） |
|---|---|---|---|
| P-A 均衡稳定化 | PASS | **PASS** | 540 守恒 PASS（9/9 model residual=0）；9 model verdict **8 PASS + 1 GRAY（deepseek-v4-pro）**；BOSS-P-A1 倍数均值 145.8182×；BOSS-P-A2 PG 形式 13.6%(3/22) |
| P-C 幂律 | FAIL_H0（幂律死） | **FAIL_H0** | R²=**0.1986/0.2670 双 FAIL_H0**（log-log 拟合） |
| P-E 物理公式 + D_fix2 | PASS | **PARTIAL_PASS**（user 12:01 拍板 A 接受） | 9 model verdict **6 PASS + 2 GRAY + 1 FAIL（deepseek-v4-pro）**；D_fix2 8/1/0 分布；9m per-model Spearman(D_fix2,T_frac)=-0.832 / (D_fix2,A_frac)=+0.941；540 cells cell-level -0.986 / +0.506 |
| P-F observer | PASS | **PASS** | 9m×5c 守恒 **45/45**（T=41 R=0 A=4，residual=0）；6 fresh volcengine LLM 调用 |

**P-G V0.1 关键数**：
- d_H/d_E 放大比 **≈ 5x（range 4.4–8.0）**
- Spearman rho_H_vs_E = **1.0000**
- 5 锚 V0→V0.1 真值（5/5 PASS）：P_G_HYPERBOLIC_TRANSPORT `9c3c50005103` / P_G_CURVATURE_BOUND `8ff586b2722e` / P_G_LLM_CLIENT `0130d179059e` / P_G_HARNESS `27419597798b` / P_G_FROZEN_BENCHMARK `9205c1168e59`（与 d7 verdict JSON "V0.1 真值"逐一相同；V0 占位 230b5caee415/dcbcf2b8d45f/2c1f572aa2bf/8b90c53f1e01/91db66afecc3 同时在两源一致）
- 指纹：kill report `4ffb21bb6bfa`（8526 B）；d7 verdict JSON `4505cca79c15`

---

## ⑥ 委托信 §9 源件清单逐件在位性 + SHA 对账

**10/10 全在位；8 枚已声明 SHA 全部逐位一致；2 枚"待算"项本轮实算如下。**

| # | 文件（挂载仓相对路径） | 信中声明 | 本轮实测 | 判定 |
|---|---|---|---|---|
| 1 | `results/_trae_5audit_aggregated_2026_09_17.md` | 待算（~11,465 B） | **43265e4bf2be**，11,465 B | 待算项已闭合（字节数与信一致） |
| 2 | `docs/V3X/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md` | 53a90b9efbb9 | 53a90b9efbb9（5,154 B） | ✓ 一致 |
| 3 | `results/_trae_d7_v1_audit_20260917_190000.md` | e240ca712be6 | e240ca712be6（7,855 B） | ✓ 一致 |
| 4 | `results/_trae_kimi_push_v3_audit_20260917_193000.md` | 8ece24be6b8a | 8ece24be6b8a（3,281 B） | ✓ 一致 |
| 5 | `results/_trae_corpus_5_audit_20260917_193000.md` | f2a655cd5e54 | f2a655cd5e54（3,467 B） | ✓ 一致 |
| 6 | `results/_trae_anchor_18_audit_20260917_193000.md` | 4af67e6cbe71 | 4af67e6cbe71（3,449 B） | ✓ 一致 |
| 7 | `results/_trae_paper_8ch_双审_20260917_200000.md` | bec666969ffc | bec666969ffc（4,040 B） | ✓ 一致 |
| 8 | `results/_v3x_d0_5_aggregation_2026_09_17.md` | ddf0d1aa96d2 | ddf0d1aa96d2（12,010 B） | ✓ 一致 |
| 9 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md` | 待算 | **27db4950f710**（8,222 B） | 待算项已闭合 |
| 10 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` | c41c1d6aa794 | c41c1d6aa794（6,799 B） | ✓ 一致 |

---

## 附录 A：如实并列项（叙述层与盘面出入，只录事实、不作判断）

1. **委托信 §4 依据列算术**："零成本 7 + 中成本 6 + LLM 3 + F/G/K 1 + 豆包 1" 字面加和 = 18 ≠ 17；同表修正列 "11 + 2 + 1 + 2 + 1 = 17" 算术成立且与仓库实测状态口径一致。
2. **worker 计数**：委托信 §0 称 8 worker（5 done + 1 failed 豆包旧版 + 2 done 补测 v2 + 加速器 v2）；Trae 聚合表 §3 表头写 "8 worker 全部完成" 但表体列 9 行 bg task（含 P-D V0.3 实测 bg_a93672e9 与 OR 重试 bg_a87339c8）。
3. **委托信 §5 outline 行 "10 零成本 (7 PASS + 3 LLM done)"**：仓库实测 10 零成本中 7 件非 LLM 终态 = **5 PASS（I/J/L/P/Q）+ 1 GRAY（H）+ 1 UNVERIFIED（A）**；3 件 LLM 后派 = F（COMPLETED, 2/3 model）+ G（FAIL_EXPOSURE_PARTIAL）+ K（FAIL_NO_QWEN3_MODEL）。Trae 聚合表对应行原文为 "✅ 7 PASS/READY"。"7 中成本 (6 PASS + 1 GRAY)" 与实测一致（O=GRAY）。
4. **KT-D0 主锚大小写**：一手源小写 `03c6c01f3697`；委托信/D7 报告大写 `03C6C01F3697`（十六进制同值）。
5. **挂点 1 "3 backbone β CI 0.0016-0.0029 极窄"**：数值域 0.0016–0.0029 实测对应豆包 vision 族 4 端点 β CI（负值域，绝对值 0.0016–0.0029）；开源 3 backbone β CI 实测为 [-0.0369, +0.0001] 域。两族数值并列如上，供撰稿取数。
6. **委托信挂点 4 "7 制品"**：信 §2 挂点 4 原文写 "7 制品"；资产层可数制品（corpus/v20/by_model）为 5 件（§⑤ 核验对象）。原文照录。
7. **Adendum C 勘误**：`_adendum_C_pm_attack_surface_v2_20260917_133852.json` verdict=PASS（KIMI push 副审曾标 "detection=0.0+PASS 矛盾复发" 阻断项；`deposon_team/plugins/_fix_adendum_c_erratum_2026_09_17.py` 在位）——仅录在位事实。

## 附录 B：本轮引用一手源指纹总表（挂载仓路径 → SHA-12 / 字节）

```
docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md                    977fe1b48f75  19751B
results/deposon_v3_v7_summary_2026_09_11.json              063ac8d00542  25049B
results/_p_l_v3_phase1_report_20260917_132341.md           b41a17eda169  11035B
results/_p_l_v3_phase2_beta_summary_20260917_142748.json   86d4cb146241   2417B
results/_p_l_v3_phase2_report_20260917_142748.md           58e15c07af33   9056B
results/_p_l_v3_phase2_or_embedding_v3_summary_…162614.json 21c9f23699a8  8308B
results/_p_l_v3_phase2_closedsource_summary_…175544.json   a3eafaf9ba03   3286B
results/_p_l_v3_phase2_closedsource_report_…175544.md      02443dd300ce   5909B
results/_p_l_v3_phase2_doubao_v2_summary_…172206.json      e3dccddaed87  14469B
results/_p_l_v3_vector_embedding_doubao_L30_…142748.json   b9488e2b01ae  11834B
results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json  05ff758ae921  12992B
results/_adendum_O_pk_v2_three_way_v2_…133852.json         a30ff093305d   1970B
results/_p_l_v3_phase3_plus_adendum_7_report_…133358.md    54859cf2217a   6637B
results/_v3x_18frozen_remeasure_2026_09_16/…results.json   928794710241   4202B
deposon_team/plugins/_v3x_frozen_schema_v1.json            9e99dcc4d920  12919B
verifier/handoff/KT_ABC1_anchors_sha256_12.json            03c6c01f3697   6680B  ← 该文件即 KT-D0 主锚本体
results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json   b5873afb9d29  18104B
results/_p_d_v03_22caption_verification_…163757.json       dfbcc5d6fc34  13775B
docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_…md         7f1492fbe657  10979B
docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md               4ffb21bb6bfa   8526B
results/d7_5anchor_60cells_9model_verdict_2026_09_18.json  4505cca79c15   2456B
results/_letter_to_coze_paper_v1_委托_2026_09_17.md        6d72e74b3482  （208 行，委托信本体）
results/_d7_external_advisor_〔IM〕_publish_v1_20260918.md     ——（旧错误值 87.0%/Adendum13 出处，未计指纹）
corpus/v20/by_model/kimi/index_v2_2026_09_16.json          efe05ad775de
corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test…   268ab1239a8a
corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json   39732a92b5c9
corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json   fee04170aa73
corpus/v20/by_model/minimax/artifact_v_2026_09_16.json     9e1ccbdceacc
deposon_team/plugins/skill_a_p_a_60cells.py                b1463bb24403
deposon_team/plugins/skill_b_p_c_alpha_beta.py             e5a299f69a22
deposon_team/plugins/skill_c_p_e_3modality.py              e19e76c5da7e
deposon_team/plugins/skill_d_p_f_observer.py               3e369a1f6171
```

**Adendum 17 件逐件（最新版）指纹**：A `results/_adendum_A_degradation_precheck_20260917_132049.json`；B `…B_pi_real_labels_v2_20260917_133852.json`；C `…C_pm_attack_surface_v2_20260917_133852.json`；D `…D_pc_r2_per_model_v2_20260917_133852.json`；E `…E_pd_supplement_v2_20260917_133852.json`；F `…F_pe_3modal_v2_20260917_143033.json`；G `…G_pf_dfix2_v2_20260917_143033.json`；H `…H_pg_dhde_shrink_20260917_132049.json`；I `…I_po_captions_closure_20260917_132049.json`；J `…J_warehouse_spearman_health_20260917_132049.json`；K `…K_qwen3_087_cluster_v2_20260917_143033.json`；L `…L_verifier_dual_impl_diff_20260917_132049.json`；M `…M_pj_convergence_basin_v2_20260917_133852.json`；N `…N_pn_coupling_v2_20260917_133852.json`；O `…O_pk_v2_three_way_v2_20260917_133852.json`；P `…P_pc_two_phase_fail_h0_20260917_132049.json`；Q `…Q_deepseek_v4_pro_anchor_20260917_132049.json`（均在 `results/` 下、全在位；verdict 实测见 ①-2）。

---

**核验结论一句话**：任务清单 6 块数字全部核到、零 pending；挂载仓只读纪律全程遵守；唯一需撰稿人取数时注意的是附录 A 列出的 5 处叙述层与盘面的字面出入（均已给出两侧实测原文）。

—— 鲍勃-实验分析师 · 2026-09-18 · 只读核验 · 零写入
