# D9 相对路径悬空 · 回写执行登记（A-甲）

> **授权**：PI 卡 `ask_ac388fb8cb83c9f2a6bc85f9` · `d9_fix` 采 **A** · 本轮另裁 **A-甲**＝连带 5 根定义行一齐改，合计 30 行
>
> **本棒权限**：**唯一获准编辑 `.py` 的棒**（仅 5 件）；⛔ 0 移动/重命名/删除任何件；⛔ 0 触 `〔本地归档区〕`
>
> **底本**：`results/_d9_relpath_rewrite_map_2026_10_12.md` · SHA-12 `c3167a531e0e` · 21,352 B · ⛔ 0 回改（逐字回读并作唯一改写依据）
>
> **产出**：本件（执行登记）＋ `results/_seven23_map_revision_register_2026_10_12.md`（修订登记，另立）
>
> **执行**：worker（回写执行棒）· 2026-10-12 (+08:00)

---

## 0. ⚠ 底本完整性异常（须 PI 知悉）

底本 `c3167a531e0e` **实测 `NONASCII_BYTES = 0`、`?` 计数 = 4,631**：其中文正文在**成稿时**即已被替换为字面 `?`（0 个非 ASCII 字节），**非本次读取通道所致**（经 `unicode_escape` ASCII 安全通道复核确认），故**中文叙述不可复原**。

- **仍完整可用者**（＝全部作业数据）：文件名、行号、原行逐字、新址、SHA-12、bytes、风险码（R1–R7）、附录 A 指纹。
- **不可用者**：中文叙述性说明。
- **处置**：⛔ 0 以臆测补中文；本棒仅据 ASCII 作业数据＋PI 令执行；本条如实登记，**是否重制底本 候 PI**。

---

## 1. 落盘前实测复核（⛔ 0 沿用记忆值）

### 1.1 底本复核

| 项 | 实测 | 底本载 | 判定 |
|---|---|---|---|
| SHA-12 | `c3167a531e0e` | `c3167a531e0e` | MATCH |
| bytes | 21,352 | 21,352 | MATCH |
| BOM / CR | 无 / 0 | 无 / 0 | MATCH |

### 1.2 5 件宿主（改前）

| 件 | SHA-12 | bytes | BOM | CR | TAB | 底本 §1.3／附录 A 载 | 判定 |
|---|---|---|---|---|---|---|---|
| H1 `_s4prime_readings_runner_2026_10_11.py` | `0aa414188361` | 23,766 | 无 | 0 | 0 | `0aa414188361` / 23,766 | MATCH |
| H2 `_s5doubleprime_five_lines_runner_2026_10_11.py` | `9de3c08e3863` | 31,138 | 无 | 0 | 0 | `9de3c08e3863` / 31,138 | MATCH |
| H3 `_v3_recheck_05_executor_2026_09_28.py` | `d6c8bc163e11` | 38,639 | 无 | 0 | 0 | `d6c8bc163e11` / 38,639 | MATCH |
| H4 `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | `1bf6f47a590d` | 18,923 | 无 | 0 | 0 | `1bf6f47a590d` / 18,923 | MATCH |
| H5 `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | `068e1a7a1d04` | 52,655 | 无 | 0 | 0 | `068e1a7a1d04` / 52,655 | MATCH |

**5 件均为 UTF-8 无 BOM、纯 LF（CR=0）、无 TAB**；改写全程保持。

### 1.3 24 行新址实测（`os.path.exists` ＋ sha256 ＋ bytes）

| 行 | 新址 | exists | SHA-12 | bytes | 与底本载 |
|---|---|---|---|---|---|
| H1 L40 | `REPO\results\_s4prime_five_lines_runner_2026_10_11.py` | True | `f784b2fc92f4` | 29,813 | MATCH |
| H1 L42 | `REPO\results\_v4_pi_cot_v3_ruleset_v3_executor.py` | True | `8a81d90c69ba` | 58,794 | MATCH |
| H1 L45 | `REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | True | `6a670e629dca` | 20,033 | MATCH |
| H1 L46 | `REPO\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | True | `6cbb8ba01bfb` | 15,409 | MATCH |
| H1 L48 | `REPO\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | True | `5777a07c608a` | 43,130 | MATCH |
| H1 L53 | `REPO\results\_s4prime_five_lines_readings_2026_10_11.json` | True | `65a9b9be6327` | 15,219 | MATCH |
| H1 L56 | `REPO\results\_stage3_trigger_readings_items_2026_10_11.json` | True | `079108c62a82` | 21,049 | MATCH |
| H2 L39 | `REPO\results\_v4_pi_cot_v3_ruleset_v3_executor.py` | True | `8a81d90c69ba` | 58,794 | MATCH |
| H2 L43 | `REPO\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | True | `5777a07c608a` | 43,130 | MATCH |
| H2 L45 | `REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | True | `6a670e629dca` | 20,033 | MATCH |
| H2 L585 | `REPO\results\_s5doubleprime_five_lines_readings_2026_10_11.json` | True | `839fb5452578` | 16,099 | MATCH |
| H3 L57 | `REPO\results\deposon_v3_physical_opt_60cells_2026_09_11.json` | True | `c659695aa23c` | 17,732 | MATCH |
| H3 L58 | `REPO\results\deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json` | True | `4e4a17d43adf` | 13,562 | MATCH |
| H3 L60 | `REPO\verifier\audit\conservation.py` | True | `4bdec2683f06` | 22,105 | MATCH |
| H3 L62 | `REPO\results\_v3_recheck_05_result_2026_09_28.json` | True | `f63b36b75a51` | 450,701 | MATCH |
| H4 L66 | `REPO\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | True | `6cbb8ba01bfb` | 15,409 | MATCH |
| H4 L69 | `REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | True | `6a670e629dca` | 20,033 | MATCH |
| H5 L81 | `REPO\results\_s4_heldout_sampling_seedthird_items_2026_10_11.json` | True | `5777a07c608a` | 43,130 | MATCH |
| H5 L84 | `REPO\results\_s4_heldout_sampling_seedthird_items_register_2026_10_11.md` | True | `784f042bf93d` | 22,646 | MATCH |
| H5 L87 | `REPO\results\_s4_heldout_sampling_seed42_items_2026_10_09.json` | True | `6a670e629dca` | 20,033 | MATCH |
| H5 L90 | `REPO\results\_s4_heldout_sampling_seedprime_items_2026_10_10.json` | True | `6cbb8ba01bfb` | 15,409 | MATCH |
| H5 L93 | `REPO\results\_s4_v31_displacement_items_2026_10_10.json` | True | `6f020c03e52c` | 36,822 | MATCH |
| H5 L96 | `REPO\results\_s4_v31_regen_gold_items_2026_10_10.json` | True | `4125cb2df92b` | 36,830 | MATCH |
| H5 L99 | `REPO\results\_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json` | True | `a834e0e7121a` | 28,030 | MATCH |

**24/24 全部 MATCH，0 不符**。另实测 **24 行旧址（`SUB\results\…`）`exists = False`**，与「悬空」前提一致。
目录名实测 `私人资料` = `U+79C1 U+4EBA U+8D44 U+6599`（4 字），与底本 `〔本机路径〕\????\…` 之 4 字掩码吻合。

### 1.4 跳过行与 0 改动行实测

| 行 | 事项 | 实测 | 处置 |
|---|---|---|---|
| H3 L61 | `SRC_ANCHOR_FALLBACK = REPO / "_archive_deposon_2026_09_17" / "verifier" / "audit" / "conservation.py"` | 4 候选址全 **False**：`REPO\_archive_deposon_2026_09_17\…`、`REPO\_archive_deposon_2026_09_17_backup\…`、`SUB\_archive_deposon_2026_09_17\…`、`SUB\_archive_deposon_2026_09_17_backup\…` | **⛔ 0 改写、0 臆造新址**（底本 §2.3／附录注 7 明示**候 PI**） |
| H3 L59 | `SRC_BOSS_PA1 = REPO / "results" / "boss_pa_1_rbr_rm_result_2026_09_15.json"` | `REPO\results\…` 与 `SUB\results\…` **两区皆 True**，同为 `c7c59e0d2f6c` / 8,753 B | 0 改动（底本 §2.6） |

---

## 2. 执行口径（A-甲）及其逐文件适配

底本 A-甲：`REPO_RESULTS = pathlib.Path(r"_repo_mirror\results")`，H3 另定义 `REPO_ROOT`。

**适配说明（⛔ 0 增删任何 import，故按各件既有 import 体例落笔）**：

| 件 | 既有 import | 定义行（新增 1 根／件） |
|---|---|---|
| H1 | `import pathlib` | `REPO_RESULTS = pathlib.Path(r"_repo_mirror\results")` |
| H2 | `import pathlib` | `REPO_RESULTS = pathlib.Path(r"_repo_mirror\results")` |
| H3 | `from pathlib import Path` | `REPO_ROOT = Path(r"_repo_mirror")` |
| H4 | **无 pathlib**（仅 `os`） | `REPO_RESULTS = r"_repo_mirror\results"`（纯 raw str） |
| H5 | **无 pathlib**（仅 `os`） | `REPO_RESULTS = r"_repo_mirror\results"`（纯 raw str） |

H4/H5 以纯字符串常量承之，语义与 A-甲「显式绝对路径常量」等同，且免增 import；⛔ 0 重定义既有 `RESULTS`／`REPO`（其后续引用一律保持原样，见 §5）。

---

## 3. 逐件逐行 before → after（照录）

> 行号格式：`旧 Lx → 新 Ly`；每件新增定义行 1 根，故其后行号 **+1**。

### 3.1 H1 `_s4prime_readings_runner_2026_10_11.py`（改 7 ＋ 新增 1 ＝ 8 行）

| 行 | BEFORE | AFTER |
|---|---|---|
| 旧 L37 → 新 L37（**不改**） | `REPO = RESULTS.parent` | 同左（0 改动） |
| **新增 新 L38** | — | `REPO_RESULTS = pathlib.Path(r"_repo_mirror\results")` |
| 旧 L40 → 新 L41 | `RUNNER_FIVE = RESULTS / "_s4prime_five_lines_runner_2026_10_11.py"` | `RUNNER_FIVE = REPO_RESULTS / "_s4prime_five_lines_runner_2026_10_11.py"` |
| 旧 L42 → 新 L43 | `EXECUTOR = RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` | `EXECUTOR = REPO_RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` |
| 旧 L45 → 新 L46 | `HOLDOUT_D1 = RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `HOLDOUT_D1 = REPO_RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"` |
| 旧 L46 → 新 L47 | `HOLDOUT_D2 = RESULTS / "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` | `HOLDOUT_D2 = REPO_RESULTS / "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` |
| 旧 L48 → 新 L49 | `HOLDOUT_D3 = RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `HOLDOUT_D3 = REPO_RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` |
| 旧 L53 → 新 L54 | `D2_REGISTERED = RESULTS / "_s4prime_five_lines_readings_2026_10_11.json"` | `D2_REGISTERED = REPO_RESULTS / "_s4prime_five_lines_readings_2026_10_11.json"` |
| 旧 L56 → 新 L57 | `OUT_JSON = RESULTS / "_stage3_trigger_readings_items_2026_10_11.json"` | `OUT_JSON = REPO_RESULTS / "_stage3_trigger_readings_items_2026_10_11.json"` |

### 3.2 H2 `_s5doubleprime_five_lines_runner_2026_10_11.py`（改 4 ＋ 新增 1 ＝ 5 行）

| 行 | BEFORE | AFTER |
|---|---|---|
| 旧 L38 → 新 L38（**不改**） | `REPO = RESULTS.parent` | 同左（0 改动） |
| **新增 新 L39** | — | `REPO_RESULTS = pathlib.Path(r"_repo_mirror\results")` |
| 旧 L39 → 新 L40 | `EXECUTOR = RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` | `EXECUTOR = REPO_RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py"` |
| 旧 L43 → 新 L44 | `NEW_HELDOUT_JSON = RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `NEW_HELDOUT_JSON = REPO_RESULTS / "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` |
| 旧 L45 → 新 L46 | `OLD_HELDOUT_JSON = RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"  # 仅供管道同源自证` | `OLD_HELDOUT_JSON = REPO_RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json"  # 仅供管道同源自证`（**行尾注释逐字保留**） |
| 旧 L585 → 新 L586 | `    op = RESULTS / "_s5doubleprime_five_lines_readings_2026_10_11.json"` | `    op = REPO_RESULTS / "_s5doubleprime_five_lines_readings_2026_10_11.json"`（函数体内，**4 空格缩进保留**） |
| 旧 L140（**不改**） | `        fp = RESULTS / fname` | 同左（0 改动，非 25 行之一，见 §5） |

### 3.3 H3 `_v3_recheck_05_executor_2026_09_28.py`（改 4 ＋ 新增 1 ＝ 5 行；**跳过 1**）

| 行 | BEFORE | AFTER |
|---|---|---|
| 旧 L56 → 新 L56（**不改**） | `REPO = Path(__file__).resolve().parent.parent` | 同左（0 改动） |
| **新增 新 L57** | — | `REPO_ROOT = Path(r"_repo_mirror")` |
| 旧 L57 → 新 L58 | `SRC_V3_PHYS = REPO / "results" / "deposon_v3_physical_opt_60cells_2026_09_11.json"` | `SRC_V3_PHYS = REPO_ROOT / "results" / "deposon_v3_physical_opt_60cells_2026_09_11.json"` |
| 旧 L58 → 新 L59 | `SRC_PE3 = REPO / "results" / "deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json"` | `SRC_PE3 = REPO_ROOT / "results" / "deposon_boss_pe_3_reservoir_verify_9m60c_2026_09_15.json"` |
| 旧 L59 → 新 L60（**0 改动**） | `SRC_BOSS_PA1 = REPO / "results" / "boss_pa_1_rbr_rm_result_2026_09_15.json"` | 同左（底本 §2.6：两区同 SHA 同 bytes） |
| 旧 L60 → 新 L61 | `SRC_ANCHOR_MAIN = REPO / "verifier" / "audit" / "conservation.py"` | `SRC_ANCHOR_MAIN = REPO_ROOT / "verifier" / "audit" / "conservation.py"` |
| 旧 L61 → 新 L62（**⛔ 跳过**） | `SRC_ANCHOR_FALLBACK = REPO / "_archive_deposon_2026_09_17" / "verifier" / "audit" / "conservation.py"` | **同左，一字未动**（4 候选址皆 False，⛔ 0 臆造新址，**候 PI**） |
| 旧 L62 → 新 L63 | `OUT_JSON = REPO / "results" / "_v3_recheck_05_result_2026_09_28.json"` | `OUT_JSON = REPO_ROOT / "results" / "_v3_recheck_05_result_2026_09_28.json"` |

### 3.4 H4 `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py`（改 2 ＋ 新增 1 ＝ 3 行）

| 行 | BEFORE | AFTER |
|---|---|---|
| 旧 L60 → 新 L60（**不改**） | `RESULTS = os.path.abspath(os.path.join(HERE, os.pardir, "results"))` | 同左（0 改动） |
| **新增 新 L61** | — | `REPO_RESULTS = r"_repo_mirror\results"` |
| 旧 L67 → 新 L68 | `    RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` | `    REPO_RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` |
| 旧 L70 → 新 L71 | `    RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `    REPO_RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"` |

### 3.5 H5 `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`（改 7 ＋ 新增 1 ＝ 8 行）

| 行 | BEFORE | AFTER |
|---|---|---|
| 旧 L73 → 新 L73（**不改**） | `RESULTS = os.path.abspath(os.path.join(HERE))` | 同左（0 改动） |
| **新增 新 L74** | — | `REPO_RESULTS = r"_repo_mirror\results"` |
| 旧 L82 → 新 L83 | `    RESULTS, "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` | `    REPO_RESULTS, "_s4_heldout_sampling_seedthird_items_2026_10_11.json"` |
| 旧 L85 → 新 L86 | `    RESULTS, "_s4_heldout_sampling_seedthird_items_register_2026_10_11.md"` | `    REPO_RESULTS, "_s4_heldout_sampling_seedthird_items_register_2026_10_11.md"` |
| 旧 L88 → 新 L89 | `    RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"` | `    REPO_RESULTS, "_s4_heldout_sampling_seed42_items_2026_10_09.json"` |
| 旧 L91 → 新 L92 | `    RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` | `    REPO_RESULTS, "_s4_heldout_sampling_seedprime_items_2026_10_10.json"` |
| 旧 L94 → 新 L95 | `    RESULTS, "_s4_v31_displacement_items_2026_10_10.json"` | `    REPO_RESULTS, "_s4_v31_displacement_items_2026_10_10.json"` |
| 旧 L97 → 新 L98 | `    RESULTS, "_s4_v31_regen_gold_items_2026_10_10.json"` | `    REPO_RESULTS, "_s4_v31_regen_gold_items_2026_10_10.json"` |
| 旧 L100 → 新 L101 | `    RESULTS, "_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json"` | `    REPO_RESULTS, "_s4_seedprime_seq_t1_only_supplement_items_2026_10_11.json"` |

### 3.6 计数

| 件 | 底本 25 行中之占 | 实改常量行 | 新增定义行 | 合计落笔 |
|---|---|---|---|---|
| H1 | 7 | 7 | 1 | 8 |
| H2 | 4 | 4 | 1 | 5 |
| H3 | 5（含跳过 1） | 4 | 1 | 5 |
| H4 | 2 | 2 | 1 | 3 |
| H5 | 7 | 7 | 1 | 8 |
| **合计** | **25** | **24**（25 − 跳过 1） | **5** | **29** |

**PI 令 30 行** ＝ 25 常量行 ＋ 5 定义行；其中 **1 行（`SRC_ANCHOR_FALLBACK`）依底本明示 0 改写 候 PI**，故**实落笔 29 行**。

---

## 4. 指纹对照（改前 → 改后）

| 件 | SHA-12 前 | SHA-12 后 | bytes 前 | bytes 后 | Δbytes | 正文行数 前 → 后 |
|---|---|---|---|---|---|---|
| H1 | `0aa414188361` | **`52bb6e3bba15`** | 23,766 | **23,870** | +104 | 463 → 464 |
| H2 | `9de3c08e3863` | **`57f5a4c5d5cd`** | 31,138 | **31,227** | +89 | 591 → 592 |
| H3 | `d6c8bc163e11` | **`a7267d1cad80`** | 38,639 | **38,709** | +70 | 734 → 735 |
| H4 | `1bf6f47a590d` | **`0ccd739d026e`** | 18,923 | **18,988** | +65 | 439 → 440 |
| H5 | `068e1a7a1d04` | **`90b5bb66dadb`** | 52,655 | **52,745** | +90 | 840 → 841 |

**全 SHA-256（改后）**

| 件 | SHA-256 |
|---|---|
| H1 | `52bb6e3bba153110af2a836f76e875d5f110eb3c549cccaae78bbe2d9d168953` |
| H2 | `57f5a4c5d5cd2b90cee5b89dc81fd0a462b3d556952f575ae915e1550037b12e` |
| H3 | `a7267d1cad8014f0e0a690cb0c56949528694fe2729ebf61d9b0fea2565b8047` |
| H4 | `0ccd739d026ec6ead69d4170c94d771baff97c5258706f3420a2f54703a86d14` |
| H5 | `90b5bb66dadbf5457665a8d13f033845cb1a3381b968cb724c98fee056ee6a1e` |

---

## 5. 「0 其余改动」之声明与实证

**声明**：5 件除 §3 所载 **29 行** 外，⛔ **0** 非目标行改动、⛔ **0** 格式／换行／编码变更、⛔ **0** import／逻辑变更、⛔ 0 `ruff` 或任何格式化、⛔ 0 移动／重命名／删除、⛔ 0 触他棒产物。

**实证一（逆替换回归）**：对改后各件「删去新增定义行 ＋ 反向替换全部目标行」，重算指纹并与底本载之改前指纹比对——

| 件 | 逆替换后 SHA-12 | 逆替换后 bytes | 底本载 | 判定 |
|---|---|---|---|---|
| H1 | `0aa414188361` | 23,766 | `0aa414188361` / 23,766 | **仅目标行改动** |
| H2 | `9de3c08e3863` | 31,138 | `9de3c08e3863` / 31,138 | **仅目标行改动** |
| H3 | `d6c8bc163e11` | 38,639 | `d6c8bc163e11` / 38,639 | **仅目标行改动** |
| H4 | `1bf6f47a590d` | 18,923 | `1bf6f47a590d` / 18,923 | **仅目标行改动** |
| H5 | `068e1a7a1d04` | 52,655 | `068e1a7a1d04` / 52,655 | **仅目标行改动** |

即：除 §3 明载之 29 行外，**0 字节级差异**。

**实证二（编码／行尾）**：改后 5 件实测 **BOM = 无、CR = 0、TAB = 0、CTRL = 0**，与原件一致（UTF-8 无 BOM、纯 LF）。

**实证三（语法）**：改后 5 件 `ast.parse` **全 OK**（⛔ 0 执行任何 runner，⛔ 0 触网络／PAT／`.env`）。

**实证四（新址可解析）**：以 AST **只求值常量表达式**（⛔ 0 执行模块体），得 **23 行可解析常量**（H2 L586 为函数体内赋值，另行求值）**全部指向存在的新址**：

| 件 | 已解析且 `exists=True` 之常量 |
|---|---|
| H1 | `RUNNER_FIVE`、`EXECUTOR`、`HOLDOUT_D1`、`HOLDOUT_D2`、`HOLDOUT_D3`、`D2_REGISTERED`、`OUT_JSON`（7） |
| H2 | `EXECUTOR`、`NEW_HELDOUT_JSON`、`OLD_HELDOUT_JSON`、函数体 `op`（4） |
| H3 | `SRC_V3_PHYS`、`SRC_PE3`、`SRC_ANCHOR_MAIN`、`OUT_JSON`（4） |
| H4 | `OUT_ITEMS_JSON`、`CURRENT_ITEMS_JSON`（2） |
| H5 | `OUT_ITEMS_JSON`、`OUT_REGISTER_MD`、`CURRENT_ITEMS_JSON`、`PRIME_ITEMS_JSON`、`DISP_ITEMS_JSON`、`GOLD_ITEMS_JSON`、`PRIME_T1_SUPP_JSON`（7） |

---

## 6. 跳过项／异常项／残留面（如实登记，⛔ 0 自行裁定）

| # | 项 | 事实 | 处置 |
|---|---|---|---|
| 1 | **H3 L61 `SRC_ANCHOR_FALLBACK`** | 4 候选址全 False；底本明示 0 改写、⛔ 0 臆造新址 | **0 改动 · 候 PI**（该行仍指向 `SUB\_archive_deposon_2026_09_17\…`＝不存在） |
| 2 | **底本 CJK 损坏** | `c3167a531e0e` 实测 0 非 ASCII 字节、4,631 字面 `?` | 如实登记；中文叙述不可复原，是否重制 **候 PI** |
| 3 | **H3 L60 `SRC_BOSS_PA1`** | 依底本 §2.6 为 0 改动行；两区同 SHA 同 bytes | 0 改动；仍指向 `SUB\results\…`（该文件两区皆存） |
| 4 | **非目标 `RESULTS` 引用残留** | H2 旧 L140 `fp = RESULTS / fname`；H4 旧 L111/117/139；H5 旧 L160/166/185 —— 均仍指向 `SUB\results` | ⛔ 0 越 30 行授权改之；**登记为残留面，候 PI 裁**（H4/H5 之 `os.listdir(RESULTS)` 仍扫 sub 面） |
| 5 | 执行前复核脚本自身笔误 | 首次复核表内 H2 L45 一行因构造文件名笔误报 MISMATCH | **非件异常**：重核该址 `6a670e629dca` / 20,033 B，与底本载一致；24/24 全 MATCH |

---

## 7. 本棒边界（⛔ 0 越权）

- ⛔ 0 回改任何既有 markdown／无关件一字（含底本 `c3167a531e0e`、723 映射表 `2b244f0760b4`、错讹正误件 `7395034a09aa`）。
- ⛔ 0 写入他棒产物名域（`_d9_relpath_rewrite_map_*`／`_d9_runner_input_relpath_erratum_*`／`_gate1_*`／`_itemH_*`／`_degradation_*`／`_pi_batch_rulings_*`／`_trae_issues_*`／`letters/`）。
- ⛔ 0 移动／重命名／删除；⛔ 0 触 `〔本地归档区〕`（0 读 0 写 0 列目录）。
- ⛔ 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT；⛔ 0 改终判词／阈值／门柱；⛔ 0 赋 `k_v3s_4_4_*` 布尔。
- ⛔ **0 执行任何 runner**；⛔ **0 宣告 D9 已闭**——**D9 收束权不在本棒**，回写完成 ＝ 待 PI／他棒复核收束。

---

## 附录 A · 本登记件指纹

| 项 | 值 |
|---|---|
| 路径 | `REPO\results\_d9_rewrite_execution_register_2026_10_12.md` |
| SHA-12 | 见交付回报（本件为新件，落盘后自测） |
| bytes | 见交付回报 |
| BOM / CR / TAB / CTRL | 无 / 0 / 0 / 0 · UTF-8 无 BOM · 纯 LF |

## 附录 B · 落盘前检查（本件与修订登记件）

- 落盘前 `Test-Path`：两件皆 **False**
- 落盘前 glob 命中：**0**