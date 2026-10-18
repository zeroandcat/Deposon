# 仓面全量文件夹整理之盘面编目（成果清单 v2.0 之底本）

> 📌 **状态栏**：📋 **全量清点＋归类＋编目**（**0 物理移动／0 重命名／0 删除／0 改路径**）｜🟢 **实测域 ＝ `D:\私人资料\deposon-repo` 全仓（含 `.mavis`/`.tmp`/`.trae` 等隐藏面）**｜⛔ **禁触区 `D:\私人资料\_non_upload_local_archive` ＝ 0 读 0 写 0 列目录**｜⚠ **另二区（`deposon-sub`／`Deposon_v1_2_0_交付包`）仅列存在性与件数，0 深读**｜⛔ **0 立成果清单、0 出收尾桶**（二者为后续棒）｜⛔ 0 回改任何既有件一字｜⛔ 0 网络／0 skill／0 LLM／0 API key／0 读 `.env`

---

## §0 一句话结论

deposon-repo 实测 **2557 件 / 89,904,628 B / 15 目录 ＋ 顶层 73 件**；逐件 SHA-12・bytes・mtime・BOM・CR 计数**全量实测完毕**（0 件测量失败）；漂移面（近 72h）**851 件**；同名异名冲突 **9 组**；BOM **122 件**、CR>0 **465 件**；**未核得 10 类**——本件**仅为编目**，⛔ 0 立清单、0 出桶、0 移动任何一件。

---

## §1 目录级汇总表（**实测 · 全量**）

| # | 目录 | 件数 | 总 bytes | 最早 mtime | 最新 mtime | 归属面判定 |
| :-:|:--|:-:|-:|:--|:--|:--|
| 1 | .mavis/ | 4 | 992 | 2026-09-24 22:23:52 | 2026-09-24 22:30:25 | 运行时面 |
| 2 | .tmp/ | 581 | 23,532,678 | 2026-09-24 18:50:23 | 2026-10-11 23:53:15 | 草稿/临时面 |
| 3 | .trae/ | 2 | 34,781 | 2026-09-09 14:14:27 | 2026-09-09 14:14:27 | 第三方件面 |
| 4 | attacks/ | 4 | 12,922 | 2026-09-01 11:19:18 | 2026-09-04 13:11:07 | 攻击/鲁棒性面 |
| 5 | corpus/ | 43 | 951,375 | 1979-11-30 00:00:00 | 2026-10-09 13:39:49 | 语料面 |
| 6 | deposon_team/ | 86 | 1,446,106 | 2026-09-11 17:05:38 | 2026-10-12 01:34:23 | 团队件面（agent/插件执行体） |
| 7 | docs/ | 135 | 2,383,514 | 2026-08-22 21:07:01 | 2026-10-01 09:51:11 | 文档面（SPEC/报告/模板） |
| 8 | letters/ | 97 | 2,637,062 | 2026-09-11 16:30:23 | 2026-10-12 01:34:03 | 委托·回函面 |
| 9 | paper/ | 5 | 145,087 | 2026-08-29 15:43:30 | 2026-09-20 17:11:14 | 论文面 |
| 10 | results/ | 1341 | 56,673,729 | 2026-08-22 21:07:01 | 2026-10-12 01:39:16 | 成果件面（读数/终判/登记/勘误） |
| 11 | reviews/ | 32 | 376,244 | 2026-08-23 21:40:22 | 2026-08-30 04:02:12 | 评审面 |
| 12 | scripts/ | 10 | 148,821 | 2026-09-10 16:15:10 | 2026-09-16 11:01:12 | 脚本面 |
| 13 | tests/ | 23 | 212,514 | 2026-08-23 09:40:33 | 2026-09-01 16:35:59 | 测试面 |
| 14 | tools/ | 5 | 61,516 | 2026-08-30 20:46:55 | 2026-09-10 14:45:46 | 工具面 |
| 15 | verifier/ | 116 | 265,425 | 2026-08-23 10:27:21 | 2026-09-22 11:02:01 | 验证面 |
| 16 | （仓根・顶层散件） | 73 | 1,021,862 | 2026-08-22 21:07:01 | 2026-10-10 20:18:55 | 顶层执行体＋总纲面 |
| — | **合计** | **2557** | **89,904,628** | **1979-11-30 00:00:00** | **2026-10-12 01:39:16** | — |

📌 **最早 mtime 异常读数**：`corpus/` 内一件 mtime ＝ **1979-11-30 00:00:00**（早于全仓任何其他件）⇒ 属**异常时间戳**，⛔ **0 断言其成因**（见 §4 未核得 U-08）。

### §1-1 另二区之存在性与件数（**仅元数据 · 0 深读 · 0 改写**）

| 区 | 存在 | 文件件数 | 目录数 | 总 bytes | 最早 mtime | 最新 mtime | 顶层子目录 |
|:--|:-:|-:|-:|-:|:--|:--|:--|
| `D:\私人资料\deposon-sub` | ✅ TRUE | **517** | 42 | 35,047,715 | 2026-08-22 21:07:01 | 2026-09-30 19:28:23 | `.trae`, `deposon_team`, `docs`, `results`, `tmp_movedout_2026_09_28`, `tmp_movedout_2026_09_29`, `tmp_movedout_2026_10_01`, `tmp_movedout_2026_10_09` |
| `D:\私人资料\Deposon_v1_2_0_交付包` | ✅ TRUE | **23** | 2 | 3,243,552 | 2026-08-22 00:16:19 | 2026-08-22 14:42:01 | `output`, `upload` |
| `D:\私人资料\_non_upload_local_archive` | ⛔ **未核得** | **未核得** | 未核得 | 未核得 | 未核得 | 未核得 | ⛔ **禁触区：0 读 0 写 0 列目录** |

---

## §2 逐件编目表

> 列：**相对路径 ／ SHA-12 ／ bytes ／ mtime ／ 类别判定**。📌 类别为**文件名＋路径＋扩展名驱动**之机检标签（规则见 §3），⛔ **0 语义判定、0 强行归一**（冲突者并列标注）。

### §2-2 results/（1341 件 / 56,673,729 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `results\__pycache__\_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | `F4194CC5A522` | 43685 | 2026-10-11 16:51:05 | 读数/结果＋成果件面 |
| `results\__pycache__\_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc` | `9FC3E2152679` | 44952 | 2026-10-11 20:32:37 | 读数/结果＋成果件面 |
| `results\__pycache__\_t1_exp2_executor_2026_10_09.cpython-314.pyc` | `346595DF084C` | 87302 | 2026-10-09 22:50:42 | 读数/结果＋成果件面 |
| `results\__pycache__\_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | `08D4B51C45C6` | 67081 | 2026-10-09 17:34:40 | 读数/结果＋成果件面 |
| `results\__pycache__\_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | `E7AB1ADBF898` | 69630 | 2026-10-09 17:43:14 | 读数/结果＋成果件面 |
| `results\_149_face_effect_disposal_2026_10_10.md` | `E7C1232DF138` | 24295 | 2026-10-10 01:15:42 | 读数/结果＋成果件面 |
| `results\_9model_full_merge_from_4workers_2026_10_09.json` | `32AA0618A9D7` | 19337 | 2026-10-09 12:08:37 | 读数/结果＋成果件面 |
| `results\_9model_merge_disposition_register_2026_10_09.md` | `455277298212` | 11651 | 2026-10-09 12:09:24 | 登记＋读数/结果＋成果件面 |
| `results\_a02_excluded_items_idx_collection_2026_10_10.md` | `03407E0B6662` | 39565 | 2026-10-10 18:40:34 | 读数/结果＋成果件面 |
| `results\_af_entity_definition_draft_2026_10_10.md` | `97654060D86E` | 25257 | 2026-10-10 13:24:57 | 读数/结果＋成果件面 |
| `results\_alt_delib_pkg3_two_judgments_2026_10_10.md` | `3F52709A48E8` | 38032 | 2026-10-10 01:06:09 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_archive_2026_09_20\_archive_manifest_2026_09_18.json` | `A729875C0C67` | 4712 | 2026-09-18 22:04:18 | 读数/结果＋成果件面 |
| `results\_archive_2026_09_20\_archive_manifest_2026_09_20.json` | `4DD89950BF11` | 35682 | 2026-09-20 11:07:34 | 读数/结果＋成果件面 |
| `results\_archive_2026_09_21\_archive_manifest_2026_09_21.json` | `33FE31633DA8` | 17353 | 2026-09-21 19:55:39 | 读数/结果＋成果件面 |
| `results\_archive_2026_09_24\_final_verify.py` | `31A5D44497F1` | 2307 | 2026-09-23 15:34:04 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\_final_verify.py._moved_20260924_1830` | `DB4428293040` | 2279 | 2026-09-24 13:37:46 | 核查＋读数/结果＋成果件面 |
| `results\_archive_2026_09_24\_inspect_captions.py` | `DFB02ADE1474` | 591 | 2026-09-10 17:31:00 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\_l11_run1.json` | `20B0E13064F8` | 12143 | 2026-09-24 13:34:09 | 读数/结果＋成果件面 |
| `results\_archive_2026_09_24\_l13_latency_test.py` | `DAE238354342` | 2954 | 2026-09-24 14:03:31 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\_l14_checkpoint.json` | `91B582672B49` | 10963 | 2026-09-24 14:56:40 | 核查＋读数/结果＋成果件面 |
| `results\_archive_2026_09_24\_l14_records.json` | `8F6FCF027149` | 50957 | 2026-09-24 15:34:57 | 读数/结果＋成果件面 |
| `results\_archive_2026_09_24\_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | `07CA9EE8E1BB` | 113508 | 2026-09-22 16:00:10 | 读数/结果＋成果件面 |
| `results\_archive_2026_09_24\_verify_worker_c.py` | `CC578C46B332` | 1155 | 2026-09-10 21:27:55 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\_volc_22cap_emb.py` | `15904ECAE629` | 11105 | 2026-09-10 17:36:26 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\_worker_openrouter_rag_run.py` | `4458CCF3D64A` | 24113 | 2026-09-16 11:01:12 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\l14_runner_v2.py` | `ACF1CD6CCBD4` | 23056 | 2026-09-24 15:07:26 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\l14_runner_v2_r1_atomic_2026_09_29.py` | `B1923528AB84` | 25892 | 2026-09-29 11:12:41 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\l14_small_batch.py` | `0659C947BEC1` | 21784 | 2026-09-24 14:51:45 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_2026_09_24\latency_test.py` | `FD9FD98785E1` | 617 | 2026-09-24 14:44:18 | 读数/结果＋执行体＋成果件面 |
| `results\_archive_and_b6_inquiry_register_2026_10_08.md` | `1D08A780A715` | 21163 | 2026-10-08 17:12:12 | 登记＋读数/结果＋成果件面 |
| `results\_archive_cleanup_extension_2026_09_28.md` | `889D15247607` | 28774 | 2026-09-28 20:03:52 | 读数/结果＋成果件面 |
| `results\_archive_cleanup_non_upload_2026_09_28.md` | `34F2C63306B8` | 56714 | 2026-09-28 19:09:12 | 读数/结果＋成果件面 |
| `results\_archive_ledger_rectification_register_2026_10_09.md` | `99359733EEF1` | 20933 | 2026-10-09 09:31:31 | 登记＋读数/结果＋成果件面 |
| `results\_archive_manifest_deposon_sub_2026_09_23.json` | `B34B9F7BDFB7` | 52153 | 2026-09-23 15:11:29 | 读数/结果＋成果件面 |
| `results\_archive_manifest_non_upload_2026_09_23.json` | `B899103853CA` | 148690 | 2026-09-23 15:11:35 | 读数/结果＋成果件面 |
| `results\_archive_manifest_non_upload_v2_2026_09_28.json` | `84EEF669234B` | 236651 | 2026-09-28 19:02:06 | 读数/结果＋成果件面 |
| `results\_archive_manifest_non_upload_v3_2026_09_28.json` | `A2E4C5A9B713` | 204256 | 2026-09-28 20:00:44 | 读数/结果＋成果件面 |
| `results\_archive_moveout_register_2026_09_29.md` | `56639E57AC06` | 13363 | 2026-09-29 21:20:14 | 登记＋读数/结果＋成果件面 |
| `results\_asset_identity_reconciliation_2026_10_01.md` | `0D22797F084F` | 28291 | 2026-10-01 11:27:03 | 读数/结果＋成果件面 |
| `results\_axis1_three_recomputations_2026_10_11.md` | `8DE23F7D7384` | 29938 | 2026-10-11 17:26:24 | 核查＋读数/结果＋成果件面 |
| `results\_b_coincidence_closeout_register_2026_10_10.md` | `51CE7B49C423` | 31451 | 2026-10-10 13:32:32 | 登记＋读数/结果＋成果件面 |
| `results\_b_coincidence_disposition_judgment_2026_10_10.md` | `7FF80485955C` | 42838 | 2026-10-10 13:17:14 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_b01_new_key_classification_2026_10_10.md` | `2DDFECF6201C` | 38669 | 2026-10-10 21:31:57 | 读数/结果＋成果件面 |
| `results\_b01_new_key_residue_judgment_2026_10_10.md` | `345517455DCF` | 41984 | 2026-10-10 23:13:30 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_b01_p_counting_recompute_2026_10_10.md` | `3511CF21A869` | 22104 | 2026-10-10 20:00:44 | 核查＋读数/结果＋成果件面 |
| `results\_b01_recompute_authorization_supplement_2026_10_11.md` | `03A66D4C663A` | 18454 | 2026-10-11 00:14:37 | 核查＋读数/结果＋成果件面 |
| `results\_b01_recompute_sec4_2_erratum_2026_10_10.md` | `FAC3308FB295` | 16441 | 2026-10-10 21:33:26 | 勘误＋核查＋读数/结果＋成果件面 |
| `results\_b14_audit_f2f3_closure_register_2026_10_11.md` | `9D4A3D6DDF88` | 29620 | 2026-10-11 14:36:37 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_b14_vk_evidence_audit_2026_10_10.md` | `89F17297F1F5` | 33586 | 2026-10-11 00:07:21 | 核查＋读数/结果＋成果件面 |
| `results\_backfill_rule_execution_register_2026_10_08.md` | `3A7F8E203B28` | 27267 | 2026-10-08 16:52:40 | 登记＋读数/结果＋成果件面 |
| `results\_backfill_rule_final_2026_10_09.md` | `3E97D5286760` | 34602 | 2026-10-09 09:26:50 | 读数/结果＋成果件面 |
| `results\_backfill_rule_vk_closeout_2026_10_08.md` | `20F5835D47D2` | 26890 | 2026-10-08 17:02:40 | 读数/结果＋成果件面 |
| `results\_batch3_receipt_kimi_2026_10_01.md` | `8C2CB4C6A937` | 2238 | 2026-10-01 00:07:36 | 读数/结果＋成果件面 |
| `results\_bayesian_baseline_design_2026_10_10.md` | `7E181A167702` | 29783 | 2026-10-10 02:45:24 | 读数/结果＋成果件面 |
| `results\_beta_formal_run_exec_register_2026_10_09.md` | `2E5F080EAB6C` | 16811 | 2026-10-09 23:32:35 | 登记＋读数/结果＋成果件面 |
| `results\_beta_formal_run_result_2026_10_09.json` | `A5A918FD9861` | 103691 | 2026-10-09 23:30:08 | 读数/结果＋成果件面 |
| `results\_blade_caliber_b8_judgment_2026_10_10.md` | `E189D6EB63D9` | 28738 | 2026-10-10 09:51:16 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_c_component4_d2d3_gap_judgment_2026_10_11.md` | `08D3BFD82235` | 27490 | 2026-10-11 00:15:45 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_c_component4_three_items_judgment_2026_10_11.md` | `FD0094E2F865` | 41580 | 2026-10-11 00:26:46 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_c_reading_recompute_2026_10_09.md` | `95D7D23D24FD` | 21006 | 2026-10-09 09:55:37 | 核查＋读数/结果＋成果件面 |
| `results\_c1c4_ab_alpha_pilot_result_2026_10_09.json` | `BC7C35707B78` | 104225 | 2026-10-09 22:55:04 | 读数/结果＋成果件面 |
| `results\_c1c4_ab_beta_pilot_result_2026_10_09.json` | `FD72EBF836E1` | 109879 | 2026-10-09 22:59:59 | 读数/结果＋成果件面 |
| `results\_c1c4_ab_pilot_comparison_2026_10_09.md` | `BDD2A1D7E6C5` | 15390 | 2026-10-09 23:02:14 | 读数/结果＋成果件面 |
| `results\_c1c4_input_gap_fill_plan_2026_10_09.md` | `9F5675633E03` | 35635 | 2026-10-09 17:27:41 | 读数/结果＋成果件面 |
| `results\_c2_criterion_third_tier_draft_2026_10_11.md` | `844179898102` | 26713 | 2026-10-11 17:36:57 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_c4_math_corrections_downstream_erratum_2026_10_10.md` | `643CB9E249F7` | 28886 | 2026-10-10 18:18:42 | 勘误＋读数/结果＋成果件面 |
| `results\_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | `4C369CB86DB4` | 31607 | 2026-10-10 21:20:30 | 勘误＋读数/结果＋成果件面 |
| `results\_c4_reply_intake_acceptance_register_2026_10_01.md` | `E1E8CB7B9DB4` | 33728 | 2026-10-10 21:19:00 | 登记＋回函＋读数/结果＋成果件面 |
| `results\_c4_theory_source_caliber_correction_2026_09_30.md` | `61B139EFD0EF` | 25022 | 2026-10-01 09:18:38 | 勘误＋读数/结果＋成果件面 |
| `results\_c4_unblock_reply_independent_review_2026_10_10.md` | `2ECD866E2468` | 27364 | 2026-10-10 18:13:09 | 回函＋评审＋读数/结果＋成果件面 |
| `results\_c8_c2_disposition_register_2026_10_11.md` | `FB816C572779` | 30956 | 2026-10-11 16:53:47 | 登记＋读数/结果＋成果件面 |
| `results\_carrier_qid_disposition_2026_10_11.md` | `7D74D5A4D81E` | 3406 | 2026-10-11 23:22:17 | 读数/结果＋成果件面 |
| `results\_charlie_delivery_register_2026_10_08.md` | `6F4BF31276F5` | 10733 | 2026-10-08 15:52:36 | 登记＋读数/结果＋成果件面 |
| `results\_chd_construction_domain_declaration_draft_2026_10_10.md` | `17CF0D59CD7B` | 34948 | 2026-10-10 23:35:41 | 读数/结果＋成果件面 |
| `results\_ci_bc_lines_ci_collection_2026_10_09.md` | `6DB4D0FB2452` | 24769 | 2026-10-09 16:47:04 | 读数/结果＋成果件面 |
| `results\_ci_bc_scope_estimand_judgments_2026_10_09.md` | `D76BA2297D0D` | 37682 | 2026-10-09 17:34:04 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_ci_degradation_binding_form_a_register_2026_10_09.md` | `424730B5123D` | 26104 | 2026-10-09 17:32:42 | 登记＋读数/结果＋成果件面 |
| `results\_ci_detail_decoupling_degradation_baseline_2026_10_09.md` | `56B62ED5AB74` | 20973 | 2026-10-09 15:53:38 | 读数/结果＋成果件面 |
| `results\_ci_four_items_effectiveness_register_2026_10_09.md` | `4AB2464A266E` | 29365 | 2026-10-09 17:14:39 | 登记＋读数/结果＋成果件面 |
| `results\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.json` | `F729A6A03A9E` | 23272 | 2026-10-09 17:43:45 | 读数/结果＋成果件面 |
| `results\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md` | `BEE0F1F0BDB2` | 29709 | 2026-10-09 17:48:22 | 读数/结果＋成果件面 |
| `results\_ci_line_establishment_2026_10_09.md` | `329C1C5E91D1` | 28262 | 2026-10-09 15:19:58 | 读数/结果＋成果件面 |
| `results\_ci_three_delegated_judgments_2026_10_09.md` | `DAC19EE9E66B` | 26090 | 2026-10-09 17:16:22 | 终判/裁定＋判死线/准入门＋读数/结果＋成果件面 |
| `results\_ci_three_items_effectivity_register_2026_10_09.md` | `2B7166A7D726` | 31488 | 2026-10-09 21:12:50 | 登记＋读数/结果＋成果件面 |
| `results\_ci_width_halfwidth_pin_2026_10_09.md` | `51765F40F5F9` | 17426 | 2026-10-09 15:52:02 | 读数/结果＋成果件面 |
| `results\_cleanup_round_2026_10_01.md` | `0DB6E5D6146C` | 27477 | 2026-10-01 16:42:21 | 读数/结果＋成果件面 |
| `results\_cleanup_round_2026_10_08.md` | `D048A6DE1DEA` | 33179 | 2026-10-08 18:25:13 | 读数/结果＋成果件面 |
| `results\_cleanup_round2_register_2026_09_29.md` | `EE47A2EC49F4` | 36245 | 2026-09-29 22:20:14 | 登记＋读数/结果＋成果件面 |
| `results\_clearance_evening_round_register_2026_09_29.md` | `9C5543961E27` | 18201 | 2026-09-29 22:49:26 | 登记＋读数/结果＋成果件面 |
| `results\_clearance_materials_register_2026_10_08.md` | `356EB1C53986` | 45254 | 2026-10-08 16:24:26 | 登记＋读数/结果＋成果件面 |
| `results\_clearance_mini_rulings_closeout_register_2026_10_01.md` | `9238C2287AF5` | 31942 | 2026-10-01 09:10:24 | 终判/裁定＋登记＋读数/结果＋成果件面 |
| `results\_clearance_round_1_register_2026_10_08.md` | `58FA92543338` | 13826 | 2026-10-08 16:43:54 | 登记＋读数/结果＋成果件面 |
| `results\_closing_round_4_decisions_register_2026_10_08.md` | `771E37B4A25D` | 5322 | 2026-10-08 17:54:26 | 登记＋读数/结果＋成果件面 |
| `results\_closing_round_5_decisions_register_2026_10_08.md` | `5B08D34A05BA` | 3282 | 2026-10-08 18:02:35 | 登记＋读数/结果＋成果件面 |
| `results\_closing_round_6_decisions_register_2026_10_08.md` | `272CB570C78B` | 3869 | 2026-10-08 18:05:56 | 登记＋读数/结果＋成果件面 |
| `results\_closing_round_7_decisions_register_2026_10_09.md` | `D5976BFE23C6` | 3206 | 2026-10-09 09:29:38 | 登记＋读数/结果＋成果件面 |
| `results\_closing_round_8_decisions_register_2026_10_09.md` | `A28A478E14A8` | 2151 | 2026-10-09 10:12:53 | 登记＋读数/结果＋成果件面 |
| `results\_closing_round_9_decisions_register_2026_10_09.md` | `27118156A99A` | 2314 | 2026-10-09 10:59:27 | 登记＋读数/结果＋成果件面 |
| `results\_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | `B979E78562A9` | 22895 | 2026-10-10 18:13:35 | 登记＋回函＋读数/结果＋成果件面 |
| `results\_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | `C46D073589CF` | 24240 | 2026-10-10 17:05:56 | 登记＋回函＋读数/结果＋成果件面 |
| `results\_codex_c4_values_reply_intake_register_2026_10_10.md` | `8F1D27A02833` | 12926 | 2026-10-10 14:09:06 | 登记＋回函＋读数/结果＋成果件面 |
| `results\_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | `A2D7F86D72E5` | 27100 | 2026-10-10 18:06:56 | 登记＋回函＋读数/结果＋成果件面 |
| `results\_commission_closeout_erratum_and_supplement_2026_10_11.md` | `7C102A6B4667` | 12447 | 2026-10-11 23:46:12 | 勘误＋委托＋读数/结果＋成果件面 |
| `results\_confirm_b9_tension_annex_2026_10_01.md` | `F28724A99A0C` | 19454 | 2026-10-01 10:29:54 | 读数/结果＋成果件面 |
| `results\_confirm_round_2_2026_10_01_register.md` | `817302144788` | 22327 | 2026-10-01 09:44:14 | 登记＋读数/结果＋成果件面 |
| `results\_confirm_round_2026_10_01_register.md` | `23A97E340FDF` | 14500 | 2026-10-01 00:35:17 | 登记＋读数/结果＋成果件面 |
| `results\_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | `A82881653520` | 465366 | 2026-09-26 22:50:54 | 读数/结果＋成果件面 |
| `results\_cpath_e3_sign_normalization_2026_10_01.md` | `E67EBCCC82C9` | 19740 | 2026-10-01 14:06:32 | 读数/结果＋成果件面 |
| `results\_criterion_application_scope_prereg_2026_10_01.md` | `C4E3338619C6` | 50322 | 2026-10-01 16:02:40 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_d05_b_coincidence_checks_exec_2026_10_10.md` | `840FBF08CAF4` | 21061 | 2026-10-10 12:10:50 | 核查＋读数/结果＋成果件面 |
| `results\_d05_b_coincidence_checks_exec_readings_2026_10_10.json` | `586C435D1F15` | 13960 | 2026-10-10 12:08:44 | 核查＋读数/结果＋成果件面 |
| `results\_d05_three_checks_readings_recheck_confirm_2026_10_10.md` | `DCF9F5CFA2DB` | 20044 | 2026-10-10 12:43:54 | 核查＋读数/结果＋成果件面 |
| `results\_d1_backfill_b3_b7_suggestion_table_2026_10_01.md` | `8E1494301BB8` | 26731 | 2026-10-01 12:15:24 | 读数/结果＋成果件面 |
| `results\_d1_backfill_collection_rounds_2026_10_01.md` | `2D1A0D43E588` | 22908 | 2026-10-01 12:29:25 | 读数/结果＋成果件面 |
| `results\_d1_backfill_conflict_trace_2026_10_01.md` | `0CECDA616F15` | 31506 | 2026-10-01 11:06:56 | 读数/结果＋成果件面 |
| `results\_d1_backfill_event_id_prefix_proposal_2026_10_01.md` | `2636394DF918` | 14074 | 2026-10-01 12:28:08 | 读数/结果＋成果件面 |
| `results\_d1_backfill_intake_verdict_2026_10_01.md` | `A7E8F90D9DB7` | 42115 | 2026-10-10 11:37:23 | 登记＋读数/结果＋成果件面 |
| `results\_d1_backfill_readiness_pack_2026_10_01.md` | `ED644FB07F88` | 26462 | 2026-10-01 11:49:06 | 读数/结果＋成果件面 |
| `results\_d1_ruling_and_s3_transition_2026_10_01.md` | `DC9CB0E02922` | 28370 | 2026-10-10 11:37:23 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_d8_boundary_revision_register_2026_09_30.md` | `B46370BB9E3B` | 32406 | 2026-09-30 14:00:09 | 登记＋读数/结果＋成果件面 |
| `results\_d8_closeout_protocol_recompute_2026_09_30.md` | `57ABA2CD26A6` | 31007 | 2026-09-30 22:57:20 | 核查＋读数/结果＋成果件面 |
| `results\_d8_collection_ledger_2026_09_30.md` | `031DD8429048` | 20290 | 2026-09-30 16:42:14 | 登记＋读数/结果＋成果件面 |
| `results\_d8_dup_overlap_disposal_2026_09_30.md` | `DE8691727842` | 32350 | 2026-09-30 14:14:24 | 读数/结果＋成果件面 |
| `results\_d8_supplement_open_questions_2026_09_30.md` | `579B375E9508` | 24833 | 2026-09-30 13:14:41 | 读数/结果＋成果件面 |
| `results\_day_close_register_2026_10_01.md` | `6DBAC1D1BCD6` | 33115 | 2026-10-01 16:55:26 | 登记＋读数/结果＋成果件面 |
| `results\_deemphasis_verification_register_2026_10_08.md` | `3F806E44A13F` | 27322 | 2026-10-08 16:02:33 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_dup_name_diff_content_scan_2026_10_08.json` | `A27D11F45C21` | 1302889 | 2026-10-08 17:23:27 | 核查＋读数/结果＋成果件面 |
| `results\_e2_glm2_distill_side_receipt_register_2026_10_09.md` | `974124FC53F9` | 11336 | 2026-10-09 10:03:28 | 登记＋读数/结果＋成果件面 |
| `results\_e4_lineage_conflict_correction_2026_10_11.md` | `E20B96E32F54` | 30510 | 2026-10-11 16:22:45 | 勘误＋读数/结果＋成果件面 |
| `results\_e5_nonbinary_count_judgment_2026_10_10.md` | `2EF8797C03F4` | 37762 | 2026-10-10 11:36:54 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_e6_alt_permp_comparability_closure_2026_10_10.md` | `1C663430B4AA` | 16636 | 2026-10-10 15:03:20 | 读数/结果＋成果件面 |
| `results\_e6_case_a_judgment_face_promotion_2026_10_10.md` | `4E65C53F68E8` | 42116 | 2026-10-10 12:53:23 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_e6_j5_backfill_resolution_2026_10_10.md` | `C888158B3263` | 23171 | 2026-10-10 11:45:26 | 读数/结果＋成果件面 |
| `results\_e6_j5_semantics_conflict_judgment_2026_10_10.md` | `3C7628A4964D` | 27682 | 2026-10-10 13:13:46 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_e6_j5_semantics_erratum_note_2026_10_10.md` | `B2DB427147E2` | 21166 | 2026-10-10 13:34:44 | 勘误＋读数/结果＋成果件面 |
| `results\_e6_n_distinct_judge_types_recompute_2026_10_10.md` | `82C5C143134E` | 26304 | 2026-10-10 15:02:56 | 核查＋读数/结果＋成果件面 |
| `results\_e6_th_v3_19_alignment_register_2026_10_10.md` | `622CEBEF2C9F` | 32582 | 2026-10-10 15:13:34 | 登记＋读数/结果＋成果件面 |
| `results\_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | `442D5FF4ACDB` | 46261 | 2026-10-10 17:59:21 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_e6_verdict_v3_rationale_review_2026_10_10.md` | `664E82968FC2` | 39008 | 2026-10-10 13:36:11 | 评审＋读数/结果＋成果件面 |
| `results\_ea_audit_batch_vk_2026_10_09.md` | `CE27DB55E0C5` | 19611 | 2026-10-09 12:17:38 | 核查＋读数/结果＋成果件面 |
| `results\_eps_ls_semantics_judgment_2026_10_11.md` | `51434449FF3B` | 31391 | 2026-10-11 14:59:15 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_evening_audit_b2_sampling_and_rejudges_2026_10_09.md` | `B067FD28F950` | 29069 | 2026-10-09 23:42:59 | 核查＋读数/结果＋成果件面 |
| `results\_executor_prereg_docstring_correction_2026_10_11.md` | `F7F8328C49BA` | 27721 | 2026-10-12 00:34:33 | 勘误＋读数/结果＋成果件面 |
| `results\_executor_prereg_vs_impl_equivalence_2026_10_11.md` | `E84CEC618659` | 20028 | 2026-10-12 00:08:14 | 读数/结果＋成果件面 |
| `results\_exp03_blade_caliber_review_2026_10_10.md` | `8C030758B331` | 19797 | 2026-10-10 03:00:34 | 评审＋读数/结果＋成果件面 |
| `results\_exp04_h_contrast_readings_2026_10_10.json` | `106E8667BE2D` | 72704 | 2026-10-10 10:05:05 | 读数/结果＋成果件面 |
| `results\_exp04_h_contrast_readings_2026_10_10.md` | `AC571BFE4D1D` | 17386 | 2026-10-10 10:06:54 | 读数/结果＋成果件面 |
| `results\_exp05_missing_true_disposition_judgment_2026_10_10.md` | `E8E1E63A11DB` | 25552 | 2026-10-10 10:46:49 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_exp05_negative_probe_rescan_2026_10_10.md` | `CA7FF556FD7A` | 11566 | 2026-10-10 03:06:08 | 核查＋读数/结果＋成果件面 |
| `results\_exp06_independent_check_2026_10_10.json` | `4C36C376AB9C` | 20480 | 2026-10-10 10:31:42 | 核查＋读数/结果＋成果件面 |
| `results\_exp06_kcf4_check_bit_landing_2026_10_10.md` | `088BA3D58C0F` | 20709 | 2026-10-10 03:06:42 | 核查＋读数/结果＋成果件面 |
| `results\_exp06_selfverified_renaming_note_2026_10_10.md` | `8B4EC41A37DD` | 34554 | 2026-10-10 11:25:56 | 核查＋读数/结果＋成果件面 |
| `results\_exp06_selfverified_runner_fix_note_2026_10_10.md` | `247398B687E6` | 17052 | 2026-10-10 10:51:43 | 核查＋读数/结果＋成果件面 |
| `results\_exp06_supplement_four_gaps_2026_10_10.md` | `9F86CC5BE8E9` | 26519 | 2026-10-10 10:33:13 | 读数/结果＋成果件面 |
| `results\_exp08_s4_prompt_face_register_2026_10_10.md` | `83109ECF440E` | 11929 | 2026-10-10 03:07:20 | 登记＋读数/结果＋成果件面 |
| `results\_exp08_volume_reconciliation_2026_10_10.md` | `895EB3F2943C` | 24140 | 2026-10-10 10:33:56 | 读数/结果＋成果件面 |
| `results\_external_letters_two_generation_values_note_2026_10_01.md` | `9F4439BF89A9` | 10979 | 2026-10-01 09:18:01 | 读数/结果＋成果件面 |
| `results\_external_pat_ark_prep_2026_09_30.md` | `CA540E5CAB23` | 14055 | 2026-09-30 19:41:47 | 读数/结果＋成果件面 |
| `results\_external_sibling_path_reference_rule_2026_10_01.md` | `E79EABB6CFA7` | 23871 | 2026-10-01 13:59:04 | 读数/结果＋成果件面 |
| `results\_f2_branch_fix_register_2026_09_29.md` | `A0CAB58C032E` | 22940 | 2026-09-29 22:57:03 | 登记＋读数/结果＋成果件面 |
| `results\_f2_closeout_note_2026_09_29.md` | `1599CB99ABF3` | 16317 | 2026-09-29 23:05:32 | 读数/结果＋成果件面 |
| `results\_f3_definition_deep_judgment_2026_10_11.md` | `11945E587B1D` | 42351 | 2026-10-11 13:46:07 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_f3_new_definition_draft_2026_10_11.md` | `7482699E8B07` | 48068 | 2026-10-11 12:51:45 | 读数/结果＋成果件面 |
| `results\_f3f4_exit_drafts_2026_10_11.md` | `523DC6CBDF9A` | 50427 | 2026-10-11 01:44:40 | 读数/结果＋成果件面 |
| `results\_f4_direction1_domain_effectivity_2026_10_11.md` | `FD4EC7559342` | 40301 | 2026-10-11 14:05:56 | 读数/结果＋成果件面 |
| `results\_f4_direction1_prereq_check_2026_10_11.md` | `BB49153C311F` | 38664 | 2026-10-11 12:42:20 | 核查＋读数/结果＋成果件面 |
| `results\_f4_direction1_seed_and_domain_draft_2026_10_11.md` | `F77C080D9FC6` | 33887 | 2026-10-11 13:29:50 | 读数/结果＋成果件面 |
| `results\_f5_77_16items_reconciliation_2026_10_01.md` | `38BE1DC9A33F` | 23930 | 2026-10-01 11:15:01 | 读数/结果＋成果件面 |
| `results\_f5_d1_event_count_correction_2026_10_01.md` | `771641E234D6` | 24994 | 2026-10-01 10:05:17 | 勘误＋读数/结果＋成果件面 |
| `results\_f5_d1_event_count_correction_execution_2026_10_01.md` | `44D8CC9CB4A5` | 24279 | 2026-10-01 10:22:03 | 勘误＋读数/结果＋成果件面 |
| `results\_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` | `41D7B76EA4D6` | 40957 | 2026-09-30 17:25:45 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_fake_verdict_session_log_reverify_2026_09_30.md` | `C14094BDF815` | 25953 | 2026-09-30 12:54:50 | 核查＋读数/结果＋成果件面 |
| `results\_five_items_effectivity_register_2026_10_11.md` | `8AFFDCA64B4B` | 43332 | 2026-10-11 16:31:27 | 登记＋读数/结果＋成果件面 |
| `results\_five_pending_items_drafts_2026_10_11.md` | `86C46998DE63` | 55102 | 2026-10-11 16:06:04 | 读数/结果＋成果件面 |
| `results\_five_stage_chain_design_reconstruction_2026_10_12.md` | `BFF2FB754564` | 12625 | 2026-10-12 01:02:53 | 读数/结果＋成果件面 |
| `results\_five_terminal_judgments_ruling_2026_10_10.md` | `9E96D0A1BA12` | 27315 | 2026-10-10 12:28:00 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_forgotten_items_quick_sweep_register_2026_10_01.md` | `91103473289A` | 43735 | 2026-10-01 10:05:19 | 登记＋读数/结果＋成果件面 |
| `results\_forgotten_recovery_register_2026_09_29.md` | `D78BE896BCB6` | 47494 | 2026-09-29 21:39:46 | 登记＋读数/结果＋成果件面 |
| `results\_forgotten_recovery_register_2026_10_08.md` | `C981347CFFAD` | 34287 | 2026-10-08 16:33:10 | 登记＋读数/结果＋成果件面 |
| `results\_four_items_execution_batch_2026_10_11.md` | `8006D1962E5F` | 31515 | 2026-10-11 15:16:44 | 读数/结果＋成果件面 |
| `results\_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | `B7C060AB2D49` | 32886 | 2026-10-11 16:22:16 | 登记＋读数/结果＋成果件面 |
| `results\_freeze_receipt_2026_10_01_q1.md` | `9B7101BC09BD` | 698 | 2026-10-01 21:02:42 | 读数/结果＋成果件面 |
| `results\_ftfb_order_judgment_2026_10_11.md` | `B6EEC487E9D7` | 45911 | 2026-10-11 15:40:48 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_full_tidy_inventory_register_2026_09_30.md` | `33F68DBFBD6F` | 27687 | 2026-09-30 17:48:12 | 登记＋读数/结果＋成果件面 |
| `results\_g10_threshold_closed_domain_judgment_2026_10_11.md` | `586ABDA5DDF7` | 55727 | 2026-10-11 01:18:04 | 终判/裁定＋判死线/准入门＋读数/结果＋成果件面 |
| `results\_g11_krj4_effectivity_register_2026_10_11.md` | `17168119ECCC` | 39870 | 2026-10-11 12:31:21 | 登记＋读数/结果＋成果件面 |
| `results\_g4_controlled_reproduction_design_2026_10_09.md` | `B1C7C24926BB` | 23675 | 2026-10-09 09:47:11 | 核查＋读数/结果＋成果件面 |
| `results\_g4_e3_definition_independent_judgment_2026_10_09.md` | `AEBAFF5B503C` | 29094 | 2026-10-09 12:33:36 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g4_e3_definition_ruling_material_2026_10_09.md` | `8AE4016BB41D` | 30662 | 2026-10-09 11:07:09 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g4_reproduction_execution_register_2026_10_09.md` | `4DAAF68CBF0E` | 20414 | 2026-10-09 10:21:25 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_g4_residual_probe_2026_10_08.md` | `3554AA156E08` | 23025 | 2026-10-08 16:19:49 | 核查＋读数/结果＋成果件面 |
| `results\_g4_runtime_state_trace_2026_10_01.md` | `E0AE0AD66ACB` | 25631 | 2026-10-01 16:31:10 | 读数/结果＋成果件面 |
| `results\_g4_skill_read_scope_trace_2026_10_01.md` | `9196A608BB0D` | 26906 | 2026-10-01 14:31:34 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_g5_ccp_execution_prereqs_2026_10_10.md` | `AB1A07AE2FD1` | 32815 | 2026-10-10 18:52:37 | 读数/结果＋成果件面 |
| `results\_g5_ccp_p0_verification_2026_10_10.md` | `8C7693379496` | 24819 | 2026-10-10 19:05:07 | 核查＋读数/结果＋成果件面 |
| `results\_g5_ccp_seed_designation_revision_2026_10_10.md` | `B53F40ABB90B` | 20979 | 2026-10-10 19:15:26 | 读数/结果＋成果件面 |
| `results\_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | `3015F2481DF1` | 33880 | 2026-10-10 14:44:04 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_g5_displacement_threshold_draft_2026_10_10.md` | `7C8107D9A8FB` | 25619 | 2026-10-10 14:02:11 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | `22D90F12D605` | 45207 | 2026-10-10 18:34:36 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | `15301B3025FA` | 49051 | 2026-10-10 17:09:46 | 终判/裁定＋核查＋读数/结果＋成果件面 |
| `results\_g5_rejudgment_construction_change_plan_2026_10_10.md` | `FA0001A6DD0A` | 57004 | 2026-10-10 18:22:43 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g5_rejudgment_construction_question_judgment_2026_10_10.md` | `EE660515D9E3` | 59309 | 2026-10-10 17:47:40 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g5_rejudgment_face_prereg_2026_10_10.md` | `04495EF4B343` | 35097 | 2026-10-10 16:04:10 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` | `16C31894D445` | 48727 | 2026-10-10 17:12:00 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g5_seg3_tie_veto_judgment_2026_10_10.md` | `3306D1FD020D` | 35983 | 2026-10-10 15:17:28 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | `C3117773AB36` | 33976 | 2026-10-10 18:29:03 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_g9_read_b_effectivity_register_2026_10_11.md` | `F5D601A0602A` | 29649 | 2026-10-11 16:53:23 | 登记＋读数/结果＋成果件面 |
| `results\_gap_closeout_status_2026_10_09.md` | `EA41E346C4C4` | 28793 | 2026-10-09 11:07:19 | 读数/结果＋成果件面 |
| `results\_gate_one_declared_adoption_register_2026_10_11.md` | `3A965362D4F4` | 12923 | 2026-10-12 00:18:23 | 判死线/准入门＋登记＋读数/结果＋成果件面 |
| `results\_gate_one_pi_endorsement_register_2026_10_12.md` | `B09209E9C20D` | 9579 | 2026-10-12 00:53:49 | 判死线/准入门＋登记＋读数/结果＋成果件面 |
| `results\_ghostref_copy_log_2026_09_23.json` | `8CD133D0896F` | 129780 | 2026-09-23 15:11:45 | 读数/结果＋成果件面 |
| `results\_give_up_n10_erratum_2026_10_10.md` | `E0DB6B819138` | 22021 | 2026-10-10 15:25:42 | 勘误＋读数/结果＋成果件面 |
| `results\_give_up_semantics_draft_2026_10_10.md` | `B6A4AE82E038` | 23497 | 2026-10-10 13:26:05 | 读数/结果＋成果件面 |
| `results\_glm_five_items_suggestion_table_2026_10_01.md` | `F2B1359BE37D` | 29622 | 2026-10-01 11:21:40 | 读数/结果＋成果件面 |
| `results\_gt_recon_gamma_erratum_note_2026_10_01.md` | `CA063E6B9D60` | 9103 | 2026-10-01 09:17:17 | 勘误＋读数/结果＋成果件面 |
| `results\_id_face_revision_sync_note_2026_10_10.md` | `5D6C473731C4` | 20690 | 2026-10-10 00:43:53 | 读数/结果＋成果件面 |
| `results\_is_corr_pair_caliber_revision_proposal_2026_10_09.md` | `084C7D20067F` | 33497 | 2026-10-09 14:46:03 | 读数/结果＋成果件面 |
| `results\_j2_identifier_coupling_judgment_2026_10_11.md` | `2FD4505FDCA2` | 34261 | 2026-10-11 16:03:04 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_j2_kj4_disposition_register_2026_10_11.md` | `C1A4FF1B96E5` | 34112 | 2026-10-11 16:37:29 | 登记＋读数/结果＋成果件面 |
| `results\_k_cf_4_effectivity_register_2026_10_09.md` | `EDC6A548E3CA` | 35872 | 2026-10-09 17:06:53 | 登记＋读数/结果＋成果件面 |
| `results\_k_cf_4_low_cardinality_recure_2026_10_09.md` | `5F91D553E392` | 33788 | 2026-10-09 15:39:37 | 读数/结果＋成果件面 |
| `results\_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md` | `618280CB8CFD` | 31801 | 2026-10-09 15:44:50 | 核查＋读数/结果＋成果件面 |
| `results\_k_v3df_0_1_four_readings_2026_10_09.json` | `E87937D55471` | 65507 | 2026-10-09 11:24:10 | 读数/结果＋成果件面 |
| `results\_k_v3df_0_1_four_readings_2026_10_09.md` | `53C28CA1AE3D` | 46522 | 2026-10-09 11:24:10 | 读数/结果＋成果件面 |
| `results\_k_v3df_0_1_readings_verdict_2026_10_09.md` | `E98BEE353448` | 37003 | 2026-10-09 12:06:13 | 读数/结果＋成果件面 |
| `results\_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | `A14AAFA220C4` | 27735 | 2026-10-09 11:50:56 | 读数/结果＋成果件面 |
| `results\_k_v3df_scope_two_judgments_2026_10_09.md` | `4B22BA3C463E` | 21350 | 2026-10-09 17:33:46 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_k_v3s_3_4_lock_freeze_2026_10_08.md` | `C64865C32761` | 16973 | 2026-10-08 16:45:08 | 读数/结果＋成果件面 |
| `results\_k_v3s_4_2_domain_extension_judgment_2026_10_09.md` | `A802AF7AC3BC` | 23018 | 2026-10-09 21:06:53 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_k_v3s_4_3_frozen_recompute_2026_10_09.md` | `1C1494083255` | 26674 | 2026-10-09 14:27:36 | 核查＋读数/结果＋成果件面 |
| `results\_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | `B508E5335377` | 29664 | 2026-10-10 11:06:34 | 登记＋读数/结果＋成果件面 |
| `results\_kd_doc1_correction_adoption_register_2026_10_11.md` | `C55770BE5E33` | 10255 | 2026-10-12 00:39:06 | 登记＋勘误＋读数/结果＋成果件面 |
| `results\_kd_heteronym_classification_disposition_2026_10_09.md` | `C0CFD21D57A8` | 29761 | 2026-10-09 17:54:34 | 读数/结果＋成果件面 |
| `results\_kd_legacy_rewrite_plan_2026_10_10.md` | `A9698FED8B9B` | 17643 | 2026-10-10 02:57:52 | 读数/结果＋成果件面 |
| `results\_kd_legacy_rewrite_register_2026_10_10.md` | `9A7936882A5D` | 14537 | 2026-10-10 10:41:53 | 登记＋读数/结果＋成果件面 |
| `results\_kd_legacy_rewrite_ruling_2026_10_10.md` | `2CADAB5ED4F7` | 13731 | 2026-10-10 10:40:29 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_kd_login_register_section65_correction_2026_10_10.md` | `316D14C137BB` | 20422 | 2026-10-10 13:56:56 | 登记＋勘误＋读数/结果＋成果件面 |
| `results\_kd_resolvability_and_optional_experiments_2026_10_09.md` | `3138AC9095B0` | 70328 | 2026-10-09 21:01:37 | 读数/结果＋成果件面 |
| `results\_kd_rewrite_fingerprint_sync_2026_10_10.md` | `AEEFC94A94B5` | 20862 | 2026-10-10 11:53:38 | 读数/结果＋成果件面 |
| `results\_kd_unambiguous_meaning_ruling_2026_10_10.md` | `F22EDE7226D2` | 24898 | 2026-10-10 11:36:58 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` | `B07887551F7C` | 19525 | 2026-10-10 11:38:50 | 登记＋读数/结果＋成果件面 |
| `results\_kd_writing_convention_guidance_2026_10_09.md` | `708DFAC55BE9` | 20179 | 2026-10-09 21:59:00 | 读数/结果＋成果件面 |
| `results\_kd04_c_denominator_closeout_register_2026_10_10.md` | `78481CC60494` | 23029 | 2026-10-10 13:21:16 | 登记＋读数/结果＋成果件面 |
| `results\_kd04_c_denominator_expansion_exec_2026_10_10.md` | `2CAA3966B866` | 27915 | 2026-10-10 11:41:56 | 读数/结果＋成果件面 |
| `results\_kd04_c_denominator_expansion_readings_2026_10_10.json` | `249009E6A0CC` | 23314 | 2026-10-10 11:44:09 | 读数/结果＋成果件面 |
| `results\_kd04_c_denominator_killline_prereg_2026_10_10.md` | `8F2025E9DE6F` | 24527 | 2026-10-10 11:27:33 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | `19AD36F7EC84` | 25123 | 2026-10-10 13:03:50 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_kickoff_decisions_register_2026_10_08.md` | `6EE5D2B8323C` | 16388 | 2026-10-08 16:02:29 | 登记＋读数/结果＋成果件面 |
| `results\_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md` | `1C7445FCA0DE` | 4794 | 2026-09-30 21:47:40 | 终判/裁定＋登记＋读数/结果＋成果件面 |
| `results\_kj1_abc_choice_judgment_2026_10_11.md` | `D02EC6B0987E` | 42083 | 2026-10-11 15:02:27 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_kj1_eps_ls_effectivity_register_2026_10_11.md` | `809EDB4BB1CC` | 62344 | 2026-10-11 15:42:36 | 登记＋读数/结果＋成果件面 |
| `results\_kj1_judgment_premise_correction_2026_10_11.md` | `003B134CCE24` | 35050 | 2026-10-11 15:16:12 | 终判/裁定＋勘误＋读数/结果＋成果件面 |
| `results\_kj1_sc1_premise_correction_2026_10_11.md` | `8B344B9B4715` | 31044 | 2026-10-11 14:59:46 | 勘误＋读数/结果＋成果件面 |
| `results\_kj4_e4_unification_judgment_2026_10_11.md` | `A14D49F7D3A2` | 36839 | 2026-10-11 16:08:15 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_krj_all_five_verdicts_rewrite_2026_10_11.md` | `78FB8C47C944` | 72247 | 2026-10-11 21:12:00 | 读数/结果＋成果件面 |
| `results\_krj_all_terminal_verdicts_2026_10_11.md` | `F52231807E36` | 95659 | 2026-10-11 17:51:02 | 读数/结果＋成果件面 |
| `results\_krj_cond4_bytes_erratum_2026_10_11.md` | `78A95E5561FC` | 3886 | 2026-10-11 20:41:59 | 勘误＋读数/结果＋成果件面 |
| `results\_krj_cond4_effectivity_declaration_2026_10_11.md` | `F5C317F4CC96` | 15546 | 2026-10-11 20:32:37 | 读数/结果＋成果件面 |
| `results\_krj_five_verdicts_adjudication_2026_10_11.md` | `5C0EFD663847` | 16064 | 2026-10-11 21:20:35 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | `31E32CCC59BF` | 15214 | 2026-10-11 21:34:15 | 读数/结果＋成果件面 |
| `results\_krj10_reverdict_after_r4_convergence_2026_10_11.md` | `A21915EC55A7` | 31672 | 2026-10-12 00:05:01 | 读数/结果＋成果件面 |
| `results\_krj10_terminal_verdict_closure_2026_10_11.md` | `F2E8E32089B2` | 14101 | 2026-10-11 20:52:41 | 读数/结果＋成果件面 |
| `results\_krj4_trj1_adjudication_judgment_2026_10_11.md` | `50E91BF30E45` | 30293 | 2026-10-11 20:43:41 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | `FB7BB5DA85EC` | 16567 | 2026-10-11 21:06:58 | 读数/结果＋成果件面 |
| `results\_krj5_final_disposition_verdict_2026_10_11.md` | `2B6BF509A135` | 60700 | 2026-10-11 01:17:39 | 读数/结果＋成果件面 |
| `results\_krj5_subject_scope_judgment_2026_10_11.md` | `AE9DF5119861` | 45372 | 2026-10-11 00:47:58 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_krj5d_third_tier_effectivity_2026_10_11.md` | `062093D95C9F` | 10729 | 2026-10-11 21:52:41 | 读数/结果＋成果件面 |
| `results\_krj9_scope_clarification_draft_2026_10_10.md` | `B17B3C38EC21` | 28654 | 2026-10-10 19:55:36 | 读数/结果＋成果件面 |
| `results\_kv3s_3_2_terminal_verdict_2026_10_01.md` | `B081D19BE1B4` | 32296 | 2026-10-01 16:06:09 | 读数/结果＋成果件面 |
| `results\_kv3s_4_1_2_rejudge_2026_10_09.md` | `9CDE399502BA` | 51594 | 2026-10-09 22:34:56 | 读数/结果＋成果件面 |
| `results\_kv3s_4_4_carryover_bytes_correction_2026_10_10.md` | `0A7D2CCF74AD` | 5807 | 2026-10-10 00:39:05 | 勘误＋读数/结果＋成果件面 |
| `results\_kv3s_4_4_rejudge_2026_10_09.md` | `BC397D5099DD` | 42687 | 2026-10-09 23:10:27 | 读数/结果＋成果件面 |
| `results\_kv3s_4_4_review_carryover_2026_10_10.md` | `660D40DDD78C` | 17606 | 2026-10-10 00:38:39 | 评审＋读数/结果＋成果件面 |
| `results\_kv3s_4_terminal_verdict_2026_10_09.md` | `E51317FCC5CF` | 50858 | 2026-10-09 17:23:30 | 读数/结果＋成果件面 |
| `results\_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | `0F82948DEFB3` | 20211 | 2026-10-09 18:06:24 | 读数/结果＋成果件面 |
| `results\_letters_archive_register_2026_10_01.md` | `9F0740DA7E4D` | 26299 | 2026-10-02 00:29:52 | 登记＋读数/结果＋成果件面 |
| `results\_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | `F4B129E3312F` | 14770 | 2026-10-11 21:43:15 | 勘误＋读数/结果＋成果件面 |
| `results\_lim_aperiod_restatement_third_domain_2026_10_11.md` | `8672A5541CA8` | 27946 | 2026-10-11 21:38:15 | 勘误＋读数/结果＋成果件面 |
| `results\_limb_reading_verdict_kv3s33_2026_10_01.md` | `C5866CE87D9C` | 56329 | 2026-10-10 11:37:24 | 读数/结果＋成果件面 |
| `results\_linestand_pi_signoff_2026_10_01.md` | `CB5D933F8FAE` | 35538 | 2026-10-01 12:20:10 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_linestand_trace_gap_note_2026_10_01.md` | `91BB552BF76B` | 23252 | 2026-10-01 10:04:22 | 读数/结果＋成果件面 |
| `results\_log_observation_review_2026_10_08.md` | `AE20780C8D4E` | 2918 | 2026-10-08 18:14:19 | 评审＋读数/结果＋成果件面 |
| `results\_log_surface_scan_2026_10_08.md` | `6B0B202C5A6C` | 3156 | 2026-10-08 18:40:53 | 核查＋读数/结果＋成果件面 |
| `results\_m_r16_alias_table_draft_2026_10_01.md` | `0BA685B0D875` | 28128 | 2026-10-01 09:52:02 | 读数/结果＋成果件面 |
| `results\_m_r16_alias_table_effective_2026_10_01.md` | `4FFDB809EF22` | 36578 | 2026-10-01 10:28:11 | 读数/结果＋成果件面 |
| `results\_m5_eps_drift_disposition_2026_10_11.md` | `0722F25F5838` | 2736 | 2026-10-11 23:19:36 | 读数/结果＋成果件面 |
| `results\_md_trigger_prereg_effectivity_2026_10_11.md` | `5D8CD0D1676F` | 41636 | 2026-10-11 14:03:16 | 读数/结果＋成果件面 |
| `results\_mini_round_3_decisions_register_2026_10_01.md` | `BFF06D3B3F97` | 44308 | 2026-10-01 10:24:36 | 登记＋读数/结果＋成果件面 |
| `results\_mini_round_4_decisions_register_2026_10_01.md` | `0F2D1AFCC793` | 37804 | 2026-10-01 11:06:23 | 登记＋读数/结果＋成果件面 |
| `results\_mini_round_5_decisions_register_2026_10_01.md` | `D5FFFE6A5E79` | 53125 | 2026-10-10 11:37:23 | 登记＋读数/结果＋成果件面 |
| `results\_mini_round_6_7_settlement_register_2026_10_01.md` | `A87D1121B4AC` | 68053 | 2026-10-01 12:38:47 | 登记＋读数/结果＋成果件面 |
| `results\_misformed_commission_drafts_deletion_register_2026_10_11.md` | `BBDC9C2C8028` | 7261 | 2026-10-11 22:45:36 | 登记＋委托＋读数/结果＋成果件面 |
| `results\_morning_wrapup_pending_rulings_2026_10_01.md` | `2B6E8B527F93` | 7341 | 2026-10-01 09:36:01 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_n01_n08_revision_2026_10_10.md` | `FA8400D8AE70` | 26628 | 2026-10-10 15:22:33 | 读数/结果＋成果件面 |
| `results\_n1_d4_clause_placement_determination_2026_10_01.md` | `7CDA6ADEA62B` | 53732 | 2026-10-01 13:55:45 | 读数/结果＋成果件面 |
| `results\_n7_mutual_exclusion_determination_2026_10_01.md` | `B6BDF807CB27` | 40169 | 2026-10-10 11:37:24 | 读数/结果＋成果件面 |
| `results\_naming_erratum_linestand_note_2026_10_01.md` | `38C8218D066B` | 12137 | 2026-10-01 12:27:50 | 勘误＋读数/结果＋成果件面 |
| `results\_naming_ruling_note_2026_09_29.md` | `57024F2CD30A` | 7843 | 2026-09-29 21:18:08 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_nonportrait_criterion_formalization_design_2026_10_10.md` | `F4E145B090B1` | 55605 | 2026-10-10 02:54:17 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_o_r2_r5_external_verification_2026_10_01.md` | `D03832D3E2FF` | 59327 | 2026-10-01 09:16:48 | 核查＋读数/结果＋成果件面 |
| `results\_overnight_delivery_index_2026_10_10.md` | `266D0327025D` | 35344 | 2026-10-10 03:23:28 | 读数/结果＋成果件面 |
| `results\_p_i_real_labels_2026_09_16\p_i_real_labels_results_2026_09_16.json` | `E934819EE9ED` | 1043 | 2026-09-16 22:11:35 | 读数/结果＋成果件面 |
| `results\_p_j_convergence_basin_2026_09_16\p_j_convergence_basin_results_2026_09_16.json` | `A9AD1DE618F5` | 1669 | 2026-09-16 17:39:59 | 读数/结果＋成果件面 |
| `results\_p_l_p_c_finite_size_scaling_2026_09_16\p_l_p_c_finite_size_scaling_results_2026_09_16.json` | `664E7CC05AEC` | 9076 | 2026-09-16 15:50:08 | 读数/结果＋成果件面 |
| `results\_p_l_real_data_collapse_2026_09_16\p_l_real_data_collapse_results_v2_2026_09_16.json` | `AFE975606D40` | 3761 | 2026-09-16 22:40:54 | 读数/结果＋成果件面 |
| `results\_p_m_attack_surface_cost_2026_09_16\p_m_attack_surface_cost_results_2026_09_16.json` | `FBCB60CF5102` | 5266 | 2026-09-16 17:34:14 | 读数/结果＋成果件面 |
| `results\_p_m_real_separation_2026_09_16\p_m_real_separation_results_2026_09_16.json` | `A4B12D1CFEDC` | 2042 | 2026-09-16 22:12:02 | 读数/结果＋成果件面 |
| `results\_p_n_curvature_potential_coupling_2026_09_16\p_n_curvature_potential_coupling_results_2026_09_16.json` | `088F28524A1D` | 4276 | 2026-09-16 17:43:33 | 读数/结果＋成果件面 |
| `results\_p_o_stranger_verification_2026_09_16\p_o_stranger_verification_results_2026_09_16.json` | `1E4C065DA058` | 5916 | 2026-09-16 13:23:52 | 核查＋读数/结果＋成果件面 |
| `results\_p_refresh_registration_preliminary_2026_10_10.md` | `A3E14B508A4A` | 32780 | 2026-10-10 21:56:34 | 读数/结果＋成果件面 |
| `results\_p_refresh_s0_judgment_2026_10_10.md` | `369173063A7C` | 41449 | 2026-10-10 21:28:04 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_p_refresh_scope_judgment_2026_10_10.md` | `44E98DC31E2B` | 34004 | 2026-10-10 23:12:55 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_p_s4_1_revision_register_2026_10_09.md` | `AD5C76111570` | 29961 | 2026-10-09 12:09:39 | 登记＋读数/结果＋成果件面 |
| `results\_p4_attribution_determination_2026_10_01.md` | `C6793CFF46D7` | 22053 | 2026-10-01 10:49:15 | 勘误＋读数/结果＋成果件面 |
| `results\_p4_clause2_ratification_note_2026_10_01.md` | `CDF009712B96` | 26871 | 2026-10-01 12:19:59 | 读数/结果＋成果件面 |
| `results\_pack_d_closeout_confirm_receipt_note_2026_10_01.md` | `15C18A28080F` | 35223 | 2026-10-01 15:57:56 | 读数/结果＋成果件面 |
| `results\_pack_d_closeout_effectuation_note_2026_10_01.md` | `97A3573E2A2D` | 27609 | 2026-10-01 15:46:18 | 读数/结果＋成果件面 |
| `results\_pack_d_closeout_register_2026_10_01.md` | `0F1F94DF75BA` | 62012 | 2026-10-01 14:54:17 | 登记＋读数/结果＋成果件面 |
| `results\_pending_pi_items_drafts_2026_10_11.md` | `55F469269D3D` | 40678 | 2026-10-11 14:44:15 | 读数/结果＋成果件面 |
| `results\_pending_pi_items_master_register_2026_10_09.md` | `87AB4929477F` | 35258 | 2026-10-09 12:45:09 | 登记＋读数/结果＋成果件面 |
| `results\_pending_rulings_drafts_2026_10_11.md` | `C8428B883029` | 42775 | 2026-10-11 12:17:37 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_pending_supply_search_receipt_2026_10_08.md` | `11BBEE2BEA42` | 12595 | 2026-10-08 16:17:05 | 读数/结果＋成果件面 |
| `results\_phase1_completion_judgment_2026_10_10.md` | `6049C68F027B` | 28836 | 2026-10-10 19:44:53 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | `0A4B752CBC56` | 13883 | 2026-10-12 00:11:11 | 判死线/准入门＋委托＋读数/结果＋成果件面 |
| `results\_pi_effectivity_declaration_register_2026_10_11.md` | `41A82BDE5190` | 54511 | 2026-10-11 14:22:34 | 登记＋读数/结果＋成果件面 |
| `results\_pi_facing_items_screen_2026_10_09.md` | `A6D33CF318FE` | 59604 | 2026-10-09 21:53:15 | 读数/结果＋成果件面 |
| `results\_pi_pending_items_draft_package_2026_10_09.md` | `8FA2A7A2C49D` | 51793 | 2026-10-09 23:42:17 | 读数/结果＋成果件面 |
| `results\_plan_v3_pending_verify_2026_09_30.md` | `7374004D6075` | 42280 | 2026-09-30 19:06:18 | 核查＋读数/结果＋成果件面 |
| `results\_pre_exec_report_kimi_2026_09_30.md` | `3E3EF9007A90` | 5677 | 2026-09-30 20:04:18 | 读数/结果＋报告＋成果件面 |
| `results\_pre_execution_report_kimi_2026_10_01.md` | `941E1A68B2DF` | 6277 | 2026-10-01 20:59:50 | 读数/结果＋报告＋成果件面 |
| `results\_protocol_version_landing_status_2026_10_09.md` | `1D1895489D17` | 11562 | 2026-10-09 11:20:01 | 读数/结果＋成果件面 |
| `results\_proxy_signoff_execution_register_2026_10_01.md` | `B6E5E15B70E5` | 20766 | 2026-10-01 16:04:59 | 终判/裁定＋登记＋读数/结果＋成果件面 |
| `results\_q2_scope_vs_revision_judgment_2026_10_11.md` | `B4F00E5A69C4` | 43195 | 2026-10-11 01:01:21 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | `9572DFC3CD59` | 16105 | 2026-10-09 23:56:42 | 读数/结果＋成果件面 |
| `results\_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | `E30D4032F195` | 64849 | 2026-10-09 23:54:41 | 读数/结果＋执行体＋成果件面 |
| `results\_q3_reported_value_errata_supplement_2026_10_10.md` | `E026F20839B1` | 12499 | 2026-10-10 00:47:10 | 勘误＋读数/结果＋报告＋成果件面 |
| `results\_q3_transposition_errata_2026_10_09.md` | `659C4101F10B` | 11757 | 2026-10-09 23:26:45 | 勘误＋读数/结果＋成果件面 |
| `results\_q4_legacy_disposal_register_2026_10_01.md` | `A8763C406D4F` | 13336 | 2026-10-01 09:18:49 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_2026_10_09.md` | `D917180DB36F` | 442288 | 2026-10-09 18:10:16 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | `6C18D336E018` | 84127 | 2026-10-10 19:09:19 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | `52C97D1C11E9` | 55341 | 2026-10-10 20:19:27 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | `1FF6919967A7` | 121137 | 2026-10-10 23:55:57 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | `43E0B642F8B2` | 114253 | 2026-10-11 12:52:21 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | `79BC4BFE38A5` | 54883 | 2026-10-11 13:35:24 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | `3654C41EDA64` | 44698 | 2026-10-11 13:47:15 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `DC43E3CB7610` | 262542 | 2026-10-10 00:23:35 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `193386B9F23C` | 72199 | 2026-10-09 21:28:13 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | `11681F0AD861` | 67225 | 2026-10-10 01:12:02 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | `D6FF041A9DF9` | 116506 | 2026-10-10 10:54:25 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | `EDB57308170D` | 77189 | 2026-10-10 13:59:18 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | `95BA771FA760` | 106453 | 2026-10-10 15:09:57 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md` | `0984955B0370` | 11752 | 2026-10-10 15:11:57 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `1FB8EAC82781` | 52602 | 2026-10-10 16:42:53 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `A651F76A6547` | 17517 | 2026-10-10 17:12:50 | 登记＋勘误＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | `29B30D845841` | 50790 | 2026-10-10 17:51:27 | 登记＋读数/结果＋成果件面 |
| `results\_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | `B6C0B4F29152` | 84422 | 2026-10-10 18:55:53 | 登记＋读数/结果＋成果件面 |
| `results\_r_pair_addendum_2026_10_09.json` | `CEBC2F6EF5EC` | 110510 | 2026-10-09 16:45:34 | 读数/结果＋成果件面 |
| `results\_r_pair_intake_recompute_register_2026_10_09.md` | `2DC64593B889` | 36774 | 2026-10-09 16:48:36 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_r_pair_interval_statement_errata_2026_10_09.md` | `61944EB91B72` | 9259 | 2026-10-09 22:43:07 | 勘误＋读数/结果＋成果件面 |
| `results\_r_pair_is_corr_coverage_design_2026_10_09.md` | `48F04FA39397` | 27208 | 2026-10-09 12:31:28 | 读数/结果＋成果件面 |
| `results\_r_pair_nonportrait_full_document_review_2026_10_09.md` | `D8D5E4D2154F` | 28176 | 2026-10-09 22:32:22 | 评审＋读数/结果＋成果件面 |
| `results\_r_pair_question_texts_2026_10_09.md` | `0AD849022328` | 30352 | 2026-10-09 12:37:13 | 读数/结果＋成果件面 |
| `results\_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md` | `5FAA16446171` | 23975 | 2026-10-09 22:42:46 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_r_pair_texts_independent_review_2026_10_09.md` | `8C5F83C3C4CF` | 35443 | 2026-10-09 17:43:25 | 评审＋读数/结果＋成果件面 |
| `results\_r_pair4_design_and_texts_2026_10_09.md` | `F793C5D9128F` | 35189 | 2026-10-09 14:22:32 | 读数/结果＋成果件面 |
| `results\_r1_amendment_undetermined_face_2026_10_01.md` | `DAB48B4D77C2` | 45128 | 2026-10-01 14:41:49 | 读数/结果＋成果件面 |
| `results\_r2_reference_pointer_disposition_2026_10_11.md` | `403ADEC92CE1` | 3121 | 2026-10-11 23:19:28 | 读数/结果＋成果件面 |
| `results\_r2_verdict_179domain_arith_verification_2026_10_09.md` | `511C81B96745` | 30532 | 2026-10-09 21:45:26 | 核查＋读数/结果＋成果件面 |
| `results\_r3_r4_interpretation_case_2026_10_01.md` | `46469217883B` | 64849 | 2026-10-10 11:37:24 | 读数/结果＋成果件面 |
| `results\_r3_wording_disposition_2026_10_11.md` | `9D381C9D95E6` | 3917 | 2026-10-11 23:19:03 | 读数/结果＋成果件面 |
| `results\_r4_convergence_2026_10_11.md` | `678394C47724` | 3133 | 2026-10-11 23:22:31 | 读数/结果＋成果件面 |
| `results\_r6_disposition_2026_10_11.md` | `CC51203FE8F5` | 3704 | 2026-10-11 23:19:12 | 读数/结果＋成果件面 |
| `results\_reading_face_basis_rejudge_2026_10_10.md` | `3FE193A2A01F` | 24208 | 2026-10-10 03:13:46 | 读数/结果＋成果件面 |
| `results\_readme_proper_batch_recheck_register_2026_09_30.md` | `2E530923457E` | 20781 | 2026-09-30 17:13:36 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_receipt_disposition_register_2026_10_08.md` | `A79C3B82EE01` | 23050 | 2026-10-08 17:25:43 | 登记＋读数/结果＋成果件面 |
| `results\_refcheck_hash_change_reference_recheck_2026_09_30.md` | `F011C29944B9` | 33625 | 2026-09-30 22:57:31 | 核查＋读数/结果＋成果件面 |
| `results\_register3_bytes_erratum_2026_10_11.md` | `F9F6805A7B76` | 13294 | 2026-10-11 12:32:09 | 登记＋勘误＋读数/结果＋成果件面 |
| `results\_registry_lag_correction_batch_2026_10_01.md` | `5B86FBF0CBBD` | 36367 | 2026-10-01 10:08:43 | 登记＋勘误＋读数/结果＋成果件面 |
| `results\_remote_residual_disposal_execution_order_2026_10_08.md` | `602C4D09623D` | 36486 | 2026-10-08 17:06:56 | 读数/结果＋成果件面 |
| `results\_round19_followup_round21_22_approvals_effect_register_2026_10_10.md` | `0C8DBA07DD1E` | 54850 | 2026-10-10 00:31:15 | 登记＋读数/结果＋成果件面 |
| `results\_round20_approvals_effect_register_2026_10_10.md` | `29D737C59E8B` | 27711 | 2026-10-10 00:24:02 | 登记＋读数/结果＋成果件面 |
| `results\_round23_26_threshold_review_effect_register_2026_10_10.md` | `9B0C62765576` | 47297 | 2026-10-10 01:15:09 | 判死线/准入门＋登记＋评审＋读数/结果＋成果件面 |
| `results\_round27_34_approvals_effect_register_2026_10_10.md` | `D0BC0B1A9AE0` | 73226 | 2026-10-10 11:02:09 | 登记＋读数/结果＋成果件面 |
| `results\_round45_dispositions_effect_register_2026_10_10.md` | `D66A1076952A` | 19803 | 2026-10-10 14:11:43 | 登记＋读数/结果＋成果件面 |
| `results\_round51_effectivity_register_2026_10_10.md` | `B8B0C52296B2` | 27070 | 2026-10-10 16:04:24 | 登记＋读数/结果＋成果件面 |
| `results\_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | `E861C7BC19AD` | 21788 | 2026-10-10 16:34:00 | 登记＋读数/结果＋成果件面 |
| `results\_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | `DEBD88FC150C` | 45351 | 2026-10-10 16:31:38 | 登记＋读数/结果＋成果件面 |
| `results\_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | `B27814792394` | 25637 | 2026-10-10 17:10:04 | 登记＋读数/结果＋成果件面 |
| `results\_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | `4C3A6DC0070D` | 20023 | 2026-10-10 17:11:26 | 登记＋读数/结果＋成果件面 |
| `results\_round54_g5_dispositions_register_2026_10_10.md` | `AFC67818BB85` | 39977 | 2026-10-10 17:42:45 | 登记＋读数/结果＋成果件面 |
| `results\_round55_dispositions_register_2026_10_10.md` | `002FA0A9A5E4` | 34913 | 2026-10-10 18:12:53 | 登记＋读数/结果＋成果件面 |
| `results\_round56_ad8fix_effectivity_register_2026_10_10.md` | `2E7F86314428` | 16553 | 2026-10-10 18:12:36 | 登记＋读数/结果＋成果件面 |
| `results\_round56_b01_followup_disposition_plan_2026_10_10.md` | `857FB940A43C` | 31004 | 2026-10-10 20:29:17 | 读数/结果＋成果件面 |
| `results\_round56_direct_adoptions_register_2_2026_10_10.md` | `F8E0FA28C067` | 26690 | 2026-10-10 20:15:55 | 登记＋读数/结果＋成果件面 |
| `results\_round56_direct_adoptions_register_2026_10_10.md` | `E3C56C5D0A97` | 43240 | 2026-10-10 19:06:22 | 登记＋读数/结果＋成果件面 |
| `results\_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | `936F551F0FD3` | 34181 | 2026-10-10 19:13:12 | 登记＋读数/结果＋成果件面 |
| `results\_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | `52D3B10A16A0` | 25045 | 2026-10-10 19:11:29 | 读数/结果＋成果件面 |
| `results\_round56_idx_sc1_resolution_2026_10_10.md` | `9B41F2A38B2F` | 47107 | 2026-10-10 19:27:46 | 读数/结果＋成果件面 |
| `results\_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | `C72086990450` | 8181 | 2026-10-10 19:55:10 | 读数/结果＋成果件面 |
| `results\_round56_n10_erratum_register_2026_10_10.md` | `599D0450434E` | 20321 | 2026-10-10 18:49:02 | 登记＋勘误＋读数/结果＋成果件面 |
| `results\_round56_pending_questions_compilation_2026_10_10.md` | `EF09B3D28A0F` | 33504 | 2026-10-10 18:17:26 | 读数/结果＋成果件面 |
| `results\_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | `421C936F6AE8` | 29019 | 2026-10-10 18:40:21 | 读数/结果＋成果件面 |
| `results\_round56_registration_supplement_2026_10_10.md` | `71A59735302C` | 21865 | 2026-10-10 21:37:33 | 读数/结果＋成果件面 |
| `results\_round56_review_effectivity_register_2026_10_10.md` | `DA6B55162E50` | 49013 | 2026-10-10 21:36:54 | 登记＋评审＋读数/结果＋成果件面 |
| `results\_round56_review_effectivity_register_3_2026_10_10.md` | `84ED13256250` | 77181 | 2026-10-10 23:50:47 | 登记＋评审＋读数/结果＋成果件面 |
| `results\_round56_review_effectivity_register_4_2026_10_11.md` | `EE31BB8A94FE` | 46908 | 2026-10-11 00:23:15 | 登记＋评审＋读数/结果＋成果件面 |
| `results\_round56_review_effectivity_register_5_2026_10_11.md` | `5DEBA7D27BB1` | 67613 | 2026-10-11 01:04:02 | 登记＋评审＋读数/结果＋成果件面 |
| `results\_round56_review_effectivity_register_6_2026_10_11.md` | `2F3255EA344F` | 58478 | 2026-10-11 01:37:31 | 登记＋评审＋读数/结果＋成果件面 |
| `results\_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | `AF4C3335538A` | 16640 | 2026-10-10 18:11:58 | 勘误＋核查＋读数/结果＋成果件面 |
| `results\_round56_shortname_backfill_note_2026_10_10.md` | `BB2444CCCD65` | 22195 | 2026-10-10 19:07:14 | 读数/结果＋成果件面 |
| `results\_round56_terminal_boundary_effectivity_register_2026_10_10.md` | `D5BF826278CB` | 35878 | 2026-10-10 18:48:25 | 登记＋读数/结果＋成果件面 |
| `results\_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | `6794FB09CE7E` | 28378 | 2026-10-10 18:49:59 | 登记＋读数/结果＋成果件面 |
| `results\_round56_th4_two_field_reporting_resolution_2026_10_10.md` | `71894A686E92` | 28233 | 2026-10-10 18:50:57 | 读数/结果＋报告＋成果件面 |
| `results\_round56_typeb_backfill_register_2026_10_10.md` | `607DED06D840` | 40253 | 2026-10-10 21:24:40 | 登记＋读数/结果＋成果件面 |
| `results\_round56_typeb_form_draft_2026_10_10.md` | `582C5FB9970C` | 50170 | 2026-10-10 20:18:30 | 读数/结果＋成果件面 |
| `results\_round56_typeb_implementation_register_2026_10_10.md` | `C296A7833A70` | 26367 | 2026-10-10 19:08:08 | 登记＋读数/结果＋成果件面 |
| `results\_round56_v4_kd_row_correction_revision_2026_10_10.md` | `6D8537CB127F` | 23453 | 2026-10-10 19:12:12 | 勘误＋读数/结果＋成果件面 |
| `results\_round56a_dispositions_register_2026_10_10.md` | `D8980CFAE7F7` | 50365 | 2026-10-10 18:33:00 | 登记＋读数/结果＋成果件面 |
| `results\_round56c_card_id_erratum_2026_10_10.md` | `F6C2D40F18FF` | 18747 | 2026-10-10 19:05:04 | 勘误＋读数/结果＋成果件面 |
| `results\_round56c_d23_ad5_judgment_2026_10_10.md` | `061813859345` | 50747 | 2026-10-10 18:36:42 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_round56r8_dispositions_register_2026_10_10.md` | `CFB08D0E15F4` | 46135 | 2026-10-10 18:57:58 | 登记＋读数/结果＋成果件面 |
| `results\_round56r9r10_dispositions_register_2026_10_10.md` | `0EB408AE60F5` | 49754 | 2026-10-10 19:57:04 | 登记＋读数/结果＋成果件面 |
| `results\_rpq_wordlist_and_t1p2_judgments_2026_10_09.md` | `246CE35C4DDC` | 44796 | 2026-10-09 23:30:07 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | `D2326973AAF8` | 29991 | 2026-10-10 23:51:48 | 读数/结果＋成果件面 |
| `results\_s2prime_krj3_applicability_recheck_2026_10_10.md` | `10518510B628` | 41322 | 2026-10-11 00:02:57 | 核查＋读数/结果＋成果件面 |
| `results\_s3_c4_recount_2026_10_01.md` | `86AF4C109519` | 32025 | 2026-10-01 11:15:06 | 读数/结果＋成果件面 |
| `results\_s3_closeout_convergence_2026_10_01.md` | `BB62B5C174DA` | 42443 | 2026-10-01 12:16:50 | 读数/结果＋成果件面 |
| `results\_s3_closeout_rules_case_2026_10_01.md` | `7E622691AEC1` | 52659 | 2026-10-01 11:55:45 | 读数/结果＋成果件面 |
| `results\_s3_d1_rulings_supplement_register_2026_10_01.md` | `4CE661ACC81F` | 28762 | 2026-10-01 13:35:56 | 终判/裁定＋登记＋读数/结果＋成果件面 |
| `results\_s3_d1fill_recount_2026_10_01.md` | `A7DFF824ED56` | 22877 | 2026-10-01 13:44:10 | 读数/结果＋成果件面 |
| `results\_s3_f1_loader_fix_recompute_2026_10_08.json` | `3044A070106E` | 20144 | 2026-10-08 16:58:00 | 核查＋读数/结果＋成果件面 |
| `results\_s3_f1_loader_fix_recompute_2026_10_08.md` | `B2C9840D237B` | 22065 | 2026-10-08 17:00:38 | 核查＋读数/结果＋成果件面 |
| `results\_s3_kv3s_3_full_recompute_2026_10_01.md` | `B0123F161C10` | 22183 | 2026-10-01 08:57:14 | 核查＋读数/结果＋成果件面 |
| `results\_s3_kv3s_3_verdict_2026_10_01.md` | `E394BB6B5DDF` | 35037 | 2026-10-10 11:37:23 | 读数/结果＋成果件面 |
| `results\_s3_missing_field_backfill_rule_draft_2026_10_01.md` | `8496A53D183A` | 35827 | 2026-10-10 11:37:24 | 读数/结果＋成果件面 |
| `results\_s3_missing_field_backfill_rule_effective_2026_10_01.md` | `1450057B0819` | 52469 | 2026-10-10 11:37:24 | 读数/结果＋成果件面 |
| `results\_s3_th_v21_reconciliation_verdict_2026_10_01.md` | `84FA6996B656` | 51073 | 2026-10-10 11:37:23 | 读数/结果＋成果件面 |
| `results\_s3prime_alert_disposition_judgment_2026_10_11.md` | `E7FCBC290A7E` | 53188 | 2026-10-11 00:29:00 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s3prime_degeneracy_selfcert_2026_10_11.md` | `E4D96A516289` | 39939 | 2026-10-11 00:15:56 | 读数/结果＋成果件面 |
| `results\_s3prime_recompute_after_supplement_2026_10_11.md` | `FA025E4DC166` | 41708 | 2026-10-11 00:59:13 | 核查＋读数/结果＋成果件面 |
| `results\_s4_abcreadings_reproducibility_check_2026_10_10.md` | `892E5DFE3ED1` | 25234 | 2026-10-10 12:27:42 | 核查＋读数/结果＋成果件面 |
| `results\_s4_bc_construction_ruling_2026_10_09.md` | `E2FDB380CD3C` | 30257 | 2026-10-09 23:22:00 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s4_chain_clearance_register_2026_10_09.md` | `EDA3D304D381` | 2684 | 2026-10-09 14:52:20 | 登记＋读数/结果＋成果件面 |
| `results\_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | `C7609657DFE4` | 44199 | 2026-10-10 17:50:47 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s4_daily_share_margin_prerequisite_2026_10_09.md` | `A929502E8421` | 18197 | 2026-10-09 09:59:56 | 读数/结果＋成果件面 |
| `results\_s4_dkb_backfill_register_2026_10_10.md` | `3A992C3FE235` | 25591 | 2026-10-10 10:26:50 | 登记＋读数/结果＋成果件面 |
| `results\_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | `2BDA07AF86FC` | 29700 | 2026-10-10 15:05:02 | 读数/结果＋成果件面 |
| `results\_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | `F48601FEE958` | 51898 | 2026-10-10 15:44:56 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s4_empty_sequence_backfill_assessment_2026_10_10.md` | `41B75FFEA7BE` | 28771 | 2026-10-10 00:40:54 | 读数/结果＋成果件面 |
| `results\_s4_execution_sequence_review_2026_10_10.md` | `0E1EB2FDD25E` | 19158 | 2026-10-10 13:04:40 | 评审＋读数/结果＋成果件面 |
| `results\_s4_face_closeout_2026_10_09.md` | `F7D76EDA2911` | 29158 | 2026-10-09 23:49:50 | 读数/结果＋成果件面 |
| `results\_s4_face_dual_files_verification_2026_10_09.md` | `CC3FC6EEBC6B` | 40228 | 2026-10-09 16:57:36 | 核查＋读数/结果＋成果件面 |
| `results\_s4_face_five_lines_ci_readings_2026_10_09.md` | `BEA9BC43A8F3` | 39462 | 2026-10-09 21:15:30 | 读数/结果＋成果件面 |
| `results\_s4_face_five_lines_ci_readings_execution_2026_10_09.md` | `73550514152D` | 29750 | 2026-10-09 22:50:18 | 读数/结果＋成果件面 |
| `results\_s4_face_sync_2026_10_09.md` | `6F8BA105B892` | 38955 | 2026-10-09 15:33:16 | 读数/结果＋成果件面 |
| `results\_s4_face_v2_sync_2026_10_09.md` | `9D3CC20FD980` | 46890 | 2026-10-09 15:45:37 | 读数/结果＋成果件面 |
| `results\_s4_feature_surface_v3_1_definition_2026_10_10.md` | `D044CE1C069D` | 30310 | 2026-10-10 11:10:18 | 读数/结果＋成果件面 |
| `results\_s4_final_ruling_card_register_2026_10_09.md` | `F62401B619CC` | 2135 | 2026-10-09 15:09:52 | 终判/裁定＋登记＋读数/结果＋成果件面 |
| `results\_s4_final_ruling_effectivity_register_2026_10_09.md` | `21F2926EFC5D` | 32975 | 2026-10-09 15:00:52 | 终判/裁定＋登记＋读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | `FB1B696DE1D6` | 35453 | 2026-10-09 21:26:53 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | `6A670E629DCA` | 20033 | 2026-10-09 22:08:41 | 读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | `73A02AC5937D` | 34689 | 2026-10-09 22:11:08 | 登记＋读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seed42_register_2026_10_09.md` | `2A2AD5C2E29F` | 37615 | 2026-10-09 21:11:25 | 登记＋读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seed42_sets_2026_10_09.json` | `8DFC9E0D8BF9` | 59100 | 2026-10-09 21:07:05 | 读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1BF6F47A590D` | 18923 | 2026-10-10 21:59:20 | 读数/结果＋执行体＋成果件面 |
| `results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `6CBB8BA01BFB` | 15409 | 2026-10-10 23:07:39 | 读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | `9DA183328F18` | 24690 | 2026-10-10 23:07:07 | 登记＋读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068E1A7A1D04` | 52655 | 2026-10-11 16:03:09 | 读数/结果＋执行体＋成果件面 |
| `results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `5777A07C608A` | 43130 | 2026-10-11 16:03:31 | 读数/结果＋成果件面 |
| `results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `784F042BF93D` | 22646 | 2026-10-11 16:03:31 | 登记＋读数/结果＋成果件面 |
| `results\_s4_heldout_seedprime_verification_2026_10_10.md` | `8C64314D0EC0` | 21966 | 2026-10-10 23:21:06 | 核查＋读数/结果＋成果件面 |
| `results\_s4_kex_killline_freeze_2026_10_10.md` | `6269D0C6FD10` | 15284 | 2026-10-10 13:03:55 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_s4_keyword_expansion_and_regen_design_2026_10_10.md` | `6EFDDAB54CA5` | 31149 | 2026-10-10 01:11:17 | 读数/结果＋成果件面 |
| `results\_s4_open_questions_addendum_2026_10_09.json` | `4378DCC20624` | 35215 | 2026-10-09 14:29:17 | 读数/结果＋成果件面 |
| `results\_s4_open_questions_design_2026_10_09.md` | `0186A4499BBC` | 31803 | 2026-10-09 13:33:22 | 读数/结果＋成果件面 |
| `results\_s4_open_questions_intake_recompute_register_2026_10_09.md` | `2E66478E6DB6` | 33672 | 2026-10-09 14:30:52 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_s4_reading_prep_order_2026_10_08.md` | `7AC726CDA752` | 20613 | 2026-10-08 16:46:34 | 读数/结果＋成果件面 |
| `results\_s4_reading_surface_and_authority_register_2026_10_09.md` | `0148B5271154` | 34405 | 2026-10-09 09:28:19 | 登记＋读数/结果＋成果件面 |
| `results\_s4_regen_execution_plan_2026_10_10.md` | `70E22220350D` | 33444 | 2026-10-10 12:00:40 | 读数/结果＋成果件面 |
| `results\_s4_regen_golive_clearance_2026_10_10.md` | `80D8905B9762` | 27436 | 2026-10-10 13:33:31 | 读数/结果＋成果件面 |
| `results\_s4_regen_traceability_judgment_2026_10_10.md` | `A330273B981C` | 36071 | 2026-10-10 09:44:42 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s4_revision_effectiveness_register_2026_10_09.md` | `356FE8509669` | 32820 | 2026-10-09 14:47:44 | 登记＋读数/结果＋成果件面 |
| `results\_s4_seedprime_inheldout_recompute_2026_10_10.md` | `CF3368E7D5A0` | 21866 | 2026-10-10 23:20:20 | 核查＋读数/结果＋成果件面 |
| `results\_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | `B2B044289FFE` | 24783 | 2026-10-11 00:50:28 | 读数/结果＋成果件面 |
| `results\_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | `A834E0E7121A` | 28030 | 2026-10-11 00:50:28 | 读数/结果＋成果件面 |
| `results\_s4_source_wave_mapping_registration_2026_10_10.md` | `26C8278E3552` | 38231 | 2026-10-10 17:56:29 | 读数/结果＋成果件面 |
| `results\_s4_substrate_freeze_register_2026_10_09.md` | `F4A52862521B` | 29064 | 2026-10-09 14:17:49 | 登记＋读数/结果＋成果件面 |
| `results\_s4_substrate_grid_availability_2026_10_08.json` | `66BE80AB4B81` | 11446 | 2026-10-08 16:59:10 | 读数/结果＋成果件面 |
| `results\_s4_substrate_grid_availability_2026_10_08.md` | `7DEAEE06C41A` | 14995 | 2026-10-08 17:00:03 | 读数/结果＋成果件面 |
| `results\_s4_substrate_refreeze_register_179_2026_10_09.md` | `24EA764DAEAC` | 45386 | 2026-10-09 21:03:55 | 登记＋读数/结果＋成果件面 |
| `results\_s4_substrate_topup_addendum_2026_10_09.json` | `1780542F0014` | 85861 | 2026-10-09 13:53:09 | 读数/结果＋成果件面 |
| `results\_s4_substrate_topup_collection_register_2026_10_09.md` | `33C1A818EF4F` | 18327 | 2026-10-09 10:20:29 | 登记＋读数/结果＋成果件面 |
| `results\_s4_terminal_face_recompute_2026_10_09.md` | `B412342EABEC` | 46701 | 2026-10-09 17:08:17 | 核查＋读数/结果＋成果件面 |
| `results\_s4_topup_intake_recompute_register_2026_10_09.md` | `DFC9B0FBEF5A` | 32779 | 2026-10-09 13:55:13 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_s4_topup_intake_verdict_2026_10_09.md` | `658D7F3AB231` | 33799 | 2026-10-09 14:04:40 | 登记＋读数/结果＋成果件面 |
| `results\_s4_topup_questionnaire_design_2026_10_09.md` | `B8F8F987F21B` | 38466 | 2026-10-09 11:00:13 | 读数/结果＋成果件面 |
| `results\_s4_tree_construct_adjusted_readings_2026_10_10.json` | `A7AA4E9C8D47` | 108593 | 2026-10-10 09:51:47 | 读数/结果＋成果件面 |
| `results\_s4_tree_construct_adjustment_assessment_2026_10_10.md` | `016C7DACAA54` | 33453 | 2026-10-10 01:25:59 | 读数/结果＋成果件面 |
| `results\_s4_tree_construct_adjustment_exec_2026_10_10.md` | `B6B47008F8FD` | 28515 | 2026-10-10 09:55:59 | 读数/结果＋成果件面 |
| `results\_s4_tree_prereg_revision_2026_10_10.md` | `037140972829` | 30382 | 2026-10-10 10:48:57 | 读数/结果＋成果件面 |
| `results\_s4_v11_axis2_displacement_items_2026_10_10.json` | `0EED9053619C` | 9941 | 2026-10-10 15:04:30 | 读数/结果＋成果件面 |
| `results\_s4_v31_displacement_items_2026_10_10.json` | `6F020C03E52C` | 36822 | 2026-10-10 13:56:13 | 读数/结果＋成果件面 |
| `results\_s4_v31_displacement_register_face2_2026_10_10.md` | `B6CE4A79116E` | 17736 | 2026-10-10 13:57:19 | 登记＋读数/结果＋成果件面 |
| `results\_s4_v31_drift_register_face1_2026_10_10.md` | `5AB168D82873` | 11485 | 2026-10-10 13:56:41 | 登记＋读数/结果＋成果件面 |
| `results\_s4_v31_exec_section8_errata_2026_10_10.md` | `EC11AEC2380D` | 23250 | 2026-10-10 14:42:11 | 勘误＋读数/结果＋成果件面 |
| `results\_s4_v31_keyword_table_final_2026_10_10.md` | `1B7BCBCCE589` | 23270 | 2026-10-10 13:03:25 | 读数/结果＋成果件面 |
| `results\_s4_v31_readings_execution_2026_10_10.md` | `80D765F34163` | 21467 | 2026-10-10 13:55:46 | 读数/结果＋成果件面 |
| `results\_s4_v31_readings_summary_2026_10_10.json` | `882A1B3DEB0B` | 5569 | 2026-10-10 13:56:13 | 读数/结果＋成果件面 |
| `results\_s4_v31_regen_gold_items_2026_10_10.json` | `4125CB2DF92B` | 36830 | 2026-10-10 13:54:57 | 读数/结果＋成果件面 |
| `results\_s4_v31_regen_gold_register_2026_10_10.md` | `9C9D8E8ECC72` | 27133 | 2026-10-10 13:54:32 | 登记＋读数/结果＋成果件面 |
| `results\_s4_vclause_1_6_revision_2026_10_10.md` | `017B3CF38AE3` | 14900 | 2026-10-10 13:05:11 | 读数/结果＋成果件面 |
| `results\_s4_w1_3636_consistency_check_2026_10_10.md` | `0E9AE4B6EE8C` | 29196 | 2026-10-10 14:15:28 | 核查＋读数/结果＋成果件面 |
| `results\_s4_w2_disposition_registration_2026_10_10.md` | `566C2F0AD7E8` | 23545 | 2026-10-10 14:59:02 | 读数/结果＋成果件面 |
| `results\_s4_w2_e4_separate_judgment_2026_10_10.md` | `A51BD6530075` | 37607 | 2026-10-10 14:36:06 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_s4_w2bc_effect_registration_2026_10_10.md` | `B24A8411A260` | 26418 | 2026-10-10 15:36:26 | 读数/结果＋成果件面 |
| `results\_s4prime_five_lines_readings_2026_10_11.json` | `65A9B9BE6327` | 15219 | 2026-10-11 01:22:11 | 读数/结果＋成果件面 |
| `results\_s4prime_five_lines_readings_2026_10_11.md` | `E91E7F52C726` | 23877 | 2026-10-11 01:21:28 | 读数/结果＋成果件面 |
| `results\_s4prime_five_lines_runner_2026_10_11.py` | `F784B2FC92F4` | 29813 | 2026-10-11 01:19:53 | 读数/结果＋执行体＋成果件面 |
| `results\_s4prime_readings_runner_2026_10_11.py` | `0AA414188361` | 23766 | 2026-10-11 16:52:24 | 读数/结果＋执行体＋成果件面 |
| `results\_s4q04_level_attribution_judgment_2026_10_10.md` | `49A07216A1BB` | 26407 | 2026-10-10 13:20:41 | 终判/裁定＋勘误＋读数/结果＋成果件面 |
| `results\_s5doubleprime_five_lines_readings_2026_10_11.json` | `839FB5452578` | 16099 | 2026-10-11 18:14:08 | 读数/结果＋成果件面 |
| `results\_s5doubleprime_five_lines_runner_2026_10_11.py` | `9DE3C08E3863` | 31138 | 2026-10-11 18:12:11 | 读数/结果＋执行体＋成果件面 |
| `results\_s5dp_mixed_object_erratum_2026_10_11.md` | `07CDE000E66F` | 8380 | 2026-10-11 20:36:49 | 勘误＋读数/结果＋成果件面 |
| `results\_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | `9A62FB2A6956` | 58378 | 2026-10-11 20:43:15 | 登记＋读数/结果＋成果件面 |
| `results\_s5prime_lim_a_and_item_registers_2026_10_11.md` | `FA74831FA0AD` | 47225 | 2026-10-11 01:38:02 | 登记＋读数/结果＋成果件面 |
| `results\_s6doubleprime_terminal_verdicts_2026_10_11.md` | `BBA3B889D849` | 76910 | 2026-10-11 17:10:58 | 读数/结果＋成果件面 |
| `results\_s6doubleprime_verdict_supplement_2026_10_11.md` | `8E19C10CE219` | 31515 | 2026-10-11 17:38:34 | 读数/结果＋成果件面 |
| `results\_s6prime_terminal_verdicts_2026_10_11.md` | `1C8CE58D6484` | 54937 | 2026-10-11 12:36:08 | 读数/结果＋成果件面 |
| `results\_s7doubleprime_verification_2026_10_11.md` | `06AC684B4923` | 41680 | 2026-10-11 17:27:15 | 核查＋读数/结果＋成果件面 |
| `results\_s7doubleprime_verification_erratum_2026_10_11.md` | `9FF40693E4AC` | 32822 | 2026-10-11 17:39:50 | 勘误＋核查＋读数/结果＋成果件面 |
| `results\_s7prime_findings_erratum_2026_10_11.md` | `A7DFA8E789B7` | 31008 | 2026-10-11 13:38:58 | 勘误＋读数/结果＋成果件面 |
| `results\_s7prime_prereq_and_verification_2026_10_11.md` | `E44DA4B83810` | 36787 | 2026-10-11 12:59:14 | 核查＋读数/结果＋成果件面 |
| `results\_seed_double_criterion_draft_2026_10_11.md` | `025212E91546` | 40499 | 2026-10-11 14:21:47 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_seed_double_identifier_final_judgment_2026_10_11.md` | `728D18391748` | 50222 | 2026-10-11 15:02:43 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_seed_double_identifier_finalization_2026_10_11.md` | `6904852F8CEB` | 26864 | 2026-10-11 15:36:15 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_seed_double_rule_judgment_2026_10_11.md` | `F70A689FD8C1` | 57185 | 2026-10-11 14:02:53 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_seven_gap_closures_adoption_register_2026_10_11.md` | `AC3C41663F84` | 11960 | 2026-10-12 00:02:59 | 登记＋读数/结果＋成果件面 |
| `results\_skill_cache_inventory_and_reference_update_advice_2026_09_30.md` | `C14489750416` | 31692 | 2026-09-30 15:32:36 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_skill_call_surface_probe_2026_09_30.md` | `112346DF64FB` | 32261 | 2026-09-30 16:52:00 | 判死线/准入门＋核查＋读数/结果＋成果件面 |
| `results\_skill_call_surface_probe_supplement_a_2026_09_30.md` | `A06316C3C7F2` | 50658 | 2026-09-30 17:25:29 | 判死线/准入门＋核查＋读数/结果＋成果件面 |
| `results\_skill_call_surface_probe_supplement_b_2026_09_30.md` | `69D311E6A4C7` | 82744 | 2026-09-30 17:36:35 | 判死线/准入门＋核查＋读数/结果＋成果件面 |
| `results\_skill_directory_update_and_addressing_rule_2026_10_01.md` | `4A3A2D0C5B95` | 20335 | 2026-10-01 10:26:01 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_skill_erratum_and_parent_success_note_2026_09_30.md` | `7A64949402D9` | 24143 | 2026-09-30 16:16:31 | 判死线/准入门＋勘误＋读数/结果＋成果件面 |
| `results\_skill_load_failure_window_readonly_facts_2026_09_30.md` | `9F5B73620B8A` | 23065 | 2026-09-30 16:16:36 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | `16861E71305F` | 30771 | 2026-09-30 17:25:45 | 判死线/准入门＋勘误＋读数/结果＋成果件面 |
| `results\_skill_reference_update_and_user_surface_survey_2026_09_30.md` | `CB7B7EC9EBCD` | 60621 | 2026-09-30 17:49:57 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_stage1_tail_caliber_unification_register_2026_10_11.md` | `D486EC491E8E` | 41140 | 2026-10-11 14:41:24 | 登记＋读数/结果＋成果件面 |
| `results\_stage2_trae_reply_acceptance_register_2026_10_12.md` | `CE0B5A64CFCE` | 14874 | 2026-10-12 01:39:16 | 登记＋回函＋读数/结果＋成果件面 |
| `results\_stage3_extraction_verification_2026_10_11.md` | `F973E6D737C3` | 22399 | 2026-10-11 16:56:21 | 核查＋读数/结果＋成果件面 |
| `results\_stage3_readings_verification_2026_10_11.md` | `023A0CDD3350` | 29956 | 2026-10-11 17:13:11 | 核查＋读数/结果＋成果件面 |
| `results\_stage3_trigger_readings_2026_10_11.md` | `2900948BCA6D` | 35711 | 2026-10-11 16:56:23 | 读数/结果＋成果件面 |
| `results\_stage3_trigger_readings_items_2026_10_11.json` | `079108C62A82` | 21049 | 2026-10-11 16:52:40 | 读数/结果＋成果件面 |
| `results\_stage3_trigger_recheck_2026_10_11.md` | `AEF26B8CBE50` | 49109 | 2026-10-11 16:26:38 | 核查＋读数/结果＋成果件面 |
| `results\_sub_artifact_ledger_history_r5_2026_10_01.md` | `372A53B9E832` | 35845 | 2026-10-01 10:15:04 | 登记＋读数/结果＋成果件面 |
| `results\_sub_transfer_candidates_2026_10_01.md` | `2F61C0AA2A2B` | 21796 | 2026-10-01 19:35:10 | 读数/结果＋成果件面 |
| `results\_sub_transfer_execution_register_2026_10_01.md` | `C41013A975E0` | 13377 | 2026-10-01 19:45:58 | 登记＋读数/结果＋成果件面 |
| `results\_sub_transfer_wave2_register_2026_10_01.md` | `265B03EA493A` | 14286 | 2026-10-01 19:57:08 | 登记＋读数/结果＋成果件面 |
| `results\_sub_transfer_wave3_register_2026_10_01.md` | `CD80B993F497` | 14419 | 2026-10-01 20:33:47 | 登记＋读数/结果＋成果件面 |
| `results\_suspect17_release_move_register_2026_10_09.md` | `9A4D40BFCDC3` | 22351 | 2026-10-09 09:47:38 | 登记＋读数/结果＋成果件面 |
| `results\_t_s3_3_disposition_judgment_2026_10_10.md` | `EE7A822A077B` | 31855 | 2026-10-10 11:18:26 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1_7_2_correction_2026_10_08.md` | `D90BF82338F6` | 16469 | 2026-10-10 11:37:23 | 勘误＋读数/结果＋成果件面 |
| `results\_t1_d7_reading_line_judgment_2026_10_10.md` | `60BD9AE98640` | 28559 | 2026-10-10 00:18:41 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1_exp2_activation_supplement_2026_10_09.md` | `8DB3F88B5ED0` | 24708 | 2026-10-09 22:17:22 | 读数/结果＋成果件面 |
| `results\_t1_exp2_answer_face_baseline_2026_10_09.json` | `35773F5F1EDB` | 11792 | 2026-10-09 22:22:00 | 读数/结果＋成果件面 |
| `results\_t1_exp2_exec_register_2026_10_09.md` | `3A08DCFA8C7F` | 18597 | 2026-10-10 02:34:26 | 登记＋读数/结果＋成果件面 |
| `results\_t1_exp2_executor_2026_10_09.py` | `CE393B41618C` | 67955 | 2026-10-09 22:21:51 | 读数/结果＋执行体＋成果件面 |
| `results\_t1_exp2_result_2026_10_09.json` | `D9CCD75C652B` | 35239 | 2026-10-10 02:33:06 | 读数/结果＋成果件面 |
| `results\_t1_exp2_verdict_2026_10_10.md` | `15C1C4B317A0` | 48298 | 2026-10-10 02:47:15 | 读数/结果＋成果件面 |
| `results\_t1_exp2_verdict_bytes_correction_2026_10_10.md` | `E863CA5FB157` | 13480 | 2026-10-10 10:29:40 | 勘误＋读数/结果＋成果件面 |
| `results\_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | `4BDD82C796B8` | 72934 | 2026-10-10 11:37:24 | 判死线/准入门＋核查＋读数/结果＋成果件面 |
| `results\_t1_gate_revision_draft_2026_10_09.md` | `50E8B2440346` | 27452 | 2026-10-09 21:17:22 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_t1_gate_revision_formal_2026_10_09.md` | `0E0CB002C5DE` | 35658 | 2026-10-09 22:21:20 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_t1_o1_design_axis_exemption_judgment_2026_10_09.md` | `A27C7F411DE5` | 17073 | 2026-10-09 17:09:36 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1_p2_aggregation_caliber_judgment_2026_10_09.md` | `02F44F5BF2DD` | 14397 | 2026-10-09 17:08:31 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1_pairing_caliber_ruling_2026_10_09.md` | `2DED8091114A` | 21346 | 2026-10-09 21:56:51 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | `BDA5D5F3DFA0` | 16994 | 2026-10-09 10:03:07 | 读数/结果＋成果件面 |
| `results\_t1_prereg_revision_temp_axis_exp2_2026_10_09.md` | `2FF15AEEB5D0` | 34217 | 2026-10-09 21:49:30 | 读数/结果＋成果件面 |
| `results\_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | `7AD31E741400` | 17341 | 2026-10-09 11:20:07 | 登记＋读数/结果＋成果件面 |
| `results\_t1_qwen_temp_sweep_executor_2026_10_09.py` | `F0C845864603` | 32399 | 2026-10-09 10:22:20 | 读数/结果＋执行体＋成果件面 |
| `results\_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | `CF4826A731D6` | 23681 | 2026-10-09 18:10:33 | 登记＋读数/结果＋成果件面 |
| `results\_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | `38D0CF7FC9BA` | 53184 | 2026-10-09 18:06:06 | 读数/结果＋执行体＋成果件面 |
| `results\_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | `8D6242DA158C` | 58712 | 2026-10-09 18:06:16 | 读数/结果＋成果件面 |
| `results\_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | `9C18B9893579` | 42817 | 2026-10-09 18:23:43 | 读数/结果＋成果件面 |
| `results\_t1_qwen_temp_sweep_verdict_2026_10_09.md` | `DFC858D3D930` | 21672 | 2026-10-09 11:54:29 | 读数/结果＋成果件面 |
| `results\_t1_r2_activation_2026_10_09.md` | `8E59B797AA2D` | 21111 | 2026-10-09 17:07:33 | 读数/结果＋成果件面 |
| `results\_t1_r2_d1_field_caliber_correction_2026_10_09.md` | `99CAFDA125F1` | 25396 | 2026-10-09 21:28:08 | 勘误＋读数/结果＋成果件面 |
| `results\_t1_substrate_gap_census_2026_10_01.md` | `62FB594BE3F9` | 32371 | 2026-10-01 14:40:17 | 读数/结果＋成果件面 |
| `results\_t1_substrate_gap_precondition_2026_10_01.md` | `CF207DF06762` | 22196 | 2026-10-01 13:40:35 | 读数/结果＋成果件面 |
| `results\_t1_temp_axis_new_experiment_design_2026_10_09.md` | `7AAA90EE6D50` | 41392 | 2026-10-09 21:17:20 | 读数/结果＋成果件面 |
| `results\_t1_temp_axis_retirement_consolidation_2026_10_10.md` | `40CB2E81425A` | 20308 | 2026-10-10 10:51:31 | 读数/结果＋成果件面 |
| `results\_t1_temp_axis_retirement_judgment_2026_10_10.md` | `19AFC7E191A7` | 27384 | 2026-10-10 09:43:25 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1p2_enable_judgment_2026_10_10.md` | `1E97D06B6EC9` | 20132 | 2026-10-10 00:30:13 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1p2_escalation_judgment_2026_10_10.md` | `5F43775A3224` | 22930 | 2026-10-10 00:30:53 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_t1p2_judgment_bytes_correction_2026_10_10.md` | `D9D29BEC3A0B` | 6377 | 2026-10-10 00:31:40 | 终判/裁定＋勘误＋读数/结果＋成果件面 |
| `results\_th_id_attribution_verification_2026_10_09.md` | `94740F8D3C8D` | 8409 | 2026-10-09 15:02:39 | 勘误＋核查＋读数/结果＋成果件面 |
| `results\_th_id_miscitation_correction_2026_10_09.md` | `B61321BA3B6E` | 10468 | 2026-10-09 16:43:24 | 勘误＋读数/结果＋成果件面 |
| `results\_th_t1_n_min_revision_proposal_2026_10_09.md` | `24DA21074CC2` | 34884 | 2026-10-09 15:33:46 | 读数/结果＋成果件面 |
| `results\_theory_boundary_clone_sync_register_2026_10_09.md` | `1F9FD007649C` | 17528 | 2026-10-09 09:47:13 | 登记＋读数/结果＋成果件面 |
| `results\_theory_input_request_supplement_2026_09_29.md` | `C966E7B605AF` | 48190 | 2026-09-30 20:27:38 | 委托＋读数/结果＋成果件面 |
| `results\_three_pending_items_drafts_2026_10_11.md` | `8995859E5A76` | 51748 | 2026-10-11 21:55:16 | 读数/结果＋成果件面 |
| `results\_three_pending_items_effectivity_2026_10_11.md` | `DF1F5F75C7A0` | 16744 | 2026-10-11 22:05:39 | 读数/结果＋成果件面 |
| `results\_three_state_standard_repeal_register_2026_10_10.md` | `8503708C73BF` | 18364 | 2026-10-10 14:44:36 | 登记＋读数/结果＋成果件面 |
| `results\_thv3_15_parallel_seed_double_note_2026_10_11.md` | `3CD92287059E` | 15569 | 2026-10-11 15:17:29 | 读数/结果＋成果件面 |
| `results\_tidy_round2_archive_transfer_register_2026_09_30.md` | `1C1365F23C92` | 27641 | 2026-09-30 19:20:01 | 登记＋读数/结果＋成果件面 |
| `results\_tmp_disposal_register_2026_10_10.md` | `E0F6B744E826` | 20812 | 2026-10-10 12:00:12 | 登记＋读数/结果＋成果件面 |
| `results\_tra_v0_2026_09_10.py` | `D80A8F75A122` | 12125 | 2026-09-10 20:20:20 | 读数/结果＋执行体＋成果件面 |
| `results\_trae_errata_sha_drift_attribution_2026_10_01.md` | `6D5836CC6D3A` | 23913 | 2026-10-01 12:31:37 | 勘误＋读数/结果＋成果件面 |
| `results\_trae_sixitem_disposal_and_collision_register_2026_10_01.md` | `545B17D403BE` | 19268 | 2026-10-01 09:10:55 | 登记＋读数/结果＋成果件面 |
| `results\_trigger_denominator_caliber_judgment_2026_10_11.md` | `16BF9332DEEF` | 43448 | 2026-10-11 00:12:10 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_trj_w1_downstream_erratum_2026_10_10.md` | `E52D0016FBC6` | 24888 | 2026-10-10 18:41:15 | 勘误＋读数/结果＋成果件面 |
| `results\_trj_w1_verification_2026_10_10.md` | `CC6DE8E981F6` | 23014 | 2026-10-10 18:33:08 | 核查＋读数/结果＋成果件面 |
| `results\_typeb_m_caliber_2026_10_10.md` | `4D067A884C6C` | 32830 | 2026-10-10 23:30:45 | 读数/结果＋成果件面 |
| `results\_typeb_m_definition_judgment_2026_10_10.md` | `97AC7FCC4803` | 41432 | 2026-10-10 23:15:39 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_typeb_m_registration_2026_10_10.md` | `3B68D3890473` | 27778 | 2026-10-10 23:32:32 | 读数/结果＋成果件面 |
| `results\_u_cf_category_caliber_2026_10_10.md` | `73F181D76169` | 18976 | 2026-10-10 23:29:45 | 读数/结果＋成果件面 |
| `results\_u_cf_reclassification_2026_10_10.md` | `02F910E8795B` | 25698 | 2026-10-10 23:30:49 | 读数/结果＋成果件面 |
| `results\_u_closure_execution_register_2026_10_09.md` | `CBF0C9503284` | 12781 | 2026-10-09 09:38:19 | 登记＋读数/结果＋成果件面 |
| `results\_u_r_numbering_attribution_2026_10_11.md` | `53672C23D7F9` | 5331 | 2026-10-11 23:21:55 | 勘误＋读数/结果＋成果件面 |
| `results\_u_v04_01_criterion_scope_determination_2026_10_01.md` | `E82609024B59` | 27079 | 2026-10-01 11:05:37 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_u04_1_exemption_precondition_verification_2026_10_09.json` | `BDDFEAC3EE2F` | 21862 | 2026-10-09 17:25:09 | 核查＋读数/结果＋成果件面 |
| `results\_u04_1_exemption_precondition_verification_2026_10_09.md` | `C072FFE6110E` | 21377 | 2026-10-09 17:26:27 | 核查＋读数/结果＋成果件面 |
| `results\_u11_execution_register_2026_10_09.md` | `8BC087A16F5A` | 24549 | 2026-10-10 11:37:24 | 登记＋读数/结果＋成果件面 |
| `results\_u2u3_effectivity_register_2026_10_10.md` | `B00B87CEC825` | 27192 | 2026-10-10 13:49:44 | 登记＋读数/结果＋成果件面 |
| `results\_u3_carrier_qid_verification_2026_10_11.md` | `6509AE68F778` | 21572 | 2026-10-11 21:31:55 | 核查＋读数/结果＋成果件面 |
| `results\_u5_fingerprint_relocation_erratum_2026_10_10.md` | `200C7E4C57CB` | 24999 | 2026-10-10 15:25:33 | 勘误＋读数/结果＋成果件面 |
| `results\_u5b_citation_surface_revision_2026_10_10.md` | `5CC29C53A422` | 50079 | 2026-10-10 16:06:18 | 读数/结果＋成果件面 |
| `results\_u5b_p_counting_resolution_2026_10_10.md` | `E12E9D9A32C4` | 20086 | 2026-10-10 18:44:20 | 读数/结果＋成果件面 |
| `results\_u6_negative_delta_compatibility_2026_10_11.md` | `1846E917119F` | 20969 | 2026-10-11 21:35:16 | 读数/结果＋成果件面 |
| `results\_unclosed_items_inventory_2026_10_08.md` | `B0E7C74E951E` | 30219 | 2026-10-08 16:28:20 | 读数/结果＋成果件面 |
| `results\_upload_execution_receipt_kimi_2026_09_26.md` | `B4AC31F917F3` | 4191 | 2026-09-26 22:08:26 | 读数/结果＋成果件面 |
| `results\_upload_execution_receipt_kimi_2026_09_30.md` | `20E1F592CA61` | 4159 | 2026-09-30 20:21:45 | 读数/结果＋成果件面 |
| `results\_upload_execution_receipt_kimi_2026_10_01.md` | `A9A9A1D19661` | 4581 | 2026-10-01 21:06:04 | 读数/结果＋成果件面 |
| `results\_upload_guard_mirror_pair_2026_10_08.md` | `D923371CDBCE` | 23534 | 2026-10-08 17:11:17 | 读数/结果＋成果件面 |
| `results\_upload_ledger_kimi_2026_09_30.json` | `B17CB8AAE62D` | 218279 | 2026-09-30 20:21:46 | 登记＋读数/结果＋成果件面 |
| `results\_upload_ledger_kimi_2026_10_01.json` | `79A0FB18683B` | 43275 | 2026-10-01 21:06:04 | 登记＋读数/结果＋成果件面 |
| `results\_uv04_field_completeness_fill_2026_10_01.md` | `EB9B8D185F44` | 28735 | 2026-10-01 14:19:04 | 读数/结果＋成果件面 |
| `results\_v3_02_ethard_closure_verdict_2026_10_09.md` | `AA0F96BB618F` | 27819 | 2026-10-09 14:03:16 | 读数/结果＋成果件面 |
| `results\_v3_02_ethard_execution_register_2026_10_09.md` | `23457F5CE432` | 22007 | 2026-10-09 13:43:03 | 登记＋读数/结果＋成果件面 |
| `results\_v3_02_override_register_2026_10_09.md` | `C5441E186C3F` | 36245 | 2026-10-09 13:33:36 | 登记＋读数/结果＋成果件面 |
| `results\_v3_05_h_caliber_judgment_2026_10_09.md` | `1C2B5F40E15D` | 22050 | 2026-10-09 22:58:01 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_v3_construct_degradation_diag_2026_09_23.json` | `C8D539A58D29` | 11609 | 2026-09-23 14:20:36 | 读数/结果＋成果件面 |
| `results\_v3_n_cpath_live_data_2026_09_27.json` | `25374AF92F88` | 12711 | 2026-09-27 14:16:19 | 读数/结果＋成果件面 |
| `results\_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | `26C0D0B0FFB6` | 6411 | 2026-09-27 14:17:05 | 读数/结果＋成果件面 |
| `results\_v3_n_pg_boss_live_data_2026_09_27.json` | `BE11C5274807` | 9220 | 2026-09-27 14:15:46 | 读数/结果＋成果件面 |
| `results\_v3_n_recheck_llm_verdict_2026_09_27.md` | `426CFE18CF65` | 21332 | 2026-09-27 14:20:06 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_01_executor_2026_09_27.py` | `919FA909381E` | 41004 | 2026-09-27 15:43:40 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_01_rescript_2026_09_27.md` | `A3C95102290F` | 14541 | 2026-09-30 16:15:20 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_01_result_2026_09_27.json` | `C19E2AB24E63` | 167831 | 2026-09-27 16:04:01 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_04_executor_2026_09_27.py` | `E098FA21700D` | 49405 | 2026-09-27 15:56:09 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_04_rescript_2026_09_27.md` | `34099595FE75` | 14780 | 2026-09-30 16:15:20 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_04_result_2026_09_27.json` | `DB8CFB974CE3` | 840158 | 2026-09-27 16:04:05 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_05_executor_2026_09_28.py` | `D6C8BC163E11` | 38639 | 2026-09-28 13:27:45 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_05_rescript_2026_09_28.md` | `88B7EAF8675D` | 22178 | 2026-09-28 13:29:42 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_05_result_2026_09_28.json` | `F63B36B75A51` | 450701 | 2026-09-28 13:28:21 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_08_executor_2026_09_27.py` | `21C4BA4D479E` | 15598 | 2026-09-27 14:49:01 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_08_rescript_2026_09_27.md` | `2E08B9AE9F09` | 10459 | 2026-09-27 14:50:51 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_08_result_2026_09_27.json` | `0D2AF01086DB` | 10587 | 2026-09-27 14:51:08 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_08b_executor\executor_2026_09_27.py` | `B292410D9A69` | 43901 | 2026-09-27 15:17:27 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_08b_executor\rescript_2026_09_27.md` | `78F3ABA1F24C` | 18501 | 2026-09-27 15:18:54 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_08b_executor\result_2026_09_27.json` | `F9A7FA2D65B1` | 88052 | 2026-09-27 15:17:36 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_08c_preexp_data\_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | `4B7ED4D0A3E5` | 1395 | 2026-10-12 01:30:19 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_08c_preexp_data\executor_2026_09_27.py` | `CB6EB9164DF3` | 37775 | 2026-09-27 17:52:40 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_08c_preexp_data\rescript_2026_09_27.md` | `035AF77DB626` | 17069 | 2026-10-12 01:30:19 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_08c_preexp_data\result_2026_09_27.json` | `689A6E4427A8` | 146601 | 2026-09-27 17:52:51 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_10_executor_2026_09_27.py` | `80947906E592` | 33647 | 2026-09-27 15:12:15 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_10_rescript_2026_09_27.md` | `FC0FFD27ADCA` | 14445 | 2026-09-27 15:23:59 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_10_result_2026_09_27.json` | `5D4B6BAF1B18` | 82535 | 2026-09-27 15:20:09 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_12_executor_2026_09_27.py` | `4850B1CBB010` | 49430 | 2026-09-27 16:00:42 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_12_jsv_check_2026_09_27.md` | `C5EAB30E9FC6` | 15821 | 2026-09-30 16:15:20 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_12_jsv_phase_data_2026_09_27.json` | `642582D4FBD1` | 17718 | 2026-09-27 16:20:32 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_12_rescript_2026_09_27.md` | `776C86C735F8` | 21222 | 2026-09-30 16:15:20 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_12_result_2026_09_27.json` | `CDB37ED0B32F` | 187612 | 2026-09-27 16:04:05 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_12_rj5_provenance_2026_09_27.md` | `20F15C49FEB5` | 23822 | 2026-09-27 17:30:07 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_19_executor_2026_09_27.py` | `B133A631B1A8` | 19215 | 2026-09-27 14:55:27 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_19_rescript_2026_09_27.md` | `82A947F2AEBD` | 11089 | 2026-09-27 14:56:14 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_19_result_2026_09_27.json` | `DF07CF80930F` | 59888 | 2026-09-27 14:56:25 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_21_rescript_2026_09_27.md` | `04F6ECD482B9` | 14618 | 2026-09-27 16:44:40 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_21_result_2026_09_27.json` | `354AE9C14FE2` | 44928 | 2026-09-27 16:54:07 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_26_executor_2026_09_27.py` | `46C326C756C3` | 15056 | 2026-09-27 14:45:28 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_26_preexp_data_2026_09_27.json` | `177C88E1BD82` | 94658 | 2026-09-27 15:30:22 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_26_preexp_executor_2026_09_27.py` | `775217A462F5` | 38726 | 2026-09-27 15:29:13 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_26_preexp_report_2026_09_27.md` | `A46230E344AF` | 23048 | 2026-09-30 16:15:20 | 核查＋读数/结果＋报告＋成果件面 |
| `results\_v3_recheck_26_rescript_2026_09_27.md` | `6B86576146A3` | 13747 | 2026-09-27 20:10:38 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_26_result_2026_09_27.json` | `EB6A99DD46DD` | 11994 | 2026-09-27 14:51:06 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_26b_executor_2026_09_27.py` | `5C906113A210` | 43171 | 2026-09-27 15:51:38 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_26b_executor_r2_2026_09_28.py` | `0808AF6212C5` | 52272 | 2026-09-28 22:47:39 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_26b_executor_r3_2026_09_29.py` | `6C83E7A7CA2E` | 64959 | 2026-09-29 10:50:41 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_26b_r3_result_2026_09_29.json` | `C9D3C9F819F1` | 54294 | 2026-09-29 19:08:57 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_26b_rescript_2026_09_27.md` | `AE81D9B59054` | 30552 | 2026-09-30 16:15:20 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_26b_result_2026_09_27.json` | `49C6E5A07732` | 44379 | 2026-09-27 15:52:40 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_26b_verdict_2026_10_01.md` | `8BBECB15B28B` | 26309 | 2026-10-01 09:03:39 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_26b_verdict_prep_2026_10_01.md` | `3AAB3F7660FC` | 36133 | 2026-10-01 08:58:09 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_27_executor_2026_09_27.py` | `190CBE01D061` | 34084 | 2026-09-27 15:17:40 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_27_rescript_2026_09_27.md` | `6F045BDC70E7` | 14599 | 2026-09-27 15:22:57 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_27_result_2026_09_27.json` | `E06CB51FB3AF` | 42571 | 2026-09-27 15:20:39 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_28_executor_2026_09_27.py` | `4E8C0DD8F54F` | 17735 | 2026-09-27 14:47:05 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v3_recheck_28_rescript_2026_09_27.md` | `A0734E0A6860` | 10187 | 2026-09-27 14:50:20 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_28_result_2026_09_27.json` | `C0A8CB9029A7` | 26113 | 2026-09-27 14:53:26 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_35_rescript_2026_09_27.md` | `138FAF395F40` | 13211 | 2026-09-27 16:24:33 | 核查＋论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_recheck_35_result_2026_09_27.json` | `A8A4BEFB21F5` | 35091 | 2026-09-29 12:07:14 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_prereg_v1_2026_09_27.md` | `88052D7DB895` | 37346 | 2026-09-27 13:33:20 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_prereg_v1p1_2026_09_27.md` | `BCC3CEE23E82` | 42970 | 2026-09-27 14:44:22 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_prereg_v1p2_2026_09_27.md` | `9DA148037744` | 38932 | 2026-09-30 16:15:20 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_prereg_v1p2_2026_09_29.md` | `A667A5F69B7A` | 25854 | 2026-09-29 18:34:16 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_prereg_v1p3_2026_09_27.md` | `272ED65BF50E` | 35200 | 2026-09-30 16:15:20 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_prereg_v1p4_2026_09_27.md` | `5294E4A2BD14` | 69406 | 2026-09-28 15:27:29 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_prereg_v1p5_2026_09_29.md` | `7B1374578DE4` | 18680 | 2026-09-29 19:22:00 | 核查＋读数/结果＋成果件面 |
| `results\_v3_recheck_verdict_register_2026_09_27.md` | `D9B6B974CFC1` | 112085 | 2026-09-30 16:15:20 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_v3_s_phrasetemplate_preexp_data\executor_2026_09_27.py` | `96F491A8E2BF` | 35555 | 2026-09-27 17:47:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v3_s_phrasetemplate_preexp_data\rescript_2026_09_27.md` | `D42EA1FA61F1` | 17574 | 2026-10-12 01:30:19 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_s_phrasetemplate_preexp_data\result_2026_09_27.json` | `FAE3C4640507` | 36844 | 2026-09-27 17:47:59 | 读数/结果＋成果件面 |
| `results\_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` | `7E1323B09030` | 33932 | 2026-09-27 17:11:28 | 读数/结果＋成果件面 |
| `results\_v3_s_prereg_v1_2026_09_27.md` | `EF5A40554960` | 46836 | 2026-09-27 15:28:46 | 读数/结果＋成果件面 |
| `results\_v3_s1_executor\executor_2026_09_27.py` | `10870941C283` | 54937 | 2026-09-27 15:44:50 | 读数/结果＋执行体＋成果件面 |
| `results\_v3_s1_executor\rescript_2026_09_27.md` | `9D49A632EE81` | 17253 | 2026-09-27 15:45:21 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_s1_executor\result_2026_09_27.json` | `BFC99C3133DD` | 24975 | 2026-09-27 15:45:21 | 读数/结果＋成果件面 |
| `results\_v3_s2_executor\executor_2026_09_27.py` | `F1E272A0924A` | 84993 | 2026-09-27 16:03:46 | 读数/结果＋执行体＋成果件面 |
| `results\_v3_s2_executor\rescript_2026_09_27.md` | `FF0F964BE8AA` | 25151 | 2026-10-12 01:30:19 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_s2_executor\result_2026_09_27.json` | `D73D51E670DE` | 51039 | 2026-09-27 16:05:12 | 读数/结果＋成果件面 |
| `results\_v3_s3_collection_brief_2026_09_28.md` | `D5BA1161E37F` | 19045 | 2026-09-28 13:38:11 | 读数/结果＋成果件面 |
| `results\_v3_s3_wordexpand_data\executor_2026_09_28.py` | `80F1445CE45D` | 46005 | 2026-09-28 13:35:10 | 读数/结果＋执行体＋成果件面 |
| `results\_v3_s3_wordexpand_data\executor_r1_2026_09_28.py` | `39C29E0F092E` | 43524 | 2026-09-28 13:59:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v3_s3_wordexpand_data\rescript_2026_09_28.md` | `98D4F62CD52A` | 18225 | 2026-09-28 13:36:15 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_s3_wordexpand_data\rescript_r1_2026_09_28.md` | `C991DDB1DEB4` | 17168 | 2026-09-28 14:04:26 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v3_s3_wordexpand_data\result_2026_09_28.json` | `F7F6D875D73A` | 34953 | 2026-09-28 13:38:18 | 读数/结果＋成果件面 |
| `results\_v3_s3_wordexpand_recheck_r1_2026_09_28.json` | `67CCEA282D1C` | 33867 | 2026-09-28 14:04:43 | 核查＋读数/结果＋成果件面 |
| `results\_v3_supplement_verdict_2026_09_23.md` | `B70211BFA83E` | 15247 | 2026-09-23 14:27:09 | 读数/结果＋成果件面 |
| `results\_v3_v4_achievements_inventory_2026_09_24.md` | `965DB22E9130` | 194083 | 2026-09-30 16:18:35 | 读数/结果＋成果件面 |
| `results\_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `DF7E9CD39251` | 355819 | 2026-09-29 12:12:36 | 读数/结果＋成果件面 |
| `results\_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md` | `C64146C4CCAC` | 23152 | 2026-09-24 20:04:58 | 读数/结果＋成果件面 |
| `results\_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md` | `24C64CC23907` | 37212 | 2026-09-26 19:18:37 | 读数/结果＋成果件面 |
| `results\_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md` | `4C731A625868` | 17130 | 2026-09-26 19:45:55 | 读数/结果＋成果件面 |
| `results\_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md` | `55CD332F66F2` | 10288 | 2026-09-24 18:55:03 | 勘误＋读数/结果＋成果件面 |
| `results\_v3_v4_ghostref_reconciliation_2026_09_23.md` | `1D52DB0EBF53` | 169864 | 2026-09-23 15:11:45 | 读数/结果＋成果件面 |
| `results\_v34_experiment_gap_plan_2026_10_08.md` | `996FEB1DB9CB` | 36066 | 2026-10-08 16:46:11 | 读数/结果＋成果件面 |
| `results\_v3n_cpath_live_rerun_2026_10_01.json` | `7C26D08ECE3B` | 60012 | 2026-10-01 09:24:20 | 读数/结果＋成果件面 |
| `results\_v3n_cpath_live_rerun_verdict_2026_10_01.md` | `A91EFBFEC3D0` | 16409 | 2026-10-01 09:26:42 | 读数/结果＋成果件面 |
| `results\_v3r1_threshold_final_path_judgment_2026_10_10.md` | `93F187F1AB75` | 39653 | 2026-10-10 09:58:13 | 终判/裁定＋判死线/准入门＋读数/结果＋成果件面 |
| `results\_v3r1_threshold_path4_draft_2026_10_10.md` | `A51F5DE630ED` | 39077 | 2026-10-10 10:14:38 | 判死线/准入门＋读数/结果＋成果件面 |
| `results\_v3r1_threshold_restatement_design_2026_10_10.md` | `FB85A8013F9D` | 33847 | 2026-10-10 01:00:44 | 判死线/准入门＋勘误＋读数/结果＋成果件面 |
| `results\_v3x_18frozen_remeasure_2026_09_16\v3x_18frozen_remeasure_results_2026_09_16.json` | `928794710241` | 4202 | 2026-09-16 23:32:09 | 读数/结果＋成果件面 |
| `results\_v3x_conservation_anchor_2026_09_17.txt` | `F331A9C2BD22` | 940 | 2026-09-17 10:20:17 | 读数/结果＋成果件面 |
| `results\_v3x_d0_5_aggregation_2026_09_17.md` | `DDF0D1AA96D2` | 12010 | 2026-09-17 13:08:30 | 读数/结果＋成果件面 |
| `results\_v3x_d0_5_experiment_invitation_2026_09_17.md` | `D8F2B99AA527` | 7617 | 2026-09-17 09:34:32 | 委托＋读数/结果＋成果件面 |
| `results\_v3x_d0_5_proposal_coze_2026_09_17.md` | `759C25B21ED4` | 13200 | 2026-09-17 11:06:19 | 读数/结果＋成果件面 |
| `results\_v3x_d0_5_proposal_trae_2026_09_17.md` | `B1C227D54A82` | 13254 | 2026-09-20 17:11:14 | 读数/结果＋成果件面 |
| `results\_v3x_experiments_2026_09_16\v3x_experiments_results_2026_09_16.json` | `F39412103366` | 17053 | 2026-09-16 12:37:12 | 读数/结果＋成果件面 |
| `results\_v3x_p_k_verify_2026_09_16\v3x_p_k_verify_results_2026_09_16.json` | `59C2113B7C71` | 2059 | 2026-09-16 23:33:03 | 核查＋读数/结果＋成果件面 |
| `results\_v3x_p_l_v3_external_spec_2026_09_17.md` | `6A5B6EB635F0` | 5769 | 2026-09-17 11:03:24 | 读数/结果＋成果件面 |
| `results\_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | `523B5941C30C` | 16835 | 2026-09-17 11:52:29 | 读数/结果＋成果件面 |
| `results\_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md` | `183205BAA9AC` | 9570 | 2026-09-17 11:53:50 | 读数/结果＋成果件面 |
| `results\_v4_85_77_attribution_verifier_r1_2026_09_29.md` | `CD8EBAA86E44` | 17727 | 2026-09-29 16:04:04 | 勘误＋核查＋读数/结果＋成果件面 |
| `results\_v4_bom_u1_prereg_2026_09_28.md` | `5456ACBF2CB5` | 19185 | 2026-09-28 18:33:05 | 读数/结果＋成果件面 |
| `results\_v4_checkpoint_atomic_and_pycache_2026_09_28.md` | `52B3DEC13E06` | 25470 | 2026-09-28 15:55:24 | 核查＋读数/结果＋成果件面 |
| `results\_v4_closeout_bucket_register_2026_10_01.md` | `99355C24A03B` | 41943 | 2026-10-01 10:49:39 | 登记＋读数/结果＋成果件面 |
| `results\_v4_concl_t_verify_2026_09_28.md` | `927ADBA66E9B` | 13237 | 2026-09-28 19:32:52 | 核查＋读数/结果＋成果件面 |
| `results\_v4_daily_cleanup_2026_09_28.md` | `F56E6FBF04EF` | 25491 | 2026-09-28 18:29:44 | 读数/结果＋成果件面 |
| `results\_v4_day_inventory_2026_09_27.md` | `7662D5058A7D` | 40487 | 2026-09-27 18:11:43 | 读数/结果＋成果件面 |
| `results\_v4_day_inventory_measure_2026_09_27.py` | `3E903F224F87` | 8226 | 2026-09-27 18:02:27 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_effective_register_2026_09_28.md` | `2A65C1274202` | 30607 | 2026-09-28 14:22:37 | 登记＋读数/结果＋成果件面 |
| `results\_v4_evidence_audit_reconcile_2026_09_26.md` | `FE907046EDA1` | 24168 | 2026-09-30 16:15:20 | 核查＋读数/结果＋成果件面 |
| `results\_v4_exec_surface_switch_2026_09_28.md` | `3BC852E0D48B` | 28506 | 2026-09-28 17:28:07 | 读数/结果＋成果件面 |
| `results\_v4_final_verify.py` | `1DC482062D9B` | 4794 | 2026-09-23 10:49:06 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v4_gamma_r1_exec_2026_09_28.md` | `0D946E65BA3C` | 21496 | 2026-09-28 17:38:42 | 读数/结果＋成果件面 |
| `results\_v4_gamma_r1_prereg_2026_09_28.md` | `C9DA8678CF2B` | 33489 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_gamma_r1_prereg_v2_stop_2026_09_28.md` | `9349E2FDB537` | 17999 | 2026-09-28 19:36:48 | 读数/结果＋成果件面 |
| `results\_v4_gamma_r1_sources_20260928_S1.md` | `3D6E997AA692` | 2944 | 2026-09-28 17:36:55 | 读数/结果＋成果件面 |
| `results\_v4_gamma_r1_sources_20260928_S2.md` | `DCEC110CA2E0` | 2647 | 2026-09-28 17:37:02 | 读数/结果＋成果件面 |
| `results\_v4_gamma_r1_sources_20260928_S3.md` | `6B9761D710CA` | 2554 | 2026-09-28 17:37:12 | 读数/结果＋成果件面 |
| `results\_v4_gamma_r1_sources_20260928_S4.md` | `16AF6BAF8463` | 3050 | 2026-09-28 17:37:22 | 读数/结果＋成果件面 |
| `results\_v4_gamma_r1_sources_20260928_S5_faceD.md` | `4F77D49756DB` | 2264 | 2026-09-28 17:37:38 | 读数/结果＋成果件面 |
| `results\_v4_item04_closeout_prereg_2026_09_28.md` | `176E2B1C95AE` | 26719 | 2026-09-28 18:33:05 | 读数/结果＋成果件面 |
| `results\_v4_item04_textfix_prereg_v1x_2026_09_28.md` | `4AD2695935D3` | 42153 | 2026-09-28 17:46:40 | 读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_manifest_2026_09_24.md` | `32CC61D394F2` | 19104 | 2026-09-24 17:59:34 | 读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_manifest_v2_2026_09_26.md` | `F586A5A21584` | 27909 | 2026-09-26 18:43:10 | 读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_moves_ledger_2026_09_24.md` | `4025E871726B` | 18829 | 2026-09-24 18:15:50 | 登记＋读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_moves_ledger_v2_2026_09_24.md` | `64C4EF850025` | 47909 | 2026-09-24 18:29:40 | 登记＋读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_moves_ledger_v3_2026_09_24.md` | `8F5136E176B8` | 31689 | 2026-09-24 19:16:52 | 登记＋读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_moves_ledger_v4_2026_09_24.md` | `9BD8932FA214` | 37047 | 2026-09-24 19:39:04 | 登记＋读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_moves_ledger_v5_2026_09_24.md` | `272E8C752406` | 46058 | 2026-09-24 19:58:55 | 登记＋读数/结果＋成果件面 |
| `results\_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` | `CC498BC28525` | 37629 | 2026-09-26 19:12:42 | 登记＋读数/结果＋成果件面 |
| `results\_v4_maindir_count_monitor_2026_09_27.md` | `71E9CC179BEC` | 15313 | 2026-09-27 11:50:37 | 读数/结果＋成果件面 |
| `results\_v4_noise_cleanup_manifest_v2_2026_09_24.md` | `90253E8342DA` | 9683 | 2026-09-24 21:42:05 | 读数/结果＋成果件面 |
| `results\_v4_noise_cleanup_manifest_v3_2026_09_25.md` | `6F3F6FA3AB1D` | 24491 | 2026-09-25 01:12:20 | 读数/结果＋成果件面 |
| `results\_v4_noise_cleanup_manifest_v4_2026_09_27.md` | `82E90FF496AE` | 38001 | 2026-09-27 21:19:39 | 读数/结果＋成果件面 |
| `results\_v4_pending_decisions_2026_09_28.md` | `FE4671517827` | 24676 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_coding_review_2026_09_26.md` | `5FBEC21E0AD2` | 42914 | 2026-09-26 18:35:47 | 评审＋读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_collection_log.md` | `167AD91F198E` | 1181 | 2026-09-23 17:49:35 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset.json` | `7B01CD835A41` | 12672 | 2026-09-24 15:55:01 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | `172093A23E4B` | 4103 | 2026-09-24 18:47:18 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | `439721007AAF` | 6132 | 2026-09-26 16:54:17 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | `41D6C28CA87C` | 7566 | 2026-09-26 17:04:48 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | `99C58906F792` | 6666 | 2026-09-26 17:22:21 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | `C6D092F77932` | 7668 | 2026-09-26 17:27:21 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | `26F110A6E571` | 10257 | 2026-09-26 17:39:37 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | `6E104E2DB038` | 11589 | 2026-09-26 18:10:28 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | `D96B747BFC6C` | 14722 | 2026-09-26 18:18:19 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | `401BD614CDF7` | 19615 | 2026-09-26 18:30:47 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_prereg.md` | `CC25C5149CE1` | 4247 | 2026-09-23 17:56:05 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_prereg_activation_2026_09_23.md` | `00584E5A5C78` | 1016 | 2026-09-23 18:03:11 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_questionnaire_v1.md` | `7B14CDB31D21` | 12402 | 2026-09-24 10:51:01 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_result.json` | `1665F367B2C4` | 9068 | 2026-09-24 17:41:54 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_result_v2.json` | `F86727C857A8` | 18089 | 2026-09-26 18:50:30 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_ruleset.json` | `821465001819` | 5876 | 2026-09-24 17:41:54 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_ruleset_executor.py` | `48DCA1D4281C` | 39281 | 2026-09-24 17:41:44 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_pi_cot_v2_ruleset_v2.json` | `C5B3DD141655` | 6179 | 2026-09-26 18:50:30 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_ruleset_v2_executor.py` | `EB22F13D571C` | 52465 | 2026-09-26 18:49:42 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_pi_cot_v2_verdict.md` | `EB9AD4193CF2` | 22340 | 2026-09-24 18:07:05 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_verdict_v2.md` | `5D79E67A4E9D` | 33723 | 2026-09-26 19:03:30 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `BA4D07BD7000` | 26637 | 2026-09-26 19:14:42 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md` | `58ED6BE022ED` | 10251 | 2026-09-27 17:14:41 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset.json` | `5118F5B44F17` | 16025 | 2026-09-27 12:12:25 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | `CBF60A630C9F` | 20194 | 2026-09-27 12:10:45 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | `6EED9ACDB99A` | 18714 | 2026-09-27 17:04:40 | 勘误＋读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | `990C0C42A6F6` | 16587 | 2026-09-27 13:17:51 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | `9669EFA804B7` | 19214 | 2026-09-28 13:46:29 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | `5D94A8617B5B` | 27009 | 2026-09-28 15:00:07 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | `B02EF31F1E4E` | 58581 | 2026-09-30 16:21:49 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | `769EF8B71462` | 374072 | 2026-09-30 16:18:01 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | `B9026CBF5CA2` | 46909 | 2026-10-01 12:55:21 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | `C0EBBD1F4633` | 17252 | 2026-09-29 10:57:48 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | `ED596914259A` | 12975 | 2026-09-27 17:48:03 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json` | `CBC14A76F038` | 26891 | 2026-09-27 17:13:08 | 核查＋读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md` | `AE154971D1D2` | 12152 | 2026-09-28 14:04:07 | 登记＋读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md` | `44C4D570375C` | 12851 | 2026-09-28 14:03:02 | 登记＋勘误＋读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_prereg.md` | `B7547329AF2E` | 27223 | 2026-09-27 12:02:44 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md` | `238077D25919` | 53581 | 2026-09-28 15:19:16 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_result_v3.json` | `585714F9660C` | 27203 | 2026-09-27 13:04:21 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | `735C03DB1AE9` | 22292 | 2026-09-27 17:48:03 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_ruleset_v3.json` | `9D77A5E2CBAB` | 21392 | 2026-09-27 12:31:02 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_ruleset_v3_executor.py` | `8A81D90C69BA` | 58794 | 2026-09-27 12:29:46 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py` | `EE8671A28C2F` | 62115 | 2026-09-27 16:56:08 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | `75AEDF9BA95E` | 11385 | 2026-09-30 16:15:20 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_verdict_v3.md` | `BB44FDC7AB0F` | 53751 | 2026-09-27 13:15:20 | 读数/结果＋成果件面 |
| `results\_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | `41D29F4DEB70` | 42157 | 2026-09-27 13:24:20 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_v4_r4_cleanup_execution_2026_09_29.md` | `3932B46B16CE` | 15357 | 2026-09-29 14:12:44 | 读数/结果＋成果件面 |
| `results\_v4_r4_key_purge_manifest_2026_09_24.md` | `5BF4D9AD2877` | 13884 | 2026-09-24 18:55:22 | 读数/结果＋成果件面 |
| `results\_v4_r4_purge_actions_2026_09_24.md` | `8BBFE831E7C3` | 33117 | 2026-09-24 19:24:11 | 读数/结果＋成果件面 |
| `results\_v4_rj5_rederive_2026_09_28.md` | `34EC49511EE3` | 22145 | 2026-09-28 18:13:12 | 读数/结果＋成果件面 |
| `results\_v4_rj5_rederive_appendix_2026_09_28.md` | `985673661209` | 9226 | 2026-09-28 18:13:40 | 读数/结果＋成果件面 |
| `results\_v4_slow_cleanup_manifest_2026_09_28.md` | `012501569AEA` | 15693 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14_n11full_verdict.md` | `8EEF73BF9856` | 19697 | 2026-09-29 16:25:57 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch1_executor.py` | `B48019494530` | 29354 | 2026-09-24 20:45:39 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r2_executor.py` | `2BDB5163400F` | 29598 | 2026-09-24 21:00:44 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r2_result.json` | `00C7B545C397` | 40815 | 2026-09-24 21:11:40 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r3_executor.py` | `60C78B6F0281` | 43289 | 2026-09-24 21:15:11 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r3_result.json` | `6E01255B80C9` | 44888 | 2026-09-24 21:25:24 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r4_executor.py` | `4F5269BA8F18` | 46811 | 2026-09-24 21:28:35 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r4_result.json` | `9C800874701A` | 46927 | 2026-09-24 21:38:53 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r5_executor.py` | `91C72F8AD209` | 49138 | 2026-09-24 21:43:59 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r5_result.json` | `664355F29AB9` | 67897 | 2026-09-24 21:54:45 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r6_executor.py` | `5F02C7E0F094` | 47242 | 2026-09-24 21:59:06 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch1_r6_result.json` | `6B92BBFF7180` | 57925 | 2026-09-25 00:27:42 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch1_result.json` | `22EB01144062` | 46518 | 2026-09-24 20:56:34 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r1_executor.py` | `D4DD5C949443` | 56894 | 2026-09-26 16:32:01 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r1_result.json` | `14DDDB13D658` | 68329 | 2026-09-26 16:36:02 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r2_executor.py` | `BB601B4F5ECB` | 58073 | 2026-09-26 16:49:05 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r2_result.json` | `400EE4D21FC9` | 69460 | 2026-09-26 16:53:10 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r3_executor.py` | `EEF1475E325C` | 58539 | 2026-09-26 16:56:53 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r3_result.json` | `88A06F08928F` | 70658 | 2026-09-26 17:00:02 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r4_executor.py` | `4F68937D7A95` | 68856 | 2026-09-26 17:06:19 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r4_result.json` | `9D91A8DC039A` | 74733 | 2026-09-26 17:09:13 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r5_executor.py` | `04383377B6A2` | 70471 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch10_r5_result.json` | `7F02E08FC0DA` | 74979 | 2026-09-26 17:18:27 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r1_executor.py` | `E52F930654D3` | 50808 | 2026-09-24 22:34:16 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r1_result.json` | `D245AE4CE385` | 4128 | 2026-09-24 22:35:43 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r2_executor.py` | `E7418F47A130` | 55317 | 2026-09-24 22:44:56 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r2_models_probe.err.log` | `E3B0C44298FC` | 0 | 2026-09-24 22:40:11 | 核查＋读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r2_models_probe.json` | `3C9DC60B5071` | 1503 | 2026-09-24 22:40:12 | 核查＋读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r2_models_probe.log` | `5664C63102A0` | 1260 | 2026-09-24 22:40:12 | 核查＋读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r2_models_probe.py` | `A31D54A4B765` | 5334 | 2026-09-27 20:26:47 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r2_result.json` | `8C125E257AF8` | 62887 | 2026-09-24 22:51:00 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json` | `21A89EB36A14` | 2635 | 2026-09-24 22:43:10 | 核查＋读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r3_executor.py` | `72FD2BB3838E` | 56467 | 2026-09-24 23:12:40 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r3_result.json` | `25251ACA6D79` | 62886 | 2026-09-24 23:23:19 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r4_executor.py` | `D9FE7AA2D292` | 58176 | 2026-09-24 23:26:12 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r4_result.json` | `15B8DDC5BA9E` | 63572 | 2026-09-24 23:30:50 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r5_executor.py` | `BF1E4FE02402` | 60046 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r5_result.json` | `479F4119CF72` | 64285 | 2026-09-24 23:39:39 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r6_executor.py` | `E38D068F309C` | 63788 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch2_r6_result.json` | `E37D9C74C3E5` | 65083 | 2026-09-24 23:50:52 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r1_executor.py` | `0C284A3DCE21` | 61899 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r1_result.json` | `D24B84671C23` | 66520 | 2026-09-24 23:38:45 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r2_executor.py` | `B1699098C53B` | 64634 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r2_result.json` | `58E9C55A770D` | 67767 | 2026-09-24 23:51:13 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r3_executor.py` | `3B7381CE5FE8` | 66396 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r3_result.json` | `6E677FFCC880` | 68488 | 2026-09-25 00:01:27 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r4_executor.py` | `C79B5C274A10` | 68874 | 2026-09-25 01:01:33 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r4_result.json` | `0E47768640D3` | 69635 | 2026-09-25 01:05:56 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r5_executor.py` | `B7478168F87F` | 72156 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch3_r5_result.json` | `38998F994B84` | 70064 | 2026-09-25 01:23:36 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r1_executor.py` | `E84BFFD5DC7D` | 66097 | 2026-09-24 23:35:04 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r1_result.json` | `7D9FE9D319A2` | 71775 | 2026-09-24 23:41:34 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r2_executor.py` | `7D8E12267790` | 66774 | 2026-09-24 23:49:42 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r2_result.json` | `6A9A362D9869` | 71998 | 2026-09-24 23:55:28 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r3_executor.py` | `B5E1C3637405` | 68560 | 2026-09-25 00:02:06 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r3_result.json` | `ED5267DF7D6F` | 72884 | 2026-09-25 00:08:49 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r4_executor.py` | `184186902A9F` | 73379 | 2026-09-25 01:08:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r4_result.json` | `41E0BA55E205` | 74448 | 2026-09-25 01:20:35 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r5_executor.py` | `8A505613B476` | 78984 | 2026-09-25 01:27:34 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r5_result.json` | `BAD01F2B89FD` | 76138 | 2026-09-25 01:34:21 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r5_verify.py` | `60D19AEEE6F5` | 3050 | 2026-09-25 01:35:07 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r6_executor.py` | `7F2C5E26E6C5` | 80877 | 2026-09-25 01:44:02 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r6_result.json` | `6B8093FF8962` | 32369 | 2026-09-25 01:44:37 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch4_r6_verify.py` | `222972125231` | 4712 | 2026-09-25 01:45:49 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r1_executor.py` | `DAC0648507B9` | 63517 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r1_result.json` | `120D45D1774F` | 71021 | 2026-09-24 23:36:37 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r2_executor.py` | `4C40334929BB` | 66252 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r2_result.json` | `B0F76B5C3522` | 72550 | 2026-09-24 23:52:24 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r3_executor.py` | `ED9557830F8B` | 66454 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r3_result.json` | `8E2ACDACFA1E` | 73682 | 2026-09-25 00:03:51 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r4_executor.py` | `28844C34B12B` | 67894 | 2026-09-25 01:01:38 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r4_result.json` | `1C62520C372B` | 74100 | 2026-09-25 01:04:23 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r5_executor.py` | `82C283D8F37A` | 77033 | 2026-09-25 01:08:52 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch5_r5_result.json` | `C874D21A4CBE` | 77137 | 2026-09-25 01:11:16 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r1_executor.py` | `AD35565F1EC9` | 49296 | 2026-09-25 00:28:11 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r1_result.json` | `0D29E1AB4AE2` | 57799 | 2026-09-25 00:39:57 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r2_executor.py` | `93C931FC3B1C` | 53494 | 2026-09-25 01:01:58 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r2_report.md` | `080F9CAF313C` | 6460 | 2026-09-25 01:15:52 | 读数/结果＋报告＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r2_result.json` | `96E1DE46ED30` | 64672 | 2026-09-25 01:14:34 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r3_executor.py` | `1385D2CA356F` | 53717 | 2026-09-25 01:27:17 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r3_report.md` | `6EF770D61308` | 6354 | 2026-09-25 01:39:41 | 读数/结果＋报告＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r3_result.json` | `15A7FECDFFE7` | 64975 | 2026-09-25 01:38:53 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r4_executor.py` | `08F329B36E9D` | 54588 | 2026-09-25 01:42:04 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r4_report.md` | `0D0EDC68CD35` | 7019 | 2026-09-25 01:53:59 | 读数/结果＋报告＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r4_result.json` | `B7377BA019A1` | 65254 | 2026-09-25 01:53:14 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r5_executor.py` | `8A8BABB911B8` | 57783 | 2026-09-25 01:56:05 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r5_report.md` | `D339D7286AD8` | 8596 | 2026-09-25 02:08:01 | 读数/结果＋报告＋成果件面 |
| `results\_v4_supp_l14v3_batch6_r5_result.json` | `E40424BF8ABE` | 65651 | 2026-09-25 02:07:09 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r1_executor.py` | `C49FC9BCA8C4` | 51545 | 2026-09-25 02:13:59 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r1_result.json` | `3558A1D15867` | 61114 | 2026-09-25 02:18:50 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r2_executor.py` | `35CDA0C0F7DA` | 53145 | 2026-09-25 02:26:48 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r2_result.json` | `924F12C4E7AB` | 61458 | 2026-09-25 02:31:15 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r3_executor.py` | `5C0B426E2EE0` | 51271 | 2026-09-25 02:41:04 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r3_result.json` | `B431A1BA54DF` | 61389 | 2026-09-25 02:46:39 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r4_executor.py` | `D789F9BD4FA1` | 51289 | 2026-09-25 03:06:20 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r4_result.json` | `0FE4C1339D88` | 61824 | 2026-09-25 03:13:45 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r5_executor.py` | `38710A448E9C` | 53155 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch7_r5_result.json` | `09A481EBCA6B` | 61658 | 2026-09-25 03:29:41 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r1_executor.py` | `1E5F2249C517` | 56181 | 2026-09-25 02:21:24 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r1_result.json` | `E6A94A0A13B7` | 62531 | 2026-09-25 02:21:40 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r2_executor.py` | `6A9BBC43C808` | 57634 | 2026-09-25 02:35:52 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r2_result.json` | `7B23996B5F4C` | 63440 | 2026-09-25 02:36:27 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r3_executor.py` | `0F654D945F12` | 58494 | 2026-09-25 02:50:01 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r3_result.json` | `56FAF9324FBA` | 63670 | 2026-09-25 03:00:00 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r4_executor.py` | `6B69EC8406D4` | 59351 | 2026-09-25 03:13:26 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r4_result.json` | `C7D5AA2A9B00` | 64038 | 2026-09-25 03:18:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r5_executor.py` | `6961281824AE` | 60475 | 2026-09-25 03:32:20 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch8_r5_result.json` | `3620A7DAF9C1` | 63785 | 2026-09-25 03:37:47 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r1_executor.py` | `E78CA71BD077` | 60645 | 2026-09-26 16:38:53 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r1_result.json` | `7E8DFE0156CD` | 69251 | 2026-09-26 16:38:42 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r2_executor.py` | `7EEC235A9CA2` | 60580 | 2026-09-26 16:48:39 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r2_result.json` | `08B0AAAAE726` | 69325 | 2026-09-26 16:56:40 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r3_executor.py` | `CFE41DD4FE62` | 62131 | 2026-09-26 17:01:28 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r3_result.json` | `29E0D865A7BF` | 69984 | 2026-09-26 17:08:33 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r4_executor.py` | `1B3FCFBACD59` | 64538 | 2026-09-26 17:14:29 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r4_result.json` | `EB8B13D9F592` | 71093 | 2026-09-26 17:23:11 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r5_executor.py` | `9B1A82A28DFB` | 65672 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_l14v3_batch9_r5_result.json` | `1610F5060EF1` | 72047 | 2026-09-26 17:34:59 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_model_mapping_2026_09_24.md` | `9BA12A0FBAC1` | 49326 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_l14v3_n26_verdict.md` | `DF6453D57F8A` | 65978 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | `E7C3E2EF4E6B` | 62847 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md` | `843E42EF4D2A` | 21309 | 2026-09-24 20:34:15 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | 52942 | 2026-09-24 20:29:16 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936B630015` | 14234 | 2026-09-24 20:27:29 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_T15_2026_09_24.md` | `8898B964A9D9` | 76991 | 2026-09-24 23:48:31 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` | `443EFB39804A` | 20751 | 2026-09-24 23:48:54 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_T15r2_2026_09_26.md` | `883DCED872B4` | 97059 | 2026-09-26 16:38:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md` | `F6ED61C25572` | 34195 | 2026-09-26 16:36:21 | 读数/结果＋成果件面 |
| `results\_v4_supp_t1_executor.py` | `91B8F70E4E18` | 60563 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t1_result.json` | `D6CB03A4657E` | 82365 | 2026-09-24 22:32:37 | 读数/结果＋成果件面 |
| `results\_v4_supp_t1_verdict.md` | `0AD42625F333` | 29106 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_t15_executor.py` | `558E635F9BA6` | 62285 | 2026-09-24 23:57:30 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | `7DA23C0E94CF` | 66317 | 2026-09-29 11:12:41 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15_executor_r1_2026_09_27.py` | `6D22444C65AF` | 67517 | 2026-09-27 20:51:43 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | `9E89E021EA03` | 70056 | 2026-09-28 15:46:02 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15_executor_r3_2026_09_28.py` | `B86CCE242ABE` | 70056 | 2026-09-28 17:25:01 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15_result.json` | `6B47D389B7AE` | 53265 | 2026-09-25 00:44:39 | 读数/结果＋成果件面 |
| `results\_v4_supp_t15_verdict.md` | `3CB5C2F59961` | 54377 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_supp_t15r2_executor.py` | `4B5B720D5CDA` | 84884 | 2026-09-26 16:50:49 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | `678032F726A8` | 89083 | 2026-09-29 11:12:41 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15r2_executor_r1_2026_09_28.py` | `E0936A68FA82` | 90390 | 2026-09-28 15:14:04 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | `215DB16A0556` | 92915 | 2026-09-28 15:44:50 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15r2_executor_r3_2026_09_28.py` | `4F514B3FB4B8` | 92915 | 2026-09-28 17:25:01 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_supp_t15r2_methodology_template.md` | `6F9B865280A3` | 17411 | 2026-09-27 11:40:23 | 读数/结果＋成果件面 |
| `results\_v4_supp_t15r2_result.json` | `C69AB0E3002E` | 73526 | 2026-09-26 17:15:40 | 读数/结果＋成果件面 |
| `results\_v4_supp_t15r2_verdict.md` | `963725DBD82A` | 65638 | 2026-09-30 16:15:20 | 读数/结果＋成果件面 |
| `results\_v4_track2_endpoints_probe.py` | `E7A6EB42C0AF` | 20738 | 2026-09-27 20:26:47 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v4_track2_models_probe.py` | `DA62ABAA1E03` | 3191 | 2026-09-27 20:27:07 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v4_track2_multimodel_rerun.py` | `5C0983EAAF11` | 38719 | 2026-09-27 20:26:47 | 读数/结果＋执行体＋成果件面 |
| `results\_v4_track2_multimodel_rerun_2026_09_23.json` | `E3DAE2A4BBC2` | 35011 | 2026-09-23 15:26:47 | 读数/结果＋成果件面 |
| `results\_v4_track2_multimodel_verdict_2026_09_23.md` | `44D9BAD9039B` | 12883 | 2026-09-23 15:27:54 | 读数/结果＋成果件面 |
| `results\_v4_track2_reprobe.py` | `F92CC93F1304` | 2860 | 2026-09-27 20:27:07 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v4_trae_remaining_audit_2026_09_28.md` | `1A8648083228` | 39681 | 2026-09-28 15:28:25 | 核查＋读数/结果＋成果件面 |
| `results\_v4s3_shadowing_priority_assessment_2026_10_01.md` | `2AAAC67603CE` | 20111 | 2026-10-01 14:30:41 | 读数/结果＋成果件面 |
| `results\_v5_a_system_default_register_2026_09_28.md` | `8C22796A42F5` | 19892 | 2026-09-28 23:00:28 | 登记＋读数/结果＋成果件面 |
| `results\_v5_agent_trio_post_reorg_note_2026_09_29.md` | `9C7182D93049` | 9795 | 2026-09-29 14:17:11 | 读数/结果＋成果件面 |
| `results\_v5_alias_table_d01_d04_c01_c03_2026_09_29.md` | `B3E39064D7C5` | 15315 | 2026-09-29 14:10:27 | 读数/结果＋成果件面 |
| `results\_v5_anchor_drift_backfill_2026_09_28.md` | `6F1EDD1CCEBB` | 14438 | 2026-09-28 22:59:46 | 读数/结果＋成果件面 |
| `results\_v5_b12_verify_pack_q1_q3_q4_2026_09_29.md` | `698262E6FE8B` | 33803 | 2026-09-29 16:32:42 | 核查＋读数/结果＋成果件面 |
| `results\_v5_b14_08c_material_plan_2026_09_29.md` | `B69D65CBB329` | 22104 | 2026-09-29 17:26:18 | 读数/结果＋成果件面 |
| `results\_v5_b14_3_v1_4_prereg_2026_09_29.md` | `0F1665E7056F` | 20045 | 2026-09-29 16:55:29 | 读数/结果＋成果件面 |
| `results\_v5_b14_4_v1_3_prereg_2026_09_29.md` | `AE474BF48C62` | 20043 | 2026-09-29 16:55:31 | 读数/结果＋成果件面 |
| `results\_v5_b14_p41c_independent_judgment_2026_09_29.md` | `B752582BC692` | 22437 | 2026-09-29 19:13:24 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_v5_b15_offsite_readonly_authorization_2026_09_29.md` | `96A069701B3D` | 18483 | 2026-09-29 17:33:36 | 读数/结果＋成果件面 |
| `results\_v5_b15_offsite_readonly_authorization_activation_2026_09_29.md` | `99978EB15C10` | 35006 | 2026-09-29 19:40:50 | 读数/结果＋成果件面 |
| `results\_v5_b15_pp1_impl_fix_2026_09_29.md` | `DED842B6241C` | 12911 | 2026-09-29 17:33:06 | 读数/结果＋成果件面 |
| `results\_v5_b17_fault_register_2026_09_29.md` | `48CB0AB5F317` | 18129 | 2026-09-29 17:01:39 | 登记＋读数/结果＋成果件面 |
| `results\_v5_b17_recheck12_register_2026_09_29.md` | `73242A890BE9` | 19981 | 2026-09-29 17:02:29 | 登记＋核查＋读数/结果＋成果件面 |
| `results\_v5_b18_o8_semantic_verify_2026_09_29.md` | `49D4ADF8F197` | 26544 | 2026-09-29 20:34:46 | 核查＋读数/结果＋成果件面 |
| `results\_v5_b18_o8_semantic_verify_r2_2026_09_29.md` | `DC1233D0AB4F` | 24145 | 2026-09-29 20:46:30 | 核查＋读数/结果＋成果件面 |
| `results\_v5_b20_gamma_a_attribution_2026_09_29.md` | `7BAD6E52A0F3` | 30789 | 2026-09-29 17:31:42 | 勘误＋读数/结果＋成果件面 |
| `results\_v5_b20_gamma_a_rereview_2026_09_29.md` | `B22DDA133038` | 30680 | 2026-09-29 19:01:52 | 评审＋读数/结果＋成果件面 |
| `results\_v5_b22_r05_path_backfill_2026_09_29.md` | `09B3105ACB6F` | 12233 | 2026-09-29 18:18:33 | 读数/结果＋成果件面 |
| `results\_v5_b22_r07_four_cond_prereg_2026_09_29.md` | `CEEA8F4534FB` | 23151 | 2026-09-29 18:27:58 | 读数/结果＋成果件面 |
| `results\_v5_b35_result_attribution_2026_09_29.md` | `EC358F6F76A3` | 35313 | 2026-09-29 17:48:32 | 勘误＋读数/结果＋成果件面 |
| `results\_v5_bom_u1_exec_2026_09_29.md` | `5B0282960D52` | 22730 | 2026-09-29 10:48:46 | 读数/结果＋成果件面 |
| `results\_v5_bom_u1_exec_2026_09_29.py` | `C140A28E15AE` | 31134 | 2026-09-29 10:46:21 | 读数/结果＋执行体＋成果件面 |
| `results\_v5_bulk_activation_2026_09_28.md` | `B5A50447B4DA` | 39378 | 2026-09-30 17:02:47 | 读数/结果＋成果件面 |
| `results\_v5_c3_reading_b_prereg_2026_09_28.md` | `8DCF5E1E6DDE` | 32178 | 2026-09-30 17:02:47 | 读数/结果＋成果件面 |
| `results\_v5_checkpoint_tail3_revision_2026_09_29.md` | `C962851FF3FF` | 27966 | 2026-09-29 11:24:06 | 核查＋读数/结果＋成果件面 |
| `results\_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md` | `C514B321FE10` | 18271 | 2026-09-29 19:24:07 | 读数/结果＋成果件面 |
| `results\_v5_clearance_mr11_doc_calibration_2026_09_29.md` | `C4BCE5A5E8BE` | 14974 | 2026-09-29 19:30:58 | 读数/结果＋成果件面 |
| `results\_v5_clearance_mr14_rerun_note_2026_09_29.md` | `F3DD5EFD3E34` | 22894 | 2026-09-29 19:12:01 | 读数/结果＋成果件面 |
| `results\_v5_clearance_mr19_sha1_note_2026_09_29.md` | `C74FFC6278A8` | 22859 | 2026-09-29 19:21:08 | 读数/结果＋成果件面 |
| `results\_v5_clearance_mr3_s40_fix_note_2026_09_29.md` | `B1244981065B` | 15522 | 2026-09-29 19:20:43 | 读数/结果＋成果件面 |
| `results\_v5_clearance_o15_ready_pack_2026_09_29.md` | `618E5990B3E5` | 48968 | 2026-09-29 18:19:44 | 读数/结果＋成果件面 |
| `results\_v5_clearance_pending_backlog_register_2026_09_29.md` | `1132072288DE` | 32369 | 2026-09-29 20:52:20 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_readme_c5_register_2026_09_29.md` | `ABABDAA392CA` | 8730 | 2026-09-29 21:09:27 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round1_b19_register_2026_09_29.md` | `B69EC2DDC9BE` | 28556 | 2026-09-29 18:08:51 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round11_register_2026_09_29.md` | `2E5E6F8B328E` | 59923 | 2026-09-29 19:12:41 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round12_14_register_2026_09_29.md` | `13D741979EBB` | 75131 | 2026-09-29 19:32:25 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round15_18_register_2026_09_29.md` | `3A3C9C734BF9` | 99989 | 2026-09-29 20:32:07 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round2_3_register_2026_09_29.md` | `32CA90E63A56` | 37340 | 2026-09-29 18:25:58 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round4_5_register_2026_09_29.md` | `9D381FAB5F46` | 52782 | 2026-09-29 18:35:54 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round6_register_2026_09_29.md` | `68FE5B397DF3` | 38248 | 2026-09-29 18:43:49 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round7_8_register_2026_09_29.md` | `60CDEEF91D4A` | 63311 | 2026-09-29 18:53:57 | 登记＋读数/结果＋成果件面 |
| `results\_v5_clearance_round9_10_register_2026_09_29.md` | `428E0857EBB7` | 68512 | 2026-09-29 19:03:45 | 登记＋读数/结果＋成果件面 |
| `results\_v5_closing_register_2026_09_28.md` | `522B08506290` | 27224 | 2026-09-30 17:02:47 | 登记＋读数/结果＋成果件面 |
| `results\_v5_closing_register_r2_2026_09_28.md` | `1094EDB6E8C0` | 25446 | 2026-09-30 17:02:47 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b1_decisions_register_2026_09_29.md` | `62CA213BB56C` | 28469 | 2026-09-29 13:09:11 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b10_decisions_register_2026_09_29.md` | `67EA81A2E6D9` | 13282 | 2026-09-29 14:18:35 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b11_decisions_register_2026_09_29.md` | `07E9FE512DA5` | 12276 | 2026-09-29 14:20:13 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b12_decisions_register_2026_09_29.md` | `DB0D6E56A497` | 15898 | 2026-09-29 14:24:50 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b13_b22_anchor_verify_2026_09_29.md` | `A0C2D1D5FE6B` | 16393 | 2026-09-29 15:26:00 | 核查＋读数/结果＋成果件面 |
| `results\_v5_confirm_b13_b22_exec_queue_2026_09_29.md` | `56549B04A925` | 39531 | 2026-09-29 16:59:11 | 读数/结果＋成果件面 |
| `results\_v5_confirm_b13_decisions_register_2026_09_29.md` | `C7CA4FBECC8B` | 33086 | 2026-09-29 15:14:58 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b14_b15_decisions_register_2026_09_29.md` | `E48276A8DD31` | 26154 | 2026-09-29 15:21:25 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b16_b17_decisions_register_2026_09_29.md` | `8E36A3E4C6FF` | 29624 | 2026-09-29 15:22:32 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b18_b19_decisions_register_2026_09_29.md` | `AE160194878E` | 21072 | 2026-09-29 15:23:32 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b2_decisions_register_2026_09_29.md` | `63DED68919DF` | 28383 | 2026-09-29 13:13:58 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b20_b22_decisions_register_2026_09_29.md` | `FCCAAC464565` | 24883 | 2026-09-29 15:24:33 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b3_decisions_register_2026_09_29.md` | `4DBB11C219FC` | 34015 | 2026-09-29 13:24:45 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b4_decisions_register_2026_09_29.md` | `4D02F9DF594E` | 43498 | 2026-09-29 13:33:06 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b5_decisions_register_2026_09_29.md` | `3B5F2819AF8F` | 45525 | 2026-09-29 13:43:30 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b7_decisions_register_2026_09_29.md` | `0A80AE035042` | 23833 | 2026-09-29 14:04:02 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b8_decisions_register_2026_09_29.md` | `6862659FF900` | 15106 | 2026-09-29 14:11:28 | 登记＋读数/结果＋成果件面 |
| `results\_v5_confirm_b9_decisions_register_2026_09_29.md` | `8C510CDA6014` | 17008 | 2026-09-29 14:13:01 | 登记＋读数/结果＋成果件面 |
| `results\_v5_ea_review_chain_rules_2026_09_29.md` | `8E235F520FB9` | 11511 | 2026-09-29 14:13:43 | 评审＋读数/结果＋成果件面 |
| `results\_v5_exec_f2_r3_register_2026_09_29.md` | `9D64EE1D6996` | 24177 | 2026-09-29 10:54:17 | 登记＋读数/结果＋成果件面 |
| `results\_v5_fake_verdict_forensics_2026_09_28.md` | `1B135D8B1E08` | 35870 | 2026-09-28 23:22:52 | 读数/结果＋成果件面 |
| `results\_v5_fake_verdict_session_log_2026_09_28.md` | `132BFA0C02F5` | 18877 | 2026-09-30 17:02:47 | 读数/结果＋成果件面 |
| `results\_v5_fake_verdict_v1x_prereg_2026_09_28.md` | `088085D6C90D` | 28484 | 2026-09-30 17:02:47 | 读数/结果＋成果件面 |
| `results\_v5_familyline_r01_r02_independent_judgment_2026_09_29.md` | `E16E50329C88` | 25392 | 2026-09-29 19:40:23 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_v5_gamma_end1_rb_clause_addendum_2026_09_29.md` | `BF38E5F0161E` | 10397 | 2026-09-29 14:08:53 | 读数/结果＋成果件面 |
| `results\_v5_gamma_r1_v2_withdraw_2026_09_29.md` | `F4EF22A5F97C` | 24611 | 2026-09-29 10:59:20 | 读数/结果＋成果件面 |
| `results\_v5_gt_exec_2026_09_29.json` | `01E95E49B035` | 142217 | 2026-09-29 11:18:07 | 读数/结果＋成果件面 |
| `results\_v5_gt_exec_2026_09_29.md` | `9A679F43F796` | 27701 | 2026-09-29 11:21:06 | 读数/结果＋成果件面 |
| `results\_v5_gt_p10_lowarm_prereg_2026_09_29.md` | `07E28E2FE374` | 38464 | 2026-09-29 13:58:52 | 读数/结果＋成果件面 |
| `results\_v5_gt_verdict_2026_09_29.md` | `45648B0EC940` | 57227 | 2026-09-29 11:41:25 | 读数/结果＋成果件面 |
| `results\_v5_gt33_attrib_fill_prereg_2026_09_29.md` | `48742D6CBD03` | 36984 | 2026-09-29 12:14:15 | 读数/结果＋成果件面 |
| `results\_v5_gt33_d5_crossref_note_2026_09_29.md` | `DD50FF801EF7` | 10989 | 2026-09-29 13:55:24 | 读数/结果＋成果件面 |
| `results\_v5_gt4_reattrib_2026_09_29.json` | `4B75DF5F7454` | 3074 | 2026-09-29 11:18:07 | 读数/结果＋成果件面 |
| `results\_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md` | `2505FF5D203F` | 63447 | 2026-09-28 20:14:25 | 读数/结果＋成果件面 |
| `results\_v5_gt5_reattrib_2026_09_29.json` | `E15B3B171D60` | 5626 | 2026-09-29 11:18:07 | 读数/结果＋成果件面 |
| `results\_v5_gt5b_reattrib_2026_09_29.json` | `212E5BB8C7D7` | 7084 | 2026-09-29 11:18:07 | 读数/结果＋成果件面 |
| `results\_v5_gt6_trajint_2026_09_29.json` | `578FBEAA4635` | 83722 | 2026-09-29 11:18:07 | 读数/结果＋成果件面 |
| `results\_v5_gt8_expand_2026_09_29.json` | `34FF826F97C2` | 20090 | 2026-09-29 11:18:07 | 读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_exec_2026_09_29.md` | `365EA6CB77E8` | 21542 | 2026-09-29 15:34:42 | 读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_result_2026_09_29.json` | `C68076C88140` | 26253 | 2026-09-29 15:21:52 | 读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` | `C68076C88140` | 26253 | 2026-09-29 15:21:52 | 读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json` | `24B0D5EDA48A` | 28638 | 2026-09-29 15:29:24 | 读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_resultb_2026_09_29.json` | `8AA69A5E922D` | 48948 | 2026-09-29 15:32:44 | 读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_seta_verify_2026_09_29.json` | `D1370B0A3853` | 9001 | 2026-09-29 15:33:32 | 核查＋读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_verdict_2026_09_29.md` | `9140B6E5970B` | 32653 | 2026-09-29 15:50:16 | 读数/结果＋成果件面 |
| `results\_v5_gt8_lowarm_verdict_r2_2026_09_29.md` | `AFF727434AA4` | 40282 | 2026-09-29 19:32:56 | 读数/结果＋成果件面 |
| `results\_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md` | `31E5BD7B4003` | 14481 | 2026-09-29 14:05:11 | 读数/结果＋成果件面 |
| `results\_v5_h231_r07_independent_judgment_2026_09_29.md` | `70025895600A` | 37949 | 2026-09-29 19:07:37 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_v5_item05_prereg_2026_09_28.md` | `567F0F177699` | 19115 | 2026-09-28 19:34:42 | 读数/结果＋成果件面 |
| `results\_v5_item21_anchor_recompute_2026_09_28.json` | `47177CAB0303` | 9527 | 2026-09-28 20:03:28 | 核查＋读数/结果＋成果件面 |
| `results\_v5_item21_anchor_recompute_2026_09_28.md` | `E5623D4BD3F3` | 9221 | 2026-09-28 20:04:46 | 核查＋读数/结果＋成果件面 |
| `results\_v5_item21_asset_recovery_2026_09_28.md` | `6C80FF43BDD7` | 8793 | 2026-09-28 19:51:41 | 读数/结果＋成果件面 |
| `results\_v5_item21_patched_recompute_2026_09_28.json` | `AA53E5DB77C9` | 14879 | 2026-09-28 20:26:23 | 核查＋读数/结果＋成果件面 |
| `results\_v5_item21_patched_recompute_2026_09_28.md` | `2C1D85913CCC` | 15895 | 2026-09-28 20:27:30 | 核查＋读数/结果＋成果件面 |
| `results\_v5_item21_rerun_conditions_prereg_2026_09_28.md` | `4185BDAD6DF5` | 31429 | 2026-09-28 23:00:28 | 读数/结果＋成果件面 |
| `results\_v5_item21_strategyqa_realias_recompute_2026_09_29.json` | `49F068C716A8` | 34314 | 2026-09-29 16:17:02 | 核查＋读数/结果＋成果件面 |
| `results\_v5_item21_strategyqa_realias_recompute_2026_09_29.md` | `4E941D0A9C48` | 14639 | 2026-09-29 16:17:29 | 核查＋读数/结果＋成果件面 |
| `results\_v5_item21_strategyqa_realias_verdict_2026_09_29.md` | `26EAA156108F` | 32354 | 2026-09-29 16:45:55 | 读数/结果＋成果件面 |
| `results\_v5_item21_verdict_2026_09_28.md` | `DE274BD38955` | 28155 | 2026-09-28 21:30:15 | 读数/结果＋成果件面 |
| `results\_v5_item26b_attribution_effective_2026_09_28.md` | `C353FBCDC753` | 35261 | 2026-09-28 22:29:35 | 勘误＋读数/结果＋成果件面 |
| `results\_v5_item26b_endpoint_definition_prereg_2026_09_28.md` | `5E59A11466DB` | 38939 | 2026-09-28 21:32:27 | 读数/结果＋成果件面 |
| `results\_v5_item26b_literal_gap_prereg_v2_2026_09_28.md` | `BB0A211FA675` | 38885 | 2026-09-28 20:24:02 | 读数/结果＋成果件面 |
| `results\_v5_item35_prereg_v2_2026_09_28.md` | `1FB2419C6E96` | 35633 | 2026-09-28 22:22:11 | 读数/结果＋成果件面 |
| `results\_v5_item35_v2_matrix_exec_2026_09_29.md` | `4E88682284D8` | 24624 | 2026-09-29 12:27:44 | 读数/结果＋成果件面 |
| `results\_v5_item35_v2_matrix_result_2026_09_29.json` | `13AD5B740F80` | 84699 | 2026-09-29 12:27:24 | 读数/结果＋成果件面 |
| `results\_v5_item35_v2_verdict_2026_09_29.md` | `B59BEF293712` | 26232 | 2026-09-29 12:56:02 | 读数/结果＋成果件面 |
| `results\_v5_item35_v3_collinear_exec_2026_09_29.md` | `912AFFFED6B9` | 46000 | 2026-09-29 15:13:22 | 读数/结果＋成果件面 |
| `results\_v5_item35_v3_collinear_prereg_2026_09_29.md` | `873652FD39DD` | 42504 | 2026-09-29 13:56:34 | 读数/结果＋成果件面 |
| `results\_v5_item35_v3_collinear_recompute_2026_10_01.json` | `A210E2C41275` | 49682 | 2026-10-01 08:55:37 | 核查＋读数/结果＋成果件面 |
| `results\_v5_item35_v3_collinear_result_2026_09_29.json` | `99F3E504589E` | 187287 | 2026-09-29 14:29:52 | 读数/结果＋成果件面 |
| `results\_v5_item35_v3_collinear_verdict_2026_10_01.md` | `363CCE3DAE59` | 38266 | 2026-10-01 09:05:02 | 读数/结果＋成果件面 |
| `results\_v5_item35_v3_collinear_verdict_prep_2026_10_01.md` | `A31026F2384D` | 33755 | 2026-10-01 08:57:30 | 读数/结果＋成果件面 |
| `results\_v5_item36_prereg_2026_09_28.md` | `7F42D5EE131C` | 18141 | 2026-09-28 19:35:54 | 读数/结果＋成果件面 |
| `results\_v5_loadcorpus_fix_2026_09_29.md` | `E47614CCF5FF` | 17355 | 2026-09-29 11:58:05 | 读数/结果＋成果件面 |
| `results\_v5_loadcorpus_switch_2026_09_29.md` | `D37E97644BF8` | 16414 | 2026-09-29 12:13:38 | 读数/结果＋成果件面 |
| `results\_v5_paper_remedy_line_orchestration_2026_09_29.md` | `D911674E68CF` | 48292 | 2026-09-29 14:02:32 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v5_paper_remedy_r1_pledge_2026_09_29.md` | `816CB91D4611` | 47778 | 2026-09-29 16:36:25 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` | `29DA2CA8932F` | 34647 | 2026-09-29 15:49:34 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v5_paper_remedy_r6b_x27_sourcetrace_2026_09_29.md` | `B75CC49B360F` | 16125 | 2026-09-29 17:10:36 | 论文/脚本文本＋读数/结果＋成果件面 |
| `results\_v5_pd_v04_root_naming_candidates_2026_09_29.md` | `46599DDE51A8` | 14312 | 2026-09-29 14:06:13 | 读数/结果＋成果件面 |
| `results\_v5_pi_decision_trace_gap_audit_2026_09_29.md` | `38B043C4BE6A` | 33101 | 2026-09-29 13:53:25 | 核查＋读数/结果＋成果件面 |
| `results\_v5_pjpm_pc_closeout_readout_2026_09_29.md` | `1B9AC6B07670` | 32243 | 2026-09-29 13:46:56 | 读数/结果＋成果件面 |
| `results\_v5_pjpm_pc_deg_prereg_2026_09_29.md` | `989EE2BCE660` | 59446 | 2026-09-29 12:17:51 | 读数/结果＋成果件面 |
| `results\_v5_pjpm_pc_degen_precheck_executor_2026_09_29.py` | `F58B0D1C1A93` | 76822 | 2026-09-29 13:46:42 | 核查＋读数/结果＋执行体＋成果件面 |
| `results\_v5_pjpm_pc_degen_precheck_result_2026_09_29.json` | `3641AFE9D49C` | 103747 | 2026-09-29 13:46:56 | 核查＋读数/结果＋成果件面 |
| `results\_v5_pjpm_pc_reverify_bang2_2026_09_29.md` | `6833CAE407E8` | 39517 | 2026-09-29 14:14:27 | 核查＋读数/结果＋成果件面 |
| `results\_v5_pjpm_pc_verdict_bang3_2026_09_29.md` | `1814F9590F0F` | 41566 | 2026-09-29 14:27:08 | 读数/结果＋成果件面 |
| `results\_v5_pl2_fourband_prereg_2026_09_29.md` | `D5FDB89582FD` | 29253 | 2026-09-29 17:42:35 | 读数/结果＋成果件面 |
| `results\_v5_prereg_chain_activation_register_2026_09_28.md` | `3CC05F8CBD1A` | 27047 | 2026-09-28 22:10:58 | 登记＋读数/结果＋成果件面 |
| `results\_v5_prereg_chain_status_annotation_2026_09_28.md` | `CB4104938CC8` | 23857 | 2026-09-28 22:28:54 | 读数/结果＋成果件面 |
| `results\_v5_proxy_temp_T0.3.json` | `04D915714B96` | 143345 | 2026-09-23 11:59:01 | 读数/结果＋成果件面 |
| `results\_v5_proxy_temp_T1.5.json` | `2B36D8632A80` | 143261 | 2026-09-23 11:59:01 | 读数/结果＋成果件面 |
| `results\_v5_proxy_vocab_V50.json` | `2DEEDC43FC40` | 78182 | 2026-09-23 11:59:01 | 读数/结果＋成果件面 |
| `results\_v5_proxy_vocab_V500.json` | `4DDD6AFBF16B` | 78191 | 2026-09-23 11:59:01 | 读数/结果＋成果件面 |
| `results\_v5_r2h2_residual_merged_catalogue_2026_09_29.md` | `B62D19C1C7CC` | 50554 | 2026-09-29 14:29:32 | 读数/结果＋成果件面 |
| `results\_v5_r4_residual_merged_catalogue_2026_09_29.md` | `0C4BBD26EA55` | 102410 | 2026-09-29 16:43:51 | 读数/结果＋成果件面 |
| `results\_v5_recyclebin_sha12_completion_2026_09_29.md` | `5F3223A4B349` | 59551 | 2026-09-29 16:19:12 | 读数/结果＋成果件面 |
| `results\_v5_rj5_verdict_2026_09_29.md` | `9C1CCBD5CF5A` | 40057 | 2026-09-29 02:05:11 | 读数/结果＋成果件面 |
| `results\_v5_sha12_collision_statement_2026_09_29.md` | `F0F44CF6DC65` | 28155 | 2026-09-29 17:20:57 | 读数/结果＋成果件面 |
| `results\_v5_sub_artifact_ledger_2026_09_28.md` | `DD38C77EA486` | 71818 | 2026-09-30 17:02:47 | 登记＋读数/结果＋成果件面 |
| `results\_v5_sub_artifact_ledger_history_r1_2026_09_29.md` | `535B3C2AD102` | 48539 | 2026-09-29 10:56:50 | 登记＋读数/结果＋成果件面 |
| `results\_v5_sub_artifact_ledger_history_r2_2026_09_29.md` | `5FF7784DB145` | 150957 | 2026-09-29 11:42:24 | 登记＋读数/结果＋成果件面 |
| `results\_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `E04A46B02D13` | 128760 | 2026-09-29 12:44:15 | 登记＋读数/结果＋成果件面 |
| `results\_v5_sub_artifact_ledger_history_r4_2026_09_29.md` | `B6B8BE476A73` | 603599 | 2026-09-29 16:26:42 | 登记＋读数/结果＋成果件面 |
| `results\_v5_t1_decisions_register_2026_09_29.md` | `7DD7DD3FB721` | 31330 | 2026-09-29 11:34:08 | 登记＋读数/结果＋成果件面 |
| `results\_v5_theory_input_acquisition_request_2026_09_29.md` | `83AFC4802FE7` | 10691 | 2026-09-30 20:26:40 | 委托＋读数/结果＋成果件面 |
| `results\_v5_track2_qwen_retry_2026_09_29.json` | `6ACAFE021AAF` | 2735 | 2026-09-29 11:10:33 | 读数/结果＋成果件面 |
| `results\_v5_track2_qwen_retry_2026_09_29.md` | `C890771728F3` | 11957 | 2026-09-29 11:13:37 | 读数/结果＋成果件面 |
| `results\_v5_track2_qwen_retry_executor_20260929.py` | `D34B46E24A7C` | 11586 | 2026-09-29 11:10:20 | 读数/结果＋执行体＋成果件面 |
| `results\_v5_trae_doubt6_verify_2026_09_28_r3verifier.md` | `58101EF93A6F` | 30192 | 2026-09-30 17:02:47 | 核查＋读数/结果＋成果件面 |
| `results\_v5_v3_deg_c5_b_halt_report_2026_09_29.md` | `F2B68EE099B5` | 14862 | 2026-09-29 13:44:25 | 读数/结果＋报告＋成果件面 |
| `results\_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | `1088FDD2B197` | 744352 | 2026-10-01 09:21:49 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_c5_proposal_2026_09_29.md` | `2158B11BBA9A` | 33356 | 2026-09-29 13:25:19 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_fix_c1c4_result_2026_09_29.json` | `1B5BFECC818E` | 266417 | 2026-09-29 12:11:14 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_fix_exec_2026_09_29.md` | `7D885528F287` | 30261 | 2026-09-29 12:10:05 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_fix_prereg_2026_09_29.md` | `98286CC1AEC7` | 41622 | 2026-09-29 11:44:32 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_p1_reopen_exec_2026_09_29.md` | `38231EF6F053` | 33622 | 2026-09-29 13:45:42 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_p1_reopen_result_2026_09_29.json` | `B86D6740D487` | 571451 | 2026-09-29 13:41:39 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` | `63D898AB1B71` | 42645 | 2026-09-29 15:16:34 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` | `8ADAF4E5D868` | 44054 | 2026-09-29 15:24:27 | 读数/结果＋成果件面 |
| `results\_v5_v3_deg_p1_reopen_verify_2026_09_29.md` | `4AFEB8CD41DE` | 27898 | 2026-09-29 14:20:21 | 核查＋读数/结果＋成果件面 |
| `results\_v5_v3_deg_reopen_line_2026_09_29.md` | `2EA1C2CEE65D` | 42778 | 2026-09-29 13:17:28 | 读数/结果＋成果件面 |
| `results\_v5_v3_t1_effect_judgment_2026_09_29.md` | `1995BD4460AE` | 40697 | 2026-09-29 20:13:28 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_v5_v3deg_prereg_activation_register_2026_09_29.md` | `E587DA3B4CF8` | 24370 | 2026-09-29 12:19:34 | 登记＋读数/结果＋成果件面 |
| `results\_v5_v3r2_errata_note_2026_09_29.md` | `D687AD25A68C` | 29089 | 2026-09-29 20:12:47 | 勘误＋读数/结果＋成果件面 |
| `results\_v5_v4_export_filter_spec_2026_09_29.md` | `14DD6CCDBED6` | 22884 | 2026-09-29 17:04:12 | 读数/结果＋成果件面 |
| `results\_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md` | `79BCFF089F21` | 14620 | 2026-09-29 14:16:40 | 读数/结果＋成果件面 |
| `results\_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md` | `AC0D6F19F06C` | 22185 | 2026-09-29 15:18:09 | 核查＋读数/结果＋成果件面 |
| `results\_v5r_s40_recompute_2026_09_29.json` | `5BE465342AE1` | 4992 | 2026-09-29 19:19:15 | 核查＋读数/结果＋成果件面 |
| `results\_verdict_pack_d_prep_2026_10_01.md` | `119F98CD8D2D` | 49471 | 2026-10-01 13:22:05 | 读数/结果＋成果件面 |
| `results\_vk_current_counting_face_2026_10_10.md` | `4D4E41C3EFF5` | 24795 | 2026-10-10 21:35:11 | 读数/结果＋成果件面 |
| `results\_vk_face_category_erratum_2026_10_11.md` | `67BF70301889` | 17373 | 2026-10-11 00:15:40 | 勘误＋读数/结果＋成果件面 |
| `results\_vk_two_items_judgments_2026_10_09.md` | `82556D54726C` | 33399 | 2026-10-09 23:16:17 | 终判/裁定＋读数/结果＋成果件面 |
| `results\_wordlist_house_effectivity_note_2026_10_10.md` | `4E89A5BB4B68` | 14606 | 2026-10-10 12:01:03 | 读数/结果＋成果件面 |
| `results\_wordlist_house_establishment_draft_2026_10_10.md` | `AFA5EB53D216` | 38468 | 2026-10-10 02:43:26 | 读数/结果＋成果件面 |
| `results\_wrapup_cleanup_inventory_register_2026_09_29.md` | `6BEEB397A4C1` | 22556 | 2026-09-29 21:31:56 | 登记＋读数/结果＋成果件面 |
| `results\_zero_consumption_cells_field_correction_2026_10_10.md` | `36F9AC4EBBF6` | 12244 | 2026-10-10 20:17:54 | 勘误＋读数/结果＋成果件面 |
| `results\_zero_reading_judgment_2026_10_10.md` | `A9947F5677DF` | 27824 | 2026-10-10 21:28:00 | 终判/裁定＋读数/结果＋成果件面 |
| `results\boss_pa_1_rbr_rm_result_2026_09_15.json` | `C7C59E0D2F6C` | 8753 | 2026-09-15 15:28:10 | 读数/结果＋成果件面 |
| `results\boss_pa_2_potential_game_result_2026_09_15.json` | `5C76137D6430` | 7530 | 2026-09-15 15:28:10 | 读数/结果＋成果件面 |
| `results\boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `D6F233D73C45` | 9098 | 2026-09-15 15:28:10 | 读数/结果＋成果件面 |
| `results\boss_pc_1_a1_resampling_2026_09_15.json` | `D21912A05D79` | 1017 | 2026-09-15 13:34:48 | 读数/结果＋成果件面 |
| `results\boss_pc_1_real_2d_ising_2026_09_15.json` | `43D9CE160FC8` | 2460 | 2026-09-15 15:28:00 | 读数/结果＋成果件面 |
| `results\boss_pc_2_a2_fitting_2026_09_15.json` | `5A880678C386` | 1024 | 2026-09-15 13:34:48 | 读数/结果＋成果件面 |
| `results\boss_pc_2_real_transverse_ising_2026_09_15.json` | `8933D61B180A` | 3553 | 2026-09-15 15:27:35 | 读数/结果＋成果件面 |
| `results\boss_pc_3_a3_clipping_2026_09_15.json` | `D74D6B39D1B0` | 1265 | 2026-09-15 13:34:48 | 读数/结果＋成果件面 |
| `results\boss_pc_3_real_reservoir_2026_09_15.json` | `94B5398BE76C` | 2364 | 2026-09-15 15:28:00 | 读数/结果＋成果件面 |
| `results\boss_pe_1_real_2d_ising_2026_09_15.json` | `43D9CE160FC8` | 2460 | 2026-09-15 13:34:49 | 读数/结果＋成果件面 |
| `results\boss_pe_2_real_transverse_ising_2026_09_15.json` | `8933D61B180A` | 3553 | 2026-09-15 13:34:49 | 读数/结果＋成果件面 |
| `results\boss_pe_3_real_reservoir_2026_09_15.json` | `94B5398BE76C` | 2364 | 2026-09-15 13:34:49 | 读数/结果＋成果件面 |
| `results\c5_b_group_fix_readings_2026_10_01.json` | `2A7749DA7C4D` | 9996 | 2026-10-01 09:25:22 | 读数/结果＋成果件面 |
| `results\c5_b_group_fix_readings_2026_10_09.json` | `4E415990B71D` | 10029 | 2026-10-09 13:39:57 | 读数/结果＋成果件面 |
| `results\c5_b_group_root_candidate_2026_10_01.md` | `2FD8946CFE80` | 28867 | 2026-10-01 09:24:13 | 读数/结果＋成果件面 |
| `results\c5_b_group_verdict_2026_10_01.md` | `3FBF6B38A383` | 30118 | 2026-10-01 09:53:17 | 读数/结果＋成果件面 |
| `results\c5_guard_0_1_recheck_verdict_2026_10_01.md` | `24418FA60EDE` | 33287 | 2026-10-01 10:21:29 | 核查＋读数/结果＋成果件面 |
| `results\c5_guard_minmaxstd_readings_2026_10_01.json` | `7FF301514F66` | 19935 | 2026-10-01 10:14:10 | 读数/结果＋成果件面 |
| `results\c5_guard_minmaxstd_report_2026_10_01.md` | `F465FBDB7579` | 19909 | 2026-10-01 10:15:08 | 读数/结果＋报告＋成果件面 |
| `results\c5_protocol_version_annex_2026_10_01.md` | `2593EA7B93CF` | 18558 | 2026-10-01 10:25:17 | 读数/结果＋成果件面 |
| `results\d7_5anchor_60cells_9model_verdict_2026_09_18.json` | `4505CCA79C15` | 2456 | 2026-09-16 11:00:06 | 读数/结果＋成果件面 |
| `results\deposon_3risk_v0_fixes_2026_09_11.json` | `D87C0327A6FB` | 8338 | 2026-09-11 17:16:56 | 读数/结果＋成果件面 |
| `results\deposon_ark_models_2026_09_10.json` | `CCC3EA09A7F5` | 23296 | 2026-09-10 15:14:46 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_3_details.json` | `9FCB6B243E0D` | 656572 | 2026-08-23 00:01:28 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_3_labelfree.json` | `57F06A426BEC` | 3011 | 2026-08-23 00:30:18 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_3_labelshuffle.json` | `5A7555358BE3` | 182322 | 2026-08-23 00:01:28 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_3_resonant.json` | `769AE8C908C9` | 3134 | 2026-08-23 00:30:18 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_3_simple.json` | `9347ADD72401` | 2245 | 2026-08-23 00:01:28 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_3_traps.json` | `82EB64151F2B` | 3112 | 2026-08-23 00:01:28 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_4_gsm8k.json` | `5CD6269D7BAF` | 2741 | 2026-08-23 05:00:55 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_4_gsm8k_details.json` | `39F79FCE7CDB` | 208350 | 2026-08-23 05:00:55 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_4_sc5.json` | `C9796D3B3263` | 12479 | 2026-08-23 15:14:50 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_4_strategyqa.json` | `B51FD24586B3` | 1691 | 2026-08-23 13:04:23 | 读数/结果＋成果件面 |
| `results\deposon_benchmark_v1_4_strategyqa_details.json` | `A63EBEA7B29A` | 235779 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `4E4A17D43ADF` | 13562 | 2026-09-15 13:35:18 | 核查＋读数/结果＋成果件面 |
| `results\deposon_cpath_simulation_2026_09_10.json` | `9466FDBF9C95` | 6351 | 2026-09-10 20:44:37 | 读数/结果＋成果件面 |
| `results\deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | `9F88A212A77C` | 204441 | 2026-09-16 11:01:12 | 核查＋读数/结果＋成果件面 |
| `results\deposon_deepseek_v41_flash_2026_09_10.json` | `4D7BEA150F3A` | 13373 | 2026-09-10 15:47:09 | 读数/结果＋成果件面 |
| `results\deposon_deepseek_v41_flash_30cells_2026_09_10.json` | `84DF447C38DF` | 46432 | 2026-09-10 16:02:21 | 读数/结果＋成果件面 |
| `results\deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json` | `05CDE1CA74EF` | 17549 | 2026-09-10 16:17:05 | 读数/结果＋成果件面 |
| `results\deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` | `56401317E62B` | 18592 | 2026-09-10 16:40:43 | 读数/结果＋成果件面 |
| `results\deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json` | `28BAD561C328` | 6748 | 2026-09-10 16:55:12 | 读数/结果＋成果件面 |
| `results\deposon_dpath_cross_modal_2026_09_10.json` | `AB0C2EAFF0D1` | 75964 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_dpath_cross_modal_runner_2026_09_10.py` | `FB20A6BA5EC6` | 27930 | 2026-09-16 11:01:12 | 读数/结果＋执行体＋成果件面 |
| `results\deposon_embedding_dual_2026_09_10.json` | `33F8AC5D4BFF` | 6834 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_embedding_openrouter_5models_2026_09_10.json` | `0C0D9AFD39AC` | 12785 | 2026-09-10 16:55:37 | 读数/结果＋成果件面 |
| `results\deposon_feshbach_lindblad_sim_2026_09_10.json` | `AA545C67604D` | 7414 | 2026-09-10 22:09:37 | 读数/结果＋成果件面 |
| `results\deposon_feshbach_rag_30cells_2026_09_10.json` | `508F664FFA44` | 64978 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_feshbach_rag_30cells_2026_09_10.py` | `A072E4184E83` | 14343 | 2026-09-16 11:01:12 | 读数/结果＋执行体＋成果件面 |
| `results\deposon_g1_mindmap_demo.json` | `55428F6BD848` | 3041 | 2026-08-23 05:00:55 | 读数/结果＋成果件面 |
| `results\deposon_g2_boltzmann_pathintegral.json` | `9FD0F3399AB3` | 2204 | 2026-08-23 05:00:55 | 读数/结果＋成果件面 |
| `results\deposon_g2_boltzmann_pathintegral_rewrite.json` | `F36667E5B5B8` | 2782 | 2026-08-23 09:40:33 | 读数/结果＋成果件面 |
| `results\deposon_g3_arrhenius.json` | `A3DE045B5DD7` | 2284 | 2026-08-23 05:00:55 | 读数/结果＋成果件面 |
| `results\deposon_game_theory_eval_2026_09_10.json` | `3FA0FF2C8C08` | 10096 | 2026-09-10 21:53:17 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_astra_smoke_2026_09_10.json` | `4BF92BFDEFDA` | 3500 | 2026-09-10 14:37:29 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_proxy_smoke_2026_09_10.json` | `524B34E319B5` | 5485 | 2026-09-10 15:13:52 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_proxy_step1_2026_09_10.json` | `2E23115D9D4B` | 1245 | 2026-09-10 15:13:16 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_proxy_v2_2026_09_10.json` | `A6812512F8F3` | 5810 | 2026-09-10 15:47:09 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_teamorouter_2026_09_10.json` | `F44636F5F72F` | 3827 | 2026-09-10 16:49:38 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_teamorouter_30cells_2026_09_10.json` | `EA38EE252701` | 18290 | 2026-09-10 17:30:03 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_teamorouter_cn_2026_09_10.json` | `2241567C6EFD` | 4855 | 2026-09-10 17:00:24 | 读数/结果＋成果件面 |
| `results\deposon_gpt6_vpn_smoke_2026_09_10.json` | `3267746E47E9` | 3489 | 2026-09-10 14:53:46 | 读数/结果＋成果件面 |
| `results\deposon_gsm8k_stratified.json` | `8B7574B25336` | 3411 | 2026-08-23 09:40:34 | 读数/结果＋成果件面 |
| `results\deposon_llm_codingplan_30cells_2026_09_10.json` | `24E4DCBAA4EA` | 18634 | 2026-09-10 15:15:24 | 读数/结果＋成果件面 |
| `results\deposon_openrouter_5model_30cells_2026_09_10.json` | `B374F80F3B2D` | 31690 | 2026-09-10 22:47:29 | 读数/结果＋成果件面 |
| `results\deposon_openrouter_5model_rag_30cells_2026_09_10.json` | `2E55C53BE25D` | 111710 | 2026-09-10 23:34:43 | 读数/结果＋成果件面 |
| `results\deposon_openrouter_embedding_5model_2026_09_10.json` | `45F314F3415C` | 9472 | 2026-09-10 22:24:35 | 读数/结果＋成果件面 |
| `results\deposon_overseas_open_smoke_2026_09_10.json` | `2481ADADCBB9` | 6787 | 2026-09-10 14:56:03 | 读数/结果＋成果件面 |
| `results\deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | `B5873AFB9D29` | 18104 | 2026-09-16 18:39:54 | 读数/结果＋成果件面 |
| `results\deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33AD1C01F745` | 20398 | 2026-10-01 09:43:44 | 读数/结果＋成果件面 |
| `results\deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `95F3F0957BE8` | 21176 | 2026-10-09 13:39:49 | 读数/结果＋成果件面 |
| `results\deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | `576EAF8D7431` | 11341 | 2026-09-16 18:39:55 | 读数/结果＋成果件面 |
| `results\deposon_pa_d1_d3_2026_09_15.json` | `E221792715F8` | 15604 | 2026-09-15 11:29:23 | 读数/结果＋成果件面 |
| `results\deposon_pc_d1_d3_2026_09_15.json` | `B2046AF03610` | 20408 | 2026-09-15 11:01:56 | 读数/结果＋成果件面 |
| `results\deposon_pe_d1_d3_2026_09_15.json` | `594D7A8D3DE8` | 17085 | 2026-09-15 10:49:09 | 读数/结果＋成果件面 |
| `results\deposon_pf_d1_2026_09_15.json` | `12791772814E` | 21933 | 2026-09-15 11:30:53 | 读数/结果＋成果件面 |
| `results\deposon_pf_d1_full_9m5c_2026_09_15.json` | `FCB5105DF0B6` | 33829 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_pf_implementation_2026_09_11.json` | `509DCEE3B139` | 27311 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_pg_v01_9m60c_2026_09_15.json` | `AB75889EE738` | 11512 | 2026-09-15 13:35:24 | 读数/结果＋成果件面 |
| `results\deposon_risk1_02940_decision_2026_09_11.json` | `2DC8CA9E36C1` | 4336 | 2026-09-15 10:22:25 | 读数/结果＋成果件面 |
| `results\deposon_risk2_canonical5_decision_2026_09_11.json` | `CF4A882160E1` | 4066 | 2026-09-15 10:22:26 | 读数/结果＋成果件面 |
| `results\deposon_risk3_seff_decision_2026_09_11.json` | `67867E752F47` | 6488 | 2026-09-15 10:22:26 | 读数/结果＋成果件面 |
| `results\deposon_v1_implementation_calculator_2026_09_10.py` | `121F104012F4` | 10751 | 2026-09-10 22:21:56 | 读数/结果＋执行体＋成果件面 |
| `results\deposon_v15_diffusion.json` | `C16D1768D1CA` | 519387 | 2026-08-23 19:21:32 | 读数/结果＋成果件面 |
| `results\deposon_v15_diffusion_maxpath_negativeresult.json` | `00EE97C82DCC` | 416460 | 2026-08-23 19:21:32 | 读数/结果＋成果件面 |
| `results\deposon_v15_diffusion_summary.json` | `5B95D06E66B0` | 6079 | 2026-08-23 19:22:36 | 读数/结果＋成果件面 |
| `results\deposon_v16_llm_prior.json` | `C17B31AE4F3B` | 39974 | 2026-08-23 20:21:38 | 读数/结果＋成果件面 |
| `results\deposon_v16_llm_prior_summary.json` | `A7952D9D78DB` | 5517 | 2026-08-23 20:28:34 | 读数/结果＋成果件面 |
| `results\deposon_v16_paired_stats.json` | `20BC4288E0DE` | 9176 | 2026-08-23 20:59:51 | 读数/结果＋成果件面 |
| `results\deposon_v17_fixed_sampler.json` | `701AD291A714` | 106317 | 2026-08-23 21:38:59 | 读数/结果＋成果件面 |
| `results\deposon_v17_fusion_fix.json` | `AF51DA229652` | 106164 | 2026-08-23 21:31:41 | 读数/结果＋成果件面 |
| `results\deposon_v17_fusion_fix_tieartifact_negativeresult.json` | `556086D9E3BC` | 106125 | 2026-08-23 21:31:36 | 读数/结果＋成果件面 |
| `results\deposon_v17_multigraph.json` | `2836605CA12F` | 16896 | 2026-08-23 21:34:43 | 读数/结果＋成果件面 |
| `results\deposon_v18_api_supplements.json` | `62C1A41E1DB8` | 80624 | 2026-08-23 23:20:04 | 读数/结果＋成果件面 |
| `results\deposon_v19_benchmark_fixes.json` | `910C4333EEAD` | 409104 | 2026-08-24 01:11:01 | 读数/结果＋成果件面 |
| `results\deposon_v19_fullrank.json` | `FBBFD3EF3890` | 42458 | 2026-08-24 01:04:04 | 读数/结果＋成果件面 |
| `results\deposon_v19_meanfield.json` | `108DA40D5D4E` | 44443 | 2026-08-24 01:02:01 | 读数/结果＋成果件面 |
| `results\deposon_v19_quickwins.json` | `1EC7ABA6AFD8` | 7842 | 2026-08-24 01:07:59 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase1_60cells_2026_09_11.json` | `A18BBC703B42` | 85508 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase2_dual_mainline_2026_09_11.json` | `E337B824C4B9` | 3189 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase2_f2_2026_09_11.json` | `8B16B611C4DB` | 4582 | 2026-09-11 11:19:24 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase3_f3_2026_09_11.json` | `0B5DCA765D16` | 2474 | 2026-09-11 11:19:55 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase3_strip_embeddings_2026_09_11.json` | `1DED6731CC27` | 2398383 | 2026-09-11 11:33:43 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase3_strip_reembed_2026_09_11.json` | `8900526D8E3A` | 4160 | 2026-09-11 11:33:43 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase4_f4_2026_09_11.json` | `CF7682348617` | 5212 | 2026-09-11 11:17:21 | 读数/结果＋成果件面 |
| `results\deposon_v2_phase5_f5_2026_09_11.json` | `889FC57B3B72` | 2356 | 2026-09-11 11:16:45 | 读数/结果＋成果件面 |
| `results\deposon_v20_baselines.json` | `6EDB2AEC1660` | 16987 | 2026-08-29 01:17:30 | 读数/结果＋成果件面 |
| `results\deposon_v20_bigquiz_eval.json` | `283DBC8C5B63` | 35718 | 2026-08-28 23:54:14 | 读数/结果＋成果件面 |
| `results\deposon_v20_corpus_eval.json` | `CA71AA6858E1` | 631644 | 2026-08-29 01:21:14 | 读数/结果＋成果件面 |
| `results\deposon_v20_cot_quiz.json` | `94FD018B5CC8` | 7101 | 2026-08-28 21:13:05 | 读数/结果＋成果件面 |
| `results\deposon_v20_crossval.json` | `76479B7A5ED6` | 8404 | 2026-08-28 20:27:06 | 读数/结果＋成果件面 |
| `results\deposon_v20_familyl_ingest.json` | `676EB83EDC27` | 1303 | 2026-08-28 17:38:45 | 读数/结果＋成果件面 |
| `results\deposon_v20_fastcheck.json` | `A1EF105B0269` | 1768 | 2026-08-28 22:08:40 | 核查＋读数/结果＋成果件面 |
| `results\deposon_v20_gt.json` | `497B9C2D6746` | 3803 | 2026-08-28 17:43:00 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt2b.json` | `A2AE7997EE67` | 123331 | 2026-08-29 19:57:39 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt3.json` | `35B676773243` | 7844 | 2026-08-29 15:03:29 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt5.json` | `FCA14C5735DD` | 72647 | 2026-08-29 15:35:11 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt5b.json` | `2907006DBE48` | 56425 | 2026-08-29 15:44:55 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt6.json` | `04B90B638BDC` | 65105 | 2026-08-29 15:45:04 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt7.json` | `896589B673EC` | 17925 | 2026-08-29 17:57:57 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt8.json` | `2B88948DCA19` | 5396 | 2026-08-29 19:34:34 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt8b.json` | `6339EA4E500C` | 2706 | 2026-08-30 10:28:49 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt8b_ingest.json` | `AA077CC1725E` | 986 | 2026-08-30 10:28:44 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt8c.json` | `9B16FA802EF8` | 2864 | 2026-08-30 16:17:46 | 读数/结果＋成果件面 |
| `results\deposon_v20_gt8c_ingest.json` | `4B11B1BD8ADA` | 1018 | 2026-08-30 16:17:42 | 读数/结果＋成果件面 |
| `results\deposon_v20_photonics.json` | `0B7893196D0B` | 6796 | 2026-08-29 01:19:15 | 读数/结果＋成果件面 |
| `results\deposon_v20_quiz_eval.json` | `9194EE703218` | 22623 | 2026-08-28 20:46:44 | 读数/结果＋成果件面 |
| `results\deposon_v20_vector_audit.json` | `B9B65C568842` | 915 | 2026-08-28 21:15:08 | 核查＋读数/结果＋成果件面 |
| `results\deposon_v21_gtformal.json` | `9D9AE5001C57` | 69204 | 2026-08-30 15:44:09 | 读数/结果＋成果件面 |
| `results\deposon_v22_e95ci.json` | `928BCFBDB7C3` | 1496 | 2026-08-30 21:45:29 | 读数/结果＋成果件面 |
| `results\deposon_v22_p1c.json` | `2BED4DE3A57C` | 763 | 2026-08-30 21:59:28 | 读数/结果＋成果件面 |
| `results\deposon_v3_physical_opt_2026_09_11.json` | `27F9BD5CC260` | 17591 | 2026-09-11 12:05:53 | 读数/结果＋成果件面 |
| `results\deposon_v3_physical_opt_60cells_2026_09_11.json` | `C659695AA23C` | 17732 | 2026-09-15 10:19:42 | 读数/结果＋成果件面 |
| `results\deposon_v3_v7_summary_2026_09_11.json` | `063AC8D00542` | 25049 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_v3x_6way_stage2_2026_09_10.json` | `D301BBFED982` | 2741 | 2026-09-10 17:56:17 | 读数/结果＋成果件面 |
| `results\deposon_v3x_6way_stage3_2026_09_10.json` | `D892A9D3D6BA` | 15943 | 2026-09-10 18:15:22 | 读数/结果＋成果件面 |
| `results\deposon_v3x_6way_summary_2026_09_10.json` | `63E0798E5843` | 1506 | 2026-09-10 18:17:10 | 读数/结果＋成果件面 |
| `results\deposon_v41_flash_60cells_v2_2026_09_10.json` | `B1D802A68723` | 38428 | 2026-09-10 17:34:41 | 读数/结果＋成果件面 |
| `results\deposon_v41_flash_rag_baseline_2026_09_10.json` | `6754D2655E0A` | 101484 | 2026-09-10 17:07:49 | 读数/结果＋成果件面 |
| `results\deposon_v42_v2_miss_rate_curve_2026_09_16.json` | `0A8ED127D6DE` | 24435 | 2026-09-16 18:27:36 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_22caption_embedding_2026_09_10.json` | `C4B774C8E34C` | 4559 | 2026-09-10 17:36:46 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_7model_smoke_2026_09_10.json` | `EAE44CC3B7B2` | 5944 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_9model_30cells_2026_09_10.json` | `58AB335CA341` | 4894 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_9model_smoke_2026_09_10.json` | `0E5AE7D7D641` | 5328 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_coding_plan_5cells_2026_09_10.json` | `52AA8901556E` | 6058 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_coding_plan_catalog_2026_09_10.json` | `C0EFB547B9D1` | 2841 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_doubao_embedding_2026_09_10.json` | `E99783D18139` | 3303 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_embedding_30cells_2026_09_10.json` | `12BE52BC02A7` | 24794 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | `4EC04D3D7D8C` | 32995 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_glm_latest_5cells_2026_09_10.json` | `83C35597AF81` | 4895 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_glm_latest_5cells_2026_09_10.py` | `A3CA05AEC6FB` | 8112 | 2026-09-16 11:01:12 | 读数/结果＋执行体＋成果件面 |
| `results\deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json` | `0C3EDE881FB1` | 6466 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | `FBB7677B9CD5` | 23472 | 2026-09-16 18:20:55 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | `218EF1A99F97` | 11703 | 2026-09-16 18:20:55 | 读数/结果＋执行体＋成果件面 |
| `results\deposon_volcengine_seed_code_30cells_2026_09_10.json` | `5149F5CAFCF9` | 23034 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_worker_a_2026_09_10.json` | `506810017D34` | 25464 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_worker_b_2026_09_10.json` | `B1EB668377CE` | 49338 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_worker_b_2026_09_10.py` | `401DFD3C27F3` | 13232 | 2026-09-16 11:01:12 | 读数/结果＋执行体＋成果件面 |
| `results\deposon_volcengine_worker_c_2026_09_10.json` | `F6F172820C97` | 51716 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\deposon_volcengine_worker_c_2026_09_10.py` | `B5EEEF1E9BD7` | 11692 | 2026-09-16 11:01:12 | 读数/结果＋执行体＋成果件面 |
| `results\deposon_volcengine_worker_d_2026_09_10.json` | `FAE79888344B` | 20280 | 2026-09-16 11:01:12 | 读数/结果＋成果件面 |
| `results\Deposon_评估汇总_v1_3_0.json` | `2F02F50C164B` | 2811 | 2026-08-22 21:07:01 | 读数/结果＋成果件面 |
| `results\manifest_large_files.md` | `E0DC7A8E4C75` | 3440 | 2026-08-29 01:26:28 | 读数/结果＋成果件面 |

### §2-3 letters/（97 件 / 2,637,062 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `letters\_c4_theory_scan_reply_claude_code_2026_09_30.md` | `2166B37E5D2A` | 27894 | 2026-09-30 21:51:00 | 核查＋回函＋委托·回函面 |
| `letters\_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | `F4DEFAE83553` | 22064 | 2026-10-11 23:40:53 | 回函＋委托·回函面 |
| `letters\_codex_c4_values_followup_reply_2026_10_10.md` | `97A35F8AE94C` | 4490 | 2026-10-10 16:02:26 | 回函＋委托·回函面 |
| `letters\_codex_c4_values_reply_2026_10_10.md` | `8E4972352291` | 13378 | 2026-10-10 13:49:24 | 回函＋委托·回函面 |
| `letters\_codex_c4_values_unblock_reply_2026_10_10.md` | `A975C7990CD8` | 21486 | 2026-10-10 17:35:08 | 回函＋委托·回函面 |
| `letters\_codex_theory_derivation_reply_2026_09_30.md` | `7558EB1A5E34` | 71002 | 2026-09-30 23:52:12 | 回函＋委托·回函面 |
| `letters\_commission_c4_values_EN_2026_10_10.md` | `A397621085D6` | 56217 | 2026-10-10 13:14:46 | 委托＋委托·回函面 |
| `letters\_commission_c4_values_EN_differences_exits_note_2026_10_10.md` | `B20F25A66267` | 7817 | 2026-10-10 13:15:32 | 委托＋委托·回函面 |
| `letters\_commission_c4_values_followup_EN_2026_10_10.md` | `ABE0652AB00F` | 7583 | 2026-10-10 14:31:49 | 委托＋委托·回函面 |
| `letters\_commission_c4_values_unblock_EN_2026_10_10.md` | `FDE64A863B09` | 10244 | 2026-10-10 17:17:35 | 委托＋委托·回函面 |
| `letters\_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md` | `1C769E28F8F5` | 3139 | 2026-10-10 17:17:46 | 委托＋委托·回函面 |
| `letters\_commission_codex_theory_derivation_EN_2026_09_30.md` | `AF50969BEBE2` | 66754 | 2026-09-30 19:58:54 | 委托＋委托·回函面 |
| `letters\_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` | `8B15F0957E0F` | 82016 | 2026-09-30 21:55:05 | 委托＋委托·回函面 |
| `letters\_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | `758E1EF3DE27` | 53344 | 2026-10-01 21:19:36 | 委托＋论文/脚本文本＋委托·回函面 |
| `letters\_commission_glm_dualtrack_paper_v0.5_2026_10_01.md` | `D1650B14D89C` | 42807 | 2026-10-01 11:48:26 | 委托＋论文/脚本文本＋委托·回函面 |
| `letters\_commission_glm_theory_derivation_2026_09_30.md` | `344F5B9E0B08` | 32472 | 2026-09-30 19:49:06 | 委托＋委托·回函面 |
| `letters\_commission_kimi_upload_2026_10_01_v0.2.md` | `A77F7D509285` | 35421 | 2026-10-01 20:38:35 | 委托＋委托·回函面 |
| `letters\_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | `0CE066E5EB3F` | 22685 | 2026-10-11 22:27:45 | 委托＋委托·回函面 |
| `letters\_commission_trae_direct_fix_2026_10_09_v0.1.md` | `C50822B41539` | 37262 | 2026-10-12 01:16:25 | 委托＋委托·回函面 |
| `letters\_dualtrack_paper_clue_book_v0.5_2026_10_01.md` | `0FD7A26FC339` | 109614 | 2026-10-01 11:50:06 | 登记＋论文/脚本文本＋委托·回函面 |
| `letters\_kimi_v4_t12_review_2026_09_20.md` | `38070FD12F31` | 6644 | 2026-09-20 14:53:18 | 评审＋委托·回函面 |
| `letters\_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md` | `BC14F47D927D` | 14155 | 2026-09-20 21:11:34 | 回函＋委托·回函面 |
| `letters\_kimi_v4_theme_reply_2026_09_20.md` | `3E37352EFB4B` | 7372 | 2026-09-20 17:52:32 | 回函＋委托·回函面 |
| `letters\_letter_to_pi_upload_application_approval_2026_09_26.md` | `76D0B60E6BDC` | 23368 | 2026-09-26 21:29:31 | 委托·回函面 |
| `letters\_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md` | `512C73D45087` | 36945 | 2026-09-26 20:45:07 | 委托·回函面 |
| `letters\_letter_to_pi_upload_application_supplement_2026_09_26.md` | `5346A361801B` | 9151 | 2026-09-26 21:28:18 | 委托·回函面 |
| `letters\_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | `44D9A1972A13` | 68449 | 2026-09-26 21:07:20 | 委托·回函面 |
| `letters\_minimax_feedback_log_bloat_2026_09_29.md` | `79FF4043169A` | 13361 | 2026-09-29 22:56:25 | 委托·回函面 |
| `letters\_trae_direct_fix_reply_trae_code_2026_10_12.md` | `F37EBC80D1DF` | 21379 | 2026-10-12 01:34:03 | 回函＋委托·回函面 |
| `letters\_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | `DDA07AD77910` | 42948 | 2026-09-27 20:43:21 | 委托·回函面 |
| `letters\_v3_recheck_indep_judgment_request_2026_09_27.md` | `2C486C1791D5` | 22702 | 2026-09-27 16:18:21 | 终判/裁定＋核查＋委托＋委托·回函面 |
| `letters\_v4_acceptance_coze_2026_09_20.md` | `B2BF2A073AC8` | 5467 | 2026-09-20 14:58:15 | 委托·回函面 |
| `letters\_v4_acceptance_trae_code_2026_09_20.md` | `3E2F1C84E86D` | 7746 | 2026-09-30 16:14:47 | 委托·回函面 |
| `letters\_v4_acceptance_trae_work_v1.0_2026_09_20.md` | `3CAF4E653A68` | 7176 | 2026-09-20 17:36:19 | 委托·回函面 |
| `letters\_v4_attribution_errata_trae_work_2026_09_20.md` | `E061C5806AF6` | 2816 | 2026-09-20 17:36:48 | 勘误＋委托·回函面 |
| `letters\_v4_commission_inventory_anchor_note_2026_09_29.md` | `849F8EBA5BF0` | 2655 | 2026-09-29 13:25:03 | 委托＋委托·回函面 |
| `letters\_v4_commission_kimi_fullupload_w3_2026_09_30.md` | `84C2F4AA9691` | 16404 | 2026-09-30 19:41:29 | 委托＋委托·回函面 |
| `letters\_v4_commission_paper_final_glm_2026_09_24.md` | `53A425FE1BD2` | 10515 | 2026-09-24 18:55:43 | 委托＋论文/脚本文本＋委托·回函面 |
| `letters\_v4_commission_paper_final_glm_2026_09_24_v2.md` | `F3B3E13A0F1B` | 13749 | 2026-09-24 20:05:57 | 委托＋论文/脚本文本＋委托·回函面 |
| `letters\_v4_commission_paper_final_glm_2026_09_24_v3.md` | `614DF9879696` | 20989 | 2026-09-26 19:19:09 | 委托＋论文/脚本文本＋委托·回函面 |
| `letters\_v4_commission_paper_final_glm_2026_09_24_v4.md` | `D5337702CEC9` | 31531 | 2026-09-26 21:25:21 | 委托＋论文/脚本文本＋委托·回函面 |
| `letters\_v4_commission_upload_channel_authorization_2026_09_26.md` | `5E5479BFC453` | 26937 | 2026-09-26 19:50:59 | 委托＋委托·回函面 |
| `letters\_v4_commission_upload_channel_authorization_reply_kimi_2026_09_26.md` | `F8F4AE2E7B9B` | 11575 | 2026-09-26 20:04:44 | 回函＋委托＋委托·回函面 |
| `letters\_v4_commission_upload_executor_2026_09_24.md` | `ADFA7DD03F76` | 13012 | 2026-09-24 18:56:08 | 委托＋委托·回函面 |
| `letters\_v4_commission_upload_executor_2026_09_24_v2.md` | `FF2154CE182D` | 16894 | 2026-09-24 20:05:57 | 委托＋委托·回函面 |
| `letters\_v4_commission_upload_executor_2026_09_24_v3.md` | `C20D4F58F5C8` | 25091 | 2026-09-26 19:20:04 | 委托＋委托·回函面 |
| `letters\_v4_commission_upload_executor_reply_v3_2026_09_24.md` | `50592E36ECAD` | 9848 | 2026-09-26 19:35:40 | 回函＋委托＋委托·回函面 |
| `letters\_v4_commission_upload_executor_reply_v3_exec_2026_09_26.md` | `631BB517F79D` | 4471 | 2026-09-26 19:53:10 | 回函＋委托＋委托·回函面 |
| `letters\_v4_commission_〔IM〕_report_coze_2026_09_24.md` | `15F8227308BC` | 7197 | 2026-09-24 18:55:26 | 委托＋报告＋委托·回函面 |
| `letters\_v4_commission_〔IM〕_report_coze_2026_09_24_v2.md` | `389C51E70D19` | 10599 | 2026-09-24 20:05:56 | 委托＋报告＋委托·回函面 |
| `letters\_v4_commission_〔IM〕_report_coze_2026_09_24_v3.md` | `E5B63D181B15` | 13898 | 2026-09-26 19:19:29 | 委托＋报告＋委托·回函面 |
| `letters\_v4_commission_〔IM〕_report_coze_2026_09_24_v4.md` | `802C705E1469` | 21433 | 2026-09-26 21:25:16 | 委托＋报告＋委托·回函面 |
| `letters\_v4_commission_〔IM〕_report_coze_reply_v4_2026_09_24.md` | `C60DFD7C0F45` | 16471 | 2026-09-26 22:20:19 | 回函＋委托＋报告＋委托·回函面 |
| `letters\_v4_d1_response_workbuddy_2026_09_20.md` | `BC663B671994` | 14881 | 2026-09-20 14:36:48 | 委托·回函面 |
| `letters\_v4_d1_review_codex_2026_09_20.md` | `48387412B109` | 4506 | 2026-09-21 11:12:20 | 评审＋委托·回函面 |
| `letters\_v4_distillation_acceptance_coze_2026_09_20.md` | `3A8CB7B9D041` | 14295 | 2026-09-20 18:03:55 | 委托·回函面 |
| `letters\_v4_distillation_acceptance_kimi_2026_09_20.md` | `A4D194DBF9AD` | 6454 | 2026-09-20 17:56:29 | 委托·回函面 |
| `letters\_v4_distillation_acceptance_trae_code_2026_09_20.md` | `DC47FBF3C491` | 5218 | 2026-09-20 17:32:33 | 委托·回函面 |
| `letters\_v4_distillation_brainstorm_reply_codex_2026_09_21.md` | `0FF6C042B845` | 9048 | 2026-09-21 11:12:20 | 回函＋委托·回函面 |
| `letters\_v4_distillation_invitation_2026_09_20_v1.0.md` | `E4B00FA97D03` | 54784 | 2026-09-30 16:14:47 | 委托＋委托·回函面 |
| `letters\_v4_distillation_reply_claude_code_2026_09_20.md` | `D39CB17B051B` | 64212 | 2026-09-21 11:01:14 | 回函＋委托·回函面 |
| `letters\_v4_distillation_reply_coze_2026_09_20.md` | `00593014CBD3` | 71084 | 2026-09-20 21:53:15 | 回函＋委托·回函面 |
| `letters\_v4_distillation_reply_trae_code_2026_09_20.md` | `E87EC8F7E2FE` | 43570 | 2026-09-20 21:21:36 | 回函＋委托·回函面 |
| `letters\_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | `9BB22099DB3B` | 28207 | 2026-09-23 13:35:13 | 回函＋评审＋委托·回函面 |
| `letters\_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md` | `59B8DF6E2E22` | 6067 | 2026-09-23 13:46:15 | 回函＋评审＋委托·回函面 |
| `letters\_v4_distillation_theme_reply_workbuddy_2026_09_20.md` | `E3FE63A2F708` | 18785 | 2026-09-20 18:19:48 | 回函＋委托·回函面 |
| `letters\_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md` | `CDB27CD3008C` | 13553 | 2026-09-21 09:42:45 | 回函＋委托·回函面 |
| `letters\_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` | `BFB4932F4467` | 12963 | 2026-09-20 18:26:36 | 回函＋委托·回函面 |
| `letters\_v4_experiment_invitation_2026_09_20.md` | `20F8242DE6CA` | 32164 | 2026-09-30 16:14:47 | 委托＋委托·回函面 |
| `letters\_v4_experiment_invitation_2026_09_20_v0.2.md` | `72FC2E7FB098` | 43024 | 2026-09-30 16:14:47 | 委托＋委托·回函面 |
| `letters\_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | `F88E429717AA` | 13263 | 2026-09-30 16:14:47 | 评审＋委托·回函面 |
| `letters\_v4_ide_track_review_trae_work_2026_09_20.md` | `21D384CF3422` | 7488 | 2026-09-20 17:35:40 | 评审＋委托·回函面 |
| `letters\_v4_review_claude_code_2026_09_20.md` | `B6F9956BCF5C` | 7004 | 2026-09-20 14:32:01 | 评审＋委托·回函面 |
| `letters\_v4_theme_reply_mavis_2026_09_20.md` | `5D932D7085CD` | 37980 | 2026-09-30 16:14:47 | 回函＋委托·回函面 |
| `letters\_v4_theme_reply_mavis_2026_09_20_v1.1.md` | `5C61F61F1F7E` | 38085 | 2026-09-30 16:14:47 | 回函＋委托·回函面 |
| `letters\_v4_theme_reply_mavis_2026_09_20_v1.2.md` | `F1D73C82511D` | 38087 | 2026-09-30 16:14:47 | 回函＋委托·回函面 |
| `letters\_v4_theme_reply_trae_work_2026_09_20.md` | `EBA83C88B629` | 11458 | 2026-09-20 17:35:40 | 回函＋委托·回函面 |
| `letters\_v4_theme_reply_trae_work_2026_09_20_v1.1.md` | `BE850D129F35` | 13404 | 2026-09-20 17:39:33 | 回函＋委托·回函面 |
| `letters\_v4_theme_reply_trae_work_2026_09_20_v1.2.md` | `6BEE6EC434BD` | 28395 | 2026-09-20 20:58:07 | 回函＋委托·回函面 |
| `letters\_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | `F86B8B6C8ED2` | 60139 | 2026-09-27 20:13:23 | 回函＋委托·回函面 |
| `letters\_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` | `9A98ABF3119A` | 20610 | 2026-09-27 20:28:20 | 回函＋委托·回函面 |
| `letters\_v5_rj5_external_rederive_request_2026_09_28.md` | `CFD58AE66463` | 31381 | 2026-09-28 18:22:06 | 委托＋委托·回函面 |
| `letters\_v5_rj5_external_rederive_request_EN_2026_09_28.md` | `498215A9EC7D` | 51013 | 2026-09-28 18:47:14 | 委托＋委托·回函面 |
| `letters\_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md` | `5BFC26BBAA41` | 15606 | 2026-09-30 19:07:36 | 核查＋回函＋委托·回函面 |
| `letters\LETTER_FROM_TRAE_2026_09_11.md` | `1D3A9E52ABE3` | 13617 | 2026-09-11 16:30:23 | 委托·回函面 |
| `letters\LETTER_FROM_TRAE_3RISK_2026_09_11.md` | `A1AFBF3E1296` | 5145 | 2026-09-15 10:25:49 | 委托·回函面 |
| `letters\LETTER_FROM_TRAE_REVIEW_2026_09_16.md` | `6145162379C9` | 7718 | 2026-09-15 15:19:16 | 评审＋委托·回函面 |
| `letters\LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md` | `141E05BF56EA` | 3571 | 2026-09-15 15:39:01 | 核查＋委托·回函面 |
| `letters\TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md` | `53A90B9EFBB9` | 5154 | 2026-09-17 19:16:03 | 委托·回函面 |
| `letters\TRAE_FIX_REQUEST_3RISKS_2026_09_11.md` | `62C4AF080EA3` | 15990 | 2026-09-11 17:27:09 | 委托＋委托·回函面 |
| `letters\TRAE_V3_CODE_IMPROVEMENT_LETTER_2026_09_16.md` | `9AA717B2E1AC` | 7376 | 2026-09-16 20:58:07 | 委托·回函面 |
| `letters\TRAE_V3_REVIEW_LETTER_2026_09_23.md` | `0E7600AC4478` | 7510 | 2026-09-23 13:08:23 | 评审＋委托·回函面 |
| `letters\TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md` | `6AC3CB09567B` | 105136 | 2026-09-27 19:20:37 | 委托＋委托·回函面 |
| `letters\TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` | `E17412088546` | 101560 | 2026-09-30 18:05:24 | 核查＋委托＋委托·回函面 |
| `letters\verify_c4_originated_math.py` | `3042CF59448E` | 4115 | 2026-10-10 17:30:17 | 核查＋执行体＋委托·回函面 |
| `letters\查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | `8BAA9854B3F7` | 239700 | 2026-10-10 21:21:41 | 委托·回函面 |
| `letters\查理_glm_dualtrack_paper_sole_letter_2026_10_01.md` | `3C5059319FFE` | 13105 | 2026-10-02 00:19:43 | 论文/脚本文本＋委托·回函面 |

### §2-4 docs/（135 件 / 2,383,514 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `docs\ADVISOR_BRIEFING_2026-08-30.md` | `40278BC425E6` | 5890 | 2026-08-29 10:16:17 | 文档面 |
| `docs\ARCH_AUDIT_v2.md` | `5BEE4C6CF47C` | 14698 | 2026-08-30 04:39:28 | 核查＋文档面 |
| `docs\BASELINE_REGISTRY.md` | `51B271548835` | 3356 | 2026-08-28 20:59:38 | 登记＋文档面 |
| `docs\CLOSURE_v19_and_v2X_gametheory.md` | `84323775A212` | 9065 | 2026-08-28 15:55:51 | 文档面 |
| `docs\DATASET_HEALTH_v2.md` | `C87A0C1F5AF6` | 4892 | 2026-08-30 04:40:23 | 文档面 |
| `docs\Deposon_Requirements_v1.md` | `EE33F3F22E1B` | 13914 | 2026-08-22 21:07:01 | 文档面 |
| `docs\Deposon_v1_3_验证报告.md` | `DC5BE727F920` | 8003 | 2026-08-22 21:07:01 | 文档面 |
| `docs\Deposon_v1_4_验证报告.md` | `3BCCCF03F7CA` | 4254 | 2026-08-22 21:11:43 | 文档面 |
| `docs\FIGURES_v2.md` | `1CD4A4CB0A76` | 5851 | 2026-08-30 11:15:47 | 文档面 |
| `docs\Findings_GT_FORMAL.md` | `FAB607F0E180` | 6345 | 2026-08-30 15:45:12 | 文档面 |
| `docs\Findings_GT2B.md` | `E6CC74F9917D` | 3322 | 2026-08-29 20:00:21 | 文档面 |
| `docs\Findings_GT3.md` | `4F3242B2A661` | 2632 | 2026-08-29 15:06:30 | 文档面 |
| `docs\Findings_GT8.md` | `869C0071FBC2` | 3890 | 2026-08-29 19:36:27 | 文档面 |
| `docs\Findings_GT8B.md` | `956183753A2E` | 9809 | 2026-08-30 10:38:41 | 文档面 |
| `docs\Findings_v2.0.md` | `7E5DC4B045D8` | 4364 | 2026-08-28 17:44:22 | 文档面 |
| `docs\Findings_v2.0_bigquiz.md` | `D4ED18152DC0` | 3291 | 2026-08-28 23:55:23 | 文档面 |
| `docs\Findings_v2.0_boss.md` | `36C714EABE3B` | 3642 | 2026-08-28 21:16:05 | 文档面 |
| `docs\Findings_v2.0_corrections.md` | `5864BBE5ADAE` | 5012 | 2026-08-29 01:23:08 | 勘误＋文档面 |
| `docs\Findings_v2.0_crossval.md` | `32D26CB09568` | 4566 | 2026-08-28 20:28:59 | 文档面 |
| `docs\Findings_v2.0_hardening.md` | `A7F479793F01` | 3563 | 2026-08-28 22:49:38 | 文档面 |
| `docs\Findings_v2.0_photonics.md` | `9158F54EC248` | 4377 | 2026-08-30 04:46:02 | 文档面 |
| `docs\Findings_v2.0_skills.md` | `43731392B581` | 3456 | 2026-08-28 20:47:31 | 判死线/准入门＋文档面 |
| `docs\GT_FORMALIZATION_v1.md` | `AEEFB8EF6972` | 19100 | 2026-08-30 15:45:39 | 文档面 |
| `docs\GT_RECONSTRUCTION.md` | `CFF15D000D47` | 13424 | 2026-09-28 22:57:17 | 文档面 |
| `docs\LESSONS_INDEX.md` | `7E3674A80CB7` | 4682 | 2026-08-29 10:11:09 | 文档面 |
| `docs\LESSONS_v19.md` | `DBBCF8E5E89D` | 5290 | 2026-08-28 17:56:50 | 文档面 |
| `docs\LESSONS_v20_deepprobe.md` | `5C898D4407EE` | 8409 | 2026-08-29 10:06:48 | 核查＋文档面 |
| `docs\MODEL_ARGUMENTATION_v2.md` | `2C83C42804E4` | 30142 | 2026-08-30 10:42:40 | 文档面 |
| `docs\PAPER_BRIEF.md` | `DE450C0BEFFA` | 11296 | 2026-08-30 11:09:37 | 论文/脚本文本＋文档面 |
| `docs\PROGRESS_REPORT_LAYMAN.md` | `25546FFDC56B` | 8472 | 2026-08-29 15:08:52 | 报告＋文档面 |
| `docs\REF_VERIFICATION_v2.md` | `64F0A3772C12` | 5860 | 2026-08-30 11:17:21 | 核查＋文档面 |
| `docs\REFACTOR_v2.md` | `03C8BAA18D93` | 23042 | 2026-08-30 10:39:00 | 文档面 |
| `docs\reviews\review_gtformal_integration_v2X.md` | `325C9D87787B` | 8582 | 2026-08-30 16:58:11 | 评审＋文档面 |
| `docs\reviews\review_salvage_integration_v2X.md` | `96AE50306F36` | 6212 | 2026-08-30 05:06:19 | 评审＋文档面 |
| `docs\reviews\review_sprint_v2X.md` | `4356CD02562E` | 7776 | 2026-08-30 11:11:11 | 评审＋文档面 |
| `docs\Roadmap_v2X.md` | `A6AAF3200611` | 6467 | 2026-08-24 11:13:19 | 文档面 |
| `docs\SALVAGE_v2.md` | `F28A81D6302D` | 7312 | 2026-08-30 04:41:52 | 文档面 |
| `docs\SECURITY_AUDIT_v2.md` | `317FB508940A` | 4707 | 2026-08-30 04:39:49 | 核查＋文档面 |
| `docs\simple_baseline_failure_analysis.md` | `968776002868` | 6080 | 2026-08-23 00:01:28 | 文档面 |
| `docs\space_release_log.json` | `110607514753` | 5056 | 2026-08-28 23:54:50 | 文档面 |
| `docs\SPEC_GT2B.md` | `68A5B08EF007` | 3318 | 2026-08-29 19:56:29 | 文档面 |
| `docs\SPEC_GT2C.md` | `29AF533486B2` | 3172 | 2026-08-30 18:32:55 | 文档面 |
| `docs\SPEC_GT3.md` | `432EC337D586` | 5369 | 2026-08-29 14:09:52 | 文档面 |
| `docs\SPEC_GT5C.md` | `1E41B4334735` | 3046 | 2026-08-30 18:33:30 | 文档面 |
| `docs\SPEC_GT8.md` | `EDF6F4465EAD` | 4181 | 2026-08-29 19:40:49 | 文档面 |
| `docs\SPEC_GT8B.md` | `3545C01E1291` | 7486 | 2026-08-30 10:37:50 | 文档面 |
| `docs\SPEC_GT8C.md` | `6B09DE9911C0` | 6326 | 2026-08-30 15:50:15 | 文档面 |
| `docs\SPEC_v1.5.md` | `C165A86CF551` | 6204 | 2026-08-23 19:22:13 | 文档面 |
| `docs\SPEC_v1.8.md` | `AD0E445714D9` | 9850 | 2026-08-23 23:19:47 | 文档面 |
| `docs\SPEC_v2.0.md` | `BAC61D51FD20` | 5333 | 2026-08-28 16:54:47 | 文档面 |
| `docs\SPEC_v2.0_amendment1.md` | `3E3A5014CB0E` | 4743 | 2026-08-29 01:22:16 | 文档面 |
| `docs\SYNTHESIS_mind_game.md` | `0F36AAEEDA6F` | 9191 | 2026-08-29 00:22:08 | 论文/脚本文本＋文档面 |
| `docs\THINKING_V3_GT_CONTRIB_2026.md` | `8C1D733F9182` | 19508 | 2026-08-30 20:45:01 | 文档面 |
| `docs\V3X\AGENT_TEAM_OPT_V2_2026_09_11.md` | `BBD074B76526` | 11835 | 2026-09-11 16:30:03 | 文档面 |
| `docs\V3X\BOSS_B123_BUGFIX_2026_09_09.md` | `9352A1675B10` | 5615 | 2026-09-09 14:50:57 | 文档面 |
| `docs\V3X\BOSS_F_GHOST_PATH_NOTE_2026_09_11.md` | `354A1360234F` | 4840 | 2026-09-11 13:16:07 | 文档面 |
| `docs\V3X\BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `C28F7F0B530F` | 11079 | 2026-09-15 13:36:08 | 核查＋报告＋文档面 |
| `docs\V3X\BOSS_SELFTEST_PHASE_B_2026_09_09.md` | `4485443757E7` | 15478 | 2026-09-09 14:18:07 | 文档面 |
| `docs\V3X\BOSS_URL_2026_09_11.md` | `1BA7419178A1` | 7135 | 2026-09-11 13:01:49 | 文档面 |
| `docs\V3X\BOSS_URL_DUE_DILIGENCE_2026_09_11.md` | `0FB588BB0C2E` | 10970 | 2026-09-11 12:11:02 | 文档面 |
| `docs\V3X\BPA_PILOT_2026_09_09_mavis.md` | `D74E1534493E` | 6864 | 2026-09-09 13:39:22 | 文档面 |
| `docs\V3X\CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md` | `B049140E130C` | 6804 | 2026-09-11 13:30:46 | 核查＋文档面 |
| `docs\V3X\CPATH_SIMULATION_REPORT_2026_09_10.md` | `DE772CD9E7BA` | 6825 | 2026-09-10 20:47:18 | 报告＋文档面 |
| `docs\V3X\D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `0A63824F0805` | 7352 | 2026-09-15 14:07:47 | 核查＋报告＋文档面 |
| `docs\V3X\D0_FREEZE_PREP_2026_09_09.md` | `0D1E88C258AA` | 9844 | 2026-09-09 10:55:24 | 文档面 |
| `docs\V3X\D3_〔IM〕_MIDTERM_TEMPLATE.md` | `574D5A79E363` | 4361 | 2026-09-09 11:23:41 | 文档面 |
| `docs\V3X\D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `8FF1A7C5413F` | 21756 | 2026-09-15 15:15:39 | 报告＋文档面 |
| `docs\V3X\D7_GITHUB_PUSH_RECEIVE_2026_09_15_v2.md` | `2C4BB6078EE7` | 5930 | 2026-09-15 17:28:16 | 文档面 |
| `docs\V3X\D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md` | `67063F9CB238` | 6459 | 2026-09-11 13:30:46 | 文档面 |
| `docs\V3X\D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | `87563A63B854` | 5830 | 2026-09-09 11:00:34 | 文档面 |
| `docs\V3X\D7_POST_CLEANUP_PLAN_2026_09_18.json` | `0B8A1A357AAE` | 20271 | 2026-09-15 17:27:45 | 文档面 |
| `docs\V3X\D7_POST_CLEANUP_REPORT_2026_09_16.json` | `40955BF2ABC5` | 1248 | 2026-09-16 11:01:13 | 报告＋文档面 |
| `docs\V3X\D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md` | `51869E3184F4` | 10692 | 2026-09-16 11:09:18 | 文档面 |
| `docs\V3X\D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | `935CB6EE3566` | 8037 | 2026-09-16 11:08:22 | 文档面 |
| `docs\V3X\DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md` | `AC8997B07731` | 22442 | 2026-09-10 20:22:54 | 文档面 |
| `docs\V3X\DEPOSON_EMBEDDING_6WAY_VERIFICATION_2026_09_10.md` | `240A7AE4BDFB` | 17803 | 2026-09-10 18:16:43 | 核查＋文档面 |
| `docs\V3X\DPATH_CROSS_MODAL_2026_09_10.md` | `E4EE3999F7CE` | 26460 | 2026-09-16 11:01:12 | 文档面 |
| `docs\V3X\KT_A1_SPEC_V0.1.md` | `78B71D404366` | 29570 | 2026-09-09 13:42:23 | 文档面 |
| `docs\V3X\KT_B1_REWORK_REPORT_2026_09_10.md` | `BAEF94E393DE` | 11478 | 2026-09-10 12:05:42 | 报告＋文档面 |
| `docs\V3X\KT_B1_SPEC_V0.1.md` | `0397B757362F` | 39206 | 2026-09-30 20:36:32 | 文档面 |
| `docs\V3X\KT_C1_REPORT_PHASE_B_2026_09_09.md` | `825337B10A2D` | 8753 | 2026-09-09 14:17:30 | 报告＋文档面 |
| `docs\V3X\KT_C1_SPEC_V0.1.md` | `59D8F56347D5` | 31241 | 2026-09-09 13:42:23 | 文档面 |
| `docs\V3X\KT_D0_EVIDENCE_CARD.md` | `75B2F3B38C2A` | 6354 | 2026-09-09 10:59:38 | 文档面 |
| `docs\V3X\KT_D0_SPEC_V0.1.md` | `CCE8E9A1B00E` | 20927 | 2026-09-09 13:42:24 | 文档面 |
| `docs\V3X\P_A_D1_D3_REPORT_2026_09_15.md` | `977FE1B48F75` | 19751 | 2026-09-15 11:31:34 | 报告＋文档面 |
| `docs\V3X\P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `BD1CAAB42B4C` | 10351 | 2026-09-09 10:05:24 | 文档面 |
| `docs\V3X\P_B_DISTORTION_BOUND_V0_SPEC.md` | `423C84DE20D5` | 15457 | 2026-09-30 20:36:51 | 文档面 |
| `docs\V3X\P_C_D1_D3_REPORT_2026_09_15.md` | `79C7321056B8` | 13419 | 2026-09-15 15:08:22 | 报告＋文档面 |
| `docs\V3X\P_C_P_E_V0_1_VERIFICATION_2026_09_12.md` | `EE043A13F801` | 3899 | 2026-09-11 13:01:11 | 核查＋文档面 |
| `docs\V3X\P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `D427B2F57C33` | 6301 | 2026-09-08 16:03:54 | 文档面 |
| `docs\V3X\P_C_V0_1_VERIFICATION_2026_09_12.md` | `00C7B7CECCDC` | 4885 | 2026-09-11 13:00:18 | 核查＋文档面 |
| `docs\V3X\P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` | `7F1492FBE657` | 10979 | 2026-09-16 18:26:46 | 核查＋文档面 |
| `docs\V3X\P_D_FINGERPRINT_V0_3_SPEC.md` | `F119F2F30287` | 34393 | 2026-09-17 15:15:44 | 文档面 |
| `docs\V3X\P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md` | `FC73CAB85D8F` | 15021 | 2026-09-17 15:16:40 | 文档面 |
| `docs\V3X\P_D_FINGERPRINT_V0_4_SPEC.md` | `C13449101AB3` | 34367 | 2026-10-01 09:51:11 | 文档面 |
| `docs\V3X\P_D_FINGERPRINT_V0_SPEC.md` | `3B67461B05FE` | 9192 | 2026-09-04 13:11:41 | 文档面 |
| `docs\V3X\P_E_D1_D3_REPORT_2026_09_15.md` | `900DA300D11E` | 13109 | 2026-09-15 11:27:04 | 报告＋文档面 |
| `docs\V3X\P_E_DOUBAN_EMBEDDING_V0_SPEC.md` | `6F3C550CEC13` | 16876 | 2026-09-08 21:56:01 | 文档面 |
| `docs\V3X\P_F_D1_FULL_REPORT_2026_09_15.md` | `817EFDC2F0AD` | 15985 | 2026-09-15 12:15:12 | 报告＋文档面 |
| `docs\V3X\P_F_D1_REPORT_2026_09_15.md` | `E47D0348922E` | 12608 | 2026-09-16 11:01:12 | 报告＋文档面 |
| `docs\V3X\P_F_IMPLEMENTATION_2026_09_11.md` | `EDD048EAA721` | 22973 | 2026-09-16 11:01:12 | 文档面 |
| `docs\V3X\P_F_RESEARCH_2026_09_09.md` | `98085DF7811A` | 17603 | 2026-09-09 13:49:14 | 文档面 |
| `docs\V3X\P_F_SPEC_V0.md` | `DE90FAF362C5` | 19804 | 2026-09-09 13:50:05 | 文档面 |
| `docs\V3X\P_F_V0_1_UPGRADE_2026_09_11.md` | `B10FAE0DA66D` | 6375 | 2026-09-11 12:15:55 | 文档面 |
| `docs\V3X\P_F_V0_1_VERIFICATION_2026_09_12.md` | `4D970E9C0AEC` | 4188 | 2026-09-11 13:09:27 | 核查＋文档面 |
| `docs\V3X\P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | `2F0765A1D39D` | 12501 | 2026-09-15 11:33:11 | 文档面 |
| `docs\V3X\P_G_V01_REPORT_2026_09_15.md` | `9A6B08D03E0C` | 15479 | 2026-09-15 12:06:17 | 报告＋文档面 |
| `docs\V3X\PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | `C165CD33A362` | 4587 | 2026-09-11 11:17:21 | 文档面 |
| `docs\V3X\PHASE_B_DELIVERY_2026_09_09.md` | `BA53D73E3937` | 9701 | 2026-09-09 14:19:28 | 文档面 |
| `docs\V3X\QUICK_KILL_6_DIRECTIONS.md` | `A476F241EDB2` | 15085 | 2026-09-09 09:53:43 | 判死线/准入门＋文档面 |
| `docs\V3X\REVIEWER_A_STATIC_AUDIT_2026_09_15.md` | `575572872E9A` | 34647 | 2026-09-15 14:22:04 | 核查＋评审＋文档面 |
| `docs\V3X\REVIEWER_A_TRAE_FIX_AUDIT_2026_09_15.md` | `195373C094D6` | 20698 | 2026-09-15 15:29:00 | 核查＋评审＋文档面 |
| `docs\V3X\REVIEWER_A_TRAE_N123_AUDIT_2026_09_15.md` | `33EE7266CF5B` | 17151 | 2026-09-15 15:59:57 | 核查＋评审＋文档面 |
| `docs\V3X\REVIEWER_B_AUDIT_PHASE_B_2026_09_09.md` | `5E99E79F2E11` | 14835 | 2026-09-09 14:17:07 | 核查＋评审＋文档面 |
| `docs\V3X\REVIEWER_B_TRAE_FIX_RERUN_2026_09_15.md` | `F5AC9820310A` | 16278 | 2026-09-15 15:28:54 | 评审＋文档面 |
| `docs\V3X\REVIEWER_B_TRAE_N123_RERUN_2026_09_15.md` | `31C27C0117A6` | 16926 | 2026-09-15 15:57:55 | 评审＋文档面 |
| `docs\V3X\RISK3_V0_FIXES_2026_09_11.md` | `C00D1C22E7ED` | 13271 | 2026-09-11 17:17:36 | 文档面 |
| `docs\V3X\SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md` | `00E543564E3F` | 10708 | 2026-09-09 14:18:34 | 文档面 |
| `docs\V3X\TRAE_3RISK_FIX_REPORT_2026_09_16.md` | `7478959CFC7D` | 9267 | 2026-09-15 15:10:00 | 报告＋文档面 |
| `docs\V3X\TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | `4020B1809780` | 8849 | 2026-09-17 11:12:54 | 文档面 |
| `docs\V3X\TRAE_PROACTIVE_AUDIT_REPORT_2026_09_16.md` | `813B34DCAC70` | 6493 | 2026-09-15 15:18:50 | 核查＋报告＋文档面 |
| `docs\V3X\TRAE_SELFCHECK_FIX_REPORT_2026_09_15.md` | `226F740AA120` | 4840 | 2026-09-15 15:39:00 | 核查＋报告＋文档面 |
| `docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | `41F5F1689D09` | 857551 | 2026-09-29 19:42:49 | 勘误＋文档面 |
| `docs\V3X\V3X_1WEEK_KILL_REPORT_2026_09_18.md` | `4FFB21BB6BFA` | 8526 | 2026-09-16 11:03:10 | 判死线/准入门＋报告＋文档面 |
| `docs\V3X\V3X_D6_PAPER_V2_2026_09_09_mavis.md` | `4D06D34CB6FA` | 24778 | 2026-09-09 13:41:07 | 论文/脚本文本＋文档面 |
| `docs\V3X\V3X_D6_PAPER_zh.md` | `FEAE8AF2FEFE` | 19716 | 2026-09-09 11:34:06 | 论文/脚本文本＋文档面 |
| `docs\V3X\V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | `4A08521F8DE1` | 38545 | 2026-09-16 11:01:12 | 报告＋文档面 |
| `docs\V3X\V3X_DAILY_KILL_V2_PLAN.md` | `37E97E1E7B7F` | 15327 | 2026-09-09 11:39:34 | 判死线/准入门＋文档面 |
| `docs\V3X\V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` | `3D847F9F3151` | 22427 | 2026-09-16 12:28:47 | 文档面 |
| `docs\V3X\V3X_PROJECT_EVOLUTION_FOR_KIMI.md` | `4DE2CBF57A49` | 12908 | 2026-09-15 14:55:11 | 文档面 |
| `docs\V3X\V42_V2_REMEDIATION_CLAUSE_2026_09_16.md` | `E451A5A3D079` | 4775 | 2026-09-16 18:33:04 | 文档面 |
| `docs\V3X\V42_V2_VERIFIER_PERFORMANCE_REPORT_2026_09_16.md` | `914053FC3E17` | 11080 | 2026-09-16 18:33:19 | 核查＋报告＋文档面 |
| `docs\V3X\V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | `F80CC4E1FB7F` | 7344 | 2026-09-11 13:15:52 | 文档面 |
| `docs\V3X_COLLAB_DIRECTIONS.md` | `5A27C2350036` | 16363 | 2026-08-31 09:32:54 | 文档面 |
| `docs\variant_params_table.md` | `25F90F106451` | 4035 | 2026-08-23 00:01:28 | 文档面 |

### §2-5 verifier/（116 件 / 265,425 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `verifier\_build_partial.py` | `04FCD95C70F1` | 7160 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\_read_summary.py` | `B4D89F052875` | 1231 | 2026-09-10 20:50:17 | 核查＋执行体＋验证面 |
| `verifier\_run.log` | `E148D7BF11E1` | 7190 | 2026-09-10 21:03:13 | 核查＋验证面 |
| `verifier\_test_one.py` | `893641FD9E25` | 2564 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\_worker_a_run.log` | `9DF22377DC55` | 4532 | 2026-09-10 21:29:39 | 核查＋验证面 |
| `verifier\audit\conservation.py` | `4BDEC2683F06` | 22105 | 2026-09-10 09:29:22 | 核查＋执行体＋验证面 |
| `verifier\handoff\KT_ABC1_anchors_sha256_12.json` | `03C6C01F3697` | 6680 | 2026-09-09 13:19:32 | 核查＋验证面 |
| `verifier\handoff\KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | `6E9CD8CD8E07` | 11318 | 2026-09-22 11:02:01 | 核查＋验证面 |
| `verifier\handoff\KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `DA517C115F3C` | 5049 | 2026-09-15 13:31:24 | 核查＋验证面 |
| `verifier\handoff\P_F_PREDECISION_2026_09_09.json` | `B41C98BF90CC` | 3680 | 2026-09-09 13:50:15 | 核查＋验证面 |
| `verifier\handoff\P_F_PREDECISION_2026_09_11_V0.1.json` | `312D635E6259` | 12498 | 2026-09-11 13:08:54 | 核查＋验证面 |
| `verifier\kill_lines\kt_b1_kill_decision.py` | `9F351078E5BF` | 2781 | 2026-09-09 13:17:24 | 判死线/准入门＋核查＋执行体＋验证面 |
| `verifier\README.md` | `D76F2DC473BE` | 14360 | 2026-08-30 17:08:56 | 核查＋验证面 |
| `verifier\run_volcengine_9model_30cells.py` | `54F8033CFB29` | 12050 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\runs\20260823.log` | `F8D8DB6A4D8B` | 1197 | 2026-08-23 20:24:15 | 核查＋验证面 |
| `verifier\runs\20260823T022721Z.log` | `CF205DBB8CEA` | 7 | 2026-08-23 10:27:21 | 核查＋验证面 |
| `verifier\runs\20260823T130229Z.log` | `1AF06784D975` | 839 | 2026-08-23 21:02:31 | 核查＋验证面 |
| `verifier\runs\20260823T130254Z.log` | `8316E03518F2` | 839 | 2026-08-23 21:02:55 | 核查＋验证面 |
| `verifier\runs\20260823T130326Z.log` | `E8698E422D69` | 819 | 2026-08-23 21:03:27 | 核查＋验证面 |
| `verifier\runs\20260823T130405Z.log` | `D6071FF9493E` | 576 | 2026-08-23 21:04:08 | 核查＋验证面 |
| `verifier\runs\20260823T131053Z.log` | `94E578649599` | 911 | 2026-08-23 21:10:55 | 核查＋验证面 |
| `verifier\runs\20260823T134128Z.log` | `6CF95AADE825` | 910 | 2026-08-23 21:41:34 | 核查＋验证面 |
| `verifier\runs\20260823T134305Z.log` | `C9AE2079FC1F` | 972 | 2026-08-23 21:43:08 | 核查＋验证面 |
| `verifier\runs\20260823T154658Z.log` | `1FCA45290883` | 1536 | 2026-08-23 23:47:08 | 核查＋验证面 |
| `verifier\runs\2026-09-04_pd_v0.jsonl` | `5042869BDF85` | 100 | 2026-09-04 13:33:46 | 核查＋验证面 |
| `verifier\runs\v10_run1.md` | `54BE4344E99A` | 701 | 2026-08-24 07:51:43 | 核查＋验证面 |
| `verifier\runs\v11_run1.md` | `BD36F361EA12` | 514 | 2026-08-28 17:57:42 | 核查＋验证面 |
| `verifier\runs\v12_run1.md` | `927EAFCB3B0B` | 788 | 2026-08-28 20:01:49 | 核查＋验证面 |
| `verifier\runs\v13_run1.md` | `AA1456D217FC` | 145 | 2026-08-28 20:30:14 | 核查＋验证面 |
| `verifier\runs\v14_run1.md` | `3FDCA6C35DCB` | 145 | 2026-08-28 20:48:36 | 核查＋验证面 |
| `verifier\runs\v15_run1.md` | `634EF5FA4EF8` | 475 | 2026-08-28 21:17:49 | 核查＋验证面 |
| `verifier\runs\v16_run1.md` | `E6BF3B753FF6` | 359 | 2026-08-28 21:54:50 | 核查＋验证面 |
| `verifier\runs\v17_run1.md` | `9D0332C44044` | 283 | 2026-08-28 22:51:36 | 核查＋验证面 |
| `verifier\runs\v18_run1.md` | `4A3CE944CCE3` | 276 | 2026-08-28 23:57:39 | 核查＋验证面 |
| `verifier\runs\v19_run1.md` | `7B95DBD3F168` | 297 | 2026-08-29 00:25:02 | 核查＋验证面 |
| `verifier\runs\v20_run1.md` | `41D3D7F4A148` | 295 | 2026-08-29 00:35:08 | 核查＋验证面 |
| `verifier\runs\v21_run1.md` | `36B69E195F06` | 247 | 2026-08-29 01:26:03 | 核查＋验证面 |
| `verifier\runs\v21_run2.md` | `3246C7D46480` | 448 | 2026-08-29 11:35:00 | 核查＋验证面 |
| `verifier\runs\v22_run1.md` | `582531CCD67D` | 436 | 2026-08-29 11:22:52 | 核查＋验证面 |
| `verifier\runs\v23_run1.md` | `9578066064CC` | 586 | 2026-08-29 15:09:59 | 核查＋验证面 |
| `verifier\runs\v24_run1.md` | `67FD4FEC19F2` | 498 | 2026-08-29 15:50:05 | 核查＋验证面 |
| `verifier\runs\v25_run1.md` | `B81E2FB0EA28` | 526 | 2026-08-29 18:00:55 | 核查＋验证面 |
| `verifier\runs\v26_run1.md` | `09B69C05BB47` | 546 | 2026-08-29 19:39:05 | 核查＋验证面 |
| `verifier\runs\v27_run1.md` | `0759457758BE` | 559 | 2026-08-29 20:02:00 | 核查＋验证面 |
| `verifier\runs\v27_run2.md` | `82A92D9CE191` | 554 | 2026-08-29 20:03:11 | 核查＋验证面 |
| `verifier\runs\v28_run1.md` | `6D85472D724C` | 771 | 2026-08-29 21:09:29 | 核查＋验证面 |
| `verifier\runs\v29_run1.md` | `26A667EDEC7A` | 440 | 2026-08-29 23:03:33 | 核查＋验证面 |
| `verifier\runs\v29_run2.md` | `BADD1ED95A6D` | 627 | 2026-08-29 23:05:27 | 核查＋验证面 |
| `verifier\runs\v30_run1.md` | `CEF68A7A30A5` | 735 | 2026-08-29 23:47:50 | 核查＋验证面 |
| `verifier\runs\v30_run2.md` | `D22151B9AD6D` | 787 | 2026-08-29 23:49:54 | 核查＋验证面 |
| `verifier\runs\v30_run3.md` | `0DC553ED64C2` | 771 | 2026-08-29 23:51:37 | 核查＋验证面 |
| `verifier\runs\v31_run1.md` | `DCB11FEFABF2` | 673 | 2026-08-30 01:08:22 | 核查＋验证面 |
| `verifier\runs\v31_run2.md` | `8727C88269F3` | 747 | 2026-08-30 01:10:29 | 核查＋验证面 |
| `verifier\runs\v32_run1.md` | `1798C48ACEA7` | 859 | 2026-08-30 03:57:46 | 核查＋验证面 |
| `verifier\runs\v32_run2.md` | `83C987FB96D9` | 894 | 2026-08-30 03:59:13 | 核查＋验证面 |
| `verifier\runs\v32_run3.md` | `4A99A1134C8C` | 886 | 2026-08-30 04:06:01 | 核查＋验证面 |
| `verifier\runs\v33_run1.md` | `9E917334781C` | 2160 | 2026-08-30 05:05:50 | 核查＋验证面 |
| `verifier\runs\v33_run2.md` | `158948A53671` | 1783 | 2026-08-30 05:12:50 | 核查＋验证面 |
| `verifier\runs\v34_run1.md` | `03F773F08FA7` | 83 | 2026-08-30 09:57:16 | 核查＋验证面 |
| `verifier\runs\v34_run2.md` | `D9BFAAE6D08B` | 118 | 2026-08-30 14:13:30 | 核查＋验证面 |
| `verifier\runs\v35_run1.md` | `A693C838AE57` | 39 | 2026-08-30 15:47:20 | 核查＋验证面 |
| `verifier\runs\v35_run2.md` | `11CE6990B84A` | 118 | 2026-08-30 17:08:56 | 核查＋验证面 |
| `verifier\runs\v36_runs.log` | `18668F3D7D58` | 106 | 2026-09-17 23:20:46 | 核查＋验证面 |
| `verifier\runs\v37_runs.log` | `F0DE3DE22EAE` | 124 | 2026-09-17 23:20:46 | 核查＋验证面 |
| `verifier\runs\v38_runs.log` | `0FC3395DAC12` | 271 | 2026-09-17 23:20:47 | 核查＋验证面 |
| `verifier\runs\v39_runs.log` | `73B035B4FC3C` | 173 | 2026-09-17 23:20:48 | 核查＋验证面 |
| `verifier\runs\v40_runs.log` | `0E511B4E6CAA` | 133 | 2026-09-17 23:20:48 | 核查＋验证面 |
| `verifier\runs\v41_2026-08-30_run1.txt` | `E156E87CABA8` | 158 | 2026-09-17 23:20:49 | 核查＋验证面 |
| `verifier\runs\v42_2026-08-30_run1.txt` | `8FDE2819EF29` | 279 | 2026-09-17 23:20:49 | 核查＋验证面 |
| `verifier\runs\v42_2026-08-30_run2.txt` | `1AA0257CAAC9` | 156 | 2026-09-17 23:20:50 | 核查＋验证面 |
| `verifier\runs\v43_2026-09-01_run1.txt` | `AA82005B05DE` | 199 | 2026-09-17 23:20:51 | 核查＋验证面 |
| `verifier\v1\check.py` | `03BC1ADFC82F` | 2976 | 2026-08-23 10:27:37 | 核查＋执行体＋验证面 |
| `verifier\v10\check.py` | `4FD5FDD754C0` | 5261 | 2026-08-24 07:15:04 | 核查＋执行体＋验证面 |
| `verifier\v11\check.py` | `3B8682A7E562` | 2767 | 2026-08-28 17:56:50 | 核查＋执行体＋验证面 |
| `verifier\v12\check.py` | `87C9C883E3BF` | 4142 | 2026-08-29 01:14:15 | 核查＋执行体＋验证面 |
| `verifier\v13\check.py` | `1159FACAB6DB` | 3495 | 2026-08-28 20:29:43 | 核查＋执行体＋验证面 |
| `verifier\v14\check.py` | `4BA223D2185D` | 3278 | 2026-08-28 20:48:03 | 核查＋执行体＋验证面 |
| `verifier\v15\check.py` | `BE0F2BBAB0A2` | 3231 | 2026-08-28 21:17:37 | 核查＋执行体＋验证面 |
| `verifier\v16\check.py` | `223082632A1D` | 2691 | 2026-08-28 21:54:41 | 核查＋执行体＋验证面 |
| `verifier\v17\check.py` | `679792BE51ED` | 2897 | 2026-08-28 22:51:15 | 核查＋执行体＋验证面 |
| `verifier\v17\erratum.md` | `50F15F7EA3DC` | 438 | 2026-08-29 01:26:03 | 勘误＋核查＋验证面 |
| `verifier\v18\check.py` | `6ABDDA4F7400` | 3180 | 2026-08-29 01:14:16 | 核查＋执行体＋验证面 |
| `verifier\v19\check.py` | `C53CF72D085B` | 1995 | 2026-08-29 00:24:42 | 核查＋执行体＋验证面 |
| `verifier\v2\check.py` | `AF3A78983537` | 2510 | 2026-08-23 19:21:32 | 核查＋执行体＋验证面 |
| `verifier\v20\check.py` | `9D0F1E950DEE` | 2790 | 2026-08-29 00:33:07 | 核查＋执行体＋验证面 |
| `verifier\v20\erratum.md` | `35081D39F35B` | 316 | 2026-08-29 01:26:03 | 勘误＋核查＋验证面 |
| `verifier\v21\check.py` | `5E7D7435C4A3` | 3702 | 2026-08-29 01:23:52 | 核查＋执行体＋验证面 |
| `verifier\v22\check.py` | `F16BEAAE5675` | 2857 | 2026-08-29 11:20:44 | 核查＋执行体＋验证面 |
| `verifier\v23\check.py` | `9ECB25362C9A` | 2659 | 2026-08-29 15:08:00 | 核查＋执行体＋验证面 |
| `verifier\v24\check.py` | `E6C7513D54F3` | 3124 | 2026-08-29 15:49:47 | 核查＋执行体＋验证面 |
| `verifier\v25\check.py` | `CC6FF5453E06` | 2576 | 2026-08-29 18:00:10 | 核查＋执行体＋验证面 |
| `verifier\v26\check.py` | `C58A9652A42A` | 2595 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\v27\check.py` | `118524C7E808` | 2132 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\v28\check.py` | `B73A6B268F64` | 2201 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\v29\check.py` | `5923E2C379F6` | 2124 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\v3\check.py` | `02A5A86D38BF` | 2544 | 2026-08-23 19:21:32 | 核查＋执行体＋验证面 |
| `verifier\v30\check.py` | `2CF46F79A669` | 2565 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\v31\check.py` | `E5BB0020E500` | 2185 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\v32\check.py` | `399BFC743F24` | 2551 | 2026-09-16 11:01:12 | 核查＋执行体＋验证面 |
| `verifier\v33\check.py` | `32FEFC485326` | 6019 | 2026-08-30 05:11:44 | 核查＋执行体＋验证面 |
| `verifier\v34\check.py` | `0BBD226CD2AE` | 3715 | 2026-08-30 09:57:03 | 核查＋执行体＋验证面 |
| `verifier\v35\check.py` | `2130A5F5E1BF` | 2385 | 2026-08-30 15:47:20 | 核查＋执行体＋验证面 |
| `verifier\v36\check.sh` | `2212DCD98CD1` | 968 | 2026-09-18 13:43:52 | 核查＋执行体＋验证面 |
| `verifier\v37\check.sh` | `CED43B5F8800` | 1141 | 2026-09-18 13:43:52 | 核查＋执行体＋验证面 |
| `verifier\v38\check.sh` | `43B501C5C20D` | 1705 | 2026-09-17 23:20:52 | 核查＋执行体＋验证面 |
| `verifier\v39\check.sh` | `D48AC555761F` | 1935 | 2026-09-17 23:20:53 | 核查＋执行体＋验证面 |
| `verifier\v4\check.py` | `F058E85C5383` | 3205 | 2026-08-23 19:33:47 | 核查＋执行体＋验证面 |
| `verifier\v40\check.sh` | `7B15CD2F4C7E` | 1604 | 2026-09-17 23:20:54 | 核查＋执行体＋验证面 |
| `verifier\v41\check.sh` | `2C9FE869DAAA` | 1687 | 2026-09-17 23:20:54 | 核查＋执行体＋验证面 |
| `verifier\v42\check.sh` | `3EA87E2CFC61` | 1509 | 2026-09-17 23:20:55 | 核查＋执行体＋验证面 |
| `verifier\v43\check.sh` | `71B83217032D` | 1224 | 2026-09-17 23:20:55 | 核查＋执行体＋验证面 |
| `verifier\v5\check.py` | `3D776381F665` | 2255 | 2026-08-23 20:04:44 | 核查＋执行体＋验证面 |
| `verifier\v6\check.py` | `8366078A10E4` | 2757 | 2026-08-23 20:23:46 | 核查＋执行体＋验证面 |
| `verifier\v7\check.py` | `A70A68037D92` | 4300 | 2026-08-23 21:03:13 | 核查＋执行体＋验证面 |
| `verifier\v8\check.py` | `01B63B1A9C5F` | 3210 | 2026-08-23 21:40:59 | 核查＋执行体＋验证面 |
| `verifier\v9\check.py` | `5FAAD917D839` | 5352 | 2026-08-23 23:46:50 | 核查＋执行体＋验证面 |

### §2-6 deposon_team/（86 件 / 1,446,106 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.cpython-314.pyc` | `F96453EBEAD6` | 55784 | 2026-10-09 23:25:55 | 团队件面 |
| `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.cpython-314.pyc` | `80A752CCA163` | 57022 | 2026-10-09 23:25:21 | 团队件面 |
| `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc` | `74467BB37F95` | 103946 | 2026-10-10 10:03:53 | 团队件面 |
| `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | `341B6726AC4E` | 33994 | 2026-10-10 11:23:01 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | `CD43C41716F0` | 35321 | 2026-10-10 11:23:01 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py` | `041525FD05A2` | 31457 | 2026-10-10 10:50:15 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | `DE16BC002198` | 20322 | 2026-09-29 13:43:09 | 执行体＋团队件面 |
| `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | `7C095C54FB99` | 21826 | 2026-10-09 13:38:37 | 执行体＋团队件面 |
| `deposon_team\plugins\_pg_v01_compute.py` | `D511C545F88E` | 20923 | 2026-09-16 18:54:48 | 执行体＋团队件面 |
| `deposon_team\plugins\_tdf_s1_2026_10_12.py` | `5F9AB0AD7BAB` | 5856 | 2026-10-12 01:23:22 | 执行体＋团队件面 |
| `deposon_team\plugins\_tdf_s1b_2026_10_12.py` | `BEBBA19790C0` | 8064 | 2026-10-12 01:24:29 | 执行体＋团队件面 |
| `deposon_team\plugins\_tdf_s1c_2026_10_12.py` | `D8BD9C41194A` | 7485 | 2026-10-12 01:26:27 | 执行体＋团队件面 |
| `deposon_team\plugins\_tdf_s2_apply_2026_10_12.py` | `4BD6D16E20D7` | 10899 | 2026-10-12 01:29:57 | 执行体＋团队件面 |
| `deposon_team\plugins\_tdf_s3_jumps_2026_10_12.py` | `16F7E10AC78F` | 676 | 2026-10-12 01:30:39 | 执行体＋团队件面 |
| `deposon_team\plugins\_tdf_s3b_2026_10_12.py` | `CCEC66BB426E` | 1229 | 2026-10-12 01:31:26 | 执行体＋团队件面 |
| `deposon_team\plugins\_tdf_s4_final_2026_10_12.py` | `1DF9A5D22E42` | 2695 | 2026-10-12 01:34:23 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3_construct_diag_2026_09_23.py` | `CE10A3DBCB2B` | 22490 | 2026-09-23 14:20:25 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r1_inventory_2026_09_23.py` | `7B97EF02C52E` | 5526 | 2026-09-23 13:13:02 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r1b_2026_09_23.py` | `B5E77E114D88` | 1795 | 2026-09-23 13:13:45 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r1c_2026_09_23.py` | `FDFEB03E8D6F` | 2919 | 2026-09-23 13:14:27 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r1d_2026_09_23.py` | `4ADBD9B5EAB5` | 1712 | 2026-09-23 13:14:59 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r2_verify_2026_09_23.py` | `AEE06C009ED1` | 4528 | 2026-09-23 13:24:40 | 核查＋评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r2b_2026_09_23.py` | `9D6343BD9755` | 3189 | 2026-09-23 13:25:02 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r2c_2026_09_23.py` | `1C30CDA5AAD6` | 4400 | 2026-09-23 13:25:39 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r3_sha_2026_09_23.py` | `D3B45B64C0DA` | 1881 | 2026-09-23 13:26:41 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r4_fixscan_2026_09_23.py` | `917B18EB9A5F` | 3896 | 2026-09-23 13:31:36 | 核查＋评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r5_anchor_probe_2026_09_23.py` | `7EBE0F65A64A` | 2653 | 2026-09-23 13:33:00 | 核查＋评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r6_final_sha_2026_09_23.py` | `8AF3F4460144` | 2135 | 2026-09-23 13:34:47 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r7_fix_e15_2026_09_23.py` | `40D66379EF17` | 2951 | 2026-09-23 13:39:17 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r8_precise_scan_2026_09_23.py` | `2FF60F715DEF` | 5241 | 2026-09-23 13:44:30 | 核查＋评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3_review_r9_final_state_2026_09_23.py` | `FCF5BAF4DD7F` | 2117 | 2026-09-23 13:46:51 | 评审＋执行体＋团队件面 |
| `deposon_team\plugins\_v3n_cpath_live_2026_09_27.py` | `5248BA7AC21C` | 19823 | 2026-09-27 14:16:12 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3n_cpath_live_r1_2026_09_27.py` | `321D39C7DF41` | 28187 | 2026-09-27 20:54:38 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3n_cpath_live_rerun_2026_10_01.py` | `7D8D26174CE9` | 22133 | 2026-10-01 14:02:02 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3n_ktb1_distortion_bound_2026_09_27.py` | `5572EF4055A5` | 13055 | 2026-09-27 14:16:59 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3n_pg_boss_live_2026_09_27.py` | `B6040D34F0AC` | 14223 | 2026-09-27 14:15:38 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3r1p1_21_ktb1_distortion_2026_09_27.py` | `F7B61F041C0B` | 30672 | 2026-09-27 16:35:23 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3r1p1_35_gt2b_bankseed_2026_09_27.py` | `62353279CD0C` | 26734 | 2026-09-27 16:23:05 | 执行体＋团队件面 |
| `deposon_team\plugins\_v3x_frozen_schema_v1.json` | `9E99DCC4D920` | 12919 | 2026-09-17 10:27:19 | 团队件面 |
| `deposon_team\plugins\_v4_contrast_nondegenerate_2026_09_23.py` | `A0BFC7DF887F` | 42876 | 2026-09-23 16:06:11 | 执行体＋团队件面 |
| `deposon_team\plugins\_v4_wide_s1_inventory_2026_09_27.py` | `145AE518F5F0` | 1669 | 2026-09-27 20:18:35 | 执行体＋团队件面 |
| `deposon_team\plugins\_v4_wide_s5_prescan_2026_09_27.py` | `724964301582` | 2839 | 2026-09-27 20:25:46 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_apply_b4_2026_09_27.py` | `FD0A08029841` | 6113 | 2026-09-27 20:10:30 | 执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s0_verify_2026_09_27.py` | `4DCB81343577` | 8462 | 2026-09-27 20:02:03 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s2_b1diff_2026_09_27.py` | `B61CB447F306` | 2015 | 2026-09-27 20:02:28 | 执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s2_b1recheck_2026_09_27.py` | `E643AC7F9718` | 5650 | 2026-09-27 20:03:23 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s3_b2probe_2026_09_27.py` | `A5DB027ADAC5` | 6089 | 2026-09-27 20:08:43 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s3b_b2confirm_2026_09_27.py` | `7AAF6F21D459` | 3604 | 2026-09-27 20:09:01 | 执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s4_b4verify_2026_09_27.py` | `5E1EC533DE1F` | 2595 | 2026-09-27 20:09:38 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s4b_b4recompute_2026_09_27.py` | `EDCDFDA20F91` | 4174 | 2026-09-27 20:09:59 | 核查＋读数/结果＋执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s4c_regonly_2026_09_27.py` | `20F265761280` | 3900 | 2026-09-27 20:10:57 | 执行体＋团队件面 |
| `deposon_team\plugins\_v4_wt_s6_final_2026_09_27.py` | `653077D03468` | 3435 | 2026-09-27 20:13:00 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_gt8_lowarm_2026_09_29.py` | `9B21988AFFF7` | 57033 | 2026-09-29 15:28:35 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_gt8_lowarm_setA_2026_09_29.py` | `F72F062F6B67` | 43224 | 2026-09-29 15:27:05 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_gt8_lowarm_seta_verify_2026_09_29.py` | `BED2D444C196` | 15553 | 2026-09-29 15:33:15 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_v5_item21_strategyqa_realias_2026_09_29.py` | `AAAAE1F02815` | 25482 | 2026-09-29 16:15:43 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_item35_v2_matrix_2026_09_29.py` | `EF73F9B90AFC` | 44777 | 2026-09-29 12:23:55 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_item35_v3_collinear_2026_09_29.py` | `7115928822A1` | 63376 | 2026-09-29 14:21:40 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_pp1_pattern_fix_2026_09_29.py` | `E3CF9D552F30` | 22544 | 2026-09-29 17:31:40 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_wa_s2_2026_09_30.py` | `88CD82E65627` | 5812 | 2026-09-30 19:03:02 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5_wa_s4_2026_09_30.py` | `2E7743DD8139` | 2063 | 2026-09-30 19:07:54 | 执行体＋团队件面 |
| `deposon_team\plugins\_v5r_s40_rerun_executor_fix_2026_09_29.py` | `A4AE5D5F19C8` | 17665 | 2026-09-29 19:19:06 | 执行体＋团队件面 |
| `deposon_team\plugins\_verify_15frozen.py` | `EFAE9274962E` | 3905 | 2026-09-17 10:12:02 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_verify_15frozen_v1.py` | `60523E406055` | 2094 | 2026-09-17 10:27:53 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_verify_batch5_2026_09_18.py` | `BC6CBF27A338` | 4238 | 2026-09-18 13:45:30 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_verify_pg_v0.py` | `CDD3415AD993` | 3978 | 2026-09-17 10:12:02 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\_verify_pg_v0_v1.py` | `67088AE1A860` | 2521 | 2026-09-17 10:27:53 | 核查＋执行体＋团队件面 |
| `deposon_team\plugins\boss_pa_1_rbr_rm.py` | `5CC594147E00` | 17743 | 2026-09-15 15:16:26 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py` | `06016F90FD3A` | 45777 | 2026-10-09 22:54:53 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.py` | `3524E454D8ED` | 47580 | 2026-10-09 22:59:41 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py` | `7761F2C339E6` | 61102 | 2026-09-29 12:05:45 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.py` | `77724BCE0C06` | 91135 | 2026-09-29 13:40:58 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pa_2_potential_game.py` | `33DFB4338C53` | 10410 | 2026-09-15 15:16:26 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pa_3_replicator_dynamics.py` | `A2BD9DD24C25` | 12900 | 2026-09-15 15:16:26 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pc_1_2d_ising_universality.py` | `BFC319808447` | 7547 | 2026-09-15 15:37:54 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pc_2_transverse_field_ising.py` | `210105A7F29A` | 7053 | 2026-09-15 15:37:54 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pc_3_reservoir_computing.py` | `021EA39B7193` | 7373 | 2026-09-15 15:37:54 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pg_1_riemannian_degenerate.py` | `97FEDE6C8A4E` | 5996 | 2026-09-15 15:37:53 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pg_2_hyperbolic_classification_collapse.py` | `F006D4CACA94` | 5285 | 2026-09-15 15:37:53 | 执行体＋团队件面 |
| `deposon_team\plugins\boss_pg_3_geodesic_violation.py` | `09F37C01A258` | 5517 | 2026-09-15 15:37:54 | 执行体＋团队件面 |
| `deposon_team\plugins\github_dir_structure_2026_09_18.md` | `0FD07AD38282` | 11675 | 2026-09-15 15:17:42 | 团队件面 |
| `deposon_team\plugins\github_upload_2026_09_18.sh` | `52BC19845B2B` | 6030 | 2026-09-15 15:18:06 | 执行体＋团队件面 |
| `deposon_team\plugins\skill_a_p_a_60cells.py` | `B1463BB24403` | 9078 | 2026-09-11 17:05:38 | 判死线/准入门＋执行体＋团队件面 |
| `deposon_team\plugins\skill_b_p_c_alpha_beta.py` | `E5A299F69A22` | 8699 | 2026-09-11 17:05:38 | 判死线/准入门＋执行体＋团队件面 |
| `deposon_team\plugins\skill_c_p_e_3modality.py` | `E19E76C5DA7E` | 8915 | 2026-09-11 17:05:38 | 判死线/准入门＋执行体＋团队件面 |
| `deposon_team\plugins\skill_d_p_f_observer.py` | `3E369A1F6171` | 15927 | 2026-09-15 13:30:57 | 判死线/准入门＋执行体＋团队件面 |

### §2-7 corpus/（43 件 / 951,375 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `corpus\v20\all.json` | `8DF31C95B1FC` | 2557 | 2026-09-17 10:24:31 | 语料 |
| `corpus\v20\by_model\coze\coze_artifact_v_2026_09_16.json` | `FEE04170AA73` | 10978 | 2026-09-24 11:28:03 | 语料 |
| `corpus\v20\by_model\GLM_1\three_way_glm_slot_blind_test_2026_09_16.json` | `268AB1239A8A` | 19685 | 1979-11-30 00:00:00 | 语料 |
| `corpus\v20\by_model\GLM_2\glm_artifact_v_2026_09_16.json` | `39732A92B5C9` | 13150 | 1979-11-30 00:00:00 | 语料 |
| `corpus\v20\by_model\kimi\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 | 2026-09-16 18:39:54 | 语料 |
| `corpus\v20\by_model\minimax\artifact_v_2026_09_16.json` | `9E1CCBDCEACC` | 25347 | 2026-09-16 18:20:56 | 语料 |
| `corpus\v20\index.json` | `8423FFE266AF` | 7335 | 2026-08-28 23:53:05 | 语料 |
| `corpus\v20\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 | 2026-09-16 18:39:54 | 语料 |
| `corpus\v20\index_v3_2026_09_29.json` | `3BA2449CF986` | 24421 | 2026-10-01 09:43:44 | 语料 |
| `corpus\v20\index_v3_2026_10_09.json` | `74B27393574F` | 24837 | 2026-10-09 13:39:49 | 语料 |
| `corpus\v20\L_algorithm_process.json` | `FF0EF9131FDD` | 3920 | 2026-08-28 17:38:45 | 语料 |
| `corpus\v20\L_biological_taxonomy.json` | `0C7AD5235AE9` | 3562 | 2026-08-28 17:38:45 | 语料 |
| `corpus\v20\L_geography_world.json` | `77B0C1466DC0` | 3699 | 2026-08-28 23:11:44 | 语料 |
| `corpus\v20\L_historical_causality.json` | `12E0DE4BB103` | 4329 | 2026-08-28 17:38:45 | 语料 |
| `corpus\v20\L_physics_concepts.json` | `D8780859D310` | 3397 | 2026-08-28 17:38:45 | 语料 |
| `corpus\v20\L_project_management.json` | `32CA32C00DA4` | 3898 | 2026-08-28 23:12:37 | 语料 |
| `corpus\v20\S1.json` | `A890C56F7705` | 1512 | 2026-08-28 17:07:51 | 语料 |
| `corpus\v20\S1_n35.json` | `F035043BFDDD` | 2521 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S1_n45.json` | `52B4D6E52AE9` | 3171 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S1_n60.json` | `584DE37EBEC1` | 4122 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S2.json` | `B1F6C5AA4DE6` | 2234 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S2_n20.json` | `BFC9D38C8C0F` | 1537 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S2_n35.json` | `E20A1BBEAEE7` | 2480 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S2_n45.json` | `58BB0A7D2E46` | 3175 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S2_n60.json` | `01C492A97B98` | 4123 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S3.json` | `3B6879AB2440` | 2297 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S4.json` | `E6045F0920EC` | 4932 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S5.json` | `4B10F9CAE09F` | 3319 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S6.json` | `01D9C95EA690` | 3320 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S6_n20.json` | `4A0689892C1B` | 1724 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S6_n35.json` | `8D02FBADD277` | 2676 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\S6_n60.json` | `704E2FD0D021` | 4296 | 2026-08-28 17:07:52 | 语料 |
| `corpus\v20\strip_captions_22.json` | `6A2656878745` | 12798 | 2026-09-11 11:33:40 | 语料 |
| `corpus\v20_caption_surface\_adendum_I_po_captions_closure_20260917_132049.json` | `18165008BEF6` | 4429 | 2026-09-17 13:20:50 | 语料 |
| `corpus\v20_caption_surface\_inspect_captions.py` | `DFB02ADE1474` | 591 | 2026-09-10 17:31:00 | 执行体＋语料 |
| `corpus\v20_caption_surface\_p_d_b3_merkle_22caption_runner_2026_09_16.py` | `D2CD7ACB29A1` | 18596 | 2026-09-16 18:54:48 | 执行体＋语料 |
| `corpus\v20_caption_surface\_p_d_v03_22caption_verification_20260917_163757.json` | `DFBCC5D6FC34` | 13775 | 2026-09-17 16:37:57 | 核查＋语料 |
| `corpus\v20_caption_surface\_v41_flash_rag_caption_embs.bak.json` | `25F745609658` | 612511 | 2026-09-10 17:05:53 | 语料 |
| `corpus\v20_caption_surface\caption_distance_mat_22.json` | `1C4FFF004CC4` | 8552 | 2026-09-23 16:44:30 | 语料 |
| `corpus\v20_caption_surface\caption_features_22.json` | `727A253566DD` | 18362 | 2026-09-23 16:44:30 | 语料 |
| `corpus\v20_caption_surface\caption_stats_22.json` | `DA34F54D4F5B` | 632 | 2026-09-23 16:44:30 | 语料 |
| `corpus\v20_caption_surface\manifest.json` | `4FDDA6480BB5` | 1477 | 2026-09-23 16:44:30 | 语料 |
| `corpus\v20_caption_surface\strip_captions_22.json` | `6A2656878745` | 12798 | 2026-09-11 11:33:40 | 语料 |

### §2-8 reviews/（32 件 / 376,244 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `reviews\data\t1_potential.csv` | `E110A020954F` | 4833 | 2026-08-28 21:30:52 | 评审＋评审面 |
| `reviews\data\t1b_classics.csv` | `82016E695F48` | 5450 | 2026-08-28 21:32:04 | 评审＋评审面 |
| `reviews\data\t1c_loglinear.csv` | `C50FF98A95CC` | 5566 | 2026-08-28 21:33:20 | 评审＋评审面 |
| `reviews\data\t1d_pagerank.csv` | `8B1A9E5113BB` | 4167 | 2026-08-28 21:36:57 | 评审＋评审面 |
| `reviews\data\t2_linkpred.csv` | `19555B7D9D43` | 6750 | 2026-08-28 21:30:43 | 评审＋评审面 |
| `reviews\data\t2b_linkpred.csv` | `6DE8F0E651C4` | 5520 | 2026-08-28 21:31:15 | 评审＋评审面 |
| `reviews\data\t2c_advlink.csv` | `67D1D8342060` | 6886 | 2026-08-28 21:32:32 | 评审＋评审面 |
| `reviews\data\t2d_hiding.csv` | `5749CE2C5BF7` | 5377 | 2026-08-28 21:33:27 | 评审＋评审面 |
| `reviews\data\t2e_nettack.csv` | `2628F74421F2` | 1875 | 2026-08-28 21:35:25 | 评审＋评审面 |
| `reviews\data\t2f_waniek.csv` | `F0D2C9D2A39B` | 1271 | 2026-08-28 21:35:28 | 评审＋评审面 |
| `reviews\data\t3_mechdesign.csv` | `6E8B6E4730A8` | 6680 | 2026-08-28 21:31:20 | 评审＋评审面 |
| `reviews\data\t3b_verifiable.csv` | `F48C9F09A3B4` | 6731 | 2026-08-28 21:32:32 | 核查＋评审＋评审面 |
| `reviews\data\t3d_llmmd.csv` | `49028967AD57` | 3405 | 2026-08-28 21:35:31 | 评审＋评审面 |
| `reviews\data\t3e_commit.csv` | `BF0A2B544A74` | 3691 | 2026-08-28 21:36:14 | 评审＋评审面 |
| `reviews\data\t4_poa.csv` | `8BA9FADA9EAD` | 6567 | 2026-08-28 21:31:59 | 评审＋评审面 |
| `reviews\deep_probe_R1.md` | `190DD5DF9AF2` | 14895 | 2026-08-29 01:04:00 | 核查＋评审＋评审面 |
| `reviews\deep_probe_R2.md` | `A4F8A55B70BA` | 23391 | 2026-08-29 01:10:13 | 核查＋评审＋评审面 |
| `reviews\design_probe_v19.md` | `C41F1717310E` | 13967 | 2026-08-24 00:49:48 | 核查＋评审＋评审面 |
| `reviews\experiment_design_v19.md` | `56ECEF878539` | 8840 | 2026-08-24 00:35:44 | 评审＋评审面 |
| `reviews\independent_review_20260823.md` | `7474FC258375` | 1724 | 2026-08-23 21:40:22 | 评审＋评审面 |
| `reviews\literature_scan_v19.md` | `70EA38D5B9C0` | 28449 | 2026-08-24 00:40:36 | 核查＋评审＋评审面 |
| `reviews\literature_scan_v2X_A.md` | `D0BBA9379B4B` | 18876 | 2026-08-28 21:42:49 | 核查＋评审＋评审面 |
| `reviews\literature_scan_v2X_B.md` | `313B30815A39` | 30468 | 2026-08-28 21:50:11 | 核查＋评审＋评审面 |
| `reviews\peer_review_v19_A.md` | `28878116D87B` | 24409 | 2026-08-24 00:36:05 | 评审＋评审面 |
| `reviews\peer_review_v19_B.md` | `DA98F9E310D4` | 42672 | 2026-08-24 01:07:19 | 评审＋评审面 |
| `reviews\post_draft_verification_v2X.md` | `0C49F2D36088` | 9979 | 2026-08-29 21:06:20 | 核查＋评审＋评审面 |
| `reviews\post_edit_verification_v19.md` | `E262E9D684FE` | 19327 | 2026-08-24 07:49:36 | 核查＋评审＋评审面 |
| `reviews\review_coach_v2X_draft.md` | `0BAFE659C00D` | 23468 | 2026-08-29 22:22:13 | 评审＋评审面 |
| `reviews\review_coach_v2X_draft_r2.md` | `67162AB18F9A` | 15721 | 2026-08-29 23:42:38 | 评审＋评审面 |
| `reviews\review_coach_v2X_outline.md` | `5BEBB5E1D329` | 11295 | 2026-08-29 15:34:49 | 评审＋评审面 |
| `reviews\review_format_v2X.md` | `2DC4B45424AB` | 6656 | 2026-08-30 04:02:12 | 评审＋评审面 |
| `reviews\review_realign_v2X.md` | `3ECB285DB3D8` | 7338 | 2026-08-30 01:03:56 | 评审＋评审面 |

### §2-9 tests/（23 件 / 212,514 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `tests\test_agents_merge.py` | `C7CC85FFB3F0` | 26615 | 2026-08-30 10:34:38 | 执行体＋工具/脚本 |
| `tests\test_diffusion.py` | `2452BE26AF7E` | 12463 | 2026-08-23 19:21:32 | 执行体＋工具/脚本 |
| `tests\test_fast.py` | `5829F89C2352` | 3653 | 2026-08-28 22:11:59 | 执行体＋工具/脚本 |
| `tests\test_fingerprint_v0.py` | `506BA4A55704` | 13788 | 2026-09-01 16:35:59 | 执行体＋工具/脚本 |
| `tests\test_gt_common.py` | `6A2F32D1316A` | 3697 | 2026-08-30 10:29:22 | 执行体＋工具/脚本 |
| `tests\test_llm_fetch.py` | `90772F5CF41B` | 11095 | 2026-08-30 10:28:46 | 执行体＋工具/脚本 |
| `tests\test_llm_prior.py` | `11C2FFA37610` | 7701 | 2026-08-23 20:02:35 | 执行体＋工具/脚本 |
| `tests\test_new_modes.py` | `0B2276028391` | 21275 | 2026-08-23 09:40:33 | 执行体＋工具/脚本 |
| `tests\test_protocol.py` | `F103C9D87C61` | 6979 | 2026-08-30 04:58:18 | 执行体＋工具/脚本 |
| `tests\test_v18.py` | `C523AE4B0989` | 17093 | 2026-08-23 23:15:42 | 执行体＋工具/脚本 |
| `tests\test_v19.py` | `B44E2945FA31` | 6056 | 2026-08-24 01:10:27 | 执行体＋工具/脚本 |
| `tests\test_v19_benchmark.py` | `F343754F380C` | 7371 | 2026-08-24 01:12:52 | 执行体＋工具/脚本 |
| `tests\test_v20.py` | `E4712875F65D` | 13249 | 2026-08-28 17:19:09 | 执行体＋工具/脚本 |
| `tests\test_v20_gt2b.py` | `4CD18AE1D3DC` | 4318 | 2026-08-29 19:58:34 | 执行体＋工具/脚本 |
| `tests\test_v20_gt5.py` | `1F104B13A170` | 5746 | 2026-08-29 15:36:51 | 执行体＋工具/脚本 |
| `tests\test_v20_gt5b.py` | `81FEB1F137B4` | 2423 | 2026-08-29 15:44:42 | 执行体＋工具/脚本 |
| `tests\test_v20_gt6.py` | `5C7DD774A3F3` | 2584 | 2026-08-29 15:44:43 | 执行体＋工具/脚本 |
| `tests\test_v20_gt7.py` | `E8727F8F42DA` | 6489 | 2026-08-29 17:56:48 | 执行体＋工具/脚本 |
| `tests\test_v20_gt8.py` | `B9479374DE4D` | 5122 | 2026-08-29 19:34:11 | 执行体＋工具/脚本 |
| `tests\test_v20_gt8b.py` | `3C4395DF9311` | 10109 | 2026-08-29 22:27:24 | 执行体＋工具/脚本 |
| `tests\test_v20_gt8c.py` | `562DD8B920BC` | 13458 | 2026-08-30 15:55:13 | 执行体＋工具/脚本 |
| `tests\test_v21_gtformal.py` | `74650B1D603B` | 7376 | 2026-08-30 15:20:33 | 执行体＋工具/脚本 |
| `tests\test_v22_p1c.py` | `B19BDB965CC0` | 3854 | 2026-08-30 18:30:56 | 执行体＋工具/脚本 |

### §2-10 scripts/（10 件 / 148,821 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `scripts\run_deepseek_v41_30cells_v2.py` | `C7411AE13EC0` | 14017 | 2026-09-10 16:15:10 | 执行体＋工具/脚本 |
| `scripts\run_deepseek_v41_30cells_v3.py` | `03BC34EA88A8` | 13955 | 2026-09-10 16:38:40 | 执行体＋工具/脚本 |
| `scripts\run_deepseek_v41_60cells_v2_startup.py` | `769E1D04503B` | 16071 | 2026-09-10 17:31:43 | 执行体＋工具/脚本 |
| `scripts\run_embedding_dual_smoke.py` | `9253225DE974` | 13599 | 2026-09-10 17:03:53 | 执行体＋工具/脚本 |
| `scripts\run_v3x_6way_stage3_recovery.py` | `E4F96F2E9E4F` | 15872 | 2026-09-10 18:03:01 | 执行体＋工具/脚本 |
| `scripts\run_v3x_6way_verification.py` | `27A046D569D1` | 25060 | 2026-09-10 17:55:59 | 核查＋执行体＋工具/脚本 |
| `scripts\run_v3x_finalize.py` | `46787531BF8E` | 5932 | 2026-09-10 18:15:09 | 终判/裁定＋执行体＋工具/脚本 |
| `scripts\run_v3x_stage3_minimal.py` | `8B5D42772D5E` | 12477 | 2026-09-10 18:07:56 | 执行体＋工具/脚本 |
| `scripts\run_v41_flash_5cells_fix.py` | `E4546D734A53` | 17914 | 2026-09-10 16:54:23 | 执行体＋工具/脚本 |
| `scripts\run_volcengine_seed_code_30cells.py` | `75002485AA94` | 13924 | 2026-09-16 11:01:12 | 执行体＋工具/脚本 |

### §2-11 paper/（5 件 / 145,087 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `paper\deposon_paper_final_cn.md` | `C5F6A23F4408` | 53838 | 2026-09-20 17:11:14 | 论文/脚本文本＋论文面 |
| `paper\deposon_paper_final_en.md` | `2EC20B96E941` | 68164 | 2026-09-20 17:11:14 | 论文/脚本文本＋论文面 |
| `paper\FIGURE_LANGUAGE_POLICY.md` | `A18B5D0D4485` | 2495 | 2026-08-30 11:16:21 | 论文/脚本文本＋论文面 |
| `paper\v2\outline_v2X.md` | `116D193B1607` | 10476 | 2026-08-30 10:43:36 | 论文/脚本文本＋论文面 |
| `paper\v2\related_work_v2X.md` | `7FB001ADD973` | 10114 | 2026-08-29 15:43:30 | 论文/脚本文本＋论文面 |

### §2-12 tools/（5 件 / 61,516 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `tools\exp_harness.py` | `275E480BA4D9` | 10090 | 2026-09-09 16:16:50 | 执行体＋工具/脚本 |
| `tools\llm_client.py` | `1722500DA4AA` | 8118 | 2026-09-09 16:16:02 | 执行体＋工具/脚本 |
| `tools\make_figures_v2.py` | `0DC3EA09F42D` | 21073 | 2026-08-30 20:52:09 | 执行体＋工具/脚本 |
| `tools\make_figures_v2_en.py` | `B4E880A6AF33` | 21188 | 2026-08-30 20:46:55 | 执行体＋工具/脚本 |
| `tools\read_key.py` | `A9B56C4E775F` | 1047 | 2026-09-10 14:45:46 | 执行体＋工具/脚本 |

### §2-13 attacks/（4 件 / 12,922 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `attacks\__init__.py` | `D11E085D9ECC` | 183 | 2026-09-01 11:19:18 | 执行体＋攻击/鲁棒性面 |
| `attacks\a1_delete_anchor.py` | `78AC391D16FC` | 4693 | 2026-09-04 13:11:07 | 执行体＋攻击/鲁棒性面 |
| `attacks\a2_reshuffle_manifest.py` | `3D54B277620E` | 3792 | 2026-09-01 11:19:34 | 执行体＋攻击/鲁棒性面 |
| `attacks\a3_rewrite_runs.py` | `F02B3EEE8D6E` | 4254 | 2026-09-01 16:31:25 | 执行体＋攻击/鲁棒性面 |

### §2-14 .mavis/（4 件 / 992 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `.mavis\scripts\kt_a1\test_persist.txt` | `2898ABB5082B` | 15 | 2026-09-24 22:30:25 | 运行时面 |
| `.mavis\scripts\kt_a1\test_write.txt` | `9F86D081884C` | 4 | 2026-09-24 22:27:23 | 运行时面 |
| `.mavis\scripts\kt_b1\fix_safe_float.py` | `4420543E60A4` | 966 | 2026-09-24 22:23:52 | 执行体＋运行时面 |
| `.mavis\scripts\kt_c1\test_write.txt` | `85D443E165BB` | 7 | 2026-09-24 22:29:06 | 运行时面 |

### §2-15 .trae/（2 件 / 34,781 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `.trae\scripts\_arxiv_renumber.py` | `F488AD141EF9` | 16531 | 2026-09-09 14:14:27 | 执行体＋第三方件面 |
| `.trae\scripts\_verify_tex.py` | `3B977BB8A715` | 18250 | 2026-09-09 14:14:27 | 核查＋执行体＋第三方件面 |

### §2-16 （仓根・顶层散件）（73 件 / 1,021,862 B）

| 相对路径 | SHA-12 | bytes | mtime | 类别判定 |
|:--|:--|-:|:--|:--|
| `$null` | `400D7E27B03F` | 898 | 2026-10-10 20:18:55 | 其他/未归类 |
| `.gitignore` | `7D8D71EA2AF2` | 91 | 2026-08-22 21:07:01 | 其他/未归类 |
| `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `739245682D40` | 26633 | 2026-09-26 19:13:56 | 终判/裁定 |
| `_v5_gt_exec_2026_09_29.py` | `EEF7B446CC0E` | 75689 | 2026-09-29 11:17:03 | 执行体 |
| `audits_dataset_health.json` | `4F827071B0B8` | 7398 | 2026-08-28 15:53:27 | 核查 |
| `audits_outliers.json` | `3B1C881C4594` | 132875 | 2026-08-28 15:53:28 | 核查 |
| `audits_security.json` | `553C90AA3BA6` | 1610 | 2026-08-28 15:52:30 | 核查 |
| `deposon_agents.py` | `5496954B0AD5` | 104622 | 2026-09-18 13:41:44 | 执行体 |
| `deposon_agents_v1_3.py` | `715026B48678` | 1827 | 2026-08-30 10:23:11 | 执行体 |
| `deposon_agents_v1_4.py` | `59F0CE83E06D` | 1726 | 2026-08-30 10:23:11 | 执行体 |
| `deposon_diffusion.py` | `FE4D668EB1DA` | 19171 | 2026-08-30 04:52:41 | 执行体 |
| `deposon_fast.py` | `7A2DCBADAC73` | 4581 | 2026-08-30 04:53:24 | 执行体 |
| `deposon_g2_modes.py` | `6A175A264B46` | 6316 | 2026-08-23 09:33:59 | 执行体 |
| `deposon_photonics.py` | `C7E78AD9F030` | 10402 | 2026-08-29 00:34:47 | 执行体 |
| `deposon_protocol.py` | `CA756668CE2E` | 2845 | 2026-08-30 04:55:56 | 执行体 |
| `fingerprint_v0.py` | `C0C38007C4E8` | 10950 | 2026-09-01 16:36:32 | 执行体 |
| `gt_common.py` | `425B4B2F1C01` | 3601 | 2026-08-30 10:17:31 | 执行体 |
| `LICENSE` | `6A703B06F0FE` | 1085 | 2026-08-22 21:07:57 | 其他/未归类 |
| `llm_fetch.py` | `FDA22714DE2D` | 8433 | 2026-08-30 10:09:18 | 执行体 |
| `llm_prior.py` | `7FBA7D72A679` | 7466 | 2026-08-30 10:10:54 | 执行体 |
| `mindmap_corpus_v20.py` | `E77E7F3455E0` | 25791 | 2026-09-29 12:06:04 | 执行体 |
| `README.md` | `A80B3DB006A5` | 7279 | 2026-09-30 23:53:17 | 其他/未归类 |
| `README_V4_2026_09_29.md` | `A6F88FB6E325` | 58635 | 2026-09-30 20:36:18 | 其他/未归类 |
| `RELEASE_v1.4.0.md` | `FF9FF3177C06` | 3847 | 2026-08-23 16:38:29 | 其他/未归类 |
| `requirements.txt` | `AB3045B2C6D9` | 27 | 2026-08-22 21:07:57 | 其他/未归类 |
| `run_benchmark_v1_3.py` | `54EA2644DF14` | 10690 | 2026-08-23 00:30:44 | 执行体 |
| `run_benchmark_v1_4_gsm8k.py` | `FAC50B283DA5` | 11253 | 2026-08-24 01:05:38 | 执行体 |
| `run_benchmark_v1_4_strategyqa.py` | `F523875A15DB` | 14537 | 2026-08-30 10:26:51 | 执行体 |
| `run_g2_ensemble.py` | `E3914712A984` | 8907 | 2026-08-23 09:40:07 | 执行体 |
| `run_v15_experiment.py` | `58A5623F3AA1` | 22761 | 2026-08-30 04:56:14 | 执行体 |
| `run_v16_llm_prior.py` | `6350BBAECB81` | 13423 | 2026-08-30 04:56:13 | 执行体 |
| `run_v17_fixed_sampler.py` | `3E54797EEDEB` | 10435 | 2026-08-23 21:38:54 | 执行体 |
| `run_v17_fusion_fix.py` | `B592470C47AE` | 10236 | 2026-08-23 21:31:25 | 执行体 |
| `run_v17_multigraph.py` | `CA7E6031272C` | 5682 | 2026-08-23 21:33:45 | 执行体 |
| `run_v18_api_supplements.py` | `AEF28D92D763` | 42681 | 2026-08-23 23:19:13 | 执行体 |
| `run_v19_benchmark_fixes.py` | `674C2E5349CF` | 22802 | 2026-08-24 01:10:53 | 执行体 |
| `run_v19_fullrank.py` | `8D1067E4E27B` | 8976 | 2026-08-30 04:56:31 | 执行体 |
| `run_v19_meanfield.py` | `67EF3779478A` | 11690 | 2026-08-30 04:56:31 | 执行体 |
| `run_v19_quickwins.py` | `93958A96B19A` | 10509 | 2026-08-24 01:07:34 | 执行体 |
| `run_v20_baselines.py` | `1B9815FAD7CA` | 12435 | 2026-08-29 01:14:15 | 执行体 |
| `run_v20_bigquiz_eval.py` | `1C1A82F4B48A` | 9091 | 2026-08-28 23:54:08 | 执行体 |
| `run_v20_bigquiz_fetch.py` | `F810F3A34EB2` | 7808 | 2026-08-30 10:16:33 | 执行体 |
| `run_v20_corpus_eval.py` | `2FAD3B28D34C` | 20470 | 2026-08-28 17:41:03 | 执行体 |
| `run_v20_cot_fetch.py` | `B4A214C4E50F` | 3323 | 2026-08-30 10:14:35 | 执行体 |
| `run_v20_crossval_eval.py` | `1CDC6C37B236` | 14379 | 2026-08-28 20:26:46 | 执行体 |
| `run_v20_crossval_fetch.py` | `3465B43E2F8A` | 4958 | 2026-08-30 10:15:16 | 执行体 |
| `run_v20_familyL_fetch.py` | `FF38DBB3DE7F` | 2088 | 2026-08-30 10:14:03 | 执行体 |
| `run_v20_familyL_ingest.py` | `C5D96C1F0522` | 6108 | 2026-08-29 01:14:15 | 执行体 |
| `run_v20_fastcheck.py` | `B6585A30D808` | 7243 | 2026-08-28 22:07:04 | 核查＋执行体 |
| `run_v20_gt.py` | `9F6DF7E94CDC` | 9824 | 2026-08-28 17:14:47 | 执行体 |
| `run_v20_gt2b.py` | `361AFF516219` | 9076 | 2026-08-29 19:57:30 | 执行体 |
| `run_v20_gt3_eval.py` | `6A234EEE29B3` | 6983 | 2026-08-29 15:02:33 | 执行体 |
| `run_v20_gt3_fetch.py` | `1853F7E82A3A` | 3858 | 2026-08-30 10:11:34 | 执行体 |
| `run_v20_gt3b_fetch.py` | `EFAA93762269` | 3135 | 2026-08-30 10:12:06 | 执行体 |
| `run_v20_gt3c_fetch.py` | `48B659B95984` | 3193 | 2026-08-30 10:13:37 | 执行体 |
| `run_v20_gt5.py` | `32C03F5739D7` | 14957 | 2026-08-30 10:18:23 | 执行体 |
| `run_v20_gt5b.py` | `3B344435F4EA` | 10419 | 2026-08-30 10:19:10 | 执行体 |
| `run_v20_gt6.py` | `C5DCDB0F12E2` | 11010 | 2026-08-29 15:43:45 | 执行体 |
| `run_v20_gt7.py` | `38071308E9EF` | 17509 | 2026-08-30 10:20:37 | 执行体 |
| `run_v20_gt8.py` | `D07233229279` | 13876 | 2026-08-29 19:33:18 | 执行体 |
| `run_v20_gt8b_eval.py` | `07B74332EBC2` | 9196 | 2026-08-29 22:27:23 | 执行体 |
| `run_v20_gt8b_fetch.py` | `FCE719AD054D` | 6558 | 2026-08-30 10:34:04 | 执行体 |
| `run_v20_gt8b_ingest.py` | `5E3DB6F4869D` | 5676 | 2026-08-29 22:24:05 | 执行体 |
| `run_v20_gt8c_eval.py` | `6D6DB8BDBB06` | 9594 | 2026-08-30 15:52:41 | 执行体 |
| `run_v20_gt8c_fetch.py` | `8079A5DBE251` | 8068 | 2026-08-30 15:51:03 | 执行体 |
| `run_v20_gt8c_ingest.py` | `81690A38F421` | 5866 | 2026-08-30 15:51:41 | 执行体 |
| `run_v20_photonics.py` | `EC00CB18F95A` | 7615 | 2026-08-29 01:19:14 | 执行体 |
| `run_v20_quizbank.py` | `3B2A7DD2044C` | 8744 | 2026-08-28 20:46:28 | 执行体 |
| `run_v20_vector_audit.py` | `16A270A6BDAB` | 4717 | 2026-08-28 21:14:03 | 核查＋执行体 |
| `run_v21_gtformal.py` | `9BBE43F41FA8` | 16600 | 2026-08-30 15:35:54 | 执行体 |
| `run_v22_e95ci.py` | `8470E3CE8CAE` | 3058 | 2026-08-30 21:26:23 | 执行体 |
| `run_v22_p1c.py` | `6E9673205DC0` | 7236 | 2026-08-30 18:28:58 | 执行体 |
| `svg_mindmap_ingest.py` | `FA661FD759ED` | 8811 | 2026-08-23 05:00:55 | 执行体 |

### §2-17 .tmp/（草稿区・581 件 / 23,532,678 B）—— **0 逐件展开**（依 PI 令）

📌 **单列汇总如下；⛔ 0 逐件展开、0 纳入成果清单**（草稿区）。

| 项 | 实测值 |
|:--|:--|
| 件数 | **581** |
| 总 bytes | **23,532,678** |
| 最早 mtime | 2026-09-24 18:50:23 |
| 最新 mtime | 2026-10-11 23:53:15 |
| 近 72h 变动件 | **330** |
| BOM 件 | 113 |
| CR>0 件 | 188 |
| 扩展名分布 | .py 409 ／ .txt 62 ／ .json 67 ／ .log 20 ／ .pyc 5 ／ 其他 18 |

📌 **`.tmp` 中「明示应入清单」之件（4 件）—— 理由：其仓内已存在 SHA-12 完全一致之孪生副本（属成果面），故 `.tmp` 侧为**影子副本**，登记以防成果清单**重复计数或漏计**：**

| `.tmp` 相对路径 | SHA-12 | bytes | 其孪生副本（仓内他处） |
|:--|:--|-:|:--|
| `.tmp\_s4_refreeze179_enumerate_probe_2026_10_09_v1_dead.py` | `169D160BA600` | 4630 | 影子副本（.tmp 侧） |
| `.tmp\_s4_refreeze179_enumerate_probe2_2026_10_09.py` | `169D160BA600` | 4630 | 影子副本（.tmp 侧） |
| `.tmp\_s5dp_five_lines_runner_third_2026_10_11.py` | `9DE3C08E3863` | 31138 | 影子副本（.tmp 侧） |
| `results\_s5doubleprime_five_lines_runner_2026_10_11.py` | `9DE3C08E3863` | 31138 | 成果面（建议以此为准） |
| `corpus\v20\by_model\kimi\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 | 成果面（建议以此为准） |
| `corpus\v20\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 | 成果面（建议以此为准） |
| `.tmp\_v16_full_decoded.txt` | `FDFE315FF54A` | 174424 | 影子副本（.tmp 侧） |
| `.tmp\_v16_tail_dump.txt` | `FDFE315FF54A` | 174424 | 影子副本（.tmp 侧） |
## §3 类别体系与冲突标注

📌 **本体系为自拟，且明示可机检**：判据 ＝ **`相对路径`（小写化）＋ `文件名` ＋ `扩展名` 三者之正则并集**。⛔ **0 语义判定**（未读件之正文以分类）。

| 标签 | 机检规则（对 `rel` 小写化后匹配） |
|:--|:--|
| 终判/裁定 | `verdict｜judgment｜ruling｜adjudication｜signoff｜finalization｜finalize` |
| 判死线/准入门 | `kill｜criterion｜threshold｜gate｜predecess｜floor` |
| 登记 | `register｜registry｜enroll｜intake｜ledger｜book` |
| 勘误 | `errata｜erratum｜correction｜restatement｜relabel｜attribution` |
| 核查 | `verif｜check｜audit｜recheck｜consistency｜recomput｜scan｜probe｜reprodu` |
| 回函 | `reply` |
| 委托 | `commission｜invitation｜request` |
| 论文/脚本文本 | `paper｜thesis｜manuscript｜abstract｜clue_book｜rescript` |
| 评审 | `review｜peer_｜literature` |
| 读数/结果 | `readings｜result｜recompute` |
| 报告 | `report` |
| 执行体 | 扩展名 ∈ `.py｜.sh｜.ps1` |
| 归属面标签 | 首级目录 ＝ `.tmp`→草稿/临时；`corpus`→语料；`verifier`→验证面；`deposon_team`→团队件面；`docs`→文档面；`letters`→委托·回函面；`results`→成果件面；`reviews`→评审面；`scripts｜tools｜tests`→工具/脚本；`attacks`→攻击/鲁棒性面；`paper`→论文面；`.mavis`→运行时面；`.trae`→第三方件面 |
| 其他/未归类 | 上列规则**全不命中**时之兜底 |

📌 **实测分布**：单一标签 **321** 件／**并列多标签（冲突面）** **2229** 件／**兜底未归类** **7** 件 ⇒ 合计 2557。📌 **冲突者 ⛔ 0 强行归一**，一律以 ＋ 并列标注于 §2 各件之「类别判定」列（可机检：以 ＋ 为分隔符切分即得全标签集）。

---

## §4 「未核得」清单（`plan.md` §四③段明文要求）

> ⛔ **凡未能实测者一律写「未核得」并注原因；0 填估值、0 填推断值。**

| # | 项 | 状态 | 原因（实测依据） |
|:-:|:--|:--|:--|
| U-01 | `_non_upload_local_archive` 之件数／bytes／mtime／目录 | **未核得** | ⛔ **禁触区**（PI 令：0 读 0 写 0 列目录）⇒ 本件**未对其作任何系统调用** |
| U-02 | `deposon-sub`／`Deposon_v1_2_0_交付包` 之**逐件** SHA-12・逐件编目 | **未核得** | PI 令「另二区仅列存在性与件数，⛔ 0 深读 0 改写」⇒ 仅取元数据（§1-1） |
| U-03 | 各件之**内容语义**（是否已成败／是否已入既有册／结论是否终局） | **未核得** | 本件仅读 元数据＋字节指纹＋编码字节，⛔ **0 深读件之正文** ⇒ §3 之类别为**名／径驱动**，非语义判定 |
| U-04 | 各件之 **git 版本谱系**（commit／branch／是否已提交） | **未核得** | 仓根非 git 仓（`Is a git repository: false`）⇒ 无谱系可核 |
| U-05 | 漂移面（§5）**之根因** | **未核得** | PI 令「⛔ 0 断言根因」⇒ 仅登记实测时点读数 |
| U-06 | T1.5 verdict 之 **55,352 B 与 52,884 B** 两读数之落点 | **未核得** | 全仓按字节精确匹配 **各 0 命中**（§5-2）⇒ 去向未决，⛔ 0 断言 |
| U-07 | 各件与既有 `closing_round` 册之**逐份对齐**结果 | **未核得** | 须读既有册内容，⛔ 0 深读（承 U-03） |
| U-08 | `corpus/v20/…` 一件 **mtime ＝ 1979-11-30 00:00:00** 之成因 | **未核得** | 实测值如实登记；⛔ 0 推断为改写/复制/归档所致 |
| U-09 | **大小写异名双副本**（如 `Foo.md` 与 `foo.md` 并存） | **实测 0 命中（且结构上不可存在）** | 本盘为 NTFS **默认大小写不敏感**文件系统 ⇒ 两件不可共存于同一目录；全仓大小写不敏感基名比对亦 **0 命中**。📌 此为**结构性结论**，非「未查到」 |
| U-10 | `.pyc`（13 件）／`__pycache__` 目录是否属成果清单应纳面 | **未核得** | 属 PI 裁（成果面之界定）⇒ 本件仅登记其存在与字节 |

---

## §5 漂移面专章（近 72 小时内 mtime 变动之件）

📌 **判据**：mtime ≥ **2026-10-09 01:53:38**（实测时点 2026-10-12 01:53:38 之前 72 小时）｜📌 **命中 851 件**（占全仓 33.3%）｜⛔ **0 断言根因、0 断言「最终」读数**。

### §5-1 按目录分布

| 目录 | 漂移件数 | 占该目录 |
|:--|-:|-:|
| .mavis/ | 0 | 0.0% |
| .tmp/ | 330 | 56.8% |
| .trae/ | 0 | 0.0% |
| attacks/ | 0 | 0.0% |
| corpus/ | 1 | 2.3% |
| deposon_team/ | 16 | 18.6% |
| docs/ | 0 | 0.0% |
| letters/ | 14 | 14.4% |
| paper/ | 0 | 0.0% |
| results/ | 489 | 36.5% |
| reviews/ | 0 | 0.0% |
| scripts/ | 0 | 0.0% |
| tests/ | 0 | 0.0% |
| tools/ | 0 | 0.0% |
| verifier/ | 0 | 0.0% |
| （顶层） | 1 | 1.4% |

### §5-2 #21（T1.5 verdict）四读数之对账 —— 📌 **只登记实测时点读数**

| 在册四读数（②段回函所警示） | 盘面按字节精确匹配 | 命中件 | SHA-12 | mtime |
|:-:|:--|:--|:--|:--|
| 29,106 B | ✅ **1 命中** | `results\_v4_supp_t1_verdict.md` | `0AD42625F333` | 2026-09-30 16:15:20 |
| 55,352 B | ❌ **0 命中（未核得・去向未决）** | — | — | — |
| 52,884 B | ❌ **0 命中（未核得・去向未决）** | — | — | — |
| 54,377 B | ✅ **1 命中** | `results\_v4_supp_t15_verdict.md` | `3CB5C2F59961` | 2026-09-30 16:15:20 |

📌 **实测时点补充登记（⛔ 0 断言何者为「最终」）**：

| 件 | SHA-12 | bytes | mtime |
|:--|:--|-:|:--|
| `results\_v4_supp_t15_verdict.md` | `3CB5C2F59961` | 54377 | 2026-09-30 16:15:20 |
| `results\_v4_supp_t15r2_verdict.md` | `963725DBD82A` | 65638 | 2026-09-30 16:15:20 |
| `results\_v4_supp_t1_verdict.md` | `0AD42625F333` | 29106 | 2026-09-30 16:15:20 |

📌 即：29,106 B 落于 **`_v4_supp_t1_verdict.md`**（**t1**，非 t15）、54,377 B 落于 **`_v4_supp_t15_verdict.md`**、另存在 **`_v4_supp_t15r2_verdict.md`**（65,638 B）；**55,352 B 与 52,884 B 于全仓 0 命中**。⛔ **0 断言四读数之对应关系、0 断言何者为最终读数、0 断言根因**——归 PI 裁。

### §5-3 漂移件全量明细（851 件）

| mtime | 相对路径 | SHA-12 | bytes |
|:--|:--|:--|-:|
| 2026-10-12 01:39:16 | `results\_stage2_trae_reply_acceptance_register_2026_10_12.md` | `CE0B5A64CFCE` | 14874 |
| 2026-10-12 01:34:23 | `deposon_team\plugins\_tdf_s4_final_2026_10_12.py` | `1DF9A5D22E42` | 2695 |
| 2026-10-12 01:34:03 | `letters\_trae_direct_fix_reply_trae_code_2026_10_12.md` | `F37EBC80D1DF` | 21379 |
| 2026-10-12 01:31:26 | `deposon_team\plugins\_tdf_s3b_2026_10_12.py` | `CCEC66BB426E` | 1229 |
| 2026-10-12 01:30:39 | `deposon_team\plugins\_tdf_s3_jumps_2026_10_12.py` | `16F7E10AC78F` | 676 |
| 2026-10-12 01:30:19 | `results\_v3_s_phrasetemplate_preexp_data\rescript_2026_09_27.md` | `D42EA1FA61F1` | 17574 |
| 2026-10-12 01:30:19 | `results\_v3_s2_executor\rescript_2026_09_27.md` | `FF0F964BE8AA` | 25151 |
| 2026-10-12 01:30:19 | `results\_v3_recheck_08c_preexp_data\rescript_2026_09_27.md` | `035AF77DB626` | 17069 |
| 2026-10-12 01:30:19 | `results\_v3_recheck_08c_preexp_data\_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | `4B7ED4D0A3E5` | 1395 |
| 2026-10-12 01:29:57 | `deposon_team\plugins\_tdf_s2_apply_2026_10_12.py` | `4BD6D16E20D7` | 10899 |
| 2026-10-12 01:26:27 | `deposon_team\plugins\_tdf_s1c_2026_10_12.py` | `D8BD9C41194A` | 7485 |
| 2026-10-12 01:24:29 | `deposon_team\plugins\_tdf_s1b_2026_10_12.py` | `BEBBA19790C0` | 8064 |
| 2026-10-12 01:23:22 | `deposon_team\plugins\_tdf_s1_2026_10_12.py` | `5F9AB0AD7BAB` | 5856 |
| 2026-10-12 01:16:25 | `letters\_commission_trae_direct_fix_2026_10_09_v0.1.md` | `C50822B41539` | 37262 |
| 2026-10-12 01:02:53 | `results\_five_stage_chain_design_reconstruction_2026_10_12.md` | `BFF2FB754564` | 12625 |
| 2026-10-12 00:53:49 | `results\_gate_one_pi_endorsement_register_2026_10_12.md` | `B09209E9C20D` | 9579 |
| 2026-10-12 00:39:06 | `results\_kd_doc1_correction_adoption_register_2026_10_11.md` | `C55770BE5E33` | 10255 |
| 2026-10-12 00:34:33 | `results\_executor_prereg_docstring_correction_2026_10_11.md` | `F7F8328C49BA` | 27721 |
| 2026-10-12 00:18:23 | `results\_gate_one_declared_adoption_register_2026_10_11.md` | `3A965362D4F4` | 12923 |
| 2026-10-12 00:11:11 | `results\_pi_card_123_adoption_and_gate_one_request_2026_10_11.md` | `0A4B752CBC56` | 13883 |
| 2026-10-12 00:08:14 | `results\_executor_prereg_vs_impl_equivalence_2026_10_11.md` | `E84CEC618659` | 20028 |
| 2026-10-12 00:05:01 | `results\_krj10_reverdict_after_r4_convergence_2026_10_11.md` | `A21915EC55A7` | 31672 |
| 2026-10-12 00:02:59 | `results\_seven_gap_closures_adoption_register_2026_10_11.md` | `AC3C41663F84` | 11960 |
| 2026-10-11 23:53:15 | `.tmp\_claude_reply_view.txt` | `54BDDF32F9DF` | 23246 |
| 2026-10-11 23:46:12 | `results\_commission_closeout_erratum_and_supplement_2026_10_11.md` | `7C102A6B4667` | 12447 |
| 2026-10-11 23:40:53 | `letters\_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | `F4DEFAE83553` | 22064 |
| 2026-10-11 23:22:31 | `results\_r4_convergence_2026_10_11.md` | `678394C47724` | 3133 |
| 2026-10-11 23:22:17 | `results\_carrier_qid_disposition_2026_10_11.md` | `7D74D5A4D81E` | 3406 |
| 2026-10-11 23:21:55 | `results\_u_r_numbering_attribution_2026_10_11.md` | `53672C23D7F9` | 5331 |
| 2026-10-11 23:19:36 | `results\_m5_eps_drift_disposition_2026_10_11.md` | `0722F25F5838` | 2736 |
| 2026-10-11 23:19:28 | `results\_r2_reference_pointer_disposition_2026_10_11.md` | `403ADEC92CE1` | 3121 |
| 2026-10-11 23:19:12 | `results\_r6_disposition_2026_10_11.md` | `CC51203FE8F5` | 3704 |
| 2026-10-11 23:19:03 | `results\_r3_wording_disposition_2026_10_11.md` | `9D381C9D95E6` | 3917 |
| 2026-10-11 22:45:36 | `results\_misformed_commission_drafts_deletion_register_2026_10_11.md` | `BBDC9C2C8028` | 7261 |
| 2026-10-11 22:27:45 | `letters\_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | `0CE066E5EB3F` | 22685 |
| 2026-10-11 22:05:39 | `results\_three_pending_items_effectivity_2026_10_11.md` | `DF1F5F75C7A0` | 16744 |
| 2026-10-11 21:55:16 | `results\_three_pending_items_drafts_2026_10_11.md` | `8995859E5A76` | 51748 |
| 2026-10-11 21:52:41 | `results\_krj5d_third_tier_effectivity_2026_10_11.md` | `062093D95C9F` | 10729 |
| 2026-10-11 21:43:15 | `results\_lim_aperiod_adoption_and_label_correction_2026_10_11.md` | `F4B129E3312F` | 14770 |
| 2026-10-11 21:38:15 | `results\_lim_aperiod_restatement_third_domain_2026_10_11.md` | `8672A5541CA8` | 27946 |
| 2026-10-11 21:35:16 | `results\_u6_negative_delta_compatibility_2026_10_11.md` | `1846E917119F` | 20969 |
| 2026-10-11 21:34:15 | `results\_krj_pi_picks_adoption_krj6_revise_2026_10_11.md` | `31E32CCC59BF` | 15214 |
| 2026-10-11 21:31:55 | `results\_u3_carrier_qid_verification_2026_10_11.md` | `6509AE68F778` | 21572 |
| 2026-10-11 21:20:35 | `results\_krj_five_verdicts_adjudication_2026_10_11.md` | `5C0EFD663847` | 16064 |
| 2026-10-11 21:12:00 | `results\_krj_all_five_verdicts_rewrite_2026_10_11.md` | `78FB8C47C944` | 72247 |
| 2026-10-11 21:06:58 | `results\_krj4_trj1_pick_and_pass_verdict_2026_10_11.md` | `FB7BB5DA85EC` | 16567 |
| 2026-10-11 20:52:41 | `results\_krj10_terminal_verdict_closure_2026_10_11.md` | `F2E8E32089B2` | 14101 |
| 2026-10-11 20:43:41 | `results\_krj4_trj1_adjudication_judgment_2026_10_11.md` | `50E91BF30E45` | 30293 |
| 2026-10-11 20:43:15 | `results\_s5prime_double_lim_a_and_item_registers_2026_10_11.md` | `9A62FB2A6956` | 58378 |
| 2026-10-11 20:41:59 | `results\_krj_cond4_bytes_erratum_2026_10_11.md` | `78A95E5561FC` | 3886 |
| 2026-10-11 20:36:49 | `results\_s5dp_mixed_object_erratum_2026_10_11.md` | `07CDE000E66F` | 8380 |
| 2026-10-11 20:32:37 | `results\_krj_cond4_effectivity_declaration_2026_10_11.md` | `F5C317F4CC96` | 15546 |
| 2026-10-11 20:32:37 | `results\__pycache__\_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc` | `9FC3E2152679` | 44952 |
| 2026-10-11 18:14:09 | `.tmp\_s5dp_run_stdout_2026_10_11.txt` | `13F90AAFAB80` | 7256 |
| 2026-10-11 18:14:08 | `results\_s5doubleprime_five_lines_readings_2026_10_11.json` | `839FB5452578` | 16099 |
| 2026-10-11 18:13:10 | `.tmp\__pycache__\_s5dp_five_lines_runner_third_2026_10_11.cpython-314.pyc` | `01A31E74A420` | 44946 |
| 2026-10-11 18:12:11 | `results\_s5doubleprime_five_lines_runner_2026_10_11.py` | `9DE3C08E3863` | 31138 |
| 2026-10-11 18:12:11 | `.tmp\_s5dp_five_lines_runner_third_2026_10_11.py` | `9DE3C08E3863` | 31138 |
| 2026-10-11 18:09:23 | `.tmp\_q_cards_2026_10_11.txt` | `181A8B249B88` | 14888 |
| 2026-10-11 17:51:02 | `results\_krj_all_terminal_verdicts_2026_10_11.md` | `F52231807E36` | 95659 |
| 2026-10-11 17:39:50 | `results\_s7doubleprime_verification_erratum_2026_10_11.md` | `9FF40693E4AC` | 32822 |
| 2026-10-11 17:38:34 | `results\_s6doubleprime_verdict_supplement_2026_10_11.md` | `8E19C10CE219` | 31515 |
| 2026-10-11 17:36:57 | `results\_c2_criterion_third_tier_draft_2026_10_11.md` | `844179898102` | 26713 |
| 2026-10-11 17:27:15 | `results\_s7doubleprime_verification_2026_10_11.md` | `06AC684B4923` | 41680 |
| 2026-10-11 17:26:24 | `results\_axis1_three_recomputations_2026_10_11.md` | `8DE23F7D7384` | 29938 |
| 2026-10-11 17:13:11 | `results\_stage3_readings_verification_2026_10_11.md` | `023A0CDD3350` | 29956 |
| 2026-10-11 17:10:58 | `results\_s6doubleprime_terminal_verdicts_2026_10_11.md` | `BBA3B889D849` | 76910 |
| 2026-10-11 16:56:23 | `results\_stage3_trigger_readings_2026_10_11.md` | `2900948BCA6D` | 35711 |
| 2026-10-11 16:56:21 | `results\_stage3_extraction_verification_2026_10_11.md` | `F973E6D737C3` | 22399 |
| 2026-10-11 16:53:47 | `results\_c8_c2_disposition_register_2026_10_11.md` | `FB816C572779` | 30956 |
| 2026-10-11 16:53:23 | `results\_g9_read_b_effectivity_register_2026_10_11.md` | `F5D601A0602A` | 29649 |
| 2026-10-11 16:52:40 | `results\_stage3_trigger_readings_items_2026_10_11.json` | `079108C62A82` | 21049 |
| 2026-10-11 16:52:24 | `results\_s4prime_readings_runner_2026_10_11.py` | `0AA414188361` | 23766 |
| 2026-10-11 16:51:05 | `results\__pycache__\_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | `F4194CC5A522` | 43685 |
| 2026-10-11 16:37:29 | `results\_j2_kj4_disposition_register_2026_10_11.md` | `C1A4FF1B96E5` | 34112 |
| 2026-10-11 16:31:27 | `results\_five_items_effectivity_register_2026_10_11.md` | `8AFFDCA64B4B` | 43332 |
| 2026-10-11 16:26:38 | `results\_stage3_trigger_recheck_2026_10_11.md` | `AEF26B8CBE50` | 49109 |
| 2026-10-11 16:22:45 | `results\_e4_lineage_conflict_correction_2026_10_11.md` | `E20B96E32F54` | 30510 |
| 2026-10-11 16:22:16 | `results\_fp3_anchor_and_krj_restrament_register_2026_10_11.md` | `B7C060AB2D49` | 32886 |
| 2026-10-11 16:08:15 | `results\_kj4_e4_unification_judgment_2026_10_11.md` | `A14D49F7D3A2` | 36839 |
| 2026-10-11 16:06:04 | `results\_five_pending_items_drafts_2026_10_11.md` | `86C46998DE63` | 55102 |
| 2026-10-11 16:03:31 | `results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `784F042BF93D` | 22646 |
| 2026-10-11 16:03:31 | `results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `5777A07C608A` | 43130 |
| 2026-10-11 16:03:09 | `results\_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068E1A7A1D04` | 52655 |
| 2026-10-11 16:03:04 | `results\_j2_identifier_coupling_judgment_2026_10_11.md` | `2FD4505FDCA2` | 34261 |
| 2026-10-11 15:42:36 | `results\_kj1_eps_ls_effectivity_register_2026_10_11.md` | `809EDB4BB1CC` | 62344 |
| 2026-10-11 15:40:48 | `results\_ftfb_order_judgment_2026_10_11.md` | `B6EEC487E9D7` | 45911 |
| 2026-10-11 15:36:15 | `results\_seed_double_identifier_finalization_2026_10_11.md` | `6904852F8CEB` | 26864 |
| 2026-10-11 15:17:29 | `results\_thv3_15_parallel_seed_double_note_2026_10_11.md` | `3CD92287059E` | 15569 |
| 2026-10-11 15:16:44 | `results\_four_items_execution_batch_2026_10_11.md` | `8006D1962E5F` | 31515 |
| 2026-10-11 15:16:12 | `results\_kj1_judgment_premise_correction_2026_10_11.md` | `003B134CCE24` | 35050 |
| 2026-10-11 15:02:43 | `results\_seed_double_identifier_final_judgment_2026_10_11.md` | `728D18391748` | 50222 |
| 2026-10-11 15:02:27 | `results\_kj1_abc_choice_judgment_2026_10_11.md` | `D02EC6B0987E` | 42083 |
| 2026-10-11 14:59:46 | `results\_kj1_sc1_premise_correction_2026_10_11.md` | `8B344B9B4715` | 31044 |
| 2026-10-11 14:59:15 | `results\_eps_ls_semantics_judgment_2026_10_11.md` | `51434449FF3B` | 31391 |
| 2026-10-11 14:44:15 | `results\_pending_pi_items_drafts_2026_10_11.md` | `55F469269D3D` | 40678 |
| 2026-10-11 14:41:24 | `results\_stage1_tail_caliber_unification_register_2026_10_11.md` | `D486EC491E8E` | 41140 |
| 2026-10-11 14:36:37 | `results\_b14_audit_f2f3_closure_register_2026_10_11.md` | `9D4A3D6DDF88` | 29620 |
| 2026-10-11 14:22:34 | `results\_pi_effectivity_declaration_register_2026_10_11.md` | `41A82BDE5190` | 54511 |
| 2026-10-11 14:21:47 | `results\_seed_double_criterion_draft_2026_10_11.md` | `025212E91546` | 40499 |
| 2026-10-11 14:05:56 | `results\_f4_direction1_domain_effectivity_2026_10_11.md` | `FD4EC7559342` | 40301 |
| 2026-10-11 14:03:16 | `results\_md_trigger_prereg_effectivity_2026_10_11.md` | `5D8CD0D1676F` | 41636 |
| 2026-10-11 14:02:53 | `results\_seed_double_rule_judgment_2026_10_11.md` | `F70A689FD8C1` | 57185 |
| 2026-10-11 13:47:15 | `results\_questionnaire_cards_intake_register_supplement_15_2026_10_11.md` | `3654C41EDA64` | 44698 |
| 2026-10-11 13:46:07 | `results\_f3_definition_deep_judgment_2026_10_11.md` | `11945E587B1D` | 42351 |
| 2026-10-11 13:38:58 | `results\_s7prime_findings_erratum_2026_10_11.md` | `A7DFA8E789B7` | 31008 |
| 2026-10-11 13:35:24 | `results\_questionnaire_cards_intake_register_supplement_14_2026_10_11.md` | `79BC4BFE38A5` | 54883 |
| 2026-10-11 13:29:50 | `results\_f4_direction1_seed_and_domain_draft_2026_10_11.md` | `F77C080D9FC6` | 33887 |
| 2026-10-11 12:59:14 | `results\_s7prime_prereq_and_verification_2026_10_11.md` | `E44DA4B83810` | 36787 |
| 2026-10-11 12:52:21 | `results\_questionnaire_cards_intake_register_supplement_13_2026_10_11.md` | `43E0B642F8B2` | 114253 |
| 2026-10-11 12:51:45 | `results\_f3_new_definition_draft_2026_10_11.md` | `7482699E8B07` | 48068 |
| 2026-10-11 12:42:20 | `results\_f4_direction1_prereq_check_2026_10_11.md` | `BB49153C311F` | 38664 |
| 2026-10-11 12:36:08 | `results\_s6prime_terminal_verdicts_2026_10_11.md` | `1C8CE58D6484` | 54937 |
| 2026-10-11 12:32:09 | `results\_register3_bytes_erratum_2026_10_11.md` | `F9F6805A7B76` | 13294 |
| 2026-10-11 12:31:21 | `results\_g11_krj4_effectivity_register_2026_10_11.md` | `17168119ECCC` | 39870 |
| 2026-10-11 12:17:37 | `results\_pending_rulings_drafts_2026_10_11.md` | `C8428B883029` | 42775 |
| 2026-10-11 01:44:40 | `results\_f3f4_exit_drafts_2026_10_11.md` | `523DC6CBDF9A` | 50427 |
| 2026-10-11 01:38:02 | `results\_s5prime_lim_a_and_item_registers_2026_10_11.md` | `FA74831FA0AD` | 47225 |
| 2026-10-11 01:37:31 | `results\_round56_review_effectivity_register_6_2026_10_11.md` | `2F3255EA344F` | 58478 |
| 2026-10-11 01:22:11 | `results\_s4prime_five_lines_readings_2026_10_11.json` | `65A9B9BE6327` | 15219 |
| 2026-10-11 01:21:28 | `results\_s4prime_five_lines_readings_2026_10_11.md` | `E91E7F52C726` | 23877 |
| 2026-10-11 01:19:53 | `results\_s4prime_five_lines_runner_2026_10_11.py` | `F784B2FC92F4` | 29813 |
| 2026-10-11 01:18:04 | `results\_g10_threshold_closed_domain_judgment_2026_10_11.md` | `586ABDA5DDF7` | 55727 |
| 2026-10-11 01:17:39 | `results\_krj5_final_disposition_verdict_2026_10_11.md` | `2B6BF509A135` | 60700 |
| 2026-10-11 01:04:02 | `results\_round56_review_effectivity_register_5_2026_10_11.md` | `5DEBA7D27BB1` | 67613 |
| 2026-10-11 01:01:21 | `results\_q2_scope_vs_revision_judgment_2026_10_11.md` | `B4F00E5A69C4` | 43195 |
| 2026-10-11 00:59:13 | `results\_s3prime_recompute_after_supplement_2026_10_11.md` | `FA025E4DC166` | 41708 |
| 2026-10-11 00:50:28 | `results\_s4_seedprime_seq_t1_only_supplement_2026_10_11.md` | `B2B044289FFE` | 24783 |
| 2026-10-11 00:50:28 | `results\_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | `A834E0E7121A` | 28030 |
| 2026-10-11 00:50:21 | `.tmp\_s4_seedprime_seq_t1_supplement_2026_10_11.py` | `3A9DB2126E4F` | 31705 |
| 2026-10-11 00:47:58 | `results\_krj5_subject_scope_judgment_2026_10_11.md` | `AE9DF5119861` | 45372 |
| 2026-10-11 00:29:00 | `results\_s3prime_alert_disposition_judgment_2026_10_11.md` | `E7FCBC290A7E` | 53188 |
| 2026-10-11 00:26:46 | `results\_c_component4_three_items_judgment_2026_10_11.md` | `FD0094E2F865` | 41580 |
| 2026-10-11 00:23:15 | `results\_round56_review_effectivity_register_4_2026_10_11.md` | `EE31BB8A94FE` | 46908 |
| 2026-10-11 00:15:56 | `results\_s3prime_degeneracy_selfcert_2026_10_11.md` | `E4D96A516289` | 39939 |
| 2026-10-11 00:15:45 | `results\_c_component4_d2d3_gap_judgment_2026_10_11.md` | `08D3BFD82235` | 27490 |
| 2026-10-11 00:15:40 | `results\_vk_face_category_erratum_2026_10_11.md` | `67BF70301889` | 17373 |
| 2026-10-11 00:14:37 | `results\_b01_recompute_authorization_supplement_2026_10_11.md` | `03A66D4C663A` | 18454 |
| 2026-10-11 00:12:10 | `results\_trigger_denominator_caliber_judgment_2026_10_11.md` | `16BF9332DEEF` | 43448 |
| 2026-10-11 00:07:21 | `results\_b14_vk_evidence_audit_2026_10_10.md` | `89F17297F1F5` | 33586 |
| 2026-10-11 00:02:57 | `results\_s2prime_krj3_applicability_recheck_2026_10_10.md` | `10518510B628` | 41322 |
| 2026-10-10 23:55:57 | `results\_questionnaire_cards_intake_register_supplement_12_2026_10_10.md` | `1FF6919967A7` | 121137 |
| 2026-10-10 23:51:48 | `results\_s1prime_trigger_caliber_reevaluation_2026_10_10.md` | `D2326973AAF8` | 29991 |
| 2026-10-10 23:50:47 | `results\_round56_review_effectivity_register_3_2026_10_10.md` | `84ED13256250` | 77181 |
| 2026-10-10 23:35:41 | `results\_chd_construction_domain_declaration_draft_2026_10_10.md` | `17CF0D59CD7B` | 34948 |
| 2026-10-10 23:32:32 | `results\_typeb_m_registration_2026_10_10.md` | `3B68D3890473` | 27778 |
| 2026-10-10 23:30:49 | `results\_u_cf_reclassification_2026_10_10.md` | `02F910E8795B` | 25698 |
| 2026-10-10 23:30:45 | `results\_typeb_m_caliber_2026_10_10.md` | `4D067A884C6C` | 32830 |
| 2026-10-10 23:29:45 | `results\_u_cf_category_caliber_2026_10_10.md` | `73F181D76169` | 18976 |
| 2026-10-10 23:21:06 | `results\_s4_heldout_seedprime_verification_2026_10_10.md` | `8C64314D0EC0` | 21966 |
| 2026-10-10 23:20:20 | `results\_s4_seedprime_inheldout_recompute_2026_10_10.md` | `CF3368E7D5A0` | 21866 |
| 2026-10-10 23:15:39 | `results\_typeb_m_definition_judgment_2026_10_10.md` | `97AC7FCC4803` | 41432 |
| 2026-10-10 23:13:30 | `results\_b01_new_key_residue_judgment_2026_10_10.md` | `345517455DCF` | 41984 |
| 2026-10-10 23:12:55 | `results\_p_refresh_scope_judgment_2026_10_10.md` | `44E98DC31E2B` | 34004 |
| 2026-10-10 23:07:39 | `results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `6CBB8BA01BFB` | 15409 |
| 2026-10-10 23:07:07 | `results\_s4_heldout_sampling_seedprime_items_register_2026_10_10.md` | `9DA183328F18` | 24690 |
| 2026-10-10 21:59:20 | `results\_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1BF6F47A590D` | 18923 |
| 2026-10-10 21:56:34 | `results\_p_refresh_registration_preliminary_2026_10_10.md` | `A3E14B508A4A` | 32780 |
| 2026-10-10 21:37:33 | `results\_round56_registration_supplement_2026_10_10.md` | `71A59735302C` | 21865 |
| 2026-10-10 21:36:54 | `results\_round56_review_effectivity_register_2026_10_10.md` | `DA6B55162E50` | 49013 |
| 2026-10-10 21:35:11 | `results\_vk_current_counting_face_2026_10_10.md` | `4D4E41C3EFF5` | 24795 |
| 2026-10-10 21:33:26 | `results\_b01_recompute_sec4_2_erratum_2026_10_10.md` | `FAC3308FB295` | 16441 |
| 2026-10-10 21:31:57 | `results\_b01_new_key_classification_2026_10_10.md` | `2DDFECF6201C` | 38669 |
| 2026-10-10 21:28:04 | `results\_p_refresh_s0_judgment_2026_10_10.md` | `369173063A7C` | 41449 |
| 2026-10-10 21:28:00 | `results\_zero_reading_judgment_2026_10_10.md` | `A9947F5677DF` | 27824 |
| 2026-10-10 21:24:40 | `results\_round56_typeb_backfill_register_2026_10_10.md` | `607DED06D840` | 40253 |
| 2026-10-10 21:21:41 | `letters\查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | `8BAA9854B3F7` | 239700 |
| 2026-10-10 21:20:30 | `results\_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md` | `4C369CB86DB4` | 31607 |
| 2026-10-10 21:19:00 | `results\_c4_reply_intake_acceptance_register_2026_10_01.md` | `E1E8CB7B9DB4` | 33728 |
| 2026-10-10 20:29:17 | `results\_round56_b01_followup_disposition_plan_2026_10_10.md` | `857FB940A43C` | 31004 |
| 2026-10-10 20:19:27 | `results\_questionnaire_cards_intake_register_supplement_11_2026_10_10.md` | `52C97D1C11E9` | 55341 |
| 2026-10-10 20:18:55 | `$null` | `400D7E27B03F` | 898 |
| 2026-10-10 20:18:30 | `results\_round56_typeb_form_draft_2026_10_10.md` | `582C5FB9970C` | 50170 |
| 2026-10-10 20:17:54 | `results\_zero_consumption_cells_field_correction_2026_10_10.md` | `36F9AC4EBBF6` | 12244 |
| 2026-10-10 20:15:55 | `results\_round56_direct_adoptions_register_2_2026_10_10.md` | `F8E0FA28C067` | 26690 |
| 2026-10-10 20:00:44 | `results\_b01_p_counting_recompute_2026_10_10.md` | `3511CF21A869` | 22104 |
| 2026-10-10 19:57:04 | `results\_round56r9r10_dispositions_register_2026_10_10.md` | `0EB408AE60F5` | 49754 |
| 2026-10-10 19:55:36 | `results\_krj9_scope_clarification_draft_2026_10_10.md` | `B17B3C38EC21` | 28654 |
| 2026-10-10 19:55:10 | `results\_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | `C72086990450` | 8181 |
| 2026-10-10 19:44:53 | `results\_phase1_completion_judgment_2026_10_10.md` | `6049C68F027B` | 28836 |
| 2026-10-10 19:37:42 | `.tmp\_vk_q8.py` | `5A81E5558C72` | 1025 |
| 2026-10-10 19:37:27 | `.tmp\_vk_q7.py` | `A6C525F88F11` | 1331 |
| 2026-10-10 19:27:46 | `results\_round56_idx_sc1_resolution_2026_10_10.md` | `9B41F2A38B2F` | 47107 |
| 2026-10-10 19:15:26 | `results\_g5_ccp_seed_designation_revision_2026_10_10.md` | `B53F40ABB90B` | 20979 |
| 2026-10-10 19:13:12 | `results\_round56_g2_enable_and_v1_rule_register_2026_10_10.md` | `936F551F0FD3` | 34181 |
| 2026-10-10 19:12:12 | `results\_round56_v4_kd_row_correction_revision_2026_10_10.md` | `6D8537CB127F` | 23453 |
| 2026-10-10 19:11:29 | `results\_round56_gu_backdoor_exclusion_revision_2026_10_10.md` | `52D3B10A16A0` | 25045 |
| 2026-10-10 19:09:19 | `results\_questionnaire_cards_intake_register_supplement_10_2026_10_10.md` | `6C18D336E018` | 84127 |
| 2026-10-10 19:08:08 | `results\_round56_typeb_implementation_register_2026_10_10.md` | `C296A7833A70` | 26367 |
| 2026-10-10 19:07:14 | `results\_round56_shortname_backfill_note_2026_10_10.md` | `BB2444CCCD65` | 22195 |
| 2026-10-10 19:06:22 | `results\_round56_direct_adoptions_register_2026_10_10.md` | `E3C56C5D0A97` | 43240 |
| 2026-10-10 19:05:07 | `results\_g5_ccp_p0_verification_2026_10_10.md` | `8C7693379496` | 24819 |
| 2026-10-10 19:05:04 | `results\_round56c_card_id_erratum_2026_10_10.md` | `F6C2D40F18FF` | 18747 |
| 2026-10-10 18:57:58 | `results\_round56r8_dispositions_register_2026_10_10.md` | `CFB08D0E15F4` | 46135 |
| 2026-10-10 18:55:53 | `results\_questionnaire_cards_intake_register_supplement_9_2026_10_10.md` | `B6C0B4F29152` | 84422 |
| 2026-10-10 18:52:37 | `results\_g5_ccp_execution_prereqs_2026_10_10.md` | `AB1A07AE2FD1` | 32815 |
| 2026-10-10 18:50:57 | `results\_round56_th4_two_field_reporting_resolution_2026_10_10.md` | `71894A686E92` | 28233 |
| 2026-10-10 18:49:59 | `results\_round56_th3_coverage_line_effectivity_register_2026_10_10.md` | `6794FB09CE7E` | 28378 |
| 2026-10-10 18:49:02 | `results\_round56_n10_erratum_register_2026_10_10.md` | `599D0450434E` | 20321 |
| 2026-10-10 18:48:25 | `results\_round56_terminal_boundary_effectivity_register_2026_10_10.md` | `D5BF826278CB` | 35878 |
| 2026-10-10 18:44:20 | `results\_u5b_p_counting_resolution_2026_10_10.md` | `E12E9D9A32C4` | 20086 |
| 2026-10-10 18:41:15 | `results\_trj_w1_downstream_erratum_2026_10_10.md` | `E52D0016FBC6` | 24888 |
| 2026-10-10 18:40:34 | `results\_a02_excluded_items_idx_collection_2026_10_10.md` | `03407E0B6662` | 39565 |
| 2026-10-10 18:40:21 | `results\_round56_pending_questions_compilation_supplement_note_2026_10_10.md` | `421C936F6AE8` | 29019 |
| 2026-10-10 18:36:42 | `results\_round56c_d23_ad5_judgment_2026_10_10.md` | `061813859345` | 50747 |
| 2026-10-10 18:34:36 | `results\_g5_krj9_denominator_reconciliation_judgment_2026_10_10.md` | `22D90F12D605` | 45207 |
| 2026-10-10 18:33:08 | `results\_trj_w1_verification_2026_10_10.md` | `CC6DE8E981F6` | 23014 |
| 2026-10-10 18:33:00 | `results\_round56a_dispositions_register_2026_10_10.md` | `D8980CFAE7F7` | 50365 |
| 2026-10-10 18:29:03 | `results\_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md` | `C3117773AB36` | 33976 |
| 2026-10-10 18:22:43 | `results\_g5_rejudgment_construction_change_plan_2026_10_10.md` | `FA0001A6DD0A` | 57004 |
| 2026-10-10 18:18:42 | `results\_c4_math_corrections_downstream_erratum_2026_10_10.md` | `643CB9E249F7` | 28886 |
| 2026-10-10 18:17:26 | `results\_round56_pending_questions_compilation_2026_10_10.md` | `EF09B3D28A0F` | 33504 |
| 2026-10-10 18:13:35 | `results\_codex_c4_unblock_reply_adoption_register_2026_10_10.md` | `B979E78562A9` | 22895 |
| 2026-10-10 18:13:09 | `results\_c4_unblock_reply_independent_review_2026_10_10.md` | `2ECD866E2468` | 27364 |
| 2026-10-10 18:12:53 | `results\_round55_dispositions_register_2026_10_10.md` | `002FA0A9A5E4` | 34913 |
| 2026-10-10 18:12:36 | `results\_round56_ad8fix_effectivity_register_2026_10_10.md` | `2E7F86314428` | 16553 |
| 2026-10-10 18:11:58 | `results\_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md` | `AF4C3335538A` | 16640 |
| 2026-10-10 18:06:56 | `results\_codex_c4_values_unblock_reply_intake_register_2026_10_10.md` | `A2D7F86D72E5` | 27100 |
| 2026-10-10 17:59:21 | `results\_e6_th_v3_19_residual_exits_judgment_2026_10_10.md` | `442D5FF4ACDB` | 46261 |
| 2026-10-10 17:56:29 | `results\_s4_source_wave_mapping_registration_2026_10_10.md` | `26C8278E3552` | 38231 |
| 2026-10-10 17:51:27 | `results\_questionnaire_cards_intake_register_supplement_8_2026_10_10.md` | `29B30D845841` | 50790 |
| 2026-10-10 17:50:47 | `results\_s4_corpus_scope_hard_constraint_judgment_2026_10_10.md` | `C7609657DFE4` | 44199 |
| 2026-10-10 17:47:40 | `results\_g5_rejudgment_construction_question_judgment_2026_10_10.md` | `EE660515D9E3` | 59309 |
| 2026-10-10 17:42:45 | `results\_round54_g5_dispositions_register_2026_10_10.md` | `AFC67818BB85` | 39977 |
| 2026-10-10 17:35:08 | `letters\_codex_c4_values_unblock_reply_2026_10_10.md` | `A975C7990CD8` | 21486 |
| 2026-10-10 17:30:17 | `letters\verify_c4_originated_math.py` | `3042CF59448E` | 4115 |
| 2026-10-10 17:17:46 | `letters\_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md` | `1C769E28F8F5` | 3139 |
| 2026-10-10 17:17:35 | `letters\_commission_c4_values_unblock_EN_2026_10_10.md` | `FDE64A863B09` | 10244 |
| 2026-10-10 17:12:50 | `results\_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `A651F76A6547` | 17517 |
| 2026-10-10 17:12:00 | `results\_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md` | `16C31894D445` | 48727 |
| 2026-10-10 17:11:26 | `results\_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md` | `4C3A6DC0070D` | 20023 |
| 2026-10-10 17:10:04 | `results\_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md` | `B27814792394` | 25637 |
| 2026-10-10 17:09:46 | `results\_g5_rejudgment_c_applicability_recheck_2026_10_10.md` | `15301B3025FA` | 49051 |
| 2026-10-10 17:05:56 | `results\_codex_c4_values_followup_reply_intake_register_2026_10_10.md` | `C46D073589CF` | 24240 |
| 2026-10-10 16:42:53 | `results\_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `1FB8EAC82781` | 52602 |
| 2026-10-10 16:34:00 | `results\_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md` | `E861C7BC19AD` | 21788 |
| 2026-10-10 16:31:38 | `results\_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md` | `DEBD88FC150C` | 45351 |
| 2026-10-10 16:06:18 | `results\_u5b_citation_surface_revision_2026_10_10.md` | `5CC29C53A422` | 50079 |
| 2026-10-10 16:04:24 | `results\_round51_effectivity_register_2026_10_10.md` | `B8B0C52296B2` | 27070 |
| 2026-10-10 16:04:10 | `results\_g5_rejudgment_face_prereg_2026_10_10.md` | `04495EF4B343` | 35097 |
| 2026-10-10 16:02:26 | `letters\_codex_c4_values_followup_reply_2026_10_10.md` | `97A35F8AE94C` | 4490 |
| 2026-10-10 15:44:56 | `results\_s4_e4b_ad5_type_separate_judgment_2026_10_10.md` | `F48601FEE958` | 51898 |
| 2026-10-10 15:36:26 | `results\_s4_w2bc_effect_registration_2026_10_10.md` | `B24A8411A260` | 26418 |
| 2026-10-10 15:25:42 | `results\_give_up_n10_erratum_2026_10_10.md` | `E0DB6B819138` | 22021 |
| 2026-10-10 15:25:33 | `results\_u5_fingerprint_relocation_erratum_2026_10_10.md` | `200C7E4C57CB` | 24999 |
| 2026-10-10 15:22:33 | `results\_n01_n08_revision_2026_10_10.md` | `FA8400D8AE70` | 26628 |
| 2026-10-10 15:17:28 | `results\_g5_seg3_tie_veto_judgment_2026_10_10.md` | `3306D1FD020D` | 35983 |
| 2026-10-10 15:13:34 | `results\_e6_th_v3_19_alignment_register_2026_10_10.md` | `622CEBEF2C9F` | 32582 |
| 2026-10-10 15:11:57 | `results\_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md` | `0984955B0370` | 11752 |
| 2026-10-10 15:11:50 | `.tmp\_build_receipt_supplement_6.py` | `BBC6B3E20B92` | 11369 |
| 2026-10-10 15:10:47 | `.tmp\_crosscheck_messages_35_48.py` | `DCFE48359488` | 1608 |
| 2026-10-10 15:10:32 | `.tmp\_verify_intake_supplement_6.py` | `1FBB1BD1DB6C` | 3678 |
| 2026-10-10 15:09:57 | `results\_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | `95BA771FA760` | 106453 |
| 2026-10-10 15:09:46 | `.tmp\_append_intake_supplement_6_tail.py` | `C3339682D68C` | 9335 |
| 2026-10-10 15:09:02 | `.tmp\_build_intake_supplement_6.py` | `6336456853AE` | 13094 |
| 2026-10-10 15:07:59 | `.tmp\_cards_35_48_full.txt` | `8D99789C1999` | 120330 |
| 2026-10-10 15:07:41 | `.tmp\_intake_cards_35_48_extract.py` | `74CCA5BDA270` | 3416 |
| 2026-10-10 15:05:02 | `results\_s4_e4_axis_disposition_axis2_run_2026_10_10.md` | `2BDA07AF86FC` | 29700 |
| 2026-10-10 15:04:30 | `results\_s4_v11_axis2_displacement_items_2026_10_10.json` | `0EED9053619C` | 9941 |
| 2026-10-10 15:03:20 | `results\_e6_alt_permp_comparability_closure_2026_10_10.md` | `1C663430B4AA` | 16636 |
| 2026-10-10 15:02:56 | `results\_e6_n_distinct_judge_types_recompute_2026_10_10.md` | `82C5C143134E` | 26304 |
| 2026-10-10 15:02:27 | `.tmp\e4_axis2_hit_unchanged_probe_2026_10_10.py` | `FC5D6BDE78AD` | 2629 |
| 2026-10-10 15:02:17 | `.tmp\_e6_alt_permp_closure_analysis_2026_10_10.py` | `AFFABEF74DE4` | 2736 |
| 2026-10-10 15:01:15 | `.tmp\e4_axis2_validation_out.json` | `5B3EF39DC114` | 2657 |
| 2026-10-10 15:01:06 | `.tmp\e4_axis2_final_validation_2026_10_10.py` | `8D2211F8AC91` | 6489 |
| 2026-10-10 15:00:40 | `.tmp\_e6_alt_permp_closure_raw_2026_10_10.json` | `C48395E135FD` | 8345 |
| 2026-10-10 15:00:27 | `.tmp\e4_axis2_crosscheck_2026_10_10.py` | `FBF93A534B99` | 3607 |
| 2026-10-10 15:00:04 | `.tmp\e4_axis2_denominator_recheck_2026_10_10.py` | `5944EFD3B68E` | 3833 |
| 2026-10-10 14:59:42 | `.tmp\_e6_alt_permp_closure_runner_2026_10_10.py` | `9BB254AA58A9` | 9985 |
| 2026-10-10 14:59:39 | `.tmp\e4_axis2_run_out.json` | `536080B19999` | 3514 |
| 2026-10-10 14:59:32 | `.tmp\e4_axis2_v11_displacement_run_2026_10_10.py` | `A950AE064FDE` | 10617 |
| 2026-10-10 14:59:14 | `.tmp\_e6_ndjt_recompute_out_2026_10_10.json` | `6499760993BF` | 7005 |
| 2026-10-10 14:59:02 | `results\_s4_w2_disposition_registration_2026_10_10.md` | `566C2F0AD7E8` | 23545 |
| 2026-10-10 14:58:57 | `.tmp\_e6_ndjt_recompute_2026_10_10.py` | `59C2D618305F` | 5064 |
| 2026-10-10 14:44:36 | `results\_three_state_standard_repeal_register_2026_10_10.md` | `8503708C73BF` | 18364 |
| 2026-10-10 14:44:04 | `results\_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md` | `3015F2481DF1` | 33880 |
| 2026-10-10 14:42:11 | `results\_s4_v31_exec_section8_errata_2026_10_10.md` | `EC11AEC2380D` | 23250 |
| 2026-10-10 14:36:06 | `results\_s4_w2_e4_separate_judgment_2026_10_10.md` | `A51BD6530075` | 37607 |
| 2026-10-10 14:31:49 | `letters\_commission_c4_values_followup_EN_2026_10_10.md` | `ABE0652AB00F` | 7583 |
| 2026-10-10 14:15:28 | `results\_s4_w1_3636_consistency_check_2026_10_10.md` | `0E9AE4B6EE8C` | 29196 |
| 2026-10-10 14:11:43 | `results\_round45_dispositions_effect_register_2026_10_10.md` | `D66A1076952A` | 19803 |
| 2026-10-10 14:09:06 | `results\_codex_c4_values_reply_intake_register_2026_10_10.md` | `8F1D27A02833` | 12926 |
| 2026-10-10 14:02:11 | `results\_g5_displacement_threshold_draft_2026_10_10.md` | `7C8107D9A8FB` | 25619 |
| 2026-10-10 13:59:18 | `results\_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | `EDB57308170D` | 77189 |
| 2026-10-10 13:57:19 | `results\_s4_v31_displacement_register_face2_2026_10_10.md` | `B6CE4A79116E` | 17736 |
| 2026-10-10 13:56:56 | `results\_kd_login_register_section65_correction_2026_10_10.md` | `316D14C137BB` | 20422 |
| 2026-10-10 13:56:41 | `results\_s4_v31_drift_register_face1_2026_10_10.md` | `5AB168D82873` | 11485 |
| 2026-10-10 13:56:13 | `results\_s4_v31_readings_summary_2026_10_10.json` | `882A1B3DEB0B` | 5569 |
| 2026-10-10 13:56:13 | `results\_s4_v31_displacement_items_2026_10_10.json` | `6F020C03E52C` | 36822 |
| 2026-10-10 13:56:04 | `.tmp\write_summary_json.py` | `6214AD3CDC2D` | 9049 |
| 2026-10-10 13:55:46 | `results\_s4_v31_readings_execution_2026_10_10.md` | `80D765F34163` | 21467 |
| 2026-10-10 13:54:57 | `results\_s4_v31_regen_gold_items_2026_10_10.json` | `4125CB2DF92B` | 36830 |
| 2026-10-10 13:54:45 | `.tmp\write_items_json.py` | `9DCE7986E20D` | 4388 |
| 2026-10-10 13:54:32 | `results\_s4_v31_regen_gold_register_2026_10_10.md` | `9C9D8E8ECC72` | 27133 |
| 2026-10-10 13:52:29 | `.tmp\tables.py` | `02CC157B6D69` | 1818 |
| 2026-10-10 13:52:04 | `.tmp\_payload.json` | `BE0A4F54AADE` | 42672 |
| 2026-10-10 13:51:46 | `.tmp\prep.py` | `E401C8E50F93` | 4091 |
| 2026-10-10 13:50:16 | `.tmp\singlevar.py` | `F0BBA43AF3E5` | 1515 |
| 2026-10-10 13:49:44 | `results\_u2u3_effectivity_register_2026_10_10.md` | `B00B87CEC825` | 27192 |
| 2026-10-10 13:49:24 | `letters\_codex_c4_values_reply_2026_10_10.md` | `8E4972352291` | 13378 |
| 2026-10-10 13:49:20 | `.tmp\pool_search.py` | `3245AF3F3BBB` | 2127 |
| 2026-10-10 13:48:55 | `.tmp\scope_scan.py` | `07349ACFE90F` | 3380 |
| 2026-10-10 13:47:39 | `.tmp\diffcause.py` | `2B24513CDF74` | 2724 |
| 2026-10-10 13:45:25 | `.tmp\_disp.json` | `076648DE25FF` | 3484 |
| 2026-10-10 13:45:15 | `.tmp\run_steps.py` | `019F8405D4CF` | 2756 |
| 2026-10-10 13:44:11 | `.tmp\__pycache__\s4_regen_runner.cpython-314.pyc` | `31DD999DF336` | 21608 |
| 2026-10-10 13:43:59 | `.tmp\s4_regen_runner.py` | `70467364BDB1` | 13040 |
| 2026-10-10 13:36:11 | `results\_e6_verdict_v3_rationale_review_2026_10_10.md` | `664E82968FC2` | 39008 |
| 2026-10-10 13:34:44 | `results\_e6_j5_semantics_erratum_note_2026_10_10.md` | `B2DB427147E2` | 21166 |
| 2026-10-10 13:33:31 | `results\_s4_regen_golive_clearance_2026_10_10.md` | `80D8905B9762` | 27436 |
| 2026-10-10 13:32:32 | `results\_b_coincidence_closeout_register_2026_10_10.md` | `51CE7B49C423` | 31451 |
| 2026-10-10 13:26:05 | `results\_give_up_semantics_draft_2026_10_10.md` | `B6A4AE82E038` | 23497 |
| 2026-10-10 13:24:57 | `results\_af_entity_definition_draft_2026_10_10.md` | `97654060D86E` | 25257 |
| 2026-10-10 13:21:16 | `results\_kd04_c_denominator_closeout_register_2026_10_10.md` | `78481CC60494` | 23029 |
| 2026-10-10 13:20:41 | `results\_s4q04_level_attribution_judgment_2026_10_10.md` | `49A07216A1BB` | 26407 |
| 2026-10-10 13:17:14 | `results\_b_coincidence_disposition_judgment_2026_10_10.md` | `7FF80485955C` | 42838 |
| 2026-10-10 13:15:32 | `letters\_commission_c4_values_EN_differences_exits_note_2026_10_10.md` | `B20F25A66267` | 7817 |
| 2026-10-10 13:14:46 | `letters\_commission_c4_values_EN_2026_10_10.md` | `A397621085D6` | 56217 |
| 2026-10-10 13:13:46 | `results\_e6_j5_semantics_conflict_judgment_2026_10_10.md` | `3C7628A4964D` | 27682 |
| 2026-10-10 13:05:11 | `results\_s4_vclause_1_6_revision_2026_10_10.md` | `017B3CF38AE3` | 14900 |
| 2026-10-10 13:04:40 | `results\_s4_execution_sequence_review_2026_10_10.md` | `0E1EB2FDD25E` | 19158 |
| 2026-10-10 13:03:55 | `results\_s4_kex_killline_freeze_2026_10_10.md` | `6269D0C6FD10` | 15284 |
| 2026-10-10 13:03:50 | `results\_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md` | `19AD36F7EC84` | 25123 |
| 2026-10-10 13:03:25 | `results\_s4_v31_keyword_table_final_2026_10_10.md` | `1B7BCBCCE589` | 23270 |
| 2026-10-10 12:53:23 | `results\_e6_case_a_judgment_face_promotion_2026_10_10.md` | `4E65C53F68E8` | 42116 |
| 2026-10-10 12:43:54 | `results\_d05_three_checks_readings_recheck_confirm_2026_10_10.md` | `DCF9F5CFA2DB` | 20044 |
| 2026-10-10 12:43:01 | `.tmp\_d05_s4only_out_2026_10_10.json` | `FA0907234347` | 427 |
| 2026-10-10 12:42:55 | `.tmp\_d05_s4only_2026_10_10.py` | `802069E2C06E` | 3438 |
| 2026-10-10 12:42:30 | `.tmp\_d05_caliber_out_2026_10_10.json` | `080606669599` | 1725 |
| 2026-10-10 12:42:22 | `.tmp\_d05_caliber_2026_10_10.py` | `65CB84529CB2` | 8011 |
| 2026-10-10 12:41:33 | `.tmp\_d05_three_checks_recheck_out_2026_10_10.json` | `4EB425260682` | 3622 |
| 2026-10-10 12:41:16 | `.tmp\_d05_three_checks_recheck_2026_10_10.py` | `FC1201CB71E7` | 11134 |
| 2026-10-10 12:28:00 | `results\_five_terminal_judgments_ruling_2026_10_10.md` | `9E96D0A1BA12` | 27315 |
| 2026-10-10 12:27:42 | `results\_s4_abcreadings_reproducibility_check_2026_10_10.md` | `892E5DFE3ED1` | 25234 |
| 2026-10-10 12:26:47 | `.tmp\_abc_final_2026_10_10.json` | `5F4C2F499620` | 1291 |
| 2026-10-10 12:26:39 | `.tmp\_abc_final_2026_10_10.py` | `15B4DE4FDFF6` | 7329 |
| 2026-10-10 12:26:11 | `.tmp\_abc_rfd_2026_10_10.py` | `39268CA6ADFF` | 5938 |
| 2026-10-10 12:25:38 | `.tmp\__pycache__\_abc_readings_reprocheck_2026_10_10.cpython-314.pyc` | `18EF2E6B1FEF` | 15886 |
| 2026-10-10 12:25:38 | `.tmp\_abc_h1h2_out_2026_10_10.json` | `068BE36A60D8` | 4922 |
| 2026-10-10 12:25:31 | `.tmp\_abc_h1h2_2026_10_10.py` | `16F19BAD301F` | 7889 |
| 2026-10-10 12:23:35 | `.tmp\_abc_diff_2026_10_10.py` | `6D6733F0E5C2` | 6620 |
| 2026-10-10 12:23:28 | `.tmp\five_terminal_classify_2026_10_10.json` | `9E04C58572BD` | 188834 |
| 2026-10-10 12:23:20 | `.tmp\scan_classify_five_terminal_2026_10_10.py` | `0B9B59083534` | 7603 |
| 2026-10-10 12:23:11 | `.tmp\_abc_readings_reprocheck_out_2026_10_10.json` | `2F9AA16B63CA` | 78436 |
| 2026-10-10 12:23:04 | `.tmp\_abc_readings_reprocheck_2026_10_10.py` | `0EC2A2BF3BAB` | 9491 |
| 2026-10-10 12:22:44 | `.tmp\five_terminal_supplement_2026_10_10.json` | `B664C3BAEB75` | 17614 |
| 2026-10-10 12:22:25 | `.tmp\scan_supplement_five_terminal_2026_10_10.py` | `7C0A6D022104` | 6010 |
| 2026-10-10 12:21:59 | `.tmp\five_terminal_domain_2026_10_10.json` | `1EFE7E458AB1` | 192600 |
| 2026-10-10 12:21:53 | `.tmp\scan_domain_five_terminal_2026_10_10.py` | `732489DC3DBD` | 2243 |
| 2026-10-10 12:21:44 | `.tmp\five_terminal_scan_2026_10_10.json` | `5196B75B95B6` | 126177 |
| 2026-10-10 12:21:36 | `.tmp\scan_five_terminal_2026_10_10.py` | `7200487FDAB1` | 4319 |
| 2026-10-10 12:10:50 | `results\_d05_b_coincidence_checks_exec_2026_10_10.md` | `840FBF08CAF4` | 21061 |
| 2026-10-10 12:08:56 | `.tmp\_d05_detail.txt` | `6CB5D73BD8DA` | 3017 |
| 2026-10-10 12:08:44 | `.tmp\_d05_summary.json` | `12655F3523C4` | 1144 |
| 2026-10-10 12:08:44 | `results\_d05_b_coincidence_checks_exec_readings_2026_10_10.json` | `586C435D1F15` | 13960 |
| 2026-10-10 12:08:37 | `.tmp\_d05_b_coincidence_checks_2026_10_10.py` | `C1FC428D450C` | 22078 |
| 2026-10-10 12:07:27 | `.tmp\_d05_probe_j1.py` | `B3FBA6AE6152` | 4651 |
| 2026-10-10 12:07:07 | `.tmp\_d05_probe_leak.py` | `EDB264CCFC51` | 4105 |
| 2026-10-10 12:05:24 | `.tmp\_d05_probe_den.py` | `7B8207D9BBBA` | 4587 |
| 2026-10-10 12:05:07 | `.tmp\_d05_probe_train.py` | `4435748F010D` | 4770 |
| 2026-10-10 12:04:50 | `.tmp\_d05_probe_thresh.py` | `A91F28BFD48B` | 4565 |
| 2026-10-10 12:04:33 | `.tmp\_d05_probe_metrics.py` | `5A670AE27A5B` | 908 |
| 2026-10-10 12:04:21 | `.tmp\_d05_probe_order.py` | `788FDF5F3142` | 4981 |
| 2026-10-10 12:04:00 | `.tmp\_d05_probe_arm1.py` | `CCB6B4AEF623` | 4983 |
| 2026-10-10 12:02:44 | `.tmp\_d05_probe_phrase.py` | `E519B5D5F51E` | 4844 |
| 2026-10-10 12:02:24 | `.tmp\_d05_probe_dist.py` | `4866BA720010` | 4079 |
| 2026-10-10 12:02:02 | `.tmp\_d05_probe_seq.py` | `88C3533D7FCB` | 4925 |
| 2026-10-10 12:01:03 | `results\_wordlist_house_effectivity_note_2026_10_10.md` | `4E89A5BB4B68` | 14606 |
| 2026-10-10 12:00:40 | `results\_s4_regen_execution_plan_2026_10_10.md` | `70E22220350D` | 33444 |
| 2026-10-10 12:00:18 | `.tmp\_d05_probe_labels.py` | `53784EC36E27` | 3816 |
| 2026-10-10 12:00:12 | `results\_tmp_disposal_register_2026_10_10.md` | `E0F6B744E826` | 20812 |
| 2026-10-10 11:59:58 | `.tmp\_d05_probe_tree.py` | `D445274FCFA4` | 4616 |
| 2026-10-10 11:59:34 | `.tmp\_d05_probe_align.py` | `78C079BEF471` | 1429 |
| 2026-10-10 11:59:12 | `.tmp\_d05_probe_ho.py` | `3509E3F21790` | 1612 |
| 2026-10-10 11:58:15 | `.tmp\_d05_instrument_audit.py` | `EDFA99486954` | 5948 |
| 2026-10-10 11:55:01 | `.tmp\_d05_probe_inter.py` | `23EE92345BF1` | 3008 |
| 2026-10-10 11:54:20 | `.tmp\_d05_probe_keys.py` | `4BC4F8C89E44` | 1967 |
| 2026-10-10 11:53:38 | `results\_kd_rewrite_fingerprint_sync_2026_10_10.md` | `AEEFC94A94B5` | 20862 |
| 2026-10-10 11:51:23 | `.tmp\d05_hash_index.py` | `070B6F865EBA` | 1004 |
| 2026-10-10 11:45:26 | `results\_e6_j5_backfill_resolution_2026_10_10.md` | `C888158B3263` | 23171 |
| 2026-10-10 11:44:09 | `results\_kd04_c_denominator_expansion_readings_2026_10_10.json` | `249009E6A0CC` | 23314 |
| 2026-10-10 11:42:44 | `.tmp\_kd04_c_den_exec_2026_10_10.py` | `419F9F691E63` | 21430 |
| 2026-10-10 11:41:56 | `results\_kd04_c_denominator_expansion_exec_2026_10_10.md` | `2CAA3966B866` | 27915 |
| 2026-10-10 11:38:50 | `results\_kd_uncognizable_meaning_rewrite_register_2026_10_10.md` | `B07887551F7C` | 19525 |
| 2026-10-10 11:37:24 | `results\_s3_missing_field_backfill_rule_effective_2026_10_01.md` | `1450057B0819` | 52469 |
| 2026-10-10 11:37:24 | `results\_u11_execution_register_2026_10_09.md` | `8BC087A16F5A` | 24549 |
| 2026-10-10 11:37:24 | `results\_s3_missing_field_backfill_rule_draft_2026_10_01.md` | `8496A53D183A` | 35827 |
| 2026-10-10 11:37:24 | `results\_limb_reading_verdict_kv3s33_2026_10_01.md` | `C5866CE87D9C` | 56329 |
| 2026-10-10 11:37:24 | `results\_t1_gate_closure_and_recompute_verdict_2026_10_01.md` | `4BDD82C796B8` | 72934 |
| 2026-10-10 11:37:24 | `results\_n7_mutual_exclusion_determination_2026_10_01.md` | `B6BDF807CB27` | 40169 |
| 2026-10-10 11:37:24 | `results\_r3_r4_interpretation_case_2026_10_01.md` | `46469217883B` | 64849 |
| 2026-10-10 11:37:23 | `results\_t1_7_2_correction_2026_10_08.md` | `D90BF82338F6` | 16469 |
| 2026-10-10 11:37:23 | `results\_s3_kv3s_3_verdict_2026_10_01.md` | `E394BB6B5DDF` | 35037 |
| 2026-10-10 11:37:23 | `results\_s3_th_v21_reconciliation_verdict_2026_10_01.md` | `84FA6996B656` | 51073 |
| 2026-10-10 11:37:23 | `results\_mini_round_5_decisions_register_2026_10_01.md` | `D5FFFE6A5E79` | 53125 |
| 2026-10-10 11:37:23 | `results\_d1_backfill_intake_verdict_2026_10_01.md` | `A7E8F90D9DB7` | 42115 |
| 2026-10-10 11:37:23 | `results\_d1_ruling_and_s3_transition_2026_10_01.md` | `DC9CB0E02922` | 28370 |
| 2026-10-10 11:36:58 | `results\_kd_unambiguous_meaning_ruling_2026_10_10.md` | `F22EDE7226D2` | 24898 |
| 2026-10-10 11:36:54 | `results\_e5_nonbinary_count_judgment_2026_10_10.md` | `2EF8797C03F4` | 37762 |
| 2026-10-10 11:27:33 | `results\_kd04_c_denominator_killline_prereg_2026_10_10.md` | `8F2025E9DE6F` | 24527 |
| 2026-10-10 11:25:56 | `results\_exp06_selfverified_renaming_note_2026_10_10.md` | `8B4EC41A37DD` | 34554 |
| 2026-10-10 11:23:01 | `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | `341B6726AC4E` | 33994 |
| 2026-10-10 11:23:01 | `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | `CD43C41716F0` | 35321 |
| 2026-10-10 11:22:20 | `.tmp\_exp06_1009fix_build_2026_10_10.py` | `E5ACB3C0BCA2` | 29412 |
| 2026-10-10 11:20:46 | `.tmp\_exp06_1009fix_lnref2_2026_10_10.py` | `3FF21D556306` | 1505 |
| 2026-10-10 11:20:15 | `.tmp\_exp06_1009fix_lnref_2026_10_10.py` | `9C7096147878` | 1508 |
| 2026-10-10 11:18:26 | `results\_t_s3_3_disposition_judgment_2026_10_10.md` | `EE7A822A077B` | 31855 |
| 2026-10-10 11:17:16 | `.tmp\_exp06_1009fix_verify_2026_10_10.py` | `47FDF9673ACC` | 7817 |
| 2026-10-10 11:10:18 | `results\_s4_feature_surface_v3_1_definition_2026_10_10.md` | `D044CE1C069D` | 30310 |
| 2026-10-10 11:06:34 | `results\_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | `B508E5335377` | 29664 |
| 2026-10-10 11:02:09 | `results\_round27_34_approvals_effect_register_2026_10_10.md` | `D0BC0B1A9AE0` | 73226 |
| 2026-10-10 10:59:49 | `.tmp\_vk_q6.py` | `7DA34DD24EB0` | 811 |
| 2026-10-10 10:58:17 | `.tmp\_vk_q5.py` | `7B95307225BA` | 1246 |
| 2026-10-10 10:58:01 | `.tmp\_vk_q4.py` | `DEFC3C53B7DF` | 784 |
| 2026-10-10 10:57:46 | `.tmp\_vk_q3.py` | `A00CD309205F` | 612 |
| 2026-10-10 10:57:35 | `.tmp\_vk_q2.py` | `D5759D40DC43` | 540 |
| 2026-10-10 10:57:23 | `.tmp\_vk_q.py` | `67364902116C` | 519 |
| 2026-10-10 10:54:25 | `results\_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | `D6FF041A9DF9` | 116506 |
| 2026-10-10 10:51:43 | `results\_exp06_selfverified_runner_fix_note_2026_10_10.md` | `247398B687E6` | 17052 |
| 2026-10-10 10:51:31 | `results\_t1_temp_axis_retirement_consolidation_2026_10_10.md` | `40CB2E81425A` | 20308 |
| 2026-10-10 10:50:15 | `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py` | `041525FD05A2` | 31457 |
| 2026-10-10 10:49:23 | `.tmp\_exp06_fixcopy_verify_probe_2026_10_10.py` | `680B6893F9F7` | 3598 |
| 2026-10-10 10:48:57 | `results\_s4_tree_prereg_revision_2026_10_10.md` | `037140972829` | 30382 |
| 2026-10-10 10:46:49 | `results\_exp05_missing_true_disposition_judgment_2026_10_10.md` | `E8E1E63A11DB` | 25552 |
| 2026-10-10 10:41:53 | `results\_kd_legacy_rewrite_register_2026_10_10.md` | `9A7936882A5D` | 14537 |
| 2026-10-10 10:40:29 | `results\_kd_legacy_rewrite_ruling_2026_10_10.md` | `2CADAB5ED4F7` | 13731 |
| 2026-10-10 10:33:56 | `results\_exp08_volume_reconciliation_2026_10_10.md` | `895EB3F2943C` | 24140 |
| 2026-10-10 10:33:13 | `results\_exp06_supplement_four_gaps_2026_10_10.md` | `9F86CC5BE8E9` | 26519 |
| 2026-10-10 10:31:42 | `results\_exp06_independent_check_2026_10_10.json` | `4C36C376AB9C` | 20480 |
| 2026-10-10 10:31:30 | `.tmp\exp06_independent_json_gen_2026_10_10.py` | `5CE8F89C9396` | 21560 |
| 2026-10-10 10:30:11 | `.tmp\exp06_supplement_probe_2026_10_10.py` | `97076C37AFA7` | 7438 |
| 2026-10-10 10:30:11 | `.tmp\_verify_r32_card_2026_10_10.py` | `61F99FC5FDB9` | 631 |
| 2026-10-10 10:29:40 | `results\_t1_exp2_verdict_bytes_correction_2026_10_10.md` | `E863CA5FB157` | 13480 |
| 2026-10-10 10:26:50 | `results\_s4_dkb_backfill_register_2026_10_10.md` | `3A992C3FE235` | 25591 |
| 2026-10-10 10:14:38 | `results\_v3r1_threshold_path4_draft_2026_10_10.md` | `A51F5DE630ED` | 39077 |
| 2026-10-10 10:12:37 | `.tmp\_dump_dkb3_records2_2026_10_10.py` | `E71D1E81DA64` | 1366 |
| 2026-10-10 10:11:13 | `.tmp\_dump_dkb3_records_2026_10_10.py` | `144B204237BF` | 1781 |
| 2026-10-10 10:06:54 | `results\_exp04_h_contrast_readings_2026_10_10.md` | `AC571BFE4D1D` | 17386 |
| 2026-10-10 10:05:05 | `results\_exp04_h_contrast_readings_2026_10_10.json` | `106E8667BE2D` | 72704 |
| 2026-10-10 10:04:20 | `.tmp\exp04_h_contrast_2026_10_10.py` | `572F1B9C3927` | 14333 |
| 2026-10-10 10:03:53 | `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc` | `74467BB37F95` | 103946 |
| 2026-10-10 09:58:13 | `results\_v3r1_threshold_final_path_judgment_2026_10_10.md` | `93F187F1AB75` | 39653 |
| 2026-10-10 09:55:59 | `results\_s4_tree_construct_adjustment_exec_2026_10_10.md` | `B6B47008F8FD` | 28515 |
| 2026-10-10 09:51:47 | `results\_s4_tree_construct_adjusted_readings_2026_10_10.json` | `A7AA4E9C8D47` | 108593 |
| 2026-10-10 09:51:36 | `.tmp\_s4_tree_construct_exec_2026_10_10.py` | `4CBD10B61AAE` | 34265 |
| 2026-10-10 09:51:16 | `results\_blade_caliber_b8_judgment_2026_10_10.md` | `E189D6EB63D9` | 28738 |
| 2026-10-10 09:44:42 | `results\_s4_regen_traceability_judgment_2026_10_10.md` | `A330273B981C` | 36071 |
| 2026-10-10 09:43:25 | `results\_t1_temp_axis_retirement_judgment_2026_10_10.md` | `19AFC7E191A7` | 27384 |
| 2026-10-10 03:23:28 | `results\_overnight_delivery_index_2026_10_10.md` | `266D0327025D` | 35344 |
| 2026-10-10 03:13:46 | `results\_reading_face_basis_rejudge_2026_10_10.md` | `3FE193A2A01F` | 24208 |
| 2026-10-10 03:07:20 | `results\_exp08_s4_prompt_face_register_2026_10_10.md` | `83109ECF440E` | 11929 |
| 2026-10-10 03:06:42 | `results\_exp06_kcf4_check_bit_landing_2026_10_10.md` | `088BA3D58C0F` | 20709 |
| 2026-10-10 03:06:08 | `results\_exp05_negative_probe_rescan_2026_10_10.md` | `CA7FF556FD7A` | 11566 |
| 2026-10-10 03:00:34 | `results\_exp03_blade_caliber_review_2026_10_10.md` | `8C030758B331` | 19797 |
| 2026-10-10 02:58:44 | `.tmp\_exp03_blade_recompute_out_2026_10_10.json` | `3D7DE35263F8` | 19719 |
| 2026-10-10 02:57:52 | `results\_kd_legacy_rewrite_plan_2026_10_10.md` | `A9698FED8B9B` | 17643 |
| 2026-10-10 02:54:17 | `results\_nonportrait_criterion_formalization_design_2026_10_10.md` | `F4E145B090B1` | 55605 |
| 2026-10-10 02:47:15 | `results\_t1_exp2_verdict_2026_10_10.md` | `15C1C4B317A0` | 48298 |
| 2026-10-10 02:45:24 | `results\_bayesian_baseline_design_2026_10_10.md` | `7E181A167702` | 29783 |
| 2026-10-10 02:43:26 | `results\_wordlist_house_establishment_draft_2026_10_10.md` | `AFA5EB53D216` | 38468 |
| 2026-10-10 02:34:26 | `results\_t1_exp2_exec_register_2026_10_09.md` | `3A08DCFA8C7F` | 18597 |
| 2026-10-10 02:33:06 | `results\_t1_exp2_result_2026_10_09.json` | `D9CCD75C652B` | 35239 |
| 2026-10-10 02:31:56 | `.tmp\_t1_exp2_c_driver_stdout4.log` | `16F08FF22F9D` | 73756 |
| 2026-10-10 02:31:56 | `.tmp\_t1_exp2_c_driver.log` | `8ABAC60BB797` | 108388 |
| 2026-10-10 02:31:55 | `.tmp\_t1_exp2_c_records.json` | `F53681C7569A` | 6277328 |
| 2026-10-10 01:37:43 | `.tmp\_t1_exp2_c_driver_stdout3.log` | `D0AACA46B41A` | 9376 |
| 2026-10-10 01:25:59 | `results\_s4_tree_construct_adjustment_assessment_2026_10_10.md` | `016C7DACAA54` | 33453 |
| 2026-10-10 01:23:46 | `.tmp\_s4_tree_construct_probe_2026_10_10.py` | `E1073738B40D` | 8643 |
| 2026-10-10 01:15:42 | `results\_149_face_effect_disposal_2026_10_10.md` | `E7C1232DF138` | 24295 |
| 2026-10-10 01:15:09 | `results\_round23_26_threshold_review_effect_register_2026_10_10.md` | `9B0C62765576` | 47297 |
| 2026-10-10 01:12:02 | `results\_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | `11681F0AD861` | 67225 |
| 2026-10-10 01:11:45 | `.tmp\gen_supp3.py` | `EB53C9CE140C` | 15813 |
| 2026-10-10 01:11:17 | `results\_s4_keyword_expansion_and_regen_design_2026_10_10.md` | `6EFDDAB54CA5` | 31149 |
| 2026-10-10 01:06:09 | `results\_alt_delib_pkg3_two_judgments_2026_10_10.md` | `3F52709A48E8` | 38032 |
| 2026-10-10 01:00:44 | `results\_v3r1_threshold_restatement_design_2026_10_10.md` | `FB85A8013F9D` | 33847 |
| 2026-10-10 00:47:10 | `results\_q3_reported_value_errata_supplement_2026_10_10.md` | `E026F20839B1` | 12499 |
| 2026-10-10 00:43:53 | `results\_id_face_revision_sync_note_2026_10_10.md` | `5D6C473731C4` | 20690 |
| 2026-10-10 00:40:54 | `results\_s4_empty_sequence_backfill_assessment_2026_10_10.md` | `41B75FFEA7BE` | 28771 |
| 2026-10-10 00:39:05 | `results\_kv3s_4_4_carryover_bytes_correction_2026_10_10.md` | `0A7D2CCF74AD` | 5807 |
| 2026-10-10 00:38:39 | `results\_kv3s_4_4_review_carryover_2026_10_10.md` | `660D40DDD78C` | 17606 |
| 2026-10-10 00:37:39 | `.tmp\card23_readout_utf8.txt` | `4AA127D1DC62` | 5088 |
| 2026-10-10 00:37:32 | `.tmp\_t1_exp2_c_driver_stdout2.log` | `120391010514` | 9272 |
| 2026-10-10 00:37:18 | `.tmp\_card23_readout_utf8.txts` | `4AA127D1DC62` | 5088 |
| 2026-10-10 00:31:40 | `results\_t1p2_judgment_bytes_correction_2026_10_10.md` | `D9D29BEC3A0B` | 6377 |
| 2026-10-10 00:31:15 | `results\_round19_followup_round21_22_approvals_effect_register_2026_10_10.md` | `0C8DBA07DD1E` | 54850 |
| 2026-10-10 00:30:53 | `results\_t1p2_escalation_judgment_2026_10_10.md` | `5F43775A3224` | 22930 |
| 2026-10-10 00:30:13 | `results\_t1p2_enable_judgment_2026_10_10.md` | `1E97D06B6EC9` | 20132 |
| 2026-10-10 00:24:02 | `results\_round20_approvals_effect_register_2026_10_10.md` | `29D737C59E8B` | 27711 |
| 2026-10-10 00:23:35 | `results\_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `DC43E3CB7610` | 262542 |
| 2026-10-10 00:18:41 | `results\_t1_d7_reading_line_judgment_2026_10_10.md` | `60BD9AE98640` | 28559 |
| 2026-10-09 23:56:42 | `results\_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md` | `9572DFC3CD59` | 16105 |
| 2026-10-09 23:54:42 | `.tmp\_q3_l282_fix_validate_2026_10_09.txt` | `35B98FD8CDE4` | 6026 |
| 2026-10-09 23:54:41 | `results\_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` | `E30D4032F195` | 64849 |
| 2026-10-09 23:49:50 | `results\_s4_face_closeout_2026_10_09.md` | `F7D76EDA2911` | 29158 |
| 2026-10-09 23:42:59 | `results\_evening_audit_b2_sampling_and_rejudges_2026_10_09.md` | `B067FD28F950` | 29069 |
| 2026-10-09 23:42:17 | `results\_pi_pending_items_draft_package_2026_10_09.md` | `8FA2A7A2C49D` | 51793 |
| 2026-10-09 23:37:33 | `.tmp\_t1_exp2_c_driver_stdout.log` | `0BF18EDC773D` | 9410 |
| 2026-10-09 23:32:35 | `results\_beta_formal_run_exec_register_2026_10_09.md` | `2E5F080EAB6C` | 16811 |
| 2026-10-09 23:30:08 | `results\_beta_formal_run_result_2026_10_09.json` | `A5A918FD9861` | 103691 |
| 2026-10-09 23:30:07 | `results\_rpq_wordlist_and_t1p2_judgments_2026_10_09.md` | `246CE35C4DDC` | 44796 |
| 2026-10-09 23:26:45 | `results\_q3_transposition_errata_2026_10_09.md` | `659C4101F10B` | 11757 |
| 2026-10-09 23:25:55 | `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.cpython-314.pyc` | `F96453EBEAD6` | 55784 |
| 2026-10-09 23:25:21 | `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.cpython-314.pyc` | `80A752CCA163` | 57022 |
| 2026-10-09 23:22:00 | `results\_s4_bc_construction_ruling_2026_10_09.md` | `E2FDB380CD3C` | 30257 |
| 2026-10-09 23:16:17 | `results\_vk_two_items_judgments_2026_10_09.md` | `82556D54726C` | 33399 |
| 2026-10-09 23:10:27 | `results\_kv3s_4_4_rejudge_2026_10_09.md` | `BC397D5099DD` | 42687 |
| 2026-10-09 23:02:14 | `results\_c1c4_ab_pilot_comparison_2026_10_09.md` | `BDD2A1D7E6C5` | 15390 |
| 2026-10-09 22:59:59 | `results\_c1c4_ab_beta_pilot_result_2026_10_09.json` | `FD72EBF836E1` | 109879 |
| 2026-10-09 22:59:41 | `deposon_team\plugins\boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.py` | `3524E454D8ED` | 47580 |
| 2026-10-09 22:58:01 | `results\_v3_05_h_caliber_judgment_2026_10_09.md` | `1C2B5F40E15D` | 22050 |
| 2026-10-09 22:55:04 | `results\_c1c4_ab_alpha_pilot_result_2026_10_09.json` | `BC7C35707B78` | 104225 |
| 2026-10-09 22:54:53 | `deposon_team\plugins\boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py` | `06016F90FD3A` | 45777 |
| 2026-10-09 22:50:42 | `results\__pycache__\_t1_exp2_executor_2026_10_09.cpython-314.pyc` | `346595DF084C` | 87302 |
| 2026-10-09 22:50:18 | `results\_s4_face_five_lines_ci_readings_execution_2026_10_09.md` | `73550514152D` | 29750 |
| 2026-10-09 22:45:37 | `.tmp\_t1_exp2_d_readings.json` | `2315F6823011` | 3991 |
| 2026-10-09 22:44:11 | `.tmp\_t1_exp2_d_records.json` | `AADBA0C4F952` | 488395 |
| 2026-10-09 22:43:07 | `results\_r_pair_interval_statement_errata_2026_10_09.md` | `61944EB91B72` | 9259 |
| 2026-10-09 22:42:46 | `results\_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md` | `5FAA16446171` | 23975 |
| 2026-10-09 22:41:07 | `.tmp\_t1_exp2_run_d2.log` | `34123220512B` | 3132 |
| 2026-10-09 22:34:56 | `results\_kv3s_4_1_2_rejudge_2026_10_09.md` | `9CDE399502BA` | 51594 |
| 2026-10-09 22:32:22 | `results\_r_pair_nonportrait_full_document_review_2026_10_09.md` | `D8D5E4D2154F` | 28176 |
| 2026-10-09 22:30:43 | `.tmp\_t1_exp2_run_d.log` | `B5391E5B0CA3` | 4752 |
| 2026-10-09 22:30:20 | `.tmp\_rpq_nonportrait_full_probe_out4_2026_10_09.txt` | `B2C96951BC8F` | 9112 |
| 2026-10-09 22:27:05 | `.tmp\_rpq_nonportrait_full_probe_out3_2026_10_09.txt` | `3B5ECD179B2F` | 43422 |
| 2026-10-09 22:25:54 | `.tmp\_rpq_nonportrait_full_probe_out_2026_10_09.txt` | `4470B09DA8F4` | 23891 |
| 2026-10-09 22:22:58 | `.tmp\_t1_exp2_c_driver_2026_10_09.py` | `5D474B7CEADA` | 2898 |
| 2026-10-09 22:22:00 | `results\_t1_exp2_answer_face_baseline_2026_10_09.json` | `35773F5F1EDB` | 11792 |
| 2026-10-09 22:21:51 | `results\_t1_exp2_executor_2026_10_09.py` | `CE393B41618C` | 67955 |
| 2026-10-09 22:21:20 | `results\_t1_gate_revision_formal_2026_10_09.md` | `0E0CB002C5DE` | 35658 |
| 2026-10-09 22:20:17 | `.tmp\_t1_exp2_calib_2026_10_09.json` | `DE09D4EE3721` | 611 |
| 2026-10-09 22:19:48 | `.tmp\_t1_exp2_probe_log.json` | `C6478415E2BF` | 760 |
| 2026-10-09 22:19:29 | `.tmp\_t1_exp2_selfcert.json` | `D929EB9AE0B8` | 6780 |
| 2026-10-09 22:17:22 | `results\_t1_exp2_activation_supplement_2026_10_09.md` | `8DB3F88B5ED0` | 24708 |
| 2026-10-09 22:15:52 | `.tmp\_t1_exp2_pi_card_ask6455cd9f15bf7dc12ae673d9.json` | `A7322DFE48E5` | 5269 |
| 2026-10-09 22:11:08 | `results\_s4_heldout_sampling_seed42_items_register_2026_10_09.md` | `73A02AC5937D` | 34689 |
| 2026-10-09 22:08:53 | `.tmp\__pycache__\_s4_heldout_items_exec.cpython-314.pyc` | `8FE2DDA7646C` | 22922 |
| 2026-10-09 22:08:41 | `results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | `6A670E629DCA` | 20033 |
| 2026-10-09 21:59:00 | `results\_kd_writing_convention_guidance_2026_10_09.md` | `708DFAC55BE9` | 20179 |
| 2026-10-09 21:56:51 | `results\_t1_pairing_caliber_ruling_2026_10_09.md` | `2DED8091114A` | 21346 |
| 2026-10-09 21:55:37 | `.tmp\_pk_pairing_caliber_probe_2026_10_09.py` | `0ADE7A44D216` | 4463 |
| 2026-10-09 21:53:50 | `.tmp\_probe_schema.py` | `D9A4F1898C31` | 583 |
| 2026-10-09 21:53:15 | `results\_pi_facing_items_screen_2026_10_09.md` | `A6D33CF318FE` | 59604 |
| 2026-10-09 21:49:30 | `results\_t1_prereg_revision_temp_axis_exp2_2026_10_09.md` | `2FF15AEEB5D0` | 34217 |
| 2026-10-09 21:45:26 | `results\_r2_verdict_179domain_arith_verification_2026_10_09.md` | `511C81B96745` | 30532 |
| 2026-10-09 21:39:22 | `.tmp\_ea_179_domain_retest_2026_10_09.py` | `9309E4977B22` | 2814 |
| 2026-10-09 21:36:37 | `.tmp\_ea_r2_axis_probe2_2026_10_09.py` | `DBE562353608` | 2863 |
| 2026-10-09 21:36:01 | `.tmp\_ea_r2_recompute_probe_2026_10_09.py` | `817639D7E5C3` | 6596 |
| 2026-10-09 21:28:13 | `results\_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `193386B9F23C` | 72199 |
| 2026-10-09 21:28:08 | `results\_t1_r2_d1_field_caliber_correction_2026_10_09.md` | `99CAFDA125F1` | 25396 |
| 2026-10-09 21:26:53 | `results\_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | `FB1B696DE1D6` | 35453 |
| 2026-10-09 21:17:22 | `results\_t1_gate_revision_draft_2026_10_09.md` | `50E8B2440346` | 27452 |
| 2026-10-09 21:17:20 | `results\_t1_temp_axis_new_experiment_design_2026_10_09.md` | `7AAA90EE6D50` | 41392 |
| 2026-10-09 21:15:30 | `results\_s4_face_five_lines_ci_readings_2026_10_09.md` | `BEA9BC43A8F3` | 39462 |
| 2026-10-09 21:13:23 | `.tmp\_t1_temp_axis_design_probe_2026_10_09.json` | `02E8133D3000` | 5657 |
| 2026-10-09 21:13:15 | `.tmp\_t1_temp_axis_design_probe_2026_10_09.py` | `F4A736868825` | 7634 |
| 2026-10-09 21:12:50 | `results\_ci_three_items_effectivity_register_2026_10_09.md` | `2B7166A7D726` | 31488 |
| 2026-10-09 21:11:25 | `results\_s4_heldout_sampling_seed42_register_2026_10_09.md` | `2A2AD5C2E29F` | 37615 |
| 2026-10-09 21:07:05 | `results\_s4_heldout_sampling_seed42_sets_2026_10_09.json` | `8DFC9E0D8BF9` | 59100 |
| 2026-10-09 21:06:53 | `results\_k_v3s_4_2_domain_extension_judgment_2026_10_09.md` | `A802AF7AC3BC` | 23018 |
| 2026-10-09 21:05:37 | `.tmp\__pycache__\_s4_heldout_seed42_probe_2026_10_09.cpython-314.pyc` | `C6999C34D697` | 18870 |
| 2026-10-09 21:03:55 | `results\_s4_substrate_refreeze_register_179_2026_10_09.md` | `24EA764DAEAC` | 45386 |
| 2026-10-09 21:01:37 | `results\_kd_resolvability_and_optional_experiments_2026_10_09.md` | `3138AC9095B0` | 70328 |
| 2026-10-09 21:00:29 | `.tmp\_s4_refreeze179_final_readings_2026_10_09.txt` | `4B1A8145E7B7` | 1306 |
| 2026-10-09 21:00:23 | `.tmp\_s4_refreeze179_final_probe_2026_10_09.py` | `AD615FB96FA1` | 3954 |
| 2026-10-09 21:00:07 | `.tmp\_s4_refreeze179_grid_readings2_2026_10_09.txt` | `E26BA2C34705` | 2351 |
| 2026-10-09 21:00:01 | `.tmp\_s4_refreeze179_grid_probe2_2026_10_09.py` | `B8866D89B84C` | 4518 |
| 2026-10-09 20:59:40 | `.tmp\_s4_refreeze179_grid_readings_2026_10_09.txt` | `4D175865DB79` | 5293 |
| 2026-10-09 20:59:35 | `.tmp\_s4_refreeze179_grid_probe_2026_10_09.py` | `4F1F759F66AF` | 9824 |
| 2026-10-09 20:59:10 | `.tmp\_s4_refreeze179_readings_2026_10_09.txt` | `18426FF0AFB0` | 3833 |
| 2026-10-09 20:59:10 | `.tmp\_s4_refreeze179_enumerate_probe3_2026_10_09.py` | `5472B7D7BFBA` | 4843 |
| 2026-10-09 20:58:39 | `.tmp\_s4_refreeze179_enumerate_probe2_2026_10_09.py` | `169D160BA600` | 4630 |
| 2026-10-09 20:58:39 | `.tmp\_s4_refreeze179_enumerate_probe_2026_10_09_v1_dead.py` | `169D160BA600` | 4630 |
| 2026-10-09 20:58:20 | `.tmp\_s4_refreeze179_enumerate_probe_2026_10_09.py` | `3CA8EEC4888F` | 4241 |
| 2026-10-09 18:23:43 | `results\_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md` | `9C18B9893579` | 42817 |
| 2026-10-09 18:20:53 | `.tmp\_vk_r2_axis_probe_2026_10_09.py` | `EB35C7A23CF5` | 5806 |
| 2026-10-09 18:10:40 | `.tmp\_t1_r2_verify_2026_10_09.json` | `860294C4FC8F` | 5641 |
| 2026-10-09 18:10:33 | `results\_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | `CF4826A731D6` | 23681 |
| 2026-10-09 18:10:16 | `results\_questionnaire_cards_intake_register_2026_10_09.md` | `D917180DB36F` | 442288 |
| 2026-10-09 18:06:24 | `results\_kv3s_4_terminal_verdict_supplement_2026_10_09.md` | `0F82948DEFB3` | 20211 |
| 2026-10-09 18:06:16 | `results\_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | `8D6242DA158C` | 58712 |
| 2026-10-09 18:06:06 | `results\_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | `38D0CF7FC9BA` | 53184 |
| 2026-10-09 18:03:12 | `.tmp\_t1_r2_run_driver.log` | `C397AD7AF316` | 37504 |
| 2026-10-09 18:03:12 | `.tmp\_t1_qwen_temp_sweep_r2_records.json` | `BB511E7B0BAF` | 1795870 |
| 2026-10-09 17:54:34 | `results\_kd_heteronym_classification_disposition_2026_10_09.md` | `C0CFD21D57A8` | 29761 |
| 2026-10-09 17:48:22 | `results\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md` | `BEE0F1F0BDB2` | 29709 |
| 2026-10-09 17:43:45 | `.tmp\_ci_gap_fill_out.txt` | `353DC9DF9650` | 11040 |
| 2026-10-09 17:43:45 | `results\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.json` | `F729A6A03A9E` | 23272 |
| 2026-10-09 17:43:25 | `results\_r_pair_texts_independent_review_2026_10_09.md` | `8C5F83C3C4CF` | 35443 |
| 2026-10-09 17:43:14 | `results\__pycache__\_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | `E7AB1ADBF898` | 69630 |
| 2026-10-09 17:42:53 | `.tmp\_ci_gap_fill_err.txt` | `E3B0C44298FC` | 0 |
| 2026-10-09 17:42:45 | `.tmp\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | `B0CF9BABA64B` | 20997 |
| 2026-10-09 17:39:04 | `.tmp\_rpq_indep_probe_2026_10_09.py` | `DCFEA9293D62` | 6529 |
| 2026-10-09 17:36:04 | `.tmp\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.log` | `F258AE241DEB` | 2360 |
| 2026-10-09 17:34:40 | `results\__pycache__\_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | `08D4B51C45C6` | 67081 |
| 2026-10-09 17:34:04 | `results\_ci_bc_scope_estimand_judgments_2026_10_09.md` | `D76BA2297D0D` | 37682 |
| 2026-10-09 17:33:46 | `results\_k_v3df_scope_two_judgments_2026_10_09.md` | `4B22BA3C463E` | 21350 |
| 2026-10-09 17:32:42 | `results\_ci_degradation_binding_form_a_register_2026_10_09.md` | `424730B5123D` | 26104 |
| 2026-10-09 17:27:41 | `results\_c1c4_input_gap_fill_plan_2026_10_09.md` | `9F5675633E03` | 35635 |
| 2026-10-09 17:26:27 | `results\_u04_1_exemption_precondition_verification_2026_10_09.md` | `C072FFE6110E` | 21377 |
| 2026-10-09 17:25:09 | `results\_u04_1_exemption_precondition_verification_2026_10_09.json` | `BDDFEAC3EE2F` | 21862 |
| 2026-10-09 17:24:49 | `.tmp\u04_1_make_data.py` | `309AC58E049D` | 19773 |
| 2026-10-09 17:24:17 | `.tmp\gate_check2.py` | `7025CECEB766` | 840 |
| 2026-10-09 17:24:02 | `.tmp\gate_check.py` | `ABE7FBDB394B` | 648 |
| 2026-10-09 17:23:30 | `results\_kv3s_4_terminal_verdict_2026_10_09.md` | `E51317FCC5CF` | 50858 |
| 2026-10-09 17:23:16 | `.tmp\u04_1_dual_verify.py` | `F5702456560F` | 3228 |
| 2026-10-09 17:22:54 | `.tmp\u04_1_chain_verify.py` | `13E573534692` | 4849 |
| 2026-10-09 17:22:28 | `.tmp\pa_block.py` | `19AC8C59439B` | 345 |
| 2026-10-09 17:22:02 | `.tmp\kro_extract.py` | `B5731ABAE41F` | 802 |
| 2026-10-09 17:16:22 | `results\_ci_three_delegated_judgments_2026_10_09.md` | `DAC19EE9E66B` | 26090 |
| 2026-10-09 17:14:39 | `results\_ci_four_items_effectiveness_register_2026_10_09.md` | `4AB2464A266E` | 29365 |
| 2026-10-09 17:09:36 | `results\_t1_o1_design_axis_exemption_judgment_2026_10_09.md` | `A27C7F411DE5` | 17073 |
| 2026-10-09 17:08:31 | `results\_t1_p2_aggregation_caliber_judgment_2026_10_09.md` | `02F44F5BF2DD` | 14397 |
| 2026-10-09 17:08:17 | `results\_s4_terminal_face_recompute_2026_10_09.md` | `B412342EABEC` | 46701 |
| 2026-10-09 17:07:33 | `results\_t1_r2_activation_2026_10_09.md` | `8E59B797AA2D` | 21111 |
| 2026-10-09 17:06:53 | `results\_k_cf_4_effectivity_register_2026_10_09.md` | `EDC6A548E3CA` | 35872 |
| 2026-10-09 17:02:49 | `.tmp\_s4_terminal_decomp_probe_2026_10_09.py` | `5F222D513F87` | 5192 |
| 2026-10-09 17:00:27 | `.tmp\_s4_terminal_uv_probe_2026_10_09.py` | `B687B9844BA2` | 6412 |
| 2026-10-09 16:59:55 | `.tmp\_t1_r2_verify_2026_10_09.py` | `3CE6D45CFBF7` | 4018 |
| 2026-10-09 16:59:17 | `.tmp\_t1_r2_run_driver_2026_10_09.py` | `B71F4916BEE1` | 2749 |
| 2026-10-09 16:59:00 | `.tmp\_t1_qwen_temp_sweep_r2_probe_log.json` | `5182F6FDD9EF` | 739 |
| 2026-10-09 16:58:49 | `.tmp\_t1_qwen_temp_sweep_r2_selfcert.json` | `124051B56295` | 6353 |
| 2026-10-09 16:58:13 | `.tmp\_s4_terminal_grid_probe_2026_10_09.py` | `A131C696A55E` | 8584 |
| 2026-10-09 16:57:36 | `results\_s4_face_dual_files_verification_2026_10_09.md` | `CC3FC6EEBC6B` | 40228 |
| 2026-10-09 16:55:16 | `.tmp\_t1_r2_calib_max_tokens_2026_10_09.json` | `3F35AEDE29F6` | 3305 |
| 2026-10-09 16:53:04 | `.tmp\_enc_test.txt` | `B1E6F7046A46` | 67 |
| 2026-10-09 16:52:24 | `.tmp\_t1_r2_calib_max_tokens_2026_10_09.py` | `7BBB0DE0C00F` | 6120 |
| 2026-10-09 16:48:49 | `.tmp\_verify_dual_probe9_2026_10_09.py` | `A4467A8A7118` | 1722 |
| 2026-10-09 16:48:36 | `results\_r_pair_intake_recompute_register_2026_10_09.md` | `2DC64593B889` | 36774 |
| 2026-10-09 16:48:23 | `.tmp\_verify_dual_probe8_2026_10_09.py` | `F40D20D0794F` | 2396 |
| 2026-10-09 16:47:08 | `.tmp\_verify_dual_probe7_2026_10_09.py` | `3EBBF43ECDAF` | 2795 |
| 2026-10-09 16:47:04 | `results\_ci_bc_lines_ci_collection_2026_10_09.md` | `6DB4D0FB2452` | 24769 |
| 2026-10-09 16:46:36 | `.tmp\_rp_verify_2026_10_09.py` | `E0ADAE15FC26` | 3282 |
| 2026-10-09 16:46:24 | `.tmp\_verify_dual_probe6_2026_10_09.py` | `35D6E8C4F838` | 3227 |
| 2026-10-09 16:46:11 | `.tmp\_rp_post_probe_2026_10_09.py` | `AB6B1AA8BE4B` | 3641 |
| 2026-10-09 16:45:41 | `.tmp\_verify_dual_probe5_2026_10_09.py` | `605F4E963169` | 3160 |
| 2026-10-09 16:45:34 | `results\_r_pair_addendum_2026_10_09.json` | `CEBC2F6EF5EC` | 110510 |
| 2026-10-09 16:45:20 | `.tmp\_rp_addendum_build_2026_10_09.py` | `C4E8B75D656B` | 30375 |
| 2026-10-09 16:45:06 | `.tmp\_verify_dual_probe4_2026_10_09.py` | `4AE5BE9872A1` | 3374 |
| 2026-10-09 16:43:36 | `.tmp\_verify_dual_probe3b_2026_10_09.py` | `61F84109FC1F` | 2194 |
| 2026-10-09 16:43:24 | `results\_th_id_miscitation_correction_2026_10_09.md` | `B61321BA3B6E` | 10468 |
| 2026-10-09 16:43:12 | `.tmp\_verify_dual_probe3_2026_10_09.py` | `E6BDD2712A13` | 2943 |
| 2026-10-09 16:41:49 | `.tmp\_verify_dual_probe2_2026_10_09.py` | `18261CBDE500` | 2453 |
| 2026-10-09 16:41:18 | `.tmp\_rp_intake_probe_2026_10_09.py` | `80EBA48D3D0B` | 4920 |
| 2026-10-09 16:41:07 | `.tmp\_verify_dual_probe1_2026_10_09.py` | `E42CF6C832BF` | 5671 |
| 2026-10-09 15:53:38 | `results\_ci_detail_decoupling_degradation_baseline_2026_10_09.md` | `56B62ED5AB74` | 20973 |
| 2026-10-09 15:52:02 | `results\_ci_width_halfwidth_pin_2026_10_09.md` | `51765F40F5F9` | 17426 |
| 2026-10-09 15:45:37 | `results\_s4_face_v2_sync_2026_10_09.md` | `9D3CC20FD980` | 46890 |
| 2026-10-09 15:44:50 | `results\_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md` | `618280CB8CFD` | 31801 |
| 2026-10-09 15:44:21 | `.tmp\_s4f2_manifest_post.txt` | `8824ECE12D30` | 130975 |
| 2026-10-09 15:39:37 | `results\_k_cf_4_low_cardinality_recure_2026_10_09.md` | `5F91D553E392` | 33788 |
| 2026-10-09 15:39:21 | `.tmp\_s4f2_manifest_pre.txt` | `8650EA333291` | 130701 |
| 2026-10-09 15:38:23 | `.tmp\_s4f2_probe6_2026_10_09.py` | `408E40B5D697` | 3067 |
| 2026-10-09 15:37:45 | `.tmp\_s4f2_probe5_2026_10_09.py` | `823AA6DEB0C5` | 4682 |
| 2026-10-09 15:36:59 | `.tmp\_s4f2_probe4_2026_10_09.py` | `6489BACF4B03` | 4132 |
| 2026-10-09 15:36:30 | `.tmp\_s4f2_probe3_out.txt` | `959372C08EFF` | 6228 |
| 2026-10-09 15:36:16 | `.tmp\_s4f2_probe3_2026_10_09.py` | `9B7DEADBC2ED` | 6735 |
| 2026-10-09 15:35:41 | `.tmp\_s4f2_probe2_out.txt` | `44C9D5176D12` | 9414 |
| 2026-10-09 15:35:26 | `.tmp\_s4f2_probe2_2026_10_09.py` | `7C05160D5B33` | 7959 |
| 2026-10-09 15:34:09 | `.tmp\_s4f2_probe_out.txt` | `B8F1E47BA331` | 9943 |
| 2026-10-09 15:33:46 | `results\_th_t1_n_min_revision_proposal_2026_10_09.md` | `24DA21074CC2` | 34884 |
| 2026-10-09 15:33:39 | `.tmp\_s4f2_face_probe_2026_10_09.py` | `62E04248D122` | 14896 |
| 2026-10-09 15:33:21 | `.tmp\_s4f2_dbg.py` | `5159C9C30180` | 431 |
| 2026-10-09 15:33:16 | `results\_s4_face_sync_2026_10_09.md` | `6F8BA105B892` | 38955 |
| 2026-10-09 15:32:23 | `.tmp\_s4f2_patch4.py` | `7D85756A841D` | 565 |
| 2026-10-09 15:32:06 | `.tmp\_s4fs_selfreport_2026_10_09.py` | `485071C7DD5E` | 432 |
| 2026-10-09 15:31:52 | `.tmp\_s4f2_patch3.py` | `6D57FF4CE76C` | 815 |
| 2026-10-09 15:31:23 | `.tmp\_s4f2_scanner_selftest.py` | `5B6FD262F785` | 1819 |
| 2026-10-09 15:31:07 | `.tmp\_s4f2_patch2.py` | `045BD90B237A` | 421 |
| 2026-10-09 15:30:03 | `.tmp\_s4f2_patch.py` | `B79A7073099D` | 2740 |
| 2026-10-09 15:29:34 | `.tmp\_s4fs_yitable_2026_10_09.py` | `2BF7FD0EF5DC` | 1634 |
| 2026-10-09 15:29:05 | `.tmp\_s4fs_auxdate_2026_10_09.py` | `637E936D8BC7` | 1877 |
| 2026-10-09 15:28:34 | `.tmp\_s4fs_probe_2026_10_09.py` | `96E37CA7314F` | 14709 |
| 2026-10-09 15:19:58 | `results\_ci_line_establishment_2026_10_09.md` | `329C1C5E91D1` | 28262 |
| 2026-10-09 15:09:52 | `results\_s4_final_ruling_card_register_2026_10_09.md` | `F62401B619CC` | 2135 |
| 2026-10-09 15:02:39 | `results\_th_id_attribution_verification_2026_10_09.md` | `94740F8D3C8D` | 8409 |
| 2026-10-09 15:00:52 | `results\_s4_final_ruling_effectivity_register_2026_10_09.md` | `21F2926EFC5D` | 32975 |
| 2026-10-09 14:52:20 | `results\_s4_chain_clearance_register_2026_10_09.md` | `EDA3D304D381` | 2684 |
| 2026-10-09 14:47:44 | `results\_s4_revision_effectiveness_register_2026_10_09.md` | `356FE8509669` | 32820 |
| 2026-10-09 14:46:03 | `results\_is_corr_pair_caliber_revision_proposal_2026_10_09.md` | `084C7D20067F` | 33497 |
| 2026-10-09 14:43:47 | `.tmp\_iscp_dual_probe_out_2026_10_09.txt` | `E3BAAE0B8D08` | 1342 |
| 2026-10-09 14:43:36 | `.tmp\_iscp_dual_impl_2026_10_09.py` | `8734F4326D5A` | 2974 |
| 2026-10-09 14:43:17 | `.tmp\_iscp_probe_out_2026_10_09.txt` | `B4C67CF64825` | 6424 |
| 2026-10-09 14:43:09 | `.tmp\_iscp_caliber_probe_2026_10_09.py` | `87497A1CF3B0` | 6344 |
| 2026-10-09 14:31:04 | `.tmp\_s4oq_final_verify_2026_10_09.py` | `944A4F7006C8` | 959 |
| 2026-10-09 14:30:52 | `results\_s4_open_questions_intake_recompute_register_2026_10_09.md` | `2E66478E6DB6` | 33672 |
| 2026-10-09 14:29:39 | `.tmp\_s4oq_recompute_2026_10_09.py` | `07CDEC653345` | 3202 |
| 2026-10-09 14:29:39 | `.tmp\_s4oq_stats_2026_10_09.json` | `570489BB6163` | 1669 |
| 2026-10-09 14:29:27 | `.tmp\_s4oq_verify_addendum_2026_10_09.py` | `419C15A7A2C5` | 2252 |
| 2026-10-09 14:29:17 | `results\_s4_open_questions_addendum_2026_10_09.json` | `4378DCC20624` | 35215 |
| 2026-10-09 14:29:16 | `.tmp\_s4oq_write_addendum_2026_10_09.py` | `63E61AFA6517` | 11886 |
| 2026-10-09 14:28:47 | `.tmp\_s4oq_sups_draft_2026_10_09.json` | `ACE64D4F377D` | 23401 |
| 2026-10-09 14:28:47 | `.tmp\_s4oq_build_draft_2026_10_09.py` | `0797D19DCAF3` | 8719 |
| 2026-10-09 14:28:05 | `.tmp\_s4oq_forward_2026_10_09.py` | `43E72C62587D` | 3482 |
| 2026-10-09 14:27:36 | `results\_k_v3s_4_3_frozen_recompute_2026_10_09.md` | `1C1494083255` | 26674 |
| 2026-10-09 14:27:35 | `.tmp\_s4oq_variants_2026_10_09.py` | `CCBBB499E19A` | 1233 |
| 2026-10-09 14:27:26 | `.tmp\_s4oq_skel_2026_10_09.py` | `73FC780B4849` | 466 |
| 2026-10-09 14:26:50 | `.tmp\_s4oq_grid_cmp_2026_10_09.py` | `F00865587D6A` | 1601 |
| 2026-10-09 14:26:34 | `.tmp\_s4oq_grid_diag_2026_10_09.py` | `082E8B8B7BC4` | 1553 |
| 2026-10-09 14:26:19 | `.tmp\_s4oq_grid_recompute_2026_10_09.py` | `AFB613F5CED1` | 2394 |
| 2026-10-09 14:25:58 | `.tmp\_s4oq_entryclass_probe_2026_10_09.py` | `2B9AD9A3EB8E` | 771 |
| 2026-10-09 14:25:49 | `.tmp\_kv3s43_frozen_recompute_readings3_2026_10_09.txt` | `3AD13513E25C` | 7370 |
| 2026-10-09 14:25:39 | `.tmp\_kv3s43_frozen_recompute_probe3_2026_10_09.py` | `BF2642242416` | 7782 |
| 2026-10-09 14:25:17 | `.tmp\_s4oq_addendum_struct_2026_10_09.py` | `67652ACDF681` | 843 |
| 2026-10-09 14:25:12 | `.tmp\_kv3s43_frozen_recompute_readings2_2026_10_09.txt` | `FC3BA9FE051B` | 7100 |
| 2026-10-09 14:25:04 | `.tmp\_s4oq_read_db_probe_2026_10_09.py` | `5926143C8A6D` | 658 |
| 2026-10-09 14:25:01 | `.tmp\_kv3s43_frozen_recompute_probe2_2026_10_09.py` | `ACF84B8657C5` | 6957 |
| 2026-10-09 14:24:41 | `.tmp\_kv3s43_diag_out.txt` | `24CE4995AA09` | 2378 |
| 2026-10-09 14:24:04 | `.tmp\_kv3s43_diag_2026_10_09.py` | `398EBF6F33E0` | 614 |
| 2026-10-09 14:23:34 | `.tmp\_kv3s43_frozen_recompute_readings_2026_10_09.txt` | `2F20780CB7A6` | 13244 |
| 2026-10-09 14:23:19 | `.tmp\_kv3s43_frozen_recompute_probe_2026_10_09.py` | `10AFD4410E25` | 7211 |
| 2026-10-09 14:22:32 | `results\_r_pair4_design_and_texts_2026_10_09.md` | `F793C5D9128F` | 35189 |
| 2026-10-09 14:20:42 | `.tmp\_rp4_final2_probe_2026_10_09.py` | `DA0E79E6E834` | 5929 |
| 2026-10-09 14:20:05 | `.tmp\_rp4_final_probe_2026_10_09.py` | `8B6DBCC64A16` | 7304 |
| 2026-10-09 14:19:41 | `.tmp\_rp4_cand3_probe_2026_10_09.py` | `2CA81A4A2D62` | 1494 |
| 2026-10-09 14:19:16 | `.tmp\_rp4_cand_probe_2026_10_09.py` | `1730FE65E2EE` | 5022 |
| 2026-10-09 14:18:29 | `.tmp\_rp4_grid_probe_2026_10_09.py` | `5950BD120B87` | 5003 |
| 2026-10-09 14:18:05 | `.tmp\_rp4_reuse_probe_2026_10_09.py` | `6F0098ED1C0C` | 5627 |
| 2026-10-09 14:17:49 | `results\_s4_substrate_freeze_register_2026_10_09.md` | `F4A52862521B` | 29064 |
| 2026-10-09 14:17:38 | `.tmp\_rp4_slug_probe_b_2026_10_09.py` | `AC6978F92A6D` | 4201 |
| 2026-10-09 14:17:03 | `.tmp\_rp4_slug_probe_2026_10_09.py` | `7F2126CFB6FF` | 2418 |
| 2026-10-09 14:16:26 | `.tmp\_rp4_probe_r7c.py` | `D65F18FFB59A` | 643 |
| 2026-10-09 14:16:15 | `.tmp\_rp4_probe_r7b.py` | `F3BE733BF87A` | 453 |
| 2026-10-09 14:16:02 | `.tmp\_rp4_probe_r7.py` | `249951837E6E` | 676 |
| 2026-10-09 14:14:54 | `.tmp\_rp4_fields.py` | `1D112AB8F3B4` | 433 |
| 2026-10-09 14:14:44 | `.tmp\_s4_freeze_rpair_readings_2026_10_09.txt` | `C2276232B04A` | 14312 |
| 2026-10-09 14:14:21 | `.tmp\_s4_freeze_rpair_probe_2026_10_09.py` | `0F3F44968250` | 2165 |
| 2026-10-09 14:13:57 | `.tmp\_s4_freeze_final_probe_2026_10_09.py` | `6CC3D55EC4F7` | 2419 |
| 2026-10-09 14:13:27 | `.tmp\_s4_freeze_bucket_src_probe_2026_10_09.py` | `73A2253B0D3D` | 1678 |
| 2026-10-09 14:13:15 | `.tmp\_rp4_probe_all_r.py` | `90023E831E24` | 1152 |
| 2026-10-09 14:13:03 | `.tmp\_rp4_probe_r78.py` | `6208A3327CF3` | 807 |
| 2026-10-09 14:12:34 | `.tmp\_s4_freeze_count_crosscheck3_2026_10_09.py` | `EE420DFD57E6` | 4041 |
| 2026-10-09 14:12:32 | `.tmp\_rp4_probe_r_axes.py` | `CF0534F24D4E` | 528 |
| 2026-10-09 14:12:07 | `.tmp\_s4_freeze_count_crosscheck2_2026_10_09.py` | `15FA4D155FC9` | 3920 |
| 2026-10-09 14:11:38 | `.tmp\_s4_freeze_rowkeys_probe_2026_10_09.py` | `256711C88004` | 1701 |
| 2026-10-09 14:11:12 | `.tmp\_s4_freeze_count_crosscheck_2026_10_09.py` | `856E6AB48DAE` | 3463 |
| 2026-10-09 14:10:29 | `.tmp\_s4_freeze_daystamp_probe_2026_10_09.py` | `3BB9E2856D95` | 3024 |
| 2026-10-09 14:10:08 | `.tmp\_s4_freeze_enumerate_probe_2026_10_09.py` | `AE51DDE19DD6` | 2218 |
| 2026-10-09 14:04:40 | `results\_s4_topup_intake_verdict_2026_10_09.md` | `658D7F3AB231` | 33799 |
| 2026-10-09 14:03:16 | `results\_v3_02_ethard_closure_verdict_2026_10_09.md` | `AA0F96BB618F` | 27819 |
| 2026-10-09 14:00:59 | `.tmp\_vk_pv02_recheck_g.py` | `F237E1D2715F` | 2269 |
| 2026-10-09 14:00:45 | `.tmp\_vk_pv02_recheck_f.py` | `C2E298CCEBC6` | 1522 |
| 2026-10-09 14:00:39 | `.tmp\_vk_dualread_probe_2026_10_09.txt` | `79AD926F75A8` | 888 |
| 2026-10-09 14:00:38 | `.tmp\_vk_dualread_probe_2026_10_09.py` | `A2C315831EFE` | 3240 |
| 2026-10-09 14:00:32 | `.tmp\_vk_pv02_recheck_e.py` | `D925E60C1D3C` | 1742 |
| 2026-10-09 14:00:06 | `.tmp\_vk_pv02_recheck_d.py` | `7AE7ED6BCD8A` | 982 |
| 2026-10-09 13:59:57 | `.tmp\_vk_baxis_probe_2026_10_09.txt` | `D74E9AE8CD3A` | 5156 |
| 2026-10-09 13:59:55 | `.tmp\_vk_baxis_probe_2026_10_09.py` | `5F55151BDC76` | 1832 |
| 2026-10-09 13:59:48 | `.tmp\_vk_pv02_recheck_c.py` | `7D35B715F8E2` | 2397 |
| 2026-10-09 13:59:19 | `.tmp\_vk_pv02_recheck_b.py` | `FE0F10E38BB3` | 1646 |
| 2026-10-09 13:59:08 | `.tmp\_vk_s4_topup_intake_recheck_2026_10_09.txt` | `683501B8FB41` | 7098 |
| 2026-10-09 13:58:59 | `.tmp\_vk_s4_topup_intake_recheck_2026_10_09.py` | `A1D8047F1833` | 6678 |
| 2026-10-09 13:58:44 | `.tmp\_vk_pv02_recheck_a.py` | `37D55BF0FBA6` | 4188 |
| 2026-10-09 13:55:13 | `results\_s4_topup_intake_recompute_register_2026_10_09.md` | `DFC9B0FBEF5A` | 32779 |
| 2026-10-09 13:53:50 | `.tmp\_s4_topup_addendum_verify_2026_10_09.txt` | `AABDEF1DA2B7` | 841 |
| 2026-10-09 13:53:09 | `results\_s4_substrate_topup_addendum_2026_10_09.json` | `1780542F0014` | 85861 |
| 2026-10-09 13:53:01 | `.tmp\_s4_topup_addendum_builder_2026_10_09.py` | `B9987C7A8D5F` | 21122 |
| 2026-10-09 13:50:48 | `.tmp\_s4_intake_recompute_readings_2026_10_09.txt` | `BB5EB15E9C1A` | 6641 |
| 2026-10-09 13:50:34 | `.tmp\_s4_intake_recompute_probe_2026_10_09.py` | `100A25F7E818` | 11175 |
| 2026-10-09 13:43:03 | `results\_v3_02_ethard_execution_register_2026_10_09.md` | `23457F5CE432` | 22007 |
| 2026-10-09 13:39:57 | `results\c5_b_group_fix_readings_2026_10_09.json` | `4E415990B71D` | 10029 |
| 2026-10-09 13:39:49 | `corpus\v20\index_v3_2026_10_09.json` | `74B27393574F` | 24837 |
| 2026-10-09 13:39:49 | `results\deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `95F3F0957BE8` | 21176 |
| 2026-10-09 13:38:56 | `.tmp\_c5_b_group_fix_readings_2026_10_09.py` | `B6855B38ACC2` | 12289 |
| 2026-10-09 13:38:37 | `deposon_team\plugins\_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | `7C095C54FB99` | 21826 |
| 2026-10-09 13:33:36 | `results\_v3_02_override_register_2026_10_09.md` | `C5441E186C3F` | 36245 |
| 2026-10-09 13:33:22 | `results\_s4_open_questions_design_2026_10_09.md` | `0186A4499BBC` | 31803 |
| 2026-10-09 13:31:17 | `.tmp\_s4oq_slug_search2_2026_10_09.py` | `FE6F7044EC4E` | 5258 |
| 2026-10-09 13:30:50 | `.tmp\_s4oq_slug_opt_2026_10_09.py` | `77D696B1690D` | 4636 |
| 2026-10-09 13:30:29 | `.tmp\_s4oq_cellmap_2026_10_09.py` | `C07589F292E1` | 1734 |
| 2026-10-09 13:30:18 | `.tmp\_s4oq_reuse_v2_2026_10_09.py` | `BC0F200EDD1E` | 6293 |
| 2026-10-09 13:29:55 | `.tmp\_s4oq_reuse_check_2026_10_09.py` | `952C76C5B103` | 6712 |
| 2026-10-09 13:29:42 | `.tmp\_s4oq_keyscan_2026_10_09.py` | `C9F94C812F7F` | 573 |
| 2026-10-09 13:29:34 | `.tmp\_s4oq_baseline_faces_2026_10_09.json` | `7DEB932BB35D` | 38835 |
| 2026-10-09 13:29:27 | `.tmp\_s4oq_build_baseline_2026_10_09.py` | `3CF28FE89611` | 3501 |
| 2026-10-09 12:45:09 | `results\_pending_pi_items_master_register_2026_10_09.md` | `87AB4929477F` | 35258 |
| 2026-10-09 12:38:16 | `.tmp\_rpd_verify_landed_2026_10_09.py` | `912A2B8066F1` | 6335 |
| 2026-10-09 12:37:13 | `results\_r_pair_question_texts_2026_10_09.md` | `0AD849022328` | 30352 |
| 2026-10-09 12:35:42 | `.tmp\_rpd_reuse_strict_2026_10_09.py` | `4557B47B7361` | 4746 |
| 2026-10-09 12:35:20 | `.tmp\_rpd_neighbors_2026_10_09.py` | `28CFA9466EA3` | 1286 |
| 2026-10-09 12:35:06 | `.tmp\_rpd_reuse_probe_2026_10_09.py` | `0A711147AC83` | 9280 |
| 2026-10-09 12:34:09 | `.tmp\_rpd_probe_b_2026_10_09.py` | `A7155D07B98B` | 1812 |
| 2026-10-09 12:33:55 | `.tmp\_rpd_probe_2026_10_09.py` | `B0E0EB00279B` | 2313 |
| 2026-10-09 12:33:36 | `results\_g4_e3_definition_independent_judgment_2026_10_09.md` | `AEBAFF5B503C` | 29094 |
| 2026-10-09 12:31:28 | `results\_r_pair_is_corr_coverage_design_2026_10_09.md` | `48F04FA39397` | 27208 |
| 2026-10-09 12:17:38 | `results\_ea_audit_batch_vk_2026_10_09.md` | `CE27DB55E0C5` | 19611 |
| 2026-10-09 12:09:39 | `results\_p_s4_1_revision_register_2026_10_09.md` | `AD5C76111570` | 29961 |
| 2026-10-09 12:09:24 | `results\_9model_merge_disposition_register_2026_10_09.md` | `455277298212` | 11651 |
| 2026-10-09 12:08:37 | `results\_9model_full_merge_from_4workers_2026_10_09.json` | `32AA0618A9D7` | 19337 |
| 2026-10-09 12:08:13 | `.tmp\_w5_9model_merge_2026_10_09.py` | `AFA52E90F332` | 18475 |
| 2026-10-09 12:06:13 | `results\_k_v3df_0_1_readings_verdict_2026_10_09.md` | `E98BEE353448` | 37003 |
| 2026-10-09 12:02:48 | `.tmp\vk_v3df_0_1_agree.py` | `84C090952894` | 6140 |
| 2026-10-09 12:01:29 | `.tmp\vk_v3df_0_1_materiality.py` | `B666B7A38082` | 2875 |
| 2026-10-09 12:01:06 | `.tmp\vk_v3df_0_1_coverage_gap.py` | `DF25000E7180` | 1971 |
| 2026-10-09 12:00:38 | `.tmp\vk_v3df_0_1_verify_out_2026_10_09.json` | `D6DCCC069511` | 30845 |
| 2026-10-09 12:00:28 | `.tmp\vk_v3df_0_1_verify_2026_10_09.py` | `0E7CB9348A16` | 14347 |
| 2026-10-09 11:54:29 | `results\_t1_qwen_temp_sweep_verdict_2026_10_09.md` | `DFC858D3D930` | 21672 |
| 2026-10-09 11:50:56 | `results\_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | `A14AAFA220C4` | 27735 |
| 2026-10-09 11:49:48 | `.tmp\_t1_verdict_probe_readonly.txt` | `0E2DF9CA7AB2` | 4655 |
| 2026-10-09 11:24:10 | `results\_k_v3df_0_1_four_readings_2026_10_09.md` | `53C28CA1AE3D` | 46522 |
| 2026-10-09 11:24:10 | `results\_k_v3df_0_1_four_readings_2026_10_09.json` | `E87937D55471` | 65507 |
| 2026-10-09 11:24:00 | `.tmp\k_v3df_0_1_four_readings_2026_10_09.py` | `2E990644CC8D` | 50232 |
| 2026-10-09 11:20:07 | `results\_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | `7AD31E741400` | 17341 |
| 2026-10-09 11:20:01 | `results\_protocol_version_landing_status_2026_10_09.md` | `1D1895489D17` | 11562 |
| 2026-10-09 11:17:05 | `.tmp\_t1_qwen_temp_sweep_decomposition.txt` | `2D96061318D9` | 1312 |
| 2026-10-09 11:16:56 | `.tmp\_t1_qwen_temp_sweep_decomposition.py` | `97A6520C7105` | 1981 |
| 2026-10-09 11:16:41 | `.tmp\_t1_qwen_temp_sweep_readings_table.txt` | `2E1BEC1E11A1` | 2042 |
| 2026-10-09 11:16:31 | `.tmp\_t1_qwen_temp_sweep_dump_readings.py` | `7E06567AFC2A` | 1137 |
| 2026-10-09 11:15:36 | `.tmp\_t1_qwen_temp_sweep_readings.json` | `E5E8F024E42E` | 11013 |
| 2026-10-09 11:15:15 | `.tmp\_t1_qwen_temp_sweep_retry.log` | `1A791E41BD4B` | 1757 |
| 2026-10-09 11:15:00 | `.tmp\_t1_qwen_temp_sweep_records.json` | `5B51AF62C640` | 96866 |
| 2026-10-09 11:11:23 | `.tmp\_t1_qwen_temp_sweep_run.log` | `EE6A1EE19548` | 8402 |
| 2026-10-09 11:07:19 | `results\_gap_closeout_status_2026_10_09.md` | `EA41E346C4C4` | 28793 |
| 2026-10-09 11:07:09 | `results\_g4_e3_definition_ruling_material_2026_10_09.md` | `8AE4016BB41D` | 30662 |
| 2026-10-09 11:00:13 | `results\_s4_topup_questionnaire_design_2026_10_09.md` | `B8F8F987F21B` | 38466 |
| 2026-10-09 10:59:27 | `results\_closing_round_9_decisions_register_2026_10_09.md` | `27118156A99A` | 2314 |
| 2026-10-09 10:57:41 | `.tmp\_s4td_cell_map_2026_10_09.py` | `6665669D858D` | 3642 |
| 2026-10-09 10:57:16 | `.tmp\_s4td_floor_bound_2026_10_09.py` | `AD95B6D5E9B9` | 4378 |
| 2026-10-09 10:56:36 | `.tmp\_s4td_reuse_and_bound_2026_10_09.py` | `AF6FDC892F60` | 8765 |
| 2026-10-09 10:55:52 | `.tmp\_s4td_slug_search_2026_10_09.py` | `CE5529EC7516` | 4657 |
| 2026-10-09 10:52:32 | `.tmp\_s4td_existing_faces.json` | `1009161547CF` | 36128 |
| 2026-10-09 10:52:22 | `.tmp\_s4td_grid_probe_2026_10_09.py` | `2C5DD849A2D0` | 6401 |
| 2026-10-09 10:50:06 | `.tmp\_s4td_existing_qindex.tsv` | `AD8C9E3C966B` | 14093 |
| 2026-10-09 10:23:35 | `.tmp\_t1_qwen_temp_sweep_probe_log.json` | `B5E4151AF490` | 445 |
| 2026-10-09 10:22:42 | `.tmp\_t1_qwen_temp_sweep_selfcert.json` | `91C2505DEEF3` | 3866 |
| 2026-10-09 10:22:20 | `results\_t1_qwen_temp_sweep_executor_2026_10_09.py` | `F0C845864603` | 32399 |
| 2026-10-09 10:21:25 | `results\_g4_reproduction_execution_register_2026_10_09.md` | `4DAAF68CBF0E` | 20414 |
| 2026-10-09 10:20:29 | `results\_s4_substrate_topup_collection_register_2026_10_09.md` | `33C1A818EF4F` | 18327 |
| 2026-10-09 10:17:54 | `.tmp\_s4fill_probe5.py` | `F55B9936088C` | 1333 |
| 2026-10-09 10:17:06 | `.tmp\_s4fill_probe4.py` | `61C287C9B2B7` | 796 |
| 2026-10-09 10:14:39 | `.tmp\_s4fill_probe3.py` | `DFB60C74FE3C` | 366 |
| 2026-10-09 10:13:59 | `.tmp\_s4fill_probe2.py` | `2FE506AB8A68` | 708 |
| 2026-10-09 10:13:27 | `.tmp\_s4fill_probe1.py` | `0F1BF6024884` | 401 |
| 2026-10-09 10:12:53 | `results\_closing_round_8_decisions_register_2026_10_09.md` | `A28A478E14A8` | 2151 |
| 2026-10-09 10:03:28 | `results\_e2_glm2_distill_side_receipt_register_2026_10_09.md` | `974124FC53F9` | 11336 |
| 2026-10-09 10:03:07 | `results\_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | `BDA5D5F3DFA0` | 16994 |
| 2026-10-09 09:59:56 | `results\_s4_daily_share_margin_prerequisite_2026_10_09.md` | `A929502E8421` | 18197 |
| 2026-10-09 09:58:23 | `.tmp\_v412_s4_daily_share_prereq_probe_2026_10_09.py` | `DA7EA40657F7` | 4823 |
| 2026-10-09 09:57:37 | `.tmp\_v412_unique_scan.py` | `B2E381F09828` | 1300 |
| 2026-10-09 09:57:19 | `.tmp\_v412_contrib.py` | `1085411B4896` | 1040 |
| 2026-10-09 09:56:56 | `.tmp\_v412_s3side_probe.py` | `60A3E0F59B6F` | 1412 |
| 2026-10-09 09:56:27 | `.tmp\_v412_m1_domain_probe.py` | `A59587EB5E3F` | 2524 |
| 2026-10-09 09:55:37 | `results\_c_reading_recompute_2026_10_09.md` | `95D7D23D24FD` | 21006 |
| 2026-10-09 09:55:00 | `.tmp\_v412_material_scan.py` | `F3493907CBE2` | 627 |
| 2026-10-09 09:47:38 | `results\_suspect17_release_move_register_2026_10_09.md` | `9A4D40BFCDC3` | 22351 |
| 2026-10-09 09:47:13 | `results\_theory_boundary_clone_sync_register_2026_10_09.md` | `1F9FD007649C` | 17528 |
| 2026-10-09 09:47:11 | `results\_g4_controlled_reproduction_design_2026_10_09.md` | `B1C7C24926BB` | 23675 |
| 2026-10-09 09:38:19 | `results\_u_closure_execution_register_2026_10_09.md` | `CBF0C9503284` | 12781 |
| 2026-10-09 09:31:31 | `results\_archive_ledger_rectification_register_2026_10_09.md` | `99359733EEF1` | 20933 |
| 2026-10-09 09:29:38 | `results\_closing_round_7_decisions_register_2026_10_09.md` | `D5976BFE23C6` | 3206 |
| 2026-10-09 09:28:19 | `results\_s4_reading_surface_and_authority_register_2026_10_09.md` | `0148B5271154` | 34405 |
| 2026-10-09 09:26:50 | `results\_backfill_rule_final_2026_10_09.md` | `3E97D5286760` | 34602 |

---

## §6 撞名／双副本／同一性专章

���������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������� **检索口径**：全仓（2557 件）按**大小写不敏感基名**分组，取组内 N>1 者。

### §6-1 结论

| 分支 | 组数 | 判读 |
|:--|:-:|:--|
| **同名异哈希（CONFLICT）** | **9** | 同名而内容不同 ⇒ ⛔ 0 判性质、0 删、0 合、0 改名 |
| **同哈希异名（同一性・SAME_IDENTITY）** | **3** | 同内容多份 ⇒ ⛔ **0 重复计数**（须在成果清单中作一件计） |
| 大小写异名双副本 | **0** | **结构上不可共存**（NTFS 默认大小写不敏感，承 U-09） |

### §6-2 CONFLICT 组逐对登记（同名・异 SHA-12）

**_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md** —— 2 份 / 2 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `739245682D40` | 26633 |
| `results\_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` | `BA4D07BD7000` | 26637 |

**check.py** —— 35 份 / 35 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `verifier\v1\check.py` | `03BC1ADFC82F` | 2976 |
| `verifier\v10\check.py` | `4FD5FDD754C0` | 5261 |
| `verifier\v11\check.py` | `3B8682A7E562` | 2767 |
| `verifier\v12\check.py` | `87C9C883E3BF` | 4142 |
| `verifier\v13\check.py` | `1159FACAB6DB` | 3495 |
| `verifier\v14\check.py` | `4BA223D2185D` | 3278 |
| `verifier\v15\check.py` | `BE0F2BBAB0A2` | 3231 |
| `verifier\v16\check.py` | `223082632A1D` | 2691 |
| `verifier\v17\check.py` | `679792BE51ED` | 2897 |
| `verifier\v18\check.py` | `6ABDDA4F7400` | 3180 |
| `verifier\v19\check.py` | `C53CF72D085B` | 1995 |
| `verifier\v2\check.py` | `AF3A78983537` | 2510 |
| `verifier\v20\check.py` | `9D0F1E950DEE` | 2790 |
| `verifier\v21\check.py` | `5E7D7435C4A3` | 3702 |
| `verifier\v22\check.py` | `F16BEAAE5675` | 2857 |
| `verifier\v23\check.py` | `9ECB25362C9A` | 2659 |
| `verifier\v24\check.py` | `E6C7513D54F3` | 3124 |
| `verifier\v25\check.py` | `CC6FF5453E06` | 2576 |
| `verifier\v26\check.py` | `C58A9652A42A` | 2595 |
| `verifier\v27\check.py` | `118524C7E808` | 2132 |
| `verifier\v28\check.py` | `B73A6B268F64` | 2201 |
| `verifier\v29\check.py` | `5923E2C379F6` | 2124 |
| `verifier\v3\check.py` | `02A5A86D38BF` | 2544 |
| `verifier\v30\check.py` | `2CF46F79A669` | 2565 |
| `verifier\v31\check.py` | `E5BB0020E500` | 2185 |
| `verifier\v32\check.py` | `399BFC743F24` | 2551 |
| `verifier\v33\check.py` | `32FEFC485326` | 6019 |
| `verifier\v34\check.py` | `0BBD226CD2AE` | 3715 |
| `verifier\v35\check.py` | `2130A5F5E1BF` | 2385 |
| `verifier\v4\check.py` | `F058E85C5383` | 3205 |
| `verifier\v5\check.py` | `3D776381F665` | 2255 |
| `verifier\v6\check.py` | `8366078A10E4` | 2757 |
| `verifier\v7\check.py` | `A70A68037D92` | 4300 |
| `verifier\v8\check.py` | `01B63B1A9C5F` | 3210 |
| `verifier\v9\check.py` | `5FAAD917D839` | 5352 |

**check.sh** —— 8 份 / 8 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `verifier\v36\check.sh` | `2212DCD98CD1` | 968 |
| `verifier\v37\check.sh` | `CED43B5F8800` | 1141 |
| `verifier\v38\check.sh` | `43B501C5C20D` | 1705 |
| `verifier\v39\check.sh` | `D48AC555761F` | 1935 |
| `verifier\v40\check.sh` | `7B15CD2F4C7E` | 1604 |
| `verifier\v41\check.sh` | `2C9FE869DAAA` | 1687 |
| `verifier\v42\check.sh` | `3EA87E2CFC61` | 1509 |
| `verifier\v43\check.sh` | `71B83217032D` | 1224 |

**erratum.md** —— 2 份 / 2 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `verifier\v17\erratum.md` | `50F15F7EA3DC` | 438 |
| `verifier\v20\erratum.md` | `35081D39F35B` | 316 |

**executor_2026_09_27.py** —— 5 份 / 5 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `results\_v3_recheck_08b_executor\executor_2026_09_27.py` | `B292410D9A69` | 43901 |
| `results\_v3_recheck_08c_preexp_data\executor_2026_09_27.py` | `CB6EB9164DF3` | 37775 |
| `results\_v3_s_phrasetemplate_preexp_data\executor_2026_09_27.py` | `96F491A8E2BF` | 35555 |
| `results\_v3_s1_executor\executor_2026_09_27.py` | `10870941C283` | 54937 |
| `results\_v3_s2_executor\executor_2026_09_27.py` | `F1E272A0924A` | 84993 |

**readme.md** —— 2 份 / 2 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `README.md` | `A80B3DB006A5` | 7279 |
| `verifier\README.md` | `D76F2DC473BE` | 14360 |

**rescript_2026_09_27.md** —— 5 份 / 5 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `results\_v3_recheck_08b_executor\rescript_2026_09_27.md` | `78F3ABA1F24C` | 18501 |
| `results\_v3_recheck_08c_preexp_data\rescript_2026_09_27.md` | `035AF77DB626` | 17069 |
| `results\_v3_s_phrasetemplate_preexp_data\rescript_2026_09_27.md` | `D42EA1FA61F1` | 17574 |
| `results\_v3_s1_executor\rescript_2026_09_27.md` | `9D49A632EE81` | 17253 |
| `results\_v3_s2_executor\rescript_2026_09_27.md` | `FF0F964BE8AA` | 25151 |

**result_2026_09_27.json** —— 5 份 / 5 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `results\_v3_recheck_08b_executor\result_2026_09_27.json` | `F9A7FA2D65B1` | 88052 |
| `results\_v3_recheck_08c_preexp_data\result_2026_09_27.json` | `689A6E4427A8` | 146601 |
| `results\_v3_s_phrasetemplate_preexp_data\result_2026_09_27.json` | `FAE3C4640507` | 36844 |
| `results\_v3_s1_executor\result_2026_09_27.json` | `BFC99C3133DD` | 24975 |
| `results\_v3_s2_executor\result_2026_09_27.json` | `D73D51E670DE` | 51039 |

**test_write.txt** —— 2 份 / 2 个互异 SHA-12

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `.mavis\scripts\kt_a1\test_write.txt` | `9F86D081884C` | 4 |
| `.mavis\scripts\kt_c1\test_write.txt` | `85D443E165BB` | 7 |

### §6-3 SAME_IDENTITY 组（同哈希・异名/异位）

**_inspect_captions.py** —— 2 份 / SHA-12 全等 DFB02ADE1474  

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `corpus\v20_caption_surface\_inspect_captions.py` | `DFB02ADE1474` | 591 |
| `results\_archive_2026_09_24\_inspect_captions.py` | `DFB02ADE1474` | 591 |

**index_v2_2026_09_16.json** —— 2 份 / SHA-12 全等 EFE05AD775DE  

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `corpus\v20\by_model\kimi\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 |
| `corpus\v20\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 |

**strip_captions_22.json** —— 2 份 / SHA-12 全等 6A2656878745  

| 相对路径 | SHA-12 | bytes |
|:--|:--|-:|
| `corpus\v20\strip_captions_22.json` | `6A2656878745` | 12798 |
| `corpus\v20_caption_surface\strip_captions_22.json` | `6A2656878745` | 12798 |

### §6-4 跨名同哈希全量（14 组 / 28 件）—— 含异名之同一性

| SHA-12 | 件数 | bytes | 相对路径 |
|:--|:-:|-:|:--|
| `169D160BA600` | 2 | 4630 | `.tmp\_s4_refreeze179_enumerate_probe_2026_10_09_v1_dead.py`<br>`.tmp\_s4_refreeze179_enumerate_probe2_2026_10_09.py` |
| `43D9CE160FC8` | 2 | 2460 | `results\boss_pc_1_real_2d_ising_2026_09_15.json`<br>`results\boss_pe_1_real_2d_ising_2026_09_15.json` |
| `4AA127D1DC62` | 2 | 5088 | `.tmp\_card23_readout_utf8.txts`<br>`.tmp\card23_readout_utf8.txt` |
| `68C85CF076D1` | 2 | 2634 | `.tmp\_recheck_r1_runA.log`<br>`.tmp\_recheck_r1_runB.log` |
| `6A2656878745` | 2 | 12798 | `corpus\v20\strip_captions_22.json`<br>`corpus\v20_caption_surface\strip_captions_22.json` |
| `8933D61B180A` | 2 | 3553 | `results\boss_pc_2_real_transverse_ising_2026_09_15.json`<br>`results\boss_pe_2_real_transverse_ising_2026_09_15.json` |
| `94B5398BE76C` | 2 | 2364 | `results\boss_pc_3_real_reservoir_2026_09_15.json`<br>`results\boss_pe_3_real_reservoir_2026_09_15.json` |
| `9DE3C08E3863` | 2 | 31138 | `.tmp\_s5dp_five_lines_runner_third_2026_10_11.py`<br>`results\_s5doubleprime_five_lines_runner_2026_10_11.py` |
| `B15384CFF9F0` | 2 | 2568 | `.tmp\_recheck_r1_runC.log`<br>`.tmp\_recheck_r1_runD.log` |
| `C68076C88140` | 2 | 26253 | `results\_v5_gt8_lowarm_result_2026_09_29.json`<br>`results\_v5_gt8_lowarm_result_2026_09_29_cb132cd5.json` |
| `DFB02ADE1474` | 2 | 591 | `corpus\v20_caption_surface\_inspect_captions.py`<br>`results\_archive_2026_09_24\_inspect_captions.py` |
| `E3B0C44298FC` | 2 | 0 | `.tmp\_ci_gap_fill_err.txt`<br>`results\_v4_supp_l14v3_batch2_r2_models_probe.err.log` |
| `EFE05AD775DE` | 2 | 24150 | `corpus\v20\by_model\kimi\index_v2_2026_09_16.json`<br>`corpus\v20\index_v2_2026_09_16.json` |
| `FDFE315FF54A` | 2 | 174424 | `.tmp\_v16_full_decoded.txt`<br>`.tmp\_v16_tail_dump.txt` |

---

## §7 编码异常专章（BOM ／ CR 计数 —— **字节级实测**）

> 📌 **测量仪器声明**：BOM ＝ 验**前三字节** `EF BB BF`（`[System.IO.File]::Open`＋`Read(3)`）；CR 计数 ＝ **以 Latin-1(28591) 逐块读取全字节流、统计 `0x0D` 个数**。⛔ **0 用 `grep -c $'\r'`**（其对 byte-identical 之 LF 件**假阳性**）。

### §7-1 总览

| 目录 | 件数 | BOM 件 | CR>0 件 | BOM 且 CR>0 | BOM 且 CR=0 |
|:--|-:|-:|-:|-:|-:|
| .mavis/ | 4 | 0 | 0 | 0 | 0 |
| .tmp/ | 581 | 113 | 188 | 99 | 14 |
| .trae/ | 2 | 0 | 0 | 0 | 0 |
| attacks/ | 4 | 0 | 0 | 0 | 0 |
| corpus/ | 43 | 0 | 15 | 0 | 0 |
| deposon_team/ | 86 | 4 | 20 | 4 | 0 |
| docs/ | 135 | 0 | 11 | 0 | 0 |
| letters/ | 97 | 0 | 2 | 0 | 0 |
| paper/ | 5 | 0 | 0 | 0 | 0 |
| results/ | 1341 | 5 | 210 | 4 | 1 |
| reviews/ | 32 | 0 | 0 | 0 | 0 |
| scripts/ | 10 | 0 | 1 | 0 | 0 |
| tests/ | 23 | 0 | 0 | 0 | 0 |
| tools/ | 5 | 0 | 0 | 0 | 0 |
| verifier/ | 116 | 0 | 18 | 0 | 0 |
| （顶层） | 0 | 0 | 0 | 0 | 0 |
| **合计** | **2557** | **122** | **465** | **107** | **15** |

📌 **测量失败件数 ＝ 0**（全仓 2,557 件之 BOM／CR／SHA-256 **均实测成功**）。

### §7-2 BOM 件逐件登记（122 件）

| 相对路径 | SHA-12 | bytes | CR 计数 |
|:--|:--|-:|-:|
| `.tmp\_audit_part3_out.txt` | `85A9D9861D38` | 5195 | 144 |
| `.tmp\_c5_b_prestate_baseline.json` | `09F27C6C1869` | 1543 | 1 |
| `.tmp\_c5_b3_rewalk_postcheck_2026_10_01.py` | `ACA7DAD6DDFA` | 2249 | 1 |
| `.tmp\_c5_b3_rewalk_precheck_2026_10_01.py` | `4AAD531A2DDB` | 2035 | 1 |
| `.tmp\_c5_b3_rewalk_utf8check_2026_10_01.py` | `5488FF2DB11F` | 925 | 1 |
| `.tmp\_c5_b3_utf8_out.txt` | `29DE7D0ACF02` | 933 | 8 |
| `.tmp\_c5_feasibility_probe.py` | `D730612B0C9A` | 1036 | 1 |
| `.tmp\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | `B0CF9BABA64B` | 20997 | 0 |
| `.tmp\_d05_detail.txt` | `6CB5D73BD8DA` | 3017 | 12 |
| `.tmp\_dump_dkb3_records2_2026_10_10.py` | `E71D1E81DA64` | 1366 | 1 |
| `.tmp\_en_final_2026_09_28.py` | `97A05AACE5A8` | 2369 | 1 |
| `.tmp\_en_verify_2026_09_28.py` | `51D9410D459B` | 6071 | 1 |
| `.tmp\_en_verify2_2026_09_28.py` | `7E84E75CB838` | 1870 | 1 |
| `.tmp\_en_verify3_2026_09_28.py` | `658292CCE916` | 1638 | 1 |
| `.tmp\_en_verify4_2026_09_28.py` | `7EAEB9B4BA48` | 1484 | 0 |
| `.tmp\_hash21.py` | `0D5335F0AC54` | 944 | 1 |
| `.tmp\_probe_schema.py` | `D9A4F1898C31` | 583 | 1 |
| `.tmp\_probe21.py` | `5A40370032B3` | 564 | 1 |
| `.tmp\_r1_scratch_bom.json` | `339DE051E817` | 17 | 0 |
| `.tmp\_r4_cleanup_worker_keyscan_2026_09_29.py` | `01E1AC2EF239` | 3561 | 0 |
| `.tmp\_rj5_convention_check_2026_09_27.out.json` | `C88E4BA1A4CE` | 8983 | 241 |
| `.tmp\_rj5_mapping_test_2026_09_27.out.txt` | `796E3A8B432F` | 1384 | 21 |
| `.tmp\_rp_post_probe_2026_10_09.py` | `AB6B1AA8BE4B` | 3641 | 1 |
| `.tmp\_rp_verify_2026_10_09.py` | `E0ADAE15FC26` | 3282 | 1 |
| `.tmp\_rp4_fields.py` | `1D112AB8F3B4` | 433 | 1 |
| `.tmp\_rp4_probe_all_r.py` | `90023E831E24` | 1152 | 1 |
| `.tmp\_rp4_probe_r_axes.py` | `CF0534F24D4E` | 528 | 1 |
| `.tmp\_rp4_probe_r7.py` | `249951837E6E` | 676 | 1 |
| `.tmp\_rp4_probe_r78.py` | `6208A3327CF3` | 807 | 1 |
| `.tmp\_rp4_probe_r7b.py` | `F3BE733BF87A` | 453 | 1 |
| `.tmp\_rp4_probe_r7c.py` | `D65F18FFB59A` | 643 | 1 |
| `.tmp\_run_output.log` | `F5FE18205E3D` | 1420 | 23 |
| `.tmp\_s4f2_dbg.py` | `5159C9C30180` | 431 | 1 |
| `.tmp\_s4f2_manifest_post.txt` | `8824ECE12D30` | 130975 | 929 |
| `.tmp\_s4f2_manifest_pre.txt` | `8650EA333291` | 130701 | 927 |
| `.tmp\_s4f2_patch.py` | `B79A7073099D` | 2740 | 1 |
| `.tmp\_s4f2_patch2.py` | `045BD90B237A` | 421 | 1 |
| `.tmp\_s4f2_patch3.py` | `6D57FF4CE76C` | 815 | 1 |
| `.tmp\_s4f2_patch4.py` | `7D85756A841D` | 565 | 1 |
| `.tmp\_s4f2_probe_out.txt` | `B8F1E47BA331` | 9943 | 164 |
| `.tmp\_s4f2_probe2_out.txt` | `44C9D5176D12` | 9414 | 90 |
| `.tmp\_s4f2_probe3_out.txt` | `959372C08EFF` | 6228 | 75 |
| `.tmp\_s4f2_scanner_selftest.py` | `5B6FD262F785` | 1819 | 1 |
| `.tmp\_s4fill_probe1.py` | `0F1BF6024884` | 401 | 1 |
| `.tmp\_s4fill_probe2.py` | `2FE506AB8A68` | 708 | 1 |
| `.tmp\_s4fill_probe3.py` | `DFB60C74FE3C` | 366 | 1 |
| `.tmp\_s4fill_probe4.py` | `61C287C9B2B7` | 796 | 1 |
| `.tmp\_s4fill_probe5.py` | `F55B9936088C` | 1333 | 1 |
| `.tmp\_s4oq_addendum_struct_2026_10_09.py` | `67652ACDF681` | 843 | 1 |
| `.tmp\_s4oq_build_draft_2026_10_09.py` | `0797D19DCAF3` | 8719 | 1 |
| `.tmp\_s4oq_entryclass_probe_2026_10_09.py` | `2B9AD9A3EB8E` | 771 | 1 |
| `.tmp\_s4oq_final_verify_2026_10_09.py` | `944A4F7006C8` | 959 | 1 |
| `.tmp\_s4oq_forward_2026_10_09.py` | `43E72C62587D` | 3482 | 1 |
| `.tmp\_s4oq_grid_cmp_2026_10_09.py` | `F00865587D6A` | 1601 | 1 |
| `.tmp\_s4oq_grid_diag_2026_10_09.py` | `082E8B8B7BC4` | 1553 | 1 |
| `.tmp\_s4oq_grid_recompute_2026_10_09.py` | `AFB613F5CED1` | 2394 | 1 |
| `.tmp\_s4oq_keyscan_2026_10_09.py` | `C9F94C812F7F` | 573 | 1 |
| `.tmp\_s4oq_read_db_probe_2026_10_09.py` | `5926143C8A6D` | 658 | 1 |
| `.tmp\_s4oq_recompute_2026_10_09.py` | `07CDEC653345` | 3202 | 1 |
| `.tmp\_s4oq_skel_2026_10_09.py` | `73FC780B4849` | 466 | 1 |
| `.tmp\_s4oq_variants_2026_10_09.py` | `CCBBB499E19A` | 1233 | 1 |
| `.tmp\_s4oq_verify_addendum_2026_10_09.py` | `419C15A7A2C5` | 2252 | 1 |
| `.tmp\_s4oq_write_addendum_2026_10_09.py` | `63E61AFA6517` | 11886 | 1 |
| `.tmp\_s4td_existing_qindex.tsv` | `AD8C9E3C966B` | 14093 | 149 |
| `.tmp\_s5dp_run_stdout_2026_10_11.txt` | `13F90AAFAB80` | 7256 | 94 |
| `.tmp\_t1_qwen_temp_sweep_retry.log` | `1A791E41BD4B` | 1757 | 42 |
| `.tmp\_t1_qwen_temp_sweep_run.log` | `EE6A1EE19548` | 8402 | 174 |
| `.tmp\_t15_inspect3_out.txt` | `56F1909CD962` | 1588 | 15 |
| `.tmp\_t15_inspect4_out.txt` | `BA65EC451865` | 3057 | 48 |
| `.tmp\_t15_inspect5_out.txt` | `E632FEB9AD99` | 933 | 7 |
| `.tmp\_t15_inspect6_out.txt` | `194F2AC92089` | 6659 | 57 |
| `.tmp\_t15_inspect7_out.txt` | `5D51DCAD59D1` | 3647 | 40 |
| `.tmp\_t15_percell.txt` | `95D32BED4C21` | 491 | 10 |
| `.tmp\_t15_percell_out.txt` | `CBEC28A08723` | 772 | 6 |
| `.tmp\_v412_contrib.py` | `1085411B4896` | 1040 | 1 |
| `.tmp\_v412_m1_domain_probe.py` | `A59587EB5E3F` | 2524 | 1 |
| `.tmp\_v412_material_scan.py` | `F3493907CBE2` | 627 | 1 |
| `.tmp\_v412_s3side_probe.py` | `60A3E0F59B6F` | 1412 | 1 |
| `.tmp\_v412_unique_scan.py` | `B2E381F09828` | 1300 | 1 |
| `.tmp\_verify_dual_probe1_2026_10_09.py` | `E42CF6C832BF` | 5671 | 0 |
| `.tmp\_verify_dual_probe2_2026_10_09.py` | `18261CBDE500` | 2453 | 0 |
| `.tmp\_verify_dual_probe3_2026_10_09.py` | `E6BDD2712A13` | 2943 | 0 |
| `.tmp\_verify_dual_probe3b_2026_10_09.py` | `61F84109FC1F` | 2194 | 0 |
| `.tmp\_verify_dual_probe4_2026_10_09.py` | `4AE5BE9872A1` | 3374 | 0 |
| `.tmp\_verify_dual_probe5_2026_10_09.py` | `605F4E963169` | 3160 | 0 |
| `.tmp\_verify_dual_probe6_2026_10_09.py` | `35D6E8C4F838` | 3227 | 0 |
| `.tmp\_verify_dual_probe7_2026_10_09.py` | `3EBBF43ECDAF` | 2795 | 0 |
| `.tmp\_verify_dual_probe8_2026_10_09.py` | `F40D20D0794F` | 2396 | 0 |
| `.tmp\_verify_dual_probe9_2026_10_09.py` | `A4467A8A7118` | 1722 | 0 |
| `.tmp\_verify_r32_card_2026_10_10.py` | `61F99FC5FDB9` | 631 | 1 |
| `.tmp\_vk_baxis_probe_2026_10_09.py` | `5F55151BDC76` | 1832 | 1 |
| `.tmp\_vk_dualread_probe_2026_10_09.py` | `A2C315831EFE` | 3240 | 1 |
| `.tmp\_vk_pv02_recheck_a.py` | `37D55BF0FBA6` | 4188 | 1 |
| `.tmp\_vk_pv02_recheck_b.py` | `FE0F10E38BB3` | 1646 | 1 |
| `.tmp\_vk_pv02_recheck_c.py` | `7D35B715F8E2` | 2397 | 1 |
| `.tmp\_vk_pv02_recheck_d.py` | `7AE7ED6BCD8A` | 982 | 1 |
| `.tmp\_vk_pv02_recheck_e.py` | `D925E60C1D3C` | 1742 | 1 |
| `.tmp\_vk_pv02_recheck_f.py` | `C2E298CCEBC6` | 1522 | 1 |
| `.tmp\_vk_pv02_recheck_g.py` | `F237E1D2715F` | 2269 | 1 |
| `.tmp\_vk_q.py` | `67364902116C` | 519 | 1 |
| `.tmp\_vk_q2.py` | `D5759D40DC43` | 540 | 1 |
| `.tmp\_vk_q3.py` | `A00CD309205F` | 612 | 1 |
| `.tmp\_vk_q4.py` | `DEFC3C53B7DF` | 784 | 1 |
| `.tmp\_vk_q5.py` | `7B95307225BA` | 1246 | 1 |
| `.tmp\_vk_q6.py` | `7DA34DD24EB0` | 811 | 1 |
| `.tmp\_vk_q7.py` | `A6C525F88F11` | 1331 | 1 |
| `.tmp\_vk_q8.py` | `5A81E5558C72` | 1025 | 1 |
| `.tmp\e4_axis2_run_out.json` | `536080B19999` | 3514 | 152 |
| `.tmp\e4_axis2_validation_out.json` | `5B3EF39DC114` | 2657 | 170 |
| `.tmp\gate_check.py` | `ABE7FBDB394B` | 648 | 1 |
| `.tmp\gate_check2.py` | `7025CECEB766` | 840 | 1 |
| `.tmp\kro_extract.py` | `B5731ABAE41F` | 802 | 1 |
| `.tmp\pa_block.py` | `19AC8C59439B` | 345 | 1 |
| `deposon_team\plugins\_verify_15frozen.py` | `EFAE9274962E` | 3905 | 1 |
| `deposon_team\plugins\_verify_15frozen_v1.py` | `60523E406055` | 2094 | 1 |
| `deposon_team\plugins\_verify_pg_v0.py` | `CDD3415AD993` | 3978 | 1 |
| `deposon_team\plugins\_verify_pg_v0_v1.py` | `67088AE1A860` | 2521 | 1 |
| `results\_archive_2026_09_21\_archive_manifest_2026_09_21.json` | `33FE31633DA8` | 17353 | 442 |
| `results\_v3x_conservation_anchor_2026_09_17.txt` | `F331A9C2BD22` | 940 | 1 |
| `results\_v3x_d0_5_aggregation_2026_09_17.md` | `DDF0D1AA96D2` | 12010 | 1 |
| `results\_v3x_p_l_v3_external_spec_2026_09_17.md` | `6A5B6EB635F0` | 5769 | 1 |
| `results\_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md` | `41D29F4DEB70` | 42157 | 0 |

📌 **`.tmp` 以外之 BOM 件（9 件）** —— ⛔ **仅登记，0 代修**（冻结内只登记）：`deposon_team/plugins/_verify_15frozen.py`、`_verify_15frozen_v1.py`、`_verify_pg_v0.py`、`_verify_pg_v0_v1.py`；`results/_archive_2026_09_21/_archive_manifest_2026_09_21.json`（CR=442）、`results/_v3x_conservation_anchor_2026_09_17.txt`、`results/_v3x_d0_5_aggregation_2026_09_17.md`、`results/_v3x_p_l_v3_external_spec_2026_09_17.md`、`results/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md`（BOM 且 CR=0）。

### §7-3 CR>0 件逐件登记（465 件）

| 相对路径 | SHA-12 | bytes | CR 计数 |
|:--|:--|-:|-:|
| `.tmp\__pycache__\_abc_readings_reprocheck_2026_10_10.cpython-314.pyc` | `18EF2E6B1FEF` | 15886 | 60 |
| `.tmp\__pycache__\_s4_heldout_items_exec.cpython-314.pyc` | `8FE2DDA7646C` | 22922 | 83 |
| `.tmp\__pycache__\_s4_heldout_seed42_probe_2026_10_09.cpython-314.pyc` | `C6999C34D697` | 18870 | 62 |
| `.tmp\__pycache__\_s5dp_five_lines_runner_third_2026_10_11.cpython-314.pyc` | `01A31E74A420` | 44946 | 187 |
| `.tmp\__pycache__\s4_regen_runner.cpython-314.pyc` | `31DD999DF336` | 21608 | 81 |
| `.tmp\_abc_final_2026_10_10.json` | `5F4C2F499620` | 1291 | 58 |
| `.tmp\_abc_h1h2_out_2026_10_10.json` | `068BE36A60D8` | 4922 | 249 |
| `.tmp\_abc_readings_reprocheck_out_2026_10_10.json` | `2F9AA16B63CA` | 78436 | 5366 |
| `.tmp\_audit_part3_out.txt` | `85A9D9861D38` | 5195 | 144 |
| `.tmp\_audit_part4.txt` | `DEF27C1C3511` | 14826 | 191 |
| `.tmp\_audit3b.txt` | `E64565A2B180` | 50554 | 699 |
| `.tmp\_c5_b_prestate_baseline.json` | `09F27C6C1869` | 1543 | 1 |
| `.tmp\_c5_b3_rewalk_postcheck_2026_10_01.py` | `ACA7DAD6DDFA` | 2249 | 1 |
| `.tmp\_c5_b3_rewalk_precheck_2026_10_01.py` | `4AAD531A2DDB` | 2035 | 1 |
| `.tmp\_c5_b3_rewalk_utf8check_2026_10_01.py` | `5488FF2DB11F` | 925 | 1 |
| `.tmp\_c5_b3_utf8_out.txt` | `29DE7D0ACF02` | 933 | 8 |
| `.tmp\_c5_feasibility_probe.py` | `D730612B0C9A` | 1036 | 1 |
| `.tmp\_card23_readout_utf8.txts` | `4AA127D1DC62` | 5088 | 42 |
| `.tmp\_cards_35_48_full.txt` | `8D99789C1999` | 120330 | 474 |
| `.tmp\_ci_gap_fill_alt_bc_aper_prime_2026_10_09.log` | `F258AE241DEB` | 2360 | 22 |
| `.tmp\_ci_gap_fill_out.txt` | `353DC9DF9650` | 11040 | 79 |
| `.tmp\_cpatomic_keyscan_2026_09_28.json` | `B4E45CFFA5CD` | 2672 | 115 |
| `.tmp\_cpatomic_patch_manifest_2026_09_28.json` | `CDB8EBC2ECE3` | 357 | 13 |
| `.tmp\_cpatomic_pycache_post_2026_09_28.json` | `1EB3C5C9C62D` | 6476 | 240 |
| `.tmp\_cpatomic_pycache_pre_2026_09_28.json` | `0F62453472B7` | 10772 | 383 |
| `.tmp\_cpatomic_register_2026_09_28.json` | `B68D7FF817BB` | 29361 | 1010 |
| `.tmp\_cpatomic_verify_2026_09_28.json` | `6B820F7DA4A4` | 3144 | 117 |
| `.tmp\_d05_caliber_out_2026_10_10.json` | `080606669599` | 1725 | 108 |
| `.tmp\_d05_detail.txt` | `6CB5D73BD8DA` | 3017 | 12 |
| `.tmp\_d05_s4only_out_2026_10_10.json` | `FA0907234347` | 427 | 28 |
| `.tmp\_d05_three_checks_recheck_out_2026_10_10.json` | `4EB425260682` | 3622 | 189 |
| `.tmp\_d4_relabel_run1.log` | `97B5245DEAC3` | 1158 | 19 |
| `.tmp\_diff21_anchor_drift.txt` | `FB648F327945` | 20994 | 275 |
| `.tmp\_dump_dkb3_records2_2026_10_10.py` | `E71D1E81DA64` | 1366 | 1 |
| `.tmp\_e3536.txt` | `E28953F7623B` | 2248 | 8 |
| `.tmp\_e6_alt_permp_closure_raw_2026_10_10.json` | `C48395E135FD` | 8345 | 361 |
| `.tmp\_e6_ndjt_recompute_out_2026_10_10.json` | `6499760993BF` | 7005 | 315 |
| `.tmp\_en_final_2026_09_28.py` | `97A05AACE5A8` | 2369 | 1 |
| `.tmp\_en_verify_2026_09_28.py` | `51D9410D459B` | 6071 | 1 |
| `.tmp\_en_verify2_2026_09_28.py` | `7E84E75CB838` | 1870 | 1 |
| `.tmp\_en_verify3_2026_09_28.py` | `658292CCE916` | 1638 | 1 |
| `.tmp\_exp03_blade_recompute_out_2026_10_10.json` | `3D7DE35263F8` | 19719 | 850 |
| `.tmp\_final_sha.txt` | `548D466D81A9` | 611 | 6 |
| `.tmp\_gaps.txt` | `3F03D0608731` | 435 | 7 |
| `.tmp\_gaps2.txt` | `4D899338B548` | 2377 | 21 |
| `.tmp\_hash21.py` | `0D5335F0AC54` | 944 | 1 |
| `.tmp\_kv3s43_diag_out.txt` | `24CE4995AA09` | 2378 | 10 |
| `.tmp\_kv3s43_frozen_recompute_readings_2026_10_09.txt` | `2F20780CB7A6` | 13244 | 88 |
| `.tmp\_kv3s43_frozen_recompute_readings2_2026_10_09.txt` | `FC3BA9FE051B` | 7100 | 64 |
| `.tmp\_kv3s43_frozen_recompute_readings3_2026_10_09.txt` | `3AD13513E25C` | 7370 | 65 |
| `.tmp\_l14v3_aggregated_10cells.json` | `6F09512818F0` | 634458 | 12712 |
| `.tmp\_l14v3_aggregated_10cells_v4.json` | `66A9B8B3DABF` | 2233138 | 45109 |
| `.tmp\_l14v3_n26_metrics.json` | `80C5ECCF4630` | 1445 | 54 |
| `.tmp\_l14v3_n26_metrics_v2.json` | `EB9CE9683AD3` | 2579 | 98 |
| `.tmp\_l14v3_sensitivity_v2.json` | `DCAA4B6B3B0B` | 2292 | 104 |
| `.tmp\_payload.json` | `BE0A4F54AADE` | 42672 | 2078 |
| `.tmp\_pk_probe.py` | `6D79BA939526` | 398 | 1 |
| `.tmp\_pk_probe2.py` | `CAEA18365BE2` | 352 | 1 |
| `.tmp\_pk_probe3.py` | `4C1BAB003027` | 462 | 1 |
| `.tmp\_pk_probe4.py` | `999D874CEAAF` | 176 | 1 |
| `.tmp\_pk_probe5.py` | `1A3C047F383A` | 338 | 1 |
| `.tmp\_pk_probe8.py` | `B292C8B9152E` | 1636 | 1 |
| `.tmp\_postcheck_v16_alt_stdout.txt` | `F116B23FA967` | 1558 | 16 |
| `.tmp\_probe_schema.py` | `D9A4F1898C31` | 583 | 1 |
| `.tmp\_probe21.py` | `5A40370032B3` | 564 | 1 |
| `.tmp\_r10.txt` | `7F96AA9BB271` | 3867 | 23 |
| `.tmp\_r11_ctx.txt` | `25E2C97E9A17` | 4106 | 52 |
| `.tmp\_r4_cleanup_worker_keyscan_results_2026_09_29.json` | `F3E8AE7A6DB9` | 75 | 4 |
| `.tmp\_r4_key_scan_r1_files_2026_09_27.json` | `CEE49AA2F482` | 2313 | 91 |
| `.tmp\_r4_key_scan_results_2026_09_24.json` | `B03B348FD3DA` | 1014 | 51 |
| `.tmp\_r6_evidence.txt` | `EAED8C0A509E` | 30834 | 217 |
| `.tmp\_recheck_r1_run1.log` | `80B338A0E9AD` | 2486 | 45 |
| `.tmp\_recheck_r1_runA.log` | `68C85CF076D1` | 2634 | 45 |
| `.tmp\_recheck_r1_runB.log` | `68C85CF076D1` | 2634 | 45 |
| `.tmp\_recheck_r1_runC.log` | `B15384CFF9F0` | 2568 | 45 |
| `.tmp\_recheck_r1_runD.log` | `B15384CFF9F0` | 2568 | 45 |
| `.tmp\_rj5_convention_check_2026_09_27.out.json` | `C88E4BA1A4CE` | 8983 | 241 |
| `.tmp\_rj5_mapping_test_2026_09_27.out.txt` | `796E3A8B432F` | 1384 | 21 |
| `.tmp\_rp_post_probe_2026_10_09.py` | `AB6B1AA8BE4B` | 3641 | 1 |
| `.tmp\_rp_verify_2026_10_09.py` | `E0ADAE15FC26` | 3282 | 1 |
| `.tmp\_rp4_fields.py` | `1D112AB8F3B4` | 433 | 1 |
| `.tmp\_rp4_probe_all_r.py` | `90023E831E24` | 1152 | 1 |
| `.tmp\_rp4_probe_r_axes.py` | `CF0534F24D4E` | 528 | 1 |
| `.tmp\_rp4_probe_r7.py` | `249951837E6E` | 676 | 1 |
| `.tmp\_rp4_probe_r78.py` | `6208A3327CF3` | 807 | 1 |
| `.tmp\_rp4_probe_r7b.py` | `F3BE733BF87A` | 453 | 1 |
| `.tmp\_rp4_probe_r7c.py` | `D65F18FFB59A` | 643 | 1 |
| `.tmp\_run_output.log` | `F5FE18205E3D` | 1420 | 23 |
| `.tmp\_s4_freeze_rpair_readings_2026_10_09.txt` | `C2276232B04A` | 14312 | 22 |
| `.tmp\_s4f2_dbg.py` | `5159C9C30180` | 431 | 1 |
| `.tmp\_s4f2_manifest_post.txt` | `8824ECE12D30` | 130975 | 929 |
| `.tmp\_s4f2_manifest_pre.txt` | `8650EA333291` | 130701 | 927 |
| `.tmp\_s4f2_patch.py` | `B79A7073099D` | 2740 | 1 |
| `.tmp\_s4f2_patch2.py` | `045BD90B237A` | 421 | 1 |
| `.tmp\_s4f2_patch3.py` | `6D57FF4CE76C` | 815 | 1 |
| `.tmp\_s4f2_patch4.py` | `7D85756A841D` | 565 | 1 |
| `.tmp\_s4f2_probe_out.txt` | `B8F1E47BA331` | 9943 | 164 |
| `.tmp\_s4f2_probe2_out.txt` | `44C9D5176D12` | 9414 | 90 |
| `.tmp\_s4f2_probe3_out.txt` | `959372C08EFF` | 6228 | 75 |
| `.tmp\_s4f2_scanner_selftest.py` | `5B6FD262F785` | 1819 | 1 |
| `.tmp\_s4fill_probe1.py` | `0F1BF6024884` | 401 | 1 |
| `.tmp\_s4fill_probe2.py` | `2FE506AB8A68` | 708 | 1 |
| `.tmp\_s4fill_probe3.py` | `DFB60C74FE3C` | 366 | 1 |
| `.tmp\_s4fill_probe4.py` | `61C287C9B2B7` | 796 | 1 |
| `.tmp\_s4fill_probe5.py` | `F55B9936088C` | 1333 | 1 |
| `.tmp\_s4oq_addendum_struct_2026_10_09.py` | `67652ACDF681` | 843 | 1 |
| `.tmp\_s4oq_baseline_faces_2026_10_09.json` | `7DEB932BB35D` | 38835 | 1342 |
| `.tmp\_s4oq_build_draft_2026_10_09.py` | `0797D19DCAF3` | 8719 | 1 |
| `.tmp\_s4oq_entryclass_probe_2026_10_09.py` | `2B9AD9A3EB8E` | 771 | 1 |
| `.tmp\_s4oq_final_verify_2026_10_09.py` | `944A4F7006C8` | 959 | 1 |
| `.tmp\_s4oq_forward_2026_10_09.py` | `43E72C62587D` | 3482 | 1 |
| `.tmp\_s4oq_grid_cmp_2026_10_09.py` | `F00865587D6A` | 1601 | 1 |
| `.tmp\_s4oq_grid_diag_2026_10_09.py` | `082E8B8B7BC4` | 1553 | 1 |
| `.tmp\_s4oq_grid_recompute_2026_10_09.py` | `AFB613F5CED1` | 2394 | 1 |
| `.tmp\_s4oq_keyscan_2026_10_09.py` | `C9F94C812F7F` | 573 | 1 |
| `.tmp\_s4oq_read_db_probe_2026_10_09.py` | `5926143C8A6D` | 658 | 1 |
| `.tmp\_s4oq_recompute_2026_10_09.py` | `07CDEC653345` | 3202 | 1 |
| `.tmp\_s4oq_skel_2026_10_09.py` | `73FC780B4849` | 466 | 1 |
| `.tmp\_s4oq_stats_2026_10_09.json` | `570489BB6163` | 1669 | 125 |
| `.tmp\_s4oq_sups_draft_2026_10_09.json` | `ACE64D4F377D` | 23401 | 229 |
| `.tmp\_s4oq_variants_2026_10_09.py` | `CCBBB499E19A` | 1233 | 1 |
| `.tmp\_s4oq_verify_addendum_2026_10_09.py` | `419C15A7A2C5` | 2252 | 1 |
| `.tmp\_s4oq_write_addendum_2026_10_09.py` | `63E61AFA6517` | 11886 | 1 |
| `.tmp\_s4td_existing_faces.json` | `1009161547CF` | 36128 | 895 |
| `.tmp\_s4td_existing_qindex.tsv` | `AD8C9E3C966B` | 14093 | 149 |
| `.tmp\_s5dp_run_stdout_2026_10_11.txt` | `13F90AAFAB80` | 7256 | 94 |
| `.tmp\_t1_exp2_c_driver_stdout.log` | `0BF18EDC773D` | 9410 | 72 |
| `.tmp\_t1_exp2_c_driver_stdout2.log` | `120391010514` | 9272 | 72 |
| `.tmp\_t1_exp2_c_driver_stdout3.log` | `D0AACA46B41A` | 9376 | 72 |
| `.tmp\_t1_exp2_c_driver_stdout4.log` | `16F08FF22F9D` | 73756 | 606 |
| `.tmp\_t1_exp2_run_d.log` | `B5391E5B0CA3` | 4752 | 37 |
| `.tmp\_t1_exp2_run_d2.log` | `34123220512B` | 3132 | 24 |
| `.tmp\_t1_qwen_temp_sweep_retry.log` | `1A791E41BD4B` | 1757 | 42 |
| `.tmp\_t1_qwen_temp_sweep_run.log` | `EE6A1EE19548` | 8402 | 174 |
| `.tmp\_t1_temp_axis_design_probe_2026_10_09.json` | `02E8133D3000` | 5657 | 234 |
| `.tmp\_t15_inspect3_out.txt` | `56F1909CD962` | 1588 | 15 |
| `.tmp\_t15_inspect4_out.txt` | `BA65EC451865` | 3057 | 48 |
| `.tmp\_t15_inspect5_out.txt` | `E632FEB9AD99` | 933 | 7 |
| `.tmp\_t15_inspect6_out.txt` | `194F2AC92089` | 6659 | 57 |
| `.tmp\_t15_inspect7_out.txt` | `5D51DCAD59D1` | 3647 | 40 |
| `.tmp\_t15_percell.txt` | `95D32BED4C21` | 491 | 10 |
| `.tmp\_t15_percell_out.txt` | `CBEC28A08723` | 772 | 6 |
| `.tmp\_t15_probe_log.json` | `94444963FF77` | 718 | 24 |
| `.tmp\_t15r2_checkpoint_warn.jsonl` | `E8A146D6998F` | 914 | 2 |
| `.tmp\_v16_tail_only.txt` | `63FCCC843CDD` | 3471 | 21 |
| `.tmp\_v3r1_diag.json` | `E2E61AD91ECE` | 5699 | 250 |
| `.tmp\_v3r1_run1.log` | `2E3CA9E57EB6` | 5062 | 130 |
| `.tmp\_v3r1_run2.log` | `4D945579A5EE` | 2066 | 6 |
| `.tmp\_v412_contrib.py` | `1085411B4896` | 1040 | 1 |
| `.tmp\_v412_m1_domain_probe.py` | `A59587EB5E3F` | 2524 | 1 |
| `.tmp\_v412_material_scan.py` | `F3493907CBE2` | 627 | 1 |
| `.tmp\_v412_s3side_probe.py` | `60A3E0F59B6F` | 1412 | 1 |
| `.tmp\_v412_unique_scan.py` | `B2E381F09828` | 1300 | 1 |
| `.tmp\_verify_r32_card_2026_10_10.py` | `61F99FC5FDB9` | 631 | 1 |
| `.tmp\_vk_baxis_probe_2026_10_09.py` | `5F55151BDC76` | 1832 | 1 |
| `.tmp\_vk_baxis_probe_2026_10_09.txt` | `D74E9AE8CD3A` | 5156 | 38 |
| `.tmp\_vk_dualread_probe_2026_10_09.py` | `A2C315831EFE` | 3240 | 1 |
| `.tmp\_vk_dualread_probe_2026_10_09.txt` | `79AD926F75A8` | 888 | 11 |
| `.tmp\_vk_pv02_recheck_a.py` | `37D55BF0FBA6` | 4188 | 1 |
| `.tmp\_vk_pv02_recheck_b.py` | `FE0F10E38BB3` | 1646 | 1 |
| `.tmp\_vk_pv02_recheck_c.py` | `7D35B715F8E2` | 2397 | 1 |
| `.tmp\_vk_pv02_recheck_d.py` | `7AE7ED6BCD8A` | 982 | 1 |
| `.tmp\_vk_pv02_recheck_e.py` | `D925E60C1D3C` | 1742 | 1 |
| `.tmp\_vk_pv02_recheck_f.py` | `C2E298CCEBC6` | 1522 | 1 |
| `.tmp\_vk_pv02_recheck_g.py` | `F237E1D2715F` | 2269 | 1 |
| `.tmp\_vk_q.py` | `67364902116C` | 519 | 1 |
| `.tmp\_vk_q2.py` | `D5759D40DC43` | 540 | 1 |
| `.tmp\_vk_q3.py` | `A00CD309205F` | 612 | 1 |
| `.tmp\_vk_q4.py` | `DEFC3C53B7DF` | 784 | 1 |
| `.tmp\_vk_q5.py` | `7B95307225BA` | 1246 | 1 |
| `.tmp\_vk_q6.py` | `7DA34DD24EB0` | 811 | 1 |
| `.tmp\_vk_q7.py` | `A6C525F88F11` | 1331 | 1 |
| `.tmp\_vk_q8.py` | `5A81E5558C72` | 1025 | 1 |
| `.tmp\_vk_s4_topup_intake_recheck_2026_10_09.txt` | `683501B8FB41` | 7098 | 86 |
| `.tmp\anchor_snapshot.json` | `54607FC836A1` | 3706 | 151 |
| `.tmp\card23_readout_utf8.txt` | `4AA127D1DC62` | 5088 | 42 |
| `.tmp\e4_axis2_run_out.json` | `536080B19999` | 3514 | 152 |
| `.tmp\e4_axis2_validation_out.json` | `5B3EF39DC114` | 2657 | 170 |
| `.tmp\five_terminal_classify_2026_10_10.json` | `9E04C58572BD` | 188834 | 7604 |
| `.tmp\five_terminal_domain_2026_10_10.json` | `1EFE7E458AB1` | 192600 | 10456 |
| `.tmp\five_terminal_scan_2026_10_10.json` | `5196B75B95B6` | 126177 | 6897 |
| `.tmp\five_terminal_supplement_2026_10_10.json` | `B664C3BAEB75` | 17614 | 589 |
| `.tmp\gate_check.py` | `ABE7FBDB394B` | 648 | 1 |
| `.tmp\gate_check2.py` | `7025CECEB766` | 840 | 1 |
| `.tmp\k_v3df_0_1_four_readings_2026_10_09.py` | `2E990644CC8D` | 50232 | 933 |
| `.tmp\kro_extract.py` | `B5731ABAE41F` | 802 | 1 |
| `.tmp\pa_block.py` | `19AC8C59439B` | 345 | 1 |
| `.tmp\receipt_disp_idx.txt` | `08261E23970B` | 6876782 | 41514 |
| `corpus\v20\all.json` | `8DF31C95B1FC` | 2557 | 45 |
| `corpus\v20\by_model\kimi\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 | 571 |
| `corpus\v20\by_model\minimax\artifact_v_2026_09_16.json` | `9E1CCBDCEACC` | 25347 | 795 |
| `corpus\v20\index_v2_2026_09_16.json` | `EFE05AD775DE` | 24150 | 571 |
| `corpus\v20\index_v3_2026_09_29.json` | `3BA2449CF986` | 24421 | 579 |
| `corpus\v20\index_v3_2026_10_09.json` | `74B27393574F` | 24837 | 581 |
| `corpus\v20\strip_captions_22.json` | `6A2656878745` | 12798 | 155 |
| `corpus\v20_caption_surface\_adendum_I_po_captions_closure_20260917_132049.json` | `18165008BEF6` | 4429 | 114 |
| `corpus\v20_caption_surface\_p_d_b3_merkle_22caption_runner_2026_09_16.py` | `D2CD7ACB29A1` | 18596 | 417 |
| `corpus\v20_caption_surface\_p_d_v03_22caption_verification_20260917_163757.json` | `DFBCC5D6FC34` | 13775 | 410 |
| `corpus\v20_caption_surface\caption_distance_mat_22.json` | `1C4FFF004CC4` | 8552 | 558 |
| `corpus\v20_caption_surface\caption_features_22.json` | `727A253566DD` | 18362 | 687 |
| `corpus\v20_caption_surface\caption_stats_22.json` | `DA34F54D4F5B` | 632 | 26 |
| `corpus\v20_caption_surface\manifest.json` | `4FDDA6480BB5` | 1477 | 60 |
| `corpus\v20_caption_surface\strip_captions_22.json` | `6A2656878745` | 12798 | 155 |
| `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.cpython-314.pyc` | `F96453EBEAD6` | 55784 | 183 |
| `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.cpython-314.pyc` | `80A752CCA163` | 57022 | 171 |
| `deposon_team\plugins\__pycache__\boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.cpython-314.pyc` | `74467BB37F95` | 103946 | 255 |
| `deposon_team\plugins\_pg_v01_compute.py` | `D511C545F88E` | 20923 | 510 |
| `deposon_team\plugins\_v3x_frozen_schema_v1.json` | `9E99DCC4D920` | 12919 | 215 |
| `deposon_team\plugins\_verify_15frozen.py` | `EFAE9274962E` | 3905 | 1 |
| `deposon_team\plugins\_verify_15frozen_v1.py` | `60523E406055` | 2094 | 1 |
| `deposon_team\plugins\_verify_pg_v0.py` | `CDD3415AD993` | 3978 | 1 |
| `deposon_team\plugins\_verify_pg_v0_v1.py` | `67088AE1A860` | 2521 | 1 |
| `deposon_team\plugins\boss_pa_1_rbr_rm.py` | `5CC594147E00` | 17743 | 404 |
| `deposon_team\plugins\boss_pa_2_potential_game.py` | `33DFB4338C53` | 10410 | 248 |
| `deposon_team\plugins\boss_pa_3_replicator_dynamics.py` | `A2BD9DD24C25` | 12900 | 307 |
| `deposon_team\plugins\boss_pc_1_2d_ising_universality.py` | `BFC319808447` | 7547 | 181 |
| `deposon_team\plugins\boss_pc_2_transverse_field_ising.py` | `210105A7F29A` | 7053 | 176 |
| `deposon_team\plugins\boss_pc_3_reservoir_computing.py` | `021EA39B7193` | 7373 | 194 |
| `deposon_team\plugins\boss_pg_1_riemannian_degenerate.py` | `97FEDE6C8A4E` | 5996 | 125 |
| `deposon_team\plugins\boss_pg_2_hyperbolic_classification_collapse.py` | `F006D4CACA94` | 5285 | 115 |
| `deposon_team\plugins\boss_pg_3_geodesic_violation.py` | `09F37C01A258` | 5517 | 117 |
| `deposon_team\plugins\github_dir_structure_2026_09_18.md` | `0FD07AD38282` | 11675 | 232 |
| `deposon_team\plugins\github_upload_2026_09_18.sh` | `52BC19845B2B` | 6030 | 113 |
| `docs\V3X\CPATH_SIMULATION_REPORT_2026_09_10.md` | `DE772CD9E7BA` | 6825 | 150 |
| `docs\V3X\D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` | `0A63824F0805` | 7352 | 97 |
| `docs\V3X\D5_DECISIONS_LAND_REPORT_2026_09_15.md` | `8FF1A7C5413F` | 21756 | 433 |
| `docs\V3X\D7_POST_CLEANUP_PLAN_2026_09_18.json` | `0B8A1A357AAE` | 20271 | 810 |
| `docs\V3X\D7_POST_CLEANUP_REPORT_2026_09_16.json` | `40955BF2ABC5` | 1248 | 33 |
| `docs\V3X\DPATH_CROSS_MODAL_2026_09_10.md` | `E4EE3999F7CE` | 26460 | 483 |
| `docs\V3X\P_C_D1_D3_REPORT_2026_09_15.md` | `79C7321056B8` | 13419 | 240 |
| `docs\V3X\P_F_D1_REPORT_2026_09_15.md` | `E47D0348922E` | 12608 | 199 |
| `docs\V3X\P_F_IMPLEMENTATION_2026_09_11.md` | `EDD048EAA721` | 22973 | 371 |
| `docs\V3X\PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` | `C165CD33A362` | 4587 | 113 |
| `docs\V3X\V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` | `4A08521F8DE1` | 38545 | 620 |
| `letters\_letter_to_pi_upload_scoping_verdict_2026_09_26.md` | `44D9A1972A13` | 68449 | 833 |
| `letters\_v4_distillation_reply_claude_code_2026_09_20.md` | `D39CB17B051B` | 64212 | 393 |
| `results\__pycache__\_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | `F4194CC5A522` | 43685 | 188 |
| `results\__pycache__\_s5doubleprime_five_lines_runner_2026_10_11.cpython-314.pyc` | `9FC3E2152679` | 44952 | 187 |
| `results\__pycache__\_t1_exp2_executor_2026_10_09.cpython-314.pyc` | `346595DF084C` | 87302 | 376 |
| `results\__pycache__\_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | `08D4B51C45C6` | 67081 | 187 |
| `results\__pycache__\_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.cpython-314.pyc` | `E7AB1ADBF898` | 69630 | 188 |
| `results\_archive_2026_09_20\_archive_manifest_2026_09_18.json` | `A729875C0C67` | 4712 | 127 |
| `results\_archive_2026_09_20\_archive_manifest_2026_09_20.json` | `4DD89950BF11` | 35682 | 974 |
| `results\_archive_2026_09_21\_archive_manifest_2026_09_21.json` | `33FE31633DA8` | 17353 | 442 |
| `results\_archive_2026_09_24\_worker_openrouter_rag_run.py` | `4458CCF3D64A` | 24113 | 517 |
| `results\_archive_cleanup_extension_2026_09_28.md` | `889D15247607` | 28774 | 372 |
| `results\_archive_cleanup_non_upload_2026_09_28.md` | `34F2C63306B8` | 56714 | 419 |
| `results\_archive_manifest_deposon_sub_2026_09_23.json` | `B34B9F7BDFB7` | 52153 | 1826 |
| `results\_archive_manifest_non_upload_2026_09_23.json` | `B899103853CA` | 148690 | 5886 |
| `results\_archive_manifest_non_upload_v2_2026_09_28.json` | `84EEF669234B` | 236651 | 9539 |
| `results\_archive_manifest_non_upload_v3_2026_09_28.json` | `A2E4C5A9B713` | 204256 | 8681 |
| `results\_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | `A82881653520` | 465366 | 1626 |
| `results\_freeze_receipt_2026_10_01_q1.md` | `9B7101BC09BD` | 698 | 1 |
| `results\_ghostref_copy_log_2026_09_23.json` | `8CD133D0896F` | 129780 | 2777 |
| `results\_p_i_real_labels_2026_09_16\p_i_real_labels_results_2026_09_16.json` | `E934819EE9ED` | 1043 | 46 |
| `results\_p_j_convergence_basin_2026_09_16\p_j_convergence_basin_results_2026_09_16.json` | `A9AD1DE618F5` | 1669 | 58 |
| `results\_p_l_p_c_finite_size_scaling_2026_09_16\p_l_p_c_finite_size_scaling_results_2026_09_16.json` | `664E7CC05AEC` | 9076 | 476 |
| `results\_p_l_real_data_collapse_2026_09_16\p_l_real_data_collapse_results_v2_2026_09_16.json` | `AFE975606D40` | 3761 | 163 |
| `results\_p_m_attack_surface_cost_2026_09_16\p_m_attack_surface_cost_results_2026_09_16.json` | `FBCB60CF5102` | 5266 | 224 |
| `results\_p_m_real_separation_2026_09_16\p_m_real_separation_results_2026_09_16.json` | `A4B12D1CFEDC` | 2042 | 74 |
| `results\_p_n_curvature_potential_coupling_2026_09_16\p_n_curvature_potential_coupling_results_2026_09_16.json` | `088F28524A1D` | 4276 | 153 |
| `results\_p_o_stranger_verification_2026_09_16\p_o_stranger_verification_results_2026_09_16.json` | `1E4C065DA058` | 5916 | 195 |
| `results\_upload_ledger_kimi_2026_09_30.json` | `B17CB8AAE62D` | 218279 | 4886 |
| `results\_upload_ledger_kimi_2026_10_01.json` | `79A0FB18683B` | 43275 | 940 |
| `results\_v3_construct_degradation_diag_2026_09_23.json` | `C8D539A58D29` | 11609 | 328 |
| `results\_v3_n_cpath_live_data_2026_09_27.json` | `25374AF92F88` | 12711 | 527 |
| `results\_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | `26C0D0B0FFB6` | 6411 | 162 |
| `results\_v3_n_pg_boss_live_data_2026_09_27.json` | `BE11C5274807` | 9220 | 368 |
| `results\_v3_recheck_01_result_2026_09_27.json` | `C19E2AB24E63` | 167831 | 6680 |
| `results\_v3_recheck_04_result_2026_09_27.json` | `DB8CFB974CE3` | 840158 | 28858 |
| `results\_v3_recheck_05_result_2026_09_28.json` | `F63B36B75A51` | 450701 | 15212 |
| `results\_v3_recheck_08_result_2026_09_27.json` | `0D2AF01086DB` | 10587 | 370 |
| `results\_v3_recheck_08b_executor\result_2026_09_27.json` | `F9A7FA2D65B1` | 88052 | 2160 |
| `results\_v3_recheck_08c_preexp_data\_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | `4B7ED4D0A3E5` | 1395 | 27 |
| `results\_v3_recheck_08c_preexp_data\result_2026_09_27.json` | `689A6E4427A8` | 146601 | 5065 |
| `results\_v3_recheck_10_result_2026_09_27.json` | `5D4B6BAF1B18` | 82535 | 3094 |
| `results\_v3_recheck_12_result_2026_09_27.json` | `CDB37ED0B32F` | 187612 | 7091 |
| `results\_v3_recheck_19_result_2026_09_27.json` | `DF07CF80930F` | 59888 | 1935 |
| `results\_v3_recheck_21_result_2026_09_27.json` | `354AE9C14FE2` | 44928 | 1660 |
| `results\_v3_recheck_26_preexp_data_2026_09_27.json` | `177C88E1BD82` | 94658 | 5562 |
| `results\_v3_recheck_26_result_2026_09_27.json` | `EB6A99DD46DD` | 11994 | 434 |
| `results\_v3_recheck_26b_r3_result_2026_09_29.json` | `C9D3C9F819F1` | 54294 | 1175 |
| `results\_v3_recheck_26b_result_2026_09_27.json` | `49C6E5A07732` | 44379 | 1096 |
| `results\_v3_recheck_27_result_2026_09_27.json` | `E06CB51FB3AF` | 42571 | 1493 |
| `results\_v3_recheck_28_result_2026_09_27.json` | `C0A8CB9029A7` | 26113 | 922 |
| `results\_v3_recheck_35_result_2026_09_27.json` | `A8A4BEFB21F5` | 35091 | 1324 |
| `results\_v3_s_phrasetemplate_preexp_data\result_2026_09_27.json` | `FAE3C4640507` | 36844 | 1309 |
| `results\_v3_s3_wordexpand_data\result_2026_09_28.json` | `F7F6D875D73A` | 34953 | 1037 |
| `results\_v3_s3_wordexpand_recheck_r1_2026_09_28.json` | `67CCEA282D1C` | 33867 | 992 |
| `results\_v3_v4_achievements_inventory_2026_09_24.md` | `965DB22E9130` | 194083 | 1926 |
| `results\_v3_v4_achievements_inventory_3dir_2026_09_24.md` | `DF7E9CD39251` | 355819 | 3818 |
| `results\_v3_v4_ghostref_reconciliation_2026_09_23.md` | `1D52DB0EBF53` | 169864 | 658 |
| `results\_v3n_cpath_live_rerun_2026_10_01.json` | `7C26D08ECE3B` | 60012 | 2321 |
| `results\_v3x_18frozen_remeasure_2026_09_16\v3x_18frozen_remeasure_results_2026_09_16.json` | `928794710241` | 4202 | 149 |
| `results\_v3x_conservation_anchor_2026_09_17.txt` | `F331A9C2BD22` | 940 | 1 |
| `results\_v3x_d0_5_aggregation_2026_09_17.md` | `DDF0D1AA96D2` | 12010 | 1 |
| `results\_v3x_experiments_2026_09_16\v3x_experiments_results_2026_09_16.json` | `F39412103366` | 17053 | 591 |
| `results\_v3x_p_k_verify_2026_09_16\v3x_p_k_verify_results_2026_09_16.json` | `59C2113B7C71` | 2059 | 57 |
| `results\_v3x_p_l_v3_external_spec_2026_09_17.md` | `6A5B6EB635F0` | 5769 | 1 |
| `results\_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` | `523B5941C30C` | 16835 | 405 |
| `results\_v4_pi_cot_v2_result.json` | `1665F367B2C4` | 9068 | 352 |
| `results\_v4_pi_cot_v2_result_v2.json` | `F86727C857A8` | 18089 | 829 |
| `results\_v4_pi_cot_v2_ruleset.json` | `821465001819` | 5876 | 371 |
| `results\_v4_pi_cot_v2_ruleset_v2.json` | `C5B3DD141655` | 6179 | 340 |
| `results\_v4_pi_cot_v3_dataset_v1p3_2026_09_27.json` | `ED596914259A` | 12975 | 284 |
| `results\_v4_pi_cot_v3_result_v3r1_2026_09_27.json` | `735C03DB1AE9` | 22292 | 781 |
| `results\_v4_r4_purge_actions_2026_09_24.md` | `8BBFE831E7C3` | 33117 | 4 |
| `results\_v4_supp_l14v3_batch2_r1_result.json` | `D245AE4CE385` | 4128 | 101 |
| `results\_v4_supp_l14v3_batch2_r2_models_probe.json` | `3C9DC60B5071` | 1503 | 64 |
| `results\_v4_supp_l14v3_batch2_r2_models_probe.log` | `5664C63102A0` | 1260 | 55 |
| `results\_v4_supp_l14v3_batch2_r2_result.json` | `8C125E257AF8` | 62887 | 1456 |
| `results\_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json` | `21A89EB36A14` | 2635 | 82 |
| `results\_v4_supp_l14v3_batch2_r3_result.json` | `25251ACA6D79` | 62886 | 1451 |
| `results\_v4_supp_l14v3_batch2_r4_result.json` | `15B8DDC5BA9E` | 63572 | 1463 |
| `results\_v4_supp_l14v3_batch2_r5_result.json` | `479F4119CF72` | 64285 | 1475 |
| `results\_v4_supp_l14v3_batch2_r6_result.json` | `E37D9C74C3E5` | 65083 | 1457 |
| `results\_v4_supp_l14v3_batch3_r1_result.json` | `D24B84671C23` | 66520 | 1514 |
| `results\_v4_supp_l14v3_batch3_r2_result.json` | `58E9C55A770D` | 67767 | 1533 |
| `results\_v4_supp_l14v3_batch3_r3_result.json` | `6E677FFCC880` | 68488 | 1544 |
| `results\_v4_supp_l14v3_batch3_r4_result.json` | `0E47768640D3` | 69635 | 1556 |
| `results\_v4_supp_l14v3_batch3_r5_result.json` | `38998F994B84` | 70064 | 1524 |
| `results\_v4_supp_l14v3_batch4_r1_result.json` | `7D9FE9D319A2` | 71775 | 1563 |
| `results\_v4_supp_l14v3_batch4_r2_result.json` | `6A9A362D9869` | 71998 | 1581 |
| `results\_v4_supp_l14v3_batch4_r3_result.json` | `ED5267DF7D6F` | 72884 | 1605 |
| `results\_v4_supp_l14v3_batch4_r4_result.json` | `41E0BA55E205` | 74448 | 1639 |
| `results\_v4_supp_l14v3_batch4_r5_result.json` | `BAD01F2B89FD` | 76138 | 1647 |
| `results\_v4_supp_l14v3_batch4_r6_result.json` | `6B8093FF8962` | 32369 | 724 |
| `results\_v4_supp_l14v3_batch5_r1_result.json` | `120D45D1774F` | 71021 | 1582 |
| `results\_v4_supp_l14v3_batch5_r2_result.json` | `B0F76B5C3522` | 72550 | 1595 |
| `results\_v4_supp_l14v3_batch5_r3_result.json` | `8E2ACDACFA1E` | 73682 | 1628 |
| `results\_v4_supp_l14v3_batch5_r4_result.json` | `1C62520C372B` | 74100 | 1638 |
| `results\_v4_supp_l14v3_batch5_r5_result.json` | `C874D21A4CBE` | 77137 | 1641 |
| `results\_v4_supp_l14v3_batch9_r1_result.json` | `7E8DFE0156CD` | 69251 | 1405 |
| `results\_v4_supp_l14v3_batch9_r2_result.json` | `08B0AAAAE726` | 69325 | 1415 |
| `results\_v4_supp_l14v3_batch9_r3_result.json` | `29E0D865A7BF` | 69984 | 1419 |
| `results\_v4_supp_l14v3_batch9_r4_result.json` | `EB8B13D9F592` | 71093 | 1433 |
| `results\_v4_supp_l14v3_batch9_r5_result.json` | `1610F5060EF1` | 72047 | 1452 |
| `results\_v4_supp_t1_result.json` | `D6CB03A4657E` | 82365 | 2451 |
| `results\_v4_supp_t15_result.json` | `6B47D389B7AE` | 53265 | 1371 |
| `results\_v4_supp_t15r2_result.json` | `C69AB0E3002E` | 73526 | 1799 |
| `results\_v4_track2_models_probe.py` | `DA62ABAA1E03` | 3191 | 85 |
| `results\_v4_track2_reprobe.py` | `F92CC93F1304` | 2860 | 62 |
| `results\_v5_item21_strategyqa_realias_recompute_2026_09_29.json` | `49F068C716A8` | 34314 | 1218 |
| `results\_v5_item35_v2_matrix_result_2026_09_29.json` | `13AD5B740F80` | 84699 | 3116 |
| `results\_v5_item35_v3_collinear_result_2026_09_29.json` | `99F3E504589E` | 187287 | 6296 |
| `results\_v5_track2_qwen_retry_2026_09_29.json` | `6ACAFE021AAF` | 2735 | 80 |
| `results\_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json` | `1088FDD2B197` | 744352 | 45404 |
| `results\_v5_v3_deg_fix_c1c4_result_2026_09_29.json` | `1B5BFECC818E` | 266417 | 10010 |
| `results\_v5_v3_deg_p1_reopen_result_2026_09_29.json` | `B86D6740D487` | 571451 | 19091 |
| `results\_v5r_s40_recompute_2026_09_29.json` | `5BE465342AE1` | 4992 | 131 |
| `results\boss_pa_1_rbr_rm_result_2026_09_15.json` | `C7C59E0D2F6C` | 8753 | 350 |
| `results\boss_pa_2_potential_game_result_2026_09_15.json` | `5C76137D6430` | 7530 | 242 |
| `results\boss_pa_3_replicator_dynamics_result_2026_09_15.json` | `D6F233D73C45` | 9098 | 334 |
| `results\boss_pc_1_a1_resampling_2026_09_15.json` | `D21912A05D79` | 1017 | 45 |
| `results\boss_pc_1_real_2d_ising_2026_09_15.json` | `43D9CE160FC8` | 2460 | 98 |
| `results\boss_pc_2_a2_fitting_2026_09_15.json` | `5A880678C386` | 1024 | 43 |
| `results\boss_pc_2_real_transverse_ising_2026_09_15.json` | `8933D61B180A` | 3553 | 135 |
| `results\boss_pc_3_a3_clipping_2026_09_15.json` | `D74D6B39D1B0` | 1265 | 57 |
| `results\boss_pc_3_real_reservoir_2026_09_15.json` | `94B5398BE76C` | 2364 | 95 |
| `results\boss_pe_1_real_2d_ising_2026_09_15.json` | `43D9CE160FC8` | 2460 | 98 |
| `results\boss_pe_2_real_transverse_ising_2026_09_15.json` | `8933D61B180A` | 3553 | 135 |
| `results\boss_pe_3_real_reservoir_2026_09_15.json` | `94B5398BE76C` | 2364 | 95 |
| `results\c5_b_group_fix_readings_2026_10_01.json` | `2A7749DA7C4D` | 9996 | 447 |
| `results\c5_b_group_fix_readings_2026_10_09.json` | `4E415990B71D` | 10029 | 448 |
| `results\d7_5anchor_60cells_9model_verdict_2026_09_18.json` | `4505CCA79C15` | 2456 | 102 |
| `results\deposon_3risk_v0_fixes_2026_09_11.json` | `D87C0327A6FB` | 8338 | 240 |
| `results\deposon_ark_models_2026_09_10.json` | `CCC3EA09A7F5` | 23296 | 867 |
| `results\deposon_benchmark_v1_4_strategyqa_details.json` | `A63EBEA7B29A` | 235779 | 8097 |
| `results\deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `4E4A17D43ADF` | 13562 | 428 |
| `results\deposon_cpath_simulation_2026_09_10.json` | `9466FDBF9C95` | 6351 | 254 |
| `results\deposon_d_fix2_metric_verify_9m60c_2026_09_15.json` | `9F88A212A77C` | 204441 | 6721 |
| `results\deposon_deepseek_v41_flash_2026_09_10.json` | `4D7BEA150F3A` | 13373 | 457 |
| `results\deposon_deepseek_v41_flash_30cells_2026_09_10.json` | `84DF447C38DF` | 46432 | 1211 |
| `results\deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json` | `05CDE1CA74EF` | 17549 | 498 |
| `results\deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` | `56401317E62B` | 18592 | 534 |
| `results\deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json` | `28BAD561C328` | 6748 | 187 |
| `results\deposon_dpath_cross_modal_2026_09_10.json` | `AB0C2EAFF0D1` | 75964 | 2252 |
| `results\deposon_dpath_cross_modal_runner_2026_09_10.py` | `FB20A6BA5EC6` | 27930 | 659 |
| `results\deposon_embedding_dual_2026_09_10.json` | `33F8AC5D4BFF` | 6834 | 133 |
| `results\deposon_embedding_openrouter_5models_2026_09_10.json` | `0C0D9AFD39AC` | 12785 | 402 |
| `results\deposon_feshbach_lindblad_sim_2026_09_10.json` | `AA545C67604D` | 7414 | 237 |
| `results\deposon_feshbach_rag_30cells_2026_09_10.json` | `508F664FFA44` | 64978 | 1578 |
| `results\deposon_feshbach_rag_30cells_2026_09_10.py` | `A072E4184E83` | 14343 | 398 |
| `results\deposon_game_theory_eval_2026_09_10.json` | `3FA0FF2C8C08` | 10096 | 278 |
| `results\deposon_gpt6_astra_smoke_2026_09_10.json` | `4BF92BFDEFDA` | 3500 | 84 |
| `results\deposon_gpt6_proxy_smoke_2026_09_10.json` | `524B34E319B5` | 5485 | 109 |
| `results\deposon_gpt6_proxy_step1_2026_09_10.json` | `2E23115D9D4B` | 1245 | 38 |
| `results\deposon_gpt6_proxy_v2_2026_09_10.json` | `A6812512F8F3` | 5810 | 121 |
| `results\deposon_gpt6_teamorouter_30cells_2026_09_10.json` | `EA38EE252701` | 18290 | 427 |
| `results\deposon_gpt6_vpn_smoke_2026_09_10.json` | `3267746E47E9` | 3489 | 102 |
| `results\deposon_llm_codingplan_30cells_2026_09_10.json` | `24E4DCBAA4EA` | 18634 | 421 |
| `results\deposon_openrouter_5model_30cells_2026_09_10.json` | `B374F80F3B2D` | 31690 | 1442 |
| `results\deposon_openrouter_5model_rag_30cells_2026_09_10.json` | `2E55C53BE25D` | 111710 | 3640 |
| `results\deposon_openrouter_embedding_5model_2026_09_10.json` | `45F314F3415C` | 9472 | 342 |
| `results\deposon_overseas_open_smoke_2026_09_10.json` | `2481ADADCBB9` | 6787 | 187 |
| `results\deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | `B5873AFB9D29` | 18104 | 700 |
| `results\deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33AD1C01F745` | 20398 | 736 |
| `results\deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `95F3F0957BE8` | 21176 | 747 |
| `results\deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json` | `576EAF8D7431` | 11341 | 386 |
| `results\deposon_pa_d1_d3_2026_09_15.json` | `E221792715F8` | 15604 | 468 |
| `results\deposon_pc_d1_d3_2026_09_15.json` | `B2046AF03610` | 20408 | 586 |
| `results\deposon_pe_d1_d3_2026_09_15.json` | `594D7A8D3DE8` | 17085 | 431 |
| `results\deposon_pf_d1_2026_09_15.json` | `12791772814E` | 21933 | 483 |
| `results\deposon_pf_d1_full_9m5c_2026_09_15.json` | `FCB5105DF0B6` | 33829 | 1045 |
| `results\deposon_pf_implementation_2026_09_11.json` | `509DCEE3B139` | 27311 | 407 |
| `results\deposon_pg_v01_9m60c_2026_09_15.json` | `AB75889EE738` | 11512 | 403 |
| `results\deposon_risk1_02940_decision_2026_09_11.json` | `2DC8CA9E36C1` | 4336 | 110 |
| `results\deposon_risk2_canonical5_decision_2026_09_11.json` | `CF4A882160E1` | 4066 | 80 |
| `results\deposon_risk3_seff_decision_2026_09_11.json` | `67867E752F47` | 6488 | 167 |
| `results\deposon_v2_phase1_60cells_2026_09_11.json` | `A18BBC703B42` | 85508 | 2645 |
| `results\deposon_v2_phase2_dual_mainline_2026_09_11.json` | `E337B824C4B9` | 3189 | 95 |
| `results\deposon_v2_phase2_f2_2026_09_11.json` | `8B16B611C4DB` | 4582 | 197 |
| `results\deposon_v2_phase3_f3_2026_09_11.json` | `0B5DCA765D16` | 2474 | 93 |
| `results\deposon_v2_phase3_strip_reembed_2026_09_11.json` | `8900526D8E3A` | 4160 | 131 |
| `results\deposon_v2_phase4_f4_2026_09_11.json` | `CF7682348617` | 5212 | 203 |
| `results\deposon_v2_phase5_f5_2026_09_11.json` | `889FC57B3B72` | 2356 | 77 |
| `results\deposon_v3_physical_opt_2026_09_11.json` | `27F9BD5CC260` | 17591 | 692 |
| `results\deposon_v3_physical_opt_60cells_2026_09_11.json` | `C659695AA23C` | 17732 | 604 |
| `results\deposon_v3_v7_summary_2026_09_11.json` | `063AC8D00542` | 25049 | 380 |
| `results\deposon_v3x_6way_stage2_2026_09_10.json` | `D301BBFED982` | 2741 | 117 |
| `results\deposon_v3x_6way_stage3_2026_09_10.json` | `D892A9D3D6BA` | 15943 | 452 |
| `results\deposon_v3x_6way_summary_2026_09_10.json` | `63E0798E5843` | 1506 | 57 |
| `results\deposon_v41_flash_60cells_v2_2026_09_10.json` | `B1D802A68723` | 38428 | 1027 |
| `results\deposon_v41_flash_rag_baseline_2026_09_10.json` | `6754D2655E0A` | 101484 | 1366 |
| `results\deposon_v42_v2_miss_rate_curve_2026_09_16.json` | `0A8ED127D6DE` | 24435 | 805 |
| `results\deposon_volcengine_22caption_embedding_2026_09_10.json` | `C4B774C8E34C` | 4559 | 254 |
| `results\deposon_volcengine_7model_smoke_2026_09_10.json` | `EAE44CC3B7B2` | 5944 | 191 |
| `results\deposon_volcengine_9model_30cells_2026_09_10.json` | `58AB335CA341` | 4894 | 182 |
| `results\deposon_volcengine_9model_smoke_2026_09_10.json` | `0E5AE7D7D641` | 5328 | 208 |
| `results\deposon_volcengine_coding_plan_5cells_2026_09_10.json` | `52AA8901556E` | 6058 | 164 |
| `results\deposon_volcengine_coding_plan_catalog_2026_09_10.json` | `C0EFB547B9D1` | 2841 | 119 |
| `results\deposon_volcengine_doubao_embedding_2026_09_10.json` | `E99783D18139` | 3303 | 112 |
| `results\deposon_volcengine_embedding_30cells_2026_09_10.json` | `12BE52BC02A7` | 24794 | 1088 |
| `results\deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | `4EC04D3D7D8C` | 32995 | 750 |
| `results\deposon_volcengine_glm_latest_5cells_2026_09_10.json` | `83C35597AF81` | 4895 | 137 |
| `results\deposon_volcengine_glm_latest_5cells_2026_09_10.py` | `A3CA05AEC6FB` | 8112 | 220 |
| `results\deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json` | `0C3EDE881FB1` | 6466 | 145 |
| `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.json` | `FBB7677B9CD5` | 23472 | 748 |
| `results\deposon_volcengine_minimax_m3_30cells_2026_09_10.py` | `218EF1A99F97` | 11703 | 300 |
| `results\deposon_volcengine_seed_code_30cells_2026_09_10.json` | `5149F5CAFCF9` | 23034 | 531 |
| `results\deposon_volcengine_worker_a_2026_09_10.json` | `506810017D34` | 25464 | 665 |
| `results\deposon_volcengine_worker_b_2026_09_10.json` | `B1EB668377CE` | 49338 | 1378 |
| `results\deposon_volcengine_worker_b_2026_09_10.py` | `401DFD3C27F3` | 13232 | 353 |
| `results\deposon_volcengine_worker_c_2026_09_10.json` | `F6F172820C97` | 51716 | 1468 |
| `results\deposon_volcengine_worker_c_2026_09_10.py` | `B5EEEF1E9BD7` | 11692 | 315 |
| `results\deposon_volcengine_worker_d_2026_09_10.json` | `FAE79888344B` | 20280 | 612 |
| `scripts\run_volcengine_seed_code_30cells.py` | `75002485AA94` | 13924 | 359 |
| `verifier\_build_partial.py` | `04FCD95C70F1` | 7160 | 163 |
| `verifier\_run.log` | `E148D7BF11E1` | 7190 | 68 |
| `verifier\_test_one.py` | `893641FD9E25` | 2564 | 54 |
| `verifier\_worker_a_run.log` | `9DF22377DC55` | 4532 | 84 |
| `verifier\handoff\KT_ABC1_anchors_sha256_12.json` | `03C6C01F3697` | 6680 | 188 |
| `verifier\handoff\KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | `6E9CD8CD8E07` | 11318 | 218 |
| `verifier\handoff\P_F_PREDECISION_2026_09_11_V0.1.json` | `312D635E6259` | 12498 | 252 |
| `verifier\run_volcengine_9model_30cells.py` | `54F8033CFB29` | 12050 | 311 |
| `verifier\runs\2026-09-04_pd_v0.jsonl` | `5042869BDF85` | 100 | 1 |
| `verifier\v26\check.py` | `C58A9652A42A` | 2595 | 38 |
| `verifier\v27\check.py` | `118524C7E808` | 2132 | 38 |
| `verifier\v28\check.py` | `B73A6B268F64` | 2201 | 34 |
| `verifier\v29\check.py` | `5923E2C379F6` | 2124 | 32 |
| `verifier\v30\check.py` | `2CF46F79A669` | 2565 | 38 |
| `verifier\v31\check.py` | `E5BB0020E500` | 2185 | 31 |
| `verifier\v32\check.py` | `399BFC743F24` | 2551 | 42 |
| `verifier\v36\check.sh` | `2212DCD98CD1` | 968 | 10 |
| `verifier\v37\check.sh` | `CED43B5F8800` | 1141 | 17 |

---

## §8 可上线性建议（**仅建议・⛔ 0 执行**）

| # | 建议 | 依据（实测） | 归 PI 裁？ |
|:-:|:--|:--|:--|
| R-1 | **成果清单核心纳入面** ＝ `results/` 1,341 件 ＋ `letters/` 97 件 ＋ 顶层 73 件 ＋ `docs/` 135 件 ＋ `verifier/` 116 件 ＋ `deposon_team/` 86 件（＝ 1,848 件） | §1 目录级实测；此六面合计占全仓 72.3% | 否（依 PI 令） |
| R-2 | **草稿/临时不入清单**：`.tmp/` 581 件 0 纳入（其中 330 件近 72h 变动）；其 4 件与 `results/` 存 SHA-12 全等孪生副本者，**建议以成果面为准、`.tmp` 侧作影子副本登记**以防重复计数 | §2-15 明示 4 件孪生；§7-2 之 BOM 113 件集中于 `.tmp` | 否 |
| R-3 | **须 PI 指定唯一权威之撞名**：`_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md` 于仓根（26,633 B／`739245682D40`）与 `results/`（26,637 B／`BA4D07BD7000`）**同名而差 4 B** ⇒ 清单若两处同列将致**双计且口径不一** | §6-2 CONFLICT 组 | ✅ **是** |
| R-4 | **编码异常面仅登记不代改**：`results/` 内 CR>0 者 210 件（以 `.json` 读数面为主）—— 若清单须逐件复算，建议**以字节级读数为权威面**并附本件 §7-3 之 CR 计数；⛔ 本件 0 改其一字 | §7-1／§7-3 | 否 |
| R-5 | **需补测之未核得项**：仓外二区（`deposon-sub` 517 件／`Deposon_v1_2_0_交付包` 23 件）之**逐件**编目，以及 `_non_upload_local_archive` 之存在性—— 二者本件受令/受禁**未核得**，成果清单 v2.0 若须覆盖全盘，须 PI 另令解禁 | §1-1／§4 U-01・U-02 | ✅ **是** |
| R-6 | **`.pyc` 13 件／`__pycache__` 之归属**须 PI 裁定是否入成果面（本件仅登记存在与字节，⛔ 0 判） | §4 U-10 | ✅ **是** |

📌 **⛔ 本件 0 执行上述任何一条**；R-3／R-5／R-6 三条**归 PI 裁**，本件⛔ 0 代拍板。

---

## §9 ⛔ 本件 0 作之事项（逐条）

① ⛔ **0 回改**任何既有件一字（含 `plan.md` 等会话面件）｜② ⛔ **0 物理移动／0 重命名／0 删除／0 改路径**任何仓内文件（一切「应移动/应归档」之判断**仅登记为提案**，归 PI）｜③ ⛔ **0 新建第二个文件**（临时脚本只落 `%TEMP%`）｜④ ⛔ **0 立成果清单**、⛔ **0 出收尾桶**（二者为后续棒）｜⑤ ⛔ **0 触及** `D:\私人资料\_non_upload_local_archive`（0 读 0 写 0 列目录）｜⑥ ⛔ **0 深读／0 改写** `deposon-sub` 与 `Deposon_v1_2_0_交付包`｜⑦ ⛔ **0 断言**漂移根因、⛔ **0 断言**任何「最终」读数、⛔ **0 断言** T1.5 四读数之对应｜⑧ ⛔ **0 判**撞名件之性质、⛔ 0 删、0 合、0 改名｜⑨ ⛔ **0 赋任一** `k_v3s_4_4_*` 布尔｜⑩ ⛔ **0 改任何阈值／门柱／判死线**｜⑪ ⛔ **0 宣告**任何闭／开／段之毕（含③段自身）｜⑫ ⛔ **0 代 PI 拍板**｜⑬ ⛔ **0 冒充** PI／parent／worker／verdict-keeper／verifier／doc-writer／protocol-keeper／Trae code｜⑭ ⛔ 0 网络／0 skill／0 LLM／0 API key／0 读 `.env`｜⑮ ⛔ **0 填**「未核得」项之估值或推断值

---

## 输入链（自报实测）

| 源 | 角色 | 取用方式 |
|:--|:--|:--|
| `D:\私人资料\deposon-repo`（全仓） | 编目主体 | `Get-ChildItem -Recurse -File -Force` ＋ `Get-FileHash -Algorithm SHA256`（⛔ **0 用内建 `hash()`**） |
| `results\_five_stage_chain_design_reconstruction_2026_10_12.md` | ③段设计规格之盘面对账源（`plan.md` §四③ 之转述件） | 只读 1 处（12,625 B／`BFF2FB754564`） |
| `D:\私人资料\deposon-sub` | 仅存在性・件数・bytes・mtime | 仅元数据枚举 |
| `D:\私人资料\Deposon_v1_2_0_交付包` | 仅存在性・件数・bytes・mtime | 仅元数据枚举 |
| `%TEMP%\deposon_inv\`（本棒临时工作区） | CSV 中间件与脚本 | 棒末经可恢复通道清理 |

📌 **本件自身指纹（落盘后实测自报）**：SHA-12 ／ bytes ／ BOM ＝ False ／ CRLF ＝ 0 —— 📌 **自指哈希不可内含于自身文件**（写入即改哈希），故其**实测值在本棒回报正文自报**；版式纪律（UTF-8 无 BOM·纯 LF）由落盘后 `Get-FileHash`＋`Length`＋前三字节＋CR 计数四项实测佐证。

---

*件止。**evidence-auditor（agent-11335500b168）**· 2026-10-12 · **五段链③段・第一步：全量文件夹整理之盘面编目（成果清单 v2.0 之底本）** —— 📌 次序铁律「**先完整全量整理文件夹，再立全清单**」（PI 2026-10-12 令）已守：本件**仅编目**｜⛔ **0 移动 0 删改 0 立清单 0 出桶 0 宣告闭开**｜⛔ 0 回改任何既有件一字｜⛔ 0 触及 `_non_upload_local_archive`｜⛔ 0 断言漂移根因与任何「最终」读数｜⛔ 0 冒充任何角色｜⛔ 0 网络／0 skill／0 LLM*