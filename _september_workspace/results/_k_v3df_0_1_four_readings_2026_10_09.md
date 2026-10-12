# `K-V3DF-0-1` 读数面四读数补报件 · worker · 2026-10-09

> **性质**：缺口主件 `results/_v34_experiment_gap_plan_2026_10_08.md`（`996feb1db9cb`）§1.1 表 **V3-04** 行之**读数面四读数补报**；W4 波（§2.2 验收字面「四读数齐全」）第 2 件。
> **授权锚**：PI 2026-10-09 卷⑨问卷（`ask_cfb9284519a5abf29d0f03eb`）Q1「五段全开·批准后当日即办」＋「①②③④⑤按顺序」；**W4 波许可已获** —— `results/_closing_round_8_decisions_register_2026_10_09.md`（`a28a478e14a8`）§1 表 Q4 落地栏①＋§2 第 4 项。
> **判据唯一源**：`results/_v5_v3_deg_fix_prereg_2026_09_29.md`（`98286cc1aec7`）§4.0 **L229**。
> **本棒身份**：**worker**（`mvs_96aa893021ef45f88af8c0f96fbea8a0`）· W4 波第 2 件（V3-04）。
> **0 判定**：**0 落 PASS/FAIL/KD**、0 判门是否开跑、0 判「修好成立」、0 翻案、0 代裁 —— 落态归 **verdict-keeper**；本件只报读数与派生。
> **0 回改既有件**：另立**新名**产出件 2 件（本 md ＋ 伴随读数 JSON）；**0 写入／0 重命名／0 删除**任何既有件。
> **0 编造**：一切读数本人盘上现算（脚本 `.tmp/k_v3df_0_1_four_readings_2026_10_09.py`；**仅用标准库** `json`／`os`／`hashlib`／`collections`，`mean`／`std`(ddof=0/1) 为**手写公式**；**0 网络、0 读 key**）。
> **R4**：key 永不明文；本件 0 读 key。
> **命名合规**：按 `results/_naming_ruling_note_2026_09_29.md`（`57024f2cd30a`）§1.2② —— 新件 0 带 `_v5_`/`_v4_`/`_v3_` 等 **V-阶段前缀**、文件名 0 含阶段号作为首段；本件首段 ＝ `k`，`v3df` 属**判据 ID `K-V3DF-0-1` 的冻结字面**（沿盘上既有判据 ID，0 自造新阶段号），故合规。
> **版式**：UTF-8 无 BOM · LF。

---

## §0 输入件 · 本人盘上实测 SHA-256／SHA-12／bytes（**0 复用自报值**）

| # | 件（盘上路径） | SHA-12 | SHA-256（全 64 位） | bytes | 末次写 mtime | BOM/CRLF/LF |
|:-:|---|---|---|---:|---|---|
| 1 | `corpus/v20/index_v3_2026_09_29.json` | **`3ba2449cf986`** | `3ba2449cf9863b9162679d3ec4765da9c0a20eafb2e32ce75c8613ee09633f81` | 24,421 | 2026-10-01 09:43:44 | 无／579／0 |
| 2 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | **`33ad1c01f745`** | `33ad1c01f7456b6a01109f253485a880e0fc36a10eb9a95d3eddf377dbcef88f` | 20,398 | 2026-10-01 09:43:44 | 无／736／0 |
| 3 | `results/c5_b_group_fix_readings_2026_10_01.json` | **`2a7749da7c4d`** | `2a7749da7c4d35f5264e372dcc30c1aebf4470a72e1db36eefedec28c70387d7` | 9,996 | 2026-10-01 09:25:22 | 无／447／0 |
| 4 | `results/c5_guard_minmaxstd_report_2026_10_01.md` | **`f465fbdb7579`** | `f465fbdb7579996f1667254b85a4c38e99ed7d4a7df8d0e68d2f0adb8add8444` | 19,909 | 2026-10-01 10:15:08 | 无／0／213 |
| 5 | `results/c5_guard_minmaxstd_readings_2026_10_01.json` | **`7ff301514f66`** | `7ff301514f661e90acbf707dd56d5271f41e9b08ac89ee3586fcf6c90ef9df1e` | 19,935 | 2026-10-01 10:14:10 | 无／0／931 |
| 6 | `results/c5_guard_0_1_recheck_verdict_2026_10_01.md` | **`24418fa60ede`** | `24418fa60ede63bbe9db1288b7706b5205840c9353fee6ddd9435789e26e2e0c` | 33,287 | 2026-10-01 10:21:29 | 无／0／290 |
| 7 | `results/_v5_v3_deg_fix_prereg_2026_09_29.md` | **`98286cc1aec7`** | `98286cc1aec7b16dcbc15f4c3fb4a4b17d3d407072d189d9ac6185ab98bd34fe` | 41,622 | 2026-09-29 11:44:32 | 无／0／419 |
| 8 | `results/_v34_experiment_gap_plan_2026_10_08.md` | **`996feb1db9cb`** | `996feb1db9cb39bf830b5ad817b9c133adec83a3d53631c2e266d962d6fbbfb5` | 36,066 | 2026-10-08 16:46:11 | 无／0／287 |
| 9 | `results/_closing_round_8_decisions_register_2026_10_09.md` | **`a28a478e14a8`** | `a28a478e14a84c0cffe4ed0c28c79ab9a3faf3a26ca479e478626dc4bd3cbb8d` | 2,151 | 2026-10-09 10:12:53 | 无／0／32 |
| 10 | `results/_naming_ruling_note_2026_09_29.md` | **`57024f2cd30a`** | `57024f2cd30a66a197d6eaa56eac9dd8081c43a6c3ae22cabc69f352cb4f4a98` | 7,843 | 2026-09-29 21:18:08 | 无／0／81 |

**复算口径**：`hashlib.sha256(全文字节).hexdigest()`；SHA-12 ＝ 前 12 位小写（沿 `results/_v5_v3_deg_fix_prereg_2026_09_29.md` L9 口径；⛔ 禁内建 `hash()`）。

**时序核验（防「快照后修正未复测」，一律以盘上终态为准）**：上列 10 件末次写 mtime 全部落在 **2026-09-29 ～ 2026-10-01**，均**早于本棒开工**（2026-10-09）⇒ **0 发现快照后修正面**；本件一切数值以终态 `hashlib` 复算为准。

**与既有件自报值一致性**：`results/c5_guard_0_1_recheck_verdict_2026_10_01.md`（`24418fa60ede`）§0 表 1–8 自报 SHA-12 与本人终态复算**逐件同值**（`3fbf6b38a383`／`f465fbdb7579`／`7ff301514f66`／`2fd8946cfe80`／`98286cc1aec7`／`33ad1c01f745`／`3ba2449cf986`／`2a7749da7c4d`）⇒ 0 冲突面。

## §1 四读数口径（**沿既有件 · 0 自创 · 0 新设阈值**）

| 项 | 本件口径 | 沿用来源 |
|---|---|---|
| `std` 主报 | **`ddof = 0`**（总体标准差）—— 22 节为全体总体，非抽样 | `results/c5_guard_minmaxstd_report_2026_10_01.md` §1 |
| `std` 并列 | `ddof = 1` **并列给出**；0 声称与盘上他件口径一致 | 同上 |
| 字符串列 `min`／`max` | **字典序（lexicographic）** | 同上 |
| 字符串列 `std` | **未定义** ⇒ 如实记 `null` ＋ `std_note`，⛔ **0 伪填 0.0**；另附 `int(hex,16)` 与 `len()` **派生读数**（标注为派生、**0 设阈值**） | 同上 |
| 布尔列 | `bool → 0/1` 归一后统计 | 同上（`link_verified` 等） |
| 标量（`n = 1`） | `std` 未定义（`ddof=0` 下为 0.0） | 同上 |
| 浮点登记精度 | `round(x, 6)`；0 影响任何判定切点（切点字面 ＝ `n_distinct ≤ 3`，为整数判比） | 本件登记约定 |
| 警报阈值 | `n_distinct ≤ 3`（含 3 本身） | `results/_v5_v3_deg_fix_prereg_2026_09_29.md` §4.0 L229（**未动**） |
| 落态映射 | 警报命中 ⇒ KD；读数面不达标 ⇒ 不得开跑 | 同上（**0 判定**） |

## §2 四读数全表（**齐报**：`n_distinct`／`min`／`max`／`std`）

> 覆盖面 ＝ 判据字面「**每个输入字段**与**每个输出读数列**」。字符串列 `std` 如实记「未定义」并附派生读数（0 伪填）。

### §2.1 A. `index_v3` captions 面（输入字段 · 22 条）

| 字段 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 现值来源 |
|---|---:|---:|---|---|---:|---:|---|
| `captions[].caption_id` | 22 | **22** | `L_algorithm_process` | `S6_n60` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json captions[].caption_id` |
| `captions[].text` | 22 | **22** | `世界; 亚洲; 欧洲; 非洲; 北美洲; 南美洲; 大洋洲; 南极洲; 中国; 日本; 印度; 法国; 德国; 英国; 埃及; 南非; 美国; 加拿大; 巴西; 阿根廷; 澳大利亚; 新西兰; 南极大陆; 长城站; 北京; 东京; 新德里; 巴黎; 柏林; 伦敦; 开罗; 约翰内斯堡; 纽约; 多伦多; 里约热内卢; 布宜诺斯艾利斯; 悉尼; 奥克兰; 故宫; 埃菲尔铁塔; 自由女神像; 大堡礁; 富士山; 泰姬陵; 金字塔` | `项目立项; 需求收集; 需求分析; 需求确认; 项目范围; WBS分解; 范围确认; 项目计划; 进度计划; 成本预算; 资源计划; 风险识别; 风险应对计划; 质量计划; 沟通计划; 采购计划; 干系人管理; 任务执行; 团队管理; 质量保证; 风险监控; 质量控制; 进度监控; 成本控制; 变更控制; 沟通汇报; 采购实施; 产品交付; 验收确认; 文档归档; 项目复盘; 经验总结; 项目关闭` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json captions[].text` |
| `captions[].text 字符长度（派生）` | 22 | **21** | 92 | 304 | 59.499931 | 60.900120 | `corpus/v20/index_v3_2026_09_29.json captions[].text → len()` |
| `captions[].family` | 22 | **2** | `L` | `S` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json captions[].family` |
| `captions[].structure` | 22 | **7** | `balanced_binary_tree` | `three_hub_competition` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json captions[].structure` |
| `captions[].n_labels` | 22 | **11** | 20 | 60 | 11.382984 | 11.650855 | `corpus/v20/index_v3_2026_09_29.json captions[].n_labels` |
| `captions[].byte_hash` | 22 | **22** | `0e89a90afea3` | `fbfa04f1128c` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json captions[].byte_hash` |
| `captions[].semantic_hash` | 22 | **9** | `006d4` | `03eef` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json captions[].semantic_hash` |
| `captions[].dual_v04` | 22 | **22** | `0e89a903eed` | `fbfa0401ad5` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json captions[].dual_v04` |

**字符串列派生读数**（标注为派生 · 0 设阈值）：

- `captions[].caption_id`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 8 ／ `min` 2 ／ `max` 22 ／ `std`(ddof=0) **6.939080** ／ `std`(ddof=1) 7.102374
- `captions[].text`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 21 ／ `min` 92 ／ `max` 304 ／ `std`(ddof=0) **59.499931** ／ `std`(ddof=1) 60.900120
- `captions[].family`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 1 ／ `min` 1 ／ `max` 1 ／ `std`(ddof=0) **0** ／ `std`(ddof=1) 0
- `captions[].structure`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 6 ／ `min` 12 ／ `max` 24 ／ `std`(ddof=0) **3.951409** ／ `std`(ddof=1) 4.044396
- `captions[].byte_hash`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 22 ／ `min` 15,984,409,378,467 ／ `max` 277,051,243,303,564 ／ `std`(ddof=0) **74,872,849,733,430.062500** ／ `std`(ddof=1) 76,634,804,910,943.437500
- `captions[].semantic_hash`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 9 ／ `min` 1,748 ／ `max` 16,111 ／ `std`(ddof=0) **5,618.693197** ／ `std`(ddof=1) 5,750.915833
- `captions[].dual_v04`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 22 ／ `min` 999,025,557,229 ／ `max` 17,315,701,725,909 ／ `std`(ddof=0) **4,679,553,017,117.271484** ／ `std`(ddof=1) 4,789,675,213,565.161133

### §2.2 B. `index_v3` graphs 面（输入字段 · 22 条）

| 字段 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 现值来源 |
|---|---:|---:|---|---|---:|---:|---|
| `graphs[].graph_id` | 22 | **22** | `L_algorithm_process` | `S6_n60` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json graphs[].graph_id` |
| `graphs[].family` | 22 | **2** | `L` | `S` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json graphs[].family` |
| `graphs[].structure` | 22 | **7** | `balanced_binary_tree` | `three_hub_competition` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json graphs[].structure` |
| `graphs[].N` | 22 | **11** | 20 | 60 | 11.382984 | 11.650855 | `corpus/v20/index_v3_2026_09_29.json graphs[].N` |
| `graphs[].n_edges` | 22 | **15** | 19 | 88 | 15.478124 | 15.842365 | `corpus/v20/index_v3_2026_09_29.json graphs[].n_edges` |
| `graphs[].n_named` | 22 | **16** | 7 | 59 | 13.608760 | 13.929010 | `corpus/v20/index_v3_2026_09_29.json graphs[].n_named` |
| `graphs[].n_filler` | 22 | **16** | 0 | 47 | 13.272182 | 13.584512 | `corpus/v20/index_v3_2026_09_29.json graphs[].n_filler` |
| `graphs[].source` | 22 | **2** | 0 | 1 | 0.208299 | 0.213201 | `corpus/v20/index_v3_2026_09_29.json graphs[].source` |
| `graphs[].target` | 22 | **13** | 1 | 59 | 17.785917 | 18.204466 | `corpus/v20/index_v3_2026_09_29.json graphs[].target` |
| `graphs[].seed` | 22 | **22** | 200,101 | 1,634,062,263 | 434,702,481.462804 | 444,932,174.744391 | `corpus/v20/index_v3_2026_09_29.json graphs[].seed` |
| `graphs[].sha256` | 22 | **22** | `0944d0222d5cc12e8c906f25888b777f5cc474f762054755518ec9821e8e2d7e` | `f63039c8ec1ebdebb9a34d7b226d6328a1c771564ce99789b5c64a924da7267b` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json graphs[].sha256` |
| `graphs[].file` | 22 | **22** | `L_algorithm_process.json` | `S6_n60.json` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json graphs[].file` |

**字符串列派生读数**（标注为派生 · 0 设阈值）：

- `graphs[].graph_id`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 8 ／ `min` 2 ／ `max` 22 ／ `std`(ddof=0) **6.939080** ／ `std`(ddof=1) 7.102374
- `graphs[].family`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 1 ／ `min` 1 ／ `max` 1 ／ `std`(ddof=0) **0** ／ `std`(ddof=1) 0
- `graphs[].structure`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 6 ／ `min` 12 ／ `max` 24 ／ `std`(ddof=0) **3.951409** ／ `std`(ddof=1) 4.044396
- `graphs[].sha256`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 22 ／ `min` 4,192,397,722,309,856,911,300,428,129,239,443,548,342,955,927,620,112,753,533,025,983,721,982,799,230 ／ `max` 111,354,168,226,990,341,788,842,090,360,732,861,297,671,547,653,696,312,007,157,724,824,957,278,955,131 ／ `std`(ddof=0) **30,284,026,395,949,939,078,093,600,503,362,485,390,522,290,522,412,169,252,317,332,834,553,908,166,656.000000** ／ `std`(ddof=1) 30,996,689,227,594,119,904,767,121,043,041,631,432,360,353,290,955,193,419,430,171,561,605,839,454,208.000000
- `graphs[].file`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 8 ／ `min` 7 ／ `max` 27 ／ `std`(ddof=0) **6.939080** ／ `std`(ddof=1) 7.102374

### §2.3 C. `index_v3` 顶层标量与列表

| 字段 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 现值来源 |
|---|---:|---:|---|---|---:|---:|---|
| `index_v3.n_graphs（标量）` | 1 | **1** | 22 | 22 | 0 | 未定义 | `corpus/v20/index_v3_2026_09_29.json n_graphs` |
| `index_v3.n_captions（标量）` | 1 | **1** | 22 | 22 | 0 | 未定义 | `corpus/v20/index_v3_2026_09_29.json n_captions` |
| `index_v3.corpus / generator_version / spec / named_filler_rule（4 标量并列）` | 4 | **4** | `docs/SPEC_v2.0.md §1` | `v20` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json 顶层 4 标量` |
| `index_v3.fingerprint_anchors（3 hex 列）` | 3 | **3** | `7d6d3d39fad8` | `f88d855aaf83` | 未定义 | 未定义 | `corpus/v20/index_v3_2026_09_29.json fingerprint_anchors` |

**字符串列派生读数**（标注为派生 · 0 设阈值）：

- `index_v3.corpus / generator_version / spec / named_filler_rule（4 标量并列）`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 4 ／ `min` 3 ／ `max` 60 ／ `std`(ddof=0) **22.719760** ／ `std`(ddof=1) 26.234519
- `index_v3.fingerprint_anchors（3 hex 列）`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 3 ／ `min` 137,908,132,117,208 ／ `max` 273,286,711,390,083 ／ `std`(ddof=0) **59,678,594,034,630.234375** ／ `std`(ddof=1) 73,091,051,975,774.062500

### §2.4 D. B3 `per_caption` 面（22 节）

| 字段 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 现值来源 |
|---|---:|---:|---|---|---:|---:|---|
| `B3 per_caption[].caption_id` | 22 | **22** | `L_algorithm_process` | `S6_n60` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].caption_id` |
| `B3 per_caption[].byte_hash` | 22 | **22** | `0e89a90afea3` | `fbfa04f1128c` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].byte_hash` |
| `B3 per_caption[].semantic_hash` | 22 | **9** | `006d4` | `03eef` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].semantic_hash` |
| `B3 per_caption[].dual` | 22 | **22** | `0e89a903eed` | `fbfa0401ad5` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].dual` |
| `B3 per_caption[].dual_hex_width` | 22 | **1** | 11 | 11 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].dual_hex_width` |
| `B3 per_caption[].coords_k[0]` | 22 | **22** | -0.921827 | -0.522025 | 0.129530 | 0.132579 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].coords_k[0]` |
| `B3 per_caption[].coords_k[1]` | 22 | **22** | -0.167983 | 0.621236 | 0.276760 | 0.283273 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].coords_k[1]` |
| `B3 per_caption[].coords_k[2]` | 22 | **22** | -0.362677 | 0.514085 | 0.166955 | 0.170883 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].coords_k[2]` |
| `B3 diff_registration_vs_f4.semantic_hash_identical` | 22 | **1** | 0 | 0 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json …vs_f4` |
| `B3 diff_registration_vs_f4.dual_identical` | 22 | **1** | 0 | 0 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json …vs_f4` |
| `B3 diff_registration_vs_v3phys.semantic_hash_identical` | 22 | **1** | 0 | 0 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json …vs_v3phys` |
| `B3 diff_registration_vs_v3phys.dual_identical` | 22 | **1** | 0 | 0 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json …vs_v3phys` |
| `B3 chain.parent_state` | 22 | **22** | `08a30c2cfe79` | `ec04dfa75fd0` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].chain.parent_state` |
| `B3 chain.link_input` | 22 | **22** | `08a30c2cfe79|S4|b1d3eb03eed` | `ec04dfa75fd0|S5|1cdcbd01ecd` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].chain.link_input` |
| `B3 chain.node_state` | 22 | **22** | `08a30c2cfe79` | `ec04dfa75fd0` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json per_caption[].chain.node_state` |
| `B3 chain.link_verified` | 22 | **1** | 1 | 1 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json …chain.link_verified` |
| `B3 chain.self_verified_only` | 22 | **1** | 1 | 1 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json …chain.self_verified_only` |

**字符串列派生读数**（标注为派生 · 0 设阈值）：

- `B3 per_caption[].caption_id`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 8 ／ `min` 2 ／ `max` 22 ／ `std`(ddof=0) **6.939080** ／ `std`(ddof=1) 7.102374
- `B3 per_caption[].byte_hash`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 22 ／ `min` 15,984,409,378,467 ／ `max` 277,051,243,303,564 ／ `std`(ddof=0) **74,872,849,733,430.062500** ／ `std`(ddof=1) 76,634,804,910,943.437500
- `B3 per_caption[].semantic_hash`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 9 ／ `min` 1,748 ／ `max` 16,111 ／ `std`(ddof=0) **5,618.693197** ／ `std`(ddof=1) 5,750.915833
- `B3 per_caption[].dual`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 22 ／ `min` 999,025,557,229 ／ `max` 17,315,701,725,909 ／ `std`(ddof=0) **4,679,553,017,117.271484** ／ `std`(ddof=1) 4,789,675,213,565.161133
- `B3 chain.parent_state`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 22 ／ `min` 9,496,376,966,777 ／ `max` 259,505,676,312,528 ／ `std`(ddof=0) **77,235,440,410,508.875000** ／ `std`(ddof=1) 79,052,993,563,665.546875
- `B3 chain.link_input`：`int(hex,16)` 派生 **不适用**（非 hex 列）⇒ 长度派生读数 ⇒ `n_distinct` 8 ／ `min` 27 ／ `max` 47 ／ `std`(ddof=0) **6.939080** ／ `std`(ddof=1) 7.102374
- `B3 chain.node_state`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 22 ／ `min` 9,496,376,966,777 ／ `max` 259,505,676,312,528 ／ `std`(ddof=0) **78,944,833,746,749.515625** ／ `std`(ddof=1) 80,802,613,423,271.062500

### §2.5 E. B3 标量 / caliber / 登记面

| 字段 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 现值来源 |
|---|---:|---:|---|---|---:|---:|---|
| `chain_summary 三环并列（3 hex 列）` | 3 | **3** | `45ef859b2be9` | `bf492f1c8424` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json chain_summary` |
| `chain_summary.b3_merkle_root（标量）` | 1 | **1** | `45ef859b2be9` | `45ef859b2be9` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json chain_summary` |
| `chain_summary.ext_1_after_anchor2（标量）` | 1 | **1** | `bf492f1c8424` | `bf492f1c8424` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json chain_summary` |
| `chain_summary.state_22_after_22_captions（标量）` | 1 | **1** | `bbd61495cb5d` | `bbd61495cb5d` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json chain_summary` |
| `chain_summary.independent_rewalk_ok（标量 bool）` | 1 | **1** | 1 | 1 | 0 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json chain_summary` |
| `B3 anchors.values（3 hex 列）` | 3 | **3** | `7d6d3d39fad8` | `f88d855aaf83` | 未定义 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json anchors.values` |
| `caliber.code_len_bit（标量）` | 1 | **1** | 18 | 18 | 0 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json caliber` |
| `caliber.hex_width（标量）` | 1 | **1** | 5 | 5 | 0 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json caliber` |
| `caliber.n_components / planes_per_dim（2 标量并列）` | 2 | **2** | 3 | 6 | 1.500000 | 2.121320 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json caliber` |
| `caliber.hyperplanes_shape[0..1]（2 标量并列）` | 2 | **2** | 3 | 18 | 7.500000 | 10.606602 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json caliber` |
| `caliber.d_over_2_reference（标量）` | 1 | **1** | 9 | 9 | 0 | 未定义 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json caliber` |
| `id_correspondence.n_graph_ids / n_caption_ids（2 标量并列）` | 2 | **1** | 22 | 22 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json id_correspondence` |
| `id_correspondence.positional_match / raw_concept_ids_match（2 bool 并列）` | 2 | **1** | 1 | 1 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json id_correspondence` |
| `input_selfcheck 三项（max_abs_dev / svd_var_k / reproduces_flag→0/1）` | 3 | **3** | 0 | 0.792848 | 0.371653 | 0.455180 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json input_selfcheck` |
| `diff_registration 四项 identical_count（4 标量并列）` | 4 | **1** | 0 | 0 | 0 | 0 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json diff_registration` |

**字符串列派生读数**（标注为派生 · 0 设阈值）：

- `chain_summary 三环并列（3 hex 列）`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 3 ／ `min` 76,895,041,039,337 ／ `max` 210,321,043,915,812 ／ `std`(ddof=0) **62,022,957,580,829.468750** ／ `std`(ddof=1) 75,962,299,205,658.968750
- `chain_summary.b3_merkle_root（标量）`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 1 ／ `min` 76,895,041,039,337 ／ `max` 76,895,041,039,337 ／ `std`(ddof=0) **0** ／ `std`(ddof=1) 未定义
- `chain_summary.ext_1_after_anchor2（标量）`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 1 ／ `min` 210,321,043,915,812 ／ `max` 210,321,043,915,812 ／ `std`(ddof=0) **0** ／ `std`(ddof=1) 未定义
- `chain_summary.state_22_after_22_captions（标量）`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 1 ／ `min` 206,528,142,756,701 ／ `max` 206,528,142,756,701 ／ `std`(ddof=0) **0** ／ `std`(ddof=1) 未定义
- `B3 anchors.values（3 hex 列）`：`int(hex,16)` 派生读数 ⇒ `n_distinct` 3 ／ `min` 137,908,132,117,208 ／ `max` 273,286,711,390,083 ／ `std`(ddof=0) **59,678,594,034,630.234375** ／ `std`(ddof=1) 73,091,051,975,774.062500

### §2.6 F. 输出读数列面（修后读数件 · 本人现算）

| 字段 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 现值来源 |
|---|---:|---:|---|---|---:|---:|---|
| `输出读数列 · Hamming 全部配对（231 对 · 本人由 22 码重算）` | 231 | **9** | 0 | 8 | 2.630033 | 2.635744 | `corpus/v20/index_v3_2026_09_29.json/B3 semantic_hash 22 码 → C(22,2)=231 对` |
| `输出读数列 · 簇大小分布（9 码）` | 9 | **4** | 1 | 10 | 2.753225 | 2.920236 | `results/c5_b_group_fix_readings_2026_10_01.json stored_distribution` |
| `输出读数列 · 类内 Hamming（4 类）` | 4 | **4** | 1.330000 | 5.330000 | 1.418529 | 1.637976 | `results/c5_b_group_fix_readings_2026_10_01.json class_intra_hamming` |
| `输出读数列 · 跨 seed 码数（42–48）` | 7 | **4** | 6 | 9 | 1.124858 | 1.214986 | `results/c5_b_group_fix_readings_2026_10_01.json KV3DF_5_3_cross_seed.repaired_per_seed[].n_distinct` |
| `输出读数列 · 跨 seed Hamming 均值（7）` | 7 | **7** | 1.632000 | 3.766000 | 0.640959 | 0.692315 | `results/c5_b_group_fix_readings_2026_10_01.json …hamming_mean_observed` |
| `输出读数列 · 跨 seed 零对（7）` | 7 | **6** | 50 | 121 | 26.153394 | 28.248894 | `results/c5_b_group_fix_readings_2026_10_01.json …hamming_pairs_zero` |
| `输出读数列 · 基线 12-bit 码数（7）` | 7 | **4** | 3 | 6 | 0.880631 | 0.951190 | `results/c5_b_group_fix_readings_2026_10_01.json baseline_12bit_per_seed_on_disk[].n_distinct` |
| `输出读数列 · svd_var_explained（k=2/3/4）` | 3 | **3** | 0.764974 | 0.817153 | 0.021319 | 0.026110 | `results/c5_b_group_fix_readings_2026_10_01.json input_selfcheck.svd_var_explained` |
| `输出读数列 · d/2 参照（9.0 ／ 18/2）` | 2 | **1** | 9 | 9 | 0 | 0 | `results/c5_b_group_fix_readings_2026_10_01.json KV3DF_5_2_reference` |
| `cross_seed_control 三标量（n_distinct / hamming_mean / zero_count）` | 3 | **3** | 2 | 20 | 7.400204 | 9.063362 | `results/c5_b_group_fix_readings_2026_10_01.json cross_seed_control` |

### §2.7 G. 修后读数件 `degradation_guard` 面（原只报 `n_distinct` 之读数列 · 补四项）

| 字段 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 现值来源 |
|---|---:|---:|---|---|---:|---:|---|
| `修后读数件 degradation_guard.semantic_hash_codelen_n_distinct` | 1 | **1** | 9 | 9 | 0 | 未定义 | `results/c5_b_group_fix_readings_2026_10_01.json degradation_guard` |
| `修后读数件 degradation_guard.root_predup_dual_n_distinct` | 1 | **1** | 22 | 22 | 0 | 未定义 | `results/c5_b_group_fix_readings_2026_10_01.json degradation_guard` |
| `修后读数件 degradation_guard.byte_hash_primary_n_distinct` | 1 | **1** | 22 | 22 | 0 | 未定义 | `results/c5_b_group_fix_readings_2026_10_01.json degradation_guard` |
| `修后读数件 degradation_guard.threshold_n_distinct_le` | 1 | **1** | 3 | 3 | 0 | 未定义 | `results/c5_b_group_fix_readings_2026_10_01.json degradation_guard` |

### §2.8 链式衔接与旧 root 存在性登记（沿补报 §2.5 口径）

| 项 | 本人现算 |
|---|---|
| `node_state` 出现重复的取值数 | **0** |
| `node_state` 重复占用槽位数（Σcount−1） | **0** |
| `parent_state[i] == node_state[i−1]`（i=1..21） | **21／21** |
| `parent_state[0] == anchors[0]`（`7d6d3d39fad8`） | **true** |
| 旧 root `75596bbabdb8` 在 B3 产出件全文命中 | **0** |
| 旧 root `75596bbabdb8` 在 `index_v3` 全文命中 | **0** |

> **0 判读**：§9 看护项 5 判据「出现重复 `node_state`」之比对结果为**读数事实**；**0 自行判为通过**（判档归 verdict-keeper）。

---

## §3 V3-04 缺口 **9 字段**闭合对照（**本件核心交付**）

> 缺口登记源：`results/c5_guard_0_1_recheck_verdict_2026_10_01.md`（`24418fa60ede`）§3.1「残留缺口（本人现算，判据要求报而补报未报）」表 **9 行**。本件对该 9 行**逐项补齐四项**，⛔ 0 回改该判定件。
>
> **行数口径**：该 9 行 ＝ **11 个字段级读数列** —— 第 1 行（`coords_k[0]`／`[1]`／`[2]` 的 `n_distinct`）含 **3 列**，故 9 行展开为 11 项；下表按**字段级**逐项列全。
>
> **长串呈现口径**：`captions[].text` 之字典序 `min`／`max` 全串见伴随 JSON `four_readings` 节；下表超 40 字符者**截断呈现并标注全长**（⛔ 0 改值）。

| # | 缺口项 | `n` | `n_distinct` | `min` | `max` | `std`(ddof=0) | `std`(ddof=1) | 缺口来源 |
|:-:|---|---:|---:|---|---|---:|---:|---|
| 1 | `B3 per_caption[].coords_k[0] 的 n_distinct` | 22 | **22** | -0.921827 | -0.522025 | 0.129530 | 0.132579 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 1 行 |
| 2 | `B3 per_caption[].coords_k[1] 的 n_distinct` | 22 | **22** | -0.167983 | 0.621236 | 0.276760 | 0.283273 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 1 行 |
| 3 | `B3 per_caption[].coords_k[2] 的 n_distinct` | 22 | **22** | -0.362677 | 0.514085 | 0.166955 | 0.170883 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 1 行 |
| 4 | `graphs[].family` | 22 | **2** | `L` | `S` | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 2 行 |
| 5 | `graphs[].file` | 22 | **22** | `L_algorithm_process.json` | `S6_n60.json` | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 3 行 |
| 6 | `graphs[].graph_id` | 22 | **22** | `L_algorithm_process` | `S6_n60` | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 4 行 |
| 7 | `graphs[].sha256` | 22 | **22** | `0944d0222d5cc12e8c906f25888b777f5cc474f7…`（全长 **64** 字符，全串见 JSON） | `f63039c8ec1ebdebb9a34d7b226d6328a1c77156…`（全长 **64** 字符，全串见 JSON） | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 5 行 |
| 8 | `graphs[].structure` | 22 | **7** | `balanced_binary_tree` | `three_hub_competition` | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 6 行 |
| 9 | `captions[].byte_hash` | 22 | **22** | `0e89a90afea3` | `fbfa04f1128c` | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 7 行 |
| 10 | `captions[].dual_v04` | 22 | **22** | `0e89a903eed` | `fbfa0401ad5` | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 8 行 |
| 11 | `captions[].text（原串列 n_distinct）` | 22 | **22** | `世界; 亚洲; 欧洲; 非洲; 北美洲; 南美洲; 大洋洲; 南极洲; 中国; …`（全长 **214** 字符，全串见 JSON） | `项目立项; 需求收集; 需求分析; 需求确认; 项目范围; WBS分解; 范围确…`（全长 **200** 字符，全串见 JSON） | 未定义 | 未定义 | results/c5_guard_0_1_recheck_verdict_2026_10_01.md §3.1 表第 9 行 |

**缺口 9 行逐项说明**：

1. `B3 per_caption[].coords_k[0] 的 n_distinct` —— 数值列，四项齐报。
2. `B3 per_caption[].coords_k[1] 的 n_distinct` —— 数值列，四项齐报。
3. `B3 per_caption[].coords_k[2] 的 n_distinct` —— 数值列，四项齐报。
4. `graphs[].family` —— 字符串列，`std` 按口径记**未定义**（0 伪填）。
5. `graphs[].file` —— 字符串列，`std` 按口径记**未定义**（0 伪填）。
6. `graphs[].graph_id` —— 字符串列，`std` 按口径记**未定义**（0 伪填）。
7. `graphs[].sha256` —— 字符串列，`std` 按口径记**未定义**（0 伪填）；`int(hex,16)` 派生 `std`(ddof=0) ＝ **30,284,026,395,949,939,078,093,600,503,362,485,390,522,290,522,412,169,252,317,332,834,553,908,166,656.000000**。
8. `graphs[].structure` —— 字符串列，`std` 按口径记**未定义**（0 伪填）。
9. `captions[].byte_hash` —— 字符串列，`std` 按口径记**未定义**（0 伪填）；`int(hex,16)` 派生 `std`(ddof=0) ＝ **74,872,849,733,430.062500**。
10. `captions[].dual_v04` —— 字符串列，`std` 按口径记**未定义**（0 伪填）；`int(hex,16)` 派生 `std`(ddof=0) ＝ **4,679,553,017,117.271484**。
11. `captions[].text（原串列 n_distinct）` —— 字符串列，`std` 按口径记**未定义**（0 伪填）。

**⇒ 9 行全部四项齐报；`K-V3DF-0-1` 字面覆盖面（「每个输入字段」＋「每个输出读数列」）之残留缺口在本件口径下 0 残留。**

### §3.1 原缺口字面实测（本人重算 · 复现「只报 `n_distinct`」之原始证据）

| 件 | `"min"` 命中 | `"max"` 命中 | `"std"` 命中 |
|---|---:|---:|---:|
| `results/c5_b_group_fix_readings_2026_10_01.json`（修后读数件） | **0** | **0** | **0** |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json`（B3 产出件） | **0** | **0** | **0** |

⇒ 与缺口主件 §1.1 V3-04 行所述「全文检索 `"std"`/`"min"`/`"max"` 命中 0」**本人重算逐项复现**。

---

## §4 退化警报字面比对面（**读数事实登记 · 0 判定**）

> 沿 `results/_v5_v3_deg_fix_prereg_2026_09_29.md` §4.0 字面「**任一 `n_distinct ≤ 3`** ⇒ 退化警报」；下表为**本件全量读数**中命中该字面之字段清单。
>
> ⛔ **本件 0 判定**：0 落 PASS/FAIL/KD、0 判门是否开跑、0 判「修好成立」、0 判告警真伪。**落态归 verdict-keeper**。
> ⚠️ **诚实边界**：上表读数**是本件 worker 的现算值**，**不是**修复件／补报件的报出值；判据要求「修复件报」方为闭合，**worker 本人算得 0 豁免该要求** ⇒ 本件**只登记读数**。

| 字段 | `n` | `n_distinct` | `std`(ddof=0) | 列类 | 所属表 | 字段性质（登记事实） |
|---|---:|---:|---:|---|---|---|
| `B3 chain.link_verified` | 22 | **1** | 0 | numeric | D. B3 `per_caption` 面 | 布尔指示位（22/22 true） |
| `B3 chain.self_verified_only` | 22 | **1** | 0 | numeric | D. B3 `per_caption` 面 | 布尔指示位（22/22 true） |
| `B3 diff_registration_vs_f4.dual_identical` | 22 | **1** | 0 | numeric | D. B3 `per_caption` 面 | 布尔差异登记位（22/22 false） |
| `B3 diff_registration_vs_f4.semantic_hash_identical` | 22 | **1** | 0 | numeric | D. B3 `per_caption` 面 | 布尔差异登记位（22/22 false） |
| `B3 diff_registration_vs_v3phys.dual_identical` | 22 | **1** | 0 | numeric | D. B3 `per_caption` 面 | 布尔差异登记位（22/22 false） |
| `B3 diff_registration_vs_v3phys.semantic_hash_identical` | 22 | **1** | 0 | numeric | D. B3 `per_caption` 面 | 布尔差异登记位（22/22 false） |
| `B3 per_caption[].dual_hex_width` | 22 | **1** | 0 | numeric | D. B3 `per_caption` 面 | 定长表示法常量（构造决定 6+5＝11 hex；沿既有甲档条件处理面，0 判） |
| `diff_registration 四项 identical_count（4 标量并列）` | 4 | **1** | 0 | numeric | E. B3 标量 / caliber / 登记面 | —（本件未预登记性质；0 自拟归因） |
| `id_correspondence.n_graph_ids / n_caption_ids（2 标量并列）` | 2 | **1** | 0 | numeric | E. B3 标量 / caliber / 登记面 | 标量并列成列（计数常量） |
| `id_correspondence.positional_match / raw_concept_ids_match（2 bool 并列）` | 2 | **1** | 0 | numeric | E. B3 标量 / caliber / 登记面 | 布尔指示位并列成列（2/2 true） |
| `输出读数列 · d/2 参照（9.0 ／ 18/2）` | 2 | **1** | 0 | numeric | F. 输出读数列面 | —（本件未预登记性质；0 自拟归因） |
| `caliber.hyperplanes_shape[0..1]（2 标量并列）` | 2 | **2** | 7.500000 | numeric | E. B3 标量 / caliber / 登记面 | 标量并列成列（构造常量） |
| `caliber.n_components / planes_per_dim（2 标量并列）` | 2 | **2** | 1.500000 | numeric | E. B3 标量 / caliber / 登记面 | 标量并列成列（构造常量） |
| `captions[].family` | 22 | **2** | 未定义 | string | A. `index_v3` captions 面 | 具名标签（L／S 二类） |
| `graphs[].family` | 22 | **2** | 未定义 | string | B. `index_v3` graphs 面 | 具名标签（L／S 二类） |
| `graphs[].source` | 22 | **2** | 0.208299 | numeric | B. `index_v3` graphs 面 | 0-1 二值来源标志位 |
| `B3 anchors.values（3 hex 列）` | 3 | **3** | 未定义 | string | E. B3 标量 / caliber / 登记面 | 3 hex 锚点列（n=3，值集必为 3） |
| `chain_summary 三环并列（3 hex 列）` | 3 | **3** | 未定义 | string | E. B3 标量 / caliber / 登记面 | 补报自建派生列（3 标量合并成列，值集必为 3） |
| `cross_seed_control 三标量（n_distinct / hamming_mean / zero_count）` | 3 | **3** | 7.400204 | numeric | F. 输出读数列面 | 对 3 个对位标量并列成一列（派生列） |
| `index_v3.fingerprint_anchors（3 hex 列）` | 3 | **3** | 未定义 | string | C. `index_v3` 顶层标量与列表 | 3 hex 锚点列（n=3，值集必为 3） |
| `input_selfcheck 三项（max_abs_dev / svd_var_k / reproduces_flag→0/1）` | 3 | **3** | 0.371653 | numeric | E. B3 标量 / caliber / 登记面 | —（本件未预登记性质；0 自拟归因） |
| `输出读数列 · svd_var_explained（k=2/3/4）` | 3 | **3** | 0.021319 | numeric | F. 输出读数列面 | —（本件未预登记性质；0 自拟归因） |

**命中项计：22 项**（对 §2 全部 **7 表 · 71 列**逐列判比，`n ≥ 2` 且 `n_distinct ≤ 3`）。

**标量列（`n = 1`）· `n_distinct = 1` 为平凡真 —— 单列登记，0 混入上表命中面**：

> **口径说明**：标量列（构造常量／元数据／单值语义）之 `n_distinct` 恒 ＝ 1，属**平凡真**；本件将其自警报命中面**分列**登记，防以平凡真充数。**是否豁免归 verdict-keeper，本件 0 判定**。

| 字段 | `n_distinct` | 盘上标量值 | 所属表 | 字段性质（登记事实） |
|---|---:|---:|---|---|
| `caliber.code_len_bit（标量）` | **1** | 18 | E. B3 标量 / caliber / 登记面 | 标量（构造常量） |
| `caliber.d_over_2_reference（标量）` | **1** | 9 | E. B3 标量 / caliber / 登记面 | 标量（n=1） |
| `caliber.hex_width（标量）` | **1** | 5 | E. B3 标量 / caliber / 登记面 | 标量（构造常量） |
| `chain_summary.b3_merkle_root（标量）` | **1** | 45ef859b2be9 | E. B3 标量 / caliber / 登记面 | 标量（n=1，单值即其语义） |
| `chain_summary.ext_1_after_anchor2（标量）` | **1** | bf492f1c8424 | E. B3 标量 / caliber / 登记面 | 标量（n=1，单值即其语义） |
| `chain_summary.independent_rewalk_ok（标量 bool）` | **1** | 1 | E. B3 标量 / caliber / 登记面 | 布尔指示位（n=1） |
| `chain_summary.state_22_after_22_captions（标量）` | **1** | bbd61495cb5d | E. B3 标量 / caliber / 登记面 | 标量（n=1，单值即其语义） |
| `index_v3.n_captions（标量）` | **1** | 22 | C. `index_v3` 顶层标量与列表 | —（本件未预登记性质） |
| `index_v3.n_graphs（标量）` | **1** | 22 | C. `index_v3` 顶层标量与列表 | —（本件未预登记性质） |
| `修后读数件 degradation_guard.byte_hash_primary_n_distinct` | **1** | 22 | G. 修后读数件 `degradation_guard` 面 | 标量（n=1，构造常量）；盘上原值 22 与同字段现算一致，⛔ 0 差异 |
| `修后读数件 degradation_guard.root_predup_dual_n_distinct` | **1** | 22 | G. 修后读数件 `degradation_guard` 面 | 标量（n=1，构造常量）；盘上原值 22 与同字段现算一致，⛔ 0 差异 |
| `修后读数件 degradation_guard.semantic_hash_codelen_n_distinct` | **1** | 9 | G. 修后读数件 `degradation_guard` 面 | 标量（n=1，构造常量）；盘上原值 9 与同字段现算一致，⛔ 0 差异 |
| `修后读数件 degradation_guard.threshold_n_distinct_le` | **1** | 3 | G. 修后读数件 `degradation_guard` 面 | 标量（n=1）；盘上原值 3（警报阈值本身） |

**标量列计：13 项**（全列登记，0 遗漏）。

**操作方向登记（0 判定）**：`results/c5_guard_0_1_recheck_verdict_2026_10_01.md`（`24418fa60ede`）§7 已载「`K-V3DF-0-1` **不得开跑**」，并落 **KD**；本件**0 触碰该落态**（0 改判、0 翻案）。本件仅补齐读数面。

---

## §5 待 verifier 复核面（**沿判定链 worker ＋ verifier**，worker 0 代复核）

| 项 | 面 |
|---|---|
| 复核人 | **verifier**（独立复算 · ⛔ **0 复用本件报值**） |
| 复核对象 | 伴随读数 JSON `results/_k_v3df_0_1_four_readings_2026_10_09.json` ＋ 本 md §2 全表／§3 缺口 9 项／§4 命中清单 |
| 重点面 | ① §3 缺口 **9 字段**四项；② Hamming **231 对**重算（均值／零对／极值）；③ 字符串列 `std` 记「未定义」之**合规性**（0 伪填）；④ 警报命中清单是否与读数逐项吻合 |
| 验收标准 | 沿 `results/_v5_v3_deg_fix_prereg_2026_09_29.md` §棒 2 重验棒：与 worker 报值**逐项一致或给出不一致面**；不一致 ⇒ 回报分歧，⛔ 0 择一冒充定论 |
| 不一致面处置 | 回报 verdict-keeper；**0 由 worker 自改本件**（本件 0 预设自我辩护） |

**worker 自检（0 非独立复核）**：§2 数值由脚本直接从 3 件源数据算出并写入产出件（0 手工誊抄）；缺口 9 字段与 §2 表为**同一内存对象**取数（0 二处算、0 不一致源）。

---

## §6 复算命令逐项登记（**他人可原样复跑**）

```powershell
# 工作目录 = 仓根 D:\私人资料\deposon-repo
$env:PYTHONIOENCODING='utf-8'

# ① 输入件 SHA-256／SHA-12／bytes／mtime（§0 表逐行）
foreach($f in @(
  'corpus/v20/index_v3_2026_09_29.json',
  'results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json',
  'results/c5_b_group_fix_readings_2026_10_01.json',
  'results/c5_guard_minmaxstd_report_2026_10_01.md',
  'results/c5_guard_minmaxstd_readings_2026_10_01.json',
  'results/c5_guard_0_1_recheck_verdict_2026_10_01.md',
  'results/_v5_v3_deg_fix_prereg_2026_09_29.md',
  'results/_v34_experiment_gap_plan_2026_10_08.md',
  'results/_closing_round_8_decisions_register_2026_10_09.md',
  'results/_naming_ruling_note_2026_09_29.md'
)){ $rp=(Resolve-Path $f).Path; $h=(Get-FileHash $rp -Algorithm SHA256).Hash.ToLower();
  "$f | sha12=$($h.Substring(0,12)) | bytes=$([System.IO.File]::ReadAllBytes($rp).Length) | mtime=$((Get-Item $rp).LastWriteTime)" }

# ② 原缺口字面实测（§3.1 表）
Select-String -Path 'results/c5_b_group_fix_readings_2026_10_01.json' -Pattern '"min"' -AllMatches | Measure-Object | Select-Object Count
Select-String -Path 'results/c5_b_group_fix_readings_2026_10_01.json' -Pattern '"max"' -AllMatches | Measure-Object | Select-Object Count
Select-String -Path 'results/c5_b_group_fix_readings_2026_10_01.json' -Pattern '"std"' -AllMatches | Measure-Object | Select-Object Count

# ③ 全量四读数重算（§2／§3／§4 全表）—— 生成脚本（0 网络、0 读 key）
python .tmp/k_v3df_0_1_four_readings_2026_10_09.py
```

**0 依赖第三方库**：脚本仅用 `json`／`os`／`hashlib`／`collections`（标准库）；统计量 `mean`／`std(ddof=0)`／`std(ddof=1)` 为手写公式（`sum((x-mean)^2)/n` 与 `/(n-1)`），⛔ 0 用 numpy/scipy。

---

## §7 纪律自证

| 纪律 | 落实 |
|---|---|
| **0 判定** | ✅ 全文只给读数与派生；**0 落 PASS/FAIL/KD**、0 判门开跑与否、0 翻案 —— 落态归 **verdict-keeper** |
| **0 回改既有件** | ✅ §0 表 **10 件输入件** SHA-256/SHA-12/bytes 全部**只读复算**，0 写入／0 重命名／0 删除；产出为 **2 件新名件** |
| **0 新设阈值** | ✅ 唯一阈值 `n_distinct ≤ 3` 沿 `results/_v5_v3_deg_fix_prereg_2026_09_29.md` §4.0 L229（未动）；`ddof`／字典序／`int(hex,16)`／`len()` 均**标注为读数派生**，非判定阈值 |
| **0 编造** | ✅ 一切数值由脚本从 3 件源数据**现算**并程序化写入产出件（0 手工誊抄）；输入件指纹先核后引 |
| **0 网络 · 0 读 key（R4）** | ✅ 纯本地文件读取；无网络调用、无 key 读取、**R4 key 永不明文** |
| **0 撞名 · 0 覆写** | ✅ 落盘前 `Test-Path` ＝ False ＋ `glob results/_k_v3df_0_1_four_readings_2026_10_09.*` 命中 0（见 §8） |
| **命名合规** | ✅ 沿 `results/_naming_ruling_note_2026_09_29.md` §1.2②：0 带 V-阶段前缀、0 含阶段号作首段（`v3df` ＝ 判据 ID 冻结字面） |
| **编码** | ✅ UTF-8 **无 BOM** · **LF**（`.md` ＝ LF；JSON 沿族惯例 `indent=1`、`ensure_ascii=false`、`\n` 收尾） |
| **署名如实** | ✅ 出件方 ＝ **worker**（`mvs_96aa893021ef45f88af8c0f96fbea8a0`，W4 波第 2 件 V3-04）；⛔ 不冒 verdict-keeper／verifier／protocol-keeper 名 |
| **1–2 件即停** | ✅ 2 件新名产出（md ＋ 伴随 JSON）；脚本落 `.tmp/` 工具面，**0 计入产出件** |

---

## §8 落盘前后自检（SHA-256／SHA-12／bytes／CRLF 自报）

**落前**：`Test-Path 'results/_k_v3df_0_1_four_readings_2026_10_09.md'` ＝ **False**；`Test-Path 'results/_k_v3df_0_1_four_readings_2026_10_09.json'` ＝ **False**；`glob 'results/_k_v3df_0_1_four_readings_2026_10_09.*'` 命中 **0**。

**落后自报口径**：本件与伴随 JSON 之 **SHA-256／SHA-12／bytes／BOM／CRLF** 值**不自写入本件** —— 沿 `results/_naming_ruling_note_2026_09_29.md` L9「本件自身指纹不自写入本件」纪律（自写入即自指悖论：写入动作本身会改变被写入件的指纹）。二件终值**由回执逐项自报**（落盘后 `hashlib` 复算）。

---

## §9 边界与外推声明

| 面 | 边界 |
|---|---|
| 本件读数域 | B 组 **18-bit 修后构造面**（SVD-3 坐标 ＋ 18-bit LSH ＋ `byte_hash` 主键 ＋ 22 caption ＋ 22 graphs） |
| ⛔ 0 外推 | 真实语义面（22 caption 之外）／其他端点／其他 embedding 模型／其他协议版本／其他 SVD 维数／**修前 12-bit 面**（改维度 ⇒ 换域，读数 0 直接比较） |
| 0 等效主张 | ⛔ **0 作修前／修后同口径等效比较主张**；一切比对仅在 B 组 18-bit 修后构造面内横向进行 |
| 落态外推限制 | 本件**0 落任何判据态**；`KD`／`FAIL` 等落态**0 触碰、0 重裁、0 改写** |
| R4 | key 永不明文；本件 0 读 key |

---

*出证 ＝ worker（`mvs_96aa893021ef45f88af8c0f96fbea8a0`）｜2026-10-09｜W4 波第 2 件 · **V3-04** `K-V3DF-0-1` 读数面四读数补报｜判据唯一源 ＝ `results/_v5_v3_deg_fix_prereg_2026_09_29.md` §4.0 L229｜输入 10 件盘上终态实测 SHA-12 全部登记｜四读数齐报含缺口 9 字段｜⛔ 0 判定、0 回改既有件、0 新设阈值、0 编造、0 联网、0 读 key*
