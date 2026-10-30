# 归档区只读核验件 ｜ KD-MC-06/07 之第三源实测 ｜ 2026-10-18

📌 **件之性质**：本件为**核验件（只读取证面）**——PI 卡 `ask_ad5deaadfbb115c3253f3355` Q4 opt1（2026-10-18 14:17:36.889）授权「核（只读核验——归档区读取不违纪；⛔ 0 写/删）」之**证据底面**。
📌 **标的**：镜像形态对比件 `results/_mirror_morphology_comparison_2026_10_18.md` 之 §5-1（**21 件**·仓内副本与远端删前 blob 不符）＋ §5-2（**81 件**·仓内双区均无副本）＋ 其 `KD-MC-06`/`KD-MC-07`。
📌 **今日 0 实验**（纯本地只读）｜**0 联网**｜**归档区 0 写 0 删 0 移 0 改名**（见 §8 之 0 触动自证）。
📌 **FTFB**：本件之一切判据，先落于判据冻结件、**事后一字未调**（见 §0）。

---

## §0 FTFB · 判据冻结件与引件指纹（凡引他件，先实测）

| 件 | 路径 | bytes | SHA-256（实测） | 备注 |
|---|---|--:|---|---|
| **判据冻结件** | `.tmp/_archive_area_ro_verify_criteria_freeze_2026_10_18.md` | 4,460 | `c02bbde71cda` | **先于一切比对落盘**；BOM=0 · CRLF=0 · 纯 LF |
| 对比件（标的） | `results/_mirror_morphology_comparison_2026_10_18.md` | 134,278 | `39dcf23f9f67` | **与 PI 派工所载 `39dcf23f9f67` 相符** ✅ · BOM=0 · CRLF=0 |
| 补函执行回执 | `results/_supplement_execution_receipt_kimi_2026_10_18.md` | 41,236 | `85f8777f139c` | **与对比件 §0 所载相符** ✅ · BOM=0 · CRLF=0 |

**冻结之要点**：①内容同一性主判据 ＝ **Git-blob-SHA-1-12**（与回执「删前 blob SHA-12」同量纲；⛔ 0 用 SHA-256 对 Git-SHA1——KD-MC-04 教训）②**三通道**（路径／文件名／内容）③枚举须 **os.walk ＋ 断言遍历错误 0**（⛔ 0 `-Recurse`＋`SilentlyContinue`）④21 件之判读三档（相符／不符／不在）与 81 件之在位二值（在·具名／不在）⑤**⛔ 0 判回执失实与否**（判定归 verifier／PI，本件只出证据面）。

---

## §1 三源之全量枚举（os.walk ＋ onerror，遍历错误 0）

| 源 | 路径 | 件数 | 目录数 | 字节 | **遍历错误** | 枚举耗时 |
|---|---|--:|--:|--:|--:|--:|
| S1 repo | `〔本地路径已脱敏〕` | 4,081 | 143 | 172,449,511 | **0** | 0.64 s |
| S2 sub | `〔本地路径已脱敏〕` | 1,276 | 55 | 60,166,418 | **0** | 0.56 s |
| **S3 归档区** | `〔归档区〕` | **39,949** | 19,475 | **1,394,150,914** | **0** | 20.17 s |

**内容哈希**：三源**全量穷举**（⛔ 0 抽样、⛔ 0 以 bytes 预筛缩小搜索面），逐件算 **Git-blob-SHA-1-12 ＋ SHA-256-12 ＋ bytes**；读错误 **0**（repo 4,083 / sub 1,276 / archive 39,949）。
📌 repo 侧两次测量 4,081 → 4,083 件、172,449,511 → 183,264,058 B：测量窗内有**并发写入**（他棒 `.tmp/` 产物，与 `KD-MC-10` 之告诫一致）。**归档区侧两测逐项一致**（见 §8），本件结论不受此并发影响。

**SHA 量纲之交叉核对（独立实测）**：对比件 §5-1／§5-2 表内所载「回执载删前 SHA-1-12」与回执 R-S4 逐件表实测值 —— **21/21 MATCH、81/81 MATCH** ✅（⛔ 0 凭记忆转述，两源皆程序化解析）。

---

## §2 §5-1 之 21 件 · 归档区逐件对账（KD-MC-06 之实测）

| 判 | 件数 |
|---|--:|
| **相符**（归档区有与远端删前 blob **逐位相符**之副本：Git-blob-SHA1-12 ＋ bytes 双相等） | **20** |
| **不符**（归档区有候选而内容不符） | **0** |
| **不在**（归档区三通道皆 0 命中） | **1** |

**相符 20 件之落点分布**：`_remote_delete_face_pullback_2026_10_18_kimi_supplement14/_september_workspace/` **13**（＝回执 R-S3 自承之「weak 13」拉回集，13/13 相符 ✅）＋ `_remote_delete_face_pullback_2026_10_18/_september_workspace/` **7**。

**唯一「不在」件**：`results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` —— 归档区三通道（路径／文件名／内容）**皆 0 命中**；然 **repo 侧有内容同一副本**：`〔幽灵引用·未上传:REVIEWER_B_TMP_RERUN_2026_09_15.md〕`，fresh read 复算 Git-blob-SHA1-12 ＝ `3ef2e8075f1b` ＝ 回执删前值 **MATCH**（6/6 之第 1 件，见 §9-C）。
📌 故对比件 §5-1 之推断「相符副本**只能在归档区**」——**20/21 成立，1/21 不成立**（其相符副本在 repo 之拉回落地面，不在归档区）。**⛔ 0 判对比件失实**（其表述为条件式推断，本棒只补实测）。

| 仓内副本 SHA-1-12（对比件载） | 路径 | 回执删前 SHA-1-12 | 归档区判定 | 归档区具名副本（＋他源） |
|---|---|---|---|---|
| 2418872d1612 | `.tmp/_audit3b.txt` | `e992573fbe2f` | 相符 | 〔归档件引用·未上传:_audit3b.txt〕 |
| f510e8e32a74 | `.tmp/_audit_part3_out.txt` | `0c62f640ffcf` | 相符 | 〔归档件引用·未上传:_audit_part3_out.txt〕 |
| ad89424325a2 | `.tmp/_audit_part4.txt` | `43a8ce00dc25` | 相符 | 〔归档件引用·未上传:_audit_part4.txt〕 |
| e60f811604cc | `.tmp/_r6_evidence.py` | `239cad89b5c5` | 相符 | 〔归档件引用·未上传:_r6_evidence.py〕 |
| 6dff3aa38b81 | `.tmp/_trae_audit_part3.py` | `6a409f23309c` | 相符 | 〔归档件引用·未上传:_trae_audit_part3.py〕 |
| d3afcff64d72 | `.tmp/_trae_audit_part3b.py` | `13511b18379a` | 相符 | 〔归档件引用·未上传:_trae_audit_part3b.py〕 |
| c3e09bc0f03a | `.tmp/_trae_audit_part4.py` | `7f2fba38c479` | 相符 | 〔归档件引用·未上传:_trae_audit_part4.py〕 |
| fbcc85ae9b1d | `docs/V3X/D7_ONE_PAGE_SUMMARY_TEMPLATE.md` | `223297c38fb6` | 相符 | 〔归档件引用·未上传:D7_ONE_PAGE_SUMMARY_TEMPLATE.md〕 |
| 62e38ee7b8f3 | `results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` | `3ef2e8075f1b` | 不在 | 归档区 0 命中；repo `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/REVIEWER_B_TMP_RERUN_2026_09_15.md` |
| 3b131b61a712 | `results/_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | `a7a80c786fa2` | 相符 | 〔归档件引用·未上传:_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md〕 |
| 3d1f7d0174b7 | `results/_g10_threshold_closed_domain_judgment_2026_10_11.md` | `1397dbcbeafe` | 相符 | 〔归档件引用·未上传:_g10_threshold_closed_domain_judgment_2026_10_11.md〕 |
| 3a0774bd6a95 | `results/_ghostref_copy_log_2026_09_23.json` | `be98a7b238b0` | 相符 | 〔归档件引用·未上传:_ghostref_copy_log_2026_09_23.json〕 |
| 69fade5420f2 | `results/_glm_response_v2_template_2026_09_18.md` | `9da3d432a134` | 相符 | 〔归档件引用·未上传:_glm_response_v2_template_2026_09_18.md〕 |
| 29b45ba24ab9 | `results/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md` | `9aabb430172f` | 相符 | 〔归档件引用·未上传:_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md〕 |
| aec1c93d1e90 | `results/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md` | `1842e1b1dd01` | 相符 | 〔归档件引用·未上传:_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md〕 |
| 3d51bfffd3d1 | `results/_t1_qwen_temp_sweep_executor_2026_10_09.py` | `a87adc2ed532` | 相符 | 〔归档件引用·未上传:_t1_qwen_temp_sweep_executor_2026_10_09.py〕 |
| 4fa77864eca7 | `results/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md` | `b633a675c9de` | 相符 | 〔归档件引用·未上传:_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md〕 |
| 2b096d07501f | `results/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py` | `ff15ac539b98` | 相符 | 〔归档件引用·未上传:_t1_qwen_temp_sweep_r2_executor_2026_10_09.py〕 |
| b4f964ab73a9 | `results/_t1_qwen_temp_sweep_r2_result_2026_10_09.json` | `308419654ed7` | 相符 | 〔归档件引用·未上传:_t1_qwen_temp_sweep_r2_result_2026_10_09.json〕 |
| e32047ecc3f3 | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | `d1905830b2bd` | 相符 | 〔归档件引用·未上传:_t1_qwen_temp_sweep_verdict_2026_10_09.md〕 |
| aa3a94399724 | `tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_tmp_cleanup_2026_09_28.md` | `a2c177ec2bfe` | 相符 | 〔归档件引用·未上传:_v4_tmp_cleanup_2026_09_28.md〕 |

---

## §3 §5-2 之 81 件 · 归档区在位逐件对账（KD-MC-07 之实测）

| 判 | 件数 |
|---|--:|
| **在归档区（内容相符 · 具名路径）** | **76** |
| 在归档区（内容异） | **0** |
| **不在归档区** | **5** |

**在位 76 件之落点分布**（共 **86 份**副本，10 件各有 2 份内容同一副本）：`_remote_delete_face_pullback_2026_10_18/_september_workspace/` **82** 份 ／ `_movedout_scratch_2026_10_01/errata_drafts_2026_10_01/` **2** 份 ／ `_remote_delete_face_pullback_2026_10_18_kimi_supplement14/_september_workspace/` **1** 份（＝回执 R-S3 之「none 1」`docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md`，1/1 相符 ✅）／ `results/_remote_version_freeze_2026_10_12/` **1** 份（异名命中：`_v4_tmp_cleanup_2026_09_28.md.remote_2026_10_12`）。

**「不在」5 件之共同形态**：全属 `results/_archive_2026_09_20/` 族，归档区三通道皆 0 命中；然 **repo 侧皆有内容同一副本**：`〔幽灵引用·未上传:…〕`，fresh read 复算 **5/5 MATCH**（见 §9-C）。

| 回执载 bytes | 路径 | 归档区在位判定 | 归档区具名副本（＋他源） |
|---:|---|---|---|
| 4142 | `.tmp/_b12_q4_anchor_probe_2026_09_29.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_b12_q4_anchor_probe_2026_09_29.py〕 |
| 1543 | `.tmp/_c5_b_prestate_baseline.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_c5_b_prestate_baseline.json〕 |
| 2672 | `.tmp/_cpatomic_keyscan_2026_09_28.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_cpatomic_keyscan_2026_09_28.json〕 |
| 357 | `.tmp/_cpatomic_patch_manifest_2026_09_28.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_cpatomic_patch_manifest_2026_09_28.json〕 |
| 6476 | `.tmp/_cpatomic_pycache_post_2026_09_28.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_cpatomic_pycache_post_2026_09_28.json〕 |
| 10772 | `.tmp/_cpatomic_pycache_pre_2026_09_28.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_cpatomic_pycache_pre_2026_09_28.json〕 |
| 3144 | `.tmp/_cpatomic_verify_2026_09_28.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_cpatomic_verify_2026_09_28.json〕 |
| 1158 | `.tmp/_d4_relabel_run1.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_d4_relabel_run1.log〕 |
| 20994 | `.tmp/_diff21_anchor_drift.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_diff21_anchor_drift.txt〕 |
| 66339 | `.tmp/_docwriter_wt2_enum_final_2026_09_30.tsv` | 在归档区·内容相符 | 〔归档件引用·未上传:_docwriter_wt2_enum_final_2026_09_30.tsv〕 |
| 2248 | `.tmp/_e3536.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_e3536.txt〕 |
| 16236 | `.tmp/_e50_c1.md` | 在归档区·内容相符 | 〔归档件引用·未上传:_e50_c1.md〕；〔归档件引用·未上传:_e50_c1.md（归档区〕 2 份内容同一副本，全列如左） |
| 17220 | `.tmp/_e50_c2.md` | 在归档区·内容相符 | 〔归档件引用·未上传:_e50_c2.md〕；〔归档件引用·未上传:_e50_c2.md（归档区〕 2 份内容同一副本，全列如左） |
| 611 | `.tmp/_final_sha.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_final_sha.txt〕 |
| 435 | `.tmp/_gaps.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_gaps.txt〕 |
| 2377 | `.tmp/_gaps2.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_gaps2.txt〕 |
| 634458 | `.tmp/_l14v3_aggregated_10cells.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_l14v3_aggregated_10cells.json〕 |
| 243 | `.tmp/_l14v3_aggregated_10cells_v2.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_l14v3_aggregated_10cells_v2.json〕；〔归档件引用·未上传:_l14v3_aggregated_10cells_v3.json（归档区〕 2 份内容同一副本，全列如左） |
| 243 | `.tmp/_l14v3_aggregated_10cells_v3.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_l14v3_aggregated_10cells_v2.json〕；〔归档件引用·未上传:_l14v3_aggregated_10cells_v3.json（归档区〕 2 份内容同一副本，全列如左） |
| 2233138 | `.tmp/_l14v3_aggregated_10cells_v4.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_l14v3_aggregated_10cells_v4.json〕 |
| 1445 | `.tmp/_l14v3_n26_metrics.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_l14v3_n26_metrics.json〕 |
| 2579 | `.tmp/_l14v3_n26_metrics_v2.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_l14v3_n26_metrics_v2.json〕 |
| 2292 | `.tmp/_l14v3_sensitivity_v2.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_l14v3_sensitivity_v2.json〕 |
| 352 | `.tmp/_pk_probe2.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pk_probe2.py〕 |
| 462 | `.tmp/_pk_probe3.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pk_probe3.py〕 |
| 176 | `.tmp/_pk_probe4.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pk_probe4.py〕 |
| 338 | `.tmp/_pk_probe5.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pk_probe5.py〕 |
| 257 | `.tmp/_pk_probe6.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pk_probe6.py〕 |
| 1636 | `.tmp/_pk_probe7.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pk_probe7.py〕 |
| 1636 | `.tmp/_pk_probe8.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pk_probe8.py〕 |
| 633 | `.tmp/_pkf34_probe1.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pkf34_probe1.py〕 |
| 604 | `.tmp/_pkf34_probe2.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_pkf34_probe2.py〕 |
| 2876 | `.tmp/_probe21_fields.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_probe21_fields.py〕 |
| 3867 | `.tmp/_r10.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_r10.txt〕 |
| 4106 | `.tmp/_r11_ctx.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_r11_ctx.txt〕 |
| 17 | `.tmp/_r1_scratch_bom.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_r1_scratch_bom.json〕 |
| 15 | `.tmp/_r1_scratch_corrupt_a.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_r1_scratch_corrupt_a.json〕 |
| 14 | `.tmp/_r1_scratch_good.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_r1_scratch_good.json〕 |
| 75 | `.tmp/_r4_cleanup_worker_keyscan_results_2026_09_29.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_r4_cleanup_worker_keyscan_results_2026_09_29.json〕 |
| 2313 | `.tmp/_r4_key_scan_r1_files_2026_09_27.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_r4_key_scan_r1_files_2026_09_27.json〕 |
| 1014 | `.tmp/_r4_key_scan_results_2026_09_24.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_r4_key_scan_results_2026_09_24.json〕 |
| 30834 | `.tmp/_r6_evidence.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_r6_evidence.txt〕 |
| 2634 | `.tmp/_recheck_r1_runA.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_recheck_r1_runA.log〕；〔归档件引用·未上传:_recheck_r1_runB.log（归档区〕 2 份内容同一副本，全列如左） |
| 2634 | `.tmp/_recheck_r1_runB.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_recheck_r1_runA.log〕；〔归档件引用·未上传:_recheck_r1_runB.log（归档区〕 2 份内容同一副本，全列如左） |
| 2568 | `.tmp/_recheck_r1_runC.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_recheck_r1_runC.log〕；〔归档件引用·未上传:_recheck_r1_runD.log（归档区〕 2 份内容同一副本，全列如左） |
| 2568 | `.tmp/_recheck_r1_runD.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_recheck_r1_runC.log〕；〔归档件引用·未上传:_recheck_r1_runD.log（归档区〕 2 份内容同一副本，全列如左） |
| 8983 | `.tmp/_rj5_convention_check_2026_09_27.out.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_rj5_convention_check_2026_09_27.out.json〕 |
| 1384 | `.tmp/_rj5_mapping_test_2026_09_27.out.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_rj5_mapping_test_2026_09_27.out.txt〕 |
| 1420 | `.tmp/_run_output.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_run_output.log〕 |
| 1588 | `.tmp/_t15_inspect3_out.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15_inspect3_out.txt〕 |
| 3057 | `.tmp/_t15_inspect4_out.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15_inspect4_out.txt〕 |
| 933 | `.tmp/_t15_inspect5_out.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15_inspect5_out.txt〕 |
| 6659 | `.tmp/_t15_inspect6_out.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15_inspect6_out.txt〕 |
| 3647 | `.tmp/_t15_inspect7_out.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15_inspect7_out.txt〕 |
| 491 | `.tmp/_t15_percell.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15_percell.txt〕 |
| 772 | `.tmp/_t15_percell_out.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15_percell_out.txt〕 |
| 914 | `.tmp/_t15r2_checkpoint_warn.jsonl` | 在归档区·内容相符 | 〔归档件引用·未上传:_t15r2_checkpoint_warn.jsonl〕 |
| 19595 | `.tmp/_tail3_atomic_make_2026_09_29.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_tail3_atomic_make_2026_09_29.json〕 |
| 5784 | `.tmp/_tail3_atomic_refs_2026_09_29.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_tail3_atomic_refs_2026_09_29.json〕 |
| 11116 | `.tmp/_tail3_atomic_verify_2026_09_29.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_tail3_atomic_verify_2026_09_29.json〕 |
| 174424 | `.tmp/_v16_full_decoded.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_v16_full_decoded.txt〕；〔归档件引用·未上传:_v16_tail_dump.txt（归档区〕 2 份内容同一副本，全列如左） |
| 174424 | `.tmp/_v16_tail_dump.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_v16_full_decoded.txt〕；〔归档件引用·未上传:_v16_tail_dump.txt（归档区〕 2 份内容同一副本，全列如左） |
| 3471 | `.tmp/_v16_tail_only.txt` | 在归档区·内容相符 | 〔归档件引用·未上传:_v16_tail_only.txt〕 |
| 5699 | `.tmp/_v3r1_diag.json` | 在归档区·内容相符 | 〔归档件引用·未上传:_v3r1_diag.json〕 |
| 5062 | `.tmp/_v3r1_run1.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_v3r1_run1.log〕 |
| 2066 | `.tmp/_v3r1_run2.log` | 在归档区·内容相符 | 〔归档件引用·未上传:_v3r1_run2.log〕 |
| 19685 | `.tmp/_v5_item21_patch.diff` | 在归档区·内容相符 | 〔归档件引用·未上传:_v5_item21_patch.diff〕 |
| 16768 | `.tmp/_v5_item21_patched_b1_semA_none_default.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_v5_item21_patched_b1_semA_none_default.py〕 |
| 16829 | `.tmp/_v5_item21_patched_b1_semB_none_skip.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_v5_item21_patched_b1_semB_none_skip.py〕 |
| 16036 | `.tmp/_v5_item21_patched_b2_semA_none_default.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_v5_item21_patched_b2_semA_none_default.py〕 |
| 16097 | `.tmp/_v5_item21_patched_b2_semB_none_skip.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_v5_item21_patched_b2_semB_none_skip.py〕 |
| 15778 | `.tmp/_v5_item21_patched_b3_semA_none_default.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_v5_item21_patched_b3_semA_none_default.py〕 |
| 15839 | `.tmp/_v5_item21_patched_b3_semB_none_skip.py` | 在归档区·内容相符 | 〔归档件引用·未上传:_v5_item21_patched_b3_semB_none_skip.py〕 |
| 95139 | `.tmp/verif_doubt6/baseline_pre.json` | 在归档区·内容相符 | 〔归档件引用·未上传:baseline_pre.json〕 |
| 4397 | `docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md` | 在归档区·内容相符 | 〔归档件引用·未上传:D3_ONLINE_MIDTERM_TEMPLATE.md〕 |
| 1171 | `results/_archive_2026_09_20/_audit_temp_inspect_minimax_m3.py.bak` | 不在 | 归档区 0 命中；repo `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_temp_inspect_minimax_m3.py.bak` |
| 1158 | `results/_archive_2026_09_20/_audit_temp_inspect_workers.py.bak` | 不在 | 归档区 0 命中；repo `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_temp_inspect_workers.py.bak` |
| 18023 | `results/_archive_2026_09_20/_audit_temp_stage1_tra_breakdown.py.bak` | 不在 | 归档区 0 命中；repo `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_audit_temp_stage1_tra_breakdown.py.bak` |
| 5 | `results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` | 不在 | 归档区 0 命中；repo `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_openrouter_emb_runner.bak.note` |
| 1270 | `results/_archive_2026_09_20/_tmp_probe_archive` | 不在 | 归档区 0 命中；repo `_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_tmp_probe_archive` |
| 5131 | `results/_v4_tmp_cleanup_2026_09_28.md` | 在归档区·内容相符 | 〔归档件引用·未上传:_v4_tmp_cleanup_2026_09_28.md.remote_2026_10_12〕 |

---

## §4 回执 R-S3「279 件三源相符」之核验面（**逐件之据** · ⛔ 0 判真伪）

**主张之原文**（回执 R-S3，`85f8777f139c`）：「**279 件**：本地区三源（repo／sub／归档区）既有副本之内容 SHA 与远端逐件相符——副本在手，删除无损」；「**14 件**：本地无相符副本（weak 13 ＋ none 1）……删前已逐件拉回至归档区独立子目录」。

**本棒实测之结论面**：

| 项 | 实测 |
|---|---|
| R-S4 逐件表行数 ／ 唯一路径 | **293 行 ／ 291 路径**（序号 1..293 **0 缺号**；重复见 §6） |
| 293 行中「三源至少一源存在内容相符副本」者 | **293**（Git-blob-SHA1-12 ＋ bytes 双相等） |
| 293 行中「三源皆无相符副本」者 | **0** |
| **扣回执自承之 14 件拉回集后之 279 集** | **279/279 相符** ⇒ 与 R-S3 之主张**相符**（逐件之据见 §2／§3／本节分布） |
| 279 集中「含归档区副本」 | **226** ／ **53** 无归档区副本（相符副本在 repo 或 sub） |

**279 集之相符副本所在源之分布**（一件可多源命中，故列和 279）：

| repo | sub | 归档区 | 行数 |
|:--:|:--:|:--:|--:|
| ✔ | ✘ | ✔ | 154 |
| ✘ | ✘ | ✔ | 69 |
| ✔ | ✘ | ✘ | 27 |
| ✘ | ✔ | ✘ | 18 |
| ✔ | ✔ | ✘ | 8 |
| ✘ | ✔ | ✔ | 3 |

📌 **本棒只出此证据面，⛔ 0 判回执失实与否**（判定归 verifier／PI）。本面之可复核入口：`.tmp/_archive_ro_verify_recon_2026_10_18.json`（293 行逐件之三通道命中，含绝对路径）。

---

## §5 拉回 14 件 · 落点在位与内容之实测

| 判 | 实测 |
|---|--:|
| 落点根在位 | ✅ `〔归档件引用·未上传:_remote_delete_face_pullback_2026_10_18_kimi_supplement14〕` |
| 盘上件数 | **14**（0 覆写既有归档之主张**成立**：该目录为独立子目录） |
| **14/14 内容相符**（Git-blob-SHA1-12 ＝ 回执删前 SHA-12 ＋ bytes 相等） | **14 / 14** ✅ |

⚠ **落点路径形态差（登记为 `KD-ARV-01`）**：实体路径为 **`<根>\_september_workspace\<rel>`**（如 `〔归档件引用·未上传:D7_ONE_PAGE_SUMMARY_TEMPLATE.md〕`）；而回执 R-S3「拉回落点」栏写作 **`<根>\<rel>`**（**漏 `_september_workspace\` 一段**）。
📌 影响面：**按回执字面路径取件将 14/14 全部落空**；内容之无损**不受影响**（实体俱在且相符）。本棒 ⛔ 0 代改回执、⛔ 0 移动归档区实体。

---

## §6 同一性与缺件之登记（防重复计数）

| 分支 | 实测 |
|---|---|
| **SAME_IDENTITY（81 件内）** | **10 件**在归档区各有 **2 份内容同一副本**（`_e50_c1.md`／`_e50_c2.md`／`_l14v3_aggregated_10cells_v2.json` ＋ `_v3.json`／`_recheck_r1_runA.log` ＋ `_runB.log`／`_runC.log` ＋ `_runD.log`／`_v16_full_decoded.txt` ＋ `_v16_tail_dump.txt`）——**计数须分「81 件」与「86 份副本」** |
| 同上之回执侧成因 | 上述 10 件在 R-S4 内本即**同删前 SHA、不同路径**之 4 组：`b412df2c3d70`（v2/v3）｜`eeb137ee0997`（runA/B）｜`ddd32d5b8398`（runC/D）｜`8afc120c47f0`（v16_full/tail） |
| **CONFLICT（同名异内容）** | **0**（21 ＋ 81 两面内，归档区无「同名而内容不符」之候选） |
| **MISSING_TRUE（三处均无）** | **0** —— 归档区 0 命中之 6 件（21 中 1、81 中 5）**均有 repo 内容同一副本** ⇒ **⛔ 0 断言为真缺件，⛔ 0 编造来源**（本棒未发现任何一件三处皆无） |
| **GHOST_REF（引用在、实体仓外）** | 本面未触发（本棒 0 判定引用之有效性） |

---

## §7 新出 KD 登记（编号域 `KD-ARV-*` · 落笔前实测全仓 **0 占用** ✅）

| KD | 面 | 事实（实测） | 处置 |
|---|---|---|---|
| `KD-ARV-01` | 引用路径规范 | 回执 R-S3 之「拉回落点」写作 `<根>\<rel>`，**盘上实体为 `<根>\_september_workspace\<rel>`**（14/14 内容相符，仅形态差一层） | **候 PI 裁**是否更正回执之路径表述；本棒 ⛔ 0 代改、⛔ 0 动归档区实体 |
| `KD-ARV-02` | 计数口径 | R-S4 逐件表 **293 行 ≠ 291 唯一路径**：`audits_dataset_health.json`（#218／#292）、`docs/DATASET_HEALTH_v2.md`（#220／#293）各 2 次，**删前 SHA 与 bytes 全同、commit 不同** | **登记**：一切计数须分「293 行／291 路径」；⛔ 0 静默去重（本棒已显式登记） |
| `KD-ARV-03` | 「无副本」之口径 | 21 中 1、81 中 5 共 **6 件**在 repo 之 `_remote_pullback_2026_10_17/_september_workspace/` 有内容同一副本；**repo∪sub 任一路径**内容相符 ＝ **210**，**规范路径**相符 ＝ **191**（与对比件所载 191 **逐位吻合**） | **登记为口径差（非矛盾）**；⛔ 0 判对比件失实；⛔ 0 以任一口径覆盖另一口径 |
| `KD-ARV-04` | 仪器缺陷（自审） | 本棒首轮解析器**未剥反引号** ⇒ §5-1／§5-2／R-S4 **全返 0 行**（假阴性，若不察将误报「清单不存在」） | **已修仪器**（`h()` 剥除后比对）；⛔ 0 改文本以迁就仪器；⛔ 0 以首轮之 0 行充结论 |
| `KD-ARV-05` | 仪器之量纲 | 归档区 **1.394 GB／39,949 件全量**算 Git-blob-SHA1，**⛔ 0 以 bytes 预筛**缩小搜索面（免判据依赖回执 bytes 之正确性） | 已实施 ✅ |

📌 **⛔ 0 闭任何既有 KD**（含 `KD-MC-06`／`KD-MC-07`）——本件仅提供其实测之据，闭否归 PI。

---

## §8 0 触动自证（归档区只读之证）

| 判据 | 前测 | 复测 | Δ |
|---|--:|--:|--:|
| 归档区件数 | 39,949 | **39,949** | **0** |
| 归档区字节总量 | 1,394,150,914 | **1,394,150,914** | **0** |
| 归档区遍历错误 | 0 | **0** | 0 |

**`ARCHIVE_ZERO_TOUCH = PASS`** ✅ ｜ 归档区根 mtime ＝ `2026-10-18 12:55:20`（**早于本棒作业**，未被本棒触碰）。
本棒对归档区之动作全表：**读字节 · 列目录 · 算哈希**；**0 写 · 0 删 · 0 移 · 0 改名 · 0 新建临时件**。本棒全部写落于 repo 之 `.tmp/`（证据件）与 `results/`（本交付件）。

---

## §9 仪器自审（**测量仪器自身即误差源**）

- **A · 交叉复现他棒之数**：以本棒独立测得之「repo∪sub **规范路径**内容相符 ＝ 191」，与对比件 §5-0 所载 **191** **逐位吻合** ⇒ 本棒之量纲与解析口径**与前棒一致**（⛔ 0 以文本迁就仪器）。
- **B · 假阴性之修**（`KD-ARV-04`）：首轮 0 行系仪器缺陷，**已修仪器**；修后 21／81／293 三表皆**行数自证**（21、81、序号 1..293 0 缺号）。
- **C · 例外件之独立复算**：6 件「归档区 0 命中」者，另起 fresh read（**不复用哈希索引**）逐件重算 Git-blob-SHA1 —— **6/6 MATCH** ✅。
- **D · ⛔ 0 抽样 · ⛔ 0 假碰撞**：全量算 SHA-1（Git blob 量纲）；⛔ 0 以 SHA-256 对 Git-SHA1（KD-MC-04 之 2,862 件假碰撞教训）。
- **E · 三通道互证**：路径／文件名／内容三通道皆跑；6 件之判读依赖通道③之内容证据，非路径猜测。

---

## §10 如实交代 · 未软化 · 边界

1. **21 件之「不在 1」是「归档区」口径，不是「三源皆无」** —— 该件相符副本在 repo 之拉回落地面。三源口径：**21/21 有相符副本**。
2. **81 件之「不在 5」同为归档区口径** —— 5 件皆有 repo 内容同一副本。三源口径：**81/81 有相符副本**。
3. **「相符」之定义严于「有副本」**：本件之相符 ＝ Git-blob-SHA1-12 ＋ bytes **双相等**；⛔ 0 以「路径在位」充「副本无损」。
4. **计数两处须分口径**：R-S4「293 行／291 路径」；§5-2「81 件／86 份副本」。
5. **本棒 ⛔ 0 判回执失实与否**（§4 只列逐件之据；判定归 verifier／PI）；⛔ 0 闭 `KD-MC-06`／`KD-MC-07`；⛔ 0 落五终判；⛔ 0 宣告任何段毕；⛔ 0 代 PI 裁。
6. **时效限定**：本件之本地侧读数为**测量时刻**之快照（repo 侧测量窗内有并发写入，见 §1）；归档区侧两测一致。
7. **0 实验 · 0 联网 · 0 凭据**：本面纯本地只读哈希比对，⛔ 0 触远端、⛔ 0 触 GLM 面。

---

## §11 交付与验收（自证）

| 判据 | 实测 |
|---|---|
| A-1 落前检查 | `Test-Path=False` ＋ glob **0 命中** ✅（落盘前实测） |
| A-2 落盘方式 | `io.open(encoding='utf-8', newline='\n')` 直写 ｜ **UTF-8 无 BOM · 纯 LF（CRLF ＝ 0）** |
| A-3 字节级自报 | **落盘后由异工具亲测回读**并自报于棒回执；旁证件：`.tmp/_archive_ro_verify_deliver_selfcert_2026_10_18.txt`（因**自指哈希不可解**，⛔ 0 内嵌于本件——沿对比件 §7-5 之体例） |
| A-4 引件先测指纹 | §0 三件皆**先实测** ✅ |
| A-5 三源遍历错误 | repo **0** ／ sub **0** ／ 归档区 **0** ✅ |
| A-6 0 触 | 归档区 **0 写 0 删 0 移 0 改名**（§8 两测一致）✅ ｜ GLM 面 0 触 ｜ 远端 0 触 |
| A-7 边界 | 0 闭既有 KD · 0 落五终判 · 0 宣告段毕 · 0 代 PI 裁 · 0 实验 · 0 联网 · 0 凭据 |

---

**件止** ｜ *evidence-auditor（证据链审计官）* · 2026-10-18 · **归档区只读核验件（取证面）· 候 PI 阅 · ⛔ 0 代裁** —— 本件仅出**第三源实测之证据面**；**⛔ 0 判回执或对比件之真伪**（判定归 verifier／PI）；⛔ 0 闭既有 KD（含 `KD-MC-06`／`KD-MC-07`）· ⛔ 0 落五终判 · ⛔ 0 宣告①毕/②毕/③毕/④毕/⑤毕 · ⛔ 0 代 PI 裁 · ⛔ 0 实验 · ⛔ 0 联网 · ⛔ 0 触 GLM 面 · ⛔ 0 写/删/移/改名归档区 ｜ **既有件触动数 ＝ 0**（append-only）
