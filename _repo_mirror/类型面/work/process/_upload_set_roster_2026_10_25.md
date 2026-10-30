# 上传集名单件（对外版·远端公开仓之上传集）· 2026-10-25

> 📌 **本棒为回棒复活**（本会话于 2026-10-25 约 11:0x 断连；PI 实测 `results\` 按名 `*upload_set*` **0 命中** ⇒ 件未落盘）——本件为**断连后之续作**，非重作：§3 名单之逐件实测于断连**前**已测毕并留存（见 §7-1）。
> 📌 **本件性质**：**名单件（口径固化面）**——⛔0 落五终判｜⛔0 闭 `KD`｜⛔0 宣告段毕或门槛成就｜⛔0 代 PI 裁。
> 📌 **派工**：PI 裁 134（`pi_rulings\_pi_card_answers_register_2026_10_25_v321.md` §1 表 **L21** 逐字：「**派 `protocol-keeper` 出『上传集名单』件**」）——该件本棒自测 **3,706／`9cc90b8a206a`**。
> 📌 **棒别**：`protocol-keeper`（口径与预登记官）｜**观测时点**：2026-10-25 **10:44–11:40 UTC+8**（本会话）。
> 📌 **铁律遵守**：⛔0 回改任何既有件一字｜⛔0 移动／重命名／删除任一既有件｜⛔0 新建目录｜⛔0 联网｜⛔0 向远端推送任何东西｜⛔0 跑实验｜⛔0 读 `〔本地路径已脱敏〕`（⛔0 读内容·⛔0 取指纹）｜⛔0 读归档区正文（**仅按名与指纹认人**）｜⛔0 调 LLM·API｜⛔0 落五终判／闭 `KD`／宣告段毕｜⛔0 代 PI 裁。
> 📌 **本棒实际携带之 skill**：`scientific-research-workflows:experimental-design`（**实带·已加载正文**）——路径 `〔本地路径已脱敏〕`，**本棒自测 13,044／`0a314eed103a`**。⚠ **诚实登记**：其正文之实验设计体例（随机化／区组／伪重复）对本件之**口径固化面无直接贡献**，本件**未据其任何条文立判**；实带之事实仅登记于此。

---

## §0 一句话（上传集之定义）

> **上传集 U ＝ 以在册分母（`deposon-repo` 去仓根 `.tmp` ＋ `deposon-sub` 全文件）为域，经「必上传 8／9 类」之准入、经「归档区不上传／仓根 `.tmp`／在途闸／HF-A…HF-M／加严①②／必不上传 9 类」之逐闸准出后所余之实体件集；其在册名单基线 ＝ `results\evidence\register\_upload_face_manifest_2026_10_22.md` §4 之 2,415 件（母件式读 2,415／字面式读 2,610）。**

**本件之名单件数 ＝ 2,415 件**（在册基线；本棒逐件现测 **2,415／2,415 盘上在、指纹逐位相符**）。

---

## §1 上传集之口径（准入／准出 · 可判之条件）

### §1-1 域（分母）之可判条件

- 域 ＝ `deposon-repo`（**去仓根 `.tmp`**）∪ `deposon-sub`（全文件）。
- **归档区**（`..\〔归档区〕`）**不入域**（PI 2026-10-22 18:0x 逐字「归档区不上传」）。
- `results\.tmp\` **计入域**（母件 §4.3 之口径：**去仓根** `.tmp`）。
- `GLM` 面：⛔0 入域、⛔0 取指纹（仅计数）。

依据（皆本棒开卷回读＋自测指纹）：`results\doc\document\_achievements_inventory_full_2026_10_23.md`（**443,173／`c9ed5ef032c1`**）§2.3 **L67**；`results\evidence\register\_upload_face_manifest_2026_10_22.md`（**504,831／`b09f23a3fba8`**）§1 **L34–L36**。

### §1-2 准入（可判）

件 f 入 U 须**同时**满足：

- **(A1)** f ∈ 域（§1-1）；
- **(A2)** f 属**必上传类**之一：V-KD／V-VERDICT／V-JUDGE／S-SRC／R-FINAL／T-STRUCT／D-PAPER／D-LETTER／D-README（**9 类**）——母件 §4.3 载「必上传 **8** 类」，而清单件实算之列含 T-STRUCT ＝ **9 类**（**两读并出，本件以 9 类为实算面并明书此差**）；
- **(A3)** f ∉ 在途闸（G0：`mtime ≥ 当日 00:00`；**此闸随时点滚动**，故两测点之数不可直接相减）。

依据：清单件 §2-1 ① **L47**（9 类之列）、② **L48**（G0 在途闸）；`results\work\process\_reorg_dirrule_and_content_criteria_2026_10_22.md`（**70,037／`ccf5483ccb8b`**）§4.1 类别表 **L368–L391**（22 类之「上传远端」列 ＝ 必上传／必不上传／PI 定）。

### §1-3 准出（可判）

件 f **不入** U，若命中任一：

- **(B1)** f 位于**归档区**；
- **(B2)** f 位于**仓根 `.tmp\`** 之下；
- **(B3)** f 属**必不上传 9 类**（类表之「上传远端」列作必不上传者：W-LOG／W-EMPTY／W-BUILD／W-SCRATCH／R-INTERIM／X-SNAP／X-DUPE／X-UNK 及其余同类）；
- **(B4)** f 命中**硬禁止 HF-A…HF-M**（含 HF-M「答卡登记件禁传」）；
- **(B5)** f 命中**加严①**（委托／回函面）**或 加严②**（dataset 隐私面）；
- **(B6)** f 属 **PI 定 5 类**（D-REPORT／D-PLAN／X-REVIEW／E-EVID／M-MEDIA）且 PI 未定其传（**留而不传**，可逆）。

依据：清单件 §1 **L37**、§2-1 ③④⑤⑥ **L49–L52**；类表 **L379–L391**；母件 §4.3 ③；`results\evidence\register\_uploadface_hardening_from_kimi_commission_2026_10_22.md`（**9,610／`1cddb2d7d490`**）§5。

### §1-4 逐闸算式（在册逐环数 · 本棒**不重演**分类器）

分母 → ① 必上传 9 类 ∩ 非在途 **2,901** → ② −HF-A…HF-L **−120** → ③ −HF-M **−234** → ④ −加严① **−36** → ⑤ −加严② **−22** → **U2 ＝ 2,415**（母件式）。
⚠ 本件**⛔0 重演分类器**（重演即新仪器、必有口径漂移风险）⇒ 名单取**在册基线**并逐件**现测**（§3）。

### §1-5 两读并出（母件式 2,415／字面式 2,610）

依清单件 §2-3 **L74** 逐字：「**两读并出：⛔ 0 择一而不言**，两数并报」。本件**两数并报**，不择。

### §1-6 构造面 vs 外推边界

见 §6。

---

## §2 与「三集划分」之关系（阴性断言 · 射程写死 · 双正控）

### §2-1 断言

**在册无以「三集划分」为名之件**；**在册无以「上传集」为名之件**。⇒ 本件所出之名单**系本棒依 PI 裁 134 新立之口径件**，**⛔0 假称在册已有「三集划分件」**。

### §2-2 射程（四根实枚举 · 本棒自测）

| 根 | 枚数（实枚举） | 名含「三集」 | 名含「划分」 | 名含「上传集」 | 名含「集」 |
|:--|--:|--:|--:|--:|--:|
| `deposon-repo`（工作根） | **7,778** | **0** | **0** | **0** | **0** |
| `..\deposon-sub` | **1,275** | **0** | **0** | **0** | **0** |
| `..\〔归档区〕` | **40,242** | **0** | **0** | **0** | **0** |
| `~/.minimax` | **106,399** | **0** | **0** | **0** | **1**（见 §2-3-4） |
| **合计** | **155,694** | **0** | **0** | **0** | **1** |

枚举法：`Get-ChildItem -Recurse -File -Force` 逐件取 `Name` 作 `-like` 匹配；枚举时点 2026-10-25 约 10:47–10:55 UTC+8。
⚠ **并发变动（如实登记）**：仓根件数于 10:47 实测 **7,778**、11:0x 后复测 **7,710**（PI 裁 135 之「整理之刀」正在分批删 `.tmp` 之 `.py`／`.txt`）⇒ 本表之仓根数为**该时点读数**，非恒值。

### §2-3 正控（阴性断言须两项齐备 · 本件两项俱备）

1. **同一性正控（指纹通道为活）**：`tools\exp_harness.py` ＝ **45,590／`ce64b9b97489`**——本棒以 `python -P .tmp\_bcheck.py` **实测**（BYTES／SHA12／SHA256 三行皆符）⇒ 证本棒之枚举＋指纹通道为活。
2. **活性正控（目标词确在时必命中）**：`results\verdict\judgement\_r8_tmp_exclusion_dispute_2026_10_25.md`（**34,757／`2f5f0aff62f5`**）——本棒实测其正文含目标词「**上传集**」**25** 处、「**三集划分**」**5** 处 ⇒ 证本棒之检索通道在目标词确实存在时**必能命中**（故 §2-2 之 0 命中**非因检索失效**）。
3. **阴性对照**：同法施于 `tools\exp_harness.py`（「上传集」**0**、「三集划分」**0**）⇒ 证该计数法**不虚报**。另：底本 v2 `results\_full_inventory_export_v2_2026_10_24.md`（**103,521／`11eb13d33d69`**）实测含「上传集」**2** 处、「三集划分」**0** 处——其「三集划分 ＝ 0」与本棒之**按名** 0 命中**同向而不等同**（一为内容面、一为按名面）。
4. **按名过滤器之活性旁证**：`~/.minimax` 之名含「集」者 **1** 件（`V7-选品优化-dispatch模板集合-2026-09-03.md`·**别域**）⇒ 证按名过滤器在「名含目标字」时**确会命中**（0 命中**非过滤器失效**）。

### §2-4 与「三集」之**判读**（在册有判读 · 但无「三集划分」件）

- PI 逐字（`pi_rulings\_pi_card_answers_register_2026_10_22_v231.md` **7,395／`127894a36c0a`** **L73**，本棒开卷回读）：「**文件数问题大于体积问题，repo 与 sub 区几千份文件不可能不归档全上传远端仓库**」；
- 主代理判读（同件 **L74**）：「② **全量上传不可行**：repo 与 sub 两个区合计数千件，远端仓库不可能全收 ⇒ 须**归档分层**（**必上传集／归档集／本地留存集**三分）」；
- 待办（同件 **L76**）：「**待办**：另立「**三集划分（必上传／归档／本地留）**」件；该件须与 C 类归档索引（`bg_b9f342c6` 产出）并读。」

⇒ **本件与该「三集」之对应**：

| 集 | 本件之覆盖 | 本件之状态 |
|:--|:--|:--|
| **必上传集** | **本件即其名单**（2,415 件之逐件名单） | ✅ 已出（**待 PI 复核生效，生效即锁**） |
| **归档集** | ⛔0 出（须 C 类归档索引 `bg_b9f342c6` 并读；归档区本棒**仅计数与按名·指纹认人**，⛔0 读其正文） | ❌ 未出 |
| **本地留存集** | ⛔0 出（其界之裁须 PI） | ❌ 未出 |

⇒ **明书**：在册**无**名为「三集划分」之件；**本件系新立之「上传集（＝必上传集）」名单件**——口径**承**在册 PI 判读与在册上传面清单（`b09f23a3fba8`），而**名单件之名为本棒新立**。**⛔0 假称在册已有「三集划分件」。**

---

## §3 名单

### §3-1 列义

| 列 | 义 |
|:--|:--|
| 序 | 在册清单 §4 之序号（本棒逐行沿用） |
| 区 | `repo` ＝ `deposon-repo`｜`sub` ＝ `..\deposon-sub`；**区根相对**之现相对路径 |
| 现相对路径 | 区根相对路径（**本棒现测**其盘上现址仍为此） |
| BYTES | **本棒现测**（实际字节数） |
| SHA-12 | **本棒现测**（SHA-256 前 12 位小写） |
| 面/子类 | 在册母件 22 类之落位（在册值，本棒沿用） |
| 远端目标路径 | 在册母件 §3.5 改写规则之目标路径（在册值，本棒沿用） |
| 来源面 | **`L`** ＝ 本地版（唯一源；本棒现测在盘且指纹符）｜**`R`** ＝ 远端轨（`_remote_pullback_2026_10_17` 之本地留痕）｜**`O`** ＝ 其他 |

### §3-2 逐件清单（**2,415 件** · 本棒逐件现测）

> 📌 **本表全体 2,415 件之现测态 ＝ 在盘 ＋ SHA-12 与在册逐位相符（2,415／2,415）**；**来源面 ＝ `L` 2,415／`R` 0／`O` 0**（与远端轨之逐字节命中 ＝ 0，见 §3-4）。

| 序 | 区 | 现相对路径 | BYTES | SHA-12 | 面/子类 | 远端目标路径 | 来源面 |
|--:|:--|:--|--:|:--|:--|:--|:-:|
| 1 | repo | .mavis/scripts/cleanup511/audit_manifest.py | 2091 | `02e196e2c667` | source/tool | source/tool/audit_manifest.py | L |
| 2 | repo | .mavis/scripts/cleanup511/audit_manifest2.py | 3453 | `8cebb1cd14ae` | source/tool | source/tool/audit_manifest2.py | L |
| 3 | repo | .mavis/scripts/cleanup511/audit_manifest3.py | 2119 | `588c821490ce` | source/tool | source/tool/audit_manifest3.py | L |
| 4 | repo | .mavis/scripts/cleanup511/batch_exec.py | 5963 | `26c99e9a0c42` | source/tool | source/tool/batch_exec.py | L |
| 5 | repo | .mavis/scripts/cleanup511/debug_i.py | 1466 | `a73a6885b4ba` | source/tool | source/tool/debug_i.py | L |
| 6 | repo | .mavis/scripts/cleanup511/exec_list.json | 85898 | `570b1509e16d` | readout/final | readout/final/exec_list.json | L |
| 7 | repo | .mavis/scripts/cleanup511/exec_report.json | 251947 | `eaddc07479ab` | readout/final | readout/final/exec_report.json | L |
| 8 | repo | .mavis/scripts/cleanup511/final_sweep.py | 3502 | `c271feb2b853` | source/tool | source/tool/final_sweep.py | L |
| 9 | repo | .mavis/scripts/cleanup511/finalize.py | 3570 | `224bda85007b` | source/tool | source/tool/finalize.py | L |
| 10 | repo | .mavis/scripts/cleanup511/make_register.py | 13920 | `45416c09e419` | source/tool | source/tool/make_register.py | L |
| 11 | repo | .mavis/scripts/cleanup511/reconcile_probe.py | 1934 | `32bb7912b613` | source/tool | source/tool/reconcile_probe.py | L |
| 12 | repo | .mavis/scripts/cleanup511/recycle_exec.py | 6489 | `c93fc1c27fea` | source/tool | source/tool/recycle_exec.py | L |
| 13 | repo | .mavis/scripts/cleanup511/spot_check.py | 2238 | `10ced278e75f` | source/tool | source/tool/spot_check.py | L |
| 14 | repo | .mavis/scripts/cleanup511/survey511.py | 10678 | `5e9672a15d4e` | source/tool | source/tool/survey511.py | L |
| 15 | repo | .mavis/scripts/cleanup511/verify_dirs.py | 1747 | `84fd486f0dcb` | source/tool | source/tool/verify_dirs.py | L |
| 16 | repo | .mavis/scripts/kt_b1/fix_safe_float.py | 966 | `4420543e60a4` | source/tool | source/tool/fix_safe_float.py | L |
| 17 | repo | .trae/scripts/_arxiv_renumber.py | 16531 | `f488ad141ef9` | source/tool | source/tool/_arxiv_renumber.py | L |
| 18 | repo | .trae/scripts/_verify_tex.py | 18250 | `3b977bb8a715` | source/tool | source/tool/_verify_tex.py | L |
| 19 | repo | .vscode/settings.json | 41 | `4ad2e86b6169` | readout/final | readout/final/settings.json | L |
| 20 | repo | README.md | 7279 | `a80b3db006a5` | doc/paper | doc/paper/README.md | L |
| 21 | repo | README_V4_2026_09_29.md | 58635 | `a6f88fb6e325` | verdict/kd | verdict/kd/README_V4_2026_09_29.md | L |
| 22 | repo | _docwriter_sha_index_scratch.py | 1369 | `5d14277b148f` | source/tool | source/tool/_docwriter_sha_index_scratch.py | L |
| 23 | repo | _field_sources/ritt_remeasure_measurement_2026_10_17.json | 325531 | `29bb4c4a8bca` | readout/final | readout/final/ritt_remeasure_measurement_2026_10_17.json | L |
| 24 | repo | _kd_flip_anchor_scan.py | 2575 | `9560a4fb4121` | source/tool | source/tool/_kd_flip_anchor_scan.py | L |
| 25 | repo | _kd_flip_kdcensus.py | 3541 | `ff11e0c650d8` | source/tool | source/tool/_kd_flip_kdcensus.py | L |
| 26 | repo | _kd_flip_verify.py | 1827 | `5bbdc66e0855` | source/tool | source/tool/_kd_flip_verify.py | L |
| 27 | repo | _kd_flip_write.py | 38829 | `e3063681d015` | source/tool | source/tool/_kd_flip_write.py | L |
| 28 | repo | _tools_docwriter_backlog_scan.py | 2743 | `f0686ae7c0d3` | source/tool | source/tool/_tools_docwriter_backlog_scan.py | L |
| 29 | repo | _tools_docwriter_candidate_items.py | 4281 | `ec8ad1cc648e` | source/tool | source/tool/_tools_docwriter_candidate_items.py | L |
| 30 | repo | _tools_docwriter_counts.py | 1286 | `0e2ff2225e94` | source/tool | source/tool/_tools_docwriter_counts.py | L |
| 31 | repo | _tools_docwriter_heading_extract.py | 2267 | `86c90cb722a6` | source/tool | source/tool/_tools_docwriter_heading_extract.py | L |
| 32 | repo | _tools_docwriter_heading_extract.txt | 41865 | `db2b1edc2906` | verdict/pi | verdict/pi/_tools_docwriter_heading_extract.txt | L |
| 33 | repo | _tools_docwriter_measurements.py | 8141 | `83d25b4b1fc7` | source/tool | source/tool/_tools_docwriter_measurements.py | L |
| 34 | repo | _tools_docwriter_measurements.txt | 23974 | `e9cb0aaf216a` | verdict/pi | verdict/pi/_tools_docwriter_measurements.txt | L |
| 35 | repo | _tools_docwriter_sha_scan.py | 981 | `d59b500db14f` | source/tool | source/tool/_tools_docwriter_sha_scan.py | L |
| 36 | repo | _tools_docwriter_state_dist.py | 2707 | `b29cc723917b` | source/tool | source/tool/_tools_docwriter_state_dist.py | L |
| 37 | repo | _tools_docwriter_verify.py | 4540 | `655debda5e00` | source/tool | source/tool/_tools_docwriter_verify.py | L |
| 38 | repo | _tools_v171_fp.py | 2213 | `8fa0047c4fdd` | source/tool | source/tool/_tools_v171_fp.py | L |
| 39 | repo | _tools_v171_fp_out.json | 1423 | `9bd61909a003` | readout/final | readout/final/_tools_v171_fp_out.json | L |
| 40 | repo | _tools_v171_idx.py | 850 | `a6183d07f3c9` | source/tool | source/tool/_tools_v171_idx.py | L |
| 41 | repo | _tools_v171_ph.py | 2047 | `50ac25cbd192` | source/tool | source/tool/_tools_v171_ph.py | L |
| 42 | repo | _tools_v171_probe.py | 5205 | `8ab103d55b1f` | source/tool | source/tool/_tools_v171_probe.py | L |
| 43 | repo | _tools_v171_probe_out.json | 20957 | `277e588641e3` | readout/final | readout/final/_tools_v171_probe_out.json | L |
| 44 | repo | _tools_v171_reg_lines.txt | 3139 | `529d4960b489` | verdict/pi | verdict/pi/_tools_v171_reg_lines.txt | L |
| 45 | repo | _tools_v171_regdump.py | 618 | `06ff6df76e89` | source/tool | source/tool/_tools_v171_regdump.py | L |
| 46 | repo | _tools_v171_sum.txt | 2252 | `f32c25e89ec5` | verdict/pi | verdict/pi/_tools_v171_sum.txt | L |
| 47 | repo | _tools_v171_v170_tail.txt | 5144 | `f1b8864c7517` | verdict/pi | verdict/pi/_tools_v171_v170_tail.txt | L |
| 48 | repo | _tools_v176_bj.py | 1095 | `6c99818dfd3f` | source/tool | source/tool/_tools_v176_bj.py | L |
| 49 | repo | _tools_v176_fp.py | 1546 | `d46ef3730d24` | source/tool | source/tool/_tools_v176_fp.py | L |
| 50 | repo | _tools_v176_fp_out.json | 3562 | `2c9e2da19fa5` | readout/final | readout/final/_tools_v176_fp_out.json | L |
| 51 | repo | _tools_v176_measure.py | 5882 | `616a6cbf6986` | source/tool | source/tool/_tools_v176_measure.py | L |
| 52 | repo | _tools_v176_measure_out.txt | 7873 | `5b4740761940` | verdict/pi | verdict/pi/_tools_v176_measure_out.txt | L |
| 53 | repo | _tools_v176_open1.py | 1027 | `5e5384b1dbc3` | source/tool | source/tool/_tools_v176_open1.py | L |
| 54 | repo | _tools_v176_open1.txt | 35617 | `2c29186acbc2` | verdict/pi | verdict/pi/_tools_v176_open1.txt | L |
| 55 | repo | _tools_v176_open2.py | 2316 | `dc3e2483d245` | source/tool | source/tool/_tools_v176_open2.py | L |
| 56 | repo | _tools_v176_open2.txt | 91201 | `3352793f4141` | verdict/kd | verdict/kd/_tools_v176_open2.txt | L |
| 57 | repo | _tools_v176_panel2.py | 3303 | `d3924cac1fb9` | source/tool | source/tool/_tools_v176_panel2.py | L |
| 58 | repo | _tools_v176_panel2.txt | 4551 | `21e2927581ba` | readout/final | readout/final/_tools_v176_panel2.txt | L |
| 59 | repo | _tools_v176_panel3.py | 2468 | `f6e8bbdc7a97` | source/tool | source/tool/_tools_v176_panel3.py | L |
| 60 | repo | _tools_v176_panel3.txt | 18203 | `311fdb07c866` | verdict/kd | verdict/kd/_tools_v176_panel3.txt | L |
| 61 | repo | _tools_v176_panel4.py | 2104 | `724d2bbbcba4` | source/tool | source/tool/_tools_v176_panel4.py | L |
| 62 | repo | _tools_v176_panel4.txt | 47464 | `b30d6d8a4f76` | verdict/kd | verdict/kd/_tools_v176_panel4.txt | L |
| 63 | repo | _tools_v176_secorder.py | 613 | `4c817e6d5d6f` | source/tool | source/tool/_tools_v176_secorder.py | L |
| 64 | repo | _tools_v176_secorder.txt | 26369 | `a2a6d326f2a6` | verdict/pi | verdict/pi/_tools_v176_secorder.txt | L |
| 65 | repo | _v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md | 26633 | `739245682d40` | verdict/pi | verdict/pi/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md | L |
| 66 | repo | _v5_gt_exec_2026_09_29.py | 75689 | `eef7b446cc0e` | source/tool | source/tool/_v5_gt_exec_2026_09_29.py | L |
| 67 | repo | attacks/__init__.py | 183 | `d11e085d9ecc` | source/tool | source/tool/__init__.py | L |
| 68 | repo | attacks/a1_delete_anchor.py | 4693 | `78ac391d16fc` | source/tool | source/tool/a1_delete_anchor.py | L |
| 69 | repo | attacks/a2_reshuffle_manifest.py | 3792 | `3d54b277620e` | source/tool | source/tool/a2_reshuffle_manifest.py | L |
| 70 | repo | attacks/a3_rewrite_runs.py | 4254 | `f02b3eee8d6e` | source/tool | source/tool/a3_rewrite_runs.py | L |
| 71 | repo | corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json | 19685 | `268ab1239a8a` | readout/final | readout/final/three_way_glm_slot_blind_test_2026_09_16.json | L |
| 72 | repo | corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json | 13150 | `39732a92b5c9` | readout/final | readout/final/glm_artifact_v_2026_09_16.json | L |
| 73 | repo | corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json | 10978 | `fee04170aa73` | readout/final | readout/final/coze_artifact_v_2026_09_16.json | L |
| 74 | repo | corpus/v20/by_model/minimax/artifact_v_2026_09_16.json | 25347 | `9e1ccbdceacc` | readout/final | readout/final/artifact_v_2026_09_16.json | L |
| 75 | repo | corpus/v20/index_v3_2026_09_29.json | 24421 | `3ba2449cf986` | readout/final | readout/final/index_v3_2026_09_29.json | L |
| 76 | repo | corpus/v20/index_v3_2026_10_09.json | 24837 | `74b27393574f` | readout/final | readout/final/index_v3_2026_10_09.json | L |
| 77 | repo | corpus/v20_caption_surface/_inspect_captions.py | 591 | `dfb02ade1474` | source/tool | source/tool/_inspect_captions.py | L |
| 78 | repo | corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py | 18596 | `d2cd7acb29a1` | source/tool | source/tool/_p_d_b3_merkle_22caption_runner_2026_09_16.py | L |
| 79 | repo | corpus/v20_caption_surface/caption_distance_mat_22.json | 8552 | `1c4fff004cc4` | readout/final | readout/final/caption_distance_mat_22.json | L |
| 80 | repo | corpus/v20_caption_surface/caption_features_22.json | 18362 | `727a253566dd` | readout/final | readout/final/caption_features_22.json | L |
| 81 | repo | corpus/v20_caption_surface/caption_stats_22.json | 632 | `da34f54d4f5b` | readout/final | readout/final/caption_stats_22.json | L |
| 82 | repo | corpus/v20_caption_surface/manifest.json | 1477 | `4fdda6480bb5` | readout/final | readout/final/manifest.json | L |
| 83 | repo | deposon_agents.py | 104622 | `5496954b0ad5` | source/tool | source/tool/deposon_agents.py | L |
| 84 | repo | deposon_agents_v1_3.py | 1827 | `715026b48678` | source/tool | source/tool/deposon_agents_v1_3.py | L |
| 85 | repo | deposon_agents_v1_4.py | 1726 | `59f0ce83e06d` | source/tool | source/tool/deposon_agents_v1_4.py | L |
| 86 | repo | deposon_diffusion.py | 19171 | `fe4d668eb1da` | source/tool | source/tool/deposon_diffusion.py | L |
| 87 | repo | deposon_fast.py | 4581 | `7a2dcbadac73` | source/tool | source/tool/deposon_fast.py | L |
| 88 | repo | deposon_g2_modes.py | 6316 | `6a175a264b46` | source/tool | source/tool/deposon_g2_modes.py | L |
| 89 | repo | deposon_photonics.py | 10402 | `c7e78ad9f030` | source/tool | source/tool/deposon_photonics.py | L |
| 90 | repo | deposon_protocol.py | 2845 | `ca756668ce2e` | source/tool | source/tool/deposon_protocol.py | L |
| 91 | repo | deposon_team/plugins/_dfr_s1_2026_10_12.py | 5327 | `b003e57c14f7` | source/tool | source/tool/_dfr_s1_2026_10_12.py | L |
| 92 | repo | deposon_team/plugins/_dfr_s2_2026_10_12.py | 4499 | `745c1a86c868` | source/tool | source/tool/_dfr_s2_2026_10_12.py | L |
| 93 | repo | deposon_team/plugins/_ofc_s1_2026_10_12.py | 5667 | `bb7b9faa547a` | source/tool | source/tool/_ofc_s1_2026_10_12.py | L |
| 94 | repo | deposon_team/plugins/_ofc_s1b_2026_10_12.py | 4684 | `0bf02827c1d9` | source/tool | source/tool/_ofc_s1b_2026_10_12.py | L |
| 95 | repo | deposon_team/plugins/_ofc_s2_2026_10_12.py | 3960 | `0ac81224ac7f` | source/tool | source/tool/_ofc_s2_2026_10_12.py | L |
| 96 | repo | deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py | 33994 | `341b6726ac4e` | source/tool | source/tool/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py | L |
| 97 | repo | deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py | 35321 | `cd43c41716f0` | source/tool | source/tool/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py | L |
| 98 | repo | deposon_team/plugins/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py | 31457 | `041525fd05a2` | source/tool | source/tool/_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py | L |
| 99 | repo | deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py | 20322 | `de16bc002198` | source/tool | source/tool/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py | L |
| 100 | repo | deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py | 21826 | `7c095c54fb99` | source/tool | source/tool/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py | L |
| 101 | repo | deposon_team/plugins/_pg_v01_compute.py | 20923 | `d511c545f88e` | source/tool | source/tool/_pg_v01_compute.py | L |
| 102 | repo | deposon_team/plugins/_tdf_s1_2026_10_12.py | 5856 | `5f9ab0ad7bab` | source/tool | source/tool/_tdf_s1_2026_10_12.py | L |
| 103 | repo | deposon_team/plugins/_tdf_s1b_2026_10_12.py | 8064 | `bebba19790c0` | source/tool | source/tool/_tdf_s1b_2026_10_12.py | L |
| 104 | repo | deposon_team/plugins/_tdf_s1c_2026_10_12.py | 7485 | `d8bd9c41194a` | source/tool | source/tool/_tdf_s1c_2026_10_12.py | L |
| 105 | repo | deposon_team/plugins/_tdf_s2_apply_2026_10_12.py | 10899 | `4bd6d16e20d7` | source/tool | source/tool/_tdf_s2_apply_2026_10_12.py | L |
| 106 | repo | deposon_team/plugins/_tdf_s3_jumps_2026_10_12.py | 676 | `16f7e10ac78f` | source/tool | source/tool/_tdf_s3_jumps_2026_10_12.py | L |
| 107 | repo | deposon_team/plugins/_tdf_s3b_2026_10_12.py | 1229 | `ccec66bb426e` | source/tool | source/tool/_tdf_s3b_2026_10_12.py | L |
| 108 | repo | deposon_team/plugins/_tdf_s4_final_2026_10_12.py | 2695 | `1df9a5d22e42` | source/tool | source/tool/_tdf_s4_final_2026_10_12.py | L |
| 109 | repo | deposon_team/plugins/_v3_construct_diag_2026_09_23.py | 22490 | `ce10a3dbcb2b` | source/tool | source/tool/_v3_construct_diag_2026_09_23.py | L |
| 110 | repo | deposon_team/plugins/_v3_review_r1_inventory_2026_09_23.py | 5526 | `7b97ef02c52e` | source/tool | source/tool/_v3_review_r1_inventory_2026_09_23.py | L |
| 111 | repo | deposon_team/plugins/_v3_review_r1b_2026_09_23.py | 1795 | `b5e77e114d88` | source/tool | source/tool/_v3_review_r1b_2026_09_23.py | L |
| 112 | repo | deposon_team/plugins/_v3_review_r1c_2026_09_23.py | 2919 | `fdfeb03e8d6f` | source/tool | source/tool/_v3_review_r1c_2026_09_23.py | L |
| 113 | repo | deposon_team/plugins/_v3_review_r1d_2026_09_23.py | 1712 | `4adbd9b5eab5` | source/tool | source/tool/_v3_review_r1d_2026_09_23.py | L |
| 114 | repo | deposon_team/plugins/_v3_review_r2_verify_2026_09_23.py | 4528 | `aee06c009ed1` | source/tool | source/tool/_v3_review_r2_verify_2026_09_23.py | L |
| 115 | repo | deposon_team/plugins/_v3_review_r2b_2026_09_23.py | 3189 | `9d6343bd9755` | source/tool | source/tool/_v3_review_r2b_2026_09_23.py | L |
| 116 | repo | deposon_team/plugins/_v3_review_r2c_2026_09_23.py | 4400 | `1c30cda5aad6` | source/tool | source/tool/_v3_review_r2c_2026_09_23.py | L |
| 117 | repo | deposon_team/plugins/_v3_review_r3_sha_2026_09_23.py | 1881 | `d3b45b64c0da` | source/tool | source/tool/_v3_review_r3_sha_2026_09_23.py | L |
| 118 | repo | deposon_team/plugins/_v3_review_r4_fixscan_2026_09_23.py | 3896 | `917b18eb9a5f` | source/tool | source/tool/_v3_review_r4_fixscan_2026_09_23.py | L |
| 119 | repo | deposon_team/plugins/_v3_review_r5_anchor_probe_2026_09_23.py | 2653 | `7ebe0f65a64a` | source/tool | source/tool/_v3_review_r5_anchor_probe_2026_09_23.py | L |
| 120 | repo | deposon_team/plugins/_v3_review_r6_final_sha_2026_09_23.py | 2135 | `8af3f4460144` | source/tool | source/tool/_v3_review_r6_final_sha_2026_09_23.py | L |
| 121 | repo | deposon_team/plugins/_v3_review_r7_fix_e15_2026_09_23.py | 2951 | `40d66379ef17` | source/tool | source/tool/_v3_review_r7_fix_e15_2026_09_23.py | L |
| 122 | repo | deposon_team/plugins/_v3_review_r8_precise_scan_2026_09_23.py | 5241 | `2ff60f715def` | source/tool | source/tool/_v3_review_r8_precise_scan_2026_09_23.py | L |
| 123 | repo | deposon_team/plugins/_v3_review_r9_final_state_2026_09_23.py | 2117 | `fcf5baf4dd7f` | source/tool | source/tool/_v3_review_r9_final_state_2026_09_23.py | L |
| 124 | repo | deposon_team/plugins/_v3n_cpath_live_2026_09_27.py | 19823 | `5248ba7ac21c` | source/tool | source/tool/_v3n_cpath_live_2026_09_27.py | L |
| 125 | repo | deposon_team/plugins/_v3n_cpath_live_r1_2026_09_27.py | 28187 | `321d39c7df41` | source/tool | source/tool/_v3n_cpath_live_r1_2026_09_27.py | L |
| 126 | repo | deposon_team/plugins/_v3n_cpath_live_rerun_2026_10_01.py | 22133 | `7d8d26174ce9` | source/tool | source/tool/_v3n_cpath_live_rerun_2026_10_01.py | L |
| 127 | repo | deposon_team/plugins/_v3n_ktb1_distortion_bound_2026_09_27.py | 13055 | `5572ef4055a5` | source/tool | source/tool/_v3n_ktb1_distortion_bound_2026_09_27.py | L |
| 128 | repo | deposon_team/plugins/_v3n_pg_boss_live_2026_09_27.py | 14223 | `b6040d34f0ac` | source/tool | source/tool/_v3n_pg_boss_live_2026_09_27.py | L |
| 129 | repo | deposon_team/plugins/_v3r1p1_21_ktb1_distortion_2026_09_27.py | 30672 | `f7b61f041c0b` | source/tool | source/tool/_v3r1p1_21_ktb1_distortion_2026_09_27.py | L |
| 130 | repo | deposon_team/plugins/_v3r1p1_35_gt2b_bankseed_2026_09_27.py | 26734 | `62353279cd0c` | source/tool | source/tool/_v3r1p1_35_gt2b_bankseed_2026_09_27.py | L |
| 131 | repo | deposon_team/plugins/_v3x_frozen_schema_v1.json | 12919 | `9e99dcc4d920` | readout/final | readout/final/_v3x_frozen_schema_v1.json | L |
| 132 | repo | deposon_team/plugins/_v4_contrast_nondegenerate_2026_09_23.py | 42876 | `a0bfc7df887f` | source/tool | source/tool/_v4_contrast_nondegenerate_2026_09_23.py | L |
| 133 | repo | deposon_team/plugins/_v4_wide_s1_inventory_2026_09_27.py | 1669 | `145ae518f5f0` | source/tool | source/tool/_v4_wide_s1_inventory_2026_09_27.py | L |
| 134 | repo | deposon_team/plugins/_v4_wide_s5_prescan_2026_09_27.py | 2839 | `724964301582` | source/tool | source/tool/_v4_wide_s5_prescan_2026_09_27.py | L |
| 135 | repo | deposon_team/plugins/_v4_wt_apply_b4_2026_09_27.py | 6113 | `fd0a08029841` | source/tool | source/tool/_v4_wt_apply_b4_2026_09_27.py | L |
| 136 | repo | deposon_team/plugins/_v4_wt_s0_verify_2026_09_27.py | 8462 | `4dcb81343577` | source/tool | source/tool/_v4_wt_s0_verify_2026_09_27.py | L |
| 137 | repo | deposon_team/plugins/_v4_wt_s2_b1diff_2026_09_27.py | 2015 | `b61cb447f306` | source/tool | source/tool/_v4_wt_s2_b1diff_2026_09_27.py | L |
| 138 | repo | deposon_team/plugins/_v4_wt_s2_b1recheck_2026_09_27.py | 5650 | `e643ac7f9718` | source/tool | source/tool/_v4_wt_s2_b1recheck_2026_09_27.py | L |
| 139 | repo | deposon_team/plugins/_v4_wt_s3_b2probe_2026_09_27.py | 6089 | `a5db027adac5` | source/tool | source/tool/_v4_wt_s3_b2probe_2026_09_27.py | L |
| 140 | repo | deposon_team/plugins/_v4_wt_s3b_b2confirm_2026_09_27.py | 3604 | `7aaf6f21d459` | source/tool | source/tool/_v4_wt_s3b_b2confirm_2026_09_27.py | L |
| 141 | repo | deposon_team/plugins/_v4_wt_s4_b4verify_2026_09_27.py | 2595 | `5e1ec533de1f` | source/tool | source/tool/_v4_wt_s4_b4verify_2026_09_27.py | L |
| 142 | repo | deposon_team/plugins/_v4_wt_s4b_b4recompute_2026_09_27.py | 4174 | `edcdfda20f91` | source/tool | source/tool/_v4_wt_s4b_b4recompute_2026_09_27.py | L |
| 143 | repo | deposon_team/plugins/_v4_wt_s4c_regonly_2026_09_27.py | 3900 | `20f265761280` | source/tool | source/tool/_v4_wt_s4c_regonly_2026_09_27.py | L |
| 144 | repo | deposon_team/plugins/_v4_wt_s6_final_2026_09_27.py | 3435 | `653077d03468` | source/tool | source/tool/_v4_wt_s6_final_2026_09_27.py | L |
| 145 | repo | deposon_team/plugins/_v5_gt8_lowarm_2026_09_29.py | 57033 | `9b21988afff7` | source/tool | source/tool/_v5_gt8_lowarm_2026_09_29.py | L |
| 146 | repo | deposon_team/plugins/_v5_gt8_lowarm_setA_2026_09_29.py | 43224 | `f72f062f6b67` | source/tool | source/tool/_v5_gt8_lowarm_setA_2026_09_29.py | L |
| 147 | repo | deposon_team/plugins/_v5_gt8_lowarm_seta_verify_2026_09_29.py | 15553 | `bed2d444c196` | source/tool | source/tool/_v5_gt8_lowarm_seta_verify_2026_09_29.py | L |
| 148 | repo | deposon_team/plugins/_v5_item21_strategyqa_realias_2026_09_29.py | 25482 | `aaaae1f02815` | source/tool | source/tool/_v5_item21_strategyqa_realias_2026_09_29.py | L |
| 149 | repo | deposon_team/plugins/_v5_item35_v2_matrix_2026_09_29.py | 44777 | `ef73f9b90afc` | source/tool | source/tool/_v5_item35_v2_matrix_2026_09_29.py | L |
| 150 | repo | deposon_team/plugins/_v5_item35_v3_collinear_2026_09_29.py | 63376 | `7115928822a1` | source/tool | source/tool/_v5_item35_v3_collinear_2026_09_29.py | L |
| 151 | repo | deposon_team/plugins/_v5_pp1_pattern_fix_2026_09_29.py | 22544 | `e3cf9d552f30` | source/tool | source/tool/_v5_pp1_pattern_fix_2026_09_29.py | L |
| 152 | repo | deposon_team/plugins/_v5_wa_s2_2026_09_30.py | 5812 | `88cd82e65627` | source/tool | source/tool/_v5_wa_s2_2026_09_30.py | L |
| 153 | repo | deposon_team/plugins/_v5_wa_s4_2026_09_30.py | 2063 | `2e7743dd8139` | source/tool | source/tool/_v5_wa_s4_2026_09_30.py | L |
| 154 | repo | deposon_team/plugins/_v5r_s40_rerun_executor_fix_2026_09_29.py | 17665 | `a4ae5d5f19c8` | source/tool | source/tool/_v5r_s40_rerun_executor_fix_2026_09_29.py | L |
| 155 | repo | deposon_team/plugins/_verify_15frozen.py | 3905 | `efae9274962e` | source/tool | source/tool/_verify_15frozen.py | L |
| 156 | repo | deposon_team/plugins/_verify_15frozen_v1.py | 2094 | `60523e406055` | source/tool | source/tool/_verify_15frozen_v1.py | L |
| 157 | repo | deposon_team/plugins/_verify_batch5_2026_09_18.py | 4238 | `bc6cbf27a338` | source/tool | source/tool/_verify_batch5_2026_09_18.py | L |
| 158 | repo | deposon_team/plugins/_verify_pg_v0.py | 3978 | `cdd3415ad993` | source/tool | source/tool/_verify_pg_v0.py | L |
| 159 | repo | deposon_team/plugins/_verify_pg_v0_v1.py | 2521 | `67088ae1a860` | source/tool | source/tool/_verify_pg_v0_v1.py | L |
| 160 | repo | deposon_team/plugins/boss_pa_1_rbr_rm.py | 17743 | `5cc594147e00` | source/tool | source/tool/boss_pa_1_rbr_rm.py | L |
| 161 | repo | deposon_team/plugins/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py | 45777 | `06016f90fd3a` | source/tool | source/tool/boss_pa_1_rbr_rm_v3df_ab_alpha_2026_10_09.py | L |
| 162 | repo | deposon_team/plugins/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.py | 47580 | `3524e454d8ed` | source/tool | source/tool/boss_pa_1_rbr_rm_v3df_ab_beta_2026_10_09.py | L |
| 163 | repo | deposon_team/plugins/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py | 61102 | `7761f2c339e6` | source/tool | source/tool/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py | L |
| 164 | repo | deposon_team/plugins/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.py | 91135 | `77724bce0c06` | source/tool | source/tool/boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.py | L |
| 165 | repo | deposon_team/plugins/boss_pa_2_potential_game.py | 10410 | `33dfb4338c53` | source/tool | source/tool/boss_pa_2_potential_game.py | L |
| 166 | repo | deposon_team/plugins/boss_pa_3_replicator_dynamics.py | 12900 | `a2bd9dd24c25` | source/tool | source/tool/boss_pa_3_replicator_dynamics.py | L |
| 167 | repo | deposon_team/plugins/boss_pc_1_2d_ising_universality.py | 7547 | `bfc319808447` | source/tool | source/tool/boss_pc_1_2d_ising_universality.py | L |
| 168 | repo | deposon_team/plugins/boss_pc_2_transverse_field_ising.py | 7053 | `210105a7f29a` | source/tool | source/tool/boss_pc_2_transverse_field_ising.py | L |
| 169 | repo | deposon_team/plugins/boss_pc_3_reservoir_computing.py | 7373 | `021ea39b7193` | source/tool | source/tool/boss_pc_3_reservoir_computing.py | L |
| 170 | repo | deposon_team/plugins/boss_pg_1_riemannian_degenerate.py | 5996 | `97fede6c8a4e` | source/tool | source/tool/boss_pg_1_riemannian_degenerate.py | L |
| 171 | repo | deposon_team/plugins/boss_pg_2_hyperbolic_classification_collapse.py | 5285 | `f006d4caca94` | source/tool | source/tool/boss_pg_2_hyperbolic_classification_collapse.py | L |
| 172 | repo | deposon_team/plugins/boss_pg_3_geodesic_violation.py | 5517 | `09f37c01a258` | source/tool | source/tool/boss_pg_3_geodesic_violation.py | L |
| 173 | repo | deposon_team/plugins/github_dir_structure_2026_09_18.md | 11675 | `0fd07ad38282` | doc/letter | doc/letter/github_dir_structure_2026_09_18.md | L |
| 174 | repo | deposon_team/plugins/github_upload_2026_09_18.sh | 6030 | `52bc19845b2b` | source/tool | source/tool/github_upload_2026_09_18.sh | L |
| 175 | repo | deposon_team/plugins/skill_a_p_a_60cells.py | 9078 | `b1463bb24403` | source/tool | source/tool/skill_a_p_a_60cells.py | L |
| 176 | repo | deposon_team/plugins/skill_b_p_c_alpha_beta.py | 8699 | `e5a299f69a22` | source/tool | source/tool/skill_b_p_c_alpha_beta.py | L |
| 177 | repo | deposon_team/plugins/skill_c_p_e_3modality.py | 8915 | `e19e76c5da7e` | source/tool | source/tool/skill_c_p_e_3modality.py | L |
| 178 | repo | deposon_team/plugins/skill_d_p_f_observer.py | 15927 | `3e369a1f6171` | source/tool | source/tool/skill_d_p_f_observer.py | L |
| 179 | repo | docs/GT_RECONSTRUCTION.md | 13424 | `cff15d000d47` | readout/final | readout/final/GT_RECONSTRUCTION.md | L |
| 180 | repo | docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md | 15457 | `423c84de20d5` | doc/readme | doc/readme/P_B_DISTORTION_BOUND_V0_SPEC.md | L |
| 181 | repo | fingerprint_v0.py | 10950 | `c0c38007c4e8` | source/tool | source/tool/fingerprint_v0.py | L |
| 182 | repo | gt_common.py | 3601 | `425b4b2f1c01` | source/tool | source/tool/gt_common.py | L |
| 183 | repo | llm_fetch.py | 8433 | `fda22714de2d` | source/tool | source/tool/llm_fetch.py | L |
| 184 | repo | llm_prior.py | 7466 | `7fba7d72a679` | source/tool | source/tool/llm_prior.py | L |
| 185 | repo | mindmap_corpus_v20.py | 25791 | `e77e7f3455e0` | source/tool | source/tool/mindmap_corpus_v20.py | L |
| 186 | repo | paper/deposon_paper_final_cn.md | 53838 | `c5f6a23f4408` | doc/paper | doc/paper/deposon_paper_final_cn.md | L |
| 187 | repo | paper/deposon_paper_final_en.md | 68164 | `2ec20b96e941` | doc/paper | doc/paper/deposon_paper_final_en.md | L |
| 188 | repo | results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_build_2026_10_10.py | 29412 | `e5acb3c0bca2` | source/tool | source/tool/_exp06_1009fix_build_2026_10_10.py | L |
| 189 | repo | results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref2_2026_10_10.py | 1505 | `3ff21d556306` | source/tool | source/tool/_exp06_1009fix_lnref2_2026_10_10.py | L |
| 190 | repo | results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_lnref_2026_10_10.py | 1508 | `9c7096147878` | source/tool | source/tool/_exp06_1009fix_lnref_2026_10_10.py | L |
| 191 | repo | results/_archive_2026-10-12/exec_artifacts/_exp06_1009fix_verify_2026_10_10.py | 7817 | `47fdf9673acc` | source/tool | source/tool/_exp06_1009fix_verify_2026_10_10.py | L |
| 192 | repo | results/_archive_2026-10-12/exec_artifacts/_exp06_fixcopy_verify_probe_2026_10_10.py | 3598 | `680b6893f9f7` | source/tool | source/tool/_exp06_fixcopy_verify_probe_2026_10_10.py | L |
| 193 | repo | results/_archive_2026-10-12/exec_artifacts/c5_guard_minmaxstd_2026_10_01.py | 15009 | `d74ff478993c` | source/tool | source/tool/c5_guard_minmaxstd_2026_10_01.py | L |
| 194 | repo | results/_archive_2026-10-12/exec_artifacts/e4_axis2_crosscheck_2026_10_10.py | 3607 | `fbf93a534b99` | source/tool | source/tool/e4_axis2_crosscheck_2026_10_10.py | L |
| 195 | repo | results/_archive_2026-10-12/exec_artifacts/e4_axis2_denominator_recheck_2026_10_10.py | 3833 | `5944efd3b68e` | source/tool | source/tool/e4_axis2_denominator_recheck_2026_10_10.py | L |
| 196 | repo | results/_archive_2026-10-12/exec_artifacts/e4_axis2_final_validation_2026_10_10.py | 6489 | `8d2211f8ac91` | source/tool | source/tool/e4_axis2_final_validation_2026_10_10.py | L |
| 197 | repo | results/_archive_2026-10-12/exec_artifacts/e4_axis2_hit_unchanged_probe_2026_10_10.py | 2629 | `fc5d6bde78ad` | source/tool | source/tool/e4_axis2_hit_unchanged_probe_2026_10_10.py | L |
| 198 | repo | results/_archive_2026-10-12/exec_artifacts/e4_axis2_v11_displacement_run_2026_10_10.py | 10617 | `a950ae064fde` | source/tool | source/tool/e4_axis2_v11_displacement_run_2026_10_10.py | L |
| 199 | repo | results/_archive_2026-10-12/exec_artifacts/exp06_independent_json_gen_2026_10_10.py | 21560 | `5ce8f89c9396` | source/tool | source/tool/exp06_independent_json_gen_2026_10_10.py | L |
| 200 | repo | results/_archive_2026-10-12/exec_artifacts/exp06_supplement_probe_2026_10_10.py | 7438 | `97076c37afa7` | source/tool | source/tool/exp06_supplement_probe_2026_10_10.py | L |
| 201 | repo | results/_archive_2026-10-12/exec_artifacts/scan_five_terminal_2026_10_10.py | 4319 | `7200487fdab1` | source/tool | source/tool/scan_five_terminal_2026_10_10.py | L |
| 202 | repo | results/_archive_2026-10-14/voided/_four_class_backtrace_inventory_2026_10_13.md | 29156 | `cc45240386e8` | verdict/pi | verdict/pi/_four_class_backtrace_inventory_2026_10_13.md | L |
| 203 | repo | results/_archive_2026-10-14/voided/_ge01_epsilon_sensitivity_grid_design_2026_10_13.md | 35263 | `fc08d248a6bf` | verdict/pi | verdict/pi/_ge01_epsilon_sensitivity_grid_design_2026_10_13.md | L |
| 204 | repo | results/_archive_2026_09_24/_l11_run1.json | 12143 | `20b0e13064f8` | readout/final | readout/final/_l11_run1.json | L |
| 205 | repo | results/_archive_2026_09_24/_l14_checkpoint.json | 10963 | `91b582672b49` | readout/final | readout/final/_l14_checkpoint.json | L |
| 206 | repo | results/_archive_2026_09_24/_l14_records.json | 50957 | `8f6fcf027149` | readout/final | readout/final/_l14_records.json | L |
| 207 | repo | results/_archive_2026_09_24/_volc_22cap_emb.py | 11105 | `15904ecae629` | source/tool | source/tool/_volc_22cap_emb.py | L |
| 208 | repo | results/_archive_2026_09_24/l14_runner_v2.py | 23056 | `acf1cd6ccbd4` | source/tool | source/tool/l14_runner_v2.py | L |
| 209 | repo | results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py | 25892 | `b1923528ab84` | source/tool | source/tool/l14_runner_v2_r1_atomic_2026_09_29.py | L |
| 210 | repo | results/_d9_e2e_backup_2026_10_13/_v3_recheck_05_result_2026_09_28.json | 450701 | `f63b36b75a51` | readout/final | readout/final/_v3_recheck_05_result_2026_09_28__f63b36b75a51.json | L |
| 211 | repo | results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_d1_ruling_and_s3_transition_2026_10_01.md | 28370 | `dc9cb0e02922` | verdict/pi | verdict/pi/_d1_ruling_and_s3_transition_2026_10_01.md | L |
| 212 | repo | results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_kv3s_3_2_terminal_verdict_2026_10_01.md | 32296 | `693eefdd7a82` | verdict/judge | verdict/judge/_kv3s_3_2_terminal_verdict_2026_10_01.md | L |
| 213 | repo | results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_limb_reading_verdict_kv3s33_2026_10_01.md | 56321 | `4aba41f67db5` | verdict/judge | verdict/judge/_limb_reading_verdict_kv3s33_2026_10_01.md | L |
| 214 | repo | results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_s3_d1_rulings_supplement_register_2026_10_01.md | 28762 | `303bf7c6f34d` | verdict/pi | verdict/pi/_s3_d1_rulings_supplement_register_2026_10_01.md | L |
| 215 | repo | results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/_t1_gate_closure_and_recompute_verdict_2026_10_01.md | 72926 | `784e5d375a6e` | verdict/kd | verdict/kd/_t1_gate_closure_and_recompute_verdict_2026_10_01__784e5d375a6e.md | L |
| 216 | repo | results/_v3_recheck_08b_executor/executor_2026_09_27.py | 43901 | `b292410d9a69` | source/tool | source/tool/executor_2026_09_27__b292410d9a69.py | L |
| 217 | repo | results/_v3_recheck_08b_executor/rescript_2026_09_27.md | 18501 | `78f3aba1f24c` | verdict/pi | verdict/pi/rescript_2026_09_27.md | L |
| 218 | repo | results/_v3_recheck_08b_executor/result_2026_09_27.json | 88052 | `f9a7fa2d65b1` | readout/final | readout/final/result_2026_09_27__f9a7fa2d65b1.json | L |
| 219 | repo | results/_v3_recheck_08c_preexp_data/_v3_recheck_08c_sha12fix_r1_2026_10_12.py | 1395 | `4b7ed4d0a3e5` | source/tool | source/tool/_v3_recheck_08c_sha12fix_r1_2026_10_12.py | L |
| 220 | repo | results/_v3_recheck_08c_preexp_data/executor_2026_09_27.py | 37775 | `cb6eb9164df3` | source/tool | source/tool/executor_2026_09_27__cb6eb9164df3.py | L |
| 221 | repo | results/_v3_recheck_08c_preexp_data/rescript_2026_09_27.md | 17069 | `035af77db626` | verdict/judge | verdict/judge/rescript_2026_09_27.md | L |
| 222 | repo | results/_v3_recheck_08c_preexp_data/result_2026_09_27.json | 146601 | `689a6e4427a8` | readout/final | readout/final/result_2026_09_27.json | L |
| 223 | repo | results/_v3_s1_executor/executor_2026_09_27.py | 54937 | `10870941c283` | source/tool | source/tool/executor_2026_09_27.py | L |
| 224 | repo | results/_v3_s1_executor/rescript_2026_09_27.md | 17253 | `9d49a632ee81` | verdict/kd | verdict/kd/rescript_2026_09_27.md | L |
| 225 | repo | results/_v3_s1_executor/result_2026_09_27.json | 24975 | `bfc99c3133dd` | readout/final | readout/final/result_2026_09_27__bfc99c3133dd.json | L |
| 226 | repo | results/_v3_s2_executor/executor_2026_09_27.py | 84993 | `f1e272a0924a` | source/tool | source/tool/executor_2026_09_27__f1e272a0924a.py | L |
| 227 | repo | results/_v3_s2_executor/rescript_2026_09_27.md | 25151 | `ff0f964be8aa` | verdict/kd | verdict/kd/rescript_2026_09_27__ff0f964be8aa.md | L |
| 228 | repo | results/_v3_s2_executor/result_2026_09_27.json | 51039 | `d73d51e670de` | readout/final | readout/final/result_2026_09_27__d73d51e670de.json | L |
| 229 | repo | results/_v3_s3_wordexpand_data/executor_2026_09_28.py | 46005 | `80f1445ce45d` | source/tool | source/tool/executor_2026_09_28.py | L |
| 230 | repo | results/_v3_s3_wordexpand_data/executor_r1_2026_09_28.py | 43524 | `39c29e0f092e` | source/tool | source/tool/executor_r1_2026_09_28.py | L |
| 231 | repo | results/_v3_s3_wordexpand_data/rescript_2026_09_28.md | 18225 | `98d4f62cd52a` | verdict/kd | verdict/kd/rescript_2026_09_28.md | L |
| 232 | repo | results/_v3_s3_wordexpand_data/result_2026_09_28.json | 34953 | `f7f6d875d73a` | readout/final | readout/final/result_2026_09_28.json | L |
| 233 | repo | results/_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py | 35555 | `96f491a8e2bf` | source/tool | source/tool/executor_2026_09_27__96f491a8e2bf.py | L |
| 234 | repo | results/_v3_s_phrasetemplate_preexp_data/rescript_2026_09_27.md | 17574 | `d42ea1fa61f1` | verdict/judge | verdict/judge/rescript_2026_09_27__d42ea1fa61f1.md | L |
| 235 | repo | results/_v3_s_phrasetemplate_preexp_data/result_2026_09_27.json | 36844 | `fae3c4640507` | readout/final | readout/final/result_2026_09_27__fae3c4640507.json | L |
| 236 | repo | results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json | 4202 | `928794710241` | readout/final | readout/final/v3x_18frozen_remeasure_results_2026_09_16.json | L |
| 237 | repo | results/doc/document/_ablation_design_2026_10_20.md | 98542 | `e1cbf00adcf8` | verdict/kd | verdict/kd/_ablation_design_2026_10_20.md | L |
| 238 | repo | results/doc/document/_bayesian_baseline_design_2026_10_10.md | 29783 | `7e181a167702` | verdict/judge | verdict/judge/_bayesian_baseline_design_2026_10_10.md | L |
| 239 | repo | results/doc/document/_c1c4_input_gap_fill_plan_2026_10_09.md | 35635 | `9f5675633e03` | verdict/judge | verdict/judge/_c1c4_input_gap_fill_plan_2026_10_09.md | L |
| 240 | repo | results/doc/document/_d13_current_caliber_parenthesis_note_2026_10_21.md | 48277 | `a5953d67cfbc` | readout/final | readout/final/_d13_current_caliber_parenthesis_note_2026_10_21.md | L |
| 241 | repo | results/doc/document/_d13_den16_dnm16_retrieval_guide_2026_10_21.md | 50692 | `72d914843f10` | doc/readme | doc/readme/_d13_den16_dnm16_retrieval_guide_2026_10_21.md | L |
| 242 | repo | results/doc/document/_d1d2_and_guide_adoption_supplement_2026_10_12.md | 18881 | `4c60dcbec07f` | verdict/pi | verdict/pi/_d1d2_and_guide_adoption_supplement_2026_10_12.md | L |
| 243 | repo | results/doc/document/_d_dimension_canonical_coexistence_note_2026_10_16.md | 8941 | `a9485534ff5b` | doc/readme | doc/readme/_d_dimension_canonical_coexistence_note_2026_10_16.md | L |
| 244 | repo | results/doc/document/_degradation_reversal_guide_kimi_2026_10_12.md | 7408 | `11f8422fc0f9` | verdict/judge | verdict/judge/_degradation_reversal_guide_kimi_2026_10_12.md | L |
| 245 | repo | results/doc/document/_domain_backfill_design_2026_10_18.md | 46798 | `07efaef73397` | verdict/kd | verdict/kd/_domain_backfill_design_2026_10_18.md | L |
| 246 | repo | results/doc/document/_experimentalization_proposal_batch1_2026_10_21.md | 84029 | `e601c3d606dd` | verdict/kd | verdict/kd/_experimentalization_proposal_batch1_2026_10_21.md | L |
| 247 | repo | results/doc/document/_f2_closeout_note_2026_09_29.md | 16317 | `1599cb99abf3` | verdict/pi | verdict/pi/_f2_closeout_note_2026_09_29.md | L |
| 248 | repo | results/doc/document/_four_class_backtrace_inventory_2026_10_13_r1.md | 29809 | `1b28a9467567` | verdict/pi | verdict/pi/_four_class_backtrace_inventory_2026_10_13_r1.md | L |
| 249 | repo | results/doc/document/_g5_ccp_seed_designation_revision_2026_10_10.md | 20979 | `b53f40abb90b` | verdict/kd | verdict/kd/_g5_ccp_seed_designation_revision_2026_10_10.md | L |
| 250 | repo | results/doc/document/_gd03_caliber_note_2026_10_20.md | 19611 | `b664e821df34` | verdict/pi | verdict/pi/_gd03_caliber_note_2026_10_20.md | L |
| 251 | repo | results/doc/document/_gd03_two_calibers_genesis_note_2026_10_21.md | 25944 | `6b7da22e078c` | verdict/pi | verdict/pi/_gd03_two_calibers_genesis_note_2026_10_21.md | L |
| 252 | repo | results/doc/document/_interval_range_post_lock_note_2026_10_16.md | 16253 | `21737d3a40d5` | verdict/pi | verdict/pi/_interval_range_post_lock_note_2026_10_16.md | L |
| 253 | repo | results/doc/document/_is_corr_pair_caliber_revision_proposal_2026_10_09.md | 33497 | `084c7d20067f` | verdict/judge | verdict/judge/_is_corr_pair_caliber_revision_proposal_2026_10_09.md | L |
| 254 | repo | results/doc/document/_knock_off_directive_effect_2026_10_18.md | 1765 | `a20a7fd90f82` | verdict/pi | verdict/pi/_knock_off_directive_effect_2026_10_18.md | L |
| 255 | repo | results/doc/document/_kreltrig_release_note_2026_10_21.md | 44908 | `25f8841cdbd4` | verdict/pi | verdict/pi/_kreltrig_release_note_2026_10_21.md | L |
| 256 | repo | results/doc/document/_l266_face_label_note_2026_10_16.md | 15074 | `ca2e941d89ff` | readout/final | readout/final/_l266_face_label_note_2026_10_16.md | L |
| 257 | repo | results/doc/document/_m44_status_enum_backfill_design_2026_10_16.md | 51650 | `e17dde9e2547` | verdict/judge | verdict/judge/_m44_status_enum_backfill_design_2026_10_16.md | L |
| 258 | repo | results/doc/document/_numbering_hash_bucket_criterion_design_2026_10_14.md | 21733 | `be92eddb4034` | verdict/judge | verdict/judge/_numbering_hash_bucket_criterion_design_2026_10_14.md | L |
| 259 | repo | results/doc/document/_p3_ablation_design_2026_10_21.md | 112664 | `9fcaaccd555f` | verdict/kd | verdict/kd/_p3_ablation_design_2026_10_21.md | L |
| 260 | repo | results/doc/document/_p9_gatekeeping_note_2026_10_21.md | 22579 | `6c7aae81dcd0` | readout/final | readout/final/_p9_gatekeeping_note_2026_10_21.md | L |
| 261 | repo | results/doc/document/_post_execution_report_kimi_2026_10_18.md | 7251 | `316ea6b69adb` | doc/letter | doc/letter/_post_execution_report_kimi_2026_10_18.md | L |
| 262 | repo | results/doc/document/_preexp_design_kmda8a24_degen_2026_10_20.md | 87243 | `4dc9aaced5f7` | verdict/kd | verdict/kd/_preexp_design_kmda8a24_degen_2026_10_20.md | L |
| 263 | repo | results/doc/document/_preexp_design_new_construct_mda8a24_2026_10_20.md | 79800 | `356ef2e9db1c` | verdict/kd | verdict/kd/_preexp_design_new_construct_mda8a24_2026_10_20.md | L |
| 264 | repo | results/doc/document/_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md | 16105 | `9572dfc3cd59` | verdict/judge | verdict/judge/_q3_c1c4_l282_transposition_fix_applied_note_2026_10_09.md | L |
| 265 | repo | results/doc/document/_r2_build_manifest_2026_10_12.json | 216510 | `303db70b37f6` | readout/final | readout/final/_r2_build_manifest_2026_10_12.json | L |
| 266 | repo | results/doc/document/_r_pair4_design_and_texts_2026_10_09.md | 35189 | `f793c5d9128f` | verdict/judge | verdict/judge/_r_pair4_design_and_texts_2026_10_09.md | L |
| 267 | repo | results/doc/document/_s2_confirmation_parenthesis_correction_note_2026_10_21.md | 106055 | `aee86cfebcfe` | readout/final | readout/final/_s2_confirmation_parenthesis_correction_note_2026_10_21.md | L |
| 268 | repo | results/doc/document/_spec_l22_landing_path_migration_note_2026_10_16.md | 12574 | `b297e95ab164` | doc/readme | doc/readme/_spec_l22_landing_path_migration_note_2026_10_16.md | L |
| 269 | repo | results/doc/document/_spec_l32_scope_note_2026_10_16.md | 13114 | `f171e4d384a9` | doc/readme | doc/readme/_spec_l32_scope_note_2026_10_16.md | L |
| 270 | repo | results/doc/document/_t1_temp_axis_new_experiment_design_2026_10_09.md | 41392 | `7aaa90ee6d50` | verdict/judge | verdict/judge/_t1_temp_axis_new_experiment_design_2026_10_09.md | L |
| 271 | repo | results/doc/document/_th_t1_n_min_revision_proposal_2026_10_09.md | 34884 | `24da21074cc2` | verdict/kd | verdict/kd/_th_t1_n_min_revision_proposal_2026_10_09.md | L |
| 272 | repo | results/doc/document/_upload_plan_2026_10_12.json | 311429 | `10b282bf7d16` | readout/final | readout/final/_upload_plan_2026_10_12.json | L |
| 273 | repo | results/doc/document/_zone_balance_inventory_2026_10_13.md | 725629 | `4a7cfa13c79e` | verdict/pi | verdict/pi/_zone_balance_inventory_2026_10_13.md | L |
| 274 | repo | results/doc/document/c5_guard_minmaxstd_report_2026_10_01.md | 19909 | `f465fbdb7579` | verdict/judge | verdict/judge/c5_guard_minmaxstd_report_2026_10_01.md | L |
| 275 | repo | results/evidence/register/_9model_full_merge_from_4workers_2026_10_09.json | 19337 | `32aa0618a9d7` | readout/final | readout/final/_9model_full_merge_from_4workers_2026_10_09.json | L |
| 276 | repo | results/evidence/register/_anchor_status_naming_note_2026_10_16.md | 11716 | `d042dd66e3c7` | verdict/pi | verdict/pi/_anchor_status_naming_note_2026_10_16.md | L |
| 277 | repo | results/evidence/register/_anchor_value_update_and_l261_patch_migration_register_2026_10_16.md | 17521 | `3f75ce7b3f3f` | verdict/pi | verdict/pi/_anchor_value_update_and_l261_patch_migration_register_2026_10_16.md | L |
| 278 | repo | results/evidence/register/_archive_whitelist_purge_exec_register_2026_10_17.md | 99775 | `9a68efcd5ceb` | verdict/pi | verdict/pi/_archive_whitelist_purge_exec_register_2026_10_17.md | L |
| 279 | repo | results/evidence/register/_archive_zone_exception_g2_extension_register_2026_10_12.md | 4151 | `7ae0c25f072f` | verdict/pi | verdict/pi/_archive_zone_exception_g2_extension_register_2026_10_12.md | L |
| 280 | repo | results/evidence/register/_archive_zone_exception_grant_register_2026_10_12.md | 5750 | `f09279fbb11c` | verdict/pi | verdict/pi/_archive_zone_exception_grant_register_2026_10_12.md | L |
| 281 | repo | results/evidence/register/_archive_zone_exception_p4_extension_register_2026_10_12.md | 3945 | `64da1d988121` | verdict/pi | verdict/pi/_archive_zone_exception_p4_extension_register_2026_10_12.md | L |
| 282 | repo | results/evidence/register/_archive_zone_write_clause_corrigendum_2026_10_17.md | 13526 | `074a6f256655` | readout/final | readout/final/_archive_zone_write_clause_corrigendum_2026_10_17.md | L |
| 283 | repo | results/evidence/register/_b4_source_fix_and_reissue_register_2026_10_12.md | 11168 | `622097d3b964` | verdict/pi | verdict/pi/_b4_source_fix_and_reissue_register_2026_10_12.md | L |
| 284 | repo | results/evidence/register/_batch3_closure_register_2026_10_12.md | 22896 | `69c459496a5b` | verdict/pi | verdict/pi/_batch3_closure_register_2026_10_12.md | L |
| 285 | repo | results/evidence/register/_batch3_residuals_disposition_register_2026_10_12.md | 6278 | `ca31b01643d5` | verdict/pi | verdict/pi/_batch3_residuals_disposition_register_2026_10_12.md | L |
| 286 | repo | results/evidence/register/_batch9_deliberation_judgment_2026_10_14.md | 36623 | `a93cd166a83b` | verdict/judge | verdict/judge/_batch9_deliberation_judgment_2026_10_14.md | L |
| 287 | repo | results/evidence/register/_budget_210_actual_evidence_register_2026_10_16.md | 19542 | `daf7ee522707` | verdict/pi | verdict/pi/_budget_210_actual_evidence_register_2026_10_16.md | L |
| 288 | repo | results/evidence/register/_budget_720_authorized_actual_register_2026_10_16.md | 28062 | `da3c031e0dd6` | verdict/pi | verdict/pi/_budget_720_authorized_actual_register_2026_10_16.md | L |
| 289 | repo | results/evidence/register/_c7_remote_timeline_correction_register_2026_10_14.md | 10314 | `99703cba855f` | verdict/pi | verdict/pi/_c7_remote_timeline_correction_register_2026_10_14.md | L |
| 290 | repo | results/evidence/register/_card_register_relocation_mapping_2026_10_17.md | 17871 | `ff69e7517f8d` | verdict/pi | verdict/pi/_card_register_relocation_mapping_2026_10_17.md | L |
| 291 | repo | results/evidence/register/_card_register_relocation_register_2026_10_17.md | 28415 | `8ca4b2d7320b` | verdict/pi | verdict/pi/_card_register_relocation_register_2026_10_17.md | L |
| 292 | repo | results/evidence/register/_classification_tree_anchor_erratum_2026_10_13.md | 24616 | `781d6d106cb6` | verdict/pi | verdict/pi/_classification_tree_anchor_erratum_2026_10_13.md | L |
| 293 | repo | results/evidence/register/_cleanup511_exec_register_2026_10_17.md | 59310 | `36290316e075` | verdict/pi | verdict/pi/_cleanup511_exec_register_2026_10_17.md | L |
| 294 | repo | results/evidence/register/_clearance_evening_round_register_2026_09_29.md | 18201 | `9c5543961e27` | verdict/pi | verdict/pi/_clearance_evening_round_register_2026_09_29.md | L |
| 295 | repo | results/evidence/register/_closing_round_8_decisions_register_2026_10_09.md | 2151 | `a28a478e14a8` | verdict/pi | verdict/pi/_closing_round_8_decisions_register_2026_10_09.md | L |
| 296 | repo | results/evidence/register/_clue_book_v06_backfill_and_dual_version_register_2026_10_12.md | 12839 | `a0f72c702470` | verdict/pi | verdict/pi/_clue_book_v06_backfill_and_dual_version_register_2026_10_12.md | L |
| 297 | repo | results/evidence/register/_copilot_eq_grok_clarification_register_2026_10_17.md | 25694 | `4d3f76687155` | verdict/pi | verdict/pi/_copilot_eq_grok_clarification_register_2026_10_17.md | L |
| 298 | repo | results/evidence/register/_count_chain_independent_review_2026_10_13.md | 30624 | `8e8abcb0d323` | verdict/judge | verdict/judge/_count_chain_independent_review_2026_10_13.md | L |
| 299 | repo | results/evidence/register/_counting_ban_release_channel_2026_10_16.md | 16740 | `4b117aa1ceeb` | readout/final | readout/final/_counting_ban_release_channel_2026_10_16.md | L |
| 300 | repo | results/evidence/register/_criterion_application_scope_prereg_2026_10_01.md | 50322 | `c4e3338619c6` | verdict/kd | verdict/kd/_criterion_application_scope_prereg_2026_10_01.md | L |
| 301 | repo | results/evidence/register/_d15_d16_caliber_and_authority_register_2026_10_12.md | 18397 | `62604e6d6f06` | verdict/pi | verdict/pi/_d15_d16_caliber_and_authority_register_2026_10_12.md | L |
| 302 | repo | results/evidence/register/_d1_c_effect_register_2026_10_15.md | 30686 | `1bbfa5f33a61` | verdict/pi | verdict/pi/_d1_c_effect_register_2026_10_15.md | L |
| 303 | repo | results/evidence/register/_d2_bytes_column_annotation_register_2026_10_13.md | 8269 | `d1d0e9947d4c` | verdict/pi | verdict/pi/_d2_bytes_column_annotation_register_2026_10_13.md | L |
| 304 | repo | results/evidence/register/_d2_d6_erratum_and_annotation_register_2026_10_12.md | 22698 | `d9da4f54482e` | verdict/pi | verdict/pi/_d2_d6_erratum_and_annotation_register_2026_10_12.md | L |
| 305 | repo | results/evidence/register/_d6_l171_timeblock_restatement_register_2026_10_13.md | 8306 | `8839995131a1` | verdict/pi | verdict/pi/_d6_l171_timeblock_restatement_register_2026_10_13.md | L |
| 306 | repo | results/evidence/register/_d8_boundary_revision_register_2026_09_30.md | 32406 | `b46370bb9e3b` | verdict/pi | verdict/pi/_d8_boundary_revision_register_2026_09_30.md | L |
| 307 | repo | results/evidence/register/_d8_collection_ledger_2026_09_30.md | 20290 | `031dd8429048` | verdict/pi | verdict/pi/_d8_collection_ledger_2026_09_30.md | L |
| 308 | repo | results/evidence/register/_d9_base_reissue_2026_10_13.md | 47738 | `c7bb38f60ffe` | readout/final | readout/final/_d9_base_reissue_2026_10_13.md | L |
| 309 | repo | results/evidence/register/_d9_e2e_disposition_and_f4_closure_register_2026_10_13.md | 22149 | `467b7c10b466` | verdict/pi | verdict/pi/_d9_e2e_disposition_and_f4_closure_register_2026_10_13.md | L |
| 310 | repo | results/evidence/register/_d9_h2_r1files_repair_register_2026_10_13.md | 14026 | `ef3317e5dbb3` | verdict/pi | verdict/pi/_d9_h2_r1files_repair_register_2026_10_13.md | L |
| 311 | repo | results/evidence/register/_d9_independent_review_2026_10_12.md | 22644 | `732cfae29bbc` | verdict/judge | verdict/judge/_d9_independent_review_2026_10_12.md | L |
| 312 | repo | results/evidence/register/_d9_relpath_map_mojibake_defect_register_2026_10_12.md | 5930 | `0ec673877e14` | verdict/pi | verdict/pi/_d9_relpath_map_mojibake_defect_register_2026_10_12.md | L |
| 313 | repo | results/evidence/register/_d9_residual_repair_register_2026_10_12.md | 14927 | `cddb7a196473` | verdict/pi | verdict/pi/_d9_residual_repair_register_2026_10_12.md | L |
| 314 | repo | results/evidence/register/_d9_rewrite_execution_register_2026_10_12.md | 20432 | `0ea7852c4511` | verdict/pi | verdict/pi/_d9_rewrite_execution_register_2026_10_12.md | L |
| 315 | repo | results/evidence/register/_dangling_630_adoption_and_283_corrigendum_2026_10_17.md | 18524 | `2ce9301be94f` | readout/final | readout/final/_dangling_630_adoption_and_283_corrigendum_2026_10_17.md | L |
| 316 | repo | results/evidence/register/_degradation_reversal_guide_dual_adoption_register_2026_10_12.md | 11191 | `65e7c9c521ba` | verdict/pi | verdict/pi/_degradation_reversal_guide_dual_adoption_register_2026_10_12.md | L |
| 317 | repo | results/evidence/register/_deliverables_verification_and_v5_handover_pending_2026_10_12.md | 12636 | `a4fd656650a4` | verdict/pi | verdict/pi/_deliverables_verification_and_v5_handover_pending_2026_10_12.md | L |
| 318 | repo | results/evidence/register/_domain_backfill_brush2_execution_register_2026_10_18.md | 11970 | `62329c8ad856` | verdict/pi | verdict/pi/_domain_backfill_brush2_execution_register_2026_10_18.md | L |
| 319 | repo | results/evidence/register/_domain_backfill_execution_register_2026_10_18.md | 20002 | `6a21885da482` | verdict/pi | verdict/pi/_domain_backfill_execution_register_2026_10_18.md | L |
| 320 | repo | results/evidence/register/_domain_backfill_hold235_retain_register_2026_10_18.md | 25577 | `65224ff572bb` | verdict/pi | verdict/pi/_domain_backfill_hold235_retain_register_2026_10_18.md | L |
| 321 | repo | results/evidence/register/_duplicate_name_six_items_attribution_register_2026_10_12.md | 8476 | `42788a70a913` | verdict/pi | verdict/pi/_duplicate_name_six_items_attribution_register_2026_10_12.md | L |
| 322 | repo | results/evidence/register/_eta_construct_face_freeze_draft_2026_10_19.md | 64877 | `afdb26047b79` | readout/final | readout/final/_eta_construct_face_freeze_draft_2026_10_19.md | L |
| 323 | repo | results/evidence/register/_eta_main_run_register_2026_10_20.md | 39157 | `80da33294928` | verdict/pi | verdict/pi/_eta_main_run_register_2026_10_20.md | L |
| 324 | repo | results/evidence/register/_eta_preexp_run_register_2026_10_20.md | 45129 | `6c0beae1e5da` | verdict/pi | verdict/pi/_eta_preexp_run_register_2026_10_20.md | L |
| 325 | repo | results/evidence/register/_eta_preexp_stop_register_2026_10_20.md | 50188 | `ec6c023dbd6e` | verdict/pi | verdict/pi/_eta_preexp_stop_register_2026_10_20.md | L |
| 326 | repo | results/evidence/register/_f2_branch_fix_register_2026_09_29.md | 22940 | `a0cab58c032e` | verdict/pi | verdict/pi/_f2_branch_fix_register_2026_09_29.md | L |
| 327 | repo | results/evidence/register/_field_sources_lift_register_2026_10_19.md | 21258 | `f44cde956e1e` | verdict/pi | verdict/pi/_field_sources_lift_register_2026_10_19.md | L |
| 328 | repo | results/evidence/register/_forgotten_recovery_register_2026_10_08.md | 34287 | `c981347cffad` | verdict/pi | verdict/pi/_forgotten_recovery_register_2026_10_08.md | L |
| 329 | repo | results/evidence/register/_four_items_alternative_deliberation_judgment_2026_10_13.md | 44728 | `0b5bb95a86d7` | verdict/judge | verdict/judge/_four_items_alternative_deliberation_judgment_2026_10_13.md | L |
| 330 | repo | results/evidence/register/_freeze_final_replay_2026_10_18.md | 31254 | `a95605c38bac` | verdict/judge | verdict/judge/_freeze_final_replay_2026_10_18.md | L |
| 331 | repo | results/evidence/register/_freeze_preexp_design_2026_10_17.md | 40906 | `d52a5d94a002` | verdict/kd | verdict/kd/_freeze_preexp_design_2026_10_17.md | L |
| 332 | repo | results/evidence/register/_freeze_preexp_exec_2026_10_17.md | 34681 | `547da6852c98` | readout/final | readout/final/_freeze_preexp_exec_2026_10_17.md | L |
| 333 | repo | results/evidence/register/_freeze_preexp_exec_r2_2026_10_17.md | 52887 | `fd3656a22b1c` | readout/final | readout/final/_freeze_preexp_exec_r2_2026_10_17.md | L |
| 334 | repo | results/evidence/register/_g1_archive_zone_search_register_2026_10_12.md | 14175 | `3f293b8c5444` | verdict/pi | verdict/pi/_g1_archive_zone_search_register_2026_10_12.md | L |
| 335 | repo | results/evidence/register/_g1_closure_register_2026_10_12.md | 20423 | `10bd066ab5bf` | verdict/pi | verdict/pi/_g1_closure_register_2026_10_12.md | L |
| 336 | repo | results/evidence/register/_g2_residual_cause_register_2026_10_12.md | 26134 | `e6b881562420` | verdict/pi | verdict/pi/_g2_residual_cause_register_2026_10_12.md | L |
| 337 | repo | results/evidence/register/_gate1_count_defect_erratum_2026_10_13.md | 23027 | `41bfe0a7c58d` | verdict/pi | verdict/pi/_gate1_count_defect_erratum_2026_10_13.md | L |
| 338 | repo | results/evidence/register/_gate1_gap_residuals_adoption_register_2026_10_12.md | 30908 | `b84b9808fc71` | verdict/pi | verdict/pi/_gate1_gap_residuals_adoption_register_2026_10_12.md | L |
| 339 | repo | results/evidence/register/_gate1_unclosed_writeoff_register_2026_10_13.md | 25318 | `5cea0cc0148c` | verdict/pi | verdict/pi/_gate1_unclosed_writeoff_register_2026_10_13.md | L |
| 340 | repo | results/evidence/register/_gate_one_registers_erratum_distribution_and_path_2026_10_12.md | 13901 | `69ac4fb16a4f` | verdict/pi | verdict/pi/_gate_one_registers_erratum_distribution_and_path_2026_10_12.md | L |
| 341 | repo | results/evidence/register/_gate_one_reopened_and_stage2_rejection_register_2026_10_12.md | 8644 | `b2f6f55e76b7` | verdict/pi | verdict/pi/_gate_one_reopened_and_stage2_rejection_register_2026_10_12.md | L |
| 342 | repo | results/evidence/register/_ge01_5anchor_json_approval_register_2026_10_14.md | 29776 | `d9b30c816e2c` | verdict/pi | verdict/pi/_ge01_5anchor_json_approval_register_2026_10_14.md | L |
| 343 | repo | results/evidence/register/_ge01_5anchor_json_register_2026_10_14.md | 31882 | `65000a1ac5bc` | verdict/pi | verdict/pi/_ge01_5anchor_json_register_2026_10_14.md | L |
| 344 | repo | results/evidence/register/_ge01_c2_canonical_effect_register_2026_10_14.md | 27902 | `b92a7830d38a` | verdict/pi | verdict/pi/_ge01_c2_canonical_effect_register_2026_10_14.md | L |
| 345 | repo | results/evidence/register/_ge01_c3_gaps_disposition_2026_10_14.md | 33390 | `0e796a657868` | verdict/pi | verdict/pi/_ge01_c3_gaps_disposition_2026_10_14.md | L |
| 346 | repo | results/evidence/register/_ge01_c5_disposition_register_2026_10_14.md | 16314 | `181aa4d580a1` | verdict/pi | verdict/pi/_ge01_c5_disposition_register_2026_10_14.md | L |
| 347 | repo | results/evidence/register/_ge01_calculator_rebuild_design_2026_10_14.md | 46007 | `8ab699f017c8` | verdict/pi | verdict/pi/_ge01_calculator_rebuild_design_2026_10_14.md | L |
| 348 | repo | results/evidence/register/_ge01_calculator_rebuild_register_2026_10_14.md | 31515 | `0bb909c36108` | verdict/pi | verdict/pi/_ge01_calculator_rebuild_register_2026_10_14.md | L |
| 349 | repo | results/evidence/register/_ge01_d1_theory_input_disposition_2026_10_14.md | 36272 | `657fe57c8cbd` | verdict/pi | verdict/pi/_ge01_d1_theory_input_disposition_2026_10_14.md | L |
| 350 | repo | results/evidence/register/_ge01_ecr_anchor_convergence_deliberation_2026_10_14.md | 26832 | `b32ca40ec103` | verdict/pi | verdict/pi/_ge01_ecr_anchor_convergence_deliberation_2026_10_14.md | L |
| 351 | repo | results/evidence/register/_ge01_ecr_anchor_effect_register_2026_10_15.md | 15707 | `2c7c202aafec` | verdict/pi | verdict/pi/_ge01_ecr_anchor_effect_register_2026_10_15.md | L |
| 352 | repo | results/evidence/register/_ge01_ecr_baseline_invalid_register_2026_10_14.md | 22796 | `dcdfe7c0bd09` | verdict/pi | verdict/pi/_ge01_ecr_baseline_invalid_register_2026_10_14.md | L |
| 353 | repo | results/evidence/register/_ge01_epsilon_grid_exec_register_2026_10_16.md | 45389 | `f8de4abb5e12` | verdict/pi | verdict/pi/_ge01_epsilon_grid_exec_register_2026_10_16.md | L |
| 354 | repo | results/evidence/register/_ge01_epsilon_sensitivity_grid_design_r1_2026_10_13.md | 35956 | `7551c47d3ece` | verdict/pi | verdict/pi/_ge01_epsilon_sensitivity_grid_design_r1_2026_10_13.md | L |
| 355 | repo | results/evidence/register/_ge01_freeze_flow_execution_2026_10_20.md | 58027 | `0d1dd9d16d8a` | verdict/pi | verdict/pi/_ge01_freeze_flow_execution_2026_10_20.md | L |
| 356 | repo | results/evidence/register/_ge01_frozen_runs_on_disk_erratum_2026_10_13.md | 22559 | `6aa7fb58b270` | verdict/pi | verdict/pi/_ge01_frozen_runs_on_disk_erratum_2026_10_13.md | L |
| 357 | repo | results/evidence/register/_ge01_full_1494_exec_2026_10_16.md | 32363 | `e0efc8501305` | verdict/judge | verdict/judge/_ge01_full_1494_exec_2026_10_16.md | L |
| 358 | repo | results/evidence/register/_ge01_full_1494_exec_r1_2026_10_16.md | 46115 | `515128a23182` | verdict/judge | verdict/judge/_ge01_full_1494_exec_r1_2026_10_16.md | L |
| 359 | repo | results/evidence/register/_ge01_full_1494_freeze_2026_10_16.md | 14129 | `171d1b6d5725` | readout/final | readout/final/_ge01_full_1494_freeze_2026_10_16.md | L |
| 360 | repo | results/evidence/register/_ge01_full_1494_resume32_register_2026_10_16.md | 41003 | `ae4b90375fe7` | verdict/pi | verdict/pi/_ge01_full_1494_resume32_register_2026_10_16.md | L |
| 361 | repo | results/evidence/register/_ge01_gt_kill_family_byte_stream_effect_register_2026_10_14.md | 29189 | `e631795149eb` | verdict/pi | verdict/pi/_ge01_gt_kill_family_byte_stream_effect_register_2026_10_14.md | L |
| 362 | repo | results/evidence/register/_ge01_gt_kill_family_carrier_construction_draft_2026_10_14.md | 32568 | `75a818b2654f` | verdict/kd | verdict/kd/_ge01_gt_kill_family_carrier_construction_draft_2026_10_14.md | L |
| 363 | repo | results/evidence/register/_ge01_gt_kill_family_member_table_register_2026_10_14.md | 28470 | `ccf1071ce431` | verdict/pi | verdict/pi/_ge01_gt_kill_family_member_table_register_2026_10_14.md | L |
| 364 | repo | results/evidence/register/_ge01_launch_gate_recheck_2026_10_17.md | 82206 | `de8fd5291962` | verdict/pi | verdict/pi/_ge01_launch_gate_recheck_2026_10_17.md | L |
| 365 | repo | results/evidence/register/_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md | 17808 | `ed3b544d33a6` | verdict/kd | verdict/kd/_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md | L |
| 366 | repo | results/evidence/register/_ge01_prereg_5anchor_v3.json | 35911 | `0c269b9558da` | readout/final | readout/final/_ge01_prereg_5anchor_v3.json | L |
| 367 | repo | results/evidence/register/_ge01_prereg_prelexp_selection_design_v2_2026_10_13.md | 46864 | `6fc11dacaf24` | verdict/kd | verdict/kd/_ge01_prereg_prelexp_selection_design_v2_2026_10_13.md | L |
| 368 | repo | results/evidence/register/_ge01_prereg_seven_requirements_draft_2026_10_13.md | 39337 | `0a031a9795a9` | verdict/kd | verdict/kd/_ge01_prereg_seven_requirements_draft_2026_10_13.md | L |
| 369 | repo | results/evidence/register/_ge01_readiness_after_prereg_effect_2026_10_13.md | 31736 | `5a72c931148a` | verdict/kd | verdict/kd/_ge01_readiness_after_prereg_effect_2026_10_13.md | L |
| 370 | repo | results/evidence/register/_ge01_s3_v_adjudicable_recheck_2026_10_16.md | 51621 | `3873af2cce4f` | readout/final | readout/final/_ge01_s3_v_adjudicable_recheck_2026_10_16.md | L |
| 371 | repo | results/evidence/register/_ge01_s3b_v_exec_2026_10_16.md | 54012 | `89b3be872de8` | readout/final | readout/final/_ge01_s3b_v_exec_2026_10_16.md | L |
| 372 | repo | results/evidence/register/_ge01_spec_anchor_canonical_register_2026_10_14.md | 22828 | `fb73dc317eb5` | verdict/pi | verdict/pi/_ge01_spec_anchor_canonical_register_2026_10_14.md | L |
| 373 | repo | results/evidence/register/_ge01_spec_anchor_erratum_2026_10_14.md | 18129 | `2eeb522748ca` | doc/readme | doc/readme/_ge01_spec_anchor_erratum_2026_10_14.md | L |
| 374 | repo | results/evidence/register/_ge01_unblock_effect_register_2026_10_14.md | 24534 | `277a6f9e4d94` | verdict/pi | verdict/pi/_ge01_unblock_effect_register_2026_10_14.md | L |
| 375 | repo | results/evidence/register/_ge01_unblock_progress_2026_10_14.md | 25315 | `893eddf769a6` | verdict/pi | verdict/pi/_ge01_unblock_progress_2026_10_14.md | L |
| 376 | repo | results/evidence/register/_ge02_adoption_freeze_register_2026_10_20.md | 29719 | `f45df63a9469` | verdict/pi | verdict/pi/_ge02_adoption_freeze_register_2026_10_20.md | L |
| 377 | repo | results/evidence/register/_ge02_anchor_landing_build_register_2026_10_16.md | 15311 | `629567744899` | verdict/pi | verdict/pi/_ge02_anchor_landing_build_register_2026_10_16.md | L |
| 378 | repo | results/evidence/register/_ge02_anchor_landing_effect_register_2026_10_16.md | 18441 | `5347521e5add` | verdict/pi | verdict/pi/_ge02_anchor_landing_effect_register_2026_10_16.md | L |
| 379 | repo | results/evidence/register/_gitignore_rx_fix_adoption_register_2026_10_17.md | 13078 | `277bfe56b9ee` | verdict/pi | verdict/pi/_gitignore_rx_fix_adoption_register_2026_10_17.md | L |
| 380 | repo | results/evidence/register/_glm_crossface_item4_register_2026_10_13.md | 5345 | `2d8d5e8c58be` | verdict/pi | verdict/pi/_glm_crossface_item4_register_2026_10_13.md | L |
| 381 | repo | results/evidence/register/_glm_delivery_face_disposition_register_2026_10_13.md | 16662 | `4d9f84d04cae` | verdict/pi | verdict/pi/_glm_delivery_face_disposition_register_2026_10_13.md | L |
| 382 | repo | results/evidence/register/_glm_delivery_pack_verification_2026_10_14.md | 12580 | `a2d1a9187ee9` | verdict/pi | verdict/pi/_glm_delivery_pack_verification_2026_10_14.md | L |
| 383 | repo | results/evidence/register/_glm_evidence_pack_unpack_register_2026_10_13.md | 28909 | `5762be8a68f8` | verdict/pi | verdict/pi/_glm_evidence_pack_unpack_register_2026_10_13.md | L |
| 384 | repo | results/evidence/register/_gt_kill_family_carrier_draft_register_2026_10_15.md | 22501 | `d8c41976ef1b` | verdict/pi | verdict/pi/_gt_kill_family_carrier_draft_register_2026_10_15.md | L |
| 385 | repo | results/evidence/register/_gt_kill_line_carrier_effect_register_2026_10_15.md | 25941 | `e40f060fa3a3` | verdict/kd | verdict/kd/_gt_kill_line_carrier_effect_register_2026_10_15.md | L |
| 386 | repo | results/evidence/register/_harness_anchor_reconcile_register_2026_10_16.md | 26023 | `4de10aad8f0b` | verdict/pi | verdict/pi/_harness_anchor_reconcile_register_2026_10_16.md | L |
| 387 | repo | results/evidence/register/_item6_c2_e3_erratum_update_register_2026_10_18.md | 30176 | `4d4633d3a48a` | verdict/pi | verdict/pi/_item6_c2_e3_erratum_update_register_2026_10_18.md | L |
| 388 | repo | results/evidence/register/_item6_c3_selflimit_sentence_effect_register_2026_10_18.md | 20228 | `d8f9e9fe68db` | verdict/pi | verdict/pi/_item6_c3_selflimit_sentence_effect_register_2026_10_18.md | L |
| 389 | repo | results/evidence/register/_killface_v1_effect_register_2026_10_16.md | 21872 | `98aabe87ae11` | verdict/pi | verdict/pi/_killface_v1_effect_register_2026_10_16.md | L |
| 390 | repo | results/evidence/register/_kt_a1_v0_lineage_corrigendum_2026_10_14.md | 31849 | `e2c35c2ac858` | doc/readme | doc/readme/_kt_a1_v0_lineage_corrigendum_2026_10_14.md | L |
| 391 | repo | results/evidence/register/_leftover_minor_adoptions_register_2026_10_12.md | 13565 | `e18e620e22c5` | verdict/pi | verdict/pi/_leftover_minor_adoptions_register_2026_10_12.md | L |
| 392 | repo | results/evidence/register/_log_purge_register_2026_10_13.md | 8855 | `d0d5ba7a7cde` | verdict/pi | verdict/pi/_log_purge_register_2026_10_13.md | L |
| 393 | repo | results/evidence/register/_log_purge_v2_execution_register_2026_10_13.md | 6671 | `13f959934b3a` | verdict/pi | verdict/pi/_log_purge_v2_execution_register_2026_10_13.md | L |
| 394 | repo | results/evidence/register/_log_retention_policy_register_2026_10_13.md | 7055 | `a44f903ea331` | verdict/pi | verdict/pi/_log_retention_policy_register_2026_10_13.md | L |
| 395 | repo | results/evidence/register/_m08_boundary_caliber_c1_c8_effect_2026_10_16.md | 16630 | `608572ded536` | verdict/pi | verdict/pi/_m08_boundary_caliber_c1_c8_effect_2026_10_16.md | L |
| 396 | repo | results/evidence/register/_m3_disposition_v_eps_star_register_2026_10_16.md | 23452 | `fd452e0cb8c0` | verdict/pi | verdict/pi/_m3_disposition_v_eps_star_register_2026_10_16.md | L |
| 397 | repo | results/evidence/register/_m5_k5_network_verification_register_2026_10_13.md | 23309 | `7a4b2695c1d5` | verdict/pi | verdict/pi/_m5_k5_network_verification_register_2026_10_13.md | L |
| 398 | repo | results/evidence/register/_main_count_caliber_lock_2026_10_16.md | 14055 | `6f1a253db9bd` | readout/final | readout/final/_main_count_caliber_lock_2026_10_16.md | L |
| 399 | repo | results/evidence/register/_material_expansion_sourcing_2026_10_16.md | 31814 | `afd1c0517a43` | readout/final | readout/final/_material_expansion_sourcing_2026_10_16.md | L |
| 400 | repo | results/evidence/register/_md_trigger_prereg_effectivity_2026_10_11.md | 41636 | `5d8cd0d1676f` | verdict/kd | verdict/kd/_md_trigger_prereg_effectivity_2026_10_11.md | L |
| 401 | repo | results/evidence/register/_mda8_preexp_run_register_2026_10_20.md | 32115 | `9061fb974b18` | verdict/pi | verdict/pi/_mda8_preexp_run_register_2026_10_20.md | L |
| 402 | repo | results/evidence/register/_mq_rollout_v1_effect_register_2026_10_14.md | 14924 | `3bd1942ec154` | verdict/pi | verdict/pi/_mq_rollout_v1_effect_register_2026_10_14.md | L |
| 403 | repo | results/evidence/register/_mq_rollout_v2_effect_register_2026_10_14.md | 15336 | `652da23484e2` | verdict/pi | verdict/pi/_mq_rollout_v2_effect_register_2026_10_14.md | L |
| 404 | repo | results/evidence/register/_mq_rollout_v3_effect_register_2026_10_14.md | 9649 | `66536311243d` | verdict/pi | verdict/pi/_mq_rollout_v3_effect_register_2026_10_14.md | L |
| 405 | repo | results/evidence/register/_mq_rollout_v4_effect_register_2026_10_14.md | 24423 | `5f33f74e947d` | verdict/pi | verdict/pi/_mq_rollout_v4_effect_register_2026_10_14.md | L |
| 406 | repo | results/evidence/register/_mq_rollout_v5_effect_register_2026_10_14.md | 15119 | `591e432c1635` | verdict/pi | verdict/pi/_mq_rollout_v5_effect_register_2026_10_14.md | L |
| 407 | repo | results/evidence/register/_mq_rollout_v6_effect_register_2026_10_14.md | 15467 | `d79637fee0ef` | verdict/pi | verdict/pi/_mq_rollout_v6_effect_register_2026_10_14.md | L |
| 408 | repo | results/evidence/register/_mq_rollout_v9_effect_register_2026_10_14.md | 29389 | `aa4e8d0554e2` | verdict/pi | verdict/pi/_mq_rollout_v9_effect_register_2026_10_14.md | L |
| 409 | repo | results/evidence/register/_n2_equivalence_verification_register_2026_10_12.md | 29081 | `1987d48234a3` | verdict/pi | verdict/pi/_n2_equivalence_verification_register_2026_10_12.md | L |
| 410 | repo | results/evidence/register/_n3_o5_terminal_effect_register_2026_10_16.md | 35944 | `7414869866ad` | verdict/pi | verdict/pi/_n3_o5_terminal_effect_register_2026_10_16.md | L |
| 411 | repo | results/evidence/register/_n7_af_relocation_register_2026_10_17.md | 35057 | `7a2133c810b1` | verdict/pi | verdict/pi/_n7_af_relocation_register_2026_10_17.md | L |
| 412 | repo | results/evidence/register/_ncc2_expansion_c6c7_prereg_2026_10_21.md | 101030 | `f83fee00746c` | verdict/kd | verdict/kd/_ncc2_expansion_c6c7_prereg_2026_10_21.md | L |
| 413 | repo | results/evidence/register/_night_mode_adoption_relabel_register_2026_10_14.md | 8672 | `2660d5ea717d` | verdict/pi | verdict/pi/_night_mode_adoption_relabel_register_2026_10_14.md | L |
| 414 | repo | results/evidence/register/_night_outputs_adoption_register_2026_10_16.md | 8476 | `837685c9ef64` | verdict/pi | verdict/pi/_night_outputs_adoption_register_2026_10_16.md | L |
| 415 | repo | results/evidence/register/_night_shift_handover_2026_10_14.md | 48375 | `c3d766464634` | readout/final | readout/final/_night_shift_handover_2026_10_14.md | L |
| 416 | repo | results/evidence/register/_noncore_upload_caliber_effect_register_2026_10_17.md | 50419 | `f007da0a98d6` | verdict/pi | verdict/pi/_noncore_upload_caliber_effect_register_2026_10_17.md | L |
| 417 | repo | results/evidence/register/_null_u_aggregation_effect_register_2026_10_16.md | 17142 | `7af0b66a68a1` | verdict/pi | verdict/pi/_null_u_aggregation_effect_register_2026_10_16.md | L |
| 418 | repo | results/evidence/register/_numbering_family_count_effect_register_2026_10_14.md | 22786 | `80a97ee882d5` | verdict/pi | verdict/pi/_numbering_family_count_effect_register_2026_10_14.md | L |
| 419 | repo | results/evidence/register/_o1_reading_c_effect_register_2026_10_16.md | 30762 | `30e0dee146ce` | verdict/pi | verdict/pi/_o1_reading_c_effect_register_2026_10_16.md | L |
| 420 | repo | results/evidence/register/_p4_fallback_target_search_register_2026_10_12.md | 14561 | `dba255b2b734` | verdict/pi | verdict/pi/_p4_fallback_target_search_register_2026_10_12.md | L |
| 421 | repo | results/evidence/register/_p4_inplace_resolution_register_2026_10_13.md | 13194 | `d2aeaeedf39c` | verdict/pi | verdict/pi/_p4_inplace_resolution_register_2026_10_13.md | L |
| 422 | repo | results/evidence/register/_pa_harness_anchor_v3_effect_register_2026_10_16.md | 12794 | `22c336d5049b` | verdict/pi | verdict/pi/_pa_harness_anchor_v3_effect_register_2026_10_16.md | L |
| 423 | repo | results/evidence/register/_pa_harness_anchor_value_update_v3.json | 23745 | `0c205e8efa43` | readout/final | readout/final/_pa_harness_anchor_value_update_v3.json | L |
| 424 | repo | results/evidence/register/_pa_harness_anchor_value_update_v3_lock_register_2026_10_16.md | 19555 | `ccb5a8e0301e` | verdict/pi | verdict/pi/_pa_harness_anchor_value_update_v3_lock_register_2026_10_16.md | L |
| 425 | repo | results/evidence/register/_pack_fingerprint_baseline_register_2026_10_14.md | 15051 | `b8468b52cd64` | verdict/pi | verdict/pi/_pack_fingerprint_baseline_register_2026_10_14.md | L |
| 426 | repo | results/evidence/register/_pack_payload8_k1r4r3_disposition_register_2026_10_14.md | 17602 | `092485278299` | verdict/pi | verdict/pi/_pack_payload8_k1r4r3_disposition_register_2026_10_14.md | L |
| 427 | repo | results/evidence/register/_pb_anchor_reanchor_register_2026_10_14.md | 11438 | `91b9326c5a2e` | verdict/pi | verdict/pi/_pb_anchor_reanchor_register_2026_10_14.md | L |
| 428 | repo | results/evidence/register/_prereg_caliber4_epsilon_revision_2026_10_15.md | 9659 | `e49c11b43c65` | verdict/kd | verdict/kd/_prereg_caliber4_epsilon_revision_2026_10_15.md | L |
| 429 | repo | results/evidence/register/_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md | 18582 | `a3dd3cc1caf2` | verdict/kd | verdict/kd/_prereg_lock_v1_epsilon_lu_klm41_register_2026_10_15.md | L |
| 430 | repo | results/evidence/register/_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md | 33312 | `4c782fc8566b` | verdict/kd | verdict/kd/_prereg_lock_v2_h_epsilon_gamma_taucert_u_register_2026_10_15.md | L |
| 431 | repo | results/evidence/register/_prereg_lock_v2a_t5_completion_register_2026_10_15.md | 46621 | `404d4fbeef40` | verdict/kd | verdict/kd/_prereg_lock_v2a_t5_completion_register_2026_10_15.md | L |
| 432 | repo | results/evidence/register/_r3_m2_disposition_register_2026_10_14.md | 17025 | `e11bc0e63ccc` | verdict/pi | verdict/pi/_r3_m2_disposition_register_2026_10_14.md | L |
| 433 | repo | results/evidence/register/_r5_spec_pack_retrieval_register_2026_10_13.md | 24845 | `d7ef2c8e56bb` | verdict/pi | verdict/pi/_r5_spec_pack_retrieval_register_2026_10_13.md | L |
| 434 | repo | results/evidence/register/_r6_github_face_verification_2026_10_14.md | 18215 | `fd70af96eff9` | readout/final | readout/final/_r6_github_face_verification_2026_10_14.md | L |
| 435 | repo | results/evidence/register/_r9_ge01_prereg_effect_register_2026_10_13.md | 16466 | `18529950fe6f` | verdict/kd | verdict/kd/_r9_ge01_prereg_effect_register_2026_10_13.md | L |
| 436 | repo | results/evidence/register/_r_pair_addendum_2026_10_09.json | 110510 | `cebc2f6ef5ec` | readout/final | readout/final/_r_pair_addendum_2026_10_09.json | L |
| 437 | repo | results/evidence/register/_r_pair_intake_recompute_register_2026_10_09.md | 36774 | `2dc64593b889` | verdict/pi | verdict/pi/_r_pair_intake_recompute_register_2026_10_09.md | L |
| 438 | repo | results/evidence/register/_refonly_161_verify_register_2026_10_17.md | 69821 | `74d63d55ee97` | verdict/pi | verdict/pi/_refonly_161_verify_register_2026_10_17.md | L |
| 439 | repo | results/evidence/register/_refonly_161_verify_register_r2_2026_10_17.md | 94675 | `b687e16cc7d9` | verdict/pi | verdict/pi/_refonly_161_verify_register_r2_2026_10_17.md | L |
| 440 | repo | results/evidence/register/_register_correction_batch_and_u14_effect_2026_10_17.md | 55316 | `9a94037f80d1` | verdict/pi | verdict/pi/_register_correction_batch_and_u14_effect_2026_10_17.md | L |
| 441 | repo | results/evidence/register/_remote_baseline_advance_register_2026_10_12.md | 6625 | `ebf55ddb1eb2` | verdict/pi | verdict/pi/_remote_baseline_advance_register_2026_10_12.md | L |
| 442 | repo | results/evidence/register/_resume32_adoption_and_flip_register_2026_10_16.md | 38971 | `9d220cae64b9` | verdict/pi | verdict/pi/_resume32_adoption_and_flip_register_2026_10_16.md | L |
| 443 | repo | results/evidence/register/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md | 24690 | `9da183328f18` | verdict/pi | verdict/pi/_s4_heldout_sampling_seedprime_items_register_2026_10_10.md | L |
| 444 | repo | results/evidence/register/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md | 22646 | `784f042bf93d` | verdict/pi | verdict/pi/_s4_heldout_sampling_seedthird_items_register_2026_10_11.md | L |
| 445 | repo | results/evidence/register/_s4_open_questions_intake_recompute_register_2026_10_09.md | 33672 | `2e66478e6db6` | verdict/pi | verdict/pi/_s4_open_questions_intake_recompute_register_2026_10_09.md | L |
| 446 | repo | results/evidence/register/_s4_substrate_freeze_register_2026_10_09.md | 29064 | `f4a52862521b` | verdict/pi | verdict/pi/_s4_substrate_freeze_register_2026_10_09.md | L |
| 447 | repo | results/evidence/register/_s4_substrate_refreeze_register_179_2026_10_09.md | 45386 | `24ea764daeac` | verdict/pi | verdict/pi/_s4_substrate_refreeze_register_179_2026_10_09.md | L |
| 448 | repo | results/evidence/register/_s4_substrate_topup_collection_register_2026_10_09.md | 18327 | `33c1a818ef4f` | verdict/pi | verdict/pi/_s4_substrate_topup_collection_register_2026_10_09.md | L |
| 449 | repo | results/evidence/register/_s4_topup_intake_recompute_register_2026_10_09.md | 32779 | `dfc9b0fbef5a` | verdict/pi | verdict/pi/_s4_topup_intake_recompute_register_2026_10_09.md | L |
| 450 | repo | results/evidence/register/_s4_v31_regen_gold_register_2026_10_10.md | 27133 | `9c9d8e8ecc72` | verdict/pi | verdict/pi/_s4_v31_regen_gold_register_2026_10_10.md | L |
| 451 | repo | results/evidence/register/_seven23_map_revision_register_2026_10_12.md | 7050 | `e981be2e3286` | verdict/pi | verdict/pi/_seven23_map_revision_register_2026_10_12.md | L |
| 452 | repo | results/evidence/register/_skill_reference_update_and_user_surface_survey_2026_09_30.md | 60621 | `cb7b7ec9ebcd` | verdict/pi | verdict/pi/_skill_reference_update_and_user_surface_survey_2026_09_30.md | L |
| 453 | repo | results/evidence/register/_stage1_eta_kill_line_freeze_draft_2026_10_19.md | 38472 | `f9ab11413a94` | verdict/kd | verdict/kd/_stage1_eta_kill_line_freeze_draft_2026_10_19.md | L |
| 454 | repo | results/evidence/register/_stage1_eta_numeric_freeze_draft_2026_10_19.md | 39393 | `1d7baa667b98` | verdict/kd | verdict/kd/_stage1_eta_numeric_freeze_draft_2026_10_19.md | L |
| 455 | repo | results/evidence/register/_stage1_eta_preexp_execution_register_2026_10_19.md | 31832 | `a7787f3c8e6e` | verdict/pi | verdict/pi/_stage1_eta_preexp_execution_register_2026_10_19.md | L |
| 456 | repo | results/evidence/register/_stage1_eta_preexp_run_register_2026_10_19.md | 25002 | `851aeb7a8782` | verdict/pi | verdict/pi/_stage1_eta_preexp_run_register_2026_10_19.md | L |
| 457 | repo | results/evidence/register/_stage1_field_table_completion_register_2026_10_19.md | 50471 | `ae2addc2ccce` | verdict/pi | verdict/pi/_stage1_field_table_completion_register_2026_10_19.md | L |
| 458 | repo | results/evidence/register/_stage1_field_table_freeze_draft_2026_10_19.md | 51152 | `c29628efe748` | verdict/kd | verdict/kd/_stage1_field_table_freeze_draft_2026_10_19.md | L |
| 459 | repo | results/evidence/register/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md | 4495 | `a0e437ef317c` | verdict/pi | verdict/pi/_stage3_1_register_fingerprint_placeholder_erratum_2026_10_12.md | L |
| 460 | repo | results/evidence/register/_stage3_completion_and_stage4_open_register_2026_10_12.md | 12634 | `e2f4ad9e1360` | verdict/pi | verdict/pi/_stage3_completion_and_stage4_open_register_2026_10_12.md | L |
| 461 | repo | results/evidence/register/_stage4_close_and_batch3_receipt_register_2026_10_18.md | 2406 | `1abec5fd9839` | verdict/pi | verdict/pi/_stage4_close_and_batch3_receipt_register_2026_10_18.md | L |
| 462 | repo | results/evidence/register/_stage5_g2_item_e_closure_turn_b_register_2026_10_18.md | 2050 | `47df3ce2ce4e` | verdict/pi | verdict/pi/_stage5_g2_item_e_closure_turn_b_register_2026_10_18.md | L |
| 463 | repo | results/evidence/register/_stage_sequence_violation_register_2026_10_12.md | 11159 | `8dcfc200c7fd` | verdict/pi | verdict/pi/_stage_sequence_violation_register_2026_10_12.md | L |
| 464 | repo | results/evidence/register/_strip_c3_non_adoption_register_2026_10_16.md | 25221 | `726c32d83734` | verdict/pi | verdict/pi/_strip_c3_non_adoption_register_2026_10_16.md | L |
| 465 | repo | results/evidence/register/_supplement_500_combo_effect_register_2026_10_16.md | 30213 | `ddd311fb1311` | verdict/pi | verdict/pi/_supplement_500_combo_effect_register_2026_10_16.md | L |
| 466 | repo | results/evidence/register/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md | 16994 | `bda5d5f3dfa0` | verdict/kd | verdict/kd/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md | L |
| 467 | repo | results/evidence/register/_t1_prereg_revision_temp_axis_exp2_2026_10_09.md | 34217 | `2ff15aeeb5d0` | verdict/kd | verdict/kd/_t1_prereg_revision_temp_axis_exp2_2026_10_09.md | L |
| 468 | repo | results/evidence/register/_t1_qwen_temp_sweep_exec_register_2026_10_09.md | 17341 | `7ad31e741400` | verdict/pi | verdict/pi/_t1_qwen_temp_sweep_exec_register_2026_10_09.md | L |
| 469 | repo | results/evidence/register/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md | 23681 | `cf4826a731d6` | verdict/pi | verdict/pi/_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md | L |
| 470 | repo | results/evidence/register/_t1_r2_activation_2026_10_09.md | 21111 | `8e59b797aa2d` | verdict/judge | verdict/judge/_t1_r2_activation_2026_10_09.md | L |
| 471 | repo | results/evidence/register/_t2_license_final_register_2026_10_16.md | 18510 | `0ba73a1793e1` | verdict/pi | verdict/pi/_t2_license_final_register_2026_10_16.md | L |
| 472 | repo | results/evidence/register/_t4_license_final_register_2026_10_16.md | 16202 | `d575f88b40ce` | verdict/pi | verdict/pi/_t4_license_final_register_2026_10_16.md | L |
| 473 | repo | results/evidence/register/_theory_u_hit_rate_retirement_register_2026_10_15.md | 22012 | `1ba41ba3bbe9` | verdict/pi | verdict/pi/_theory_u_hit_rate_retirement_register_2026_10_15.md | L |
| 474 | repo | results/evidence/register/_three_exception_pullback_register_2026_10_13.md | 12295 | `62fff3dc6cca` | verdict/pi | verdict/pi/_three_exception_pullback_register_2026_10_13.md | L |
| 475 | repo | results/evidence/register/_three_seed_readout_validity_effect_register_2026_10_16.md | 27429 | `1f988e61beb2` | verdict/pi | verdict/pi/_three_seed_readout_validity_effect_register_2026_10_16.md | L |
| 476 | repo | results/evidence/register/_tmp_archive_disposition_register_2026_10_12.md | 12836 | `3fdf474df1f9` | verdict/pi | verdict/pi/_tmp_archive_disposition_register_2026_10_12.md | L |
| 477 | repo | results/evidence/register/_tmp_carrier_original_deletion_register_2026_10_19.md | 7499 | `0b3779e78310` | verdict/pi | verdict/pi/_tmp_carrier_original_deletion_register_2026_10_19.md | L |
| 478 | repo | results/evidence/register/_tmp_single_copy_preservation_register_2026_10_21.md | 32341 | `709068245ab3` | verdict/pi | verdict/pi/_tmp_single_copy_preservation_register_2026_10_21.md | L |
| 479 | repo | results/evidence/register/_trae_issues_batch2_corrections_register_2026_10_12.md | 36422 | `592800923f3f` | verdict/pi | verdict/pi/_trae_issues_batch2_corrections_register_2026_10_12.md | L |
| 480 | repo | results/evidence/register/_trae_issues_dfamily_corrections_register_2026_10_12.md | 33471 | `12da29eb102c` | verdict/pi | verdict/pi/_trae_issues_dfamily_corrections_register_2026_10_12.md | L |
| 481 | repo | results/evidence/register/_two_items_alternative_deliberation_judgment_2026_10_13.md | 44778 | `f2cdaad477f6` | readout/final | readout/final/_two_items_alternative_deliberation_judgment_2026_10_13.md | L |
| 482 | repo | results/evidence/register/_u_1494_carrier_effect_register_2026_10_16.md | 42588 | `6f194df09b33` | verdict/pi | verdict/pi/_u_1494_carrier_effect_register_2026_10_16.md | L |
| 483 | repo | results/evidence/register/_u_33_34_lock_and_33_declaration_coexistence_register_2026_10_16.md | 28868 | `5c6120d7e69b` | verdict/pi | verdict/pi/_u_33_34_lock_and_33_declaration_coexistence_register_2026_10_16.md | L |
| 484 | repo | results/evidence/register/_u_720face_lock_register_2026_10_17.md | 41007 | `4ed6194729b5` | verdict/pi | verdict/pi/_u_720face_lock_register_2026_10_17.md | L |
| 485 | repo | results/evidence/register/_u_axis_equation_direction_effect_register_2026_10_16.md | 18935 | `68c4a68b1ee8` | verdict/pi | verdict/pi/_u_axis_equation_direction_effect_register_2026_10_16.md | L |
| 486 | repo | results/evidence/register/_u_hface15_18889_lock_register_2026_10_17.md | 24452 | `59f8c6c2826b` | verdict/pi | verdict/pi/_u_hface15_18889_lock_register_2026_10_17.md | L |
| 487 | repo | results/evidence/register/_u_hface_lock_register_2026_10_16.md | 15551 | `892f8f9ae0b5` | verdict/pi | verdict/pi/_u_hface_lock_register_2026_10_16.md | L |
| 488 | repo | results/evidence/register/_u_recalc_post_expansion_2026_10_16.md | 28570 | `c5116ff749b1` | readout/final | readout/final/_u_recalc_post_expansion_2026_10_16.md | L |
| 489 | repo | results/evidence/register/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md | 31100 | `0cf3faba8c21` | verdict/pi | verdict/pi/_unclosed_47_direct_clear_b_tier_register_2026_10_13.md | L |
| 490 | repo | results/evidence/register/_unclosed_47_direct_clear_register_2026_10_13.md | 35560 | `3d87efe5680d` | verdict/pi | verdict/pi/_unclosed_47_direct_clear_register_2026_10_13.md | L |
| 491 | repo | results/evidence/register/_upload_ledger_2026_10_12.json | 367903 | `44019e7dca1e` | readout/final | readout/final/_upload_ledger_2026_10_12.json | L |
| 492 | repo | results/evidence/register/_v3_recheck_prereg_v1_2026_09_27.md | 37346 | `88052d7db895` | verdict/kd | verdict/kd/_v3_recheck_prereg_v1_2026_09_27.md | L |
| 493 | repo | results/evidence/register/_v3_recheck_prereg_v1p1_2026_09_27.md | 42970 | `bcc3cee23e82` | verdict/kd | verdict/kd/_v3_recheck_prereg_v1p1_2026_09_27.md | L |
| 494 | repo | results/evidence/register/_v3_recheck_prereg_v1p2_2026_09_27.md | 38932 | `9da148037744` | verdict/kd | verdict/kd/_v3_recheck_prereg_v1p2_2026_09_27.md | L |
| 495 | repo | results/evidence/register/_v3_recheck_prereg_v1p3_2026_09_27.md | 35200 | `272ed65bf50e` | verdict/kd | verdict/kd/_v3_recheck_prereg_v1p3_2026_09_27.md | L |
| 496 | repo | results/evidence/register/_v3_recheck_prereg_v1p4_2026_09_27.md | 69406 | `5294e4a2bd14` | verdict/kd | verdict/kd/_v3_recheck_prereg_v1p4_2026_09_27.md | L |
| 497 | repo | results/evidence/register/_v3_recheck_prereg_v1p5_2026_09_29.md | 18680 | `7b1374578de4` | verdict/kd | verdict/kd/_v3_recheck_prereg_v1p5_2026_09_29.md | L |
| 498 | repo | results/evidence/register/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md | 33932 | `7e1323b09030` | verdict/kd | verdict/kd/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md | L |
| 499 | repo | results/evidence/register/_v3_s_prereg_v1_2026_09_27.md | 46836 | `ef5a40554960` | verdict/kd | verdict/kd/_v3_s_prereg_v1_2026_09_27.md | L |
| 500 | repo | results/evidence/register/_v4_bom_u1_prereg_2026_09_28.md | 19185 | `5456acbf2cb5` | verdict/kd | verdict/kd/_v4_bom_u1_prereg_2026_09_28.md | L |
| 501 | repo | results/evidence/register/_v4_closeout_bulk_reorganize_register_2026_10_12.md | 197283 | `2b244f0760b4` | verdict/pi | verdict/pi/_v4_closeout_bulk_reorganize_register_2026_10_12.md | L |
| 502 | repo | results/evidence/register/_v4_effective_register_2026_09_28.md | 30607 | `2a65c1274202` | verdict/pi | verdict/pi/_v4_effective_register_2026_09_28.md | L |
| 503 | repo | results/evidence/register/_v4_item04_textfix_prereg_v1x_2026_09_28.md | 42153 | `4ad2695935d3` | verdict/kd | verdict/kd/_v4_item04_textfix_prereg_v1x_2026_09_28.md | L |
| 504 | repo | results/evidence/register/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md | 62847 | `e7c3e2ef4e6b` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md | L |
| 505 | repo | results/evidence/register/_v4_supp_prereg_v02_add_T15_2026_09_24.md | 76991 | `8898b964a9d9` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_T15_2026_09_24.md | L |
| 506 | repo | results/evidence/register/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md | 97059 | `883dced872b4` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md | L |
| 507 | repo | results/evidence/register/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md | 34195 | `f6ed61c25572` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_T15r2_activation_2026_09_26.md | L |
| 508 | repo | results/evidence/register/_v4_supp_prereg_v02_add_T1_2026_09_24.md | 52942 | `802dece2286a` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_T1_2026_09_24.md | L |
| 509 | repo | results/evidence/register/_v5_c3_reading_b_prereg_2026_09_28.md | 32178 | `8dcf5e1e6dde` | verdict/kd | verdict/kd/_v5_c3_reading_b_prereg_2026_09_28.md | L |
| 510 | repo | results/evidence/register/_v5_closing_register_2026_09_28.md | 27224 | `522b08506290` | verdict/kd | verdict/kd/_v5_closing_register_2026_09_28.md | L |
| 511 | repo | results/evidence/register/_v5_confirm_b11_decisions_register_2026_09_29.md | 12276 | `07e9fe512da5` | verdict/kd | verdict/kd/_v5_confirm_b11_decisions_register_2026_09_29.md | L |
| 512 | repo | results/evidence/register/_v5_confirm_b14_b15_decisions_register_2026_09_29.md | 26154 | `e48276a8dd31` | verdict/kd | verdict/kd/_v5_confirm_b14_b15_decisions_register_2026_09_29.md | L |
| 513 | repo | results/evidence/register/_v5_confirm_b5_decisions_register_2026_09_29.md | 45525 | `3b5f2819af8f` | verdict/pi | verdict/pi/_v5_confirm_b5_decisions_register_2026_09_29.md | L |
| 514 | repo | results/evidence/register/_v5_confirm_b7_decisions_register_2026_09_29.md | 23833 | `0a80ae035042` | verdict/kd | verdict/kd/_v5_confirm_b7_decisions_register_2026_09_29.md | L |
| 515 | repo | results/evidence/register/_v5_confirm_b9_decisions_register_2026_09_29.md | 17008 | `8c510cda6014` | verdict/pi | verdict/pi/_v5_confirm_b9_decisions_register_2026_09_29.md | L |
| 516 | repo | results/evidence/register/_v5_exec_f2_r3_register_2026_09_29.md | 24177 | `9d64ee1d6996` | verdict/pi | verdict/pi/_v5_exec_f2_r3_register_2026_09_29.md | L |
| 517 | repo | results/evidence/register/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md | 63447 | `2505ff5d203f` | verdict/kd | verdict/kd/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md | L |
| 518 | repo | results/evidence/register/_v5_gt_p10_lowarm_prereg_2026_09_29.md | 38464 | `07e28e2fe374` | verdict/kd | verdict/kd/_v5_gt_p10_lowarm_prereg_2026_09_29.md | L |
| 519 | repo | results/evidence/register/_v5_item21_anchor_recompute_2026_09_28.md | 9221 | `e5623d4bd3f3` | verdict/judge | verdict/judge/_v5_item21_anchor_recompute_2026_09_28.md | L |
| 520 | repo | results/evidence/register/_v5_item26b_endpoint_definition_prereg_2026_09_28.md | 38939 | `5e59a11466db` | verdict/kd | verdict/kd/_v5_item26b_endpoint_definition_prereg_2026_09_28.md | L |
| 521 | repo | results/evidence/register/_v5_item26b_literal_gap_prereg_v2_2026_09_28.md | 38885 | `bb0a211fa675` | verdict/kd | verdict/kd/_v5_item26b_literal_gap_prereg_v2_2026_09_28.md | L |
| 522 | repo | results/evidence/register/_v5_item35_prereg_v2_2026_09_28.md | 35633 | `1fb2419c6e96` | verdict/kd | verdict/kd/_v5_item35_prereg_v2_2026_09_28.md | L |
| 523 | repo | results/evidence/register/_v5_item35_v3_collinear_prereg_2026_09_29.md | 42504 | `873652fd39dd` | verdict/kd | verdict/kd/_v5_item35_v3_collinear_prereg_2026_09_29.md | L |
| 524 | repo | results/evidence/register/_v5_pjpm_pc_deg_prereg_2026_09_29.md | 59446 | `989ee2bce660` | verdict/kd | verdict/kd/_v5_pjpm_pc_deg_prereg_2026_09_29.md | L |
| 525 | repo | results/evidence/register/_v5_r2h2_residual_merged_catalogue_2026_09_29.md | 50554 | `b62d19c1c7cc` | verdict/kd | verdict/kd/_v5_r2h2_residual_merged_catalogue_2026_09_29.md | L |
| 526 | repo | results/evidence/register/_v5_sub_artifact_ledger_2026_09_28.md | 71818 | `dd38c77ea486` | verdict/kd | verdict/kd/_v5_sub_artifact_ledger_2026_09_28.md | L |
| 527 | repo | results/evidence/register/_v5_v3_deg_fix_prereg_2026_09_29.md | 41622 | `98286cc1aec7` | verdict/kd | verdict/kd/_v5_v3_deg_fix_prereg_2026_09_29.md | L |
| 528 | repo | results/evidence/register/_voided_files_reference_update_2026_10_14.md | 16514 | `3f29efd33d80` | verdict/pi | verdict/pi/_voided_files_reference_update_2026_10_14.md | L |
| 529 | repo | results/evidence/register/_voided_files_relocation_register_2026_10_14.md | 9587 | `d72b3a52c20c` | verdict/pi | verdict/pi/_voided_files_relocation_register_2026_10_14.md | L |
| 530 | repo | results/evidence/register/_whitelist_backup_mapping_2026_10_17.md | 155757 | `8115382861f3` | readout/final | readout/final/_whitelist_backup_mapping_2026_10_17.md | L |
| 531 | repo | results/evidence/register/_whitelist_register_2026_10_17.md | 120358 | `7511b98c6483` | verdict/pi | verdict/pi/_whitelist_register_2026_10_17.md | L |
| 532 | repo | results/evidence/register/_xiang14_reissue_register_2026_10_13.md | 13928 | `519a6be78024` | verdict/pi | verdict/pi/_xiang14_reissue_register_2026_10_13.md | L |
| 533 | repo | results/evidence/register/_xiang14_third_pullback_register_2026_10_18.md | 7632 | `8923c8d44aaa` | verdict/pi | verdict/pi/_xiang14_third_pullback_register_2026_10_18.md | L |
| 534 | repo | results/evidence/register/_xiang14_third_reissue_registration_2026_10_13.md | 7188 | `25141de92c50` | verdict/pi | verdict/pi/_xiang14_third_reissue_registration_2026_10_13.md | L |
| 535 | repo | results/evidence/register/_z1_d9_three_and_c1_adoption_register_2026_10_12.md | 19446 | `8f1542dca1c5` | verdict/pi | verdict/pi/_z1_d9_three_and_c1_adoption_register_2026_10_12.md | L |
| 536 | repo | results/evidence/register/_z1_n2_da25_agency_register_2026_10_12.md | 22223 | `718842329683` | verdict/pi | verdict/pi/_z1_n2_da25_agency_register_2026_10_12.md | L |
| 537 | repo | results/evidence/register/_z1_three_yishi_adoption_register_2026_10_12.md | 19922 | `836b5d0611b7` | verdict/pi | verdict/pi/_z1_three_yishi_adoption_register_2026_10_12.md | L |
| 538 | repo | results/evidence/register/_z1_two_items_adoption_register_2026_10_12.md | 20261 | `312d74cf5630` | verdict/pi | verdict/pi/_z1_two_items_adoption_register_2026_10_12.md | L |
| 539 | repo | results/evidence/register/_zerocall_gap_proof_register_2026_10_17.md | 47618 | `92d59ee2500f` | verdict/pi | verdict/pi/_zerocall_gap_proof_register_2026_10_17.md | L |
| 540 | repo | results/evidence/register/c5_b_group_root_candidate_2026_10_01.md | 28867 | `2fd8946cfe80` | readout/final | readout/final/c5_b_group_root_candidate_2026_10_01.md | L |
| 541 | repo | results/evidence/register/ge01_prereg_5anchor_landing_v1.json | 50650 | `5518346a5e61` | readout/final | readout/final/ge01_prereg_5anchor_landing_v1.json | L |
| 542 | repo | results/readout/reading/_ablation_reading_2026_10_20.md | 102663 | `ce5548bffaf3` | readout/final | readout/final/_ablation_reading_2026_10_20.md | L |
| 543 | repo | results/readout/reading/_d05_b_coincidence_checks_exec_readings_2026_10_10.json | 13960 | `586c435d1f15` | readout/final | readout/final/_d05_b_coincidence_checks_exec_readings_2026_10_10.json | L |
| 544 | repo | results/readout/reading/_eta_main_run_reading_2026_10_20.json | 786523 | `f6fa0e8934b1` | readout/final | readout/final/_eta_main_run_reading_2026_10_20.json | L |
| 545 | repo | results/readout/reading/_eta_preexp_run_reading_2026_10_20.json | 1415042 | `df037dcb3a3a` | readout/final | readout/final/_eta_preexp_run_reading_2026_10_20.json | L |
| 546 | repo | results/readout/reading/_eta_sep_measurement_reading_2026_10_20.md | 36597 | `d9fe4bebfb84` | verdict/pi | verdict/pi/_eta_sep_measurement_reading_2026_10_20.md | L |
| 547 | repo | results/readout/reading/_exp04_h_contrast_readings_2026_10_10.md | 17386 | `ac571bfe4d1d` | verdict/judge | verdict/judge/_exp04_h_contrast_readings_2026_10_10.md | L |
| 548 | repo | results/readout/reading/_exp8_bar_a_reading_2026_10_21.md | 46810 | `10c66e478b77` | verdict/pi | verdict/pi/_exp8_bar_a_reading_2026_10_21.md | L |
| 549 | repo | results/readout/reading/_h_exact_enum_run_reading_2026_10_21.md | 48472 | `3317fe625320` | readout/final | readout/final/_h_exact_enum_run_reading_2026_10_21.md | L |
| 550 | repo | results/readout/reading/_k_v3s_4_3_frozen_recompute_2026_10_09.md | 26674 | `1c1494083255` | verdict/judge | verdict/judge/_k_v3s_4_3_frozen_recompute_2026_10_09.md | L |
| 551 | repo | results/readout/reading/_mda8_preexp_run_reading_2026_10_20.json | 145592 | `56eb9db8bfd1` | readout/final | readout/final/_mda8_preexp_run_reading_2026_10_20.json | L |
| 552 | repo | results/readout/reading/_mq19_item6_f12_archive_recompute_2026_10_14.md | 65549 | `0dfd3c886020` | verdict/judge | verdict/judge/_mq19_item6_f12_archive_recompute_2026_10_14.md | L |
| 553 | repo | results/readout/reading/_numbering_family_count_erratum_2026_10_13.md | 15557 | `26b708beb153` | readout/final | readout/final/_numbering_family_count_erratum_2026_10_13.md | L |
| 554 | repo | results/readout/reading/_numbering_raw_residual_461_root_cause_2026_10_14.md | 17806 | `23e0b4f997a4` | verdict/judge | verdict/judge/_numbering_raw_residual_461_root_cause_2026_10_14.md | L |
| 555 | repo | results/readout/reading/_p3_ablation_run_reading_2026_10_21.md | 69520 | `7559adb143d1` | readout/final | readout/final/_p3_ablation_run_reading_2026_10_21.md | L |
| 556 | repo | results/readout/reading/_preexp_degen_gate_reading_2026_10_20.md | 46923 | `a039533d6893` | verdict/judge | verdict/judge/_preexp_degen_gate_reading_2026_10_20.md | L |
| 557 | repo | results/readout/reading/_preexp_mda8a24_c1_reading_2026_10_20.md | 36891 | `d3115c5850cc` | readout/final | readout/final/_preexp_mda8a24_c1_reading_2026_10_20.md | L |
| 558 | repo | results/readout/reading/_preexp_mda8a24_c2c4_reading_2026_10_20.md | 44911 | `d91a11e88b95` | verdict/judge | verdict/judge/_preexp_mda8a24_c2c4_reading_2026_10_20.md | L |
| 559 | repo | results/readout/reading/_preexp_mda8a24_c5_armpairs_reading_2026_10_20.md | 45500 | `3386b8bd838e` | readout/final | readout/final/_preexp_mda8a24_c5_armpairs_reading_2026_10_20.md | L |
| 560 | repo | results/readout/reading/_reading_e_33_baseline_declaration_deliberation_2026_10_15.md | 29882 | `74622229f730` | readout/final | readout/final/_reading_e_33_baseline_declaration_deliberation_2026_10_15.md | L |
| 561 | repo | results/readout/reading/_reading_e_33_historical_nominal_value_corrigendum_2026_10_15.md | 26976 | `20ad5b45ba2c` | verdict/pi | verdict/pi/_reading_e_33_historical_nominal_value_corrigendum_2026_10_15.md | L |
| 562 | repo | results/readout/reading/_replies_arrival_and_stage2_restore_directive_effect_2026_10_19.md | 2753 | `249853568c26` | doc/letter | doc/letter/_replies_arrival_and_stage2_restore_directive_effect_2026_10_19.md | L |
| 563 | repo | results/readout/reading/_ritt_remeasure_readings_2026_10_17.md | 23064 | `16dccc9c0a88` | verdict/pi | verdict/pi/_ritt_remeasure_readings_2026_10_17.md | L |
| 564 | repo | results/readout/reading/_runface_vs_shape_multidim_reading_2026_10_20.md | 68272 | `94d0ddba7adb` | readout/final | readout/final/_runface_vs_shape_multidim_reading_2026_10_20.md | L |
| 565 | repo | results/readout/reading/_s3_closeout_convergence_2026_10_01.md | 42443 | `bb62b5c174da` | verdict/judge | verdict/judge/_s3_closeout_convergence_2026_10_01.md | L |
| 566 | repo | results/readout/reading/_s3_d1fill_recount_2026_10_01.md | 22877 | `a7dff824ed56` | readout/final | readout/final/_s3_d1fill_recount_2026_10_01.md | L |
| 567 | repo | results/readout/reading/_s3_f1_loader_fix_recompute_2026_10_08.json | 20144 | `3044a070106e` | readout/final | readout/final/_s3_f1_loader_fix_recompute_2026_10_08.json | L |
| 568 | repo | results/readout/reading/_s3_flip_s5_resolution_effect_2026_10_17.md | 37073 | `9bd2c6df2834` | readout/final | readout/final/_s3_flip_s5_resolution_effect_2026_10_17.md | L |
| 569 | repo | results/readout/reading/_s3_kv3s_3_full_recompute_2026_10_01.md | 22183 | `b0123f161c10` | verdict/pi | verdict/pi/_s3_kv3s_3_full_recompute_2026_10_01.md | L |
| 570 | repo | results/readout/reading/_s4_daily_share_margin_prerequisite_2026_10_09.md | 18197 | `a929502e8421` | verdict/pi | verdict/pi/_s4_daily_share_margin_prerequisite_2026_10_09.md | L |
| 571 | repo | results/readout/reading/_s4_face_five_lines_ci_readings_execution_2026_10_09.md | 29750 | `73550514152d` | verdict/judge | verdict/judge/_s4_face_five_lines_ci_readings_execution_2026_10_09.md | L |
| 572 | repo | results/readout/reading/_s4_face_five_lines_exec_sec8_erratum_2026_10_12.md | 16696 | `9e17535df62e` | readout/final | readout/final/_s4_face_five_lines_exec_sec8_erratum_2026_10_12.md | L |
| 573 | repo | results/readout/reading/_s4_face_sync_2026_10_09.md | 38955 | `6f8ba105b892` | verdict/pi | verdict/pi/_s4_face_sync_2026_10_09.md | L |
| 574 | repo | results/readout/reading/_s4_face_v2_sync_2026_10_09.md | 46890 | `9d3cc20fd980` | verdict/pi | verdict/pi/_s4_face_v2_sync_2026_10_09.md | L |
| 575 | repo | results/readout/reading/_s4_heldout_sampling_seed42_items_2026_10_09.json | 20033 | `6a670e629dca` | readout/final | readout/final/_s4_heldout_sampling_seed42_items_2026_10_09.json | L |
| 576 | repo | results/readout/reading/_s4_heldout_sampling_seedprime_items_2026_10_10.json | 15409 | `6cbb8ba01bfb` | readout/final | readout/final/_s4_heldout_sampling_seedprime_items_2026_10_10.json | L |
| 577 | repo | results/readout/reading/_s4_heldout_sampling_seedthird_items_2026_10_11.json | 43130 | `5777a07c608a` | readout/final | readout/final/_s4_heldout_sampling_seedthird_items_2026_10_11.json | L |
| 578 | repo | results/readout/reading/_s4_open_questions_addendum_2026_10_09.json | 35215 | `4378dcc20624` | readout/final | readout/final/_s4_open_questions_addendum_2026_10_09.json | L |
| 579 | repo | results/readout/reading/_s4_open_questions_design_2026_10_09.md | 31803 | `0186a4499bbc` | verdict/judge | verdict/judge/_s4_open_questions_design_2026_10_09.md | L |
| 580 | repo | results/readout/reading/_s4_reading_prep_order_2026_10_08.md | 20613 | `7ac726cda752` | verdict/judge | verdict/judge/_s4_reading_prep_order_2026_10_08.md | L |
| 581 | repo | results/readout/reading/_s4_regen_execution_plan_2026_10_10.md | 33444 | `70e22220350d` | verdict/judge | verdict/judge/_s4_regen_execution_plan_2026_10_10.md | L |
| 582 | repo | results/readout/reading/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md | 24783 | `b2b044289ffe` | readout/final | readout/final/_s4_seedprime_seq_t1_only_supplement_2026_10_11.md | L |
| 583 | repo | results/readout/reading/_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json | 28030 | `a834e0e7121a` | readout/final | readout/final/_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json | L |
| 584 | repo | results/readout/reading/_s4_source_wave_mapping_registration_2026_10_10.md | 38231 | `26c8278e3552` | verdict/pi | verdict/pi/_s4_source_wave_mapping_registration_2026_10_10.md | L |
| 585 | repo | results/readout/reading/_s4_substrate_grid_availability_2026_10_08.md | 14995 | `7deaee06c41a` | verdict/judge | verdict/judge/_s4_substrate_grid_availability_2026_10_08.md | L |
| 586 | repo | results/readout/reading/_s4_substrate_topup_addendum_2026_10_09.json | 85861 | `1780542f0014` | readout/final | readout/final/_s4_substrate_topup_addendum_2026_10_09.json | L |
| 587 | repo | results/readout/reading/_s4_topup_questionnaire_design_2026_10_09.md | 38466 | `b8f8f987f21b` | verdict/judge | verdict/judge/_s4_topup_questionnaire_design_2026_10_09.md | L |
| 588 | repo | results/readout/reading/_s4_tree_construct_adjusted_readings_2026_10_10.json | 108593 | `a7aa4e9c8d47` | readout/final | readout/final/_s4_tree_construct_adjusted_readings_2026_10_10.json | L |
| 589 | repo | results/readout/reading/_s4_tree_construct_adjustment_assessment_2026_10_10.md | 33453 | `016c7dacaa54` | verdict/judge | verdict/judge/_s4_tree_construct_adjustment_assessment_2026_10_10.md | L |
| 590 | repo | results/readout/reading/_s4_v31_displacement_items_2026_10_10.json | 36822 | `6f020c03e52c` | readout/final | readout/final/_s4_v31_displacement_items_2026_10_10.json | L |
| 591 | repo | results/readout/reading/_s4_v31_readings_summary_2026_10_10.json | 5569 | `882a1b3deb0b` | readout/final | readout/final/_s4_v31_readings_summary_2026_10_10.json | L |
| 592 | repo | results/readout/reading/_s4_vclause_1_6_revision_2026_10_10.md | 14900 | `017b3cf38ae3` | verdict/pi | verdict/pi/_s4_vclause_1_6_revision_2026_10_10.md | L |
| 593 | repo | results/readout/reading/_s4prime_five_lines_readings_2026_10_11.json | 15219 | `65a9b9be6327` | readout/final | readout/final/_s4prime_five_lines_readings_2026_10_11.json | L |
| 594 | repo | results/readout/reading/_s5doubleprime_five_lines_readings_2026_10_11.json | 16099 | `839fb5452578` | readout/final | readout/final/_s5doubleprime_five_lines_readings_2026_10_11.json | L |
| 595 | repo | results/readout/reading/_stage1_experiment_gap_inventory_2026_10_19.md | 56161 | `73c78efbf555` | readout/final | readout/final/_stage1_experiment_gap_inventory_2026_10_19.md | L |
| 596 | repo | results/readout/reading/_stage1_gate_remedy_draft_2026_10_12.md | 35130 | `764f3376f830` | verdict/judge | verdict/judge/_stage1_gate_remedy_draft_2026_10_12.md | L |
| 597 | repo | results/readout/reading/_stage1_independent_gate_review_2026_10_12.md | 29479 | `4d95ae28c469` | verdict/judge | verdict/judge/_stage1_independent_gate_review_2026_10_12.md | L |
| 598 | repo | results/readout/reading/_stage1_prereq_wave1_proposals_2026_10_20.md | 77534 | `a8a9018fd67e` | verdict/kd | verdict/kd/_stage1_prereq_wave1_proposals_2026_10_20.md | L |
| 599 | repo | results/readout/reading/_stage34_completion_withdrawal_effect_2026_10_19.md | 2804 | `22a99b582f83` | verdict/pi | verdict/pi/_stage34_completion_withdrawal_effect_2026_10_19.md | L |
| 600 | repo | results/readout/reading/_stage3_trigger_readings_items_2026_10_11.json | 21049 | `079108c62a82` | readout/final | readout/final/_stage3_trigger_readings_items_2026_10_11.json | L |
| 601 | repo | results/readout/reading/_stage3_trigger_recheck_2026_10_11.md | 49109 | `aef26b8cbe50` | verdict/judge | verdict/judge/_stage3_trigger_recheck_2026_10_11.md | L |
| 602 | repo | results/readout/reading/_stage5_7_3_registration_dissolution_2026_10_18.md | 46684 | `b0560bc85be8` | verdict/pi | verdict/pi/_stage5_7_3_registration_dissolution_2026_10_18.md | L |
| 603 | repo | results/readout/reading/_stage5_7_6_citation_permission_effect_2026_10_18.md | 29727 | `ac4b2de65837` | readout/final | readout/final/_stage5_7_6_citation_permission_effect_2026_10_18.md | L |
| 604 | repo | results/readout/reading/_stage5_g1_g3_g4_verification_2026_10_18.md | 45863 | `7339ce946b37` | readout/final | readout/final/_stage5_g1_g3_g4_verification_2026_10_18.md | L |
| 605 | repo | results/readout/reading/_stage5_g2_deferred_disposition_plan_2026_10_18.md | 44782 | `6c080b069f94` | verdict/pi | verdict/pi/_stage5_g2_deferred_disposition_plan_2026_10_18.md | L |
| 606 | repo | results/readout/reading/_stage5_g2_tier_b_registration_execution_2026_10_18.md | 52500 | `dc84cdff1ce9` | verdict/pi | verdict/pi/_stage5_g2_tier_b_registration_execution_2026_10_18.md | L |
| 607 | repo | results/readout/reading/_stage5_g6_g8_adoption_effect_2026_10_18.md | 42597 | `4fd2e6b938e0` | readout/final | readout/final/_stage5_g6_g8_adoption_effect_2026_10_18.md | L |
| 608 | repo | results/readout/reading/_stage5_g6_g8_four_items_ranking_2026_10_18.md | 44294 | `6e71388400ee` | readout/final | readout/final/_stage5_g6_g8_four_items_ranking_2026_10_18.md | L |
| 609 | repo | results/readout/reading/_stage5_g6_g8_four_items_ranking_adoption_effect_2026_10_18.md | 34819 | `f730f6b24b68` | readout/final | readout/final/_stage5_g6_g8_four_items_ranking_adoption_effect_2026_10_18.md | L |
| 610 | repo | results/readout/reading/_stage5_preparation_design_2026_10_18.md | 43856 | `20ad343fb8d3` | doc/paper | doc/paper/_stage5_preparation_design_2026_10_18.md | L |
| 611 | repo | results/readout/reading/_supplement_execution_receipt_kimi_2026_10_18.md | 41236 | `85f8777f139c` | doc/letter | doc/letter/_supplement_execution_receipt_kimi_2026_10_18.md | L |
| 612 | repo | results/readout/reading/_t1_exp2_answer_face_baseline_2026_10_09.json | 11792 | `35773f5f1edb` | readout/final | readout/final/_t1_exp2_answer_face_baseline_2026_10_09.json | L |
| 613 | repo | results/readout/reading/_t2_path_b_build_exec_2026_10_16.md | 35389 | `359ab9d180f2` | verdict/kd | verdict/kd/_t2_path_b_build_exec_2026_10_16.md | L |
| 614 | repo | results/readout/reading/_t2_t3_value_request_form_2026_10_14.md | 15054 | `21abb5173b87` | readout/final | readout/final/_t2_t3_value_request_form_2026_10_14.md | L |
| 615 | repo | results/readout/reading/_t2_t3_value_sourcing_2026_10_15.md | 24658 | `bcb0d60fdd2d` | readout/final | readout/final/_t2_t3_value_sourcing_2026_10_15.md | L |
| 616 | repo | results/readout/reading/_t_s3_3_disposition_judgment_2026_10_10.md | 31855 | `ee7a822a077b` | verdict/pi | verdict/pi/_t_s3_3_disposition_judgment_2026_10_10.md | L |
| 617 | repo | results/readout/reading/_three_seed_readout_validity_deliberation_2026_10_16.md | 32097 | `75e5608106ec` | verdict/judge | verdict/judge/_three_seed_readout_validity_deliberation_2026_10_16.md | L |
| 618 | repo | results/readout/reading/_u04_1_exemption_precondition_verification_2026_10_09.json | 21862 | `bddfeac3ee2f` | readout/final | readout/final/_u04_1_exemption_precondition_verification_2026_10_09.json | L |
| 619 | repo | results/readout/reading/_v3_s3_collection_brief_2026_09_28.md | 19045 | `d5ba1161e37f` | verdict/kd | verdict/kd/_v3_s3_collection_brief_2026_09_28.md | L |
| 620 | repo | results/readout/reading/_v3_s3_wordexpand_recheck_r1_2026_09_28.json | 33867 | `67ccea282d1c` | readout/final | readout/final/_v3_s3_wordexpand_recheck_r1_2026_09_28.json | L |
| 621 | repo | results/readout/reading/_v5_item21_patched_recompute_2026_09_28.json | 14879 | `aa53e5db77c9` | readout/final | readout/final/_v5_item21_patched_recompute_2026_09_28.json | L |
| 622 | repo | results/readout/reading/_v5_item21_strategyqa_realias_recompute_2026_09_29.json | 34314 | `49f068c716a8` | readout/final | readout/final/_v5_item21_strategyqa_realias_recompute_2026_09_29.json | L |
| 623 | repo | results/readout/reading/_v5_item35_v3_collinear_recompute_2026_10_01.json | 49682 | `a210e2c41275` | readout/final | readout/final/_v5_item35_v3_collinear_recompute_2026_10_01.json | L |
| 624 | repo | results/readout/reading/_v5_pjpm_pc_closeout_readout_2026_09_29.md | 32243 | `1b9ac6b07670` | verdict/pi | verdict/pi/_v5_pjpm_pc_closeout_readout_2026_09_29.md | L |
| 625 | repo | results/readout/reading/_v5r_s40_recompute_2026_09_29.json | 4992 | `5be465342ae1` | readout/final | readout/final/_v5r_s40_recompute_2026_09_29.json | L |
| 626 | repo | results/readout/reading/c5_b_group_fix_readings_2026_10_09.json | 10029 | `4e415990b71d` | readout/final | readout/final/c5_b_group_fix_readings_2026_10_09.json | L |
| 627 | repo | results/readout/reading/c5_guard_minmaxstd_readings_2026_10_01.json | 19935 | `7ff301514f66` | readout/final | readout/final/c5_guard_minmaxstd_readings_2026_10_01.json | L |
| 628 | repo | results/readout/run/_af_landing_n7_and_two_cells_effect_2026_10_17.md | 40560 | `955222063aa0` | verdict/pi | verdict/pi/_af_landing_n7_and_two_cells_effect_2026_10_17.md | L |
| 629 | repo | results/readout/run/_corpus_index_citation_surface_annotation_2026_10_12.md | 28951 | `402b1f2754e9` | verdict/pi | verdict/pi/_corpus_index_citation_surface_annotation_2026_10_12.md | L |
| 630 | repo | results/readout/run/_d9_runner_input_relpath_erratum_2026_10_12.md | 23592 | `7395034a09aa` | verdict/pi | verdict/pi/_d9_runner_input_relpath_erratum_2026_10_12.md | L |
| 631 | repo | results/readout/run/_h_face_external_evidence_eval_2026_10_18.md | 35016 | `22cbba5aefb8` | readout/final | readout/final/_h_face_external_evidence_eval_2026_10_18.md | L |
| 632 | repo | results/readout/run/_v148_four_points_erratum_draft_2026_10_20.md | 53088 | `524865bdc941` | readout/final | readout/final/_v148_four_points_erratum_draft_2026_10_20.md | L |
| 633 | repo | results/readout/run/_v3_construct_degradation_diag_2026_09_23.json | 11609 | `c8d539a58d29` | readout/final | readout/final/_v3_construct_degradation_diag_2026_09_23.json | L |
| 634 | repo | results/readout/run/_v3_n_cpath_live_data_2026_09_27.json | 12711 | `25374af92f88` | readout/final | readout/final/_v3_n_cpath_live_data_2026_09_27.json | L |
| 635 | repo | results/readout/run/_v3_n_ktb1_distortion_bound_data_2026_09_27.json | 6411 | `26c0d0b0ffb6` | readout/final | readout/final/_v3_n_ktb1_distortion_bound_data_2026_09_27.json | L |
| 636 | repo | results/readout/run/_v3_n_pg_boss_live_data_2026_09_27.json | 9220 | `be11c5274807` | readout/final | readout/final/_v3_n_pg_boss_live_data_2026_09_27.json | L |
| 637 | repo | results/readout/run/_v3_recheck_01_rescript_2026_09_27.md | 14541 | `a3c95102290f` | verdict/kd | verdict/kd/_v3_recheck_01_rescript_2026_09_27.md | L |
| 638 | repo | results/readout/run/_v3_recheck_01_result_2026_09_27.json | 167831 | `c19e2ab24e63` | readout/final | readout/final/_v3_recheck_01_result_2026_09_27.json | L |
| 639 | repo | results/readout/run/_v3_recheck_04_rescript_2026_09_27.md | 14780 | `34099595fe75` | verdict/pi | verdict/pi/_v3_recheck_04_rescript_2026_09_27.md | L |
| 640 | repo | results/readout/run/_v3_recheck_04_result_2026_09_27.json | 840158 | `db8cfb974ce3` | readout/final | readout/final/_v3_recheck_04_result_2026_09_27.json | L |
| 641 | repo | results/readout/run/_v3_recheck_05_rescript_2026_09_28.md | 22178 | `88b7eaf8675d` | verdict/kd | verdict/kd/_v3_recheck_05_rescript_2026_09_28.md | L |
| 642 | repo | results/readout/run/_v3_recheck_05_result_2026_09_28.json | 450751 | `81460acbb4f9` | readout/final | readout/final/_v3_recheck_05_result_2026_09_28.json | L |
| 643 | repo | results/readout/run/_v3_recheck_08_rescript_2026_09_27.md | 10459 | `2e08b9ae9f09` | verdict/kd | verdict/kd/_v3_recheck_08_rescript_2026_09_27.md | L |
| 644 | repo | results/readout/run/_v3_recheck_08_result_2026_09_27.json | 10587 | `0d2af01086db` | readout/final | readout/final/_v3_recheck_08_result_2026_09_27.json | L |
| 645 | repo | results/readout/run/_v3_recheck_10_rescript_2026_09_27.md | 14445 | `fc0ffd27adca` | verdict/kd | verdict/kd/_v3_recheck_10_rescript_2026_09_27.md | L |
| 646 | repo | results/readout/run/_v3_recheck_10_result_2026_09_27.json | 82535 | `5d4b6baf1b18` | readout/final | readout/final/_v3_recheck_10_result_2026_09_27.json | L |
| 647 | repo | results/readout/run/_v3_recheck_12_jsv_check_2026_09_27.md | 15821 | `c5eab30e9fc6` | verdict/kd | verdict/kd/_v3_recheck_12_jsv_check_2026_09_27.md | L |
| 648 | repo | results/readout/run/_v3_recheck_12_rescript_2026_09_27.md | 21222 | `776c86c735f8` | verdict/kd | verdict/kd/_v3_recheck_12_rescript_2026_09_27.md | L |
| 649 | repo | results/readout/run/_v3_recheck_12_result_2026_09_27.json | 187612 | `cdb37ed0b32f` | readout/final | readout/final/_v3_recheck_12_result_2026_09_27.json | L |
| 650 | repo | results/readout/run/_v3_recheck_12_rj5_provenance_2026_09_27.md | 23822 | `20f15c49feb5` | readout/final | readout/final/_v3_recheck_12_rj5_provenance_2026_09_27.md | L |
| 651 | repo | results/readout/run/_v3_recheck_19_rescript_2026_09_27.md | 11089 | `82a947f2aebd` | verdict/kd | verdict/kd/_v3_recheck_19_rescript_2026_09_27.md | L |
| 652 | repo | results/readout/run/_v3_recheck_19_result_2026_09_27.json | 59888 | `df07cf80930f` | readout/final | readout/final/_v3_recheck_19_result_2026_09_27.json | L |
| 653 | repo | results/readout/run/_v3_recheck_21_rescript_2026_09_27.md | 14618 | `04f6ecd482b9` | verdict/kd | verdict/kd/_v3_recheck_21_rescript_2026_09_27.md | L |
| 654 | repo | results/readout/run/_v3_recheck_21_result_2026_09_27.json | 44928 | `354ae9c14fe2` | readout/final | readout/final/_v3_recheck_21_result_2026_09_27.json | L |
| 655 | repo | results/readout/run/_v3_recheck_26_preexp_data_2026_09_27.json | 94658 | `177c88e1bd82` | readout/final | readout/final/_v3_recheck_26_preexp_data_2026_09_27.json | L |
| 656 | repo | results/readout/run/_v3_recheck_26_preexp_report_2026_09_27.md | 23048 | `a46230e344af` | verdict/judge | verdict/judge/_v3_recheck_26_preexp_report_2026_09_27.md | L |
| 657 | repo | results/readout/run/_v3_recheck_26_rescript_2026_09_27.md | 13747 | `6b86576146a3` | verdict/kd | verdict/kd/_v3_recheck_26_rescript_2026_09_27.md | L |
| 658 | repo | results/readout/run/_v3_recheck_26_result_2026_09_27.json | 11994 | `eb6a99dd46dd` | readout/final | readout/final/_v3_recheck_26_result_2026_09_27.json | L |
| 659 | repo | results/readout/run/_v3_recheck_26b_r3_result_2026_09_29.json | 54294 | `c9d3c9f819f1` | readout/final | readout/final/_v3_recheck_26b_r3_result_2026_09_29.json | L |
| 660 | repo | results/readout/run/_v3_recheck_26b_rescript_2026_09_27.md | 30552 | `ae81d9b59054` | verdict/pi | verdict/pi/_v3_recheck_26b_rescript_2026_09_27.md | L |
| 661 | repo | results/readout/run/_v3_recheck_26b_result_2026_09_27.json | 44379 | `49c6e5a07732` | readout/final | readout/final/_v3_recheck_26b_result_2026_09_27.json | L |
| 662 | repo | results/readout/run/_v3_recheck_27_rescript_2026_09_27.md | 14599 | `6f045bdc70e7` | verdict/kd | verdict/kd/_v3_recheck_27_rescript_2026_09_27.md | L |
| 663 | repo | results/readout/run/_v3_recheck_27_result_2026_09_27.json | 42571 | `e06cb51fb3af` | readout/final | readout/final/_v3_recheck_27_result_2026_09_27.json | L |
| 664 | repo | results/readout/run/_v3_recheck_28_rescript_2026_09_27.md | 10187 | `a0734e0a6860` | verdict/kd | verdict/kd/_v3_recheck_28_rescript_2026_09_27.md | L |
| 665 | repo | results/readout/run/_v3_recheck_28_result_2026_09_27.json | 26113 | `c0a8cb9029a7` | readout/final | readout/final/_v3_recheck_28_result_2026_09_27.json | L |
| 666 | repo | results/readout/run/_v3_recheck_35_rescript_2026_09_27.md | 13211 | `138faf395f40` | verdict/kd | verdict/kd/_v3_recheck_35_rescript_2026_09_27.md | L |
| 667 | repo | results/readout/run/_v3_recheck_35_result_2026_09_27.json | 35091 | `a8a4befb21f5` | readout/final | readout/final/_v3_recheck_35_result_2026_09_27.json | L |
| 668 | repo | results/readout/run/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md | 10288 | `55cd332f66f2` | readout/final | readout/final/_v3_v4_achievements_inventory_3dir_erratum_2026_09_24.md | L |
| 669 | repo | results/readout/run/_v3_v4_ghostref_reconciliation_2026_09_23.md | 169864 | `1d52db0ebf53` | verdict/judge | verdict/judge/_v3_v4_ghostref_reconciliation_2026_09_23.md | L |
| 670 | repo | results/readout/run/_v3n_cpath_live_rerun_2026_10_01.json | 60012 | `7c26d08ece3b` | readout/final | readout/final/_v3n_cpath_live_rerun_2026_10_01.json | L |
| 671 | repo | results/readout/run/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md | 9570 | `183205baa9ac` | doc/readme | doc/readme/_v3x_p_l_v3_summary_mistral_large_2512_20260917_115049.md | L |
| 672 | repo | results/readout/run/_v4_day_inventory_2026_09_27.md | 40487 | `7662d5058a7d` | verdict/pi | verdict/pi/_v4_day_inventory_2026_09_27.md | L |
| 673 | repo | results/readout/run/_v4_exec_surface_switch_2026_09_28.md | 28506 | `3bc852e0d48b` | verdict/pi | verdict/pi/_v4_exec_surface_switch_2026_09_28.md | L |
| 674 | repo | results/readout/run/_v4_maindir_count_monitor_2026_09_27.md | 15313 | `71e9cc179bec` | verdict/pi | verdict/pi/_v4_maindir_count_monitor_2026_09_27.md | L |
| 675 | repo | results/readout/run/_v4_supp_l14v3_batch10_r1_result.json | 68329 | `14dddb13d658` | readout/final | readout/final/_v4_supp_l14v3_batch10_r1_result.json | L |
| 676 | repo | results/readout/run/_v4_supp_l14v3_batch10_r2_result.json | 69460 | `400ee4d21fc9` | readout/final | readout/final/_v4_supp_l14v3_batch10_r2_result.json | L |
| 677 | repo | results/readout/run/_v4_supp_l14v3_batch10_r3_result.json | 70658 | `88a06f08928f` | readout/final | readout/final/_v4_supp_l14v3_batch10_r3_result.json | L |
| 678 | repo | results/readout/run/_v4_supp_l14v3_batch10_r4_result.json | 74733 | `9d91a8dc039a` | readout/final | readout/final/_v4_supp_l14v3_batch10_r4_result.json | L |
| 679 | repo | results/readout/run/_v4_supp_l14v3_batch10_r5_result.json | 74979 | `7f02e08fc0da` | readout/final | readout/final/_v4_supp_l14v3_batch10_r5_result.json | L |
| 680 | repo | results/readout/run/_v4_supp_l14v3_batch1_r2_result.json | 40815 | `00c7b545c397` | readout/final | readout/final/_v4_supp_l14v3_batch1_r2_result.json | L |
| 681 | repo | results/readout/run/_v4_supp_l14v3_batch1_r3_result.json | 44888 | `6e01255b80c9` | readout/final | readout/final/_v4_supp_l14v3_batch1_r3_result.json | L |
| 682 | repo | results/readout/run/_v4_supp_l14v3_batch1_r4_result.json | 46927 | `9c800874701a` | readout/final | readout/final/_v4_supp_l14v3_batch1_r4_result.json | L |
| 683 | repo | results/readout/run/_v4_supp_l14v3_batch1_r5_result.json | 67897 | `664355f29ab9` | readout/final | readout/final/_v4_supp_l14v3_batch1_r5_result.json | L |
| 684 | repo | results/readout/run/_v4_supp_l14v3_batch1_r6_result.json | 57925 | `6b92bbff7180` | readout/final | readout/final/_v4_supp_l14v3_batch1_r6_result.json | L |
| 685 | repo | results/readout/run/_v4_supp_l14v3_batch1_result.json | 46518 | `22eb01144062` | readout/final | readout/final/_v4_supp_l14v3_batch1_result.json | L |
| 686 | repo | results/readout/run/_v4_supp_l14v3_batch2_r1_result.json | 4128 | `d245ae4ce385` | readout/final | readout/final/_v4_supp_l14v3_batch2_r1_result.json | L |
| 687 | repo | results/readout/run/_v4_supp_l14v3_batch2_r2_result.json | 62887 | `8c125e257af8` | readout/final | readout/final/_v4_supp_l14v3_batch2_r2_result.json | L |
| 688 | repo | results/readout/run/_v4_supp_l14v3_batch2_r3_result.json | 62886 | `25251aca6d79` | readout/final | readout/final/_v4_supp_l14v3_batch2_r3_result.json | L |
| 689 | repo | results/readout/run/_v4_supp_l14v3_batch2_r4_result.json | 63572 | `15b8ddc5ba9e` | readout/final | readout/final/_v4_supp_l14v3_batch2_r4_result.json | L |
| 690 | repo | results/readout/run/_v4_supp_l14v3_batch2_r5_result.json | 64285 | `479f4119cf72` | readout/final | readout/final/_v4_supp_l14v3_batch2_r5_result.json | L |
| 691 | repo | results/readout/run/_v4_supp_l14v3_batch2_r6_result.json | 65083 | `e37d9c74c3e5` | readout/final | readout/final/_v4_supp_l14v3_batch2_r6_result.json | L |
| 692 | repo | results/readout/run/_v4_supp_l14v3_batch3_r1_result.json | 66520 | `d24b84671c23` | readout/final | readout/final/_v4_supp_l14v3_batch3_r1_result.json | L |
| 693 | repo | results/readout/run/_v4_supp_l14v3_batch3_r2_result.json | 67767 | `58e9c55a770d` | readout/final | readout/final/_v4_supp_l14v3_batch3_r2_result.json | L |
| 694 | repo | results/readout/run/_v4_supp_l14v3_batch3_r3_result.json | 68488 | `6e677ffcc880` | readout/final | readout/final/_v4_supp_l14v3_batch3_r3_result.json | L |
| 695 | repo | results/readout/run/_v4_supp_l14v3_batch3_r4_result.json | 69635 | `0e47768640d3` | readout/final | readout/final/_v4_supp_l14v3_batch3_r4_result.json | L |
| 696 | repo | results/readout/run/_v4_supp_l14v3_batch3_r5_result.json | 70064 | `38998f994b84` | readout/final | readout/final/_v4_supp_l14v3_batch3_r5_result.json | L |
| 697 | repo | results/readout/run/_v4_supp_l14v3_batch4_r1_result.json | 71775 | `7d9fe9d319a2` | readout/final | readout/final/_v4_supp_l14v3_batch4_r1_result.json | L |
| 698 | repo | results/readout/run/_v4_supp_l14v3_batch4_r2_result.json | 71998 | `6a9a362d9869` | readout/final | readout/final/_v4_supp_l14v3_batch4_r2_result.json | L |
| 699 | repo | results/readout/run/_v4_supp_l14v3_batch4_r3_result.json | 72884 | `ed5267df7d6f` | readout/final | readout/final/_v4_supp_l14v3_batch4_r3_result.json | L |
| 700 | repo | results/readout/run/_v4_supp_l14v3_batch4_r4_result.json | 74448 | `41e0ba55e205` | readout/final | readout/final/_v4_supp_l14v3_batch4_r4_result.json | L |
| 701 | repo | results/readout/run/_v4_supp_l14v3_batch4_r5_result.json | 76138 | `bad01f2b89fd` | readout/final | readout/final/_v4_supp_l14v3_batch4_r5_result.json | L |
| 702 | repo | results/readout/run/_v4_supp_l14v3_batch4_r6_result.json | 32369 | `6b8093ff8962` | readout/final | readout/final/_v4_supp_l14v3_batch4_r6_result.json | L |
| 703 | repo | results/readout/run/_v4_supp_l14v3_batch5_r1_result.json | 71021 | `120d45d1774f` | readout/final | readout/final/_v4_supp_l14v3_batch5_r1_result.json | L |
| 704 | repo | results/readout/run/_v4_supp_l14v3_batch5_r2_result.json | 72550 | `b0f76b5c3522` | readout/final | readout/final/_v4_supp_l14v3_batch5_r2_result.json | L |
| 705 | repo | results/readout/run/_v4_supp_l14v3_batch5_r3_result.json | 73682 | `8e2acdacfa1e` | readout/final | readout/final/_v4_supp_l14v3_batch5_r3_result.json | L |
| 706 | repo | results/readout/run/_v4_supp_l14v3_batch5_r4_result.json | 74100 | `1c62520c372b` | readout/final | readout/final/_v4_supp_l14v3_batch5_r4_result.json | L |
| 707 | repo | results/readout/run/_v4_supp_l14v3_batch5_r5_result.json | 77137 | `c874d21a4cbe` | readout/final | readout/final/_v4_supp_l14v3_batch5_r5_result.json | L |
| 708 | repo | results/readout/run/_v4_supp_l14v3_batch6_r1_result.json | 57799 | `0d29e1ab4ae2` | readout/final | readout/final/_v4_supp_l14v3_batch6_r1_result.json | L |
| 709 | repo | results/readout/run/_v4_supp_l14v3_batch6_r2_result.json | 64672 | `96e1de46ed30` | readout/final | readout/final/_v4_supp_l14v3_batch6_r2_result.json | L |
| 710 | repo | results/readout/run/_v4_supp_l14v3_batch6_r3_result.json | 64975 | `15a7fecdffe7` | readout/final | readout/final/_v4_supp_l14v3_batch6_r3_result.json | L |
| 711 | repo | results/readout/run/_v4_supp_l14v3_batch6_r4_result.json | 65254 | `b7377ba019a1` | readout/final | readout/final/_v4_supp_l14v3_batch6_r4_result.json | L |
| 712 | repo | results/readout/run/_v4_supp_l14v3_batch6_r5_result.json | 65651 | `e40424bf8abe` | readout/final | readout/final/_v4_supp_l14v3_batch6_r5_result.json | L |
| 713 | repo | results/readout/run/_v4_supp_l14v3_batch7_r1_result.json | 61114 | `3558a1d15867` | readout/final | readout/final/_v4_supp_l14v3_batch7_r1_result.json | L |
| 714 | repo | results/readout/run/_v4_supp_l14v3_batch7_r2_result.json | 61458 | `924f12c4e7ab` | readout/final | readout/final/_v4_supp_l14v3_batch7_r2_result.json | L |
| 715 | repo | results/readout/run/_v4_supp_l14v3_batch7_r3_result.json | 61389 | `b431a1ba54df` | readout/final | readout/final/_v4_supp_l14v3_batch7_r3_result.json | L |
| 716 | repo | results/readout/run/_v4_supp_l14v3_batch7_r4_result.json | 61824 | `0fe4c1339d88` | readout/final | readout/final/_v4_supp_l14v3_batch7_r4_result.json | L |
| 717 | repo | results/readout/run/_v4_supp_l14v3_batch7_r5_result.json | 61658 | `09a481ebca6b` | readout/final | readout/final/_v4_supp_l14v3_batch7_r5_result.json | L |
| 718 | repo | results/readout/run/_v4_supp_l14v3_batch8_r1_result.json | 62531 | `e6a94a0a13b7` | readout/final | readout/final/_v4_supp_l14v3_batch8_r1_result.json | L |
| 719 | repo | results/readout/run/_v4_supp_l14v3_batch8_r2_result.json | 63440 | `7b23996b5f4c` | readout/final | readout/final/_v4_supp_l14v3_batch8_r2_result.json | L |
| 720 | repo | results/readout/run/_v4_supp_l14v3_batch8_r3_result.json | 63670 | `56faf9324fba` | readout/final | readout/final/_v4_supp_l14v3_batch8_r3_result.json | L |
| 721 | repo | results/readout/run/_v4_supp_l14v3_batch8_r4_result.json | 64038 | `c7d5aa2a9b00` | readout/final | readout/final/_v4_supp_l14v3_batch8_r4_result.json | L |
| 722 | repo | results/readout/run/_v4_supp_l14v3_batch8_r5_result.json | 63785 | `3620a7daf9c1` | readout/final | readout/final/_v4_supp_l14v3_batch8_r5_result.json | L |
| 723 | repo | results/readout/run/_v4_supp_l14v3_batch9_r1_result.json | 69251 | `7e8dfe0156cd` | readout/final | readout/final/_v4_supp_l14v3_batch9_r1_result.json | L |
| 724 | repo | results/readout/run/_v4_supp_l14v3_batch9_r2_result.json | 69325 | `08b0aaaae726` | readout/final | readout/final/_v4_supp_l14v3_batch9_r2_result.json | L |
| 725 | repo | results/readout/run/_v4_supp_l14v3_batch9_r3_result.json | 69984 | `29e0d865a7bf` | readout/final | readout/final/_v4_supp_l14v3_batch9_r3_result.json | L |
| 726 | repo | results/readout/run/_v4_supp_l14v3_batch9_r4_result.json | 71093 | `eb8b13d9f592` | readout/final | readout/final/_v4_supp_l14v3_batch9_r4_result.json | L |
| 727 | repo | results/readout/run/_v4_supp_l14v3_batch9_r5_result.json | 72047 | `1610f5060ef1` | readout/final | readout/final/_v4_supp_l14v3_batch9_r5_result.json | L |
| 728 | repo | results/readout/run/_v4_supp_t15_result.json | 53265 | `6b47d389b7ae` | readout/final | readout/final/_v4_supp_t15_result.json | L |
| 729 | repo | results/readout/run/_v4_supp_t15r2_result.json | 73526 | `c69ab0e3002e` | readout/final | readout/final/_v4_supp_t15r2_result.json | L |
| 730 | repo | results/readout/run/_v4_supp_t1_result.json | 82365 | `d6cb03a4657e` | readout/final | readout/final/_v4_supp_t1_result.json | L |
| 731 | repo | results/readout/run/_v5_b15_pp1_impl_fix_2026_09_29.md | 12911 | `ded842b6241c` | verdict/kd | verdict/kd/_v5_b15_pp1_impl_fix_2026_09_29.md | L |
| 732 | repo | results/readout/run/_v5_bulk_activation_2026_09_28.md | 39378 | `b5a50447b4da` | verdict/pi | verdict/pi/_v5_bulk_activation_2026_09_28.md | L |
| 733 | repo | results/readout/run/_v5_clearance_mr14_rerun_note_2026_09_29.md | 22894 | `f3dd5efd3e34` | verdict/pi | verdict/pi/_v5_clearance_mr14_rerun_note_2026_09_29.md | L |
| 734 | repo | results/readout/run/_v5_gt4_reattrib_2026_09_29.json | 3074 | `4b75df5f7454` | readout/final | readout/final/_v5_gt4_reattrib_2026_09_29.json | L |
| 735 | repo | results/readout/run/_v5_gt5_reattrib_2026_09_29.json | 5626 | `e15b3b171d60` | readout/final | readout/final/_v5_gt5_reattrib_2026_09_29.json | L |
| 736 | repo | results/readout/run/_v5_gt5b_reattrib_2026_09_29.json | 7084 | `212e5bb8c7d7` | readout/final | readout/final/_v5_gt5b_reattrib_2026_09_29.json | L |
| 737 | repo | results/readout/run/_v5_gt6_trajint_2026_09_29.json | 83722 | `578fbeaa4635` | readout/final | readout/final/_v5_gt6_trajint_2026_09_29.json | L |
| 738 | repo | results/readout/run/_v5_gt8_expand_2026_09_29.json | 20090 | `34ff826f97c2` | readout/final | readout/final/_v5_gt8_expand_2026_09_29.json | L |
| 739 | repo | results/readout/run/_v5_gt8_lowarm_result_2026_09_29.json | 26253 | `c68076c88140` | readout/final | readout/final/_v5_gt8_lowarm_result_2026_09_29.json | L |
| 740 | repo | results/readout/run/_v5_gt8_lowarm_resultb_2026_09_29.json | 48948 | `8aa69a5e922d` | readout/final | readout/final/_v5_gt8_lowarm_resultb_2026_09_29.json | L |
| 741 | repo | results/readout/run/_v5_gt8_lowarm_seta_verify_2026_09_29.json | 9001 | `d1370b0a3853` | readout/final | readout/final/_v5_gt8_lowarm_seta_verify_2026_09_29.json | L |
| 742 | repo | results/readout/run/_v5_gt_exec_2026_09_29.md | 27701 | `9a679f43f796` | verdict/kd | verdict/kd/_v5_gt_exec_2026_09_29.md | L |
| 743 | repo | results/readout/run/_v5_handover_guide_project_initiation_2026_10_12.md | 5580 | `dddf7b0a7221` | verdict/pi | verdict/pi/_v5_handover_guide_project_initiation_2026_10_12.md | L |
| 744 | repo | results/readout/run/_v5_item26b_attribution_effective_2026_09_28.md | 35261 | `c353fbcdc753` | verdict/kd | verdict/kd/_v5_item26b_attribution_effective_2026_09_28.md | L |
| 745 | repo | results/readout/run/_v5_item35_v2_matrix_exec_2026_09_29.md | 24624 | `4e88682284d8` | verdict/kd | verdict/kd/_v5_item35_v2_matrix_exec_2026_09_29.md | L |
| 746 | repo | results/readout/run/_v5_item35_v2_matrix_result_2026_09_29.json | 84699 | `13ad5b740f80` | readout/final | readout/final/_v5_item35_v2_matrix_result_2026_09_29.json | L |
| 747 | repo | results/readout/run/_v5_item35_v3_collinear_result_2026_09_29.json | 187287 | `99f3e504589e` | readout/final | readout/final/_v5_item35_v3_collinear_result_2026_09_29.json | L |
| 748 | repo | results/readout/run/_v5_pjpm_pc_degen_precheck_result_2026_09_29.json | 103747 | `3641afe9d49c` | readout/final | readout/final/_v5_pjpm_pc_degen_precheck_result_2026_09_29.json | L |
| 749 | repo | results/readout/run/_v5_theory_input_acquisition_request_2026_09_29.md | 10751 | `19099ecb3c46` | verdict/kd | verdict/kd/_v5_theory_input_acquisition_request_2026_09_29.md | L |
| 750 | repo | results/readout/run/_v5_v3_deg_fix_c1c4_result_2026_09_29.json | 266417 | `1b5bfecc818e` | readout/final | readout/final/_v5_v3_deg_fix_c1c4_result_2026_09_29.json | L |
| 751 | repo | results/readout/run/_v5_v3_deg_fix_exec_2026_09_29.md | 30261 | `7d885528f287` | readout/final | readout/final/_v5_v3_deg_fix_exec_2026_09_29.md | L |
| 752 | repo | results/readout/run/_v5_v3_deg_p1_reopen_result_2026_09_29.json | 571451 | `b86d6740d487` | readout/final | readout/final/_v5_v3_deg_p1_reopen_result_2026_09_29.json | L |
| 753 | repo | results/readout/run/_v5_v3_deg_reopen_line_2026_09_29.md | 42778 | `2ea1c2cee65d` | verdict/judge | verdict/judge/_v5_v3_deg_reopen_line_2026_09_29.md | L |
| 754 | repo | results/readout/run/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json | 21176 | `95f3f0957be8` | readout/final | readout/final/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json | L |
| 755 | repo | results/review/audit/_anchor_drift_authorized_adoption_2026_10_16.md | 25026 | `306b2cd2e0b6` | readout/final | readout/final/_anchor_drift_authorized_adoption_2026_10_16.md | L |
| 756 | repo | results/review/audit/_anchor_drift_migration_register_2026_10_21.md | 33121 | `e5fde6b405ee` | verdict/pi | verdict/pi/_anchor_drift_migration_register_2026_10_21.md | L |
| 757 | repo | results/review/audit/_anchor_drift_registration_correction_note_2026_10_21.md | 24781 | `1924cdbe1f40` | verdict/pi | verdict/pi/_anchor_drift_registration_correction_note_2026_10_21.md | L |
| 758 | repo | results/review/audit/_archive_manifest_non_upload_2026_09_23.json | 148690 | `b899103853ca` | readout/final | readout/final/_archive_manifest_non_upload_2026_09_23.json | L |
| 759 | repo | results/review/audit/_batch1_d4_d5_b1_errata_2026_10_12.md | 22871 | `5193321dbe61` | verdict/pi | verdict/pi/_batch1_d4_d5_b1_errata_2026_10_12.md | L |
| 760 | repo | results/review/audit/_collision_196_2026_10_12.json | 42490 | `3c95da787454` | readout/final | readout/final/_collision_196_2026_10_12.json | L |
| 761 | repo | results/review/audit/_collision_509_ruling_effect_2026_10_18.md | 1160 | `ef7a2a400412` | verdict/pi | verdict/pi/_collision_509_ruling_effect_2026_10_18.md | L |
| 762 | repo | results/review/audit/_collision_baseline_update_and_disposition_2026_10_17.md | 26197 | `f4f0fdc9915d` | verdict/pi | verdict/pi/_collision_baseline_update_and_disposition_2026_10_17.md | L |
| 763 | repo | results/review/audit/_fake_kd_p2_p7_reversal_errata_2026_10_21.md | 47276 | `2f2006f9a4ff` | verdict/kd | verdict/kd/_fake_kd_p2_p7_reversal_errata_2026_10_21.md | L |
| 764 | repo | results/review/audit/_fake_kd_p4_reversal_errata_2026_10_21.md | 84218 | `dcbc81cc92f8` | verdict/kd | verdict/kd/_fake_kd_p4_reversal_errata_2026_10_21.md | L |
| 765 | repo | results/review/audit/_fake_kd_p5_reversal_errata_2026_10_21.md | 59726 | `32fa2969ad44` | verdict/kd | verdict/kd/_fake_kd_p5_reversal_errata_2026_10_21.md | L |
| 766 | repo | results/review/audit/_ghost_reference_register_2026_10_21.md | 21235 | `e927dfce3464` | verdict/pi | verdict/pi/_ghost_reference_register_2026_10_21.md | L |
| 767 | repo | results/review/audit/_gitignore_rx_fix_drift_register_2026_10_17.md | 11747 | `bbb98cd5e9ce` | verdict/pi | verdict/pi/_gitignore_rx_fix_drift_register_2026_10_17.md | L |
| 768 | repo | results/review/audit/_harness_42b_drift_semantics_2026_10_19.md | 37904 | `49b2f5b27f34` | readout/final | readout/final/_harness_42b_drift_semantics_2026_10_19.md | L |
| 769 | repo | results/review/audit/_hidden_gaps_audit_full_history_2026_10_19.md | 6661 | `eccea2d276f1` | verdict/pi | verdict/pi/_hidden_gaps_audit_full_history_2026_10_19.md | L |
| 770 | repo | results/review/audit/_kt_a1_anchor_drift_root_cause_2026_10_14.md | 37430 | `ba19ab186747` | verdict/judge | verdict/judge/_kt_a1_anchor_drift_root_cause_2026_10_14.md | L |
| 771 | repo | results/review/audit/_material_expansion_drift_authorized_register_2026_10_16.md | 15044 | `edf98dc7da62` | verdict/pi | verdict/pi/_material_expansion_drift_authorized_register_2026_10_16.md | L |
| 772 | repo | results/review/audit/_memory_errata_register_2026_10_14.md | 10701 | `dbe9d0b16d14` | verdict/pi | verdict/pi/_memory_errata_register_2026_10_14.md | L |
| 773 | repo | results/review/audit/_mq20_errata_register_2026_10_14.md | 11441 | `8bb4bbc28c16` | verdict/pi | verdict/pi/_mq20_errata_register_2026_10_14.md | L |
| 774 | repo | results/review/audit/_ncc2_prereg_label_errata_note_2026_10_21.md | 39613 | `0c0439807cf8` | verdict/kd | verdict/kd/_ncc2_prereg_label_errata_note_2026_10_21.md | L |
| 775 | repo | results/review/audit/_numbering_system_audit_and_definition_2026_10_13.md | 44897 | `47f20fa27a62` | readout/final | readout/final/_numbering_system_audit_and_definition_2026_10_13.md | L |
| 776 | repo | results/review/audit/_one_finish_gap_audit_2026_10_17.md | 45582 | `1c713252e870` | readout/final | readout/final/_one_finish_gap_audit_2026_10_17.md | L |
| 777 | repo | results/review/audit/_q3_transposition_errata_2026_10_09.md | 11757 | `659c4101f10b` | readout/final | readout/final/_q3_transposition_errata_2026_10_09.md | L |
| 778 | repo | results/review/audit/_register_face_errata_2026_10_20.md | 22269 | `92d3068fca09` | verdict/pi | verdict/pi/_register_face_errata_2026_10_20.md | L |
| 779 | repo | results/review/audit/_remote_509_desensitization_direction_audit_2026_10_18.md | 65859 | `931751f30cae` | verdict/pi | verdict/pi/_remote_509_desensitization_direction_audit_2026_10_18.md | L |
| 780 | repo | results/review/audit/_s4_v31_drift_register_face1_2026_10_10.md | 11485 | `5ab168d82873` | verdict/pi | verdict/pi/_s4_v31_drift_register_face1_2026_10_10.md | L |
| 781 | repo | results/review/audit/_stage1_gap_exhaustive_audit_2026_10_20.md | 54167 | `cc00c068aa50` | verdict/judge | verdict/judge/_stage1_gap_exhaustive_audit_2026_10_20.md | L |
| 782 | repo | results/review/audit/_supplement_500_combo_drift_authorized_register_2026_10_16.md | 13742 | `71d2ef525d3b` | verdict/pi | verdict/pi/_supplement_500_combo_drift_authorized_register_2026_10_16.md | L |
| 783 | repo | results/review/audit/_t2_path_b_drift_authorized_register_2026_10_16.md | 10939 | `d07d33f0eb82` | verdict/pi | verdict/pi/_t2_path_b_drift_authorized_register_2026_10_16.md | L |
| 784 | repo | results/review/audit/_t3trap_answerable_drift_authorized_register_2026_10_15.md | 15196 | `aa8e9fce651c` | verdict/pi | verdict/pi/_t3trap_answerable_drift_authorized_register_2026_10_15.md | L |
| 785 | repo | results/review/audit/_t5_anchor_drift_authorized_register_2026_10_15.md | 11553 | `1308662a369a` | verdict/pi | verdict/pi/_t5_anchor_drift_authorized_register_2026_10_15.md | L |
| 786 | repo | results/review/audit/_thirdparty_collision_16_register_kimi_2026_10_18.md | 3959 | `58c0b02114ae` | verdict/pi | verdict/pi/_thirdparty_collision_16_register_kimi_2026_10_18.md | L |
| 787 | repo | results/review/audit/_trae_sixitem_disposal_and_collision_register_2026_10_01.md | 19268 | `545b17d403be` | verdict/pi | verdict/pi/_trae_sixitem_disposal_and_collision_register_2026_10_01.md | L |
| 788 | repo | results/tool/generator/_deliverable_pack_v2_selfextract_2026_10_21.py | 1431160 | `e3084c2f7716` | source/tool | source/tool/_deliverable_pack_v2_selfextract_2026_10_21.py | L |
| 789 | repo | results/tool/generator/_log_retention_purge_2026_10_13.py | 9401 | `8527db8d0ef7` | source/tool | source/tool/_log_retention_purge_2026_10_13.py | L |
| 790 | repo | results/tool/generator/_s4prime_five_lines_runner_2026_10_11.py | 29813 | `f784b2fc92f4` | source/tool | source/tool/_s4prime_five_lines_runner_2026_10_11.py | L |
| 791 | repo | results/tool/generator/_t1_exp2_executor_2026_10_09.py | 67955 | `ce393b41618c` | source/tool | source/tool/_t1_exp2_executor_2026_10_09.py | L |
| 792 | repo | results/tool/generator/_t1_qwen_temp_sweep_executor_2026_10_09.py | 32399 | `f0c845864603` | source/tool | source/tool/_t1_qwen_temp_sweep_executor_2026_10_09.py | L |
| 793 | repo | results/tool/generator/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py | 53184 | `38d0cf7fc9ba` | source/tool | source/tool/_t1_qwen_temp_sweep_r2_executor_2026_10_09.py | L |
| 794 | repo | results/tool/generator/_tmp_measure_c5b_register.py | 2807 | `77248d427f32` | source/tool | source/tool/_tmp_measure_c5b_register.py | L |
| 795 | repo | results/tool/generator/_tmp_write_copilot_register.py | 18397 | `bc87bbf099ef` | source/tool | source/tool/_tmp_write_copilot_register.py | L |
| 796 | repo | results/tool/generator/_tra_v0_2026_09_10.py | 12125 | `d80a8f75a122` | source/tool | source/tool/_tra_v0_2026_09_10.py | L |
| 797 | repo | results/tool/generator/_v3_recheck_01_executor_2026_09_27.py | 41004 | `919fa909381e` | source/tool | source/tool/_v3_recheck_01_executor_2026_09_27.py | L |
| 798 | repo | results/tool/generator/_v3_recheck_04_executor_2026_09_27.py | 49405 | `e098fa21700d` | source/tool | source/tool/_v3_recheck_04_executor_2026_09_27.py | L |
| 799 | repo | results/tool/generator/_v3_recheck_08_executor_2026_09_27.py | 15598 | `21c4ba4d479e` | source/tool | source/tool/_v3_recheck_08_executor_2026_09_27.py | L |
| 800 | repo | results/tool/generator/_v3_recheck_26_executor_2026_09_27.py | 15056 | `46c326c756c3` | source/tool | source/tool/_v3_recheck_26_executor_2026_09_27.py | L |
| 801 | repo | results/tool/generator/_v3_recheck_26_preexp_executor_2026_09_27.py | 38726 | `775217a462f5` | source/tool | source/tool/_v3_recheck_26_preexp_executor_2026_09_27.py | L |
| 802 | repo | results/tool/generator/_v3_recheck_26b_executor_2026_09_27.py | 43171 | `5c906113a210` | source/tool | source/tool/_v3_recheck_26b_executor_2026_09_27.py | L |
| 803 | repo | results/tool/generator/_v3_recheck_26b_executor_r2_2026_09_28.py | 52272 | `0808af6212c5` | source/tool | source/tool/_v3_recheck_26b_executor_r2_2026_09_28.py | L |
| 804 | repo | results/tool/generator/_v3_recheck_26b_executor_r3_2026_09_29.py | 64959 | `6c83e7a7ca2e` | source/tool | source/tool/_v3_recheck_26b_executor_r3_2026_09_29.py | L |
| 805 | repo | results/tool/generator/_v4_day_inventory_measure_2026_09_27.py | 8226 | `3e903f224f87` | source/tool | source/tool/_v4_day_inventory_measure_2026_09_27.py | L |
| 806 | repo | results/tool/generator/_v4_pi_cot_v2_ruleset_executor.py | 39281 | `48dca1d4281c` | source/tool | source/tool/_v4_pi_cot_v2_ruleset_executor.py | L |
| 807 | repo | results/tool/generator/_v4_pi_cot_v2_ruleset_v2_executor.py | 52465 | `eb22f13d571c` | source/tool | source/tool/_v4_pi_cot_v2_ruleset_v2_executor.py | L |
| 808 | repo | results/tool/generator/_v4_pi_cot_v3_ruleset_v3_executor.py | 58794 | `8a81d90c69ba` | source/tool | source/tool/_v4_pi_cot_v3_ruleset_v3_executor.py | L |
| 809 | repo | results/tool/generator/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py | 62115 | `ee8671a28c2f` | source/tool | source/tool/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py | L |
| 810 | repo | results/tool/generator/_v4_supp_l14v3_batch10_r1_executor.py | 56894 | `d4dd5c949443` | source/tool | source/tool/_v4_supp_l14v3_batch10_r1_executor.py | L |
| 811 | repo | results/tool/generator/_v4_supp_l14v3_batch10_r2_executor.py | 58073 | `bb601b4f5ecb` | source/tool | source/tool/_v4_supp_l14v3_batch10_r2_executor.py | L |
| 812 | repo | results/tool/generator/_v4_supp_l14v3_batch10_r3_executor.py | 58539 | `eef1475e325c` | source/tool | source/tool/_v4_supp_l14v3_batch10_r3_executor.py | L |
| 813 | repo | results/tool/generator/_v4_supp_l14v3_batch10_r4_executor.py | 68856 | `4f68937d7a95` | source/tool | source/tool/_v4_supp_l14v3_batch10_r4_executor.py | L |
| 814 | repo | results/tool/generator/_v4_supp_l14v3_batch1_executor.py | 29354 | `b48019494530` | source/tool | source/tool/_v4_supp_l14v3_batch1_executor.py | L |
| 815 | repo | results/tool/generator/_v4_supp_l14v3_batch1_r2_executor.py | 29598 | `2bdb5163400f` | source/tool | source/tool/_v4_supp_l14v3_batch1_r2_executor.py | L |
| 816 | repo | results/tool/generator/_v4_supp_l14v3_batch1_r3_executor.py | 43289 | `60c78b6f0281` | source/tool | source/tool/_v4_supp_l14v3_batch1_r3_executor.py | L |
| 817 | repo | results/tool/generator/_v4_supp_l14v3_batch1_r4_executor.py | 46811 | `4f5269ba8f18` | source/tool | source/tool/_v4_supp_l14v3_batch1_r4_executor.py | L |
| 818 | repo | results/tool/generator/_v4_supp_l14v3_batch1_r5_executor.py | 49138 | `91c72f8ad209` | source/tool | source/tool/_v4_supp_l14v3_batch1_r5_executor.py | L |
| 819 | repo | results/tool/generator/_v4_supp_l14v3_batch1_r6_executor.py | 47242 | `5f02c7e0f094` | source/tool | source/tool/_v4_supp_l14v3_batch1_r6_executor.py | L |
| 820 | repo | results/tool/generator/_v4_supp_l14v3_batch2_r1_executor.py | 50808 | `e52f930654d3` | source/tool | source/tool/_v4_supp_l14v3_batch2_r1_executor.py | L |
| 821 | repo | results/tool/generator/_v4_supp_l14v3_batch2_r2_executor.py | 55317 | `e7418f47a130` | source/tool | source/tool/_v4_supp_l14v3_batch2_r2_executor.py | L |
| 822 | repo | results/tool/generator/_v4_supp_l14v3_batch2_r3_executor.py | 56467 | `72fd2bb3838e` | source/tool | source/tool/_v4_supp_l14v3_batch2_r3_executor.py | L |
| 823 | repo | results/tool/generator/_v4_supp_l14v3_batch2_r4_executor.py | 58176 | `d9fe7aa2d292` | source/tool | source/tool/_v4_supp_l14v3_batch2_r4_executor.py | L |
| 824 | repo | results/tool/generator/_v4_supp_l14v3_batch2_r5_executor.py | 60046 | `bf1e4fe02402` | source/tool | source/tool/_v4_supp_l14v3_batch2_r5_executor.py | L |
| 825 | repo | results/tool/generator/_v4_supp_l14v3_batch3_r1_executor.py | 61899 | `0c284a3dce21` | source/tool | source/tool/_v4_supp_l14v3_batch3_r1_executor.py | L |
| 826 | repo | results/tool/generator/_v4_supp_l14v3_batch3_r2_executor.py | 64634 | `b1699098c53b` | source/tool | source/tool/_v4_supp_l14v3_batch3_r2_executor.py | L |
| 827 | repo | results/tool/generator/_v4_supp_l14v3_batch3_r3_executor.py | 66396 | `3b7381ce5fe8` | source/tool | source/tool/_v4_supp_l14v3_batch3_r3_executor.py | L |
| 828 | repo | results/tool/generator/_v4_supp_l14v3_batch3_r4_executor.py | 68874 | `c79b5c274a10` | source/tool | source/tool/_v4_supp_l14v3_batch3_r4_executor.py | L |
| 829 | repo | results/tool/generator/_v4_supp_l14v3_batch4_r1_executor.py | 66097 | `e84bffd5dc7d` | source/tool | source/tool/_v4_supp_l14v3_batch4_r1_executor.py | L |
| 830 | repo | results/tool/generator/_v4_supp_l14v3_batch4_r2_executor.py | 66774 | `7d8e12267790` | source/tool | source/tool/_v4_supp_l14v3_batch4_r2_executor.py | L |
| 831 | repo | results/tool/generator/_v4_supp_l14v3_batch4_r3_executor.py | 68560 | `b5e1c3637405` | source/tool | source/tool/_v4_supp_l14v3_batch4_r3_executor.py | L |
| 832 | repo | results/tool/generator/_v4_supp_l14v3_batch4_r4_executor.py | 73379 | `184186902a9f` | source/tool | source/tool/_v4_supp_l14v3_batch4_r4_executor.py | L |
| 833 | repo | results/tool/generator/_v4_supp_l14v3_batch4_r5_executor.py | 78984 | `8a505613b476` | source/tool | source/tool/_v4_supp_l14v3_batch4_r5_executor.py | L |
| 834 | repo | results/tool/generator/_v4_supp_l14v3_batch4_r6_executor.py | 80877 | `7f2c5e26e6c5` | source/tool | source/tool/_v4_supp_l14v3_batch4_r6_executor.py | L |
| 835 | repo | results/tool/generator/_v4_supp_l14v3_batch5_r1_executor.py | 63517 | `dac0648507b9` | source/tool | source/tool/_v4_supp_l14v3_batch5_r1_executor.py | L |
| 836 | repo | results/tool/generator/_v4_supp_l14v3_batch5_r2_executor.py | 66252 | `4c40334929bb` | source/tool | source/tool/_v4_supp_l14v3_batch5_r2_executor.py | L |
| 837 | repo | results/tool/generator/_v4_supp_l14v3_batch5_r3_executor.py | 66454 | `ed9557830f8b` | source/tool | source/tool/_v4_supp_l14v3_batch5_r3_executor.py | L |
| 838 | repo | results/tool/generator/_v4_supp_l14v3_batch5_r4_executor.py | 67894 | `28844c34b12b` | source/tool | source/tool/_v4_supp_l14v3_batch5_r4_executor.py | L |
| 839 | repo | results/tool/generator/_v4_supp_l14v3_batch5_r5_executor.py | 77033 | `82c283d8f37a` | source/tool | source/tool/_v4_supp_l14v3_batch5_r5_executor.py | L |
| 840 | repo | results/tool/generator/_v4_supp_l14v3_batch6_r1_executor.py | 49296 | `ad35565f1ec9` | source/tool | source/tool/_v4_supp_l14v3_batch6_r1_executor.py | L |
| 841 | repo | results/tool/generator/_v4_supp_l14v3_batch6_r2_executor.py | 53494 | `93c931fc3b1c` | source/tool | source/tool/_v4_supp_l14v3_batch6_r2_executor.py | L |
| 842 | repo | results/tool/generator/_v4_supp_l14v3_batch6_r3_executor.py | 53717 | `1385d2ca356f` | source/tool | source/tool/_v4_supp_l14v3_batch6_r3_executor.py | L |
| 843 | repo | results/tool/generator/_v4_supp_l14v3_batch6_r4_executor.py | 54588 | `08f329b36e9d` | source/tool | source/tool/_v4_supp_l14v3_batch6_r4_executor.py | L |
| 844 | repo | results/tool/generator/_v4_supp_l14v3_batch6_r5_executor.py | 57783 | `8a8babb911b8` | source/tool | source/tool/_v4_supp_l14v3_batch6_r5_executor.py | L |
| 845 | repo | results/tool/generator/_v4_supp_l14v3_batch7_r1_executor.py | 51545 | `c49fc9bca8c4` | source/tool | source/tool/_v4_supp_l14v3_batch7_r1_executor.py | L |
| 846 | repo | results/tool/generator/_v4_supp_l14v3_batch7_r2_executor.py | 53145 | `35cda0c0f7da` | source/tool | source/tool/_v4_supp_l14v3_batch7_r2_executor.py | L |
| 847 | repo | results/tool/generator/_v4_supp_l14v3_batch7_r3_executor.py | 51271 | `5c0b426e2ee0` | source/tool | source/tool/_v4_supp_l14v3_batch7_r3_executor.py | L |
| 848 | repo | results/tool/generator/_v4_supp_l14v3_batch7_r4_executor.py | 51289 | `d789f9bd4fa1` | source/tool | source/tool/_v4_supp_l14v3_batch7_r4_executor.py | L |
| 849 | repo | results/tool/generator/_v4_supp_l14v3_batch8_r1_executor.py | 56181 | `1e5f2249c517` | source/tool | source/tool/_v4_supp_l14v3_batch8_r1_executor.py | L |
| 850 | repo | results/tool/generator/_v4_supp_l14v3_batch8_r2_executor.py | 57634 | `6a9bbc43c808` | source/tool | source/tool/_v4_supp_l14v3_batch8_r2_executor.py | L |
| 851 | repo | results/tool/generator/_v4_supp_l14v3_batch8_r3_executor.py | 58494 | `0f654d945f12` | source/tool | source/tool/_v4_supp_l14v3_batch8_r3_executor.py | L |
| 852 | repo | results/tool/generator/_v4_supp_l14v3_batch8_r4_executor.py | 59351 | `6b69ec8406d4` | source/tool | source/tool/_v4_supp_l14v3_batch8_r4_executor.py | L |
| 853 | repo | results/tool/generator/_v4_supp_l14v3_batch8_r5_executor.py | 60475 | `6961281824ae` | source/tool | source/tool/_v4_supp_l14v3_batch8_r5_executor.py | L |
| 854 | repo | results/tool/generator/_v4_supp_l14v3_batch9_r1_executor.py | 60645 | `e78ca71bd077` | source/tool | source/tool/_v4_supp_l14v3_batch9_r1_executor.py | L |
| 855 | repo | results/tool/generator/_v4_supp_l14v3_batch9_r2_executor.py | 60580 | `7eec235a9ca2` | source/tool | source/tool/_v4_supp_l14v3_batch9_r2_executor.py | L |
| 856 | repo | results/tool/generator/_v4_supp_l14v3_batch9_r3_executor.py | 62131 | `cfe41dd4fe62` | source/tool | source/tool/_v4_supp_l14v3_batch9_r3_executor.py | L |
| 857 | repo | results/tool/generator/_v4_supp_l14v3_batch9_r4_executor.py | 64538 | `1b3fcfbacd59` | source/tool | source/tool/_v4_supp_l14v3_batch9_r4_executor.py | L |
| 858 | repo | results/tool/generator/_v4_supp_t15_executor.py | 62285 | `558e635f9ba6` | source/tool | source/tool/_v4_supp_t15_executor.py | L |
| 859 | repo | results/tool/generator/_v4_supp_t15_executor_r0_atomic_2026_09_29.py | 66317 | `7da23c0e94cf` | source/tool | source/tool/_v4_supp_t15_executor_r0_atomic_2026_09_29.py | L |
| 860 | repo | results/tool/generator/_v4_supp_t15_executor_r1_2026_09_27.py | 67517 | `6d22444c65af` | source/tool | source/tool/_v4_supp_t15_executor_r1_2026_09_27.py | L |
| 861 | repo | results/tool/generator/_v4_supp_t15_executor_r2_atomic_2026_09_28.py | 70056 | `9e89e021ea03` | source/tool | source/tool/_v4_supp_t15_executor_r2_atomic_2026_09_28.py | L |
| 862 | repo | results/tool/generator/_v4_supp_t15_executor_r3_2026_09_28.py | 70056 | `b86cce242abe` | source/tool | source/tool/_v4_supp_t15_executor_r3_2026_09_28.py | L |
| 863 | repo | results/tool/generator/_v4_supp_t15r2_executor.py | 84884 | `4b5b720d5cda` | source/tool | source/tool/_v4_supp_t15r2_executor.py | L |
| 864 | repo | results/tool/generator/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py | 89083 | `678032f726a8` | source/tool | source/tool/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py | L |
| 865 | repo | results/tool/generator/_v4_supp_t15r2_executor_r1_2026_09_28.py | 90390 | `e0936a68fa82` | source/tool | source/tool/_v4_supp_t15r2_executor_r1_2026_09_28.py | L |
| 866 | repo | results/tool/generator/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py | 92915 | `215db16a0556` | source/tool | source/tool/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py | L |
| 867 | repo | results/tool/generator/_v4_supp_t15r2_executor_r3_2026_09_28.py | 92915 | `4f514b3fb4b8` | source/tool | source/tool/_v4_supp_t15r2_executor_r3_2026_09_28.py | L |
| 868 | repo | results/tool/generator/_v4_supp_t1_executor.py | 60563 | `91b8f70e4e18` | source/tool | source/tool/_v4_supp_t1_executor.py | L |
| 869 | repo | results/tool/generator/_v4_track2_multimodel_rerun.py | 38719 | `5c0983eaaf11` | source/tool | source/tool/_v4_track2_multimodel_rerun.py | L |
| 870 | repo | results/tool/generator/deposon_dpath_cross_modal_runner_2026_09_10.py | 27930 | `fb20a6ba5ec6` | source/tool | source/tool/deposon_dpath_cross_modal_runner_2026_09_10.py | L |
| 871 | repo | results/tool/generator/deposon_feshbach_rag_30cells_2026_09_10.py | 14343 | `a072e4184e83` | source/tool | source/tool/deposon_feshbach_rag_30cells_2026_09_10.py | L |
| 872 | repo | results/tool/generator/deposon_v1_implementation_calculator_2026_09_10.py | 10751 | `121f104012f4` | source/tool | source/tool/deposon_v1_implementation_calculator_2026_09_10.py | L |
| 873 | repo | results/tool/generator/deposon_volcengine_worker_b_2026_09_10.py | 13232 | `401dfd3c27f3` | source/tool | source/tool/deposon_volcengine_worker_b_2026_09_10.py | L |
| 874 | repo | results/tool/generator/deposon_volcengine_worker_c_2026_09_10.py | 11692 | `b5eeef1e9bd7` | source/tool | source/tool/deposon_volcengine_worker_c_2026_09_10.py | L |
| 875 | repo | results/verdict/judgement/_ablation_data_2026_10_20.json | 349715 | `78e52185063a` | readout/final | readout/final/_ablation_data_2026_10_20.json | L |
| 876 | repo | results/verdict/judgement/_af1_attribution_verdict_2026_10_17.md | 43259 | `d6d8c488fc33` | verdict/judge | verdict/judge/_af1_attribution_verdict_2026_10_17.md | L |
| 877 | repo | results/verdict/judgement/_af2_proof_and_grain_scope_effect_2026_10_17.md | 41779 | `faee80c8b051` | readout/final | readout/final/_af2_proof_and_grain_scope_effect_2026_10_17.md | L |
| 878 | repo | results/verdict/judgement/_af_flip要件消解_rulings_effect_2026_10_17.md | 45096 | `dc5ee48e1f53` | verdict/pi | verdict/pi/_af_flip要件消解_rulings_effect_2026_10_17.md | L |
| 879 | repo | results/verdict/judgement/_af_rules_approval_effect_2026_10_17.md | 43731 | `ce0a2847ad4e` | verdict/judge | verdict/judge/_af_rules_approval_effect_2026_10_17.md | L |
| 880 | repo | results/verdict/judgement/_approval_card_four_rulings_effect_2026_10_17.md | 50703 | `8e1b7d6ae996` | verdict/pi | verdict/pi/_approval_card_four_rulings_effect_2026_10_17.md | L |
| 881 | repo | results/verdict/judgement/_arxiv_2609_09001_metadata_snapshot_2026_10_20.md | 13861 | `215f89a0c461` | doc/paper | doc/paper/_arxiv_2609_09001_metadata_snapshot_2026_10_20.md | L |
| 882 | repo | results/verdict/judgement/_b0_sixty_items_location_list_2026_10_13.md | 33046 | `7c1f8a704f83` | verdict/pi | verdict/pi/_b0_sixty_items_location_list_2026_10_13.md | L |
| 883 | repo | results/verdict/judgement/_b4_alternative_deliberation_judgment_2026_10_12.md | 14233 | `f050e5aff611` | verdict/judge | verdict/judge/_b4_alternative_deliberation_judgment_2026_10_12.md | L |
| 884 | repo | results/verdict/judgement/_b_tier_five_subitems_draft_2026_10_14.md | 37605 | `3adfa261bab9` | verdict/judge | verdict/judge/_b_tier_five_subitems_draft_2026_10_14.md | L |
| 885 | repo | results/verdict/judgement/_backfill_verification_2026_10_21.md | 52147 | `c6367741737a` | verdict/judge | verdict/judge/_backfill_verification_2026_10_21.md | L |
| 886 | repo | results/verdict/judgement/_batch10_deliberation_judgment_2026_10_14.md | 32458 | `f1e9d439b04d` | verdict/judge | verdict/judge/_batch10_deliberation_judgment_2026_10_14.md | L |
| 887 | repo | results/verdict/judgement/_batch11_deliberation_judgment_2026_10_14.md | 25153 | `70b50503a32e` | verdict/judge | verdict/judge/_batch11_deliberation_judgment_2026_10_14.md | L |
| 888 | repo | results/verdict/judgement/_batch3_execution_receipt_kimi_2026_10_18.md | 140713 | `10a3b36859d7` | verdict/pi | verdict/pi/_batch3_execution_receipt_kimi_2026_10_18.md | L |
| 889 | repo | results/verdict/judgement/_batch5_deliberation_judgment_2026_10_13.md | 46325 | `a1ad238879ad` | readout/final | readout/final/_batch5_deliberation_judgment_2026_10_13.md | L |
| 890 | repo | results/verdict/judgement/_batch6_deliberation_judgment_2026_10_13.md | 29421 | `a41332378c56` | verdict/judge | verdict/judge/_batch6_deliberation_judgment_2026_10_13.md | L |
| 891 | repo | results/verdict/judgement/_batch8_deliberation_judgment_2026_10_14.md | 49012 | `a68b2971b8e1` | verdict/judge | verdict/judge/_batch8_deliberation_judgment_2026_10_14.md | L |
| 892 | repo | results/verdict/judgement/_buexp_backfill_deliberation_2026_10_21.md | 80157 | `4125ea2b2f82` | readout/final | readout/final/_buexp_backfill_deliberation_2026_10_21.md | L |
| 893 | repo | results/verdict/judgement/_c1_u5_ruling_register_2026_10_12.md | 15499 | `2c3f48e111cc` | verdict/pi | verdict/pi/_c1_u5_ruling_register_2026_10_12.md | L |
| 894 | repo | results/verdict/judgement/_c1c4_ab_alpha_pilot_result_2026_10_09.json | 104225 | `bc7c35707b78` | readout/final | readout/final/_c1c4_ab_alpha_pilot_result_2026_10_09.json | L |
| 895 | repo | results/verdict/judgement/_c1c4_ab_beta_pilot_result_2026_10_09.json | 109879 | `fd72ebf836e1` | readout/final | readout/final/_c1c4_ab_beta_pilot_result_2026_10_09.json | L |
| 896 | repo | results/verdict/judgement/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md | 37908 | `f1ca2c59bed9` | verdict/judge | verdict/judge/_c4_rejection_axis_reconciliation_judgment_2026_10_12.md | L |
| 897 | repo | results/verdict/judgement/_c4_scope_ruling_and_d1_requalification_register_2026_10_12.md | 29510 | `b28540b999a6` | verdict/pi | verdict/pi/_c4_scope_ruling_and_d1_requalification_register_2026_10_12.md | L |
| 898 | repo | results/verdict/judgement/_c5_both_pillars_closed_effect_2026_10_17.md | 24464 | `91fe9a16059d` | verdict/pi | verdict/pi/_c5_both_pillars_closed_effect_2026_10_17.md | L |
| 899 | repo | results/verdict/judgement/_c5b_closure_verdict_2026_10_17.md | 26218 | `660555b9b6be` | verdict/pi | verdict/pi/_c5b_closure_verdict_2026_10_17.md | L |
| 900 | repo | results/verdict/judgement/_canonical_face_scope_corrigendum_2026_10_16.md | 14502 | `1b45571bddca` | verdict/pi | verdict/pi/_canonical_face_scope_corrigendum_2026_10_16.md | L |
| 901 | repo | results/verdict/judgement/_card_register_dir_verdict_2026_10_17.md | 26682 | `a694e5d55ce1` | verdict/pi | verdict/pi/_card_register_dir_verdict_2026_10_17.md | L |
| 902 | repo | results/verdict/judgement/_chd_construction_domain_declaration_draft_2026_10_10.md | 34948 | `17cf0d59cd7b` | verdict/kd | verdict/kd/_chd_construction_domain_declaration_draft_2026_10_10.md | L |
| 903 | repo | results/verdict/judgement/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.json | 23272 | `f729a6a03a9e` | readout/final | readout/final/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.json | L |
| 904 | repo | results/verdict/judgement/_citation_corrigenda_volume_2026_10_17.md | 68731 | `7c20c38c501d` | readout/final | readout/final/_citation_corrigenda_volume_2026_10_17.md | L |
| 905 | repo | results/verdict/judgement/_citation_no_utility_caliber_draft_2026_10_17.md | 49332 | `536a3064ad38` | verdict/judge | verdict/judge/_citation_no_utility_caliber_draft_2026_10_17.md | L |
| 906 | repo | results/verdict/judgement/_closure_sweep_r2_2026_10_18.md | 121848 | `31a03b8d756b` | verdict/judge | verdict/judge/_closure_sweep_r2_2026_10_18.md | L |
| 907 | repo | results/verdict/judgement/_cluster_a_sface_adjudication_2026_10_18.md | 53759 | `9c05d0ab78d5` | verdict/judge | verdict/judge/_cluster_a_sface_adjudication_2026_10_18.md | L |
| 908 | repo | results/verdict/judgement/_cluster_abc_pack_adoption_effect_2026_10_18.md | 82049 | `479e28afba53` | readout/final | readout/final/_cluster_abc_pack_adoption_effect_2026_10_18.md | L |
| 909 | repo | results/verdict/judgement/_cluster_b_carrier_adjudication_2026_10_18.md | 72984 | `3f34fd241a50` | readout/final | readout/final/_cluster_b_carrier_adjudication_2026_10_18.md | L |
| 910 | repo | results/verdict/judgement/_cluster_c_keyface_adjudication_2026_10_18.md | 63462 | `8e9ec9104a1e` | readout/final | readout/final/_cluster_c_keyface_adjudication_2026_10_18.md | L |
| 911 | repo | results/verdict/judgement/_cluster_d_counting_adjudication_2026_10_18.md | 57929 | `edcc23114b18` | verdict/judge | verdict/judge/_cluster_d_counting_adjudication_2026_10_18.md | L |
| 912 | repo | results/verdict/judgement/_cluster_dfghi_pack_adoption_effect_2026_10_18.md | 68478 | `d85a8101aa12` | readout/final | readout/final/_cluster_dfghi_pack_adoption_effect_2026_10_18.md | L |
| 913 | repo | results/verdict/judgement/_cluster_f_deletion_adjudication_2026_10_18.md | 52226 | `e289d12fd5d4` | readout/final | readout/final/_cluster_f_deletion_adjudication_2026_10_18.md | L |
| 914 | repo | results/verdict/judgement/_cluster_g_deletion_preconditions_adjudication_2026_10_18.md | 76051 | `918659f9b0f6` | verdict/judge | verdict/judge/_cluster_g_deletion_preconditions_adjudication_2026_10_18.md | L |
| 915 | repo | results/verdict/judgement/_cluster_h_directory_adjudication_2026_10_18.md | 61721 | `616e466f4f49` | verdict/judge | verdict/judge/_cluster_h_directory_adjudication_2026_10_18.md | L |
| 916 | repo | results/verdict/judgement/_cluster_i_f1_f6_f7_verdict_2026_10_18.md | 51397 | `98b3ef11e115` | verdict/judge | verdict/judge/_cluster_i_f1_f6_f7_verdict_2026_10_18.md | L |
| 917 | repo | results/verdict/judgement/_cluster_i_f4_f5_evidence_2026_10_18.md | 39529 | `84037fd8d0a6` | verdict/judge | verdict/judge/_cluster_i_f4_f5_evidence_2026_10_18.md | L |
| 918 | repo | results/verdict/judgement/_cluster_i_historical_adjudication_2026_10_18.md | 65872 | `53ac8f30556d` | verdict/judge | verdict/judge/_cluster_i_historical_adjudication_2026_10_18.md | L |
| 919 | repo | results/verdict/judgement/_cluster_i_item14_closure_effect_2026_10_18.md | 34968 | `c62c7fad4afd` | verdict/pi | verdict/pi/_cluster_i_item14_closure_effect_2026_10_18.md | L |
| 920 | repo | results/verdict/judgement/_cluster_i_item14_closure_verdict_2026_10_18.md | 39751 | `d23de0a9e7eb` | verdict/judge | verdict/judge/_cluster_i_item14_closure_verdict_2026_10_18.md | L |
| 921 | repo | results/verdict/judgement/_cluster_i_item6_compatibility_adjudication_2026_10_18.md | 40492 | `e3daf0cd6fb8` | verdict/judge | verdict/judge/_cluster_i_item6_compatibility_adjudication_2026_10_18.md | L |
| 922 | repo | results/verdict/judgement/_cluster_i_item6_conditions_adjudication_2026_10_18.md | 40834 | `f2802aa63370` | verdict/judge | verdict/judge/_cluster_i_item6_conditions_adjudication_2026_10_18.md | L |
| 923 | repo | results/verdict/judgement/_cluster_i_item6_give_values_adjudication_2026_10_18.md | 45549 | `b33aae011ca8` | verdict/judge | verdict/judge/_cluster_i_item6_give_values_adjudication_2026_10_18.md | L |
| 924 | repo | results/verdict/judgement/_cluster_j_glm_62_adjudication_2026_10_19.md | 48997 | `b4252f1f736d` | verdict/judge | verdict/judge/_cluster_j_glm_62_adjudication_2026_10_19.md | L |
| 925 | repo | results/verdict/judgement/_cluster_k_eta_blockers_adjudication_2026_10_19.md | 55977 | `4b1040954064` | verdict/judge | verdict/judge/_cluster_k_eta_blockers_adjudication_2026_10_19.md | L |
| 926 | repo | results/verdict/judgement/_consolidated_pending_rulings_scroll_2026_10_18.md | 104340 | `df894c9acc2a` | verdict/pi | verdict/pi/_consolidated_pending_rulings_scroll_2026_10_18.md | L |
| 927 | repo | results/verdict/judgement/_construction_change_count_ruling_effect_2026_10_18.md | 20247 | `44021af1d6ff` | verdict/pi | verdict/pi/_construction_change_count_ruling_effect_2026_10_18.md | L |
| 928 | repo | results/verdict/judgement/_continued_three_rulings_effect_2026_10_17.md | 38440 | `4397d1a16805` | verdict/pi | verdict/pi/_continued_three_rulings_effect_2026_10_17.md | L |
| 929 | repo | results/verdict/judgement/_copilot_eq_grok_rulings_effect_2026_10_17.md | 22894 | `d34d769afaca` | verdict/pi | verdict/pi/_copilot_eq_grok_rulings_effect_2026_10_17.md | L |
| 930 | repo | results/verdict/judgement/_count_value_timestamp_mandate_effect_2026_10_18.md | 24101 | `cb887fda55b5` | verdict/pi | verdict/pi/_count_value_timestamp_mandate_effect_2026_10_18.md | L |
| 931 | repo | results/verdict/judgement/_coze_v5_r2_residual4_adjudication_2026_10_18.md | 43038 | `89de292707fb` | doc/letter | doc/letter/_coze_v5_r2_residual4_adjudication_2026_10_18.md | L |
| 932 | repo | results/verdict/judgement/_coze_v5_r2_residual4_adoption_effect_2026_10_18.md | 40381 | `f688f21015e0` | readout/final | readout/final/_coze_v5_r2_residual4_adoption_effect_2026_10_18.md | L |
| 933 | repo | results/verdict/judgement/_cpath_e3_sign_normalization_2026_10_01.md | 19740 | `e67ebccc82c9` | verdict/pi | verdict/pi/_cpath_e3_sign_normalization_2026_10_01.md | L |
| 934 | repo | results/verdict/judgement/_d1_ab_deliberation_judgment_2026_10_15.md | 46542 | `88c2af72ff7b` | verdict/judge | verdict/judge/_d1_ab_deliberation_judgment_2026_10_15.md | L |
| 935 | repo | results/verdict/judgement/_d1_backfill_intake_verdict_2026_10_01.md | 42115 | `42a3858976f2` | verdict/pi | verdict/pi/_d1_backfill_intake_verdict_2026_10_01.md | L |
| 936 | repo | results/verdict/judgement/_dangling_630_remediation_list_2026_10_17.md | 120723 | `5bc372de9a84` | verdict/pi | verdict/pi/_dangling_630_remediation_list_2026_10_17.md | L |
| 937 | repo | results/verdict/judgement/_deliverable_pack_manifest_2026_10_21.md | 80302 | `debce2c6d3cb` | readout/final | readout/final/_deliverable_pack_manifest_2026_10_21.md | L |
| 938 | repo | results/verdict/judgement/_deliverable_pack_v2_manifest_2026_10_21.md | 57693 | `7ae0efbb777d` | readout/final | readout/final/_deliverable_pack_v2_manifest_2026_10_21.md | L |
| 939 | repo | results/verdict/judgement/_den16_rename_prefix_candidates_2026_10_21.md | 92103 | `7c3166071a5c` | readout/final | readout/final/_den16_rename_prefix_candidates_2026_10_21.md | L |
| 940 | repo | results/verdict/judgement/_deposon_full_history_main_2026_10_19.md | 14265 | `9c65f1db6202` | doc/paper | doc/paper/_deposon_full_history_main_2026_10_19.md | L |
| 941 | repo | results/verdict/judgement/_deposon_full_history_sub_2026_10_19.md | 45958 | `a572747a2001` | readout/final | readout/final/_deposon_full_history_sub_2026_10_19.md | L |
| 942 | repo | results/verdict/judgement/_domain_backfill_401_v2_caliber_effect_2026_10_18.md | 21793 | `86a4fedebbbc` | verdict/pi | verdict/pi/_domain_backfill_401_v2_caliber_effect_2026_10_18.md | L |
| 943 | repo | results/verdict/judgement/_domain_backfill_hold235_adjudication_2026_10_18.md | 39456 | `43515db69b4c` | verdict/judge | verdict/judge/_domain_backfill_hold235_adjudication_2026_10_18.md | L |
| 944 | repo | results/verdict/judgement/_domain_backfill_rulings_effect_2026_10_18.md | 1394 | `fc9683f63afe` | verdict/pi | verdict/pi/_domain_backfill_rulings_effect_2026_10_18.md | L |
| 945 | repo | results/verdict/judgement/_erratum_arm_label_transcription_2026_10_17.md | 19052 | `45452ccac4ac` | readout/final | readout/final/_erratum_arm_label_transcription_2026_10_17.md | L |
| 946 | repo | results/verdict/judgement/_esc3_esc6_resolution_2026_10_17.md | 28717 | `509e52734292` | readout/final | readout/final/_esc3_esc6_resolution_2026_10_17.md | L |
| 947 | repo | results/verdict/judgement/_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md | 34206 | `e550e344a258` | readout/final | readout/final/_esc5_adoption_and_ritt_remeasure_effect_2026_10_17.md | L |
| 948 | repo | results/verdict/judgement/_esc5_verdict_2026_10_17.md | 27258 | `d970bb175672` | verdict/judge | verdict/judge/_esc5_verdict_2026_10_17.md | L |
| 949 | repo | results/verdict/judgement/_eta_construct_c1_c16_recommendation_2026_10_20.md | 83989 | `56760f30332b` | readout/final | readout/final/_eta_construct_c1_c16_recommendation_2026_10_20.md | L |
| 950 | repo | results/verdict/judgement/_eta_missing_params_and_c1_adjudication_2026_10_19.md | 27703 | `57efdf5255ee` | verdict/pi | verdict/pi/_eta_missing_params_and_c1_adjudication_2026_10_19.md | L |
| 951 | repo | results/verdict/judgement/_eta_preexp_wait_and_leveling_effect_2026_10_18.md | 32594 | `a79b0ca9ce9e` | readout/final | readout/final/_eta_preexp_wait_and_leveling_effect_2026_10_18.md | L |
| 952 | repo | results/verdict/judgement/_eta_sep_caliber_draft_2026_10_20.md | 68943 | `2383be56f28f` | verdict/kd | verdict/kd/_eta_sep_caliber_draft_2026_10_20.md | L |
| 953 | repo | results/verdict/judgement/_eta_sep_measurement_data_2026_10_20.json | 45635 | `54c070d9f389` | readout/final | readout/final/_eta_sep_measurement_data_2026_10_20.json | L |
| 954 | repo | results/verdict/judgement/_eta_sep_measurement_recalc_2026_10_20.md | 37061 | `585a30bf9f54` | readout/final | readout/final/_eta_sep_measurement_recalc_2026_10_20.md | L |
| 955 | repo | results/verdict/judgement/_exp06_independent_check_2026_10_10.json | 20480 | `4c36c376ab9c` | readout/final | readout/final/_exp06_independent_check_2026_10_10.json | L |
| 956 | repo | results/verdict/judgement/_experiment_face_scope_column1_supplement_draft_2026_10_19.md | 37932 | `1de82ef76e16` | verdict/kd | verdict/kd/_experiment_face_scope_column1_supplement_draft_2026_10_19.md | L |
| 957 | repo | results/verdict/judgement/_experiment_face_scope_list_draft_2026_10_19.md | 27727 | `3fdd7f38b124` | verdict/kd | verdict/kd/_experiment_face_scope_list_draft_2026_10_19.md | L |
| 958 | repo | results/verdict/judgement/_ext5_verdict_2026_10_17.md | 63647 | `80a81bd525d4` | verdict/judge | verdict/judge/_ext5_verdict_2026_10_17.md | L |
| 959 | repo | results/verdict/judgement/_f12_kd_disposition_register_2026_10_15.md | 12661 | `9c0427685a19` | verdict/kd | verdict/kd/_f12_kd_disposition_register_2026_10_15.md | L |
| 960 | repo | results/verdict/judgement/_f3_payment_vector_reconstruction_2026_10_19.md | 51428 | `56ed8250525b` | verdict/pi | verdict/pi/_f3_payment_vector_reconstruction_2026_10_19.md | L |
| 961 | repo | results/verdict/judgement/_f3_payment_vector_reconstruction_data_2026_10_19.json | 210141 | `7f80d5ae03bb` | readout/final | readout/final/_f3_payment_vector_reconstruction_data_2026_10_19.json | L |
| 962 | repo | results/verdict/judgement/_f3_payment_vector_third_party_recalc_2026_10_19.md | 48898 | `d716cd3f1240` | verdict/pi | verdict/pi/_f3_payment_vector_third_party_recalc_2026_10_19.md | L |
| 963 | repo | results/verdict/judgement/_f4_direction1_domain_effectivity_2026_10_11.md | 40301 | `fd4ec7559342` | verdict/pi | verdict/pi/_f4_direction1_domain_effectivity_2026_10_11.md | L |
| 964 | repo | results/verdict/judgement/_f7d_today_no_open_erratum_2026_10_19.md | 21682 | `f794107e790a` | verdict/pi | verdict/pi/_f7d_today_no_open_erratum_2026_10_19.md | L |
| 965 | repo | results/verdict/judgement/_face_r_coexist_verdict_2026_10_17.md | 37604 | `0fd3788e2d3b` | verdict/judge | verdict/judge/_face_r_coexist_verdict_2026_10_17.md | L |
| 966 | repo | results/verdict/judgement/_fail_h0_verdict_2026_10_17.md | 41481 | `c8794d87b4b6` | verdict/judge | verdict/judge/_fail_h0_verdict_2026_10_17.md | L |
| 967 | repo | results/verdict/judgement/_fake_kd_closeout_register_2026_10_21.md | 40192 | `23bf57ed06dd` | verdict/kd | verdict/kd/_fake_kd_closeout_register_2026_10_21.md | L |
| 968 | repo | results/verdict/judgement/_fake_kd_itemwise_adjudication_2026_10_21.md | 83606 | `b6221e7a2efe` | verdict/kd | verdict/kd/_fake_kd_itemwise_adjudication_2026_10_21.md | L |
| 969 | repo | results/verdict/judgement/_fake_kd_p3_readjudication_2026_10_21.md | 72909 | `9c09cc70b339` | verdict/kd | verdict/kd/_fake_kd_p3_readjudication_2026_10_21.md | L |
| 970 | repo | results/verdict/judgement/_fake_kd_p4_reversal_adjudication_2026_10_21.md | 97074 | `e78092e45065` | verdict/kd | verdict/kd/_fake_kd_p4_reversal_adjudication_2026_10_21.md | L |
| 971 | repo | results/verdict/judgement/_fake_kd_p5_reversal_adjudication_2026_10_21.md | 64697 | `6addfa5db8e9` | verdict/kd | verdict/kd/_fake_kd_p5_reversal_adjudication_2026_10_21.md | L |
| 972 | repo | results/verdict/judgement/_fake_kd_p6_confirmation_adjudication_2026_10_21.md | 71937 | `af506d37e00a` | verdict/kd | verdict/kd/_fake_kd_p6_confirmation_adjudication_2026_10_21.md | L |
| 973 | repo | results/verdict/judgement/_fake_kd_p8_confirmation_adjudication_2026_10_21.md | 68956 | `7a0dd145a76d` | verdict/kd | verdict/kd/_fake_kd_p8_confirmation_adjudication_2026_10_21.md | L |
| 974 | repo | results/verdict/judgement/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md | 40957 | `41d7b76ea4d6` | verdict/pi | verdict/pi/_fake_verdict_reverify_sixitem_ledger_2026_09_30.md | L |
| 975 | repo | results/verdict/judgement/_family_de_stale_refresh_matrix_2026_10_14.md | 78861 | `7d67b6af125a` | verdict/judge | verdict/judge/_family_de_stale_refresh_matrix_2026_10_14.md | L |
| 976 | repo | results/verdict/judgement/_family_de_stale_refresh_repo_exec_2026_10_14.md | 31151 | `55155ec5f430` | verdict/pi | verdict/pi/_family_de_stale_refresh_repo_exec_2026_10_14.md | L |
| 977 | repo | results/verdict/judgement/_family_de_stale_refresh_sub_exec_2026_10_14.md | 31813 | `c7d20b3c18ba` | verdict/pi | verdict/pi/_family_de_stale_refresh_sub_exec_2026_10_14.md | L |
| 978 | repo | results/verdict/judgement/_field_table_c6_c8_o5_recommendation_draft_2026_10_19.md | 61896 | `bbcbac292f8d` | readout/final | readout/final/_field_table_c6_c8_o5_recommendation_draft_2026_10_19.md | L |
| 979 | repo | results/verdict/judgement/_five_terminal_judgments_ruling_2026_10_10.md | 27315 | `9e96d0a1ba12` | verdict/kd | verdict/kd/_five_terminal_judgments_ruling_2026_10_10.md | L |
| 980 | repo | results/verdict/judgement/_five_zero_recheck_evidence_2026_10_18.md | 37035 | `193d11089327` | verdict/judge | verdict/judge/_five_zero_recheck_evidence_2026_10_18.md | L |
| 981 | repo | results/verdict/judgement/_freeze_face_four_rulings_effect_2026_10_17.md | 41068 | `1e512ea146d3` | verdict/pi | verdict/pi/_freeze_face_four_rulings_effect_2026_10_17.md | L |
| 982 | repo | results/verdict/judgement/_g5_ccp_execution_prereqs_2026_10_10.md | 32815 | `ab1a07ae2fd1` | verdict/judge | verdict/judge/_g5_ccp_execution_prereqs_2026_10_10.md | L |
| 983 | repo | results/verdict/judgement/_gamma_taucert_scope_delimitation_2026_10_17.md | 37104 | `7374c29a8d4e` | readout/final | readout/final/_gamma_taucert_scope_delimitation_2026_10_17.md | L |
| 984 | repo | results/verdict/judgement/_gap10_four_rulings_effect_2026_10_17.md | 35339 | `b5596dd2abbb` | verdict/pi | verdict/pi/_gap10_four_rulings_effect_2026_10_17.md | L |
| 985 | repo | results/verdict/judgement/_gap_and_kd_flip_master_inventory_2026_10_19.md | 9043 | `989f2dc022a5` | verdict/kd | verdict/kd/_gap_and_kd_flip_master_inventory_2026_10_19.md | L |
| 986 | repo | results/verdict/judgement/_gate1_five_zero_recheck_2026_10_12.md | 20330 | `9c70140c7b02` | verdict/pi | verdict/pi/_gate1_five_zero_recheck_2026_10_12.md | L |
| 987 | repo | results/verdict/judgement/_gate1_five_zero_recheck_glm_scope_2026_10_13.md | 34647 | `2f27acf42897` | verdict/pi | verdict/pi/_gate1_five_zero_recheck_glm_scope_2026_10_13.md | L |
| 988 | repo | results/verdict/judgement/_gate1_gap_three_items_disposition_2026_10_12.md | 36087 | `5cf848421c2b` | verdict/pi | verdict/pi/_gate1_gap_three_items_disposition_2026_10_12.md | L |
| 989 | repo | results/verdict/judgement/_ge01_readiness_adjudication_2026_10_21.md | 64097 | `336500609b5c` | verdict/judge | verdict/judge/_ge01_readiness_adjudication_2026_10_21.md | L |
| 990 | repo | results/verdict/judgement/_github_suspect_rulings_effect_2026_10_17.md | 51654 | `f49079f46c2b` | verdict/pi | verdict/pi/_github_suspect_rulings_effect_2026_10_17.md | L |
| 991 | repo | results/verdict/judgement/_h_budget_measurement_exec_2026_10_15.md | 25705 | `c5a58305876a` | readout/final | readout/final/_h_budget_measurement_exec_2026_10_15.md | L |
| 992 | repo | results/verdict/judgement/_h_exact_enum_killline_prereg_2026_10_21.md | 74275 | `bfce04eb2745` | verdict/kd | verdict/kd/_h_exact_enum_killline_prereg_2026_10_21.md | L |
| 993 | repo | results/verdict/judgement/_h_exact_enum_trace_2026_10_21.md | 61131 | `d187e54cc291` | readout/final | readout/final/_h_exact_enum_trace_2026_10_21.md | L |
| 994 | repo | results/verdict/judgement/_h_face_freeze_ruling_effect_2026_10_18.md | 28087 | `3aa3bcc56258` | verdict/pi | verdict/pi/_h_face_freeze_ruling_effect_2026_10_18.md | L |
| 995 | repo | results/verdict/judgement/_harness_mask_correct_value_validation_2026_10_17.md | 21741 | `b7d638ebef6e` | verdict/judge | verdict/judge/_harness_mask_correct_value_validation_2026_10_17.md | L |
| 996 | repo | results/verdict/judgement/_historical_ forgetting_recheck_2026_10_18.md | 34941 | `19b73ab478f5` | verdict/judge | verdict/judge/_historical_ forgetting_recheck_2026_10_18.md | L |
| 997 | repo | results/verdict/judgement/_historical_forgetting_21_status_update_2026_10_18.md | 43130 | `f2f1a9be203d` | verdict/pi | verdict/pi/_historical_forgetting_21_status_update_2026_10_18.md | L |
| 998 | repo | results/verdict/judgement/_independent_review_history_gaps_kd_2026_10_19_sub.md | 52087 | `9adf7d28fe2d` | verdict/kd | verdict/kd/_independent_review_history_gaps_kd_2026_10_19_sub.md | L |
| 999 | repo | results/verdict/judgement/_interval_420_600_upper_bound_deliberation_2026_10_16.md | 34256 | `4d2c65968311` | readout/final | readout/final/_interval_420_600_upper_bound_deliberation_2026_10_16.md | L |
| 1000 | repo | results/verdict/judgement/_interval_ceiling_post_lock_deliberation_2026_10_16.md | 46687 | `fce2f69802b9` | readout/final | readout/final/_interval_ceiling_post_lock_deliberation_2026_10_16.md | L |
| 1001 | repo | results/verdict/judgement/_item6_c2_card_reference_registration_2026_10_18.md | 23201 | `df61b2798ecb` | verdict/pi | verdict/pi/_item6_c2_card_reference_registration_2026_10_18.md | L |
| 1002 | repo | results/verdict/judgement/_item6_c2_four_fields_adjudication_2026_10_18.md | 50802 | `a40de66d87c8` | verdict/pi | verdict/pi/_item6_c2_four_fields_adjudication_2026_10_18.md | L |
| 1003 | repo | results/verdict/judgement/_item6_c2_four_fields_adoption_effect_2026_10_18.md | 40889 | `42ead18967d9` | verdict/pi | verdict/pi/_item6_c2_four_fields_adoption_effect_2026_10_18.md | L |
| 1004 | repo | results/verdict/judgement/_judgement_criteria_reference_only_no_utility_draft_2026_10_17.md | 42968 | `f5bad2e2ff00` | verdict/judge | verdict/judge/_judgement_criteria_reference_only_no_utility_draft_2026_10_17.md | L |
| 1005 | repo | results/verdict/judgement/_kabla6_trigger_review_adjudication_2026_10_21.md | 50919 | `09aea8d27041` | verdict/judge | verdict/judge/_kabla6_trigger_review_adjudication_2026_10_21.md | L |
| 1006 | repo | results/verdict/judgement/_kd04_c_denominator_expansion_readings_2026_10_10.json | 23314 | `249009e6a0cc` | readout/final | readout/final/_kd04_c_denominator_expansion_readings_2026_10_10.json | L |
| 1007 | repo | results/verdict/judgement/_kd04_c_denominator_killline_prereg_2026_10_10.md | 24527 | `8f2025e9de6f` | verdict/kd | verdict/kd/_kd04_c_denominator_killline_prereg_2026_10_10.md | L |
| 1008 | repo | results/verdict/judgement/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md | 32067 | `99b578a1be2c` | verdict/judge | verdict/judge/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md | L |
| 1009 | repo | results/verdict/judgement/_kd14_null_u_carrier_deliberation_2026_10_16.md | 35608 | `0a6279970446` | verdict/judge | verdict/judge/_kd14_null_u_carrier_deliberation_2026_10_16.md | L |
| 1010 | repo | results/verdict/judgement/_kd14_null_u_carrier_effect_register_2026_10_16.md | 24828 | `141816a6aec9` | verdict/pi | verdict/pi/_kd14_null_u_carrier_effect_register_2026_10_16.md | L |
| 1011 | repo | results/verdict/judgement/_kd1_preexp_contrast_2026_10_17.md | 27149 | `351d18d74934` | readout/final | readout/final/_kd1_preexp_contrast_2026_10_17.md | L |
| 1012 | repo | results/verdict/judgement/_kd4_adoption_and_caliber_pack_effect_2026_10_17.md | 32577 | `ce1604dfd251` | verdict/judge | verdict/judge/_kd4_adoption_and_caliber_pack_effect_2026_10_17.md | L |
| 1013 | repo | results/verdict/judgement/_kd4_homology_verdict_2026_10_17.md | 32823 | `1992b9d359a8` | verdict/judge | verdict/judge/_kd4_homology_verdict_2026_10_17.md | L |
| 1014 | repo | results/verdict/judgement/_kd_11_12_resolution_register_2026_10_16.md | 18606 | `807932c7e1c8` | verdict/kd | verdict/kd/_kd_11_12_resolution_register_2026_10_16.md | L |
| 1015 | repo | results/verdict/judgement/_kd_13_9_3_closure_register_2026_10_16.md | 19461 | `410f885430a4` | verdict/kd | verdict/kd/_kd_13_9_3_closure_register_2026_10_16.md | L |
| 1016 | repo | results/verdict/judgement/_kd_2_4_6_caliber_note_2026_10_16.md | 20497 | `0fd67a2075b7` | verdict/kd | verdict/kd/_kd_2_4_6_caliber_note_2026_10_16.md | L |
| 1017 | repo | results/verdict/judgement/_kd_civ_closure_effect_2026_10_18.md | 27186 | `040338b4940c` | verdict/kd | verdict/kd/_kd_civ_closure_effect_2026_10_18.md | L |
| 1018 | repo | results/verdict/judgement/_kd_civ_closure_verdict_2026_10_18.md | 43116 | `60e9a18fa428` | verdict/kd | verdict/kd/_kd_civ_closure_verdict_2026_10_18.md | L |
| 1019 | repo | results/verdict/judgement/_kd_cluster_verdict_pack_adjudication_2026_10_19.md | 113327 | `d87a711b0ecf` | verdict/kd | verdict/kd/_kd_cluster_verdict_pack_adjudication_2026_10_19.md | L |
| 1020 | repo | results/verdict/judgement/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md | 77119 | `522be8905484` | verdict/kd | verdict/kd/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md | L |
| 1021 | repo | results/verdict/judgement/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md | 73955 | `85e5caeb3478` | verdict/kd | verdict/kd/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md | L |
| 1022 | repo | results/verdict/judgement/_kd_esc5v2_closure_adjudication_2026_10_21.md | 74163 | `b9ba3ff8d010` | verdict/kd | verdict/kd/_kd_esc5v2_closure_adjudication_2026_10_21.md | L |
| 1023 | repo | results/verdict/judgement/_kd_eta_main_run_verdict_2026_10_20.md | 64606 | `8a5727bc4c11` | verdict/kd | verdict/kd/_kd_eta_main_run_verdict_2026_10_20.md | L |
| 1024 | repo | results/verdict/judgement/_kd_eta_selection_verdict_2026_10_20.md | 37788 | `80b8cafcd085` | verdict/kd | verdict/kd/_kd_eta_selection_verdict_2026_10_20.md | L |
| 1025 | repo | results/verdict/judgement/_kd_eta_sep_measurement_verdict_2026_10_20.md | 66712 | `ceb71b3a2570` | verdict/kd | verdict/kd/_kd_eta_sep_measurement_verdict_2026_10_20.md | L |
| 1026 | repo | results/verdict/judgement/_kd_false9_remedy_proposals_2026_10_20.md | 85265 | `77bc92c9d227` | verdict/kd | verdict/kd/_kd_false9_remedy_proposals_2026_10_20.md | L |
| 1027 | repo | results/verdict/judgement/_kd_false9_wave0_calibers_2026_10_20.md | 76664 | `97ac680345ac` | verdict/kd | verdict/kd/_kd_false9_wave0_calibers_2026_10_20.md | L |
| 1028 | repo | results/verdict/judgement/_kd_gap_resolution_rulings_effect_2026_10_17.md | 38813 | `10e40a51c9c1` | verdict/kd | verdict/kd/_kd_gap_resolution_rulings_effect_2026_10_17.md | L |
| 1029 | repo | results/verdict/judgement/_kd_gap_survey_2026_10_17.md | 45716 | `592a50470e76` | verdict/kd | verdict/kd/_kd_gap_survey_2026_10_17.md | L |
| 1030 | repo | results/verdict/judgement/_kd_ge01_eps4_scope_escalation_note_2026_10_16.md | 26411 | `731144fbda94` | verdict/kd | verdict/kd/_kd_ge01_eps4_scope_escalation_note_2026_10_16.md | L |
| 1031 | repo | results/verdict/judgement/_kd_h1_h7_disposition_draft_2026_10_20.md | 72915 | `42ea79ea3f06` | verdict/kd | verdict/kd/_kd_h1_h7_disposition_draft_2026_10_20.md | L |
| 1032 | repo | results/verdict/judgement/_kd_h1_h7_hidden_gaps_register_2026_10_19.md | 51557 | `7eefedd92808` | verdict/kd | verdict/kd/_kd_h1_h7_hidden_gaps_register_2026_10_19.md | L |
| 1033 | repo | results/verdict/judgement/_kd_h1_lineage_declaration_2026_10_20.md | 54662 | `b17b642f1183` | verdict/kd | verdict/kd/_kd_h1_lineage_declaration_2026_10_20.md | L |
| 1034 | repo | results/verdict/judgement/_kd_h2_anchor_chain_erratum_2026_10_20.md | 39377 | `a23dfaf20278` | verdict/kd | verdict/kd/_kd_h2_anchor_chain_erratum_2026_10_20.md | L |
| 1035 | repo | results/verdict/judgement/_kd_h4_fingerprint_reanchor_register_2026_10_20.md | 47335 | `15d1279d1638` | verdict/kd | verdict/kd/_kd_h4_fingerprint_reanchor_register_2026_10_20.md | L |
| 1036 | repo | results/verdict/judgement/_kd_h5_h6_recheck_2026_10_14.md | 22205 | `d9459768e058` | verdict/kd | verdict/kd/_kd_h5_h6_recheck_2026_10_14.md | L |
| 1037 | repo | results/verdict/judgement/_kd_h5_session_history_domain_caliber_2026_10_20.md | 55674 | `8db6f947bf98` | verdict/kd | verdict/kd/_kd_h5_session_history_domain_caliber_2026_10_20.md | L |
| 1038 | repo | results/verdict/judgement/_kd_h5_session_history_pilot_1of10_2026_10_20.md | 1000949 | `30a6398b1e2e` | verdict/kd | verdict/kd/_kd_h5_session_history_pilot_1of10_2026_10_20.md | L |
| 1039 | repo | results/verdict/judgement/_kd_h6_caliber_mapping_adjudication_2026_10_20.md | 68036 | `9e853e0f259b` | verdict/kd | verdict/kd/_kd_h6_caliber_mapping_adjudication_2026_10_20.md | L |
| 1040 | repo | results/verdict/judgement/_kd_history_pack_adjudication_2026_10_19.md | 56575 | `fce088063dbd` | verdict/kd | verdict/kd/_kd_history_pack_adjudication_2026_10_19.md | L |
| 1041 | repo | results/verdict/judgement/_kd_identified_defect_attribution_caliber_2026_10_20.md | 73752 | `609943436a0d` | verdict/kd | verdict/kd/_kd_identified_defect_attribution_caliber_2026_10_20.md | L |
| 1042 | repo | results/verdict/judgement/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md | 73620 | `b666077233c5` | verdict/kd | verdict/kd/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md | L |
| 1043 | repo | results/verdict/judgement/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md | 92280 | `30e47f1181d3` | verdict/kd | verdict/kd/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md | L |
| 1044 | repo | results/verdict/judgement/_kd_mda8_domain_readings_adjudication_2026_10_19.md | 65988 | `42af8a6e0703` | verdict/kd | verdict/kd/_kd_mda8_domain_readings_adjudication_2026_10_19.md | L |
| 1045 | repo | results/verdict/judgement/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md | 57571 | `9a960a574260` | verdict/kd | verdict/kd/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md | L |
| 1046 | repo | results/verdict/judgement/_kd_mda8_first_reading_verdict_2026_10_20.md | 64345 | `9c75b5c16676` | verdict/kd | verdict/kd/_kd_mda8_first_reading_verdict_2026_10_20.md | L |
| 1047 | repo | results/verdict/judgement/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md | 95664 | `ebe106d2da47` | verdict/kd | verdict/kd/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md | L |
| 1048 | repo | results/verdict/judgement/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md | 80642 | `8a77b155fd64` | verdict/kd | verdict/kd/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md | L |
| 1049 | repo | results/verdict/judgement/_kd_mda8_spec_rest_recommendation_2026_10_19.md | 69095 | `242b7ea98eb7` | verdict/kd | verdict/kd/_kd_mda8_spec_rest_recommendation_2026_10_19.md | L |
| 1050 | repo | results/verdict/judgement/_kd_mda8a24_clearance_verdict_2026_10_20.md | 77696 | `170ab543d941` | verdict/kd | verdict/kd/_kd_mda8a24_clearance_verdict_2026_10_20.md | L |
| 1051 | repo | results/verdict/judgement/_kd_mda9_closure_adjudication_2026_10_21.md | 75087 | `b6f3a254abb1` | verdict/kd | verdict/kd/_kd_mda9_closure_adjudication_2026_10_21.md | L |
| 1052 | repo | results/verdict/judgement/_kd_s3_2_3_corrigendum_2026_10_16.md | 26395 | `5c4fd13640f4` | verdict/kd | verdict/kd/_kd_s3_2_3_corrigendum_2026_10_16.md | L |
| 1053 | repo | results/verdict/judgement/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md | 49252 | `e09780d24a7a` | verdict/kd | verdict/kd/_kd_s3b1_kd1_n7_rulings_effect_2026_10_17.md | L |
| 1054 | repo | results/verdict/judgement/_kd_s3b1_verdict_2026_10_17.md | 45846 | `ed36d0171672` | verdict/kd | verdict/kd/_kd_s3b1_verdict_2026_10_17.md | L |
| 1055 | repo | results/verdict/judgement/_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md | 48246 | `3ecf179b83a1` | verdict/kd | verdict/kd/_kd_s3b5_kd1_esc36_batch_lock_effect_2026_10_17.md | L |
| 1056 | repo | results/verdict/judgement/_kd_sepcal7_final_verdict_2026_10_20.md | 70518 | `c013aeb1235f` | verdict/kd | verdict/kd/_kd_sepcal7_final_verdict_2026_10_20.md | L |
| 1057 | repo | results/verdict/judgement/_kd_two_gates_boundary_adoption_2026_10_21.md | 43097 | `b69092972467` | verdict/kd | verdict/kd/_kd_two_gates_boundary_adoption_2026_10_21.md | L |
| 1058 | repo | results/verdict/judgement/_kd_two_gates_boundary_proposal_2026_10_21.md | 41462 | `0ef78a26f637` | verdict/kd | verdict/kd/_kd_two_gates_boundary_proposal_2026_10_21.md | L |
| 1059 | repo | results/verdict/judgement/_kd_two_gates_comparison_2026_10_20.md | 45929 | `45f1ea5e5b23` | verdict/kd | verdict/kd/_kd_two_gates_comparison_2026_10_20.md | L |
| 1060 | repo | results/verdict/judgement/_kd_u1_u4_rulings_effect_2026_10_17.md | 30072 | `4500a4715f3b` | verdict/kd | verdict/kd/_kd_u1_u4_rulings_effect_2026_10_17.md | L |
| 1061 | repo | results/verdict/judgement/_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md | 38534 | `85702808df0c` | verdict/kd | verdict/kd/_kd_u5_u6_s3b4_rulings_effect_2026_10_17.md | L |
| 1062 | repo | results/verdict/judgement/_kd_u6_readside_rewire_validation_2026_10_17.md | 24961 | `751205f0368f` | verdict/kd | verdict/kd/_kd_u6_readside_rewire_validation_2026_10_17.md | L |
| 1063 | repo | results/verdict/judgement/_kd_unambiguous_meaning_ruling_2026_10_10.md | 24898 | `f22ede7226d2` | verdict/kd | verdict/kd/_kd_unambiguous_meaning_ruling_2026_10_10.md | L |
| 1064 | repo | results/verdict/judgement/_kd_writing_convention_guidance_2026_10_09.md | 20179 | `f47031323865` | verdict/kd | verdict/kd/_kd_writing_convention_guidance_2026_10_09.md | L |
| 1065 | repo | results/verdict/judgement/_kdb2r2_kd14_merge_governance_2026_10_17.md | 26107 | `4fdadf27b70c` | readout/final | readout/final/_kdb2r2_kd14_merge_governance_2026_10_17.md | L |
| 1066 | repo | results/verdict/judgement/_kdb2r3_u13_rulings_effect_2026_10_17.md | 35207 | `688424929409` | verdict/pi | verdict/pi/_kdb2r3_u13_rulings_effect_2026_10_17.md | L |
| 1067 | repo | results/verdict/judgement/_kdk45_remeasure_2026_10_17.md | 31662 | `25ff6e4f31bc` | readout/final | readout/final/_kdk45_remeasure_2026_10_17.md | L |
| 1068 | repo | results/verdict/judgement/_kfp6_nature_and_eta_expface_adjudication_2026_10_19.md | 48993 | `591b73224eee` | verdict/judge | verdict/judge/_kfp6_nature_and_eta_expface_adjudication_2026_10_19.md | L |
| 1069 | repo | results/verdict/judgement/_kill_line_field_value_sourcing_2026_10_15.md | 19471 | `e5615b993000` | verdict/kd | verdict/kd/_kill_line_field_value_sourcing_2026_10_15.md | L |
| 1070 | repo | results/verdict/judgement/_kimi_preexec_final_rulings_effect_2026_10_18.md | 42226 | `7828c5300fdf` | verdict/pi | verdict/pi/_kimi_preexec_final_rulings_effect_2026_10_18.md | L |
| 1071 | repo | results/verdict/judgement/_kimi_receipt_authority_rulings_effect_2026_10_18.md | 62860 | `789fed8aacc7` | verdict/pi | verdict/pi/_kimi_receipt_authority_rulings_effect_2026_10_18.md | L |
| 1072 | repo | results/verdict/judgement/_kl_m41_3_remeasure_2026_10_17.md | 36936 | `20a1ce111547` | readout/final | readout/final/_kl_m41_3_remeasure_2026_10_17.md | L |
| 1073 | repo | results/verdict/judgement/_kl_m41_3_reverdict_2026_10_17.md | 61667 | `63625672139a` | verdict/judge | verdict/judge/_kl_m41_3_reverdict_2026_10_17.md | L |
| 1074 | repo | results/verdict/judgement/_kl_m41_3_reverdict_adoption_effect_2026_10_17.md | 38651 | `27545e411171` | verdict/pi | verdict/pi/_kl_m41_3_reverdict_adoption_effect_2026_10_17.md | L |
| 1075 | repo | results/verdict/judgement/_kl_m41_3_three_seed_exec_2026_10_16.md | 41140 | `3e13344783b0` | readout/final | readout/final/_kl_m41_3_three_seed_exec_2026_10_16.md | L |
| 1076 | repo | results/verdict/judgement/_kl_m41_3_verdict_2026_10_17.md | 33138 | `5dc4e089f458` | verdict/judge | verdict/judge/_kl_m41_3_verdict_2026_10_17.md | L |
| 1077 | repo | results/verdict/judgement/_klm41_2_bootstrap_ci_exec_2026_10_16.md | 45192 | `a467a77d895f` | readout/final | readout/final/_klm41_2_bootstrap_ci_exec_2026_10_16.md | L |
| 1078 | repo | results/verdict/judgement/_krj3_kd_registry_correction_2026_10_12.md | 16648 | `4d514147670a` | verdict/kd | verdict/kd/_krj3_kd_registry_correction_2026_10_12.md | L |
| 1079 | repo | results/verdict/judgement/_kv3s_4_4_rejudge_2026_10_09.md | 42687 | `bc397d5099dd` | verdict/judge | verdict/judge/_kv3s_4_4_rejudge_2026_10_09.md | L |
| 1080 | repo | results/verdict/judgement/_l2_2_duplication_criterion_adjudication_2026_10_19.md | 42517 | `ecbf3288d791` | verdict/judge | verdict/judge/_l2_2_duplication_criterion_adjudication_2026_10_19.md | L |
| 1081 | repo | results/verdict/judgement/_l2_2_two_arms_identity_adjudication_2026_10_19.md | 49080 | `84e8d866054a` | readout/final | readout/final/_l2_2_two_arms_identity_adjudication_2026_10_19.md | L |
| 1082 | repo | results/verdict/judgement/_m08_measured_enumeration_exec_2026_10_16.md | 45462 | `4513f841234e` | verdict/judge | verdict/judge/_m08_measured_enumeration_exec_2026_10_16.md | L |
| 1083 | repo | results/verdict/judgement/_m2_c_tier_corrigendum_2026_10_14.md | 17212 | `f621f836aa86` | verdict/judge | verdict/judge/_m2_c_tier_corrigendum_2026_10_14.md | L |
| 1084 | repo | results/verdict/judgement/_m2_kd_disposition_2026_10_14.md | 21750 | `810e20778e6c` | verdict/kd | verdict/kd/_m2_kd_disposition_2026_10_14.md | L |
| 1085 | repo | results/verdict/judgement/_m2_terminal_verdict_effect_register_2026_10_14.md | 31647 | `17fd10488da0` | verdict/pi | verdict/pi/_m2_terminal_verdict_effect_register_2026_10_14.md | L |
| 1086 | repo | results/verdict/judgement/_m41_verdict_kd_effect_register_2026_10_15.md | 23630 | `f54e8a10acde` | verdict/kd | verdict/kd/_m41_verdict_kd_effect_register_2026_10_15.md | L |
| 1087 | repo | results/verdict/judgement/_m5_reattribution_recommendation_2026_10_14.md | 22700 | `0c9641e512e4` | verdict/judge | verdict/judge/_m5_reattribution_recommendation_2026_10_14.md | L |
| 1088 | repo | results/verdict/judgement/_material_expansion_build_exec_2026_10_16.md | 35966 | `6ca1c64c2c44` | verdict/kd | verdict/kd/_material_expansion_build_exec_2026_10_16.md | L |
| 1089 | repo | results/verdict/judgement/_material_expansion_verdict_kd_effect_register_2026_10_16.md | 35655 | `42a0b3aeff96` | verdict/kd | verdict/kd/_material_expansion_verdict_kd_effect_register_2026_10_16.md | L |
| 1090 | repo | results/verdict/judgement/_material_root45_remeasure_2026_10_17.md | 19477 | `f2a5c4330112` | readout/final | readout/final/_material_root45_remeasure_2026_10_17.md | L |
| 1091 | repo | results/verdict/judgement/_md_a_field_composition_draft_2026_10_18.md | 58572 | `121a3b861261` | readout/final | readout/final/_md_a_field_composition_draft_2026_10_18.md | L |
| 1092 | repo | results/verdict/judgement/_mda8_readlaw_o1_o4_c4_recommendation_2026_10_20.md | 73898 | `1046dd5d1be0` | readout/final | readout/final/_mda8_readlaw_o1_o4_c4_recommendation_2026_10_20.md | L |
| 1093 | repo | results/verdict/judgement/_morning_brief_pending_rulings_2026_10_18.md | 37227 | `9ed6dfdbc62e` | verdict/pi | verdict/pi/_morning_brief_pending_rulings_2026_10_18.md | L |
| 1094 | repo | results/verdict/judgement/_mq19_item6_caption_restatement_2026_10_15.md | 10795 | `656b2324d598` | readout/final | readout/final/_mq19_item6_caption_restatement_2026_10_15.md | L |
| 1095 | repo | results/verdict/judgement/_n2_clause_transcription_supplement_2026_10_12.md | 16192 | `ad8f0d542290` | verdict/judge | verdict/judge/_n2_clause_transcription_supplement_2026_10_12.md | L |
| 1096 | repo | results/verdict/judgement/_n3_o5_terminal_verdict_2026_10_16.md | 39037 | `88df2c228eae` | verdict/judge | verdict/judge/_n3_o5_terminal_verdict_2026_10_16.md | L |
| 1097 | repo | results/verdict/judgement/_n_distinct_grain_verdict_2026_10_17.md | 41028 | `0abaee4aeefb` | verdict/judge | verdict/judge/_n_distinct_grain_verdict_2026_10_17.md | L |
| 1098 | repo | results/verdict/judgement/_n_distinct_proof_2026_10_17.md | 24241 | `2b538eba112a` | readout/final | readout/final/_n_distinct_proof_2026_10_17.md | L |
| 1099 | repo | results/verdict/judgement/_naming_ruling_note_2026_09_29.md | 7843 | `57024f2cd30a` | verdict/kd | verdict/kd/_naming_ruling_note_2026_09_29.md | L |
| 1100 | repo | results/verdict/judgement/_ncc_c6_admission_adjudication_2026_10_21.md | 76725 | `0a3dedb79479` | verdict/judge | verdict/judge/_ncc_c6_admission_adjudication_2026_10_21.md | L |
| 1101 | repo | results/verdict/judgement/_ncc_c6_condition4_adjudication_2026_10_21.md | 62358 | `1c7be88017c7` | verdict/judge | verdict/judge/_ncc_c6_condition4_adjudication_2026_10_21.md | L |
| 1102 | repo | results/verdict/judgement/_ncc_c6_sixpair_measurement_2026_10_21.md | 66029 | `0d127134aa97` | readout/final | readout/final/_ncc_c6_sixpair_measurement_2026_10_21.md | L |
| 1103 | repo | results/verdict/judgement/_ncc_c6_thirdparty_recalc_2026_10_21.md | 87979 | `2e06217bbe61` | readout/final | readout/final/_ncc_c6_thirdparty_recalc_2026_10_21.md | L |
| 1104 | repo | results/verdict/judgement/_next_stage3_dir_optimization_ruling_2026_10_18.md | 11599 | `015b4e200103` | verdict/pi | verdict/pi/_next_stage3_dir_optimization_ruling_2026_10_18.md | L |
| 1105 | repo | results/verdict/judgement/_night_shift_handover_2026_10_14_r2.md | 63091 | `1dbe20a3ba1c` | readout/final | readout/final/_night_shift_handover_2026_10_14_r2.md | L |
| 1106 | repo | results/verdict/judgement/_no_backup_ruling_and_report_caliber_effect_2026_10_17.md | 53634 | `bd748afec4f8` | verdict/pi | verdict/pi/_no_backup_ruling_and_report_caliber_effect_2026_10_17.md | L |
| 1107 | repo | results/verdict/judgement/_noncore_upload_caliber_draft_2026_10_17.md | 29489 | `3ac146a3f8e5` | verdict/judge | verdict/judge/_noncore_upload_caliber_draft_2026_10_17.md | L |
| 1108 | repo | results/verdict/judgement/_numbering_659_overlap_semantic_review_2026_10_14.md | 209219 | `c98d310e183e` | verdict/judge | verdict/judge/_numbering_659_overlap_semantic_review_2026_10_14.md | L |
| 1109 | repo | results/verdict/judgement/_numbering_claims_and_prefix_table_effect_2026_10_13.md | 39933 | `34c1031746fa` | verdict/pi | verdict/pi/_numbering_claims_and_prefix_table_effect_2026_10_13.md | L |
| 1110 | repo | results/verdict/judgement/_numbering_face_recheck_2026_10_13.md | 18487 | `7953a89ea015` | verdict/judge | verdict/judge/_numbering_face_recheck_2026_10_13.md | L |
| 1111 | repo | results/verdict/judgement/_numbering_face_signature_supplement_2026_10_13.md | 12578 | `fd88b3669676` | readout/final | readout/final/_numbering_face_signature_supplement_2026_10_13.md | L |
| 1112 | repo | results/verdict/judgement/_o1_498_lock_scope_deliberation_2026_10_16.md | 52216 | `c9c808083d46` | readout/final | readout/final/_o1_498_lock_scope_deliberation_2026_10_16.md | L |
| 1113 | repo | results/verdict/judgement/_o1_transcription_face_erratum_2026_10_20.md | 81406 | `941002361d54` | verdict/pi | verdict/pi/_o1_transcription_face_erratum_2026_10_20.md | L |
| 1114 | repo | results/verdict/judgement/_p3_disposition_deliberation_2026_10_21.md | 60752 | `14f2e90cc430` | verdict/pi | verdict/pi/_p3_disposition_deliberation_2026_10_21.md | L |
| 1115 | repo | results/verdict/judgement/_p3_path1_codebook_killline_prereg_2026_10_21.md | 114003 | `30925758a3c7` | verdict/kd | verdict/kd/_p3_path1_codebook_killline_prereg_2026_10_21.md | L |
| 1116 | repo | results/verdict/judgement/_pack_card_four_rulings_effect_2026_10_17.md | 46371 | `7fa815bf567d` | verdict/pi | verdict/pi/_pack_card_four_rulings_effect_2026_10_17.md | L |
| 1117 | repo | results/verdict/judgement/_pending_pack_four_rulings_effect_2026_10_17.md | 27925 | `9572516d82e7` | verdict/pi | verdict/pi/_pending_pack_four_rulings_effect_2026_10_17.md | L |
| 1118 | repo | results/verdict/judgement/_pending_residual_minimal_set_2026_10_18.md | 53502 | `0f6098f36bd0` | verdict/judge | verdict/judge/_pending_residual_minimal_set_2026_10_18.md | L |
| 1119 | repo | results/verdict/judgement/_pending_rulings_triage_2026_10_18.md | 63300 | `19c91a3bf7e8` | verdict/pi | verdict/pi/_pending_rulings_triage_2026_10_18.md | L |
| 1120 | repo | results/verdict/judgement/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md | 11798 | `37876a02ad17` | verdict/pi | verdict/pi/_pi_batch_rulings_and_gate1_definition_register_2026_10_12.md | L |
| 1121 | repo | results/verdict/judgement/_pi_four_rulings_adoption_and_effectivity_2026_10_12.md | 14146 | `b99a9f039ecc` | verdict/pi | verdict/pi/_pi_four_rulings_adoption_and_effectivity_2026_10_12.md | L |
| 1122 | repo | results/verdict/judgement/_poststrip_recalc_2026_10_17.md | 42707 | `cfcf430f306c` | readout/final | readout/final/_poststrip_recalc_2026_10_17.md | L |
| 1123 | repo | results/verdict/judgement/_predelete_backup_caliber_draft_2026_10_17.md | 32084 | `653505b88a08` | readout/final | readout/final/_predelete_backup_caliber_draft_2026_10_17.md | L |
| 1124 | repo | results/verdict/judgement/_preexp_degen_gate_data_2026_10_20.json | 77179 | `6d0a2b8a0fa9` | readout/final | readout/final/_preexp_degen_gate_data_2026_10_20.json | L |
| 1125 | repo | results/verdict/judgement/_preexp_degen_gate_recalc_2026_10_20.md | 49419 | `374be409dc47` | readout/final | readout/final/_preexp_degen_gate_recalc_2026_10_20.md | L |
| 1126 | repo | results/verdict/judgement/_preexp_mda8a24_c1_data_2026_10_20.json | 34152 | `aa0541131982` | readout/final | readout/final/_preexp_mda8a24_c1_data_2026_10_20.json | L |
| 1127 | repo | results/verdict/judgement/_preexp_mda8a24_c2c4_data_2026_10_20.json | 95158 | `5df042e20fd7` | readout/final | readout/final/_preexp_mda8a24_c2c4_data_2026_10_20.json | L |
| 1128 | repo | results/verdict/judgement/_preexp_mda8a24_c5_armpairs_data_2026_10_20.json | 54108 | `205323631d0f` | readout/final | readout/final/_preexp_mda8a24_c5_armpairs_data_2026_10_20.json | L |
| 1129 | repo | results/verdict/judgement/_preexp_mda8a24_c5_armpairs_measurement_2026_10_20.md | 57997 | `829e07a7a63b` | readout/final | readout/final/_preexp_mda8a24_c5_armpairs_measurement_2026_10_20.md | L |
| 1130 | repo | results/verdict/judgement/_preexp_mda8a24_c5_armpairs_measurement_data_2026_10_20.json | 68042 | `54f7b164bb22` | readout/final | readout/final/_preexp_mda8a24_c5_armpairs_measurement_data_2026_10_20.json | L |
| 1131 | repo | results/verdict/judgement/_preexp_mda8a24_c5_armpairs_recalc_2026_10_20.md | 59947 | `c038121c9ad5` | readout/final | readout/final/_preexp_mda8a24_c5_armpairs_recalc_2026_10_20.md | L |
| 1132 | repo | results/verdict/judgement/_preexp_mda8a24_recalc_2026_10_20.md | 63402 | `39ffd5e4c47f` | readout/final | readout/final/_preexp_mda8a24_recalc_2026_10_20.md | L |
| 1133 | repo | results/verdict/judgement/_r2_reading_verdict_2026_10_17.md | 43055 | `99b9bff47682` | verdict/kd | verdict/kd/_r2_reading_verdict_2026_10_17.md | L |
| 1134 | repo | results/verdict/judgement/_r2_sep_endogeneity_erratum_2026_10_18.md | 41770 | `ed5591c3c38d` | readout/final | readout/final/_r2_sep_endogeneity_erratum_2026_10_18.md | L |
| 1135 | repo | results/verdict/judgement/_r2b_adoption_and_bytewise_caliber_effect_2026_10_17.md | 31009 | `c8f3a36c152b` | readout/final | readout/final/_r2b_adoption_and_bytewise_caliber_effect_2026_10_17.md | L |
| 1136 | repo | results/verdict/judgement/_r6_supplement_first_version_disposition_2026_10_14.md | 19984 | `b2e0a65f722c` | verdict/pi | verdict/pi/_r6_supplement_first_version_disposition_2026_10_14.md | L |
| 1137 | repo | results/verdict/judgement/_r_pair_question_texts_2026_10_09.md | 30352 | `0ad849022328` | verdict/judge | verdict/judge/_r_pair_question_texts_2026_10_09.md | L |
| 1138 | repo | results/verdict/judgement/_recycle_purge_resolution_and_434_adoption_2026_10_17.md | 44360 | `ba3944565c13` | readout/final | readout/final/_recycle_purge_resolution_and_434_adoption_2026_10_17.md | L |
| 1139 | repo | results/verdict/judgement/_ref_only_no_utility_criteria_effect_2026_10_17.md | 26214 | `7fc20904d015` | verdict/judge | verdict/judge/_ref_only_no_utility_criteria_effect_2026_10_17.md | L |
| 1140 | repo | results/verdict/judgement/_refonly_161_reading_verdict_2026_10_17.md | 39243 | `bd94d12323e0` | verdict/kd | verdict/kd/_refonly_161_reading_verdict_2026_10_17.md | L |
| 1141 | repo | results/verdict/judgement/_remote_root_face_413_68_erratum_2026_10_18.md | 27604 | `81c42f70e271` | verdict/pi | verdict/pi/_remote_root_face_413_68_erratum_2026_10_18.md | L |
| 1142 | repo | results/verdict/judgement/_residual_card1_four_rulings_effect_2026_10_18.md | 52696 | `cff53e597044` | verdict/pi | verdict/pi/_residual_card1_four_rulings_effect_2026_10_18.md | L |
| 1143 | repo | results/verdict/judgement/_resolution_path_rulings_effect_2026_10_17.md | 29195 | `91555b6b7bd6` | verdict/pi | verdict/pi/_resolution_path_rulings_effect_2026_10_17.md | L |
| 1144 | repo | results/verdict/judgement/_results_path_mapping_2026_10_21.md | 274617 | `5653b96d93c4` | readout/final | readout/final/_results_path_mapping_2026_10_21.md | L |
| 1145 | repo | results/verdict/judgement/_ritt_def_adoption_and_remeasure_effect_2026_10_17.md | 28232 | `a7539659c5df` | readout/final | readout/final/_ritt_def_adoption_and_remeasure_effect_2026_10_17.md | L |
| 1146 | repo | results/verdict/judgement/_ritt_def_proof_2026_10_17.md | 23310 | `5d411ebf07ed` | verdict/judge | verdict/judge/_ritt_def_proof_2026_10_17.md | L |
| 1147 | repo | results/verdict/judgement/_rpp_perseed_recalc_2026_10_17.md | 30617 | `7e693b27c1f7` | readout/final | readout/final/_rpp_perseed_recalc_2026_10_17.md | L |
| 1148 | repo | results/verdict/judgement/_ruled_unclosed_closure_verdict_2026_10_18.md | 54716 | `03fe4d044c78` | verdict/judge | verdict/judge/_ruled_unclosed_closure_verdict_2026_10_18.md | L |
| 1149 | repo | results/verdict/judgement/_s3_s5_explanation_and_disposition_verdict_2026_10_17.md | 28816 | `2c1479af62cb` | verdict/pi | verdict/pi/_s3_s5_explanation_and_disposition_verdict_2026_10_17.md | L |
| 1150 | repo | results/verdict/judgement/_s3_s5_kd_effect_2026_10_17.md | 33609 | `eea5245b31da` | verdict/kd | verdict/kd/_s3_s5_kd_effect_2026_10_17.md | L |
| 1151 | repo | results/verdict/judgement/_s3_s5_kd_effect_2026_10_17_append1.md | 17624 | `905be2174c52` | verdict/kd | verdict/kd/_s3_s5_kd_effect_2026_10_17_append1.md | L |
| 1152 | repo | results/verdict/judgement/_s3_th_v21_reconciliation_verdict_2026_10_01.md | 51073 | `84fa6996b656` | verdict/judge | verdict/judge/_s3_th_v21_reconciliation_verdict_2026_10_01.md | L |
| 1153 | repo | results/verdict/judgement/_s3prime_alert_disposition_judgment_2026_10_11.md | 53188 | `e7fcbc290a7e` | verdict/pi | verdict/pi/_s3prime_alert_disposition_judgment_2026_10_11.md | L |
| 1154 | repo | results/verdict/judgement/_s4_final_ruling_effectivity_register_2026_10_09.md | 32975 | `21f2926efc5d` | verdict/pi | verdict/pi/_s4_final_ruling_effectivity_register_2026_10_09.md | L |
| 1155 | repo | results/verdict/judgement/_s4_heldout_sampling_caliber_ruling_2026_10_09.md | 35453 | `fb1b696de1d6` | verdict/pi | verdict/pi/_s4_heldout_sampling_caliber_ruling_2026_10_09.md | L |
| 1156 | repo | results/verdict/judgement/_s4_kex_killline_freeze_2026_10_10.md | 15284 | `6269d0c6fd10` | verdict/kd | verdict/kd/_s4_kex_killline_freeze_2026_10_10.md | L |
| 1157 | repo | results/verdict/judgement/_scroll_wave1_four_rulings_effect_2026_10_18.md | 51739 | `2813eea5584a` | verdict/pi | verdict/pi/_scroll_wave1_four_rulings_effect_2026_10_18.md | L |
| 1158 | repo | results/verdict/judgement/_scroll_wave2_four_rulings_effect_2026_10_18.md | 51949 | `57881886e428` | verdict/pi | verdict/pi/_scroll_wave2_four_rulings_effect_2026_10_18.md | L |
| 1159 | repo | results/verdict/judgement/_scroll_wave4_three_rulings_effect_2026_10_18.md | 51604 | `0db1e827d943` | verdict/pi | verdict/pi/_scroll_wave4_three_rulings_effect_2026_10_18.md | L |
| 1160 | repo | results/verdict/judgement/_scroll_wave5_four_rulings_effect_2026_10_18.md | 71453 | `c44183973483` | verdict/pi | verdict/pi/_scroll_wave5_four_rulings_effect_2026_10_18.md | L |
| 1161 | repo | results/verdict/judgement/_seed_double_identifier_finalization_2026_10_11.md | 26864 | `6904852f8ceb` | verdict/pi | verdict/pi/_seed_double_identifier_finalization_2026_10_11.md | L |
| 1162 | repo | results/verdict/judgement/_stage1_killline_values_proposal_2026_10_21.md | 90488 | `5bccb1af707d` | verdict/kd | verdict/kd/_stage1_killline_values_proposal_2026_10_21.md | L |
| 1163 | repo | results/verdict/judgement/_stage1_killline_values_proposal_second_reading_2026_10_21.md | 99794 | `60f02aa54930` | verdict/kd | verdict/kd/_stage1_killline_values_proposal_second_reading_2026_10_21.md | L |
| 1164 | repo | results/verdict/judgement/_stage3_close_and_cmp2_rulings_effect_2026_10_18.md | 54315 | `22843cb2ce08` | verdict/pi | verdict/pi/_stage3_close_and_cmp2_rulings_effect_2026_10_18.md | L |
| 1165 | repo | results/verdict/judgement/_stage_sequence_ruling_effect_2026_10_17.md | 18115 | `b582bde59d6d` | verdict/pi | verdict/pi/_stage_sequence_ruling_effect_2026_10_17.md | L |
| 1166 | repo | results/verdict/judgement/_strict3_verdict_2026_10_17.md | 41236 | `d392bd36ec34` | verdict/judge | verdict/judge/_strict3_verdict_2026_10_17.md | L |
| 1167 | repo | results/verdict/judgement/_supplement_500_combo_exec_2026_10_16.md | 46503 | `ee7a1563d850` | readout/final | readout/final/_supplement_500_combo_exec_2026_10_16.md | L |
| 1168 | repo | results/verdict/judgement/_t1_exp2_result_2026_10_09.json | 35239 | `d9ccd75c652b` | readout/final | readout/final/_t1_exp2_result_2026_10_09.json | L |
| 1169 | repo | results/verdict/judgement/_t1_qwen_temp_sweep_r2_result_2026_10_09.json | 58712 | `8d6242da158c` | readout/final | readout/final/_t1_qwen_temp_sweep_r2_result_2026_10_09.json | L |
| 1170 | repo | results/verdict/judgement/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md | 42817 | `9c18b9893579` | verdict/judge | verdict/judge/_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md | L |
| 1171 | repo | results/verdict/judgement/_t1_qwen_temp_sweep_verdict_2026_10_09.md | 21672 | `dfc858d3d930` | verdict/judge | verdict/judge/_t1_qwen_temp_sweep_verdict_2026_10_09.md | L |
| 1172 | repo | results/verdict/judgement/_t1_substrate_gap_precondition_2026_10_01.md | 22196 | `a019602cfab2` | verdict/judge | verdict/judge/_t1_substrate_gap_precondition_2026_10_01.md | L |
| 1173 | repo | results/verdict/judgement/_t3trap_answerable_build_exec_2026_10_15.md | 31808 | `b9e9c9b5a06b` | verdict/kd | verdict/kd/_t3trap_answerable_build_exec_2026_10_15.md | L |
| 1174 | repo | results/verdict/judgement/_t3trap_kd3_bprime_effect_register_2026_10_15.md | 27675 | `7a4a0ed3222c` | verdict/pi | verdict/pi/_t3trap_kd3_bprime_effect_register_2026_10_15.md | L |
| 1175 | repo | results/verdict/judgement/_t3trap_kd3_disposition_deliberation_2026_10_15.md | 29776 | `b58775c33928` | verdict/pi | verdict/pi/_t3trap_kd3_disposition_deliberation_2026_10_15.md | L |
| 1176 | repo | results/verdict/judgement/_t4_key_preexp_killline_prereg_2026_10_21.md | 168029 | `50780b0cd677` | verdict/kd | verdict/kd/_t4_key_preexp_killline_prereg_2026_10_21.md | L |
| 1177 | repo | results/verdict/judgement/_t4t5_layer1_application_2026_10_21.md | 78379 | `7098861f241a` | readout/final | readout/final/_t4t5_layer1_application_2026_10_21.md | L |
| 1178 | repo | results/verdict/judgement/_t5_generator_build_exec_2026_10_15.md | 26857 | `1fd4a9465809` | verdict/kd | verdict/kd/_t5_generator_build_exec_2026_10_15.md | L |
| 1179 | repo | results/verdict/judgement/_t5_prereq_premise_correction_2026_10_21.md | 52401 | `3bc96df61b08` | verdict/pi | verdict/pi/_t5_prereq_premise_correction_2026_10_21.md | L |
| 1180 | repo | results/verdict/judgement/_th_id_attribution_verification_2026_10_09.md | 8409 | `94740f8d3c8d` | verdict/pi | verdict/pi/_th_id_attribution_verification_2026_10_09.md | L |
| 1181 | repo | results/verdict/judgement/_third_batch_four_rulings_effect_2026_10_18.md | 64832 | `aef5ae501043` | verdict/pi | verdict/pi/_third_batch_four_rulings_effect_2026_10_18.md | L |
| 1182 | repo | results/verdict/judgement/_thirdparty_16_overwrite_necessity_2026_10_18.md | 14122 | `6435ecc3a540` | verdict/pi | verdict/pi/_thirdparty_16_overwrite_necessity_2026_10_18.md | L |
| 1183 | repo | results/verdict/judgement/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md | 43428 | `322582749c53` | verdict/pi | verdict/pi/_thirdparty_16_overwrite_ruling_effect_2026_10_18.md | L |
| 1184 | repo | results/verdict/judgement/_three_items_alternative_deliberation_judgment_2026_10_13.md | 64069 | `40c154d64169` | verdict/judge | verdict/judge/_three_items_alternative_deliberation_judgment_2026_10_13.md | L |
| 1185 | repo | results/verdict/judgement/_three_seed_measurement_exec_2026_10_16.md | 48178 | `0e0716fde41f` | readout/final | readout/final/_three_seed_measurement_exec_2026_10_16.md | L |
| 1186 | repo | results/verdict/judgement/_trae_issues_disposition_schedule_2026_10_12.md | 12849 | `57b9dcca2630` | verdict/pi | verdict/pi/_trae_issues_disposition_schedule_2026_10_12.md | L |
| 1187 | repo | results/verdict/judgement/_u01_u15_recheck_after_rulings_2026_10_17.md | 39219 | `71c6b834dd9d` | verdict/pi | verdict/pi/_u01_u15_recheck_after_rulings_2026_10_17.md | L |
| 1188 | repo | results/verdict/judgement/_u10_fail_h0_verdict_2026_10_18.md | 59918 | `0884b8f98b96` | verdict/judge | verdict/judge/_u10_fail_h0_verdict_2026_10_18.md | L |
| 1189 | repo | results/verdict/judgement/_u10_s3_denominator_rulings_effect_2026_10_18.md | 79234 | `97719ffddda6` | verdict/pi | verdict/pi/_u10_s3_denominator_rulings_effect_2026_10_18.md | L |
| 1190 | repo | results/verdict/judgement/_u5_referent_registry_correction_2026_10_12.md | 25048 | `111a76fa9667` | verdict/pi | verdict/pi/_u5_referent_registry_correction_2026_10_12.md | L |
| 1191 | repo | results/verdict/judgement/_u5_semantics_resolution_2026_10_12.md | 24046 | `8b5f1a495a99` | verdict/pi | verdict/pi/_u5_semantics_resolution_2026_10_12.md | L |
| 1192 | repo | results/verdict/judgement/_u_axis_active_ruling_register_2026_10_16.md | 22219 | `30fed54c3d09` | verdict/pi | verdict/pi/_u_axis_active_ruling_register_2026_10_16.md | L |
| 1193 | repo | results/verdict/judgement/_u_axis_equation_direction_deliberation_2026_10_16.md | 40049 | `5b6847e424b0` | readout/final | readout/final/_u_axis_equation_direction_deliberation_2026_10_16.md | L |
| 1194 | repo | results/verdict/judgement/_u_axis_input_vs_kdb2_recheck_2026_10_17.md | 25669 | `45e62039cee3` | verdict/judge | verdict/judge/_u_axis_input_vs_kdb2_recheck_2026_10_17.md | L |
| 1195 | repo | results/verdict/judgement/_u_cluster1_verdict_2026_10_17.md | 40213 | `0172e2a52c80` | verdict/judge | verdict/judge/_u_cluster1_verdict_2026_10_17.md | L |
| 1196 | repo | results/verdict/judgement/_u_cluster2_verdict_2026_10_17.md | 47057 | `4dd0d2f38d46` | verdict/judge | verdict/judge/_u_cluster2_verdict_2026_10_17.md | L |
| 1197 | repo | results/verdict/judgement/_u_domain3_carrier_1494_2026_10_16.md | 42227 | `59f52f8bb287` | readout/final | readout/final/_u_domain3_carrier_1494_2026_10_16.md | L |
| 1198 | repo | results/verdict/judgement/_u_lock_recalc_2026_10_17.md | 24411 | `6793b0b56925` | verdict/judge | verdict/judge/_u_lock_recalc_2026_10_17.md | L |
| 1199 | repo | results/verdict/judgement/_v3_n_recheck_llm_verdict_2026_09_27.md | 21332 | `426cfe18cf65` | verdict/judge | verdict/judge/_v3_n_recheck_llm_verdict_2026_09_27.md | L |
| 1200 | repo | results/verdict/judgement/_v3_recheck_26b_verdict_prep_2026_10_01.md | 36133 | `3aab3f7660fc` | verdict/kd | verdict/kd/_v3_recheck_26b_verdict_prep_2026_10_01.md | L |
| 1201 | repo | results/verdict/judgement/_v3_recheck_verdict_register_2026_09_27.md | 112085 | `d9b6b974cfc1` | verdict/pi | verdict/pi/_v3_recheck_verdict_register_2026_09_27.md | L |
| 1202 | repo | results/verdict/judgement/_v3_supplement_verdict_2026_09_23.md | 15247 | `b70211bfa83e` | verdict/judge | verdict/judge/_v3_supplement_verdict_2026_09_23.md | L |
| 1203 | repo | results/verdict/judgement/_v4_pi_cot_v3_verdict_v3.md | 53751 | `bb44fdc7ab0f` | verdict/kd | verdict/kd/_v4_pi_cot_v3_verdict_v3.md | L |
| 1204 | repo | results/verdict/judgement/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md | 42157 | `41d29f4deb70` | verdict/pi | verdict/pi/_v4_pi_cot_v3_verdict_v3_signoff_2026_09_27.md | L |
| 1205 | repo | results/verdict/judgement/_v4_supp_l14_n11full_verdict.md | 19697 | `8eef73bf9856` | verdict/judge | verdict/judge/_v4_supp_l14_n11full_verdict.md | L |
| 1206 | repo | results/verdict/judgement/_v4_supp_l14v3_n26_verdict.md | 65978 | `df6453d57f8a` | verdict/kd | verdict/kd/_v4_supp_l14v3_n26_verdict.md | L |
| 1207 | repo | results/verdict/judgement/_v4_supp_t15_verdict.md | 54377 | `3cb5c2f59961` | verdict/judge | verdict/judge/_v4_supp_t15_verdict.md | L |
| 1208 | repo | results/verdict/judgement/_v4_supp_t15r2_verdict.md | 65638 | `963725dbd82a` | verdict/judge | verdict/judge/_v4_supp_t15r2_verdict.md | L |
| 1209 | repo | results/verdict/judgement/_v4_supp_t1_verdict.md | 29106 | `0ad42625f333` | verdict/judge | verdict/judge/_v4_supp_t1_verdict.md | L |
| 1210 | repo | results/verdict/judgement/_v4_track2_multimodel_verdict_2026_09_23.md | 12883 | `44d9bad9039b` | verdict/judge | verdict/judge/_v4_track2_multimodel_verdict_2026_09_23.md | L |
| 1211 | repo | results/verdict/judgement/_v5_fake_verdict_session_log_2026_09_28.md | 18877 | `132bfa0c02f5` | verdict/pi | verdict/pi/_v5_fake_verdict_session_log_2026_09_28.md | L |
| 1212 | repo | results/verdict/judgement/_v5_fake_verdict_v1x_prereg_2026_09_28.md | 28484 | `088085d6c90d` | verdict/kd | verdict/kd/_v5_fake_verdict_v1x_prereg_2026_09_28.md | L |
| 1213 | repo | results/verdict/judgement/_v5_gt_verdict_2026_09_29.md | 57227 | `45648b0ec940` | verdict/kd | verdict/kd/_v5_gt_verdict_2026_09_29.md | L |
| 1214 | repo | results/verdict/judgement/_v5_item35_v2_verdict_2026_09_29.md | 26232 | `b59bef293712` | verdict/kd | verdict/kd/_v5_item35_v2_verdict_2026_09_29.md | L |
| 1215 | repo | results/verdict/judgement/_value_card_template_7col_2026_10_13.md | 17013 | `33f68fd8ea3b` | readout/final | readout/final/_value_card_template_7col_2026_10_13.md | L |
| 1216 | repo | results/verdict/judgement/_weighted_law_killline_prereg_2026_10_21.md | 69409 | `769b345d9bdf` | verdict/kd | verdict/kd/_weighted_law_killline_prereg_2026_10_21.md | L |
| 1217 | repo | results/verdict/judgement/_whitelist_and_scope_ruling_effect_2026_10_17.md | 56228 | `afd2a78e6a4f` | verdict/pi | verdict/pi/_whitelist_and_scope_ruling_effect_2026_10_17.md | L |
| 1218 | repo | results/verdict/judgement/_xiang14_third_trace_and_pullback_2026_10_18.md | 7129 | `567cb4e5bfe0` | verdict/pi | verdict/pi/_xiang14_third_trace_and_pullback_2026_10_18.md | L |
| 1219 | repo | results/verdict/judgement/_xiang8_xiang12_deliberation_judgment_2026_10_13.md | 36926 | `3c6edf11135d` | verdict/judge | verdict/judge/_xiang8_xiang12_deliberation_judgment_2026_10_13.md | L |
| 1220 | repo | results/verdict/judgement/_zerocall_criterion_redefinition_2026_10_17.md | 31602 | `f2bed1e98f62` | readout/final | readout/final/_zerocall_criterion_redefinition_2026_10_17.md | L |
| 1221 | repo | results/verdict/judgement/c5_guard_0_1_recheck_verdict_2026_10_01.md | 33287 | `24418fa60ede` | verdict/judge | verdict/judge/c5_guard_0_1_recheck_verdict_2026_10_01.md | L |
| 1222 | repo | results/verdict/judgement/d7_5anchor_60cells_9model_verdict_2026_09_18.json | 2456 | `4505cca79c15` | readout/final | readout/final/d7_5anchor_60cells_9model_verdict_2026_09_18.json | L |
| 1223 | repo | results/verdict/pi_register/_pi_card_payload_extraction_2026_10_20.json | 67321 | `df0ad50fce40` | readout/final | readout/final/_pi_card_payload_extraction_2026_10_20.json | L |
| 1224 | repo | results/verdict/pi_register/_pi_card_payload_extraction_2026_10_20.md | 53460 | `f8545e95374f` | verdict/pi | verdict/pi/_pi_card_payload_extraction_2026_10_20.md | L |
| 1225 | repo | results/verdict/pi_register/_pi_decision_backlog_consolidated_2026_10_21.md | 100274 | `87d3bac68420` | verdict/kd | verdict/kd/_pi_decision_backlog_consolidated_2026_10_21.md | L |
| 1226 | repo | results/verdict/pi_register/_pi_register_dedup_note_2026_10_21.md | 3911 | `ae893e953781` | verdict/pi | verdict/pi/_pi_register_dedup_note_2026_10_21.md | L |
| 1227 | repo | results/verdict/pi_register/_v4_pi_cot_v2_coding_review_2026_09_26.md | 42914 | `5fbec21e0ad2` | verdict/judge | verdict/judge/_v4_pi_cot_v2_coding_review_2026_09_26.md | L |
| 1228 | repo | results/verdict/pi_register/_v4_pi_cot_v2_prereg.md | 4247 | `cc25c5149ce1` | verdict/kd | verdict/kd/_v4_pi_cot_v2_prereg.md | L |
| 1229 | repo | results/verdict/pi_register/_v4_pi_cot_v2_questionnaire_v1.md | 12402 | `7b14cdb31d21` | verdict/kd | verdict/kd/_v4_pi_cot_v2_questionnaire_v1.md | L |
| 1230 | repo | results/verdict/pi_register/_v4_pi_cot_v2_result_v2.json | 18089 | `f86727c857a8` | readout/final | readout/final/_v4_pi_cot_v2_result_v2.json | L |
| 1231 | repo | results/verdict/pi_register/_v4_pi_cot_v2_ruleset_v2.json | 6179 | `c5b3dd141655` | readout/final | readout/final/_v4_pi_cot_v2_ruleset_v2.json | L |
| 1232 | repo | results/verdict/pi_register/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md | 10251 | `58ed6be022ed` | readout/final | readout/final/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md | L |
| 1233 | repo | results/verdict/pi_register/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json | 26891 | `cbc14a76f038` | readout/final | readout/final/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json | L |
| 1234 | repo | results/verdict/pi_register/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md | 12851 | `44c4d570375c` | verdict/pi | verdict/pi/_v4_pi_cot_v3_missing_ledger_correction_2026_09_28.md | L |
| 1235 | repo | results/verdict/pi_register/_v4_pi_cot_v3_prereg.md | 27223 | `b7547329af2e` | verdict/kd | verdict/kd/_v4_pi_cot_v3_prereg.md | L |
| 1236 | repo | results/verdict/pi_register/_v4_pi_cot_v3_result_v3.json | 27203 | `585714f9660c` | readout/final | readout/final/_v4_pi_cot_v3_result_v3.json | L |
| 1237 | repo | results/verdict/pi_register/_v4_pi_cot_v3_result_v3r1_2026_09_27.json | 22292 | `735c03db1ae9` | readout/final | readout/final/_v4_pi_cot_v3_result_v3r1_2026_09_27.json | L |
| 1238 | repo | results/verdict/pi_register/_v4_pi_cot_v3_ruleset_v3.json | 21392 | `9d77a5e2cbab` | readout/final | readout/final/_v4_pi_cot_v3_ruleset_v3.json | L |
| 1239 | repo | results/verdict/pi_register/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md | 11385 | `75aedf9ba95e` | readout/final | readout/final/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md | L |
| 1240 | repo | results/work/process/_archive_zone_scan_violation_register_2026_10_12.md | 5723 | `9391d1293f9b` | verdict/pi | verdict/pi/_archive_zone_scan_violation_register_2026_10_12.md | L |
| 1241 | repo | results/work/process/_census_543_to_256_correction_2026_10_14.md | 5435 | `b154a961c27f` | readout/final | readout/final/_census_543_to_256_correction_2026_10_14.md | L |
| 1242 | repo | results/work/process/_census_exit_four_rulings_effect_2026_10_17.md | 44267 | `ac0928f38b85` | verdict/pi | verdict/pi/_census_exit_four_rulings_effect_2026_10_17.md | L |
| 1243 | repo | results/work/process/_census_text_exec_inconsistency_register_2026_10_14.md | 5634 | `55cd847688b3` | verdict/pi | verdict/pi/_census_text_exec_inconsistency_register_2026_10_14.md | L |
| 1244 | repo | results/work/process/_cleanup_exec_register_2026_10_15.md | 36349 | `d53036b01062` | verdict/pi | verdict/pi/_cleanup_exec_register_2026_10_15.md | L |
| 1245 | repo | results/work/process/_cleanup_inventory_2026_10_15.md | 124617 | `9194110cb3f3` | readout/final | readout/final/_cleanup_inventory_2026_10_15.md | L |
| 1246 | repo | results/work/process/_cleanup_noise_register_2026_10_21.md | 16415 | `5ca28bb4c73a` | verdict/pi | verdict/pi/_cleanup_noise_register_2026_10_21.md | L |
| 1247 | repo | results/work/process/_cleanup_r2_plus83_exec_register_2026_10_17.md | 22779 | `e0492696dd12` | verdict/pi | verdict/pi/_cleanup_r2_plus83_exec_register_2026_10_17.md | L |
| 1248 | repo | results/work/process/_cleanup_r2_repo_sub_exec_register_2026_10_17.md | 21686 | `c6f89b961d14` | verdict/pi | verdict/pi/_cleanup_r2_repo_sub_exec_register_2026_10_17.md | L |
| 1249 | repo | results/work/process/_compound_numbering_census_2026_10_13.md | 38268 | `956d19e4e670` | readout/final | readout/final/_compound_numbering_census_2026_10_13.md | L |
| 1250 | repo | results/work/process/_fiveverdict_census_2026_10_17.md | 31237 | `0b9512c6b68b` | verdict/judge | verdict/judge/_fiveverdict_census_2026_10_17.md | L |
| 1251 | repo | results/work/process/_kd_family_census_2026_10_20.md | 404394 | `69b133558795` | verdict/kd | verdict/kd/_kd_family_census_2026_10_20.md | L |
| 1252 | repo | results/work/process/_kd_flip_census_2026_10_17.md | 38344 | `cbb42aae0865` | verdict/kd | verdict/kd/_kd_flip_census_2026_10_17.md | L |
| 1253 | repo | results/work/process/_kd_h5_background_tasks_full_scan_2026_10_20.md | 70187 | `165ac1c8f063` | verdict/kd | verdict/kd/_kd_h5_background_tasks_full_scan_2026_10_20.md | L |
| 1254 | repo | results/work/process/_kd_h5_background_tasks_full_scan_data_2026_10_20.json | 569582 | `c84936df607a` | readout/final | readout/final/_kd_h5_background_tasks_full_scan_data_2026_10_20.json | L |
| 1255 | repo | results/work/process/_p0_scan_2026_10_12.json | 20879 | `224b7fc0dcdf` | readout/final | readout/final/_p0_scan_2026_10_12.json | L |
| 1256 | repo | results/work/process/_repo_noise_cleanup_register_2026_10_13.md | 76649 | `f63672dc0250` | verdict/pi | verdict/pi/_repo_noise_cleanup_register_2026_10_13.md | L |
| 1257 | repo | results/work/process/_stage3_1_bulk_reorg_completion_register_2026_10_12.md | 15818 | `7439157b7be4` | verdict/pi | verdict/pi/_stage3_1_bulk_reorg_completion_register_2026_10_12.md | L |
| 1258 | repo | results/work/process/_stage3_r2_cleanup_register_2026_10_18.md | 62885 | `d6b1dc8f8a02` | verdict/pi | verdict/pi/_stage3_r2_cleanup_register_2026_10_18.md | L |
| 1259 | repo | results/work/process/_t1_substrate_gap_census_2026_10_01.md | 32371 | `62fb594be3f9` | readout/final | readout/final/_t1_substrate_gap_census_2026_10_01.md | L |
| 1260 | repo | results/work/process/_t3_repro_probe_2026_10_16.md | 33722 | `1a104886964f` | readout/final | readout/final/_t3_repro_probe_2026_10_16.md | L |
| 1261 | repo | results/work/process/_temp_cleanup_register_2026_10_13.md | 10598 | `89cbdf1eefab` | verdict/pi | verdict/pi/_temp_cleanup_register_2026_10_13.md | L |
| 1262 | repo | results/work/process/_v4_closeout_moves_and_cleanup_register_2026_10_12.md | 18568 | `69a834caf812` | verdict/pi | verdict/pi/_v4_closeout_moves_and_cleanup_register_2026_10_12.md | L |
| 1263 | repo | results/work/process/_v4_supp_l14v3_batch2_r2_models_probe.json | 1503 | `3c9dc60b5071` | readout/final | readout/final/_v4_supp_l14v3_batch2_r2_models_probe.json | L |
| 1264 | repo | results/work/process/_whitelist_backup_470_cleanup_register_2026_10_18.md | 14642 | `4b951b0accd9` | verdict/pi | verdict/pi/_whitelist_backup_470_cleanup_register_2026_10_18.md | L |
| 1265 | repo | results/work/process/_whitelist_backup_669_cleanup_register_2026_10_18.md | 151245 | `26dc055bed66` | verdict/pi | verdict/pi/_whitelist_backup_669_cleanup_register_2026_10_18.md | L |
| 1266 | repo | run_benchmark_v1_3.py | 10690 | `54ea2644df14` | source/tool | source/tool/run_benchmark_v1_3.py | L |
| 1267 | repo | run_benchmark_v1_4_gsm8k.py | 11253 | `fac50b283da5` | source/tool | source/tool/run_benchmark_v1_4_gsm8k.py | L |
| 1268 | repo | run_benchmark_v1_4_strategyqa.py | 14537 | `f523875a15db` | source/tool | source/tool/run_benchmark_v1_4_strategyqa.py | L |
| 1269 | repo | run_g2_ensemble.py | 8907 | `e3914712a984` | source/tool | source/tool/run_g2_ensemble.py | L |
| 1270 | repo | run_v15_experiment.py | 22761 | `58a5623f3aa1` | source/tool | source/tool/run_v15_experiment.py | L |
| 1271 | repo | run_v16_llm_prior.py | 13423 | `6350bbaecb81` | source/tool | source/tool/run_v16_llm_prior.py | L |
| 1272 | repo | run_v17_fixed_sampler.py | 10435 | `3e54797eedeb` | source/tool | source/tool/run_v17_fixed_sampler.py | L |
| 1273 | repo | run_v17_fusion_fix.py | 10236 | `b592470c47ae` | source/tool | source/tool/run_v17_fusion_fix.py | L |
| 1274 | repo | run_v17_multigraph.py | 5682 | `ca7e6031272c` | source/tool | source/tool/run_v17_multigraph.py | L |
| 1275 | repo | run_v18_api_supplements.py | 42681 | `aef28d92d763` | source/tool | source/tool/run_v18_api_supplements.py | L |
| 1276 | repo | run_v19_benchmark_fixes.py | 22802 | `674c2e5349cf` | source/tool | source/tool/run_v19_benchmark_fixes.py | L |
| 1277 | repo | run_v19_fullrank.py | 8976 | `8d1067e4e27b` | source/tool | source/tool/run_v19_fullrank.py | L |
| 1278 | repo | run_v19_meanfield.py | 11690 | `67ef3779478a` | source/tool | source/tool/run_v19_meanfield.py | L |
| 1279 | repo | run_v19_quickwins.py | 10509 | `93958a96b19a` | source/tool | source/tool/run_v19_quickwins.py | L |
| 1280 | repo | run_v20_baselines.py | 12435 | `1b9815fad7ca` | source/tool | source/tool/run_v20_baselines.py | L |
| 1281 | repo | run_v20_bigquiz_eval.py | 9091 | `1c1a82f4b48a` | source/tool | source/tool/run_v20_bigquiz_eval.py | L |
| 1282 | repo | run_v20_bigquiz_fetch.py | 7808 | `f810f3a34eb2` | source/tool | source/tool/run_v20_bigquiz_fetch.py | L |
| 1283 | repo | run_v20_corpus_eval.py | 20470 | `2fad3b28d34c` | source/tool | source/tool/run_v20_corpus_eval.py | L |
| 1284 | repo | run_v20_cot_fetch.py | 3323 | `b4a214c4e50f` | source/tool | source/tool/run_v20_cot_fetch.py | L |
| 1285 | repo | run_v20_crossval_eval.py | 14379 | `1cdc6c37b236` | source/tool | source/tool/run_v20_crossval_eval.py | L |
| 1286 | repo | run_v20_crossval_fetch.py | 4958 | `3465b43e2f8a` | source/tool | source/tool/run_v20_crossval_fetch.py | L |
| 1287 | repo | run_v20_familyL_fetch.py | 2088 | `ff38dbb3de7f` | source/tool | source/tool/run_v20_familyL_fetch.py | L |
| 1288 | repo | run_v20_familyL_ingest.py | 6108 | `c5d96c1f0522` | source/tool | source/tool/run_v20_familyL_ingest.py | L |
| 1289 | repo | run_v20_fastcheck.py | 7243 | `b6585a30d808` | source/tool | source/tool/run_v20_fastcheck.py | L |
| 1290 | repo | run_v20_gt.py | 9824 | `9f6df7e94cdc` | source/tool | source/tool/run_v20_gt.py | L |
| 1291 | repo | run_v20_gt2b.py | 9076 | `361aff516219` | source/tool | source/tool/run_v20_gt2b.py | L |
| 1292 | repo | run_v20_gt3_eval.py | 6983 | `6a234eee29b3` | source/tool | source/tool/run_v20_gt3_eval.py | L |
| 1293 | repo | run_v20_gt3_fetch.py | 3858 | `1853f7e82a3a` | source/tool | source/tool/run_v20_gt3_fetch.py | L |
| 1294 | repo | run_v20_gt3b_fetch.py | 3135 | `efaa93762269` | source/tool | source/tool/run_v20_gt3b_fetch.py | L |
| 1295 | repo | run_v20_gt3c_fetch.py | 3193 | `48b659b95984` | source/tool | source/tool/run_v20_gt3c_fetch.py | L |
| 1296 | repo | run_v20_gt5.py | 14957 | `32c03f5739d7` | source/tool | source/tool/run_v20_gt5.py | L |
| 1297 | repo | run_v20_gt5b.py | 10419 | `3b344435f4ea` | source/tool | source/tool/run_v20_gt5b.py | L |
| 1298 | repo | run_v20_gt6.py | 11010 | `c5dcdb0f12e2` | source/tool | source/tool/run_v20_gt6.py | L |
| 1299 | repo | run_v20_gt7.py | 17509 | `38071308e9ef` | source/tool | source/tool/run_v20_gt7.py | L |
| 1300 | repo | run_v20_gt8.py | 13876 | `d07233229279` | source/tool | source/tool/run_v20_gt8.py | L |
| 1301 | repo | run_v20_gt8b_eval.py | 9196 | `07b74332ebc2` | source/tool | source/tool/run_v20_gt8b_eval.py | L |
| 1302 | repo | run_v20_gt8b_fetch.py | 6558 | `fce719ad054d` | source/tool | source/tool/run_v20_gt8b_fetch.py | L |
| 1303 | repo | run_v20_gt8b_ingest.py | 5676 | `5e3db6f4869d` | source/tool | source/tool/run_v20_gt8b_ingest.py | L |
| 1304 | repo | run_v20_gt8c_eval.py | 9594 | `6d6db8bdbb06` | source/tool | source/tool/run_v20_gt8c_eval.py | L |
| 1305 | repo | run_v20_gt8c_fetch.py | 8068 | `8079a5dbe251` | source/tool | source/tool/run_v20_gt8c_fetch.py | L |
| 1306 | repo | run_v20_gt8c_ingest.py | 5866 | `81690a38f421` | source/tool | source/tool/run_v20_gt8c_ingest.py | L |
| 1307 | repo | run_v20_photonics.py | 7615 | `ec00cb18f95a` | source/tool | source/tool/run_v20_photonics.py | L |
| 1308 | repo | run_v20_quizbank.py | 8744 | `3b2a7dd2044c` | source/tool | source/tool/run_v20_quizbank.py | L |
| 1309 | repo | run_v20_vector_audit.py | 4717 | `16a270a6bdab` | source/tool | source/tool/run_v20_vector_audit.py | L |
| 1310 | repo | run_v21_gtformal.py | 16600 | `9bbe43f41fa8` | source/tool | source/tool/run_v21_gtformal.py | L |
| 1311 | repo | run_v22_e95ci.py | 3058 | `8470e3ce8cae` | source/tool | source/tool/run_v22_e95ci.py | L |
| 1312 | repo | run_v22_p1c.py | 7236 | `6e9673205dc0` | source/tool | source/tool/run_v22_p1c.py | L |
| 1313 | repo | scripts/run_deepseek_v41_30cells_v2.py | 14017 | `c7411ae13ec0` | source/tool | source/tool/run_deepseek_v41_30cells_v2.py | L |
| 1314 | repo | scripts/run_deepseek_v41_30cells_v3.py | 13955 | `03bc34ea88a8` | source/tool | source/tool/run_deepseek_v41_30cells_v3.py | L |
| 1315 | repo | scripts/run_deepseek_v41_60cells_v2_startup.py | 16071 | `769e1d04503b` | source/tool | source/tool/run_deepseek_v41_60cells_v2_startup.py | L |
| 1316 | repo | scripts/run_embedding_dual_smoke.py | 13599 | `9253225de974` | source/tool | source/tool/run_embedding_dual_smoke.py | L |
| 1317 | repo | scripts/run_v3x_6way_stage3_recovery.py | 15872 | `e4f96f2e9e4f` | source/tool | source/tool/run_v3x_6way_stage3_recovery.py | L |
| 1318 | repo | scripts/run_v3x_6way_verification.py | 25060 | `27a046d569d1` | source/tool | source/tool/run_v3x_6way_verification.py | L |
| 1319 | repo | scripts/run_v3x_finalize.py | 5932 | `46787531bf8e` | source/tool | source/tool/run_v3x_finalize.py | L |
| 1320 | repo | scripts/run_v3x_stage3_minimal.py | 12477 | `8b5d42772d5e` | source/tool | source/tool/run_v3x_stage3_minimal.py | L |
| 1321 | repo | scripts/run_v41_flash_5cells_fix.py | 17914 | `e4546d734a53` | source/tool | source/tool/run_v41_flash_5cells_fix.py | L |
| 1322 | repo | scripts/run_volcengine_seed_code_30cells.py | 13924 | `75002485aa94` | source/tool | source/tool/run_volcengine_seed_code_30cells.py | L |
| 1323 | repo | svg_mindmap_ingest.py | 8811 | `fa661fd759ed` | source/tool | source/tool/svg_mindmap_ingest.py | L |
| 1324 | repo | tests/test_agents_merge.py | 26615 | `c7cc85ffb3f0` | source/tool | source/tool/test_agents_merge.py | L |
| 1325 | repo | tests/test_diffusion.py | 12463 | `2452be26af7e` | source/tool | source/tool/test_diffusion.py | L |
| 1326 | repo | tests/test_fast.py | 3653 | `5829f89c2352` | source/tool | source/tool/test_fast.py | L |
| 1327 | repo | tests/test_fingerprint_v0.py | 13788 | `506ba4a55704` | source/tool | source/tool/test_fingerprint_v0.py | L |
| 1328 | repo | tests/test_gt_common.py | 3697 | `6a2f32d1316a` | source/tool | source/tool/test_gt_common.py | L |
| 1329 | repo | tests/test_llm_fetch.py | 11095 | `90772f5cf41b` | source/tool | source/tool/test_llm_fetch.py | L |
| 1330 | repo | tests/test_llm_prior.py | 7701 | `11c2ffa37610` | source/tool | source/tool/test_llm_prior.py | L |
| 1331 | repo | tests/test_new_modes.py | 21275 | `0b2276028391` | source/tool | source/tool/test_new_modes.py | L |
| 1332 | repo | tests/test_protocol.py | 6979 | `f103c9d87c61` | source/tool | source/tool/test_protocol.py | L |
| 1333 | repo | tests/test_v18.py | 17093 | `c523ae4b0989` | source/tool | source/tool/test_v18.py | L |
| 1334 | repo | tests/test_v19.py | 6056 | `b44e2945fa31` | source/tool | source/tool/test_v19.py | L |
| 1335 | repo | tests/test_v19_benchmark.py | 7371 | `f343754f380c` | source/tool | source/tool/test_v19_benchmark.py | L |
| 1336 | repo | tests/test_v20.py | 13249 | `e4712875f65d` | source/tool | source/tool/test_v20.py | L |
| 1337 | repo | tests/test_v20_gt2b.py | 4318 | `4cd18ae1d3dc` | source/tool | source/tool/test_v20_gt2b.py | L |
| 1338 | repo | tests/test_v20_gt5.py | 5746 | `1f104b13a170` | source/tool | source/tool/test_v20_gt5.py | L |
| 1339 | repo | tests/test_v20_gt5b.py | 2423 | `81feb1f137b4` | source/tool | source/tool/test_v20_gt5b.py | L |
| 1340 | repo | tests/test_v20_gt6.py | 2584 | `5c7dd774a3f3` | source/tool | source/tool/test_v20_gt6.py | L |
| 1341 | repo | tests/test_v20_gt7.py | 6489 | `e8727f8f42da` | source/tool | source/tool/test_v20_gt7.py | L |
| 1342 | repo | tests/test_v20_gt8.py | 5122 | `b9479374de4d` | source/tool | source/tool/test_v20_gt8.py | L |
| 1343 | repo | tests/test_v20_gt8b.py | 10109 | `3c4395df9311` | source/tool | source/tool/test_v20_gt8b.py | L |
| 1344 | repo | tests/test_v20_gt8c.py | 13458 | `562dd8b920bc` | source/tool | source/tool/test_v20_gt8c.py | L |
| 1345 | repo | tests/test_v21_gtformal.py | 7376 | `74650b1d603b` | source/tool | source/tool/test_v21_gtformal.py | L |
| 1346 | repo | tests/test_v22_p1c.py | 3854 | `b19bdb965cc0` | source/tool | source/tool/test_v22_p1c.py | L |
| 1347 | repo | tools/_archive_purge_2026_10_17/inventory_compare.json | 98697 | `1b9eee6810b4` | readout/final | readout/final/inventory_compare.json | L |
| 1348 | repo | tools/_archive_purge_2026_10_17/inventory_compare.py | 4365 | `7c09c04d53cf` | source/tool | source/tool/inventory_compare.py | L |
| 1349 | repo | tools/_archive_purge_2026_10_17/recycle_channel.py | 3540 | `06619281cd09` | source/tool | source/tool/recycle_channel.py | L |
| 1350 | repo | tools/_archive_purge_2026_10_17/step2_recheck.py | 2656 | `a2e324411df7` | source/tool | source/tool/step2_recheck.py | L |
| 1351 | repo | tools/_archive_purge_2026_10_17/step2_sample.py | 4613 | `54daf47662a2` | source/tool | source/tool/step2_sample.py | L |
| 1352 | repo | tools/_archive_purge_2026_10_17/step2_sample_verify.json | 2028 | `46e72777f74e` | readout/final | readout/final/step2_sample_verify.json | L |
| 1353 | repo | tools/_archive_purge_2026_10_17/step2_sample_verify_rejudge.json | 397 | `d32809934409` | readout/final | readout/final/step2_sample_verify_rejudge.json | L |
| 1354 | repo | tools/_archive_purge_2026_10_17/step3_bulk_purge.py | 7780 | `90523fef8e09` | source/tool | source/tool/step3_bulk_purge.py | L |
| 1355 | repo | tools/_archive_purge_2026_10_17/step3_bulk_result.json | 374277 | `3601cc490af7` | readout/final | readout/final/step3_bulk_result.json | L |
| 1356 | repo | tools/_archive_purge_2026_10_17/step4_bin_audit.json | 8102 | `89da5036d061` | readout/final | readout/final/step4_bin_audit.json | L |
| 1357 | repo | tools/_archive_purge_2026_10_17/step4_bin_audit.py | 2442 | `e8e5333144ec` | source/tool | source/tool/step4_bin_audit.py | L |
| 1358 | repo | tools/_archive_purge_2026_10_17/step5_register.py | 17778 | `cbb6539394a8` | source/tool | source/tool/step5_register.py | L |
| 1359 | repo | tools/_archive_purge_2026_10_17/step5_register_result.json | 210 | `c6788de2a588` | readout/final | readout/final/step5_register_result.json | L |
| 1360 | repo | tools/distortion_calculator.py | 50896 | `ae7ff6e0bac5` | source/tool | source/tool/distortion_calculator.py | L |
| 1361 | repo | tools/exp_harness.py | 45590 | `ce64b9b97489` | source/tool | source/tool/exp_harness.py | L |
| 1362 | repo | tools/llm_client.py | 8118 | `1722500da4aa` | source/tool | source/tool/llm_client.py | L |
| 1363 | repo | tools/make_figures_v2.py | 21073 | `0dc3ea09f42d` | source/tool | source/tool/make_figures_v2.py | L |
| 1364 | repo | tools/make_figures_v2_en.py | 21188 | `b4e880a6af33` | source/tool | source/tool/make_figures_v2_en.py | L |
| 1365 | repo | tools/read_key.py | 1047 | `a9b56c4e775f` | source/tool | source/tool/read_key.py | L |
| 1366 | repo | verifier/_build_partial.py | 7160 | `04fcd95c70f1` | source/tool | source/tool/_build_partial.py | L |
| 1367 | repo | verifier/_read_summary.py | 1231 | `b4d89f052875` | source/tool | source/tool/_read_summary.py | L |
| 1368 | repo | verifier/_test_one.py | 2564 | `893641fd9e25` | source/tool | source/tool/_test_one.py | L |
| 1369 | repo | verifier/audit/conservation.py | 22105 | `4bdec2683f06` | source/tool | source/tool/conservation.py | L |
| 1370 | repo | verifier/handoff/KT_ABC1_anchors_sha256_12.json | 6680 | `03c6c01f3697` | readout/final | readout/final/KT_ABC1_anchors_sha256_12.json | L |
| 1371 | repo | verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json | 12498 | `312d635e6259` | readout/final | readout/final/P_F_PREDECISION_2026_09_11_V0.1.json | L |
| 1372 | repo | verifier/kill_lines/kt_b1_kill_decision.py | 2781 | `9f351078e5bf` | source/tool | source/tool/kt_b1_kill_decision.py | L |
| 1373 | repo | verifier/run_volcengine_9model_30cells.py | 12050 | `54f8033cfb29` | source/tool | source/tool/run_volcengine_9model_30cells.py | L |
| 1374 | repo | verifier/runs/2026-09-04_pd_v0.jsonl | 100 | `5042869bdf85` | readout/final | readout/final/2026-09-04_pd_v0.jsonl | L |
| 1375 | repo | verifier/runs/v15_run1.md | 475 | `634ef5fa4ef8` | verdict/pi | verdict/pi/v15_run1.md | L |
| 1376 | repo | verifier/runs/v21_run2.md | 448 | `3246c7d46480` | verdict/pi | verdict/pi/v21_run2.md | L |
| 1377 | repo | verifier/runs/v22_run1.md | 436 | `582531ccd67d` | doc/readme | doc/readme/v22_run1.md | L |
| 1378 | repo | verifier/runs/v23_run1.md | 586 | `9578066064cc` | doc/readme | doc/readme/v23_run1.md | L |
| 1379 | repo | verifier/runs/v24_run1.md | 498 | `67fd4fec19f2` | verdict/judge | verdict/judge/v24_run1.md | L |
| 1380 | repo | verifier/runs/v25_run1.md | 526 | `b81e2fb0ea28` | verdict/judge | verdict/judge/v25_run1.md | L |
| 1381 | repo | verifier/runs/v26_run1.md | 546 | `09b69c05bb47` | verdict/kd | verdict/kd/v26_run1.md | L |
| 1382 | repo | verifier/runs/v27_run1.md | 559 | `0759457758be` | verdict/judge | verdict/judge/v27_run1.md | L |
| 1383 | repo | verifier/runs/v27_run2.md | 554 | `82a92d9ce191` | verdict/judge | verdict/judge/v27_run2.md | L |
| 1384 | repo | verifier/runs/v29_run1.md | 440 | `26a667edec7a` | verdict/judge | verdict/judge/v29_run1.md | L |
| 1385 | repo | verifier/runs/v29_run2.md | 627 | `badd1ed95a6d` | verdict/judge | verdict/judge/v29_run2.md | L |
| 1386 | repo | verifier/runs/v30_run1.md | 735 | `cef68a7a30a5` | doc/paper | doc/paper/v30_run1.md | L |
| 1387 | repo | verifier/runs/v30_run2.md | 787 | `d22151b9ad6d` | doc/paper | doc/paper/v30_run2.md | L |
| 1388 | repo | verifier/runs/v30_run3.md | 771 | `0dc553ed64c2` | doc/paper | doc/paper/v30_run3.md | L |
| 1389 | repo | verifier/runs/v35_run2.md | 118 | `11ce6990b84a` | verdict/judge | verdict/judge/v35_run2.md | L |
| 1390 | repo | verifier/runs/v42_2026-08-30_run1.txt | 279 | `8fde2819ef29` | readout/final | readout/final/v42_2026-08-30_run1.txt | L |
| 1391 | repo | verifier/runs/v42_2026-08-30_run2.txt | 156 | `1aa0257caac9` | readout/final | readout/final/v42_2026-08-30_run2.txt | L |
| 1392 | repo | verifier/runs/v43_2026-09-01_run1.txt | 199 | `aa82005b05de` | readout/final | readout/final/v43_2026-09-01_run1.txt | L |
| 1393 | repo | verifier/v1/check.py | 2976 | `03bc1adfc82f` | source/tool | source/tool/check__03bc1adfc82f.py | L |
| 1394 | repo | verifier/v10/check.py | 5261 | `4fd5fdd754c0` | source/tool | source/tool/check__4fd5fdd754c0.py | L |
| 1395 | repo | verifier/v11/check.py | 2767 | `3b8682a7e562` | source/tool | source/tool/check__3b8682a7e562.py | L |
| 1396 | repo | verifier/v12/check.py | 4142 | `87c9c883e3bf` | source/tool | source/tool/check__87c9c883e3bf.py | L |
| 1397 | repo | verifier/v13/check.py | 3495 | `1159facab6db` | source/tool | source/tool/check__1159facab6db.py | L |
| 1398 | repo | verifier/v14/check.py | 3278 | `4ba223d2185d` | source/tool | source/tool/check__4ba223d2185d.py | L |
| 1399 | repo | verifier/v15/check.py | 3231 | `be0f2bbab0a2` | source/tool | source/tool/check__be0f2bbab0a2.py | L |
| 1400 | repo | verifier/v16/check.py | 2691 | `223082632a1d` | source/tool | source/tool/check__223082632a1d.py | L |
| 1401 | repo | verifier/v17/check.py | 2897 | `679792be51ed` | source/tool | source/tool/check__679792be51ed.py | L |
| 1402 | repo | verifier/v18/check.py | 3180 | `6abdda4f7400` | source/tool | source/tool/check__6abdda4f7400.py | L |
| 1403 | repo | verifier/v19/check.py | 1995 | `c53cf72d085b` | source/tool | source/tool/check__c53cf72d085b.py | L |
| 1404 | repo | verifier/v2/check.py | 2510 | `af3a78983537` | source/tool | source/tool/check__af3a78983537.py | L |
| 1405 | repo | verifier/v20/check.py | 2790 | `9d0f1e950dee` | source/tool | source/tool/check__9d0f1e950dee.py | L |
| 1406 | repo | verifier/v20/erratum.md | 316 | `35081d39f35b` | doc/readme | doc/readme/erratum.md | L |
| 1407 | repo | verifier/v21/check.py | 3702 | `5e7d7435c4a3` | source/tool | source/tool/check__5e7d7435c4a3.py | L |
| 1408 | repo | verifier/v22/check.py | 2857 | `f16beaae5675` | source/tool | source/tool/check__f16beaae5675.py | L |
| 1409 | repo | verifier/v23/check.py | 2659 | `9ecb25362c9a` | source/tool | source/tool/check__9ecb25362c9a.py | L |
| 1410 | repo | verifier/v24/check.py | 3124 | `e6c7513d54f3` | source/tool | source/tool/check__e6c7513d54f3.py | L |
| 1411 | repo | verifier/v25/check.py | 2576 | `cc6ff5453e06` | source/tool | source/tool/check__cc6ff5453e06.py | L |
| 1412 | repo | verifier/v26/check.py | 2595 | `c58a9652a42a` | source/tool | source/tool/check__c58a9652a42a.py | L |
| 1413 | repo | verifier/v27/check.py | 2132 | `118524c7e808` | source/tool | source/tool/check__118524c7e808.py | L |
| 1414 | repo | verifier/v28/check.py | 2201 | `b73a6b268f64` | source/tool | source/tool/check__b73a6b268f64.py | L |
| 1415 | repo | verifier/v29/check.py | 2124 | `5923e2c379f6` | source/tool | source/tool/check__5923e2c379f6.py | L |
| 1416 | repo | verifier/v3/check.py | 2544 | `02a5a86d38bf` | source/tool | source/tool/check__02a5a86d38bf.py | L |
| 1417 | repo | verifier/v30/check.py | 2565 | `2cf46f79a669` | source/tool | source/tool/check__2cf46f79a669.py | L |
| 1418 | repo | verifier/v31/check.py | 2185 | `e5bb0020e500` | source/tool | source/tool/check__e5bb0020e500.py | L |
| 1419 | repo | verifier/v32/check.py | 2551 | `399bfc743f24` | source/tool | source/tool/check__399bfc743f24.py | L |
| 1420 | repo | verifier/v33/check.py | 6019 | `32fefc485326` | source/tool | source/tool/check__32fefc485326.py | L |
| 1421 | repo | verifier/v34/check.py | 3715 | `0bbd226cd2ae` | source/tool | source/tool/check__0bbd226cd2ae.py | L |
| 1422 | repo | verifier/v35/check.py | 2385 | `2130a5f5e1bf` | source/tool | source/tool/check__2130a5f5e1bf.py | L |
| 1423 | repo | verifier/v36/check.sh | 968 | `2212dcd98cd1` | source/tool | source/tool/check.sh | L |
| 1424 | repo | verifier/v37/check.sh | 1141 | `ced43b5f8800` | source/tool | source/tool/check__ced43b5f8800.sh | L |
| 1425 | repo | verifier/v38/check.sh | 1705 | `43b501c5c20d` | source/tool | source/tool/check__43b501c5c20d.sh | L |
| 1426 | repo | verifier/v39/check.sh | 1935 | `d48ac555761f` | source/tool | source/tool/check__d48ac555761f.sh | L |
| 1427 | repo | verifier/v4/check.py | 3205 | `f058e85c5383` | source/tool | source/tool/check__f058e85c5383.py | L |
| 1428 | repo | verifier/v40/check.sh | 1604 | `7b15cd2f4c7e` | source/tool | source/tool/check__7b15cd2f4c7e.sh | L |
| 1429 | repo | verifier/v41/check.sh | 1687 | `2c9fe869daaa` | source/tool | source/tool/check__2c9fe869daaa.sh | L |
| 1430 | repo | verifier/v42/check.sh | 1509 | `3ea87e2cfc61` | source/tool | source/tool/check__3ea87e2cfc61.sh | L |
| 1431 | repo | verifier/v43/check.sh | 1224 | `71b83217032d` | source/tool | source/tool/check__71b83217032d.sh | L |
| 1432 | repo | verifier/v5/check.py | 2255 | `3d776381f665` | source/tool | source/tool/check__3d776381f665.py | L |
| 1433 | repo | verifier/v6/check.py | 2757 | `8366078a10e4` | source/tool | source/tool/check__8366078a10e4.py | L |
| 1434 | repo | verifier/v7/check.py | 4300 | `a70a68037d92` | source/tool | source/tool/check__a70a68037d92.py | L |
| 1435 | repo | verifier/v8/check.py | 3210 | `01b63b1a9c5f` | source/tool | source/tool/check.py | L |
| 1436 | repo | verifier/v9/check.py | 5352 | `5faad917d839` | source/tool | source/tool/check__5faad917d839.py | L |
| 1437 | sub | .trae/audit/compare_versions.py | 7958 | `03e22a91bc0c` | source/tool | source/tool/compare_versions.py | L |
| 1438 | sub | .trae/audit/compile_evidence/compile_runner.ps1 | 2022 | `1fc5f3ab3f93` | source/tool | source/tool/compile_runner.ps1 | L |
| 1439 | sub | .trae/audit/compile_evidence/extract_tars.py | 1141 | `befdd577adce` | source/tool | source/tool/extract_tars.py | L |
| 1440 | sub | .trae/audit/compile_evidence/v1_62refs_20260908/compile_runner.ps1 | 1469 | `51d29cb72b68` | source/tool | source/tool/compile_runner__51d29cb72b68.ps1 | L |
| 1441 | sub | .trae/audit/compile_evidence/v2_overfull_fix_20260909/COMPILE_SUMMARY.txt | 1887 | `fe6f9872a2fe` | doc/paper | doc/paper/COMPILE_SUMMARY.txt | L |
| 1442 | sub | .trae/audit/identify_dedicated.py | 3806 | `3feb84107c02` | source/tool | source/tool/identify_dedicated.py | L |
| 1443 | sub | .trae/audit/inspect_current_tars.py | 2501 | `291877043221` | source/tool | source/tool/inspect_current_tars.py | L |
| 1444 | sub | .trae/audit/rebuild_trae_home.py | 8554 | `7bd38b8e70d4` | source/tool | source/tool/rebuild_trae_home.py | L |
| 1445 | sub | .trae/deliverables/MANIFEST.sha256.txt | 1282 | `3ab185e6c047` | doc/paper | doc/paper/MANIFEST.sha256.txt | L |
| 1446 | sub | .trae/scripts/_md_to_tex.py | 48627 | `f55da6fe7aea` | source/tool | source/tool/_md_to_tex.py | L |
| 1447 | sub | .trae/scripts/_split_packages.py | 7755 | `872530d93a7f` | source/tool | source/tool/_split_packages.py | L |
| 1448 | sub | Deposon_凝子_统一场论报告_一致性核对_20260907.md | 3441 | `125998731621` | doc/letter | doc/letter/Deposon_凝子_统一场论报告_一致性核对_20260907.md | L |
| 1449 | sub | _check_conv_archive.ps1 | 2326 | `c89d46c47026` | source/tool | source/tool/_check_conv_archive.ps1 | L |
| 1450 | sub | _list_teamo_models.py | 1273 | `c51f3d2005fe` | source/tool | source/tool/_list_teamo_models.py | L |
| 1451 | sub | _merge_or_stub_overlap_table_v3_2026_09_17.py | 5050 | `300daa32f7be` | source/tool | source/tool/_merge_or_stub_overlap_table_v3_2026_09_17.py | L |
| 1452 | sub | _movedin_2026_10_22/results___.tmp____audit_bom_cr_2026_10_19.py | 880 | `107a9ed5090a` | source/tool | source/tool/results___.tmp____audit_bom_cr_2026_10_19.py | L |
| 1453 | sub | _movedin_2026_10_22/results___.tmp____audit_final_2026_10_19.py | 2739 | `ffc34fee17b2` | source/tool | source/tool/results___.tmp____audit_final_2026_10_19.py | L |
| 1454 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_append_2026_10_19.py | 3116 | `e3aca88d382f` | source/tool | source/tool/results___.tmp____audit_s12_append_2026_10_19.py | L |
| 1455 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_heads_2026_10_19.py | 2814 | `faa86d3f25bc` | source/tool | source/tool/results___.tmp____audit_s12_heads_2026_10_19.py | L |
| 1456 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_heads_out_2026_10_19.txt | 83701 | `c285e696fce1` | verdict/kd | verdict/kd/results___.tmp____audit_s12_heads_out_2026_10_19.txt | L |
| 1457 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_keyclass_2026_10_19.py | 3057 | `b4f7569705a8` | source/tool | source/tool/results___.tmp____audit_s12_keyclass_2026_10_19.py | L |
| 1458 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_keyclass_2026_10_19.txt | 1385 | `21d7e6e9fdbc` | doc/readme | doc/readme/results___.tmp____audit_s12_keyclass_2026_10_19.txt | L |
| 1459 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_keyscan_2026_10_19.py | 8367 | `6a2dc54827b7` | source/tool | source/tool/results___.tmp____audit_s12_keyscan_2026_10_19.py | L |
| 1460 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_keyscan_out_2026_10_19.txt | 6950 | `aa7fa6ff4255` | readout/final | readout/final/results___.tmp____audit_s12_keyscan_out_2026_10_19.txt | L |
| 1461 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_refined_2026_10_19.py | 12829 | `c53201f4bae4` | source/tool | source/tool/results___.tmp____audit_s12_refined_2026_10_19.py | L |
| 1462 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_refined_out_2026_10_19.txt | 8779 | `16ee96876c4a` | readout/final | readout/final/results___.tmp____audit_s12_refined_out_2026_10_19.txt | L |
| 1463 | sub | _movedin_2026_10_22/results___.tmp____audit_s12_scan_2026_10_19.py | 2767 | `e19a994d3f9b` | source/tool | source/tool/results___.tmp____audit_s12_scan_2026_10_19.py | L |
| 1464 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_7_append_2026_10_20.py | 2395 | `953abd8121f7` | source/tool | source/tool/results___.tmp____audit_s13_7_append_2026_10_20.py | L |
| 1465 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_anchors_2026_10_20.py | 12723 | `eeb9f79522b0` | source/tool | source/tool/results___.tmp____audit_s13_anchors_2026_10_20.py | L |
| 1466 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_anchors_out_2026_10_20.txt | 13754 | `9063b4326cec` | verdict/pi | verdict/pi/results___.tmp____audit_s13_anchors_out_2026_10_20.txt | L |
| 1467 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_append_2026_10_20.py | 3520 | `b4a1c8d6a3d9` | source/tool | source/tool/results___.tmp____audit_s13_append_2026_10_20.py | L |
| 1468 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_conv_out_2026_10_20.txt | 419151 | `2e523f11e8c2` | readout/final | readout/final/results___.tmp____audit_s13_conv_out_2026_10_20.txt | L |
| 1469 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_final_2026_10_20.py | 8898 | `036b4a749f95` | source/tool | source/tool/results___.tmp____audit_s13_final_2026_10_20.py | L |
| 1470 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_final_out_2026_10_20.txt | 19178 | `f3b199fa0deb` | readout/final | readout/final/results___.tmp____audit_s13_final_out_2026_10_20.txt | L |
| 1471 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_main_heads_2026_10_20.py | 611 | `67bcc0955f22` | source/tool | source/tool/results___.tmp____audit_s13_main_heads_2026_10_20.py | L |
| 1472 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_main_heads_2026_10_20.txt | 1792 | `dc3a10abbc2b` | readout/final | readout/final/results___.tmp____audit_s13_main_heads_2026_10_20.txt | L |
| 1473 | sub | _movedin_2026_10_22/results___.tmp____audit_s13_scan_2026_10_20.py | 4924 | `8c8b9d995f05` | source/tool | source/tool/results___.tmp____audit_s13_scan_2026_10_20.py | L |
| 1474 | sub | _movedin_2026_10_22/results___.tmp____audit_tail_2026_10_19.py | 704 | `893914b4ef10` | source/tool | source/tool/results___.tmp____audit_tail_2026_10_19.py | L |
| 1475 | sub | _movedin_2026_10_22/results___.tmp____s12_7_body_2026_10_19.md | 4754 | `e80e4fe4aa0f` | verdict/pi | verdict/pi/results___.tmp____s12_7_body_2026_10_19.md | L |
| 1476 | sub | _movedin_2026_10_22/results___.tmp____s12_body_2026_10_19.md | 40199 | `ebea307102a1` | readout/final | readout/final/results___.tmp____s12_body_2026_10_19.md | L |
| 1477 | sub | _movedin_2026_10_22/results___.tmp____s13_7_body_2026_10_20.md | 4975 | `5a74e4bdea89` | verdict/pi | verdict/pi/results___.tmp____s13_7_body_2026_10_20.md | L |
| 1478 | sub | _movedin_2026_10_22/results___.tmp____s13_body_2026_10_20.md | 51542 | `758ad1bac2e6` | readout/final | readout/final/results___.tmp____s13_body_2026_10_20.md | L |
| 1479 | sub | _movedin_2026_10_22/results___.tmp____s14_anchor2_2026_10_21.py | 7115 | `6c9463882c9f` | source/tool | source/tool/results___.tmp____s14_anchor2_2026_10_21.py | L |
| 1480 | sub | _movedin_2026_10_22/results___.tmp____s14_anchorchain2_2026_10_21.md | 26640 | `cd3435aecb60` | readout/final | readout/final/results___.tmp____s14_anchorchain2_2026_10_21.md | L |
| 1481 | sub | _movedin_2026_10_22/results___.tmp____s14_anchorchain_2026_10_21.md | 480977 | `dd49e6612dbe` | verdict/pi | verdict/pi/results___.tmp____s14_anchorchain_2026_10_21.md | L |
| 1482 | sub | _movedin_2026_10_22/results___.tmp____s14_anchorchain_2026_10_21.py | 4247 | `d80719c6d092` | source/tool | source/tool/results___.tmp____s14_anchorchain_2026_10_21.py | L |
| 1483 | sub | _movedin_2026_10_22/results___.tmp____s14_append_2026_10_21.py | 8769 | `4402eb22f4ad` | source/tool | source/tool/results___.tmp____s14_append_2026_10_21.py | L |
| 1484 | sub | _movedin_2026_10_22/results___.tmp____s14_append_report_2026_10_21.md | 1505 | `67d8df4dcc34` | verdict/judge | verdict/judge/results___.tmp____s14_append_report_2026_10_21.md | L |
| 1485 | sub | _movedin_2026_10_22/results___.tmp____s14_body_2026_10_21.md | 38541 | `4893e543556f` | readout/final | readout/final/results___.tmp____s14_body_2026_10_21.md | L |
| 1486 | sub | _movedin_2026_10_22/results___.tmp____s14_cards_full_2026_10_21.md | 153751 | `71e52e6aa470` | verdict/pi | verdict/pi/results___.tmp____s14_cards_full_2026_10_21.md | L |
| 1487 | sub | _movedin_2026_10_22/results___.tmp____s14_cards_full_2026_10_21.py | 1587 | `0f95bd681cf6` | source/tool | source/tool/results___.tmp____s14_cards_full_2026_10_21.py | L |
| 1488 | sub | _movedin_2026_10_22/results___.tmp____s14_disk_scan_2026_10_21.py | 2982 | `854019e4b7d3` | source/tool | source/tool/results___.tmp____s14_disk_scan_2026_10_21.py | L |
| 1489 | sub | _movedin_2026_10_22/results___.tmp____s14_disk_scan_out_t1.md | 4313 | `de8d0b8a76b0` | readout/final | readout/final/results___.tmp____s14_disk_scan_out_t1.md | L |
| 1490 | sub | _movedin_2026_10_22/results___.tmp____s14_disk_scan_out_t2.md | 42088 | `8f184f097720` | readout/final | readout/final/results___.tmp____s14_disk_scan_out_t2.md | L |
| 1491 | sub | _movedin_2026_10_22/results___.tmp____s14_events2_2026_10_21.py | 2668 | `0c75fb83c89d` | source/tool | source/tool/results___.tmp____s14_events2_2026_10_21.py | L |
| 1492 | sub | _movedin_2026_10_22/results___.tmp____s14_final_measure_2026_10_21.md | 25045 | `5c4f0d43ada4` | verdict/pi | verdict/pi/results___.tmp____s14_final_measure_2026_10_21.md | L |
| 1493 | sub | _movedin_2026_10_22/results___.tmp____s14_final_measure_2026_10_21.py | 5872 | `e0dc2e74ff62` | source/tool | source/tool/results___.tmp____s14_final_measure_2026_10_21.py | L |
| 1494 | sub | _movedin_2026_10_22/results___.tmp____s14_instrument_2026_10_21.py | 4550 | `6eb1a23daf22` | source/tool | source/tool/results___.tmp____s14_instrument_2026_10_21.py | L |
| 1495 | sub | _movedin_2026_10_22/results___.tmp____s14_instrument_out_2026_10_21.md | 40930 | `53fadc8fc515` | readout/final | readout/final/results___.tmp____s14_instrument_out_2026_10_21.md | L |
| 1496 | sub | _movedin_2026_10_22/results___.tmp____s14_main_events2_2026_10_21.md | 177579 | `2faed7996933` | readout/final | readout/final/results___.tmp____s14_main_events2_2026_10_21.md | L |
| 1497 | sub | _movedin_2026_10_22/results___.tmp____s14_main_events_2026_10_21.md | 289 | `1e5b4e17e616` | readout/final | readout/final/results___.tmp____s14_main_events_2026_10_21.md | L |
| 1498 | sub | _movedin_2026_10_22/results___.tmp____s14_main_session_slice_2026_10_21.md | 96411 | `4b10cb45fd44` | readout/final | readout/final/results___.tmp____s14_main_session_slice_2026_10_21.md | L |
| 1499 | sub | _movedin_2026_10_22/results___.tmp____s14_msgdist_2026_10_21.md | 675 | `6b0da8b7ce9b` | readout/final | readout/final/results___.tmp____s14_msgdist_2026_10_21.md | L |
| 1500 | sub | _movedin_2026_10_22/results___.tmp____s14_msgdist_2026_10_21.py | 2958 | `31bcc0f213c0` | source/tool | source/tool/results___.tmp____s14_msgdist_2026_10_21.py | L |
| 1501 | sub | _movedin_2026_10_22/results___.tmp____s14_session_scan2_2026_10_21.py | 4080 | `e93a45e23469` | source/tool | source/tool/results___.tmp____s14_session_scan2_2026_10_21.py | L |
| 1502 | sub | _movedin_2026_10_22/results___.tmp____s14_session_scan_2026_10_21.py | 3618 | `a4cc5099940c` | source/tool | source/tool/results___.tmp____s14_session_scan_2026_10_21.py | L |
| 1503 | sub | _movedin_2026_10_22/results___.tmp____s14_session_scan_out_2026_10_21.md | 1137664 | `5741ac6af12a` | readout/final | readout/final/results___.tmp____s14_session_scan_out_2026_10_21.md | L |
| 1504 | sub | _movedin_2026_10_22/results___.tmp____s15_append_2026_10_21.md | 2459 | `8161b1da2340` | doc/readme | doc/readme/results___.tmp____s15_append_2026_10_21.md | L |
| 1505 | sub | _movedin_2026_10_22/results___.tmp____s15_body_2026_10_21.md | 55575 | `258115c22f32` | verdict/pi | verdict/pi/results___.tmp____s15_body_2026_10_21.md | L |
| 1506 | sub | _movedin_2026_10_22/results___.tmp____s16_append_2026_10_21.md | 9441 | `b925b0c48d58` | doc/readme | doc/readme/results___.tmp____s16_append_2026_10_21.md | L |
| 1507 | sub | _movedin_2026_10_22/results___.tmp____s16_body_2026_10_21.md | 77994 | `11af4e96c034` | verdict/pi | verdict/pi/results___.tmp____s16_body_2026_10_21.md | L |
| 1508 | sub | _movedout_manifest_2026_09_28.json | 2003 | `6b557f005a40` | readout/final | readout/final/_movedout_manifest_2026_09_28.json | L |
| 1509 | sub | _p_l_v3_phase1_finalize_2026_09_17.py | 19226 | `cf8fd1178ab1` | source/tool | source/tool/_p_l_v3_phase1_finalize_2026_09_17.py | L |
| 1510 | sub | _p_l_v3_phase1_runner_2026_09_17.py | 35425 | `d5e74a98c44b` | source/tool | source/tool/_p_l_v3_phase1_runner_2026_09_17.py | L |
| 1511 | sub | _p_l_v3_phase2_closedsource_finalize_2026_09_17.py | 14700 | `20f038a7a8dd` | source/tool | source/tool/_p_l_v3_phase2_closedsource_finalize_2026_09_17.py | L |
| 1512 | sub | _p_l_v3_phase2_closedsource_runner_2026_09_17.py | 28344 | `e6005733ca7c` | source/tool | source/tool/_p_l_v3_phase2_closedsource_runner_2026_09_17.py | L |
| 1513 | sub | _p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py | 26716 | `090d34377c9d` | source/tool | source/tool/_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py | L |
| 1514 | sub | _p_l_v3_phase2_finalize_2026_09_17.py | 19901 | `eaa04c5713d6` | source/tool | source/tool/_p_l_v3_phase2_finalize_2026_09_17.py | L |
| 1515 | sub | _p_l_v3_phase2_glm53_only_2026_09_17.py | 12604 | `c88608c7a26b` | source/tool | source/tool/_p_l_v3_phase2_glm53_only_2026_09_17.py | L |
| 1516 | sub | _p_l_v3_phase2_or_embedding_2026_09_17.py | 26300 | `e7353ffbb94f` | source/tool | source/tool/_p_l_v3_phase2_or_embedding_2026_09_17.py | L |
| 1517 | sub | _p_l_v3_phase2_or_embedding_v3_2026_09_17.py | 27863 | `5edc460b35d3` | source/tool | source/tool/_p_l_v3_phase2_or_embedding_v3_2026_09_17.py | L |
| 1518 | sub | _p_l_v3_phase2_runner_2026_09_17.py | 21868 | `ac780b206cae` | source/tool | source/tool/_p_l_v3_phase2_runner_2026_09_17.py | L |
| 1519 | sub | _p_l_v3_phase2_vector_emb_2026_09_17.py | 3810 | `f5e51b83541a` | source/tool | source/tool/_p_l_v3_phase2_vector_emb_2026_09_17.py | L |
| 1520 | sub | _p_l_v3_phase2_vector_emb_doubao_2026_09_17.py | 37263 | `b0a59c92a3e6` | source/tool | source/tool/_p_l_v3_phase2_vector_emb_doubao_2026_09_17.py | L |
| 1521 | sub | _print_sha_2026_09_17.py | 1227 | `51d33faa22b9` | source/tool | source/tool/_print_sha_2026_09_17.py | L |
| 1522 | sub | _show_teamo_ownedby.py | 1342 | `3c8175c35d82` | source/tool | source/tool/_show_teamo_ownedby.py | L |
| 1523 | sub | _test_3bb_vary.py | 3541 | `a7046b2dd65e` | source/tool | source/tool/_test_3bb_vary.py | L |
| 1524 | sub | _test_gpt56sol_real.py | 2060 | `19a48c278183` | source/tool | source/tool/_test_gpt56sol_real.py | L |
| 1525 | sub | _tmp_degen.py | 719 | `88004f338e9c` | source/tool | source/tool/_tmp_degen.py | L |
| 1526 | sub | _tmp_v1_recompute.py | 9819 | `86a6407a7bd6` | source/tool | source/tool/_tmp_v1_recompute.py | L |
| 1527 | sub | _tmp_v2_redesign.py | 13762 | `4cd07b3a7dea` | source/tool | source/tool/_tmp_v2_redesign.py | L |
| 1528 | sub | _tmp_verify.py | 384 | `e93a9cb16b08` | source/tool | source/tool/_tmp_verify.py | L |
| 1529 | sub | _v4_l6_s38v2_verify_2026_09_24.py | 3729 | `c665860f459a` | source/tool | source/tool/_v4_l6_s38v2_verify_2026_09_24.py | L |
| 1530 | sub | deposon_team/_designs/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md | 12667 | `3fbc7f4dfd22` | doc/letter | doc/letter/D7_PRE_DISPATCH_EXECUTION_REPORT_2026_09_16.md | L |
| 1531 | sub | deposon_team/_designs/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md | 12844 | `23bb7d39bf58` | doc/letter | doc/letter/DELEGATION_CONFIGS_FOR_USER_B_2026_09_16.md | L |
| 1532 | sub | deposon_team/_designs/EXTERNAL_AGENT_PROMPTS_2026_09_16.md | 12326 | `6a7b0c20a133` | doc/letter | doc/letter/EXTERNAL_AGENT_PROMPTS_2026_09_16.md | L |
| 1533 | sub | deposon_team/_designs/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md | 8714 | `2185433b1f32` | doc/letter | doc/letter/V3X_CLOSURE_REPORT_REQUIREMENTS_FOR_EXTERNAL_AGENT.md | L |
| 1534 | sub | deposon_team/_designs/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md | 12878 | `95925a562597` | doc/letter | doc/letter/V3X_FULL_CLOSEOUT_REPORT_2026_09_16.md | L |
| 1535 | sub | deposon_team/_designs/V3X_GAME_THEORY_NON_EUCLIDEAN_MASTER_NARRATIVE_2026_09_16.py | 9244 | `7f6563d22ce7` | source/tool | source/tool/V3X_GAME_THEORY_NON_EUCLIDEAN_MASTER_NARRATIVE_2026_09_16.py | L |
| 1536 | sub | deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md | 8222 | `27db4950f710` | doc/letter | doc/letter/V3X_PATCH_5ANCHOR_RECONCILE_2026_09_16.md | L |
| 1537 | sub | deposon_team/_designs/V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md | 11232 | `11cd57800bd6` | doc/letter | doc/letter/V3X_TEAM_IMPROVEMENT_PLAN_2026_09_16.md | L |
| 1538 | sub | deposon_team/plugins/_audit_minimax_extract_2026_09_16.py | 4364 | `da1c38940b6c` | source/tool | source/tool/_audit_minimax_extract_2026_09_16.py | L |
| 1539 | sub | deposon_team/plugins/_audit_v3_runners_2026_09_16.py | 3145 | `b490f695841c` | source/tool | source/tool/_audit_v3_runners_2026_09_16.py | L |
| 1540 | sub | deposon_team/plugins/_build_minimax_artifact_2026_09_16.py | 7361 | `d0d188c60a62` | source/tool | source/tool/_build_minimax_artifact_2026_09_16.py | L |
| 1541 | sub | deposon_team/plugins/_d7_5anchor_60cells_2026_09_18.py | 10049 | `568d30cf6d92` | source/tool | source/tool/_d7_5anchor_60cells_2026_09_18.py | L |
| 1542 | sub | deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_16.py | 6241 | `821fd0b19eb3` | source/tool | source/tool/_d7_post_anchor_rotation_remediation_2026_09_16.py | L |
| 1543 | sub | deposon_team/plugins/_d7_post_anchor_rotation_remediation_2026_09_18.py | 9152 | `b0a450752a97` | source/tool | source/tool/_d7_post_anchor_rotation_remediation_2026_09_18.py | L |
| 1544 | sub | deposon_team/plugins/_fix_adendum_c_erratum_2026_09_17.py | 1820 | `eb44de412de5` | source/tool | source/tool/_fix_adendum_c_erratum_2026_09_17.py | L |
| 1545 | sub | deposon_team/plugins/_fix_minimax_extract_2026_09_16.py | 5103 | `8a722b0a4aea` | source/tool | source/tool/_fix_minimax_extract_2026_09_16.py | L |
| 1546 | sub | deposon_team/plugins/_fix_v3_selfcheck_2026_09_16.py | 7401 | `b9a414293ebe` | source/tool | source/tool/_fix_v3_selfcheck_2026_09_16.py | L |
| 1547 | sub | deposon_team/plugins/_goal_completion_audit_2026_09_17.py | 3752 | `5c18b72e7bb3` | source/tool | source/tool/_goal_completion_audit_2026_09_17.py | L |
| 1548 | sub | deposon_team/plugins/_p_i_real_labels_runner_2026_09_16.py | 7055 | `8678e5083b41` | source/tool | source/tool/_p_i_real_labels_runner_2026_09_16.py | L |
| 1549 | sub | deposon_team/plugins/_p_j_convergence_basin_runner_2026_09_16.py | 9143 | `877b9415a217` | source/tool | source/tool/_p_j_convergence_basin_runner_2026_09_16.py | L |
| 1550 | sub | deposon_team/plugins/_p_k_blind_test_runner_2026_09_16.py | 19031 | `70e34edc0926` | source/tool | source/tool/_p_k_blind_test_runner_2026_09_16.py | L |
| 1551 | sub | deposon_team/plugins/_p_l_p_c_finite_size_scaling_runner_2026_09_16.py | 9177 | `bca06b3cc2f7` | source/tool | source/tool/_p_l_p_c_finite_size_scaling_runner_2026_09_16.py | L |
| 1552 | sub | deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16.py | 5663 | `daff134b8e0b` | source/tool | source/tool/_p_l_real_data_collapse_runner_2026_09_16.py | L |
| 1553 | sub | deposon_team/plugins/_p_l_real_data_collapse_runner_2026_09_16_v2.py | 5778 | `ed9d066f3ea3` | source/tool | source/tool/_p_l_real_data_collapse_runner_2026_09_16_v2.py | L |
| 1554 | sub | deposon_team/plugins/_p_m_attack_surface_cost_runner_2026_09_16.py | 10622 | `9e054e93982b` | source/tool | source/tool/_p_m_attack_surface_cost_runner_2026_09_16.py | L |
| 1555 | sub | deposon_team/plugins/_p_m_real_separation_runner_2026_09_16.py | 7316 | `d5133ecca740` | source/tool | source/tool/_p_m_real_separation_runner_2026_09_16.py | L |
| 1556 | sub | deposon_team/plugins/_p_n_curvature_potential_coupling_runner_2026_09_16.py | 9473 | `7355795bbc67` | source/tool | source/tool/_p_n_curvature_potential_coupling_runner_2026_09_16.py | L |
| 1557 | sub | deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py | 13230 | `d1bc564264ef` | source/tool | source/tool/_p_o_stranger_verification_runner_2026_09_16.py | L |
| 1558 | sub | deposon_team/plugins/_transfer_2026_09_15.ps1 | 2485 | `4b724f65286a` | source/tool | source/tool/_transfer_2026_09_15.ps1 | L |
| 1559 | sub | deposon_team/plugins/_transfer_2026_09_15.py | 2253 | `0f98b38169dd` | source/tool | source/tool/_transfer_2026_09_15.py | L |
| 1560 | sub | deposon_team/plugins/_v3x_18frozen_remeasure_2026_09_16.py | 5216 | `94686cf517f4` | source/tool | source/tool/_v3x_18frozen_remeasure_2026_09_16.py | L |
| 1561 | sub | deposon_team/plugins/_v3x_experiments_runner_2026_09_16.py | 18555 | `0fac09bec7c4` | source/tool | source/tool/_v3x_experiments_runner_2026_09_16.py | L |
| 1562 | sub | deposon_team/plugins/_v3x_p_k_verify_2026_09_16.py | 5373 | `e516675e3db5` | source/tool | source/tool/_v3x_p_k_verify_2026_09_16.py | L |
| 1563 | sub | deposon_team/plugins/_v42_v2_runner_2026_09_16.py | 22460 | `cf8a1f5fd383` | source/tool | source/tool/_v42_v2_runner_2026_09_16.py | L |
| 1564 | sub | deposon_team/plugins/attack_pc_a1_resampling.py | 4834 | `b3ff941c9b9e` | source/tool | source/tool/attack_pc_a1_resampling.py | L |
| 1565 | sub | deposon_team/plugins/attack_pc_a2_fitting.py | 4502 | `1861aecfbfe2` | source/tool | source/tool/attack_pc_a2_fitting.py | L |
| 1566 | sub | deposon_team/plugins/attack_pc_a3_clipping.py | 4469 | `3a62ad10abf7` | source/tool | source/tool/attack_pc_a3_clipping.py | L |
| 1567 | sub | deposon_team/plugins/fix_boss_naming_2026_09_16.py | 17479 | `21ad055e7e06` | source/tool | source/tool/fix_boss_naming_2026_09_16.py | L |
| 1568 | sub | deposon_team/plugins/fix_proactive_audit_2026_09_16.py | 15444 | `f5704c9b4497` | source/tool | source/tool/fix_proactive_audit_2026_09_16.py | L |
| 1569 | sub | deposon_team/plugins/fix_risk1_02940_boundary.py | 7125 | `1017671173cb` | source/tool | source/tool/fix_risk1_02940_boundary.py | L |
| 1570 | sub | deposon_team/plugins/fix_risk2_canonical5.py | 8871 | `cbdbfa029f70` | source/tool | source/tool/fix_risk2_canonical5.py | L |
| 1571 | sub | deposon_team/plugins/fix_risk3_s_eff_normalization.py | 13429 | `ba347f5d9982` | source/tool | source/tool/fix_risk3_s_eff_normalization.py | L |
| 1572 | sub | deposon_team/plugins/fix_selfcheck_bug_n1_2026_09_15.py | 4680 | `fb571653df6c` | source/tool | source/tool/fix_selfcheck_bug_n1_2026_09_15.py | L |
| 1573 | sub | deposon_team/plugins/fix_selfcheck_bug_n2_2026_09_15.py | 3412 | `eba2d444f4da` | source/tool | source/tool/fix_selfcheck_bug_n2_2026_09_15.py | L |
| 1574 | sub | deposon_team/plugins/fix_selfcheck_bug_n3_2026_09_15.py | 5134 | `47fc588b3cae` | source/tool | source/tool/fix_selfcheck_bug_n3_2026_09_15.py | L |
| 1575 | sub | deposon_team/plugins/fix_verify_freeze_policy_2026_09_16.py | 7122 | `fa521fe37da0` | source/tool | source/tool/fix_verify_freeze_policy_2026_09_16.py | L |
| 1576 | sub | deposon_team/plugins/git_commit_msg_2026_09_18.txt | 3223 | `b2841d12a444` | verdict/kd | verdict/kd/git_commit_msg_2026_09_18.txt | L |
| 1577 | sub | deposon_team/plugins/runner_pa_d1_d3.py | 27712 | `1b9578eadc14` | source/tool | source/tool/runner_pa_d1_d3.py | L |
| 1578 | sub | deposon_team/products/kimi_artifact_v_2026_09_16.json | 9938 | `1f8612344592` | readout/final | readout/final/kimi_artifact_v_2026_09_16.json | L |
| 1579 | sub | docs/ADVISOR_BRIEFING_2026-08-30.md | 5890 | `40278bc425e6` | verdict/kd | verdict/kd/ADVISOR_BRIEFING_2026-08-30.md | L |
| 1580 | sub | docs/FIGURES_v2.md | 5851 | `1cd4a4cb0a76` | doc/paper | doc/paper/FIGURES_v2.md | L |
| 1581 | sub | docs/LESSONS_v20_deepprobe.md | 8409 | `5c898d4407ee` | verdict/pi | verdict/pi/LESSONS_v20_deepprobe.md | L |
| 1582 | sub | docs/MODEL_ARGUMENTATION_v2.md | 30142 | `2c83c42804e4` | verdict/kd | verdict/kd/MODEL_ARGUMENTATION_v2.md | L |
| 1583 | sub | docs/SALVAGE_v2.md | 7312 | `f28a81d6302d` | doc/paper | doc/paper/SALVAGE_v2.md | L |
| 1584 | sub | docs/SPEC_GT2C.md | 3172 | `29af533486b2` | verdict/kd | verdict/kd/SPEC_GT2C.md | L |
| 1585 | sub | docs/SPEC_GT5C.md | 3046 | `1e41b4334735` | verdict/kd | verdict/kd/SPEC_GT5C.md | L |
| 1586 | sub | docs/SPEC_v1.5.md | 6204 | `c165a86cf551` | doc/paper | doc/paper/SPEC_v1.5.md | L |
| 1587 | sub | docs/THINKING_V3_GT_CONTRIB_2026.md | 19508 | `8c1d733f9182` | verdict/kd | verdict/kd/THINKING_V3_GT_CONTRIB_2026.md | L |
| 1588 | sub | docs/V3X/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md | 4840 | `354a1360234f` | doc/letter | doc/letter/BOSS_F_GHOST_PATH_NOTE_2026_09_11.md | L |
| 1589 | sub | docs/V3X/BOSS_URL_2026_09_11.md | 7135 | `1ba7419178a1` | doc/letter | doc/letter/BOSS_URL_2026_09_11.md | L |
| 1590 | sub | docs/V3X/D0_FREEZE_PREP_2026_09_09.md | 9844 | `0d1e88c258aa` | doc/readme | doc/readme/D0_FREEZE_PREP_2026_09_09.md | L |
| 1591 | sub | docs/V3X/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md | 6459 | `67063f9cb238` | verdict/judge | verdict/judge/D7_ONE_PAGE_SUMMARY_2026_09_11_v5.md | L |
| 1592 | sub | docs/V3X/D7_POST_CLEANUP_PLAN_2026_09_18.json | 20271 | `0b8a1a357aae` | readout/final | readout/final/D7_POST_CLEANUP_PLAN_2026_09_18.json | L |
| 1593 | sub | docs/V3X/D7_POST_CLEANUP_REPORT_2026_09_16.json | 1248 | `40955bf2abc5` | readout/final | readout/final/D7_POST_CLEANUP_REPORT_2026_09_16.json | L |
| 1594 | sub | docs/V3X/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md | 10692 | `51869e3184f4` | doc/paper | doc/paper/D7_PRE_V3_POLISH_AND_TEAM_IMPROVEMENT_2026_09_16.md | L |
| 1595 | sub | docs/V3X/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md | 22442 | `ac8997b07731` | doc/readme | doc/readme/DEPOSON_EMBEDDING_6WAY_THEORY_V0_2026_09_10.md | L |
| 1596 | sub | docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md | 26460 | `e4ee3999f7ce` | doc/readme | doc/readme/DPATH_CROSS_MODAL_2026_09_10.md | L |
| 1597 | sub | docs/V3X/KT_A1_SPEC_V0.1.md | 29570 | `78b71d404366` | doc/readme | doc/readme/KT_A1_SPEC_V0.1.md | L |
| 1598 | sub | docs/V3X/KT_B1_SPEC_V0.1.md | 39206 | `0397b757362f` | doc/readme | doc/readme/KT_B1_SPEC_V0.1.md | L |
| 1599 | sub | docs/V3X/KT_C1_SPEC_V0.1.md | 31241 | `59d8f56347d5` | doc/readme | doc/readme/KT_C1_SPEC_V0.1.md | L |
| 1600 | sub | docs/V3X/KT_D0_SPEC_V0.1.md | 20927 | `cce8e9a1b00e` | doc/readme | doc/readme/KT_D0_SPEC_V0.1.md | L |
| 1601 | sub | docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md | 10351 | `bd1caab42b4c` | doc/readme | doc/readme/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md | L |
| 1602 | sub | docs/V3X/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md | 3899 | `ee043a13f801` | verdict/judge | verdict/judge/P_C_P_E_V0_1_VERIFICATION_2026_09_12.md | L |
| 1603 | sub | docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md | 6301 | `d427b2f57c33` | doc/readme | doc/readme/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md | L |
| 1604 | sub | docs/V3X/P_C_V0_1_VERIFICATION_2026_09_12.md | 4885 | `00c7b7ceccdc` | doc/letter | doc/letter/P_C_V0_1_VERIFICATION_2026_09_12.md | L |
| 1605 | sub | docs/V3X/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md | 15021 | `fc73cab85d8f` | doc/readme | doc/readme/P_D_FINGERPRINT_V0_3_SPEC_CHANGELOG.md | L |
| 1606 | sub | docs/V3X/P_D_FINGERPRINT_V0_SPEC.md | 9192 | `3b67461b05fe` | doc/readme | doc/readme/P_D_FINGERPRINT_V0_SPEC.md | L |
| 1607 | sub | docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md | 13109 | `900da300d11e` | doc/letter | doc/letter/P_E_D1_D3_REPORT_2026_09_15.md | L |
| 1608 | sub | docs/V3X/P_F_RESEARCH_2026_09_09.md | 17603 | `98085df7811a` | verdict/kd | verdict/kd/P_F_RESEARCH_2026_09_09.md | L |
| 1609 | sub | docs/V3X/P_F_SPEC_V0.md | 19804 | `de90faf362c5` | doc/readme | doc/readme/P_F_SPEC_V0.md | L |
| 1610 | sub | docs/V3X/P_F_V0_1_VERIFICATION_2026_09_12.md | 4188 | `4d970e9c0aec` | doc/letter | doc/letter/P_F_V0_1_VERIFICATION_2026_09_12.md | L |
| 1611 | sub | docs/V3X/QUICK_KILL_6_DIRECTIONS.md | 15085 | `a476f241edb2` | doc/paper | doc/paper/QUICK_KILL_6_DIRECTIONS.md | L |
| 1612 | sub | docs/V3X/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md | 10708 | `00e543564e3f` | doc/readme | doc/readme/SPEC_V0_1_BOSS_SELFTEST_2026_09_09.md | L |
| 1613 | sub | docs/V3X/V3X_D6_PAPER_V2_2026_09_09_mavis.md | 24778 | `4d06d34cb6fa` | doc/paper | doc/paper/V3X_D6_PAPER_V2_2026_09_09_mavis.md | L |
| 1614 | sub | docs/V3X/V3X_D6_PAPER_zh.md | 19716 | `feae8af2fefe` | doc/paper | doc/paper/V3X_D6_PAPER_zh.md | L |
| 1615 | sub | docs/V3X/V3X_PROJECT_EVOLUTION_FOR_KIMI.md | 12908 | `4de2cbf57a49` | doc/letter | doc/letter/V3X_PROJECT_EVOLUTION_FOR_KIMI.md | L |
| 1616 | sub | docs/V3X/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md | 4775 | `e451a5a3d079` | doc/paper | doc/paper/V42_V2_REMEDIATION_CLAUSE_2026_09_16.md | L |
| 1617 | sub | docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md | 7344 | `f80cc4e1fb7f` | doc/letter | doc/letter/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md | L |
| 1618 | sub | docs/V3X_COLLAB_DIRECTIONS.md | 16363 | `5a27c2350036` | verdict/kd | verdict/kd/V3X_COLLAB_DIRECTIONS.md | L |
| 1619 | sub | docs/reviews/review_salvage_integration_v2X.md | 6212 | `96ae50306f36` | verdict/judge | verdict/judge/review_salvage_integration_v2X.md | L |
| 1620 | sub | results/_149_face_effect_disposal_2026_10_10.md | 24295 | `e7c1232df138` | verdict/pi | verdict/pi/_149_face_effect_disposal_2026_10_10.md | L |
| 1621 | sub | results/_a02_excluded_items_idx_collection_2026_10_10.md | 39565 | `03407e0b6662` | readout/final | readout/final/_a02_excluded_items_idx_collection_2026_10_10.md | L |
| 1622 | sub | results/_adendum_A_degradation_precheck_20260917_132049.json | 4248 | `38fabeb19691` | readout/final | readout/final/_adendum_A_degradation_precheck_20260917_132049.json | L |
| 1623 | sub | results/_adendum_C_pm_attack_surface_v2_20260917_133726.json | 4123 | `193ba7d66412` | readout/final | readout/final/_adendum_C_pm_attack_surface_v2_20260917_133726.json | L |
| 1624 | sub | results/_adendum_C_pm_attack_surface_v2_20260917_133852.json | 4122 | `6eba63788ca8` | readout/final | readout/final/_adendum_C_pm_attack_surface_v2_20260917_133852.json | L |
| 1625 | sub | results/_adendum_D_pc_r2_per_model_v2_20260917_133726.json | 4605 | `6fe706750823` | readout/final | readout/final/_adendum_D_pc_r2_per_model_v2_20260917_133726.json | L |
| 1626 | sub | results/_adendum_D_pc_r2_per_model_v2_20260917_133852.json | 4605 | `d66792eea40e` | readout/final | readout/final/_adendum_D_pc_r2_per_model_v2_20260917_133852.json | L |
| 1627 | sub | results/_adendum_E_pd_supplement_v2_20260917_133726.json | 1353 | `2c4790ffb6e3` | readout/final | readout/final/_adendum_E_pd_supplement_v2_20260917_133726.json | L |
| 1628 | sub | results/_adendum_E_pd_supplement_v2_20260917_133852.json | 1353 | `46d8dacb4721` | readout/final | readout/final/_adendum_E_pd_supplement_v2_20260917_133852.json | L |
| 1629 | sub | results/_adendum_F_pe_3modal_closure_llm_dispatch_20260917_132143.json | 3646 | `879494ed8fb9` | readout/final | readout/final/_adendum_F_pe_3modal_closure_llm_dispatch_20260917_132143.json | L |
| 1630 | sub | results/_adendum_F_pe_3modal_v2_20260917_143033.json | 38622 | `afab79249be7` | readout/final | readout/final/_adendum_F_pe_3modal_v2_20260917_143033.json | L |
| 1631 | sub | results/_adendum_G_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json | 2757 | `d10462080832` | readout/final | readout/final/_adendum_G_pf_dfix2_timing_converge_llm_dispatch_20260917_132143.json | L |
| 1632 | sub | results/_adendum_G_pf_dfix2_v2_20260917_143033.json | 95292 | `bf8db2ad255b` | readout/final | readout/final/_adendum_G_pf_dfix2_v2_20260917_143033.json | L |
| 1633 | sub | results/_adendum_H_pg_dhde_shrink_20260917_132049.json | 4613 | `b9a0253ba6a0` | readout/final | readout/final/_adendum_H_pg_dhde_shrink_20260917_132049.json | L |
| 1634 | sub | results/_adendum_I_po_captions_closure_20260917_132049.json | 4429 | `18165008bef6` | readout/final | readout/final/_adendum_I_po_captions_closure_20260917_132049.json | L |
| 1635 | sub | results/_adendum_J_warehouse_spearman_health_20260917_132049.json | 11337 | `df661d62426a` | readout/final | readout/final/_adendum_J_warehouse_spearman_health_20260917_132049.json | L |
| 1636 | sub | results/_adendum_K_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json | 2911 | `acdf933f68e0` | readout/final | readout/final/_adendum_K_087_cluster_cross_backbone_llm_dispatch_20260917_132143.json | L |
| 1637 | sub | results/_adendum_K_qwen3_087_cluster_v2_20260917_143033.json | 32481 | `43477c8ea2d6` | readout/final | readout/final/_adendum_K_qwen3_087_cluster_v2_20260917_143033.json | L |
| 1638 | sub | results/_adendum_L_verifier_dual_impl_diff_20260917_132049.json | 2783 | `1532607ded80` | readout/final | readout/final/_adendum_L_verifier_dual_impl_diff_20260917_132049.json | L |
| 1639 | sub | results/_adendum_M_pj_convergence_basin_v2_20260917_133726.json | 3694 | `ea7ffda97e20` | readout/final | readout/final/_adendum_M_pj_convergence_basin_v2_20260917_133726.json | L |
| 1640 | sub | results/_adendum_M_pj_convergence_basin_v2_20260917_133852.json | 3686 | `8ab01a1e42ae` | readout/final | readout/final/_adendum_M_pj_convergence_basin_v2_20260917_133852.json | L |
| 1641 | sub | results/_adendum_N_pn_coupling_v2_20260917_133726.json | 2012 | `1b91cc25ca57` | readout/final | readout/final/_adendum_N_pn_coupling_v2_20260917_133726.json | L |
| 1642 | sub | results/_adendum_N_pn_coupling_v2_20260917_133852.json | 2011 | `a32f3c8ba520` | readout/final | readout/final/_adendum_N_pn_coupling_v2_20260917_133852.json | L |
| 1643 | sub | results/_adendum_O_pk_v2_three_way_v2_20260917_133726.json | 1971 | `725fd7b961f8` | readout/final | readout/final/_adendum_O_pk_v2_three_way_v2_20260917_133726.json | L |
| 1644 | sub | results/_adendum_O_pk_v2_three_way_v2_20260917_133852.json | 1970 | `a30ff093305d` | readout/final | readout/final/_adendum_O_pk_v2_three_way_v2_20260917_133852.json | L |
| 1645 | sub | results/_adendum_P_pc_two_phase_fail_h0_20260917_132049.json | 2456 | `6b26daddc92c` | readout/final | readout/final/_adendum_P_pc_two_phase_fail_h0_20260917_132049.json | L |
| 1646 | sub | results/_alt_delib_pkg3_two_judgments_2026_10_10.md | 38032 | `3f52709a48e8` | readout/final | readout/final/_alt_delib_pkg3_two_judgments_2026_10_10.md | L |
| 1647 | sub | results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md | 7855 | `e240ca712be6` | doc/letter | doc/letter/_trae_d7_v1_audit_20260917_190000.md | L |
| 1648 | sub | results/_archive_2026_09_18/_trae_paper_8ch_双审_20260917_200000.md | 4040 | `bec666969ffc` | doc/paper | doc/paper/_trae_paper_8ch_双审_20260917_200000.md | L |
| 1649 | sub | results/_archive_2026_09_21/2026-09-20.md | 6186 | `be7aa1c479b2` | readout/final | readout/final/2026-09-20.md | L |
| 1650 | sub | results/_archive_2026_09_21/2026-09-21.md | 2676 | `ef648f34a3a3` | doc/letter | doc/letter/2026-09-21.md | L |
| 1651 | sub | results/_archive_2026_09_21/_archive_manifest_2026_09_21.json | 17353 | `33fe31633da8` | readout/final | readout/final/_archive_manifest_2026_09_21.json | L |
| 1652 | sub | results/_archive_2026_09_24/_final_verify.py | 2307 | `31a5d44497f1` | source/tool | source/tool/_final_verify.py | L |
| 1653 | sub | results/_archive_2026_09_24/_l13_latency_test.py | 2954 | `dae238354342` | source/tool | source/tool/_l13_latency_test.py | L |
| 1654 | sub | results/_archive_2026_09_24/_verify_worker_c.py | 1155 | `cc578c46b332` | source/tool | source/tool/_verify_worker_c.py | L |
| 1655 | sub | results/_archive_2026_09_24/l14_small_batch.py | 21784 | `0659c947bec1` | source/tool | source/tool/l14_small_batch.py | L |
| 1656 | sub | results/_archive_2026_09_24/latency_test.py | 617 | `fd9fd98785e1` | source/tool | source/tool/latency_test.py | L |
| 1657 | sub | results/_archive_manifest_non_upload_v2_2026_09_28.json | 236651 | `84eef669234b` | readout/final | readout/final/_archive_manifest_non_upload_v2_2026_09_28.json | L |
| 1658 | sub | results/_archive_manifest_non_upload_v3_2026_09_28.json | 204256 | `a2e4c5a9b713` | readout/final | readout/final/_archive_manifest_non_upload_v3_2026_09_28.json | L |
| 1659 | sub | results/_asset_identity_reconciliation_2026_10_01.md | 28291 | `0d22797f084f` | verdict/pi | verdict/pi/_asset_identity_reconciliation_2026_10_01.md | L |
| 1660 | sub | results/_axis1_three_recomputations_2026_10_11.md | 29938 | `8de23f7d7384` | verdict/judge | verdict/judge/_axis1_three_recomputations_2026_10_11.md | L |
| 1661 | sub | results/_b01_new_key_classification_2026_10_10.md | 38669 | `2ddfecf6201c` | verdict/kd | verdict/kd/_b01_new_key_classification_2026_10_10.md | L |
| 1662 | sub | results/_b01_new_key_residue_judgment_2026_10_10.md | 41984 | `345517455dcf` | verdict/kd | verdict/kd/_b01_new_key_residue_judgment_2026_10_10.md | L |
| 1663 | sub | results/_b_coincidence_disposition_judgment_2026_10_10.md | 42838 | `7ff80485955c` | verdict/pi | verdict/pi/_b_coincidence_disposition_judgment_2026_10_10.md | L |
| 1664 | sub | results/_backfill_rule_final_2026_10_09.md | 34602 | `3e97d5286760` | verdict/pi | verdict/pi/_backfill_rule_final_2026_10_09.md | L |
| 1665 | sub | results/_backfill_rule_vk_closeout_2026_10_08.md | 26890 | `20f5835d47d2` | verdict/judge | verdict/judge/_backfill_rule_vk_closeout_2026_10_08.md | L |
| 1666 | sub | results/_beta_formal_run_result_2026_10_09.json | 103691 | `a5a918fd9861` | readout/final | readout/final/_beta_formal_run_result_2026_10_09.json | L |
| 1667 | sub | results/_blade_caliber_b8_judgment_2026_10_10.md | 28738 | `e189d6eb63d9` | verdict/judge | verdict/judge/_blade_caliber_b8_judgment_2026_10_10.md | L |
| 1668 | sub | results/_c2_criterion_third_tier_draft_2026_10_11.md | 26713 | `844179898102` | verdict/kd | verdict/kd/_c2_criterion_third_tier_draft_2026_10_11.md | L |
| 1669 | sub | results/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md | 31607 | `4c369cb86db4` | readout/final | readout/final/_c4_math_corrections_E1_E2_execution_erratum_2026_10_10.md | L |
| 1670 | sub | results/_c4_math_corrections_downstream_erratum_2026_10_10.md | 28886 | `643cb9e249f7` | verdict/pi | verdict/pi/_c4_math_corrections_downstream_erratum_2026_10_10.md | L |
| 1671 | sub | results/_c4_theory_source_caliber_correction_2026_09_30.md | 25022 | `61b139efd0ef` | verdict/pi | verdict/pi/_c4_theory_source_caliber_correction_2026_09_30.md | L |
| 1672 | sub | results/_c_component4_three_items_judgment_2026_10_11.md | 41580 | `fd0094e2f865` | verdict/kd | verdict/kd/_c_component4_three_items_judgment_2026_10_11.md | L |
| 1673 | sub | results/_carrier_qid_disposition_2026_10_11.md | 3406 | `7d74d5a4d81e` | verdict/pi | verdict/pi/_carrier_qid_disposition_2026_10_11.md | L |
| 1674 | sub | results/_ci_bc_lines_ci_collection_2026_10_09.md | 24769 | `6db4d0fb2452` | verdict/pi | verdict/pi/_ci_bc_lines_ci_collection_2026_10_09.md | L |
| 1675 | sub | results/_ci_bc_scope_estimand_judgments_2026_10_09.md | 37682 | `d76ba2297d0d` | verdict/judge | verdict/judge/_ci_bc_scope_estimand_judgments_2026_10_09.md | L |
| 1676 | sub | results/_ci_detail_decoupling_degradation_baseline_2026_10_09.md | 20973 | `56b62ed5ab74` | verdict/kd | verdict/kd/_ci_detail_decoupling_degradation_baseline_2026_10_09.md | L |
| 1677 | sub | results/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md | 29709 | `bee0f1f0bdb2` | verdict/pi | verdict/pi/_ci_gap_fill_alt_bc_aper_prime_2026_10_09.md | L |
| 1678 | sub | results/_ci_line_establishment_2026_10_09.md | 28262 | `329c1c5e91d1` | verdict/kd | verdict/kd/_ci_line_establishment_2026_10_09.md | L |
| 1679 | sub | results/_coze_paper_v1_draft_2026_09_17.md | 29484 | `c08e7abf5ee3` | doc/paper | doc/paper/_coze_paper_v1_draft_2026_09_17.md | L |
| 1680 | sub | results/_d05_backbone_robustness_beta_20260918_100853.json | 1490 | `9b6f085d96dc` | readout/final | readout/final/_d05_backbone_robustness_beta_20260918_100853.json | L |
| 1681 | sub | results/_d05_i1i5_invariants_check_20260918_100853.json | 1920 | `f12af5435928` | readout/final | readout/final/_d05_i1i5_invariants_check_20260918_100853.json | L |
| 1682 | sub | results/_d05_main_run_results_20260918_100853.json | 15243 | `0a933d7c8d7a` | readout/final | readout/final/_d05_main_run_results_20260918_100853.json | L |
| 1683 | sub | results/_d05_main_run_results_nemotron_3.5_20260918_100853.json | 15111 | `1b1b6ad67c39` | readout/final | readout/final/_d05_main_run_results_nemotron_3.5_20260918_100853.json | L |
| 1684 | sub | results/_d05_main_run_results_qwen3_failed_20260918_100853.json | 18358 | `427b18da8114` | readout/final | readout/final/_d05_main_run_results_qwen3_failed_20260918_100853.json | L |
| 1685 | sub | results/_d05_opt_5_directions_results_20260918_100853.json | 5614 | `e5979133195a` | readout/final | readout/final/_d05_opt_5_directions_results_20260918_100853.json | L |
| 1686 | sub | results/_d1_backfill_b3_b7_suggestion_table_2026_10_01.md | 26731 | `8e1494301bb8` | verdict/judge | verdict/judge/_d1_backfill_b3_b7_suggestion_table_2026_10_01.md | L |
| 1687 | sub | results/_d1_backfill_collection_rounds_2026_10_01.md | 22908 | `2d1a0d43e588` | verdict/kd | verdict/kd/_d1_backfill_collection_rounds_2026_10_01.md | L |
| 1688 | sub | results/_d1_backfill_conflict_trace_2026_10_01.md | 31506 | `0cecda616f15` | verdict/kd | verdict/kd/_d1_backfill_conflict_trace_2026_10_01.md | L |
| 1689 | sub | results/_d1_backfill_readiness_pack_2026_10_01.md | 26462 | `ed644fb07f88` | verdict/judge | verdict/judge/_d1_backfill_readiness_pack_2026_10_01.md | L |
| 1690 | sub | results/_deposon_v2scripts_reverify_20260918_105219.json | 12888 | `8ac002ccb082` | readout/final | readout/final/_deposon_v2scripts_reverify_20260918_105219.json | L |
| 1691 | sub | results/_deposon_v2scripts_summary_挂点回扣_20260918_105219.json | 404 | `2ca5870e4659` | readout/final | readout/final/_deposon_v2scripts_summary_挂点回扣_20260918_105219.json | L |
| 1692 | sub | results/_e4_lineage_conflict_correction_2026_10_11.md | 30510 | `e20b96e32f54` | verdict/pi | verdict/pi/_e4_lineage_conflict_correction_2026_10_11.md | L |
| 1693 | sub | results/_e5_nonbinary_count_judgment_2026_10_10.md | 37762 | `2ef8797c03f4` | verdict/judge | verdict/judge/_e5_nonbinary_count_judgment_2026_10_10.md | L |
| 1694 | sub | results/_e6_alt_permp_comparability_closure_2026_10_10.md | 16636 | `1c663430b4aa` | readout/final | readout/final/_e6_alt_permp_comparability_closure_2026_10_10.md | L |
| 1695 | sub | results/_e6_case_a_judgment_face_promotion_2026_10_10.md | 42116 | `4e65c53f68e8` | verdict/pi | verdict/pi/_e6_case_a_judgment_face_promotion_2026_10_10.md | L |
| 1696 | sub | results/_e6_j5_backfill_resolution_2026_10_10.md | 23171 | `c888158b3263` | verdict/judge | verdict/judge/_e6_j5_backfill_resolution_2026_10_10.md | L |
| 1697 | sub | results/_e6_j5_semantics_conflict_judgment_2026_10_10.md | 27682 | `3c7628a4964d` | verdict/judge | verdict/judge/_e6_j5_semantics_conflict_judgment_2026_10_10.md | L |
| 1698 | sub | results/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md | 46261 | `442d5ff4acdb` | verdict/kd | verdict/kd/_e6_th_v3_19_residual_exits_judgment_2026_10_10.md | L |
| 1699 | sub | results/_exp03_blade_caliber_review_2026_10_10.md | 19797 | `8c030758b331` | verdict/kd | verdict/kd/_exp03_blade_caliber_review_2026_10_10.md | L |
| 1700 | sub | results/_exp05_missing_true_disposition_judgment_2026_10_10.md | 25552 | `e8e1e63a11db` | verdict/pi | verdict/pi/_exp05_missing_true_disposition_judgment_2026_10_10.md | L |
| 1701 | sub | results/_external_pat_ark_prep_2026_09_30.md | 14055 | `ca540e5cab23` | verdict/pi | verdict/pi/_external_pat_ark_prep_2026_09_30.md | L |
| 1702 | sub | results/_external_sibling_path_reference_rule_2026_10_01.md | 23871 | `e79eabb6cfa7` | doc/readme | doc/readme/_external_sibling_path_reference_rule_2026_10_01.md | L |
| 1703 | sub | results/_f3_definition_deep_judgment_2026_10_11.md | 42351 | `11945e587b1d` | verdict/judge | verdict/judge/_f3_definition_deep_judgment_2026_10_11.md | L |
| 1704 | sub | results/_f4_direction1_seed_and_domain_draft_2026_10_11.md | 33887 | `f77c080d9fc6` | verdict/kd | verdict/kd/_f4_direction1_seed_and_domain_draft_2026_10_11.md | L |
| 1705 | sub | results/_f5_d1_event_count_correction_2026_10_01.md | 24994 | `771641e234d6` | verdict/pi | verdict/pi/_f5_d1_event_count_correction_2026_10_01.md | L |
| 1706 | sub | results/_family_e_q_type_conflict_resolution_2026_10_14.md | 19640 | `dd5547b8e8c7` | verdict/judge | verdict/judge/_family_e_q_type_conflict_resolution_2026_10_14.md | L |
| 1707 | sub | results/_four_items_execution_batch_2026_10_11.md | 31515 | `8006d1962e5f` | verdict/pi | verdict/pi/_four_items_execution_batch_2026_10_11.md | L |
| 1708 | sub | results/_g10_threshold_closed_domain_judgment_2026_10_11.md | 55727 | `586abda5ddf7` | verdict/judge | verdict/judge/_g10_threshold_closed_domain_judgment_2026_10_11.md | L |
| 1709 | sub | results/_g4_e3_definition_independent_judgment_2026_10_09.md | 29094 | `aebaff5b503c` | verdict/kd | verdict/kd/_g4_e3_definition_independent_judgment_2026_10_09.md | L |
| 1710 | sub | results/_g4_runtime_state_trace_2026_10_01.md | 25631 | `e0ae0ad66acb` | verdict/pi | verdict/pi/_g4_runtime_state_trace_2026_10_01.md | L |
| 1711 | sub | results/_g5_ccp_p0_verification_2026_10_10.md | 24819 | `8c7693379496` | readout/final | readout/final/_g5_ccp_p0_verification_2026_10_10.md | L |
| 1712 | sub | results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md | 48727 | `16c31894d445` | verdict/judge | verdict/judge/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md | L |
| 1713 | sub | results/_g5_seg3_tie_veto_judgment_2026_10_10.md | 35983 | `3306d1fd020d` | verdict/judge | verdict/judge/_g5_seg3_tie_veto_judgment_2026_10_10.md | L |
| 1714 | sub | results/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md | 33976 | `c3117773ab36` | verdict/judge | verdict/judge/_g5_x4_dual_axis_interpretation_judgment_2026_10_10.md | L |
| 1715 | sub | results/_gap_closeout_status_2026_10_09.md | 28793 | `ea41e346c4c4` | verdict/pi | verdict/pi/_gap_closeout_status_2026_10_09.md | L |
| 1716 | sub | results/_give_up_n10_erratum_2026_10_10.md | 22021 | `e0db6b819138` | verdict/kd | verdict/kd/_give_up_n10_erratum_2026_10_10.md | L |
| 1717 | sub | results/_glm_five_items_suggestion_table_2026_10_01.md | 29622 | `f2b1359be37d` | doc/paper | doc/paper/_glm_five_items_suggestion_table_2026_10_01.md | L |
| 1718 | sub | results/_glm_response_v2_template_2026_09_18.md | 44191 | `972401e056f6` | doc/paper | doc/paper/_glm_response_v2_template_2026_09_18.md | L |
| 1719 | sub | results/_itemH_fingerprint_provenance_2026_10_12.md | 22752 | `bacbee9a158f` | readout/final | readout/final/_itemH_fingerprint_provenance_2026_10_12.md | L |
| 1720 | sub | results/_j2_identifier_coupling_judgment_2026_10_11.md | 34261 | `2fd4505fdca2` | verdict/judge | verdict/judge/_j2_identifier_coupling_judgment_2026_10_11.md | L |
| 1721 | sub | results/_k_cf_4_low_cardinality_recure_2026_10_09.md | 33788 | `5f91d553e392` | verdict/kd | verdict/kd/_k_cf_4_low_cardinality_recure_2026_10_09.md | L |
| 1722 | sub | results/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md | 31801 | `618280cb8cfd` | verdict/kd | verdict/kd/_k_cf_4_low_cardinality_reurecheck_and_precedent_fill_2026_10_09.md | L |
| 1723 | sub | results/_k_v3s_4_2_domain_extension_judgment_2026_10_09.md | 23018 | `a802af7ac3bc` | verdict/judge | verdict/judge/_k_v3s_4_2_domain_extension_judgment_2026_10_09.md | L |
| 1724 | sub | results/_kimi_push_v3_manifest_batch10_1b753116.json | 5007 | `326adca520f1` | readout/final | readout/final/_kimi_push_v3_manifest_batch10_1b753116.json | L |
| 1725 | sub | results/_kimi_push_v3_manifest_batch11_7d6a7c8f.json | 2573 | `383446f24707` | readout/final | readout/final/_kimi_push_v3_manifest_batch11_7d6a7c8f.json | L |
| 1726 | sub | results/_kimi_push_v3_manifest_batch12_a2853574.json | 1246 | `6be21f9586ec` | readout/final | readout/final/_kimi_push_v3_manifest_batch12_a2853574.json | L |
| 1727 | sub | results/_kimi_push_v3_manifest_batch13_83f895f9.json | 739 | `0694838f66a8` | readout/final | readout/final/_kimi_push_v3_manifest_batch13_83f895f9.json | L |
| 1728 | sub | results/_kimi_push_v3_manifest_batch14_e5952130.json | 1055 | `64aa9d8a5c7d` | readout/final | readout/final/_kimi_push_v3_manifest_batch14_e5952130.json | L |
| 1729 | sub | results/_kimi_push_v3_manifest_batch15_0e65fe2f.json | 385 | `cfc345d10c7d` | readout/final | readout/final/_kimi_push_v3_manifest_batch15_0e65fe2f.json | L |
| 1730 | sub | results/_kimi_push_v3_manifest_batch1_77e2f952.json | 2534 | `b5f517a321a3` | readout/final | readout/final/_kimi_push_v3_manifest_batch1_77e2f952.json | L |
| 1731 | sub | results/_kimi_push_v3_manifest_batch2_e18c17bb.json | 9260 | `f14341b8a1a1` | readout/final | readout/final/_kimi_push_v3_manifest_batch2_e18c17bb.json | L |
| 1732 | sub | results/_kimi_push_v3_manifest_batch3_01ecf050.json | 9656 | `fd64909ea1d8` | readout/final | readout/final/_kimi_push_v3_manifest_batch3_01ecf050.json | L |
| 1733 | sub | results/_kimi_push_v3_manifest_batch4_2f872d54.json | 9720 | `d35453f21049` | readout/final | readout/final/_kimi_push_v3_manifest_batch4_2f872d54.json | L |
| 1734 | sub | results/_kimi_push_v3_manifest_batch5_34439e1e.json | 9511 | `2769b83f5b1d` | readout/final | readout/final/_kimi_push_v3_manifest_batch5_34439e1e.json | L |
| 1735 | sub | results/_kimi_push_v3_manifest_batch6_28055e59.json | 10107 | `f3eb7a38ae7d` | readout/final | readout/final/_kimi_push_v3_manifest_batch6_28055e59.json | L |
| 1736 | sub | results/_kimi_push_v3_manifest_batch7_0903df7e.json | 9748 | `7bda1fecd7c4` | readout/final | readout/final/_kimi_push_v3_manifest_batch7_0903df7e.json | L |
| 1737 | sub | results/_kimi_push_v3_manifest_batch8_7468a23b.json | 9880 | `5a38fc02978c` | readout/final | readout/final/_kimi_push_v3_manifest_batch8_7468a23b.json | L |
| 1738 | sub | results/_kimi_push_v3_manifest_batch9_f7d9cf1d.json | 9745 | `968d7c6c43ca` | readout/final | readout/final/_kimi_push_v3_manifest_batch9_f7d9cf1d.json | L |
| 1739 | sub | results/_kimi_push_v3_manifest_verifier21_cc3c92d0.json | 4159 | `5a6601f47632` | readout/final | readout/final/_kimi_push_v3_manifest_verifier21_cc3c92d0.json | L |
| 1740 | sub | results/_kimi_safe_batch_push_v1_2026_09_17.json | 7280 | `4a204fb0d682` | readout/final | readout/final/_kimi_safe_batch_push_v1_2026_09_17.json | L |
| 1741 | sub | results/_kimi_safe_batch_push_v2_full_2026_09_17.json | 47954 | `adf3a8017e26` | readout/final | readout/final/_kimi_safe_batch_push_v2_full_2026_09_17.json | L |
| 1742 | sub | results/_kimi_safe_batch_push_v3_full_2026_09_17.json | 7954 | `058099c10cfb` | readout/final | readout/final/_kimi_safe_batch_push_v3_full_2026_09_17.json | L |
| 1743 | sub | results/_kj1_judgment_premise_correction_2026_10_11.md | 35050 | `003b134cce24` | verdict/pi | verdict/pi/_kj1_judgment_premise_correction_2026_10_11.md | L |
| 1744 | sub | results/_kj1_sc1_premise_correction_2026_10_11.md | 31044 | `8b344b9b4715` | verdict/pi | verdict/pi/_kj1_sc1_premise_correction_2026_10_11.md | L |
| 1745 | sub | results/_kj4_e4_unification_judgment_2026_10_11.md | 36839 | `a14d49f7d3a2` | verdict/judge | verdict/judge/_kj4_e4_unification_judgment_2026_10_11.md | L |
| 1746 | sub | results/_krj10_reverdict_after_r4_convergence_2026_10_11.md | 31672 | `a21915ec55a7` | verdict/judge | verdict/judge/_krj10_reverdict_after_r4_convergence_2026_10_11.md | L |
| 1747 | sub | results/_krj5_subject_scope_judgment_2026_10_11.md | 45372 | `ae9df5119861` | verdict/judge | verdict/judge/_krj5_subject_scope_judgment_2026_10_11.md | L |
| 1748 | sub | results/_krj5d_third_tier_effectivity_2026_10_11.md | 10729 | `062093d95c9f` | verdict/pi | verdict/pi/_krj5d_third_tier_effectivity_2026_10_11.md | L |
| 1749 | sub | results/_krj_cond4_bytes_erratum_2026_10_11.md | 3886 | `78a95e5561fc` | readout/final | readout/final/_krj_cond4_bytes_erratum_2026_10_11.md | L |
| 1750 | sub | results/_kv3s_4_1_2_rejudge_2026_10_09.md | 51594 | `9cde399502ba` | verdict/judge | verdict/judge/_kv3s_4_1_2_rejudge_2026_10_09.md | L |
| 1751 | sub | results/_kv3s_4_4_carryover_bytes_correction_2026_10_10.md | 5807 | `0a7d2ccf74ad` | verdict/judge | verdict/judge/_kv3s_4_4_carryover_bytes_correction_2026_10_10.md | L |
| 1752 | sub | results/_kv3s_4_4_review_carryover_2026_10_10.md | 17606 | `660d40ddd78c` | verdict/pi | verdict/pi/_kv3s_4_4_review_carryover_2026_10_10.md | L |
| 1753 | sub | results/_lim_aperiod_adoption_and_label_correction_2026_10_11.md | 14770 | `f4b129e3312f` | verdict/pi | verdict/pi/_lim_aperiod_adoption_and_label_correction_2026_10_11.md | L |
| 1754 | sub | results/_lim_aperiod_restatement_third_domain_2026_10_11.md | 27946 | `8672a5541ca8` | verdict/judge | verdict/judge/_lim_aperiod_restatement_third_domain_2026_10_11.md | L |
| 1755 | sub | results/_log_observation_review_2026_10_08.md | 2918 | `ae20780c8d4e` | verdict/judge | verdict/judge/_log_observation_review_2026_10_08.md | L |
| 1756 | sub | results/_n01_n08_revision_2026_10_10.md | 26628 | `fa8400d8ae70` | verdict/kd | verdict/kd/_n01_n08_revision_2026_10_10.md | L |
| 1757 | sub | results/_n1_d4_clause_placement_determination_2026_10_01.md | 53732 | `7cda6adea62b` | verdict/kd | verdict/kd/_n1_d4_clause_placement_determination_2026_10_01.md | L |
| 1758 | sub | results/_n7_mutual_exclusion_determination_2026_10_01.md | 40169 | `b6bdf807cb27` | verdict/judge | verdict/judge/_n7_mutual_exclusion_determination_2026_10_01.md | L |
| 1759 | sub | results/_numbering_face_signature_effect_2026_10_13.md | 11273 | `6a7f0a1890a4` | verdict/pi | verdict/pi/_numbering_face_signature_effect_2026_10_13.md | L |
| 1760 | sub | results/_numbering_family_count_corrigendum_2026_10_14.md | 19812 | `9baf2ea2e9cb` | verdict/judge | verdict/judge/_numbering_family_count_corrigendum_2026_10_14.md | L |
| 1761 | sub | results/_numbering_raw_residual_461_variants_corrigendum_2026_10_14.md | 5239 | `33feb734ca80` | verdict/judge | verdict/judge/_numbering_raw_residual_461_variants_corrigendum_2026_10_14.md | L |
| 1762 | sub | results/_p4_attribution_determination_2026_10_01.md | 22053 | `c6793cff46d7` | verdict/kd | verdict/kd/_p4_attribution_determination_2026_10_01.md | L |
| 1763 | sub | results/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json | 12992 | `05ff758ae921` | readout/final | readout/final/_p_k_v3_three_way_rerun_2026-09-17T08-23-41Z.json | L |
| 1764 | sub | results/_p_l_v3_phase2_beta_summary_20260917_142748.json | 2417 | `86d4cb146241` | readout/final | readout/final/_p_l_v3_phase2_beta_summary_20260917_142748.json | L |
| 1765 | sub | results/_p_l_v3_phase2_closedsource_summary_20260917_175544.json | 3286 | `a3eafaf9ba03` | readout/final | readout/final/_p_l_v3_phase2_closedsource_summary_20260917_175544.json | L |
| 1766 | sub | results/_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json | 4357 | `c366f4e30b6b` | readout/final | readout/final/_p_l_v3_phase2_doubao_v2_summary_20260917_170828.json | L |
| 1767 | sub | results/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json | 14469 | `e3dccddaed87` | readout/final | readout/final/_p_l_v3_phase2_doubao_v2_summary_20260917_172206.json | L |
| 1768 | sub | results/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json | 8308 | `21c9f23699a8` | readout/final | readout/final/_p_l_v3_phase2_or_embedding_v3_summary_20260917_162614.json | L |
| 1769 | sub | results/_p_l_v3_real_collapse_mistral_L100_20260917_132341.json | 43903 | `4657b210782a` | readout/final | readout/final/_p_l_v3_real_collapse_mistral_L100_20260917_132341.json | L |
| 1770 | sub | results/_p_l_v3_real_collapse_mistral_L30_20260917_132341.json | 16545 | `f6ab84f27d9a` | readout/final | readout/final/_p_l_v3_real_collapse_mistral_L30_20260917_132341.json | L |
| 1771 | sub | results/_p_l_v3_real_collapse_mistral_L45_20260917_132341.json | 20108 | `dc37ee54781c` | readout/final | readout/final/_p_l_v3_real_collapse_mistral_L45_20260917_132341.json | L |
| 1772 | sub | results/_p_l_v3_real_collapse_mistral_L60_20260917_132341.json | 1174 | `e3fb4f775e22` | readout/final | readout/final/_p_l_v3_real_collapse_mistral_L60_20260917_132341.json | L |
| 1773 | sub | results/_p_l_v3_robustness_claude_sonnet5_L30_20260917_174011.json | 30772 | `9d329721f67d` | readout/final | readout/final/_p_l_v3_robustness_claude_sonnet5_L30_20260917_174011.json | L |
| 1774 | sub | results/_p_l_v3_robustness_claude_sonnet5_L60_20260917_174011.json | 1292 | `28e462c11692` | readout/final | readout/final/_p_l_v3_robustness_claude_sonnet5_L60_20260917_174011.json | L |
| 1775 | sub | results/_p_l_v3_robustness_gemini_37flash_L30_20260917_175003.json | 30514 | `0f5c80a8a4ae` | readout/final | readout/final/_p_l_v3_robustness_gemini_37flash_L30_20260917_175003.json | L |
| 1776 | sub | results/_p_l_v3_robustness_gemini_37flash_L60_20260917_175003.json | 1288 | `e2590651f9c0` | readout/final | readout/final/_p_l_v3_robustness_gemini_37flash_L60_20260917_175003.json | L |
| 1777 | sub | results/_p_l_v3_robustness_glm53_L30_20260917_142011.json | 18281 | `2deadd7be100` | readout/final | readout/final/_p_l_v3_robustness_glm53_L30_20260917_142011.json | L |
| 1778 | sub | results/_p_l_v3_robustness_glm53_L60_20260917_142011.json | 1037 | `31556b58caa1` | readout/final | readout/final/_p_l_v3_robustness_glm53_L60_20260917_142011.json | L |
| 1779 | sub | results/_p_l_v3_robustness_gpt56sol_L30_20260917_173159.json | 30347 | `3865d7a61ca1` | readout/final | readout/final/_p_l_v3_robustness_gpt56sol_L30_20260917_173159.json | L |
| 1780 | sub | results/_p_l_v3_robustness_gpt56sol_L60_20260917_173159.json | 1266 | `8c79e9a289fb` | readout/final | readout/final/_p_l_v3_robustness_gpt56sol_L60_20260917_173159.json | L |
| 1781 | sub | results/_p_l_v3_robustness_mistral_L60_20260917_142748.json | 1071 | `ba41a0d4b927` | readout/final | readout/final/_p_l_v3_robustness_mistral_L60_20260917_142748.json | L |
| 1782 | sub | results/_p_l_v3_robustness_qwen3_L30_20260917_140017.json | 18595 | `e9bac1743a2a` | readout/final | readout/final/_p_l_v3_robustness_qwen3_L30_20260917_140017.json | L |
| 1783 | sub | results/_p_l_v3_robustness_qwen3_L60_20260917_140017.json | 1057 | `f79f1b00e5d3` | readout/final | readout/final/_p_l_v3_robustness_qwen3_L60_20260917_140017.json | L |
| 1784 | sub | results/_p_l_v3_vector_embedding_doubao-text-240715_L30_20260917_172206.json | 18509 | `2d4827f9cda2` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-text-240715_L30_20260917_172206.json | L |
| 1785 | sub | results/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_171614.json | 1669762 | `2b91eb1dbbcf` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_171614.json | L |
| 1786 | sub | results/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_172206.json | 1670172 | `e836a04a04d8` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-vision-241215_L30_20260917_172206.json | L |
| 1787 | sub | results/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_171614.json | 1670501 | `46c99397f01b` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_171614.json | L |
| 1788 | sub | results/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_172206.json | 1669285 | `0432f25cf6c3` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-vision-250328_L30_20260917_172206.json | L |
| 1789 | sub | results/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_171614.json | 1670027 | `6b8af7d8bca9` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_171614.json | L |
| 1790 | sub | results/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_172206.json | 1671116 | `710b7f291355` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-vision-250615_L30_20260917_172206.json | L |
| 1791 | sub | results/_p_l_v3_vector_embedding_doubao-vision-251215_L30_20260917_172206.json | 1670482 | `a00976c6f87b` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao-vision-251215_L30_20260917_172206.json | L |
| 1792 | sub | results/_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json | 11834 | `b9488e2b01ae` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json | L |
| 1793 | sub | results/_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json | 18468 | `198f8fe39f94` | readout/final | readout/final/_p_l_v3_vector_embedding_doubao_L30_20260917_170828.json | L |
| 1794 | sub | results/_p_l_v3_vector_embedding_glm53_L30_20260917_142748.json | 11833 | `d91b0c5f642f` | readout/final | readout/final/_p_l_v3_vector_embedding_glm53_L30_20260917_142748.json | L |
| 1795 | sub | results/_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json | 11835 | `33d0259073dc` | readout/final | readout/final/_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json | L |
| 1796 | sub | results/_p_l_v3_vector_embedding_or_bge-large_L30_20260917_162614.json | 1017974 | `aff028e8506c` | readout/final | readout/final/_p_l_v3_vector_embedding_or_bge-large_L30_20260917_162614.json | L |
| 1797 | sub | results/_p_l_v3_vector_embedding_or_e5-multi_L30_20260917_162614.json | 1017684 | `8676b519a031` | readout/final | readout/final/_p_l_v3_vector_embedding_or_e5-multi_L30_20260917_162614.json | L |
| 1798 | sub | results/_p_l_v3_vector_embedding_or_gte-large_L30_20260917_162614.json | 1017381 | `07561d4d23d1` | readout/final | readout/final/_p_l_v3_vector_embedding_or_gte-large_L30_20260917_162614.json | L |
| 1799 | sub | results/_p_l_v3_vector_embedding_or_qwen3-emb-8b_L30_20260917_162614.json | 3929893 | `a4bd70c02aaa` | readout/final | readout/final/_p_l_v3_vector_embedding_or_qwen3-emb-8b_L30_20260917_162614.json | L |
| 1800 | sub | results/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_170828.json | 2452705 | `1928ada51527` | readout/final | readout/final/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_170828.json | L |
| 1801 | sub | results/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_172206.json | 2452273 | `bebee5346543` | readout/final | readout/final/_p_l_v3_vector_embedding_qwen3-emb-4b_L30_20260917_172206.json | L |
| 1802 | sub | results/_p_l_v3_vector_embedding_qwen3_L30_20260917_142748.json | 11833 | `26f7493f1c95` | readout/final | readout/final/_p_l_v3_vector_embedding_qwen3_L30_20260917_142748.json | L |
| 1803 | sub | results/_p_refresh_registration_preliminary_2026_10_10.md | 32780 | `a3e14b508a4a` | verdict/kd | verdict/kd/_p_refresh_registration_preliminary_2026_10_10.md | L |
| 1804 | sub | results/_p_refresh_s0_judgment_2026_10_10.md | 41449 | `369173063a7c` | verdict/kd | verdict/kd/_p_refresh_s0_judgment_2026_10_10.md | L |
| 1805 | sub | results/_p_refresh_scope_judgment_2026_10_10.md | 34004 | `44e98dc31e2b` | verdict/kd | verdict/kd/_p_refresh_scope_judgment_2026_10_10.md | L |
| 1806 | sub | results/_pending_supply_search_receipt_2026_10_08.md | 12595 | `11bbee2bea42` | doc/paper | doc/paper/_pending_supply_search_receipt_2026_10_08.md | L |
| 1807 | sub | results/_phase1_completion_judgment_2026_10_10.md | 28836 | `6049c68f027b` | verdict/judge | verdict/judge/_phase1_completion_judgment_2026_10_10.md | L |
| 1808 | sub | results/_protocol_version_landing_status_2026_10_09.md | 11562 | `1d1895489d17` | verdict/pi | verdict/pi/_protocol_version_landing_status_2026_10_09.md | L |
| 1809 | sub | results/_q2_scope_vs_revision_judgment_2026_10_11.md | 43195 | `b4f00e5a69c4` | verdict/kd | verdict/kd/_q2_scope_vs_revision_judgment_2026_10_11.md | L |
| 1810 | sub | results/_r1_amendment_undetermined_face_2026_10_01.md | 45128 | `dab48b4d77c2` | verdict/kd | verdict/kd/_r1_amendment_undetermined_face_2026_10_01.md | L |
| 1811 | sub | results/_r2_reference_pointer_disposition_2026_10_11.md | 3121 | `403adec92ce1` | verdict/pi | verdict/pi/_r2_reference_pointer_disposition_2026_10_11.md | L |
| 1812 | sub | results/_r3_wording_disposition_2026_10_11.md | 3917 | `9d381c9d95e6` | verdict/pi | verdict/pi/_r3_wording_disposition_2026_10_11.md | L |
| 1813 | sub | results/_r4_convergence_2026_10_11.md | 3133 | `678394c47724` | verdict/pi | verdict/pi/_r4_convergence_2026_10_11.md | L |
| 1814 | sub | results/_r6_disposition_2026_10_11.md | 3704 | `cc51203fe8f5` | verdict/pi | verdict/pi/_r6_disposition_2026_10_11.md | L |
| 1815 | sub | results/_r_pair_nonportrait_full_document_review_2026_10_09.md | 28176 | `d8d5e4d2154f` | verdict/judge | verdict/judge/_r_pair_nonportrait_full_document_review_2026_10_09.md | L |
| 1816 | sub | results/_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md | 23975 | `5faa16446171` | verdict/kd | verdict/kd/_r_pair_rp3b_rp2_rpq6_judgments_2026_10_09.md | L |
| 1817 | sub | results/_r_pair_texts_independent_review_2026_10_09.md | 35443 | `8c5f83c3c4cf` | verdict/judge | verdict/judge/_r_pair_texts_independent_review_2026_10_09.md | L |
| 1818 | sub | results/_refcheck_hash_change_reference_recheck_2026_09_30.md | 33625 | `f011c29944b9` | verdict/pi | verdict/pi/_refcheck_hash_change_reference_recheck_2026_09_30.md | L |
| 1819 | sub | results/_registry_lag_correction_batch_2026_10_01.md | 36367 | `5b86fbf0cbbd` | verdict/pi | verdict/pi/_registry_lag_correction_batch_2026_10_01.md | L |
| 1820 | sub | results/_remote_residual_disposal_execution_order_2026_10_08.md | 36486 | `602c4d09623d` | verdict/kd | verdict/kd/_remote_residual_disposal_execution_order_2026_10_08.md | L |
| 1821 | sub | results/_round56_gu_backdoor_exclusion_revision_2026_10_10.md | 25045 | `52d3b10a16a0` | verdict/pi | verdict/pi/_round56_gu_backdoor_exclusion_revision_2026_10_10.md | L |
| 1822 | sub | results/_round56_pending_questions_compilation_2026_10_10.md | 33504 | `ef09b3d28a0f` | verdict/judge | verdict/judge/_round56_pending_questions_compilation_2026_10_10.md | L |
| 1823 | sub | results/_round56_registration_supplement_2026_10_10.md | 21865 | `71a59735302c` | verdict/pi | verdict/pi/_round56_registration_supplement_2026_10_10.md | L |
| 1824 | sub | results/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md | 16640 | `af4c3335538a` | verdict/pi | verdict/pi/_round56_sc4_nstar_inconsistency_erratum_2026_10_10.md | L |
| 1825 | sub | results/_round56c_d23_ad5_judgment_2026_10_10.md | 50747 | `061813859345` | verdict/judge | verdict/judge/_round56c_d23_ad5_judgment_2026_10_10.md | L |
| 1826 | sub | results/_rpq_wordlist_and_t1p2_judgments_2026_10_09.md | 44796 | `246ce35c4ddc` | verdict/kd | verdict/kd/_rpq_wordlist_and_t1p2_judgments_2026_10_09.md | L |
| 1827 | sub | results/_s2prime_krj3_applicability_recheck_2026_10_10.md | 41322 | `10518510b628` | verdict/judge | verdict/judge/_s2prime_krj3_applicability_recheck_2026_10_10.md | L |
| 1828 | sub | results/_s5dp_mixed_object_erratum_2026_10_11.md | 8380 | `07cde000e66f` | verdict/pi | verdict/pi/_s5dp_mixed_object_erratum_2026_10_11.md | L |
| 1829 | sub | results/_s7doubleprime_verification_2026_10_11.md | 41680 | `06ac684b4923` | verdict/kd | verdict/kd/_s7doubleprime_verification_2026_10_11.md | L |
| 1830 | sub | results/_s7doubleprime_verification_erratum_2026_10_11.md | 32822 | `9ff40693e4ac` | verdict/kd | verdict/kd/_s7doubleprime_verification_erratum_2026_10_11.md | L |
| 1831 | sub | results/_s7prime_findings_erratum_2026_10_11.md | 31008 | `a7dfa8e789b7` | verdict/kd | verdict/kd/_s7prime_findings_erratum_2026_10_11.md | L |
| 1832 | sub | results/_s7prime_prereq_and_verification_2026_10_11.md | 36787 | `e44da4b83810` | verdict/kd | verdict/kd/_s7prime_prereq_and_verification_2026_10_11.md | L |
| 1833 | sub | results/_seed_double_identifier_final_judgment_2026_10_11.md | 50222 | `728d18391748` | verdict/pi | verdict/pi/_seed_double_identifier_final_judgment_2026_10_11.md | L |
| 1834 | sub | results/_seed_double_rule_judgment_2026_10_11.md | 57185 | `f70a689fd8c1` | verdict/judge | verdict/judge/_seed_double_rule_judgment_2026_10_11.md | L |
| 1835 | sub | results/_skill_load_failure_window_readonly_facts_2026_09_30.md | 23065 | `9f5b73620b8a` | verdict/pi | verdict/pi/_skill_load_failure_window_readonly_facts_2026_09_30.md | L |
| 1836 | sub | results/_t1_7_2_correction_2026_10_08.md | 16469 | `d90bf82338f6` | verdict/judge | verdict/judge/_t1_7_2_correction_2026_10_08.md | L |
| 1837 | sub | results/_t1_p2_aggregation_caliber_judgment_2026_10_09.md | 14397 | `02f44f5bf2dd` | verdict/judge | verdict/judge/_t1_p2_aggregation_caliber_judgment_2026_10_09.md | L |
| 1838 | sub | results/_t1_r2_d1_field_caliber_correction_2026_10_09.md | 25396 | `99cafda125f1` | readout/final | readout/final/_t1_r2_d1_field_caliber_correction_2026_10_09.md | L |
| 1839 | sub | results/_t1_temp_axis_retirement_consolidation_2026_10_10.md | 20308 | `40cb2e81425a` | readout/final | readout/final/_t1_temp_axis_retirement_consolidation_2026_10_10.md | L |
| 1840 | sub | results/_t1_temp_axis_retirement_judgment_2026_10_10.md | 27384 | `19afc7e191a7` | readout/final | readout/final/_t1_temp_axis_retirement_judgment_2026_10_10.md | L |
| 1841 | sub | results/_t1p2_enable_judgment_2026_10_10.md | 20132 | `1e97d06b6ec9` | verdict/judge | verdict/judge/_t1p2_enable_judgment_2026_10_10.md | L |
| 1842 | sub | results/_t1p2_escalation_judgment_2026_10_10.md | 22930 | `5f43775a3224` | verdict/judge | verdict/judge/_t1p2_escalation_judgment_2026_10_10.md | L |
| 1843 | sub | results/_t1p2_judgment_bytes_correction_2026_10_10.md | 6377 | `d9d29bec3a0b` | verdict/judge | verdict/judge/_t1p2_judgment_bytes_correction_2026_10_10.md | L |
| 1844 | sub | results/_theory_input_request_supplement_2026_09_29.md | 48190 | `c966e7b605af` | verdict/kd | verdict/kd/_theory_input_request_supplement_2026_09_29.md | L |
| 1845 | sub | results/_three_pending_items_drafts_2026_10_11.md | 51748 | `8995859e5a76` | verdict/judge | verdict/judge/_three_pending_items_drafts_2026_10_11.md | L |
| 1846 | sub | results/_three_pending_items_effectivity_2026_10_11.md | 16744 | `df1f5f75c7a0` | verdict/pi | verdict/pi/_three_pending_items_effectivity_2026_10_11.md | L |
| 1847 | sub | results/_tra_v0_2026_09_10.json | 3695 | `0b096048e01d` | readout/final | readout/final/_tra_v0_2026_09_10.json | L |
| 1848 | sub | results/_track2_qwen_check_2026_09_23.json | 2513 | `727d1ffc7f3f` | readout/final | readout/final/_track2_qwen_check_2026_09_23.json | L |
| 1849 | sub | results/_trigger_denominator_caliber_judgment_2026_10_11.md | 43448 | `16bf9332deef` | verdict/kd | verdict/kd/_trigger_denominator_caliber_judgment_2026_10_11.md | L |
| 1850 | sub | results/_trj_w1_downstream_erratum_2026_10_10.md | 24888 | `e52d0016fbc6` | readout/final | readout/final/_trj_w1_downstream_erratum_2026_10_10.md | L |
| 1851 | sub | results/_trj_w1_verification_2026_10_10.md | 23014 | `cc6de8e981f6` | verdict/pi | verdict/pi/_trj_w1_verification_2026_10_10.md | L |
| 1852 | sub | results/_typeb_m_registration_2026_10_10.md | 27778 | `3b68d3890473` | verdict/pi | verdict/pi/_typeb_m_registration_2026_10_10.md | L |
| 1853 | sub | results/_u04_1_exemption_precondition_verification_2026_10_09.md | 21377 | `c072ffe6110e` | verdict/pi | verdict/pi/_u04_1_exemption_precondition_verification_2026_10_09.md | L |
| 1854 | sub | results/_u3_carrier_qid_verification_2026_10_11.md | 21572 | `6509ae68f778` | verdict/pi | verdict/pi/_u3_carrier_qid_verification_2026_10_11.md | L |
| 1855 | sub | results/_u5_fingerprint_relocation_erratum_2026_10_10.md | 24999 | `200c7e4c57cb` | verdict/kd | verdict/kd/_u5_fingerprint_relocation_erratum_2026_10_10.md | L |
| 1856 | sub | results/_u5b_citation_surface_revision_2026_10_10.md | 50079 | `5cc29c53a422` | verdict/kd | verdict/kd/_u5b_citation_surface_revision_2026_10_10.md | L |
| 1857 | sub | results/_u5b_p_counting_resolution_2026_10_10.md | 20086 | `e12e9d9a32c4` | verdict/judge | verdict/judge/_u5b_p_counting_resolution_2026_10_10.md | L |
| 1858 | sub | results/_u6_negative_delta_compatibility_2026_10_11.md | 20969 | `1846e917119f` | verdict/judge | verdict/judge/_u6_negative_delta_compatibility_2026_10_11.md | L |
| 1859 | sub | results/_u_cf_category_caliber_2026_10_10.md | 18976 | `73f181d76169` | verdict/kd | verdict/kd/_u_cf_category_caliber_2026_10_10.md | L |
| 1860 | sub | results/_u_cf_reclassification_2026_10_10.md | 25698 | `02f910e8795b` | verdict/kd | verdict/kd/_u_cf_reclassification_2026_10_10.md | L |
| 1861 | sub | results/_u_v04_01_criterion_scope_determination_2026_10_01.md | 27079 | `e82609024b59` | verdict/judge | verdict/judge/_u_v04_01_criterion_scope_determination_2026_10_01.md | L |
| 1862 | sub | results/_upload_execution_receipt_kimi_2026_09_26.md | 4191 | `b4ac31f917f3` | doc/letter | doc/letter/_upload_execution_receipt_kimi_2026_09_26.md | L |
| 1863 | sub | results/_upload_execution_receipt_kimi_2026_09_30.md | 4159 | `20e1f592ca61` | doc/letter | doc/letter/_upload_execution_receipt_kimi_2026_09_30.md | L |
| 1864 | sub | results/_upload_execution_receipt_kimi_2026_10_01.md | 4581 | `a9a9a1d19661` | doc/letter | doc/letter/_upload_execution_receipt_kimi_2026_10_01.md | L |
| 1865 | sub | results/_upload_guard_mirror_pair_2026_10_08.md | 23534 | `d923371cdbce` | verdict/kd | verdict/kd/_upload_guard_mirror_pair_2026_10_08.md | L |
| 1866 | sub | results/_uv04_field_completeness_fill_2026_10_01.md | 28735 | `eb9b8d185f44` | verdict/kd | verdict/kd/_uv04_field_completeness_fill_2026_10_01.md | L |
| 1867 | sub | results/_v5_r4_residual_merged_catalogue_2026_09_29.md | 102410 | `0c4bbd26ea55` | verdict/kd | verdict/kd/_v5_r4_residual_merged_catalogue_2026_09_29.md | L |
| 1868 | sub | results/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md | 14620 | `79bcff089f21` | verdict/kd | verdict/kd/_v5_v4_proposal_23item_merged_catalogue_2026_09_29.md | L |
| 1869 | sub | results/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md | 22185 | `ac0d6f19f06c` | verdict/kd | verdict/kd/_v5_v4_proposal_23item_merged_catalogue_sourceverify_2026_09_29.md | L |
| 1870 | sub | results/_vk_current_counting_face_2026_10_10.md | 24795 | `4d4e41c3eff5` | verdict/kd | verdict/kd/_vk_current_counting_face_2026_10_10.md | L |
| 1871 | sub | results/_vk_face_category_erratum_2026_10_11.md | 17373 | `67bf70301889` | verdict/kd | verdict/kd/_vk_face_category_erratum_2026_10_11.md | L |
| 1872 | sub | results/_vk_two_items_judgments_2026_10_09.md | 33399 | `82556d54726c` | verdict/kd | verdict/kd/_vk_two_items_judgments_2026_10_09.md | L |
| 1873 | sub | results/_wordlist_house_establishment_draft_2026_10_10.md | 38468 | `afa5eb53d216` | verdict/kd | verdict/kd/_wordlist_house_establishment_draft_2026_10_10.md | L |
| 1874 | sub | results/doc/document/_D05_DATA_RESCUE_NOTE_2026_09_18.md | 1181 | `120295a19655` | readout/final | readout/final/_D05_DATA_RESCUE_NOTE_2026_09_18.md | L |
| 1875 | sub | results/doc/document/_d1_backfill_event_id_prefix_proposal_2026_10_01.md | 14074 | `2636394df918` | verdict/kd | verdict/kd/_d1_backfill_event_id_prefix_proposal_2026_10_01.md | L |
| 1876 | sub | results/doc/document/_e6_j5_semantics_erratum_note_2026_10_10.md | 21166 | `b2db427147e2` | verdict/pi | verdict/pi/_e6_j5_semantics_erratum_note_2026_10_10.md | L |
| 1877 | sub | results/doc/document/_g4_controlled_reproduction_design_2026_10_09.md | 23675 | `b1c7c24926bb` | verdict/kd | verdict/kd/_g4_controlled_reproduction_design_2026_10_09.md | L |
| 1878 | sub | results/doc/document/_id_face_revision_sync_note_2026_10_10.md | 20690 | `5d6c473731c4` | verdict/pi | verdict/pi/_id_face_revision_sync_note_2026_10_10.md | L |
| 1879 | sub | results/doc/document/_naming_erratum_linestand_note_2026_10_01.md | 12137 | `38c8218d066b` | verdict/pi | verdict/pi/_naming_erratum_linestand_note_2026_10_01.md | L |
| 1880 | sub | results/doc/document/_p_d_v03_verification_report_20260917_163757.md | 9799 | `67aafb57a8ed` | doc/readme | doc/readme/_p_d_v03_verification_report_20260917_163757.md | L |
| 1881 | sub | results/doc/document/_pack_d_closeout_confirm_receipt_note_2026_10_01.md | 35223 | `15c18a28080f` | verdict/pi | verdict/pi/_pack_d_closeout_confirm_receipt_note_2026_10_01.md | L |
| 1882 | sub | results/doc/document/_pack_d_closeout_effectuation_note_2026_10_01.md | 27609 | `97a3573e2a2d` | verdict/pi | verdict/pi/_pack_d_closeout_effectuation_note_2026_10_01.md | L |
| 1883 | sub | results/doc/document/_pre_exec_report_kimi_2026_09_30.md | 5677 | `3e3ef9007a90` | doc/letter | doc/letter/_pre_exec_report_kimi_2026_09_30.md | L |
| 1884 | sub | results/doc/document/_pre_execution_report_kimi_2026_10_01.md | 6277 | `941e1a68b2df` | doc/letter | doc/letter/_pre_execution_report_kimi_2026_10_01.md | L |
| 1885 | sub | results/doc/document/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md | 7126 | `bb7ca9838150` | doc/readme | doc/readme/_pulled_back_P_B_DISTORTION_BOUND_V0_SPEC_2026_10_13.md | L |
| 1886 | sub | results/doc/document/_round56_b01_followup_disposition_plan_2026_10_10.md | 31004 | `857fb940a43c` | verdict/kd | verdict/kd/_round56_b01_followup_disposition_plan_2026_10_10.md | L |
| 1887 | sub | results/doc/document/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md | 8181 | `c72086990450` | verdict/pi | verdict/pi/_round56_idx_sc1_temp_deletion_deviation_note_2026_10_10.md | L |
| 1888 | sub | results/doc/document/_round56_pending_questions_compilation_supplement_note_2026_10_10.md | 29019 | `421c936f6ae8` | verdict/pi | verdict/pi/_round56_pending_questions_compilation_supplement_note_2026_10_10.md | L |
| 1889 | sub | results/doc/document/_round56_shortname_backfill_note_2026_10_10.md | 22195 | `bb2444cccd65` | verdict/pi | verdict/pi/_round56_shortname_backfill_note_2026_10_10.md | L |
| 1890 | sub | results/doc/document/_round56_th4_two_field_reporting_resolution_2026_10_10.md | 28233 | `71894a686e92` | verdict/pi | verdict/pi/_round56_th4_two_field_reporting_resolution_2026_10_10.md | L |
| 1891 | sub | results/doc/document/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md | 31692 | `c14489750416` | verdict/pi | verdict/pi/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md | L |
| 1892 | sub | results/doc/document/_skill_erratum_and_parent_success_note_2026_09_30.md | 24143 | `7a64949402d9` | verdict/pi | verdict/pi/_skill_erratum_and_parent_success_note_2026_09_30.md | L |
| 1893 | sub | results/doc/document/_thv3_15_parallel_seed_double_note_2026_10_11.md | 15569 | `3cd92287059e` | verdict/pi | verdict/pi/_thv3_15_parallel_seed_double_note_2026_10_11.md | L |
| 1894 | sub | results/doc/document/_unclosed_items_inventory_2026_10_08.md | 30219 | `b0e7c74e951e` | verdict/pi | verdict/pi/_unclosed_items_inventory_2026_10_08.md | L |
| 1895 | sub | results/evidence/register/_9model_merge_disposition_register_2026_10_09.md | 11651 | `455277298212` | verdict/pi | verdict/pi/_9model_merge_disposition_register_2026_10_09.md | L |
| 1896 | sub | results/evidence/register/_adendum_Q_deepseek_v4_pro_anchor_20260917_132049.json | 4003 | `ab5d9ae6e42a` | readout/final | readout/final/_adendum_Q_deepseek_v4_pro_anchor_20260917_132049.json | L |
| 1897 | sub | results/evidence/register/_archive_and_b6_inquiry_register_2026_10_08.md | 21163 | `1d08a780a715` | verdict/pi | verdict/pi/_archive_and_b6_inquiry_register_2026_10_08.md | L |
| 1898 | sub | results/evidence/register/_archive_ledger_rectification_register_2026_10_09.md | 20933 | `99359733eef1` | verdict/kd | verdict/kd/_archive_ledger_rectification_register_2026_10_09.md | L |
| 1899 | sub | results/evidence/register/_archive_moveout_register_2026_09_29.md | 13363 | `56639e57ac06` | verdict/pi | verdict/pi/_archive_moveout_register_2026_09_29.md | L |
| 1900 | sub | results/evidence/register/_b_coincidence_closeout_register_2026_10_10.md | 31451 | `51ce7b49c423` | verdict/kd | verdict/kd/_b_coincidence_closeout_register_2026_10_10.md | L |
| 1901 | sub | results/evidence/register/_backfill_rule_execution_register_2026_10_08.md | 27267 | `3a7f8e203b28` | verdict/pi | verdict/pi/_backfill_rule_execution_register_2026_10_08.md | L |
| 1902 | sub | results/evidence/register/_beta_formal_run_exec_register_2026_10_09.md | 16811 | `2e5f080eab6c` | verdict/pi | verdict/pi/_beta_formal_run_exec_register_2026_10_09.md | L |
| 1903 | sub | results/evidence/register/_c8_c2_disposition_register_2026_10_11.md | 30956 | `fb816c572779` | verdict/pi | verdict/pi/_c8_c2_disposition_register_2026_10_11.md | L |
| 1904 | sub | results/evidence/register/_charlie_delivery_register_2026_10_08.md | 10733 | `6f4bf31276f5` | verdict/pi | verdict/pi/_charlie_delivery_register_2026_10_08.md | L |
| 1905 | sub | results/evidence/register/_ci_degradation_binding_form_a_register_2026_10_09.md | 26104 | `424730b5123d` | verdict/kd | verdict/kd/_ci_degradation_binding_form_a_register_2026_10_09.md | L |
| 1906 | sub | results/evidence/register/_ci_four_items_effectiveness_register_2026_10_09.md | 29365 | `4ab2464a266e` | verdict/kd | verdict/kd/_ci_four_items_effectiveness_register_2026_10_09.md | L |
| 1907 | sub | results/evidence/register/_ci_three_items_effectivity_register_2026_10_09.md | 31488 | `2b7166a7d726` | verdict/kd | verdict/kd/_ci_three_items_effectivity_register_2026_10_09.md | L |
| 1908 | sub | results/evidence/register/_clearance_materials_register_2026_10_08.md | 45254 | `356eb1c53986` | verdict/pi | verdict/pi/_clearance_materials_register_2026_10_08.md | L |
| 1909 | sub | results/evidence/register/_clearance_round_1_register_2026_10_08.md | 13826 | `58fa92543338` | verdict/pi | verdict/pi/_clearance_round_1_register_2026_10_08.md | L |
| 1910 | sub | results/evidence/register/_closing_round_4_decisions_register_2026_10_08.md | 5322 | `771e37b4a25d` | verdict/pi | verdict/pi/_closing_round_4_decisions_register_2026_10_08.md | L |
| 1911 | sub | results/evidence/register/_closing_round_5_decisions_register_2026_10_08.md | 3282 | `5b08d34a05ba` | verdict/pi | verdict/pi/_closing_round_5_decisions_register_2026_10_08.md | L |
| 1912 | sub | results/evidence/register/_closing_round_6_decisions_register_2026_10_08.md | 3869 | `272cb570c78b` | verdict/pi | verdict/pi/_closing_round_6_decisions_register_2026_10_08.md | L |
| 1913 | sub | results/evidence/register/_closing_round_7_decisions_register_2026_10_09.md | 3206 | `d5976bfe23c6` | verdict/pi | verdict/pi/_closing_round_7_decisions_register_2026_10_09.md | L |
| 1914 | sub | results/evidence/register/_closing_round_9_decisions_register_2026_10_09.md | 2314 | `27118156a99a` | verdict/pi | verdict/pi/_closing_round_9_decisions_register_2026_10_09.md | L |
| 1915 | sub | results/evidence/register/_confirm_round_2026_10_01_register.md | 14500 | `23a97e340fdf` | verdict/pi | verdict/pi/_confirm_round_2026_10_01_register.md | L |
| 1916 | sub | results/evidence/register/_confirm_round_2_2026_10_01_register.md | 22327 | `817302144788` | verdict/pi | verdict/pi/_confirm_round_2_2026_10_01_register.md | L |
| 1917 | sub | results/evidence/register/_day_close_register_2026_10_01.md | 33115 | `6dbac1d1bcd6` | verdict/kd | verdict/kd/_day_close_register_2026_10_01.md | L |
| 1918 | sub | results/evidence/register/_deemphasis_verification_register_2026_10_08.md | 27322 | `3f806e44a13f` | verdict/pi | verdict/pi/_deemphasis_verification_register_2026_10_08.md | L |
| 1919 | sub | results/evidence/register/_e2_glm2_distill_side_receipt_register_2026_10_09.md | 11336 | `974124fc53f9` | verdict/pi | verdict/pi/_e2_glm2_distill_side_receipt_register_2026_10_09.md | L |
| 1920 | sub | results/evidence/register/_e6_th_v3_19_alignment_register_2026_10_10.md | 32582 | `622cebef2c9f` | verdict/pi | verdict/pi/_e6_th_v3_19_alignment_register_2026_10_10.md | L |
| 1921 | sub | results/evidence/register/_executor_prereg_docstring_correction_2026_10_11.md | 27721 | `f7f8328c49ba` | verdict/kd | verdict/kd/_executor_prereg_docstring_correction_2026_10_11.md | L |
| 1922 | sub | results/evidence/register/_executor_prereg_vs_impl_equivalence_2026_10_11.md | 20028 | `e84cec618659` | verdict/kd | verdict/kd/_executor_prereg_vs_impl_equivalence_2026_10_11.md | L |
| 1923 | sub | results/evidence/register/_exp08_s4_prompt_face_register_2026_10_10.md | 11929 | `83109ecf440e` | verdict/pi | verdict/pi/_exp08_s4_prompt_face_register_2026_10_10.md | L |
| 1924 | sub | results/evidence/register/_five_items_effectivity_register_2026_10_11.md | 43332 | `8affdca64b4b` | verdict/pi | verdict/pi/_five_items_effectivity_register_2026_10_11.md | L |
| 1925 | sub | results/evidence/register/_forgotten_items_quick_sweep_register_2026_10_01.md | 43735 | `91103473289a` | verdict/kd | verdict/kd/_forgotten_items_quick_sweep_register_2026_10_01.md | L |
| 1926 | sub | results/evidence/register/_forgotten_recovery_register_2026_09_29.md | 47494 | `d78be896bcb6` | verdict/kd | verdict/kd/_forgotten_recovery_register_2026_09_29.md | L |
| 1927 | sub | results/evidence/register/_fp3_anchor_and_krj_restrament_register_2026_10_11.md | 32886 | `b7c060ab2d49` | verdict/kd | verdict/kd/_fp3_anchor_and_krj_restrament_register_2026_10_11.md | L |
| 1928 | sub | results/evidence/register/_freeze_receipt_2026_10_01_q1.md | 698 | `9b7101bc09bd` | readout/final | readout/final/_freeze_receipt_2026_10_01_q1.md | L |
| 1929 | sub | results/evidence/register/_full_tidy_inventory_register_2026_09_30.md | 27687 | `33f68dbfbd6f` | verdict/pi | verdict/pi/_full_tidy_inventory_register_2026_09_30.md | L |
| 1930 | sub | results/evidence/register/_g11_krj4_effectivity_register_2026_10_11.md | 39870 | `17168119eccc` | verdict/pi | verdict/pi/_g11_krj4_effectivity_register_2026_10_11.md | L |
| 1931 | sub | results/evidence/register/_g4_reproduction_execution_register_2026_10_09.md | 20414 | `4daaf68cbf0e` | verdict/pi | verdict/pi/_g4_reproduction_execution_register_2026_10_09.md | L |
| 1932 | sub | results/evidence/register/_g5_rejudgment_face_prereg_2026_10_10.md | 35097 | `04495ef4b343` | verdict/kd | verdict/kd/_g5_rejudgment_face_prereg_2026_10_10.md | L |
| 1933 | sub | results/evidence/register/_g9_read_b_effectivity_register_2026_10_11.md | 29649 | `f5d601a0602a` | verdict/pi | verdict/pi/_g9_read_b_effectivity_register_2026_10_11.md | L |
| 1934 | sub | results/evidence/register/_gate_one_declared_adoption_register_2026_10_11.md | 12923 | `3a965362d4f4` | verdict/pi | verdict/pi/_gate_one_declared_adoption_register_2026_10_11.md | L |
| 1935 | sub | results/evidence/register/_ge01_H_enumeration_and_lock_2026_10_13.md | 28522 | `4c5860342d7f` | verdict/pi | verdict/pi/_ge01_H_enumeration_and_lock_2026_10_13.md | L |
| 1936 | sub | results/evidence/register/_ge01_H_enumeration_round2_2026_10_13.md | 37191 | `ff2afb7a634b` | verdict/pi | verdict/pi/_ge01_H_enumeration_round2_2026_10_13.md | L |
| 1937 | sub | results/evidence/register/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md | 17885 | `deea2ccb2643` | verdict/kd | verdict/kd/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md | L |
| 1938 | sub | results/evidence/register/_itemH_nonclade_and_hangings_register_2026_10_12.md | 13223 | `37ea7f65a8d6` | verdict/pi | verdict/pi/_itemH_nonclade_and_hangings_register_2026_10_12.md | L |
| 1939 | sub | results/evidence/register/_j2_kj4_disposition_register_2026_10_11.md | 34112 | `c1a4ff1b96e5` | verdict/pi | verdict/pi/_j2_kj4_disposition_register_2026_10_11.md | L |
| 1940 | sub | results/evidence/register/_k_cf_4_effectivity_register_2026_10_09.md | 35872 | `edc6a548e3ca` | verdict/pi | verdict/pi/_k_cf_4_effectivity_register_2026_10_09.md | L |
| 1941 | sub | results/evidence/register/_k_v3s_3_4_lock_freeze_2026_10_08.md | 16973 | `c64865c32761` | verdict/kd | verdict/kd/_k_v3s_3_4_lock_freeze_2026_10_08.md | L |
| 1942 | sub | results/evidence/register/_kickoff_decisions_register_2026_10_08.md | 16388 | `6ee5d2b8323c` | verdict/kd | verdict/kd/_kickoff_decisions_register_2026_10_08.md | L |
| 1943 | sub | results/evidence/register/_kj1_eps_ls_effectivity_register_2026_10_11.md | 62344 | `809edb4bb1cc` | verdict/kd | verdict/kd/_kj1_eps_ls_effectivity_register_2026_10_11.md | L |
| 1944 | sub | results/evidence/register/_l3_deferred_items_immediate_disposition_register_2026_10_13.md | 33958 | `92e410f45256` | verdict/pi | verdict/pi/_l3_deferred_items_immediate_disposition_register_2026_10_13.md | L |
| 1945 | sub | results/evidence/register/_m3_glm29_adoption_register_2026_10_13.md | 23309 | `6aff3c459ca0` | verdict/pi | verdict/pi/_m3_glm29_adoption_register_2026_10_13.md | L |
| 1946 | sub | results/evidence/register/_m5_rejudgment_and_dual_value_register_2026_10_14.md | 16093 | `4b72fbe08ce2` | verdict/pi | verdict/pi/_m5_rejudgment_and_dual_value_register_2026_10_14.md | L |
| 1947 | sub | results/evidence/register/_mini_round_3_decisions_register_2026_10_01.md | 44308 | `bff06d3b3f97` | verdict/pi | verdict/pi/_mini_round_3_decisions_register_2026_10_01.md | L |
| 1948 | sub | results/evidence/register/_mini_round_4_decisions_register_2026_10_01.md | 37804 | `0f2d1afcc793` | verdict/pi | verdict/pi/_mini_round_4_decisions_register_2026_10_01.md | L |
| 1949 | sub | results/evidence/register/_mini_round_5_decisions_register_2026_10_01.md | 53125 | `eb40a1b9f4e1` | verdict/pi | verdict/pi/_mini_round_5_decisions_register_2026_10_01.md | L |
| 1950 | sub | results/evidence/register/_mini_round_6_7_settlement_register_2026_10_01.md | 68053 | `3cb2dfe3c293` | verdict/pi | verdict/pi/_mini_round_6_7_settlement_register_2026_10_01.md | L |
| 1951 | sub | results/evidence/register/_mq_rollout_v7_effect_register_2026_10_14.md | 15538 | `a709ff7b48de` | verdict/pi | verdict/pi/_mq_rollout_v7_effect_register_2026_10_14.md | L |
| 1952 | sub | results/evidence/register/_mq_rollout_v8_effect_register_2026_10_14.md | 14621 | `5f32931507bb` | verdict/pi | verdict/pi/_mq_rollout_v8_effect_register_2026_10_14.md | L |
| 1953 | sub | results/evidence/register/_p3_candidate3_supplement_register_2026_10_13.md | 22448 | `b7f725de2d95` | verdict/pi | verdict/pi/_p3_candidate3_supplement_register_2026_10_13.md | L |
| 1954 | sub | results/evidence/register/_p_s4_1_revision_register_2026_10_09.md | 29961 | `ad5c76111570` | verdict/kd | verdict/kd/_p_s4_1_revision_register_2026_10_09.md | L |
| 1955 | sub | results/evidence/register/_pack_d_closeout_register_2026_10_01.md | 62012 | `0f1f94df75ba` | verdict/pi | verdict/pi/_pack_d_closeout_register_2026_10_01.md | L |
| 1956 | sub | results/evidence/register/_proxy_signoff_execution_register_2026_10_01.md | 20766 | `b6e5e15b70e5` | verdict/pi | verdict/pi/_proxy_signoff_execution_register_2026_10_01.md | L |
| 1957 | sub | results/evidence/register/_q4_legacy_disposal_register_2026_10_01.md | 13336 | `a8763c406d4f` | verdict/pi | verdict/pi/_q4_legacy_disposal_register_2026_10_01.md | L |
| 1958 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md | 84127 | `6c18d336e018` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_10_2026_10_10.md | L |
| 1959 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md | 55341 | `52c97d1c11e9` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_11_2026_10_10.md | L |
| 1960 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md | 121137 | `1ff6919967a7` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_12_2026_10_10.md | L |
| 1961 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md | 114253 | `43e0b642f8b2` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_13_2026_10_11.md | L |
| 1962 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md | 54883 | `79bc4bfe38a5` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_14_2026_10_11.md | L |
| 1963 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md | 44698 | `3654c41eda64` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_15_2026_10_11.md | L |
| 1964 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md | 52602 | `1fb8eac82781` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md | L |
| 1965 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md | 17517 | `a651f76a6547` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md | L |
| 1966 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md | 50790 | `29b30d845841` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md | L |
| 1967 | sub | results/evidence/register/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md | 84422 | `b6c0b4f29152` | verdict/pi | verdict/pi/_questionnaire_cards_intake_register_supplement_9_2026_10_10.md | L |
| 1968 | sub | results/evidence/register/_readme_proper_batch_recheck_register_2026_09_30.md | 20781 | `2e530923457e` | verdict/pi | verdict/pi/_readme_proper_batch_recheck_register_2026_09_30.md | L |
| 1969 | sub | results/evidence/register/_receipt_disposition_register_2026_10_08.md | 23050 | `a79c3b82ee01` | verdict/pi | verdict/pi/_receipt_disposition_register_2026_10_08.md | L |
| 1970 | sub | results/evidence/register/_register3_bytes_erratum_2026_10_11.md | 13294 | `f9f6805a7b76` | verdict/kd | verdict/kd/_register3_bytes_erratum_2026_10_11.md | L |
| 1971 | sub | results/evidence/register/_round19_followup_round21_22_approvals_effect_register_2026_10_10.md | 54850 | `0c8dba07dd1e` | verdict/kd | verdict/kd/_round19_followup_round21_22_approvals_effect_register_2026_10_10.md | L |
| 1972 | sub | results/evidence/register/_round20_approvals_effect_register_2026_10_10.md | 27711 | `29d737c59e8b` | verdict/kd | verdict/kd/_round20_approvals_effect_register_2026_10_10.md | L |
| 1973 | sub | results/evidence/register/_round23_26_threshold_review_effect_register_2026_10_10.md | 47297 | `9b0c62765576` | verdict/kd | verdict/kd/_round23_26_threshold_review_effect_register_2026_10_10.md | L |
| 1974 | sub | results/evidence/register/_round27_34_approvals_effect_register_2026_10_10.md | 73226 | `d0bc0b1a9ae0` | verdict/kd | verdict/kd/_round27_34_approvals_effect_register_2026_10_10.md | L |
| 1975 | sub | results/evidence/register/_round45_dispositions_effect_register_2026_10_10.md | 19803 | `d66a1076952a` | verdict/pi | verdict/pi/_round45_dispositions_effect_register_2026_10_10.md | L |
| 1976 | sub | results/evidence/register/_round51_effectivity_register_2026_10_10.md | 27070 | `b8b0c52296b2` | verdict/pi | verdict/pi/_round51_effectivity_register_2026_10_10.md | L |
| 1977 | sub | results/evidence/register/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md | 21788 | `e861c7bc19ad` | verdict/pi | verdict/pi/_round52_e6b_caliber_naming_effectivity_register_2026_10_10.md | L |
| 1978 | sub | results/evidence/register/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md | 45351 | `debd88fc150c` | verdict/pi | verdict/pi/_round52_s4_e4b_ad5_type_effectivity_register_2026_10_10.md | L |
| 1979 | sub | results/evidence/register/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md | 25637 | `b27814792394` | verdict/kd | verdict/kd/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md | L |
| 1980 | sub | results/evidence/register/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md | 20023 | `4c3a6dc0070d` | verdict/pi | verdict/pi/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md | L |
| 1981 | sub | results/evidence/register/_round54_g5_dispositions_register_2026_10_10.md | 39977 | `afc67818bb85` | verdict/pi | verdict/pi/_round54_g5_dispositions_register_2026_10_10.md | L |
| 1982 | sub | results/evidence/register/_round55_dispositions_register_2026_10_10.md | 34913 | `002fa0a9a5e4` | verdict/pi | verdict/pi/_round55_dispositions_register_2026_10_10.md | L |
| 1983 | sub | results/evidence/register/_round56_ad8fix_effectivity_register_2026_10_10.md | 16553 | `2e7f86314428` | verdict/pi | verdict/pi/_round56_ad8fix_effectivity_register_2026_10_10.md | L |
| 1984 | sub | results/evidence/register/_round56_direct_adoptions_register_2026_10_10.md | 43240 | `e3c56c5d0a97` | verdict/pi | verdict/pi/_round56_direct_adoptions_register_2026_10_10.md | L |
| 1985 | sub | results/evidence/register/_round56_direct_adoptions_register_2_2026_10_10.md | 26690 | `f8e0fa28c067` | verdict/pi | verdict/pi/_round56_direct_adoptions_register_2_2026_10_10.md | L |
| 1986 | sub | results/evidence/register/_round56_g2_enable_and_v1_rule_register_2026_10_10.md | 34181 | `936f551f0fd3` | verdict/pi | verdict/pi/_round56_g2_enable_and_v1_rule_register_2026_10_10.md | L |
| 1987 | sub | results/evidence/register/_round56_n10_erratum_register_2026_10_10.md | 20321 | `599d0450434e` | verdict/pi | verdict/pi/_round56_n10_erratum_register_2026_10_10.md | L |
| 1988 | sub | results/evidence/register/_round56_review_effectivity_register_2026_10_10.md | 49013 | `da6b55162e50` | verdict/pi | verdict/pi/_round56_review_effectivity_register_2026_10_10.md | L |
| 1989 | sub | results/evidence/register/_round56_review_effectivity_register_3_2026_10_10.md | 77181 | `84ed13256250` | verdict/pi | verdict/pi/_round56_review_effectivity_register_3_2026_10_10.md | L |
| 1990 | sub | results/evidence/register/_round56_review_effectivity_register_4_2026_10_11.md | 46908 | `ee31bb8a94fe` | verdict/pi | verdict/pi/_round56_review_effectivity_register_4_2026_10_11.md | L |
| 1991 | sub | results/evidence/register/_round56_review_effectivity_register_5_2026_10_11.md | 67613 | `5deba7d27bb1` | verdict/pi | verdict/pi/_round56_review_effectivity_register_5_2026_10_11.md | L |
| 1992 | sub | results/evidence/register/_round56_review_effectivity_register_6_2026_10_11.md | 58478 | `2f3255ea344f` | verdict/pi | verdict/pi/_round56_review_effectivity_register_6_2026_10_11.md | L |
| 1993 | sub | results/evidence/register/_round56_terminal_boundary_effectivity_register_2026_10_10.md | 35878 | `d5bf826278cb` | verdict/pi | verdict/pi/_round56_terminal_boundary_effectivity_register_2026_10_10.md | L |
| 1994 | sub | results/evidence/register/_round56_th3_coverage_line_effectivity_register_2026_10_10.md | 28378 | `6794fb09ce7e` | verdict/pi | verdict/pi/_round56_th3_coverage_line_effectivity_register_2026_10_10.md | L |
| 1995 | sub | results/evidence/register/_round56_typeb_backfill_register_2026_10_10.md | 40253 | `607ded06d840` | verdict/pi | verdict/pi/_round56_typeb_backfill_register_2026_10_10.md | L |
| 1996 | sub | results/evidence/register/_round56_typeb_implementation_register_2026_10_10.md | 26367 | `c296a7833a70` | verdict/pi | verdict/pi/_round56_typeb_implementation_register_2026_10_10.md | L |
| 1997 | sub | results/evidence/register/_round56a_dispositions_register_2026_10_10.md | 50365 | `d8980cfae7f7` | verdict/pi | verdict/pi/_round56a_dispositions_register_2026_10_10.md | L |
| 1998 | sub | results/evidence/register/_round56r8_dispositions_register_2026_10_10.md | 46135 | `cfb08d0e15f4` | verdict/pi | verdict/pi/_round56r8_dispositions_register_2026_10_10.md | L |
| 1999 | sub | results/evidence/register/_round56r9r10_dispositions_register_2026_10_10.md | 49754 | `0eb408ae60f5` | verdict/pi | verdict/pi/_round56r9r10_dispositions_register_2026_10_10.md | L |
| 2000 | sub | results/evidence/register/_s4_chain_clearance_register_2026_10_09.md | 2684 | `eda3d304d381` | verdict/pi | verdict/pi/_s4_chain_clearance_register_2026_10_09.md | L |
| 2001 | sub | results/evidence/register/_s4_dkb_backfill_register_2026_10_10.md | 25591 | `3a992c3fe235` | verdict/pi | verdict/pi/_s4_dkb_backfill_register_2026_10_10.md | L |
| 2002 | sub | results/evidence/register/_s4_heldout_sampling_seed42_items_register_2026_10_09.md | 34689 | `73a02ac5937d` | verdict/pi | verdict/pi/_s4_heldout_sampling_seed42_items_register_2026_10_09.md | L |
| 2003 | sub | results/evidence/register/_s4_heldout_sampling_seed42_register_2026_10_09.md | 37615 | `2a2ad5c2e29f` | verdict/pi | verdict/pi/_s4_heldout_sampling_seed42_register_2026_10_09.md | L |
| 2004 | sub | results/evidence/register/_s4_reading_surface_and_authority_register_2026_10_09.md | 34405 | `0148b5271154` | verdict/pi | verdict/pi/_s4_reading_surface_and_authority_register_2026_10_09.md | L |
| 2005 | sub | results/evidence/register/_s4_revision_effectiveness_register_2026_10_09.md | 32820 | `356fe8509669` | verdict/kd | verdict/kd/_s4_revision_effectiveness_register_2026_10_09.md | L |
| 2006 | sub | results/evidence/register/_s4_tree_prereg_revision_2026_10_10.md | 30382 | `037140972829` | verdict/kd | verdict/kd/_s4_tree_prereg_revision_2026_10_10.md | L |
| 2007 | sub | results/evidence/register/_s4_v31_displacement_register_face2_2026_10_10.md | 17736 | `b6ce4a79116e` | verdict/pi | verdict/pi/_s4_v31_displacement_register_face2_2026_10_10.md | L |
| 2008 | sub | results/evidence/register/_s5prime_double_lim_a_and_item_registers_2026_10_11.md | 58378 | `9a62fb2a6956` | verdict/pi | verdict/pi/_s5prime_double_lim_a_and_item_registers_2026_10_11.md | L |
| 2009 | sub | results/evidence/register/_s5prime_lim_a_and_item_registers_2026_10_11.md | 47225 | `fa74831fa0ad` | verdict/pi | verdict/pi/_s5prime_lim_a_and_item_registers_2026_10_11.md | L |
| 2010 | sub | results/evidence/register/_seven_gap_closures_adoption_register_2026_10_11.md | 11960 | `ac3c41663f84` | verdict/pi | verdict/pi/_seven_gap_closures_adoption_register_2026_10_11.md | L |
| 2011 | sub | results/evidence/register/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md | 30771 | `16861e71305f` | verdict/pi | verdict/pi/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md | L |
| 2012 | sub | results/evidence/register/_stage1_tail_caliber_unification_register_2026_10_11.md | 41140 | `d486ec491e8e` | verdict/kd | verdict/kd/_stage1_tail_caliber_unification_register_2026_10_11.md | L |
| 2013 | sub | results/evidence/register/_stage3_open_and_mandate_register_2026_10_12.md | 13865 | `1b0a109a7914` | verdict/pi | verdict/pi/_stage3_open_and_mandate_register_2026_10_12.md | L |
| 2014 | sub | results/evidence/register/_sub_artifact_ledger_history_r5_2026_10_01.md | 35845 | `372a53b9e832` | verdict/pi | verdict/pi/_sub_artifact_ledger_history_r5_2026_10_01.md | L |
| 2015 | sub | results/evidence/register/_sub_transfer_execution_register_2026_10_01.md | 13377 | `c41013a975e0` | verdict/pi | verdict/pi/_sub_transfer_execution_register_2026_10_01.md | L |
| 2016 | sub | results/evidence/register/_sub_transfer_wave2_register_2026_10_01.md | 14286 | `265b03ea493a` | verdict/pi | verdict/pi/_sub_transfer_wave2_register_2026_10_01.md | L |
| 2017 | sub | results/evidence/register/_sub_transfer_wave3_register_2026_10_01.md | 14419 | `cd80b993f497` | verdict/pi | verdict/pi/_sub_transfer_wave3_register_2026_10_01.md | L |
| 2018 | sub | results/evidence/register/_t1_exp2_exec_register_2026_10_09.md | 18597 | `3a08dcfa8c7f` | verdict/pi | verdict/pi/_t1_exp2_exec_register_2026_10_09.md | L |
| 2019 | sub | results/evidence/register/_theory_boundary_clone_sync_register_2026_10_09.md | 17528 | `1f9fd007649c` | verdict/pi | verdict/pi/_theory_boundary_clone_sync_register_2026_10_09.md | L |
| 2020 | sub | results/evidence/register/_three_state_standard_repeal_register_2026_10_10.md | 18364 | `8503708c73bf` | verdict/kd | verdict/kd/_three_state_standard_repeal_register_2026_10_10.md | L |
| 2021 | sub | results/evidence/register/_tidy_round2_archive_transfer_register_2026_09_30.md | 27641 | `1c1365f23c92` | verdict/pi | verdict/pi/_tidy_round2_archive_transfer_register_2026_09_30.md | L |
| 2022 | sub | results/evidence/register/_tmp_disposal_register_2026_10_10.md | 20812 | `e0f6b744e826` | verdict/pi | verdict/pi/_tmp_disposal_register_2026_10_10.md | L |
| 2023 | sub | results/evidence/register/_u11_execution_register_2026_10_09.md | 24549 | `8bc087a16f5a` | verdict/pi | verdict/pi/_u11_execution_register_2026_10_09.md | L |
| 2024 | sub | results/evidence/register/_u2u3_effectivity_register_2026_10_10.md | 27192 | `b00b87cec825` | verdict/pi | verdict/pi/_u2u3_effectivity_register_2026_10_10.md | L |
| 2025 | sub | results/evidence/register/_u_closure_execution_register_2026_10_09.md | 12781 | `cbf0c9503284` | verdict/pi | verdict/pi/_u_closure_execution_register_2026_10_09.md | L |
| 2026 | sub | results/evidence/register/_upload_ledger_kimi_2026_09_30.json | 218279 | `b17cb8aae62d` | readout/final | readout/final/_upload_ledger_kimi_2026_09_30.json | L |
| 2027 | sub | results/evidence/register/_upload_ledger_kimi_2026_10_01.json | 43275 | `79a0fb18683b` | readout/final | readout/final/_upload_ledger_kimi_2026_10_01.json | L |
| 2028 | sub | results/evidence/register/_v3_02_ethard_execution_register_2026_10_09.md | 22007 | `23457f5ce432` | verdict/pi | verdict/pi/_v3_02_ethard_execution_register_2026_10_09.md | L |
| 2029 | sub | results/evidence/register/_v3_02_override_register_2026_10_09.md | 36245 | `c5441e186c3f` | verdict/kd | verdict/kd/_v3_02_override_register_2026_10_09.md | L |
| 2030 | sub | results/evidence/register/_v3_recheck_prereg_v1p2_2026_09_29.md | 25854 | `a667a5f69b7a` | verdict/kd | verdict/kd/_v3_recheck_prereg_v1p2_2026_09_29.md | L |
| 2031 | sub | results/evidence/register/_v4_closeout_bucket_register_2026_10_01.md | 41943 | `99355c24a03b` | verdict/pi | verdict/pi/_v4_closeout_bucket_register_2026_10_01.md | L |
| 2032 | sub | results/evidence/register/_v4_gamma_r1_prereg_2026_09_28.md | 33489 | `c9da8678cf2b` | verdict/kd | verdict/kd/_v4_gamma_r1_prereg_2026_09_28.md | L |
| 2033 | sub | results/evidence/register/_v4_gamma_r1_prereg_v2_stop_2026_09_28.md | 17999 | `9349e2fdb537` | verdict/kd | verdict/kd/_v4_gamma_r1_prereg_v2_stop_2026_09_28.md | L |
| 2034 | sub | results/evidence/register/_v4_item04_closeout_prereg_2026_09_28.md | 26719 | `176e2b1c95ae` | verdict/kd | verdict/kd/_v4_item04_closeout_prereg_2026_09_28.md | L |
| 2035 | sub | results/evidence/register/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md | 21309 | `843e42ef4d2a` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md | L |
| 2036 | sub | results/evidence/register/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md | 20751 | `443efb39804a` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md | L |
| 2037 | sub | results/evidence/register/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md | 14234 | `79936b630015` | verdict/kd | verdict/kd/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md | L |
| 2038 | sub | results/evidence/register/_v5_a_system_default_register_2026_09_28.md | 19892 | `8c22796a42f5` | verdict/kd | verdict/kd/_v5_a_system_default_register_2026_09_28.md | L |
| 2039 | sub | results/evidence/register/_v5_b14_3_v1_4_prereg_2026_09_29.md | 20045 | `0f1665e7056f` | verdict/kd | verdict/kd/_v5_b14_3_v1_4_prereg_2026_09_29.md | L |
| 2040 | sub | results/evidence/register/_v5_b14_4_v1_3_prereg_2026_09_29.md | 20043 | `ae474bf48c62` | verdict/kd | verdict/kd/_v5_b14_4_v1_3_prereg_2026_09_29.md | L |
| 2041 | sub | results/evidence/register/_v5_b17_fault_register_2026_09_29.md | 18129 | `48cb0ab5f317` | verdict/kd | verdict/kd/_v5_b17_fault_register_2026_09_29.md | L |
| 2042 | sub | results/evidence/register/_v5_b17_recheck12_register_2026_09_29.md | 19981 | `73242a890be9` | verdict/pi | verdict/pi/_v5_b17_recheck12_register_2026_09_29.md | L |
| 2043 | sub | results/evidence/register/_v5_b22_r07_four_cond_prereg_2026_09_29.md | 23151 | `ceea8f4534fb` | verdict/kd | verdict/kd/_v5_b22_r07_four_cond_prereg_2026_09_29.md | L |
| 2044 | sub | results/evidence/register/_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md | 18271 | `c514b321fe10` | verdict/kd | verdict/kd/_v5_clearance_mr10_pb_reembed_prereg_2026_09_29.md | L |
| 2045 | sub | results/evidence/register/_v5_clearance_pending_backlog_register_2026_09_29.md | 32369 | `1132072288de` | verdict/pi | verdict/pi/_v5_clearance_pending_backlog_register_2026_09_29.md | L |
| 2046 | sub | results/evidence/register/_v5_clearance_readme_c5_register_2026_09_29.md | 8730 | `ababdaa392ca` | verdict/pi | verdict/pi/_v5_clearance_readme_c5_register_2026_09_29.md | L |
| 2047 | sub | results/evidence/register/_v5_clearance_round11_register_2026_09_29.md | 59923 | `2e5e6f8b328e` | verdict/pi | verdict/pi/_v5_clearance_round11_register_2026_09_29.md | L |
| 2048 | sub | results/evidence/register/_v5_clearance_round12_14_register_2026_09_29.md | 75131 | `13d741979ebb` | verdict/pi | verdict/pi/_v5_clearance_round12_14_register_2026_09_29.md | L |
| 2049 | sub | results/evidence/register/_v5_clearance_round15_18_register_2026_09_29.md | 99989 | `3a3c9c734bf9` | verdict/pi | verdict/pi/_v5_clearance_round15_18_register_2026_09_29.md | L |
| 2050 | sub | results/evidence/register/_v5_clearance_round1_b19_register_2026_09_29.md | 28556 | `b69ec2ddc9be` | verdict/kd | verdict/kd/_v5_clearance_round1_b19_register_2026_09_29.md | L |
| 2051 | sub | results/evidence/register/_v5_clearance_round2_3_register_2026_09_29.md | 37340 | `32ca90e63a56` | verdict/kd | verdict/kd/_v5_clearance_round2_3_register_2026_09_29.md | L |
| 2052 | sub | results/evidence/register/_v5_clearance_round4_5_register_2026_09_29.md | 52782 | `9d381fab5f46` | verdict/kd | verdict/kd/_v5_clearance_round4_5_register_2026_09_29.md | L |
| 2053 | sub | results/evidence/register/_v5_clearance_round6_register_2026_09_29.md | 38248 | `68fe5b397df3` | verdict/pi | verdict/pi/_v5_clearance_round6_register_2026_09_29.md | L |
| 2054 | sub | results/evidence/register/_v5_clearance_round7_8_register_2026_09_29.md | 63311 | `60cdeef91d4a` | verdict/pi | verdict/pi/_v5_clearance_round7_8_register_2026_09_29.md | L |
| 2055 | sub | results/evidence/register/_v5_clearance_round9_10_register_2026_09_29.md | 68512 | `428e0857ebb7` | verdict/pi | verdict/pi/_v5_clearance_round9_10_register_2026_09_29.md | L |
| 2056 | sub | results/evidence/register/_v5_closing_register_r2_2026_09_28.md | 25446 | `1094edb6e8c0` | verdict/kd | verdict/kd/_v5_closing_register_r2_2026_09_28.md | L |
| 2057 | sub | results/evidence/register/_v5_confirm_b10_decisions_register_2026_09_29.md | 13282 | `67ea81a2e6d9` | verdict/kd | verdict/kd/_v5_confirm_b10_decisions_register_2026_09_29.md | L |
| 2058 | sub | results/evidence/register/_v5_confirm_b12_decisions_register_2026_09_29.md | 15898 | `db0d6e56a497` | verdict/kd | verdict/kd/_v5_confirm_b12_decisions_register_2026_09_29.md | L |
| 2059 | sub | results/evidence/register/_v5_confirm_b13_b22_anchor_verify_2026_09_29.md | 16393 | `a0c2d1d5fe6b` | verdict/kd | verdict/kd/_v5_confirm_b13_b22_anchor_verify_2026_09_29.md | L |
| 2060 | sub | results/evidence/register/_v5_confirm_b13_decisions_register_2026_09_29.md | 33086 | `c7ca4fbecc8b` | verdict/kd | verdict/kd/_v5_confirm_b13_decisions_register_2026_09_29.md | L |
| 2061 | sub | results/evidence/register/_v5_confirm_b16_b17_decisions_register_2026_09_29.md | 29624 | `8e36a3e4c6ff` | verdict/kd | verdict/kd/_v5_confirm_b16_b17_decisions_register_2026_09_29.md | L |
| 2062 | sub | results/evidence/register/_v5_confirm_b18_b19_decisions_register_2026_09_29.md | 21072 | `ae160194878e` | verdict/kd | verdict/kd/_v5_confirm_b18_b19_decisions_register_2026_09_29.md | L |
| 2063 | sub | results/evidence/register/_v5_confirm_b1_decisions_register_2026_09_29.md | 28469 | `62ca213bb56c` | verdict/pi | verdict/pi/_v5_confirm_b1_decisions_register_2026_09_29.md | L |
| 2064 | sub | results/evidence/register/_v5_confirm_b20_b22_decisions_register_2026_09_29.md | 24883 | `fccaac464565` | verdict/kd | verdict/kd/_v5_confirm_b20_b22_decisions_register_2026_09_29.md | L |
| 2065 | sub | results/evidence/register/_v5_confirm_b2_decisions_register_2026_09_29.md | 28383 | `63ded68919df` | verdict/pi | verdict/pi/_v5_confirm_b2_decisions_register_2026_09_29.md | L |
| 2066 | sub | results/evidence/register/_v5_confirm_b3_decisions_register_2026_09_29.md | 34015 | `4dbb11c219fc` | verdict/pi | verdict/pi/_v5_confirm_b3_decisions_register_2026_09_29.md | L |
| 2067 | sub | results/evidence/register/_v5_confirm_b4_decisions_register_2026_09_29.md | 43498 | `4d02f9df594e` | verdict/pi | verdict/pi/_v5_confirm_b4_decisions_register_2026_09_29.md | L |
| 2068 | sub | results/evidence/register/_v5_confirm_b8_decisions_register_2026_09_29.md | 15106 | `6862659ff900` | verdict/kd | verdict/kd/_v5_confirm_b8_decisions_register_2026_09_29.md | L |
| 2069 | sub | results/evidence/register/_v5_gt33_attrib_fill_prereg_2026_09_29.md | 36984 | `48742d6cbd03` | verdict/kd | verdict/kd/_v5_gt33_attrib_fill_prereg_2026_09_29.md | L |
| 2070 | sub | results/evidence/register/_v5_item05_prereg_2026_09_28.md | 19115 | `567f0f177699` | verdict/kd | verdict/kd/_v5_item05_prereg_2026_09_28.md | L |
| 2071 | sub | results/evidence/register/_v5_item21_rerun_conditions_prereg_2026_09_28.md | 31429 | `4185bdad6df5` | verdict/kd | verdict/kd/_v5_item21_rerun_conditions_prereg_2026_09_28.md | L |
| 2072 | sub | results/evidence/register/_v5_item36_prereg_2026_09_28.md | 18141 | `7f42d5ee131c` | verdict/kd | verdict/kd/_v5_item36_prereg_2026_09_28.md | L |
| 2073 | sub | results/evidence/register/_v5_pl2_fourband_prereg_2026_09_29.md | 29253 | `d5fdb89582fd` | verdict/kd | verdict/kd/_v5_pl2_fourband_prereg_2026_09_29.md | L |
| 2074 | sub | results/evidence/register/_v5_prereg_chain_activation_register_2026_09_28.md | 27047 | `3cc05f8cbd1a` | verdict/kd | verdict/kd/_v5_prereg_chain_activation_register_2026_09_28.md | L |
| 2075 | sub | results/evidence/register/_v5_prereg_chain_status_annotation_2026_09_28.md | 23857 | `cb4104938cc8` | verdict/kd | verdict/kd/_v5_prereg_chain_status_annotation_2026_09_28.md | L |
| 2076 | sub | results/evidence/register/_v5_sub_artifact_ledger_history_r1_2026_09_29.md | 48539 | `535b3c2ad102` | verdict/kd | verdict/kd/_v5_sub_artifact_ledger_history_r1_2026_09_29.md | L |
| 2077 | sub | results/evidence/register/_v5_sub_artifact_ledger_history_r2_2026_09_29.md | 150957 | `5ff7784db145` | verdict/kd | verdict/kd/_v5_sub_artifact_ledger_history_r2_2026_09_29.md | L |
| 2078 | sub | results/evidence/register/_v5_sub_artifact_ledger_history_r3_2026_09_29.md | 128760 | `e04a46b02d13` | verdict/kd | verdict/kd/_v5_sub_artifact_ledger_history_r3_2026_09_29.md | L |
| 2079 | sub | results/evidence/register/_v5_sub_artifact_ledger_history_r4_2026_09_29.md | 603599 | `b6b8be476a73` | verdict/pi | verdict/pi/_v5_sub_artifact_ledger_history_r4_2026_09_29.md | L |
| 2080 | sub | results/evidence/register/_v5_t1_decisions_register_2026_09_29.md | 31330 | `7dd7dd3fb721` | verdict/pi | verdict/pi/_v5_t1_decisions_register_2026_09_29.md | L |
| 2081 | sub | results/evidence/register/_v5_v3deg_prereg_activation_register_2026_09_29.md | 24370 | `e587da3b4cf8` | verdict/kd | verdict/kd/_v5_v3deg_prereg_activation_register_2026_09_29.md | L |
| 2082 | sub | results/evidence/register/_w1_stage2_premise_stale_register_2026_10_14.md | 8326 | `a7e14145e1c8` | verdict/pi | verdict/pi/_w1_stage2_premise_stale_register_2026_10_14.md | L |
| 2083 | sub | results/manifest_large_files.md | 3440 | `e0dc7a8e4c75` | doc/paper | doc/paper/manifest_large_files.md | L |
| 2084 | sub | results/quizbank_v20.json | 37250 | `f6035466ff3d` | readout/final | readout/final/quizbank_v20.json | L |
| 2085 | sub | results/quizbank_v20_big.json | 104872 | `da6fecdcbbf6` | readout/final | readout/final/quizbank_v20_big.json | L |
| 2086 | sub | results/readout/reading/_b01_p_counting_recompute_2026_10_10.md | 22104 | `3511cf21a869` | verdict/judge | verdict/judge/_b01_p_counting_recompute_2026_10_10.md | L |
| 2087 | sub | results/readout/reading/_b01_recompute_authorization_supplement_2026_10_11.md | 18454 | `03a66d4c663a` | verdict/kd | verdict/kd/_b01_recompute_authorization_supplement_2026_10_11.md | L |
| 2088 | sub | results/readout/reading/_b01_recompute_sec4_2_erratum_2026_10_10.md | 16441 | `fac3308fb295` | verdict/kd | verdict/kd/_b01_recompute_sec4_2_erratum_2026_10_10.md | L |
| 2089 | sub | results/readout/reading/_c_reading_recompute_2026_10_09.md | 21006 | `95d7d23d24fd` | verdict/pi | verdict/pi/_c_reading_recompute_2026_10_09.md | L |
| 2090 | sub | results/readout/reading/_d8_closeout_protocol_recompute_2026_09_30.md | 31007 | `57aba2cd26a6` | verdict/pi | verdict/pi/_d8_closeout_protocol_recompute_2026_09_30.md | L |
| 2091 | sub | results/readout/reading/_kimi_ftfb_s7_independent_recompute_2026_09_18.json | 3605 | `879db0217f04` | readout/final | readout/final/_kimi_ftfb_s7_independent_recompute_2026_09_18.json | L |
| 2092 | sub | results/readout/reading/_reading_face_basis_rejudge_2026_10_10.md | 24208 | `3fe193a2a01f` | verdict/judge | verdict/judge/_reading_face_basis_rejudge_2026_10_10.md | L |
| 2093 | sub | results/readout/reading/_s3_c4_recount_2026_10_01.md | 32025 | `86af4c109519` | verdict/judge | verdict/judge/_s3_c4_recount_2026_10_01.md | L |
| 2094 | sub | results/readout/reading/_s3_f1_loader_fix_recompute_2026_10_08.md | 22065 | `b2c9840d237b` | readout/final | readout/final/_s3_f1_loader_fix_recompute_2026_10_08.md | L |
| 2095 | sub | results/readout/reading/_s4_e4_axis_disposition_axis2_run_2026_10_10.md | 29700 | `2bda07af86fc` | verdict/pi | verdict/pi/_s4_e4_axis_disposition_axis2_run_2026_10_10.md | L |
| 2096 | sub | results/readout/reading/_s4_empty_sequence_backfill_assessment_2026_10_10.md | 28771 | `41b75ffea7be` | verdict/judge | verdict/judge/_s4_empty_sequence_backfill_assessment_2026_10_10.md | L |
| 2097 | sub | results/readout/reading/_s4_face_closeout_2026_10_09.md | 29158 | `f7d76eda2911` | verdict/judge | verdict/judge/_s4_face_closeout_2026_10_09.md | L |
| 2098 | sub | results/readout/reading/_s4_face_dual_files_verification_2026_10_09.md | 40228 | `cc3fc6eebc6b` | verdict/judge | verdict/judge/_s4_face_dual_files_verification_2026_10_09.md | L |
| 2099 | sub | results/readout/reading/_s4_face_five_lines_ci_readings_2026_10_09.md | 39462 | `bea9bc43a8f3` | verdict/judge | verdict/judge/_s4_face_five_lines_ci_readings_2026_10_09.md | L |
| 2100 | sub | results/readout/reading/_s4_feature_surface_v3_1_definition_2026_10_10.md | 30310 | `d044ce1c069d` | verdict/pi | verdict/pi/_s4_feature_surface_v3_1_definition_2026_10_10.md | L |
| 2101 | sub | results/readout/reading/_s4_heldout_sampling_seed42_sets_2026_10_09.json | 59100 | `8dfc9e0d8bf9` | readout/final | readout/final/_s4_heldout_sampling_seed42_sets_2026_10_09.json | L |
| 2102 | sub | results/readout/reading/_s4_regen_traceability_judgment_2026_10_10.md | 36071 | `a330273b981c` | verdict/judge | verdict/judge/_s4_regen_traceability_judgment_2026_10_10.md | L |
| 2103 | sub | results/readout/reading/_s4_terminal_face_recompute_2026_10_09.md | 46701 | `b412342eabec` | verdict/pi | verdict/pi/_s4_terminal_face_recompute_2026_10_09.md | L |
| 2104 | sub | results/readout/reading/_s4_tree_construct_adjustment_exec_2026_10_10.md | 28515 | `b6b47008f8fd` | readout/final | readout/final/_s4_tree_construct_adjustment_exec_2026_10_10.md | L |
| 2105 | sub | results/readout/reading/_s4_v11_axis2_displacement_items_2026_10_10.json | 9941 | `0eed9053619c` | readout/final | readout/final/_s4_v11_axis2_displacement_items_2026_10_10.json | L |
| 2106 | sub | results/readout/reading/_s4_w1_3636_consistency_check_2026_10_10.md | 29196 | `0e9ae4b6ee8c` | doc/letter | doc/letter/_s4_w1_3636_consistency_check_2026_10_10.md | L |
| 2107 | sub | results/readout/reading/_s4_w2_disposition_registration_2026_10_10.md | 23545 | `566c2f0ad7e8` | verdict/pi | verdict/pi/_s4_w2_disposition_registration_2026_10_10.md | L |
| 2108 | sub | results/readout/reading/_s4_w2bc_effect_registration_2026_10_10.md | 26418 | `b24a8411a260` | verdict/pi | verdict/pi/_s4_w2bc_effect_registration_2026_10_10.md | L |
| 2109 | sub | results/readout/reading/_stage3_readings_verification_2026_10_11.md | 29956 | `023a0cdd3350` | verdict/judge | verdict/judge/_stage3_readings_verification_2026_10_11.md | L |
| 2110 | sub | results/readout/reading/_stage3_trigger_readings_2026_10_11.md | 35711 | `2900948bca6d` | readout/final | readout/final/_stage3_trigger_readings_2026_10_11.md | L |
| 2111 | sub | results/readout/reading/_t1_d7_reading_line_judgment_2026_10_10.md | 28559 | `60bd9ae98640` | verdict/judge | verdict/judge/_t1_d7_reading_line_judgment_2026_10_10.md | L |
| 2112 | sub | results/readout/reading/_v5_item21_patched_recompute_2026_09_28.md | 15895 | `2c1d85913ccc` | verdict/judge | verdict/judge/_v5_item21_patched_recompute_2026_09_28.md | L |
| 2113 | sub | results/readout/reading/_v5_item21_strategyqa_realias_recompute_2026_09_29.md | 14639 | `4e941d0a9c48` | verdict/kd | verdict/kd/_v5_item21_strategyqa_realias_recompute_2026_09_29.md | L |
| 2114 | sub | results/readout/reading/_zero_reading_judgment_2026_10_10.md | 27824 | `a9947f5677df` | verdict/judge | verdict/judge/_zero_reading_judgment_2026_10_10.md | L |
| 2115 | sub | results/readout/reading/deposon_v3x_6way_stage2_2026_09_10.json | 2741 | `d301bbfed982` | readout/final | readout/final/deposon_v3x_6way_stage2_2026_09_10.json | L |
| 2116 | sub | results/readout/reading/deposon_v3x_6way_stage3_2026_09_10.json | 15943 | `d892a9d3d6ba` | readout/final | readout/final/deposon_v3x_6way_stage3_2026_09_10.json | L |
| 2117 | sub | results/readout/run/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md | 33880 | `3015f2481df1` | verdict/pi | verdict/pi/_g5_displacement_threshold_c_approval_effect_and_trigger_eval_2026_10_10.md | L |
| 2118 | sub | results/readout/run/_v3_05_h_caliber_judgment_2026_10_09.md | 22050 | `1c2b5f40e15d` | readout/final | readout/final/_v3_05_h_caliber_judgment_2026_10_09.md | L |
| 2119 | sub | results/readout/run/_v3_recheck_12_jsv_phase_data_2026_09_27.json | 17718 | `642582d4fbd1` | readout/final | readout/final/_v3_recheck_12_jsv_phase_data_2026_09_27.json | L |
| 2120 | sub | results/readout/run/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md | 23152 | `c64146c4ccac` | readout/final | readout/final/_v3_v4_achievements_inventory_3dir_addendum_2026_09_24.md | L |
| 2121 | sub | results/readout/run/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md | 37212 | `24c64cc23907` | readout/final | readout/final/_v3_v4_achievements_inventory_3dir_addendum_v2_2026_09_26.md | L |
| 2122 | sub | results/readout/run/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md | 17130 | `4c731a625868` | doc/letter | doc/letter/_v3_v4_achievements_inventory_3dir_addendum_v2p1_2026_09_26.md | L |
| 2123 | sub | results/readout/run/_v3r1_threshold_path4_draft_2026_10_10.md | 39077 | `a51f5de630ed` | verdict/judge | verdict/judge/_v3r1_threshold_path4_draft_2026_10_10.md | L |
| 2124 | sub | results/readout/run/_v4_concl_t_verify_2026_09_28.md | 13237 | `927adba66e9b` | verdict/judge | verdict/judge/_v4_concl_t_verify_2026_09_28.md | L |
| 2125 | sub | results/readout/run/_v4_design_integration_2026_09_21_v1.0.md | 119732 | `4b10cde29c27` | doc/letter | doc/letter/_v4_design_integration_2026_09_21_v1.0.md | L |
| 2126 | sub | results/readout/run/_v4_design_integration_2026_09_21_v1.1.md | 140007 | `fb5656993071` | doc/letter | doc/letter/_v4_design_integration_2026_09_21_v1.1.md | L |
| 2127 | sub | results/readout/run/_v4_gA3_seeds_judgment_draft_2026_09_22.md | 19772 | `9119bb791dc1` | verdict/judge | verdict/judge/_v4_gA3_seeds_judgment_draft_2026_09_22.md | L |
| 2128 | sub | results/readout/run/_v4_gamma_r1_exec_2026_09_28.md | 21496 | `0d946e65ba3c` | verdict/kd | verdict/kd/_v4_gamma_r1_exec_2026_09_28.md | L |
| 2129 | sub | results/readout/run/_v4_gamma_r1_sources_20260928_S1.md | 2944 | `3d6e997aa692` | verdict/kd | verdict/kd/_v4_gamma_r1_sources_20260928_S1.md | L |
| 2130 | sub | results/readout/run/_v4_gamma_r1_sources_20260928_S2.md | 2647 | `dcec110ca2e0` | verdict/kd | verdict/kd/_v4_gamma_r1_sources_20260928_S2.md | L |
| 2131 | sub | results/readout/run/_v4_gamma_r1_sources_20260928_S3.md | 2554 | `6b9761d710ca` | verdict/kd | verdict/kd/_v4_gamma_r1_sources_20260928_S3.md | L |
| 2132 | sub | results/readout/run/_v4_gamma_r1_sources_20260928_S4.md | 3050 | `16af6baf8463` | verdict/kd | verdict/kd/_v4_gamma_r1_sources_20260928_S4.md | L |
| 2133 | sub | results/readout/run/_v4_gamma_r1_sources_20260928_S5_faceD.md | 2264 | `4f77d49756db` | verdict/kd | verdict/kd/_v4_gamma_r1_sources_20260928_S5_faceD.md | L |
| 2134 | sub | results/readout/run/_v4_group_b_explore_subs_integration_2026_09_22.md | 20532 | `588b45430e88` | doc/letter | doc/letter/_v4_group_b_explore_subs_integration_2026_09_22.md | L |
| 2135 | sub | results/readout/run/_v4_pending_decisions_2026_09_28.md | 24676 | `fe4671517827` | verdict/pi | verdict/pi/_v4_pending_decisions_2026_09_28.md | L |
| 2136 | sub | results/readout/run/_v4_r4_key_purge_manifest_2026_09_24.md | 13884 | `5bf4d9ad2877` | readout/final | readout/final/_v4_r4_key_purge_manifest_2026_09_24.md | L |
| 2137 | sub | results/readout/run/_v4_r4_purge_actions_2026_09_24.md | 33117 | `8bbfe831e7c3` | readout/final | readout/final/_v4_r4_purge_actions_2026_09_24.md | L |
| 2138 | sub | results/readout/run/_v4_rj5_rederive_appendix_2026_09_28.md | 9226 | `985673661209` | verdict/judge | verdict/judge/_v4_rj5_rederive_appendix_2026_09_28.md | L |
| 2139 | sub | results/readout/run/_v4_supp_t15r2_methodology_template.md | 17411 | `6f9b865280a3` | verdict/judge | verdict/judge/_v4_supp_t15r2_methodology_template.md | L |
| 2140 | sub | results/readout/run/_v5_alias_table_d01_d04_c01_c03_2026_09_29.md | 15315 | `b3e39064d7c5` | verdict/kd | verdict/kd/_v5_alias_table_d01_d04_c01_c03_2026_09_29.md | L |
| 2141 | sub | results/readout/run/_v5_b14_p41c_independent_judgment_2026_09_29.md | 22437 | `b752582bc692` | verdict/kd | verdict/kd/_v5_b14_p41c_independent_judgment_2026_09_29.md | L |
| 2142 | sub | results/readout/run/_v5_b15_offsite_readonly_authorization_2026_09_29.md | 18483 | `96a069701b3d` | verdict/kd | verdict/kd/_v5_b15_offsite_readonly_authorization_2026_09_29.md | L |
| 2143 | sub | results/readout/run/_v5_b15_offsite_readonly_authorization_activation_2026_09_29.md | 35006 | `99978eb15c10` | verdict/kd | verdict/kd/_v5_b15_offsite_readonly_authorization_activation_2026_09_29.md | L |
| 2144 | sub | results/readout/run/_v5_b18_o8_semantic_verify_2026_09_29.md | 26544 | `49d4adf8f197` | verdict/kd | verdict/kd/_v5_b18_o8_semantic_verify_2026_09_29.md | L |
| 2145 | sub | results/readout/run/_v5_b18_o8_semantic_verify_r2_2026_09_29.md | 24145 | `dc1233d0ab4f` | verdict/kd | verdict/kd/_v5_b18_o8_semantic_verify_r2_2026_09_29.md | L |
| 2146 | sub | results/readout/run/_v5_b20_gamma_a_attribution_2026_09_29.md | 30789 | `7bad6e52a0f3` | verdict/kd | verdict/kd/_v5_b20_gamma_a_attribution_2026_09_29.md | L |
| 2147 | sub | results/readout/run/_v5_b20_gamma_a_rereview_2026_09_29.md | 30680 | `b22dda133038` | verdict/kd | verdict/kd/_v5_b20_gamma_a_rereview_2026_09_29.md | L |
| 2148 | sub | results/readout/run/_v5_b35_result_attribution_2026_09_29.md | 35313 | `ec358f6f76a3` | verdict/kd | verdict/kd/_v5_b35_result_attribution_2026_09_29.md | L |
| 2149 | sub | results/readout/run/_v5_clearance_mr19_sha1_note_2026_09_29.md | 22859 | `c74ffc6278a8` | verdict/kd | verdict/kd/_v5_clearance_mr19_sha1_note_2026_09_29.md | L |
| 2150 | sub | results/readout/run/_v5_clearance_mr3_s40_fix_note_2026_09_29.md | 15522 | `b1244981065b` | verdict/kd | verdict/kd/_v5_clearance_mr3_s40_fix_note_2026_09_29.md | L |
| 2151 | sub | results/readout/run/_v5_confirm_b13_b22_exec_queue_2026_09_29.md | 39531 | `56549b04a925` | verdict/kd | verdict/kd/_v5_confirm_b13_b22_exec_queue_2026_09_29.md | L |
| 2152 | sub | results/readout/run/_v5_ea_review_chain_rules_2026_09_29.md | 11511 | `8e235f520fb9` | verdict/kd | verdict/kd/_v5_ea_review_chain_rules_2026_09_29.md | L |
| 2153 | sub | results/readout/run/_v5_familyline_r01_r02_independent_judgment_2026_09_29.md | 25392 | `e16e50329c88` | verdict/kd | verdict/kd/_v5_familyline_r01_r02_independent_judgment_2026_09_29.md | L |
| 2154 | sub | results/readout/run/_v5_gamma_end1_rb_clause_addendum_2026_09_29.md | 10397 | `bf38e5f0161e` | verdict/kd | verdict/kd/_v5_gamma_end1_rb_clause_addendum_2026_09_29.md | L |
| 2155 | sub | results/readout/run/_v5_gamma_r1_v2_withdraw_2026_09_29.md | 24611 | `f4ef22a5f97c` | verdict/pi | verdict/pi/_v5_gamma_r1_v2_withdraw_2026_09_29.md | L |
| 2156 | sub | results/readout/run/_v5_gt33_d5_crossref_note_2026_09_29.md | 10989 | `dd50ff801ef7` | readout/final | readout/final/_v5_gt33_d5_crossref_note_2026_09_29.md | L |
| 2157 | sub | results/readout/run/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json | 28638 | `24b0d5eda48a` | readout/final | readout/final/_v5_gt8_lowarm_resultA_cb132cd5_2026_09_29.json | L |
| 2158 | sub | results/readout/run/_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md | 14481 | `31e5bd7b4003` | verdict/kd | verdict/kd/_v5_gt8f_m1_g1_fail_clause_addendum_2026_09_29.md | L |
| 2159 | sub | results/readout/run/_v5_gt_exec_2026_09_29.json | 142217 | `01e95e49b035` | readout/final | readout/final/_v5_gt_exec_2026_09_29.json | L |
| 2160 | sub | results/readout/run/_v5_h231_r07_independent_judgment_2026_09_29.md | 37949 | `70025895600a` | verdict/judge | verdict/judge/_v5_h231_r07_independent_judgment_2026_09_29.md | L |
| 2161 | sub | results/readout/run/_v5_item21_asset_recovery_2026_09_28.md | 8793 | `6c80ff43bdd7` | verdict/judge | verdict/judge/_v5_item21_asset_recovery_2026_09_28.md | L |
| 2162 | sub | results/readout/run/_v5_item35_v3_collinear_exec_2026_09_29.md | 46000 | `912afffed6b9` | verdict/kd | verdict/kd/_v5_item35_v3_collinear_exec_2026_09_29.md | L |
| 2163 | sub | results/readout/run/_v5_loadcorpus_switch_2026_09_29.md | 16414 | `d37e97644bf8` | readout/final | readout/final/_v5_loadcorpus_switch_2026_09_29.md | L |
| 2164 | sub | results/readout/run/_v5_paper_remedy_line_orchestration_2026_09_29.md | 48292 | `d911674e68cf` | verdict/kd | verdict/kd/_v5_paper_remedy_line_orchestration_2026_09_29.md | L |
| 2165 | sub | results/readout/run/_v5_paper_remedy_r1_pledge_2026_09_29.md | 47778 | `816cb91d4611` | verdict/kd | verdict/kd/_v5_paper_remedy_r1_pledge_2026_09_29.md | L |
| 2166 | sub | results/readout/run/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md | 34647 | `29da2ca8932f` | doc/paper | doc/paper/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md | L |
| 2167 | sub | results/readout/run/_v5_paper_remedy_r6b_x27_sourcetrace_2026_09_29.md | 16125 | `b75cc49b360f` | doc/paper | doc/paper/_v5_paper_remedy_r6b_x27_sourcetrace_2026_09_29.md | L |
| 2168 | sub | results/readout/run/_v5_pd_v04_root_naming_candidates_2026_09_29.md | 14312 | `46599dde51a8` | verdict/kd | verdict/kd/_v5_pd_v04_root_naming_candidates_2026_09_29.md | L |
| 2169 | sub | results/readout/run/_v5_pjpm_pc_reverify_bang2_2026_09_29.md | 39517 | `6833cae407e8` | verdict/kd | verdict/kd/_v5_pjpm_pc_reverify_bang2_2026_09_29.md | L |
| 2170 | sub | results/readout/run/_v5_proxy_temp_T0.3.json | 143345 | `04d915714b96` | readout/final | readout/final/_v5_proxy_temp_T0.3.json | L |
| 2171 | sub | results/readout/run/_v5_proxy_temp_T1.5.json | 143261 | `2b36d8632a80` | readout/final | readout/final/_v5_proxy_temp_T1.5.json | L |
| 2172 | sub | results/readout/run/_v5_proxy_vocab_V50.json | 78182 | `2deedc43fc40` | readout/final | readout/final/_v5_proxy_vocab_V50.json | L |
| 2173 | sub | results/readout/run/_v5_proxy_vocab_V500.json | 78191 | `4ddd6afbf16b` | readout/final | readout/final/_v5_proxy_vocab_V500.json | L |
| 2174 | sub | results/readout/run/_v5_theory_input_acquisition_request_2026_09_29.md | 10691 | `83afc4802fe7` | verdict/kd | verdict/kd/_v5_theory_input_acquisition_request_2026_09_29__83afc4802fe7.md | L |
| 2175 | sub | results/readout/run/_v5_track2_qwen_retry_2026_09_29.md | 11957 | `c890771728f3` | verdict/pi | verdict/pi/_v5_track2_qwen_retry_2026_09_29.md | L |
| 2176 | sub | results/readout/run/_v5_v3_deg_p1_reopen_exec_2026_09_29.md | 33622 | `38231ef6f053` | verdict/judge | verdict/judge/_v5_v3_deg_p1_reopen_exec_2026_09_29.md | L |
| 2177 | sub | results/readout/run/_v5_v3_t1_effect_judgment_2026_09_29.md | 40697 | `1995bd4460ae` | verdict/judge | verdict/judge/_v5_v3_t1_effect_judgment_2026_09_29.md | L |
| 2178 | sub | results/readout/run/_v5_v4_export_filter_spec_2026_09_29.md | 22884 | `14dd6ccdbed6` | verdict/kd | verdict/kd/_v5_v4_export_filter_spec_2026_09_29.md | L |
| 2179 | sub | results/readout/run/_zero_consumption_cells_field_correction_2026_10_10.md | 12244 | `36f9ac4ebbf6` | readout/final | readout/final/_zero_consumption_cells_field_correction_2026_10_10.md | L |
| 2180 | sub | results/readout/run/deposon_3risk_v0_fixes_2026_09_11.json | 8338 | `d87c0327a6fb` | readout/final | readout/final/deposon_3risk_v0_fixes_2026_09_11.json | L |
| 2181 | sub | results/readout/run/deposon_ark_models_2026_09_10.json | 23296 | `ccc3ea09a7f5` | readout/final | readout/final/deposon_ark_models_2026_09_10.json | L |
| 2182 | sub | results/readout/run/deposon_benchmark_v1_3_labelshuffle.json | 182322 | `5a7555358be3` | readout/final | readout/final/deposon_benchmark_v1_3_labelshuffle.json | L |
| 2183 | sub | results/readout/run/deposon_deepseek_v41_flash_2026_09_10.json | 13373 | `4d7bea150f3a` | readout/final | readout/final/deposon_deepseek_v41_flash_2026_09_10.json | L |
| 2184 | sub | results/readout/run/deposon_deepseek_v41_flash_30cells_2026_09_10.json | 46432 | `84df447c38df` | readout/final | readout/final/deposon_deepseek_v41_flash_30cells_2026_09_10.json | L |
| 2185 | sub | results/readout/run/deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json | 17549 | `05cde1ca74ef` | readout/final | readout/final/deposon_deepseek_v41_flash_30cells_v2_2026_09_10.json | L |
| 2186 | sub | results/readout/run/deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json | 6748 | `28bad561c328` | readout/final | readout/final/deposon_deepseek_v41_flash_5cells_fix_2026_09_10.json | L |
| 2187 | sub | results/readout/run/deposon_embedding_dual_2026_09_10.json | 6834 | `33f8ac5d4bff` | readout/final | readout/final/deposon_embedding_dual_2026_09_10.json | L |
| 2188 | sub | results/readout/run/deposon_embedding_openrouter_5models_2026_09_10.json | 12785 | `0c0d9afd39ac` | readout/final | readout/final/deposon_embedding_openrouter_5models_2026_09_10.json | L |
| 2189 | sub | results/readout/run/deposon_feshbach_lindblad_sim_2026_09_10.json | 7414 | `aa545c67604d` | readout/final | readout/final/deposon_feshbach_lindblad_sim_2026_09_10.json | L |
| 2190 | sub | results/readout/run/deposon_feshbach_rag_30cells_2026_09_10.json | 64978 | `508f664ffa44` | readout/final | readout/final/deposon_feshbach_rag_30cells_2026_09_10.json | L |
| 2191 | sub | results/readout/run/deposon_gpt6_astra_smoke_2026_09_10.json | 3500 | `4bf92bfdefda` | readout/final | readout/final/deposon_gpt6_astra_smoke_2026_09_10.json | L |
| 2192 | sub | results/readout/run/deposon_gpt6_proxy_smoke_2026_09_10.json | 5485 | `524b34e319b5` | readout/final | readout/final/deposon_gpt6_proxy_smoke_2026_09_10.json | L |
| 2193 | sub | results/readout/run/deposon_gpt6_proxy_step1_2026_09_10.json | 1245 | `2e23115d9d4b` | readout/final | readout/final/deposon_gpt6_proxy_step1_2026_09_10.json | L |
| 2194 | sub | results/readout/run/deposon_gpt6_proxy_v2_2026_09_10.json | 5810 | `a6812512f8f3` | readout/final | readout/final/deposon_gpt6_proxy_v2_2026_09_10.json | L |
| 2195 | sub | results/readout/run/deposon_gpt6_teamorouter_cn_2026_09_10.json | 4855 | `2241567c6efd` | readout/final | readout/final/deposon_gpt6_teamorouter_cn_2026_09_10.json | L |
| 2196 | sub | results/readout/run/deposon_gpt6_vpn_smoke_2026_09_10.json | 3489 | `3267746e47e9` | readout/final | readout/final/deposon_gpt6_vpn_smoke_2026_09_10.json | L |
| 2197 | sub | results/readout/run/deposon_llm_codingplan_30cells_2026_09_10.json | 18634 | `24e4dcbaa4ea` | readout/final | readout/final/deposon_llm_codingplan_30cells_2026_09_10.json | L |
| 2198 | sub | results/readout/run/deposon_openrouter_5model_30cells_2026_09_10.json | 31690 | `b374f80f3b2d` | readout/final | readout/final/deposon_openrouter_5model_30cells_2026_09_10.json | L |
| 2199 | sub | results/readout/run/deposon_openrouter_embedding_5model_2026_09_10.json | 9472 | `45f314f3415c` | readout/final | readout/final/deposon_openrouter_embedding_5model_2026_09_10.json | L |
| 2200 | sub | results/readout/run/deposon_overseas_open_smoke_2026_09_10.json | 6787 | `2481adadcbb9` | readout/final | readout/final/deposon_overseas_open_smoke_2026_09_10.json | L |
| 2201 | sub | results/readout/run/deposon_pf_d1_2026_09_15.json | 21933 | `12791772814e` | readout/final | readout/final/deposon_pf_d1_2026_09_15.json | L |
| 2202 | sub | results/readout/run/deposon_v2_phase2_dual_mainline_2026_09_11.json | 3189 | `e337b824c4b9` | readout/final | readout/final/deposon_v2_phase2_dual_mainline_2026_09_11.json | L |
| 2203 | sub | results/readout/run/deposon_v2_phase2_f2_2026_09_11.json | 4582 | `8b16b611c4db` | readout/final | readout/final/deposon_v2_phase2_f2_2026_09_11.json | L |
| 2204 | sub | results/readout/run/deposon_v2_phase3_f3_2026_09_11.json | 2474 | `0b5dca765d16` | readout/final | readout/final/deposon_v2_phase3_f3_2026_09_11.json | L |
| 2205 | sub | results/readout/run/deposon_v2_phase3_strip_reembed_2026_09_11.json | 4160 | `8900526d8e3a` | readout/final | readout/final/deposon_v2_phase3_strip_reembed_2026_09_11.json | L |
| 2206 | sub | results/readout/run/deposon_v2_phase5_f5_2026_09_11.json | 2356 | `889fc57b3b72` | readout/final | readout/final/deposon_v2_phase5_f5_2026_09_11.json | L |
| 2207 | sub | results/readout/run/deposon_v3x_6way_summary_2026_09_10.json | 1506 | `63e0798e5843` | readout/final | readout/final/deposon_v3x_6way_summary_2026_09_10.json | L |
| 2208 | sub | results/readout/run/deposon_v41_flash_60cells_v2_2026_09_10.json | 38428 | `b1d802a68723` | readout/final | readout/final/deposon_v41_flash_60cells_v2_2026_09_10.json | L |
| 2209 | sub | results/readout/run/deposon_v41_flash_rag_baseline_2026_09_10.json | 101484 | `6754d2655e0a` | readout/final | readout/final/deposon_v41_flash_rag_baseline_2026_09_10.json | L |
| 2210 | sub | results/readout/run/deposon_volcengine_7model_smoke_2026_09_10.json | 5944 | `eae44cc3b7b2` | readout/final | readout/final/deposon_volcengine_7model_smoke_2026_09_10.json | L |
| 2211 | sub | results/readout/run/deposon_volcengine_9model_smoke_2026_09_10.json | 5328 | `0e5ae7d7d641` | readout/final | readout/final/deposon_volcengine_9model_smoke_2026_09_10.json | L |
| 2212 | sub | results/readout/run/deposon_volcengine_coding_plan_5cells_2026_09_10.json | 6058 | `52aa8901556e` | readout/final | readout/final/deposon_volcengine_coding_plan_5cells_2026_09_10.json | L |
| 2213 | sub | results/readout/run/deposon_volcengine_coding_plan_catalog_2026_09_10.json | 2841 | `c0efb547b9d1` | readout/final | readout/final/deposon_volcengine_coding_plan_catalog_2026_09_10.json | L |
| 2214 | sub | results/readout/run/deposon_volcengine_doubao_embedding_2026_09_10.json | 3303 | `e99783d18139` | readout/final | readout/final/deposon_volcengine_doubao_embedding_2026_09_10.json | L |
| 2215 | sub | results/readout/run/deposon_volcengine_embedding_30cells_2026_09_10.json | 24794 | `12be52bc02a7` | readout/final | readout/final/deposon_volcengine_embedding_30cells_2026_09_10.json | L |
| 2216 | sub | results/review/audit/_b14_audit_f2f3_closure_register_2026_10_11.md | 29620 | `9d4a3d6ddf88` | verdict/pi | verdict/pi/_b14_audit_f2f3_closure_register_2026_10_11.md | L |
| 2217 | sub | results/review/audit/_b14_vk_evidence_audit_2026_10_10.md | 33586 | `89f17297f1f5` | verdict/pi | verdict/pi/_b14_vk_evidence_audit_2026_10_10.md | L |
| 2218 | sub | results/review/audit/_deposon_v2scripts_kimi7_audit_20260918_105219.json | 2096 | `3da62b979053` | readout/final | readout/final/_deposon_v2scripts_kimi7_audit_20260918_105219.json | L |
| 2219 | sub | results/review/audit/_ea_audit_batch_vk_2026_10_09.md | 19611 | `ce27db55e0c5` | verdict/judge | verdict/judge/_ea_audit_batch_vk_2026_10_09.md | L |
| 2220 | sub | results/review/audit/_evening_audit_b2_sampling_and_rejudges_2026_10_09.md | 29069 | `b067fd28f950` | verdict/judge | verdict/judge/_evening_audit_b2_sampling_and_rejudges_2026_10_09.md | L |
| 2221 | sub | results/review/audit/_m5_eps_drift_disposition_2026_10_11.md | 2736 | `0722f25f5838` | verdict/pi | verdict/pi/_m5_eps_drift_disposition_2026_10_11.md | L |
| 2222 | sub | results/review/audit/_p_k_v3_glm_json_audit_2026-09-17T08-23-41Z.json | 6678 | `f236e88f22ca` | readout/final | readout/final/_p_k_v3_glm_json_audit_2026-09-17T08-23-41Z.json | L |
| 2223 | sub | results/review/audit/_s4_v31_exec_section8_errata_2026_10_10.md | 23250 | `ec11aec2380d` | readout/final | readout/final/_s4_v31_exec_section8_errata_2026_10_10.md | L |
| 2224 | sub | results/review/audit/_v4_trae_remaining_audit_2026_09_28.md | 39681 | `1a8648083228` | verdict/pi | verdict/pi/_v4_trae_remaining_audit_2026_09_28.md | L |
| 2225 | sub | results/review/audit/_v5_anchor_drift_backfill_2026_09_28.md | 14438 | `6f1edd1ccebb` | verdict/pi | verdict/pi/_v5_anchor_drift_backfill_2026_09_28.md | L |
| 2226 | sub | results/review/audit/_v5_pi_decision_trace_gap_audit_2026_09_29.md | 33101 | `38b043c4be6a` | verdict/kd | verdict/kd/_v5_pi_decision_trace_gap_audit_2026_09_29.md | L |
| 2227 | sub | results/review/audit/_v5_sha12_collision_statement_2026_09_29.md | 28155 | `f0f44cf6dc65` | verdict/kd | verdict/kd/_v5_sha12_collision_statement_2026_09_29.md | L |
| 2228 | sub | results/review/audit/_v5_v3r2_errata_note_2026_09_29.md | 29089 | `d687ad25a68c` | verdict/judge | verdict/judge/_v5_v3r2_errata_note_2026_09_29.md | L |
| 2229 | sub | results/skill_a_p_a_60cells_result_2026_09_11.json | 2220 | `f4a210d69220` | readout/final | readout/final/skill_a_p_a_60cells_result_2026_09_11.json | L |
| 2230 | sub | results/skill_b_p_c_alpha_beta_result_2026_09_11.json | 12609 | `b921002e4dfb` | readout/final | readout/final/skill_b_p_c_alpha_beta_result_2026_09_11.json | L |
| 2231 | sub | results/skill_c_p_e_3modality_result_2026_09_11.json | 5271 | `470425a8c77d` | readout/final | readout/final/skill_c_p_e_3modality_result_2026_09_11.json | L |
| 2232 | sub | results/skill_d_p_f_observer_result_2026_09_11.json | 11010 | `0207c01b9562` | readout/final | readout/final/skill_d_p_f_observer_result_2026_09_11.json | L |
| 2233 | sub | results/tool/generator/_cpath_sim_runner.py | 18783 | `6074d83944dc` | source/tool | source/tool/_cpath_sim_runner.py | L |
| 2234 | sub | results/tool/generator/_pc_d1_d3_2026_09_15.py | 43019 | `09c7c4ddbb39` | source/tool | source/tool/_pc_d1_d3_2026_09_15.py | L |
| 2235 | sub | results/tool/generator/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py | 64849 | `e30d4032f195` | source/tool | source/tool/_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py | L |
| 2236 | sub | results/tool/generator/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py | 19003 | `cd4f1e7b4879` | source/tool | source/tool/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py | L |
| 2237 | sub | results/tool/generator/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py | 52785 | `8ae074194a3d` | source/tool | source/tool/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py | L |
| 2238 | sub | results/tool/generator/_s4prime_readings_runner_2026_10_11.py | 23870 | `52bb6e3bba15` | source/tool | source/tool/_s4prime_readings_runner_2026_10_11.py | L |
| 2239 | sub | results/tool/generator/_s5doubleprime_five_lines_runner_2026_10_11.py | 31232 | `2d8cf387b478` | source/tool | source/tool/_s5doubleprime_five_lines_runner_2026_10_11.py | L |
| 2240 | sub | results/tool/generator/_track2_qwen_check_2026_09_23.py | 12078 | `3ddba570c221` | source/tool | source/tool/_track2_qwen_check_2026_09_23.py | L |
| 2241 | sub | results/tool/generator/_v2_setup.py | 3483 | `73f2b8712a90` | source/tool | source/tool/_v2_setup.py | L |
| 2242 | sub | results/tool/generator/_v2_show_summary.py | 1200 | `0012b38ce438` | source/tool | source/tool/_v2_show_summary.py | L |
| 2243 | sub | results/tool/generator/_v2_smoketest.py | 2040 | `0b6c22c8f379` | source/tool | source/tool/_v2_smoketest.py | L |
| 2244 | sub | results/tool/generator/_v2_stage1_60cells.py | 31556 | `8c7bd12c3a8c` | source/tool | source/tool/_v2_stage1_60cells.py | L |
| 2245 | sub | results/tool/generator/_v2_stage2_f2_drift.py | 10798 | `7e9b2fc57d80` | source/tool | source/tool/_v2_stage2_f2_drift.py | L |
| 2246 | sub | results/tool/generator/_v2_stage3_f3_strip.py | 11803 | `ce4362e325ca` | source/tool | source/tool/_v2_stage3_f3_strip.py | L |
| 2247 | sub | results/tool/generator/_v2_stage4_f4_pdv2.py | 10355 | `b84f5aab6faf` | source/tool | source/tool/_v2_stage4_f4_pdv2.py | L |
| 2248 | sub | results/tool/generator/_v2_stage5_f5_dpath.py | 6480 | `e8871b829d89` | source/tool | source/tool/_v2_stage5_f5_dpath.py | L |
| 2249 | sub | results/tool/generator/_v2_verify_outputs.py | 2656 | `eb0107dd79b5` | source/tool | source/tool/_v2_verify_outputs.py | L |
| 2250 | sub | results/tool/generator/_v3_recheck_05_executor_2026_09_28.py | 38733 | `65f8a7514f34` | source/tool | source/tool/_v3_recheck_05_executor_2026_09_28.py | L |
| 2251 | sub | results/tool/generator/_v3_recheck_10_executor_2026_09_27.py | 33647 | `80947906e592` | source/tool | source/tool/_v3_recheck_10_executor_2026_09_27.py | L |
| 2252 | sub | results/tool/generator/_v3_recheck_12_executor_2026_09_27.py | 49430 | `4850b1cbb010` | source/tool | source/tool/_v3_recheck_12_executor_2026_09_27.py | L |
| 2253 | sub | results/tool/generator/_v3_recheck_19_executor_2026_09_27.py | 19215 | `b133a631b1a8` | source/tool | source/tool/_v3_recheck_19_executor_2026_09_27.py | L |
| 2254 | sub | results/tool/generator/_v3_recheck_27_executor_2026_09_27.py | 34084 | `190cbe01d061` | source/tool | source/tool/_v3_recheck_27_executor_2026_09_27.py | L |
| 2255 | sub | results/tool/generator/_v3_recheck_28_executor_2026_09_27.py | 17735 | `4e8c0dd8f54f` | source/tool | source/tool/_v3_recheck_28_executor_2026_09_27.py | L |
| 2256 | sub | results/tool/generator/_v4_final_verify.py | 4794 | `1dc482062d9b` | source/tool | source/tool/_v4_final_verify.py | L |
| 2257 | sub | results/tool/generator/_v4_supp_l14v3_batch10_r5_executor.py | 70471 | `04383377b6a2` | source/tool | source/tool/_v4_supp_l14v3_batch10_r5_executor.py | L |
| 2258 | sub | results/tool/generator/_v4_supp_l14v3_batch2_r2_models_probe.py | 5334 | `a31d54a4b765` | source/tool | source/tool/_v4_supp_l14v3_batch2_r2_models_probe.py | L |
| 2259 | sub | results/tool/generator/_v4_supp_l14v3_batch2_r6_executor.py | 63788 | `e38d068f309c` | source/tool | source/tool/_v4_supp_l14v3_batch2_r6_executor.py | L |
| 2260 | sub | results/tool/generator/_v4_supp_l14v3_batch3_r5_executor.py | 72156 | `b7478168f87f` | source/tool | source/tool/_v4_supp_l14v3_batch3_r5_executor.py | L |
| 2261 | sub | results/tool/generator/_v4_supp_l14v3_batch4_r5_verify.py | 3050 | `60d19aeee6f5` | source/tool | source/tool/_v4_supp_l14v3_batch4_r5_verify.py | L |
| 2262 | sub | results/tool/generator/_v4_supp_l14v3_batch4_r6_verify.py | 4712 | `222972125231` | source/tool | source/tool/_v4_supp_l14v3_batch4_r6_verify.py | L |
| 2263 | sub | results/tool/generator/_v4_supp_l14v3_batch7_r5_executor.py | 53155 | `38710a448e9c` | source/tool | source/tool/_v4_supp_l14v3_batch7_r5_executor.py | L |
| 2264 | sub | results/tool/generator/_v4_supp_l14v3_batch9_r5_executor.py | 65672 | `9b1a82a28dfb` | source/tool | source/tool/_v4_supp_l14v3_batch9_r5_executor.py | L |
| 2265 | sub | results/tool/generator/_v4_track2_endpoints_probe.py | 20738 | `e7a6eb42c0af` | source/tool | source/tool/_v4_track2_endpoints_probe.py | L |
| 2266 | sub | results/tool/generator/_v4_track2_models_probe.py | 3191 | `da62abaa1e03` | source/tool | source/tool/_v4_track2_models_probe.py | L |
| 2267 | sub | results/tool/generator/_v4_track2_reprobe.py | 2860 | `f92cc93f1304` | source/tool | source/tool/_v4_track2_reprobe.py | L |
| 2268 | sub | results/tool/generator/_v5_bom_u1_exec_2026_09_29.py | 31134 | `c140a28e15ae` | source/tool | source/tool/_v5_bom_u1_exec_2026_09_29.py | L |
| 2269 | sub | results/tool/generator/_v5_pjpm_pc_degen_precheck_executor_2026_09_29.py | 76822 | `f58b0d1c1a93` | source/tool | source/tool/_v5_pjpm_pc_degen_precheck_executor_2026_09_29.py | L |
| 2270 | sub | results/tool/generator/_v5_track2_qwen_retry_executor_20260929.py | 11586 | `d34b46e24a7c` | source/tool | source/tool/_v5_track2_qwen_retry_executor_20260929.py | L |
| 2271 | sub | results/tool/generator/_worker_openrouter_rag_run.py | 24113 | `4458ccf3d64a` | source/tool | source/tool/_worker_openrouter_rag_run.py | L |
| 2272 | sub | results/v20_regression_field.json | 5396 | `534c121765b1` | readout/final | readout/final/v20_regression_field.json | L |
| 2273 | sub | results/verdict/judgement/_clearance_mini_rulings_closeout_register_2026_10_01.md | 31942 | `9238c2287af5` | verdict/pi | verdict/pi/_clearance_mini_rulings_closeout_register_2026_10_01.md | L |
| 2274 | sub | results/verdict/judgement/_e6_n_distinct_judge_types_recompute_2026_10_10.md | 26304 | `82c5c143134e` | verdict/judge | verdict/judge/_e6_n_distinct_judge_types_recompute_2026_10_10.md | L |
| 2275 | sub | results/verdict/judgement/_e6_verdict_v3_rationale_review_2026_10_10.md | 39008 | `664e82968fc2` | verdict/judge | verdict/judge/_e6_verdict_v3_rationale_review_2026_10_10.md | L |
| 2276 | sub | results/verdict/judgement/_fake_verdict_session_log_reverify_2026_09_30.md | 25953 | `c14094bdf815` | verdict/pi | verdict/pi/_fake_verdict_session_log_reverify_2026_09_30.md | L |
| 2277 | sub | results/verdict/judgement/_g4_e3_definition_ruling_material_2026_10_09.md | 30662 | `8ae4016bb41d` | verdict/pi | verdict/pi/_g4_e3_definition_ruling_material_2026_10_09.md | L |
| 2278 | sub | results/verdict/judgement/_k_v3df_0_1_readings_verdict_2026_10_09.md | 37003 | `e98bee353448` | verdict/judge | verdict/judge/_k_v3df_0_1_readings_verdict_2026_10_09.md | L |
| 2279 | sub | results/verdict/judgement/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md | 27735 | `a14aafa220c4` | verdict/judge | verdict/judge/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md | L |
| 2280 | sub | results/verdict/judgement/_kd04_c_denominator_closeout_register_2026_10_10.md | 23029 | `78481cc60494` | verdict/kd | verdict/kd/_kd04_c_denominator_closeout_register_2026_10_10.md | L |
| 2281 | sub | results/verdict/judgement/_kd04_c_denominator_expansion_exec_2026_10_10.md | 27915 | `2caa3966b866` | readout/final | readout/final/_kd04_c_denominator_expansion_exec_2026_10_10.md | L |
| 2282 | sub | results/verdict/judgement/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md | 25123 | `19ad36f7ec84` | verdict/judge | verdict/judge/_kd04_c_denominator_verdict_keeper_alternative_judgment_2026_10_10.md | L |
| 2283 | sub | results/verdict/judgement/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md | 29664 | `63d1566d273e` | verdict/kd | verdict/kd/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md | L |
| 2284 | sub | results/verdict/judgement/_kd_doc1_correction_adoption_register_2026_10_11.md | 10255 | `c55770be5e33` | verdict/kd | verdict/kd/_kd_doc1_correction_adoption_register_2026_10_11.md | L |
| 2285 | sub | results/verdict/judgement/_kd_heteronym_classification_disposition_2026_10_09.md | 29761 | `2d291f1d8de5` | verdict/kd | verdict/kd/_kd_heteronym_classification_disposition_2026_10_09.md | L |
| 2286 | sub | results/verdict/judgement/_kd_legacy_rewrite_plan_2026_10_10.md | 17643 | `a9698fed8b9b` | verdict/kd | verdict/kd/_kd_legacy_rewrite_plan_2026_10_10.md | L |
| 2287 | sub | results/verdict/judgement/_kd_legacy_rewrite_register_2026_10_10.md | 14537 | `9a7936882a5d` | verdict/kd | verdict/kd/_kd_legacy_rewrite_register_2026_10_10.md | L |
| 2288 | sub | results/verdict/judgement/_kd_legacy_rewrite_ruling_2026_10_10.md | 13731 | `2cadab5ed4f7` | verdict/kd | verdict/kd/_kd_legacy_rewrite_ruling_2026_10_10.md | L |
| 2289 | sub | results/verdict/judgement/_kd_login_register_section65_correction_2026_10_10.md | 20422 | `316d14c137bb` | verdict/kd | verdict/kd/_kd_login_register_section65_correction_2026_10_10.md | L |
| 2290 | sub | results/verdict/judgement/_kd_resolvability_and_optional_experiments_2026_10_09.md | 70328 | `53d4fa3a681f` | verdict/kd | verdict/kd/_kd_resolvability_and_optional_experiments_2026_10_09.md | L |
| 2291 | sub | results/verdict/judgement/_kd_rewrite_fingerprint_sync_2026_10_10.md | 20862 | `aeefc94a94b5` | verdict/kd | verdict/kd/_kd_rewrite_fingerprint_sync_2026_10_10.md | L |
| 2292 | sub | results/verdict/judgement/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md | 19525 | `b07887551f7c` | verdict/kd | verdict/kd/_kd_uncognizable_meaning_rewrite_register_2026_10_10.md | L |
| 2293 | sub | results/verdict/judgement/_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md | 4794 | `1c7445fca0de` | verdict/pi | verdict/pi/_kimi_fullupload_r1_r4_rulings_register_2026_09_30.md | L |
| 2294 | sub | results/verdict/judgement/_krj10_terminal_verdict_closure_2026_10_11.md | 14101 | `f2e8e32089b2` | verdict/judge | verdict/judge/_krj10_terminal_verdict_closure_2026_10_11.md | L |
| 2295 | sub | results/verdict/judgement/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md | 16567 | `fb7bb5da85ec` | verdict/pi | verdict/pi/_krj4_trj1_pick_and_pass_verdict_2026_10_11.md | L |
| 2296 | sub | results/verdict/judgement/_krj5_final_disposition_verdict_2026_10_11.md | 60700 | `2b6bf509a135` | verdict/pi | verdict/pi/_krj5_final_disposition_verdict_2026_10_11.md | L |
| 2297 | sub | results/verdict/judgement/_krj_all_five_verdicts_rewrite_2026_10_11.md | 72247 | `78fb8c47c944` | verdict/judge | verdict/judge/_krj_all_five_verdicts_rewrite_2026_10_11.md | L |
| 2298 | sub | results/verdict/judgement/_krj_all_terminal_verdicts_2026_10_11.md | 95659 | `f52231807e36` | verdict/kd | verdict/kd/_krj_all_terminal_verdicts_2026_10_11.md | L |
| 2299 | sub | results/verdict/judgement/_krj_five_verdicts_adjudication_2026_10_11.md | 16064 | `5c0efd663847` | verdict/judge | verdict/judge/_krj_five_verdicts_adjudication_2026_10_11.md | L |
| 2300 | sub | results/verdict/judgement/_kv3s_4_terminal_verdict_2026_10_09.md | 50858 | `e51317fcc5cf` | verdict/pi | verdict/pi/_kv3s_4_terminal_verdict_2026_10_09.md | L |
| 2301 | sub | results/verdict/judgement/_kv3s_4_terminal_verdict_supplement_2026_10_09.md | 20211 | `0f82948defb3` | verdict/judge | verdict/judge/_kv3s_4_terminal_verdict_supplement_2026_10_09.md | L |
| 2302 | sub | results/verdict/judgement/_limb_reading_verdict_kv3s33_2026_10_01.md | 56329 | `c5866ce87d9c` | verdict/judge | verdict/judge/_limb_reading_verdict_kv3s33_2026_10_01__c5866ce87d9c.md | L |
| 2303 | sub | results/verdict/judgement/_morning_wrapup_pending_rulings_2026_10_01.md | 7341 | `2b6e8b527f93` | verdict/pi | verdict/pi/_morning_wrapup_pending_rulings_2026_10_01.md | L |
| 2304 | sub | results/verdict/judgement/_pending_rulings_drafts_2026_10_11.md | 42775 | `c8428b883029` | verdict/kd | verdict/kd/_pending_rulings_drafts_2026_10_11.md | L |
| 2305 | sub | results/verdict/judgement/_r2_verdict_179domain_arith_verification_2026_10_09.md | 30532 | `511c81b96745` | verdict/judge | verdict/judge/_r2_verdict_179domain_arith_verification_2026_10_09.md | L |
| 2306 | sub | results/verdict/judgement/_round56_v4_kd_row_correction_revision_2026_10_10.md | 23453 | `6d8537cb127f` | verdict/kd | verdict/kd/_round56_v4_kd_row_correction_revision_2026_10_10.md | L |
| 2307 | sub | results/verdict/judgement/_s3_kv3s_3_verdict_2026_10_01.md | 35037 | `e394bb6b5ddf` | verdict/judge | verdict/judge/_s3_kv3s_3_verdict_2026_10_01.md | L |
| 2308 | sub | results/verdict/judgement/_s4_bc_construction_ruling_2026_10_09.md | 30257 | `e2fdb380cd3c` | verdict/pi | verdict/pi/_s4_bc_construction_ruling_2026_10_09.md | L |
| 2309 | sub | results/verdict/judgement/_s4_final_ruling_card_register_2026_10_09.md | 2135 | `f62401b619cc` | verdict/pi | verdict/pi/_s4_final_ruling_card_register_2026_10_09.md | L |
| 2310 | sub | results/verdict/judgement/_s4_topup_intake_verdict_2026_10_09.md | 33799 | `658d7f3ab231` | verdict/judge | verdict/judge/_s4_topup_intake_verdict_2026_10_09.md | L |
| 2311 | sub | results/verdict/judgement/_s6doubleprime_terminal_verdicts_2026_10_11.md | 76910 | `bba3b889d849` | verdict/judge | verdict/judge/_s6doubleprime_terminal_verdicts_2026_10_11.md | L |
| 2312 | sub | results/verdict/judgement/_s6doubleprime_verdict_supplement_2026_10_11.md | 31515 | `8e19c10ce219` | verdict/pi | verdict/pi/_s6doubleprime_verdict_supplement_2026_10_11.md | L |
| 2313 | sub | results/verdict/judgement/_s6prime_terminal_verdicts_2026_10_11.md | 54937 | `1c8ce58d6484` | verdict/judge | verdict/judge/_s6prime_terminal_verdicts_2026_10_11.md | L |
| 2314 | sub | results/verdict/judgement/_t1_exp2_verdict_2026_10_10.md | 48298 | `15c1c4b317a0` | verdict/kd | verdict/kd/_t1_exp2_verdict_2026_10_10.md | L |
| 2315 | sub | results/verdict/judgement/_t1_exp2_verdict_bytes_correction_2026_10_10.md | 13480 | `e863ca5fb157` | verdict/judge | verdict/judge/_t1_exp2_verdict_bytes_correction_2026_10_10.md | L |
| 2316 | sub | results/verdict/judgement/_t1_gate_closure_and_recompute_verdict_2026_10_01.md | 72934 | `0b5fb78727c2` | verdict/kd | verdict/kd/_t1_gate_closure_and_recompute_verdict_2026_10_01.md | L |
| 2317 | sub | results/verdict/judgement/_t1_pairing_caliber_ruling_2026_10_09.md | 21346 | `2ded8091114a` | verdict/pi | verdict/pi/_t1_pairing_caliber_ruling_2026_10_09.md | L |
| 2318 | sub | results/verdict/judgement/_v3_02_ethard_closure_verdict_2026_10_09.md | 27819 | `aa0f96bb618f` | verdict/judge | verdict/judge/_v3_02_ethard_closure_verdict_2026_10_09.md | L |
| 2319 | sub | results/verdict/judgement/_v3_recheck_26b_verdict_2026_10_01.md | 26309 | `8bbecb15b28b` | verdict/judge | verdict/judge/_v3_recheck_26b_verdict_2026_10_01.md | L |
| 2320 | sub | results/verdict/judgement/_v3n_cpath_live_rerun_verdict_2026_10_01.md | 16409 | `a91efbfec3d0` | verdict/judge | verdict/judge/_v3n_cpath_live_rerun_verdict_2026_10_01.md | L |
| 2321 | sub | results/verdict/judgement/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md | 26637 | `ba4d07bd7000` | verdict/pi | verdict/pi/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26__ba4d07bd7000.md | L |
| 2322 | sub | results/verdict/judgement/_v5_fake_verdict_forensics_2026_09_28.md | 35870 | `1b135d8b1e08` | verdict/pi | verdict/pi/_v5_fake_verdict_forensics_2026_09_28.md | L |
| 2323 | sub | results/verdict/judgement/_v5_gt8_lowarm_verdict_2026_09_29.md | 32653 | `9140b6e5970b` | verdict/judge | verdict/judge/_v5_gt8_lowarm_verdict_2026_09_29.md | L |
| 2324 | sub | results/verdict/judgement/_v5_gt8_lowarm_verdict_r2_2026_09_29.md | 40282 | `aff727434aa4` | verdict/judge | verdict/judge/_v5_gt8_lowarm_verdict_r2_2026_09_29.md | L |
| 2325 | sub | results/verdict/judgement/_v5_item21_strategyqa_realias_verdict_2026_09_29.md | 32354 | `26eaa156108f` | verdict/pi | verdict/pi/_v5_item21_strategyqa_realias_verdict_2026_09_29.md | L |
| 2326 | sub | results/verdict/judgement/_v5_item21_verdict_2026_09_28.md | 28155 | `de274bd38955` | verdict/judge | verdict/judge/_v5_item21_verdict_2026_09_28.md | L |
| 2327 | sub | results/verdict/judgement/_v5_item35_v3_collinear_verdict_2026_10_01.md | 38266 | `363cce3dae59` | verdict/kd | verdict/kd/_v5_item35_v3_collinear_verdict_2026_10_01.md | L |
| 2328 | sub | results/verdict/judgement/_v5_item35_v3_collinear_verdict_prep_2026_10_01.md | 33755 | `a31026f2384d` | verdict/kd | verdict/kd/_v5_item35_v3_collinear_verdict_prep_2026_10_01.md | L |
| 2329 | sub | results/verdict/judgement/_v5_pjpm_pc_verdict_bang3_2026_09_29.md | 41566 | `1814f9590f0f` | verdict/judge | verdict/judge/_v5_pjpm_pc_verdict_bang3_2026_09_29.md | L |
| 2330 | sub | results/verdict/judgement/_v5_rj5_verdict_2026_09_29.md | 40057 | `9c1ccbd5cf5a` | verdict/judge | verdict/judge/_v5_rj5_verdict_2026_09_29.md | L |
| 2331 | sub | results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md | 42645 | `63d898ab1b71` | verdict/kd | verdict/kd/_v5_v3_deg_p1_reopen_verdict_2026_09_29.md | L |
| 2332 | sub | results/verdict/judgement/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md | 44054 | `8adaf4e5d868` | verdict/kd | verdict/kd/_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md | L |
| 2333 | sub | results/verdict/judgement/_verdict_pack_d_prep_2026_10_01.md | 49471 | `8c2ce0dc1c2d` | verdict/judge | verdict/judge/_verdict_pack_d_prep_2026_10_01.md | L |
| 2334 | sub | results/verdict/judgement/c5_b_group_verdict_2026_10_01.md | 30118 | `3fbf6b38a383` | verdict/kd | verdict/kd/c5_b_group_verdict_2026_10_01.md | L |
| 2335 | sub | results/verdict/pi_register/_adendum_B_pi_real_labels_v2_20260917_133726.json | 2374 | `3d344711cf8c` | readout/final | readout/final/_adendum_B_pi_real_labels_v2_20260917_133726.json | L |
| 2336 | sub | results/verdict/pi_register/_adendum_B_pi_real_labels_v2_20260917_133852.json | 2374 | `c725e08e0a1c` | readout/final | readout/final/_adendum_B_pi_real_labels_v2_20260917_133852.json | L |
| 2337 | sub | results/verdict/pi_register/_gate_one_pi_endorsement_register_2026_10_12.md | 9579 | `b09209e9c20d` | verdict/pi | verdict/pi/_gate_one_pi_endorsement_register_2026_10_12.md | L |
| 2338 | sub | results/verdict/pi_register/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md | 15214 | `31e32ccc59bf` | verdict/pi | verdict/pi/_krj_pi_picks_adoption_krj6_revise_2026_10_11.md | L |
| 2339 | sub | results/verdict/pi_register/_linestand_pi_signoff_2026_10_01.md | 35538 | `cb5d933f8fae` | verdict/pi | verdict/pi/_linestand_pi_signoff_2026_10_01.md | L |
| 2340 | sub | results/verdict/pi_register/_pending_pi_items_master_register_2026_10_09.md | 35258 | `87ab4929477f` | verdict/pi | verdict/pi/_pending_pi_items_master_register_2026_10_09.md | L |
| 2341 | sub | results/verdict/pi_register/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md | 13883 | `0a4b752cbc56` | verdict/pi | verdict/pi/_pi_card_123_adoption_and_gate_one_request_2026_10_11.md | L |
| 2342 | sub | results/verdict/pi_register/_pi_effectivity_declaration_register_2026_10_11.md | 54511 | `41a82bde5190` | verdict/kd | verdict/kd/_pi_effectivity_declaration_register_2026_10_11.md | L |
| 2343 | sub | results/verdict/pi_register/_pi_facing_items_screen_2026_10_09.md | 59604 | `a6d33cf318fe` | verdict/pi | verdict/pi/_pi_facing_items_screen_2026_10_09.md | L |
| 2344 | sub | results/verdict/pi_register/_v4_pi_cot_v2_collection_log.md | 1181 | `167ad91f198e` | readout/final | readout/final/_v4_pi_cot_v2_collection_log.md | L |
| 2345 | sub | results/verdict/pi_register/_v4_pi_cot_v2_prereg_activation_2026_09_23.md | 1016 | `00584e5a5c78` | verdict/kd | verdict/kd/_v4_pi_cot_v2_prereg_activation_2026_09_23.md | L |
| 2346 | sub | results/verdict/pi_register/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md | 12152 | `ae154971d1d2` | verdict/pi | verdict/pi/_v4_pi_cot_v3_lock_and_rejudge_register_2026_09_28.md | L |
| 2347 | sub | results/work/process/_archive_cleanup_extension_2026_09_28.md | 28774 | `889d15247607` | verdict/pi | verdict/pi/_archive_cleanup_extension_2026_09_28.md | L |
| 2348 | sub | results/work/process/_archive_cleanup_non_upload_2026_09_28.md | 56714 | `34f2c63306b8` | verdict/pi | verdict/pi/_archive_cleanup_non_upload_2026_09_28.md | L |
| 2349 | sub | results/work/process/_cleanup_round2_register_2026_09_29.md | 36245 | `ee47a2ec49f4` | verdict/pi | verdict/pi/_cleanup_round2_register_2026_09_29.md | L |
| 2350 | sub | results/work/process/_cleanup_round_2026_10_01.md | 27477 | `0db6e5d6146c` | verdict/pi | verdict/pi/_cleanup_round_2026_10_01.md | L |
| 2351 | sub | results/work/process/_cleanup_round_2026_10_08.md | 33179 | `d048a6de1dea` | verdict/pi | verdict/pi/_cleanup_round_2026_10_08.md | L |
| 2352 | sub | results/work/process/_dup_name_diff_content_scan_2026_10_08.json | 1302889 | `a27d11f45c21` | readout/final | readout/final/_dup_name_diff_content_scan_2026_10_08.json | L |
| 2353 | sub | results/work/process/_log_surface_scan_2026_10_08.md | 3156 | `6b0b202c5a6c` | verdict/judge | verdict/judge/_log_surface_scan_2026_10_08.md | L |
| 2354 | sub | results/work/process/_probe_url_update_log_2026_09_23.md | 5398 | `8fcdd872dc07` | readout/final | readout/final/_probe_url_update_log_2026_09_23.md | L |
| 2355 | sub | results/work/process/_skill_call_surface_probe_2026_09_30.md | 32261 | `112346df64fb` | verdict/pi | verdict/pi/_skill_call_surface_probe_2026_09_30.md | L |
| 2356 | sub | results/work/process/_skill_call_surface_probe_supplement_a_2026_09_30.md | 50658 | `a06316c3c7f2` | verdict/pi | verdict/pi/_skill_call_surface_probe_supplement_a_2026_09_30.md | L |
| 2357 | sub | results/work/process/_skill_call_surface_probe_supplement_b_2026_09_30.md | 82744 | `69d311e6a4c7` | verdict/pi | verdict/pi/_skill_call_surface_probe_supplement_b_2026_09_30.md | L |
| 2358 | sub | results/work/process/_suspect17_release_move_register_2026_10_09.md | 22351 | `9a4d40bfcdc3` | verdict/pi | verdict/pi/_suspect17_release_move_register_2026_10_09.md | L |
| 2359 | sub | results/work/process/_track2_endpoints_probe_2026_09_23.json | 5803 | `c846f7fc79ee` | readout/final | readout/final/_track2_endpoints_probe_2026_09_23.json | L |
| 2360 | sub | results/work/process/_v4_daily_cleanup_2026_09_28.md | 25491 | `f56e6fbf04ef` | verdict/pi | verdict/pi/_v4_daily_cleanup_2026_09_28.md | L |
| 2361 | sub | results/work/process/_v4_noise_cleanup_manifest_v3_2026_09_25.md | 24491 | `6f3f6fa3ab1d` | readout/final | readout/final/_v4_noise_cleanup_manifest_v3_2026_09_25.md | L |
| 2362 | sub | results/work/process/_v4_noise_cleanup_manifest_v4_2026_09_27.md | 38001 | `82e90ff496ae` | verdict/pi | verdict/pi/_v4_noise_cleanup_manifest_v4_2026_09_27.md | L |
| 2363 | sub | results/work/process/_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json | 2635 | `21a89eb36a14` | readout/final | readout/final/_v4_supp_l14v3_batch2_r2_result_probe_fail_v1.json | L |
| 2364 | sub | results/work/process/_v5_agent_trio_post_reorg_note_2026_09_29.md | 9795 | `9c7182d93049` | verdict/kd | verdict/kd/_v5_agent_trio_post_reorg_note_2026_09_29.md | L |
| 2365 | sub | results/work/process/_wrapup_cleanup_inventory_register_2026_09_29.md | 22556 | `6beeb397a4c1` | verdict/pi | verdict/pi/_wrapup_cleanup_inventory_register_2026_09_29.md | L |
| 2366 | sub | reviews/deep_probe_R1.md | 14895 | `190dd5df9af2` | verdict/judge | verdict/judge/deep_probe_R1.md | L |
| 2367 | sub | reviews/literature_scan_v2X_B.md | 30468 | `313b30815a39` | readout/final | readout/final/literature_scan_v2X_B.md | L |
| 2368 | sub | tmp_movedout_2026_09_28/_cleanup_classify_2026_09_28.py | 3232 | `efb57dc056f0` | source/tool | source/tool/_cleanup_classify_2026_09_28.py | L |
| 2369 | sub | tmp_movedout_2026_09_28/_cleanup_probe_2026_09_28.py | 2556 | `20bd0972fa00` | source/tool | source/tool/_cleanup_probe_2026_09_28.py | L |
| 2370 | sub | tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt | 12365 | `75f9058f8a51` | readout/final | readout/final/_cleanup_probe_out_2026_09_28.txt | L |
| 2371 | sub | tmp_movedout_2026_09_28/_cleanup_resolve_2026_09_28.py | 2735 | `57085a643c33` | source/tool | source/tool/_cleanup_resolve_2026_09_28.py | L |
| 2372 | sub | tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py | 3229 | `97291768f38d` | source/tool | source/tool/_cleanup_transfer_scan_2026_09_28.py | L |
| 2373 | sub | tmp_movedout_2026_09_28/_cleanup_transfer_scan_out_2026_09_28.txt | 5017 | `04d99d651df9` | verdict/judge | verdict/judge/_cleanup_transfer_scan_out_2026_09_28.txt | L |
| 2374 | sub | tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/_old_corpus_view.py | 23893 | `7d8d6a30dd8c` | source/tool | source/tool/_old_corpus_view.py | L |
| 2375 | sub | tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/annotate_baseline.py | 2050 | `be710bb0c40f` | source/tool | source/tool/annotate_baseline.py | L |
| 2376 | sub | tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/apply_fix.py | 3460 | `c3808483722e` | source/tool | source/tool/apply_fix.py | L |
| 2377 | sub | tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/baseline_post.json | 115634 | `5cdf357a45e8` | readout/final | readout/final/baseline_post.json | L |
| 2378 | sub | tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/baseline_pre.json | 115139 | `c5e0497b9020` | readout/final | readout/final/baseline_pre.json | L |
| 2379 | sub | tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/snapshot.py | 1438 | `dcede756619f` | source/tool | source/tool/snapshot.py | L |
| 2380 | sub | tmp_movedout_2026_09_29/_v5_loadcorpus_switch_2026_09_29/verify_2026_09_29.py | 11167 | `a1c70189ebbb` | source/tool | source/tool/verify_2026_09_29.py | L |
| 2381 | sub | tmp_movedout_2026_10_01/legacy_caliber/README_V1_LEGACY.md | 3756 | `18e095c85427` | doc/readme | doc/readme/README_V1_LEGACY.md | L |
| 2382 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s1b_inv2_2026_09_27.py | 1546 | `af475f496a5e` | source/tool | source/tool/_v4_wide_s1b_inv2_2026_09_27.py | L |
| 2383 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s2_scan_2026_09_27.py | 4000 | `c2cc22b27047` | source/tool | source/tool/_v4_wide_s2_scan_2026_09_27.py | L |
| 2384 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3_keyscan_2026_09_27.py | 2647 | `a32af07111df` | source/tool | source/tool/_v4_wide_s3_keyscan_2026_09_27.py | L |
| 2385 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3b_uuidctx_2026_09_27.py | 1707 | `8fdec59aa96b` | source/tool | source/tool/_v4_wide_s3b_uuidctx_2026_09_27.py | L |
| 2386 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s3c_keydetail_2026_09_27.py | 2490 | `16ae5764add1` | source/tool | source/tool/_v4_wide_s3c_keydetail_2026_09_27.py | L |
| 2387 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s4_verify_2026_09_27.py | 2812 | `dbe00430d769` | source/tool | source/tool/_v4_wide_s4_verify_2026_09_27.py | L |
| 2388 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s6_unrefscan_2026_09_27.py | 2495 | `1b31a3111a86` | source/tool | source/tool/_v4_wide_s6_unrefscan_2026_09_27.py | L |
| 2389 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s7_fix_2026_09_27.py | 6101 | `fc200e5f343d` | source/tool | source/tool/_v4_wide_s7_fix_2026_09_27.py | L |
| 2390 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s8_fix3_2026_09_27.py | 3514 | `051dbdb121c9` | source/tool | source/tool/_v4_wide_s8_fix3_2026_09_27.py | L |
| 2391 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wide_2026_09_27/_v4_wide_s9_final_2026_09_27.py | 3399 | `aef86f53cc0e` | source/tool | source/tool/_v4_wide_s9_final_2026_09_27.py | L |
| 2392 | sub | tmp_movedout_2026_10_01/process_scripts/v4_wt_2026_09_27/_v4_wt_s5_verify_2026_09_27.py | 4950 | `736e56cd5553` | source/tool | source/tool/_v4_wt_s5_verify_2026_09_27.py | L |
| 2393 | sub | tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s1_2026_09_30.py | 4351 | `f77f72f7b86e` | source/tool | source/tool/_v5_wa_s1_2026_09_30.py | L |
| 2394 | sub | tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s2b_2026_09_30.py | 3583 | `9403dfac5824` | source/tool | source/tool/_v5_wa_s2b_2026_09_30.py | L |
| 2395 | sub | tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s2c_2026_09_30.py | 3168 | `2f55832a82cb` | source/tool | source/tool/_v5_wa_s2c_2026_09_30.py | L |
| 2396 | sub | tmp_movedout_2026_10_01/process_scripts/v5_wa_2026_09_30/_v5_wa_s3_fix_2026_09_30.py | 4742 | `ff16d68fdb81` | source/tool | source/tool/_v5_wa_s3_fix_2026_09_30.py | L |
| 2397 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_asset_recount_2026_09_30.md | 9441 | `e56286e6cba0` | doc/letter | doc/letter/_asset_recount_2026_09_30.md | L |
| 2398 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v4_tmp_cleanup_2026_09_28.md | 5131 | `b8338bdd33f2` | verdict/pi | verdict/pi/_v4_tmp_cleanup_2026_09_28.md | L |
| 2399 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_1_k04_caliber_fixation_2026_09_29.md | 13127 | `697145c8352d` | verdict/kd | verdict/kd/_v5_b14_1_k04_caliber_fixation_2026_09_29.md | L |
| 2400 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b14_r3_anchor_retrieval_2026_09_29.md | 23023 | `6e0a1461a688` | readout/final | readout/final/_v5_b14_r3_anchor_retrieval_2026_09_29.md | L |
| 2401 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_1dcritical_lit_search_2026_09_29.md | 26931 | `09ad0c6ce46a` | verdict/kd | verdict/kd/_v5_b16_1dcritical_lit_search_2026_09_29.md | L |
| 2402 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_dual_caliber_rule_2026_09_29.md | 16262 | `3b7dfdce494e` | verdict/kd | verdict/kd/_v5_b16_dual_caliber_rule_2026_09_29.md | L |
| 2403 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_idx23_blindrate_verify_2026_09_29.md | 19755 | `430588419975` | verdict/kd | verdict/kd/_v5_b16_idx23_blindrate_verify_2026_09_29.md | L |
| 2404 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b16_mq11_case_2026_09_29.md | 16723 | `85f92c8d18d1` | verdict/kd | verdict/kd/_v5_b16_mq11_case_2026_09_29.md | L |
| 2405 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b17_three_caliber_fixation_2026_09_29.md | 19709 | `d47b5e067c1c` | verdict/kd | verdict/kd/_v5_b17_three_caliber_fixation_2026_09_29.md | L |
| 2406 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b18_coding_caliber_2026_09_29.md | 14304 | `04f6890dc4a8` | verdict/kd | verdict/kd/_v5_b18_coding_caliber_2026_09_29.md | L |
| 2407 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_b18_single_count_fixation_2026_09_29.md | 13608 | `006e316bfe4c` | verdict/kd | verdict/kd/_v5_b18_single_count_fixation_2026_09_29.md | L |
| 2408 | sub | tmp_movedout_2026_10_09/uncertain_release_2026_09/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md | 18514 | `bf0874456a58` | readout/final | readout/final/_v5_glm_charlie_reread_ac74a04efeb2_2026_09_29.md | L |
| 2409 | sub | verifier/README.md | 14360 | `d76f2dc473be` | doc/paper | doc/paper/README__d76f2dc473be.md | L |
| 2410 | sub | verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json | 5049 | `da517c115f3c` | readout/final | readout/final/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json | L |
| 2411 | sub | verifier/handoff/P_A_V0_anchors_sha256_12.json | 7796 | `c4f029f780d8` | readout/final | readout/final/P_A_V0_anchors_sha256_12.json | L |
| 2412 | sub | verifier/handoff/P_F_PREDECISION_2026_09_09.json | 3680 | `b41c98bf90cc` | readout/final | readout/final/P_F_PREDECISION_2026_09_09.json | L |
| 2413 | sub | verifier/kill_lines/GT_kill_line_carrier_v0.md | 16486 | `0f65a42e7a34` | verdict/kd | verdict/kd/GT_kill_line_carrier_v0.md | L |
| 2414 | sub | verifier/kill_lines/GT_kill_line_carrier_v1.md | 18905 | `9e09214cf088` | verdict/kd | verdict/kd/GT_kill_line_carrier_v1.md | L |
| 2415 | sub | volcengine_glm_latest_30cells_v2_runner_2026_09_10.py | 20745 | `26ff34bfcc79` | source/tool | source/tool/volcengine_glm_latest_30cells_v2_runner_2026_09_10.py | L |

### §3-3 远端轨面（**218 件** · 按名与指纹认人）

> 📌 **远端轨 ＝ `_remote_pullback_2026_10_17`**（远端公开仓 `zeroandcat/Deposon` 之本地拉回留痕·时点 2026-10-17）。本棒**逐件自测**其 BYTES／SHA-12；**⛔0 读其正文内容**（仅按名与指纹认人）。面内分布：`_september_workspace/` 145 件、`results/` 72 件、`letters/` 1 件。

| # | 远端轨相对路径 | BYTES | SHA-12 | 来源面 |
|--:|:--|--:|:--|:-:|
| 1 | _september_workspace\deposon_team\verifier\v42_v2_2026_09_16.py | 17363 | `c5598b13c139` | R |
| 2 | _september_workspace\deposon_team\verifier\v42_v2_baseline_2026_09_16.json | 1879 | `483602856618` | R |
| 3 | _september_workspace\deposon_team\verifier\v42_v2_runs_2026_09_16.jsonl | 770 | `b471190e579c` | R |
| 4 | _september_workspace\results\_archive_2026_09_20\_archive_manifest_2026_09_18.json | 4712 | `a729875c0c67` | R |
| 5 | _september_workspace\results\_archive_2026_09_20\_archive_manifest_2026_09_20.json | 35690 | `df133892691e` | R |
| 6 | _september_workspace\results\_archive_2026_09_20\_audit_secret_2026_09_20_anchor_guard.py | 6433 | `780a8adae5e8` | R |
| 7 | _september_workspace\results\_archive_2026_09_20\_audit_temp_inspect_minimax_m3.py.bak | 1171 | `dd92ca013774` | R |
| 8 | _september_workspace\results\_archive_2026_09_20\_audit_temp_inspect_workers.py.bak | 1158 | `772925b20bcc` | R |
| 9 | _september_workspace\results\_archive_2026_09_20\_audit_temp_stage1_tra_breakdown.py.bak | 18023 | `dfc4aa73e2fc` | R |
| 10 | _september_workspace\results\_archive_2026_09_20\_coze_online_v3_d7format_2026_09_18.pdf | 454307 | `adc99e04ac53` | R |
| 11 | _september_workspace\results\_archive_2026_09_20\_coze_paper_v1_双审报告_2026_09_17.md | 85627 | `dc761bd8b85d` | R |
| 12 | _september_workspace\results\_archive_2026_09_20\_cpath_sim_run_2026_09_10.log | 1508 | `6bfc5dde07a8` | R |
| 13 | _september_workspace\results\_archive_2026_09_20\_d05_main_runner_2026_09_18.py | 41446 | `f3d4ec483599` | R |
| 14 | _september_workspace\results\_archive_2026_09_20\_d05_main_runner_20260918.log | 9232 | `b6657ba162b3` | R |
| 15 | _september_workspace\results\_archive_2026_09_20\_d05_md_report_only_2026_09_18.py | 13694 | `7a5be4aef9ac` | R |
| 16 | _september_workspace\results\_archive_2026_09_20\_d05_sanity_3backbone_2026_09_18.py | 5452 | `c917f8fa142c` | R |
| 17 | _september_workspace\results\_archive_2026_09_20\_d05_sanity_3backbone_20260918.log | 2088 | `41bea33b9492` | R |
| 18 | _september_workspace\results\_archive_2026_09_20\_d05_sanity_3backbone_20260918_100110.json | 2292 | `0a1e91d6f772` | R |
| 19 | _september_workspace\results\_archive_2026_09_20\_d05_verify_sha_2026_09_18.py | 2938 | `0b7e50a8a036` | R |
| 20 | _september_workspace\results\_archive_2026_09_20\_deposon_v2scripts_reverify_worker_2026_09_18.py | 34134 | `18984b04c45e` | R |
| 21 | _september_workspace\results\_archive_2026_09_20\_final_sha_2026_09_18.py | 2678 | `0769f60a0504` | R |
| 22 | _september_workspace\results\_archive_2026_09_20\_fix_batch2_2026_09_18.py | 4100 | `81bb1751be4c` | R |
| 23 | _september_workspace\results\_archive_2026_09_20\_fix_batch3_2026_09_18.py | 3207 | `01e63e488ce2` | R |
| 24 | _september_workspace\results\_archive_2026_09_20\_fix_batch4_2026_09_18.py | 8225 | `2efcd5ff42f1` | R |
| 25 | _september_workspace\results\_archive_2026_09_20\_fix_batch6_2026_09_18.py | 2214 | `1c59e7b803fe` | R |
| 26 | _september_workspace\results\_archive_2026_09_20\_fix_batch7_2026_09_18.py | 4261 | `389283c51275` | R |
| 27 | _september_workspace\results\_archive_2026_09_20\_fix_batch8_2026_09_18.py | 2249 | `5057ccf97d6b` | R |
| 28 | _september_workspace\results\_archive_2026_09_20\_fix_d05_rescue_2026_09_18.py | 3524 | `2c2cc3ff542a` | R |
| 29 | _september_workspace\results\_archive_2026_09_20\_ftfb_pass2_results_limitations_audit_2026_09_17.md | 11390 | `5610a549e116` | R |
| 30 | _september_workspace\results\_archive_2026_09_20\_letter_to_coze_online_v2_2026_09_18.md | 18611 | `dc3e56adc3fc` | R |
| 31 | _september_workspace\results\_archive_2026_09_20\_letter_to_coze_paper_v1_委托_2026_09_17.md | 12813 | `f4610b0bb47c` | R |
| 32 | _september_workspace\results\_archive_2026_09_20\_letter_to_glm_ftfb_deep_revision_2026_09_18.md | 26990 | `3de722dc9e39` | R |
| 33 | _september_workspace\results\_archive_2026_09_20\_letter_to_kimi_push_v3_final_2026_09_17.md | 10307 | `affe5eebf2e7` | R |
| 34 | _september_workspace\results\_archive_2026_09_20\_letter_to_kimi_push_v3_final_v2_2026_09_17.md | 13967 | `6d95317f4355` | R |
| 35 | _september_workspace\results\_archive_2026_09_20\_letter_to_kimi_push_v3_委托_2026_09_17.md | 13592 | `05f92d837412` | R |
| 36 | _september_workspace\results\_archive_2026_09_20\_letter_to_kimi_upload_requirements_2026_09_18.md | 22591 | `8b22a026f30b` | R |
| 37 | _september_workspace\results\_archive_2026_09_20\_letter_to_mavis_full_mirror_request_2026_09_17.md | 9717 | `f2934e5279e6` | R |
| 38 | _september_workspace\results\_archive_2026_09_20\_letter_to_trae_code_2026_09_17_final.md | 10702 | `b75ba5c152b7` | R |
| 39 | _september_workspace\results\_archive_2026_09_20\_openrouter_emb_runner.bak.note | 5 | `f01a374e9c81` | R |
| 40 | _september_workspace\results\_archive_2026_09_20\_p_i_curvature_audit_probe_runner_2026_09_16.py | 12919 | `e05555deb611` | R |
| 41 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase1_finalize.log | 1184 | `c2172607419e` | R |
| 42 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase1_runner.log | 8202 | `90ead4a9fba8` | R |
| 43 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_closedsource_runner.log | 2370 | `37e1f9cc19d3` | R |
| 44 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_closedsource_runner_v2_20260917_171640.log | 1516 | `77b62d39f474` | R |
| 45 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_closedsource_runner_v2_20260917_172440_gpt56sol.log | 865 | `fefdac35fa6e` | R |
| 46 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_closedsource_runner_v2_20260917_172928_gpt56sol.log | 955 | `ef172ad159b4` | R |
| 47 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_closedsource_runner_v2_20260917_173159_gpt56sol.log | 2765 | `a6517028a720` | R |
| 48 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_closedsource_runner_v2_20260917_174011_claude_sonnet5.log | 2687 | `0ffa261c5ed8` | R |
| 49 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_closedsource_runner_v2_20260917_175003_gemini_37flash.log | 2342 | `0b61aadb4509` | R |
| 50 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_finalize.log | 2712 | `4a707293fada` | R |
| 51 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_finalize_20260917_142748.log | 1224 | `995bad3cce30` | R |
| 52 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_glm53.log | 2542 | `11f8ec231ead` | R |
| 53 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_glm53_only_20260917_142011.log | 1140 | `4c91156dc821` | R |
| 54 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_or_embedding.err | 530 | `4346e7e916db` | R |
| 55 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_or_embedding.log | 564 | `bb54209b0cdc` | R |
| 56 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_or_embedding_v3_2026_09_17.console.log | 10102 | `4056814f73dc` | R |
| 57 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_probe.log | 3100 | `b1128aa5441c` | R |
| 58 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_probe_agent.log | 6760 | `49765ca671d8` | R |
| 59 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_probe_emb.log | 2046 | `456a6bf39f9e` | R |
| 60 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_probe_emb_proxy_v2.log | 17632 | `b4d2803c6290` | R |
| 61 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_probe_ext.log | 4992 | `a72a38a9fb6f` | R |
| 62 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_probe_gpt4o.log | 3462 | `d9bf12a6f713` | R |
| 63 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_runner.log | 3416 | `9b4cdb0ec25b` | R |
| 64 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console.log | 6134 | `1f65ad49911c` | R |
| 65 | _september_workspace\results\_archive_2026_09_20\_p_l_v3_phase2_vector_emb_doubao_2026_09_17.console2.log | 2925 | `fcca7035073a` | R |
| 66 | _september_workspace\results\_archive_2026_09_20\_probe_doubao_4versions_diff_2026_09_17.json | 1393 | `49dde3059959` | R |
| 67 | _september_workspace\results\_archive_2026_09_20\_probe_doubao_4versions_diff_2026_09_17.py | 2720 | `93527eb7b2f7` | R |
| 68 | _september_workspace\results\_archive_2026_09_20\_probe_doubao_emb_direct_2026_09_17.py | 2371 | `9bcfe80c0dd0` | R |
| 69 | _september_workspace\results\_archive_2026_09_20\_probe_doubao_emb_via_proxy_2026_09_17.py | 2589 | `f2818fc2ddff` | R |
| 70 | _september_workspace\results\_archive_2026_09_20\_probe_teamo_via_proxy.log | 4526 | `74badfd3270f` | R |
| 71 | _september_workspace\results\_archive_2026_09_20\_probe_teamo_via_proxy.py | 2841 | `dce965058076` | R |
| 72 | _september_workspace\results\_archive_2026_09_20\_reviewer_a_audit_tmp.py | 4397 | `268225ccbb76` | R |
| 73 | _september_workspace\results\_archive_2026_09_20\_sanity_openai_more.log | 1444 | `c7db5599e6a5` | R |
| 74 | _september_workspace\results\_archive_2026_09_20\_sanity_openai_more.py | 2187 | `e11319f32dc5` | R |
| 75 | _september_workspace\results\_archive_2026_09_20\_sanity_teamo_one.py | 2119 | `63eb0a0aa102` | R |
| 76 | _september_workspace\results\_archive_2026_09_20\_sanity_teamo_three.log | 2168 | `e6e40a339ef7` | R |
| 77 | _september_workspace\results\_archive_2026_09_20\_sanity_teamo_three.py | 3540 | `888d02cd1443` | R |
| 78 | _september_workspace\results\_archive_2026_09_20\_teamorouter_smoke_tmp.json | 277 | `4181a24c9ca1` | R |
| 79 | _september_workspace\results\_archive_2026_09_20\_temp_volc_test.py | 6687 | `264f2bf5a3f2` | R |
| 80 | _september_workspace\results\_archive_2026_09_20\_test_3bb_vary.log | 11522 | `699d751ced17` | R |
| 81 | _september_workspace\results\_archive_2026_09_20\_tmp_inspect_22cap.py | 675 | `0c9addf4a70f` | R |
| 82 | _september_workspace\results\_archive_2026_09_20\_tmp_inspect_5model.py | 1029 | `048ebc99177c` | R |
| 83 | _september_workspace\results\_archive_2026_09_20\_tmp_probe_archive | 1270 | `a6689025804c` | R |
| 84 | _september_workspace\results\_archive_2026_09_20\_v2_stage1_60cells.console.log | 17158 | `cd7710002ff0` | R |
| 85 | _september_workspace\results\_archive_2026_09_20\_v2_stage3_f3_strip.console.log | 2440 | `0087364298e1` | R |
| 86 | _september_workspace\results\_archive_2026_09_20\_v3x_6way_finalize.log | 618 | `1db3842e21e6` | R |
| 87 | _september_workspace\results\_archive_2026_09_20\_v3x_6way_run.log | 8952 | `0a2e66649663` | R |
| 88 | _september_workspace\results\_archive_2026_09_20\_v3x_6way_stage3_minimal.log | 1678 | `a8a69c85571c` | R |
| 89 | _september_workspace\results\_archive_2026_09_20\_v3x_6way_stage3_recovery.log | 2242 | `1758b615ebb1` | R |
| 90 | _september_workspace\results\_archive_2026_09_20\_v41_flash_rag_baseline_run.log | 17456 | `7b659fdc69c9` | R |
| 91 | _september_workspace\results\_archive_2026_09_20\_v41_flash_rag_baseline_run.log.bak | 6106 | `18b56e3d1c7b` | R |
| 92 | _september_workspace\results\_archive_2026_09_20\_v41_flash_rag_partial.bak.json | 88584 | `b0e2673f4a56` | R |
| 93 | _september_workspace\results\_archive_2026_09_20\_volc_22cap_emb.log | 9068 | `27cb6630ec37` | R |
| 94 | _september_workspace\results\_archive_2026_09_20\_worker_openrouter_rag_run.log | 6476 | `9a5603811f45` | R |
| 95 | _september_workspace\results\_archive_2026_09_20\compile_verification.txt | 9663 | `463fc7575663` | R |
| 96 | _september_workspace\results\_archive_2026_09_20\deposon_d_fix2_metric_verify_9m60c_2026_09_15.log | 24634 | `1eec8b03b30f` | R |
| 97 | _september_workspace\results\_archive_2026_09_20\deposon_deepseek_v41_flash_30cells_2026_09_10.log | 6514 | `cbcecdec0fdb` | R |
| 98 | _september_workspace\results\_archive_2026_09_20\deposon_dpath_cross_modal_2026_09_10.log | 8885 | `95298ca6d95e` | R |
| 99 | _september_workspace\results\_archive_2026_09_20\deposon_dpath_cross_modal_runner_2026_09_10.stdout.log | 17772 | `388439eb8d17` | R |
| 100 | _september_workspace\results\_archive_2026_09_20\deposon_feshbach_rag_30cells_2026_09_10.log | 6887 | `2e8564b94b02` | R |
| 101 | _september_workspace\results\_archive_2026_09_20\deposon_v2_phase1_60cells_2026_09_11.log | 8578 | `b5169e715434` | R |
| 102 | _september_workspace\results\_archive_2026_09_20\deposon_v2_phase2_f2_2026_09_11.log | 1272 | `c0fa485cd9fe` | R |
| 103 | _september_workspace\results\_archive_2026_09_20\deposon_v2_phase3_f3_2026_09_11.log | 1247 | `3b61b7028cc8` | R |
| 104 | _september_workspace\results\_archive_2026_09_20\deposon_v2_phase4_f4_2026_09_11.log | 1064 | `86812e1003e5` | R |
| 105 | _september_workspace\results\_archive_2026_09_20\deposon_v2_phase5_f5_2026_09_11.log | 1092 | `af736aa656c7` | R |
| 106 | _september_workspace\results\_archive_2026_09_20\deposon_v41_flash_60cells_v2_2026_09_10.log | 12470 | `ad7fafb3582b` | R |
| 107 | _september_workspace\results\_archive_2026_09_20\deposon_volcengine_minimax_m3_30cells_2026_09_10.log | 3444 | `a0fc4423470c` | R |
| 108 | _september_workspace\results\_archive_2026_09_20\deposon_volcengine_seed_code_30cells_2026_09_10.log | 7342 | `19f295ce9ff9` | R |
| 109 | _september_workspace\results\_archive_2026_09_20\deposon_volcengine_worker_b_2026_09_10.log | 3326 | `5d40bdc3a0db` | R |
| 110 | _september_workspace\results\_archive_2026_09_20\deposon_volcengine_worker_c_2026_09_10.log | 5869 | `e62cd7fd2a0e` | R |
| 111 | _september_workspace\results\_archive_2026_09_20\deposon_volcengine_worker_c_2026_09_10.run.log | 12070 | `644425852b1a` | R |
| 112 | _september_workspace\results\_archive_2026_09_20\fiction_that_feeds_back.pdf | 356123 | `2d9edc8c7303` | R |
| 113 | _september_workspace\results\_archive_2026_09_20\fiction_that_feeds_back.tex | 93324 | `d060f75dbe9f` | R |
| 114 | _september_workspace\results\_archive_2026_09_20\fiction_that_feeds_back_source.md | 84388 | `543479649b3e` | R |
| 115 | _september_workspace\results\_archive_2026_09_20\ftfb_pass1_background_methodology_audit_2026_09_17.md | 8257 | `7243192d86be` | R |
| 116 | _september_workspace\results\_archive_2026_09_20\gpt6_30cells_run.log | 4220 | `74bbc7dcf5aa` | R |
| 117 | _september_workspace\results\_archive_2026_09_20\gpt6_30cells_run.log.err | 0 | `e3b0c44298fc` | R |
| 118 | _september_workspace\results\_archive_2026_09_20\LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md | 10586 | `ff37f39264bc` | R |
| 119 | _september_workspace\results\_archive_2026_09_20\LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md | 13295 | `00e5d185ef74` | R |
| 120 | _september_workspace\results\_archive_2026_09_20\LETTER_TO_TRAE_2026_09_11.md | 22820 | `b09251018102` | R |
| 121 | _september_workspace\results\_archive_2026_09_20\LETTER_TO_TRAE_FIX_SELFCHECK_2026_09_15.md | 7855 | `c0d629df69d8` | R |
| 122 | _september_workspace\results\_archive_2026_09_20\LETTER_TO_TRAE_REVIEW_2026_09_16.md | 12671 | `c086c84e04a6` | R |
| 123 | _september_workspace\results\_archive_2026_09_20\p_i_curvature_audit_probe_results_2026_09_16.json | 2637 | `ae07f5551e87` | R |
| 124 | _september_workspace\results\_archive_2026_09_20\review_content_A1_dsv4pro.md | 20082 | `5198a7059c06` | R |
| 125 | _september_workspace\results\_archive_2026_09_20\review_content_A1_glm51.md | 7617 | `fd38a2a1ea05` | R |
| 126 | _september_workspace\results\_archive_2026_09_20\review_content_A2_kimik3.md | 24843 | `a964defb923d` | R |
| 127 | _september_workspace\results\_archive_2026_09_20\review_tech_B1_dsv4pro.md | 30494 | `0d36d7cd0589` | R |
| 128 | _september_workspace\results\_archive_2026_09_20\review_tech_B1_grok46.md | 18923 | `09784ff172b3` | R |
| 129 | _september_workspace\results\_archive_2026_09_20\review_tech_B2_grok46.md | 13726 | `fe80bad08eef` | R |
| 130 | _september_workspace\results\_archive_2026_09_20\review_tech_B2_qwen3max.md | 8098 | `8d00c6d4a242` | R |
| 131 | _september_workspace\results\_archive_2026_09_20\REVIEWER_B_TMP_RERUN_2026_09_15.md | 21654 | `ceb8f595a911` | R |
| 132 | _september_workspace\results\_archive_2026_09_20\SHA256_MANIFEST.txt | 552 | `416dda94cb63` | R |
| 133 | _september_workspace\results\_archive_2026_09_20\TRAE_CODE_FIX_LIST_2026_09_18.md | 9343 | `ace3c6b390cb` | R |
| 134 | _september_workspace\results\_archive_2026_09_20\TRAE_DAILY_AUDIT_LETTER_2026_09_18.md | 11575 | `0011b7924dfb` | R |
| 135 | _september_workspace\results\_archive_2026_09_20\TRAE_FIX_RECEIPT_2026_09_18.md | 4784 | `2e6a31af5e4b` | R |
| 136 | _september_workspace\results\_archive_2026_09_20\volcengine_glm_latest_30cells_v2_run_2026_09_10.log | 4091 | `d2f7840ebc51` | R |
| 137 | _september_workspace\results\_archive_2026_09_20\volcengine_glm_latest_30cells_v2_run_2026_09_10.log.err | 0 | `e3b0c44298fc` | R |
| 138 | _september_workspace\results\_archive_2026_09_20\戴夫_FTFB双审包简报v3_2026-09-17.md | 8419 | `6952b3b02b96` | R |
| 139 | _september_workspace\results\_coze_online_v3_2026_09_18.md | 7476 | `53c9c1ab2d12` | R |
| 140 | _september_workspace\results\_coze_online_v3_d7format_2026_09_18.md | 8727 | `debe3761c565` | R |
| 141 | _september_workspace\results\_coze_online_v3_final_2026_09_18.md | 11660 | `36439bc12bba` | R |
| 142 | _september_workspace\results\_coze_online_v4_d7format_2026_09_26.pdf | 465366 | `a82881653520` | R |
| 143 | _september_workspace\results\_coze_paper_v1_draft_2026_09_17.md | 29511 | `2832800ceca6` | R |
| 144 | _september_workspace\results\_coze_paper_v1_summary_2026_09_17.md | 3624 | `2efdc3d7741d` | R |
| 145 | _september_workspace\verifier\volcengine_补测_worker_A_2026_09_10.py | 16252 | `20b8a2f54ad9` | R |
| 146 | letters\_v5_rj5_external_rederive_reply_codex_2026_09_29.md | 27835 | `c706e69d00fc` | R |
| 147 | results\_d05_sanity_3backbone_20260918_100110.json | 2292 | `0a1e91d6f772` | R |
| 148 | results\_trae_anchor_18_audit_20260917_193000.md | 3449 | `4af67e6cbe71` | R |
| 149 | results\_trae_corpus_5_audit_20260917_193000.md | 3467 | `f2a655cd5e54` | R |
| 150 | results\_trae_d7_v1_audit_20260917_190000.json | 4253 | `3184b30b7b0d` | R |
| 151 | results\_trae_d7_v1_audit_20260917_190000.md | 7863 | `41c142eab4a1` | R |
| 152 | results\_trae_kimi_push_v3_audit_20260917_193000.md | 3281 | `8ece24be6b8a` | R |
| 153 | results\_trae_paper_8ch_双审_20260917_200000.md | 4044 | `145abbb9c365` | R |
| 154 | results\attacker_xl_cache\algorithm_process.json | 5353 | `1878428d3c90` | R |
| 155 | results\attacker_xl_cache\biological_taxonomy.json | 5036 | `8e11c03b11cf` | R |
| 156 | results\attacker_xl_cache\geography_world.json | 5314 | `3977f0ab6a28` | R |
| 157 | results\attacker_xl_cache\historical_causality.json | 4389 | `9d4b5a29decf` | R |
| 158 | results\attacker_xl_cache\physics_concepts.json | 5874 | `9ca7c11860f6` | R |
| 159 | results\attacker_xl_cache\project_management.json | 4541 | `e19e1137258e` | R |
| 160 | results\deposon_benchmark_v1_3_labelfree.json | 3011 | `57f06a426bec` | R |
| 161 | results\deposon_benchmark_v1_3_resonant.json | 3134 | `769ae8c908c9` | R |
| 162 | results\deposon_benchmark_v1_4_sc5.json | 12479 | `c9796d3b3263` | R |
| 163 | results\deposon_g3_arrhenius.json | 2284 | `a3de045b5dd7` | R |
| 164 | results\deposon_v16_llm_prior_summary.json | 5517 | `a7952d9d78db` | R |
| 165 | results\deposon_v20_familyL_ingest.json | 1304 | `d7c2d9fee5b2` | R |
| 166 | results\Deposon_评估汇总_v1_3_0.json | 2811 | `2f02f50c164b` | R |
| 167 | results\familyL_cache\algorithm_process.json | 1442 | `611f346091b9` | R |
| 168 | results\familyL_cache\biological_taxonomy.json | 1296 | `1a6bf80e22ca` | R |
| 169 | results\familyL_cache\geography_world.json | 1319 | `d5afc69e2fb3` | R |
| 170 | results\familyL_cache\historical_causality.json | 1622 | `db30c0e7bd33` | R |
| 171 | results\familyL_cache\physics_concepts.json | 1253 | `9963951cf859` | R |
| 172 | results\familyL_cache\project_management.json | 1346 | `48faa9bf14fa` | R |
| 173 | results\familyL_prior_cache\algorithm_process.json | 2061 | `b302e5f54141` | R |
| 174 | results\familyL_prior_cache\biological_taxonomy.json | 2231 | `8014873eee66` | R |
| 175 | results\familyL_prior_cache\geography_world.json | 2314 | `7056a5298bff` | R |
| 176 | results\familyL_prior_cache\historical_causality.json | 3034 | `6e032f3a58ac` | R |
| 177 | results\familyL_prior_cache\physics_concepts.json | 2596 | `9eae1fa8fd7c` | R |
| 178 | results\familyL_prior_cache\project_management.json | 1895 | `3467c1985133` | R |
| 179 | results\gt2_attacker_cache\algorithm_process.json | 2783 | `7ad7b97486e8` | R |
| 180 | results\gt2_attacker_cache\biological_taxonomy.json | 2386 | `f7c9a3344c54` | R |
| 181 | results\gt2_attacker_cache\historical_causality.json | 2342 | `b9f8f472b2f9` | R |
| 182 | results\gt2_attacker_cache\physics_concepts.json | 2387 | `ec91290fbddc` | R |
| 183 | results\gt3_prior_cache\deepseek-v4-pro-260425__algorithm_process.json | 3315 | `fb255ad93ec9` | R |
| 184 | results\gt3_prior_cache\deepseek-v4-pro-260425__biological_taxonomy.json | 2564 | `d50690ff2279` | R |
| 185 | results\gt3_prior_cache\deepseek-v4-pro-260425__geography_world.json | 2847 | `7830ece1d516` | R |
| 186 | results\gt3_prior_cache\deepseek-v4-pro-260425__historical_causality.json | 2851 | `d556c647747d` | R |
| 187 | results\gt3_prior_cache\deepseek-v4-pro-260425__physics_concepts.json | 2176 | `8bc5467ced92` | R |
| 188 | results\gt3_prior_cache\deepseek-v4-pro-260425__project_management.json | 2083 | `23863deac9a3` | R |
| 189 | results\gt3_prior_cache\doubao-seed-evolving__algorithm_process.json | 498 | `3e0173feb34d` | R |
| 190 | results\gt3_prior_cache\doubao-seed-evolving__biological_taxonomy.json | 2362 | `f6db5e6b980f` | R |
| 191 | results\gt3_prior_cache\doubao-seed-evolving__geography_world.json | 2475 | `4925ec2a5ca1` | R |
| 192 | results\gt3_prior_cache\doubao-seed-evolving__historical_causality.json | 501 | `aedf8a050cb3` | R |
| 193 | results\gt3_prior_cache\doubao-seed-evolving__physics_concepts.json | 2013 | `6dd47c33fb27` | R |
| 194 | results\gt3_prior_cache\doubao-seed-evolving__project_management.json | 1719 | `ebae449cf921` | R |
| 195 | results\gt3_prior_cache\kimi-k2-thinking__algorithm_process.json | 479 | `669da0e1c36b` | R |
| 196 | results\gt3_prior_cache\kimi-k2-thinking__biological_taxonomy.json | 2350 | `51746e4094dc` | R |
| 197 | results\gt3_prior_cache\kimi-k2-thinking__geography_world.json | 2499 | `29cce1102bba` | R |
| 198 | results\gt3_prior_cache\kimi-k2-thinking__historical_causality.json | 2500 | `9506ad922380` | R |
| 199 | results\gt3_prior_cache\kimi-k2-thinking__physics_concepts.json | 2006 | `bd828a9e748b` | R |
| 200 | results\gt3_prior_cache\kimi-k2-thinking__project_management.json | 480 | `540a9ef09bf0` | R |
| 201 | results\gt3_prior_cache\moonshot-v1-8k__algorithm_process.json | 2737 | `b0dc14fac249` | R |
| 202 | results\gt3_prior_cache\moonshot-v1-8k__biological_taxonomy.json | 2324 | `769991471ad1` | R |
| 203 | results\gt3_prior_cache\moonshot-v1-8k__geography_world.json | 2495 | `b7cce4938263` | R |
| 204 | results\gt3_prior_cache\moonshot-v1-8k__historical_causality.json | 2649 | `202e2e38a573` | R |
| 205 | results\gt3_prior_cache\moonshot-v1-8k__physics_concepts.json | 2540 | `6081c483c999` | R |
| 206 | results\gt3_prior_cache\moonshot-v1-8k__project_management.json | 478 | `8896856f7e65` | R |
| 207 | results\llm_prior_cache.json | 938 | `5f16be89efc5` | R |
| 208 | results\llm_prior_cache_v18_contamination.json | 639 | `d3f72f67977d` | R |
| 209 | results\llm_prior_cache_v18_contentless.json | 512 | `7c0d169ef164` | R |
| 210 | results\llm_prior_cache_v18_direction.json | 2168 | `023f936f80fb` | R |
| 211 | results\llm_prior_cache_v18_direction_run1_malformed_archive.json | 655 | `d5526e712e99` | R |
| 212 | results\llm_prior_cache_v18_labelshuffle.json | 1925 | `8dce6d7618a2` | R |
| 213 | results\MANIFEST_large_files.md | 3816 | `b138fb94ca71` | R |
| 214 | results\v19_edges_audit_input.csv | 2186 | `8b6682181392` | R |
| 215 | results\v20_graph_features.csv | 2151 | `f95f382ace44` | R |
| 216 | results\v20_regression_field_v2.json | 4236 | `3596490e1fc0` | R |
| 217 | results\v20_statcheck_fm_vs_deg.json | 988 | `dfe014c627ca` | R |
| 218 | results\v20_statcheck_fm_vs_rand.json | 868 | `1dadfaeb2c43` | R |

### §3-4 上传集 与 远端轨 之交（**0**）

- 上传集 2,415 件 与 远端轨 218 件 之**同名**交 ＝ **4** 件；其中 **BYTES 亦相等者 ＝ 0**、**SHA-12 相等者 ＝ 0** ⇒ **四件皆「同名而内容已变」**（远端轨为旧版，本地为新版）：

| 上传集序 | 上传集件（本地） | BYTES／SHA-12 | 远端轨件 | BYTES／SHA-12 |
|--:|:--|:--|:--|:--|
| 1679 | `results/_coze_paper_v1_draft_2026_09_17.md` | 29,484／`c08e7abf5ee3` | `_september_workspace\results\_coze_paper_v1_draft_2026_09_17.md` | 29,511／`2832800ceca6` |
| 1647 | `results/_archive_2026_09_18/_trae_d7_v1_audit_20260917_190000.md` | 7,855／`e240ca712be6` | `results\_trae_d7_v1_audit_20260917_190000.md` | 7,863／`41c142eab4a1` |
| 1648 | `results/_archive_2026_09_18/_trae_paper_8ch_双审_20260917_200000.md` | 4,040／`bec666969ffc` | `results\_trae_paper_8ch_双审_20260917_200000.md` | 4,044／`145abbb9c365` |
| 2083 | `results/manifest_large_files.md` | 3,440／`e0dc7a8e4c75` | `results\MANIFEST_large_files.md` | 3,816／`b138fb94ca71` |

⇒ **在册上传集与远端轨现存镜像之同字节交 ＝ 0** ⇒ **上传尚未发生**。此与在册远端读数（「镜像区外可见仓仅 414 件·`pushed_at` 2026-10-18T15:02:52Z」）**同向而不等同**：彼为远端全树之旧读数、**照录·非本棒自测**；本棒**⛔0 联网**核远端现值。

---

## §4 与 `R8` 之 15 行（实 14 具名）之对应

### §4-1 那 15 行从何处来

`results\_full_inventory_export_v2_2026_10_24.md`（**103,521／`11eb13d33d69`**）§2 之索引面中，路径以 `.tmp\` 开头者 **15 行**（本棒逐行回读确认）⇒ `R8` 之呈现面读数「未成就（命中 15 行）」（同件 §3-1 **L403**、§3-6 **L486**）。其中 `#141` 与 `#162` **系同一文件**（`.tmp\ea_sha12.json`·289,347／`381dd57aaca4`）⇒ **15 行 ＝ 14 具名**。
📌 PI `v283` §2-2 **L47–L57** 所载「14 名」之字面，本棒**开卷核其节号**；⚠ 该件之指纹本棒**未自测** ⇒ 该处标「**在册值·非本棒自测**」。

### §4-2 逐件核（14 具名逐件）

> 判据 ＝ §1-3 (B2)：**仓根 `.tmp\` 下之件不入上传集**（该口径之**分母**即已去仓根 `.tmp`）。另：§3-2 之 2,415 件清单中**路径含任何 `.tmp\` 者 ＝ 0**（本棒逐行实核）⇒ **双证**。

| # | 具名（相对仓根） | 底本序 | BYTES | SHA-12 | 本棒现测（2026-10-25） | 判 |
|--:|:--|--:|--:|:--|:--|:-:|
| 1 | `.tmp\_cleanup_empty_dirs_2026_10_24.py` | #7 | 2,038 | `420034e3c370` | 在盘·2,038／`420034e3c370`·相符 | **不入** |
| 2 | `.tmp\_find_844179898102_2026_10_24.py` | #8 | 1,565 | `e32a44c35655` | 在盘·1,565／`e32a44c35655`·相符 | **不入** |
| 3 | `.tmp\_empty_dirs_manifest2_2026_10_24.json` | #28 | 148 | `26a4edfa2977` | 在盘·148／`26a4edfa2977`·相符 | **不入** |
| 4 | `.tmp\_t1_qwen_temp_sweep_r2_records.json` | #66 | 1,795,870 | `bb511e7b0baf` | 在盘·1,795,870／`bb511e7b0baf`·相符 | **不入** |
| 5 | `.tmp\_t1_qwen_temp_sweep_records.json` | #67 | 96,866 | `5b51af62c640` | 在盘·96,866／`5b51af62c640`·相符 | **不入** |
| 6 | `.tmp\_w_measure_summary.txt` | #123 | 10,838 | `6de52927d93d` | 在盘·10,838／`6de52927d93d`·相符 | **不入** |
| 7 | `.tmp\_w_probe1.out.txt` | #124 | 15,525 | `cf8ff3b25f6f` | 在盘·15,525／`cf8ff3b25f6f`·相符 | **不入** |
| 8 | `.tmp\_w_probe4.out.txt` | #125 | 1,215 | `a2146b87248b` | 在盘·1,215／`a2146b87248b`·相符 | **不入** |
| 9 | `.tmp\_w_tables_for_register.txt` | #126 | 8,021 | `5893140f2167` | 在盘·8,021／`5893140f2167`·相符 | **不入** |
| 10 | `.tmp\_w_verify_eta_preexp_2026_10_20.txt` | #127 | 7,391 | `5d3a4389f52b` | 在盘·7,391／`5d3a4389f52b`·相符 | **不入** |
| 11 | `.tmp\_write_probe2_2026_10_20.txt` | #128 | 58 | `4cf027dc1d90` | 在盘·58／`4cf027dc1d90`·相符 | **不入** |
| 12 | `.tmp\_write_probe_2026_10_20.txt` | #129 | 14 | `64c0e0c777df` | 在盘·14／`64c0e0c777df`·相符 | **不入** |
| 13 | `.tmp\ea_sha12.json` | #141／#162（**两行同一件**） | 289,347 | `381dd57aaca4` | 在盘·289,347／`381dd57aaca4`·相符 | **不入** |
| 14 | `.tmp\pk_t5lock_verify_2026_10_15.json` | #175 | 4,931 | `0b9c36f612da` | 在盘·4,931／`0b9c36f612da`·相符 | **不入** |

⇒ **14／14 判「不入」**，**0 件「不可判」**。

### §4-3 后果（明书）

1. **`R8` 实体面之放行条件成立**：PI 裁 134 之辨明果所写死之放行条件为「**三集划分件出时核『必上传集 ∩ 仓根 `.tmp` ＝ ∅』**」⇒ 本件之实测 ＝ **∅ 成立**（上传集 2,415 件 ∩ 仓根 `.tmp` 面 ＝ **0**；14 具名 0 入）。
2. **实体面之凭今由「仅在册口径」升为「有名单之凭」**：本件即该凭之实体。⚠ **惟**：本件**未**裁「实体面已成就」——**成就与否归 `verdict-keeper`／PI**；本棒⛔0 代裁、⛔0 落五终判。
3. **呈现面不动**：那 15 行**仍留档**、`R8` 之「未成就」**维持**（PI `v283` 已裁之呈现面处置）⇒ 本件**不使呈现面成就、亦不使其失准**；实体面与呈现面**两读并存**（同向而不等同）。
4. **⚠ 在册之悬置**：底本 v2 §9-3 附记⑤ **L751** 载「删该 15 行 ＋ 连带勘正 ＝ 乙态 216→201、合计 254→239…」之改法**已备而未行**（⛔0 擅删）⇒ 本棒**⛔0 代裁**其行否；**呈现面 15 行之去留仍为候 PI 面**（§5-U3）。
5. **⚠ 上传集之缺口（§5-U1／U2）**：本件之 2,415 件基线**测点为 2026-10-22 23:19**；此后新增之件（含底本 v2 本身、`R8` 辨明件、**本件**）**不在基线内** ⇒ 实体面之放行**以「基线 ∩ 仓根 `.tmp` ＝ ∅」为凭则成立**；**以「当态上传面 ∩ 仓根 `.tmp` ＝ ∅」为凭则本棒未核**（当态上传面须重演分类器·本棒⛔0 重演）。**此即实体面之凭之唯一缺口**，列 §5-U1 候 PI 裁。

---

## §5 未定面（候 PI 裁 · 本棒判不了者）

| # | 面 | 现值（本棒自测） | 为何本棒判不了 | 代价不对称 |
|:--|:--|:--|:--|:--|
| **U-1** | **当态上传面是否须重算**（基线测点 2026-10-22 23:19 之后新增之件） | 现行分母 ＝ **4,034**（repo 去仓根 `.tmp` **2,759** ＋ sub **1,275**）；基线覆盖 **2,415** ⇒ **1,619 件现于分母而不在基线内** | 重算须**重演分类器**（22 类 × 裁决序 × 滚动在途闸 × HF-A…HF-M × 加严①②）⇒ **新仪器、必有口径漂移风险**；且 HF-D（隐私面 10 件）之清单**在册未给**（清单件 §3-4 **L112**：源只给件数不给路径，且明禁以文件名反推） | **重算**：得当态全名单，但须新出分类器＋PI 另给 HF-D 清单（**多花**：PI 一轮给值＋一棒仪器自审）｜**不重算**：以基线为准（**少花**），但实体面之凭存 1,619 件之缺口（**少花而欠确**） |
| **U-2** | **1,619 件之归属**（应入上传面／被闸剔出） | 本棒**未判** | 同 U-1（分类器未重演） | 本棒径给即等于**代裁口径** ⇒ ⛔0 |
| **U-3** | **呈现面 15 行之去留**（底本 v2 §9-3 附记⑤ 之改法已备未行） | 未行 | 删之违 PI 明令之语（「索引面 ⛔0 删任何树内具名·254 具名全列」）；留之违 `R8` 要件 ⇒ **两条 PI 令正面相抵**（R8 辨明件 §3-2 已定性） | **删**：连带改写 8 处计数（**多花**且动 PI 明令之语）｜**留**：维持「未成就」明记（**少花**，即 PI `v283` 之甲案） |
| **U-4** | **HF-D（隐私面 10 件）** | 未计入（清单件 §3-4 **L112**：源只给件数不给路径，且明禁以文件名反推） | 须 PI 给**逐件清单** | **PI 给清单**：上传面至多再减 10 件（**少花**）｜**不给**：隐私面留存于面上（**欠确**且违禁传语） |
| **U-5** | **HF-K（当日审计／登记 5 件）** | 其中 **4 件在本棒上传集内**（清单件 §3-4 **L113** 自陈「**本件列之，须 PI 核**」） | 源文载「**推荐排除**」而**非硬禁** ⇒ 归 PI | **PI 裁**：可剔 4 件（**多花**一轮裁）｜**不裁**：4 件照传（**少花**） |
| **U-6** | **母件式 2,415 vs 字面式 2,610**（PI 定 5 类 ＝ D-REPORT／D-PLAN／X-REVIEW／E-EVID／M-MEDIA 之去留） | 两数并报（§1-5） | 在册明载「⛔ 0 择一而不言」⇒ **须 PI 择** | **取母件式**：**少 195 件**（留而不传·可逆）｜**取字面式**：**多 195 件**（PI 定 5 类随传） |
| **U-7** | **归档集与本地留存集之名单** | 未出 | 须 C 类归档索引（`bg_b9f342c6`）并读；归档区本棒**仅计数与按名·指纹认人**、⛔0 读其正文 | **出**：可成完整三集（**多花**一棒）｜**不出**：上传集之名单**已足 R8 实体面之需**（三集之另二集**非本件之射程**） |
| **U-8** | **上传时点与远端写** | ⛔0 代定（清单件 §3-6-2 **L500** 明载「⛔ **0 代定**」） | 远端写之权归 PI | — |
| **U-9** | **本件之生效** | **待 PI 复核生效，生效即锁** | 预登记／名单类件须 PI 复核 | — |

---

## §6 构造面 vs 真实面（外推边界声明）

- **构造面 ＝** 在册上传面清单 §4 之 2,415 件（测点 2026-10-22 23:19:29）＋ 本棒 2026-10-25 之现测指纹；远端轨 218 件（拉回时点 2026-10-17）之按名与指纹。
- **外推边界 ＝ 构造域**：⛔0 外推至 10-22 之后新增之件（1,619 件之归属未判）｜⛔0 外推至仓根 `.tmp` 面（**仅计数与按名·指纹认人**）｜⛔0 外推至归档区正文（**⛔0 读**）｜⛔0 外推至 `GLM` 面（**⛔0 读·⛔0 取指纹**）｜⛔0 外推至远端现值（**⛔0 联网**）｜⛔0 外推至任何**未登记之构造变更**。

---

## §7 老实交代（限制面 · ⛔0 软化）

1. **本棒为回棒复活**：本会话于 2026-10-25 约 11:0x 断连；PI 实测 `results\` 按名 `*upload_set*` **0 命中**（件未落盘）⇒ 本件为**断连后之续作**，**非重作**：§3 名单之逐件实测（2,415 件逐一复算指纹，耗时 **321.9 s**）于断连**前**已测毕并留存于本机 `%TEMP%`（2 件中间表），本棒于断连后据此**续作**并于落盘前**复核**（§3-2 之 2,415/2,415 指纹相符为复核后之果）。⚠ **如实登记**：断连期间盘上有并发变动（裁 135 之「整理之刀」分批删 `.tmp` 之 `.py`／`.txt`）⇒ 仓根件数 10:47 实测 7,778、11:0x 后复测 7,710；**本件之名单 2,415 件则全部不受影响**。
2. **本棒自陈二处脚本缺陷（均已修，且均经复核）**：(i) 首轮逐件测量之 BYTES 列因 PowerShell 字符串插值之 `"$b.Length"` 未取属性（落成字节数组之串接）而**作废**；**SHA-12 之比较不受影响**（该比较用 `$hex.Substring(0,12)`，非插值）⇒ 「2,415／2,415 指纹逐位相符」之结论**始终成立**；BYTES 已以 `Get-Item .Length` 全部重取。(ii) 名单注入时**末列误填现测态之 `ON` 而非来源面之 `L`**（取值位错一格）⇒ 已于呈件前全量改正并逐行复核（末列计数：`L` **2,415**／`R` 0／`ON` 残留 **0**）。**此二处皆为本棒自身之工具面缺陷，⛔0 涉任何在册件一字之改。**
3. **本件之名单非自建仪器之产出**：名单取**在册基线**（`_upload_face_manifest_2026_10_22.md` §4 之 2,415 行）并**逐件现测**其现址／BYTES／SHA-12；本棒**⛔0 重演分类器**（22 类 × 裁决序 × 滚动在途闸 × HF-A…HF-M × 加严①②）⇒ 「在册基线」与「当态上传面」**两者本棒未合**，其差即 §5-U-1／U-2。
4. **阴性断言以射程为界**：§2 之「按名 0 命中」之射程 ＝ 四根共 **155,694** 件（实枚举）；**⛔0** 断言仓外任何位置、任何未枚举之命名空间之状况；「三集划分」之**内容面**（非按名面）于在册**多处命中**（如 PI `v231` L76 逐字载其待办）⇒ **本件之断言只限「以该名为名之件」**，**⛔0** 扩读为「在册无三集之判读」（该判读**有**，见 §2-4）。
5. **「`R8`」有二义**：本仓 `R8` 既指**合规要件**（`.tmp` 已排除）又指**物理 `pair_code`**（R8 辨明件 §2 未栏载 `reversal_pair.pair_code` ＝ `R8`）⇒ 本件凡引 `R8` **一律指合规要件**；且本棒**未以裸搜 `R8` 定位任何件**（全部按路径开卷回读）。
6. **归档区与 `GLM`**：归档区 40,242 件本棒**仅计数与按名·指纹认人**、**⛔0 读其正文**；`GLM` 面本棒**零触及**（⛔0 读·⛔0 取指纹）。
7. **远端现值未核**：⛔0 联网 ⇒ 远端 `zeroandcat/Deposon` 之**现值**（推时点／commit／树形）本棒**未核**；§3-3 之 218 件系**本地拉回留痕**（时点 2026-10-17），**非远端现状**；在册远端读数系**照录·非本棒自测**。
8. **禁供面**：本件**⛔0** 载任何 `correct`／`value` 原值、答案哈希、排名、统计量；§3 之逐件列**不含**任何逐格原值（仅路径／字节数／指纹／分类／远端目标路径）。
9. **⛔0 回改**：本件**未改**任何既有件一字；**未移动／重命名／删除**任一既有件；**未新建目录**；**唯一新件 ＝ 本件**（预定名 `results\work\process\_upload_set_roster_2026_10_25.md`，落盘前 `Test-Path` ＝ **False**，**未撞名**、故**不启用 `_b` 后缀**）。
10. **中间件**：逐件实测之 **3 件**中间表落于**本机 `%TEMP%`**（**仓外**，非仓内；其中一件为首轮测量之 375 MB 之 CSV）⇒ 仓内件数不增；本件落盘并核验后**已逐件经可恢复删除通道（`rm --` → mavis-trash）移出**（`%TEMP%` 内 `deposon_upset_*` 残留 **0**）。
11. **在册件指纹之新旧**：本件所引各件之 BYTES／SHA-12 **皆本棒自测**；唯 `pi_rulings\_pi_card_answers_register_2026_10_24_v283.md` 之「14 名」之字面，本棒**开卷核其节号而未自测其指纹** ⇒ 该处标「在册值·非本棒自测」。⚠ 树之在册指纹（247,218／`599252c058e4`）**已过期**——本棒实测 `results\work\process\_experiment_tree_v2_main_2026_10_23.md` ＝ **269,980／`cd4261dfb051`**。
12. **本件不裁任何事**：⛔0 落五终判｜⛔0 闭 `KD`｜⛔0 宣告段毕或门槛成就｜⛔0 代 PI 裁「实体面是否成就」「归档集／本地留存集之去留」「上传时点」「PI 定 5 类之择」「HF-D 清单」「HF-K 4 件之剔」——以上**一律候 PI 裁**，并已附代价不对称（§5）。
13. **本件之状态**：**已落盘 · 呈 PI 复核**（**待 PI 复核生效，生效即锁**）——本棒**未**宣告任何成就。

---

## §8 本件之自核（落盘后实测）

- 字节自检：`.tmp\_bcheck.py`（`python -P`）实测 → **见本棒之回报面**（BYTES／SHA-12／BOM／CR／VT／FFFD／末字节）。
- 参照件（`tools\exp_harness.py`）本棒实测 ＝ 45,590／`ce64b9b97489`（同一性正控，⛔0 引用在册值充自测值）。

---

**状态行**：`上传集名单件 · 2,415 件（母件式读 2,415／字面式读 2,610）· 14 具名 0 入（仓根 `.tmp` ∩ 上传集 ＝ ∅）· 待 PI 复核生效，生效即锁`
**落款**：主代理之口径棒 `protocol-keeper` · 2026-10-25 11:40 UTC+8 · ⛔0 代 PI 裁 · ⛔0 落五终判 · ⛔0 闭 KD
