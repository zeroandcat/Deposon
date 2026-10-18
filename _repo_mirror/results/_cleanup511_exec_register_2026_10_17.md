# 清理执行登记件（2026-10-17 · PI 卡 `ask_9f7d29f61ac912895a4c3a70` Q1 授权执行）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_cleanup511_exec_register_2026_10_17.md` |
| **授权出处** | PI 卡 `ask_9f7d29f61ac912895a4c3a70` **Q1** 逐字「授权执行（可清 511 件·可恢复通道）」 |
| **体例沿用** | `results/_cleanup_exec_register_2026_10_15.md`（10-15 清理登记件） |
| **执行棒** | worker（清理执行棒 · CLEANUP-EXEC-511） |
| **回收站** | `〔回收站〕` |
| **删除通道** | `shell32.SHFileOperationW(FO_DELETE)` ＋ `FOF_ALLOWUNDO`（可恢复） |
| **永久删** | **0 件**（本棒全程 ⛔0 `rm`／`Remove-Item`／`unlink`／`rmtree`） |
| **清理前 `$I` 条目** | 2（10-15 等前序清理之留存） |
| **清理后 `$I` 条目** | 436（＝本棒 434 ＋ **并发他棒 2**，见 §7） |

---

## §1 执行对照总表

| 处置 | 件数 | bytes |
| :-- | --: | --: |
| 已入回收站（可恢复） | 434 | 21,187,490 |
| 永久删（$I 在、$R 缺失） | 0 | 0 |
| 永久删（无 $I/$R 记录） | 0 | 0 |
| 失败（原件仍在） | 0 | 0 |
| **合计** | **434** | **21,187,490** |

**结果**：**删入回收站 434 件 ／ 永久删 0 件 ／ 失败 0 件**（含空目录 3 个）。

**类别分解**：C1 四通道零命中 428 件（`.tmp` 内）｜C4 `__pycache__` 3 件｜C5 空目录 3 个。

---

## §2 逐件执行对照（434 件）

| # | 路径 | bytes | SHA-12 | `$I` | `$R` | 结论 |
| --: | :-- | --: | :-- | :-- | :-- | :-- |
| 1 | `.tmp/h_mq20.py` | 285 | `5f81afe2955c` | `$IRBKH1X.py` | `$RRBKH1X.py` | 已入回收站（验道件） |
| 2 | `.tmp/r461_probe09.txt` | 0 | `e3b0c44298fc` | `$IICNAQE.txt` | `$RICNAQE.txt` | 已入回收站（验道件） |
| 3 | `.tmp/_659_ctx_probe.txt` | 11,873 | `c54be1035a90` | `$ILD8KF0.txt` | `$RLD8KF0.txt` | 已入回收站 |
| 4 | `.tmp/_659_flagged.txt` | 16,485 | `4c0817f40091` | `$ICTOV06.txt` | `$RCTOV06.txt` | 已入回收站 |
| 5 | `.tmp/_659_run_verdict.json` | 12,831 | `5f9a7560cac7` | `$IOWV4JK.json` | `$ROWV4JK.json` | 已入回收站 |
| 6 | `.tmp/__pycache__/_659_report_gen.cpython-314.pyc` | 39,841 | `6fed070a015d` | `$IOZD3OI.pyc` | `$ROZD3OI.pyc` | 已入回收站 |
| 7 | `.tmp/__pycache__/ref_exp_harness_OLD_2026_10_15.cpython-314.pyc` | 20,714 | `4efb34e71dcc` | `$IRLYPW9.pyc` | `$RRLYPW9.pyc` | 已入回收站 |
| 8 | `.tmp/__pycache__/s4_regen_runner.cpython-314.pyc` | 21,608 | `31dd999df336` | `$IQ757BR.pyc` | `$RQ757BR.pyc` | 已入回收站 |
| 9 | `.tmp/__pycache__/t2b_harness_pre_change_snapshot_2026_10_16.cpython-314.pyc` | 35,886 | `d34ed54fc1f3` | `$IFHNQYX.pyc` | `$RFHNQYX.pyc` | 已入回收站 |
| 10 | `.tmp/_audit_calls.py` | 611 | `f944d932dd6f` | `$INM327F.py` | `$RNM327F.py` | 已入回收站 |
| 11 | `.tmp/_build_reg_v33_and_effect_2026_10_16.py` | 54,882 | `a424fdb26ee8` | `$IKB7CC9.py` | `$RKB7CC9.py` | 已入回收站 |
| 12 | `.tmp/_bytecheck.py` | 888 | `53c5443da96f` | `$IIMTXZE.py` | `$RIMTXZE.py` | 已入回收站 |
| 13 | `.tmp/_c6_fast.json` | 9,901 | `65ca656c2d4f` | `$IB2N38M.json` | `$RB2N38M.json` | 已入回收站 |
| 14 | `.tmp/_c6_meta.txt` | 461 | `2a8301f02c84` | `$IYAYWW8.txt` | `$RYAYWW8.txt` | 已入回收站 |
| 15 | `.tmp/_c6_selfcheck.json` | 388 | `9e3a5bcea21e` | `$IQXBXBI.json` | `$RQXBXBI.json` | 已入回收站 |
| 16 | `.tmp/_c6_summary.txt` | 1,657 | `94ff1c5b89fc` | `$IP3QFF4.txt` | `$RP3QFF4.txt` | 已入回收站 |
| 17 | `.tmp/_canonical_census_out.json` | 5,252 | `0dfd3b6f363b` | `$I579FGT.json` | `$R579FGT.json` | 已入回收站 |
| 18 | `.tmp/_canonical_writecheck.json` | 308 | `1fa14fcff8d7` | `$IJQOJXX.json` | `$RJQOJXX.json` | 已入回收站 |
| 19 | `.tmp/_doc_c6_census.json` | 34,804 | `ca6c73cb7c65` | `$IHVLV0N.json` | `$RHVLV0N.json` | 已入回收站 |
| 20 | `.tmp/_docwriter_linecount_out.txt` | 1,554 | `2154f6321f18` | `$IR8RNTI.txt` | `$RR8RNTI.txt` | 已入回收站 |
| 21 | `.tmp/_docwriter_refscan_out_r1.txt` | 6,403 | `9056dea1d889` | `$IUX21H7.txt` | `$RUX21H7.txt` | 已入回收站 |
| 22 | `.tmp/_dw_abs_hits_dump.md` | 16,838 | `7e58051ba34b` | `$IPU8QDO.md` | `$RPU8QDO.md` | 已入回收站 |
| 23 | `.tmp/_dw_final_verify.md` | 572 | `f9cf34fdc6b3` | `$IGW6Q03.md` | `$RGW6Q03.md` | 已入回收站 |
| 24 | `.tmp/_dw_fullrows.md` | 10,893 | `d223e89d3b0c` | `$I4Z4WO6.md` | `$R4Z4WO6.md` | 已入回收站 |
| 25 | `.tmp/_dw_manifest_lines.md` | 4,400 | `da2762af8b25` | `$IQ6GB3N.md` | `$RQ6GB3N.md` | 已入回收站 |
| 26 | `.tmp/_dw_pkg_and_downstream.json` | 78,463 | `9a162fe53d4e` | `$IWYVPCT.json` | `$RWYVPCT.json` | 已入回收站 |
| 27 | `.tmp/_dw_pkg_downstream_dump.md` | 12,044 | `d48522c7f373` | `$I1Y8PBG.md` | `$R1Y8PBG.md` | 已入回收站 |
| 28 | `.tmp/_dw_probe.md` | 17,596 | `9d6c36858636` | `$IS4S62U.md` | `$RS4S62U.md` | 已入回收站 |
| 29 | `.tmp/_e_q_guard.txt` | 435 | `5b55e521b623` | `$IQKKMGS.txt` | `$RQKKMGS.txt` | 已入回收站 |
| 30 | `.tmp/_e_q_occ.txt` | 52 | `d85c13156af5` | `$IWNFO3Q.txt` | `$RWNFO3Q.txt` | 已入回收站 |
| 31 | `.tmp/_e_q_out.txt` | 10,063 | `e4fe5b54e2a8` | `$IQUUOLX.txt` | `$RQUUOLX.txt` | 已入回收站 |
| 32 | `.tmp/_e_q_rg.txt` | 65 | `42886f0e909b` | `$IWXLX9I.txt` | `$RWXLX9I.txt` | 已入回收站 |
| 33 | `.tmp/_e_q_self.txt` | 320 | `d697a97b6bd4` | `$IMVJ0GT.txt` | `$RMVJ0GT.txt` | 已入回收站 |
| 34 | `.tmp/_ea_461b.txt` | 963 | `90e55ecf537b` | `$IENFC5D.txt` | `$RENFC5D.txt` | 已入回收站 |
| 35 | `.tmp/_ea_anchor_hits.txt` | 299 | `cb092f350ad0` | `$I434WA2.txt` | `$R434WA2.txt` | 已入回收站 |
| 36 | `.tmp/_ea_f4c.txt` | 4,938 | `7a6b3d474f0b` | `$I8DJHVO.txt` | `$R8DJHVO.txt` | 已入回收站 |
| 37 | `.tmp/_ea_fam_lines.txt` | 2,328 | `ae05e267db9c` | `$IWRI22Q.txt` | `$RWRI22Q.txt` | 已入回收站 |
| 38 | `.tmp/_ea_int_u_index.txt` | 4,055 | `7364e38f6e7f` | `$IH9R7S2.txt` | `$RH9R7S2.txt` | 已入回收站 |
| 39 | `.tmp/_ea_reply_s10.txt` | 4,226 | `50b2c15085d4` | `$IEZ2JWU.txt` | `$REZ2JWU.txt` | 已入回收站 |
| 40 | `.tmp/_ea_scan.txt` | 5,147 | `31c64a39301d` | `$I8X476Z.txt` | `$R8X476Z.txt` | 已入回收站 |
| 41 | `.tmp/_ea_scan2.txt` | 550 | `f05ee2420944` | `$IVTDTST.txt` | `$RVTDTST.txt` | 已入回收站 |
| 42 | `.tmp/_ea_scan3.txt` | 2,868 | `e3199c565bdf` | `$IYS9LE1.txt` | `$RYS9LE1.txt` | 已入回收站 |
| 43 | `.tmp/_ea_scan4.txt` | 3,726 | `351d208cc3fd` | `$IIU55LI.txt` | `$RIU55LI.txt` | 已入回收站 |
| 44 | `.tmp/_ea_scan5.txt` | 42,807 | `65d1c0362ff5` | `$IHHAH27.txt` | `$RHHAH27.txt` | 已入回收站 |
| 45 | `.tmp/_ea_sub_lines.txt` | 2,300 | `584e3e4151b6` | `$I0HQQ9R.txt` | `$R0HQQ9R.txt` | 已入回收站 |
| 46 | `.tmp/_ea_v06_96.txt` | 2,657 | `457ddd94904d` | `$IRMZFAB.txt` | `$RRMZFAB.txt` | 已入回收站 |
| 47 | `.tmp/_ea_v06_s7.txt` | 4,233 | `fc536507a1d9` | `$IL548DD.txt` | `$RL548DD.txt` | 已入回收站 |
| 48 | `.tmp/_ea_v06_u_rows.txt` | 2,558 | `75cf5737b281` | `$IBO1TIR.txt` | `$RBO1TIR.txt` | 已入回收站 |
| 49 | `.tmp/_ecr_pa_a0_recompute_out_2026_10_15.json` | 7,646 | `8ec0ef8fa1e6` | `$IXAUHA3.json` | `$RXAUHA3.json` | 已入回收站 |
| 50 | `.tmp/_ecr_pa_verify_out_2026_10_15.json` | 1,994 | `799853fe155c` | `$IIE12A1.json` | `$RIE12A1.json` | 已入回收站 |
| 51 | `.tmp/_ecr_pa_verify_out_final_2026_10_15.json` | 2,262 | `4c58096971b5` | `$I1VVA76.json` | `$R1VVA76.json` | 已入回收站 |
| 52 | `.tmp/_gamma_probe_structure.py` | 607 | `b009c23b36bc` | `$IBTDOOX.py` | `$RBTDOOX.py` | 已入回收站 |
| 53 | `.tmp/_gamma_probe_structure2.py` | 662 | `c4f028462870` | `$ISWA8T7.py` | `$RSWA8T7.py` | 已入回收站 |
| 54 | `.tmp/_ge01_ecr_downstream.txt` | 72,275 | `6d3212ccba08` | `$IDLSME0.txt` | `$RDLSME0.txt` | 已入回收站 |
| 55 | `.tmp/_ge01_ecr_final_check.txt` | 854 | `7c0a38d4f5fd` | `$IBGL3JY.txt` | `$RBGL3JY.txt` | 已入回收站 |
| 56 | `.tmp/_ge01_ecr_probe3_out.txt` | 95,900 | `f0af8caa4755` | `$IM6NLHA.txt` | `$RM6NLHA.txt` | 已入回收站 |
| 57 | `.tmp/_ge01_ecr_probe4_out.txt` | 27,013 | `d8f839eca7ce` | `$I4YXQ11.txt` | `$R4YXQ11.txt` | 已入回收站 |
| 58 | `.tmp/_ge01_ecr_probe5_out.txt` | 14,527 | `0876c28e4694` | `$IMRNKE9.txt` | `$RMRNKE9.txt` | 已入回收站 |
| 59 | `.tmp/_ge01_ecr_probe6_out.txt` | 433 | `25f3a2ac4630` | `$IP9QLV0.txt` | `$RP9QLV0.txt` | 已入回收站 |
| 60 | `.tmp/_ge01_ecr_probe7_out.txt` | 5,453 | `fd895d6aa0ed` | `$IMX2Z2K.txt` | `$RMX2Z2K.txt` | 已入回收站 |
| 61 | `.tmp/_ge01_ecr_probe8_out.txt` | 18,519 | `d5051d628807` | `$IP3F6KM.txt` | `$RP3F6KM.txt` | 已入回收站 |
| 62 | `.tmp/_ge01_ecr_probe_out.txt` | 86,220 | `8531ebdb2c9c` | `$IQN7M1F.txt` | `$RQN7M1F.txt` | 已入回收站 |
| 63 | `.tmp/_ge01_ecr_sourcing_archive.txt` | 988 | `547e09add2da` | `$IK8QO71.txt` | `$RK8QO71.txt` | 已入回收站 |
| 64 | `.tmp/_ge01_ecr_sourcing_census.txt` | 5,895 | `da6f97237f4c` | `$I01O24F.txt` | `$R01O24F.txt` | 已入回收站 |
| 65 | `.tmp/_ge01_ecr_sourcing_ctx.txt` | 5,324 | `828c7ebeb270` | `$IT4UA5I.txt` | `$RT4UA5I.txt` | 已入回收站 |
| 66 | `.tmp/_ge01_ecr_sourcing_dumpA.txt` | 8,757 | `e0670450a21e` | `$IBDZ6ZB.txt` | `$RBDZ6ZB.txt` | 已入回收站 |
| 67 | `.tmp/_ge01_ecr_sourcing_dumpB.txt` | 15,362 | `7ff1277ee4f9` | `$IQKR2B9.txt` | `$RQKR2B9.txt` | 已入回收站 |
| 68 | `.tmp/_ge01_ecr_sourcing_extract.txt` | 24,792 | `19881212aa35` | `$IU9QDNP.txt` | `$RU9QDNP.txt` | 已入回收站 |
| 69 | `.tmp/_ge01_ecr_sourcing_gtformal.txt` | 1,682 | `493284935015` | `$IWT257E.txt` | `$RWT257E.txt` | 已入回收站 |
| 70 | `.tmp/_ge01_ecr_sourcing_keys.txt` | 5,879 | `b47f3563d16f` | `$IG7JCD2.txt` | `$RG7JCD2.txt` | 已入回收站 |
| 71 | `.tmp/_ge01_ecr_sourcing_recompute.txt` | 2,911 | `920994c1a364` | `$IUUUYHF.txt` | `$RUUUYHF.txt` | 已入回收站 |
| 72 | `.tmp/_ge01_ecr_sourcing_v4prereg.txt` | 1,626 | `942847227e66` | `$ISZQ5NK.txt` | `$RSZQ5NK.txt` | 已入回收站 |
| 73 | `.tmp/_ge01_ecr_sourcing_v4track.txt` | 38,520 | `c62de09bbde9` | `$I201VUS.txt` | `$R201VUS.txt` | 已入回收站 |
| 74 | `.tmp/_ge01_ecr_sourcing_version.txt` | 5,006 | `a36522d01b21` | `$I6KMOK6.txt` | `$R6KMOK6.txt` | 已入回收站 |
| 75 | `.tmp/_heads.txt` | 1,276 | `573ee1005d85` | `$IPJHFEN.txt` | `$RPJHFEN.txt` | 已入回收站 |
| 76 | `.tmp/_idx1.py` | 1,114 | `4700ce30ca92` | `$ILCAUNU.py` | `$RLCAUNU.py` | 已入回收站 |
| 77 | `.tmp/_idx_probe.py` | 788 | `4c474f0ab1bf` | `$I87EF3A.py` | `$R87EF3A.py` | 已入回收站 |
| 78 | `.tmp/_item_map.txt` | 48,135 | `13ddacba74e9` | `$IYFLIEU.txt` | `$RYFLIEU.txt` | 已入回收站 |
| 79 | `.tmp/_kd13_emit.py` | 34,615 | `3e9c0f4cc072` | `$IP8KNM4.py` | `$RP8KNM4.py` | 已入回收站 |
| 80 | `.tmp/_kd13_probe.py` | 4,212 | `3a7d4aa4ee7c` | `$INJV540.py` | `$RNJV540.py` | 已入回收站 |
| 81 | `.tmp/_kd13_probe2.py` | 6,845 | `5b70135c5b23` | `$IEA0PBE.py` | `$REA0PBE.py` | 已入回收站 |
| 82 | `.tmp/_kd13_probe2_out.txt` | 2,246 | `41be5e82f978` | `$I5BPZV4.txt` | `$R5BPZV4.txt` | 已入回收站 |
| 83 | `.tmp/_kd13_probe_out.txt` | 13,481 | `d6a9ac9c08b7` | `$IV2EBO1.txt` | `$RV2EBO1.txt` | 已入回收站 |
| 84 | `.tmp/_kd13_selfreport.txt` | 757 | `43b2f0c6a267` | `$IIRSQ3T.txt` | `$RIRSQ3T.txt` | 已入回收站 |
| 85 | `.tmp/_kd13_v1_ecr.txt` | 941 | `388df853e3cb` | `$IZAMEIK.txt` | `$RZAMEIK.txt` | 已入回收站 |
| 86 | `.tmp/_kd13_verify.py` | 4,735 | `7d6fc895cf23` | `$I69HUW8.py` | `$R69HUW8.py` | 已入回收站 |
| 87 | `.tmp/_kd13_verify.txt` | 2,773 | `11363670a32a` | `$IPBDAUH.txt` | `$RPBDAUH.txt` | 已入回收站 |
| 88 | `.tmp/_kd_s3_2_3_corrigendum_payload.py` | 27,221 | `5fb6c3f2c6d7` | `$IDN64T7.py` | `$RDN64T7.py` | 已入回收站 |
| 89 | `.tmp/_keyloc.py` | 736 | `f36875c7828e` | `$IH2L887.py` | `$RH2L887.py` | 已入回收站 |
| 90 | `.tmp/_keyloc_out.txt` | 814 | `9d650d0225d5` | `$IV3DUP5.txt` | `$RV3DUP5.txt` | 已入回收站 |
| 91 | `.tmp/_keyscan2.py` | 1,831 | `80628dc5a749` | `$IMS9TA1.py` | `$RMS9TA1.py` | 已入回收站 |
| 92 | `.tmp/_keyscan2_out.txt` | 762 | `3d28b0142ab5` | `$IM95SY1.txt` | `$RM95SY1.txt` | 已入回收站 |
| 93 | `.tmp/_keyscan3.py` | 2,104 | `ba750186821c` | `$ISOGMF7.py` | `$RSOGMF7.py` | 已入回收站 |
| 94 | `.tmp/_keyscan3_out.txt` | 786 | `e46c6d362908` | `$I9WS0PP.txt` | `$R9WS0PP.txt` | 已入回收站 |
| 95 | `.tmp/_kf.py` | 311 | `56fdfb73f99f` | `$IOH7J5H.py` | `$ROH7J5H.py` | 已入回收站 |
| 96 | `.tmp/_land_t2_t3.py` | 920 | `d1135725e933` | `$ILLJT9E.py` | `$RLLJT9E.py` | 已入回收站 |
| 97 | `.tmp/_lit2_raw.txt` | 12,050 | `d8640f48c712` | `$I4MIBJP.txt` | `$R4MIBJP.txt` | 已入回收站 |
| 98 | `.tmp/_m5_decomp_out.txt` | 6,338 | `7721e92ce82e` | `$IATMTQX.txt` | `$RATMTQX.txt` | 已入回收站 |
| 99 | `.tmp/_m5_hunk_out.txt` | 10,820 | `5261971aacbe` | `$IDQ60EL.txt` | `$RDQ60EL.txt` | 已入回收站 |
| 100 | `.tmp/_m5_land_out.txt` | 2,090 | `34e6d27cd542` | `$I2K0TR4.txt` | `$R2K0TR4.txt` | 已入回收站 |
| 101 | `.tmp/_m5_sweep_out.txt` | 3,824 | `6fd5030dd9c8` | `$ID7BXAK.txt` | `$RD7BXAK.txt` | 已入回收站 |
| 102 | `.tmp/_pk_verify.py` | 628 | `2d56fbdf4db8` | `$IICUPNL.py` | `$RICUPNL.py` | 已入回收站 |
| 103 | `.tmp/_pk_write_lock_register.py` | 29,639 | `2601583827b6` | `$IIJI2D5.py` | `$RIJI2D5.py` | 已入回收站 |
| 104 | `.tmp/_pre_mod/__pycache__/exp_harness_pre.cpython-314.pyc` | 35,868 | `ff5f068ce036` | `$I8F8OVM.pyc` | `$R8F8OVM.pyc` | 已入回收站 |
| 105 | `.tmp/_pre_probe1.py` | 1,314 | `4459d3940d6c` | `$IKBI34E.py` | `$RKBI34E.py` | 已入回收站 |
| 106 | `.tmp/_probe10.md` | 77 | `c592c094b6ad` | `$IHJNEZ0.md` | `$RHJNEZ0.md` | 已入回收站 |
| 107 | `.tmp/_probe_roundtrip.txt` | 84 | `a1a709f5b019` | `$IX3O2UC.txt` | `$RX3O2UC.txt` | 已入回收站 |
| 108 | `.tmp/_probe_words.txt` | 44 | `7a967017bbd2` | `$IWBRDZC.txt` | `$RWBRDZC.txt` | 已入回收站 |
| 109 | `.tmp/_reg_v32_append6_2026_10_16.py` | 2,094 | `26880a8b6ea3` | `$ICHAOMR.py` | `$RCHAOMR.py` | 已入回收站 |
| 110 | `.tmp/_reg_v32_probe2_2026_10_16.py` | 2,593 | `71c0ddbb5574` | `$IB6N095.py` | `$RB6N095.py` | 已入回收站 |
| 111 | `.tmp/_reg_v32_probe3_2026_10_16.py` | 2,576 | `9d052912d635` | `$I1LRN5A.py` | `$R1LRN5A.py` | 已入回收站 |
| 112 | `.tmp/_reg_v32_probe4_2026_10_16.py` | 2,327 | `e243f65ad00c` | `$IB67ICX.py` | `$RB67ICX.py` | 已入回收站 |
| 113 | `.tmp/_reg_v32_probe5_2026_10_16.py` | 2,947 | `373e10955bf2` | `$IO3MMWN.py` | `$RO3MMWN.py` | 已入回收站 |
| 114 | `.tmp/_reg_v32_probe_2026_10_16.py` | 4,279 | `93b56fcc52f9` | `$IRL1V58.py` | `$RRL1V58.py` | 已入回收站 |
| 115 | `.tmp/_reg_v32_sec6_2026_10_16.md` | 6,788 | `dfd846fe93ff` | `$ICXM1RU.md` | `$RCXM1RU.md` | 已入回收站 |
| 116 | `.tmp/_reg_v32_staging_2026_10_16.md` | 24,309 | `e23e1b1e520b` | `$I6OJJVY.md` | `$R6OJJVY.md` | 已入回收站 |
| 117 | `.tmp/_reg_v32_write_2026_10_16.py` | 4,199 | `af532505b7a1` | `$ILXPE11.py` | `$RLXPE11.py` | 已入回收站 |
| 118 | `.tmp/_runtime_report.txt` | 5,659 | `bb31895a5454` | `$IH5R2U0.txt` | `$RH5R2U0.txt` | 已入回收站 |
| 119 | `.tmp/_s2_corrigendum_payload.py` | 26,270 | `adedb634495b` | `$IS9JXVM.py` | `$RS9JXVM.py` | 已入回收站 |
| 120 | `.tmp/_s3b_r1_run.log` | 21,580 | `4ac0b69ce6e0` | `$IQUFNXK.log` | `$RQUFNXK.log` | 已入回收站 |
| 121 | `.tmp/_scan_pct.py` | 595 | `eb614598c853` | `$IHD8LU6.py` | `$RHD8LU6.py` | 已入回收站 |
| 122 | `.tmp/_scan_repo.json` | 92,914 | `84b90b209ec5` | `$IFUAEAL.json` | `$RFUAEAL.json` | 已入回收站 |
| 123 | `.tmp/_scan_runtime.json` | 194,993 | `32e1e35b0480` | `$ISZJTRF.json` | `$RSZJTRF.json` | 已入回收站 |
| 124 | `.tmp/_sha_probe_w1.py` | 600 | `ac9957d65d81` | `$I22RAGW.py` | `$R22RAGW.py` | 已入回收站 |
| 125 | `.tmp/_stage_t2_t3.md` | 24,619 | `5e93b0ac8df4` | `$IM8KHOK.md` | `$RM8KHOK.md` | 已入回收站 |
| 126 | `.tmp/_t2_t3_prex_a_route_err.txt` | 0 | `e3b0c44298fc` | `$ITRQ4QN.txt` | `$RTRQ4QN.txt` | 已入回收站 |
| 127 | `.tmp/_t3probe_analyze.py` | 3,144 | `7a8e212ec66d` | `$I3SHDF6.py` | `$R3SHDF6.py` | 已入回收站 |
| 128 | `.tmp/_t3probe_attr1.py` | 1,989 | `8859e5745902` | `$IM0DH7W.py` | `$RM0DH7W.py` | 已入回收站 |
| 129 | `.tmp/_t3probe_attr2.py` | 1,403 | `429a95eba06d` | `$I9BRJ62.py` | `$R9BRJ62.py` | 已入回收站 |
| 130 | `.tmp/_t3probe_attr3.py` | 3,436 | `a8f2ae7e2ff7` | `$IKUNM7V.py` | `$RKUNM7V.py` | 已入回收站 |
| 131 | `.tmp/_t3probe_census.py` | 1,182 | `2f8b5a27e179` | `$ITPB9UI.py` | `$RTPB9UI.py` | 已入回收站 |
| 132 | `.tmp/_t3probe_det.py` | 397 | `3f8fb545da20` | `$ISL5HO8.py` | `$RSL5HO8.py` | 已入回收站 |
| 133 | `.tmp/_t3probe_det2.py` | 1,785 | `8f53a1f58db3` | `$I2ZPYWB.py` | `$R2ZPYWB.py` | 已入回收站 |
| 134 | `.tmp/_t3probe_env.py` | 411 | `53db456f321d` | `$IL1LL5B.py` | `$RL1LL5B.py` | 已入回收站 |
| 135 | `.tmp/_t3probe_final.py` | 3,055 | `469aaafcf3e6` | `$ILYVRWN.py` | `$RLYVRWN.py` | 已入回收站 |
| 136 | `.tmp/_t3probe_frz.py` | 762 | `452000262191` | `$IXV5GFS.py` | `$RXV5GFS.py` | 已入回收站 |
| 137 | `.tmp/_t3probe_frz2.py` | 566 | `d0f6411c64f1` | `$I5LQ08D.py` | `$R5LQ08D.py` | 已入回收站 |
| 138 | `.tmp/_t3probe_ftfb.py` | 3,652 | `fafe20311c7c` | `$IUDPZQ5.py` | `$RUDPZQ5.py` | 已入回收站 |
| 139 | `.tmp/_t3probe_hunk.py` | 861 | `7397bf9d79f9` | `$IEC142E.py` | `$REC142E.py` | 已入回收站 |
| 140 | `.tmp/_t3probe_hunk2.py` | 787 | `139e312f81ae` | `$IWIO5YZ.py` | `$RWIO5YZ.py` | 已入回收站 |
| 141 | `.tmp/_t3probe_hunk3.py` | 537 | `f186d2d9eaf4` | `$IQVFQSO.py` | `$RQVFQSO.py` | 已入回收站 |
| 142 | `.tmp/_t3probe_hunk4.py` | 631 | `f7df3783ddad` | `$IYBQBPY.py` | `$RYBQBPY.py` | 已入回收站 |
| 143 | `.tmp/_t3probe_jsonl.py` | 399 | `9cd2d75b5819` | `$IHLI0EO.py` | `$RHLI0EO.py` | 已入回收站 |
| 144 | `.tmp/_t3probe_layers.py` | 1,845 | `6114b547ae4e` | `$IT5BL5Y.py` | `$RT5BL5Y.py` | 已入回收站 |
| 145 | `.tmp/_t3probe_old.py` | 2,105 | `29c9850b9b0a` | `$I0DGDBQ.py` | `$R0DGDBQ.py` | 已入回收站 |
| 146 | `.tmp/_t3probe_old2.py` | 2,275 | `8655f9495f99` | `$IQ5WM7W.py` | `$RQ5WM7W.py` | 已入回收站 |
| 147 | `.tmp/_t3probe_path.py` | 728 | `6433041ed5e2` | `$I1Z3ZM5.py` | `$R1Z3ZM5.py` | 已入回收站 |
| 148 | `.tmp/_t3probe_peek.py` | 567 | `1c513a778129` | `$IEP6YBD.py` | `$REP6YBD.py` | 已入回收站 |
| 149 | `.tmp/_t3probe_peek2.py` | 744 | `1cbb76a7423b` | `$IIASK57.py` | `$RIASK57.py` | 已入回收站 |
| 150 | `.tmp/_t3probe_rows.py` | 854 | `40292f51bc30` | `$I80RR8G.py` | `$R80RR8G.py` | 已入回收站 |
| 151 | `.tmp/_t3probe_run.py` | 5,044 | `35d662b2d9a6` | `$IKF1WR2.py` | `$RKF1WR2.py` | 已入回收站 |
| 152 | `.tmp/_t3probe_scan1.py` | 920 | `554b4d94118e` | `$IJOKZ37.py` | `$RJOKZ37.py` | 已入回收站 |
| 153 | `.tmp/_t3probe_selfcheck.py` | 1,246 | `977e576bd99d` | `$ISGYM8T.py` | `$RSGYM8T.py` | 已入回收站 |
| 154 | `.tmp/_t3probe_src.py` | 1,199 | `cdde6f432998` | `$IQM1SSS.py` | `$RQM1SSS.py` | 已入回收站 |
| 155 | `.tmp/_t3probe_t3calls.py` | 398 | `262dfbec92c2` | `$IUR8VJ7.py` | `$RUR8VJ7.py` | 已入回收站 |
| 156 | `.tmp/_three_items_judgment_src.md` | 64,073 | `7ec619efdcd4` | `$IY6SJ7C.md` | `$RY6SJ7C.md` | 已入回收站 |
| 157 | `.tmp/_tmp_dump_cmp.py` | 1,684 | `c1b7bd01280a` | `$I5ONTQP.py` | `$R5ONTQP.py` | 已入回收站 |
| 158 | `.tmp/_tmp_dump_tbl.py` | 2,086 | `213dc3a9cdfc` | `$IQ1BUJ5.py` | `$RQ1BUJ5.py` | 已入回收站 |
| 159 | `.tmp/_tmp_dump_v.py` | 2,293 | `f4260aa2fdb4` | `$IOCLF83.py` | `$ROCLF83.py` | 已入回收站 |
| 160 | `.tmp/_tmp_land.py` | 2,084 | `4e4933dce696` | `$I7RLQUD.py` | `$R7RLQUD.py` | 已入回收站 |
| 161 | `.tmp/_verify_t2_t3.py` | 1,684 | `f3a21eaf849c` | `$I9ISV08.py` | `$R9ISV08.py` | 已入回收站 |
| 162 | `.tmp/_w1_anchorprobe.py` | 892 | `63aceb884c3d` | `$IINR68C.py` | `$RINR68C.py` | 已入回收站 |
| 163 | `.tmp/_w1_anchorv2.py` | 334 | `ab52e3ba555b` | `$I3RMQ1A.py` | `$R3RMQ1A.py` | 已入回收站 |
| 164 | `.tmp/_w1_driftprobe.py` | 664 | `d12b2d914220` | `$I2XP4JA.py` | `$R2XP4JA.py` | 已入回收站 |
| 165 | `.tmp/_w1_final_report.py` | 824 | `4a48358ad2bf` | `$IOVV1XN.py` | `$ROVV1XN.py` | 已入回收站 |
| 166 | `.tmp/_w1_keyprobe.py` | 602 | `75988c47fb45` | `$I87T300.py` | `$R87T300.py` | 已入回收站 |
| 167 | `.tmp/_w1_probe_harness.py` | 372 | `764f6074a85a` | `$IFTZHMP.py` | `$RFTZHMP.py` | 已入回收站 |
| 168 | `.tmp/_w1_spot.py` | 486 | `efdba27d997a` | `$IYJ3Y31.py` | `$RYJ3Y31.py` | 已入回收站 |
| 169 | `.tmp/_w1_spot2.py` | 466 | `f2902f2fadf3` | `$IR21TFL.py` | `$RR21TFL.py` | 已入回收站 |
| 170 | `.tmp/_w1_v6probe.py` | 846 | `a0821889ff61` | `$I61NWXC.py` | `$R61NWXC.py` | 已入回收站 |
| 171 | `.tmp/_write_gemini4_reply_verification_register.py` | 34,829 | `d14c965581a6` | `$IBH0J1Q.py` | `$RBH0J1Q.py` | 已入回收站 |
| 172 | `.tmp/_write_u_recalc.py` | 28,811 | `cada2e0fdaab` | `$I6124DT.py` | `$R6124DT.py` | 已入回收站 |
| 173 | `.tmp/anch_v4_stage2_json.py` | 28,350 | `049776685d11` | `$IO93DG9.py` | `$RO93DG9.py` | 已入回收站 |
| 174 | `.tmp/anch_v4_stage2_result.json` | 48 | `6f42f8db527d` | `$IENPIZT.json` | `$RENPIZT.json` | 已入回收站 |
| 175 | `.tmp/anch_v4_stage3_lock.py` | 24,575 | `ce8e9dc56752` | `$IZJEPEW.py` | `$RZJEPEW.py` | 已入回收站 |
| 176 | `.tmp/anch_v4_verify.py` | 7,071 | `2b74debe23ce` | `$IAZSZ57.py` | `$RAZSZ57.py` | 已入回收站 |
| 177 | `.tmp/build_n3_o5_verdict.py` | 39,462 | `4968f1f018f1` | `$I5X7X8O.py` | `$R5X7X8O.py` | 已入回收站 |
| 178 | `.tmp/build_v2_anchor.py` | 18,813 | `147162fce9c2` | `$IS4X9YK.py` | `$RS4X9YK.py` | 已入回收站 |
| 179 | `.tmp/build_v2_lock.py` | 18,536 | `d8f205375a2c` | `$IIKFJP2.py` | `$RIKFJP2.py` | 已入回收站 |
| 180 | `.tmp/build_v3.py` | 19,741 | `ab3742fe3bac` | `$ILJDG1B.py` | `$RLJDG1B.py` | 已入回收站 |
| 181 | `.tmp/build_v3_lock.py` | 18,564 | `75c24b61afc8` | `$IER57JH.py` | `$RER57JH.py` | 已入回收站 |
| 182 | `.tmp/check_memo_drift_2026_10_16.py` | 688 | `60980ff907f3` | `$I8NXPV9.py` | `$R8NXPV9.py` | 已入回收站 |
| 183 | `.tmp/check_quotes.py` | 590 | `f49c18ccbef2` | `$IXT9IVK.py` | `$RXT9IVK.py` | 已入回收站 |
| 184 | `.tmp/d1_judgment_build.py` | 50,302 | `d9c9013097c0` | `$IJTSMB8.py` | `$RJTSMB8.py` | 已入回收站 |
| 185 | `.tmp/docwriter_c5_selfcheck.json` | 343 | `6fc6184060a8` | `$IROIGPO.json` | `$RROIGPO.json` | 已入回收站 |
| 186 | `.tmp/docwriter_debug_block.py` | 754 | `b93c99b2ef51` | `$IW1QOEY.py` | `$RW1QOEY.py` | 已入回收站 |
| 187 | `.tmp/docwriter_final_verify.py` | 3,763 | `d5d8e2048b07` | `$ISX70NE.py` | `$RSX70NE.py` | 已入回收站 |
| 188 | `.tmp/docwriter_v41_probe_err.txt` | 0 | `e3b0c44298fc` | `$ISMWM09.txt` | `$RSMWM09.txt` | 已入回收站 |
| 189 | `.tmp/docwriter_v41_probe_out.json` | 861,900 | `6e559e1ee253` | `$IBZFZ4K.json` | `$RBZFZ4K.json` | 已入回收站 |
| 190 | `.tmp/docwriter_v41_verify.py` | 3,378 | `d98932573850` | `$IBSI8RJ.py` | `$RBSI8RJ.py` | 已入回收站 |
| 191 | `.tmp/docwriter_write_u1494.py` | 44,307 | `0485d86b7746` | `$II9GCYK.py` | `$RI9GCYK.py` | 已入回收站 |
| 192 | `.tmp/docwriter_write_v41.py` | 44,021 | `c6ce0ac23598` | `$IAC9T2S.py` | `$RAC9T2S.py` | 已入回收站 |
| 193 | `.tmp/dscan_final.txt` | 461 | `677116ad017c` | `$I160IEH.txt` | `$R160IEH.txt` | 已入回收站 |
| 194 | `.tmp/dscan_repo_exec_result.txt` | 1,774 | `65abea802cd9` | `$IRGU40D.txt` | `$RRGU40D.txt` | 已入回收站 |
| 195 | `.tmp/dscan_repo_exec_summary.json` | 2,714 | `2e179f2d1d4b` | `$IYRPCWX.json` | `$RYRPCWX.json` | 已入回收站 |
| 196 | `.tmp/dw_reg_v28_normalize_2026_10_16.py` | 2,968 | `735586971318` | `$ISAK9WH.py` | `$RSAK9WH.py` | 已入回收站 |
| 197 | `.tmp/ea_cand.json` | 52,982 | `1853c54e1130` | `$IB5SF0X.json` | `$RB5SF0X.json` | 已入回收站 |
| 198 | `.tmp/ea_cand14.json` | 20,815 | `656a8483cd18` | `$IQ9MDOF.json` | `$RQ9MDOF.json` | 已入回收站 |
| 199 | `.tmp/ea_find_targets.py` | 1,358 | `41bf57479a30` | `$ISUMYR3.py` | `$RSUMYR3.py` | 已入回收站 |
| 200 | `.tmp/ea_probe.py` | 3,052 | `19560d996179` | `$I38HHHC.py` | `$R38HHHC.py` | 已入回收站 |
| 201 | `.tmp/ea_roles.json` | 89,853 | `c893e9d84f50` | `$IYKFV5H.json` | `$RYKFV5H.json` | 已入回收站 |
| 202 | `.tmp/ea_verify_after.py` | 5,891 | `b642ebc7e3ed` | `$IKRJIE6.py` | `$RKRJIE6.py` | 已入回收站 |
| 203 | `.tmp/ea_verify_sources.py` | 1,283 | `025fb2f7345d` | `$I677HBG.py` | `$R677HBG.py` | 已入回收站 |
| 204 | `.tmp/ea_write_deliverables.py` | 35,742 | `10bd3a54f21b` | `$IR7L9QL.py` | `$RR7L9QL.py` | 已入回收站 |
| 205 | `.tmp/final_audit.py` | 4,136 | `d0c9cdbd8da6` | `$IM89MMZ.py` | `$RM89MMZ.py` | 已入回收站 |
| 206 | `.tmp/final_out.txt` | 2,142 | `8cd17147e240` | `$ICKDNRS.txt` | `$RCKDNRS.txt` | 已入回收站 |
| 207 | `.tmp/gamma_taucert_recursion.py` | 2,256 | `68251f1418b1` | `$IKY4QL0.py` | `$RKY4QL0.py` | 已入回收站 |
| 208 | `.tmp/gamma_taucert_stage2.py` | 2,619 | `f67eeeeaaf9f` | `$IOO7FS0.py` | `$ROO7FS0.py` | 已入回收站 |
| 209 | `.tmp/gamma_taucert_stage3.py` | 2,802 | `53fe4853a3a3` | `$IAN0YRY.py` | `$RAN0YRY.py` | 已入回收站 |
| 210 | `.tmp/gamma_taucert_verify.py` | 1,274 | `bfad0adbb7a4` | `$IZJOWGN.py` | `$RZJOWGN.py` | 已入回收站 |
| 211 | `.tmp/ge01_full_1494_write_md_2026_10_16.py` | 33,337 | `5c92ccdf8cbe` | `$IB347Z2.py` | `$RB347Z2.py` | 已入回收站 |
| 212 | `.tmp/ge01_s3_byteself_2026_10_16.py` | 3,435 | `1cde2cd14af6` | `$ICB48V1.py` | `$RCB48V1.py` | 已入回收站 |
| 213 | `.tmp/ge01_s3b_probe_2026_10_16.py` | 1,255 | `945a3e763796` | `$IHDFH1B.py` | `$RHDFH1B.py` | 已入回收站 |
| 214 | `.tmp/ge01b.py` | 570 | `a351d50116f2` | `$IJQPMPE.py` | `$RJQPMPE.py` | 已入回收站 |
| 215 | `.tmp/ge02_check.py` | 1,054 | `4eac36c11811` | `$IKZ22LU.py` | `$RKZ22LU.py` | 已入回收站 |
| 216 | `.tmp/ge02_final.py` | 1,842 | `cdb4afcff9c4` | `$INHQTGX.py` | `$RNHQTGX.py` | 已入回收站 |
| 217 | `.tmp/ge02_keys.py` | 500 | `8dcc98f7f829` | `$IX878SM.py` | `$RX878SM.py` | 已入回收站 |
| 218 | `.tmp/gen_deliverable.py` | 33,928 | `a9c505ff3d2a` | `$I90KZPC.py` | `$R90KZPC.py` | 已入回收站 |
| 219 | `.tmp/gen_kd14_carrier_deliberation.py` | 37,481 | `50ac53ae50b3` | `$IP00FIU.py` | `$RP00FIU.py` | 已入回收站 |
| 220 | `.tmp/gen_reg_v38_axis_effect_2026_10_16.py` | 19,960 | `98f0a3fd7c58` | `$IWTXUST.py` | `$RWTXUST.py` | 已入回收站 |
| 221 | `.tmp/gen_reg_v38_register_2026_10_16.py` | 23,987 | `ba4cf7bd34a2` | `$I1LMFTI.py` | `$R1LMFTI.py` | 已入回收站 |
| 222 | `.tmp/gen_u_axis_direction_deliberation_2026_10_16.py` | 38,737 | `87aa54dfe1fc` | `$IYQRE2X.py` | `$RYQRE2X.py` | 已入回收站 |
| 223 | `.tmp/h_ecr.py` | 1,053 | `ab75b709d50d` | `$I5S3KUD.py` | `$R5S3KUD.py` | 已入回收站 |
| 224 | `.tmp/h_ecr2.py` | 702 | `875835f24e5e` | `$I7TX2XL.py` | `$R7TX2XL.py` | 已入回收站 |
| 225 | `.tmp/h_src2.py` | 558 | `f16067beeeea` | `$IZB1SVU.py` | `$RZB1SVU.py` | 已入回收站 |
| 226 | `.tmp/klm41_2_accept_check_2026_10_16.py` | 3,400 | `d035dd778940` | `$IFOJD1I.py` | `$RFOJD1I.py` | 已入回收站 |
| 227 | `.tmp/klm41_3_ts_agg_2026_10_16.py` | 2,857 | `c166350e1753` | `$IFT45QP.py` | `$RFT45QP.py` | 已入回收站 |
| 228 | `.tmp/klm41_3_ts_byteself_2026_10_16.py` | 3,039 | `c681898eac9b` | `$I3Y3TRO.py` | `$R3Y3TRO.py` | 已入回收站 |
| 229 | `.tmp/klm41_3_ts_ctrlcal.py` | 740 | `542d2ec5f0b5` | `$ISXWXFZ.py` | `$RSXWXFZ.py` | 已入回收站 |
| 230 | `.tmp/klm41_3_ts_diffcheck.py` | 1,633 | `e4ba8c0c305e` | `$I552N31.py` | `$R552N31.py` | 已入回收站 |
| 231 | `.tmp/klm41_3_ts_freeze_write_2026_10_16.py` | 7,755 | `e8abd8ad0df5` | `$IJ1XI0Z.py` | `$RJ1XI0Z.py` | 已入回收站 |
| 232 | `.tmp/klm41_3_ts_write_2026_10_16.py` | 32,336 | `9871f22d32af` | `$IY5RXLS.py` | `$RY5RXLS.py` | 已入回收站 |
| 233 | `.tmp/loc2.py` | 735 | `2097168a4c53` | `$ICII2ET.py` | `$RCII2ET.py` | 已入回收站 |
| 234 | `.tmp/loc3.py` | 653 | `ff8b543ad105` | `$IDE4UC1.py` | `$RDE4UC1.py` | 已入回收站 |
| 235 | `.tmp/loc4.py` | 496 | `8f9978e89bbf` | `$IRZ5YLB.py` | `$RRZ5YLB.py` | 已入回收站 |
| 236 | `.tmp/m08_boundary_2026_10_16.json` | 1,662 | `b8fe6ab59208` | `$IRWT57Z.json` | `$RRWT57Z.json` | 已入回收站 |
| 237 | `.tmp/m08_boundary_2026_10_16.py` | 2,810 | `5ac7a7dcce75` | `$ILBOCBS.py` | `$RLBOCBS.py` | 已入回收站 |
| 238 | `.tmp/m08_enum_2026_10_16.json` | 15,049 | `f6e6bec76fc3` | `$IROYZM2.json` | `$RROYZM2.json` | 已入回收站 |
| 239 | `.tmp/m08_enum_2026_10_16.py` | 9,311 | `43af2e0ec6e4` | `$I6UQZAP.py` | `$R6UQZAP.py` | 已入回收站 |
| 240 | `.tmp/m08_llm_arm_2026_10_16.json` | 3,479 | `06f8ac063105` | `$IFQG2WI.json` | `$RFQG2WI.json` | 已入回收站 |
| 241 | `.tmp/m08_llm_arm_2026_10_16.py` | 5,568 | `fa35d870c9be` | `$I3EVUSU.py` | `$R3EVUSU.py` | 已入回收站 |
| 242 | `.tmp/m08_llm_arm_calls_2026_10_16.jsonl` | 7,167 | `ca5f6e8198a1` | `$I927NJJ.jsonl` | `$R927NJJ.jsonl` | 已入回收站 |
| 243 | `.tmp/m08_llm_arm_perm_2026_10_16.json` | 4,319 | `25af9ef9009c` | `$I8CNX53.json` | `$R8CNX53.json` | 已入回收站 |
| 244 | `.tmp/m08_llm_arm_perm_2026_10_16.py` | 5,728 | `9db926fbbff2` | `$ITBWH5G.py` | `$RTBWH5G.py` | 已入回收站 |
| 245 | `.tmp/m08_llm_probe.py` | 3,334 | `108a5fc1f597` | `$IRIZ3SJ.py` | `$RRIZ3SJ.py` | 已入回收站 |
| 246 | `.tmp/m08_llm_probe_2026_10_16.json` | 1,598 | `3488d16f3efe` | `$IQP413L.json` | `$RQP413L.json` | 已入回收站 |
| 247 | `.tmp/m08_r1_verify_2026_10_16.json` | 5,650 | `3cafa1153b07` | `$IKJEM25.json` | `$RKJEM25.json` | 已入回收站 |
| 248 | `.tmp/m08_r1_verify_2026_10_16.py` | 8,577 | `9ae320d3f65f` | `$IWK2DO4.py` | `$RWK2DO4.py` | 已入回收站 |
| 249 | `.tmp/m08_src_sha.py` | 2,341 | `af2a193d546d` | `$IV8Z81G.py` | `$RV8Z81G.py` | 已入回收站 |
| 250 | `.tmp/m08_src_sha_2026_10_16.json` | 1,990 | `64e7163e0d13` | `$I9L0J09.json` | `$R9L0J09.json` | 已入回收站 |
| 251 | `.tmp/m2_measure_out.txt` | 1,808 | `9812d4adcaa5` | `$IHZMMZY.txt` | `$RHZMMZY.txt` | 已入回收站 |
| 252 | `.tmp/m2_probe2_out.json` | 5,227 | `162a9419b037` | `$IHFU1LB.json` | `$RHFU1LB.json` | 已入回收站 |
| 253 | `.tmp/m2_probe3_out.json` | 559 | `9f93ad25606c` | `$IPJ66Q4.json` | `$RPJ66Q4.json` | 已入回收站 |
| 254 | `.tmp/m2_probe4_out.json` | 1,678 | `ff37a1576b76` | `$IMEZN8X.json` | `$RMEZN8X.json` | 已入回收站 |
| 255 | `.tmp/m2_probe5_out.json` | 942 | `948aea324bdd` | `$IJZF8XC.json` | `$RJZF8XC.json` | 已入回收站 |
| 256 | `.tmp/m2_probe6_out.json` | 43,930 | `c4a1990c9f8d` | `$I66EN52.json` | `$R66EN52.json` | 已入回收站 |
| 257 | `.tmp/m2_probe7_out.json` | 10,013 | `0571f07c0fdf` | `$ITCA8HN.json` | `$RTCA8HN.json` | 已入回收站 |
| 258 | `.tmp/m2_probe_err2.txt` | 1,692 | `c11fe104a0e5` | `$IJVZ01I.txt` | `$RJVZ01I.txt` | 已入回收站 |
| 259 | `.tmp/m2_probe_out.json` | 2,830 | `c0856f2261cd` | `$I3HHKXM.json` | `$R3HHKXM.json` | 已入回收站 |
| 260 | `.tmp/m2_probe_out2.txt` | 10,266 | `3d694531b9da` | `$IJ3TJZ8.txt` | `$RJ3TJZ8.txt` | 已入回收站 |
| 261 | `.tmp/m2_probe_out3.txt` | 898 | `82d2ca6917e7` | `$IHAZYH7.txt` | `$RHAZYH7.txt` | 已入回收站 |
| 262 | `.tmp/m2_verify_out.txt` | 948 | `3c7876b1197f` | `$IU3XYML.txt` | `$RU3XYML.txt` | 已入回收站 |
| 263 | `.tmp/m2_verify_out2.txt` | 948 | `afcfeab17341` | `$IMEAFLJ.txt` | `$RMEAFLJ.txt` | 已入回收站 |
| 264 | `.tmp/m2_write_out.txt` | 612 | `d209e129e977` | `$I1RP171.txt` | `$R1RP171.txt` | 已入回收站 |
| 265 | `.tmp/m2verdict_lines_report.txt` | 14,366 | `81c20b9c3110` | `$I83HLKP.txt` | `$R83HLKP.txt` | 已入回收站 |
| 266 | `.tmp/m41_r15_audit.py` | 3,192 | `f6c67969b5ce` | `$IZZ1J17.py` | `$RZZ1J17.py` | 已入回收站 |
| 267 | `.tmp/m41_r15_write_doc.py` | 23,616 | `a0ce44a8dfdf` | `$IV2UE5I.py` | `$RV2UE5I.py` | 已入回收站 |
| 268 | `.tmp/me_census_2026_10_16.py` | 2,176 | `6e64fe18a183` | `$I71CDN7.py` | `$R71CDN7.py` | 已入回收站 |
| 269 | `.tmp/me_census_post_2026_10_16.json` | 88,364 | `99512bcce87d` | `$IQYSB7G.json` | `$RQYSB7G.json` | 已入回收站 |
| 270 | `.tmp/me_census_pre_2026_10_16.json` | 88,197 | `b06f7ae2c313` | `$I5VONVH.json` | `$R5VONVH.json` | 已入回收站 |
| 271 | `.tmp/me_construct_census_2026_10_16.json` | 9,470 | `53a1afce2093` | `$IOU2N8A.json` | `$ROU2N8A.json` | 已入回收站 |
| 272 | `.tmp/me_construct_census_2026_10_16.py` | 8,224 | `ffa8297e0fe5` | `$ILMJIYX.py` | `$RLMJIYX.py` | 已入回收站 |
| 273 | `.tmp/me_final_verify_2026_10_16.py` | 6,620 | `d94b604e9dd9` | `$IOEQP0S.py` | `$ROEQP0S.py` | 已入回收站 |
| 274 | `.tmp/me_freeze_2026_10_16.py` | 21,119 | `674efba35991` | `$IEQZGD6.py` | `$REQZGD6.py` | 已入回收站 |
| 275 | `.tmp/me_harness_hunks_2026_10_16.json` | 1,368 | `4c4f4708991a` | `$IGGCCPO.json` | `$RGGCCPO.json` | 已入回收站 |
| 276 | `.tmp/me_measure_2026_10_16.py` | 16,203 | `5d76ac24a658` | `$IP14J37.py` | `$RP14J37.py` | 已入回收站 |
| 277 | `.tmp/me_patch_harness_2026_10_16.py` | 30,657 | `cfde1a0d83de` | `$INWKSAC.py` | `$RNWKSAC.py` | 已入回收站 |
| 278 | `.tmp/me_write_docs_2026_10_16.py` | 63,363 | `cd55f8e738a7` | `$IQNOULU.py` | `$RQNOULU.py` | 已入回收站 |
| 279 | `.tmp/mq04_verify_disk_2026_10_15.py` | 2,203 | `b76e35f97f59` | `$I743AIV.py` | `$R743AIV.py` | 已入回收站 |
| 280 | `.tmp/mq19i6_anchors.pkl` | 132,519 | `84c436875595` | `$IBWT4XV.pkl` | `$RBWT4XV.pkl` | 已入回收站 |
| 281 | `.tmp/mq19i6_digest_index.pkl` | 10,614,428 | `754f1f2c0cc1` | `$IL4EVI4.pkl` | `$RL4EVI4.pkl` | 已入回收站 |
| 282 | `.tmp/mq19i6_final.pkl` | 191,403 | `75c0b7e05828` | `$I95FD5C.pkl` | `$R95FD5C.pkl` | 已入回收站 |
| 283 | `.tmp/mq19i6_inventory.pkl` | 4,326,911 | `c7da3ec2a062` | `$I7L537P.pkl` | `$R7L537P.pkl` | 已入回收站 |
| 284 | `.tmp/mq19i6_retest.pkl` | 535 | `553c84ce526c` | `$I9Y503O.pkl` | `$R9Y503O.pkl` | 已入回收站 |
| 285 | `.tmp/mq19i6_rows.pkl` | 207,479 | `6ea425946ea0` | `$IF8WJ7J.pkl` | `$RF8WJ7J.pkl` | 已入回收站 |
| 286 | `.tmp/mq19i6_s1_summary.txt` | 631 | `4a1e996d9086` | `$I5QE3GK.txt` | `$R5QE3GK.txt` | 已入回收站 |
| 287 | `.tmp/mq19i6_verdicts.pkl` | 152,881 | `12bcd3f69d28` | `$IB7T87M.pkl` | `$RB7T87M.pkl` | 已入回收站 |
| 288 | `.tmp/nashpy_normal_form_games.rst` | 12,381 | `5870416973b6` | `$IQ1EUNN.rst` | `$RQ1EUNN.rst` | 已入回收站 |
| 289 | `.tmp/numaudit_20261013` | 0 | `（空目录）` | `$I5UU4UL` | `$R5UU4UL` | 已入回收站（空目录·事后验真） |
| 290 | `.tmp/o1_arith_check.py` | 1,673 | `9d0caf1c1596` | `$IVAP46D.py` | `$RVAP46D.py` | 已入回收站 |
| 291 | `.tmp/o1_arith_check2.py` | 1,406 | `7f9c747b709d` | `$IE9F5PZ.py` | `$RE9F5PZ.py` | 已入回收站 |
| 292 | `.tmp/o1_caiying_u_compute_2026_10_16.py` | 4,669 | `c000fbc1daa8` | `$IXK8Y3F.py` | `$RXK8Y3F.py` | 已入回收站 |
| 293 | `.tmp/o1_final_verify2_2026_10_16.py` | 3,235 | `8927845d9cd7` | `$IHM2LDN.py` | `$RHM2LDN.py` | 已入回收站 |
| 294 | `.tmp/o1_final_verify_2026_10_16.py` | 4,242 | `2050a43a475d` | `$IKHRE3P.py` | `$RKHRE3P.py` | 已入回收站 |
| 295 | `.tmp/o1_fix_d5_mojibake_2026_10_16.py` | 1,256 | `086dd86b07d7` | `$IKKX5CD.py` | `$RKKX5CD.py` | 已入回收站 |
| 296 | `.tmp/o1_sha_scan.py` | 933 | `37944914d465` | `$IBW1R9H.py` | `$RBW1R9H.py` | 已入回收站 |
| 297 | `.tmp/o1_verify_2026_10_16.py` | 3,026 | `ddeddb253a24` | `$IFJ5VRX.py` | `$RFJ5VRX.py` | 已入回收站 |
| 298 | `.tmp/o1_verify_probe.py` | 2,695 | `f668d287956f` | `$IMI4UOT.py` | `$RMI4UOT.py` | 已入回收站 |
| 299 | `.tmp/o1_write_2026_10_16.py` | 53,281 | `f589b7b0ee56` | `$I14O4B3.py` | `$R14O4B3.py` | 已入回收站 |
| 300 | `.tmp/pk33q_precheck.py` | 1,152 | `d8d5e4938fc5` | `$IW134ZM.py` | `$RW134ZM.py` | 已入回收站 |
| 301 | `.tmp/pk33q_write.py` | 2,813 | `c66fdfc06f59` | `$I7ADN42.py` | `$R7ADN42.py` | 已入回收站 |
| 302 | `.tmp/pk_anchor_verify.txt` | 260 | `59ed48cc5149` | `$ITP0OSU.txt` | `$RTP0OSU.txt` | 已入回收站 |
| 303 | `.tmp/pk_anchor_verify_20261016.py` | 878 | `f906865ed630` | `$IXU35MC.py` | `$RXU35MC.py` | 已入回收站 |
| 304 | `.tmp/pk_glm_hash_20261016.py` | 1,282 | `d12f1011d301` | `$IL88I6I.py` | `$RL88I6I.py` | 已入回收站 |
| 305 | `.tmp/pk_glm_hash_out.txt` | 121 | `8450ab2e54a5` | `$IQC32KW.txt` | `$RQC32KW.txt` | 已入回收站 |
| 306 | `.tmp/pk_hash_map_20261016.py` | 1,417 | `b31273fc7e58` | `$ILLU9W1.py` | `$RLLU9W1.py` | 已入回收站 |
| 307 | `.tmp/pk_hash_map_out.txt` | 647 | `4b5122117f88` | `$IIV2XPN.txt` | `$RIV2XPN.txt` | 已入回收站 |
| 308 | `.tmp/pk_lockv2_postcheck_2026_10_15.json` | 1,062 | `4c10652a2f77` | `$ITZM365.json` | `$RTZM365.json` | 已入回收站 |
| 309 | `.tmp/pk_lockv2_postcheck_2026_10_15.py` | 3,994 | `bd38f9f0cf71` | `$IXH6283.py` | `$RXH6283.py` | 已入回收站 |
| 310 | `.tmp/pk_selfreport_20261016.txt` | 1,348 | `06ae586bde64` | `$IHM45LE.txt` | `$RHM45LE.txt` | 已入回收站 |
| 311 | `.tmp/pk_t5lock_write_report_2026_10_15.json` | 1,820 | `2bb4721c475b` | `$I788VCT.json` | `$R788VCT.json` | 已入回收站 |
| 312 | `.tmp/pk_u3334_hash_report_20261016.txt` | 612 | `993ac62563f4` | `$IQT61Z1.txt` | `$RQT61Z1.txt` | 已入回收站 |
| 313 | `.tmp/pk_u3334_hash_verify_20261016.py` | 1,297 | `3cf751a68ced` | `$I0YOW0C.py` | `$R0YOW0C.py` | 已入回收站 |
| 314 | `.tmp/pk_u3334_panel_check_20261016.py` | 1,182 | `f655261eb41b` | `$I2UAJOG.py` | `$R2UAJOG.py` | 已入回收站 |
| 315 | `.tmp/pk_u3334_panel_check_20261016.txt` | 295 | `2b8bad35a540` | `$IWGESWK.txt` | `$RWGESWK.txt` | 已入回收站 |
| 316 | `.tmp/pk_u3334_recompute_20261016.py` | 2,516 | `234a79c841bd` | `$IO3YEFK.py` | `$RO3YEFK.py` | 已入回收站 |
| 317 | `.tmp/pk_u3334_recompute_20261016.txt` | 1,491 | `a6b4be97225f` | `$I3YZ4X6.txt` | `$R3YZ4X6.txt` | 已入回收站 |
| 318 | `.tmp/pk_u3334_verify_20261016.py` | 3,113 | `f9cf85807a29` | `$IECGRVW.py` | `$RECGRVW.py` | 已入回收站 |
| 319 | `.tmp/pk_u3334_verify_20261016.txt` | 780 | `b6eedc174012` | `$IQMYIHI.txt` | `$RQMYIHI.txt` | 已入回收站 |
| 320 | `.tmp/pk_u3334_write_20261016.py` | 29,322 | `b7d65bb95ea7` | `$I6C8L1Q.py` | `$R6C8L1Q.py` | 已入回收站 |
| 321 | `.tmp/pk_verify_effect_register_20261016.py` | 2,839 | `59c30f342362` | `$I71D72P.py` | `$R71D72P.py` | 已入回收站 |
| 322 | `.tmp/pk_verify_final_2026_10_16.py` | 3,456 | `69a69f6e9da5` | `$I9K4DUC.py` | `$R9K4DUC.py` | 已入回收站 |
| 323 | `.tmp/pk_write_effect_register_20261016.py` | 32,199 | `d6dab1351db9` | `$IR4X9BQ.py` | `$RR4X9BQ.py` | 已入回收站 |
| 324 | `.tmp/probe11.err` | 0 | `e3b0c44298fc` | `$I4IWOB7.err` | `$R4IWOB7.err` | 已入回收站 |
| 325 | `.tmp/probe11.log` | 29 | `375c87e52511` | `$IBSSUK5.log` | `$RBSSUK5.log` | 已入回收站 |
| 326 | `.tmp/probe4_out.txt` | 8,417 | `e41753d347c6` | `$I9DEPL8.txt` | `$R9DEPL8.txt` | 已入回收站 |
| 327 | `.tmp/probe5_out.txt` | 6,397 | `861f09ac01c2` | `$I0BA9FQ.txt` | `$R0BA9FQ.txt` | 已入回收站 |
| 328 | `.tmp/probe6_out.txt` | 3,749 | `16e2f8ac7364` | `$IYA1VZS.txt` | `$RYA1VZS.txt` | 已入回收站 |
| 329 | `.tmp/probe7_out.txt` | 8,015 | `7d57d43b3e51` | `$IMT8XAI.txt` | `$RMT8XAI.txt` | 已入回收站 |
| 330 | `.tmp/probe8_out.txt` | 1,322 | `2ad32aca80a6` | `$I1YDLEM.txt` | `$R1YDLEM.txt` | 已入回收站 |
| 331 | `.tmp/probe9_out.txt` | 1,990 | `41a82bab4d83` | `$IDL5GPE.txt` | `$RDL5GPE.txt` | 已入回收站 |
| 332 | `.tmp/probe_anchors_2026_10_16.py` | 1,746 | `35e266592819` | `$I6PGNDV.py` | `$R6PGNDV.py` | 已入回收站 |
| 333 | `.tmp/r461_combos.json` | 467 | `86881a39436b` | `$IK1BK9N.json` | `$RK1BK9N.json` | 已入回收站 |
| 334 | `.tmp/r461_perfile.json` | 101,289 | `0629bf16b893` | `$IKFEE14.json` | `$RKFEE14.json` | 已入回收站 |
| 335 | `.tmp/r461_perfile_asof.json` | 94,355 | `4bd95f8cfb25` | `$IK396AF.json` | `$RK396AF.json` | 已入回收站 |
| 336 | `.tmp/r461_probe06.txt` | 10,156 | `e6c566d26edd` | `$IZR3INK.txt` | `$RZR3INK.txt` | 已入回收站 |
| 337 | `.tmp/r461_probe07.txt` | 437 | `b64c1a7f432b` | `$ID6J4CF.txt` | `$RD6J4CF.txt` | 已入回收站 |
| 338 | `.tmp/r461_probe08.txt` | 3,303 | `74f7494fa214` | `$IYDEZOM.txt` | `$RYDEZOM.txt` | 已入回收站 |
| 339 | `.tmp/r461_probe10.txt` | 372 | `36e84117e673` | `$IXH6UBN.txt` | `$RXH6UBN.txt` | 已入回收站 |
| 340 | `.tmp/r461_probe11.txt` | 8,646 | `0c50a7661fea` | `$IC7NWO9.txt` | `$RC7NWO9.txt` | 已入回收站 |
| 341 | `.tmp/r461_probe12.txt` | 5,974 | `5c28c166bb78` | `$IG0Q0X2.txt` | `$RG0Q0X2.txt` | 已入回收站 |
| 342 | `.tmp/r461_probe13.txt` | 12,390 | `9344b7be3ebb` | `$IVYJQHN.txt` | `$RVYJQHN.txt` | 已入回收站 |
| 343 | `.tmp/r461_probe14.txt` | 2,084 | `7a3bbe9d2dcc` | `$IVPBYCR.txt` | `$RVPBYCR.txt` | 已入回收站 |
| 344 | `.tmp/r461_probe15.txt` | 3,217 | `946f76f1fc4e` | `$IXL4H1Y.txt` | `$RXL4H1Y.txt` | 已入回收站 |
| 345 | `.tmp/r461_probe16.txt` | 3,875 | `f9d8c648881c` | `$I7H9ZMC.txt` | `$R7H9ZMC.txt` | 已入回收站 |
| 346 | `.tmp/r461_probe17.txt` | 711 | `edd08d764e74` | `$IZQ2ZIG.txt` | `$RZQ2ZIG.txt` | 已入回收站 |
| 347 | `.tmp/r461_probe18.txt` | 1,780 | `1554066ec0f8` | `$II5LDCK.txt` | `$RI5LDCK.txt` | 已入回收站 |
| 348 | `.tmp/r6_supp_fv_body_draft.md` | 59 | `17f058e2f28d` | `$IHMGTOB.md` | `$RHMGTOB.md` | 已入回收站 |
| 349 | `.tmp/reg_v27_adopt_write.py` | 32,788 | `92d3914037e5` | `$IJHNU6P.py` | `$RJHNU6P.py` | 已入回收站 |
| 350 | `.tmp/reg_v31_write_1.py` | 38,140 | `9e937104e6b6` | `$IYU8B8X.py` | `$RYU8B8X.py` | 已入回收站 |
| 351 | `.tmp/reg_v31_write_2.py` | 52,274 | `fabd6d7a9361` | `$IM77HIH.py` | `$RM77HIH.py` | 已入回收站 |
| 352 | `.tmp/reg_v36_precheck_2026_10_16.py` | 3,355 | `f69ff63db2fd` | `$IZQMNH8.py` | `$RZQMNH8.py` | 已入回收站 |
| 353 | `.tmp/reg_v36_verify_2026_10_16.py` | 3,061 | `647c8cd706b0` | `$I3LR7R8.py` | `$R3LR7R8.py` | 已入回收站 |
| 354 | `.tmp/reg_v36_write_2026_10_16.py` | 71,901 | `a6d33b79eb42` | `$I7FA57Z.py` | `$R7FA57Z.py` | 已入回收站 |
| 355 | `.tmp/reg_v38_scan_2026_10_16.py` | 4,166 | `249cc004cd0a` | `$IKK95IB.py` | `$RKK95IB.py` | 已入回收站 |
| 356 | `.tmp/reg_v38_scan_result_2026_10_16.json` | 4,400 | `4914e95f523e` | `$IU35K44.json` | `$RU35K44.json` | 已入回收站 |
| 357 | `.tmp/rt_check.py` | 654 | `193da5917a4f` | `$IML1TQX.py` | `$RML1TQX.py` | 已入回收站 |
| 358 | `.tmp/scan_doubled.py` | 1,098 | `0e0d7e5edca3` | `$IYTEEZF.py` | `$RYTEEZF.py` | 已入回收站 |
| 359 | `.tmp/scan_sha.py` | 830 | `4220df4af334` | `$I6U8YL3.py` | `$R6U8YL3.py` | 已入回收站 |
| 360 | `.tmp/scout1.py` | 1,716 | `2ffd86d567cb` | `$IMSEFOF.py` | `$RMSEFOF.py` | 已入回收站 |
| 361 | `.tmp/scout2.py` | 3,001 | `cd32e4cf02ff` | `$I3S8FKU.py` | `$R3S8FKU.py` | 已入回收站 |
| 362 | `.tmp/scout2_findings.md` | 9,453 | `af207b067524` | `$IZHYQVJ.md` | `$RZHYQVJ.md` | 已入回收站 |
| 363 | `.tmp/scout3.py` | 2,735 | `1b2c7dc66074` | `$IV7CJUX.py` | `$RV7CJUX.py` | 已入回收站 |
| 364 | `.tmp/scout3_findings.md` | 10,193 | `26bfd840f88d` | `$IWKJR3Z.md` | `$RWKJR3Z.md` | 已入回收站 |
| 365 | `.tmp/scout4.py` | 3,465 | `7dfe45b233da` | `$I2OJ4JR.py` | `$R2OJ4JR.py` | 已入回收站 |
| 366 | `.tmp/scout4_findings.md` | 2,035 | `d8a366edcbf5` | `$IIQZV46.md` | `$RIQZV46.md` | 已入回收站 |
| 367 | `.tmp/scout5.py` | 2,136 | `9bf848146012` | `$IXWV0EP.py` | `$RXWV0EP.py` | 已入回收站 |
| 368 | `.tmp/scout5_findings.md` | 1,016 | `374db5178ad9` | `$INJE2HO.md` | `$RNJE2HO.md` | 已入回收站 |
| 369 | `.tmp/scout6.py` | 3,023 | `349f2d203b96` | `$IPWHK2S.py` | `$RPWHK2S.py` | 已入回收站 |
| 370 | `.tmp/scout6_findings.md` | 5,343 | `34bc36b5d744` | `$IHO9YP9.md` | `$RHO9YP9.md` | 已入回收站 |
| 371 | `.tmp/scout7.py` | 3,437 | `ff36e30bd910` | `$IXEPOD4.py` | `$RXEPOD4.py` | 已入回收站 |
| 372 | `.tmp/scout7_findings.md` | 751 | `f4d3f7d88a43` | `$I1RCY9E.md` | `$R1RCY9E.md` | 已入回收站 |
| 373 | `.tmp/sqa_sample.json` | 22,373 | `e870aa641631` | `$I2GXQ6D.json` | `$R2GXQ6D.json` | 已入回收站 |
| 374 | `.tmp/t2b_census_post_2026_10_16.json` | 117,196 | `e6df31e1eb38` | `$I9AX0TK.json` | `$R9AX0TK.json` | 已入回收站 |
| 375 | `.tmp/t2b_diagnose2_2026_10_16.py` | 2,382 | `d769c3a12750` | `$IUUD2YN.py` | `$RUUD2YN.py` | 已入回收站 |
| 376 | `.tmp/t2b_diagnose_2026_10_16.py` | 2,194 | `c5134c5f7c7b` | `$IUTH8YL.py` | `$RUTH8YL.py` | 已入回收站 |
| 377 | `.tmp/t2b_facts_inspect_2026_10_16.json` | 7,001 | `03b5ff1fd4e8` | `$IERYACN.json` | `$RERYACN.json` | 已入回收站 |
| 378 | `.tmp/t2b_harness_hunks_2026_10_16.json` | 10,102 | `efb4fcc11ef9` | `$IK7HV7S.json` | `$RK7HV7S.json` | 已入回收站 |
| 379 | `.tmp/t2b_official_facts_2026_10_16.json` | 17,263 | `3b07efe2765d` | `$IU19902.json` | `$RU19902.json` | 已入回收站 |
| 380 | `.tmp/t2b_prior_freeze_extract.json` | 5,147 | `c028df02048f` | `$IMSRFP0.json` | `$RMSRFP0.json` | 已入回收站 |
| 381 | `.tmp/t2b_readout_derive_2026_10_16.json` | 5,285 | `7e7ed499cb29` | `$IQOW1PE.json` | `$RQOW1PE.json` | 已入回收站 |
| 382 | `.tmp/t2b_verify_docs_2026_10_16.py` | 3,515 | `7b4179f7adf4` | `$I3JFHH3.py` | `$R3JFHH3.py` | 已入回收站 |
| 383 | `.tmp/t2b_write_docs_2026_10_16.py` | 48,097 | `2bb3b8bd9fc3` | `$IX7R2XJ.py` | `$RX7R2XJ.py` | 已入回收站 |
| 384 | `.tmp/t2license_items_probe2_2026_10_16.py` | 1,367 | `2a7b18194ed6` | `$IBCMW96.py` | `$RBCMW96.py` | 已入回收站 |
| 385 | `.tmp/t2license_items_probe3_2026_10_16.py` | 1,444 | `e88f8cd0bc46` | `$I7TAJQK.py` | `$R7TAJQK.py` | 已入回收站 |
| 386 | `.tmp/t2license_items_probe_2026_10_16.py` | 1,897 | `468f256ee779` | `$IUBHCSE.py` | `$RUBHCSE.py` | 已入回收站 |
| 387 | `.tmp/t2license_probe_2026_10_16.py` | 1,959 | `bd8eeccc563f` | `$IWA7XVN.py` | `$RWA7XVN.py` | 已入回收站 |
| 388 | `.tmp/t3_digest_procedure_resolved_2026_10_15.json` | 716 | `7513c451bff4` | `$IEUUE3E.json` | `$REUUE3E.json` | 已入回收站 |
| 389 | `.tmp/t3_final_check.py` | 3,748 | `12ee00f5865f` | `$IV10YA9.py` | `$RV10YA9.py` | 已入回收站 |
| 390 | `.tmp/t3_freeze_write.py` | 9,607 | `699fef8ab2bc` | `$IHZA899.py` | `$RHZA899.py` | 已入回收站 |
| 391 | `.tmp/t3_postchange_digest_2026_10_15.json` | 4,160 | `7ad62751da6f` | `$IQI0WGD.json` | `$RQI0WGD.json` | 已入回收站 |
| 392 | `.tmp/t3_prechange_baseline.py` | 2,397 | `a1121504815d` | `$IA9RL09.py` | `$RA9RL09.py` | 已入回收站 |
| 393 | `.tmp/t3_write_docs_2026_10_15.py` | 45,574 | `cdc5706f1289` | `$IN54X4T.py` | `$RN54X4T.py` | 已入回收站 |
| 394 | `.tmp/ud3_keyscan_20261016.py` | 2,305 | `ca374754b834` | `$IZQX9YV.py` | `$RZQX9YV.py` | 已入回收站 |
| 395 | `.tmp/ud3_patch_concurrency_20261016.py` | 6,033 | `fa7f38e7d882` | `$IEP7YCS.py` | `$REP7YCS.py` | 已入回收站 |
| 396 | `.tmp/ud3_patch_selfreport_20261016.py` | 3,778 | `bee751f59d9d` | `$I5FHYR8.py` | `$R5FHYR8.py` | 已入回收站 |
| 397 | `.tmp/ud3_probe2_20261016.py` | 1,409 | `2242eaa14d30` | `$IH6P5PB.py` | `$RH6P5PB.py` | 已入回收站 |
| 398 | `.tmp/ud3_probe_20261016.py` | 2,642 | `1c758a3e916d` | `$IFQ7FTK.py` | `$RFQ7FTK.py` | 已入回收站 |
| 399 | `.tmp/ud3_write_carrier_20261016.py` | 38,536 | `7485075d16ed` | `$I8TSG43.py` | `$R8TSG43.py` | 已入回收站 |
| 400 | `.tmp/v30_selfreport_2026_10_16.py` | 1,327 | `d1d8cdc4f7d5` | `$IUGFP3G.py` | `$RUGFP3G.py` | 已入回收站 |
| 401 | `.tmp/verdict_keeper_recount.py` | 2,042 | `b2a78900a96a` | `$IUQ4N55.py` | `$RUQ4N55.py` | 已入回收站 |
| 402 | `.tmp/verdict_keeper_recount_out.txt` | 4,234 | `33bf3cdbe7df` | `$IXTZMIM.txt` | `$RXTZMIM.txt` | 已入回收站 |
| 403 | `.tmp/verdict_keeper_verify.py` | 4,086 | `f0c82788b36c` | `$ITW0YAN.py` | `$RTW0YAN.py` | 已入回收站 |
| 404 | `.tmp/verdict_keeper_verify_out.txt` | 2,136 | `3f1a88c1b7f6` | `$IY1KOQB.txt` | `$RY1KOQB.txt` | 已入回收站 |
| 405 | `.tmp/verdict_keeper_write.py` | 36,025 | `da5bc61b76c5` | `$IYIARV4.py` | `$RYIARV4.py` | 已入回收站 |
| 406 | `.tmp/verify_deliverable.py` | 2,745 | `dd983b28e9aa` | `$I0AZ1QP.py` | `$R0AZ1QP.py` | 已入回收站 |
| 407 | `.tmp/verify_gamma_taucert_bytes.py` | 1,666 | `2be519ee8f4b` | `$I7U6WZF.py` | `$R7U6WZF.py` | 已入回收站 |
| 408 | `.tmp/verify_kd_s3_recompute_2026_10_16.py` | 4,676 | `f83b2eb753ca` | `$IUOOUN4.py` | `$RUOOUN4.py` | 已入回收站 |
| 409 | `.tmp/verify_kd_s3_redline2_2026_10_16.py` | 1,646 | `07cb48d7e9e2` | `$IOAL2WJ.py` | `$ROAL2WJ.py` | 已入回收站 |
| 410 | `.tmp/verify_kd_s3_redline_2026_10_16.py` | 1,972 | `82320baeb8e2` | `$I824B9O.py` | `$R824B9O.py` | 已入回收站 |
| 411 | `.tmp/verify_kd_s3_v1table_2026_10_16.py` | 2,048 | `4b40124a5101` | `$IOIFXB0.py` | `$ROIFXB0.py` | 已入回收站 |
| 412 | `.tmp/verify_reconcile.py` | 3,099 | `4cc8cb5177a7` | `$ITKDIVC.py` | `$RTKDIVC.py` | 已入回收站 |
| 413 | `.tmp/verify_two2.py` | 1,191 | `27778065e3a6` | `$IDFZTKE.py` | `$RDFZTKE.py` | 已入回收站 |
| 414 | `.tmp/verify_two3.py` | 844 | `fd85615cbd21` | `$IDR7FXU.py` | `$RDR7FXU.py` | 已入回收站 |
| 415 | `.tmp/verify_u_axis_direction_2026_10_16.py` | 1,879 | `86af98a26b9e` | `$I6E65GJ.py` | `$R6E65GJ.py` | 已入回收站 |
| 416 | `.tmp/vk_build_v1_2026_10_15.py` | 11,848 | `4cf585681505` | `$I3NK39Z.py` | `$R3NK39Z.py` | 已入回收站 |
| 417 | `.tmp/vk_diff_v1_2026_10_15.py` | 1,398 | `7c2b68ec50e2` | `$I6VZIK6.py` | `$R6VZIK6.py` | 已入回收站 |
| 418 | `.tmp/vk_fp_probe_2026_10_16.py` | 557 | `f364aefe7ef1` | `$IFUHKNQ.py` | `$RFUHKNQ.py` | 已入回收站 |
| 419 | `.tmp/vk_keyscan_2026_10_16.py` | 546 | `83fedc2b2e68` | `$IWTTEL0.py` | `$RWTTEL0.py` | 已入回收站 |
| 420 | `.tmp/vk_src_probe_2026_10_15.py` | 1,779 | `0a92d1936b1b` | `$IW0EY59.py` | `$RW0EY59.py` | 已入回收站 |
| 421 | `.tmp/vk_verify_all_2026_10_15.py` | 4,459 | `a2f343f8ca3a` | `$I8OXX5U.py` | `$R8OXX5U.py` | 已入回收站 |
| 422 | `.tmp/vk_write_m41_reg_2026_10_15.py` | 24,228 | `3ae01762d0e9` | `$I76BC29.py` | `$R76BC29.py` | 已入回收站 |
| 423 | `.tmp/vk_write_mig_reg_2026_10_15.py` | 25,981 | `d809e3836e11` | `$I7I1Z1Z.py` | `$R7I1Z1Z.py` | 已入回收站 |
| 424 | `.tmp/write_33base.py` | 30,525 | `ea509bd7c54b` | `$IHMLMQ8.py` | `$RHMLMQ8.py` | 已入回收站 |
| 425 | `.tmp/write_d1_c_effect.py` | 31,870 | `659b7993d403` | `$IY8ROBT.py` | `$RY8ROBT.py` | 已入回收站 |
| 426 | `.tmp/write_field_value_sourcing.py` | 22,442 | `826b764d980a` | `$I48MBVV.py` | `$R48MBVV.py` | 已入回收站 |
| 427 | `.tmp/write_gamma_taucert_sourcing.py` | 36,831 | `4cccd496e23b` | `$IZ2A9LG.py` | `$RZ2A9LG.py` | 已入回收站 |
| 428 | `.tmp/write_out.txt` | 311 | `44131335f427` | `$IGDKGWS.txt` | `$RGDKGWS.txt` | 已入回收站 |
| 429 | `.tmp/write_reconcile_register.py` | 27,704 | `8bbf2224a026` | `$IZPVXK8.py` | `$RZPVXK8.py` | 已入回收站 |
| 430 | `.tmp/write_u_retirement.py` | 23,220 | `af2ad133f0f4` | `$IK6LNC7.py` | `$RK6LNC7.py` | 已入回收站 |
| 431 | `results/__pycache__/_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | 43,685 | `f4194cc5a522` | `$I4A4ZAU.pyc` | `$R4A4ZAU.pyc` | 已入回收站 |
| 432 | `results/__pycache__/_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | 67,081 | `08d4b51c45c6` | `$IJ93049.pyc` | `$RJ93049.pyc` | 已入回收站 |
| 433 | `results/_archive_2026_09_20` | 0 | `（空目录）` | `$IZL68JA` | `$RZL68JA` | 已入回收站（空目录·事后验真） |
| 434 | `results/_archive_2026_09_21` | 0 | `（空目录）` | `$I98DSGM` | `$R98DSGM` | 已入回收站（空目录·事后验真） |

---

## §3 验道记录（小样验道 · 批量之前）

派工单指定「以 1 件零字节件走可恢复通道，验 `$I`/`$R` 成对 ＋ `$I` 原路径解码（偏移 28）」。
**派工单建议的 `.tmp/_e_q_exec.txt` 未被采用** —— 该件被本棒四通道 B（裸名）拦下：
10-15 登记件 `results/_cleanup_exec_register_2026_10_15.md:54` 钉有 `.tmp/_e_q_exec.py`，
同 stem 之 `_e_q_exec.txt` 随之被拦。**⛔0 强删拦下件**，改取本棒清单内真零字节件。

| 验道件 | bytes | SHA-12 | `$I` | `$R` | 离原位 | `$I` 原路径解码 | 偏移 | `$R` 内容校验 |
| :-- | --: | :-- | :-- | :-- | :-- | :-- | --: | :-- |
| `.tmp/r461_probe09.txt`（零字节） | 0 | `e3b0c44298fc` | `$IICNAQE.txt` | `$RICNAQE.txt` | 是 | `_repo_mirror\.tmp\r461_probe09.txt` | **28** | 0 B ＝ 原值 |
| `.tmp/h_mq20.py`（非空载荷） | 285 | `5f81afe2955c` | `$IRBKH1X.py` | `$RRBKH1X.py` | 是 | `_repo_mirror\.tmp\h_mq20.py` | **28** | `$R` 实测 285 B ＝ 原值 |

**验真结论**：通道成立 —— 两件皆「目标离原位 ＋ `$I`/`$R` 成对 ＋ `$I` 原路径解码正确」，
**`$I` 路径实测偏移 ＝ 28，与派工单所述一致（文件型）**。
追加非空载荷件（285 B）是为证明「载荷真落入 `$R`」，非派工单要求，属验真加强。
`$I` 版本 ＝ 2；字节偏移 28 处起为 UTF-16LE 原路径。
**实测补充**：**目录型 `$I` 之路径起于字节偏移 26**（3 个空目录实测），与文件型 28 不同。

---

## §4 清单自建与 511 之交叉

派工单明示「⛔0 凭转述数字执行 —— 以自建四通道实测为准」，故本棒**未沿用 511 之数**，自行复测：

| 项 | 值 |
| :-- | :-- |
| 语料（`.tmp` 外全仓） | 1744 件 ／ 61,258,582 B |
| 遍历错误 | **0** |
| 候选（`.tmp` 全量） | 1158 件 |
| 四通道零命中（严格） | **424 件** |
| ＋ D 通道伪阳修正 | **428 件** |
| 勘察棒之数 | 511 件 |
| **差（KD）** | **83 件** |

**日分层交叉**

| 日 | 勘察棒 511 | 本棒四通道 | 差 |
| :-- | --: | --: | --: |
| 2026-10-13 | 46 | 30 | **＋16** |
| 2026-10-14 | 120 | 100 | **＋20** |
| 2026-10-15 | 84 | 70 | **＋14** |
| 2026-10-16 | 261 | 228 | **＋33** |
| **合计** | **511** | **428** | **＋83** |

**KD 83 件之根因（均为「本棒更严」方向，落安全侧）**

**在 10-13..10-16 窗内、纯由通道拦下（无绝对排除）者共 350 件，命中通道组合分布**：

| 命中通道组合 | 件数 |
| :-- | --: |
| A＋B＋C | 126 |
| A＋B＋C＋D | 117 |
| B | 87 |
| D | 14 |
| B＋D | 3 |
| B＋C | 2 |
| A＋B＋D | 1 |

**主因 1 · B 通道 stem 连带（51 件，占 B 单挂 88 件中之多数）** —— 10-15 登记/清单件 
`results/_cleanup_exec_register_2026_10_15.md`、
`results/_cleanup_inventory_2026_10_15.md` 钉有大量 `.tmp/<stem>.py` 名；本棒 B 通道含裸 stem 判据，
故**同 stem 之 `.txt`／`.json` 兄弟件一并被拦**（如 `_e_q_exec.py` 已清 → `_e_q_exec.txt`／`_e_q_exec.json` 被拦）。
其中 **51 件全仓以「件名」0 命中**（仅 stem 提及），系最可能被勘察棒计入 511 者。

**主因 2 · C 通道与 A 通道重叠（余量）** —— 本棒 C 通道之取样含「任何含 `.tmp` 的引号字符串」，
故凡 A 已命中者 C 必同命中，C 实为 A 之超集而非独立信号；此重叠使 A＋C 组合项偏大。

**已修正项 · D 通道伪阳（4 件）** —— `e3b0c44298fc`（SHA-256 空串）被 `letters/`、`results/` 多件登记为
「0 字节件」之通用标记，非指向本棒候选；D 通道对零字节件不具区分力。**本棒已修正**（非区分性内容哈希不触发 D），
4 件回归可清：`_t2_t3_prex_a_route_err.txt`／`docwriter_v41_probe_err.txt`／`probe11.err`／`r461_probe09.txt`。
另有 3 件零字节件（`_e_q_exec.txt`／`_m5_k5_net.err`／`_m5_k5_scan.err`）因 **B 通道**仍被拦，不属本项。

**处置立场**：派工单明示「凡你自建之四通道零命中者方为可清」，故本棒**只清 428 件、未为凑数放宽判据**；
差额 83 件以 KD 呈报，候 PI 裁是否授权按「件名（不含 stem）」重判。

---

## §5 绝对排除与保护面核验（删后实测）

| 约束 | 处置 | 删后实测 |
| :-- | :-- | :-- |
| ② 轨迹数据面（`*measurement*`／`*llm_calls*`／`*records*`／`three_seed*`／`*_detail*`） | ⛔0 清 | `.tmp` 内仍存 **46 件**（＝复测 R2 计数，全数留存） |
| ③ 当日（2026-10-17）件 | ⛔0 清 | `.tmp` 内当日件全数留存 |
| `results/`／`letters/`／`docs/` 下任何件 | ⛔0 动 | `results` 1081 件／`letters` 111 件／`docs` 135 件，**除 C4 两个 `__pycache__` 外 0 触动** |
| 乙档（入链）／存疑 33／sub 88 | ⛔0 动 | 复测命中入链者**全部留存**（含 `.tmp/s4_regen_runner.py`，`results/_s4_source_wave_mapping_registration_2026_10_10.md:235` 明载「0 改、0 移、0 删」） |
| 凡不在本清单内者 | ⛔0 动 | 删后 `.tmp` 留存 733 件，**其中计划内而未删者 ＝ 0** |

**删后范围自证**：`os.walk` 遍历错误 **0**；431 件计划件**离原位者 431／431**；
431 件**全部**在回收站有 `$I` 记录（431／431），随机抽验 15 件之 `$R` 载荷 SHA-12 **15／15 与删前一致**。

---

## §6 纪律自报（字节级）

| 项 | 值 |
| :-- | :-- |
| 落盘前 Test-Path | `False` |
| 落盘前同名 glob | `results/_cleanup511*` → **0 命中** |
| 编码 | UTF-8 **无 BOM** |
| 行尾 | **纯 LF**（CRLF ＝ 0） |
| 落盘方式 | Python `io.open(..., newline="\n")` 直写 |
| 路径写法 | Windows raw 字符串 |
| key 形态扫描 | 0 命中（未读 key／未落盘凭据） |
| 网络 | **⛔0 网络** |
| 永久删 | **0 件** |
| 署名 | worker |

---

## §7 并发观测（非本棒所为 · 须知悉）

执行窗内另有棒并发写/删：

1. **`.tmp` 并发写入** —— 勘察期间 `.tmp` 件数 1149 → 1158（`collision_survey_*` 系列，实测 10:07:57–58 落盘）；
   该批全为 10-17 件，由约束 ③ 全数拦下，未入本棒清单。
2. **他棒删 `results/` 2 件** —— 回收站另有 `$ICQO5B3.json`／`$IICM2TA.json`（`$I` 时刻 **10:19:26／10:19:32**，
   晚于本棒批次结束 10:17:59），指向 `results/_dep_dangling_final.json`／`results/_dep_dangling_scan_raw.json`。
   **该 2 件不在本棒清单内，非本棒所删**，特此区分以免归因错位。

---

## §8 风险与遗留

1. **回收站为唯一恢复面** —— 回收站于 10-15 后曾被清空过（10-15 登记件载 `$I` 6→283，本棒开工前盘面仅 `desktop.ini`）；
   本棒 434 件之可恢复性**完全依赖回收站不被清空**。清空即不可逆。
2. **KD 83 件未清** —— 候 PI 裁是否按「仅件名、不含 stem」重判 B 通道（见 §4）。
3. **C4 判定留痕** —— `results/__pycache__` 2 件与 `.tmp/__pycache__/s4_regen_runner.cpython-314.pyc` 系按
   派工单判据 ④「两个 `__pycache__` 可清」纳入，而非四通道零命中；其中后者之源 `.tmp/s4_regen_runner.py` 为
   **受保护唯一实现载体**，删其字节码不删其源码，风险极低但**属判据 ④ 之运用，非四通道结论**，故明示。
4. **⛔ 未宣告①毕** —— 本棒仅执行清理面，⛔0 就①段收束作任何宣告。
