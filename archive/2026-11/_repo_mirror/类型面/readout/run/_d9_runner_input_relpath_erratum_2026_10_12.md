# D9 · sub 面 runner「输入悬空」· 路径勘误与相对引用回写面

> **状态栏**：📌 **D9 之处置面（勘误面·仅登记）** —— 本件系 D9（Trae 走读所报高 severity 缺陷）之**处置面**：实测定位 + 逐处断链判定 + 处置建议。
>
> ⛔ **0 以「已勘误」充「已收束」**：本件 0 执行任何回改／补置／改基准；**D9 仍为未收束（挂账）**，收束归 PI。
>
> **执行体**：worker（执行面）｜**执行时点**：2026-10-12 (+08:00)
>
> **前置**：⛔ 0 回改／0 移动／0 重命名／0 删除任何既有件｜⛔ 0 触及 `〔归档区〕`｜⛔ 0 经手 PAT／0 远端写｜⛔ 0 网络／0 skill／0 LLM／0 读 `.env`｜⛔ 0 宣告任何闭/开

---

## 0. 一句话结论

**实测结论（以盘上实测为准，不强行对齐 Trae 之数）**：sub 面以 `__file__` 派生基准定位输入之活代码共 **5 件**（Trae 所报 3 件 ＋ 本棒全量扫描增列 2 件 extractor），共 **26 条**可执行路径常量，其中 **25 条断链**、**1 条未断链**；25 条断链中 **24 条**之输入/输出件现址**仅存于 `deposon-repo\results`**（Trae「输入件全部留在 repo\results」获实测确认），余 1 条两区皆缺。

### 0.1 5 件清单（附断链判定）

| # | 件名（`deposon-sub\results\`） | SHA-12 | bytes | `__file__` 基准行 | 可执行路径常量 | 断链 | **断链判定** |
|---|---|---|---|---|---|---|---|
| 1 | `_s4prime_readings_runner_2026_10_11.py` | `0aa414188361` | 23,766 | L36 | 7 | 7 | **断链（全断）** |
| 2 | `_s5doubleprime_five_lines_runner_2026_10_11.py` | `9de3c08e3863` | 31,138 | L37 | 4 | 4 | **断链（全断）** |
| 3 | `_v3_recheck_05_executor_2026_09_28.py` | `d6c8bc163e11` | 38,639 | L56 | 6 | 5 | **断链（5/6，1 条未断）** |
| 4 | `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1bf6f47a590d` | 18,923 | L59 | 2 | 2 | **断链（全断）** |
| 5 | `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068e1a7a1d04` | 52,655 | L71 | 7 | 7 | **断链（全断）** |
| — | **合计** | — | — | — | **26** | **25** | — |

**未断链 1 条**：`_v3_recheck_05_executor_2026_09_28.py:59` `SRC_BOSS_PA1` → `boss_pa_1_rbr_rm_result_2026_09_15.json`，该件**两区各存一份且 SHA-12 一致**（`c7c59e0d2f6c` · 8,753 B）⇒ 未断链。

### 0.2 与 Trae 所报之差（如实登记，不强行对齐）

| 项 | Trae 所报 | 本棒实测 | 差因（如实登记） |
|---|---|---|---|
| 件数 | **3 件** | **5 件** | Trae 之 3 件应为 #1/#2/#3（文件名含 `runner`/`executor`）；#4/#5 为 `extractor`，同用 `__file__` 派生基准（`os.path.dirname(os.path.abspath(__file__))`），属同一断链族，本棒据 R-8 扫描增列 |
| 「`.pyc` 归档面证明原在 repo 运行」 | 作为证据 | **盘上 0 命中** | 两区 `*.pyc` 与 `__pycache__` 目录实测均 0 件 ⇒ 该证据在盘上**不可复核**；本件 0 采信、0 否定，原运行地改由**其他独立证据**支持（见 §2.0） |

---

## 1. D9 原文照录 · 成因 · 规程依据

### 1.1 D9 登记原文（逐字照录）

> 出处：`letters/_oct_full_coverage_reply_trae_code_2026_10_12.md`（SHA-12 `d11d75ba6236` · 23,978 B）之 **§1.G** 第 **103** 行。
>
> 「- **D9（高）**：sub 面 3 件 runner **输入悬空**（移 723 件后 `__file__` 相对路径指向的输入件全部留在 repo\results；`.pyc` 归档面证明原在 repo 运行）——按新址执行即 FileNotFoundError。」

### 1.2 R-8 规程原文（逐字照录 · 本棒沿之执行）

> 同件第 **162** 行：「**R-8** | **迁移评估纳入相对引用扫描**：Move-Item / 改名 / 归档前，除 CodeRefs 外还须扫 **md/py 内相对路径引用面**；迁移后对高引用件出「路径勘误」并回写引用面（当前仅出映射表不回改 = 系统性断链敞口：D9 三 runner 输入悬空实证） | 迁移前后相对引用扫描 diff = 0 断链 | 三/四 |」

### 1.3 成因（沿派工单所载 ＋ 本棒实测补强）

📌 **③段-① 之跨区转移（723 件）未设「迁移后相对引用扫描/回写」** ⇒ 系统性断链敞口。

本棒实测补强（3 条，均为盘上事实）：

1. 723 迁移登记 §2 自陈**转移件「CodeRefs ＝ 0」**——即迁移时按「0 件被活代码引用」放行；**但实测 5 件活代码确以 `__file__` 相对路径引用了未随迁的输入件** ⇒ 该判据**漏检相对路径引用面**（CodeRefs 按「活代码按文件名引用被移件」立判，**不含**「活代码引用未随迁件」之反向情形）。
2. 5 件源件**确在** 723 映射表内（已登记旧→新），而其 **24 个输入/输出件 0 登记** ⇒ **迁移只带走了引用者，没带走被引用者**。
3. 723 登记 §1 已记「600 件被在册活代码按绝对路径钉住，移动即断链」⇒ **同一断链机理在同一次整理中已被识别并用于 600 件**，惟其识别口径（绝对路径）**未覆盖相对路径**，致本 5 件漏网。

---

## 2. 5 件 runner 之逐件实测（含行号）

### 2.0 判读方法与仪器（自陈，防仪器误差同案登记）

- **仪器**：`〔本地路径已脱敏〕` ＋ `ast` 模块解析（**非**正则行匹配）——判定「可执行路径常量」＝ 由 `__file__` 派生之目录变量（或硬编码绝对路径）为根、经 `/` 或 `os.path.join` 拼接且末段为 `.json/.py/.md` 之**赋值表达式**；⛔ 散文提及、注释、字符串清单**不计**。
- **口径**：实测某路径常量时，先按 AST 求值出绝对期望路径，再 `os.path.exists` 实测；「现址」另以同构相对路径在 `deposon-repo` 侧复核。
- **独立仪器交叉验证**：723 映射表第 649 行记 `_s4prime_readings_runner_2026_10_11.py` = `0aa414188361` / 23,766 B；与本棒独立实测**逐位一致** ⇒ 两仪器读数一致。

### 2.1 `_s4prime_readings_runner_2026_10_11.py`（SHA-12 `0aa414188361` · 23,766 B）

**基准表达式（照录 L36）**：`RESULTS = pathlib.Path(__file__).resolve().parent`　（另 L37 `REPO = RESULTS.parent`）

| 行号 | 变量名 | 引用表达式（照录） | 期望路径（按新址求值） | 现址 | 断链判定 |
|---|---|---|---|---|---|
| L40 | `RUNNER_FIVE` | `RESULTS / "_s4prime_five_lines_runner_2026_10_11.py"` | `sub\results\_s4prime_five_lines_runner_2026_10_11.py` | `repo\results\` | **断链** |
| L42 | `EXECUTOR` | `RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` | `sub\results\_v4_pi_cot_v3_ruleset_v3_executor.py` | `repo\results\` | **断链** |
| L45 | `HOLDOUT_D1` | `RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `sub\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | `repo\results\` | **断链** |
| L46 | `HOLDOUT_D2` | `RESULTS / "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` | `sub\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `repo\results\` | **断链** |
| L48 | `HOLDOUT_D3` | `RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `sub\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `repo\results\` | **断链** |
| L53 | `D2_REGISTERED` | `RESULTS / "_s4prime_five_lines_readings_2026_10_11.json"` | `sub\results\_s4prime_five_lines_readings_2026_10_11.json` | `repo\results\` | **断链** |
| L56 | `OUT_JSON` | `RESULTS / "_stage3_trigger_readings_items_2026_10_11.json"` | `sub\results\_stage3_trigger_readings_items_2026_10_11.json` | `repo\results\` | **断链（输出侧）** |

> **注**：L56 为**输出**侧（写盘目标），亦随相对基准漂移；L40/L42 为**活代码输入**（`importlib` 只读加载）。

### 2.2 `_s5doubleprime_five_lines_runner_2026_10_11.py`（SHA-12 `9de3c08e3863` · 31,138 B）

**基准表达式（照录 L37）**：`RESULTS = pathlib.Path(__file__).resolve().parent`　（另 L38 `REPO = RESULTS.parent`）

| 行号 | 变量名 | 引用表达式（照录） | 期望路径（按新址求值） | 现址 | 断链判定 |
|---|---|---|---|---|---|
| L39 | `EXECUTOR` | `RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` | `sub\results\_v4_pi_cot_v3_ruleset_v3_executor.py` | `repo\results\` | **断链** |
| L43 | `NEW_HELDOUT_JSON` | `RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `sub\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `repo\results\` | **断链** |
| L45 | `OLD_HELDOUT_JSON` | `RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `sub\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | `repo\results\` | **断链** |
| L585 | `op` | `op = RESULTS / "_s5doubleprime_five_lines_readings_2026_10_11.json"` | `sub\results\_s5doubleprime_five_lines_readings_2026_10_11.json` | `repo\results\` | **断链（输出侧）** |

### 2.3 `_v3_recheck_05_executor_2026_09_28.py`（SHA-12 `d6c8bc163e11` · 38,639 B）

**基准表达式（照录 L56）**：`REPO = Path(__file__).resolve().parent.parent`　⇒ 原在 `repo\results` 时 `REPO` ＝ `repo`；现址求值得 `REPO` ＝ **`deposon-sub`**（**根位移，非 results 内位移**）

| 行号 | 变量名 | 引用表达式（照录） | 期望路径（按新址求值） | 现址 | 断链判定 |
|---|---|---|---|---|---|
| L57 | `SRC_V3_PHYS` | `REPO / "results" / "deposon_v3_physical_opt_60cells_2026_09_11.json"` | `sub\results\deposon_v3_physical_opt_60cells_2026_09_11.json` | `repo\results\` | **断链** |
| L58 | `SRC_PE3` | `REPO / "results" / "deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json"` | `sub\results\deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | `repo\results\` | **断链** |
| L59 | `SRC_BOSS_PA1` | `REPO / "results" / "boss_pa_1_rbr_rm_result_2026_09_15.json"` | `sub\results\boss_pa_1_rbr_rm_result_2026_09_15.json` | **两区各存一份，SHA-12 一致**（`c7c59e0d2f6c` · 8,753 B） | **未断链** |
| L60 | `SRC_ANCHOR_MAIN` | `REPO / "verifier" / "audit" / "conservation.py"` | `sub\verifier\audit\conservation.py` | `repo\verifier\audit\conservation.py`（**非 results 层**） | **断链** |
| L61 | `SRC_ANCHOR_FALLBACK` | `REPO / "_archive_deposon_2026_09_17" / "verifier" / "audit" / "conservation.py"` | `sub\_archive_deposon_2026_09_17\verifier\audit\conservation.py` | **repo 侧等价址亦不存在** | **断链（两区皆缺）** |
| L62 | `OUT_JSON` | `REPO / "results" / "_v3_recheck_05_result_2026_09_28.json"` | `sub\results\_v3_recheck_05_result_2026_09_28.json` | `repo\results\` | **断链（输出侧）** |

> ⚠ **本件是 5 件中受损最重者**：其基准 `parent.parent` 指向**仓根**而非 `results`，故断链面**溢出 `results` 层**（L60/L61 落到 `verifier/` 与 `_archive_deposon_2026_09_17/`）。L61 之 fallback 目标在 **repo 侧亦已不存在** ⇒ 该 fallback 分支**在迁移前即可能已失效**，非迁移所致（如实登记，不归因迁移）。

### 2.4 `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py`（SHA-12 `1bf6f47a590d` · 18,923 B）〔本棒增列〕

**基准表达式（照录 L59–60）**：`HERE = os.path.dirname(os.path.abspath(__file__))` ／ `RESULTS = os.path.abspath(os.path.join(HERE, os.pardir, "results"))`

> **注**：此式经 `..` 回卷，**恒等于「自身所在目录」**（`results/../results` ≡ `results`）⇒ 该式**位置无关**，迁移前后求值同解；断链纯由「输入件未随迁」造成，非基准漂移。

| 行号 | 变量名 | 引用表达式（照录） | 期望路径（按新址求值） | 现址 | 断链判定 |
|---|---|---|---|---|---|
| L66 | `OUT_ITEMS_JSON` | `os.path.join(RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json")` | `sub\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `repo\results\` | **断链（输出侧）** |
| L69 | `CURRENT_ITEMS_JSON` | `os.path.join(RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json")` | `sub\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | `repo\results\` | **断链（输入）** |

> ⚠ 本件另有 **24 条**字面文件名（`_r_pair_addendum_2026_10_09.json` 等，行 75–95）位于 `DOMAIN_REGISTERED` 清单元组内，经运行时逐件拼接读取；本棒 AST 口径**不计元组内裸字面**，故本表仅列 2 条赋值型常量。此 24 件**同为 repo 侧现址**（实测见 §3 层 1 附注）⇒ 实际断链面**大于本表**，须于回写时一并纳入（归后续棒）。

### 2.5 `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`（SHA-12 `068e1a7a1d04` · 52,655 B）〔本棒增列〕

**基准表达式（照录 L71–73）**：`HERE = os.path.dirname(os.path.abspath(__file__))` ／ `REPO = os.path.abspath(os.path.join(HERE, os.pardir))` ／ `RESULTS = os.path.abspath(os.path.join(HERE))`

| 行号 | 变量名 | 引用表达式（照录） | 期望路径（按新址求值） | 现址 | 断链判定 |
|---|---|---|---|---|---|
| L81 | `OUT_ITEMS_JSON` | `os.path.join(RESULTS, "_s4_heldout_sampling_seedthird_items_2026_10_11.json")` | `sub\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | `repo\results\` | **断链（输出侧）** |
| L84 | `OUT_REGISTER_MD` | `os.path.join(RESULTS, "_s4_heldout_sampling_seedthird_items_register_2026_10_11.md")` | `sub\results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | `repo\results\` | **断链（输出侧）** |
| L87 | `CURRENT_ITEMS_JSON` | `os.path.join(RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json")` | `sub\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | `repo\results\` | **断链（输入）** |
| L90 | `PRIME_ITEMS_JSON` | `os.path.join(RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json")` | `sub\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | `repo\results\` | **断链（输入）** |
| L93 | `DISP_ITEMS_JSON` | `os.path.join(RESULTS, "_s4_v31_displacement_items_2026_10_10.json")` | `sub\results\_s4_v31_displacement_items_2026_10_10.json` | `repo\results\` | **断链（输入）** |
| L96 | `GOLD_ITEMS_JSON` | `os.path.join(RESULTS, "_s4_v31_regen_gold_items_2026_10_10.json")` | `sub\results\_s4_v31_regen_gold_items_2026_10_10.json` | `repo\results\` | **断链（输入）** |
| L99 | `PRIME_T1_SUPP_JSON` | `os.path.join(RESULTS, "_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json")` | `sub\results\_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | `repo\results\` | **断链（输入）** |

### 2.6 反向排除：`_q3_c1c4_l282_transposition_fix_executor_2026_10_09.py` —— **非 D9 受害件**

该件虽在 `sub\results` 且同在 723 映射表内，但 **L95 为硬编码绝对路径**（照录）：

> `REPO_ROOT = r"〔本地路径已脱敏〕"`

⇒ 其全部路径常量求值后**恒指 repo 原址**，迁移**不影响** ⇒ **不断链**。如实登记，以避免把「迁移断链」与「硬编码免疫」混为一族。

---

## 3. 全量相对引用扫描结果（沿 R-8 · 两层口径）

### 3.1 层 1 · 可执行面（py · `__file__` 派生）—— `deposon-sub\results`

| 指标 | 实测值 |
|---|---|
| `sub\results` 文件总数（递归） | 1,032 |
| 含 `__file__` 之 py 件 | 11 |
| 其中**有可执行路径常量**者 | **5** |
| 可执行路径常量总条数 | **26** |
| **断链条数** | **25** |
| 未断链条数 | 1（`_v3_recheck_05_executor:59`） |
| 断链引用之目标「仅存于 repo\results」者 | **24** |
| 目标于 repo 侧亦缺（两区皆断）者 | 1（`_v3_recheck_05_executor:61`） |
| 目标存于 repo 但**非 results 层**者 | 1（`_v3_recheck_05_executor:60` → `repo\verifier\audit\conservation.py`） |

> **附注（AST 口径之已知边界，如实登记）**：`_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` 行 75–95 之 `DOMAIN_REGISTERED` 清单含 **24 条**裸文件名元组（运行时经 `RESULTS` 拼接读取，**全部现址在 repo\results**），AST 口径不计元组内裸字面 ⇒ **层 1 断链面 25 条系下界**，实际 ≥ 49 条。此边界须于回写时纳入（归后续棒）。

### 3.2 层 2 · 文档引用面（md · `results/<件名>` 相对引用）—— `deposon-sub\results`

| 指标 | 实测值 |
|---|---|
| `sub\results` 之 md 件总数 | 708 |
| 含 `results/<件名>` 相对引用之 md 件 | 645 |
| 其中引用目标**仅存于 repo**（跨区指向）之 md 件 | **484** |
| 件名全集：sub | 1,029 |
| 件名全集：repo | 641 |
| 两区**同名皆有** | 45 |
| **仅存于 repo** | 596 |

> **判读边界（重要，防误判）**：层 2 之 `results/<件名>` 在 md 中多为**文档引证**（指向 repo 路径的引文），**非可执行路径**；且无法据字面判定其应解析至 repo 抑或 sub（取决于原约定）。故本层**只报命中件数，不报「断链件数」**——其是否构成断链**须 PI 先裁「引证路径基准」**，方能判定（如实登记为**未判定**，⛔ 0 冒充已判）。

### 3.3 反向扫描 —— `deposon-repo\results`

| 指标 | 实测值 |
|---|---|
| `repo\results` 文件总数（递归） | 652 |
| 扫描之 md/py 件 | 351 |
| `results/<件名>` 字面引用总处数 | 9,158 |
| 引用目标**仅存于 sub**（即已迁走）之 md/py 件 | **134** |
| 「仅存于 sub」之件名总数 | 984 |

> 命中面示例（跨区指向已迁件最多者）：`_achievements_inventory_full_2026_10_09.md`（809）、`_forgotten_recovery_register_2026_10_08.md`（8）、`_d1_backfill_intake_verdict_2026_10_01.md`（5）、`_chd_construction_domain_declaration_draft_2026_10_10.md`（4）、`_c1c4_input_gap_fill_plan_2026_10_09.md`（3）。
>
> ⛔ **本层 0 判定为断链**——与层 2 同因：引证基准未裁 ⇒ **只报命中，不报断链**（归后续棒／PI 裁）。

---

## 4. 与 723 条映射之核对

**核对对象**：`results/_v4_closeout_bulk_reorganize_register_2026_10_12.md`（SHA-12 `2b244f0760b4` · 197,283 B）

| 类别 | 件 | 723 映射表内命中 | 判定 |
|---|---|---|---|
| **引用者**（5 件源件） | `_s4prime_readings_runner_2026_10_11.py` 等 5 件 | 各 **2 处**（含旧→新映射行） | **已登记、已迁移** |
| **被引用者**（24 个输入/输出件） | `_v4_pi_cot_v3_ruleset_v3_executor.py`、`_s4_heldout_sampling_seed42_items_2026_10_09.json` 等 | **0 处** | **未登记、未迁移** |

**结论：「输入件未被迁」（非「已随迁」）。**

**独立读数交叉验证**：映射表第 649 行记 `_s4prime_readings_runner_2026_10_11.py` = `0aa414188361` / 23,766 B / `MATCH`；本棒独立实测 SHA-12 与 bytes **逐位一致** ⇒ 5 件迁移后字节**未在 sub 侧发生漂移**，断链系**纯粹的位置/引用面问题**，非内容损坏。

> ⚠ **同时登记一项登记面事实**：映射表中 `_s4_heldout_sampling_seed42_items_register_2026_10_09.md`（第 664 行，序号 403）**已迁移**；而 #4/#5 两 extractor 于 L69/L87/L90 所需之 `_s4_heldout_sampling_seed42_items_2026_10_09.json`（**`items`** ＝数据件，非 `items_register` ＝登记件）**0 登记**。二者**同名族、易混**，回写时须逐名核，⛔ 0 误补。

---

## 5. 处置建议（**建议 ≠ 执行** · 归 PI／后续棒）

| # | 建议 | 依据 | 本棒处置 |
|---|---|---|---|
| **建议 A** | **出「路径勘误件」逐处列旧→新映射供回写**：将 5 件之相对基准改为**显式绝对路径**（沿 723 登记 §1 已述「600 件被在册活代码按绝对路径钉住」之**同一处置模式**），或将其回写为 repo 侧绝对址 | 该模式在**同一次整理**中已被采用并成功避免 600 件断链；D9 之相对路径面属**同一机理之未覆盖面** | ⛔ 0 执行 |
| **建议 B** | **于 sub 面补置所需输入件**（24 件） | ⚠ **本棒建议不采**：① 其中含 `_v4_pi_cot_v3_ruleset_v3_executor.py` 等**活代码**，补置将造成双份可执行副本；② 盘上已有 `boss_pa_1_rbr_rm_result_2026_09_15.json` **两区同名字份**先例，补置将扩大之；③ 与 PI「两区件数拉平」之令（723 登记 §1）相悖 | ⛔ 0 执行 |
| **建议 C** | **改 runner 之相对基准**（仅 5 行，每件 1 处基准行） | 改动面**最小**（5 件 × 1 行 = 5 行），且可一处覆盖该件全部 26 条常量；但须**同步** SHA-12 登记与 verifier 判定键（沿 10-08「改键」纪律，0 只改一半） | ⛔ 0 执行 |
| **建议 D** | **请 PI 裁两项**：① Trae「`.pyc` 归档面」证据盘上 0 命中，是否改写 D9 登记字面；② §3.2／§3.3 文档引证层之**路径基准**未裁（sub 侧 484 件／repo 侧 134 件命中），故**只报命中不报断链** | 两歧义均须 PI 裁，agent 侧 0 代裁 | ⛔ 0 追问、0 代立 |

> ⚠ **建议之效力边界**：以上**仅建议**。⛔ 本棒 0 执行 A/B/C 之任一；⛔ 0 以「已勘误」充「已收束」；**D9 之状态仍为未收束（挂账）**，收束归 PI。

---

## 6. ⛔ 本件 0 作之事项（明示免责）

1. ⛔ **0 回改** 5 件 runner 之任一行（0 改基准／0 补路径／0 改指纹常量）。
2. ⛔ **0 移动／0 重命名／0 删除**任何既有件；本棒于两区**只读**。
3. ⛔ **0 修改** 723 映射表（`2b244f0760b4`）或 D9 原件（`d11d75ba6236`）之任一字节。
4. ⛔ **0 执行**任何路径勘误回写、0 补置输入件、0 新建第二件（临时脚本仅落 `%TEMP%`，用后清理）。
5. ⛔ **0 宣告** D9 已收束／已勘误完成；⛔ 0 宣告任何「闭」或「开」。
6. ⛔ **0 经手 PAT／0 远端写**；⛔ 0 触及 `〔归档区〕`；⛔ 0 网络／0 skill／0 LLM／0 读 `.env`。
7. ⛔ **0 强行对齐** Trae 之数：实测 5 件与所报 3 件之差、`.pyc` 证据 0 命中，均**如实登记**（§0.2）。
8. ⛔ **0 把文档引证层**（§3.2／§3.3）冒充「已判定断链」——基准未裁，只报命中。

---

## 附 · 输入链表（SHA-12／bytes／BOM／CRLF／TAB／CTRL 一律实测）

### 附.1 本棒实测之 5 件（D9 受影响面）

| 件（`deposon-sub\results\`） | SHA-12 | bytes | BOM | CR | TAB | CTRL |
|---|---|---|---|---|---|---|
| `_s4prime_readings_runner_2026_10_11.py` | `0aa414188361` | 23,766 | False | 0 | 0 | 0 |
| `_s5doubleprime_five_lines_runner_2026_10_11.py` | `9de3c08e3863` | 31,138 | False | 0 | 0 | 0 |
| `_v3_recheck_05_executor_2026_09_28.py` | `d6c8bc163e11` | 38,639 | False | 0 | 0 | 0 |
| `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1bf6f47a590d` | 18,923 | False | 0 | 0 | 0 |
| `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068e1a7a1d04` | 52,655 | False | 0 | 0 | 0 |

### 附.2 本棒所读之原件

| 件 | SHA-12 | bytes | BOM | CR | TAB | CTRL |
|---|---|---|---|---|---|---|
| `deposon-repo\letters\_oct_full_coverage_reply_trae_code_2026_10_12.md` | `d11d75ba6236` | 23,978 | False | 0 | 0 | 0 |
| `deposon-repo\results\_v4_closeout_bulk_reorganize_register_2026_10_12.md` | `2b244f0760b4` | 197,283 | False | 0 | 0 | 0 |

### 附.3 落前预检（实测）

- 目标路径 `Test-Path` ＝ **False**
- `repo\results\*d9_runner_input*` glob ＝ **0 命中**；`sub\results\*d9_runner_input*` glob ＝ **0 命中**

---

**落款**：**worker**（执行面）｜2026-10-12 (+08:00)

> 本件系 **D9 之处置面**（勘误面·仅登记）。⛔ 0 回改任何既有件；⛔ 0 执行任何处置建议；⛔ **0 以「已勘误」充「已收束」**——**D9 仍为未收束（挂账）**，收束归 PI。
