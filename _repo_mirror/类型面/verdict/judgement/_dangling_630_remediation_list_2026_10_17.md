# 悬空引用·回填／改登记 清单件（2026-10-17）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_dangling_630_remediation_list_2026_10_17.md` |
| **棒 ID** | `DANGLING-630-REMEDIATION-LIST` |
| **授权出处** | PI 2026-10-17 复工首送卡（`ask_9f7d29f61ac912895a4c3a70`）Q3 逐字「全部 630 项出回填清单」 |
| **本件性质** | 回填／改登记之**设计面**（方案与依据），**非执行面** |
| **状态** | **候 PI 核准**；核准前 ⛔0 执行任何回填／恢复／删除 |
| **署名** | doc-writer（文稿起草／登记专官） |
| **数据基座** | 全仓实测自建（`.tmp` 外 1,712 件文本件逐行扫描），⛔0 转引派工单之转述数字 |
| **归因面** | `results/_cleanup_exec_register_2026_10_15.md` · SHA-12 `D53036B01062` · 36,349 bytes（实测正身） |
| **执行表行数** | 277 行已执行（其中 `.tmp/` 下 274 行） |
| **落盘时点** | 2026-10-17T10:11:17 |

---

## §0 边界声明（先于一切结论）

- ⛔ **0 执行**：本棒**未**恢复、**未**回填、**未**删除任何文件；**未**改动任何既有件（本件为唯一新增件）。
- ⛔ **0 回改**：§3–§5 所列「建议径」一律为**建议**，采纳与否由 PI 裁定。
- ⛔ **0 网络**：全流程无任何联网动作。
- 本件所载「悬空项」为**实测扫描结果**；与派工单转述之 630 之差异，见 §6 逐层对账（**未**以转述数字覆盖实测）。

---

## §1 自建悬空清单：扫描口径与三重自审

### §1.1 口径

| 口径项 | 实测取值 |
| :-- | :-- |
| 遍历根 | `〔本地路径已脱敏〕` |
| 遍历面 | 除根 `.tmp/` 外全仓（含 `_archive_*` 已废弃面 5 目录／32 件） |
| 排除面 | 根 `.tmp/`（引用面非被引面）；`.git`／`node_modules`／`__pycache__`／`.venv`／`venv` |
| 排除之二进制载体 | 25 件（`.pyc`/`.pkl`/`.log` 等）——经实测**不改变唯一名集合**（§1.3 之三） |
| 排除之自身产物 | 2 件（前次扫描落盘之 JSON，防自污染，见 §1.4） |
| 严格解码 | UTF-8 严格；解码失败 1 件（`_u5_inventory_tmp.txt`）**跳过不猜** |
| 扫描文本件 | 1,712 件 / 57,682,671 bytes |
| `.tmp/` 引用面现存件 | 1158 件（目录 `__pycache__`／`_pre_mod`／`_pre_mod/__pycache__`／`numaudit_20261013`） |
| 引用式样 | `.tmp/<名>` 与 `.tmp\<名>` 并取；含子路径者取**最长存在前缀**，否则判缺 |

### §1.2 三重自审（阴性结论）

| 自审项 | 要求 | 实测 | 结论 |
| :-- | :-- | :-- | :-- |
| 一·遍历完整性 | `os.walk` 遍历错误数须为 0 | `walk_errs = 0` | ✅ 无遍历遗漏 |
| 二·模式非结构性互斥 | 结论不得由扫描口径之结构性副作用生成 | 二进制载体排除前后**唯一名集合相同**（0 件仅由二进制承载） | ✅ 非口径产物 |
| 三·时点新鲜 | 须为当次实测 | 2026-10-17T10:11:17（本棒即时扫描） | ✅ 新鲜 |

另附**独立法交叉验**：对 A1 全部 273 件另以 `os.path.exists` 直探（**不经** `os.walk` 清单），命中 0 件；并作大小写不敏感复探，命中 0 件。**A1 全数确不在 `.tmp/`。**

### §1.3 二进制载体之排除（实测非口径产物）

`.pyc` 等二进制件以 `errors='replace'` 解码时会吐出伪 `.tmp/` 串（曾使引用面计数虚增至 10,419）。实测：**全部 644 个唯一悬空名均由文本载体（`.md`/`.json`/`.py`）承载，仅由二进制承载者 0 件**。故二进制仅影响**出现次数**，不影响**唯一名集合**，排除之。

### §1.4 自污染事故与修正（老实交代）

首轮扫描将原始结果落盘于 `results/_dep_dangling_scan_raw.json` 与 `_dep_dangling_final.json`，二者**自身即含** `.tmp/<名>` 字面量，遂被次轮扫描当作引用件计入。实测证据：`.tmp/_t15r2_records.json` 直测出现 **176** 次，扣去两个自身产物之 **44 + 88 = 132** 次，得 **44** 次。

**修正**：最终扫描①排除本棒自身产物（`_dep_dangling*` 前缀）②原始数据改落仓外临时目录。修正后 `_t15r2_records.json` 恰为 **44 次**，与派工单转述之「44 处」**吻合**。此事故亦为本次「引用面计数虚高」之唯一根因。

---

## §2 实测结果与三分层

| 层 | 件数 | 引用处次数 | 定义（本棒实测口径） |
| :-- | --: | --: | :-- |
| **A1** | **273** | 549 | 目标名命中 10-15 执行表 `.tmp/` 行 ⇒ 归因于该次清理（**自伤断链**） |
| **A2** | **326** | 1,421 | 目标名不在该表 ⇒ 先于 10-15 之既有缺陷 |
| **B** | **45** | 89 | 引用之**正则产物**（通配／截断词干／语法残留／`__pycache__`／无扩展名碎片）⇒ 非真实缺失件 |
| **合计** | **644** | **2,059** | 唯一悬空目标名 |

引用面总计 `.tmp/` 引用处 **5,083** 处，其中**命中现存件／现存目录 3,024 处**、**悬空 2,059 处**（3,024 ＋ 2,059 = 5,083）。命中之 3,024 处中，含 5 处形如 `.tmp/<名>#<片SHA>…` 之锚形态引用：其 `#` 后为部分 SHA 锚（PI 制式），基础名 **全部存在**于 `.tmp/`，故该 5 处**引用本身有效**，本棒正则曾越 `#` 截取，已修正（详见 §5.3 第 2 条）。

---

## §3 A1 层（273 项·自伤断链）之逐项清单与处置建议

### §3.1 甲／乙 通道存续实测（本棒**先验** `$I`/`$R`，仅出方案）

| 通道 | 实测 | 结论 |
| :-- | :-- | :-- |
| 甲-1 回收站 `$R` | `〔本地路径已脱敏〕` 下 `$I` 条目 **0**、`$R` 条目 **0**（全 bin 递归亦 0/0） | ❌ **不可用** |
| 甲-2 外部非上传归档 | `〔归档区〕`（39,720 件）内按精确 `.tmp/<名>` 路径命中 A1 **0 / 273** | ❌ **不可用** |

> **与执行登记件之落差（须 PI 留意）**：10-15 执行登记件表头载「清理后 `$I` 条目 **283**（6 ＋ 待清 277，成对齐全）」。本棒 2026-10-17 实测该 SID 目录 `$I`/`$R` **均为 0**，且该目录 `LastWriteTime` 为 **2026-10-17 09:50:37**（当日本棒开工前约 15 分钟）。即：**回收站已于 10-15 之后被清空**，两条恢复通道同时断。
>
> **结论：甲（回填）对 A1 全 273 项均不可行**（双通道实测皆空）。故 §3.3 之建议径**无一条为甲**。

### §3.2 A1 之引用分布——决定性发现

A1 之 273 项共 549 个引用处，其引用件分布**极端集中**：

| 引用件 | 覆盖 A1 项数 |
| :-- | --: |
| `results/_cleanup_exec_register_2026_10_15.md`（**执行登记件自身**） | 273 |
| `results/_cleanup_inventory_2026_10_15.md`（**待清清单件自身**） | 273 |
| `results/_m41_double_readout_contrast_exec_2026_10_15.md` | **1** |
| `results/_m41_verdict_kd_effect_register_2026_10_15.md` | **1** |

**逐字回读示例**（执行登记件 L37，同指 `_659_overlap_extract.py`）：

```
| 4 | `.tmp/_659_overlap_extract.py` | 10,934 | `8501C1B8B1AF` | `$IOZX5RI.py` | `$ROZX5RI.py` | 已入回收站 |
```

**此为「该路径**曾**存在、且已被本表所载之清理动作删除」之**史实陈述**；其形如 `.tmp/<名>` 之字符串系**被删对象之记名**，非「现应可达之链接」。**

> **对处置面之根本影响**：对 **272 / 273** 项而言，其唯一引用位于**清理登记件自身**。若对其施加「乙（改登记·失效引用勘误注记）」，等于**改写已执行之清理动作之历史记录**——此举本身构成记录失真，**本棒明确不建议**。故 A1 之大部**建议径为「无需处置」**，理由是**引用非失效，扫描判其为悬空系口径所致**。
>
> 唯一例外：`m41_fix_diag.py`——其引用**另见活文档**（M41 执行件 L273、M41 判定登记件 L164），非纯史实件，方属「活文档之失效引用」。

### §3.3 A1 逐项清单（273 行）

图例：`建议径`＝**甲**回填／**乙**改登记（另立件并列注记·⛔0 回改原件）／**无**无需处置；`依据`＝`史`＝引用为清理史实之真实陈述，`活`＝活文档之失效引用。

| # | 目标名（`.tmp/` 下） | bytes | SHA-12 | `$I` | `$R` | 引用处（件·行） | 建议径 | 依据 |
| --: | :-- | --: | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | `_659_overlap_extract.py` | 10,934 | `8501C1B8B1AF` | `$IOZX5RI.py` | `$ROZX5RI.py` | 执行登记件:L37 ／ 待清清单件:L49 | **无** | 史 |
| 2 | `_build_l3_register_2026_10_13.py` | 39,911 | `272C363BBA08` | `$IWMU1EH.py` | `$RWMU1EH.py` | 执行登记件:L38 ／ 待清清单件:L50 | **无** | 史 |
| 3 | `_consolidate_user_md.py` | 7,607 | `5CAE585CE3F0` | `$IV1M1NH.py` | `$RV1M1NH.py` | 执行登记件:L39 ／ 待清清单件:L51 | **无** | 史 |
| 4 | `_docwriter_linecount_probe.py` | 1,332 | `73A6DB90AC00` | `$IFHE0MC.py` | `$RFHE0MC.py` | 执行登记件:L40 ／ 待清清单件:L52 | **无** | 史 |
| 5 | `_docwriter_night_headers.py` | 1,473 | `B413F97E8E18` | `$IFY7U7W.py` | `$RFY7U7W.py` | 执行登记件:L41 ／ 待清清单件:L53 | **无** | 史 |
| 6 | `_docwriter_night_measure.py` | 2,094 | `DA7B60413E52` | `$IWVS453.py` | `$RWVS453.py` | 执行登记件:L42 ／ 待清清单件:L54 | **无** | 史 |
| 7 | `_docwriter_refscan_probe.py` | 1,925 | `4510E596FA83` | `$INHWL3E.py` | `$RNHWL3E.py` | 执行登记件:L43 ／ 待清清单件:L55 | **无** | 史 |
| 8 | `_docwriter_refscan_probe_r1.py` | 2,150 | `627D628A83BF` | `$IRP9DBZ.py` | `$RRP9DBZ.py` | 执行登记件:L44 ／ 待清清单件:L56 | **无** | 史 |
| 9 | `_dw_chain.py` | 1,395 | `2363F7B81800` | `$I9BNWF9.py` | `$R9BNWF9.py` | 执行登记件:L45 ／ 待清清单件:L57 | **无** | 史 |
| 10 | `_dw_ge01_g7_approval.py` | 30,188 | `90612B980D89` | `$II2W07U.py` | `$RI2W07U.py` | 执行登记件:L46 ／ 待清清单件:L58 | **无** | 史 |
| 11 | `_dw_lines.py` | 1,340 | `8E9162831C51` | `$I4ZBKLV.py` | `$R4ZBKLV.py` | 执行登记件:L47 ／ 待清清单件:L59 | **无** | 史 |
| 12 | `_dw_m5_scan3.py` | 1,663 | `A5AAC1F61A2D` | `$IJZK7WD.py` | `$RJZK7WD.py` | 执行登记件:L48 ／ 待清清单件:L60 | **无** | 史 |
| 13 | `_dw_m5_verify.py` | 2,385 | `FF13D1E4DEDE` | `$I2HN06Q.py` | `$R2HN06Q.py` | 执行登记件:L49 ／ 待清清单件:L61 | **无** | 史 |
| 14 | `_dw_scan4.py` | 2,586 | `1CE045907050` | `$IM1A1UW.py` | `$RM1A1UW.py` | 执行登记件:L50 ／ 待清清单件:L62 | **无** | 史 |
| 15 | `_dw_scan_m5.py` | 1,087 | `10289C48D724` | `$IE55MTJ.py` | `$RE55MTJ.py` | 执行登记件:L51 ／ 待清清单件:L63 | **无** | 史 |
| 16 | `_dw_selfcheck.py` | 2,035 | `2E68C224B104` | `$I44Q5TY.py` | `$R44Q5TY.py` | 执行登记件:L52 ／ 待清清单件:L64 | **无** | 史 |
| 17 | `_dw_write_m5.py` | 16,938 | `37EF3F28715C` | `$I7K1KC1.py` | `$R7K1KC1.py` | 执行登记件:L53 ／ 待清清单件:L65 | **无** | 史 |
| 18 | `_e_q_exec.py` | 5,006 | `82A590D47646` | `$IADM9B3.py` | `$RADM9B3.py` | 执行登记件:L54 ／ 待清清单件:L66 | **无** | 史 |
| 19 | `_e_q_precheck.py` | 3,446 | `A7C013804E94` | `$IFRTA5R.py` | `$RFRTA5R.py` | 执行登记件:L55 ／ 待清清单件:L67 | **无** | 史 |
| 20 | `_e_q_recon.py` | 4,991 | `DB07D0E36F5E` | `$IO0AN7H.py` | `$RO0AN7H.py` | 执行登记件:L56 ／ 待清清单件:L68 | **无** | 史 |
| 21 | `_e_q_scan.py` | 1,301 | `DD6E09C118BF` | `$IX3LY65.py` | `$RX3LY65.py` | 执行登记件:L57 ／ 待清清单件:L69 | **无** | 史 |
| 22 | `_e_q_verify.py` | 2,199 | `06AA677DB832` | `$IBHEUEV.py` | `$RBHEUEV.py` | 执行登记件:L58 ／ 待清清单件:L70 | **无** | 史 |
| 23 | `_e_q_write.py` | 1,705 | `3436C7E026C8` | `$IK3ONSS.py` | `$RK3ONSS.py` | 执行登记件:L59 ／ 待清清单件:L71 | **无** | 史 |
| 24 | `_ea_461_verify.py` | 2,878 | `D4D632C26FA2` | `$IU042AC.py` | `$RU042AC.py` | 执行登记件:L60 ／ 待清清单件:L72 | **无** | 史 |
| 25 | `_ea_closeout4.py` | 1,350 | `2EE2F1D522D4` | `$I092IUF.py` | `$R092IUF.py` | 执行登记件:L61 ／ 待清清单件:L73 | **无** | 史 |
| 26 | `_ea_extra.py` | 2,126 | `CAEC74CADC34` | `$IO31XU7.py` | `$RO31XU7.py` | 执行登记件:L62 ／ 待清清单件:L74 | **无** | 史 |
| 27 | `_ea_extra2.py` | 1,644 | `0EFA93B89DB4` | `$IYNQPN0.py` | `$RYNQPN0.py` | 执行登记件:L63 ／ 待清清单件:L75 | **无** | 史 |
| 28 | `_ea_prewrite.py` | 2,244 | `2E14C3D93B8F` | `$IY95IOG.py` | `$RY95IOG.py` | 执行登记件:L64 ／ 待清清单件:L76 | **无** | 史 |
| 29 | `_ea_selfcheck.py` | 1,715 | `79AA8DA91CE9` | `$IQMNO9F.py` | `$RQMNO9F.py` | 执行登记件:L65 ／ 待清清单件:L77 | **无** | 史 |
| 30 | `_ecr_pa_verify_2026_10_15.py` | 5,120 | `69D91B3CA5E2` | `$IK98R9H.py` | `$RK98R9H.py` | 执行登记件:L66 ／ 待清清单件:L78 | **无** | 史 |
| 31 | `_ecr_pa_write_carrier_2026_10_15.py` | 12,212 | `F4B21FAE4D5D` | `$ISJJXTW.py` | `$RSJJXTW.py` | 执行登记件:L67 ／ 待清清单件:L79 | **无** | 史 |
| 32 | `_ecr_pa_write_register_2026_10_15.py` | 1,040 | `D464A1D6E5C6` | `$I4DR43P.py` | `$R4DR43P.py` | 执行登记件:L68 ／ 待清清单件:L80 | **无** | 史 |
| 33 | `_ev_m5_diff_2026_10_14.py` | 1,594 | `FCC4A11F8050` | `$IU8VOD0.py` | `$RU8VOD0.py` | 执行登记件:L69 ／ 待清清单件:L81 | **无** | 史 |
| 34 | `_ev_map2_2026_10_14.py` | 2,421 | `ED2CA7DD3694` | `$IDHNKR7.py` | `$RDHNKR7.py` | 执行登记件:L70 ／ 待清清单件:L82 | **无** | 史 |
| 35 | `_ev_map_2026_10_14.py` | 1,703 | `8DD1DFD65D02` | `$IV8472V.py` | `$RV8472V.py` | 执行登记件:L71 ／ 待清清单件:L83 | **无** | 史 |
| 36 | `_ev_probe_2026_10_14.py` | 936 | `B234D32F5EF7` | `$IQOZD23.py` | `$RQOZD23.py` | 执行登记件:L72 ／ 待清清单件:L84 | **无** | 史 |
| 37 | `_ev_rt_2026_10_14.py` | 2,690 | `B3DC15BD3441` | `$IPDIRNU.py` | `$RPDIRNU.py` | 执行登记件:L73 ／ 待清清单件:L85 | **无** | 史 |
| 38 | `_ev_scan2_2026_10_14.py` | 3,140 | `9AEDB7071C14` | `$IBKYX40.py` | `$RBKYX40.py` | 执行登记件:L74 ／ 待清清单件:L86 | **无** | 史 |
| 39 | `_ev_scan_2026_10_14.py` | 3,110 | `BEDE66F1A93B` | `$I1PB8J6.py` | `$R1PB8J6.py` | 执行登记件:L75 ／ 待清清单件:L87 | **无** | 史 |
| 40 | `_ev_verify_meta_2026_10_14.py` | 4,763 | `AA0DAEF7443C` | `$I42PVHL.py` | `$R42PVHL.py` | 执行登记件:L76 ／ 待清清单件:L88 | **无** | 史 |
| 41 | `_ev_verify_out_2026_10_14.py` | 2,115 | `C6096A6FD98D` | `$I1P7KM4.py` | `$R1P7KM4.py` | 执行登记件:L77 ／ 待清清单件:L89 | **无** | 史 |
| 42 | `_evidence_auditor_m5_delta_decomp.py` | 5,140 | `60970491E11C` | `$IL72CQ9.py` | `$RL72CQ9.py` | 执行登记件:L78 ／ 待清清单件:L90 | **无** | 史 |
| 43 | `_evidence_auditor_m5_erratum_fp.py` | 1,265 | `A97A7CFF819E` | `$IUAV8RZ.py` | `$RUAV8RZ.py` | 执行登记件:L79 ／ 待清清单件:L91 | **无** | 史 |
| 44 | `_evidence_auditor_m5_hunk_detail.py` | 4,256 | `339BEF248888` | `$IQSCHAR.py` | `$RQSCHAR.py` | 执行登记件:L80 ／ 待清清单件:L92 | **无** | 史 |
| 45 | `_evidence_auditor_m5_land.py` | 28,224 | `30E70282C305` | `$I9VLYGC.py` | `$R9VLYGC.py` | 执行登记件:L81 ／ 待清清单件:L93 | **无** | 史 |
| 46 | `_evidence_auditor_m5_negative_sweep.py` | 4,443 | `92A2813E4E42` | `$IN6QW34.py` | `$RN6QW34.py` | 执行登记件:L82 ／ 待清清单件:L94 | **无** | 史 |
| 47 | `_evidence_auditor_m5_reaudit_probe.py` | 6,278 | `95252FDA0813` | `$IALTZ3K.py` | `$RALTZ3K.py` | 执行登记件:L83 ／ 待清清单件:L95 | **无** | 史 |
| 48 | `_f12_kd_disposition_verify_2026_10_15.py` | 3,476 | `203771088EF3` | `$I87O407.py` | `$R87O407.py` | 执行登记件:L84 ／ 待清清单件:L96 | **无** | 史 |
| 49 | `_f12_kd_disposition_write_2026_10_15.py` | 24,703 | `0D42A6B5342A` | `$IGPDSQI.py` | `$RGPDSQI.py` | 执行登记件:L85 ／ 待清清单件:L97 | **无** | 史 |
| 50 | `_ge01_ecr_anchor_probe_2026_10_14.py` | 5,850 | `22D4CB9E0457` | `$IZ5A5GP.py` | `$RZ5A5GP.py` | 执行登记件:L86 ／ 待清清单件:L98 | **无** | 史 |
| 51 | `_ge01_ecr_extract.py` | 564 | `7639EECE129E` | `$I7D6IWO.py` | `$R7D6IWO.py` | 执行登记件:L87 ／ 待清清单件:L99 | **无** | 史 |
| 52 | `_ge01_ecr_probe.py` | 986 | `36E1579C341D` | `$I82P4P8.py` | `$R82P4P8.py` | 执行登记件:L88 ／ 待清清单件:L100 | **无** | 史 |
| 53 | `_ge01_ecr_probe2.py` | 2,266 | `01554968C614` | `$IHWRNV7.py` | `$RHWRNV7.py` | 执行登记件:L89 ／ 待清清单件:L101 | **无** | 史 |
| 54 | `_ge01_ecr_probe3.py` | 2,866 | `62A887BE2EC8` | `$IRZT9DV.py` | `$RRZT9DV.py` | 执行登记件:L90 ／ 待清清单件:L102 | **无** | 史 |
| 55 | `_ge01_ecr_probe4.py` | 3,638 | `2B09FC4301E4` | `$I1BOQ6N.py` | `$R1BOQ6N.py` | 执行登记件:L91 ／ 待清清单件:L103 | **无** | 史 |
| 56 | `_ge01_ecr_probe5.py` | 3,381 | `F545FD9976EB` | `$IPEWY03.py` | `$RPEWY03.py` | 执行登记件:L92 ／ 待清清单件:L104 | **无** | 史 |
| 57 | `_ge01_ecr_probe6.py` | 1,777 | `369DF9392729` | `$I11ZF3R.py` | `$R11ZF3R.py` | 执行登记件:L93 ／ 待清清单件:L105 | **无** | 史 |
| 58 | `_ge01_ecr_probe7.py` | 1,227 | `41748DFBE314` | `$IAV59U6.py` | `$RAV59U6.py` | 执行登记件:L94 ／ 待清清单件:L106 | **无** | 史 |
| 59 | `_ge01_ecr_probe8.py` | 1,335 | `5B9A0057A940` | `$I4CDO8W.py` | `$R4CDO8W.py` | 执行登记件:L95 ／ 待清清单件:L107 | **无** | 史 |
| 60 | `_ge01_final_verify.py` | 1,200 | `7FAC40E69A55` | `$IDNM8X0.py` | `$RDNM8X0.py` | 执行登记件:L96 ／ 待清清单件:L108 | **无** | 史 |
| 61 | `_ge01_precedent.py` | 888 | `64AAF11B2B4D` | `$IGK0ON3.py` | `$RGK0ON3.py` | 执行登记件:L97 ／ 待清清单件:L109 | **无** | 史 |
| 62 | `_ge01_write_ecr_sourcing_design.py` | 42,346 | `543E71A6DD0A` | `$IXT0P1B.py` | `$RXT0P1B.py` | 执行登记件:L98 ／ 待清清单件:L110 | **无** | 史 |
| 63 | `_ge01_write_invalid_register.py` | 24,549 | `FF8AF654B91B` | `$ITP4CEA.py` | `$RTP4CEA.py` | 执行登记件:L99 ／ 待清清单件:L111,752 | **无** | 史 |
| 64 | `_gen_ge01_calc_rebuild_design.py` | 46,822 | `7901B4D5D943` | `$ILPC31B.py` | `$RLPC31B.py` | 执行登记件:L100 ／ 待清清单件:L112 | **无** | 史 |
| 65 | `_h_fp_worker.py` | 1,758 | `83044C28F1E4` | `$IMOQSJP.py` | `$RMOQSJP.py` | 执行登记件:L101 ／ 待清清单件:L113 | **无** | 史 |
| 66 | `_h_prewrite_worker.py` | 922 | `19E12EA93813` | `$IENWE2M.py` | `$RENWE2M.py` | 执行登记件:L102 ／ 待清清单件:L114 | **无** | 史 |
| 67 | `_h_probe2_worker.py` | 3,980 | `A4EA10047A87` | `$IZ5FLM3.py` | `$RZ5FLM3.py` | 执行登记件:L103 ／ 待清清单件:L115 | **无** | 史 |
| 68 | `_h_probe3_worker.py` | 3,868 | `BECB396A938A` | `$ITOIG1G.py` | `$RTOIG1G.py` | 执行登记件:L104 ／ 待清清单件:L116 | **无** | 史 |
| 69 | `_h_probe4_worker.py` | 2,620 | `944AC4875842` | `$IOBZJWK.py` | `$ROBZJWK.py` | 执行登记件:L105 ／ 待清清单件:L117 | **无** | 史 |
| 70 | `_h_probe5_worker.py` | 2,515 | `19D7ED57310D` | `$IEBIH2B.py` | `$REBIH2B.py` | 执行登记件:L106 ／ 待清清单件:L118 | **无** | 史 |
| 71 | `_h_probe6_worker.py` | 1,618 | `73C37891934A` | `$IYDVFGJ.py` | `$RYDVFGJ.py` | 执行登记件:L107 ／ 待清清单件:L119 | **无** | 史 |
| 72 | `_h_probe7_worker.py` | 2,068 | `CE25C7C49984` | `$ICOP965.py` | `$RCOP965.py` | 执行登记件:L108 ／ 待清清单件:L120 | **无** | 史 |
| 73 | `_h_write_worker.py` | 29,848 | `B1219747CFDB` | `$IF0YHSQ.py` | `$RF0YHSQ.py` | 执行登记件:L109 ／ 待清清单件:L121 | **无** | 史 |
| 74 | `_kd_h5_h6_gen.py` | 23,239 | `73F18F1DD3FC` | `$IRC7OM4.py` | `$RRC7OM4.py` | 执行登记件:L110 ／ 待清清单件:L122 | **无** | 史 |
| 75 | `_land_three_items.py` | 1,970 | `4FB8F6AEA50E` | `$I96PQQZ.py` | `$R96PQQZ.py` | 执行登记件:L111 ／ 待清清单件:L123 | **无** | 史 |
| 76 | `_locate_c1_c2_2026_10_14.py` | 1,109 | `691A5A30AABD` | `$IRAIQZ9.py` | `$RRAIQZ9.py` | 执行登记件:L112 ／ 待清清单件:L124 | **无** | 史 |
| 77 | `_m5_k5_net2.py` | 2,976 | `46AA235FD5AB` | `$IP8ZE01.py` | `$RP8ZE01.py` | 执行登记件:L113 ／ 待清清单件:L125 | **无** | 史 |
| 78 | `_m5_k5_write.py` | 24,488 | `BF0CEE570FC4` | `$I9UW6TK.py` | `$R9UW6TK.py` | 执行登记件:L114 ／ 待清清单件:L126 | **无** | 史 |
| 79 | `_m5_reaudit_keyscan.py` | 1,107 | `16C00B54CFB1` | `$INACW2U.py` | `$RNACW2U.py` | 执行登记件:L115 ／ 待清清单件:L127 | **无** | 史 |
| 80 | `_m5_reaudit_write.py` | 24,862 | `89424CE195DF` | `$I27DCUD.py` | `$R27DCUD.py` | 执行登记件:L116 ／ 待清清单件:L128 | **无** | 史 |
| 81 | `_mk_voided_files_reference_update.py` | 19,073 | `769CDFB82F0A` | `$IVU2TNA.py` | `$RVU2TNA.py` | 执行登记件:L117 ／ 待清清单件:L129 | **无** | 史 |
| 82 | `_peek_lines.py` | 768 | `1578C5E68FB2` | `$IQUUJU2.py` | `$RQUUJU2.py` | 执行登记件:L118 ／ 待清清单件:L130 | **无** | 史 |
| 83 | `_pk_write_batch_rollout_design.py` | 84,939 | `41C40E6D40F0` | `$IZLXIU5.py` | `$RZLXIU5.py` | 执行登记件:L119 ／ 待清清单件:L131 | **无** | 史 |
| 84 | `_probe_5anchor_v1.py` | 3,145 | `D618B067A8A9` | `$ISH09VH.py` | `$RSH09VH.py` | 执行登记件:L120 ／ 待清清单件:L132 | **无** | 史 |
| 85 | `_tmp_mech_recheck.py` | 521 | `6BD7E0281F57` | `$IQG2FBU.py` | `$RQG2FBU.py` | 执行登记件:L121 ／ 待清清单件:L133 | **无** | 史 |
| 86 | `_tmp_mem_overhaul_verify.py` | 2,362 | `FE8C2E79AD2B` | `$IWLK0K6.py` | `$RWLK0K6.py` | 执行登记件:L122 ／ 待清清单件:L134 | **无** | 史 |
| 87 | `_tmp_mem_overhaul_write.py` | 19,101 | `C2FA52CEBDD4` | `$IZDLOGV.py` | `$RZDLOGV.py` | 执行登记件:L123 ／ 待清清单件:L135 | **无** | 史 |
| 88 | `_tmp_w1_stage2_stale_write.py` | 8,816 | `83C46B95E9D0` | `$IZXCW17.py` | `$RZXCW17.py` | 执行登记件:L124 ／ 待清清单件:L136 | **无** | 史 |
| 89 | `_v5_effect_verify.py` | 2,285 | `FD4D20645D93` | `$IVH197I.py` | `$RVH197I.py` | 执行登记件:L125 ／ 待清清单件:L137 | **无** | 史 |
| 90 | `_v5_effect_write.py` | 16,046 | `ED2C7FA3D546` | `$IO5PWB4.py` | `$RO5PWB4.py` | 执行登记件:L126 ／ 待清清单件:L138 | **无** | 史 |
| 91 | `_v5_hash.py` | 324 | `7EFF55336C46` | `$I712NYT.py` | `$R712NYT.py` | 执行登记件:L127 ／ 待清清单件:L139 | **无** | 史 |
| 92 | `_verify_5anchor_v1.py` | 1,793 | `25264633CF05` | `$I0OAE1P.py` | `$R0OAE1P.py` | 执行登记件:L128 ／ 待清清单件:L140 | **无** | 史 |
| 93 | `_verify_e_ascii.py` | 861 | `7A2EB324F1A1` | `$IAAYJHB.py` | `$RAAYJHB.py` | 执行登记件:L129 ／ 待清清单件:L141 | **无** | 史 |
| 94 | `_verify_mq_v7_effect_register.py` | 1,177 | `C8D08C5560C5` | `$IXOPXKU.py` | `$RXOPXKU.py` | 执行登记件:L130 ／ 待清清单件:L142 | **无** | 史 |
| 95 | `_verify_r1.py` | 1,232 | `69B68D434C77` | `$IAF7GXD.py` | `$RAF7GXD.py` | 执行登记件:L131 ／ 待清清单件:L143 | **无** | 史 |
| 96 | `_verify_v2_effects.py` | 4,218 | `351B1D76CC66` | `$ILXYMXE.py` | `$RLXYMXE.py` | 执行登记件:L132 ／ 待清清单件:L144 | **无** | 史 |
| 97 | `_verify_v8_deliverables.py` | 4,640 | `C98115980DDA` | `$IZS8TTM.py` | `$RZS8TTM.py` | 执行登记件:L133 ／ 待清清单件:L145 | **无** | 史 |
| 98 | `_w_c7_timeline.py` | 10,764 | `4A149505193E` | `$I4D8QNN.py` | `$R4D8QNN.py` | 执行登记件:L134 ／ 待清清单件:L146 | **无** | 史 |
| 99 | `_w_pb_reanchor.py` | 11,877 | `F4AB4A816B04` | `$IBWM5NK.py` | `$RBWM5NK.py` | 执行登记件:L135 ／ 待清清单件:L147 | **无** | 史 |
| 100 | `_w_v2_effect_register.py` | 15,777 | `7CA06EEA4A27` | `$IE8N80V.py` | `$RE8N80V.py` | 执行登记件:L136 ／ 待清清单件:L148 | **无** | 史 |
| 101 | `_wb_meta.py` | 1,210 | `8D3B7E8451C1` | `$IQZ07EF.py` | `$RQZ07EF.py` | 执行登记件:L137 ／ 待清清单件:L149 | **无** | 史 |
| 102 | `_wb_meta2.py` | 453 | `8547C39E78EE` | `$IDIHM6L.py` | `$RDIHM6L.py` | 执行登记件:L138 ／ 待清清单件:L150 | **无** | 史 |
| 103 | `_wb_meta3.py` | 455 | `BBDD5D19EAB5` | `$I2SOAR3.py` | `$R2SOAR3.py` | 执行登记件:L139 ／ 待清清单件:L151 | **无** | 史 |
| 104 | `_wb_meta4.py` | 718 | `90BF092CC15C` | `$I7TOI79.py` | `$R7TOI79.py` | 执行登记件:L140 ／ 待清清单件:L152 | **无** | 史 |
| 105 | `_wb_meta5.py` | 470 | `99C57DA75906` | `$I8L34JQ.py` | `$R8L34JQ.py` | 执行登记件:L141 ／ 待清清单件:L153 | **无** | 史 |
| 106 | `_wb_write_ge01_numeric_lit_2026_10_14.py` | 32,736 | `D6132717C8AA` | `$IZ6WLFD.py` | `$RZ6WLFD.py` | 执行登记件:L142 ／ 待清清单件:L154 | **无** | 史 |
| 107 | `_wb_write_ge01_t2t3.py` | 44,932 | `64447244C209` | `$IPQ1J3P.py` | `$RPQ1J3P.py` | 执行登记件:L143 ／ 待清清单件:L155 | **无** | 史 |
| 108 | `_worker_write_ge01_c3_gaps_disposition.py` | 34,641 | `7035F9FD6F83` | `$ITY3UXG.py` | `$RTY3UXG.py` | 执行登记件:L144 ／ 待清清单件:L156 | **无** | 史 |
| 109 | `_write_c2_effect_register.py` | 28,783 | `30891DD2B8DD` | `$IQ7CFLH.py` | `$RQ7CFLH.py` | 执行登记件:L145 ／ 待清清单件:L157 | **无** | 史 |
| 110 | `_write_c6_unblock.py` | 25,766 | `4D6811789D41` | `$IHV8G8X.py` | `$RHV8G8X.py` | 执行登记件:L146 ／ 待清清单件:L158 | **无** | 史 |
| 111 | `_write_mq_v7_effect_register.py` | 15,988 | `23035C1A4DD0` | `$IKCG40T.py` | `$RKCG40T.py` | 执行登记件:L147 ／ 待清清单件:L159 | **无** | 史 |
| 112 | `_write_v8_deliverables.py` | 32,192 | `934155D5103E` | `$IK16T3O.py` | `$RK16T3O.py` | 执行登记件:L148 ／ 待清清单件:L160 | **无** | 史 |
| 113 | `batch5_build.py` | 49,310 | `8E750C8A598E` | `$IN48D5W.py` | `$RN48D5W.py` | 执行登记件:L149 ／ 待清清单件:L161 | **无** | 史 |
| 114 | `batch5_patch.py` | 1,370 | `4BA9404D3EA4` | `$ILGX55Y.py` | `$RLGX55Y.py` | 执行登记件:L150 ／ 待清清单件:L162 | **无** | 史 |
| 115 | `batch5_patch2.py` | 667 | `351225ADF10F` | `$IM1RYVD.py` | `$RM1RYVD.py` | 执行登记件:L151 ／ 待清清单件:L163 | **无** | 史 |
| 116 | `docwriter_c5_register.py` | 17,726 | `B7CB69C339D7` | `$IZPJE2P.py` | `$RZPJE2P.py` | 执行登记件:L152 ／ 待清清单件:L164 | **无** | 史 |
| 117 | `dscan_referent.py` | 1,688 | `784EAE8C56F5` | `$ISMUK1X.py` | `$RSMUK1X.py` | 执行登记件:L153 ／ 待清清单件:L165 | **无** | 史 |
| 118 | `dscan_repo_exec.py` | 6,782 | `26E3CA3ED21A` | `$IWSDJZG.py` | `$RWSDJZG.py` | 执行登记件:L154 ／ 待清清单件:L166 | **无** | 史 |
| 119 | `dscan_repo_exec2.py` | 6,261 | `F626D359F649` | `$I5F8KA0.py` | `$R5F8KA0.py` | 执行登记件:L155 ／ 待清清单件:L167 | **无** | 史 |
| 120 | `dscan_repo_r1.py` | 2,074 | `2397F69099FA` | `$IKHNCB9.py` | `$RKHNCB9.py` | 执行登记件:L156 ／ 待清清单件:L168 | **无** | 史 |
| 121 | `dscan_repo_r1_dump.py` | 769 | `7A3B9AD13022` | `$IHV2294.py` | `$RHV2294.py` | 执行登记件:L157 ／ 待清清单件:L169 | **无** | 史 |
| 122 | `dscan_repo_state.py` | 1,880 | `C0C17BFFCC5A` | `$I45O7TV.py` | `$R45O7TV.py` | 执行登记件:L158 ／ 待清清单件:L170 | **无** | 史 |
| 123 | `dscan_repo_verify.py` | 5,739 | `7BAD157D050E` | `$IAXBRSC.py` | `$RAXBRSC.py` | 执行登记件:L159 ／ 待清清单件:L171 | **无** | 史 |
| 124 | `dscan_repo_write.py` | 32,700 | `E628380C804D` | `$IUMDUKK.py` | `$RUMDUKK.py` | 执行登记件:L160 ／ 待清清单件:L172 | **无** | 史 |
| 125 | `dscan_verify_01.py` | 1,294 | `85DFEC7684C0` | `$I1ZNRD3.py` | `$R1ZNRD3.py` | 执行登记件:L161 ／ 待清清单件:L173 | **无** | 史 |
| 126 | `dw_chk_mq20.py` | 302 | `A0AA18C1220C` | `$I60T63M.py` | `$R60T63M.py` | 执行登记件:L162 ／ 待清清单件:L174 | **无** | 史 |
| 127 | `dw_dump_counts.py` | 665 | `61A5EB22FFB9` | `$I3RH2BG.py` | `$R3RH2BG.py` | 执行登记件:L163 ／ 待清清单件:L175 | **无** | 史 |
| 128 | `dw_dump_mqtable.py` | 394 | `D322214D0446` | `$II3LPVE.py` | `$RI3LPVE.py` | 执行登记件:L164 ／ 待清清单件:L176 | **无** | 史 |
| 129 | `dw_final_integrity.py` | 2,962 | `E116836CC67D` | `$IHL8YMN.py` | `$RHL8YMN.py` | 执行登记件:L165 ／ 待清清单件:L177 | **无** | 史 |
| 130 | `dw_sha_scan_deriv.py` | 845 | `E943E414710D` | `$I4X8WAU.py` | `$R4X8WAU.py` | 执行登记件:L166 ／ 待清清单件:L178 | **无** | 史 |
| 131 | `dw_sha_scan_effect.py` | 460 | `DA307DB0B0F6` | `$I304NTR.py` | `$R304NTR.py` | 执行登记件:L167 ／ 待清清单件:L179 | **无** | 史 |
| 132 | `dw_sha_scan_v9.py` | 1,034 | `14E82A0F4E4F` | `$I0KSXVN.py` | `$R0KSXVN.py` | 执行登记件:L168 ／ 待清清单件:L180 | **无** | 史 |
| 133 | `dw_verify_v9_effect.py` | 2,919 | `EDD30083C010` | `$IB5CLM9.py` | `$RB5CLM9.py` | 执行登记件:L169 ／ 待清清单件:L181 | **无** | 史 |
| 134 | `dw_write_v9_effect.py` | 29,939 | `68DD2C45DEE9` | `$IYZ3YCH.py` | `$RYZ3YCH.py` | 执行登记件:L170 ／ 待清清单件:L182 | **无** | 史 |
| 135 | `ea_anchor.py` | 3,671 | `8027BFBFB4AA` | `$IYAH171.py` | `$RYAH171.py` | 执行登记件:L171 ／ 待清清单件:L183 | **无** | 史 |
| 136 | `ea_anchor2.py` | 3,568 | `E500D6B195D2` | `$ILOQVM9.py` | `$RLOQVM9.py` | 执行登记件:L172 ／ 待清清单件:L184 | **无** | 史 |
| 137 | `ea_census.py` | 1,434 | `431C705B3358` | `$IGZX4HT.py` | `$RGZX4HT.py` | 执行登记件:L173 ／ 待清清单件:L185 | **无** | 史 |
| 138 | `ea_count.py` | 981 | `62E003BF57B7` | `$IJ50TIY.py` | `$RJ50TIY.py` | 执行登记件:L174 ／ 待清清单件:L186 | **无** | 史 |
| 139 | `ea_draft.py` | 1,967 | `FCDF9E7A3DD3` | `$IV9OFZ1.py` | `$RV9OFZ1.py` | 执行登记件:L175 ／ 待清清单件:L187 | **无** | 史 |
| 140 | `ea_patch.py` | 871 | `94529F6FED1A` | `$IS3SMS3.py` | `$RS3SMS3.py` | 执行登记件:L176 ／ 待清清单件:L188 | **无** | 史 |
| 141 | `ea_rerun.py` | 1,645 | `64153D10E694` | `$II18QSD.py` | `$RI18QSD.py` | 执行登记件:L177 ／ 待清清单件:L189 | **无** | 史 |
| 142 | `ea_rerun2.py` | 2,179 | `EC05E28033AF` | `$I8I99D7.py` | `$R8I99D7.py` | 执行登记件:L178 ／ 待清清单件:L190 | **无** | 史 |
| 143 | `ea_rerun3.py` | 1,931 | `0A9356F58054` | `$IYBG2C6.py` | `$RYBG2C6.py` | 执行登记件:L179 ／ 待清清单件:L191 | **无** | 史 |
| 144 | `ea_scan2.py` | 1,264 | `140D049B5172` | `$IUCUJWJ.py` | `$RUCUJWJ.py` | 执行登记件:L180 ／ 待清清单件:L192 | **无** | 史 |
| 145 | `ea_scan3.py` | 1,289 | `7C064EE268C1` | `$IQOGSKU.py` | `$RQOGSKU.py` | 执行登记件:L181 ／ 待清清单件:L193 | **无** | 史 |
| 146 | `ea_scan4.py` | 1,383 | `871F8FC83E98` | `$IOFKTPN.py` | `$ROFKTPN.py` | 执行登记件:L182 ／ 待清清单件:L194 | **无** | 史 |
| 147 | `ea_scan5.py` | 1,958 | `9B1681334AF6` | `$IGI468X.py` | `$RGI468X.py` | 执行登记件:L183 ／ 待清清单件:L195 | **无** | 史 |
| 148 | `ea_scan6.py` | 2,642 | `0E747BF48923` | `$IZWDLNK.py` | `$RZWDLNK.py` | 执行登记件:L184 ／ 待清清单件:L196 | **无** | 史 |
| 149 | `ea_scan7.py` | 1,003 | `F3F11744D8C4` | `$II3LUHN.py` | `$RI3LUHN.py` | 执行登记件:L185 ／ 待清清单件:L197 | **无** | 史 |
| 150 | `ea_scan8.py` | 464 | `DD933B8A45AB` | `$ITIFRVJ.py` | `$RTIFRVJ.py` | 执行登记件:L186 ／ 待清清单件:L198 | **无** | 史 |
| 151 | `ea_verify.py` | 2,383 | `F7D3A561DFF4` | `$IKXZLYV.py` | `$RKXZLYV.py` | 执行登记件:L187 ／ 待清清单件:L199 | **无** | 史 |
| 152 | `epsilon_check.py` | 1,516 | `6CFD253E53D1` | `$I4AE1LV.py` | `$R4AE1LV.py` | 执行登记件:L188 ／ 待清清单件:L200 | **无** | 史 |
| 153 | `epsilon_check2.py` | 1,695 | `27E0E5EE0BDF` | `$I5S8G99.py` | `$R5S8G99.py` | 执行登记件:L189 ／ 待清清单件:L201 | **无** | 史 |
| 154 | `gen_v4.py` | 24,695 | `B6C497726A72` | `$IW2CO3S.py` | `$RW2CO3S.py` | 执行登记件:L190 ／ 待清清单件:L202 | **无** | 史 |
| 155 | `glm_erratum_finalize_2026_10_14.py` | 1,640 | `E2F1FF316C97` | `$IOX72Y1.py` | `$ROX72Y1.py` | 执行登记件:L191 ／ 待清清单件:L203 | **无** | 史 |
| 156 | `glm_premise_scan_2026_10_14.py` | 1,979 | `76CFA463FD42` | `$IK6RH8Y.py` | `$RK6RH8Y.py` | 执行登记件:L192 ／ 待清清单件:L204 | **无** | 史 |
| 157 | `glm_wholepack_recompute_2026_10_14.py` | 4,654 | `84A6BA873A1F` | `$I8424ZT.py` | `$R8424ZT.py` | 执行登记件:L193 ／ 待清清单件:L205 | **无** | 史 |
| 158 | `h_census1.py` | 1,091 | `970612ECF7E6` | `$IRB5BM0.py` | `$RRB5BM0.py` | 执行登记件:L194 ／ 待清清单件:L206 | **无** | 史 |
| 159 | `h_census2.py` | 1,054 | `621E17F32E0C` | `$I3S1560.py` | `$R3S1560.py` | 执行登记件:L195 ／ 待清清单件:L207 | **无** | 史 |
| 160 | `h_final.py` | 988 | `51499F458F94` | `$IOKJOPY.py` | `$ROKJOPY.py` | 执行登记件:L196 ／ 待清清单件:L208 | **无** | 史 |
| 161 | `h_final2.py` | 607 | `3D445C007077` | `$IIS90MY.py` | `$RIS90MY.py` | 执行登记件:L197 ／ 待清清单件:L209 | **无** | 史 |
| 162 | `h_final3.py` | 627 | `74F1A18D34CE` | `$IN8A6R2.py` | `$RN8A6R2.py` | 执行登记件:L198 ／ 待清清单件:L210 | **无** | 史 |
| 163 | `h_verify.py` | 1,033 | `115CC19FD78F` | `$IZVAMQ0.py` | `$RZVAMQ0.py` | 执行登记件:L200 ／ 待清清单件:L212 | **无** | 史 |
| 164 | `h_write_carrier.py` | 17,212 | `C33C689E1A77` | `$IFT5W20.py` | `$RFT5W20.py` | 执行登记件:L201 ／ 待清清单件:L213 | **无** | 史 |
| 165 | `h_write_register.py` | 23,246 | `8F2A77936667` | `$I5HGAVK.py` | `$R5HGAVK.py` | 执行登记件:L202 ／ 待清清单件:L214 | **无** | 史 |
| 166 | `loc.py` | 431 | `351145063CB0` | `$IUIXZSG.py` | `$RUIXZSG.py` | 执行登记件:L203 ／ 待清清单件:L215 | **无** | 史 |
| 167 | `loc1.py` | 627 | `6D918AC38D7C` | `$IZJSAA7.py` | `$RZJSAA7.py` | 执行登记件:L204 ／ 待清清单件:L216 | **无** | 史 |
| 168 | `m2_docwriter_measure.py` | 1,599 | `1333784DCC49` | `$IXD88MP.py` | `$RXD88MP.py` | 执行登记件:L205 ／ 待清清单件:L217 | **无** | 史 |
| 169 | `m2_docwriter_probe.py` | 1,105 | `A473EA7E2350` | `$IHOIGRA.py` | `$RHOIGRA.py` | 执行登记件:L206 ／ 待清清单件:L218 | **无** | 史 |
| 170 | `m2_docwriter_probe2.py` | 1,791 | `E89D2AED1219` | `$IJJT4PO.py` | `$RJJT4PO.py` | 执行登记件:L207 ／ 待清清单件:L219 | **无** | 史 |
| 171 | `m2_docwriter_verify.py` | 1,157 | `0C23CD7AB2AC` | `$IUTX3V7.py` | `$RUTX3V7.py` | 执行登记件:L208 ／ 待清清单件:L220 | **无** | 史 |
| 172 | `m2_probe.py` | 3,461 | `5658C387D6B5` | `$IMIVIQQ.py` | `$RMIVIQQ.py` | 执行登记件:L209 ／ 待清清单件:L221 | **无** | 史 |
| 173 | `m2_probe2.py` | 2,667 | `D139698132D0` | `$ISRNKPZ.py` | `$RSRNKPZ.py` | 执行登记件:L210 ／ 待清清单件:L222 | **无** | 史 |
| 174 | `m2_probe3.py` | 2,390 | `04AF6FED2703` | `$IDMEL32.py` | `$RDMEL32.py` | 执行登记件:L211 ／ 待清清单件:L223 | **无** | 史 |
| 175 | `m2_probe5.py` | 1,460 | `E08CC1A453E5` | `$IVOJR5L.py` | `$RVOJR5L.py` | 执行登记件:L212 ／ 待清清单件:L224 | **无** | 史 |
| 176 | `m2_probe7.py` | 2,301 | `AC26ADB86EA9` | `$I173RSE.py` | `$R173RSE.py` | 执行登记件:L213 ／ 待清清单件:L225 | **无** | 史 |
| 177 | `m2verdict_check2.py` | 1,728 | `3474CE7B820E` | `$IKRABN5.py` | `$RKRABN5.py` | 执行登记件:L214 ／ 待清清单件:L226 | **无** | 史 |
| 178 | `m2verdict_check3.py` | 952 | `82ECDABF1FD2` | `$IV7VGAB.py` | `$RV7VGAB.py` | 执行登记件:L215 ／ 待清清单件:L227 | **无** | 史 |
| 179 | `m2verdict_check4.py` | 1,600 | `976916ED916C` | `$IIQHJJ8.py` | `$RIQHJJ8.py` | 执行登记件:L216 ／ 待清清单件:L228 | **无** | 史 |
| 180 | `m2verdict_confirm.py` | 904 | `92A4CF48DC0E` | `$IILAVK0.py` | `$RILAVK0.py` | 执行登记件:L217 ／ 待清清单件:L229 | **无** | 史 |
| 181 | `m2verdict_lines.py` | 2,007 | `5077FC416ADC` | `$IZRU5GK.py` | `$RZRU5GK.py` | 执行登记件:L218 ／ 待清清单件:L230 | **无** | 史 |
| 182 | `m2verdict_lines2.py` | 1,428 | `ACDE200B467B` | `$I4GAG4D.py` | `$R4GAG4D.py` | 执行登记件:L219 ／ 待清清单件:L231 | **无** | 史 |
| 183 | `m2verdict_verify.py` | 2,516 | `CB3291DB8BAE` | `$IA7KKS0.py` | `$RA7KKS0.py` | 执行登记件:L220 ／ 待清清单件:L232 | **无** | 史 |
| 184 | `m2verdict_write.py` | 33,043 | `0DABD18535AD` | `$IT4ACN8.py` | `$RT4ACN8.py` | 执行登记件:L221 ／ 待清清单件:L233 | **无** | 史 |
| 185 | `m41_fix_diag.py` | 2,862 | `F45AD6BFE98C` | `$IK8M8OC.py` | `$RK8M8OC.py` | 执行登记件:L222 ／ 待清清单件:L234 ／ M41执行件:L273 ／ M41判定登记件:L164 | **乙** | 活 |
| 186 | `m41_rerun_dual_readout.py` | 11,615 | `4ACF8A4FBE6C` | `$ILBNWD4.py` | `$RLBNWD4.py` | 执行登记件:L223 ／ 待清清单件:L235 | **无** | 史 |
| 187 | `m41_rerun_endpoint_probe.py` | 1,908 | `EAAD608625C8` | `$IBU6PPS.py` | `$RBU6PPS.py` | 执行登记件:L224 ／ 待清清单件:L236 | **无** | 史 |
| 188 | `m41_rerun_probe2.py` | 3,293 | `C2360AB5B97F` | `$IM96G5A.py` | `$RM96G5A.py` | 执行登记件:L225 ／ 待清清单件:L237 | **无** | 史 |
| 189 | `m41_rerun_probe3.py` | 1,994 | `0323A3BB9A63` | `$IFKOVUK.py` | `$RFKOVUK.py` | 执行登记件:L226 ／ 待清清单件:L238 | **无** | 史 |
| 190 | `m41_rerun_probe4.py` | 2,210 | `D273BAA480B4` | `$IQ6JC4M.py` | `$RQ6JC4M.py` | 执行登记件:L227 ／ 待清清单件:L239 | **无** | 史 |
| 191 | `m41_rerun_probe5.py` | 1,760 | `F8ABFA046BB1` | `$IJSJV4R.py` | `$RJSJV4R.py` | 执行登记件:L228 ／ 待清清单件:L240 | **无** | 史 |
| 192 | `m41_rerun_probe6.py` | 1,942 | `385EA4324E73` | `$IIH2MLL.py` | `$RIH2MLL.py` | 执行登记件:L229 ／ 待清清单件:L241 | **无** | 史 |
| 193 | `m41_rerun_probe7.py` | 1,990 | `CB93891E5AD5` | `$I1T7IS9.py` | `$R1T7IS9.py` | 执行登记件:L230 ／ 待清清单件:L242 | **无** | 史 |
| 194 | `m41_rerun_probe8.py` | 2,316 | `513EC74DBA84` | `$IO7TK5V.py` | `$RO7TK5V.py` | 执行登记件:L231 ／ 待清清单件:L243 | **无** | 史 |
| 195 | `mq19i6_s10_render.py` | 29,373 | `61E08A86C692` | `$IDF4Y5A.py` | `$RDF4Y5A.py` | 执行登记件:L232 ／ 待清清单件:L244 | **无** | 史 |
| 196 | `mq19i6_s11_reverify.py` | 1,974 | `2D43DE763EDC` | `$IOLBWK6.py` | `$ROLBWK6.py` | 执行登记件:L233 ／ 待清清单件:L245 | **无** | 史 |
| 197 | `mq19i6_s12_selfcheck.py` | 1,699 | `B8C01102097F` | `$IQW0R72.py` | `$RQW0R72.py` | 执行登记件:L234 ／ 待清清单件:L246 | **无** | 史 |
| 198 | `mq19i6_s1_inventory.py` | 2,439 | `9EF7C5EC930C` | `$IRW0Q3Q.py` | `$RRW0Q3Q.py` | 执行登记件:L235 ／ 待清清单件:L247 | **无** | 史 |
| 199 | `mq19i6_s2_parse.py` | 1,983 | `ABDC24641D0E` | `$IBVJW85.py` | `$RBVJW85.py` | 执行登记件:L236 ／ 待清清单件:L248 | **无** | 史 |
| 200 | `mq19i6_s3_digest.py` | 1,795 | `C1B90147BB93` | `$IDWZYO2.py` | `$RDWZYO2.py` | 执行登记件:L237 ／ 待清清单件:L249 | **无** | 史 |
| 201 | `mq19i6_s4_anchors.py` | 4,390 | `C35F7C3A6A9D` | `$IO6DP4V.py` | `$RO6DP4V.py` | 执行登记件:L238 ／ 待清清单件:L250 | **无** | 史 |
| 202 | `mq19i6_s4b_probe.py` | 816 | `F6975DCEDD59` | `$IY37CIO.py` | `$RY37CIO.py` | 执行登记件:L239 ／ 待清清单件:L251 | **无** | 史 |
| 203 | `mq19i6_s5_verdict.py` | 6,442 | `CD4977E89D3D` | `$IKMHG0I.py` | `$RKMHG0I.py` | 执行登记件:L240 ／ 待清清单件:L252 | **无** | 史 |
| 204 | `mq19i6_s6_final.py` | 3,835 | `EE73F35D2D29` | `$IGYCAUF.py` | `$RGYCAUF.py` | 执行登记件:L241 ／ 待清清单件:L253 | **无** | 史 |
| 205 | `mq19i6_s7_detail.py` | 1,631 | `9352812D73A4` | `$ISBT0JT.py` | `$RSBT0JT.py` | 执行登记件:L242 ／ 待清清单件:L254 | **无** | 史 |
| 206 | `mq19i6_s8_retest.py` | 3,418 | `50177A3FC1D6` | `$INQ01SP.py` | `$RNQ01SP.py` | 执行登记件:L243 ／ 待清清单件:L255 | **无** | 史 |
| 207 | `mq19i6_s9_negdetail.py` | 1,763 | `947C3EAADE0F` | `$I7WW82Y.py` | `$R7WW82Y.py` | 执行登记件:L244 ／ 待清清单件:L256 | **无** | 史 |
| 208 | `pk_audit.py` | 2,980 | `C60A2AFEDE5A` | `$IZ56UXB.py` | `$RZ56UXB.py` | 执行登记件:L245 ／ 待清清单件:L257 | **无** | 史 |
| 209 | `pk_kl.py` | 614 | `20EA4E0B5DA8` | `$IZMX9K0.py` | `$RZMX9K0.py` | 执行登记件:L246 ／ 待清清单件:L258 | **无** | 史 |
| 210 | `pk_measure_02.py` | 2,590 | `F91F5C5CC3C6` | `$IURHYW0.py` | `$RURHYW0.py` | 执行登记件:L247 ／ 待清清单件:L259 | **无** | 史 |
| 211 | `pk_measure_03.py` | 3,031 | `543980697A2F` | `$IOFEWHN.py` | `$ROFEWHN.py` | 执行登记件:L248 ／ 待清清单件:L260 | **无** | 史 |
| 212 | `pk_measure_04.py` | 2,505 | `35FC55C84FF5` | `$I3UYLFA.py` | `$R3UYLFA.py` | 执行登记件:L249 ／ 待清清单件:L261 | **无** | 史 |
| 213 | `pk_measure_05.py` | 1,577 | `3D4D6639B76C` | `$IYDI9RD.py` | `$RYDI9RD.py` | 执行登记件:L250 ／ 待清清单件:L262 | **无** | 史 |
| 214 | `pk_measure_06.py` | 2,692 | `9998A8992428` | `$IV1MWMK.py` | `$RV1MWMK.py` | 执行登记件:L251 ／ 待清清单件:L263 | **无** | 史 |
| 215 | `pk_occ.py` | 554 | `CADD708E3864` | `$IPUKHX5.py` | `$RPUKHX5.py` | 执行登记件:L252 ／ 待清清单件:L264 | **无** | 史 |
| 216 | `pk_v6v9.py` | 483 | `62D78A2B5E6E` | `$I649C7Z.py` | `$R649C7Z.py` | 执行登记件:L253 ／ 待清清单件:L265 | **无** | 史 |
| 217 | `pk_v9card.py` | 249 | `8AE98D577A41` | `$IG7LK7F.py` | `$RG7LK7F.py` | 执行登记件:L254 ／ 待清清单件:L266 | **无** | 史 |
| 218 | `pk_verify_src.py` | 705 | `6EBD138F9FD2` | `$I9PMWYF.py` | `$R9PMWYF.py` | 执行登记件:L255 ／ 待清清单件:L267 | **无** | 史 |
| 219 | `pk_write1.py` | 897 | `98614C01FF0B` | `$IJ6EQE9.py` | `$RJ6EQE9.py` | 执行登记件:L256 ／ 待清清单件:L268 | **无** | 史 |
| 220 | `pk_write2.py` | 869 | `03A126A170CF` | `$ITZQQKT.py` | `$RTZQQKT.py` | 执行登记件:L257 ／ 待清清单件:L269 | **无** | 史 |
| 221 | `pk_write_01.py` | 38,538 | `9322F2AC1994` | `$ISRU2I7.py` | `$RSRU2I7.py` | 执行登记件:L258 ／ 待清清单件:L270 | **无** | 史 |
| 222 | `pre_v6.py` | 948 | `9E487A5BE822` | `$I94FZEZ.py` | `$R94FZEZ.py` | 执行登记件:L259 ／ 待清清单件:L271 | **无** | 史 |
| 223 | `precheck_v4.py` | 803 | `98B9E1F9F26A` | `$I5QF2GR.py` | `$R5QF2GR.py` | 执行登记件:L260 ／ 待清清单件:L272 | **无** | 史 |
| 224 | `r461_probe_01.py` | 3,844 | `2FF4A89AE4FA` | `$I541QI8.py` | `$R541QI8.py` | 执行登记件:L261 ／ 待清清单件:L273 | **无** | 史 |
| 225 | `r461_probe_02.py` | 4,387 | `398795C14489` | `$IBPCE5F.py` | `$RBPCE5F.py` | 执行登记件:L262 ／ 待清清单件:L274 | **无** | 史 |
| 226 | `r461_probe_03.py` | 4,681 | `C3B2F3CFAA8B` | `$IDR33IZ.py` | `$RDR33IZ.py` | 执行登记件:L263 ／ 待清清单件:L275 | **无** | 史 |
| 227 | `r461_probe_04.py` | 9,821 | `A0F7794A4245` | `$IIHPVB0.py` | `$RIHPVB0.py` | 执行登记件:L264 ／ 待清清单件:L276 | **无** | 史 |
| 228 | `r461_probe_05.py` | 10,455 | `8B43674101E1` | `$IIL1TVT.py` | `$RIL1TVT.py` | 执行登记件:L265 ／ 待清清单件:L277 | **无** | 史 |
| 229 | `r461_probe_06.py` | 8,805 | `56D5B11C9298` | `$ICKW2A7.py` | `$RCKW2A7.py` | 执行登记件:L266 ／ 待清清单件:L278 | **无** | 史 |
| 230 | `r461_probe_07.py` | 8,102 | `3AEE3606E0B6` | `$IDT56TE.py` | `$RDT56TE.py` | 执行登记件:L267 ／ 待清清单件:L279 | **无** | 史 |
| 231 | `r461_probe_08.py` | 9,075 | `BB8A0D09D52D` | `$IM09WPC.py` | `$RM09WPC.py` | 执行登记件:L268 ／ 待清清单件:L280 | **无** | 史 |
| 232 | `r461_probe_09.py` | 6,657 | `86FF4FF150FD` | `$I5AMUWX.py` | `$R5AMUWX.py` | 执行登记件:L269 ／ 待清清单件:L281 | **无** | 史 |
| 233 | `r461_probe_10.py` | 7,155 | `A512FBFDD122` | `$IT2LSXR.py` | `$RT2LSXR.py` | 执行登记件:L270 ／ 待清清单件:L282 | **无** | 史 |
| 234 | `r461_probe_11.py` | 7,456 | `92D72C002014` | `$IYZJUOL.py` | `$RYZJUOL.py` | 执行登记件:L271 ／ 待清清单件:L283 | **无** | 史 |
| 235 | `r461_probe_12.py` | 9,523 | `E1881790642B` | `$I5I771J.py` | `$R5I771J.py` | 执行登记件:L272 ／ 待清清单件:L284 | **无** | 史 |
| 236 | `r461_probe_13.py` | 5,731 | `BDD97CED522E` | `$I7I63B0.py` | `$R7I63B0.py` | 执行登记件:L273 ／ 待清清单件:L285 | **无** | 史 |
| 237 | `r461_probe_14.py` | 6,891 | `7B365CE4E9DB` | `$IN6XAOX.py` | `$RN6XAOX.py` | 执行登记件:L274 ／ 待清清单件:L286 | **无** | 史 |
| 238 | `r461_probe_15.py` | 6,617 | `FF4A4E5EB20E` | `$ID36SIG.py` | `$RD36SIG.py` | 执行登记件:L275 ／ 待清清单件:L287 | **无** | 史 |
| 239 | `r461_probe_16.py` | 8,118 | `A5D1D955E86F` | `$IYOMEDO.py` | `$RYOMEDO.py` | 执行登记件:L276 ／ 待清清单件:L288 | **无** | 史 |
| 240 | `r461_probe_17.py` | 5,978 | `E48337117C54` | `$IKMZA3M.py` | `$RKMZA3M.py` | 执行登记件:L277 ／ 待清清单件:L289 | **无** | 史 |
| 241 | `r461_probe_18.py` | 6,583 | `6E27F300D093` | `$IZ0JSJT.py` | `$RZ0JSJT.py` | 执行登记件:L278 ／ 待清清单件:L290 | **无** | 史 |
| 242 | `r461_write_02.py` | 6,292 | `CA9D22D2DFFC` | `$IGCR7P3.py` | `$RGCR7P3.py` | 执行登记件:L279 ／ 待清清单件:L291 | **无** | 史 |
| 243 | `r6_supp_fv_scan_2026_10_14.py` | 3,333 | `BFE4BE024F04` | `$I9K3ODY.py` | `$R9K3ODY.py` | 执行登记件:L280 ／ 待清清单件:L292 | **无** | 史 |
| 244 | `r6_supp_fv_write_2026_10_14.py` | 21,384 | `5E6516952A49` | `$IMLWVN2.py` | `$RMLWVN2.py` | 执行登记件:L281 ／ 待清清单件:L293 | **无** | 史 |
| 245 | `repair_ge01.py` | 2,490 | `6E5E5C15D943` | `$IVL85X0.py` | `$RVL85X0.py` | 执行登记件:L282 ／ 待清清单件:L294 | **无** | 史 |
| 246 | `verbatim_diff.py` | 1,173 | `1DD0A9DDEA1C` | `$IQNDSRE.py` | `$RQNDSRE.py` | 执行登记件:L283 ／ 待清清单件:L295 | **无** | 史 |
| 247 | `verify_ge01_final.py` | 1,826 | `45981937A49F` | `$IDFQQ46.py` | `$RDFQQ46.py` | 执行登记件:L284 ／ 待清清单件:L296 | **无** | 史 |
| 248 | `verify_ge01_probe1.py` | 1,359 | `26380A207AAE` | `$I8ECGGT.py` | `$R8ECGGT.py` | 执行登记件:L285 ／ 待清清单件:L297 | **无** | 史 |
| 249 | `verify_ge01_probe2.py` | 3,894 | `197C61107EA8` | `$I4CKH0X.py` | `$R4CKH0X.py` | 执行登记件:L286 ／ 待清清单件:L298 | **无** | 史 |
| 250 | `verify_ge01_probe3.py` | 3,515 | `FE79E4004CF9` | `$I7XRXY0.py` | `$R7XRXY0.py` | 执行登记件:L287 ／ 待清清单件:L299 | **无** | 史 |
| 251 | `verify_ge01_probe4.py` | 4,156 | `8CE881670771` | `$I8CMG66.py` | `$R8CMG66.py` | 执行登记件:L288 ／ 待清清单件:L300 | **无** | 史 |
| 252 | `verify_ge01_probe5.py` | 3,589 | `6C93EFE1B680` | `$IZ3DA6I.py` | `$RZ3DA6I.py` | 执行登记件:L289 ／ 待清清单件:L301 | **无** | 史 |
| 253 | `verify_ge01_probe6.py` | 3,932 | `0439CF951738` | `$I0GX9QE.py` | `$R0GX9QE.py` | 执行登记件:L290 ／ 待清清单件:L302 | **无** | 史 |
| 254 | `verify_ge01_probe7.py` | 524 | `CD0664C535FF` | `$IUEK2GJ.py` | `$RUEK2GJ.py` | 执行登记件:L291 ／ 待清清单件:L303 | **无** | 史 |
| 255 | `verify_ge01_probe8.py` | 1,528 | `CE4FBC5CEDC3` | `$I1H25D4.py` | `$R1H25D4.py` | 执行登记件:L292 ／ 待清清单件:L304 | **无** | 史 |
| 256 | `verify_ge01_probe9.py` | 1,626 | `62499FE3B8A4` | `$ISDTJ23.py` | `$RSDTJ23.py` | 执行登记件:L293 ／ 待清清单件:L305 | **无** | 史 |
| 257 | `verify_v4.py` | 2,377 | `6BFC05B4DE04` | `$IFRUCWV.py` | `$RFRUCWV.py` | 执行登记件:L294 ／ 待清清单件:L306 | **无** | 史 |
| 258 | `verify_v6.py` | 2,664 | `4A4ABF42C4DF` | `$IXKD0FY.py` | `$RXKD0FY.py` | 执行登记件:L295 ／ 待清清单件:L307 | **无** | 史 |
| 259 | `verify_v6b.py` | 1,537 | `6FC905728DB8` | `$IV4IJC6.py` | `$RV4IJC6.py` | 执行登记件:L296 ／ 待清清单件:L308 | **无** | 史 |
| 260 | `verify_v6c.py` | 1,367 | `9E62126B6B67` | `$IG7Y5IF.py` | `$RG7Y5IF.py` | 执行登记件:L297 ／ 待清清单件:L309 | **无** | 史 |
| 261 | `verify_v6d.py` | 514 | `4BD2FE616E42` | `$IJ6R976.py` | `$RJ6R976.py` | 执行登记件:L298 ／ 待清清单件:L310 | **无** | 史 |
| 262 | `verify_v6e.py` | 954 | `45CAEDC9121C` | `$I4T96LZ.py` | `$R4T96LZ.py` | 执行登记件:L299 ／ 待清清单件:L311 | **无** | 史 |
| 263 | `verify_v6f.py` | 1,136 | `A958F1FDC060` | `$IEK0THO.py` | `$REK0THO.py` | 执行登记件:L300 ／ 待清清单件:L312 | **无** | 史 |
| 264 | `write_ge01_readiness.py` | 33,215 | `B7DAFAD2B38D` | `$IAU4MJT.py` | `$RAU4MJT.py` | 执行登记件:L301 ／ 待清清单件:L313 | **无** | 史 |
| 265 | `write_v6.py` | 788 | `70660C1CAEE8` | `$I2BAKVX.py` | `$R2BAKVX.py` | 执行登记件:L302 ／ 待清清单件:L314 | **无** | 史 |
| 266 | `xiang14_build.py` | 15,168 | `DF469332A35F` | `$IZCX2HQ.py` | `$RZCX2HQ.py` | 执行登记件:L303 ／ 待清清单件:L315 | **无** | 史 |
| 267 | `xiang14_coverage.py` | 2,123 | `A81270B214C0` | `$IC9408L.py` | `$RC9408L.py` | 执行登记件:L304 ／ 待清清单件:L316 | **无** | 史 |
| 268 | `xiang14_map.py` | 1,457 | `781E3ECFA888` | `$I2MY3VN.py` | `$R2MY3VN.py` | 执行登记件:L305 ／ 待清清单件:L317 | **无** | 史 |
| 269 | `xiang14_measure.py` | 2,732 | `BE53A6E1A708` | `$IKV6YVA.py` | `$RKV6YVA.py` | 执行登记件:L306 ／ 待清清单件:L318 | **无** | 史 |
| 270 | `xiang14_reissue3_build.py` | 28,965 | `06F921A99EBB` | `$ISS5JTS.py` | `$RSS5JTS.py` | 执行登记件:L307 ／ 待清清单件:L319 | **无** | 史 |
| 271 | `xiang14_reissue3_counts.py` | 1,513 | `9A0AE783EC09` | `$ISQIJM8.py` | `$RSQIJM8.py` | 执行登记件:L308 ／ 待清清单件:L320 | **无** | 史 |
| 272 | `xiang14_reissue3_dump_v1.py` | 422 | `0EBA143EB784` | `$IHJDV2I.py` | `$RHJDV2I.py` | 执行登记件:L309 ／ 待清清单件:L321 | **无** | 史 |
| 273 | `xiang14_reissue3_scan.py` | 2,323 | `39AA1FB716D5` | `$IOI9303.py` | `$ROI9303.py` | 执行登记件:L310 ／ 待清清单件:L322 | **无** | 史 |

**A1 处置汇总**：建议**无**需处置 **272** 项（＝引用为清理史实之真实陈述）；建议**乙**（另立件并列勘误注记）**1** 项（`m41_fix_diag.py`，因另见活文档引用）。**建议甲者 0 项**——甲双通道实测皆空，无一可行。

**乙 之执行形态（若 PI 核准；仅出方案·本棒 ⛔0 执行）**：另立 `results/_a1_erratum_m41_fix_diag_ref_2026_10_17.md`，载明：`.tmp/m41_fix_diag.py` 于 2026-10-15 经授权清理删除（登记件第 189 行，`$I`=`$IK8M8OC.py`／`$R`=`$RK8M8OC.py`，两通道现已清空故不可恢复）；其于 M41 执行件 L273、M41 判定登记件 L164 之引用系**指向已删件之历史引用**；后续复算须重建该诊断件。⛔0 回改 M41 二件原文。

---

## §4 A2 层（326 项·既有缺陷）之建议

### §4.1 处置取向

A2 之 326 项**不在** 10-15 执行表内 ⇒ 其删除事件**先于**该次清理且**多不可考**（无 `$I`/`$R` 记录、无 SHA 登记）。故：

- **乙（改登记）为主**：以另立件之勘误注记，记「该目标已不存于 `.tmp/`，原删除事件不可考」，⛔0 回改原件。
- **丙（迁移）为副**：15 项于外部非上传归档内**按同名可寻得实体**，可就地校验后迁移至 `.tmp/` 或改登记指向新址（下表 §4.3）。
- **甲（回填）不建议**：A2 无删除事件记录，无从判断原字节；即便可寻得同名件，亦须先校 SHA-12 再议，**本棒 ⛔0 执行**。

### §4.2 高频项单列（引用处 ≥ 5 件者，共 45 项）

| 目标名 | 引用处 | 引用件数 | 归档可寻 |
| :-- | --: | --: | :-- |
| `_t15r2_records.json` | 44 | 14 | 否 |
| `c5_guard_minmaxstd_2026_10_01.py` | 21 | 10 | 否 |
| `_exp06_1009fix_build_2026_10_10.py` | 17 | 6 | 否 |
| `_exp06_1009fix_verify_2026_10_10.py` | 17 | 6 | 否 |
| `_l14_records.json` | 17 | 12 | 否 |
| `exp06_supplement_probe_2026_10_10.py` | 15 | 8 | 否 |
| `_exp06_fixcopy_verify_probe_2026_10_10.py` | 13 | 7 | 否 |
| `_l14v3_aggregated_10cells_v4.json` | 13 | 8 | 否 |
| `_t1_records.json` | 13 | 10 | 否 |
| `_l14v3_n26_metrics_v2.json` | 12 | 8 | 否 |
| `_l14v3_sensitivity_v2.json` | 12 | 8 | 否 |
| `exp06_independent_json_gen_2026_10_10.py` | 11 | 6 | 否 |
| `_verify_d_fix2_metric_9m60c_2026_09_15.py` | 10 | 7 | **是**（`results/.tmp/_verify_d_fix2_metric_9m60c_2026_09_15.py`） |
| `_exp06_1009fix_lnref_2026_10_10.py` | 9 | 5 | 否 |
| `scan_five_terminal_2026_10_10.py` | 9 | 5 | 否 |
| `_pk_probe5.py` | 8 | 7 | 否 |
| `_postproc_d_fix2_metric_2026_09_15.py` | 8 | 5 | **是**（`results/.tmp/_postproc_d_fix2_metric_2026_09_15.py`） |
| `_s4_tree_construct_probe_2026_10_10.py` | 8 | 5 | 否 |
| `_t15_inspect3_out.txt` | 8 | 6 | 否 |
| `_t15r2_checkpoint_warn.jsonl` | 8 | 8 | 否 |
| `verif_doubt6/baseline_pre.json` | 8 | 7 | **是**（`_movedout_scratch_2026_10_01/verif_doubt6_prestate/baseline_pre.json`） |
| `_iscp_caliber_probe_2026_10_09.py` | 7 | 5 | 否 |
| `_pk_probe2.py` | 7 | 6 | 否 |
| `_pk_probe3.py` | 7 | 6 | 否 |
| `_pk_probe4.py` | 7 | 6 | 否 |
| `_pk_probe8.py` | 7 | 6 | 否 |
| `_t15_inspect7_out.txt` | 7 | 6 | 否 |
| `_v16_full_decoded.txt` | 7 | 6 | 否 |
| `_cpatomic_pycache_pre_2026_09_28.json` | 6 | 5 | 否 |
| `_l14v3_aggregated_10cells.json` | 6 | 6 | 否 |
| `_l14v3_n26_metrics.json` | 6 | 6 | 否 |
| `_pkf34_probe1.py` | 6 | 5 | 否 |
| `_pkf34_probe2.py` | 6 | 5 | 否 |
| `_t15_inspect4_out.txt` | 6 | 5 | 否 |
| `_t15_inspect5_out.txt` | 6 | 5 | 否 |
| `_t15_inspect6_out.txt` | 6 | 5 | 否 |
| `_t15_percell.txt` | 6 | 5 | 否 |
| `_t15_percell_out.txt` | 6 | 5 | 否 |
| `_v16_tail_dump.txt` | 6 | 5 | 否 |
| `_cpatomic_keyscan_2026_09_28.json` | 5 | 5 | 否 |
| `_cpatomic_patch_manifest_2026_09_28.json` | 5 | 5 | 否 |
| `_cpatomic_pycache_post_2026_09_28.json` | 5 | 5 | 否 |
| `_cpatomic_verify_2026_09_28.json` | 5 | 5 | 否 |
| `_r4_key_scan_results_2026_09_24.json` | 5 | 5 | 否 |
| `_v16_tail_only.txt` | 5 | 5 | 否 |

> 派工单点名之两项**均已复现**：`_t15r2_records.json` **44 处 / 14 件**（与转述「44 处」**吻合**）；`c5_guard_minmaxstd_2026_10_01.py` **21 处 / 10 件**（与转述「21 处」**吻合**）。二者引用面横跨 `results/`、`letters/`、`docs/V3X/`，属**跨面传播**，建议列为 A2 之**首批乙（改登记）对象**。

### §4.3 丙（迁移）可行项——15 项

| 目标名 | 引用处 | 归档内实体（相对 `〔归档区〕`） |
| :-- | --: | :-- |
| `_verify_d_fix2_metric_9m60c_2026_09_15.py` | 10 | `results/.tmp/_verify_d_fix2_metric_9m60c_2026_09_15.py` |
| `_postproc_d_fix2_metric_2026_09_15.py` | 8 | `results/.tmp/_postproc_d_fix2_metric_2026_09_15.py` |
| `verif_doubt6/baseline_pre.json` | 8 | `_movedout_scratch_2026_10_01/verif_doubt6_prestate/baseline_pre.json` |
| `_pf_d1_full_2026_09_15.py` | 4 | `tmp/.tmp/_pf_d1_full_2026_09_15.py` |
| `_e50_c1.md` | 4 | `_movedout_scratch_2026_10_01/errata_drafts_2026_10_01/_e50_c1.md` |
| `_d1_full_run.log` | 3 | `tmp/.tmp/_d1_full_run.log` |
| `_verify_pf_d1_2026_09_15.py` | 3 | `tmp/.tmp/_verify_pf_d1_2026_09_15.py` |
| `_e50_c2.md` | 3 | `_movedout_scratch_2026_10_01/errata_drafts_2026_10_01/_e50_c2.md` |
| `_verify_15frozen_post.txt` | 3 | `tmp/.tmp/_verify_15frozen_post.txt` |
| `_verify_15frozen_run.txt` | 3 | `tmp/.tmp/_verify_15frozen_run.txt` |
| `_d1_runlog.txt` | 2 | `tmp/.tmp/_d1_runlog.txt` |
| `_verify_final.py` | 2 | `tmp/.tmp/_verify_final.py` |
| `verif_doubt6_v_20260928/_v5_trae_doubt6_verify_2026_09_28.md` | 2 | `_movedout_scratch_2026_09_29/verif_doubt6_v_20260928/_v5_trae_doubt6_verify_2026_09_28.md` |
| `verif_doubt6_v_20260928/baseline_mine.json` | 2 | `_movedout_scratch_2026_09_29/verif_doubt6_v_20260928/baseline_mine.json` |
| `verif_doubt6_v_20260928/_merged_canonical_snapshot_224910.md` | 2 | `_movedout_scratch_2026_09_29/verif_doubt6_v_20260928/_merged_canonical_snapshot_224910.md` |

> **注**：上列均**仅证「同名实体存在」**，⛔0 未校验 SHA-12（故 8 项中仅 2 项路径形态与原引用一致：`_postproc_d_fix2_metric_2026_09_15.py`、`_verify_d_fix2_metric_9m60c_2026_09_15.py` 落 `results/.tmp/`；其余落 `tmp/.tmp/` 或 `_movedout_scratch_*/`）。**迁移前须逐项校 SHA-12**，否则同名异体风险。

### §4.4 A2 全量清单（326 行）

| # | 目标名 | 引用处 | 引用件数 | 主要引用件（前 3） | 归档可寻 | 建议径 |
| --: | :-- | --: | --: | :-- | :-- | :-- |
| 1 | `_t15r2_records.json` | 44 | 14 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_v4_checkpoint_atomic_and_pycache_2026_09_28.md；_v4_exec_surface_switch_20 | 否 | **乙** |
| 2 | `c5_guard_minmaxstd_2026_10_01.py` | 21 | 10 | c5_guard_minmaxstd_2026_10_01.py；exp06_independent_json_gen_2026_10_10.py；_corpus_index_citation_surface_annot | 否 | **乙** |
| 3 | `_exp06_1009fix_build_2026_10_10.py` | 17 | 6 | _achievements_inventory_full_2026_10_09.md；_corpus_index_citation_surface_annotation_2026_10_12.md；_exp06_self | 否 | **乙** |
| 4 | `_exp06_1009fix_verify_2026_10_10.py` | 17 | 6 | _achievements_inventory_full_2026_10_09.md；_corpus_index_citation_surface_annotation_2026_10_12.md；_exp06_self | 否 | **乙** |
| 5 | `_l14_records.json` | 17 | 12 | l14_runner_v2.py；l14_runner_v2_r1_atomic_2026_09_29.py；_v4_supp_l14_n11full_verdict.md | 否 | **乙** |
| 6 | `exp06_supplement_probe_2026_10_10.py` | 15 | 8 | _achievements_inventory_full_2026_10_09.md；exp06_independent_json_gen_2026_10_10.py；_corpus_index_citation_sur | 否 | **乙** |
| 7 | `_exp06_fixcopy_verify_probe_2026_10_10.py` | 13 | 7 | _achievements_inventory_full_2026_10_09.md；_corpus_index_citation_surface_annotation_2026_10_12.md；_exp06_self | 否 | **乙** |
| 8 | `_l14v3_aggregated_10cells_v4.json` | 13 | 8 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 9 | `_t1_records.json` | 13 | 10 | _v4_supp_prereg_v02_add_L14V3_2026_09_24.md；_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md；_v4_supp_pr | 否 | **乙** |
| 10 | `_l14v3_n26_metrics_v2.json` | 12 | 8 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 11 | `_l14v3_sensitivity_v2.json` | 12 | 8 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 12 | `exp06_independent_json_gen_2026_10_10.py` | 11 | 6 | _achievements_inventory_full_2026_10_09.md；_corpus_index_citation_surface_annotation_2026_10_12.md；_exp06_supp | 否 | **乙** |
| 13 | `_verify_d_fix2_metric_9m60c_2026_09_15.py` | 10 | 7 | D7_POST_CLEANUP_PLAN_2026_09_18.json；D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md；_archive_manifest_non_upload_20 | 是 | **乙＋丙** |
| 14 | `l14_runner_v2.py` | 10 | 3 | l14_runner_v2.py；l14_runner_v2_r1_atomic_2026_09_29.py；_v5_checkpoint_tail3_revision_2026_09_29.md | 否 | **乙** |
| 15 | `_exp06_1009fix_lnref_2026_10_10.py` | 9 | 5 | _achievements_inventory_full_2026_10_09.md；_exp06_selfverified_renaming_note_2026_10_10.md；_repo_full_inventor | 否 | **乙** |
| 16 | `_probe_schema.py` | 9 | 4 | _numbering_659_overlap_semantic_review_2026_10_14.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_c | 否 | **乙** |
| 17 | `_rp4_probe_r7c.py` | 9 | 4 | _numbering_659_overlap_semantic_review_2026_10_14.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_c | 否 | **乙** |
| 18 | `scan_five_terminal_2026_10_10.py` | 9 | 5 | _achievements_inventory_full_2026_10_09.md；_five_terminal_judgments_ruling_2026_10_10.md；_repo_full_inventory_ | 否 | **乙** |
| 19 | `_pk_probe5.py` | 8 | 7 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_v4_wide_walkthrough_reply_trae_cod | 否 | **乙** |
| 20 | `_postproc_d_fix2_metric_2026_09_15.py` | 8 | 5 | D7_POST_CLEANUP_PLAN_2026_09_18.json；_archive_manifest_non_upload_2026_09_23.json；_ghostref_copy_log_2026_09_2 | 是 | **乙＋丙** |
| 21 | `_s4_tree_construct_probe_2026_10_10.py` | 8 | 5 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 22 | `_t15_inspect3_out.txt` | 8 | 6 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 23 | `_t15r2_checkpoint_warn.jsonl` | 8 | 8 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 24 | `verif_doubt6/baseline_pre.json` | 8 | 7 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_trae_direct_fix_re | 是 | **乙＋丙** |
| 25 | `_exp06_1009fix_lnref2_2026_10_10.py` | 7 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 26 | `_iscp_caliber_probe_2026_10_09.py` | 7 | 5 | _is_corr_pair_caliber_revision_proposal_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_ | 否 | **乙** |
| 27 | `_pk_probe2.py` | 7 | 6 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_v4_wide_walkthrough_reply_trae_cod | 否 | **乙** |
| 28 | `_pk_probe3.py` | 7 | 6 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_v4_wide_walkthrough_reply_trae_cod | 否 | **乙** |
| 29 | `_pk_probe4.py` | 7 | 6 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_v4_wide_walkthrough_reply_trae_cod | 否 | **乙** |
| 30 | `_pk_probe8.py` | 7 | 6 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_v4_wide_walkthrough_reply_trae_cod | 否 | **乙** |
| 31 | `_s4fill_probe4.py` | 7 | 4 | _corpus_index_citation_surface_annotation_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_pos | 否 | **乙** |
| 32 | `_t15_checkpoint_warn.jsonl` | 7 | 4 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_v4_supp_t15_executor_r1_2026_09_27.py；_v4_supp_t15_executor_r2_atomic_202 | 否 | **乙** |
| 33 | `_t15_inspect7_out.txt` | 7 | 6 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 34 | `_v16_full_decoded.txt` | 7 | 6 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_lo | 否 | **乙** |
| 35 | `e4_axis2_crosscheck_2026_10_10.py` | 7 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 36 | `e4_axis2_denominator_recheck_2026_10_10.py` | 7 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 37 | `e4_axis2_final_validation_2026_10_10.py` | 7 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 38 | `e4_axis2_hit_unchanged_probe_2026_10_10.py` | 7 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 39 | `e4_axis2_v11_displacement_run_2026_10_10.py` | 7 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 40 | `_cpatomic_pycache_pre_2026_09_28.json` | 6 | 5 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 41 | `_l14v3_aggregated_10cells.json` | 6 | 6 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 42 | `_l14v3_n26_metrics.json` | 6 | 6 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 43 | `_pkf34_probe1.py` | 6 | 5 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_post_cleanup_ | 否 | **乙** |
| 44 | `_pkf34_probe2.py` | 6 | 5 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_post_cleanup_ | 否 | **乙** |
| 45 | `_rp4_probe_all_r.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 46 | `_rp4_probe_r7.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 47 | `_rp4_probe_r78.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 48 | `_rp4_probe_r7b.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 49 | `_rp4_probe_r_axes.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 50 | `_rp_post_probe_2026_10_09.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 51 | `_s4_refreeze179_enumerate_probe2_2026_10_09.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 52 | `_s4_refreeze179_enumerate_probe_2026_10_09_v1_dead.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 53 | `_s4fill_probe1.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 54 | `_s4fill_probe2.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 55 | `_s4fill_probe3.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 56 | `_s4fill_probe5.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 57 | `_s4oq_entryclass_probe_2026_10_09.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 58 | `_s4oq_read_db_probe_2026_10_09.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 59 | `_t15_inspect4_out.txt` | 6 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 60 | `_t15_inspect5_out.txt` | 6 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 61 | `_t15_inspect6_out.txt` | 6 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 62 | `_t15_percell.txt` | 6 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 63 | `_t15_percell_out.txt` | 6 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 64 | `_v16_tail_dump.txt` | 6 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 65 | `_v412_m1_domain_probe.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 66 | `_v412_s3side_probe.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 67 | `_vk_baxis_probe_2026_10_09.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 68 | `_vk_dualread_probe_2026_10_09.py` | 6 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 69 | `_b12_q4_anchor_probe_2026_09_29.py` | 5 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_post_cleanup_ | 否 | **乙** |
| 70 | `_c5_b_prestate_baseline.json` | 5 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 71 | `_cpatomic_keyscan_2026_09_28.json` | 5 | 5 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 72 | `_cpatomic_patch_manifest_2026_09_28.json` | 5 | 5 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 73 | `_cpatomic_pycache_post_2026_09_28.json` | 5 | 5 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 74 | `_cpatomic_verify_2026_09_28.json` | 5 | 5 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 75 | `_d05_probe_align.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 76 | `_d05_probe_arm1.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 77 | `_d05_probe_den.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 78 | `_d05_probe_dist.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 79 | `_d05_probe_ho.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 80 | `_d05_probe_inter.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 81 | `_d05_probe_j1.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 82 | `_d05_probe_keys.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 83 | `_d05_probe_labels.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 84 | `_d05_probe_leak.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 85 | `_d05_probe_metrics.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 86 | `_d05_probe_order.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 87 | `_d05_probe_phrase.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 88 | `_d05_probe_seq.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 89 | `_d05_probe_thresh.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 90 | `_d05_probe_train.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 91 | `_d05_probe_tree.py` | 5 | 4 | _achievements_inventory_full_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_sna | 否 | **乙** |
| 92 | `_probe21_fields.py` | 5 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_post_cleanup_ | 否 | **乙** |
| 93 | `_r4_key_scan_results_2026_09_24.json` | 5 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 94 | `_rj5_mapping_test_2026_09_27.out.txt` | 5 | 4 | _internal_true_clue_book_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_v3_recheck_12_rj5_provena | 否 | **乙** |
| 95 | `_s4_refreeze179_enumerate_probe3_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_substrate_refreeze_ | 否 | **乙** |
| 96 | `_s4_refreeze179_final_probe_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_substrate_refreeze_ | 否 | **乙** |
| 97 | `_s4_refreeze179_grid_probe2_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_substrate_refreeze_ | 否 | **乙** |
| 98 | `_s4_refreeze179_grid_probe_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_substrate_refreeze_ | 否 | **乙** |
| 99 | `_s4f2_manifest_pre.txt` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_s4_face_v2_sync_2026_10_09.md；_v4_closeout_bulk_reorganize_regis | 否 | **乙** |
| 100 | `_s4f2_probe2_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_face_v2_sync_2026_1 | 否 | **乙** |
| 101 | `_s4f2_probe3_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_face_v2_sync_2026_1 | 否 | **乙** |
| 102 | `_s4f2_probe4_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_face_v2_sync_2026_1 | 否 | **乙** |
| 103 | `_s4f2_probe5_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_face_v2_sync_2026_1 | 否 | **乙** |
| 104 | `_s4f2_probe6_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_face_v2_sync_2026_1 | 否 | **乙** |
| 105 | `_s4fs_probe_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_face_sync_2026_10_0 | 否 | **乙** |
| 106 | `_t1_exp2_c_driver_stdout3.log` | 5 | 3 | _numbering_659_overlap_semantic_review_2026_10_14.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout | 否 | **乙** |
| 107 | `_t1_gap_acct_probe_2026_10_01.py` | 5 | 4 | _t1_substrate_gap_census_2026_10_01.md；_repo_post_cleanup_snapshot_2026_10_12.md；_t1_substrate_gap_census_2026 | 否 | **乙** |
| 108 | `_t1_gap_dup_probe_2026_10_01.py` | 5 | 4 | _t1_substrate_gap_census_2026_10_01.md；_repo_post_cleanup_snapshot_2026_10_12.md；_t1_substrate_gap_census_2026 | 否 | **乙** |
| 109 | `_t1_gap_itemkey_probe_2026_10_01.py` | 5 | 4 | _t1_substrate_gap_census_2026_10_01.md；_repo_post_cleanup_snapshot_2026_10_12.md；_t1_substrate_gap_census_2026 | 否 | **乙** |
| 110 | `_t1_gap_struct_probe_2026_10_01.py` | 5 | 4 | _t1_substrate_gap_census_2026_10_01.md；_repo_post_cleanup_snapshot_2026_10_12.md；_t1_substrate_gap_census_2026 | 否 | **乙** |
| 111 | `_t1_temp_axis_design_probe_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_t1_temp_axis_new_exper | 否 | **乙** |
| 112 | `_v16_tail_only.txt` | 5 | 5 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 113 | `_v412_s4_daily_share_prereq_probe_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_s4_daily_share_margin_ | 否 | **乙** |
| 114 | `_verify_dual_probe1_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 115 | `_verify_dual_probe2_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 116 | `_verify_dual_probe3_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 117 | `_verify_dual_probe3b_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 118 | `_verify_dual_probe4_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 119 | `_verify_dual_probe5_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 120 | `_verify_dual_probe6_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 121 | `_verify_dual_probe7_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 122 | `_verify_dual_probe8_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 123 | `_verify_dual_probe9_2026_10_09.py` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 124 | `_vk_baxis_probe_2026_10_09.txt` | 5 | 3 | _numbering_659_overlap_semantic_review_2026_10_14.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout | 否 | **乙** |
| 125 | `_vk_r2_axis_probe_2026_10_09.py` | 5 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_t1_qwen_temp_sweep_r2_ | 否 | **乙** |
| 126 | `card23_readout_utf8.txt` | 5 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md；_v4_closeout_ | 否 | **乙** |
| 127 | `five_terminal_classify_2026_10_10.json` | 5 | 3 | _five_terminal_judgments_ruling_2026_10_10.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 128 | `five_terminal_scan_2026_10_10.json` | 5 | 4 | scan_five_terminal_2026_10_10.py；_five_terminal_judgments_ruling_2026_10_10.md；_repo_full_inventory_catalogue_ | 否 | **乙** |
| 129 | `_card23_readout_utf8.txts` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 130 | `_d05_detail.txt` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 131 | `_diff21_anchor_drift.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 132 | `_e3536.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 133 | `_e50_c1.md` | 4 | 3 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_fake_verdict_rever | 是 | **乙＋丙** |
| 134 | `_ea_r2_axis_probe2_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 135 | `_ea_r2_recompute_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 136 | `_final_sha.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 137 | `_gaps.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 138 | `_gaps2.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 139 | `_kv3s43_frozen_recompute_probe2_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 140 | `_kv3s43_frozen_recompute_probe3_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 141 | `_kv3s43_frozen_recompute_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 142 | `_l14v3_aggregated_10cells_v2.json` | 4 | 4 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 143 | `_l14v3_aggregated_10cells_v3.json` | 4 | 4 | _internal_true_clue_book_2026_10_12.md；_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md；_ | 否 | **乙** |
| 144 | `_pf_d1_full_2026_09_15.py` | 4 | 3 | P_F_D1_FULL_REPORT_2026_09_15.md；_archive_manifest_non_upload_2026_09_23.json；_v3_v4_achievements_inventory_3d | 是 | **乙＋丙** |
| 145 | `_pk_pairing_caliber_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 146 | `_pk_probe7.py` | 4 | 4 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_v4_wide_walkthrough_reply_trae_cod | 否 | **乙** |
| 147 | `_r10.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 148 | `_r11_ctx.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 149 | `_r1_scratch_bom.json` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 150 | `_r1_scratch_corrupt_a.json` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 151 | `_r4_cleanup_worker_keyscan_results_2026_09_29.json` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 152 | `_r6_evidence.txt` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_repo_full_inventor | 否 | **乙** |
| 153 | `_rp4_cand3_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 154 | `_rp4_cand_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 155 | `_rp4_final2_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 156 | `_rp4_final_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 157 | `_rp4_grid_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 158 | `_rp4_reuse_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 159 | `_rp4_slug_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 160 | `_rp4_slug_probe_b_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 161 | `_rp_intake_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 162 | `_rpd_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 163 | `_rpd_probe_b_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 164 | `_rpd_reuse_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 165 | `_rpq_indep_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 166 | `_run_output.log` | 4 | 3 | _internal_true_clue_book_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorgani | 否 | **乙** |
| 167 | `_s4_freeze_bucket_src_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 168 | `_s4_freeze_daystamp_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 169 | `_s4_freeze_enumerate_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 170 | `_s4_freeze_final_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 171 | `_s4_freeze_rowkeys_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 172 | `_s4_freeze_rpair_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 173 | `_s4_intake_recompute_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 174 | `_s4_refreeze179_enumerate_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 175 | `_s4_terminal_decomp_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 176 | `_s4_terminal_grid_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 177 | `_s4_terminal_uv_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 178 | `_s4f2_manifest_post.txt` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 179 | `_s4f2_probe2_out.txt` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 180 | `_s4f2_probe3_out.txt` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 181 | `_s4f2_probe_out.txt` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 182 | `_s4td_existing_qindex.tsv` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 183 | `_s4td_grid_probe_2026_10_09.py` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_repo_post_cleanup_snapshot_2026_10_12.md；_zone_balance_inventory | 否 | **乙** |
| 184 | `_s5dp_run_stdout_2026_10_11.txt` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 185 | `_t1_qwen_temp_sweep_decomposition.txt` | 4 | 4 | _repo_full_inventory_catalogue_2026_10_12.md；_t1_qwen_temp_sweep_exec_register_2026_10_09.md；_t1_qwen_temp_swe | 否 | **乙** |
| 186 | `_t1_qwen_temp_sweep_retry.log` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 187 | `_t1_qwen_temp_sweep_run.log` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 188 | `_t1_temp_axis_design_probe_2026_10_09.json` | 4 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_t1_temp_axis_new_experiment_design_2026_10_09.md；_v4_closeout_bu | 否 | **乙** |
| 189 | `_tail3_atomic_make_2026_09_29.json` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 190 | `_tail3_atomic_refs_2026_09_29.json` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 191 | `_tail3_atomic_verify_2026_09_29.json` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 192 | `_v5_item21_patch.diff` | 4 | 4 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_v4_closeout_moves_ | 否 | **乙** |
| 193 | `e4_axis2_run_out.json` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 194 | `e4_axis2_validation_out.json` | 4 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 195 | `five_terminal_domain_2026_10_10.json` | 4 | 3 | _five_terminal_judgments_ruling_2026_10_10.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 196 | `five_terminal_supplement_2026_10_10.json` | 4 | 3 | _five_terminal_judgments_ruling_2026_10_10.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 197 | `ge01_full_1494_adjudication_2026_10_16.json` | 4 | 2 | _pi_card_answers_register_2026_10_16_v41.md；_u_1494_carrier_effect_register_2026_10_16.md | 否 | **乙** |
| 198 | `_abc_final_2026_10_10.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 199 | `_abc_h1h2_out_2026_10_10.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 200 | `_c5_b3_utf8_out.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 201 | `_cards_35_48_full.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 202 | `_ci_gap_fill_alt_bc_aper_prime_2026_10_09.log` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 203 | `_ci_gap_fill_err.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 204 | `_ci_gap_fill_out.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 205 | `_d05_caliber_out_2026_10_10.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 206 | `_d05_s4only_out_2026_10_10.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 207 | `_d1_full_run.log` | 3 | 2 | P_F_D1_FULL_REPORT_2026_09_15.md；_archive_manifest_non_upload_2026_09_23.json | 是 | **乙＋丙** |
| 208 | `_d4_relabel_run1.log` | 3 | 3 | _internal_true_clue_book_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorgani | 否 | **乙** |
| 209 | `_docwriter_wt2_enum_final_2026_09_30.tsv` | 3 | 3 | _tdf_s1b_2026_10_12.py；_internal_true_clue_book_2026_10_12.md；_walkthrough_bugfix_audit_reply_trae_code_2026_0 | 否 | **乙** |
| 210 | `_e50_c2.md` | 3 | 3 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_fake_verdict_rever | 是 | **乙＋丙** |
| 211 | `_e6_alt_permp_closure_raw_2026_10_10.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 212 | `_e6_ndjt_recompute_out_2026_10_10.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 213 | `_exp03_blade_recompute_out_2026_10_10.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 214 | `_kv3s43_diag_out.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 215 | `_kv3s43_frozen_recompute_readings2_2026_10_09.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 216 | `_kv3s43_frozen_recompute_readings3_2026_10_09.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 217 | `_kv3s43_frozen_recompute_readings_2026_10_09.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 218 | `_payload.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 219 | `_pk_probe6.py` | 3 | 3 | TRAE_V3_ASSET_ERRATUM_2026_09_23.md；_internal_true_clue_book_2026_10_12.md；_v4_wide_walkthrough_reply_trae_cod | 否 | **乙** |
| 220 | `_q3_l282_fix_validate_2026_10_09.txt` | 3 | 3 | _q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_cl | 否 | **乙** |
| 221 | `_r1_scratch_good.json` | 3 | 3 | TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md；_internal_true_clue_book_2026_10_12.md；_v4_closeout_bulk_r | 否 | **乙** |
| 222 | `_r4_key_scan_r1_files_2026_09_27.json` | 3 | 3 | _internal_true_clue_book_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorgani | 否 | **乙** |
| 223 | `_s4_freeze_rpair_readings_2026_10_09.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 224 | `_s4_refreeze179_grid_readings_2026_10_09.txt` | 3 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_s4_substrate_refreeze_register_179_2026_10_09.md；_v4_closeout_bu | 否 | **乙** |
| 225 | `_s4oq_baseline_faces_2026_10_09.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 226 | `_s4oq_stats_2026_10_09.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 227 | `_s4oq_sups_draft_2026_10_09.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 228 | `_s4td_existing_faces.json` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 229 | `_t1_exp2_c_driver_stdout.log` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 230 | `_t1_exp2_c_driver_stdout2.log` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 231 | `_t1_exp2_c_driver_stdout4.log` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 232 | `_t1_exp2_pi_card_ask6455cd9f15bf7dc12ae673d9.json` | 3 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_t1_exp2_activation_supplement_2026_10_09.md；_v4_closeout_bulk_re | 否 | **乙** |
| 233 | `_t1_exp2_run_d.log` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 234 | `_t1_exp2_run_d2.log` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 235 | `_t1_gap_prewrite_snapshot_2026_10_01.json` | 3 | 3 | _t1_substrate_gap_census_2026_10_01.md；_t1_substrate_gap_census_2026_10_01.md；_v4_closeout_bulk_reorganize_reg | 否 | **乙** |
| 236 | `_t1_r2_run_driver.log` | 3 | 3 | _repo_full_inventory_catalogue_2026_10_12.md；_t1_r2_activation_2026_10_09.md；_v4_closeout_bulk_reorganize_regi | 否 | **乙** |
| 237 | `_v3r1_diag.json` | 3 | 3 | _internal_true_clue_book_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorgani | 否 | **乙** |
| 238 | `_v3r1_run1.log` | 3 | 3 | _internal_true_clue_book_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorgani | 否 | **乙** |
| 239 | `_v3r1_run2.log` | 3 | 3 | _internal_true_clue_book_2026_10_12.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorgani | 否 | **乙** |
| 240 | `_verify_15frozen_post.txt` | 3 | 3 | _archive_manifest_non_upload_2026_09_23.json；_v3_v4_achievements_inventory_3dir_2026_09_24.md；_v3_v4_ghostref_ | 是 | **乙＋丙** |
| 241 | `_verify_15frozen_run.txt` | 3 | 3 | _archive_manifest_non_upload_2026_09_23.json；_v3_v4_achievements_inventory_3dir_2026_09_24.md；_v3_v4_ghostref_ | 是 | **乙＋丙** |
| 242 | `_verify_pf_d1_2026_09_15.py` | 3 | 3 | P_F_D1_REPORT_2026_09_15.md；_archive_manifest_non_upload_2026_09_23.json；_v3_v4_achievements_inventory_3dir_20 | 是 | **乙＋丙** |
| 243 | `_vk_dualread_probe_2026_10_09.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 244 | `receipt_disp_idx.txt` | 3 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 245 | `vk_v3df_0_1_verify_out_2026_10_09.json` | 3 | 3 | _exp06_selfverified_renaming_note_2026_10_10.md；_repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk | 否 | **乙** |
| 246 | `_claude_reply_view.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 247 | `_d05_summary.json` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 248 | `_d1_runlog.txt` | 2 | 2 | _archive_manifest_non_upload_2026_09_23.json；_v3_v4_achievements_inventory_3dir_2026_09_24.md | 是 | **乙＋丙** |
| 249 | `_disp.json` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 250 | `_docwriter_wt2_enum_2026_09_30.tsv` | 2 | 2 | _tdf_s1b_2026_10_12.py；TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md | 否 | **乙** |
| 251 | `_enc_test.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 252 | `_iscp_dual_probe_out_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 253 | `_iscp_probe_out_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 254 | `_l14v3_records.json` | 2 | 2 | _v4_supp_prereg_v02_add_L14V3_2026_09_24.md；_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md | 否 | **乙** |
| 255 | `_p0_prereq_verify_2026_10_10.py` | 2 | 1 | _g5_ccp_execution_prereqs_2026_10_10.md | 否 | **乙** |
| 256 | `_q3_l282_fix_build_2026_10_09.py` | 2 | 1 | _q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md | 否 | **乙** |
| 257 | `_q3_l282_fix_validate_2026_10_09.py` | 2 | 1 | _q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md | 否 | **乙** |
| 258 | `_q_cards_2026_10_11.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 259 | `_rpq_nonportrait_full_probe_out3_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 260 | `_rpq_nonportrait_full_probe_out4_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 261 | `_rpq_nonportrait_full_probe_out_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 262 | `_run_output.lo` | 2 | 1 | _numbering_659_overlap_semantic_review_2026_10_14.md | 否 | **乙** |
| 263 | `_s4_intake_recompute_readings_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 264 | `_s4_refreeze179_final_readings_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 265 | `_s4_refreeze179_grid_readings2_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 266 | `_s4_refreeze179_readings_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 267 | `_s4_topup_addendum_verify_2026_10_09.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 268 | `_t1_exp2_c_driver.log` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 269 | `_t1_qwen_temp_sweep_readings_table.txt` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 270 | `_t1_r2_verify_2026_10_09.json` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 271 | `_v5_loadcorpus_switch_2026_09_29/apply_fix.py` | 2 | 1 | _v5_confirm_b5_decisions_register_2026_09_29.md | 否 | **乙** |
| 272 | `_v5_loadcorpus_switch_2026_09_29/verify_2026_09_29.py` | 2 | 1 | _v5_confirm_b5_decisions_register_2026_09_29.md | 否 | **乙** |
| 273 | `_verify_final.py` | 2 | 2 | _archive_manifest_non_upload_2026_09_23.json；_v3_v4_achievements_inventory_3dir_2026_09_24.md | 是 | **乙＋丙** |
| 274 | `anchor_snapshot.json` | 2 | 2 | _repo_full_inventory_catalogue_2026_10_12.md；_v4_closeout_bulk_reorganize_register_2026_10_12.md | 否 | **乙** |
| 275 | `verif_doubt6_v_20260928/_merged_canonical_snapshot_224910.md` | 2 | 1 | _v5_trae_doubt6_verify_2026_09_28_r3verifier.md | 是 | **乙＋丙** |
| 276 | `verif_doubt6_v_20260928/_v5_trae_doubt6_verify_2026_09_28.md` | 2 | 2 | _v5_closing_register_2026_09_28.md；_v5_sub_artifact_ledger_2026_09_28.md | 是 | **乙＋丙** |
| 277 | `verif_doubt6_v_20260928/baseline_mine.json` | 2 | 2 | _v5_confirm_b5_decisions_register_2026_09_29.md；_v5_trae_doubt6_verify_2026_09_28_r3verifier.md | 是 | **乙＋丙** |
| 278 | `_c5_probe_2026_10_01.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 279 | `_check2.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 280 | `_cleanup_worker_analysis_2026_10_15.py` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 281 | `_cleanup_worker_delete_2026_10_15.py` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 282 | `_cleanup_worker_delete_result_2026_10_15.json` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 283 | `_cleanup_worker_gen_inventory_2026_10_15.py` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 284 | `_cleanup_worker_probe_2026_10_15.py` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 285 | `_cleanup_worker_scan_2026_10_15.json` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 286 | `_cleanup_worker_scan_tmp_2026_10_15.json` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 287 | `_cleanup_worker_scan_tmp_2026_10_15.py` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 288 | `_cleanup_worker_verify_2026_10_15.json` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 289 | `_cleanup_worker_verify_2026_10_15.py` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 290 | `_dupids.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 291 | `_errata_sec12_prereg.md` | 1 | 1 | _v5_sub_artifact_ledger_2026_09_28.md | 否 | **乙** |
| 292 | `_errata_sec6_register.md` | 1 | 1 | _v5_sub_artifact_ledger_2026_09_28.md | 否 | **乙** |
| 293 | `_eventids.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 294 | `_explore_addenda.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 295 | `_g1_archive_register_write.py` | 1 | 1 | _g1_archive_zone_search_register_2026_10_12.md | 否 | **乙** |
| 296 | `_g1_closure_register_write.py` | 1 | 1 | _g1_closure_register_2026_10_12.md | 否 | **乙** |
| 297 | `_g2_probe1.py` | 1 | 1 | _g2_residual_cause_register_2026_10_12.md | 否 | **乙** |
| 298 | `_g2_probe1–5.py` | 1 | 1 | _g2_residual_cause_register_2026_10_12.md | 否 | **乙** |
| 299 | `_g2_write.py` | 1 | 1 | _g2_residual_cause_register_2026_10_12.md | 否 | **乙** |
| 300 | `_h_prov_probe.py` | 1 | 1 | _itemH_fingerprint_provenance_2026_10_12.md | 否 | **乙** |
| 301 | `_handoff_summary.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 302 | `_pk_selfscan_v3s.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 303 | `_probe21.py（驱动脚本，非读数；读数件在` | 1 | 1 | _v5_item21_anchor_recompute_2026_09_28.json | 否 | **乙** |
| 304 | `_probe_result.txt` | 1 | 1 | _cleanup_exec_register_2026_10_15.md | 否 | **乙** |
| 305 | `_s4_finalize.py` | 1 | 1 | _g5_ccp_execution_prereqs_2026_10_10.md | 否 | **乙** |
| 306 | `_s4_heldout_items_exec.py` | 1 | 1 | _g5_ccp_execution_prereqs_2026_10_10.md | 否 | **乙** |
| 307 | `_t1_gap_selfscan_2026_10_01.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 308 | `_test_fp.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 309 | `_v2verdict_check.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 310 | `_v5_c5_b_preflight_degradation_guard.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 311 | `_v6_w7_pre_move_state.json` | 1 | 1 | _v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md | 否 | **乙** |
| 312 | `_verify_btier.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 313 | `_verify_pf_d1_full_2026_09_15.py` | 1 | 1 | deposon_pf_d1_full_9m5c_2026_09_15.json | 否 | **乙** |
| 314 | `_verify_v3.py` | 1 | 1 | _v4_day_inventory_2026_09_27.md | 否 | **乙** |
| 315 | `d1fill_finalscan.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 316 | `d1fill_postcheck.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 317 | `d1fill_recount_probe.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 318 | `d1fill_recount_probe2.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 319 | `d1fill_recount_probe3.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 320 | `docwriter_v41_write_v41.py` | 1 | 1 | _pi_card_answers_register_2026_10_16_v41.md | 否 | **乙** |
| 321 | `s3_recompute_full.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 322 | `s3_recompute_pass3.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 323 | `s3_recompute_pass5.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 324 | `s3_recompute_pass6.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 325 | `s3_recompute_probe.py` | 1 | 1 | _v4_closeout_moves_and_cleanup_register_2026_10_12.md | 否 | **乙** |
| 326 | `vk_budget_calc_2026_10_16.py` | 1 | 1 | _interval_420_600_upper_bound_deliberation_2026_10_16.md | 否 | **乙** |

---

## §5 B 层（45 项·正则产物）——非真实缺失件

### §5.1 分类与判据

| 判据类 | 件数 | 何以判为产物（非真实缺失） |
| :-- | --: | :-- |
| `B_EXTENSIONLESS_FRAGMENT`（无扩展名碎片） | 17 | 无扩展名之裸词干／目录片段，正文行文中之简指 |
| `B_TRUNCATED_STEM`（截断词干） | 11 | 名以 `_` 收尾，系文档排版折行处截断之**词干**，非完整文件名 |
| `B_GLOB_WILDCARD`（通配符残留） | 9 | 名中含 `*`，系原文之通配表述，本非具体件名 |
| `B_SYNTAX_ARTIFACT`（语法／编辑残留） | 7 | `.pyc`/`.bak`/`.o`/`.swp` 等编辑器与编译器残留路径 |
| `B_PYCACHE`（`__pycache__` 产物） | 1 | 指向 `__pycache__/` 之 Python 字节码缓存目录 |

### §5.2 B 全量清单（45 行）

| # | 目标名 | 引用处 | 判据类 |
| --: | :-- | --: | :-- |
| 1 | `verif_doubt6_v_20260928/` | 6 | `B_EXTENSIONLESS_FRAGMENT` |
| 2 | `_t15_records/` | 5 | `B_EXTENSIONLESS_FRAGMENT` |
| 3 | `_ea` | 3 | `B_EXTENSIONLESS_FRAGMENT` |
| 4 | `_cpatomic_scratch/` | 2 | `B_EXTENSIONLESS_FRAGMENT` |
| 5 | `_tail3_scratch/` | 2 | `B_EXTENSIONLESS_FRAGMENT` |
| 6 | `_vk_pv02_reche` | 2 | `B_EXTENSIONLESS_FRAGMENT` |
| 7 | `sweep_scan_2026_10_01/` | 2 | `B_EXTENSIONLESS_FRAGMENT` |
| 8 | `verif_doubt6）——删并` | 2 | `B_EXTENSIONLESS_FRAGMENT` |
| 9 | `_t1_records/` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 10 | `_tail3_scratch` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 11 | `_tmp_v3df` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 12 | `_v5_c5_b_fix_readings_2026_10_01.py/` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 13 | `_vk_dualread` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 14 | `doc_writer_v06/` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 15 | `docwriter_v42` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 16 | `ge01_eps_grid_exec` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 17 | `scratch` | 1 | `B_EXTENSIONLESS_FRAGMENT` |
| 18 | `_e48_*.py` | 2 | `B_GLOB_WILDCARD` |
| 19 | `_e49_*.md` | 1 | `B_GLOB_WILDCARD` |
| 20 | `_e50_*.md` | 1 | `B_GLOB_WILDCARD` |
| 21 | `_pk_probe*.py` | 1 | `B_GLOB_WILDCARD` |
| 22 | `_run_*_verify/table` | 1 | `B_GLOB_WILDCARD` |
| 23 | `ge01_eps_grid_exec2_*.json` | 1 | `B_GLOB_WILDCARD` |
| 24 | `m2verdict_*.py` | 1 | `B_GLOB_WILDCARD` |
| 25 | `verify_two*.py` | 1 | `B_GLOB_WILDCARD` |
| 26 | `x*.json` | 1 | `B_GLOB_WILDCARD` |
| 27 | `__pycache__/` | 5 | `B_PYCACHE` |
| 28 | `__pycache__/_s4_heldout_items_exec.cpython-314.pyc` | 4 | `B_SYNTAX_ARTIFACT` |
| 29 | `__pycache__/_abc_readings_reprocheck_2026_10_10.cpython-314.pyc` | 3 | `B_SYNTAX_ARTIFACT` |
| 30 | `__pycache__/_s4_heldout_seed42_probe_2026_10_09.cpython-314.pyc` | 3 | `B_SYNTAX_ARTIFACT` |
| 31 | `__pycache__/_s5dp_five_lines_runner_third_2026_10_11.cpython-314.pyc` | 3 | `B_SYNTAX_ARTIFACT` |
| 32 | `__pycache__//s4_regen_runner.cpython-314.pyc` | 1 | `B_SYNTAX_ARTIFACT` |
| 33 | `_r1_syntax_check.pyc` | 1 | `B_SYNTAX_ARTIFACT` |
| 34 | `_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak` | 1 | `B_SYNTAX_ARTIFACT` |
| 35 | `_l14v3_` | 8 | `B_TRUNCATED_STEM` |
| 36 | `_t15r2_batch_` | 5 | `B_TRUNCATED_STEM` |
| 37 | `docwriter_v44_` | 4 | `B_TRUNCATED_STEM` |
| 38 | `_cpatomic_` | 1 | `B_TRUNCATED_STEM` |
| 39 | `_e48_` | 1 | `B_TRUNCATED_STEM` |
| 40 | `_rj5_` | 1 | `B_TRUNCATED_STEM` |
| 41 | `_s4f2_manifest_` | 1 | `B_TRUNCATED_STEM` |
| 42 | `_t1_exp2_c_` | 1 | `B_TRUNCATED_STEM` |
| 43 | `_tail3_atomic_` | 1 | `B_TRUNCATED_STEM` |
| 44 | `_v16_` | 1 | `B_TRUNCATED_STEM` |
| 45 | `five_terminal_` | 1 | `B_TRUNCATED_STEM` |

### §5.3 检索口径之修正建议（⛔0 回改原件）

B 层**不计入断链**，其成因是**检索口径**而非文件缺失。建议之修正**仅作用于后续扫描脚本之口径**，⛔0 回改任何既有件：

1. **排除通配与词干**：名中含 `*`、或以 `_` 收尾者，于「悬空集」入口即滤除，另入「口径产物集」。
2. **锚先行切分**：凡含 `#`，一律**先于 `#` 切分**再判存废（本棒实测 10 处 `#<片SHA>` 引用之基础名**全部存在**，若不切分将误判 10 处）。
3. **语法残留单列**：`.pyc`/`.pyo`/`.bak`/`.orig`/`.o`/`.swp` 及 `__pycache__/` 路径，不入悬空集。
4. **二进制载体禁入**：`.pyc`/`.pkl`/`.log` 等以宽松解码扫描会产生伪串（本棒实测曾致引用处虚增至 10,419），应**严格 UTF-8 解码、失败即跳过并登记**。
5. **防自污染**：扫描器自身落盘产物须落仓外临时目录，或于扫描时排除自身前缀——本棒实测此一修正即将 `_t15r2_records.json` 之计数由 176 校正为 **44**。

---

## §6 与派工单转述之 630 之逐层对账（诚实交代）

派工单载「无在盘载体·文本报回」，故本棒**⛔0 以转述数字覆盖实测**，改为独立实测后逐层对账如下：

| 层 | 派工单转述 | 本棒实测 | 差 | 对账结论 |
| :-- | --: | --: | --: | :-- |
| A1 | 273 | **273** | **0** | ✅ **精确吻合**——归因面（10-15 执行表 `.tmp/` 274 行）与 A1 目标名**完全重合**，双向可验 |
| A2 | 313 | **326** | **+13** | ⚠️ 未复现；差异集中于 A2 之**边界判定**（见下） |
| B | 44 | **45** | **+1** | ✅ 若不计 `_archive_*` 面之 1 项，则**恰为 44**（实测 `B` = 44） |
| 合计 | 630 | **644** | **+14** | 差异 **+14**，占 2.2% |

**旁证（多项独立指标吻合，佐证本棒口径与转述口径同源）**：

| 指标 | 派工单转述 | 本棒实测 |
| :-- | --: | --: |
| A1 件数 | 273 | **273** ✅ |
| `_t15r2_records.json` 引用处 | 44 处 | **44** ✅ |
| `c5_guard_minmaxstd_2026_10_01.py` 引用处 | 21 处 | **21** ✅ |
| 悬空引用处总数 | 2,068 处 | **2,059 处**（−9，0.4%） |
| B 件数（不计归档面） | 44 | **44** ✅ |

**未能复现之 +13（A2）之可能成因（本棒据实列出，不作推断性断言）**：

1. **A2/B 边界归属差异**：本棒 B 层判据为「名含 `*`／以 `_` 收尾／语法残留／`__pycache__`／无扩展名」。若转述之 B 层判据更宽，则部分本棒计入 A2 者会被计入 B，反向亦然；该边界之具体归属无法由「无在盘载体」之转述复原。
2. **`_archive_*` 已废弃面之纳入与否**：本棒**纳入**（5 目录／32 件）；纳入致 B +1、悬空名 +1。
3. **`.tmp/` 子路径引用之归属**：含子路径者本棒取「最长存在前缀」判定；`results/.tmp/<名>` 形态（该目录已不存在）实测仅 2 名，若转述口径另计「目录级失效」，则计数口径相异。

> **结论**：A1（**273 项·处置面之主体**）与 B（**44**）**已精确复现**，且三项独立高频指标逐一吻合；余 **+13** 集中于 A2 之**边界判定**而非**实体差异**（转述之 2,068 与实测 2,059 之差仅 −9，亦指向同一结论）。**本件以实测为准**，差异逐层列明如上，**候 PI 裁定采何种 A2 口径**。

---

## §7 KD 清单（known defects·已知缺陷与未决项）

| # | KD 项 | 性质 | 实测依据 | 处置 |
| --: | :-- | :-- | :-- | :-- |
| KD-1 | **回收站已空**，甲（回填）通道全断 | 已知缺陷 | `〔本地路径已脱敏〕` 下 `$I`=0、`$R`=0（全 bin 递归亦 0/0）；该目录 `LastWriteTime`=2026-10-17 09:50:37 | 记为不可恢复；A1 处置径由「甲／乙」二径收敛为**乙／无**二径 |
| KD-2 | **执行登记件所载「清理后 `$I` 283 条」与现状不符** | 登记与现状之落差 | 登记件表头载 283；本棒实测 0 | 须 PI 裁：是否就「10-15 清理之可恢复性承诺」另立勘误 |
| KD-3 | A2 件数**未复现**（转述 313 ／ 实测 326） | 口径未定 | 见 §6 | 候 PI 裁 A2 边界口径；本件以实测为准 |
| KD-4 | A2 中 15 项「归档同名实体」**未校 SHA-12** | 未验证之可用性 | 仅证同名，未比对字节 | 迁移前须逐项校 SHA-12；本棒 ⛔0 未校、未迁 |
| KD-5 | `_u5_inventory_tmp.txt` 非 UTF-8，**未扫描** | 扫描覆盖缺口 | 严格 UTF-8 解码失败，依纪律跳过不猜 | 该件之 `.tmp/` 引用面**未知**；候 PI 裁是否授权以宽松解码补扫 |
| KD-6 | 本棒前次扫描产物 2 件落于 `results/` | 自污染隐患 | `_dep_dangling_final.json`、`_dep_dangling_scan_raw.json` 自身含 `.tmp/<名>` 字面量 | 已于最终扫描中排除并改落仓外；**二件待清**（强删已被安全策略拦截，本棒 ⛔0 强删） |

---
## §8 自核节（字节级自报）

### §8.1 输入件（实测正身）

| 件 | SHA-12 | bytes |
| :-- | :-- | --: |
| `results/_cleanup_exec_register_2026_10_15.md` | `D53036B01062` | 36,349 |
| `results/_cleanup_inventory_2026_10_15.md` | `9194110CB3F3` | 124,617 |

### §8.2 本件

| 项 | 值 |
| :-- | :-- |
| **路径** | `results/_dangling_630_remediation_list_2026_10_17.md` |
| **编码** | UTF-8 无 BOM |
| **换行** | 纯 LF（0 个 CR） |
| **署名** | doc-writer |
| **状态** | 候 PI 核准；⛔0 执行任何回填／恢复／删除 |

### §8.3 落盘前闸门（实测）

- `Test-Path(OUT)` = **False**（落盘前）✅
- `results/_dangling_630_remediation_list*` 同名 glob 命中 = **0** ✅

### §8.4 阴性结论三重自审（复述）

| 自审 | 实测 |
| :-- | :-- |
| 一·`os.walk` 遍历错误数 | **0**（须 0） ✅ |
| 二·模式非结构性互斥 | 二进制载体排除前后唯一名集合**相同**（仅由二进制承载者 0 件） ✅ |
| 三·时点新鲜 | 扫描时点 2026-10-17T10:11:17（本棒即时） ✅ |
| 附·独立法交叉验 | A1 全 273 件另以 `os.path.exists` 直探，命中 0；大小写不敏感复探，命中 0 ✅ |

### §8.5 本棒实际动作清单（诚实交代）

- **已落盘**：本件 1 件（新增）。
- **未执行**：恢复 0、回填 0、删除 0、迁移 0、SHA-12 校验 0 次（丙路径之 15 项仅证同名）。
- **未回改**：任何既有件 0 件。
- **未联网**：0 次。
- **遗留**：前次扫描产物 2 件（`_dep_dangling_final.json`、`_dep_dangling_scan_raw.json`）尚在 `results/`，已排除于最终扫描之外，待清（KD-6）。
