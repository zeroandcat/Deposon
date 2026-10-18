# V5 清卷 M-R3｜S-40 kill-line 双因修复 ＋ 预登记字面复算注记（2026-09-29）

- **任务**：deposon V4 清卷·轮 11 裁项 **M-R3** ＝ **A「采纳补正建议行＋汇入勘误链」**
- **执行**：Mavis worker（delegated sub-task 2026-09-29，本会话 worker 分支）
- **裁项出件**：`results/_v5_r4_residual_merged_catalogue_2026_09_29.md` §M-R3（L165–L181）
- **0 回改既有件承诺**：源执行棒、升格件、预登记、语义复核件、勘误建议件 **全部只读**

---

## §0 一句话结果

按 `0d6b3c74dc98` L153/L155 两条修复建议修执行棒（**落新名件**），
S-40 按**预登记字面**独立复算：**三项 kill-line 全部 False（hit=False / pass=True）⇒ S-40 = PASS**。
复算读数与 `0d6b3c74dc98` §4.3 独立复算在 4 位精度内**完全吻合**（0 凑结论，读数由公式算出）。

---

## §1 核明（先核后引 · SHA-12 盘上实测）

SHA-12 口径 = `hashlib.sha256(字节).hexdigest()[:12]`（小写）。

| 件 | 派工单标称 | **盘上实测** | 字节 | 核验 |
|---|---|---|---|---|
| `results/_v4_s40_correction_note_2026_09_23.md` | `065e57820c36` | **`065e57820c36`** ✅ | 11,581 | 一致 |
| `results/_v4_s40_semantics_verdict_2026_09_23.md` | `0d6b3c74dc98` | **`0d6b3c74dc98`** ✅ | 12,143 | 一致 |
| `results/_v4_rootcause_upgrade_review.md`（升格件） | `c398cf82b3ea` | **`c398cf82b3ea`** ✅ | 20,182 | 一致 |
| `results/_v4_seeds_prereg_supplement_2026_09_23.md`（预登记） | — | `113cbe555643` | 53,633 | 与 `065e57820c36` L136 登记一致 |
| `results/_v4_rerun_executor_2026_09_23.py`（执行棒） | 「先核后引」 | **`cb47672e3062`** | 67,571 | **见 §2 重要发现** |

> **定位说明**：上述四根均在**仓外** `D:/私人资料/_non_upload_local_archive/results/`（不在 `deposon-repo/results/`）。
> 按盘上实测路径引用；沿「仓外只读」纪律执行。

### §1.1 预登记字面（只读引用 · `113cbe555643`）

- **L361**（claim）：检测信号在 V2/V3/D7 三版本上 **CV < 0.50**（跨版本稳定）
- **L367 K-S40-1**：**CV ≥ 0.50 即 FAIL**
- **L368 K-S40-2**：**bootstrap CI 95% 上界 ≥ 0.50 即 FAIL**
- **L369 K-S40-3**：**合成 token-shuffle 负对照 CV ≥ 0.50 且 CV_proxy ≤ CV_shuffle 即 FAIL**
- **L510**（S-40 汇总行）：`CV ≥ 0.50 即 FAIL（K-S40-1）`

**判死线全文三条，本棒 0 触碰一字**（`TH_TAU_CV = 0.50` 一字未动）。

---

## §2 ⚠️ 重要发现：源执行棒盘上**已是修复后形态**（先核后引的核出物）

派工单按「修执行棒」派工。**实测核出与派工前提有出入，如实报告**：

| 项 | `065e57820c36` L19/L21/L138 登记 | 盘上实测 | 判读 |
|---|---|---|---|
| executor SHA-12 | 改前 `7a98fdf05466` → 改后 `cb47672e3062` | **`cb47672e3062`** | 盘上 **＝「改后」** |
| executor 字节 | 67,039 → 67,571（+532） | **67,571** | 盘上 **＝「改后」** |
| L833 | 登记含 `or range_val > 1.0` | 盘上 **无**该子句 | 致命 1 **已被修** |
| L837–L853 | 登记为 pass wrapper 形态 | 盘上 **已是** `pass` + `threshold_desc` | 致命 2 **已被修** |

**即**：2026-09-23 的 VFIX-S40 棒（`065e57820c36` L3 记 session `mvs_d65db996d6a844ad8e9418b4841225db`）
**已在原文件上就地改**（该档 L7/L138 自注「**改**：L833 + L837-L853（共 17 行）」，
与同档 L7 承诺的「`_v4_rerun_verdict.md` 等原件一字不动」并列 —— 承诺范围不含 executor 自身，
但**与本轮 R5「改动只落新名件」口径不一致**）。

**对本轮的影响（如实定性）**：

1. **本轮交付的「新名修复 executor」在实质上是「可复现的修复版新名件」**，不是首次就地修复。
2. **改前字节（`7a98fdf05466` / 67,039 B）盘上已不存在**，全盘无该形态副本
   ⇒ §3 的「改前」文本**只能逐字转引自 `065e57820c36` L28/L29**（文献性转引，非盘上实测）。
3. **未受影响的仍成立**：本轮 0 回改既有 executor ＋ 0 回改升格件 ＋ 0 触预登记字面；
   复算仍在**新名件**上跑通并落**新名结果件**。

---

## §3 修复内容（L833 / L837 前后对照）

### 3.1 修复点 ①：L833 `failed` 公式 —— 删非预登记条款

| | 文本 |
|---|---|
| **改前**（逐字转引 `065e57820c36` L28；**盘上已无此字节**） | `failed = cv_val >= TH_TAU_CV or ci[1] >= TH_TAU_CV or range_val > 1.0 or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)` |
| **改后**（新名件 `failed_prereg_only()`，盘上实测） | `failed = cv_val >= TH_TAU_CV or ci[1] >= TH_TAU_CV or (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)` |

- **依据**：`0d6b3c74dc98` L153「删除 `or range_val > 1.0` 子句；或将其从 failed 公式迁出为独立 sanity-check 字段（标注『构造警告』而非 kill-line）」。
- **本件处置**：**两条建议同时采纳** —— 子句从判死面删除，同时在结果件中以
  `construction_warning_not_a_killline` 字段保留其读数（`range_val = 2.119411`，`triggered = true`），
  **明确标注不参与 verdict**。
- **0 触预登记**：删的是**多出来的子句**，不是**判死线本身**；`K-S40-1/2/3` 三条字面与 `TH_TAU_CV=0.50` 一字未动。

### 3.2 修复点 ②：L837 `kill_lines` —— 恢复 `pass` 命名 wrapper

| | 文本 |
|---|---|
| **改前**（逐字转引 `065e57820c36` L29；**盘上已无此字节**） | `"kill_lines": {"K-S40-1": cv_val < TH_TAU_CV, "K-S40-2": ci[1] < TH_TAU_CV, "K-S40-3": not (cv_shuf >= TH_TAU_CV and cv_val <= cv_shuf)}`（raw bool，无命名方向） |
| **改后**（新名件 `kill_lines_fixed()`，盘上实测） | 每个键嵌 `threshold_desc` + `pass` wrapper：`"K-S40-1": {threshold_desc: "CV>=0.50即FAIL", observed: <v>, pass: bool(<v> < 0.50)}`（三项同构） |

- **命名方向**：`pass = True` ＝ **kill-line 未触发 ＝ claim 存活**，与预登记字面「CV ≥ 0.50 即 FAIL」**同向**。
- **依据**：`0d6b3c74dc98` L155/L157–L163 建议块（逐字采用其字典形态）。
- **对照留痕**：改前 raw bool 形态仍以 `counterfactual_prefix_documented_only.kill_lines_prefix_raw_bool`
  落盘（三项均 `True`，若按「True = hit」消费即方向相反），**仅作双因对照，不驱动 verdict**。

### 3.3 新名件修复点对照（落盘件内）

| 件内函数 | 对应源行 | 作用 |
|---|---|---|
| `failed_prereg_only()` | L833（修） | 判死面仅含预登记三项 |
| `failed_with_unprereg_clause()` | L833（改前） | 双因对照，不驱动 verdict |
| `kill_lines_fixed()` | L837–L853（修） | 恢复 `pass` wrapper ＋ `threshold_desc` |
| `kill_lines_prefix_raw_bool()` | L837（改前） | 双因对照，不驱动 verdict |

---

## §4 S-40 按预登记字面复算结果

**复算件**：`results/_v5r_s40_recompute_2026_09_29.json`（SHA-12 `5be465342ae1`，4,992 B）
**执行件**：`deposon_team/plugins/_v5r_s40_rerun_executor_fix_2026_09_29.py`（SHA-12 `a4ae5d5f19c8`，17,665 B）

### 4.1 读数（seed=42，22 caption → 100 cell，**全精度**）

| 量 | 全精度 | 4 位 |
|---|---|---|
| `cv_val`（K-S40-1） | **0.100852** | 0.1009 |
| `ci_95` | **[0.092012, 0.110904]** | [0.092, 0.1109] |
| `cv_shuf`（负对照） | **0.100852** | 0.1009 |
| `range_val`（**非** kill-line） | **2.119411** | 2.1194 |
| `min_cvs` / `max_cvs` | 0.013747 / 0.227494 | — |
| `n_cells` | **100** | — |

### 4.2 三项 kill-line（**方向 = hit**；括号内为 `pass`）

| kill-line | 预登记字面 | 观测量 | 阈值 | **hit** | `pass` |
|---|---|---|---|---|---|
| K-S40-1 | CV ≥ 0.50 即 FAIL | 0.1009 | 0.50 | **False** | True |
| K-S40-2 | CI 95% 上界 ≥ 0.50 即 FAIL | 0.1109 | 0.50 | **False** | True |
| K-S40-3 | CV_shuf ≥ 0.50 ∧ CV_proxy ≤ CV_shuf 即 FAIL | [0.1009, 0.1009] | 0.50 | **False** | True |

> K-S40-3 的第二个合取项 `CV_proxy ≤ CV_shuffle` **为真**（0.100852 ≤ 0.100852，相等），
> 但第一个合取项 `CV_shuf ≥ 0.50` **为假**（0.100852 < 0.50）⇒ 合取式**整体为假 ⇒ 未触发**。

### 4.3 判定

- `all_three_false = true`
- **`verdict = PASS`**，`root_cause = 命题层面成立`
- 与 `0d6b3c74dc98` §4.2 独立复算（cv_val=0.100852 / ci_hi=0.110904 / cv_shuf=0.100852）**逐位吻合**。
- 与 `065e57820c36` §4 五对照表「改后重跑」行（0.1009 / [0.092, 0.1109] / 0.1009）**4 位精度内完全吻合**。

### 4.4 等价性交叉核对（`--cross-check` 实测）

新名件以**只读**方式 import 源执行棒、调用其 `run_S40()`，与本件复刻逐字段比对：

```
cross-check equivalent = true
  source_verdict  = PASS   replica_verdict = PASS
  source_kill_lines_pass  = {K-S40-1: true, K-S40-2: true, K-S40-3: true}
  replica_kill_lines_pass = {K-S40-1: true, K-S40-2: true, K-S40-3: true}
```

⇒ 新名件复刻与源执行棒 `run_S40()` **数值等价**（cv / ci / range / negctrl / n_cells / 三项 pass 全等）。

### 4.5 构造警告（**不参与 verdict**）

`range_val = 2.119411 > 1.0` ⇒ `triggered = true`。
按 `0d6b3c74dc98` L153 的第二处置，该子句以 **sanity-check 字段**留痕，**不是 kill-line**。

---

## §5 双因入链建议（勘误条目文本 · 供后续用）

> **本节仅为「补正建议行」文本**。本棒**0 改写升格件 `c398cf82b3ea` 一字**，
> 是否采纳由 parent 复审后按勘误链流程处置（沿 `065e57820c36` L186「须 parent 审核」纪律）。

### 5.1 建议入链条目（E-2x · S-40 kill-line 语义双因补正）

**根因（建议措辞）**：

> S-40 PASS→FAIL 翻转系执行棒 `_v4_rerun_executor_2026_09_23.py:833` failed 公式新增
> **非预登记条款 `range_val > 1.0`**（致命 1）**单独驱动**
> ＋ L837 kill_lines 字典**丢弃 pass 命名 wrapper**，
> 致「True = hit」与预登记字面「**CV >= 0.50 即 FAIL**」**方向相反**（致命 2）**双因**；
> 按预登记字面独立复算三项 kill-line **全部 False → S-40 应判 PASS**。

**升格件归因补正（建议措辞）**：

| | 文本 |
|---|---|
| 原（`c398cf82b3ea` L166，**原件不动**） | 「K-S40-1/2/3 hit 方向翻转 ＝ threshold-evaluation-path artifact」 |
| 建议补正 | 「S-40 PASS→FAIL 翻转系**执行棒构造面越权（failed 公式引入非预登记条款 `range_val > 1.0`）** ＋ **kill_lines 丢 pass wrapper 致方向歧义**」双因；升格件原归因**方向对**（假证伪成立）但**根因描述不完整（漏致命 1）**。 |

**范围声明（建议措辞）**：

- 升格件 L166–L227「真证伪 = 0 条 / 假证伪 13 条」**整体结论方向正确**，0 推翻；
- 本条仅补 **S-40 单条**的根因描述，**0 改判任何其他条目**；
- **0 改判死线字面**：`K-S40-1/2/3` 与 `TH_TAU_CV=0.50` 一字未动。

### 5.2 附带的第三条建议（**新发现 · 供 parent 裁量**）

> **执行棒就地改动与新名件纪律的偏离**：2026-09-23 VFIX-S40 棒在**原文件**上就地改了 executor
> （`7a98fdf05466`/67,039 B → `cb47672e3062`/67,571 B，`065e57820c36` L138 自注「**改**」），
> 改前字节**盘上已无留存**，致本次「改前/改后」对照**只能文献转引**。
> 建议 parent 裁量：是否把「执行棒类改动一律落新名件、保留改前副本」写进后续工程纪律条目。

---

## §6 0 回改自证（既有件 SHA 前后复验 · 跑前 vs 跑后）

**六件只读根，跑前/跑后 SHA-12 完全一致，mtime 全部仍为 2026-09-23（今日 0 写）**：

| 件 | 跑前 SHA-12 | 跑后 SHA-12 | 字节 | mtime | 触动 |
|---|---|---|---|---|---|
| `_v4_rerun_executor_2026_09_23.py` | `cb47672e3062` | **`cb47672e3062`** | 67,571 | 2026-09-23 16:29:33 | **0** |
| `_v4_s40_correction_note_2026_09_23.md` | `065e57820c36` | **`065e57820c36`** | 11,581 | 2026-09-23 16:40:48 | **0** |
| `_v4_s40_semantics_verdict_2026_09_23.md` | `0d6b3c74dc98` | **`0d6b3c74dc98`** | 12,143 | 2026-09-23 16:18:47 | **0** |
| `_v4_rootcause_upgrade_review.md`（升格件） | `c398cf82b3ea` | **`c398cf82b3ea`** | 20,182 | 2026-09-23 15:34:54 | **0** |
| `_v4_seeds_prereg_supplement_2026_09_23.md`（预登记） | `113cbe555643` | **`113cbe555643`** | 53,633 | 2026-09-23 11:37:59 | **0** |
| `_v4_exec_s40_rejudged_2026_09_23.json` | `d3f376a6c45f` | **`d3f376a6c45f`** | 6,703 | 2026-09-23 16:38:39 | **0** |

**本棒落盘件（3 件，全部新名）**：

| 件 | SHA-12 | 字节 |
|---|---|---|
| `deposon_team/plugins/_v5r_s40_rerun_executor_fix_2026_09_29.py` | `a4ae5d5f19c8` | 17,665 |
| `results/_v5r_s40_recompute_2026_09_29.json` | `5be465342ae1` | 4,992 |
| `results/_v5_clearance_mr3_s40_fix_note_2026_09_29.md`（本档） | 见交付回执 | — |

> 落盘前已 `glob` 确认 0 同名件；派生结果 JSON **不并入**任何既有 JSON（沿「派生 JSON 不合并」）。

---

## §7 诚实边界

1. **0 LLM / 0 API / 0 proxy / 0 gateway** —— 纯本地 `random.Random(42)` 复算，无任何网络调用。
2. **R4 key 永不明文** —— 新落 3 件 key 形态自扫 clean：按四类凭证形态正则（`sk-` 前缀长串 / 凭证名+值对 / `Bearer` 头 / 令牌赋值）全量扫描，**0 命中**。本档自身曾因逐字列出该四类模式名而产生 1 处自指误报，已改写措辞后复扫 0 命中。
3. **0 触预登记字面** —— `TH_TAU_CV=0.50` 与 K-S40-1/2/3 一字未动；修的是**实现**不是**判死线**。
4. **0 改既有 executor / 0 改升格件 `c398cf82b3ea`** —— 全部改动只落新名件，六件只读根 0 触动（§6）。
5. **0 预判结论** —— `verdict` 由 `failed_prereg_only()` 公式算出，未写死；`kill_lines` 由观测量算出，未预填。
6. **0 编造读数** —— 全部读数来自本地实跑并落盘；未沿用任何历史件的数值（本棒实跑独立产出）。
7. **⚠️ 改前文本非盘上实测** —— 源 executor 盘上已是修复后形态（§2），
   §3 的「改前」两行**逐字转引自 `065e57820c36` L28/L29**，标注为文献性转引，**未冒充实测**。
8. **本棒 0 独立复核既有三件判定** —— 双因归因、`0d6b3c74dc98` 复算、`c398cf82b3ea` 判定
   **全为他棒字面**；本棒只做「按预登记字面复算」＋「新名件修复」，
   **0 认可、0 推翻、0 改判**（沿 `065e57820c36` L186 纪律）。
9. **PASS 的适用范围** —— 本次 PASS 是「**按预登记字面**的 S-40 单条」判定；
   **不构成**对升格件其余 21/22 条的任何改判，**不构成**对 S-40 命题「跨版本稳定」的经验性证实
   （本读数出自**模拟构造**的 CV 路径，与原执行棒同构，非新独立证据）。

---

## §8 交付回执

| 项 | 值 |
|---|---|
| 修复 executor（新名） | `deposon_team/plugins/_v5r_s40_rerun_executor_fix_2026_09_29.py` / `a4ae5d5f19c8` / 17,665 B |
| 复算结果件（新名） | `results/_v5r_s40_recompute_2026_09_29.json` / `5be465342ae1` / 4,992 B |
| 注记件（本档） | `results/_v5_clearance_mr3_s40_fix_note_2026_09_29.md` |
| 复算结论 | **三项 kill-line 全 False ⇒ S-40 = PASS**（命题层面成立） |
| 0 回改 | 六件只读根 0 触动（§6） |

**出件署名**：Mavis worker（delegated sub-task 2026-09-29，M-R3 裁 A 执行棒）。
本档所有引述均标明来源件与其 SHA-12；**未沿用/顶替任何他方署名**。
