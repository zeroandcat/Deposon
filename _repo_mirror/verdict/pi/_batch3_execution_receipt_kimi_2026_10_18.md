# 第三批执行回执 ｜ 改名 ＋ 拉回 172 ＋ 删 70 ＋ 传 590（23＋56＋511）｜ KIMI ｜ 2026-10-18

- 裁定源件：`letters/_final_rulings_compilation_kimi_2026_10_18.md`（SHA-12 `832E69EB49A4` ／ 37,950 B · 唯一裁定稿 · PI 核准后传出 · 17 裁合卷）
- 委托源件：新委托（`6bd84d3f4e94`）＋改名补充委托（`77962d9b64de`）＋ v0.4（`51ca14265086`）＋唯一补函（`557d61c1eb5a`）——四者原样并存
- 执行棒：KIMI（受托方 · 远端写／删／拉回之执行）｜全部 ref 更新 fast-forward、0 force；删除逐件独立 commit；传面按面分批 commit（沿 53 件先例之体例）

## 执行总览与 HEAD 链

| 时点 | HEAD ／ commit | 事件 |
|---|---|---|
| 序 0 基线（R-A-8） | `4cd417b32e5d4ae05de95825e2d13d602b8b928a` | live HEAD 重取 · 与对比件基线同一 · 0 漂移（commit 时间 2026-10-18T05:38:54Z） |
| 序 1 改名 | `5d31b4be381c02ad42fe8ebbfa3cdc9249b4ef51` | `_september_workspace/` → `_repo_mirror/`（单 commit · 6,068 tree ops · blob 全不变 · 前缀面 .gitignore 91B→105B） |
| 序 2-c 传 S3-23 | `768e43af3ced8bb02a644f0b86373cf60bd45ea1` | 23 件脱敏副本新传 |
| 序 2-c 传 丙档56 | `9ec782b2b1b5944c2f66c6f18d608c9df4ffefbc` | 56 件新传 |
| 序 2-c 覆盖面 511 | `739a7daf533b6ead320667d924ab0884c9614edc` | 509 件脱敏后覆盖＋组A 2 件 |
| 终态 | `739a7daf533b6ead320667d924ab0884c9614edc` | 全树 3,456 blobs · truncated=False |

序 2-b 删 70 ＝ 70 个独立 commit（逐件见 R-A-4 表）。序 2-a 拉回 ＝ 本地动作（0 commit）。

---

# R-A-1 ｜ 收悉之确认

- 已收悉唯一裁定稿：`letters/_final_rulings_compilation_kimi_2026_10_18.md`（SHA-12 `832E69EB49A4` ／ 37,950 B）——17 裁（裁一～裁十七）＋ §2 总序＋ §3 前置面＋ §5 回执面，全卷通读

# R-A-2 ｜ 序 1 改名（裁一＋裁二 · 单 commit）

- commit `5d31b4be381c02ad42fe8ebbfa3cdc9249b4ef51`；改名后 live HEAD ＝ `5d31b4be381c02ad42fe8ebbfa3cdc9249b4ef51`
- 旧前缀残留 **0**（期望 0）｜新前缀 blobs **3,034**｜根层遗留 **413**｜总 blobs 3,447（改名前后恒定）
- **blob 全不变之校核**：改名前后 blob 多重集之差 ＝ 仅 `.gitignore` 一处（旧 `b23ed435697e` 91B → 新 `4fc0d746af9d` 105B，即裁二之取值；该 blob 与根层 `.gitignore` 同一，0 新建 blob）
- 终验：`_repo_mirror/.gitignore` ＝ `4fc0d746af9d` ／ 105 B（105 B 新版 · 含 `.tmp/` 行 ⇒ **止血成就**）；truncated=False

# R-A-3 ｜ 序 2-a 拉回 172 件（裁五·裁十三 · 全数 · 落归档区 · ⛔ 0 入仓）

- 拉回 **172/172**（failed=0）｜落点根：`〔归档件引用·未上传:_mirror_pullback_172_2026_10_18〕\`（独立子目录 · 0 覆写既有归档 · **0 入仓**）
- 逐件核验：取回字节之 git blob SHA-1 与远端逐件相符 172/172；落盘后 SHA-256-12 逐件登记于下表
- 仪器如实交代：首轮经 `/contents` 径取回时 **42 件 `.log`** 因该径对非 UTF-8 字节之重编码而字节偏移（sha 校验即时拦截，0 落盘）⇒ 改经 `/git/blobs/<sha>` 径字节级重取，42/42 修复 ⇒ **172/172 字节级相符**

| # | 仓内路径（远端＝`_repo_mirror/<rel>`） | bytes | git SHA-1-12 | 落档 SHA-256-12 | 属70件删面 |
|--:|---|--:|---|---|:-:|
| 1 | `.trae/audit/compile_evidence/DONE.flag` | 85 | `62d11e56a062` | `3FE4DB4261E6` |  |
| 2 | `.trae/audit/compile_evidence/cn_pdflatex_pass2.log` | 74,481 | `767d26050580` | `E35B58FF8678` |  |
| 3 | `.trae/audit/compile_evidence/cn_pdflatex_stdout.log` | 1,386 | `fe5fe2b8b2d0` | `8E2D26F9CBB5` |  |
| 4 | `.trae/audit/compile_evidence/en_pdflatex_pass2.log` | 45,951 | `7476489839da` | `62BE98532216` |  |
| 5 | `.trae/audit/compile_evidence/en_pdflatex_stdout.log` | 1,386 | `52941f523383` | `56E405E8D23F` |  |
| 6 | `.trae/audit/compile_evidence/v1_62refs_20260908/DONE.flag` | 33 | `1ecf5c39db74` | `1E7DCB4DEE3C` |  |
| 7 | `.trae/audit/compile_evidence/v1_62refs_20260908/cn_pdflatex_pass2.log` | 74,268 | `957e7426e0db` | `48695210A6B9` |  |
| 8 | `.trae/audit/compile_evidence/v1_62refs_20260908/cn_runner.log` | 1,278 | `6507336ade0e` | `BD2B6476FE94` |  |
| 9 | `.trae/audit/compile_evidence/v1_62refs_20260908/en_pdflatex_pass2.log` | 45,794 | `bf6c810051d1` | `C3A68CDF165D` |  |
| 10 | `.trae/audit/compile_evidence/v1_62refs_20260908/en_runner.log` | 1,278 | `d98befafc10e` | `D80135E2CBF4` |  |
| 11 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/DONE.flag` | 85 | `0943ef645f9c` | `30247E72B26E` |  |
| 12 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/EXTRACT_NEW.flag` | 102 | `d0887c6d2fa8` | `B02164316CF8` |  |
| 13 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/cn_pdflatex_pass2.log` | 60,325 | `1381b75d060b` | `3C67684916FE` |  |
| 14 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/cn_pdflatex_stdout.log` | 1,386 | `fe5fe2b8b2d0` | `8E2D26F9CBB5` |  |
| 15 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/en_pdflatex_pass2.log` | 39,448 | `936582d2d57b` | `1F74BFB1E9BB` |  |
| 16 | `.trae/audit/compile_evidence/v2_overfull_fix_20260909/en_pdflatex_stdout.log` | 1,386 | `52941f523383` | `56E405E8D23F` |  |
| 17 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/COMPILE_SUMMARY.txt` | 1,693 | `d6a600658c5c` | `1BAD41B3929F` |  |
| 18 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/DONE.flag` | 85 | `62d11e56a062` | `3FE4DB4261E6` |  |
| 19 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/cn_pdflatex_pass2.log` | 74,481 | `767d26050580` | `E35B58FF8678` |  |
| 20 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/cn_pdflatex_stdout.log` | 1,386 | `fe5fe2b8b2d0` | `8E2D26F9CBB5` |  |
| 21 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/en_pdflatex_pass2.log` | 45,951 | `7476489839da` | `62BE98532216` |  |
| 22 | `.trae/audit/compile_evidence/v2pre_h1h3_20260909/en_pdflatex_stdout.log` | 1,386 | `52941f523383` | `56E405E8D23F` |  |
| 23 | `_mirror_manifest.json` | 192,689 | `0a92d7bd23f1` | `E4548DC95E27` |  |
| 24 | `corpus/v20_caption_surface/_adendum_I_po_captions_closure_20260917_132049.json` | 4,429 | `df5e8e3c7f2d` | `18165008BEF6` |  |
| 25 | `deposon_team/plugins/_v4_wide_s1b_inv2_2026_09_27.py` | 1,546 | `b3de03b9c386` | `AF475F496A5E` |  |
| 26 | `deposon_team/plugins/_v4_wide_s2_scan_2026_09_27.py` | 4,000 | `320eb0da8f13` | `C2CC22B27047` |  |
| 27 | `deposon_team/plugins/_v4_wide_s3_keyscan_2026_09_27.py` | 2,647 | `d591872191e1` | `A32AF07111DF` |  |
| 28 | `deposon_team/plugins/_v4_wide_s3b_uuidctx_2026_09_27.py` | 1,707 | `30a2b0875241` | `8FDEC59AA96B` |  |
| 29 | `deposon_team/plugins/_v4_wide_s3c_keydetail_2026_09_27.py` | 2,490 | `49aaf6223a34` | `16AE5764ADD1` |  |
| 30 | `deposon_team/plugins/_v4_wide_s4_verify_2026_09_27.py` | 2,812 | `05ac84a856ad` | `DBE00430D769` |  |
| 31 | `deposon_team/plugins/_v4_wide_s6_unrefscan_2026_09_27.py` | 2,495 | `daf43fb20421` | `1B31A3111A86` |  |
| 32 | `deposon_team/plugins/_v4_wide_s7_fix_2026_09_27.py` | 6,101 | `0deb7931c842` | `FC200E5F343D` |  |
| 33 | `deposon_team/plugins/_v4_wide_s8_fix3_2026_09_27.py` | 3,514 | `5bf93f2343ff` | `051DBDB121C9` |  |
| 34 | `deposon_team/plugins/_v4_wide_s9_final_2026_09_27.py` | 3,399 | `22e371480238` | `AEF86F53CC0E` |  |
| 35 | `deposon_team/plugins/_v4_wt_s5_verify_2026_09_27.py` | 4,950 | `9a23a8f01f35` | `736E56CD5553` |  |
| 36 | `deposon_team/plugins/_v5_wa_s1_2026_09_30.py` | 4,351 | `713ec0c3bf0c` | `F77F72F7B86E` |  |
| 37 | `deposon_team/plugins/_v5_wa_s2b_2026_09_30.py` | 3,583 | `4815f547278f` | `9403DFAC5824` |  |
| 38 | `deposon_team/plugins/_v5_wa_s2c_2026_09_30.py` | 3,168 | `581e5d0565e2` | `2F55832A82CB` |  |
| 39 | `deposon_team/plugins/_v5_wa_s3_fix_2026_09_30.py` | 4,742 | `4b785e9b99bd` | `FF16D68FDB81` |  |
| 40 | `docs/V3X/D7_EXTERNAL_ADVISOR_ONLINE_PUSH_REQUIREMENTS_2026_09_18.md` | 8,066 | `8adff5e918e3` | `244B76B690F0` |  |
| 41 | `docs/V3X/LETTER_FROM_TRAE_2026_09_11.md` | 13,629 | `720cfaf53161` | `0C1028B9500A` |  |
| 42 | `docs/V3X/LETTER_FROM_TRAE_3RISK_2026_09_11.md` | 5,145 | `f60d3f3eca8b` | `A1AFBF3E1296` |  |
| 43 | `docs/V3X/LETTER_FROM_TRAE_REVIEW_2026_09_16.md` | 7,724 | `610cd2c2bbdb` | `233CF19D9FB6` |  |
| 44 | `docs/V3X/LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md` | 3,571 | `f369e5c35f8a` | `141E05BF56EA` |  |
| 45 | `docs/V3X/TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md` | 5,154 | `b937094b1e44` | `53A90B9EFBB9` |  |
| 46 | `docs/V3X/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md` | 16,008 | `4670cf5c9b75` | `A13D233E350D` |  |
| 47 | `docs/V3X/TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md` | 7,376 | `158b0518e100` | `9AA717B2E1AC` |  |
| 48 | `results/AUDIT_2026-08-30.json` | 3,143 | `f8c3fdbeb1b6` | `ED5EB708F332` |  |
| 49 | `results/Deposon_评估汇总_v1_3_0.json` | 2,811 | `3adf056b6c80` | `2F02F50C164B` |  |
| 50 | `results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | 10,586 | `bcf317b88d6e` | `FF37F39264BC` | 是 |
| 51 | `results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | 7,855 | `d39d91ecd84c` | `C0D629DF69D8` | 是 |
| 52 | `results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | 9,343 | `96c744af6776` | `ACE3C6B390CB` | 是 |
| 53 | `results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | 11,575 | `f6c1e86b1542` | `0011B7924DFB` | 是 |
| 54 | `results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | 4,784 | `eb23f9346728` | `2E6A31AF5E4B` | 是 |
| 55 | `results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | 454,307 | `d10a14ba179a` | `ADC99E04AC53` | 是 |
| 56 | `results/_archive_2026_09_20/_cpath_sim_run_2026_09_10.log` | 1,508 | `10e844e84dad` | `6BFC5DDE07A8` | 是 |
| 57 | `results/_archive_2026_09_20/_d05_main_runner_20260918.log` | 9,232 | `345608fea302` | `B6657BA162B3` | 是 |
| 58 | `results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | 18,611 | `a76a2658a272` | `DC3E56ADC3FC` | 是 |
| 59 | `results/_archive_2026_09_20/_p_l_v3_phase1_finalize.log` | 1,184 | `1a098d388a6e` | `C2172607419E` | 是 |
| 60 | `results/_archive_2026_09_20/_p_l_v3_phase1_runner.log` | 8,202 | `e731a8ade38f` | `90EAD4A9FBA8` | 是 |
| 61 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner.log` | 2,370 | `ead67cc76e5d` | `37E1F9CC19D3` | 是 |
| 62 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_171640.log` | 1,516 | `2b5128e0a098` | `77B62D39F474` | 是 |
| 63 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172440_gpt56sol.log` | 865 | `1a98af38bdef` | `FEFDAC35FA6E` | 是 |
| 64 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172928_gpt56sol.log` | 955 | `d0fe6629bee3` | `EF172AD159B4` | 是 |
| 65 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_173159_gpt56sol.log` | 2,765 | `c83c63c766f4` | `A6517028A720` | 是 |
| 66 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_174011_claude_sonnet5.log` | 2,687 | `60f85dbfabc3` | `0FFA261C5ED8` | 是 |
| 67 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_175003_gemini_37flash.log` | 2,342 | `0952adb63097` | `0B61AADB4509` | 是 |
| 68 | `results/_archive_2026_09_20/_p_l_v3_phase2_finalize.log` | 2,712 | `e506d97fb9fc` | `4A707293FADA` | 是 |
| 69 | `results/_archive_2026_09_20/_p_l_v3_phase2_finalize_20260917_142748.log` | 1,224 | `19e035b669d0` | `995BAD3CCE30` | 是 |
| 70 | `results/_archive_2026_09_20/_p_l_v3_phase2_glm53.log` | 2,542 | `f85eddf2fc03` | `11F8EC231EAD` | 是 |
| 71 | `results/_archive_2026_09_20/_p_l_v3_phase2_glm53_only_20260917_142011.log` | 1,140 | `bb5e79511c7e` | `4C91156DC821` | 是 |
| 72 | `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.err` | 530 | `2c10446f7d93` | `4346E7E916DB` | 是 |
| 73 | `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.log` | 564 | `3055f18b8f1d` | `BB54209B0CDC` | 是 |
| 74 | `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding_v3_2026_09_17.console.log` | 10,102 | `5ee1916ddb81` | `4056814F73DC` | 是 |
| 75 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe.log` | 3,100 | `9678a036b1b7` | `B1128AA5441C` | 是 |
| 76 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_agent.log` | 6,760 | `54c4f808cd15` | `49765CA671D8` | 是 |
| 77 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb.log` | 2,046 | `5267d1048a6e` | `456A6BF39F9E` | 是 |
| 78 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb_proxy_v2.log` | 17,632 | `16a34c3ae004` | `B4D2803C6290` | 是 |
| 79 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_ext.log` | 4,992 | `4cb29bc0fce1` | `A72A38A9FB6F` | 是 |
| 80 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_gpt4o.log` | 3,462 | `2e5b3c200544` | `D9BF12A6F713` | 是 |
| 81 | `results/_archive_2026_09_20/_p_l_v3_phase2_runner.log` | 3,416 | `7e9ff72e8505` | `9B4CDB0EC25B` | 是 |
| 82 | `results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console.log` | 6,134 | `303659550a1b` | `1F65AD49911C` | 是 |
| 83 | `results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console2.log` | 2,925 | `d42b879bc3de` | `FCCA7035073A` | 是 |
| 84 | `results/_archive_2026_09_20/_probe_teamo_via_proxy.log` | 4,526 | `7d540c86567e` | `74BADFD3270F` | 是 |
| 85 | `results/_archive_2026_09_20/_sanity_openai_more.log` | 1,444 | `ac1d0b5bd3c2` | `C7DB5599E6A5` | 是 |
| 86 | `results/_archive_2026_09_20/_sanity_teamo_three.log` | 2,168 | `8912d907b188` | `E6E40A339EF7` | 是 |
| 87 | `results/_archive_2026_09_20/_test_3bb_vary.log` | 11,522 | `63bad8ab3356` | `699D751CED17` | 是 |
| 88 | `results/_archive_2026_09_20/_v2_stage1_60cells.console.log` | 17,158 | `f401a22768be` | `CD7710002FF0` | 是 |
| 89 | `results/_archive_2026_09_20/_v2_stage3_f3_strip.console.log` | 2,440 | `639a46fbc44c` | `0087364298E1` | 是 |
| 90 | `results/_archive_2026_09_20/_v3x_6way_finalize.log` | 618 | `e8e3eecbbe55` | `1DB3842E21E6` | 是 |
| 91 | `results/_archive_2026_09_20/_v3x_6way_run.log` | 8,952 | `cb8f0635c4e8` | `0A2E66649663` | 是 |
| 92 | `results/_archive_2026_09_20/_v3x_6way_stage3_minimal.log` | 1,678 | `2f5edcac6a91` | `A8A69C85571C` | 是 |
| 93 | `results/_archive_2026_09_20/_v3x_6way_stage3_recovery.log` | 2,242 | `713e5f75c289` | `1758B615EBB1` | 是 |
| 94 | `results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log` | 17,456 | `8b06e5d3f43d` | `7B659FDC69C9` | 是 |
| 95 | `results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log.bak` | 6,106 | `1b86970816da` | `18B56E3D1C7B` | 是 |
| 96 | `results/_archive_2026_09_20/_volc_22cap_emb.log` | 9,068 | `42c9d2e4a9ea` | `27CB6630EC37` | 是 |
| 97 | `results/_archive_2026_09_20/_worker_openrouter_rag_run.log` | 6,476 | `e56dd631a770` | `9A5603811F45` | 是 |
| 98 | `results/_archive_2026_09_20/deposon_d_fix2_metric_verify_9m60c_2026_09_15.log` | 24,634 | `e71aecfebe91` | `1EEC8B03B30F` | 是 |
| 99 | `results/_archive_2026_09_20/deposon_deepseek_v41_flash_30cells_2026_09_10.log` | 6,514 | `4de1a9c448f7` | `CBCECDEC0FDB` | 是 |
| 100 | `results/_archive_2026_09_20/deposon_dpath_cross_modal_2026_09_10.log` | 8,885 | `f33a29327e11` | `95298CA6D95E` | 是 |
| 101 | `results/_archive_2026_09_20/deposon_dpath_cross_modal_runner_2026_09_10.stdout.log` | 17,772 | `97e2aa66522f` | `388439EB8D17` | 是 |
| 102 | `results/_archive_2026_09_20/deposon_feshbach_rag_30cells_2026_09_10.log` | 6,887 | `c6aca7403cf8` | `2E8564B94B02` | 是 |
| 103 | `results/_archive_2026_09_20/deposon_v2_phase1_60cells_2026_09_11.log` | 8,578 | `3d3a6b8994db` | `B5169E715434` | 是 |
| 104 | `results/_archive_2026_09_20/deposon_v2_phase2_f2_2026_09_11.log` | 1,272 | `41eba7b8f98b` | `C0FA485CD9FE` | 是 |
| 105 | `results/_archive_2026_09_20/deposon_v2_phase3_f3_2026_09_11.log` | 1,247 | `0467038c016f` | `3B61B7028CC8` | 是 |
| 106 | `results/_archive_2026_09_20/deposon_v2_phase4_f4_2026_09_11.log` | 1,064 | `be3d138384e2` | `86812E1003E5` | 是 |
| 107 | `results/_archive_2026_09_20/deposon_v2_phase5_f5_2026_09_11.log` | 1,092 | `8cfd8dd5620c` | `AF736AA656C7` | 是 |
| 108 | `results/_archive_2026_09_20/deposon_v41_flash_60cells_v2_2026_09_10.log` | 12,470 | `ebdc60a61dbc` | `AD7FAFB3582B` | 是 |
| 109 | `results/_archive_2026_09_20/deposon_volcengine_minimax_m3_30cells_2026_09_10.log` | 3,444 | `f03cb6416a01` | `A0FC4423470C` | 是 |
| 110 | `results/_archive_2026_09_20/deposon_volcengine_seed_code_30cells_2026_09_10.log` | 7,342 | `672e14623f28` | `19F295CE9FF9` | 是 |
| 111 | `results/_archive_2026_09_20/deposon_volcengine_worker_b_2026_09_10.log` | 3,326 | `853dd2881e5e` | `5D40BDC3A0DB` | 是 |
| 112 | `results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.log` | 5,869 | `c3b87ceaad9d` | `E62CD7FD2A0E` | 是 |
| 113 | `results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.run.log` | 12,070 | `5a6919ccc9b6` | `644425852B1A` | 是 |
| 114 | `results/_archive_2026_09_20/fiction_that_feeds_back.tex` | 93,324 | `68da7b05797b` | `D060F75DBE9F` | 是 |
| 115 | `results/_archive_2026_09_20/gpt6_30cells_run.log` | 4,220 | `cd78df661d8b` | `74BBC7DCF5AA` | 是 |
| 116 | `results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | 20,082 | `7375dbcc2a8b` | `5198A7059C06` | 是 |
| 117 | `results/_archive_2026_09_20/review_tech_B1_grok46.md` | 18,923 | `5c05888226a8` | `09784FF172B3` | 是 |
| 118 | `results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | 8,098 | `3c2dd5f7c0ab` | `8D00C6D4A242` | 是 |
| 119 | `results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log` | 4,091 | `b39406b8614e` | `D2F7840EBC51` | 是 |
| 120 | `results/_archive_2026_09_21/Deposon_评估汇总_v1_3_0.json` | 2,811 | `3adf056b6c80` | `2F02F50C164B` |  |
| 121 | `results/_c5_kv3df_0_1_minmaxstd_readings_2026_10_12.json` | 7,193 | `12864634c039` | `04F14CD2FDBF` |  |
| 122 | `results/_c5_kv3df_0_1_minmaxstd_suppl_prereg_2026_10_12.md` | 5,697 | `e5df207d1ece` | `88CB33B53A7E` |  |
| 123 | `results/_c5_kv3df_0_1_minmaxstd_suppl_report_2026_10_12.md` | 8,476 | `843d944a56ec` | `31A4E2976DAB` |  |
| 124 | `results/_coze_online_v3_2026_09_18.md` | 7,476 | `68c3e712d66f` | `53C9C1AB2D12` |  |
| 125 | `results/_coze_online_v3_d7format_2026_09_18.md` | 8,727 | `0382feb27519` | `DEBE3761C565` |  |
| 126 | `results/_coze_online_v3_final_2026_09_18.md` | 11,660 | `5400179aa0e1` | `36439BC12BBA` |  |
| 127 | `results/_coze_online_v4_d7format_2026_09_26.pdf` | 465,366 | `52f222502a31` | `A82881653520` |  |
| 128 | `results/_d7_external_advisor_online_publish_v1_20260918.md` | 9,915 | `a75d029036c1` | `788FBDD8C12F` |  |
| 129 | `results/_deemphasis_sha_drift_register_B1_2026_10_06.md` | 1,206 | `56342823a0ca` | `8F13BFDE0134` |  |
| 130 | `results/_deemphasis_sha_drift_register_B2_2026_10_06.md` | 1,418 | `d68f2ef16e70` | `5DD775E634A3` |  |
| 131 | `results/_deemphasis_sha_drift_register_B3_2026_10_06.md` | 2,830 | `f35523665a53` | `28D3422D7A34` |  |
| 132 | `results/_deemphasis_sha_drift_register_B4_2026_10_06.md` | 11,715 | `736c19ff59b9` | `B7734DE6C082` |  |
| 133 | `results/_deemphasis_sha_drift_register_B5_2026_10_06.md` | 14,237 | `3bacf10ffed6` | `4CD701B819C4` |  |
| 134 | `results/_deemphasis_sha_drift_register_B6a_2026_10_06.md` | 11,696 | `04d96fe5cfa6` | `16E71608D1AD` |  |
| 135 | `results/_deemphasis_sha_drift_register_B6b_2026_10_06.md` | 22,219 | `add00a68d28a` | `B461AE908236` |  |
| 136 | `results/_deemphasis_sha_drift_register_B6c_2026_10_06.md` | 14,351 | `1603d2ce19cc` | `80BE5E5E9EF1` |  |
| 137 | `results/_e20_runner_sha_drift_dual_value_register_2026_10_12.md` | 4,352 | `6f88c954c36d` | `3CEE8E81A66E` |  |
| 138 | `results/_experiment_execution_plan_v1_1_funnel5_adopted_2026_10_18.md` | 21,411 | `c1d32ba51a59` | `C43494DDD528` |  |
| 139 | `results/_gt_reconstruction_sha_drift_dual_value_register_2026_10_12.md` | 4,789 | `7421807680d5` | `261EBBA5C09E` |  |
| 140 | `results/_pi_dual_ruling_register_ge02_acceptance_ge01_readiness_2026_10_12.md` | 19,296 | `a047342a5444` | `2E7D804DAD2A` |  |
| 141 | `results/_q2_77_74_62_three_caliber_consolidation_register_2026_10_12.md` | 4,609 | `2fb51610efcf` | `CC75F1E3D8AF` |  |
| 142 | `results/_repo_state_auth_refresh_register_2026_10_18.md` | 11,449 | `d3ec5cf4e6f1` | `60DBB71D1117` |  |
| 143 | `results/_s3_kv3s_3_4_judgment_prereg_2026_10_12.md` | 5,678 | `eb9759f2915d` | `A80D9AE8008B` |  |
| 144 | `results/_s3_kv3s_3_4_supplementary_verdict_2026_10_12.md` | 6,156 | `f9c4150ec3dd` | `338F30AD7460` |  |
| 145 | `results/_s4_kv3s_4_123_judgment_prereg_2026_10_12.md` | 5,637 | `6b0ecbcfad76` | `2CD7250C3721` |  |
| 146 | `results/_v2_setup.py._moved_20260924_1830.py` | 3,477 | `a5c77c7dc81d` | `5E8C023C6B26` |  |
| 147 | `results/_v2_show_summary.py._moved_20260924_1830.py` | 1,160 | `f81723551363` | `96D121CC4D5C` |  |
| 148 | `results/_v2_smoketest.py._moved_20260924_1830.py` | 2,042 | `be5610adfb55` | `B9DF410ACA0A` |  |
| 149 | `results/_v2_stage1_60cells.py._moved_20260924_1830.py` | 31,470 | `3e528f9919ae` | `CD147D98F7B7` |  |
| 150 | `results/_v2_stage2_f2_drift.py._moved_20260924_1830.py` | 10,760 | `3e821561537b` | `C127E8E537C0` |  |
| 151 | `results/_v2_stage3_f3_strip.py._moved_20260924_1830.py` | 11,765 | `48a46fa99a97` | `2B3ECF5459F3` |  |
| 152 | `results/_v2_stage4_f4_pdv2.py._moved_20260924_1830.py` | 10,307 | `dfeda739c97f` | `D10D93B86443` |  |
| 153 | `results/_v2_stage5_f5_dpath.py._moved_20260924_1830.py` | 6,456 | `1550772e0eed` | `6FB84EF6EC62` |  |
| 154 | `results/_v2_verify_outputs.py._moved_20260924_1830.py` | 2,544 | `af8148a9fdac` | `486C0744172A` |  |
| 155 | `results/_v4_01_knifeedge_independent_review_2026_09_29.md` | 19,731 | `718926199008` | `A66B4159793F` |  |
| 156 | `results/_v5_b14_1_k04_caliber_fixation_2026_09_29.md` | 13,127 | `47a98042d24a` | `697145C8352D` |  |
| 157 | `results/_v5_b14_r3_anchor_retrieval_2026_09_29.md` | 23,023 | `cf395fdb3282` | `6E0A1461A688` |  |
| 158 | `results/_v5_b16_1dcritical_lit_search_2026_09_29.md` | 26,931 | `c2bcd2e61452` | `09AD0C6CE46A` |  |
| 159 | `results/_v5_b16_dual_caliber_rule_2026_09_29.md` | 16,262 | `e8c841c4559e` | `3B7DFDCE494E` |  |
| 160 | `results/_v5_b16_idx23_blindrate_verify_2026_09_29.md` | 19,755 | `8c45f5bec3dc` | `430588419975` |  |
| 161 | `results/_v5_b16_mq11_case_2026_09_29.md` | 16,723 | `712964f3eb17` | `85F92C8D18D1` |  |
| 162 | `results/_v5_b17_three_caliber_fixation_2026_09_29.md` | 19,709 | `aa13f2945e85` | `D47B5E067C1C` |  |
| 163 | `results/_v5_b18_coding_caliber_2026_09_29.md` | 14,304 | `df968dda4772` | `04F6890DC4A8` |  |
| 164 | `results/_v5_b18_single_count_fixation_2026_09_29.md` | 13,608 | `fd8c3dbd4794` | `006E316BFE4C` |  |
| 165 | `results/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md` | 18,514 | `a2989b1b5b26` | `BF0874456A58` |  |
| 166 | `results/_v5_spec_prereq_reference_archive_2026_10_18.md` | 20,423 | `ddafeb14dccc` | `E54BC00E9787` |  |
| 167 | `results/_verify_worker_c.py` | 1,155 | `e454eb83619f` | `CC578C46B332` |  |
| 168 | `results/verify_ge02_acceptance.py` | 20,212 | `85cfbc2a5a06` | `6B9B17F6D0FC` |  |
| 169 | `results/verify_ge02_acceptance_results.json` | 1,836 | `ac3e45e5b0a6` | `F5DA17E62B07` |  |
| 170 | `tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak` | 23,893 | `c3f0ec7ba9fb` | `7D8D6A30DD8C` |  |
| 171 | `tmp_movedout_2026_10_01/process_scripts/volcengine_补测_worker_A_2026_09_10.py` | 16,252 | `92ee1bf107cd` | `20B8A2F54AD9` |  |
| 172 | `verifier/volcengine_补测_worker_A_2026_09_10.py` | 16,252 | `92ee1bf107cd` | `20B8A2F54AD9` |  |

# R-A-4 ｜ 序 2-b 删 70 件（裁四 · 先拉回存证后删 · 逐条独立 commit · ⛔ 0 整目录删）

- 删前去重对账（R-SSC-3 面）：70 件 ＝ 拉回 172 之 `results/_archive_2026_09_20/` 子集；与 v0.4 §9 之 302 件次面之交 ＝ 该前缀下前轮已删 5 件（0 重删）；遗留面 413 与本面 0 交（前缀面 ⇔ 根层面互斥）
- 前置成就：70/70 拉回存证在位（R-A-3 表「属70件删面」列）⇒ 删 **70/70**（failed=0）｜删后终验：70 路径于终态全树 **0** 命中（期望 0）

| # | 仓内路径 | 删前 blob SHA-12 | bytes | commit-12 |
|--:|---|---|--:|---|
| 1 | `results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | `bcf317b88d6e` | 10,586 | `312330ce3cef` |
| 2 | `results/_archive_2026_09_20/LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md` | `d39d91ecd84c` | 7,855 | `96b60eee06b5` |
| 3 | `results/_archive_2026_09_20/TRAE_CODE_FIX_LIST_2026_09_18.md` | `96c744af6776` | 9,343 | `cec2795228fe` |
| 4 | `results/_archive_2026_09_20/TRAE_DAILY_AUDIT_LETTER_2026_09_18.md` | `f6c1e86b1542` | 11,575 | `5b233e1e021d` |
| 5 | `results/_archive_2026_09_20/TRAE_FIX_RECEIPT_2026_09_18.md` | `eb23f9346728` | 4,784 | `4dc75e4985e5` |
| 6 | `results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | `d10a14ba179a` | 454,307 | `523906bcc978` |
| 7 | `results/_archive_2026_09_20/_cpath_sim_run_2026_09_10.log` | `10e844e84dad` | 1,508 | `5059fdc35f57` |
| 8 | `results/_archive_2026_09_20/_d05_main_runner_20260918.log` | `345608fea302` | 9,232 | `c86acc2b77a3` |
| 9 | `results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | `a76a2658a272` | 18,611 | `1d0053c171ff` |
| 10 | `results/_archive_2026_09_20/_p_l_v3_phase1_finalize.log` | `1a098d388a6e` | 1,184 | `c69c6a06dfcf` |
| 11 | `results/_archive_2026_09_20/_p_l_v3_phase1_runner.log` | `e731a8ade38f` | 8,202 | `70c66720dcb3` |
| 12 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner.log` | `ead67cc76e5d` | 2,370 | `ec35695b5479` |
| 13 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_171640.log` | `2b5128e0a098` | 1,516 | `f02992c7aff2` |
| 14 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172440_gpt56sol.log` | `1a98af38bdef` | 865 | `d7f57b8826b8` |
| 15 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_172928_gpt56sol.log` | `d0fe6629bee3` | 955 | `969160f75293` |
| 16 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_173159_gpt56sol.log` | `c83c63c766f4` | 2,765 | `25477700de0f` |
| 17 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_174011_claude_sonnet5.log` | `60f85dbfabc3` | 2,687 | `0afb03163ed4` |
| 18 | `results/_archive_2026_09_20/_p_l_v3_phase2_closedsource_runner_v2_20260917_175003_gemini_37flash.log` | `0952adb63097` | 2,342 | `649a2a016b24` |
| 19 | `results/_archive_2026_09_20/_p_l_v3_phase2_finalize.log` | `e506d97fb9fc` | 2,712 | `5fa9f4bc4bf6` |
| 20 | `results/_archive_2026_09_20/_p_l_v3_phase2_finalize_20260917_142748.log` | `19e035b669d0` | 1,224 | `788e863f7a23` |
| 21 | `results/_archive_2026_09_20/_p_l_v3_phase2_glm53.log` | `f85eddf2fc03` | 2,542 | `19b5e68bdf47` |
| 22 | `results/_archive_2026_09_20/_p_l_v3_phase2_glm53_only_20260917_142011.log` | `bb5e79511c7e` | 1,140 | `f5cccc1e5b6a` |
| 23 | `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.err` | `2c10446f7d93` | 530 | `07fcc5bfeab7` |
| 24 | `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding.log` | `3055f18b8f1d` | 564 | `c8bd724f0d3d` |
| 25 | `results/_archive_2026_09_20/_p_l_v3_phase2_or_embedding_v3_2026_09_17.console.log` | `5ee1916ddb81` | 10,102 | `bd544cc14400` |
| 26 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe.log` | `9678a036b1b7` | 3,100 | `aa5faa73531c` |
| 27 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_agent.log` | `54c4f808cd15` | 6,760 | `8072a5f0003d` |
| 28 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb.log` | `5267d1048a6e` | 2,046 | `e435edef34da` |
| 29 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_emb_proxy_v2.log` | `16a34c3ae004` | 17,632 | `d5fa8fabe79b` |
| 30 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_ext.log` | `4cb29bc0fce1` | 4,992 | `3fb1611197c8` |
| 31 | `results/_archive_2026_09_20/_p_l_v3_phase2_probe_gpt4o.log` | `2e5b3c200544` | 3,462 | `8d91cca38b73` |
| 32 | `results/_archive_2026_09_20/_p_l_v3_phase2_runner.log` | `7e9ff72e8505` | 3,416 | `30c65db0ca1b` |
| 33 | `results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console.log` | `303659550a1b` | 6,134 | `4d6c75dc083c` |
| 34 | `results/_archive_2026_09_20/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console2.log` | `d42b879bc3de` | 2,925 | `6bdbf2659fc3` |
| 35 | `results/_archive_2026_09_20/_probe_teamo_via_proxy.log` | `7d540c86567e` | 4,526 | `8a6c53a5bf32` |
| 36 | `results/_archive_2026_09_20/_sanity_openai_more.log` | `ac1d0b5bd3c2` | 1,444 | `61910bdb5dc4` |
| 37 | `results/_archive_2026_09_20/_sanity_teamo_three.log` | `8912d907b188` | 2,168 | `957fa6e06c9b` |
| 38 | `results/_archive_2026_09_20/_test_3bb_vary.log` | `63bad8ab3356` | 11,522 | `3b1d572c143e` |
| 39 | `results/_archive_2026_09_20/_v2_stage1_60cells.console.log` | `f401a22768be` | 17,158 | `4d960834acca` |
| 40 | `results/_archive_2026_09_20/_v2_stage3_f3_strip.console.log` | `639a46fbc44c` | 2,440 | `21a0aab1c3e4` |
| 41 | `results/_archive_2026_09_20/_v3x_6way_finalize.log` | `e8e3eecbbe55` | 618 | `895ec3356d5e` |
| 42 | `results/_archive_2026_09_20/_v3x_6way_run.log` | `cb8f0635c4e8` | 8,952 | `007bde15eeed` |
| 43 | `results/_archive_2026_09_20/_v3x_6way_stage3_minimal.log` | `2f5edcac6a91` | 1,678 | `c349c30ddbdc` |
| 44 | `results/_archive_2026_09_20/_v3x_6way_stage3_recovery.log` | `713e5f75c289` | 2,242 | `25e8ac8397a0` |
| 45 | `results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log` | `8b06e5d3f43d` | 17,456 | `ce1709f782f5` |
| 46 | `results/_archive_2026_09_20/_v41_flash_rag_baseline_run.log.bak` | `1b86970816da` | 6,106 | `c33297a48024` |
| 47 | `results/_archive_2026_09_20/_volc_22cap_emb.log` | `42c9d2e4a9ea` | 9,068 | `a29cb5320b61` |
| 48 | `results/_archive_2026_09_20/_worker_openrouter_rag_run.log` | `e56dd631a770` | 6,476 | `8f2ef3b675a8` |
| 49 | `results/_archive_2026_09_20/deposon_d_fix2_metric_verify_9m60c_2026_09_15.log` | `e71aecfebe91` | 24,634 | `14045422bf33` |
| 50 | `results/_archive_2026_09_20/deposon_deepseek_v41_flash_30cells_2026_09_10.log` | `4de1a9c448f7` | 6,514 | `610b29d1b70e` |
| 51 | `results/_archive_2026_09_20/deposon_dpath_cross_modal_2026_09_10.log` | `f33a29327e11` | 8,885 | `d957e3ad8f87` |
| 52 | `results/_archive_2026_09_20/deposon_dpath_cross_modal_runner_2026_09_10.stdout.log` | `97e2aa66522f` | 17,772 | `2fa2efeb632c` |
| 53 | `results/_archive_2026_09_20/deposon_feshbach_rag_30cells_2026_09_10.log` | `c6aca7403cf8` | 6,887 | `c8a5e2dc0420` |
| 54 | `results/_archive_2026_09_20/deposon_v2_phase1_60cells_2026_09_11.log` | `3d3a6b8994db` | 8,578 | `84f001609fea` |
| 55 | `results/_archive_2026_09_20/deposon_v2_phase2_f2_2026_09_11.log` | `41eba7b8f98b` | 1,272 | `ce5d71f516e9` |
| 56 | `results/_archive_2026_09_20/deposon_v2_phase3_f3_2026_09_11.log` | `0467038c016f` | 1,247 | `2f4ce8ab83ad` |
| 57 | `results/_archive_2026_09_20/deposon_v2_phase4_f4_2026_09_11.log` | `be3d138384e2` | 1,064 | `bd228857a766` |
| 58 | `results/_archive_2026_09_20/deposon_v2_phase5_f5_2026_09_11.log` | `8cfd8dd5620c` | 1,092 | `bf69166bf41a` |
| 59 | `results/_archive_2026_09_20/deposon_v41_flash_60cells_v2_2026_09_10.log` | `ebdc60a61dbc` | 12,470 | `5d36d3e9c355` |
| 60 | `results/_archive_2026_09_20/deposon_volcengine_minimax_m3_30cells_2026_09_10.log` | `f03cb6416a01` | 3,444 | `acf07a1f78bc` |
| 61 | `results/_archive_2026_09_20/deposon_volcengine_seed_code_30cells_2026_09_10.log` | `672e14623f28` | 7,342 | `0dce3cf4404b` |
| 62 | `results/_archive_2026_09_20/deposon_volcengine_worker_b_2026_09_10.log` | `853dd2881e5e` | 3,326 | `b543d8d0c511` |
| 63 | `results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.log` | `c3b87ceaad9d` | 5,869 | `ff8d328137da` |
| 64 | `results/_archive_2026_09_20/deposon_volcengine_worker_c_2026_09_10.run.log` | `5a6919ccc9b6` | 12,070 | `9e78a44efb0c` |
| 65 | `results/_archive_2026_09_20/fiction_that_feeds_back.tex` | `68da7b05797b` | 93,324 | `0bb38962013f` |
| 66 | `results/_archive_2026_09_20/gpt6_30cells_run.log` | `cd78df661d8b` | 4,220 | `077e58890235` |
| 67 | `results/_archive_2026_09_20/review_content_A1_dsv4pro.md` | `7375dbcc2a8b` | 20,082 | `5bc66a934787` |
| 68 | `results/_archive_2026_09_20/review_tech_B1_grok46.md` | `5c05888226a8` | 18,923 | `a0236cf328cd` |
| 69 | `results/_archive_2026_09_20/review_tech_B2_qwen3max.md` | `3c2dd5f7c0ab` | 8,098 | `abe5825a3324` |
| 70 | `results/_archive_2026_09_20/volcengine_glm_latest_30cells_v2_run_2026_09_10.log` | `b39406b8614e` | 4,091 | `7de9c35d6a33` |

# R-A-5 ｜ 序 2-c 传（裁三·裁七·裁十一 · 脱敏后传 · P0 四门全过）

**P0 面（R-SSC-6）**：

- **P0-1**：上传集 ＝ 序 0 live HEAD 树重核后之裁定清单（172/209/514 逐条在位性与 sha 重核 0 漂移），⛔ 非本地整树
- **P0-2**（文件名面之特定词族扫描 · 判准回读新委托 §2.1-6 之在册面）：590 件路径扫描 **0 命中**（`KD-SSC-06` 之 9 件已依裁十一剔除 · 144 拉回副本 0 传）
- **P0-3**（内容面）：590 件脱敏副本全量过门禁同语义扫描族（CN 六词子串／三词大小写不敏感／一词词界锚定）＋ 密钥族正则（带长度锚）⇒ **590/590 全零**；构建即扫、0 残留件入推送面；扫描规则自身 0 入扫描集
- **P0-4**（PDF 面）：本批 590 件中 PDF **0 件**（唯一 2 件 PDF 属被剔除之 9 件面）⇒ 文本层复算登记**无标的**，如实登记

**脱敏面**：方案 `065a36b4b067`（已裁·追认·生效）之规则族 R-01～R-11 机械执行；590 件中 **264 件**触发替换、**326 件** 0 触发；触发计数逐件入下表「规则」列；原件 0 改动（构建只读 · 副本落执行侧工作区 `_r7_desensitized/`）

**blob 去重之如实登记**：590 件之脱敏内容对应 **589 个唯一 blob**——`corpus/v20_caption_surface/_inspect_captions.py` 与 `results/_archive_2026_09_24/_inspect_captions.py` 脱敏后逐字节同一（`6c3e6486863a`），Git blob 天然共体，两路径各自在位、内容同一

**本地移动靶之如实登记（KD-SSC-13）**：`results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md` 本地版于对比件快照后漂移（表载 `2d40510c92b5` → 现版 `1ace80bfb19c`）；依打包裁「以本地为权威」之旨以**现版**脱敏覆盖，两指纹并录于此

**逐件表**（覆前／覆后 sha-1-12 ＋ bytes ＋ 行数 ＋ commit ＋ 规则触发）：

| # | 面 | 仓内路径（远端＝`_repo_mirror/<rel>`） | 覆前 sha-12 ／ bytes ／ 行 | 覆后 sha-12 ／ bytes ／ 行 | commit-12 | 规则 |
|--:|:-:|---|---|---|---|---|
| 1 | S3-23 | `audits_dataset_health.json` | **新增** | `4a33af111f0f` ／ 7,398 ／ 237 | `768e43af3ced` | — |
| 2 | S3-23 | `docs/DATASET_HEALTH_v2.md` | **新增** | `db57fcae77b1` ／ 4,892 ／ 61 | `768e43af3ced` | — |
| 3 | S3-23 | `results/_v4_pi_cot_v2_dataset.json` | **新增** | `fc0a48202902` ／ 12,672 ／ 60 | `768e43af3ced` | — |
| 4 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | **新增** | `f91692efd347` ／ 4,103 ／ 83 | `768e43af3ced` | — |
| 5 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | **新增** | `11548fa9c347` ／ 6,132 ／ 102 | `768e43af3ced` | — |
| 6 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | **新增** | `4de634e0ad8e` ／ 7,566 ／ 108 | `768e43af3ced` | — |
| 7 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | **新增** | `bbabf547f6df` ／ 6,666 ／ 113 | `768e43af3ced` | — |
| 8 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | **新增** | `2c84943121fb` ／ 7,668 ／ 113 | `768e43af3ced` | — |
| 9 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | **新增** | `65ad8aacb53d` ／ 10,257 ／ 143 | `768e43af3ced` | — |
| 10 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | **新增** | `f59b97601d73` ／ 11,589 ／ 173 | `768e43af3ced` | — |
| 11 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | **新增** | `95fff0a09d87` ／ 14,722 ／ 178 | `768e43af3ced` | — |
| 12 | S3-23 | `results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | **新增** | `5cb3a1cbb369` ／ 19,615 ／ 185 | `768e43af3ced` | — |
| 13 | S3-23 | `results/_v4_pi_cot_v3_dataset.json` | **新增** | `8c0300e90060` ／ 16,025 ／ 247 | `768e43af3ced` | — |
| 14 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | **新增** | `fc04fe9be042` ／ 20,194 ／ 205 | `768e43af3ced` | — |
| 15 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | **新增** | `570275c1731a` ／ 18,714 ／ 335 | `768e43af3ced` | — |
| 16 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | **新增** | `1f1904c9d786` ／ 16,587 ／ 154 | `768e43af3ced` | — |
| 17 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | **新增** | `b60f81e8f595` ／ 19,214 ／ 221 | `768e43af3ced` | — |
| 18 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | **新增** | `d0b2e5bfd237` ／ 27,009 ／ 256 | `768e43af3ced` | — |
| 19 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | **新增** | `945e2a9c7605` ／ 58,581 ／ 850 | `768e43af3ced` | — |
| 20 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | **新增** | `66362bf125e7` ／ 374,072 ／ 4766 | `768e43af3ced` | — |
| 21 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | **新增** | `0e2301038e1c` ／ 46,909 ／ 495 | `768e43af3ced` | — |
| 22 | S3-23 | `results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | **新增** | `07f910b7397a` ／ 17,252 ／ 197 | `768e43af3ced` | — |
| 23 | S3-23 | `results/_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | **新增** | `4004f2c5eec3` ／ 12,975 ／ 285 | `768e43af3ced` | — |
| 24 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v100.md` | **新增** | `8b1af9b69ec5` ／ 40,128 ／ 162 | `9ec782b2b1b5` | — |
| 25 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v101.md` | **新增** | `72cb4f23a08d` ／ 46,191 ／ 185 | `9ec782b2b1b5` | — |
| 26 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v102.md` | **新增** | `29f020a5b3ba` ／ 57,912 ／ 223 | `9ec782b2b1b5` | — |
| 27 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v103.md` | **新增** | `ee58dbb80767` ／ 68,524 ／ 217 | `9ec782b2b1b5` | — |
| 28 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v90.md` | **新增** | `74dbe52d8af4` ／ 35,256 ／ 259 | `9ec782b2b1b5` | — |
| 29 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v91.md` | **新增** | `6bfa06d24bfa` ／ 35,197 ／ 308 | `9ec782b2b1b5` | — |
| 30 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v92.md` | **新增** | `2f06040fc008` ／ 46,595 ／ 353 | `9ec782b2b1b5` | — |
| 31 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v93.md` | **新增** | `4c101994598d` ／ 51,967 ／ 349 | `9ec782b2b1b5` | — |
| 32 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v94.md` | **新增** | `99cd30477496` ／ 32,030 ／ 168 | `9ec782b2b1b5` | — |
| 33 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v95.md` | **新增** | `f5f5e2fff2c9` ／ 28,959 ／ 140 | `9ec782b2b1b5` | — |
| 34 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v96.md` | **新增** | `ca1dc65c4db0` ／ 49,227 ／ 212 | `9ec782b2b1b5` | — |
| 35 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v97.md` | **新增** | `15ea982a00c6` ／ 33,410 ／ 152 | `9ec782b2b1b5` | — |
| 36 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v98.md` | **新增** | `df5d21a96752` ／ 46,786 ／ 193 | `9ec782b2b1b5` | — |
| 37 | C-56 | `pi_rulings/_pi_card_answers_register_2026_10_18_v99.md` | **新增** | `9d01cad624a6` ／ 50,107 ／ 202 | `9ec782b2b1b5` | — |
| 38 | C-56 | `results/_achievements_inventory_full_2026_10_18.md` | **新增** | `df6bdbfa8e99` ／ 805,466 ／ 7103 | `9ec782b2b1b5` | R-04×19 |
| 39 | C-56 | `results/_archive_2026_09_20/_d05_sanity_3backbone_20260918_100110.json` | **新增** | `79a41fc22dab` ／ 2,292 ／ 65 | `9ec782b2b1b5` | — |
| 40 | C-56 | `results/_clearance_materials_register_2026_10_08.md` | **新增** | `85786983a421` ／ 45,385 ／ 305 | `9ec782b2b1b5` | R-01×1·R-02×3·R-04×14·R-05×3·R-07×6·R-08×3 |
| 41 | C-56 | `results/_closure_sweep_r2_2026_10_18.md` | **新增** | `3b5fc95ac9c6` ／ 121,848 ／ 358 | `9ec782b2b1b5` | — |
| 42 | C-56 | `results/_commission_v04_approval_rulings_effect_2026_10_18.md` | **新增** | `4f5528d06f7c` ／ 67,299 ／ 406 | `9ec782b2b1b5` | — |
| 43 | C-56 | `results/_commission_v04_ghost_reference_erratum_2026_10_18.md` | **新增** | `dfd7e44221fa` ／ 37,518 ／ 379 | `9ec782b2b1b5` | — |
| 44 | C-56 | `results/_consolidated_pending_rulings_scroll_2026_10_18.md` | **新增** | `e0c7b6a7f831` ／ 104,340 ／ 380 | `9ec782b2b1b5` | — |
| 45 | C-56 | `results/_deemphasis_verification_register_2026_10_08.md` | **新增** | `c23b829945c1` ／ 27,611 ／ 304 | `9ec782b2b1b5` | R-01×4·R-02×8·R-03×3·R-04×23·R-05×5·R-06×3·R-07×7·R-08×6·R-09×3·R-10×3 |
| 46 | C-56 | `results/_eta_preexp_wait_and_leveling_effect_2026_10_18.md` | **新增** | `dada54d9aab6` ／ 32,594 ／ 300 | `9ec782b2b1b5` | — |
| 47 | C-56 | `results/_five_zero_recheck_evidence_2026_10_18.md` | **新增** | `7031bd2a1995` ／ 37,035 ／ 253 | `9ec782b2b1b5` | — |
| 48 | C-56 | `results/_freeze_final_replay_2026_10_18.md` | **新增** | `be5a801851df` ／ 31,254 ／ 264 | `9ec782b2b1b5` | — |
| 49 | C-56 | `results/_h_face_external_evidence_eval_2026_10_18.md` | **新增** | `e9cb29bee98d` ／ 35,016 ／ 273 | `9ec782b2b1b5` | — |
| 50 | C-56 | `results/_h_face_freeze_ruling_effect_2026_10_18.md` | **新增** | `9e0657fe2908` ／ 28,089 ／ 158 | `9ec782b2b1b5` | R-04×1 |
| 51 | C-56 | `results/_historical_ forgetting_recheck_2026_10_18.md` | **新增** | `ea229f6c7bd6` ／ 34,941 ／ 286 | `9ec782b2b1b5` | — |
| 52 | C-56 | `results/_kickoff_decisions_register_2026_10_08.md` | **新增** | `2f79df3622e7` ／ 16,412 ／ 121 | `9ec782b2b1b5` | R-02×6 |
| 53 | C-56 | `results/_kimi_postexec_receipt_verification_2026_10_18.md` | **新增** | `1922769aa303` ／ 21,678 ／ 150 | `9ec782b2b1b5` | — |
| 54 | C-56 | `results/_kimi_preexec_final_rulings_effect_2026_10_18.md` | **新增** | `e304d53d4747` ／ 42,226 ／ 219 | `9ec782b2b1b5` | — |
| 55 | C-56 | `results/_kimi_receipt_authority_rulings_effect_2026_10_18.md` | **新增** | `0b431bc0f9de` ／ 62,860 ／ 231 | `9ec782b2b1b5` | — |
| 56 | C-56 | `results/_md_a_field_composition_draft_2026_10_18.md` | **新增** | `966d6db93b67` ／ 58,572 ／ 302 | `9ec782b2b1b5` | — |
| 57 | C-56 | `results/_morning_brief_pending_rulings_2026_10_18.md` | **新增** | `6b33b016873f` ／ 37,227 ／ 345 | `9ec782b2b1b5` | — |
| 58 | C-56 | `results/_next_stage3_dir_optimization_ruling_2026_10_18.md` | **新增** | `f68393b6b384` ／ 11,599 ／ 161 | `9ec782b2b1b5` | — |
| 59 | C-56 | `results/_pending_residual_minimal_set_2026_10_18.md` | **新增** | `fd746ac78c08` ／ 53,502 ／ 345 | `9ec782b2b1b5` | — |
| 60 | C-56 | `results/_pending_rulings_triage_2026_10_18.md` | **新增** | `2a7c5eaefee4` ／ 63,300 ／ 428 | `9ec782b2b1b5` | — |
| 61 | C-56 | `results/_post_execution_report_kimi_2026_10_18.md` | **新增** | `2ec601aa97d3` ／ 7,251 ／ 80 | `9ec782b2b1b5` | — |
| 62 | C-56 | `results/_pre_execution_report_kimi_2026_10_18.md` | **新增** | `39bc47e46948` ／ 6,971 ／ 87 | `9ec782b2b1b5` | R-04×1 |
| 63 | C-56 | `results/_r2_sep_endogeneity_erratum_2026_10_18.md` | **新增** | `f09d9a231756` ／ 41,770 ／ 258 | `9ec782b2b1b5` | — |
| 64 | C-56 | `results/_remote_delete_face_pullback_register_2026_10_18.md` | **新增** | `1f31c749b9ff` ／ 82,690 ／ 353 | `9ec782b2b1b5` | — |
| 65 | C-56 | `results/_remote_residual_disposal_execution_order_2026_10_08.md` | **新增** | `9c1c4eb43443` ／ 36,752 ／ 429 | `9ec782b2b1b5` | R-01×4·R-02×3·R-04×20·R-05×11·R-07×7·R-08×14·R-09×1 |
| 66 | C-56 | `results/_reply_letter_approval_effect_2026_10_18.md` | **新增** | `f1f635588fbc` ／ 38,991 ／ 179 | `9ec782b2b1b5` | — |
| 67 | C-56 | `results/_ruled_unclosed_closure_verdict_2026_10_18.md` | **新增** | `a542d7bc793e` ／ 54,716 ／ 218 | `9ec782b2b1b5` | — |
| 68 | C-56 | `results/_scroll_wave1_four_rulings_effect_2026_10_18.md` | **新增** | `2382e51cbb4f` ／ 51,739 ／ 228 | `9ec782b2b1b5` | — |
| 69 | C-56 | `results/_scroll_wave2_four_rulings_effect_2026_10_18.md` | **新增** | `730f2037e8b8` ／ 51,949 ／ 248 | `9ec782b2b1b5` | — |
| 70 | C-56 | `results/_scroll_wave4_three_rulings_effect_2026_10_18.md` | **新增** | `eefabee5fde5` ／ 51,604 ／ 233 | `9ec782b2b1b5` | — |
| 71 | C-56 | `results/_scroll_wave5_four_rulings_effect_2026_10_18.md` | **新增** | `5cc9aba339be` ／ 71,453 ／ 328 | `9ec782b2b1b5` | — |
| 72 | C-56 | `results/_stage3_close_and_cmp2_rulings_effect_2026_10_18.md` | **新增** | `1d22d0187f46` ／ 54,315 ／ 369 | `9ec782b2b1b5` | — |
| 73 | C-56 | `results/_stage5_preparation_design_2026_10_18.md` | **新增** | `73ed0d6e543e` ／ 43,856 ／ 247 | `9ec782b2b1b5` | — |
| 74 | C-56 | `results/_thirdparty_16_overwrite_necessity_2026_10_18.md` | **新增** | `635767454632` ／ 14,122 ／ 160 | `9ec782b2b1b5` | — |
| 75 | C-56 | `results/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md` | **新增** | `b34a12eb5d90` ／ 43,428 ／ 209 | `9ec782b2b1b5` | — |
| 76 | C-56 | `results/_u10_fail_h0_verdict_2026_10_18.md` | **新增** | `91cbe31fc56a` ／ 59,918 ／ 418 | `9ec782b2b1b5` | — |
| 77 | C-56 | `results/_u10_s3_denominator_rulings_effect_2026_10_18.md` | **新增** | `58b444fc324b` ／ 79,234 ／ 394 | `9ec782b2b1b5` | — |
| 78 | C-56 | `results/_unique_supplement_letter_approval_effect_2026_10_18.md` | **新增** | `00bc7551df03` ／ 51,240 ／ 238 | `9ec782b2b1b5` | R-04×1 |
| 79 | C-56 | `results/_v34_experiment_gap_plan_2026_10_08.md` | **新增** | `99c3cfd5e178` ／ 36,070 ／ 287 | `9ec782b2b1b5` | R-02×1 |
| 80 | OVW-511 | `.gitignore` | `4fc0d746af9d` ／ 105 ／ 10 | `4fc0d746af9d` ／ 105 ／ 10 | `739a7daf533b` | — |
| 81 | OVW-511 | `.trae/audit/compare_versions.py` | `75600d25d0a0` ／ 7,990 ／ 179 | `75600d25d0a0` ／ 7,990 ／ 179 | `739a7daf533b` | R-01×2·R-05×1·R-07×1·R-08×1 |
| 82 | OVW-511 | `.trae/scripts/_arxiv_renumber.py` | `2292a3044e55` ／ 16,523 ／ 369 | `941186a880eb` ／ 16,531 ／ 369 | `739a7daf533b` | — |
| 83 | OVW-511 | `.trae/scripts/_md_to_tex.py` | `cb94bef12c8c` ／ 48,647 ／ 911 | `5bde2e624c81` ／ 48,655 ／ 911 | `739a7daf533b` | R-01×2·R-08×2 |
| 84 | OVW-511 | `.trae/scripts/_verify_tex.py` | `6bcf5ed11826` ／ 18,256 ／ 366 | `8293e59b0a41` ／ 18,264 ／ 366 | `739a7daf533b` | R-01×2 |
| 85 | OVW-511 | `README_V4_2026_09_29.md` | `c5e19f40a90b` ／ 58,646 ／ 415 | `714dc17f8f5c` ／ 58,634 ／ 415 | `739a7daf533b` | R-02×3·R-04×1·R-11×1 |
| 86 | OVW-511 | `_movedout_manifest_2026_09_21.json` | `8a16a7461a32` ／ 291,567 ／ 5447 | `5f649d030753` ／ 291,575 ／ 5447 | `739a7daf533b` | R-04×12 |
| 87 | OVW-511 | `_p_l_v3_phase1_finalize_2026_09_17.py` | `f8110f41c607` ／ 19,224 ／ 337 | `e88eb617d975` ／ 19,232 ／ 337 | `739a7daf533b` | R-02×1·R-04×1 |
| 88 | OVW-511 | `_p_l_v3_phase1_runner_2026_09_17.py` | `3a5af3e5448e` ／ 35,425 ／ 762 | `81148156f14a` ／ 35,431 ／ 762 | `739a7daf533b` | R-02×1·R-04×1 |
| 89 | OVW-511 | `_p_l_v3_phase2_finalize_2026_09_17.py` | `56b4aa16d2e2` ／ 19,901 ／ 372 | `5b4f2f24fcb0` ／ 19,907 ／ 372 | `739a7daf533b` | R-02×1·R-04×1 |
| 90 | OVW-511 | `corpus/v20_caption_surface/_inspect_captions.py` | `207a74970678` ／ 583 ／ 17 | `6c3e6486863a` ／ 591 ／ 17 | `739a7daf533b` | — |
| 91 | OVW-511 | `deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md` | `4ac42cc84dac` ／ 12,689 ／ 249 | `4ac42cc84dac` ／ 12,689 ／ 249 | `739a7daf533b` | R-02×4·R-04×3 |
| 92 | OVW-511 | `deposon_team/_designs/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md` | `dffe99f8d9fa` ／ 12,866 ／ 281 | `a8c512443b0b` ／ 12,858 ／ 281 | `739a7daf533b` | R-02×2·R-04×3 |
| 93 | OVW-511 | `deposon_team/_designs/EXTERNAL_AGENT_PROMPTS_2026_09_16.md` | `2f1b9580912e` ／ 12,338 ／ 247 | `2f1b9580912e` ／ 12,338 ／ 247 | `739a7daf533b` | R-02×1·R-04×4 |
| 94 | OVW-511 | `deposon_team/_designs/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md` | `775144c54f1b` ／ 8,740 ／ 208 | `775144c54f1b` ／ 8,740 ／ 208 | `739a7daf533b` | R-02×4·R-04×5 |
| 95 | OVW-511 | `deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md` | `da84d81aa976` ／ 12,908 ／ 198 | `da84d81aa976` ／ 12,908 ／ 198 | `739a7daf533b` | R-02×5·R-04×5 |
| 96 | OVW-511 | `deposon_team/_designs/V3X_KIMI_7_DIRECTIONS_FULL_ACCEPT_2026_09_16.md` | `a26392eb0e96` ／ 10,952 ／ 198 | `a26392eb0e96` ／ 10,952 ／ 198 | `739a7daf533b` | R-02×3·R-04×2 |
| 97 | OVW-511 | `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md` | `f61a9452e2c8` ／ 6,805 ／ 158 | `f61a9452e2c8` ／ 6,805 ／ 158 | `739a7daf533b` | R-02×1·R-04×1 |
| 98 | OVW-511 | `deposon_team/_designs/V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md` | `025c158f7feb` ／ 11,256 ／ 200 | `025c158f7feb` ／ 11,256 ／ 200 | `739a7daf533b` | R-02×4·R-04×4 |
| 99 | OVW-511 | `deposon_team/_designs/v3x_dispatch_log_2026_09_16.md` | `ee4eddfad35f` ／ 8,439 ／ 147 | `9839bc1ac2fd` ／ 8,437 ／ 147 | `739a7daf533b` | R-02×1·R-04×2 |
| 100 | OVW-511 | `deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_16.py` | `c901b65dd9e7` ／ 6,239 ／ 172 | `abcca18feded` ／ 6,247 ／ 172 | `739a7daf533b` | R-02×1·R-04×1 |
| 101 | OVW-511 | `deposon_team/plugins/_pg_v01_compute.py` | `edb4685a740b` ／ 20,931 ／ 510 | `c70f833f9014` ／ 20,939 ／ 510 | `739a7daf533b` | R-02×2·R-04×4 |
| 102 | OVW-511 | `deposon_team/plugins/_tdf_s1_2026_10_12.py` | `2df029e81991` ／ 5,848 ／ 112 | `18aa51927654` ／ 5,856 ／ 112 | `739a7daf533b` | — |
| 103 | OVW-511 | `deposon_team/plugins/_tdf_s1b_2026_10_12.py` | `5908015bb22a` ／ 8,056 ／ 165 | `a5c5396ad589` ／ 8,064 ／ 165 | `739a7daf533b` | — |
| 104 | OVW-511 | `deposon_team/plugins/_tdf_s1c_2026_10_12.py` | `e88528dbc37e` ／ 7,477 ／ 146 | `62823388e682` ／ 7,485 ／ 146 | `739a7daf533b` | — |
| 105 | OVW-511 | `deposon_team/plugins/_tdf_s2_apply_2026_10_12.py` | `6778a10ac0e3` ／ 10,891 ／ 210 | `139831d429c6` ／ 10,899 ／ 210 | `739a7daf533b` | — |
| 106 | OVW-511 | `deposon_team/plugins/_tdf_s3_jumps_2026_10_12.py` | `a0c386e92374` ／ 668 ／ 13 | `fb8e290bfd7c` ／ 676 ／ 13 | `739a7daf533b` | — |
| 107 | OVW-511 | `deposon_team/plugins/_tdf_s3b_2026_10_12.py` | `84394f9e5ee6` ／ 1,221 ／ 27 | `72b9df5b6a46` ／ 1,229 ／ 27 | `739a7daf533b` | — |
| 108 | OVW-511 | `deposon_team/plugins/_tdf_s4_final_2026_10_12.py` | `ecfa39768f34` ／ 2,687 ／ 54 | `e13bb36e5115` ／ 2,695 ／ 54 | `739a7daf533b` | — |
| 109 | OVW-511 | `deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py` | `f31efedb713a` ／ 30,627 ／ 569 | `c42d45b19fde` ／ 30,676 ／ 569 | `739a7daf533b` | R-02×1 |
| 110 | OVW-511 | `deposon_team/plugins/_v3x_experiments_runner_2026_09_16.py` | `ab1a25ac9008` ／ 18,553 ／ 473 | `7638772a1e75` ／ 18,561 ／ 473 | `739a7daf533b` | R-02×1·R-04×1 |
| 111 | OVW-511 | `deposon_team/plugins/boss_pa_1_rbr_rm.py` | `2e563e9fd165` ／ 17,705 ／ 404 | `ed9562894231` ／ 17,745 ／ 404 | `739a7daf533b` | R-04×1 |
| 112 | OVW-511 | `deposon_team/plugins/boss_pa_2_potential_game.py` | `48e3ca1d1ccf` ／ 10,380 ／ 248 | `5d3950a54d65` ／ 10,412 ／ 248 | `739a7daf533b` | R-04×1 |
| 113 | OVW-511 | `deposon_team/plugins/boss_pa_3_replicator_dynamics.py` | `3cb86ea403ad` ／ 12,870 ／ 307 | `fc74b59e22d5` ／ 12,902 ／ 307 | `739a7daf533b` | R-04×1 |
| 114 | OVW-511 | `deposon_team/plugins/boss_pg_1_riemannian_degenerate.py` | `f4dbf7158e55` ／ 6,012 ／ 125 | `f4dbf7158e55` ／ 6,012 ／ 125 | `739a7daf533b` | R-02×3·R-04×2 |
| 115 | OVW-511 | `deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py` | `e0a794481e41` ／ 5,297 ／ 115 | `e0a794481e41` ／ 5,297 ／ 115 | `739a7daf533b` | R-02×2·R-04×2 |
| 116 | OVW-511 | `deposon_team/plugins/boss_pg_3_geodesic_violation.py` | `497d2a008357` ／ 5,529 ／ 117 | `497d2a008357` ／ 5,529 ／ 117 | `739a7daf533b` | R-02×2·R-04×2 |
| 117 | OVW-511 | `deposon_team/plugins/fix_boss_naming_2026_09_16.py` | `9f1e923dd24a` ／ 17,475 ／ 322 | `233b8d8364ce` ／ 17,483 ／ 322 | `739a7daf533b` | R-02×1 |
| 118 | OVW-511 | `deposon_team/plugins/git_commit_msg_2026_09_18.txt` | `f32b043fd6e4` ／ 3,241 ／ 61 | `f32b043fd6e4` ／ 3,241 ／ 61 | `739a7daf533b` | R-02×3·R-04×3 |
| 119 | OVW-511 | `deposon_team/plugins/runner_pa_d1_d3.py` | `414aeeaaf803` ／ 27,680 ／ 557 | `d39d9023f615` ／ 27,736 ／ 557 | `739a7daf533b` | R-02×4·R-04×4 |
| 120 | OVW-511 | `deposon_team/plugins/skill_a_p_a_60cells.py` | `3565dd4edb1c` ／ 9,037 ／ 210 | `65ba10553f14` ／ 9,082 ／ 210 | `739a7daf533b` | R-04×2 |
| 121 | OVW-511 | `deposon_team/plugins/skill_b_p_c_alpha_beta.py` | `a675bae218b4` ／ 8,668 ／ 214 | `4d56cf50ee47` ／ 8,701 ／ 214 | `739a7daf533b` | R-04×1 |
| 122 | OVW-511 | `deposon_team/plugins/skill_c_p_e_3modality.py` | `d46e9dd7ab4f` ／ 8,872 ／ 213 | `0f64eff3d553` ／ 8,917 ／ 213 | `739a7daf533b` | R-04×1 |
| 123 | OVW-511 | `deposon_team/plugins/skill_d_p_f_observer.py` | `471b37678096` ／ 15,889 ／ 339 | `8277ff019e1f` ／ 15,935 ／ 339 | `739a7daf533b` | R-02×1·R-04×2 |
| 124 | OVW-511 | `docs/THINKING_V3_GT_CONTRIB_2026.md` | `69fa556aa47a` ／ 19,614 ／ 132 | `69fa556aa47a` ／ 19,614 ／ 132 | `739a7daf533b` | R-01×13·R-05×1·R-06×1·R-09×1 |
| 125 | OVW-511 | `docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | `5ccceefbaa16` ／ 11,859 ／ 173 | `60f5932e4b0b` ／ 11,843 ／ 173 | `739a7daf533b` | R-02×2 |
| 126 | OVW-511 | `docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `d1462f7a0baf` ／ 11,091 ／ 224 | `d1462f7a0baf` ／ 11,091 ／ 224 | `739a7daf533b` | R-02×2·R-04×2 |
| 127 | OVW-511 | `docs/V3X/BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | `515954f5c09f` ／ 10,974 ／ 179 | `515954f5c09f` ／ 10,974 ／ 179 | `739a7daf533b` | R-02×1 |
| 128 | OVW-511 | `docs/V3X/BPA_PILOT_2026_09_09_mavis.md` | `de51c39ddedc` ／ 6,868 ／ 93 | `de51c39ddedc` ／ 6,868 ／ 93 | `739a7daf533b` | R-02×1 |
| 129 | OVW-511 | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | `c7f2a4404206` ／ 9,914 ／ 162 | `c7f2a4404206` ／ 9,914 ／ 162 | `739a7daf533b` | R-02×12·R-03×7·R-04×4 |
| 130 | OVW-511 | `docs/V3X/D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `27523eab8450` ／ 21,764 ／ 433 | `27523eab8450` ／ 21,764 ／ 433 | `739a7daf533b` | R-02×1·R-04×2 |
| 131 | OVW-511 | `docs/V3X/D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | `90e26e14f4fd` ／ 5,942 ／ 149 | `90e26e14f4fd` ／ 5,942 ／ 149 | `739a7daf533b` | R-02×2·R-04×2 |
| 132 | OVW-511 | `docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | `e16d2a5f8ecd` ／ 6,479 ／ 99 | `e16d2a5f8ecd` ／ 6,479 ／ 99 | `739a7daf533b` | R-02×4·R-04×2 |
| 133 | OVW-511 | `docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | `b891bb4004c6` ／ 10,734 ／ 239 | `b891bb4004c6` ／ 10,734 ／ 239 | `739a7daf533b` | R-02×8·R-04×5 |
| 134 | OVW-511 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | `d9b81cfc1571` ／ 22,408 ／ 403 | `5b88cdfd0ea8` ／ 22,448 ／ 403 | `739a7daf533b` | R-02×1·R-04×1 |
| 135 | OVW-511 | `docs/V3X/DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | `909fabce2d8b` ／ 17,813 ／ 324 | `909fabce2d8b` ／ 17,813 ／ 324 | `739a7daf533b` | R-02×2·R-04×1 |
| 136 | OVW-511 | `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `3baf552bab87` ／ 7,366 ／ 97 | `3baf552bab87` ／ 7,366 ／ 97 | `739a7daf533b` | R-02×3·R-04×1 |
| 137 | OVW-511 | `docs/V3X/KT_A1_SPEC_V0.1.md` | `db69ddfd15d8` ／ 29,670 ／ 461 | `2f906c2424cd` ／ 29,668 ／ 461 | `739a7daf533b` | R-01×2·R-02×15·R-04×5·R-06×1·R-09×1 |
| 138 | OVW-511 | `docs/V3X/KT_B1_SPEC_V0.1.md` | `2536948d64ee` ／ 39,385 ／ 638 | `2057eb16bc03` ／ 39,383 ／ 638 | `739a7daf533b` | R-01×3·R-02×25·R-03×2·R-04×19·R-06×1·R-09×1 |
| 139 | OVW-511 | `docs/V3X/KT_C1_SPEC_V0.1.md` | `53fa9d2e5398` ／ 31,317 ／ 514 | `3d3a40ce9676` ／ 31,315 ／ 514 | `739a7daf533b` | R-01×2·R-02×7·R-03×2·R-04×7·R-06×1·R-09×1 |
| 140 | OVW-511 | `docs/V3X/KT_D0_EVIDENCE_CARD.md` | `f78b5f420d57` ／ 6,362 ／ 112 | `f78b5f420d57` ／ 6,362 ／ 112 | `739a7daf533b` | R-02×2 |
| 141 | OVW-511 | `docs/V3X/KT_D0_SPEC_V0.1.md` | `dcb9123bb035` ／ 20,983 ／ 338 | `529f58459cf9` ／ 20,981 ／ 338 | `739a7daf533b` | R-01×2·R-02×4·R-03×3·R-04×2·R-06×1·R-09×1 |
| 142 | OVW-511 | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | `816d56eeb283` ／ 19,777 ／ 349 | `816d56eeb283` ／ 19,777 ／ 349 | `739a7daf533b` | R-02×4·R-04×5 |
| 143 | OVW-511 | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `85f4334d29be` ／ 10,371 ／ 171 | `85f4334d29be` ／ 10,371 ／ 171 | `739a7daf533b` | R-02×4·R-04×2 |
| 144 | OVW-511 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `cf1f3d2f858c` ／ 15,549 ／ 177 | `cf1f3d2f858c` ／ 15,549 ／ 177 | `739a7daf533b` | R-02×19·R-04×8 |
| 145 | OVW-511 | `docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` | `995354ff82be` ／ 13,431 ／ 240 | `995354ff82be` ／ 13,431 ／ 240 | `739a7daf533b` | R-02×1·R-04×4 |
| 146 | OVW-511 | `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `bc57b2d877a6` ／ 6,325 ／ 146 | `bc57b2d877a6` ／ 6,325 ／ 146 | `739a7daf533b` | R-02×5·R-04×2 |
| 147 | OVW-511 | `docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md` | `0e3f19a48a69` ／ 13,135 ／ 261 | `0e3f19a48a69` ／ 13,135 ／ 261 | `739a7daf533b` | R-02×4·R-04×5 |
| 148 | OVW-511 | `docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | `3077f29a3205` ／ 16,900 ／ 334 | `b05ff8152eee` ／ 16,904 ／ 334 | `739a7daf533b` | R-02×6·R-04×2 |
| 149 | OVW-511 | `docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` | `629dd923bdab` ／ 16,013 ／ 252 | `2214e735c7d6` ／ 16,011 ／ 252 | `739a7daf533b` | R-02×4·R-04×5 |
| 150 | OVW-511 | `docs/V3X/P_F_D1_REPORT_2026_09_15.md` | `2440a613ed72` ／ 12,616 ／ 200 | `2440a613ed72` ／ 12,616 ／ 200 | `739a7daf533b` | R-02×1·R-04×2 |
| 151 | OVW-511 | `docs/V3X/P_F_IMPLEMENTATION_2026_09_11.md` | `d1f45c8fb34f` ／ 23,027 ／ 371 | `d1f45c8fb34f` ／ 23,027 ／ 371 | `739a7daf533b` | R-01×2·R-02×6·R-04×1·R-06×1·R-09×1 |
| 152 | OVW-511 | `docs/V3X/P_F_RESEARCH_2026_09_09.md` | `01059346371f` ／ 17,647 ／ 260 | `01059346371f` ／ 17,647 ／ 260 | `739a7daf533b` | R-01×2·R-02×4·R-06×1·R-09×1 |
| 153 | OVW-511 | `docs/V3X/P_F_SPEC_V0.md` | `44d0481664e4` ／ 19,910 ／ 415 | `5a0196ba7313` ／ 19,908 ／ 415 | `739a7daf533b` | R-01×2·R-02×17·R-04×4·R-06×1·R-09×1 |
| 154 | OVW-511 | `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | `40ff107b5181` ／ 12,523 ／ 250 | `40ff107b5181` ／ 12,523 ／ 250 | `739a7daf533b` | R-02×3·R-04×5 |
| 155 | OVW-511 | `docs/V3X/P_G_V01_REPORT_2026_09_15.md` | `a1b52ba63522` ／ 15,501 ／ 297 | `a1b52ba63522` ／ 15,501 ／ 297 | `739a7daf533b` | R-02×3·R-04×5 |
| 156 | OVW-511 | `docs/V3X/QUICK_KILL_6_DIRECTIONS.md` | `5302dfea87da` ／ 15,107 ／ 151 | `5302dfea87da` ／ 15,107 ／ 151 | `739a7daf533b` | R-02×4·R-04×3 |
| 157 | OVW-511 | `docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | `b8c68387046b` ／ 34,605 ／ 431 | `fb2016c6f150` ／ 34,677 ／ 431 | `739a7daf533b` | R-02×5·R-04×5 |
| 158 | OVW-511 | `docs/V3X/REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | `52335388369a` ／ 20,690 ／ 258 | `8d6efeeae783` ／ 20,706 ／ 258 | `739a7daf533b` | R-02×2 |
| 159 | OVW-511 | `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` | `9dd3cea98340` ／ 13,299 ／ 287 | `9dd3cea98340` ／ 13,299 ／ 287 | `739a7daf533b` | R-02×6·R-04×2 |
| 160 | OVW-511 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_16.md` | `c4e7a025ab3b` ／ 9,281 ／ 97 | `c4e7a025ab3b` ／ 9,281 ／ 97 | `739a7daf533b` | R-02×3·R-04×1 |
| 161 | OVW-511 | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | `8da06df0e058` ／ 857,249 ／ 5650 | `75434cb47c34` ／ 857,591 ／ 5650 | `739a7daf533b` | R-01×2·R-04×13 |
| 162 | OVW-511 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `0debb6baba97` ／ 8,554 ／ 178 | `0debb6baba97` ／ 8,554 ／ 178 | `739a7daf533b` | R-02×5·R-04×4 |
| 163 | OVW-511 | `docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md` | `dc9183d82725` ／ 24,814 ／ 521 | `dc9183d82725` ／ 24,814 ／ 521 | `739a7daf533b` | R-02×7·R-03×3·R-04×1 |
| 164 | OVW-511 | `docs/V3X/V3X_D6_PAPER_zh.md` | `78577e0de271` ／ 19,764 ／ 460 | `ed599f6c12fc` ／ 19,762 ／ 460 | `739a7daf533b` | R-02×7·R-03×7·R-04×2 |
| 165 | OVW-511 | `docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | `9b5bbb811a91` ／ 38,553 ／ 620 | `9b5bbb811a91` ／ 38,553 ／ 620 | `739a7daf533b` | R-02×2 |
| 166 | OVW-511 | `docs/V3X/V3X_DAILY_KILL_V2_PLAN.md` | `04b5307e1392` ／ 15,375 ／ 340 | `04b5307e1392` ／ 15,375 ／ 340 | `739a7daf533b` | R-02×8·R-03×8 |
| 167 | OVW-511 | `docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `dac61c7effde` ／ 22,455 ／ 508 | `dac61c7effde` ／ 22,455 ／ 508 | `739a7daf533b` | R-02×4·R-04×6 |
| 168 | OVW-511 | `docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | `3f4c25025250` ／ 12,928 ／ 319 | `3f4c25025250` ／ 12,928 ／ 319 | `739a7daf533b` | R-02×3·R-04×4 |
| 169 | OVW-511 | `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | `0da3bc43cd7c` ／ 7,348 ／ 105 | `0da3bc43cd7c` ／ 7,348 ／ 105 | `739a7daf533b` | R-02×1 |
| 170 | OVW-511 | `docs/V3X_COLLAB_DIRECTIONS.md` | `8764166830d0` ／ 16,396 ／ 104 | `8764166830d0` ／ 16,396 ／ 104 | `739a7daf533b` | R-01×1·R-02×3·R-06×1·R-09×1 |
| 171 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v46.md` | `62910e2b2dff` ／ 64,396 ／ 325 | `62910e2b2dff` ／ 64,396 ／ 325 | `739a7daf533b` | R-02×4·R-04×4 |
| 172 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v54.md` | `6396645627f1` ／ 72,381 ／ 408 | `6396645627f1` ／ 72,381 ／ 408 | `739a7daf533b` | R-04×1 |
| 173 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v72.md` | `fcc9e3a4ac13` ／ 33,680 ／ 255 | `fcc9e3a4ac13` ／ 33,680 ／ 255 | `739a7daf533b` | R-11×1 |
| 174 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v80.md` | `6188dbda5e77` ／ 33,779 ／ 226 | `6188dbda5e77` ／ 33,779 ／ 226 | `739a7daf533b` | R-04×1 |
| 175 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v81.md` | `c68062107ee4` ／ 51,671 ／ 303 | `c68062107ee4` ／ 51,671 ／ 303 | `739a7daf533b` | R-04×2 |
| 176 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v82.md` | `b43ea3881756` ／ 47,751 ／ 265 | `b43ea3881756` ／ 47,751 ／ 265 | `739a7daf533b` | R-04×1 |
| 177 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v83.md` | `1b916be2cd26` ／ 49,998 ／ 295 | `1b916be2cd26` ／ 49,998 ／ 295 | `739a7daf533b` | R-04×1 |
| 178 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v85.md` | `75fb0b94f171` ／ 51,364 ／ 314 | `75fb0b94f171` ／ 51,364 ／ 314 | `739a7daf533b` | R-04×1 |
| 179 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v86.md` | `8f44312eeae7` ／ 39,041 ／ 295 | `8f44312eeae7` ／ 39,041 ／ 295 | `739a7daf533b` | R-04×1 |
| 180 | OVW-511 | `pi_rulings/_pi_card_answers_register_2026_10_17_v87.md` | `0e617b1f4efc` ／ 56,901 ／ 350 | `0e617b1f4efc` ／ 56,901 ／ 350 | `739a7daf533b` | R-04×1 |
| 181 | OVW-511 | `results/_a02_excluded_items_idx_collection_2026_10_10.md` | `4a89109b9893` ／ 39,505 ／ 318 | `c114ca7ac083` ／ 39,565 ／ 318 | `739a7daf533b` | — |
| 182 | OVW-511 | `results/_achievements_inventory_full_2026_10_09.md` | `acb25540ac22` ／ 372,346 ／ 3459 | `acb25540ac22` ／ 372,346 ／ 3459 | `739a7daf533b` | R-04×14 |
| 183 | OVW-511 | `results/_alt_delib_pkg3_two_judgments_2026_10_10.md` | `8c694436358f` ／ 38,034 ／ 333 | `343ba0d8fc9d` ／ 38,032 ／ 333 | `739a7daf533b` | — |
| 184 | OVW-511 | `results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md` | `1b17763e4fc7` ／ 11,495 ／ 188 | `1b17763e4fc7` ／ 11,495 ／ 188 | `739a7daf533b` | R-02×6·R-04×3 |
| 185 | OVW-511 | `results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | `484df38a6e46` ／ 20,892 ／ 328 | `6d826839f41f` ／ 20,952 ／ 328 | `739a7daf533b` | R-02×2·R-04×3 |
| 186 | OVW-511 | `results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md` | `004e79c610af` ／ 7,863 ／ 78 | `1f54a9822ce1` ／ 7,857 ／ 78 | `739a7daf533b` | R-04×1 |
| 187 | OVW-511 | `results/_archive_2026_09_18/_trae_paper_8ch_双审_20260917_200000.md` | `4f92d3020764` ／ 4,042 ／ 59 | `4f92d3020764` ／ 4,042 ／ 59 | `739a7daf533b` | R-04×1 |
| 188 | OVW-511 | `results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | `e6599255e59d` ／ 13,295 ／ 263 | `66de2e44ee7c` ／ 13,306 ／ 263 | `739a7daf533b` | R-02×3·R-04×4 |
| 189 | OVW-511 | `results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | `37c28c9d515a` ／ 22,820 ／ 357 | `22f3c6798d2b` ／ 22,856 ／ 357 | `739a7daf533b` | R-02×16·R-04×8 |
| 190 | OVW-511 | `results/_archive_2026_09_20/LETTER_TO_TRAE_REVIEW_2026_09_16.md` | `5dc3c0faffed` ／ 12,671 ／ 298 | `340ee68b89a3` ／ 12,676 ／ 298 | `739a7daf533b` | R-02×1·R-04×2 |
| 191 | OVW-511 | `results/_archive_2026_09_20/_archive_manifest_2026_09_20.json` | `f86ca7abd474` ／ 35,690 ／ 975 | `f86ca7abd474` ／ 35,690 ／ 975 | `739a7daf533b` | R-04×4 |
| 192 | OVW-511 | `results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | `938102d0e310` ／ 6,433 ／ 167 | `8e6d0f12d997` ／ 6,441 ／ 167 | `739a7daf533b` | R-04×4 |
| 193 | OVW-511 | `results/_archive_2026_09_20/_coze_paper_v1_双审报告_2026_09_17.md` | `dcad9d2da5bd` ／ 85,627 ／ 494 | `570aa07611f4` ／ 85,645 ／ 494 | `739a7daf533b` | R-02×18 |
| 194 | OVW-511 | `results/_archive_2026_09_20/_d05_sanity_3backbone_2026_09_18.py` | `72854074e603` ／ 5,452 ／ 122 | `06c54e651f5d` ／ 5,458 ／ 122 | `739a7daf533b` | — |
| 195 | OVW-511 | `results/_archive_2026_09_20/_ftfb_pass2_results_limitations_audit_2026_09_17.md` | `a4489af68f91` ／ 11,390 ／ 97 | `87c967818299` ／ 11,392 ／ 97 | `739a7daf533b` | R-04×1 |
| 196 | OVW-511 | `results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | `22c18e6d3604` ／ 12,813 ／ 208 | `9bff09e32332` ／ 12,838 ／ 208 | `739a7daf533b` | R-02×9·R-04×8 |
| 197 | OVW-511 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md` | `e5615dfdf907` ／ 10,307 ／ 210 | `8bb204dc864e` ／ 10,312 ／ 210 | `739a7daf533b` | R-02×1·R-04×2 |
| 198 | OVW-511 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_v2_2026_09_17.md` | `f0ee0664b7e3` ／ 13,967 ／ 245 | `82ff04b16b92` ／ 13,972 ／ 245 | `739a7daf533b` | R-02×1·R-04×2 |
| 199 | OVW-511 | `results/_archive_2026_09_20/_letter_to_kimi_push_v3_委托_2026_09_17.md` | `691137aa0627` ／ 13,592 ／ 219 | `30d89421bb45` ／ 13,600 ／ 219 | `739a7daf533b` | R-02×2·R-04×3 |
| 200 | OVW-511 | `results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | `0dd53df5dccb` ／ 22,591 ／ 342 | `679eb741de41` ／ 22,611 ／ 342 | `739a7daf533b` | R-04×10 |
| 201 | OVW-511 | `results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | `35362d1a6671` ／ 10,702 ／ 203 | `5bb21c0cdee1` ／ 10,722 ／ 203 | `739a7daf533b` | R-02×4·R-04×8 |
| 202 | OVW-511 | `results/_archive_2026_09_20/ftfb_pass1_background_methodology_audit_2026_09_17.md` | `3df594818649` ／ 8,257 ／ 75 | `477a5cc75f25` ／ 8,259 ／ 75 | `739a7daf533b` | R-04×1 |
| 203 | OVW-511 | `results/_archive_2026_09_24/_inspect_captions.py` | `207a74970678` ／ 583 ／ 17 | `6c3e6486863a` ／ 591 ／ 17 | `739a7daf533b` | — |
| 204 | OVW-511 | `results/_archive_2026_09_24/_verify_worker_c.py` | `a22aa0b2ddea` ／ 1,147 ／ 21 | `e454eb83619f` ／ 1,155 ／ 21 | `739a7daf533b` | — |
| 205 | OVW-511 | `results/_archive_2026_09_24/_volc_22cap_emb.py` | `c7f9aceeaa08` ／ 11,091 ／ 262 | `987fd959ce49` ／ 11,105 ／ 262 | `739a7daf533b` | — |
| 206 | OVW-511 | `results/_archive_2026_09_24/_worker_openrouter_rag_run.py` | `5332c33c3466` ／ 24,107 ／ 517 | `6ce92f706bdd` ／ 24,113 ／ 517 | `739a7daf533b` | — |
| 207 | OVW-511 | `results/_archive_ledger_rectification_register_2026_10_09.md` | `31d356a8ff63` ／ 20,926 ／ 190 | `6d9bc4c95e8e` ／ 20,933 ／ 190 | `739a7daf533b` | — |
| 208 | OVW-511 | `results/_archive_manifest_deposon_sub_2026_09_23.json` | `60238391952b` ／ 52,156 ／ 1827 | `3b667b0acf62` ／ 52,165 ／ 1827 | `739a7daf533b` | R-04×6 |
| 209 | OVW-511 | `results/_archive_manifest_non_upload_2026_09_23.json` | `4bfc21e8edfc` ／ 148,670 ／ 5887 | `a096694fbe49` ／ 148,692 ／ 5887 | `739a7daf533b` | R-04×1 |
| 210 | OVW-511 | `results/_archive_manifest_non_upload_v2_2026_09_28.json` | `6dd94f28c8d1` ／ 236,631 ／ 9540 | `cdf86876eece` ／ 236,653 ／ 9540 | `739a7daf533b` | R-04×1 |
| 211 | OVW-511 | `results/_archive_manifest_non_upload_v3_2026_09_28.json` | `0f34b6d8b8e6` ／ 204,236 ／ 8682 | `c45247cf27b8` ／ 204,258 ／ 8682 | `739a7daf533b` | R-04×1 |
| 212 | OVW-511 | `results/_axis1_three_recomputations_2026_10_11.md` | `8a85318ae33e` ／ 29,898 ／ 260 | `1d0857087ccf` ／ 29,938 ／ 260 | `739a7daf533b` | — |
| 213 | OVW-511 | `results/_b01_new_key_classification_2026_10_10.md` | `f479531ce574` ／ 38,621 ／ 384 | `85a23e2ac195` ／ 38,669 ／ 384 | `739a7daf533b` | — |
| 214 | OVW-511 | `results/_b01_new_key_residue_judgment_2026_10_10.md` | `cbd82437ff52` ／ 41,924 ／ 329 | `a5fbdfb9265b` ／ 41,984 ／ 329 | `739a7daf533b` | — |
| 215 | OVW-511 | `results/_b01_p_counting_recompute_2026_10_10.md` | `941424bc6d71` ／ 22,064 ／ 218 | `37ab9642da7b` ／ 22,104 ／ 218 | `739a7daf533b` | — |
| 216 | OVW-511 | `results/_b01_recompute_authorization_supplement_2026_10_11.md` | `82b0af3f4730` ／ 18,414 ／ 160 | `fe1fc73afb48` ／ 18,454 ／ 160 | `739a7daf533b` | — |
| 217 | OVW-511 | `results/_b01_recompute_sec4_2_erratum_2026_10_10.md` | `e63e29fe22a0` ／ 16,401 ／ 157 | `30cb0056be0a` ／ 16,441 ／ 157 | `739a7daf533b` | — |
| 218 | OVW-511 | `results/_b14_audit_f2f3_closure_register_2026_10_11.md` | `dc21e594ae6a` ／ 29,580 ／ 293 | `330cf31449c0` ／ 29,620 ／ 293 | `739a7daf533b` | — |
| 219 | OVW-511 | `results/_b14_vk_evidence_audit_2026_10_10.md` | `7da95eb67e06` ／ 33,546 ／ 327 | `580177f1eb35` ／ 33,586 ／ 327 | `739a7daf533b` | — |
| 220 | OVW-511 | `results/_batch8_deliberation_judgment_2026_10_14.md` | `3305435b7d67` ／ 49,028 ／ 367 | `3305435b7d67` ／ 49,028 ／ 367 | `739a7daf533b` | R-02×4 |
| 221 | OVW-511 | `results/_batch9_deliberation_judgment_2026_10_14.md` | `37a49fbe40b0` ／ 36,629 ／ 343 | `37a49fbe40b0` ／ 36,629 ／ 343 | `739a7daf533b` | R-02×1·R-04×1 |
| 222 | OVW-511 | `results/_c2_criterion_third_tier_draft_2026_10_11.md` | `c17c103993f3` ／ 26,673 ／ 231 | `c0d7213a09fa` ／ 26,713 ／ 231 | `739a7daf533b` | — |
| 223 | OVW-511 | `results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | `ec5eb05066a9` ／ 31,567 ／ 226 | `d05d668a6c50` ／ 31,607 ／ 226 | `739a7daf533b` | — |
| 224 | OVW-511 | `results/_c4_math_corrections_downstream_erratum_2026_10_10.md` | `b5004c027d08` ／ 28,826 ／ 228 | `44ed4e1dbd49` ／ 28,886 ／ 228 | `739a7daf533b` | — |
| 225 | OVW-511 | `results/_c4_theory_source_caliber_correction_2026_09_30.md` | `8b7c48eea3da` ／ 25,138 ／ 238 | `8b7c48eea3da` ／ 25,138 ／ 238 | `739a7daf533b` | R-02×25·R-04×8 |
| 226 | OVW-511 | `results/_c4_unblock_reply_independent_review_2026_10_10.md` | `ef0bb966d450` ／ 27,360 ／ 231 | `25829e1b7260` ／ 27,364 ／ 231 | `739a7daf533b` | — |
| 227 | OVW-511 | `results/_c8_c2_disposition_register_2026_10_11.md` | `a57424c19d1d` ／ 30,916 ／ 220 | `774e2e98ab1f` ／ 30,956 ／ 220 | `739a7daf533b` | — |
| 228 | OVW-511 | `results/_c_component4_d2d3_gap_judgment_2026_10_11.md` | `1631ae2d6777` ／ 27,470 ／ 195 | `3c8a0039b3c4` ／ 27,490 ／ 195 | `739a7daf533b` | — |
| 229 | OVW-511 | `results/_c_component4_three_items_judgment_2026_10_11.md` | `d523d9bea24e` ／ 41,540 ／ 310 | `1e8427ebf11c` ／ 41,580 ／ 310 | `739a7daf533b` | — |
| 230 | OVW-511 | `results/_charlie_delivery_register_2026_10_08.md` | `91d92fd7a88b` ／ 10,683 ／ 161 | `df5a43c97f7b` ／ 10,733 ／ 161 | `739a7daf533b` | — |
| 231 | OVW-511 | `results/_chd_construction_domain_declaration_draft_2026_10_10.md` | `437f828e6dbd` ／ 34,908 ／ 298 | `a73d123433be` ／ 34,948 ／ 298 | `739a7daf533b` | — |
| 232 | OVW-511 | `results/_cleanup_round_2026_10_08.md` | `2feaa54a9800` ／ 33,152 ／ 301 | `84d19c144ab1` ／ 33,179 ／ 301 | `739a7daf533b` | — |
| 233 | OVW-511 | `results/_clearance_evening_round_register_2026_09_29.md` | `c3634de6f3fd` ／ 18,209 ／ 207 | `c3634de6f3fd` ／ 18,209 ／ 207 | `739a7daf533b` | R-02×2 |
| 234 | OVW-511 | `results/_clearance_round_1_register_2026_10_08.md` | `00a941c68be1` ／ 13,828 ／ 151 | `c12334453b58` ／ 13,826 ／ 151 | `739a7daf533b` | — |
| 235 | OVW-511 | `results/_clue_side_dual_and_glm_commission_open_register_2026_10_12.md` | `3e6459931d3f` ／ 14,499 ／ 146 | `3e6459931d3f` ／ 14,499 ／ 146 | `739a7daf533b` | R-01×1·R-02×1·R-03×1·R-04×1·R-05×1·R-06×1·R-07×1·R-08×1·R-09×1·R-10×1 |
| 236 | OVW-511 | `results/_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | `e7a1b16d5559` ／ 22,899 ／ 200 | `9e8ac3f39e98` ／ 22,895 ／ 200 | `739a7daf533b` | — |
| 237 | OVW-511 | `results/_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | `45fe997ff1e4` ／ 24,162 ／ 222 | `e221b31c229a` ／ 24,240 ／ 222 | `739a7daf533b` | — |
| 238 | OVW-511 | `results/_codex_c4_values_reply_intake_register_2026_10_10.md` | `5c8994056166` ／ 12,920 ／ 146 | `281a81f02a88` ／ 12,926 ／ 146 | `739a7daf533b` | — |
| 239 | OVW-511 | `results/_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | `a9235f93834e` ／ 27,058 ／ 264 | `b2bca9e0cc97` ／ 27,100 ／ 264 | `739a7daf533b` | — |
| 240 | OVW-511 | `results/_collision_baseline_update_and_disposition_2026_10_17.md` | `47f13ee7d3ba` ／ 26,219 ／ 205 | `47f13ee7d3ba` ／ 26,219 ／ 205 | `739a7daf533b` | R-02×3·R-03×2·R-04×3 |
| 241 | OVW-511 | `results/_commission_closeout_erratum_and_supplement_2026_10_11.md` | `6812ceb67f0a` ／ 12,427 ／ 107 | `3d38e496a803` ／ 12,447 ／ 107 | `739a7daf533b` | — |
| 242 | OVW-511 | `results/_coze_paper_v1_draft_2026_09_17.md` | `56568828a7bc` ／ 29,511 ／ 373 | `56568828a7bc` ／ 29,511 ／ 373 | `739a7daf533b` | R-01×1·R-02×2·R-04×2·R-05×1·R-09×1 |
| 243 | OVW-511 | `results/_d1_backfill_intake_verdict_2026_10_01.md`（组A） | `ecd9f5463bcb` ／ 42,115 ／ 390 | `f533096eecba` ／ 42,115 ／ 390 | `739a7daf533b` | — |
| 244 | OVW-511 | `results/_d8_boundary_revision_register_2026_09_30.md` | `5a33f2c079c6` ／ 32,408 ／ 319 | `5a33f2c079c6` ／ 32,408 ／ 319 | `739a7daf533b` | R-04×1 |
| 245 | OVW-511 | `results/_d8_dup_overlap_disposal_2026_09_30.md` | `c4ed04fd18fa` ／ 32,352 ／ 454 | `c4ed04fd18fa` ／ 32,352 ／ 454 | `739a7daf533b` | R-04×1 |
| 246 | OVW-511 | `results/_d8_supplement_open_questions_2026_09_30.md` | `0da60b9a1de6` ／ 24,835 ／ 303 | `0da60b9a1de6` ／ 24,835 ／ 303 | `739a7daf533b` | R-04×1 |
| 247 | OVW-511 | `results/_e2_glm2_distill_side_receipt_register_2026_10_09.md` | `3889af913d4c` ／ 11,338 ／ 159 | `4a8e99afdf6d` ／ 11,336 ／ 159 | `739a7daf533b` | — |
| 248 | OVW-511 | `results/_e4_lineage_conflict_correction_2026_10_11.md` | `57bde656f762` ／ 30,472 ／ 276 | `d08f1625732a` ／ 30,510 ／ 276 | `739a7daf533b` | — |
| 249 | OVW-511 | `results/_e6_j5_semantics_conflict_judgment_2026_10_10.md` | `584717acd90e` ／ 27,674 ／ 223 | `90692d4100f3` ／ 27,682 ／ 223 | `739a7daf533b` | — |
| 250 | OVW-511 | `results/_e6_j5_semantics_erratum_note_2026_10_10.md` | `935b16bc9d48` ／ 21,158 ／ 188 | `23265fc6acf4` ／ 21,166 ／ 188 | `739a7daf533b` | — |
| 251 | OVW-511 | `results/_e6_n_distinct_judge_types_recompute_2026_10_10.md` | `141f9a6f7450` ／ 26,296 ／ 245 | `2724e195ef58` ／ 26,304 ／ 245 | `739a7daf533b` | — |
| 252 | OVW-511 | `results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | `8ef45406f66d` ／ 46,243 ／ 379 | `467ace4389f7` ／ 46,261 ／ 379 | `739a7daf533b` | — |
| 253 | OVW-511 | `results/_ea_audit_batch_vk_2026_10_09.md` | `cb3c79a9b561` ／ 19,571 ／ 252 | `a7cba69019ce` ／ 19,611 ／ 252 | `739a7daf533b` | — |
| 254 | OVW-511 | `results/_eps_ls_semantics_judgment_2026_10_11.md` | `6cf929fa6f49` ／ 31,371 ／ 218 | `94f2a70ee4d5` ／ 31,391 ／ 218 | `739a7daf533b` | — |
| 255 | OVW-511 | `results/_executor_prereg_docstring_correction_2026_10_11.md` | `8211ed74f0de` ／ 27,681 ／ 222 | `cad9573c7130` ／ 27,721 ／ 222 | `739a7daf533b` | — |
| 256 | OVW-511 | `results/_executor_prereg_vs_impl_equivalence_2026_10_11.md` | `6567a3e316d1` ／ 19,988 ／ 197 | `c4e270d0b423` ／ 20,028 ／ 197 | `739a7daf533b` | — |
| 257 | OVW-511 | `results/_exp05_missing_true_disposition_judgment_2026_10_10.md` | `1ab497ffcf5e` ／ 25,568 ／ 192 | `1ab497ffcf5e` ／ 25,568 ／ 192 | `739a7daf533b` | R-02×3·R-04×2 |
| 258 | OVW-511 | `results/_exp05_negative_probe_rescan_2026_10_10.md` | `1a434dd57eb3` ／ 11,488 ／ 139 | `a2a4b2977fc9` ／ 11,566 ／ 139 | `739a7daf533b` | — |
| 259 | OVW-511 | `results/_exp08_s4_prompt_face_register_2026_10_10.md` | `262ac921c4b0` ／ 11,921 ／ 132 | `556bdc0a5670` ／ 11,929 ／ 132 | `739a7daf533b` | — |
| 260 | OVW-511 | `results/_external_letters_two_generation_values_note_2026_10_01.md` | `491f4338aeeb` ／ 10,989 ／ 137 | `491f4338aeeb` ／ 10,989 ／ 137 | `739a7daf533b` | R-04×5 |
| 261 | OVW-511 | `results/_f3_definition_deep_judgment_2026_10_11.md` | `0aa61e767615` ／ 42,311 ／ 324 | `173e51260711` ／ 42,351 ／ 324 | `739a7daf533b` | — |
| 262 | OVW-511 | `results/_f3_new_definition_draft_2026_10_11.md` | `43a3c50882d4` ／ 48,028 ／ 328 | `ab7a494cd3d7` ／ 48,068 ／ 328 | `739a7daf533b` | — |
| 263 | OVW-511 | `results/_f3f4_exit_drafts_2026_10_11.md` | `6b957b805b3f` ／ 50,367 ／ 387 | `f9f61cac47b0` ／ 50,427 ／ 387 | `739a7daf533b` | — |
| 264 | OVW-511 | `results/_f4_direction1_domain_effectivity_2026_10_11.md` | `a9a9122ec067` ／ 40,281 ／ 342 | `8bb3eeded041` ／ 40,301 ／ 342 | `739a7daf533b` | — |
| 265 | OVW-511 | `results/_f4_direction1_prereq_check_2026_10_11.md` | `4c4a1d6f60f5` ／ 38,624 ／ 336 | `516c6ea1c749` ／ 38,664 ／ 336 | `739a7daf533b` | — |
| 266 | OVW-511 | `results/_f4_direction1_seed_and_domain_draft_2026_10_11.md` | `3cbc03448af2` ／ 33,867 ／ 306 | `f9b7ad758bcb` ／ 33,887 ／ 306 | `739a7daf533b` | — |
| 267 | OVW-511 | `results/_five_items_effectivity_register_2026_10_11.md` | `5fd04575e161` ／ 43,312 ／ 341 | `2a498e82f9f4` ／ 43,332 ／ 341 | `739a7daf533b` | — |
| 268 | OVW-511 | `results/_five_pending_items_drafts_2026_10_11.md` | `ccd50440800d` ／ 55,082 ／ 453 | `48bc160b3265` ／ 55,102 ／ 453 | `739a7daf533b` | — |
| 269 | OVW-511 | `results/_five_stage_chain_design_reconstruction_2026_10_12.md` | `ee9375365231` ／ 12,617 ／ 109 | `b20b035930f9` ／ 12,635 ／ 109 | `739a7daf533b` | R-02×2·R-04×1 |
| 270 | OVW-511 | `results/_forgotten_recovery_register_2026_09_29.md` | `94e70b3cff4b` ／ 47,526 ／ 415 | `713f48eecb52` ／ 47,534 ／ 415 | `739a7daf533b` | R-02×9·R-04×2 |
| 271 | OVW-511 | `results/_forgotten_recovery_register_2026_10_08.md` | `d8ec52809c02` ／ 34,269 ／ 263 | `817ff913f1f7` ／ 34,287 ／ 263 | `739a7daf533b` | — |
| 272 | OVW-511 | `results/_four_items_execution_batch_2026_10_11.md` | `68089948c69a` ／ 31,497 ／ 266 | `9c27502abd00` ／ 31,515 ／ 266 | `739a7daf533b` | — |
| 273 | OVW-511 | `results/_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | `7a7627198619` ／ 32,846 ／ 313 | `2257524856ca` ／ 32,886 ／ 313 | `739a7daf533b` | — |
| 274 | OVW-511 | `results/_ftfb_order_judgment_2026_10_11.md` | `5a15b031e42e` ／ 45,871 ／ 277 | `0c943bbf536b` ／ 45,911 ／ 277 | `739a7daf533b` | — |
| 275 | OVW-511 | `results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md` | `43ef77ff0939` ／ 20,119 ／ 208 | `43ef77ff0939` ／ 20,119 ／ 208 | `739a7daf533b` | R-04×1 |
| 276 | OVW-511 | `results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md` | `8529c3f37779` ／ 28,565 ／ 278 | `299849cc9149` ／ 28,581 ／ 278 | `739a7daf533b` | R-04×1 |
| 277 | OVW-511 | `results/_g11_krj4_effectivity_register_2026_10_11.md` | `e2f46324fb78` ／ 39,830 ／ 318 | `5adc81e60162` ／ 39,870 ／ 318 | `739a7daf533b` | — |
| 278 | OVW-511 | `results/_g4_e3_definition_ruling_material_2026_10_09.md` | `afcd2edaa952` ／ 30,664 ／ 294 | `3638e15133ac` ／ 30,662 ／ 294 | `739a7daf533b` | — |
| 279 | OVW-511 | `results/_g4_reproduction_execution_register_2026_10_09.md` | `0fc49c17205b` ／ 20,420 ／ 226 | `3136a2fcae1c` ／ 20,414 ／ 226 | `739a7daf533b` | — |
| 280 | OVW-511 | `results/_g4_residual_probe_2026_10_08.md` | `ce3db50d3ec3` ／ 23,035 ／ 245 | `7c59058181e2` ／ 23,025 ／ 245 | `739a7daf533b` | — |
| 281 | OVW-511 | `results/_g5_ccp_execution_prereqs_2026_10_10.md` | `d4b16b573cd0` ／ 32,795 ／ 303 | `1293be908983` ／ 32,815 ／ 303 | `739a7daf533b` | — |
| 282 | OVW-511 | `results/_g5_ccp_p0_verification_2026_10_10.md` | `86018028a7fa` ／ 24,799 ／ 239 | `10eb0a5e9649` ／ 24,819 ／ 239 | `739a7daf533b` | — |
| 283 | OVW-511 | `results/_g5_ccp_seed_designation_revision_2026_10_10.md` | `92876b0b8dbd` ／ 20,959 ／ 216 | `b5b0f2cf3c37` ／ 20,979 ／ 216 | `739a7daf533b` | — |
| 284 | OVW-511 | `results/_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | `487e281745b8` ／ 45,167 ／ 300 | `685e17c9407d` ／ 45,207 ／ 300 | `739a7daf533b` | — |
| 285 | OVW-511 | `results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | `887969a1931c` ／ 49,031 ／ 313 | `e76d9b74029e` ／ 49,051 ／ 313 | `739a7daf533b` | — |
| 286 | OVW-511 | `results/_g5_rejudgment_construction_change_plan_2026_10_10.md` | `5142c8d4461a` ／ 56,984 ／ 343 | `cc626bcf5107` ／ 57,004 ／ 343 | `739a7daf533b` | — |
| 287 | OVW-511 | `results/_g5_rejudgment_construction_question_judgment_2026_10_10.md` | `f3448246455c` ／ 59,289 ／ 376 | `07747d9019e7` ／ 59,309 ／ 376 | `739a7daf533b` | — |
| 288 | OVW-511 | `results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | `0c646c01d983` ／ 33,936 ／ 255 | `d7bc5cb50edf` ／ 33,976 ／ 255 | `739a7daf533b` | — |
| 289 | OVW-511 | `results/_g9_read_b_effectivity_register_2026_10_11.md` | `68bb6bd96c10` ／ 29,621 ／ 195 | `8f52777de504` ／ 29,649 ／ 195 | `739a7daf533b` | — |
| 290 | OVW-511 | `results/_gate1_five_zero_recheck_glm_scope_2026_10_13.md` | `0819ac19f2e1` ／ 34,653 ／ 314 | `0819ac19f2e1` ／ 34,653 ／ 314 | `739a7daf533b` | R-04×3 |
| 291 | OVW-511 | `results/_gate_one_declared_adoption_register_2026_10_11.md` | `62966dc92fca` ／ 12,903 ／ 132 | `b2fbd94ef807` ／ 12,923 ／ 132 | `739a7daf533b` | — |
| 292 | OVW-511 | `results/_gate_one_pi_endorsement_register_2026_10_12.md` | `7ca62a5dc884` ／ 9,559 ／ 106 | `f93621af5205` ／ 9,579 ／ 106 | `739a7daf533b` | — |
| 293 | OVW-511 | `results/_gate_one_reopened_and_stage2_rejection_register_2026_10_12.md` | `bcdfdbb0940a` ／ 8,646 ／ 97 | `bcdfdbb0940a` ／ 8,646 ／ 97 | `739a7daf533b` | R-04×1 |
| 294 | OVW-511 | `results/_ge01_d1_theory_input_disposition_2026_10_14.md` | `df3149a13a5d` ／ 36,286 ／ 270 | `df3149a13a5d` ／ 36,286 ／ 270 | `739a7daf533b` | R-02×3·R-04×1 |
| 295 | OVW-511 | `results/_ge01_d1_theory_input_sourcing_design_2026_10_14.md` | `8427f472ce39` ／ 38,280 ／ 291 | `8427f472ce39` ／ 38,280 ／ 291 | `739a7daf533b` | R-02×12·R-04×5 |
| 296 | OVW-511 | `results/_ge01_spec_anchor_erratum_2026_10_14.md` | `f0c93a1f65c2` ／ 18,135 ／ 193 | `f0c93a1f65c2` ／ 18,135 ／ 193 | `739a7daf533b` | R-02×1·R-04×1 |
| 297 | OVW-511 | `results/_ge01_unblock_progress_2026_10_14.md` | `ed36772f3efe` ／ 25,319 ／ 201 | `ed36772f3efe` ／ 25,319 ／ 201 | `739a7daf533b` | R-02×1 |
| 298 | OVW-511 | `results/_github_suspect_rulings_effect_2026_10_17.md` | `a732da6d363a` ／ 51,656 ／ 396 | `a732da6d363a` ／ 51,656 ／ 396 | `739a7daf533b` | R-04×1 |
| 299 | OVW-511 | `results/_itemH_fingerprint_provenance_2026_10_12.md` | `d5f27db26e9a` ／ 22,764 ／ 271 | `d5f27db26e9a` ／ 22,764 ／ 271 | `739a7daf533b` | R-02×3 |
| 300 | OVW-511 | `results/_j2_identifier_coupling_judgment_2026_10_11.md` | `def2db2aea26` ／ 34,241 ／ 282 | `6bc5fde90a05` ／ 34,261 ／ 282 | `739a7daf533b` | — |
| 301 | OVW-511 | `results/_j2_kj4_disposition_register_2026_10_11.md` | `6ea8b41cad43` ／ 34,092 ／ 311 | `c903073be182` ／ 34,112 ／ 311 | `739a7daf533b` | — |
| 302 | OVW-511 | `results/_k_v3df_0_1_four_readings_2026_10_09.md` | `852ce8b50ec9` ／ 46,514 ／ 411 | `ce503683fb4a` ／ 46,522 ／ 411 | `739a7daf533b` | — |
| 303 | OVW-511 | `results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | `c4580a3b3b29` ／ 36,995 ／ 409 | `c4aa2b53e20f` ／ 37,003 ／ 409 | `739a7daf533b` | — |
| 304 | OVW-511 | `results/_kd1_preexp_contrast_2026_10_17.md` | `e15cac5d6ab4` ／ 27,153 ／ 304 | `e15cac5d6ab4` ／ 27,153 ／ 304 | `739a7daf533b` | R-02×1 |
| 305 | OVW-511 | `results/_kd_doc1_correction_adoption_register_2026_10_11.md` | `d15e442aa686` ／ 10,235 ／ 106 | `f8c1722d4d67` ／ 10,255 ／ 106 | `739a7daf533b` | — |
| 306 | OVW-511 | `results/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md` | `1507a17b2448` ／ 49,256 ／ 278 | `1507a17b2448` ／ 49,256 ／ 278 | `739a7daf533b` | R-02×1 |
| 307 | OVW-511 | `results/_kd_s3b1_verdict_2026_10_17.md` | `9172d0748ed3` ／ 45,862 ／ 384 | `9172d0748ed3` ／ 45,862 ／ 384 | `739a7daf533b` | R-02×4 |
| 308 | OVW-511 | `results/_kimi_push_v3_manifest_batch14_e5952130.json` | `2a1f389a4d99` ／ 1,063 ／ 40 | `2a1f389a4d99` ／ 1,063 ／ 40 | `739a7daf533b` | R-04×4 |
| 309 | OVW-511 | `results/_kimi_push_v3_manifest_batch5_34439e1e.json` | `ef0f17c3f2be` ／ 9,513 ／ 310 | `ef0f17c3f2be` ／ 9,513 ／ 310 | `739a7daf533b` | R-04×1 |
| 310 | OVW-511 | `results/_kimi_safe_batch_push_v2_full_2026_09_17.json` | `ca670157f6c9` ／ 47,000 ／ 634 | `7cec2a017c35` ／ 47,962 ／ 634 | `739a7daf533b` | R-04×4 |
| 311 | OVW-511 | `results/_kj1_abc_choice_judgment_2026_10_11.md` | `925a68307d20` ／ 42,043 ／ 281 | `69953e57b0fc` ／ 42,083 ／ 281 | `739a7daf533b` | — |
| 312 | OVW-511 | `results/_kj1_eps_ls_effectivity_register_2026_10_11.md` | `13c4094f2053` ／ 62,308 ／ 393 | `6c42ba3f285e` ／ 62,344 ／ 393 | `739a7daf533b` | — |
| 313 | OVW-511 | `results/_kj1_judgment_premise_correction_2026_10_11.md` | `8b6724812e08` ／ 35,012 ／ 311 | `a9664bdcccdd` ／ 35,050 ／ 311 | `739a7daf533b` | — |
| 314 | OVW-511 | `results/_kj1_sc1_premise_correction_2026_10_11.md` | `b38b11217838` ／ 31,046 ／ 266 | `b3c0d245c088` ／ 31,044 ／ 266 | `739a7daf533b` | — |
| 315 | OVW-511 | `results/_kj4_e4_unification_judgment_2026_10_11.md` | `2a19e1aaf1b8` ／ 36,799 ／ 281 | `796dab06c04e` ／ 36,839 ／ 281 | `739a7daf533b` | — |
| 316 | OVW-511 | `results/_krj10_reverdict_after_r4_convergence_2026_10_11.md` | `dc3e67f7d4f5` ／ 31,652 ／ 216 | `7b7684a49c58` ／ 31,672 ／ 216 | `739a7daf533b` | — |
| 317 | OVW-511 | `results/_krj10_terminal_verdict_closure_2026_10_11.md` | `cdf830797db3` ／ 14,081 ／ 105 | `f2253efbeb13` ／ 14,101 ／ 105 | `739a7daf533b` | — |
| 318 | OVW-511 | `results/_krj4_trj1_adjudication_judgment_2026_10_11.md` | `8e93f206b546` ／ 30,253 ／ 273 | `a894aed7b566` ／ 30,293 ／ 273 | `739a7daf533b` | — |
| 319 | OVW-511 | `results/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | `a6cbce33a1ff` ／ 16,547 ／ 148 | `741e2698699f` ／ 16,567 ／ 148 | `739a7daf533b` | — |
| 320 | OVW-511 | `results/_krj5_final_disposition_verdict_2026_10_11.md` | `caba9ef44ff8` ／ 60,640 ／ 413 | `b3b155e38028` ／ 60,700 ／ 413 | `739a7daf533b` | — |
| 321 | OVW-511 | `results/_krj5_subject_scope_judgment_2026_10_11.md` | `21e8e42f284f` ／ 45,304 ／ 274 | `b873520cdd95` ／ 45,372 ／ 274 | `739a7daf533b` | — |
| 322 | OVW-511 | `results/_krj5d_third_tier_effectivity_2026_10_11.md` | `c9983f6177ac` ／ 10,709 ／ 102 | `acdadd7aefef` ／ 10,729 ／ 102 | `739a7daf533b` | — |
| 323 | OVW-511 | `results/_krj9_scope_clarification_draft_2026_10_10.md` | `a2bf7d0f85d8` ／ 28,614 ／ 213 | `f686df361df6` ／ 28,654 ／ 213 | `739a7daf533b` | — |
| 324 | OVW-511 | `results/_krj_all_five_verdicts_rewrite_2026_10_11.md` | `cd304426ffe5` ／ 72,207 ／ 356 | `943c8aafa85f` ／ 72,247 ／ 356 | `739a7daf533b` | — |
| 325 | OVW-511 | `results/_krj_all_terminal_verdicts_2026_10_11.md` | `26aaf47192de` ／ 95,619 ／ 411 | `7c6f1187c880` ／ 95,659 ／ 411 | `739a7daf533b` | — |
| 326 | OVW-511 | `results/_krj_cond4_effectivity_declaration_2026_10_11.md` | `44660f750727` ／ 15,526 ／ 141 | `8ea98f0f8dc2` ／ 15,546 ／ 141 | `739a7daf533b` | — |
| 327 | OVW-511 | `results/_krj_five_verdicts_adjudication_2026_10_11.md` | `c0edaf60f28c` ／ 16,044 ／ 169 | `40b387aed7af` ／ 16,064 ／ 169 | `739a7daf533b` | — |
| 328 | OVW-511 | `results/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | `54842032466d` ／ 15,194 ／ 177 | `a4612beda9a8` ／ 15,214 ／ 177 | `739a7daf533b` | — |
| 329 | OVW-511 | `results/_kt_a1_anchor_drift_root_cause_2026_10_14.md` | `4e262d90f4ca` ／ 37,446 ／ 339 | `4e262d90f4ca` ／ 37,446 ／ 339 | `739a7daf533b` | R-02×3·R-04×2 |
| 330 | OVW-511 | `results/_kt_a1_v0_lineage_corrigendum_2026_10_14.md` | `b85cd41cbd73` ／ 31,855 ／ 300 | `b85cd41cbd73` ／ 31,855 ／ 300 | `739a7daf533b` | R-02×1·R-04×1 |
| 331 | OVW-511 | `results/_letters_archive_register_2026_10_01.md` | `eb92d0ae25ed` ／ 26,158 ／ 339 | `c32276eebb22` ／ 26,303 ／ 339 | `739a7daf533b` | R-03×1·R-04×1 |
| 332 | OVW-511 | `results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | `f56ccb6de842` ／ 14,750 ／ 132 | `ea3f82948673` ／ 14,770 ／ 132 | `739a7daf533b` | — |
| 333 | OVW-511 | `results/_lim_aperiod_restatement_third_domain_2026_10_11.md` | `8fb9a1bbd91e` ／ 27,906 ／ 214 | `dc518753f244` ／ 27,946 ／ 214 | `739a7daf533b` | — |
| 334 | OVW-511 | `results/_limb_reading_verdict_kv3s33_2026_10_01.md` | `5eaa7a03f151` ／ 56,321 ／ 484 | `d5590410823a` ／ 56,329 ／ 484 | `739a7daf533b` | — |
| 335 | OVW-511 | `results/_md_trigger_prereg_effectivity_2026_10_11.md` | `d68307e2e863` ／ 41,598 ／ 346 | `4b1c32665b9c` ／ 41,636 ／ 346 | `739a7daf533b` | — |
| 336 | OVW-511 | `results/_mini_round_5_decisions_register_2026_10_01.md`（组A） | `c9422fa9e7ed` ／ 53,125 ／ 376 | `52f5f0dd8a8c` ／ 53,125 ／ 376 | `739a7daf533b` | — |
| 337 | OVW-511 | `results/_misformed_commission_drafts_deletion_register_2026_10_11.md` | `b577aa149ac3` ／ 7,233 ／ 73 | `933ea82b8572` ／ 7,261 ／ 73 | `739a7daf533b` | — |
| 338 | OVW-511 | `results/_noncore_upload_caliber_draft_2026_10_17.md` | `ca6633580c8c` ／ 29,501 ／ 336 | `ca6633580c8c` ／ 29,501 ／ 336 | `739a7daf533b` | R-02×2·R-04×2 |
| 339 | OVW-511 | `results/_noncore_upload_caliber_effect_register_2026_10_17.md` | `4b72a49b9221` ／ 50,425 ／ 324 | `4b72a49b9221` ／ 50,425 ／ 324 | `739a7daf533b` | R-02×1·R-04×1 |
| 340 | OVW-511 | `results/_overnight_delivery_index_2026_10_10.md` | `6be2d532c63f` ／ 35,306 ／ 359 | `5876b6b8d617` ／ 35,344 ／ 359 | `739a7daf533b` | — |
| 341 | OVW-511 | `results/_p0_scan_2026_10_12.json` | `8f3a3743c8ac` ／ 20,994 ／ 408 | `8f3a3743c8ac` ／ 20,994 ／ 408 | `739a7daf533b` | R-01×2·R-02×6·R-03×2·R-04×7·R-05×1·R-06×2·R-07×3·R-09×2 |
| 342 | OVW-511 | `results/_p_k_v3_glm_fpr_audit_report_2026-09-17T08-23-41Z.md` | `030801392946` ／ 8,536 ／ 169 | `4896fc796ed8` ／ 8,560 ／ 169 | `739a7daf533b` | R-04×1 |
| 343 | OVW-511 | `results/_p_l_v3_phase1_report_20260917_132341.md` | `52a3d1e8be7b` ／ 11,041 ／ 223 | `52a3d1e8be7b` ／ 11,041 ／ 223 | `739a7daf533b` | R-02×1·R-04×1 |
| 344 | OVW-511 | `results/_p_l_v3_phase2_report_20260917_142748.md` | `9b5ea1432a1c` ／ 9,062 ／ 159 | `9b5ea1432a1c` ／ 9,062 ／ 159 | `739a7daf533b` | R-02×1·R-04×1 |
| 345 | OVW-511 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133358.md` | `cb06e4e5292a` ／ 6,639 ／ 146 | `cb06e4e5292a` ／ 6,639 ／ 146 | `739a7daf533b` | R-04×1 |
| 346 | OVW-511 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133512.md` | `4790cc6fde8a` ／ 6,339 ／ 141 | `4790cc6fde8a` ／ 6,339 ／ 141 | `739a7daf533b` | R-04×1 |
| 347 | OVW-511 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133705.md` | `aa33183b3cae` ／ 6,436 ／ 141 | `aa33183b3cae` ／ 6,436 ／ 141 | `739a7daf533b` | R-04×1 |
| 348 | OVW-511 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133726.md` | `ac783f124570` ／ 6,437 ／ 141 | `ac783f124570` ／ 6,437 ／ 141 | `739a7daf533b` | R-04×1 |
| 349 | OVW-511 | `results/_p_l_v3_phase3_plus_adendum_7_report_20260917_133852.md` | `524651e929bf` ／ 6,618 ／ 141 | `524651e929bf` ／ 6,618 ／ 141 | `739a7daf533b` | R-04×1 |
| 350 | OVW-511 | `results/_p_refresh_registration_preliminary_2026_10_10.md` | `d62328c4f3a9` ／ 32,740 ／ 301 | `d79c8f0c8fd4` ／ 32,780 ／ 301 | `739a7daf533b` | — |
| 351 | OVW-511 | `results/_p_refresh_s0_judgment_2026_10_10.md` | `06c7ada9fbb1` ／ 41,409 ／ 400 | `e875378b22ff` ／ 41,449 ／ 400 | `739a7daf533b` | — |
| 352 | OVW-511 | `results/_p_refresh_scope_judgment_2026_10_10.md` | `034f84aec0e5` ／ 33,964 ／ 259 | `217b7f46438f` ／ 34,004 ／ 259 | `739a7daf533b` | — |
| 353 | OVW-511 | `results/_pc_d1_d3_2026_09_15.py` | `f4501d50cb6c` ／ 43,039 ／ 803 | `e728ba7bd2b4` ／ 43,047 ／ 803 | `739a7daf533b` | R-02×3·R-04×8 |
| 354 | OVW-511 | `results/_pending_pi_items_drafts_2026_10_11.md` | `8227c455082f` ／ 40,658 ／ 300 | `a9ee659d65c8` ／ 40,678 ／ 300 | `739a7daf533b` | — |
| 355 | OVW-511 | `results/_pending_rulings_drafts_2026_10_11.md` | `f48cd3b0d562` ／ 42,735 ／ 340 | `f59136835d7d` ／ 42,775 ／ 340 | `739a7daf533b` | — |
| 356 | OVW-511 | `results/_pending_supply_search_receipt_2026_10_08.md` | `bde67d5a1516` ／ 12,601 ／ 154 | `52d072ec0343` ／ 12,595 ／ 154 | `739a7daf533b` | — |
| 357 | OVW-511 | `results/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md` | `8dc82b7c3c0f` ／ 11,800 ／ 148 | `8dc82b7c3c0f` ／ 11,800 ／ 148 | `739a7daf533b` | R-04×1 |
| 358 | OVW-511 | `results/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | `ee185be5f7da` ／ 13,863 ／ 131 | `68078f446d66` ／ 13,883 ／ 131 | `739a7daf533b` | — |
| 359 | OVW-511 | `results/_pi_effectivity_declaration_register_2026_10_11.md` | `4ebeea7caa2f` ／ 54,475 ／ 365 | `f1e451d60df1` ／ 54,511 ／ 365 | `739a7daf533b` | — |
| 360 | OVW-511 | `results/_plan_v3_pending_verify_2026_09_30.md` | `4544e99386d7` ／ 42,266 ／ 479 | `f40825a364b8` ／ 42,294 ／ 479 | `739a7daf533b` | R-04×7 |
| 361 | OVW-511 | `results/_pre_exec_report_kimi_2026_09_30.md` | `911ddccd5c44` ／ 5,683 ／ 74 | `e9232f54656e` ／ 5,677 ／ 74 | `739a7daf533b` | — |
| 362 | OVW-511 | `results/_pre_execution_report_kimi_2026_10_01.md` | `12eeed4c5426` ／ 6,279 ／ 88 | `91ac74bd958a` ／ 6,277 ／ 88 | `739a7daf533b` | — |
| 363 | OVW-511 | `results/_pre_execution_report_kimi_2026_10_12.md` | `70b0915abdbc` ／ 7,729 ／ 109 | `70b0915abdbc` ／ 7,729 ／ 109 | `739a7daf533b` | R-01×2·R-02×6·R-03×2·R-04×8·R-05×1·R-06×2·R-07×3·R-09×2 |
| 364 | OVW-511 | `results/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md` | `e90fe5903e28` ／ 7,176 ／ 152 | `e90fe5903e28` ／ 7,176 ／ 152 | `739a7daf533b` | R-02×10·R-04×5 |
| 365 | OVW-511 | `results/_q2_scope_vs_revision_judgment_2026_10_11.md` | `8d2534d1a44e` ／ 43,155 ／ 308 | `a76a99b95a0c` ／ 43,195 ／ 308 | `739a7daf533b` | — |
| 366 | OVW-511 | `results/_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | `5f1e0670f4c4` ／ 16,097 ／ 214 | `4d37c7e75106` ／ 16,105 ／ 214 | `739a7daf533b` | — |
| 367 | OVW-511 | `results/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | `f747cbdd3ce0` ／ 64,833 ／ 1119 | `7d8441077e67` ／ 64,849 ／ 1119 | `739a7daf533b` | — |
| 368 | OVW-511 | `results/_questionnaire_cards_intake_register_2026_10_09.md` | `441b199e098c` ／ 442,352 ／ 7501 | `37497030b73b` ／ 442,333 ／ 7501 | `739a7daf533b` | R-02×13·R-04×14·R-07×4·R-11×5 |
| 369 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | `a611d3e62978` ／ 84,113 ／ 1102 | `5140616c2035` ／ 84,127 ／ 1102 | `739a7daf533b` | — |
| 370 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | `877fe26ca772` ／ 55,327 ／ 602 | `46ee8668402e` ／ 55,341 ／ 602 | `739a7daf533b` | — |
| 371 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | `e552a449fc9b` ／ 121,123 ／ 1683 | `626c30caf82d` ／ 121,137 ／ 1683 | `739a7daf533b` | — |
| 372 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | `9e29f7f3ab4e` ／ 114,239 ／ 1508 | `ae2c5587a86b` ／ 114,253 ／ 1508 | `739a7daf533b` | — |
| 373 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | `d268d9eea466` ／ 54,871 ／ 540 | `3239456c7c9e` ／ 54,883 ／ 540 | `739a7daf533b` | — |
| 374 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | `a861f72e0d3c` ／ 44,684 ／ 398 | `884f61b07779` ／ 44,698 ／ 398 | `739a7daf533b` | — |
| 375 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `19fea1e0e3e8` ／ 72,217 ／ 1175 | `4a85ae03c395` ／ 72,199 ／ 1175 | `739a7daf533b` | — |
| 376 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `0de951feb9f3` ／ 262,560 ／ 4215 | `89744f279f62` ／ 262,542 ／ 4215 | `739a7daf533b` | — |
| 377 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | `294752c30345` ／ 67,227 ／ 892 | `131d0e0d0636` ／ 67,225 ／ 892 | `739a7daf533b` | — |
| 378 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | `8542b765938a` ／ 116,508 ／ 1538 | `2124536e1f71` ／ 116,476 ／ 1538 | `739a7daf533b` | R-11×2 |
| 379 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | `42e99a1c5aa4` ／ 77,193 ／ 1189 | `5376f4aae453` ／ 77,189 ／ 1189 | `739a7daf533b` | — |
| 380 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | `69a21d50620b` ／ 106,412 ／ 1593 | `1ad43c70cf01` ／ 106,453 ／ 1593 | `739a7daf533b` | — |
| 381 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `c69261f091af` ／ 52,586 ／ 849 | `ba5c6e7a4a9c` ／ 52,602 ／ 849 | `739a7daf533b` | — |
| 382 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `59026ae97582` ／ 17,501 ／ 162 | `abc9a7d2293a` ／ 17,517 ／ 162 | `739a7daf533b` | — |
| 383 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | `723b79dffa1c` ／ 50,774 ／ 530 | `62e68c52414c` ／ 50,790 ／ 530 | `739a7daf533b` | — |
| 384 | OVW-511 | `results/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | `c533fd52eb13` ／ 84,408 ／ 1076 | `249c30c031d3` ／ 84,422 ／ 1076 | `739a7daf533b` | — |
| 385 | OVW-511 | `results/_r2_build_manifest_2026_10_12.json` | `5b89369890ee` ／ 217,655 ／ 7339 | `5b89369890ee` ／ 217,655 ／ 7339 | `739a7daf533b` | R-01×17·R-02×124·R-03×11·R-04×159·R-05×3·R-06×9·R-07×4·R-08×2·R-09×10 |
| 386 | OVW-511 | `results/_r2_execution_receipt_kimi_2026_10_12.md` | `4cc87c0abd0b` ／ 5,444 ／ 57 | `4cc87c0abd0b` ／ 5,444 ／ 57 | `739a7daf533b` | R-01×2·R-02×2·R-03×2·R-04×3·R-05×2·R-06×2·R-07×2·R-08×2·R-09×2·R-10×1 |
| 387 | OVW-511 | `results/_r5_spec_pack_retrieval_register_2026_10_13.md` | `e9d4379d24b3` ／ 24,851 ／ 235 | `e9d4379d24b3` ／ 24,851 ／ 235 | `739a7daf533b` | R-03×2·R-04×1 |
| 388 | OVW-511 | `results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md.asset.json` | `2d360c03f4d1` ／ 1,039 ／ 17 | `2d360c03f4d1` ／ 1,039 ／ 17 | `739a7daf533b` | R-04×1 |
| 389 | OVW-511 | `results/_r_pair_addendum_2026_10_09.json` | `f462ad619013` ／ 110,512 ／ 1303 | `e3ceee1988ad` ／ 110,510 ／ 1303 | `739a7daf533b` | — |
| 390 | OVW-511 | `results/_receipt_disposition_register_2026_10_08.md` | `2f749d7d1457` ／ 22,999 ／ 234 | `f286e357b13f` ／ 23,050 ／ 234 | `739a7daf533b` | — |
| 391 | OVW-511 | `results/_refcheck_hash_change_reference_recheck_2026_09_30.md` | `c8de825f3391` ／ 33,633 ／ 346 | `c8de825f3391` ／ 33,633 ／ 346 | `739a7daf533b` | R-02×2 |
| 392 | OVW-511 | `results/_register3_bytes_erratum_2026_10_11.md` | `ee2c0b0ccc5a` ／ 13,254 ／ 135 | `7bc1a4d3c812` ／ 13,294 ／ 135 | `739a7daf533b` | — |
| 393 | OVW-511 | `results/_repo_full_inventory_catalogue_2026_10_12.md` | `35309e81bd0a` ／ 591,773 ／ 3908 | `6828c18578ae` ／ 591,851 ／ 3908 | `739a7daf533b` | R-04×9 |
| 394 | OVW-511 | `results/_repo_post_cleanup_snapshot_2026_10_12.md` | `9094c78c5433` ／ 309,394 ／ 2973 | `ccf2abf85550` ／ 309,447 ／ 2973 | `739a7daf533b` | R-04×14 |
| 395 | OVW-511 | `results/_root_session_history_memo_2026_10_14.md` | `066c6f031ba0` ／ 66,582 ／ 601 | `8efe88fe1076` ／ 97,162 ／ 927 | `739a7daf533b` | R-02×3·R-04×4·R-05×1 |
| 396 | OVW-511 | `results/_root_session_history_memo_main_2026_10_14.md` | `9502b9beaf9f` ／ 160,625 ／ 1035 | `9502b9beaf9f` ／ 160,625 ／ 1035 | `739a7daf533b` | R-02×4·R-04×3 |
| 397 | OVW-511 | `results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | `7b021054c471` ／ 25,621 ／ 215 | `df3281e6871a` ／ 25,637 ／ 215 | `739a7daf533b` | — |
| 398 | OVW-511 | `results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | `a5bf28d3fcca` ／ 20,007 ／ 177 | `67da78b3d19e` ／ 20,023 ／ 177 | `739a7daf533b` | — |
| 399 | OVW-511 | `results/_round54_g5_dispositions_register_2026_10_10.md` | `fdd3ccd3a8a1` ／ 39,961 ／ 269 | `a483ac9fba64` ／ 39,977 ／ 269 | `739a7daf533b` | — |
| 400 | OVW-511 | `results/_round55_dispositions_register_2026_10_10.md` | `5c7cb610a8c7` ／ 34,897 ／ 268 | `3193804b4aaf` ／ 34,913 ／ 268 | `739a7daf533b` | — |
| 401 | OVW-511 | `results/_round56_ad8fix_effectivity_register_2026_10_10.md` | `df46bd4e2eec` ／ 16,555 ／ 159 | `67df53c3e97f` ／ 16,553 ／ 159 | `739a7daf533b` | — |
| 402 | OVW-511 | `results/_round56_b01_followup_disposition_plan_2026_10_10.md` | `648f83115184` ／ 30,964 ／ 304 | `388ef92900f2` ／ 31,004 ／ 304 | `739a7daf533b` | — |
| 403 | OVW-511 | `results/_round56_direct_adoptions_register_2026_10_10.md` | `3a8b5c22f5e3` ／ 43,202 ／ 285 | `866261714244` ／ 43,240 ／ 285 | `739a7daf533b` | — |
| 404 | OVW-511 | `results/_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | `10ca088d9ce1` ／ 34,165 ／ 329 | `3a50cef82902` ／ 34,181 ／ 329 | `739a7daf533b` | — |
| 405 | OVW-511 | `results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | `23d65bf5e9fd` ／ 25,029 ／ 240 | `bddcd0848fb2` ／ 25,045 ／ 240 | `739a7daf533b` | — |
| 406 | OVW-511 | `results/_round56_idx_sc1_resolution_2026_10_10.md` | `bb722799e89e` ／ 47,089 ／ 336 | `0f61665cb8ea` ／ 47,107 ／ 336 | `739a7daf533b` | — |
| 407 | OVW-511 | `results/_round56_n10_erratum_register_2026_10_10.md` | `bd948baf6f71` ／ 20,305 ／ 187 | `78da765f2b4b` ／ 20,321 ／ 187 | `739a7daf533b` | — |
| 408 | OVW-511 | `results/_round56_pending_questions_compilation_2026_10_10.md` | `3fbba85846d8` ／ 33,444 ／ 166 | `219b55f758e9` ／ 33,504 ／ 166 | `739a7daf533b` | — |
| 409 | OVW-511 | `results/_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | `bb5c9001dd31` ／ 28,959 ／ 208 | `3b894f46c3d1` ／ 29,019 ／ 208 | `739a7daf533b` | — |
| 410 | OVW-511 | `results/_round56_registration_supplement_2026_10_10.md` | `f22659a123c5` ／ 21,827 ／ 175 | `280a921dea9a` ／ 21,865 ／ 175 | `739a7daf533b` | — |
| 411 | OVW-511 | `results/_round56_review_effectivity_register_2026_10_10.md` | `641eb4c6ac2a` ／ 48,969 ／ 349 | `251e2eb167c2` ／ 49,013 ／ 349 | `739a7daf533b` | — |
| 412 | OVW-511 | `results/_round56_review_effectivity_register_3_2026_10_10.md` | `0b07905291dc` ／ 77,137 ／ 432 | `15295e3eeb26` ／ 77,181 ／ 432 | `739a7daf533b` | — |
| 413 | OVW-511 | `results/_round56_review_effectivity_register_4_2026_10_11.md` | `e5889a1a51bb` ／ 46,870 ／ 260 | `f3d03ea79519` ／ 46,908 ／ 260 | `739a7daf533b` | — |
| 414 | OVW-511 | `results/_round56_review_effectivity_register_5_2026_10_11.md` | `5118e6894251` ／ 67,575 ／ 290 | `11f8befcefa3` ／ 67,613 ／ 290 | `739a7daf533b` | — |
| 415 | OVW-511 | `results/_round56_review_effectivity_register_6_2026_10_11.md` | `e126cd454064` ／ 58,440 ／ 264 | `acba222fdf57` ／ 58,478 ／ 264 | `739a7daf533b` | — |
| 416 | OVW-511 | `results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | `9069eede88f9` ／ 16,642 ／ 163 | `729043e158c8` ／ 16,640 ／ 163 | `739a7daf533b` | — |
| 417 | OVW-511 | `results/_round56_shortname_backfill_note_2026_10_10.md` | `ed112e78cbb8` ／ 22,157 ／ 200 | `eb5bee36daf4` ／ 22,195 ／ 200 | `739a7daf533b` | — |
| 418 | OVW-511 | `results/_round56_terminal_boundary_effectivity_register_2026_10_10.md` | `734fc54ea746` ／ 35,862 ／ 274 | `bc45365245aa` ／ 35,878 ／ 274 | `739a7daf533b` | — |
| 419 | OVW-511 | `results/_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | `e1b8a8b66c9d` ／ 28,362 ／ 224 | `1b8daf6983d7` ／ 28,378 ／ 224 | `739a7daf533b` | — |
| 420 | OVW-511 | `results/_round56_th4_two_field_reporting_resolution_2026_10_10.md` | `1f182b639d5e` ／ 28,217 ／ 216 | `da1a6ea941f2` ／ 28,233 ／ 216 | `739a7daf533b` | — |
| 421 | OVW-511 | `results/_round56_typeb_backfill_register_2026_10_10.md` | `a36975e48f45` ／ 40,215 ／ 331 | `238be5a072c6` ／ 40,253 ／ 331 | `739a7daf533b` | — |
| 422 | OVW-511 | `results/_round56_typeb_form_draft_2026_10_10.md` | `df7a80c3e61f` ／ 50,150 ／ 382 | `ab979408cda3` ／ 50,170 ／ 382 | `739a7daf533b` | — |
| 423 | OVW-511 | `results/_round56_typeb_implementation_register_2026_10_10.md` | `8a2ccfd50d52` ／ 26,329 ／ 231 | `a2deb8df3616` ／ 26,367 ／ 231 | `739a7daf533b` | — |
| 424 | OVW-511 | `results/_round56_v4_kd_row_correction_revision_2026_10_10.md` | `5200924444b7` ／ 23,437 ／ 236 | `40932e5803d0` ／ 23,453 ／ 236 | `739a7daf533b` | — |
| 425 | OVW-511 | `results/_round56a_dispositions_register_2026_10_10.md` | `43f36a646019` ／ 50,329 ／ 289 | `490aa8148a87` ／ 50,365 ／ 289 | `739a7daf533b` | — |
| 426 | OVW-511 | `results/_round56c_card_id_erratum_2026_10_10.md` | `b9aba7f5edb9` ／ 18,703 ／ 174 | `bec98ef06a48` ／ 18,749 ／ 174 | `739a7daf533b` | R-04×1 |
| 427 | OVW-511 | `results/_round56c_d23_ad5_judgment_2026_10_10.md` | `d50569ddcca4` ／ 50,727 ／ 335 | `f526cceb4c75` ／ 50,747 ／ 335 | `739a7daf533b` | — |
| 428 | OVW-511 | `results/_round56r8_dispositions_register_2026_10_10.md` | `2c56d7b3835a` ／ 46,119 ／ 289 | `834d4dc31af5` ／ 46,135 ／ 289 | `739a7daf533b` | — |
| 429 | OVW-511 | `results/_round56r9r10_dispositions_register_2026_10_10.md` | `1449fe1ab5df` ／ 49,698 ／ 293 | `f6e9704ac575` ／ 49,754 ／ 293 | `739a7daf533b` | — |
| 430 | OVW-511 | `results/_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | `e2fee828f1b8` ／ 29,951 ／ 249 | `37a856ff5782` ／ 29,991 ／ 249 | `739a7daf533b` | — |
| 431 | OVW-511 | `results/_s2prime_krj3_applicability_recheck_2026_10_10.md` | `ab4d6db386cd` ／ 41,282 ／ 337 | `ea7839df970c` ／ 41,322 ／ 337 | `739a7daf533b` | — |
| 432 | OVW-511 | `results/_s3prime_alert_disposition_judgment_2026_10_11.md` | `66975edaa99f` ／ 53,128 ／ 378 | `325b927ceea6` ／ 53,188 ／ 378 | `739a7daf533b` | — |
| 433 | OVW-511 | `results/_s3prime_degeneracy_selfcert_2026_10_11.md` | `139986b64f9c` ／ 39,879 ／ 327 | `47a10d98edae` ／ 39,939 ／ 327 | `739a7daf533b` | — |
| 434 | OVW-511 | `results/_s3prime_recompute_after_supplement_2026_10_11.md` | `97619a3c7c8e` ／ 41,648 ／ 338 | `4992c2b84c99` ／ 41,708 ／ 338 | `739a7daf533b` | — |
| 435 | OVW-511 | `results/_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | `b899cb2f91fe` ／ 44,179 ／ 337 | `5872e85049bf` ／ 44,199 ／ 337 | `739a7daf533b` | — |
| 436 | OVW-511 | `results/_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | `1b693dec8fea` ／ 34,681 ／ 383 | `baf86b575ab1` ／ 34,689 ／ 383 | `739a7daf533b` | — |
| 437 | OVW-511 | `results/_s4_heldout_sampling_seed42_register_2026_10_09.md` | `cefb47728dbb` ／ 37,607 ／ 398 | `302b47c9138b` ／ 37,615 ／ 398 | `739a7daf533b` | — |
| 438 | OVW-511 | `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `d03126028128` ／ 18,923 ／ 439 | `dcd1fc53e83c` ／ 19,003 ／ 440 | `739a7daf533b` | — |
| 439 | OVW-511 | `results/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | `90370c77b4a5` ／ 24,650 ／ 281 | `dc49602cad89` ／ 24,690 ／ 281 | `739a7daf533b` | — |
| 440 | OVW-511 | `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `1b1f027db264` ／ 52,655 ／ 841 | `ee0f43b1fe83` ／ 52,785 ／ 842 | `739a7daf533b` | — |
| 441 | OVW-511 | `results/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `a300572d5420` ／ 22,606 ／ 250 | `040718619f7b` ／ 22,646 ／ 250 | `739a7daf533b` | — |
| 442 | OVW-511 | `results/_s4_heldout_seedprime_verification_2026_10_10.md` | `74e09e84ff0c` ／ 21,946 ／ 257 | `fdf02a9a0447` ／ 21,966 ／ 257 | `739a7daf533b` | — |
| 443 | OVW-511 | `results/_s4_open_questions_addendum_2026_10_09.json` | `2d7b322065d2` ／ 35,217 ／ 349 | `8a2cb27e6fe0` ／ 35,215 ／ 349 | `739a7daf533b` | — |
| 444 | OVW-511 | `results/_s4_seedprime_inheldout_recompute_2026_10_10.md` | `14a461780763` ／ 21,826 ／ 244 | `73382f10061f` ／ 21,866 ／ 244 | `739a7daf533b` | — |
| 445 | OVW-511 | `results/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | `d90c313b2c99` ／ 24,743 ／ 217 | `319c77148b2c` ／ 24,783 ／ 217 | `739a7daf533b` | — |
| 446 | OVW-511 | `results/_s4_source_wave_mapping_registration_2026_10_10.md` | `51ee08ae73cf` ／ 38,211 ／ 309 | `1dea5a7f30f7` ／ 38,231 ／ 309 | `739a7daf533b` | — |
| 447 | OVW-511 | `results/_s4_substrate_topup_addendum_2026_10_09.json` | `1ba293951b31` ／ 85,863 ／ 926 | `e32529b0371b` ／ 85,861 ／ 926 | `739a7daf533b` | — |
| 448 | OVW-511 | `results/_s4prime_five_lines_readings_2026_10_11.md` | `747f06b6009c` ／ 23,857 ／ 301 | `d1f01b136d9e` ／ 23,877 ／ 301 | `739a7daf533b` | — |
| 449 | OVW-511 | `results/_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | `fb5c677e72a4` ／ 58,338 ／ 360 | `e1373b419641` ／ 58,378 ／ 360 | `739a7daf533b` | — |
| 450 | OVW-511 | `results/_s5prime_lim_a_and_item_registers_2026_10_11.md` | `2cd63dba3bb8` ／ 47,185 ／ 335 | `d4ab99975a77` ／ 47,225 ／ 335 | `739a7daf533b` | — |
| 451 | OVW-511 | `results/_s6doubleprime_terminal_verdicts_2026_10_11.md` | `33b19246feb9` ／ 76,850 ／ 360 | `1ff6f03a1c96` ／ 76,910 ／ 360 | `739a7daf533b` | — |
| 452 | OVW-511 | `results/_s6doubleprime_verdict_supplement_2026_10_11.md` | `7853e29f5cfc` ／ 31,495 ／ 174 | `746426b0b285` ／ 31,515 ／ 174 | `739a7daf533b` | — |
| 453 | OVW-511 | `results/_s6prime_terminal_verdicts_2026_10_11.md` | `7a8b356ffd8b` ／ 54,877 ／ 350 | `4d449dc4acd8` ／ 54,937 ／ 350 | `739a7daf533b` | — |
| 454 | OVW-511 | `results/_s7doubleprime_verification_2026_10_11.md` | `e1121ea6b28c` ／ 41,620 ／ 370 | `9661494aea4f` ／ 41,680 ／ 370 | `739a7daf533b` | — |
| 455 | OVW-511 | `results/_s7doubleprime_verification_erratum_2026_10_11.md` | `2bbf169f9be6` ／ 32,762 ／ 239 | `00a219feb86a` ／ 32,822 ／ 239 | `739a7daf533b` | — |
| 456 | OVW-511 | `results/_s7prime_findings_erratum_2026_10_11.md` | `99f9c34aaa90` ／ 30,948 ／ 289 | `b4493b9fbe38` ／ 31,008 ／ 289 | `739a7daf533b` | — |
| 457 | OVW-511 | `results/_s7prime_prereq_and_verification_2026_10_11.md` | `6c04e8c0e1d2` ／ 36,727 ／ 303 | `5b975ed206a5` ／ 36,787 ／ 303 | `739a7daf533b` | — |
| 458 | OVW-511 | `results/_seed_double_criterion_draft_2026_10_11.md` | `f3d8f45561f5` ／ 40,459 ／ 283 | `0a3362018856` ／ 40,499 ／ 283 | `739a7daf533b` | — |
| 459 | OVW-511 | `results/_seed_double_identifier_final_judgment_2026_10_11.md` | `709d6bf1bbd2` ／ 50,182 ／ 368 | `32d25d82a584` ／ 50,222 ／ 368 | `739a7daf533b` | — |
| 460 | OVW-511 | `results/_seed_double_identifier_finalization_2026_10_11.md` | `6f5d16b74ea8` ／ 26,844 ／ 247 | `3bb2b5bc9289` ／ 26,864 ／ 247 | `739a7daf533b` | — |
| 461 | OVW-511 | `results/_seed_double_rule_judgment_2026_10_11.md` | `500d1c84f2e0` ／ 57,145 ／ 346 | `42cc96d0683f` ／ 57,185 ／ 346 | `739a7daf533b` | — |
| 462 | OVW-511 | `results/_seven_gap_closures_adoption_register_2026_10_11.md` | `d1d9dfb4557a` ／ 11,940 ／ 102 | `77bc8321aa38` ／ 11,960 ／ 102 | `739a7daf533b` | — |
| 463 | OVW-511 | `results/_stage1_independent_gate_review_2026_10_12.md` | `cc864345e5f3` ／ 29,425 ／ 264 | `8489ee888ae0` ／ 29,479 ／ 264 | `739a7daf533b` | — |
| 464 | OVW-511 | `results/_stage1_tail_caliber_unification_register_2026_10_11.md` | `d10449b8019f` ／ 41,120 ／ 355 | `97315904a13e` ／ 41,140 ／ 355 | `739a7daf533b` | — |
| 465 | OVW-511 | `results/_stage2_trae_reply_acceptance_register_2026_10_12.md` | `b5cb510206f3` ／ 14,854 ／ 140 | `9e006c0584c8` ／ 14,874 ／ 140 | `739a7daf533b` | — |
| 466 | OVW-511 | `results/_stage3_1_bulk_reorg_completion_register_2026_10_12.md` | `408fb37dfc15` ／ 15,803 ／ 173 | `c6814cf0a0b7` ／ 15,818 ／ 173 | `739a7daf533b` | — |
| 467 | OVW-511 | `results/_stage3_completion_and_stage4_open_register_2026_10_12.md` | `6b412b2a8c5a` ／ 12,642 ／ 122 | `6b412b2a8c5a` ／ 12,642 ／ 122 | `739a7daf533b` | R-02×2 |
| 468 | OVW-511 | `results/_stage3_extraction_verification_2026_10_11.md` | `e777c746f6d8` ／ 22,379 ／ 266 | `635b562d3a5b` ／ 22,399 ／ 266 | `739a7daf533b` | — |
| 469 | OVW-511 | `results/_stage3_open_and_mandate_register_2026_10_12.md` | `8f6f952dea43` ／ 13,825 ／ 131 | `3caf22fa7486` ／ 13,865 ／ 131 | `739a7daf533b` | — |
| 470 | OVW-511 | `results/_stage3_r2_cleanup_register_2026_10_18.md` | `c703e9611da8` ／ 62,893 ／ 476 | `c703e9611da8` ／ 62,893 ／ 476 | `739a7daf533b` | R-04×4 |
| 471 | OVW-511 | `results/_stage3_readings_verification_2026_10_11.md` | `faf2d978ef74` ／ 29,936 ／ 334 | `8943272627e9` ／ 29,956 ／ 334 | `739a7daf533b` | — |
| 472 | OVW-511 | `results/_stage3_trigger_readings_2026_10_11.md` | `8d8488bc8716` ／ 35,683 ／ 335 | `3f3a8d002a47` ／ 35,711 ／ 335 | `739a7daf533b` | — |
| 473 | OVW-511 | `results/_stage3_trigger_recheck_2026_10_11.md` | `c866e0dfd4ba` ／ 49,049 ／ 347 | `0b57f4096b3f` ／ 49,109 ／ 347 | `739a7daf533b` | — |
| 474 | OVW-511 | `results/_stage_sequence_violation_register_2026_10_12.md` | `1e9cbb33d96d` ／ 11,139 ／ 110 | `531018438e42` ／ 11,159 ／ 110 | `739a7daf533b` | — |
| 475 | OVW-511 | `results/_supplement_to_500_design_review_2026_10_16.md` | `4133b3599fd3` ／ 46,163 ／ 378 | `4133b3599fd3` ／ 46,163 ／ 378 | `739a7daf533b` | R-02×1 |
| 476 | OVW-511 | `results/_suspect17_release_move_register_2026_10_09.md` | `0f1d1f80230f` ／ 22,328 ／ 203 | `7d8f557cdf1e` ／ 22,351 ／ 203 | `739a7daf533b` | — |
| 477 | OVW-511 | `results/_t1_exp2_activation_supplement_2026_10_09.md` | `20f29e21c80c` ／ 24,710 ／ 248 | `61049ff75bb6` ／ 24,708 ／ 248 | `739a7daf533b` | — |
| 478 | OVW-511 | `results/_t1_exp2_executor_2026_10_09.py` | `8697740e0aca` ／ 67,949 ／ 1430 | `fe80596a9a6f` ／ 67,955 ／ 1430 | `739a7daf533b` | — |
| 479 | OVW-511 | `results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md`（漂移登记） | `ddb383dcc51b` ／ 72,926 ／ 550 | `1ace80bfb19c` ／ 72,934 ／ 550 | `739a7daf533b` | — |
| 480 | OVW-511 | `results/_temp_cleanup_register_2026_10_13.md` | `22fde9ae557b` ／ 10,600 ／ 170 | `22fde9ae557b` ／ 10,600 ／ 170 | `739a7daf533b` | R-03×1 |
| 481 | OVW-511 | `results/_theory_boundary_clone_sync_register_2026_10_09.md` | `085fbf7cd9aa` ／ 17,532 ／ 164 | `085fbf7cd9aa` ／ 17,532 ／ 164 | `739a7daf533b` | R-02×1 |
| 482 | OVW-511 | `results/_theory_input_request_supplement_2026_09_29.md` | `1517f0249d63` ／ 48,280 ／ 431 | `1517f0249d63` ／ 48,280 ／ 431 | `739a7daf533b` | R-02×20·R-04×5 |
| 483 | OVW-511 | `results/_three_pending_items_drafts_2026_10_11.md` | `27ca82578a29` ／ 51,688 ／ 361 | `41c763713c1a` ／ 51,748 ／ 361 | `739a7daf533b` | — |
| 484 | OVW-511 | `results/_three_pending_items_effectivity_2026_10_11.md` | `19b47d140045` ／ 16,724 ／ 168 | `b199ecc80ca8` ／ 16,744 ／ 168 | `739a7daf533b` | — |
| 485 | OVW-511 | `results/_thv3_15_parallel_seed_double_note_2026_10_11.md` | `3a31f5d7ad13` ／ 15,551 ／ 167 | `fde59293f674` ／ 15,569 ／ 167 | `739a7daf533b` | — |
| 486 | OVW-511 | `results/_trae_issues_batch3_six_items_draft_2026_10_12.md` | `79bddad30c1d` ／ 29,961 ／ 263 | `79bddad30c1d` ／ 29,961 ／ 263 | `739a7daf533b` | R-02×1 |
| 487 | OVW-511 | `results/_trae_issues_disposition_schedule_2026_10_12.md` | `ab901b9a72ef` ／ 12,861 ／ 131 | `ab901b9a72ef` ／ 12,861 ／ 131 | `739a7daf533b` | R-04×6 |
| 488 | OVW-511 | `results/_trigger_denominator_caliber_judgment_2026_10_11.md` | `712b54772f56` ／ 43,388 ／ 276 | `223e30582ee0` ／ 43,448 ／ 276 | `739a7daf533b` | — |
| 489 | OVW-511 | `results/_trj_w1_downstream_erratum_2026_10_10.md` | `688b98ff44bd` ／ 24,868 ／ 219 | `9ca61f7833db` ／ 24,888 ／ 219 | `739a7daf533b` | — |
| 490 | OVW-511 | `results/_trj_w1_verification_2026_10_10.md` | `712b03ed9568` ／ 22,994 ／ 231 | `414410f8c677` ／ 23,014 ／ 231 | `739a7daf533b` | — |
| 491 | OVW-511 | `results/_two_items_alternative_deliberation_judgment_2026_10_13.md` | `f6b73a4b8228` ／ 44,782 ／ 355 | `f6b73a4b8228` ／ 44,782 ／ 355 | `739a7daf533b` | R-04×2 |
| 492 | OVW-511 | `results/_typeb_m_caliber_2026_10_10.md` | `d7b400366a1f` ／ 32,810 ／ 281 | `628fb6fe4fb0` ／ 32,830 ／ 281 | `739a7daf533b` | — |
| 493 | OVW-511 | `results/_typeb_m_definition_judgment_2026_10_10.md` | `0a2b396958c4` ／ 41,412 ／ 302 | `29be716acfa5` ／ 41,432 ／ 302 | `739a7daf533b` | — |
| 494 | OVW-511 | `results/_typeb_m_registration_2026_10_10.md` | `f06b8ebb594c` ／ 27,758 ／ 238 | `f661a9c43455` ／ 27,778 ／ 238 | `739a7daf533b` | — |
| 495 | OVW-511 | `results/_u04_1_exemption_precondition_verification_2026_10_09.md` | `b779b83fb02c` ／ 21,369 ／ 190 | `74b52b923a57` ／ 21,377 ／ 190 | `739a7daf533b` | — |
| 496 | OVW-511 | `results/_u3_carrier_qid_verification_2026_10_11.md` | `3f6a88210fb2` ／ 21,552 ／ 245 | `1762d338a1c9` ／ 21,572 ／ 245 | `739a7daf533b` | — |
| 497 | OVW-511 | `results/_u5b_p_counting_resolution_2026_10_10.md` | `a1847e9f51f7` ／ 20,046 ／ 144 | `431f998079cb` ／ 20,086 ／ 144 | `739a7daf533b` | — |
| 498 | OVW-511 | `results/_u6_negative_delta_compatibility_2026_10_11.md` | `3989ef97bfb1` ／ 20,949 ／ 184 | `015bc8dd1609` ／ 20,969 ／ 184 | `739a7daf533b` | — |
| 499 | OVW-511 | `results/_u_cf_category_caliber_2026_10_10.md` | `4b82a9671d6e` ／ 18,916 ／ 194 | `b99e008fb01c` ／ 18,976 ／ 194 | `739a7daf533b` | — |
| 500 | OVW-511 | `results/_u_cf_reclassification_2026_10_10.md` | `51527925597f` ／ 25,638 ／ 252 | `be3de9009298` ／ 25,698 ／ 252 | `739a7daf533b` | — |
| 501 | OVW-511 | `results/_u_closure_execution_register_2026_10_09.md` | `4c5d5368aa76` ／ 12,759 ／ 116 | `f890ddd6e453` ／ 12,781 ／ 116 | `739a7daf533b` | — |
| 502 | OVW-511 | `results/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md` | `20cedf10c2f5` ／ 31,106 ／ 207 | `20cedf10c2f5` ／ 31,106 ／ 207 | `739a7daf533b` | R-04×3 |
| 503 | OVW-511 | `results/_unclosed_47_pi_give_draft_2026_10_13.md` | `a401d4a2b4d5` ／ 61,343 ／ 445 | `a401d4a2b4d5` ／ 61,343 ／ 445 | `739a7daf533b` | R-04×1 |
| 504 | OVW-511 | `results/_unclosed_items_inventory_2026_10_08.md` | `5d822b49bbc8` ／ 30,235 ／ 278 | `5d822b49bbc8` ／ 30,235 ／ 278 | `739a7daf533b` | R-04×3·R-07×1 |
| 505 | OVW-511 | `results/_upload_execution_receipt_kimi_2026_10_12.md` | `fa634919ff9e` ／ 4,843 ／ 79 | `fa634919ff9e` ／ 4,843 ／ 79 | `739a7daf533b` | R-01×1·R-02×1·R-03×1·R-04×1·R-05×1·R-06×1·R-07×1·R-08×1·R-09×1·R-10×1 |
| 506 | OVW-511 | `results/_upload_guard_mirror_pair_2026_10_08.md` | `ae7633cfa6b7` ／ 23,604 ／ 273 | `c347fa1b2e34` ／ 23,634 ／ 273 | `739a7daf533b` | R-03×1·R-04×44·R-07×1 |
| 507 | OVW-511 | `results/_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md` | `c8331b3a63c0` ／ 75,241 ／ 477 | `c8331b3a63c0` ／ 75,241 ／ 477 | `739a7daf533b` | R-01×18·R-02×125·R-03×12·R-04×160·R-05×4·R-06×10·R-07×5·R-08×3·R-09×11·R-10×1 |
| 508 | OVW-511 | `results/_v3_recheck_05_result_2026_09_28.json` | `948ae3ece224` ／ 450,701 ／ 15213 | `eda36fcfe0df` ／ 450,751 ／ 15213 | `739a7daf533b` | — |
| 509 | OVW-511 | `results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md` | `c7ff24b95ca4` ／ 17,071 ／ 241 | `e495b054ef0b` ／ 17,069 ／ 241 | `739a7daf533b` | — |
| 510 | OVW-511 | `results/_v3_recheck_21_rescript_2026_09_27.md` | `8927d7c3cee1` ／ 14,622 ／ 167 | `8927d7c3cee1` ／ 14,622 ／ 167 | `739a7daf533b` | R-02×1 |
| 511 | OVW-511 | `results/_v3_recheck_21_result_2026_09_27.json` | `ad9135f3a220` ／ 44,771 ／ 1661 | `baeaedc35531` ／ 44,936 ／ 1661 | `739a7daf533b` | R-02×2 |
| 512 | OVW-511 | `results/_v3_recheck_prereg_v1p1_2026_09_27.md` | `f8394583129f` ／ 42,907 ／ 365 | `4422e0a2032d` ／ 42,978 ／ 365 | `739a7daf533b` | R-02×2 |
| 513 | OVW-511 | `results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md` | `ac73825cb34a` ／ 17,576 ／ 234 | `46ab58f5894e` ／ 17,574 ／ 234 | `739a7daf533b` | — |
| 514 | OVW-511 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | `b16d7fe824a8` ／ 194,179 ／ 1927 | `f6ac11f43855` ／ 194,131 ／ 1927 | `739a7daf533b` | R-04×24 |
| 515 | OVW-511 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `da9fb0cad410` ／ 356,039 ／ 3818 | `f7f39fb8549a` ／ 355,847 ／ 3818 | `739a7daf533b` | R-04×14 |
| 516 | OVW-511 | `results/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `b24d710ed030` ／ 23,092 ／ 262 | `3915f60c6d9b` ／ 23,162 ／ 262 | `739a7daf533b` | R-04×5 |
| 517 | OVW-511 | `results/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | `bd07469049db` ／ 37,173 ／ 439 | `f649e045876a` ／ 37,218 ／ 439 | `739a7daf533b` | R-04×3 |
| 518 | OVW-511 | `results/_v3_v4_ghostref_reconciliation_2026_09_23.md` | `0be54db0d1ea` ／ 169,884 ／ 658 | `0be54db0d1ea` ／ 169,884 ／ 658 | `739a7daf533b` | R-04×10 |
| 519 | OVW-511 | `results/_v3x_d0_5_aggregation_2026_09_17.md` | `c06b707cb516` ／ 12,016 ／ 253 | `c06b707cb516` ／ 12,016 ／ 253 | `739a7daf533b` | R-02×1·R-04×1 |
| 520 | OVW-511 | `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` | `455a9f62453b` ／ 7,639 ／ 159 | `455a9f62453b` ／ 7,639 ／ 159 | `739a7daf533b` | R-02×3·R-04×5 |
| 521 | OVW-511 | `results/_v3x_d0_5_proposal_coze_2026_09_17.md` | `47787a82029d` ／ 13,204 ／ 146 | `47787a82029d` ／ 13,204 ／ 146 | `739a7daf533b` | R-02×1 |
| 522 | OVW-511 | `results/_v3x_p_l_v3_external_spec_2026_09_17.md` | `36aaab76914d` ／ 5,775 ／ 178 | `36aaab76914d` ／ 5,775 ／ 178 | `739a7daf533b` | R-02×1·R-04×1 |
| 523 | OVW-511 | `results/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `847cee4f1ba8` ／ 9,576 ／ 169 | `847cee4f1ba8` ／ 9,576 ／ 169 | `739a7daf533b` | R-02×1·R-04×1 |
| 524 | OVW-511 | `results/_v4_closeout_account_reconciliation_2026_10_12.md` | `e2dc09b06007` ／ 24,398 ／ 243 | `1fd9e231650b` ／ 24,453 ／ 243 | `739a7daf533b` | — |
| 525 | OVW-511 | `results/_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `87a2ff256873` ／ 184,936 ／ 1045 | `2b36d3874b4d` ／ 197,287 ／ 1045 | `739a7daf533b` | R-04×2 |
| 526 | OVW-511 | `results/_v4_closeout_moves_and_cleanup_register_2026_10_12.md` | `d3e6528187c2` ／ 18,536 ／ 176 | `36c7b38ca540` ／ 18,568 ／ 176 | `739a7daf533b` | — |
| 527 | OVW-511 | `results/_v4_design_integration_2026_09_21_v1.1.md` | `28b94277ca51` ／ 139,983 ／ 1190 | `86c5f6065bef` ／ 140,009 ／ 1190 | `739a7daf533b` | R-04×1 |
| 528 | OVW-511 | `results/_v4_gA1_experiment_outline_2026_09_22.md` | `0f94a003dbb9` ／ 7,839 ／ 91 | `0f94a003dbb9` ／ 7,839 ／ 91 | `739a7daf533b` | R-04×1 |
| 529 | OVW-511 | `results/_v4_gA1_terminology_draft_2026_09_22.md` | `ca4bad1a0f19` ／ 9,818 ／ 84 | `039b075d4d92` ／ 9,820 ／ 84 | `739a7daf533b` | R-04×1 |
| 530 | OVW-511 | `results/_v4_gA3_seeds_judgment_draft_2026_09_22.md` | `aa3da939a79c` ／ 19,774 ／ 147 | `aa3da939a79c` ／ 19,774 ／ 147 | `739a7daf533b` | R-04×1 |
| 531 | OVW-511 | `results/_v4_group_b_17letters_judgment_draft_2026_09_22.md` | `38246f705a64` ／ 24,824 ／ 176 | `38246f705a64` ／ 24,824 ／ 176 | `739a7daf533b` | R-04×1 |
| 532 | OVW-511 | `results/_v4_group_b_explore_subs_integration_2026_09_22.md` | `1d66f37a9e8e` ／ 20,518 ／ 201 | `27af641910d2` ／ 20,534 ／ 201 | `739a7daf533b` | R-04×1 |
| 533 | OVW-511 | `results/_v4_maindir_cleanup_manifest_2026_09_24.md` | `c096f23a2f79` ／ 19,069 ／ 288 | `97f162c94d17` ／ 19,108 ／ 288 | `739a7daf533b` | R-04×2 |
| 534 | OVW-511 | `results/_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | `22d2c1d03065` ／ 27,853 ／ 360 | `5fcbf0934ef7` ／ 27,913 ／ 360 | `739a7daf533b` | R-04×2 |
| 535 | OVW-511 | `results/_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `461124b1c8bb` ／ 31,549 ／ 424 | `dab9a1c18a9e` ／ 31,691 ／ 424 | `739a7daf533b` | R-04×1 |
| 536 | OVW-511 | `results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `6fc3463e11c1` ／ 37,582 ／ 388 | `0284c0035f1a` ／ 37,653 ／ 388 | `739a7daf533b` | R-04×12 |
| 537 | OVW-511 | `results/_v4_maindir_count_monitor_2026_09_27.md` | `42dc9efce725` ／ 15,304 ／ 271 | `cdc09278eb09` ／ 15,321 ／ 271 | `739a7daf533b` | R-04×4 |
| 538 | OVW-511 | `results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | `de3da25bc7a8` ／ 53,583 ／ 1083 | `de3da25bc7a8` ／ 53,583 ／ 1083 | `739a7daf533b` | R-04×1 |
| 539 | OVW-511 | `results/_v4_trae_remaining_audit_2026_09_28.md` | `9f37ef2ba0db` ／ 39,668 ／ 461 | `31cde3f8fec0` ／ 39,697 ／ 461 | `739a7daf533b` | R-04×8 |
| 540 | OVW-511 | `results/_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | `4a2cb20f948f` ／ 33,786 ／ 388 | `359ca8e92cbf` ／ 33,813 ／ 388 | `739a7daf533b` | R-04×5 |
| 541 | OVW-511 | `results/_v5_clearance_mr11_doc_calibration_2026_09_29.md` | `6cab8f3ed1e8` ／ 14,986 ／ 166 | `6cab8f3ed1e8` ／ 14,986 ／ 166 | `739a7daf533b` | R-02×3 |
| 542 | OVW-511 | `results/_v5_clearance_o15_ready_pack_2026_09_29.md` | `1b145eded648` ／ 48,972 ／ 500 | `1b145eded648` ／ 48,972 ／ 500 | `739a7daf533b` | R-02×1 |
| 543 | OVW-511 | `results/_v5_confirm_b11_decisions_register_2026_09_29.md` | `17f590a839a5` ／ 12,302 ／ 173 | `17f590a839a5` ／ 12,302 ／ 173 | `739a7daf533b` | R-02×6·R-04×1 |
| 544 | OVW-511 | `results/_v5_confirm_b3_decisions_register_2026_09_29.md` | `3f455a73da77` ／ 34,025 ／ 335 | `3f455a73da77` ／ 34,025 ／ 335 | `739a7daf533b` | R-04×5 |
| 545 | OVW-511 | `results/_v5_confirm_b8_decisions_register_2026_09_29.md` | `0778f4b25bf6` ／ 15,118 ／ 145 | `7ade25305d6f` ／ 15,116 ／ 145 | `739a7daf533b` | R-02×1·R-04×3 |
| 546 | OVW-511 | `results/_v5_handover_guide_project_initiation_2026_10_12.md` | `fc1fac3d9898` ／ 5,582 ／ 67 | `fc1fac3d9898` ／ 5,582 ／ 67 | `739a7daf533b` | R-04×1 |
| 547 | OVW-511 | `results/_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `6c291f7574b6` ／ 31,437 ／ 336 | `6c291f7574b6` ／ 31,437 ／ 336 | `739a7daf533b` | R-02×2 |
| 548 | OVW-511 | `results/_v5_item21_verdict_2026_09_28.md` | `6ee482285e78` ／ 28,163 ／ 340 | `6ee482285e78` ／ 28,163 ／ 340 | `739a7daf533b` | R-02×2 |
| 549 | OVW-511 | `results/_v5_paper_remedy_r1_pledge_2026_09_29.md` | `911e88d52b64` ／ 47,737 ／ 599 | `71bdd060801f` ／ 47,790 ／ 599 | `739a7daf533b` | R-02×2·R-04×2 |
| 550 | OVW-511 | `results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | `b38a5f82e104` ／ 34,651 ／ 337 | `714b2bf2648b` ／ 34,673 ／ 337 | `739a7daf533b` | R-02×4·R-04×5 |
| 551 | OVW-511 | `results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | `82c6c5530d55` ／ 102,393 ／ 798 | `00c1b6c49015` ／ 102,414 ／ 798 | `739a7daf533b` | R-02×1 |
| 552 | OVW-511 | `results/_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | `ce300c1883d8` ／ 48,514 ／ 414 | `0e56b13c733f` ／ 48,543 ／ 414 | `739a7daf533b` | R-02×1 |
| 553 | OVW-511 | `results/_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | `5644406f7355` ／ 150,967 ／ 785 | `5644406f7355` ／ 150,967 ／ 785 | `739a7daf533b` | R-02×2·R-04×1 |
| 554 | OVW-511 | `results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `90617176e1ae` ／ 128,834 ／ 810 | `06d65401458f` ／ 128,828 ／ 810 | `739a7daf533b` | R-02×5·R-04×24 |
| 555 | OVW-511 | `results/_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | `8e40c48ca35d` ／ 603,712 ／ 3256 | `8c2cf5065dfb` ／ 603,753 ／ 3256 | `739a7daf533b` | R-01×2·R-02×19·R-03×1·R-04×31 |
| 556 | OVW-511 | `results/_v5_t1_decisions_register_2026_09_29.md` | `a2dd2d65b1ec` ／ 31,336 ／ 397 | `643d3aea5cc6` ／ 31,334 ／ 397 | `739a7daf533b` | R-02×1 |
| 557 | OVW-511 | `results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | `969470464033` ／ 14,626 ／ 193 | `969470464033` ／ 14,626 ／ 193 | `739a7daf533b` | R-02×1·R-04×1 |
| 558 | OVW-511 | `results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | `2f115c9a6662` ／ 22,187 ／ 176 | `2f115c9a6662` ／ 22,187 ／ 176 | `739a7daf533b` | R-04×1 |
| 559 | OVW-511 | `results/_vk_current_counting_face_2026_10_10.md` | `505d7e1dd421` ／ 24,755 ／ 246 | `1228f05a235e` ／ 24,795 ／ 246 | `739a7daf533b` | — |
| 560 | OVW-511 | `results/_vk_face_category_erratum_2026_10_11.md` | `7801775634bd` ／ 17,333 ／ 179 | `06662bff1840` ／ 17,373 ／ 179 | `739a7daf533b` | — |
| 561 | OVW-511 | `results/_zero_reading_judgment_2026_10_10.md` | `a07774dbcb71` ／ 27,804 ／ 272 | `f49d7e4235f7` ／ 27,824 ／ 272 | `739a7daf533b` | — |
| 562 | OVW-511 | `results/_zone_balance_inventory_2026_10_13.md` | `48ea4e6774c3` ／ 725,689 ／ 6208 | `48ea4e6774c3` ／ 725,689 ／ 6208 | `739a7daf533b` | R-04×30 |
| 563 | OVW-511 | `results/deposon_3risk_v0_fixes_2026_09_11.json` | `65cc3eaa19f6` ／ 8,352 ／ 241 | `65cc3eaa19f6` ／ 8,352 ／ 241 | `739a7daf533b` | R-02×3·R-04×1 |
| 564 | OVW-511 | `results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `8df74e7345ab` ／ 13,568 ／ 429 | `8df74e7345ab` ／ 13,568 ／ 429 | `739a7daf533b` | R-02×1·R-04×1 |
| 565 | OVW-511 | `results/deposon_pa_d1_d3_2026_09_15.json` | `17fb4ef17572` ／ 15,622 ／ 469 | `17fb4ef17572` ／ 15,622 ／ 469 | `739a7daf533b` | R-02×3·R-04×3 |
| 566 | OVW-511 | `results/deposon_pc_d1_d3_2026_09_15.json` | `98b60214583e` ／ 20,422 ／ 587 | `98b60214583e` ／ 20,422 ／ 587 | `739a7daf533b` | R-02×2·R-04×3 |
| 567 | OVW-511 | `results/deposon_pe_d1_d3_2026_09_15.json` | `6f4b25cca87b` ／ 17,091 ／ 432 | `6f4b25cca87b` ／ 17,091 ／ 432 | `739a7daf533b` | R-02×1·R-04×1 |
| 568 | OVW-511 | `results/deposon_pf_d1_full_9m5c_2026_09_15.json` | `096c001f92ca` ／ 33,741 ／ 1046 | `8ab58d68ec02` ／ 33,837 ／ 1046 | `739a7daf533b` | R-02×1·R-04×2 |
| 569 | OVW-511 | `results/deposon_pf_implementation_2026_09_11.json` | `3bf750dc3f8b` ／ 27,272 ／ 407 | `9030ad73b4ad` ／ 27,337 ／ 407 | `739a7daf533b` | R-02×6·R-04×1 |
| 570 | OVW-511 | `results/deposon_pg_v01_9m60c_2026_09_15.json` | `ca0ffb87f97b` ／ 11,526 ／ 404 | `ca0ffb87f97b` ／ 11,526 ／ 404 | `739a7daf533b` | R-02×2·R-04×3 |
| 571 | OVW-511 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `5d4875397a9f` ／ 17,738 ／ 604 | `5d4875397a9f` ／ 17,738 ／ 604 | `739a7daf533b` | R-02×1·R-04×1 |
| 572 | OVW-511 | `results/deposon_v3_v7_summary_2026_09_11.json` | `289e897f3a07` ／ 25,042 ／ 380 | `4e31f9167442` ／ 25,055 ／ 380 | `739a7daf533b` | R-02×1·R-04×1 |
| 573 | OVW-511 | `results/skill_d_p_f_observer_result_2026_09_11.json` | `b83ad0fd3517` ／ 11,018 ／ 314 | `b83ad0fd3517` ／ 11,018 ／ 314 | `739a7daf533b` | R-02×1·R-04×2 |
| 574 | OVW-511 | `tmp_movedout_2026_09_28/_cleanup_classify_2026_09_28.py` | `fc27f4f3a1bf` ／ 3,224 ／ 93 | `9e692ba895ed` ／ 3,232 ／ 93 | `739a7daf533b` | — |
| 575 | OVW-511 | `tmp_movedout_2026_09_28/_cleanup_classify_out_2026_09_28.txt` | `e9e63476d717` ／ 10,267 ／ 144 | `dd447d4ca5c2` ／ 11,347 ／ 144 | `739a7daf533b` | — |
| 576 | OVW-511 | `tmp_movedout_2026_09_28/_cleanup_probe_2026_09_28.py` | `ca9dc8aefe34` ／ 2,548 ／ 73 | `dd8a35858a6b` ／ 2,556 ／ 73 | `739a7daf533b` | — |
| 577 | OVW-511 | `tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt` | `c4c89193db52` ／ 12,359 ／ 139 | `75429a79bae4` ／ 12,367 ／ 139 | `739a7daf533b` | R-04×1 |
| 578 | OVW-511 | `tmp_movedout_2026_09_28/_cleanup_resolve_2026_09_28.py` | `4e3fef8ea6ec` ／ 2,707 ／ 73 | `dc578941a2df` ／ 2,735 ／ 73 | `739a7daf533b` | — |
| 579 | OVW-511 | `tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py` | `0020de27f803` ／ 3,221 ／ 84 | `4fe0eef8bd7d` ／ 3,229 ／ 84 | `739a7daf533b` | — |
| 580 | OVW-511 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_asset_recount_2026_09_30.md` | `5274aee17142` ／ 9,396 ／ 157 | `8af3fd8a08db` ／ 9,441 ／ 157 | `739a7daf533b` | — |
| 581 | OVW-511 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_letter_review_bob_w3_commission_2026_09_30.md` | `d2163dca73e5` ／ 10,295 ／ 100 | `f038e15fe156` ／ 10,286 ／ 100 | `739a7daf533b` | — |
| 582 | OVW-511 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_r3_anchor_retrieval_2026_09_29.md` | `c634e087d745` ／ 23,066 ／ 210 | `cf395fdb3282` ／ 23,023 ／ 210 | `739a7daf533b` | — |
| 583 | OVW-511 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b17_three_caliber_fixation_2026_09_29.md` | `203d3ee799ba` ／ 19,678 ／ 229 | `aa13f2945e85` ／ 19,709 ／ 229 | `739a7daf533b` | — |
| 584 | OVW-511 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md` | `d908c85c4da4` ／ 18,510 ／ 171 | `a2989b1b5b26` ／ 18,514 ／ 171 | `739a7daf533b` | — |
| 585 | OVW-511 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `2a9a263e2ffc` ／ 5,055 ／ 81 | `2a9a263e2ffc` ／ 5,055 ／ 81 | `739a7daf533b` | R-02×1·R-04×1 |
| 586 | OVW-511 | `verifier/handoff/P_F_PREDECISION_2026_09_09.json` | `f9beac73eef9` ／ 3,690 ／ 88 | `f9beac73eef9` ／ 3,690 ／ 88 | `739a7daf533b` | R-02×2·R-04×1 |
| 587 | OVW-511 | `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` | `81afead5bd49` ／ 12,504 ／ 253 | `81afead5bd49` ／ 12,504 ／ 253 | `739a7daf533b` | R-02×1·R-04×1 |
| 588 | OVW-511 | `verifier/v36/check.sh` | `23b9f6d2bc40` ／ 975 ／ 10 | `23b9f6d2bc40` ／ 975 ／ 10 | `739a7daf533b` | R-01×1 |
| 589 | OVW-511 | `verifier/v41/check.sh` | `4f3916a0596d` ／ 1,694 ／ 20 | `4f3916a0596d` ／ 1,694 ／ 20 | `739a7daf533b` | R-01×1 |
| 590 | OVW-511 | `volcengine_glm_latest_30cells_v2_runner_2026_09_10.py` | `4ffa7c767bef` ／ 20,710 ／ 515 | `61706e9cbcf5` ／ 20,751 ／ 515 | `739a7daf533b` | R-02×1·R-04×1 |

# R-A-6 ｜ 序 2-d 组A 2 件覆盖 ＋ 组B 3 件 0 覆盖（裁八·裁九）

- 组A 2 件随覆盖面同序覆盖毕（见 R-A-5 表「（组A）」行）：`results/_d1_backfill_intake_verdict_2026_10_01.md` ｜ `results/_mini_round_5_decisions_register_2026_10_01.md`
- 组B 3 件 0 覆盖之终态确认：

| 仓内路径 | 基线 SHA-12 | 终态 SHA-12 | 0 覆盖 |
|---|---|---|:-:|
| `results/_s4prime_readings_runner_2026_10_11.py` | `1ea332165702` | `1ea332165702` | ✅ |
| `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | `93d13cd8a5fa` | `93d13cd8a5fa` | ✅ |
| `results/_v3_recheck_05_executor_2026_09_28.py` | `01b8e0ccd990` | `01b8e0ccd990` | ✅ |

# R-A-7 ｜ 序 3 遗留面 413 件全留（裁十二 · 远端 0 任何动作）

- 终态全树之根层面（非 `_repo_mirror/` 前缀）＝ **413** blobs；与序 0 基线树（`7294fa49edac` · 4cd417b3 之树）逐件对照：sha 差 **0**（期望 0）⇒ 全留 0 动作成立
- 前缀面 `.gitignore` 终态 ＝ `4fc0d746af9d` ／ 105 B（105 B 止血面存续）

# R-A-8 ｜ 执行时点之 live HEAD

- 序 0 执行基线：`4cd417b32e5d4ae05de95825e2d13d602b8b928a`（commit 时间 2026-10-18T05:38:54Z · tree `7294fa49edac` · truncated=False · blobs 3,447 ＝ 前缀 3,034 ＋ 遗留 413；172/209/514 三面逐条重核 0 漂移）
- 终态 live HEAD：`739a7daf533b6ead320667d924ab0884c9614edc`

# R-A-9 ｜ 凭据面自证（R4）

- PAT 仅走进程环境变量，0 落盘、0 打印、0 入 commit／message／文稿／JSON；本回执落盘前经密钥族正则（带长度锚）自检 **0 命中** ⇒ **回执 0 含任何凭据片段**
- 门禁词族同语义扫描本回执 **0 命中**（本回执自体已过 R-01～R-11 同族之门禁口径）

# R-A-10 ｜ 归档区只读核（裁十四 · ⛔ 0 写 0 删）

- 21 件「仓内副本与远端删前 blob 不一致」面：归档区**内容相符副本 20/21** ｜ 无相符副本 **1** 件：
  - `results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md`（删前 `3ef2e8075f1b`）
- 81 件「仓内双区均无副本」面：归档区**内容相符副本 75/81** ｜ 无相符副本 **6** 件：
  - `results/_archive_2026_09_20/_audit_temp_inspect_minimax_m3.py.bak`（删前 `96bb0a05de8b`）
  - `results/_archive_2026_09_20/_audit_temp_inspect_workers.py.bak`（删前 `843afd0baa41`）
  - `results/_archive_2026_09_20/_audit_temp_stage1_tra_breakdown.py.bak`（删前 `e96ad684b886`）
  - `results/_archive_2026_09_20/_openrouter_emb_runner.bak.note`（删前 `af0744ae0a65`）
  - `results/_archive_2026_09_20/_tmp_probe_archive`（删前 `4edd37d18fbc`）
  - `results/_v4_tmp_cleanup_2026_09_28.md`（删前 `aa3a94399724`）
- 口径：归档区全递归索引 40,121 件 · 按 basename 定位后以删前 blob git SHA-1 逐字节比对；⛔ 0 断言无相符副本者即真缺件（或落于别径别介质）· ⛔ 0 判任何回执失实；核验全程只读（0 写 0 删）

---

## 附 ｜ 序 0 三面重核汇总（R-SSC-2／R-SSC-3 之执行面）

- 面① 172：在位且 sha 相符 172/172 ｜ 面② 209：前缀下缺席 209/209 ｜ 面③ 514：在位且远端 sha 相符 514/514 ｜ 遗留面 413 计数相符
- 去重对账：70 ⊂ 172（先拉后删之前置链）；v0.4 之 302 件次面 ＝ 前轮已毕（本轮 0 重删）；三面交集 0 新增
- 序 4 域级回填 ＝ 本地仓面 · 非受托方面（裁十五）⇒ 本棒 0 触碰

*回执毕 ｜ KIMI（受托方 · 执行棒）｜ 2026-10-18 ｜ 0 代裁 · 0 闭 KD · 0 落五终判 · 0 密钥明文 · 0 PAT 片段*
