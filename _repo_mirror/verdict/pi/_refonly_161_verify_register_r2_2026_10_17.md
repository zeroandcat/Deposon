# 161 件之**要件②重测登记件**（`_r2`）｜判读方向 ＝ 草案 §2-2 逐字六类

| 项 | 值 |
| :-- | :-- |
| **落盘路径** | `results/_refonly_161_verify_register_r2_2026_10_17.md` |
| **件之性质** | **核验登记件**（①沿用＋②新测＋逐件留痕）· **⛔ 0 择读** · **⛔ 0 宣告任一件之终判** |
| **授权** | PI 2026-10-17 ≈16:18 裁「**采认 ＋ 修正探针重测**」·卡 `ask_c74c097fc9b0521ea53f7788` Q1 `opt1`（**转述**·见 §0-KD-1） |
| **上游** | 判断件 `bd94d12323e0`（§8 三证清单 E-1／E-2／E-3）→ 本件 ＝ **E-1＋E-2 之正典重测** |
| **判读之唯一权威** | 口径草案 `536a3064ad38` §2-2（`results/_citation_no_utility_caliber_draft_2026_10_17.md`）——**⛔ 0 与并存版 `f5bad2e2ff00` 混用**（该版 0 载六类） |
| **谓词版本** | `REQ2-R2.0.0`（探针 `.tmp/refonly161_r2_probe.py` · **另立副本**·⛔ 0 改前棒 `b4bafa0860d1` 原件一字） |
| **本棒写面** | 本件 ＋ `.tmp/refonly161_r2_probe.py` ＋ `.tmp/refonly161_r2_out.json` ＋ `.tmp/refonly161_r2_tally*.py` ＋ 本构建器 |
| **既有件触动数** | **0**（⛔ 0 删 · ⛔ 0 移 · ⛔ 0 改名 · ⛔ 0 回改一字 · **核验非清理**） |

## §0-KD 卡面未开卷

本件之卡号／所择项系**转述**（派工面）⇒ 全部结论仅据在盘件。**实测**：全仓（含 `.tmp/`·`results/`·`letters/`·`docs/`）检索 `c74c097fc9b0521ea53f7788` ＝ **0 命中** ⇒ 卡面**未在盘**；卡面若另有约束，须以其为准。

---

## §1 读件与指纹（**逐字回读 · 本棒直算 SHA-256 之后取 `[:12]`**）

| # | 件 | 路径 | SHA-12 | bytes | mtime |
| :-: | :-- | :-- | :-: | --: | :-- |
| 1 | 判断件（上游） | `results/_refonly_161_reading_verdict_2026_10_17.md` | `bd94d12323e0` | 39,243 | 2026-10-17 16:13:11 |
| 2 | 口径草案（判读权威） | `results/_citation_no_utility_caliber_draft_2026_10_17.md` | `536a3064ad38` | 49,332 | 2026-10-17 13:22:41 |
| 3 | 前探针（⛔ 0 改） | `.tmp/refonly161_verify_probe.py` | `b4bafa0860d1` | 15,090 | 2026-10-17 15:44:00 |
| 4 | **本棒探针（`_r2`）** | `.tmp/refonly161_r2_probe.py` | `c3171dc8cdf9` | 26,360 | 2026-10-17 16:34:09 |
| 5 | 白名单登记件（候选池＋保护面） | `results/_whitelist_register_2026_10_17.md` | `7511b98c6483` | 120,358 | 2026-10-17 12:09:31 |
| 6 | 前棒登记件（① 之源） | `results/_refonly_161_verify_register_2026_10_17.md` | `74d63d55ee97` | 69,821 | 2026-10-17 15:47:49 |
| 7 | **本棒探针产物** | `.tmp/refonly161_r2_out.json` | `c47c6f4afddd` | 2,029,558 | 2026-10-17 16:37:50 |
| 8 | 前棒探针产物（① 之源） | `.tmp/refonly161_probe_out.json` | `a87f13960926` | 1,342,186 | 2026-10-17 15:46:41 |

📌 **指纹约定实测自证**：`.tmp/_659_compact.txt` 直算 SHA-12 ＝ `795862c09a40` ＝ 白名单登记表所载之 `795862c09a40` ⇒ **约定 ＝ SHA-256 前 12 位**（前棒同一约定）。

### §1-1 逐字回读之要点（本件之判读所依）

| 来源 | 逐字要点 | 锚 |
| :-- | :-- | :-: |
| 判断件 §8 | **E-1** 类 5 之「活」性须「逐引用件扫描其**自身**之被引用／被执行面」；**E-2** 类 6 须「**全文**扫 `OBLIG` 之义务表述词」；**E-3** 人工阅件补扫（`V-list` 外） | `bd94d12323e0:176-178` |
| 判断件 §7-R-4 | 乙读之 0 ＝ **假证伪**（工具／构造层面失灵）：`② ✗`（类 5 纯扩展名赋值 ＋ 类 6 仅前 3 命中行）；`③ ✗`（引用件自身是否被调用之证据未取） | `bd94d12323e0:160` |
| 草案 §2-2 | 六类逐字：类 5「该引用件**自身被** import／执行／读取为数据」；类 6「引用**承载义务**（载『待办／须重建／须核／失效引用』之义务性表述）」；二分「类 1–4 ＝ 史实记录面；类 5–6 ＝ 活义务面」；优先级「**一活义务面即出本面**」 | `536a3064ad38:117-127` |
| 草案 §2-2 ⚠ | 「类 5／类 6 之『活』性之判定**依赖全引用集与调用面扫描**，⛔ **0 仅凭扩展名或文件名断定**（`.py` 未必被调用，`.md` 未必已失效）」 | `536a3064ad38:129` |
| 白名单 §4-3 | 保护面 ＝ ①白名单集 699 件本体 ②其备份副本（`.tmp/whitelist_backup_2026_10_17/`）；射程「**0 删 · 0 移 · 0 重命名 · 0 改**」；「**保护面 ≠ 永久保留**——若 PI 后续另有裁决，以其裁决为准」 | `7511b98c6483:789-791` |

> 📌 **本棒 ⛔ 0 解除保护面**、⛔ 0 代裁解除（沿 KD-10 之正交性）：**无论择何读，本件皆不产生任何清理许可**。

---

## §2 前棒构造失灵之三证 → 本棒之修正（**逐条对位**）

| # | 前棒（`b4bafa0860d1`）之实码 | 失灵性质 | 本棒（`REQ2-R2.0.0`）之修正 | 可复算之验证点 |
| :-: | :-- | :-- | :-- | :-: |
| **X-1** | `:186` `if is_code: cls.add('5')` —— 类 5 **纯扩展名无条件赋值**（⛔ 违草案 `:129`） | 构造面失灵（假证伪） | 类 5 须**内容面核验**：①**脚本／工具类**（kind＝script）**且**②其**自身正文**含计数之调用形态（写模式 `open` 与纯路径拼接已排除）→ `script+content_call`；③或**被动消费**（全仓存在以调用形态／解释器调用引用该引用件之命中行）→ `passive` | `results` 之 `citer_detail[].ev[5].via` ∈ {`script+content_call`,`passive`,二者兼具}；计数见 §4-2 |
| **X-2** | `:274` `lines: [...][:3]` —— 类 6 命中面**截前 3 行** | 证据面不全（E-2 未取） | 类 6 之命中面 ＝ **全命中行**（`hit_lines` 不截断，附 `line` ＋ `literals` ＋ `text`）；另落**宽集诊断**（`wide_diag`，前棒 `OBLIG` 之 20 词）**⛔ 0 充判据** | `citer_detail[].ev[6].n_hit_lines_scanned` ＝ 该引用件命中行总数（未截断） |
| **X-3** | `:303` `req2_strict_ok = len(load_sites)==0`，`load_sites` 由 `vlist_hits` 派生 ⇒ **②与①同源** | **零分辨力**（②＝①之复述） | ② 谓词**独立于①**：类 5 走**引用件自身之调用面**（needle ＝ 引用件名，pass B，178 needle），类 6 走**引用行之义务表述**；`vlist_hits` 仅作 **① 之交叉校验**（`req1_vlist_hits_xcheck`），**⛔ 0 参与②之任一判定** | `n_needles_B` ＝ 178（引用件名）vs `n_needles_A` ＝ 465（目标件名）；两遍扫描独立 |

> 📌 **前棒探针 ⛔ 0 改一字**（指纹 `b4bafa0860d1` 前后一致·见 §9）——修正**另立副本** `_r2`。

### §2-1 首二跑之失败与修正（如实登记 · ⛔ 0 隐去）

| 跑次 | 状态 | 失败点 | 修正 |
| :-: | :-- | :-- | :-- |
| 1 | ❌ 失败（`KeyError: 'live'`） | 判定环节漏带 `live` 字段（两遍扫描已完成） | 补齐 `live`／`hist_mark`／`ob_hit`／`content_call` |
| 2 | ⚠ 跑毕但**构造有偏** | **白名单备份副本未被排除**出引用集（前棒有排除 ⇒ 与①之引用集不可比） | 增 `BACKUP_PREFIX` 排除（引用件数由 3084 降至 2597）＋ 落 `excl.whitelist_backup` 计数 |
| 3 | ✅ 采用 | —— | 同上 ＋ 类 6 全文诊断字段由 `ev[6]`（未命中即缺）改为**独立字段** `c6_fulltext_diag`（修诊断盲区） |

> 📌 三跑之间判读规则**未变**（`REQ2-R2.0.0` 之口径恒定）；所改者**仅实现缺陷与诊断可见性**。跑 3 之 `n_citer_files` ＝ **178**（前棒 177 ＋ 本棒快照新增 1 件引用文件，见 §6）。

---

## §3 谓词 `REQ2-R2.0.0` 之全文（**判读方向 ＝ 草案 §2-2 · ⛔ 0 新拟数值阈值**）

### §3-1 六类之机械判据（逐类 · ⛔ 0 仅凭扩展名断定 5／6）

| 类 | 面 | 本棒判据（逐字可复算） | 计入判定的证据 |
| :-: | :-- | :-- | :-: |
| **1** | 登记／落账面 | 件名含 `register`（大小写不敏感）**或** 首表内「件性质」＋「逐字登记」之自称 | 名称／自称标记 |
| **2** | 清单／清册面 | 件名含 `list`／`inventory`／`mapping` **或** 正文之「逐件表」节 | 名称标记／正文节 |
| **3** | 勘误／并列注记面 | 件名含 `corrigendum`／`erratum` **或** 自称「勘误注记」／「并列注记」 | 名称标记／自称 |
| **4** | 备忘录／会话史面 | 件名含 `_root_session_history_memo_` | 名称标记 |
| **5** | 活代码面 | （**kind ＝ script／工具**）**且**（自身正文含计数之调用形态 **OR** 被动消费证据） | `via` ＝ `script+content_call`／`passive`／二者兼具 ＋ 引用件自身调用行号 ＋ 被动消费之 `at:line` |
| **6** | 活文档面 | 引用件之**引用命中行**载草案四词之一（`待办`／`须重建`／`须核`／`失效引用`）——**义务表述之逐字形态以草案为准** | `hit_lines`（`line` ＋ `literals` ＋ `text` 逐行全留） |

**二分与优先级（草案 `:126-127` 逐字）**：类 1–4 ＝ 史实记录面（②**真**）；类 5–6 ＝ 活义务面（②**假**）；「若目标件**同时**有史实记录面引用**与**活义务面引用 ⇒ 要件② **假**（**一活义务面即出本面**）」。

### §3-2 「json 枚举件单纯载名 vs 载义务表述」之分判（派工面所点之差额来源）

对 `DATA_EXT` ＝ `.json`／`.jsonl`／`.yaml`／`.yml`／`.toml`／`.ini`／`.cfg`／`.conf`／`.xml`／`.csv` 之引用件，本棒**逐件分判**并落 `json_enum` 字段：

| 分判 | 判据 | 实测（引用件·件次） |
| :-: | :-- | --: |
| 载名（单纯枚举） | 引用命中行**无**草案四词 ⇒ 单纯载名 | **1,464** |

> 🔴 **实测结论（与派工面所点之差额来源相左）**：本池 **1,464** 个 json／数据类引用件·件次**全部为「单纯载名」**，**0 件次**在引用行上载义务表述 ⇒ **差额之真正来源不是「json 件载义务表述」，而是「json 件被读取为数据」**（类 5 之被动面，见 §4-2）。详见 KD-2。

### §3-3 三读法（**同一套证据 · 三种判读面 · ⛔ 0 由本件择定**）

| 读法 | ② 成立之条件 | 口径依据 |
| :-: | :-- | :-- |
| **R2-A（主读法）** | 每个引用件**无类 5 且无类 6**（＝「**无活义务面**」之正面判读） | 草案 `:113` 标题字面「**无活义务面**」＋ `:126` 二分 |
| **R2-B** | 每个引用件**无类 5（限 `script+content_call` 之脚本／工具面）且无类 6**（被动消费不计入） | 草案 `:123` 类 5 之机械标记「该引用件**自身被** import／执行／读取为数据」**收窄至脚本／工具面**；派工面「如其为脚本／工具且含加载／调用语义方为类 5／类 6」 |
| **R2-C** | R2-B **且** 每个引用件**至少命中一类 1–4 之显式标记** | 草案 `:126`「类 1–4 ＝ 史实记录面」之**穷尽读法**（未标记者 ⩾ 史实面 ⩾ 本面） |

> 📌 **类 6 之判读面另有一维敏感（草案未载）**：`引用命中行`（R2-A／B／C 之采）vs `引用件文档全文`。实测见 §4-3 ⇒ 落 **KD-1**（**口径开口 · ⛔ 0 由本件择定**）。

---

## §4 汇总（**② 之三数 · 三读法并报**）

### §4-1 主表

| 读法 | **② 成就 N1（可转判定）** | **② 不成就 N2** | **测量面不明 N3** | ＋ ① 成立之合取数（①② 之合取） |
| :-- | --: | --: | --: | --: |
| **R2-A**（主读法 · 无活义务面） | **0** | **161** | **0** | **0** |
| **R2-B**（类 5 限脚本／工具面） | **55** | **106** | **0** | **55** |
| **R2-C**（严格 1–4 标记读法） | **0** | **161** | **0** | **0** |
| **R2-B ＋ 类 6 取文档全文**（敏感面） | **7** | **154** | **0** | **7** |

**测量面 N3 ＝ 0 之依据**：161／161 件在盘存在（`missing_on_disk` ＝ **0**）· SHA-12 与白名单登记表**逐位相符 161／161**（`sha_mismatch` ＝ **0**）· 读取错误 **0** · 遍历错误 **0** ⇒ **无「证据不足而不可判」之件**。⚠ **N3 ＝ 0 之口径面含义见 KD-1／KD-2**（口径未载 ≠ 本棒擅自择读）。

**R2-B 之 55 件（`② 成就` 之唯一有数之读法）**：`.tmp/_659_compact.txt`、`.tmp/_659_overlap_digest.txt`、`.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md`、`.tmp/_docwriter_night_measure.json`、`.tmp/_dw_abs_scan.json`、`.tmp/_lit_log.txt`、`.tmp/_m5_k5_net.json`、`.tmp/_m5_k5_net2.json`、`.tmp/_m5_reaudit_archive_out.json`、`.tmp/_t2_t3_lit_search2.py`、`.tmp/_t2_t3_llm_probe.py`、`.tmp/_t2_t3_prex_a_route.py`、`.tmp/_t2_t3_prex_a_route_out.json`、`.tmp/docwriter_v42_verify.py`、`.tmp/docwriter_v46_card_raw.py`、`.tmp/docwriter_v46_probe.py`、`.tmp/docwriter_v46_verify.py`、`.tmp/docwriter_v46_verify_r2.py`、`.tmp/docwriter_v48_norm.py`、`.tmp/docwriter_v49_norm.py`、`.tmp/docwriter_verify_v45.py`、`.tmp/docwriter_write_v43.py`、`.tmp/docwriter_write_v44.py`、`.tmp/docwriter_write_v45.py`、`.tmp/evauditor_one_finish_write.py`、`.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py`、`.tmp/ge01_full_1494_precheck_2026_10_16.py`、`.tmp/ge01_full_1494_resume32_collect_2026_10_16.py`、`.tmp/ge01_full_1494_resume32_readout_2026_10_16.py`、`.tmp/ge01_gate_write.py`、`.tmp/ge01_s3b_v_exec_r1_write_2026_10_16.py`、`.tmp/ge02_build.py`、`.tmp/ge02_recompute.py`、`.tmp/kd14_absorption_probe.py`、`.tmp/kd14_carrier_probe.py`、`.tmp/kd14_m4_corrected.py`、`.tmp/klm41_3_ts_collect_2026_10_16.py`、`.tmp/m08_r1_amend2_2026_10_16.json`、`.tmp/m08_r1_amend3_2026_10_16.json`、`.tmp/m08_r1_amend_2026_10_16.json`、`.tmp/me_llm_calls_2026_10_16.jsonl`、`.tmp/t2b_census_2026_10_16.py`、`.tmp/t2b_derive_2026_10_16.py`、`.tmp/t2b_fetch_facts_2026_10_16.py`、`.tmp/t2b_freeze_2026_10_16.py`、`.tmp/t2b_freeze_v2_2026_10_16.py`、`.tmp/t2b_impl_audit_2026_10_16.py`、`.tmp/t2b_inspect_facts_2026_10_16.py`、`.tmp/t2b_measure_2026_10_16.py`、`.tmp/t2b_patch_harness_2026_10_16.py`、`.tmp/t3_baseline_procedure_probe.py`、`.tmp/t3_nt_measure_2026_10_15.py`、`.tmp/t3_nt_verify.py`、`.tmp/t3_postchange_equiv.py`、`.tmp/t3_postcheck.py`

**R2-B ＋ 类 6 取全文 之 7 件（最严读法下之成就集）**：`.tmp/docwriter_v46_card_raw.py`、`.tmp/docwriter_v46_probe.py`、`.tmp/docwriter_v46_verify.py`、`.tmp/docwriter_v46_verify_r2.py`、`.tmp/docwriter_v48_norm.py`、`.tmp/docwriter_v49_norm.py`、`.tmp/ge01_gate_write.py`

### §4-2 ② 不成就之成因分解（**驱动因 · 引用件·件次**）

| 成因 | 引用件·件次 | 受影响之件 |
| :-- | --: | --: |
| **类 5 · 脚本／工具面**（`script+content_call`） | **198** | **106／161** |
| **类 5 · 被动消费**（`passive`：`json.load`／`os.path.join`／`importlib` 等以**该引用件**为对象） | **481** | **161／161**（其中仅由被动面致其失败者 55 件） |
| **类 6**（引用行载义务表述） | **0** | **0／161** |
| 类 5 兼类 6 之件 | **0** | 0 |

**决定性锚点（去重 Top 12 · 可逐条回读）**：

| # | 引用件 | 消费／调用面 | 引用件·件次 |
| :-: | :-- | :-- | --: |
| 1 | `inventory_compare.json` | `step5_register.py:L40` | 161 |
| 2 | `step3_bulk_result.json` | `step5_register.py:L43` | 160 |
| 3 | `cleanup511_manifest_2026_10_17.json` | `make_register.py:L13` | 124 |
| 4 | `_cleanup_inventory_2026_10_15.md` | `_write_predelete_caliber_draft.py:L34` | 15 |
| 5 | `_cleanup_r2_report.py` | 自身 `L5` 起含调用形态 | 15 |
| 6 | `dscan_write_01.py` | 自身 `L2` 起含调用形态 | 12 |
| 7 | `step4_bin_audit.json` | `step5_register.py:L44` | 11 |
| 8 | `_cleanup_r2_scan4.py` | 自身 `L16` 起含调用形态 | 9 |
| 9 | `docwriter_write_v43.py` | 自身 `L1` 起含调用形态 | 8 |
| 10 | `docwriter_write_v44.py` | 自身 `L5` 起含调用形态 | 8 |
| 11 | `_cleanup_r2_scan3.py` | 自身 `L15` 起含调用形态 | 6 |
| 12 | `_cleanup_r2_scan2.py` | 自身 `L15` 起含调用形态 | 5 |

### §4-3 类 6 之判读面敏感性（**草案未载 · KD-1**）

| 判读面 | 类 6 成立之件 | R2-B 之②成就数 |
| :-- | --: | --: |
| **引用命中行**（主读法之采 · 草案「引用**承载义务**」之机械代理） | **0／161** | **55** |
| **引用件文档全文**（同一四词 · 不限引用行） | **129／161** | **7** |

📌 **全文面之语料样本**：`cleanup511_manifest_2026_10_17.json:70259` 载「……须核引用……」（被引**条文数据**，非义务表述）；`results/_dangling_630_remediation_list_2026_10_17.md`；`results/_pi_card_answers_register_2026_10_17_v45.md`／`v50.md`。⇒ **全文面会把「引用他件之条文／义务词」误计为「本引用承载义务」** ⇒ 二读法之差 **48 件**（55 → 7）。🔴 **择读归 PI · 本件 ⛔ 0 择定**。

### §4-4 引用件面之构成（全池 2,597 件次 ／ 178 个不同引用件文件）

| 项 | 值 |
| :-- | --: |
| 引用件·件次（kind 分布） | `data` 1,464 · `doc` 935 · `script` 198 |
| 类标记·件次合计 | 类1 663 · 类2 673 · 类5 679 |
| 史实标记（1–4）且非活面 | 796 |
| 未标记 1–4 且非活面（`面 ＝ 未标记（非1-4/5/6）`） | 1,122 |

> 📌 **未标记面之主体**（1,122 件次）：`_cleanup_r2_scan4_out.json`(161)、`pk_refonly_tally_out.json`(161)、`wlbk_2026_10_17_backup2_out.json`(161)、`wlbk_2026_10_17_backup_out.json`(161)、`wlbk_2026_10_17_scan_out.json`(161)、`_cleanup_r2_scan_out.json`(154)

---

## §5 逐件四栏表（**161 行 · 全量 · 无省略**）

**四栏之定义**：① ＝ 引用形态（**沿用前棒** `74d63d55ee97` 之实测值·本棒 ⛔ 0 复判）；②  ＝ 引用件性质（**本棒新测** · `REQ2-R2.0.0`）；③  引用集完整性（件次 now／prior）；④  判读依据（决定性锚点 ＋ 类计数）。

| # | 件（路径 · SHA-12 · bytes） | ① 引用形态（前棒复用） | ② 引用件性质（本棒新测） | ③ 引用集 | ④ 判读依据（锚点） |
| :-: | :-- | :-: | :-: | :-: | :-- |
| 4 | `.tmp/_659_compact.txt`<br>`795862c09a40` · 155,628 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×3／2×5／5×5 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 5 | `.tmp/_659_overlap_digest.txt`<br>`4f20b8085fb9` · 239,157 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×3／2×5／5×5 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 42 | `.tmp/_cleanup_r2_cleanlist.json`<br>`ce71dda28157` · 810 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×4／2×4／5×6 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 43 | `.tmp/_cleanup_r2_exec.py`<br>`a2029c340ac5` · 7,884 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×4／2×4／5×8 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 44 | `.tmp/_cleanup_r2_exec_journal.json`<br>`cd636cb64813` · 10,327 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 20／19（+1）<br>类 1×4／2×4／5×10 | 类5·脚本面 `.tmp/_cleanup_r2_exec.py`（自身 L8 起含 14 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 5 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 45 | `.tmp/_cleanup_r2_postcheck.json`<br>`720b25650bcd` · 6,652 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×6 | 类5·脚本面 `.tmp/_cleanup_r2_postcheck.py`（自身 L3 起含 8 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 5 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 46 | `.tmp/_cleanup_r2_postcheck.py`<br>`cfd60493f18d` · 4,585 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 5 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 47 | `.tmp/_cleanup_r2_scan.py`<br>`60d6d3d37076` · 11,507 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×4／2×4／5×7 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 48 | `.tmp/_cleanup_r2_scan2.py`<br>`7019c7b8d728` · 12,112 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×4／2×4／5×6 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 49 | `.tmp/_cleanup_r2_scan3.py`<br>`46b7b8230e86` · 12,389 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 50 | `.tmp/_cleanup_r2_scan_out.json`<br>`3b107c078490` · 758,995 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×4／2×4／5×9 | 类5·脚本面 `.tmp/_cleanup_r2_exec.py`（自身 L8 起含 14 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 5 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 53 | `.tmp/_corrupt_ge01_readiness_firstwrite_2026_10_13.md`<br>`3a240806c2d3` · 31,745 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 72 | `.tmp/_docwriter_night_measure.json`<br>`f5bacfac3f1c` · 22,679 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 17／16（+1）<br>类 1×4／2×6／5×4 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 80 | `.tmp/_dw_abs_scan.json`<br>`5c584826ed16` · 56,306 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 98 | `.tmp/_e_q_exec.json`<br>`d4bd8c92201f` · 6,161 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×6／2×6／5×5 | 类5·脚本面 `.mavis/scripts/cleanup511/make_register.py`（自身 L3 起含 8 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 99 | `.tmp/_e_q_exec.txt`<br>`e3b0c44298fc` · 0 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 21／20（+1）<br>类 1×7／2×6／5×7 | 类5·脚本面 `.mavis/scripts/cleanup511/make_register.py`（自身 L3 起含 8 处调用形态）；类5·被动 `.tmp/archive_survey_outdupe.json` ← `archive_survey_overlap.py:L4`（call:json.load,open(read)）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 124 | `.tmp/_lit_log.txt`<br>`b062da7b654a` · 8,733 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 125 | `.tmp/_m5_k5_net.err`<br>`e3b0c44298fc` · 0 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 21／20（+1）<br>类 1×7／2×5／5×7 | 类5·脚本面 `.mavis/scripts/cleanup511/make_register.py`（自身 L3 起含 8 处调用形态）；类5·被动 `.tmp/archive_survey_outdupe.json` ← `archive_survey_overlap.py:L4`（call:json.load,open(read)）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 126 | `.tmp/_m5_k5_net.json`<br>`9d7fe894a26b` · 92,060 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 17／16（+1）<br>类 1×4／2×5／5×4 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 128 | `.tmp/_m5_k5_net2.json`<br>`b2bc158e7499` · 952,252 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 18／17（+1）<br>类 1×4／2×6／5×4 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 130 | `.tmp/_m5_k5_scan.json`<br>`ebf1ad76dc8a` · 9,530 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 21／20（+1）<br>类 1×7／2×5／5×7 | 类5·脚本面 `.mavis/scripts/cleanup511/make_register.py`（自身 L3 起含 8 处调用形态）；类5·被动 `.tmp/archive_survey_outdupe.json` ← `archive_survey_overlap.py:L4`（call:json.load,open(read)）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 133 | `.tmp/_m5_reaudit_archive_out.json`<br>`e3542ccb4d3e` · 654 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 135 | `.tmp/_m5_reaudit_detail.txt`<br>`8c117d51fc64` · 9,214 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×5／5×5 | 类5·脚本面 `.tmp/_m5_reaudit_detail.py`（自身 L3 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 287 | `.tmp/_t2_t3_lit_search2.py`<br>`c0caa8ba29f1` · 4,946 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 288 | `.tmp/_t2_t3_lit_search2_out.json`<br>`13ffff0d0b28` · 29,596 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/_t2_t3_lit_search2.py`（自身 L11 起含 10 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 289 | `.tmp/_t2_t3_lit_search_out.json`<br>`cc70fac3d81b` · 26,588 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/_t2_t3_lit_search.py`（自身 L12 起含 11 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 290 | `.tmp/_t2_t3_llm_probe.py`<br>`5561f7af5662` · 4,544 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 291 | `.tmp/_t2_t3_llm_probe_out.json`<br>`993477af77db` · 5,331 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/_t2_t3_llm_probe.py`（自身 L18 起含 11 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 292 | `.tmp/_t2_t3_prex_a_route.py`<br>`c25af5d2966b` · 10,166 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 294 | `.tmp/_t2_t3_prex_a_route2_out.json`<br>`63f37ba943c1` · 6,949 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/_t2_t3_prex_a_route2.py`（自身 L16 起含 10 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 295 | `.tmp/_t2_t3_prex_a_route_out.json`<br>`3cad087a69c3` · 22,640 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 354 | `.tmp/_write_predelete_caliber_draft.py`<br>`82d7f9c628b6` · 32,826 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×3 | 类5·脚本面 `.tmp/docwriter_v49_norm.py`（自身 L3 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 355 | `.tmp/anch.py`<br>`c05693efbb30` · 1,484 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×5／2×4／5×6 | 类5·脚本面 `.tmp/_cleanup_r2_plus83_report.py`（自身 L3 起含 10 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 359 | `.tmp/archive_survey_census2.py`<br>`2863f5edca41` · 780 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 13／12（+1）<br>类 1×4／2×4／5×3 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 5 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 378 | `.tmp/docwriter_v41_probe.py`<br>`210a07303fe7` · 6,503 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_v41_scan2.py`（自身 L5 起含 11 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 379 | `.tmp/docwriter_v41_scan2.json`<br>`e988b26ba229` · 4,066 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 21／20（+1）<br>类 1×6／2×4／5×6 | 类5·脚本面 `.tmp/_cleanup_r2_plus83_report.py`（自身 L3 起含 10 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 380 | `.tmp/docwriter_v41_scan2.py`<br>`e88316a0fc2c` · 3,661 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 381 | `.tmp/docwriter_v42_scan.py`<br>`93d9c4c5c927` · 4,601 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v42.py`（自身 L3 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 382 | `.tmp/docwriter_v42_scan_out.txt`<br>`d1470a9eaea9` · 5,267 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×5／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v42_scan.py`（自身 L6 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 383 | `.tmp/docwriter_v42_verify.py`<br>`47c794a64dff` · 4,858 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 384 | `.tmp/docwriter_v42_verify_out.txt`<br>`c38b853adda1` · 2,899 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_v42_verify.py`（自身 L3 起含 10 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 385 | `.tmp/docwriter_v43_fp.py`<br>`000c7e036d9c` · 1,488 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v43.py`（自身 L1 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 386 | `.tmp/docwriter_v43_fp2.py`<br>`87ef5d8aba15` · 1,716 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v43.py`（自身 L1 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 387 | `.tmp/docwriter_v43_fp_out.txt`<br>`35a223091bbe` · 2,420 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×5／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v43_fp2.py`（自身 L1 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 388 | `.tmp/docwriter_v43_scan.py`<br>`5356708d6a6f` · 2,061 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v43.py`（自身 L1 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 389 | `.tmp/docwriter_v43_scan_out.txt`<br>`c80e849e7c99` · 2,353 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×5／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v43_scan.py`（自身 L1 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 390 | `.tmp/docwriter_v43_verify.py`<br>`2cf26203f12d` · 4,497 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v43.py`（自身 L1 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 391 | `.tmp/docwriter_v43_verify_out.txt`<br>`c1d14e3d7e06` · 759 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×5／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v43_verify.py`（自身 L1 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 392 | `.tmp/docwriter_v44_fp.py`<br>`4c2e2a4a2ad2` · 2,485 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×6／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v44.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 393 | `.tmp/docwriter_v44_fp_out.txt`<br>`6ab1382d766e` · 1,601 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×6／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v44_fp.py`（自身 L3 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 394 | `.tmp/docwriter_v44_fresh.py`<br>`855298e666f6` · 2,319 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×6／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v44.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 395 | `.tmp/docwriter_v44_fresh_out.txt`<br>`6d7d8ad5c4ed` · 1,646 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×6／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v44_fresh.py`（自身 L4 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 396 | `.tmp/docwriter_v44_scan.py`<br>`3cc9fa3130a4` · 3,822 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×6／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v44.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 397 | `.tmp/docwriter_v44_scan_out.txt`<br>`24663bc22391` · 2,290 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×6／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v44_scan.py`（自身 L4 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 398 | `.tmp/docwriter_v45_scan.py`<br>`c6703629a7b0` · 5,186 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v45.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 399 | `.tmp/docwriter_v45_scan_out.txt`<br>`28c06dd53ae4` · 1,661 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v45.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 400 | `.tmp/docwriter_v45_scan_out_r1.txt`<br>`28c06dd53ae4` · 1,661 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v45.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 401 | `.tmp/docwriter_v45_scan_out_r2.txt`<br>`ef49039e5d90` · 1,728 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×5／2×4／5×6 | 类5·脚本面 `.tmp/docwriter_v45_scan.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 402 | `.tmp/docwriter_v45_scan_r2.py`<br>`189764eebc91` · 4,212 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v45.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 403 | `.tmp/docwriter_v45_verify_out.txt`<br>`e5a0fdfbc914` · 2,031 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·脚本面 `.tmp/docwriter_verify_v45.py`（自身 L5 起含 1 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 404 | `.tmp/docwriter_v46_card_raw.py`<br>`b8754c12612b` · 1,652 B | ✔ | A ✘ ／ **B ✔** ／ C ✘（＋全文面 ✘） | 13／12（+1）<br>类 1×4／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 405 | `.tmp/docwriter_v46_card_raw.txt`<br>`e31064337198` · 26 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v46_card_raw.py`（自身 L3 起含 1 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 406 | `.tmp/docwriter_v46_probe.py`<br>`15d2a2cef38c` · 8,174 B | ✔ | A ✘ ／ **B ✔** ／ C ✘（＋全文面 ✘） | 13／12（+1）<br>类 1×4／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 407 | `.tmp/docwriter_v46_probe_out.txt`<br>`45358bad9e37` · 10,158 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·脚本面 `.tmp/docwriter_v46_probe.py`（自身 L3 起含 14 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 408 | `.tmp/docwriter_v46_timeshift_out.txt`<br>`4623d2f470da` · 708 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·脚本面 `.tmp/docwriter_v46_timeshift.py`（自身 L3 起含 4 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 409 | `.tmp/docwriter_v46_verify.py`<br>`7d657b923cf3` · 6,883 B | ✔ | A ✘ ／ **B ✔** ／ C ✘（＋全文面 ✘） | 13／12（+1）<br>类 1×4／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 410 | `.tmp/docwriter_v46_verify_r2.py`<br>`98878b701653` · 3,940 B | ✔ | A ✘ ／ **B ✔** ／ C ✘（＋全文面 ✘） | 13／12（+1）<br>类 1×4／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 411 | `.tmp/docwriter_v47_verify.py`<br>`9383724baaa4` · 1,220 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×5／2×4／5×3 | 类5·脚本面 `.tmp/docwriter_v47_write1.py`（自身 L2 起含 1 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 412 | `.tmp/docwriter_v47_write1.py`<br>`8fa8d72c3a69` · 62,466 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 22／21（+1）<br>类 1×7／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v51_addendum.py`（自身 L3 起含 4 处调用形态）；类5·被动 `results/_pi_card_answers_register_2026_10_17_v50.md` ← `docwriter_v50_append.py:L5`（call:open(read)）；未标记 1–4 者 11 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 413 | `.tmp/docwriter_v47_write2.py`<br>`1ee1ee14ac3e` · 48,627 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×6／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_v47_write1.py`（自身 L2 起含 1 处调用形态）；类5·被动 `results/_pi_card_answers_register_2026_10_17_v50.md` ← `docwriter_v50_append.py:L5`（call:open(read)）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 414 | `.tmp/docwriter_v48_norm.py`<br>`e39ea2ab2756` · 12,880 B | ✔ | A ✘ ／ **B ✔** ／ C ✘（＋全文面 ✘） | 13／12（+1）<br>类 1×4／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 415 | `.tmp/docwriter_v48_probe.py`<br>`8dfd0f40cdb5` · 4,448 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·脚本面 `.tmp/docwriter_v48_norm.py`（自身 L6 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 416 | `.tmp/docwriter_v48_probe_out.txt`<br>`48b1c4a81ad4` · 4,169 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·脚本面 `.tmp/docwriter_v48_probe.py`（自身 L5 起含 11 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 417 | `.tmp/docwriter_v49_norm.py`<br>`d1b3481335eb` · 16,740 B | ✔ | A ✘ ／ **B ✔** ／ C ✘（＋全文面 ✘） | 15／14（+1）<br>类 1×4／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 418 | `.tmp/docwriter_v49_probe.py`<br>`753b0ad48557` · 4,806 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 20／19（+1）<br>类 1×6／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v49_norm.py`（自身 L3 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 419 | `.tmp/docwriter_v49_probe_out.txt`<br>`c04bcaf87623` · 4,353 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_v49_norm.py`（自身 L3 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 420 | `.tmp/docwriter_verify_v44.py`<br>`19cfb64700a1` · 4,692 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×6／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v44.py`（自身 L5 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 421 | `.tmp/docwriter_verify_v44_out.txt`<br>`f3d33d095a8a` · 2,371 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×6／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_verify_v44.py`（自身 L4 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 422 | `.tmp/docwriter_verify_v45.py`<br>`92230e228d83` · 3,780 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 13／12（+1）<br>类 1×4／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 423 | `.tmp/docwriter_write_effect_v43.py`<br>`01098529c399` · 27,715 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×5／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v43.py`（自身 L1 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 424 | `.tmp/docwriter_write_v42.py`<br>`5cc438f6338d` · 66,543 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 21／20（+1）<br>类 1×7／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_v51_addendum.py`（自身 L3 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 425 | `.tmp/docwriter_write_v43.py`<br>`d5e6390b900d` · 33,607 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 426 | `.tmp/docwriter_write_v44.py`<br>`54812b76573b` · 84,551 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×5／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 427 | `.tmp/docwriter_write_v45.py`<br>`af3a22741b2f` · 61,168 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 16／15（+1）<br>类 1×5／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 428 | `.tmp/dscan_01.json`<br>`bab5d4a367af` · 195,396 B | ✘ | **A ✘ ／ B ✘ ／ C ✘** | 25／24（+1）<br>类 1×4／2×5／5×11 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 437 | `.tmp/dscan_classified.json`<br>`458a2e06a2d3` · 47,129 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×5 | 类5·脚本面 `.tmp/dscan_02.py`（自身 L2 起含 2 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 438 | `.tmp/dscan_classified.txt`<br>`2945d458f5a6` · 11,199 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×5 | 类5·脚本面 `.tmp/dscan_02.py`（自身 L2 起含 2 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 439 | `.tmp/dscan_copycmp.txt`<br>`3af905a1f5c4` · 687 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/dscan_write_01.py`（自身 L2 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 440 | `.tmp/dscan_families.txt`<br>`3bc5960fa2bf` · 3,535 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×5 | 类5·脚本面 `.tmp/dscan_04.py`（自身 L2 起含 6 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 441 | `.tmp/dscan_matrix.json`<br>`875f08dd0648` · 273,930 B | ✘ | **A ✘ ／ B ✘ ／ C ✘** | 21／20（+1）<br>类 1×3／2×4／5×8 | 类5·脚本面 `.tmp/dscan_05.py`（自身 L2 起含 3 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 442 | `.tmp/dscan_matrix.txt`<br>`a8d3aa0287b6` · 1,452 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×5 | 类5·脚本面 `.tmp/dscan_05.py`（自身 L2 起含 3 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 443 | `.tmp/dscan_repo_dump.txt`<br>`06d5da0d55ed` · 24,326 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/dscan_write_01.py`（自身 L2 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 444 | `.tmp/dscan_stats.txt`<br>`b35fb0ebd75d` · 2,712 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×5 | 类5·脚本面 `.tmp/dscan_06.py`（自身 L2 起含 2 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 445 | `.tmp/dscan_sub_dump.txt`<br>`8c3f99c0b128` · 94,170 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/dscan_write_01.py`（自身 L2 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 446 | `.tmp/dscan_tables.md`<br>`0a96d4720449` · 56,191 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×5 | 类5·脚本面 `.tmp/dscan_08.py`（自身 L2 起含 2 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 448 | `.tmp/dscan_xcheck.txt`<br>`57dcd8344683` · 3,196 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×5 | 类5·脚本面 `.tmp/dscan_03.py`（自身 L52 起含 2 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 454 | `.tmp/ea_files.json`<br>`48b76f2549f3` · 191,599 B | ✘ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×3／2×5／5×6 | 类5·脚本面 `.tmp/ea_build.py`（自身 L3 起含 9 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 459 | `.tmp/evauditor_one_finish_write.py`<br>`c24967f8114e` · 46,211 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 472 | `.tmp/ge01_full_1494_collect_2026_10_16.py`<br>`039ebfca39b7` · 28,322 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py`（自身 L8 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 473 | `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py`<br>`9e9e402893ef` · 43,129 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 17／16（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 10 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 475 | `.tmp/ge01_full_1494_freeze_write_2026_10_16.py`<br>`b89e0432ab97` · 23,781 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py`（自身 L8 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 476 | `.tmp/ge01_full_1494_llm_calls_2026_10_16.jsonl`<br>`e922d168ab60` · 235,298 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 28／27（+1）<br>类 1×6／2×4／5×10 | 类5·脚本面 `.tmp/_final_verify.py`（自身 L1 起含 8 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 11 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 478 | `.tmp/ge01_full_1494_measurement_resume32_2026_10_16.json`<br>`7ccc5f9e8b2c` · 570,852 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.py`（自身 L16 起含 11 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 479 | `.tmp/ge01_full_1494_precheck_2026_10_16.json`<br>`bd6dd07ad1c3` · 9,432 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/ge01_full_1494_precheck_2026_10_16.py`（自身 L6 起含 13 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 480 | `.tmp/ge01_full_1494_precheck_2026_10_16.py`<br>`cc34ab8552f9` · 10,700 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 481 | `.tmp/ge01_full_1494_probe_2026_10_16.py`<br>`a38499e4d4a9` · 3,199 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×4／2×5／5×4 | 类5·脚本面 `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py`（自身 L8 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_plus83_exec_journal.json`） |
| 483 | `.tmp/ge01_full_1494_resume32_collect_2026_10_16.py`<br>`9496620e32b2` · 14,609 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 484 | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.log`<br>`ada7f41b8cb2` · 1,761 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×6／2×4／5×5 | 类5·脚本面 `.tmp/docwriter_write_v42.py`（自身 L3 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 485 | `.tmp/ge01_full_1494_resume32_precheck_2026_10_16.py`<br>`463532446b61` · 6,122 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×6／2×4／5×4 | 类5·脚本面 `.tmp/docwriter_write_v42.py`（自身 L3 起含 4 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 486 | `.tmp/ge01_full_1494_resume32_probe_2026_10_16.json`<br>`579a7f8b6fe3` · 338 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/ge01_full_1494_resume32_collect_2026_10_16.py`（自身 L23 起含 15 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 487 | `.tmp/ge01_full_1494_resume32_readout_2026_10_16.py`<br>`de50589bd6c6` · 29,430 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 488 | `.tmp/ge01_full_1494_resume32_run_2026_10_16.log`<br>`f655e7d9e3e0` · 1,033 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/ge01_full_1494_resume32_collect_2026_10_16.py`（自身 L23 起含 15 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 489 | `.tmp/ge01_full_1494_resume32_stage_2026_10_16.json`<br>`25d95a22bbb1` · 7,574 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/ge01_full_1494_resume32_collect_2026_10_16.py`（自身 L23 起含 15 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 490 | `.tmp/ge01_full_1494_run_2026_10_16.log`<br>`3e85eac1bf6a` · 14,810 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/ge01_full_1494_exec_r1_write_2026_10_16.py`（自身 L8 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 491 | `.tmp/ge01_gate_index.py`<br>`fc4ed5e7dea0` · 3,095 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·脚本面 `.tmp/ge01_gate_write.py`（自身 L3 起含 5 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 492 | `.tmp/ge01_gate_measure.py`<br>`c2cdebcb0bfc` · 4,068 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×5／5×4 | 类5·脚本面 `.tmp/ge01_gate_list.py`（自身 L2 起含 1 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 493 | `.tmp/ge01_gate_probe.py`<br>`82bf49985799` · 3,196 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·脚本面 `.tmp/ge01_gate_write.py`（自身 L3 起含 5 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 494 | `.tmp/ge01_gate_scan.py`<br>`5f6212d13cb5` · 1,955 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·脚本面 `.tmp/ge01_gate_write.py`（自身 L3 起含 5 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 495 | `.tmp/ge01_gate_write.py`<br>`a661b2c7e5f0` · 82,875 B | ✔ | A ✘ ／ **B ✔** ／ C ✘（＋全文面 ✘） | 13／12（+1）<br>类 1×3／2×4／5×2 | 类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 496 | `.tmp/ge01_measure_list.json`<br>`2eb41639edf4` · 2,435 B | ✘ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×5／5×6 | 类5·脚本面 `.tmp/_cleanup_r2_report.py`（自身 L5 起含 10 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 5 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 497 | `.tmp/ge01_results_sha12.json`<br>`97fb1089de90` · 192,203 B | ✘ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×3／2×4／5×6 | 类5·脚本面 `.tmp/ge01_gate_index.py`（自身 L5 起含 1 处调用形态）；类5·被动 `tools/_archive_purge_2026_10_17/inventory_compare.json` ← `step5_register.py:L40`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 503 | `.tmp/ge01_s3b_v_exec_r1_readings_2026_10_16.json`<br>`1ec7c258c637` · 25,489 B | ✘ | **A ✘ ／ B ✘ ／ C ✘** | 18／17（+1）<br>类 1×3／2×4／5×7 | 类5·脚本面 `.tmp/ge01_s3b_v_exec_r1_2026_10_16.py`（自身 L7 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 505 | `.tmp/ge01_s3b_v_exec_r1_write_2026_10_16.py`<br>`359b768e7dc0` · 56,062 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 506 | `.tmp/ge02_build.py`<br>`a10c57adf6b5` · 24,774 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 507 | `.tmp/ge02_recompute.py`<br>`811d4a138788` · 1,347 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 513 | `.tmp/kd14_absorption_probe.py`<br>`915c968f2d04` · 1,358 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 514 | `.tmp/kd14_carrier_probe.py`<br>`758033c2a76b` · 1,206 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 515 | `.tmp/kd14_m4_corrected.py`<br>`50c1c7d85616` · 932 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 527 | `.tmp/klm41_3_ts_collect_2026_10_16.py`<br>`a28c4ba40940` · 23,196 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 532 | `.tmp/klm41_3_ts_preflight_2026_10_16.py`<br>`c787c6d4e361` · 6,228 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/klm41_3_ts_collect_2026_10_16.py`（自身 L19 起含 16 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 536 | `.tmp/m08_enum_v2_2026_10_16.json`<br>`c45cfc3ddc8d` · 12,255 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×4／2×5／5×4 | 类5·脚本面 `.tmp/m08_r1_write_2026_10_16.py`（自身 L10 起含 9 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_plus83_exec_journal.json`） |
| 537 | `.tmp/m08_r1_amend2_2026_10_16.json`<br>`21ad2e7acd0b` · 1,296 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 19／18（+1）<br>类 1×4／2×5／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 10 件（主 `.tmp/_cleanup_r2_plus83_exec_journal.json`） |
| 538 | `.tmp/m08_r1_amend3_2026_10_16.json`<br>`d77931c6d7a5` · 3,034 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 18／17（+1）<br>类 1×4／2×5／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_plus83_exec_journal.json`） |
| 539 | `.tmp/m08_r1_amend_2026_10_16.json`<br>`3c982068b276` · 1,204 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 20／19（+1）<br>类 1×4／2×5／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 11 件（主 `.tmp/_cleanup_r2_plus83_exec_journal.json`） |
| 547 | `.tmp/m08_r1_llm_calls_partial_pass1_2026_10_16.jsonl`<br>`d30121ed7ebf` · 8,230 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/m08_r1_write_2026_10_16.py`（自身 L10 起含 9 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 568 | `.tmp/m41_llm_calls.jsonl`<br>`a1651f3d9303` · 642 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/m41_dual_readout.py`（自身 L10 起含 5 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 569 | `.tmp/m41_mech_arms.json`<br>`be1a8fce8660` · 1,252 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×5／5×5 | 类5·脚本面 `.tmp/m41_mech_arms.py`（自身 L7 起含 3 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 576 | `.tmp/m41_selfcheck.json`<br>`d18a46a884f2` · 318 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×5／5×5 | 类5·脚本面 `.tmp/m41_selfcheck.py`（自身 L2 起含 1 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 579 | `.tmp/m41_src_shas.txt`<br>`b2c58664cd51` · 420 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×3／2×5／5×5 | 类5·脚本面 `.tmp/m41_src_shas.py`（自身 L2 起含 2 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 581 | `.tmp/me_llm_calls_2026_10_16.jsonl`<br>`fbdedcb0ef48` · 21,339 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 15／14（+1）<br>类 1×5／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 582 | `.tmp/me_t4_resolve_2026_10_16.py`<br>`71b0e9c8da44` · 9,507 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 21／20（+1）<br>类 1×4／2×5／5×6 | 类5·脚本面 `.tmp/_pre_mod/exp_harness_pre.py`（自身 L72 起含 8 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 9 件（主 `.tmp/_cleanup_r2_plus83_exec_journal.json`） |
| 621 | `.tmp/t2b_census_2026_10_16.py`<br>`71f99afb9199` · 3,041 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 622 | `.tmp/t2b_derive_2026_10_16.py`<br>`324165eb0c7d` · 7,964 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 623 | `.tmp/t2b_fetch_facts_2026_10_16.py`<br>`0941558d024e` · 5,774 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 624 | `.tmp/t2b_freeze_2026_10_16.py`<br>`575b796a2e6f` · 13,908 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 625 | `.tmp/t2b_freeze_v2_2026_10_16.py`<br>`02a261b12f7b` · 17,044 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 626 | `.tmp/t2b_harness_pre_change_snapshot_2026_10_16.py`<br>`d5c8d676bb5b` · 36,217 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 19／18（+1）<br>类 1×4／2×5／5×7 | 类5·脚本面 `.tmp/t2b_impl_audit_2026_10_16.py`（自身 L3 起含 13 处调用形态）；类5·被动 `.mavis/scripts/cleanup511/exec_list.json` ← `make_register.py:L11`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 627 | `.tmp/t2b_impl_audit_2026_10_16.py`<br>`e02a343246bd` · 4,856 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 18／17（+1）<br>类 1×5／2×5／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_plus83_exec_journal.json`） |
| 628 | `.tmp/t2b_inspect_facts_2026_10_16.py`<br>`de3c879e39f1` · 1,732 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 629 | `.tmp/t2b_llm_calls_2026_10_16.jsonl`<br>`a54a3af46ba2` · 5,317 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 16／15（+1）<br>类 1×4／2×4／5×5 | 类5·脚本面 `.tmp/t2b_derive_2026_10_16.py`（自身 L3 起含 7 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 630 | `.tmp/t2b_measure_2026_10_16.py`<br>`bd377372927c` · 15,547 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 632 | `.tmp/t2b_patch_harness_2026_10_16.py`<br>`bac4775c5c44` · 7,065 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×4／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 6 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 633 | `.tmp/t3_baseline_procedure_probe.py`<br>`b4c2a5e68dfa` · 2,292 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 634 | `.tmp/t3_baseline_procedure_probe_2026_10_15.json`<br>`7ac600d45dcc` · 1,332 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/t3_baseline_procedure_probe.py`（自身 L4 起含 9 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 638 | `.tmp/t3_nt_measure_2026_10_15.py`<br>`35860b379b7a` · 17,111 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 640 | `.tmp/t3_nt_verify.py`<br>`a1c38dc17d65` · 6,657 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 642 | `.tmp/t3_postchange_equiv.py`<br>`1e579de6033c` · 5,975 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 643 | `.tmp/t3_postchange_equiv_2026_10_15.json`<br>`e8a97dc64a08` · 3,904 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/t3_postchange_equiv.py`（自身 L6 起含 11 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 644 | `.tmp/t3_postchange_manifest_check_2026_10_15.json`<br>`dbfae4d96b46` · 2,135 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 15／14（+1）<br>类 1×3／2×4／5×4 | 类5·脚本面 `.tmp/t3_postcheck.py`（自身 L3 起含 6 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 645 | `.tmp/t3_postcheck.py`<br>`20c96933b00d` · 3,129 B | ✔ | A ✘ ／ **B ✔** ／ C ✘ | 14／13（+1）<br>类 1×3／2×4／5×3 | 类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 7 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |
| 648 | `.tmp/t3_prove_minimal_increment_2026_10_15.py`<br>`1f39cf068862` · 7,303 B | ✔ | **A ✘ ／ B ✘ ／ C ✘** | 17／16（+1）<br>类 1×4／2×4／5×4 | 类5·脚本面 `.tmp/t3_postcheck.py`（自身 L3 起含 6 处调用形态）；类5·被动 `.tmp/cleanup511_manifest_2026_10_17.json` ← `make_register.py:L13`（call:json.load,path_join+load）；未标记 1–4 者 8 件（主 `.tmp/_cleanup_r2_scan4_out.json`） |

**逐件表之读法**：② 栏 `A` ＝ R2-A（无活义务面）· `B` ＝ R2-B（类 5 限脚本／工具面）· `C` ＝ R2-C（＋严格 1–4 标记）；✔ ＝ 该读法下 ② 成立。**三读法之别在「类 5 被动面」与「未标记者是否算史实面」两点**（口径未载 ⇒ KD-1／KD-2）。

---

## §6 与前棒（`74d63d55ee97` ／ 探针产物 `a87f13960926`）之对账

| 面 | 前棒 | 本棒 | 一致性 |
| :-- | :-- | :-- | :-- |
| **① 引用形态 · 成就数** | **155**（`.tmp/dscan_01.json`＋`.tmp/dscan_matrix.json`＋`.tmp/ea_files.json`＋`.tmp/ge01_measure_list.json`＋`.tmp/ge01_results_sha12.json`＋`.tmp/ge01_s3b_v_exec_r1_readings_2026_10_16.json`） | **155**（**同值复用**·⛔ 0 复判） | ✅ **逐位一致** |
| **① 之 6 件不成立** | 6 件 | 同 6 件（复用值） | ✅ 集合相同 |
| **① 之独立交叉校验**（**诊断**·非本棒之判） | —— | 于本棒快照复算 ＝ **6 件**，与前棒**同集、0 增 0 减** | ✅ **偶然相符**（见 KD-3） |
| **② 引用件性质** | 甲读 155 ／ 乙读 **0**（**构造失灵**·假证伪） | **本棒新测**：A **0** ／ B **55** ／ C **0** ／ B＋全文 **7** | ✅ 构造已修正并可复算 |
| **引用件数合计** | **2,436** 件次 | **2,597** 件次 | ⚠ **每件 +1**（161／161 件皆 +1）⇒ 非同一快照 |
| **不同引用件文件数** | 177 | **178** | ✅ +1（已定位·见下） |
| **扫描面** | 3,373 文件 ／ 159,299,464 B | **3,665 文件 ／ 166,360,398 B** | ⚠ 仓内增长（＋292 文件） |
| **③ 拦截 ／ N2** | 161 全数拦截（沿 S-2／S-5 §4-3 字面） | **本棒 0 复算**（沿 `7511b98c6483` §4-3 字面：保护面在册 · **解除归 PI**） | ⛔ 未解除 ⇒ **0 件具备清理许可** |

**「+1 引用件」之身份（已定位）**：`results/_refonly_161_verify_register_2026_10_17.md`（＝ 前棒登记件 `74d63d55ee97` 自身之逐件表）⇒ 前棒探针运行于**其自身登记件落盘之前**，本棒运行于**之后** ⇒ **每件恰 +1 之全部差额**（`delta` 分布：**全部 161 件 ＝ +1**；0 件为 0、0 件为 +2 以上）。

📌 **① 之复用之诚实界**：本棒 ① 栏 ＝ **前棒之值原样搬运**，**⛔ 0 声称「本棒于同集独立复算相符」**；本棒于**扩大集**（每件 +1）上的 ① 复算结果**偶然与前棒同集**（KD-3）。

---

## §7 KD 清单（**本件自列 · 如实 · ⛔ 0 代裁**）

| # | KD | 内容 |
| :-: | :-- | :-- |
| **KD-1** | **类 6 之判读面未载（口径开口 · 本件不择）** | 草案 `:124` 仅载「引用**承载义务**」，**⛔ 未载**其判读面是「引用命中行」还是「引用件文档全文」。实测二读法之差 ＝ **48 件**（`55` → `7`）。⇒ **择读归 PI**；本件**三读法并报**。 |
| **KD-2** | **差额之真正来源与派工面所点者相左（实测）** | 派工面/卡面所点之差额来源 ＝「json 枚举件单纯载名 vs 载义务表述」；**实测**：1,464 个 json／数据类引用件·件次**全部为单纯载名**，**0 件次**于引用行载义务表述 ⇒ **类 6 于本池 0 成立**（引用行面与全文面皆 0 命中于引用行）⇒ **差额之真正来源 ＝ 类 5 之被动面**（json 件被 `json.load` 读取为数据：481 件次）。 |
| **KD-3** | ① 之复用之界（快照不同） | 前棒扫描面 3,373 文件，本棒 **3,665** 文件 ⇒ 引用集每件 **+1**（前棒自身登记件）。本棒 ① 栏 ＝ **复用值**；于扩大集上之 ① 复算**偶然同集**（6/6）—— 属**加强性旁证**，⛔ **0** 充作「同集复算相符」。 |
| **KD-4** | **类 5 之被动面存在封闭世界缺口（`R2-B` 之 55 系**上界**）** | 被动消费之取证为**行内共现**（同一行同时含该引用件名与计数之调用形态／解释器调用）。**经路径变量间接读取**（如 `POOL` 常量 + `json.load(POOL)`，名与调用**不同行**）者**不被计入** ⇒ 系统性**漏检活面** ⇒ **R2-B 之 55 件应视为上界**（真值 ⩽ 55）。本件**⛔ 0 以文件级共现充判据**（其假阳性面过宽，已实测评估：见 §3-2 之 json 分判）。 |
| **KD-5** | **类 5 之「脚本／工具」与「数据」之 kind 划界未载** | 草案 `:123` 之「读取为数据」**未限**于脚本件；本棒 R2-B 将其收窄至 `kind ＝ script`，R2-A 则含 `data`／`doc`。⇒ **R2-A ⩾ R2-B 之 55 件差额全在此一点**（`data` 1,464 ＋ `doc` 935 件次被动面）。 |
| **KD-6** | **「未标记 1–4 且非活面」者之归属未载** | 1,122 件次之引用件**未命中**类 1–4 之任何机械标记（主体为 `_cleanup_r2_scan4_out.json` 等**探针产物 json／txt**）⇒ 草案 `:126`「类 1–4 ＝ 史实记录面」**未覆盖**之。R2-C 将其视为**非史实面**（② 假），R2-A／B 将其视为**无活义务面**（② 真）⇒ **此点独力使 R2-C ＝ 0**。 |
| **KD-7** | **E-3（`V-list` 外之调用形态）本棒 0 取证** | 沿判断件 `:178` 登记之 E-3「人工阅件补扫」**不在本棒授权面**（本棒 ＝ 要件② 之重测）⇒ **① 之封闭世界缺口（KD-C5）未解**；本件对 ① **不置一词**。 |
| **KD-8** | 同名 stem 之归因残余 | 9 组／18 件共享 stem（`_cleanup_r2_postcheck` 等）⇒ 裸 stem 提及**不可分辨**所指 ⇒ 沿前棒之登记（**① 之归因残余**）；对②之影响：引用件**名**（含扩展名）层面之归属不受影响。 |
| **KD-9** | **本棒之自指界限** | 本件于三跑之扫描**之后**落盘 ⇒ 本件**未进入**其任何扫描面；📌 且**本件自身将成为后续扫描之引用件**（前棒登记件即由此 +1）⇒ **0 声称本件之存在充任何结论之先验**。 |
| **KD-10** | **读法之争与处置面正交** | 沿 `7511b98c6483` §4-3：白名单保护面**在册未解除**（解除归 PI）⇒ 🔴 **无论择何读，皆 0 件具备清理许可**；择读仅及「判定」之**名义落档**。 |
| **KD-11** | 首二跑之构造缺陷（如实登记） | 跑 1 因 `KeyError` 失败；跑 2 引用集**误含白名单备份副本**（致引用件 3084 vs 2597）⇒ **跑 3 之前二跑之任何数字皆不采用**。判读规则三跑恒定。 |
| **KD-12** | **测量面 N3 ＝ 0 ≠ 口径面无开口** | 本件之 N3 ＝ 0 意为「**无证据不足之件**」；两处**口径开口**（KD-1／KD-2 之 kind 划界、KD-6 之未标记归属）**不计入 N3** ⇒ 🔴 **0 以 N3 ＝ 0 充「② 之择读已定」**。 |
| **KD-13** | 判读权威之单一性 | 六类之唯一在册出处 ＝ 草案 `536a3064ad38` §2-2；并存版 `f5bad2e2ff00` **0 载六类**（沿判断件 R-甲5 之实测）⇒ 本件**0 与之混用**。 |

---

## §8 边界与不软化声明

1. **本件 0 择读**：三读法之取舍（类 5 之 kind 划界 · 类 6 之判读面 · 未标记者之归属）**三处皆口径未载** ⇒ **归 PI 裁**；本件**仅实测与并报**。
| # | 承诺 | 状态 |
| :-: | :-- | :-: |
| 1 | ⛔ **0 择读**（R2-A／B／C 之取舍归 PI） | ✅ |
| 2 | ⛔ **0** 宣告任一件之终判（`pass`／`af`／`kd`／`fail`／`give-up` 之任一） | ✅ 本件**非终判** |
| 3 | ⛔ **0** 以任何估计值充实测（`R2-B ＋ 全文 ＝ %d` 系**实测之敏感数**，⛔ 0 充预测） | ✅ |
| 4 | ⛔ **0** 复用 `vlist_hits` 充②之谓词（② 之 needle 集 ＝ **引用件名**，独立于①之**目标件名**） | ✅ `n_needles_B` ＝ 178 |
| 5 | ⛔ **0** 仅凭扩展名或文件名断定类 5／类 6 | ✅ 类 5 须内容面（`script+content_call` ＝ 自身调用行）／被动面（`at:line` 锚）；类 6 须引用行全量（`n_hit_lines_scanned` 未截断） |
| 6 | ⛔ **0** 触归档区 · ⛔ **0** 网络 · ⛔ **0** 读 key · ⛔ **0** LLM 调用 · ⛔ **0** 动 `tools/` | ✅ |
| 7 | ⛔ **0** 删除 · ⛔ **0** 移动 · ⛔ **0** 改名 · ⛔ **0** 回改任何既有件一字（**核验非清理**） | ✅ 既有件触动数 ＝ **0** |
| 8 | ⛔ **0** 宣告①毕 · ⛔ **0** 代 PI 解除保护面 | ✅ |
| 9 | 交付之唯一判据 ＝ **盘上实测** | ✅ 见 §9 |

---

## §9 落盘纪律与自核（**唯一判据 ＝ 盘上实测**）

| 项 | 值／状态 |
| :-- | :-- |
| **落盘前占位实测** | `Test-Path` ＝ `False`（1/1）＋ `results/` 内 `_refonly_161_verify_register_r2_2026_10_17*` 之 `glob` ＝ **0** 命中 ⇒ **无撞号** |
| **写入通道** | `io.open(path, 'w', encoding='utf-8', newline='\n')` 直写（UTF-8 无 BOM · 纯 LF） |
| **最终 `SHA-12`／`bytes`** | 🔴 **⛔ 0 自载**（自指悖论 · 沿前棒体例）⇒ **见棒回执**（本棒直算 · 落盘后回读） |
| **`CR`／`CRLF`／`BOM`／`U+FFFD`** | 见棒回执（本棒直算 · 逐字节扫描） |
| **探针版本指纹** | `REQ2-R2.0.0` · 探针 `c3171dc8cdf9`（26,360 B）· 产物 `c47c6f4afddd`（2,029,558 B）· Python 3.14.7 · 耗时 206.1 s |
| **扫描完整性** | `os.walk` 遍历错误 **0** · 读取错误 **0** · 文件 **3,665**／解码 **3,665**（逐位相符）· 字节 **166,360,398** · 行 **2,595,047** |
| **候选池自解析复核** | 白名单登记表独立复解析 **699** 行 ／ `B`-only **161** 件 ＝ 池 **161** 件（**差集双向皆 0** · 顺序逐位相同）· 在盘存在 **161**／161 · SHA-12 相符 **161**／161 |
| **源件终检复测** | §1 之 8 件于落盘后逐一复测指纹，**mtime 未变**（**0 既有件被触动**） |

---

## §10 声明

1. **本件为核验登记件**：**⛔ 0 代 PI 裁** · **⛔ 0** 宣告任一件之终判 · **⛔ 0** 宣告①毕 · **⛔ 0** 回改任何既有件一字 · **⛔ 0** 主张任何清理动作已发生或可即刻发生；
2. **可复算性**：本件全部数字之单一数据源 ＝ `.tmp/refonly161_r2_out.json`（`REQ2-R2.0.0`）；探针源码 ＋ 谓词定义 ＋ 逐件留痕（`ev` 内含每类之 `mark`／命中行／锚点）**齐备于产物内** ⇒ 任一件可逐条回读复算；
3. **阈值纪律**：⛔ **0 新拟任何数值阈值**；四读法之数为**构造面**之实测，非阈值裁定；
4. **与前棒之关系**：⛔ **0** 主张前棒之结论错误 —— 前棒自陈其乙读之 0 系「**假证伪**（构造面失灵）」，**本棒实测证实该自陈**（其失灵三处逐条对位·§2），本棒之 0／55／0 三数系**修正后之构造**之新测值；
5. **本件之数不可直接充「可转判定」**：**须先经 PI 择读**（三处口径开口·KD-1／KD-5／KD-6）⇒ 🔴 **0 件具备清理许可**（KD-10 · 保护面未解除）。

**—— req2-remeasure（要件②重测官）· 核验登记件 · 2026-10-17**
