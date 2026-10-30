# `_bloat_inventory_2026_10_22.md` —「本地仓库臃肿量化 ＋ 清理候选分级 ＋ 远端瘦身方案」（只读勘查之落盘）

| 项 | 值 |
| :-- | :-- |
| 件名 | `_bloat_inventory_2026_10_22.md` |
| 棒别 | explore（只读勘查棒 `bg_def9cc59`）· 勘查：2026-10-22 00:39–00:52 · **落盘：主代理 mavis 亲办**（explore 角色无 write 工具，全文由棒之报回交付，本件为其落盘版） |
| 令源 | PI 2026-10-22 排队令：「整理文件夹清放开手脚，无论远端仓库或本地都过于臃肿」 |
| 铁律 | ⛔0 删／⛔0 移／⛔0 改名／⛔0 建目录／⛔0 联网／⛔0 读 key／⛔0 落五终判／⛔0 闭 KD／⛔0 代裁 |
| 仪器 | `os.walk` 穷举（遍历错误 0）＋ `hashlib.sha256`（hash 错误 0）＋ 全文本引用面索引（5,785 件／135,242,359 B）＋ 在册测量件转引 |
| 状态 | **清单与方案已出；0 执行**（执行归 PI 逐单令） |

## §0 术语（首现附白话）

- **臃肿** ＝ 件数与体积超出维护必需。
- **压舱物** ＝ 占体积大而引用少的件。
- **引用面** ＝ 某件被仓内文本件（md／txt／py／log／jsonl／csv／err／out）以文件名或路径提及之面；引用面非空者，删除即生**幽灵引用**（引而不在盘）。
- **可恢复通道** ＝ `SHFileOperationW` ＋ `FOF_ALLOWUNDO`（入回收站，非永久删除）；载体 `tools/_archive_purge_2026_10_17/recycle_channel.py`（`06619281cd09`·3,540 B）。
- **零引用面** ＝ 该件在全文本引用面中 0 命中。

## §1 基线与体量画像（时点截面）

| 时点 | 全仓件数 | 字节 | MB | 遍历错误 |
|---|---:|---:|---:|---:|
| 00:39 | 6,671 | 644,015,955 | 614.2 | 0 |
| 00:51 | **6,697** | **645,001,204** | **615.1** | 0 |

⚠ 勘查期间 **+26 件**（并行棒写入）⇒ 一切计数为时点截面，**执行前须重测**。

### §1-1 一级面

| 面 | 件数 | MB | 占仓 |
|---|---:|---:|---:|
| **`.tmp`** | 4,026→4,032 | **514.1** | **83.6%** |
| `results`（全树；根层 1,399 ＋ 26 子目录） | 1,538 | 80.9 | 13.2% |
| `letters` | 141 | 4.3 | 0.7% |
| `pi_rulings` | 234 | 4.1 | 0.7% |
| `_remote_pullback_2026_10_17` | 219 | 3.4 | 0.6% |
| `deposon_team`（plugins 88） | 88 | 1.2 | 0.2% |
| `docs` | 43 | 1.2 | 0.2% |
| `corpus` | 42 | 0.9 | 0.2% |
| `tools` | 24 | 0.8 | 0.1% |
| `verifier` | 105 | 0.3 | 0.0% |

### §1-2 扩展名

`.json` 811／**425.6 MB** · `.md` 2,357／87.9 MB · `.tsv` 30／**56.6 MB** · `.py` 2,492／26.6 MB · `.txt` 790／12.2 MB · `.jsonl` 25 · `.pdf` 3 · `.zip` 1 · `.pyc` 15 · `.log` 85。

### §1-3 `.json` > 5 MB 者全 7 件（合计 **327.7 MB**，100% 在 `.tmp`，`results` 内 0 件）

| bytes | mtime | 路径 |
|---:|---|---|
| 286,347,176 | 10-20 20:52 | `.tmp\kdcensus_20261020_ea_data.json`（**占全仓 53.1%**） |
| 13,468,808 | 10-17 11:27 | `.tmp\archive_survey_inventory.json` |
| 10,812,360 | 10-18 14:23 | `.tmp\_archive_ro_verify_enum_2026_10_18.json` |
| 10,037,568 | 10-14 00:01 | `.tmp\_h_census_worker.json` |
| 9,700,261 | 10-18 00:20 | `.tmp\_r2_tool_03_refindex.json` |
| 6,987,091 | 10-18 14:24 | `.tmp\_archive_ro_verify_hashindex_2026_10_18.json` |
| 6,277,328 | 10-10 02:31 | `.tmp\_t1_exp2_c_records.json` |

## §2 重复与引用面（本件最要紧之两段）

### §2-1 逐字节重复

全树 **118 组／270 件／可回收 10.6 MB**（`.tmp` 域 24 组）。⚠ **「可留其一」不成立**：每组两侧**皆在引用链上** ⇒ 删除面 ＝ 0（「同字节异名」本身即复现性之据）。其中 28 件为 0 字节件（`e3b0c44298fc`），且**25 件皆被 md 引用**（删之即生幽灵）。

### §2-2 引用面索引（「体积在 `.tmp`，但 `.tmp` 几乎全在引用链上」）

| 扫描面 | 文件数 | 字节 | `.tmp` 域零引用件 | 零引用字节 |
|---|---:|---:|---:|---:|
| md 单扫 | 2,357 | 92,219,114 | 1,400 | 36.01 MB |
| 扩展（md＋txt＋py＋log＋jsonl＋csv＋err＋out） | 5,785 | 135,242,359 | **21** | **4.11 MB** |

⇒ 引用面自 md 扩至全文本后，零引用面**收缩 98.5%（件）／88.6%（字节）**。

### §2-3 引用风格（决定「移动」之代价）

路径式 token **200,432** vs 纯 basename token 52,833；5,748 件文本中 **4,516 件含路径式引用（78.6%）** ⇒ **移动将制造大量幽灵引用**；整理之正解是**索引件拉平**，而非移动改名。

## §3 四分类（A 可删／B 须 PI 逐单／C 宜归档／D 禁动）

| 类 | 件数 | 字节 | 判据 |
|---|---:|---:|---|
| **A 可直接删（可恢复通道）** | **7** | **202,251** | 0 引用 ＋ 源 `.py` 在盘 ＋ 非归档区 |
| **B 须 PI 逐单令** | ≥2,260 | ≥490 MB | 有引用面／证据件／留痕件／任何 `.md` 交付件／今日在途工作件 |
| **C 宜归档** | 144＋（另 `results\.tmp` 58） | 7.9 MB＋ | 同族旧版／早期纪元／工作面整体 |
| **D 禁动** | 1,700＋ | 60 MB＋ | 钉定锚件／`pi_rulings`／备忘录两版／`results` 交付 md／归档区 |

### §3-A A 类（7 件，逐件；皆为 `.pyc`，源 `.py` 在盘）

| # | 路径 | bytes |
|---|---|---:|
| 1 | `tools\_archive_purge_2026_10_17\__pycache__\recycle_channel.cpython-314.pyc` | 5,826 ★验道样本 |
| 2 | `tools\__pycache__\llm_client.cpython-314.pyc` | 11,727 |
| 3 | `tools\__pycache__\exp_harness.cpython-312.pyc` | 39,384 |
| 4 | `tools\__pycache__\exp_harness.cpython-314.pyc` | 44,342 |
| 5 | `tools\__pycache__\distortion_calculator.cpython-314.pyc` | 62,806 |
| 6 | `.mavis\scripts\cleanup511\__pycache__\recycle_exec.cpython-314.pyc` | 10,525 |
| 7 | `verifier\audit\__pycache__\conservation.cpython-314.pyc` | 27,641（⚠ 删 `.pyc` 不触锚源；若取「verifier 整树禁动」读则移 D） |

**另登记不删**：6 个 0 件空目录（`.tmp\github_survey_`／`.tmp\whitelist_backup_2026_10_17\_pre_mod`／`.tmp\_pre_mod\__pycache__`／`.tmp\__pycache__`／`docs\reviews`／`results\__pycache__`）。

### §3-B B 类（代表性；逐单令方可动，**体积序**）

1. `kdcensus_20261020_ea_data.json`（273.1 MB）—— 被 `_ksepcal9_release_pro_release_text_2026_10_21.md` L128 与 `_stage1_gap_exhaustive_audit_2026_10_20.md` L308 指名 ⇒ **KD/EA 普查原始数据面，⛔0 自判可删**；须 PI 先裁其派生摘要是否已入权威件。
2. 其余 6 件 `>5 MB` `.json`（54.6 MB）。
3. 30 件 `.tsv`（56.6 MB，全在 `.tmp`）＝`_h5aud_full_*`×4＋`_h5full2_*`×4＋`_h5full_*`×4＋`_h5aud_gate_*`×4＋`_h5gate2_*`×4＋`_h5gate_*`×4＋`_h5pilot_*` 族。
4. 28–30 件 0 字节件（全在引用链上）。
5. `.tmp\_cleanup_sha_prefix_index_4zone_2026_10_21.txt`（4,008,208 B）—— 前案明载「⛔0 删」（幽灵判定之仪器面）。
6. `.tmp\_c514_remote_blobs_2026_10_18`（514 件／20.1 MB）—— 远端比对底本。
7. `results` 根层 1,017 件 `.md` 交付件（48.8 MB）／`letters` 141 件／`results` 根层 89 件 `.py`／仓根 0 引用探针脚本 11 件。

### §3-C C 类（宜归档；移动须 PI 逐单令）

同族旧版 28 件（前案 `_cleanup_noise_register_2026_10_21.md` §4.1 逐件在册）＋ 早期纪元 116 件／7,875,415 B（< 2026-09-20，逐件见 `_results_index_v2_2026_10_21.md` §3）＋ `results\.tmp` 58 件／3,047,447 B（审计探针族）＋ `.tmp` 工作面整体 4,032 件／514.1 MB（**移动前必先出索引件**）。

### §3-D D 类（禁动）

18 frozen（16 anchor ＋ 2 anchor JSON，含 `KT_ABC1_anchors_sha256_12.json` `03c6c01f3697` 等）／5 制品 baseline（`corpus/v20/by_model/` 五件，尺寸与在册邀请函逐字吻合）／schema v1（`_v3x_frozen_schema_v1.json` 12,919 B·`9e99dcc4d920`）／4 plugin spec／P-G V0·V0.1 三件／`verifier/` 105 件（内建脚本）／`pi_rulings` 234 件／备忘录两版（558,430 B·273,072 B）／`results` 交付 md 1,017 件／归档区（`results\_archive_*` 32 件 ＋ `_remote_pullback_2026_10_17` 219 件 ＋ `pycache_sink` 8 件 `.pyc`，**仅列名，未触**）。

## §4 远端瘦身方案（只出方案；⛔0 联网·⛔0 执行）

### §4-1 仓内既有测量底账（转引，未向远端复核）

| 时点 | 载体 | 关键数 |
|---|---|---|
| 10-18 | `.tmp/ev18_evidence.json`（417,820 B） | head `7a5093f939b5…`；**tree_blobs 3,739**（前一 head 3,686）；`tree_truncated=False`（枚举完整）；local 2,017／remote 3,739／same 286／diff 0／local_only 1,731／remote_only 3,453 |
| 09-17 | `_letter_to_mavis_full_mirror_request_2026_09_17.md`（拉回区） | local_only 781／remote_only 612；**排除集合 358 件**（含 PNG 74＋paper/ 21）；remote_only 内容：verifier/ 99、`v3x-1week-kill-2026-09-18/` 399、其余 114 |
| 09-17 | `_letter_to_kimi_push_v3_final_2026_09_17.md` | **每批 ≤50 件**；`v3x-1week-kill` 399 件默认保留（删除属 destructive，须明示批准） |
| 10-12 | `results/_upload_plan_2026_10_12.json`／`_upload_ledger_2026_10_12.json` | plan 830；head `fb0ee9963b91…`；**triad_ok 三联校验**（sha256_full＋remote_blob_gitsha1＋local_gitsha1） |
| 10-18 | `.tmp/_c514_classify2_2026_10_18.json` | 514 remote blob 逐件双口径比对（cal_hit 1/8） |

### §4-2 判读

远端 `tree_blobs` **3,739 ＝ 本地 2,017 之 1.85 倍**；remote_only 3,453／local_only 1,731 ⇒ **本地瘦身不会自动瘦远端**。远端臃肿主因＝`_september_workspace/` 镜像树、`verifier/`、`v3x-1week-kill-2026-09-18/`（399）、PNG 74、`paper/` 21 之累积。远端仓名 `deposon-v3x-1week-kill`（`deposon_team/plugins/github_dir_structure_2026_09_18.md` 在册）。

### §4-3 步骤（待 PI 授权后由 PI 渠道执行）

- **S1 冻结基线**：head ＋ tree_blobs ＋ `truncated=False` ＋ 排除集合 358 入 manifest（缺 `truncated` 之树视为无效）。
- **S2 分批**：每批 **≤50 件**，按目录切分；非 force、不 rewrite 历史、不 force-push。
- **S3 每批比对**：`git/trees?recursive=1` 取远端全树逐件比对（沿 C514 逐件字段 `cls`／`local_gitsha1_12`／`remote_gitsha1_12`／`hunks`／`substantive`）。
- **S4 manifest 入库**：rel／sha12／sha256_full／git_sha1／bytes／zone／triad_ok／batch_no／timestamp；入库后方进下一批。
- **S5 密钥扫描**：每批前跑 desensitization 与密钥残留扫描；⚠ 10-18 底账 desen53／collision16 之 raw 皆 404（present 0）⇒ **须重测后方可据以判断**。
- **S6 排除集合**：PNG 74／`paper/` 21／归档区 32／`v3x-1week-kill` 399 默认保留（destructive 须 PI 逐单）。
- **S7 每批前后对照表**：tree_blobs／local_only／remote_only／总字节／件名清单。
- **S8 收尾**：全量比对 ＋ `remote_slimming_receipt`（head／批数／净减件数／逐批清单）。

## §5 最小安全执行序（若 PI 说「放开手脚」）

- **Step 0 静默闸（先决）**：现测 +26 件漂移、6 件今日在途工作件 ⇒ **无棒在途方可动**。
- **Step 1 A 类 1 件验道**：取 `recycle_channel.cpython-314.pyc`（5,826 B），走 `recycle_channel.py`（`SHFileOperationW`＋`FOF_ALLOWUNDO`）。**四验**：①`$I`／`$R` 成对 ②`decode_i()` 于 `$I` **偏移 28** 解出原路径逐字吻合（记录实测 `path_offset`）③原件 `Test-Path=False`（长名式复测）④源 `.py` 仍在盘且 SHA-12 未变（`06619281cd09`）。缺一即停手报回。
- **Step 2 分批 ≤12 件/批**：每批前后出件数／体积对照表（全仓／`.tmp`／`results`／回收站新增 `$I`+`$R` 对数）。首批 7 件 → 预期 −7 件／−202,251 B。
- **Step 3 B 类逐单令**（体积序，见 §3-B）。
- **Step 4 C 类**：先出索引件再谈移动；每移一件即预生幽灵。
- **Step 5 D 类永不动**。

## §6 老实交代

1. 本件之体量画像与分类清单皆为**时点截面**（00:39–00:52；仓为活面，件数 +26）。
2. **引用面仪器仅覆盖文本类**（5,785 件／135,242,359 B），**未覆盖 `.json`（425.6 MB）** ⇒「零引用」为**上界**，A 类实际可删面可能更小。
3. **远端面全为仓内既有测量件转引**（10-12／10-17／10-18），0 联网、0 远端复核；10-18 之 desen53／collision16 raw 皆 404。
4. **D 类 `expected_sha256_12` 系转引 schema v1 登记值，未逐件复算**（属禁动面；可复算载体 `_verify_15frozen.py`）；归档区仅列名与件数、0 触。
5. **本件系 explore 棒之勘查果，由主代理落盘**（该角色无 write 工具）；棒之全文报回含更细列名（最大 30 件逐件表、21 件零引用件全名单、重复 8 组逐组表），本件为其可执行之浓缩版。0 删／0 移／0 改名／0 新建目录／0 联网／0 读 key／0 落五终判／0 闭 KD／0 代裁。

*件止。勘查：explore `bg_def9cc59`（2026-10-22 00:39–00:52）· 落盘：主代理 mavis（00:5x）。*
