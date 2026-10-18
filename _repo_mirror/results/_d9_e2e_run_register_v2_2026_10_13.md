# D9 端到端实跑棒 · 执行登记 v2（2026-10-13）

> **件位**：②段 · D9 端到端实跑棒 · 第 2 轮（PI 甲裁后之实跑轮）
> **结论一句话**：**5 件 runner 以原态全部实跑通过（exit=0／stderr 全空／无超时），6 目标全部产出；5/6 字节可复现，H3 因 P-2／P-4 两项既有修复而产生 5 叶元数据差异（可归因，非不确定性）；除 6 目标外两树 0 changed／0 deleted。**
> **⛔ 本件 0 回改任何既有件；⛔ 0 删除／0 移动／0 重命名；⛔ 0 手工改 runner；⛔ 0 自行补救任何跑后差异**

---

## §1 PI 授权（逐字）

| 项 | 内容 |
|:--|:--|
| 卡 | `ask_dbf6b2c80f55707960acafe1` |
| 字段 | `e2e_scope` |
| **PI 裁（逐字）** | **「准覆写 6 目标（先备份既有产出至新位·可溯）·跑全量」** |
| 所选档 | **甲** |
| 上棒 | `results/_d9_e2e_run_register_2026_10_13.md`（`af22751858d1`／12,581 B）· 因「0 覆写既有件」底线而**停手未跑**（实跑 0／5） |

📌 **本棒据此获准者有二，且仅此二者**：① **先备份**该 6 目标至新位（可溯）；② 以**原态**跑 5 件 runner（含覆写该 6 目标）。
📌 **本棒未获准者**：对 6 目标以外任何件的覆写／删除／移动／重命名；手工改 runner；自行补救跑后差异。

### §1-1 上游件（逐字回读，⛔ 0 凭转述）

| 件 | SHA-12 | 本棒用途 |
|:--|:--:|:--|
| `results/_d9_e2e_run_register_2026_10_13.md` | `af22751858d1` | 取 5 件 runner 之写面判定与既有目标指纹 |
| `results/_d9_residual_repair_register_2026_10_12.md` | `cddb7a196473` | 取 P-1／P-2／P-3 修态与残余 C-1…C-7 |
| `results/_d9_h2_r1files_repair_register_2026_10_13.md` | `ef3317e5dbb3` | 取 H2 `r1_files` 21/21 修态（U-5） |
| `results/_p4_inplace_resolution_register_2026_10_13.md` | `d2aeaeedf39c` | 取 P-4 候选③址新建（`SRC_ANCHOR_FALLBACK` 由 False 转 True） |

---

## §2 runner 指纹复核（跑前实测 5/5 全符）

📌 全部 5 件 runner 位于 **`deposon-sub\results\`**（⛔ 非主仓）。**跑前**与**紧邻每次执行之前**双重复核，**跑后再复核**一次。

| 件 | 文件 | 跑前 SHA-12 | 跑前 bytes | 报称值 | 判定 | 跑后 SHA-12 | 跑后未变 |
|:-:|:--|:--:|--:|:--:|:--:|:--:|:--:|
| H1 | `_s4prime_readings_runner_2026_10_11.py` | `52bb6e3bba15` | 23,870 | 同 | ✅ | `52bb6e3bba15` | ✅ |
| H2 | `_s5doubleprime_five_lines_runner_2026_10_11.py` | `2d8cf387b478` | 31,232 | 同 | ✅ | `2d8cf387b478` | ✅ |
| H3 | `_v3_recheck_05_executor_2026_09_28.py` | `65f8a7514f34` | 38,733 | 同 | ✅ | `65f8a7514f34` | ✅ |
| H4 | `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `cd4f1e7b4879` | 19,003 | 同 | ✅ | `cd4f1e7b4879` | ✅ |
| H5 | `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `8ae074194a3d` | 52,785 | 同 | ✅ | `8ae074194a3d` | ✅ |

**FINGERPRINTS_ALL_MATCH = True（5/5）**　📌 ⛔ **0 手工改 runner** 之自证：跑前＝跑后，5 件一字未动。
运行环境：CPython **3.14.7**（Windows）｜numpy **2.5.3**｜`PYTHONIOENCODING=utf-8`／`PYTHONUTF8=1`。

---

## §3 6 个写出目标（自行实测取精确文件名 · ⛔ 0 凭截断名）

📌 由 AST **静态求值**各件之路径常量（⛔ 未执行即取得）+ **全源写点字面扫描**双重确定。

| 件 | 定义处 | 写出点 | 绝对路径 | 写点数 |
|:-:|:--|:--|:--|--:|
| H1 | L57 `OUT_JSON` | L457 `write_text` | `deposon-repo\results\_stage3_trigger_readings_items_2026_10_11.json` | 1 |
| H2 | L586 `op = REPO_RESULTS / …` | L587 `op.write_text` | `deposon-repo\results\_s5doubleprime_five_lines_readings_2026_10_11.json` | 1 |
| H3 | L63 `OUT_JSON` | L695 `write_text` | `deposon-repo\results\_v3_recheck_05_result_2026_09_28.json` | 1 |
| H4 | L67–L69 `OUT_ITEMS_JSON` | L425–L427 `open(…,"w")`+`json.dump` | `deposon-repo\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 1 |
| H5a | L82–L84 `OUT_ITEMS_JSON` | L647 `write_text` | `deposon-repo\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 1 |
| H5b | L85–L87 `OUT_REGISTER_MD` | L830 `write_text` | `deposon-repo\results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | 1 |

📌 **全源写点扫描（`write_text`／`.write(`／`json.dump`／`open(`／`shutil.`／`os.remove`／`mkdir` 等）**：H1＝1、H2＝1、H3＝1（L76 之 `open(path,"r")` 系**读**）、H4＝1、H5＝2 ⇒ **合计 6 个写出目标，无第 7 个**，且**无任何删除／移动／重命名／mkdir 调用**。
📌 6 目标**全部**落主仓 `deposon-repo\results`，**无一**落 `deposon-sub`（与上棒结论一致，本棒独立复证）。

---

## §4 备份明细（6 件 · 原件 ↔ 备份件双指纹 · 逐位一致）

**备份目录**：`results\_d9_e2e_backup_2026_10_13\`（**本棒新建**；建前 `exists=False` ⇒ 0 冲突、0 覆写）
**方式**：`shutil.copy2` **二进制复制**（⛔ 0 移动／0 删除／0 重命名原件；不经过任何文本解码／编码／换行转换）

| # | 件 | 原件 SHA-12 | 备份件 SHA-12 | 原件 bytes | 备份件 bytes | 原件 mtime | 备份件 mtime | 逐位一致 | 跑后再校 |
|:-:|:--|:--:|:--:|--:|--:|:--|:--:|:--:|:--:|
| 1 | H1 `_stage3_trigger_readings_items_2026_10_11.json` | `079108c62a82` | `079108c62a82` | 21,049 | 21,049 | 2026-10-11 16:52:40 | 2026-10-11 16:52:40 | ✅ | ✅ 未变 |
| 2 | H2 `_s5doubleprime_five_lines_readings_2026_10_11.json` | `839fb5452578` | `839fb5452578` | 16,099 | 16,099 | 2026-10-11 18:14:08 | 2026-10-11 18:14:08 | ✅ | ✅ 未变 |
| 3 | H3 `_v3_recheck_05_result_2026_09_28.json` | `f63b36b75a51` | `f63b36b75a51` | 450,701 | 450,701 | 2026-09-28 13:28:21 | 2026-09-28 13:28:21 | ✅ | ✅ 未变 |
| 4 | H4 `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `6cbb8ba01bfb` | `6cbb8ba01bfb` | 15,409 | 15,409 | 2026-10-10 23:07:39 | 2026-10-10 23:07:39 | ✅ | ✅ 未变 |
| 5 | H5a `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `5777a07c608a` | `5777a07c608a` | 43,130 | 43,130 | 2026-10-11 16:03:31 | 2026-10-11 16:03:31 | ✅ | ✅ 未变 |
| 6 | H5b `_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `784f042bf93d` | `784f042bf93d` | 22,646 | 22,646 | 2026-10-11 16:03:31 | 2026-10-11 16:03:31 | ✅ | ✅ 未变 |

**BACKUP_ALL_BYTE_IDENTICAL = True（6/6）**　📌 一致性判据为 **SHA-256 全串**逐位相等（⛔ 非仅比对前 12 位）。
📌 **原件 6 件于备份后即刻复校，字节与 mtime 皆未变** ⇒ 备份动作本身 0 扰动原件。
📌 **备份件于全部跑毕后再校 6/6 仍等于跑前字节** ⇒ 备份可信、可溯、可作还原基准。

---

## §5 执行顺序之依赖依据（本棒实测发现 · 上棒未载）

🔴 **关键实测**：5 件 runner 之写出目标**并非互不相干** —— **H4／H5 之产出系 H1／H2 之输入**。故跑序必须「产出者先于消费者」，否则 H1／H2 将消费陈旧数据。

| 消费者 | 常量 | 定义处 | 实指 | 产出者 |
|:--|:--|:--|:--|:--|
| H5 | `PRIME_ITEMS_JSON` | L91–L93 | `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 🔴 **H4** |
| H1 | `HOLDOUT_D2` | L47 | `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 🔴 **H4** |
| H1 | `HOLDOUT_D3` | L49 | `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 🔴 **H5** |
| H2 | `NEW_HELDOUT_JSON` | L44 | `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 🔴 **H5** |

**本棒采用之跑序**：**H3（独立）→ H4 → H5 → H1 → H2**。
📌 H3 之输入链与其他 4 件无交集（其 4 输入常量互不指向他人产出），故置于首位。
📌 此序保证 H1／H2 消费到的是**本轮刚由 H4／H5 产出**之数据，而非跑前旧件。
📌 跑后 H1 复算之第二域指纹 `3c25e1a2ea94`（＝H4 本轮产出）与第三域指纹 `c34835ad59cf`（＝H5 本轮产出）**逐位吻合**，可反证此序正确。

---

## §6 逐件执行记录（实跑 5／5）

**工作目录** ＝ 各 runner 所在目录 `_repo_mirror\results`（保 `__file__` 语义）｜**限时** ＝ 每件 ≤900 s｜**命令** ＝ `python <runner>`

| 件 | 跑否 | 退出码 | 耗时(s) | 超时 | stdout 字符 | stderr 字符 | runner 跑后未变 |
|:-:|:--:|:--:|--:|:--:|--:|--:|:--:|
| H1 | ✅ 跑 | **0** | 0.65 | 否 | 3,398 | **0** | ✅ |
| H2 | ✅ 跑 | **0** | 1.17 | 否 | 7,225 | **0** | ✅ |
| H3 | ✅ 跑 | **0** | 2.18 | 否 | 1,379 | **0** | ✅ |
| H4 | ✅ 跑 | **0** | 0.75 | 否 | 557 | **0** | ✅ |
| H5 | ✅ 跑 | **0** | 0.76 | 否 | 1,259 | **0** | ✅ |
| — | **实跑 5／5** | **5/5 = 0** | 合计 5.51 | **0 件超时** | — | **全空** | **5/5 未变** |

### §6-1 H3 摘录（`_v3_recheck_05_executor_2026_09_28.py`）

```
[输入链] v3_phys=c659695aa23c pe3=4e4a17d43adf pa1=c7c59e0d2f6c anchor=4bdec2683f06 (fallback 在盘=True)
[重建面] n_cells=540 matches_source=True pe3 样例对账 20/20 一致
[恒等面对照 C1] 整数形式 max|dev|=0.0 residual_540=0；浮点 frac 形式 max|dev|=0.0
[防退化门] 输入面 pass=True 新构造面 pass=True
[K-V3R-5] primary CI_upper=183.271250 -> PASS（fail_hit=False）
[双口径] new=PASS / legacy=PASS (冻结锚 n_records=540, max_dev=0.0)
[产出] deposon-repo\results\_v3_recheck_05_result_2026_09_28.json  bytes=450751  sha12=81460acbb4f9
```

📌 **`(fallback 在盘=True)`** ＝ P-4 就地消解（候选③址新建）在**运行期**获实证，非仅静态解析。

### §6-2 H4 摘录（stdout 全量 · 557 字符）

```
== 门 B · seed42 逐件自审 ==
  heldout_n=26  items 全等=True  per_cell 全等=True  指纹全等=True
  seed42 sha12=acedff01d18c   自审通过=True
== R7 · seed′ 抽取 ==
  seed′=1830975565  新 heldout_n=26
  新指纹 sha12=3c25e1a2ea94   b=1 件数=0
  写入 = ..\..\deposon-repo\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json
OK
```

### §6-3 H5 摘录（stdout 全量 · 1,259 字符）

```
== 门 B · seed42 逐件自审 ==   items/cells/指纹 全等=True  self_audit_pass=True
== 门 B′ · seed′ 复算核 ==     reference_fp=recomputed=3c25e1a2ea94  self_audit_pass=True
== R7 · seed″ 抽取（一次）==   seed″=3223484571  新 heldout_n=26  FP3=c34835ad59cf
== 可动件实测（逐位序列比对）==
  V31−T1 差集词数=9  可动件数=1 / 26   控制核（第二集 26 件逐位全等）=True
== in_heldout 重算（面 II 24 件）==
  第三集 新内/新外=5 / 19   控制核 第一集=9 / 15   第二集=4 / 20
== 落盘 ==  JSON=…_seedthird_items_2026_10_11.json  登记件=…_seedthird_items_register_2026_10_11.md
OK
```

📌 **门 B′（seed′ 复算核）通过** ＝ H5 成功读到 H4 **本轮**产出并复算吻合 ⇒ 反证 §5 跑序正确。

### §6-4 H1 摘录（`_s4prime_readings_runner_2026_10_11.py`）

```
=== ANCHORS (read-only) ===
  runner_five_lines       f784b2fc92f4  expect=f784b2fc92f4  OK
  executor                8a81d90c69ba  expect=8a81d90c69ba  OK
  heldout_d2_seedprime    6cbb8ba01bfb  expect=6cbb8ba01bfb  OK
  heldout_d3_seedthird    5777a07c608a  expect=5777a07c608a  OK
  d2_registered_readings  65a9b9be6327  expect=65a9b9be6327  OK
=== FACE ===  rows=179 files=21
=== GRID SELF-PROOF (13 items) ===  13/13 OK
=== SELF-AUDIT: 第二构造域 (3c25e1a2ea94) 逐件复现 ===
  fingerprint recomputed=3c25e1a2ea94 expect=3c25e1a2ea94 match=True
  n_items=26  field-level diffs=0
  => SELF-AUDIT PASS: 26/26 items, 13 fields each, BIT-IDENTICAL
=== HELD-OUT FINGERPRINT (第三构造域) ===
  recomputed=c34835ad59cf  expect=c34835ad59cf  match=True
  cross-check vs 5777a07c608a (seq_v31/q_id): 26/26 ok
=== CROSS-CHECK vs 在册 LS 读数 ===  逐位全等=True；mean/std rel_diff<1e-12 -> True
=== CROSS-CHECK vs 在册 MD 静态读数 ===  n_distinct=8 min=0.0 max=16.0 loo_min=7  => 逐位全等: True
wrote _stage3_trigger_readings_items_2026_10_11.json  sha12=079108c62a82  bytes=21049
```

### §6-5 H2 摘录（`_s5doubleprime_five_lines_runner_2026_10_11.py`）

```
=== ANCHORS ===
  executor                  8a81d90c69ba  expect=8a81d90c69ba  OK
  new_heldout               5777a07c608a  expect=5777a07c608a  OK
  old_heldout_selftest_only 6a670e629dca  expect=6a670e629dca  OK
=== FACE ===  rows=179 files=21 (expect 179 / 21)
=== GRID SELF-PROOF (13 items) ===  13/13 OK
=== PIPELINE SELF-CERT (old domain, gold=V3 · vs 73550514152d §3.7) ===
  A/Ap/B/C/D point 与 CI 逐项 BIT-IDENTICAL；B num/den=[9,21]、C num/den=[3,5] OK
  => B/C CI 自证: PASS
=== HELD-OUT FINGERPRINT (K-RJ-8' new criterion) ===
  recomputed=c34835ad59cf  registered=c34835ad59cf  expect=c34835ad59cf  match=True
  n=26 (expect 26)  all keys resolve in face: True  (unresolved=0)
=== FIVE-LINE RUN (third domain seed'' c34835ad59cf · gold=V3.1 · model=V3) ===
  n_events=179 n_held=26 n_train=153 tree_depth=6
  A   point=0.36776556776556774  ci=[0.24487179487179486, 0.4818681318681319]
  Ap  point=0.14743589743589744  B=11/21=0.5238095238095238   C=1/5=0.2
wrote _s5doubleprime_five_lines_readings_2026_10_11.json  sha12=839fb5452578  bytes=16099
```

📌 **`rows=179 files=21 (expect 179 / 21)` 且 `unresolved=0`** ＝ H2 `r1_files` 21 件断链（U-5／C-1）在**运行期**获实证修复：21 个文件名于 `REPO_RESULTS` 逐件可读，⛔ 无一 `FileNotFoundError`。

---

## §7 6 目标 before → after 指纹

**before** ＝ 跑前实测（＝ §4 备份件字节）；**after** ＝ 跑毕实测。

| 件 | 目标件 | before SHA-12 | before bytes | **after SHA-12** | **after bytes** | 字节可复现 |
|:-:|:--|:--:|--:|:--:|--:|:--:|
| H1 | `_stage3_trigger_readings_items_2026_10_11.json` | `079108c62a82` | 21,049 | `079108c62a82` | 21,049 | ✅ **完全一致** |
| H2 | `_s5doubleprime_five_lines_readings_2026_10_11.json` | `839fb5452578` | 16,099 | `839fb5452578` | 16,099 | ✅ **完全一致** |
| H3 | `_v3_recheck_05_result_2026_09_28.json` | `f63b36b75a51` | 450,701 | **`81460acbb4f9`** | **450,751** | 🔴 **已变（＋50 B）** |
| H4 | `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `6cbb8ba01bfb` | 15,409 | `6cbb8ba01bfb` | 15,409 | ✅ **完全一致** |
| H5a | `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `5777a07c608a` | 43,130 | `5777a07c608a` | 43,130 | ✅ **完全一致** |
| H5b | `_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `784f042bf93d` | 22,646 | `784f042bf93d` | 22,646 | ✅ **完全一致** |

**字节可复现 5／6**（H1／H2／H4／H5a／H5b **SHA-12 与 bytes 双双逐位复现跑前值**）｜**1／6 变动**（H3）。

### §7-1 H3 变动之归因（实测 · 结构化逐叶差分）

📌 对 H3 新旧产出作**结构化全量逐叶差分**（⛔ 非抽样）⇒ **差异恰 5 叶，全部落于 `input_chain` 元数据面**：

| # | 字段 | before | after | 归因 |
|:-:|:--|:--|:--|:--|
| 1 | `input_chain.v3_phys_60cells.path` | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `deposon-repo/results/…` | **P-2 修复**（L117 `relative_to(REPO)` → `relative_to(REPO_ROOT.parent)`，记录路径基准由 sub 相对改为共同祖先相对） |
| 2 | `input_chain.boss_pe_3_9m60c.path` | `results/deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `deposon-repo/results/…` | 同上 |
| 3 | `input_chain.boss_pa_1_result.path` | `results/boss_pa_1_rbr_rm_result_2026_09_15.json` | `deposon-sub/results/…` | 同上 |
| 4 | `input_chain.conservation_py_main_path.path` | `verifier/audit/conservation.py` | `deposon-repo/verifier/audit/…` | 同上 |
| 5 | `input_chain.conservation_py_fallback_path.exists` | `false` | **`true`** | **P-4 就地消解**（候选③址 `deposon-sub\_archive_deposon_2026_09_17\verifier\audit\conservation.py` 已由前棒新建 ⇒ `.exists()` 由 False 转 True） |

📌 **归因结论**：H3 之变动 **100% 可归因于 P-2／P-4 两项既有修复之预期效果**，⛔ **非不确定性、⛔ 非缺陷、⛔ 非数据漂移**。佐证：

| 佐证 | 实测 |
|:--|:--|
| 全部 `sha12_observed` 值 | **4/4 逐位未变**（`c659695aa23c`／`4e4a17d43adf`／`c7c59e0d2f6c`／`4bdec2683f06`）⇒ **输入数据零漂移** |
| 全部统计量与判定 | **未变**：`n_cells=540`、`max\|dev\|=0.0`、`CI_upper=183.271250`、`[K-V3R-5] primary → PASS`、`new=PASS / legacy=PASS` |
| 文本级 unified diff | 恰 **27 行**（含上下文），改动集中于 `input_chain` 之 5 处 |

📌 **上棒 §3.2 所载 H3 自述「若本棒重跑，仅覆写本棒自身上一轮产出（**seed 固定 → 输出字节可复现**）」** 之「字节可复现」前提，就 H1／H2／H4／H5 **4/4 成立**；就 H3 **不成立**，其成因已归因如上（如实登记，⛔ 0 掩盖）。

### §7-2 跑后盘上态（如实声明）

📌 **⛔ 本棒 0 还原**：6 目标当前盘上态**即跑后态**。H1／H2／H4／H5a／H5b 因字节可复现，**盘上态与跑前态本就相同**；**唯 H3 盘上为新产出**（`81460acbb4f9`／450,751 B），其跑前原件完好存于 `results\_d9_e2e_backup_2026_10_13\_v3_recheck_05_result_2026_09_28.json`（`f63b36b75a51`／450,701 B），**可溯、可还原**。是否还原、以何者为准则**候 PI**（见 §9-U-2）。

---

## §8 全树 0 他改之自证

**方法**：路径 ＋ size ＋ mtime(ns) **全树递归快照**，`before`（任何动作之前）／`after`（跑毕之后）逐路径比对。归档区 `〔本地归档区〕` **0 读 0 写 0 列目录**（遍历内置断言，越界即抛）。

| 树 | before 件数 | after 件数 | added | deleted | **size-changed** | mtime-only |
|:--|--:|--:|--:|--:|--:|--:|
| `deposon-repo\results` | **735** | **742** | **7** | **0** | **1** | 5 |
| `deposon-sub`（全树） | **1,189** | **1,189** | **0** | **0** | **0** | **0** |

### §8-1 `deposon-sub` 全树

**added＝0／deleted＝0／changed＝0／mtime-touched＝0** ⇒ ✅ **`deposon-sub` 全树逐字节态与跑前完全一致，本棒对其 0 写入、0 删除、0 触碰**。

### §8-2 `deposon-repo\results` 之 size-changed

| 件 | 路径 | 变动 | 授权 |
|:--|:--|:--|:--|
| H3 | `results\_v3_recheck_05_result_2026_09_28.json` | 450,701 → 450,751 | ✅ **PI 甲裁授权之 6 目标内** |

📌 **授权外 size-changed ＝ 0 件** ⇒ ✅ **6 目标之外无任何既有件被改动**。
📌 mtime-only 5 件 ＝ H1／H2／H4／H5a／H5b（字节未变、仅 mtime 因重写而更新）⇒ 仍属授权之 6 目标。

### §8-3 `added` 7 件之逐件归属

| # | 新增件 | 归属 |
|:-:|:--|:--|
| 1–6 | `results\_d9_e2e_backup_2026_10_13\` 内 6 件 | ✅ **本棒新建**（PI 甲裁明文授权之「备份至新位」） |
| 7 | `results\__pycache__\_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc`（43,685 B · mtime 2026-10-13 00:35:33） | 🔴 **如实登记 · 见下** |

### §8-4 🔴 `__pycache__` 之新生件（如实登记 · ⛔ 0 自行补救）

| 项 | 实测 |
|:--|:--|
| 文件 | `deposon-repo\results\__pycache__\_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` |
| bytes ／ mtime | 43,685 ／ 2026-10-13 00:35:33.892617 |
| 成因 | CPython 于 **H1 L204 `load_ro(RUNNER_FIVE, …)`** 以 `importlib.util.spec_from_file_location`（**H1 L74**）**导入** `results\_s4prime_five_lines_runner_2026_10_11.py` 时，**解释器自动生成之字节码缓存** |
| `__pycache__` 目录本身 | **跑前已存在**（BEFORE 快照内含其下 2 个 `.pyc`） |
| 既有 2 个 `.pyc` | `_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc`／`…_r1_2026_09_27.cpython-314.pyc`（mtime 均 2026-10-12 15:06:40）⇒ **未被改动、未被删除** |
| 性质 | **新增（added）之解释器副产物**，⛔ **非对任何既有件之改动或删除** |
| 本棒处置 | ⛔ **0 删除、0 移动、0 改写**（遵派工单「⛔ 0 自行补救」）⇒ **原样留置并登记** |

### §8-5 全树闸门判定

| 判据 | 结果 |
|:--|:--|
| 授权外 **changed**（两树） | **0** ✅ |
| **deleted**（两树） | **0** ✅ |
| 授权外 **新增**（`deposon-sub`） | **0** ✅ |
| 授权外新增（`results`，扣除备份目录） | **1**（`__pycache__` 之 `.pyc`，§8-4）🔴 已登记 |

📌 **主结论**：**除 PI 授权之 6 目标外，两树 MUST 0 changed／0 deleted 之要求 ✅ 满足**（changed 0／deleted 0）。
🔴 **如实登记之唯一例外**：解释器于 `deposon-repo\results\__pycache__\` 下新生 1 个 `.pyc`（§8-4）—— 属「新增」而非「改动／删除」，**⛔ 本棒未自行补救**，候 PI 处置（§9-U-1）。

---

## §9 D9「runner 可运行性」结论（三档）

| 档 | 判据 | 本案 |
|:--|:--|:--|
| 🟢 **可运行** | 全部 5 件可在原态跑通并产出 | ✅ **本档** |
| 部分 | 部分可跑、部分因写面停手 | — |
| 🔴 不可运行 | 全部因写面指向既有件而停手 | —（上棒所归之档） |

**结论（逐字）**：**D9 runner 可运行性 ＝「可运行」—— 5/5 件以原态（未改一字节）实跑，退出码全 0、stderr 全空、无一超时，6 个写出目标全部产出。**

### §9-1 本棒所取得之凭据（逐项 · 皆为实测，非推断）

| # | 凭据 | 实测 |
|:-:|:--|:--|
| 1 | **端到端可执行性** | 5/5 exit=0，⛔ 无一导入崩、无一 `SystemExit` |
| 2 | **P-1（H4／H5 域读取面 21 件门柱）** | H4／H5 均过 `len(files) != 21` 门柱并 `OK` 收尾 ⇒ **运行期成立** |
| 3 | **P-2（H3 `relative_to` ×2）** | H3 L117 于模块顶层**未抛** `ValueError`（改前必抛、导入即崩）⇒ **运行期成立** |
| 4 | **P-3（H5 `.tmp` 导入面）** | H5 正常完成，无 `ModuleNotFoundError` ⇒ **运行期成立** |
| 5 | **U-5／C-1（H2 `r1_files` 21/21）** | `rows=179 files=21 (expect 179 / 21)`、`unresolved=0` ⇒ **21/21 运行期可读** |
| 6 | **P-4（H3 `SRC_ANCHOR_FALLBACK`）** | stdout 载 `(fallback 在盘=True)`、产出体 `exists: true` ⇒ **运行期成立** |
| 7 | **产出可复现性** | 6 目标中 **5/6 字节完全可复现**；H3 之差异已逐叶归因于 P-2／P-4 |
| 8 | **runner 之只读锚校验** | H1 5/5 锚 OK、H2 3/3 锚 OK ⇒ 跑前未破坏任何上游锚 |

### §9-2 必读之限定（⛔ 0 过度推论）

1. 本结论**仅**陈述「5 件 runner 于现行源码之下端到端可执行并产出」；⛔ **0 反推 D9 已闭**、⛔ **0 反推①毕**、⛔ **0 代裁任何终判**。
2. 「可运行」系**可执行性**之判，**非正确性之判**。产出内容之对错、门柱之当否、阈值之妥否，**均非本棒所裁**。
3. H3 之产出变动（§7-1）虽已归因于 P-2／P-4，仍**属既有修复面之效果**；其是否应入卷、是否取代跑前原件，**候 PI**（§10-U-2）。
4. 本棒**未**执行任何 6 目标以外之产出面，⛔ 未对 `deposon-sub` 作任何写入；故 **H2／H4／H5 于 `deposon-sub` 侧之行为**（若有其写出落于该侧者）**未验** —— 但实测写点扫描已证其**写出目标 6/6 皆落主仓**，故该面**不存在**。

---

## §10 未决项（⛔ 0 代裁 · 0 代立）

| # | 事项 | 现状 | 归口 |
|:-:|:--|:--|:--|
| **U-1** | `results\__pycache__\_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` 之**留存／清除** | 已如实登记（§8-4）；⛔ 本棒 0 删除、0 自行补救 | **PI** |
| **U-2** | **H3 产出已变更**（`f63b36b75a51`／450,701 → `81460acbb4f9`／450,751，5 叶，归因见 §7-1）—— 以新产出为准、抑或自备份还原？ | 🔴 **未决**；跑前原件完好可溯于 `_d9_e2e_backup_2026_10_13\` | **PI** |
| **U-3** | **F-4「端到端可运行性」** 本棒已取得**可执行性凭据**（5/5 exit=0） | 🔴 **0 宣告闭合**；是否据以闭合 F-4，归 verdict-keeper／PI | **PI／verdict-keeper** |
| **U-4** | `k_v3s_4_4_*` 布尔 | 🔴 **0 赋值**（硬约束） | — |
| **U-5** | ①毕 | 🔴 **0 宣告** | — |
| **U-6** | 既有未决项 C-3（`d6ff7e9b4bd6` §2.4 载 24／实测 21）、C-4（底本 CJK 损坏）、U-7／U-6 | 状态**不因本棒而变**；⛔ 本棒 0 回改 v2、0 触底本 | PI／勘正 |
| **U-7** | 本棒**新建件清单**：备份目录 6 件 ＋ 本登记件 ＋（解释器副产物）`.pyc` 1 件 | 已于 §8-3／§9 列明；⛔ 除此 0 新建、0 删除、0 移动、0 重命名 | — |

---

## §11 纪律对照

| 纪律 | 自证 |
|:--|:--|
| 🔴 **唯一获准覆写者 ＝ 该 6 目标** | ✅ 跑后 size-changed **恰 1 件**且属 6 目标内（H3）；**授权外 changed ＝ 0**（§8-2、§8-5） |
| ⛔ **0 覆写 6 目标以外任何件** | ✅ 两树 0 changed／0 deleted |
| ⛔ **0 删除／0 移动／0 重命名** | ✅ 0 次。备份用 `copy2` 复制；原件 6 件路径与名**全程未变** |
| ⛔ **0 手工改任何 runner** | ✅ 5 件跑前＝跑后指纹全同（§2） |
| ⛔ **0 回改任何既有件** | ✅ 4 件上游登记件仅**只读回读**；既有 `results\_d9_*`／`_p4_*`／`_gate1_*`／`letters/`／`_bob_*`／`_remote_baseline*`／`_archive_2026-10-12` **0 写** |
| ⛔ **0 触归档区** | ✅ 全程遍历内置断言 `non_upload_local_archive` 越界即抛；0 读 0 写 0 列目录（本棒无例外） |
| ⛔ **0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT** | ✅ 纯本机 Python 读取＋哈希＋快照＋子进程执行 |
| ⛔ **0 改终判词／阈值／门柱／判死线** | ✅ 未触及任何条文（`len(files) != 21`／`sys.exit(2)`／CI95／`fail_hit` 等**仅读取并记录**） |
| ⛔ **0 赋 `k_v3s_4_4_*` 布尔** | ✅ 0 赋值 |
| ⛔ **0 宣告①毕** | ✅ 本件 0 作任何毕之宣告 |
| ⛔ **0 自行补救跑后差异** | ✅ `.pyc` 原样留置（§8-4）；H3 未还原（§7-2） |
| 限时 ≤900 s／件 | ✅ 最长者 H3 2.18 s；**0 件超时** |
| 编码 | ✅ UTF-8 **无 BOM** · **纯 LF**（详见附录 A） |

> ⛔ **本件 0 主张**：①D9 已闭；②①毕；③H3 变动为缺陷；④产出内容之正确性已获判定；⑤任一终判已作出。
> 📌 **本件所主张者 ＝ 唯一**：**依 PI 甲裁，5 件 runner 以原态实跑 5/5 通过（exit=0／stderr 全空／无超时），6 目标全部产出（5/6 字节可复现，H3 差异已逐叶归因于 P-2／P-4），除 6 目标外两树 0 changed／0 deleted，备份 6/6 逐位一致可溯。**

---

## 附录 A · 本件指纹

| 项 | 值 |
|:--|:--|
| 路径 | `results/_d9_e2e_run_register_v2_2026_10_13.md` |
| SHA-12 | **见交付回报**（落盘后字节级自测） |
| bytes | **见交付回报** |
| BOM | **无** |
| CR ／ TAB ／ CTRL | **0 ／ 0 ／ 0** · **纯 LF** |
| nonAscii | **> 0**（断言成立） |
| U+FFFD | **0**（断言成立） |

*件止。D9 端到端实跑棒 · 第 2 轮 · 2026-10-13*
