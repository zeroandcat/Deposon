# `.tmp\whitelist_backup_2026_10_17\` 副本清除面（第二批 · 669 件）— 执行登记件（2026-10-18）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_whitelist_backup_669_cleanup_register_2026_10_18.md` |
| **件性质** | 执行登记件（权源 ＋ 判据冻结 ＋ 逐件清除登记 ＋ 验道证据 ＋ 保留面 ＋ 停手候裁面 ＋ 计数对账 ＋ 字节级自报）· **非判定件** ⇒ ⛔ 0 落五终判 · ⛔ 0 宣告段毕/①毕 · ⛔ 0 代 PI 裁 |
| **权源** | PI 裁 卡 `ask_190ad1b8234cd9916d046aa2` Q1 opt2 · 2026-10-18 12:25:36.627 生效：「授权清 669 件（孪生在 `.tmp` 面者——警：其内容将仅存 `.tmp` 易清面单份）」 |
| **前棒登记件** | `results/_whitelist_backup_470_cleanup_register_2026_10_18.md`（`4b951b0accd9`·14,642 B）·其 R1 669 ／ R2 3 ／ R3 17 三分之复核实测见 §1 |
| **判据冻结件（FTFB）** | `.tmp/_wb669_criteria_freeze_2026_10_18.md` · SHA-256 `13607986e99a836e1e29b9102ed903132cc1186ba5fcdb1610bead550ab973cf` · 9,596 B · **落盘先于本棒任何删除动作**（落盘时已删件数 ＝ 0）· **事后未调** |
| **区域** | 仅 `deposon-repo\.tmp\whitelist_backup_2026_10_17\` 之清除集｜⛔ 0 触 `deposon-sub`、`_remote_pullback_2026_10_17`、`GLM`、`〔归档区〕` |
| **纪律** | ⛔ 0 永久删（`Remove-Item` 不用）· ⛔ 0 联网 · ⛔ 0 读 key · ⛔ 0 回改任何既有件 · ⛔ 0 落五终判 · ⛔ 0 宣告段毕 · ⛔ 0 代 PI 裁 |

---

## §0 一句话结论

清走 **669 件 ／ 37,859,085 B**（= PI 裁之数 = 前棒 R1 之全量，二者件数・字节**逐位全等**），验道 **669/669 全过**（离原位 ＋ D 卷 `$I`/`$R` 成对 ＋ `$I` 偏移 28 解码原路径逐字吻合 ＋ `$R` 载荷 SHA-256 逐位回验 ＋ 尺寸三项一致）。**保留 20 件**：R3 全域唯一存本 **17 件** ＋ R2 零字节 **3 件**。清走后备份树 **20 件 ／ 148,185 B**，与保留面**完全对平**。⚠ 本棒实测 `.tmp` 孪生判据之成立集为 **672** 而非 669，差 **3 件**零字节退化同值之件 —— 本棒**按裁之 669 行、3 件保留**，理由见 §1（未软化，见 §5-H2b）。

---

## §1 冻结时实测前提（逐件 SHA-256 · 1 MiB 分块）

**扫描面**：`deposon-repo\.tmp\` ∖ 备份子树 **1,839** 件 ＋ `results\` 1,156 件 ＋ `_remote_pullback_2026_10_17\` 219 件 ＋ `deposon-sub` 1,276 件 ＋ 备份树 689 件。**读文件失败数 ＝ 0**。

| 口径 | 实测值 | 与前棒／与裁之对照 |
| :-- | --: | :-- |
| 清走前备份树件数 ／ 字节 | **689** ／ **38,007,270** | 与前棒清走后状态**逐位一致**（无漂移） |
| 备份树 distinct SHA | 683（689 件·5 组自身成组） | — |
| **孪生在 `.tmp\` 面且逐位全等者** | **672** ／ 37,859,085 | ⚠ 裁称 669（差 3，见下） |
| ├ 其中**非零字节**（＝真孪生，**本棒清除集**） | **669** ／ **37,859,085** | **与前棒 R1 件数・字节逐位全等** ✅ |
| └ 其中**零字节**（＝退化同值，**本棒保留**） | **3** ／ 0 | ＝ 前棒 R2 之 3 件 |
| `results\` 面残留孪生 | **0** | 与前棒一致（前棒已清走其 10 件） |

### §1-1 「669 vs 672」之 3 件差之实测成因（如实，未软化）

以「`.tmp\` 面有逐位全等之孪生」为判据时，空内容哈希 `e3b0c442…b7852b855` 之下**任一空文件与任一空文件皆逐位全等** ⇒ 下列 3 件（皆 **0 字节**）于 `.tmp\` 面各有 **7** 件同值孪生，于 `_remote_pullback_2026_10_17\` 各另有 **2** 件孪生：

| 件名 | bytes | SHA-256 | `.tmp\` 同值孪生数 | `_remote_pullback` 孪生数 |
| :-- | --: | :-- | --: | --: |
| `_e_q_exec.txt` | 0 | `e3b0c44298fc…52b855` | 7 | 2 |
| `_m5_k5_net.err` | 0 | `e3b0c44298fc…52b855` | 7 | 2 |
| `_m5_k5_scan.err` | 0 | `e3b0c44298fc…52b855` | 7 | 2 |

**故本棒按 669 行、3 件零字节者保留**，理由三条：

1. **PI 裁逐字授权之数为 669**（＝前棒 R1 全体）⇒ 增列 3 件即**超出授权之数**；
2. 该 3 件于前棒系**独立保留类 R2**，其候裁项 **H2 未答** ⇒ 清之即**自裁未答之候裁项**；
3. 其「孪生」成立性系**空内容哈希之退化同值** ⇒ ⛔ 0 以退化同值充作「重复内容」之据。

---

## §2 清除判据之清走时实测（C2 · 冻结件 §2）

| 判据 | 冻结时 | **清走时实测** |
| :-- | --: | --: |
| **C1** 备份件与 `.tmp\` 内（备份子树外）某件逐位全等 | 669 | **669** |
| **C2** 清走时点孪生件**在位且逐位全等**（清走前逐件复验，⛔ 0 以建表旧值代替） | 669 | **669 ／ 669 通过，0 失败** |

📌 C2 实测覆盖：**673 个孪生件**逐件重算 SHA-256（669 目标中 **4** 件各有 2 个孪生，故 669 ＋ 4 ＝ 673）；**清走前**另对 669 目标本身逐件重算，⛔ 0 复用建表值。

---

## §3 可恢复通道之验道（V1–V7 · 逐件 669/669 全过）

| 判据 | 实测结果 |
| :-- | :-- |
| **V1** ⛔ 0 以 `Remove-Item` 永久删 | 全程未用；删除仅经受信启动器顶层单命令 `rm -- <字面目标>` |
| **V2** 通道 | `〔本地路径已脱敏〕`（运行时受信启动器）；裸名调用被安全策略拦阻（且**未删任何件**），改顶层 `rm` 后通行 |
| **V2a** 1 件小样本先验道 | `docwriter_v46_card_raw.txt`（26 B）单独先行，V3/V4/V5/V5-layout/V5-len/V7/size **7/7 全过**后方清其余 668 件 |
| **V3** 目标离原位 | **669 / 669**（`Test-Path` ＝ `False`） |
| **V4** `$I`／`$R` 成对落于 **D 卷** | **669 / 669**（`〔本地路径已脱敏〕`，非 C 卷） |
| **V5** `$I` 偏移 28 解码原路径逐字吻合（区分大小写） | **669 / 669** |
| **V5-layout** `I_len − 28 − pathLen×2 ＝ 0` | **669 / 669** |
| **V5-len** `len(path) ＋ 1 ＝ pathLen`（尾随 NUL 计于 pathLen） | **669 / 669** |
| **V7**（前棒自加）`$R` 载荷 SHA-256 复算 ＝ 清走前 SHA-256 | **669 / 669** |
| **size** `$I` header fileSize ＝ `$R` 实际字节 ＝ 原件字节 | **669 / 669** |
| `$I` version | 全部 **2**（唯一值） |

⚠ **通道 ≠ 兜底**：「凡删除即永久性处置·0 备份兜底」之戒**在册** —— 回收站仅为其**通道**，⛔ **0** 充作备份兜底。本棒 **0 新建任何备份**；清走之 669 件内容之存续**完全依赖**既有 `.tmp\` 孪生（已逐件于清走时点复验在位且逐位全等）。

### §3-1 `$I` 结构实测（本棒之新增教训，与前棒之偏移教训并列）

前棒记「偏移 24 为**字符数** `pathLen`，其字节长度为 `pathLen×2`」。本棒实测再加一条：**`pathLen` 之计数**含**一个尾随 NUL 终止符** —— 即 `len(解码所得路径) ＋ 1 ＝ pathLen`。本棒首次解码时⛔ 未剥该 NUL，致 `$I` 索引键与被清件绝对路径不匹配、V5 误报「无 `$I` 条目」；经原始字节直解（`$I5PP645.txt`：`len`＝190、`pathLen`＝81、`tail`＝162 ＝ 81×2、`layout_ok`＝True、解码得 `…\x00`）定位并改正。**记此以免复犯**。

### §3-2 通道之命令长度上限（本棒实测，如实登记）

首次批量以 **96** 个字面目标发单命令（**8,052 字符**），实际仅落 **47** 件即止（其后目标**未被处理**，非部分删除）。经逐点核算：第 47 目标处命令长 **3,952** 字符、含第 48 目标则 **4,029** 字符 ⇒ 判为**约 4,000 字符之输入上限**，非通道故障（非目标数上限、非 launcher 故障）。据此重按**实际命令长度 ≤ 3,700 字符**重分块（15 块），其后各块除下述 §3-3 一处疏漏外**均整块通过**。📌 中途另有 3 块各被截断于 32–45 件处，**亦系同一上限所致**，已由逐件实测复点捕获并补清（最终 669/669 全过，⛔ 0 遗漏、⛔ 0 越界）。

### §3-3 一处疏漏之如实交代

第 2 块（重分块之 CHUNK 0，标称 44 件）实发 **43** 件 —— 末位目标 `_e48_probe_register.py` 因转录疏漏**未列入该命令**，于下一批**补入并清走**（见 §4 之 #151）。此疏漏**未造成任何越界删除**，且由 §5 之逐件复点实测捕获。

---

## §4 清除集之逐件登记（669 件 · 路径 ＋ SHA-256 ＋ `.tmp\` 孪生 ＋ 验道证据）

`$I`／`$R` 之 `V3V4V5V7` 列中 `V3`＝离原位、`V4`＝`$R` 成对、`V5`＝偏移 28 解码逐字吻合、`V7`＝`$R` 载荷 SHA-256 回验；`尺寸`列 ＝ `$I` fileSize ＝ `$R` 字节 ＝ 原件字节。全部 **669 行皆七项全 ✅**（汇总见 §3）。

| # | 备份件路径（相对备份树） | SHA-256 | bytes | `.tmp\` 孪生路径 | `$I` | `$R` | V3V4V5V7 | 尺寸 |
| --: | :-- | :-- | --: | :-- | :-- | :-- | :-: | :-: |
| 1 | `_26b_verdict_prep_hashcheck_2026_10_01.py` | `6927c9462f412bad848bc6f41b79f6a6bc965c9be706f3292d36d8e46d441b1a` | 3,842 | `_26b_verdict_prep_hashcheck_2026_10_01.py` | `$ICZQKV9.py` | `$RCZQKV9.py` | ✅✅✅✅ | ✅ |
| 2 | `_26b_verdict_prep_literalcheck_2026_10_01.py` | `50fe799b0a2e4f34751682349d9d3fd0550dd2179c746da35cfc312f4cf70669` | 4,378 | `_26b_verdict_prep_literalcheck_2026_10_01.py` | `$IGSPAM0.py` | `$RGSPAM0.py` | ✅✅✅✅ | ✅ |
| 3 | `_26b_verdict_prep_validate_2026_10_01.py` | `494cca45b8736f103c3f64e2aa597a2fbb9b400467d6e01dd12ea5c802e03f6f` | 4,640 | `_26b_verdict_prep_validate_2026_10_01.py` | `$I2YND5N.py` | `$R2YND5N.py` | ✅✅✅✅ | ✅ |
| 4 | `_659_compact.txt` | `795862c09a40535ad362da6111c6758b2afccae22f86d889504add2066c77e10` | 155,628 | `_659_compact.txt` | `$IDBRJGT.txt` | `$RDBRJGT.txt` | ✅✅✅✅ | ✅ |
| 5 | `_659_overlap_digest.txt` | `4f20b8085fb9d9db988b98a2726823f56e97bfcbfe62bca6d311ee7ebe363c9d` | 239,157 | `_659_overlap_digest.txt` | `$I7958B8.txt` | `$R7958B8.txt` | ✅✅✅✅ | ✅ |
| 6 | `_659_report_gen.py` | `cd4b8ed56b2c358c7b9e4962d6373daa6c15d3fd9daf86238f0473152310dbda` | 27,457 | `_659_report_gen.py` | `$IN91235.py` | `$RN91235.py` | ✅✅✅✅ | ✅ |
| 7 | `_abc_diff_2026_10_10.py` | `6d6733f0e5c2b662f02005b338a19dbc29bd65fad8e475a21d530d2e758cf551` | 6,620 | `_abc_diff_2026_10_10.py` | `$ILIHGJA.py` | `$RLIHGJA.py` | ✅✅✅✅ | ✅ |
| 8 | `_abc_final_2026_10_10.py` | `15b4de4fdff6da15c4d5285b4e50f9e7bde357cee91db4429f647af11f13efd3` | 7,329 | `_abc_final_2026_10_10.py` | `$IIGL3K7.py` | `$RIGL3K7.py` | ✅✅✅✅ | ✅ |
| 9 | `_abc_h1h2_2026_10_10.py` | `16f19bad301f98372957a4ec598e89226d5635618113f9c31d2cd83176187c73` | 7,889 | `_abc_h1h2_2026_10_10.py` | `$I6GAXIM.py` | `$R6GAXIM.py` | ✅✅✅✅ | ✅ |
| 10 | `_abc_readings_reprocheck_2026_10_10.py` | `0ec2a2bf3bab974031390ecb10c252c194dab0c99ebe3ee9aae6e4aa5202a603` | 9,491 | `_abc_readings_reprocheck_2026_10_10.py` | `$IE2OZMH.py` | `$RE2OZMH.py` | ✅✅✅✅ | ✅ |
| 11 | `_abc_readings_reprocheck_out_2026_10_10.json` | `2f9aa16b63cad5b989d8331f2cfe69ba8a394b808f866184f56341dd1618c53a` | 78,436 | `_abc_readings_reprocheck_out_2026_10_10.json` | `$ILQGYLK.json` | `$RLQGYLK.json` | ✅✅✅✅ | ✅ |
| 12 | `_abc_rfd_2026_10_10.py` | `39268ca6adffd3dd4f6930de780660b58b2e1cc0ab4cdcf791cf6f6e65e7c33b` | 5,938 | `_abc_rfd_2026_10_10.py` | `$I5ETXUB.py` | `$R5ETXUB.py` | ✅✅✅✅ | ✅ |
| 13 | `_aggregate_10cells.py` | `3bdc6250d0f2213ad1be9b24edb23ad8578e0b6e1f6b2f963abbb9fa9f88cb6e` | 3,009 | `_aggregate_10cells.py` | `$I2D3SHA.py` | `$R2D3SHA.py` | ✅✅✅✅ | ✅ |
| 14 | `_aggregate_10cells_v2.py` | `af1b7f09f74d0d9f93101557832780c82ddda80231d47e75a14bb76e84dbdea0` | 5,131 | `_aggregate_10cells_v2.py` | `$IJSVPED.py` | `$RJSVPED.py` | ✅✅✅✅ | ✅ |
| 15 | `_aggregate_10cells_v3.py` | `04b127d80bf0d95485702512dc4dfea1e788c0778c8253cea714cc90c92e3fd7` | 2,969 | `_aggregate_10cells_v3.py` | `$IBKLSP8.py` | `$RBKLSP8.py` | ✅✅✅✅ | ✅ |
| 16 | `_aggregate_10cells_v4.py` | `f99a3765c3c31d6255b851d50e02ea36f356f5e6f40402b864d1904eaa686462` | 2,454 | `_aggregate_10cells_v4.py` | `$IWORMT7.py` | `$RWORMT7.py` | ✅✅✅✅ | ✅ |
| 17 | `_append_intake_supplement_6_tail.py` | `c3339682d68ce0e540b3cf8a9a469dbb7f173b72c07012f2a29fdbe4bc8a24e7` | 9,335 | `_append_intake_supplement_6_tail.py` | `$IA8KXFH.py` | `$RA8KXFH.py` | ✅✅✅✅ | ✅ |
| 18 | `_audit3b.txt` | `e64565a2b1808ad576caf9490792f625509959a88a3e5360b59e7196ece65bac` | 50,554 | `_audit3b.txt` | `$IP66SXW.txt` | `$RP66SXW.txt` | ✅✅✅✅ | ✅ |
| 19 | `_audit_part3_out.txt` | `85a9d9861d38eef3ed1d7ddfc12ba05e9c635db70d110b8a2af55ad80eb04cb4` | 5,195 | `_audit_part3_out.txt` | `$IRNUXPZ.txt` | `$RRNUXPZ.txt` | ✅✅✅✅ | ✅ |
| 20 | `_audit_part4.txt` | `def27c1c35116943cc5f4a60225fdd1d3362a4d013fbdaca74df07620b11733c` | 14,826 | `_audit_part4.txt` | `$INAEZBC.txt` | `$RNAEZBC.txt` | ✅✅✅✅ | ✅ |
| 21 | `_b12_q1_refs_2026_09_29.py` | `86b2d9b7b7bd062648d42dea89c564b23bee15b03959449b10416b5dc6d0f9ad` | 4,890 | `_b12_q1_refs_2026_09_29.py` | `$IUPFB55.py` | `$RUPFB55.py` | ✅✅✅✅ | ✅ |
| 22 | `_b12_q1_timeslice_2026_09_29.py` | `bacf6379b9bf02b9ef6473c67b29d95f69c2773663865dbe2f067e689c0784a9` | 798 | `_b12_q1_timeslice_2026_09_29.py` | `$I9DH8S8.py` | `$R9DH8S8.py` | ✅✅✅✅ | ✅ |
| 23 | `_b12_q4_adjacent_2026_09_29.py` | `61cbc9965896b2d6a5eae7a8a2bc4efe101f7851fb67df6809aec2db086669df` | 5,709 | `_b12_q4_adjacent_2026_09_29.py` | `$IHRE6Z7.py` | `$RHRE6Z7.py` | ✅✅✅✅ | ✅ |
| 24 | `_b12_q4_exact_2026_09_29.py` | `79eba6136d83131bc6eddff0735c101a8b7f9e3286e09d741b851d3892fc1150` | 7,140 | `_b12_q4_exact_2026_09_29.py` | `$IBUG15Y.py` | `$RBUG15Y.py` | ✅✅✅✅ | ✅ |
| 25 | `_b12_q4_formcand_2026_09_29.py` | `f58f388996d4bbf1605dc0e6dfd461a3e23f6445e515bb846ef9ee36b1a0e279` | 6,510 | `_b12_q4_formcand_2026_09_29.py` | `$IOA0RLY.py` | `$ROA0RLY.py` | ✅✅✅✅ | ✅ |
| 26 | `_b12_tables_2026_09_29.py` | `10db58be72cf3c5bb05a13d5313afaeaab8922dc173525a46be474796c933e40` | 1,907 | `_b12_tables_2026_09_29.py` | `$IJUPX4A.py` | `$RJUPX4A.py` | ✅✅✅✅ | ✅ |
| 27 | `_build_5anchor_json_draft.py` | `391e7a1be0e53850529f7ac03473dc9419f652328b3805ec4969053526cc8475` | 34,455 | `_build_5anchor_json_draft.py` | `$IUUMYDH.py` | `$RUUMYDH.py` | ✅✅✅✅ | ✅ |
| 28 | `_build_5anchor_json_v1.py` | `56c459492ecf2e2329d05b95367343ff34fff3f7c2403325ce5e96df66631022` | 11,627 | `_build_5anchor_json_v1.py` | `$I6ZKOXT.py` | `$R6ZKOXT.py` | ✅✅✅✅ | ✅ |
| 29 | `_build_intake_supplement_6.py` | `6336456853ae320470105e859734840bc4c08c2cb5a218350aa3a7e18c3dbc2d` | 13,094 | `_build_intake_supplement_6.py` | `$IY6RR83.py` | `$RY6RR83.py` | ✅✅✅✅ | ✅ |
| 30 | `_build_receipt_supplement_6.py` | `20c44c665b4ffbadeb55f77c83cc8bf005873b4c46e632e54eee093f043e5dec` | 11,430 | `_build_receipt_supplement_6.py` | `$IH7BDUT.py` | `$RH7BDUT.py` | ✅✅✅✅ | ✅ |
| 31 | `_c5_b3_rewalk_postcheck_2026_10_01.py` | `aca7dad6ddfa976c51ee1ec8b0912328e7e3b5f1530f280ec4da302bd310d515` | 2,249 | `_c5_b3_rewalk_postcheck_2026_10_01.py` | `$I7FERM9.py` | `$R7FERM9.py` | ✅✅✅✅ | ✅ |
| 32 | `_c5_b3_rewalk_precheck_2026_10_01.py` | `4aad531a2ddb888c46f0484f0e0f3334573de3059a3d1f2c5ab3ab816f84554b` | 2,035 | `_c5_b3_rewalk_precheck_2026_10_01.py` | `$IFXRUVW.py` | `$RFXRUVW.py` | ✅✅✅✅ | ✅ |
| 33 | `_c5_b3_rewalk_utf8check_2026_10_01.py` | `5488ff2db11f76d06b4ab6a5b8b5d02604ac812bfd17199a7dd0b67dc55567bf` | 925 | `_c5_b3_rewalk_utf8check_2026_10_01.py` | `$I0QEYI8.py` | `$R0QEYI8.py` | ✅✅✅✅ | ✅ |
| 34 | `_c5_b_group_fix_readings_2026_10_09.py` | `b6855b38acc2a20dfdcaba2bd85863ee8322e0eec0b78b3f565c63c90342f630` | 12,289 | `_c5_b_group_fix_readings_2026_10_09.py` | `$ILSH6V1.py` | `$RLSH6V1.py` | ✅✅✅✅ | ✅ |
| 35 | `_c5_feasibility_probe.py` | `d730612b0c9ac0f1db695ec2104c2d610adbf816ee4d9cc11e9ea3a3990dc4d9` | 1,036 | `_c5_feasibility_probe.py` | `$IYLRJNW.py` | `$RYLRJNW.py` | ✅✅✅✅ | ✅ |
| 36 | `_canonical_census.py` | `36b7af564c56c16c970d87c4fb6a2479499a14ebfc8bb4c433a286ee9b18bde9` | 4,382 | `_canonical_census.py` | `$I8FYFAE.py` | `$R8FYFAE.py` | ✅✅✅✅ | ✅ |
| 37 | `_canonical_lines.json` | `9b0997fc7e527af9d75fa635b3c2451eaa6dd8293f740b5a16e6bce7711c1994` | 15,033 | `_canonical_lines.json` | `$IE6R2SL.json` | `$RE6R2SL.json` | ✅✅✅✅ | ✅ |
| 38 | `_canonical_lines.py` | `08aa8638a0b239863a1014591a5f361f7ca0eeb30cc8ab535dcea3af9f297395` | 3,354 | `_canonical_lines.py` | `$IUYTSXA.py` | `$RUYTSXA.py` | ✅✅✅✅ | ✅ |
| 39 | `_check_escape.py` | `5f026b0baf3918046574d3b842167a2614cbf9e4397f65b5d4eaed8f555e9806` | 332 | `_check_escape.py` | `$ILA06J7.py` | `$RLA06J7.py` | ✅✅✅✅ | ✅ |
| 40 | `_check_kimi_sides.py` | `4f3291959a6d90384fb5bf7cd806d6f794f54d06affc58165aa71af5c786cd67` | 1,459 | `_check_kimi_sides.py` | `$I2GRVOW.py` | `$R2GRVOW.py` | ✅✅✅✅ | ✅ |
| 41 | `_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | `b0cf9baba64b935b273f610cdddc08183c54412c9cbcdb464da72a09e26a4373` | 20,997 | `_ci_gap_fill_alt_bc_aper_prime_2026_10_09.py` | `$I33O9L7.py` | `$R33O9L7.py` | ✅✅✅✅ | ✅ |
| 42 | `_cleanup_r2_cleanlist.json` | `ce71dda2815702c5a82314f0dd0936851c1859060f7d2e1b25a023fd675c5d9d` | 810 | `_cleanup_r2_cleanlist.json` | `$I0U0O0H.json` | `$R0U0O0H.json` | ✅✅✅✅ | ✅ |
| 43 | `_cleanup_r2_exec.py` | `a2029c340ac54f31cae660e417dd98f441f9d6952b802b7ff41aa746969e4d75` | 7,884 | `_cleanup_r2_exec.py` | `$IISCOBN.py` | `$RISCOBN.py` | ✅✅✅✅ | ✅ |
| 44 | `_cleanup_r2_exec_journal.json` | `cd636cb6481385c9cc27127ac6ea3e633c8eb14c38d3075d940ab2701d2c306e` | 10,327 | `_cleanup_r2_exec_journal.json` | `$IVL9Z6C.json` | `$RVL9Z6C.json` | ✅✅✅✅ | ✅ |
| 45 | `_cleanup_r2_postcheck.json` | `720b25650bcd27408c327e440e8fe6d8e473d4f006fc3a97b153f1aca76b6702` | 6,652 | `_cleanup_r2_postcheck.json` | `$I049F9C.json` | `$R049F9C.json` | ✅✅✅✅ | ✅ |
| 46 | `_cleanup_r2_postcheck.py` | `cfd60493f18d0cd1b79b36a05e6d8b3641609fa8f99b57da348ac6b61f9e3cf7` | 4,585 | `_cleanup_r2_postcheck.py` | `$IZQBVD0.py` | `$RZQBVD0.py` | ✅✅✅✅ | ✅ |
| 47 | `_cleanup_r2_scan.py` | `60d6d3d370768fb8d74bf33dd867df04382150a1a40c755fab3a2bb772f92708` | 11,507 | `_cleanup_r2_scan.py` | `$IVEFERW.py` | `$RVEFERW.py` | ✅✅✅✅ | ✅ |
| 48 | `_cleanup_r2_scan2.py` | `7019c7b8d7283f78e781174aa29d39386f84bb3072be0189919e61f288c3dab5` | 12,112 | `_cleanup_r2_scan2.py` | `$ISQL2HL.py` | `$RSQL2HL.py` | ✅✅✅✅ | ✅ |
| 49 | `_cleanup_r2_scan3.py` | `46b7b8230e86be34f2fc5a72260995f45a6d1e2998f4451d7900d2c5e2525c80` | 12,389 | `_cleanup_r2_scan3.py` | `$I2VHRV6.py` | `$R2VHRV6.py` | ✅✅✅✅ | ✅ |
| 50 | `_cleanup_r2_scan_out.json` | `3b107c0784904c524b47537135fc22968a8df02487c5b72d961badd24d985a45` | 758,995 | `_cleanup_r2_scan_out.json` | `$I0TP26K.json` | `$R0TP26K.json` | ✅✅✅✅ | ✅ |
| 51 | `_compute_metrics.py` | `ae2b0142b09e20cf5df2c41f7a56305d55465eb6b227b177ff08cef02be55039` | 7,752 | `_compute_metrics.py` | `$IKXJUV4.py` | `$RKXJUV4.py` | ✅✅✅✅ | ✅ |
| 52 | `_compute_metrics_v2.py` | `0620ef317e8a4c78562e2a292dfac644c7b1dd28c776f62edc91583e1f4ff52b` | 8,017 | `_compute_metrics_v2.py` | `$IK347FT.py` | `$RK347FT.py` | ✅✅✅✅ | ✅ |
| 53 | `_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | `3a240806c2d33447b47aecc4dd9e03649af17307b19a4ecb593b019c39da8a24` | 31,745 | `_corrupt_ge01_readiness_firstwrite_2026_10_13.md` | `$IPDCRMV.md` | `$RPDCRMV.md` | ✅✅✅✅ | ✅ |
| 54 | `_cpatomic_dump_pyc_2026_09_28.py` | `d7c9ac28b0963bac1796b76f6d6ceba5c6d3d3cea6739168a295204de96b1507` | 468 | `_cpatomic_dump_pyc_2026_09_28.py` | `$I52A890.py` | `$R52A890.py` | ✅✅✅✅ | ✅ |
| 55 | `_cpatomic_keyscan_2026_09_28.py` | `393a8d3fa68f60535d17ec9343a30e3e454d5828f28a84ccc713590b29d359c0` | 3,074 | `_cpatomic_keyscan_2026_09_28.py` | `$IQL9CD9.py` | `$RQL9CD9.py` | ✅✅✅✅ | ✅ |
| 56 | `_cpatomic_make_fix_2026_09_28.py` | `76c822b640a0d6e4886c5822c357fe1605b1cb4f3593c51721fad57b7a28224b` | 7,796 | `_cpatomic_make_fix_2026_09_28.py` | `$IYO7TW6.py` | `$RYO7TW6.py` | ✅✅✅✅ | ✅ |
| 57 | `_cpatomic_pycache_post_2026_09_28.py` | `171b2a31c0e1625c0a916f4cee51a7c99c8ceb8c537d9f72fc28b1e55cc2c90f` | 5,164 | `_cpatomic_pycache_post_2026_09_28.py` | `$IMOPM95.py` | `$RMOPM95.py` | ✅✅✅✅ | ✅ |
| 58 | `_cpatomic_pycache_pre_2026_09_28.py` | `b86619676bf4db1aa70adf3f24f599eeb898057391c874780171db00e83cf673` | 3,912 | `_cpatomic_pycache_pre_2026_09_28.py` | `$IL4HC8B.py` | `$RL4HC8B.py` | ✅✅✅✅ | ✅ |
| 59 | `_cpatomic_register_2026_09_28.json` | `b68d7ff817bb32beecb9c6db3bfa6e0e4b39f84e046a9107a0bff430d5dddc66` | 29,361 | `_cpatomic_register_2026_09_28.json` | `$IA7A7TH.json` | `$RA7A7TH.json` | ✅✅✅✅ | ✅ |
| 60 | `_cpatomic_register_2026_09_28.py` | `98fe9fa24e80509e156c503f61e85e0f2b0c15f2418372f50d02d8cbd2d7510b` | 6,322 | `_cpatomic_register_2026_09_28.py` | `$I7CIRDK.py` | `$R7CIRDK.py` | ✅✅✅✅ | ✅ |
| 61 | `_cpatomic_verify_2026_09_28.py` | `85139011457c17b3804e15018a24070f3f8cbc1535b3cb86831b2e31e970900b` | 11,036 | `_cpatomic_verify_2026_09_28.py` | `$IEN167F.py` | `$REN167F.py` | ✅✅✅✅ | ✅ |
| 62 | `_crosscheck_messages_35_48.py` | `dcfe4835948856ddb73dc5354dab86d057de287912b10553029ff61b52a7aadc` | 1,608 | `_crosscheck_messages_35_48.py` | `$IPQZDKC.py` | `$RPQZDKC.py` | ✅✅✅✅ | ✅ |
| 63 | `_d05_b_coincidence_checks_2026_10_10.py` | `c1fc428d450c9081672cfc27e01c966a0ada04242c9a63eb9b04f01dd08e67ab` | 22,078 | `_d05_b_coincidence_checks_2026_10_10.py` | `$IQ2B89T.py` | `$RQ2B89T.py` | ✅✅✅✅ | ✅ |
| 64 | `_d05_caliber_2026_10_10.py` | `65cb84529cb21d2fc6b870724bb07885015191921f347c28694422b4cf0fc210` | 8,011 | `_d05_caliber_2026_10_10.py` | `$IJNIWU2.py` | `$RJNIWU2.py` | ✅✅✅✅ | ✅ |
| 65 | `_d05_instrument_audit.py` | `edfa99486954c1c737bb00423c9e6ad85a5650f7d12846e044eb7805f35b4dd0` | 5,948 | `_d05_instrument_audit.py` | `$IQF9LHH.py` | `$RQF9LHH.py` | ✅✅✅✅ | ✅ |
| 66 | `_d05_s4only_2026_10_10.py` | `802069e2c06ec00c9481fb8927fd953e046382a9271e0de0c485ce1710e6682e` | 3,438 | `_d05_s4only_2026_10_10.py` | `$I5YGBBH.py` | `$R5YGBBH.py` | ✅✅✅✅ | ✅ |
| 67 | `_d05_three_checks_recheck_2026_10_10.py` | `fc1201cb71e79824da58eae0cc605abd642fd964d87abd24743fd5bb88efa9a5` | 11,134 | `_d05_three_checks_recheck_2026_10_10.py` | `$I6HI49T.py` | `$R6HI49T.py` | ✅✅✅✅ | ✅ |
| 68 | `_d05_three_checks_recheck_out_2026_10_10.json` | `4eb425260682a257b679f28635359e564b10552a82846528f7f15ba5493707f3` | 3,622 | `_d05_three_checks_recheck_out_2026_10_10.json` | `$I0XCI63.json` | `$R0XCI63.json` | ✅✅✅✅ | ✅ |
| 69 | `_diff21_anchor_drift.py` | `de2a99cf199977f6e40fd5a369024232f807311a46da2a147be307af39a95593` | 960 | `_diff21_anchor_drift.py` | `$IQ3RTRG.py` | `$RQ3RTRG.py` | ✅✅✅✅ | ✅ |
| 70 | `_docwriter_night_headers.txt` | `729875e7999e5af4455b5a300d3cfd18a913718d971e31dd9e49d84a2e94b088` | 52,370 | `_docwriter_night_headers.txt` | `$IED3XFL.txt` | `$RED3XFL.txt` | ✅✅✅✅ | ✅ |
| 71 | `_docwriter_night_measure.json` | `f5bacfac3f1cfc758025123c8b354de1730720c95dbe7ee463782516f52e0379` | 22,679 | `_docwriter_night_measure.json` | `$IIR6RKN.json` | `$RIR6RKN.json` | ✅✅✅✅ | ✅ |
| 72 | `_docwriter_q4_l117_append_block.md` | `7c7d633047e425fd8ec38b8b8212466fa2c29b036a7a0341bc9ebf6607d2019f` | 4,857 | `_docwriter_q4_l117_append_block.md` | `$IKQCS0L.md` | `$RKQCS0L.md` | ✅✅✅✅ | ✅ |
| 73 | `_docwriter_recheck.py` | `54b522e4e2fe723120cc1daf37b9e3c997060f1d98d4cf611a7046bc396cd2af` | 2,374 | `_docwriter_recheck.py` | `$IEF94V0.py` | `$REF94V0.py` | ✅✅✅✅ | ✅ |
| 74 | `_docwriter_write_handover.py` | `a553d705a482401a0175ffb7128fbc4d26ab6bf29a6626c23907d85601d150e9` | 49,400 | `_docwriter_write_handover.py` | `$I8S9MSQ.py` | `$R8S9MSQ.py` | ✅✅✅✅ | ✅ |
| 75 | `_dump_dkb3_records2_2026_10_10.py` | `e71d1e81da64d66e7451acd85ec0fe276dc022c205551d7785c1bf29afedbb7e` | 1,366 | `_dump_dkb3_records2_2026_10_10.py` | `$IF1XML5.py` | `$RF1XML5.py` | ✅✅✅✅ | ✅ |
| 76 | `_dump_dkb3_records_2026_10_10.py` | `144b204237bffd798667f6069365b4457027efb5ae2603ec8690cdc94f6a5440` | 1,781 | `_dump_dkb3_records_2026_10_10.py` | `$I48QD7S.py` | `$R48QD7S.py` | ✅✅✅✅ | ✅ |
| 77 | `_dup_name_diff_content_scan2_2026_10_08.py` | `b3fe206ef866e0841e810c2fc6a15111dea01da169bdcf73f2fa9826105f03a0` | 7,547 | `_dup_name_diff_content_scan2_2026_10_08.py` | `$IUX2WAO.py` | `$RUX2WAO.py` | ✅✅✅✅ | ✅ |
| 78 | `_dup_name_diff_content_scan_2026_10_08.py` | `675cc3136e70cc1d742a1f57cc9509d1caf57fde61fe02785e0d27f8d79e2e49` | 4,519 | `_dup_name_diff_content_scan_2026_10_08.py` | `$I41BV0V.py` | `$R41BV0V.py` | ✅✅✅✅ | ✅ |
| 79 | `_dw_abs_scan.json` | `5c584826ed161e7c681ddbf33ab0edc3d1c9a6943bd57b7af90b50488ff79719` | 56,306 | `_dw_abs_scan.json` | `$ITN4RUT.json` | `$RTN4RUT.json` | ✅✅✅✅ | ✅ |
| 80 | `_e47_docwriter_count.py` | `33cc563b947197ade577bec6491f01bd70c8b879679c0f56b8ccd0d2ae06fc00` | 1,124 | `_e47_docwriter_count.py` | `$IZFHTPP.py` | `$RZFHTPP.py` | ✅✅✅✅ | ✅ |
| 81 | `_e48_apply.py` | `d4e6f0934e5fc83b2ed31ff5c0c8ea908304ba168c640429c780e3cbc990c2d3` | 2,329 | `_e48_apply.py` | `$IA84RCB.py` | `$RA84RCB.py` | ✅✅✅✅ | ✅ |
| 82 | `_e48_c1.md` | `c2a814a90330131600138659006e8e3e2fda1e4ed23e864377149e3a65c89ff9` | 5,039 | `_e48_c1.md` | `$IPS6AIX.md` | `$RPS6AIX.md` | ✅✅✅✅ | ✅ |
| 83 | `_e48_c2.md` | `4d3cae4cbcc0140537da2f221c3eedacc0dec845d80f512e45da15ce86967484` | 5,966 | `_e48_c2.md` | `$I39L7IR.md` | `$R39L7IR.md` | ✅✅✅✅ | ✅ |
| 84 | `_e48_c3.md` | `769c714754045bb6ba45bf1362e8f6bb87a34b3dca242823f61a6941c4063e0d` | 6,563 | `_e48_c3.md` | `$IMMIJFG.md` | `$RMMIJFG.md` | ✅✅✅✅ | ✅ |
| 85 | `_e48_c4.md` | `8143d01ca0e1eaf8bac0da8255447c20977fe787bd105261219054e05acb681d` | 21,710 | `_e48_c4.md` | `$IQ15P4N.md` | `$RQ15P4N.md` | ✅✅✅✅ | ✅ |
| 86 | `_e48_c5.md` | `2f7ab971f69184f24f01f56cb30cb6a1a9364eaacf934e069510ec03e6738061` | 1,686 | `_e48_c5.md` | `$IKSXSNS.md` | `$RKSXSNS.md` | ✅✅✅✅ | ✅ |
| 87 | `_e48_docwriter_chain.py` | `da5e16e02b7dc388568b88f8e23cf9d2374fb3b475033e5e4b99568521be4141` | 2,550 | `_e48_docwriter_chain.py` | `$I15CN0O.py` | `$R15CN0O.py` | ✅✅✅✅ | ✅ |
| 88 | `_e48_docwriter_enum.py` | `80bad142f13d376ef23de14b983fa47b7d58d284348c957e037cc2f2605ad8e8` | 1,248 | `_e48_docwriter_enum.py` | `$IEVOL6N.py` | `$REVOL6N.py` | ✅✅✅✅ | ✅ |
| 89 | `_e48_docwriter_hash.py` | `4656b3b734c52373a81a660e47c43f7369234296a9609c76c03ff6b71362d94f` | 2,578 | `_e48_docwriter_hash.py` | `$I0XESO9.py` | `$R0XESO9.py` | ✅✅✅✅ | ✅ |
| 90 | `_e48_docwriter_hash2.py` | `9a3c5b05e29ef3347e941808040df60660ae7d76b8204759b24622305162b7a5` | 1,229 | `_e48_docwriter_hash2.py` | `$IFUGV5G.py` | `$RFUGV5G.py` | ✅✅✅✅ | ✅ |
| 91 | `_e48_probe_register.py` | `d92f74712dabc45a3fa2e4cd03fa205138e56ef44a90070b0a653b95d0881dae` | 873 | `_e48_probe_register.py` | `$I8T70WQ.py` | `$R8T70WQ.py` | ✅✅✅✅ | ✅ |
| 92 | `_e49_c1.md` | `1e6e30d4ce4d4688b6d260456c35fc73a8459885f68fe499b80cb59abfe1ccd2` | 13,607 | `_e49_c1.md` | `$IL2ZXTF.md` | `$RL2ZXTF.md` | ✅✅✅✅ | ✅ |
| 93 | `_e49_c2.md` | `11beaed14ea7b470c7fcfeb70ba4ce25939accb80513ff6505574cd41c6ca8da` | 17,872 | `_e49_c2.md` | `$IML2ETK.md` | `$RML2ETK.md` | ✅✅✅✅ | ✅ |
| 94 | `_e6_alt_permp_closure_analysis_2026_10_10.py` | `affabef74de40f12757bf07d409dff3a31cc6950321c109087300f9d1062371b` | 2,736 | `_e6_alt_permp_closure_analysis_2026_10_10.py` | `$I3XNG03.py` | `$R3XNG03.py` | ✅✅✅✅ | ✅ |
| 95 | `_e6_alt_permp_closure_runner_2026_10_10.py` | `9bb254aa58a983db7483eef8fd061bf6c934326bb6ca29efcd7bedd5c851044c` | 9,985 | `_e6_alt_permp_closure_runner_2026_10_10.py` | `$IY8TCSN.py` | `$RY8TCSN.py` | ✅✅✅✅ | ✅ |
| 96 | `_e6_ndjt_recompute_2026_10_10.py` | `59c2d618305feeddfceac2962d736b62cf15a266afa0585473dda9d5878cd55f` | 5,064 | `_e6_ndjt_recompute_2026_10_10.py` | `$II21DYT.py` | `$RI21DYT.py` | ✅✅✅✅ | ✅ |
| 97 | `_e_q_doc.md` | `71f5a0769dab936f0cb33d631d17977bfa2ed6f84a2d63ad30ea7ebd0f4b56d5` | 28,259 | `_e_q_doc.md` | `$I6PV2Q2.md` | `$R6PV2Q2.md` | ✅✅✅✅ | ✅ |
| 98 | `_e_q_exec.json` | `d4bd8c92201fb706d2dbe5eec628b9724869f2ee79a8468f056316ec81dc8d20` | 6,161 | `_e_q_exec.json` | `$ITHFOKI.json` | `$RTHFOKI.json` | ✅✅✅✅ | ✅ |
| 99 | `_ea_179_domain_retest_2026_10_09.py` | `9309e4977b224e9dbd97dac2bf12e70f368dc951cc0c457680968468a370e1a5` | 2,814 | `_ea_179_domain_retest_2026_10_09.py` | `$IKUUPYS.py` | `$RKUUPYS.py` | ✅✅✅✅ | ✅ |
| 100 | `_ecr_pa_a0_recompute_2026_10_15.py` | `92e204d66c84f39f9b1bce62162eaf5d8591e9527c69d74959838b1a577228d8` | 8,804 | `_ecr_pa_a0_recompute_2026_10_15.py` | `$IZQ30E0.py` | `$RZQ30E0.py` | ✅✅✅✅ | ✅ |
| 101 | `_en_final_2026_09_28.py` | `97a05aace5a832a0576af8bf6b5b9903b7c6a2d35274a217c0631c2d20084db6` | 2,369 | `_en_final_2026_09_28.py` | `$IILCJNB.py` | `$RILCJNB.py` | ✅✅✅✅ | ✅ |
| 102 | `_en_verify2_2026_09_28.py` | `7e84e75cb838fe15c7c4b348cc6ae06715e4c1fe6630df512ddfe288af42c5ad` | 1,870 | `_en_verify2_2026_09_28.py` | `$IYLOMW2.py` | `$RYLOMW2.py` | ✅✅✅✅ | ✅ |
| 103 | `_en_verify3_2026_09_28.py` | `658292cce916704bc50a70f334ac811a525610bf41e569a06789f5ba439ac1e2` | 1,638 | `_en_verify3_2026_09_28.py` | `$ILGZVS3.py` | `$RLGZVS3.py` | ✅✅✅✅ | ✅ |
| 104 | `_en_verify4_2026_09_28.py` | `7eaeb9b4ba483c2eec5e9f22154cd09c8412248f321b369f6b1afc6522f8e112` | 1,484 | `_en_verify4_2026_09_28.py` | `$IPJ4MHE.py` | `$RPJ4MHE.py` | ✅✅✅✅ | ✅ |
| 105 | `_en_verify_2026_09_28.py` | `51d9410d459b9ecc6d769c27fabc065a1b9943016008723a621f6e62f30c4f60` | 6,071 | `_en_verify_2026_09_28.py` | `$I0GSNLO.py` | `$R0GSNLO.py` | ✅✅✅✅ | ✅ |
| 106 | `_execswitch_verify_2026_09_28.py` | `0814f3c2d7ab7430eb6ddd3d3af42958ca72876270eafa792e2009b46b788a30` | 3,501 | `_execswitch_verify_2026_09_28.py` | `$I983TDC.py` | `$R983TDC.py` | ✅✅✅✅ | ✅ |
| 107 | `_final_check.py` | `ee7f008d36cbc46a56b17b20853280430c78d3bb01a0601372599ef6bf7a209f` | 1,562 | `_final_check.py` | `$IY72H1J.py` | `$RY72H1J.py` | ✅✅✅✅ | ✅ |
| 108 | `_final_sha.py` | `8ea91ad82b9d96b0325d20794999af16e1c89b98fb1c8372626eb2ec2f5158b8` | 1,435 | `_final_sha.py` | `$IU5VSOL.py` | `$RU5VSOL.py` | ✅✅✅✅ | ✅ |
| 109 | `_final_verify.py` | `88aad6650405f319fd44111c0a097f86bf2d311fe8b9f8fec2f17e8ffdc0f383` | 2,457 | `_final_verify.py` | `$ISKRE4H.py` | `$RSKRE4H.py` | ✅✅✅✅ | ✅ |
| 110 | `_ge01_g7_register_build.py` | `7731337a516df2347d308f83a26d981b55c3b65b21c73f8939652dc9d0d39429` | 33,147 | `_ge01_g7_register_build.py` | `$I60SY10.py` | `$R60SY10.py` | ✅✅✅✅ | ✅ |
| 111 | `_ge01_g7_register_measure.py` | `5c3454c88a926bb53297df0dc78d712cd7da020a31d18c7532092e4b001333a3` | 5,090 | `_ge01_g7_register_measure.py` | `$IRUIOU4.py` | `$RRUIOU4.py` | ✅✅✅✅ | ✅ |
| 112 | `_gh_tree.txt` | `823cfbb23a0397d8a8522df5c45f0a8782633f261c6a9c56891f6de17f3fdf78` | 341,814 | `_gh_tree.txt` | `$IXIBMQ6.txt` | `$RXIBMQ6.txt` | ✅✅✅✅ | ✅ |
| 113 | `_h_census_worker.json` | `22531e8519b2cdbe7d1f29d586dd5f7c05edd7ec44d686432a17a852d7255c8d` | 10,037,568 | `_h_census_worker.json` | `$IKLV4FN.json` | `$RKLV4FN.json` | ✅✅✅✅ | ✅ |
| 114 | `_h_census_worker.py` | `7f858d86f865b07284cb4aef906c97878ebab0c6d07ad9844190a0275918cef8` | 5,639 | `_h_census_worker.py` | `$IO9DPKG.py` | `$RO9DPKG.py` | ✅✅✅✅ | ✅ |
| 115 | `_hash21.py` | `0d5335f0ac5410f797fb3f31c1313f7f01d245571b121b0de04c6a0c2033a9a0` | 944 | `_hash21.py` | `$IDF0CMM.py` | `$RDF0CMM.py` | ✅✅✅✅ | ✅ |
| 116 | `_inspect_10cells.py` | `919f8f4e8ad2f4895091679d40bf503dacc075f1e41276d46e6a8ecb091126c3` | 2,460 | `_inspect_10cells.py` | `$IFH8RT9.py` | `$RFH8RT9.py` | ✅✅✅✅ | ✅ |
| 117 | `_inspect_batch4_rounds.py` | `bf479a2667dfa98a05f79e0e5b115930a69f797c743285f7e8fcb8e599e682ba` | 898 | `_inspect_batch4_rounds.py` | `$IKDMZ31.py` | `$RKDMZ31.py` | ✅✅✅✅ | ✅ |
| 118 | `_intake_cards_35_48_extract.py` | `74cca5bda2708e372c781ce14f71a8f45e8ad469c8e1e0b18f37e3213a3d8a3a` | 3,416 | `_intake_cards_35_48_extract.py` | `$I1ZL6IZ.py` | `$R1ZL6IZ.py` | ✅✅✅✅ | ✅ |
| 119 | `_iscp_dual_impl_2026_10_09.py` | `8734f4326d5a1e149bdac49a671b66ec3260793249462aaa456f904c5e6bec9a` | 2,974 | `_iscp_dual_impl_2026_10_09.py` | `$ISAQXMU.py` | `$RSAQXMU.py` | ✅✅✅✅ | ✅ |
| 120 | `_item35_v3_collinear_recompute_2026_10_01.py` | `c8d859cbb69ef88fdc043bd90a4f04561e09495be3234bef73e742a13235dab9` | 16,493 | `_item35_v3_collinear_recompute_2026_10_01.py` | `$IMS7LM6.py` | `$RMS7LM6.py` | ✅✅✅✅ | ✅ |
| 121 | `_kd04_c_den_exec_2026_10_10.py` | `419f9f691e6390fcdb7e30eeec610db53f48b1cbd0d479cdd6c77cd5b6e0de1c` | 21,430 | `_kd04_c_den_exec_2026_10_10.py` | `$ISWYXMI.py` | `$RSWYXMI.py` | ✅✅✅✅ | ✅ |
| 122 | `_kv3s43_diag_2026_10_09.py` | `398ebf6f33e0f6a71691297bf3fad4709b8958b869397ec9dc0e117aba8987b5` | 614 | `_kv3s43_diag_2026_10_09.py` | `$I3DA696.py` | `$R3DA696.py` | ✅✅✅✅ | ✅ |
| 123 | `_lit_log.txt` | `b062da7b654a6c0373a5d442257cbcff8725bc97ae219603e804bf4ac9081e9d` | 8,733 | `_lit_log.txt` | `$IUUOA5Z.txt` | `$RUUOA5Z.txt` | ✅✅✅✅ | ✅ |
| 124 | `_m5_k5_net.json` | `9d7fe894a26b9f9417c574d10ee08a348dee6f98844f38d24b7d0c9b04cb21fc` | 92,060 | `_m5_k5_net.json` | `$IOZ0RNP.json` | `$ROZ0RNP.json` | ✅✅✅✅ | ✅ |
| 125 | `_m5_k5_net.py` | `ec944f9178ea93f18019ee05986235044d1d370b47718ca364deae335f3450d1` | 3,173 | `_m5_k5_net.py` | `$I90EPM1.py` | `$R90EPM1.py` | ✅✅✅✅ | ✅ |
| 126 | `_m5_k5_net2.json` | `b2bc158e74999babf2181f32eef1b871a60c7c1147cc2148bb2fea3a9d0cc7e4` | 952,252 | `_m5_k5_net2.json` | `$ICM58KX.json` | `$RCM58KX.json` | ✅✅✅✅ | ✅ |
| 127 | `_m5_k5_scan.json` | `ebf1ad76dc8a42107cd19b8116a5a5b6d80e53f6898f248cc561211aac3e4d88` | 9,530 | `_m5_k5_scan.json` | `$ICEGVQU.json` | `$RCEGVQU.json` | ✅✅✅✅ | ✅ |
| 128 | `_m5_k5_scan.py` | `f5245072750f6e30561ed7b2bd231a8062e2897619bb88e0779846710c06e989` | 3,541 | `_m5_k5_scan.py` | `$ISSXY1K.py` | `$RSSXY1K.py` | ✅✅✅✅ | ✅ |
| 129 | `_m5_reaudit_archive.py` | `54540d871fb73dec2969e8d00aa1f3aa5b08c0f8d9a31354745731a68c44f461` | 1,405 | `_m5_reaudit_archive.py` | `$IZ2A7TU.py` | `$RZ2A7TU.py` | ✅✅✅✅ | ✅ |
| 130 | `_m5_reaudit_archive_out.json` | `e3542ccb4d3e2ec0e5ef366687bfc7b5ae17c35dd84ad71f3248a7fc077a1a4a` | 654 | `_m5_reaudit_archive_out.json` | `$IHQOSR6.json` | `$RHQOSR6.json` | ✅✅✅✅ | ✅ |
| 131 | `_m5_reaudit_detail.py` | `f43d192a972649039032d7b3e811726bf91a7f70bc220cbfe0294061d3b8c1b9` | 2,276 | `_m5_reaudit_detail.py` | `$IIJVVG5.py` | `$RIJVVG5.py` | ✅✅✅✅ | ✅ |
| 132 | `_m5_reaudit_detail.txt` | `8c117d51fc64a0fc094baa3b3fa231e5556de92a83aa2bc2d0e2bdc19d8180d6` | 9,214 | `_m5_reaudit_detail.txt` | `$IP55LBO.txt` | `$RP55LBO.txt` | ✅✅✅✅ | ✅ |
| 133 | `_m5_reaudit_probe.py` | `5b005dd13f95fc2fcaabb8545e51dfa48ced653a2ad8ca8e7412feec0f1e6614` | 4,469 | `_m5_reaudit_probe.py` | `$I10UWUS.py` | `$R10UWUS.py` | ✅✅✅✅ | ✅ |
| 134 | `_mk_voided_reloc_register.py` | `7c2d2f6955d07d2c1e004f34852683a706263d3fb0559df63f9bd0adc1957960` | 13,003 | `_mk_voided_reloc_register.py` | `$IC8GI6O.py` | `$RC8GI6O.py` | ✅✅✅✅ | ✅ |
| 135 | `_n1_n2_check.py` | `71f3f53a6eed4b5dfca0632584f82dcf897e6145f3e4de2cd33c2dba084c8926` | 1,628 | `_n1_n2_check.py` | `$IVPNVO2.py` | `$RVPNVO2.py` | ✅✅✅✅ | ✅ |
| 136 | `_ofc_s1_inventory.json` | `c2858312798b52dae8e7ef2312da03d50769196dc43ade977cd2b66bd0edaba1` | 216,695 | `_ofc_s1_inventory.json` | `$I7UMVOK.json` | `$R7UMVOK.json` | ✅✅✅✅ | ✅ |
| 137 | `_ofc_s1b_inventory.json` | `a28f35879008af95af1bd1a0625e2bbf51e2906432d832aa36b376ae4b97d6bb` | 336,955 | `_ofc_s1b_inventory.json` | `$I78BS7A.json` | `$R78BS7A.json` | ✅✅✅✅ | ✅ |
| 138 | `_patch21_emit.py` | `1d3c8aea6bad4f495f97cc0d0a5fbdc871f96eff2f3af2c32a8b33322053aed5` | 17,106 | `_patch21_emit.py` | `$I3HDZHX.py` | `$R3HDZHX.py` | ✅✅✅✅ | ✅ |
| 139 | `_patch21_make.py` | `b6cfdfaf80fa8bbf97d070ef23fac94f23b4b607cf63cef4555b8a751728a9f6` | 8,807 | `_patch21_make.py` | `$IE3MW0U.py` | `$RE3MW0U.py` | ✅✅✅✅ | ✅ |
| 140 | `_patch21_run.py` | `6333d9256716979e7a0232f71a59049d62f03fd052606607c1df2f460f1b1ffc` | 3,866 | `_patch21_run.py` | `$I19QDQV.py` | `$R19QDQV.py` | ✅✅✅✅ | ✅ |
| 141 | `_pc.py` | `7c59c7e80d5073342d702dfd4d1cfdeedaa7c260ded52424e4ccbd5afbbb563a` | 431 | `_pc.py` | `$ITSL335.py` | `$RTSL335.py` | ✅✅✅✅ | ✅ |
| 142 | `_pk_probe.py` | `6d79ba93952685be4e52521b1f6b3daa2e7409c9b9678553a6e3fdc235c7d89b` | 398 | `_pk_probe.py` | `$ISAYTX2.py` | `$RSAYTX2.py` | ✅✅✅✅ | ✅ |
| 143 | `_pk_sha_scan.py` | `df460eaec6194fe79895c0b65c003ed57e30555849fcfe8b42138f3a76c9353f` | 599 | `_pk_sha_scan.py` | `$IJ4SCC9.py` | `$RJ4SCC9.py` | ✅✅✅✅ | ✅ |
| 144 | `_pkf34_f3.py` | `389b3fdecd29fd4267d53ef026328843d047445b65b32d349bc19167a138f288` | 3,068 | `_pkf34_f3.py` | `$INUZSFW.py` | `$RNUZSFW.py` | ✅✅✅✅ | ✅ |
| 145 | `_pkf34_f34.py` | `a972a0383cf43a527c3e8b0155880e7613b99d303e663bcc615bb4bdea91549f` | 4,282 | `_pkf34_f34.py` | `$IHSVWUV.py` | `$RHSVWUV.py` | ✅✅✅✅ | ✅ |
| 146 | `_pkf34_f3b.py` | `e1bcbf3897d809dd718ef8ff73f4786a09e4fb2b4c6611a8621968a584d42006` | 2,703 | `_pkf34_f3b.py` | `$I70CZZQ.py` | `$R70CZZQ.py` | ✅✅✅✅ | ✅ |
| 147 | `_pkf34_f4.py` | `880a69b9cf296578633a376b687fc0e8fe152f5940435a4389b2f13cfc1f5b54` | 3,958 | `_pkf34_f4.py` | `$IM00HEC.py` | `$RM00HEC.py` | ✅✅✅✅ | ✅ |
| 148 | `_pkf34_f4b.py` | `e97f6ee41becec634173d914174797f6cdbce5f167ad9cef011b7f8d0bace637` | 4,401 | `_pkf34_f4b.py` | `$IM26TQT.py` | `$RM26TQT.py` | ✅✅✅✅ | ✅ |
| 149 | `_pkf34_f4c.py` | `c758efa2a5297627a9d2d76649de094d9be7c3696290aa17316663e28ed2f0d5` | 3,045 | `_pkf34_f4c.py` | `$IPTVQNJ.py` | `$RPTVQNJ.py` | ✅✅✅✅ | ✅ |
| 150 | `_pkf34_f4d.py` | `fb565a667edcc320bc38079a0045312ad02282b5298496911702b01c374ff8f6` | 3,686 | `_pkf34_f4d.py` | `$IEES4H4.py` | `$REES4H4.py` | ✅✅✅✅ | ✅ |
| 151 | `_pkf34_final.py` | `4b6140aaa61857dede40f705322b9c59a4e4980b105747ff9ac03029548fdde5` | 5,903 | `_pkf34_final.py` | `$I2K9E4A.py` | `$R2K9E4A.py` | ✅✅✅✅ | ✅ |
| 152 | `_pkf34_nd.py` | `527883f7ebb824662da08981422a123272c379145a3521b46e579089d1908a86` | 2,537 | `_pkf34_nd.py` | `$IWIBNFA.py` | `$RWIBNFA.py` | ✅✅✅✅ | ✅ |
| 153 | `_pkf34_v12.py` | `c650b0c20eee3ab9fa7b66e7a68d4f95341d3623a00b4bca574fc5cbd3b18024` | 5,639 | `_pkf34_v12.py` | `$IO4X4OV.py` | `$RO4X4OV.py` | ✅✅✅✅ | ✅ |
| 154 | `_postcheck_v16_alt.py` | `4d485d7a4d918f066cb0b306208e754c735bfcdedde2c77a7323c0d7a022ef93` | 1,282 | `_postcheck_v16_alt.py` | `$IS939MV.py` | `$RS939MV.py` | ✅✅✅✅ | ✅ |
| 155 | `_postcheck_v16_alt_stdout.txt` | `f116b23fa967f5cbdb336cd2ae5f2e3b339cb42753a4d4e4134bb0b3d7052926` | 1,558 | `_postcheck_v16_alt_stdout.txt` | `$IXUF0D1.txt` | `$RXUF0D1.txt` | ✅✅✅✅ | ✅ |
| 156 | `_postcheck_v16_sha.py` | `46759ba2b8e5c19db113a8cef00b4359c4a3ce350c889b722fe6811a6fa3cf6f` | 1,391 | `_postcheck_v16_sha.py` | `$ISXHYZ3.py` | `$RSXHYZ3.py` | ✅✅✅✅ | ✅ |
| 157 | `_pre_mod/exp_harness_pre.py` | `d5c8d676bb5b6b4e7fb3a6cb61ea331543be363b61b0801997d5a7c9b114ee98` | 36,217 | `t2b_harness_pre_change_snapshot_2026_10_16.py`, `_pre_mod/exp_harness_pre.py` | `$IU1DHIZ.py` | `$RU1DHIZ.py` | ✅✅✅✅ | ✅ |
| 158 | `_precheck_v15_tail.ps1` | `e94d8011bbf4485e4f3c8d7a93acfeeff21f440957784ec5cfeed88ff380f6e8` | 505 | `_precheck_v15_tail.ps1` | `$IF4141J.ps1` | `$RF4141J.ps1` | ✅✅✅✅ | ✅ |
| 159 | `_probe21.py` | `5a40370032b32e96c7bb276e8ef42c5bb07755c9f31a596956d5ebd064451e42` | 564 | `_probe21.py` | `$IU7T5W1.py` | `$RU7T5W1.py` | ✅✅✅✅ | ✅ |
| 160 | `_r10.py` | `1b012cd12a00294da3da37ae702f3661bb661c3d1ad52ac4535ffa9aa7ae5ea0` | 1,525 | `_r10.py` | `$IV5P74X.py` | `$RV5P74X.py` | ✅✅✅✅ | ✅ |
| 161 | `_r1_alarm_test.py` | `c44a09297f1aade0347cdd96bf12d396607bfc591fc9727d3833ee07666244dc` | 2,297 | `_r1_alarm_test.py` | `$I52SDNV.py` | `$R52SDNV.py` | ✅✅✅✅ | ✅ |
| 162 | `_r3_header_fix_2026_09_28.py` | `6f8cec0fe0064dc78af3dbb011dd84ee7b3859497ec778b6ce21a06c43c14fae` | 3,280 | `_r3_header_fix_2026_09_28.py` | `$IO8AXLM.py` | `$RO8AXLM.py` | ✅✅✅✅ | ✅ |
| 163 | `_r3_verify_2026_09_28.py` | `721e52f9d55f8b3a4cec4c976789aabfc3b12d2f6c4a729b789f20deb008cd76` | 5,494 | `_r3_verify_2026_09_28.py` | `$IMJBSIQ.py` | `$RMJBSIQ.py` | ✅✅✅✅ | ✅ |
| 164 | `_r4_cleanup_worker_keycount_2026_09_29.py` | `ca0cbafed00b7ce3ead9a9a20deaf5c4e4c61ad91c36ffcd74a6258029e6873e` | 1,909 | `_r4_cleanup_worker_keycount_2026_09_29.py` | `$INJCAUN.py` | `$RNJCAUN.py` | ✅✅✅✅ | ✅ |
| 165 | `_r4_cleanup_worker_keyscan_2026_09_29.py` | `01e1ac2ef2390f4c4c76813f17f992f1bc05743c5bbc8f1bad5dbc019f3400cd` | 3,561 | `_r4_cleanup_worker_keyscan_2026_09_29.py` | `$I224A1K.py` | `$R224A1K.py` | ✅✅✅✅ | ✅ |
| 166 | `_r4_cleanup_worker_nearmiss_2026_09_29.py` | `22336cc16500695734f815df199547267bcae7fb43fb6028f32c247df901307b` | 1,382 | `_r4_cleanup_worker_nearmiss_2026_09_29.py` | `$I0IXF0C.py` | `$R0IXF0C.py` | ✅✅✅✅ | ✅ |
| 167 | `_r4_cleanup_worker_scan_2026_09_29.py` | `af404c489392a2673cbeeb54130ca34aab932d83637b3414a6d43df52d962489` | 2,411 | `_r4_cleanup_worker_scan_2026_09_29.py` | `$IQTAJE8.py` | `$RQTAJE8.py` | ✅✅✅✅ | ✅ |
| 168 | `_r4_cleanup_worker_shape_2026_09_29.py` | `f7f6313edce866a05a83f9377861ac7dac713bcd54f330932a861f08c69c687d` | 1,110 | `_r4_cleanup_worker_shape_2026_09_29.py` | `$IP2ADJY.py` | `$RP2ADJY.py` | ✅✅✅✅ | ✅ |
| 169 | `_r4_key_scan_2026_09_24.py` | `c782d1a18092da6e64a4a5031731ed64150f2d34321872dccbcb4ca1f2ae5a91` | 3,743 | `_r4_key_scan_2026_09_24.py` | `$I5ZZJBM.py` | `$R5ZZJBM.py` | ✅✅✅✅ | ✅ |
| 170 | `_r4_key_scan_r1_files_2026_09_27.py` | `cec4c1f3ff9c374ee7f8dd4ffb9e5853c6ce435e4f682d99552881f6d1277e85` | 4,079 | `_r4_key_scan_r1_files_2026_09_27.py` | `$IV3ZOXO.py` | `$RV3ZOXO.py` | ✅✅✅✅ | ✅ |
| 171 | `_r5_write_register_2026_10_13.py` | `139c8a7316db3a2d38e36fed27ceb9fdbcb3555c94d43ea1f37753dbac31e814` | 25,902 | `_r5_write_register_2026_10_13.py` | `$IW9JD7D.py` | `$RW9JD7D.py` | ✅✅✅✅ | ✅ |
| 172 | `_r6_evidence.py` | `4de12a4f441bd8189dc01acf964f60286aaae51b17a29c0263e0b11a1077cdae` | 2,525 | `_r6_evidence.py` | `$I7EWKL6.py` | `$R7EWKL6.py` | ✅✅✅✅ | ✅ |
| 173 | `_recheck_r1_run1.log` | `80b338a0e9ad1884237d7bcd3a85c0b8c3d31d1a2113cbd63573b9040e6faa98` | 2,486 | `_recheck_r1_run1.log` | `$IRYXX8L.log` | `$RRYXX8L.log` | ✅✅✅✅ | ✅ |
| 174 | `_rj5_convention_check_2026_09_27.py` | `5dbb93b3c5e55e1176dd9f1cd66d3647a205c2647649bb1475c79c2d86f15d0a` | 8,018 | `_rj5_convention_check_2026_09_27.py` | `$ISXKCAX.py` | `$RSXKCAX.py` | ✅✅✅✅ | ✅ |
| 175 | `_rj5_mapping_test_2026_09_27.py` | `75ff70d87bd7bf41bb0e17b55165c20f61966047b34c69e4ccf2424131422dae` | 5,968 | `_rj5_mapping_test_2026_09_27.py` | `$IKVHWK1.py` | `$RKVHWK1.py` | ✅✅✅✅ | ✅ |
| 176 | `_rp4_fields.py` | `1d112ab8f3b476a1ae4eb49f59313d6e9c389ffa416f5be0d49d0a613604e2ed` | 433 | `_rp4_fields.py` | `$IWLUX6I.py` | `$RWLUX6I.py` | ✅✅✅✅ | ✅ |
| 177 | `_rp_addendum_build_2026_10_09.py` | `c4e8b75d656b7f1b4169c7bb3d1c7ac0150db0da5224351c5625fe5674f8a2a3` | 30,375 | `_rp_addendum_build_2026_10_09.py` | `$IX0P7U6.py` | `$RX0P7U6.py` | ✅✅✅✅ | ✅ |
| 178 | `_rp_verify_2026_10_09.py` | `e0adae15fc266f061d360c87b2869606c8c12186582a5df18fd261104a4e295e` | 3,282 | `_rp_verify_2026_10_09.py` | `$IGUQC8O.py` | `$RGUQC8O.py` | ✅✅✅✅ | ✅ |
| 179 | `_rpd_neighbors_2026_10_09.py` | `28cfa9466ea38f1757071867798fcebc3530c9b35d649fde3bbde01b7648952e` | 1,286 | `_rpd_neighbors_2026_10_09.py` | `$I2N8023.py` | `$R2N8023.py` | ✅✅✅✅ | ✅ |
| 180 | `_rpd_reuse_strict_2026_10_09.py` | `4557b47b736115a142dbd5a2a656fd742801b33397d9b939c1c3052423b12d12` | 4,746 | `_rpd_reuse_strict_2026_10_09.py` | `$IONILC3.py` | `$RONILC3.py` | ✅✅✅✅ | ✅ |
| 181 | `_rpd_verify_landed_2026_10_09.py` | `912a2b8066f12e93666dfe752cf917dd6c5d2e0459cfffd85c2f7dcde524c582` | 6,335 | `_rpd_verify_landed_2026_10_09.py` | `$I3WGHYG.py` | `$R3WGHYG.py` | ✅✅✅✅ | ✅ |
| 182 | `_run2.py` | `8acbf24342d14e0991048a42f5b6aab219d4f3bb5be7b161fe11dd2bc47ab17b` | 4,366 | `_run2.py` | `$ID3Q4AN.py` | `$RD3Q4AN.py` | ✅✅✅✅ | ✅ |
| 183 | `_run_d4_relabel_addendum.py` | `620eabf853aff66bd103d522cbdea73b160c0f0d8619140a997e0f5749759948` | 17,550 | `_run_d4_relabel_addendum.py` | `$I23EHZR.py` | `$R23EHZR.py` | ✅✅✅✅ | ✅ |
| 184 | `_run_d6_addendum_2026_09_28.py` | `e472ea36ed08c2c41e57e4d4df8f06d32db10651bd397a3173b0fec46bddafae` | 23,204 | `_run_d6_addendum_2026_09_28.py` | `$I3O1KCQ.py` | `$R3O1KCQ.py` | ✅✅✅✅ | ✅ |
| 185 | `_run_d6b_addendum_2026_09_28.py` | `f0a4e919eeaa36b58a920b6a13b334a6dbc14c95dd3eb045a94fd1672a04a30f` | 31,468 | `_run_d6b_addendum_2026_09_28.py` | `$IVDNDJI.py` | `$RVDNDJI.py` | ✅✅✅✅ | ✅ |
| 186 | `_run_d8_addendum_2026_09_30.py` | `7ce330b3e5ae37527a36fed05834152940d92ea87c0a41fd65cd04225555bef5` | 107,959 | `_run_d8_addendum_2026_09_30.py` | `$I19CMDV.py` | `$R19CMDV.py` | ✅✅✅✅ | ✅ |
| 187 | `_run_d8_bhalf_addendum_2026_09_30.py` | `90fa2c44352963038ea1705ad042f3ed1ea395cb0dc28a03a62a9b91f281b3a0` | 40,576 | `_run_d8_bhalf_addendum_2026_09_30.py` | `$I1S7JDX.py` | `$R1S7JDX.py` | ✅✅✅✅ | ✅ |
| 188 | `_run_day_inventory_table_2026_09_27.py` | `329bf2b664220d3757126fac5ab6feab318a174940a41e5d1a7b2d6d5f5f4958` | 2,763 | `_run_day_inventory_table_2026_09_27.py` | `$IGF46YZ.py` | `$RGF46YZ.py` | ✅✅✅✅ | ✅ |
| 189 | `_run_final.py` | `75d466add5d54cbe603ba56363786f4ab1885a128ed41125871c42c47d474bf2` | 26,654 | `_run_final.py` | `$IOYFYO8.py` | `$ROYFYO8.py` | ✅✅✅✅ | ✅ |
| 190 | `_run_final_selfscan_2026_09_27.py` | `cf5c5c7684bbaf6512fb1bccf82e1bddca8f05879fe24eceb28f285773135b3a` | 1,358 | `_run_final_selfscan_2026_09_27.py` | `$I3LYABE.py` | `$R3LYABE.py` | ✅✅✅✅ | ✅ |
| 191 | `_run_frozen_0touch_verify_2026_09_27.py` | `48246f41e7d3eb4accdf83d71636ff8a93e21a572df3edc4e89fa11986ca279b` | 2,309 | `_run_frozen_0touch_verify_2026_09_27.py` | `$IVJ1TP0.py` | `$RVJ1TP0.py` | ✅✅✅✅ | ✅ |
| 192 | `_run_recheck_r1.py` | `a76ec3a2340e260e494c1d8958b99e5ea8dc20090f84738d3e9502eea11e02cc` | 34,895 | `_run_recheck_r1.py` | `$I0EP7BC.py` | `$R0EP7BC.py` | ✅✅✅✅ | ✅ |
| 193 | `_run_result_v3.py` | `83cd4414f4046eb21a8550ad89ba2b8f994408a7cd3eb98983a891d83d6763e0` | 3,304 | `_run_result_v3.py` | `$ITLDVJG.py` | `$RTLDVJG.py` | ✅✅✅✅ | ✅ |
| 194 | `_run_v3r1_relabel.py` | `55d06ce42b3d9744e217d5edcae4dbfb6c25928ff152fdf8f44b48ac232d611e` | 30,875 | `_run_v3r1_relabel.py` | `$IJ9EYW7.py` | `$RJ9EYW7.py` | ✅✅✅✅ | ✅ |
| 195 | `_s3_f1_loader_fix_recompute_2026_10_08.py` | `e39e4ae7d6eda2fac90b676c5d3933f3cb05ee29480d2a4dc8dc08c74ffd7743` | 21,231 | `_s3_f1_loader_fix_recompute_2026_10_08.py` | `$I8563PR.py` | `$R8563PR.py` | ✅✅✅✅ | ✅ |
| 196 | `_s4_freeze_count_crosscheck2_2026_10_09.py` | `15fa4d155fc9f6b75a600d23feed11c82c8c283a14d626ce8a2456e5759b69ba` | 3,920 | `_s4_freeze_count_crosscheck2_2026_10_09.py` | `$IM70UV8.py` | `$RM70UV8.py` | ✅✅✅✅ | ✅ |
| 197 | `_s4_freeze_count_crosscheck3_2026_10_09.py` | `ee420dfd57e6c345683f5762a47d8862342dd09b74fa7c2159863cb1ff359f3a` | 4,041 | `_s4_freeze_count_crosscheck3_2026_10_09.py` | `$II8RO82.py` | `$RI8RO82.py` | ✅✅✅✅ | ✅ |
| 198 | `_s4_freeze_count_crosscheck_2026_10_09.py` | `856e6ab48dae95a0b70cffceea54ef183ecb9f38e031fb52ee4d6b0790ff3f41` | 3,463 | `_s4_freeze_count_crosscheck_2026_10_09.py` | `$IAWBTBX.py` | `$RAWBTBX.py` | ✅✅✅✅ | ✅ |
| 199 | `_s4_seedprime_seq_t1_supplement_2026_10_11.py` | `3a9db2126e4f6fd21d7790a5a6c2a55ca200b75aa40da3302ecece864c4557b8` | 31,705 | `_s4_seedprime_seq_t1_supplement_2026_10_11.py` | `$IY999Q3.py` | `$RY999Q3.py` | ✅✅✅✅ | ✅ |
| 200 | `_s4_topup_addendum_builder_2026_10_09.py` | `b9987c7a8d5f3badb8830b8d21d78229e0b68e6ccdbf1480e8c2478ade37b6e9` | 21,122 | `_s4_topup_addendum_builder_2026_10_09.py` | `$IW6W01B.py` | `$RW6W01B.py` | ✅✅✅✅ | ✅ |
| 201 | `_s4_tree_construct_exec_2026_10_10.py` | `4cbd10b61aae0f6409717ce330ec4dcf1c2acd83046b33417d500ac7848c8487` | 34,265 | `_s4_tree_construct_exec_2026_10_10.py` | `$IN6JXL0.py` | `$RN6JXL0.py` | ✅✅✅✅ | ✅ |
| 202 | `_s4f2_dbg.py` | `5159c9c30180ca60120bdc7579a655cb158fd88eaf5061653ae0d00990fa62c1` | 431 | `_s4f2_dbg.py` | `$ISQVWJW.py` | `$RSQVWJW.py` | ✅✅✅✅ | ✅ |
| 203 | `_s4f2_face_probe_2026_10_09.py` | `62e04248d12214a27ffb1ba2945a5b55c184fda8f1e26f989f8942d3492f16a5` | 14,896 | `_s4f2_face_probe_2026_10_09.py` | `$ILKQ3LR.py` | `$RLKQ3LR.py` | ✅✅✅✅ | ✅ |
| 204 | `_s4f2_patch.py` | `b79a7073099df43634bab0942ce43361ad2d8dcf4274686c489cebce0454f598` | 2,740 | `_s4f2_patch.py` | `$IGYWVUA.py` | `$RGYWVUA.py` | ✅✅✅✅ | ✅ |
| 205 | `_s4f2_patch2.py` | `045bd90b237a6de02c3722aa5aeb2b7177fd4f5e4ea5852eab296df32beb1e72` | 421 | `_s4f2_patch2.py` | `$IA9RXPH.py` | `$RA9RXPH.py` | ✅✅✅✅ | ✅ |
| 206 | `_s4f2_patch3.py` | `6d57ff4ce76cbb6441f5a4c991c918bb48da04b8007377af667992274dcdfca5` | 815 | `_s4f2_patch3.py` | `$IMJAMUZ.py` | `$RMJAMUZ.py` | ✅✅✅✅ | ✅ |
| 207 | `_s4f2_patch4.py` | `7d85756a841dc4cf9766a82af183d99573b135d9d418e67f38ac53af3a3cbbe2` | 565 | `_s4f2_patch4.py` | `$I09ON5T.py` | `$R09ON5T.py` | ✅✅✅✅ | ✅ |
| 208 | `_s4f2_scanner_selftest.py` | `5b6fd262f7850533cca26b877fee94ff15a31d0da454e581dd7ba68fc61c1760` | 1,819 | `_s4f2_scanner_selftest.py` | `$IWIS2PV.py` | `$RWIS2PV.py` | ✅✅✅✅ | ✅ |
| 209 | `_s4fs_auxdate_2026_10_09.py` | `637e936d8bc77e2a5a8f42c76db65eacdd71e5fa3c7341b7271d4f0050df467f` | 1,877 | `_s4fs_auxdate_2026_10_09.py` | `$IF4JO5P.py` | `$RF4JO5P.py` | ✅✅✅✅ | ✅ |
| 210 | `_s4fs_selfreport_2026_10_09.py` | `485071c7dd5ef0d9841137765908035c34f5ffbebd2234227fbde56aba7d2181` | 432 | `_s4fs_selfreport_2026_10_09.py` | `$IKU80CX.py` | `$RKU80CX.py` | ✅✅✅✅ | ✅ |
| 211 | `_s4fs_yitable_2026_10_09.py` | `2bf7fd0ef5dc3dd310b1c524e17408b4d4937751b14bc00cb74e511498a7a523` | 1,634 | `_s4fs_yitable_2026_10_09.py` | `$IQP9GAG.py` | `$RQP9GAG.py` | ✅✅✅✅ | ✅ |
| 212 | `_s4oq_addendum_struct_2026_10_09.py` | `67652acdf681fa1edb6607f2f49ae4a5ee8c5d34c67015378bc9e88b83b619ae` | 843 | `_s4oq_addendum_struct_2026_10_09.py` | `$IOABJVB.py` | `$ROABJVB.py` | ✅✅✅✅ | ✅ |
| 213 | `_s4oq_build_baseline_2026_10_09.py` | `3cf28fe89611bb9c977f7db243acdc7a81ab77ff7c383e0ebffd6aa9ca0c5c54` | 3,501 | `_s4oq_build_baseline_2026_10_09.py` | `$IVXBN92.py` | `$RVXBN92.py` | ✅✅✅✅ | ✅ |
| 214 | `_s4oq_build_draft_2026_10_09.py` | `0797d19dcaf3bfbfb071f61cb5189dd5d297f81296fe6ff4ebfdc6bfc2c0e783` | 8,719 | `_s4oq_build_draft_2026_10_09.py` | `$I5DVPEJ.py` | `$R5DVPEJ.py` | ✅✅✅✅ | ✅ |
| 215 | `_s4oq_cellmap_2026_10_09.py` | `c07589f292e1d7d0e291f5d7d1780508c0df6f4bd3f4e38ca5c6e968d57fb70e` | 1,734 | `_s4oq_cellmap_2026_10_09.py` | `$IB2KJIP.py` | `$RB2KJIP.py` | ✅✅✅✅ | ✅ |
| 216 | `_s4oq_final_verify_2026_10_09.py` | `944a4f7006c8e8fbdacbb3bdb9c811e82118032ce758bd60b64c18bdc9191b2e` | 959 | `_s4oq_final_verify_2026_10_09.py` | `$IWLYASO.py` | `$RWLYASO.py` | ✅✅✅✅ | ✅ |
| 217 | `_s4oq_forward_2026_10_09.py` | `43e72c62587d0a8e85aed8a4fa358d7e272ed7e49dc1e9d8a349c2335a50d194` | 3,482 | `_s4oq_forward_2026_10_09.py` | `$IKINRK9.py` | `$RKINRK9.py` | ✅✅✅✅ | ✅ |
| 218 | `_s4oq_grid_cmp_2026_10_09.py` | `f00865587d6abb3c1af88c4cecff29c9a879a91aba86472e1d169c621ec17bfc` | 1,601 | `_s4oq_grid_cmp_2026_10_09.py` | `$IT9SAGU.py` | `$RT9SAGU.py` | ✅✅✅✅ | ✅ |
| 219 | `_s4oq_grid_diag_2026_10_09.py` | `082e8b8b7bc4e7fffc503fd9f90b578101bcb5b22c366286f9085723188dcf29` | 1,553 | `_s4oq_grid_diag_2026_10_09.py` | `$ILOUANQ.py` | `$RLOUANQ.py` | ✅✅✅✅ | ✅ |
| 220 | `_s4oq_grid_recompute_2026_10_09.py` | `afb613f5ced1f2431143239b0344939a041443ec9a06c2b924b3c3b4de014dd6` | 2,394 | `_s4oq_grid_recompute_2026_10_09.py` | `$IRHTZBM.py` | `$RRHTZBM.py` | ✅✅✅✅ | ✅ |
| 221 | `_s4oq_keyscan_2026_10_09.py` | `c9f94c812f7f26c76f905b945bf178d23186633779112300994d482faab6f236` | 573 | `_s4oq_keyscan_2026_10_09.py` | `$IN05UTW.py` | `$RN05UTW.py` | ✅✅✅✅ | ✅ |
| 222 | `_s4oq_recompute_2026_10_09.py` | `07cdec6533450779e935619db4365a904e2d3e983359bcb5b57b4cf9e4549291` | 3,202 | `_s4oq_recompute_2026_10_09.py` | `$I1J5WBC.py` | `$R1J5WBC.py` | ✅✅✅✅ | ✅ |
| 223 | `_s4oq_reuse_check_2026_10_09.py` | `952c76c5b103771faef460f1b5940366c17178f69da4358094a970e01c9c7c2c` | 6,712 | `_s4oq_reuse_check_2026_10_09.py` | `$I78L3NU.py` | `$R78L3NU.py` | ✅✅✅✅ | ✅ |
| 224 | `_s4oq_reuse_v2_2026_10_09.py` | `bc0f200edd1ea3b19067d6e329b266f04efc2d818c169a81feebe42deff68b74` | 6,293 | `_s4oq_reuse_v2_2026_10_09.py` | `$IC3ZBJ1.py` | `$RC3ZBJ1.py` | ✅✅✅✅ | ✅ |
| 225 | `_s4oq_skel_2026_10_09.py` | `73fc780b48499d28e2c6a8c3c93c72a78b82f657e6ba084f12dc221c0e1bb084` | 466 | `_s4oq_skel_2026_10_09.py` | `$IPEO113.py` | `$RPEO113.py` | ✅✅✅✅ | ✅ |
| 226 | `_s4oq_slug_opt_2026_10_09.py` | `77d696b1690d6dfeb7d65c7d239f85759ce17edecf961f59f66aa17091bb82ca` | 4,636 | `_s4oq_slug_opt_2026_10_09.py` | `$I7PKQ59.py` | `$R7PKQ59.py` | ✅✅✅✅ | ✅ |
| 227 | `_s4oq_slug_search2_2026_10_09.py` | `fe6f7044ec4eb6cef5cc4e0dbe2b05a07f4ef561913eb1de01d11ddabfec9b54` | 5,258 | `_s4oq_slug_search2_2026_10_09.py` | `$I8OYSIE.py` | `$R8OYSIE.py` | ✅✅✅✅ | ✅ |
| 228 | `_s4oq_variants_2026_10_09.py` | `ccbbb499e19a04c87b63071a95e61ab2a3c91989eb2a6aaf64ded84b232fd221` | 1,233 | `_s4oq_variants_2026_10_09.py` | `$IB065OY.py` | `$RB065OY.py` | ✅✅✅✅ | ✅ |
| 229 | `_s4oq_verify_addendum_2026_10_09.py` | `419c15a7a2c5208b7f90836af27a039109e007c53a8099e015ce52bebabf7669` | 2,252 | `_s4oq_verify_addendum_2026_10_09.py` | `$IE6EJJY.py` | `$RE6EJJY.py` | ✅✅✅✅ | ✅ |
| 230 | `_s4oq_write_addendum_2026_10_09.py` | `63e61afa651729f2b7968caa625a163291a195cefc18186e808258aefcfd48d3` | 11,886 | `_s4oq_write_addendum_2026_10_09.py` | `$IQV3BPI.py` | `$RQV3BPI.py` | ✅✅✅✅ | ✅ |
| 231 | `_s4td_cell_map_2026_10_09.py` | `6665669d858d7f0292eb6ed5dfbbadb6ad000fbb2df6694dee858a7035a864ca` | 3,642 | `_s4td_cell_map_2026_10_09.py` | `$IFXYF2J.py` | `$RFXYF2J.py` | ✅✅✅✅ | ✅ |
| 232 | `_s4td_floor_bound_2026_10_09.py` | `ad95b6d5e9b9938937d681f68a748af14639fdf57ea660cbe13a8c02bdc2510f` | 4,378 | `_s4td_floor_bound_2026_10_09.py` | `$IN15I97.py` | `$RN15I97.py` | ✅✅✅✅ | ✅ |
| 233 | `_s4td_reuse_and_bound_2026_10_09.py` | `af6fdc892f6095d2aaf4b94dab0c70c0143f9b915cf9a2a88b66ad5cc98ea9cf` | 8,765 | `_s4td_reuse_and_bound_2026_10_09.py` | `$IKVBLEG.py` | `$RKVBLEG.py` | ✅✅✅✅ | ✅ |
| 234 | `_s4td_slug_search_2026_10_09.py` | `ce5529ec7516075d94076c0fa9f8797c32b3df2e6c954ca8b6b7ec3c8309b224` | 4,657 | `_s4td_slug_search_2026_10_09.py` | `$ICQIROJ.py` | `$RCQIROJ.py` | ✅✅✅✅ | ✅ |
| 235 | `_s5dp_five_lines_runner_third_2026_10_11.py` | `9de3c08e386399f82095dffd664b3424e7e8ac24381a90f6bb1270a436cdf171` | 31,138 | `_s5dp_five_lines_runner_third_2026_10_11.py` | `$IUYR8R0.py` | `$RUYR8R0.py` | ✅✅✅✅ | ✅ |
| 236 | `_sensitivity.py` | `8aacafa48f9cb28c98bf869c0270061a78e6e7d7a1177d6a93e4c254aa9096d0` | 5,954 | `_sensitivity.py` | `$I74JC21.py` | `$R74JC21.py` | ✅✅✅✅ | ✅ |
| 237 | `_sha12_check.ps1` | `a4bfec107a773f3df6d405b15c8065dbf43c95f6c3ffec5d8a4e307ab23e9659` | 697 | `_sha12_check.ps1` | `$IKH5RZT.ps1` | `$RKH5RZT.ps1` | ✅✅✅✅ | ✅ |
| 238 | `_sha12_check2.ps1` | `3e9174fb1e03a46e191acd038645ab9343aa983760d51f570ab412f72e5e872f` | 691 | `_sha12_check2.ps1` | `$IU9W6QW.ps1` | `$RU9W6QW.ps1` | ✅✅✅✅ | ✅ |
| 239 | `_t15_inspect.py` | `9877c9536e33d30bf399148abff82d05198b02207e6f9ed9789163202f32b9d4` | 2,728 | `_t15_inspect.py` | `$IKZZ081.py` | `$RKZZ081.py` | ✅✅✅✅ | ✅ |
| 240 | `_t15_inspect2.py` | `9a6b5bb328aafb5251d6922670acd43ca7e9b83df90919aa4c770f4e685a4e6a` | 1,942 | `_t15_inspect2.py` | `$IAU8T76.py` | `$RAU8T76.py` | ✅✅✅✅ | ✅ |
| 241 | `_t15_inspect3.py` | `d423ca72cb3c91e6b1629751fb3c390789dabf047b32fd2c3fc5bd94c55c1b66` | 1,890 | `_t15_inspect3.py` | `$I935763.py` | `$R935763.py` | ✅✅✅✅ | ✅ |
| 242 | `_t15_inspect4.py` | `069b7562f463dae6b97da906c0f92bb1b48c6848cf8b4976e9d53c498e933205` | 2,756 | `_t15_inspect4.py` | `$IN2RIE8.py` | `$RN2RIE8.py` | ✅✅✅✅ | ✅ |
| 243 | `_t15_inspect5.py` | `977753c193d22673eca9325751660de38c5543d8cb44881ed787d75199579233` | 2,712 | `_t15_inspect5.py` | `$IINOU51.py` | `$RINOU51.py` | ✅✅✅✅ | ✅ |
| 244 | `_t15_inspect6.py` | `eba3a29f6264b00f728bbca833b93312b158c4570a1b57af0b7781947aaa7e62` | 1,234 | `_t15_inspect6.py` | `$I96YB7O.py` | `$R96YB7O.py` | ✅✅✅✅ | ✅ |
| 245 | `_t15_inspect7.py` | `78dafdf124f78154f9fe73ac8d6e6816cdf2029802487f731064d4fd909b3c90` | 3,880 | `_t15_inspect7.py` | `$IVXNEX1.py` | `$RVXNEX1.py` | ✅✅✅✅ | ✅ |
| 246 | `_t15_percell.py` | `c035476cfb413941c614d828217a3169c66e8a1e53474aae2a2c1bd595e23814` | 596 | `_t15_percell.py` | `$IU6WGZ5.py` | `$RU6WGZ5.py` | ✅✅✅✅ | ✅ |
| 247 | `_t15_probe_log.json` | `94444963ff77a0fac3cc20758178d959ef82cbe81508dec5874da5fd4245d679` | 718 | `_t15_probe_log.json` | `$ICKTBA6.json` | `$RCKTBA6.json` | ✅✅✅✅ | ✅ |
| 248 | `_t15_records.json` | `8014af0e2b793d2220d1a2c8d1e371bd9c7dccab473b7f69ddc302d1ebd0686a` | 96,443 | `_t15_records.json` | `$IZ0SQMK.json` | `$RZ0SQMK.json` | ✅✅✅✅ | ✅ |
| 249 | `_t15_update_result.py` | `ad66f242c6a186f5fa6a6308770b3cb58e02edb5d9e97235594ae904e3a98f89` | 9,226 | `_t15_update_result.py` | `$IA94B5X.py` | `$RA94B5X.py` | ✅✅✅✅ | ✅ |
| 250 | `_t15r2_inspect.py` | `c58dc90fd86a05d48a228fcf7c9eae036b04de31a0b40445df90b5dd7a9459a4` | 3,730 | `_t15r2_inspect.py` | `$IGPPV42.py` | `$RGPPV42.py` | ✅✅✅✅ | ✅ |
| 251 | `_t15r2_verify.py` | `5267b4dee7dc7a81849eb0e23f72d6d3fb64869485167a652d16519920469913` | 6,737 | `_t15r2_verify.py` | `$IFZM48G.py` | `$RFZM48G.py` | ✅✅✅✅ | ✅ |
| 252 | `_t1_exp2_c_driver_2026_10_09.py` | `5d474b7ceada193a5df68230017f3ed064566fcf083e7ef7661800314941501d` | 2,898 | `_t1_exp2_c_driver_2026_10_09.py` | `$IYMPSDK.py` | `$RYMPSDK.py` | ✅✅✅✅ | ✅ |
| 253 | `_t1_exp2_c_records.json` | `f53681c7569af6fc3ab8eb1175035804445350fbb0c571b62ad960ba617fa221` | 6,277,328 | `_t1_exp2_c_records.json` | `$I85O1BS.json` | `$R85O1BS.json` | ✅✅✅✅ | ✅ |
| 254 | `_t1_exp2_calib_2026_10_09.json` | `de09d4ee3721aae3f449f44caa8d27c4b73e140b4165c621ccf64a8503a03493` | 611 | `_t1_exp2_calib_2026_10_09.json` | `$I34RS1F.json` | `$R34RS1F.json` | ✅✅✅✅ | ✅ |
| 255 | `_t1_exp2_d_readings.json` | `2315f68230118fadbb7770d5923292b20b674350d55a42ac1d1bfe28b9dabf1c` | 3,991 | `_t1_exp2_d_readings.json` | `$IIFI5G4.json` | `$RIFI5G4.json` | ✅✅✅✅ | ✅ |
| 256 | `_t1_exp2_d_records.json` | `aadba0c4f952dce99d070755d8c0bd33d5c1e445d2e75d7982e9859063b76735` | 488,395 | `_t1_exp2_d_records.json` | `$IQ9O49Y.json` | `$RQ9O49Y.json` | ✅✅✅✅ | ✅ |
| 257 | `_t1_exp2_probe_log.json` | `c6478415e2bfd3778ba881e9ed5b4ca72955eb43dd78042bd51c3d5b2fcfa6d1` | 760 | `_t1_exp2_probe_log.json` | `$IS5PGG4.json` | `$RS5PGG4.json` | ✅✅✅✅ | ✅ |
| 258 | `_t1_exp2_selfcert.json` | `d929eb9ae0b846e98ea72de03219183f9e7a31660ce54d124a37b72eaf302946` | 6,780 | `_t1_exp2_selfcert.json` | `$IY682U0.json` | `$RY682U0.json` | ✅✅✅✅ | ✅ |
| 259 | `_t1_gap_domain_sweep_2026_10_01.py` | `74d1ed439442fd99222fd32b25615f108241931da588297d9882f5ebb5d18e6b` | 2,502 | `_t1_gap_domain_sweep_2026_10_01.py` | `$INUKCQO.py` | `$RNUKCQO.py` | ✅✅✅✅ | ✅ |
| 260 | `_t1_gap_postwrite_verify_2026_10_01.py` | `33b4108f14a139415812de1ec84a9a95e23051dad0d8d1a920cc1dcf86dffa1d` | 5,666 | `_t1_gap_postwrite_verify_2026_10_01.py` | `$IYW8VF2.py` | `$RYW8VF2.py` | ✅✅✅✅ | ✅ |
| 261 | `_t1_gap_snapshot_2026_10_01.py` | `fd53258bd16f1a16b43aaffecc88d6ec9cb13761b53ed2edc975804c39f23268` | 2,588 | `_t1_gap_snapshot_2026_10_01.py` | `$IYIFPV2.py` | `$RYIFPV2.py` | ✅✅✅✅ | ✅ |
| 262 | `_t1_qwen_temp_sweep_decomposition.py` | `97a6520c7105affe118010cf78065391ab792f09ca8a0f8eaafee13a9dadb8a2` | 1,981 | `_t1_qwen_temp_sweep_decomposition.py` | `$I8TFYC9.py` | `$R8TFYC9.py` | ✅✅✅✅ | ✅ |
| 263 | `_t1_qwen_temp_sweep_dump_readings.py` | `7e06567afc2a30e41aef9799f5508539d1906ae3c9d0779982672b790a138d7b` | 1,137 | `_t1_qwen_temp_sweep_dump_readings.py` | `$IF59U5G.py` | `$RF59U5G.py` | ✅✅✅✅ | ✅ |
| 264 | `_t1_qwen_temp_sweep_probe_log.json` | `b5e4151af490ee35ff7c6fe96483a95389b5084af591d329bb5e98b53b4557d8` | 445 | `_t1_qwen_temp_sweep_probe_log.json` | `$I9S1E9Z.json` | `$R9S1E9Z.json` | ✅✅✅✅ | ✅ |
| 265 | `_t1_qwen_temp_sweep_r2_probe_log.json` | `5182f6fdd9efa0116124aa89d2ecd460f6c1ee23f38b89810f3d93f74880f999` | 739 | `_t1_qwen_temp_sweep_r2_probe_log.json` | `$IXD1HUJ.json` | `$RXD1HUJ.json` | ✅✅✅✅ | ✅ |
| 266 | `_t1_qwen_temp_sweep_r2_records.json` | `bb511e7b0baf9f91baa277307813309962d51ee24ab9a75c7ee9d1b365e4ddd6` | 1,795,870 | `_t1_qwen_temp_sweep_r2_records.json` | `$IP97WR0.json` | `$RP97WR0.json` | ✅✅✅✅ | ✅ |
| 267 | `_t1_qwen_temp_sweep_r2_selfcert.json` | `124051b56295720f6c85ed9d4b2a0300b90a290a02046d62cd9ffbcfde60dffd` | 6,353 | `_t1_qwen_temp_sweep_r2_selfcert.json` | `$IID4561.json` | `$RID4561.json` | ✅✅✅✅ | ✅ |
| 268 | `_t1_qwen_temp_sweep_readings.json` | `e5e8f024e42e61b5a6d6bbe6d74d6cc5b2aab38272fa0fc82733caed50070b0f` | 11,013 | `_t1_qwen_temp_sweep_readings.json` | `$I2MS5S7.json` | `$R2MS5S7.json` | ✅✅✅✅ | ✅ |
| 269 | `_t1_qwen_temp_sweep_records.json` | `5b51af62c6401015d1b4f14cbc42fe55d7a689b95800c7edab7f0a4ed99738b5` | 96,866 | `_t1_qwen_temp_sweep_records.json` | `$I6HX2WG.json` | `$R6HX2WG.json` | ✅✅✅✅ | ✅ |
| 270 | `_t1_qwen_temp_sweep_selfcert.json` | `91c2505deef3968f9066f84572b5aea3f6753369847007658329da2f02b5684f` | 3,866 | `_t1_qwen_temp_sweep_selfcert.json` | `$I9E3V89.json` | `$R9E3V89.json` | ✅✅✅✅ | ✅ |
| 271 | `_t1_r2_calib_max_tokens_2026_10_09.json` | `3f35aede29f676c329adec06cd38149a52b0a6571a4633819bc9c878899f49f3` | 3,305 | `_t1_r2_calib_max_tokens_2026_10_09.json` | `$I471VPL.json` | `$R471VPL.json` | ✅✅✅✅ | ✅ |
| 272 | `_t1_r2_calib_max_tokens_2026_10_09.py` | `7bbb0de0c00f209818c9463d0efe6d76e71766f0fef9db821cd8c068151e34d1` | 6,120 | `_t1_r2_calib_max_tokens_2026_10_09.py` | `$I3UAOAF.py` | `$R3UAOAF.py` | ✅✅✅✅ | ✅ |
| 273 | `_t1_r2_run_driver_2026_10_09.py` | `b71f4916bee16d9ae2a5a4bbac358de5b3c7b2e3c4a0d6f5fd4a91eac5f896c8` | 2,749 | `_t1_r2_run_driver_2026_10_09.py` | `$ICRBRCF.py` | `$RCRBRCF.py` | ✅✅✅✅ | ✅ |
| 274 | `_t1_r2_verify_2026_10_09.py` | `3ce6d45cfbf780bf7c4040d5c5529fa0775c523f0d3a8293c6735be94860bbe0` | 4,018 | `_t1_r2_verify_2026_10_09.py` | `$ICZRLML.py` | `$RCZRLML.py` | ✅✅✅✅ | ✅ |
| 275 | `_t1_verdict_probe_readonly.txt` | `0e2df9ca7ab282ba3c0afd49b011afc976c982f85a99174a4f4359be4880d736` | 4,655 | `_t1_verdict_probe_readonly.txt` | `$I5HHU7Y.txt` | `$R5HHU7Y.txt` | ✅✅✅✅ | ✅ |
| 276 | `_t2_t3_lit_search.py` | `0829d37e0cd8c1c67e208865eec52c86c11ca45db1e3817ade16e783035c4eae` | 5,695 | `_t2_t3_lit_search.py` | `$IUT0US6.py` | `$RUT0US6.py` | ✅✅✅✅ | ✅ |
| 277 | `_t2_t3_lit_search2.py` | `c0caa8ba29f15c10959d81e6731e3c6ebe23391a2044f05e77b522d847c0d43f` | 4,946 | `_t2_t3_lit_search2.py` | `$IVBFLS6.py` | `$RVBFLS6.py` | ✅✅✅✅ | ✅ |
| 278 | `_t2_t3_lit_search2_out.json` | `13ffff0d0b28d2cc4f98babb2101b09bf517877fe4c1b06f4d36a34e31e0eb8c` | 29,596 | `_t2_t3_lit_search2_out.json` | `$IWKVJNW.json` | `$RWKVJNW.json` | ✅✅✅✅ | ✅ |
| 279 | `_t2_t3_lit_search_out.json` | `cc70fac3d81b13688e50bc30cafe3633fe50137625a5fce523b8eae9197c35b0` | 26,588 | `_t2_t3_lit_search_out.json` | `$IKAJ0XD.json` | `$RKAJ0XD.json` | ✅✅✅✅ | ✅ |
| 280 | `_t2_t3_llm_probe.py` | `5561f7af56624fb33cf0412835d098379fcb1af53e3b772fc2f3b16ae196565e` | 4,544 | `_t2_t3_llm_probe.py` | `$IXW5PJ9.py` | `$RXW5PJ9.py` | ✅✅✅✅ | ✅ |
| 281 | `_t2_t3_llm_probe_out.json` | `993477af77db6e8bbe2b80f52fd491fa7bc059669d9d64cbf38719a46c3288d1` | 5,331 | `_t2_t3_llm_probe_out.json` | `$IC72R9D.json` | `$RC72R9D.json` | ✅✅✅✅ | ✅ |
| 282 | `_t2_t3_prex_a_route.py` | `c25af5d2966bf19dacc50ba1dfaa5939ba091600fa716fca9f281ff0d84c62c0` | 10,166 | `_t2_t3_prex_a_route.py` | `$I5F0I3H.py` | `$R5F0I3H.py` | ✅✅✅✅ | ✅ |
| 283 | `_t2_t3_prex_a_route2.py` | `0c44afba463a79fd32755048e9954b66665f4eedca18a82740efa47fda53e19d` | 5,850 | `_t2_t3_prex_a_route2.py` | `$IN4X5LV.py` | `$RN4X5LV.py` | ✅✅✅✅ | ✅ |
| 284 | `_t2_t3_prex_a_route2_out.json` | `63f37ba943c1fcde76248fa8023f39557fa96c004356924c2bfcfebde3c0be1d` | 6,949 | `_t2_t3_prex_a_route2_out.json` | `$IE647L5.json` | `$RE647L5.json` | ✅✅✅✅ | ✅ |
| 285 | `_t2_t3_prex_a_route_out.json` | `3cad087a69c37ca0d5305d35caa112ad46c76958a94e9fb8a604eff333fadb2e` | 22,640 | `_t2_t3_prex_a_route_out.json` | `$I2FD5KH.json` | `$R2FD5KH.json` | ✅✅✅✅ | ✅ |
| 286 | `_tail3_atomic_landing_check_2026_09_29.py` | `5c19cf8f29fb3c2b8b1a23de3ffcce69b23ef153c5eb26c461abd683f6a33ae9` | 2,699 | `_tail3_atomic_landing_check_2026_09_29.py` | `$IP1MQZ5.py` | `$RP1MQZ5.py` | ✅✅✅✅ | ✅ |
| 287 | `_tail3_atomic_make_2026_09_29.py` | `94d57549533b4be94e37fb6d5f6ec219df246dee7bc6d2fac922300ca0d63810` | 17,272 | `_tail3_atomic_make_2026_09_29.py` | `$IWHEH6G.py` | `$RWHEH6G.py` | ✅✅✅✅ | ✅ |
| 288 | `_tail3_atomic_refs_2026_09_29.py` | `4e8ea9bea9487269f3df8aac225d83e98b8c3873e371c291c3d7b66ad55254ee` | 2,636 | `_tail3_atomic_refs_2026_09_29.py` | `$IZO8ELX.py` | `$RZO8ELX.py` | ✅✅✅✅ | ✅ |
| 289 | `_tail3_atomic_verify_2026_09_29.py` | `8d12c9c9cb2d295a739d56b8d952be3f03871adce4ec25684bef047d74ed085a` | 21,338 | `_tail3_atomic_verify_2026_09_29.py` | `$I41DVPW.py` | `$R41DVPW.py` | ✅✅✅✅ | ✅ |
| 290 | `_tail_only.py` | `cf3bbd24b4011a3440f9e61035c4e25851320d23a4766e4e202c2000a321ac8f` | 436 | `_tail_only.py` | `$IAD0OMN.py` | `$RAD0OMN.py` | ✅✅✅✅ | ✅ |
| 291 | `_trae_audit_part1.py` | `ac67b341b56b97e6abc1a9db57e83edd306acba9e471db3784644c7a1db693fe` | 5,510 | `_trae_audit_part1.py` | `$IOJJNMQ.py` | `$ROJJNMQ.py` | ✅✅✅✅ | ✅ |
| 292 | `_trae_audit_part2.py` | `9faaa564c3bc3784815609945e946c3fbadeb3a28c48d1102ef2c0804563af98` | 3,632 | `_trae_audit_part2.py` | `$IQQELG4.py` | `$RQQELG4.py` | ✅✅✅✅ | ✅ |
| 293 | `_trae_audit_part3.py` | `f4c9940043115a20bf760f646d72bc170c9d82fe64892d25d67a7cf7bcafaa69` | 8,617 | `_trae_audit_part3.py` | `$ITTIJVZ.py` | `$RTTIJVZ.py` | ✅✅✅✅ | ✅ |
| 294 | `_trae_audit_part3b.py` | `c1a9a6c3c17ab68b4244a709d54ff9406a4c31a0b4ec1795e19293259aa3101d` | 7,662 | `_trae_audit_part3b.py` | `$IY6Y79N.py` | `$RY6Y79N.py` | ✅✅✅✅ | ✅ |
| 295 | `_trae_audit_part4.py` | `bc8d4721bf3baf2f9ce1073045bb29162ae95b068480ce0e7639f7c62e45058e` | 7,173 | `_trae_audit_part4.py` | `$ISPTQ1L.py` | `$RSPTQ1L.py` | ✅✅✅✅ | ✅ |
| 296 | `_v412_contrib.py` | `1085411b4896ff8e552056a93b44cf0053f84825954bdd9aae7441593cdb42d1` | 1,040 | `_v412_contrib.py` | `$I67H0NO.py` | `$R67H0NO.py` | ✅✅✅✅ | ✅ |
| 297 | `_v412_material_scan.py` | `f3493907cbe2bd2e3cb80e8885f8de68afc0275d0c5949a16b9f1b45729d19df` | 627 | `_v412_material_scan.py` | `$I8WHO8N.py` | `$R8WHO8N.py` | ✅✅✅✅ | ✅ |
| 298 | `_v412_unique_scan.py` | `b2e381f098288676c885e76ea34cab0a565a5ac3933b8865d0ebc53cd05f004e` | 1,300 | `_v412_unique_scan.py` | `$IJLTV7W.py` | `$RJLTV7W.py` | ✅✅✅✅ | ✅ |
| 299 | `_v5_c5_b_clause4_consistency_check.py` | `56ad3329a3c77820e5ce8b9aa5216045495fe1746dfa2fc3ee4a302e6b3e75ee` | 6,528 | `_v5_c5_b_clause4_consistency_check.py` | `$I4YZT65.py` | `$R4YZT65.py` | ✅✅✅✅ | ✅ |
| 300 | `_v5_c5_b_fetch_raw_embeddings.py` | `8e4f2ae63de3a1010bb5ba3f2d363b058725ab6f110a729e8eaf3f9e49973389` | 9,476 | `_v5_c5_b_fetch_raw_embeddings.py` | `$IN0U6T6.py` | `$RN0U6T6.py` | ✅✅✅✅ | ✅ |
| 301 | `_v5_c5_b_fix_readings_2026_10_01.py` | `191efa7fe0b6ed0f011c7b957866e5faea9b30732efe906d852b98a964a5d28c` | 12,014 | `_v5_c5_b_fix_readings_2026_10_01.py` | `$IRJN9E1.py` | `$RRJN9E1.py` | ✅✅✅✅ | ✅ |
| 302 | `_v5_item21_anchor_driver.py` | `cb14f672dd1e4b0ccc8375f3078db8d2c479baba88c8f239923dee3a9a342a1c` | 5,401 | `_v5_item21_anchor_driver.py` | `$IIT0I9M.py` | `$RIT0I9M.py` | ✅✅✅✅ | ✅ |
| 303 | `_v5_loadcorpus_verify_2026_09_29.py` | `564e3575ab1d9f53fa29a72691f66311125958ee3069fbe46bb505eae815c0c3` | 8,798 | `_v5_loadcorpus_verify_2026_09_29.py` | `$I0JT0YF.py` | `$R0JT0YF.py` | ✅✅✅✅ | ✅ |
| 304 | `_v5_qwen_retry_candidates_20260929.py` | `f42600827cc3bd0cb0f31c0a038033cf9eadbd094e6747927613ec8d428e5ada` | 1,689 | `_v5_qwen_retry_candidates_20260929.py` | `$I2VY3GE.py` | `$R2VY3GE.py` | ✅✅✅✅ | ✅ |
| 305 | `_v5_qwen_retry_introspect_20260929.py` | `117b64fc1d5b1ad62f11dea7abb6185359a3335bed05be279d2a1faa28ea7acb` | 3,149 | `_v5_qwen_retry_introspect_20260929.py` | `$IAO4YC8.py` | `$RAO4YC8.py` | ✅✅✅✅ | ✅ |
| 306 | `_verdict_keeper_sha_helper.ps1` | `bc11b03d3b84af8a8e3e9a6926901b5dcbe91b8084b86377b9eb4332e3e7b111` | 679 | `_verdict_keeper_sha_helper.ps1` | `$IH7EQZC.ps1` | `$RH7EQZC.ps1` | ✅✅✅✅ | ✅ |
| 307 | `_verify_d8_addendum_2026_09_30.py` | `28de8c99c05437387da0deda4f1d8a06e2cb1b4af24bf3117e6a98c938fa3187` | 4,900 | `_verify_d8_addendum_2026_09_30.py` | `$IPK8E7G.py` | `$RPK8E7G.py` | ✅✅✅✅ | ✅ |
| 308 | `_verify_intake_supplement_6.py` | `1fbb1bd1db6c9b80dc0cf2592513ef9cdf25b415f627aafc8e85d78a59d4e589` | 3,678 | `_verify_intake_supplement_6.py` | `$I7BNKLL.py` | `$R7BNKLL.py` | ✅✅✅✅ | ✅ |
| 309 | `_verify_r32_card_2026_10_10.py` | `61f99fc5fdb9106650d3bb2bf267438631ce8bbe19733f6847f4d7420265873a` | 631 | `_verify_r32_card_2026_10_10.py` | `$IKJ6ELL.py` | `$RKJ6ELL.py` | ✅✅✅✅ | ✅ |
| 310 | `_verify_tail.py` | `23198a6a0a9b4ed46eba20491707da8fa580275295a798fc3a8f4d949bcd46c9` | 733 | `_verify_tail.py` | `$IOYFJ6W.py` | `$ROYFJ6W.py` | ✅✅✅✅ | ✅ |
| 311 | `_verify_two_pieces_2026_09_30.py` | `509afa876df0d647f482cf0d4f213aede5a91b31ff545367b72820fc79f5a010` | 4,739 | `_verify_two_pieces_2026_09_30.py` | `$IW13VGN.py` | `$RW13VGN.py` | ✅✅✅✅ | ✅ |
| 312 | `_vk_pv02_recheck_a.py` | `37d55bf0fba6b54a82b62f12681288e270450ecb6ae2cfa2f50a5201051bfbcd` | 4,188 | `_vk_pv02_recheck_a.py` | `$I4YKTD3.py` | `$R4YKTD3.py` | ✅✅✅✅ | ✅ |
| 313 | `_vk_pv02_recheck_b.py` | `fe0f10e38bb37041358a440659b98d2aeeaa5013c72e23943c7ccb872f6f8204` | 1,646 | `_vk_pv02_recheck_b.py` | `$IV0GTKV.py` | `$RV0GTKV.py` | ✅✅✅✅ | ✅ |
| 314 | `_vk_pv02_recheck_c.py` | `7d35b715f8e22dd1a805f3be7213c5931ca790f7efb5cd3a0164d118b9df1f58` | 2,397 | `_vk_pv02_recheck_c.py` | `$IBW9NJS.py` | `$RBW9NJS.py` | ✅✅✅✅ | ✅ |
| 315 | `_vk_pv02_recheck_d.py` | `7ae7ed6bcd8add4e68d6ecfc8250c50ced2824212887db903434a11441099ea7` | 982 | `_vk_pv02_recheck_d.py` | `$IO664WV.py` | `$RO664WV.py` | ✅✅✅✅ | ✅ |
| 316 | `_vk_pv02_recheck_e.py` | `d925e60c1d3cba119f245a84bc7f683ea019af63570606c575987ed880a043c6` | 1,742 | `_vk_pv02_recheck_e.py` | `$I83WFFW.py` | `$R83WFFW.py` | ✅✅✅✅ | ✅ |
| 317 | `_vk_pv02_recheck_f.py` | `c2e298ccebc60795a652cf6449d8d688f60d98f65a0986c030376bfa0c29d120` | 1,522 | `_vk_pv02_recheck_f.py` | `$IRCMF3D.py` | `$RRCMF3D.py` | ✅✅✅✅ | ✅ |
| 318 | `_vk_pv02_recheck_g.py` | `f237e1d2715f0da9fda214a677326db20f7bd9b707c76f366ca91e14860e2246` | 2,269 | `_vk_pv02_recheck_g.py` | `$I892UM8.py` | `$R892UM8.py` | ✅✅✅✅ | ✅ |
| 319 | `_vk_q.py` | `67364902116c76c7bab68b09dceae432ce1e849a29883fff25e50e5f12c6a6c3` | 519 | `_vk_q.py` | `$IB9QOD2.py` | `$RB9QOD2.py` | ✅✅✅✅ | ✅ |
| 320 | `_vk_q2.py` | `d5759d40dc43df3110eb3c727f6ada2ad9bfcbbf20aad5cd61dadf357f3b8057` | 540 | `_vk_q2.py` | `$IFVQAAD.py` | `$RFVQAAD.py` | ✅✅✅✅ | ✅ |
| 321 | `_vk_q3.py` | `a00cd309205f04b8ce2dc5da83ad4519822556598b2de1133043fa8b46b831bb` | 612 | `_vk_q3.py` | `$IM9L0RK.py` | `$RM9L0RK.py` | ✅✅✅✅ | ✅ |
| 322 | `_vk_q4.py` | `defc3c53b7df4ce785cfcc14d8e451b08d47338cad80f5383fd7f013fbb3c804` | 784 | `_vk_q4.py` | `$IHH7NJN.py` | `$RHH7NJN.py` | ✅✅✅✅ | ✅ |
| 323 | `_vk_q5.py` | `7b95307225bafb725bfb11cf27e7009f2abf51c7ac7eae99d254f9084257081a` | 1,246 | `_vk_q5.py` | `$II60JQL.py` | `$RI60JQL.py` | ✅✅✅✅ | ✅ |
| 324 | `_vk_q6.py` | `7da34dd24eb07d8f9cb6aba056a0e0e63c266e14d345216846453e292cded188` | 811 | `_vk_q6.py` | `$IYVMJDI.py` | `$RYVMJDI.py` | ✅✅✅✅ | ✅ |
| 325 | `_vk_q7.py` | `a6c525f88f119b849eb62a34230e770e732b5e23d7d171e52a687a7e476a27f7` | 1,331 | `_vk_q7.py` | `$I2ME1SM.py` | `$R2ME1SM.py` | ✅✅✅✅ | ✅ |
| 326 | `_vk_q8.py` | `5a81e5558c7251fefa1e62c5b5ae2c6c64a51625aa9459bdfbd9b2e5150f4432` | 1,025 | `_vk_q8.py` | `$I7ETV6Y.py` | `$R7ETV6Y.py` | ✅✅✅✅ | ✅ |
| 327 | `_vk_s4_topup_intake_recheck_2026_10_09.py` | `a1d8047f18330d1c3860e67b3b8a23ead516c8581eee4258b1c32678736176f5` | 6,678 | `_vk_s4_topup_intake_recheck_2026_10_09.py` | `$ITTHIE0.py` | `$RTTHIE0.py` | ✅✅✅✅ | ✅ |
| 328 | `_vk_s4_topup_intake_recheck_2026_10_09.txt` | `683501b8fb411187458503a7528580f0fe5e5665062c69d1bbdab626c51b9b50` | 7,098 | `_vk_s4_topup_intake_recheck_2026_10_09.txt` | `$IQ45322.txt` | `$RQ45322.txt` | ✅✅✅✅ | ✅ |
| 329 | `_w1_collect.py` | `7c3155b2c3700e89f5863495d7e8a6c9692e814751456b375a79e62ea366f7c4` | 19,559 | `_w1_collect.py` | `$IM5I9U1.py` | `$RM5I9U1.py` | ✅✅✅✅ | ✅ |
| 330 | `_w1_drift_write.py` | `44e026ae190db5cfa03cfa60d0e0e588d3e7caebd37ae55cc5b07d8c33bec751` | 16,560 | `_w1_drift_write.py` | `$IWVI3FP.py` | `$RWVI3FP.py` | ✅✅✅✅ | ✅ |
| 331 | `_w1_freeze_write.py` | `97211806b0d0ee82ffa4f0657864eaf4f3ceaaf85cf04dad16cd4b8c3e1b8f99` | 24,351 | `_w1_freeze_write.py` | `$IO18DUV.py` | `$RO18DUV.py` | ✅✅✅✅ | ✅ |
| 332 | `_w1_phaseB_write.py` | `4e85afe94966b527e1911d0f791db9554aa09c43d4486acbc3ad1dcb0e3b4bab` | 31,303 | `_w1_phaseB_write.py` | `$IOA02F8.py` | `$ROA02F8.py` | ✅✅✅✅ | ✅ |
| 333 | `_w1_verify_final.py` | `040c35e21bf2e83c0abb855e687a4abc2babef08b9b596419077f48f460ee359` | 7,944 | `_w1_verify_final.py` | `$IDRIDSI.py` | `$RDRIDSI.py` | ✅✅✅✅ | ✅ |
| 334 | `_w5_9model_merge_2026_10_09.py` | `afa52e90f332b31f2c510c3addfc9c93ae5f812598e299150612a97073138061` | 18,475 | `_w5_9model_merge_2026_10_09.py` | `$IPF9YSX.py` | `$RPF9YSX.py` | ✅✅✅✅ | ✅ |
| 335 | `_worker_write_ge01_unblock_progress.py` | `7c18f854316c1d6c228088a1ed1399c1204ff91a645ad2f833d56f52f14b5fa0` | 26,125 | `_worker_write_ge01_unblock_progress.py` | `$IEQ6BQN.py` | `$REQ6BQN.py` | ✅✅✅✅ | ✅ |
| 336 | `_write_canonical_register.py` | `867acc46aff9b7d5ef5be5035e4d219947d4710cc4091929adbf493ead385d90` | 24,636 | `_write_canonical_register.py` | `$I652Z9O.py` | `$R652Z9O.py` | ✅✅✅✅ | ✅ |
| 337 | `_write_eps_grid_design.py` | `df37b02f1c0f041bb5aac968513207d4cce3617a5736aea51f25255e5416afec` | 38,246 | `_write_eps_grid_design.py` | `$IQ7IZDW.py` | `$RQ7IZDW.py` | ✅✅✅✅ | ✅ |
| 338 | `_write_predelete_caliber_draft.py` | `82d7f9c628b618ac01719728aeb1f50c5793c42e2971840da090cee422ac803a` | 32,826 | `_write_predelete_caliber_draft.py` | `$IES7T7V.py` | `$RES7T7V.py` | ✅✅✅✅ | ✅ |
| 339 | `anch.py` | `c05693efbb30036a62decfb7953621e2db06fb3a884810fe70c42725fefcb29c` | 1,484 | `anch.py` | `$IQHPCN8.py` | `$RQHPCN8.py` | ✅✅✅✅ | ✅ |
| 340 | `anch_v4_build.py` | `adcae459701a32bc803357663ef1d8aaccf3e8da22a221d95b00ecc018a29a38` | 7,175 | `anch_v4_build.py` | `$IQHA3CI.py` | `$RQHA3CI.py` | ✅✅✅✅ | ✅ |
| 341 | `anch_v4_build_measurements.json` | `5708226b943fecc0bec6cd06c363878df9e43cd78d830cdcc81dcb92f4bffd8c` | 2,315 | `anch_v4_build_measurements.json` | `$IFYJDKW.json` | `$RFYJDKW.json` | ✅✅✅✅ | ✅ |
| 342 | `anch_v4_probe.py` | `f47af093e3aa6ba6df4fa278b771e5bb1266cebbae261f060e248f34cee80009` | 2,662 | `anch_v4_probe.py` | `$II3VE8J.py` | `$RI3VE8J.py` | ✅✅✅✅ | ✅ |
| 343 | `archive_survey_census2.py` | `2863f5edca41cf8a1969d215bc38f77159b81d13a71951d5ba3e4aae7a5b0c2b` | 780 | `archive_survey_census2.py` | `$I3MDS9D.py` | `$R3MDS9D.py` | ✅✅✅✅ | ✅ |
| 344 | `claude_spotcheck.py` | `a78755b356b902be1f24f37c07ba223ecec55f79894864dca8ba95b332000701` | 4,136 | `claude_spotcheck.py` | `$IDSO8GA.py` | `$RDSO8GA.py` | ✅✅✅✅ | ✅ |
| 345 | `cleanup511_manifest_2026_10_17.json` | `b7093a701856b9fb928e624e6f0aa717d858783f1789d7a0c08a06592f5638aa` | 1,754,609 | `cleanup511_manifest_2026_10_17.json` | `$I79KSP4.json` | `$R79KSP4.json` | ✅✅✅✅ | ✅ |
| 346 | `collision_survey_hashes.json` | `0329afb1e9fcc58a3372120b92ee86282001269516f5163e47f4fa21dc754192` | 75,439 | `collision_survey_hashes.json` | `$ICN8TA8.json` | `$RCN8TA8.json` | ✅✅✅✅ | ✅ |
| 347 | `collision_survey_inventory.json` | `a4cd5b2fc5c8d31101f6cfecfa91ba4ac7f5b30e7c21081981978f70fef0a854` | 37,588 | `collision_survey_inventory.json` | `$IG751VW.json` | `$RG751VW.json` | ✅✅✅✅ | ✅ |
| 348 | `combo_llm_calls_2026_10_16.jsonl` | `86f05646031b09c0905998c7725faa245acbf4278895c7d0d4de31cc67f7cae3` | 59,626 | `combo_llm_calls_2026_10_16.jsonl` | `$IW6DN52.jsonl` | `$RW6DN52.jsonl` | ✅✅✅✅ | ✅ |
| 349 | `combo_measurement_2026_10_16.json` | `27609799e40ee2b274070fde2b4d1004d787ebbdb288684fc12aaaec9a1442e4` | 121,779 | `combo_measurement_2026_10_16.json` | `$IG9GQZP.json` | `$RG9GQZP.json` | ✅✅✅✅ | ✅ |
| 350 | `d05_hash_index.py` | `070b6f865eba37ae36f0f8894590f9d550d4d319dd237a2474b89001b45f93bc` | 1,004 | `d05_hash_index.py` | `$IX313LK.py` | `$RX313LK.py` | ✅✅✅✅ | ✅ |
| 351 | `d1fill_anchor_snapshot.py` | `15c0b0ade7abfedcabc1d62c1e94f581617f066a9c7ee1eb99ba37a4f4d5dd54` | 1,985 | `d1fill_anchor_snapshot.py` | `$I4ZCV63.py` | `$R4ZCV63.py` | ✅✅✅✅ | ✅ |
| 352 | `d1fill_recount_checks.py` | `b8af087b5e1f3020c89641f6bcfc5e6a481227ca020667216ce229e8699d8d74` | 2,336 | `d1fill_recount_checks.py` | `$I1R81R7.py` | `$R1R81R7.py` | ✅✅✅✅ | ✅ |
| 353 | `d1fill_recount_impl1.py` | `bb30ad15c89b0e7e66ff557d1c408c1c7a6d2c7b935a8513235231ea97aa3c97` | 6,464 | `d1fill_recount_impl1.py` | `$IPCLGAT.py` | `$RPCLGAT.py` | ✅✅✅✅ | ✅ |
| 354 | `d1fill_recount_impl2.ps1` | `88411408e6716ee347417d9e9d003f99cc91fea8c043c332a969ad47ddac2546` | 6,132 | `d1fill_recount_impl2.ps1` | `$IN481CU.ps1` | `$RN481CU.ps1` | ✅✅✅✅ | ✅ |
| 355 | `diag.py` | `db20dd0e6efb290850253ed7864e0df2dcc9deb214aab5dbecf612d3e909462a` | 972 | `diag.py` | `$I5I6O1Z.py` | `$R5I6O1Z.py` | ✅✅✅✅ | ✅ |
| 356 | `diffcause.py` | `2b24513cdf74d9d0851b68219646cccff093a7b71d88c5a9566bd1b56ada2c93` | 2,724 | `diffcause.py` | `$IJ42TOY.py` | `$RJ42TOY.py` | ✅✅✅✅ | ✅ |
| 357 | `docwriter_c2_effect_census.json` | `1ef99b1da14de10e4445fbc96b8ab5dbf0908804ecc974eb26bbb42db544c931` | 36,157 | `docwriter_c2_effect_census.json` | `$IRRYYMO.json` | `$RRRYYMO.json` | ✅✅✅✅ | ✅ |
| 358 | `docwriter_c2_effect_census.py` | `a8e52d7e9f8dd7273c673802979c930dda9ce6e4cd25bc7daf0141006418bead` | 5,518 | `docwriter_c2_effect_census.py` | `$INQU97T.py` | `$RNQU97T.py` | ✅✅✅✅ | ✅ |
| 359 | `docwriter_c2_effect_table.py` | `503230d1e7e391b6bcbfe16c5a49ea67e2040f7d1278693bbb6ab3f9d248fe3e` | 1,400 | `docwriter_c2_effect_table.py` | `$IRNV3NR.py` | `$RRNV3NR.py` | ✅✅✅✅ | ✅ |
| 360 | `docwriter_c2_effect_table.txt` | `1b5382cc9936ec91790e45d2dc2f228d6f76aa91e0e10a18b727802329472631` | 21,554 | `docwriter_c2_effect_table.txt` | `$I3ENISK.txt` | `$R3ENISK.txt` | ✅✅✅✅ | ✅ |
| 361 | `docwriter_sigsup.py` | `d116fefd336cb3d4d42336076816a0c98a1e8108f3aec1fa46bb797247217237` | 13,645 | `docwriter_sigsup.py` | `$I4ZRBED.py` | `$R4ZRBED.py` | ✅✅✅✅ | ✅ |
| 362 | `docwriter_v41_probe.py` | `210a07303fe7516801ff529b051c516744383a8644e20da9d0653cc34049f44a` | 6,503 | `docwriter_v41_probe.py` | `$I07DYWQ.py` | `$R07DYWQ.py` | ✅✅✅✅ | ✅ |
| 363 | `docwriter_v41_scan2.json` | `e988b26ba229c4588ab8e1a27b55b78c6f2fde7527b771f56a8007b5d9230ddd` | 4,066 | `docwriter_v41_scan2.json` | `$IA3CHCJ.json` | `$RA3CHCJ.json` | ✅✅✅✅ | ✅ |
| 364 | `docwriter_v41_scan2.py` | `e88316a0fc2ccf824cfa6463c07b9b614e26372aa92f7e44fc5ec10b871bf08d` | 3,661 | `docwriter_v41_scan2.py` | `$I65JJ4K.py` | `$R65JJ4K.py` | ✅✅✅✅ | ✅ |
| 365 | `docwriter_v42_scan.py` | `93d9c4c5c92718c38594e3e901123bfcd3c2007fc4bfe83826589ffce1c1c4c5` | 4,601 | `docwriter_v42_scan.py` | `$I4M3SWZ.py` | `$R4M3SWZ.py` | ✅✅✅✅ | ✅ |
| 366 | `docwriter_v42_scan_out.txt` | `d1470a9eaea95508a41ace535bd1182c93fe119c62efc0e5be8e0a2e4d0cfd86` | 5,267 | `docwriter_v42_scan_out.txt` | `$I0GQ31N.txt` | `$R0GQ31N.txt` | ✅✅✅✅ | ✅ |
| 367 | `docwriter_v42_verify.py` | `47c794a64dff0905de99fe15f6d32bae6d466f90b6e3258cf23a23993048bf83` | 4,858 | `docwriter_v42_verify.py` | `$IFK53QP.py` | `$RFK53QP.py` | ✅✅✅✅ | ✅ |
| 368 | `docwriter_v42_verify_out.txt` | `c38b853adda18a5cb43fe6a28045df24715e6a70c2eaeb8678afd1d1ca6aa3b5` | 2,899 | `docwriter_v42_verify_out.txt` | `$IUEK3I3.txt` | `$RUEK3I3.txt` | ✅✅✅✅ | ✅ |
| 369 | `docwriter_v43_fp.py` | `000c7e036d9c80555264394f6dd754b99db9ad083a3d966302c6297a262796de` | 1,488 | `docwriter_v43_fp.py` | `$IGCB3AZ.py` | `$RGCB3AZ.py` | ✅✅✅✅ | ✅ |
| 370 | `docwriter_v43_fp2.py` | `87ef5d8aba152c2092a5c6a844f8791d44d6e1324590fb695587cd511f221f79` | 1,716 | `docwriter_v43_fp2.py` | `$IXRJ794.py` | `$RXRJ794.py` | ✅✅✅✅ | ✅ |
| 371 | `docwriter_v43_fp_out.txt` | `35a223091bbe5137a9072ff80b4a6bea24ccb3424d3a05f7410d99921d106f35` | 2,420 | `docwriter_v43_fp_out.txt` | `$I71CT1S.txt` | `$R71CT1S.txt` | ✅✅✅✅ | ✅ |
| 372 | `docwriter_v43_scan.py` | `5356708d6a6f144fb78e2e6f5fc0f10346a71b99b480b4ed17a823c15570c376` | 2,061 | `docwriter_v43_scan.py` | `$IL78XBP.py` | `$RL78XBP.py` | ✅✅✅✅ | ✅ |
| 373 | `docwriter_v43_scan_out.txt` | `c80e849e7c995ed6eeadb1b0ef2e4153d484fea6903b7846b71ebdd9dbc9def1` | 2,353 | `docwriter_v43_scan_out.txt` | `$I9PXQLG.txt` | `$R9PXQLG.txt` | ✅✅✅✅ | ✅ |
| 374 | `docwriter_v43_verify.py` | `2cf26203f12d7a6782edff49707afbc1916c7d10e5eddc2b4a4d0a7bfa07b226` | 4,497 | `docwriter_v43_verify.py` | `$IN8XO9F.py` | `$RN8XO9F.py` | ✅✅✅✅ | ✅ |
| 375 | `docwriter_v43_verify_out.txt` | `c1d14e3d7e06c39ebb9098fadc0be42da7c2fc62f92c53800cc7521a8c544976` | 759 | `docwriter_v43_verify_out.txt` | `$IRZ8TVR.txt` | `$RRZ8TVR.txt` | ✅✅✅✅ | ✅ |
| 376 | `docwriter_v44_fp.py` | `4c2e2a4a2ad220416fee2bc7d59b471aa03a79cced073af7c7ae3641b8827bc5` | 2,485 | `docwriter_v44_fp.py` | `$IEMAD6N.py` | `$REMAD6N.py` | ✅✅✅✅ | ✅ |
| 377 | `docwriter_v44_fp_out.txt` | `6ab1382d766ea8627c41292dc08a6b2aaef11ec205397f61b40c258741a7f0e2` | 1,601 | `docwriter_v44_fp_out.txt` | `$IQ3I9AI.txt` | `$RQ3I9AI.txt` | ✅✅✅✅ | ✅ |
| 378 | `docwriter_v44_fresh.py` | `855298e666f6832c128990ea1aa1900f4f6be9942d8e0fd0adc649709328eed2` | 2,319 | `docwriter_v44_fresh.py` | `$I0ISDTB.py` | `$R0ISDTB.py` | ✅✅✅✅ | ✅ |
| 379 | `docwriter_v44_fresh_out.txt` | `6d7d8ad5c4edb0271a8e80eaf5e9537499ffb5afb63a86ac8b7107ecb39b2e7f` | 1,646 | `docwriter_v44_fresh_out.txt` | `$I02OKTE.txt` | `$R02OKTE.txt` | ✅✅✅✅ | ✅ |
| 380 | `docwriter_v44_scan.py` | `3cc9fa3130a4013413bd6b381c1fdd75a56cdb7a1e71b7cc6292f7025d905b3a` | 3,822 | `docwriter_v44_scan.py` | `$IZZ1YZY.py` | `$RZZ1YZY.py` | ✅✅✅✅ | ✅ |
| 381 | `docwriter_v44_scan_out.txt` | `24663bc22391354e5a7f77c2c4de56b673787bc6f7aeb1dfc774b01e0dd609dd` | 2,290 | `docwriter_v44_scan_out.txt` | `$I9PBXVK.txt` | `$R9PBXVK.txt` | ✅✅✅✅ | ✅ |
| 382 | `docwriter_v45_scan.py` | `c6703629a7b0f0678dd4a1bf64cb2c088aaf26b036d71828bfb7040ea5b29da8` | 5,186 | `docwriter_v45_scan.py` | `$IS35AVM.py` | `$RS35AVM.py` | ✅✅✅✅ | ✅ |
| 383 | `docwriter_v45_scan_out.txt` | `28c06dd53ae479255f3dfd63d74557d7f74a1ae7819a3b9d83c9271fb85a6bc9` | 1,661 | `docwriter_v45_scan_out.txt`, `docwriter_v45_scan_out_r1.txt` | `$I92HRIW.txt` | `$R92HRIW.txt` | ✅✅✅✅ | ✅ |
| 384 | `docwriter_v45_scan_out_r1.txt` | `28c06dd53ae479255f3dfd63d74557d7f74a1ae7819a3b9d83c9271fb85a6bc9` | 1,661 | `docwriter_v45_scan_out.txt`, `docwriter_v45_scan_out_r1.txt` | `$IBM2XM5.txt` | `$RBM2XM5.txt` | ✅✅✅✅ | ✅ |
| 385 | `docwriter_v45_scan_out_r2.txt` | `ef49039e5d902b1191687bbb9f015e227a2088f994c4bb5d181f97bcba470804` | 1,728 | `docwriter_v45_scan_out_r2.txt` | `$I62K90X.txt` | `$R62K90X.txt` | ✅✅✅✅ | ✅ |
| 386 | `docwriter_v45_scan_r2.py` | `189764eebc913880d31bf4501494545cc1ead86f07cf8b5116c31f31fc6b60de` | 4,212 | `docwriter_v45_scan_r2.py` | `$IVXXXKJ.py` | `$RVXXXKJ.py` | ✅✅✅✅ | ✅ |
| 387 | `docwriter_v45_verify_out.txt` | `e5a0fdfbc9145b064736065ea79f6cc29f7550694390c4ea4f05907dfbb20e05` | 2,031 | `docwriter_v45_verify_out.txt` | `$IHDNANL.txt` | `$RHDNANL.txt` | ✅✅✅✅ | ✅ |
| 388 | `docwriter_v46_card_raw.py` | `b8754c12612b65bc33d62b05582bb6fe2255c1ae6d7cc207d367b18c035c88af` | 1,652 | `docwriter_v46_card_raw.py` | `$I280VXV.py` | `$R280VXV.py` | ✅✅✅✅ | ✅ |
| 389 | `docwriter_v46_card_raw.txt` | `e31064337198c4fee065a69afe5a3115c9eb02dcdc2b95a9dba7c239f5d6303c` | 26 | `docwriter_v46_card_raw.txt` | `$I5PP645.txt` | `$R5PP645.txt` | ✅✅✅✅ | ✅ |
| 390 | `docwriter_v46_probe.py` | `15d2a2cef38c4a956530e6f3e5a850f1511fff55f85b2a0a743f3c1645746087` | 8,174 | `docwriter_v46_probe.py` | `$IY3XJ3N.py` | `$RY3XJ3N.py` | ✅✅✅✅ | ✅ |
| 391 | `docwriter_v46_probe_out.txt` | `45358bad9e37f25461b161ddef691a44291fb62a0f540db227f527f4e1c28b97` | 10,158 | `docwriter_v46_probe_out.txt` | `$IBBO4XJ.txt` | `$RBBO4XJ.txt` | ✅✅✅✅ | ✅ |
| 392 | `docwriter_v46_timeshift_out.txt` | `4623d2f470da02abf5e48329162c3fb28f1df3d348fdc6ced578d631e6ae24bb` | 708 | `docwriter_v46_timeshift_out.txt` | `$IYYCOEV.txt` | `$RYYCOEV.txt` | ✅✅✅✅ | ✅ |
| 393 | `docwriter_v46_verify.py` | `7d657b923cf3d465b13a237004334e9056d4a56c1c1356ffd73159d0430e2be3` | 6,883 | `docwriter_v46_verify.py` | `$IGZBMPU.py` | `$RGZBMPU.py` | ✅✅✅✅ | ✅ |
| 394 | `docwriter_v46_verify_r2.py` | `98878b7016536212eb951f1d8c300c7b1309297689e1a036a74fea978d738341` | 3,940 | `docwriter_v46_verify_r2.py` | `$IXLDYJS.py` | `$RXLDYJS.py` | ✅✅✅✅ | ✅ |
| 395 | `docwriter_v47_verify.py` | `9383724baaa4f9809548995203707da6aed1d0fec04bbd56d586bc633cf5944a` | 1,220 | `docwriter_v47_verify.py` | `$ISJBNOF.py` | `$RSJBNOF.py` | ✅✅✅✅ | ✅ |
| 396 | `docwriter_v47_write1.py` | `8fa8d72c3a6911dbf14c71633fe11da4c5b78d791bbe85dba0f3681fb852f5f2` | 62,466 | `docwriter_v47_write1.py` | `$IFW78UM.py` | `$RFW78UM.py` | ✅✅✅✅ | ✅ |
| 397 | `docwriter_v47_write2.py` | `1ee1ee14ac3e5976d7271cb89d62d62c63921193bce26e56b20d91eac4e2cc41` | 48,627 | `docwriter_v47_write2.py` | `$I0WUEZQ.py` | `$R0WUEZQ.py` | ✅✅✅✅ | ✅ |
| 398 | `docwriter_v48_norm.py` | `e39ea2ab27564cfdeec487ab1f217259465a838ccfe9285840edc4abc972f639` | 12,880 | `docwriter_v48_norm.py` | `$I6FCVTQ.py` | `$R6FCVTQ.py` | ✅✅✅✅ | ✅ |
| 399 | `docwriter_v48_probe.py` | `8dfd0f40cdb5ee35dc69a47f54cb157671a837b316a679a9955f88c7e516874e` | 4,448 | `docwriter_v48_probe.py` | `$I4A5MPF.py` | `$R4A5MPF.py` | ✅✅✅✅ | ✅ |
| 400 | `docwriter_v48_probe_out.txt` | `48b1c4a81ad4350285ac98bb3dd8237b126f2c584e80316d961f0bcffe744065` | 4,169 | `docwriter_v48_probe_out.txt` | `$IMHR3WH.txt` | `$RMHR3WH.txt` | ✅✅✅✅ | ✅ |
| 401 | `docwriter_v49_norm.py` | `d1b3481335ebcca8f4aac05c645dc3c094ff3d0b371cc113f0a9343ece893626` | 16,740 | `docwriter_v49_norm.py` | `$ID86YN0.py` | `$RD86YN0.py` | ✅✅✅✅ | ✅ |
| 402 | `docwriter_v49_probe.py` | `753b0ad48557562e79054635a3d1cb0fb7d0ccfcc597899ef58201d9e08485b9` | 4,806 | `docwriter_v49_probe.py` | `$IAUY2YT.py` | `$RAUY2YT.py` | ✅✅✅✅ | ✅ |
| 403 | `docwriter_v49_probe_out.txt` | `c04bcaf876235000c5e789bfb311116a23566e0f5fbd0542bc25544bdd834a71` | 4,353 | `docwriter_v49_probe_out.txt` | `$IT0OR9E.txt` | `$RT0OR9E.txt` | ✅✅✅✅ | ✅ |
| 404 | `docwriter_verify_v44.py` | `19cfb64700a102dffc97df54973ddb39417c010bb8967b72dcdd59febf060cfa` | 4,692 | `docwriter_verify_v44.py` | `$IBDJ5CA.py` | `$RBDJ5CA.py` | ✅✅✅✅ | ✅ |
| 405 | `docwriter_verify_v44_out.txt` | `f3d33d095a8a49bba8d5adf5bd5032a54370d1779405f8d94a9ca7e388ba6565` | 2,371 | `docwriter_verify_v44_out.txt` | `$I95ATAJ.txt` | `$R95ATAJ.txt` | ✅✅✅✅ | ✅ |
| 406 | `docwriter_verify_v45.py` | `92230e228d8303ee23953ffcc8b9d89a54ec0e66f78805c6552c341dee4b33ab` | 3,780 | `docwriter_verify_v45.py` | `$I60QJLF.py` | `$R60QJLF.py` | ✅✅✅✅ | ✅ |
| 407 | `docwriter_write_effect_v43.py` | `01098529c399cf6fa13017548006d43ab0cc86e725be8a01e281d19c660a6114` | 27,715 | `docwriter_write_effect_v43.py` | `$I4VN6VG.py` | `$R4VN6VG.py` | ✅✅✅✅ | ✅ |
| 408 | `docwriter_write_v42.py` | `5cc438f6338df828afa46178a355a7ecdb4f8b6d82444d2290ee2c245f76b3bd` | 66,543 | `docwriter_write_v42.py` | `$I7TL6VF.py` | `$R7TL6VF.py` | ✅✅✅✅ | ✅ |
| 409 | `docwriter_write_v43.py` | `d5e6390b900dbd2d9f7b838834282c7be8884b726aabc127aeb99784d6708e26` | 33,607 | `docwriter_write_v43.py` | `$ILVR8IM.py` | `$RLVR8IM.py` | ✅✅✅✅ | ✅ |
| 410 | `docwriter_write_v44.py` | `54812b76573b5bc0ec698361174268f1b8c5236c4fab303b929a1fe533eb8d5d` | 84,551 | `docwriter_write_v44.py` | `$I48A4ZL.py` | `$R48A4ZL.py` | ✅✅✅✅ | ✅ |
| 411 | `docwriter_write_v45.py` | `af3a22741b2f33fe84fd29665e4b56709b7921bdc0f1b0977fc155be0f0a8a1e` | 61,168 | `docwriter_write_v45.py` | `$I9GQWVB.py` | `$R9GQWVB.py` | ✅✅✅✅ | ✅ |
| 412 | `dscan_01.json` | `bab5d4a367af507cd6c284b8ac5e59e33bfe38a9b085202ea8a1774c6c07f7c6` | 195,396 | `dscan_01.json` | `$IYH2Z2E.json` | `$RYH2Z2E.json` | ✅✅✅✅ | ✅ |
| 413 | `dscan_01.py` | `a58735d65c3cab1fe12b260b3ce3399d0930621d488873b0582c479629f0c813` | 2,865 | `dscan_01.py` | `$IT6VDB9.py` | `$RT6VDB9.py` | ✅✅✅✅ | ✅ |
| 414 | `dscan_02.py` | `1f6ffd7e0f47140ffc764cc3c6b22605c990eae69e5536799d1e7e30291bb524` | 5,078 | `dscan_02.py` | `$I040H6K.py` | `$R040H6K.py` | ✅✅✅✅ | ✅ |
| 415 | `dscan_03.py` | `35711329ad8fe89ab5b5be106f738b8d27b975ecf4a042995a9a094a4179a9b6` | 5,360 | `dscan_03.py` | `$ITIWZL7.py` | `$RTIWZL7.py` | ✅✅✅✅ | ✅ |
| 416 | `dscan_04.py` | `43e661f72888cda0a22c65bfe5afb62ede7b8ce8a2093636fcfeb66be42a45f2` | 2,302 | `dscan_04.py` | `$IDS53ST.py` | `$RDS53ST.py` | ✅✅✅✅ | ✅ |
| 417 | `dscan_05.py` | `966d9ce0df2d0d713a9ae56b781ccc96994011845bec8828a436589668d1f74c` | 6,207 | `dscan_05.py` | `$IQNSXCQ.py` | `$RQNSXCQ.py` | ✅✅✅✅ | ✅ |
| 418 | `dscan_06.py` | `7c059d99677825d74db3c4eead86bd650b06501ffd1bf4365cc05181a697aa20` | 1,845 | `dscan_06.py` | `$I2LJ6ZX.py` | `$R2LJ6ZX.py` | ✅✅✅✅ | ✅ |
| 419 | `dscan_07.py` | `26897ce010796d72cefb258daa7ff1f425a8ddeba36bf3b6dc8e3d2321668b60` | 1,074 | `dscan_07.py` | `$IX1KXRQ.py` | `$RX1KXRQ.py` | ✅✅✅✅ | ✅ |
| 420 | `dscan_08.py` | `fc3c78d3f0e5f4f8201713f827978ddf434d59a46fc1942bc67af32e1c309f39` | 2,370 | `dscan_08.py` | `$IAY4Z4U.py` | `$RAY4Z4U.py` | ✅✅✅✅ | ✅ |
| 421 | `dscan_classified.json` | `458a2e06a2d383136bae2073cd8977aaf0e719f01d26007e88a5f03c3126afce` | 47,129 | `dscan_classified.json` | `$ICNURPU.json` | `$RCNURPU.json` | ✅✅✅✅ | ✅ |
| 422 | `dscan_classified.txt` | `2945d458f5a694d17ea25962276a0ee4e0592396d15b8026eaa3b2809d15d939` | 11,199 | `dscan_classified.txt` | `$IIR00SS.txt` | `$RIR00SS.txt` | ✅✅✅✅ | ✅ |
| 423 | `dscan_copycmp.txt` | `3af905a1f5c45ad1d636da8708af403527dd7ba6790d18f5b435ed1d1f006e88` | 687 | `dscan_copycmp.txt` | `$I6I1ZBG.txt` | `$R6I1ZBG.txt` | ✅✅✅✅ | ✅ |
| 424 | `dscan_families.txt` | `3bc5960fa2bf59c43e55129f15412357edd916162245a5b06803712944403837` | 3,535 | `dscan_families.txt` | `$IFKW961.txt` | `$RFKW961.txt` | ✅✅✅✅ | ✅ |
| 425 | `dscan_matrix.json` | `875f08dd06489a2dc43874946b556dc090bc0c9b6ab4c828b910f40e727cfed4` | 273,930 | `dscan_matrix.json` | `$IKDUZJM.json` | `$RKDUZJM.json` | ✅✅✅✅ | ✅ |
| 426 | `dscan_matrix.txt` | `a8d3aa0287b60eb241ed40632ea3640725607d2a5f7842c874a43750e27391c0` | 1,452 | `dscan_matrix.txt` | `$IVQJ75S.txt` | `$RVQJ75S.txt` | ✅✅✅✅ | ✅ |
| 427 | `dscan_repo_dump.txt` | `06d5da0d55ed49edaeb60ef3c85677247bbb890722956433a4831d9e36173b07` | 24,326 | `dscan_repo_dump.txt` | `$IDSNRLM.txt` | `$RDSNRLM.txt` | ✅✅✅✅ | ✅ |
| 428 | `dscan_stats.txt` | `b35fb0ebd75da48e77ffa7812f023ccdd130c980cc0488fa386cba1a16f1aa21` | 2,712 | `dscan_stats.txt` | `$I9P938X.txt` | `$R9P938X.txt` | ✅✅✅✅ | ✅ |
| 429 | `dscan_sub_dump.txt` | `8c3f99c0b128fd2184e2dc74830972196581b7469ccef50039488a43cb284845` | 94,170 | `dscan_sub_dump.txt` | `$IBSF452.txt` | `$RBSF452.txt` | ✅✅✅✅ | ✅ |
| 430 | `dscan_tables.md` | `0a96d4720449b5a3bd94a418cc105a90d7c8e7a5588203d835a5e87ad6bcb46b` | 56,191 | `dscan_tables.md` | `$I7FWE94.md` | `$R7FWE94.md` | ✅✅✅✅ | ✅ |
| 431 | `dscan_write_01.py` | `71cbf839d36b26f6f4e1fcfdaae642bbeb9e75fa7f247d6ed13853b925637098` | 23,330 | `dscan_write_01.py` | `$ILFCHBZ.py` | `$RLFCHBZ.py` | ✅✅✅✅ | ✅ |
| 432 | `dscan_xcheck.txt` | `57dcd8344683939b6e10ece16cf2cbb8980216e27a76c415d8a18e2da714ac4f` | 3,196 | `dscan_xcheck.txt` | `$IT3M6X1.txt` | `$RT3M6X1.txt` | ✅✅✅✅ | ✅ |
| 433 | `dw720_calc_2026_10_16.py` | `5da6bf2d700a2b3164f5588c91a05840ef7d55eec3858830b42ac00cf051ed24` | 1,797 | `dw720_calc_2026_10_16.py` | `$IPTWUXK.py` | `$RPTWUXK.py` | ✅✅✅✅ | ✅ |
| 434 | `dw720_probe_2026_10_16.py` | `efdb4c877f3f4848a650ea51c04791c0b8a76d0dd0ba655ec94af8d782c10195` | 1,450 | `dw720_probe_2026_10_16.py` | `$IVZKBPD.py` | `$RVZKBPD.py` | ✅✅✅✅ | ✅ |
| 435 | `dw720_verify_2026_10_16.py` | `c90f9a64c3d8601a52c7c42fa96325145237da62636346288405b950adaeb2dc` | 3,909 | `dw720_verify_2026_10_16.py` | `$ISV9AD3.py` | `$RSV9AD3.py` | ✅✅✅✅ | ✅ |
| 436 | `dw720_write_2026_10_16.py` | `46e8be383b3cba206a3ed7dac9261d5f0e7da77b3a2ca1a663ec4172a41cb391` | 29,681 | `dw720_write_2026_10_16.py` | `$IFE39MC.py` | `$RFE39MC.py` | ✅✅✅✅ | ✅ |
| 437 | `ea_build.py` | `8048ac40151e06cbeee2dfb56237bd185f7b29bac4c1ece8e8631162d74eddf4` | 30,376 | `ea_build.py` | `$I98D8OY.py` | `$R98D8OY.py` | ✅✅✅✅ | ✅ |
| 438 | `ea_files.json` | `48b76f2549f39083ae506ac72f62a15bd29250a692b2dc53c75253f9f0ee9a0a` | 191,599 | `ea_files.json` | `$IWAY5OL.json` | `$RWAY5OL.json` | ✅✅✅✅ | ✅ |
| 439 | `ea_p2.py` | `64fb6201dca94cf068cdbc49be667e3eef33f42457b4d4115da3d3a16bd33ade` | 1,030 | `ea_p2.py` | `$IYYEX1A.py` | `$RYYEX1A.py` | ✅✅✅✅ | ✅ |
| 440 | `ea_scan1.py` | `e21c9fca13d0bd573ff42bdafc46ba64326116a0dfdbde6ffd2029d4e38cf529` | 1,005 | `ea_scan1.py` | `$I44CE2Z.py` | `$R44CE2Z.py` | ✅✅✅✅ | ✅ |
| 441 | `ea_sha12.json` | `381dd57aaca4021151a91732b87c08155c8f1075d13b2465e64d1acf9465b2c0` | 289,347 | `ea_sha12.json` | `$I04BLJ0.json` | `$R04BLJ0.json` | ✅✅✅✅ | ✅ |
| 442 | `evauditor_one_finish_write.py` | `c24967f8114e94c74920289d3a917708979a53e63e14cdbd1cec596a0fbc933f` | 46,211 | `evauditor_one_finish_write.py` | `$IFYB5DN.py` | `$RFYB5DN.py` | ✅✅✅✅ | ✅ |
| 443 | `exp04_h_contrast_2026_10_10.py` | `572f1b9c3927d8606bbf1d307c77abc39e99cc5bcad544d39e3d6e9f20c2aa4a` | 14,333 | `exp04_h_contrast_2026_10_10.py` | `$I0OW6HK.py` | `$R0OW6HK.py` | ✅✅✅✅ | ✅ |
| 444 | `f2_branch_fix_transform_2026_09_29.py` | `0a970b156867db90db26f5ea0cadc47e961df9243d8aeaf7afd18387658500f6` | 18,152 | `f2_branch_fix_transform_2026_09_29.py` | `$ID1ZEMW.py` | `$RD1ZEMW.py` | ✅✅✅✅ | ✅ |
| 445 | `f2_branch_selftest_2026_09_29.py` | `68a927174a2e792ee7d4567d11a7613d9fecef18f7ec606fc3183370ab82f7f4` | 7,377 | `f2_branch_selftest_2026_09_29.py` | `$I91GJ2S.py` | `$R91GJ2S.py` | ✅✅✅✅ | ✅ |
| 446 | `gate_check.py` | `abe7fbdb394befdc5299b76636b5d1177175101eee03d98fa55ba7121ea7fadd` | 648 | `gate_check.py` | `$IKD042A.py` | `$RKD042A.py` | ✅✅✅✅ | ✅ |
| 447 | `gate_check2.py` | `7025ceceb766bc544484c9ef96f916dbaa3fad1e3969beecabddfa599d2e9425` | 840 | `gate_check2.py` | `$IKL4PJ0.py` | `$RKL4PJ0.py` | ✅✅✅✅ | ✅ |
| 448 | `ge01_eps_grid_exec2_2026_10_16.json` | `af1fcc0e8852355f239f00c8e82f4d068429ffd74654318fe328d16fb486faa1` | 53,903 | `ge01_eps_grid_exec2_2026_10_16.json` | `$I5C9LKF.json` | `$R5C9LKF.json` | ✅✅✅✅ | ✅ |
| 449 | `ge01_eps_grid_exec2_2026_10_16.py` | `9ef16d1b8525cc39651f4bbdc6ff2165929b341fc5fafeecd2602d3d9eb0ae66` | 11,452 | `ge01_eps_grid_exec2_2026_10_16.py` | `$IT8OWH9.py` | `$RT8OWH9.py` | ✅✅✅✅ | ✅ |
| 450 | `ge01_eps_grid_exec3_2026_10_16.py` | `5225d7800544e5ef7cfd0ba24be722c6b3fc0fb57a11982a63b3871c347f651e` | 3,580 | `ge01_eps_grid_exec3_2026_10_16.py` | `$ISOKZMU.py` | `$RSOKZMU.py` | ✅✅✅✅ | ✅ |
| 451 | `ge01_eps_grid_exec_2026_10_16.json` | `45b233594ee94481eac71c4bb19d2c4da2a66ee94f6dfba18c82c7b989f57a94` | 62,749 | `ge01_eps_grid_exec_2026_10_16.json` | `$I4RYQ04.json` | `$R4RYQ04.json` | ✅✅✅✅ | ✅ |
| 452 | `ge01_eps_grid_exec_2026_10_16.py` | `ab5e001cb63b1a9e241166d9f1dff79c1b9796aa1648dbf0973b9c85deec401b` | 11,018 | `ge01_eps_grid_exec_2026_10_16.py` | `$IXJH4I3.py` | `$RXJH4I3.py` | ✅✅✅✅ | ✅ |
| 453 | `ge01_eps_grid_verify_2026_10_16.py` | `4ff9d5a95dcfd7aaea26624a2a4641061158050c900b20008f26054674a615d7` | 3,016 | `ge01_eps_grid_verify_2026_10_16.py` | `$IGT5H63.py` | `$RGT5H63.py` | ✅✅✅✅ | ✅ |
| 454 | `ge01_full_1494_adjudicate_2026_10_16.py` | `8108e4c883ad4e71fe4da6de2851fe628c5f9a9eb16ba0633a68b09f3d017a2b` | 14,293 | `ge01_full_1494_adjudicate_2026_10_16.py` | `$I31QASC.py` | `$R31QASC.py` | ✅✅✅✅ | ✅ |
| 455 | `ge01_full_1494_collect_2026_10_16.py` | `039ebfca39b7af5a6e45cf112c56f0ba664b4faef34a947a9e37fc9a2130725d` | 28,322 | `ge01_full_1494_collect_2026_10_16.py` | `$IDWLJTS.py` | `$RDWLJTS.py` | ✅✅✅✅ | ✅ |
| 456 | `ge01_full_1494_exec_r1_write_2026_10_16.py` | `9e9e402893ef79facec58587db97fe86a9e3ff6578d5df861fe2cbd211e21f75` | 43,129 | `ge01_full_1494_exec_r1_write_2026_10_16.py` | `$IFZY436.py` | `$RFZY436.py` | ✅✅✅✅ | ✅ |
| 457 | `ge01_full_1494_freeze_2026_10_16.json` | `8494390a274ab64be0c9f8e3d546ce3c3e7a3c7fd9bcb82ba8dc0e23a29a503e` | 7,479 | `ge01_full_1494_freeze_2026_10_16.json` | `$I1XUSC1.json` | `$R1XUSC1.json` | ✅✅✅✅ | ✅ |
| 458 | `ge01_full_1494_freeze_write_2026_10_16.py` | `b89e0432ab9705ede37579b163c658794259ad8cb2f23342a9e3279787af83aa` | 23,781 | `ge01_full_1494_freeze_write_2026_10_16.py` | `$IJTD1LO.py` | `$RJTD1LO.py` | ✅✅✅✅ | ✅ |
| 459 | `ge01_full_1494_llm_calls_2026_10_16.jsonl` | `e922d168ab60cc99eaab35139600ec74288f9ebb3e3d519dc26847459ac22e25` | 235,298 | `ge01_full_1494_llm_calls_2026_10_16.jsonl` | `$IJBKXPK.jsonl` | `$RJBKXPK.jsonl` | ✅✅✅✅ | ✅ |
| 460 | `ge01_full_1494_measurement_2026_10_16.json` | `4054d1393b84c8b73a9647e7c18d66969f76553dbcf14a869f5538b473de9364` | 547,703 | `ge01_full_1494_measurement_2026_10_16.json` | `$IAIPC0D.json` | `$RAIPC0D.json` | ✅✅✅✅ | ✅ |
| 461 | `ge01_full_1494_measurement_resume32_2026_10_16.json` | `7ccc5f9e8b2ce2d27c04c154612d2f20afdde6af2b62321ca37a2744050da826` | 570,852 | `ge01_full_1494_measurement_resume32_2026_10_16.json` | `$IXKZRVI.json` | `$RXKZRVI.json` | ✅✅✅✅ | ✅ |
| 462 | `ge01_full_1494_precheck_2026_10_16.json` | `bd6dd07ad1c374d9a7089327a357d8c18d7f87c2762dcca4f8fb41795c64b176` | 9,432 | `ge01_full_1494_precheck_2026_10_16.json` | `$IX8GHHQ.json` | `$RX8GHHQ.json` | ✅✅✅✅ | ✅ |
| 463 | `ge01_full_1494_precheck_2026_10_16.py` | `cc34ab8552f9c83fab0c5a62bf2256640746e46a9b41fe4aa2e310d46b08575d` | 10,700 | `ge01_full_1494_precheck_2026_10_16.py` | `$IJUJGZ3.py` | `$RJUJGZ3.py` | ✅✅✅✅ | ✅ |
| 464 | `ge01_full_1494_probe_2026_10_16.py` | `a38499e4d4a9535de80012837a0e4789fcb44852a9c87fbb8bf44a92fbbd98a4` | 3,199 | `ge01_full_1494_probe_2026_10_16.py` | `$INJ0S8Z.py` | `$RNJ0S8Z.py` | ✅✅✅✅ | ✅ |
| 465 | `ge01_full_1494_readout_2026_10_16.py` | `59ed27635c6e387a97e93356f181246035c43737cbb9cb289855768861ac8adf` | 22,920 | `ge01_full_1494_readout_2026_10_16.py` | `$I38TWRA.py` | `$R38TWRA.py` | ✅✅✅✅ | ✅ |
| 466 | `ge01_full_1494_resume32_collect_2026_10_16.py` | `9496620e32b266fcdecf5d86a91c5b98e0386a8a649d3dd7f6cfdf8a610244cd` | 14,609 | `ge01_full_1494_resume32_collect_2026_10_16.py` | `$IG860PC.py` | `$RG860PC.py` | ✅✅✅✅ | ✅ |
| 467 | `ge01_full_1494_resume32_precheck_2026_10_16.log` | `ada7f41b8cb25b8e6951888cfd976bd266444338c75fc59e3d4593cf517363d1` | 1,761 | `ge01_full_1494_resume32_precheck_2026_10_16.log` | `$I4CKW8M.log` | `$R4CKW8M.log` | ✅✅✅✅ | ✅ |
| 468 | `ge01_full_1494_resume32_precheck_2026_10_16.py` | `463532446b61f575455974216d1f41e0598bb019bd073b743a7735208ee36d71` | 6,122 | `ge01_full_1494_resume32_precheck_2026_10_16.py` | `$IU7VAMM.py` | `$RU7VAMM.py` | ✅✅✅✅ | ✅ |
| 469 | `ge01_full_1494_resume32_probe_2026_10_16.json` | `579a7f8b6fe30af180dc831c02856a091d8c9004dd0875b3d229f87d68c57c3e` | 338 | `ge01_full_1494_resume32_probe_2026_10_16.json` | `$I15WYH5.json` | `$R15WYH5.json` | ✅✅✅✅ | ✅ |
| 470 | `ge01_full_1494_resume32_readout_2026_10_16.py` | `de50589bd6c6eb18b2677ddc75c513ce4fcf927fc0933f4f1ff0112ced5503f7` | 29,430 | `ge01_full_1494_resume32_readout_2026_10_16.py` | `$IF7KS0I.py` | `$RF7KS0I.py` | ✅✅✅✅ | ✅ |
| 471 | `ge01_full_1494_resume32_run_2026_10_16.log` | `f655e7d9e3e099b9b2fbd5c47748a9936456545a547985cf1dddde9f1e5a3512` | 1,033 | `ge01_full_1494_resume32_run_2026_10_16.log` | `$I65IQ87.log` | `$R65IQ87.log` | ✅✅✅✅ | ✅ |
| 472 | `ge01_full_1494_resume32_stage_2026_10_16.json` | `25d95a22bbb1493601afc6a2ceec011ce192a0304fe1be59a26d399fc538f0e5` | 7,574 | `ge01_full_1494_resume32_stage_2026_10_16.json` | `$IK80YNZ.json` | `$RK80YNZ.json` | ✅✅✅✅ | ✅ |
| 473 | `ge01_full_1494_run_2026_10_16.log` | `3e85eac1bf6afb38f50c62700eea5af7264568415dc24fc8878b37895d01bf56` | 14,810 | `ge01_full_1494_run_2026_10_16.log` | `$I8XN3XB.log` | `$R8XN3XB.log` | ✅✅✅✅ | ✅ |
| 474 | `ge01_gate_index.py` | `fc4ed5e7dea065d2fdcc26961fa5aba1d4662231fb38e88db8030a86feab1d56` | 3,095 | `ge01_gate_index.py` | `$I5U58IE.py` | `$R5U58IE.py` | ✅✅✅✅ | ✅ |
| 475 | `ge01_gate_measure.py` | `c2cdebcb0bfc990a5720d21fe2f194034d5d8347d7d4a71b58ecc8f3fd6aa647` | 4,068 | `ge01_gate_measure.py` | `$IPWJ0VG.py` | `$RPWJ0VG.py` | ✅✅✅✅ | ✅ |
| 476 | `ge01_gate_probe.py` | `82bf49985799b61bf75cab6052733710d96caa980349885c05f370998b2ded96` | 3,196 | `ge01_gate_probe.py` | `$IL3YU7O.py` | `$RL3YU7O.py` | ✅✅✅✅ | ✅ |
| 477 | `ge01_gate_scan.py` | `5f6212d13cb5b975aa4930ee516809af0fc4175729bfd1be12105be1b75d6383` | 1,955 | `ge01_gate_scan.py` | `$IUCY512.py` | `$RUCY512.py` | ✅✅✅✅ | ✅ |
| 478 | `ge01_gate_write.py` | `a661b2c7e5f00356733e502f795793188626b2635eec706b4292b6322004a5b3` | 82,875 | `ge01_gate_write.py` | `$IOA9CRB.py` | `$ROA9CRB.py` | ✅✅✅✅ | ✅ |
| 479 | `ge01_measure_list.json` | `2eb41639edf420646ccf0843da2ea7bf7e37f3295ea46397d9f50b21de38b83f` | 2,435 | `ge01_measure_list.json` | `$I90US3O.json` | `$R90US3O.json` | ✅✅✅✅ | ✅ |
| 480 | `ge01_results_sha12.json` | `97fb1089de90aeccb0d5a908ea5682961af59136097d3a6327299974183d5ff3` | 192,203 | `ge01_results_sha12.json` | `$I8G4IBJ.json` | `$R8G4IBJ.json` | ✅✅✅✅ | ✅ |
| 481 | `ge01_s3_keyscan_2026_10_16.py` | `5f8a18033a9932db9829a9924e8adcfaf322a991bb49e9f69820ffbba063262b` | 1,730 | `ge01_s3_keyscan_2026_10_16.py` | `$I2YMEY6.py` | `$R2YMEY6.py` | ✅✅✅✅ | ✅ |
| 482 | `ge01_s3_vadj_recheck_2026_10_16.py` | `91d3e1d91b58ba2d5c466a47c90b4ff9138708ce854f95d8ba9ebb30d1c6442a` | 13,088 | `ge01_s3_vadj_recheck_2026_10_16.py` | `$IOKJUYE.py` | `$ROKJUYE.py` | ✅✅✅✅ | ✅ |
| 483 | `ge01_s3b_keyscan_2026_10_16.py` | `b7743ec5a7ab45260c8fcff89eb56f67f9e3e0ec947800f59db61721583f7843` | 2,052 | `ge01_s3b_keyscan_2026_10_16.py` | `$IUTXMRK.py` | `$RUTXMRK.py` | ✅✅✅✅ | ✅ |
| 484 | `ge01_s3b_v_exec_2026_10_16.py` | `0df5d957a91153f2e513d3a999f85e9c40d2678e24909191b12ee815ce964798` | 6,410 | `ge01_s3b_v_exec_2026_10_16.py` | `$IG0Z4VR.py` | `$RG0Z4VR.py` | ✅✅✅✅ | ✅ |
| 485 | `ge01_s3b_v_exec_r1_2026_10_16.py` | `4f525232efe4688159bab22add370935d4afe158849f2491698c463f6a1af21a` | 15,257 | `ge01_s3b_v_exec_r1_2026_10_16.py` | `$IG9PRHU.py` | `$RG9PRHU.py` | ✅✅✅✅ | ✅ |
| 486 | `ge01_s3b_v_exec_r1_readings_2026_10_16.json` | `1ec7c258c637d45a7c3240c040ea70813eaecbb62a7266e5f42c120881ce1f7c` | 25,489 | `ge01_s3b_v_exec_r1_readings_2026_10_16.json` | `$IJ0SJYK.json` | `$RJ0SJYK.json` | ✅✅✅✅ | ✅ |
| 487 | `ge01_s3b_v_exec_r1_supp_2026_10_16.py` | `0646da5ccbe5a11522e1199fc27b23e188555649a66517f25e279cb20d599809` | 5,199 | `ge01_s3b_v_exec_r1_supp_2026_10_16.py` | `$IUZ42EC.py` | `$RUZ42EC.py` | ✅✅✅✅ | ✅ |
| 488 | `ge01_s3b_v_exec_r1_write_2026_10_16.py` | `359b768e7dc0d587c4a4d6501a9487e41fe020100ce4db79e6fe3ae15bc7e3e9` | 56,062 | `ge01_s3b_v_exec_r1_write_2026_10_16.py` | `$IP110Z6.py` | `$RP110Z6.py` | ✅✅✅✅ | ✅ |
| 489 | `ge02_build.py` | `a10c57adf6b5f1501d087bcbedb98cfbc7330208a711b7048ffaa6478a91a4b1` | 24,774 | `ge02_build.py` | `$INMWK3X.py` | `$RNMWK3X.py` | ✅✅✅✅ | ✅ |
| 490 | `ge02_recompute.py` | `811d4a138788dd526b306ef8ee9871e6f28620b68748cd07cb5e913d0eca710a` | 1,347 | `ge02_recompute.py` | `$IKS1SO4.py` | `$RKS1SO4.py` | ✅✅✅✅ | ✅ |
| 491 | `gen_supp3.py` | `eb53c9ce140c2cc6d25d633220130a120dd2b4f1c611195a173dee1b344aa5ff` | 15,813 | `gen_supp3.py` | `$IEUP8BR.py` | `$REUP8BR.py` | ✅✅✅✅ | ✅ |
| 492 | `gen_v35_uactive_2026_10_16.py` | `628c99636f10e222b9991862cdb069aca67045e5a8002344a0994865a37a0458` | 43,518 | `gen_v35_uactive_2026_10_16.py` | `$IBMTWVV.py` | `$RBMTWVV.py` | ✅✅✅✅ | ✅ |
| 493 | `h_src.py` | `a4b8970b8b1f9d62f37dbf39ef57dafea32c0beaaad4cf7d046d81cca5f35352` | 727 | `h_src.py` | `$IWK56J1.py` | `$RWK56J1.py` | ✅✅✅✅ | ✅ |
| 494 | `harness.py` | `56e02c4878f4bb0f1b0bea0c0320d4f923f5d92a553e0628be1528e3bc131058` | 687 | `harness.py` | `$IJ4TTJ8.py` | `$RJ4TTJ8.py` | ✅✅✅✅ | ✅ |
| 495 | `k_v3df_0_1_four_readings_2026_10_09.py` | `2e990644cc8d14a404a2031df7e03befea0ee20ca34f221b821c23941a3ef243` | 50,232 | `k_v3df_0_1_four_readings_2026_10_09.py` | `$IXM4B6X.py` | `$RXM4B6X.py` | ✅✅✅✅ | ✅ |
| 496 | `kd14_absorption_probe.py` | `915c968f2d04619e85c7ebb79c0eed9d6ab0eb4ecbe869e3eb329c499fc7022d` | 1,358 | `kd14_absorption_probe.py` | `$IVN9RER.py` | `$RVN9RER.py` | ✅✅✅✅ | ✅ |
| 497 | `kd14_carrier_probe.py` | `758033c2a76b21f5876dd8d6df26bef7c60ad9dde6b4671081a4dc01af3f102e` | 1,206 | `kd14_carrier_probe.py` | `$ITIBDBX.py` | `$RTIBDBX.py` | ✅✅✅✅ | ✅ |
| 498 | `kd14_m4_corrected.py` | `50c1c7d85616aebf6257b3642de526780d03014e70822144c2f710c9f0538367` | 932 | `kd14_m4_corrected.py` | `$ILIVA48.py` | `$RLIVA48.py` | ✅✅✅✅ | ✅ |
| 499 | `klm41_2_bootstrap_ci_2026_10_16.json` | `be99abcba9bf938af0343d905fdfa69655164e72a8d611875361c3a6877145e4` | 12,373 | `klm41_2_bootstrap_ci_2026_10_16.json` | `$I9N8TDL.json` | `$R9N8TDL.json` | ✅✅✅✅ | ✅ |
| 500 | `klm41_2_caliber_decl_2026_10_16.json` | `6f0721d20c066432d0cafbf497cdca01dfc2a5f233dfc25d2581a1cdf246b502` | 4,757 | `klm41_2_caliber_decl_2026_10_16.json` | `$IJG6X0S.json` | `$RJG6X0S.json` | ✅✅✅✅ | ✅ |
| 501 | `klm41_2_caliber_decl_2026_10_16.py` | `d9754474ad9aded05aa16727a0553cacaa537e34979f1f5a631caa0010f1ed0e` | 10,466 | `klm41_2_caliber_decl_2026_10_16.py` | `$I1K2ZIF.py` | `$R1K2ZIF.py` | ✅✅✅✅ | ✅ |
| 502 | `klm41_2_compute_ci_2026_10_16.py` | `fb38b90df08fd5643a8aab0bb0273990b5515376f2f964f078579c7a4478e372` | 14,398 | `klm41_2_compute_ci_2026_10_16.py` | `$I77I22P.py` | `$R77I22P.py` | ✅✅✅✅ | ✅ |
| 503 | `klm41_2_freeze_2026_10_16.json` | `2a4453d9610bab51361cd950173c12f91279c70c3623ba51e0a17cf4440b360f` | 3,211 | `klm41_2_freeze_2026_10_16.json` | `$ILEOSLB.json` | `$RLEOSLB.json` | ✅✅✅✅ | ✅ |
| 504 | `klm41_2_stratified_ci_2026_10_16.json` | `67ae4f540e477957586ba1186736ea2a368e86c234207b4581b59f162e7806fe` | 18,820 | `klm41_2_stratified_ci_2026_10_16.json` | `$I8FSHGA.json` | `$R8FSHGA.json` | ✅✅✅✅ | ✅ |
| 505 | `klm41_2_stratified_ci_2026_10_16.py` | `f29526bccea3a08514869b49902bac0bed238fc9abd4c526b92fcc1e1bda8858` | 8,819 | `klm41_2_stratified_ci_2026_10_16.py` | `$IYCHPLR.py` | `$RYCHPLR.py` | ✅✅✅✅ | ✅ |
| 506 | `klm41_2_verify_2026_10_16.json` | `5ded5068566b6e62e75c88f93ed06208cff183f9265b92e17d41ad0d6a72b6eb` | 2,906 | `klm41_2_verify_2026_10_16.json` | `$IBXNIVC.json` | `$RBXNIVC.json` | ✅✅✅✅ | ✅ |
| 507 | `klm41_2_verify_2026_10_16.py` | `af0f38f33222a9813423add52b97c09e6cd7e543f75e3f9b6d043e429b293d34` | 10,976 | `klm41_2_verify_2026_10_16.py` | `$IE8OR4X.py` | `$RE8OR4X.py` | ✅✅✅✅ | ✅ |
| 508 | `klm41_2_write_doc_2026_10_16.py` | `902dcf78f2b81aecd5a7c04574368047db67648dee955b16c14b13a34889a52c` | 48,391 | `klm41_2_write_doc_2026_10_16.py` | `$IP4HXQM.py` | `$RP4HXQM.py` | ✅✅✅✅ | ✅ |
| 509 | `klm41_3_ts_caliber_decl_2026_10_16.json` | `96456529a4855435c29a16482cae3f932b789ed838b85abe012adff2aa03bc29` | 3,255 | `klm41_3_ts_caliber_decl_2026_10_16.json` | `$I6APGL4.json` | `$R6APGL4.json` | ✅✅✅✅ | ✅ |
| 510 | `klm41_3_ts_collect_2026_10_16.py` | `a28c4ba40940480407d8b3fc0ae168c4ccdc8d609ecf5c9edc44f1df4a121e79` | 23,196 | `klm41_3_ts_collect_2026_10_16.py` | `$IYD4QEA.py` | `$RYD4QEA.py` | ✅✅✅✅ | ✅ |
| 511 | `klm41_3_ts_freeze_2026_10_16.json` | `25c021d29b1bf184c71594b7e6d21cc02fd8c8c527529d6251e6cd03010c1a2c` | 2,235 | `klm41_3_ts_freeze_2026_10_16.json` | `$IQJKL9P.json` | `$RQJKL9P.json` | ✅✅✅✅ | ✅ |
| 512 | `klm41_3_ts_llm_calls_2026_10_16.jsonl` | `595699b7ec442721da7a0b8eac78ea7cf9acf1aa9b008c537469238a4740428b` | 123,255 | `klm41_3_ts_llm_calls_2026_10_16.jsonl` | `$IW897UX.jsonl` | `$RW897UX.jsonl` | ✅✅✅✅ | ✅ |
| 513 | `klm41_3_ts_measurement_2026_10_16.json` | `211a49ca9941802c528724a0f009a81cab1bcd0d612ea961f4b684ac1f45bc09` | 252,951 | `klm41_3_ts_measurement_2026_10_16.json` | `$IDN1SKZ.json` | `$RDN1SKZ.json` | ✅✅✅✅ | ✅ |
| 514 | `klm41_3_ts_preflight_2026_10_16.json` | `d1fe0a6889be81dc91ad6bb7f1a46839cae6debbdd9bdbb8049efa37c6f350ed` | 6,349 | `klm41_3_ts_preflight_2026_10_16.json` | `$IW3M3T0.json` | `$RW3M3T0.json` | ✅✅✅✅ | ✅ |
| 515 | `klm41_3_ts_preflight_2026_10_16.py` | `c787c6d4e3615bfe2b53ec2b32c419daed80a98c6bcc1bfa86df07c4ecade378` | 6,228 | `klm41_3_ts_preflight_2026_10_16.py` | `$IKEMO0M.py` | `$RKEMO0M.py` | ✅✅✅✅ | ✅ |
| 516 | `klm41_3_ts_tables_2026_10_16.md` | `54213bffc2165403e62344ec725c772d509483f5e016f13c641126654dc3a79a` | 11,297 | `klm41_3_ts_tables_2026_10_16.md` | `$I0GALU6.md` | `$R0GALU6.md` | ✅✅✅✅ | ✅ |
| 517 | `klm41_3_ts_verify_2026_10_16.json` | `8cf7bb595870caf04268e24207e221ccd178def51ed8e580c5f1d8ebce624a07` | 5,848 | `klm41_3_ts_verify_2026_10_16.json` | `$INK9RLL.json` | `$RNK9RLL.json` | ✅✅✅✅ | ✅ |
| 518 | `kro_extract.py` | `b5731abae41fb577a8fce7039353d61505bfbb80a431f0f22a90c5b676176adc` | 802 | `kro_extract.py` | `$I6Q9HO8.py` | `$R6Q9HO8.py` | ✅✅✅✅ | ✅ |
| 519 | `m08_enum_v2_2026_10_16.json` | `c45cfc3ddc8dab63fe76aa49d220e1becad58b008f2c0fde1a50c80dcf860482` | 12,255 | `m08_enum_v2_2026_10_16.json` | `$IT0N5PO.json` | `$RT0N5PO.json` | ✅✅✅✅ | ✅ |
| 520 | `m08_r1_amend2_2026_10_16.json` | `21ad2e7acd0b900eddc6a130e5fceea77cd1e4b7853e4e68d4b430f39c3b2c86` | 1,296 | `m08_r1_amend2_2026_10_16.json` | `$INXZ2MD.json` | `$RNXZ2MD.json` | ✅✅✅✅ | ✅ |
| 521 | `m08_r1_amend3_2026_10_16.json` | `d77931c6d7a5a76c3859ca9edd0cbd11214b7e43e03ba9a2759fdf2a05204413` | 3,034 | `m08_r1_amend3_2026_10_16.json` | `$IRJPUZD.json` | `$RRJPUZD.json` | ✅✅✅✅ | ✅ |
| 522 | `m08_r1_amend_2026_10_16.json` | `3c982068b27673622b7f7eb3d9fac0cfb642936b56bdf46ee148e69089c71fdf` | 1,204 | `m08_r1_amend_2026_10_16.json` | `$IQY4QD6.json` | `$RQY4QD6.json` | ✅✅✅✅ | ✅ |
| 523 | `m08_r1_enum_2026_10_16.json` | `361f67e37092e956e8179d25131e62695e4f49f289c0cd5dcc91376d941ed179` | 13,253 | `m08_r1_enum_2026_10_16.json` | `$I8FPD9T.json` | `$R8FPD9T.json` | ✅✅✅✅ | ✅ |
| 524 | `m08_r1_enum_2026_10_16.py` | `884b7161e053b242c20e9d49afe59801a1cd77ef2eeb96cf80ca1d27594184b0` | 16,318 | `m08_r1_enum_2026_10_16.py` | `$IF5LGO4.py` | `$RF5LGO4.py` | ✅✅✅✅ | ✅ |
| 525 | `m08_r1_freeze_2026_10_16.json` | `1a40d8046fdce69cbf5fbb4f97dccfbb8800381fac0852ad6ff54ea0754804a9` | 7,655 | `m08_r1_freeze_2026_10_16.json` | `$IID0LLT.json` | `$RID0LLT.json` | ✅✅✅✅ | ✅ |
| 526 | `m08_r1_freeze_2026_10_16.py` | `8c6b5e0d3ebb8f8a90f0f98595e75c707a19272e634d2bd87113c27f5a2909c2` | 9,207 | `m08_r1_freeze_2026_10_16.py` | `$I1ETNXX.py` | `$R1ETNXX.py` | ✅✅✅✅ | ✅ |
| 527 | `m08_r1_llm_arm_2026_10_16.json` | `19d93d77b46e1ed819e06d24df58fdb28c3f5284b7bb8b9774816da4f7cab584` | 11,335 | `m08_r1_llm_arm_2026_10_16.json` | `$IH81IQF.json` | `$RH81IQF.json` | ✅✅✅✅ | ✅ |
| 528 | `m08_r1_llm_arm_2026_10_16.py` | `987820693d069660ffaf478e448d39a71de92b596fca7c72b1947edc113b764e` | 9,852 | `m08_r1_llm_arm_2026_10_16.py` | `$IYOVGCZ.py` | `$RYOVGCZ.py` | ✅✅✅✅ | ✅ |
| 529 | `m08_r1_llm_calls_2026_10_16.jsonl` | `0e8c9664b06de8038c641f1ff06cd206499b0c901a7b3c4227a1c3052206d57d` | 8,271 | `m08_r1_llm_calls_2026_10_16.jsonl` | `$IAUXGI9.jsonl` | `$RAUXGI9.jsonl` | ✅✅✅✅ | ✅ |
| 530 | `m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | `d30121ed7ebfc01e7e383360bd51eba41fd2cfe75f78b9ce7255ab9aa1926588` | 8,230 | `m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl` | `$IVBTHAW.jsonl` | `$RVBTHAW.jsonl` | ✅✅✅✅ | ✅ |
| 531 | `m08_r1_llm_probe2_2026_10_16.json` | `d2a8510b132235b58cc0f18104e1e7a1f6d6423f445e3d27ea30890d87648da4` | 1,805 | `m08_r1_llm_probe2_2026_10_16.json` | `$IQKSTUK.json` | `$RQKSTUK.json` | ✅✅✅✅ | ✅ |
| 532 | `m08_r1_llm_probe2_2026_10_16.py` | `190668eae9da1e6b65900243e699ae555d3c09de9fc681a935b2538cc056dbb4` | 2,359 | `m08_r1_llm_probe2_2026_10_16.py` | `$IH3BZCX.py` | `$RH3BZCX.py` | ✅✅✅✅ | ✅ |
| 533 | `m08_r1_probe_2026_10_16.json` | `c2ba80ba548b55d14fec18fe9d51ed52d67bd94572a37818f05484b921c0e1f9` | 3,752 | `m08_r1_probe_2026_10_16.json` | `$IYTJVIG.json` | `$RYTJVIG.json` | ✅✅✅✅ | ✅ |
| 534 | `m08_r1_probe_2026_10_16.py` | `63f0234a7c89e8662c770671c5a28032e1e971b187b2ffaaa5558d1d81cfa24e` | 4,739 | `m08_r1_probe_2026_10_16.py` | `$IK9MSQ2.py` | `$RK9MSQ2.py` | ✅✅✅✅ | ✅ |
| 535 | `m08_r1_recompute_2026_10_16.json` | `59ddca239f67d20f8f8fb9bdd8c0203600837536bfb4a65cc039d396ca7f1a08` | 2,072 | `m08_r1_recompute_2026_10_16.json` | `$ITW2S8B.json` | `$RTW2S8B.json` | ✅✅✅✅ | ✅ |
| 536 | `m08_r1_recompute_2026_10_16.py` | `305ee668612c64e3a98067790d3a9be0fad18289128ddbf52ad77e95579989a7` | 6,998 | `m08_r1_recompute_2026_10_16.py` | `$I7JWTW1.py` | `$R7JWTW1.py` | ✅✅✅✅ | ✅ |
| 537 | `m08_r1_srcsha_2026_10_16.json` | `2074096a45e2df1b070abdd55410882560e3b3873f3e1c6476750f2fad61321f` | 8,851 | `m08_r1_srcsha_2026_10_16.json` | `$I4T1N3C.json` | `$R4T1N3C.json` | ✅✅✅✅ | ✅ |
| 538 | `m08_r1_srcsha_2026_10_16.py` | `96ac0e7c23f65c7e64a45abe8aceeb87acc421a32301f447b16c242fba6b433b` | 3,697 | `m08_r1_srcsha_2026_10_16.py` | `$IQWB804.py` | `$RQWB804.py` | ✅✅✅✅ | ✅ |
| 539 | `m08_r1_write_2026_10_16.py` | `0a5d9e9f18d91127567e85b753b8ffb4ce20b82c58c88ee2dc74ed0d7b8a6c87` | 58,218 | `m08_r1_write_2026_10_16.py` | `$I0C61K5.py` | `$R0C61K5.py` | ✅✅✅✅ | ✅ |
| 540 | `m2_docwriter_write.py` | `9842ca168062f5d73b50b1938b9d55e01672dd46721d7d47fc1b21b19865078b` | 23,214 | `m2_docwriter_write.py` | `$I1FBS5V.py` | `$R1FBS5V.py` | ✅✅✅✅ | ✅ |
| 541 | `m2_write.py` | `133387a21ec6ffbedba69c65d7d9e43c433b9314e1b51e8ea21dcf08f0856875` | 24,159 | `m2_write.py` | `$IBEVY5Z.py` | `$RBEVY5Z.py` | ✅✅✅✅ | ✅ |
| 542 | `m2verdict_downstream.py` | `93c831a7fc0fcdadb57ffe1184edd9576c04e3165aca43a44fb11efe0c4c213e` | 2,240 | `m2verdict_downstream.py` | `$I626UQX.py` | `$R626UQX.py` | ✅✅✅✅ | ✅ |
| 543 | `m2verdict_meta.py` | `c895996558072218151fe8b82e4307b646c04ce2ee022686b6baa4ac97674b6c` | 1,223 | `m2verdict_meta.py` | `$IDP9VAS.py` | `$RDP9VAS.py` | ✅✅✅✅ | ✅ |
| 544 | `m2verdict_probe.py` | `3a401ef46a006002856c9ec172ea4aeb1ae139a860c2165847b60328f8a6c059` | 4,493 | `m2verdict_probe.py` | `$I4QCFEZ.py` | `$R4QCFEZ.py` | ✅✅✅✅ | ✅ |
| 545 | `m2verdict_ruling.py` | `841949136e81332086c08dd203123fcce078e1e46d4cd482f766a681ef24d012` | 1,125 | `m2verdict_ruling.py` | `$I9N6OGS.py` | `$R9N6OGS.py` | ✅✅✅✅ | ✅ |
| 546 | `m41_dual_readout.py` | `45f3d856efd8b0c2f6bd52d27b8609b7db9e2a61bf9377a36056fe3266f8efb6` | 6,471 | `m41_dual_readout.py` | `$ITJRS38.py` | `$RTJRS38.py` | ✅✅✅✅ | ✅ |
| 547 | `m41_endpoint_probe.py` | `f9811a6ecebad612c50a443b14025bf423a08726b4d7d8d093df59ec6999da5a` | 1,520 | `m41_endpoint_probe.py` | `$IFN3VU6.py` | `$RFN3VU6.py` | ✅✅✅✅ | ✅ |
| 548 | `m41_fix_diag.json` | `2e34378d0d2c1c4f39048a2b90ad354e2d91b117a01aea23db9ac29397cb54b8` | 1,034 | `m41_fix_diag.json` | `$IU4BC8F.json` | `$RU4BC8F.json` | ✅✅✅✅ | ✅ |
| 549 | `m41_keyprobe.py` | `10e08b837e0518972b2021709e66ad468ad861e903c3f4cdc267d0f7552bca13` | 892 | `m41_keyprobe.py` | `$IVZQ6A1.py` | `$RVZQ6A1.py` | ✅✅✅✅ | ✅ |
| 550 | `m41_keysurvey.py` | `795daa633133e08667371c47383e5e121d03b8038a91d87a0c1f6f9a66f23e05` | 1,296 | `m41_keysurvey.py` | `$INVXFH3.py` | `$RNVXFH3.py` | ✅✅✅✅ | ✅ |
| 551 | `m41_llm_calls.jsonl` | `a1651f3d93030b128d82c832760f26709c8ec728a2bf97d39626d8b6eebd3a77` | 642 | `m41_llm_calls.jsonl` | `$IY3227M.jsonl` | `$RY3227M.jsonl` | ✅✅✅✅ | ✅ |
| 552 | `m41_mech_arms.json` | `be1a8fce8660c6f34ee406762b245c529c236834efe083eddaf310ce095623e8` | 1,252 | `m41_mech_arms.json` | `$IPSL1KQ.json` | `$RPSL1KQ.json` | ✅✅✅✅ | ✅ |
| 553 | `m41_mech_arms.py` | `a92812ceae614b896e9428ec381a270b851f16cd27ed6bfee84d06984e7aaf61` | 3,731 | `m41_mech_arms.py` | `$IQ28YK5.py` | `$RQ28YK5.py` | ✅✅✅✅ | ✅ |
| 554 | `m41_r15_collect_readout.py` | `d4e882337b80c98edd9054302dbd3b980087bf6cbecc625e61dff6bb28fe7de6` | 13,324 | `m41_r15_collect_readout.py` | `$ISMOI8U.py` | `$RSMOI8U.py` | ✅✅✅✅ | ✅ |
| 555 | `m41_r15_llm_calls.jsonl` | `7d0dbb58d53a4b326b1286f9f2c1739a4f6e24727176bb9f7066b4ed09e4f4fa` | 3,467 | `m41_r15_llm_calls.jsonl` | `$IGDMGCG.jsonl` | `$RGDMGCG.jsonl` | ✅✅✅✅ | ✅ |
| 556 | `m41_r15_readout.json` | `33a4720bcafd990a8c22ab723bce2a319e632a2d024bce6b072ef923ef775125` | 14,261 | `m41_r15_readout.json` | `$ISBX6FG.json` | `$RSBX6FG.json` | ✅✅✅✅ | ✅ |
| 557 | `m41_r15_verify.py` | `f72545f959b46461b7b5e1f8cc5dd211c5b5e5329e9b514383db8d95e61ef422` | 4,235 | `m41_r15_verify.py` | `$IO8HKSL.py` | `$RO8HKSL.py` | ✅✅✅✅ | ✅ |
| 558 | `m41_rerun_llm_calls.jsonl` | `19fa12f4e053c1198088ce93f3bc95b88ceab774a000b267d99eddee69241ca8` | 24,253 | `m41_rerun_llm_calls.jsonl` | `$IJUY0UP.jsonl` | `$RJUY0UP.jsonl` | ✅✅✅✅ | ✅ |
| 559 | `m41_selfcheck.json` | `d18a46a884f2519af5cbb54ee9be74feeeb48c51aac45da375f0b5c6b9254f04` | 318 | `m41_selfcheck.json` | `$I0Z6T5W.json` | `$R0Z6T5W.json` | ✅✅✅✅ | ✅ |
| 560 | `m41_selfcheck.py` | `5f066493fdbce49e63b34f00997643adbf70d1530801f44ae6c9405bdf4376a0` | 1,291 | `m41_selfcheck.py` | `$IAS8V3B.py` | `$RAS8V3B.py` | ✅✅✅✅ | ✅ |
| 561 | `m41_src_shas.py` | `47a192be190a4f299be73398e77b3aafec6eb85207520beee0577a2b79445263` | 1,138 | `m41_src_shas.py` | `$ID84QI8.py` | `$RD84QI8.py` | ✅✅✅✅ | ✅ |
| 562 | `m41_src_shas.txt` | `b2c58664cd515e97d520e8acfca07519d062a007463364d521b5bc1e7a8371d3` | 420 | `m41_src_shas.txt` | `$INI1OXV.txt` | `$RNI1OXV.txt` | ✅✅✅✅ | ✅ |
| 563 | `material_expansion_kill_freeze_2026_10_16.json` | `03a628456f0bb31320c6635d198621e18c7b249b90fb49eb4d02a9ed9bc89b5b` | 15,187 | `material_expansion_kill_freeze_2026_10_16.json` | `$INNMNVT.json` | `$RNNMNVT.json` | ✅✅✅✅ | ✅ |
| 564 | `me_llm_calls_2026_10_16.jsonl` | `fbdedcb0ef481828a991f9c8f004af83b3935959da8ce8ddcc5fe7b81df23d30` | 21,339 | `me_llm_calls_2026_10_16.jsonl` | `$IAS0XAS.jsonl` | `$RAS0XAS.jsonl` | ✅✅✅✅ | ✅ |
| 565 | `me_t4_resolve_2026_10_16.py` | `71b0e9c8da44d0806fd9ce071f83932edd632fe2fabf544004a0a310e38d10c1` | 9,507 | `me_t4_resolve_2026_10_16.py` | `$IJTYMZ1.py` | `$RJTYMZ1.py` | ✅✅✅✅ | ✅ |
| 566 | `mq04_budget_calc_2026_10_15.json` | `e8a5b2533ac2f3f914151a4477cd86c2414bcce18024cb30b73fe55e743a69f1` | 5,436 | `mq04_budget_calc_2026_10_15.json` | `$ILQU3ZH.json` | `$RLQU3ZH.json` | ✅✅✅✅ | ✅ |
| 567 | `mq04_budget_calc_2026_10_15.py` | `e5e4fcfd5e29a246dbaebddaaec6309465306e8f2d9d455a922c5f5c15afd75a` | 6,803 | `mq04_budget_calc_2026_10_15.py` | `$I0CJT0X.py` | `$R0CJT0X.py` | ✅✅✅✅ | ✅ |
| 568 | `mq04_nt_llm_calls_2026_10_15.jsonl` | `734af91354412565c3b439e84b966439b892717e45a8c0f0af2f5b176a13c92d` | 24,320 | `mq04_nt_llm_calls_2026_10_15.jsonl` | `$IYM78AI.jsonl` | `$RYM78AI.jsonl` | ✅✅✅✅ | ✅ |
| 569 | `mq04_nt_measure_2026_10_15.py` | `5e55c0ff27f80a63ab96424c1c86f30239764d5ac18433e3fc21788a7cb73990` | 14,503 | `mq04_nt_measure_2026_10_15.py` | `$IPJTMJV.py` | `$RPJTMJV.py` | ✅✅✅✅ | ✅ |
| 570 | `mq04_nt_measurement_2026_10_15.json` | `956d35f25c705e3f60192f57ef19b44d85c4cc8ea8d0770f69aa6e95f4135e2e` | 6,047 | `mq04_nt_measurement_2026_10_15.json` | `$I9TIM61.json` | `$R9TIM61.json` | ✅✅✅✅ | ✅ |
| 571 | `mq04_write_doc_2026_10_15.py` | `7fb01308674172898747dc3963a16c1325b56926651b32da9d2c880fe0c61e56` | 26,377 | `mq04_write_doc_2026_10_15.py` | `$I08AOCE.py` | `$R08AOCE.py` | ✅✅✅✅ | ✅ |
| 572 | `pa_block.py` | `19ac8c59439b06a769115440d5cef8ee0378823147fc34befedd015b89bba1c9` | 345 | `pa_block.py` | `$IUHA7LJ.py` | `$RUHA7LJ.py` | ✅✅✅✅ | ✅ |
| 573 | `pk_lockv2_degeneracy_2026_10_15.json` | `1106bb7d5c5650a4de4c7b3a64a8f34bc61c373d16be36362f3d93bd5dc5e863` | 2,583 | `pk_lockv2_degeneracy_2026_10_15.json` | `$IHSWDH6.json` | `$RHSWDH6.json` | ✅✅✅✅ | ✅ |
| 574 | `pk_lockv2_degeneracy_2026_10_15.py` | `e8067070c8498c79fc26a287c196dc97b6e8a7f8629e250aedae8fd4429bd497` | 2,425 | `pk_lockv2_degeneracy_2026_10_15.py` | `$IFF9GSO.py` | `$RFF9GSO.py` | ✅✅✅✅ | ✅ |
| 575 | `pk_lockv2_verify_2026_10_15.json` | `34cf77faf82570e2eefacd7c32cdc59273f569af75d3eb8c713d49770e2b3008` | 4,691 | `pk_lockv2_verify_2026_10_15.json` | `$IE992KD.json` | `$RE992KD.json` | ✅✅✅✅ | ✅ |
| 576 | `pk_lockv2_verify_2026_10_15.py` | `67795949087d8165675729d11646b1773046305936218463c2544065db0a89c1` | 3,784 | `pk_lockv2_verify_2026_10_15.py` | `$IPMTXT0.py` | `$RPMTXT0.py` | ✅✅✅✅ | ✅ |
| 577 | `pk_lockv2_write_2026_10_15.py` | `440affa3e1027bce2ada7df43af93513615be1d6b1b3cba92d78b74c3953f090` | 33,749 | `pk_lockv2_write_2026_10_15.py` | `$IU1V47I.py` | `$RU1V47I.py` | ✅✅✅✅ | ✅ |
| 578 | `pk_measure_01.py` | `76af3ed43f2cc686dad8f7f8c843377818478c34ac1e094f1fc659cd1f094edd` | 1,510 | `pk_measure_01.py` | `$IDPUC15.py` | `$RDPUC15.py` | ✅✅✅✅ | ✅ |
| 579 | `pk_probe2_2026_10_16.py` | `632e6dca295d934cf3f6a23455587836a3dfdc6920358b960d3f400e98ff8bd4` | 1,140 | `pk_probe2_2026_10_16.py` | `$ID6UJM6.py` | `$RD6UJM6.py` | ✅✅✅✅ | ✅ |
| 580 | `pk_probe_2026_10_16.py` | `809cf2066d48b819aca9717f83d437c3e39fea613ef9539f6f8bcbbec1d2c80a` | 878 | `pk_probe_2026_10_16.py` | `$IA2OENF.py` | `$RA2OENF.py` | ✅✅✅✅ | ✅ |
| 581 | `pk_supp500_calc_2026_10_16.py` | `5325e2e6bc002bc38696eefa9e54d6f5a6f96f3df8573f069dd002688987b5f2` | 3,079 | `pk_supp500_calc_2026_10_16.py` | `$ICP9958.py` | `$RCP9958.py` | ✅✅✅✅ | ✅ |
| 582 | `pk_t5lock_verify_2026_10_15.json` | `0b9c36f612daf8aa2ac2b0739680eadaf439a8195b6242b0b07b3c27184f79ca` | 4,931 | `pk_t5lock_verify_2026_10_15.json` | `$IPQ2U1Z.json` | `$RPQ2U1Z.json` | ✅✅✅✅ | ✅ |
| 583 | `pk_t5lock_verify_2026_10_15.py` | `3f21b53443b43e1c295c1b0002ae1d97a4634bb59605bfe692565391e41f0143` | 5,559 | `pk_t5lock_verify_2026_10_15.py` | `$IGYWKPS.py` | `$RGYWKPS.py` | ✅✅✅✅ | ✅ |
| 584 | `pk_t5lock_write_2026_10_15.py` | `e80c2626944692fd38081723467ccd2f2140e2859bf78af491cd39e4532200b2` | 3,938 | `pk_t5lock_write_2026_10_15.py` | `$INROY0J.py` | `$RNROY0J.py` | ✅✅✅✅ | ✅ |
| 585 | `pk_write_budget210_2026_10_16.py` | `0c65c2e859f954910f00209b4138f0fa9abcb6ee91190d547ead2bb3b6d0a57c` | 20,931 | `pk_write_budget210_2026_10_16.py` | `$ICWE6C2.py` | `$RCWE6C2.py` | ✅✅✅✅ | ✅ |
| 586 | `pk_write_design_review_2026_10_16.py` | `439fa0ae048df8047fc3568e9fc0485d755a75bcab09699e27479462b5512a7f` | 47,618 | `pk_write_design_review_2026_10_16.py` | `$IYILMF9.py` | `$RYILMF9.py` | ✅✅✅✅ | ✅ |
| 587 | `pool_search.py` | `3245af3f3bbba6f2f433be5e0b4c5a40f00dcd151eddbca2438f609bb2590111` | 2,127 | `pool_search.py` | `$IW9J5MM.py` | `$RW9J5MM.py` | ✅✅✅✅ | ✅ |
| 588 | `prep.py` | `e401c8e50f9325e69d44f74e614038ed3565945803d114edeecdfc263c525592` | 4,091 | `prep.py` | `$ICXREJL.py` | `$RCXREJL.py` | ✅✅✅✅ | ✅ |
| 589 | `probe3_out.txt` | `d2cef770903398126b6d0289a2a58a3f9170355c642e4054e52c771a52e60706` | 41,096 | `probe3_out.txt` | `$IHPP7S6.txt` | `$RHPP7S6.txt` | ✅✅✅✅ | ✅ |
| 590 | `r3m2_disp_write.py` | `988c2fee3ea29da11dbec49c582143c965b866479fe31186e135befee5992b7f` | 18,437 | `r3m2_disp_write.py` | `$IZMYTZ1.py` | `$RZMYTZ1.py` | ✅✅✅✅ | ✅ |
| 591 | `r461_layers.json` | `fee35e10c20893832aaca3b9018b4d9fb7e1ae5e0fb760f048c13c7d658ce4ba` | 102,003 | `r461_layers.json` | `$IDCGZH7.json` | `$RDCGZH7.json` | ✅✅✅✅ | ✅ |
| 592 | `r461_write_01.py` | `9030a50780daa56f6fc0a1e1c5377a0452e8fcb5be93bdfaa7837dea32b7dca0` | 19,104 | `r461_write_01.py` | `$IE2BE7I.py` | `$RE2BE7I.py` | ✅✅✅✅ | ✅ |
| 593 | `recheck2.py` | `85c4cfa3eb4678bc9e9d8d5a43461b0687c395f396cc4106a44c2121d92f45cc` | 2,282 | `recheck2.py` | `$I56PIPS.py` | `$R56PIPS.py` | ✅✅✅✅ | ✅ |
| 594 | `run_steps.py` | `019f8405d4cf62501fa65ebc047a81e9e946ae7bc906674dc0ced900859339e1` | 2,756 | `run_steps.py` | `$I1X8DMX.py` | `$R1X8DMX.py` | ✅✅✅✅ | ✅ |
| 595 | `s3_recompute_pass4.py` | `6f210893fccef42c02f43c56d2800886df36fb50511db29295fb2ca93617770e` | 4,439 | `s3_recompute_pass4.py` | `$I24BM1C.py` | `$R24BM1C.py` | ✅✅✅✅ | ✅ |
| 596 | `s4_regen_runner.py` | `70467364bdb1567ea7b1682420e1244920cf12adc479144a5b20df800a0c92cf` | 13,040 | `s4_regen_runner.py` | `$I3D46EY.py` | `$R3D46EY.py` | ✅✅✅✅ | ✅ |
| 597 | `scan_classify_five_terminal_2026_10_10.py` | `0b9b590835341a09fbcff0bc74a2dbb81500b419f9794fe02cc039c9f16f0090` | 7,603 | `scan_classify_five_terminal_2026_10_10.py` | `$IX0I39C.py` | `$RX0I39C.py` | ✅✅✅✅ | ✅ |
| 598 | `scan_domain_five_terminal_2026_10_10.py` | `732489dc3dbde73e7550f035b9f8645031d33ad3c4cb4921625d0de5d3d715de` | 2,243 | `scan_domain_five_terminal_2026_10_10.py` | `$IELKFKO.py` | `$RELKFKO.py` | ✅✅✅✅ | ✅ |
| 599 | `scan_supplement_five_terminal_2026_10_10.py` | `7c0a6d0221047ddd544d28652f3f719e9dc61408ec1388bbf6fee1b806fc3c72` | 6,010 | `scan_supplement_five_terminal_2026_10_10.py` | `$ISP6PT1.py` | `$RSP6PT1.py` | ✅✅✅✅ | ✅ |
| 600 | `scope_scan.py` | `07349acfe90fa890129c4d9c34a15632bef517327cd3b961172e751b703e3a47` | 3,380 | `scope_scan.py` | `$IMH7V3I.py` | `$RMH7V3I.py` | ✅✅✅✅ | ✅ |
| 601 | `singlevar.py` | `f0bba43af3e5c711b891546abec169ebe673600340c01459e8d575f01e08b166` | 1,515 | `singlevar.py` | `$ITSEVMC.py` | `$RTSEVMC.py` | ✅✅✅✅ | ✅ |
| 602 | `t2_path_b_kill_freeze_2026_10_16.json` | `3f3272100f624cf1f0dedd7727566d3a953fc4899fc48e7336e425d7467be8b3` | 14,896 | `t2_path_b_kill_freeze_2026_10_16.json` | `$I75EQIY.json` | `$R75EQIY.json` | ✅✅✅✅ | ✅ |
| 603 | `t2b_census_2026_10_16.py` | `71f99afb91991de2ad735ca812e70fc1420c658373d5fc56bd875fd725819e54` | 3,041 | `t2b_census_2026_10_16.py` | `$I2AFNFV.py` | `$R2AFNFV.py` | ✅✅✅✅ | ✅ |
| 604 | `t2b_derive_2026_10_16.py` | `324165eb0c7d0c5f8e251e705f6686d5583bbcabf3a31f7df4d77bb4f050e56e` | 7,964 | `t2b_derive_2026_10_16.py` | `$IH1OIDO.py` | `$RH1OIDO.py` | ✅✅✅✅ | ✅ |
| 605 | `t2b_fetch_facts_2026_10_16.py` | `0941558d024e43546424d866a657c22b6a38594b09effdd23d44abb8f064974d` | 5,774 | `t2b_fetch_facts_2026_10_16.py` | `$I27BHP3.py` | `$R27BHP3.py` | ✅✅✅✅ | ✅ |
| 606 | `t2b_freeze_2026_10_16.py` | `575b796a2e6fb3aa35137ef27f5f57cb916e05783ccf19a558fee17cb9db790f` | 13,908 | `t2b_freeze_2026_10_16.py` | `$ISPZC41.py` | `$RSPZC41.py` | ✅✅✅✅ | ✅ |
| 607 | `t2b_freeze_v2_2026_10_16.py` | `02a261b12f7b9c6632bac8368f859cd06a1ff4c6253beb8b4d7218a91535bfeb` | 17,044 | `t2b_freeze_v2_2026_10_16.py` | `$IQWLC80.py` | `$RQWLC80.py` | ✅✅✅✅ | ✅ |
| 608 | `t2b_harness_pre_change_snapshot_2026_10_16.py` | `d5c8d676bb5b6b4e7fb3a6cb61ea331543be363b61b0801997d5a7c9b114ee98` | 36,217 | `t2b_harness_pre_change_snapshot_2026_10_16.py`, `_pre_mod/exp_harness_pre.py` | `$ISP87O5.py` | `$RSP87O5.py` | ✅✅✅✅ | ✅ |
| 609 | `t2b_impl_audit_2026_10_16.py` | `e02a343246bdd0ce72a1e9e8881b86521ea304a4b500e1d827241e4fdaca19f5` | 4,856 | `t2b_impl_audit_2026_10_16.py` | `$ILFJFYK.py` | `$RLFJFYK.py` | ✅✅✅✅ | ✅ |
| 610 | `t2b_inspect_facts_2026_10_16.py` | `de3c879e39f1479245721bda5ea43dce5e57140774f1f07af02471d4c5762249` | 1,732 | `t2b_inspect_facts_2026_10_16.py` | `$I8PBZ4S.py` | `$R8PBZ4S.py` | ✅✅✅✅ | ✅ |
| 611 | `t2b_llm_calls_2026_10_16.jsonl` | `a54a3af46ba2f9100703c736e18cd35cf66a96120e51084c29dadb9ac5c152d3` | 5,317 | `t2b_llm_calls_2026_10_16.jsonl` | `$ICRQA0R.jsonl` | `$RCRQA0R.jsonl` | ✅✅✅✅ | ✅ |
| 612 | `t2b_measure_2026_10_16.py` | `bd377372927c4c03ff3455a6d045813476c506380f23a02cf7dc4b5b61df6ca0` | 15,547 | `t2b_measure_2026_10_16.py` | `$IZS9HBC.py` | `$RZS9HBC.py` | ✅✅✅✅ | ✅ |
| 613 | `t2b_measurement_2026_10_16.json` | `fe5db6defb0953b9a78622b3b49e6739e619fa8fddef71917ac782e059d8ecf7` | 25,796 | `t2b_measurement_2026_10_16.json` | `$IKP1WV6.json` | `$RKP1WV6.json` | ✅✅✅✅ | ✅ |
| 614 | `t2b_patch_harness_2026_10_16.py` | `bac4775c5c44a63b57fb46233533abf64bc878297e0b3d3f9cd228a606d21850` | 7,065 | `t2b_patch_harness_2026_10_16.py` | `$I1Y529J.py` | `$R1Y529J.py` | ✅✅✅✅ | ✅ |
| 615 | `t2b_strategyqa_train_snapshot_2026_10_16.json` | `728e28b7d6bdfe6da3a0a5f8c5923113a79063d199e960cfcc9f8a3ab34cd92c` | 4,281,955 | `t2b_strategyqa_train_snapshot_2026_10_16.json` | `$I8E4KIG.json` | `$R8E4KIG.json` | ✅✅✅✅ | ✅ |
| 616 | `t3_baseline_procedure_probe.py` | `b4c2a5e68dfabc35c865e0ad981a5fc0d0d695982ffaf62306f53d35259959af` | 2,292 | `t3_baseline_procedure_probe.py` | `$IKRT5Z7.py` | `$RKRT5Z7.py` | ✅✅✅✅ | ✅ |
| 617 | `t3_baseline_procedure_probe_2026_10_15.json` | `7ac600d45dcc52d31a670feceb3c972dea2dc0959a7ea9baf77a3e86ec8f448f` | 1,332 | `t3_baseline_procedure_probe_2026_10_15.json` | `$ILW40MA.json` | `$RLW40MA.json` | ✅✅✅✅ | ✅ |
| 618 | `t3_freeze_2026_10_15.json` | `313f091718cc3f9dd504d7fac7ceaf00f69b7971d47afef7ff6c960e233a09fd` | 7,436 | `t3_freeze_2026_10_15.json` | `$IF4E9HR.json` | `$RF4E9HR.json` | ✅✅✅✅ | ✅ |
| 619 | `t3_nt_llm_calls_2026_10_15.jsonl` | `0cb1decec8787bc5540c8e402d3b723dba82e7d3ff6e5490ccbd4afe6a65b1ce` | 5,250 | `t3_nt_llm_calls_2026_10_15.jsonl` | `$I8VUMSF.jsonl` | `$R8VUMSF.jsonl` | ✅✅✅✅ | ✅ |
| 620 | `t3_nt_measure_2026_10_15.py` | `35860b379b7af3f6cd7285bf827d942d96120dc188cd49281c8218bcb076e31a` | 17,111 | `t3_nt_measure_2026_10_15.py` | `$ID22B6F.py` | `$RD22B6F.py` | ✅✅✅✅ | ✅ |
| 621 | `t3_nt_measurement_2026_10_15.json` | `92f0dc763cafc9bbfe22df823f6b34c2d46da6eb0f26dce608a7b5bdf4715ae6` | 19,576 | `t3_nt_measurement_2026_10_15.json` | `$IBF7J5R.json` | `$RBF7J5R.json` | ✅✅✅✅ | ✅ |
| 622 | `t3_nt_verify.py` | `a1c38dc17d65a1f0fc468e26e751804279f04ef46c1ab26e51829cbb651a25a5` | 6,657 | `t3_nt_verify.py` | `$I85O1LU.py` | `$R85O1LU.py` | ✅✅✅✅ | ✅ |
| 623 | `t3_nt_verify_2026_10_15.json` | `700de33ee255c11713448caa97a613b988d3abb51c2749ec7784fe9d807c5ed5` | 3,885 | `t3_nt_verify_2026_10_15.json` | `$I9GS1T5.json` | `$R9GS1T5.json` | ✅✅✅✅ | ✅ |
| 624 | `t3_postchange_equiv.py` | `1e579de6033cea59362cbc6cf99d84ba9d3850d7aaeed51fa59691f20101d15f` | 5,975 | `t3_postchange_equiv.py` | `$ID2T7C7.py` | `$RD2T7C7.py` | ✅✅✅✅ | ✅ |
| 625 | `t3_postchange_equiv_2026_10_15.json` | `e8a97dc64a089bae4bc3207f5026afddd6f397896510f53d74ab06289d8e3b12` | 3,904 | `t3_postchange_equiv_2026_10_15.json` | `$IZZGHXI.json` | `$RZZGHXI.json` | ✅✅✅✅ | ✅ |
| 626 | `t3_postchange_manifest_check_2026_10_15.json` | `dbfae4d96b46056137135aaf1c8c006592a14ce2d36b62b471a86daccde444dd` | 2,135 | `t3_postchange_manifest_check_2026_10_15.json` | `$I7MQMEX.json` | `$R7MQMEX.json` | ✅✅✅✅ | ✅ |
| 627 | `t3_postcheck.py` | `20c96933b00d2b870486a5553a80ab410c4e62e8d62d33f6eb4ca89e3f249c3b` | 3,129 | `t3_postcheck.py` | `$IZKA3ZW.py` | `$RZKA3ZW.py` | ✅✅✅✅ | ✅ |
| 628 | `t3_prechange_manifest_2026_10_15.json` | `f1508ebe14e7a8d10b37366719ce99a495de887a784e6f666379bffd59f40676` | 76,683 | `t3_prechange_manifest_2026_10_15.json` | `$ITW8A5Y.json` | `$RTW8A5Y.json` | ✅✅✅✅ | ✅ |
| 629 | `t3_prove_minimal_increment_2026_10_15.json` | `3f858f6958cd75e7bf3c24ace5353b905f8b9b4a1c7f5a70a8dd0e9904512bd1` | 433 | `t3_prove_minimal_increment_2026_10_15.json` | `$INBPV2X.json` | `$RNBPV2X.json` | ✅✅✅✅ | ✅ |
| 630 | `t3_prove_minimal_increment_2026_10_15.py` | `1f39cf0688622f552276167db2a2a140c2cfbdc7ef47f9c662937c6fc89bc583` | 7,303 | `t3_prove_minimal_increment_2026_10_15.py` | `$IWJTLIK.py` | `$RWJTLIK.py` | ✅✅✅✅ | ✅ |
| 631 | `t3_repro_probe_ftfb_freeze_2026_10_16.json` | `44761c404b862a7425f0492a01c8aa7ad037ddb8794f6af599b7af427c425694` | 2,936 | `t3_repro_probe_ftfb_freeze_2026_10_16.json` | `$IGQYVL4.json` | `$RGQYVL4.json` | ✅✅✅✅ | ✅ |
| 632 | `t3_repro_probe_llm_calls_2026_10_16.jsonl` | `54ad4d2cd8bf5f605793f22cf0ef9f4077a409273f9d9c28788d3184a682731c` | 7,441 | `t3_repro_probe_llm_calls_2026_10_16.jsonl` | `$IL2BZAK.jsonl` | `$RL2BZAK.jsonl` | ✅✅✅✅ | ✅ |
| 633 | `t3_repro_probe_measure_2026_10_16.json` | `31779f66c051be37d0d7024633bb9de48f2efc1e7d413501293b0e9e81a96a74` | 9,137 | `t3_repro_probe_measure_2026_10_16.json` | `$IWYF2RY.json` | `$RWYF2RY.json` | ✅✅✅✅ | ✅ |
| 634 | `t5_baseline_manifest_2026_10_15.json` | `2d5ad82c0a63331b042ee3b5aa1942c4fe7d7e47352808b3f1b65983c653cbb8` | 99,724 | `t5_baseline_manifest_2026_10_15.json` | `$IHO5QY2.json` | `$RHO5QY2.json` | ✅✅✅✅ | ✅ |
| 635 | `t5_kill_line_freeze_2026_10_15.json` | `1910a62c1e9fb43fdefbabb64b329518018abf08e86137ad6932720876ce5c11` | 3,183 | `t5_kill_line_freeze_2026_10_15.json` | `$IBU5Y8K.json` | `$RBU5Y8K.json` | ✅✅✅✅ | ✅ |
| 636 | `t5_nt_llm_calls_2026_10_15.jsonl` | `8e488d14bff6862f412b6d79628e5f9a70e4332a78cdfce4bd2461f1560f0e5e` | 7,258 | `t5_nt_llm_calls_2026_10_15.jsonl` | `$I9Y45AY.jsonl` | `$R9Y45AY.jsonl` | ✅✅✅✅ | ✅ |
| 637 | `t5_nt_measure_2026_10_15.py` | `c96c985d8e231a65765ae892a361de5b919bd3efa683117031d33ea092ab5ece` | 15,602 | `t5_nt_measure_2026_10_15.py` | `$I2ZUYH8.py` | `$R2ZUYH8.py` | ✅✅✅✅ | ✅ |
| 638 | `t5_nt_measurement_2026_10_15.json` | `674e95ecff030905c0c84a7aa870a03d7566515d2f8021bf00a076758d0cb2b5` | 3,845 | `t5_nt_measurement_2026_10_15.json` | `$I96PVJZ.json` | `$R96PVJZ.json` | ✅✅✅✅ | ✅ |
| 639 | `t5_prove_minimal_increment_2026_10_15.py` | `65cec9c9788e44b5536ba4573b6fbe9fc56483e5e6e871aa112fdf3b8a831768` | 6,308 | `t5_prove_minimal_increment_2026_10_15.py` | `$IO4RKR4.py` | `$RO4RKR4.py` | ✅✅✅✅ | ✅ |
| 640 | `t5_write_docs_2026_10_15.py` | `f104bf4706e67ffdab89ace7d002cbb89e10c70fe90c3759d5a32e31959a9902` | 47,918 | `t5_write_docs_2026_10_15.py` | `$ICGBBGR.py` | `$RCGBBGR.py` | ✅✅✅✅ | ✅ |
| 641 | `tables.py` | `02cc157b6d69695857ef1816d468cb4c75ddcfac3ca7ed0bd1fc69f6ab74a9f4` | 1,818 | `tables.py` | `$I5HPA0A.py` | `$R5HPA0A.py` | ✅✅✅✅ | ✅ |
| 642 | `three_seed_caliber_decl_2026_10_16.json` | `5df309d557b08ffd9ae8c593df9560b825ba49b61927d1be93a33401497695c8` | 4,859 | `three_seed_caliber_decl_2026_10_16.json` | `$INYEEG5.json` | `$RNYEEG5.json` | ✅✅✅✅ | ✅ |
| 643 | `three_seed_collect_2026_10_16.py` | `672d12ad98013846db85a194806edcf3baffd6064469e4bf9fa5b35ed4c4c563` | 28,520 | `three_seed_collect_2026_10_16.py` | `$II57LZK.py` | `$RI57LZK.py` | ✅✅✅✅ | ✅ |
| 644 | `three_seed_collect_log_2026_10_16.txt` | `55c783261d187c13e26644057930e404f6bfd03a053100e998f881ef1da80bca` | 16,230 | `three_seed_collect_log_2026_10_16.txt` | `$IZUWGDJ.txt` | `$RZUWGDJ.txt` | ✅✅✅✅ | ✅ |
| 645 | `three_seed_freeze_2026_10_16.json` | `46260e3b842677dd5383aaf4e02f1da3884f403dc7ba7658b82d303e815d27f0` | 10,536 | `three_seed_freeze_2026_10_16.json` | `$IBASYTR.json` | `$RBASYTR.json` | ✅✅✅✅ | ✅ |
| 646 | `three_seed_llm_calls_2026_10_16.jsonl` | `5a8cbcf85aa74b55089afb4793bcb334ffd0301f00bdb1dc449db8988b8e6bf0` | 104,288 | `three_seed_llm_calls_2026_10_16.jsonl` | `$ILJPOGV.jsonl` | `$RLJPOGV.jsonl` | ✅✅✅✅ | ✅ |
| 647 | `three_seed_measurement_2026_10_16.json` | `ff5ed4b0e3297388a5cafea6912a8cb4e811b40ce9cd4e36bb5fd3a400e7a8e0` | 226,256 | `three_seed_measurement_2026_10_16.json` | `$IY1FR4J.json` | `$RY1FR4J.json` | ✅✅✅✅ | ✅ |
| 648 | `three_seed_preflight_2026_10_16.py` | `98e0e4ae7a73545fdfeef8efe24c344098fe4d4eff45ca61fb24d388632e57a8` | 5,661 | `three_seed_preflight_2026_10_16.py` | `$I1JBN8L.py` | `$R1JBN8L.py` | ✅✅✅✅ | ✅ |
| 649 | `three_seed_verify_2026_10_16.json` | `61e3d0bfa05da9c937790c305f3a4970bc8090718bf8797b7548b6193b8e5f38` | 3,205 | `three_seed_verify_2026_10_16.json` | `$I12LYRA.json` | `$R12LYRA.json` | ✅✅✅✅ | ✅ |
| 650 | `three_seed_verify_2026_10_16.py` | `5c382ace957396d1b934f9adddb22759e252fb4c7ab0a7e800bfa937288304a8` | 13,402 | `three_seed_verify_2026_10_16.py` | `$IJKCVU8.py` | `$RJKCVU8.py` | ✅✅✅✅ | ✅ |
| 651 | `three_seed_write_doc_2026_10_16.py` | `f546bdd3630c505e7231d9292c20e00be01d0b83a7edeaefe21997517392cca2` | 50,308 | `three_seed_write_doc_2026_10_16.py` | `$IQZFMIJ.py` | `$RQZFMIJ.py` | ✅✅✅✅ | ✅ |
| 652 | `u04_1_chain_verify.py` | `13e573534692431260298451065c1f93af6226d4337832ea60da18e4deec6462` | 4,849 | `u04_1_chain_verify.py` | `$IT1THYS.py` | `$RT1THYS.py` | ✅✅✅✅ | ✅ |
| 653 | `u04_1_dual_verify.py` | `f5702456560fad4c9aad1cc16c0ddc479ac2d7c27de08a7a359ca6c9eb9d064e` | 3,228 | `u04_1_dual_verify.py` | `$ICQ7UVL.py` | `$RCQ7UVL.py` | ✅✅✅✅ | ✅ |
| 654 | `u04_1_make_data.py` | `309ac58e049ddd94515c20845abfdcbaa683e30c0324cd80e2cbd4f8cc8a060d` | 19,773 | `u04_1_make_data.py` | `$IO74VOA.py` | `$RO74VOA.py` | ✅✅✅✅ | ✅ |
| 655 | `verify_final.py` | `904eb215f1398b53b5a3fb5dc6c7efa37cb4aba3bb9059059d175f0b61e1c280` | 805 | `verify_final.py` | `$IROLGNP.py` | `$RROLGNP.py` | ✅✅✅✅ | ✅ |
| 656 | `verify_t3trap_bprime_2026_10_15.py` | `a9e880243eab308cd0ce4291bc9888a529ea2a0eced0a075c25f317ba4da7503` | 6,928 | `verify_t3trap_bprime_2026_10_15.py` | `$IOAOYSJ.py` | `$ROAOYSJ.py` | ✅✅✅✅ | ✅ |
| 657 | `vk_denominator_2026_10_16.py` | `d935b89bfa31d077246ca492a89326fe27cd048fcedd1dd00aedc2661274bf9b` | 856 | `vk_denominator_2026_10_16.py` | `$IG3KBOS.py` | `$RG3KBOS.py` | ✅✅✅✅ | ✅ |
| 658 | `vk_interval_arith_2026_10_16.py` | `901d8df83bb3a6f704df80f49f69e07d95611f7d2229e023bd2877cb1c59f4a6` | 1,273 | `vk_interval_arith_2026_10_16.py` | `$IXOMU75.py` | `$RXOMU75.py` | ✅✅✅✅ | ✅ |
| 659 | `vk_v3df_0_1_agree.py` | `84c090952894753447fbb46840b85ba2fd48cc7a091933053ef09ba2714258f2` | 6,140 | `vk_v3df_0_1_agree.py` | `$IMQYJ8W.py` | `$RMQYJ8W.py` | ✅✅✅✅ | ✅ |
| 660 | `vk_v3df_0_1_coverage_gap.py` | `df25000e71806a03733d879e4ea9a66abe3572913f46d86d99e596890ee858af` | 1,971 | `vk_v3df_0_1_coverage_gap.py` | `$IBZ05BQ.py` | `$RBZ05BQ.py` | ✅✅✅✅ | ✅ |
| 661 | `vk_v3df_0_1_materiality.py` | `b666b7a38082148d075a146646782c32221719db010f582ba1b75e30b5a4ed45` | 2,875 | `vk_v3df_0_1_materiality.py` | `$I3NWKCO.py` | `$R3NWKCO.py` | ✅✅✅✅ | ✅ |
| 662 | `vk_v3df_0_1_verify_2026_10_09.py` | `0e7cb9348a1679d42b70239fc8810a52fc11aa31ebede70549230bfeef6478f3` | 14,347 | `vk_v3df_0_1_verify_2026_10_09.py` | `$I9H8UUW.py` | `$R9H8UUW.py` | ✅✅✅✅ | ✅ |
| 663 | `vk_verify_2026_10_16.py` | `6ad7edf03032dcdf587e4b188e89f418a523408c5b7b8699150dcf5188d6d5bd` | 3,780 | `vk_verify_2026_10_16.py` | `$IEGVMT8.py` | `$REGVMT8.py` | ✅✅✅✅ | ✅ |
| 664 | `vk_verify_interval_ceiling_2026_10_16.py` | `18b0f12b2c669a4379264b96a90142eca8fd436b055325e4bdb736ca803d7479` | 3,692 | `vk_verify_interval_ceiling_2026_10_16.py` | `$IBLVA2M.py` | `$RBLVA2M.py` | ✅✅✅✅ | ✅ |
| 665 | `vk_write_2026_10_16.py` | `2334a967a1d4b3dcf7aa31f31fe35dbc3dfdbbb7206defc894d22dca6a3bd3b9` | 62,030 | `vk_write_2026_10_16.py` | `$I54OIU2.py` | `$R54OIU2.py` | ✅✅✅✅ | ✅ |
| 666 | `vk_write_interval_ceiling_post_lock_2026_10_16.py` | `3076d727e02cca37a050bad775a24e113e356d98133c9f41165cdbf89baf6438` | 47,768 | `vk_write_interval_ceiling_post_lock_2026_10_16.py` | `$ISUZZMU.py` | `$RSUZZMU.py` | ✅✅✅✅ | ✅ |
| 667 | `write_items_json.py` | `9dce7986e20d5a2688423ad47c5d91102a81b191f92699042d357f7a56ea7f89` | 4,388 | `write_items_json.py` | `$IRJ512S.py` | `$RRJ512S.py` | ✅✅✅✅ | ✅ |
| 668 | `write_summary_json.py` | `6214ad3cdc2d71a7d148d11a7f8542827451031da7ad80d06b2174cfda8dabd2` | 9,049 | `write_summary_json.py` | `$IAHFAFD.py` | `$RAHFAFD.py` | ✅✅✅✅ | ✅ |
| 669 | `write_t3trap_bprime_2026_10_15.py` | `ca5fc520f530695b7c8a5e51a19fc580817b73884b36cba04130ecf965784841` | 33,905 | `write_t3trap_bprime_2026_10_15.py` | `$IDXE8NO.py` | `$RDXE8NO.py` | ✅✅✅✅ | ✅ |

---

## §5 保留面（20 件 · ⛔ 0 动 · 逐件复验）

### §5-1 R3 · 全域无任何孪生（17 件 · 148,185 B · ⚠ 全域唯一存本）

**0 触之自证**：清走后逐件复算 SHA-256 与冻结建表值**逐位一致**、bytes 一致、文件**在位**，**17 / 17 全等**；且三者**具名与 SHA 与前棒登记件 §4-1 之表逐项一致**（无漂移）。清走之命令之目标集**全部位于备份树之内**，本棒**未对备份树外任何路径发出删除命令**。

| 件名 | SHA-256 | bytes | 在位 | 与冻结值全等 |
| :-- | :-- | --: | :-: | :-: |
| `_recheck_r1_runA.log` | `68c85cf076d111da22c646f5af7b33348a36295b8ce4bc8439043c019c9390df` | 2,634 | ✅ | ✅ |
| `_recheck_r1_runB.log` | `68c85cf076d111da22c646f5af7b33348a36295b8ce4bc8439043c019c9390df` | 2,634 | ✅ | ✅ |
| `_recheck_r1_runC.log` | `b15384cff9f0f75ed825cda787789857b8e54892ec2e00ead4920cd440802332` | 2,568 | ✅ | ✅ |
| `_recheck_r1_runD.log` | `b15384cff9f0f75ed825cda787789857b8e54892ec2e00ead4920cd440802332` | 2,568 | ✅ | ✅ |
| `_rj5_convention_check_2026_09_27.out.json` | `c88e4ba1a4ce1caab9d598acfb9926300924aea4030e9898ba05c5470df3d037` | 8,983 | ✅ | ✅ |
| `_t1_gap_implA_2026_10_01.py` | `c5d1dc7badcdd0660cd417152f8e4b7f4fa0fe677c2ba162f0396d43f79a6469` | 4,468 | ✅ | ✅ |
| `_t1_gap_implB_2026_10_01.ps1` | `19aebfd44310a0f41a381c764a92473caf4a634443d1c717011e1abca077485d` | 5,735 | ✅ | ✅ |
| `_v5_item21_patched_b1_semA_none_default.py` | `ceb33de660fd5a43d3c22bd051ad9c6b281c92d8727bc435bca9fad5b4bd2770` | 16,768 | ✅ | ✅ |
| `_v5_item21_patched_b1_semB_none_skip.py` | `be0208abaffac626b33d0e7d4dcaf8539a128d059bb505d6c7260048bc27cae7` | 16,829 | ✅ | ✅ |
| `_v5_item21_patched_b2_semA_none_default.py` | `801ee31e8bdc24ab5a37cd65ee25660caabf4fd6f29f991c29c0ce4f34f1f443` | 16,036 | ✅ | ✅ |
| `_v5_item21_patched_b2_semB_none_skip.py` | `8293535673dc2e5aceec70fc9f0d1610e8026f8d4900730cb94c218f031496f9` | 16,097 | ✅ | ✅ |
| `_v5_item21_patched_b3_semA_none_default.py` | `9d8a4a875b6278bfd6f4cb985ee86b9350772c0acd30c9d5d0bdc5903c90fd54` | 15,778 | ✅ | ✅ |
| `_v5_item21_patched_b3_semB_none_skip.py` | `8df8e94724fff8d893276960764c2cb1422d162d41b173f586f8750ac0984174` | 15,839 | ✅ | ✅ |
| `ref_exp_harness_OLD_2026_10_15.py` | `7957bac14455fd45b546c51a22a85cc0460c07edd1c828bfbf2a759614b43d51` | 13,342 | ✅ | ✅ |
| `t3_harness_diff_2026_10_15.diff` | `0f8532aefdffaa3cc88a69c68fe321da7cfe390ea3aff0c9c5353abb9e443974` | 3,463 | ✅ | ✅ |
| `t5_harness_diff_2026_10_15.diff` | `6f1e9689201b9c4e65e6f9064e01f214a7169154593089526162146fa6d9f66d` | 4,043 | ✅ | ✅ |
| `t5_prefix_T1T4_digest_2026_10_15.json` | `9eb43782b73cd606440a285a5a6993d4a616283cdb9b2f6e2030e61eb4bfe6c8` | 400 | ✅ | ✅ |

📌 **成因（承前棒，本棒沿用而不代裁）**：前棒以 `③段-R2` 之快照复算，备份树 699 件于该快照时点 **100% 有孪生**；现仅 682 有孪生 ⇒ R3 之 17 件系 `③段-R2` 以「须有存活孪生」为据清 `.tmp\` 侧、以本备份面为存活孪生之净效应（见 `results/_stage3_r2_cleanup_register_2026_10_18.md` §3-1）。**非本棒所致**。**清之即实质内容灭失**。

### §5-2 R2 · 零字节退化同值（3 件 · 0 B）

**0 触之自证**：逐件复验 —— 在位 ＝ `True`、bytes ＝ **0**、SHA-256 ＝ `e3b0c442…b7852b855` ＝ 冻结建表值 ＝ 空内容哈希，**3 / 3 全等**。

| 件名 | bytes | SHA-256 | 在位 | 与冻结值全等 |
| :-- | --: | :-- | :-: | :-: |
| `_e_q_exec.txt` | 0 | `e3b0c44298fc…52b855` | ✅ | ✅ |
| `_m5_k5_net.err` | 0 | `e3b0c44298fc…52b855` | ✅ | ✅ |
| `_m5_k5_scan.err` | 0 | `e3b0c44298fc…52b855` | ✅ | ✅ |

### §5-3 备份树外之 0 触核验（件数复点，对照普查基线）

| 面 | 普查基线 | 清走后实测 | 增删 | 判定 |
| :-- | --: | --: | --: | :-- |
| `results\` | 1,156 | **1,163** | **＋7** | ⛔ 0 删除；增量**非本棒所致**（本棒于 `results\` **未发任何删除命令**，且本件写入前未于该面落任何件）——如实登记该面于本棒执行期间有他方增写 |
| `_remote_pullback_2026_10_17\` | 219 | **219** | **±0** | ✅ 0 触 |
| `deposon-sub` | 1,276 | **1,276** | **±0** | ✅ 0 触 |

---

## §6 停手候裁面（⛔ 0 自行推进）

| 候裁项 | 内容 | 最小待裁之问 |
| :-- | :-- | :-- |
| **H2b**（本棒新提） | **3 件零字节**于 `.tmp\` 判据下**形式成立**（退化空哈希同值） | 零字节退化同值是否计入「孪生」判据？若计入，清除集为 **672**；本棒按裁之数 **669** 行、3 件保留 |
| **H2**（承前棒·未答） | R2 之 3 件 | 同上（前棒已列，本棒 ⛔ 0 动） |
| **H3**（承前棒·未答） | R3 之 17 件（全域唯一存本，**非副本**） | 请 PI 明示其处置；**清之即实质内容灭失** |
| **H6**（本棒新提） | 本批之存续根据已由「可由 `results\` 再生·0 损失」变为「**仅存 `.tmp\` 易清面单份**」 | PI 裁已随权明示并加警；本棒据实登记：该 669 件之孪生面**与被清面同为 `.tmp\`**，若 `.tmp\` 被整体清理，**二者同尽** |
| **H7**（本棒新提） | 本棒自留工件落于 `.tmp\`（即与其所守护之孪生**同一易清面**） | 是否接受？若否，须移至他面 |
| **H8**（本棒新提） | §3-2 之命令长度上限致 3 块被截断（已由逐件复点全数补清） | 是否需为后续大批量清除面预设「分块 ＋ 逐件复点」之标准作业 |

---

## §7 计数对账

| 项 | 值 |
| :-- | --: |
| 清走前备份树 | **689 件 ／ 38,007,270 B** |
| 清走（清除集） | **669 件 ／ 37,859,085 B** |
| 清走后备份树（实测复点） | **20 件 ／ 148,185 B** |
| **件数对平** | 689 − 669 ＝ **20** ✅ |
| **字节对平** | 38,007,270 − 37,859,085 ＝ **148,185** ✅ |
| 保留（R3 17 ＋ R2 3） | 17 ＋ 3 ＝ **20** ✅ |
| 清走字节 ＋ 保留字节 | 37,859,085 ＋ 148,185 ＝ **38,007,270** ✅ |
| 验道通过 ／ 失败 | **669 ／ 0** ✅ |
| 非预期移除 | **0** |
| 预期移除而仍留存 | **0** |
| 孪生丢失 ／ 内容灭失 | **0**（清走前逐件复验 669 目标及其 673 个 `.tmp\` 孪生皆在位且逐位全等） |
| R3 之 17 件被触 | **0**（17 / 17 复验全等且在位） |
| R2 之 3 件被触 | **0**（3 / 3 复验全等且在位） |

---

## §8 字节级自报

| 项 | 值 |
| :-- | :-- |
| 落盘编码 | UTF-8 **无 BOM** · 纯 LF（`CR` 计数 ＝ 0） |
| 落前占位实测 | `Test-Path` ＝ `False`；`results\*whitelist_backup_669*` glob ＝ **0**；仓全域 `*whitelist_backup_669*` glob ＝ **0** |
| 本棒新增工件（`.tmp\`，**未清走**，供复核复算） | `_wb669_measure_2026_10_18.py`、`_wb669_census_2026_10_18.json`、`_wb669_crosscheck_2026_10_18.py`、`_wb669_targets_2026_10_18.json`、`_wb669_c2_2026_10_18.py`、`_wb669_c2_2026_10_18.json`、`_wb669_criteria_freeze_2026_10_18.md`、`_wb669_mkspec_2026_10_18.py`、`_wb669_spec_sample.json`、`_wb669_verify_2026_10_18.py`、`_wb669_verify_sample.json`、`_wb669_progress_2026_10_18.py`、`_wb669_dbg_2026_10_18.py`、`_wb669_len_2026_10_18.py`、`_wb669_chunks_2026_10_18.py`、`_wb669_chunks_2026_10_18.txt`、`_wb669_names_2026_10_18.py`、`_wb669_names_2026_10_18.txt`、`_wb669_names2_2026_10_18.py`、`_wb669_names2_2026_10_18.txt`、`_wb669_names3_2026_10_18.py`、`_wb669_names3_2026_10_18.txt`、`_wb669_rem_2026_10_18.py`、`_wb669_rem_2026_10_18.txt`、`_wb669_final_2026_10_18.py`、`_wb669_final_2026_10_18.json`、`_wb669_r2check_2026_10_18.py` |
| 净清走 | **669 件 ／ 37,859,085 B**（不含本棒自留工件） |
| 永久删除 | **0**（全程经可恢复通道；`Remove-Item` 使用次数 ＝ 0） |
| 新建备份 | **0** |

**本件为执行登记件 · ⛔ 0 落五终判 · ⛔ 0 宣告段毕/①毕 · ⛔ 0 代 PI 裁。**
