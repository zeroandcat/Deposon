# skill 引用面 ④ 批量更新登记 ＋ ⑥ 用户面 223 项普查（2026-09-30）

- **件性质**：**执行登记件**（含两节：④ 更新明细 ＋ ⑥ 普查表 ＋ 风险清单 ＋ 诚实边界）
- **触发**：PI 2026-09-30 裁「skill 面**六项全办**」；本棒执行其中 **④**（48 件引用更新）与 **⑥**（223 项普查）
- **依据**：`results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md`（`c14489750416`，§引用盘点：48 件）＋ `results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md`（`644e0666fbc4`，§4-⑥ 未决项 #6）
- **出件**：**worker**（`mvs_09b77b878382407c8701411ae5046c92`）· 依派工单执行 · **0 LLM / 0 API / 0 外部 URL / 0 key 读取**
- **方法**：PowerShell 只读枚举 + `Get-FileHash -Algorithm SHA256`（全值算完截前 12，**非 SHA-1 冒充**）+ `grep` 只读检索；**追加写仅限 29 件授权面**（见 §1）
- **命名**：去版本前缀 · `_主题_日期`；落名前 **2 轮 × 4 目录**（`results/` `docs/` `letters/` `deposon_team/`）全部 `exists=False`，另加全仓递归近名 glob（`*user_surface_survey*` / `*reference_update*`）仅命中依据件本身 ⇒ **新建，0 覆写**

> **一票结论（先看这条）**：④ 的 48 件里，**47 件的引用字面 2026-09-30 复核后仍然成立**（路径逐字在位、树哈希同目录名、`SKILL.md` SHA-12 对得上）——**没有「过期值」可供就地更新**，故 29 件文字件一律**追加注记**、**19 件冻结产出物一律跳过**，**0 件就地更新**。唯一确已过期的注记（`verification-before-completion`「possibly-missing」）按「实录件 0 回改」惯例**以追加勘误承载**。⑥ 的 223 项**结构面 223/223 齐备**（0 异常），但**调用面 0 次实测**——本棒工具面无 skill 加载器，故 223 项**调用面一律记「未测」**。

---

## §0 输入链核验（全部只读 · 本棒实测 · 非转述）

| # | 件 | 本棒实测 SHA-12 | 字节 | 引用面 |
|---|---|---|---|---|
| 1 | `results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md` | `c14489750416` | 31,692 | **④ 依据**：§3.1 列 48 件文字件；§3.2 建议 A1–A8 |
| 2 | `results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | `644e0666fbc4` | 25,901 | **⑥ 依据**：§4 未决项 #4（48 件批量更新）/ #6（223 项普查） |

**本棒独立复测的盘上锚**（不转述依据件数值）：

| 锚 | 本棒实测 | 与依据件 |
|---|---|---|
| plugin-cache 树数 | **28** | 一致 |
| plugin-cache skill 总数 | **172** | 一致 |
| 树 `611965fcb620…` | 在位，**9** skills | 一致 |
| 树 `ade95665080e…` | 在位，**14** skills | 一致 |
| 树 `01afed677637…` | 在位，**4** skills | 一致 |
| `.minimax\plugins\` | **空目录（0 项）** | 一致 |
| `.minimax\.builtin-skills\` | **20** 项 | 一致 |
| `experimental-design/SKILL.md` | `0a314eed103a` / **13,044** B | 一致 |
| `scientific-writing/SKILL.md`（plugin 面） | `31f4fb3c0df5` / **13,047** B | 一致 |
| `peer-review/SKILL.md`（plugin 面） | `fed0262d707a` / **11,639** B | 一致 |
| `verification-before-completion/SKILL.md` | `2befe7fc55bc` / **3,646** B | 一致 |
| `academic-paper-polish/SKILL.md` | `23d90731e1fe` / **7,095** B | 一致 |
| `C:\Users\Administrator\.minimax` | **Junction** → `D:\Users\Administrator\.minimax` | 一致 |

**命中数口径已对账（本棒新增）**：依据件 §3.1 的「命中数」为 **出现次数**（occurrence）口径；本棒初测用 **行数**口径，两者不等。本棒**两种口径同时给出**并已**逐件对齐**——按出现次数计，29 件文字件与依据件 §3.1 **逐字全等**（9/9/4/4/4/1/2/1 · 3/5/4/1/1/1/1/1/1/1/1/2/1/2/2/4/3/4/4）。**口径差异系测量法差异，非件面差异。**

---

## §1 ④ 48 件引用更新（分类最小合规处置）

### §1.1 处置规则（分类依据与理由）

| 类 | 件数 | 处置 | 理由 |
|---|---|---|---|
| **A 类 · 内部文字件**（`results/*.md` 登记/复核/裁决/清册类） | 21 | **追加尾注** | 47/48 字面经复核**仍成立** ⇒ **无过期值可改**；「就地更新」无对象。且 PI 口径「实录件 0 回改、反转型修正以追加勘误承载」⇒ 追加为最小动作 |
| **B 类 · 对外件 / 信本体**（`letters/*.md` 8 件） | 8 | **追加尾注** | 派工单明列「已对外件、落册/信本体、冻结锚件：一律追加注记形式」；路径/树哈希写死之陈旧风险（建议 A1）**仍成立**，以追加行承载，**0 删改任何历史字面** |
| **C 类 · 冻结产出物**（`.py` 14 + `.json` 5） | 19 | **跳过（0 改动）** | 建议 A3：内嵌绝对路径属**冻结产出物内容**；其字节/哈希已被其他件作为证据引用，改之即破坏既有对账链 ⇒ 锚由本登记件承载 |
| **D 类 · 二进制状态备份** | 0（本棒不涉） | — | 依据件 §3.1 单列 1 件二进制（`.evidence_backup_2026_09_28/runtime-state.sqlite`），**不属 48 件文字件**，本棒 0 触动 |

**就地更新计数 = 0**，理由见上：**无任何一件存在「已过期的值」可供就地替换**——唯一过期注记（A6）按实录件惯例走追加勘误。

### §1.2 逐件更新明细（29 件「追加」面）

**B 类 · 对外件 8 件**

| # | 件 | 原引用面（行/出现次数） | 处置 | 前 SHA-12 → 后 SHA-12 | 字节 |
|---|---|---|---|---|---|
| 1 | `letters/_v4_experiment_invitation_2026_09_20.md` | L326,362,367,421,423,424,426 / 9 | 追加尾注 | `4e8c0ea57028` → `20f8242de6ca` | 30,820 → 32,164 |
| 2 | `letters/_v4_experiment_invitation_2026_09_20_v0.2.md` | L344,380,385,439,441,442,444 / 9 | 追加尾注 | `8e1e7434905d` → `72fc2e7fb098` | 41,680 → 43,024 |
| 3 | `letters/_v4_theme_reply_mavis_2026_09_20.md` | L12 / 4 | 追加尾注 | `00315728bbf5` → `5d932d7085cd` | 36,719 → 37,980 |
| 4 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.1.md` | L12 / 4 | 追加尾注 | `82fee0a18dab` → `5c61f61f1f7e` | 36,824 → 38,085 |
| 5 | `letters/_v4_theme_reply_mavis_2026_09_20_v1.2.md` | L12 / 4 | 追加尾注 | `3ecf5b38048e` → `f1d73c82511d` | 36,826 → 38,087 |
| 6 | `letters/_v4_acceptance_trae_code_2026_09_20.md` | L72 / 1 | 追加尾注 | `3205593030bc` → `3e2f1c84e86d` | 6,301 → 7,746 |
| 7 | `letters/_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | L74 / 2 | 追加尾注 | `d3bdfc99fcdc` → `f88e429717aa` | 11,877 → 13,263 |
| 8 | `letters/_v4_distillation_invitation_2026_09_20_v1.0.md` | L322 / 1 | 追加尾注 | `3d9f73519f6c` → `e4b00fa97d03` | 53,539 → 54,784 |

**A 类 · 内部文字件 21 件**

| # | 件 | 原引用面（行/出现次数） | 处置 | 前 SHA-12 → 后 SHA-12 | 字节 |
|---|---|---|---|---|---|
| 9 | `results/_v3_recheck_12_jsv_check_2026_09_27.md` | L136,137 / 3 | 追加尾注 | `2b9e886e729d` → `c5eab30e9fc6` | 14,525 → 15,821 |
| 10 | `results/_v3_recheck_26_preexp_report_2026_09_27.md` | L24,26,228 / 5 | 追加尾注 | `0a2b5c837c83` → `a46230e344af` | 21,855 → 23,048 |
| 11 | `results/_v3_recheck_26b_rescript_2026_09_27.md` | L19,21 / 4 | 追加尾注 | `c300e74a082c` → `ae81d9b59054` | 29,349 → 30,552 |
| 12 | `results/_v3_recheck_01_rescript_2026_09_27.md` | L143 / 1 | 追加尾注 | `434b3213bdce` → `a3c95102290f` | 13,233 → 14,541 |
| 13 | `results/_v3_recheck_04_rescript_2026_09_27.md` | L153 / 1 | 追加尾注 | `2e0f6b8bf141` → `34099595fe75` | 13,472 → 14,780 |
| 14 | `results/_v3_recheck_12_rescript_2026_09_27.md` | L204 / 1 | 追加尾注 | `1cd36ac1b2c0` → `776c86c735f8` | 19,914 → 21,222 |
| 15 | `results/_v3_recheck_prereg_v1p2_2026_09_27.md` | L259 / 1 | 追加尾注 | `bc68854a6eba` → `9da148037744` | 37,636 → 38,932 |
| 16 | `results/_v3_recheck_prereg_v1p3_2026_09_27.md` | L230 / 1 | 追加尾注 | `a8da321b64d2` → `272ed65bf50e` | 33,904 → 35,200 |
| 17 | `results/_v3_recheck_verdict_register_2026_09_27.md` | L330 / 1 | 追加尾注 | `17262abfd1d5` → `d9b6b974cfc1` | 110,787 → 112,085 |
| 18 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | L14 / 1 | **追加勘误尾注**（A6 唯一过期项） | `2fb5987f544d` → `189ba84fc12e` | 192,292 → 193,632 |
| 19 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` | L234 / 1 | 追加尾注 | `68f66904c0c8` → `fe907046eda1` | 22,863 → 24,168 |
| 20 | `results/_v4_gamma_r1_prereg_2026_09_28.md` | L283 / 1 | 追加尾注 | `02c072833cca` → `c9da8678cf2b` | 32,186 → 33,489 |
| 21 | `results/_v4_pending_decisions_2026_09_28.md` | L171 / 1 | 追加尾注 | `6db65c9d8792` → `fe4671517827` | 23,373 → 24,676 |
| 22 | `results/_v4_pi_cot_v3_v3r1_rescript_2026_09_27.md` | L6 / 2 | 追加尾注 | `fbf88f8ac7a6` → `75aedf9ba95e` | 10,103 → 11,385 |
| 23 | `results/_v4_slow_cleanup_manifest_2026_09_28.md` | L175 / 1 | 追加尾注（反向情形） | `5a6bb7f70418` → `012501569aea` | 14,600 → 15,693 |
| 24 | `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | L52,259 / 2 | 追加尾注 | `98a779d61c1e` → `9ba12a0fbac1` | 48,028 → 49,326 |
| 25 | `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` | L50,487 / 2 | 追加尾注 | `05b975a86989` → `e7c3e2ef4e6b` | 61,547 → 62,847 |
| 26 | `results/_v4_supp_l14v3_n26_verdict.md` | L437,474,509 / 4 | 追加尾注（＋A5 统计口径） | `f4435801d09f` → `df6453d57f8a` | 64,485 → 65,978 |
| 27 | `results/_v4_supp_t1_verdict.md` | L275,306 / 3 | 追加尾注（＋A5 统计口径） | `f1b5e49f3058` → `0ad42625f333` | 27,538 → 29,106 |
| 28 | `results/_v4_supp_t15_verdict.md` | L397,432,466 / 4 | 追加尾注（＋A5 统计口径） | `52c985429c91` → `3cb5c2f59961` | 52,884 → 54,377 |
| 29 | `results/_v4_supp_t15r2_verdict.md` | L389,426,458 / 4 | 追加尾注（＋A5 统计口径） | `8355724a26e3` → `963725dbd82a` | 64,145 → 65,638 |

### §1.3 追加注记的统一内容（29 件同构）

每件文末追加一块 `<!-- appended-note:2026-09-30 … -->` 标注的引用面，内含四要素：**原引用面**（行号 + 出现次数 + 字面摘）→ **2026-09-30 只读复核结论** → **当前三段式锚**（`plugin:skill` 名 + 树哈希前 12 + `SKILL.md` SHA-12/字节 + 定位方式）→ **执行件指针与署名**。按件附加的专属条款：

- **B 类 8 件**：＋「对外件口径」（建议 A1 风险仍成立，附注仅供内部对账、**未随原件对外发出**）；其中 2 件 ＋「树哈希口径」（树哈希 = 打包哈希 ≠ `SKILL.md` 哈希，建议 A4）。
- **实录失败件 6 件**（#19–21、#24、#25 及 #26 族）：复核结论为「**失败 ≠ 盘上缺失**；失败成因本棒未定位、**0 断言**」。
- **条件句 4 件**（#26–29）：＋「统计口径（防误读）」——本件内 `Local skill not found` 为**条件句（「若实录」）**，**不得计为实测失败**（建议 A5）。
- **A6 件 1 件**（#18）：勘误尾注，指向依据件 §1 E-01，并声明本件 SHA-12 已变更（原 `2fb5987f544d`）。
- **反向情形 1 件**（#23）：「Mavis plugin-cache sha256（不适用）」经复核**无过期值可改**。

### §1.4 C 类 · 19 件冻结产出物（跳过 · 0 改动 · SHA-12 与字节为「跳过后」实测值）

| # | 件 | SHA-12（未变） | 字节 | 跳过理由 |
|---|---|---|---|---|
| 30 | `results/_v3_recheck_12_jsv_phase_data_2026_09_27.json` | `642582d4fbd1` | 17,718 | 冻结产出物：`resolved_path` 字段随产出冻结 |
| 31 | `results/_v3_recheck_08b_executor/executor_2026_09_27.py` | `b292410d9a69` | 43,901 | 冻结产出物：源码注释内嵌缩写路径 |
| 32 | `results/_v3_recheck_08b_executor/result_2026_09_27.json` | `f9a7fa2d65b1` | 88,052 | 冻结产出物：`loaded_path` 字段 |
| 33 | `results/_v4_supp_t1_executor.py` | `91b8f70e4e18` | 60,563 | 冻结产出物：源码内嵌树哈希 |
| 34 | `results/_v4_supp_t1_result.json` | `d6cb03a4657e` | 82,365 | 冻结产出物：`skill_absence_fallback` 字段 |
| 35 | `results/_v4_supp_t15_executor.py` | `558e635f9ba6` | 62,285 | 同上 |
| 36 | `results/_v4_supp_t15_executor_r1_2026_09_27.py` | `6d22444c65af` | 67,517 | 同上 |
| 37 | `results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py` | `9e89e021ea03` | 70,056 | 同上 |
| 38 | `results/_v4_supp_t15_executor_r3_2026_09_28.py` | `b86cce242abe` | 70,056 | 同上 |
| 39 | `results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py` | `7da23c0e94cf` | 66,317 | 同上 |
| 40 | `results/_v4_supp_t15_result.json` | `6b47d389b7ae` | 53,265 | 同上 |
| 41 | `results/_v4_supp_t15r2_executor.py` | `4b5b720d5cda` | 84,884 | 同上 |
| 42 | `results/_v4_supp_t15r2_executor_r1_2026_09_28.py` | `e0936a68fa82` | 90,390 | 同上 |
| 43 | `results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py` | `215db16a0556` | 92,915 | 同上 |
| 44 | `results/_v4_supp_t15r2_executor_r3_2026_09_28.py` | `4f514b3fb4b8` | 92,915 | 同上 |
| 45 | `results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py` | `678032f726a8` | 89,083 | 同上 |
| 46 | `results/_v4_supp_t15r2_result.json` | `c69ab0e3002e` | 73,526 | 同上 |
| 47 | `results/_v4_pi_cot_v2_ruleset_executor.py` | `48dca1d4281c` | 39,281 | 冻结产出物：docstring 内嵌树哈希 |
| 48 | `results/_v4_pi_cot_v2_ruleset_v2_executor.py` | `eb22f13d571c` | 52,465 | 同上 |

### §1.5 ④ 计数

| 处置 | 件数 | 说明 |
|---|---|---|
| **就地更新** | **0** | 47/48 字面经复核仍成立 ⇒ **无过期值可改**；唯一过期注记按实录件惯例走追加勘误 |
| **追加注记** | **29** | 对外件 8 ＋ 内部文字件 21 |
| **跳过（0 改动）** | **19** | 冻结产出物 14 `.py` ＋ 5 `.json` |
| 合计 | **48** | 与依据件 §3.1 的 48 件文字件**逐件对得上** |

---

## §2 ⑥ 用户面 223 项可解析性普查

### §2.1 普查口径（本棒自定义，逐项登记）

| 维度 | 三态定义 | 计数 |
|---|---|---|
| **结构面** | **可解析** = 目录存在 ＋ `SKILL.md` 存在 ＋ 可解 UTF-8 ＋ frontmatter 闭合 ＋ 含 `name` ＋ 含 `description` ＝ 具备被解析的**最低结构条件**；**不可解析** = 上列任一不满足 | **可解析 223 / 不可解析 0 / 未测 0** |
| **调用面** | **可解析** = 运行时加载器实测成功；**不可解析** = 实测返回失败；**未测** = 本棒**未做该实测** | **可解析 0 / 不可解析 0 / 未测 223** |

> ⚠️ **两维度不可混读**：「结构面可解析」**不等于**「运行时能加载」。§2.2 的结构面 223/223 与 §2.3 的调用面 0 次实测是**两件事**，本件**不以前者冒认后者**。

### §2.2 逐项普查（全量 223 项 · 逐项明细见附录 A）

| 指标 | 本棒实测 |
|---|---|
| 目录数 | **223**（`.minimax\skills\` 下 0 缺 `SKILL.md`） |
| `SKILL.md` 合计字节 | **3,215,448** B |
| 编码 | **223/223 严格 UTF-8 可解**；**0 BOM**、**0 CRLF** |
| frontmatter | **223/223 闭合**、**223/223 含 `name`**、**223/223 含 `description`** ⇒ **结构面 0 异常** |
| `name` == 目录名 | **201 / 223** |
| `name` 为 YAML 引号值 | **1**（`prd-to-prototype` → `"PRD to Prototype"`，去引号后仍 ≠ 目录名） |
| `name` 实质 ≠ 目录名 | **21**（大小写/中文命名：见 §2.4） |
| **同名存在于 plugin-cache 面** | **10**（与依据件 §2.2 逐件同值） |
| **同名存在于 `.builtin-skills` 面** | **5**（`deep-research` `docx` `pdf` `pptx` `xlsx`）——**依据件未记此面，本棒新增** |
| **三面同名（三重遮蔽）** | **4**（`docx` `pdf` `pptx` `xlsx`：用户面 ＋ plugin-cache ＋ builtin 三面各有同名目录） |

### §2.3 调用面：本棒为何 0 次实测（诚实交代 · 不以沉默充作「无变化」）

- 派工单要求「可调用面按拟用写法**实测解析**（严格串行、每次仅 1 次调用、间隔 ≥1s、总计受控）」。
- **本棒工具面内不存在 skill 加载器**：本棒可用工具为 `Read` / `Write` / `Edit` / `Bash` / `Grep` / `Glob` / `web_fetch` / `mcp_invoke` / `excel_editor` / `word_editor` / 任务与部署类，**无任何 skill 装载入口**。
- 因此 **223 项调用面一律记「未测」**：**0 次加载、0 次解析调用、0 次网络请求**，**未复现也未否证**依据件 §2 的 18 例对照结果（该 18 例系**他棒实测**，本棒**仅引用不冒认**）。
- **拟用写法**（供后续棒直接沿用，本棒只读登记）：依据件 §2 实测的两种形态为 `plugin:skill` 限定名（**0/10 成功**）与**裸名**（同名双份 5/5 成功、plugin-cache 独有 0/2 失败）⇒ **本项目拟用写法 = 裸名**。
- **成本边界**：即便具备加载器，223 项全量实测亦须**串行 × ≥1s 间隔**（≈ 4 分钟下限）；本棒建议后续**按需抽样**而非全量，并沿用「串行 · 单次 · ≥1s」纪律。

### §2.4 三态分布与定位面

| 定位面 | 件数 | 说明 |
|---|---|---|
| 用户面 `.minimax\skills\` | **223** | 全部 223 项的**所在面** |
| ＋ plugin-cache 同名 | **10** | 遮蔽风险面：`docx` `hypothesis-generation` `pdf` `peer-review` `pptx` `scholar-evaluation` `scientific-brainstorming` `scientific-writing` `statistical-analysis` `xlsx`（10/10 内容不同，SHA-12 与字节逐件与依据件同值） |
| ＋ builtin 同名 | **5** | `deep-research` `docx` `pdf` `pptx` `xlsx`（其中 4 项为**三面同名**） |
| ＋ plugin-cache 独有（用户面无同名） | — | 含 `experimental-design`、`academic-paper-polish` 等关键 skill ⇒ **用户面 0 命中**，故其解析面**不在本普查范围内** |

**`name` ≠ 目录名 21 项**（结构面「可解析」但**按裸名寻址可能落空**的候选面）：`abstract-writing`→`Abstract Writing`、`academic-paper-writing-expert-zip`→`论文写作专家`、`antimicrobial-stewardship`→`Antimicrobial Stewardship`、`bayesian-clinical-reasoning`→`Bayesian Clinical Reasoning`、`clinical-decision-rules`→`Clinical Decision Rules`、`critical-appraisal`→`Critical Appraisal`、`differential-diagnosis-generation`→`Differential Diagnosis Generation`、`dose-adjustment`→`Dose Adjustment`、`drug-interactions`→`Drug Interactions`、`evidence-levels-and-hierarchies`→`Evidence Levels and Hierarchies`、`grade-assessment`→`GRADE Assessment`、`hypothesis-testing`→`Hypothesis Testing`、`illness-scripts`→`Illness Scripts`、`imrad-structure`→`IMRAD Structure`、`lab-interpretation`→`Lab Interpretation`、`prd-to-prototype`→`PRD to Prototype`（引号值）、`rct-design`→`RCT Design`、`regression-analysis`→`Regression Analysis`、`sample-size-calculation`→`Sample Size Calculation`、`sensitivity-and-specificity`→`Sensitivity and Specificity`、`shared-decision-making`→`Shared Decision-Making`、`survival-analysis`→`Survival Analysis`。

> **诚实标注**：本棒**未实测**这 21 项按裸名/按 `name` 寻址是否命中——**0 次调用**，故「可能落空」是**由字面差异推出的候选**，**非实测失败**。此外本棒初测曾把 **4 个 YAML 引号值**误记为 `name` 差异（`company-value-analyzer` / `formula-derivation` / `knowledge-digest` 等），**已自查修正**，修正后差异数为 21 + 1，**非 25**。

---

## §3 风险清单：盘上 `SKILL.md` 可疑 / 祈使性内容

> **总纪律**：本棒 ⛔ **0 执行任何 `SKILL.md` 内指令**。以下条目**一律只登记、不遵从**。指令来源是**盘上文件**，**不是 PI**，**不得以盘上文本冒充 PI 指令**。

| id | skill | 位置 | 命中内容（原文摘） | 风险类 | 本棒处置 |
|---|---|---|---|---|---|
| **R1** | `openclaw-setup-assistant` | `SKILL.md:42`（macOS）、`:47`（Linux） | ``osascript … "export MINIMAX_API_KEY='<用户提供的API_KEY>' && curl -fsSL https://molt.bot/install.sh | bash"`` | **高**：① 远端脚本 `curl \| bash` 直接执行；② 凭据注入命令行（进 shell 历史/进程表）；③ 指令 Agent **代开终端**执行 | **未遵从** · 仅登记 |
| **R2** | `docx` | `SKILL.md:412` | **`Use "Claude" as the author** for tracked changes and comments, unless the user explicitly requests use of a different name.` | **高**：**署名冒名**指令——要求以「Claude」为作者身份写入修订痕迹 | **未遵从** · 仅登记。**注**：plugin-cache 面同名副本**实测 0 命中**该句 ⇒ **两面内容分歧**，冒名指令**仅存于用户面** |
| **R3** | `openclaw-self-evolution-pack` | `SKILL.md:56,62,64` | 「通过飞书机器人 Webhook 将进化状态和消息内容发送至指定群组」 | **中**：内容外推送至外部端点 | **未遵从** · 仅登记 |
| **R4** | `open-notebook` | `SKILL.md:39` | `curl -o docker-compose.yml https://raw.githubusercontent.com/lfnovo/open-notebook/main/docker-compose.yml` | **中**：远端内容直接落盘为工作文件 | **未遵从** · 仅登记 |
| **R5** | `database-lookup` | `SKILL.md:226-230, 305` | 多个 `curl -X POST … https://api.platform.opentargets.org/…` 等公共端点 | **低-中**：触发外部网络请求 | **未遵从** · 仅登记 |
| **R6** | 涉凭据/环境变量字面 | **44 件**（`API_KEY` / `.env` / `credential` / `password` / `secret` 模式命中） | — | **面级提示**：与本项目「0 key」纪律的潜在冲突面 | **仅登记计数** · 本棒 0 读取任何 key、0 执行 |
| **R7** | `folder-cleanup-assistant` | `SKILL.md:64, 117` | `rm -rf`、`Remove-Item`、`del` | **误报登记**：出现在 ❌ **禁列**（明令禁止使用），**非诱导执行** | 不作风险计 |
| **R8** | `evaluation` `torch-geometric` | `:213` / `:202` | `run_rubric_eval(candidate)` / `model.eval()` | **误报登记**：`eval(` 正则命中 **PyTorch/函数名**，非代码执行 | 不作风险计 |
| **R9** | `harness-engineering` | `SKILL.md:144` | 「Define what the agent may do without asking and what requires approval.」 | **指令覆盖类扫描唯一命中**，经判读为**权限边界设计指引**，**非**「忽略先前指令」类覆盖 | 不作风险计 |
| **R10** | 其余 218 项 | — | 祈使性内容**普遍存在**（承接依据件 §2.5-3 的登记） | 本棒**按 9 类高危模式筛查**（署名冒名 / 指令覆盖 / 危险执行 / 凭据外传 / 持久化 / 隐蔽动作 / 端点外送 / 破坏性命令 / 遮蔽冲突） | **未逐条判「可遵从性」** —— 诚实记为**筛查非穷尽** |

**扫描口径**：仅 `grep` 只读检索 223 件 `SKILL.md` 的**字面命中**；**未执行、未加载、未验签、未做语义级风险评级**。

---

## §4 诚实边界（不夸大 · 不误导）

1. **④ 未做「就地更新」**：0 件。因 **47/48 字面经本棒复核仍成立**，**无过期值可改**——若强行「更新」即为**无对象的改动**。此为**明示取舍**，非漏做。
2. **④ 改变了 29 件的 SHA-12**：追加注记必然改变文件哈希。**引用这 29 件旧 SHA-12 的其他件可能失配**，故 §1.2 同时登记**前后双值**。本棒**未回改任何引用他件的这 29 处哈希**（超出本棒授权面）——**是否需要另出哈希勘误，待 PI 拍板**。
3. **④ 一处已修复的写入缺陷（如实登记，不掩盖）**：首轮追加时，本棒以「末字节是否 CR」判换行风格，致 **CRLF 风格的** `results/_v3_v4_achievements_inventory_2026_09_24.md` **被追加为 LF**（cr=1914 / lf=1925，混合）。**自核时检出**（非事后掩盖）⇒ 已**截回原长 192,292 B 并复算哈希 `2fb5587…`→`2fb5987f544d` 校验通过**后改以 CRLF 重写，现 **cr=1925 / lf=1925 均匀、0 BOM、前缀逐字节一致**。最终 SHA-12 `189ba84fc12e`。**该件的中间态哈希 `3b4a1d4e83bd` 作废，不应被引用。**
4. **④ 追加注记的版式瑕疵（如实登记）**：PowerShell 双引号 here-string 对反引号的转义，使少数注记行内的**行内代码标记（`` ` ``）被吞**，文字语义不受影响，但**该几行不呈现为代码样式**。历史字面**未受影响**。
5. **⑥ 调用面 0 次实测**：本棒**无 skill 加载工具面**（§2.3）。**223 项调用面全记「未测」**；**未复现、未否证**依据件 §2 的 18 例，**0 冒认**。**「结构面 223/223 可解析」不可被读作「223 项都能加载」**。
6. **⑥ 筛查非穷尽**：§3 风险清单基于 **9 类模式的字面筛查**，**0 逐条判可遵从性**、**0 验签**、**0 语义级风险评级**。**未命中不等于安全**。
7. **⑥ 「三面遮蔽」为盘上事实，不含成因判断**：本棒登记 `docx`/`pdf`/`pptx`/`xlsx` **三面同名**这一**事实**，**不判定**加载器如何取舍、**不判定**哪一面更权威。
8. **0 配置改动**：`config.yaml`、`mcp.json`、`plugin.json`、`skill-hub.json` **一律未读未写**（含敏感值文件回避）。
9. **0 skill 目录改动**：`.minimax\skills\`、plugin-cache、`.builtin-skills\` **全部只读**，**0 写入、0 移动、0 重命名**。
10. **0 二进制触动**：`.evidence_backup_2026_09_28/runtime-state.sqlite`（依据件单列的二进制件）**不在 48 件文字件内**，本棒**0 读写**。
11. **写入面**：本件 1 件（新建）＋ §1.2 表列 **29 件追加**；`results/` `docs/` `letters/` `deposon_team/` 内**0 删除、0 重命名、0 覆写**。
12. **未读加载器实现、未读更新日志 / changelog / 版本号**，故**不回答「为什么失败」**——④ 中 6 件实录失败件，**失败成因本棒 0 定位、0 断言**。
13. **本件自身 SHA-12 不可内嵌**（自引用悖论）——落盘后由 parent 对终态复算并回填回执。
14. **署名如实**：出件为 **worker**（本棒），**不冒认**他方名头；依据件 §2 的 18 例加载结论**明确标注为他棒实测**。

---

## §5 自核节

- **编码 / 版式**：UTF-8 **无 BOM** · **LF**（0 CRLF）——落盘后**实测**核验，**不预填**。
- **哈希口径**：一律 `Get-FileHash -Algorithm SHA256`，全值算完**截前 12**；**非** SHA-1 冒充。
- **0 删改自证（强证）**：对 29 件逐一**取新文件的前「原字节数」字节重算 SHA-12**，与追加前实测值比对 ⇒ **29/29 逐字一致**（含 1 件 CRLF 修复件）。即：**既有字节 0 改动**为**密码学可证**，非仅凭声明。
- **未变更自证**：§1.4 的 19 件冻结产出物，SHA-12 与字节在追加操作**前后完全一致**（本棒 0 写入）。
- **撞名实测**：落名前 **2 轮 × 4 目录** 全部 `exists=False`，全仓递归近名 glob 仅命中依据件本身。
- **succeeded ≠ 跑完**：本棒一次写入失败（`FileStream.Write` 重载在 PS 5.1 不可用）**已如实登记并复核**——失败后立即做 8 件完整性复算（`changed=0`，证明失败尝试**未写入任何字节**），修正重参数后重跑。§4-3 的 CRLF 缺陷同样**检出—修复—复验**，两处均登记在案。
- **0 凭据**：本件不含任何密钥 / token / 端点；**0 LLM 调用、0 API 调用、0 外部 URL**。
- **V1–V3 只读**：未触动任何 V1–V3 资产。
- **本件自身 SHA-12 / 字节 / 行数**：由 parent **落盘后对终态复算**并回填回执（自引用不可内嵌，见 §4-13）。

<!-- self-check-tail -->

---

## §6 交叉引用校正（parent 协调令 · 2026-09-30 · 仅追加不删改）

**校正事项**：④ 第 18 件（`results/_v3_v4_achievements_inventory_2026_09_24.md`）的追加注记与本件 §1.3，原将「正式勘误」指向依据件 `644e0666fbc4` §1 E-01。PI 裁「六项全办之①**拆件**」后，**独立勘误件已拆出**。

| 项 | 值 |
|---|---|
| **正式勘误权威落点** | `results/_skill_erratum_and_parent_success_note_2026_09_30.md`（`7a64949402d9`）**§1 E-01** |
| 草案位（历史，**不删改**） | `results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md`（`644e0666fbc4`）§1 |
| 本棒校正动作 | 于上述第 18 件**文末追加一行**校正说明（0 删改已追加行）；本件以本节登记该口径 |

**本棒独立核验**（不转述）：拆件存在 ✅；实测 SHA-12 = `7a64949402d9` ✅（24,143 B）；其 §1 标题逐字为「独立勘误登记（PI 第①项 · 自 `644e0666fbc4` §1 拆出）」✅，含 E-01 ✅。

> **口径效力**：凡引用「A6 正式勘误」处，**一律以拆件 `7a64949402d9` §1 为准**；`644e0666fbc4` §1 为**草案位（历史）**，仅作沿革留痕。本件 §1.2 第 18 行与 §1.3 中「指向依据件 §1 E-01」之表述**以本节为准**，**历史表述保留不删改**。

---

## 附录 A · 223 项逐项普查表（全量 · 机器生成 · 未手工转录）

**列义**：`结构面` = 具备被解析的最低结构条件（目录 + `SKILL.md` + 可解 UTF-8 + frontmatter 闭合 + 含 `name`/`description`）；`调用面` = 运行时加载实测——**本棒 0 次实测**（§2.3），故 223/223 记「未测」。`定位面` 中 `用户面` 为所在面，`＋PC` = 同名亦存在于 plugin-cache 面，`＋BI` = 同名亦存在于 `.builtin-skills` 面。

| # | 项名（目录） | `SKILL.md` 字节 | `SKILL.md` SHA-12 | frontmatter `name` | name==目录 | 定位面 | 结构面 | 调用面 |
|---|---|---|---|---|---|---|---|---|
| 1 | `abstract-writing` | 10157 | `df2f2ef27bcb` | `Abstract Writing` | 否 | 用户面 | 可解析 | 未测 |
| 2 | `academic-paper-writing-expert-zip` | 5836 | `5d43b2911ca3` | `论文写作专家` | 否 | 用户面 | 可解析 | 未测 |
| 3 | `academic-researcher` | 8396 | `c85bce2c486e` | `academic-researcher` | 是 | 用户面 | 可解析 | 未测 |
| 4 | `adaptyv` | 3741 | `1d236003aaca` | `adaptyv` | 是 | 用户面 | 可解析 | 未测 |
| 5 | `advanced-evaluation` | 16990 | `8b9e3d9de07a` | `advanced-evaluation` | 是 | 用户面 | 可解析 | 未测 |
| 6 | `adversarial-proof-review` | 4837 | `c14a03e6ec2c` | `adversarial-proof-review` | 是 | 用户面 | 可解析 | 未测 |
| 7 | `aeon` | 10586 | `487327ddbde7` | `aeon` | 是 | 用户面 | 可解析 | 未测 |
| 8 | `agent-safety` | 2318 | `ed6b5c615219` | `agent-safety` | 是 | 用户面 | 可解析 | 未测 |
| 9 | `anndata` | 10213 | `801ad688e978` | `anndata` | 是 | 用户面 | 可解析 | 未测 |
| 10 | `antimicrobial-stewardship` | 10978 | `82c44fe80005` | `Antimicrobial Stewardship` | 否 | 用户面 | 可解析 | 未测 |
| 11 | `arboreto` | 6928 | `c87ae2497058` | `arboreto` | 是 | 用户面 | 可解析 | 未测 |
| 12 | `arxiv-search` | 1007 | `403df19c354a` | `arxiv-search` | 是 | 用户面 | 可解析 | 未测 |
| 13 | `astropy` | 11533 | `94debbfcc5ba` | `astropy` | 是 | 用户面 | 可解析 | 未测 |
| 14 | `b2b-lead-engine` | 33382 | `1e9ad808bc20` | `b2b-lead-engine` | 是 | 用户面 | 可解析 | 未测 |
| 15 | `bayesian-clinical-reasoning` | 7360 | `264e28ab2a2a` | `Bayesian Clinical Reasoning` | 否 | 用户面 | 可解析 | 未测 |
| 16 | `bdi-mental-states` | 17738 | `2a68bf11815b` | `bdi-mental-states` | 是 | 用户面 | 可解析 | 未测 |
| 17 | `benchling-integration` | 13062 | `4305f084ed93` | `benchling-integration` | 是 | 用户面 | 可解析 | 未测 |
| 18 | `bgpt-paper-search` | 2478 | `fb3000067bda` | `bgpt-paper-search` | 是 | 用户面 | 可解析 | 未测 |
| 19 | `biopython` | 13828 | `8865f5f5727c` | `biopython` | 是 | 用户面 | 可解析 | 未测 |
| 20 | `bioservices` | 9946 | `5d0a296c1284` | `bioservices` | 是 | 用户面 | 可解析 | 未测 |
| 21 | `book-sft-pipeline` | 14242 | `4079f17b32dd` | `book-sft-pipeline` | 是 | 用户面 | 可解析 | 未测 |
| 22 | `career-future-mirror` | 35152 | `83b6585c3e98` | `career-future-mirror` | 是 | 用户面 | 可解析 | 未测 |
| 23 | `cellxgene-census` | 15438 | `d088087c45f2` | `cellxgene-census` | 是 | 用户面 | 可解析 | 未测 |
| 24 | `cirq` | 10647 | `eab8268df2e6` | `cirq` | 是 | 用户面 | 可解析 | 未测 |
| 25 | `citation-management` | 32594 | `a5f786d9dac0` | `citation-management` | 是 | 用户面 | 可解析 | 未测 |
| 26 | `claim-lifecycle` | 3822 | `12112ceacc74` | `claim-lifecycle` | 是 | 用户面 | 可解析 | 未测 |
| 27 | `clickhouse-best-practices` | 7785 | `e338755220c1` | `clickhouse-best-practices` | 是 | 用户面 | 可解析 | 未测 |
| 28 | `clinical-decision-rules` | 6455 | `932e8265d78d` | `Clinical Decision Rules` | 否 | 用户面 | 可解析 | 未测 |
| 29 | `clinical-decision-support` | 26495 | `b2788d90e888` | `clinical-decision-support` | 是 | 用户面 | 可解析 | 未测 |
| 30 | `clinical-reports` | 39694 | `f076bddfe087` | `clinical-reports` | 是 | 用户面 | 可解析 | 未测 |
| 31 | `cobrapy` | 12449 | `e8552de3c4b8` | `cobrapy` | 是 | 用户面 | 可解析 | 未测 |
| 32 | `company-value-analyzer` | 41024 | `f277f9d7557c` | `company-value-analyzer` | 是 | 用户面 | 可解析 | 未测 |
| 33 | `comprehensive-research-agent` | 8532 | `c9314da5df61` | `comprehensive-research-agent` | 是 | 用户面 | 可解析 | 未测 |
| 34 | `conjecture-testing` | 5549 | `03971ba56bff` | `conjecture-testing` | 是 | 用户面 | 可解析 | 未测 |
| 35 | `consciousness-council` | 8728 | `e77f05328526` | `consciousness-council` | 是 | 用户面 | 可解析 | 未测 |
| 36 | `context-compression` | 18214 | `c4111db0514e` | `context-compression` | 是 | 用户面 | 可解析 | 未测 |
| 37 | `context-degradation` | 19180 | `4e1896f641dd` | `context-degradation` | 是 | 用户面 | 可解析 | 未测 |
| 38 | `context-fundamentals` | 17013 | `03b56e1c40ed` | `context-fundamentals` | 是 | 用户面 | 可解析 | 未测 |
| 39 | `context-optimization` | 15667 | `8cecc30872ec` | `context-optimization` | 是 | 用户面 | 可解析 | 未测 |
| 40 | `critical-appraisal` | 8559 | `045fc825f5d5` | `Critical Appraisal` | 否 | 用户面 | 可解析 | 未测 |
| 41 | `cross-pollination-ideation` | 7210 | `3a537ee5a2dc` | `cross-pollination-ideation` | 是 | 用户面 | 可解析 | 未测 |
| 42 | `dask` | 14302 | `835c8ffa4e56` | `dask` | 是 | 用户面 | 可解析 | 未测 |
| 43 | `database-lookup` | 29276 | `dfae260889df` | `database-lookup` | 是 | 用户面 | 可解析 | 未测 |
| 44 | `datamol` | 18866 | `f685a3161099` | `datamol` | 是 | 用户面 | 可解析 | 未测 |
| 45 | `deepchem` | 17782 | `b752f9ae0fb9` | `deepchem` | 是 | 用户面 | 可解析 | 未测 |
| 46 | `deep-research` | 6995 | `5637feab59dc` | `deep-research` | 是 | 用户面 ＋BI | 可解析 | 未测 |
| 47 | `deeptools` | 17984 | `3a4333652d60` | `deeptools` | 是 | 用户面 | 可解析 | 未测 |
| 48 | `denario` | 5999 | `4fce63da211a` | `denario` | 是 | 用户面 | 可解析 | 未测 |
| 49 | `depmap` | 11277 | `3bd80d251776` | `depmap` | 是 | 用户面 | 可解析 | 未测 |
| 50 | `dep-updates` | 5164 | `e3fccc6698e6` | `dep-updates` | 是 | 用户面 | 可解析 | 未测 |
| 51 | `dhdna-profiler` | 10081 | `52d86523c69f` | `dhdna-profiler` | 是 | 用户面 | 可解析 | 未测 |
| 52 | `diffdock` | 15486 | `c4552b289589` | `diffdock` | 是 | 用户面 | 可解析 | 未测 |
| 53 | `differential-diagnosis-generation` | 6589 | `be1eae5a640d` | `Differential Diagnosis Generation` | 否 | 用户面 | 可解析 | 未测 |
| 54 | `digital-brain` | 7028 | `e66ece9e2b0f` | `digital-brain` | 是 | 用户面 | 可解析 | 未测 |
| 55 | `dnanexus-integration` | 10649 | `24b1fe38f7d3` | `dnanexus-integration` | 是 | 用户面 | 可解析 | 未测 |
| 56 | `docx` | 20084 | `cfbabd72b1ae` | `docx` | 是 | 用户面 ＋PC ＋BI（三面同名） | 可解析 | 未测 |
| 57 | `dose-adjustment` | 10333 | `6c47d038348f` | `Dose Adjustment` | 否 | 用户面 | 可解析 | 未测 |
| 58 | `drug-interactions` | 8893 | `4b071debe144` | `Drug Interactions` | 否 | 用户面 | 可解析 | 未测 |
| 59 | `esm` | 10561 | `994175f14e3a` | `esm` | 是 | 用户面 | 可解析 | 未测 |
| 60 | `etetoolkit` | 17883 | `a19f4eeb1a0c` | `etetoolkit` | 是 | 用户面 | 可解析 | 未测 |
| 61 | `evaluation` | 16829 | `1f31cda0910d` | `evaluation` | 是 | 用户面 | 可解析 | 未测 |
| 62 | `evidence-contract` | 3921 | `e7fd7b39c22f` | `evidence-contract` | 是 | 用户面 | 可解析 | 未测 |
| 63 | `evidence-levels-and-hierarchies` | 8499 | `0064b3a3da96` | `Evidence Levels and Hierarchies` | 否 | 用户面 | 可解析 | 未测 |
| 64 | `exploratory-data-analysis` | 14315 | `305c2dc13435` | `exploratory-data-analysis` | 是 | 用户面 | 可解析 | 未测 |
| 65 | `filesystem-context` | 15919 | `bbde98d3481f` | `filesystem-context` | 是 | 用户面 | 可解析 | 未测 |
| 66 | `flowio` | 16771 | `ae294468af76` | `flowio` | 是 | 用户面 | 可解析 | 未测 |
| 67 | `fluidsim` | 9395 | `87dfa817f9d9` | `fluidsim` | 是 | 用户面 | 可解析 | 未测 |
| 68 | `folder-cleanup-assistant` | 4470 | `9c5b1d8b8b8e` | `folder-cleanup-assistant` | 是 | 用户面 | 可解析 | 未测 |
| 69 | `formula-derivation` | 7092 | `74497d832850` | `formula-derivation` | 是 | 用户面 | 可解析 | 未测 |
| 70 | `generate-image` | 7047 | `bb22bdd7dee9` | `generate-image` | 是 | 用户面 | 可解析 | 未测 |
| 71 | `geniml` | 10091 | `f127f95b25dd` | `geniml` | 是 | 用户面 | 可解析 | 未测 |
| 72 | `geomaster` | 12109 | `457bccd89900` | `geomaster` | 是 | 用户面 | 可解析 | 未测 |
| 73 | `geopandas` | 7116 | `54a88f69dc2d` | `geopandas` | 是 | 用户面 | 可解析 | 未测 |
| 74 | `get-available-resources` | 9836 | `72c408667935` | `get-available-resources` | 是 | 用户面 | 可解析 | 未测 |
| 75 | `gget` | 25087 | `8cc35df81f28` | `gget` | 是 | 用户面 | 可解析 | 未测 |
| 76 | `gif-sticker-generator` | 10264 | `a3dcc519b256` | `gif-sticker-generator` | 是 | 用户面 | 可解析 | 未测 |
| 77 | `ginkgo-cloud-lab` | 3469 | `cb52652c0d44` | `ginkgo-cloud-lab` | 是 | 用户面 | 可解析 | 未测 |
| 78 | `glycoengineering` | 12462 | `f36b189b9860` | `glycoengineering` | 是 | 用户面 | 可解析 | 未测 |
| 79 | `grade-assessment` | 10287 | `433d22b9a7b5` | `GRADE Assessment` | 否 | 用户面 | 可解析 | 未测 |
| 80 | `gtars` | 7805 | `b28fd4344008` | `gtars` | 是 | 用户面 | 可解析 | 未测 |
| 81 | `harness-engineering` | 11413 | `dde3d8f46d4d` | `harness-engineering` | 是 | 用户面 | 可解析 | 未测 |
| 82 | `histolab` | 20151 | `6e2cf72fb7e1` | `histolab` | 是 | 用户面 | 可解析 | 未测 |
| 83 | `hosted-agents` | 17717 | `4786dad600b0` | `hosted-agents` | 是 | 用户面 | 可解析 | 未测 |
| 84 | `html-presentation-generator` | 42732 | `d22e3329c08c` | `html-presentation-generator` | 是 | 用户面 | 可解析 | 未测 |
| 85 | `hypogenic` | 21653 | `4daee607df82` | `hypogenic` | 是 | 用户面 | 可解析 | 未测 |
| 86 | `hypothesis-generation` | 13846 | `6e15fe44f5a4` | `hypothesis-generation` | 是 | 用户面 ＋PC | 可解析 | 未测 |
| 87 | `hypothesis-testing` | 10303 | `d90e2931c854` | `Hypothesis Testing` | 否 | 用户面 | 可解析 | 未测 |
| 88 | `icon-maker` | 10516 | `9e03bd0f35f5` | `icon-maker` | 是 | 用户面 | 可解析 | 未测 |
| 89 | `illness-scripts` | 7912 | `0ddcdce71091` | `Illness Scripts` | 否 | 用户面 | 可解析 | 未测 |
| 90 | `image-creator` | 16958 | `108661c3b11b` | `image-creator` | 是 | 用户面 | 可解析 | 未测 |
| 91 | `imaging-data-commons` | 34425 | `64053e6a770c` | `imaging-data-commons` | 是 | 用户面 | 可解析 | 未测 |
| 92 | `imrad-structure` | 10931 | `91838e6c1a30` | `IMRAD Structure` | 否 | 用户面 | 可解析 | 未测 |
| 93 | `inbox-parser` | 4310 | `14d4f362ca7c` | `inbox-parser` | 是 | 用户面 | 可解析 | 未测 |
| 94 | `industry-research-report` | 27177 | `82e4eca9d1b2` | `industry-research-report` | 是 | 用户面 | 可解析 | 未测 |
| 95 | `infographics` | 18071 | `f178bf7856b0` | `infographics` | 是 | 用户面 | 可解析 | 未测 |
| 96 | `investment-research-analyst` | 30324 | `34ac4ffb3d1b` | `investment-research-analyst` | 是 | 用户面 | 可解析 | 未测 |
| 97 | `iso-13485-certification` | 23248 | `5e1265308aca` | `iso-13485-certification` | 是 | 用户面 | 可解析 | 未测 |
| 98 | `knowledge-digest` | 25104 | `ff270a2d610a` | `knowledge-digest` | 是 | 用户面 | 可解析 | 未测 |
| 99 | `labarchive-integration` | 9442 | `6c68dca6355d` | `labarchive-integration` | 是 | 用户面 | 可解析 | 未测 |
| 100 | `lab-interpretation` | 9250 | `5e00bc476b01` | `Lab Interpretation` | 否 | 用户面 | 可解析 | 未测 |
| 101 | `lamindb` | 14369 | `8300681fa08f` | `lamindb` | 是 | 用户面 | 可解析 | 未测 |
| 102 | `landing-page-generator` | 8296 | `e6ad4158f4f1` | `landing-page-generator` | 是 | 用户面 | 可解析 | 未测 |
| 103 | `latchbio-integration` | 9815 | `e5fbce2abdfa` | `latchbio-integration` | 是 | 用户面 | 可解析 | 未测 |
| 104 | `latent-briefing` | 13029 | `d84e7abe51f0` | `latent-briefing` | 是 | 用户面 | 可解析 | 未测 |
| 105 | `latex-posters` | 59800 | `32cae5494fa3` | `latex-posters` | 是 | 用户面 | 可解析 | 未测 |
| 106 | `literature-review` | 23788 | `d0ce8d57aaa8` | `literature-review` | 是 | 用户面 | 可解析 | 未测 |
| 107 | `long-horizon-prompting` | 25666 | `75f8c53453fb` | `long-horizon-prompting` | 是 | 用户面 | 可解析 | 未测 |
| 108 | `marginal-tracker` | 18186 | `ea8778c000e3` | `marginal-tracker` | 是 | 用户面 | 可解析 | 未测 |
| 109 | `markdown-mermaid-writing` | 14888 | `edfa23bfc413` | `markdown-mermaid-writing` | 是 | 用户面 | 可解析 | 未测 |
| 110 | `market-research-reports` | 28742 | `ddeec472dca7` | `market-research-reports` | 是 | 用户面 | 可解析 | 未测 |
| 111 | `markitdown` | 12630 | `7bd6add05a22` | `markitdown` | 是 | 用户面 | 可解析 | 未测 |
| 112 | `matchms` | 7009 | `ac8ed2f7f0c2` | `matchms` | 是 | 用户面 | 可解析 | 未测 |
| 113 | `matlab` | 10044 | `0414644e5d6a` | `matlab` | 是 | 用户面 | 可解析 | 未测 |
| 114 | `matplotlib` | 11453 | `100faa8c78a2` | `matplotlib` | 是 | 用户面 | 可解析 | 未测 |
| 115 | `mckinsey-presentation-generator` | 40319 | `5e56adf71927` | `mckinsey-presentation-generator` | 是 | 用户面 | 可解析 | 未测 |
| 116 | `medchem` | 10152 | `9790fdc38680` | `medchem` | 是 | 用户面 | 可解析 | 未测 |
| 117 | `memory-systems` | 16554 | `9e2b38ffe947` | `memory-systems` | 是 | 用户面 | 可解析 | 未测 |
| 118 | `minimax-docx` | 16366 | `15f4b45ef41b` | `minimax-docx` | 是 | 用户面 | 可解析 | 未测 |
| 119 | `minimax-pdf` | 8624 | `8b0497ddd27d` | `minimax-pdf` | 是 | 用户面 | 可解析 | 未测 |
| 120 | `minimax-xlsx` | 8398 | `4ffb70af6ccd` | `minimax-xlsx` | 是 | 用户面 | 可解析 | 未测 |
| 121 | `ml-paper-writing` | 35572 | `2544fcd5575f` | `ml-paper-writing` | 是 | 用户面 | 可解析 | 未测 |
| 122 | `modal` | 12413 | `2dde37f532b1` | `modal` | 是 | 用户面 | 可解析 | 未测 |
| 123 | `molecular-dynamics` | 14700 | `39610e686445` | `molecular-dynamics` | 是 | 用户面 | 可解析 | 未测 |
| 124 | `molfeat` | 14810 | `b3155763a7e5` | `molfeat` | 是 | 用户面 | 可解析 | 未测 |
| 125 | `multi-agent-patterns` | 18649 | `786ff9345eb4` | `multi-agent-patterns` | 是 | 用户面 | 可解析 | 未测 |
| 126 | `networkx` | 12713 | `9c8fa590462f` | `networkx` | 是 | 用户面 | 可解析 | 未测 |
| 127 | `neurokit2` | 12019 | `330233a77582` | `neurokit2` | 是 | 用户面 | 可解析 | 未测 |
| 128 | `neuropixels-analysis` | 11550 | `ca82a34bb4cb` | `neuropixels-analysis` | 是 | 用户面 | 可解析 | 未测 |
| 129 | `novel-writing-expert` | 3051 | `badd76befdb2` | `novel-writing-expert` | 是 | 用户面 | 可解析 | 未测 |
| 130 | `omero-integration` | 8043 | `1d021d13e4bb` | `omero-integration` | 是 | 用户面 | 可解析 | 未测 |
| 131 | `openclaw-self-evolution-pack` | 2726 | `bf156e00a517` | `openclaw-self-evolution-pack` | 是 | 用户面 | 可解析 | 未测 |
| 132 | `openclaw-setup-assistant` | 11730 | `5344a0f0d37e` | `openclaw-setup-assistant` | 是 | 用户面 | 可解析 | 未测 |
| 133 | `open-notebook` | 10451 | `a8d5cc801b08` | `open-notebook` | 是 | 用户面 | 可解析 | 未测 |
| 134 | `opentrons-integration` | 14720 | `27c87a247fa2` | `opentrons-integration` | 是 | 用户面 | 可解析 | 未测 |
| 135 | `paper-2-web` | 16446 | `994429004860` | `paper-2-web` | 是 | 用户面 | 可解析 | 未测 |
| 136 | `paper-lookup` | 10150 | `a08c1c3999b3` | `paper-lookup` | 是 | 用户面 | 可解析 | 未测 |
| 137 | `parallel-web` | 11656 | `5d3941e6754d` | `parallel-web` | 是 | 用户面 | 可解析 | 未测 |
| 138 | `pathml` | 7366 | `a16f701903ea` | `pathml` | 是 | 用户面 | 可解析 | 未测 |
| 139 | `pdf` | 8072 | `9f78b8359fbd` | `pdf` | 是 | 用户面 ＋PC ＋BI（三面同名） | 可解析 | 未测 |
| 140 | `peer-review` | 23119 | `1a07d4a72406` | `peer-review` | 是 | 用户面 ＋PC | 可解析 | 未测 |
| 141 | `pennylane` | 7396 | `7ad9eb1a8c8f` | `pennylane` | 是 | 用户面 | 可解析 | 未测 |
| 142 | `perplexity-search` | 14084 | `6f42d1777cfd` | `perplexity-search` | 是 | 用户面 | 可解析 | 未测 |
| 143 | `phylogenetics` | 13914 | `ecea8ee3b168` | `phylogenetics` | 是 | 用户面 | 可解析 | 未测 |
| 144 | `plotly` | 7198 | `608e857e4e50` | `plotly` | 是 | 用户面 | 可解析 | 未测 |
| 145 | `polars` | 9430 | `b7839f79ef81` | `polars` | 是 | 用户面 | 可解析 | 未测 |
| 146 | `polars-bio` | 14052 | `496d3cf7a9b6` | `polars-bio` | 是 | 用户面 | 可解析 | 未测 |
| 147 | `pptx` | 9182 | `e5b0df918cbe` | `pptx` | 是 | 用户面 ＋PC ＋BI（三面同名） | 可解析 | 未测 |
| 148 | `pptx-generator` | 7930 | `6eeb36239fde` | `pptx-generator` | 是 | 用户面 | 可解析 | 未测 |
| 149 | `pptx-posters` | 14145 | `155059d3230d` | `pptx-posters` | 是 | 用户面 | 可解析 | 未测 |
| 150 | `prd-to-prototype` | 9923 | `8fda2384b597` | `PRD to Prototype` | 否 | 用户面 | 可解析 | 未测 |
| 151 | `primekg` | 3821 | `1dc8be0176c5` | `primekg` | 是 | 用户面 | 可解析 | 未测 |
| 152 | `project-development` | 18960 | `acfeda3048cf` | `project-development` | 是 | 用户面 | 可解析 | 未测 |
| 153 | `proof-writer` | 7594 | `6d7b3094711f` | `proof-writer` | 是 | 用户面 | 可解析 | 未测 |
| 154 | `protocolsio-integration` | 14899 | `f7d45c56cce4` | `protocolsio-integration` | 是 | 用户面 | 可解析 | 未测 |
| 155 | `pufferlib` | 13500 | `736d917b1a67` | `pufferlib` | 是 | 用户面 | 可解析 | 未测 |
| 156 | `pydeseq2` | 16165 | `1a4875f66800` | `pydeseq2` | 是 | 用户面 | 可解析 | 未测 |
| 157 | `pydicom` | 13188 | `4ff0bc8b41d1` | `pydicom` | 是 | 用户面 | 可解析 | 未测 |
| 158 | `pyhealth` | 17652 | `86d66ea09565` | `pyhealth` | 是 | 用户面 | 可解析 | 未测 |
| 159 | `pylabrobot` | 8193 | `d78a82ad4c0d` | `pylabrobot` | 是 | 用户面 | 可解析 | 未测 |
| 160 | `pymatgen` | 20033 | `57ff1b1bf0f8` | `pymatgen` | 是 | 用户面 | 可解析 | 未测 |
| 161 | `pymc` | 15779 | `abee8e33c64d` | `pymc` | 是 | 用户面 | 可解析 | 未测 |
| 162 | `pymoo` | 16752 | `37571351035e` | `pymoo` | 是 | 用户面 | 可解析 | 未测 |
| 163 | `pyopenms` | 5628 | `ded0610c2990` | `pyopenms` | 是 | 用户面 | 可解析 | 未测 |
| 164 | `pysam` | 9994 | `790ec1a74c2a` | `pysam` | 是 | 用户面 | 可解析 | 未测 |
| 165 | `pytdc` | 12699 | `69155d4b3586` | `pytdc` | 是 | 用户面 | 可解析 | 未测 |
| 166 | `pytorch-lightning` | 6674 | `7bdecc78dcdf` | `pytorch-lightning` | 是 | 用户面 | 可解析 | 未测 |
| 167 | `pyzotero` | 4398 | `a8b4fd9a7788` | `pyzotero` | 是 | 用户面 | 可解析 | 未测 |
| 168 | `qiskit` | 8754 | `21b8dc60d69b` | `qiskit` | 是 | 用户面 | 可解析 | 未测 |
| 169 | `qutip` | 9047 | `cdc96ef046bb` | `qutip` | 是 | 用户面 | 可解析 | 未测 |
| 170 | `rct-design` | 7863 | `340a7f874ba3` | `RCT Design` | 否 | 用户面 | 可解析 | 未测 |
| 171 | `rdkit` | 20420 | `0fe28d387eaa` | `rdkit` | 是 | 用户面 | 可解析 | 未测 |
| 172 | `reasoning-trace-optimizer` | 6359 | `6d330b7afc13` | `reasoning-trace-optimizer` | 是 | 用户面 | 可解析 | 未测 |
| 173 | `regression-analysis` | 10588 | `c04a68a588bd` | `Regression Analysis` | 否 | 用户面 | 可解析 | 未测 |
| 174 | `research-grants` | 37215 | `b062ef2bab28` | `research-grants` | 是 | 用户面 | 可解析 | 未测 |
| 175 | `research-lookup` | 16232 | `f917e638fb9b` | `research-lookup` | 是 | 用户面 | 可解析 | 未测 |
| 176 | `rowan` | 12510 | `9690cf9dbe3c` | `rowan` | 是 | 用户面 | 可解析 | 未测 |
| 177 | `run-summary` | 3442 | `a7947ff90b84` | `run-summary` | 是 | 用户面 | 可解析 | 未测 |
| 178 | `sales-powermap` | 23226 | `63c47170da42` | `sales-powermap` | 是 | 用户面 | 可解析 | 未测 |
| 179 | `sample-size-calculation` | 10585 | `12ab422904e3` | `Sample Size Calculation` | 否 | 用户面 | 可解析 | 未测 |
| 180 | `scanpy` | 11322 | `c93a0bfa855f` | `scanpy` | 是 | 用户面 | 可解析 | 未测 |
| 181 | `scholar-evaluation` | 12257 | `4157069eee2e` | `scholar-evaluation` | 是 | 用户面 ＋PC | 可解析 | 未测 |
| 182 | `scientific-brainstorming` | 8178 | `dfdc611eb35e` | `scientific-brainstorming` | 是 | 用户面 ＋PC | 可解析 | 未测 |
| 183 | `scientific-critical-thinking` | 23704 | `df53105c317a` | `scientific-critical-thinking` | 是 | 用户面 | 可解析 | 未测 |
| 184 | `scientific-schematics` | 23848 | `88224e248c1e` | `scientific-schematics` | 是 | 用户面 | 可解析 | 未测 |
| 185 | `scientific-slides` | 47290 | `27db363932fd` | `scientific-slides` | 是 | 用户面 | 可解析 | 未测 |
| 186 | `scientific-visualization` | 25527 | `981bfae95f31` | `scientific-visualization` | 是 | 用户面 | 可解析 | 未测 |
| 187 | `scientific-writing` | 33780 | `f835a31244ad` | `scientific-writing` | 是 | 用户面 ＋PC | 可解析 | 未测 |
| 188 | `scikit-bio` | 14750 | `66cb2309d38c` | `scikit-bio` | 是 | 用户面 | 可解析 | 未测 |
| 189 | `scikit-learn` | 15532 | `7658a0d3a6d2` | `scikit-learn` | 是 | 用户面 | 可解析 | 未测 |
| 190 | `scikit-survival` | 15077 | `7674199a2bc0` | `scikit-survival` | 是 | 用户面 | 可解析 | 未测 |
| 191 | `scvelo` | 10288 | `8a83fbc44689` | `scvelo` | 是 | 用户面 | 可解析 | 未测 |
| 192 | `scvi-tools` | 7238 | `1909d968193a` | `scvi-tools` | 是 | 用户面 | 可解析 | 未测 |
| 193 | `seaborn` | 19600 | `613d07dc7fcf` | `seaborn` | 是 | 用户面 | 可解析 | 未测 |
| 194 | `self-improvement-loops` | 22244 | `699926720701` | `self-improvement-loops` | 是 | 用户面 | 可解析 | 未测 |
| 195 | `sensitivity-and-specificity` | 7936 | `9a87d365110c` | `Sensitivity and Specificity` | 否 | 用户面 | 可解析 | 未测 |
| 196 | `seo-geo-optimizer` | 51482 | `40d89aa0e11f` | `seo-geo-optimizer` | 是 | 用户面 | 可解析 | 未测 |
| 197 | `shap` | 18412 | `8c950c3852da` | `shap` | 是 | 用户面 | 可解析 | 未测 |
| 198 | `shared-decision-making` | 8289 | `92878deb20ea` | `Shared Decision-Making` | 否 | 用户面 | 可解析 | 未测 |
| 199 | `simpy` | 12164 | `73be2e0f1ce5` | `simpy` | 是 | 用户面 | 可解析 | 未测 |
| 200 | `skill-template` | 5163 | `664c93838ff8` | `skill-template` | 是 | 用户面 | 可解析 | 未测 |
| 201 | `stable-baselines3` | 9506 | `3a3b3f98ff23` | `stable-baselines3` | 是 | 用户面 | 可解析 | 未测 |
| 202 | `statistical-analysis` | 19765 | `82c7ee1761ac` | `statistical-analysis` | 是 | 用户面 ＋PC | 可解析 | 未测 |
| 203 | `statsmodels` | 19691 | `6eadae2bd489` | `statsmodels` | 是 | 用户面 | 可解析 | 未测 |
| 204 | `stock-financial-analysis` | 1949 | `d62b28fd2c48` | `stock-financial-analysis` | 是 | 用户面 | 可解析 | 未测 |
| 205 | `survival-analysis` | 12005 | `6c251e084ba5` | `Survival Analysis` | 否 | 用户面 | 可解析 | 未测 |
| 206 | `sympy` | 13466 | `0c8dd6903b44` | `sympy` | 是 | 用户面 | 可解析 | 未测 |
| 207 | `tiledbvcf` | 15360 | `1da719b9ec64` | `tiledbvcf` | 是 | 用户面 | 可解析 | 未测 |
| 208 | `timesfm-forecasting` | 30154 | `101f92e7a6c8` | `timesfm-forecasting` | 是 | 用户面 | 可解析 | 未测 |
| 209 | `tool-design` | 20089 | `14f5a12b6911` | `tool-design` | 是 | 用户面 | 可解析 | 未测 |
| 210 | `torchdrug` | 14145 | `b9d779a78286` | `torchdrug` | 是 | 用户面 | 可解析 | 未测 |
| 211 | `torch-geometric` | 17059 | `375c1aa1e52d` | `torch-geometric` | 是 | 用户面 | 可解析 | 未测 |
| 212 | `transformers` | 5083 | `b2753065e1e1` | `transformers` | 是 | 用户面 | 可解析 | 未测 |
| 213 | `treatment-plans` | 52691 | `66c81ea88cd4` | `treatment-plans` | 是 | 用户面 | 可解析 | 未测 |
| 214 | `umap-learn` | 15393 | `63f035cb4815` | `umap-learn` | 是 | 用户面 | 可解析 | 未测 |
| 215 | `usfiscaldata` | 7297 | `1260dc9c5f05` | `usfiscaldata` | 是 | 用户面 | 可解析 | 未测 |
| 216 | `vaex` | 6595 | `53fc6ee59ecd` | `vaex` | 是 | 用户面 | 可解析 | 未测 |
| 217 | `venue-targeting` | 8038 | `d080a43e7ca0` | `venue-targeting` | 是 | 用户面 | 可解析 | 未测 |
| 218 | `venue-templates` | 23294 | `4f412d3b092b` | `venue-templates` | 是 | 用户面 | 可解析 | 未测 |
| 219 | `what-if-oracle` | 9481 | `6696e69bfae3` | `what-if-oracle` | 是 | 用户面 | 可解析 | 未测 |
| 220 | `workspace-setup` | 2927 | `910e2aac66b7` | `workspace-setup` | 是 | 用户面 | 可解析 | 未测 |
| 221 | `xiaohongshu-collector` | 9099 | `a6f28381cbff` | `xiaohongshu-collector` | 是 | 用户面 | 可解析 | 未测 |
| 222 | `xlsx` | 11464 | `55591d7decc1` | `xlsx` | 是 | 用户面 ＋PC ＋BI（三面同名） | 可解析 | 未测 |
| 223 | `zarr-python` | 20046 | `e5dfd7907be4` | `zarr-python` | 是 | 用户面 | 可解析 | 未测 |

---

## §7 终态复核值（追加 · 因 §6 校正动作而变动的 1 件）

**变动原因**：§6 交叉引用校正对 §1.2 第 18 件**追加了一行**，故该件 SHA-12 与字节**再次变化**。§1.2 中所列为**追加勘误尾注后、校正行追加前**的中间值。

| 件 | §1.2 所列（中间态） | **终态（本节为准）** | 字节 |
|---|---|---|---|
| `results/_v3_v4_achievements_inventory_2026_09_24.md` | `189ba84fc12e` / 193,632 B | **`965db22e9130` / 194,083 B** | 192,292（原始）→ 194,083 |

> **作废声明**：中间态 `189ba84fc12e`（193,632 B）与更早的 LF 混排态 `3b4a1d4e83bd` **均作废，不应被任何件引用**；本件**唯一有效值 = `965db22e9130`**。

> **其余 28 件**：§1.2 所列终态值**未被后续动作触及，仍为有效**（本节不再重列，避免两处数值分叉）。

> **原始值备查**：本节所涉件**追加前原始值 = ``2fb5987f544d`` / 192,292 B**（经前缀哈希复算逐字验证，见 §5 强证）。

> **本件自身**：SHA-12 **不可内嵌**（自引用悖论）——由 parent 对落盘终态复算并回填回执。

---

## §8 调用面补测补记（2026-09-30 · 文末追加）

> **本节为文末纯追加补记**：0 删改、0 覆写本件任何原行（含 §2.3／§2.4／§7 与附录 A）。

**① 调用面已补测**（PI 2026-09-30 收尾小卷 `ask_61300ee638519d59d23a1d33` q2 裁「**改为补满全量**」）：**首轮 40 枚 / 62 次**已落盘 ＝ `results/_skill_call_surface_probe_2026_09_30.md`（`112346df64fb`；40 枚样本 / 62 次调用 / 成功 40 / 失败 22）。**补满两半均已落盘**（**本棒追加前即时实测值**）：

| 棒 | 件 | SHA-12 | 字节 | 末次 mtime | 覆盖区间（件自述） |
|---|---|---|---|---|---|
| 甲半 | `results/_skill_call_surface_probe_supplement_a_2026_09_30.md` | `054e08dc3b6e` | 34,765 | 17:23:33 | 未测 183 枚之第 **1–92** 位 |
| 乙半 | `results/_skill_call_surface_probe_supplement_b_2026_09_30.md` | `2e6088301882` | 17,725 | 17:23:13 | 未测 183 枚之第 **93–183** 位 |

> 甲 92 ＋ 乙 91 ＝ 未测 **183** 枚；＋首轮 40 枚 ＝ 用户面 **223** 项（**按三件自述区间之算术，非全量结论**）。⚠️ **两半系 17:19–17:22 陆续落盘**，本表为**追加前最后一次实测**；若其后另有续写，**以其终态为准**。**全量并集结论由父棒汇总续记，本棒 0 代裁、0 冒认全量。**

**② 寻址键 ＝ frontmatter `name` 值**（对 §2.4 L185／L187「按裸名寻址**可能落空**」之**实测回应**）：§2.4 列表**实列 22 项**（本棒逐项复核 L185 内 `→` 分隔条目 ＝ **22** 枚）中，**按目录名裸名 0/22 成功**（失败形态 22/22 均为 `Local skill not found: <名>`，**0 其他形态**），**按 `name` 值形态 22/22 成功**且 **22/22 命中用户面**；对照组（`name` ＝ 目录名）裸名 **18/18 成功**。⇒ §2.4 L187 的诚实标注（「可能落空」系**由字面差异推出的候选，非实测失败**）**已由实测落地为 0/22 全落空**。**本件 L185／L187 字面 0 回改**，仅补记实测回应。
> **关联登记（标注 ≠ 篡改 · 0 回改）**：本件 §2.3 L173 所载「本项目拟用写法 ＝ **裸名**」在 **`name` ＝ 目录名项**上仍成立（18/18），但对 §2.4 的 **22 枚不成立**（0/22）⇒ 拟用口径应按「**`name` 值寻址**」而非笼统「裸名」；**该行 0 改写**，留待新件遵用（若 PI 裁修订，再由相应棒另出修订件）。

**③ §2.4「21 项」与列表实列 22 项之差**：标题写 **21 项**、列表**实列 22 枚**（＝21 项常规 `name`≠目录名 ＋ `prd-to-prototype` 这一 YAML 引号值项，与本件 §2.2「`name` 为 YAML 引号值 **1**」的「21 ＋ 1」自述一致）。该差**已由** `results/_skill_call_surface_probe_2026_09_30.md`（`112346df64fb`）§5.3／§5.4 登记（按列表**全取 22 项**，**未发现因标题／列表不一致导致的漏项**）⇒ **本件 0 回改**。

**来源与口径**：来源锚 ＝ 首轮件 `112346df64fb`；补满两半值见上表（**本棒独立复算，SHA-256[:12] 小写；0 certutil／0 `Get-FileHash` 默认／0 内建 `hash()`**）。**追加前本件 SHA-12 ＝ `e96d99ff9e75` ／ 55,340 B ／ 509 行（LF）**。

**出证｜Mavis 团队 evidence-auditor（`agent-11335500b168`）· 文末追加棒｜2026-09-30**

---

## §9 终值补正与全量结论（2026-09-30 · 父棒汇总续记）

> **本节为文末纯追加补正**：0 删改本件任何原行；§8 表内两半值系**追加时点实测之写入中间态**，**终值以本节为准**。

| 棒 | 件 | 终值 SHA-12 | 字节 | 行数 | 结果 |
|---|---|---|---|---|---|
| 首轮 | `results/_skill_call_surface_probe_2026_09_30.md` | `112346df64fb` | 32,261 | 288 | 40 枚／62 次（失败 22 次＝目录名形态，其 22 项均已以 `name` 值取得成功） |
| 甲半 | `results/_skill_call_surface_probe_supplement_a_2026_09_30.md` | `a06316c3c7f2` | 50,658 | 372 | 92/92 成功（全用户面） |
| 乙半 | `results/_skill_call_surface_probe_supplement_b_2026_09_30.md` | `69d311e6a4c7` | 82,744 | 521 | 91/91 成功（全用户面） |

**全量结论（并集）**：**223/223 全覆盖**——40 ＋ 92 ＋ 91 ＝ 用户面 223 项**全部经真实加载实测**；**全部可加载成功（0 最终失败）**；其中 **22 项须以 frontmatter `name` 值形态寻址**（目录名形态 0/22），其余及对照组以目录名形态即可；**命中面 223/223 全为用户面**（plugin-cache／builtin 面 0 命中）。

**边界（如实）**：①「可加载」≠「可执行／质量达标」（如 `stock-financial-analysis` 加载成功但正文无数据源）；②风险登记仅覆盖 `SKILL.md` 本体（首轮件 §4＋乙半件 §4），`references/`／`scripts/` 0 加载 0 断言；③两处转录观察值（34,853／55,374）无盘上支撑——**权威以盘上实测为准**（首轮件 32,261 B；各阶段以链证为准）；④乙半件回执记「522 行」系 ±1 计数口径差（盘上 LF 复算 ＝ **521**）。

**父棒复算（parent · 2026-09-30）**：三件终值 SHA-12／字节／行数逐字复核吻合；本件追加前 ＝ `0b8041435f8e` ／ 58,660 B（前缀恒等链见 §8）。

**汇总续记｜Mavis（root · parent）｜2026-09-30**
