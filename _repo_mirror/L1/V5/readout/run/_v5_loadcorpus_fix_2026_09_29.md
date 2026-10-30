# P-6 修 `load_corpus` 孤儿哨兵（V4 GT 执行棒 γ-V5R3-13 遗留）— 修订件落盘报告

- **日期**：2026-09-29 上午
- **执行**：`worker`（Mavis 8-agent team，deposon 工作区）
- **来源**：`results/_v5_gt_exec_2026_09_29.md` §10.1 P-6 / §10.2 γ-V5R3-13（GT 执行棒自报 `9a679f43f796`）
- **授权**：PI 拍板「修加载器」（`ask_1e658ed52e7856a0bb3647ed` q2）
- **skill**：派工单未指定 skill 名 ⇒ **0 skill 加载**（沿 GT 执行棒 γ-V5R3-10 同口径）

---

## §0 结论上限（先说边界，防误导）

1. 本棒**只修 `load_corpus` 的孤儿判据**，**不重建 `index.json`、不触碰 `corpus/v20` 任何数据**。
2. 修订件 `mindmap_corpus_v20_r1.py` 是**新名独立件**；**原件 `mindmap_corpus_v20.py` 0 触动**（跑前跑后 SHA-12 逐值相同，见 §5）。
3. **下游 36 个 import 面 0 切换**：现有 `run_v20_*.py` / `tests/*` 全部仍 import 原件 ⇒ 本棒修的是「后续复用不再撞上」的前置件，**既有执行面行为一字未变**。是否切换到 r1 属 PI 二次定（§6）。
4. 修复**未设任何新阈值**、**未改判死线**、**未改 named/filler 口径**、**未改 `build_index`**。
5. 本棒**0 调 LLM / 0 调端点 / 0 key 落盘**。

---

## §1 缺陷复现（修前抛错，3 件误判实证）

原件判据（`mindmap_corpus_v20.py:359-361`）按**文件名后缀**把目录下所有 `.json` 一律当图记录：

```python
orphans = sorted(fn for fn in os.listdir(corpus_dir)
                 if fn.endswith(".json") and fn != "index.json"
                 and fn not in registered)
```

实测（对真语料目录 `corpus/v20` 调原件 `load_corpus`）：

| 项 | 实测值 |
|---|---|
| 抛出 | `RuntimeError` |
| 误报件数 | **3** |
| 误报名 | `all.json` / `index_v2_2026_09_16.json` / `strip_captions_22.json` |

**3 件的真实形态**（读盘核对）：

| 文件 | 顶层类型 | 顶层键 | 为何不是图记录 |
|---|---|---|---|
| `all.json` | dict | `agents` / `generated_at` / `layout` / `paths` / `version` | 布局清单，无 `graph_id`/`edges`/`N` |
| `index_v2_2026_09_16.json` | dict | `captions` / `corpus` / `fingerprint_anchors` / `graphs` / `integrity` / `n_captions` / `n_graphs` / … | **是另一份索引**（含 `graphs` 清单），非单图记录 |
| `strip_captions_22.json` | **list** | 22 元素 | 字幕条目列表，顶层非 dict |

对照：22 件真图记录（族 S 16 + 族 L 6）**全部**为 dict 且含 `graph_id`/`family`/`N`/`edges`。

**根因（非机械诚实，追问到根）**：判据用了**文件名维度**（`.json` 后缀）代替**记录形态维度**。哨兵的本意是「摄入未建索引导致静默漏图」，但语料目录同时承载了图记录与非图记录两类 `.json`，后缀判据无法区分二者 ⇒ 误报。**非构造失灵、非环境问题**，是判据选错维度。

---

## §2 frozen 核验（先核后动）

### §2.1 核验方法与证据

| 受保护面 | 盘上锚 | `mindmap_corpus_v20.py` 是否在内 |
|---|---|---|
| **18 frozen** | `results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json`（18 项逐条列名，全仓穷举核对） | **不在**（18 项为 `docs/V3X/*` 9 件 + `verifier/handoff/*` 4 件 + KT/P_F/P_G spec 4 件 + `verifier/audit/conservation.py` 1 件） |
| **9 网格** | `results/_v4_*` 链（派工单与 `letters/_v4_commission_paper_final_glm_2026_09_24_v4.md:174` 定义为 results 链层） | **不在**（该模块不在 `results/_v4_*` 链内） |
| **哈希锚登记** | `results/_v3_recheck_35_result_2026_09_27.json:78-82`：`corpus_loader` sha12 = `7d8d6a30dd8c`，`access: read_only` | **是**（以只读锚登记） |
| **成就清单** | `results/_v3_v4_achievements_inventory_3dir_2026_09_24.md:676`：sha12 `7D8D6A30DD8C`，View `C` | **是** |
| **全仓基线** | `.tmp/verif_doubt6/baseline_pre.json` / `baseline_mine.json` 收录 `./mindmap_corpus_v20.py` → `7d8d6a30dd8c` / 23893 | **是** |
| **P-G v0/v01** | — | 不涉及 |
| **plugin spec** | — | 不涉及 |
| **verifier 内置脚本** | `verifier/v21/check.py` 引用该模块名（只读引用） | 不改 verifier |

### §2.2 核验结论与据此采取的处置

- **不在** 18 frozen / 9 网格 / P-G / plugin spec 正式清单内；
- **但**以 SHA-12 `7d8d6a30dd8c` 落在**两处哈希锚登记 + 一处全仓基线**上，且被 **36 个文件、40 处 import** 引用（`run_v20_*` 族 + `tests/*` + `verifier/v21/check.py`）。

⇒ **引用面过宽** ⇒ 按派工单「先核后动 / 安全侧」：**出新名修订件 `mindmap_corpus_v20_r1.py`，原件 0 触动**。未做就地最小修（对比方案见 §6，留 PI 二次定）。

---

## §3 修复面（逐行核验；仅哨兵逻辑面）

修复件：`mindmap_corpus_v20_r1.py`（新名；仓库根，与原件同目录 ⇒ `HERE/corpus/v20` 解析路径与原件完全一致，**0 改路径解析**）。

### §3.1 判据变更（唯一实质变更）

| 面 | 原件 | r1 |
|---|---|---|
| 判据维度 | 文件名后缀 `fn.endswith(".json")` | **记录形态**：`isinstance(obj, dict)` 且含 4 核心键 |
| 核心键集 | — | `("graph_id", "family", "N", "edges")`（模块常量 `_GRAPH_RECORD_CORE_KEYS`） |
| 分类函数 | — | 新增私有 `_graph_record_kind(path) -> "graph" \| "non_graph"` |
| 不可解析 .json | 落入 orphan 并抛错（**保持**） | 单独收进 `unparsable` 列表，**仍抛错**（不静默跳过） |
| 抛错条件 | `if orphans:` | `if orphans or unparsable:`（**只放宽非图记录，不放宽真孤儿**） |

**核心键选法依据（现场代码为准，0 自创）**：`generate_graph()` 产出的记录含 `graph_id`/`family`/`N`/`edges`；族 L 记录（`run_v20_familyL_ingest` 摄入）同样含此 4 键。**刻意不要求 `target`**——实测族 L 记录顶层键无 `target`（见 §1 对照表），若按族 S 全键要求会把族 L 真孤儿漏放。

### §3.2 完整 diff（4 个变更块，全部落在 `load_corpus` 邻近面）

```diff
@@ -349,20 +349,55 @@
     return {"written": written, "n_graphs": idx["n_graphs"]}
 
+
+# ---------------------------------------------------------------- 孤儿哨兵 r1（P-6）
+# r1 修订（PI 2026-09-29 拍板「修加载器」，源 results/_v5_gt_exec_2026_09_29.md
+# P-6 / γ-V5R3-13）：原判据按**文件名后缀**（``fn.endswith(".json")``）把目录下
+# 所有 .json 一律当图记录，致 3 个**非图记录** .json（all.json /
+# index_v2_2026_09_16.json / strip_captions_22.json）被误判为孤儿图
+# ⇒ load_corpus 抛 RuntimeError。
+# r1 改按**记录形态**判定：图记录 = dict 且同时含 graph_id / family / N /
+# edges 四个核心键（族 S 与族 L 记录均满足；不要求 target——族 L 记录无该键）。
+# 核心键齐备但未入册 ⇒ 仍是真孤儿（哨兵不放宽）；不可解析的 .json 仍上抛
+# （不静默跳过）。
+# 0 改 build_index / 0 重建 index.json / 0 改 corpus 数据 / 0 新设阈值。
+_GRAPH_RECORD_CORE_KEYS = ("graph_id", "family", "N", "edges")
+
+
+def _graph_record_kind(path: str) -> str:
+    """"graph" | "non_graph"——按记录形态分类单个 .json（不依赖文件名）。"""
+    with open(path, encoding="utf-8") as f:
+        obj = json.load(f)
+    if isinstance(obj, dict) and all(k in obj for k in _GRAPH_RECORD_CORE_KEYS):
+        return "graph"
+    return "non_graph"
+
+
 def load_corpus(corpus_dir: str = CORPUS_DIR, families=("S",)) -> list:
     """按 index.json 顺序读入图记录（默认只读族 S）。
-    孤儿哨兵（R2/E3）：目录中存在未入册的图 JSON 时显式报错——
-    防「摄入未建索引导致静默漏图」复发。"""
+    孤儿哨兵（R2/E3，r1 修订 P-6）：目录中存在未入册的**图记录** JSON 时
+    显式报错——防「摄入未建索引导致静默漏图」复发。
+    r1：孤儿按**记录形态**判定（graph_id/family/N/edges 四核心键），
+    非图记录 .json 不再误判；真孤儿与不可解析 .json 仍上抛。"""
     with open(os.path.join(corpus_dir, "index.json"), encoding="utf-8") as f:
         idx = json.load(f)
     registered = {e["file"] for e in idx["graphs"]}
-    orphans = sorted(fn for fn in os.listdir(corpus_dir)
-                     if fn.endswith(".json") and fn != "index.json"
-                     and fn not in registered)
-    if orphans:
+    orphans, unparsable = [], []
+    for fn in sorted(os.listdir(corpus_dir)):
+        if not fn.endswith(".json") or fn == "index.json" or fn in registered:
+            continue
+        try:
+            kind = _graph_record_kind(os.path.join(corpus_dir, fn))
+        except (ValueError, UnicodeDecodeError):
+            unparsable.append(fn)
+            continue
+        if kind == "graph":
+            orphans.append(fn)
+    if orphans or unparsable:
         raise RuntimeError(
             f"corpus orphan graphs (not in index.json): {orphans} — "
-            "先运行 build_index()（R2/E3 哨兵）")
+            "先运行 build_index()（R2/E3 哨兵）"
+            + (f"；不可解析 .json（形态判据无法应用，报错不静默）：{unparsable}"
+               if unparsable else ""))
     out = []
     for e in idx["graphs"]:
         if families and e["family"] not in families:
```

变更块定位（`difflib` opcode）：`insert @orig L352` / `replace L354-355` / `replace L359-362` / `replace L365` ⇒ **共 4 块，全部在 `load_corpus` 函数体 + 其前置常量/helper，0 触及其他函数**。

### §3.3 「0 触及其他面」的机器核验

`ast.dump`（`include_attributes=False`）逐函数哈希对照：

| 项 | 原件 | r1 |
|---|---|---|
| 顶层函数总数 | 22 | 23 |
| **AST 不一致的函数** | — | **仅 `load_corpus`**（21/22 逐 AST 相同） |
| 新增函数 | — | `_graph_record_kind`（新增私有 helper） |
| 新增模块常量 | — | `_GRAPH_RECORD_CORE_KEYS` |

`build_corpus` / `build_index` / `generate_graph` / `corpus_plan` / `is_dag` / `longest_path_family` / `parse_familyL_response` / `_PROMPT_TEMPLATE` 等**全部逐 AST 相同** ⇒ 0 改生成面、0 改族 L 解析面。

---

## §4 验证（7 项，全 PASS）

验证脚本：`.tmp/_v5_loadcorpus_verify_2026_09_29.py`（sha12 `7b8fc7e9ed7f`，171 行，**新名件**）。反例构造**全部在 `tempfile` 临时目录内**（真语料 0 写）。

| # | 验证项 | 期望 | 实测 | 判定 |
|---|---|---|---|---|
| ① | **修前复现**：原件 `load_corpus` 对真语料 | 抛 `RuntimeError`，误报 3 件 | 抛出，命中 `all.json` / `index_v2_2026_09_16.json` / `strip_captions_22.json` **3/3** | **PASS** |
| ② | **修后通过**：r1 对真语料 | 不抛，读出族 S 16 图 | 不抛，`n_graphs_S = 16` | **PASS** |
| ③ | **真孤儿反例**（防放宽过度） | r1 仍抛且只点真孤儿 | 抛错，点名 `S_true_orphan_probe.json`，**3 件非图记录名 0 出现在消息中** | **PASS** |
| ③b | **不可解析 .json** | 仍抛（不静默） | 抛错并点名 `_broken_probe.json` | **PASS** |
| ③c | **半个核心键**（`graph_id` 有，`edges`/`family`/`N` 缺） | 判非图记录，不抛 | 不抛，`n_graphs_S = 16` | **PASS** |
| ③d | **反证**：删 3 件非图记录后调**原件** | 原件应通过（证误报确源于此） | 不抛，16 图 | **PASS** |
| ④ | **语法** `ast.parse` | 双件通过 | orig PASS / rev PASS | **PASS** |
| ⑤ | **0 触动**（跑前跑后哈希复验） | 原件与语料均不变 | 见 §5 | **PASS** |

**③ 的关键读数**：`non_graph_absent = true` ⇒ r1 的抛错消息里**只**含真孤儿，**不含**任何非图记录名 ⇒ 修复是**精准放宽**，不是整体关掉哨兵。

**功能等价核验**（原件 vs r1，同一目录条件下返回值逐值一致）：

| 口径 | 件数 | 记录内容 sha256[:12] |
|---|---|---|
| 原件（移除 3 件非图记录）族 S | 16 | `3a7505235f68` |
| r1（同目录）族 S | 16 | `3a7505235f68` |

⇒ **等价 = True**。另：r1 对真语料读出 `families=("S",)` → 16、`("L",)` → 6、`("S","L")` → 22，与 `index.json` 登记的 22 图一致 ⇒ 族 L 面 0 回归。

**未跑的检查（如实交代）**：`pytest` **未安装**（`No module named pytest`）⇒ `tests/test_v20.py::test_on_disk_corpus_index_consistent`（L299-307，断言 `len(graphs) == 16`）**未以 pytest 形式执行**。已用上表「修后通过 = 16 图」+「原件/修订件返回值逐值等价」两条实跑覆盖同一断言口径，但**不等于 pytest 绿**，如实登记为未验项。

---

## §5 0 触动实证（跑前跑后哈希复验）

SHA-12 口径：`hashlib.sha256(...).hexdigest()[:12]` 小写（派工单铁律）。

| 件 | 跑前 sha12 | 跑后 sha12 | 字节 | 判定 |
|---|---|---|---|---|
| `mindmap_corpus_v20.py`（原件） | `7d8d6a30dd8c` | `7d8d6a30dd8c` | 23893 → 23893 | **0 触动** |
| `corpus/v20/`（全目录聚合摘要） | `ad2a7ab3f37e` | `ad2a7ab3f37e` | — | **0 触动** |
| `corpus/v20/index.json` | — | `8423ffe266af` | 7335 | **0 重建** |
| `mindmap_corpus_v20_r1.py`（修复件，新名） | — | `e77e7f3455e0` | 25791 | 新增 |

原件 SHA-12 `7d8d6a30dd8c` 与两处盘上登记（`_v3_recheck_35_result_2026_09_27.json:80`、成就清单 `7D8D6A30DD8C`）及全仓基线 `.tmp/verif_doubt6/baseline_pre.json` **逐值吻合** ⇒ 既有哈希锚**未漂移**。

**新增/落盘件清单**（全部新名）：

| 件 | SHA-12 | 字节 | 行 |
|---|---|---|---|
| `mindmap_corpus_v20_r1.py` | `e77e7f3455e0` | 25,791 | 542 |
| `.tmp/_v5_loadcorpus_verify_2026_09_29.py` | `7b8fc7e9ed7f` | 7,297 | 171 |
| `results/_v5_loadcorpus_fix_2026_09_29.md` | 见 §7 回报 | — | — |

原件行尾：LF（CRLF 计数 0）；r1 沿用 LF ⇒ 0 行尾漂移。

---

## §6 待 PI 二次定：是否切下游 import 面

派工单要求：引用面过宽须如实登记并给出「就地最小修 + 留痕」方案对比，**由 PI 二次定**，不自作主张。

| 方案 | 内容 | 触动面 | 留痕 | 风险 |
|---|---|---|---|---|
| **A（本棒已交付）** | 新名 r1 件存在，下游 36 文件 0 切换 | **0 触动**（原件/语料/verifier 全不动） | 本报告 + 修复件 | 哨兵修复**未生效于既有执行面**；后续复用须显式 `import mindmap_corpus_v20_r1`（否则仍撞旧哨兵） |
| **B 就地最小修 + 留痕** | 改 `mindmap_corpus_v20.py:359-365` 哨兵（diff 同 §3.2），并在 `_v3_recheck_35_result_2026_09_27.json` 的 `corpus_loader.sha12` 留痕更新为新值 + 出修订记录 | 触动 1 件原件 + 2 处哈希锚登记（`corpus_loader.sha12`、成就清单行） | 需同步更新 2 处锚，否则锚漂移 | 36 处 import 行为**立即同步改变**（正面：修复生效；风险面：既有 0 基线假定 `7d8d6a30dd8c` 的复核件将锚漂移） |
| **C 下游渐进切换** | 保留原件，新增 `mindmap_corpus_v20_r1` 并逐个 `run_v20_*` 显式改 import（每改一件留痕） | 逐件递增 | 每件一条 | 改动面最大、工时最长，但每步可回滚 |

**本棒处置**：只交 A，**B / C 未执行、未预判**。PI 定为 B 或 C 时，`_v5_gt_exec_2026_09_29.md` P-6 / γ-V5R3-13 即可结案（哨兵本体修完）；PI 若维持 A，则 γ-V5R3-13 状态应改记为「修复件已备、下游未切换」。

---

## §7 铁律逐条对照

| 铁律 | 本棒状态 | 证据 |
|---|---|---|
| 优先新名件 | ✅ | 出 `mindmap_corpus_v20_r1.py`，未就地改 |
| 既有件 0 触动（含 `mindmap_corpus_v20.py` 原件、corpus/v20 数据） | ✅ | §5 跑前跑后 SHA-12 逐值相同 |
| 0 新设阈值 | ✅ | 核心键集取自现场 `generate_graph()` 产出形态；非数值阈值 |
| 0 改判死线 / named-filler 口径 | ✅ | 生成面 21/22 函数逐 AST 相同（§3.3） |
| SHA-12 = `sha256 hexdigest()[:12]` 小写 | ✅ | 全文口径一致 |
| 署名如实（worker） | ✅ | 本文件执行方 = `worker`；未冒用他方名头 |
| 不编造 | ✅ | `pytest` 未装如实登记（§4）；未跑项 0 声称为已跑 |
| skill 未指定 ⇒ 按派工单字面执行并交代 | ✅ | 0 skill 加载（抬头） |
| 0 key 落盘 / 0 调 LLM / 0 调端点 | ✅ | 全程本地文件读 + 本地 py 执行 |

---

## §8 结论

- **P-6 哨兵误报已修**：修前 3 件误判复现（① PASS），修后不抛且 16 图通过（② PASS），真孤儿反例仍被检出且消息不含非图记录名（③ PASS），不可解析 .json 仍上抛（③b PASS），双件 `ast.parse` 通过（④ PASS），原件与语料 0 触动（⑤ PASS）。
- **修复面 0 外溢**：4 个 diff 块全部落在 `load_corpus` + 前置 helper/常量；21/22 顶层函数逐 AST 相同。
- **哨兵未被放宽过度**：真孤儿、不可解析 .json 两类反例均仍触发抛错；唯一被排除的是「顶层非 dict」或「缺 4 核心键」的非图记录。
- **γ-V5R3-13 状态**：哨兵本体**已修**（新名件），但**下游 36 个 import 面 0 切换** ⇒ 复用方须显式引入 r1 才吃到修复。是否切换留 **§6** 由 PI 二次定。

**出证**：`worker`（Mavis 8-agent team，deposon 工作区），2026-09-29。
