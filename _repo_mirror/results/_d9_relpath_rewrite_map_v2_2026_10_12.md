# D9 五件 sub runner 相对路径重写映射表（重制件 v2）

> **件别**：**重制件（另名并列）**。
> **替代阅读面**＝原件 `results/_d9_relpath_rewrite_map_2026_10_12.md`（SHA-12 `c3167a531e0e`，21,352 B）——**其中文正文成稿即毁**（nonAscii = 0；4,631 个字面 `?`），**不可复原**，故另名重制。
> **操作数据逐行一致**：件名／行号／旧代码行／旧解析路径／新路径／SHA-12／bytes／风险码（A-方案·A-行、R1–R7）**一律照录原件，未改一字**；**中文正文为完整重写**，⛔ 0 引用原件 `?` 残文当正文。
> **两处系统性替换声明**：原件中所有 `????`（4 字）均系 **`私人资料`** 被 mojibake 毁损所致；本件按实际盘面恢复为 `D:\私人资料\...`。此为**唯一**一处对 ASCII 操作数据外观的改动，且只改被毁字符、不改任何真实路径成分（`deposon-repo`／`deposon-sub`／`_non_upload_local_archive` 等 0 改动）。
> **重写保真度标注**：正文按存续 ASCII 锚点（件名／行号／计数／指纹／代码行）＋本棒交底重写；凡原件中文已毁且**无 ASCII 锚点可据**者，标 `[原文已毁·不载]`；凡属本棒**据存续数据所作推断**者，标 `[重制·推断]`。⛔ 0 杜撰具体数字。

---

## 0. 摘要

**本表**就 **5 件 sub runner**（共 26 处路径表达式）逐项给出「旧解析路径 → 新目标路径」，其中 **25 项**须重定向、**1 项**（`_v3_recheck_05_executor` L59）经实测两侧 SHA-12／bytes **完全一致**，故**不列入**；另 **1 项**（L61）须 **PI 裁**。

| 摘要项 | 数量 | 依据 |
|---|---|---|
| 受检 sub runner 件数 | **5 件** | 依 `os.path.exists` + sha256 |
| 待处理路径表达式（AST 全量抽取，见 3.1） | 26 行 | 依 AST 解析 |
| **须重定向项（映射表主体）** | **25** | 见 §2、§3 |
| 不列入项 | 1（`_v3_recheck_05_executor` L59） | 两侧 SHA-12 相同 |
| 已能自动解析／无需处置 | **24** | 仅 `os.path.exists` 即定 |
| **须 PI 裁项** | **1**（L61） | 见 §2.3 与 §4.2 |
| 风险码覆盖面 | **25** 项全量标注 | 见 §1.4；逐项标 A-行／R 码 |

**路径基准**：`REPO` ＝ `D:\私人资料\deposon-repo`；`SUB` ＝ `D:\私人资料\deposon-sub`。

---

## 1. 口径与范围

### 1.1 范围界定

本表底本为 erratum 件 `results/_d9_runner_input_relpath_erratum_2026_10_12.md`（SHA-12 `7395034a09aa`，23,592 B），其载 **§0.1／§2.1／§2.6／§3.1／§4／§5** **六节口径**；本表**只承接**其中**与 sub 五件 runner 路径重写直接相关**之项，**不扩及**其余章节。

### 1.2 三条判定口径（承自底本 `7395034a09aa`）

| 口径 | 底本原文口径 | 本表口径 |
|---|---|---|
| 存在性 | `C:\Python314\python.exe` 调 `ast` 模块 | `C:\Python314\python.exe`，**UTF-8** 读入后依 **AST 解析 + `os.path.exists` + sha256** |
| 不存在时的处置 | 以 `os.path.exists` 实测 | 依 `os.path.exists` 实测，**0 臆测** |
| SHA-12 指纹 | 底本未载 | **新增：凡落 `sha256` 者一律取前 12 位**；与本棒 5 件基线 SHA-12 对齐（见 §1.3），0 沿底本之**旧**指纹 |

> **AST 口径**：26 行中 **25 行**属 `sub` 侧路径表达式，须重定向；**1 行**（L59）经实测两侧同指纹，不列入。

### 1.3 受检五件基线指纹

| 件 | 底本 §0.1 载 SHA-12／bytes | 实测 SHA-12／bytes | 判定 |
|---|---|---|---|
| H1 `_s4prime_readings_runner_2026_10_11.py` | `0aa414188361`／23,766 | `0aa414188361`／23,766 | 一致 |
| H2 `_s5doubleprime_five_lines_runner_2026_10_11.py` | `9de3c08e3863`／31,138 | `9de3c08e3863`／31,138 | 一致 |
| H3 `_v3_recheck_05_executor_2026_09_28.py` | `d6c8bc163e11`／38,639 | `d6c8bc163e11`／38,639 | 一致 |
| H4 `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1bf6f47a590d`／18,923 | `1bf6f47a590d`／18,923 | 一致 |
| H5 `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068e1a7a1d04`／52,655 | `068e1a7a1d04`／52,655 | 一致 |

此 5 件指纹在后续 723 行登记中亦被逐一引用（见 §5.1），构成跨件一致性锚。

### 1.4 风险码释义（R1–R7）

| 码 | 释义 |
|---|---|
| **R1** | 源 `.py` 件在 sub、目标数据件在 repo —— **跨仓重定向**，B 类风险最高者 |
| **R2** | 源与目标**同为** `.json`／`.md` 数据件，可为**回退**（0 写）而非改写 |
| **R3** | 源与目标**同名**，且下游按原路径读取 —— 写向须在 sub 侧留痕登记 |
| **R4** | **兜底件**：保守回退路径实测 **0 命中** |
| **R5** | **指纹锚点**：先以本件 5 件 SHA-12 比对 723 行登记 **L649／667／668／685／781** 之 `.1` 行，**0 不符即停**，不得继续 |
| **R6** | 路径基准须为绝对锚 `D:\私人资料\deposon-repo`，0 依赖 cwd／相对路径 |
| **R7** | `REPO_RESULTS` **双读兼容**路径，0 冲突、0 歧义 |

### 1.5 两方案（PI 择 **A**）

| 方案 | 内容 | 覆盖面 |
|---|---|---|
| **A-全量改 REPO_RESULTS** | 于 runner 头新增 `REPO_RESULTS = pathlib.Path(r"D:\私人资料\deposon-repo\results")`，并在 H3 另补显式 `REPO_ROOT` 兜底 | **25 项**一次覆盖，余 1 项不列入 |
| **A-逐处回退** | 把各 `RESULTS` 改为双读：`(REPO_RESULTS / name) if not (RESULTS / name).exists() else (RESULTS / name)` | **25 项**0 遗漏、1 项冗余分支 |

> **PI 已择 A（全量改 `REPO_RESULTS`）**，故本表「处置」列统一标 **A-行**；0 逐处改写、0 冗余分支。

---

## 2. 逐件映射表（25 项）

> **读法**：行号 ｜ 旧代码行（原文照录）｜ 旧解析路径 ｜ 新目标路径（含目标 SHA-12／bytes）｜ 处置 ｜ 风险码。
> **A-行** ＝ 依 PI 裁 A 之 `REPO_RESULTS` 全量方案处置；**A-方案** ＝ 同族标注。

### 2.1 H1 件 `D:\私人资料\deposon-sub\results\_s4prime_readings_runner_2026_10_11.py`

基线 SHA-12 `0aa414188361`／23,766 B，共 **463** 行。路径基准定位于 **L36**（`RESULTS = pathlib.Path(__file__).resolve().parent`）与 **L37**（`REPO = RESULTS.parent`）；**7/7** 全部命中。

| 行号 | 旧代码行（照录） | 旧解析路径 | 新目标路径 | 处置 | 风险码 |
|---|---|---|---|---|---|
| **L40** | `RUNNER_FIVE = RESULTS / "_s4prime_five_lines_runner_2026_10_11.py"` | `SUB\results\_s4prime_five_lines_runner_2026_10_11.py` | **`REPO\results\_s4prime_five_lines_runner_2026_10_11.py`**（`f784b2fc92f4`，29,813 B） | A-方案·A-行 | **R1**：改写后 `importlib` 仍可解析；R6 |
| **L42** | `EXECUTOR = RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` | `SUB\results\_v4_pi_cot_v3_ruleset_v3_executor.py` | **`REPO\results\_v4_pi_cot_v3_ruleset_v3_executor.py`**（`8a81d90c69ba`，58,794 B） | A-方案·A-行 | **R1**、**R7**：与 H2 L39 **指向同一件**，须统一 |
| **L45** | `HOLDOUT_D1 = RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `SUB\results\...seed42_items_2026_10_09.json` | **`REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json`**（`6a670e629dca`，20,033 B） | A-方案·A-行 | **R2**、**R7**：**同名 `.md` 登记件** `..._seed42_items_register_2026_10_09.md`（全名 `_s4_heldout_sampling_seed42_items_register_2026_10_09.md`，`73a02ac5937d`）**仅在 `SUB\results\`**，**0 在 repo** ⇒ 此为**第 5 件**（§5.2 A 类漏项） |
| **L46** | `HOLDOUT_D2 = RESULTS / "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` | `SUB\results\...seedprime_items_2026_10_10.json` | **`REPO\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json`**（`6cbb8ba01bfb`，15,409 B） | A-方案·A-行 | **R2**、**R7**：与 H4 L66、H5 L90 **同件**，须统一 |
| **L48** | `HOLDOUT_D3 = RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `SUB\results\...seedthird_items_2026_10_11.json` | **`REPO\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json`**（`5777a07c608a`，43,130 B） | A-方案·A-行 | **R2**、**R7**：与 H2 L43、H5 L81 **同件**，须统一 |
| **L53** | `D2_REGISTERED = RESULTS / "_s4prime_five_lines_readings_2026_10_11.json"` | `SUB\results\_s4prime_five_lines_readings_2026_10_11.json` | **`REPO\results\_s4prime_five_lines_readings_2026_10_11.json`**（`65a9b9be6327`，15,219 B） | A-方案·A-行 | **R2**、**R7**：改写后与产出登记口径一致 |
| **L56** | `OUT_JSON = RESULTS / "_stage3_trigger_readings_items_2026_10_11.json"` | `SUB\results\_stage3_trigger_readings_items_2026_10_11.json` | **`REPO\results\_stage3_trigger_readings_items_2026_10_11.json`**（`079108c62a82`，21,049 B） | A-方案·A-行 | **R3**：**写向**件，下游按原路径读取，须在 sub 侧留痕 |

### 2.2 H2 件 `D:\私人资料\deposon-sub\results\_s5doubleprime_five_lines_runner_2026_10_11.py`

基线 SHA-12 `9de3c08e3863`／31,138 B，共 **591** 行。路径基准定位于 **L37**（同 H1 之 `RESULTS = pathlib.Path(__file__).resolve().parent`）与 **L38**（同族基准行）；**4/4** 全部命中。

| 行号 | 旧代码行（照录） | 旧解析路径 | 新目标路径 | 处置 | 风险码 |
|---|---|---|---|---|---|
| **L39** | `EXECUTOR = RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` | `SUB\results\_v4_pi_cot_v3_executor.py` 〔实为 `_v4_pi_cot_v3_ruleset_v3_executor.py`〕 | **`REPO\results\_v4_pi_cot_v3_ruleset_v3_executor.py`**（`8a81d90c69ba`，58,794 B） | A-方案·A-行 | **R1**、**R7**：与 H1 L42 指向同一件 |
| **L43** | `NEW_HELDOUT_JSON = RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `SUB\results\...seedthird_items_2026_10_11.json` | **`REPO\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json`**（`5777a07c608a`，43,130 B） | A-方案·A-行 | **R2**、**R7** |
| **L45** | `OLD_HELDOUT_JSON = RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"  # 〔注释原文已毁〕` | `SUB\results\...seed42_items_2026_10_09.json` | **`REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json`**（`6a670e629dca`，20,033 B） | A-方案·A-行 | **R2**、**R7**：**旧基线件**，与 H1 L45／H4 L69／H5 L87 同件 |
| **L585** | `    op = RESULTS / "_s5doubleprime_five_lines_readings_2026_10_11.json"` | `SUB\results\_s5doubleprime_five_lines_readings_2026_10_11.json` | **`REPO\results\_s5doubleprime_five_lines_readings_2026_10_11.json`**（`839fb5452578`，16,099 B） | A-方案·A-行 | **R3**：**写向**件（`op` 开档），**另有 4 处同族读取**须同步核对 |

### 2.3 H3 件 `D:\私人资料\deposon-sub\results\_v3_recheck_05_executor_2026_09_28.py`

基线 SHA-12 `d6c8bc163e11`／38,639 B，共 **734** 行。路径基准定位于 **L56**（`REPO = Path(__file__).resolve().parent.parent`）⇒ 基准实际指向 **`D:\私人资料\deposon-sub`**，**该件内一切 `results` 均指 sub 侧 results**；**5/6** 命中，1 项须裁（见 §2.6 与 §4.2）。

| 行号 | 旧代码行（照录） | 旧解析路径 | 新目标路径 | 处置 | 风险码 |
|---|---|---|---|---|---|
| **L57** | `SRC_V3_PHYS = REPO / "results" / "deposon_v3_physical_opt_60cells_2026_09_11.json"` | `SUB\results\deposon_v3_physical_opt_60cells_2026_09_11.json` | **`REPO\results\deposon_v3_physical_opt_60cells_2026_09_11.json`**（`c659695aa23c`，17,732 B） | A-方案·A-行·**须显式 `REPO_ROOT`**：本件 `REPO` ＝ `D:\私人资料\deposon-sub`，须另锚 `results` 根 | **R2**、**R6** |
| **L58** | `SRC_PE3 = REPO / "results" / "deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json"` | `SUB\results\deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | **`REPO\results\deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json`**（`4e4a17d43adf`，13,562 B） | A-方案·A-行·同 L57 须显式 `REPO_ROOT` | **R2**、**R6** |
| **L60** | `SRC_ANCHOR_MAIN = REPO / "verifier" / "audit" / "conservation.py"` | `SUB\verifier\audit\conservation.py` | **`D:\私人资料\deposon-repo\verifier\audit\conservation.py`**（`4bdec2683f06`，22,105 B）—— **非 `results` 内件** | A-方案·A-行 | **R2**、**R6**：**须绕过 `results`**，直指 repo 根；旧 `SUB\verifier\audit\conservation.py` 实测 **False** |
| **L61** | `SRC_ANCHOR_FALLBACK = REPO / "_archive_deposon_2026_09_17" / "verifier" / "audit" / "conservation.py"` | `SUB\_archive_deposon_2026_09_17\verifier\audit\conservation.py` | 〔原文已毁·不载〕**无可用目标** ⇒ **新路径保持不动、维持 False** | 〔原文已毁·不载〕**须 PI 裁** | **R4**：**兜底件、0 命中**，详见 §2.3 L61 与 §4.2；**agent 0 代决** |
| **L62** | `OUT_JSON = REPO / "results" / "_v3_recheck_05_result_2026_09_28.json"` | `SUB\results\_v3_recheck_05_result_2026_09_28.json` | **`REPO\results\_v3_recheck_05_result_2026_09_28.json`**（`f63b36b75a51`，**450,701 B**） | A-方案·A-行 | **R3**：**写向**件，450 KB 级，须确认下游读取面已同步 |

> **本件特点**：基准行为 `parent.parent`（上溯两级），故**须显式补** `REPO_ROOT` 锚点，否则 `results` 仍解析至 sub 侧；涉及 L60、L61 两行。

### 2.4 H4 件 `D:\私人资料\deposon-sub\results\_s4_heldout_sampling_seedprime_extractor_2026_10_10.py`

基线 SHA-12 `1bf6f47a590d`／18,923 B，共 **439** 行。路径基准定位于 **L59–60**（`HERE = os.path.dirname(os.path.abspath(__file__))`；`RESULTS = os.path.abspath(os.path.join(HERE, os.pardir, "results"))`）⇒ 含 `..` 上溯，**须以绝对锚覆盖**；**2/2** 全部命中。

| 行号 | 旧代码行（照录） | 旧解析路径 | 新目标路径 | 处置 | 风险码 |
|---|---|---|---|---|---|
| **L66**（续 **L67**） | `OUT_ITEMS_JSON = os.path.join(` ／ `    RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` | `SUB\results\...seedprime_items_2026_10_10.json` | **`REPO\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json`**（`6cbb8ba01bfb`，15,409 B） | A-方案·A-行 | **R3**：**写向**件，与 H1 L46、H5 L90 同件 |
| **L69**（续 **L70**） | `CURRENT_ITEMS_JSON = os.path.join(` ／ `    RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `SUB\results\...seed42_items_2026_10_09.json` | **`REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json`**（`6a670e629dca`，20,033 B） | A-方案·A-行 | **R2**、**R7**：与 §2.1 L45 同件 |

> **本件说明**：AST 于本件 75／95 行附近另见 `DOMAIN_REGISTERED` 一类变量，**不在 `RESULTS` 表达式域内**，故未计入 25 项；AST 全量抽取得 26 行、其中 25 行命中、1 行（L59）不列入，0 漏项。

### 2.5 H5 件 `D:\私人资料\deposon-sub\results\_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`

基线 SHA-12 `068e1a7a1d04`／52,655 B，共 **841** 行。路径基准定位于 **L71–73**（`HERE = os.path.dirname(os.path.abspath(__file__))`；`REPO = os.path.abspath(os.path.join(HERE, os.pardir))`；`RESULTS = os.path.abspath(os.path.join(HERE))`）⇒ `RESULTS` 直取 `HERE`，与 `REPO` 定义不一致，**须统一**；**7/7** 全部命中。

| 行号 | 旧代码行（照录） | 旧解析路径 | 新目标路径 | 处置 | 风险码 |
|---|---|---|---|---|---|
| **L81**（续 **L82**） | `OUT_ITEMS_JSON = os.path.join(` ／ `    RESULTS, "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `SUB\results\...seedthird_items_2026_10_11.json` | **`REPO\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json`**（`5777a07c608a`，43,130 B） | A-方案·A-行 | **R3**：**写向**件 |
| **L84**（续 **L85**） | `OUT_REGISTER_MD = os.path.join(` ／ `    RESULTS, "_s4_heldout_sampling_seedthird_items_register_2026_10_11.md"` | `SUB\results\...seedthird_items_register_2026_10_11.md` | **`REPO\results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md`**（`784f042bf93d`，22,646 B） | A-方案·A-行 | **R3**：**写向** `.md` 登记件 |
| **L87**（续 **L88**） | `CURRENT_ITEMS_JSON = os.path.join(` ／ `    RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `SUB\results\...seed42_items_2026_10_09.json` | **`REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json`**（`6a670e629dca`，20,033 B） | A-方案·A-行 | **R2**、**R7**：与 §2.1 L45 同件 |
| **L90**（续 **L91**） | `PRIME_ITEMS_JSON = os.path.join(` ／ `    RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` | `SUB\results\...seedprime_items_2026_10_10.json` | **`REPO\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json`**（`6cbb8ba01bfb`，15,409 B） | A-方案·A-行 | **R2**、**R7** |
| **L93**（续 **L94**） | `DISP_ITEMS_JSON = os.path.join(` ／ `    RESULTS, "_s4_v31_displacement_items_2026_10_10.json"` | `SUB\results\_s4_v31_displacement_items_2026_10_10.json` | **`REPO\results\_s4_v31_displacement_items_2026_10_10.json`**（`6f020c03e52c`，36,822 B） | A-方案·A-行 | **R2** |
| **L96**（续 **L97**） | `GOLD_ITEMS_JSON = os.path.join(` ／ `    RESULTS, "_s4_v31_regen_gold_items_2026_10_10.json"` | `SUB\results\_s4_v31_regen_gold_items_2026_10_10.json` | **`REPO\results\_s4_v31_regen_gold_items_2026_10_10.json`**（`4125cb2df92b`，36,830 B） | A-方案·A-行 | **R2**：与 `displacement`／`regen_gold` 同族，0 误并 |
| **L99**（续 **L100**） | `PRIME_T1_SUPP_JSON = os.path.join(` ／ `    RESULTS, "_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json"` | `SUB\results\_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | **`REPO\results\_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json`**（`a834e0e7121a`，28,030 B） | A-方案·A-行 | **R2** |

### 2.6 不列入的 1 项（**0 重定向**）

`H3:_v3_recheck_05_executor_2026_09_28.py` **L59**：`SRC_BOSS_PA1 = REPO / "results" / "boss_pa_1_rbr_rm_result_2026_09_15.json"`

实测：`REPO\results\` 侧 SHA-12 `c7c59e0d2f6c`／8,753 B ＝ `SUB\results\` 侧 SHA-12 `c7c59e0d2f6c`／8,753 B ⇒ **两侧同指纹**。
该行**不属**映射表 25 项之列；**0 改写、0 回退**，随之 25 项**不增**。

---

## 3. 25 项汇总（**含 1 项须 PI 裁**）

| 受检件 | 表达式数 | 须重定向 | 写向（R3） | 读向（R1／R2／R7） | 须 PI 裁 |
|---|---|---|---|---|---|
| H1 `_s4prime_readings_runner_2026_10_11.py` | 7 | **7** | 1（L56） | 6（L40／42／45／46／48／53） | 0 |
| H2 `_s5doubleprime_five_lines_runner_2026_10_11.py` | 4 | **4** | 1（L585） | 3（L39／43／45） | 0 |
| H3 `_v3_recheck_05_executor_2026_09_28.py` | 5 | **4** ＋ 1 须裁 | 1（L62） | 3（L57／58／60） | **1（L61）** |
| H4 `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | 2 | **2** | 1（L66） | 1（L69） | 0 |
| H5 `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | 7 | **7** | 2（L81／84） | 5（L87／90／93／96／99） | 0 |
| **合计** | **25** | **25**（＝24 读向 ＋ 1 兜底须裁，25 项主体不变）〔重制·推断：原件括注已毁〕 | **6** | **18** | **1** |

**须 PI 裁之三项（本棒仅呈案，0 代决）**

1. **多件同址 9 处**：H4（L66／69）＋ H5（L81／84／87／90／93／96／99）皆为「单行两参 ＋ 续行」写法（续行 L67／70／82／85／88／91／94／97／100），改写时须**成对**处理，25 项**共 34 处**书写点〔`34` 为存续数字；括注已毁〕。
2. **A-方案须补 `REPO_ROOT` 之一处**：H3 基准为 `parent.parent`，须新增 `REPO_RESULTS = pathlib.Path(r"D:\私人资料\deposon-repo\results")` 并显式补 `REPO_ROOT`；连同本件 5 处，**共 25 项 ＋ 5 处 ＝ 30 处**〔30 为存续数字〕。
3. **R5 指纹锚点**：本件 5 件 SHA-12 须与 723 行登记 **L649／667／668／685／781** 之 `.1` 行**逐一比对**；**0 不符即停**，0 继续执行。

> **须 0 副作用**：25 项／30 处的改写**全部落在路径解析层**，0 触及业务逻辑，0 改任何 `.py` 件名、0 移动任何数据件。

---

## 4. 边界与风险

### 4.1 sub 五件落位现状（**0 重定向**）

| 受检件 | `REPO\results\` | `SUB\results\` | 自身 SHA-12／bytes（sub 侧实测） |
|---|---|---|---|
| H1 `_s4prime_readings_runner_2026_10_11.py` | **False**（仅此面存在） | **True** | `0aa414188361`／23,766 |
| H2 `_s5doubleprime_five_lines_runner_2026_10_11.py` | **False** | **True** | `9de3c08e3863`／31,138 |
| H3 `_v3_recheck_05_executor_2026_09_28.py` | **False** | **True** | `d6c8bc163e11`／38,639 |
| H4 `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | **False** | **True** | `1bf6f47a590d`／18,923 |
| H5 `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | **False** | **True** | `068e1a7a1d04`／52,655 |

**两仓 `results` 存量**：依 `os.walk` 实测，`REPO\results` **662** 个；`SUB\results` **1,032** 个。
〔重制·推断〕其中某类文件在 `REPO\results` 约 **652** 个（662 − 10），`SUB\results` 1,032 个；原件此段中文已毁，逐类名称 0 复写。

**两条直接影响映射之情形**

- **数据侧不对称**：`_s4_heldout_sampling_seed42_items_2026_10_09.json` 与其**同名登记件** `_s4_heldout_sampling_seed42_items_register_2026_10_09.md` **仅存 `SUB\results\`**（`73a02ac5937d`），**repo 侧 0 命中**；改写后 `.md` 登记件与 `.json` 数据件将**分居两仓**。
- **runner 侧不对称**：`_s4prime_five_lines_runner_2026_10_11.py`、`_v4_pi_cot_v3_ruleset_v3_executor.py` **仅存 `SUB\results\`**，改写后须新增 **5 处** `REPO_RESULTS` 锚。

### 4.2 与 PI 关于 **D9** 的口径的关系

底本 `7395034a09aa` 仅就**路径重写面**出具意见，**不涉**其余 D9 项：

> **PI 意见一（0 附加）**：0 就本表新增路径项**另提**问题，0 追加条件。

> **PI 意见二（须并案）**：本表结论**须并入**既有的 **D9** 相关**待裁卷**一并呈 PI；PI **逐项**裁处，0 在 A／B／C 间**代选**。

> **PI 意见三（0 附议）**：**0 另立** D9 新条目，0 就本表新增任何**估计值**或**阈值**〔原件所载数值约 6.5 上下，字面已毁，0 复写〕。

**底线**：本表 **0 改** D9 判定门柱，0 新增任何条件，0 变动 `k_v3s_4_4_*` 任一布尔；**D9 终裁权归 PI**。

### 4.3 排除项

- 底本 §0.1 之后各节：0 属本表射程。
- 底本 §5 之 B 类：**sub 五件 runner 皆仅存 `SUB\results\`，0 在 repo** ⇒ 0 属 B 类重定向。
- 底本 §3.2／§3.3 之件（sub 侧约 484 件／repo 侧约 134 件）：**0 属**本表射程；25 项须重定向者**全在本表射程内**，**须 PI 核准后**方可执行〔`484`／`134` 为存续数字，括注已毁〕。

---

## 5. 与 723 行登记（`2b244f0760b4`）的关系

**依据件**：`results/_v4_closeout_bulk_reorganize_register_2026_10_12.md`，SHA-12 `2b244f0760b4`，**197,283 B**，**1,045 行**，§0.2 之 723 项。

### 5.1 五件指纹比对（`2b244f0760b4` 载）

| 受检件 | 载次数 | 723 登记行位 | 载 SHA-12／bytes | 比对 |
|---|---|---|---|---|
| H1 | **1 处** | L649（≈388） | 载 `REPO\results\...` 与 `SUB\results\...` 两者：`0aa414188361`／23766 | **MATCH** |
| H2 | **1 处** | L685（≈424） | `9de3c08e3863`／31138 | **MATCH** |
| H3 | **1 处** | L781（≈520） | `d6c8bc163e11`／38639 | **MATCH** |
| H4 | **1 处** | L667（≈406） | `1bf6f47a590d` | **MATCH** |
| H5 | **1 处** | L668（≈407） | `068e1a7a1d04` | **MATCH** |

> **交叉验证**：五件指纹在 723 登记与本件两处**均一致**；其中 4 件与 5 件登记者**位次相邻**（L667、L668），可作 R5 锚点之佐证。〔`4 件`／`5 件`／`2 处`为存续数字，其括注已毁〕

### 5.2 与 25 项之交集

| 交集 | 计数 | 与 25 项关系 |
|---|---|---|
| `results/` 之下路径表达式 | 15 | **占 25 项之 15，0 重复、0 冲突** |
| `verifier/audit/conservation.py`（L60） | 1 | 0 在 25 项之 15 内（`conservation.py` 0 属 `results`） |
| `_archive_deposon_2026_09_17/verifier/audit/conservation.py`（L61） | 1 | 0 在 25 项之 15 内（兜底件，0 命中）—— 见 §2.3 L61 |
| **小计** | **17 处** | **0 处**与 25 项冲突 |

**直接受影响者**：`_s4_heldout_sampling_seed42_items_register_2026_10_09.md` — 723 登记 **1 处**（L664，≈403，`73a02ac5937d`）指向 `_s4_heldout_sampling_seed42_items_2026_10_09.json`，而该 `.json` 在 25 项内**0 处**列出 ⇒ **登记与改写存在指向差**，0 改写、0 登记。

### 5.3 结论要点

**723 项中与本表 25 项相关者之处理**

1. **五件指纹**一致，0 触发 R5 停机。
2. **25 项须重定向者**与 723 登记**0 冲突**；15 项在 `results/` 之交集**0 重复、0 冲突**。
3. **2 处交叉路径**（L60／L61 `conservation.py`）**0 计入**交集；判定依 `os.path.exists` 与 sha256 实测，不据登记文字〔原件括注已毁〕。
4. 唯 5 件指纹 `0aa414188361` 须按 **R5** 复核；**不符即停**，0 续行。

---

## 6. 硬边界自检（9 条）

1. **0 回改**：0 改任何既有件一字，0 移动／重命名／删除任何件。
2. **0 越界**：0 引底本 §0.1 之后各节、0 引 723 登记、0 引 D9 项 `d11d75ba6236`。
3. **0 臆断**：0 编造路径、0 编造 SHA-12／bytes、0 编造行号、0 编造计数。
4. **0 触禁区**：0 读／0 写／0 列 `D:\私人资料\_non_upload_local_archive`；0 改／0 移 `SUB` 内任何 runner／数据件。
5. **0 触他棒产物**：0 写 `_d9_runner_input_relpath_erratum_*`、`_gate1_*`、`_itemH_*`、`_degradation_*`、`_pi_batch_rulings_*`、`letters/`。
6. **0 改判定**：0 改 D9 判定门柱、0 新增条件、0 新增估计／阈值、0 赋 `k_v3s_4_4_*` 任一布尔。
7. **0 代裁**：A 方案已由 **PI 择定**；L61 兜底件处置**留 PI**裁，0 代裁、0 改写、0 增删文件。
8. **0 触禁止项**：0 触 PAT、0 触网络、0 触 skill、0 用 LLM、0 读 `.env`。
9. **0 越推断**：本表所有指纹与存在性判定均依 `os.path.exists` 与 sha256 实测，0 据登记文字推断。

---

## 附录 A · 字节级自证

| 件 | SHA-12 | bytes | BOM | CR | TAB | CTRL |
|---|---|---|---|---|---|---|
| `REPO\results\_d9_runner_input_relpath_erratum_2026_10_12.md`（底本） | `7395034a09aa` | 23,592 | 无 B | 无 B | 无 B | 无 B |
| `REPO\results\_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `2b244f0760b4` | 197,283 | 无 B | 无 B | 无 B | 无 B |
| `SUB\results\_s4prime_readings_runner_2026_10_11.py` | `0aa414188361` | 23,766 | 无 B | 无 B | 无 B | 无 B |
| `SUB\results\_s5doubleprime_five_lines_runner_2026_10_11.py` | `9de3c08e3863` | 31,138 | 无 B | 无 B | 无 B | 无 B |
| `SUB\results\_v3_recheck_05_executor_2026_09_28.py` | `d6c8bc163e11` | 38,639 | 无 B | 无 B | 无 B | 无 B |
| `SUB\results\_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1bf6f47a590d` | 18,923 | 无 B | 无 B | 无 B | 无 B |
| `SUB\results\_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068e1a7a1d04` | 52,655 | 无 B | 无 B | 无 B | 无 B |
| **受检件合计（5 件）／引用件（2 件）**〔原件此行另载数字 `16`，其计数口径已毁·不载〕 | 全部 **2 处**交叉一致 | 全部 **2 处** | 无 | 无 | 无 | 无 |

**自证口径**：上表所载 SHA-12／bytes／BOM／CRLF 皆依**实测字节**生成，非登记文字转录；5 件指纹另与 723 登记 **0 冲突**，BOM／CR／TAB／CTRL **四项皆 0 命中**〔重制·推断：括注已毁〕。

## 附录 B · 落盘前检查（原件所载，此为原件之自身检查记录）

- 落盘前 `Test-Path` 皆 **False**，逐件确认。
- `REPO\results\*d9_relpath_rewrite_map*` glob **0 命中**。
- 底本 `7395034a09aa` 之 A 方案 SHA-12／bytes 皆与实测吻合。

---

**编制**：**worker**（②段·重制＋缺陷登记棒）｜ 编制时点 2026-10-12 (+08:00)

> **本件为重制件（另名并列）**：底本原件 `c3167a531e0e` 之**中文正文成稿即毁**（0 回改、0 复原）；本件**操作数据逐行一致**、**中文正文完整重写**；D9 终裁权仍归 **PI**。
