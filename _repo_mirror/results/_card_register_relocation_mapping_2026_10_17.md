# 卡答登记件之迁移映射件（2026-10-17 · `CARD-RELOCATE` · M2）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_card_register_relocation_mapping_2026_10_17.md` |
| **件性质** | **迁移映射件**（**先有据、后动件**）—— 承先例 `results/_voided_files_relocation_register_2026_10_14.md` §1-3 之体制 ＋ 判断件 `results/_card_register_dir_verdict_2026_10_17.md`（SHA-12 `a694e5d55ce1`）§3-1 之 **M2**；**非卡答登记件**（本件不载 PI 裁答之逐字答录，故不在 PI 射程「仅卡答登记件」之内）⇒ 留 `results/` |
| **署名** | `protocol-keeper`（口径与预登记官）· 棒 `CARD-RELOCATE` |
| **落点目录** | `D:\私人资料\deposon-repo\pi_rulings\`（**新建根层目录** · PI 裁**丁案**）|
| **裁源** | PI 2026-10-17 ≈16:52 · 卡 `ask_2934bcc32391d96596131ffd` · Q1 `opt2`（目录＝丁案 `pi_rulings/`）＋ Q2 `opt2`（迁 **57** 件·含合并卷 `bc9680a5d39a`）—— **经派工单转述**（见 §4 KD-2）|
| **本件射程** | 仅**旧→新路径映射**之登记（**58** 行 ＝ `results/` **57** 件 ＋ `.tmp` v58 候迁件 **1** 件）。⛔ **0** 执行迁移（执行面见 `results/_card_register_relocation_register_2026_10_17.md`）· ⛔ **0** 回改任何既有件一字 · ⛔ **0** 删件 · ⛔ **0** 触归档区 · ⛔ **0** 网络 |

---

## §1 映射面（58 行 · 逐件实测值取自 M1 迁前快照）

> 「旧路径」＝ **M1 迁前实测存在**之路径；「旧 SHA-12／旧 bytes／旧 mtime」＝ 迁移前实算值（**非沿用任何历史登记之值**，遵判断件 §3-2「SHA 漂移之既存面」之诫）。

| # | 旧路径（迁后已失效） | → 新路径 | 旧 SHA-12 | 旧 bytes | 旧 mtime |
| :-: | :-- | :-- | :-- | --: | :-- |
| 1 | `results/_pi_card_answers_register_2026_10_13.md` | `pi_rulings/_pi_card_answers_register_2026_10_13.md` | `10a74ce8901d` | 5707 | 2026-10-14 00:13:48 |
| 2 | `results/_pi_card_answers_register_2026_10_14.md` | `pi_rulings/_pi_card_answers_register_2026_10_14.md` | `bc9680a5d39a` | 5529 | 2026-10-14 20:57:43 |
| 3 | `results/_pi_card_answers_register_2026_10_14_v2.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v2.md` | `ee392ef4a69a` | 5968 | 2026-10-14 21:15:04 |
| 4 | `results/_pi_card_answers_register_2026_10_14_v3.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v3.md` | `59e8a7be4c05` | 5664 | 2026-10-14 21:30:03 |
| 5 | `results/_pi_card_answers_register_2026_10_14_v4.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v4.md` | `7838b3300596` | 5010 | 2026-10-14 21:41:45 |
| 6 | `results/_pi_card_answers_register_2026_10_14_v5.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v5.md` | `3587e46b45c3` | 5643 | 2026-10-14 21:53:10 |
| 7 | `results/_pi_card_answers_register_2026_10_14_v6.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v6.md` | `7e95b053e249` | 5469 | 2026-10-14 22:02:43 |
| 8 | `results/_pi_card_answers_register_2026_10_14_v7.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v7.md` | `d114b7576b78` | 5851 | 2026-10-14 22:12:13 |
| 9 | `results/_pi_card_answers_register_2026_10_14_v8.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v8.md` | `58d1c527e228` | 5252 | 2026-10-14 22:41:48 |
| 10 | `results/_pi_card_answers_register_2026_10_14_v9.md` | `pi_rulings/_pi_card_answers_register_2026_10_14_v9.md` | `64450a287abd` | 4071 | 2026-10-14 23:15:40 |
| 11 | `results/_pi_card_answers_register_2026_10_15_v10.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v10.md` | `57b4d493789a` | 6132 | 2026-10-15 09:39:21 |
| 12 | `results/_pi_card_answers_register_2026_10_15_v11.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v11.md` | `30408490f37e` | 4577 | 2026-10-15 10:02:55 |
| 13 | `results/_pi_card_answers_register_2026_10_15_v12.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v12.md` | `97111fee4410` | 6081 | 2026-10-15 11:03:46 |
| 14 | `results/_pi_card_answers_register_2026_10_15_v13.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v13.md` | `693181b9354b` | 3661 | 2026-10-15 12:53:08 |
| 15 | `results/_pi_card_answers_register_2026_10_15_v14.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v14.md` | `ac3b580defbb` | 5805 | 2026-10-15 14:37:19 |
| 16 | `results/_pi_card_answers_register_2026_10_15_v15.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v15.md` | `c6c1e9fe17ad` | 4531 | 2026-10-15 15:14:09 |
| 17 | `results/_pi_card_answers_register_2026_10_15_v16.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v16.md` | `b8036d12e28f` | 5070 | 2026-10-15 16:05:21 |
| 18 | `results/_pi_card_answers_register_2026_10_15_v17.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v17.md` | `bc3041ec2cbc` | 4140 | 2026-10-15 16:41:15 |
| 19 | `results/_pi_card_answers_register_2026_10_15_v18.md` | `pi_rulings/_pi_card_answers_register_2026_10_15_v18.md` | `318d176e027c` | 4670 | 2026-10-15 17:06:55 |
| 20 | `results/_pi_card_answers_register_2026_10_16_v19.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v19.md` | `e1f9b3d07eef` | 4773 | 2026-10-16 10:50:16 |
| 21 | `results/_pi_card_answers_register_2026_10_16_v20.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v20.md` | `44aa59715d21` | 6075 | 2026-10-16 11:32:01 |
| 22 | `results/_pi_card_answers_register_2026_10_16_v21.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v21.md` | `4b72c0b23504` | 3210 | 2026-10-16 11:41:27 |
| 23 | `results/_pi_card_answers_register_2026_10_16_v22.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v22.md` | `e8d476480244` | 5629 | 2026-10-16 13:43:01 |
| 24 | `results/_pi_card_answers_register_2026_10_16_v23.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v23.md` | `a2a883a6be8e` | 4889 | 2026-10-16 14:23:19 |
| 25 | `results/_pi_card_answers_register_2026_10_16_v24.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v24.md` | `e18bb149018d` | 3985 | 2026-10-16 15:04:12 |
| 26 | `results/_pi_card_answers_register_2026_10_16_v25.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v25.md` | `b682e95fba5e` | 5400 | 2026-10-16 15:16:39 |
| 27 | `results/_pi_card_answers_register_2026_10_16_v26.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v26.md` | `bcd9598a243a` | 4338 | 2026-10-16 15:55:54 |
| 28 | `results/_pi_card_answers_register_2026_10_16_v27.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v27.md` | `6cdb2bc823f9` | 10776 | 2026-10-16 19:22:10 |
| 29 | `results/_pi_card_answers_register_2026_10_16_v28.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v28.md` | `87aea4811290` | 11627 | 2026-10-16 19:32:50 |
| 30 | `results/_pi_card_answers_register_2026_10_16_v29.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v29.md` | `bfcc14f8a4ce` | 16960 | 2026-10-16 19:45:45 |
| 31 | `results/_pi_card_answers_register_2026_10_16_v30.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v30.md` | `1c11cc165d27` | 24832 | 2026-10-16 20:01:01 |
| 32 | `results/_pi_card_answers_register_2026_10_16_v31.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v31.md` | `ad53416b5f10` | 26239 | 2026-10-16 20:19:06 |
| 33 | `results/_pi_card_answers_register_2026_10_16_v32.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v32.md` | `c20d77f3b79c` | 31156 | 2026-10-16 20:24:30 |
| 34 | `results/_pi_card_answers_register_2026_10_16_v33.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v33.md` | `a03c20e88d66` | 18077 | 2026-10-16 20:25:45 |
| 35 | `results/_pi_card_answers_register_2026_10_16_v34.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v34.md` | `f4ebae2d17e7` | 21659 | 2026-10-16 20:53:06 |
| 36 | `results/_pi_card_answers_register_2026_10_16_v35.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v35.md` | `6ff343861b29` | 19575 | 2026-10-16 21:17:15 |
| 37 | `results/_pi_card_answers_register_2026_10_16_v36.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v36.md` | `371a3c19b734` | 26950 | 2026-10-16 21:38:38 |
| 38 | `results/_pi_card_answers_register_2026_10_16_v37.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v37.md` | `8d46bd80c654` | 25891 | 2026-10-16 21:41:50 |
| 39 | `results/_pi_card_answers_register_2026_10_16_v38.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v38.md` | `db7b9f80bdd1` | 23104 | 2026-10-16 22:02:03 |
| 40 | `results/_pi_card_answers_register_2026_10_16_v39.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v39.md` | `8ce18e4b5eab` | 20508 | 2026-10-16 22:18:26 |
| 41 | `results/_pi_card_answers_register_2026_10_16_v40.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v40.md` | `8f8ba225a558` | 26768 | 2026-10-16 22:40:00 |
| 42 | `results/_pi_card_answers_register_2026_10_16_v41.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v41.md` | `1e75eecc1657` | 41175 | 2026-10-16 23:14:03 |
| 43 | `results/_pi_card_answers_register_2026_10_16_v42.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v42.md` | `57d938ea80dc` | 41612 | 2026-10-16 23:39:16 |
| 44 | `results/_pi_card_answers_register_2026_10_16_v43.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v43.md` | `c5d5d0c24041` | 33335 | 2026-10-16 23:49:16 |
| 45 | `results/_pi_card_answers_register_2026_10_16_v44.md` | `pi_rulings/_pi_card_answers_register_2026_10_16_v44.md` | `996331734904` | 45596 | 2026-10-17 00:17:54 |
| 46 | `results/_pi_card_answers_register_2026_10_17_v45.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v45.md` | `fb444970452c` | 61355 | 2026-10-17 10:14:30 |
| 47 | `results/_pi_card_answers_register_2026_10_17_v46.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v46.md` | `3b5e35eebcbd` | 64372 | 2026-10-17 10:38:06 |
| 48 | `results/_pi_card_answers_register_2026_10_17_v47.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v47.md` | `6731d5533709` | 65046 | 2026-10-17 10:54:30 |
| 49 | `results/_pi_card_answers_register_2026_10_17_v48.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v48.md` | `876f0e5dc38d` | 63119 | 2026-10-17 11:12:18 |
| 50 | `results/_pi_card_answers_register_2026_10_17_v49.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v49.md` | `2367979d60a4` | 58978 | 2026-10-17 11:23:23 |
| 51 | `results/_pi_card_answers_register_2026_10_17_v50.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v50.md` | `188ac0656715` | 87647 | 2026-10-17 11:59:35 |
| 52 | `results/_pi_card_answers_register_2026_10_17_v51.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v51.md` | `ffa1cd08b98b` | 106355 | 2026-10-17 12:33:27 |
| 53 | `results/_pi_card_answers_register_2026_10_17_v52.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v52.md` | `511d3518aa15` | 61157 | 2026-10-17 14:22:21 |
| 54 | `results/_pi_card_answers_register_2026_10_17_v53.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v53.md` | `4c2d5c66f52b` | 51621 | 2026-10-17 15:19:00 |
| 55 | `results/_pi_card_answers_register_2026_10_17_v54.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v54.md` | `b45c83999e9f` | 72379 | 2026-10-17 16:02:50 |
| 56 | `results/_pi_card_answers_register_2026_10_17_v55.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v55.md` | `84f6c4bfdb07` | 54188 | 2026-10-17 16:05:37 |
| 57 | `results/_pi_card_answers_register_2026_10_17_v56.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v56.md` | `d4c5d4988944` | 51458 | 2026-10-17 16:18:36 |
| 58 | `.tmp/_pi_card_answers_register_2026_10_17_v58.md` | `pi_rulings/_pi_card_answers_register_2026_10_17_v58.md` | `e15de4a194e0` | 43565 | 2026-10-17 16:39:11 |

**合计**：**58** 件 · **1,444,210** B ｜ 来源：`results/` **57** 件 ＋ `.tmp/` **1** 件（v58 候迁件，自暂存面顺迁）

---

## §2 映射口径

| 项 | 口径 |
| :-- | :-- |
| 旧路径 | **相对仓库根** `D:\私人资料\deposon-repo` 之正斜杠路径（与先例 §3 之绝对路径写法并存，本件用相对式以便跨机复算）|
| 新路径 | `pi_rulings/<同名件>` —— **同名同址·仅换目录**（⛔ **0** 改名 ⛔ **0** 改扩展名 ⛔ **0** 改大小写）|
| SHA-12 | 全文件 SHA-256 之前 **12** 位十六进制（**全文口径**）|
| bytes | `os.stat().st_size`（原始字节数）|
| mtime | `st_mtime` 之本地时间 `YYYY-MM-DD HH:MM:SS`（**迁移须保持**，见先例 §1-3 之 3）|
| 迁移法 | 同卷（D:→D:）`os.rename`（保 mtime）—— ⛔ **0** 用「复制＋删源」（先例 §1-3）|
| 删语义 | **0**（迁移＝ move；先例 §1-2 之裁量口径）|

---

## §3 引用面基线（M1 双通道 · 迁前时点快照）

| 通道 | 判据 | 处数 | 件数 |
| :-- | :-- | --: | --: |
| **M1-① 文件名道** | 全仓文件名逐字命中 58 个目标基名 | — | **58**（**均系被迁移件自身**，外同名件 **0**）|
| **M1-② 内容道（A）** | 全文 UTF-8 解码后**逐件基名**子串计数 | **3,490** | **567** |
| **M1-② 内容道（A）· 剔 `.tmp`/`__pycache__`** | 同上，剔暂存面 | **550** | **221** |
| **M1-② 内容道（B·超集）** | 族名前缀正则（含省略号截断形） | **3,626** | **581** |
| **M1-③ 字节道** | **7** 件 >4 MiB ＋ **89** 件非 UTF-8 之**字节级**补扫 | **2** | **2**（**均系 `.pyc` 编译产物**）|

**遍历面**：`os.walk` 遍历文件 **3,699** 件 ／ 目录 **143** 个 ／ **遍历错误 ＝ 0**（`onerror` 断言·先例 §1-3 之 1）｜检索根 ＝ 仓库根（**含** `.mavis`／`.trae`／`.vscode`／`.tmp` 等运行时附件面·**0 排除**）｜大小上限 **4 MiB**（与判断件 §0 同口径）

**入向覆盖**：被引之不同目标件名 **58／58** ⇒ **全族 100% 件至少被 1 件按名引用**（与判断件 §0-4 之 57／57 同向）

**引用面处置**：⛔ **0 回改** —— 依先例 §2-3 与 PI「⛔ 0 回改任何既有件一字」之纪律，上述 **3,492** 处引用（剔 `.tmp` 后 **550** 处／221 件）**一律只记不改**；其字面路径迁后成**悬空锚**，可解析性**以本映射件为准**（先例 §3 之映射面即为此而设）。

**基线快照落点**：`.tmp/card_reloc_m1_refscan_2026_10_17.json`（生成时点 **2026-10-17 16:57:35**）—— 逐件「旧 SHA-12／bytes／mtime」与逐通道明细之可复算源

---

## §4 KD（本件如实登记 · 0 编造）

| id | KD | 实测依据 |
| :-- | :-- | :-- |
| **KD-1** | **`pi_rulings/` 之目录创建先于本棒，且其内已落 v59 件①** —— 目录 mtime **2026-10-17 16:54:36**，内含 `_pi_card_answers_register_2026_10_17_v59.md`。本棒 M3 占用双检之「`Test-Path` 目录 ＝ `False`」一项**不成立**（如实载），**逐件目标名 58／58 命中 ＝ 0** ⇒ **非冲突**：v59 之件名不与本映射面任何一行同名，**0 覆盖 · 0 移动之 · 0 改名** | M3 实测 · §1 之 58 行件名与 v59 件名逐字比对 |
| **KD-2** | **PI 裁逐字未自独立件复核** —— 卡 `ask_2934bcc32391d96596131ffd` 之 Q1 `opt2`／Q2 `opt2` 系**经派工单转述**；本棒以关键词（`ask_2934bcc32391d96596131ffd`／`pi_rulings` 之裁答语汇）**全仓实测检索**未寻得独立载裁之件 ⇒ 权威性承自派工单 | 承先例 §1-1 之 KD-D 同型 |
| **KD-3** | **引用面处数与判断件 §0-4 基线不同量级（口径差，非计数错）** —— 判断件基线为「1,625 处／393 件（含 `.tmp`）」「482 处／202 件（剔 `.tmp`）」；本棒为「内容道 A **3,490** 处／**567** 件（含 `.tmp`）」「**550** 处／**221** 件（剔 `.tmp`）」。二者**口径不同**（本棒＝**逐件完整基名**精确计数，判其前缀／截断形者另有内容道 B 超集 **3,626** 处），且盘面在动（判断件时点 **16:4x** → 本棒 **2026-10-17 16:57:35**；遍历文件 3,699 件）。⇒ **判死线级不变量「全族 100% 件有入向引用」两法同向成立**；绝对处数**以本件之 M1 快照为准** | M1 快照 · 逐字段可复算 |
| **KD-4** | **M1 之 89 件非 UTF-8 件须以字节道补扫** —— 内容道 A 仅适用于可 UTF-8 解码之件；本棒对 **7** 件 >4 MiB ＋ **89** 件解码失败件**另跑字节道**（文件名皆 ASCII，字节级子串计数成立）⇒ 命中 **2** 处／**2** 件，**均系 `__pycache__` 下 `.pyc` 编译产物**（`tools\__pycache__\exp_harness.cpython-314.pyc`、`…\.tmp\__pycache__\refonly161_r2_build_register.cpython-314.pyc`）—— **非源码引用**，故**不影响**「0 回改」之处置面 | M1-③ 明细 |
| **KD-5** | **v59 件①（`pi_rulings/`）之归属与续迁** —— v59 棒（`bg_114e9e55`）在途，其件①**已直落 `pi_rulings/`**（另见 `.tmp/` 内同秒前后之同名件 **40,214 B**·**16:53:53**）⇒ **不在本件 58 行映射面内**（非 `results/` 族、非 v58 候迁件）；本棒 **0 动之**，其归属与续迁归 v59 棒／登记件之 KD 面 | M3 实测 · 盘面快照 |

---

## §5 本件状态

| 项 | 值 |
| :-- | :-- |
| **状态** | **已落盘**（M2 ＝「映射件先行」之先有据条件已满足 ⇒ 迁移 M4 之执行前提成立）|
| **落前占位实测** | `Test-Path` 目标件 ＝ `False`；全仓 glob 命中目标名 ＝ **0**（本件写入前实测）|
| **0 回改声明** | 本棒 **0** 改写任何既有件之任一字（含 58 件被迁移件、200 件引用者）—— 本件与登记件系**新增件**，非回改 |

## §6 落盘自报（字节级 · 落盘后复算）

| 项 | 值 |
| :-- | :-- |
| **路径** | `D:\私人资料\deposon-repo\results\_card_register_relocation_mapping_2026_10_17.md` |
| **bytes** |  17,871 |
| **SHA-12** | `73cb539bbb6f` |
| **SHA-12 口径** | 自文件首字节起、至本 `**SHA-12**` 所在行**行首（不含该行）**之全部字节之 SHA-256 前 12 位（**前缀口径**·承先例 §6；因全文哈希具自指性）|
| **编码** | UTF-8 **无 BOM** |
| **行尾** | **纯 LF** |

