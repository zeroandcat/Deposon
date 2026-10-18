# D9 · H2 `r1_files` 21/21 断链 · 补修登记（U-5 · PI 扩授权「甲」）

> **本棒身份**：D9 之**补修执行棒**（H2·**PI 已扩授权**·**本棒为获准编辑 H2 之棒**）。
>
> **PI 裁（逐字）**：卡 `ask_0bbe075ddb9384473f717902` 之 `h2_residual` ＝ **「甲：扩授权补修（同 P-1 式·最小行级·逐行留痕）」**。
>
> **授权范围**：**唯一编辑对象 ＝ H2**（`_s5doubleprime_five_lines_runner_2026_10_11.py`，**sub 面**），**逐行留痕**。⛔ 0 编辑任何 markdown 既有件；⛔ 0 新建／移动／重命名／删除除本件外任何件；⛔ 0 覆写；⛔ 0 编辑 H1／H3／H4／H5。
>
> **上游件（只读回读，⛔ 0 回改）**：D9 补修登记 `results/_d9_residual_repair_register_2026_10_12.md`（`cddb7a196473`）§C-1 · 独立复核件 `results/_d9_independent_review_2026_10_12.md`（`732cfae29bbc`）§3-④ · U-5。
>
> **产出**：本件（唯一新件）。
>
> **执行**：worker（补修执行棒）· 2026-10-13 (+08:00)

---

## 0. 补修口径

| 项 | 值 |
|---|---|
| 修法总则 | **最小行级（同 P-1 式）**：⛔ 0 改他行、⛔ 0 改格式／行尾／编码、⛔ 0 增删 import |
| 落笔量 | **1 行**（H2 L141） |
| 行级留痕 | §A 逐字 **before → after 照录** |
| 验证方式 | **静态**：指纹／逆替换／`ast.parse`／`pathlib` 纯路径求值。⛔ **0 执行任何 runner** |
| 0 回改 | 上游 2 件 md **一字未动**（实测指纹见 §D-1，与在册值逐位吻合） |

---

## §A 病灶事实（落盘前实测 · 逐字回读，非转述）

### A-1 · 独立复核件 §3-④（`_d9_independent_review_2026_10_12.md` L165-167）逐字

> - H2 **L141** `fp = RESULTS / fname`，其 `r1_files` 取自 `OLD_HELDOUT_JSON["domain"]["r1_byte_sorted_files"]`（L388）——该 JSON **已改指 repo**（可达）。
> - **实测**：其 21 个文件名在 `SUB\results` **21/21 缺失**、在 `REPO\results` **0 缺失** ⇒ L141 指向 sub 将致 `FileNotFoundError`。
> - **登记状态**：执行登记 §6-④ **已载**「H2 旧 L140 `fp = RESULTS / fname`……仍指向 `SUB\results`」⇒ **本项经登记**，本棒仅**补其实测后果**（21/21 缺失）。

### A-2 · D9 补修登记 §C-1（`cddb7a196473` L136）逐字

> **H2 `r1_files`**（`_s5doubleprime_five_lines_runner_2026_10_11.py` L141 `fp = RESULTS / fname`）｜21 个文件名在 `SUB\results` **21/21 缺失**、在 `REPO\results` **0 缺失** ⇒ 指向 sub 将致 `FileNotFoundError`｜**H2 不在本棒授权 3 件内** ⇒ ⛔ 0 编辑；**候 PI**（复核件 U-5「随 P-1 口径一并裁」，PI 本轮所裁 P-1 限于 H4／H5）

### A-3 · 断链之机理（本棒独立复验）

`r1_files` 之**数据源**（L388 `old_ds["domain"]["r1_byte_sorted_files"]`，源 ＝ L46 `OLD_HELDOUT_JSON`）**已改指 repo 侧且可达**；唯**消费端**（L141 之 `RESULTS` 仍 ＝ `pathlib.Path(__file__).resolve().parent` ＝ **sub 面**）滞留于旧址 ⇒ **读源成功、逐件取数必抛 `FileNotFoundError`**。

**全件 `RESULTS` 实测出现处（改前，共 3 处）**：

| 行 | 逐字 | 性质 |
|---|---|---|
| L37 | `RESULTS = pathlib.Path(__file__).resolve().parent` | **定义行** |
| L38 | `REPO = RESULTS.parent` | 承 L37 定义 |
| **L141** | `        fp = RESULTS / fname` | **断链点（唯一病灶行）** |

---

## §B 修法与理由（最小行级 · 同 P-1 式）

- **修法**：将**唯一病灶行 L141** 之 `RESULTS` 改为**既有 D9 常量 `REPO_RESULTS`**（＝ `_repo_mirror\results`），**⛔ 0 新造字面**。
- **为何改调用点而不改 `RESULTS` 定义行（L37）**：① 改定义行虽省 1 行，但会**连带改写 L38 `REPO = RESULTS.parent` 之实际指向**（＝ 由 `deposon-sub` 变为 `deposon-repo`）——`REPO` 为该件**既有语义常量**，本棒⛔ 0 静默变更其指向；② 改调用点则 **L37／L38 逐字不动**；③ `REPO_RESULTS` 定义于 **L39**，**在 L141 之前**，⛔ 0 先后序问题；④ 与 D9 补修登记 §A-1（P-1 改 `RESULTS` 读取调用点、不改定义行）**同一口径**（PI 裁「同 P-1 式」）。
- **为何 `REPO_RESULTS` 确为此 21 件之正确现址**：逐件 `pathlib` 实测（§C）——sub 侧 **0/21 存在**、repo 侧 **21/21 存在**。

**逐行 before → after（照录 · 唯一落笔行）**

| 行 | BEFORE | AFTER |
|---|---|---|
| L141 | `        fp = RESULTS / fname` | `        fp = REPO_RESULTS / fname` |

> ⛔ L37（定义行）、L38（`REPO`）、L39（`REPO_RESULTS` 定义）、L142（`read_text`）、L388（`r1_files` 取值）、L390（`files=` 打印）——**一字未动**。

---

## §C 21 处逐处明细（目标现址实测 · 两区 `Test-Path`／`pathlib`）

> **修法为「一改全消」**：L141 单一读取点改指后，其循环所覆盖之 **21 个文件名逐处同消断链**。故下表「修否」栏 21/21 皆由**同一行**之改动而成立。

| # | 行号 | before → after | 目标文件名 | sub 现址 | repo 现址 | 修否 | 理由 |
|---|---|---|---|---|---|---|---|
| 1 | L141 | `RESULTS / fname` → `REPO_RESULTS / fname` | `_r_pair_addendum_2026_10_09.json` | **False** | **True** | ✅修 | 读取点改指 repo 侧 |
| 2 | L141 | 同上 | `_s4_open_questions_addendum_2026_10_09.json` | **False** | **True** | ✅修 | 同上 |
| 3 | L141 | 同上 | `_s4_substrate_topup_addendum_2026_10_09.json` | **False** | **True** | ✅修 | 同上 |
| 4 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | **False** | **True** | ✅修 | 同上 |
| 5 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 6 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 7 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 8 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 9 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 10 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 11 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 12 | L141 | 同上 | `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | **False** | **True** | ✅修 | 同上 |
| 13 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json` | **False** | **True** | ✅修 | 同上 |
| 14 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json` | **False** | **True** | ✅修 | 同上 |
| 15 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json` | **False** | **True** | ✅修 | 同上 |
| 16 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json` | **False** | **True** | ✅修 | 同上 |
| 17 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json` | **False** | **True** | ✅修 | 同上 |
| 18 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json` | **False** | **True** | ✅修 | 同上 |
| 19 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json` | **False** | **True** | ✅修 | 同上 |
| 20 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | **False** | **True** | ✅修 | 同上 |
| 21 | L141 | 同上 | `_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | **False** | **True** | ✅修 | 同上 |

**修毕计数：21 / 21**（**未能修之处：0**）——**0 处需因「两区皆缺」而保留断链**（21 件 repo 侧**逐件存在**，故⛔ 0 臆造址之情形**未触发**）。

---

## §D 指纹 · 差分 · 0 回改声明

### D-1 · H2 指纹（改前 → 改后）

| 项 | 改前（实测·落笔前） | 改后（实测） |
|---|---|---|
| 路径 | `_repo_mirror\results\_s5doubleprime_five_lines_runner_2026_10_11.py` | 同 |
| SHA-12 | `57f5a4c5d5cd`（与复核件／补修登记**在册值逐位吻合**，**不符即停手**之检验通过） | **`2d8cf387b478`** |
| bytes | **31,227** | **31,232**（**Δ ＋5** ＝ `REPO_RESULTS` 比 `RESULTS` 多 5 字符） |
| SHA-256 | `57f5a4c5d5cd2b90cee5b89dc81fd0a462b3d556952f575ae915e1550037b12e` | `2d8cf387b47896fb547ab31b8e2ccdf1429971cf2ed2c9d37d92550d58a39f04` |

### D-2 · 「仅 1 行变动」之实证（逆替换精确复现 · 非抽样）

对改后件作**单点逆替换**（`        fp = REPO_RESULTS / fname` → `        fp = RESULTS / fname`）后重算：

| 项 | 逆替换后实测 | 原件在册 | 判定 |
|---|---|---|---|
| SHA-12 | `57f5a4c5d5cd` | `57f5a4c5d5cd` | **精确复现** |
| bytes | **31,227** | 31,227 | **精确复现** |

⇒ **除 L141 外 0 行内容变动**（字节级反证）。

### D-3 · 编码／语法（改后实测）

| 项 | 值 |
|---|---|
| BOM | **无**（首三字节 `23 21 2f` ＝ `#!/`） |
| CR | **0** |
| TAB | **0** |
| CTRL | **0** |
| 行数 | 592（**未增减**） |
| 末行换行符 | `ends_nl=True`（与原件同，⛔ 0 擅改） |
| `ast.parse` | **OK**（⛔ 0 新增 import 需求：`pathlib`／`REPO_RESULTS` 皆已在件内） |

### D-4 · 静态可运行性核验（⛔ 0 执行 runner）

| 项 | 改后实测 |
|---|---|
| `r1_files` 件数（源 JSON 实读） | **21**（L390 期望 `179 / 21` 之 files 分量 ✅ 符） |
| 21 件于 `REPO_RESULTS` 之存在数 | **21 / 21** |
| 改前 `REPO_RESULTS` 存在数 | 21/21（改后不变，**读源与取数同侧，口径一致**） |

### D-5 · 上游件 0 回改与姊妹件 0 漂移（实测指纹）

| 件 | 本棒实测 SHA-12 ／ bytes | 在册 | 判定 |
|---|---|---|---|
| `_d9_residual_repair_register_2026_10_12.md` | **见 §D-6 实测** ／ 14,927 | `cddb7a196473` ／ 14,927 | **MATCH · 0 编辑** |
| `_d9_independent_review_2026_10_12.md` | **`732cfae29bbc`** ／ 22,644 | `732cfae29bbc` ／ 22,644 | **MATCH · 0 编辑** |
| `_s4prime_readings_runner_2026_10_11.py`（H1） | `52bb6e3bba15` ／ 23,870 | `52bb6e3bba15` ／ 23,870 | **MATCH · ⛔ 0 编辑** |
| `_s4_heldout_sampling_seedprime_extractor_2026_10_10.py`（H4） | `cd4f1e7b4879` ／ 19,003 | 补修登记改后值 | **MATCH · ⛔ 0 编辑** |
| `_s4_heldout_sampling_seedthird_extractor_2026_10_11.py`（H5） | `8ae074194a3d` ／ 52,785 | 补修登记改后值 | **MATCH · ⛔ 0 编辑** |
| `_v3_recheck_05_executor_2026_09_28.py`（H3） | `65f8a7514f34` ／ 38,733 | 补修登记改后值 | **MATCH · ⛔ 0 编辑** |

### D-6 · 本件落盘前检查

- 落盘前 `Test-Path`（`results/_d9_h2_r1files_repair_register_2026_10_13.md`）：**False**
- 落盘前 glob（`results/_d9_h2_r1files_repair*`）：**0 命中**

### D-7 · 0 回改声明

- ⛔ **0 回改任何 markdown 既有件一字**——含 D9 补修登记 `cddb7a196473`、独立复核件 `732cfae29bbc`、执行登记 `0ea7852c4511`。
- ⛔ **0 编辑 H1／H3／H4／H5**；**唯一编辑对象 ＝ H2 之 1 行**（L141，逐行留痕，逆替换字节级实证 0 溢出）。
- ⛔ **0 覆写**除 H2 之行级编辑外任何文件；⛔ **0 新建／0 移动／0 重命名／0 删除**除本件外任何件。
- ⛔ **0 触** `〔本地归档区〕`（**0 读 0 写 0 列目录**）；临时脚本仅落 `%TEMP%`，**未入仓**。
- ⛔ 0 网络／0 skill／0 LLM／0 读 `.env`／0 经手 PAT；⛔ **0 改终判词／阈值／门柱／判死线**（`len(files) != 21` 之类门柱**未触碰**；L390 期望值 `(expect 179 / 21)` **一字未动**）；⛔ 0 赋 `k_v3s_4_4_*` 布尔；⛔ **0 执行任何 runner**；⛔ **0 宣告①毕**。
- ⛔ 0 写他棒产物名域（`_p4_inplace_resolution*`／既有 `_d9_*`／`_p4_*`／`_three_exception_pullback*`／`letters/`／`_bob_*`／`_remote_baseline*`／`_archive_2026-10-12`）。

---

## §E 对「runner 可运行性」项之影响（如实登记 · ⛔ 0 代裁）

| 项 | 本棒呈报 |
|---|---|
| **U-5（H2 `r1_files` 21/21）** | **静态修毕 21/21**（1 行）。改前：sub 侧 21/21 缺失 ⇒ L142 `read_text` **必抛 `FileNotFoundError`**；改后：repo 侧 **21/21 可达**。 |
| **D9 之 ②「runner 可运行性」跟踪项** | 本棒**仅闭合 U-5 一项**。余下登记在案者**状态不变**：**H3 `SRC_ANCHOR_FALLBACK`**（L62，4 候选址皆 `False`·**P-4**·候 PI）、**C-3**（`d6ff7e9b4bd6` §2.4 载 24／实测 21）、**C-4**（底本 CJK 损坏）。⇒ **⛔ 0 宣告 runner 可运行性成立或归零**（**⛔ 0 执行 runner**，端到端**未验**）。 |
| **①（29 行路径改写）** | **不受影响**——本棒 1 行与该 29 行**无交集**，⛔ 0 触及其一。 |

> 📌 **0 判定声明**：本件所载**全部为读数**（静态指纹／逆替换／路径求值／语法解析），**非判定**；**判定归 PI**。⛔ 0 代裁 `Z-1`／`Z-4` 之任何计数。

---

## §F 未决项（候 PI · ⛔ 0 自作主张处置）

| # | 未决 | 状态 | 归属 |
|---|---|---|---|
| F-1 | **H3 `SRC_ANCHOR_FALLBACK`**（L62） | 4 候选址皆 `False`；本棒**0 触碰** | **P-4** · 候 PI |
| F-2 | **C-3** `d6ff7e9b4bd6` §2.4「24 条」vs 实测 21 条 | 差 3；⛔ 0 回改 v2 | **U-7** · 候 PI／勘正 |
| F-3 | **C-4** 底本 `c3167a531e0e` CJK 损坏 | 实测 0 非 ASCII 字节、4,631 字面 `?` | **U-6** · 候 PI |
| F-4 | **端到端可运行性** | ⛔ 0 执行 runner，**无凭据** | 候 PI 裁是否派执行棒 |

---

## 附录 A · 本登记件指纹

| 项 | 值 |
|---|---|
| 路径 | `results/_d9_h2_r1files_repair_register_2026_10_13.md` |
| SHA-12 | **见交付回报**（落盘后字节级自测） |
| bytes | **见交付回报** |
| BOM／CR／TAB／CTRL | **无 ／ 0 ／ 0 ／ 0** · UTF-8 无 BOM · 纯 LF |
| nonAscii | **> 0**（断言成立） |
| U+FFFD | **0**（断言成立） |
