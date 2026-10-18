# ARCHIVE-WHITELIST-PURGE 执行登记件（deposon ①段 · PI Q1 令「清除（须 PI 令）」）

- 生成者：worker（ARCHIVE-WHITELIST-PURGE）｜父会话：mvs_bbeb804b1a6a41109be740636eed1709
- 生成时点：2026-10-17 12:26:49（本机）
- 清除通道：**唯一** `SHFileOperationW` + `FOF_ALLOWUNDO`（flags=1108 = 0x0400 NOERRORUI + 0x0040 ALLOWUNDO + 0x0010 NOCONFIRMATION + 0x0004 SILENT；目录另加 0x0200 NOCONFIRMMKDIR）
- ⛔ 未使用 `rm` / `shutil.rmtree` / `Remove-Item` / 任何其他删除机制

## 1. 授权链（逐字照录）

| 项 | 值 |
|---|---|
| 交互卡号 | `ask_69efe394d3e5b6865e529026`（PI 卡答 · Q1） |
| 选项 id | `q1_5e3acedc_opt2` |
| 提交时间 | ms `1792210567075` |
| PI 逐字答复 | **「清除（须 PI 令）」** |
| v50 登记件 | `188ac0656715` · KD-6 载许可射程未及（白名单备份棒于改道指令前按其许可解读写入） |

授权射程之辨（照录派工）：

- 目标：归档区白名单副本 `〔本地归档区〕\whitelist_backup_2026_10_17\`（699 件 / 38,301,580 B）。
- **仅留** `.tmp/whitelist_backup_2026_10_17/` 副本为生效备份面（⛔0 动）——本次未动，逐节 6 复测为证。
- 归档区之「0 写」之其余面与「0 上传」维持不变；「读取不违纪」（PI 2026-10-13 射程纠正）。
- ⛔0 网络（本棒未发起任何网络请求）；⛔0 宣告①毕。

## 2. 目标面核验（清除前必做前置）

### 2.1 双面清单与 SHA-12 逐件对照

| 项 | 目标面（待清除） | 备份面（生效·⛔0 动） |
|---|---|---|
| 路径 | `〔本地归档区〕\whitelist_backup_2026_10_17` | `_repo_mirror\.tmp\whitelist_backup_2026_10_17` |
| 存在 | True | True |
| 件数 | 699 | 699 |
| 目录数 | 2 | 2 |
| 总字节 | 38,301,580 | 38,301,580 |
| 逐件 SHA-12 全算 | 是 | 是 |
| `os.walk` 遍历错误数 | 0 | 0 |

对照结果（`inventory_compare.json`）：

| 比较项 | 结果 |
|---|---|
| 共有相对路径 | 699 |
| 仅存于目标面 | 0 |
| 仅存于备份面 | 0 |
| SHA-12 不等 | 0 |
| 字节数不等 | 0 |
| 目录集差异（仅目标面 / 仅备份面） | 0 / 0（即两目录集**相等**） |
| 裁定 | **IDENTICAL_699** |

> 前置判据（照录派工）：「先确证 .tmp 副本 699/699 在位且 SHA-12 全等——若 .tmp 副本有缺则停手报 parent」。实测 **699/699 在位、SHA-12 全等、0 遍历错误** → 前置满足，准予进入验道。

## 3. 小样验道（硬性先行，先于任何批量处置）

| 项 | 值 |
|---|---|
| 样本 | `docwriter_v46_card_raw.txt`（目标面内最小非空件，26 B） |
| 期望 SHA-12 | `e31064337198` |
| 调用前回收站条目数 | 65 |
| `SHFileOperationW` rc | 0 |
| `fAnyOperationsAborted` | False |
| 源件消失 | True |
| 新增 `$I` | `$IMHA15T.txt`（206 B） |
| 新增 `$R` | `$RMHA15T.txt` |
| `$I` 路径起始偏移 | **28** |
| `$I` 解码原路径 | `〔本地归档区〕\whitelist_backup_2026_10_17\docwriter_v46_card_raw.txt` |
| `$I` 原尺寸字段 | 26（= 样本 26 B） |
| `$R` 载荷 SHA-12 复验 | `e31064337198` = 期望值 → **全等** |
| 验道裁定 | **CHANNEL_VERIFIED** |

逐项判定：

- [PASS] op_rc_zero — rc=0
- [PASS] not_aborted — aborted=False
- [PASS] source_removed — 〔本地归档区〕\whitelist_backup_2026_10_17\docwriter_v46_card_raw.txt
- [PASS] one_new_I_record — ['$IMHA15T.txt']
- [PASS] one_new_R_record — ['$RMHA15T.txt']
- [PASS] I_R_stem_paired — $IMHA15T.txt <-> $RMHA15T.txt (key=MHA15T.txt)
- [PASS] I_path_offset_is_28 — 28
- [PASS] I_decoded_path_matches_source — decoded='〔本地资料区〕\\_non_upload_local_archive\\whitelist_backup_2026_10_17\\docwriter_v46_card_raw.txt'
- [PASS] I_orig_size_matches — 26 vs 26
- [PASS] R_payload_sha12_matches_inventory — e31064337198 vs e31064337198

**首判据缺陷与复判（照录）**：首判以 `os.path.splitext()` 比较 `$IMHA15T.txt` 与 `$RMHA15T.txt`，而 `$I`/`$R` 前缀本就相异，故该等式结构上永不成立——属**我方判据缺陷**，非通道缺陷。复判改以「去前缀后的共有基名」为配对键：

| 复判项 | 值 |
|---|---|
| `$I` 配对键 | `MHA15T.txt` |
| `$R` 配对键 | `MHA15T.txt` |
| 配对键相等 | **True** |
| 复判时记录仍在回收站 | True |
| 复判后裁定 | **CHANNEL_VERIFIED** |

> 验道全程只处置这 1 件（其本身即清除目标之一），未额外消耗任何他件；`.tmp` 面未动。

## 4. 清除执行 · 逐件对照表

每件处置链：`SHFileOperationW` → rc/aborted → 源件消失 → 新增 `$I` 恰 1 → `$I` 解码原路径逐字比对 → `$I` 原尺寸比对 → `$R` 载荷 SHA-12 复算 → 成对判定。

| # | 相对路径 | 字节 | SHA-12(期望) | `$I` | `$R` | 偏移 | `$I` 原路径吻合 | `$R` 载荷 SHA-12 吻合 | 判定 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `docwriter_v46_card_raw.txt` | 26 | `e31064337198` | `$IMHA15T.txt` | `$RMHA15T.txt` | 28 | 是 | 是（`e31064337198`） | **验道** |
| 2 | `_26b_verdict_prep_hashcheck_2026_10_01.py` | 3842 | `6927c9462f41` | `$ICK9PCA.py` | `$RCK9PCA.py` | 28 | 是 | 是 | **通过** |
| 3 | `_26b_verdict_prep_literalcheck_2026_10_01.py` | 4378 | `50fe799b0a2e` | `$IIURSME.py` | `$RIURSME.py` | 28 | 是 | 是 | **通过** |
| 4 | `_26b_verdict_prep_validate_2026_10_01.py` | 4640 | `494cca45b873` | `$IJ8BVSS.py` | `$RJ8BVSS.py` | 28 | 是 | 是 | **通过** |
| 5 | `_659_compact.txt` | 155628 | `795862c09a40` | `$I3GB9AA.txt` | `$R3GB9AA.txt` | 28 | 是 | 是 | **通过** |
| 6 | `_659_overlap_digest.txt` | 239157 | `4f20b8085fb9` | `$IVWA3Z3.txt` | `$RVWA3Z3.txt` | 28 | 是 | 是 | **通过** |
| 7 | `_659_report_gen.py` | 27457 | `cd4b8ed56b2c` | `$I66D4UV.py` | `$R66D4UV.py` | 28 | 是 | 是 | **通过** |
| 8 | `_abc_diff_2026_10_10.py` | 6620 | `6d6733f0e5c2` | `$II22KCH.py` | `$RI22KCH.py` | 28 | 是 | 是 | **通过** |
| 9 | `_abc_final_2026_10_10.py` | 7329 | `15b4de4fdff6` | `$I4JFV9V.py` | `$R4JFV9V.py` | 28 | 是 | 是 | **通过** |
| 10 | `_abc_h1h2_2026_10_10.py` | 7889 | `16f19bad301f` | `$IHD8GVO.py` | `$RHD8GVO.py` | 28 | 是 | 是 | **通过** |
| 11 | `_abc_readings_reprocheck_2026_10_10.py` | 9491 | `0ec2a2bf3bab` | `$IBJEWAQ.py` | `$RBJEWAQ.py` | 28 | 是 | 是 | **通过** |
| 12 | `_abc_readings_reprocheck_out_2026_10_10.json` | 78436 | `2f9aa16b63ca` | `$IGAWZ2F.json` | `$RGAWZ2F.json` | 28 | 是 | 是 | **通过** |
| 13 | `_abc_rfd_2026_10_10.py` | 5938 | `39268ca6adff` | `$ILWJWLD.py` | `$RLWJWLD.py` | 28 | 是 | 是 | **通过** |
| 14 | `_aggregate_10cells.py` | 3009 | `3bdc6250d0f2` | `$II86VT4.py` | `$RI86VT4.py` | 28 | 是 | 是 | **通过** |
| 15 | `_aggregate_10cells_v2.py` | 5131 | `af1b7f09f74d` | `$IP612NI.py` | `$RP612NI.py` | 28 | 是 | 是 | **通过** |
| 16 | `_aggregate_10cells_v3.py` | 2969 | `04b127d80bf0` | `$I6OE7E5.py` | `$R6OE7E5.py` | 28 | 是 | 是 | **通过** |
| 17 | `_aggregate_10cells_v4.py` | 2454 | `f99a3765c3c3` | `$IJ3YI2R.py` | `$RJ3YI2R.py` | 28 | 是 | 是 | **通过** |
| 18 | `_append_intake_supplement_6_tail.py` | 9335 | `c3339682d68c` | `$I2LWCLR.py` | `$R2LWCLR.py` | 28 | 是 | 是 | **通过** |
| 19 | `_audit3b.txt` | 50554 | `e64565a2b180` | `$IOPLOUR.txt` | `$ROPLOUR.txt` | 28 | 是 | 是 | **通过** |
| 20 | `_audit_part3_out.txt` | 5195 | `85a9d9861d38` | `$IDDMUW5.txt` | `$RDDMUW5.txt` | 28 | 是 | 是 | **通过** |
| 21 | `_audit_part4.txt` | 14826 | `def27c1c3511` | `$IN2MO4H.txt` | `$RN2MO4H.txt` | 28 | 是 | 是 | **通过** |
| 22 | `_b12_q1_refs_2026_09_29.py` | 4890 | `86b2d9b7b7bd` | `$I2WQ1ZM.py` | `$R2WQ1ZM.py` | 28 | 是 | 是 | **通过** |
| 23 | `_b12_q1_timeslice_2026_09_29.py` | 798 | `bacf6379b9bf` | `$IO0OOCG.py` | `$RO0OOCG.py` | 28 | 是 | 是 | **通过** |
| 24 | `_b12_q4_adjacent_2026_09_29.py` | 5709 | `61cbc9965896` | `$IUAZMVH.py` | `$RUAZMVH.py` | 28 | 是 | 是 | **通过** |
| 25 | `_b12_q4_exact_2026_09_29.py` | 7140 | `79eba6136d83` | `$IML1LL6.py` | `$RML1LL6.py` | 28 | 是 | 是 | **通过** |
| 26 | `_b12_q4_formcand_2026_09_29.py` | 6510 | `f58f388996d4` | `$IXEE41B.py` | `$RXEE41B.py` | 28 | 是 | 是 | **通过** |
| 27 | `_b12_tables_2026_09_29.py` | 1907 | `10db58be72cf` | `$ISXJ0Y9.py` | `$RSXJ0Y9.py` | 28 | 是 | 是 | **通过** |
| 28 | `_build_5anchor_json_draft.py` | 34455 | `391e7a1be0e5` | `$I15RR8V.py` | `$R15RR8V.py` | 28 | 是 | 是 | **通过** |
| 29 | `_build_5anchor_json_v1.py` | 11627 | `56c459492ecf` | `$ICJKUE9.py` | `$RCJKUE9.py` | 28 | 是 | 是 | **通过** |
| 30 | `_build_intake_supplement_6.py` | 13094 | `6336456853ae` | `$ILKET5O.py` | `$RLKET5O.py` | 28 | 是 | 是 | **通过** |
| 31 | `_build_receipt_supplement_6.py` | 11430 | `20c44c665b4f` | `$IUO4PN7.py` | `$RUO4PN7.py` | 28 | 是 | 是 | **通过** |
| 32 | `_c5_b3_rewalk_postcheck_2026_10_01.py` | 2249 | `aca7dad6ddfa` | `$I10L493.py` | `$R10L493.py` | 28 | 是 | 是 | **通过** |
| 33 | `_c5_b3_rewalk_precheck_2026_10_01.py` | 2035 | `4aad531a2ddb` | `$IZWK9GD.py` | `$RZWK9GD.py` | 28 | 是 | 是 | **通过** |
| 34 | `_c5_b3_rewalk_utf8check_2026_10_01.py` | 925 | `5488ff2db11f` | `$IMDB3WA.py` | `$RMDB3WA.py` | 28 | 是 | 是 | **通过** |
| 35 | `_c5_b_group_fix_readings_2026_10_09.py` | 12289 | `b6855b38acc2` | `$IRM67AZ.py` | `$RRM67AZ.py` | 28 | 是 | 是 | **通过** |
| 36 | `_c5_feasibility_probe.py` | 1036 | `d730612b0c9a` | `$ITTHB04.py` | `$RTTHB04.py` | 28 | 是 | 是 | **通过** |
| 37 | `_canonical_census.py` | 4382 | `36b7af564c56` | `$IZY0BYB.py` | `$RZY0BYB.py` | 28 | 是 | 是 | **通过** |
| 38 | `_canonical_lines.json` | 15033 | `9b0997fc7e52` | `$IDCEU4Z.json` | `$RDCEU4Z.json` | 28 | 是 | 是 | **通过** |
| 39 | `_canonical_lines.py` | 3354 | `08aa8638a0b2` | `$IKYBVC2.py` | `$RKYBVC2.py` | 28 | 是 | 是 | **通过** |
| 40 | `_check_escape.py` | 332 | `5f026b0baf39` | `$I6L7UFS.py` | `$R6L7UFS.py` | 28 | 是 | 是 | **通过** |
| 41 | `_check_kimi_sides.py` | 1459 | `4f3291959a6d` | `$IIYST6Q.py` | `$RIYST6Q.py` | 28 | 是 | 是 | **通过** |
| 42 | `_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | 20997 | `b0cf9baba64b` | `$I80LNXW.py` | `$R80LNXW.py` | 28 | 是 | 是 | **通过** |
| 43 | `_cleanup_r2_cleanlist.json` | 810 | `ce71dda28157` | `$IP9BRA6.json` | `$RP9BRA6.json` | 28 | 是 | 是 | **通过** |
| 44 | `_cleanup_r2_exec.py` | 7884 | `a2029c340ac5` | `$I4Y1ZKN.py` | `$R4Y1ZKN.py` | 28 | 是 | 是 | **通过** |
| 45 | `_cleanup_r2_exec_journal.json` | 10327 | `cd636cb64813` | `$IX3X162.json` | `$RX3X162.json` | 28 | 是 | 是 | **通过** |
| 46 | `_cleanup_r2_postcheck.json` | 6652 | `720b25650bcd` | `$IM7OD81.json` | `$RM7OD81.json` | 28 | 是 | 是 | **通过** |
| 47 | `_cleanup_r2_postcheck.py` | 4585 | `cfd60493f18d` | `$IMYLBFU.py` | `$RMYLBFU.py` | 28 | 是 | 是 | **通过** |
| 48 | `_cleanup_r2_scan.py` | 11507 | `60d6d3d37076` | `$IULBBAX.py` | `$RULBBAX.py` | 28 | 是 | 是 | **通过** |
| 49 | `_cleanup_r2_scan2.py` | 12112 | `7019c7b8d728` | `$IKZIAHF.py` | `$RKZIAHF.py` | 28 | 是 | 是 | **通过** |
| 50 | `_cleanup_r2_scan3.py` | 12389 | `46b7b8230e86` | `$IN2YECP.py` | `$RN2YECP.py` | 28 | 是 | 是 | **通过** |
| 51 | `_cleanup_r2_scan_out.json` | 758995 | `3b107c078490` | `$I7Y8I93.json` | `$R7Y8I93.json` | 28 | 是 | 是 | **通过** |
| 52 | `_compute_metrics.py` | 7752 | `ae2b0142b09e` | `$IZOKBOM.py` | `$RZOKBOM.py` | 28 | 是 | 是 | **通过** |
| 53 | `_compute_metrics_v2.py` | 8017 | `0620ef317e8a` | `$I5PSI9C.py` | `$R5PSI9C.py` | 28 | 是 | 是 | **通过** |
| 54 | `_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | 31745 | `3a240806c2d3` | `$I8U0MWF.md` | `$R8U0MWF.md` | 28 | 是 | 是 | **通过** |
| 55 | `_cpatomic_dump_pyc_2026_09_28.py` | 468 | `d7c9ac28b096` | `$IBOELE0.py` | `$RBOELE0.py` | 28 | 是 | 是 | **通过** |
| 56 | `_cpatomic_keyscan_2026_09_28.py` | 3074 | `393a8d3fa68f` | `$I4LKBTB.py` | `$R4LKBTB.py` | 28 | 是 | 是 | **通过** |
| 57 | `_cpatomic_make_fix_2026_09_28.py` | 7796 | `76c822b640a0` | `$IM8J7KP.py` | `$RM8J7KP.py` | 28 | 是 | 是 | **通过** |
| 58 | `_cpatomic_pycache_post_2026_09_28.py` | 5164 | `171b2a31c0e1` | `$I8Q1ZX7.py` | `$R8Q1ZX7.py` | 28 | 是 | 是 | **通过** |
| 59 | `_cpatomic_pycache_pre_2026_09_28.py` | 3912 | `b86619676bf4` | `$IX4FD2R.py` | `$RX4FD2R.py` | 28 | 是 | 是 | **通过** |
| 60 | `_cpatomic_register_2026_09_28.json` | 29361 | `b68d7ff817bb` | `$IL5XVXO.json` | `$RL5XVXO.json` | 28 | 是 | 是 | **通过** |
| 61 | `_cpatomic_register_2026_09_28.py` | 6322 | `98fe9fa24e80` | `$ILL00PL.py` | `$RLL00PL.py` | 28 | 是 | 是 | **通过** |
| 62 | `_cpatomic_verify_2026_09_28.py` | 11036 | `85139011457c` | `$IGNTMQQ.py` | `$RGNTMQQ.py` | 28 | 是 | 是 | **通过** |
| 63 | `_crosscheck_messages_35_48.py` | 1608 | `dcfe48359488` | `$IY3S1XQ.py` | `$RY3S1XQ.py` | 28 | 是 | 是 | **通过** |
| 64 | `_d05_b_coincidence_checks_2026_10_10.py` | 22078 | `c1fc428d450c` | `$IQRIUOZ.py` | `$RQRIUOZ.py` | 28 | 是 | 是 | **通过** |
| 65 | `_d05_caliber_2026_10_10.py` | 8011 | `65cb84529cb2` | `$IY3R1JJ.py` | `$RY3R1JJ.py` | 28 | 是 | 是 | **通过** |
| 66 | `_d05_instrument_audit.py` | 5948 | `edfa99486954` | `$I1ZTZN2.py` | `$R1ZTZN2.py` | 28 | 是 | 是 | **通过** |
| 67 | `_d05_s4only_2026_10_10.py` | 3438 | `802069e2c06e` | `$I9JHKK4.py` | `$R9JHKK4.py` | 28 | 是 | 是 | **通过** |
| 68 | `_d05_three_checks_recheck_2026_10_10.py` | 11134 | `fc1201cb71e7` | `$IAVFFQP.py` | `$RAVFFQP.py` | 28 | 是 | 是 | **通过** |
| 69 | `_d05_three_checks_recheck_out_2026_10_10.json` | 3622 | `4eb425260682` | `$IBVTMTF.json` | `$RBVTMTF.json` | 28 | 是 | 是 | **通过** |
| 70 | `_dfam_corr_src_2026_10_12.md` | 33471 | `12da29eb102c` | `$I1F1GC3.md` | `$R1F1GC3.md` | 28 | 是 | 是 | **通过** |
| 71 | `_diff21_anchor_drift.py` | 960 | `de2a99cf1999` | `$II1CWUH.py` | `$RI1CWUH.py` | 28 | 是 | 是 | **通过** |
| 72 | `_docwriter_night_headers.txt` | 52370 | `729875e7999e` | `$I37ZCTG.txt` | `$R37ZCTG.txt` | 28 | 是 | 是 | **通过** |
| 73 | `_docwriter_night_measure.json` | 22679 | `f5bacfac3f1c` | `$I846L5A.json` | `$R846L5A.json` | 28 | 是 | 是 | **通过** |
| 74 | `_docwriter_q4_l117_append_block.md` | 4857 | `7c7d633047e4` | `$IUKJO2U.md` | `$RUKJO2U.md` | 28 | 是 | 是 | **通过** |
| 75 | `_docwriter_recheck.py` | 2374 | `54b522e4e2fe` | `$I5LUM9X.py` | `$R5LUM9X.py` | 28 | 是 | 是 | **通过** |
| 76 | `_docwriter_write_handover.py` | 49400 | `a553d705a482` | `$IDO6N27.py` | `$RDO6N27.py` | 28 | 是 | 是 | **通过** |
| 77 | `_dump_dkb3_records2_2026_10_10.py` | 1366 | `e71d1e81da64` | `$IEKKNLD.py` | `$REKKNLD.py` | 28 | 是 | 是 | **通过** |
| 78 | `_dump_dkb3_records_2026_10_10.py` | 1781 | `144b204237bf` | `$IH9ROZQ.py` | `$RH9ROZQ.py` | 28 | 是 | 是 | **通过** |
| 79 | `_dup_name_diff_content_scan2_2026_10_08.py` | 7547 | `b3fe206ef866` | `$ITODUZZ.py` | `$RTODUZZ.py` | 28 | 是 | 是 | **通过** |
| 80 | `_dup_name_diff_content_scan_2026_10_08.py` | 4519 | `675cc3136e70` | `$IJ8NPTB.py` | `$RJ8NPTB.py` | 28 | 是 | 是 | **通过** |
| 81 | `_dw_abs_scan.json` | 56306 | `5c584826ed16` | `$IZSAK3Y.json` | `$RZSAK3Y.json` | 28 | 是 | 是 | **通过** |
| 82 | `_e47_docwriter_count.py` | 1124 | `33cc563b9471` | `$I8T8G6I.py` | `$R8T8G6I.py` | 28 | 是 | 是 | **通过** |
| 83 | `_e48_apply.py` | 2329 | `d4e6f0934e5f` | `$ITAZ1K4.py` | `$RTAZ1K4.py` | 28 | 是 | 是 | **通过** |
| 84 | `_e48_c1.md` | 5039 | `c2a814a90330` | `$IQMQZ9Z.md` | `$RQMQZ9Z.md` | 28 | 是 | 是 | **通过** |
| 85 | `_e48_c2.md` | 5966 | `4d3cae4cbcc0` | `$IUUBT39.md` | `$RUUBT39.md` | 28 | 是 | 是 | **通过** |
| 86 | `_e48_c3.md` | 6563 | `769c71475404` | `$IVV5W46.md` | `$RVV5W46.md` | 28 | 是 | 是 | **通过** |
| 87 | `_e48_c4.md` | 21710 | `8143d01ca0e1` | `$IMDVEQ4.md` | `$RMDVEQ4.md` | 28 | 是 | 是 | **通过** |
| 88 | `_e48_c5.md` | 1686 | `2f7ab971f691` | `$IZW03SP.md` | `$RZW03SP.md` | 28 | 是 | 是 | **通过** |
| 89 | `_e48_docwriter_chain.py` | 2550 | `da5e16e02b7d` | `$IHP416X.py` | `$RHP416X.py` | 28 | 是 | 是 | **通过** |
| 90 | `_e48_docwriter_enum.py` | 1248 | `80bad142f13d` | `$IYTLPBF.py` | `$RYTLPBF.py` | 28 | 是 | 是 | **通过** |
| 91 | `_e48_docwriter_hash.py` | 2578 | `4656b3b734c5` | `$I9Y4VF7.py` | `$R9Y4VF7.py` | 28 | 是 | 是 | **通过** |
| 92 | `_e48_docwriter_hash2.py` | 1229 | `9a3c5b05e29e` | `$I1M7Q7E.py` | `$R1M7Q7E.py` | 28 | 是 | 是 | **通过** |
| 93 | `_e48_probe_register.py` | 873 | `d92f74712dab` | `$IWCK4MY.py` | `$RWCK4MY.py` | 28 | 是 | 是 | **通过** |
| 94 | `_e49_c1.md` | 13607 | `1e6e30d4ce4d` | `$I83R9AW.md` | `$R83R9AW.md` | 28 | 是 | 是 | **通过** |
| 95 | `_e49_c2.md` | 17872 | `11beaed14ea7` | `$IVZRPSP.md` | `$RVZRPSP.md` | 28 | 是 | 是 | **通过** |
| 96 | `_e6_alt_permp_closure_analysis_2026_10_10.py` | 2736 | `affabef74de4` | `$IA6JXFL.py` | `$RA6JXFL.py` | 28 | 是 | 是 | **通过** |
| 97 | `_e6_alt_permp_closure_runner_2026_10_10.py` | 9985 | `9bb254aa58a9` | `$IR28HAI.py` | `$RR28HAI.py` | 28 | 是 | 是 | **通过** |
| 98 | `_e6_ndjt_recompute_2026_10_10.py` | 5064 | `59c2d618305f` | `$IE4YEUK.py` | `$RE4YEUK.py` | 28 | 是 | 是 | **通过** |
| 99 | `_e_q_doc.md` | 28259 | `71f5a0769dab` | `$ICZ2WSH.md` | `$RCZ2WSH.md` | 28 | 是 | 是 | **通过** |
| 100 | `_e_q_exec.json` | 6161 | `d4bd8c92201f` | `$IST0J2U.json` | `$RST0J2U.json` | 28 | 是 | 是 | **通过** |
| 101 | `_e_q_exec.txt` | 0 | `e3b0c44298fc` | `$IICLKL6.txt` | `$RICLKL6.txt` | 28 | 是 | 是 | **通过** |
| 102 | `_ea_179_domain_retest_2026_10_09.py` | 2814 | `9309e4977b22` | `$IYPT18O.py` | `$RYPT18O.py` | 28 | 是 | 是 | **通过** |
| 103 | `_ecr_pa_a0_recompute_2026_10_15.py` | 8804 | `92e204d66c84` | `$IK9YMUV.py` | `$RK9YMUV.py` | 28 | 是 | 是 | **通过** |
| 104 | `_ecr_pa_register_src_2026_10_15.md` | 15707 | `2c7c202aafec` | `$IFOCA9P.md` | `$RFOCA9P.md` | 28 | 是 | 是 | **通过** |
| 105 | `_en_final_2026_09_28.py` | 2369 | `97a05aace5a8` | `$I7E4MR6.py` | `$R7E4MR6.py` | 28 | 是 | 是 | **通过** |
| 106 | `_en_verify2_2026_09_28.py` | 1870 | `7e84e75cb838` | `$I19J961.py` | `$R19J961.py` | 28 | 是 | 是 | **通过** |
| 107 | `_en_verify3_2026_09_28.py` | 1638 | `658292cce916` | `$IZN1ZS2.py` | `$RZN1ZS2.py` | 28 | 是 | 是 | **通过** |
| 108 | `_en_verify4_2026_09_28.py` | 1484 | `7eaeb9b4ba48` | `$I070SD2.py` | `$R070SD2.py` | 28 | 是 | 是 | **通过** |
| 109 | `_en_verify_2026_09_28.py` | 6071 | `51d9410d459b` | `$IRHXHR4.py` | `$RRHXHR4.py` | 28 | 是 | 是 | **通过** |
| 110 | `_execswitch_verify_2026_09_28.py` | 3501 | `0814f3c2d7ab` | `$IRYC4W1.py` | `$RRYC4W1.py` | 28 | 是 | 是 | **通过** |
| 111 | `_final_check.py` | 1562 | `ee7f008d36cb` | `$IP6DDWP.py` | `$RP6DDWP.py` | 28 | 是 | 是 | **通过** |
| 112 | `_final_sha.py` | 1435 | `8ea91ad82b9d` | `$IUEDFDD.py` | `$RUEDFDD.py` | 28 | 是 | 是 | **通过** |
| 113 | `_final_verify.py` | 2457 | `88aad6650405` | `$ILNR858.py` | `$RLNR858.py` | 28 | 是 | 是 | **通过** |
| 114 | `_ge01_g7_register_build.py` | 33147 | `7731337a516d` | `$IR113EY.py` | `$RR113EY.py` | 28 | 是 | 是 | **通过** |
| 115 | `_ge01_g7_register_measure.py` | 5090 | `5c3454c88a92` | `$IBQKGWK.py` | `$RBQKGWK.py` | 28 | 是 | 是 | **通过** |
| 116 | `_gh_tree.txt` | 341814 | `823cfbb23a03` | `$IIXJYMH.txt` | `$RIXJYMH.txt` | 28 | 是 | 是 | **通过** |
| 117 | `_h_census_worker.json` | 10037568 | `22531e8519b2` | `$ILV4NBZ.json` | `$RLV4NBZ.json` | 28 | 是 | 是 | **通过** |
| 118 | `_h_census_worker.py` | 5639 | `7f858d86f865` | `$IPOGZ5D.py` | `$RPOGZ5D.py` | 28 | 是 | 是 | **通过** |
| 119 | `_hash21.py` | 944 | `0d5335f0ac54` | `$I24SKMD.py` | `$R24SKMD.py` | 28 | 是 | 是 | **通过** |
| 120 | `_inspect_10cells.py` | 2460 | `919f8f4e8ad2` | `$I9MI24F.py` | `$R9MI24F.py` | 28 | 是 | 是 | **通过** |
| 121 | `_inspect_batch4_rounds.py` | 898 | `bf479a2667df` | `$IEKWYIZ.py` | `$REKWYIZ.py` | 28 | 是 | 是 | **通过** |
| 122 | `_intake_cards_35_48_extract.py` | 3416 | `74cca5bda270` | `$IN5EQS5.py` | `$RN5EQS5.py` | 28 | 是 | 是 | **通过** |
| 123 | `_iscp_dual_impl_2026_10_09.py` | 2974 | `8734f4326d5a` | `$IVA8463.py` | `$RVA8463.py` | 28 | 是 | 是 | **通过** |
| 124 | `_item35_v3_collinear_recompute_2026_10_01.py` | 16493 | `c8d859cbb69e` | `$IHYWR78.py` | `$RHYWR78.py` | 28 | 是 | 是 | **通过** |
| 125 | `_kd04_c_den_exec_2026_10_10.py` | 21430 | `419f9f691e63` | `$IO6LCNO.py` | `$RO6LCNO.py` | 28 | 是 | 是 | **通过** |
| 126 | `_kv3s43_diag_2026_10_09.py` | 614 | `398ebf6f33e0` | `$I6DH7H9.py` | `$R6DH7H9.py` | 28 | 是 | 是 | **通过** |
| 127 | `_lit_log.txt` | 8733 | `b062da7b654a` | `$I4KKN0E.txt` | `$R4KKN0E.txt` | 28 | 是 | 是 | **通过** |
| 128 | `_m5_k5_net.err` | 0 | `e3b0c44298fc` | `$I8B4HF5.err` | `$R8B4HF5.err` | 28 | 是 | 是 | **通过** |
| 129 | `_m5_k5_net.json` | 92060 | `9d7fe894a26b` | `$IRMQBFZ.json` | `$RRMQBFZ.json` | 28 | 是 | 是 | **通过** |
| 130 | `_m5_k5_net.py` | 3173 | `ec944f9178ea` | `$IJ9KZ2X.py` | `$RJ9KZ2X.py` | 28 | 是 | 是 | **通过** |
| 131 | `_m5_k5_net2.json` | 952252 | `b2bc158e7499` | `$IOZ2JO6.json` | `$ROZ2JO6.json` | 28 | 是 | 是 | **通过** |
| 132 | `_m5_k5_scan.err` | 0 | `e3b0c44298fc` | `$I8HNPGA.err` | `$R8HNPGA.err` | 28 | 是 | 是 | **通过** |
| 133 | `_m5_k5_scan.json` | 9530 | `ebf1ad76dc8a` | `$IQ608KR.json` | `$RQ608KR.json` | 28 | 是 | 是 | **通过** |
| 134 | `_m5_k5_scan.py` | 3541 | `f5245072750f` | `$I9RCJK5.py` | `$R9RCJK5.py` | 28 | 是 | 是 | **通过** |
| 135 | `_m5_reaudit_archive.py` | 1405 | `54540d871fb7` | `$IZUWC89.py` | `$RZUWC89.py` | 28 | 是 | 是 | **通过** |
| 136 | `_m5_reaudit_archive_out.json` | 654 | `e3542ccb4d3e` | `$IDFPK09.json` | `$RDFPK09.json` | 28 | 是 | 是 | **通过** |
| 137 | `_m5_reaudit_detail.py` | 2276 | `f43d192a9726` | `$IW6K7F1.py` | `$RW6K7F1.py` | 28 | 是 | 是 | **通过** |
| 138 | `_m5_reaudit_detail.txt` | 9214 | `8c117d51fc64` | `$I9KENAT.txt` | `$R9KENAT.txt` | 28 | 是 | 是 | **通过** |
| 139 | `_m5_reaudit_probe.py` | 4469 | `5b005dd13f95` | `$IW120YU.py` | `$RW120YU.py` | 28 | 是 | 是 | **通过** |
| 140 | `_mk_voided_reloc_register.py` | 13003 | `7c2d2f6955d0` | `$IIWG89U.py` | `$RIWG89U.py` | 28 | 是 | 是 | **通过** |
| 141 | `_n1_n2_check.py` | 1628 | `71f3f53a6eed` | `$IXRZ7RS.py` | `$RXRZ7RS.py` | 28 | 是 | 是 | **通过** |
| 142 | `_ofc_s1_inventory.json` | 216695 | `c2858312798b` | `$I6GC66J.json` | `$R6GC66J.json` | 28 | 是 | 是 | **通过** |
| 143 | `_ofc_s1b_inventory.json` | 336955 | `a28f35879008` | `$I3G4030.json` | `$R3G4030.json` | 28 | 是 | 是 | **通过** |
| 144 | `_patch21_emit.py` | 17106 | `1d3c8aea6bad` | `$IZHEPHW.py` | `$RZHEPHW.py` | 28 | 是 | 是 | **通过** |
| 145 | `_patch21_make.py` | 8807 | `b6cfdfaf80fa` | `$ITZW70I.py` | `$RTZW70I.py` | 28 | 是 | 是 | **通过** |
| 146 | `_patch21_run.py` | 3866 | `6333d9256716` | `$IV5ML86.py` | `$RV5ML86.py` | 28 | 是 | 是 | **通过** |
| 147 | `_pc.py` | 431 | `7c59c7e80d50` | `$I5IK1XB.py` | `$R5IK1XB.py` | 28 | 是 | 是 | **通过** |
| 148 | `_pk_probe.py` | 398 | `6d79ba939526` | `$I0LZFWR.py` | `$R0LZFWR.py` | 28 | 是 | 是 | **通过** |
| 149 | `_pk_sha_scan.py` | 599 | `df460eaec619` | `$IZLM2UQ.py` | `$RZLM2UQ.py` | 28 | 是 | 是 | **通过** |
| 150 | `_pkf34_f3.py` | 3068 | `389b3fdecd29` | `$IQAMM53.py` | `$RQAMM53.py` | 28 | 是 | 是 | **通过** |
| 151 | `_pkf34_f34.py` | 4282 | `a972a0383cf4` | `$IL115C5.py` | `$RL115C5.py` | 28 | 是 | 是 | **通过** |
| 152 | `_pkf34_f3b.py` | 2703 | `e1bcbf3897d8` | `$I57L223.py` | `$R57L223.py` | 28 | 是 | 是 | **通过** |
| 153 | `_pkf34_f4.py` | 3958 | `880a69b9cf29` | `$IC36JJ3.py` | `$RC36JJ3.py` | 28 | 是 | 是 | **通过** |
| 154 | `_pkf34_f4b.py` | 4401 | `e97f6ee41bec` | `$IBROOKS.py` | `$RBROOKS.py` | 28 | 是 | 是 | **通过** |
| 155 | `_pkf34_f4c.py` | 3045 | `c758efa2a529` | `$IH3OGFJ.py` | `$RH3OGFJ.py` | 28 | 是 | 是 | **通过** |
| 156 | `_pkf34_f4d.py` | 3686 | `fb565a667edc` | `$IT4WV1Z.py` | `$RT4WV1Z.py` | 28 | 是 | 是 | **通过** |
| 157 | `_pkf34_final.py` | 5903 | `4b6140aaa618` | `$IA85C5O.py` | `$RA85C5O.py` | 28 | 是 | 是 | **通过** |
| 158 | `_pkf34_nd.py` | 2537 | `527883f7ebb8` | `$IK47PX9.py` | `$RK47PX9.py` | 28 | 是 | 是 | **通过** |
| 159 | `_pkf34_v12.py` | 5639 | `c650b0c20eee` | `$IW2J4SJ.py` | `$RW2J4SJ.py` | 28 | 是 | 是 | **通过** |
| 160 | `_postcheck_v16_alt.py` | 1282 | `4d485d7a4d91` | `$IW57YPU.py` | `$RW57YPU.py` | 28 | 是 | 是 | **通过** |
| 161 | `_postcheck_v16_alt_stdout.txt` | 1558 | `f116b23fa967` | `$IQAN121.txt` | `$RQAN121.txt` | 28 | 是 | 是 | **通过** |
| 162 | `_postcheck_v16_sha.py` | 1391 | `46759ba2b8e5` | `$IIEJ7BN.py` | `$RIEJ7BN.py` | 28 | 是 | 是 | **通过** |
| 163 | `_pre_mod\exp_harness_pre.py` | 36217 | `d5c8d676bb5b` | `$IF9EW4M.py` | `$RF9EW4M.py` | 28 | 是 | 是 | **通过** |
| 164 | `_precheck_v15_tail.ps1` | 505 | `e94d8011bbf4` | `$IP7BO7W.ps1` | `$RP7BO7W.ps1` | 28 | 是 | 是 | **通过** |
| 165 | `_probe21.py` | 564 | `5a40370032b3` | `$I59IQYR.py` | `$R59IQYR.py` | 28 | 是 | 是 | **通过** |
| 166 | `_r10.py` | 1525 | `1b012cd12a00` | `$II0AB9D.py` | `$RI0AB9D.py` | 28 | 是 | 是 | **通过** |
| 167 | `_r1_alarm_test.py` | 2297 | `c44a09297f1a` | `$IKEHJR4.py` | `$RKEHJR4.py` | 28 | 是 | 是 | **通过** |
| 168 | `_r2_body.md` | 63091 | `1dbe20a3ba1c` | `$IPQ4HIE.md` | `$RPQ4HIE.md` | 28 | 是 | 是 | **通过** |
| 169 | `_r3_header_fix_2026_09_28.py` | 3280 | `6f8cec0fe006` | `$ILD7AUZ.py` | `$RLD7AUZ.py` | 28 | 是 | 是 | **通过** |
| 170 | `_r3_verify_2026_09_28.py` | 5494 | `721e52f9d55f` | `$IV5CFL2.py` | `$RV5CFL2.py` | 28 | 是 | 是 | **通过** |
| 171 | `_r4_cleanup_worker_keycount_2026_09_29.py` | 1909 | `ca0cbafed00b` | `$I5IM8BA.py` | `$R5IM8BA.py` | 28 | 是 | 是 | **通过** |
| 172 | `_r4_cleanup_worker_keyscan_2026_09_29.py` | 3561 | `01e1ac2ef239` | `$IZM7P1F.py` | `$RZM7P1F.py` | 28 | 是 | 是 | **通过** |
| 173 | `_r4_cleanup_worker_nearmiss_2026_09_29.py` | 1382 | `22336cc16500` | `$IFLD465.py` | `$RFLD465.py` | 28 | 是 | 是 | **通过** |
| 174 | `_r4_cleanup_worker_scan_2026_09_29.py` | 2411 | `af404c489392` | `$IYXCF7R.py` | `$RYXCF7R.py` | 28 | 是 | 是 | **通过** |
| 175 | `_r4_cleanup_worker_shape_2026_09_29.py` | 1110 | `f7f6313edce8` | `$IG4C2FD.py` | `$RG4C2FD.py` | 28 | 是 | 是 | **通过** |
| 176 | `_r4_key_scan_2026_09_24.py` | 3743 | `c782d1a18092` | `$IF92SDC.py` | `$RF92SDC.py` | 28 | 是 | 是 | **通过** |
| 177 | `_r4_key_scan_r1_files_2026_09_27.py` | 4079 | `cec4c1f3ff9c` | `$IPYB8H4.py` | `$RPYB8H4.py` | 28 | 是 | 是 | **通过** |
| 178 | `_r5_write_register_2026_10_13.py` | 25902 | `139c8a7316db` | `$I3LKQYL.py` | `$R3LKQYL.py` | 28 | 是 | 是 | **通过** |
| 179 | `_r6_evidence.py` | 2525 | `4de12a4f441b` | `$I4DL07S.py` | `$R4DL07S.py` | 28 | 是 | 是 | **通过** |
| 180 | `_recheck_r1_run1.log` | 2486 | `80b338a0e9ad` | `$IX53SH0.log` | `$RX53SH0.log` | 28 | 是 | 是 | **通过** |
| 181 | `_recheck_r1_runA.log` | 2634 | `68c85cf076d1` | `$IQRUNDF.log` | `$RQRUNDF.log` | 28 | 是 | 是 | **通过** |
| 182 | `_recheck_r1_runB.log` | 2634 | `68c85cf076d1` | `$IGLJDY8.log` | `$RGLJDY8.log` | 28 | 是 | 是 | **通过** |
| 183 | `_recheck_r1_runC.log` | 2568 | `b15384cff9f0` | `$IRLO398.log` | `$RRLO398.log` | 28 | 是 | 是 | **通过** |
| 184 | `_recheck_r1_runD.log` | 2568 | `b15384cff9f0` | `$IZ1XNSS.log` | `$RZ1XNSS.log` | 28 | 是 | 是 | **通过** |
| 185 | `_rj5_convention_check_2026_09_27.out.json` | 8983 | `c88e4ba1a4ce` | `$ICTNEH9.json` | `$RCTNEH9.json` | 28 | 是 | 是 | **通过** |
| 186 | `_rj5_convention_check_2026_09_27.py` | 8018 | `5dbb93b3c5e5` | `$IR1IQ42.py` | `$RR1IQ42.py` | 28 | 是 | 是 | **通过** |
| 187 | `_rj5_mapping_test_2026_09_27.py` | 5968 | `75ff70d87bd7` | `$INFXILR.py` | `$RNFXILR.py` | 28 | 是 | 是 | **通过** |
| 188 | `_rp4_fields.py` | 433 | `1d112ab8f3b4` | `$IET02KT.py` | `$RET02KT.py` | 28 | 是 | 是 | **通过** |
| 189 | `_rp_addendum_build_2026_10_09.py` | 30375 | `c4e8b75d656b` | `$IXTC7WT.py` | `$RXTC7WT.py` | 28 | 是 | 是 | **通过** |
| 190 | `_rp_verify_2026_10_09.py` | 3282 | `e0adae15fc26` | `$IE95307.py` | `$RE95307.py` | 28 | 是 | 是 | **通过** |
| 191 | `_rpd_neighbors_2026_10_09.py` | 1286 | `28cfa9466ea3` | `$ICWRSP8.py` | `$RCWRSP8.py` | 28 | 是 | 是 | **通过** |
| 192 | `_rpd_reuse_strict_2026_10_09.py` | 4746 | `4557b47b7361` | `$I98L2PA.py` | `$R98L2PA.py` | 28 | 是 | 是 | **通过** |
| 193 | `_rpd_verify_landed_2026_10_09.py` | 6335 | `912a2b8066f1` | `$I1Y54Z0.py` | `$R1Y54Z0.py` | 28 | 是 | 是 | **通过** |
| 194 | `_run2.py` | 4366 | `8acbf24342d1` | `$IW5XHVY.py` | `$RW5XHVY.py` | 28 | 是 | 是 | **通过** |
| 195 | `_run_d4_relabel_addendum.py` | 17550 | `620eabf853af` | `$IULRFK3.py` | `$RULRFK3.py` | 28 | 是 | 是 | **通过** |
| 196 | `_run_d6_addendum_2026_09_28.py` | 23204 | `e472ea36ed08` | `$I1E1JCV.py` | `$R1E1JCV.py` | 28 | 是 | 是 | **通过** |
| 197 | `_run_d6b_addendum_2026_09_28.py` | 31468 | `f0a4e919eeaa` | `$I8BRDX4.py` | `$R8BRDX4.py` | 28 | 是 | 是 | **通过** |
| 198 | `_run_d8_addendum_2026_09_30.py` | 107959 | `7ce330b3e5ae` | `$IMODE4D.py` | `$RMODE4D.py` | 28 | 是 | 是 | **通过** |
| 199 | `_run_d8_bhalf_addendum_2026_09_30.py` | 40576 | `90fa2c443529` | `$I65ZX25.py` | `$R65ZX25.py` | 28 | 是 | 是 | **通过** |
| 200 | `_run_day_inventory_table_2026_09_27.py` | 2763 | `329bf2b66422` | `$I9AJO2O.py` | `$R9AJO2O.py` | 28 | 是 | 是 | **通过** |
| 201 | `_run_final.py` | 26654 | `75d466add5d5` | `$IUJ7GWG.py` | `$RUJ7GWG.py` | 28 | 是 | 是 | **通过** |
| 202 | `_run_final_selfscan_2026_09_27.py` | 1358 | `cf5c5c7684bb` | `$IM0K9LM.py` | `$RM0K9LM.py` | 28 | 是 | 是 | **通过** |
| 203 | `_run_frozen_0touch_verify_2026_09_27.py` | 2309 | `48246f41e7d3` | `$ISKKE6T.py` | `$RSKKE6T.py` | 28 | 是 | 是 | **通过** |
| 204 | `_run_recheck_r1.py` | 34895 | `a76ec3a2340e` | `$IVSHP79.py` | `$RVSHP79.py` | 28 | 是 | 是 | **通过** |
| 205 | `_run_result_v3.py` | 3304 | `83cd4414f404` | `$I4J035X.py` | `$R4J035X.py` | 28 | 是 | 是 | **通过** |
| 206 | `_run_v3r1_relabel.py` | 30875 | `55d06ce42b3d` | `$IL4E87Y.py` | `$RL4E87Y.py` | 28 | 是 | 是 | **通过** |
| 207 | `_s3_f1_loader_fix_recompute_2026_10_08.py` | 21231 | `e39e4ae7d6ed` | `$IGG9S54.py` | `$RGG9S54.py` | 28 | 是 | 是 | **通过** |
| 208 | `_s4_freeze_count_crosscheck2_2026_10_09.py` | 3920 | `15fa4d155fc9` | `$IXYDKKJ.py` | `$RXYDKKJ.py` | 28 | 是 | 是 | **通过** |
| 209 | `_s4_freeze_count_crosscheck3_2026_10_09.py` | 4041 | `ee420dfd57e6` | `$I5HRVHY.py` | `$R5HRVHY.py` | 28 | 是 | 是 | **通过** |
| 210 | `_s4_freeze_count_crosscheck_2026_10_09.py` | 3463 | `856e6ab48dae` | `$IU47P06.py` | `$RU47P06.py` | 28 | 是 | 是 | **通过** |
| 211 | `_s4_seedprime_seq_t1_supplement_2026_10_11.py` | 31705 | `3a9db2126e4f` | `$IF083JC.py` | `$RF083JC.py` | 28 | 是 | 是 | **通过** |
| 212 | `_s4_topup_addendum_builder_2026_10_09.py` | 21122 | `b9987c7a8d5f` | `$IAW748W.py` | `$RAW748W.py` | 28 | 是 | 是 | **通过** |
| 213 | `_s4_tree_construct_exec_2026_10_10.py` | 34265 | `4cbd10b61aae` | `$IJYAITN.py` | `$RJYAITN.py` | 28 | 是 | 是 | **通过** |
| 214 | `_s4f2_dbg.py` | 431 | `5159c9c30180` | `$IHSJIG6.py` | `$RHSJIG6.py` | 28 | 是 | 是 | **通过** |
| 215 | `_s4f2_face_probe_2026_10_09.py` | 14896 | `62e04248d122` | `$IGRGMZU.py` | `$RGRGMZU.py` | 28 | 是 | 是 | **通过** |
| 216 | `_s4f2_patch.py` | 2740 | `b79a7073099d` | `$ILF4TR0.py` | `$RLF4TR0.py` | 28 | 是 | 是 | **通过** |
| 217 | `_s4f2_patch2.py` | 421 | `045bd90b237a` | `$I9J1CUE.py` | `$R9J1CUE.py` | 28 | 是 | 是 | **通过** |
| 218 | `_s4f2_patch3.py` | 815 | `6d57ff4ce76c` | `$IJ8ZR6H.py` | `$RJ8ZR6H.py` | 28 | 是 | 是 | **通过** |
| 219 | `_s4f2_patch4.py` | 565 | `7d85756a841d` | `$IZ8FHQW.py` | `$RZ8FHQW.py` | 28 | 是 | 是 | **通过** |
| 220 | `_s4f2_scanner_selftest.py` | 1819 | `5b6fd262f785` | `$ILIRR8E.py` | `$RLIRR8E.py` | 28 | 是 | 是 | **通过** |
| 221 | `_s4fs_auxdate_2026_10_09.py` | 1877 | `637e936d8bc7` | `$I2JMUSU.py` | `$R2JMUSU.py` | 28 | 是 | 是 | **通过** |
| 222 | `_s4fs_selfreport_2026_10_09.py` | 432 | `485071c7dd5e` | `$IHEJ3CV.py` | `$RHEJ3CV.py` | 28 | 是 | 是 | **通过** |
| 223 | `_s4fs_yitable_2026_10_09.py` | 1634 | `2bf7fd0ef5dc` | `$IJ92NTD.py` | `$RJ92NTD.py` | 28 | 是 | 是 | **通过** |
| 224 | `_s4oq_addendum_struct_2026_10_09.py` | 843 | `67652acdf681` | `$I0E4DYJ.py` | `$R0E4DYJ.py` | 28 | 是 | 是 | **通过** |
| 225 | `_s4oq_build_baseline_2026_10_09.py` | 3501 | `3cf28fe89611` | `$I0Q64VE.py` | `$R0Q64VE.py` | 28 | 是 | 是 | **通过** |
| 226 | `_s4oq_build_draft_2026_10_09.py` | 8719 | `0797d19dcaf3` | `$IGPUZRE.py` | `$RGPUZRE.py` | 28 | 是 | 是 | **通过** |
| 227 | `_s4oq_cellmap_2026_10_09.py` | 1734 | `c07589f292e1` | `$ICMD88W.py` | `$RCMD88W.py` | 28 | 是 | 是 | **通过** |
| 228 | `_s4oq_final_verify_2026_10_09.py` | 959 | `944a4f7006c8` | `$IHQU20S.py` | `$RHQU20S.py` | 28 | 是 | 是 | **通过** |
| 229 | `_s4oq_forward_2026_10_09.py` | 3482 | `43e72c62587d` | `$IZGNQ4H.py` | `$RZGNQ4H.py` | 28 | 是 | 是 | **通过** |
| 230 | `_s4oq_grid_cmp_2026_10_09.py` | 1601 | `f00865587d6a` | `$IJIOV6L.py` | `$RJIOV6L.py` | 28 | 是 | 是 | **通过** |
| 231 | `_s4oq_grid_diag_2026_10_09.py` | 1553 | `082e8b8b7bc4` | `$IJ2G0WL.py` | `$RJ2G0WL.py` | 28 | 是 | 是 | **通过** |
| 232 | `_s4oq_grid_recompute_2026_10_09.py` | 2394 | `afb613f5ced1` | `$ISZWAQV.py` | `$RSZWAQV.py` | 28 | 是 | 是 | **通过** |
| 233 | `_s4oq_keyscan_2026_10_09.py` | 573 | `c9f94c812f7f` | `$IUYR60O.py` | `$RUYR60O.py` | 28 | 是 | 是 | **通过** |
| 234 | `_s4oq_recompute_2026_10_09.py` | 3202 | `07cdec653345` | `$IS5150V.py` | `$RS5150V.py` | 28 | 是 | 是 | **通过** |
| 235 | `_s4oq_reuse_check_2026_10_09.py` | 6712 | `952c76c5b103` | `$IKE2NUW.py` | `$RKE2NUW.py` | 28 | 是 | 是 | **通过** |
| 236 | `_s4oq_reuse_v2_2026_10_09.py` | 6293 | `bc0f200edd1e` | `$IFA7HXK.py` | `$RFA7HXK.py` | 28 | 是 | 是 | **通过** |
| 237 | `_s4oq_skel_2026_10_09.py` | 466 | `73fc780b4849` | `$IW9BSER.py` | `$RW9BSER.py` | 28 | 是 | 是 | **通过** |
| 238 | `_s4oq_slug_opt_2026_10_09.py` | 4636 | `77d696b1690d` | `$I6OUUXV.py` | `$R6OUUXV.py` | 28 | 是 | 是 | **通过** |
| 239 | `_s4oq_slug_search2_2026_10_09.py` | 5258 | `fe6f7044ec4e` | `$I6BE44S.py` | `$R6BE44S.py` | 28 | 是 | 是 | **通过** |
| 240 | `_s4oq_variants_2026_10_09.py` | 1233 | `ccbbb499e19a` | `$IHFWL7H.py` | `$RHFWL7H.py` | 28 | 是 | 是 | **通过** |
| 241 | `_s4oq_verify_addendum_2026_10_09.py` | 2252 | `419c15a7a2c5` | `$I0YFAPK.py` | `$R0YFAPK.py` | 28 | 是 | 是 | **通过** |
| 242 | `_s4oq_write_addendum_2026_10_09.py` | 11886 | `63e61afa6517` | `$IZHHRBC.py` | `$RZHHRBC.py` | 28 | 是 | 是 | **通过** |
| 243 | `_s4td_cell_map_2026_10_09.py` | 3642 | `6665669d858d` | `$IM1SXP8.py` | `$RM1SXP8.py` | 28 | 是 | 是 | **通过** |
| 244 | `_s4td_floor_bound_2026_10_09.py` | 4378 | `ad95b6d5e9b9` | `$I5P8VE0.py` | `$R5P8VE0.py` | 28 | 是 | 是 | **通过** |
| 245 | `_s4td_reuse_and_bound_2026_10_09.py` | 8765 | `af6fdc892f60` | `$I4JUMD7.py` | `$R4JUMD7.py` | 28 | 是 | 是 | **通过** |
| 246 | `_s4td_slug_search_2026_10_09.py` | 4657 | `ce5529ec7516` | `$IMQ9F0W.py` | `$RMQ9F0W.py` | 28 | 是 | 是 | **通过** |
| 247 | `_s5dp_five_lines_runner_third_2026_10_11.py` | 31138 | `9de3c08e3863` | `$IWHKWY3.py` | `$RWHKWY3.py` | 28 | 是 | 是 | **通过** |
| 248 | `_sensitivity.py` | 5954 | `8aacafa48f9c` | `$IS2469B.py` | `$RS2469B.py` | 28 | 是 | 是 | **通过** |
| 249 | `_sha12_check.ps1` | 697 | `a4bfec107a77` | `$ICGZPTP.ps1` | `$RCGZPTP.ps1` | 28 | 是 | 是 | **通过** |
| 250 | `_sha12_check2.ps1` | 691 | `3e9174fb1e03` | `$IU9A4F4.ps1` | `$RU9A4F4.ps1` | 28 | 是 | 是 | **通过** |
| 251 | `_t15_inspect.py` | 2728 | `9877c9536e33` | `$I1K7OEX.py` | `$R1K7OEX.py` | 28 | 是 | 是 | **通过** |
| 252 | `_t15_inspect2.py` | 1942 | `9a6b5bb328aa` | `$II5OCB4.py` | `$RI5OCB4.py` | 28 | 是 | 是 | **通过** |
| 253 | `_t15_inspect3.py` | 1890 | `d423ca72cb3c` | `$IZC06DD.py` | `$RZC06DD.py` | 28 | 是 | 是 | **通过** |
| 254 | `_t15_inspect4.py` | 2756 | `069b7562f463` | `$I57WSY0.py` | `$R57WSY0.py` | 28 | 是 | 是 | **通过** |
| 255 | `_t15_inspect5.py` | 2712 | `977753c193d2` | `$I2T3MZU.py` | `$R2T3MZU.py` | 28 | 是 | 是 | **通过** |
| 256 | `_t15_inspect6.py` | 1234 | `eba3a29f6264` | `$I2XXNVE.py` | `$R2XXNVE.py` | 28 | 是 | 是 | **通过** |
| 257 | `_t15_inspect7.py` | 3880 | `78dafdf124f7` | `$IJYVRNA.py` | `$RJYVRNA.py` | 28 | 是 | 是 | **通过** |
| 258 | `_t15_percell.py` | 596 | `c035476cfb41` | `$IZ07EHF.py` | `$RZ07EHF.py` | 28 | 是 | 是 | **通过** |
| 259 | `_t15_probe_log.json` | 718 | `94444963ff77` | `$IHDCR4R.json` | `$RHDCR4R.json` | 28 | 是 | 是 | **通过** |
| 260 | `_t15_records.json` | 96443 | `8014af0e2b79` | `$I7JZT06.json` | `$R7JZT06.json` | 28 | 是 | 是 | **通过** |
| 261 | `_t15_update_result.py` | 9226 | `ad66f242c6a1` | `$ISUZQUP.py` | `$RSUZQUP.py` | 28 | 是 | 是 | **通过** |
| 262 | `_t15r2_inspect.py` | 3730 | `c58dc90fd86a` | `$I9YROPY.py` | `$R9YROPY.py` | 28 | 是 | 是 | **通过** |
| 263 | `_t15r2_verify.py` | 6737 | `5267b4dee7dc` | `$IRVHMA6.py` | `$RRVHMA6.py` | 28 | 是 | 是 | **通过** |
| 264 | `_t1_exp2_c_driver_2026_10_09.py` | 2898 | `5d474b7ceada` | `$I9VOL4Q.py` | `$R9VOL4Q.py` | 28 | 是 | 是 | **通过** |
| 265 | `_t1_exp2_c_records.json` | 6277328 | `f53681c7569a` | `$IYTFQ8Z.json` | `$RYTFQ8Z.json` | 28 | 是 | 是 | **通过** |
| 266 | `_t1_exp2_calib_2026_10_09.json` | 611 | `de09d4ee3721` | `$IVDQ4B7.json` | `$RVDQ4B7.json` | 28 | 是 | 是 | **通过** |
| 267 | `_t1_exp2_d_readings.json` | 3991 | `2315f6823011` | `$IS5ZD8X.json` | `$RS5ZD8X.json` | 28 | 是 | 是 | **通过** |
| 268 | `_t1_exp2_d_records.json` | 488395 | `aadba0c4f952` | `$IXMC1L2.json` | `$RXMC1L2.json` | 28 | 是 | 是 | **通过** |
| 269 | `_t1_exp2_probe_log.json` | 760 | `c6478415e2bf` | `$IDKLMOW.json` | `$RDKLMOW.json` | 28 | 是 | 是 | **通过** |
| 270 | `_t1_exp2_selfcert.json` | 6780 | `d929eb9ae0b8` | `$I6VB7CC.json` | `$R6VB7CC.json` | 28 | 是 | 是 | **通过** |
| 271 | `_t1_gap_domain_sweep_2026_10_01.py` | 2502 | `74d1ed439442` | `$I7PZAB5.py` | `$R7PZAB5.py` | 28 | 是 | 是 | **通过** |
| 272 | `_t1_gap_implA_2026_10_01.py` | 4468 | `c5d1dc7badcd` | `$IRZ2XKP.py` | `$RRZ2XKP.py` | 28 | 是 | 是 | **通过** |
| 273 | `_t1_gap_implB_2026_10_01.ps1` | 5735 | `19aebfd44310` | `$I0TYI2L.ps1` | `$R0TYI2L.ps1` | 28 | 是 | 是 | **通过** |
| 274 | `_t1_gap_postwrite_verify_2026_10_01.py` | 5666 | `33b4108f14a1` | `$IQ9FRV3.py` | `$RQ9FRV3.py` | 28 | 是 | 是 | **通过** |
| 275 | `_t1_gap_snapshot_2026_10_01.py` | 2588 | `fd53258bd16f` | `$IKD4BBC.py` | `$RKD4BBC.py` | 28 | 是 | 是 | **通过** |
| 276 | `_t1_qwen_temp_sweep_decomposition.py` | 1981 | `97a6520c7105` | `$IM5KBK8.py` | `$RM5KBK8.py` | 28 | 是 | 是 | **通过** |
| 277 | `_t1_qwen_temp_sweep_dump_readings.py` | 1137 | `7e06567afc2a` | `$I22PVSA.py` | `$R22PVSA.py` | 28 | 是 | 是 | **通过** |
| 278 | `_t1_qwen_temp_sweep_probe_log.json` | 445 | `b5e4151af490` | `$IU8AZNO.json` | `$RU8AZNO.json` | 28 | 是 | 是 | **通过** |
| 279 | `_t1_qwen_temp_sweep_r2_probe_log.json` | 739 | `5182f6fdd9ef` | `$IW2K12S.json` | `$RW2K12S.json` | 28 | 是 | 是 | **通过** |
| 280 | `_t1_qwen_temp_sweep_r2_records.json` | 1795870 | `bb511e7b0baf` | `$IYOHZE0.json` | `$RYOHZE0.json` | 28 | 是 | 是 | **通过** |
| 281 | `_t1_qwen_temp_sweep_r2_selfcert.json` | 6353 | `124051b56295` | `$I0BCXXD.json` | `$R0BCXXD.json` | 28 | 是 | 是 | **通过** |
| 282 | `_t1_qwen_temp_sweep_readings.json` | 11013 | `e5e8f024e42e` | `$IO381ET.json` | `$RO381ET.json` | 28 | 是 | 是 | **通过** |
| 283 | `_t1_qwen_temp_sweep_records.json` | 96866 | `5b51af62c640` | `$IHYHW3N.json` | `$RHYHW3N.json` | 28 | 是 | 是 | **通过** |
| 284 | `_t1_qwen_temp_sweep_selfcert.json` | 3866 | `91c2505deef3` | `$IS0RXZC.json` | `$RS0RXZC.json` | 28 | 是 | 是 | **通过** |
| 285 | `_t1_r2_calib_max_tokens_2026_10_09.json` | 3305 | `3f35aede29f6` | `$I4NNF35.json` | `$R4NNF35.json` | 28 | 是 | 是 | **通过** |
| 286 | `_t1_r2_calib_max_tokens_2026_10_09.py` | 6120 | `7bbb0de0c00f` | `$IL91HLZ.py` | `$RL91HLZ.py` | 28 | 是 | 是 | **通过** |
| 287 | `_t1_r2_run_driver_2026_10_09.py` | 2749 | `b71f4916bee1` | `$IK7X2U6.py` | `$RK7X2U6.py` | 28 | 是 | 是 | **通过** |
| 288 | `_t1_r2_verify_2026_10_09.py` | 4018 | `3ce6d45cfbf7` | `$IO8ICB3.py` | `$RO8ICB3.py` | 28 | 是 | 是 | **通过** |
| 289 | `_t1_verdict_probe_readonly.txt` | 4655 | `0e2df9ca7ab2` | `$I1OWQF3.txt` | `$R1OWQF3.txt` | 28 | 是 | 是 | **通过** |
| 290 | `_t2_t3_lit_search.py` | 5695 | `0829d37e0cd8` | `$I5BMQ3M.py` | `$R5BMQ3M.py` | 28 | 是 | 是 | **通过** |
| 291 | `_t2_t3_lit_search2.py` | 4946 | `c0caa8ba29f1` | `$IPDZH1V.py` | `$RPDZH1V.py` | 28 | 是 | 是 | **通过** |
| 292 | `_t2_t3_lit_search2_out.json` | 29596 | `13ffff0d0b28` | `$I6M74Q7.json` | `$R6M74Q7.json` | 28 | 是 | 是 | **通过** |
| 293 | `_t2_t3_lit_search_out.json` | 26588 | `cc70fac3d81b` | `$I4EURGG.json` | `$R4EURGG.json` | 28 | 是 | 是 | **通过** |
| 294 | `_t2_t3_llm_probe.py` | 4544 | `5561f7af5662` | `$I3HJCN3.py` | `$R3HJCN3.py` | 28 | 是 | 是 | **通过** |
| 295 | `_t2_t3_llm_probe_out.json` | 5331 | `993477af77db` | `$IQ3Y8SR.json` | `$RQ3Y8SR.json` | 28 | 是 | 是 | **通过** |
| 296 | `_t2_t3_prex_a_route.py` | 10166 | `c25af5d2966b` | `$IOYMPRQ.py` | `$ROYMPRQ.py` | 28 | 是 | 是 | **通过** |
| 297 | `_t2_t3_prex_a_route2.py` | 5850 | `0c44afba463a` | `$I7NK2N3.py` | `$R7NK2N3.py` | 28 | 是 | 是 | **通过** |
| 298 | `_t2_t3_prex_a_route2_out.json` | 6949 | `63f37ba943c1` | `$IS5GYH7.json` | `$RS5GYH7.json` | 28 | 是 | 是 | **通过** |
| 299 | `_t2_t3_prex_a_route_out.json` | 22640 | `3cad087a69c3` | `$I3G48UE.json` | `$R3G48UE.json` | 28 | 是 | 是 | **通过** |
| 300 | `_tail3_atomic_landing_check_2026_09_29.py` | 2699 | `5c19cf8f29fb` | `$IZMI0XF.py` | `$RZMI0XF.py` | 28 | 是 | 是 | **通过** |
| 301 | `_tail3_atomic_make_2026_09_29.py` | 17272 | `94d57549533b` | `$IRFU4A3.py` | `$RRFU4A3.py` | 28 | 是 | 是 | **通过** |
| 302 | `_tail3_atomic_refs_2026_09_29.py` | 2636 | `4e8ea9bea948` | `$ITM0FVX.py` | `$RTM0FVX.py` | 28 | 是 | 是 | **通过** |
| 303 | `_tail3_atomic_verify_2026_09_29.py` | 21338 | `8d12c9c9cb2d` | `$IZ4QQA2.py` | `$RZ4QQA2.py` | 28 | 是 | 是 | **通过** |
| 304 | `_tail_only.py` | 436 | `cf3bbd24b401` | `$IV7RNUO.py` | `$RV7RNUO.py` | 28 | 是 | 是 | **通过** |
| 305 | `_trae_audit_part1.py` | 5510 | `ac67b341b56b` | `$IR3YEM4.py` | `$RR3YEM4.py` | 28 | 是 | 是 | **通过** |
| 306 | `_trae_audit_part2.py` | 3632 | `9faaa564c3bc` | `$ICNLM9K.py` | `$RCNLM9K.py` | 28 | 是 | 是 | **通过** |
| 307 | `_trae_audit_part3.py` | 8617 | `f4c994004311` | `$I8035XP.py` | `$R8035XP.py` | 28 | 是 | 是 | **通过** |
| 308 | `_trae_audit_part3b.py` | 7662 | `c1a9a6c3c17a` | `$IYRDK3S.py` | `$RYRDK3S.py` | 28 | 是 | 是 | **通过** |
| 309 | `_trae_audit_part4.py` | 7173 | `bc8d4721bf3b` | `$I84RFAC.py` | `$R84RFAC.py` | 28 | 是 | 是 | **通过** |
| 310 | `_v412_contrib.py` | 1040 | `1085411b4896` | `$IXLSM77.py` | `$RXLSM77.py` | 28 | 是 | 是 | **通过** |
| 311 | `_v412_material_scan.py` | 627 | `f3493907cbe2` | `$INI4Q9H.py` | `$RNI4Q9H.py` | 28 | 是 | 是 | **通过** |
| 312 | `_v412_unique_scan.py` | 1300 | `b2e381f09828` | `$IUJM11G.py` | `$RUJM11G.py` | 28 | 是 | 是 | **通过** |
| 313 | `_v5_c5_b_clause4_consistency_check.py` | 6528 | `56ad3329a3c7` | `$IUZ9ZVD.py` | `$RUZ9ZVD.py` | 28 | 是 | 是 | **通过** |
| 314 | `_v5_c5_b_fetch_raw_embeddings.py` | 9476 | `8e4f2ae63de3` | `$I1UHFMZ.py` | `$R1UHFMZ.py` | 28 | 是 | 是 | **通过** |
| 315 | `_v5_c5_b_fix_readings_2026_10_01.py` | 12014 | `191efa7fe0b6` | `$IPR9GYM.py` | `$RPR9GYM.py` | 28 | 是 | 是 | **通过** |
| 316 | `_v5_item21_anchor_driver.py` | 5401 | `cb14f672dd1e` | `$IYWOMRU.py` | `$RYWOMRU.py` | 28 | 是 | 是 | **通过** |
| 317 | `_v5_item21_patched_b1_semA_none_default.py` | 16768 | `ceb33de660fd` | `$IBD2WKF.py` | `$RBD2WKF.py` | 28 | 是 | 是 | **通过** |
| 318 | `_v5_item21_patched_b1_semB_none_skip.py` | 16829 | `be0208abaffa` | `$ITJ5HRA.py` | `$RTJ5HRA.py` | 28 | 是 | 是 | **通过** |
| 319 | `_v5_item21_patched_b2_semA_none_default.py` | 16036 | `801ee31e8bdc` | `$IRHJR4C.py` | `$RRHJR4C.py` | 28 | 是 | 是 | **通过** |
| 320 | `_v5_item21_patched_b2_semB_none_skip.py` | 16097 | `8293535673dc` | `$IK34LP5.py` | `$RK34LP5.py` | 28 | 是 | 是 | **通过** |
| 321 | `_v5_item21_patched_b3_semA_none_default.py` | 15778 | `9d8a4a875b62` | `$IJ2087Q.py` | `$RJ2087Q.py` | 28 | 是 | 是 | **通过** |
| 322 | `_v5_item21_patched_b3_semB_none_skip.py` | 15839 | `8df8e94724ff` | `$IDMY6RD.py` | `$RDMY6RD.py` | 28 | 是 | 是 | **通过** |
| 323 | `_v5_loadcorpus_verify_2026_09_29.py` | 8798 | `564e3575ab1d` | `$IRAFH6A.py` | `$RRAFH6A.py` | 28 | 是 | 是 | **通过** |
| 324 | `_v5_qwen_retry_candidates_20260929.py` | 1689 | `f42600827cc3` | `$IYCH6JM.py` | `$RYCH6JM.py` | 28 | 是 | 是 | **通过** |
| 325 | `_v5_qwen_retry_introspect_20260929.py` | 3149 | `117b64fc1d5b` | `$IVK1SMM.py` | `$RVK1SMM.py` | 28 | 是 | 是 | **通过** |
| 326 | `_verdict_keeper_sha_helper.ps1` | 679 | `bc11b03d3b84` | `$IBI0OW4.ps1` | `$RBI0OW4.ps1` | 28 | 是 | 是 | **通过** |
| 327 | `_verify_d8_addendum_2026_09_30.py` | 4900 | `28de8c99c054` | `$IUXPFHZ.py` | `$RUXPFHZ.py` | 28 | 是 | 是 | **通过** |
| 328 | `_verify_intake_supplement_6.py` | 3678 | `1fbb1bd1db6c` | `$IGAB19V.py` | `$RGAB19V.py` | 28 | 是 | 是 | **通过** |
| 329 | `_verify_r32_card_2026_10_10.py` | 631 | `61f99fc5fdb9` | `$I57D3OK.py` | `$R57D3OK.py` | 28 | 是 | 是 | **通过** |
| 330 | `_verify_tail.py` | 733 | `23198a6a0a9b` | `$IBYDKID.py` | `$RBYDKID.py` | 28 | 是 | 是 | **通过** |
| 331 | `_verify_two_pieces_2026_09_30.py` | 4739 | `509afa876df0` | `$I1HE0KZ.py` | `$R1HE0KZ.py` | 28 | 是 | 是 | **通过** |
| 332 | `_vk_pv02_recheck_a.py` | 4188 | `37d55bf0fba6` | `$IFDICH3.py` | `$RFDICH3.py` | 28 | 是 | 是 | **通过** |
| 333 | `_vk_pv02_recheck_b.py` | 1646 | `fe0f10e38bb3` | `$IDAKE8U.py` | `$RDAKE8U.py` | 28 | 是 | 是 | **通过** |
| 334 | `_vk_pv02_recheck_c.py` | 2397 | `7d35b715f8e2` | `$IR6G3TB.py` | `$RR6G3TB.py` | 28 | 是 | 是 | **通过** |
| 335 | `_vk_pv02_recheck_d.py` | 982 | `7ae7ed6bcd8a` | `$IGZIAV9.py` | `$RGZIAV9.py` | 28 | 是 | 是 | **通过** |
| 336 | `_vk_pv02_recheck_e.py` | 1742 | `d925e60c1d3c` | `$I9FHJZP.py` | `$R9FHJZP.py` | 28 | 是 | 是 | **通过** |
| 337 | `_vk_pv02_recheck_f.py` | 1522 | `c2e298ccebc6` | `$II7HCLY.py` | `$RI7HCLY.py` | 28 | 是 | 是 | **通过** |
| 338 | `_vk_pv02_recheck_g.py` | 2269 | `f237e1d2715f` | `$I9PJMBD.py` | `$R9PJMBD.py` | 28 | 是 | 是 | **通过** |
| 339 | `_vk_q.py` | 519 | `67364902116c` | `$I8JPL28.py` | `$R8JPL28.py` | 28 | 是 | 是 | **通过** |
| 340 | `_vk_q2.py` | 540 | `d5759d40dc43` | `$I84GJNH.py` | `$R84GJNH.py` | 28 | 是 | 是 | **通过** |
| 341 | `_vk_q3.py` | 612 | `a00cd309205f` | `$IEGHYA1.py` | `$REGHYA1.py` | 28 | 是 | 是 | **通过** |
| 342 | `_vk_q4.py` | 784 | `defc3c53b7df` | `$IXC4NNE.py` | `$RXC4NNE.py` | 28 | 是 | 是 | **通过** |
| 343 | `_vk_q5.py` | 1246 | `7b95307225ba` | `$IVFYPC5.py` | `$RVFYPC5.py` | 28 | 是 | 是 | **通过** |
| 344 | `_vk_q6.py` | 811 | `7da34dd24eb0` | `$I7MUPFW.py` | `$R7MUPFW.py` | 28 | 是 | 是 | **通过** |
| 345 | `_vk_q7.py` | 1331 | `a6c525f88f11` | `$IPWNL2S.py` | `$RPWNL2S.py` | 28 | 是 | 是 | **通过** |
| 346 | `_vk_q8.py` | 1025 | `5a81e5558c72` | `$IS6V4CX.py` | `$RS6V4CX.py` | 28 | 是 | 是 | **通过** |
| 347 | `_vk_s4_topup_intake_recheck_2026_10_09.py` | 6678 | `a1d8047f1833` | `$I015C19.py` | `$R015C19.py` | 28 | 是 | 是 | **通过** |
| 348 | `_vk_s4_topup_intake_recheck_2026_10_09.txt` | 7098 | `683501b8fb41` | `$I5Z828R.txt` | `$R5Z828R.txt` | 28 | 是 | 是 | **通过** |
| 349 | `_w1_collect.py` | 19559 | `7c3155b2c370` | `$IYZ4AAI.py` | `$RYZ4AAI.py` | 28 | 是 | 是 | **通过** |
| 350 | `_w1_drift_write.py` | 16560 | `44e026ae190d` | `$IKX8K39.py` | `$RKX8K39.py` | 28 | 是 | 是 | **通过** |
| 351 | `_w1_freeze_write.py` | 24351 | `97211806b0d0` | `$IRXYYMI.py` | `$RRXYYMI.py` | 28 | 是 | 是 | **通过** |
| 352 | `_w1_phaseB_write.py` | 31303 | `4e85afe94966` | `$I2008MK.py` | `$R2008MK.py` | 28 | 是 | 是 | **通过** |
| 353 | `_w1_verify_final.py` | 7944 | `040c35e21bf2` | `$I5SR5YB.py` | `$R5SR5YB.py` | 28 | 是 | 是 | **通过** |
| 354 | `_w5_9model_merge_2026_10_09.py` | 18475 | `afa52e90f332` | `$IVHEZ7E.py` | `$RVHEZ7E.py` | 28 | 是 | 是 | **通过** |
| 355 | `_worker_write_ge01_unblock_progress.py` | 26125 | `7c18f854316c` | `$IZT6VOJ.py` | `$RZT6VOJ.py` | 28 | 是 | 是 | **通过** |
| 356 | `_write_canonical_register.py` | 24636 | `867acc46aff9` | `$IOAOGMG.py` | `$ROAOGMG.py` | 28 | 是 | 是 | **通过** |
| 357 | `_write_eps_grid_design.py` | 38246 | `df37b02f1c0f` | `$IAUAY4B.py` | `$RAUAY4B.py` | 28 | 是 | 是 | **通过** |
| 358 | `_write_predelete_caliber_draft.py` | 32826 | `82d7f9c628b6` | `$IF01LUE.py` | `$RF01LUE.py` | 28 | 是 | 是 | **通过** |
| 359 | `anch.py` | 1484 | `c05693efbb30` | `$I7JTPOH.py` | `$R7JTPOH.py` | 28 | 是 | 是 | **通过** |
| 360 | `anch_v4_build.py` | 7175 | `adcae459701a` | `$IA4UZN9.py` | `$RA4UZN9.py` | 28 | 是 | 是 | **通过** |
| 361 | `anch_v4_build_measurements.json` | 2315 | `5708226b943f` | `$IZ84BSD.json` | `$RZ84BSD.json` | 28 | 是 | 是 | **通过** |
| 362 | `anch_v4_probe.py` | 2662 | `f47af093e3aa` | `$IW6S21O.py` | `$RW6S21O.py` | 28 | 是 | 是 | **通过** |
| 363 | `archive_survey_census2.py` | 780 | `2863f5edca41` | `$ILH6LPA.py` | `$RLH6LPA.py` | 28 | 是 | 是 | **通过** |
| 364 | `body_relabel.md` | 8672 | `2660d5ea717d` | `$IEZ6TJ5.md` | `$REZ6TJ5.md` | 28 | 是 | 是 | **通过** |
| 365 | `body_v6_effect.md` | 15467 | `d79637fee0ef` | `$IYKF54F.md` | `$RYKF54F.md` | 28 | 是 | 是 | **通过** |
| 366 | `claude_spotcheck.py` | 4136 | `a78755b356b9` | `$I1S9FS1.py` | `$R1S9FS1.py` | 28 | 是 | 是 | **通过** |
| 367 | `cleanup511_manifest_2026_10_17.json` | 1754609 | `b7093a701856` | `$IXBGN3X.json` | `$RXBGN3X.json` | 28 | 是 | 是 | **通过** |
| 368 | `collision_survey_hashes.json` | 75439 | `0329afb1e9fc` | `$IGTV0ED.json` | `$RGTV0ED.json` | 28 | 是 | 是 | **通过** |
| 369 | `collision_survey_inventory.json` | 37588 | `a4cd5b2fc5c8` | `$I287ZVY.json` | `$R287ZVY.json` | 28 | 是 | 是 | **通过** |
| 370 | `combo_llm_calls_2026_10_16.jsonl` | 59626 | `86f05646031b` | `$IWXKSHD.jsonl` | `$RWXKSHD.jsonl` | 28 | 是 | 是 | **通过** |
| 371 | `combo_measurement_2026_10_16.json` | 121779 | `27609799e40e` | `$IIUW7T4.json` | `$RIUW7T4.json` | 28 | 是 | 是 | **通过** |
| 372 | `d05_hash_index.py` | 1004 | `070b6f865eba` | `$IRFL9PD.py` | `$RRFL9PD.py` | 28 | 是 | 是 | **通过** |
| 373 | `d1fill_anchor_snapshot.py` | 1985 | `15c0b0ade7ab` | `$IY90GZ3.py` | `$RY90GZ3.py` | 28 | 是 | 是 | **通过** |
| 374 | `d1fill_recount_checks.py` | 2336 | `b8af087b5e1f` | `$IWR3QJA.py` | `$RWR3QJA.py` | 28 | 是 | 是 | **通过** |
| 375 | `d1fill_recount_impl1.py` | 6464 | `bb30ad15c89b` | `$IOK77MH.py` | `$ROK77MH.py` | 28 | 是 | 是 | **通过** |
| 376 | `d1fill_recount_impl2.ps1` | 6132 | `88411408e671` | `$IMKFLJZ.ps1` | `$RMKFLJZ.ps1` | 28 | 是 | 是 | **通过** |
| 377 | `diag.py` | 972 | `db20dd0e6efb` | `$IRME98A.py` | `$RRME98A.py` | 28 | 是 | 是 | **通过** |
| 378 | `diffcause.py` | 2724 | `2b24513cdf74` | `$IOTCZLI.py` | `$ROTCZLI.py` | 28 | 是 | 是 | **通过** |
| 379 | `docwriter_c2_effect_census.json` | 36157 | `1ef99b1da14d` | `$IW7UYBD.json` | `$RW7UYBD.json` | 28 | 是 | 是 | **通过** |
| 380 | `docwriter_c2_effect_census.py` | 5518 | `a8e52d7e9f8d` | `$ILWBBQ8.py` | `$RLWBBQ8.py` | 28 | 是 | 是 | **通过** |
| 381 | `docwriter_c2_effect_table.py` | 1400 | `503230d1e7e3` | `$IUB55A6.py` | `$RUB55A6.py` | 28 | 是 | 是 | **通过** |
| 382 | `docwriter_c2_effect_table.txt` | 21554 | `1b5382cc9936` | `$IRZKKQR.txt` | `$RRZKKQR.txt` | 28 | 是 | 是 | **通过** |
| 383 | `docwriter_sigsup.py` | 13645 | `d116fefd336c` | `$IGR1ILZ.py` | `$RGR1ILZ.py` | 28 | 是 | 是 | **通过** |
| 384 | `docwriter_v41_probe.py` | 6503 | `210a07303fe7` | `$IYSVVA7.py` | `$RYSVVA7.py` | 28 | 是 | 是 | **通过** |
| 385 | `docwriter_v41_scan2.json` | 4066 | `e988b26ba229` | `$IQMXIOT.json` | `$RQMXIOT.json` | 28 | 是 | 是 | **通过** |
| 386 | `docwriter_v41_scan2.py` | 3661 | `e88316a0fc2c` | `$IYPRU3J.py` | `$RYPRU3J.py` | 28 | 是 | 是 | **通过** |
| 387 | `docwriter_v42_scan.py` | 4601 | `93d9c4c5c927` | `$I989J6L.py` | `$R989J6L.py` | 28 | 是 | 是 | **通过** |
| 388 | `docwriter_v42_scan_out.txt` | 5267 | `d1470a9eaea9` | `$I3F78AT.txt` | `$R3F78AT.txt` | 28 | 是 | 是 | **通过** |
| 389 | `docwriter_v42_verify.py` | 4858 | `47c794a64dff` | `$IJ3FOE0.py` | `$RJ3FOE0.py` | 28 | 是 | 是 | **通过** |
| 390 | `docwriter_v42_verify_out.txt` | 2899 | `c38b853adda1` | `$IU1YPC1.txt` | `$RU1YPC1.txt` | 28 | 是 | 是 | **通过** |
| 391 | `docwriter_v43_fp.py` | 1488 | `000c7e036d9c` | `$IFIVH35.py` | `$RFIVH35.py` | 28 | 是 | 是 | **通过** |
| 392 | `docwriter_v43_fp2.py` | 1716 | `87ef5d8aba15` | `$ICQTAV9.py` | `$RCQTAV9.py` | 28 | 是 | 是 | **通过** |
| 393 | `docwriter_v43_fp_out.txt` | 2420 | `35a223091bbe` | `$I4KQQM4.txt` | `$R4KQQM4.txt` | 28 | 是 | 是 | **通过** |
| 394 | `docwriter_v43_scan.py` | 2061 | `5356708d6a6f` | `$I40P4U2.py` | `$R40P4U2.py` | 28 | 是 | 是 | **通过** |
| 395 | `docwriter_v43_scan_out.txt` | 2353 | `c80e849e7c99` | `$I7WCO7N.txt` | `$R7WCO7N.txt` | 28 | 是 | 是 | **通过** |
| 396 | `docwriter_v43_verify.py` | 4497 | `2cf26203f12d` | `$IHB534L.py` | `$RHB534L.py` | 28 | 是 | 是 | **通过** |
| 397 | `docwriter_v43_verify_out.txt` | 759 | `c1d14e3d7e06` | `$IA0PXUK.txt` | `$RA0PXUK.txt` | 28 | 是 | 是 | **通过** |
| 398 | `docwriter_v44_fp.py` | 2485 | `4c2e2a4a2ad2` | `$IN3H57F.py` | `$RN3H57F.py` | 28 | 是 | 是 | **通过** |
| 399 | `docwriter_v44_fp_out.txt` | 1601 | `6ab1382d766e` | `$IVUWOOH.txt` | `$RVUWOOH.txt` | 28 | 是 | 是 | **通过** |
| 400 | `docwriter_v44_fresh.py` | 2319 | `855298e666f6` | `$I2D4VAB.py` | `$R2D4VAB.py` | 28 | 是 | 是 | **通过** |
| 401 | `docwriter_v44_fresh_out.txt` | 1646 | `6d7d8ad5c4ed` | `$IXLW0UJ.txt` | `$RXLW0UJ.txt` | 28 | 是 | 是 | **通过** |
| 402 | `docwriter_v44_scan.py` | 3822 | `3cc9fa3130a4` | `$IPSDQE3.py` | `$RPSDQE3.py` | 28 | 是 | 是 | **通过** |
| 403 | `docwriter_v44_scan_out.txt` | 2290 | `24663bc22391` | `$ICN6U3N.txt` | `$RCN6U3N.txt` | 28 | 是 | 是 | **通过** |
| 404 | `docwriter_v45_scan.py` | 5186 | `c6703629a7b0` | `$IYAY8NH.py` | `$RYAY8NH.py` | 28 | 是 | 是 | **通过** |
| 405 | `docwriter_v45_scan_out.txt` | 1661 | `28c06dd53ae4` | `$IGLA8C6.txt` | `$RGLA8C6.txt` | 28 | 是 | 是 | **通过** |
| 406 | `docwriter_v45_scan_out_r1.txt` | 1661 | `28c06dd53ae4` | `$IXDGM6N.txt` | `$RXDGM6N.txt` | 28 | 是 | 是 | **通过** |
| 407 | `docwriter_v45_scan_out_r2.txt` | 1728 | `ef49039e5d90` | `$IAR5JLM.txt` | `$RAR5JLM.txt` | 28 | 是 | 是 | **通过** |
| 408 | `docwriter_v45_scan_r2.py` | 4212 | `189764eebc91` | `$ITZMASX.py` | `$RTZMASX.py` | 28 | 是 | 是 | **通过** |
| 409 | `docwriter_v45_verify_out.txt` | 2031 | `e5a0fdfbc914` | `$IFYH2U2.txt` | `$RFYH2U2.txt` | 28 | 是 | 是 | **通过** |
| 410 | `docwriter_v46_card_raw.py` | 1652 | `b8754c12612b` | `$IWR0SPV.py` | `$RWR0SPV.py` | 28 | 是 | 是 | **通过** |
| 411 | `docwriter_v46_probe.py` | 8174 | `15d2a2cef38c` | `$IHE8G9I.py` | `$RHE8G9I.py` | 28 | 是 | 是 | **通过** |
| 412 | `docwriter_v46_probe_out.txt` | 10158 | `45358bad9e37` | `$IXI0UI4.txt` | `$RXI0UI4.txt` | 28 | 是 | 是 | **通过** |
| 413 | `docwriter_v46_timeshift_out.txt` | 708 | `4623d2f470da` | `$IN59HO3.txt` | `$RN59HO3.txt` | 28 | 是 | 是 | **通过** |
| 414 | `docwriter_v46_verify.py` | 6883 | `7d657b923cf3` | `$IKLE2R6.py` | `$RKLE2R6.py` | 28 | 是 | 是 | **通过** |
| 415 | `docwriter_v46_verify_r2.py` | 3940 | `98878b701653` | `$I3DBP6U.py` | `$R3DBP6U.py` | 28 | 是 | 是 | **通过** |
| 416 | `docwriter_v47_verify.py` | 1220 | `9383724baaa4` | `$ITZCUTU.py` | `$RTZCUTU.py` | 28 | 是 | 是 | **通过** |
| 417 | `docwriter_v47_write1.py` | 62466 | `8fa8d72c3a69` | `$I3JIWG6.py` | `$R3JIWG6.py` | 28 | 是 | 是 | **通过** |
| 418 | `docwriter_v47_write2.py` | 48627 | `1ee1ee14ac3e` | `$ITMFBY6.py` | `$RTMFBY6.py` | 28 | 是 | 是 | **通过** |
| 419 | `docwriter_v48_norm.py` | 12880 | `e39ea2ab2756` | `$I3G4I6Z.py` | `$R3G4I6Z.py` | 28 | 是 | 是 | **通过** |
| 420 | `docwriter_v48_probe.py` | 4448 | `8dfd0f40cdb5` | `$IPXV2V8.py` | `$RPXV2V8.py` | 28 | 是 | 是 | **通过** |
| 421 | `docwriter_v48_probe_out.txt` | 4169 | `48b1c4a81ad4` | `$IM96GW1.txt` | `$RM96GW1.txt` | 28 | 是 | 是 | **通过** |
| 422 | `docwriter_v49_norm.py` | 16740 | `d1b3481335eb` | `$IWHEO1M.py` | `$RWHEO1M.py` | 28 | 是 | 是 | **通过** |
| 423 | `docwriter_v49_probe.py` | 4806 | `753b0ad48557` | `$IR4175P.py` | `$RR4175P.py` | 28 | 是 | 是 | **通过** |
| 424 | `docwriter_v49_probe_out.txt` | 4353 | `c04bcaf87623` | `$IDNKPDH.txt` | `$RDNKPDH.txt` | 28 | 是 | 是 | **通过** |
| 425 | `docwriter_verify_v44.py` | 4692 | `19cfb64700a1` | `$IX9J4TZ.py` | `$RX9J4TZ.py` | 28 | 是 | 是 | **通过** |
| 426 | `docwriter_verify_v44_out.txt` | 2371 | `f3d33d095a8a` | `$II4WRI3.txt` | `$RI4WRI3.txt` | 28 | 是 | 是 | **通过** |
| 427 | `docwriter_verify_v45.py` | 3780 | `92230e228d83` | `$IO215UH.py` | `$RO215UH.py` | 28 | 是 | 是 | **通过** |
| 428 | `docwriter_write_effect_v43.py` | 27715 | `01098529c399` | `$IGKPP8H.py` | `$RGKPP8H.py` | 28 | 是 | 是 | **通过** |
| 429 | `docwriter_write_v42.py` | 66543 | `5cc438f6338d` | `$I9KESS4.py` | `$R9KESS4.py` | 28 | 是 | 是 | **通过** |
| 430 | `docwriter_write_v43.py` | 33607 | `d5e6390b900d` | `$IQUIPE3.py` | `$RQUIPE3.py` | 28 | 是 | 是 | **通过** |
| 431 | `docwriter_write_v44.py` | 84551 | `54812b76573b` | `$ITNZCQR.py` | `$RTNZCQR.py` | 28 | 是 | 是 | **通过** |
| 432 | `docwriter_write_v45.py` | 61168 | `af3a22741b2f` | `$IR2ZSTV.py` | `$RR2ZSTV.py` | 28 | 是 | 是 | **通过** |
| 433 | `dscan_01.json` | 195396 | `bab5d4a367af` | `$ICFG92Y.json` | `$RCFG92Y.json` | 28 | 是 | 是 | **通过** |
| 434 | `dscan_01.py` | 2865 | `a58735d65c3c` | `$I7ORAK3.py` | `$R7ORAK3.py` | 28 | 是 | 是 | **通过** |
| 435 | `dscan_02.py` | 5078 | `1f6ffd7e0f47` | `$IBTYK2I.py` | `$RBTYK2I.py` | 28 | 是 | 是 | **通过** |
| 436 | `dscan_03.py` | 5360 | `35711329ad8f` | `$I8X5LIW.py` | `$R8X5LIW.py` | 28 | 是 | 是 | **通过** |
| 437 | `dscan_04.py` | 2302 | `43e661f72888` | `$IT0AZ5A.py` | `$RT0AZ5A.py` | 28 | 是 | 是 | **通过** |
| 438 | `dscan_05.py` | 6207 | `966d9ce0df2d` | `$IXJFTY3.py` | `$RXJFTY3.py` | 28 | 是 | 是 | **通过** |
| 439 | `dscan_06.py` | 1845 | `7c059d996778` | `$INZC32Z.py` | `$RNZC32Z.py` | 28 | 是 | 是 | **通过** |
| 440 | `dscan_07.py` | 1074 | `26897ce01079` | `$ISZMWX6.py` | `$RSZMWX6.py` | 28 | 是 | 是 | **通过** |
| 441 | `dscan_08.py` | 2370 | `fc3c78d3f0e5` | `$IPAWB4V.py` | `$RPAWB4V.py` | 28 | 是 | 是 | **通过** |
| 442 | `dscan_classified.json` | 47129 | `458a2e06a2d3` | `$IWKB0YK.json` | `$RWKB0YK.json` | 28 | 是 | 是 | **通过** |
| 443 | `dscan_classified.txt` | 11199 | `2945d458f5a6` | `$I00M391.txt` | `$R00M391.txt` | 28 | 是 | 是 | **通过** |
| 444 | `dscan_copycmp.txt` | 687 | `3af905a1f5c4` | `$IY8JT2H.txt` | `$RY8JT2H.txt` | 28 | 是 | 是 | **通过** |
| 445 | `dscan_families.txt` | 3535 | `3bc5960fa2bf` | `$I92CFQP.txt` | `$R92CFQP.txt` | 28 | 是 | 是 | **通过** |
| 446 | `dscan_matrix.json` | 273930 | `875f08dd0648` | `$IULJXT6.json` | `$RULJXT6.json` | 28 | 是 | 是 | **通过** |
| 447 | `dscan_matrix.txt` | 1452 | `a8d3aa0287b6` | `$IY1NT8C.txt` | `$RY1NT8C.txt` | 28 | 是 | 是 | **通过** |
| 448 | `dscan_repo_dump.txt` | 24326 | `06d5da0d55ed` | `$IJH88QK.txt` | `$RJH88QK.txt` | 28 | 是 | 是 | **通过** |
| 449 | `dscan_stats.txt` | 2712 | `b35fb0ebd75d` | `$INWRXCT.txt` | `$RNWRXCT.txt` | 28 | 是 | 是 | **通过** |
| 450 | `dscan_sub_dump.txt` | 94170 | `8c3f99c0b128` | `$I3W9CAF.txt` | `$R3W9CAF.txt` | 28 | 是 | 是 | **通过** |
| 451 | `dscan_tables.md` | 56191 | `0a96d4720449` | `$IARWKWS.md` | `$RARWKWS.md` | 28 | 是 | 是 | **通过** |
| 452 | `dscan_write_01.py` | 23330 | `71cbf839d36b` | `$I68T4T3.py` | `$R68T4T3.py` | 28 | 是 | 是 | **通过** |
| 453 | `dscan_xcheck.txt` | 3196 | `57dcd8344683` | `$I975FKK.txt` | `$R975FKK.txt` | 28 | 是 | 是 | **通过** |
| 454 | `dw720_calc_2026_10_16.py` | 1797 | `5da6bf2d700a` | `$INKJG3W.py` | `$RNKJG3W.py` | 28 | 是 | 是 | **通过** |
| 455 | `dw720_probe_2026_10_16.py` | 1450 | `efdb4c877f3f` | `$IPQ44BM.py` | `$RPQ44BM.py` | 28 | 是 | 是 | **通过** |
| 456 | `dw720_verify_2026_10_16.py` | 3909 | `c90f9a64c3d8` | `$IWJ8983.py` | `$RWJ8983.py` | 28 | 是 | 是 | **通过** |
| 457 | `dw720_write_2026_10_16.py` | 29681 | `46e8be383b3c` | `$IK4XZJP.py` | `$RK4XZJP.py` | 28 | 是 | 是 | **通过** |
| 458 | `ea_build.py` | 30376 | `8048ac40151e` | `$IB2RNOI.py` | `$RB2RNOI.py` | 28 | 是 | 是 | **通过** |
| 459 | `ea_files.json` | 191599 | `48b76f2549f3` | `$IB2VRYN.json` | `$RB2VRYN.json` | 28 | 是 | 是 | **通过** |
| 460 | `ea_p2.py` | 1030 | `64fb6201dca9` | `$INKJSJZ.py` | `$RNKJSJZ.py` | 28 | 是 | 是 | **通过** |
| 461 | `ea_scan1.py` | 1005 | `e21c9fca13d0` | `$IQT4EKM.py` | `$RQT4EKM.py` | 28 | 是 | 是 | **通过** |
| 462 | `ea_sha12.json` | 289347 | `381dd57aaca4` | `$I2P1F55.json` | `$R2P1F55.json` | 28 | 是 | 是 | **通过** |
| 463 | `erratum_glm_wholepack_body.md` | 24905 | `0291002f749e` | `$IPH0DGG.md` | `$RPH0DGG.md` | 28 | 是 | 是 | **通过** |
| 464 | `evauditor_one_finish_write.py` | 46211 | `c24967f8114e` | `$I99YMMN.py` | `$R99YMMN.py` | 28 | 是 | 是 | **通过** |
| 465 | `exp04_h_contrast_2026_10_10.py` | 14333 | `572f1b9c3927` | `$IPG6S72.py` | `$RPG6S72.py` | 28 | 是 | 是 | **通过** |
| 466 | `f2_branch_fix_transform_2026_09_29.py` | 18152 | `0a970b156867` | `$IT16SZL.py` | `$RT16SZL.py` | 28 | 是 | 是 | **通过** |
| 467 | `f2_branch_selftest_2026_09_29.py` | 7377 | `68a927174a2e` | `$I79UXHA.py` | `$R79UXHA.py` | 28 | 是 | 是 | **通过** |
| 468 | `gate_check.py` | 648 | `abe7fbdb394b` | `$IPIRNQT.py` | `$RPIRNQT.py` | 28 | 是 | 是 | **通过** |
| 469 | `gate_check2.py` | 840 | `7025ceceb766` | `$IL8DDE4.py` | `$RL8DDE4.py` | 28 | 是 | 是 | **通过** |
| 470 | `ge01_eps_grid_exec2_2026_10_16.json` | 53903 | `af1fcc0e8852` | `$IQRH5KJ.json` | `$RQRH5KJ.json` | 28 | 是 | 是 | **通过** |
| 471 | `ge01_eps_grid_exec2_2026_10_16.py` | 11452 | `9ef16d1b8525` | `$IFIYTKT.py` | `$RFIYTKT.py` | 28 | 是 | 是 | **通过** |
| 472 | `ge01_eps_grid_exec3_2026_10_16.py` | 3580 | `5225d7800544` | `$IZBHFH6.py` | `$RZBHFH6.py` | 28 | 是 | 是 | **通过** |
| 473 | `ge01_eps_grid_exec_2026_10_16.json` | 62749 | `45b233594ee9` | `$I4C2HF9.json` | `$R4C2HF9.json` | 28 | 是 | 是 | **通过** |
| 474 | `ge01_eps_grid_exec_2026_10_16.py` | 11018 | `ab5e001cb63b` | `$ICS93CL.py` | `$RCS93CL.py` | 28 | 是 | 是 | **通过** |
| 475 | `ge01_eps_grid_verify_2026_10_16.py` | 3016 | `4ff9d5a95dcf` | `$ISO04TE.py` | `$RSO04TE.py` | 28 | 是 | 是 | **通过** |
| 476 | `ge01_full_1494_adjudicate_2026_10_16.py` | 14293 | `8108e4c883ad` | `$IU37RVR.py` | `$RU37RVR.py` | 28 | 是 | 是 | **通过** |
| 477 | `ge01_full_1494_collect_2026_10_16.py` | 28322 | `039ebfca39b7` | `$I6JFW84.py` | `$R6JFW84.py` | 28 | 是 | 是 | **通过** |
| 478 | `ge01_full_1494_exec_r1_write_2026_10_16.py` | 43129 | `9e9e402893ef` | `$IZ58UDQ.py` | `$RZ58UDQ.py` | 28 | 是 | 是 | **通过** |
| 479 | `ge01_full_1494_freeze_2026_10_16.json` | 7479 | `8494390a274a` | `$IH0I307.json` | `$RH0I307.json` | 28 | 是 | 是 | **通过** |
| 480 | `ge01_full_1494_freeze_write_2026_10_16.py` | 23781 | `b89e0432ab97` | `$I7RUKXO.py` | `$R7RUKXO.py` | 28 | 是 | 是 | **通过** |
| 481 | `ge01_full_1494_llm_calls_2026_10_16.jsonl` | 235298 | `e922d168ab60` | `$IU0VEF1.jsonl` | `$RU0VEF1.jsonl` | 28 | 是 | 是 | **通过** |
| 482 | `ge01_full_1494_measurement_2026_10_16.json` | 547703 | `4054d1393b84` | `$I7913RQ.json` | `$R7913RQ.json` | 28 | 是 | 是 | **通过** |
| 483 | `ge01_full_1494_measurement_resume32_2026_10_16.json` | 570852 | `7ccc5f9e8b2c` | `$IWKIXPK.json` | `$RWKIXPK.json` | 28 | 是 | 是 | **通过** |
| 484 | `ge01_full_1494_precheck_2026_10_16.json` | 9432 | `bd6dd07ad1c3` | `$IFBR1OD.json` | `$RFBR1OD.json` | 28 | 是 | 是 | **通过** |
| 485 | `ge01_full_1494_precheck_2026_10_16.py` | 10700 | `cc34ab8552f9` | `$ISBQZLN.py` | `$RSBQZLN.py` | 28 | 是 | 是 | **通过** |
| 486 | `ge01_full_1494_probe_2026_10_16.py` | 3199 | `a38499e4d4a9` | `$IIB5YYF.py` | `$RIB5YYF.py` | 28 | 是 | 是 | **通过** |
| 487 | `ge01_full_1494_readout_2026_10_16.py` | 22920 | `59ed27635c6e` | `$IZCWOLT.py` | `$RZCWOLT.py` | 28 | 是 | 是 | **通过** |
| 488 | `ge01_full_1494_resume32_collect_2026_10_16.py` | 14609 | `9496620e32b2` | `$I3IL581.py` | `$R3IL581.py` | 28 | 是 | 是 | **通过** |
| 489 | `ge01_full_1494_resume32_precheck_2026_10_16.log` | 1761 | `ada7f41b8cb2` | `$IXTZSJ9.log` | `$RXTZSJ9.log` | 28 | 是 | 是 | **通过** |
| 490 | `ge01_full_1494_resume32_precheck_2026_10_16.py` | 6122 | `463532446b61` | `$IUQODRS.py` | `$RUQODRS.py` | 28 | 是 | 是 | **通过** |
| 491 | `ge01_full_1494_resume32_probe_2026_10_16.json` | 338 | `579a7f8b6fe3` | `$IFX28M4.json` | `$RFX28M4.json` | 28 | 是 | 是 | **通过** |
| 492 | `ge01_full_1494_resume32_readout_2026_10_16.py` | 29430 | `de50589bd6c6` | `$IV0UBPN.py` | `$RV0UBPN.py` | 28 | 是 | 是 | **通过** |
| 493 | `ge01_full_1494_resume32_run_2026_10_16.log` | 1033 | `f655e7d9e3e0` | `$IN8XRQY.log` | `$RN8XRQY.log` | 28 | 是 | 是 | **通过** |
| 494 | `ge01_full_1494_resume32_stage_2026_10_16.json` | 7574 | `25d95a22bbb1` | `$I4B46Y7.json` | `$R4B46Y7.json` | 28 | 是 | 是 | **通过** |
| 495 | `ge01_full_1494_run_2026_10_16.log` | 14810 | `3e85eac1bf6a` | `$I3E2A3A.log` | `$R3E2A3A.log` | 28 | 是 | 是 | **通过** |
| 496 | `ge01_gate_index.py` | 3095 | `fc4ed5e7dea0` | `$I4FP8CD.py` | `$R4FP8CD.py` | 28 | 是 | 是 | **通过** |
| 497 | `ge01_gate_measure.py` | 4068 | `c2cdebcb0bfc` | `$I9QWPQM.py` | `$R9QWPQM.py` | 28 | 是 | 是 | **通过** |
| 498 | `ge01_gate_probe.py` | 3196 | `82bf49985799` | `$IGLR82F.py` | `$RGLR82F.py` | 28 | 是 | 是 | **通过** |
| 499 | `ge01_gate_scan.py` | 1955 | `5f6212d13cb5` | `$IS18KX8.py` | `$RS18KX8.py` | 28 | 是 | 是 | **通过** |
| 500 | `ge01_gate_write.py` | 82875 | `a661b2c7e5f0` | `$I6VC9SA.py` | `$R6VC9SA.py` | 28 | 是 | 是 | **通过** |
| 501 | `ge01_measure_list.json` | 2435 | `2eb41639edf4` | `$IXQJXZX.json` | `$RXQJXZX.json` | 28 | 是 | 是 | **通过** |
| 502 | `ge01_results_sha12.json` | 192203 | `97fb1089de90` | `$IZ1T82M.json` | `$RZ1T82M.json` | 28 | 是 | 是 | **通过** |
| 503 | `ge01_s3_keyscan_2026_10_16.py` | 1730 | `5f8a18033a99` | `$I9IPIL7.py` | `$R9IPIL7.py` | 28 | 是 | 是 | **通过** |
| 504 | `ge01_s3_vadj_recheck_2026_10_16.py` | 13088 | `91d3e1d91b58` | `$ISY43CH.py` | `$RSY43CH.py` | 28 | 是 | 是 | **通过** |
| 505 | `ge01_s3b_keyscan_2026_10_16.py` | 2052 | `b7743ec5a7ab` | `$I90WN2C.py` | `$R90WN2C.py` | 28 | 是 | 是 | **通过** |
| 506 | `ge01_s3b_v_exec_2026_10_16.py` | 6410 | `0df5d957a911` | `$IGDHC70.py` | `$RGDHC70.py` | 28 | 是 | 是 | **通过** |
| 507 | `ge01_s3b_v_exec_r1_2026_10_16.py` | 15257 | `4f525232efe4` | `$IFGMBF4.py` | `$RFGMBF4.py` | 28 | 是 | 是 | **通过** |
| 508 | `ge01_s3b_v_exec_r1_readings_2026_10_16.json` | 25489 | `1ec7c258c637` | `$I45T38P.json` | `$R45T38P.json` | 28 | 是 | 是 | **通过** |
| 509 | `ge01_s3b_v_exec_r1_supp_2026_10_16.py` | 5199 | `0646da5ccbe5` | `$I771WX8.py` | `$R771WX8.py` | 28 | 是 | 是 | **通过** |
| 510 | `ge01_s3b_v_exec_r1_write_2026_10_16.py` | 56062 | `359b768e7dc0` | `$INQW9E9.py` | `$RNQW9E9.py` | 28 | 是 | 是 | **通过** |
| 511 | `ge02_build.py` | 24774 | `a10c57adf6b5` | `$IMYYY6C.py` | `$RMYYY6C.py` | 28 | 是 | 是 | **通过** |
| 512 | `ge02_recompute.py` | 1347 | `811d4a138788` | `$IKM4FZ0.py` | `$RKM4FZ0.py` | 28 | 是 | 是 | **通过** |
| 513 | `gen_supp3.py` | 15813 | `eb53c9ce140c` | `$IZ6JVAD.py` | `$RZ6JVAD.py` | 28 | 是 | 是 | **通过** |
| 514 | `gen_v35_uactive_2026_10_16.py` | 43518 | `628c99636f10` | `$IRJMCWN.py` | `$RRJMCWN.py` | 28 | 是 | 是 | **通过** |
| 515 | `h_src.py` | 727 | `a4b8970b8b1f` | `$I7CQHK6.py` | `$R7CQHK6.py` | 28 | 是 | 是 | **通过** |
| 516 | `harness.py` | 687 | `56e02c4878f4` | `$IUXOGB9.py` | `$RUXOGB9.py` | 28 | 是 | 是 | **通过** |
| 517 | `k_v3df_0_1_four_readings_2026_10_09.py` | 50232 | `2e990644cc8d` | `$I81JVN9.py` | `$R81JVN9.py` | 28 | 是 | 是 | **通过** |
| 518 | `kd14_absorption_probe.py` | 1358 | `915c968f2d04` | `$IPTQQEU.py` | `$RPTQQEU.py` | 28 | 是 | 是 | **通过** |
| 519 | `kd14_carrier_probe.py` | 1206 | `758033c2a76b` | `$ISDIVY1.py` | `$RSDIVY1.py` | 28 | 是 | 是 | **通过** |
| 520 | `kd14_m4_corrected.py` | 932 | `50c1c7d85616` | `$IQ3GVXN.py` | `$RQ3GVXN.py` | 28 | 是 | 是 | **通过** |
| 521 | `klm41_2_bootstrap_ci_2026_10_16.json` | 12373 | `be99abcba9bf` | `$IV5WHP9.json` | `$RV5WHP9.json` | 28 | 是 | 是 | **通过** |
| 522 | `klm41_2_caliber_decl_2026_10_16.json` | 4757 | `6f0721d20c06` | `$IHUSZGY.json` | `$RHUSZGY.json` | 28 | 是 | 是 | **通过** |
| 523 | `klm41_2_caliber_decl_2026_10_16.py` | 10466 | `d9754474ad9a` | `$I8QAZVW.py` | `$R8QAZVW.py` | 28 | 是 | 是 | **通过** |
| 524 | `klm41_2_compute_ci_2026_10_16.py` | 14398 | `fb38b90df08f` | `$IKW9S1A.py` | `$RKW9S1A.py` | 28 | 是 | 是 | **通过** |
| 525 | `klm41_2_freeze_2026_10_16.json` | 3211 | `2a4453d9610b` | `$I7VXX9C.json` | `$R7VXX9C.json` | 28 | 是 | 是 | **通过** |
| 526 | `klm41_2_stratified_ci_2026_10_16.json` | 18820 | `67ae4f540e47` | `$IHNI6OZ.json` | `$RHNI6OZ.json` | 28 | 是 | 是 | **通过** |
| 527 | `klm41_2_stratified_ci_2026_10_16.py` | 8819 | `f29526bccea3` | `$IJ09CDC.py` | `$RJ09CDC.py` | 28 | 是 | 是 | **通过** |
| 528 | `klm41_2_verify_2026_10_16.json` | 2906 | `5ded5068566b` | `$ILFUC2M.json` | `$RLFUC2M.json` | 28 | 是 | 是 | **通过** |
| 529 | `klm41_2_verify_2026_10_16.py` | 10976 | `af0f38f33222` | `$ICJ8408.py` | `$RCJ8408.py` | 28 | 是 | 是 | **通过** |
| 530 | `klm41_2_write_doc_2026_10_16.py` | 48391 | `902dcf78f2b8` | `$IQRR19Q.py` | `$RQRR19Q.py` | 28 | 是 | 是 | **通过** |
| 531 | `klm41_3_ts_caliber_decl_2026_10_16.json` | 3255 | `96456529a485` | `$IJLQHYO.json` | `$RJLQHYO.json` | 28 | 是 | 是 | **通过** |
| 532 | `klm41_3_ts_collect_2026_10_16.py` | 23196 | `a28c4ba40940` | `$ITIY139.py` | `$RTIY139.py` | 28 | 是 | 是 | **通过** |
| 533 | `klm41_3_ts_freeze_2026_10_16.json` | 2235 | `25c021d29b1b` | `$ILHZXFZ.json` | `$RLHZXFZ.json` | 28 | 是 | 是 | **通过** |
| 534 | `klm41_3_ts_llm_calls_2026_10_16.jsonl` | 123255 | `595699b7ec44` | `$ISHA0FK.jsonl` | `$RSHA0FK.jsonl` | 28 | 是 | 是 | **通过** |
| 535 | `klm41_3_ts_measurement_2026_10_16.json` | 252951 | `211a49ca9941` | `$IS4T26F.json` | `$RS4T26F.json` | 28 | 是 | 是 | **通过** |
| 536 | `klm41_3_ts_preflight_2026_10_16.json` | 6349 | `d1fe0a6889be` | `$I0NVCYD.json` | `$R0NVCYD.json` | 28 | 是 | 是 | **通过** |
| 537 | `klm41_3_ts_preflight_2026_10_16.py` | 6228 | `c787c6d4e361` | `$IGJWC84.py` | `$RGJWC84.py` | 28 | 是 | 是 | **通过** |
| 538 | `klm41_3_ts_tables_2026_10_16.md` | 11297 | `54213bffc216` | `$IIMH12T.md` | `$RIMH12T.md` | 28 | 是 | 是 | **通过** |
| 539 | `klm41_3_ts_verify_2026_10_16.json` | 5848 | `8cf7bb595870` | `$IQ2XK6O.json` | `$RQ2XK6O.json` | 28 | 是 | 是 | **通过** |
| 540 | `kro_extract.py` | 802 | `b5731abae41f` | `$I9QNHEZ.py` | `$R9QNHEZ.py` | 28 | 是 | 是 | **通过** |
| 541 | `m08_enum_v2_2026_10_16.json` | 12255 | `c45cfc3ddc8d` | `$IZPZQKC.json` | `$RZPZQKC.json` | 28 | 是 | 是 | **通过** |
| 542 | `m08_r1_amend2_2026_10_16.json` | 1296 | `21ad2e7acd0b` | `$I982CR3.json` | `$R982CR3.json` | 28 | 是 | 是 | **通过** |
| 543 | `m08_r1_amend3_2026_10_16.json` | 3034 | `d77931c6d7a5` | `$I52OHL6.json` | `$R52OHL6.json` | 28 | 是 | 是 | **通过** |
| 544 | `m08_r1_amend_2026_10_16.json` | 1204 | `3c982068b276` | `$I3YKIH1.json` | `$R3YKIH1.json` | 28 | 是 | 是 | **通过** |
| 545 | `m08_r1_enum_2026_10_16.json` | 13253 | `361f67e37092` | `$IST9UTZ.json` | `$RST9UTZ.json` | 28 | 是 | 是 | **通过** |
| 546 | `m08_r1_enum_2026_10_16.py` | 16318 | `884b7161e053` | `$IQMIBP5.py` | `$RQMIBP5.py` | 28 | 是 | 是 | **通过** |
| 547 | `m08_r1_freeze_2026_10_16.json` | 7655 | `1a40d8046fdc` | `$IAOXA9W.json` | `$RAOXA9W.json` | 28 | 是 | 是 | **通过** |
| 548 | `m08_r1_freeze_2026_10_16.py` | 9207 | `8c6b5e0d3ebb` | `$IYR93JO.py` | `$RYR93JO.py` | 28 | 是 | 是 | **通过** |
| 549 | `m08_r1_llm_arm_2026_10_16.json` | 11335 | `19d93d77b46e` | `$I85GM79.json` | `$R85GM79.json` | 28 | 是 | 是 | **通过** |
| 550 | `m08_r1_llm_arm_2026_10_16.py` | 9852 | `987820693d06` | `$I5319DF.py` | `$R5319DF.py` | 28 | 是 | 是 | **通过** |
| 551 | `m08_r1_llm_calls_2026_10_16.jsonl` | 8271 | `0e8c9664b06d` | `$IUCEU2H.jsonl` | `$RUCEU2H.jsonl` | 28 | 是 | 是 | **通过** |
| 552 | `m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | 8230 | `d30121ed7ebf` | `$IQSH045.jsonl` | `$RQSH045.jsonl` | 28 | 是 | 是 | **通过** |
| 553 | `m08_r1_llm_probe2_2026_10_16.json` | 1805 | `d2a8510b1322` | `$IEVLYRA.json` | `$REVLYRA.json` | 28 | 是 | 是 | **通过** |
| 554 | `m08_r1_llm_probe2_2026_10_16.py` | 2359 | `190668eae9da` | `$IP0KLZ5.py` | `$RP0KLZ5.py` | 28 | 是 | 是 | **通过** |
| 555 | `m08_r1_probe_2026_10_16.json` | 3752 | `c2ba80ba548b` | `$IGPH1Z2.json` | `$RGPH1Z2.json` | 28 | 是 | 是 | **通过** |
| 556 | `m08_r1_probe_2026_10_16.py` | 4739 | `63f0234a7c89` | `$ILUTNVD.py` | `$RLUTNVD.py` | 28 | 是 | 是 | **通过** |
| 557 | `m08_r1_recompute_2026_10_16.json` | 2072 | `59ddca239f67` | `$IFTG4QR.json` | `$RFTG4QR.json` | 28 | 是 | 是 | **通过** |
| 558 | `m08_r1_recompute_2026_10_16.py` | 6998 | `305ee668612c` | `$I00QE9M.py` | `$R00QE9M.py` | 28 | 是 | 是 | **通过** |
| 559 | `m08_r1_srcsha_2026_10_16.json` | 8851 | `2074096a45e2` | `$IEZ2FTF.json` | `$REZ2FTF.json` | 28 | 是 | 是 | **通过** |
| 560 | `m08_r1_srcsha_2026_10_16.py` | 3697 | `96ac0e7c23f6` | `$I8V7GI3.py` | `$R8V7GI3.py` | 28 | 是 | 是 | **通过** |
| 561 | `m08_r1_write_2026_10_16.py` | 58218 | `0a5d9e9f18d9` | `$IJJJXYR.py` | `$RJJJXYR.py` | 28 | 是 | 是 | **通过** |
| 562 | `m2_docwriter_write.py` | 23214 | `9842ca168062` | `$I8QUA8S.py` | `$R8QUA8S.py` | 28 | 是 | 是 | **通过** |
| 563 | `m2_write.py` | 24159 | `133387a21ec6` | `$IED3ZHO.py` | `$RED3ZHO.py` | 28 | 是 | 是 | **通过** |
| 564 | `m2verdict_downstream.py` | 2240 | `93c831a7fc0f` | `$I3ZWWY8.py` | `$R3ZWWY8.py` | 28 | 是 | 是 | **通过** |
| 565 | `m2verdict_meta.py` | 1223 | `c89599655807` | `$IGIUAYI.py` | `$RGIUAYI.py` | 28 | 是 | 是 | **通过** |
| 566 | `m2verdict_probe.py` | 4493 | `3a401ef46a00` | `$I4XCWXB.py` | `$R4XCWXB.py` | 28 | 是 | 是 | **通过** |
| 567 | `m2verdict_ruling.py` | 1125 | `841949136e81` | `$I20NOEG.py` | `$R20NOEG.py` | 28 | 是 | 是 | **通过** |
| 568 | `m41_dual_readout.py` | 6471 | `45f3d856efd8` | `$IZ9ZF9B.py` | `$RZ9ZF9B.py` | 28 | 是 | 是 | **通过** |
| 569 | `m41_endpoint_probe.py` | 1520 | `f9811a6eceba` | `$IVF62M5.py` | `$RVF62M5.py` | 28 | 是 | 是 | **通过** |
| 570 | `m41_fix_diag.json` | 1034 | `2e34378d0d2c` | `$IHP8FUB.json` | `$RHP8FUB.json` | 28 | 是 | 是 | **通过** |
| 571 | `m41_keyprobe.py` | 892 | `10e08b837e05` | `$ITF1M9K.py` | `$RTF1M9K.py` | 28 | 是 | 是 | **通过** |
| 572 | `m41_keysurvey.py` | 1296 | `795daa633133` | `$IF5A5HO.py` | `$RF5A5HO.py` | 28 | 是 | 是 | **通过** |
| 573 | `m41_llm_calls.jsonl` | 642 | `a1651f3d9303` | `$I5RMA5K.jsonl` | `$R5RMA5K.jsonl` | 28 | 是 | 是 | **通过** |
| 574 | `m41_mech_arms.json` | 1252 | `be1a8fce8660` | `$I3P9Y42.json` | `$R3P9Y42.json` | 28 | 是 | 是 | **通过** |
| 575 | `m41_mech_arms.py` | 3731 | `a92812ceae61` | `$IPF4M3B.py` | `$RPF4M3B.py` | 28 | 是 | 是 | **通过** |
| 576 | `m41_r15_collect_readout.py` | 13324 | `d4e882337b80` | `$IXDSVKH.py` | `$RXDSVKH.py` | 28 | 是 | 是 | **通过** |
| 577 | `m41_r15_llm_calls.jsonl` | 3467 | `7d0dbb58d53a` | `$IZSAB4V.jsonl` | `$RZSAB4V.jsonl` | 28 | 是 | 是 | **通过** |
| 578 | `m41_r15_readout.json` | 14261 | `33a4720bcafd` | `$I4UD1MH.json` | `$R4UD1MH.json` | 28 | 是 | 是 | **通过** |
| 579 | `m41_r15_verify.py` | 4235 | `f72545f959b4` | `$IXWK80U.py` | `$RXWK80U.py` | 28 | 是 | 是 | **通过** |
| 580 | `m41_rerun_llm_calls.jsonl` | 24253 | `19fa12f4e053` | `$IOL9TII.jsonl` | `$ROL9TII.jsonl` | 28 | 是 | 是 | **通过** |
| 581 | `m41_selfcheck.json` | 318 | `d18a46a884f2` | `$IE04O5M.json` | `$RE04O5M.json` | 28 | 是 | 是 | **通过** |
| 582 | `m41_selfcheck.py` | 1291 | `5f066493fdbc` | `$IU6S0B1.py` | `$RU6S0B1.py` | 28 | 是 | 是 | **通过** |
| 583 | `m41_src_shas.py` | 1138 | `47a192be190a` | `$IJ8VI3S.py` | `$RJ8VI3S.py` | 28 | 是 | 是 | **通过** |
| 584 | `m41_src_shas.txt` | 420 | `b2c58664cd51` | `$I5AUCFS.txt` | `$R5AUCFS.txt` | 28 | 是 | 是 | **通过** |
| 585 | `material_expansion_kill_freeze_2026_10_16.json` | 15187 | `03a628456f0b` | `$IOF12YF.json` | `$ROF12YF.json` | 28 | 是 | 是 | **通过** |
| 586 | `me_llm_calls_2026_10_16.jsonl` | 21339 | `fbdedcb0ef48` | `$IK9W2S7.jsonl` | `$RK9W2S7.jsonl` | 28 | 是 | 是 | **通过** |
| 587 | `me_t4_resolve_2026_10_16.py` | 9507 | `71b0e9c8da44` | `$I090SI7.py` | `$R090SI7.py` | 28 | 是 | 是 | **通过** |
| 588 | `mq04_budget_calc_2026_10_15.json` | 5436 | `e8a5b2533ac2` | `$IGNZO0U.json` | `$RGNZO0U.json` | 28 | 是 | 是 | **通过** |
| 589 | `mq04_budget_calc_2026_10_15.py` | 6803 | `e5e4fcfd5e29` | `$IEA49YJ.py` | `$REA49YJ.py` | 28 | 是 | 是 | **通过** |
| 590 | `mq04_nt_llm_calls_2026_10_15.jsonl` | 24320 | `734af9135441` | `$I8Q9CE1.jsonl` | `$R8Q9CE1.jsonl` | 28 | 是 | 是 | **通过** |
| 591 | `mq04_nt_measure_2026_10_15.py` | 14503 | `5e55c0ff27f8` | `$IUZDHAB.py` | `$RUZDHAB.py` | 28 | 是 | 是 | **通过** |
| 592 | `mq04_nt_measurement_2026_10_15.json` | 6047 | `956d35f25c70` | `$I32M2VM.json` | `$R32M2VM.json` | 28 | 是 | 是 | **通过** |
| 593 | `mq04_write_doc_2026_10_15.py` | 26377 | `7fb013086741` | `$IIK0RU6.py` | `$RIK0RU6.py` | 28 | 是 | 是 | **通过** |
| 594 | `pa_block.py` | 345 | `19ac8c59439b` | `$I1FWACG.py` | `$R1FWACG.py` | 28 | 是 | 是 | **通过** |
| 595 | `pk33q_body.md` | 26976 | `20ad5b45ba2c` | `$I4KISRE.md` | `$R4KISRE.md` | 28 | 是 | 是 | **通过** |
| 596 | `pk_body1.md` | 26832 | `b32ca40ec103` | `$IE6SP3L.md` | `$RE6SP3L.md` | 28 | 是 | 是 | **通过** |
| 597 | `pk_body2.md` | 32568 | `75a818b2654f` | `$IFR85GE.md` | `$RFR85GE.md` | 28 | 是 | 是 | **通过** |
| 598 | `pk_lockv2_degeneracy_2026_10_15.json` | 2583 | `1106bb7d5c56` | `$IHY96W3.json` | `$RHY96W3.json` | 28 | 是 | 是 | **通过** |
| 599 | `pk_lockv2_degeneracy_2026_10_15.py` | 2425 | `e8067070c849` | `$IRGVQKT.py` | `$RRGVQKT.py` | 28 | 是 | 是 | **通过** |
| 600 | `pk_lockv2_verify_2026_10_15.json` | 4691 | `34cf77faf825` | `$IM4VOH1.json` | `$RM4VOH1.json` | 28 | 是 | 是 | **通过** |
| 601 | `pk_lockv2_verify_2026_10_15.py` | 3784 | `67795949087d` | `$IYPH4G2.py` | `$RYPH4G2.py` | 28 | 是 | 是 | **通过** |
| 602 | `pk_lockv2_write_2026_10_15.py` | 33749 | `440affa3e102` | `$IR4IRRS.py` | `$RR4IRRS.py` | 28 | 是 | 是 | **通过** |
| 603 | `pk_measure_01.py` | 1510 | `76af3ed43f2c` | `$IA1AYO0.py` | `$RA1AYO0.py` | 28 | 是 | 是 | **通过** |
| 604 | `pk_probe2_2026_10_16.py` | 1140 | `632e6dca295d` | `$ICZRCGQ.py` | `$RCZRCGQ.py` | 28 | 是 | 是 | **通过** |
| 605 | `pk_probe_2026_10_16.py` | 878 | `809cf2066d48` | `$IRM06U6.py` | `$RRM06U6.py` | 28 | 是 | 是 | **通过** |
| 606 | `pk_supp500_calc_2026_10_16.py` | 3079 | `5325e2e6bc00` | `$ISOAPFN.py` | `$RSOAPFN.py` | 28 | 是 | 是 | **通过** |
| 607 | `pk_t5lock_body_2026_10_15.md` | 46621 | `404d4fbeef40` | `$IJITZBH.md` | `$RJITZBH.md` | 28 | 是 | 是 | **通过** |
| 608 | `pk_t5lock_verify_2026_10_15.json` | 4931 | `0b9c36f612da` | `$IMRK7HC.json` | `$RMRK7HC.json` | 28 | 是 | 是 | **通过** |
| 609 | `pk_t5lock_verify_2026_10_15.py` | 5559 | `3f21b53443b4` | `$I66UBLI.py` | `$R66UBLI.py` | 28 | 是 | 是 | **通过** |
| 610 | `pk_t5lock_write_2026_10_15.py` | 3938 | `e80c26269446` | `$ID915HZ.py` | `$RD915HZ.py` | 28 | 是 | 是 | **通过** |
| 611 | `pk_write_budget210_2026_10_16.py` | 20931 | `0c65c2e859f9` | `$III8X71.py` | `$RII8X71.py` | 28 | 是 | 是 | **通过** |
| 612 | `pk_write_design_review_2026_10_16.py` | 47618 | `439fa0ae048d` | `$I0OZHIN.py` | `$R0OZHIN.py` | 28 | 是 | 是 | **通过** |
| 613 | `pool_search.py` | 2127 | `3245af3f3bbb` | `$IJ45H6I.py` | `$RJ45H6I.py` | 28 | 是 | 是 | **通过** |
| 614 | `prep.py` | 4091 | `e401c8e50f93` | `$ICILN8W.py` | `$RCILN8W.py` | 28 | 是 | 是 | **通过** |
| 615 | `probe3_out.txt` | 41096 | `d2cef7709033` | `$IN70C0C.txt` | `$RN70C0C.txt` | 28 | 是 | 是 | **通过** |
| 616 | `r3m2_disp_write.py` | 18437 | `988c2fee3ea2` | `$IZJTEXL.py` | `$RZJTEXL.py` | 28 | 是 | 是 | **通过** |
| 617 | `r461_layers.json` | 102003 | `fee35e10c208` | `$IZ5J7OO.json` | `$RZ5J7OO.json` | 28 | 是 | 是 | **通过** |
| 618 | `r461_write_01.py` | 19104 | `9030a50780da` | `$ICCW2PW.py` | `$RCCW2PW.py` | 28 | 是 | 是 | **通过** |
| 619 | `recheck2.py` | 2282 | `85c4cfa3eb46` | `$II7IWZO.py` | `$RI7IWZO.py` | 28 | 是 | 是 | **通过** |
| 620 | `ref_exp_harness_OLD_2026_10_15.py` | 13342 | `7957bac14455` | `$IBBIZVI.py` | `$RBBIZVI.py` | 28 | 是 | 是 | **通过** |
| 621 | `run_steps.py` | 2756 | `019f8405d4cf` | `$IX27VOI.py` | `$RX27VOI.py` | 28 | 是 | 是 | **通过** |
| 622 | `s3_recompute_pass4.py` | 4439 | `6f210893fcce` | `$I9YLTH3.py` | `$R9YLTH3.py` | 28 | 是 | 是 | **通过** |
| 623 | `s4_regen_runner.py` | 13040 | `70467364bdb1` | `$IBPUKWA.py` | `$RBPUKWA.py` | 28 | 是 | 是 | **通过** |
| 624 | `scan_classify_five_terminal_2026_10_10.py` | 7603 | `0b9b59083534` | `$I6EMYRE.py` | `$R6EMYRE.py` | 28 | 是 | 是 | **通过** |
| 625 | `scan_domain_five_terminal_2026_10_10.py` | 2243 | `732489dc3dbd` | `$IIGZZH1.py` | `$RIGZZH1.py` | 28 | 是 | 是 | **通过** |
| 626 | `scan_supplement_five_terminal_2026_10_10.py` | 6010 | `7c0a6d022104` | `$IYKJZB8.py` | `$RYKJZB8.py` | 28 | 是 | 是 | **通过** |
| 627 | `scope_scan.py` | 3380 | `07349acfe90f` | `$IRIQKU3.py` | `$RRIQKU3.py` | 28 | 是 | 是 | **通过** |
| 628 | `singlevar.py` | 1515 | `f0bba43af3e5` | `$I5BJ9KU.py` | `$R5BJ9KU.py` | 28 | 是 | 是 | **通过** |
| 629 | `t2_path_b_kill_freeze_2026_10_16.json` | 14896 | `3f3272100f62` | `$I2DMC1W.json` | `$R2DMC1W.json` | 28 | 是 | 是 | **通过** |
| 630 | `t2b_census_2026_10_16.py` | 3041 | `71f99afb9199` | `$ILB8TEG.py` | `$RLB8TEG.py` | 28 | 是 | 是 | **通过** |
| 631 | `t2b_derive_2026_10_16.py` | 7964 | `324165eb0c7d` | `$IF8AIAZ.py` | `$RF8AIAZ.py` | 28 | 是 | 是 | **通过** |
| 632 | `t2b_fetch_facts_2026_10_16.py` | 5774 | `0941558d024e` | `$IOIOW0C.py` | `$ROIOW0C.py` | 28 | 是 | 是 | **通过** |
| 633 | `t2b_freeze_2026_10_16.py` | 13908 | `575b796a2e6f` | `$IXUR7XW.py` | `$RXUR7XW.py` | 28 | 是 | 是 | **通过** |
| 634 | `t2b_freeze_v2_2026_10_16.py` | 17044 | `02a261b12f7b` | `$IGPD5V0.py` | `$RGPD5V0.py` | 28 | 是 | 是 | **通过** |
| 635 | `t2b_harness_pre_change_snapshot_2026_10_16.py` | 36217 | `d5c8d676bb5b` | `$I4DNQWB.py` | `$R4DNQWB.py` | 28 | 是 | 是 | **通过** |
| 636 | `t2b_impl_audit_2026_10_16.py` | 4856 | `e02a343246bd` | `$I7BREOU.py` | `$R7BREOU.py` | 28 | 是 | 是 | **通过** |
| 637 | `t2b_inspect_facts_2026_10_16.py` | 1732 | `de3c879e39f1` | `$IWM17DP.py` | `$RWM17DP.py` | 28 | 是 | 是 | **通过** |
| 638 | `t2b_llm_calls_2026_10_16.jsonl` | 5317 | `a54a3af46ba2` | `$IV5ZTJD.jsonl` | `$RV5ZTJD.jsonl` | 28 | 是 | 是 | **通过** |
| 639 | `t2b_measure_2026_10_16.py` | 15547 | `bd377372927c` | `$IOTXQY4.py` | `$ROTXQY4.py` | 28 | 是 | 是 | **通过** |
| 640 | `t2b_measurement_2026_10_16.json` | 25796 | `fe5db6defb09` | `$I7ACEGM.json` | `$R7ACEGM.json` | 28 | 是 | 是 | **通过** |
| 641 | `t2b_patch_harness_2026_10_16.py` | 7065 | `bac4775c5c44` | `$IFI9KCU.py` | `$RFI9KCU.py` | 28 | 是 | 是 | **通过** |
| 642 | `t2b_strategyqa_train_snapshot_2026_10_16.json` | 4281955 | `728e28b7d6bd` | `$IEXHAY0.json` | `$REXHAY0.json` | 28 | 是 | 是 | **通过** |
| 643 | `t3_baseline_procedure_probe.py` | 2292 | `b4c2a5e68dfa` | `$ILP1Y0P.py` | `$RLP1Y0P.py` | 28 | 是 | 是 | **通过** |
| 644 | `t3_baseline_procedure_probe_2026_10_15.json` | 1332 | `7ac600d45dcc` | `$IT3FDJH.json` | `$RT3FDJH.json` | 28 | 是 | 是 | **通过** |
| 645 | `t3_freeze_2026_10_15.json` | 7436 | `313f091718cc` | `$ITSYV7T.json` | `$RTSYV7T.json` | 28 | 是 | 是 | **通过** |
| 646 | `t3_harness_diff_2026_10_15.diff` | 3463 | `0f8532aefdff` | `$ITQN5BA.diff` | `$RTQN5BA.diff` | 28 | 是 | 是 | **通过** |
| 647 | `t3_nt_llm_calls_2026_10_15.jsonl` | 5250 | `0cb1decec878` | `$IPBMSOQ.jsonl` | `$RPBMSOQ.jsonl` | 28 | 是 | 是 | **通过** |
| 648 | `t3_nt_measure_2026_10_15.py` | 17111 | `35860b379b7a` | `$ITNA7J0.py` | `$RTNA7J0.py` | 28 | 是 | 是 | **通过** |
| 649 | `t3_nt_measurement_2026_10_15.json` | 19576 | `92f0dc763caf` | `$IMJ4M5Z.json` | `$RMJ4M5Z.json` | 28 | 是 | 是 | **通过** |
| 650 | `t3_nt_verify.py` | 6657 | `a1c38dc17d65` | `$IDYELGR.py` | `$RDYELGR.py` | 28 | 是 | 是 | **通过** |
| 651 | `t3_nt_verify_2026_10_15.json` | 3885 | `700de33ee255` | `$I866RHG.json` | `$R866RHG.json` | 28 | 是 | 是 | **通过** |
| 652 | `t3_postchange_equiv.py` | 5975 | `1e579de6033c` | `$IMALBBZ.py` | `$RMALBBZ.py` | 28 | 是 | 是 | **通过** |
| 653 | `t3_postchange_equiv_2026_10_15.json` | 3904 | `e8a97dc64a08` | `$IQ0A36H.json` | `$RQ0A36H.json` | 28 | 是 | 是 | **通过** |
| 654 | `t3_postchange_manifest_check_2026_10_15.json` | 2135 | `dbfae4d96b46` | `$IL4QEUR.json` | `$RL4QEUR.json` | 28 | 是 | 是 | **通过** |
| 655 | `t3_postcheck.py` | 3129 | `20c96933b00d` | `$IGNU9G7.py` | `$RGNU9G7.py` | 28 | 是 | 是 | **通过** |
| 656 | `t3_prechange_manifest_2026_10_15.json` | 76683 | `f1508ebe14e7` | `$I1UDWK8.json` | `$R1UDWK8.json` | 28 | 是 | 是 | **通过** |
| 657 | `t3_prove_minimal_increment_2026_10_15.json` | 433 | `3f858f6958cd` | `$IS7BZE9.json` | `$RS7BZE9.json` | 28 | 是 | 是 | **通过** |
| 658 | `t3_prove_minimal_increment_2026_10_15.py` | 7303 | `1f39cf068862` | `$IML5U13.py` | `$RML5U13.py` | 28 | 是 | 是 | **通过** |
| 659 | `t3_repro_probe_ftfb_freeze_2026_10_16.json` | 2936 | `44761c404b86` | `$IPEIDOX.json` | `$RPEIDOX.json` | 28 | 是 | 是 | **通过** |
| 660 | `t3_repro_probe_llm_calls_2026_10_16.jsonl` | 7441 | `54ad4d2cd8bf` | `$I4BI6OE.jsonl` | `$R4BI6OE.jsonl` | 28 | 是 | 是 | **通过** |
| 661 | `t3_repro_probe_measure_2026_10_16.json` | 9137 | `31779f66c051` | `$I4LGQ1L.json` | `$R4LGQ1L.json` | 28 | 是 | 是 | **通过** |
| 662 | `t5_baseline_manifest_2026_10_15.json` | 99724 | `2d5ad82c0a63` | `$I96TFAV.json` | `$R96TFAV.json` | 28 | 是 | 是 | **通过** |
| 663 | `t5_harness_diff_2026_10_15.diff` | 4043 | `6f1e9689201b` | `$I6CDB8K.diff` | `$R6CDB8K.diff` | 28 | 是 | 是 | **通过** |
| 664 | `t5_kill_line_freeze_2026_10_15.json` | 3183 | `1910a62c1e9f` | `$IPWAI63.json` | `$RPWAI63.json` | 28 | 是 | 是 | **通过** |
| 665 | `t5_nt_llm_calls_2026_10_15.jsonl` | 7258 | `8e488d14bff6` | `$IVAQMY2.jsonl` | `$RVAQMY2.jsonl` | 28 | 是 | 是 | **通过** |
| 666 | `t5_nt_measure_2026_10_15.py` | 15602 | `c96c985d8e23` | `$IR772XN.py` | `$RR772XN.py` | 28 | 是 | 是 | **通过** |
| 667 | `t5_nt_measurement_2026_10_15.json` | 3845 | `674e95ecff03` | `$IZHRDFO.json` | `$RZHRDFO.json` | 28 | 是 | 是 | **通过** |
| 668 | `t5_prefix_T1T4_digest_2026_10_15.json` | 400 | `9eb43782b73c` | `$I5HJE9P.json` | `$R5HJE9P.json` | 28 | 是 | 是 | **通过** |
| 669 | `t5_prove_minimal_increment_2026_10_15.py` | 6308 | `65cec9c9788e` | `$IRNEYQ6.py` | `$RRNEYQ6.py` | 28 | 是 | 是 | **通过** |
| 670 | `t5_write_docs_2026_10_15.py` | 47918 | `f104bf4706e6` | `$IR13ZYB.py` | `$RR13ZYB.py` | 28 | 是 | 是 | **通过** |
| 671 | `tables.py` | 1818 | `02cc157b6d69` | `$I4ZR5PT.py` | `$R4ZR5PT.py` | 28 | 是 | 是 | **通过** |
| 672 | `three_seed_caliber_decl_2026_10_16.json` | 4859 | `5df309d557b0` | `$IWXQ4IT.json` | `$RWXQ4IT.json` | 28 | 是 | 是 | **通过** |
| 673 | `three_seed_collect_2026_10_16.py` | 28520 | `672d12ad9801` | `$I8X158M.py` | `$R8X158M.py` | 28 | 是 | 是 | **通过** |
| 674 | `three_seed_collect_log_2026_10_16.txt` | 16230 | `55c783261d18` | `$IPLD55S.txt` | `$RPLD55S.txt` | 28 | 是 | 是 | **通过** |
| 675 | `three_seed_freeze_2026_10_16.json` | 10536 | `46260e3b8426` | `$IRAFZLD.json` | `$RRAFZLD.json` | 28 | 是 | 是 | **通过** |
| 676 | `three_seed_llm_calls_2026_10_16.jsonl` | 104288 | `5a8cbcf85aa7` | `$IJUJ3RR.jsonl` | `$RJUJ3RR.jsonl` | 28 | 是 | 是 | **通过** |
| 677 | `three_seed_measurement_2026_10_16.json` | 226256 | `ff5ed4b0e329` | `$ICTYSPV.json` | `$RCTYSPV.json` | 28 | 是 | 是 | **通过** |
| 678 | `three_seed_preflight_2026_10_16.py` | 5661 | `98e0e4ae7a73` | `$IKNPAQ3.py` | `$RKNPAQ3.py` | 28 | 是 | 是 | **通过** |
| 679 | `three_seed_verify_2026_10_16.json` | 3205 | `61e3d0bfa05d` | `$IM46TRU.json` | `$RM46TRU.json` | 28 | 是 | 是 | **通过** |
| 680 | `three_seed_verify_2026_10_16.py` | 13402 | `5c382ace9573` | `$IO8N161.py` | `$RO8N161.py` | 28 | 是 | 是 | **通过** |
| 681 | `three_seed_write_doc_2026_10_16.py` | 50308 | `f546bdd3630c` | `$I5UFYXG.py` | `$R5UFYXG.py` | 28 | 是 | 是 | **通过** |
| 682 | `u04_1_chain_verify.py` | 4849 | `13e573534692` | `$ISJMXTL.py` | `$RSJMXTL.py` | 28 | 是 | 是 | **通过** |
| 683 | `u04_1_dual_verify.py` | 3228 | `f5702456560f` | `$IKMUI5J.py` | `$RKMUI5J.py` | 28 | 是 | 是 | **通过** |
| 684 | `u04_1_make_data.py` | 19773 | `309ac58e049d` | `$ISMYZLE.py` | `$RSMYZLE.py` | 28 | 是 | 是 | **通过** |
| 685 | `verify_final.py` | 805 | `904eb215f139` | `$IAH2EAB.py` | `$RAH2EAB.py` | 28 | 是 | 是 | **通过** |
| 686 | `verify_t3trap_bprime_2026_10_15.py` | 6928 | `a9e880243eab` | `$IOTIHW3.py` | `$ROTIHW3.py` | 28 | 是 | 是 | **通过** |
| 687 | `vk_denominator_2026_10_16.py` | 856 | `d935b89bfa31` | `$INBGQFV.py` | `$RNBGQFV.py` | 28 | 是 | 是 | **通过** |
| 688 | `vk_interval_arith_2026_10_16.py` | 1273 | `901d8df83bb3` | `$ILG0LXA.py` | `$RLG0LXA.py` | 28 | 是 | 是 | **通过** |
| 689 | `vk_v3df_0_1_agree.py` | 6140 | `84c090952894` | `$I3NRWIJ.py` | `$R3NRWIJ.py` | 28 | 是 | 是 | **通过** |
| 690 | `vk_v3df_0_1_coverage_gap.py` | 1971 | `df25000e7180` | `$I8L50G6.py` | `$R8L50G6.py` | 28 | 是 | 是 | **通过** |
| 691 | `vk_v3df_0_1_materiality.py` | 2875 | `b666b7a38082` | `$IE4ZKE8.py` | `$RE4ZKE8.py` | 28 | 是 | 是 | **通过** |
| 692 | `vk_v3df_0_1_verify_2026_10_09.py` | 14347 | `0e7cb9348a16` | `$IAN4PZ3.py` | `$RAN4PZ3.py` | 28 | 是 | 是 | **通过** |
| 693 | `vk_verify_2026_10_16.py` | 3780 | `6ad7edf03032` | `$IKCIC8D.py` | `$RKCIC8D.py` | 28 | 是 | 是 | **通过** |
| 694 | `vk_verify_interval_ceiling_2026_10_16.py` | 3692 | `18b0f12b2c66` | `$I2DWVQV.py` | `$R2DWVQV.py` | 28 | 是 | 是 | **通过** |
| 695 | `vk_write_2026_10_16.py` | 62030 | `2334a967a1d4` | `$IM1KS6X.py` | `$RM1KS6X.py` | 28 | 是 | 是 | **通过** |
| 696 | `vk_write_interval_ceiling_post_lock_2026_10_16.py` | 47768 | `3076d727e02c` | `$ITQJ0WU.py` | `$RTQJ0WU.py` | 28 | 是 | 是 | **通过** |
| 697 | `write_items_json.py` | 4388 | `9dce7986e20d` | `$I0XGZXI.py` | `$R0XGZXI.py` | 28 | 是 | 是 | **通过** |
| 698 | `write_summary_json.py` | 9049 | `6214ad3cdc2d` | `$IZ3CONP.py` | `$RZ3CONP.py` | 28 | 是 | 是 | **通过** |
| 699 | `write_t3trap_bprime_2026_10_15.py` | 33905 | `ca5fc520f530` | `$IU89HRT.py` | `$RU89HRT.py` | 28 | 是 | 是 | **通过** |

### 4.1 目录本体（空后，同通道）

| 目录 | rc | 已消失 | `$I` | `$R` | `$I` 长度 | 偏移 | 解码原路径 | 判定 |
|---|---|---|---|---|---|---|---|---|
| `〔本地归档区〕\whitelist_backup_2026_10_17\_pre_mod` | 0 | True | `$I1W5CWI` | `$R1W5CWI` | 170 | 28 | `〔本地归档区〕\whitelist_backup_2026_10_17\_pre_mod` | **通过** |
| `〔本地归档区〕\whitelist_backup_2026_10_17` | 0 | True | `$IDY946X` | `$RDY946X` | 152 | 28 | `〔本地归档区〕\whitelist_backup_2026_10_17` | **通过** |

**关于偏移之实测更正（照录）**：派工给定「偏移 28（文件）/ 26（目录）」。实测本机之目录 `$I` 记录长度 170 B（`_pre_mod`）/ 152 B（根目录），其字节布局为 `02 00 00 00 00 00 00 00`（版本=2）｜`00×8`（原尺寸=0）｜8 B 删除 FILETIME｜4 B 路径字符数｜路径自 **偏移 28** 起。即**文件与目录皆为偏移 28**；偏移 26 之所以「亦可解出同一串」，仅因字节 26–27 恰为 `00 00` 所致的**假性同解**，非规范字段边界。故目录记录亦判 28，不判 26。

## 5. 执行汇总

| 类别 | 计数 | 说明 |
|---|---|---|
| 计划清除（文件） | 699 | 授权面 699 件 |
| 已执行（文件） | 699 | 验道 1 + 批量 698 |
| 验真通过（文件） | 699 | rc=0 / 未中止 / 源件消失 / `$I`+`$R` 成对 / 原路径吻合 / 原尺寸吻合 / 载荷 SHA-12 复算全等 |
| 已执行（目录本体） | 2 | `_pre_mod` + 根目录 |
| 验真通过（目录本体） | 2 | |
| 失败 | 0 | — |
| 总载荷 | 38,301,580 B | 已处置 |
| 回收站记录组（本棒产生） | 701 | 每组 = `$I` + `$R` |
| 耗时（批量段） | 42.3 s | |

## 6. 清除后之核验

| 核验项 | 方法 | 结果 |
|---|---|---|
| 归档区目标路径已清 | PowerShell `Test-Path` | **False** |
| 归档区目标路径已清（Python 侧） | `os.path.exists` | **False** |
| `.tmp` 备份面存在 | `Test-Path` | **True** |
| `.tmp` 备份面件数 | 清点 | **699 / 699** |
| `.tmp` 备份面字节 | 清点 | **38,301,580**（= 清除前值） |
| `.tmp` 备份面 SHA-12 集合 | 699 件重算并集比对 | **与清除前全等：True** |
| `.tmp` 备份面完好性裁定 | 综合 | **未动·完好** |
| 白名单原件（`.tmp` 之源件面） | 未触碰 | 699 件 SHA-12 与上同集 |
| 归档区其他件 | 未触碰 | 本棒全部删除调用之目标路径均以目标目录前缀断言，越界 0 件 |

## 7. KD 清单

| # | 项 | 缺陷 |
|---|---|---|
| — | — | **0 件**（批量段失败 0、目录段失败 0；`kd` 数组为空） |

## 8. 呈报口径（新生效之永久性处置口径）

**凡删除即永久性处置；回收站存续不可恃（PI 手动清空已实证 2 次）；0 备份兜底。**

本棒之实测印证（时序见下）：

| 时点 | 观测 | 来源 |
|---|---|---|
| 12:22:17 | 验道件 `$I`/`$R` 成对且记录在站 | `step2_sample_verify.json` / `step2_sample_verify_rejudge.json` |
| 12:23:20 | 逐件处置全程，每次调用后当场验真通过 701/701 组记录在站 | `step3_bulk_result.json` |
| 12:23:20 之后 | 枚举该 SID 回收站 = 1157 条（少于「701 组 ×2 + 原有 65」应有之 1467） | PowerShell 独立清点 |
| 12:23:54 | 审计：应有 701 组 → 在站 **0** 组，`$I`=0、`$R`=0，仅余 `desktop.ini` | `step4_bin_audit.json` |
| 12:24:06 | 复测：仍仅 `desktop.ini`（129 B，创建于 2026-10-16 09:22:58） | PowerShell 独立清点 |

**清空之责任面**：现有盘上证据不足以判定清空之动因与执行者（我方三脚本仅调用 `SHFileOperationW` 于目标面路径并只读列举回收站，不含任何删除回收站条目之代码；`desktop.ini` 之时间戳属回收站目录自身初始化，早于本棒）。故此项列为**阴性结论**，三重自审如下：

1. **遍历错误自审**：`os.walk` / `os.listdir` 遍历错误数 = 0（`inventory_compare.json` 之 `walk_errors`、`step3_bulk_result.json` 之 `backup_walk_errors`），遍历面无遗漏。
2. **模式非结构性互斥自审**：回收站条目名以 `$I`/`$R` 为固定前缀，且与 `desktop.ini` 在同一目录内并列——命名空间互斥，无同名歧义；非「模式互斥」而致漏读。
3. **时点新鲜自审**：12:23:54 与 12:24:06 两次独立复测（Python + PowerShell 两通道）结论一致且贴近处置时点；非陈旧快照。

**口径面引证**：`BD748AFEC4F8` 之「凡删除即永久性处置·回收站存续不可恃·0 备份兜底」口径面，于本仓 glob `**/*BD748AFEC4F8*` **0 命中（未落盘）** → 依派工令改引卡答 `ask_4e247eec5ad691326de839ff`。**转引限制**：该口径之正文未在本棒可得，故上文仅以派工所载摘要与本棒实测互证，未逐字照录卡答原文。

**结论**：本棒 699 件之清除已达成且**已不可恢复**（可恢复窗口已于处置后 ≤34 秒内关闭）；留存面为 `.tmp/whitelist_backup_2026_10_17/` 699 件完好副本（唯一存续面）。回收站在本棒中**仅作通道、不作兜底**。

## 9. 纪律自报

| 纪律 | 落实 |
|---|---|
| 唯一可恢复通道 `SHFileOperationW`+`FOF_ALLOWUNDO` | 699 件 + 2 目录全部经此；⛔0 用 `rm` |
| 先 1 件小样验道 | 第 3 节，验道通过方启批量 |
| 落盘前 `Test-Path=False` ＋ glob 同名 0 命中 | `Test-Path`=False；glob `**/_archive_whitelist_purge_exec_register_2026_10_17*`=0 命中 |
| UTF-8 无 BOM · 纯 LF | `io.open(..., encoding='utf-8', newline='\n')` 直写 |
| Windows 路径 raw 字符串 | 全部脚本内路径为 `r"..."` |
| key 形态扫描 0 命中方落盘 | 见第 10 节 |
| 字节级自报 | 见第 10 节 |
| 数值来源为回读而非记忆 | 全文数值均由 4 份盘上 JSON 回读渲染 |

## 10. 落盘门禁自报（写入前实测）

| 门禁项 | 实测 |
|---|---|
| 目标路径 `Test-Path` | **False**（写入前实测） |
| glob `**/_archive_whitelist_purge_exec_register_2026_10_17*` | **0 命中**（写入前实测） |
| key 形态扫描（sk-/api_key/AKIA/xox*/PRIVATE KEY/Bearer/password/LLM_KEY 共 8 式） | **0 命中**（写入前实测，未命中方落盘） |
| 写入通道 | `io.open(path,'w',encoding='utf-8',newline='\n')` → UTF-8 无 BOM · 纯 LF |

> 本件字节数／BOM／CRLF 计数／LF 计数／SHA-256 之**写后**实测值，因写入后复测方知（不可自引），故不写入本件正文以免循环自证；其留痕于 `tools\_archive_purge_2026_10_17\step5_register_result.json`，并由 worker 于呈报正文逐项自报。

