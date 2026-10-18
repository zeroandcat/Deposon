# D9 残留断链面 · 补修登记（P-1／P-2／P-3）

> **本棒身份**：D9 之**补修执行棒**（PI 卡 `ask_02ecc63d3808dcd8425629e2` 裁「**甲：扩授权补断链面（P-1/P-2/P-3）**」）。
>
> **授权范围**：**唯一编辑对象 ＝ 复核件所指之 3 件 `.py`**（H3／H4／H5），**逐行留痕**。⛔ 0 编辑任何 markdown 既有件；⛔ 0 新建／移动／重命名／删除除本件外任何件；⛔ 0 覆写。
>
> **上游件（只读回读，⛔ 0 回改）**：独立复核件 `results/_d9_independent_review_2026_10_12.md`（SHA-12 `732cfae29bbc`）· 执行登记 `results/_d9_rewrite_execution_register_2026_10_12.md`（SHA-12 `0ea7852c4511`）。
>
> **产出**：本件（唯一新件）。
>
> **执行**：worker（补修执行棒）· 2026-10-12 (+08:00)

---

## 0. 补修口径

| 项 | 值 |
|---|---|
| 修法总则 | **最小行级**：⛔ 0 改他行、⛔ 0 改格式／行尾／编码、⛔ 0 增删 import |
| 落笔量 | **9 行**（H4 ×3 ＋ H5 ×4 ＋ H3 ×2） |
| 行级留痕 | §A 逐条 **before → after 照录** |
| 验证方式 | **静态**：指纹／逐行差分／`ast.parse`／`pathlib` 纯路径求值。⛔ **0 执行任何 runner** |
| 0 回改 | 上游 2 件 md **一字未动**（实测指纹见 §D-3，与在册值逐位吻合） |

---

## §A 补修明细（逐条 · 照录）

### A-1 · P-1 · H4／H5 之 `os.listdir(RESULTS)` 域读取面（硬阻断）

- **病灶事实**：`RESULTS` 仍 ＝ `deposon-sub\results`，而 `*addendum*.json` **实测 sub 侧 0 件／repo 侧 21 件** ⇒ `load_domain()` 返空 ⇒ `domain_gate` `len(files) != 21` ⇒ `sys.exit(2)`。
- **修法**：将 3 处**域读取调用点**改指既有 D9 常量 `REPO_RESULTS`（＝ `D:\私人资料\deposon-repo\results`）。
- **为何改调用点而不改 `RESULTS` 定义行**：① 全件 `RESULTS` 实测**仅 4 处**（定义 ＋ 3 读取），逐处皆**只读**，改定义行虽省 1 行但**改变常量语义**（牵动 `RESULTS` 之名）；② 改调用点则 `RESULTS` 定义行**一字不动**、`REPO_RESULTS`（L61／L74）在调用点之前定义，**无先后序问题**；③ 与执行登记 §2 已确立之「显式绝对路径常量」口径一致，⛔ 0 新造字面。

**件 H4** `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py`

| 行 | BEFORE | AFTER |
|---|---|---|
| L112 | `        [f for f in os.listdir(RESULTS) if f.endswith(".json") and "addendum" in f],` | `        [f for f in os.listdir(REPO_RESULTS) if f.endswith(".json") and "addendum" in f],` |
| L118 | `        p = os.path.join(RESULTS, name)` | `        p = os.path.join(REPO_RESULTS, name)` |
| L140 | `        p = os.path.join(RESULTS, name)` | `        p = os.path.join(REPO_RESULTS, name)` |

**件 H5** `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`

| 行 | BEFORE | AFTER |
|---|---|---|
| L161 | `        [f for f in os.listdir(RESULTS) if f.endswith(".json") and "addendum" in f],` | `        [f for f in os.listdir(REPO_RESULTS) if f.endswith(".json") and "addendum" in f],` |
| L167 | `        data = read_json(os.path.join(RESULTS, name))` | `        data = read_json(os.path.join(REPO_RESULTS, name))` |
| L186 | `        p = os.path.join(RESULTS, name)` | `        p = os.path.join(REPO_RESULTS, name)` |

**静态验证**：`REPO_RESULTS` 下 `*addendum*.json` 实测 **21 件** ＝ `domain_gate` 期望值；`os.path.join` 承 raw str 合法（两件均仅 `import os`，⛔ 0 增 import）。

### A-2 · P-2 · H3 之 `relative_to(REPO)` ×2（必抛 `ValueError`）

- **病灶事实**：`REPO` ＝ `deposon-sub`（⛔ 未改），而 4 条输入常量已改指 `deposon-repo` ⇒ `relative_to` 抛错；**L117 位于模块顶层 ⇒ 导入即崩**。
- **修法**：改**两处调用**之基准为 `REPO_ROOT.parent`（＝ `D:\私人资料`，两区之**共同祖先**）。
- **为何不改 `REPO` 定义行（L56）**：改 L56 虽省 1 行，但会**连带改写** `SRC_BOSS_PA1`（L60，依底本 §2.6 明示 0 改动）与 `SRC_ANCHOR_FALLBACK`（L62，P-4 待裁面）之**实际指向**——此二者为执行登记 §6 明载之登记项，⛔ 0 由本棒静默变更。改调用点则二者**逐字不动**。
- **为何取 `REPO_ROOT.parent` 而非 `REPO_ROOT`**：`inputs` 四项中 `SRC_BOSS_PA1` 仍锚 `REPO`（sub 面），`REPO_ROOT` **非其祖先** ⇒ 取 `REPO_ROOT` 会使 L117 **由 3/4 错变为 4/4 错**；取共同祖先则 **4/4 ＋ OUT_JSON 5/5 全通过**（下方实测）。L735 之 `OUT_JSON` 属 repo 侧，取共同祖先亦通过，**两行取同一基准**以免口径分裂。

**件 H3** `_v3_recheck_05_executor_2026_09_28.py`

| 行 | BEFORE | AFTER |
|---|---|---|
| L117 | `        "path": str(v.relative_to(REPO)).replace("\\", "/"),` | `        "path": str(v.relative_to(REPO_ROOT.parent)).replace("\\", "/"),` |
| L735 | `print(f"[产出] {OUT_JSON.relative_to(REPO)}  bytes={OUT_JSON.stat().st_size}  sha12={sha12(OUT_JSON)}")` | `print(f"[产出] {OUT_JSON.relative_to(REPO_ROOT.parent)}  bytes={OUT_JSON.stat().st_size}  sha12={sha12(OUT_JSON)}")` |

**静态验证**（纯 `pathlib` 求值，⛔ 0 执行 runner）：

| 项 | 基准 `REPO_ROOT.parent` ＝ `D:\私人资料` 之求值 |
|---|---|
| `SRC_V3_PHYS` | `deposon-repo\results\deposon_v3_physical_opt_60cells_2026_09_11.json` |
| `SRC_PE3` | `deposon-repo\results\deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` |
| `SRC_BOSS_PA1` | `deposon-sub\results\boss_pa_1_rbr_rm_result_2026_09_15.json` |
| `SRC_ANCHOR_MAIN` | `deposon-repo\verifier\audit\conservation.py` |
| `OUT_JSON`（L735） | `deposon-repo\results\_v3_recheck_05_result_2026_09_28.json` |

**5/5 通过，0 `ValueError`**（改前为 3/5 抛错）。

### A-3 · P-3 · H5 之 `.tmp` 导入面（`ModuleNotFoundError`）

- **病灶事实**：L314 `sys.path.insert(0, os.path.join(REPO, ".tmp"))`，`REPO` ＝ `deposon-sub` ⇒ `sub\.tmp` **`isdir=False`**。
- **修法**：改该行之 `.tmp` 基准为 `os.path.dirname(REPO_RESULTS)`（＝ repo 根），**复用既有 D9 常量**、⛔ 0 新造字面。

**件 H5** `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`

| 行 | BEFORE | AFTER |
|---|---|---|
| L314 | `    sys.path.insert(0, os.path.join(REPO, ".tmp"))` | `    sys.path.insert(0, os.path.join(os.path.dirname(REPO_RESULTS), ".tmp"))` |

**静态验证**：目标 `D:\私人资料\deposon-repo\.tmp` 实测 **`isdir=True`**，`s4_regen_runner.py` **存在**（`sub\.tmp` 仍 `isdir=False`／文件不存在）。
⛔ L315 之 `import` 行、⛔ L317 之 `.tmp/prep.py` **注释**——**一字未动**（注释非执行面）。

### A-4 · 逐件指纹（改前 → 改后）

| 件 | 标签 | 改前 SHA-12 | **改后 SHA-12** | 改前 bytes | **改后 bytes** | Δ |
|---|---|---|---|---|---|---|
| `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | H4 | `0ccd739d026e` | **`cd4f1e7b4879`** | 18,988 | **19,003** | +15 |
| `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | H5 | `90b5bb66dadb` | **`8ae074194a3d`** | 52,745 | **52,785** | +40 |
| `_v3_recheck_05_executor_2026_09_28.py` | H3 | `a7267d1cad80` | **`65f8a7514f34`** | 38,709 | **38,733** | +24 |

**全 SHA-256（改后，实测）**

| 件 | SHA-256 |
|---|---|
| H4 | `cd4f1e7b4879ad121db80a45154ca6bc9ef05719948f09a8b75cd988559cc1ba` |
| H5 | `8ae074194a3d0b70de435866e85436eb1a4d93c988a6bcd0a7cbfa44e613e722` |
| H3 | `65f8a7514f349831306db02b5d95a591c5118bd4a9df0384552a0feaa6ec222d` |

**「0 其余改动」之实证（逐行差分，非抽样）**：以改前快照对改后件作**逐行全量差分**——

| 件 | 正文行数 前 → 后 | 实际变动行 | 差分判定 |
|---|---|---|---|
| H4 | 441 → 441 | **3**（L112／L118／L140） | **除 §A 所载外 0 行变动** |
| H5 | 842 → 842 | **4**（L161／L167／L186／L314） | **除 §A 所载外 0 行变动** |
| H3 | 736 → 736 | **2**（L117／L735） | **除 §A 所载外 0 行变动** |

**编码／语法**：改后 3 件实测 **BOM ＝ 无、CR ＝ 0、TAB ＝ 0、CTRL ＝ 0**；`ast.parse` **3/3 OK**。H5 **末行仍无换行符**（`ends_nl=False`，与原件一致，⛔ 0 擅加）。

---

## §B D9 收束口径之**分列**声明（PI 裁「分列」）

| # | 收束项 | 本棒呈报 |
|---|---|---|
| **①** | **29 行路径改写** | **已毕** —— 经独立复核件 `732cfae29bbc` 实测：指纹 5/5、可达 24/24、逆替换 5/5 精确复现旧指纹、覆盖 25/25、最小性成立。**本棒复核属实，且 ⛔ 0 触及该 29 行之一字**（本棒 9 行与该 29 行**无交集**，H1／H2 亦 0 变动）。 |
| **②** | **runner 可运行性** | **另立一项跟踪**，**⛔ 不随 ① 之已毕而归零**。**本棒修态**：P-1 ✅ 修毕（6 行）｜P-2 ✅ 修毕（2 行）｜P-3 ✅ 修毕（1 行）——**均为静态修毕**（⛔ 0 执行 runner，端到端可运行性**未验**）。**残余**：H2 `r1_files` 21 件（sub 侧 21/21 缺失）**仍在断**（不在本棒 3 件授权内）｜H3 `SRC_ANCHOR_FALLBACK` 恒 `False`（P-4）｜H4／H5 之域计数 21 之门柱**⛔ 0 触碰**。 |

> 📌 **为何分列不可合并**：① 之成立系以「24 条常量已指向存在新址」为据（复核件 §2.2 实测）；② 之成立须以「runner 端到端可运行」为据。二者**不同一物**——合并即以 ① 冒充 ②。故本件**分列呈报，⛔ 0 代裁**。

---

## §C 残余与未决（⛔ 0 自作主张处置）

| # | 残余／未决 | 实测状态 | 归属 |
|---|---|---|---|
| C-1 | **H2 `r1_files`**（`_s5doubleprime_five_lines_runner_2026_10_11.py` L141 `fp = RESULTS / fname`） | 21 个文件名在 `SUB\results` **21/21 缺失**、在 `REPO\results` **0 缺失** ⇒ 指向 sub 将致 `FileNotFoundError` | **H2 不在本棒授权 3 件内** ⇒ ⛔ 0 编辑；**候 PI**（复核件 U-5「随 P-1 口径一并裁」，PI 本轮所裁 P-1 限于 H4／H5） |
| C-2 | **H3 `SRC_ANCHOR_FALLBACK`**（L62） | 4 候选址（repo／repo_backup／sub／sub_backup 之 `_archive_deposon_2026_09_17`）**皆 `False`**；本棒改后**仍指向 `REPO`（sub）**，状态**与改前同** | **P-4** · 底本明示「⛔ 0 臆造新址」⇒ ⛔ 0 改写，**候 PI** |
| C-3 | **`d6ff7e9b4bd6` §2.4 载「`DOMAIN_REGISTERED` **24** 条」** | 复核件实测 **21** 条，**差 3** | **U-7** · ⛔ 0 回改 v2，**候 PI／勘正** |
| C-4 | **底本 `c3167a531e0e` CJK 损坏** | 实测 0 非 ASCII 字节、4,631 字面 `?` | **U-6** · 属底本面非回写面，**候 PI** |
| C-5 | **H4 L60／H5 L73 之 `RESULTS` 定义行** | 改后二定义行**已无调用点**（全件 `RESULTS` 仅余定义行） | **无功能后果**（⛔ 0 删行）· 留痕备查 |
| C-6 | **H5 L833／L834 `os.path.relpath(OUT_*, REPO)`** | 以 `REPO`（sub）为基准打印相对路径，**不抛错**，输出形态为 `..\deposon-repo\…` | **未断链** · ⛔ 0 改（非断链面，超最小改动） |
| C-7 | **H5 L317 注释提及「`.tmp/prep.py`」** | 注释文字，⛔ 0 执行 | **非执行面** · ⛔ 0 改 |

> ✅ **P-1／P-2／P-3 三处补修状态：全部修毕**（静态口径）。⛔ **0 执行任何 runner**，故**端到端可运行性未验**——此归 §B ② 跟踪项，**⛔ 0 宣告归零**。

---

## §D 对 `Z-1` ／ `Z-4` 之影响 ＋ 输入链实测指纹表 ＋ 0 回改声明

### D-1 · 0 宣告声明

> ⛔ **0 宣告** D9 已收束／已闭／①毕；⛔ **0 宣告** `Z-1`／`Z-4` 任何计数**归零**；⛔ 0 宣告 runner 可运行性成立（⛔ 0 执行 runner，无端到端凭据）。
>
> 本件所载**全部为读数**（静态指纹／差分／路径求值），**非判定**；**判定归 PI**。§B 之分列**仅呈报**，⛔ 0 代裁。

### D-2 · 对 `Z-1` ／ `Z-4` 之影响面（如实登记，⛔ 0 代裁其计数）

| 面 | 本棒实测之影响 |
|---|---|
| **`Z-1`** | 本棒**未测** `Z-1` 之定义与盘面（⛔ 不在派工单射程）。就 D9 状态：**① 29 行改写**不受影响（本棒 0 触及之）；**② runner 可运行性**——H3／H4／H5 之 3 类断链**已静态修毕**，**H2 `r1_files` 仍断** ⇒ 若 `Z-1` 计数含「runner 可运行件数」，则**仍非 5/5**。⛔ **0 代其计数**。 |
| **`Z-4`** | 本棒**未测** `Z-4` 之定义与盘面。本棒仅登记：本件**不产出任何可致 `Z-4` 归零之凭据**；`Z-4` 状态**本棒 0 触碰**。 |

### D-3 · 输入链实测指纹表（本棒独立实测，⛔ 0 沿用）

| 件 | 在册 SHA-12 | **本棒实测 SHA-12** | bytes | 判定 |
|---|---|---|---|---|
| `_d9_independent_review_2026_10_12.md` | `732cfae29bbc` | **`732cfae29bbc`** | 22,644 | **MATCH** |
| `_d9_rewrite_execution_register_2026_10_12.md` | `0ea7852c4511` | **`0ea7852c4511`** | 20,432 | **MATCH** |

**既有宿主指纹（复核件 §1.2 所载，本棒实测确认 0 漂移）**

| 件 | 标签 | 本棒实测 SHA-12／bytes | 复核件 §1.2 所载 | 判定 |
|---|---|---|---|---|
| `_s4prime_readings_runner_2026_10_11.py` | H1 | `52bb6e3bba15` ／ 23,870 | `52bb6e3bba15` ／ 23,870 | **MATCH**（本棒**0 编辑**） |
| `_s5doubleprime_five_lines_runner_2026_10_11.py` | H2 | `57f5a4c5d5cd` ／ 31,227 | `57f5a4c5d5cd` ／ 31,227 | **MATCH**（本棒**0 编辑**） |

### D-4 · 0 回改声明

- ⛔ **0 回改任何 markdown 既有件一字**——含独立复核件 `732cfae29bbc`、执行登记 `0ea7852c4511`、底本 `c3167a531e0e`、v2 `d6ff7e9b4bd6`、勘误 `7395034a09aa`、回写映射 `ff0a25dc2720`、越界项 `0ec673877e14`。
- ⛔ **0 编辑** H1／H2 及其余任何 `.py`；**唯一编辑对象 ＝ H3／H4／H5 之 9 行**（§A 逐行留痕，逐行差分实证 0 溢出）。
- ⛔ **0 移动／0 重命名／0 删除**任何件；⛔ **0 触** `D:\私人资料\_non_upload_local_archive`（**0 读 0 写 0 列目录**）；临时脚本与快照仅落 `%TEMP%`，**未入仓**。
- ⛔ 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT；⛔ **0 改终判词／阈值／门柱／判死线**（`len(files) != 21`、`sys.exit(2)` 皆未触碰）；⛔ 0 赋 `k_v3s_4_4_*` 布尔；⛔ **0 执行任何 runner**；⛔ 0 宣告①毕。
- ⛔ 0 写他棒产物名域（`_d9_independent_review*`／`_d9_rewrite_execution_register*`／`_g1_*`／`_g2_*`／`_n2_*`／`letters/`／`_bob_*`／`_remote_baseline*`／`_archive_2026-10-12`）。

---

## 附录 A · 本登记件指纹

| 项 | 值 |
|---|---|
| 路径 | `results/_d9_residual_repair_register_2026_10_12.md` |
| SHA-12 | **见交付回报**（落盘后字节级自测） |
| bytes | **见交付回报** |
| BOM／CR／TAB／CTRL | **无 ／ 0 ／ 0 ／ 0** · UTF-8 无 BOM · 纯 LF |
| nonAscii | **> 0**（断言成立） |
| U+FFFD | **0**（断言成立） |

## 附录 B · 落盘前检查（本件）

- 落盘前 `Test-Path`：**False**
- 落盘前 glob 命中（`results/_d9_residual_repair*`）：**0**
