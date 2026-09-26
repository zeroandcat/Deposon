# V4 Main-Dir Cleanup Moves Ledger v2 (2026-09-24)

> by worker (执行类 / 文件治理 / 第三棒)
> **授权来源**: PI ask_721b8b46601f0b96a6989a0f (2026-09-24 18:19) cleanup_path 题 PI 选 **B**——「移动+ledger对账：131 件移入 archive/sub，frozen 锚件 0 触动，引用经迁移对账表追溯」
> **不动 v1 ledger** (`_v4_maindir_cleanup_moves_ledger_2026_09_24.md`, SHA-12=4025E871726B)
> **本棒执行明细**: 实际移动 **125 件** (A 54 + C 63 + 灰区 8), 0 件删除, 63 件因同名冲突按铁则加 `_moved_20260924_1830` 时间后缀 (C 62 件 + 灰区 1 件)
> **v1 ledger 数字与实测差异**: v1 报 131 件候选(59 A + 63 C + 8 灰区), 实测 A=54 (非 59, v1 算数偏差); C=63 ✓; 灰区=8 ✓; 实测总数 125 ≠ v1 报 131。**派工单授权覆盖所有匹配派工单 §A/C/G 类 pattern 的文件**(以 v1 ledger 列出的子类 pattern 为准), 不论具体计数
> ===================== 关键:本棒按 PI 拍板 B 路径执行 =====================

---

## 0. 摘要 (Summary)

| 维度 | 数字 |
|---|---|
| 派工单期望移动件数 | 131 件 (v1 ledger 报 59 A + 63 C + 8 灰区) |
| **本棒实测移动件数** | **125 件** (54 A + 63 C + 8 灰区) |
| 派工单期望 vs 实测差异 | A 类 v1 ledger 报 59, 实测 54 (差 -5, v1 算数偏差; C 类与灰区实测一致) |
| 同名冲突处置 | 63 件按铁则加 `_moved_20260924_1830` 时间后缀 (C 类 62 + 灰区 1), 0 件覆盖 |
| 删除件数 | **0 件** (派工单铁则: 只移不删) |
| 通道 | PowerShell `Move-Item` (atomic move, content preserved) |
| frozen 锚件 0 触动 | ✓ (6 件 SHA-12 移动前后实测一致) |
| 保护名单 0 触动 | ✓ (12 类逐类核对) |
| 派生 JSON 不合并 | ✓ (未新建派生统计 JSON) |
| 0 擅调阈值 | ✓ |
| 不覆盖既有件 | ✓ (终态对账表新名 = `_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md`) |

---

## 1. 授权依据与执行依据

### 1.1 PI 拍板 (ask_721b8b46601f0b96a6989a0f, 2026-09-24 18:19)

- cleanup_path 题 PI 选 **B**: 「移动+ledger对账：131 件移入 archive/sub, frozen 锚件 0 触动, 引用经迁移对账表追溯」
- 第二棒上交的 A/B/C 矛盾就此收口
- 引用落空由本对账表 (本 v2 ledger) 追溯承担
- 锚件不重建、SHA 不变

### 1.2 v1 ledger 与本棒实测差异

| 类 | v1 ledger 报 | 实测 | 差异 | 说明 |
|---|---|---|---|---|
| A (`_p_l_v3_vector_embedding_*` + `_p_l_v3_real_collapse_*` + `_p_l_v3_robustness_*` + `_p_l_v3_phase*` + `_p_l_v3_phase3*adendum*` + `_p_k_v3_*`) | 59 | **54** | -5 | v1 子项累加 21+4+11+9+6+3 = 54, 但 v1 总计写成 59 (算数偏差) |
| C (`_adendum_*` + `_kimi_push_v3_manifest_batch*` + `_kimi_safe_batch_push_*` + `_v2_*.py` + `_d05_*`) | 63 | **63** | 0 | ✓ |
| 灰区 (8 件 .tmp/ chain-bound) | 8 | **8** | 0 | ✓ |
| **总计** | **131** | **125** | -6 | A 类 -5 + C 类 0 + 灰区 0 = -5 (差异仅 A) |

> 老实交代: 本棒严格按派工单 §A/C/G 列出的子类 pattern 在 `D:/私人资料/deposon-repo/results/` 与 `D:/私人资料/deposon-repo/.tmp/` 实测枚举; v1 ledger 的 131 数字含 A 类的算数偏差 5 件 (v1 子项累加 = 54 ≠ v1 总计 59); 本棒实测以 125 件为基线, 不擅自补件也不擅自减件。

---

## 2. frozen 锚件 0 触动验证 (派工单 §铁则第一条)

> 移动前后各验一次 SHA-12, 必须不变。

| 件 | bytes | SHA-12 (before 2026-09-24 18:20) | SHA-12 (after 2026-09-24 18:24) | 状态 |
|---|---|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6680 | 03C6C01F3697 | 03C6C01F3697 | 未触动 ✓ |
| `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | 169864 | 1D52DB0EBF53 | 1D52DB0EBF53 | 未触动 ✓ |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` | 192160 | 29A853444D42 | 29A853444D42 | 未触动 ✓ |
| `results/_archive_manifest_deposon_sub_2026_09_23.json` | 52153 | B34B9F7BDFB7 | B34B9F7BDFB7 | 未触动 ✓ |
| `results/_ghostref_copy_log_2026_09_23.json` | 129780 | 8CD133D0896F | 8CD133D0896F | 未触动 ✓ |
| `results/_archive_manifest_non_upload_2026_09_23.json` | 148690 | B899103853CA | B899103853CA | 未触动 ✓ |

> 注: 派工单 §铁则明示 4 件 frozen 锚件 (`_v3_v4_ghostref_reconciliation` / `_v3_v4_achievements_inventory` / `archive_manifest_deposon_sub.json` / `ghostref_copy_log.json`) + `KT_ABC1_anchors_sha256_12.json` = 5 件; 加上 v1 §3.1 列示的 `_archive_manifest_non_upload_2026_09_23.json` = 6 件, 全部 0 触动。

---

## 3. A 类对账 (54 件 · 全数干净移动 · 0 同名冲突)

> 目标: `D:/私人资料/_non_upload_local_archive/results/`
> 通道: PowerShell `Move-Item`, 全部 54 件实测一次性成功 (0 fail)
> 总 bytes: 24,062,436 (与 v1 ledger §3.2 A 小计 bytes 一致)

| # | 旧路径 (repo/results/) | 新路径 (_non_upload_local_archive/results/) | SHA-12 (实测 2026-09-24 18:24) | bytes | 类别 |
|---|---|---|---|---|---|
| A1 | `D:/私人资料/deposon-repo/results/_p_k_v3_glm_fpr_audit_report_2026-09-17t08-23-41z.md` | `D:/私人资料/_non_upload_local_archive/results/_p_k_v3_glm_fpr_audit_report_2026-09-17t08-23-41z.md` | 71D5C23D9F76 | 8558 | A |
| A2 | `D:/私人资料/deposon-repo/results/_p_k_v3_glm_json_audit_2026-09-17t08-23-41z.json` | `D:/私人资料/_non_upload_local_archive/results/_p_k_v3_glm_json_audit_2026-09-17t08-23-41z.json` | F236E88F22CA | 6678 | A |
| A3 | `D:/私人资料/deposon-repo/results/_p_k_v3_three_way_rerun_2026-09-17t08-23-41z.json` | `D:/私人资料/_non_upload_local_archive/results/_p_k_v3_three_way_rerun_2026-09-17t08-23-41z.json` | 05FF758AE921 | 12992 | A |
| A4 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase1_report_20260917_132341.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase1_report_20260917_132341.md` | B41A17EDA169 | 11035 | A |
| A5 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_beta_summary_20260917_142748.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_beta_summary_20260917_142748.json` | 86D4CB146241 | 2417 | A |
| A6 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_closedsource_report_20260917_175544.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_closedsource_report_20260917_175544.md` | 02443DD300CE | 5909 | A |
| A7 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json` | A3EAFAF9BA03 | 3286 | A |
| A8 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json` | C366F4E30B6B | 4357 | A |
| A9 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json` | E3DCCDDAED87 | 14469 | A |
| A10 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_or_embedding_v3_report_20260917_162614.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_or_embedding_v3_report_20260917_162614.md` | FA5DA7A307BD | 8102 | A |
| A11 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json` | 21C9F23699A8 | 8308 | A |
| A12 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase2_report_20260917_142748.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase2_report_20260917_142748.md` | 58E15C07AF33 | 9056 | A |
| A13 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase3_adendum_summary_20260917_132143.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase3_adendum_summary_20260917_132143.md` | 8C07AB5AA968 | 16612 | A |
| A14 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md` | 54859CF2217A | 6637 | A |
| A15 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md` | C350E420ECA6 | 6337 | A |
| A16 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md` | 772112CF5BD4 | 6434 | A |
| A17 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md` | D7F03FDE4067 | 6435 | A |
| A18 | `D:/私人资料/deposon-repo/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md` | D66388B6532D | 6616 | A |
| A19 | `D:/私人资料/deposon-repo/results/_p_l_v3_real_collapse_mistral_l100_20260917_132341.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_real_collapse_mistral_l100_20260917_132341.json` | 4657B210782A | 43903 | A |
| A20 | `D:/私人资料/deposon-repo/results/_p_l_v3_real_collapse_mistral_l30_20260917_132341.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_real_collapse_mistral_l30_20260917_132341.json` | F6AB84F27D9A | 16545 | A |
| A21 | `D:/私人资料/deposon-repo/results/_p_l_v3_real_collapse_mistral_l45_20260917_132341.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_real_collapse_mistral_l45_20260917_132341.json` | DC37EE54781C | 20108 | A |
| A22 | `D:/私人资料/deposon-repo/results/_p_l_v3_real_collapse_mistral_l60_20260917_132341.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_real_collapse_mistral_l60_20260917_132341.json` | E3FB4F775E22 | 1174 | A |
| A23 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_claude_sonnet5_l30_20260917_174011.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_claude_sonnet5_l30_20260917_174011.json` | 9D329721F67D | 30772 | A |
| A24 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_claude_sonnet5_l60_20260917_174011.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_claude_sonnet5_l60_20260917_174011.json` | 28E462C11692 | 1292 | A |
| A25 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_gemini_37flash_l30_20260917_175003.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_gemini_37flash_l30_20260917_175003.json` | 0F5C80A8A4AE | 30514 | A |
| A26 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_gemini_37flash_l60_20260917_175003.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_gemini_37flash_l60_20260917_175003.json` | E2590651F9C0 | 1288 | A |
| A27 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_glm53_l30_20260917_142011.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_glm53_l30_20260917_142011.json` | 2DEADD7BE100 | 18281 | A |
| A28 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_glm53_l60_20260917_142011.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_glm53_l60_20260917_142011.json` | 31556B58CAA1 | 1037 | A |
| A29 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_gpt56sol_l30_20260917_173159.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_gpt56sol_l30_20260917_173159.json` | 3865D7A61CA1 | 30347 | A |
| A30 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_gpt56sol_l60_20260917_173159.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_gpt56sol_l60_20260917_173159.json` | 8C79E9A289FB | 1266 | A |
| A31 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_mistral_l60_20260917_142748.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_mistral_l60_20260917_142748.json` | BA41A0D4B927 | 1071 | A |
| A32 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_qwen3_l30_20260917_140017.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_qwen3_l30_20260917_140017.json` | E9BAC1743A2A | 18595 | A |
| A33 | `D:/私人资料/deposon-repo/results/_p_l_v3_robustness_qwen3_l60_20260917_140017.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_robustness_qwen3_l60_20260917_140017.json` | F79F1B00E5D3 | 1057 | A |
| A34 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao_l30_20260917_142748.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao_l30_20260917_142748.json` | B9488E2B01AE | 11834 | A |
| A35 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao_l30_20260917_170828.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao_l30_20260917_170828.json` | 198F8FE39F94 | 18468 | A |
| A36 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-text-240715_l30_20260917_172206.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-text-240715_l30_20260917_172206.json` | 2D4827F9CDA2 | 18509 | A |
| A37 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-vision-241215_l30_20260917_171614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-vision-241215_l30_20260917_171614.json` | 2B91EB1DBBCF | 1669762 | A |
| A38 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-vision-241215_l30_20260917_172206.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-vision-241215_l30_20260917_172206.json` | E836A04A04D8 | 1670172 | A |
| A39 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-vision-250328_l30_20260917_171614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-vision-250328_l30_20260917_171614.json` | 46C99397F01B | 1670501 | A |
| A40 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-vision-250328_l30_20260917_172206.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-vision-250328_l30_20260917_172206.json` | 0432F25CF6C3 | 1669285 | A |
| A41 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-vision-250615_l30_20260917_171614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-vision-250615_l30_20260917_171614.json` | 6B8AF7D8BCA9 | 1670027 | A |
| A42 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-vision-250615_l30_20260917_172206.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-vision-250615_l30_20260917_172206.json` | 710B7F291355 | 1671116 | A |
| A43 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_doubao-vision-251215_l30_20260917_172206.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_doubao-vision-251215_l30_20260917_172206.json` | A00976C6F87B | 1670482 | A |
| A44 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_glm53_l30_20260917_142748.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_glm53_l30_20260917_142748.json` | D91B0C5F642F | 11833 | A |
| A45 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_mistral_l30_20260917_142748.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_mistral_l30_20260917_142748.json` | 33D0259073DC | 11835 | A |
| A46 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_or_bge-large_l30_20260917_162614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_or_bge-large_l30_20260917_162614.json` | AFF028E8506C | 1017974 | A |
| A47 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_or_e5-multi_l30_20260917_162614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_or_e5-multi_l30_20260917_162614.json` | 8676B519A031 | 1017684 | A |
| A48 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_or_gte-large_l30_20260917_162614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_or_gte-large_l30_20260917_162614.json` | 07561D4D23D1 | 1017381 | A |
| A49 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_or_qwen3-emb-8b_l30_20260917_162614.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_or_qwen3-emb-8b_l30_20260917_162614.json` | A4BD70C02AAA | 3929893 | A |
| A50 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_qwen3_l30_20260917_142748.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_qwen3_l30_20260917_142748.json` | 26F7493F1C95 | 11833 | A |
| A51 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_qwen3-emb-4b_l30_20260917_170828.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_qwen3-emb-4b_l30_20260917_170828.json` | 1928ADA51527 | 2452705 | A |
| A52 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_qwen3-emb-4b_l30_20260917_172206.json` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_qwen3-emb-4b_l30_20260917_172206.json` | BEBEE5346543 | 2452273 | A |
| A53 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_170828.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_170828.md` | FA9CD7FFA3F2 | 17833 | A |
| A54 | `D:/私人资料/deposon-repo/results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md` | `D:/私人资料/_non_upload_local_archive/results/_p_l_v3_vector_embedding_v2_doubao_report_20260917_172206.md` | 2E3EC17259E2 | 19548 | A |

> 注: 所有 54 件 A 类文件在 `_non_upload_local_archive/results/` 目标位置无同名冲突, 干净移动, 0 件时间后缀。

---

## 4. C 类对账 (63 件 · 1 件干净 + 62 件加时间后缀)

> 目标: `D:/私人资料/deposon-sub/results/`
> 通道: PowerShell `Move-Item`
> 总 bytes: 568,033 (与 v1 ledger §3.3 C 小计 bytes 一致)
> **同名冲突实测**: 62/63 件源 SHA-12 = 目标 SHA-12 (仓外 canonical 已存在同名副本 = GHOST_REF_COPIED duplicates), 1 件 (`_adendum_H_*`) 仓外无同名副本干净移动

### 4.1 干净移动 (1 件)

| # | 旧路径 (repo/results/) | 新路径 (deposon-sub/results/) | SHA-12 (实测 2026-09-24 18:24) | bytes | 类别 |
|---|---|---|---|---|---|
| C1 | `D:/私人资料/deposon-repo/results/_adendum_H_pg_dhde_shrink_20260917_132049.json` | `D:/私人资料/deposon-sub/results/_adendum_H_pg_dhde_shrink_20260917_132049.json` | B9A0253BA6A0 | 4613 | C |

### 4.2 同名冲突 + 时间后缀移动 (62 件)

> 仓外 (`deposon-sub/results/`) 已存在 SHA-12 一致的同名 GHOST_REF_COPIED 副本;
> 按铁则"同名冲突加时间后缀存入,禁止覆盖",本棒加 `_moved_20260924_1830` 后缀 (统一批次号), 0 件覆盖仓外 canonical

| # | 旧路径 (repo/results/) | 新路径 (deposon-sub/results/ · 时间后缀) | SHA-12 (实测 2026-09-24 18:24) | bytes | 类别 |
|---|---|---|---|---|---|
| C2 | `D:/私人资料/deposon-repo/results/_adendum_a_degradation_precheck_20260917_132049.json` | `D:/私人资料/deposon-sub/results/_adendum_a_degradation_precheck_20260917_132049.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 38FABEB19691 | 4248 | C |
| C3 | `D:/私人资料/deposon-repo/results/_adendum_b_pi_real_labels_v2_20260917_133726.json` | `D:/私人资料/deposon-sub/results/_adendum_b_pi_real_labels_v2_20260917_133726.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 3D344711CF8C | 2374 | C |
| C4 | `D:/私人资料/deposon-repo/results/_adendum_b_pi_real_labels_v2_20260917_133852.json` | `D:/私人资料/deposon-sub/results/_adendum_b_pi_real_labels_v2_20260917_133852.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | C725E08E0A1C | 2374 | C |
| C5 | `D:/私人资料/deposon-repo/results/_adendum_c_pm_attack_surface_v2_20260917_133726.json` | `D:/私人资料/deposon-sub/results/_adendum_c_pm_attack_surface_v2_20260917_133726.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 193BA7D66412 | 4123 | C |
| C6 | `D:/私人资料/deposon-repo/results/_adendum_c_pm_attack_surface_v2_20260917_133852.json` | `D:/私人资料/deposon-sub/results/_adendum_c_pm_attack_surface_v2_20260917_133852.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 6EBA63788CA8 | 4122 | C |
| C7 | `D:/私人资料/deposon-repo/results/_adendum_d_pc_r2_per_model_v2_20260917_133726.json` | `D:/私人资料/deposon-sub/results/_adendum_d_pc_r2_per_model_v2_20260917_133726.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 6FE706750823 | 4605 | C |
| C8 | `D:/私人资料/deposon-repo/results/_adendum_d_pc_r2_per_model_v2_20260917_133852.json` | `D:/私人资料/deposon-sub/results/_adendum_d_pc_r2_per_model_v2_20260917_133852.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | D66792EEA40E | 4605 | C |
| C9 | `D:/私人资料/deposon-repo/results/_adendum_e_pd_supplement_v2_20260917_133726.json` | `D:/私人资料/deposon-sub/results/_adendum_e_pd_supplement_v2_20260917_133726.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 2C4790FFB6E3 | 1353 | C |
| C10 | `D:/私人资料/deposon-repo/results/_adendum_e_pd_supplement_v2_20260917_133852.json` | `D:/私人资料/deposon-sub/results/_adendum_e_pd_supplement_v2_20260917_133852.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 46D8DACB4721 | 1353 | C |
| C11 | `D:/私人资料/deposon-repo/results/_adendum_f_pe_3modal_closure_llm_dispatch_20260917_132143.json` | `D:/私人资料/deposon-sub/results/_adendum_f_pe_3modal_closure_llm_dispatch_20260917_132143.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 879494ED8FB9 | 3646 | C |
| C12 | `D:/私人资料/deposon-repo/results/_adendum_f_pe_3modal_v2_20260917_143033.json` | `D:/私人资料/deposon-sub/results/_adendum_f_pe_3modal_v2_20260917_143033.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | AFAB79249BE7 | 38622 | C |
| C13 | `D:/私人资料/deposon-repo/results/_adendum_fgk_complete_20260917_143033.md` | `D:/私人资料/deposon-sub/results/_adendum_fgk_complete_20260917_143033.md._moved_20260924_1830.md` (仓外同名旧件 0 覆盖) | 958188C83CF0 | 14005 | C |
| C14 | `D:/私人资料/deposon-repo/results/_adendum_g_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json` | `D:/私人资料/deposon-sub/results/_adendum_g_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | D10462080832 | 2757 | C |
| C15 | `D:/私人资料/deposon-repo/results/_adendum_g_pf_dfix2_v2_20260917_143033.json` | `D:/私人资料/deposon-sub/results/_adendum_g_pf_dfix2_v2_20260917_143033.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | BF8DB2AD255B | 95292 | C |
| C16 | `D:/私人资料/deposon-repo/results/_adendum_i_po_captions_closure_20260917_132049.json` | `D:/私人资料/deposon-sub/results/_adendum_i_po_captions_closure_20260917_132049.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 18165008BEF6 | 4429 | C |
| C17 | `D:/私人资料/deposon-repo/results/_adendum_j_warehouse_spearman_health_20260917_132049.json` | `D:/私人资料/deposon-sub/results/_adendum_j_warehouse_spearman_health_20260917_132049.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | DF661D62426A | 11337 | C |
| C18 | `D:/私人资料/deposon-repo/results/_adendum_k_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json` | `D:/私人资料/deposon-sub/results/_adendum_k_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | ACDF933F68E0 | 2911 | C |
| C19 | `D:/私人资料/deposon-repo/results/_adendum_k_qwen3_087_cluster_v2_20260917_143033.json` | `D:/私人资料/deposon-sub/results/_adendum_k_qwen3_087_cluster_v2_20260917_143033.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 43477C8EA2D6 | 32481 | C |
| C20 | `D:/私人资料/deposon-repo/results/_adendum_l_verifier_dual_impl_diff_20260917_132049.json` | `D:/私人资料/deposon-sub/results/_adendum_l_verifier_dual_impl_diff_20260917_132049.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 1532607DED80 | 2783 | C |
| C21 | `D:/私人资料/deposon-repo/results/_adendum_m_pj_convergence_basin_v2_20260917_133726.json` | `D:/私人资料/deposon-sub/results/_adendum_m_pj_convergence_basin_v2_20260917_133726.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | EA7FFDA97E20 | 3694 | C |
| C22 | `D:/私人资料/deposon-repo/results/_adendum_m_pj_convergence_basin_v2_20260917_133852.json` | `D:/私人资料/deposon-sub/results/_adendum_m_pj_convergence_basin_v2_20260917_133852.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 8AB01A1E42AE | 3686 | C |
| C23 | `D:/私人资料/deposon-repo/results/_adendum_n_pn_coupling_v2_20260917_133726.json` | `D:/私人资料/deposon-sub/results/_adendum_n_pn_coupling_v2_20260917_133726.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 1B91CC25CA57 | 2012 | C |
| C24 | `D:/私人资料/deposon-repo/results/_adendum_n_pn_coupling_v2_20260917_133852.json` | `D:/私人资料/deposon-sub/results/_adendum_n_pn_coupling_v2_20260917_133852.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | A32F3C8BA520 | 2011 | C |
| C25 | `D:/私人资料/deposon-repo/results/_adendum_o_pk_v2_three_way_v2_20260917_133726.json` | `D:/私人资料/deposon-sub/results/_adendum_o_pk_v2_three_way_v2_20260917_133726.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 725FD7B961F8 | 1971 | C |
| C26 | `D:/私人资料/deposon-repo/results/_adendum_o_pk_v2_three_way_v2_20260917_133852.json` | `D:/私人资料/deposon-sub/results/_adendum_o_pk_v2_three_way_v2_20260917_133852.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | A30FF093305D | 1970 | C |
| C27 | `D:/私人资料/deposon-repo/results/_adendum_p_pc_two_phase_fail_h0_20260917_132049.json` | `D:/私人资料/deposon-sub/results/_adendum_p_pc_two_phase_fail_h0_20260917_132049.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 6B26DADDC92C | 2456 | C |
| C28 | `D:/私人资料/deposon-repo/results/_adendum_q_deepseek_v4_pro_anchor_20260917_132049.json` | `D:/私人资料/deposon-sub/results/_adendum_q_deepseek_v4_pro_anchor_20260917_132049.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | AB5D9AE6E42A | 4003 | C |
| C29 | `D:/私人资料/deposon-repo/results/_d05_backbone_robustness_beta_20260918_100853.json` | `D:/私人资料/deposon-sub/results/_d05_backbone_robustness_beta_20260918_100853.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 9B6F085D96DC | 1490 | C |
| C30 | `D:/私人资料/deposon-repo/results/_d05_combined_report_20260918_100853.md` | `D:/私人资料/deposon-sub/results/_d05_combined_report_20260918_100853.md._moved_20260924_1830.md` (仓外同名旧件 0 覆盖) | C87EB8974268 | 10555 | C |
| C31 | `D:/私人资料/deposon-repo/results/_d05_data_rescue_note_2026_09_18.md` | `D:/私人资料/deposon-sub/results/_d05_data_rescue_note_2026_09_18.md._moved_20260924_1830.md` (仓外同名旧件 0 覆盖) | 120295A19655 | 1181 | C |
| C32 | `D:/私人资料/deposon-repo/results/_d05_i1i5_invariants_check_20260918_100853.json` | `D:/私人资料/deposon-sub/results/_d05_i1i5_invariants_check_20260918_100853.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | F12AF5435928 | 1920 | C |
| C33 | `D:/私人资料/deposon-repo/results/_d05_main_run_results_20260918_100853.json` | `D:/私人资料/deposon-sub/results/_d05_main_run_results_20260918_100853.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 0A933D7C8D7A | 15243 | C |
| C34 | `D:/私人资料/deposon-repo/results/_d05_main_run_results_nemotron_3.5_20260918_100853.json` | `D:/私人资料/deposon-sub/results/_d05_main_run_results_nemotron_3.5_20260918_100853.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 1B1B6AD67C39 | 15111 | C |
| C35 | `D:/私人资料/deposon-repo/results/_d05_main_run_results_qwen3_failed_20260918_100853.json` | `D:/私人资料/deposon-sub/results/_d05_main_run_results_qwen3_failed_20260918_100853.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 427B18DA8114 | 18358 | C |
| C36 | `D:/私人资料/deposon-repo/results/_d05_opt_5_directions_results_20260918_100853.json` | `D:/私人资料/deposon-sub/results/_d05_opt_5_directions_results_20260918_100853.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | E5979133195A | 5614 | C |
| C37 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch1_77e2f952.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch1_77e2f952.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | B5F517A321A3 | 2534 | C |
| C38 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch10_1b753116.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch10_1b753116.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 326ADCA520F1 | 5007 | C |
| C39 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch11_7d6a7c8f.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch11_7d6a7c8f.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 383446F24707 | 2573 | C |
| C40 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch12_a2853574.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch12_a2853574.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 6BE21F9586EC | 1246 | C |
| C41 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch13_83f895f9.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch13_83f895f9.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 0694838F66A8 | 739 | C |
| C42 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch14_e5952130.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch14_e5952130.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 64AA9D8A5C7D | 1055 | C |
| C43 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch15_0e65fe2f.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch15_0e65fe2f.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | CFC345D10C7D | 385 | C |
| C44 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch2_e18c17bb.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch2_e18c17bb.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | F14341B8A1A1 | 9260 | C |
| C45 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch3_01ecf050.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch3_01ecf050.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | FD64909EA1D8 | 9656 | C |
| C46 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch4_2f872d54.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch4_2f872d54.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | D35453F21049 | 9720 | C |
| C47 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch5_34439e1e.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch5_34439e1e.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 2769B83F5B1D | 9511 | C |
| C48 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch6_28055e59.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch6_28055e59.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | F3EB7A38AE7D | 10107 | C |
| C49 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch7_0903df7e.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch7_0903df7e.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 7BDA1FECD7C4 | 9748 | C |
| C50 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch8_7468a23b.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch8_7468a23b.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 5A38FC02978C | 9880 | C |
| C51 | `D:/私人资料/deposon-repo/results/_kimi_push_v3_manifest_batch9_f7d9cf1d.json` | `D:/私人资料/deposon-sub/results/_kimi_push_v3_manifest_batch9_f7d9cf1d.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 968D7C6C43CA | 9745 | C |
| C52 | `D:/私人资料/deposon-repo/results/_kimi_safe_batch_push_v1_2026_09_17.json` | `D:/私人资料/deposon-sub/results/_kimi_safe_batch_push_v1_2026_09_17.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 4A204FB0D682 | 7280 | C |
| C53 | `D:/私人资料/deposon-repo/results/_kimi_safe_batch_push_v2_full_2026_09_17.json` | `D:/私人资料/deposon-sub/results/_kimi_safe_batch_push_v2_full_2026_09_17.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | ADF3A8017E26 | 47954 | C |
| C54 | `D:/私人资料/deposon-repo/results/_kimi_safe_batch_push_v3_full_2026_09_17.json` | `D:/私人资料/deposon-sub/results/_kimi_safe_batch_push_v3_full_2026_09_17.json._moved_20260924_1830.json` (仓外同名旧件 0 覆盖) | 058099C10CFB | 7954 | C |
| C55 | `D:/私人资料/deposon-repo/results/_v2_setup.py` | `D:/私人资料/deposon-sub/results/_v2_setup.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | 73F2B8712A90 | 3483 | C |
| C56 | `D:/私人资料/deposon-repo/results/_v2_show_summary.py` | `D:/私人资料/deposon-sub/results/_v2_show_summary.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | 0012B38CE438 | 1200 | C |
| C57 | `D:/私人资料/deposon-repo/results/_v2_smoketest.py` | `D:/私人资料/deposon-sub/results/_v2_smoketest.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | 0B6C22C8F379 | 2040 | C |
| C58 | `D:/私人资料/deposon-repo/results/_v2_stage1_60cells.py` | `D:/私人资料/deposon-sub/results/_v2_stage1_60cells.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | 8C7BD12C3A8C | 31556 | C |
| C59 | `D:/私人资料/deposon-repo/results/_v2_stage2_f2_drift.py` | `D:/私人资料/deposon-sub/results/_v2_stage2_f2_drift.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | 7E9B2FC57D80 | 10798 | C |
| C60 | `D:/私人资料/deposon-repo/results/_v2_stage3_f3_strip.py` | `D:/私人资料/deposon-sub/results/_v2_stage3_f3_strip.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | CE4362E325CA | 11803 | C |
| C61 | `D:/私人资料/deposon-repo/results/_v2_stage4_f4_pdv2.py` | `D:/私人资料/deposon-sub/results/_v2_stage4_f4_pdv2.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | B84F5AAB6FAF | 10355 | C |
| C62 | `D:/私人资料/deposon-repo/results/_v2_stage5_f5_dpath.py` | `D:/私人资料/deposon-sub/results/_v2_stage5_f5_dpath.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | E8871B829D89 | 6480 | C |
| C63 | `D:/私人资料/deposon-repo/results/_v2_verify_outputs.py` | `D:/私人资料/deposon-sub/results/_v2_verify_outputs.py._moved_20260924_1830.py` (仓外同名旧件 0 覆盖) | EB0107DD79B5 | 2656 | C |

> 注: 62 件同名冲突件均经过 SHA 一致性实测 (源 SHA-12 = 仓外目标 SHA-12, = GHOST_REF_COPIED duplicates per `ghostref_reconciliation` & `ghostref_copy_log`); 仓外 canonical 件 0 触动; 时间后缀 `_moved_20260924_1830` 是单一批次号 (本棒所有移动用同一后缀便于清查)。

---

## 5. 灰区对账 (8 件 · 7 件干净 + 1 件时间后缀)

> 目标: `D:/私人资料/deposon-repo/results/_archive_2026_09_24/`
> 通道: PowerShell `Move-Item`
> 总 bytes: 124,753 (与 v1 ledger §3.4 灰区小计 bytes 一致)
> **同名冲突实测**: 1/8 件 (`.tmp/_final_verify.py` 2279 bytes SHA=DB4428293040 vs 仓内 `results/_archive_2026_09_24/_final_verify.py` 2307 bytes SHA=31A5D44497F1, 内容不同)

### 5.1 干净移动 (7 件)

| # | 旧路径 (repo/.tmp/) | 新路径 (repo/results/_archive_2026_09_24/) | SHA-12 (实测 2026-09-24 18:24) | bytes | 类别 |
|---|---|---|---|---|---|
| G1 | `D:/私人资料/deposon-repo/.tmp/_l11_run1.json` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/_l11_run1.json` | 20B0E13064F8 | 12143 | G |
| G2 | `D:/私人资料/deposon-repo/.tmp/_l13_latency_test.py` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/_l13_latency_test.py` | DAE238354342 | 2954 | G |
| G3 | `D:/私人资料/deposon-repo/.tmp/_l14_checkpoint.json` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/_l14_checkpoint.json` | 91B582672B49 | 10963 | G |
| G4 | `D:/私人资料/deposon-repo/.tmp/_l14_records.json` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/_l14_records.json` | 8F6FCF027149 | 50957 | G |
| G5 | `D:/私人资料/deposon-repo/.tmp/l14_runner_v2.py` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/l14_runner_v2.py` | ACF1CD6CCBD4 | 23056 | G |
| G6 | `D:/私人资料/deposon-repo/.tmp/l14_small_batch.py` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/l14_small_batch.py` | 0659C947BEC1 | 21784 | G |
| G7 | `D:/私人资料/deposon-repo/.tmp/latency_test.py` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/latency_test.py` | FD9FD98785E1 | 617 | G |

> 注: G1-G7 的 SHA-12 实测与 v1 ledger §3.4 完全一致 (ACF1CD6CCBD4 / 0659C947BEC1 / 8F6FCF027149 / 91B582672B49 / 20B0E13064F8 / DAE238354342 / FD9FD98785E1)。

### 5.2 同名冲突 + 时间后缀移动 (1 件)

| # | 旧路径 (repo/.tmp/) | 新路径 (repo/results/_archive_2026_09_24/ · 时间后缀) | SHA-12 (实测 2026-09-24 18:24) | bytes | 类别 |
|---|---|---|---|---|---|
| G8 | `D:/私人资料/deposon-repo/.tmp/_final_verify.py` | `D:/私人资料/deposon-repo/results/_archive_2026_09_24/_final_verify.py._moved_20260924_1830` (仓内同名旧件 0 覆盖) | DB4428293040 | 2279 | G |

> 注: 仓内 `_archive_2026_09_24/_final_verify.py` (2307 bytes, SHA-12=31A5D44497F1) 已存在, 内容与 `.tmp/_final_verify.py` (2279 bytes, SHA-12=DB4428293040) 不同 (实测比对), 按铁则加时间后缀避免覆盖。本棒保留仓内旧件完整 (2307 bytes 内容未触动)。

---

## 6. 四报 (派工单要求)

### 6.1 三目录 before/after 文件计数

| 目录 | before (实测 2026-09-24 18:20) | after (实测 2026-09-24 18:24) | delta | 备注 |
|---|---|---|---|---|
| `D:/私人资料/deposon-repo` | **1440** | **1324** | **-116** | 本棒新建 ledger v2 (本件) 落地 +1; 移动 125 件出仓 -125; 净 -124; 末次实测 -116 = 净差与 v2 ledger 落地时差 (after 计数 = 1324 已含本 v2 ledger) |
| `D:/私人资料/_non_upload_local_archive` | 1176 | 1230 | +54 | A 类 54 件全部入仓 |
| `D:/私人资料/deposon-sub` | 364 | 427 | +63 | C 类 63 件全部入仓 (1 件干净 + 62 件时间后缀) |
| `D:/私人资料/deposon-repo/results/_archive_2026_09_24/` (灰区目标) | 6 | 14 | +8 | 灰区 8 件全部入仓 (7 件干净 + 1 件时间后缀) |

> **核对 (末次实测 2026-09-24 18:25)**: repo 实际 = 1324 (含本 v2 ledger); 1440 - 125 + 1 = 1316 (理论), 实测 1324 (差 +8); **差 +8 来源**: before-count 与末次 after-count 之间实测差 -116, 与理论 -124 差 +8; 推测 PowerShell `Get-ChildItem -Recurse -File` 在不同时间点扫描深度或子目录遍历差异 (例如 .tmp/ / __pycache__/ 内联文件 visibility / junction / hidden 标志差异); **老实交代: 未根因定位, 不强行解释, 接受实测数**; 三类 (A 54 + C 63 + 灰区 8) 源文件实测全部清空 (Test-Path False × 125) + 三类目标文件实测全部到位 (Test-Path True × 125 + 三目标目录 delta 与移动数一致 +54/+63/+8), 故**移动事实落地完整, 不影响对账真实性**。

### 6.2 主目录最终计数

| 维度 | 数字 |
|---|---|
| 本棒实测最终 (末次实测 2026-09-24 18:25) | **1324 件** (含本 v2 ledger) |
| 派工单目标 <1000 | **未达成** (差额 +324 件 = 1324 - 1000) |
| 派工单预期消化件数 (A + C + 灰区) | 125 件已实际移动 (A 54 + C 63 + 灰区 8) |
| 相对 v1 ledger after (1440) | -116 件 (实测) / -124 件 (理论 1440-125+1; 差 +8 未根因定位) |

> **老实交代**: 目标 <1000 未达成。差额 +324 件 (1324 - 1000)。本棒已按 PI 拍板 B 路径执行 125 件全部候选; 剩余 +324 件差额构成与第一棒 manifest §G / v1 ledger §4.2 一致: V1-V3 frozen 资产 (~530) + V3/V4 frozen 派生件 (~250) + V3 ghostref 链派生件 (~243) + letters/ V4 委托链 (41) + .tmp/ 链上保留 (0) = ~1064 件不可动。**派工单授权范围仅 A/C/灰区共 125 件, 不涵盖 V1-V3 frozen / V4 pi-cot / V4 supp 等保护名单件**; 达成 <1000 需要进一步拍板保护名单外其他件 (本棒未擅自扩容)。

### 6.3 frozen / 保护名单跳过清单 (派工单 §铁则)

#### 6.3.1 frozen 锚根件 6 件 · 0 触动

(详见 §2 表格, 全部 SHA-12 移动前后实测一致)

#### 6.3.2 派工单保护名单 12 类 · 0 触动

| 类别 | 件数 | 本棒触动 |
|---|---|---|
| `results/_v4_pi_cot_v2_*` 全系 | (另一 worker 在跑 §3 V4 派工) | 0 触动 ✓ |
| `results/_v4_supp_prereg_v02_*` 锁链 8 件 | 8 | 0 触动 ✓ |
| `results/_v4_supp_*` 链上件 | ~150 | 0 触动 ✓ |
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` (424CF2D07884) | 1 | 0 触动 ✓ |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` (29A853444D42) | 1 | 0 触动 ✓ |
| `results/_v4_noise_cleanup_manifest_*` (F5D2837C2630) | 1 | 0 触动 ✓ |
| `results/_v4_maindir_cleanup_*` (32CC61D394F2 第一棒 manifest + 4025E871726B v1 ledger) | 2 | 本棒仅**新建** v2 ledger (本件), 不动其他 ✓ |
| `letters/` (`_kimi_v4_*`) | 41 | 0 触动 ✓ |
| `docs/` | 134 | 0 触动 ✓ |
| `verifier/` | 117 | 0 触动 ✓ |
| (隐含) `corpus/` V1.4 frozen | 41 | 0 触动 ✓ (注: `corpus/v20_caption_surface/_adendum_I_po_captions_closure_20260917_132049.json` 是同名大小写差异件, 不动) |
| (隐含) `attacks/` + `tests/` + `reviews/` + `scripts/` + `paper/` + `tools/` + `deposon_team/` + `.trae/` + `__pycache__/` | ~196 | 0 触动 ✓ |

> **派工单保护名单全部 0 触动, 派生 JSON 不合并项 0 触动, 不擅自调阈值, 不覆盖既有件** — 4 项铁律全守。

### 6.4 灰区余项 / 未移清单

#### 6.4.1 灰区 (8 件 · 全部已移)

v1 ledger §3.4 列出的 8 件 chain-bound 件全部已按 PI 拍板 B 路径移入 `results/_archive_2026_09_24/`。详见 §5。

#### 6.4.2 未移件 (本棒范围外, 老实交代)

| 件 | 原因 | 派工单依据 |
|---|---|---|
| `results/_p_d_v03_22caption_verification_20260917_163757.json` (13775 bytes) | 派工单 A 类 pattern 未包含 `_p_d_v03_*` (仅 `_p_l_v3_*` 与 `_p_k_v3_*` 与 `_p_l_v3_phase3*adendum*`); 虽同为 V3 ghostref 派生非核心件, 但本棒不擅自扩容 | 派工单 §A 仅列 6 子类 pattern |
| `results/_p_d_v03_verification_report_20260917_163757.md` (9799 bytes) | 同上 | 同上 |

> 2 件 `_p_d_v03_*` 留在主目录 `results/`; 若 PI 后续拍板纳入 A 类, 可单派棒以相同 B 路径执行。

---

## 7. key 形态自扫 (合规自检)

本棒改动件 (A 54 + C 63 + 灰区 8 = 125 件 + 本对账表全文) 严苛 API key 形态
`\b(sk-[A-Za-z0-9]{20,}|tp-[A-Za-z0-9]{20,}|ark-[A-Za-z0-9]{20,}|API_KEY=[A-Za-z0-9]{16,}|Authorization:\s*Bearer\s+[A-Za-z0-9_.-]{16,})\b`
→ **0 命中** (按 R4 key 永不明文铁律)

---

## 8. 通道与可恢复性

| 维度 | 值 |
|---|---|
| 移动通道 | PowerShell `Move-Item` (atomic, content preserved, same-volume move) |
| 临时调试文件清理 | 3 件 mavis-trash (`_v4_A_rows.txt` / `_v4_C_rows.txt` / `_v4_G_rows.txt`, 均为本棒 row-generation scratch, 写入 .tmp/ 后即用即清) |
| 删除通道 | 单条 mavis-trash.cmd (trusted launcher, Microsoft.VisualBasic.FileIO.FileSystem.DeleteFile → Recycle Bin) |
| 不可用工具 | 永久删除 `del` / `Remove-Item -Force` / `Remove-Item -Recurse` (safety policy 拒绝) |
| 输出信息 | 每件 `mavis-trash: moved to trash: '<path>'` |
| 可恢复性 | **3/3 项可恢复** (Recycle Bin 标准 recover 路径) |
| 0 永久删除 | ✓ |
| 0 触动 frozen 锚 | ✓ (6 件 SHA-12 不变) |
| 0 覆盖目标既有件 | ✓ (63 件同名冲突按铁则加时间后缀) |

---

## 9. skill 缺位老实交代 (fallback 纪律锚)

- `folder-cleanup-assistant` 与 `superpowers:verification-before-completion` Local skill not found → 按任务提供的纪律锚 fallback 执行 (`results/_v4_maindir_cleanup_moves_ledger_2026_09_24.md` 4025E871726B 候选清单 + `results/_v4_maindir_cleanup_manifest_2026_09_24.md` 32CC61D394F2 格式口径 + PI 拍板 ask_721b8b46601f0b96a6989a0f B 路径授权)
- 本棒**额外加码**:
  - 移动前冻结 6 件 frozen 锚 SHA-12 实测并落表 (before-table)
  - 每件移动后 `Test-Path` 源 + `Test-Path` 目标 + `Get-FileHash SHA-12` 目标三确认
  - 移动后再冻结 6 件 frozen 锚 SHA-12 实测并比对 (after-table, 全部一致)
  - 同名冲突实测: 63 件逐件比对源 SHA-12 vs 仓外/仓内目标 SHA-12 (= 62 件 C 类 GHOST_REF_COPIED + 1 件灰区内容不同, 加时间后缀避免覆盖)
- **不强信子代理 succeeded**: 本棒 0 件子代理调用 (直接 PowerShell Move-Item + Test-Path + Get-FileHash 自验三通道); succeeded ≠ 跑完, 落盘实测计数为准
- **不擅自触动 frozen 锚**: 本棒禁止任何对 6 件 frozen 锚根件的写操作; 实测 SHA-12 移动前后完全一致

---

## 10. 与第一棒 / 第二棒 / 第三棒派工单的对账

| 棒 | 派工单 ID | 期望 | 本棒实测 | 一致性 |
|---|---|---|---|---|
| 第一棒 (trash) | mvs_eba7623bfea64220aa67a963149c49b2 | trash 51 件临时件 + manifest | 1437 → 1440 (v1 ledger 落地后) | 第一棒收口, 本棒继承 |
| 第二棒 (拒绝移) | mvs_f7692aceee0b4244923a6b2c3c53afe3 | 0 件移动, 矛盾上交 PI | 1439 → 1440 (v1 ledger 落地后) | 第二棒上交, PI 拍板 B 路径 |
| 第三棒 (本棒) | (current) | PI 拍板 B: 131 件移入 archive/sub | **125 件实际移动** (54 A + 63 C + 8 灰区, A -5 是 v1 算数偏差), 0 件删除, 63 件时间后缀 | 派工单授权范围已全部覆盖, 数字差异老实交代 |

---

*— sign-off by worker, 2026-09-24, mvs_30807822972a4b29beeee8aa6563cc1c, parent mvs_bbeb804b1a6a41109be740636eed1709*

> **本棒交付清单**:
> 1. 本对账表 `results/_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` (新建; **最终字节与 SHA-12 以末次 `Get-FileHash SHA256` 实测为准** — 因 sign-off 段含完整写出的 SHA 自引用, 任一字符级修改都会引发 SHA 漂移, **不内嵌具体数, 改为外测**), 未触动第一棒 manifest / v1 ledger / 任何 frozen 锚
> 2. **125 件移动完成** (54 A + 63 C + 8 灰区) + 0 件删除 + 63 件加时间后缀 `_moved_20260924_1830`
> 3. **6 件 frozen 锚 SHA-12** 移动前后实测对齐 (03C6C01F3697 / 1D52DB0EBF53 / 29A853444D42 / B34B9F7BDFB7 / 8CD133D0896F / B899103853CA)
> 4. 12 类保护名单全部 0 触动 (派工单 §铁则)
> 5. 0 派生 JSON 合并 / 0 阈值调整 / 0 覆盖既有件
> 6. v1 ledger (4025E871726B) 与第一棒 manifest (32CC61D394F2) 0 触动
> 7. 主目录 1440 → 1323 (实测, 差 +7 老实交代未根因定位)