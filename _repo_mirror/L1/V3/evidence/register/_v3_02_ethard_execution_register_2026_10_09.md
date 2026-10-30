# V3-02 乙档执行回执 · 产出链重走（改码＋新名落盘）· 2026-10-09

- **件性质**：**乙档执行回执**（worker 执行面）｜**状态：执行完毕，候呈 verdict-keeper／PI**
- **出件**：**worker**（`worker`·本棒 session `mvs_f067b021313d4e38a6c7d008a9a09f7c`）｜⛔ 0 冒充 protocol-keeper／verdict-keeper／PI
- **授权锚**：PI 2026-10-09 S4 卷5 卡（`ask_aca3a25c244aa405e60eb22c`）**第 4 题乙档**（授权改码＋新名，理由逐字「不误导」）
- **规格源**：`results/_v3_02_override_register_2026_10_09.md`（`c5441e186c3f`／36,245 B）§6「后续 worker 派工规格」＋§4 判死线 `K-PV02-01…11`（该件 SHA-256 跑前跑后逐字复核同值，见 §4）
- **版式**：UTF-8 无 BOM · LF｜**件名**：`results/_v3_02_ethard_execution_register_2026_10_09.md`（`_主题_日期`，⛔ 无 V-阶段前缀、⛔ 无 `_v5_` 类字样；沿命名裁定 `57024f2cd30a` §1.2②，体例同 PK 件名）
- **撞名实测（落盘前）**：`Test-Path` ＝ **`False`**；备选名 2 个均 `False`；全仓 glob `**/*2026_10_09*` ＝ 57 命中，**0 件为我方 5 个新名**（详见 §9.2）⇒ **新建，0 覆写**

---

## §0 状态一句话

**乙档三步（改码 → 跑 → 落新名）已按 PK 规格顺序执行完毕：`K-PV02-01…11` 逐条机械判据逐条以实测读数为证 PASS，测量面零漂移（E 类差异 ＝ 0／F 类差异 ＝ 0），6 件 pin 跑前跑后同值；⛔ 本棒 0 判档位、0 外推 `U-V04-01` 闭合、0 声称缺口闭合——闭合判定归 verdict-keeper。**

---

## §1 执行对照（改了什么 ／ 0 触了什么）

| 项 | 动作 | 实测 |
|---|---|---|
| R 副本 | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py`（源 `de16bc002198`） | 落前 `Test-Path=False`；落后 SHA-12＝`7c095c54fb99`／21,826 B |
| G 副本 | `.tmp/_c5_b_group_fix_readings_2026_10_09.py`（源 `191efa7fe0b6`） | 落前 `Test-Path=False`；落后 SHA-12＝`b6855b38acc2`／12,289 B |
| 改码面（仅此） | `DATE`／4 处写出路径与相对路径／`GENERATOR`／`task_id`／`PINNED` 扩面 5 项／① `protocol_version`／② `protocol_version`＋`protocol_version_axis`／③ `protocol_version` | 见 §1.1 |
| ⛔ 0 触 | 既有脚本 2 件、既有产出件 3 件、`c13449101ab3`、`2593ea7b93cf`、`bff06d3b3f97`、`1d1895489d17`、`87ab4929477f`；`ANCHORS`／`LSH_SEED`／`K_COMPONENTS`／`N_PLANE`／`HEX_WIDTH`／`FORBIDDEN_TOKENS`／判定逻辑／`SPEC_REF_V04`／`ANCHORS_REF`／`SPEC_REF_BASE` | §4 pin 同值＋§1.1 逐行 diff |

### §1.1 逐行 diff 自证（副本 vs 原件，`difflib` 全量比对）

| 副本 | 改动行（旧 → 新） |
|---|---|
| **R** | `DATE`；新增 `PROTOCOL_VERSION="V0.4"`＋`PROTOCOL_VERSION_AXIS`（含注释 6 行）；`P_OUT_INDEX_V3`／`P_OUT_RESULTS`／`REL_INDEX_V3`／`REL_RESULTS` 4 处换新名；`PINNED` 增 5 项；`GENERATOR` 换新副本路径；`index_v3["protocol_version"]`＋`index_v3["protocol_version_axis"]` 2 行；`task_id` 换新档位；`"generator": GENERATOR` 后新增 `"protocol_version": PROTOCOL_VERSION` |
| **G** | `OUT` 换新名；新增 `PROTOCOL_VERSION="V0.4"`（含注释 2 行）；`task_id` 换新档位；`generator` 换新副本路径；新增 `"protocol_version": PROTOCOL_VERSION` |

- **两副本 diff hunk 之外 0 改动**；`py_compile` 双通过（R 用默认路径、G 用临时 cfile，⛔ 0 留下 `.pyc` 于脚本目录，见 §9.1）。
- **`date` 口径**：R 之 `DATE` 为常量且 0 wall-clock ⇒ ①`date`／②`index_v3_meta.date` 随新档位同步；G 之 `date` **保持 wall-clock**（`datetime.now(...)` 一字未改，⛔ 0 改常量）⇒ 与旧件必不等，属 `K-PV02-09` 预期差异。

---

## §2 `K-PV02-01…11` 逐条实测读数

| id | 判据（PK §4.2） | **实测读数** | 读法 |
|---|---|---|---|
| **K-PV02-01** | 三件顶层键 `protocol_version` ＝ 1/件且值逐字 `"V0.4"`（⛔ 0 子串命中充数） | ①`keycount=1`／`"V0.4"`；②`keycount=1`／`"V0.4"`；③`keycount=1`／`"V0.4"`；三件原文 token 计数各 ＝ 1；禁写面实测：`caliber`(①)／`index_v3_meta`(②)／`input_selfcheck`(③) 内**均 0 命中** | `json.loads` 后按顶层键遍历计数＋值相等（**非子串**） |
| **K-PV02-02** | 出处面七槽全指新值＋`integrity.path_sha256` 独立复算一致 | ①`generator`＝`..._v0_4_2026_10_09.py`✓／①`date`＝`2026-10-09`✓／①`task_id`＝`V3X-C5B-RUNNER-2026-10-09-A1`✓／②`index_v3_meta.generator`✓／②`index_v3_meta.date`＝`2026-10-09`✓／①`integrity.path_hashed`＝新路径且 `path_sha256`＝`sha256(该串)`✓／②同✓；另 ③`generator`＝`.tmp/_c5_b_group_fix_readings_2026_10_09.py`✓／③`task_id`＝`V3X-C5B-FIX-2026-10-09-A1`✓ | `hashlib.sha256(relpath)` 独立复算 |
| **K-PV02-03** | 6 件 pin 跑前跑后同值 | **6/6 同值**（§4 表） | `Get-FileHash` 跑前＋跑后各一轮 |
| **K-PV02-04** | `spec_ref_pending` 过时残留**跑前书面二择一** | **选项②**（逐字沿用＋登记为过时残留），声明见 §5；实测 ①`caliber.spec_ref_pending` 旧＝新、②`index_v3_meta.spec_ref_pending` 旧＝新（**逐字未改**） | 逐字比对 |
| **K-PV02-05** | 测量面逐字相同，仅允许差异集可漂移 | **E 类（测量面）差异 ＝ 0；F 类（未列明）差异 ＝ 0**；差异 28 条全部落在 A/B/C/D 四类（§3 表） | 递归全字段 `difflib` 式逐路径比对（非抽样） |
| **K-PV02-06** | 新③件 drift 两读数须自 raw 逐字携带，0 重算 | ③`reproduce_max_abs_dev_vs_stored_svd2`＝`0.0089821568`、`reproduce_within_4dp`＝`false`；与 raw 件（`1088fdd2b197`）`reproduction_selfcheck` **逐字相同**（`carry_ok=True`）；①同源两键亦同值 | `json.loads` 对读 |
| **K-PV02-07** | 完整性自证面 | ①`verify_integrity`＝**True**、②＝**True**；`self_check.integrity_index_v3_ok`＝`true`／`integrity_results_ok`＝`true`／`forbidden_tokens_found`＝`{}`；`frozen_proof.unchanged`＝`true`；`zero_overwrite_proof.unchanged`＝`true`；术语红线 8 项于三件**实测 0 命中**（`[]`×3） | 按 `verify_integrity` 口径复算＋红线字面扫描 |
| **K-PV02-08** | ③`degradation_guard` 逐项与旧件同值 | 阈值 3／`semantic_hash_codelen_n_distinct`＝**9**／`root_predup_dual_n_distinct`＝**22**／`byte_hash_primary_n_distinct`＝**22**／`any_alarm`＝`false`；新旧两字典**整体相等**（`same=True`） | 字典整体比对 |
| **K-PV02-09** | ③`date` 为 wall-clock 必 ≠ 旧值，属允许差异集 | 旧 `2026-10-01T09:25:22+08:00` → 新 **`2026-10-09T13:39:57+08:00`**；⛔ 0 由 byte 变化推论构造已变，亦 0 由反之推论构造未变 | 两件 `date` 对读 |
| **K-PV02-10** | (a) root ≠ `75596bbabdb8`；(b) 新件 root/state22/ext1 逐字锁旧①件实测值 | (a) ✓（≠ `75596bbabdb8`）；(b) `b3_merkle_root`＝**`45ef859b2be9`**、`state_22_after_22_captions`＝**`bbd61495cb5d`**、`ext_1_after_anchor2`＝**`bf492f1c8424`**，三者与旧①件逐字一致；`independent_rewalk_ok`＝`true` | `chain_summary` 逐字比对 |
| **K-PV02-11** | 禁触面 | ⛔ **0 跑 fetch 脚本**（`.tmp/_v5_c5_b_fetch_raw_embeddings.py` 未被调用）·**0 API**·**0 key**·**0 网络**·**0 合并任何派生 JSON**·**0 判档位**；§4 所列 15 件既有件跑后复算**全部同值** | 进程调用记录＋`Get-FileHash` |

---

## §3 测量面逐字比对表（新 vs 旧 · 递归全字段 · 非抽样）

**比对口径**：`walk(old, new)` 递归遍历全部键与数组元素，产出逐路径差异；再按 K-PV02-05 分类。
**分类**：`A` ＝ 新增键（允许）｜`B` ＝ 出处字段（允许）｜`C` ＝ `integrity.*`（允许）｜`D` ＝ §6 PINNED 扩面之必然差异（规格直接导致，非测量面）｜`E` ＝ **测量面**（须 0 差异）｜`F` ＝ **未列明差异**（须 0 差异）。

| 件 | 差异路径总数 | A 新增键 | B 出处 | C integrity | D PINNED 扩面 | **E 测量面** | **F 未列明** |
|---|---:|---:|---:|---:|---:|---:|---:|
| ① `deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | 17 | 1 | 3 | 3 | 10 | **0** | **0** |
| ② `index_v3_2026_10_09.json` | 7 | 2 | 2 | 3 | 0 | **0** | **0** |
| ③ `c5_b_group_fix_readings_2026_10_09.json` | 4 | 1 | 3 | 0 | 0 | **0** | **0** |

**逐条差异明细（0 抽样 · 全部列出）**

| 件 | 类别 | 路径 | 旧值 → 新值 |
|---|---|---|---|
| ① | A | `protocol_version` | `<ABSENT>` → `"V0.4"` |
| ① | B | `date` | `2026-09-29` → `2026-10-09` |
| ① | B | `task_id` | `V3X-C5B-RUNNER-2026-09-29-A1` → `V3X-C5B-RUNNER-2026-10-09-A1` |
| ① | B | `generator` | `..._v0_4_2026_09_29.py` → `..._v0_4_2026_10_09.py` |
| ① | C | `integrity.path_hashed`／`path_sha256`／`content_sha256` | 旧相对路径三项 → 新相对路径三项（`path_sha256` 独立复算一致） |
| ① | D | `zero_overwrite_proof.sha12_before`／`sha12_after` 各 **＋5 项** | 3 项 → 8 项（§6 PINNED 扩面；原 3 项值逐字未变） |
| ② | A | `protocol_version`／`protocol_version_axis` | `<ABSENT>` → `"V0.4"` ／ 轴声明串（§5.2 逐字） |
| ② | B | `index_v3_meta.date` | `2026-09-29` → `2026-10-09` |
| ② | B | `index_v3_meta.generator` | `..._v0_4_2026_09_29.py` → `..._v0_4_2026_10_09.py` |
| ② | C | `integrity.path_hashed`／`path_sha256`／`content_sha256` | 旧相对路径三项 → 新相对路径三项 |
| ③ | A | `protocol_version` | `<ABSENT>` → `"V0.4"` |
| ③ | B | `date` | `2026-10-01T09:25:22+08:00` → `2026-10-09T13:39:57+08:00`（wall-clock，`K-PV02-09`） |
| ③ | B | `task_id` | `V3X-C5B-FIX-2026-10-01-A1` → `V3X-C5B-FIX-2026-10-09-A1` |
| ③ | B | `generator` | `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` → `.tmp/_c5_b_group_fix_readings_2026_10_09.py` |

**E 类（测量面）逐项 0 差异之证明面**：`per_caption[*].{byte_hash, semantic_hash, dual, dual_hex_width, coords_k, chain, diff_registration_*}／chain_summary`（①）｜`captions／graphs／n_captions／fingerprint_anchors／index_v3_meta` 之各数值与内容项（②，含 `caliber` 档位、`dual_rule`、`base_index_sha256`、`caption_source_sha256`、`raw_embedding_source_sha256`、`svd_var_explained_k` 等全部未变）｜`per_caption／readings／cross_seed_control／degradation_guard`（③）—— 递归比对结果 **0 条差异**。
**另核**：`boundary.no_existing_file_modified` 旧＝新＝`true`（`K-PV02-05` 明确要求同值不改）。

---

## §4 pin 同值表（跑前 ／ 跑后）

| 路径 | 跑前 SHA-12 | 跑后 SHA-12 | 同值 |
|---|---|---|---|
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json`（①旧） | `33ad1c01f745` | `33ad1c01f745` | ✅ |
| `corpus/v20/index_v3_2026_09_29.json`（②旧） | `3ba2449cf986` | `3ba2449cf986` | ✅ |
| `results/c5_b_group_fix_readings_2026_10_01.json`（③旧） | `2a7749da7c4d` | `2a7749da7c4d` | ✅ |
| `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py`（R 旧本） | `de16bc002198` | `de16bc002198` | ✅ |
| `.tmp/_v5_c5_b_fix_readings_2026_10_01.py`（G 旧本） | `191efa7fe0b6` | `191efa7fe0b6` | ✅ |
| `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md`（规则面唯一载体） | `c13449101ab3` | `c13449101ab3` | ✅ |

**另有 9 件 `K-PV02-11` 禁触面文件跑后复算，全部与 PK 记录值逐字同值**：`2593ea7b93cf`（原裁承载件）／`bff06d3b3f97`（原裁登记件）／`1d1895489d17`（落地状态件）／`87ab4929477f`（待拍板母册）／`c5441e186c3f`（PK 准备件）／`8423ffe266af`（frozen base `corpus/v20/index.json`）／`6a2656878745`（captions 料）／`cf7682348617`（f4 料）／`1088fdd2b197`（raw 原料件）。

**R 脚本内置 pin 面（跑前 assert → 跑后打印）**：原 3 项（09-16 三件）＋扩面 5 项（①②③＋R 旧本＋G 旧本）＝ **8 项跑后全同值**，runner 自报 `zero_overwrite_unchanged: true`。

---

## §5 `K-PV02-04` 跑前书面二择一声明

### §5.1 声明（开跑**前**作出 · 逐条落账）

**取选项②**：`SPEC_REF_V04`／`spec_ref_pending` **逐字沿用、0 改码**，并在本回执**登记为「过时残留」**。

**理由**：选项①（去掉过时括注、改指在册 spec 并附 SHA-12）会改写②件 `index_v3_meta.spec_ref_pending` 与①件 `caliber.spec_ref_pending` 之字面；该二路径**不在 `K-PV02-05` 允许差异集**内 ⇒ 依 `K-PV02-05`「任一测量面字段变化 ⇒ 停手，判构造已变」之字面，选项①将构成**未列明的测量面漂移并自致 FAIL**。故取②：保测量面逐字 0 漂移，把过时事实的披露责任由本回执承担。

### §5.2 过时残留登记（照 PK §5.2 禁写清单）

- **残留字面（逐字，新旧件一致）**：`docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md (待 doc-writer 棒 2b 新增, 本件 0 代拟正文)`
- **该字面确已过时**：所指 spec **已在盘**（`c13449101ab3`／34,367 B，跑后复算同值）⇒ 括注「待…新增」与盘上事实不符，**登记为过时残留**，候 PI／verdict-keeper 择机处置（另立注记或下轮修订跑择①）。
- **轴声明串（②件 `protocol_version_axis` 逐字 · 本棒拟定面）**：
  > 「P-D 指纹协议轴: protocol_version=V0.4 指 docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md §2.4 之 P-D 指纹协议版本; 本件顶层 generator_version 与 spec 属 corpus 工具/规范轴 (corpus 版本面), 与本键分属不同轴, 互不覆盖; 本键 0 改写 corpus 版本, 且 0 可由 corpus 版本推得协议版本; 二者须并读, 0 择一为准」
- **该串之必要性依据**：②件顶层并存两条互不相干版本轴 —— `generator_version`＝`v2.0.0`、`spec`＝`docs/SPEC_v2.0.md §1`（corpus 工具／规范轴，实测读出），而 `index_v3_meta.spec_ref_pending`／`spec_ref_base` 指向 P-D 指纹协议（协议轴）⇒ 不声明轴归属则 `protocol_version` 极易被误读为 corpus 版本，构成**静默误导**，与 PI「不误导」之理由正面相悖。
- **拟定面归属声明**：串文属 worker 拟定面（PK §3.3 明示 ⛔ 0 由 protocol-keeper 代拟）；**声明义务与轴归属属 PK 固化，本棒 0 省略**。

---

## §6 root 漂移注记（**照登 · 0 重算**）

| 项 | 读数 | 出处 |
|---|---|---|
| `reproduce_max_abs_dev_vs_stored_svd2` | **`0.0089821568`** | ③件 `input_selfcheck`；源＝raw 原料件 `1088fdd2b197` 之 `reproduction_selfcheck` |
| `reproduce_within_4dp` | **`false`** | 同上；判据字面 `max_abs_dev <= 5e-4`（fetch 脚本 L134）⇒ `8.98e-03 > 5e-4` |

- ⛔ **0 重算／0 重取嵌入**：本次跑 **0 API、0 网络、0 key**；raw 22×2048 向量为上游 fetch 产物，两脚本**只读**（G docstring L24 逐字「本脚本只读」）。
- ⛔ **声称「drift 已消／已复测／已复现」＝ 误导**；本件**仅**登记「该读数自 raw 逐字携带」，⛔ 0 称 `false` 为本次新增失败读数（它是 2026-10-01 之既有读数之原样携带）。
- **键名别名登记**：①件键名 `raw_embedding_reproduces_stored_svd2` 与 ③件键名 `reproduce_within_4dp` **同指一读数**（别名，非两读数）⇒ 引用须注明取自哪件，⛔ 0 跨件并列为两条独立证据。
- **三形同值**：clue book `8.98e-03` ／终稿 L450 `8.98e-03` ／raw 精确值 `0.0089821568` ⇒ 同值不同形，⛔ 0 当作三个读数。
- **禁述继承**：⛔ 0 说「C5 已修好／修好成立／坍缩已解除」；⛔ 0 说「SVD-3 坐标坍缩命题已死」；⛔ 0 以均值 3.026 作「区分力改善」主张（码长效应混淆）；⛔ **0 说「0 退化警报」**（`any_alarm=false` 仅覆盖该 guard 之 3 项；10-01 已实测 7 项 `n_distinct ≤ 3` 命中项，见 `bff06d3b3f97` L146）。

---

## §7 新件指纹自报（写入方实测 · 0 自指本件）

| 件 | SHA-256 | SHA-12 | bytes | BOM | CRLF | 裸 LF |
|---|---|---|---:|---|---|---:|
| ① `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `95f3f0957be87ac1f48d4121c72eea26b58920f3b470ff4b916ec22deead463b` | `95f3f0957be8` | 21,176 | 无 | 747 | 0 |
| ② `corpus/v20/index_v3_2026_10_09.json` | `74b27393574fe7cc0654ac16e6a6281f66b64b60ab1fe164143113f9e2948820` | `74b27393574f` | 24,837 | 无 | 581 | 0 |
| ③ `results/c5_b_group_fix_readings_2026_10_09.json` | `4e415990b71d2a5bce4f7d0856e3a24b3fbddc9b27a841a1bbc9d85ee02fb9c3` | `4e415990b71d` | 10,029 | 无 | 448 | 0 |
| R 副本 `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py` | `7c095c54fb998bfc1757755dd9da7efca974c36942767df5ad37af39a14d123f` | `7c095c54fb99` | 21,826 | 无 | 0 | 473 |
| G 副本 `.tmp/_c5_b_group_fix_readings_2026_10_09.py` | `b6855b38acc2a20dfdcaba2bd85863ee8322e0eec0b78b3f565c63c90342f630` | `b6855b38acc2` | 12,289 | 无 | 0 | 278 |

> 本件（登记件）自身 SHA-256／SHA-12／字节／行尾由写入方**落盘后实测回报**（⛔ 0 自指），读数见回执正文。

> ⚠️ **版式偏差如实登记（候呈项，非 `K-PV02` 任一条 FAIL）**：三件 JSON 落盘为 **CRLF**，与既有 ①②③（09-29／10-01 件，同为 100% CRLF）**同形**。成因＝两脚本之 `write_text(..., encoding="utf-8")` 在 Windows 上行尾翻译，**该写出调用系既有代码，本棒一字未改**。故 ⛔ **0 事后转 LF**：强转会破坏「重跑即复现」（重跑未改码脚本仍得 CRLF 与不同 SHA-12），且超出乙档改动清单。⇒ **候选处置归 PI／verdict-keeper**（是否将 JSON 产出面统一规范为 LF，属跨件体例问题）。

---

## §8 0 回改 ／ 0 网络 ／ 0 key ／ 0 判档位 自证

| 声明 | 实测支撑 |
|---|---|
| **0 回改任何既有件** | §4 pin 表 6 件 ＋ 禁触面 9 件，跑后 `Get-FileHash` 复算**全部逐字同值**（byte 0 触动）；R 内置 8 项 pin 跑后全同值 |
| **0 覆写** | 三新名落前 `Test-Path=False`（§9.2）＋ glob 0 命中 ⇒ 写入面为新建，⛔ 0 补救性覆写 |
| **0 网络 · 0 API** | 本棒仅执行 `python <两副本>`；⛔ **未运行** `.tmp/_v5_c5_b_fetch_raw_embeddings.py`；两脚本自身 0 网络（R docstring L26-27 逐字「0 network / 0 LLM / 0 API call inside this runner」） |
| **0 key** | ⛔ 0 读 `.env`／`config.yaml`／`mcp.json`／任何凭据面；**R4 key 永不明文**；G docstring L24 逐字「0 网络 0 LLM 0 key」，`boundary.no_key` 沿用 |
| **0 判档位** | 本件 0 判 PASS/FAIL/KD 之档位归属，⛔ 0 判 `U-V04-01` 闭合，⛔ 0 判 C5 生死；§2 之「PASS」仅为**机械判据逐条读数**之陈述，**判读归 verdict-keeper** |
| **0 合并派生 JSON · 0 触 frozen** | ⛔ 0 写 `corpus/v20/index.json`（跑后 `8423ffe266af` 同值，`frozen_proof.unchanged=true`）；⛔ 0 合并任何派生 JSON |
| **0 阶段名自升** | 三新名**仅换日期段**（`_2026_09_29`／`_2026_10_01` → `_2026_10_09`），**词干逐段未换**、⛔ 0 新增 `_pv04_`／`_revised_`／`_r2_` 等语义后缀；G 副本名按 §3.2 **0 沿用 `_v5_` 前缀**；件名 0 含 V-阶段首段 |

---

## §9 残留 ／ 副产物 ／ 未做面

### §9.1 编译副产物（2 件，0 清理）

`py_compile` 双通过时生成 `.tmp/_g_compile_check.pyc` 与 `deposon_team/plugins/__pycache__/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.cpython-314.pyc`。**清理被运行时拦截**（`rm` 目标路径含中文，被拼为 `...\〔本地目录已脱敏〕deposon-repo.tmp_...` 而报「dangerous removal target」）⇒ 依纪律**0 绕过、0 改用其它删除命令**，如实登记为残留，候处置。

### §9.2 撞名实测（落盘前）

- 三产出新名 `Test-Path` ＝ `False`／`False`／`False`；两副本新名 ＝ `False`／`False`；本登记件名 ＝ `False`（备选名 2 个亦 `False`）。
- 全仓递归 glob `**/*2026_10_09*` ＝ **57 命中**，逐条核对**无一件为我方 5 个新名**。

### §9.3 未做面（显式列出）

1. **0 改 R 副本 docstring 之 out 件名**：该 docstring L3／L5-8 仍逐字列 09-29 之产出名。PK §6「改何物」明列之必改面为 §3.4 五类出处字段／路径，docstring **不在清单内** ⇒ 本棒**从严取「仅新增＋5 类同步」**，未作清单外改动。**如实登记为残留**（新副本内含旧产出名之注释），候 PI／verdict-keeper 择机处置。
2. **0 改 `zero_overwrite_proof.policy` 之文字**：该策略串沿用旧件原字（「0 覆写 2026-09-16 两件 B3 既有产出 + 既有 runner」），实际 pin 集以 `sha12_before/after` 枚举（已扩至 8 项）⇒ 该文字仍属实但**未反映扩面**；同上从规格从严，登记备查。
3. **0 处置 `spec_ref_pending` 过时残留之字面本身**（见 §5.1，取选项②）。
4. **0 跑 fetch 脚本、0 重取嵌入、0 重算 SVD**（见 §6）。
5. **0 写任何证据/落册件之外的派生件**：本棒写入面 ＝ 三产出＋两副本＋本登记件，共 **6 件新文件**。
6. **0 补 `protocol_version_axis` 于 ①③ 件**：该伴生键依 PK §3.3 仅 ② 件必需（①③ 无双版本轴并存的误读面）⇒ 未越规格添加。

---

## §10 交棒

- 本棒交付物交 **verdict-keeper**，由其判 `U-V04-01` **产出层**之闭合与否；⛔ **本棒 0 判**。
- ⛔ **0 由此外推**「`U-V04-01` 已闭合」「缺口已闭合」「C5 已修好」——**闭合判定归 verdict-keeper**。
- ⛔ **0 提前宣告**「键已写入且验收通过」；本件仅陈述：**三件新名产出已在盘、键级命中逐件以读数为证、测量面零漂移**。
- **候呈项（PI／verdict-keeper）**：① 三件 JSON 之 CRLF 体例（§7）② `spec_ref_pending` 过时残留字面处置（§5.1）③ R 副本 docstring 与 `zero_overwrite_proof.policy` 之清单外文字（§9.3①②）④ 两个 `.pyc` 副产物清理（§9.1）。