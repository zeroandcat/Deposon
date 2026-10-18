# D9 · 端到端重跑验证棒 · `P-2` 执行面凭据（2026-10-13）

> **件位**：①段收官 · D9 · **`P-2` 执行棒**（PI 2026-10-13 明示「派执行棒」）
> **一句话**：**5 件 D9 runner 于现行源码面原态重跑 5/5 通过（exit code 全 0／stderr 全空／0 件超时），6 个写出目标 6/6 字节逐位复现（SHA-256 全串相等），runner 5/5 跑前＝跑后未变，两树 0 deleted／0 size-changed ⇒「D9 端到端可运行性」取得第二份独立执行面凭据。**
> **⛔ 本件 0 回改任何既有件；⛔ 0 移动／0 重命名／0 删除任何件（备份为复制）；⛔ 0 宣告 D9「收束」；⛔ 0 宣告①毕；⛔ 0 代 PI 裁／0 代销记**

---

## §1 方法与基准

### §1-1 本棒之由来（逐字回读，⛔ 0 凭转述）

| 项 | 载 |
|:--|:--|
| `P-2` 之逐字定义 | 「**D9 端到端可运行性：是否派执行棒**」〔`results\_gate1_five_zero_recheck_2026_10_12.md:248`〕 |
| 基线件所载旧态 | 「`P-2` · D9 端到端可运行性『⛔ 0 执行 runner ⇒ 无凭据』」（阻塞要件 `Z-1`／`Z-4`）〔`2f27acf42897` §C-3〕 |
| 本棒之触发 | **PI 2026-10-13 明示「派执行棒」** ⇒ 本棒系**重跑验证**（非首跑），目的为 `项16`（D9「收束」是否宣告）提供**执行面证据** |

### §1-2 基准件（本棒**只读回读** · 实测指纹见 §1-3）

| # | 件 | 本棒之用途 |
|:-:|:--|:--|
| 1 | `results\_d9_e2e_run_register_v2_2026_10_13.md` | **基准预期之首要来源**：exit code、stdout 摘录、6 目标 after 指纹、跑序依据 |
| 2 | `results\_d9_e2e_disposition_and_f4_closure_register_2026_10_13.md` | F-4 之闭与其限定（`⛔ 0 宣告 D9 收束`）、残余 R-1～R-7 |
| 3 | `results\_d9_e2e_run_register_2026_10_13.md` | 上上棒（实跑 0/5，因「0 覆写既有件」停手）之历史对照 |

### §1-3 基准件实测指纹（本棒独立实测 · 只读）

| # | 件 | SHA-12 | bytes | mtime | 判定 |
|:-:|:--|:--:|--:|:--|:--|
| 1 | `_d9_e2e_run_register_v2_2026_10_13.md` | `72a2a0c90985` | 26,904 | 2026-10-13T00:37:49 | ✅ **与在册值逐位吻合** · ⛔ 0 编辑 |
| 2 | `_d9_e2e_disposition_and_f4_closure_register_2026_10_13.md` | `467b7c10b466` | 22,149 | 2026-10-13T09:36:44 | ✅ 实测 · ⛔ 0 编辑 |
| 3 | `_d9_e2e_run_register_2026_10_13.md` | `af22751858d1` | 12,581 | 2026-10-13T00:25:47 | ✅ **与在册值逐位吻合** · ⛔ 0 编辑 |

### §1-4 方法（可复现 · 逐项自陈）

| 项 | 法 |
|:--|:--|
| 指纹 | `sha12 = hashlib.sha256(读入字节).hexdigest()[:12]`；**可复现性判据为 SHA-256 全串逐位相等**（⛔ 非仅比对前 12 位） |
| 备份 | `shutil.copy2` **二进制复制**（⛔ 0 移动／0 删除／0 重命名原件；不经任何文本解码／编码／换行转换） |
| 跑序 | **H3 → H4 → H5 → H1 → H2**（沿 `72a2a0c90985` §5 之依赖依据：H4／H5 之产出系 H1／H2 之输入） |
| 工作目录 | ＝ 各 runner 所在目录 `D:\私人资料\deposon-sub\results`（保 `__file__` 语义） |
| 命令 | `python <runner>`（`sys.executable`）｜**限时 ≤900 s／件** |
| 捕获 | `subprocess.run(capture_output=True)` 取**原始字节**；stdout／stderr 各记 bytes 与 chars 双口径 |
| 树快照 | 路径＋size＋mtime(ns) **全树递归** before／after 比对；遍历对每一路径断言 `non_upload_local_archive` **不入界** |
| 环境 | CPython **3.14.7**（Windows）｜numpy **2.5.3**｜`PYTHONIOENCODING=utf-8`／`PYTHONUTF8=1`　（**与基准轮同版本**） |

### §1-5 落盘前检查（本件）

- `Test-Path`（`results/_d9_e2e_rerun_for_p2_2026_10_13.md`）：**False**
- `Test-Path`（`..._r1.md`）：**False** ⇒ **⛔ 0 占用、无需 `_r1`**
- glob（`**/*d9_e2e_rerun*`）：落盘前 **0 命中**（落盘后仅本件＋备份目录，属本棒新建）

---

## §2 五 runner 现态（跑前实测 · 5/5 全符基准）

📌 全部 5 件 runner 位于 **`deposon-sub\results\`**（⛔ 非主仓）。**跑前**与**跑后**各复核一次指纹。

| 件 | 文件名 | 跑前 SHA-12 | 跑前 bytes | 基准报称 | 判定 | 跑后 SHA-12 | 跑后未变 |
|:-:|:--|:--:|--:|:--:|:--:|:--:|:--:|
| H1 | `_s4prime_readings_runner_2026_10_11.py` | `52bb6e3bba15` | 23,870 | 同 | ✅ | `52bb6e3bba15` | ✅ |
| H2 | `_s5doubleprime_five_lines_runner_2026_10_11.py` | `2d8cf387b478` | 31,232 | 同 | ✅ | `2d8cf387b478` | ✅ |
| H3 | `_v3_recheck_05_executor_2026_09_28.py` | `65f8a7514f34` | 38,733 | 同 | ✅ | `65f8a7514f34` | ✅ |
| H4 | `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `cd4f1e7b4879` | 19,003 | 同 | ✅ | `cd4f1e7b4879` | ✅ |
| H5 | `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `8ae074194a3d` | 52,785 | 同 | ✅ | `8ae074194a3d` | ✅ |

### §2-1 跑前 mtime（本棒实测）

| 件 | mtime（ISO） |
|:-:|:--|
| H1 | 2026-10-12T16:33:48.196683 |
| H2 | 2026-10-13T00:17:00.357599 |
| H3 | 2026-10-12T23:53:11.808173 |
| H4 | 2026-10-12T23:53:11.668768 |
| H5 | 2026-10-12T23:53:15.935072 |

**FINGERPRINTS_ALL_MATCH = True（5/5）**　📌 **⛔ 0 手工改 runner 之自证**：跑前 ＝ 跑后，5 件一字未动。

### §2-2 写面复核（沿基准，沿用其结论并本棒独立复证）

📌 5 件之写出目标共 **6 个**，**全部落主仓 `deposon-repo\results\`**，**无一落 `deposon-sub`**；基准轮之全源写点字面扫描已证**无任何删除／移动／重命名／mkdir 调用**。本棒据此**仅**对这 6 目标作备份与产出核对。

| 件 | 目标件 | 写点数 |
|:-:|:--|--:|
| H1 | `_stage3_trigger_readings_items_2026_10_11.json` | 1 |
| H2 | `_s5doubleprime_five_lines_readings_2026_10_11.json` | 1 |
| H3 | `_v3_recheck_05_result_2026_09_28.json` | 1 |
| H4 | `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | 1 |
| H5a | `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | 1 |
| H5b | `_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | 1 |

---

## §3 备份映射（旧路径 → 备份路径）

**备份目录**：`D:\私人资料\deposon-repo\results\_d9_e2e_rerun_backup_2026_10_13\`（**本棒新建**）
**建前实测**：`exists=False` ⇒ **0 冲突、0 覆写、0 占用**
**方式**：`shutil.copy2` 二进制复制｜**⛔ 0 移动／0 删除／0 重命名原件**

| # | 旧路径（原件，主仓 `results\`） | 新路径（本棒备份） | 原件 SHA-12 | 备份 SHA-12 | 原 bytes | 备份 bytes | 逐位一致 | 原件受扰 |
|:-:|:--|:--|:--:|:--:|--:|--:|:--:|:--:|
| 1 | `_stage3_trigger_readings_items_2026_10_11.json` | `_d9_e2e_rerun_backup_2026_10_13\_stage3_trigger_readings_items_2026_10_11.json` | `079108c62a82` | `079108c62a82` | 21,049 | 21,049 | ✅ | ✅ 未变 |
| 2 | `_s5doubleprime_five_lines_readings_2026_10_11.json` | `_d9_e2e_rerun_backup_2026_10_13\_s5doubleprime_five_lines_readings_2026_10_11.json` | `839fb5452578` | `839fb5452578` | 16,099 | 16,099 | ✅ | ✅ 未变 |
| 3 | `_v3_recheck_05_result_2026_09_28.json` | `_d9_e2e_rerun_backup_2026_10_13\_v3_recheck_05_result_2026_09_28.json` | `81460acbb4f9` | `81460acbb4f9` | 450,751 | 450,751 | ✅ | ✅ 未变 |
| 4 | `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `_d9_e2e_rerun_backup_2026_10_13\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `6cbb8ba01bfb` | `6cbb8ba01bfb` | 15,409 | 15,409 | ✅ | ✅ 未变 |
| 5 | `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `_d9_e2e_rerun_backup_2026_10_13\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `5777a07c608a` | `5777a07c608a` | 43,130 | 43,130 | ✅ | ✅ 未变 |
| 6 | `_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `_d9_e2e_rerun_backup_2026_10_13\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `784f042bf93d` | `784f042bf93d` | 22,646 | 22,646 | ✅ | ✅ 未变 |

**BACKUP_ALL_BYTE_IDENTICAL = True（6/6）**（判据为 SHA-256 全串逐位相等）
**BACKUP_SRC_INTACT = True（6/6）**（复制后即刻复校原件，字节与 mtime 皆未变 ⇒ 备份动作本身 0 扰动原件）
📌 备份目录实测 **6 件**（`Get-ChildItem -File` 计数 ＝ 6）｜**⛔ 0 触碰**既有备份区 `results\_d9_e2e_backup_2026_10_13\`（该区 6 件仅只读核对，**0 写 0 改**）。

### §3-1 备份所据之现态说明（如实登记）

📌 本棒备份之原件，**既非**「原始态」**亦非**自建备份区之原态件，而是**基准轮跑毕后留于盘上之现行态**（H3 已是 `81460acbb4f9`／450,751 B，非 `f63b36b75a51`／450,701 B）。
⇒ 故本备份区之作用为「**重跑前之还原基准**」，⛔ **0 替代** `_d9_e2e_backup_2026_10_13\` 之历史原态备份（后者完好留存，6/6 只读复核 walk_errors=0）。

---

## §4 实跑记录（实跑 5／5）

**工作目录** ＝ `D:\私人资料\deposon-sub\results`｜**限时** ＝ 每件 ≤900 s｜**跑序** ＝ H3 → H4 → H5 → H1 → H2

| 件 | 跑否 | **exit code** | 耗时(s) | 超时 | stdout bytes | stdout chars | stderr bytes | stderr chars | runner 跑后未变 |
|:-:|:--:|:--:|--:|:--:|--:|--:|--:|--:|:--:|
| H1 | ✅ 跑 | **0** | 0.66 | 否 | 3,570 | 3,398 | **0** | **0** | ✅ |
| H2 | ✅ 跑 | **0** | 1.08 | 否 | 7,253 | 7,225 | **0** | **0** | ✅ |
| H3 | ✅ 跑 | **0** | 2.88 | 否 | 1,655 | 1,379 | **0** | **0** | ✅ |
| H4 | ✅ 跑 | **0** | 0.64 | 否 | 623 | 557 | **0** | **0** | ✅ |
| H5 | ✅ 跑 | **0** | 0.79 | 否 | 1,569 | 1,259 | **0** | **0** | ✅ |
| — | **实跑 5／5** | **5/5 = 0** | 合计 **6.05** | **0 件超时** | — | — | **全空** | **全空** | **5/5 未变** |

📌 **stderr 全空**（5/5 件，bytes 与 chars 双口径皆 0）；**stdout 解码 U+FFFD 计数 0/0**（⛔ 无编码损坏）。
📌 **stdout chars 5/5 与基准轮逐位相同**（3,398／7,225／1,379／557／1,259）⇒ 输出**逐字一致**。

### §4-1 H3 摘录（`_v3_recheck_05_executor_2026_09_28.py` · exit=0）

```
[输入链] v3_phys=c659695aa23c pe3=4e4a17d43adf pa1=c7c59e0d2f6c anchor=4bdec2683f06 (fallback 在盘=True)
[重建面] n_cells=540 matches_source=True pe3 样例对账 20/20 一致
[恒等面对照 C1] 整数形式 max|dev|=0.0 residual_540=0；浮点 frac 形式 max|dev|=0.0
[pairwise T_R] O=3352.0 E_pool=3272.53 Δ(带符号)=79.4667 |Δ|=79.4667 |Δ| CI95=[2.9362, 183.2713]
[防退化门] 输入面 pass=True 新构造面 pass=True
[K-V3R-5] primary CI_upper=183.271250 -> PASS（fail_hit=False）
[双口径] new=PASS / legacy=PASS (冻结锚 n_records=540, max_dev=0.0)
[产出] deposon-repo\results\_v3_recheck_05_result_2026_09_28.json  bytes=450751  sha12=81460acbb4f9
```

📌 **`(fallback 在盘=True)`** ＝ `P-4` 就地消解于**运行期**再度获实证｜**H3 模块顶层未抛 `ValueError`** ＝ `P-2` 于运行期成立｜`CI_upper=183.271250`、判定 `PASS` **与基准轮逐位相同**。

### §4-2 H4 摘录（stdout 全量 · 557 字符）

```
== 门 B · seed42 逐件自审 ==
  heldout_n = 26   items 全等 = True   per_cell 全等 = True   指纹全等 = True
  seed42 sha12 = acedff01d18c   自审通过 = True
== R7 · seed′ 抽取 ==
  seed′ = 1830975565   新 heldout_n = 26
  新指纹 sha12 = 3c25e1a2ea94   b=1 件数 = 0
  写入 = ..\..\deposon-repo\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json
OK
```

### §4-3 H5 摘录（stdout 全量 · 1,259 字符）

```
== 门 B · seed42 逐件自审 ==   items/cells/指纹 全等=True  self_audit_pass=True
== 门 B′ · seed′ 复算核 ==     reference_fp=acedff01d18c recomputed=acedff01d18c  self_audit_pass=True
== 门 B′ · seed′ 复算核 ==     reference_fp=3c25e1a2ea94  recomputed=3c25e1a2ea94  self_audit_pass=True
== R7 · seed″ 抽取（一次）==   seed″=3223484571  新 heldout_n=26  FP3=c34835ad59cf
== 可动件实测（逐位序列比对）==   V31−T1 差集词数=9  可动件数=1 / 26   控制核（第二集 26 件逐位全等）=True
== in_heldout 重算（面 II 24 件）==   第三集 新内/新外=5 / 19   控制核 第一集=9 / 15   第二集=4 / 20
== 落盘 ==   JSON=…_seedthird_items_2026_10_11.json   登记件=…_seedthird_items_register_2026_10_11.md
OK
```

📌 门 B′ 之 `recomputed=3c25e1a2ea94` **恰等于 H4 本轮产出之新指纹** ⇒ **H5 消费的是 H4 本轮产出**，跑序正确性得运行期自证。

### §4-4 H1 摘录（`_s4prime_readings_runner_2026_10_11.py` · exit=0）

```
=== ANCHORS (read-only) ===
  runner_five_lines f784b2fc92f4 / executor 8a81d90c69ba / heldout_d2_seedprime 6cbb8ba01bfb
  heldout_d3_seedthird 5777a07c608a / d2_registered_readings 65a9b9be6327    5/5 OK
=== FACE ===  rows=179 files=21
=== GRID SELF-PROOF (13 items) ===  13/13 OK
=== SELF-AUDIT: 第二构造域 (3c25e1a2ea94) 逐件复现 ===
  fingerprint recomputed=3c25e1a2ea94 expect=3c25e1a2ea94 match=True
  n_items=26  field-level diffs=0
  => SELF-AUDIT PASS: 26/26 items, 13 fields each, BIT-IDENTICAL
=== HELD-OUT FINGERPRINT (第三构造域) ===  recomputed=c34835ad59cf expect=c34835ad59cf match=True
=== CROSS-CHECK vs 在册 LS 读数 ===  逐位全等=True；mean/std rel_diff<1e-12 -> True
=== CROSS-CHECK vs 在册 MD 静态读数 ===  n_distinct=8 min=0.0 max=16.0 loo_min=7  => 逐位全等: True
wrote _stage3_trigger_readings_items_2026_10_11.json  sha12=079108c62a82  bytes=21049
```

📌 **锚校验 5/5 OK**（跑前未破坏任何上游锚）｜`rows=179 files=21` ＝ `P-1` 域读取面门柱成立｜`recomputed=3c25e1a2ea94` ＝ H4 本轮产出，`recomputed=c34835ad59cf` ＝ H5 本轮产出 ⇒ **H1 消费本轮新产出，跑序正确**。
📌 **自报指纹 `079108c62a82`／21,049 B 与本棒独立实测逐位吻合**。

### §4-5 H2 摘录（`_s5doubleprime_five_lines_runner_2026_10_11.py` · exit=0）

```
=== ANCHORS ===  executor 8a81d90c69ba / new_heldout 5777a07c608a / old_heldout_selftest_only 6a670e629dca   3/3 OK
=== FACE (steps 1-6) ===  rows=179 files=21 (expect 179 / 21)
=== GRID SELF-POOF (13 items) ===  13/13 OK
=== PIPELINE SELF-CERT (old domain, gold=V3) ===  A/Ap/B/C/D point 与 CI 逐项 BIT-IDENTICAL；B num/den=[9,21]、C num/den=[3,5] OK
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

📌 **`rows=179 files=21 (expect 179 / 21)` 且 `unresolved=0`** ＝ `U-5`／`C-1`（H2 `r1_files` 21/21）于**运行期再度获实证修复**，⛔ 无一 `FileNotFoundError`｜`recomputed=c34835ad59cf` ＝ H5 本轮 `FP3` ⇒ 跑序正确。
📌 **⛔ 0 `ModuleNotFoundError`** ＝ `P-3`（H5 `.tmp` 导入面）运行期成立（由 H5 正常 `OK` 收尾反证）。

---

## §5 对账与结论

### §5-1 6 目标 跑前 → 跑后 → 基准 after 三方对账

| 件 | 目标件 | 跑前 SHA-12 | 跑前 bytes | **跑后 SHA-12** | **跑后 bytes** | 跑后 ＝ 跑前 | 跑后 ＝ 基准 after |
|:-:|:--|:--:|--:|:--:|--:|:--:|:--:|
| H1 | `_stage3_trigger_readings_items_2026_10_11.json` | `079108c62a82` | 21,049 | `079108c62a82` | 21,049 | ✅ | ✅ |
| H2 | `_s5doubleprime_five_lines_readings_2026_10_11.json` | `839fb5452578` | 16,099 | `839fb5452578` | 16,099 | ✅ | ✅ |
| H3 | `_v3_recheck_05_result_2026_09_28.json` | `81460acbb4f9` | 450,751 | `81460acbb4f9` | 450,751 | ✅ | ✅ |
| H4 | `_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `6cbb8ba01bfb` | 15,409 | `6cbb8ba01bfb` | 15,409 | ✅ | ✅ |
| H5a | `_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `5777a07c608a` | 43,130 | `5777a07c608a` | 43,130 | ✅ | ✅ |
| H5b | `_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `784f042bf93d` | 22,646 | `784f042bf93d` | 22,646 | ✅ | ✅ |

**字节可复现 6／6（SHA-256 全串判据）**　**基准 after 吻合 6／6**

### §5-2 🔴 关键差分之归因澄清（`H3` 之 5/6 → 6/6）

| 轮次 | H3 跑前态 | H3 跑后态 | 字节可复现 |
|:--|:--|:--|:--:|
| 基准轮（2026-10-13 00:35） | `f63b36b75a51`／450,701（**修前原态**） | `81460acbb4f9`／450,751 | **5／6** |
| **本轮（2026-10-13 22:10）** | `81460acbb4f9`／450,751（**修后态**） | `81460acbb4f9`／450,751 | **6／6** |

📌 基准轮 §7-1 已将那次 5 叶变动 **100% 归因于 `P-2`／`P-4` 两项既有修复之预期效果**，并断言「⛔ 非不确定性、⛔ 非缺陷、⛔ 非数据漂移」。
📌 **本轮提供该断言之经验佐证**：同一源码面下两轮独立实跑（00:35 与 22:10）**产出 `81460acbb4f9` 逐位相同** ⇒ 该变动系**一次性状态迁移**（修前 → 修后之不动点），⛔ **非不确定性**。**本轮 6/6 复现**。
📌 ⛔ **本棒 0 代裁**基准轮 §10 `U-2`（以新产出为准否／自备份还原否）—— 本条仅为**新增事实**，其裁归 **PI**。

### §5-3 全树 0 他改之自证（before／after 全树递归比对）

| 树 | before 件数 | after 件数 | added | deleted | **size-changed** | mtime-only | walk_errors |
|:--|--:|--:|--:|--:|--:|--:|--:|
| `deposon-repo\results` | **788** | **795** | **7** | **0** | **0** | 6 | **0** |
| `deposon-sub`（全树） | **1,189** | **1,189** | **0** | **0** | **0** | **0** | **0** |

- **`deposon-sub` 全树**：added 0／deleted 0／changed 0／mtime-touched 0 ⇒ ✅ **本棒对其 0 写入、0 删除、0 触碰**（5 件 runner 亦在其中，跑前＝跑后）。
- **`size-changed = 0`** ⇒ ✅ **6 目标皆以相同字节重写**（mtime-only 6 件即 6 目标）。
- **added 7 件之逐件归属**：

| # | 新增件 | 归属 |
|:-:|:--|:--|
| 1–6 | `results\_d9_e2e_rerun_backup_2026_10_13\` 内 6 件 | ✅ **本棒新建**（派工单「须**先**复制至隔离备份目录」之产物） |
| 7 | `results\__pycache__\_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc`（`08d4b51c45c6`／67,081 B／mtime 2026-10-13T22:10:07.939889） | 🔴 **解释器副产物 · 如实登记**（见 §6 `KD-1`） |

### §5-4 `__pycache__` 之既有两态（如实登记）

| 件 | 实测 | 状态 |
|:--|:--|:--|
| `_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` | `f4194cc5a522`／43,685 B／mtime 2026-10-13T00:35:33.892617 | 🟢 **与在册值逐位吻合 · 本棒 0 改动**（PI 甲裁「保留并登记」之保留件，**保留态得维持**） |
| `_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` | `08d4b51c45c6`／67,081 B／mtime 2026-10-13T22:10:07.939889 | 🔴 **本轮新生**（其源文件 `deposon-repo\results\_v4_pi_cot_v3_ruleset_v3_executor.py` 在盘） |

📌 本棒对 `__pycache__` **0 删除、0 移动、0 改写、0 清扫**；⛔ **0 将解释器副产物充作「改动既有件」**（属「新增」）。

### §5-5 「D9 端到端可运行性」结论（三档 · 沿基准体例）

| 档 | 判据 | 本案 |
|:--|:--|:--|
| 🟢 **可运行** | 全部 5 件可在原态跑通**并产出且产出对** | ✅ **本档** |
| 部分 | 部分可跑、部分因写面停手 | — |
| 🔴 不可运行 | 全部因写面指向既有件而停手 | — |

**结论（逐字）**：**D9 端到端可运行性 ＝「可运行」—— 5/5 件 runner 以原态（未改一字节）重跑通过，exit code 全 0、stderr 全空、0 件超时；6 个写出目标全部产出，且 6/6 与基准轮 after 指纹 SHA-256 全串逐位相同。**

### §5-6 ⛔ 必读之限定（0 过度推论）

1. 本结论**仅**陈述「5 件 runner 于现行源码之下端到端**可执行并产出，且产出与基准轮一致**」；⛔ **0 反推 D9 已收束**、⛔ **0 反推 `项16` 可宣告**、⛔ **0 反推①毕**、⛔ **0 代裁任何终判**。
2. 「可运行」系**可执行性 + 产出可复现性**之判，⛔ **非正确性之判**。产出内容之对错、门柱之当否、阈值之妥否，**均非本件所裁**。
3. 本棒为**重跑验证**（第二份执行面凭据），⛔ **0 替代**基准轮之凭据，二者并存。
4. 本棒**未**执行 6 目标以外之任何产出面；⛔ 未对 `deposon-sub` 作任何写入。
5. **「可运行」之成立不连带**任何在册残余项之闭（`R-3`～`R-7` 等，见 §6-3）。

### §5-7 执行面证据之再确认（P-1／P-2／P-3／P-4／U-5 · 逐项）

| # | 修复项 | 本轮运行期实证 | 成立 |
|:-:|:--|:--|:--:|
| 1 | **`P-1`**（H4／H5 域读取面 21 件门柱） | H4／H5 均过域读取并 `OK` 收尾；H1／H2 载 `files=21` | ✅ |
| 2 | **`P-2`**（H3 `relative_to` ×2） | H3 模块顶层**未抛** `ValueError`（改前必抛、导入即崩） | ✅ |
| 3 | **`P-3`**（H5 `.tmp` 导入面） | H5 正常完成，无 `ModuleNotFoundError` | ✅ |
| 4 | **`P-4`**（H3 `SRC_ANCHOR_FALLBACK`） | stdout 载 **`(fallback 在盘=True)`** | ✅ |
| 5 | **`U-5`／`C-1`**（H2 `r1_files` 21/21） | `rows=179 files=21 (expect 179 / 21)`、`unresolved=0` | ✅ |
| 6 | **runner 只读锚校验** | H1 5/5 锚 OK、H2 3/3 锚 OK | ✅ |
| 7 | **产出可复现性** | **6/6** 字节完全可复现（基准轮为 5/6，见 §5-2） | ✅ |

---

## §6 遗留 ／ KD

### §6-1 KD 登记（本棒新发现 · **KD ＝ Known Defect** · **共 2 条**）

| # | KD | 实测事实 | 归因状态 | 处置 |
|:-:|:--|:--|:--|:--|
| **`KD-1`** | **`__pycache__` 组成在轮次间不稳定** | 上轮 §8-4 登记 `_v4_pi_cot_v3_ruleset_v3_executor.cpython-314.pyc` 为「**跑前已存在**」（mtime 2026-10-12 15:06:40）；**本棒跑前全树快照中该件不存在**（⇒ 落入 added 集），**本轮实跑后新生**（`08d4b51c45c6`／67,081 B／mtime 2026-10-13T22:10:07.939889） | 🔴 **归因不明** —— 本棒 before→after 之 `deleted=0`，故其**消失发生于本棒之前**，⛔ **非本棒所为**、⛔ **非本棒可考**（本棒无该时点之快照） | ⛔ 本棒 **0 删除、0 清扫、0 补救**；原样留置并登记。**候 PI／他棒勘正** |
| **`KD-2`** | **新生 `.pyc` 之发出 runner 未精确定位** | 该 `.pyc` 之 basename 唯一对应 `deposon-repo\results\_v4_pi_cot_v3_ruleset_v3_executor.py`（在盘）；**H1 与 H2 之 stdout 皆载 `executor 8a81d90c69ba` 锚**，二者皆经 `load_ro`（`spec_from_file_location`）导入该 executor | 🔴 **未核得** —— 本棒**未逐件隔离**以定位发出者（隔离须重复覆写 6 目标，超本棒「重跑验证」之最小射程）；⛔ **不以推断充事实** | 登记为 KD（**无法给料 ⇒ KD**）；候他棒隔离定位 |

### §6-2 本棒 0 主张（逐条）

① ⛔ **0 宣告** D9「收束」（`项16` 仍开）｜② ⛔ **0 宣告**①毕｜③ ⛔ **0 代裁**基准轮 `U-2`（H3 以新产出为准否）｜④ ⛔ **0 销记**任何在册未闭项｜⑤ ⛔ **0 变更** `Z-1`／`Z-4` 之计数｜⑥ ⛔ **0 回改**任何既有件一字｜⑦ ⛔ **0 移动／0 重命名／0 删除**任何件（备份为**复制**）｜⑧ ⛔ **0 手工改**任何 runner｜⑨ ⛔ **0 赋**任一 `k_v3s_4_4_*` 布尔｜⑩ ⛔ **0 改**终判词／阈值／门柱／判死线｜⑪ ⛔ **0 代 PI 裁／释／择／给值**｜⑫ ⛔ 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT／0 远端写／0 上传｜⑬ ⛔ **0 触** `D:\私人资料\_non_upload_local_archive`（**0 读 0 写 0 列目录**，遍历内置断言越界即抛）。

### §6-3 承继之在册残余（状态**不因本棒而变** · ⛔ 0 连带归零）

| # | 在册残余 | 本棒之后 |
|:-:|:--|:--|
| R-3 | `C-3` · v2 载「24 条」vs 实测 21 | 🔴 状态**不变**（⛔ 本棒 0 回改 v2、0 勘正） |
| R-4 | `C-4` · 底本 `c3167a531e0e` CJK 损坏 | 🔴 状态**不变**（⛔ 本棒 0 触底本） |
| R-5 | `C-5` · H4 L60／H5 L73 之 `RESULTS` 定义行 | 🔴 状态**不变**（无功能后果；⛔ 0 删行） |
| R-6 | `C-6`／`C-7` · H5 `os.path.relpath(OUT_*, REPO)`／`.tmp/prep.py` 注释 | 🔴 状态**不变**（未断链／非执行面） |
| R-7 | **D9 之「收束」未宣告** | 🔴 **仍开** —— 本棒仅提供执行面凭据 |
| U-1 | `_s4prime_five_lines_runner_2026_10_11.cpython-314.pyc` 留存／清除 | 🟢 **保留态得维持**（`f4194cc5a522` 逐位未变）；**`KD-1` 另生新件**，同面增至 2 件 |
| U-2 | H3 以新产出为准否 | 🔴 **仍开**；本棒新增事实见 §5-2 |
| U-4 | `k_v3s_4_4_*` 布尔 | 🔴 0 赋值（硬约束） |
| U-5 | ①毕 | 🔴 0 宣告 |

> 📌 **纪律**：**「可运行」之闭 ⛔ 不连带**上列任一项；**执行面证据 ⛔ 不等于收束宣告面已闭**（销记／宣告权不在本棒）。

### §6-4 阴性结论之扫描完整性自证（先证扫描完整，方出阴性结论）

| 项 | 实测 |
|:--|:--|
| 方法 | Python `os.walk` 全树递归；每一条路径断言 `non_upload_local_archive` **不入界**（越界即 `AssertionError`） |
| `deposon-repo\results` before ／ after | **788** ／ **795** 件 |
| `deposon-sub` before ／ after | **1,189** ／ **1,189** 件 |
| **遍历错误数** | **0**（before 0 ＋ after 0）｜`stat` 失败计数 **0** |
| 备份目录枚举 | **6 件**｜walk_errors **0** |
| `__pycache__` 枚举 | **2 件**｜walk_errors **0** |

⇒ 📌 **「0 deleted／0 size-changed／`deposon-sub` 0 变动」诸阴性结论，其扫描已证完整（遍历错误数 0）。**

### §6-5 临时文件

📌 辅助脚本与结果 JSON **仅落 `%TEMP%`**（`p2_probe_a.py`／`p2_rerun.py`／`p2_probe_b.py`／`p2_result.json`／`p2_stdout.txt`），**⛔ 未入仓**。

---

## 附录 A · 本件指纹（落盘后字节级自测）

| 项 | 值 |
|:--|:--|
| 路径 | `results/_d9_e2e_rerun_for_p2_2026_10_13.md` |
| SHA-12 | **见交付回报**（沿同族体例不自写入本件） |
| bytes | **见交付回报** |
| BOM | **无** |
| CR ／ TAB ／ CTRL | **0 ／ 0 ／ 0** · **纯 LF** |
| nonAscii | **> 0**（断言成立） |
| U+FFFD | **0**（断言成立） |

*件止。D9 · 端到端重跑验证棒（`P-2` 执行棒）· 2026-10-13 —— 署名 `worker`。*
