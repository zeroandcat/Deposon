# 白名单集之**备份映射件**（**复制** · ⛔ 0 移动 · ⛔ 0 删除 · **原件一字不动**）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_whitelist_backup_mapping_2026_10_17.md` |
| **件性质** | **备份映射件**（可引证据 · ⛔ **0** 代 PI 裁 · ⛔ **0 回改任何既有件一字**） |
| **署名** | **worker**（执行棒 · 棒 `WHITELIST-BACKUP-REGISTER`） |
| **对应白名单登记件** | `results/_whitelist_register_2026_10_17.md`（**同棒另立 · 互不覆盖**） |
| **授权出处** | 同登记件 §1（PI 卡 `ask_b578c32203bc3ef994fbae04` · Q1 Other 栏「有的疑似噪声与垃圾被引用了，需要备份且可视为白名单」·⚠ **转引派工单**） |
| **生效备份面** | **仓内 `.tmp` 面**：`.tmp/whitelist_backup_2026_10_17/`（落盘前 `Test-Path` ＝ **False**）· **699** 件 ／ **38,301,580** B · 双端 SHA-12 **699／699 相符** |
| **⚠ 改道前已写入之归档区副本** | `〔归档件引用·未上传:whitelist_backup_2026_10_17〕\` · **699** 件 ／ **38,301,580** B · **保留原位 · ⛔ 0 删除 · 改道后 0 再触** |
| **本棒实测动作面** | **699** 件复制（仓内面）· 逐件 SHA-12 双端复验 **699／699 相符** · ⛔ 0 不符 **0** 件 · **原件事后复验 ＝ 0 变更** · 另**独立第三次复验 699／699 相符 · 0 缺失** · ⛔ **0** 移动／重命名／删除 · **0** 网络 · ⛔ **0** 宣告①毕 |

> 📌 **本件之射程**：**仅**「白名单集 → 备份面」之**逐件映射 ＋ 双端指纹核验 ＋ 口径与许可状态之落账**；⛔ **0** 授权删除任何件；⛔ **0** 代 PI 裁。

---

## §1 备份之口径（**逐字**）

| 项 | 载 |
| :-- | :-- |
| **动作** | **复制**（`shutil.copy2` · 保留 mtime）—— ⛔ **0 移动** · ⛔ **0 重命名** · ⛔ **0 删除** · ⛔ **0 回收站**（`SHFileOperationW` 0 调用） |
| **原件** | **原件一字不动、仍在原位**（`.tmp` 内）—— 复制后**逐件重读**并复算 SHA-12：`originals_changed` ＝ **0** |
| **命名与分层** | `.tmp/whitelist_backup_2026_10_17/`（**日期分层**）＋ 其内**镜像 `.tmp` 内之相对路径**（**保原名**）—— 实测**候选集内 0 件同名冲突** |
| **时点** | 仓内面复制于 `2026-10-17 12:04:21`（耗时 4.0 s） |
| **复验** | **逐件**双端 SHA-12 相符 **699／699**（**100.00%**）· ⛔ 0 不符 0 件 · 复制前设**漂移闸**（逐件复算之 SHA-12 与登记值不符即跳过·实测漂移 **0**）· 另**独立第三次复验**（重算 699 件双端）**699／699 相符 · 0 缺失** |

---

## §2 归档区写入许可之状态：**射程未及 · 目标面已改道**

### §2-1 许可件之射程（**本棒逐字回读** `results/_archive_zone_write_clause_corrigendum_2026_10_17.md` · `%s` ／ 13,526 B）

> 「**0 推及一般可写**」｜「**0 落为默认权限**」（派工单须**逐单明示**）｜「**0 扩及他目的**｜本许可**仅限**『不上传件归档』此一目的」｜「**0 跨区通配**」｜「**0 修正既往违纪之事实**」（其 §5 限制 1–5）
> 
> 📌 该许可所开者 ＝ 「『不上传件归档』之**入区写入**动作 —— 本件**予以许可**（🔓）」（其 §2 表）

### §2-2 🔴 **射程缺口之揭出与本棒之处置**

| 项 | 载 |
| :-- | :-- |
| **缺口（经 v50 登记件 KD-6 揭出）** | 本棒之备份目的 ＝ 「**被引用的疑似噪声与垃圾**」之备份（PI Q1 Other 之「需要备份」），**非**该许可之字面目的「不上传件归档」⇒ **⛔ 0 视为已获归档区写入许可** |
| **改道（parent 指令）** | 备份目标面 ＝ 由 `〔归档件引用·未上传:whitelist_backup_2026_10_17〕\` 改为 **仓内** `〔目录引用·未上传:whitelist_backup_2026_10_17〕\` ⇒ **⛔ 0 触归档区** |
| **改道前既成事实（如实 · 不软化）** | 改道**前**本棒已依该许可之读法向归档区写入 **699** 件 ／ **38,301,580** B；**改道令到达后本棒即停 · 0 继续写入**；已写入者**保留原位 · ⛔ 0 删除** |
| **改道后之接触** | **0** 次（改道后之复制／复验／登记**全部落于仓内 `.tmp` 面**；本棒⛔ **0** 再读再写该区，其数字**系改道前之实测记录**） |
| **⛔ 本棒 0 裁之面** | ①该许可之射程**是否**可及于白名单备份（**0 自裁**·候 PI 逐单明示）②归档区已写入 699 件之**去留**（**0 代裁**·由 parent 呈 PI）③**0 动**该勘误件 `074A6F256655` 一字（**仅被引用**） |

### §2-3 其余禁面之维持与本棒之履践（逐字照录 `074A6F256655` §4）

| 禁面 | 逐字 | 本棒 |
| :-- | :-- | :-- |
| **0 上传该区任何内容** | 「🔴 **绝对维持**」 | ✅ **0** 次网络请求、**0** 次上传 |
| **0 读该区内容**（一般用途） | 「🔴 **维持**」 | 改道前**仅读本棒自落**之副本以复验；**改道后 0 读** |
| **0 列目录** | 「🔴 **维持**」 | ✅ ⛔ **0** 列该区目录（仅对区根作过 `Test-Path` 存在性判定） |

### §2-4 「随附三要件」之**逐项对照**（**该三要件系为「移动／删除面」所设**）

| 要件（逐字） | 本棒之履践 | 判定 |
| :-- | :-- | :-- |
| **① 先出清单**（件名 · bytes · SHA-12 ·「清单**先于任何移动**落盘」） | 复制**之前**：逐件**复算** SHA-12 ＋ bytes 并与登记值**逐位比对**（漂移即跳过），并实测目标子面 `Test-Path` ＝ `False` | ⚠ **部分时序**（KD-2）：**清单之落盘载体（两登记件）晚于复制动作**；惟「先于任何**移动**」之触发条件为**移动**，而本棒 **0 移动** ⇒ 其后果条款（「0 移」）未被触发 |
| **② 旧→新映射件** | ✅ **本件**：§3 逐件旧→新（**两目标面各一列**）· §4 逐件 SHA-12 | ✅ **满足** |
| **③ 可恢复通道**（入回收站 · ⛔ 0 永久删除 · ⛔ 0 `rm`／`Remove-Item`／`unlink`／`rmtree`） | 本棒为**复制**：⛔ **0 移动**、⛔ **0 删除** ⇒ **无删除面**；其**恢复通道即原件本身**（原件在位且逐件复验不变）⇒ 该要件之**实体约束（0 永久删除）本棒 0 违反** | ✅ **于复制面无涉 / 0 违反** |

📌 **可恢复性之诚实附加**：本备份**不以**「可恢复」为原件删除之**安全网**——沿 `results/_no_backup_ruling_and_report_caliber_effect_2026_10_17.md:166` 之逐字「删除之决定**不得**以『**已备份**』（若将来有）、『**可恢复**』或『**已入回收站**』为其**安全网**」⇒ **本备份不改变删除判据之任何门槛**。

---

## §3 逐件映射（原路径 → 两目标面 · **699** 件）

**列义**：`原件（仓内·仍在原位）` · `① 仓内备份面（改道后之生效面）` · `② 归档区副本（改道前写入·保留原位·候 PI）` · `bytes` · `SHA-12（原件）` · `SHA-12（①）` · `SHA-12（②）` · `三端相符`

| # | 原件（仓内·在位） | ① 仓内备份面（生效） | ② 归档区副本（候 PI） | bytes | SHA-12（原件） | SHA-12（①） | SHA-12（②） | 三端相符 |
| --: | :-- | :-- | :-- | --: | :-- | :-- | :-- | :-: |
| 1 | `.tmp/_26b_verdict_prep_hashcheck_2026_10_01.py` | `.tmp/_26b_verdict_prep_hashcheck_2026_10_01.py` | `whitelist_backup_2026_10_17/_26b_verdict_prep_hashcheck_2026_10_01.py` | 3,842 | `6927c9462f41` | `6927c9462f41` | `6927c9462f41` | ✅ |
| 2 | `.tmp/_26b_verdict_prep_literalcheck_2026_10_01.py` | `.tmp/_26b_verdict_prep_literalcheck_2026_10_01.py` | `whitelist_backup_2026_10_17/_26b_verdict_prep_literalcheck_2026_10_01.py` | 4,378 | `50fe799b0a2e` | `50fe799b0a2e` | `50fe799b0a2e` | ✅ |
| 3 | `.tmp/_26b_verdict_prep_validate_2026_10_01.py` | `.tmp/_26b_verdict_prep_validate_2026_10_01.py` | `whitelist_backup_2026_10_17/_26b_verdict_prep_validate_2026_10_01.py` | 4,640 | `494cca45b873` | `494cca45b873` | `494cca45b873` | ✅ |
| 4 | `.tmp/_659_compact.txt` | `.tmp/_659_compact.txt` | `whitelist_backup_2026_10_17/_659_compact.txt` | 155,628 | `795862c09a40` | `795862c09a40` | `795862c09a40` | ✅ |
| 5 | `.tmp/_659_overlap_digest.txt` | `.tmp/_659_overlap_digest.txt` | `whitelist_backup_2026_10_17/_659_overlap_digest.txt` | 239,157 | `4f20b8085fb9` | `4f20b8085fb9` | `4f20b8085fb9` | ✅ |
| 6 | `.tmp/_659_report_gen.py` | `.tmp/_659_report_gen.py` | `whitelist_backup_2026_10_17/_659_report_gen.py` | 27,457 | `cd4b8ed56b2c` | `cd4b8ed56b2c` | `cd4b8ed56b2c` | ✅ |
| 7 | `.tmp/_abc_diff_2026_10_10.py` | `.tmp/_abc_diff_2026_10_10.py` | `whitelist_backup_2026_10_17/_abc_diff_2026_10_10.py` | 6,620 | `6d6733f0e5c2` | `6d6733f0e5c2` | `6d6733f0e5c2` | ✅ |
| 8 | `.tmp/_abc_final_2026_10_10.py` | `.tmp/_abc_final_2026_10_10.py` | `whitelist_backup_2026_10_17/_abc_final_2026_10_10.py` | 7,329 | `15b4de4fdff6` | `15b4de4fdff6` | `15b4de4fdff6` | ✅ |
| 9 | `.tmp/_abc_h1h2_2026_10_10.py` | `.tmp/_abc_h1h2_2026_10_10.py` | `whitelist_backup_2026_10_17/_abc_h1h2_2026_10_10.py` | 7,889 | `16f19bad301f` | `16f19bad301f` | `16f19bad301f` | ✅ |
| 10 | `.tmp/_abc_readings_reprocheck_2026_10_10.py` | `.tmp/_abc_readings_reprocheck_2026_10_10.py` | `whitelist_backup_2026_10_17/_abc_readings_reprocheck_2026_10_10.py` | 9,491 | `0ec2a2bf3bab` | `0ec2a2bf3bab` | `0ec2a2bf3bab` | ✅ |
| 11 | `.tmp/_abc_readings_reprocheck_out_2026_10_10.json` | `.tmp/_abc_readings_reprocheck_out_2026_10_10.json` | `whitelist_backup_2026_10_17/_abc_readings_reprocheck_out_2026_10_10.json` | 78,436 | `2f9aa16b63ca` | `2f9aa16b63ca` | `2f9aa16b63ca` | ✅ |
| 12 | `.tmp/_abc_rfd_2026_10_10.py` | `.tmp/_abc_rfd_2026_10_10.py` | `whitelist_backup_2026_10_17/_abc_rfd_2026_10_10.py` | 5,938 | `39268ca6adff` | `39268ca6adff` | `39268ca6adff` | ✅ |
| 13 | `.tmp/_aggregate_10cells.py` | `.tmp/_aggregate_10cells.py` | `whitelist_backup_2026_10_17/_aggregate_10cells.py` | 3,009 | `3bdc6250d0f2` | `3bdc6250d0f2` | `3bdc6250d0f2` | ✅ |
| 14 | `.tmp/_aggregate_10cells_v2.py` | `.tmp/_aggregate_10cells_v2.py` | `whitelist_backup_2026_10_17/_aggregate_10cells_v2.py` | 5,131 | `af1b7f09f74d` | `af1b7f09f74d` | `af1b7f09f74d` | ✅ |
| 15 | `.tmp/_aggregate_10cells_v3.py` | `.tmp/_aggregate_10cells_v3.py` | `whitelist_backup_2026_10_17/_aggregate_10cells_v3.py` | 2,969 | `04b127d80bf0` | `04b127d80bf0` | `04b127d80bf0` | ✅ |
| 16 | `.tmp/_aggregate_10cells_v4.py` | `.tmp/_aggregate_10cells_v4.py` | `whitelist_backup_2026_10_17/_aggregate_10cells_v4.py` | 2,454 | `f99a3765c3c3` | `f99a3765c3c3` | `f99a3765c3c3` | ✅ |
| 17 | `.tmp/_append_intake_supplement_6_tail.py` | `.tmp/_append_intake_supplement_6_tail.py` | `whitelist_backup_2026_10_17/_append_intake_supplement_6_tail.py` | 9,335 | `c3339682d68c` | `c3339682d68c` | `c3339682d68c` | ✅ |
| 18 | `.tmp/_audit3b.txt` | `.tmp/_audit3b.txt` | `whitelist_backup_2026_10_17/_audit3b.txt` | 50,554 | `e64565a2b180` | `e64565a2b180` | `e64565a2b180` | ✅ |
| 19 | `.tmp/_audit_part3_out.txt` | `.tmp/_audit_part3_out.txt` | `whitelist_backup_2026_10_17/_audit_part3_out.txt` | 5,195 | `85a9d9861d38` | `85a9d9861d38` | `85a9d9861d38` | ✅ |
| 20 | `.tmp/_audit_part4.txt` | `.tmp/_audit_part4.txt` | `whitelist_backup_2026_10_17/_audit_part4.txt` | 14,826 | `def27c1c3511` | `def27c1c3511` | `def27c1c3511` | ✅ |
| 21 | `.tmp/_b12_q1_refs_2026_09_29.py` | `.tmp/_b12_q1_refs_2026_09_29.py` | `whitelist_backup_2026_10_17/_b12_q1_refs_2026_09_29.py` | 4,890 | `86b2d9b7b7bd` | `86b2d9b7b7bd` | `86b2d9b7b7bd` | ✅ |
| 22 | `.tmp/_b12_q1_timeslice_2026_09_29.py` | `.tmp/_b12_q1_timeslice_2026_09_29.py` | `whitelist_backup_2026_10_17/_b12_q1_timeslice_2026_09_29.py` | 798 | `bacf6379b9bf` | `bacf6379b9bf` | `bacf6379b9bf` | ✅ |
| 23 | `.tmp/_b12_q4_adjacent_2026_09_29.py` | `.tmp/_b12_q4_adjacent_2026_09_29.py` | `whitelist_backup_2026_10_17/_b12_q4_adjacent_2026_09_29.py` | 5,709 | `61cbc9965896` | `61cbc9965896` | `61cbc9965896` | ✅ |
| 24 | `.tmp/_b12_q4_exact_2026_09_29.py` | `.tmp/_b12_q4_exact_2026_09_29.py` | `whitelist_backup_2026_10_17/_b12_q4_exact_2026_09_29.py` | 7,140 | `79eba6136d83` | `79eba6136d83` | `79eba6136d83` | ✅ |
| 25 | `.tmp/_b12_q4_formcand_2026_09_29.py` | `.tmp/_b12_q4_formcand_2026_09_29.py` | `whitelist_backup_2026_10_17/_b12_q4_formcand_2026_09_29.py` | 6,510 | `f58f388996d4` | `f58f388996d4` | `f58f388996d4` | ✅ |
| 26 | `.tmp/_b12_tables_2026_09_29.py` | `.tmp/_b12_tables_2026_09_29.py` | `whitelist_backup_2026_10_17/_b12_tables_2026_09_29.py` | 1,907 | `10db58be72cf` | `10db58be72cf` | `10db58be72cf` | ✅ |
| 27 | `.tmp/_build_5anchor_json_draft.py` | `.tmp/_build_5anchor_json_draft.py` | `whitelist_backup_2026_10_17/_build_5anchor_json_draft.py` | 34,455 | `391e7a1be0e5` | `391e7a1be0e5` | `391e7a1be0e5` | ✅ |
| 28 | `.tmp/_build_5anchor_json_v1.py` | `.tmp/_build_5anchor_json_v1.py` | `whitelist_backup_2026_10_17/_build_5anchor_json_v1.py` | 11,627 | `56c459492ecf` | `56c459492ecf` | `56c459492ecf` | ✅ |
| 29 | `.tmp/_build_intake_supplement_6.py` | `.tmp/_build_intake_supplement_6.py` | `whitelist_backup_2026_10_17/_build_intake_supplement_6.py` | 13,094 | `6336456853ae` | `6336456853ae` | `6336456853ae` | ✅ |
| 30 | `.tmp/_build_receipt_supplement_6.py` | `.tmp/_build_receipt_supplement_6.py` | `whitelist_backup_2026_10_17/_build_receipt_supplement_6.py` | 11,430 | `20c44c665b4f` | `20c44c665b4f` | `20c44c665b4f` | ✅ |
| 31 | `.tmp/_c5_b3_rewalk_postcheck_2026_10_01.py` | `.tmp/_c5_b3_rewalk_postcheck_2026_10_01.py` | `whitelist_backup_2026_10_17/_c5_b3_rewalk_postcheck_2026_10_01.py` | 2,249 | `aca7dad6ddfa` | `aca7dad6ddfa` | `aca7dad6ddfa` | ✅ |
| 32 | `.tmp/_c5_b3_rewalk_precheck_2026_10_01.py` | `.tmp/_c5_b3_rewalk_precheck_2026_10_01.py` | `whitelist_backup_2026_10_17/_c5_b3_rewalk_precheck_2026_10_01.py` | 2,035 | `4aad531a2ddb` | `4aad531a2ddb` | `4aad531a2ddb` | ✅ |
| 33 | `.tmp/_c5_b3_rewalk_utf8check_2026_10_01.py` | `.tmp/_c5_b3_rewalk_utf8check_2026_10_01.py` | `whitelist_backup_2026_10_17/_c5_b3_rewalk_utf8check_2026_10_01.py` | 925 | `5488ff2db11f` | `5488ff2db11f` | `5488ff2db11f` | ✅ |
| 34 | `.tmp/_c5_b_group_fix_readings_2026_10_09.py` | `.tmp/_c5_b_group_fix_readings_2026_10_09.py` | `whitelist_backup_2026_10_17/_c5_b_group_fix_readings_2026_10_09.py` | 12,289 | `b6855b38acc2` | `b6855b38acc2` | `b6855b38acc2` | ✅ |
| 35 | `.tmp/_c5_feasibility_probe.py` | `.tmp/_c5_feasibility_probe.py` | `whitelist_backup_2026_10_17/_c5_feasibility_probe.py` | 1,036 | `d730612b0c9a` | `d730612b0c9a` | `d730612b0c9a` | ✅ |
| 36 | `.tmp/_canonical_census.py` | `.tmp/_canonical_census.py` | `whitelist_backup_2026_10_17/_canonical_census.py` | 4,382 | `36b7af564c56` | `36b7af564c56` | `36b7af564c56` | ✅ |
| 37 | `.tmp/_canonical_lines.json` | `.tmp/_canonical_lines.json` | `whitelist_backup_2026_10_17/_canonical_lines.json` | 15,033 | `9b0997fc7e52` | `9b0997fc7e52` | `9b0997fc7e52` | ✅ |
| 38 | `.tmp/_canonical_lines.py` | `.tmp/_canonical_lines.py` | `whitelist_backup_2026_10_17/_canonical_lines.py` | 3,354 | `08aa8638a0b2` | `08aa8638a0b2` | `08aa8638a0b2` | ✅ |
| 39 | `.tmp/_check_escape.py` | `.tmp/_check_escape.py` | `whitelist_backup_2026_10_17/_check_escape.py` | 332 | `5f026b0baf39` | `5f026b0baf39` | `5f026b0baf39` | ✅ |
| 40 | `.tmp/_check_kimi_sides.py` | `.tmp/_check_kimi_sides.py` | `whitelist_backup_2026_10_17/_check_kimi_sides.py` | 1,459 | `4f3291959a6d` | `4f3291959a6d` | `4f3291959a6d` | ✅ |
| 41 | `.tmp/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | `.tmp/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | `whitelist_backup_2026_10_17/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | 20,997 | `b0cf9baba64b` | `b0cf9baba64b` | `b0cf9baba64b` | ✅ |
| 42 | `.tmp/_cleanup_r2_cleanlist.json` | `.tmp/_cleanup_r2_cleanlist.json` | `whitelist_backup_2026_10_17/_cleanup_r2_cleanlist.json` | 810 | `ce71dda28157` | `ce71dda28157` | `ce71dda28157` | ✅ |
| 43 | `.tmp/_cleanup_r2_exec.py` | `.tmp/_cleanup_r2_exec.py` | `whitelist_backup_2026_10_17/_cleanup_r2_exec.py` | 7,884 | `a2029c340ac5` | `a2029c340ac5` | `a2029c340ac5` | ✅ |
| 44 | `.tmp/_cleanup_r2_exec_journal.json` | `.tmp/_cleanup_r2_exec_journal.json` | `whitelist_backup_2026_10_17/_cleanup_r2_exec_journal.json` | 10,327 | `cd636cb64813` | `cd636cb64813` | `cd636cb64813` | ✅ |
| 45 | `.tmp/_cleanup_r2_postcheck.json` | `.tmp/_cleanup_r2_postcheck.json` | `whitelist_backup_2026_10_17/_cleanup_r2_postcheck.json` | 6,652 | `720b25650bcd` | `720b25650bcd` | `720b25650bcd` | ✅ |
| 46 | `.tmp/_cleanup_r2_postcheck.py` | `.tmp/_cleanup_r2_postcheck.py` | `whitelist_backup_2026_10_17/_cleanup_r2_postcheck.py` | 4,585 | `cfd60493f18d` | `cfd60493f18d` | `cfd60493f18d` | ✅ |
| 47 | `.tmp/_cleanup_r2_scan.py` | `.tmp/_cleanup_r2_scan.py` | `whitelist_backup_2026_10_17/_cleanup_r2_scan.py` | 11,507 | `60d6d3d37076` | `60d6d3d37076` | `60d6d3d37076` | ✅ |
| 48 | `.tmp/_cleanup_r2_scan2.py` | `.tmp/_cleanup_r2_scan2.py` | `whitelist_backup_2026_10_17/_cleanup_r2_scan2.py` | 12,112 | `7019c7b8d728` | `7019c7b8d728` | `7019c7b8d728` | ✅ |
| 49 | `.tmp/_cleanup_r2_scan3.py` | `.tmp/_cleanup_r2_scan3.py` | `whitelist_backup_2026_10_17/_cleanup_r2_scan3.py` | 12,389 | `46b7b8230e86` | `46b7b8230e86` | `46b7b8230e86` | ✅ |
| 50 | `.tmp/_cleanup_r2_scan_out.json` | `.tmp/_cleanup_r2_scan_out.json` | `whitelist_backup_2026_10_17/_cleanup_r2_scan_out.json` | 758,995 | `3b107c078490` | `3b107c078490` | `3b107c078490` | ✅ |
| 51 | `.tmp/_compute_metrics.py` | `.tmp/_compute_metrics.py` | `whitelist_backup_2026_10_17/_compute_metrics.py` | 7,752 | `ae2b0142b09e` | `ae2b0142b09e` | `ae2b0142b09e` | ✅ |
| 52 | `.tmp/_compute_metrics_v2.py` | `.tmp/_compute_metrics_v2.py` | `whitelist_backup_2026_10_17/_compute_metrics_v2.py` | 8,017 | `0620ef317e8a` | `0620ef317e8a` | `0620ef317e8a` | ✅ |
| 53 | `.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | `.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | `whitelist_backup_2026_10_17/_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | 31,745 | `3a240806c2d3` | `3a240806c2d3` | `3a240806c2d3` | ✅ |
| 54 | `.tmp/_cpatomic_dump_pyc_2026_09_28.py` | `.tmp/_cpatomic_dump_pyc_2026_09_28.py` | `whitelist_backup_2026_10_17/_cpatomic_dump_pyc_2026_09_28.py` | 468 | `d7c9ac28b096` | `d7c9ac28b096` | `d7c9ac28b096` | ✅ |
| 55 | `.tmp/_cpatomic_keyscan_2026_09_28.py` | `.tmp/_cpatomic_keyscan_2026_09_28.py` | `whitelist_backup_2026_10_17/_cpatomic_keyscan_2026_09_28.py` | 3,074 | `393a8d3fa68f` | `393a8d3fa68f` | `393a8d3fa68f` | ✅ |
| 56 | `.tmp/_cpatomic_make_fix_2026_09_28.py` | `.tmp/_cpatomic_make_fix_2026_09_28.py` | `whitelist_backup_2026_10_17/_cpatomic_make_fix_2026_09_28.py` | 7,796 | `76c822b640a0` | `76c822b640a0` | `76c822b640a0` | ✅ |
| 57 | `.tmp/_cpatomic_pycache_post_2026_09_28.py` | `.tmp/_cpatomic_pycache_post_2026_09_28.py` | `whitelist_backup_2026_10_17/_cpatomic_pycache_post_2026_09_28.py` | 5,164 | `171b2a31c0e1` | `171b2a31c0e1` | `171b2a31c0e1` | ✅ |
| 58 | `.tmp/_cpatomic_pycache_pre_2026_09_28.py` | `.tmp/_cpatomic_pycache_pre_2026_09_28.py` | `whitelist_backup_2026_10_17/_cpatomic_pycache_pre_2026_09_28.py` | 3,912 | `b86619676bf4` | `b86619676bf4` | `b86619676bf4` | ✅ |
| 59 | `.tmp/_cpatomic_register_2026_09_28.json` | `.tmp/_cpatomic_register_2026_09_28.json` | `whitelist_backup_2026_10_17/_cpatomic_register_2026_09_28.json` | 29,361 | `b68d7ff817bb` | `b68d7ff817bb` | `b68d7ff817bb` | ✅ |
| 60 | `.tmp/_cpatomic_register_2026_09_28.py` | `.tmp/_cpatomic_register_2026_09_28.py` | `whitelist_backup_2026_10_17/_cpatomic_register_2026_09_28.py` | 6,322 | `98fe9fa24e80` | `98fe9fa24e80` | `98fe9fa24e80` | ✅ |
| 61 | `.tmp/_cpatomic_verify_2026_09_28.py` | `.tmp/_cpatomic_verify_2026_09_28.py` | `whitelist_backup_2026_10_17/_cpatomic_verify_2026_09_28.py` | 11,036 | `85139011457c` | `85139011457c` | `85139011457c` | ✅ |
| 62 | `.tmp/_crosscheck_messages_35_48.py` | `.tmp/_crosscheck_messages_35_48.py` | `whitelist_backup_2026_10_17/_crosscheck_messages_35_48.py` | 1,608 | `dcfe48359488` | `dcfe48359488` | `dcfe48359488` | ✅ |
| 63 | `.tmp/_d05_b_coincidence_checks_2026_10_10.py` | `.tmp/_d05_b_coincidence_checks_2026_10_10.py` | `whitelist_backup_2026_10_17/_d05_b_coincidence_checks_2026_10_10.py` | 22,078 | `c1fc428d450c` | `c1fc428d450c` | `c1fc428d450c` | ✅ |
| 64 | `.tmp/_d05_caliber_2026_10_10.py` | `.tmp/_d05_caliber_2026_10_10.py` | `whitelist_backup_2026_10_17/_d05_caliber_2026_10_10.py` | 8,011 | `65cb84529cb2` | `65cb84529cb2` | `65cb84529cb2` | ✅ |
| 65 | `.tmp/_d05_instrument_audit.py` | `.tmp/_d05_instrument_audit.py` | `whitelist_backup_2026_10_17/_d05_instrument_audit.py` | 5,948 | `edfa99486954` | `edfa99486954` | `edfa99486954` | ✅ |
| 66 | `.tmp/_d05_s4only_2026_10_10.py` | `.tmp/_d05_s4only_2026_10_10.py` | `whitelist_backup_2026_10_17/_d05_s4only_2026_10_10.py` | 3,438 | `802069e2c06e` | `802069e2c06e` | `802069e2c06e` | ✅ |
| 67 | `.tmp/_d05_three_checks_recheck_2026_10_10.py` | `.tmp/_d05_three_checks_recheck_2026_10_10.py` | `whitelist_backup_2026_10_17/_d05_three_checks_recheck_2026_10_10.py` | 11,134 | `fc1201cb71e7` | `fc1201cb71e7` | `fc1201cb71e7` | ✅ |
| 68 | `.tmp/_d05_three_checks_recheck_out_2026_10_10.json` | `.tmp/_d05_three_checks_recheck_out_2026_10_10.json` | `whitelist_backup_2026_10_17/_d05_three_checks_recheck_out_2026_10_10.json` | 3,622 | `4eb425260682` | `4eb425260682` | `4eb425260682` | ✅ |
| 69 | `.tmp/_dfam_corr_src_2026_10_12.md` | `.tmp/_dfam_corr_src_2026_10_12.md` | `whitelist_backup_2026_10_17/_dfam_corr_src_2026_10_12.md` | 33,471 | `12da29eb102c` | `12da29eb102c` | `12da29eb102c` | ✅ |
| 70 | `.tmp/_diff21_anchor_drift.py` | `.tmp/_diff21_anchor_drift.py` | `whitelist_backup_2026_10_17/_diff21_anchor_drift.py` | 960 | `de2a99cf1999` | `de2a99cf1999` | `de2a99cf1999` | ✅ |
| 71 | `.tmp/_docwriter_night_headers.txt` | `.tmp/_docwriter_night_headers.txt` | `whitelist_backup_2026_10_17/_docwriter_night_headers.txt` | 52,370 | `729875e7999e` | `729875e7999e` | `729875e7999e` | ✅ |
| 72 | `.tmp/_docwriter_night_measure.json` | `.tmp/_docwriter_night_measure.json` | `whitelist_backup_2026_10_17/_docwriter_night_measure.json` | 22,679 | `f5bacfac3f1c` | `f5bacfac3f1c` | `f5bacfac3f1c` | ✅ |
| 73 | `.tmp/_docwriter_q4_l117_append_block.md` | `.tmp/_docwriter_q4_l117_append_block.md` | `whitelist_backup_2026_10_17/_docwriter_q4_l117_append_block.md` | 4,857 | `7c7d633047e4` | `7c7d633047e4` | `7c7d633047e4` | ✅ |
| 74 | `.tmp/_docwriter_recheck.py` | `.tmp/_docwriter_recheck.py` | `whitelist_backup_2026_10_17/_docwriter_recheck.py` | 2,374 | `54b522e4e2fe` | `54b522e4e2fe` | `54b522e4e2fe` | ✅ |
| 75 | `.tmp/_docwriter_write_handover.py` | `.tmp/_docwriter_write_handover.py` | `whitelist_backup_2026_10_17/_docwriter_write_handover.py` | 49,400 | `a553d705a482` | `a553d705a482` | `a553d705a482` | ✅ |
| 76 | `.tmp/_dump_dkb3_records2_2026_10_10.py` | `.tmp/_dump_dkb3_records2_2026_10_10.py` | `whitelist_backup_2026_10_17/_dump_dkb3_records2_2026_10_10.py` | 1,366 | `e71d1e81da64` | `e71d1e81da64` | `e71d1e81da64` | ✅ |
| 77 | `.tmp/_dump_dkb3_records_2026_10_10.py` | `.tmp/_dump_dkb3_records_2026_10_10.py` | `whitelist_backup_2026_10_17/_dump_dkb3_records_2026_10_10.py` | 1,781 | `144b204237bf` | `144b204237bf` | `144b204237bf` | ✅ |
| 78 | `.tmp/_dup_name_diff_content_scan2_2026_10_08.py` | `.tmp/_dup_name_diff_content_scan2_2026_10_08.py` | `whitelist_backup_2026_10_17/_dup_name_diff_content_scan2_2026_10_08.py` | 7,547 | `b3fe206ef866` | `b3fe206ef866` | `b3fe206ef866` | ✅ |
| 79 | `.tmp/_dup_name_diff_content_scan_2026_10_08.py` | `.tmp/_dup_name_diff_content_scan_2026_10_08.py` | `whitelist_backup_2026_10_17/_dup_name_diff_content_scan_2026_10_08.py` | 4,519 | `675cc3136e70` | `675cc3136e70` | `675cc3136e70` | ✅ |
| 80 | `.tmp/_dw_abs_scan.json` | `.tmp/_dw_abs_scan.json` | `whitelist_backup_2026_10_17/_dw_abs_scan.json` | 56,306 | `5c584826ed16` | `5c584826ed16` | `5c584826ed16` | ✅ |
| 81 | `.tmp/_e47_docwriter_count.py` | `.tmp/_e47_docwriter_count.py` | `whitelist_backup_2026_10_17/_e47_docwriter_count.py` | 1,124 | `33cc563b9471` | `33cc563b9471` | `33cc563b9471` | ✅ |
| 82 | `.tmp/_e48_apply.py` | `.tmp/_e48_apply.py` | `whitelist_backup_2026_10_17/_e48_apply.py` | 2,329 | `d4e6f0934e5f` | `d4e6f0934e5f` | `d4e6f0934e5f` | ✅ |
| 83 | `.tmp/_e48_c1.md` | `.tmp/_e48_c1.md` | `whitelist_backup_2026_10_17/_e48_c1.md` | 5,039 | `c2a814a90330` | `c2a814a90330` | `c2a814a90330` | ✅ |
| 84 | `.tmp/_e48_c2.md` | `.tmp/_e48_c2.md` | `whitelist_backup_2026_10_17/_e48_c2.md` | 5,966 | `4d3cae4cbcc0` | `4d3cae4cbcc0` | `4d3cae4cbcc0` | ✅ |
| 85 | `.tmp/_e48_c3.md` | `.tmp/_e48_c3.md` | `whitelist_backup_2026_10_17/_e48_c3.md` | 6,563 | `769c71475404` | `769c71475404` | `769c71475404` | ✅ |
| 86 | `.tmp/_e48_c4.md` | `.tmp/_e48_c4.md` | `whitelist_backup_2026_10_17/_e48_c4.md` | 21,710 | `8143d01ca0e1` | `8143d01ca0e1` | `8143d01ca0e1` | ✅ |
| 87 | `.tmp/_e48_c5.md` | `.tmp/_e48_c5.md` | `whitelist_backup_2026_10_17/_e48_c5.md` | 1,686 | `2f7ab971f691` | `2f7ab971f691` | `2f7ab971f691` | ✅ |
| 88 | `.tmp/_e48_docwriter_chain.py` | `.tmp/_e48_docwriter_chain.py` | `whitelist_backup_2026_10_17/_e48_docwriter_chain.py` | 2,550 | `da5e16e02b7d` | `da5e16e02b7d` | `da5e16e02b7d` | ✅ |
| 89 | `.tmp/_e48_docwriter_enum.py` | `.tmp/_e48_docwriter_enum.py` | `whitelist_backup_2026_10_17/_e48_docwriter_enum.py` | 1,248 | `80bad142f13d` | `80bad142f13d` | `80bad142f13d` | ✅ |
| 90 | `.tmp/_e48_docwriter_hash.py` | `.tmp/_e48_docwriter_hash.py` | `whitelist_backup_2026_10_17/_e48_docwriter_hash.py` | 2,578 | `4656b3b734c5` | `4656b3b734c5` | `4656b3b734c5` | ✅ |
| 91 | `.tmp/_e48_docwriter_hash2.py` | `.tmp/_e48_docwriter_hash2.py` | `whitelist_backup_2026_10_17/_e48_docwriter_hash2.py` | 1,229 | `9a3c5b05e29e` | `9a3c5b05e29e` | `9a3c5b05e29e` | ✅ |
| 92 | `.tmp/_e48_probe_register.py` | `.tmp/_e48_probe_register.py` | `whitelist_backup_2026_10_17/_e48_probe_register.py` | 873 | `d92f74712dab` | `d92f74712dab` | `d92f74712dab` | ✅ |
| 93 | `.tmp/_e49_c1.md` | `.tmp/_e49_c1.md` | `whitelist_backup_2026_10_17/_e49_c1.md` | 13,607 | `1e6e30d4ce4d` | `1e6e30d4ce4d` | `1e6e30d4ce4d` | ✅ |
| 94 | `.tmp/_e49_c2.md` | `.tmp/_e49_c2.md` | `whitelist_backup_2026_10_17/_e49_c2.md` | 17,872 | `11beaed14ea7` | `11beaed14ea7` | `11beaed14ea7` | ✅ |
| 95 | `.tmp/_e6_alt_permp_closure_analysis_2026_10_10.py` | `.tmp/_e6_alt_permp_closure_analysis_2026_10_10.py` | `whitelist_backup_2026_10_17/_e6_alt_permp_closure_analysis_2026_10_10.py` | 2,736 | `affabef74de4` | `affabef74de4` | `affabef74de4` | ✅ |
| 96 | `.tmp/_e6_alt_permp_closure_runner_2026_10_10.py` | `.tmp/_e6_alt_permp_closure_runner_2026_10_10.py` | `whitelist_backup_2026_10_17/_e6_alt_permp_closure_runner_2026_10_10.py` | 9,985 | `9bb254aa58a9` | `9bb254aa58a9` | `9bb254aa58a9` | ✅ |
| 97 | `.tmp/_e6_ndjt_recompute_2026_10_10.py` | `.tmp/_e6_ndjt_recompute_2026_10_10.py` | `whitelist_backup_2026_10_17/_e6_ndjt_recompute_2026_10_10.py` | 5,064 | `59c2d618305f` | `59c2d618305f` | `59c2d618305f` | ✅ |
| 98 | `.tmp/_e_q_doc.md` | `.tmp/_e_q_doc.md` | `whitelist_backup_2026_10_17/_e_q_doc.md` | 28,259 | `71f5a0769dab` | `71f5a0769dab` | `71f5a0769dab` | ✅ |
| 99 | `.tmp/_e_q_exec.json` | `.tmp/_e_q_exec.json` | `whitelist_backup_2026_10_17/_e_q_exec.json` | 6,161 | `d4bd8c92201f` | `d4bd8c92201f` | `d4bd8c92201f` | ✅ |
| 100 | `.tmp/_e_q_exec.txt` | `.tmp/_e_q_exec.txt` | `whitelist_backup_2026_10_17/_e_q_exec.txt` | 0 | `e3b0c44298fc` | `e3b0c44298fc` | `e3b0c44298fc` | ✅ |
| 101 | `.tmp/_ea_179_domain_retest_2026_10_09.py` | `.tmp/_ea_179_domain_retest_2026_10_09.py` | `whitelist_backup_2026_10_17/_ea_179_domain_retest_2026_10_09.py` | 2,814 | `9309e4977b22` | `9309e4977b22` | `9309e4977b22` | ✅ |
| 102 | `.tmp/_ecr_pa_a0_recompute_2026_10_15.py` | `.tmp/_ecr_pa_a0_recompute_2026_10_15.py` | `whitelist_backup_2026_10_17/_ecr_pa_a0_recompute_2026_10_15.py` | 8,804 | `92e204d66c84` | `92e204d66c84` | `92e204d66c84` | ✅ |
| 103 | `.tmp/_ecr_pa_register_src_2026_10_15.md` | `.tmp/_ecr_pa_register_src_2026_10_15.md` | `whitelist_backup_2026_10_17/_ecr_pa_register_src_2026_10_15.md` | 15,707 | `2c7c202aafec` | `2c7c202aafec` | `2c7c202aafec` | ✅ |
| 104 | `.tmp/_en_final_2026_09_28.py` | `.tmp/_en_final_2026_09_28.py` | `whitelist_backup_2026_10_17/_en_final_2026_09_28.py` | 2,369 | `97a05aace5a8` | `97a05aace5a8` | `97a05aace5a8` | ✅ |
| 105 | `.tmp/_en_verify2_2026_09_28.py` | `.tmp/_en_verify2_2026_09_28.py` | `whitelist_backup_2026_10_17/_en_verify2_2026_09_28.py` | 1,870 | `7e84e75cb838` | `7e84e75cb838` | `7e84e75cb838` | ✅ |
| 106 | `.tmp/_en_verify3_2026_09_28.py` | `.tmp/_en_verify3_2026_09_28.py` | `whitelist_backup_2026_10_17/_en_verify3_2026_09_28.py` | 1,638 | `658292cce916` | `658292cce916` | `658292cce916` | ✅ |
| 107 | `.tmp/_en_verify4_2026_09_28.py` | `.tmp/_en_verify4_2026_09_28.py` | `whitelist_backup_2026_10_17/_en_verify4_2026_09_28.py` | 1,484 | `7eaeb9b4ba48` | `7eaeb9b4ba48` | `7eaeb9b4ba48` | ✅ |
| 108 | `.tmp/_en_verify_2026_09_28.py` | `.tmp/_en_verify_2026_09_28.py` | `whitelist_backup_2026_10_17/_en_verify_2026_09_28.py` | 6,071 | `51d9410d459b` | `51d9410d459b` | `51d9410d459b` | ✅ |
| 109 | `.tmp/_execswitch_verify_2026_09_28.py` | `.tmp/_execswitch_verify_2026_09_28.py` | `whitelist_backup_2026_10_17/_execswitch_verify_2026_09_28.py` | 3,501 | `0814f3c2d7ab` | `0814f3c2d7ab` | `0814f3c2d7ab` | ✅ |
| 110 | `.tmp/_final_check.py` | `.tmp/_final_check.py` | `whitelist_backup_2026_10_17/_final_check.py` | 1,562 | `ee7f008d36cb` | `ee7f008d36cb` | `ee7f008d36cb` | ✅ |
| 111 | `.tmp/_final_sha.py` | `.tmp/_final_sha.py` | `whitelist_backup_2026_10_17/_final_sha.py` | 1,435 | `8ea91ad82b9d` | `8ea91ad82b9d` | `8ea91ad82b9d` | ✅ |
| 112 | `.tmp/_final_verify.py` | `.tmp/_final_verify.py` | `whitelist_backup_2026_10_17/_final_verify.py` | 2,457 | `88aad6650405` | `88aad6650405` | `88aad6650405` | ✅ |
| 113 | `.tmp/_ge01_g7_register_build.py` | `.tmp/_ge01_g7_register_build.py` | `whitelist_backup_2026_10_17/_ge01_g7_register_build.py` | 33,147 | `7731337a516d` | `7731337a516d` | `7731337a516d` | ✅ |
| 114 | `.tmp/_ge01_g7_register_measure.py` | `.tmp/_ge01_g7_register_measure.py` | `whitelist_backup_2026_10_17/_ge01_g7_register_measure.py` | 5,090 | `5c3454c88a92` | `5c3454c88a92` | `5c3454c88a92` | ✅ |
| 115 | `.tmp/_gh_tree.txt` | `.tmp/_gh_tree.txt` | `whitelist_backup_2026_10_17/_gh_tree.txt` | 341,814 | `823cfbb23a03` | `823cfbb23a03` | `823cfbb23a03` | ✅ |
| 116 | `.tmp/_h_census_worker.json` | `.tmp/_h_census_worker.json` | `whitelist_backup_2026_10_17/_h_census_worker.json` | 10,037,568 | `22531e8519b2` | `22531e8519b2` | `22531e8519b2` | ✅ |
| 117 | `.tmp/_h_census_worker.py` | `.tmp/_h_census_worker.py` | `whitelist_backup_2026_10_17/_h_census_worker.py` | 5,639 | `7f858d86f865` | `7f858d86f865` | `7f858d86f865` | ✅ |
| 118 | `.tmp/_hash21.py` | `.tmp/_hash21.py` | `whitelist_backup_2026_10_17/_hash21.py` | 944 | `0d5335f0ac54` | `0d5335f0ac54` | `0d5335f0ac54` | ✅ |
| 119 | `.tmp/_inspect_10cells.py` | `.tmp/_inspect_10cells.py` | `whitelist_backup_2026_10_17/_inspect_10cells.py` | 2,460 | `919f8f4e8ad2` | `919f8f4e8ad2` | `919f8f4e8ad2` | ✅ |
| 120 | `.tmp/_inspect_batch4_rounds.py` | `.tmp/_inspect_batch4_rounds.py` | `whitelist_backup_2026_10_17/_inspect_batch4_rounds.py` | 898 | `bf479a2667df` | `bf479a2667df` | `bf479a2667df` | ✅ |
| 121 | `.tmp/_intake_cards_35_48_extract.py` | `.tmp/_intake_cards_35_48_extract.py` | `whitelist_backup_2026_10_17/_intake_cards_35_48_extract.py` | 3,416 | `74cca5bda270` | `74cca5bda270` | `74cca5bda270` | ✅ |
| 122 | `.tmp/_iscp_dual_impl_2026_10_09.py` | `.tmp/_iscp_dual_impl_2026_10_09.py` | `whitelist_backup_2026_10_17/_iscp_dual_impl_2026_10_09.py` | 2,974 | `8734f4326d5a` | `8734f4326d5a` | `8734f4326d5a` | ✅ |
| 123 | `.tmp/_item35_v3_collinear_recompute_2026_10_01.py` | `.tmp/_item35_v3_collinear_recompute_2026_10_01.py` | `whitelist_backup_2026_10_17/_item35_v3_collinear_recompute_2026_10_01.py` | 16,493 | `c8d859cbb69e` | `c8d859cbb69e` | `c8d859cbb69e` | ✅ |
| 124 | `.tmp/_kd04_c_den_exec_2026_10_10.py` | `.tmp/_kd04_c_den_exec_2026_10_10.py` | `whitelist_backup_2026_10_17/_kd04_c_den_exec_2026_10_10.py` | 21,430 | `419f9f691e63` | `419f9f691e63` | `419f9f691e63` | ✅ |
| 125 | `.tmp/_kv3s43_diag_2026_10_09.py` | `.tmp/_kv3s43_diag_2026_10_09.py` | `whitelist_backup_2026_10_17/_kv3s43_diag_2026_10_09.py` | 614 | `398ebf6f33e0` | `398ebf6f33e0` | `398ebf6f33e0` | ✅ |
| 126 | `.tmp/_lit_log.txt` | `.tmp/_lit_log.txt` | `whitelist_backup_2026_10_17/_lit_log.txt` | 8,733 | `b062da7b654a` | `b062da7b654a` | `b062da7b654a` | ✅ |
| 127 | `.tmp/_m5_k5_net.err` | `.tmp/_m5_k5_net.err` | `whitelist_backup_2026_10_17/_m5_k5_net.err` | 0 | `e3b0c44298fc` | `e3b0c44298fc` | `e3b0c44298fc` | ✅ |
| 128 | `.tmp/_m5_k5_net.json` | `.tmp/_m5_k5_net.json` | `whitelist_backup_2026_10_17/_m5_k5_net.json` | 92,060 | `9d7fe894a26b` | `9d7fe894a26b` | `9d7fe894a26b` | ✅ |
| 129 | `.tmp/_m5_k5_net.py` | `.tmp/_m5_k5_net.py` | `whitelist_backup_2026_10_17/_m5_k5_net.py` | 3,173 | `ec944f9178ea` | `ec944f9178ea` | `ec944f9178ea` | ✅ |
| 130 | `.tmp/_m5_k5_net2.json` | `.tmp/_m5_k5_net2.json` | `whitelist_backup_2026_10_17/_m5_k5_net2.json` | 952,252 | `b2bc158e7499` | `b2bc158e7499` | `b2bc158e7499` | ✅ |
| 131 | `.tmp/_m5_k5_scan.err` | `.tmp/_m5_k5_scan.err` | `whitelist_backup_2026_10_17/_m5_k5_scan.err` | 0 | `e3b0c44298fc` | `e3b0c44298fc` | `e3b0c44298fc` | ✅ |
| 132 | `.tmp/_m5_k5_scan.json` | `.tmp/_m5_k5_scan.json` | `whitelist_backup_2026_10_17/_m5_k5_scan.json` | 9,530 | `ebf1ad76dc8a` | `ebf1ad76dc8a` | `ebf1ad76dc8a` | ✅ |
| 133 | `.tmp/_m5_k5_scan.py` | `.tmp/_m5_k5_scan.py` | `whitelist_backup_2026_10_17/_m5_k5_scan.py` | 3,541 | `f5245072750f` | `f5245072750f` | `f5245072750f` | ✅ |
| 134 | `.tmp/_m5_reaudit_archive.py` | `.tmp/_m5_reaudit_archive.py` | `whitelist_backup_2026_10_17/_m5_reaudit_archive.py` | 1,405 | `54540d871fb7` | `54540d871fb7` | `54540d871fb7` | ✅ |
| 135 | `.tmp/_m5_reaudit_archive_out.json` | `.tmp/_m5_reaudit_archive_out.json` | `whitelist_backup_2026_10_17/_m5_reaudit_archive_out.json` | 654 | `e3542ccb4d3e` | `e3542ccb4d3e` | `e3542ccb4d3e` | ✅ |
| 136 | `.tmp/_m5_reaudit_detail.py` | `.tmp/_m5_reaudit_detail.py` | `whitelist_backup_2026_10_17/_m5_reaudit_detail.py` | 2,276 | `f43d192a9726` | `f43d192a9726` | `f43d192a9726` | ✅ |
| 137 | `.tmp/_m5_reaudit_detail.txt` | `.tmp/_m5_reaudit_detail.txt` | `whitelist_backup_2026_10_17/_m5_reaudit_detail.txt` | 9,214 | `8c117d51fc64` | `8c117d51fc64` | `8c117d51fc64` | ✅ |
| 138 | `.tmp/_m5_reaudit_probe.py` | `.tmp/_m5_reaudit_probe.py` | `whitelist_backup_2026_10_17/_m5_reaudit_probe.py` | 4,469 | `5b005dd13f95` | `5b005dd13f95` | `5b005dd13f95` | ✅ |
| 139 | `.tmp/_mk_voided_reloc_register.py` | `.tmp/_mk_voided_reloc_register.py` | `whitelist_backup_2026_10_17/_mk_voided_reloc_register.py` | 13,003 | `7c2d2f6955d0` | `7c2d2f6955d0` | `7c2d2f6955d0` | ✅ |
| 140 | `.tmp/_n1_n2_check.py` | `.tmp/_n1_n2_check.py` | `whitelist_backup_2026_10_17/_n1_n2_check.py` | 1,628 | `71f3f53a6eed` | `71f3f53a6eed` | `71f3f53a6eed` | ✅ |
| 141 | `.tmp/_ofc_s1_inventory.json` | `.tmp/_ofc_s1_inventory.json` | `whitelist_backup_2026_10_17/_ofc_s1_inventory.json` | 216,695 | `c2858312798b` | `c2858312798b` | `c2858312798b` | ✅ |
| 142 | `.tmp/_ofc_s1b_inventory.json` | `.tmp/_ofc_s1b_inventory.json` | `whitelist_backup_2026_10_17/_ofc_s1b_inventory.json` | 336,955 | `a28f35879008` | `a28f35879008` | `a28f35879008` | ✅ |
| 143 | `.tmp/_patch21_emit.py` | `.tmp/_patch21_emit.py` | `whitelist_backup_2026_10_17/_patch21_emit.py` | 17,106 | `1d3c8aea6bad` | `1d3c8aea6bad` | `1d3c8aea6bad` | ✅ |
| 144 | `.tmp/_patch21_make.py` | `.tmp/_patch21_make.py` | `whitelist_backup_2026_10_17/_patch21_make.py` | 8,807 | `b6cfdfaf80fa` | `b6cfdfaf80fa` | `b6cfdfaf80fa` | ✅ |
| 145 | `.tmp/_patch21_run.py` | `.tmp/_patch21_run.py` | `whitelist_backup_2026_10_17/_patch21_run.py` | 3,866 | `6333d9256716` | `6333d9256716` | `6333d9256716` | ✅ |
| 146 | `.tmp/_pc.py` | `.tmp/_pc.py` | `whitelist_backup_2026_10_17/_pc.py` | 431 | `7c59c7e80d50` | `7c59c7e80d50` | `7c59c7e80d50` | ✅ |
| 147 | `.tmp/_pk_probe.py` | `.tmp/_pk_probe.py` | `whitelist_backup_2026_10_17/_pk_probe.py` | 398 | `6d79ba939526` | `6d79ba939526` | `6d79ba939526` | ✅ |
| 148 | `.tmp/_pk_sha_scan.py` | `.tmp/_pk_sha_scan.py` | `whitelist_backup_2026_10_17/_pk_sha_scan.py` | 599 | `df460eaec619` | `df460eaec619` | `df460eaec619` | ✅ |
| 149 | `.tmp/_pkf34_f3.py` | `.tmp/_pkf34_f3.py` | `whitelist_backup_2026_10_17/_pkf34_f3.py` | 3,068 | `389b3fdecd29` | `389b3fdecd29` | `389b3fdecd29` | ✅ |
| 150 | `.tmp/_pkf34_f34.py` | `.tmp/_pkf34_f34.py` | `whitelist_backup_2026_10_17/_pkf34_f34.py` | 4,282 | `a972a0383cf4` | `a972a0383cf4` | `a972a0383cf4` | ✅ |
| 151 | `.tmp/_pkf34_f3b.py` | `.tmp/_pkf34_f3b.py` | `whitelist_backup_2026_10_17/_pkf34_f3b.py` | 2,703 | `e1bcbf3897d8` | `e1bcbf3897d8` | `e1bcbf3897d8` | ✅ |
| 152 | `.tmp/_pkf34_f4.py` | `.tmp/_pkf34_f4.py` | `whitelist_backup_2026_10_17/_pkf34_f4.py` | 3,958 | `880a69b9cf29` | `880a69b9cf29` | `880a69b9cf29` | ✅ |
| 153 | `.tmp/_pkf34_f4b.py` | `.tmp/_pkf34_f4b.py` | `whitelist_backup_2026_10_17/_pkf34_f4b.py` | 4,401 | `e97f6ee41bec` | `e97f6ee41bec` | `e97f6ee41bec` | ✅ |
| 154 | `.tmp/_pkf34_f4c.py` | `.tmp/_pkf34_f4c.py` | `whitelist_backup_2026_10_17/_pkf34_f4c.py` | 3,045 | `c758efa2a529` | `c758efa2a529` | `c758efa2a529` | ✅ |
| 155 | `.tmp/_pkf34_f4d.py` | `.tmp/_pkf34_f4d.py` | `whitelist_backup_2026_10_17/_pkf34_f4d.py` | 3,686 | `fb565a667edc` | `fb565a667edc` | `fb565a667edc` | ✅ |
| 156 | `.tmp/_pkf34_final.py` | `.tmp/_pkf34_final.py` | `whitelist_backup_2026_10_17/_pkf34_final.py` | 5,903 | `4b6140aaa618` | `4b6140aaa618` | `4b6140aaa618` | ✅ |
| 157 | `.tmp/_pkf34_nd.py` | `.tmp/_pkf34_nd.py` | `whitelist_backup_2026_10_17/_pkf34_nd.py` | 2,537 | `527883f7ebb8` | `527883f7ebb8` | `527883f7ebb8` | ✅ |
| 158 | `.tmp/_pkf34_v12.py` | `.tmp/_pkf34_v12.py` | `whitelist_backup_2026_10_17/_pkf34_v12.py` | 5,639 | `c650b0c20eee` | `c650b0c20eee` | `c650b0c20eee` | ✅ |
| 159 | `.tmp/_postcheck_v16_alt.py` | `.tmp/_postcheck_v16_alt.py` | `whitelist_backup_2026_10_17/_postcheck_v16_alt.py` | 1,282 | `4d485d7a4d91` | `4d485d7a4d91` | `4d485d7a4d91` | ✅ |
| 160 | `.tmp/_postcheck_v16_alt_stdout.txt` | `.tmp/_postcheck_v16_alt_stdout.txt` | `whitelist_backup_2026_10_17/_postcheck_v16_alt_stdout.txt` | 1,558 | `f116b23fa967` | `f116b23fa967` | `f116b23fa967` | ✅ |
| 161 | `.tmp/_postcheck_v16_sha.py` | `.tmp/_postcheck_v16_sha.py` | `whitelist_backup_2026_10_17/_postcheck_v16_sha.py` | 1,391 | `46759ba2b8e5` | `46759ba2b8e5` | `46759ba2b8e5` | ✅ |
| 162 | `.tmp/_precheck_v15_tail.ps1` | `.tmp/_precheck_v15_tail.ps1` | `whitelist_backup_2026_10_17/_precheck_v15_tail.ps1` | 505 | `e94d8011bbf4` | `e94d8011bbf4` | `e94d8011bbf4` | ✅ |
| 163 | `.tmp/_probe21.py` | `.tmp/_probe21.py` | `whitelist_backup_2026_10_17/_probe21.py` | 564 | `5a40370032b3` | `5a40370032b3` | `5a40370032b3` | ✅ |
| 164 | `.tmp/_r10.py` | `.tmp/_r10.py` | `whitelist_backup_2026_10_17/_r10.py` | 1,525 | `1b012cd12a00` | `1b012cd12a00` | `1b012cd12a00` | ✅ |
| 165 | `.tmp/_r1_alarm_test.py` | `.tmp/_r1_alarm_test.py` | `whitelist_backup_2026_10_17/_r1_alarm_test.py` | 2,297 | `c44a09297f1a` | `c44a09297f1a` | `c44a09297f1a` | ✅ |
| 166 | `.tmp/_r2_body.md` | `.tmp/_r2_body.md` | `whitelist_backup_2026_10_17/_r2_body.md` | 63,091 | `1dbe20a3ba1c` | `1dbe20a3ba1c` | `1dbe20a3ba1c` | ✅ |
| 167 | `.tmp/_r3_header_fix_2026_09_28.py` | `.tmp/_r3_header_fix_2026_09_28.py` | `whitelist_backup_2026_10_17/_r3_header_fix_2026_09_28.py` | 3,280 | `6f8cec0fe006` | `6f8cec0fe006` | `6f8cec0fe006` | ✅ |
| 168 | `.tmp/_r3_verify_2026_09_28.py` | `.tmp/_r3_verify_2026_09_28.py` | `whitelist_backup_2026_10_17/_r3_verify_2026_09_28.py` | 5,494 | `721e52f9d55f` | `721e52f9d55f` | `721e52f9d55f` | ✅ |
| 169 | `.tmp/_r4_cleanup_worker_keycount_2026_09_29.py` | `.tmp/_r4_cleanup_worker_keycount_2026_09_29.py` | `whitelist_backup_2026_10_17/_r4_cleanup_worker_keycount_2026_09_29.py` | 1,909 | `ca0cbafed00b` | `ca0cbafed00b` | `ca0cbafed00b` | ✅ |
| 170 | `.tmp/_r4_cleanup_worker_keyscan_2026_09_29.py` | `.tmp/_r4_cleanup_worker_keyscan_2026_09_29.py` | `whitelist_backup_2026_10_17/_r4_cleanup_worker_keyscan_2026_09_29.py` | 3,561 | `01e1ac2ef239` | `01e1ac2ef239` | `01e1ac2ef239` | ✅ |
| 171 | `.tmp/_r4_cleanup_worker_nearmiss_2026_09_29.py` | `.tmp/_r4_cleanup_worker_nearmiss_2026_09_29.py` | `whitelist_backup_2026_10_17/_r4_cleanup_worker_nearmiss_2026_09_29.py` | 1,382 | `22336cc16500` | `22336cc16500` | `22336cc16500` | ✅ |
| 172 | `.tmp/_r4_cleanup_worker_scan_2026_09_29.py` | `.tmp/_r4_cleanup_worker_scan_2026_09_29.py` | `whitelist_backup_2026_10_17/_r4_cleanup_worker_scan_2026_09_29.py` | 2,411 | `af404c489392` | `af404c489392` | `af404c489392` | ✅ |
| 173 | `.tmp/_r4_cleanup_worker_shape_2026_09_29.py` | `.tmp/_r4_cleanup_worker_shape_2026_09_29.py` | `whitelist_backup_2026_10_17/_r4_cleanup_worker_shape_2026_09_29.py` | 1,110 | `f7f6313edce8` | `f7f6313edce8` | `f7f6313edce8` | ✅ |
| 174 | `.tmp/_r4_key_scan_2026_09_24.py` | `.tmp/_r4_key_scan_2026_09_24.py` | `whitelist_backup_2026_10_17/_r4_key_scan_2026_09_24.py` | 3,743 | `c782d1a18092` | `c782d1a18092` | `c782d1a18092` | ✅ |
| 175 | `.tmp/_r4_key_scan_r1_files_2026_09_27.py` | `.tmp/_r4_key_scan_r1_files_2026_09_27.py` | `whitelist_backup_2026_10_17/_r4_key_scan_r1_files_2026_09_27.py` | 4,079 | `cec4c1f3ff9c` | `cec4c1f3ff9c` | `cec4c1f3ff9c` | ✅ |
| 176 | `.tmp/_r5_write_register_2026_10_13.py` | `.tmp/_r5_write_register_2026_10_13.py` | `whitelist_backup_2026_10_17/_r5_write_register_2026_10_13.py` | 25,902 | `139c8a7316db` | `139c8a7316db` | `139c8a7316db` | ✅ |
| 177 | `.tmp/_r6_evidence.py` | `.tmp/_r6_evidence.py` | `whitelist_backup_2026_10_17/_r6_evidence.py` | 2,525 | `4de12a4f441b` | `4de12a4f441b` | `4de12a4f441b` | ✅ |
| 178 | `.tmp/_recheck_r1_run1.log` | `.tmp/_recheck_r1_run1.log` | `whitelist_backup_2026_10_17/_recheck_r1_run1.log` | 2,486 | `80b338a0e9ad` | `80b338a0e9ad` | `80b338a0e9ad` | ✅ |
| 179 | `.tmp/_recheck_r1_runA.log` | `.tmp/_recheck_r1_runA.log` | `whitelist_backup_2026_10_17/_recheck_r1_runA.log` | 2,634 | `68c85cf076d1` | `68c85cf076d1` | `68c85cf076d1` | ✅ |
| 180 | `.tmp/_recheck_r1_runB.log` | `.tmp/_recheck_r1_runB.log` | `whitelist_backup_2026_10_17/_recheck_r1_runB.log` | 2,634 | `68c85cf076d1` | `68c85cf076d1` | `68c85cf076d1` | ✅ |
| 181 | `.tmp/_recheck_r1_runC.log` | `.tmp/_recheck_r1_runC.log` | `whitelist_backup_2026_10_17/_recheck_r1_runC.log` | 2,568 | `b15384cff9f0` | `b15384cff9f0` | `b15384cff9f0` | ✅ |
| 182 | `.tmp/_recheck_r1_runD.log` | `.tmp/_recheck_r1_runD.log` | `whitelist_backup_2026_10_17/_recheck_r1_runD.log` | 2,568 | `b15384cff9f0` | `b15384cff9f0` | `b15384cff9f0` | ✅ |
| 183 | `.tmp/_rj5_convention_check_2026_09_27.out.json` | `.tmp/_rj5_convention_check_2026_09_27.out.json` | `whitelist_backup_2026_10_17/_rj5_convention_check_2026_09_27.out.json` | 8,983 | `c88e4ba1a4ce` | `c88e4ba1a4ce` | `c88e4ba1a4ce` | ✅ |
| 184 | `.tmp/_rj5_convention_check_2026_09_27.py` | `.tmp/_rj5_convention_check_2026_09_27.py` | `whitelist_backup_2026_10_17/_rj5_convention_check_2026_09_27.py` | 8,018 | `5dbb93b3c5e5` | `5dbb93b3c5e5` | `5dbb93b3c5e5` | ✅ |
| 185 | `.tmp/_rj5_mapping_test_2026_09_27.py` | `.tmp/_rj5_mapping_test_2026_09_27.py` | `whitelist_backup_2026_10_17/_rj5_mapping_test_2026_09_27.py` | 5,968 | `75ff70d87bd7` | `75ff70d87bd7` | `75ff70d87bd7` | ✅ |
| 186 | `.tmp/_rp4_fields.py` | `.tmp/_rp4_fields.py` | `whitelist_backup_2026_10_17/_rp4_fields.py` | 433 | `1d112ab8f3b4` | `1d112ab8f3b4` | `1d112ab8f3b4` | ✅ |
| 187 | `.tmp/_rp_addendum_build_2026_10_09.py` | `.tmp/_rp_addendum_build_2026_10_09.py` | `whitelist_backup_2026_10_17/_rp_addendum_build_2026_10_09.py` | 30,375 | `c4e8b75d656b` | `c4e8b75d656b` | `c4e8b75d656b` | ✅ |
| 188 | `.tmp/_rp_verify_2026_10_09.py` | `.tmp/_rp_verify_2026_10_09.py` | `whitelist_backup_2026_10_17/_rp_verify_2026_10_09.py` | 3,282 | `e0adae15fc26` | `e0adae15fc26` | `e0adae15fc26` | ✅ |
| 189 | `.tmp/_rpd_neighbors_2026_10_09.py` | `.tmp/_rpd_neighbors_2026_10_09.py` | `whitelist_backup_2026_10_17/_rpd_neighbors_2026_10_09.py` | 1,286 | `28cfa9466ea3` | `28cfa9466ea3` | `28cfa9466ea3` | ✅ |
| 190 | `.tmp/_rpd_reuse_strict_2026_10_09.py` | `.tmp/_rpd_reuse_strict_2026_10_09.py` | `whitelist_backup_2026_10_17/_rpd_reuse_strict_2026_10_09.py` | 4,746 | `4557b47b7361` | `4557b47b7361` | `4557b47b7361` | ✅ |
| 191 | `.tmp/_rpd_verify_landed_2026_10_09.py` | `.tmp/_rpd_verify_landed_2026_10_09.py` | `whitelist_backup_2026_10_17/_rpd_verify_landed_2026_10_09.py` | 6,335 | `912a2b8066f1` | `912a2b8066f1` | `912a2b8066f1` | ✅ |
| 192 | `.tmp/_run2.py` | `.tmp/_run2.py` | `whitelist_backup_2026_10_17/_run2.py` | 4,366 | `8acbf24342d1` | `8acbf24342d1` | `8acbf24342d1` | ✅ |
| 193 | `.tmp/_run_d4_relabel_addendum.py` | `.tmp/_run_d4_relabel_addendum.py` | `whitelist_backup_2026_10_17/_run_d4_relabel_addendum.py` | 17,550 | `620eabf853af` | `620eabf853af` | `620eabf853af` | ✅ |
| 194 | `.tmp/_run_d6_addendum_2026_09_28.py` | `.tmp/_run_d6_addendum_2026_09_28.py` | `whitelist_backup_2026_10_17/_run_d6_addendum_2026_09_28.py` | 23,204 | `e472ea36ed08` | `e472ea36ed08` | `e472ea36ed08` | ✅ |
| 195 | `.tmp/_run_d6b_addendum_2026_09_28.py` | `.tmp/_run_d6b_addendum_2026_09_28.py` | `whitelist_backup_2026_10_17/_run_d6b_addendum_2026_09_28.py` | 31,468 | `f0a4e919eeaa` | `f0a4e919eeaa` | `f0a4e919eeaa` | ✅ |
| 196 | `.tmp/_run_d8_addendum_2026_09_30.py` | `.tmp/_run_d8_addendum_2026_09_30.py` | `whitelist_backup_2026_10_17/_run_d8_addendum_2026_09_30.py` | 107,959 | `7ce330b3e5ae` | `7ce330b3e5ae` | `7ce330b3e5ae` | ✅ |
| 197 | `.tmp/_run_d8_bhalf_addendum_2026_09_30.py` | `.tmp/_run_d8_bhalf_addendum_2026_09_30.py` | `whitelist_backup_2026_10_17/_run_d8_bhalf_addendum_2026_09_30.py` | 40,576 | `90fa2c443529` | `90fa2c443529` | `90fa2c443529` | ✅ |
| 198 | `.tmp/_run_day_inventory_table_2026_09_27.py` | `.tmp/_run_day_inventory_table_2026_09_27.py` | `whitelist_backup_2026_10_17/_run_day_inventory_table_2026_09_27.py` | 2,763 | `329bf2b66422` | `329bf2b66422` | `329bf2b66422` | ✅ |
| 199 | `.tmp/_run_final.py` | `.tmp/_run_final.py` | `whitelist_backup_2026_10_17/_run_final.py` | 26,654 | `75d466add5d5` | `75d466add5d5` | `75d466add5d5` | ✅ |
| 200 | `.tmp/_run_final_selfscan_2026_09_27.py` | `.tmp/_run_final_selfscan_2026_09_27.py` | `whitelist_backup_2026_10_17/_run_final_selfscan_2026_09_27.py` | 1,358 | `cf5c5c7684bb` | `cf5c5c7684bb` | `cf5c5c7684bb` | ✅ |
| 201 | `.tmp/_run_frozen_0touch_verify_2026_09_27.py` | `.tmp/_run_frozen_0touch_verify_2026_09_27.py` | `whitelist_backup_2026_10_17/_run_frozen_0touch_verify_2026_09_27.py` | 2,309 | `48246f41e7d3` | `48246f41e7d3` | `48246f41e7d3` | ✅ |
| 202 | `.tmp/_run_recheck_r1.py` | `.tmp/_run_recheck_r1.py` | `whitelist_backup_2026_10_17/_run_recheck_r1.py` | 34,895 | `a76ec3a2340e` | `a76ec3a2340e` | `a76ec3a2340e` | ✅ |
| 203 | `.tmp/_run_result_v3.py` | `.tmp/_run_result_v3.py` | `whitelist_backup_2026_10_17/_run_result_v3.py` | 3,304 | `83cd4414f404` | `83cd4414f404` | `83cd4414f404` | ✅ |
| 204 | `.tmp/_run_v3r1_relabel.py` | `.tmp/_run_v3r1_relabel.py` | `whitelist_backup_2026_10_17/_run_v3r1_relabel.py` | 30,875 | `55d06ce42b3d` | `55d06ce42b3d` | `55d06ce42b3d` | ✅ |
| 205 | `.tmp/_s3_f1_loader_fix_recompute_2026_10_08.py` | `.tmp/_s3_f1_loader_fix_recompute_2026_10_08.py` | `whitelist_backup_2026_10_17/_s3_f1_loader_fix_recompute_2026_10_08.py` | 21,231 | `e39e4ae7d6ed` | `e39e4ae7d6ed` | `e39e4ae7d6ed` | ✅ |
| 206 | `.tmp/_s4_freeze_count_crosscheck2_2026_10_09.py` | `.tmp/_s4_freeze_count_crosscheck2_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4_freeze_count_crosscheck2_2026_10_09.py` | 3,920 | `15fa4d155fc9` | `15fa4d155fc9` | `15fa4d155fc9` | ✅ |
| 207 | `.tmp/_s4_freeze_count_crosscheck3_2026_10_09.py` | `.tmp/_s4_freeze_count_crosscheck3_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4_freeze_count_crosscheck3_2026_10_09.py` | 4,041 | `ee420dfd57e6` | `ee420dfd57e6` | `ee420dfd57e6` | ✅ |
| 208 | `.tmp/_s4_freeze_count_crosscheck_2026_10_09.py` | `.tmp/_s4_freeze_count_crosscheck_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4_freeze_count_crosscheck_2026_10_09.py` | 3,463 | `856e6ab48dae` | `856e6ab48dae` | `856e6ab48dae` | ✅ |
| 209 | `.tmp/_s4_seedprime_seq_t1_supplement_2026_10_11.py` | `.tmp/_s4_seedprime_seq_t1_supplement_2026_10_11.py` | `whitelist_backup_2026_10_17/_s4_seedprime_seq_t1_supplement_2026_10_11.py` | 31,705 | `3a9db2126e4f` | `3a9db2126e4f` | `3a9db2126e4f` | ✅ |
| 210 | `.tmp/_s4_topup_addendum_builder_2026_10_09.py` | `.tmp/_s4_topup_addendum_builder_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4_topup_addendum_builder_2026_10_09.py` | 21,122 | `b9987c7a8d5f` | `b9987c7a8d5f` | `b9987c7a8d5f` | ✅ |
| 211 | `.tmp/_s4_tree_construct_exec_2026_10_10.py` | `.tmp/_s4_tree_construct_exec_2026_10_10.py` | `whitelist_backup_2026_10_17/_s4_tree_construct_exec_2026_10_10.py` | 34,265 | `4cbd10b61aae` | `4cbd10b61aae` | `4cbd10b61aae` | ✅ |
| 212 | `.tmp/_s4f2_dbg.py` | `.tmp/_s4f2_dbg.py` | `whitelist_backup_2026_10_17/_s4f2_dbg.py` | 431 | `5159c9c30180` | `5159c9c30180` | `5159c9c30180` | ✅ |
| 213 | `.tmp/_s4f2_face_probe_2026_10_09.py` | `.tmp/_s4f2_face_probe_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4f2_face_probe_2026_10_09.py` | 14,896 | `62e04248d122` | `62e04248d122` | `62e04248d122` | ✅ |
| 214 | `.tmp/_s4f2_patch.py` | `.tmp/_s4f2_patch.py` | `whitelist_backup_2026_10_17/_s4f2_patch.py` | 2,740 | `b79a7073099d` | `b79a7073099d` | `b79a7073099d` | ✅ |
| 215 | `.tmp/_s4f2_patch2.py` | `.tmp/_s4f2_patch2.py` | `whitelist_backup_2026_10_17/_s4f2_patch2.py` | 421 | `045bd90b237a` | `045bd90b237a` | `045bd90b237a` | ✅ |
| 216 | `.tmp/_s4f2_patch3.py` | `.tmp/_s4f2_patch3.py` | `whitelist_backup_2026_10_17/_s4f2_patch3.py` | 815 | `6d57ff4ce76c` | `6d57ff4ce76c` | `6d57ff4ce76c` | ✅ |
| 217 | `.tmp/_s4f2_patch4.py` | `.tmp/_s4f2_patch4.py` | `whitelist_backup_2026_10_17/_s4f2_patch4.py` | 565 | `7d85756a841d` | `7d85756a841d` | `7d85756a841d` | ✅ |
| 218 | `.tmp/_s4f2_scanner_selftest.py` | `.tmp/_s4f2_scanner_selftest.py` | `whitelist_backup_2026_10_17/_s4f2_scanner_selftest.py` | 1,819 | `5b6fd262f785` | `5b6fd262f785` | `5b6fd262f785` | ✅ |
| 219 | `.tmp/_s4fs_auxdate_2026_10_09.py` | `.tmp/_s4fs_auxdate_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4fs_auxdate_2026_10_09.py` | 1,877 | `637e936d8bc7` | `637e936d8bc7` | `637e936d8bc7` | ✅ |
| 220 | `.tmp/_s4fs_selfreport_2026_10_09.py` | `.tmp/_s4fs_selfreport_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4fs_selfreport_2026_10_09.py` | 432 | `485071c7dd5e` | `485071c7dd5e` | `485071c7dd5e` | ✅ |
| 221 | `.tmp/_s4fs_yitable_2026_10_09.py` | `.tmp/_s4fs_yitable_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4fs_yitable_2026_10_09.py` | 1,634 | `2bf7fd0ef5dc` | `2bf7fd0ef5dc` | `2bf7fd0ef5dc` | ✅ |
| 222 | `.tmp/_s4oq_addendum_struct_2026_10_09.py` | `.tmp/_s4oq_addendum_struct_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_addendum_struct_2026_10_09.py` | 843 | `67652acdf681` | `67652acdf681` | `67652acdf681` | ✅ |
| 223 | `.tmp/_s4oq_build_baseline_2026_10_09.py` | `.tmp/_s4oq_build_baseline_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_build_baseline_2026_10_09.py` | 3,501 | `3cf28fe89611` | `3cf28fe89611` | `3cf28fe89611` | ✅ |
| 224 | `.tmp/_s4oq_build_draft_2026_10_09.py` | `.tmp/_s4oq_build_draft_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_build_draft_2026_10_09.py` | 8,719 | `0797d19dcaf3` | `0797d19dcaf3` | `0797d19dcaf3` | ✅ |
| 225 | `.tmp/_s4oq_cellmap_2026_10_09.py` | `.tmp/_s4oq_cellmap_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_cellmap_2026_10_09.py` | 1,734 | `c07589f292e1` | `c07589f292e1` | `c07589f292e1` | ✅ |
| 226 | `.tmp/_s4oq_final_verify_2026_10_09.py` | `.tmp/_s4oq_final_verify_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_final_verify_2026_10_09.py` | 959 | `944a4f7006c8` | `944a4f7006c8` | `944a4f7006c8` | ✅ |
| 227 | `.tmp/_s4oq_forward_2026_10_09.py` | `.tmp/_s4oq_forward_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_forward_2026_10_09.py` | 3,482 | `43e72c62587d` | `43e72c62587d` | `43e72c62587d` | ✅ |
| 228 | `.tmp/_s4oq_grid_cmp_2026_10_09.py` | `.tmp/_s4oq_grid_cmp_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_grid_cmp_2026_10_09.py` | 1,601 | `f00865587d6a` | `f00865587d6a` | `f00865587d6a` | ✅ |
| 229 | `.tmp/_s4oq_grid_diag_2026_10_09.py` | `.tmp/_s4oq_grid_diag_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_grid_diag_2026_10_09.py` | 1,553 | `082e8b8b7bc4` | `082e8b8b7bc4` | `082e8b8b7bc4` | ✅ |
| 230 | `.tmp/_s4oq_grid_recompute_2026_10_09.py` | `.tmp/_s4oq_grid_recompute_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_grid_recompute_2026_10_09.py` | 2,394 | `afb613f5ced1` | `afb613f5ced1` | `afb613f5ced1` | ✅ |
| 231 | `.tmp/_s4oq_keyscan_2026_10_09.py` | `.tmp/_s4oq_keyscan_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_keyscan_2026_10_09.py` | 573 | `c9f94c812f7f` | `c9f94c812f7f` | `c9f94c812f7f` | ✅ |
| 232 | `.tmp/_s4oq_recompute_2026_10_09.py` | `.tmp/_s4oq_recompute_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_recompute_2026_10_09.py` | 3,202 | `07cdec653345` | `07cdec653345` | `07cdec653345` | ✅ |
| 233 | `.tmp/_s4oq_reuse_check_2026_10_09.py` | `.tmp/_s4oq_reuse_check_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_reuse_check_2026_10_09.py` | 6,712 | `952c76c5b103` | `952c76c5b103` | `952c76c5b103` | ✅ |
| 234 | `.tmp/_s4oq_reuse_v2_2026_10_09.py` | `.tmp/_s4oq_reuse_v2_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_reuse_v2_2026_10_09.py` | 6,293 | `bc0f200edd1e` | `bc0f200edd1e` | `bc0f200edd1e` | ✅ |
| 235 | `.tmp/_s4oq_skel_2026_10_09.py` | `.tmp/_s4oq_skel_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_skel_2026_10_09.py` | 466 | `73fc780b4849` | `73fc780b4849` | `73fc780b4849` | ✅ |
| 236 | `.tmp/_s4oq_slug_opt_2026_10_09.py` | `.tmp/_s4oq_slug_opt_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_slug_opt_2026_10_09.py` | 4,636 | `77d696b1690d` | `77d696b1690d` | `77d696b1690d` | ✅ |
| 237 | `.tmp/_s4oq_slug_search2_2026_10_09.py` | `.tmp/_s4oq_slug_search2_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_slug_search2_2026_10_09.py` | 5,258 | `fe6f7044ec4e` | `fe6f7044ec4e` | `fe6f7044ec4e` | ✅ |
| 238 | `.tmp/_s4oq_variants_2026_10_09.py` | `.tmp/_s4oq_variants_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_variants_2026_10_09.py` | 1,233 | `ccbbb499e19a` | `ccbbb499e19a` | `ccbbb499e19a` | ✅ |
| 239 | `.tmp/_s4oq_verify_addendum_2026_10_09.py` | `.tmp/_s4oq_verify_addendum_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_verify_addendum_2026_10_09.py` | 2,252 | `419c15a7a2c5` | `419c15a7a2c5` | `419c15a7a2c5` | ✅ |
| 240 | `.tmp/_s4oq_write_addendum_2026_10_09.py` | `.tmp/_s4oq_write_addendum_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4oq_write_addendum_2026_10_09.py` | 11,886 | `63e61afa6517` | `63e61afa6517` | `63e61afa6517` | ✅ |
| 241 | `.tmp/_s4td_cell_map_2026_10_09.py` | `.tmp/_s4td_cell_map_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4td_cell_map_2026_10_09.py` | 3,642 | `6665669d858d` | `6665669d858d` | `6665669d858d` | ✅ |
| 242 | `.tmp/_s4td_floor_bound_2026_10_09.py` | `.tmp/_s4td_floor_bound_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4td_floor_bound_2026_10_09.py` | 4,378 | `ad95b6d5e9b9` | `ad95b6d5e9b9` | `ad95b6d5e9b9` | ✅ |
| 243 | `.tmp/_s4td_reuse_and_bound_2026_10_09.py` | `.tmp/_s4td_reuse_and_bound_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4td_reuse_and_bound_2026_10_09.py` | 8,765 | `af6fdc892f60` | `af6fdc892f60` | `af6fdc892f60` | ✅ |
| 244 | `.tmp/_s4td_slug_search_2026_10_09.py` | `.tmp/_s4td_slug_search_2026_10_09.py` | `whitelist_backup_2026_10_17/_s4td_slug_search_2026_10_09.py` | 4,657 | `ce5529ec7516` | `ce5529ec7516` | `ce5529ec7516` | ✅ |
| 245 | `.tmp/_s5dp_five_lines_runner_third_2026_10_11.py` | `.tmp/_s5dp_five_lines_runner_third_2026_10_11.py` | `whitelist_backup_2026_10_17/_s5dp_five_lines_runner_third_2026_10_11.py` | 31,138 | `9de3c08e3863` | `9de3c08e3863` | `9de3c08e3863` | ✅ |
| 246 | `.tmp/_sensitivity.py` | `.tmp/_sensitivity.py` | `whitelist_backup_2026_10_17/_sensitivity.py` | 5,954 | `8aacafa48f9c` | `8aacafa48f9c` | `8aacafa48f9c` | ✅ |
| 247 | `.tmp/_sha12_check.ps1` | `.tmp/_sha12_check.ps1` | `whitelist_backup_2026_10_17/_sha12_check.ps1` | 697 | `a4bfec107a77` | `a4bfec107a77` | `a4bfec107a77` | ✅ |
| 248 | `.tmp/_sha12_check2.ps1` | `.tmp/_sha12_check2.ps1` | `whitelist_backup_2026_10_17/_sha12_check2.ps1` | 691 | `3e9174fb1e03` | `3e9174fb1e03` | `3e9174fb1e03` | ✅ |
| 249 | `.tmp/_t15_inspect.py` | `.tmp/_t15_inspect.py` | `whitelist_backup_2026_10_17/_t15_inspect.py` | 2,728 | `9877c9536e33` | `9877c9536e33` | `9877c9536e33` | ✅ |
| 250 | `.tmp/_t15_inspect2.py` | `.tmp/_t15_inspect2.py` | `whitelist_backup_2026_10_17/_t15_inspect2.py` | 1,942 | `9a6b5bb328aa` | `9a6b5bb328aa` | `9a6b5bb328aa` | ✅ |
| 251 | `.tmp/_t15_inspect3.py` | `.tmp/_t15_inspect3.py` | `whitelist_backup_2026_10_17/_t15_inspect3.py` | 1,890 | `d423ca72cb3c` | `d423ca72cb3c` | `d423ca72cb3c` | ✅ |
| 252 | `.tmp/_t15_inspect4.py` | `.tmp/_t15_inspect4.py` | `whitelist_backup_2026_10_17/_t15_inspect4.py` | 2,756 | `069b7562f463` | `069b7562f463` | `069b7562f463` | ✅ |
| 253 | `.tmp/_t15_inspect5.py` | `.tmp/_t15_inspect5.py` | `whitelist_backup_2026_10_17/_t15_inspect5.py` | 2,712 | `977753c193d2` | `977753c193d2` | `977753c193d2` | ✅ |
| 254 | `.tmp/_t15_inspect6.py` | `.tmp/_t15_inspect6.py` | `whitelist_backup_2026_10_17/_t15_inspect6.py` | 1,234 | `eba3a29f6264` | `eba3a29f6264` | `eba3a29f6264` | ✅ |
| 255 | `.tmp/_t15_inspect7.py` | `.tmp/_t15_inspect7.py` | `whitelist_backup_2026_10_17/_t15_inspect7.py` | 3,880 | `78dafdf124f7` | `78dafdf124f7` | `78dafdf124f7` | ✅ |
| 256 | `.tmp/_t15_percell.py` | `.tmp/_t15_percell.py` | `whitelist_backup_2026_10_17/_t15_percell.py` | 596 | `c035476cfb41` | `c035476cfb41` | `c035476cfb41` | ✅ |
| 257 | `.tmp/_t15_probe_log.json` | `.tmp/_t15_probe_log.json` | `whitelist_backup_2026_10_17/_t15_probe_log.json` | 718 | `94444963ff77` | `94444963ff77` | `94444963ff77` | ✅ |
| 258 | `.tmp/_t15_records.json` | `.tmp/_t15_records.json` | `whitelist_backup_2026_10_17/_t15_records.json` | 96,443 | `8014af0e2b79` | `8014af0e2b79` | `8014af0e2b79` | ✅ |
| 259 | `.tmp/_t15_update_result.py` | `.tmp/_t15_update_result.py` | `whitelist_backup_2026_10_17/_t15_update_result.py` | 9,226 | `ad66f242c6a1` | `ad66f242c6a1` | `ad66f242c6a1` | ✅ |
| 260 | `.tmp/_t15r2_inspect.py` | `.tmp/_t15r2_inspect.py` | `whitelist_backup_2026_10_17/_t15r2_inspect.py` | 3,730 | `c58dc90fd86a` | `c58dc90fd86a` | `c58dc90fd86a` | ✅ |
| 261 | `.tmp/_t15r2_verify.py` | `.tmp/_t15r2_verify.py` | `whitelist_backup_2026_10_17/_t15r2_verify.py` | 6,737 | `5267b4dee7dc` | `5267b4dee7dc` | `5267b4dee7dc` | ✅ |
| 262 | `.tmp/_t1_exp2_c_driver_2026_10_09.py` | `.tmp/_t1_exp2_c_driver_2026_10_09.py` | `whitelist_backup_2026_10_17/_t1_exp2_c_driver_2026_10_09.py` | 2,898 | `5d474b7ceada` | `5d474b7ceada` | `5d474b7ceada` | ✅ |
| 263 | `.tmp/_t1_exp2_c_records.json` | `.tmp/_t1_exp2_c_records.json` | `whitelist_backup_2026_10_17/_t1_exp2_c_records.json` | 6,277,328 | `f53681c7569a` | `f53681c7569a` | `f53681c7569a` | ✅ |
| 264 | `.tmp/_t1_exp2_calib_2026_10_09.json` | `.tmp/_t1_exp2_calib_2026_10_09.json` | `whitelist_backup_2026_10_17/_t1_exp2_calib_2026_10_09.json` | 611 | `de09d4ee3721` | `de09d4ee3721` | `de09d4ee3721` | ✅ |
| 265 | `.tmp/_t1_exp2_d_readings.json` | `.tmp/_t1_exp2_d_readings.json` | `whitelist_backup_2026_10_17/_t1_exp2_d_readings.json` | 3,991 | `2315f6823011` | `2315f6823011` | `2315f6823011` | ✅ |
| 266 | `.tmp/_t1_exp2_d_records.json` | `.tmp/_t1_exp2_d_records.json` | `whitelist_backup_2026_10_17/_t1_exp2_d_records.json` | 488,395 | `aadba0c4f952` | `aadba0c4f952` | `aadba0c4f952` | ✅ |
| 267 | `.tmp/_t1_exp2_probe_log.json` | `.tmp/_t1_exp2_probe_log.json` | `whitelist_backup_2026_10_17/_t1_exp2_probe_log.json` | 760 | `c6478415e2bf` | `c6478415e2bf` | `c6478415e2bf` | ✅ |
| 268 | `.tmp/_t1_exp2_selfcert.json` | `.tmp/_t1_exp2_selfcert.json` | `whitelist_backup_2026_10_17/_t1_exp2_selfcert.json` | 6,780 | `d929eb9ae0b8` | `d929eb9ae0b8` | `d929eb9ae0b8` | ✅ |
| 269 | `.tmp/_t1_gap_domain_sweep_2026_10_01.py` | `.tmp/_t1_gap_domain_sweep_2026_10_01.py` | `whitelist_backup_2026_10_17/_t1_gap_domain_sweep_2026_10_01.py` | 2,502 | `74d1ed439442` | `74d1ed439442` | `74d1ed439442` | ✅ |
| 270 | `.tmp/_t1_gap_implA_2026_10_01.py` | `.tmp/_t1_gap_implA_2026_10_01.py` | `whitelist_backup_2026_10_17/_t1_gap_implA_2026_10_01.py` | 4,468 | `c5d1dc7badcd` | `c5d1dc7badcd` | `c5d1dc7badcd` | ✅ |
| 271 | `.tmp/_t1_gap_implB_2026_10_01.ps1` | `.tmp/_t1_gap_implB_2026_10_01.ps1` | `whitelist_backup_2026_10_17/_t1_gap_implB_2026_10_01.ps1` | 5,735 | `19aebfd44310` | `19aebfd44310` | `19aebfd44310` | ✅ |
| 272 | `.tmp/_t1_gap_postwrite_verify_2026_10_01.py` | `.tmp/_t1_gap_postwrite_verify_2026_10_01.py` | `whitelist_backup_2026_10_17/_t1_gap_postwrite_verify_2026_10_01.py` | 5,666 | `33b4108f14a1` | `33b4108f14a1` | `33b4108f14a1` | ✅ |
| 273 | `.tmp/_t1_gap_snapshot_2026_10_01.py` | `.tmp/_t1_gap_snapshot_2026_10_01.py` | `whitelist_backup_2026_10_17/_t1_gap_snapshot_2026_10_01.py` | 2,588 | `fd53258bd16f` | `fd53258bd16f` | `fd53258bd16f` | ✅ |
| 274 | `.tmp/_t1_qwen_temp_sweep_decomposition.py` | `.tmp/_t1_qwen_temp_sweep_decomposition.py` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_decomposition.py` | 1,981 | `97a6520c7105` | `97a6520c7105` | `97a6520c7105` | ✅ |
| 275 | `.tmp/_t1_qwen_temp_sweep_dump_readings.py` | `.tmp/_t1_qwen_temp_sweep_dump_readings.py` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_dump_readings.py` | 1,137 | `7e06567afc2a` | `7e06567afc2a` | `7e06567afc2a` | ✅ |
| 276 | `.tmp/_t1_qwen_temp_sweep_probe_log.json` | `.tmp/_t1_qwen_temp_sweep_probe_log.json` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_probe_log.json` | 445 | `b5e4151af490` | `b5e4151af490` | `b5e4151af490` | ✅ |
| 277 | `.tmp/_t1_qwen_temp_sweep_r2_probe_log.json` | `.tmp/_t1_qwen_temp_sweep_r2_probe_log.json` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_r2_probe_log.json` | 739 | `5182f6fdd9ef` | `5182f6fdd9ef` | `5182f6fdd9ef` | ✅ |
| 278 | `.tmp/_t1_qwen_temp_sweep_r2_records.json` | `.tmp/_t1_qwen_temp_sweep_r2_records.json` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_r2_records.json` | 1,795,870 | `bb511e7b0baf` | `bb511e7b0baf` | `bb511e7b0baf` | ✅ |
| 279 | `.tmp/_t1_qwen_temp_sweep_r2_selfcert.json` | `.tmp/_t1_qwen_temp_sweep_r2_selfcert.json` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_r2_selfcert.json` | 6,353 | `124051b56295` | `124051b56295` | `124051b56295` | ✅ |
| 280 | `.tmp/_t1_qwen_temp_sweep_readings.json` | `.tmp/_t1_qwen_temp_sweep_readings.json` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_readings.json` | 11,013 | `e5e8f024e42e` | `e5e8f024e42e` | `e5e8f024e42e` | ✅ |
| 281 | `.tmp/_t1_qwen_temp_sweep_records.json` | `.tmp/_t1_qwen_temp_sweep_records.json` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_records.json` | 96,866 | `5b51af62c640` | `5b51af62c640` | `5b51af62c640` | ✅ |
| 282 | `.tmp/_t1_qwen_temp_sweep_selfcert.json` | `.tmp/_t1_qwen_temp_sweep_selfcert.json` | `whitelist_backup_2026_10_17/_t1_qwen_temp_sweep_selfcert.json` | 3,866 | `91c2505deef3` | `91c2505deef3` | `91c2505deef3` | ✅ |
| 283 | `.tmp/_t1_r2_calib_max_tokens_2026_10_09.json` | `.tmp/_t1_r2_calib_max_tokens_2026_10_09.json` | `whitelist_backup_2026_10_17/_t1_r2_calib_max_tokens_2026_10_09.json` | 3,305 | `3f35aede29f6` | `3f35aede29f6` | `3f35aede29f6` | ✅ |
| 284 | `.tmp/_t1_r2_calib_max_tokens_2026_10_09.py` | `.tmp/_t1_r2_calib_max_tokens_2026_10_09.py` | `whitelist_backup_2026_10_17/_t1_r2_calib_max_tokens_2026_10_09.py` | 6,120 | `7bbb0de0c00f` | `7bbb0de0c00f` | `7bbb0de0c00f` | ✅ |
| 285 | `.tmp/_t1_r2_run_driver_2026_10_09.py` | `.tmp/_t1_r2_run_driver_2026_10_09.py` | `whitelist_backup_2026_10_17/_t1_r2_run_driver_2026_10_09.py` | 2,749 | `b71f4916bee1` | `b71f4916bee1` | `b71f4916bee1` | ✅ |
| 286 | `.tmp/_t1_r2_verify_2026_10_09.py` | `.tmp/_t1_r2_verify_2026_10_09.py` | `whitelist_backup_2026_10_17/_t1_r2_verify_2026_10_09.py` | 4,018 | `3ce6d45cfbf7` | `3ce6d45cfbf7` | `3ce6d45cfbf7` | ✅ |
| 287 | `.tmp/_t1_verdict_probe_readonly.txt` | `.tmp/_t1_verdict_probe_readonly.txt` | `whitelist_backup_2026_10_17/_t1_verdict_probe_readonly.txt` | 4,655 | `0e2df9ca7ab2` | `0e2df9ca7ab2` | `0e2df9ca7ab2` | ✅ |
| 288 | `.tmp/_t2_t3_lit_search.py` | `.tmp/_t2_t3_lit_search.py` | `whitelist_backup_2026_10_17/_t2_t3_lit_search.py` | 5,695 | `0829d37e0cd8` | `0829d37e0cd8` | `0829d37e0cd8` | ✅ |
| 289 | `.tmp/_t2_t3_lit_search2.py` | `.tmp/_t2_t3_lit_search2.py` | `whitelist_backup_2026_10_17/_t2_t3_lit_search2.py` | 4,946 | `c0caa8ba29f1` | `c0caa8ba29f1` | `c0caa8ba29f1` | ✅ |
| 290 | `.tmp/_t2_t3_lit_search2_out.json` | `.tmp/_t2_t3_lit_search2_out.json` | `whitelist_backup_2026_10_17/_t2_t3_lit_search2_out.json` | 29,596 | `13ffff0d0b28` | `13ffff0d0b28` | `13ffff0d0b28` | ✅ |
| 291 | `.tmp/_t2_t3_lit_search_out.json` | `.tmp/_t2_t3_lit_search_out.json` | `whitelist_backup_2026_10_17/_t2_t3_lit_search_out.json` | 26,588 | `cc70fac3d81b` | `cc70fac3d81b` | `cc70fac3d81b` | ✅ |
| 292 | `.tmp/_t2_t3_llm_probe.py` | `.tmp/_t2_t3_llm_probe.py` | `whitelist_backup_2026_10_17/_t2_t3_llm_probe.py` | 4,544 | `5561f7af5662` | `5561f7af5662` | `5561f7af5662` | ✅ |
| 293 | `.tmp/_t2_t3_llm_probe_out.json` | `.tmp/_t2_t3_llm_probe_out.json` | `whitelist_backup_2026_10_17/_t2_t3_llm_probe_out.json` | 5,331 | `993477af77db` | `993477af77db` | `993477af77db` | ✅ |
| 294 | `.tmp/_t2_t3_prex_a_route.py` | `.tmp/_t2_t3_prex_a_route.py` | `whitelist_backup_2026_10_17/_t2_t3_prex_a_route.py` | 10,166 | `c25af5d2966b` | `c25af5d2966b` | `c25af5d2966b` | ✅ |
| 295 | `.tmp/_t2_t3_prex_a_route2.py` | `.tmp/_t2_t3_prex_a_route2.py` | `whitelist_backup_2026_10_17/_t2_t3_prex_a_route2.py` | 5,850 | `0c44afba463a` | `0c44afba463a` | `0c44afba463a` | ✅ |
| 296 | `.tmp/_t2_t3_prex_a_route2_out.json` | `.tmp/_t2_t3_prex_a_route2_out.json` | `whitelist_backup_2026_10_17/_t2_t3_prex_a_route2_out.json` | 6,949 | `63f37ba943c1` | `63f37ba943c1` | `63f37ba943c1` | ✅ |
| 297 | `.tmp/_t2_t3_prex_a_route_out.json` | `.tmp/_t2_t3_prex_a_route_out.json` | `whitelist_backup_2026_10_17/_t2_t3_prex_a_route_out.json` | 22,640 | `3cad087a69c3` | `3cad087a69c3` | `3cad087a69c3` | ✅ |
| 298 | `.tmp/_tail3_atomic_landing_check_2026_09_29.py` | `.tmp/_tail3_atomic_landing_check_2026_09_29.py` | `whitelist_backup_2026_10_17/_tail3_atomic_landing_check_2026_09_29.py` | 2,699 | `5c19cf8f29fb` | `5c19cf8f29fb` | `5c19cf8f29fb` | ✅ |
| 299 | `.tmp/_tail3_atomic_make_2026_09_29.py` | `.tmp/_tail3_atomic_make_2026_09_29.py` | `whitelist_backup_2026_10_17/_tail3_atomic_make_2026_09_29.py` | 17,272 | `94d57549533b` | `94d57549533b` | `94d57549533b` | ✅ |
| 300 | `.tmp/_tail3_atomic_refs_2026_09_29.py` | `.tmp/_tail3_atomic_refs_2026_09_29.py` | `whitelist_backup_2026_10_17/_tail3_atomic_refs_2026_09_29.py` | 2,636 | `4e8ea9bea948` | `4e8ea9bea948` | `4e8ea9bea948` | ✅ |
| 301 | `.tmp/_tail3_atomic_verify_2026_09_29.py` | `.tmp/_tail3_atomic_verify_2026_09_29.py` | `whitelist_backup_2026_10_17/_tail3_atomic_verify_2026_09_29.py` | 21,338 | `8d12c9c9cb2d` | `8d12c9c9cb2d` | `8d12c9c9cb2d` | ✅ |
| 302 | `.tmp/_tail_only.py` | `.tmp/_tail_only.py` | `whitelist_backup_2026_10_17/_tail_only.py` | 436 | `cf3bbd24b401` | `cf3bbd24b401` | `cf3bbd24b401` | ✅ |
| 303 | `.tmp/_trae_audit_part1.py` | `.tmp/_trae_audit_part1.py` | `whitelist_backup_2026_10_17/_trae_audit_part1.py` | 5,510 | `ac67b341b56b` | `ac67b341b56b` | `ac67b341b56b` | ✅ |
| 304 | `.tmp/_trae_audit_part2.py` | `.tmp/_trae_audit_part2.py` | `whitelist_backup_2026_10_17/_trae_audit_part2.py` | 3,632 | `9faaa564c3bc` | `9faaa564c3bc` | `9faaa564c3bc` | ✅ |
| 305 | `.tmp/_trae_audit_part3.py` | `.tmp/_trae_audit_part3.py` | `whitelist_backup_2026_10_17/_trae_audit_part3.py` | 8,617 | `f4c994004311` | `f4c994004311` | `f4c994004311` | ✅ |
| 306 | `.tmp/_trae_audit_part3b.py` | `.tmp/_trae_audit_part3b.py` | `whitelist_backup_2026_10_17/_trae_audit_part3b.py` | 7,662 | `c1a9a6c3c17a` | `c1a9a6c3c17a` | `c1a9a6c3c17a` | ✅ |
| 307 | `.tmp/_trae_audit_part4.py` | `.tmp/_trae_audit_part4.py` | `whitelist_backup_2026_10_17/_trae_audit_part4.py` | 7,173 | `bc8d4721bf3b` | `bc8d4721bf3b` | `bc8d4721bf3b` | ✅ |
| 308 | `.tmp/_v412_contrib.py` | `.tmp/_v412_contrib.py` | `whitelist_backup_2026_10_17/_v412_contrib.py` | 1,040 | `1085411b4896` | `1085411b4896` | `1085411b4896` | ✅ |
| 309 | `.tmp/_v412_material_scan.py` | `.tmp/_v412_material_scan.py` | `whitelist_backup_2026_10_17/_v412_material_scan.py` | 627 | `f3493907cbe2` | `f3493907cbe2` | `f3493907cbe2` | ✅ |
| 310 | `.tmp/_v412_unique_scan.py` | `.tmp/_v412_unique_scan.py` | `whitelist_backup_2026_10_17/_v412_unique_scan.py` | 1,300 | `b2e381f09828` | `b2e381f09828` | `b2e381f09828` | ✅ |
| 311 | `.tmp/_v5_c5_b_clause4_consistency_check.py` | `.tmp/_v5_c5_b_clause4_consistency_check.py` | `whitelist_backup_2026_10_17/_v5_c5_b_clause4_consistency_check.py` | 6,528 | `56ad3329a3c7` | `56ad3329a3c7` | `56ad3329a3c7` | ✅ |
| 312 | `.tmp/_v5_c5_b_fetch_raw_embeddings.py` | `.tmp/_v5_c5_b_fetch_raw_embeddings.py` | `whitelist_backup_2026_10_17/_v5_c5_b_fetch_raw_embeddings.py` | 9,476 | `8e4f2ae63de3` | `8e4f2ae63de3` | `8e4f2ae63de3` | ✅ |
| 313 | `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` | `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` | `whitelist_backup_2026_10_17/_v5_c5_b_fix_readings_2026_10_01.py` | 12,014 | `191efa7fe0b6` | `191efa7fe0b6` | `191efa7fe0b6` | ✅ |
| 314 | `.tmp/_v5_item21_anchor_driver.py` | `.tmp/_v5_item21_anchor_driver.py` | `whitelist_backup_2026_10_17/_v5_item21_anchor_driver.py` | 5,401 | `cb14f672dd1e` | `cb14f672dd1e` | `cb14f672dd1e` | ✅ |
| 315 | `.tmp/_v5_item21_patched_b1_semA_none_default.py` | `.tmp/_v5_item21_patched_b1_semA_none_default.py` | `whitelist_backup_2026_10_17/_v5_item21_patched_b1_semA_none_default.py` | 16,768 | `ceb33de660fd` | `ceb33de660fd` | `ceb33de660fd` | ✅ |
| 316 | `.tmp/_v5_item21_patched_b1_semB_none_skip.py` | `.tmp/_v5_item21_patched_b1_semB_none_skip.py` | `whitelist_backup_2026_10_17/_v5_item21_patched_b1_semB_none_skip.py` | 16,829 | `be0208abaffa` | `be0208abaffa` | `be0208abaffa` | ✅ |
| 317 | `.tmp/_v5_item21_patched_b2_semA_none_default.py` | `.tmp/_v5_item21_patched_b2_semA_none_default.py` | `whitelist_backup_2026_10_17/_v5_item21_patched_b2_semA_none_default.py` | 16,036 | `801ee31e8bdc` | `801ee31e8bdc` | `801ee31e8bdc` | ✅ |
| 318 | `.tmp/_v5_item21_patched_b2_semB_none_skip.py` | `.tmp/_v5_item21_patched_b2_semB_none_skip.py` | `whitelist_backup_2026_10_17/_v5_item21_patched_b2_semB_none_skip.py` | 16,097 | `8293535673dc` | `8293535673dc` | `8293535673dc` | ✅ |
| 319 | `.tmp/_v5_item21_patched_b3_semA_none_default.py` | `.tmp/_v5_item21_patched_b3_semA_none_default.py` | `whitelist_backup_2026_10_17/_v5_item21_patched_b3_semA_none_default.py` | 15,778 | `9d8a4a875b62` | `9d8a4a875b62` | `9d8a4a875b62` | ✅ |
| 320 | `.tmp/_v5_item21_patched_b3_semB_none_skip.py` | `.tmp/_v5_item21_patched_b3_semB_none_skip.py` | `whitelist_backup_2026_10_17/_v5_item21_patched_b3_semB_none_skip.py` | 15,839 | `8df8e94724ff` | `8df8e94724ff` | `8df8e94724ff` | ✅ |
| 321 | `.tmp/_v5_loadcorpus_verify_2026_09_29.py` | `.tmp/_v5_loadcorpus_verify_2026_09_29.py` | `whitelist_backup_2026_10_17/_v5_loadcorpus_verify_2026_09_29.py` | 8,798 | `564e3575ab1d` | `564e3575ab1d` | `564e3575ab1d` | ✅ |
| 322 | `.tmp/_v5_qwen_retry_candidates_20260929.py` | `.tmp/_v5_qwen_retry_candidates_20260929.py` | `whitelist_backup_2026_10_17/_v5_qwen_retry_candidates_20260929.py` | 1,689 | `f42600827cc3` | `f42600827cc3` | `f42600827cc3` | ✅ |
| 323 | `.tmp/_v5_qwen_retry_introspect_20260929.py` | `.tmp/_v5_qwen_retry_introspect_20260929.py` | `whitelist_backup_2026_10_17/_v5_qwen_retry_introspect_20260929.py` | 3,149 | `117b64fc1d5b` | `117b64fc1d5b` | `117b64fc1d5b` | ✅ |
| 324 | `.tmp/_verdict_keeper_sha_helper.ps1` | `.tmp/_verdict_keeper_sha_helper.ps1` | `whitelist_backup_2026_10_17/_verdict_keeper_sha_helper.ps1` | 679 | `bc11b03d3b84` | `bc11b03d3b84` | `bc11b03d3b84` | ✅ |
| 325 | `.tmp/_verify_d8_addendum_2026_09_30.py` | `.tmp/_verify_d8_addendum_2026_09_30.py` | `whitelist_backup_2026_10_17/_verify_d8_addendum_2026_09_30.py` | 4,900 | `28de8c99c054` | `28de8c99c054` | `28de8c99c054` | ✅ |
| 326 | `.tmp/_verify_intake_supplement_6.py` | `.tmp/_verify_intake_supplement_6.py` | `whitelist_backup_2026_10_17/_verify_intake_supplement_6.py` | 3,678 | `1fbb1bd1db6c` | `1fbb1bd1db6c` | `1fbb1bd1db6c` | ✅ |
| 327 | `.tmp/_verify_r32_card_2026_10_10.py` | `.tmp/_verify_r32_card_2026_10_10.py` | `whitelist_backup_2026_10_17/_verify_r32_card_2026_10_10.py` | 631 | `61f99fc5fdb9` | `61f99fc5fdb9` | `61f99fc5fdb9` | ✅ |
| 328 | `.tmp/_verify_tail.py` | `.tmp/_verify_tail.py` | `whitelist_backup_2026_10_17/_verify_tail.py` | 733 | `23198a6a0a9b` | `23198a6a0a9b` | `23198a6a0a9b` | ✅ |
| 329 | `.tmp/_verify_two_pieces_2026_09_30.py` | `.tmp/_verify_two_pieces_2026_09_30.py` | `whitelist_backup_2026_10_17/_verify_two_pieces_2026_09_30.py` | 4,739 | `509afa876df0` | `509afa876df0` | `509afa876df0` | ✅ |
| 330 | `.tmp/_vk_pv02_recheck_a.py` | `.tmp/_vk_pv02_recheck_a.py` | `whitelist_backup_2026_10_17/_vk_pv02_recheck_a.py` | 4,188 | `37d55bf0fba6` | `37d55bf0fba6` | `37d55bf0fba6` | ✅ |
| 331 | `.tmp/_vk_pv02_recheck_b.py` | `.tmp/_vk_pv02_recheck_b.py` | `whitelist_backup_2026_10_17/_vk_pv02_recheck_b.py` | 1,646 | `fe0f10e38bb3` | `fe0f10e38bb3` | `fe0f10e38bb3` | ✅ |
| 332 | `.tmp/_vk_pv02_recheck_c.py` | `.tmp/_vk_pv02_recheck_c.py` | `whitelist_backup_2026_10_17/_vk_pv02_recheck_c.py` | 2,397 | `7d35b715f8e2` | `7d35b715f8e2` | `7d35b715f8e2` | ✅ |
| 333 | `.tmp/_vk_pv02_recheck_d.py` | `.tmp/_vk_pv02_recheck_d.py` | `whitelist_backup_2026_10_17/_vk_pv02_recheck_d.py` | 982 | `7ae7ed6bcd8a` | `7ae7ed6bcd8a` | `7ae7ed6bcd8a` | ✅ |
| 334 | `.tmp/_vk_pv02_recheck_e.py` | `.tmp/_vk_pv02_recheck_e.py` | `whitelist_backup_2026_10_17/_vk_pv02_recheck_e.py` | 1,742 | `d925e60c1d3c` | `d925e60c1d3c` | `d925e60c1d3c` | ✅ |
| 335 | `.tmp/_vk_pv02_recheck_f.py` | `.tmp/_vk_pv02_recheck_f.py` | `whitelist_backup_2026_10_17/_vk_pv02_recheck_f.py` | 1,522 | `c2e298ccebc6` | `c2e298ccebc6` | `c2e298ccebc6` | ✅ |
| 336 | `.tmp/_vk_pv02_recheck_g.py` | `.tmp/_vk_pv02_recheck_g.py` | `whitelist_backup_2026_10_17/_vk_pv02_recheck_g.py` | 2,269 | `f237e1d2715f` | `f237e1d2715f` | `f237e1d2715f` | ✅ |
| 337 | `.tmp/_vk_q.py` | `.tmp/_vk_q.py` | `whitelist_backup_2026_10_17/_vk_q.py` | 519 | `67364902116c` | `67364902116c` | `67364902116c` | ✅ |
| 338 | `.tmp/_vk_q2.py` | `.tmp/_vk_q2.py` | `whitelist_backup_2026_10_17/_vk_q2.py` | 540 | `d5759d40dc43` | `d5759d40dc43` | `d5759d40dc43` | ✅ |
| 339 | `.tmp/_vk_q3.py` | `.tmp/_vk_q3.py` | `whitelist_backup_2026_10_17/_vk_q3.py` | 612 | `a00cd309205f` | `a00cd309205f` | `a00cd309205f` | ✅ |
| 340 | `.tmp/_vk_q4.py` | `.tmp/_vk_q4.py` | `whitelist_backup_2026_10_17/_vk_q4.py` | 784 | `defc3c53b7df` | `defc3c53b7df` | `defc3c53b7df` | ✅ |
| 341 | `.tmp/_vk_q5.py` | `.tmp/_vk_q5.py` | `whitelist_backup_2026_10_17/_vk_q5.py` | 1,246 | `7b95307225ba` | `7b95307225ba` | `7b95307225ba` | ✅ |
| 342 | `.tmp/_vk_q6.py` | `.tmp/_vk_q6.py` | `whitelist_backup_2026_10_17/_vk_q6.py` | 811 | `7da34dd24eb0` | `7da34dd24eb0` | `7da34dd24eb0` | ✅ |
| 343 | `.tmp/_vk_q7.py` | `.tmp/_vk_q7.py` | `whitelist_backup_2026_10_17/_vk_q7.py` | 1,331 | `a6c525f88f11` | `a6c525f88f11` | `a6c525f88f11` | ✅ |
| 344 | `.tmp/_vk_q8.py` | `.tmp/_vk_q8.py` | `whitelist_backup_2026_10_17/_vk_q8.py` | 1,025 | `5a81e5558c72` | `5a81e5558c72` | `5a81e5558c72` | ✅ |
| 345 | `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.py` | `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.py` | `whitelist_backup_2026_10_17/_vk_s4_topup_intake_recheck_2026_10_09.py` | 6,678 | `a1d8047f1833` | `a1d8047f1833` | `a1d8047f1833` | ✅ |
| 346 | `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.txt` | `.tmp/_vk_s4_topup_intake_recheck_2026_10_09.txt` | `whitelist_backup_2026_10_17/_vk_s4_topup_intake_recheck_2026_10_09.txt` | 7,098 | `683501b8fb41` | `683501b8fb41` | `683501b8fb41` | ✅ |
| 347 | `.tmp/_w1_collect.py` | `.tmp/_w1_collect.py` | `whitelist_backup_2026_10_17/_w1_collect.py` | 19,559 | `7c3155b2c370` | `7c3155b2c370` | `7c3155b2c370` | ✅ |
| 348 | `.tmp/_w1_drift_write.py` | `.tmp/_w1_drift_write.py` | `whitelist_backup_2026_10_17/_w1_drift_write.py` | 16,560 | `44e026ae190d` | `44e026ae190d` | `44e026ae190d` | ✅ |
| 349 | `.tmp/_w1_freeze_write.py` | `.tmp/_w1_freeze_write.py` | `whitelist_backup_2026_10_17/_w1_freeze_write.py` | 24,351 | `97211806b0d0` | `97211806b0d0` | `97211806b0d0` | ✅ |
| 350 | `.tmp/_w1_phaseB_write.py` | `.tmp/_w1_phaseB_write.py` | `whitelist_backup_2026_10_17/_w1_phaseB_write.py` | 31,303 | `4e85afe94966` | `4e85afe94966` | `4e85afe94966` | ✅ |
| 351 | `.tmp/_w1_verify_final.py` | `.tmp/_w1_verify_final.py` | `whitelist_backup_2026_10_17/_w1_verify_final.py` | 7,944 | `040c35e21bf2` | `040c35e21bf2` | `040c35e21bf2` | ✅ |
| 352 | `.tmp/_w5_9model_merge_2026_10_09.py` | `.tmp/_w5_9model_merge_2026_10_09.py` | `whitelist_backup_2026_10_17/_w5_9model_merge_2026_10_09.py` | 18,475 | `afa52e90f332` | `afa52e90f332` | `afa52e90f332` | ✅ |
| 353 | `.tmp/_worker_write_ge01_unblock_progress.py` | `.tmp/_worker_write_ge01_unblock_progress.py` | `whitelist_backup_2026_10_17/_worker_write_ge01_unblock_progress.py` | 26,125 | `7c18f854316c` | `7c18f854316c` | `7c18f854316c` | ✅ |
| 354 | `.tmp/_write_canonical_register.py` | `.tmp/_write_canonical_register.py` | `whitelist_backup_2026_10_17/_write_canonical_register.py` | 24,636 | `867acc46aff9` | `867acc46aff9` | `867acc46aff9` | ✅ |
| 355 | `.tmp/_write_eps_grid_design.py` | `.tmp/_write_eps_grid_design.py` | `whitelist_backup_2026_10_17/_write_eps_grid_design.py` | 38,246 | `df37b02f1c0f` | `df37b02f1c0f` | `df37b02f1c0f` | ✅ |
| 356 | `.tmp/_write_predelete_caliber_draft.py` | `.tmp/_write_predelete_caliber_draft.py` | `whitelist_backup_2026_10_17/_write_predelete_caliber_draft.py` | 32,826 | `82d7f9c628b6` | `82d7f9c628b6` | `82d7f9c628b6` | ✅ |
| 357 | `.tmp/anch.py` | `.tmp/anch.py` | `whitelist_backup_2026_10_17/anch.py` | 1,484 | `c05693efbb30` | `c05693efbb30` | `c05693efbb30` | ✅ |
| 358 | `.tmp/anch_v4_build.py` | `.tmp/anch_v4_build.py` | `whitelist_backup_2026_10_17/anch_v4_build.py` | 7,175 | `adcae459701a` | `adcae459701a` | `adcae459701a` | ✅ |
| 359 | `.tmp/anch_v4_build_measurements.json` | `.tmp/anch_v4_build_measurements.json` | `whitelist_backup_2026_10_17/anch_v4_build_measurements.json` | 2,315 | `5708226b943f` | `5708226b943f` | `5708226b943f` | ✅ |
| 360 | `.tmp/anch_v4_probe.py` | `.tmp/anch_v4_probe.py` | `whitelist_backup_2026_10_17/anch_v4_probe.py` | 2,662 | `f47af093e3aa` | `f47af093e3aa` | `f47af093e3aa` | ✅ |
| 361 | `.tmp/archive_survey_census2.py` | `.tmp/archive_survey_census2.py` | `whitelist_backup_2026_10_17/archive_survey_census2.py` | 780 | `2863f5edca41` | `2863f5edca41` | `2863f5edca41` | ✅ |
| 362 | `.tmp/body_relabel.md` | `.tmp/body_relabel.md` | `whitelist_backup_2026_10_17/body_relabel.md` | 8,672 | `2660d5ea717d` | `2660d5ea717d` | `2660d5ea717d` | ✅ |
| 363 | `.tmp/body_v6_effect.md` | `.tmp/body_v6_effect.md` | `whitelist_backup_2026_10_17/body_v6_effect.md` | 15,467 | `d79637fee0ef` | `d79637fee0ef` | `d79637fee0ef` | ✅ |
| 364 | `.tmp/claude_spotcheck.py` | `.tmp/claude_spotcheck.py` | `whitelist_backup_2026_10_17/claude_spotcheck.py` | 4,136 | `a78755b356b9` | `a78755b356b9` | `a78755b356b9` | ✅ |
| 365 | `.tmp/cleanup511_manifest_2026_10_17.json` | `.tmp/cleanup511_manifest_2026_10_17.json` | `whitelist_backup_2026_10_17/cleanup511_manifest_2026_10_17.json` | 1,754,609 | `b7093a701856` | `b7093a701856` | `b7093a701856` | ✅ |
| 366 | `.tmp/collision_survey_hashes.json` | `.tmp/collision_survey_hashes.json` | `whitelist_backup_2026_10_17/collision_survey_hashes.json` | 75,439 | `0329afb1e9fc` | `0329afb1e9fc` | `0329afb1e9fc` | ✅ |
| 367 | `.tmp/collision_survey_inventory.json` | `.tmp/collision_survey_inventory.json` | `whitelist_backup_2026_10_17/collision_survey_inventory.json` | 37,588 | `a4cd5b2fc5c8` | `a4cd5b2fc5c8` | `a4cd5b2fc5c8` | ✅ |
| 368 | `.tmp/combo_llm_calls_2026_10_16.jsonl` | `.tmp/combo_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/combo_llm_calls_2026_10_16.jsonl` | 59,626 | `86f05646031b` | `86f05646031b` | `86f05646031b` | ✅ |
| 369 | `.tmp/combo_measurement_2026_10_16.json` | `.tmp/combo_measurement_2026_10_16.json` | `whitelist_backup_2026_10_17/combo_measurement_2026_10_16.json` | 121,779 | `27609799e40e` | `27609799e40e` | `27609799e40e` | ✅ |
| 370 | `.tmp/d05_hash_index.py` | `.tmp/d05_hash_index.py` | `whitelist_backup_2026_10_17/d05_hash_index.py` | 1,004 | `070b6f865eba` | `070b6f865eba` | `070b6f865eba` | ✅ |
| 371 | `.tmp/d1fill_anchor_snapshot.py` | `.tmp/d1fill_anchor_snapshot.py` | `whitelist_backup_2026_10_17/d1fill_anchor_snapshot.py` | 1,985 | `15c0b0ade7ab` | `15c0b0ade7ab` | `15c0b0ade7ab` | ✅ |
| 372 | `.tmp/d1fill_recount_checks.py` | `.tmp/d1fill_recount_checks.py` | `whitelist_backup_2026_10_17/d1fill_recount_checks.py` | 2,336 | `b8af087b5e1f` | `b8af087b5e1f` | `b8af087b5e1f` | ✅ |
| 373 | `.tmp/d1fill_recount_impl1.py` | `.tmp/d1fill_recount_impl1.py` | `whitelist_backup_2026_10_17/d1fill_recount_impl1.py` | 6,464 | `bb30ad15c89b` | `bb30ad15c89b` | `bb30ad15c89b` | ✅ |
| 374 | `.tmp/d1fill_recount_impl2.ps1` | `.tmp/d1fill_recount_impl2.ps1` | `whitelist_backup_2026_10_17/d1fill_recount_impl2.ps1` | 6,132 | `88411408e671` | `88411408e671` | `88411408e671` | ✅ |
| 375 | `.tmp/diag.py` | `.tmp/diag.py` | `whitelist_backup_2026_10_17/diag.py` | 972 | `db20dd0e6efb` | `db20dd0e6efb` | `db20dd0e6efb` | ✅ |
| 376 | `.tmp/diffcause.py` | `.tmp/diffcause.py` | `whitelist_backup_2026_10_17/diffcause.py` | 2,724 | `2b24513cdf74` | `2b24513cdf74` | `2b24513cdf74` | ✅ |
| 377 | `.tmp/docwriter_c2_effect_census.json` | `.tmp/docwriter_c2_effect_census.json` | `whitelist_backup_2026_10_17/docwriter_c2_effect_census.json` | 36,157 | `1ef99b1da14d` | `1ef99b1da14d` | `1ef99b1da14d` | ✅ |
| 378 | `.tmp/docwriter_c2_effect_census.py` | `.tmp/docwriter_c2_effect_census.py` | `whitelist_backup_2026_10_17/docwriter_c2_effect_census.py` | 5,518 | `a8e52d7e9f8d` | `a8e52d7e9f8d` | `a8e52d7e9f8d` | ✅ |
| 379 | `.tmp/docwriter_c2_effect_table.py` | `.tmp/docwriter_c2_effect_table.py` | `whitelist_backup_2026_10_17/docwriter_c2_effect_table.py` | 1,400 | `503230d1e7e3` | `503230d1e7e3` | `503230d1e7e3` | ✅ |
| 380 | `.tmp/docwriter_c2_effect_table.txt` | `.tmp/docwriter_c2_effect_table.txt` | `whitelist_backup_2026_10_17/docwriter_c2_effect_table.txt` | 21,554 | `1b5382cc9936` | `1b5382cc9936` | `1b5382cc9936` | ✅ |
| 381 | `.tmp/docwriter_sigsup.py` | `.tmp/docwriter_sigsup.py` | `whitelist_backup_2026_10_17/docwriter_sigsup.py` | 13,645 | `d116fefd336c` | `d116fefd336c` | `d116fefd336c` | ✅ |
| 382 | `.tmp/docwriter_v41_probe.py` | `.tmp/docwriter_v41_probe.py` | `whitelist_backup_2026_10_17/docwriter_v41_probe.py` | 6,503 | `210a07303fe7` | `210a07303fe7` | `210a07303fe7` | ✅ |
| 383 | `.tmp/docwriter_v41_scan2.json` | `.tmp/docwriter_v41_scan2.json` | `whitelist_backup_2026_10_17/docwriter_v41_scan2.json` | 4,066 | `e988b26ba229` | `e988b26ba229` | `e988b26ba229` | ✅ |
| 384 | `.tmp/docwriter_v41_scan2.py` | `.tmp/docwriter_v41_scan2.py` | `whitelist_backup_2026_10_17/docwriter_v41_scan2.py` | 3,661 | `e88316a0fc2c` | `e88316a0fc2c` | `e88316a0fc2c` | ✅ |
| 385 | `.tmp/docwriter_v42_scan.py` | `.tmp/docwriter_v42_scan.py` | `whitelist_backup_2026_10_17/docwriter_v42_scan.py` | 4,601 | `93d9c4c5c927` | `93d9c4c5c927` | `93d9c4c5c927` | ✅ |
| 386 | `.tmp/docwriter_v42_scan_out.txt` | `.tmp/docwriter_v42_scan_out.txt` | `whitelist_backup_2026_10_17/docwriter_v42_scan_out.txt` | 5,267 | `d1470a9eaea9` | `d1470a9eaea9` | `d1470a9eaea9` | ✅ |
| 387 | `.tmp/docwriter_v42_verify.py` | `.tmp/docwriter_v42_verify.py` | `whitelist_backup_2026_10_17/docwriter_v42_verify.py` | 4,858 | `47c794a64dff` | `47c794a64dff` | `47c794a64dff` | ✅ |
| 388 | `.tmp/docwriter_v42_verify_out.txt` | `.tmp/docwriter_v42_verify_out.txt` | `whitelist_backup_2026_10_17/docwriter_v42_verify_out.txt` | 2,899 | `c38b853adda1` | `c38b853adda1` | `c38b853adda1` | ✅ |
| 389 | `.tmp/docwriter_v43_fp.py` | `.tmp/docwriter_v43_fp.py` | `whitelist_backup_2026_10_17/docwriter_v43_fp.py` | 1,488 | `000c7e036d9c` | `000c7e036d9c` | `000c7e036d9c` | ✅ |
| 390 | `.tmp/docwriter_v43_fp2.py` | `.tmp/docwriter_v43_fp2.py` | `whitelist_backup_2026_10_17/docwriter_v43_fp2.py` | 1,716 | `87ef5d8aba15` | `87ef5d8aba15` | `87ef5d8aba15` | ✅ |
| 391 | `.tmp/docwriter_v43_fp_out.txt` | `.tmp/docwriter_v43_fp_out.txt` | `whitelist_backup_2026_10_17/docwriter_v43_fp_out.txt` | 2,420 | `35a223091bbe` | `35a223091bbe` | `35a223091bbe` | ✅ |
| 392 | `.tmp/docwriter_v43_scan.py` | `.tmp/docwriter_v43_scan.py` | `whitelist_backup_2026_10_17/docwriter_v43_scan.py` | 2,061 | `5356708d6a6f` | `5356708d6a6f` | `5356708d6a6f` | ✅ |
| 393 | `.tmp/docwriter_v43_scan_out.txt` | `.tmp/docwriter_v43_scan_out.txt` | `whitelist_backup_2026_10_17/docwriter_v43_scan_out.txt` | 2,353 | `c80e849e7c99` | `c80e849e7c99` | `c80e849e7c99` | ✅ |
| 394 | `.tmp/docwriter_v43_verify.py` | `.tmp/docwriter_v43_verify.py` | `whitelist_backup_2026_10_17/docwriter_v43_verify.py` | 4,497 | `2cf26203f12d` | `2cf26203f12d` | `2cf26203f12d` | ✅ |
| 395 | `.tmp/docwriter_v43_verify_out.txt` | `.tmp/docwriter_v43_verify_out.txt` | `whitelist_backup_2026_10_17/docwriter_v43_verify_out.txt` | 759 | `c1d14e3d7e06` | `c1d14e3d7e06` | `c1d14e3d7e06` | ✅ |
| 396 | `.tmp/docwriter_v44_fp.py` | `.tmp/docwriter_v44_fp.py` | `whitelist_backup_2026_10_17/docwriter_v44_fp.py` | 2,485 | `4c2e2a4a2ad2` | `4c2e2a4a2ad2` | `4c2e2a4a2ad2` | ✅ |
| 397 | `.tmp/docwriter_v44_fp_out.txt` | `.tmp/docwriter_v44_fp_out.txt` | `whitelist_backup_2026_10_17/docwriter_v44_fp_out.txt` | 1,601 | `6ab1382d766e` | `6ab1382d766e` | `6ab1382d766e` | ✅ |
| 398 | `.tmp/docwriter_v44_fresh.py` | `.tmp/docwriter_v44_fresh.py` | `whitelist_backup_2026_10_17/docwriter_v44_fresh.py` | 2,319 | `855298e666f6` | `855298e666f6` | `855298e666f6` | ✅ |
| 399 | `.tmp/docwriter_v44_fresh_out.txt` | `.tmp/docwriter_v44_fresh_out.txt` | `whitelist_backup_2026_10_17/docwriter_v44_fresh_out.txt` | 1,646 | `6d7d8ad5c4ed` | `6d7d8ad5c4ed` | `6d7d8ad5c4ed` | ✅ |
| 400 | `.tmp/docwriter_v44_scan.py` | `.tmp/docwriter_v44_scan.py` | `whitelist_backup_2026_10_17/docwriter_v44_scan.py` | 3,822 | `3cc9fa3130a4` | `3cc9fa3130a4` | `3cc9fa3130a4` | ✅ |
| 401 | `.tmp/docwriter_v44_scan_out.txt` | `.tmp/docwriter_v44_scan_out.txt` | `whitelist_backup_2026_10_17/docwriter_v44_scan_out.txt` | 2,290 | `24663bc22391` | `24663bc22391` | `24663bc22391` | ✅ |
| 402 | `.tmp/docwriter_v45_scan.py` | `.tmp/docwriter_v45_scan.py` | `whitelist_backup_2026_10_17/docwriter_v45_scan.py` | 5,186 | `c6703629a7b0` | `c6703629a7b0` | `c6703629a7b0` | ✅ |
| 403 | `.tmp/docwriter_v45_scan_out.txt` | `.tmp/docwriter_v45_scan_out.txt` | `whitelist_backup_2026_10_17/docwriter_v45_scan_out.txt` | 1,661 | `28c06dd53ae4` | `28c06dd53ae4` | `28c06dd53ae4` | ✅ |
| 404 | `.tmp/docwriter_v45_scan_out_r1.txt` | `.tmp/docwriter_v45_scan_out_r1.txt` | `whitelist_backup_2026_10_17/docwriter_v45_scan_out_r1.txt` | 1,661 | `28c06dd53ae4` | `28c06dd53ae4` | `28c06dd53ae4` | ✅ |
| 405 | `.tmp/docwriter_v45_scan_out_r2.txt` | `.tmp/docwriter_v45_scan_out_r2.txt` | `whitelist_backup_2026_10_17/docwriter_v45_scan_out_r2.txt` | 1,728 | `ef49039e5d90` | `ef49039e5d90` | `ef49039e5d90` | ✅ |
| 406 | `.tmp/docwriter_v45_scan_r2.py` | `.tmp/docwriter_v45_scan_r2.py` | `whitelist_backup_2026_10_17/docwriter_v45_scan_r2.py` | 4,212 | `189764eebc91` | `189764eebc91` | `189764eebc91` | ✅ |
| 407 | `.tmp/docwriter_v45_verify_out.txt` | `.tmp/docwriter_v45_verify_out.txt` | `whitelist_backup_2026_10_17/docwriter_v45_verify_out.txt` | 2,031 | `e5a0fdfbc914` | `e5a0fdfbc914` | `e5a0fdfbc914` | ✅ |
| 408 | `.tmp/docwriter_v46_card_raw.py` | `.tmp/docwriter_v46_card_raw.py` | `whitelist_backup_2026_10_17/docwriter_v46_card_raw.py` | 1,652 | `b8754c12612b` | `b8754c12612b` | `b8754c12612b` | ✅ |
| 409 | `.tmp/docwriter_v46_card_raw.txt` | `.tmp/docwriter_v46_card_raw.txt` | `whitelist_backup_2026_10_17/docwriter_v46_card_raw.txt` | 26 | `e31064337198` | `e31064337198` | `e31064337198` | ✅ |
| 410 | `.tmp/docwriter_v46_probe.py` | `.tmp/docwriter_v46_probe.py` | `whitelist_backup_2026_10_17/docwriter_v46_probe.py` | 8,174 | `15d2a2cef38c` | `15d2a2cef38c` | `15d2a2cef38c` | ✅ |
| 411 | `.tmp/docwriter_v46_probe_out.txt` | `.tmp/docwriter_v46_probe_out.txt` | `whitelist_backup_2026_10_17/docwriter_v46_probe_out.txt` | 10,158 | `45358bad9e37` | `45358bad9e37` | `45358bad9e37` | ✅ |
| 412 | `.tmp/docwriter_v46_timeshift_out.txt` | `.tmp/docwriter_v46_timeshift_out.txt` | `whitelist_backup_2026_10_17/docwriter_v46_timeshift_out.txt` | 708 | `4623d2f470da` | `4623d2f470da` | `4623d2f470da` | ✅ |
| 413 | `.tmp/docwriter_v46_verify.py` | `.tmp/docwriter_v46_verify.py` | `whitelist_backup_2026_10_17/docwriter_v46_verify.py` | 6,883 | `7d657b923cf3` | `7d657b923cf3` | `7d657b923cf3` | ✅ |
| 414 | `.tmp/docwriter_v46_verify_r2.py` | `.tmp/docwriter_v46_verify_r2.py` | `whitelist_backup_2026_10_17/docwriter_v46_verify_r2.py` | 3,940 | `98878b701653` | `98878b701653` | `98878b701653` | ✅ |
| 415 | `.tmp/docwriter_v47_verify.py` | `.tmp/docwriter_v47_verify.py` | `whitelist_backup_2026_10_17/docwriter_v47_verify.py` | 1,220 | `9383724baaa4` | `9383724baaa4` | `9383724baaa4` | ✅ |
| 416 | `.tmp/docwriter_v47_write1.py` | `.tmp/docwriter_v47_write1.py` | `whitelist_backup_2026_10_17/docwriter_v47_write1.py` | 62,466 | `8fa8d72c3a69` | `8fa8d72c3a69` | `8fa8d72c3a69` | ✅ |
| 417 | `.tmp/docwriter_v47_write2.py` | `.tmp/docwriter_v47_write2.py` | `whitelist_backup_2026_10_17/docwriter_v47_write2.py` | 48,627 | `1ee1ee14ac3e` | `1ee1ee14ac3e` | `1ee1ee14ac3e` | ✅ |
| 418 | `.tmp/docwriter_v48_norm.py` | `.tmp/docwriter_v48_norm.py` | `whitelist_backup_2026_10_17/docwriter_v48_norm.py` | 12,880 | `e39ea2ab2756` | `e39ea2ab2756` | `e39ea2ab2756` | ✅ |
| 419 | `.tmp/docwriter_v48_probe.py` | `.tmp/docwriter_v48_probe.py` | `whitelist_backup_2026_10_17/docwriter_v48_probe.py` | 4,448 | `8dfd0f40cdb5` | `8dfd0f40cdb5` | `8dfd0f40cdb5` | ✅ |
| 420 | `.tmp/docwriter_v48_probe_out.txt` | `.tmp/docwriter_v48_probe_out.txt` | `whitelist_backup_2026_10_17/docwriter_v48_probe_out.txt` | 4,169 | `48b1c4a81ad4` | `48b1c4a81ad4` | `48b1c4a81ad4` | ✅ |
| 421 | `.tmp/docwriter_v49_norm.py` | `.tmp/docwriter_v49_norm.py` | `whitelist_backup_2026_10_17/docwriter_v49_norm.py` | 16,740 | `d1b3481335eb` | `d1b3481335eb` | `d1b3481335eb` | ✅ |
| 422 | `.tmp/docwriter_v49_probe.py` | `.tmp/docwriter_v49_probe.py` | `whitelist_backup_2026_10_17/docwriter_v49_probe.py` | 4,806 | `753b0ad48557` | `753b0ad48557` | `753b0ad48557` | ✅ |
| 423 | `.tmp/docwriter_v49_probe_out.txt` | `.tmp/docwriter_v49_probe_out.txt` | `whitelist_backup_2026_10_17/docwriter_v49_probe_out.txt` | 4,353 | `c04bcaf87623` | `c04bcaf87623` | `c04bcaf87623` | ✅ |
| 424 | `.tmp/docwriter_verify_v44.py` | `.tmp/docwriter_verify_v44.py` | `whitelist_backup_2026_10_17/docwriter_verify_v44.py` | 4,692 | `19cfb64700a1` | `19cfb64700a1` | `19cfb64700a1` | ✅ |
| 425 | `.tmp/docwriter_verify_v44_out.txt` | `.tmp/docwriter_verify_v44_out.txt` | `whitelist_backup_2026_10_17/docwriter_verify_v44_out.txt` | 2,371 | `f3d33d095a8a` | `f3d33d095a8a` | `f3d33d095a8a` | ✅ |
| 426 | `.tmp/docwriter_verify_v45.py` | `.tmp/docwriter_verify_v45.py` | `whitelist_backup_2026_10_17/docwriter_verify_v45.py` | 3,780 | `92230e228d83` | `92230e228d83` | `92230e228d83` | ✅ |
| 427 | `.tmp/docwriter_write_effect_v43.py` | `.tmp/docwriter_write_effect_v43.py` | `whitelist_backup_2026_10_17/docwriter_write_effect_v43.py` | 27,715 | `01098529c399` | `01098529c399` | `01098529c399` | ✅ |
| 428 | `.tmp/docwriter_write_v42.py` | `.tmp/docwriter_write_v42.py` | `whitelist_backup_2026_10_17/docwriter_write_v42.py` | 66,543 | `5cc438f6338d` | `5cc438f6338d` | `5cc438f6338d` | ✅ |
| 429 | `.tmp/docwriter_write_v43.py` | `.tmp/docwriter_write_v43.py` | `whitelist_backup_2026_10_17/docwriter_write_v43.py` | 33,607 | `d5e6390b900d` | `d5e6390b900d` | `d5e6390b900d` | ✅ |
| 430 | `.tmp/docwriter_write_v44.py` | `.tmp/docwriter_write_v44.py` | `whitelist_backup_2026_10_17/docwriter_write_v44.py` | 84,551 | `54812b76573b` | `54812b76573b` | `54812b76573b` | ✅ |
| 431 | `.tmp/docwriter_write_v45.py` | `.tmp/docwriter_write_v45.py` | `whitelist_backup_2026_10_17/docwriter_write_v45.py` | 61,168 | `af3a22741b2f` | `af3a22741b2f` | `af3a22741b2f` | ✅ |
| 432 | `.tmp/dscan_01.json` | `.tmp/dscan_01.json` | `whitelist_backup_2026_10_17/dscan_01.json` | 195,396 | `bab5d4a367af` | `bab5d4a367af` | `bab5d4a367af` | ✅ |
| 433 | `.tmp/dscan_01.py` | `.tmp/dscan_01.py` | `whitelist_backup_2026_10_17/dscan_01.py` | 2,865 | `a58735d65c3c` | `a58735d65c3c` | `a58735d65c3c` | ✅ |
| 434 | `.tmp/dscan_02.py` | `.tmp/dscan_02.py` | `whitelist_backup_2026_10_17/dscan_02.py` | 5,078 | `1f6ffd7e0f47` | `1f6ffd7e0f47` | `1f6ffd7e0f47` | ✅ |
| 435 | `.tmp/dscan_03.py` | `.tmp/dscan_03.py` | `whitelist_backup_2026_10_17/dscan_03.py` | 5,360 | `35711329ad8f` | `35711329ad8f` | `35711329ad8f` | ✅ |
| 436 | `.tmp/dscan_04.py` | `.tmp/dscan_04.py` | `whitelist_backup_2026_10_17/dscan_04.py` | 2,302 | `43e661f72888` | `43e661f72888` | `43e661f72888` | ✅ |
| 437 | `.tmp/dscan_05.py` | `.tmp/dscan_05.py` | `whitelist_backup_2026_10_17/dscan_05.py` | 6,207 | `966d9ce0df2d` | `966d9ce0df2d` | `966d9ce0df2d` | ✅ |
| 438 | `.tmp/dscan_06.py` | `.tmp/dscan_06.py` | `whitelist_backup_2026_10_17/dscan_06.py` | 1,845 | `7c059d996778` | `7c059d996778` | `7c059d996778` | ✅ |
| 439 | `.tmp/dscan_07.py` | `.tmp/dscan_07.py` | `whitelist_backup_2026_10_17/dscan_07.py` | 1,074 | `26897ce01079` | `26897ce01079` | `26897ce01079` | ✅ |
| 440 | `.tmp/dscan_08.py` | `.tmp/dscan_08.py` | `whitelist_backup_2026_10_17/dscan_08.py` | 2,370 | `fc3c78d3f0e5` | `fc3c78d3f0e5` | `fc3c78d3f0e5` | ✅ |
| 441 | `.tmp/dscan_classified.json` | `.tmp/dscan_classified.json` | `whitelist_backup_2026_10_17/dscan_classified.json` | 47,129 | `458a2e06a2d3` | `458a2e06a2d3` | `458a2e06a2d3` | ✅ |
| 442 | `.tmp/dscan_classified.txt` | `.tmp/dscan_classified.txt` | `whitelist_backup_2026_10_17/dscan_classified.txt` | 11,199 | `2945d458f5a6` | `2945d458f5a6` | `2945d458f5a6` | ✅ |
| 443 | `.tmp/dscan_copycmp.txt` | `.tmp/dscan_copycmp.txt` | `whitelist_backup_2026_10_17/dscan_copycmp.txt` | 687 | `3af905a1f5c4` | `3af905a1f5c4` | `3af905a1f5c4` | ✅ |
| 444 | `.tmp/dscan_families.txt` | `.tmp/dscan_families.txt` | `whitelist_backup_2026_10_17/dscan_families.txt` | 3,535 | `3bc5960fa2bf` | `3bc5960fa2bf` | `3bc5960fa2bf` | ✅ |
| 445 | `.tmp/dscan_matrix.json` | `.tmp/dscan_matrix.json` | `whitelist_backup_2026_10_17/dscan_matrix.json` | 273,930 | `875f08dd0648` | `875f08dd0648` | `875f08dd0648` | ✅ |
| 446 | `.tmp/dscan_matrix.txt` | `.tmp/dscan_matrix.txt` | `whitelist_backup_2026_10_17/dscan_matrix.txt` | 1,452 | `a8d3aa0287b6` | `a8d3aa0287b6` | `a8d3aa0287b6` | ✅ |
| 447 | `.tmp/dscan_repo_dump.txt` | `.tmp/dscan_repo_dump.txt` | `whitelist_backup_2026_10_17/dscan_repo_dump.txt` | 24,326 | `06d5da0d55ed` | `06d5da0d55ed` | `06d5da0d55ed` | ✅ |
| 448 | `.tmp/dscan_stats.txt` | `.tmp/dscan_stats.txt` | `whitelist_backup_2026_10_17/dscan_stats.txt` | 2,712 | `b35fb0ebd75d` | `b35fb0ebd75d` | `b35fb0ebd75d` | ✅ |
| 449 | `.tmp/dscan_sub_dump.txt` | `.tmp/dscan_sub_dump.txt` | `whitelist_backup_2026_10_17/dscan_sub_dump.txt` | 94,170 | `8c3f99c0b128` | `8c3f99c0b128` | `8c3f99c0b128` | ✅ |
| 450 | `.tmp/dscan_tables.md` | `.tmp/dscan_tables.md` | `whitelist_backup_2026_10_17/dscan_tables.md` | 56,191 | `0a96d4720449` | `0a96d4720449` | `0a96d4720449` | ✅ |
| 451 | `.tmp/dscan_write_01.py` | `.tmp/dscan_write_01.py` | `whitelist_backup_2026_10_17/dscan_write_01.py` | 23,330 | `71cbf839d36b` | `71cbf839d36b` | `71cbf839d36b` | ✅ |
| 452 | `.tmp/dscan_xcheck.txt` | `.tmp/dscan_xcheck.txt` | `whitelist_backup_2026_10_17/dscan_xcheck.txt` | 3,196 | `57dcd8344683` | `57dcd8344683` | `57dcd8344683` | ✅ |
| 453 | `.tmp/dw720_calc_2026_10_16.py` | `.tmp/dw720_calc_2026_10_16.py` | `whitelist_backup_2026_10_17/dw720_calc_2026_10_16.py` | 1,797 | `5da6bf2d700a` | `5da6bf2d700a` | `5da6bf2d700a` | ✅ |
| 454 | `.tmp/dw720_probe_2026_10_16.py` | `.tmp/dw720_probe_2026_10_16.py` | `whitelist_backup_2026_10_17/dw720_probe_2026_10_16.py` | 1,450 | `efdb4c877f3f` | `efdb4c877f3f` | `efdb4c877f3f` | ✅ |
| 455 | `.tmp/dw720_verify_2026_10_16.py` | `.tmp/dw720_verify_2026_10_16.py` | `whitelist_backup_2026_10_17/dw720_verify_2026_10_16.py` | 3,909 | `c90f9a64c3d8` | `c90f9a64c3d8` | `c90f9a64c3d8` | ✅ |
| 456 | `.tmp/dw720_write_2026_10_16.py` | `.tmp/dw720_write_2026_10_16.py` | `whitelist_backup_2026_10_17/dw720_write_2026_10_16.py` | 29,681 | `46e8be383b3c` | `46e8be383b3c` | `46e8be383b3c` | ✅ |
| 457 | `.tmp/ea_build.py` | `.tmp/ea_build.py` | `whitelist_backup_2026_10_17/ea_build.py` | 30,376 | `8048ac40151e` | `8048ac40151e` | `8048ac40151e` | ✅ |
| 458 | `.tmp/ea_files.json` | `.tmp/ea_files.json` | `whitelist_backup_2026_10_17/ea_files.json` | 191,599 | `48b76f2549f3` | `48b76f2549f3` | `48b76f2549f3` | ✅ |
| 459 | `.tmp/ea_p2.py` | `.tmp/ea_p2.py` | `whitelist_backup_2026_10_17/ea_p2.py` | 1,030 | `64fb6201dca9` | `64fb6201dca9` | `64fb6201dca9` | ✅ |
| 460 | `.tmp/ea_scan1.py` | `.tmp/ea_scan1.py` | `whitelist_backup_2026_10_17/ea_scan1.py` | 1,005 | `e21c9fca13d0` | `e21c9fca13d0` | `e21c9fca13d0` | ✅ |
| 461 | `.tmp/ea_sha12.json` | `.tmp/ea_sha12.json` | `whitelist_backup_2026_10_17/ea_sha12.json` | 289,347 | `381dd57aaca4` | `381dd57aaca4` | `381dd57aaca4` | ✅ |
| 462 | `.tmp/erratum_glm_wholepack_body.md` | `.tmp/erratum_glm_wholepack_body.md` | `whitelist_backup_2026_10_17/erratum_glm_wholepack_body.md` | 24,905 | `0291002f749e` | `0291002f749e` | `0291002f749e` | ✅ |
| 463 | `.tmp/evauditor_one_finish_write.py` | `.tmp/evauditor_one_finish_write.py` | `whitelist_backup_2026_10_17/evauditor_one_finish_write.py` | 46,211 | `c24967f8114e` | `c24967f8114e` | `c24967f8114e` | ✅ |
| 464 | `.tmp/exp04_h_contrast_2026_10_10.py` | `.tmp/exp04_h_contrast_2026_10_10.py` | `whitelist_backup_2026_10_17/exp04_h_contrast_2026_10_10.py` | 14,333 | `572f1b9c3927` | `572f1b9c3927` | `572f1b9c3927` | ✅ |
| 465 | `.tmp/f2_branch_fix_transform_2026_09_29.py` | `.tmp/f2_branch_fix_transform_2026_09_29.py` | `whitelist_backup_2026_10_17/f2_branch_fix_transform_2026_09_29.py` | 18,152 | `0a970b156867` | `0a970b156867` | `0a970b156867` | ✅ |
| 466 | `.tmp/f2_branch_selftest_2026_09_29.py` | `.tmp/f2_branch_selftest_2026_09_29.py` | `whitelist_backup_2026_10_17/f2_branch_selftest_2026_09_29.py` | 7,377 | `68a927174a2e` | `68a927174a2e` | `68a927174a2e` | ✅ |
| 467 | `.tmp/gate_check.py` | `.tmp/gate_check.py` | `whitelist_backup_2026_10_17/gate_check.py` | 648 | `abe7fbdb394b` | `abe7fbdb394b` | `abe7fbdb394b` | ✅ |
| 468 | `.tmp/gate_check2.py` | `.tmp/gate_check2.py` | `whitelist_backup_2026_10_17/gate_check2.py` | 840 | `7025ceceb766` | `7025ceceb766` | `7025ceceb766` | ✅ |
| 469 | `.tmp/ge01_eps_grid_exec2_2026_10_16.json` | `.tmp/ge01_eps_grid_exec2_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_eps_grid_exec2_2026_10_16.json` | 53,903 | `af1fcc0e8852` | `af1fcc0e8852` | `af1fcc0e8852` | ✅ |
| 470 | `.tmp/ge01_eps_grid_exec2_2026_10_16.py` | `.tmp/ge01_eps_grid_exec2_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_eps_grid_exec2_2026_10_16.py` | 11,452 | `9ef16d1b8525` | `9ef16d1b8525` | `9ef16d1b8525` | ✅ |
| 471 | `.tmp/ge01_eps_grid_exec3_2026_10_16.py` | `.tmp/ge01_eps_grid_exec3_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_eps_grid_exec3_2026_10_16.py` | 3,580 | `5225d7800544` | `5225d7800544` | `5225d7800544` | ✅ |
| 472 | `.tmp/ge01_eps_grid_exec_2026_10_16.json` | `.tmp/ge01_eps_grid_exec_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_eps_grid_exec_2026_10_16.json` | 62,749 | `45b233594ee9` | `45b233594ee9` | `45b233594ee9` | ✅ |
| 473 | `.tmp/ge01_eps_grid_exec_2026_10_16.py` | `.tmp/ge01_eps_grid_exec_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_eps_grid_exec_2026_10_16.py` | 11,018 | `ab5e001cb63b` | `ab5e001cb63b` | `ab5e001cb63b` | ✅ |
| 474 | `.tmp/ge01_eps_grid_verify_2026_10_16.py` | `.tmp/ge01_eps_grid_verify_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_eps_grid_verify_2026_10_16.py` | 3,016 | `4ff9d5a95dcf` | `4ff9d5a95dcf` | `4ff9d5a95dcf` | ✅ |
| 475 | `.tmp/ge01_full_1494_adjudicate_2026_10_16.py` | `.tmp/ge01_full_1494_adjudicate_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_adjudicate_2026_10_16.py` | 14,293 | `8108e4c883ad` | `8108e4c883ad` | `8108e4c883ad` | ✅ |
| 476 | `.tmp/ge01_full_1494_collect_2026_10_16.py` | `.tmp/ge01_full_1494_collect_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_collect_2026_10_16.py` | 28,322 | `039ebfca39b7` | `039ebfca39b7` | `039ebfca39b7` | ✅ |
| 477 | `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py` | `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_exec_r1_write_2026_10_16.py` | 43,129 | `9e9e402893ef` | `9e9e402893ef` | `9e9e402893ef` | ✅ |
| 478 | `.tmp/ge01_full_1494_freeze_2026_10_16.json` | `.tmp/ge01_full_1494_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_full_1494_freeze_2026_10_16.json` | 7,479 | `8494390a274a` | `8494390a274a` | `8494390a274a` | ✅ |
| 479 | `.tmp/ge01_full_1494_freeze_write_2026_10_16.py` | `.tmp/ge01_full_1494_freeze_write_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_freeze_write_2026_10_16.py` | 23,781 | `b89e0432ab97` | `b89e0432ab97` | `b89e0432ab97` | ✅ |
| 480 | `.tmp/ge01_full_1494_llm_calls_2026_10_16.jsonl` | `.tmp/ge01_full_1494_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/ge01_full_1494_llm_calls_2026_10_16.jsonl` | 235,298 | `e922d168ab60` | `e922d168ab60` | `e922d168ab60` | ✅ |
| 481 | `.tmp/ge01_full_1494_measurement_2026_10_16.json` | `.tmp/ge01_full_1494_measurement_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_full_1494_measurement_2026_10_16.json` | 547,703 | `4054d1393b84` | `4054d1393b84` | `4054d1393b84` | ✅ |
| 482 | `.tmp/ge01_full_1494_measurement_resume32_2026_10_16.json` | `.tmp/ge01_full_1494_measurement_resume32_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_full_1494_measurement_resume32_2026_10_16.json` | 570,852 | `7ccc5f9e8b2c` | `7ccc5f9e8b2c` | `7ccc5f9e8b2c` | ✅ |
| 483 | `.tmp/ge01_full_1494_precheck_2026_10_16.json` | `.tmp/ge01_full_1494_precheck_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_full_1494_precheck_2026_10_16.json` | 9,432 | `bd6dd07ad1c3` | `bd6dd07ad1c3` | `bd6dd07ad1c3` | ✅ |
| 484 | `.tmp/ge01_full_1494_precheck_2026_10_16.py` | `.tmp/ge01_full_1494_precheck_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_precheck_2026_10_16.py` | 10,700 | `cc34ab8552f9` | `cc34ab8552f9` | `cc34ab8552f9` | ✅ |
| 485 | `.tmp/ge01_full_1494_probe_2026_10_16.py` | `.tmp/ge01_full_1494_probe_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_probe_2026_10_16.py` | 3,199 | `a38499e4d4a9` | `a38499e4d4a9` | `a38499e4d4a9` | ✅ |
| 486 | `.tmp/ge01_full_1494_readout_2026_10_16.py` | `.tmp/ge01_full_1494_readout_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_readout_2026_10_16.py` | 22,920 | `59ed27635c6e` | `59ed27635c6e` | `59ed27635c6e` | ✅ |
| 487 | `.tmp/ge01_full_1494_resume32_collect_2026_10_16.py` | `.tmp/ge01_full_1494_resume32_collect_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_resume32_collect_2026_10_16.py` | 14,609 | `9496620e32b2` | `9496620e32b2` | `9496620e32b2` | ✅ |
| 488 | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.log` | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.log` | `whitelist_backup_2026_10_17/ge01_full_1494_resume32_precheck_2026_10_16.log` | 1,761 | `ada7f41b8cb2` | `ada7f41b8cb2` | `ada7f41b8cb2` | ✅ |
| 489 | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.py` | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_resume32_precheck_2026_10_16.py` | 6,122 | `463532446b61` | `463532446b61` | `463532446b61` | ✅ |
| 490 | `.tmp/ge01_full_1494_resume32_probe_2026_10_16.json` | `.tmp/ge01_full_1494_resume32_probe_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_full_1494_resume32_probe_2026_10_16.json` | 338 | `579a7f8b6fe3` | `579a7f8b6fe3` | `579a7f8b6fe3` | ✅ |
| 491 | `.tmp/ge01_full_1494_resume32_readout_2026_10_16.py` | `.tmp/ge01_full_1494_resume32_readout_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_full_1494_resume32_readout_2026_10_16.py` | 29,430 | `de50589bd6c6` | `de50589bd6c6` | `de50589bd6c6` | ✅ |
| 492 | `.tmp/ge01_full_1494_resume32_run_2026_10_16.log` | `.tmp/ge01_full_1494_resume32_run_2026_10_16.log` | `whitelist_backup_2026_10_17/ge01_full_1494_resume32_run_2026_10_16.log` | 1,033 | `f655e7d9e3e0` | `f655e7d9e3e0` | `f655e7d9e3e0` | ✅ |
| 493 | `.tmp/ge01_full_1494_resume32_stage_2026_10_16.json` | `.tmp/ge01_full_1494_resume32_stage_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_full_1494_resume32_stage_2026_10_16.json` | 7,574 | `25d95a22bbb1` | `25d95a22bbb1` | `25d95a22bbb1` | ✅ |
| 494 | `.tmp/ge01_full_1494_run_2026_10_16.log` | `.tmp/ge01_full_1494_run_2026_10_16.log` | `whitelist_backup_2026_10_17/ge01_full_1494_run_2026_10_16.log` | 14,810 | `3e85eac1bf6a` | `3e85eac1bf6a` | `3e85eac1bf6a` | ✅ |
| 495 | `.tmp/ge01_gate_index.py` | `.tmp/ge01_gate_index.py` | `whitelist_backup_2026_10_17/ge01_gate_index.py` | 3,095 | `fc4ed5e7dea0` | `fc4ed5e7dea0` | `fc4ed5e7dea0` | ✅ |
| 496 | `.tmp/ge01_gate_measure.py` | `.tmp/ge01_gate_measure.py` | `whitelist_backup_2026_10_17/ge01_gate_measure.py` | 4,068 | `c2cdebcb0bfc` | `c2cdebcb0bfc` | `c2cdebcb0bfc` | ✅ |
| 497 | `.tmp/ge01_gate_probe.py` | `.tmp/ge01_gate_probe.py` | `whitelist_backup_2026_10_17/ge01_gate_probe.py` | 3,196 | `82bf49985799` | `82bf49985799` | `82bf49985799` | ✅ |
| 498 | `.tmp/ge01_gate_scan.py` | `.tmp/ge01_gate_scan.py` | `whitelist_backup_2026_10_17/ge01_gate_scan.py` | 1,955 | `5f6212d13cb5` | `5f6212d13cb5` | `5f6212d13cb5` | ✅ |
| 499 | `.tmp/ge01_gate_write.py` | `.tmp/ge01_gate_write.py` | `whitelist_backup_2026_10_17/ge01_gate_write.py` | 82,875 | `a661b2c7e5f0` | `a661b2c7e5f0` | `a661b2c7e5f0` | ✅ |
| 500 | `.tmp/ge01_measure_list.json` | `.tmp/ge01_measure_list.json` | `whitelist_backup_2026_10_17/ge01_measure_list.json` | 2,435 | `2eb41639edf4` | `2eb41639edf4` | `2eb41639edf4` | ✅ |
| 501 | `.tmp/ge01_results_sha12.json` | `.tmp/ge01_results_sha12.json` | `whitelist_backup_2026_10_17/ge01_results_sha12.json` | 192,203 | `97fb1089de90` | `97fb1089de90` | `97fb1089de90` | ✅ |
| 502 | `.tmp/ge01_s3_keyscan_2026_10_16.py` | `.tmp/ge01_s3_keyscan_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_s3_keyscan_2026_10_16.py` | 1,730 | `5f8a18033a99` | `5f8a18033a99` | `5f8a18033a99` | ✅ |
| 503 | `.tmp/ge01_s3_vadj_recheck_2026_10_16.py` | `.tmp/ge01_s3_vadj_recheck_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_s3_vadj_recheck_2026_10_16.py` | 13,088 | `91d3e1d91b58` | `91d3e1d91b58` | `91d3e1d91b58` | ✅ |
| 504 | `.tmp/ge01_s3b_keyscan_2026_10_16.py` | `.tmp/ge01_s3b_keyscan_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_s3b_keyscan_2026_10_16.py` | 2,052 | `b7743ec5a7ab` | `b7743ec5a7ab` | `b7743ec5a7ab` | ✅ |
| 505 | `.tmp/ge01_s3b_v_exec_2026_10_16.py` | `.tmp/ge01_s3b_v_exec_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_s3b_v_exec_2026_10_16.py` | 6,410 | `0df5d957a911` | `0df5d957a911` | `0df5d957a911` | ✅ |
| 506 | `.tmp/ge01_s3b_v_exec_r1_2026_10_16.py` | `.tmp/ge01_s3b_v_exec_r1_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_2026_10_16.py` | 15,257 | `4f525232efe4` | `4f525232efe4` | `4f525232efe4` | ✅ |
| 507 | `.tmp/ge01_s3b_v_exec_r1_readings_2026_10_16.json` | `.tmp/ge01_s3b_v_exec_r1_readings_2026_10_16.json` | `whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_readings_2026_10_16.json` | 25,489 | `1ec7c258c637` | `1ec7c258c637` | `1ec7c258c637` | ✅ |
| 508 | `.tmp/ge01_s3b_v_exec_r1_supp_2026_10_16.py` | `.tmp/ge01_s3b_v_exec_r1_supp_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_supp_2026_10_16.py` | 5,199 | `0646da5ccbe5` | `0646da5ccbe5` | `0646da5ccbe5` | ✅ |
| 509 | `.tmp/ge01_s3b_v_exec_r1_write_2026_10_16.py` | `.tmp/ge01_s3b_v_exec_r1_write_2026_10_16.py` | `whitelist_backup_2026_10_17/ge01_s3b_v_exec_r1_write_2026_10_16.py` | 56,062 | `359b768e7dc0` | `359b768e7dc0` | `359b768e7dc0` | ✅ |
| 510 | `.tmp/ge02_build.py` | `.tmp/ge02_build.py` | `whitelist_backup_2026_10_17/ge02_build.py` | 24,774 | `a10c57adf6b5` | `a10c57adf6b5` | `a10c57adf6b5` | ✅ |
| 511 | `.tmp/ge02_recompute.py` | `.tmp/ge02_recompute.py` | `whitelist_backup_2026_10_17/ge02_recompute.py` | 1,347 | `811d4a138788` | `811d4a138788` | `811d4a138788` | ✅ |
| 512 | `.tmp/gen_supp3.py` | `.tmp/gen_supp3.py` | `whitelist_backup_2026_10_17/gen_supp3.py` | 15,813 | `eb53c9ce140c` | `eb53c9ce140c` | `eb53c9ce140c` | ✅ |
| 513 | `.tmp/gen_v35_uactive_2026_10_16.py` | `.tmp/gen_v35_uactive_2026_10_16.py` | `whitelist_backup_2026_10_17/gen_v35_uactive_2026_10_16.py` | 43,518 | `628c99636f10` | `628c99636f10` | `628c99636f10` | ✅ |
| 514 | `.tmp/h_src.py` | `.tmp/h_src.py` | `whitelist_backup_2026_10_17/h_src.py` | 727 | `a4b8970b8b1f` | `a4b8970b8b1f` | `a4b8970b8b1f` | ✅ |
| 515 | `.tmp/harness.py` | `.tmp/harness.py` | `whitelist_backup_2026_10_17/harness.py` | 687 | `56e02c4878f4` | `56e02c4878f4` | `56e02c4878f4` | ✅ |
| 516 | `.tmp/k_v3df_0_1_four_readings_2026_10_09.py` | `.tmp/k_v3df_0_1_four_readings_2026_10_09.py` | `whitelist_backup_2026_10_17/k_v3df_0_1_four_readings_2026_10_09.py` | 50,232 | `2e990644cc8d` | `2e990644cc8d` | `2e990644cc8d` | ✅ |
| 517 | `.tmp/kd14_absorption_probe.py` | `.tmp/kd14_absorption_probe.py` | `whitelist_backup_2026_10_17/kd14_absorption_probe.py` | 1,358 | `915c968f2d04` | `915c968f2d04` | `915c968f2d04` | ✅ |
| 518 | `.tmp/kd14_carrier_probe.py` | `.tmp/kd14_carrier_probe.py` | `whitelist_backup_2026_10_17/kd14_carrier_probe.py` | 1,206 | `758033c2a76b` | `758033c2a76b` | `758033c2a76b` | ✅ |
| 519 | `.tmp/kd14_m4_corrected.py` | `.tmp/kd14_m4_corrected.py` | `whitelist_backup_2026_10_17/kd14_m4_corrected.py` | 932 | `50c1c7d85616` | `50c1c7d85616` | `50c1c7d85616` | ✅ |
| 520 | `.tmp/klm41_2_bootstrap_ci_2026_10_16.json` | `.tmp/klm41_2_bootstrap_ci_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_2_bootstrap_ci_2026_10_16.json` | 12,373 | `be99abcba9bf` | `be99abcba9bf` | `be99abcba9bf` | ✅ |
| 521 | `.tmp/klm41_2_caliber_decl_2026_10_16.json` | `.tmp/klm41_2_caliber_decl_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_2_caliber_decl_2026_10_16.json` | 4,757 | `6f0721d20c06` | `6f0721d20c06` | `6f0721d20c06` | ✅ |
| 522 | `.tmp/klm41_2_caliber_decl_2026_10_16.py` | `.tmp/klm41_2_caliber_decl_2026_10_16.py` | `whitelist_backup_2026_10_17/klm41_2_caliber_decl_2026_10_16.py` | 10,466 | `d9754474ad9a` | `d9754474ad9a` | `d9754474ad9a` | ✅ |
| 523 | `.tmp/klm41_2_compute_ci_2026_10_16.py` | `.tmp/klm41_2_compute_ci_2026_10_16.py` | `whitelist_backup_2026_10_17/klm41_2_compute_ci_2026_10_16.py` | 14,398 | `fb38b90df08f` | `fb38b90df08f` | `fb38b90df08f` | ✅ |
| 524 | `.tmp/klm41_2_freeze_2026_10_16.json` | `.tmp/klm41_2_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_2_freeze_2026_10_16.json` | 3,211 | `2a4453d9610b` | `2a4453d9610b` | `2a4453d9610b` | ✅ |
| 525 | `.tmp/klm41_2_stratified_ci_2026_10_16.json` | `.tmp/klm41_2_stratified_ci_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_2_stratified_ci_2026_10_16.json` | 18,820 | `67ae4f540e47` | `67ae4f540e47` | `67ae4f540e47` | ✅ |
| 526 | `.tmp/klm41_2_stratified_ci_2026_10_16.py` | `.tmp/klm41_2_stratified_ci_2026_10_16.py` | `whitelist_backup_2026_10_17/klm41_2_stratified_ci_2026_10_16.py` | 8,819 | `f29526bccea3` | `f29526bccea3` | `f29526bccea3` | ✅ |
| 527 | `.tmp/klm41_2_verify_2026_10_16.json` | `.tmp/klm41_2_verify_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_2_verify_2026_10_16.json` | 2,906 | `5ded5068566b` | `5ded5068566b` | `5ded5068566b` | ✅ |
| 528 | `.tmp/klm41_2_verify_2026_10_16.py` | `.tmp/klm41_2_verify_2026_10_16.py` | `whitelist_backup_2026_10_17/klm41_2_verify_2026_10_16.py` | 10,976 | `af0f38f33222` | `af0f38f33222` | `af0f38f33222` | ✅ |
| 529 | `.tmp/klm41_2_write_doc_2026_10_16.py` | `.tmp/klm41_2_write_doc_2026_10_16.py` | `whitelist_backup_2026_10_17/klm41_2_write_doc_2026_10_16.py` | 48,391 | `902dcf78f2b8` | `902dcf78f2b8` | `902dcf78f2b8` | ✅ |
| 530 | `.tmp/klm41_3_ts_caliber_decl_2026_10_16.json` | `.tmp/klm41_3_ts_caliber_decl_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_3_ts_caliber_decl_2026_10_16.json` | 3,255 | `96456529a485` | `96456529a485` | `96456529a485` | ✅ |
| 531 | `.tmp/klm41_3_ts_collect_2026_10_16.py` | `.tmp/klm41_3_ts_collect_2026_10_16.py` | `whitelist_backup_2026_10_17/klm41_3_ts_collect_2026_10_16.py` | 23,196 | `a28c4ba40940` | `a28c4ba40940` | `a28c4ba40940` | ✅ |
| 532 | `.tmp/klm41_3_ts_freeze_2026_10_16.json` | `.tmp/klm41_3_ts_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_3_ts_freeze_2026_10_16.json` | 2,235 | `25c021d29b1b` | `25c021d29b1b` | `25c021d29b1b` | ✅ |
| 533 | `.tmp/klm41_3_ts_llm_calls_2026_10_16.jsonl` | `.tmp/klm41_3_ts_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/klm41_3_ts_llm_calls_2026_10_16.jsonl` | 123,255 | `595699b7ec44` | `595699b7ec44` | `595699b7ec44` | ✅ |
| 534 | `.tmp/klm41_3_ts_measurement_2026_10_16.json` | `.tmp/klm41_3_ts_measurement_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_3_ts_measurement_2026_10_16.json` | 252,951 | `211a49ca9941` | `211a49ca9941` | `211a49ca9941` | ✅ |
| 535 | `.tmp/klm41_3_ts_preflight_2026_10_16.json` | `.tmp/klm41_3_ts_preflight_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_3_ts_preflight_2026_10_16.json` | 6,349 | `d1fe0a6889be` | `d1fe0a6889be` | `d1fe0a6889be` | ✅ |
| 536 | `.tmp/klm41_3_ts_preflight_2026_10_16.py` | `.tmp/klm41_3_ts_preflight_2026_10_16.py` | `whitelist_backup_2026_10_17/klm41_3_ts_preflight_2026_10_16.py` | 6,228 | `c787c6d4e361` | `c787c6d4e361` | `c787c6d4e361` | ✅ |
| 537 | `.tmp/klm41_3_ts_tables_2026_10_16.md` | `.tmp/klm41_3_ts_tables_2026_10_16.md` | `whitelist_backup_2026_10_17/klm41_3_ts_tables_2026_10_16.md` | 11,297 | `54213bffc216` | `54213bffc216` | `54213bffc216` | ✅ |
| 538 | `.tmp/klm41_3_ts_verify_2026_10_16.json` | `.tmp/klm41_3_ts_verify_2026_10_16.json` | `whitelist_backup_2026_10_17/klm41_3_ts_verify_2026_10_16.json` | 5,848 | `8cf7bb595870` | `8cf7bb595870` | `8cf7bb595870` | ✅ |
| 539 | `.tmp/kro_extract.py` | `.tmp/kro_extract.py` | `whitelist_backup_2026_10_17/kro_extract.py` | 802 | `b5731abae41f` | `b5731abae41f` | `b5731abae41f` | ✅ |
| 540 | `.tmp/m08_enum_v2_2026_10_16.json` | `.tmp/m08_enum_v2_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_enum_v2_2026_10_16.json` | 12,255 | `c45cfc3ddc8d` | `c45cfc3ddc8d` | `c45cfc3ddc8d` | ✅ |
| 541 | `.tmp/m08_r1_amend2_2026_10_16.json` | `.tmp/m08_r1_amend2_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_amend2_2026_10_16.json` | 1,296 | `21ad2e7acd0b` | `21ad2e7acd0b` | `21ad2e7acd0b` | ✅ |
| 542 | `.tmp/m08_r1_amend3_2026_10_16.json` | `.tmp/m08_r1_amend3_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_amend3_2026_10_16.json` | 3,034 | `d77931c6d7a5` | `d77931c6d7a5` | `d77931c6d7a5` | ✅ |
| 543 | `.tmp/m08_r1_amend_2026_10_16.json` | `.tmp/m08_r1_amend_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_amend_2026_10_16.json` | 1,204 | `3c982068b276` | `3c982068b276` | `3c982068b276` | ✅ |
| 544 | `.tmp/m08_r1_enum_2026_10_16.json` | `.tmp/m08_r1_enum_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_enum_2026_10_16.json` | 13,253 | `361f67e37092` | `361f67e37092` | `361f67e37092` | ✅ |
| 545 | `.tmp/m08_r1_enum_2026_10_16.py` | `.tmp/m08_r1_enum_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_enum_2026_10_16.py` | 16,318 | `884b7161e053` | `884b7161e053` | `884b7161e053` | ✅ |
| 546 | `.tmp/m08_r1_freeze_2026_10_16.json` | `.tmp/m08_r1_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_freeze_2026_10_16.json` | 7,655 | `1a40d8046fdc` | `1a40d8046fdc` | `1a40d8046fdc` | ✅ |
| 547 | `.tmp/m08_r1_freeze_2026_10_16.py` | `.tmp/m08_r1_freeze_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_freeze_2026_10_16.py` | 9,207 | `8c6b5e0d3ebb` | `8c6b5e0d3ebb` | `8c6b5e0d3ebb` | ✅ |
| 548 | `.tmp/m08_r1_llm_arm_2026_10_16.json` | `.tmp/m08_r1_llm_arm_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_llm_arm_2026_10_16.json` | 11,335 | `19d93d77b46e` | `19d93d77b46e` | `19d93d77b46e` | ✅ |
| 549 | `.tmp/m08_r1_llm_arm_2026_10_16.py` | `.tmp/m08_r1_llm_arm_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_llm_arm_2026_10_16.py` | 9,852 | `987820693d06` | `987820693d06` | `987820693d06` | ✅ |
| 550 | `.tmp/m08_r1_llm_calls_2026_10_16.jsonl` | `.tmp/m08_r1_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/m08_r1_llm_calls_2026_10_16.jsonl` | 8,271 | `0e8c9664b06d` | `0e8c9664b06d` | `0e8c9664b06d` | ✅ |
| 551 | `.tmp/m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | `.tmp/m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | 8,230 | `d30121ed7ebf` | `d30121ed7ebf` | `d30121ed7ebf` | ✅ |
| 552 | `.tmp/m08_r1_llm_probe2_2026_10_16.json` | `.tmp/m08_r1_llm_probe2_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_llm_probe2_2026_10_16.json` | 1,805 | `d2a8510b1322` | `d2a8510b1322` | `d2a8510b1322` | ✅ |
| 553 | `.tmp/m08_r1_llm_probe2_2026_10_16.py` | `.tmp/m08_r1_llm_probe2_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_llm_probe2_2026_10_16.py` | 2,359 | `190668eae9da` | `190668eae9da` | `190668eae9da` | ✅ |
| 554 | `.tmp/m08_r1_probe_2026_10_16.json` | `.tmp/m08_r1_probe_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_probe_2026_10_16.json` | 3,752 | `c2ba80ba548b` | `c2ba80ba548b` | `c2ba80ba548b` | ✅ |
| 555 | `.tmp/m08_r1_probe_2026_10_16.py` | `.tmp/m08_r1_probe_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_probe_2026_10_16.py` | 4,739 | `63f0234a7c89` | `63f0234a7c89` | `63f0234a7c89` | ✅ |
| 556 | `.tmp/m08_r1_recompute_2026_10_16.json` | `.tmp/m08_r1_recompute_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_recompute_2026_10_16.json` | 2,072 | `59ddca239f67` | `59ddca239f67` | `59ddca239f67` | ✅ |
| 557 | `.tmp/m08_r1_recompute_2026_10_16.py` | `.tmp/m08_r1_recompute_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_recompute_2026_10_16.py` | 6,998 | `305ee668612c` | `305ee668612c` | `305ee668612c` | ✅ |
| 558 | `.tmp/m08_r1_srcsha_2026_10_16.json` | `.tmp/m08_r1_srcsha_2026_10_16.json` | `whitelist_backup_2026_10_17/m08_r1_srcsha_2026_10_16.json` | 8,851 | `2074096a45e2` | `2074096a45e2` | `2074096a45e2` | ✅ |
| 559 | `.tmp/m08_r1_srcsha_2026_10_16.py` | `.tmp/m08_r1_srcsha_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_srcsha_2026_10_16.py` | 3,697 | `96ac0e7c23f6` | `96ac0e7c23f6` | `96ac0e7c23f6` | ✅ |
| 560 | `.tmp/m08_r1_write_2026_10_16.py` | `.tmp/m08_r1_write_2026_10_16.py` | `whitelist_backup_2026_10_17/m08_r1_write_2026_10_16.py` | 58,218 | `0a5d9e9f18d9` | `0a5d9e9f18d9` | `0a5d9e9f18d9` | ✅ |
| 561 | `.tmp/m2_docwriter_write.py` | `.tmp/m2_docwriter_write.py` | `whitelist_backup_2026_10_17/m2_docwriter_write.py` | 23,214 | `9842ca168062` | `9842ca168062` | `9842ca168062` | ✅ |
| 562 | `.tmp/m2_write.py` | `.tmp/m2_write.py` | `whitelist_backup_2026_10_17/m2_write.py` | 24,159 | `133387a21ec6` | `133387a21ec6` | `133387a21ec6` | ✅ |
| 563 | `.tmp/m2verdict_downstream.py` | `.tmp/m2verdict_downstream.py` | `whitelist_backup_2026_10_17/m2verdict_downstream.py` | 2,240 | `93c831a7fc0f` | `93c831a7fc0f` | `93c831a7fc0f` | ✅ |
| 564 | `.tmp/m2verdict_meta.py` | `.tmp/m2verdict_meta.py` | `whitelist_backup_2026_10_17/m2verdict_meta.py` | 1,223 | `c89599655807` | `c89599655807` | `c89599655807` | ✅ |
| 565 | `.tmp/m2verdict_probe.py` | `.tmp/m2verdict_probe.py` | `whitelist_backup_2026_10_17/m2verdict_probe.py` | 4,493 | `3a401ef46a00` | `3a401ef46a00` | `3a401ef46a00` | ✅ |
| 566 | `.tmp/m2verdict_ruling.py` | `.tmp/m2verdict_ruling.py` | `whitelist_backup_2026_10_17/m2verdict_ruling.py` | 1,125 | `841949136e81` | `841949136e81` | `841949136e81` | ✅ |
| 567 | `.tmp/m41_dual_readout.py` | `.tmp/m41_dual_readout.py` | `whitelist_backup_2026_10_17/m41_dual_readout.py` | 6,471 | `45f3d856efd8` | `45f3d856efd8` | `45f3d856efd8` | ✅ |
| 568 | `.tmp/m41_endpoint_probe.py` | `.tmp/m41_endpoint_probe.py` | `whitelist_backup_2026_10_17/m41_endpoint_probe.py` | 1,520 | `f9811a6eceba` | `f9811a6eceba` | `f9811a6eceba` | ✅ |
| 569 | `.tmp/m41_fix_diag.json` | `.tmp/m41_fix_diag.json` | `whitelist_backup_2026_10_17/m41_fix_diag.json` | 1,034 | `2e34378d0d2c` | `2e34378d0d2c` | `2e34378d0d2c` | ✅ |
| 570 | `.tmp/m41_keyprobe.py` | `.tmp/m41_keyprobe.py` | `whitelist_backup_2026_10_17/m41_keyprobe.py` | 892 | `10e08b837e05` | `10e08b837e05` | `10e08b837e05` | ✅ |
| 571 | `.tmp/m41_keysurvey.py` | `.tmp/m41_keysurvey.py` | `whitelist_backup_2026_10_17/m41_keysurvey.py` | 1,296 | `795daa633133` | `795daa633133` | `795daa633133` | ✅ |
| 572 | `.tmp/m41_llm_calls.jsonl` | `.tmp/m41_llm_calls.jsonl` | `whitelist_backup_2026_10_17/m41_llm_calls.jsonl` | 642 | `a1651f3d9303` | `a1651f3d9303` | `a1651f3d9303` | ✅ |
| 573 | `.tmp/m41_mech_arms.json` | `.tmp/m41_mech_arms.json` | `whitelist_backup_2026_10_17/m41_mech_arms.json` | 1,252 | `be1a8fce8660` | `be1a8fce8660` | `be1a8fce8660` | ✅ |
| 574 | `.tmp/m41_mech_arms.py` | `.tmp/m41_mech_arms.py` | `whitelist_backup_2026_10_17/m41_mech_arms.py` | 3,731 | `a92812ceae61` | `a92812ceae61` | `a92812ceae61` | ✅ |
| 575 | `.tmp/m41_r15_collect_readout.py` | `.tmp/m41_r15_collect_readout.py` | `whitelist_backup_2026_10_17/m41_r15_collect_readout.py` | 13,324 | `d4e882337b80` | `d4e882337b80` | `d4e882337b80` | ✅ |
| 576 | `.tmp/m41_r15_llm_calls.jsonl` | `.tmp/m41_r15_llm_calls.jsonl` | `whitelist_backup_2026_10_17/m41_r15_llm_calls.jsonl` | 3,467 | `7d0dbb58d53a` | `7d0dbb58d53a` | `7d0dbb58d53a` | ✅ |
| 577 | `.tmp/m41_r15_readout.json` | `.tmp/m41_r15_readout.json` | `whitelist_backup_2026_10_17/m41_r15_readout.json` | 14,261 | `33a4720bcafd` | `33a4720bcafd` | `33a4720bcafd` | ✅ |
| 578 | `.tmp/m41_r15_verify.py` | `.tmp/m41_r15_verify.py` | `whitelist_backup_2026_10_17/m41_r15_verify.py` | 4,235 | `f72545f959b4` | `f72545f959b4` | `f72545f959b4` | ✅ |
| 579 | `.tmp/m41_rerun_llm_calls.jsonl` | `.tmp/m41_rerun_llm_calls.jsonl` | `whitelist_backup_2026_10_17/m41_rerun_llm_calls.jsonl` | 24,253 | `19fa12f4e053` | `19fa12f4e053` | `19fa12f4e053` | ✅ |
| 580 | `.tmp/m41_selfcheck.json` | `.tmp/m41_selfcheck.json` | `whitelist_backup_2026_10_17/m41_selfcheck.json` | 318 | `d18a46a884f2` | `d18a46a884f2` | `d18a46a884f2` | ✅ |
| 581 | `.tmp/m41_selfcheck.py` | `.tmp/m41_selfcheck.py` | `whitelist_backup_2026_10_17/m41_selfcheck.py` | 1,291 | `5f066493fdbc` | `5f066493fdbc` | `5f066493fdbc` | ✅ |
| 582 | `.tmp/m41_src_shas.py` | `.tmp/m41_src_shas.py` | `whitelist_backup_2026_10_17/m41_src_shas.py` | 1,138 | `47a192be190a` | `47a192be190a` | `47a192be190a` | ✅ |
| 583 | `.tmp/m41_src_shas.txt` | `.tmp/m41_src_shas.txt` | `whitelist_backup_2026_10_17/m41_src_shas.txt` | 420 | `b2c58664cd51` | `b2c58664cd51` | `b2c58664cd51` | ✅ |
| 584 | `.tmp/material_expansion_kill_freeze_2026_10_16.json` | `.tmp/material_expansion_kill_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/material_expansion_kill_freeze_2026_10_16.json` | 15,187 | `03a628456f0b` | `03a628456f0b` | `03a628456f0b` | ✅ |
| 585 | `.tmp/me_llm_calls_2026_10_16.jsonl` | `.tmp/me_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/me_llm_calls_2026_10_16.jsonl` | 21,339 | `fbdedcb0ef48` | `fbdedcb0ef48` | `fbdedcb0ef48` | ✅ |
| 586 | `.tmp/me_t4_resolve_2026_10_16.py` | `.tmp/me_t4_resolve_2026_10_16.py` | `whitelist_backup_2026_10_17/me_t4_resolve_2026_10_16.py` | 9,507 | `71b0e9c8da44` | `71b0e9c8da44` | `71b0e9c8da44` | ✅ |
| 587 | `.tmp/mq04_budget_calc_2026_10_15.json` | `.tmp/mq04_budget_calc_2026_10_15.json` | `whitelist_backup_2026_10_17/mq04_budget_calc_2026_10_15.json` | 5,436 | `e8a5b2533ac2` | `e8a5b2533ac2` | `e8a5b2533ac2` | ✅ |
| 588 | `.tmp/mq04_budget_calc_2026_10_15.py` | `.tmp/mq04_budget_calc_2026_10_15.py` | `whitelist_backup_2026_10_17/mq04_budget_calc_2026_10_15.py` | 6,803 | `e5e4fcfd5e29` | `e5e4fcfd5e29` | `e5e4fcfd5e29` | ✅ |
| 589 | `.tmp/mq04_nt_llm_calls_2026_10_15.jsonl` | `.tmp/mq04_nt_llm_calls_2026_10_15.jsonl` | `whitelist_backup_2026_10_17/mq04_nt_llm_calls_2026_10_15.jsonl` | 24,320 | `734af9135441` | `734af9135441` | `734af9135441` | ✅ |
| 590 | `.tmp/mq04_nt_measure_2026_10_15.py` | `.tmp/mq04_nt_measure_2026_10_15.py` | `whitelist_backup_2026_10_17/mq04_nt_measure_2026_10_15.py` | 14,503 | `5e55c0ff27f8` | `5e55c0ff27f8` | `5e55c0ff27f8` | ✅ |
| 591 | `.tmp/mq04_nt_measurement_2026_10_15.json` | `.tmp/mq04_nt_measurement_2026_10_15.json` | `whitelist_backup_2026_10_17/mq04_nt_measurement_2026_10_15.json` | 6,047 | `956d35f25c70` | `956d35f25c70` | `956d35f25c70` | ✅ |
| 592 | `.tmp/mq04_write_doc_2026_10_15.py` | `.tmp/mq04_write_doc_2026_10_15.py` | `whitelist_backup_2026_10_17/mq04_write_doc_2026_10_15.py` | 26,377 | `7fb013086741` | `7fb013086741` | `7fb013086741` | ✅ |
| 593 | `.tmp/pa_block.py` | `.tmp/pa_block.py` | `whitelist_backup_2026_10_17/pa_block.py` | 345 | `19ac8c59439b` | `19ac8c59439b` | `19ac8c59439b` | ✅ |
| 594 | `.tmp/pk33q_body.md` | `.tmp/pk33q_body.md` | `whitelist_backup_2026_10_17/pk33q_body.md` | 26,976 | `20ad5b45ba2c` | `20ad5b45ba2c` | `20ad5b45ba2c` | ✅ |
| 595 | `.tmp/pk_body1.md` | `.tmp/pk_body1.md` | `whitelist_backup_2026_10_17/pk_body1.md` | 26,832 | `b32ca40ec103` | `b32ca40ec103` | `b32ca40ec103` | ✅ |
| 596 | `.tmp/pk_body2.md` | `.tmp/pk_body2.md` | `whitelist_backup_2026_10_17/pk_body2.md` | 32,568 | `75a818b2654f` | `75a818b2654f` | `75a818b2654f` | ✅ |
| 597 | `.tmp/pk_lockv2_degeneracy_2026_10_15.json` | `.tmp/pk_lockv2_degeneracy_2026_10_15.json` | `whitelist_backup_2026_10_17/pk_lockv2_degeneracy_2026_10_15.json` | 2,583 | `1106bb7d5c56` | `1106bb7d5c56` | `1106bb7d5c56` | ✅ |
| 598 | `.tmp/pk_lockv2_degeneracy_2026_10_15.py` | `.tmp/pk_lockv2_degeneracy_2026_10_15.py` | `whitelist_backup_2026_10_17/pk_lockv2_degeneracy_2026_10_15.py` | 2,425 | `e8067070c849` | `e8067070c849` | `e8067070c849` | ✅ |
| 599 | `.tmp/pk_lockv2_verify_2026_10_15.json` | `.tmp/pk_lockv2_verify_2026_10_15.json` | `whitelist_backup_2026_10_17/pk_lockv2_verify_2026_10_15.json` | 4,691 | `34cf77faf825` | `34cf77faf825` | `34cf77faf825` | ✅ |
| 600 | `.tmp/pk_lockv2_verify_2026_10_15.py` | `.tmp/pk_lockv2_verify_2026_10_15.py` | `whitelist_backup_2026_10_17/pk_lockv2_verify_2026_10_15.py` | 3,784 | `67795949087d` | `67795949087d` | `67795949087d` | ✅ |
| 601 | `.tmp/pk_lockv2_write_2026_10_15.py` | `.tmp/pk_lockv2_write_2026_10_15.py` | `whitelist_backup_2026_10_17/pk_lockv2_write_2026_10_15.py` | 33,749 | `440affa3e102` | `440affa3e102` | `440affa3e102` | ✅ |
| 602 | `.tmp/pk_measure_01.py` | `.tmp/pk_measure_01.py` | `whitelist_backup_2026_10_17/pk_measure_01.py` | 1,510 | `76af3ed43f2c` | `76af3ed43f2c` | `76af3ed43f2c` | ✅ |
| 603 | `.tmp/pk_probe2_2026_10_16.py` | `.tmp/pk_probe2_2026_10_16.py` | `whitelist_backup_2026_10_17/pk_probe2_2026_10_16.py` | 1,140 | `632e6dca295d` | `632e6dca295d` | `632e6dca295d` | ✅ |
| 604 | `.tmp/pk_probe_2026_10_16.py` | `.tmp/pk_probe_2026_10_16.py` | `whitelist_backup_2026_10_17/pk_probe_2026_10_16.py` | 878 | `809cf2066d48` | `809cf2066d48` | `809cf2066d48` | ✅ |
| 605 | `.tmp/pk_supp500_calc_2026_10_16.py` | `.tmp/pk_supp500_calc_2026_10_16.py` | `whitelist_backup_2026_10_17/pk_supp500_calc_2026_10_16.py` | 3,079 | `5325e2e6bc00` | `5325e2e6bc00` | `5325e2e6bc00` | ✅ |
| 606 | `.tmp/pk_t5lock_body_2026_10_15.md` | `.tmp/pk_t5lock_body_2026_10_15.md` | `whitelist_backup_2026_10_17/pk_t5lock_body_2026_10_15.md` | 46,621 | `404d4fbeef40` | `404d4fbeef40` | `404d4fbeef40` | ✅ |
| 607 | `.tmp/pk_t5lock_verify_2026_10_15.json` | `.tmp/pk_t5lock_verify_2026_10_15.json` | `whitelist_backup_2026_10_17/pk_t5lock_verify_2026_10_15.json` | 4,931 | `0b9c36f612da` | `0b9c36f612da` | `0b9c36f612da` | ✅ |
| 608 | `.tmp/pk_t5lock_verify_2026_10_15.py` | `.tmp/pk_t5lock_verify_2026_10_15.py` | `whitelist_backup_2026_10_17/pk_t5lock_verify_2026_10_15.py` | 5,559 | `3f21b53443b4` | `3f21b53443b4` | `3f21b53443b4` | ✅ |
| 609 | `.tmp/pk_t5lock_write_2026_10_15.py` | `.tmp/pk_t5lock_write_2026_10_15.py` | `whitelist_backup_2026_10_17/pk_t5lock_write_2026_10_15.py` | 3,938 | `e80c26269446` | `e80c26269446` | `e80c26269446` | ✅ |
| 610 | `.tmp/pk_write_budget210_2026_10_16.py` | `.tmp/pk_write_budget210_2026_10_16.py` | `whitelist_backup_2026_10_17/pk_write_budget210_2026_10_16.py` | 20,931 | `0c65c2e859f9` | `0c65c2e859f9` | `0c65c2e859f9` | ✅ |
| 611 | `.tmp/pk_write_design_review_2026_10_16.py` | `.tmp/pk_write_design_review_2026_10_16.py` | `whitelist_backup_2026_10_17/pk_write_design_review_2026_10_16.py` | 47,618 | `439fa0ae048d` | `439fa0ae048d` | `439fa0ae048d` | ✅ |
| 612 | `.tmp/pool_search.py` | `.tmp/pool_search.py` | `whitelist_backup_2026_10_17/pool_search.py` | 2,127 | `3245af3f3bbb` | `3245af3f3bbb` | `3245af3f3bbb` | ✅ |
| 613 | `.tmp/prep.py` | `.tmp/prep.py` | `whitelist_backup_2026_10_17/prep.py` | 4,091 | `e401c8e50f93` | `e401c8e50f93` | `e401c8e50f93` | ✅ |
| 614 | `.tmp/probe3_out.txt` | `.tmp/probe3_out.txt` | `whitelist_backup_2026_10_17/probe3_out.txt` | 41,096 | `d2cef7709033` | `d2cef7709033` | `d2cef7709033` | ✅ |
| 615 | `.tmp/r3m2_disp_write.py` | `.tmp/r3m2_disp_write.py` | `whitelist_backup_2026_10_17/r3m2_disp_write.py` | 18,437 | `988c2fee3ea2` | `988c2fee3ea2` | `988c2fee3ea2` | ✅ |
| 616 | `.tmp/r461_layers.json` | `.tmp/r461_layers.json` | `whitelist_backup_2026_10_17/r461_layers.json` | 102,003 | `fee35e10c208` | `fee35e10c208` | `fee35e10c208` | ✅ |
| 617 | `.tmp/r461_write_01.py` | `.tmp/r461_write_01.py` | `whitelist_backup_2026_10_17/r461_write_01.py` | 19,104 | `9030a50780da` | `9030a50780da` | `9030a50780da` | ✅ |
| 618 | `.tmp/recheck2.py` | `.tmp/recheck2.py` | `whitelist_backup_2026_10_17/recheck2.py` | 2,282 | `85c4cfa3eb46` | `85c4cfa3eb46` | `85c4cfa3eb46` | ✅ |
| 619 | `.tmp/ref_exp_harness_OLD_2026_10_15.py` | `.tmp/ref_exp_harness_OLD_2026_10_15.py` | `whitelist_backup_2026_10_17/ref_exp_harness_OLD_2026_10_15.py` | 13,342 | `7957bac14455` | `7957bac14455` | `7957bac14455` | ✅ |
| 620 | `.tmp/run_steps.py` | `.tmp/run_steps.py` | `whitelist_backup_2026_10_17/run_steps.py` | 2,756 | `019f8405d4cf` | `019f8405d4cf` | `019f8405d4cf` | ✅ |
| 621 | `.tmp/s3_recompute_pass4.py` | `.tmp/s3_recompute_pass4.py` | `whitelist_backup_2026_10_17/s3_recompute_pass4.py` | 4,439 | `6f210893fcce` | `6f210893fcce` | `6f210893fcce` | ✅ |
| 622 | `.tmp/s4_regen_runner.py` | `.tmp/s4_regen_runner.py` | `whitelist_backup_2026_10_17/s4_regen_runner.py` | 13,040 | `70467364bdb1` | `70467364bdb1` | `70467364bdb1` | ✅ |
| 623 | `.tmp/scan_classify_five_terminal_2026_10_10.py` | `.tmp/scan_classify_five_terminal_2026_10_10.py` | `whitelist_backup_2026_10_17/scan_classify_five_terminal_2026_10_10.py` | 7,603 | `0b9b59083534` | `0b9b59083534` | `0b9b59083534` | ✅ |
| 624 | `.tmp/scan_domain_five_terminal_2026_10_10.py` | `.tmp/scan_domain_five_terminal_2026_10_10.py` | `whitelist_backup_2026_10_17/scan_domain_five_terminal_2026_10_10.py` | 2,243 | `732489dc3dbd` | `732489dc3dbd` | `732489dc3dbd` | ✅ |
| 625 | `.tmp/scan_supplement_five_terminal_2026_10_10.py` | `.tmp/scan_supplement_five_terminal_2026_10_10.py` | `whitelist_backup_2026_10_17/scan_supplement_five_terminal_2026_10_10.py` | 6,010 | `7c0a6d022104` | `7c0a6d022104` | `7c0a6d022104` | ✅ |
| 626 | `.tmp/scope_scan.py` | `.tmp/scope_scan.py` | `whitelist_backup_2026_10_17/scope_scan.py` | 3,380 | `07349acfe90f` | `07349acfe90f` | `07349acfe90f` | ✅ |
| 627 | `.tmp/singlevar.py` | `.tmp/singlevar.py` | `whitelist_backup_2026_10_17/singlevar.py` | 1,515 | `f0bba43af3e5` | `f0bba43af3e5` | `f0bba43af3e5` | ✅ |
| 628 | `.tmp/t2_path_b_kill_freeze_2026_10_16.json` | `.tmp/t2_path_b_kill_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/t2_path_b_kill_freeze_2026_10_16.json` | 14,896 | `3f3272100f62` | `3f3272100f62` | `3f3272100f62` | ✅ |
| 629 | `.tmp/t2b_census_2026_10_16.py` | `.tmp/t2b_census_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_census_2026_10_16.py` | 3,041 | `71f99afb9199` | `71f99afb9199` | `71f99afb9199` | ✅ |
| 630 | `.tmp/t2b_derive_2026_10_16.py` | `.tmp/t2b_derive_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_derive_2026_10_16.py` | 7,964 | `324165eb0c7d` | `324165eb0c7d` | `324165eb0c7d` | ✅ |
| 631 | `.tmp/t2b_fetch_facts_2026_10_16.py` | `.tmp/t2b_fetch_facts_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_fetch_facts_2026_10_16.py` | 5,774 | `0941558d024e` | `0941558d024e` | `0941558d024e` | ✅ |
| 632 | `.tmp/t2b_freeze_2026_10_16.py` | `.tmp/t2b_freeze_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_freeze_2026_10_16.py` | 13,908 | `575b796a2e6f` | `575b796a2e6f` | `575b796a2e6f` | ✅ |
| 633 | `.tmp/t2b_freeze_v2_2026_10_16.py` | `.tmp/t2b_freeze_v2_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_freeze_v2_2026_10_16.py` | 17,044 | `02a261b12f7b` | `02a261b12f7b` | `02a261b12f7b` | ✅ |
| 634 | `.tmp/t2b_harness_pre_change_snapshot_2026_10_16.py` | `.tmp/t2b_harness_pre_change_snapshot_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_harness_pre_change_snapshot_2026_10_16.py` | 36,217 | `d5c8d676bb5b` | `d5c8d676bb5b` | `d5c8d676bb5b` | ✅ |
| 635 | `.tmp/t2b_impl_audit_2026_10_16.py` | `.tmp/t2b_impl_audit_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_impl_audit_2026_10_16.py` | 4,856 | `e02a343246bd` | `e02a343246bd` | `e02a343246bd` | ✅ |
| 636 | `.tmp/t2b_inspect_facts_2026_10_16.py` | `.tmp/t2b_inspect_facts_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_inspect_facts_2026_10_16.py` | 1,732 | `de3c879e39f1` | `de3c879e39f1` | `de3c879e39f1` | ✅ |
| 637 | `.tmp/t2b_llm_calls_2026_10_16.jsonl` | `.tmp/t2b_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/t2b_llm_calls_2026_10_16.jsonl` | 5,317 | `a54a3af46ba2` | `a54a3af46ba2` | `a54a3af46ba2` | ✅ |
| 638 | `.tmp/t2b_measure_2026_10_16.py` | `.tmp/t2b_measure_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_measure_2026_10_16.py` | 15,547 | `bd377372927c` | `bd377372927c` | `bd377372927c` | ✅ |
| 639 | `.tmp/t2b_measurement_2026_10_16.json` | `.tmp/t2b_measurement_2026_10_16.json` | `whitelist_backup_2026_10_17/t2b_measurement_2026_10_16.json` | 25,796 | `fe5db6defb09` | `fe5db6defb09` | `fe5db6defb09` | ✅ |
| 640 | `.tmp/t2b_patch_harness_2026_10_16.py` | `.tmp/t2b_patch_harness_2026_10_16.py` | `whitelist_backup_2026_10_17/t2b_patch_harness_2026_10_16.py` | 7,065 | `bac4775c5c44` | `bac4775c5c44` | `bac4775c5c44` | ✅ |
| 641 | `.tmp/t2b_strategyqa_train_snapshot_2026_10_16.json` | `.tmp/t2b_strategyqa_train_snapshot_2026_10_16.json` | `whitelist_backup_2026_10_17/t2b_strategyqa_train_snapshot_2026_10_16.json` | 4,281,955 | `728e28b7d6bd` | `728e28b7d6bd` | `728e28b7d6bd` | ✅ |
| 642 | `.tmp/t3_baseline_procedure_probe.py` | `.tmp/t3_baseline_procedure_probe.py` | `whitelist_backup_2026_10_17/t3_baseline_procedure_probe.py` | 2,292 | `b4c2a5e68dfa` | `b4c2a5e68dfa` | `b4c2a5e68dfa` | ✅ |
| 643 | `.tmp/t3_baseline_procedure_probe_2026_10_15.json` | `.tmp/t3_baseline_procedure_probe_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_baseline_procedure_probe_2026_10_15.json` | 1,332 | `7ac600d45dcc` | `7ac600d45dcc` | `7ac600d45dcc` | ✅ |
| 644 | `.tmp/t3_freeze_2026_10_15.json` | `.tmp/t3_freeze_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_freeze_2026_10_15.json` | 7,436 | `313f091718cc` | `313f091718cc` | `313f091718cc` | ✅ |
| 645 | `.tmp/t3_harness_diff_2026_10_15.diff` | `.tmp/t3_harness_diff_2026_10_15.diff` | `whitelist_backup_2026_10_17/t3_harness_diff_2026_10_15.diff` | 3,463 | `0f8532aefdff` | `0f8532aefdff` | `0f8532aefdff` | ✅ |
| 646 | `.tmp/t3_nt_llm_calls_2026_10_15.jsonl` | `.tmp/t3_nt_llm_calls_2026_10_15.jsonl` | `whitelist_backup_2026_10_17/t3_nt_llm_calls_2026_10_15.jsonl` | 5,250 | `0cb1decec878` | `0cb1decec878` | `0cb1decec878` | ✅ |
| 647 | `.tmp/t3_nt_measure_2026_10_15.py` | `.tmp/t3_nt_measure_2026_10_15.py` | `whitelist_backup_2026_10_17/t3_nt_measure_2026_10_15.py` | 17,111 | `35860b379b7a` | `35860b379b7a` | `35860b379b7a` | ✅ |
| 648 | `.tmp/t3_nt_measurement_2026_10_15.json` | `.tmp/t3_nt_measurement_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_nt_measurement_2026_10_15.json` | 19,576 | `92f0dc763caf` | `92f0dc763caf` | `92f0dc763caf` | ✅ |
| 649 | `.tmp/t3_nt_verify.py` | `.tmp/t3_nt_verify.py` | `whitelist_backup_2026_10_17/t3_nt_verify.py` | 6,657 | `a1c38dc17d65` | `a1c38dc17d65` | `a1c38dc17d65` | ✅ |
| 650 | `.tmp/t3_nt_verify_2026_10_15.json` | `.tmp/t3_nt_verify_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_nt_verify_2026_10_15.json` | 3,885 | `700de33ee255` | `700de33ee255` | `700de33ee255` | ✅ |
| 651 | `.tmp/t3_postchange_equiv.py` | `.tmp/t3_postchange_equiv.py` | `whitelist_backup_2026_10_17/t3_postchange_equiv.py` | 5,975 | `1e579de6033c` | `1e579de6033c` | `1e579de6033c` | ✅ |
| 652 | `.tmp/t3_postchange_equiv_2026_10_15.json` | `.tmp/t3_postchange_equiv_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_postchange_equiv_2026_10_15.json` | 3,904 | `e8a97dc64a08` | `e8a97dc64a08` | `e8a97dc64a08` | ✅ |
| 653 | `.tmp/t3_postchange_manifest_check_2026_10_15.json` | `.tmp/t3_postchange_manifest_check_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_postchange_manifest_check_2026_10_15.json` | 2,135 | `dbfae4d96b46` | `dbfae4d96b46` | `dbfae4d96b46` | ✅ |
| 654 | `.tmp/t3_postcheck.py` | `.tmp/t3_postcheck.py` | `whitelist_backup_2026_10_17/t3_postcheck.py` | 3,129 | `20c96933b00d` | `20c96933b00d` | `20c96933b00d` | ✅ |
| 655 | `.tmp/t3_prechange_manifest_2026_10_15.json` | `.tmp/t3_prechange_manifest_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_prechange_manifest_2026_10_15.json` | 76,683 | `f1508ebe14e7` | `f1508ebe14e7` | `f1508ebe14e7` | ✅ |
| 656 | `.tmp/t3_prove_minimal_increment_2026_10_15.json` | `.tmp/t3_prove_minimal_increment_2026_10_15.json` | `whitelist_backup_2026_10_17/t3_prove_minimal_increment_2026_10_15.json` | 433 | `3f858f6958cd` | `3f858f6958cd` | `3f858f6958cd` | ✅ |
| 657 | `.tmp/t3_prove_minimal_increment_2026_10_15.py` | `.tmp/t3_prove_minimal_increment_2026_10_15.py` | `whitelist_backup_2026_10_17/t3_prove_minimal_increment_2026_10_15.py` | 7,303 | `1f39cf068862` | `1f39cf068862` | `1f39cf068862` | ✅ |
| 658 | `.tmp/t3_repro_probe_ftfb_freeze_2026_10_16.json` | `.tmp/t3_repro_probe_ftfb_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/t3_repro_probe_ftfb_freeze_2026_10_16.json` | 2,936 | `44761c404b86` | `44761c404b86` | `44761c404b86` | ✅ |
| 659 | `.tmp/t3_repro_probe_llm_calls_2026_10_16.jsonl` | `.tmp/t3_repro_probe_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/t3_repro_probe_llm_calls_2026_10_16.jsonl` | 7,441 | `54ad4d2cd8bf` | `54ad4d2cd8bf` | `54ad4d2cd8bf` | ✅ |
| 660 | `.tmp/t3_repro_probe_measure_2026_10_16.json` | `.tmp/t3_repro_probe_measure_2026_10_16.json` | `whitelist_backup_2026_10_17/t3_repro_probe_measure_2026_10_16.json` | 9,137 | `31779f66c051` | `31779f66c051` | `31779f66c051` | ✅ |
| 661 | `.tmp/t5_baseline_manifest_2026_10_15.json` | `.tmp/t5_baseline_manifest_2026_10_15.json` | `whitelist_backup_2026_10_17/t5_baseline_manifest_2026_10_15.json` | 99,724 | `2d5ad82c0a63` | `2d5ad82c0a63` | `2d5ad82c0a63` | ✅ |
| 662 | `.tmp/t5_harness_diff_2026_10_15.diff` | `.tmp/t5_harness_diff_2026_10_15.diff` | `whitelist_backup_2026_10_17/t5_harness_diff_2026_10_15.diff` | 4,043 | `6f1e9689201b` | `6f1e9689201b` | `6f1e9689201b` | ✅ |
| 663 | `.tmp/t5_kill_line_freeze_2026_10_15.json` | `.tmp/t5_kill_line_freeze_2026_10_15.json` | `whitelist_backup_2026_10_17/t5_kill_line_freeze_2026_10_15.json` | 3,183 | `1910a62c1e9f` | `1910a62c1e9f` | `1910a62c1e9f` | ✅ |
| 664 | `.tmp/t5_nt_llm_calls_2026_10_15.jsonl` | `.tmp/t5_nt_llm_calls_2026_10_15.jsonl` | `whitelist_backup_2026_10_17/t5_nt_llm_calls_2026_10_15.jsonl` | 7,258 | `8e488d14bff6` | `8e488d14bff6` | `8e488d14bff6` | ✅ |
| 665 | `.tmp/t5_nt_measure_2026_10_15.py` | `.tmp/t5_nt_measure_2026_10_15.py` | `whitelist_backup_2026_10_17/t5_nt_measure_2026_10_15.py` | 15,602 | `c96c985d8e23` | `c96c985d8e23` | `c96c985d8e23` | ✅ |
| 666 | `.tmp/t5_nt_measurement_2026_10_15.json` | `.tmp/t5_nt_measurement_2026_10_15.json` | `whitelist_backup_2026_10_17/t5_nt_measurement_2026_10_15.json` | 3,845 | `674e95ecff03` | `674e95ecff03` | `674e95ecff03` | ✅ |
| 667 | `.tmp/t5_prefix_T1T4_digest_2026_10_15.json` | `.tmp/t5_prefix_T1T4_digest_2026_10_15.json` | `whitelist_backup_2026_10_17/t5_prefix_T1T4_digest_2026_10_15.json` | 400 | `9eb43782b73c` | `9eb43782b73c` | `9eb43782b73c` | ✅ |
| 668 | `.tmp/t5_prove_minimal_increment_2026_10_15.py` | `.tmp/t5_prove_minimal_increment_2026_10_15.py` | `whitelist_backup_2026_10_17/t5_prove_minimal_increment_2026_10_15.py` | 6,308 | `65cec9c9788e` | `65cec9c9788e` | `65cec9c9788e` | ✅ |
| 669 | `.tmp/t5_write_docs_2026_10_15.py` | `.tmp/t5_write_docs_2026_10_15.py` | `whitelist_backup_2026_10_17/t5_write_docs_2026_10_15.py` | 47,918 | `f104bf4706e6` | `f104bf4706e6` | `f104bf4706e6` | ✅ |
| 670 | `.tmp/tables.py` | `.tmp/tables.py` | `whitelist_backup_2026_10_17/tables.py` | 1,818 | `02cc157b6d69` | `02cc157b6d69` | `02cc157b6d69` | ✅ |
| 671 | `.tmp/three_seed_caliber_decl_2026_10_16.json` | `.tmp/three_seed_caliber_decl_2026_10_16.json` | `whitelist_backup_2026_10_17/three_seed_caliber_decl_2026_10_16.json` | 4,859 | `5df309d557b0` | `5df309d557b0` | `5df309d557b0` | ✅ |
| 672 | `.tmp/three_seed_collect_2026_10_16.py` | `.tmp/three_seed_collect_2026_10_16.py` | `whitelist_backup_2026_10_17/three_seed_collect_2026_10_16.py` | 28,520 | `672d12ad9801` | `672d12ad9801` | `672d12ad9801` | ✅ |
| 673 | `.tmp/three_seed_collect_log_2026_10_16.txt` | `.tmp/three_seed_collect_log_2026_10_16.txt` | `whitelist_backup_2026_10_17/three_seed_collect_log_2026_10_16.txt` | 16,230 | `55c783261d18` | `55c783261d18` | `55c783261d18` | ✅ |
| 674 | `.tmp/three_seed_freeze_2026_10_16.json` | `.tmp/three_seed_freeze_2026_10_16.json` | `whitelist_backup_2026_10_17/three_seed_freeze_2026_10_16.json` | 10,536 | `46260e3b8426` | `46260e3b8426` | `46260e3b8426` | ✅ |
| 675 | `.tmp/three_seed_llm_calls_2026_10_16.jsonl` | `.tmp/three_seed_llm_calls_2026_10_16.jsonl` | `whitelist_backup_2026_10_17/three_seed_llm_calls_2026_10_16.jsonl` | 104,288 | `5a8cbcf85aa7` | `5a8cbcf85aa7` | `5a8cbcf85aa7` | ✅ |
| 676 | `.tmp/three_seed_measurement_2026_10_16.json` | `.tmp/three_seed_measurement_2026_10_16.json` | `whitelist_backup_2026_10_17/three_seed_measurement_2026_10_16.json` | 226,256 | `ff5ed4b0e329` | `ff5ed4b0e329` | `ff5ed4b0e329` | ✅ |
| 677 | `.tmp/three_seed_preflight_2026_10_16.py` | `.tmp/three_seed_preflight_2026_10_16.py` | `whitelist_backup_2026_10_17/three_seed_preflight_2026_10_16.py` | 5,661 | `98e0e4ae7a73` | `98e0e4ae7a73` | `98e0e4ae7a73` | ✅ |
| 678 | `.tmp/three_seed_verify_2026_10_16.json` | `.tmp/three_seed_verify_2026_10_16.json` | `whitelist_backup_2026_10_17/three_seed_verify_2026_10_16.json` | 3,205 | `61e3d0bfa05d` | `61e3d0bfa05d` | `61e3d0bfa05d` | ✅ |
| 679 | `.tmp/three_seed_verify_2026_10_16.py` | `.tmp/three_seed_verify_2026_10_16.py` | `whitelist_backup_2026_10_17/three_seed_verify_2026_10_16.py` | 13,402 | `5c382ace9573` | `5c382ace9573` | `5c382ace9573` | ✅ |
| 680 | `.tmp/three_seed_write_doc_2026_10_16.py` | `.tmp/three_seed_write_doc_2026_10_16.py` | `whitelist_backup_2026_10_17/three_seed_write_doc_2026_10_16.py` | 50,308 | `f546bdd3630c` | `f546bdd3630c` | `f546bdd3630c` | ✅ |
| 681 | `.tmp/u04_1_chain_verify.py` | `.tmp/u04_1_chain_verify.py` | `whitelist_backup_2026_10_17/u04_1_chain_verify.py` | 4,849 | `13e573534692` | `13e573534692` | `13e573534692` | ✅ |
| 682 | `.tmp/u04_1_dual_verify.py` | `.tmp/u04_1_dual_verify.py` | `whitelist_backup_2026_10_17/u04_1_dual_verify.py` | 3,228 | `f5702456560f` | `f5702456560f` | `f5702456560f` | ✅ |
| 683 | `.tmp/u04_1_make_data.py` | `.tmp/u04_1_make_data.py` | `whitelist_backup_2026_10_17/u04_1_make_data.py` | 19,773 | `309ac58e049d` | `309ac58e049d` | `309ac58e049d` | ✅ |
| 684 | `.tmp/verify_final.py` | `.tmp/verify_final.py` | `whitelist_backup_2026_10_17/verify_final.py` | 805 | `904eb215f139` | `904eb215f139` | `904eb215f139` | ✅ |
| 685 | `.tmp/verify_t3trap_bprime_2026_10_15.py` | `.tmp/verify_t3trap_bprime_2026_10_15.py` | `whitelist_backup_2026_10_17/verify_t3trap_bprime_2026_10_15.py` | 6,928 | `a9e880243eab` | `a9e880243eab` | `a9e880243eab` | ✅ |
| 686 | `.tmp/vk_denominator_2026_10_16.py` | `.tmp/vk_denominator_2026_10_16.py` | `whitelist_backup_2026_10_17/vk_denominator_2026_10_16.py` | 856 | `d935b89bfa31` | `d935b89bfa31` | `d935b89bfa31` | ✅ |
| 687 | `.tmp/vk_interval_arith_2026_10_16.py` | `.tmp/vk_interval_arith_2026_10_16.py` | `whitelist_backup_2026_10_17/vk_interval_arith_2026_10_16.py` | 1,273 | `901d8df83bb3` | `901d8df83bb3` | `901d8df83bb3` | ✅ |
| 688 | `.tmp/vk_v3df_0_1_agree.py` | `.tmp/vk_v3df_0_1_agree.py` | `whitelist_backup_2026_10_17/vk_v3df_0_1_agree.py` | 6,140 | `84c090952894` | `84c090952894` | `84c090952894` | ✅ |
| 689 | `.tmp/vk_v3df_0_1_coverage_gap.py` | `.tmp/vk_v3df_0_1_coverage_gap.py` | `whitelist_backup_2026_10_17/vk_v3df_0_1_coverage_gap.py` | 1,971 | `df25000e7180` | `df25000e7180` | `df25000e7180` | ✅ |
| 690 | `.tmp/vk_v3df_0_1_materiality.py` | `.tmp/vk_v3df_0_1_materiality.py` | `whitelist_backup_2026_10_17/vk_v3df_0_1_materiality.py` | 2,875 | `b666b7a38082` | `b666b7a38082` | `b666b7a38082` | ✅ |
| 691 | `.tmp/vk_v3df_0_1_verify_2026_10_09.py` | `.tmp/vk_v3df_0_1_verify_2026_10_09.py` | `whitelist_backup_2026_10_17/vk_v3df_0_1_verify_2026_10_09.py` | 14,347 | `0e7cb9348a16` | `0e7cb9348a16` | `0e7cb9348a16` | ✅ |
| 692 | `.tmp/vk_verify_2026_10_16.py` | `.tmp/vk_verify_2026_10_16.py` | `whitelist_backup_2026_10_17/vk_verify_2026_10_16.py` | 3,780 | `6ad7edf03032` | `6ad7edf03032` | `6ad7edf03032` | ✅ |
| 693 | `.tmp/vk_verify_interval_ceiling_2026_10_16.py` | `.tmp/vk_verify_interval_ceiling_2026_10_16.py` | `whitelist_backup_2026_10_17/vk_verify_interval_ceiling_2026_10_16.py` | 3,692 | `18b0f12b2c66` | `18b0f12b2c66` | `18b0f12b2c66` | ✅ |
| 694 | `.tmp/vk_write_2026_10_16.py` | `.tmp/vk_write_2026_10_16.py` | `whitelist_backup_2026_10_17/vk_write_2026_10_16.py` | 62,030 | `2334a967a1d4` | `2334a967a1d4` | `2334a967a1d4` | ✅ |
| 695 | `.tmp/vk_write_interval_ceiling_post_lock_2026_10_16.py` | `.tmp/vk_write_interval_ceiling_post_lock_2026_10_16.py` | `whitelist_backup_2026_10_17/vk_write_interval_ceiling_post_lock_2026_10_16.py` | 47,768 | `3076d727e02c` | `3076d727e02c` | `3076d727e02c` | ✅ |
| 696 | `.tmp/write_items_json.py` | `.tmp/write_items_json.py` | `whitelist_backup_2026_10_17/write_items_json.py` | 4,388 | `9dce7986e20d` | `9dce7986e20d` | `9dce7986e20d` | ✅ |
| 697 | `.tmp/write_summary_json.py` | `.tmp/write_summary_json.py` | `whitelist_backup_2026_10_17/write_summary_json.py` | 9,049 | `6214ad3cdc2d` | `6214ad3cdc2d` | `6214ad3cdc2d` | ✅ |
| 698 | `.tmp/write_t3trap_bprime_2026_10_15.py` | `.tmp/write_t3trap_bprime_2026_10_15.py` | `whitelist_backup_2026_10_17/write_t3trap_bprime_2026_10_15.py` | 33,905 | `ca5fc520f530` | `ca5fc520f530` | `ca5fc520f530` | ✅ |
| 699 | `.tmp/_pre_mod/exp_harness_pre.py` | `.tmp/_pre_mod/exp_harness_pre.py` | `whitelist_backup_2026_10_17/_pre_mod/exp_harness_pre.py` | 36,217 | `d5c8d676bb5b` | `d5c8d676bb5b` | `d5c8d676bb5b` | ✅ |

---

## §4 指纹核验之汇总

### §4-1 ① 仓内备份面（**生效** · 本棒改道后之动作）

| 项 | 值 |
| :-- | :-- |
| 复制件数 | **699** |
| 复制 bytes | **38,301,580** |
| **双端 SHA-12 逐位相符** | **699／699**（＝ **100.00%**） |
| 双端 SHA-12 **不符** | **0** |
| **原件事后复验之变更** | **0** |
| 复制前 SHA-12 漂移（跳过） | **0** |
| 复制错误 | **0** |
| **独立第三次复验** | **699／699 相符 · 0 缺失 · 0 不符**（重算双端 · 非复用脚本状态） |

### §4-2 ② 归档区副本（**改道前写入 · 保留原位 · 候 PI 处置**）

| 项 | 值 |
| :-- | :-- |
| 写入件数 | **699** |
| 写入 bytes | **38,301,580** |
| 当时之双端 SHA-12 相符 | **699／699** |
| 不符 | **0** |
| 原件事后复验之变更 | **0** |
| **当前状态** | **保留原位 · ⛔ 0 删除 · 改道后 0 再触**（其去留候 PI · KD-1／KD-2） |

### §4-3 抽样字节级核验（3 件 · 逐位相符）

| 原件（仓内） | bytes | SHA-12（原件） | SHA-12（①） | SHA-12（②） | 相符 |
| :-- | --: | :-- | :-- | :-- | :-: |
| `.tmp/_26b_verdict_prep_hashcheck_2026_10_01.py` | 3,842 | `6927c9462f41` | `6927c9462f41` | `6927c9462f41` | ✅ |
| `.tmp/_26b_verdict_prep_literalcheck_2026_10_01.py` | 4,378 | `50fe799b0a2e` | `50fe799b0a2e` | `50fe799b0a2e` | ✅ |
| `.tmp/_26b_verdict_prep_validate_2026_10_01.py` | 4,640 | `494cca45b873` | `494cca45b873` | `494cca45b873` | ✅ |

---

## §5 阴性结论之三重自审

| # | 阴性断言 | 自审一（怎么证的） | 自审二（反例尝试） | 自审三（阳性对照／残留） |
| :-: | :-- | :-- | :-- | :-- |
| 1 | ⛔ **0 移动** | 复制后**逐件 `open()` 原路径**成功且 SHA-12 不变（`originals_changed` ＝ 0）＋ 独立第三次复验 **699／699 在位** | 若为移动，原路径必不存在 ⇒ 逐件重读成功即证 | **阳性对照**：本棒确曾**写入** 699 件备份件 ⇒ 写入面为实然 |
| 2 | ⛔ **0 删除任何件** | 动作集 ＝ `copy2` ＋ `makedirs` ＋ `io.open(...,'w')`；⛔ 0 `rm`／`unlink`／`rmtree`／`Remove-Item`／`SHFileOperationW` | 复核备份脚本全文 | 回收站 **0** 开启；**归档区已写入之 699 件亦保留原位** |
| 3 | ⚠ **归档区接触（如实）** | 改道**前**写入 699 件（既成事实）；改道**后 0** 次访问 | 若改道后仍有访问，则应有新的读/写时戳 ⇒ 实测 0 | **如实登记**：其去留候 PI，本棒⛔ 0 代裁 |
| 4 | ⛔ **0 上传** | 全程本地文件系统 | 复核：无网络调用 | SHA-256 读数全部来自本机盘面 |
| 5 | ⛔ **0 代 PI 裁** | §2-2 之许可射程与归档区去留**如实列 KD**·未自行裁定 | 主动检索本卡卡号之在盘载体：**0 命中** | 凡 PI 未裁者（许可射程／D-only 边界／归档区去留）**列而 0 裁** |
| 6 | ⛔ **0 撞名** | 仓内备份子面落盘前 `Test-Path` ＝ False（脚本内断言·存在即 `SystemExit` 中止）· 两登记件落盘前 `Test-Path` ×2 ＝ False ＋ `glob` ＝ 0 命中 | —— | ⚠ 本二件之第 2 版系本棒**自更正**（登记件 §10）·非他人写入 |

---

## §6 声明

- ⛔ **0** 回改任何既有件一字；⛔ **0** 移动／重命名／删除任何件；⛔ **0** 上传；⛔ **0** 网络；⛔ **0** 代 PI 裁；⛔ **0** 宣告①毕；⛔ **0** 主张任何项之终判。
- **改道后 ⛔ 0 触归档区**：已写入之 699 件保留原位、去留候 PI。⛔ **0** 回改 `074A6F256655` 一字（**仅被引用**）。
- 本件自身之落盘后字节级指纹**不可内嵌**（写入即变更，自指悖论）；其 bytes／SHA-12／`BOM`／`CR`／`LF`／`TAB`／`U+FFFD`／非 ASCII 之实测值**由交付报承载**。

---

## §7 KD 清单（如实列）

| # | KD 项 | 性质 | 处置 |
| --: | :-- | :-- | :-- |
| **KD-1** | **归档区写入许可射程未及**：许可**仅限**「不上传件归档」之本次归档动作（§5 限制 3·⛔ 0 扩及他目的）⇒ **0 及于**本棒之白名单备份 | 未裁之射程（经 v50 KD-6 揭出） | **目标面已改道仓内 `.tmp`**（⛔ 0 触归档区）；**⛔ 0 自裁**其射程，候 PI 逐单明示 |
| **KD-2** | **归档区已写入 699 件 ／ 38,301,580 B** 待 PI 处置 | 既成事实 | **保留原位 · ⛔ 0 删除 · 改道后 0 再触**；留／清**⛔ 0 代裁** |
| **KD-3** | **要件①之落盘时序**：清单之**落盘载体**（两登记件）晚于复制动作（机读清单载体在先） | 时序缺口 | §2-4 已逐项对照并标注「⚠ 部分时序」；「先于任何**移动**」之触发条件本棒 **0 触发** |
| **KD-4** | **归档区既存内容 0 知**：本棒⛔ **0 列目录**该区，故其既存内容面**未知**（承 `074A6F256655` KD-4 之同一限制） | 如实声明 | 本件所涉该区之陈述**仅限本棒自落之副本**；⛔ **0** 对其余内容作任何陈述 |
| **KD-5** | **备份件之存续风险**：PI 已实证手动清空回收站 **2 次**（`1792206783658` 卡在册载） | 风险面 | 如实登记；**本备份不改变删除判据之任何门槛**（§2-4 之诚实附加） |
| **KD-6** | **备份件对他棒之可见性**：仓内备份面 **699** 件位于清理扫描面之内 | 交叉面风险 | 登记件 §4-3 **保护面登记**为其唯一防护；**请 parent 转达 PI 或相关棒** |

*件止 · **worker**（棒 `WHITELIST-BACKUP-REGISTER`）· 2026-10-17（第 2 版·含改道）· **白名单集之备份映射** —— 口径＝**复制**（⛔ 0 移动·0 删除·0 回收站·**原件一字不动**）｜生效面＝`.tmp/whitelist_backup_2026_10_17/`（699 件／38,301,580 B · 三端 SHA-12 逐位相符 · 原件变更 0）｜⚠ 归档区已写入 699 件·**保留原位·⛔ 0 删·候 PI**｜许可＝**射程未及**（v50 KD-6）·⛔ 0 自裁｜⛔ 0 撞名 · 0 网络 · 0 代裁 · 0 宣告①毕 · 6 项 KD 如实列 · 6 项阴性三重自审）·*
