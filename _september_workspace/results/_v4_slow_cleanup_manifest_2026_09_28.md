# V4 慢处置 B｜清理类三件处置记录（evidence-auditor）

- 日期：2026-09-28
- 出件：evidence-auditor（`agent-11335500b168`）
- 派工：Mavis（root session）｜派工单「慢处置 B（evidence-auditor）：清理类三件」
- 场景：worker「数据修订/资产处置」｜铁律先验路由（清理走 mavis-trash 可恢复删除）
- 哈希算法：`Get-FileHash -Algorithm SHA256`，**SHA-12 = hexdigest()[:12] 小写**（禁内建 `hash()`）

---

## §0 结论速览

| # | 处置项 | 派工前提 | 盘上实测 | 动作 | 结果 |
|---|---|---|---|---|---|
| 1 | aggregate v2/v3 | 各 243 B「疑似空壳」 | **243 B 确认空壳**，两件 SHA-12 **同值** `da0044cd24e3` | **mavis-trash 清走 2 件** | ✅ 完成 |
| 1b | aggregate v1 | 标废版登记不删 | 634,458 B / `6f09512818f0` | **0 删 0 改**，登记废版 | ✅ 完成 |
| 1c | aggregate v4 | 权威确认登记 | 2,233,138 B / `66a9b8b3dabf` | **0 触动**，登记权威 | ✅ 完成 |
| 2 | R-4 假 `.txt` | 核验 + 列两案 | 7,568 B / `6effe5ef7ae6`，三项缺陷**全部复现** | **只读核验，0 写入**（仓外部位） | ✅ 完成（呈报两案） |
| 3 | `__pycache__` | 「空目录/残留清走」 | **前提失实**：根目录**非空**，13 `.pyc` / 234,586 B | **清走根目录 1 个**（13 件 `.pyc`），其余 8 目录登记不动 | ✅ 完成（含前提更正） |

**触动数：0 触动 frozen（18/18 PASS，清前清后各跑一次，逐件 MATCH）。**

---

## §1 aggregate v2/v3 清理（清走 2 件）

### §1.1 清前登记（SHA-12 实测）

| 件（repo 相对路径） | 字节 | SHA-12 | 内容判定 |
|---|---|---|---|
| `.tmp/_l14v3_aggregated_10cells_v2.json` | 243 | `da0044cd24e3` | **空壳**：10 键全为 `[]`（`teacher_*` 5 + `distill_*` 5） |
| `.tmp/_l14v3_aggregated_10cells_v3.json` | 243 | `da0044cd24e3` | **空壳**：同上，同哈希 |

**五分支判定 = `SAME_IDENTITY`**：两件 SHA-256 **全等**（`da0044cd24e3…`），系同一空壳的两份副本，**不重复计数**（1 个哈希身份 / 2 份文件）。

> **仪器自审**：派工称「疑似空壳」，本棒**读到字节层**确认——`json.load` 可解析，10 个键值全为空数组，**零 cell 产出**。空壳判定成立，非推测。

### §1.2 清后复验

```
_l14v3_aggregated_10cells.json        EXISTS  634458   6f09512818f0
_l14v3_aggregated_10cells_v2.json     GONE
_l14v3_aggregated_10cells_v3.json     GONE
_l14v3_aggregated_10cells_v4.json     EXISTS  2233138  66a9b8b3dabf
```

- **处置方式**：`mavis-trash` **可恢复删除**（走 runtime 信任启动器 `C:\Users\Administrator\.minimax\bin\mavis-trash.cmd`，非永久删除）。
- **回执原文**：
  ```
  mavis-trash: moved to trash: 'D:/私人资料/deposon-repo/.tmp/_l14v3_aggregated_10cells_v2.json'
  mavis-trash: moved to trash: 'D:/私人资料/deposon-repo/.tmp/_l14v3_aggregated_10cells_v3.json'
  ```
- **下游引用影响核对**：v2/v3 仅被**生成脚本自身**引用（`.tmp/_aggregate_10cells_v2.py:113-117`、`.tmp/_aggregate_10cells_v3.py:66-70` 写入+自算 SHA）+ 5 份**台账/信件文档**引用为清单行（字母表登记，非运行时输入链）。**无运行时下游消费者** ⇒ 清走不破坏输入链。

### §1.3 v1 废版 / v4 权威 登记（0 删 0 改）

| 件 | 字节 | SHA-12 | 登记 | 依据 |
|---|---|---|---|---|
| `.tmp/_l14v3_aggregated_10cells.json`（v1） | 634,458 | `6f09512818f0` | **废版**（**不删**） | PI 拍板 v1 废版 / v4 权威；**被 3 份信件/台账引用**（`_letter_to_pi_upload_*` v6 ledger §2），删件即断引用 |
| `.tmp/_l14v3_aggregated_10cells_v4.json`（v4） | 2,233,138 | `66a9b8b3dabf` | **权威累加面** | R-22/E-45.4 定案；L14V3 verdict §0 **输入链锚定件**（`result.json` §inputs 字面固化） |

> **v1 不删的理由（非本棒裁量）**：PI 口径为「v1 废版**登记**」；且 v1 在盘被信件与 ledger §2 明文引用，**删除会制造幽灵引用**（引用在、件不在）⇒ 保留 + 标废版是唯一自洽处置。**本棒 0 删 0 改 0 改名。**

### §1.4 勘误注记（哈希口径歧义，不改历史行）

`results/_v4_effective_register_2026_09_28.md` **M-7** 行将 v2／v3 记作 `af1b7f09f74d` / `04b127d80bf0`。本棒实测：**该二值 = 生成脚本** `_aggregate_10cells_v2.py`（5,131 B）/ `_aggregate_10cells_v3.py`（2,969 B）的 SHA-12，**非 JSON 输出件**；JSON 输出件两件 SHA-12 **同为 `da0044cd24e3`**（与 M-7 自身引用的 `82e90ff496ae` §C.2/§C.3 口径一致）。

> **判定 = 登记口径歧义（非哈希链断裂、非篡改）**：M-7 同句已写明「v2／v3 JSON 各 243 B 且 SHA 同值 = `da0044cd24e3`」，两处并存系**脚本哈希与产物哈希混列**。
> **处置**：按 R5「frozen 只追加 + 不回改历史行」，本棒**只在本文追加勘误注记**，**不动 M-7 原行**；口径澄清待 PI 处置。

---

## §2 R-4 假 `.txt`（只读核验，0 写入）

### §2.1 位置更正（重要）

派工单给路径 `deposon-sub/results/_test_conv_out.txt`。在 `deposon-repo` 内**扫不到**（`glob **/_test_conv_out.txt` = 0 命中）；实件在**仓外兄弟目录**：

```
D:\私人资料\deposon-sub\results\_test_conv_out.txt
```

⇒ **仓外部位**，按 9 铁律「不擅动 workspace 外」+ R5「仓外目录只读 0 写入」：**本棒只读核验，0 写入、0 改名、0 移动。**

### §2.2 三项缺陷实测复现（逐字节）

| 项 | 派工口径 | 实测 | 判定 |
|---|---|---|---|
| 字节 / SHA-12 | 7,568 B | **7,568 B / `6effe5ef7ae6`** | ✅ 与 V3 勘误链 `6EFFE5EF7AE6` 一致 |
| UTF-8 BOM | 有 | **首 3 字节 `EF BB BF`**（`BOM=True`） | ✅ 复现 ⇒ `json.load` 直读报 `Unexpected UTF-8 BOM` |
| schema 伪装 | `d2b` | 首行 `"schema": "v4_pi_cot_v2_dataset_addendum_d2b/1"` | ✅ 复现：实为 **d2b JSON 却以 `.txt` 命名** |
| 占位自指哈希 | 有 | `aaaaabbbbbb` **在盘命中 = True** | ✅ 复现：`fingerprint_self_hash_after_birth` 为占位值，**第二遍自指哈希未完成** |

**四项全复现（R-4 唯一被逐项复核到字节层的条目）。**

### §2.3 处置建议：两案（**呈报，本棒不擅动副区件**）

**案 A｜改名补正（推荐）**：`.txt` → `.json`（如 `_test_conv_out.d2b.json`），去 BOM，重算并回填 `fingerprint_self_hash_after_birth`。
- **利**：`json.load` 直读可用；命名与内容自洽；占位哈希补全后指纹链闭合。
- **弊**：**需改 1 字节以上**（3 字节 BOM + 12 字符占位值 + 文件名）⇒ **涉内容层改动，超出 evidence-auditor 权限**（我方职责为资产缺陷层登记/引用规范，不代改运行语义）；且被 5 份台账/信件按旧名引用（`_v4_maindir_cleanup_moves_ledger_v6` §22 行 137 曾以 `Move-Item -Force` 动过同名件）⇒ **改名 = 制造幽灵引用**，须同步改全部引用行。

**案 B｜登记不动（保守，当前状态）**：保持 `6effe5ef7ae6` 原样，仅在本 manifest 登记三项缺陷 + 建议。
- **利**：**0 写入**（严守仓外只读）；哈希链不断；5 份既有引用行继续有效。
- **弊**：占位哈希 `aaaaabbbbbb` **持续存在** ⇒ 任何按 `fingerprint_self_hash_after_birth` 做完整性校验的下游会取到假值（**假绿风险**：校验会「通过」而不代表内容真被指纹覆盖）。

**本棒立场**：**案 B 已执行**（未动）；**案 A 是否启动属 PI 拍板项** —— 因涉「改名 → 幽灵引用 + 同步改 5 处引用行」，**不自行取舍**。

> **不误导提示**：案 B 的真实代价不是「不干净」，而是**占位哈希制造假绿**。若下游存在以该字段为完整性依据的校验，案 B 会让**未完成的指纹自证看起来已完成** —— 此点建议 PI 优先权衡。

---

## §3 `__pycache__` 清理（清走 1 个目录 + 登记 8 个）

### §3.1 派工前提更正（仪器先审自己）

派工称「`deposon-repo/__pycache__/` **空目录**/残留清走」。**实测：根目录非空** —— 13 个 `.pyc`，合计 **234,586 B**。

> **前提失实，如实登记，不按「空目录」处置**：按「**残留清走**」授权清走整个目录（含 13 `.pyc` 字节码缓存）。字节码为**可再生派生物**（`.py` 源件不动），删除后下次 import 自动重建 ⇒ 无语义损失。

### §3.2 清走 1 个目录（根目录）— 13 件逐件 SHA-12 登记

| # | `.pyc`（`__pycache__/` 内） | 字节 | SHA-12 |
|---|---|---|---|
| 1 | `deposon_diffusion.cpython-314.pyc` | 26,805 | `e45728c84ed4` |
| 2 | `deposon_protocol.cpython-314.pyc` | 3,425 | `fe0d7a1f574f` |
| 3 | `llm_fetch.cpython-314.pyc` | 11,386 | `24e5b4896930` |
| 4 | `llm_prior.cpython-314.pyc` | 7,859 | `9240adf94691` |
| 5 | `mindmap_corpus_v20.cpython-314.pyc` | 35,552 | `29f76d9b87e8` |
| 6 | `run_v15_experiment.cpython-314.pyc` | 33,387 | `5fe610ac1660` |
| 7 | `run_v16_llm_prior.cpython-314.pyc` | 16,357 | `d29f16f1f2b5` |
| 8 | `run_v17_fusion_fix.cpython-314.pyc` | 17,155 | `df7b08421bac` |
| 9 | `run_v19_fullrank.cpython-314.pyc` | 12,429 | `c2d386e27329` |
| 10 | `run_v19_meanfield.cpython-314.pyc` | 13,977 | `222ad7128b62` |
| 11 | `run_v19_quickwins.cpython-314.pyc` | 15,270 | `11f6e09806d2` |
| 12 | `run_v20_corpus_eval.cpython-314.pyc` | 26,055 | `346b364f5464` |
| 13 | `run_v20_gt2b.cpython-314.pyc` | 14,929 | `63ff13e1ee71` |

**合计：13 件 / 234,586 B。处置**：`mavis-trash` 可恢复删除（回执 `moved to trash: 'D:/私人资料/deposon-repo/__pycache__'`）。清后复验 = **GONE** ✅

### §3.3 登记不动 8 个目录（**超出派工授权范围**，如实登记）

派工点名范围为 `deposon-repo/__pycache__/`（根目录）。以下 **8 个 `__pycache__` 目录不在授权范围内，本棒 0 触动**，登记待 PI：

| 目录（repo 相对路径） | `.pyc` 数 | 本棒处置 | 不动理由 |
|---|---|---|---|
| `.tmp/__pycache__/` | 0（空） | **登记不动** | 09-27 noise manifest §3 已挂「空目录待 PI」，延续挂账 |
| `verifier/kill_lines/__pycache__/` | 0（空） | **登记不动** | 同上（空目录） |
| `verifier/audit/__pycache__/` | 1（`conservation.cpython-314.pyc`） | **登记不动** | **紧邻 18 frozen 之一 `verifier/audit/conservation.py`** ⇒ 保守口径不碰 |
| `results/__pycache__/` | 25 | **登记不动** | 含 09-27/09-28 新建 executor 字节码，**可能为在跑脚本的活缓存** |
| `results/_v3_recheck_08b_executor/__pycache__/` | 1 | **登记不动** | V3 executor 目录内 |
| `results/_v3_s1_executor/__pycache__/` | 1 | **登记不动** | V3 executor 目录内 |
| `results/_v3_s3_wordexpand_data/__pycache__/` | 2（含 09-28 当日件） | **登记不动** | **V3 数据目录内 + 含当日新字节码** |
| `deposon_team/plugins/__pycache__/` | 3（09-27） | **登记不动** | plugin 目录，保守口径 |

> **不扩大范围的理由**：派工授权止于根目录一处。`results/` 与 `deposon_team/plugins/` 下的 `.pyc` **多为近 2 日新建（09-27 16:11 / 09-28）**，属**潜在在跑脚本的活动缓存**；`verifier/audit/__pycache__` **贴邻 frozen 资产**。三者叠加 ⇒ **擅自清理可能打断在跑任务或触及 frozen 邻域**，超出「清理类」授权，**登记不擅动**。

---

## §4 0 触动自证（frozen 指纹 清前 / 清后）

**基线源**：`results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json`（18 frozen 逐件 `expected_sha12`）。
**方法**：清前 + 清后**各跑一次**全 18 件复算，逐件对照。

| 时点 | PASS | FAIL | MISSING | 判定 |
|---|---|---|---|---|
| **清前** | **18/18** | 0 | 0 | ✅ 全 MATCH |
| **清后** | **18/18** | 0 | 0 | ✅ 全 MATCH |

**触动数 = 0**（18 frozen 无一字节变化、无一缺失）。

### §4.1 交付件 / 证据件 0 动

- 本棒**唯一新增件** = 本 manifest（清理记录，**非** frozen、非证据链锚定件）。
- L14V3 verdict §0 输入链（`_l14v3_aggregated_10cells_v4.json` `66a9b8b3dabf` 等）**逐件复核在盘、未触动**。
- 派工 5 件铁律执行：agent 名 `evidence-auditor` / skill 名（无专项 skill 加载）/ Mavis plugin-cache sha256（不适用）/ 严守 7+9 铁律 / **老实交代 0 产物**（见 §6）。

---

## §5 R-4 key 形态自扫

**扫描器**：`\b` 词边界正则，扫本 manifest 全文（产物落盘后跑）。

| 模式 | 命中 |
|---|---|
| `\bsk-[A-Za-z0-9]{8,}` | **0** |
| `\btp-[A-Za-z0-9]{8,}` | **0** |
| `\bark-[A-Za-z0-9]{8,}` | **0** |
| `\bAPI_KEY\s*=` | **0** |
| `Authorization:\s*Bearer` | **0** |
| `\bBearer\s+[A-Za-z0-9\-._~+/]{12,}` | **0** |

**判定：CLEAN ✅**（本件为纯路径/哈希/缺陷描述，**0 处 key 形态**；§2.2 报出的 `aaaaabbbbbb` 系**已登记的占位哈希缺陷**，非 key，且为引用非新增）。

---

## §6 老实交代

1. **派工两处前提失实，均已实测更正**（未按原前提盲动）：
   - 「`__pycache__` **空目录**」→ 实为 **13 `.pyc` / 234,586 B 非空**。已按「残留清走」授权清走全目录，**13 件逐件 SHA-12 登记**（§3.2）。
   - R-4 路径给在 `deposon-sub/`（**仓外**）而非 `deposon-repo/` 内 → **仓外部位**，故**只读 0 写入**（§2.1）。
2. **未扩大授权范围**：8 个 `__pycache__` 目录（尤其 `results/` 近 2 日活动缓存 + `verifier/audit/` frozen 邻域）**登记不动**，非「漏清」（§3.3）。
3. **未擅动副区件**：R-4 两案仅**呈报**，案 A（改名补正）涉内容层 + 幽灵引用 + 5 处引用行同步，**超本棒权限，不自行取舍**，待 PI 拍板（§2.3）。
4. **勘误只追加**：M-7 哈希口径歧义（脚本哈希 `af1b7f09f74d`/`04b127d80bf0` 混列为 JSON 哈希）**只在本文登记，不回改历史行**（R5）。
5. **同哈希不重复计数**：v2/v3 = `SAME_IDENTITY`（`da0044cd24e3`），如实列全 2 份文件但计 **1 个身份**（§1.1）。
6. **succeeded ≠ 跑完**：三次清走均有 `mavis-trash` 回执 + 清后 `Test-Path` 复验（GONE）**双重确认**后方宣告完成；frozen 清前清后各跑一次 18/18。
7. **0 产物不编造**：本棒产物仅 1 件（本 manifest）；无未落盘宣称；§2 R-4 结论全部基于字节层实测（BOM 首 3 字节 / schema 字面 / 占位值命中）。

---

**署名**：Mavis 团队 evidence-auditor（`agent-11335500b168`）出件｜2026-09-28


<!-- appended-note:2026-09-30 skill 引用面复核（PI 派工第④项 · 0 删改历史字面） -->

> **附注（2026-09-30 追加 · 非原件内容）**
> 本件原引用字面**逐字保留、0 删改**；本附注**只增不改**。
>
> - **原引用面**：L175（出现 1 处）· 「Mavis plugin-cache sha256（不适用）」（无专项 skill 加载）
> - **2026-09-30 只读复核**：本件字面为**反向情形**（「Mavis plugin-cache sha256（不适用）」）⇒ 复核确认**当时无专项 skill 加载**，**无过期值可改**
> - **当前三段式锚**（plugin:skill + 树哈希前 12 + SKILL.md SHA-12 + 定位方式）：**不适用**（本件当时无 skill 加载）
> - **「历史实测 vs 今日实测」口径**：本件所记为**当时实测证据**，**保留有效、0 回改**；今日复核值以本附注与执行件为准，读者可据此区分二者（起因件建议 A2）。
> - **执行件**：`results/_skill_reference_update_and_user_surface_survey_2026_09_30.md` · 出件 **worker**（本棒）· **0 删改本件任何既有字节**