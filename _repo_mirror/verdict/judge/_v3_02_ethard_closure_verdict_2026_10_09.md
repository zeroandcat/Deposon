# V3-02 乙档闭合判定 · `U-V04-01` 产出层半（2026-10-09）

- **件性质**：**判定文书（verdict-keeper 收口面）**｜**状态：已判定，供 PI 复核；候裁项 4 项列出，0 代裁**
- **出件**：**verdict-keeper**（`agent-3a4d09ba3c90`·本棒 session `mvs_6bda1a938918424bb0fd86ce86acd624`）｜⛔ 0 冒充 PI／worker／protocol-keeper／verifier／evidence-auditor
- **授权锚**：PI 2026-10-09 S4 卷5 卡（`ask_aca3a25c244aa405e60eb22c`）第 4 题**乙档（授权改码＋新名）**；理由逐字「不误导」——**L2 转录**（本棒 0 读回执原件，同 PK 件 `c5441e186c3f` §1 诚实边界）
- **判据源**：`results/_v3_02_override_register_2026_10_09.md`（`c5441e186c3f`／36,245 B）§4 `K-PV02-01…11` 判据全文｜**执行回执**：`results/_v3_02_ethard_execution_register_2026_10_09.md`（`23457f5ce432`／22,007 B）
- **版式**：UTF-8 无 BOM · LF｜**件名**：`results/_v3_02_ethard_closure_verdict_2026_10_09.md`（沿命名裁定 `57024f2cd30a` §1.2②，⛔ 无 V-阶段前缀）
- **撞名实测（落盘前）**：拟落名 `Test-Path` ＝ **`False`**；备选名 2 个均 `False`；全仓递归 glob `*closure_verdict*` ＝ **0 命中**、`*v3_02*` ＝ **2 命中**（均为既有登记/准备件，0 涉本名）⇒ **新建，0 覆写**
- **复核纪律**：⛔ **0 复用执行棒自报值**；全部指纹/读数为本 Turn 独立实测（`Get-FileHash`／`json.loads` 键级遍历／递归全字段比对／`ast.literal_eval` 求值）

---

## §0 判定一句话

**`K-PV02-01…11` 逐条独立复核 ＝ 11/11 机械判据 PASS；根因三分类 ＝ 命题层被证伪 0 件／工具或构造层失灵 0 件／不明 0 件；故 `U-V04-01` 之产出层半 ＝ 【已闭合】。** 此闭合**仅**指「`protocol_version` 载体在新名下已落位且测量面零漂移」，**⛔ 0 外推**至 `U-V04-01` 规则层半、⛔ 0 外推「C5 已修好／缺口全闭合／命题存活」。

---

## §1 复核对象指纹（本 Turn 独立实测 · 非自报转录）

| 件 | SHA-12（本棒实测） | bytes | BOM | CRLF | 裸 LF | 与执行棒自报 |
|---|---|---:|---|---:|---:|---|
| ① `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `95f3f0957be8` | 21,176 | 无 | 747 | 0 | 逐字吻合 |
| ② `corpus/v20/index_v3_2026_10_09.json` | `74b27393574f` | 24,837 | 无 | 581 | 0 | 逐字吻合 |
| ③ `results/c5_b_group_fix_readings_2026_10_09.json` | `4e415990b71d` | 10,029 | 无 | 448 | 0 | 逐字吻合 |
| R 副本 `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | `7c095c54fb99` | 21,826 | 无 | 0 | 473 | 逐字吻合 |
| G 副本 `.tmp/_c5_b_group_fix_readings_2026_10_09.py` | `b6855b38acc2` | 12,289 | 无 | 0 | 278 | 逐字吻合 |
| 执行登记件 `results/_v3_02_ethard_execution_register_2026_10_09.md` | `23457f5ce432` | 22,007 | 无 | 0 | 199 | 逐字吻合 |
| PK 准备件 `results/_v3_02_override_register_2026_10_09.md` | `c5441e186c3f` | 36,245 | 无 | 0 | 272 | 逐字吻合 |

> SHA-256 全值（①`95f3f0957be87ac1f48d4121c72eea26b58920f3b470ff4b916ec22deead463b`／②`74b27393574fe7cc0654ac16e6a6281f66b64b60ab1fe164143113f9e2948820`／③`4e415990b71d2a5bce4f7d0856e3a24b3fbddc9b27a841a1bbc9d85ee02fb9c3`／R`7c095c54fb998bfc1757755dd9da7efca974c36942767df5ad37af39a14d123f`／G`b6855b38acc2a20dfdcaba2bd85863ee8322e0eec0b78b3f565c63c90342f630`）见 §7 复算回执行。

---

## §2 `K-PV02-01…11` 逐条独立复核

| id | 判据（PK §4.2 字面） | **本棒独立实测读数** | 复核 |
|---|---|---|:-:|
| **K-PV02-01** | 三件 `protocol_version` **键级**命中 ＝ 1/件，值逐字 `"V0.4"`；⛔ 非子串 | `json.loads` 后**按顶层键遍历计数**：①`keycount=1`／②`keycount=1`／③`keycount=1`，三者值均 `== "V0.4"`（Python 字符串相等，非子串）。禁写面实测：`①caliber`／`②index_v3_meta`／`③input_selfcheck` 内 `protocol_version` 键 **均不存在**（＝ 0 命中） | ✅ PASS |
| **K-PV02-02** | 出处面 7 槽全指新值 ＋ `path_sha256` 独立复算 | ①`generator`＝`deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py`；①`date`＝`2026-10-09`；①`task_id`＝`V3X-C5B-RUNNER-2026-10-09-A1`；②`index_v3_meta.generator`＝同上新副本路径；②`index_v3_meta.date`＝`2026-10-09`；①`integrity.path_hashed`＝`results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json`；②`integrity.path_hashed`＝`corpus/v20/index_v3_2026_10_09.json`。**独立复算**：`hashlib.sha256(relpath.encode("utf-8")).hexdigest()` ＝ ①`path_sha256` ✓／②`path_sha256` ✓。附槽（PK §3.4 表列）：③`generator`＝`.tmp/_c5_b_group_fix_readings_2026_10_09.py`／③`task_id`＝`V3X-C5B-FIX-2026-10-09-A1` ✓ | ✅ PASS |
| **K-PV02-03** | 6 件 pin 跑前跑后同值 | 本 Turn 对 PK §8.2 与执行回执 §4 所列 **15 件**逐一 `Get-FileHash` 实测：①②③旧本、R 旧本、G 旧本、`c13449101ab3` 及 9 件禁触/输入件（`2593ea7b93cf`／`bff06d3b3f97`／`1d1895489d17`／`87ab4929477f`／`c5441e186c3f`／`8e4f2ae63de3`／`1088fdd2b197`／`8423ffe266af`／`6a2656878745`／`cf7682348617`）**全部与预登记值逐字同值，0 漂移**。另抽验 ①件内建 8 项 pin：`sha12_before`＝`sha12_after`＝**本 Turn 盘上实测 SHA-12**，8/8 三值同字 | ✅ PASS |
| **K-PV02-04** | `spec_ref_pending` 跑前书面二择一 | 执行回执 §5.1 载**跑前**声明取**选项②**（逐字沿用＋登记为过时残留），并在 §5.2 逐字登记残留串。**本棒实测**：①`caliber.spec_ref_pending` 旧＝新、②`index_v3_meta.spec_ref_pending` 旧＝新，**新旧逐字一致**（0 静默改码）。声明之**合规性附条件**：选项② 之成立以「测量面零漂移」为前提，该前提已由 K-PV02-05 独立复核为真 ⇒ 选项② 合规（详见 §5 候呈项 C） | ✅ PASS（附条件已实测满足） |
| **K-PV02-05** | 测量面逐字相同；仅允许差异集可漂移 | **递归全字段比对（非抽样）**：①新旧差异 **21 条路径**、②**9 条**、③**4 条**。逐条分类后：①＝ `protocol_version`(新增)＋`date`／`task_id`／`generator`(出处)＋`integrity.*`(3 项)＋`zero_overwrite_proof.sha12_before/after` 各 5 项增列(D 类·PK §6 规格直接导致)；②＝ `protocol_version`＋`protocol_version_axis`(新增)＋`index_v3_meta.date/generator`＋`integrity.*`(3)；③＝ `protocol_version`(新增)＋`date`／`task_id`／`generator`。**测量面 E 类差异 ＝ 0；未列明 F 类差异 ＝ 0**。另 `③boundary.no_existing_file_modified` 旧＝新＝`true` | ✅ PASS |
| **K-PV02-06** | ③ drift 两读数自 raw 逐字携带，0 重算 | raw 件 `1088fdd2b197` 之 `reproduction_selfcheck.max_abs_dev_vs_stored_svd2` ＝ **`0.0089821568`**、`reproduce_within_4dp` ＝ **`false`**；新③`input_selfcheck` 同二键**逐字同值** ✓。①件同源键 `raw_embedding_reproduction_max_abs_dev_vs_stored_svd2` ＝ `0.0089821568`、`raw_embedding_reproduces_stored_svd2` ＝ `false` ✓。⛔ 本棒 0 重算 SVD、0 网络、0 读 key | ✅ PASS |
| **K-PV02-07** | 完整性自证面 | **按 `verify_integrity`（R 副本 L138-142）口径独立复算**：`dump_json` 字面 ＝ `json.dumps(obj, ensure_ascii=False, indent=1) + "\n"`（**含尾换行**），置 `integrity.content_sha256=""` 后 `sha256_str(dump_json(doc))` → ①**True**／②**True**。件内自证：`self_check.integrity_index_v3_ok=true`／`integrity_results_ok=true`／`forbidden_tokens_found={}`；`frozen_proof.unchanged=true`；`zero_overwrite_proof.unchanged=true`。**红线 8 项**取 `FORBIDDEN_TOKENS`（`ast.literal_eval` 递归求值 `BinOp` 拼接，得 `PoA`／`已修`／`坍缩`／`改善`／`元…` ／`ark-`／`sk-`／`ghp_` 共 8 项）于三件**实测命中 ＝ 0** | ✅ PASS |
| **K-PV02-08** | ③ `degradation_guard` 逐项与旧件同值 | 旧／新两字典**整体逐字相等**（`same=True`）：`threshold_n_distinct_le`＝3、`semantic_hash_codelen_n_distinct`＝**9**、`root_predup_dual_n_distinct`＝**22**、`byte_hash_primary_n_distinct`＝**22**、`any_alarm`＝**false**。⚠️ **口径守护已继承**：`any_alarm=false` 仅覆盖该 guard 之 3 项，⛔ 0 外推「0 退化警报」 | ✅ PASS |
| **K-PV02-09** | ③ `date` 为 wall-clock 必 ≠ 旧值 | 旧 `2026-10-01T09:25:22+08:00` → 新 **`2026-10-09T13:39:57+08:00`**，`differs=True` ✓。⛔ 0 由 byte 变化推论构造已变，⛔ 0 由反之推论构造未变 | ✅ PASS |
| **K-PV02-10** | (a) root ≠ `75596bbabdb8`；(b) root/state22/ext1 逐字锁旧①实测值 | **键位实测更正**：`b3_merkle_root` **不在顶层**，实际落面为 **`chain_summary.b3_merkle_root`**（旧①件同）⇒ PK §4.2 与执行回执均以「顶层」口吻表述，属**表述层偏差（非数值偏差）**，本棒按实际键位取读。(a) 新 `chain_summary.b3_merkle_root` ＝ **`45ef859b2be9`** ≠ `75596bbabdb8` ✓。(b) 三值旧＝新逐字：`b3_merkle_root`＝`45ef859b2be9`／`state_22_after_22_captions`＝`bbd61495cb5d`／`ext_1_after_anchor2`＝`bf492f1c8424` ✓ | ✅ PASS |
| **K-PV02-11** | 禁触面 | **0 改**：`c13449101ab3`／`2593ea7b93cf`／`bff06d3b3f97`／`1d1895489d17`／`87ab4929477f`／`c5441e186c3f` 本 Turn 实测**全部同值**（§2 K-PV02-03 行）。⛔ 0 跑 fetch 脚本（`.tmp/_v5_c5_b_fetch_raw_embeddings.py`＝`8e4f2ae63de3` 实测同值，未被改写）；⛔ 0 合并派生 JSON（`corpus/v20/index.json`＝`8423ffe266af` 同值）；⛔ 0 判档位（产出件内 `no_verdict_notice` 逐字存「本件 0 判档位; PASS/FAIL/KD 归 verdict-keeper」）；⛔ 0 key（`③boundary.no_key` 存「脚本内 0 读 key」） | ✅ PASS |

**汇总：11/11 PASS · 0 FAIL · 0 停手条件触发。**

---

## §3 抽验读数明细（⛔ 0 复用执行棒自报值）

### 3.1 键级命中（`json.loads` 顶层键遍历 · 非子串）

| 件 | `protocol_version` 顶层键计数 | 值（Python `repr`） | 值 `== "V0.4"` | 禁写面（`caliber`／`index_v3_meta`／`input_selfcheck` 内同键） |
|---|---:|---|:-:|---|
| ① | 1 | `'V0.4'` | True | 0 命中 |
| ② | 1 | `'V0.4'` | True | 0 命中 |
| ③ | 1 | `'V0.4'` | True | 0 命中 |

**② 轴声明串实测在位**（`protocol_version_axis`，逐字在盘）：
> 「P-D 指纹协议轴: protocol_version=V0.4 指 docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md §2.4 之 P-D 指纹协议版本; 本件顶层 generator_version 与 spec 属 corpus 工具/规范轴 (corpus 版本面), 与本键分属不同轴, 互不覆盖; 本键 0 改写 corpus 版本, 且 0 可由 corpus 版本推得协议版本; 二者须并读, 0 择一为准」

⇒ **双版本轴并存之误读面已被声明义务覆盖**（PK §3.3 固化之声明义务，本棒实测在位）。

### 3.2 7 槽出处字段之一（逐槽实读）

| 槽 | 实测值 | 指新名？ |
|---|---|:-:|
| ①`generator` | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | ✓ |
| ①`date` | `2026-10-09` | ✓ |
| ①`task_id` | `V3X-C5B-RUNNER-2026-10-09-A1` | ✓ |
| ②`index_v3_meta.generator` | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | ✓ |
| ②`index_v3_meta.date` | `2026-10-09` | ✓ |
| ①`integrity.path_hashed` | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json`（`path_sha256` 独立复算 ✓） | ✓ |
| ②`integrity.path_hashed` | `corpus/v20/index_v3_2026_10_09.json`（`path_sha256` 独立复算 ✓） | ✓ |
| ③`generator`（附槽） | `.tmp/_c5_b_group_fix_readings_2026_10_09.py` | ✓ |
| ③`task_id`（附槽） | `V3X-C5B-FIX-2026-10-09-A1` | ✓ |

### 3.3 `chain_summary` 三值（旧① vs 新① 逐字）

| 键 | 旧① | 新① | 同值 |
|---|---|---|:-:|
| `b3_merkle_root` | `45ef859b2be9` | `45ef859b2be9` | ✓ |
| `state_22_after_22_captions` | `bbd61495cb5d` | `bbd61495cb5d` | ✓ |
| `ext_1_after_anchor2` | `bf492f1c8424` | `bf492f1c8424` | ✓ |

### 3.4 测量面逐字抽样（递归全比对之外之独立抽样复现）

①件 `per_caption`（22 条）抽样索引 0／7／21 × `byte_hash`／`semantic_hash`／`dual` ＝ **9/9 逐字同值**（例：`per_caption[21].byte_hash` ＝ `6abc0c5ac060`；`semantic_hash` ＝ `01eed`；`dual` ＝ `6abc0c01eed`）。
③件 `per_caption[0]`／`per_caption[5]` **整体对象逐字相等**；`readings` **整体相等**；`cross_seed_control` **整体相等**。
①件 `caliber` 键面实测 ＝ `n_components`／`planes_per_dim`／`hyperplanes_shape`／`code_len_bit`／`hex_width`／`d_over_2_reference`／`d_over_2_note`／`semantic_hash`／`byte_hash`／`dual`／`spec_ref_pending`（与 PK §3.3 所列旧键面**逐段相同，0 塞入 `protocol_version`**）。

### 3.5 内建 pin 8 项（`sha12_before` ＝ `sha12_after` ＝ 本 Turn 盘上实测）

| 项 | 三值同字 |
|---|:-:|
| `corpus/v20/index_v2_2026_09_16.json` ＝ `efe05ad775de` | ✓ |
| `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` ＝ `b5873afb9d29` | ✓ |
| `corpus/v20_caption_surface/_p_d_b3_merkle_22caption_runner_2026_09_16.py` ＝ `d2cd7acb29a1` | ✓ |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` ＝ `33ad1c01f745` | ✓ |
| `corpus/v20/index_v3_2026_09_29.json` ＝ `3ba2449cf986` | ✓ |
| `results/c5_b_group_fix_readings_2026_10_01.json` ＝ `2a7749da7c4d` | ✓ |
| `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` ＝ `de16bc002198` | ✓ |
| `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` ＝ `191efa7fe0b6` | ✓ |

### 3.6 红线 8 项（`ast.literal_eval` 递归求值 · `BinOp` 拼接还原）

`FORBIDDEN_TOKENS` ＝ `PoA` ／ 已修 ／ 坍缩 ／ 改善 ／ 元…（术语红线 2 项）／ `ark-` ／ `sk-` ／ `ghp_`（凭据面 3 项），共 **8 项**。于 ①②③ 三件实测**命中 ＝ 0**（`[]`×3），与件内 `self_check.forbidden_tokens_found` ＝ `{}` 一致。**R4 key 永不明文**：本棒 0 读任何凭据面，⛔ 本件 0 落任何 key 字面。

---

## §4 根因三分类（诚实纪律 · 每条判定归且仅归一类）

| 类 | 计数 | 内容 |
|---|---:|---|
| **命题层面被证伪（真证伪）** | **0** | 无。本轮实验 0 产出负面命题结论。 |
| **工具或构造层面失灵（假证伪）** | **0** | 无。构造面（`ANCHORS`／`LSH_SEED`／`K_COMPONENTS`／`N_PLANE`／`HEX_WIDTH`／`FORBIDDEN_TOKENS`／判定逻辑）逐字未改（§2 K-PV02-11 实测），测量面零漂移（K-PV02-05 递归实测 0 条 E/F 类差异）。 |
| **不明** | **0** | 无。11 条判据全部可机械赋值且已赋出真值。 |

**⚠️ 本棒侧两处自身失灵（工具层 · 已在归因后更正 · ⛔ 0 记入被验方判定）**：

1. **完整性初判假 FAIL（工具失灵，已归因）**：初次独立复算 `content_sha256` 得 ①② 均 `false`，与件内自报 `true` 相悖。追根因＝ **本棒自建复算器漏抄 `dump_json` 之尾项 `+ "\n"`**（R 副本 L122-123 逐字 `json.dumps(obj, ensure_ascii=False, indent=1) + "\n"`）。按精确口径重算，①② 皆 **`True`**，且**新旧四件**（含 0 回改之旧基准件）一致 ⇒ 假 FAIL 系**本棒工具侧**失灵，**⛔ 0 归因于被验件、⛔ 0 记入 K-PV02-07 判档**。
2. **红线字面假命中（工具失灵，已归因）**：初次以正则抽取 `FORBIDDEN_TOKENS` 时，未处理 `"P" + "oA"` 型 `BinOp` 拼接，致拆出单字 `"P"`／`"ar"` 等并产生**假命中 7 项**。改以 `ast` 递归求值得真值 8 项后，**实测命中 ＝ 0** ⇒ 假命中系**本棒工具侧**失灵，**⛔ 0 记入 K-PV02-07 判档**。

> 上述两条同时构成**方法学登记**：凡「自建复算器 vs 件内自证」冲突，须先证伪自身口径（对**旧基准件**跑同一复算器即为有效证伪手段——本棒即以「新旧四件同向失败」定位到自身漏项）。

---

## §5 闭合判档（`U-V04-01` 产出层半）

### 5.1 主读法（机械判据读法）— **【已闭合】**

**判档**：`U-V04-01`（`protocol_version` 产出层载体缺口）之**产出层半** ＝ **已闭合**。

**依据**：PK §4.3 之「全部 PASS 之判据（且仅当）」 ＝ ① `K-PV02-01…11` 逐条 PASS ✔（§2 逐条实测 11/11）且 ② `K-PV02-05` 之**测量面逐字比对表**已随回执落盘 ✔（执行回执 §3，含逐条差异明细与 A/B/C/D/E/F 分类计数；本棒独立递归复现得**同构结果**：差异 21／9／4 条，E＝0、F＝0）。两条件**同时且仅**满足。

**闭合之确切范围（显式边界声明）**：
- 闭合者 ＝ **`protocol_version="V0.4"` 于 2026-10-09 新名下三件产出件之顶层落位** ＋ **测量面零漂移** ＋ **出处面 7 槽全指新值** ＋ **既有件 byte 0 触动**。
- **⛔ 闭合 0 涵盖** ① `U-V04-01` 之**规则层半**（PK §4.1 明载「规则面 0 触」；规则面唯一载体仍为 `c13449101ab3` §2.4 L116）② **root 漂移读数之消解**（`reproduce_within_4dp=false` 为 2026-10-01 既有读数之**原样携带**，⛔ 0 称「已消／已复现」）③ **退化面全局**（`any_alarm=false` 仅覆盖 guard 之 3 项；⛔ 0 外推「0 退化警报」）④ **C5／B3 命题之存亡** ⑤ **SVD-3 坐标坍缩命题之存亡**。
- **⛔ 0 外推**：禁述①–⑥（PK §4.1）**全条继承**于本判定文书 —— 本件**不**陈述「缺口已闭合」之全称义、**不**陈述「C5 已修好」、**不**陈述「命题存活」。

### 5.2 替代读法（双读法并列登记 · ⛔ 不合并 · 不互相取消）

| 读法 | 判档 | 论据 | 与主读法分歧处 |
|---|---|---|---|
| **（i）机械判据读法（主）** | **已闭合** | `K-PV02-01…11` 11/11 PASS ＋ 测量面比对表已交（PK §4.3 之唯一判据） | — |
| **（ii）产出可消费性读法（替代）** | **闭合（附条件）** | 载体在位可消费，**但**新副本 R 之 docstring 与 `zero_overwrite_proof.policy` 仍逐字指 09-29／09-16 旧资产（§6 呈报项 A2／A3），若下游按 docstring 之「出件路径」执行将指向旧名 | 分歧：载体**本体**闭合 vs 载体**说明书**未同步。二者不冲突（判档对象不同），但**「闭合」之表述须带此附条件**，否则构成**次生误导面** |
| **（iii）spec 残留读法（替代）** | **闭合（附条件）** | `spec_ref_pending` 字面**仍称**「待 doc-writer 棒 2b 新增」而所指 spec **已在盘**（`c13449101ab3`／34,367 B）⇒ 载体指向的是**已存在之 spec**（`protocol_version` 规则面即取自其 §2.4），故**规则依据 0 缺失**；然该括注本身为**过时残留**，已由执行回执 §5.2 登记披露 | 分歧：功能面**无缺口** vs 字面面**有过时括注**。与读法（i）不冲突，因 `K-PV02-04` 之选项②本即以「披露责任」置换「改码责任」，且本棒实测该披露**确已在回执中履行** |

**⚠️ 两替代读法与主读法之分歧已如实登记**（§5.2 表末列）；本棒**0 裁定** PI 采何读法，**0** 将任一替代读法之附条件**升级为**主读法之限制。

### 5.3 候裁依存声明（涉 PI 项 · 本棒 0 代裁）

| 候裁项 | 与闭合判档之关系 | 本棒处置 |
|---|---|---|
| **`U-V04-01-新` 整类豁免等 PI 项** | 若 PI 后续裁定 **`U-V04-01-新` 整类豁免**（即以新类目另立 `protocol_version` 相关待办、免于按本缺口口径销项），则本判档之**对象标识**须随裁调整，**判档结论（产出层已闭合）不因此改变** | **候裁依存**：判档**以当前 `U-V04-01` 字面为对象**；PI 若改类目归属，**仅需换对象名，0 需重跑实验**（因判据读数 0 依赖对象命名）。本棒**0 代裁、0 预设**该豁免成立或不成立 |
| **4 项呈报项（§6 A/B/C/D）** | 均属**体例／残留／副产物**面，**不影响** §5.1 主读法之 PASS 读数；其中 A2／A3／C 若 PI 裁定须在**本轮**修订跑内一并处置，则须**另起一轮修订跑**（本轮已封） | **候呈**：见 §6 |

---

## §6 执行棒三项呈报之处置建议（⛔ 0 代裁 · 列候呈）

> 本棒**仅列事实与建议**，处置权属 PI／verdict-keeper 后续裁；本棒**0** 执行任何处置、**0** 改任何既有件。

### A. **CRLF 体例偏差**（执行回执 §7 呈报项①）

- **事实（本棒独立实测）**：①②③ 三件 JSON 落盘为 **100% CRLF**（①747／②581／③448 处 CRLF，裸 LF ＝ 0）；**既有三件亦为 100% CRLF**（旧①736／旧②579／旧③447，裸 LF ＝ 0）⇒ **新旧同形**，非本次引入之体例分叉。R／G 两副本与两登记件为 LF 体。
- **根因**：既有代码 `Path.write_text(dump_json(...), encoding="utf-8")` 在 Windows 之行尾翻译（**该调用系既有代码，本次一字未改**）。
- **建议处置（候呈）**：**维持现状，不事后转 LF**。理由：① 转换即构成对产出件之**事后改写**，破坏「重跑即复现」；② 转换超出乙档改动清单（PK §6）；③ 新旧同形 ⇒ **无误导增量**（读者按同一体例读新旧件）。若 PI 欲统一体例，应**另立体例裁**并在**未来**产出链之写出层根治，⛔ 0 回头改本轮已封产出件。
- **⛔ 0 做的事**：本棒**0 转 LF**、**0 改任何产出件**。

### B. **`spec_ref_pending` 过时残留**（执行回执 §5／§9.3③ 呈报项②）

- **事实（本棒独立实测）**：①`caliber.spec_ref_pending` 与 ②`index_v3_meta.spec_ref_pending` 之值**新旧逐字一致**，均为 `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md (待 doc-writer 棒 2b 新增, 本件 0 代拟正文)`；所指 spec **确已在盘**（`c13449101ab3`／34,367 B）⇒ 括注**确为过时残留**。
- **执行棒之处置合规性**：取 `K-PV02-04` **选项②**（逐字沿用＋回执登记为过时残留），系**跑前书面声明**（执行回执 §5.1）之履行 ⇒ **不构成「0 声明而开跑」之静默沿用**，PASS 成立。其所给理由（选项①将改写两处 `spec_ref_pending` 字面，而该二路径不在 `K-PV02-05` 允许差异集内、致自致 FAIL）经本棒独立比对**确认为真**（§2 K-PV02-05 差异表内 0 条涉该二路径）。
- **建议处置（候呈）**：**本轮维持残留、维持披露**；建议 PI 于**下一轮**修订跑（若另有修订需求）择 `K-PV02-04` 选项① 一并清字面。⛔ **0** 在本轮单独发起仅改此括注之修订跑（成本高于收益，且将重开测量面比对义务）。
- **⚠️ 边界**：**0** 因该残留而推断「规则依据缺失」——`protocol_version` 之规则依据取自 `c13449101ab3` §2.4，**已在盘且逐字有效**。

### C. **R docstring 与 `zero_overwrite_proof.policy` 之清单外文字**（执行回执 §9.3①② 呈报项③）

- **事实（本棒逐行实测 R 副本 L1-14）**：
  - L3：`P-D B3 Merkle 22 caption dual chain re-walk runner -- V0.4 coordinate space (new name)`；
  - **L5**：`V3X-C5B-RUNNER-2026-09-29-A1`（**旧 `task_id`**；件内实字段为 `V3X-C5B-RUNNER-2026-10-09-A1`）；
  - **L7**：`corpus/v20/index_v3_2026_09_29.json`、**L8**：`results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json`（**旧产出名**，各逐字）；
  - L6 出件路径说明亦沿「0 overwrite the 2026-09-16 assets」旧句。
  - 另 `zero_overwrite_proof.policy` ＝ 「0 覆写 2026-09-16 两件 B3 既有产出 + 既有 runner」，而实 pin 集已扩至 **8 项** ⇒ **文字未反映扩面**（文字本身仍属实，非虚假陈述）。
- **规范面核对**：PK §6「改何物」所列必改面 ＝ **§3.4 五类出处字段／路径**（`DATE`／`P_OUT_*`／`REL_*`／`GENERATOR`／`task_id`／`spec_ref_pending` 处置），**docstring 与 `policy` 文字不在清单内** ⇒ 执行棒**从严取「仅新增＋五类同步」、0 清单外改动**，**未越规格**。故 ⛔ **0 判其越权**；然**如实登记为残留**（次生误导面，见 §5.2 读法（ii））。
- **建议处置（候呈）**：**本轮维持、0 改**（改之即违「0 回改既有件」之同族纪律，且须重跑以保持 docstring 与产出同步）。建议 **PI 于下一轮修订跑时将「docstring 出件名／`task_id` 与 `policy` 文字」纳入必改面清单**（属**口径扩充**，须走口径固化流程，⛔ 0 由执行棒现场自行简化）。**若 PI 裁定本轮必须清**，则须另起一轮修订跑并重交测量面比对表，⛔ 0 以「手改 JSON 之 docstring 字段」了结（JSON 内无 docstring 字段，残留仅存在于**脚本副本**内，故风险面为**脚本说明书误导**，非产出件误导）。

### D. **`.pyc` 编译副产物 2 件**（执行回执 §9.1 呈报项④）

- **事实**：`.tmp/_g_compile_check.pyc` 与 `deposon_team/plugins/__pycache__/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.cpython-314.pyc` 为 `py_compile` 副产物；清理被运行时拦截（路径含中文被判 dangerous removal target）⇒ 执行棒**依纪律 0 绕过、0 改用他法删除**，如实登记。
- **建议处置（候呈）**：**由具备删除权限者处置**（本棒**0** 执行删除，⛔ 0 绕过运行时删除保护）。其**不构成证据面污染**（`.pyc` 非读数载体、非登记件、非 pin 面）。

---

## §7 0 回改确认 · 纪律自查

- **0 回改任何既有件**：本棒**写入面 ＝ 仅本件 1 件**（新名，`Test-Path=False` ＋ glob 0 命中）；§2 K-PV02-03 行所列 **15 件**既有件本 Turn 实测**全部与预登记值逐字同值**；①件内建 8 项 pin 经本 Turn 独立复算** 8/8 三值同字**。
- **0 补写／0 合并派生 JSON**：本棒**0** 产出任何 JSON（⛔ 0 合并 K-PV02-11 禁述之派生 JSON）。
- **0 改阈值**：⛔ 0 触碰 `TH-*`／`K-*` 任一阈值字面；`K-PV02-01…11` 全条**沿预登记字面**赋值，阈值本身**0 裁定**。
- **0 编造**：本件全部指纹、键位、读数、行号为本 Turn 实测；凡引 PI 字面处**如实标注为 L2 转录**（本棒 0 读回执原件）；§4 两处自身失灵**如实登记**（含工具侧假 FAIL 与假命中之根因与更正过程）。
- **0 网络 · 0 端点 · 0 key**：本棒 0 网络调用、0 读 `.env`／`config.yaml`／`mcp.json`／任何凭据面；**R4 key 永不明文** —— 本件 0 落任何 key 字面，红线扫描仅读取脚本内 `FORBIDDEN_TOKENS` **定义字面**（`sk-`／`ghp_`／`ark-` 三项**模式名**，⛔ 非任何真实 key 之字面）。
- **0 判档越界**：本件判 `U-V04-01` **产出层半**之闭合，⛔ **0** 判 C5／B3 命题之存亡，⛔ **0** 判 SVD-3 命题之存亡，⛔ **0** 判 `U-V04-01` 规则层半。
- **0 阶段名自升**：本件名 0 含 V-阶段前缀；全部 `V0.4`／`V3-02`／`v0_4` 字样均为**既有件既有字面之引用**，0 新造阶段名／版本号。

### §7.1 本件落盘后自身实测（0 自指）

> 本节数值由**落盘后独立复算**填入（SHA-256／SHA-12／bytes／BOM／行尾），⛔ 0 自指、⛔ 0 预估。

| 项 | 实测值 |
|---|---|
| SHA-256 | `cd8e8bbe444c31dbb35246c0fa0494dd79ffe1fb86abda23dd993c6b27c79958` |
| SHA-12 | `cd8e8bbe444c` |
| bytes | 27,438 |
| BOM | 无 |
| 行尾 | LF（0 CRLF ／ 裸 LF 222） |

> ⚠️ **回填后 SHA-12 会变**：本节之回填写入本身改字节 ⇒ 上列 `cd8e8bbe444c` 为**回填前**实测值。**落盘后终值以本棒回执所报为准**（回执报终态 SHA-12 ＝ 回填后终值），本件正文与回执**逐字一致**方为终态。此登记沿既有实证件体例（回填自指之已知约束），**0** 伪称上列值为终态。
