# C 类归档索引件（`_results_c_class_index_2026_10_22.md`）

| 项 | 值 |
|---|---|
| 自路径 | `〔幽灵引用·未上传:_results_c_class_index_2026_10_22.md〕` |
| 棒别 | worker（执行面）· 观测时点 2026-10-22 13:54:25 |
| 令源 | PI 2026-10-22 排队令：「整理文件夹清放开手脚，无论远端仓库或本地都过于臃肿」 |
| 前案（⛔ 0 回改·⛔ 0 重复造案） | `_cleanup_noise_register_2026_10_21.md`（`5ca28bb4c73a`）／`_results_index_v2_2026_10_21.md`（`8487e4a34d29`）／`_results_split_proposal_2026_10_21.md`（`38eff36f1438`）／`_ghost_reference_register_2026_10_21.md`（`e927dfce3464`）／`_bloat_inventory_2026_10_22.md`（`3c55ea8be914`）／`_ghost_reference_audit_2026_10_22.md`（`37659d4a398a`） |
| 铁律 | ⛔ 0 删／⛔ 0 移／⛔ 0 改名／⛔ 0 建目录／⛔ 0 触归档区（仅列名与件数）／⛔ 0 触 `GLM` 面／⛔ 0 联网／⛔ 0 读 key／⛔ 0 LLM／⛔ 0 落五终判／⛔ 0 闭 KD／⛔ 0 宣告段毕／⛔ 0 代裁 |
| 状态 | **索引与移动序已出；0 移动 0 删除**（移动须 PI 逐单令） |
| 仪器 | `os.walk` 穷举（遍历错误 0／读错 0）＋ `hashlib.sha256` 逐件指纹 ＋ 全文本引用面自建扫描器（主面 md＋txt＋py＋log） |

## §0 术语（首现附白话）

- **C 类** ＝ 宜归档之件（**白话**：多半已过时或已被新版取代，宜挪去归档区；但**须 PI 逐单令**才可移动——本件只出索引与序，**⛔ 0 移动**）。
- **B 类** ＝ 须 PI 逐单令才可删之件（**白话**：有人引、有证据价值、是留痕或是交付件——删前得 PI 一件一件点头；其清单见 `_cleanup_b_class_list_2026_10_22.md`）。
- **索引件** ＝ 新旧路径映射表（**白话**：一张「件在哪儿」的对照清单；移动前先有它，将来真移动时引用不会失联）。
- **路径式引用** ＝ 引文写的是 `results\xxx\yyy.md` 这样带路之指（**白话**：一挪位置，指针就落空）。
- **裸名引用** ＝ 引文只写 `yyy.md` 不带路（**白话**：挪位置后按名字仍找得到，只是读者少一层定位）。
- **幽灵引用** ＝ 引文指着一个**盘上已无**的件（**白话**：话还在，东西没了）。
- **移动序** ＝ 拟移件按「被引用次数升序」之排定次序（**白话**：越少人引的先挪，风险由低到高）。
- **对照表** ＝ 每批移动前后各测一次的「件数／字节／引用数」三联表（**白话**：挪前记一笔、挪后再记一笔，对得上才算没出错）。
- **在途** ＝ 观测当日（2026-10-22）仍被并行工作面生成或改动的件（**白话**：正在用的东西，⛔ 0 擅动）。

## §1 本件之收录口径（界分·先说清）

| 项 | 值 |
|---|---|
| C 类收录范围 | 同族旧版（C1）＋ 早期纪元（C2）＋ 审计探针族（C3）＝ **315 件／124,195,869 B** |
| C1 之据 | `_cleanup_noise_register_2026_10_21.md` §4.1 在册 28 件名单——本棒**逐件复其在盘**（28／28 在盘，0 缺） |
| C2 之据 | mtime < 2026-09-20 全仓实测 470 件 → **剔 D 类禁动面与他面后留 209 件／9,130,187 B**（剔除明细见 §5） |
| C3 之据 | `results\.tmp\` 工作面全件 78 件（**注**：前案 10-22 00:5x 载 58 件／3.0 MB；本棒实测 78 件／108.7 MB——差额为当日新增之 s18 幽灵审计仪器输出 102.5 MB，**在途**） |
| 明确**不**收录 | `.tmp` 工作面之体量压舱物（>5 MB `.json`／`.tsv`／0 字节件）——属 B 类（宜**删**非宜**移**），已列于件二；`results` 根层 `.md` 交付件（1,031 件）属 B8/D 面 |
| 拟归何处之三分 | `deposon-sub`（探针执行器·保可复算性）／`归档区`（`〔归档区〕`·**⛔ 0 触其内件·仅列名与件数**）／`不移动`（在途／绝对路径钉住／亦入 B 类） |

**C 与 B 之交叠面**：13 件既属 C 类（宜归档）又入 B 类清单 ⇒ 彼等拟归处标「不移动（亦入 B 类·宜经删之令）」，交叠体量 108,115,582 B。

## §2 C 类逐件索引（拉平·逐件一行）

> 列义：**现路径**（仓根相对，`/` 分隔）｜**SHA-12**（SHA-256 前 12 位·本棒自算）｜**bytes**｜**mtime**｜**被引用次数**（主面 md＋txt＋py＋log 全文本扫描之 basename 命中次数）｜**活引用次数**（扣去快照面之提及——`_c514_remote_blobs` 镜像副本与 SHA 索引内之文本提及，**随快照件存亡，不因本件移动而断**）｜**引者件数**｜**拟归何处**｜**移动后须补之幽灵登记**。

### §2-C1 C1 · 同族旧版（被同族新版取代者） — 28 件／1,111,399 B

| 现路径 | SHA-12 | bytes | mtime | 被引用次数 | 活引用次数 | 引者件数 | 拟归何处 | 移动后须补之幽灵登记 |
|---|---|---|---|---|---|---|---|---|
| results/_achievements_inventory_full_2026_10_09.md | dd3e9806a369 | 372,318 | 2026-10-12 03:20:49 | 229 | 207 | 50 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）165 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_pk_den_layers_out_2026_10_21.txt、.tmp/_pk_f1f7_scan_out.txt …（余 26 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 22 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md | fcb0a673ee5c | 74,043 | 2026-10-12 12:50:06 | 58 | 52 | 40 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）46 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_pk_den_layers_out_2026_10_21.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 30 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 6 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_exp04_h_contrast_readings_2026_10_10.json | 106e8667be2d | 72,704 | 2026-10-10 10:05:05 | 25 | 17 | 19 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_k_v3df_0_1_four_readings_2026_10_09.json | e87937d55471 | 65,507 | 2026-10-09 11:24:10 | 36 | 22 | 28 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 9 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_runface_vs_shape_multidim_reading_2026_10_20.json | 4a9b6c5e47af | 61,109 | 2026-10-20 23:09:30 | 38 | 37 | 25 | 归档区（〔归档区〕） | 活引用（路径式）29 处（.tmp/_v169_append.py、.tmp/_v169_body_p1.md、.tmp/_v169_probe.out.txt …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_pi_card_payload_extraction_2026_10_20.md | f8545e95374f | 53,460 | 2026-10-20 19:02:30 | 50 | 49 | 22 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）40 处（.tmp/_pi_card_payload_write_2026_10_20.py、.tmp/_pi_card_payload_write_stdout_2026_10_20.txt、.tmp/_sup4_repocount.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_worker_c_2026_09_10.json | f6f172820c97 | 51,716 | 2026-09-16 11:01:12 | 37 | 24 | 29 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_worker_b_2026_09_10.json | b1eb668377ce | 49,338 | 2026-09-16 11:01:12 | 29 | 18 | 24 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_gd03_divergence_deliberation_2026_10_21.md | 6ae87e5d08eb | 44,153 | 2026-10-21 20:47:10 | 14 | 13 | 9 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）9 处（.tmp/_pk_f1f7_recheck.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt、results/_buexp_backfill_deliberation_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v4_track2_multimodel_rerun_2026_09_23.json | e3dae2a4bbc2 | 35,011 | 2026-09-23 15:26:47 | 34 | 25 | 30 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_659_compact.txt、.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 9 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v4_pi_cot_v2_verdict.md | eb9ad4193cf2 | 22,340 | 2026-09-24 18:07:05 | 85 | 72 | 56 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）41 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 23 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_ge01_prereg_5anchor_v2.json | f06313373fc6 | 21,629 | 2026-10-15 11:21:14 | 61 | 60 | 38 | 归档区（〔归档区〕） | 活引用（路径式）47 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_dw_meas1_2026_10_21.py、.tmp/_dw_write_ge02_gd03_2026_10_21.py …（余 25 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_d9_relpath_rewrite_map_2026_10_12.md | c3167a531e0e | 21,352 | 2026-10-12 16:16:20 | 31 | 28 | 21 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt、results/_achievements_inventory_full_2026_10_18.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 3 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json | 33ad1c01f745 | 20,398 | 2026-10-01 09:43:44 | 149 | 100 | 56 | 归档区（〔归档区〕） | 活引用（路径式）90 处（.tmp/_c5_b3_rewalk_postcheck_2026_10_01.py、.tmp/_c5_b3_rewalk_utf8check_2026_10_01.py、.tmp/_docwriter_pre_inventory.txt …（余 37 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 49 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_m41_double_readout_contrast_exec_2026_10_14.md | 04f2920e259a | 17,009 | 2026-10-15 09:39:38 | 44 | 43 | 18 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）40 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt、.tmp/hfr_d_out.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_pa_harness_anchor_value_update_v2.json | c43a84c70935 | 16,043 | 2026-10-16 11:42:27 | 40 | 39 | 24 | 归档区（〔归档区〕） | 活引用（路径式）27 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_pk_den_layers_out_2026_10_21.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_d9_e2e_run_register_2026_10_13.md | af22751858d1 | 12,581 | 2026-10-13 00:25:47 | 18 | 14 | 14 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）9 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt、results/_achievements_inventory_full_2026_10_18.md …（余 4 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 4 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md | 0984955b0370 | 11,752 | 2026-10-10 15:11:57 | 46 | 28 | 34 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）23 处（.tmp/_build_receipt_supplement_6.py、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py | 218ef1a99f97 | 11,703 | 2026-09-16 18:20:55 | 41 | 24 | 26 | 归档区（〔归档区〕）·⚠脚本面·须先裁其产出是否已入权威件 | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 17 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_s4_substrate_grid_availability_2026_10_08.json | 66be80ab4b81 | 11,446 | 2026-10-08 16:59:10 | 27 | 21 | 24 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_659_compact.txt、.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 6 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_ge01_prereg_5anchor.json | 4b020eb04605 | 10,701 | 2026-10-14 17:52:13 | 136 | 134 | 53 | 归档区（〔归档区〕） | 活引用（路径式）115 处（.tmp/_build_5anchor_json_draft.py、.tmp/_build_5anchor_json_v1.py、.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md …（余 42 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 2 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/c5_b_group_fix_readings_2026_10_01.json | 2a7749da7c4d | 9,996 | 2026-10-01 09:25:22 | 96 | 64 | 45 | 归档区（〔归档区〕） | 活引用（路径式）54 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 24 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 32 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v5_item21_anchor_recompute_2026_09_28.json | 47177cab0303 | 9,527 | 2026-09-28 20:03:28 | 29 | 22 | 24 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_hash21.py …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 7 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v4_pi_cot_v2_result.json | 1665f367b2c4 | 9,068 | 2026-09-24 17:41:54 | 81 | 69 | 45 | 归档区（〔归档区〕） | 活引用（路径式）43 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_glm_latest_5cells_2026_09_10.py | a3ca05aec6fb | 8,112 | 2026-09-16 11:01:12 | 44 | 24 | 28 | 归档区（〔归档区〕）·⚠脚本面·须先裁其产出是否已入权威件 | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 20 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_pre_execution_report_kimi_2026_10_12.md | 799fbfc334a7 | 7,612 | 2026-10-12 10:44:48 | 22 | 18 | 19 | 不移动（亦入 B 类·宜经删之令） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt、results/_achievements_inventory_full_2026_10_18.md …（余 9 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 4 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v4_pi_cot_v2_ruleset.json | 821465001819 | 5,876 | 2026-09-24 17:41:54 | 58 | 43 | 38 | 归档区（〔归档区〕） | 活引用（路径式）27 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 17 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 15 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_glm_latest_5cells_2026_09_10.json | 83c35597af81 | 4,895 | 2026-09-16 11:01:12 | 33 | 20 | 25 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |

### §2-C2 C2 · 早期纪元（mtime < 2026-09-20·v1.x 实验期·已剔 D 类禁动面） — 209 件／9,130,187 B

| 现路径 | SHA-12 | bytes | mtime | 被引用次数 | 活引用次数 | 引者件数 | 拟归何处 | 移动后须补之幽灵登记 |
|---|---|---|---|---|---|---|---|---|
| results/deposon_v2_phase3_strip_embeddings_2026_09_11.json | 1ded6731cc27 | 2,398,383 | 2026-09-11 11:33:43 | 32 | 24 | 28 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_c5_feasibility_probe.py、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_benchmark_v1_3_details.json | 9fcb6b243e0d | 656,572 | 2026-08-23 00:01:28 | 42 | 28 | 31 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_corpus_eval.json | ca71aa6858e1 | 631,644 | 2026-08-29 01:21:14 | 82 | 54 | 46 | 归档区（〔归档区〕） | 活引用（路径式）42 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_ecr_pa_a0_recompute_2026_10_15.py、.tmp/_ecr_pa_register_src_2026_10_15.md …（余 25 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 28 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json | 25f745609658 | 612,511 | 2026-09-10 17:05:53 | 66 | 40 | 39 | 归档区（〔归档区〕） | 活引用（路径式）39 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_ea_erratum_staging_2026_10_18.md、.tmp/_gh_tree.txt …（余 21 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 26 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v15_diffusion.json | c16d1768d1ca | 519,387 | 2026-08-23 19:21:32 | 45 | 31 | 34 | 归档区（〔归档区〕） | 活引用（路径式）26 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_kd_history_pack_body_2026_10_19.md …（余 21 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v15_diffusion_maxpath_negativeresult.json | 00ee97c82dcc | 416,460 | 2026-08-23 19:21:32 | 41 | 27 | 31 | 归档区（〔归档区〕） | 活引用（路径式）25 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 19 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v19_benchmark_fixes.json | 910c4333eead | 409,104 | 2026-08-24 01:11:01 | 183 | 128 | 134 | 归档区（〔归档区〕） | 活引用（路径式）101 处（.tmp/_build_5anchor_json_draft.py、.tmp/_build_5anchor_json_v1.py、.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md …（余 84 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 55 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_benchmark_v1_4_strategyqa_details.json | a63ebea7b29a | 235,779 | 2026-09-16 11:01:12 | 62 | 49 | 45 | 归档区（〔归档区〕） | 活引用（路径式）46 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 30 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_benchmark_v1_4_gsm8k_details.json | 39f79fce7cdb | 208,350 | 2026-08-23 05:00:55 | 69 | 53 | 52 | 归档区（〔归档区〕） | 活引用（路径式）49 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 36 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 16 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json | 9f88a212a77c | 204,441 | 2026-09-16 11:01:12 | 40 | 23 | 29 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 17 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| audits_outliers.json | 3b1c881c4594 | 132,875 | 2026-08-28 15:53:28 | 35 | 24 | 24 | 归档区（〔归档区〕） | 活引用（路径式）2 处（.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt2b.json | a2ae7997ee67 | 123,331 | 2026-08-29 19:57:39 | 96 | 66 | 48 | 归档区（〔归档区〕） | 活引用（路径式）44 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 26 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 30 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_openrouter_5model_rag_30cells_2026_09_10.json | 2e55c53be25d | 111,710 | 2026-09-10 23:34:43 | 30 | 20 | 24 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v17_fixed_sampler.json | 701ad291a714 | 106,317 | 2026-08-23 21:38:59 | 39 | 25 | 31 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v17_fusion_fix.json | af51da229652 | 106,164 | 2026-08-23 21:31:41 | 122 | 89 | 85 | 归档区（〔归档区〕） | 活引用（路径式）63 处（.tmp/_build_5anchor_json_draft.py、.tmp/_build_5anchor_json_v1.py、.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md …（余 52 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 33 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v17_fusion_fix_tieartifact_negativeresult.json | 556086d9e3bc | 106,125 | 2026-08-23 21:31:36 | 35 | 21 | 28 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v2_phase1_60cells_2026_09_11.json | a18bbc703b42 | 85,508 | 2026-09-16 11:01:12 | 68 | 46 | 43 | 归档区（〔归档区〕） | 活引用（路径式）35 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 20 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 22 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v18_api_supplements.json | 62c1a41e1db8 | 80,624 | 2026-08-23 23:20:04 | 111 | 81 | 77 | 归档区（〔归档区〕） | 活引用（路径式）59 处（.tmp/_build_5anchor_json_draft.py、.tmp/_build_5anchor_json_v1.py、.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md …（余 48 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 30 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_dpath_cross_modal_2026_09_10.json | ab0c2eaff0d1 | 75,964 | 2026-09-16 11:01:12 | 45 | 27 | 34 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt5.json | fca14c5735dd | 72,647 | 2026-08-29 15:35:11 | 67 | 46 | 45 | 归档区（〔归档区〕） | 活引用（路径式）31 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 24 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 21 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v21_gtformal.json | 9d9ae5001c57 | 69,204 | 2026-08-30 15:44:09 | 182 | 128 | 126 | 归档区（〔归档区〕） | 活引用（路径式）94 处（.tmp/_build_5anchor_json_draft.py、.tmp/_build_5anchor_json_v1.py、.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md …（余 73 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 54 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt6.json | 04b90b638bdc | 65,105 | 2026-08-29 15:45:04 | 53 | 39 | 37 | 归档区（〔归档区〕） | 活引用（路径式）28 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 21 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt5b.json | 2907006dbe48 | 56,425 | 2026-08-29 15:44:55 | 52 | 38 | 37 | 归档区（〔归档区〕） | 活引用（路径式）27 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 20 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v19_meanfield.json | 108da40d5d4e | 44,443 | 2026-08-24 01:02:01 | 41 | 23 | 30 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v19_fullrank.json | fbbfd3ef3890 | 42,458 | 2026-08-24 01:04:04 | 41 | 23 | 30 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v16_llm_prior.json | c17b31ae4f3b | 39,974 | 2026-08-23 20:21:38 | 44 | 26 | 30 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md | 4a08521f8de1 | 38,545 | 2026-09-16 11:01:12 | 91 | 58 | 60 | 归档区（〔归档区〕） | 活引用（路径式）52 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_w5_9model_merge_2026_10_09.py …（余 38 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 33 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_bigquiz_eval.json | 283dbc8c5b63 | 35,718 | 2026-08-28 23:54:14 | 37 | 23 | 28 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md | f119f2f30287 | 34,393 | 2026-09-17 15:15:44 | 63 | 45 | 40 | 归档区（〔归档区〕） | 活引用（路径式）37 处（.tmp/_659_compact.txt、.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt …（余 23 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_pf_d1_full_9m5c_2026_09_15.json | fcb5105df0b6 | 33,829 | 2026-09-16 11:01:12 | 50 | 26 | 35 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 24 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json | 4ec04d3d7d8c | 32,995 | 2026-09-16 11:01:12 | 39 | 28 | 27 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/literature_scan_v19.md | 70ea38d5b9c0 | 28,449 | 2026-08-24 00:40:36 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_pf_implementation_2026_09_11.json | 509dcee3b139 | 27,311 | 2026-09-16 11:01:12 | 40 | 24 | 33 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 17 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 16 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_worker_a_2026_09_10.json | 506810017d34 | 25,464 | 2026-09-16 11:01:12 | 31 | 19 | 25 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v3_v7_summary_2026_09_11.json | 063ac8d00542 | 25,049 | 2026-09-16 11:01:12 | 95 | 68 | 53 | 归档区（〔归档区〕） | 活引用（路径式）45 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 30 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 27 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v42_v2_miss_rate_curve_2026_09_16.json | 0a8ed127d6de | 24,435 | 2026-09-16 18:27:36 | 33 | 21 | 28 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/index_v2_2026_09_16.json | efe05ad775de | 24,150 | 2026-09-16 18:39:54 | 171 | 121 | 88 | 归档区（〔归档区〕） | 活引用（路径式）97 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 52 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 50 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json | fbb7677b9cd5 | 23,472 | 2026-09-16 18:20:55 | 34 | 23 | 26 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/REFACTOR_v2.md | 03c8baa18d93 | 23,042 | 2026-08-30 10:39:00 | 28 | 16 | 21 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、deposon_agents.py …（余 9 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_seed_code_30cells_2026_09_10.json | 5149f5cafcf9 | 23,034 | 2026-09-16 11:01:12 | 49 | 29 | 32 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 20 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_quiz_eval.json | 9194ee703218 | 22,623 | 2026-08-28 20:46:44 | 42 | 24 | 29 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_pc_d1_d3_2026_09_15.json | b2046af03610 | 20,408 | 2026-09-15 11:01:56 | 46 | 27 | 34 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_worker_d_2026_09_10.json | fae79888344b | 20,280 | 2026-09-16 11:01:12 | 28 | 16 | 23 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md | 977fe1b48f75 | 19,751 | 2026-09-15 11:31:34 | 85 | 45 | 59 | 归档区（〔归档区〕） | 活引用（路径式）36 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/probe2_out.txt …（余 31 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 40 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/post_edit_verification_v19.md | e262e9d684fe | 19,327 | 2026-08-24 07:49:36 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/GT_FORMALIZATION_v1.md | aeefb8ef6972 | 19,100 | 2026-08-30 15:45:39 | 67 | 43 | 47 | 归档区（〔归档区〕） | 活引用（路径式）33 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/h_src.py …（余 20 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 24 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json | 56401317e62b | 18,592 | 2026-09-10 16:40:43 | 31 | 20 | 24 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_gpt6_teamorouter_30cells_2026_09_10.json | ea38ee252701 | 18,290 | 2026-09-10 17:30:03 | 30 | 19 | 23 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json | b5873afb9d29 | 18,104 | 2026-09-16 18:39:54 | 51 | 41 | 35 | 归档区（〔归档区〕） | 活引用（路径式）37 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_den_layers_out_2026_10_21.txt …（余 23 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt7.json | 896589b673ec | 17,925 | 2026-08-29 17:57:57 | 49 | 30 | 36 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v3_physical_opt_60cells_2026_09_11.json | c659695aa23c | 17,732 | 2026-09-15 10:19:42 | 226 | 158 | 134 | 归档区（〔归档区〕） | 活引用（路径式）88 处（.tmp/_26b_verdict_prep_hashcheck_2026_10_01.py、.tmp/_26b_verdict_prep_validate_2026_10_01.py、.tmp/_659_overlap_digest.txt …（余 70 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 68 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v3_physical_opt_2026_09_11.json | 27f9bd5cc260 | 17,591 | 2026-09-11 12:05:53 | 47 | 36 | 31 | 归档区（〔归档区〕） | 活引用（路径式）26 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_pe_d1_d3_2026_09_15.json | 594d7a8d3de8 | 17,085 | 2026-09-15 10:49:09 | 38 | 19 | 29 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json | f39412103366 | 17,053 | 2026-09-16 12:37:12 | 61 | 38 | 38 | 归档区（〔归档区〕） | 活引用（路径式）37 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 22 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 23 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_baselines.json | 6edb2aec1660 | 16,987 | 2026-08-29 01:17:30 | 282 | 208 | 147 | 归档区（〔归档区〕） | 活引用（路径式）147 处（.tmp/_16_deliverable_write.py、.tmp/_659_overlap_digest.txt、.tmp/_b11_g86_L94_raw.txt …（余 102 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 74 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v17_multigraph.json | 2836605ca12f | 16,896 | 2026-08-23 21:34:43 | 42 | 24 | 30 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md | 6f3c550cec13 | 16,876 | 2026-09-08 21:56:01 | 40 | 20 | 34 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 20 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json | 523b5941c30c | 16,835 | 2026-09-17 11:52:29 | 56 | 24 | 32 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 32 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/review_coach_v2X_draft_r2.md | 67162ab18f9a | 15,721 | 2026-08-29 23:42:38 | 33 | 23 | 25 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_pa_d1_d3_2026_09_15.json | e221792715f8 | 15,604 | 2026-09-15 11:29:23 | 63 | 37 | 43 | 归档区（〔归档区〕） | 活引用（路径式）32 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 23 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 26 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/design_probe_v19.md | c41f1717310e | 13,967 | 2026-08-24 00:49:48 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json | dfbcc5d6fc34 | 13,775 | 2026-09-17 16:37:57 | 50 | 22 | 22 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 28 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json | 4e4a17d43adf | 13,562 | 2026-09-15 13:35:18 | 67 | 45 | 39 | 归档区（〔归档区〕） | 活引用（路径式）34 处（.tmp/_c514_calib_blobs_2026_10_18/results___v3_recheck_05_executor_2026_09_28.py、.tmp/_c514_instr_probe_out_2026_10_18.txt、.tmp/_docwriter_pre_inventory.txt …（余 25 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 22 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md | 79c7321056b8 | 13,419 | 2026-09-15 15:08:22 | 65 | 27 | 45 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 38 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/strip_captions_22.json | 6a2656878745 | 12,798 | 2026-09-11 11:33:40 | 265 | 233 | 152 | 归档区（〔归档区〕） | 活引用（路径式）130 处（.tmp/_c5_b3_rewalk_precheck_2026_10_01.py、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 86 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 32 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20_caption_surface/strip_captions_22.json | 6a2656878745 | 12,798 | 2026-09-11 11:33:40 | 265 | 233 | 152 | 归档区（〔归档区〕） | 活引用（路径式）130 处（.tmp/_c5_b3_rewalk_precheck_2026_10_01.py、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 86 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 32 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md | 2f0765a1d39d | 12,501 | 2026-09-15 11:33:11 | 72 | 39 | 52 | 归档区（〔归档区〕） | 活引用（路径式）30 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 25 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 33 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_pg_v01_9m60c_2026_09_15.json | ab75889ee738 | 11,512 | 2026-09-15 13:35:24 | 86 | 54 | 58 | 归档区（〔归档区〕） | 活引用（路径式）45 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 35 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 32 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md | baef94e393de | 11,478 | 2026-09-10 12:05:42 | 82 | 40 | 52 | 归档区（〔归档区〕） | 活引用（路径式）35 处（.tmp/_c514_calib_blobs_2026_10_18/results___kd_heteronym_classification_disposition_2026_10_09.md、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 29 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 42 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json | 576eaf8d7431 | 11,341 | 2026-09-16 18:39:55 | 39 | 21 | 30 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/PAPER_BRIEF.md | de450c0beffa | 11,296 | 2026-08-30 11:09:37 | 32 | 19 | 25 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/review_coach_v2X_outline.md | 5bebb5e1d329 | 11,295 | 2026-08-29 15:34:49 | 33 | 23 | 24 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_v174_panel2_out.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| paper/v2/outline_v2X.md | 116d193b1607 | 10,476 | 2026-08-30 10:43:36 | 50 | 29 | 34 | 归档区（〔归档区〕） | 活引用（路径式）26 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md …（余 17 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 21 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| paper/v2/related_work_v2X.md | 7fb001add973 | 10,114 | 2026-08-29 15:43:30 | 48 | 25 | 31 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 23 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_game_theory_eval_2026_09_10.json | 3fa0ff2c8c08 | 10,096 | 2026-09-10 21:53:17 | 44 | 34 | 32 | 归档区（〔归档区〕） | 活引用（路径式）25 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 19 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/post_draft_verification_v2X.md | 0c49f2d36088 | 9,979 | 2026-08-29 21:06:20 | 30 | 19 | 22 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_v1.8.md | ad0e445714d9 | 9,850 | 2026-08-23 23:19:47 | 43 | 19 | 24 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 24 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_GT8B.md | 956183753a2e | 9,809 | 2026-08-30 10:38:41 | 35 | 21 | 22 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SYNTHESIS_mind_game.md | 0f36aaeeda6f | 9,191 | 2026-08-29 00:22:08 | 33 | 18 | 22 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 9 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 15 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v16_paired_stats.json | 20bc4288e0de | 9,176 | 2026-08-23 20:59:51 | 38 | 20 | 27 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pa_3_replicator_dynamics_result_2026_09_15.json | d6f233d73c45 | 9,098 | 2026-09-15 15:28:10 | 97 | 67 | 50 | 归档区（〔归档区〕） | 活引用（路径式）56 处（.tmp/_659_compact.txt、.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt …（余 29 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 30 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json | 664e7cc05aec | 9,076 | 2026-09-16 15:50:08 | 48 | 29 | 33 | 归档区（〔归档区〕） | 活引用（路径式）28 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 20 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/CLOSURE_v19_and_v2X_gametheory.md | 84323775a212 | 9,065 | 2026-08-28 15:55:51 | 38 | 24 | 28 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/experiment_design_v19.md | 56ecef878539 | 8,840 | 2026-08-24 00:35:44 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pa_1_rbr_rm_result_2026_09_15.json | c7c59e0d2f6c | 8,753 | 2026-09-15 15:28:10 | 236 | 184 | 107 | 归档区（〔归档区〕） | 活引用（路径式）121 处（.tmp/_659_compact.txt、.tmp/_659_overlap_digest.txt、.tmp/_c514_calib_blobs_2026_10_18/results___v3_recheck_05_executor_2026_09_28.py …（余 65 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 52 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_crossval.json | 76479b7a5ed6 | 8,404 | 2026-08-28 20:27:06 | 51 | 32 | 35 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 17 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt3.json | 35b676773243 | 7,844 | 2026-08-29 15:03:29 | 72 | 44 | 36 | 归档区（〔归档区〕） | 活引用（路径式）37 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 20 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 28 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v19_quickwins.json | 1ec7aba6afd8 | 7,842 | 2026-08-24 01:07:59 | 46 | 28 | 32 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pa_2_potential_game_result_2026_09_15.json | 5c76137d6430 | 7,530 | 2026-09-15 15:28:10 | 68 | 36 | 39 | 归档区（〔归档区〕） | 活引用（路径式）25 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 32 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_GT8B.md | 3545c01e1291 | 7,486 | 2026-08-30 10:37:50 | 38 | 26 | 26 | 归档区（〔归档区〕） | 活引用（路径式）26 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、docs/Findings_GT8B.md …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| audits_dataset_health.json | 4f827071b0b8 | 7,398 | 2026-08-28 15:53:27 | 82 | 69 | 50 | 归档区（〔归档区〕） | 活引用（路径式）12 处（.tmp/_ea_erratum_staging_2026_10_18.md、.tmp/_gh_tree.txt、.tmp/_s3_paths.txt …（余 6 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/review_realign_v2X.md | 3ecb285db3d8 | 7,338 | 2026-08-30 01:03:56 | 29 | 19 | 21 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/index.json | 8423ffe266af | 7,335 | 2026-08-28 23:53:05 | 226 | 166 | 110 | 归档区（〔归档区〕） | 活引用（路径式）94 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_frozen_anchor_verify_2026_10_19.py、.tmp/_gh_tree.txt …（余 61 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 60 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_cot_quiz.json | 94fd018b5cc8 | 7,101 | 2026-08-28 21:13:05 | 39 | 21 | 27 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t2c_advlink.csv | 67d1d8342060 | 6,886 | 2026-08-28 21:32:32 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_photonics.json | 0b7893196d0b | 6,796 | 2026-08-29 01:19:15 | 45 | 25 | 31 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 20 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t2_linkpred.csv | 19555b7d9d43 | 6,750 | 2026-08-28 21:30:43 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t3b_verifiable.csv | f48c9f09a3b4 | 6,731 | 2026-08-28 21:32:32 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t3_mechdesign.csv | 6e8b6e4730a8 | 6,680 | 2026-08-28 21:31:20 | 24 | 15 | 20 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 9 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 9 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t4_poa.csv | 8ba9fada9ead | 6,567 | 2026-08-28 21:31:59 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_risk3_seff_decision_2026_09_11.json | 67867e752f47 | 6,488 | 2026-09-15 10:22:26 | 38 | 17 | 28 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 21 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json | 0c3ede881fb1 | 6,466 | 2026-09-16 11:01:12 | 28 | 17 | 22 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_cpath_simulation_2026_09_10.json | 9466fdbf9c95 | 6,351 | 2026-09-10 20:44:37 | 30 | 19 | 23 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_GT_FORMAL.md | fab607f0e180 | 6,345 | 2026-08-30 15:45:12 | 28 | 16 | 20 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_GT8C.md | 6b09de9911c0 | 6,326 | 2026-08-30 15:50:15 | 58 | 36 | 42 | 归档区（〔归档区〕） | 活引用（路径式）28 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、attacks/a1_delete_anchor.py …（余 17 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 22 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/simple_baseline_failure_analysis.md | 968776002868 | 6,080 | 2026-08-23 00:01:28 | 26 | 14 | 19 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v15_diffusion_summary.json | 5b95d06e66b0 | 6,079 | 2026-08-23 19:22:36 | 33 | 19 | 24 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json | 1e4c065da058 | 5,916 | 2026-09-16 13:23:52 | 41 | 22 | 26 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/REF_VERIFICATION_v2.md | 64f0a3772c12 | 5,860 | 2026-08-30 11:17:21 | 87 | 52 | 24 | 归档区（〔归档区〕） | 活引用（路径式）51 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.trae/scripts/_arxiv_renumber.py …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 35 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t1c_loglinear.csv | c50ff98a95cc | 5,566 | 2026-08-28 21:33:20 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t2b_linkpred.csv | 6de8f0e651c4 | 5,520 | 2026-08-28 21:31:15 | 23 | 15 | 19 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 9 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t1b_classics.csv | 82016e695f48 | 5,450 | 2026-08-28 21:32:04 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt8.json | 2b88948dca19 | 5,396 | 2026-08-29 19:34:34 | 55 | 41 | 41 | 归档区（〔归档区〕） | 活引用（路径式）36 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 27 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t2d_hiding.csv | 5749ce2c5bf7 | 5,377 | 2026-08-28 21:33:27 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_GT3.md | 432ec337d586 | 5,369 | 2026-08-29 14:09:52 | 42 | 29 | 29 | 归档区（〔归档区〕） | 活引用（路径式）29 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、docs/Findings_GT3.md …（余 17 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_v2.0.md | bac61d51fd20 | 5,333 | 2026-08-28 16:54:47 | 61 | 45 | 41 | 归档区（〔归档区〕） | 活引用（路径式）43 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_r2_tool_26_genregister.py …（余 25 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 16 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json | fbcb60cf5102 | 5,266 | 2026-09-16 17:34:14 | 49 | 30 | 33 | 归档区（〔归档区〕） | 活引用（路径式）28 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 20 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v2_phase4_f4_2026_09_11.json | cf7682348617 | 5,212 | 2026-09-11 11:17:21 | 85 | 73 | 50 | 归档区（〔归档区〕） | 活引用（路径式）48 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_v5_c5_b_clause4_consistency_check.py …（余 34 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/space_release_log.json | 110607514753 | 5,056 | 2026-08-28 23:54:50 | 30 | 20 | 24 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0_corrections.md | 5864bbe5adae | 5,012 | 2026-08-29 01:23:08 | 40 | 26 | 30 | 归档区（〔归档区〕） | 活引用（路径式）26 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S4.json | e6045f0920ec | 4,932 | 2026-08-28 17:07:52 | 31 | 22 | 23 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 9 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_9model_30cells_2026_09_10.json | 58ab335ca341 | 4,894 | 2026-09-16 11:01:12 | 31 | 21 | 26 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t1_potential.csv | e110a020954f | 4,833 | 2026-08-28 21:30:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_v2.0_amendment1.md | 3e3a5014cb0e | 4,743 | 2026-08-29 01:22:16 | 36 | 23 | 25 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、docs/Findings_v2.0_corrections.md …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md | c165cd33a362 | 4,587 | 2026-09-11 11:17:21 | 46 | 32 | 32 | 归档区（〔归档区〕） | 活引用（路径式）31 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/deposon_v2_phase4_f4_2026_09_11.log …（余 21 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0_crossval.md | 32d26cb09568 | 4,566 | 2026-08-28 20:28:59 | 36 | 22 | 26 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、_remote_pullback_2026_10_17/_september_workspace/results/_archive_2026_09_20/_letter_to_kimi_push_v3_final_2026_09_17.md …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_volcengine_22caption_embedding_2026_09_10.json | c4b774c8e34c | 4,559 | 2026-09-10 17:36:46 | 77 | 61 | 50 | 归档区（〔归档区〕） | 活引用（路径式）41 处（.tmp/_c5_feasibility_probe.py、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 30 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 16 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0_photonics.md | 9158f54ec248 | 4,377 | 2026-08-30 04:46:02 | 45 | 21 | 25 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 24 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0.md | 7e5dc4b045d8 | 4,364 | 2026-08-28 17:44:22 | 33 | 20 | 23 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_risk1_02940_decision_2026_09_11.json | 2dc8ca9e36c1 | 4,336 | 2026-09-15 10:22:25 | 30 | 19 | 23 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/L_historical_causality.json | 12e0de4bb103 | 4,329 | 2026-08-28 17:38:45 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S6_n60.json | 704e2fd0d021 | 4,296 | 2026-08-28 17:07:52 | 26 | 16 | 20 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json | 088f28524a1d | 4,276 | 2026-09-16 17:43:33 | 40 | 21 | 25 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_GT8.md | edf6f4465ead | 4,181 | 2026-08-29 19:40:49 | 50 | 38 | 30 | 归档区（〔归档区〕） | 活引用（路径式）24 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t1d_pagerank.csv | 8b1a9e5113bb | 4,167 | 2026-08-28 21:36:57 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S2_n60.json | 01c492a97b98 | 4,123 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S1_n60.json | 584de37ebec1 | 4,122 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_risk2_canonical5_decision_2026_09_11.json | cf4a882160e1 | 4,066 | 2026-09-15 10:22:26 | 35 | 20 | 27 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 15 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/variant_params_table.md | 25f90f106451 | 4,035 | 2026-08-23 00:01:28 | 25 | 15 | 20 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 10 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/L_algorithm_process.json | ff0ef9131fdd | 3,920 | 2026-08-28 17:38:45 | 30 | 19 | 24 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/L_project_management.json | 32ca32c00da4 | 3,898 | 2026-08-28 23:12:37 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_GT8.md | 869c0071fbc2 | 3,890 | 2026-08-29 19:36:27 | 33 | 20 | 22 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| RELEASE_v1.4.0.md | ff9ff3177c06 | 3,847 | 2026-08-23 16:38:29 | 39 | 27 | 31 | 归档区（〔归档区〕） | 活引用（路径式）2 处（.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_gpt6_teamorouter_2026_09_10.json | f44636f5f72f | 3,827 | 2026-09-10 16:49:38 | 25 | 17 | 22 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt.json | 497b9c2d6746 | 3,803 | 2026-08-28 17:43:00 | 115 | 96 | 70 | 归档区（〔归档区〕） | 活引用（路径式）73 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_dw_ents9_2026_10_21.py、.tmp/_dw_final_verify_2026_10_21.py …（余 49 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 19 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json | afe975606d40 | 3,761 | 2026-09-16 22:40:54 | 47 | 26 | 31 | 归档区（〔归档区〕） | 活引用（路径式）24 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 21 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/L_geography_world.json | 77b0c1466dc0 | 3,699 | 2026-08-28 23:11:44 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t3e_commit.csv | bf0a2b544a74 | 3,691 | 2026-08-28 21:36:14 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0_boss.md | 36c714eabe3b | 3,642 | 2026-08-28 21:16:05 | 36 | 23 | 24 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0_hardening.md | a7f479793f01 | 3,563 | 2026-08-28 22:49:38 | 32 | 20 | 22 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm16_v2_scan_2026_10_21.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/L_biological_taxonomy.json | 0c7ad5235ae9 | 3,562 | 2026-08-28 17:38:45 | 33 | 16 | 20 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 17 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pc_2_real_transverse_ising_2026_09_15.json | 8933d61b180a | 3,553 | 2026-09-15 15:27:35 | 53 | 30 | 32 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 23 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pe_2_real_transverse_ising_2026_09_15.json | 8933d61b180a | 3,553 | 2026-09-15 13:34:49 | 64 | 37 | 38 | 归档区（〔归档区〕） | 活引用（路径式）29 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 19 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 27 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0_skills.md | 43731392b581 | 3,456 | 2026-08-28 20:47:31 | 32 | 20 | 22 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、docs/SPEC_GT2B.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_gsm8k_stratified.json | 8b7574b25336 | 3,411 | 2026-08-23 09:40:34 | 38 | 21 | 27 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 17 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t3d_llmmd.csv | 49028967ad57 | 3,405 | 2026-08-28 21:35:31 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/L_physics_concepts.json | d8780859d310 | 3,397 | 2026-08-28 17:38:45 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/BASELINE_REGISTRY.md | 51b271548835 | 3,356 | 2026-08-28 20:59:38 | 37 | 25 | 26 | 归档区（〔归档区〕） | 活引用（路径式）24 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/scan_supplement_five_terminal_2026_10_10.py …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_GT2B.md | e6cc74f9917d | 3,322 | 2026-08-29 20:00:21 | 34 | 20 | 23 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S6.json | 01d9c95ea690 | 3,320 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S5.json | 4b10f9cae09f | 3,319 | 2026-08-28 17:07:52 | 24 | 15 | 20 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 9 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/SPEC_GT2B.md | 68a5b08ef007 | 3,318 | 2026-08-29 19:56:29 | 61 | 40 | 45 | 归档区（〔归档区〕） | 活引用（路径式）31 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py …（余 20 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 21 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_v2.0_bigquiz.md | d4ed18152dc0 | 3,291 | 2026-08-28 23:55:23 | 42 | 30 | 25 | 归档区（〔归档区〕） | 活引用（路径式）30 处（.tmp/_659_compact.txt、.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 12 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S2_n45.json | 58bb0a7d2e46 | 3,175 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S1_n45.json | 52b4d6e52ae9 | 3,171 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_benchmark_v1_3_traps.json | 82eb64151f2b | 3,112 | 2026-08-23 00:01:28 | 42 | 28 | 27 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_g1_mindmap_demo.json | 55428f6bd848 | 3,041 | 2026-08-23 05:00:55 | 81 | 64 | 40 | 归档区（〔归档区〕） | 活引用（路径式）50 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 22 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 17 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt8c.json | 9b16fa802ef8 | 2,864 | 2026-08-30 16:17:46 | 39 | 25 | 31 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_g2_boltzmann_pathintegral_rewrite.json | f36667e5b5b8 | 2,782 | 2026-08-23 09:40:33 | 33 | 19 | 24 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_benchmark_v1_4_gsm8k.json | 5cd6269d7baf | 2,741 | 2026-08-23 05:00:55 | 42 | 28 | 29 | 归档区（〔归档区〕） | 活引用（路径式）18 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt8b.json | 6339ea4e500c | 2,706 | 2026-08-30 10:28:49 | 45 | 31 | 33 | 归档区（〔归档区〕） | 活引用（路径式）23 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S6_n35.json | 8d02fbadd277 | 2,676 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| docs/Findings_GT3.md | 4f3242b2a661 | 2,632 | 2026-08-29 15:06:30 | 39 | 25 | 25 | 归档区（〔归档区〕） | 活引用（路径式）24 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/all.json | 8df31c95b1fc | 2,557 | 2026-09-17 10:24:31 | 34 | 21 | 27 | 归档区（〔归档区〕） | 活引用（路径式）11 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 13 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S1_n35.json | f035043bfddd | 2,521 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| paper/FIGURE_LANGUAGE_POLICY.md | a18b5d0d4485 | 2,495 | 2026-08-30 11:16:21 | 40 | 23 | 28 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 17 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S2_n35.json | e20a1bbeaee7 | 2,480 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pc_1_real_2d_ising_2026_09_15.json | 43d9ce160fc8 | 2,460 | 2026-09-15 15:28:00 | 54 | 30 | 34 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 24 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pe_1_real_2d_ising_2026_09_15.json | 43d9ce160fc8 | 2,460 | 2026-09-15 13:34:49 | 60 | 30 | 34 | 归档区（〔归档区〕） | 活引用（路径式）25 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 30 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pc_3_real_reservoir_2026_09_15.json | 94b5398be76c | 2,364 | 2026-09-15 15:28:00 | 56 | 33 | 31 | 归档区（〔归档区〕） | 活引用（路径式）27 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 23 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pe_3_real_reservoir_2026_09_15.json | 94b5398be76c | 2,364 | 2026-09-15 13:34:49 | 53 | 26 | 29 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 27 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S3.json | 3b6879ab2440 | 2,297 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_benchmark_v1_3_simple.json | 9347add72401 | 2,245 | 2026-08-23 00:01:28 | 41 | 25 | 28 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm_supplement_out_2026_10_21.txt …（余 11 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 16 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S2.json | b1f6c5aa4de6 | 2,234 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_g2_boltzmann_pathintegral.json | 9fd0f3399ab3 | 2,204 | 2026-08-23 05:00:55 | 34 | 20 | 24 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json | 59c2113b7c71 | 2,059 | 2026-09-16 23:33:03 | 39 | 21 | 24 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json | a4b12d1cfedc | 2,042 | 2026-09-16 22:12:02 | 41 | 23 | 26 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t2e_nettack.csv | 2628f74421f2 | 1,875 | 2026-08-28 21:35:25 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_fastcheck.json | a1ef105b0269 | 1,768 | 2026-08-28 22:08:40 | 38 | 20 | 27 | 归档区（〔归档区〕） | 活引用（路径式）17 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S6_n20.json | 4a0689892c1b | 1,724 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/independent_review_20260823.md | 7474fc258375 | 1,724 | 2026-08-23 21:40:22 | 24 | 16 | 20 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_pk_dnm16_v2_scan_2026_10_21.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_benchmark_v1_4_strategyqa.json | b51fd24586b3 | 1,691 | 2026-08-23 13:04:23 | 37 | 23 | 26 | 归档区（〔归档区〕） | 活引用（路径式）15 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 10 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json | a9ad1de618f5 | 1,669 | 2026-09-16 17:39:59 | 75 | 57 | 49 | 归档区（〔归档区〕） | 活引用（路径式）54 处（.tmp/_26b_verdict_prep_hashcheck_2026_10_01.py、.tmp/_26b_verdict_prep_validate_2026_10_01.py、.tmp/_docwriter_pre_inventory.txt …（余 35 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| audits_security.json | 553c90aa3ba6 | 1,610 | 2026-08-28 15:52:30 | 35 | 24 | 28 | 归档区（〔归档区〕） | 活引用（路径式）2 处（.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S2_n20.json | bfc9d38c8c0f | 1,537 | 2026-08-28 17:07:52 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| corpus/v20/S1.json | a890c56f7705 | 1,512 | 2026-08-28 17:07:51 | 23 | 15 | 19 | 归档区（〔归档区〕） | 活引用（路径式）13 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md …（余 7 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v22_e95ci.json | 928bcfbdb7c3 | 1,496 | 2026-08-30 21:45:29 | 48 | 37 | 32 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_familyl_ingest.json | 676eb83edc27 | 1,303 | 2026-08-28 17:38:45 | 44 | 29 | 31 | 归档区（〔归档区〕） | 活引用（路径式）26 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 18 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 15 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| reviews/data/t2f_waniek.csv | f0d2c9d2a39b | 1,271 | 2026-08-28 21:35:28 | 22 | 14 | 18 | 归档区（〔归档区〕） | 活引用（路径式）14 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 8 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 8 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pc_3_a3_clipping_2026_09_15.json | d74d6b39d1b0 | 1,265 | 2026-09-15 13:34:48 | 82 | 55 | 41 | 归档区（〔归档区〕） | 活引用（路径式）48 处（.tmp/_659_compact.txt、.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt …（余 24 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 27 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| LICENSE | 6a703b06f0fe | 1,085 | 2026-08-22 21:07:57 | 0 | 0 | 0 | 归档区（〔归档区〕） | 无须（0 路径式引用） |
| results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json | e934819ee9ed | 1,043 | 2026-09-16 22:11:35 | 41 | 23 | 26 | 归档区（〔归档区〕） | 活引用（路径式）22 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 18 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pc_2_a2_fitting_2026_09_15.json | 5a880678c386 | 1,024 | 2026-09-15 13:34:48 | 51 | 24 | 29 | 归档区（〔归档区〕） | 活引用（路径式）21 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 27 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt8c_ingest.json | 4b11b1bd8ada | 1,018 | 2026-08-30 16:17:42 | 33 | 19 | 26 | 归档区（〔归档区〕） | 活引用（路径式）16 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 13 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 14 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/boss_pc_1_a1_resampling_2026_09_15.json | d21912a05d79 | 1,017 | 2026-09-15 13:34:48 | 60 | 33 | 32 | 归档区（〔归档区〕） | 活引用（路径式）26 处（.tmp/_659_overlap_digest.txt、.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt …（余 12 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 27 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_gt8b_ingest.json | aa077cc1725e | 986 | 2026-08-30 10:28:44 | 39 | 23 | 32 | 归档区（〔归档区〕） | 活引用（路径式）19 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 16 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 16 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v20_vector_audit.json | b9b65c568842 | 915 | 2026-08-28 21:15:08 | 64 | 36 | 29 | 归档区（〔归档区〕） | 活引用（路径式）32 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 28 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/deposon_v22_p1c.json | 2bed4de3a57c | 763 | 2026-08-30 21:59:28 | 40 | 31 | 31 | 归档区（〔归档区〕） | 活引用（路径式）20 处（.tmp/_docwriter_pre_inventory.txt、.tmp/_gh_tree.txt、.tmp/_verifier_gd03v2_baseline_20261021.txt …（余 14 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 9 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| requirements.txt | ab3045b2c6d9 | 27 | 2026-08-22 21:07:57 | 34 | 23 | 27 | 归档区（〔归档区〕） | 活引用（路径式）2 处（.tmp/_gh_tree.txt、letters/_internal_true_clue_book_2026_10_12.md、results/_root_session_history_memo_main_2026_10_14.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 11 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |

### §2-C3 C3 · 审计探针族（`results\.tmp\` 工作面） — 78 件／113,954,283 B

| 现路径 | SHA-12 | bytes | mtime | 被引用次数 | 活引用次数 | 引者件数 | 拟归何处 | 移动后须补之幽灵登记 |
|---|---|---|---|---|---|---|---|---|
| results/.tmp/_s18_ghost_audit_stage3_out_2026_10_22.json | 61acc3660f52 | 36,934,926 | 2026-10-22 01:07:26 | 5 | 5 | 5 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s18_ghost_audit_instrument_out_2026_10_22.json | a683cdd1d838 | 36,506,432 | 2026-10-22 00:51:56 | 4 | 4 | 3 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s18_ghost_audit_instrument_v2_out_2026_10_22.json | 5a7608124376 | 34,037,604 | 2026-10-22 01:04:11 | 9 | 9 | 9 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s18_ghost_audit_stage5_out_2026_10_22.json | bf269de48023 | 2,489,344 | 2026-10-22 01:10:19 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s14_session_scan_out_2026_10_21.md | 5741ac6af12a | 1,137,664 | 2026-10-21 01:00:01 | 159 | 158 | 21 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）134 处（.tmp/_pk_den16_readings_2026_10_21.md、.tmp/_pk_den16_scan_v2_2026_10_21.txt、.tmp/_v169_probe3.out.txt …（余 15 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_stage4_out_2026_10_22.json | 408b9f30f175 | 654,070 | 2026-10-22 01:08:54 | 3 | 3 | 2 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s14_anchorchain_2026_10_21.md | dd49e6612dbe | 480,977 | 2026-10-21 01:03:38 | 9 | 8 | 7 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）5 处（.tmp/_pk_f1f7_scan_out.txt、results/.tmp/_s14_anchorchain_2026_10_21.py、results/_results_index_2026_10_21.md …（余 1 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s13_conv_out_2026_10_20.txt | 2e523f11e8c2 | 419,151 | 2026-10-20 15:29:08 | 30 | 29 | 8 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）28 处（results/.tmp/_audit_s13_anchors_out_2026_10_20.txt、results/.tmp/_audit_s13_scan_2026_10_20.py、results/.tmp/_s13_body_2026_10_20.md …（余 4 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_main_events2_2026_10_21.md | 2faed7996933 | 177,579 | 2026-10-21 01:07:24 | 77 | 76 | 31 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）69 处（.tmp/_pk_den16_scan_v2_2026_10_21.txt、.tmp/_v172_append.py、.tmp/_v172_body_p1.md …（余 24 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_cards_full_2026_10_21.md | 71e52e6aa470 | 153,751 | 2026-10-21 01:00:36 | 16 | 15 | 8 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）12 处（.tmp/_pk_den16_scan_v2_2026_10_21.txt、.tmp/_v174_panel2_out.txt、results/.tmp/_s14_cards_full_2026_10_21.py …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_main_session_slice_2026_10_21.md | 4b10cb45fd44 | 96,411 | 2026-10-21 00:58:23 | 53 | 52 | 29 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）45 处（.tmp/_pk_den16_readings_2026_10_21.md、.tmp/_pk_den16_scan_v2_2026_10_21.txt、.tmp/_v169_body_p4.md …（余 21 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_heads_out_2026_10_19.txt | c285e696fce1 | 83,701 | 2026-10-19 23:46:52 | 14 | 13 | 9 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）11 处（results/.tmp/_s12_body_2026_10_19.md、results/.tmp/_s14_anchorchain_2026_10_21.md、results/.tmp/_s14_session_scan_out_2026_10_21.md …（余 4 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s16_body_2026_10_21.md | 11af4e96c034 | 77,994 | 2026-10-21 23:43:46 | 13 | 13 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）7 处（results/.tmp/_s16_append_2026_10_21.md、results/.tmp/_s16_body_2026_10_21.md、results/_four_face_deliberation_2026_10_22.md …（余 2 件））→ 须补「旧路径→新路径」登记 |
| results/.tmp/_s15_body_2026_10_21.md | 258115c22f32 | 55,575 | 2026-10-21 17:51:16 | 9 | 8 | 4 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_s15_append_2026_10_21.md、results/.tmp/_s15_body_2026_10_21.md、results/_root_session_history_memo_2026_10_14.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s13_body_2026_10_20.md | 758ad1bac2e6 | 51,542 | 2026-10-20 15:37:49 | 12 | 11 | 9 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）8 处（.tmp/_v174_panel2_out.txt、_kdflipc_tokens_report.txt、results/.tmp/_audit_s13_append_2026_10_20.py …（余 3 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s17_body_2026_10_22.md | d1883cdef084 | 42,171 | 2026-10-22 00:17:31 | 6 | 6 | 3 | 不移动（在途·今日生成） | 活引用（路径式）4 处（results/.tmp/_s17_append_2026_10_22.md、results/.tmp/_s17_body_2026_10_22.md、results/_root_session_history_memo_2026_10_14.md）→ 须补「旧路径→新路径」登记 |
| results/.tmp/_s14_disk_scan_out_t2.md | 8f184f097720 | 42,088 | 2026-10-21 01:00:00 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（.tmp/_v169_probe5.out.txt、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_instrument_out_2026_10_21.md | 53fadc8fc515 | 40,930 | 2026-10-21 01:02:17 | 21 | 20 | 7 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）17 处（_kdflipc_tokens_report.txt、results/.tmp/_s14_instrument_2026_10_21.py、results/_results_index_2026_10_21.md …（余 1 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s12_body_2026_10_19.md | ebea307102a1 | 40,199 | 2026-10-19 23:52:34 | 16 | 15 | 10 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）11 处（_kdflipc_tokens_report.txt、results/.tmp/_audit_s12_append_2026_10_19.py、results/.tmp/_audit_s12_refined_out_2026_10_19.txt …（余 3 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_body_2026_10_21.md | 4893e543556f | 38,541 | 2026-10-21 01:20:23 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_emit_2026_10_22.py | c5ad4885a9d9 | 34,758 | 2026-10-22 01:27:40 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s14_anchorchain2_2026_10_21.md | cd3435aecb60 | 26,640 | 2026-10-21 01:05:10 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_s14_anchor2_2026_10_21.py、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_final_measure_2026_10_21.md | 5c4f0d43ada4 | 25,045 | 2026-10-21 01:10:55 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_s14_final_measure_2026_10_21.py、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s13_final_out_2026_10_20.txt | f3b199fa0deb | 19,178 | 2026-10-20 15:34:21 | 9 | 8 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）7 处（results/.tmp/_s13_body_2026_10_20.md、results/.tmp/_s14_session_scan_out_2026_10_21.md、results/_results_index_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_stage6_out_2026_10_22.json | 791968f0a7db | 17,045 | 2026-10-22 01:12:18 | 2 | 2 | 2 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s60_28_body_2026_10_22.md | 078ced01d6d7 | 15,559 | 2026-10-22 02:05:44 | 0 | 0 | 0 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_audit_s13_anchors_out_2026_10_20.txt | 9063b4326cec | 13,754 | 2026-10-20 15:30:45 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）6 处（results/.tmp/_audit_s13_anchors_2026_10_20.py、results/.tmp/_s13_body_2026_10_20.md、results/_results_index_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_refined_2026_10_19.py | c53201f4bae4 | 12,829 | 2026-10-19 23:55:15 | 13 | 12 | 8 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）8 处（results/.tmp/_audit_s12_refined_out_2026_10_19.txt、results/.tmp/_s14_anchorchain_2026_10_21.md、results/_results_index_2026_10_21.md …（余 1 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s13_anchors_2026_10_20.py | eeb9f79522b0 | 12,723 | 2026-10-20 15:30:26 | 10 | 9 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）6 处（results/.tmp/_audit_s13_anchors_out_2026_10_20.txt、results/.tmp/_s13_body_2026_10_20.md、results/_results_index_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_stage2_2026_10_22.py | 6d05e415e43e | 11,510 | 2026-10-22 00:48:41 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s18_ghost_audit_instrument_v2_2026_10_22.py | 3343b9939f33 | 9,941 | 2026-10-22 00:55:08 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s18_ghost_audit_stage3_2026_10_22.py | 4f4b3346c10d | 9,656 | 2026-10-22 01:07:08 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s16_append_2026_10_21.md | b925b0c48d58 | 9,441 | 2026-10-21 23:47:13 | 12 | 12 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_s16_append_2026_10_21.md、results/.tmp/_s16_body_2026_10_21.md、results/_root_session_history_memo_2026_10_14.md）→ 须补「旧路径→新路径」登记 |
| results/.tmp/_s18_ghost_audit_instrument_2026_10_22.py | 0b7ee9c9e6a2 | 9,011 | 2026-10-22 00:42:38 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_audit_s13_final_2026_10_20.py | 036b4a749f95 | 8,898 | 2026-10-20 15:34:08 | 9 | 8 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）7 处（results/.tmp/_s13_body_2026_10_20.md、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md …（余 1 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_refined_out_2026_10_19.txt | 16ee96876c4a | 8,779 | 2026-10-19 23:55:26 | 10 | 9 | 8 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_s14_anchorchain_2026_10_21.md、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_append_2026_10_21.py | 4402eb22f4ad | 8,769 | 2026-10-21 01:21:04 | 6 | 5 | 4 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_keyscan_2026_10_19.py | 6a2dc54827b7 | 8,367 | 2026-10-19 23:48:02 | 11 | 10 | 7 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）9 处（results/.tmp/_audit_s12_keyscan_out_2026_10_19.txt、results/.tmp/_audit_s12_refined_out_2026_10_19.txt、results/.tmp/_s12_body_2026_10_19.md …（余 3 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_stage2v2_2026_10_22.py | 85e59ee41018 | 8,218 | 2026-10-22 00:54:50 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s14_anchor2_2026_10_21.py | 6c9463882c9f | 7,115 | 2026-10-21 01:04:52 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_keyscan_out_2026_10_19.txt | aa7fa6ff4255 | 6,950 | 2026-10-19 23:48:10 | 22 | 21 | 8 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）19 处（results/.tmp/_audit_s12_refined_out_2026_10_19.txt、results/.tmp/_s12_body_2026_10_19.md、results/.tmp/_s14_anchorchain_2026_10_21.md …（余 3 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_final_measure_2026_10_21.py | e0dc2e74ff62 | 5,872 | 2026-10-21 01:10:37 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s17_append_2026_10_22.md | d013bcb05153 | 5,449 | 2026-10-22 00:19:28 | 8 | 8 | 3 | 不移动（在途·今日生成） | 活引用（路径式）6 处（results/.tmp/_s17_append_2026_10_22.md、results/.tmp/_s17_body_2026_10_22.md、results/_root_session_history_memo_2026_10_14.md）→ 须补「旧路径→新路径」登记 |
| results/.tmp/_s18_ghost_audit_stage4_2026_10_22.py | 68e539d48eb8 | 5,343 | 2026-10-22 01:08:21 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s13_7_body_2026_10_20.md | 5a74e4bdea89 | 4,975 | 2026-10-20 15:40:06 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_audit_s13_7_append_2026_10_20.py、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s13_scan_2026_10_20.py | 8c8b9d995f05 | 4,924 | 2026-10-20 15:29:01 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）6 处（results/.tmp/_audit_s13_anchors_out_2026_10_20.txt、results/.tmp/_s13_body_2026_10_20.md、results/_results_index_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s12_7_body_2026_10_19.md | e80e4fe4aa0f | 4,754 | 2026-10-19 23:56:39 | 13 | 12 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）5 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md、results/_results_split_proposal_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_instrument_2026_10_21.py | 6eb1a23daf22 | 4,550 | 2026-10-21 01:02:07 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_disk_scan_out_t1.md | de8d0b8a76b0 | 4,313 | 2026-10-21 00:55:51 | 13 | 12 | 11 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）9 处（.tmp/_v169_probe.out.txt、.tmp/_v169_probe3.out.txt、.tmp/_v169_probe4.out.txt …（余 5 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_anchorchain_2026_10_21.py | d80719c6d092 | 4,247 | 2026-10-21 01:03:18 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_stage5_2026_10_22.py | 00475bda68c7 | 4,136 | 2026-10-22 01:09:21 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s14_session_scan2_2026_10_21.py | e93a45e23469 | 4,080 | 2026-10-21 00:59:52 | 13 | 12 | 10 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）9 处（.tmp/_v169_probe3.out.txt、.tmp/_v169_probe4.out.txt、.tmp/_v169_probe5.out.txt …（余 4 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_stage6_2026_10_22.py | e360ac76a79a | 4,069 | 2026-10-22 01:12:01 | 1 | 1 | 1 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s14_session_scan_2026_10_21.py | a4cc5099940c | 3,618 | 2026-10-21 00:56:26 | 12 | 11 | 10 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）8 处（.tmp/_v169_probe3.out.txt、.tmp/_v169_probe4.out.txt、.tmp/_v169_probe5.out.txt …（余 4 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s13_append_2026_10_20.py | b4a1c8d6a3d9 | 3,520 | 2026-10-20 15:38:14 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_append_2026_10_19.py | e3aca88d382f | 3,116 | 2026-10-19 23:53:03 | 9 | 8 | 7 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_s14_anchorchain_2026_10_21.md、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_keyclass_2026_10_19.py | b4f7569705a8 | 3,057 | 2026-10-19 23:48:37 | 9 | 8 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）7 处（results/.tmp/_audit_s12_refined_out_2026_10_19.txt、results/.tmp/_s12_body_2026_10_19.md、results/_results_index_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_disk_scan_2026_10_21.py | 854019e4b7d3 | 2,982 | 2026-10-21 00:59:47 | 15 | 14 | 12 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）11 处（.tmp/_v169_probe.out.txt、.tmp/_v169_probe3.out.txt、.tmp/_v169_probe4.out.txt …（余 6 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_msgdist_2026_10_21.py | 31bcc0f213c0 | 2,958 | 2026-10-21 00:58:58 | 10 | 9 | 8 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）6 处（.tmp/_v169_probe5.out.txt、results/.tmp/_s14_disk_scan_out_t2.md、results/.tmp/_s14_session_scan_out_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_heads_2026_10_19.py | faa86d3f25bc | 2,814 | 2026-10-19 23:46:45 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）5 处（results/.tmp/_s12_body_2026_10_19.md、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md …（余 1 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_scan_2026_10_19.py | e19a994d3f9b | 2,767 | 2026-10-19 23:45:24 | 10 | 9 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）8 处（results/.tmp/_s12_body_2026_10_19.md、results/.tmp/_s14_anchorchain_2026_10_21.md、results/_results_index_2026_10_21.md …（余 2 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_final_2026_10_19.py | ffc34fee17b2 | 2,739 | 2026-10-19 19:36:32 | 12 | 11 | 8 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）8 处（results/.tmp/_audit_s12_heads_2026_10_19.py、results/.tmp/_audit_s12_heads_out_2026_10_19.txt、results/.tmp/_s12_body_2026_10_19.md …（余 4 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_selfcheck_2026_10_22.py | f5a269c94305 | 2,728 | 2026-10-22 00:52:38 | 0 | 0 | 0 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s18_ghost_audit_selfcheck2_2026_10_22.py | d55005d1bc3a | 2,673 | 2026-10-22 01:04:58 | 0 | 0 | 0 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_s14_events2_2026_10_21.py | 0c75fb83c89d | 2,668 | 2026-10-21 01:07:17 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s15_append_2026_10_21.md | 8161b1da2340 | 2,459 | 2026-10-21 17:52:02 | 1 | 0 | 1 | deposon-sub（探针执行器·保可复算性） | 无须（**活面 0 路径式引用**；仅有快照面之文本提及）；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s13_7_append_2026_10_20.py | 953abd8121f7 | 2,395 | 2026-10-20 15:39:40 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_caliber_2026_10_22.py | 94005bfb9e30 | 1,926 | 2026-10-22 01:05:56 | 0 | 0 | 0 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_audit_s13_main_heads_2026_10_20.txt | dc3a10abbc2b | 1,792 | 2026-10-20 15:34:32 | 6 | 5 | 4 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_cards_full_2026_10_21.py | 0f95bd681cf6 | 1,587 | 2026-10-21 01:00:31 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（.tmp/_v169_probe5.out.txt、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_append_report_2026_10_21.md | 67d8df4dcc34 | 1,505 | 2026-10-21 01:21:18 | 6 | 5 | 4 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s12_keyclass_2026_10_19.txt | 21d7e6e9fdbc | 1,385 | 2026-10-19 23:48:44 | 6 | 5 | 4 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）3 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s18_ghost_audit_postfreeze_scan_2026_10_22.json | cc627c5365ef | 887 | 2026-10-22 01:16:18 | 0 | 0 | 0 | 不移动（在途·今日生成） | 无须（0 路径式引用） |
| results/.tmp/_audit_bom_cr_2026_10_19.py | 107a9ed5090a | 880 | 2026-10-19 19:32:03 | 9 | 8 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）5 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md、results/_root_session_history_memo_2026_10_14.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_tail_2026_10_19.py | 893914b4ef10 | 704 | 2026-10-19 19:35:00 | 9 | 8 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）5 处（results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md、results/_root_session_history_memo_2026_10_14.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_msgdist_2026_10_21.md | 6b0da8b7ce9b | 675 | 2026-10-21 00:59:03 | 11 | 10 | 9 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）7 处（.tmp/_v169_probe5.out.txt、results/.tmp/_s14_disk_scan_out_t2.md、results/.tmp/_s14_msgdist_2026_10_21.py …（余 3 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_audit_s13_main_heads_2026_10_20.py | 67bcc0955f22 | 611 | 2026-10-20 15:34:32 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）5 处（results/.tmp/_s13_body_2026_10_20.md、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md …（余 1 件））→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |
| results/.tmp/_s14_main_events_2026_10_21.md | 1e5b4e17e616 | 289 | 2026-10-21 01:05:10 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） | 活引用（路径式）4 处（results/.tmp/_s14_anchor2_2026_10_21.py、results/_results_index_2026_10_21.md、results/_results_path_mapping_2026_10_21.md）→ 须补「旧路径→新路径」登记；另有**快照面提及 1 处**（`_c514_remote_blobs` 镜像／SHA 索引·随快照件存亡·⛔ 0 计为断链） |

## §3 汇总（件数／总字节／按类别小计·加总自证）

| 类别 | 件数 | 字节 | 占 C 类 |
|---|---|---|---|
| C1 · 同族旧版（被同族新版取代者） | 28 | 1,111,399 | 0.9% |
| C2 · 早期纪元（mtime < 2026-09-20·v1.x 实验期·已剔 D 类禁动面） | 209 | 9,130,187 | 7.4% |
| C3 · 审计探针族（`results\.tmp\` 工作面） | 78 | 113,954,283 | 91.8% |
| **合计** | **315** | **124,195,869** | **100.0%** |

**加总自证**：类别小计之和 ＝ 件数 315 ／ 字节 124,195,869；与逐件索引直取之和 ＝ 件数 **315** ／ 字节 **124,195,869** ⇒ **相符**。

**参量**：全仓 802,875,238 B（802.9 MB／765.7 MiB）；`.tmp` 539,646,644 B（539.6 MB）＝ 全仓之 67.2%。

## §4 移动序（被引用次数升序·每批 ≤12 件·本件只出序·⛔ 0 移动）

可移者 **283 件**（拟归 `deposon-sub` 或 `归档区`）；不可移者 **32 件**单列于 §4-2。共 **24 批**（每批 ≤ 12 件）。

### §4-1 可移者之排定

| 批 | 现路径 | bytes | 被引用次数 | **活引用次数** | 活路径式引用处 | 拟归何处 |
|---|---|---:|---:|---:|---:|---|
| 1 | LICENSE | 1,085 | 0 | 0 | 0 | 归档区（〔归档区〕） |
| 1 | results/.tmp/_s15_append_2026_10_21.md | 2,459 | 1 | 0 | 0 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_audit_s12_keyclass_2026_10_19.txt | 1,385 | 6 | 5 | 3 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_s14_append_report_2026_10_21.md | 1,505 | 6 | 5 | 3 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_audit_s13_main_heads_2026_10_20.txt | 1,792 | 6 | 5 | 3 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_s14_append_2026_10_21.py | 8,769 | 6 | 5 | 3 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_audit_s13_main_heads_2026_10_20.py | 611 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_audit_s13_7_append_2026_10_20.py | 2,395 | 7 | 6 | 3 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_s14_events2_2026_10_21.py | 2,668 | 7 | 6 | 3 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_audit_s12_heads_2026_10_19.py | 2,814 | 7 | 6 | 5 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_audit_s13_append_2026_10_20.py | 3,520 | 7 | 6 | 3 | deposon-sub（探针执行器·保可复算性） |
| 1 | results/.tmp/_s14_anchorchain_2026_10_21.py | 4,247 | 7 | 6 | 3 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_instrument_2026_10_21.py | 4,550 | 7 | 6 | 3 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_final_measure_2026_10_21.py | 5,872 | 7 | 6 | 3 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_anchor2_2026_10_21.py | 7,115 | 7 | 6 | 3 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_main_events_2026_10_21.md | 289 | 8 | 7 | 4 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_cards_full_2026_10_21.py | 1,587 | 8 | 7 | 4 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_audit_s13_scan_2026_10_20.py | 4,924 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s13_7_body_2026_10_20.md | 4,975 | 8 | 7 | 4 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_audit_s13_anchors_out_2026_10_20.txt | 13,754 | 8 | 7 | 6 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_final_measure_2026_10_21.md | 25,045 | 8 | 7 | 4 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_anchorchain2_2026_10_21.md | 26,640 | 8 | 7 | 4 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_body_2026_10_21.md | 38,541 | 8 | 7 | 3 | deposon-sub（探针执行器·保可复算性） |
| 2 | results/.tmp/_s14_disk_scan_out_t2.md | 42,088 | 8 | 7 | 4 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_tail_2026_10_19.py | 704 | 9 | 8 | 5 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_bom_cr_2026_10_19.py | 880 | 9 | 8 | 5 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_s12_keyclass_2026_10_19.py | 3,057 | 9 | 8 | 7 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_s12_append_2026_10_19.py | 3,116 | 9 | 8 | 4 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_s13_final_2026_10_20.py | 8,898 | 9 | 8 | 7 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_s13_final_out_2026_10_20.txt | 19,178 | 9 | 8 | 7 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_s15_body_2026_10_21.md | 55,575 | 9 | 8 | 4 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_s14_anchorchain_2026_10_21.md | 480,977 | 9 | 8 | 5 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_s12_scan_2026_10_19.py | 2,767 | 10 | 9 | 8 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_s14_msgdist_2026_10_21.py | 2,958 | 10 | 9 | 6 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_s12_refined_out_2026_10_19.txt | 8,779 | 10 | 9 | 4 | deposon-sub（探针执行器·保可复算性） |
| 3 | results/.tmp/_audit_s13_anchors_2026_10_20.py | 12,723 | 10 | 9 | 6 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s14_msgdist_2026_10_21.md | 675 | 11 | 10 | 7 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_audit_s12_keyscan_2026_10_19.py | 8,367 | 11 | 10 | 9 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_audit_final_2026_10_19.py | 2,739 | 12 | 11 | 8 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s14_session_scan_2026_10_21.py | 3,618 | 12 | 11 | 8 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s16_append_2026_10_21.md | 9,441 | 12 | 12 | 4 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s13_body_2026_10_20.md | 51,542 | 12 | 11 | 8 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s14_session_scan2_2026_10_21.py | 4,080 | 13 | 12 | 9 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s14_disk_scan_out_t1.md | 4,313 | 13 | 12 | 9 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s12_7_body_2026_10_19.md | 4,754 | 13 | 12 | 5 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_audit_s12_refined_2026_10_19.py | 12,829 | 13 | 12 | 8 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_s16_body_2026_10_21.md | 77,994 | 13 | 13 | 7 | deposon-sub（探针执行器·保可复算性） |
| 4 | results/.tmp/_audit_s12_heads_out_2026_10_19.txt | 83,701 | 14 | 13 | 11 | deposon-sub（探针执行器·保可复算性） |
| 5 | results/.tmp/_s14_disk_scan_2026_10_21.py | 2,982 | 15 | 14 | 11 | deposon-sub（探针执行器·保可复算性） |
| 5 | results/.tmp/_s12_body_2026_10_19.md | 40,199 | 16 | 15 | 11 | deposon-sub（探针执行器·保可复算性） |
| 5 | results/.tmp/_s14_cards_full_2026_10_21.md | 153,751 | 16 | 15 | 12 | deposon-sub（探针执行器·保可复算性） |
| 5 | results/.tmp/_s14_instrument_out_2026_10_21.md | 40,930 | 21 | 20 | 17 | deposon-sub（探针执行器·保可复算性） |
| 5 | reviews/data/t2f_waniek.csv | 1,271 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 5 | corpus/v20/S2_n20.json | 1,537 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 5 | corpus/v20/S6_n20.json | 1,724 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 5 | reviews/data/t2e_nettack.csv | 1,875 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 5 | corpus/v20/S2.json | 2,234 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 5 | corpus/v20/S3.json | 2,297 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 5 | corpus/v20/S2_n35.json | 2,480 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 5 | corpus/v20/S1_n35.json | 2,521 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/S6_n35.json | 2,676 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/S1_n45.json | 3,171 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/S2_n45.json | 3,175 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/S6.json | 3,320 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/L_physics_concepts.json | 3,397 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | reviews/data/t3d_llmmd.csv | 3,405 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 6 | reviews/data/t3e_commit.csv | 3,691 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 6 | corpus/v20/L_geography_world.json | 3,699 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/L_project_management.json | 3,898 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/S1_n60.json | 4,122 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | corpus/v20/S2_n60.json | 4,123 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 6 | reviews/data/t1d_pagerank.csv | 4,167 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | corpus/v20/L_historical_causality.json | 4,329 | 22 | 14 | 13 | 归档区（〔归档区〕） |
| 7 | reviews/data/t1_potential.csv | 4,833 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/data/t2d_hiding.csv | 5,377 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/data/t1b_classics.csv | 5,450 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/data/t1c_loglinear.csv | 5,566 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/data/t4_poa.csv | 6,567 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/data/t3b_verifiable.csv | 6,731 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/data/t2_linkpred.csv | 6,750 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/data/t2c_advlink.csv | 6,886 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | results/.tmp/_audit_s12_keyscan_out_2026_10_19.txt | 6,950 | 22 | 21 | 19 | deposon-sub（探针执行器·保可复算性） |
| 7 | reviews/experiment_design_v19.md | 8,840 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 7 | reviews/design_probe_v19.md | 13,967 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 8 | reviews/post_edit_verification_v19.md | 19,327 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 8 | reviews/literature_scan_v19.md | 28,449 | 22 | 14 | 14 | 归档区（〔归档区〕） |
| 8 | corpus/v20/S1.json | 1,512 | 23 | 15 | 13 | 归档区（〔归档区〕） |
| 8 | reviews/data/t2b_linkpred.csv | 5,520 | 23 | 15 | 15 | 归档区（〔归档区〕） |
| 8 | reviews/independent_review_20260823.md | 1,724 | 24 | 16 | 16 | 归档区（〔归档区〕） |
| 8 | corpus/v20/S5.json | 3,319 | 24 | 15 | 13 | 归档区（〔归档区〕） |
| 8 | reviews/data/t3_mechdesign.csv | 6,680 | 24 | 15 | 15 | 归档区（〔归档区〕） |
| 8 | results/deposon_gpt6_teamorouter_2026_09_10.json | 3,827 | 25 | 17 | 14 | 归档区（〔归档区〕） |
| 8 | docs/variant_params_table.md | 4,035 | 25 | 15 | 14 | 归档区（〔归档区〕） |
| 8 | results/_exp04_h_contrast_readings_2026_10_10.json | 72,704 | 25 | 17 | 13 | 归档区（〔归档区〕） |
| 8 | corpus/v20/S6_n60.json | 4,296 | 26 | 16 | 13 | 归档区（〔归档区〕） |
| 8 | docs/simple_baseline_failure_analysis.md | 6,080 | 26 | 14 | 14 | 归档区（〔归档区〕） |
| 9 | results/_s4_substrate_grid_availability_2026_10_08.json | 11,446 | 27 | 21 | 18 | 归档区（〔归档区〕） |
| 9 | docs/Findings_GT_FORMAL.md | 6,345 | 28 | 16 | 15 | 归档区（〔归档区〕） |
| 9 | results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json | 6,466 | 28 | 17 | 15 | 归档区（〔归档区〕） |
| 9 | results/deposon_volcengine_worker_d_2026_09_10.json | 20,280 | 28 | 16 | 14 | 归档区（〔归档区〕） |
| 9 | docs/REFACTOR_v2.md | 23,042 | 28 | 16 | 15 | 归档区（〔归档区〕） |
| 9 | reviews/review_realign_v2X.md | 7,338 | 29 | 19 | 19 | 归档区（〔归档区〕） |
| 9 | results/_v5_item21_anchor_recompute_2026_09_28.json | 9,527 | 29 | 22 | 18 | 归档区（〔归档区〕） |
| 9 | results/deposon_volcengine_worker_b_2026_09_10.json | 49,338 | 29 | 18 | 15 | 归档区（〔归档区〕） |
| 9 | corpus/v20/L_algorithm_process.json | 3,920 | 30 | 19 | 16 | 归档区（〔归档区〕） |
| 9 | results/deposon_risk1_02940_decision_2026_09_11.json | 4,336 | 30 | 19 | 17 | 归档区（〔归档区〕） |
| 9 | docs/space_release_log.json | 5,056 | 30 | 20 | 20 | 归档区（〔归档区〕） |
| 9 | results/deposon_cpath_simulation_2026_09_10.json | 6,351 | 30 | 19 | 15 | 归档区（〔归档区〕） |
| 10 | reviews/post_draft_verification_v2X.md | 9,979 | 30 | 19 | 19 | 归档区（〔归档区〕） |
| 10 | results/deposon_gpt6_teamorouter_30cells_2026_09_10.json | 18,290 | 30 | 19 | 15 | 归档区（〔归档区〕） |
| 10 | results/deposon_openrouter_5model_rag_30cells_2026_09_10.json | 111,710 | 30 | 20 | 18 | 归档区（〔归档区〕） |
| 10 | results/.tmp/_audit_s13_conv_out_2026_10_20.txt | 419,151 | 30 | 29 | 28 | deposon-sub（探针执行器·保可复算性） |
| 10 | results/deposon_volcengine_9model_30cells_2026_09_10.json | 4,894 | 31 | 21 | 19 | 归档区（〔归档区〕） |
| 10 | corpus/v20/S4.json | 4,932 | 31 | 22 | 19 | 归档区（〔归档区〕） |
| 10 | results/deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json | 18,592 | 31 | 20 | 16 | 归档区（〔归档区〕） |
| 10 | results/deposon_volcengine_worker_a_2026_09_10.json | 25,464 | 31 | 19 | 17 | 归档区（〔归档区〕） |
| 10 | docs/Findings_v2.0_skills.md | 3,456 | 32 | 20 | 20 | 归档区（〔归档区〕） |
| 10 | docs/Findings_v2.0_hardening.md | 3,563 | 32 | 20 | 20 | 归档区（〔归档区〕） |
| 10 | docs/PAPER_BRIEF.md | 11,296 | 32 | 19 | 17 | 归档区（〔归档区〕） |
| 10 | results/deposon_v2_phase3_strip_embeddings_2026_09_11.json | 2,398,383 | 32 | 24 | 19 | 归档区（〔归档区〕） |
| 11 | results/deposon_v20_gt8c_ingest.json | 1,018 | 33 | 19 | 16 | 归档区（〔归档区〕） |
| 11 | results/deposon_g2_boltzmann_pathintegral_rewrite.json | 2,782 | 33 | 19 | 16 | 归档区（〔归档区〕） |
| 11 | corpus/v20/L_biological_taxonomy.json | 3,562 | 33 | 16 | 15 | 归档区（〔归档区〕） |
| 11 | docs/Findings_GT8.md | 3,890 | 33 | 20 | 20 | 归档区（〔归档区〕） |
| 11 | docs/Findings_v2.0.md | 4,364 | 33 | 20 | 19 | 归档区（〔归档区〕） |
| 11 | results/deposon_volcengine_glm_latest_5cells_2026_09_10.json | 4,895 | 33 | 20 | 15 | 归档区（〔归档区〕） |
| 11 | results/deposon_v15_diffusion_summary.json | 6,079 | 33 | 19 | 17 | 归档区（〔归档区〕） |
| 11 | docs/SYNTHESIS_mind_game.md | 9,191 | 33 | 18 | 18 | 归档区（〔归档区〕） |
| 11 | reviews/review_coach_v2X_outline.md | 11,295 | 33 | 23 | 23 | 归档区（〔归档区〕） |
| 11 | reviews/review_coach_v2X_draft_r2.md | 15,721 | 33 | 23 | 23 | 归档区（〔归档区〕） |
| 11 | results/deposon_v42_v2_miss_rate_curve_2026_09_16.json | 24,435 | 33 | 21 | 18 | 归档区（〔归档区〕） |
| 11 | requirements.txt | 27 | 34 | 23 | 2 | 归档区（〔归档区〕） |
| 12 | results/deposon_g2_boltzmann_pathintegral.json | 2,204 | 34 | 20 | 15 | 归档区（〔归档区〕） |
| 12 | corpus/v20/all.json | 2,557 | 34 | 21 | 11 | 归档区（〔归档区〕） |
| 12 | docs/Findings_GT2B.md | 3,322 | 34 | 20 | 20 | 归档区（〔归档区〕） |
| 12 | results/deposon_volcengine_minimax_m3_30cells_2026_09_10.json | 23,472 | 34 | 23 | 19 | 归档区（〔归档区〕） |
| 12 | results/_v4_track2_multimodel_rerun_2026_09_23.json | 35,011 | 34 | 25 | 19 | 归档区（〔归档区〕） |
| 12 | audits_security.json | 1,610 | 35 | 24 | 2 | 归档区（〔归档区〕） |
| 12 | results/deposon_risk2_canonical5_decision_2026_09_11.json | 4,066 | 35 | 20 | 17 | 归档区（〔归档区〕） |
| 12 | docs/Findings_GT8B.md | 9,809 | 35 | 21 | 21 | 归档区（〔归档区〕） |
| 12 | results/deposon_v17_fusion_fix_tieartifact_negativeresult.json | 106,125 | 35 | 21 | 19 | 归档区（〔归档区〕） |
| 12 | audits_outliers.json | 132,875 | 35 | 24 | 2 | 归档区（〔归档区〕） |
| 12 | docs/Findings_v2.0_boss.md | 3,642 | 36 | 23 | 23 | 归档区（〔归档区〕） |
| 12 | docs/Findings_v2.0_crossval.md | 4,566 | 36 | 22 | 22 | 归档区（〔归档区〕） |
| 13 | docs/SPEC_v2.0_amendment1.md | 4,743 | 36 | 23 | 22 | 归档区（〔归档区〕） |
| 13 | results/_k_v3df_0_1_four_readings_2026_10_09.json | 65,507 | 36 | 22 | 15 | 归档区（〔归档区〕） |
| 13 | results/deposon_benchmark_v1_4_strategyqa.json | 1,691 | 37 | 23 | 15 | 归档区（〔归档区〕） |
| 13 | docs/BASELINE_REGISTRY.md | 3,356 | 37 | 25 | 24 | 归档区（〔归档区〕） |
| 13 | results/deposon_v20_bigquiz_eval.json | 35,718 | 37 | 23 | 20 | 归档区（〔归档区〕） |
| 13 | results/deposon_volcengine_worker_c_2026_09_10.json | 51,716 | 37 | 24 | 21 | 归档区（〔归档区〕） |
| 13 | results/deposon_v20_fastcheck.json | 1,768 | 38 | 20 | 17 | 归档区（〔归档区〕） |
| 13 | results/deposon_gsm8k_stratified.json | 3,411 | 38 | 21 | 18 | 归档区（〔归档区〕） |
| 13 | results/deposon_risk3_seff_decision_2026_09_11.json | 6,488 | 38 | 17 | 16 | 归档区（〔归档区〕） |
| 13 | docs/SPEC_GT8B.md | 7,486 | 38 | 26 | 26 | 归档区（〔归档区〕） |
| 13 | docs/CLOSURE_v19_and_v2X_gametheory.md | 9,065 | 38 | 24 | 20 | 归档区（〔归档区〕） |
| 13 | results/deposon_v16_paired_stats.json | 9,176 | 38 | 20 | 17 | 归档区（〔归档区〕） |
| 14 | results/deposon_pe_d1_d3_2026_09_15.json | 17,085 | 38 | 19 | 16 | 归档区（〔归档区〕） |
| 14 | results/_runface_vs_shape_multidim_reading_2026_10_20.json | 61,109 | 38 | 37 | 29 | 归档区（〔归档区〕） |
| 14 | results/deposon_v20_gt8b_ingest.json | 986 | 39 | 23 | 19 | 归档区（〔归档区〕） |
| 14 | results/_v3x_p_k_verify_2026_09_16/v3x_p_k_verify_results_2026_09_16.json | 2,059 | 39 | 21 | 20 | 归档区（〔归档区〕） |
| 14 | docs/Findings_GT3.md | 2,632 | 39 | 25 | 24 | 归档区（〔归档区〕） |
| 14 | results/deposon_v20_gt8c.json | 2,864 | 39 | 25 | 19 | 归档区（〔归档区〕） |
| 14 | RELEASE_v1.4.0.md | 3,847 | 39 | 27 | 2 | 归档区（〔归档区〕） |
| 14 | results/deposon_v20_cot_quiz.json | 7,101 | 39 | 21 | 19 | 归档区（〔归档区〕） |
| 14 | results/deposon_p_k_cross_subject_fingerprint_blind_test_2026_09_16.json | 11,341 | 39 | 21 | 19 | 归档区（〔归档区〕） |
| 14 | results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json | 32,995 | 39 | 28 | 23 | 归档区（〔归档区〕） |
| 14 | results/deposon_v17_fixed_sampler.json | 106,317 | 39 | 25 | 22 | 归档区（〔归档区〕） |
| 14 | results/deposon_v22_p1c.json | 763 | 40 | 31 | 20 | 归档区（〔归档区〕） |
| 15 | paper/FIGURE_LANGUAGE_POLICY.md | 2,495 | 40 | 23 | 21 | 归档区（〔归档区〕） |
| 15 | results/_p_n_curvature_potential_coupling_2026_09_16/p_n_curvature_potential_coupling_results_2026_09_16.json | 4,276 | 40 | 21 | 20 | 归档区（〔归档区〕） |
| 15 | docs/Findings_v2.0_corrections.md | 5,012 | 40 | 26 | 26 | 归档区（〔归档区〕） |
| 15 | results/_pa_harness_anchor_value_update_v2.json | 16,043 | 40 | 39 | 27 | 归档区（〔归档区〕） |
| 15 | docs/V3X/P_E_DOUBAN_EMBEDDING_V0_SPEC.md | 16,876 | 40 | 20 | 14 | 归档区（〔归档区〕） |
| 15 | results/deposon_pf_implementation_2026_09_11.json | 27,311 | 40 | 24 | 20 | 归档区（〔归档区〕） |
| 15 | results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json | 204,441 | 40 | 23 | 18 | 归档区（〔归档区〕） |
| 15 | results/_p_i_real_labels_2026_09_16/p_i_real_labels_results_2026_09_16.json | 1,043 | 41 | 23 | 22 | 归档区（〔归档区〕） |
| 15 | results/_p_m_real_separation_2026_09_16/p_m_real_separation_results_2026_09_16.json | 2,042 | 41 | 23 | 22 | 归档区（〔归档区〕） |
| 15 | results/deposon_benchmark_v1_3_simple.json | 2,245 | 41 | 25 | 16 | 归档区（〔归档区〕） |
| 15 | results/_p_o_stranger_verification_2026_09_16/p_o_stranger_verification_results_2026_09_16.json | 5,916 | 41 | 22 | 21 | 归档区（〔归档区〕） |
| 15 | results/deposon_volcengine_minimax_m3_30cells_2026_09_10.py | 11,703 | 41 | 24 | 18 | 归档区（〔归档区〕）·⚠脚本面·须先裁其产出是否已入权威件 |
| 16 | results/deposon_v19_fullrank.json | 42,458 | 41 | 23 | 18 | 归档区（〔归档区〕） |
| 16 | results/deposon_v19_meanfield.json | 44,443 | 41 | 23 | 17 | 归档区（〔归档区〕） |
| 16 | results/deposon_v15_diffusion_maxpath_negativeresult.json | 416,460 | 41 | 27 | 25 | 归档区（〔归档区〕） |
| 16 | results/deposon_benchmark_v1_4_gsm8k.json | 2,741 | 42 | 28 | 18 | 归档区（〔归档区〕） |
| 16 | results/deposon_benchmark_v1_3_traps.json | 3,112 | 42 | 28 | 18 | 归档区（〔归档区〕） |
| 16 | docs/Findings_v2.0_bigquiz.md | 3,291 | 42 | 30 | 30 | 归档区（〔归档区〕） |
| 16 | docs/SPEC_GT3.md | 5,369 | 42 | 29 | 29 | 归档区（〔归档区〕） |
| 16 | results/deposon_v17_multigraph.json | 16,896 | 42 | 24 | 19 | 归档区（〔归档区〕） |
| 16 | results/deposon_v20_quiz_eval.json | 22,623 | 42 | 24 | 20 | 归档区（〔归档区〕） |
| 16 | results/deposon_benchmark_v1_3_details.json | 656,572 | 42 | 28 | 23 | 归档区（〔归档区〕） |
| 16 | docs/SPEC_v1.8.md | 9,850 | 43 | 19 | 19 | 归档区（〔归档区〕） |
| 16 | results/deposon_v20_familyl_ingest.json | 1,303 | 44 | 29 | 26 | 归档区（〔归档区〕） |
| 17 | results/deposon_volcengine_glm_latest_5cells_2026_09_10.py | 8,112 | 44 | 24 | 21 | 归档区（〔归档区〕）·⚠脚本面·须先裁其产出是否已入权威件 |
| 17 | results/deposon_game_theory_eval_2026_09_10.json | 10,096 | 44 | 34 | 25 | 归档区（〔归档区〕） |
| 17 | results/deposon_v16_llm_prior.json | 39,974 | 44 | 26 | 19 | 归档区（〔归档区〕） |
| 17 | results/deposon_v20_gt8b.json | 2,706 | 45 | 31 | 23 | 归档区（〔归档区〕） |
| 17 | docs/Findings_v2.0_photonics.md | 4,377 | 45 | 21 | 21 | 归档区（〔归档区〕） |
| 17 | results/deposon_v20_photonics.json | 6,796 | 45 | 25 | 22 | 归档区（〔归档区〕） |
| 17 | results/deposon_dpath_cross_modal_2026_09_10.json | 75,964 | 45 | 27 | 22 | 归档区（〔归档区〕） |
| 17 | results/deposon_v15_diffusion.json | 519,387 | 45 | 31 | 26 | 归档区（〔归档区〕） |
| 17 | docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md | 4,587 | 46 | 32 | 31 | 归档区（〔归档区〕） |
| 17 | results/deposon_v19_quickwins.json | 7,842 | 46 | 28 | 18 | 归档区（〔归档区〕） |
| 17 | results/deposon_pc_d1_d3_2026_09_15.json | 20,408 | 46 | 27 | 21 | 归档区（〔归档区〕） |
| 17 | results/_p_l_real_data_collapse_2026_09_16/p_l_real_data_collapse_results_v2_2026_09_16.json | 3,761 | 47 | 26 | 24 | 归档区（〔归档区〕） |
| 18 | results/deposon_v3_physical_opt_2026_09_11.json | 17,591 | 47 | 36 | 26 | 归档区（〔归档区〕） |
| 18 | results/deposon_v22_e95ci.json | 1,496 | 48 | 37 | 22 | 归档区（〔归档区〕） |
| 18 | results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json | 9,076 | 48 | 29 | 28 | 归档区（〔归档区〕） |
| 18 | paper/v2/related_work_v2X.md | 10,114 | 48 | 25 | 23 | 归档区（〔归档区〕） |
| 18 | results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json | 5,266 | 49 | 30 | 28 | 归档区（〔归档区〕） |
| 18 | results/deposon_v20_gt7.json | 17,925 | 49 | 30 | 21 | 归档区（〔归档区〕） |
| 18 | results/deposon_volcengine_seed_code_30cells_2026_09_10.json | 23,034 | 49 | 29 | 19 | 归档区（〔归档区〕） |
| 18 | docs/SPEC_GT8.md | 4,181 | 50 | 38 | 24 | 归档区（〔归档区〕） |
| 18 | paper/v2/outline_v2X.md | 10,476 | 50 | 29 | 26 | 归档区（〔归档区〕） |
| 18 | corpus/v20_caption_surface/_p_d_v03_22caption_verification_20260917_163757.json | 13,775 | 50 | 22 | 22 | 归档区（〔归档区〕） |
| 18 | results/deposon_pf_d1_full_9m5c_2026_09_15.json | 33,829 | 50 | 26 | 21 | 归档区（〔归档区〕） |
| 18 | results/boss_pc_2_a2_fitting_2026_09_15.json | 1,024 | 51 | 24 | 21 | 归档区（〔归档区〕） |
| 19 | results/deposon_v20_crossval.json | 8,404 | 51 | 32 | 20 | 归档区（〔归档区〕） |
| 19 | results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json | 18,104 | 51 | 41 | 37 | 归档区（〔归档区〕） |
| 19 | results/deposon_v20_gt5b.json | 56,425 | 52 | 38 | 27 | 归档区（〔归档区〕） |
| 19 | results/boss_pe_3_real_reservoir_2026_09_15.json | 2,364 | 53 | 26 | 22 | 归档区（〔归档区〕） |
| 19 | results/boss_pc_2_real_transverse_ising_2026_09_15.json | 3,553 | 53 | 30 | 23 | 归档区（〔归档区〕） |
| 19 | results/deposon_v20_gt6.json | 65,105 | 53 | 39 | 28 | 归档区（〔归档区〕） |
| 19 | results/.tmp/_s14_main_session_slice_2026_10_21.md | 96,411 | 53 | 52 | 45 | deposon-sub（探针执行器·保可复算性） |
| 19 | results/boss_pc_1_real_2d_ising_2026_09_15.json | 2,460 | 54 | 30 | 22 | 归档区（〔归档区〕） |
| 19 | results/deposon_v20_gt8.json | 5,396 | 55 | 41 | 36 | 归档区（〔归档区〕） |
| 19 | results/boss_pc_3_real_reservoir_2026_09_15.json | 2,364 | 56 | 33 | 27 | 归档区（〔归档区〕） |
| 19 | results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json | 16,835 | 56 | 24 | 20 | 归档区（〔归档区〕） |
| 19 | results/_v4_pi_cot_v2_ruleset.json | 5,876 | 58 | 43 | 27 | 归档区（〔归档区〕） |
| 20 | docs/SPEC_GT8C.md | 6,326 | 58 | 36 | 28 | 归档区（〔归档区〕） |
| 20 | results/boss_pc_1_a1_resampling_2026_09_15.json | 1,017 | 60 | 33 | 26 | 归档区（〔归档区〕） |
| 20 | results/boss_pe_1_real_2d_ising_2026_09_15.json | 2,460 | 60 | 30 | 25 | 归档区（〔归档区〕） |
| 20 | docs/SPEC_GT2B.md | 3,318 | 61 | 40 | 31 | 归档区（〔归档区〕） |
| 20 | docs/SPEC_v2.0.md | 5,333 | 61 | 45 | 43 | 归档区（〔归档区〕） |
| 20 | results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json | 17,053 | 61 | 38 | 37 | 归档区（〔归档区〕） |
| 20 | results/_ge01_prereg_5anchor_v2.json | 21,629 | 61 | 60 | 47 | 归档区（〔归档区〕） |
| 20 | results/deposon_benchmark_v1_4_strategyqa_details.json | 235,779 | 62 | 49 | 46 | 归档区（〔归档区〕） |
| 20 | results/deposon_pa_d1_d3_2026_09_15.json | 15,604 | 63 | 37 | 32 | 归档区（〔归档区〕） |
| 20 | docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md | 34,393 | 63 | 45 | 37 | 归档区（〔归档区〕） |
| 20 | results/deposon_v20_vector_audit.json | 915 | 64 | 36 | 32 | 归档区（〔归档区〕） |
| 20 | results/boss_pe_2_real_transverse_ising_2026_09_15.json | 3,553 | 64 | 37 | 29 | 归档区（〔归档区〕） |
| 21 | docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md | 13,419 | 65 | 27 | 22 | 归档区（〔归档区〕） |
| 21 | corpus/v20_caption_surface/_v41_flash_rag_caption_embs.bak.json | 612,511 | 66 | 40 | 39 | 归档区（〔归档区〕） |
| 21 | results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json | 13,562 | 67 | 45 | 34 | 归档区（〔归档区〕） |
| 21 | docs/GT_FORMALIZATION_v1.md | 19,100 | 67 | 43 | 33 | 归档区（〔归档区〕） |
| 21 | results/deposon_v20_gt5.json | 72,647 | 67 | 46 | 31 | 归档区（〔归档区〕） |
| 21 | results/boss_pa_2_potential_game_result_2026_09_15.json | 7,530 | 68 | 36 | 25 | 归档区（〔归档区〕） |
| 21 | results/deposon_v2_phase1_60cells_2026_09_11.json | 85,508 | 68 | 46 | 35 | 归档区（〔归档区〕） |
| 21 | results/deposon_benchmark_v1_4_gsm8k_details.json | 208,350 | 69 | 53 | 49 | 归档区（〔归档区〕） |
| 21 | results/deposon_v20_gt3.json | 7,844 | 72 | 44 | 37 | 归档区（〔归档区〕） |
| 21 | docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md | 12,501 | 72 | 39 | 30 | 归档区（〔归档区〕） |
| 21 | results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json | 1,669 | 75 | 57 | 54 | 归档区（〔归档区〕） |
| 21 | results/deposon_volcengine_22caption_embedding_2026_09_10.json | 4,559 | 77 | 61 | 41 | 归档区（〔归档区〕） |
| 22 | results/.tmp/_s14_main_events2_2026_10_21.md | 177,579 | 77 | 76 | 69 | deposon-sub（探针执行器·保可复算性） |
| 22 | results/deposon_g1_mindmap_demo.json | 3,041 | 81 | 64 | 50 | 归档区（〔归档区〕） |
| 22 | results/_v4_pi_cot_v2_result.json | 9,068 | 81 | 69 | 43 | 归档区（〔归档区〕） |
| 22 | results/boss_pc_3_a3_clipping_2026_09_15.json | 1,265 | 82 | 55 | 48 | 归档区（〔归档区〕） |
| 22 | audits_dataset_health.json | 7,398 | 82 | 69 | 12 | 归档区（〔归档区〕） |
| 22 | docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md | 11,478 | 82 | 40 | 35 | 归档区（〔归档区〕） |
| 22 | results/deposon_v20_corpus_eval.json | 631,644 | 82 | 54 | 42 | 归档区（〔归档区〕） |
| 22 | results/deposon_v2_phase4_f4_2026_09_11.json | 5,212 | 85 | 73 | 48 | 归档区（〔归档区〕） |
| 22 | docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md | 19,751 | 85 | 45 | 36 | 归档区（〔归档区〕） |
| 22 | results/deposon_pg_v01_9m60c_2026_09_15.json | 11,512 | 86 | 54 | 45 | 归档区（〔归档区〕） |
| 22 | docs/REF_VERIFICATION_v2.md | 5,860 | 87 | 52 | 51 | 归档区（〔归档区〕） |
| 22 | docs/V3X/V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md | 38,545 | 91 | 58 | 52 | 归档区（〔归档区〕） |
| 23 | results/deposon_v3_v7_summary_2026_09_11.json | 25,049 | 95 | 68 | 45 | 归档区（〔归档区〕） |
| 23 | results/c5_b_group_fix_readings_2026_10_01.json | 9,996 | 96 | 64 | 54 | 归档区（〔归档区〕） |
| 23 | results/deposon_v20_gt2b.json | 123,331 | 96 | 66 | 44 | 归档区（〔归档区〕） |
| 23 | results/boss_pa_3_replicator_dynamics_result_2026_09_15.json | 9,098 | 97 | 67 | 56 | 归档区（〔归档区〕） |
| 23 | results/deposon_v18_api_supplements.json | 80,624 | 111 | 81 | 59 | 归档区（〔归档区〕） |
| 23 | results/deposon_v20_gt.json | 3,803 | 115 | 96 | 73 | 归档区（〔归档区〕） |
| 23 | results/deposon_v17_fusion_fix.json | 106,164 | 122 | 89 | 63 | 归档区（〔归档区〕） |
| 23 | results/_ge01_prereg_5anchor.json | 10,701 | 136 | 134 | 115 | 归档区（〔归档区〕） |
| 23 | results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json | 20,398 | 149 | 100 | 90 | 归档区（〔归档区〕） |
| 23 | results/.tmp/_s14_session_scan_out_2026_10_21.md | 1,137,664 | 159 | 158 | 134 | deposon-sub（探针执行器·保可复算性） |
| 23 | corpus/v20/index_v2_2026_09_16.json | 24,150 | 171 | 121 | 97 | 归档区（〔归档区〕） |
| 23 | results/deposon_v21_gtformal.json | 69,204 | 182 | 128 | 94 | 归档区（〔归档区〕） |
| 24 | results/deposon_v19_benchmark_fixes.json | 409,104 | 183 | 128 | 101 | 归档区（〔归档区〕） |
| 24 | corpus/v20/index.json | 7,335 | 226 | 166 | 94 | 归档区（〔归档区〕） |
| 24 | results/deposon_v3_physical_opt_60cells_2026_09_11.json | 17,732 | 226 | 158 | 88 | 归档区（〔归档区〕） |
| 24 | results/boss_pa_1_rbr_rm_result_2026_09_15.json | 8,753 | 236 | 184 | 121 | 归档区（〔归档区〕） |
| 24 | corpus/v20/strip_captions_22.json | 12,798 | 265 | 233 | 130 | 归档区（〔归档区〕） |
| 24 | corpus/v20_caption_surface/strip_captions_22.json | 12,798 | 265 | 233 | 130 | 归档区（〔归档区〕） |
| 24 | results/deposon_v20_baselines.json | 16,987 | 282 | 208 | 147 | 归档区（〔归档区〕） |

**零断链风险批（活路径式引用 ＝ 0）**：可移者 283 件中 **2 件**（3,544 B）之**活面无一处路径式引用** ⇒ 移动即断链处 ＝ 0，**可作首批**（仍须 PI 逐单令）。其名单（按体积降序）：

| 现路径 | bytes | 被引用次数（多为快照面） | 拟归何处 |
|---|---|---|---|
| results/.tmp/_s15_append_2026_10_21.md | 2,459 | 1 | deposon-sub（探针执行器·保可复算性） |
| LICENSE | 1,085 | 0 | 归档区（〔归档区〕） |

### §4-2 不可移者（硬阻／在途／亦入 B 类）

| 现路径 | bytes | 被引用次数 | 其中绝对路径引用 | 不可移之由 |
|---|---:|---:|---:|---|
| results/_achievements_inventory_full_2026_10_09.md | 372,318 | 229 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_v4_pi_cot_v2_verdict.md | 22,340 | 85 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_upload_side_desensitized_remote_sha_letter_kimi_2026_10_12.md | 74,043 | 58 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_pi_card_payload_extraction_2026_10_20.md | 53,460 | 50 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md | 11,752 | 46 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_m41_double_readout_contrast_exec_2026_10_14.md | 17,009 | 44 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_d9_relpath_rewrite_map_2026_10_12.md | 21,352 | 31 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_pre_execution_report_kimi_2026_10_12.md | 7,612 | 22 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_d9_e2e_run_register_2026_10_13.md | 12,581 | 18 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/_gd03_divergence_deliberation_2026_10_21.md | 44,153 | 14 | 0 | 不移动（亦入 B 类·宜经删之令） |
| results/.tmp/_s18_ghost_audit_instrument_v2_out_2026_10_22.json | 34,037,604 | 9 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s17_append_2026_10_22.md | 5,449 | 8 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s17_body_2026_10_22.md | 42,171 | 6 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage3_out_2026_10_22.json | 36,934,926 | 5 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_instrument_out_2026_10_22.json | 36,506,432 | 4 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage4_out_2026_10_22.json | 654,070 | 3 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage6_out_2026_10_22.json | 17,045 | 2 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_emit_2026_10_22.py | 34,758 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_instrument_2026_10_22.py | 9,011 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_instrument_v2_2026_10_22.py | 9,941 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage2v2_2026_10_22.py | 8,218 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage2_2026_10_22.py | 11,510 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage3_2026_10_22.py | 9,656 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage4_2026_10_22.py | 5,343 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage5_2026_10_22.py | 4,136 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage5_out_2026_10_22.json | 2,489,344 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_stage6_2026_10_22.py | 4,069 | 1 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_caliber_2026_10_22.py | 1,926 | 0 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_postfreeze_scan_2026_10_22.json | 887 | 0 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_selfcheck2_2026_10_22.py | 2,673 | 0 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s18_ghost_audit_selfcheck_2026_10_22.py | 2,728 | 0 | 0 | 不移动（在途·今日生成） |
| results/.tmp/_s60_28_body_2026_10_22.md | 15,559 | 0 | 0 | 不移动（在途·今日生成） |

### §4-3 每批执行序之规程（**PI 逐单放行后方可执行**）

1. **每批 ≤ 12 件**，批次号即上表「批」列；⛔ 0 跨批合并。
2. **每批前出对照表（甲）**：全仓件数／全仓字节／C 类在盘件数／C 类在盘字节／本批将移之件名清单（全列）。
3. **每批后出对照表（乙）**：同上五项之复测值 ＋ 逐件「旧路径→新路径」映射行 ＋ 逐件移动后 SHA-12 复算值（须与本索引件所载 **全等**）＋ 逐件 `Test-Path=False`（长名式复测）。
4. **甲乙不符即停手报回**（⛔ 0 续下一批）——本仓**非 git 仓库**，无版本级兜底，回滚只能靠「移动前之 SHA-12＋旧路径」两份账。
5. **幽灵登记同步**：每批后须将本批「旧路径→新路径」逐行追加进幽灵引用登记面——⛔ 0 回改 `_ghost_reference_register_2026_10_21.md` 之既有行（沿「⛔ 0 回改任何既有件一字」之惯例），以**新增**件承载。
6. **绝对路径面未清之前** ⇒ 涉绝对路径之件 ⛔ 0 移（§4-2 已单列）；该面之清理由 PI 另裁（`_results_split_proposal_2026_10_21.md` §1-5 载其量级为 230 件）。

## §5 已识别而未归 C 类之早期纪元件（剔除明细·不藏）

> 以下早期纪元件（mtime < 2026-09-20）**因属他面或 D 类禁动面**而未入 C 类——**⛔ 0 擅动**。列此以便 PI 一字可改其归类。

| 剔除之由 | 件数 | 字节 | 样例（≤4 件） |
|---|---|---|---|
| D-禁动：verifier/ 内建脚本全树 | 103 | 223,609 | verifier/_build_partial.py、verifier/_read_summary.py、verifier/_run.log、verifier/_test_one.py …（余 99 件） |
| 他面：代码源（⛔0 移·移动即破运行/导入） | 73 | 817,308 | attacks/__init__.py、attacks/a2_reshuffle_manifest.py、attacks/a3_rewrite_runs.py、corpus/v20_caption_surface/_inspect_captions.py …（余 69 件） |
| 他面：测试面（⛔0 移·移动即破测试） | 23 | 212,514 | tests/test_agents_merge.py、tests/test_diffusion.py、tests/test_fast.py、tests/test_fingerprint_v0.py …（余 19 件） |
| 他面：插件面（88 plugins·在用） | 19 | 171,808 | deposon_team/plugins/_pg_v01_compute.py、deposon_team/plugins/_verify_batch5_2026_09_18.py、deposon_team/plugins/_verify_pg_v0.py、deposon_team/plugins/_verify_pg_v0_v1.py …（余 15 件） |
| 他面：工具/脚本面（内建·在用） | 14 | 200,247 | scripts/run_deepseek_v41_30cells_v2.py、scripts/run_deepseek_v41_30cells_v3.py、scripts/run_deepseek_v41_60cells_v2_startup.py、scripts/run_embedding_dual_smoke.py …（余 10 件） |
| 他面：letters 外发函件面（PI 传递面） | 7 | 58,571 | letters/LETTER_FROM_TRAE_2026_09_11.md、letters/LETTER_FROM_TRAE_3RISK_2026_09_11.md、letters/LETTER_FROM_TRAE_REVIEW_2026_09_16.md、letters/LETTER_FROM_TRAE_SELFCHECK_FIX_2026_09_15.md …（余 3 件） |
| D-禁动：frozen/anchor 锚件 | 6 | 18,290 | attacks/a1_delete_anchor.py、deposon_team/plugins/_verify_15frozen.py、deposon_team/plugins/_verify_15frozen_v1.py、results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json …（余 2 件） |
| B8/D-面：results 根层 .md 交付件（⛔0 擅动） | 5 | 48,166 | results/_v3x_d0_5_aggregation_2026_09_17.md、results/_v3x_d0_5_experiment_invitation_2026_09_17.md、results/_v3x_d0_5_proposal_coze_2026_09_17.md、results/_v3x_p_l_v3_external_spec_2026_09_17.md …（余 1 件） |
| D-禁动：5 制品 baseline | 4 | 82,332 | corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json、corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json、corpus/v20/by_model/kimi/index_v2_2026_09_16.json、corpus/v20/by_model/minimax/artifact_v_2026_09_16.json |
| 他面：工具/IDE 配置面 | 2 | 34,781 | .trae/scripts/_arxiv_renumber.py、.trae/scripts/_verify_tex.py |
| D-禁动：schema v1 | 1 | 12,919 | deposon_team/plugins/_v3x_frozen_schema_v1.json |
| D-禁动：归档区（results\_archive_*） | 1 | 11,105 | results/_archive_2026_09_24/_volc_22cap_emb.py |

**剔除小计**：258 件／1,891,650 B；早期纪元全量 470 件 − 剔除 258 件 ＝ **C2 留 209 件**。

⚠ **最大之剔除桶为「代码源」**（仓内 `.py`／`.sh` 等·移动即破运行与导入）——**⛔ 0 移**。本棒据此**不**将仓根代码源列入 C 类归档候选（此为与前案分类之**显式分歧**，已在 §7 老实交代第 4 条载明）。

## §6 前案并读（本件之增量·⛔ 0 重复造案）

| 前案 | 其已载 | 本件之增量 |
|---|---|---|
| `_cleanup_noise_register_2026_10_21.md`（`5ca28bb4c73a`） | §4.1 同族旧版 **28 件**名单在册；§4.2 早期纪元 116 件／7,875,415 B | 本件**逐件复算** SHA-12／bytes／mtime／被引次数并出**移动序**；**未改其任何一行**。⚠ 本棒实测早期纪元为 **470 件**（mtime 口径·全仓）——与前案 116 件**不一致**（前案之 116 未载其口径，本棒**不复现**该数；口径差异见 §5 剔除表） |
| `_results_index_v2_2026_10_21.md`（`8487e4a34d29`） | results 现行目录清单 v2；早期纪元 116 件／7.88 MB 之**概数** | 本件给出**逐件**之 C 类映射表（该件止于概数） |
| `_results_split_proposal_2026_10_21.md`（`38eff36f1438`） | 候选戊（三档递进）之荐案：档0 索引件／档2 族级移动俟 PI 逐单令；230 件绝对路径钉住面 | 本件即**其档0 之实体化**（索引件＋旧路径→新路径映射表）；档2 之 230 面硬阻**本件未清**（清之须 PI 另裁） |
| `_ghost_reference_register_2026_10_21.md`（`e927dfce3464`）／`_ghost_reference_audit_2026_10_22.md`（`37659d4a398a`） | 幽灵判定面（6,951 对成对总体／四区 48,084 件索引面） | 本件**不重判**其幽灵面；只就 C 类移动**预生**「须补登记」之映射行 |
| `_bloat_inventory_2026_10_22.md`（`3c55ea8be914`） | 四分类判据；C 类 144＋（另 `results\.tmp` 58）；路径式 token 200,432 vs basename 52,833 | 本件**按其判据实测落地**（早期纪元之实件数、探针族之实件数、绝对路径钉住之实处数皆本棒自测） |

## §7 老实交代（限制面·八条）

1. **一切计数为时点截面**（观测时点 2026-10-22 13:54:25）——本仓为**活面**（量测期间件数由 6,758 增至 **6,763**；末次复测时 mtime 落在观测日者 **118 件**＝在途）；执行前须重测。
2. **被引用次数之射程 ＝ 主面**（md＋txt＋py＋log，5801 件／136,622,760 B）——**未覆盖 `.json`／`.tsv` 之正文**（彼等仅以其**文件名**被引时计入）⇒ 本件之数为**下界**；另以「＋jsonl＋csv＋err＋out」之宽面复测（5849 件／138,327,871 B），宽面命中 ≥ 主面。
3. **「被引用次数」按 basename 命中计**——同名异件（跨目录重名）之引用**计于该名下之全部件**；故本件之数**不含**归因误差之修正。**另设「活引用次数」列**（＝扣去快照面之提及：`_c514_remote_blobs_2026_10_18/` 镜像副本 514 件与 `_cleanup_sha_prefix_index_4zone_2026_10_21.txt` 索引 1 件内之文本提及——**二者为快照，随快照件存亡，不因原件移动而断**）⇒ 移动之真实断链面以**活引用**为准。
4. **早期纪元之界以 mtime 判**——mtime 可被工具改写（如 `touch`）⇒「早期」为**可改之量**，非内容断代；前案 116 件之口径本棒**未能复现**（不伪称相符）。**且本棒之 C2 口径与前案有显式分歧**：本棒**剔除外** 258 件（其中 73 件为**代码源**——移动即破运行与导入），故 C2 由「全量 470 件」收窄为 **209 件**（另有 3 件同属 C1，计于 C1）；此收窄为**本棒之判断**（⛔ 0 代裁），PI 一字即可改回全量。
5. **参量与派工单之 83.6% 不符**：派工单据前案载「`.tmp` 占 83.6%」——该数成于 00:39–00:51（全仓 645,001,204 B／615.1 MB 之截面）。本棒实测全仓 802,875,238 B、`.tmp` 539,646,644 B ＝ **67.2%**（差额来自 `results\.tmp` 当日新增之 s18 仪器输出 102.5 MB）⇒ **以本棒实测为准**。
6. **拟归何处为「拟」**——PI 逐单令前 ⛔ 0 移动；`deposon-sub` 与 `归档区` 之落点**尚未与两区既有件重名核销**（本棒已列各区件数：deposon-sub 1,276 件／归档区 40,121 件）。
7. **在途面已单列**（观测日 mtime 者 ⛔ 0 擅动）——`results\.tmp` 之 3 件 s18 仪器输出（102.5 MB）即属此面。
8. **本件 ⛔ 0 触归档区内件**（仅列名与件数）·⛔ 0 触 `GLM` 面·⛔ 0 联网·⛔ 0 读 key·⛔ 0 LLM·⛔ 0 落五终判·⛔ 0 闭 KD·⛔ 0 宣告段毕·⛔ 0 代裁。

## §8 本棒 0 移 0 删 之实证

| 项 | 实测 |
|---|---|
| 删既有件（任何口径·含回收站通道） | **0** |
| 回收**本棒自身**之首稿（同名两件·非既有件·可恢复通道 `mavis-trash`） | **2**（本棒自产之稿，首稿→修正稿；仓内既有件 0 触） |
| 移动 | **0** |
| 改名 | **0** |
| 新建目录 | **0** |
| 本棒于仓内之写入 | **2 件**＝本件 ＋ 件二（`_results_c_class_index_2026_10_22.md`／`_cleanup_b_class_list_2026_10_22.md`） |
| 本棒于仓外之写入 | 7 件量测脚本 ＋ 中间 JSON／log（`〔本地路径已脱敏〕`·仓外·非交付件） |
| 回改既有件之字节 | **0 字** |
| 触 `GLM` 面 / 联网 / 读 key / LLM 调用 | **0 / 0 / 0 / 0** |
| 遍历错误数（`os.walk` onerror 计数） | **0** |
| 读错数 | **0** |

*件止。索引与序已出；移动与删除皆未执行（须 PI 逐单令）。*
