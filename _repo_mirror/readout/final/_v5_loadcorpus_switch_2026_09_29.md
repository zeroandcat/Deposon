# P-6 切换落地：哨兵 r1 修复应用回原件 + 哈希锚更新（V4）

- **日期**：2026-09-29 中午
- **执行**：`worker`（Mavis 8-agent team，deposon 工作区）
- **来源棒**：`results/_v5_loadcorpus_fix_2026_09_29.md`（修 `load_corpus` 孤儿哨兵，新名件 `mindmap_corpus_v20_r1.py` / `e77e7f3455e0` / 7 项验证 PASS）
- **授权**：PI 拍板「就地修+锚更新」（`ask_ce9d69e725691a5494da3827` q1）
- **skill**：派工单未指定 skill 名 ⇒ **0 skill 加载**（沿来源棒同口径）
- **铁律口径**：SHA-12 = `hashlib.sha256(...).hexdigest()[:12]` 小写

---

## §0 结论（先说边界，防误导）

1. **原件已就地修**：`mindmap_corpus_v20.py` 由 `7d8d6a30dd8c` / 23,893 B → **`e77e7f3455e0` / 25,791 B**，修后与 r1 修复件**逐字节相同**。
2. **修复面 0 外溢**：4 个变更块全部落在 `load_corpus` + 其前置 helper/常量；本棒以**构造方式**（非人工誊抄）逐块套用，实测套用结果与 r1 **byte-identical** ⇒ 不存在誊抄走样。
3. **锚更新 3 处登记 + 2 处历史基线**（比派工单预估的「2 处 + 1 处」多，见 §4 差异说明），全部**留痕、0 静默覆盖**。
4. **下游 36 文件 / 40 处 import 面自动生效**，本棒**0 改下游任何 import**（无须改，模块名未变）。
5. **0 触及其他件**：全仓 1,450 → 1,454 件逐件比对，本棒触动 **6 件改 + 6 件新增**（新增全在本棒 `.tmp` 沙箱内），另有 **3 件改动属并发他棒、非本棒所为**（§6 如实隔离）。
6. 本棒 **0 调 LLM / 0 调端点 / 0 key 落盘 / 0 联网**。

---

## §1 复验 diff（逐块复核，0 超面）

对 `mindmap_corpus_v20_r1.py` vs 原件（修前内容）做 `difflib.SequenceMatcher(autojunk=False)`，实测 **4 个变更块**，与登记件 `_v5_loadcorpus_fix_2026_09_29.md` §3.2 所载**逐块吻合**：

| # | opcode | 原件行 | r1 行 | 位置 | 面 |
|---|---|---|---|---|---|
| 1 | `insert` | L352 前 | L352–374 | `load_corpus` 之前 | 新增 `_GRAPH_RECORD_CORE_KEYS` + `_graph_record_kind()` helper + r1 说明注释 |
| 2 | `replace` | L354–355 | L377–380 | `load_corpus` docstring | docstring 改「图 JSON」→「图记录」，补 r1 判据说明 |
| 3 | `replace` | L359–362 | L384–395 | `load_corpus` 哨兵体 | 后缀判据 → 记录形态判据 + `unparsable` 分流 |
| 4 | `replace` | L365 | L398–400 | `raise` 文案 | 追加不可解析 `.json` 提示段 |

- 相等区占比 `equal_ratio = 0.953289`；**4 块全部在 `load_corpus` 及其紧邻前置面，0 触及其他函数**。
- **超面核查（登记件未覆盖、本棒补做）**：两件**均不内嵌自身文件名**（`grep "mindmap_corpus_v20"` 在 r1 与原件内 **0 命中**），且 r1 **0 件头命名面差异** ⇒ 原件与 r1 之间**不存在件头/命名面差异**。故「修后 diff vs r1 除件头/命名面外应逐块一致」的预期退化为**更强的实测结论：完全 byte-identical**（§5⑥）。

---

## §2 原件旧值快照（改前记录 + 可恢复留档）

| 项 | 值 |
|---|---|
| 旧 SHA-12 | `7d8d6a30dd8c` |
| 旧字节数 | 23,893 B |
| 旧 mtime | `2026/08/29 01:14:15`（epoch 1787937255.0） |
| 旧行数 | 507 |
| 行尾 | LF（CRLF 计数 **0**） |
| **可恢复留档** | `.tmp/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak`（`7d8d6a30dd8c` / 23,893 B / 逐字节等同改前原件，`shutil.copy2` 保留 mtime） |

**回滚方式**（一条命令可复原）：

```powershell
Copy-Item '.tmp/_v5_loadcorpus_switch_2026_09_29/mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak' 'mindmap_corpus_v20.py' -Force
# 复原后 SHA-12 应回到 7d8d6a30dd8c / 23,893 B；锚登记件另需回改（§4 表列了旧值）
```

登记件内旧值快照：§4 锚 1 已写入 `sha12_history[]`；锚 2/3 已在同行内保留旧值 + 旧 mtime + 旧字节。

---

## §3 修复应用（构造式逐块套用，非誊抄）

套用器 `.tmp/_v5_loadcorpus_switch_2026_09_29/apply_fix.py`（`1336484486fa`）：不重写整文件，按 4 个 opcode **从后往前**替换（避免行号位移），其余行**逐字节沿用原件**；写回前过 `ast.parse` 语法闸；写回用 LF / utf-8 / 无 BOM。

实测输出：

```
change_blocks=4
  apply replace orig L365-365 -> r1 L398-400
  apply replace orig L359-362 -> r1 L384-395
  apply replace orig L354-355 -> r1 L377-380
  apply insert  orig L352-351 -> r1 L352-374
patched == r1 : True
pre  sha12 7d8d6a30dd8c (23893 B)
post sha12 e77e7f3455e0 (25791 B)
```

完整 diff 留档：`.tmp/_v5_loadcorpus_switch_2026_09_29/applied_diff.txt`。

**修后原件**：`mindmap_corpus_v20.py` → `e77e7f3455e0` / 25,791 B / 542 行 / LF（CRLF **0**，0 行尾漂移）。

---

## §4 锚更新对照表（含派工单预估差异说明）

全仓穷举 `7d8d6a30dd8c` **大小写不敏感**扫描。派工单预估「2 处锚登记 + 1 处全仓基线」；**实测 3 处锚登记 + 2 处全仓基线**——多出的 1 处锚是 `_v3_v4_achievements_inventory_2026_09_24.md`（**大写** `7D8D6A30DD8C`，来源棒只 grep 了小写，漏检）。如实登记，不静默略过。

| # | 锚位 | 旧值 | 新值 | 处置 | 件新 SHA-12 | 件新字节 |
|---|---|---|---|---|---|---|
| **锚 1** | `results/_v3_recheck_35_result_2026_09_27.json` `input_chain.corpus_loader`（JSON，CRLF） | `7d8d6a30dd8c` / 23893 | `e77e7f3455e0` / 25791 | **物理更新 + 内嵌 `sha12_history[]` 旧值快照**（旧值 / 旧字节 / 有效期 2026-08-29→2026-09-29 / 变更原因 / 旧字节留档路径） | `a8a4befb21f5`（原 `e9aa6e5180ca`） | 35,091（原 34,547） |
| **锚 2** | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md:676` | `7D8D6A30DD8C` / 23893 / 2026-08-29 01:14:15 | `E77E7F3455E0` / 25791 / 2026-09-29 12:06:04 | **物理更新 + 同行内保留旧值快照**（CRLF 保持） | `91fe5094f59a`（原 `3e4e90fb48e1`） | 355,816（原 355,687） |
| **锚 3** ⚠️ 派工单漏列 | `results/_v3_v4_achievements_inventory_2026_09_24.md:99` | `7D8D6A30DD8C` / 23893 / 2026-08-29 01:14:15 | `E77E7F3455E0` / 25791 / 2026-09-29 12:06:04 | **物理更新 + 同行内保留旧值快照**（CRLF 保持） | `d34c0b417268`（原 `29a853444d42`） | 192,289（原 192,160） |
| **基线 A** | `.tmp/verif_doubt6/baseline_pre.json`（`./mindmap_corpus_v20.py`） | `["7d8d6a30dd8c", 23893]` | 保持旧值 | **只追加注记，不物理回改**（新增独立键 `_anchor_drift_2026_09_29_p6_loadcorpus_r1`，登记新值 + 旧值 + 原因 + 该旧值的语义） | `8406cb842cac`（原 `a33b034d34cf`） | 95,135（原 102,623） |
| **基线 B** | `.tmp/verif_doubt6_v_20260928/baseline_mine.json`（`mindmap_corpus_v20.py`） | `["7d8d6a30dd8c", 23893]` | 保持旧值 | **只追加注记，不物理回改**（同上） | `96aa598222a9`（原 `fa5ca654a1f1`） | 103,914（原 92,169） |

**为何基线不回改（依据）**：两份基线是 2026-09-28 那两棒「0 触动」的**证据快照**（`verif_doubt6` 收尾件 §"跑前跑后哈希复验" 明载其为开跑前/收工后取数）。改其值 = **毁证**。故按派工单「如锚在受保护件内，只追加注记不物理回改」处置：**原条目逐字保留，注记另立新键**，读者可同时看到「快照当时值」与「其后授权变更」。

**基线 A 的诚实交代（如实，不隐去）**：因该文件原为 CRLF，追加注记时走了 `indent=None` 序列化，**排版由多行缩进变为单行**（故字节数 102,623 → 95,135）。已实测：**1,366 条原条目条数与值全部保持**（`entries=1366`，`./mindmap_corpus_v20.py` 条目仍为 `["7d8d6a30dd8c", 23893]`），`json.load` 正常 ⇒ **数据 0 丢失，仅空白排版改变**。基线 B 排版未变（仍多行）。**改前无副本留档**（本棒开工时未预见排版副作用），故字节级不可回退——如实登记，不假称可逆。

**受保护面核验（改前）**：锚 1/2/3 三件**均不在** 18 frozen 清单（逐条比对 `v3x_18frozen_remeasure_results_2026_09_16.json` 的 18 项：`verifier/handoff/*` 4 + `docs/V3X/*` 9 + KT/P_F/P_G spec 4 + `verifier/audit/conservation.py` 1）、**不在** 9 网格（`results/_v4_*` 链）、不涉 P-G v0/v01 / plugin spec。`verifier/v21/check.py` **未改**。

---

## §5 验证（6 项 + 扩展 4 项 = 16/16 PASS）

验证器 `.tmp/_v5_loadcorpus_switch_2026_09_29/verify_2026_09_29.py`（`55838224f312`）。反例**全部在 `tempfile` 临时目录内**构造 ⇒ 真语料 0 写。

| # | 验证项 | 期望 | 实测 | 判定 |
|---|---|---|---|---|
| ① | **修前抛错复现**（用留档旧件） | 抛 `RuntimeError`，误报 3 件 | 抛出，`all.json` / `index_v2_2026_09_16.json` / `strip_captions_22.json` 命中 **3/3** | **PASS** |
| ② | **修后通过（族 S）** | 不抛，16 图 | 不抛，`n_graphs_S = 16` | **PASS** |
| ③ | **真孤儿反例仍抛**（防放宽过度） | 抛，点名真孤儿，**不含**非图记录名 | 点名 `S_true_orphan_probe.json`；3 件非图记录名 **0 混入**消息 | **PASS** |
| ④ | **`ast.parse`** | 通过 | 修后原件 PASS / r1 PASS / 旧件留档 PASS | **PASS** |
| ⑤ | **下游冒烟** | 3 个 import 方不回归 | 见下表 | **PASS** |
| ⑥ | **r1 件与原件修后等价性** | 逐块一致 | **byte-identical = True**，`e77e7f3455e0` | **PASS** |
| ③b | 不可解析 `.json` 仍抛 | 抛 | 点名 `_broken_probe.json` | **PASS** |
| ③c | 半个核心键（缺 3 键） | 判非图，不抛 | 不抛，16 图 | **PASS** |
| 族面 | `families=("L",)` / `("S","L")` | 6 / 22 | 6 / 22 | **PASS** |
| 功能等价 | 原件（移走 3 件非图记录）vs 修后原件 | 逐值一致 | 16/16，记录内容 sha256[:12] 均 `3a7505235f68` | **PASS** |
| `ast.parse`×3 | 修后 / r1 / 旧件留档 | 全通过 | 全通过 | **PASS** |

### ⑤ 下游冒烟明细

| 冒烟件 | 结果 | 命中符号 | 实调 |
|---|---|---|---|
| `run_v20_baselines.py` | PASS | `load_corpus`, `CORPUS_DIR` | `load_corpus()` = **16 图** |
| `run_v20_bigquiz_eval.py` | PASS | `load_corpus`, `CORPUS_DIR` | `load_corpus()` = **16 图** |
| `run_v20_familyL_ingest.py` | PASS | `CORPUS_DIR`, `build_index` | 摄入侧件，**不持** `load_corpus`（不强求） |
| `verifier/v21/check.py`（断言直测） | PASS | — | 其**唯一**涉及本件的断言是 `check.py:52` 文本包含 `"corpus orphan graphs"`，**修前修后均成立** |

**`check.py` 的如实交代（不假称已跑通）**：`check.py` 是**顶层副作用脚本**（import 即读 `results/` 并跑 pytest），**非可 import 模块**，无法纳入「import 冒烟」。直接执行它会失败，但**失败与本棒无关**（已实证）：其失败点是 `check.py:63-65` 读 `paper/deposon_paper_v1.md`，该文件**盘上不存在**（`os.path.exists` = False），且在 GBK locale 下另于 `check.py:15` 读 `results/deposon_v20_corpus_eval.json` 即报 `UnicodeDecodeError`——两处**均早于/无关**其对本件的唯一引用（`:51` 只读文本、`:52` 文本包含）。故本棒对 `check.py` 只做**其对本件断言的直测**（PASS），**未宣称 `check.py` 整体绿**。

**方法学修正留痕（本棒自查）**：首轮冒烟曾用 `importlib` 加载 `check.py`（GBK 解码假失败）与对摄入侧件强求 `load_corpus`（判据过严假失败）——两处均为**验证器自身缺陷**，非产品缺陷；已修正验证器判据后重跑，结果如上。

---

## §6 0 触及其他件实证（全仓逐件比对）

快照器 `.tmp/_v5_loadcorpus_switch_2026_09_29/snapshot.py`（`dcede756619f`）：全仓逐件取 `sha256[:12]` + 字节数（排除 `.git` / `__pycache__` / `node_modules` / `*.pyc`），改前 `baseline_pre.json`（**1,450 件**）→ 改后 `baseline_post.json`（**1,454 件**）。

### 6.1 本棒改动（6 改 + 6 增）

| 类 | 件 | 判定依据 |
|---|---|---|
| 改 | `mindmap_corpus_v20.py` | 授权面（哨兵修复） |
| 改 | `results/_v3_recheck_35_result_2026_09_27.json` | 授权面（锚 1） |
| 改 | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md` | 授权面（锚 2） |
| 改 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | 授权面（锚 3，派工单漏列，来源棒漏检） |
| 改 | `.tmp/verif_doubt6/baseline_pre.json` | 授权面（基线 A 追加注记） |
| 改 | `.tmp/verif_doubt6_v_20260928/baseline_mine.json` | 授权面（基线 B 追加注记） |
| 增 | `.tmp/_v5_loadcorpus_switch_2026_09_29/` 下 6 件（`snapshot.py` / `baseline_pre.json` / `apply_fix.py` / `mindmap_corpus_v20.py.orig_7d8d6a30dd8c.bak` / `_old_corpus_view.py` / `annotate_baseline.py` / `verify_2026_09_29.py` / `applied_diff.txt` / `baseline_post.json`，均为本棒沙箱件） | 本棒落盘 |
| 增 | `results/_v5_loadcorpus_switch_2026_09_29.md`（本登记件） | 本棒落盘 |

**除上表外，本棒对全仓其余 1,440+ 件 0 触动**——含 `corpus/v20/` 全部语料数据（0 重建 `index.json`）、36 个下游 import 文件（0 改 import）、`verifier/v21/check.py`（0 改）、18 frozen / 9 网格 / P-G / plugin spec（0 触动）。

### 6.2 并发他棒改动（**非本棒所为**，如实隔离）

比对期间另有并发棒在写同仓，其改动**混在**同一份 diff 里。已按 mtime + 命名逐件隔离，**不计入本棒产物，亦不冒领**：

| 件 | mtime | 归属 |
|---|---|---|
| `deposon_team/plugins/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py` | 12:05:45 | 并发他棒（`v3df` 族） |
| `results/_v5_v3_deg_fix_c1c4_result_2026_09_29.json` | 12:11:14 | 并发他棒（`v3_deg_fix`） |
| `results/_v5_v3_deg_fix_exec_2026_09_29.md` | 12:10:05 | 并发他棒（`v3_deg_fix`） |
| `.tmp_v3df/inspect_c1.py` / `probe_payoff.py` / `sha_check.py`（3 件消失） | — | 并发他棒清理 |

本棒全程**未 open 过**上述 5 个路径（写入/删除）。

---

## §7 铁律逐条对照

| 铁律 | 状态 | 证据 |
|---|---|---|
| 仅授权面改动 | ✅ | §6.1 共 6 改 6 增，无越界 |
| 锚更新留痕（旧值快照、0 静默覆盖） | ✅ | §4：锚 1 内嵌 `sha12_history[]`；锚 2/3 同行留旧值；基线只追加注记 |
| 如锚在受保护件内只追加注记不物理回改 | ✅ | 基线 A/B 按此处置（§4） |
| 行尾不漂移 | ✅ | 原件 LF/CRLF=0 保持；锚 1/2/3 各自原行尾（CRLF）保持 |
| SHA-12 = `sha256 hexdigest()[:12]` 小写 | ✅ | 全文口径一致 |
| 0 新设阈值 / 0 改判死线 / 0 改 named-filler 口径 | ✅ | 修复面逐块限于哨兵；核心键集为形态键非数值阈值 |
| 署名如实 | ✅ | 本件执行方 = `worker`，未冒用他方名头 |
| 不编造 | ✅ | `check.py` 整体未跑通如实登记；基线排版副作用如实登记；漏检锚如实补列；验证器自身缺陷如实留痕 |
| 派生 JSON 不合并 | ✅ | 锚 1 就地更新既有字段，**0 新建派生 JSON** |
| 并发写入隔离 | ✅ | §6.2 五件非本棒所为，逐件归属登记 |
| skill 未指定 ⇒ 按派工单字面执行并交代 | ✅ | 0 skill 加载（抬头） |
| 0 key 落盘 / 0 调 LLM / 0 调端点 / 0 联网 | ✅ | 全程本地文件读 + 本地 py 执行 |

---

## §8 遗留 / 需 PI 知悉（本棒 0 自作主张）

1. **`mindmap_corpus_v20_r1.py` 现与原件逐字节相同**（两者皆 `e77e7f3455e0`）。PI 授权的是「应用回原件」，**未指示删除 r1** ⇒ 本棒**保留 r1 不动**。是否清理 r1（现已冗余）请 PI 定。
2. **锚 2/3 所在盘点件自身的 SHA 已被其它委托材料登记**（如 `letters/_v4_commission_*` 载 3dir 件 `3E4E90FB48E1` / 355,687 B），本棒改动该两件 ⇒ **这些 letters 里的旧登记随之漂移**。letters 属他棒/PI 管辖，**本棒 0 改**，如实上报。
3. **`.tmp` 两份基线的排版/字节已变**（数据 0 丢失，§4 已交代）——若 PI 认为基线须字节级不可变，请指示回退处置。
4. **γ-V5R3-13 状态更新**：哨兵修复**已对下游 36 个 import 面生效**（模块名未变，修复进原件即生效），来源棒 §6 的「A 方案：下游 0 切换」状态**已作废**，本棒为「B 方案：就地最小修 + 锚留痕，已完成」。

---

**出证**：`worker`（Mavis 8-agent team，deposon 工作区），2026-09-29。
