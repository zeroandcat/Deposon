# 镜像形态对比件 ｜ 远端单区 vs 本地双区 ｜ 取证面（对比件）｜ 2026-10-18

📌 **件之性质**：本件为**对比件**（取证面）——PI 令（2026-10-18 13:4x）「对比远端单区与本地双区的镜像形态，出具**新的补传与删除及拉回委托**」之**取证底面**。**委托件由 doc-writer 据本件另出**；本棒 ⛔ **0 代出委托**。
📌 **今日 0 实验**（纯取证）｜**网络仅限匿名只读**（GitHub REST API，无凭据、无认证头、⛔ 0 远端写）｜**归档区 0 触 · GLM 面 0 触**。
📌 **FTFB**：本件之一切口径，先落于判据冻结件、**事后一字未调**（见 §0）。

---

## §0 FTFB · 判据冻结件与引件指纹（凡引他件，先实测）

| 件 | 路径 | bytes | SHA-256（实测） | 备注 |
|---|---|--:|---|---|
| **判据冻结件** | `.tmp/_mirror_morphology_criteria_freeze_2026_10_18.md` | 7,899 | `1edd2511a4cd` | **先于一切比对落盘**；BOM=0 · CRLF=0 |
| 简报所引核验件 | `results/_kimi_postexec_receipt_verification_2026_10_18.md` | 21,678 | `d51ff0c7776d` | **与简报所载 `d51ff0c7776d` 相符** ✅ · BOM=0 · CRLF=0 |
| 补函执行回执 | `results/_supplement_execution_receipt_kimi_2026_10_18.md` | 41,236 | `85f8777f139c` | git-blob-SHA1-12 `f4b0124d4c1e` · **已在远端前缀面在位** |

**冻结之口径（M-1 路径映射）**：远端 `_september_workspace/<rel>` ⇔ 本地 `<rel>`；远端**根层遗留面**（非前缀者）**单列、不参与映射比对**。
**冻结之排除面（面② 专用）**：`E1` `.tmp/` ｜ `E2` `letters/` carve ｜ `E3` `S3` 隐私面（`E4`「永不上传」**永久禁令**）｜ `E4` 噪声/S5 临时件族 ｜ `E5` H4 严禁件。

---

## §1 远端形态 · 全树之取（live HEAD 复测）

| 项 | 实测值 |
|---|---|
| 仓 | `zeroandcat/Deposon`（`default_branch=main`） |
| **live HEAD** | **`4cd417b32e5d4ae05de95825e2d13d602b8b928a`** |
| commit 时间 / message | `2026-10-18T05:38:54Z` ｜ `add: results/_supplement_execution_receipt_kimi_2026_10_18.md (v0.4-SCDU execution receipt)` |
| 树 SHA | `4cd417b32e5d4ae05de95825e2d13d602b8b928a` |
| **`truncated`** | **`false`** ✅ **全树穷举，非抽样**（故「0 在位」类阴性断言成立） |
| tree entries | 3,644（其中 blob 3,447：前缀面 3,034 ＋ 根层遗留面 413） |
| 前缀面字节 | 118,689,899 B |
| 遗留面字节 | 4,087,485 B |

### §1-1 ⚠ HEAD 漂移面（登记，不软化）

回执载终态 HEAD ＝ **`bd89e1ffffe06afa172d746c1a27b3faa456ff70`**（`results/_supplement_execution_receipt_kimi_2026_10_18.md:13`）；
本棒执行时**实测 live HEAD ＝ `4cd417b32e5d4ae05de95825e2d13d602b8b928a`**，**二者不一致**，其间新增 **1 commit**，message ＝
> `add: results/_supplement_execution_receipt_kimi_2026_10_18.md (v0.4-SCDU execution receipt)`

即：**执行回执自身已被上传至远端前缀面**（实测 `_september_workspace/results/_supplement_execution_receipt_kimi_2026_10_18.md` **在位** ✅）。
依冻结件 §0「若实测漂移，以实测为准」——本件一切远端读数**均以 `4cd417b32e5d4ae05de95825e2d13d602b8b928a` 为准**。
⚠ **登记**：回执之「终态 HEAD」已成**历史锚点**，不再为 live 面；后续任何以 `bd89e1ff` 为准之对账**须先行复测**。

### §1-2 远端单区前缀之结构面（`_september_workspace/` 之**下**各一级之件分布）

- `results` — **2,167**
- `deposon_team` — **160**
- `docs` — **142**
- `verifier` — **120**
- `(root-files)` — **102**
- `pi_rulings` — **93**
- `.trae` — **42**
- `corpus` — **42**
- `reviews` — **32**
- `tests` — **23**
- `tools` — **23**
- `.mavis` — **20**
- `tmp_movedout_2026_10_01` — **18**
- `tmp_movedout_2026_10_09` — **13**
- `scripts` — **10**
- `tmp_movedout_2026_09_28` — **8**
- `tmp_movedout_2026_09_29` — **8**
- `paper` — **5**
- `attacks` — **4**
- `.vscode` — **1**
- `_archive_deposon_2026_09_17` — **1**

⚠ **`_september_workspace/.tmp/` 已整面清空**（前缀面一级清单中 **0 见 `.tmp`**）——故本地 `.tmp/` 之 2046 件为「远端已删之临时件」，依 `E1` ⛔ **0 回补**（§4 面②）。

### §1-3 根层遗留面（**不参与映射比对**，仅列清单）

**遗留面合计：413 件 blob ＋ 52 个 tree 目录 ＝ 4,087,485 B**。

按一级分布：

- `results` — **106**
- `verifier` — **78**
- `(根层文件)` — **68**
- `docs` — **59**
- `reviews` — **33**
- `corpus` — **24**
- `tests` — **22**
- `paper` — **11**
- `letters` — **7**
- `deposon_team` — **2**
- `tools` — **2**
- `.trae` — **1**

其中根层文件 **68** 件（清单见 §7-3）。**遗留面之三项专查（阴性）**：

| 专查 | 结果 |
|---|---|
| 遗留面残留 `_archive_2026_09_20/` | **0 件** ✅ |
| 遗留面残留隐私面形态（`dataset`/`addendum`/`health`） | **0 件** ✅ |
| 遗留面残留临时件族（`tmp/temp/bak/backup/copy/scratch/old`） | **0 件** ✅ |

📌 **诚实限定**：以上三项「0 残留」**仅证于遗留面**；前缀面之对应残留**另见 §6-KD-3**（`_archive_2026_09_20/` 在**前缀面**仍有 70 件残留）。**⛔ 0 以遗留面之清洁充全仓之清洁。**

---

## §2 本地双区 · 全量枚举

| 区 | 路径 | 件数 | 遍历错误 | 枚举面 |
|---|---|--:|--:|---|
| 主仓 | `〔本地路径已脱敏〕` | 4,124 | **0** | repo 相对路径 · bytes · SHA-256-12 · **Git-blob-SHA1-12** |
| 只读副本面 | `〔本地路径已脱敏〕` | 1,276 | **0** | 同上 |
| 双区并集 | — | **5,389** | 0 | — |
| 归档区 | `〔归档区〕` | **不枚举** | — | **0 读 0 写 0 列目录**；仅载「**归档区在 · 0 触**」 |
| GLM 面 | `〔本地路径已脱敏〕` | **不枚举** | — | **0 触** |

### §2-1 双区非对称面

| 关系 | 件数 |
|---|--:|
| 仅 repo 有（sub 无） | 4,113 |
| 仅 sub 有（repo 无） | 1,265 |
| 双区皆有且**内容相同** | 10 |
| 双区皆有且**内容不同** | 1 |

**唯一「双区皆有且内容不同」者**：

| 路径 | repo SHA-1-12 | sub SHA-1-12 | repo B | sub B |
|---|---|---|---|---|
| `results/_v5_theory_input_acquisition_request_2026_09_29.md` | `c062bdef8ec7` | `368bdd601d40` | 10,751 | 10,691 |

📌 该件为**双区内容漂移**——⚠ **⛔ 0 以任一区为权威、⛔ 0 径覆盖**（登记为 `KD-MC-05`，处置归 PI）。

---

## §3 三面之对账（依冻结判据 §2）

### §3-0 闭合校验（**不重不漏**之自证）

远端前缀映射面 **3,034 件** ＝ 拉回 **172** ＋ 已对齐 **2,348** ＋ 同名异内容 **514** ＝ **3,034** ✅ **精确闭合**。
本地双区并集 **5,389** ＝ 远端在位 **2,862** ＋ 远端无 **2,527** ＝ **5,389** ✅ **精确闭合**。

### §3-1 面① 远端有而本地无 ＝ **拉回候选**

**172 件 ／ 合计 2,849,991 B**。按一级分布：

- `results` — **122**
- `.trae` — **22**
- `deposon_team` — **15**
- `docs` — **8**
- `(根层文件)` — **1**
- `corpus` — **1**
- `tmp_movedout_2026_09_29` — **1**
- `tmp_movedout_2026_10_01` — **1**
- `verifier` — **1**

**构成拆解（据实测）**：

- `results/_archive_2026_09_20/` 之残留：**70** 件
- `.trae/audit/compile_evidence/` 之编译日志/旗标：**22** 件
- 其他：**80** 件
- 其中 **日志/旗标类**（`.log`/`.err`/`.flag`）：**79** 件 ⇒ 见 `KD-MC-04`

**逐件全表**（172 件 · 路径 · bytes · 远端 blob SHA-1-12）：

| 路径（映射后） | bytes | 远端 blob SHA-1-12 |
|---|---|---|
| `.trae/audit/compile_evidence/DONE.flag` | 85 | `62d11e56a062` |
| `.trae/audit/compile_evidence/cn_pdflatex_pass2.log` | 74,481 | `767d26050580` |
| `.trae/audit/compile_evidence/cn_pdflatex_stdout.log` | 1,386 | `fe5fe2b8b2d0` |
| `.trae/audit/compile_evidence/en_pdflatex_pass2.log` | 45,951 | `7476489839da` |
| `.trae/audit/compile_evidence/en_pdflatex_stdout.log` | 1,386 | `52941f523383` |
| `.trae/audit/compile_evidence/v1_62refs_20260908/DONE.flag` | 33 | `1ecf5c39db74` |
| `.trae/audit/compile_evidence/v1_62refs_20260908/cn_pdflatex_pass2.log` | 74,268 | `957e7426e0db` |
| `.trae/audit/compile_evidence/v1_62refs_20260908/cn_runner.log` | 1,278 | `6507336ade0e` |
| `.trae/audit/compile_evidence/v1_62refs_20260908/en_pdflatex_pass2.log` | 45,794 | `bf6c810051d1` |
| `.trae/audit/compile_evidence/v1_62refs_20260908/en_runner.log` | 1,278 | `d98befafc10e` |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/DONE.flag` | 85 | `0943ef645f9c` |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/EXTRACT_NEW.flag` | 102 | `d0887c6d2fa8` |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/cn_pdflatex_pass2.log` | 60,325 | `1381b75d060b` |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/cn_pdflatex_stdout.log` | 1,386 | `fe5fe2b8b2d0` |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/en_pdflatex_pass2.log` | 39,448 | `936582d2d57b` |
| `.trae/audit/compile_evidence/v2_overfull_fix_20260909/en_pdflatex_stdout.log` | 1,386 | `52941f523383` |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/COMPILE_SUMMARY.txt` | 1,693 | `d6a600658c5c` |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/DONE.flag` | 85 | `62d11e56a062` |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/cn_pdflatex_pass2.log` | 74,481 | `767d26050580` |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/cn_pdflatex_stdout.log` | 1,386 | `fe5fe2b8b2d0` |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/en_pdflatex_pass2.log` | 45,951 | `7476489839da` |
| `.trae/audit/compile_evidence/v2pre_h1h3_20260909/en_pdflatex_stdout.log` | 1,386 | `52941f523383` |
| `_mirror_manifest.json` | 192,689 | `0a92d7bd23f1` |
| `corpus/v20_caption_surface/_adendum_I_po_captions_closure_20260917_132049.json` | 4,429 | `df5e8e3c7f2d` |
| `deposon_team/plugins/_v4_wide_s1b_inv2_2026_09_27.py` | 1,546 | `b3de03b9c386` |
| `deposon_team/plugins/_v4_wide_s2_scan_2026_09_27.py` | 4,000 | `320eb0da8f13` |
| `deposon_team/plugins/_v4_wide_s3_keyscan_2026_09_27.py` | 2,647 | `d591872191e1` |
| `deposon_team/plugins/_v4_wide_s3b_uuidctx_2026_09_27.py` | 1,707 | `30a2b0875241` |
| `deposon_team/plugins/_v4_wide_s3c_keydetail_2026_09_27.py` | 2,490 | `49aaf6223a34` |
| `deposon_team/plugins/_v4_wide_s4_verify_2026_09_27.py` | 2,812 | `05ac84a856ad` |
| `deposon_team/plugins/_v4_wide_s6_unrefscan_2026_09_27.py` | 2,495 | `daf43fb20421` |
| `deposon_team/plugins/_v4_wide_s7_fix_2026_09_27.py` | 6,101 | `0deb7931c842` |
| `deposon_team/plugins/_v4_wide_s8_fix3_2026_09_27.py` | 3,514 | `5bf93f2343ff` |
| `deposon_team/plugins/_v4_wide_s9_final_2026_09_27.py` | 3,399 | `22e371480238` |
| `deposon_team/plugins/_v4_wt_s5_verify_2026_09_27.py` | 4,950 | `9a23a8f01f35` |
| `deposon_team/plugins/_v5_wa_s1_2026_09_30.py` | 4,351 | `713ec0c3bf0c` |
| `deposon_team/plugins/_v5_wa_s2b_2026_09_30.py` | 3,583 | `4815f547278f` |
| `deposon_team/plugins/_v5_wa_s2c_2026_09_30.py` | 3,168 | `581e5d0565e2` |
| `deposon_team/plugins/_v5_wa_s3_fix_2026_09_30.py` | 4,742 | `4b785e9b99bd` |
| `docs/V3X/D7_EXTERNAL_ADVISOR_ONLINE_PUSH_REQUIREMENTS_2026_09_18.md` | 8,066 | `8adff5e918e3` |
| `docs/V3X/LETTER_FROM_TRAE_2026_09_11.md` | 13,629 | `720cfaf53161` |
| `docs/V3X/LETTER_FROM_TRAE_3RISK_2026_09_11.md` | 5,145 | `f60d3f3eca8b` |
| `docs/V3X/LETTER_FROM_TRAE_REVIEW_2026_09_16.md` | 7,724 | `610cd2c2bbdb` |
| `docs/V3X/LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md` | 3,571 | `f369e5c35f8a` |
| `docs/V3X/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md` | 5,154 | `b937094b1e44` |
| `docs/V3X/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md` | 16,008 | `4670cf5c9b75` |
| `docs/V3X/TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md` | 7,376 | `158b0518e100` |
| `results/AUDIT_2026-08-30.json` | 3,143 | `f8c3fdbeb1b6` |
| `results/Deposon_评估汇总_v1_3_0.json` | 2,811 | `3adf056b6c80` |
| `results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | 10,586 | `bcf317b88d6e` |
| `results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | 7,855 | `d39d91ecd84c` |
| `results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | 9,343 | `96c744af6776` |
| `results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | 11,575 | `f6c1e86b1542` |
| `results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | 4,784 | `eb23f9346728` |
| `results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | 454,307 | `d10a14ba179a` |
| `results/_archive_2026_09_20/_cpath_sim_run_2026_09_10.log` | 1,508 | `10e844e84dad` |
| `results/_archive_2026_09_20/_d05_main_runner_20260918.log` | 9,232 | `345608fea302` |
| `results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | 18,611 | `a76a2658a272` |
| `results/_archive_2026_09_20/_p_l_v3_phase1_finalize.log` | 1,184 | `1a098d388a6e` |
| `results/_archive_2026_09_20/_p_l_v3_phase1_runner.log` | 8,202 | `e731a8ade38f` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner.log` | 2,370 | `ead67cc76e5d` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_171640.log` | 1,516 | `2b5128e0a098` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172440_gpt56sol.log` | 865 | `1a98af38bdef` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172928_gpt56sol.log` | 955 | `d0fe6629bee3` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_173159_gpt56sol.log` | 2,765 | `c83c63c766f4` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_174011_claude_sonnet5.log` | 2,687 | `60f85dbfabc3` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_175003_gemini_37flash.log` | 2,342 | `0952adb63097` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_finalize.log` | 2,712 | `e506d97fb9fc` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_finalize_20260917_142748.log` | 1,224 | `19e035b669d0` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_glm53.log` | 2,542 | `f85eddf2fc03` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_glm53_only_20260917_142011.log` | 1,140 | `bb5e79511c7e` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.err` | 530 | `2c10446f7d93` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.log` | 564 | `3055f18b8f1d` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding_v3_2026_09_17.console.log` | 10,102 | `5ee1916ddb81` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_probe.log` | 3,100 | `9678a036b1b7` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_probe_agent.log` | 6,760 | `54c4f808cd15` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb.log` | 2,046 | `5267d1048a6e` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb_proxy_v2.log` | 17,632 | `16a34c3ae004` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_probe_ext.log` | 4,992 | `4cb29bc0fce1` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_probe_gpt4o.log` | 3,462 | `2e5b3c200544` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_runner.log` | 3,416 | `7e9ff72e8505` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console.log` | 6,134 | `303659550a1b` |
| `results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console2.log` | 2,925 | `d42b879bc3de` |
| `results/_archive_2026_09_20/_probe_teamo_via_proxy.log` | 4,526 | `7d540c86567e` |
| `results/_archive_2026_09_20/_sanity_openai_more.log` | 1,444 | `ac1d0b5bd3c2` |
| `results/_archive_2026_09_20/_sanity_teamo_three.log` | 2,168 | `8912d907b188` |
| `results/_archive_2026_09_20/_test_3bb_vary.log` | 11,522 | `63bad8ab3356` |
| `results/_archive_2026_09_20/_v2_stage1_60cells.console.log` | 17,158 | `f401a22768be` |
| `results/_archive_2026_09_20/_v2_stage3_f3_strip.console.log` | 2,440 | `639a46fbc44c` |
| `results/_archive_2026_09_20/_v3x_6way_finalize.log` | 618 | `e8e3eecbbe55` |
| `results/_archive_2026_09_20/_v3x_6way_run.log` | 8,952 | `cb8f0635c4e8` |
| `results/_archive_2026_09_20/_v3x_6way_stage3_minimal.log` | 1,678 | `2f5edcac6a91` |
| `results/_archive_2026_09_20/_v3x_6way_stage3_recovery.log` | 2,242 | `713e5f75c289` |
| `results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log` | 17,456 | `8b06e5d3f43d` |
| `results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log.bak` | 6,106 | `1b86970816da` |
| `results/_archive_2026_09_20/_volc_22cap_emb.log` | 9,068 | `42c9d2e4a9ea` |
| `results/_archive_2026_09_20/_worker_openrouter_rag_run.log` | 6,476 | `e56dd631a770` |
| `results/_archive_2026_09_20/deposon_d_fix2_metric_verify_9m60c_2026_09_15.log` | 24,634 | `e71aecfebe91` |
| `results/_archive_2026_09_20/deposon_deepseek_v41_flash_30cells_2026_09_10.log` | 6,514 | `4de1a9c448f7` |
| `results/_archive_2026_09_20/deposon_dpath_cross_modal_2026_09_10.log` | 8,885 | `f33a29327e11` |
| `results/_archive_2026_09_20/deposon_dpath_cross_modal_runner_2026_09_10.stdout.log` | 17,772 | `97e2aa66522f` |
| `results/_archive_2026_09_20/deposon_feshbach_rag_30cells_2026_09_10.log` | 6,887 | `c6aca7403cf8` |
| `results/_archive_2026_09_20/deposon_v2_phase1_60cells_2026_09_11.log` | 8,578 | `3d3a6b8994db` |
| `results/_archive_2026_09_20/deposon_v2_phase2_f2_2026_09_11.log` | 1,272 | `41eba7b8f98b` |
| `results/_archive_2026_09_20/deposon_v2_phase3_f3_2026_09_11.log` | 1,247 | `0467038c016f` |
| `results/_archive_2026_09_20/deposon_v2_phase4_f4_2026_09_11.log` | 1,064 | `be3d138384e2` |
| `results/_archive_2026_09_20/deposon_v2_phase5_f5_2026_09_11.log` | 1,092 | `8cfd8dd5620c` |
| `results/_archive_2026_09_20/deposon_v41_flash_60cells_v2_2026_09_10.log` | 12,470 | `ebdc60a61dbc` |
| `results/_archive_2026_09_20/deposon_volcengine_minimax_m3_30cells_2026_09_10.log` | 3,444 | `f03cb6416a01` |
| `results/_archive_2026_09_20/deposon_volcengine_seed_code_30cells_2026_09_10.log` | 7,342 | `672e14623f28` |
| `results/_archive_2026_09_20/deposon_volcengine_worker_b_2026_09_10.log` | 3,326 | `853dd2881e5e` |
| `results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.log` | 5,869 | `c3b87ceaad9d` |
| `results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.run.log` | 12,070 | `5a6919ccc9b6` |
| `results/_archive_2026_09_20/fiction_that_feeds_back.tex` | 93,324 | `68da7b05797b` |
| `results/_archive_2026_09_20/gpt6_30cells_run.log` | 4,220 | `cd78df661d8b` |
| `results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | 20,082 | `7375dbcc2a8b` |
| `results/_archive_2026_09_20/review_tech_B1_grok46.md` | 18,923 | `5c05888226a8` |
| `results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | 8,098 | `3c2dd5f7c0ab` |
| `results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log` | 4,091 | `b39406b8614e` |
| `results/_archive_2026_09_21/Deposon_评估汇总_v1_3_0.json` | 2,811 | `3adf056b6c80` |
| `results/_c5_kv3df_0_1_minmaxstd_readings_2026_10_12.json` | 7,193 | `12864634c039` |
| `results/_c5_kv3df_0_1_minmaxstd_suppl_prereg_2026_10_12.md` | 5,697 | `e5df207d1ece` |
| `results/_c5_kv3df_0_1_minmaxstd_suppl_report_2026_10_12.md` | 8,476 | `843d944a56ec` |
| `results/_coze_online_v3_2026_09_18.md` | 7,476 | `68c3e712d66f` |
| `results/_coze_online_v3_d7format_2026_09_18.md` | 8,727 | `0382feb27519` |
| `results/_coze_online_v3_final_2026_09_18.md` | 11,660 | `5400179aa0e1` |
| `results/_coze_online_v4_d7format_2026_09_26.pdf` | 465,366 | `52f222502a31` |
| `results/_d7_external_advisor_online_publish_v1_20260918.md` | 9,915 | `a75d029036c1` |
| `results/_deemphasis_sha_drift_register_B1_2026_10_06.md` | 1,206 | `56342823a0ca` |
| `results/_deemphasis_sha_drift_register_B2_2026_10_06.md` | 1,418 | `d68f2ef16e70` |
| `results/_deemphasis_sha_drift_register_B3_2026_10_06.md` | 2,830 | `f35523665a53` |
| `results/_deemphasis_sha_drift_register_B4_2026_10_06.md` | 11,715 | `736c19ff59b9` |
| `results/_deemphasis_sha_drift_register_B5_2026_10_06.md` | 14,237 | `3bacf10ffed6` |
| `results/_deemphasis_sha_drift_register_B6a_2026_10_06.md` | 11,696 | `04d96fe5cfa6` |
| `results/_deemphasis_sha_drift_register_B6b_2026_10_06.md` | 22,219 | `add00a68d28a` |
| `results/_deemphasis_sha_drift_register_B6c_2026_10_06.md` | 14,351 | `1603d2ce19cc` |
| `results/_e20_runner_sha_drift_dual_value_register_2026_10_12.md` | 4,352 | `6f88c954c36d` |
| `results/_experiment_execution_plan_v1_1_funnel5_adopted_2026_10_18.md` | 21,411 | `c1d32ba51a59` |
| `results/_gt_reconstruction_sha_drift_dual_value_register_2026_10_12.md` | 4,789 | `7421807680d5` |
| `results/_pi_dual_ruling_register_ge02_acceptance_ge01_readiness_2026_10_12.md` | 19,296 | `a047342a5444` |
| `results/_q2_77_74_62_three_caliber_consolidation_register_2026_10_12.md` | 4,609 | `2fb51610efcf` |
| `results/_repo_state_auth_refresh_register_2026_10_18.md` | 11,449 | `d3ec5cf4e6f1` |
| `results/_s3_kv3s_3_4_judgment_prereg_2026_10_12.md` | 5,678 | `eb9759f2915d` |
| `results/_s3_kv3s_3_4_supplementary_verdict_2026_10_12.md` | 6,156 | `f9c4150ec3dd` |
| `results/_s4_kv3s_4_123_judgment_prereg_2026_10_12.md` | 5,637 | `6b0ecbcfad76` |
| `results/_v2_setup.py._moved_20260924_1830.py` | 3,477 | `a5c77c7dc81d` |
| `results/_v2_show_summary.py._moved_20260924_1830.py` | 1,160 | `f81723551363` |
| `results/_v2_smoketest.py._moved_20260924_1830.py` | 2,042 | `be5610adfb55` |
| `results/_v2_stage1_60cells.py._moved_20260924_1830.py` | 31,470 | `3e528f9919ae` |
| `results/_v2_stage2_f2_drift.py._moved_20260924_1830.py` | 10,760 | `3e821561537b` |
| `results/_v2_stage3_f3_strip.py._moved_20260924_1830.py` | 11,765 | `48a46fa99a97` |
| `results/_v2_stage4_f4_pdv2.py._moved_20260924_1830.py` | 10,307 | `dfeda739c97f` |
| `results/_v2_stage5_f5_dpath.py._moved_20260924_1830.py` | 6,456 | `1550772e0eed` |
| `results/_v2_verify_outputs.py._moved_20260924_1830.py` | 2,544 | `af8148a9fdac` |
| `results/_v4_01_knifeedge_independent_review_2026_09_29.md` | 19,731 | `718926199008` |
| `results/_v5_b14_1_k04_caliber_fixation_2026_09_29.md` | 13,127 | `47a98042d24a` |
| `results/_v5_b14_r3_anchor_retrieval_2026_09_29.md` | 23,023 | `cf395fdb3282` |
| `results/_v5_b16_1dcritical_lit_search_2026_09_29.md` | 26,931 | `c2bcd2e61452` |
| `results/_v5_b16_dual_caliber_rule_2026_09_29.md` | 16,262 | `e8c841c4559e` |
| `results/_v5_b16_idx23_blindrate_verify_2026_09_29.md` | 19,755 | `8c45f5bec3dc` |
| `results/_v5_b16_mq11_case_2026_09_29.md` | 16,723 | `712964f3eb17` |
| `results/_v5_b17_three_caliber_fixation_2026_09_29.md` | 19,709 | `aa13f2945e85` |
| `results/_v5_b18_coding_caliber_2026_09_29.md` | 14,304 | `df968dda4772` |
| `results/_v5_b18_single_count_fixation_2026_09_29.md` | 13,608 | `fd8c3dbd4794` |
| `results/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md` | 18,514 | `a2989b1b5b26` |
| `results/_v5_spec_prereq_reference_archive_2026_10_18.md` | 20,423 | `ddafeb14dccc` |
| `results/_verify_worker_c.py` | 1,155 | `e454eb83619f` |
| `results/verify_ge02_acceptance.py` | 20,212 | `85cfbc2a5a06` |
| `results/verify_ge02_acceptance_results.json` | 1,836 | `ac3e45e5b0a6` |
| `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak` | 23,893 | `c3f0ec7ba9fb` |
| `tmp_movedout_2026_10_01/process_scripts/volcengine_补测_worker_A_2026_09_10.py` | 16,252 | `92ee1bf107cd` |
| `verifier/volcengine_补测_worker_A_2026_09_10.py` | 16,252 | `92ee1bf107cd` |

### §3-2 面② 本地有而远端无 ＝ **补传候选**（**必过排除面**）

**远端无 = 2,527 件 ／ 合计 117,469,302 B**。按排除面归并：

| 排除码 | 件数 | bytes |
|---|---|---|
| **CANDIDATE（未过排除面）** | 209 | 6,735,367 |
| `E1` | 2,046 | 102,174,150 |
| `E2` | 122 | 3,817,751 |
| `E3?` | 23 | 740,812 |
| `E4` | 127 | 4,001,222 |

- **未过排除面之真候选 ＝ 209 件 ／ 6,735,367 B**（分布：`_remote_pullback_2026_10_17` 144、`results` 50、`pi_rulings` 14、`docs` 1）
- `23` 件 **归属待 PI 判定**（`S3` 隐私面之形态命中者）——依冻结件 **X-3** ⛔ **0 妄断**、⛔ **0 自造 `S3` 逐件清单**（逐件路径之唯一源为勘察 JSON，见 `letters/_supplement_s3_s5_deletion_2026_10_18.md:29`）。
- `2046` 件（`.tmp/`，102,174,150 B）：远端前缀面 `.tmp/` 已整面清空（§1-2）⇒ ⛔ **0 回补**。逐件清单见 `.tmp/_mirror_morph_recon_2026_10_18.json` → `face2[code=E1]`。
- `122` 件（`letters/` carve）：**其中 5 件于远端根层遗留面在位**（如 `letters/_codex_c4_values_reply_2026_09_10.md` 等 7 件之对应项）——依冻结件 **M-2** 遗留面不参与映射比对，故仍列本地无；**该重叠之处置归 PI**。
- `127` 件（噪声/S5 族）：见逐件表 §5-3。

#### §3-2-1 真候选（209 件）逐件全表

| 路径 | bytes | 本地 SHA-256-12 | 区 |
|---|---|---|---|
| `_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_2026_09_16.py` | 17,363 | `c5598b13c139` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_baseline_2026_09_16.json` | 1,879 | `483602856618` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/deposon_team/verifier/v42_v2_runs_2026_09_16.jsonl` | 770 | `b471190e579c` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | 10,586 | `ff37f39264bc` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | 13,295 | `00e5d185ef74` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | 22,820 | `b09251018102` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | 7,855 | `c0d629df69d8` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/LETTER_TO_TRAE_REVIEW_2026_09_16.md` | 12,671 | `c086c84e04a6` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/SHA256_MANIFEST.txt` | 552 | `416dda94cb63` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | 9,343 | `ace3c6b390cb` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | 11,575 | `0011b7924dfb` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | 4,784 | `2e6a31af5e4b` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_18.json` | 4,712 | `a729875c0c67` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | 35,690 | `df133892691e` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | 6,433 | `780a8adae5e8` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | 454,307 | `adc99e04ac53` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | 85,627 | `dc761bd8b85d` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_main_runner_2026_09_18.py` | 41,446 | `f3d4ec483599` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_md_report_only_2026_09_18.py` | 13,694 | `7a5be4aef9ac` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | `0a1e91d6f772` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_2026_09_18.py` | 5,452 | `c917f8fa142c` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` | 2,938 | `0b7e50a8a036` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` | 34,134 | `18984b04c45e` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_final_sha_2026_09_18.py` | 2,678 | `0769f60a0504` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch2_2026_09_18.py` | 4,100 | `81bb1751be4c` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` | 3,207 | `01e63e488ce2` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch4_2026_09_18.py` | 8,225 | `2efcd5ff42f1` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` | 2,214 | `1c59e7b803fe` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch7_2026_09_18.py` | 4,261 | `389283c51275` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch8_2026_09_18.py` | 2,249 | `5057ccf97d6b` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_d05_rescue_2026_09_18.py` | 3,524 | `2c2cc3ff542a` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | 11,390 | `5610a549e116` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | 18,611 | `dc3e56adc3fc` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | 12,813 | `f4610b0bb47c` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_glm_ftfb_deep_revision_2026_09_18.md` | 26,990 | `3de722dc9e39` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md` | 10,307 | `affe5eebf2e7` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_v2_2026_09_17.md` | 13,967 | `6d95317f4355` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` | 13,592 | `05f92d837412` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | 22,591 | `8b22a026f30b` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_mavis_full_mirror_request_2026_09_17.md` | 9,717 | `f2934e5279e6` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | 10,702 | `b75ba5c152b7` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_p_i_curvature_audit_probe_runner_2026_09_16.py` | 12,919 | `e05555deb611` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.json` | 1,393 | `49dde3059959` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_4versions_diff_2026_09_17.py` | 2,720 | `93527eb7b2f7` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_direct_2026_09_17.py` | 2,371 | `9bcfe80c0dd0` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_doubao_emb_via_proxy_2026_09_17.py` | 2,589 | `f2818fc2ddff` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_probe_teamo_via_proxy.py` | 2,841 | `dce965058076` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_openai_more.py` | 2,187 | `e11319f32dc5` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_one.py` | 2,119 | `63eb0a0aa102` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_sanity_teamo_three.py` | 3,540 | `888d02cd1443` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/compile_verification.txt` | 9,663 | `463fc7575663` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.pdf` | 356,123 | `2d9edc8c7303` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.tex` | 93,324 | `d060f75dbe9f` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back_source.md` | 84,388 | `543479649b3e` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | 8,257 | `7243192d86be` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/p_i_curvature_audit_probe_results_2026_09_16.json` | 2,637 | `ae07f5551e87` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | 20,082 | `5198a7059c06` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A1_glm51.md` | 7,617 | `fd38a2a1ea05` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_content_A2_kimik3.md` | 24,843 | `a964defb923d` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` | 30,494 | `0d36d7cd0589` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_grok46.md` | 18,923 | `09784ff172b3` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B2_grok46.md` | 13,726 | `fe80bad08eef` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | 8,098 | `8d00c6d4a242` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/戴夫_FTFB双审包简报v3_2026-09-17.md` | 8,419 | `6952b3b02b96` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v3_2026_09_18.md` | 7,476 | `53c9c1ab2d12` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v3_d7format_2026_09_18.md` | 8,727 | `debe3761c565` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v3_final_2026_09_18.md` | 11,660 | `36439bc12bba` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf` | 465,366 | `a82881653520` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_coze_paper_v1_draft_2026_09_17.md` | 29,511 | `2832800ceca6` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/results/_coze_paper_v1_summary_2026_09_17.md` | 3,624 | `2efdc3d7741d` | repo |
| `_remote_pullback_2026_10_17/_september_workspace/verifier/volcengine_补测_worker_A_2026_09_10.py` | 16,252 | `20b8a2f54ad9` | repo |
| `_remote_pullback_2026_10_17/letters/_v5_rj5_external_rederive_reply_codex_2026_09_29.md` | 27,835 | `c706e69d00fc` | repo |
| `_remote_pullback_2026_10_17/results/Deposon_评估汇总_v1_3_0.json` | 2,811 | `2f02f50c164b` | repo |
| `_remote_pullback_2026_10_17/results/MANIFEST_large_files.md` | 3,816 | `b138fb94ca71` | repo |
| `_remote_pullback_2026_10_17/results/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | `0a1e91d6f772` | repo |
| `_remote_pullback_2026_10_17/results/_trae_anchor_18_audit_20260917_193000.md` | 3,449 | `4af67e6cbe71` | repo |
| `_remote_pullback_2026_10_17/results/_trae_corpus_5_audit_20260917_193000.md` | 3,467 | `f2a655cd5e54` | repo |
| `_remote_pullback_2026_10_17/results/_trae_d7_v1_audit_20260917_190000.json` | 4,253 | `3184b30b7b0d` | repo |
| `_remote_pullback_2026_10_17/results/_trae_d7_v1_audit_20260917_190000.md` | 7,863 | `41c142eab4a1` | repo |
| `_remote_pullback_2026_10_17/results/_trae_kimi_push_v3_audit_20260917_193000.md` | 3,281 | `8ece24be6b8a` | repo |
| `_remote_pullback_2026_10_17/results/_trae_paper_8ch_双审_20260917_200000.md` | 4,044 | `145abbb9c365` | repo |
| `_remote_pullback_2026_10_17/results/attacker_xl_cache/algorithm_process.json` | 5,353 | `1878428d3c90` | repo |
| `_remote_pullback_2026_10_17/results/attacker_xl_cache/biological_taxonomy.json` | 5,036 | `8e11c03b11cf` | repo |
| `_remote_pullback_2026_10_17/results/attacker_xl_cache/geography_world.json` | 5,314 | `3977f0ab6a28` | repo |
| `_remote_pullback_2026_10_17/results/attacker_xl_cache/historical_causality.json` | 4,389 | `9d4b5a29decf` | repo |
| `_remote_pullback_2026_10_17/results/attacker_xl_cache/physics_concepts.json` | 5,874 | `9ca7c11860f6` | repo |
| `_remote_pullback_2026_10_17/results/attacker_xl_cache/project_management.json` | 4,541 | `e19e1137258e` | repo |
| `_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_labelfree.json` | 3,011 | `57f06a426bec` | repo |
| `_remote_pullback_2026_10_17/results/deposon_benchmark_v1_3_resonant.json` | 3,134 | `769ae8c908c9` | repo |
| `_remote_pullback_2026_10_17/results/deposon_benchmark_v1_4_sc5.json` | 12,479 | `c9796d3b3263` | repo |
| `_remote_pullback_2026_10_17/results/deposon_g3_arrhenius.json` | 2,284 | `a3de045b5dd7` | repo |
| `_remote_pullback_2026_10_17/results/deposon_v16_llm_prior_summary.json` | 5,517 | `a7952d9d78db` | repo |
| `_remote_pullback_2026_10_17/results/deposon_v20_familyL_ingest.json` | 1,304 | `d7c2d9fee5b2` | repo |
| `_remote_pullback_2026_10_17/results/familyL_cache/algorithm_process.json` | 1,442 | `611f346091b9` | repo |
| `_remote_pullback_2026_10_17/results/familyL_cache/biological_taxonomy.json` | 1,296 | `1a6bf80e22ca` | repo |
| `_remote_pullback_2026_10_17/results/familyL_cache/geography_world.json` | 1,319 | `d5afc69e2fb3` | repo |
| `_remote_pullback_2026_10_17/results/familyL_cache/historical_causality.json` | 1,622 | `db30c0e7bd33` | repo |
| `_remote_pullback_2026_10_17/results/familyL_cache/physics_concepts.json` | 1,253 | `9963951cf859` | repo |
| `_remote_pullback_2026_10_17/results/familyL_cache/project_management.json` | 1,346 | `48faa9bf14fa` | repo |
| `_remote_pullback_2026_10_17/results/familyL_prior_cache/algorithm_process.json` | 2,061 | `b302e5f54141` | repo |
| `_remote_pullback_2026_10_17/results/familyL_prior_cache/biological_taxonomy.json` | 2,231 | `8014873eee66` | repo |
| `_remote_pullback_2026_10_17/results/familyL_prior_cache/geography_world.json` | 2,314 | `7056a5298bff` | repo |
| `_remote_pullback_2026_10_17/results/familyL_prior_cache/historical_causality.json` | 3,034 | `6e032f3a58ac` | repo |
| `_remote_pullback_2026_10_17/results/familyL_prior_cache/physics_concepts.json` | 2,596 | `9eae1fa8fd7c` | repo |
| `_remote_pullback_2026_10_17/results/familyL_prior_cache/project_management.json` | 1,895 | `3467c1985133` | repo |
| `_remote_pullback_2026_10_17/results/gt2_attacker_cache/algorithm_process.json` | 2,783 | `7ad7b97486e8` | repo |
| `_remote_pullback_2026_10_17/results/gt2_attacker_cache/biological_taxonomy.json` | 2,386 | `f7c9a3344c54` | repo |
| `_remote_pullback_2026_10_17/results/gt2_attacker_cache/historical_causality.json` | 2,342 | `b9f8f472b2f9` | repo |
| `_remote_pullback_2026_10_17/results/gt2_attacker_cache/physics_concepts.json` | 2,387 | `ec91290fbddc` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__algorithm_process.json` | 3,315 | `fb255ad93ec9` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__biological_taxonomy.json` | 2,564 | `d50690ff2279` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__geography_world.json` | 2,847 | `7830ece1d516` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__historical_causality.json` | 2,851 | `d556c647747d` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__physics_concepts.json` | 2,176 | `8bc5467ced92` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/deepseek-v4-pro-260425__project_management.json` | 2,083 | `23863deac9a3` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__algorithm_process.json` | 498 | `3e0173feb34d` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__biological_taxonomy.json` | 2,362 | `f6db5e6b980f` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__geography_world.json` | 2,475 | `4925ec2a5ca1` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__historical_causality.json` | 501 | `aedf8a050cb3` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__physics_concepts.json` | 2,013 | `6dd47c33fb27` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/doubao-seed-evolving__project_management.json` | 1,719 | `ebae449cf921` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__algorithm_process.json` | 479 | `669da0e1c36b` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__biological_taxonomy.json` | 2,350 | `51746e4094dc` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__geography_world.json` | 2,499 | `29cce1102bba` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__historical_causality.json` | 2,500 | `9506ad922380` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__physics_concepts.json` | 2,006 | `bd828a9e748b` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/kimi-k2-thinking__project_management.json` | 480 | `540a9ef09bf0` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__algorithm_process.json` | 2,737 | `b0dc14fac249` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__biological_taxonomy.json` | 2,324 | `769991471ad1` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__geography_world.json` | 2,495 | `b7cce4938263` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__historical_causality.json` | 2,649 | `202e2e38a573` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__physics_concepts.json` | 2,540 | `6081c483c999` | repo |
| `_remote_pullback_2026_10_17/results/gt3_prior_cache/moonshot-v1-8k__project_management.json` | 478 | `8896856f7e65` | repo |
| `_remote_pullback_2026_10_17/results/llm_prior_cache.json` | 938 | `5f16be89efc5` | repo |
| `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contamination.json` | 639 | `d3f72f67977d` | repo |
| `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_contentless.json` | 512 | `7c0d169ef164` | repo |
| `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction.json` | 2,168 | `023f936f80fb` | repo |
| `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction_run1_malformed_archive.json` | 655 | `d5526e712e99` | repo |
| `_remote_pullback_2026_10_17/results/llm_prior_cache_v18_labelshuffle.json` | 1,925 | `8dce6d7618a2` | repo |
| `_remote_pullback_2026_10_17/results/v19_edges_audit_input.csv` | 2,186 | `8b6682181392` | repo |
| `_remote_pullback_2026_10_17/results/v20_graph_features.csv` | 2,151 | `f95f382ace44` | repo |
| `_remote_pullback_2026_10_17/results/v20_regression_field_v2.json` | 4,236 | `3596490e1fc0` | repo |
| `_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_deg.json` | 988 | `dfe014c627ca` | repo |
| `_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_rand.json` | 868 | `1dadfaeb2c43` | repo |
| `docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | 8,037 | `935cb6ee3566` | sub |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v100.md` | 40,128 | `ecf15a92456b` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v101.md` | 46,191 | `7102e7010fcb` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v102.md` | 57,912 | `363c02a81a8f` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v103.md` | 68,524 | `fbd5681f613d` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v90.md` | 35,256 | `c2b848aa30e4` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v91.md` | 35,197 | `32ace0c9d022` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v92.md` | 46,595 | `b68c7be93524` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v93.md` | 51,967 | `f3359165cac0` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v94.md` | 32,030 | `5a042d598ab2` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v95.md` | 28,959 | `6518d7c1233f` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v96.md` | 49,227 | `1b3f5228668d` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v97.md` | 33,410 | `df1907e61fd3` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v98.md` | 46,786 | `a9c973d9a7af` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_18_v99.md` | 50,107 | `b0d8b8ed7857` | repo |
| `results/_achievements_inventory_full_2026_10_18.md` | 805,428 | `515ad357fac8` | repo |
| `results/_archive_2026_09_20/LETTER_TO_WANG_TEACHER_2026_09_18_FINAL.md` | 10,562 | `7d4b5dd967e2` | sub |
| `results/_archive_2026_09_20/_coze_〔IM〕_v3_d7format_2026_09_18.pdf` | 454,307 | `adc99e04ac53` | sub |
| `results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | 2,292 | `0a1e91d6f772` | sub |
| `results/_archive_2026_09_20/_letter_to_coze_〔IM〕_v2_2026_09_18.md` | 18,596 | `ecdbf3a7a9c2` | sub |
| `results/_clearance_materials_register_2026_10_08.md` | 45,254 | `356eb1c53986` | sub |
| `results/_closure_sweep_r2_2026_10_18.md` | 121,848 | `31a03b8d756b` | repo |
| `results/_commission_v04_approval_rulings_effect_2026_10_18.md` | 67,299 | `d13f3ed169e3` | repo |
| `results/_commission_v04_ghost_reference_erratum_2026_10_18.md` | 37,518 | `482eca247fa7` | repo |
| `results/_consolidated_pending_rulings_scroll_2026_10_18.md` | 104,340 | `df894c9acc2a` | repo |
| `results/_coze_〔IM〕_v3_2026_09_18.md` | 7,466 | `229d76e1b86f` | sub |
| `results/_coze_〔IM〕_v3_d7format_2026_09_18.md` | 8,715 | `905544775aee` | sub |
| `results/_coze_〔IM〕_v3_final_2026_09_18.md` | 11,657 | `deee45f45c5d` | sub |
| `results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | 465,366 | `a82881653520` | sub |
| `results/_d7_wang_teacher_〔IM〕_publish_v1_20260918.md` | 9,891 | `f4d5b755736a` | sub |
| `results/_deemphasis_verification_register_2026_10_08.md` | 27,322 | `3f806e44a13f` | sub |
| `results/_eta_preexp_wait_and_leveling_effect_2026_10_18.md` | 32,594 | `a79b0ca9ce9e` | repo |
| `results/_five_zero_recheck_evidence_2026_10_18.md` | 37,035 | `193d11089327` | repo |
| `results/_freeze_final_replay_2026_10_18.md` | 31,254 | `a95605c38bac` | repo |
| `results/_h_face_external_evidence_eval_2026_10_18.md` | 35,016 | `22cbba5aefb8` | repo |
| `results/_h_face_freeze_ruling_effect_2026_10_18.md` | 28,087 | `3aa3bcc56258` | repo |
| `results/_historical_ forgetting_recheck_2026_10_18.md` | 34,941 | `19b73ab478f5` | repo |
| `results/_kickoff_decisions_register_2026_10_08.md` | 16,388 | `6ee5d2b8323c` | sub |
| `results/_kimi_postexec_receipt_verification_2026_10_18.md` | 21,678 | `d51ff0c7776d` | repo |
| `results/_kimi_preexec_final_rulings_effect_2026_10_18.md` | 42,226 | `7828c5300fdf` | repo |
| `results/_kimi_receipt_authority_rulings_effect_2026_10_18.md` | 62,860 | `789fed8aacc7` | repo |
| `results/_md_a_field_composition_draft_2026_10_18.md` | 58,572 | `121a3b861261` | repo |
| `results/_morning_brief_pending_rulings_2026_10_18.md` | 37,227 | `9ed6dfdbc62e` | repo |
| `results/_next_stage3_dir_optimization_ruling_2026_10_18.md` | 11,599 | `015b4e200103` | repo |
| `results/_pending_residual_minimal_set_2026_10_18.md` | 53,502 | `0f6098f36bd0` | repo |
| `results/_pending_rulings_triage_2026_10_18.md` | 63,300 | `19c91a3bf7e8` | repo |
| `results/_post_execution_report_kimi_2026_10_18.md` | 7,251 | `316ea6b69adb` | repo |
| `results/_pre_execution_report_kimi_2026_10_18.md` | 6,969 | `6fe6a91f8adf` | repo |
| `results/_r2_sep_endogeneity_erratum_2026_10_18.md` | 41,770 | `ed5591c3c38d` | repo |
| `results/_remote_delete_face_pullback_register_2026_10_18.md` | 82,690 | `0cc9a822c008` | repo |
| `results/_remote_residual_disposal_execution_order_2026_10_08.md` | 36,486 | `602c4d09623d` | sub |
| `results/_reply_letter_approval_effect_2026_10_18.md` | 38,991 | `d08b3e69e165` | repo |
| `results/_ruled_unclosed_closure_verdict_2026_10_18.md` | 54,716 | `03fe4d044c78` | repo |
| `results/_scroll_wave1_four_rulings_effect_2026_10_18.md` | 51,739 | `2813eea5584a` | repo |
| `results/_scroll_wave2_four_rulings_effect_2026_10_18.md` | 51,949 | `57881886e428` | repo |
| `results/_scroll_wave4_three_rulings_effect_2026_10_18.md` | 51,604 | `0db1e827d943` | repo |
| `results/_scroll_wave5_four_rulings_effect_2026_10_18.md` | 71,453 | `c44183973483` | repo |
| `results/_stage3_close_and_cmp2_rulings_effect_2026_10_18.md` | 54,315 | `22843cb2ce08` | repo |
| `results/_stage5_preparation_design_2026_10_18.md` | 43,856 | `20ad343fb8d3` | repo |
| `results/_thirdparty_16_overwrite_necessity_2026_10_18.md` | 14,122 | `6435ecc3a540` | repo |
| `results/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md` | 43,428 | `322582749c53` | repo |
| `results/_u10_fail_h0_verdict_2026_10_18.md` | 59,918 | `0884b8f98b96` | repo |
| `results/_u10_s3_denominator_rulings_effect_2026_10_18.md` | 79,234 | `97719ffddda6` | repo |
| `results/_unique_supplement_letter_approval_effect_2026_10_18.md` | 51,238 | `2a57f6c78d52` | repo |
| `results/_v34_experiment_gap_plan_2026_10_08.md` | 36,066 | `996feb1db9cb` | repo |

#### §3-2-2 `S3` 隐私面形态命中（23 件 · **归属待 PI 判定 · ⛔ 0 断言其归属**）

| 路径 | bytes | 本地 SHA-256-12 | 区 |
|---|---|---|---|
| `audits_dataset_health.json` | 7,398 | `4f827071b0b8` | repo |
| `docs/DATASET_HEALTH_v2.md` | 4,892 | `c87a0c1f5af6` | sub |
| `results/_v4_pi_cot_v2_dataset.json` | 12,672 | `7b01cd835a41` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | 4,103 | `172093a23e4b` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | 6,132 | `439721007aaf` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | 7,566 | `41d6c28ca87c` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | 6,666 | `99c58906f792` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | 7,668 | `c6d092f77932` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | 10,257 | `26f110a6e571` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | 11,589 | `6e104e2db038` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | 14,722 | `d96b747bfc6c` | repo |
| `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | 19,615 | `401bd614cdf7` | repo |
| `results/_v4_pi_cot_v3_dataset.json` | 16,025 | `5118f5b44f17` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | 20,194 | `cbf60a630c9f` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | 18,714 | `6eed9acdb99a` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | 16,587 | `990c0c42a6f6` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | 19,214 | `9669efa804b7` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | 27,009 | `5d94a8617b5b` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | 58,581 | `b02ef31f1e4e` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | 374,072 | `769ef8b71462` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | 46,909 | `b9026cbf5ca2` | repo |
| `results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | 17,252 | `c0ebbd1f4633` | repo |
| `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | 12,975 | `ed596914259a` | repo |

### §3-3 面③ 同名异内容 ＝ **碰撞**

**514 件**。其中 **repo 区命中 157 件** ＋ **仅 sub 区命中 357 件**（双区皆命中者 **0** 件）。
按一级分布：

- `results` — **396**
- `docs` — **47**
- `deposon_team` — **33**
- `pi_rulings` — **10**
- `(根层文件)` — **7**
- `tmp_movedout_2026_09_28` — **6**
- `tmp_movedout_2026_10_09` — **5**
- `verifier` — **5**
- `.trae` — **4**
- `corpus` — **1**

⚠ **口径提示**：面③ 之「同名」为**映射后**之同名；「异内容」为 **Git-blob-SHA1-12 不等**（非 SHA-256——见 §7 仪器修正）。

**逐件全表**（514 件 · 路径 · 远端 SHA-1-12 · 本地 SHA-1-12 · 本地区）：

| 路径（映射后） | 远端 SHA-1-12 | 本地 SHA-1-12 | 命中区 |
|---|---|---|---|
| `.gitignore` | `b23ed435697e` | `4fc0d746af9d` | repo |
| `.trae/audit/compare_versions.py` | `75600d25d0a0` | `8dbcfd895147` | sub |
| `.trae/scripts/_arxiv_renumber.py` | `2292a3044e55` | `941186a880eb` | repo |
| `.trae/scripts/_md_to_tex.py` | `cb94bef12c8c` | `0cb552ec5e5c` | sub |
| `.trae/scripts/_verify_tex.py` | `6bcf5ed11826` | `175dc4a91dfd` | repo |
| `README_V4_2026_09_29.md` | `c5e19f40a90b` | `0dd479174923` | repo |
| `_movedout_manifest_2026_09_21.json` | `8a16a7461a32` | `cc54f4651dd5` | sub |
| `_p_l_v3_phase1_finalize_2026_09_17.py` | `f8110f41c607` | `f331ec408237` | sub |
| `_p_l_v3_phase1_runner_2026_09_17.py` | `3a5af3e5448e` | `48df0b6a3912` | sub |
| `_p_l_v3_phase2_finalize_2026_09_17.py` | `56b4aa16d2e2` | `89428f44b4fd` | sub |
| `corpus/v20_caption_surface/_inspect_captions.py` | `207a74970678` | `6c3e6486863a` | repo |
| `deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md` | `4ac42cc84dac` | `cc5c70304a3b` | sub |
| `deposon_team/_designs/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md` | `dffe99f8d9fa` | `4e6fb3cd79f0` | sub |
| `deposon_team/_designs/EXTERNAL_AGENT_PROMPTS_2026_09_16.md` | `2f1b9580912e` | `6a85015b4bcc` | sub |
| `deposon_team/_designs/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md` | `775144c54f1b` | `055bc73a2d73` | sub |
| `deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` | `da84d81aa976` | `2d74e577c187` | sub |
| `deposon_team/_designs/V3X_KIMI_7_DIRECTIONS_FULL_ACCEPT_2026_09_16.md` | `a26392eb0e96` | `60b461305794` | sub |
| `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` | `f61a9452e2c8` | `1a4d1e7d6da8` | sub |
| `deposon_team/_designs/V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md` | `025c158f7feb` | `491b440556c7` | sub |
| `deposon_team/_designs/v3x_dispatch_log_2026_09_16.md` | `ee4eddfad35f` | `dd123717a9b7` | sub |
| `deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_16.py` | `c901b65dd9e7` | `b5f2c9566b9a` | sub |
| `deposon_team/plugins/_pg_v01_compute.py` | `edb4685a740b` | `6c0f873ee979` | repo |
| `deposon_team/plugins/_tdf_s1_2026_10_12.py` | `2df029e81991` | `18aa51927654` | repo |
| `deposon_team/plugins/_tdf_s1b_2026_10_12.py` | `5908015bb22a` | `a5c5396ad589` | repo |
| `deposon_team/plugins/_tdf_s1c_2026_10_12.py` | `e88528dbc37e` | `62823388e682` | repo |
| `deposon_team/plugins/_tdf_s2_apply_2026_10_12.py` | `6778a10ac0e3` | `139831d429c6` | repo |
| `deposon_team/plugins/_tdf_s3_jumps_2026_10_12.py` | `a0c386e92374` | `fb8e290bfd7c` | repo |
| `deposon_team/plugins/_tdf_s3b_2026_10_12.py` | `84394f9e5ee6` | `72b9df5b6a46` | repo |
| `deposon_team/plugins/_tdf_s4_final_2026_10_12.py` | `ecfa39768f34` | `e13bb36e5115` | repo |
| `deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` | `f31efedb713a` | `b0eace8ec8e2` | repo |
| `deposon_team/plugins/_v3x_experiments_runner_2026_09_16.py` | `ab1a25ac9008` | `3cb8210fad59` | sub |
| `deposon_team/plugins/boss_pa_1_rbr_rm.py` | `2e563e9fd165` | `130a9243459c` | repo |
| `deposon_team/plugins/boss_pa_2_potential_game.py` | `48e3ca1d1ccf` | `5d9b2a9d09e0` | repo |
| `deposon_team/plugins/boss_pa_3_replicator_dynamics.py` | `3cb86ea403ad` | `1188df982a6a` | repo |
| `deposon_team/plugins/boss_pg_1_riemannian_degenerate.py` | `f4dbf7158e55` | `0eefab43756f` | repo |
| `deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py` | `e0a794481e41` | `0c281108d168` | repo |
| `deposon_team/plugins/boss_pg_3_geodesic_violation.py` | `497d2a008357` | `2c3733c33e68` | repo |
| `deposon_team/plugins/fix_boss_naming_2026_09_16.py` | `9f1e923dd24a` | `a5caf1ab955e` | sub |
| `deposon_team/plugins/git_commit_msg_2026_09_18.txt` | `f32b043fd6e4` | `2eac85fb882c` | sub |
| `deposon_team/plugins/runner_pa_d1_d3.py` | `414aeeaaf803` | `f86ad10c7546` | sub |
| `deposon_team/plugins/skill_a_p_a_60cells.py` | `3565dd4edb1c` | `b976b9b4c012` | repo |
| `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `a675bae218b4` | `0685f3b8e3e7` | repo |
| `deposon_team/plugins/skill_c_p_e_3modality.py` | `d46e9dd7ab4f` | `a715ea8b2ac4` | repo |
| `deposon_team/plugins/skill_d_p_f_observer.py` | `471b37678096` | `72b60627ae8e` | repo |
| `docs/THINKING_V3_GT_CONTRIB_2026.md` | `69fa556aa47a` | `bdff8f21fd4b` | sub |
| `docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | `5ccceefbaa16` | `6cbdb8a30b67` | sub |
| `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `d1462f7a0baf` | `04fb77528dd7` | sub |
| `docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | `515954f5c09f` | `125e4d964195` | sub |
| `docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | `de51c39ddedc` | `f01a1cc5eaf1` | sub |
| `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | `c7f2a4404206` | `6f4c3eeb5535` | sub |
| `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `27523eab8450` | `8de2b05450ee` | sub |
| `docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | `90e26e14f4fd` | `715c1f0dc814` | sub |
| `docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | `e16d2a5f8ecd` | `4a2e40146733` | sub |
| `docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | `b891bb4004c6` | `1cec787a560b` | sub |
| `docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | `d9b81cfc1571` | `361a2d931834` | sub |
| `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | `909fabce2d8b` | `6fc89b797fe7` | sub |
| `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `3baf552bab87` | `393a3fc80c9f` | sub |
| `docs/V3X/KT_A1_SPEC_V0.1.md` | `db69ddfd15d8` | `7d6dfe1f4eda` | sub |
| `docs/V3X/KT_B1_SPEC_V0.1.md` | `2536948d64ee` | `940006093502` | sub |
| `docs/V3X/KT_C1_SPEC_V0.1.md` | `53fa9d2e5398` | `055aad216dec` | sub |
| `docs/V3X/KT_D0_EVIDENCE_CARD.md` | `f78b5f420d57` | `63972e1033aa` | sub |
| `docs/V3X/KT_D0_SPEC_V0.1.md` | `dcb9123bb035` | `bc762d59c7e7` | sub |
| `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | `816d56eeb283` | `6e3cba12a493` | repo |
| `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `85f4334d29be` | `1c5b3ed69ca9` | sub |
| `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `cf1f3d2f858c` | `bc143648210b` | repo |
| `docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` | `995354ff82be` | `a27a999a6b15` | repo |
| `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `bc57b2d877a6` | `0da4511f1871` | sub |
| `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `0e3f19a48a69` | `457e047806fb` | sub |
| `docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | `3077f29a3205` | `28346d2f86f8` | repo |
| `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | `629dd923bdab` | `1c5043645e0a` | sub |
| `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | `2440a613ed72` | `06e29336a9f5` | sub |
| `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | `d1f45c8fb34f` | `408a90fa6232` | sub |
| `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `01059346371f` | `ce690e4ce268` | sub |
| `docs/V3X/P_F_SPEC_V0.md` | `44d0481664e4` | `c29f76df5176` | sub |
| `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | `40ff107b5181` | `0fd35fe37e93` | repo |
| `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | `a1b52ba63522` | `7deae7d94d84` | sub |
| `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | `5302dfea87da` | `55959b4fb5cb` | sub |
| `docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | `b8c68387046b` | `5ff00ac7b033` | sub |
| `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | `52335388369a` | `6543cc061a0f` | sub |
| `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | `9dd3cea98340` | `5f3db9e28825` | sub |
| `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | `c4e7a025ab3b` | `297ed7a2fc7f` | sub |
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | `8da06df0e058` | `eefd063ad479` | repo |
| `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `0debb6baba97` | `9cbee701b3cf` | sub |
| `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | `dc9183d82725` | `017ecfad9398` | sub |
| `docs/V3X/V3X_D6_PAPER_zh.md` | `78577e0de271` | `81481ab42557` | sub |
| `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | `9b5bbb811a91` | `ffa64ca51a96` | repo |
| `docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | `04b5307e1392` | `1d9bcb5a129f` | sub |
| `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `dac61c7effde` | `cc3b4360b07d` | sub |
| `docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | `3f4c25025250` | `2365a5726c45` | sub |
| `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | `0da3bc43cd7c` | `efd96910a6cb` | sub |
| `docs/V3X_COLLAB_DIRECTIONS.md` | `8764166830d0` | `145b10540c03` | sub |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v46.md` | `62910e2b2dff` | `620073ef5561` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v54.md` | `6396645627f1` | `2398939250c8` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v72.md` | `fcc9e3a4ac13` | `f93a2ae209ef` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v80.md` | `6188dbda5e77` | `7aaa84998c57` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v81.md` | `c68062107ee4` | `4eea36bde7de` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v82.md` | `b43ea3881756` | `8aa524b1592d` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v83.md` | `1b916be2cd26` | `2c3fe107ce13` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v85.md` | `75fb0b94f171` | `088a40aff6be` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v86.md` | `8f44312eeae7` | `0948a85ad530` | repo |
| `pi_rulings/_pi_card_answers_register_2026_10_17_v87.md` | `0e617b1f4efc` | `e1e39abb7557` | repo |
| `results/_a02_excluded_items_idx_collection_2026_10_10.md` | `4a89109b9893` | `c114ca7ac083` | sub |
| `results/_achievements_inventory_full_2026_10_09.md` | `acb25540ac22` | `15e1fe3487f3` | repo |
| `results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | `8c694436358f` | `343ba0d8fc9d` | sub |
| `results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md` | `1b17763e4fc7` | `696df8c7a7d2` | sub |
| `results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | `484df38a6e46` | `5e39d4d5c4e4` | sub |
| `results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md` | `004e79c610af` | `4fbc5f44b85f` | sub |
| `results/_archive_2026_09_18/_trae_paper_8ch_双审_20260917_200000.md` | `4f92d3020764` | `841129fdb226` | sub |
| `results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | `e6599255e59d` | `efa395432cea` | sub |
| `results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | `37c28c9d515a` | `96b6f14391dd` | sub |
| `results/_archive_2026_09_20/LETTER_TO_TRAE_REVIEW_2026_09_16.md` | `5dc3c0faffed` | `c54c335b9191` | sub |
| `results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | `f86ca7abd474` | `791d76fb21bf` | sub |
| `results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | `938102d0e310` | `b029a65dea3a` | sub |
| `results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | `dcad9d2da5bd` | `c3949f1697cf` | sub |
| `results/_archive_2026_09_20/_d05_sanity_3backbone_2026_09_18.py` | `72854074e603` | `06c54e651f5d` | sub |
| `results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | `a4489af68f91` | `c5a3928a78c7` | sub |
| `results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | `22c18e6d3604` | `4df1be8a1ae5` | sub |
| `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md` | `e5615dfdf907` | `44a34ebc568d` | sub |
| `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_v2_2026_09_17.md` | `f0ee0664b7e3` | `d974ae78325e` | sub |
| `results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` | `691137aa0627` | `7c0b6c9a660d` | sub |
| `results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | `0dd53df5dccb` | `4fed50ef4e6e` | sub |
| `results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | `35362d1a6671` | `8db3d1ed2746` | sub |
| `results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | `3df594818649` | `11b86a0b6061` | sub |
| `results/_archive_2026_09_24/_inspect_captions.py` | `207a74970678` | `6c3e6486863a` | sub |
| `results/_archive_2026_09_24/_verify_worker_c.py` | `a22aa0b2ddea` | `e454eb83619f` | sub |
| `results/_archive_2026_09_24/_volc_22cap_emb.py` | `c7f9aceeaa08` | `987fd959ce49` | repo |
| `results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | `5332c33c3466` | `6ce92f706bdd` | sub |
| `results/_archive_ledger_rectification_register_2026_10_09.md` | `31d356a8ff63` | `6d9bc4c95e8e` | sub |
| `results/_archive_manifest_deposon_sub_2026_09_23.json` | `60238391952b` | `d187a39a467d` | repo |
| `results/_archive_manifest_non_upload_2026_09_23.json` | `4bfc21e8edfc` | `8ff03f326118` | repo |
| `results/_archive_manifest_non_upload_v2_2026_09_28.json` | `6dd94f28c8d1` | `1fb30bb77100` | sub |
| `results/_archive_manifest_non_upload_v3_2026_09_28.json` | `0f34b6d8b8e6` | `71f86b4b11c4` | sub |
| `results/_axis1_three_recomputations_2026_10_11.md` | `8a85318ae33e` | `1d0857087ccf` | sub |
| `results/_b01_new_key_classification_2026_10_10.md` | `f479531ce574` | `85a23e2ac195` | sub |
| `results/_b01_new_key_residue_judgment_2026_10_10.md` | `cbd82437ff52` | `a5fbdfb9265b` | sub |
| `results/_b01_p_counting_recompute_2026_10_10.md` | `941424bc6d71` | `37ab9642da7b` | sub |
| `results/_b01_recompute_authorization_supplement_2026_10_11.md` | `82b0af3f4730` | `fe1fc73afb48` | sub |
| `results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | `e63e29fe22a0` | `30cb0056be0a` | sub |
| `results/_b14_audit_f2f3_closure_register_2026_10_11.md` | `dc21e594ae6a` | `330cf31449c0` | sub |
| `results/_b14_vk_evidence_audit_2026_10_10.md` | `7da95eb67e06` | `580177f1eb35` | sub |
| `results/_batch8_deliberation_judgment_2026_10_14.md` | `3305435b7d67` | `4d3846018f4e` | repo |
| `results/_batch9_deliberation_judgment_2026_10_14.md` | `37a49fbe40b0` | `756c35dc0436` | repo |
| `results/_c2_criterion_third_tier_draft_2026_10_11.md` | `c17c103993f3` | `c0d7213a09fa` | sub |
| `results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | `ec5eb05066a9` | `d05d668a6c50` | sub |
| `results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | `b5004c027d08` | `44ed4e1dbd49` | sub |
| `results/_c4_theory_source_caliber_correction_2026_09_30.md` | `8b7c48eea3da` | `4976d49dc233` | sub |
| `results/_c4_unblock_reply_independent_review_2026_10_10.md` | `ef0bb966d450` | `25829e1b7260` | sub |
| `results/_c8_c2_disposition_register_2026_10_11.md` | `a57424c19d1d` | `774e2e98ab1f` | sub |
| `results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | `1631ae2d6777` | `3c8a0039b3c4` | sub |
| `results/_c_component4_three_items_judgment_2026_10_11.md` | `d523d9bea24e` | `1e8427ebf11c` | sub |
| `results/_charlie_delivery_register_2026_10_08.md` | `91d92fd7a88b` | `df5a43c97f7b` | sub |
| `results/_chd_construction_domain_declaration_draft_2026_10_10.md` | `437f828e6dbd` | `a73d123433be` | repo |
| `results/_cleanup_round_2026_10_08.md` | `2feaa54a9800` | `84d19c144ab1` | sub |
| `results/_clearance_evening_round_register_2026_09_29.md` | `c3634de6f3fd` | `b63c8170c3d3` | repo |
| `results/_clearance_round_1_register_2026_10_08.md` | `00a941c68be1` | `c12334453b58` | sub |
| `results/_clue_side_dual_and_glm_commission_open_register_2026_10_12.md` | `3e6459931d3f` | `4c3b66a53650` | repo |
| `results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | `e7a1b16d5559` | `9e8ac3f39e98` | sub |
| `results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | `45fe997ff1e4` | `e221b31c229a` | sub |
| `results/_codex_c4_values_reply_intake_register_2026_10_10.md` | `5c8994056166` | `281a81f02a88` | sub |
| `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | `a9235f93834e` | `b2bca9e0cc97` | sub |
| `results/_collision_baseline_update_and_disposition_2026_10_17.md` | `47f13ee7d3ba` | `2698f065da52` | repo |
| `results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | `6812ceb67f0a` | `3d38e496a803` | sub |
| `results/_coze_paper_v1_draft_2026_09_17.md` | `56568828a7bc` | `811ed5083780` | sub |
| `results/_d1_backfill_intake_verdict_2026_10_01.md` | `ecd9f5463bcb` | `f533096eecba` | repo |
| `results/_d8_boundary_revision_register_2026_09_30.md` | `5a33f2c079c6` | `5622d37968ff` | repo |
| `results/_d8_dup_overlap_disposal_2026_09_30.md` | `c4ed04fd18fa` | `435c7e7bc422` | sub |
| `results/_d8_supplement_open_questions_2026_09_30.md` | `0da60b9a1de6` | `d8a9159c40d9` | repo |
| `results/_e2_glm2_distill_side_receipt_register_2026_10_09.md` | `3889af913d4c` | `4a8e99afdf6d` | sub |
| `results/_e4_lineage_conflict_correction_2026_10_11.md` | `57bde656f762` | `d08f1625732a` | sub |
| `results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | `584717acd90e` | `90692d4100f3` | sub |
| `results/_e6_j5_semantics_erratum_note_2026_10_10.md` | `935b16bc9d48` | `23265fc6acf4` | sub |
| `results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | `141f9a6f7450` | `2724e195ef58` | sub |
| `results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | `8ef45406f66d` | `467ace4389f7` | sub |
| `results/_ea_audit_batch_vk_2026_10_09.md` | `cb3c79a9b561` | `a7cba69019ce` | sub |
| `results/_eps_ls_semantics_judgment_2026_10_11.md` | `6cf929fa6f49` | `94f2a70ee4d5` | sub |
| `results/_executor_prereg_docstring_correction_2026_10_11.md` | `8211ed74f0de` | `cad9573c7130` | sub |
| `results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | `6567a3e316d1` | `c4e270d0b423` | sub |
| `results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | `1ab497ffcf5e` | `c22445f2f252` | sub |
| `results/_exp05_negative_probe_rescan_2026_10_10.md` | `1a434dd57eb3` | `a2a4b2977fc9` | sub |
| `results/_exp08_s4_prompt_face_register_2026_10_10.md` | `262ac921c4b0` | `556bdc0a5670` | sub |
| `results/_external_letters_two_generation_values_note_2026_10_01.md` | `491f4338aeeb` | `6849c292af55` | sub |
| `results/_f3_definition_deep_judgment_2026_10_11.md` | `0aa61e767615` | `173e51260711` | sub |
| `results/_f3_new_definition_draft_2026_10_11.md` | `43a3c50882d4` | `ab7a494cd3d7` | sub |
| `results/_f3f4_exit_drafts_2026_10_11.md` | `6b957b805b3f` | `f9f61cac47b0` | sub |
| `results/_f4_direction1_domain_effectivity_2026_10_11.md` | `a9a9122ec067` | `8bb3eeded041` | repo |
| `results/_f4_direction1_prereq_check_2026_10_11.md` | `4c4a1d6f60f5` | `516c6ea1c749` | sub |
| `results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | `3cbc03448af2` | `f9b7ad758bcb` | sub |
| `results/_five_items_effectivity_register_2026_10_11.md` | `5fd04575e161` | `2a498e82f9f4` | sub |
| `results/_five_pending_items_drafts_2026_10_11.md` | `ccd50440800d` | `48bc160b3265` | sub |
| `results/_five_stage_chain_design_reconstruction_2026_10_12.md` | `ee9375365231` | `15f177e238e1` | sub |
| `results/_forgotten_recovery_register_2026_09_29.md` | `94e70b3cff4b` | `fc3ed9b87092` | sub |
| `results/_forgotten_recovery_register_2026_10_08.md` | `d8ec52809c02` | `817ff913f1f7` | repo |
| `results/_four_items_execution_batch_2026_10_11.md` | `68089948c69a` | `9c27502abd00` | sub |
| `results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | `7a7627198619` | `2257524856ca` | sub |
| `results/_ftfb_order_judgment_2026_10_11.md` | `5a15b031e42e` | `0c943bbf536b` | sub |
| `results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md` | `43ef77ff0939` | `c096089bb083` | sub |
| `results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md` | `8529c3f37779` | `b9f718c720a9` | sub |
| `results/_g11_krj4_effectivity_register_2026_10_11.md` | `e2f46324fb78` | `5adc81e60162` | sub |
| `results/_g4_e3_definition_ruling_material_2026_10_09.md` | `afcd2edaa952` | `3638e15133ac` | sub |
| `results/_g4_reproduction_execution_register_2026_10_09.md` | `0fc49c17205b` | `3136a2fcae1c` | sub |
| `results/_g4_residual_probe_2026_10_08.md` | `ce3db50d3ec3` | `7c59058181e2` | sub |
| `results/_g5_ccp_execution_prereqs_2026_10_10.md` | `d4b16b573cd0` | `1293be908983` | repo |
| `results/_g5_ccp_p0_verification_2026_10_10.md` | `86018028a7fa` | `10eb0a5e9649` | sub |
| `results/_g5_ccp_seed_designation_revision_2026_10_10.md` | `92876b0b8dbd` | `b5b0f2cf3c37` | repo |
| `results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | `487e281745b8` | `685e17c9407d` | sub |
| `results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | `887969a1931c` | `e76d9b74029e` | sub |
| `results/_g5_rejudgment_construction_change_plan_2026_10_10.md` | `5142c8d4461a` | `cc626bcf5107` | repo |
| `results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | `f3448246455c` | `07747d9019e7` | sub |
| `results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | `0c646c01d983` | `d7bc5cb50edf` | sub |
| `results/_g9_read_b_effectivity_register_2026_10_11.md` | `68bb6bd96c10` | `8f52777de504` | sub |
| `results/_gate1_five_zero_recheck_glm_scope_2026_10_13.md` | `0819ac19f2e1` | `6b777b654df0` | repo |
| `results/_gate_one_declared_adoption_register_2026_10_11.md` | `62966dc92fca` | `b2fbd94ef807` | sub |
| `results/_gate_one_pi_endorsement_register_2026_10_12.md` | `7ca62a5dc884` | `f93621af5205` | sub |
| `results/_gate_one_reopened_and_stage2_rejection_register_2026_10_12.md` | `bcdfdbb0940a` | `ec57aef7b6dd` | repo |
| `results/_ge01_d1_theory_input_disposition_2026_10_14.md` | `df3149a13a5d` | `09ec2bec3f3b` | repo |
| `results/_ge01_d1_theory_input_sourcing_design_2026_10_14.md` | `8427f472ce39` | `2552cd0927de` | repo |
| `results/_ge01_spec_anchor_erratum_2026_10_14.md` | `f0c93a1f65c2` | `ab40274b30f2` | repo |
| `results/_ge01_unblock_progress_2026_10_14.md` | `ed36772f3efe` | `d2b45ba41ea1` | repo |
| `results/_github_suspect_rulings_effect_2026_10_17.md` | `a732da6d363a` | `336eb58d6f5c` | repo |
| `results/_itemH_fingerprint_provenance_2026_10_12.md` | `d5f27db26e9a` | `ff668b417dee` | sub |
| `results/_j2_identifier_coupling_judgment_2026_10_11.md` | `def2db2aea26` | `6bc5fde90a05` | sub |
| `results/_j2_kj4_disposition_register_2026_10_11.md` | `6ea8b41cad43` | `c903073be182` | sub |
| `results/_k_v3df_0_1_four_readings_2026_10_09.md` | `852ce8b50ec9` | `ce503683fb4a` | repo |
| `results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | `c4580a3b3b29` | `c4aa2b53e20f` | sub |
| `results/_kd1_preexp_contrast_2026_10_17.md` | `e15cac5d6ab4` | `69beba511318` | repo |
| `results/_kd_doc1_correction_adoption_register_2026_10_11.md` | `d15e442aa686` | `f8c1722d4d67` | sub |
| `results/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | `1507a17b2448` | `e2bb4fa29c1c` | repo |
| `results/_kd_s3b1_verdict_2026_10_17.md` | `9172d0748ed3` | `b33ef808646b` | repo |
| `results/_kimi_push_v3_manifest_batch14_e5952130.json` | `2a1f389a4d99` | `9f419c786be3` | sub |
| `results/_kimi_push_v3_manifest_batch5_34439e1e.json` | `ef0f17c3f2be` | `1ccc3fdb0565` | sub |
| `results/_kimi_safe_batch_push_v2_full_2026_09_17.json` | `ca670157f6c9` | `96538e4f10b7` | sub |
| `results/_kj1_abc_choice_judgment_2026_10_11.md` | `925a68307d20` | `69953e57b0fc` | sub |
| `results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | `13c4094f2053` | `6c42ba3f285e` | sub |
| `results/_kj1_judgment_premise_correction_2026_10_11.md` | `8b6724812e08` | `a9664bdcccdd` | sub |
| `results/_kj1_sc1_premise_correction_2026_10_11.md` | `b38b11217838` | `b3c0d245c088` | sub |
| `results/_kj4_e4_unification_judgment_2026_10_11.md` | `2a19e1aaf1b8` | `796dab06c04e` | sub |
| `results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | `dc3e67f7d4f5` | `7b7684a49c58` | sub |
| `results/_krj10_terminal_verdict_closure_2026_10_11.md` | `cdf830797db3` | `f2253efbeb13` | sub |
| `results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | `8e93f206b546` | `a894aed7b566` | sub |
| `results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | `a6cbce33a1ff` | `741e2698699f` | sub |
| `results/_krj5_final_disposition_verdict_2026_10_11.md` | `caba9ef44ff8` | `b3b155e38028` | sub |
| `results/_krj5_subject_scope_judgment_2026_10_11.md` | `21e8e42f284f` | `b873520cdd95` | sub |
| `results/_krj5d_third_tier_effectivity_2026_10_11.md` | `c9983f6177ac` | `acdadd7aefef` | sub |
| `results/_krj9_scope_clarification_draft_2026_10_10.md` | `a2bf7d0f85d8` | `f686df361df6` | sub |
| `results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | `cd304426ffe5` | `943c8aafa85f` | sub |
| `results/_krj_all_terminal_verdicts_2026_10_11.md` | `26aaf47192de` | `7c6f1187c880` | sub |
| `results/_krj_cond4_effectivity_declaration_2026_10_11.md` | `44660f750727` | `8ea98f0f8dc2` | sub |
| `results/_krj_five_verdicts_adjudication_2026_10_11.md` | `c0edaf60f28c` | `40b387aed7af` | sub |
| `results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | `54842032466d` | `a4612beda9a8` | sub |
| `results/_kt_a1_anchor_drift_root_cause_2026_10_14.md` | `4e262d90f4ca` | `bfc6f452f9b9` | repo |
| `results/_kt_a1_v0_lineage_corrigendum_2026_10_14.md` | `b85cd41cbd73` | `2afed52bbc44` | repo |
| `results/_letters_archive_register_2026_10_01.md` | `eb92d0ae25ed` | `abe53c4cb5d0` | sub |
| `results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | `f56ccb6de842` | `ea3f82948673` | sub |
| `results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | `8fb9a1bbd91e` | `dc518753f244` | sub |
| `results/_limb_reading_verdict_kv3s33_2026_10_01.md` | `5eaa7a03f151` | `d5590410823a` | sub |
| `results/_md_trigger_prereg_effectivity_2026_10_11.md` | `d68307e2e863` | `4b1c32665b9c` | repo |
| `results/_mini_round_5_decisions_register_2026_10_01.md` | `c9422fa9e7ed` | `52f5f0dd8a8c` | sub |
| `results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | `b577aa149ac3` | `933ea82b8572` | sub |
| `results/_noncore_upload_caliber_draft_2026_10_17.md` | `ca6633580c8c` | `a45f2230e2f8` | repo |
| `results/_noncore_upload_caliber_effect_register_2026_10_17.md` | `4b72a49b9221` | `446a7b9cf599` | repo |
| `results/_overnight_delivery_index_2026_10_10.md` | `6be2d532c63f` | `5876b6b8d617` | sub |
| `results/_p0_scan_2026_10_12.json` | `8f3a3743c8ac` | `14b1e7848bbf` | repo |
| `results/_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md` | `030801392946` | `32c588d344a5` | sub |
| `results/_p_l_v3_phase1_report_20260917_132341.md` | `52a3d1e8be7b` | `2c1b2a7640d4` | sub |
| `results/_p_l_v3_phase2_report_20260917_142748.md` | `9b5ea1432a1c` | `996b7cf5ae30` | sub |
| `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md` | `cb06e4e5292a` | `958c56a23f44` | sub |
| `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md` | `4790cc6fde8a` | `5e22f4e86785` | sub |
| `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md` | `aa33183b3cae` | `c7f54fec778d` | sub |
| `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md` | `ac783f124570` | `d89cc9ba9449` | sub |
| `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md` | `524651e929bf` | `df754dafab52` | sub |
| `results/_p_refresh_registration_preliminary_2026_10_10.md` | `d62328c4f3a9` | `d79c8f0c8fd4` | sub |
| `results/_p_refresh_s0_judgment_2026_10_10.md` | `06c7ada9fbb1` | `e875378b22ff` | sub |
| `results/_p_refresh_scope_judgment_2026_10_10.md` | `034f84aec0e5` | `217b7f46438f` | sub |
| `results/_pc_d1_d3_2026_09_15.py` | `f4501d50cb6c` | `23a60ae75388` | sub |
| `results/_pending_pi_items_drafts_2026_10_11.md` | `8227c455082f` | `a9ee659d65c8` | sub |
| `results/_pending_rulings_drafts_2026_10_11.md` | `f48cd3b0d562` | `f59136835d7d` | sub |
| `results/_pending_supply_search_receipt_2026_10_08.md` | `bde67d5a1516` | `52d072ec0343` | sub |
| `results/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md` | `8dc82b7c3c0f` | `22c209770ddd` | repo |
| `results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | `ee185be5f7da` | `68078f446d66` | sub |
| `results/_pi_effectivity_declaration_register_2026_10_11.md` | `4ebeea7caa2f` | `f1e451d60df1` | sub |
| `results/_plan_v3_pending_verify_2026_09_30.md` | `4544e99386d7` | `5ac22eef150f` | repo |
| `results/_pre_exec_report_kimi_2026_09_30.md` | `911ddccd5c44` | `e9232f54656e` | sub |
| `results/_pre_execution_report_kimi_2026_10_01.md` | `12eeed4c5426` | `91ac74bd958a` | sub |
| `results/_pre_execution_report_kimi_2026_10_12.md` | `70b0915abdbc` | `64c7d5df3304` | repo |
| `results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | `e90fe5903e28` | `7ffdabbe6eec` | sub |
| `results/_q2_scope_vs_revision_judgment_2026_10_11.md` | `8d2534d1a44e` | `a76a99b95a0c` | sub |
| `results/_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | `5f1e0670f4c4` | `4d37c7e75106` | repo |
| `results/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | `f747cbdd3ce0` | `7d8441077e67` | sub |
| `results/_questionnaire_cards_intake_register_2026_10_09.md` | `441b199e098c` | `e08d079f26ea` | repo |
| `results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | `a611d3e62978` | `5140616c2035` | sub |
| `results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | `877fe26ca772` | `46ee8668402e` | sub |
| `results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | `e552a449fc9b` | `626c30caf82d` | sub |
| `results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | `9e29f7f3ab4e` | `ae2c5587a86b` | sub |
| `results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | `d268d9eea466` | `3239456c7c9e` | sub |
| `results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | `a861f72e0d3c` | `884f61b07779` | sub |
| `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `19fea1e0e3e8` | `4a85ae03c395` | repo |
| `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `0de951feb9f3` | `89744f279f62` | repo |
| `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | `294752c30345` | `131d0e0d0636` | repo |
| `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | `8542b765938a` | `686a64465d72` | repo |
| `results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | `42e99a1c5aa4` | `5376f4aae453` | repo |
| `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | `69a21d50620b` | `1ad43c70cf01` | repo |
| `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `c69261f091af` | `ba5c6e7a4a9c` | sub |
| `results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `59026ae97582` | `abc9a7d2293a` | sub |
| `results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | `723b79dffa1c` | `62e68c52414c` | sub |
| `results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | `c533fd52eb13` | `249c30c031d3` | sub |
| `results/_r2_build_manifest_2026_10_12.json` | `5b89369890ee` | `e47dec3e6d85` | repo |
| `results/_r2_execution_receipt_kimi_2026_10_12.md` | `4cc87c0abd0b` | `68064371a7e3` | repo |
| `results/_r5_spec_pack_retrieval_register_2026_10_13.md` | `e9d4379d24b3` | `8b664209645c` | repo |
| `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | `2d360c03f4d1` | `c3d6b36b1a4f` | sub |
| `results/_r_pair_addendum_2026_10_09.json` | `f462ad619013` | `e3ceee1988ad` | repo |
| `results/_receipt_disposition_register_2026_10_08.md` | `2f749d7d1457` | `f286e357b13f` | sub |
| `results/_refcheck_hash_change_reference_recheck_2026_09_30.md` | `c8de825f3391` | `3e859aae10b5` | sub |
| `results/_register3_bytes_erratum_2026_10_11.md` | `ee2c0b0ccc5a` | `7bc1a4d3c812` | sub |
| `results/_repo_full_inventory_catalogue_2026_10_12.md` | `35309e81bd0a` | `2a985ffc8e69` | repo |
| `results/_repo_post_cleanup_snapshot_2026_10_12.md` | `9094c78c5433` | `698de5d8249e` | repo |
| `results/_root_session_history_memo_2026_10_14.md` | `066c6f031ba0` | `2b8b82021ad3` | repo |
| `results/_root_session_history_memo_main_2026_10_14.md` | `9502b9beaf9f` | `f05098e1179f` | repo |
| `results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | `7b021054c471` | `df3281e6871a` | sub |
| `results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | `a5bf28d3fcca` | `67da78b3d19e` | sub |
| `results/_round54_g5_dispositions_register_2026_10_10.md` | `fdd3ccd3a8a1` | `a483ac9fba64` | sub |
| `results/_round55_dispositions_register_2026_10_10.md` | `5c7cb610a8c7` | `3193804b4aaf` | sub |
| `results/_round56_ad8fix_effectivity_register_2026_10_10.md` | `df46bd4e2eec` | `67df53c3e97f` | sub |
| `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | `648f83115184` | `388ef92900f2` | sub |
| `results/_round56_direct_adoptions_register_2026_10_10.md` | `3a8b5c22f5e3` | `866261714244` | sub |
| `results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | `10ca088d9ce1` | `3a50cef82902` | sub |
| `results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | `23d65bf5e9fd` | `bddcd0848fb2` | sub |
| `results/_round56_idx_sc1_resolution_2026_10_10.md` | `bb722799e89e` | `0f61665cb8ea` | sub |
| `results/_round56_n10_erratum_register_2026_10_10.md` | `bd948baf6f71` | `78da765f2b4b` | sub |
| `results/_round56_pending_questions_compilation_2026_10_10.md` | `3fbba85846d8` | `219b55f758e9` | sub |
| `results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | `bb5c9001dd31` | `3b894f46c3d1` | sub |
| `results/_round56_registration_supplement_2026_10_10.md` | `f22659a123c5` | `280a921dea9a` | sub |
| `results/_round56_review_effectivity_register_2026_10_10.md` | `641eb4c6ac2a` | `251e2eb167c2` | sub |
| `results/_round56_review_effectivity_register_3_2026_10_10.md` | `0b07905291dc` | `15295e3eeb26` | sub |
| `results/_round56_review_effectivity_register_4_2026_10_11.md` | `e5889a1a51bb` | `f3d03ea79519` | sub |
| `results/_round56_review_effectivity_register_5_2026_10_11.md` | `5118e6894251` | `11f8befcefa3` | sub |
| `results/_round56_review_effectivity_register_6_2026_10_11.md` | `e126cd454064` | `acba222fdf57` | sub |
| `results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | `9069eede88f9` | `729043e158c8` | sub |
| `results/_round56_shortname_backfill_note_2026_10_10.md` | `ed112e78cbb8` | `eb5bee36daf4` | sub |
| `results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | `734fc54ea746` | `bc45365245aa` | sub |
| `results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | `e1b8a8b66c9d` | `1b8daf6983d7` | sub |
| `results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | `1f182b639d5e` | `da1a6ea941f2` | sub |
| `results/_round56_typeb_backfill_register_2026_10_10.md` | `a36975e48f45` | `238be5a072c6` | sub |
| `results/_round56_typeb_form_draft_2026_10_10.md` | `df7a80c3e61f` | `ab979408cda3` | sub |
| `results/_round56_typeb_implementation_register_2026_10_10.md` | `8a2ccfd50d52` | `a2deb8df3616` | sub |
| `results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | `5200924444b7` | `40932e5803d0` | sub |
| `results/_round56a_dispositions_register_2026_10_10.md` | `43f36a646019` | `490aa8148a87` | sub |
| `results/_round56c_card_id_erratum_2026_10_10.md` | `b9aba7f5edb9` | `b329af678360` | sub |
| `results/_round56c_d23_ad5_judgment_2026_10_10.md` | `d50569ddcca4` | `f526cceb4c75` | sub |
| `results/_round56r8_dispositions_register_2026_10_10.md` | `2c56d7b3835a` | `834d4dc31af5` | sub |
| `results/_round56r9r10_dispositions_register_2026_10_10.md` | `1449fe1ab5df` | `f6e9704ac575` | sub |
| `results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | `e2fee828f1b8` | `37a856ff5782` | sub |
| `results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | `ab4d6db386cd` | `ea7839df970c` | sub |
| `results/_s3prime_alert_disposition_judgment_2026_10_11.md` | `66975edaa99f` | `325b927ceea6` | repo |
| `results/_s3prime_degeneracy_selfcert_2026_10_11.md` | `139986b64f9c` | `47a10d98edae` | repo |
| `results/_s3prime_recompute_after_supplement_2026_10_11.md` | `97619a3c7c8e` | `4992c2b84c99` | sub |
| `results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | `b899cb2f91fe` | `5872e85049bf` | sub |
| `results/_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | `1b693dec8fea` | `baf86b575ab1` | sub |
| `results/_s4_heldout_sampling_seed42_register_2026_10_09.md` | `cefb47728dbb` | `302b47c9138b` | sub |
| `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `d03126028128` | `dcd1fc53e83c` | sub |
| `results/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | `90370c77b4a5` | `dc49602cad89` | repo |
| `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `1b1f027db264` | `ee0f43b1fe83` | sub |
| `results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `a300572d5420` | `040718619f7b` | repo |
| `results/_s4_heldout_seedprime_verification_2026_10_10.md` | `74e09e84ff0c` | `fdf02a9a0447` | sub |
| `results/_s4_open_questions_addendum_2026_10_09.json` | `2d7b322065d2` | `8a2cb27e6fe0` | repo |
| `results/_s4_seedprime_inheldout_recompute_2026_10_10.md` | `14a461780763` | `73382f10061f` | repo |
| `results/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | `d90c313b2c99` | `319c77148b2c` | repo |
| `results/_s4_source_wave_mapping_registration_2026_10_10.md` | `51ee08ae73cf` | `1dea5a7f30f7` | repo |
| `results/_s4_substrate_topup_addendum_2026_10_09.json` | `1ba293951b31` | `e32529b0371b` | repo |
| `results/_s4prime_five_lines_readings_2026_10_11.md` | `747f06b6009c` | `d1f01b136d9e` | sub |
| `results/_s4prime_readings_runner_2026_10_11.py` | `1ea332165702` | `a951729c2167` | sub |
| `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | `93d13cd8a5fa` | `8b48768dd2b6` | sub |
| `results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | `fb5c677e72a4` | `e1373b419641` | sub |
| `results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | `2cd63dba3bb8` | `d4ab99975a77` | sub |
| `results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | `33b19246feb9` | `1ff6f03a1c96` | sub |
| `results/_s6doubleprime_verdict_supplement_2026_10_11.md` | `7853e29f5cfc` | `746426b0b285` | sub |
| `results/_s6prime_terminal_verdicts_2026_10_11.md` | `7a8b356ffd8b` | `4d449dc4acd8` | sub |
| `results/_s7doubleprime_verification_2026_10_11.md` | `e1121ea6b28c` | `9661494aea4f` | sub |
| `results/_s7doubleprime_verification_erratum_2026_10_11.md` | `2bbf169f9be6` | `00a219feb86a` | sub |
| `results/_s7prime_findings_erratum_2026_10_11.md` | `99f9c34aaa90` | `b4493b9fbe38` | sub |
| `results/_s7prime_prereq_and_verification_2026_10_11.md` | `6c04e8c0e1d2` | `5b975ed206a5` | sub |
| `results/_seed_double_criterion_draft_2026_10_11.md` | `f3d8f45561f5` | `0a3362018856` | sub |
| `results/_seed_double_identifier_final_judgment_2026_10_11.md` | `709d6bf1bbd2` | `32d25d82a584` | sub |
| `results/_seed_double_identifier_finalization_2026_10_11.md` | `6f5d16b74ea8` | `3bb2b5bc9289` | repo |
| `results/_seed_double_rule_judgment_2026_10_11.md` | `500d1c84f2e0` | `42cc96d0683f` | sub |
| `results/_seven_gap_closures_adoption_register_2026_10_11.md` | `d1d9dfb4557a` | `77bc8321aa38` | sub |
| `results/_stage1_independent_gate_review_2026_10_12.md` | `cc864345e5f3` | `8489ee888ae0` | repo |
| `results/_stage1_tail_caliber_unification_register_2026_10_11.md` | `d10449b8019f` | `97315904a13e` | sub |
| `results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | `b5cb510206f3` | `9e006c0584c8` | sub |
| `results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md` | `408fb37dfc15` | `c6814cf0a0b7` | repo |
| `results/_stage3_completion_and_stage4_open_register_2026_10_12.md` | `6b412b2a8c5a` | `8122149090fa` | repo |
| `results/_stage3_extraction_verification_2026_10_11.md` | `e777c746f6d8` | `635b562d3a5b` | sub |
| `results/_stage3_open_and_mandate_register_2026_10_12.md` | `8f6f952dea43` | `3caf22fa7486` | sub |
| `results/_stage3_r2_cleanup_register_2026_10_18.md` | `c703e9611da8` | `1da246fd164c` | repo |
| `results/_stage3_readings_verification_2026_10_11.md` | `faf2d978ef74` | `8943272627e9` | sub |
| `results/_stage3_trigger_readings_2026_10_11.md` | `8d8488bc8716` | `3f3a8d002a47` | sub |
| `results/_stage3_trigger_recheck_2026_10_11.md` | `c866e0dfd4ba` | `0b57f4096b3f` | repo |
| `results/_stage_sequence_violation_register_2026_10_12.md` | `1e9cbb33d96d` | `531018438e42` | repo |
| `results/_supplement_to_500_design_review_2026_10_16.md` | `4133b3599fd3` | `6d687bd6d657` | repo |
| `results/_suspect17_release_move_register_2026_10_09.md` | `0f1d1f80230f` | `7d8f557cdf1e` | sub |
| `results/_t1_exp2_activation_supplement_2026_10_09.md` | `20f29e21c80c` | `61049ff75bb6` | repo |
| `results/_t1_exp2_executor_2026_10_09.py` | `8697740e0aca` | `fe80596a9a6f` | repo |
| `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | `ddb383dcc51b` | `2d40510c92b5` | sub |
| `results/_temp_cleanup_register_2026_10_13.md` | `22fde9ae557b` | `9a5f14d42118` | repo |
| `results/_theory_boundary_clone_sync_register_2026_10_09.md` | `085fbf7cd9aa` | `65d7a28a7de2` | sub |
| `results/_theory_input_request_supplement_2026_09_29.md` | `1517f0249d63` | `2cb1123b2301` | sub |
| `results/_three_pending_items_drafts_2026_10_11.md` | `27ca82578a29` | `41c763713c1a` | sub |
| `results/_three_pending_items_effectivity_2026_10_11.md` | `19b47d140045` | `b199ecc80ca8` | sub |
| `results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | `3a31f5d7ad13` | `fde59293f674` | sub |
| `results/_trae_issues_batch3_six_items_draft_2026_10_12.md` | `79bddad30c1d` | `9d09d5f297a9` | repo |
| `results/_trae_issues_disposition_schedule_2026_10_12.md` | `ab901b9a72ef` | `f1b6e9a9356a` | repo |
| `results/_trigger_denominator_caliber_judgment_2026_10_11.md` | `712b54772f56` | `223e30582ee0` | sub |
| `results/_trj_w1_downstream_erratum_2026_10_10.md` | `688b98ff44bd` | `9ca61f7833db` | sub |
| `results/_trj_w1_verification_2026_10_10.md` | `712b03ed9568` | `414410f8c677` | sub |
| `results/_two_items_alternative_deliberation_judgment_2026_10_13.md` | `f6b73a4b8228` | `3b1ac930e32f` | repo |
| `results/_typeb_m_caliber_2026_10_10.md` | `d7b400366a1f` | `628fb6fe4fb0` | sub |
| `results/_typeb_m_definition_judgment_2026_10_10.md` | `0a2b396958c4` | `29be716acfa5` | sub |
| `results/_typeb_m_registration_2026_10_10.md` | `f06b8ebb594c` | `f661a9c43455` | sub |
| `results/_u04_1_exemption_precondition_verification_2026_10_09.md` | `b779b83fb02c` | `74b52b923a57` | sub |
| `results/_u3_carrier_qid_verification_2026_10_11.md` | `3f6a88210fb2` | `1762d338a1c9` | sub |
| `results/_u5b_p_counting_resolution_2026_10_10.md` | `a1847e9f51f7` | `431f998079cb` | sub |
| `results/_u6_negative_delta_compatibility_2026_10_11.md` | `3989ef97bfb1` | `015bc8dd1609` | sub |
| `results/_u_cf_category_caliber_2026_10_10.md` | `4b82a9671d6e` | `b99e008fb01c` | sub |
| `results/_u_cf_reclassification_2026_10_10.md` | `51527925597f` | `be3de9009298` | sub |
| `results/_u_closure_execution_register_2026_10_09.md` | `4c5d5368aa76` | `f890ddd6e453` | sub |
| `results/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md` | `20cedf10c2f5` | `e13549fdfbda` | repo |
| `results/_unclosed_47_pi_give_draft_2026_10_13.md` | `a401d4a2b4d5` | `9777271dc3f7` | repo |
| `results/_unclosed_items_inventory_2026_10_08.md` | `5d822b49bbc8` | `ee32fa24897c` | sub |
| `results/_upload_execution_receipt_kimi_2026_10_12.md` | `fa634919ff9e` | `98e787209928` | repo |
| `results/_upload_guard_mirror_pair_2026_10_08.md` | `ae7633cfa6b7` | `351e82299111` | sub |
| `results/_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md` | `c8331b3a63c0` | `31328d10c91a` | repo |
| `results/_v3_recheck_05_executor_2026_09_28.py` | `01b8e0ccd990` | `3dbba73f89d2` | sub |
| `results/_v3_recheck_05_result_2026_09_28.json` | `948ae3ece224` | `eda36fcfe0df` | repo |
| `results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | `c7ff24b95ca4` | `e495b054ef0b` | repo |
| `results/_v3_recheck_21_rescript_2026_09_27.md` | `8927d7c3cee1` | `54906747d7f4` | repo |
| `results/_v3_recheck_21_result_2026_09_27.json` | `ad9135f3a220` | `c785963431f0` | repo |
| `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | `f8394583129f` | `be95cb2ab1b2` | repo |
| `results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | `ac73825cb34a` | `46ab58f5894e` | repo |
| `results/_v3_v4_achievements_inventory_2026_09_24.md` | `b16d7fe824a8` | `83cff446d24f` | repo |
| `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `da9fb0cad410` | `c028ae5472fa` | repo |
| `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `b24d710ed030` | `5beb4be2913a` | sub |
| `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | `bd07469049db` | `e5bdbe69fae5` | sub |
| `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | `0be54db0d1ea` | `b4f5d7fc8a2b` | repo |
| `results/_v3x_d0_5_aggregation_2026_09_17.md` | `c06b707cb516` | `cf8c93cb97fd` | repo |
| `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | `455a9f62453b` | `c8afa0f911ef` | repo |
| `results/_v3x_d0_5_proposal_coze_2026_09_17.md` | `47787a82029d` | `01995d47e492` | repo |
| `results/_v3x_p_l_v3_external_spec_2026_09_17.md` | `36aaab76914d` | `a3e250d226fc` | repo |
| `results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `847cee4f1ba8` | `d6ccf22b86a9` | repo |
| `results/_v4_closeout_account_reconciliation_2026_10_12.md` | `e2dc09b06007` | `1fd9e231650b` | repo |
| `results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `87a2ff256873` | `e90e2b9beb66` | repo |
| `results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | `d3e6528187c2` | `36c7b38ca540` | repo |
| `results/_v4_design_integration_2026_09_21_v1.1.md` | `28b94277ca51` | `abe04e8f446c` | sub |
| `results/_v4_gA1_experiment_outline_2026_09_22.md` | `0f94a003dbb9` | `60f4e245578e` | sub |
| `results/_v4_gA1_terminology_draft_2026_09_22.md` | `ca4bad1a0f19` | `304915c9345a` | sub |
| `results/_v4_gA3_seeds_judgment_draft_2026_09_22.md` | `aa3da939a79c` | `d60da74ac642` | sub |
| `results/_v4_group_b_17letters_judgment_draft_2026_09_22.md` | `38246f705a64` | `5b09e5e9d8bb` | sub |
| `results/_v4_group_b_explore_subs_integration_2026_09_22.md` | `1d66f37a9e8e` | `33a2d474389a` | sub |
| `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | `c096f23a2f79` | `946ef3ee579a` | sub |
| `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | `22d2c1d03065` | `5309288b8ed3` | sub |
| `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `461124b1c8bb` | `200646b08b6d` | sub |
| `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `6fc3463e11c1` | `d8143cb3399b` | repo |
| `results/_v4_maindir_count_monitor_2026_09_27.md` | `42dc9efce725` | `1ca379462f93` | repo |
| `results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | `de3da25bc7a8` | `b932c59886b3` | repo |
| `results/_v4_trae_remaining_audit_2026_09_28.md` | `9f37ef2ba0db` | `81eac6c49950` | sub |
| `results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | `4a2cb20f948f` | `9298e7dc632e` | sub |
| `results/_v5_clearance_mr11_doc_calibration_2026_09_29.md` | `6cab8f3ed1e8` | `daccef7de159` | sub |
| `results/_v5_clearance_o15_ready_pack_2026_09_29.md` | `1b145eded648` | `3b91e58e1b0d` | sub |
| `results/_v5_confirm_b11_decisions_register_2026_09_29.md` | `17f590a839a5` | `9d9b8612943a` | repo |
| `results/_v5_confirm_b3_decisions_register_2026_09_29.md` | `3f455a73da77` | `6dd5434c9b81` | sub |
| `results/_v5_confirm_b8_decisions_register_2026_09_29.md` | `0778f4b25bf6` | `b42c79c43ab7` | sub |
| `results/_v5_handover_guide_project_initiation_2026_10_12.md` | `fc1fac3d9898` | `cfd3255067a6` | repo |
| `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `6c291f7574b6` | `28280791a8b7` | sub |
| `results/_v5_item21_verdict_2026_09_28.md` | `6ee482285e78` | `afedb01416e9` | sub |
| `results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | `911e88d52b64` | `0d678b5b01af` | sub |
| `results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | `b38a5f82e104` | `64fe42b900b4` | sub |
| `results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | `82c6c5530d55` | `f656711d0984` | sub |
| `results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | `ce300c1883d8` | `2efb4b5e131c` | sub |
| `results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | `5644406f7355` | `be3fe129bd5e` | sub |
| `results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `90617176e1ae` | `b93e9615fa2b` | sub |
| `results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | `8e40c48ca35d` | `bdfecc0ddff9` | sub |
| `results/_v5_t1_decisions_register_2026_09_29.md` | `a2dd2d65b1ec` | `8bb51232c796` | sub |
| `results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | `969470464033` | `867e05f76d00` | sub |
| `results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | `2f115c9a6662` | `a939678d9cd0` | sub |
| `results/_vk_current_counting_face_2026_10_10.md` | `505d7e1dd421` | `1228f05a235e` | sub |
| `results/_vk_face_category_erratum_2026_10_11.md` | `7801775634bd` | `06662bff1840` | sub |
| `results/_zero_reading_judgment_2026_10_10.md` | `a07774dbcb71` | `f49d7e4235f7` | sub |
| `results/_zone_balance_inventory_2026_10_13.md` | `48ea4e6774c3` | `aa567faafe5c` | repo |
| `results/deposon_3risk_v0_fixes_2026_09_11.json` | `65cc3eaa19f6` | `da02c9e3bf5e` | sub |
| `results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `8df74e7345ab` | `d970b499f257` | repo |
| `results/deposon_pa_d1_d3_2026_09_15.json` | `17fb4ef17572` | `b601019db22b` | repo |
| `results/deposon_pc_d1_d3_2026_09_15.json` | `98b60214583e` | `9e1e17b0cfd0` | repo |
| `results/deposon_pe_d1_d3_2026_09_15.json` | `6f4b25cca87b` | `de9ffebb6fde` | repo |
| `results/deposon_pf_d1_full_9m5c_2026_09_15.json` | `096c001f92ca` | `2572356be097` | repo |
| `results/deposon_pf_implementation_2026_09_11.json` | `3bf750dc3f8b` | `ffda3c721f2b` | repo |
| `results/deposon_pg_v01_9m60c_2026_09_15.json` | `ca0ffb87f97b` | `7d2a8f8e04f7` | repo |
| `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `5d4875397a9f` | `50adfe1c46d2` | repo |
| `results/deposon_v3_v7_summary_2026_09_11.json` | `289e897f3a07` | `8cd751b77dee` | repo |
| `results/skill_d_p_f_observer_result_2026_09_11.json` | `b83ad0fd3517` | `1725984318e1` | sub |
| `tmp_movedout_2026_09_28/_cleanup_classify_2026_09_28.py` | `fc27f4f3a1bf` | `9e692ba895ed` | sub |
| `tmp_movedout_2026_09_28/_cleanup_classify_out_2026_09_28.txt` | `e9e63476d717` | `dd447d4ca5c2` | sub |
| `tmp_movedout_2026_09_28/_cleanup_probe_2026_09_28.py` | `ca9dc8aefe34` | `dd8a35858a6b` | sub |
| `tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt` | `c4c89193db52` | `6ea1b7263a9c` | sub |
| `tmp_movedout_2026_09_28/_cleanup_resolve_2026_09_28.py` | `4e3fef8ea6ec` | `dc578941a2df` | sub |
| `tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py` | `0020de27f803` | `4fe0eef8bd7d` | sub |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/_asset_recount_2026_09_30.md` | `5274aee17142` | `8af3fd8a08db` | sub |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/_letter_review_bob_w3_commission_2026_09_30.md` | `d2163dca73e5` | `f038e15fe156` | sub |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_r3_anchor_retrieval_2026_09_29.md` | `c634e087d745` | `cf395fdb3282` | sub |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b17_three_caliber_fixation_2026_09_29.md` | `203d3ee799ba` | `aa13f2945e85` | sub |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md` | `d908c85c4da4` | `a2989b1b5b26` | sub |
| `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `2a9a263e2ffc` | `f811d309b5db` | sub |
| `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `f9beac73eef9` | `b03947774829` | sub |
| `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` | `81afead5bd49` | `55f9a857a22e` | repo |
| `verifier/v36/check.sh` | `23b9f6d2bc40` | `97995f00a2cc` | repo |
| `verifier/v41/check.sh` | `4f3916a0596d` | `f95e8b034820` | repo |
| `volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` | `4ffa7c767bef` | `9fd934425841` | sub |

### §3-4 已对齐面（非三面之任一）

映射后路径两侧皆在位、Git-blob-SHA1-12 **相等** 者 **2,348 件**——登记于形态面总账，**不入三面计数**。

### §3-5 同一性面（SAME_IDENTITY）

同一 SHA-256-12 于双区/异名多份存在者 **247 组**。依冻结件 **D-2**：⛔ **0 重复计数**（面①②以**路径**为计数单位）、⛔ **0 因同一性而隐去其一**。抽样：

| SHA-256-12 | 份数 | 分布 |  |
|---|---|---|---|
| `01e63e488ce2` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` ｜ `sub:results/_archive_2026_09_20/_fix_batch3_2026_09_18.py` |  |
| `023f936f80fb` | 2 | `repo:_remote_pullback_2026_10_17/results/llm_prior_cache_v18_direction.json` ｜ `sub:results/llm_prior_cache_v18_direction.json` |  |
| `0291002f749e` | 2 | `repo:.tmp/erratum_glm_wholepack_body.md` ｜ `repo:results/_glm_wholepack_irreproducible_erratum_2026_10_14.md` |  |
| `03fe4d044c78` | 2 | `repo:.tmp/_clv_staging_2026_10_18.md` ｜ `repo:results/_ruled_unclosed_closure_verdict_2026_10_18.md` |  |
| `048ebc99177c` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_5model.py` ｜ `sub:results/_archive_2026_09_20/_tmp_inspect_5model.py` |  |
| `0646da5ccbe5` | 2 | `repo:.tmp/ge01_s3b_v_exec_r1_supp_2026_10_16.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_supp_2026_10_16.py` |  |
| `070b6f865eba` | 2 | `repo:.tmp/d05_hash_index.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/d05_hash_index.py` |  |
| `0769f60a0504` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_final_sha_2026_09_18.py` ｜ `sub:results/_archive_2026_09_20/_final_sha_2026_09_18.py` |  |
| `079108c62a82` | 2 | `repo:results/_stage3_trigger_readings_items_2026_10_11.json` ｜ `repo:results/_d9_e2e_backup_2026_10_13/_stage3_trigger_readings_items_2026_10_11.json` |  |
| `0a1e91d6f772` | 3 | `repo:_remote_pullback_2026_10_17/results/_d05_sanity_3backbone_20260918_100110.json` ｜ `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` ｜ `sub:results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` |  |
| `0a970b156867` | 2 | `repo:.tmp/f2_branch_fix_transform_2026_09_29.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/f2_branch_fix_transform_2026_09_29.py` |  |
| `0abaee4aeefb` | 2 | `repo:.tmp/ndv_stage.md` ｜ `repo:results/_n_distinct_grain_verdict_2026_10_17.md` |  |
| `0b7e50a8a036` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` ｜ `sub:results/_archive_2026_09_20/_d05_verify_sha_2026_09_18.py` |  |
| `0c9addf4a70f` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_inspect_22cap.py` ｜ `sub:results/_archive_2026_09_20/_tmp_inspect_22cap.py` |  |
| `0d36d7cd0589` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` ｜ `sub:results/_archive_2026_09_20/review_tech_B1_dsv4pro.md` |  |
| `0df5d957a911` | 2 | `repo:.tmp/ge01_s3b_v_exec_2026_10_16.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_2026_10_16.py` |  |
| `0e7cb9348a16` | 2 | `repo:.tmp/vk_v3df_0_1_verify_2026_10_09.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/vk_v3df_0_1_verify_2026_10_09.py` |  |
| `0e8c9664b06d` | 2 | `repo:.tmp/m08_r1_llm_calls_2026_10_16.jsonl` ｜ `repo:.tmp/whitelist_backup_2026_10_17/m08_r1_llm_calls_2026_10_16.jsonl` |  |
| `0fb8fb628de0` | 2 | `repo:.tmp/d86_verify.out.txt` ｜ `repo:.tmp/d86_verify_print.txt` |  |
| `0fd3788e2d3b` | 2 | `repo:.tmp/_frc_content.md` ｜ `repo:results/_face_r_coexist_verdict_2026_10_17.md` |  |
| `121a3b861261` | 2 | `repo:.tmp/md_a_field_composition_draft_2026_10_18.staged.md` ｜ `repo:results/_md_a_field_composition_draft_2026_10_18.md` |  |
| `12da29eb102c` | 2 | `repo:.tmp/_dfam_corr_src_2026_10_12.md` ｜ `repo:results/_trae_issues_dfamily_corrections_register_2026_10_12.md` |  |
| `15904ecae629` | 2 | `repo:results/_archive_2026_09_24/_volc_22cap_emb.py` ｜ `sub:results/_volc_22cap_emb.py` |  |
| `15c0b0ade7ab` | 2 | `repo:.tmp/d1fill_anchor_snapshot.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/d1fill_anchor_snapshot.py` |  |
| `15d2a2cef38c` | 2 | `repo:.tmp/docwriter_v46_probe.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/docwriter_v46_probe.py` |  |
| `18984b04c45e` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` ｜ `sub:results/_archive_2026_09_20/_deposon_v2scripts_reverify_worker_2026_09_18.py` |  |
| `18b0f12b2c66` | 2 | `repo:.tmp/vk_verify_interval_ceiling_2026_10_16.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/vk_verify_interval_ceiling_2026_10_16.py` |  |
| `190668eae9da` | 2 | `repo:.tmp/m08_r1_llm_probe2_2026_10_16.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/m08_r1_llm_probe2_2026_10_16.py` |  |
| `19cfb64700a1` | 2 | `repo:.tmp/docwriter_verify_v44.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/docwriter_verify_v44.py` |  |
| `19d93d77b46e` | 2 | `repo:.tmp/m08_r1_llm_arm_2026_10_16.json` ｜ `repo:.tmp/whitelist_backup_2026_10_17/m08_r1_llm_arm_2026_10_16.json` |  |
| `1a40d8046fdc` | 2 | `repo:.tmp/m08_r1_freeze_2026_10_16.json` ｜ `repo:.tmp/whitelist_backup_2026_10_17/m08_r1_freeze_2026_10_16.json` |  |
| `1c59e7b803fe` | 2 | `repo:_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` ｜ `sub:results/_archive_2026_09_20/_fix_batch6_2026_09_18.py` |  |
| `1dadfaeb2c43` | 2 | `repo:_remote_pullback_2026_10_17/results/v20_statcheck_fm_vs_rand.json` ｜ `sub:results/v20_statcheck_fm_vs_rand.json` |  |
| `1dbe20a3ba1c` | 2 | `repo:.tmp/_r2_body.md` ｜ `repo:results/_night_shift_handover_2026_10_14_r2.md` |  |
| `1e579de6033c` | 2 | `repo:.tmp/t3_postchange_equiv.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/t3_postchange_equiv.py` |  |
| `1ec7c258c637` | 2 | `repo:.tmp/ge01_s3b_v_exec_r1_readings_2026_10_16.json` ｜ `repo:.tmp/whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_readings_2026_10_16.json` |  |
| `1ee1ee14ac3e` | 2 | `repo:.tmp/docwriter_v47_write2.py` ｜ `repo:.tmp/whitelist_backup_2026_10_17/docwriter_v47_write2.py` |  |
| `1ef99b1da14d` | 2 | `repo:.tmp/docwriter_c2_effect_census.json` ｜ `repo:.tmp/whitelist_backup_2026_10_17/docwriter_c2_effect_census.json` |  |
| `1fc5f3ab3f93` | 3 | `sub:.trae/audit/compile_evidence/compile_runner.ps1` ｜ `sub:.trae/audit/compile_evidence/v2pre_h1h3_20260909/compile_runner.ps1` ｜ `sub:.trae/audit/compile_evidence/v2_overfull_fix_20260909/compile_runner.ps1` |  |
| `20ad5b45ba2c` | 2 | `repo:.tmp/pk33q_body.md` ｜ `repo:results/_reading_e_33_historical_nominal_value_corrigendum_2026_10_15.md` |  |

---

## §4 形态面总账（远端单区 ⇔ 本地双区）

| 维度 | 远端（单区） | 本地（双区） |
|---|---|---|
| 承载面 | **1 个**：``_september_workspace/`` 前缀 ＋ **根层遗留面**（未受前轮 298 路径删除覆盖） | **2 个**：`deposon-repo` ＋ `deposon-sub`（**非对称**：仅 repo 4,113 · 仅 sub 1,265） |
| 件数 | blob **3,447**（前缀 3,034 ＋ 遗留 413） | 并集 **5,389**（repo 4,124 ＋ sub 1,276） |
| 字节 | 122,777,384 B（前缀 118,689,899 ＋ 遗留 4,087,485） | — |
| `.tmp/` 面 | **0 件**（已整面清空） | **2046 件**（102,174,150 B） |
| `letters/` 面 | 前缀面 **0 件**；**遗留面 7 件** | **122 件** |
| `pi_rulings/` 面 | **93 件** | 仅本地有（107 件） |
| 双区内容漂移 | 不适用 | **1 件** |

---

## §5 删除面之本地存续对账（缺件/幽灵面 · 本轮 293 条）

📌 依回执 R-S4 逐件表解析得 **293 条**（序号 1..293，**0 缺号**），逐条与远端全树 ＋ 本地双区对账。

| 判据 | 结果 |
|---|---|
| 远端**仍在位**（期望 0） | **0** ✅ |
| 本地双区**内容与删前 blob 相符** | **191** |
| 本地双区**在位但内容不一致** | **21** ⚠（逐件见 §5-1） |
| 本地双区**均无**（**仓内无副本**） | **81** ⚠（逐件见 §5-2） |

### §5-1 仓内副本与远端删前 blob **内容不一致**（21 件）

| 路径 | 回执载删前 SHA-1-12 | 本地 SHA-1-12 |
|---|---|---|
| `.tmp/_audit3b.txt` | `e992573fbe2f` | `2418872d1612` |
| `.tmp/_audit_part3_out.txt` | `0c62f640ffcf` | `f510e8e32a74` |
| `.tmp/_audit_part4.txt` | `43a8ce00dc25` | `ad89424325a2` |
| `.tmp/_r6_evidence.py` | `239cad89b5c5` | `e60f811604cc` |
| `.tmp/_trae_audit_part3.py` | `6a409f23309c` | `6dff3aa38b81` |
| `.tmp/_trae_audit_part3b.py` | `13511b18379a` | `d3afcff64d72` |
| `.tmp/_trae_audit_part4.py` | `7f2fba38c479` | `c3e09bc0f03a` |
| `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | `223297c38fb6` | `fbcc85ae9b1d` |
| `results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` | `3ef2e8075f1b` | `62e38ee7b8f3` |
| `results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | `a7a80c786fa2` | `3b131b61a712` |
| `results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | `1397dbcbeafe` | `3d1f7d0174b7` |
| `results/_ghostref_copy_log_2026_09_23.json` | `be98a7b238b0` | `3a0774bd6a95` |
| `results/_glm_response_v2_template_2026_09_18.md` | `9da3d432a134` | `69fade5420f2` |
| `results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | `9aabb430172f` | `29b45ba24ab9` |
| `results/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | `1842e1b1dd01` | `aec1c93d1e90` |
| `results/_t1_qwen_temp_sweep_executor_2026_10_09.py` | `a87adc2ed532` | `3d51bfffd3d1` |
| `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | `b633a675c9de` | `4fa77864eca7` |
| `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | `ff15ac539b98` | `2b096d07501f` |
| `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | `308419654ed7` | `b4f964ab73a9` |
| `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | `d1905830b2bd` | `e32047ecc3f3` |
| `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_tmp_cleanup_2026_09_28.md` | `a2c177ec2bfe` | `aa3a94399724` |

📌 **如实限定（⛔ 0 判回执为伪）**：回执 R-S3 载「**279 件：本地三源（repo／sub／归档区）既有副本之内容 SHA 与远端逐件相符**」。
本棒之实测为「**仓内双区（repo＋sub）之副本与远端删前 blob 不符**」；若 R-S3 之主张成立，其相符之副本**只能在归档区**——
而归档区依冻结件 §0 为 **0 触区（本棒未核）**。故本项**登记为待核**（`KD-MC-06`），**⛔ 0 断言回执失实，⛔ 0 断言归档区无副本**。

### §5-2 仓内双区均无副本（81 件 · **⛔ 0 断言为真缺件**）

依冻结件 §6「三处均无 ⇒ 如实写真缺件，⛔ 0 编造来源」——然本棒**只核了仓内双区**（第三源归档区 **0 触未核**），
故**诚实定性**：**「仓内无副本 · 归档区未核 · 非真缺件之断言」**，列 `KD-MC-07` 候 PI 授权核归档区。
（含 `docs/V3X/D3_ONLINE_MIDMID_TEMPLATE.md` 之真名 `docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md`——即回执 R-S3 自承「本地无相符副本（none 1）」之件，**与回执自述相符** ✅）

| 路径 | 回执载 bytes | 回执载删前 SHA-1-12 |
|---|---|---|
| `.tmp/_b12_q4_anchor_probe_2026_09_29.py` | 4,142 | `e639d79f3a82` |
| `.tmp/_c5_b_prestate_baseline.json` | 1,543 | `ca0b3b81b7ce` |
| `.tmp/_cpatomic_keyscan_2026_09_28.json` | 2,672 | `ddb27880cb79` |
| `.tmp/_cpatomic_patch_manifest_2026_09_28.json` | 357 | `79d2d3cf9c12` |
| `.tmp/_cpatomic_pycache_post_2026_09_28.json` | 6,476 | `66a057896f09` |
| `.tmp/_cpatomic_pycache_pre_2026_09_28.json` | 10,772 | `6dd00db4ba4f` |
| `.tmp/_cpatomic_verify_2026_09_28.json` | 3,144 | `0b0a6883ab57` |
| `.tmp/_d4_relabel_run1.log` | 1,158 | `974578688ea3` |
| `.tmp/_diff21_anchor_drift.txt` | 20,994 | `d55669326b31` |
| `.tmp/_docwriter_wt2_enum_final_2026_09_30.tsv` | 66,339 | `57f620eaca69` |
| `.tmp/_e3536.txt` | 2,248 | `1d0ed76deb8b` |
| `.tmp/_e50_c1.md` | 16,236 | `f94990aef3b4` |
| `.tmp/_e50_c2.md` | 17,220 | `ce129294776f` |
| `.tmp/_final_sha.txt` | 611 | `19615837a94f` |
| `.tmp/_gaps.txt` | 435 | `4af923ea421a` |
| `.tmp/_gaps2.txt` | 2,377 | `57855e19a280` |
| `.tmp/_l14v3_aggregated_10cells.json` | 634,458 | `74e9b4667bad` |
| `.tmp/_l14v3_aggregated_10cells_v2.json` | 243 | `b412df2c3d70` |
| `.tmp/_l14v3_aggregated_10cells_v3.json` | 243 | `b412df2c3d70` |
| `.tmp/_l14v3_aggregated_10cells_v4.json` | 2,233,138 | `c254c3e3d5fd` |
| `.tmp/_l14v3_n26_metrics.json` | 1,445 | `8e3b4ad1ffc6` |
| `.tmp/_l14v3_n26_metrics_v2.json` | 2,579 | `faf22d4872ad` |
| `.tmp/_l14v3_sensitivity_v2.json` | 2,292 | `daac269ece6a` |
| `.tmp/_pk_probe2.py` | 352 | `014d8db934ca` |
| `.tmp/_pk_probe3.py` | 462 | `bbb51498524e` |
| `.tmp/_pk_probe4.py` | 176 | `bb056f3ef908` |
| `.tmp/_pk_probe5.py` | 338 | `2a0884a182a6` |
| `.tmp/_pk_probe6.py` | 257 | `5d4f6dc5cb43` |
| `.tmp/_pk_probe7.py` | 1,636 | `fa9fb4874ad6` |
| `.tmp/_pk_probe8.py` | 1,636 | `905953d35f0a` |
| `.tmp/_pkf34_probe1.py` | 633 | `384056a5f1e8` |
| `.tmp/_pkf34_probe2.py` | 604 | `2c9b2eb91b8d` |
| `.tmp/_probe21_fields.py` | 2,876 | `f2d18d779682` |
| `.tmp/_r10.txt` | 3,867 | `1a4da74b9f68` |
| `.tmp/_r11_ctx.txt` | 4,106 | `79732c90c8a4` |
| `.tmp/_r1_scratch_bom.json` | 17 | `ce2eb62d8e53` |
| `.tmp/_r1_scratch_corrupt_a.json` | 15 | `98a98d1ad5fb` |
| `.tmp/_r1_scratch_good.json` | 14 | `6c61612aff4c` |
| `.tmp/_r4_cleanup_worker_keyscan_results_2026_09_29.json` | 75 | `ed90d28bb0bd` |
| `.tmp/_r4_key_scan_r1_files_2026_09_27.json` | 2,313 | `439e68738f93` |
| `.tmp/_r4_key_scan_results_2026_09_24.json` | 1,014 | `898e7cb3f1fc` |
| `.tmp/_r6_evidence.txt` | 30,834 | `d94143c77e96` |
| `.tmp/_recheck_r1_runA.log` | 2,634 | `eeb137ee0997` |
| `.tmp/_recheck_r1_runB.log` | 2,634 | `eeb137ee0997` |
| `.tmp/_recheck_r1_runC.log` | 2,568 | `ddd32d5b8398` |
| `.tmp/_recheck_r1_runD.log` | 2,568 | `ddd32d5b8398` |
| `.tmp/_rj5_convention_check_2026_09_27.out.json` | 8,983 | `77ccf7e3f367` |
| `.tmp/_rj5_mapping_test_2026_09_27.out.txt` | 1,384 | `3a2decf0d8cf` |
| `.tmp/_run_output.log` | 1,420 | `5365182c8f1c` |
| `.tmp/_t15_inspect3_out.txt` | 1,588 | `f8808795aad0` |
| `.tmp/_t15_inspect4_out.txt` | 3,057 | `622ae907e666` |
| `.tmp/_t15_inspect5_out.txt` | 933 | `06b00b56614a` |
| `.tmp/_t15_inspect6_out.txt` | 6,659 | `39267bbc3ea0` |
| `.tmp/_t15_inspect7_out.txt` | 3,647 | `8979135365bd` |
| `.tmp/_t15_percell.txt` | 491 | `50c3f87b8ca2` |
| `.tmp/_t15_percell_out.txt` | 772 | `248e83a89852` |
| `.tmp/_t15r2_checkpoint_warn.jsonl` | 914 | `dd348b05a666` |
| `.tmp/_tail3_atomic_make_2026_09_29.json` | 19,595 | `2624d4f8f34f` |
| `.tmp/_tail3_atomic_refs_2026_09_29.json` | 5,784 | `9dbe95f45ee0` |
| `.tmp/_tail3_atomic_verify_2026_09_29.json` | 11,116 | `3faa1bc953fb` |
| `.tmp/_v16_full_decoded.txt` | 174,424 | `8afc120c47f0` |
| `.tmp/_v16_tail_dump.txt` | 174,424 | `8afc120c47f0` |
| `.tmp/_v16_tail_only.txt` | 3,471 | `40a94d0d129f` |
| `.tmp/_v3r1_diag.json` | 5,699 | `c78e5368c61f` |
| `.tmp/_v3r1_run1.log` | 5,062 | `6d08fef6755f` |
| `.tmp/_v3r1_run2.log` | 2,066 | `58a557cb0426` |
| `.tmp/_v5_item21_patch.diff` | 19,685 | `9ce076070280` |
| `.tmp/_v5_item21_patched_b1_semA_none_default.py` | 16,768 | `2d02d5547f4f` |
| `.tmp/_v5_item21_patched_b1_semB_none_skip.py` | 16,829 | `05353829c864` |
| `.tmp/_v5_item21_patched_b2_semA_none_default.py` | 16,036 | `53b844a9e184` |
| `.tmp/_v5_item21_patched_b2_semB_none_skip.py` | 16,097 | `73a7d1558159` |
| `.tmp/_v5_item21_patched_b3_semA_none_default.py` | 15,778 | `df9efa13fa0a` |
| `.tmp/_v5_item21_patched_b3_semB_none_skip.py` | 15,839 | `ea7df8d6c21b` |
| `.tmp/verif_doubt6/baseline_pre.json` | 95,139 | `faf21d9c274e` |
| `docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md` | 4,397 | `a0ea7fd3795d` |
| `results/_archive_2026_09_20/_audit_temp_inspect_minimax_m3.py.bak` | 1,171 | `96bb0a05de8b` |
| `results/_archive_2026_09_20/_audit_temp_inspect_workers.py.bak` | 1,158 | `843afd0baa41` |
| `results/_archive_2026_09_20/_audit_temp_stage1_tra_breakdown.py.bak` | 18,023 | `e96ad684b886` |
| `results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` | 5 | `af0744ae0a65` |
| `results/_archive_2026_09_20/_tmp_probe_archive` | 1,270 | `4edd37d18fbc` |
| `results/_v4_tmp_cleanup_2026_09_28.md` | 5,131 | `aa3a94399724` |

---

## §6 新出 KD 登记（编号域 `KD-MC-*` · 实测 0 占用）

📌 冻结件 **X-2**：比对中所生之新发现，⛔ **0 径改冻结件**，而以 `KD-MC-*` 登记。
📌 编号域占用实测：`grep -r "KD-MC-"` 全仓 **0 命中**（落笔前实测）✅
📌 ⛔ **0 闭任何既有 KD** ｜ ⛔ **0 落五终判** ｜ ⛔ **0 宣告任何段毕** ｜ ⛔ **0 代 PI 裁**

| KD | 面 | 事实（实测） | 处置 |
|---|---|---|---|
| `KD-MC-01` | 拉回候选构成 | 面① 172 件中 **79 件为 `.log`/`.err`/`.flag`** ＋ **70 件为 `_archive_2026_09_20/` 残留**，多为编译/运行日志 | **候 PI 裁**：全部拉回 或 仅拉回实质件（日志/旗标除外）。本棒 ⛔ 0 代裁 |
| `KD-MC-02` | 补传候选构成 | 面②真候选 209 件中 **144 件为 `_remote_pullback_2026_10_17/`（拉回落地面）**——系**自远端拉回之副本**，⛔ 非上传面实体 | **候 PI 裁**：是否属补传面。冻结件**未含**此排除码（事前列入 `E1`–`E5` 之外）⇒ 依 X-2 以 KD 登记，**⛔ 0 径改冻结件** |
| `KD-MC-03` | 前缀面残留 | **远端前缀面 `results/_archive_2026_09_20/` 仍残留**（面① 中 **70 件**；其中 `.log` 为主体）——前轮 298 路径删除**仅删其 5 件**（回执 R-S4 明载），⛔ 非整目录 | **候 PI 裁**：是否续删整目录。⚠ 该目录含 `.pdf`/`.md` 实质件与大量日志，**⛔ 0 径行整目录删除** |
| `KD-MC-04` | 仪器缺陷（自审） | 首轮对账以 **SHA-256-12** 对远端 **Git-blob-SHA-1** → 恒不等 ⇒ **假碰撞 2,862 件**。修正后真碰撞 **514** 件、已对齐 **2,348** 件 | **已修仪器**（改以 Git-blob-SHA1-12 对齐）；⛔ **0 改文本以迁就仪器**；本件所载为**修正后**之数 |
| `KD-MC-05` | 双区内容漂移 | ``results/_v5_theory_input_acquisition_request_2026_09_29.md``：repo `c062bdef8ec7` ⇔ sub `368bdd601d40`（bytes 10,751 ⇔ 10,691） | **候 PI 裁**：何者为权威。⛔ 0 以任一区覆盖另一区 |
| `KD-MC-06` | 删除面副本内容不一致 | §5-1 之 **21 件**：仓内副本与远端删前 blob 不符；回执 R-S3 之相符主张若成立则依据在归档区（**本棒 0 触未核**） | **候 PI 授权核归档区**；⛔ 0 判回执失实 |
| `KD-MC-07` | 仓内无副本 | §5-2 之 **81 件**：远端已删 ＋ 仓内双区 0 在位；第三源归档区 **0 触未核** | **候 PI 授权核归档区**；⛔ 0 断言为真缺件、⛔ 0 编造来源 |
| `KD-MC-08` | `.gitignore` 双面并存 | 远端**两级**并存：根层 `.gitignore` **105 B / `4fc0d746af9d`**（＝本地 repo 之 105 B **对齐**）＋ 前缀面 `_september_workspace/.gitignore` **91 B / `b23ed435697e`**（＝回执 R-S1 载「仍 91 B 旧版·KD-REV18-2」之实体，**与本地 105 B 异**） | 前缀面者**复现 KD-REV18-2**（本棒 ⛔ 0 闭该 KD、⛔ 0 代修）；**候 PI 裁**补传时之取值 |
| `KD-MC-09` | 「〔W老师〕」字面 | 真候选中 **9 件**之路径含 `WANG_TEACHER` 或 `〔IM〕`（同族「〔W老师〕」〔IM〕推送面；**全部位于 sub 区**）｜PI 曾裁（`results/_root_session_history_memo_2026_10_14.md:119`）「除致谢外尽量不要提及〔W老师〕相关内容」 | **候 PI 裁**是否补传；⛔ 0 代裁、⛔ 0 径删本地实体（**0 触之实体不得由本棒处置**） |
| `KD-MC-10` | 本地区面非冻结 | 枚举**稳定性复测**：两次枚举间 repo 件数 **4,124 → 4,121**（复测实测：4,124 → 4,121），变动 = 新增 1（本棒自产脚本） ／ 移除 4 ／ 内容变 2（本棒自产 JSON）（全在 `.tmp/`）⇒ **测量窗内有并发写入** | 📌 **时效限定**：本件本地侧读数为**测量时刻**之快照；委托件执行前**须复测**（冻结件 §0 之时效原则） |

---

## §7 如实交代 · 仪器自审 · 边界

### §7-1 仪器缺陷之自审（**测量仪器自身即误差源**）

| # | 缺陷 | 症状 | 修正 | 影响 |
|---|---|---|---|---|
| 1 | 哈希基准错配 | 以 SHA-256-12 对远端 Git-blob-SHA-1 ⇒ 恒不等 | 改以 Git-blob-SHA1-12 对齐（`hashlib.sha1("blob %d\0" % size + content)`），SHA-256-12 仍留作本地 manifest | 假碰撞 2,862 → **真碰撞 514**（**未改任何文本以迁就仪器**） |
| 2 | 路径探测双重前缀 | 查 `_september_workspace/.gitignore` 时误加前缀 ⇒ 误报「不在位」 | 以全树 `.gitignore` 后缀扫描复核 ⇒ **91 B 实体在位** | 险些误报 `KD-REV18-2` 已消解；**实为仍存**（`KD-MC-08`） |
| 3 | **本交付件自身（v0）** | 落盘后自查发现 v0 有 **7 处缺陷**：占位符 `V_H12`／`K_H12`／`ALIGNF3`／`CLOSURE_REMOTE`／`CLOSURE_LOCAL` 五处**未填**（旧守卫正则只拦纯大写下划线形者，故漏之）、§1-2 双反引号、稳定性数值误取、`§5` 标题「293＋5」与正文不符、「〔W老师〕」计数口径过窄（只数 `WANG_TEACHER`，漏 `〔IM〕` 同族） | ①修模板 ②**守卫强化为「正文 0 花括号」**（`BRACE LEFTOVER` 硬失败——本轮即由该守卫拦下我自述文字中之字面花括号，**证明其生效**）③范围表述改「本轮 293 条」④计数口径放宽为 `WANG_TEACHER`∨`〔IM〕` ⑤重出 | v0 已被取代；**未改任何既有件一字**（v0 系本棒自产之缺陷产物）。版本链见 §7-5 |

### §7-5 本件之版本链（自审留痕 · 如实交代）

| 版 | bytes | SHA-256 | 状态 |
|---|--:|---|---|
| `v0` | 131,439 | `d4f987f73f852c3ffe57304b0940535ed7ee086c9824d44149d01f7689d89eb2` | ⛔ **已取代**（占位符未填 ＋ 5 项表述/口径缺陷，见 §7-1 第 3 行） |
| `v1` | 131,502 | `4162f0972b544e534e4a2d0d359e5cd51ad37ad59fcba9c1c86ee991fbb5d744` | ⛔ **已取代**（未含本版本链自审段） |
| `v2` | 133,384 | `3d0b6f9f43740a831bf124f66a4c63204f62935d110bccfbbc83409e82fae7ae` | ⛔ **已取代**（A-4「落盘自证」为**悬空引用**——件内无该节；属本棒第 4 处自身缺陷） |
| `v3` | 133,978 | `770f4269dcc704b46a9ab48b4a2350dff60c4bc5ccd9da6cba5f7251da7ff547` | ⛔ **已取代**（§7-5 之「见文末」仍为悬空引用——**悬空引用共 2 处**，均已清除） |
| `v4` | *（旁证件载）* | *（旁证件载）* | ✅ **本件（现行）** |

📌 **为何现行版之自身指纹不内嵌**：**自指哈希不可解**（写入自身哈希即改变自身字节）——故现行版（`v3`）之 bytes/SHA-256 **由落盘后以异工具实测自报于旁证件** `.tmp/_mirror_morph_deliver_selfcert_2026_10_18.txt`，⛔ 0 内嵌、⛔ 0 预估。

📌 **⛔ 0 隐瞒**：本棒交付件经**四轮自查修正**方达现行版（v0 占位符/口径 → v1 版本链 → v2 悬空引用×1 → v3 悬空引用×2）；被取代之三版指纹**照录于上**，**⛔ 0 抹除其存在**。
📌 被取代版之 0 留存实体（未复制、未另存）——其内容已全部并入现行版，差异仅为上述 7 处缺陷之修正。

### §7-2 未软化之交代（逐条）

1. **回执终态 HEAD 已漂移**：`bd89e1ff` → live `4cd417b32e5d4ae05de95825e2d13d602b8b928a`（新增 1 commit ＝ 执行回执自身）。本件一切远端读数以实测为准。
2. **回执「279 件内容相符」之仓内侧未被复现**：21 件仓内副本与远端删前 blob 不符（`KD-MC-06`）——但 ⛔ **0 据此判回执为伪**（其相符副本或仅存于 0 触之归档区）。
3. **「远端 0 在位」之断言均以 `truncated=false` 为前提**（实测 `truncated=false`）；若日后复测遇 `truncated=true`，此类阴性断言**一律无效**。
4. **本地侧为移动靶**：测量窗内 `.tmp/` 有并发增删（`KD-MC-10`）；本件本地读数为**测量时刻**快照。
5. **归档区 0 触** ⇒ §5-2 之 81 件**⛔ 0 断言为真缺件**；**⛔ 0 编造来源**。
6. **`S3` 隐私面归属未断**：23 件形态命中者**一律列「归属待 PI 判定」**（冻结件 X-3），⛔ 0 以文件名臆断、⛔ 0 自造逐件清单。
7. **遗留面之清洁不可外推**：遗留面三项专查 0 残留 ✅，然**前缀面 `_archive_2026_09_20/` 仍残留 70 件**（`KD-MC-03`）——⛔ 0 以遗留面清洁充全仓清洁。
8. **⛔ 0 闭任何既有 KD · ⛔ 0 落五终判 · ⛔ 0 宣告任何段毕 · ⛔ 0 代 PI 裁**：本件**全条遵守**。

### §7-3 根层遗留面 · 根层文件清单（68 件）

| 根层文件路径 |
|---|
| `.gitignore` |
| `LICENSE` |
| `README.md` |
| `README_V1_LEGACY.md` |
| `RELEASE_v1.4.0.md` |
| `audits_outliers.json` |
| `audits_security.json` |
| `deposon_agents_v1_3.py` |
| `deposon_agents_v1_4.py` |
| `deposon_diffusion.py` |
| `deposon_fast.py` |
| `deposon_g2_modes.py` |
| `deposon_photonics.py` |
| `deposon_protocol.py` |
| `gt_common.py` |
| `handoff_machine_readable.json` |
| `llm_fetch.py` |
| `llm_prior.py` |
| `mindmap_corpus_v20.py` |
| `requirements.txt` |
| `run_benchmark_v1_3.py` |
| `run_benchmark_v1_4_gsm8k.py` |
| `run_benchmark_v1_4_strategyqa.py` |
| `run_g2_ensemble.py` |
| `run_v15_experiment.py` |
| `run_v16_llm_prior.py` |
| `run_v17_fixed_sampler.py` |
| `run_v17_fusion_fix.py` |
| `run_v17_multigraph.py` |
| `run_v18_api_supplements.py` |
| `run_v19_benchmark_fixes.py` |
| `run_v19_fullrank.py` |
| `run_v19_meanfield.py` |
| `run_v19_quickwins.py` |
| `run_v20_baselines.py` |
| `run_v20_bigquiz_eval.py` |
| `run_v20_bigquiz_fetch.py` |
| `run_v20_corpus_eval.py` |
| `run_v20_cot_fetch.py` |
| `run_v20_crossval_eval.py` |
| `run_v20_crossval_fetch.py` |
| `run_v20_familyL_fetch.py` |
| `run_v20_familyL_ingest.py` |
| `run_v20_fastcheck.py` |
| `run_v20_gt.py` |
| `run_v20_gt2b.py` |
| `run_v20_gt3_eval.py` |
| `run_v20_gt3_fetch.py` |
| `run_v20_gt3b_fetch.py` |
| `run_v20_gt3c_fetch.py` |
| `run_v20_gt5.py` |
| `run_v20_gt5b.py` |
| `run_v20_gt6.py` |
| `run_v20_gt7.py` |
| `run_v20_gt8.py` |
| `run_v20_gt8b_eval.py` |
| `run_v20_gt8b_fetch.py` |
| `run_v20_gt8b_ingest.py` |
| `run_v20_gt8c_eval.py` |
| `run_v20_gt8c_fetch.py` |
| `run_v20_gt8c_ingest.py` |
| `run_v20_photonics.py` |
| `run_v20_quizbank.py` |
| `run_v20_vector_audit.py` |
| `run_v21_gtformal.py` |
| `run_v22_e95ci.py` |
| `run_v22_p1c.py` |
| `svg_mindmap_ingest.py` |

### §7-4 证据件清单（`.tmp/` · 本棒自产 · 0 断言其为既有资产）

| 证据件 | 用途 |
|---|---|
| `.tmp/_mirror_morphology_criteria_freeze_2026_10_18.md` | **FTFB 判据冻结件**（先于一切比对） |
| `.tmp/_mirror_morph_remote_tree_2026_10_18.json` | 远端全树原始响应（`truncated=false` 之证） |
| `.tmp/_mirror_morph_remote_summary_2026_10_18.json` | 远端形态摘要（HEAD/tree/遗留面） |
| `.tmp/_mirror_morph_local_enum_2026_10_18.json` | 本地双区全量枚举（路径·bytes·SHA-256-12·Git-SHA1-12） |
| `.tmp/_mirror_morph_recon_2026_10_18.json` | 三面对账全量明细（面①②③·排除码·非对称·同一性） |
| `.tmp/_mirror_morph_residual_out_2026_10_18.txt` | 残留面专项核查输出 |
| `.tmp/_mirror_morph_deliver_selfcert_2026_10_18.txt` | **本交付件之落盘自证旁证件**（bytes·SHA-256·BOM·CR·key 扫描·写出时刻） |
| `.tmp/_mirror_morph_freeze_write_2026_10_18.py` 等 6 脚本 | 冻结/对账/分析/残留/删除面/生成器之写出器 |

---

## §8 交付与验收（自证）

| 判据 | 实测 |
|---|---|
| A-1 远端树完整性 | `truncated=false` ✅ ｜ **阴性断言先证扫描完整** ✅ |
| A-2 本地遍历错误 | repo **0** ／ sub **0** ✅ |
| A-3 三面自洽 | 前缀面 3,034 ＝ 172＋2,348＋514 ✅ ／ 本地并集 5,389 ＝ 2,862＋2,527 ✅ |
| A-4 字节级自报 | **落盘后由异工具亲测回读**并自报于棒回执；旁证件：`.tmp/_mirror_morph_deliver_selfcert_2026_10_18.txt`（因**自指哈希不可解**，⛔ 0 内嵌于本件，见 §7-5） |
| A-5 落前检查 | `Test-Path=False` ＋ `glob` **0 命中** ✅（落盘前实测） |
| A-6 引件先测指纹 | §0 三件皆先实测 ✅ |
| A-7 0 触与 0 实验 | 归档区 0 触 · GLM 0 触 · **0 实验** · 0 凭据 ✅ |

---

**件止** ｜ *evidence-auditor（证据链审计官）* · 2026-10-18 · **镜像形态对比件（取证面）· 候 PI 阅 · ⛔ 0 代裁** —— 本件仅出**对比**与**取证**，**⛔ 0 代出委托件**（委托由 doc-writer 据本件另出）；⛔ 0 闭既有 KD · ⛔ 0 落五终判 · ⛔ 0 宣告①毕/②毕/③毕/④毕/⑤毕 · ⛔ 0 代 PI 裁 · ⛔ 0 实验 · ⛔ 0 触归档区 · ⛔ 0 触 GLM 面 · ⛔ 0 远端写 · ⛔ 0 经手凭据 ｜ **既有件触动数 ＝ 0**（append-only）
