# _deliverable_pack_v2_manifest_2026_10_21（可转交面 v2 之打包清单 · GLM 面之自解压脚本形态）

> **状态栏（贯穿全件）**：📄 **件性质**＝「能给的」可转交面 v2 之打包清单（新立件 · 与自解压脚本同面存于 `results/`）｜**打包轮**＝deposon 执行官 worker（PI v190-Q3 三令之执行棒 · 2026-10-21 16:3x–17:0x UTC+8）｜**令源**＝PI v190-Q3 Other 栏逐字「皆入包，此外远端仓库里有的文件请移出并标注远端路径，此外GLM接受内嵌压缩包的自解压脚本而不接受压缩包」（登记件 `c095262efd43`）｜**v2 之形**＝**自解压脚本**（内嵌压缩包 · 非压缩包本体）｜**载荷**＝**92 件**｜**归档条目**＝**93 条**（载荷 92 ＋ 本清单 1）｜**包指纹**＝`45930381276adc5dc6f4434b201527b69171a66064fccaa4592c63c309f6bb2f`（定义见 §8·载荷射径·0 自指）｜**纪律**＝⛔ 0 移动/0 重命名/0 删除/0 覆写任何既有件（v1 之 zip 与清单件**原处不动**）｜⛔ 0 传出任何件（传出之径归 PI）｜⛔ 0 代裁｜⛔ 0 落五终判｜⛔ 0 闭任何 KD｜⛔ 0 宣告段毕｜⛔ 0 新建目录于仓内｜**编码**：本清单 UTF-8 无 BOM · 纯 LF · 0 TAB｜**本件自身指纹 0 自写入**（落盘后实测随回执回报）｜**脚本本体指纹 0 自写入**（脚本内嵌本清单 ⇒ 循环不可自写·落盘后实测随回执回报）

---

## §0 一句话结论

v2 之包已出，**其形为自解压脚本**（PI v190-Q3 Other 栏令③）：`results\_deliverable_pack_v2_selfextract_2026_10_21.py` ——**单一可执行脚本文件**，其体内**内嵌** v2 载荷之压缩包（base64 之 ASCII 面），收件方（GLM）**运行该脚本即得**全部内容，**0 需接受压缩包本体**。载荷 **92 件**（＝v1 之载荷 91 − 移出 1 ＋ PI 令入包之两候选回函件 2 ＝ 92；其中 `letters/` 面 91 件 ＋ 脑图本体 1 件）＋**本清单** ＝ **归档条目 93**；归档载荷合计 2,385,602 B；每件 SHA-12／bytes／行数／mtime 于入包前**实测**并载于 §4；**93/93 字节级复制复验全等**（解包后逐件对原件比对·见 §10）；**敏感面预筛 0 真凭据**（§9）；**远端已有件 1 件已移出并标注其远端路径**（§5）；⛔ 0 移动/0 重命名/0 删除任何既有件·0 传出·0 代裁·0 落五终判·0 闭 KD·0 宣告段毕。

---

## §1 令源回读（逐字 · 指纹**本棒自测** · 观测时点 2026-10-21 16:47:49 UTC+8）

| 项 | 值 |
| :-- | :-- |
| **令源件** | `pi_rulings\_pi_card_answers_register_2026_10_21_v190.md` |
| **令源件 SHA-12／bytes**（本棒实测） | `c095262efd43` ／ 7,104 B |
| **卡号／requestId** | v190 ／ `ask_d303ed69e375a82740960cee` |
| **Q3 之答（Other 栏·selectedOther=true）逐字** | 「**皆入包，此外远端仓库里有的文件请移出并标注远端路径，此外GLM接受内嵌压缩包的自解压脚本而不接受压缩包**」 |
| **登记件 §2-3 之界分面（逐字要点）** | ①两候选回函件皆入包 ②远端仓库（GitHub zeroandcat/Deposon）里有之文件请移出（自包移出）并标注远端路径（核之径：本地镜像面 `_remote_pullback_2026_10_17`（其时点之注记须带）＋（若须现值）GitHub API 匿名只读核验之径（已验·0 写远端））③打包之形之改：自解压脚本（内嵌压缩包）｜⚠ 已落之 zip（`f4fe63437144`）之面之存续（⛔ 0 删已落之 zip · 其留废之裁归 PI） |

> 📌 **回读纪律**：上之令源逐字系**派工单所转录**与**登记件 §2-3 之照录**之对读（本棒亲读 `c095262efd43` 之 Q3 与 §2-3）——**0 转述即信**；登记件之 SHA-12／bytes 系**本棒自测**（派工单所载 `c095262efd43`／7,104 B 之**复测吻合**）。

---

## §2 三令之执行面（逐令 → 本棒之执行 · 每令皆载其口径与界分）

### §2-1 令①「皆入包」→ 两候选回函件皆入包（2 件）

| # | 件名（包内相对路径） | 原路径 | SHA-12 | bytes | 行数 | mtime | 远端面 | 入包之据 |
| :-: | :-- | :-- | :-- | --: | --: | :-- | :-- | :-- |
| 2 | `letters/REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` | `_repo_mirror/doc/letter/REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` | `597caf8ba5bc` | 30,459 | 318 | 2026-10-17 15:54:08 | **远端 0 命中**（同名 0 · 字节全等 0） | PI v190-Q3 Other 栏令①·候选乙 |
| 40 | `letters/_reply_eta_candidate_values_copilot_2026_10_20.md` | `_repo_mirror/doc/letter/_reply_eta_candidate_values_copilot_2026_10_20.md` | `f4845fffc44f` | 10,151 | 100 | 2026-10-20 11:31:47 | **远端 0 命中**（同名 0 · 字节全等 0） | PI v190-Q3 Other 栏令①·候选甲 |

> 📌 **口径之变（v1 → v2）之载明**：此二件在 **v1 清单 §5 排除台账**中分别列于 **#32**（`_reply_eta_candidate_values_copilot_2026_10_20.md`·E3 受托方来函）与 **#6**（`REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md`·E3 受托方来函）——**PI v190-Q3 令①明令二者皆入包** ⇒ **该二项排除判准（E3）于本 v2 对此二件不再适用**；其余 E3 排除面（余 13 件）**存续不变**。⛔ 0 回改 v1 清单（其件原处不动·**0 覆写**）——本面以**本清单之载明**承载其变。
> 📌 **受托方称谓两层分辨之戒（存续）**：`copilot` ＝ **agent 名**；其**模型面**——件内自述「Exact serving model / version / build identifier: **not exposed to this session**」⇒ **0 断言其模型面**（本棒 0 以单名定位其模型面）。
> 📌 **0 断言**：本棒 0 核该二件之内容语义之正确性（⛔ 0 判其候选值之对否·0 判其理论输入之当否）——**件之识认依 PI 令之称名**。

### §2-2 令②「远端仓库里有的文件请移出并标注远端路径」→ 移出 1 件 · 逐件载其远端路径

| # | 件名 | SHA-12 | bytes | 远端仓库 | 远端分支 | 远端路径（**标注**） | 远端 blob sha1 | 远端 bytes | 对位之据 |
| :-: | :-- | :-- | --: | :-- | :-- | :-- | :-- | --: | :-- |
| 1 | `letters/_codex_theory_derivation_reply_2026_09_30.md` | `7558eb1a5e34` | 71,002 | `zeroandcat/Deposon` | `main` | **`letters/_codex_theory_derivation_reply_2026_09_30.md`** | `25e6b4ea2f144c67e9be31c7fecd2874cba486bd` | 71,002 | **字节全等对位**（本地 git blob sha1 ＝ 远端 blob sha1） |

> 📌 **移出 ≠ 远端之删除**：令②之「移出」＝**自本包之载荷中移出**（其实体**仍在远端仓库**·**0 删远端**·**0 改远端**）；PI 2026-10-18 在册之「远端根层遗留面全留不删」之裁**存续**。
> 📌 **本棒之动作面**：**0 触达远端之写面**（远端仅经匿名只读 GET 核验·见 §7）；被移出件之**本地原件**（`letters\` 面）**原处不动·0 移动·0 重命名·0 删除**——**移出仅作用于包之构成面**。

### §2-3 令③「GLM接受内嵌压缩包的自解压脚本而不接受压缩包」→ v2 之形＝自解压脚本

| 项 | 值 |
| :-- | :-- |
| **形** | **单一 `.py` 脚本文件**（`results\_deliverable_pack_v2_selfextract_2026_10_21.py`）——其体内**内嵌**载荷之 **deflate 压缩包之 base64 文本** |
| **形之择（理由）** | ①**跨平台**（GLM 侧环境未知·非 Windows 亦可运行）②**0 执行策略依赖**（PowerShell 之 `.ps1` 于受件方可能受执行策略阻断·`.py` 无此面）③**仅标准库**（`base64`／`zipfile`／`hashlib`／`argparse`·0 第三方依赖）④**脚本面可读可核**（头注与自解压逻辑为纯文本·载荷段为 base64 之 ASCII 面） |
| **备择形（候 PI 核·本棒未采）** | `.ps1`（Windows 原生·但受件方执行策略之风险·且 PowerShell 5.1 与 7 之语法面有别） |
| **收件方之用法** | `python <脚本> --dest <目录>`（默认目录 `./deposon_v2_deliverable_pack_2026_10_21`）｜`--list`（列条目）｜`--verify-only`（0 落盘·仅校验内嵌载荷与逐条索引之自洽） |
| **自校验** | 脚本内**逐条索引**（每条目之 sha256 ＋ bytes）＋内嵌载荷整体之 sha256／bytes；解包时**逐条复算并与索引比对**，任一不符即以非零码退出 |

---

## §3 口径之沿革（v1 → v2 · 变与不变逐条）

| 面 | v1（`_deliverable_pack_manifest_2026_10_21.md`） | v2（本件） |
| :-- | :-- | :-- |
| **形** | 单一 zip 压缩档本体 | **自解压脚本（内嵌压缩包）**——PI v190-Q3 令③所改 |
| **载荷口径** | 判准甲（对外函面）＋乙（版本链/同族并列）＋丙（未毕·除锚定例外）＋丁（敏感面） | **沿袭**（PI 未改口径）＋**令①**覆 E3 之二项 |
| **入包件数** | 91 | **92**（91 − 1 移出 ＋ 2 令①） |
| **包指纹定义** | 载荷射径·0 自指·`相对路径|sha256[:12]|bytes` 逐行 LF 拼接后取 sha256（§7） | **同一定义**（§8）——**本棒以 v1 之载荷复算得 `cdaa5e10cfa09677d315666c7dcf2f5cbf080826863afd68e8c9644b2fdd7ee8` ＝ v1 清单所载 `cdaa5e10cfa0`（吻合·口径实现之自检）** |
| **排除台账** | §5 逐件列判 51 件（`letters/` 全量 141 ＝ 90 ＋ 51） | **沿袭 v1 之台账**（E1/E2/E3 之余 13／E4/E5/E7/E8 等）＋**令①覆除二项**＋**令②移出一项**⇒ 本 v2 入包 92 件 · 余 `letters/` 面 51 件仍 0 入包（其中含本次入包之二候选回函件） |
| **远端面** | 0 核（⛔ 0 联网） | **已核**（匿名只读 GET·见 §7）＋**移出 1 件** |

---

## §4 载荷件逐件清单（92 件 · 入包前逐件实测 · 93/93 字节级复验全等）

> 📌 **列义**：「包内相对路径」＝归档内之条目路径｜「原路径」＝仓内只读源之绝对路径｜SHA-12 ＝ SHA-256 于**磁盘全文字节**取前 12 位小写十六进制｜mtime ＝ 本地 UTC+8 · 秒级｜「入包之据」＝该件于所采口径之归属面。

| # | 包内相对路径 | 原路径 | SHA-12 | bytes | 行数 | mtime | 入包之据 |
| :-: | :-- | :-- | :-- | --: | --: | :-- | :-- |
| 1 | `G-30-a_脑图_AI应当如何思考_从仿生向到仿物理向_2026_10_21.jpg` | `〔本地绝对路径·脱敏略:15-37-23-553-asset_20261021-153723-553_9845154a984c_d069cedf-7498.jpg〕` | `9845154a984c` | 68,553 | 133 | 2026-10-21 15:37:23 | PI 2026-10-21 15:4x 令所供脑图本体（G-30-a／H-5 之缺件之补）·v1 载荷沿袭 |
| 2 | `letters/REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` | `_repo_mirror/doc/letter/REPLY_FROM_COPILOT_AGENT_T2_T3_THEORY_INPUTS_2026_10_17.md` | `597caf8ba5bc` | 30,459 | 318 | 2026-10-17 15:54:08 | PI v190-Q3 Other 栏令①·候选乙 |
| 3 | `letters/_alignment_reply_crossface_three_items_2026_10_12.md` | `_repo_mirror/doc/letter/_alignment_reply_crossface_three_items_2026_10_12.md` | `08b036588198` | 7,892 | 77 | 2026-10-12 20:44:03 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 4 | `letters/_approval_letter_kimi_pre_execution_2026_10_18.md` | `_repo_mirror/doc/letter/_approval_letter_kimi_pre_execution_2026_10_18.md` | `87a61f5ecc41` | 7,958 | 67 | 2026-10-18 10:28:22 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 5 | `letters/_c4_theory_scan_reply_claude_code_2026_09_30.md` | `_repo_mirror/doc/letter/_c4_theory_scan_reply_claude_code_2026_09_30.md` | `2166b37e5d2a` | 27,894 | 299 | 2026-09-30 21:51:00 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 6 | `letters/_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | `_repo_mirror/doc/letter/_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | `f4defae83553` | 22,064 | 197 | 2026-10-11 23:40:53 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 7 | `letters/_clue_book_v06_backfill_2026_10_18.md` | `_repo_mirror/work/note/_clue_book_v06_backfill_2026_10_18.md` | `88a4d800d485` | 12,896 | 149 | 2026-10-18 17:38:49 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 8 | `letters/_codex_c4_values_followup_reply_2026_10_10.md` | `_repo_mirror/doc/letter/_codex_c4_values_followup_reply_2026_10_10.md` | `97a35f8ae94c` | 4,490 | 31 | 2026-10-10 16:02:26 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 9 | `letters/_codex_c4_values_reply_2026_10_10.md` | `_repo_mirror/doc/letter/_codex_c4_values_reply_2026_10_10.md` | `8e4972352291` | 13,378 | 91 | 2026-10-10 13:49:24 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 10 | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | `_repo_mirror/review/review/_codex_c4_values_unblock_reply_2026_10_10.md` | `a975c7990cd8` | 21,486 | 143 | 2026-10-10 17:35:08 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 11 | `letters/_commission_c4_values_EN_2026_10_10.md` | `_repo_mirror/review/review/_commission_c4_values_EN_2026_10_10.md` | `a397621085d6` | 56,217 | 367 | 2026-10-10 13:14:46 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 12 | `letters/_commission_c4_values_EN_differences_exits_note_2026_10_10.md` | `_repo_mirror/doc/readme/_commission_c4_values_EN_differences_exits_note_2026_10_10.md` | `b20f25a66267` | 7,817 | 74 | 2026-10-10 13:15:32 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 13 | `letters/_commission_c4_values_followup_EN_2026_10_10.md` | `_repo_mirror/work/note/_commission_c4_values_followup_EN_2026_10_10.md` | `abe0652ab00f` | 7,583 | 69 | 2026-10-10 14:31:49 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 14 | `letters/_commission_c4_values_unblock_EN_2026_10_10.md` | `_repo_mirror/work/note/_commission_c4_values_unblock_EN_2026_10_10.md` | `fde64a863b09` | 10,244 | 83 | 2026-10-10 17:17:35 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 15 | `letters/_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md` | `_repo_mirror/doc/readme/_commission_c4_values_unblock_EN_differences_exits_note_2026_10_10.md` | `1c769e28f8f5` | 3,139 | 27 | 2026-10-10 17:17:46 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 16 | `letters/_commission_closeout_pack_paper_2026_10_09_v0.1.md` | `_repo_mirror/doc/paper/_commission_closeout_pack_paper_2026_10_09_v0.1.md` | `60e41b588d36` | 31,838 | 280 | 2026-10-12 10:22:09 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 17 | `letters/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` | `_repo_mirror/work/note/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` | `8b15f0957e0f` | 82,016 | 418 | 2026-09-30 21:55:05 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 18 | `letters/_commission_coze_〔IM〕_closeout_pack_2026_10_12.md` | `_repo_mirror/work/note/_commission_coze_〔IM〕_closeout_pack_2026_10_12.md` | `7818cfe2d226` | 26,816 | 251 | 2026-10-12 21:18:56 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 19 | `letters/_commission_eta_candidate_values_2026_10_20.md` | `_repo_mirror/work/note/_commission_eta_candidate_values_2026_10_20.md` | `e1526315c193` | 33,394 | 264 | 2026-10-20 10:46:19 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 20 | `letters/_commission_eta_candidate_values_EN_2026_10_20.md` | `_repo_mirror/review/review/_commission_eta_candidate_values_EN_2026_10_20.md` | `26a26c11b916` | 47,591 | 269 | 2026-10-20 11:08:40 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 21 | `letters/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | `_repo_mirror/doc/paper/_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` | `758e1ef3de27` | 53,344 | 447 | 2026-10-01 21:19:36 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 22 | `letters/_commission_glm_dualtrack_paper_v0.7_2026_10_18.md` | `_repo_mirror/doc/paper/_commission_glm_dualtrack_paper_v0.7_2026_10_18.md` | `07e068165dd5` | 70,048 | 573 | 2026-10-18 18:09:24 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 23 | `letters/_commission_glm_supplement_509_repair_v0.4_2026_10_18.md` | `_repo_mirror/work/note/_commission_glm_supplement_509_repair_v0.4_2026_10_18.md` | `591d5ee04d92` | 59,400 | 429 | 2026-10-18 20:07:33 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 24 | `letters/_commission_glm_theory_derivation_2026_09_30.md` | `_repo_mirror/work/note/_commission_glm_theory_derivation_2026_09_30.md` | `344f5b9e0b08` | 32,472 | 285 | 2026-09-30 19:49:06 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 25 | `letters/_commission_kimi_upload_with_d7_2026_10_09_v0.3.md` | `_repo_mirror/work/note/_commission_kimi_upload_with_d7_2026_10_09_v0.3.md` | `ae00f6fee19e` | 36,763 | 390 | 2026-10-12 09:59:43 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 26 | `letters/_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | `_repo_mirror/work/note/_commission_pending_pi_gaps_closeout_EN_2026_10_11.md` | `0ce066e5eb3f` | 22,685 | 122 | 2026-10-11 22:27:45 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 27 | `letters/_commission_t2_t3_theory_inputs_2026_10_17.md` | `_repo_mirror/work/note/_commission_t2_t3_theory_inputs_2026_10_17.md` | `393d71e51fbf` | 22,746 | 173 | 2026-10-17 15:05:39 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 28 | `letters/_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md` | `_repo_mirror/work/note/_commission_t2_t3_theory_inputs_copilot_agent_2026_10_17.md` | `385003e41ce2` | 23,919 | 176 | 2026-10-17 15:15:10 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 29 | `letters/_commission_t2_t3_theory_inputs_grok_2026_10_17.md` | `_repo_mirror/work/note/_commission_t2_t3_theory_inputs_grok_2026_10_17.md` | `6922929bfda8` | 23,906 | 176 | 2026-10-17 15:15:10 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 30 | `letters/_commission_trae_dfamily_original_text_request_2026_10_12.md` | `_repo_mirror/work/note/_commission_trae_dfamily_original_text_request_2026_10_12.md` | `23bd2366e798` | 13,767 | 159 | 2026-10-12 16:02:26 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 31 | `letters/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | `_repo_mirror/work/note/_commission_trae_direct_fix_oct_full_coverage_2026_10_12.md` | `60751abbeb3b` | 46,077 | 332 | 2026-10-12 03:18:02 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 32 | `letters/_dualtrack_paper_clue_book_v0.7_local_remote_2026_10_18.md` | `_repo_mirror/doc/paper/_dualtrack_paper_clue_book_v0.7_local_remote_2026_10_18.md` | `882309257b0f` | 69,901 | 506 | 2026-10-18 18:32:08 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 33 | `letters/_final_rulings_compilation_kimi_2026_10_18.md` | `_repo_mirror/verdict/pi/_final_rulings_compilation_kimi_2026_10_18.md` | `832e69eb49a4` | 37,950 | 309 | 2026-10-18 15:45:50 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 34 | `letters/_glm_commission_reply_request_2026_10_13.md` | `_repo_mirror/doc/paper/_glm_commission_reply_request_2026_10_13.md` | `2992b3917050` | 22,328 | 209 | 2026-10-13 09:31:53 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 35 | `letters/_kimi_v4_t12_review_2026_09_20.md` | `_repo_mirror/review/review/_kimi_v4_t12_review_2026_09_20.md` | `38070fd12f31` | 6,644 | 80 | 2026-09-20 14:53:18 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 36 | `letters/_kimi_v4_theme_reply_2026_09_20.md` | `_repo_mirror/doc/letter/_kimi_v4_theme_reply_2026_09_20.md` | `3e37352efb4b` | 7,372 | 45 | 2026-09-20 17:52:32 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 37 | `letters/_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md` | `_repo_mirror/doc/letter/_kimi_v4_theme_reply_2_brainstorm_2026_09_20.md` | `bc14f47d927d` | 14,155 | 62 | 2026-09-20 21:11:34 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 38 | `letters/_letter_to_kimi_predecessor_history_invitation_2026_10_19.md` | `_repo_mirror/doc/letter/_letter_to_kimi_predecessor_history_invitation_2026_10_19.md` | `660b5e10cac3` | 6,267 | 62 | 2026-10-19 20:07:49 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 39 | `letters/_oct_full_coverage_reply_trae_code_2026_10_12.md` | `_repo_mirror/doc/letter/_oct_full_coverage_reply_trae_code_2026_10_12.md` | `d11d75ba6236` | 23,978 | 194 | 2026-10-12 12:31:43 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 40 | `letters/_reply_eta_candidate_values_copilot_2026_10_20.md` | `_repo_mirror/doc/letter/_reply_eta_candidate_values_copilot_2026_10_20.md` | `f4845fffc44f` | 10,151 | 100 | 2026-10-20 11:31:47 | PI v190-Q3 Other 栏令①·候选甲 |
| 41 | `letters/_reply_to_glm_dualtrack_v156_rulings_2026_10_20.md` | `_repo_mirror/verdict/pi/_reply_to_glm_dualtrack_v156_rulings_2026_10_20.md` | `3ea469e5a6f3` | 31,609 | 303 | 2026-10-20 15:59:50 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 42 | `letters/_reply_to_kimi_pre_execution_2026_10_18.md` | `_repo_mirror/doc/letter/_reply_to_kimi_pre_execution_2026_10_18.md` | `abc8280b088c` | 17,182 | 179 | 2026-10-18 10:39:34 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 43 | `letters/_supplement_collision_10_overwrite_2026_10_18.md` | `_repo_mirror/doc/letter/_supplement_collision_10_overwrite_2026_10_18.md` | `72ae90de30aa` | 35,436 | 190 | 2026-10-18 12:24:38 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 44 | `letters/_supplement_consolidated_desensitized_upload_2026_10_18.md` | `_repo_mirror/doc/letter/_supplement_consolidated_desensitized_upload_2026_10_18.md` | `557d61c1eb5a` | 57,539 | 314 | 2026-10-18 12:26:06 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 45 | `letters/_supplement_g4_closure_face23_2026_10_18.md` | `_repo_mirror/doc/letter/_supplement_g4_closure_face23_2026_10_18.md` | `412e5263d27a` | 26,016 | 132 | 2026-10-18 12:18:01 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 46 | `letters/_supplement_rename_and_third_batch_2026_10_18.md` | `_repo_mirror/work/note/_supplement_rename_and_third_batch_2026_10_18.md` | `77962d9b64de` | 35,246 | 288 | 2026-10-18 14:57:20 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 47 | `letters/_supplement_s3_s5_deletion_2026_10_18.md` | `_repo_mirror/doc/letter/_supplement_s3_s5_deletion_2026_10_18.md` | `a0958089dbe3` | 25,293 | 138 | 2026-10-18 11:55:45 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 48 | `letters/_trae_dfamily_original_text_reply_2026_10_12.md` | `_repo_mirror/doc/letter/_trae_dfamily_original_text_reply_2026_10_12.md` | `ce91320d4f28` | 48,304 | 393 | 2026-10-12 17:32:26 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 49 | `letters/_trae_direct_fix_reply_trae_code_2026_10_12.md` | `_repo_mirror/doc/letter/_trae_direct_fix_reply_trae_code_2026_10_12.md` | `f37ebc80d1df` | 21,379 | 222 | 2026-10-12 01:34:03 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 50 | `letters/_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | `_repo_mirror/doc/letter/_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | `dda07ad77910` | 42,948 | 479 | 2026-09-27 20:43:21 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 51 | `letters/_v3_recheck_indep_judgment_request_2026_09_27.md` | `_repo_mirror/verdict/judge/_v3_recheck_indep_judgment_request_2026_09_27.md` | `2c486c1791d5` | 22,702 | 210 | 2026-09-27 16:18:21 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 52 | `letters/_v4_acceptance_coze_2026_09_20.md` | `_repo_mirror/work/note/_v4_acceptance_coze_2026_09_20.md` | `b2bf2a073ac8` | 5,467 | 70 | 2026-09-20 14:58:15 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 53 | `letters/_v4_acceptance_trae_code_2026_09_20.md` | `_repo_mirror/work/note/_v4_acceptance_trae_code_2026_09_20.md` | `3e2f1c84e86d` | 7,746 | 98 | 2026-09-30 16:14:47 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 54 | `letters/_v4_acceptance_trae_work_v1.0_2026_09_20.md` | `_repo_mirror/work/note/_v4_acceptance_trae_work_v1.0_2026_09_20.md` | `3caf4e653a68` | 7,176 | 73 | 2026-09-20 17:36:19 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 55 | `letters/_v4_attribution_errata_trae_work_2026_09_20.md` | `_repo_mirror/work/note/_v4_attribution_errata_trae_work_2026_09_20.md` | `e061c5806af6` | 2,816 | 41 | 2026-09-20 17:36:48 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 56 | `letters/_v4_commission_inventory_anchor_note_2026_09_29.md` | `_repo_mirror/doc/letter/_v4_commission_inventory_anchor_note_2026_09_29.md` | `849f8eba5bf0` | 2,655 | 30 | 2026-09-29 13:25:03 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 57 | `letters/_v4_commission_kimi_fullupload_w3_2026_09_30.md` | `_repo_mirror/work/note/_v4_commission_kimi_fullupload_w3_2026_09_30.md` | `84c2f4aa9691` | 16,404 | 228 | 2026-09-30 19:41:29 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 58 | `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md` | `_repo_mirror/doc/paper/_v4_commission_paper_final_glm_2026_09_24_v4.md` | `d5337702cec9` | 31,531 | 294 | 2026-09-26 21:25:21 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 59 | `letters/_v4_commission_upload_channel_authorization_2026_09_26.md` | `_repo_mirror/work/note/_v4_commission_upload_channel_authorization_2026_09_26.md` | `5e5479bfc453` | 26,937 | 288 | 2026-09-26 19:50:59 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 60 | `letters/_v4_commission_upload_channel_authorization_reply_kimi_2026_09_26.md` | `_repo_mirror/doc/letter/_v4_commission_upload_channel_authorization_reply_kimi_2026_09_26.md` | `f8f4ae2e7b9b` | 11,575 | 106 | 2026-09-26 20:04:44 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 61 | `letters/_v4_commission_upload_executor_2026_09_24_v3.md` | `_repo_mirror/work/note/_v4_commission_upload_executor_2026_09_24_v3.md` | `c20d4f58f5c8` | 25,091 | 258 | 2026-09-26 19:20:04 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 62 | `letters/_v4_commission_upload_executor_reply_v3_2026_09_24.md` | `_repo_mirror/doc/letter/_v4_commission_upload_executor_reply_v3_2026_09_24.md` | `50592e36ecad` | 9,848 | 98 | 2026-09-26 19:35:40 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 63 | `letters/_v4_commission_upload_executor_reply_v3_exec_2026_09_26.md` | `_repo_mirror/doc/letter/_v4_commission_upload_executor_reply_v3_exec_2026_09_26.md` | `631bb517f79d` | 4,471 | 55 | 2026-09-26 19:53:10 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 64 | `letters/_v4_commission_〔IM〕_report_coze_2026_10_18_v5_draft_r3.md` | `_repo_mirror/doc/report/_v4_commission_〔IM〕_report_coze_2026_10_18_v5_draft_r3.md` | `94d03c4aaa9b` | 29,420 | 321 | 2026-10-18 20:42:27 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 65 | `letters/_v4_commission_〔IM〕_report_coze_reply_v4_2026_09_24.md` | `_repo_mirror/doc/letter/_v4_commission_〔IM〕_report_coze_reply_v4_2026_09_24.md` | `c60dfd7c0f45` | 16,471 | 180 | 2026-09-26 22:20:19 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 66 | `letters/_v4_d1_response_workbuddy_2026_09_20.md` | `_repo_mirror/work/note/_v4_d1_response_workbuddy_2026_09_20.md` | `bc663b671994` | 14,881 | 158 | 2026-09-20 14:36:48 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 67 | `letters/_v4_d1_review_codex_2026_09_20.md` | `_repo_mirror/review/review/_v4_d1_review_codex_2026_09_20.md` | `48387412b109` | 4,506 | 46 | 2026-09-21 11:12:20 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 68 | `letters/_v4_distillation_acceptance_coze_2026_09_20.md` | `_repo_mirror/work/note/_v4_distillation_acceptance_coze_2026_09_20.md` | `3a8cb7b9d041` | 14,295 | 80 | 2026-09-20 18:03:55 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 69 | `letters/_v4_distillation_acceptance_kimi_2026_09_20.md` | `_repo_mirror/work/note/_v4_distillation_acceptance_kimi_2026_09_20.md` | `a4d194dbf9ad` | 6,454 | 53 | 2026-09-20 17:56:29 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 70 | `letters/_v4_distillation_acceptance_trae_code_2026_09_20.md` | `_repo_mirror/work/note/_v4_distillation_acceptance_trae_code_2026_09_20.md` | `dc47fbf3c491` | 5,218 | 49 | 2026-09-20 17:32:33 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 71 | `letters/_v4_distillation_brainstorm_reply_codex_2026_09_21.md` | `_repo_mirror/doc/letter/_v4_distillation_brainstorm_reply_codex_2026_09_21.md` | `0ff6c042b845` | 9,048 | 39 | 2026-09-21 11:12:20 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 72 | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | `_repo_mirror/work/note/_v4_distillation_invitation_2026_09_20_v1.0.md` | `e4b00fa97d03` | 54,784 | 421 | 2026-09-30 16:14:47 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 73 | `letters/_v4_distillation_reply_claude_code_2026_09_20.md` | `_repo_mirror/doc/letter/_v4_distillation_reply_claude_code_2026_09_20.md` | `d39cb17b051b` | 64,212 | 393 | 2026-09-21 11:01:14 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 74 | `letters/_v4_distillation_reply_coze_2026_09_20.md` | `_repo_mirror/doc/paper/_v4_distillation_reply_coze_2026_09_20.md` | `00593014cbd3` | 71,084 | 459 | 2026-09-20 21:53:15 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 75 | `letters/_v4_distillation_reply_trae_code_2026_09_20.md` | `_repo_mirror/doc/letter/_v4_distillation_reply_trae_code_2026_09_20.md` | `e87ec8f7e2fe` | 43,570 | 187 | 2026-09-20 21:21:36 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 76 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | `_repo_mirror/review/review/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | `9bb22099db3b` | 28,207 | 245 | 2026-09-23 13:35:13 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 77 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md` | `_repo_mirror/review/review/_v4_distillation_reply_trae_code_v3_review_2026_09_23_fix_addendum.md` | `59b8df6e2e22` | 6,067 | 73 | 2026-09-23 13:46:15 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 78 | `letters/_v4_distillation_theme_reply_workbuddy_2026_09_20.md` | `_repo_mirror/doc/letter/_v4_distillation_theme_reply_workbuddy_2026_09_20.md` | `e3fe63a2f708` | 18,785 | 170 | 2026-09-20 18:19:48 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 79 | `letters/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md` | `_repo_mirror/doc/letter/_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md` | `cdb27cd3008c` | 13,553 | 106 | 2026-09-21 09:42:45 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 80 | `letters/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` | `_repo_mirror/doc/letter/_v4_distillation_theme_reply_workbuddy_part2_2026_09_20.md` | `bfb4932f4467` | 12,963 | 140 | 2026-09-20 18:26:36 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 81 | `letters/_v4_experiment_invitation_2026_09_20_v0.2.md` | `_repo_mirror/doc/plan/_v4_experiment_invitation_2026_09_20_v0.2.md` | `72fc2e7fb098` | 43,024 | 481 | 2026-09-30 16:14:47 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 82 | `letters/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | `_repo_mirror/review/review/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | `f88e429717aa` | 13,263 | 114 | 2026-09-30 16:14:47 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 83 | `letters/_v4_ide_track_review_trae_work_2026_09_20.md` | `_repo_mirror/review/review/_v4_ide_track_review_trae_work_2026_09_20.md` | `21d384cf3422` | 7,488 | 70 | 2026-09-20 17:35:40 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 84 | `letters/_v4_review_claude_code_2026_09_20.md` | `_repo_mirror/review/review/_v4_review_claude_code_2026_09_20.md` | `b6f9956bcf5c` | 7,004 | 55 | 2026-09-20 14:32:01 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 85 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md` | `_repo_mirror/doc/letter/_v4_theme_reply_mavis_2026_09_20_v1.2.md` | `f1d73c82511d` | 38,087 | 223 | 2026-09-30 16:14:47 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 86 | `letters/_v4_theme_reply_trae_work_2026_09_20_v1.2.md` | `_repo_mirror/doc/letter/_v4_theme_reply_trae_work_2026_09_20_v1.2.md` | `6bee6ec434bd` | 28,395 | 141 | 2026-09-20 20:58:07 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 87 | `letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | `_repo_mirror/doc/letter/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md` | `f86b8b6c8ed2` | 60,139 | 615 | 2026-09-27 20:13:23 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 88 | `letters/_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` | `_repo_mirror/verdict/pi/_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` | `9a98abf3119a` | 20,610 | 211 | 2026-09-27 20:28:20 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 89 | `letters/_v5_rj5_external_rederive_request_2026_09_28.md` | `_repo_mirror/work/note/_v5_rj5_external_rederive_request_2026_09_28.md` | `cfd58ae66463` | 31,381 | 376 | 2026-09-28 18:22:06 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 90 | `letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md` | `_repo_mirror/work/note/_v5_rj5_external_rederive_request_EN_2026_09_28.md` | `498215a9ec7d` | 51,013 | 415 | 2026-09-28 18:47:14 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 91 | `letters/_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md` | `_repo_mirror/doc/letter/_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md` | `5bfc26bbaa41` | 15,606 | 187 | 2026-09-30 19:07:36 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |
| 92 | `letters/查理_glm_dualtrack_paper_sole_letter_2026_10_01.md` | `_repo_mirror/doc/paper/查理_glm_dualtrack_paper_sole_letter_2026_10_01.md` | `3c5059319ffe` | 13,105 | 114 | 2026-10-02 00:19:43 | v1 载荷沿袭（v1 清单 §4 之归属栏·面①·判准甲/乙/丙） |

**载荷总字节（92 件）**：**2,385,602 B**。**归档条目**：**93**（载荷 92 ＋ 本清单 1）。

### §4-1 载荷件之编码口径注（raw 字节计数 · 本棒实测）

| 项 | 实测汇总（92 件之和；脑图 1 件为二进制面） |
| :-- | --: |
| BOM 之件数（0xEF 0xBB 0xBF 开头） | 0 |
| CR 字节数之和 | 852 |
| TAB 字节数之和 | 96 |
| VT（0x0B）字节数之和 | 118 |
| U+FFFD 之件数 | 26696 |
| 非 UTF-8 可解码之**文本**件之件数（⛔ 0 计入二进制件） | 0 |
| 二进制件之件数（脑图本体） | 1 |
| 末行 LF 终结之件数 | 77 / 92 |

> 📌 **二进制件之读数口径**：脑图本体（`.jpg` 资产）为**二进制件**⇒ 其 CR／TAB／VT 之计数为**二进制面之正常字面**（⛔ 0 处置·⛔ 0 改其字节）；其 **JPEG 结构完整性**沿 v1 清单 §9-1 之载（magic `ffd8ffe0`／EOI `ffd9`／SOF 1596×1280）——**本棒 0 重测其语义·0 断言其内容**（件之识认依 PI 令之称名）。

---

## §5 移出台账（1 件 · 远端已有者 · 各载其远端路径）

| # | 件名 | SHA-12 | bytes | 远端路径（**标注**） | 远端 bytes | 远端 blob sha1 | 对位之据 | 远端面之时点 |
| :-: | :-- | :-- | --: | :-- | --: | :-- | :-- | :-- |
| 1 | `_codex_theory_derivation_reply_2026_09_30.md` | `7558eb1a5e34` | 71,002 | `letters/_codex_theory_derivation_reply_2026_09_30.md` | 71,002 | `25e6b4ea2f144c67e9be31c7fecd2874cba486bd` | 字节全等（git blob sha1 一致） | 2026-10-21 16:29:15 中国标准时间 |

**远端路径之写法**：`zeroandcat/Deposon` 仓 ＋ 分支 `main` ＋ 仓内相对路径 `letters/_codex_theory_derivation_reply_2026_09_30.md`（即可直接取用之路径）。

---

## §6 读乙之候核面（**路径同名而字节不同**者 4 件 · **未移出** · 归 PI 裁）

| # | 件名 | 本地 SHA-12 | 本地 bytes | 远端路径（同名） | 远端 bytes | 差 | 两读并出 |
| :-: | :-- | :-- | --: | :-- | --: | --: | :-- |
| 1 | `_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | `f4defae83553` | 22,064 | `letters/_claude_pending_pi_gaps_closeout_reply_2026_10_11.md` | 22,024 | -40 B | **读甲**＝远端所存者非同一实体（字节不同·远端版较本地版少 40 B）⇒ 不构成「远端仓库里有的**该文件**」⇒ **本棒采读甲·留在包内**｜**读乙**＝以**路径**论「远端已有」⇒ 亦应移出（则收件方于远端只得其**较贫**之版本） |
| 2 | `_codex_c4_values_followup_reply_2026_10_10.md` | `97a35f8ae94c` | 4,490 | `letters/_codex_c4_values_followup_reply_2026_10_10.md` | 4,380 | -110 B | **读甲**＝远端所存者非同一实体（字节不同·远端版较本地版少 110 B）⇒ 不构成「远端仓库里有的**该文件**」⇒ **本棒采读甲·留在包内**｜**读乙**＝以**路径**论「远端已有」⇒ 亦应移出（则收件方于远端只得其**较贫**之版本） |
| 3 | `_codex_c4_values_reply_2026_10_10.md` | `8e4972352291` | 13,378 | `letters/_codex_c4_values_reply_2026_10_10.md` | 13,058 | -320 B | **读甲**＝远端所存者非同一实体（字节不同·远端版较本地版少 320 B）⇒ 不构成「远端仓库里有的**该文件**」⇒ **本棒采读甲·留在包内**｜**读乙**＝以**路径**论「远端已有」⇒ 亦应移出（则收件方于远端只得其**较贫**之版本） |
| 4 | `_codex_c4_values_unblock_reply_2026_10_10.md` | `a975c7990cd8` | 21,486 | `letters/_codex_c4_values_unblock_reply_2026_10_10.md` | 21,264 | -222 B | **读甲**＝远端所存者非同一实体（字节不同·远端版较本地版少 222 B）⇒ 不构成「远端仓库里有的**该文件**」⇒ **本棒采读甲·留在包内**｜**读乙**＝以**路径**论「远端已有」⇒ 亦应移出（则收件方于远端只得其**较贫**之版本） |

> 📌 **本棒之采（载明·两读并出·⛔ 0 强合）**：**采读甲**（**移出之判据＝字节全等对位**）。**理由**＝令②之「远端仓库里有的文件」之实体同一性：此 4 件于远端**同名路径确在**，然其**字节与之不同**（远端版较本地版少 40–320 B）⇒ 远端所存者**非本包所载之同一实体**；以其充同一而移出，将致收件方（GLM）**得较贫之版本**而失本地之较全者。**代价不对称**：采读甲 ⇒ 包内多 4 件（重复面·小）；采读乙 ⇒ 包内失 4 件之较全版本（内容面之损·大）——**二者之择归 PI**（见 §13-1）。

---

## §7 远端面之核之径与界分（**核现值 vs 镜像面·两读并出**）

### §7-1 本棒之择（**已核现值** · 匿名只读 GET）

| 项 | 实测 |
| :-- | :-- |
| **径** | `GET https://api.github.com/repos/zeroandcat/Deposon`（仓元数据）＋ `GET …/git/trees/main?recursive=1`（全树）——**匿名·只读·0 凭据·0 写** |
| **观测时点** | **2026-10-21 16:29:15 中国标准时间**（本地 UTC+8） |
| **远端仓／分支** | `zeroandcat/Deposon` ／ `main`（`private`＝false） |
| **`pushed_at`** | 2026-10-18T15:02:52Z（远端最后推送之时点） |
| **tree sha** | `5f6dc0b7baf317eea3ab8f2a3b2f165f60fd0c2a` |
| **`truncated`** | **False**（全树穷举·非抽样⇒ 阴性断言（0 命中）成立） |
| **条目／blobs／trees** | 3,659 ／ 3,462 ／ 197 |
| **对位之法** | **git blob sha1**（`sha1("blob <len>\0" + 内容)`）——远端树 API 对每个 blob 给出其 sha1 ⇒ 本地逐件复算即可判定**字节全等**（**0 下载任何远端文件**·0 传出·0 存证） |
| **择之由** | 令②之射程为「远端仓库**里有的**文件」⇒ 须判**现值**；镜像面为 **10-17 时点**之快照（非现值）⇒ 单以镜像面判之**不足**。PI 派工单所许之径（GitHub API 匿名只读·已验在册·0 写远端）**本棒采之**；**镜像面仍作本地佐证面**（见 §7-2） |

### §7-2 镜像面（本地拉回件 `_remote_pullback_2026_10_17`）之实测与界分

| 项 | 实测 |
| :-- | :-- |
| **镜像面之件数** | **219**（`letters/` 1 ＋ `results/` 72 ＋ `_september_workspace/` 146） |
| **镜像面之时点** | **2026-10-17 拉回**（其面之 mtime 集中于 2026-10-17 15:5x）——⚠ **现值须带时点**：镜像面**非现值之面** |
| **镜像件 → 远端现值之对位** | 字节全等 **90** ／ 路径在而字节不同 **44** ／ **已不在远端** **85** |
| **映射规则（实测归纳·非假定）** | `X → X`（50）｜`_september_workspace/X → _repo_mirror/X`（21）｜`X → _repo_mirror/X`（19）——⚠ **远端路径于 10-17 之后经改组**（`_september_workspace/` → `_repo_mirror/`）⇒ **镜像面之相对路径不可直接当现值之远端路径** |
| **包中件于镜像面之对位** | **0 件**（路径对位 0 ＋ 字节对位 0）⇒ 令②之移出判定**不取镜像面**（镜像面无包中件之对应者） |
| **界分（两条）** | ①**镜像面 ≠ 远端现值**（10-17 快照·且远端其后有改组与增删——实测 85 件已不在远端）②**镜像面 ≠ 全量远端面**（其 219 件远低于远端全树 3,462 blobs）⇒ 以镜像面判定「远端有没有」**会漏判** |

### §7-3 远端根层遗留面（**单列·不参与镜像映射比对**）

| 项 | 实测 |
| :-- | :-- |
| **远端根层 blobs／trees** | 68 ／ 12（根层目录：.trae、_repo_mirror、corpus、deposon_team、docs、letters、paper、results、reviews、tests、tools、verifier） |
| **在册之裁（PI 2026-10-18 卡答·在册条）** | 远端根层遗留面＝deposon V1/V2 阶段之产物，**刻意与镜像区分离**；处置＝**全留不删**；**根层遗留面单列·不参与镜像映射比对** |
| **本棒之遵** | ✅ **单列**（本节）·**0 参与镜像映射比对**（§7-2 之对位仅以镜像件自身之字节/路径为据）·**0 删远端·0 写远端**（仅匿名只读 GET） |

---

## §8 纪律与自核

- **形态**：**自解压脚本**（内嵌压缩包）——PI v190-Q3 令③所改；**0 压缩包本体之传出面**（v1 之 zip **原处不动**·见 §11）。
- **0 传出**：⛔ 0 推送·0 外联·0 触达·0 写 `〔本地他区引用·未上传:GLM〕`——**传出之径归 PI**。
- **联网之实况（如实登记）**：**联网一次**（匿名只读 GET·远端仓元数据＋全树·**0 凭据·0 写远端·0 下载远端文件**）——**PI 派工单明载其径可用**（§7-1）；**0 传出任何件**（GET 之 URL 仅载公开仓名·请求体内 0 载任何项目内容）。
- **只读**：92 件载荷源件**0 改·0 覆写·0 移动·0 重命名·0 删除**；打包前后两轮实测 sha／bytes／mtime **全等**（见回执）。 |
- **字节级复制**：93/93 于归档内之字节与原位**逐位一致**（解包后逐件比对·含脑图 1 件·见 §10）。 |
- **包指纹**：`45930381276adc5dc6f4434b201527b69171a66064fccaa4592c63c309f6bb2f`（载荷 92 件·0 自指·定义见本节下一行）。**定义**（承 v1 §7 之口径）：对**载荷 92 件**（**不含本清单件自身**——沿族体例 0 自指）按**归档内相对路径之 Unicode 码点序**逐行拼接 `相对路径|sha256[:12]|bytes`（**每行〔含末行〕行尾 LF**）成 UTF-8 文本，对该文本求 sha256。任何方可解包后依此定义独立复算验证。**本棒以 v1 之载荷复算得 `cdaa5e10cfa09677d315666c7dcf2f5cbf080826863afd68e8c9644b2fdd7ee8` ＝ v1 清单所载 `cdaa5e10cfa0`（吻合·口径实现之自检）**。 |
- **实测声明**：本清单全部指纹／字节／行数／mtime 值系程序化计算（`hashlib`／`stat`／字节计数），**非记忆值**；未实测面 **0 断言**。
- **本清单自身指纹／脚本本体指纹**：**0 自写入**（脚本内嵌本清单 ⇒ 循环不可自写）——落盘后实测**随回执回报**。
- **⛔ 0 落五终判词**（`pass`／`af`／`kd`／`fail`／`give-up` 之任一）｜**⛔ 0 闭任何 KD**｜**⛔ 0 宣告段毕**｜**⛔ 0 宣告任何请求已发出**｜**⛔ 0 代 PI 裁**｜**⛔ 0 读 key**（敏感面预筛仅计数·0 回显字面）｜**GBK 之戒**（全程 UTF-8 解码·非 UTF-8 件 0 件·见 §4-1）。 |

---

## §9 敏感面预筛之果（**仅计数·不回显字面·⛔ 0 读 key**）

| 筛面 | 载荷 92 件之命中合计 | 判定 |
| :-- | --: | :-- |
| **凭据形态**（`sk-`／`ghp_`／`AKIA`／私钥头／`xox*`） | **0** | ✅ **0 真凭据形态** |
| **赋值形**（`api_key: <值>` 等） | **1** | 逐件**形状判定**后 ＝ 见 §9-1（**0 凭据值**） |
| **密钥类关键词**（`api_key`／`token`／`password` 等） | **4** | 逐件**形状判定**后 ＝ 见 §9-1（**0 凭据值**） |
| **URL** | **10** | 逐件**形状判定**后 ＝ 见 §9-1（**0 凭据值**） |

### §9-1 命中项之逐件形状判定（**不回显字面·仅形状属性**）

| 件名 | 命中类 | 件数 | 形状判定（属性描述·非字面） |
| :-- | :-- | --: | :-- |
| `_v4_commission_kimi_fullupload_w3_2026_09_30.md` | keyword | 2 | 关键词（7 字符）·同行赋值形 无 ⇒ 字段名/表达式之提及·0 凭据值；关键词（6 字符）·同行赋值形 无 ⇒ 字段名/表达式之提及·0 凭据值 |
| `_v4_commission_paper_final_glm_2026_09_24_v4.md` | url | 1 | 主机 127.0.0.1（本地回环·非内网/远端主机） |
| `_v4_commission_upload_executor_2026_09_24_v3.md` | url | 1 | 主机 127.0.0.1（本地回环·非内网/远端主机） |
| `_v4_ide_track_review_trae_work_2026_09_20.md` | keyword | 1 | 关键词（7 字符）·同行赋值形 无 ⇒ 字段名/表达式之提及·0 凭据值 |
| `_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` | assign_shape | 1 | 赋值形·值长 16（小写 14／大写 0／数字 0／下划线 2）·已知密钥前缀 否 ⇒ 标识符形态·0 凭据值 |
| `_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` | keyword | 1 | 关键词（7 字符）·同行赋值形 有 ⇒ 字段名/表达式之提及·0 凭据值 |
| `_v5_rj5_external_rederive_request_2026_09_28.md` | url | 4 | 主机 arxiv.org（公开文献引址） |
| `_v5_rj5_external_rederive_request_EN_2026_09_28.md` | url | 4 | 主机 arxiv.org（公开文献引址） |

> 📌 **计数口径之界分（本棒之预筛实现 vs v1 §6 之模式集）**：本棒之预筛**模式集与 v1 清单 §6 之模式集微异**——本棒之「赋值形」模式另含 `secret`／`token`／`password` 等键，故**赋值形命中计数（1）与 v1 之 0 不同**；二者**0 混读**（v1 之表系 2026-10-21 上午之独立观测·本表系本棒之独立观测·**以本表为 v2 之准**）。 |
> 📌 **与在册形状判定之相合**：`_v4_wide_walkthrough_reply_trae_code_2026_09_27.md` 之赋值形命中·本棒实测形状（16 字符·snake_case·0 大写·0 数字·0 已知密钥前缀）**与在册 v1 清单 §6-1（`debce2c6d3cb`）对该件之同向形状判定（字段名／代码表达式形态·无大写·无数字·无已知密钥前缀）相合**。
> 📌 **诚实交代**：本节之判定为**形状属性判定**（字符类／长度／前缀／结构形态／主机名），**未回显任何命中字面**；**⛔ 0 读 key**（凭据值 0 读取·0 记录·0 转写）。判定结论＝**载荷 92 件中 0 真凭据面**。 |

---

## §10 自解压之正确性之自证（**临时面自解压 · 逐位比对**）

| 项 | 实测 |
| :-- | :-- |
| **测试面** | **临时面**（系统临时目录之 `deposon_v2pack_scratch\selftest_*`）——**0 落仓内**·**0 触项目件之写面之外之执行** |
| **执行之授权面** | 令源所许：「其脚本之执行面之测试之执行面属本棒之授权面（临时面之执行）」——本棒**仅于临时面**执行其自解压 |
| **自解压方式** | 运行成件脚本本身（`python <脚本> --dest <临时目录>`）——非以其逻辑之复刻代之 |
| **比对之口径** | 解出之每件 **与本地原件逐位比对**（SHA-256 全值 ＋ bytes ＋ 逐字节） |
| **比对件数** | **93**（载荷 92 ＋ 本清单 1）——**全量**（≥5 件抽测之要求之上限达成） |
| **逐位全等** | **93 / 93** |
| **不符件** | **0** |
| **内嵌载荷整体校验** | 脚本内**载其内嵌载荷之自身 sha256／bytes 两常量**（`PAYLOAD_SHA256`／`PAYLOAD_BYTES`）——脚本 `--verify-only` 自校验（载荷 sha256 复算 ＋ 逐条索引复算）＝ **PASS**（于成件脚本实测）｜⚠ **本清单 0 自写入载荷之 sha256／bytes**：载荷含本清单 ⇒ 循环不可自写（其值随回执回报） |
| **路径无关性** | 于**临时面之独立工作目录**（`〔本地绝对路径·脱敏略:deposon_v2pack_scratch〕` 下之独立 cwd·**非仓内**）运行之——**0 依赖相对路径** |

> 📌 **测试之产出面**：**只落于临时面**（测试目录可弃）——**0 于仓内留下测试副本**；脚本之运行**0 写任何既有件**（其写入面限于 `--dest` 所指目录）。

---

## §11 v1 之 zip 之面之存续（**⛔ 0 删 · 留废之裁归 PI**）

| 项 | 值 |
| :-- | :-- |
| **v1 zip 本体** | `results\_deliverable_pack_2026_10_21.zip`（`f4fe63437144`·1,120,238 B·92 条目）——**原处不动**（0 删·0 移动·0 重命名·0 覆写） |
| **v1 清单件** | `results\_deliverable_pack_manifest_2026_10_21.md`（`debce2c6d3cb`·80,302 B）——**原处不动** |
| **其面之存续（载明）** | 令③使「压缩包本体」之形**不获 GLM 面之接受** ⇒ v1 之 zip 就 **GLM 面**而言**不属可转交之形**；然**其留废之裁归 PI**（PI 2026-10-18 铁律：⛔ 0 移动/重命名/删除；PI 令明载「⛔ 0 删已落之 zip」）⇒ **本棒 0 删之·0 动之**，其存续与处置**候 PI 裁**（见 §13-3） |
| **其内容之关系** | v2 之载荷＝v1 之载荷**减 1（移出）加 2（令①）**⇒ v1 之 zip **仍为 v2 内容面之可追溯底稿**（v1 之清单 §4 载 v1 载荷逐件指纹·0 回改） |

---

## §12 v2 之归档结构（**归档条目 93** ＝ 载荷 92 ＋ 本清单 1）

```
_deliverable_pack_v2_selfextract_2026_10_21.py   ← 收件方所运行者（内嵌压缩包之自解压脚本）
└── 载荷 92 件（归档内相对路径之层级保留）
    ├── G-30-a_脑图_AI应当如何思考_从仿生向到仿物理向_2026_10_21.jpg
    ├── letters/…（91 件）
    └── …
└── _deliverable_pack_v2_manifest_2026_10_21.md   ← 本清单（归档条目 93 · 非载荷·不计入包指纹）
```

---

## §13 候 PI 核之面（**传出前之内容面之裁归 PI · 本棒 0 代裁**）

1. **读乙之择（§6 之 4 件路径同名而字节不同者）**——**荐案：采本棒之读甲（留在包内）**。**理由**：移出将使收件方（GLM）于远端只得较本地版少 40–320 B 之版本（内容面之损）⇒ 代价不对称（大损 vs 小重）。**PI 若裁「一并移出」**，则 v2 载荷变 88 件，**须重装包**（脚本内嵌载荷与索引皆随之变）——**本棒不预作**。 |
2. **转交之对方面**——本棒 **0 断言**（PI 令未具名对方面；v1 清单 §8-3-1 之面**存续**）。PI 若定对方面为某受托方，可据此**再行剔减**。
3. **v1 之 zip 之留废之裁（§11）**——**荐案：留之**（其内容为 v2 之可追溯底稿·⛔ 0 删之铁律）。**PI 若裁删之**（或径以 v2 之内容面另立他形），**须以具名令行之**——本棒 0 预作。
4. **`.py` 之形之择（§2-3）**——**荐案：采 `.py`**（跨平台·0 执行策略依赖·仅标准库）。**PI 若裁 `.ps1`**（Windows 原生形），**须重写脚本**（载荷与索引不变·形改）——**本棒 0 预作**。
5. **入包件数面**——本棒采「**载荷 92 ＋ 清单 1 ＝ 归档条目 93**」之双数登记（⛔ 0 以条目数代载荷件数）；PI 若另给件数口径，以 PI 者为准。 |
6. **本清单之随包形态**——本清单**存于归档之根**（随 v1 体例）**且**于仓内 `results/` 另存**同一字节面**。⚠ **快照界分**：若 PI 于传出前修订本清单之内容面，则**须重装包**（归档内之清单副本为落盘时快照）——**此事归 PI 触发·本棒不预作**。
7. **两候选回函件之模型面（§2-1）**——copilot ＝ agent 名；其**模型面 0 暴露**（件内自述）⇒ **0 断言**；若 PI 之意在某一**特定模型面**之回函，请具名。
8. **远端面之现值之时效（§7-1）**——本棒之远端读数系 **2026-10-21 16:29:15 中国标准时间** 之观测（`pushed_at`＝2026-10-18T15:02:52Z）；**其后若远端有推送**，则「远端已有」之判定随之可变——**本棒 0 预作后续核**（PI 传出前如需，可令复核）。 |

---

## §14 老实交代

① **0 断言**两候选回函件之内容语义之正确性（件之识认依 PI 令之称名）；② **0 断言** copilot 之**模型面**（件内自述未暴露）；③ **0 断言**「远端已有」之判定之外之远端内容（**0 下载任何远端文件**·仅以 git blob sha1 对位）；④ **镜像面 ≠ 远端现值 ≠ 远端全量**（§7-2 之两条界分）；⑤ **读甲／读乙未强合**（§6）；⑥ **v1 zip 之留废未裁**（§11·归 PI）；⑦ **0 落五终判·0 闭任何 KD·0 宣告段毕·0 宣告任何请求已发出**；⑧ **本清单自身指纹与脚本本体指纹 0 自写入**（循环不可自写·随回执回报）；⑨ **联网一次之实况**（匿名只读 GET·0 写远端·0 传出任何件·§8）。

---

**出件｜deposon 执行官 worker（PI v190-Q3 三令之执行棒）｜2026-10-21 16:3x–17:0x UTC+8**｜v2 之形＝**自解压脚本** `results\_deliverable_pack_v2_selfextract_2026_10_21.py`（内嵌压缩包·base64·**0 压缩包本体传出**）｜**载荷 92 件**（`letters/` 面 91 ＋ 脑图 1）**＋ 本清单** ＝ **归档条目 93**｜**包指纹 `45930381276adc5dc6f4434b201527b69171a66064fccaa4592c63c309f6bb2f`**（载荷射径·0 自指·定义见 §8）｜**移出 1 件**（远端已有者·各载远端路径·§5）｜**令①入包 2 件**（§2-1）｜远端现值核验 ＝ 匿名只读 GET（`truncated=false`·全树·§7-1）｜镜像面（10-17）仅作本地佐证（§7-2）｜敏感预筛 0 真凭据（§9）｜自解压自证 **93/93 逐位全等**（临时面·§10）｜⛔ 0 移动/0 重命名/0 删除/0 覆写任何既有件·0 传出·0 代裁·0 落五终判·0 闭 KD·0 宣告段毕·0 新建目录于仓内｜**脚本本体指纹与本件自身指纹 0 自写入**——落盘后实测随回执回报。
