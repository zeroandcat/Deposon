# C5 · B 组修复链 · **看护面 `min`／`max`／`std` 补报件** · worker · 2026-10-01

> **性质**：沿 C5 判定件 `results/c5_b_group_verdict_2026_10_01.md`（`3fbf6b38a383`）§1 行 `0-1`（`K-V3DF-0-1` 落 **FAIL**，根因＝「只报 `n_distinct`、0 报 `min`／`max`／`std`」）之**归 worker 补报**部分，**现算** B3 产出面 22 节各字段之 `n_distinct`／`min`／`max`／`std`。
> **本棒身份**：**worker**（`mvs_03e34a7a4bce4bdfb6cd339c725b3813`）。**0 判定**：不判 `K-V3DF-0-1` 是否转态、不判门是否开跑，**归 verdict-keeper 复算**；**0 改任何既有件**；**0 新设阈值**（全部沿 §9／预登记字面）；**0 编造**（一切数字本人盘上现算，标复算方式）；**R4 · 0 读 key · 0 联网**（纯本地 python3 读取＋统计）。
> **纪律依据**：判据字面取自 `results/c5_b_group_root_candidate_2026_10_01.md`（`2fd8946cfe80`）**§9 防退化看护**五项表（L263–269）＋ 预登记件 `results/_v5_v3_deg_fix_prereg_2026_09_29.md`（`98286cc1aec7`）**§4.0 `K-V3DF-0-1`**（L229）「修复件对**每个输入字段**与**每个输出读数列**报 `n_distinct`／`min`／`max`／`std`」。
> **回执件（0 撞名 · 0 覆写 · 新名）**：`results/c5_guard_minmaxstd_report_2026_10_01.md`（本件）＋ `results/c5_guard_minmaxstd_readings_2026_10_01.json`（`7ff301514f66`，伴随读数 JSON，沿族惯例 UTF-8／缩进 1）＋ 生成脚本 `.tmp/c5_guard_minmaxstd_2026_10_01.py`（0 落仓内证据面，仅工具）。

---

## §0 输入件 · 本人盘上实测 SHA-12（**0 复用自报值 · 非引派工单字面**）

| # | 件 | 派工单给定 | **本人复算 SHA-12** | 一致 |
|:-:|---|---|---:|:-:|
| 1 | `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | **`3ba2449cf986`** | ✅ |
| 2 | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | **`33ad1c01f745`** | ✅ |
| 3 | `results/c5_b_group_fix_readings_2026_10_01.json` | `2a7749da7c4d` | **`2a7749da7c4d`** | ✅ |
| 4 | `results/c5_b_group_root_candidate_2026_10_01.md`（§9 判据源） | `2fd8946cfe80` | **`2fd8946cfe80`** | ✅ |
| 5 | `results/c5_b_group_verdict_2026_10_01.md`（补报范围依据） | `3fbf6b38a383` | **`3fbf6b38a383`** | ✅ |

**复算方式**：`hashlib.sha256(全文字节).hexdigest()[:12]`，小写（沿预登记件 L9 口径；禁内建 `hash()`）。**5/5 与派工单字面一致**（按「登记值可能落后于盘上终态」纪律，核验期间先比对末次写 mtime 早于本棒开工，0 发现快照后修正；**一律以终态复算为准**）。

**两产出件 ↔ 修后读数件 逐字段同一性交叉核对（本人现算）**：

| 交叉项 | 结果 |
|---|:-:|
| `index_v3.captions` 22 `caption_id` 与 B3 `per_caption` 位置对应 | ✅ 22/22 同序 |
| `byte_hash` 22 条两件同值 | ✅ |
| `semantic_hash` 22 条两件同值 | ✅ |
| `dual` ↔ `index_v3` `dual_v04` 同值 | ✅ |
| 修后读数件 `per_caption[].dual` ↔ B3 `dual` 同值 | ✅ |
| 修后读数件 `per_caption[].byte_hash` ↔ B3 同值 | ✅ |

⇒ **三件读数面互不矛盾**，补报读数可同源并列（0 合并派生 JSON 0 触既有件）。

---

## §1 复算口径声明（**0 自设阈值**）

| 项 | 本件口径 |
|---|---|
| 哈希 | `sha256(全文字节).hexdigest()[:12]` 小写 |
| **`std` 总体口径** | **`ddof = 0`（总体标准差）为主报口径** —— 22 节为全体总体，非抽样 |
| `std` 样本口径 | `ddof = 1` 并列给出；**0 声称与盘上其他件口径一致**（盘上他件未标 `ddof`） |
| 字符串／hex 字段 | `min`／`max` ＝ **字典序**（lexicographic）；`std` 对非数值列**未定义** ⇒ 如实记 `null` ＋ `std_note`，**0 伪填 0.0**；另附 `hex→int` 数值代理读数（`int(hex,16)`，**标注为派生读数、0 设阈值**） |
| 标量字段（root 三环） | `n = 1` ⇒ `std` 未定义（`ddof=0` 下为 `0.0`），如实标注 |
| 环境 | 纯本地 `python3`（`statistics` 模块）、0 网络、0 key 读取、0 既有件写入 |

---

## §2 **逐项补报表 · 字段｜`n_distinct`｜`min`｜`max`｜`std`｜现值来源**

### §2.1 看护项 **1** ｜ `dual` / `semantic_hash` 字段（§9 #1 判据 `n_distinct ≤ 3`）

| 字段 | `n_distinct` | `min` | `max` | `std`（ddof=0） | `std`（ddof=1） | 现值来源 |
|---|---:|---|---|---:|---:|---|
| `dual`（22 条） | **22** | `0e89a903eed`（字典序） | `fbfa0401ad5`（字典序） | 未定义（字符串列） | 未定义 | B3 件 `per_caption[].dual`（`33ad1c01f745`）现算 |
| `dual` hex→int 代理 | 22 | 999,025,557,229 | 17,315,701,725,909 | 4,679,553,017,117.271 | 4,789,675,213,565.161 | 同上，`int(hex,16)`（11 hex ＝ 42 bit）派生读数 |
| `semantic_hash`（22 条） | **9** | `006d4` | `03eef` | 未定义（字符串列） | 未定义 | B3 件 `per_caption[].semantic_hash` 现算 |
| `semantic_hash` hex→int 代理 | 9 | 1,748 | 16,111 | **5,618.693197** | 5,750.915833 | 同上（5 hex ＝ 18 bit LSH 码） |
| `semantic_hash` 18-bit popcount | 9 | 6 | 12 | **1.922571** | 1.967815 | 同上，`bin(x).count("1")` 派生读数 |

**现值校验**：本人现算 `semantic_hash` 分布 ＝ `{006d4:1, 006d8:2, 008d5:1, 01ad5:1, 01ecd:3, 01edd:1, 01eed:2, 03eed:10, 03eef:1}`，`n_distinct = 9` ⇒ **与修后读数件 `stored_distribution` 逐项同值**、`stored_n_distinct_codes = 9` 一致；与判定件独立复算行「`dual` 22／`semantic_hash` 9」一致。最大簇 `03eed` 占 **10/22**。
**读数面备注**：`dual` 宽度 22/22 恒 11 hex；`semantic_hash` 宽度 22/22 恒 5 hex ⇒ 宽度列 `std = 0.0`（见 §2.3）。

### §2.2 看护项 **2** ｜ 新 root 字段（本件新增，§9 #2 判据 ＝ 新 `b3_merkle_root` **等于** `75596bbabdb8`）

| 字段 | `n_distinct` | `min` | `max` | `std` | 现值来源 |
|---|---:|---|---|---|---|
| `b3_merkle_root`（标量） | 1（`n = 1`） | `45ef859b2be9` | `45ef859b2be9` | **未定义**（`n = 1`；`ddof=0` 下为 0.0） | B3 件 `chain_summary.b3_merkle_root` 现读 |
| `ext_1`（标量） | 1（`n = 1`） | `bf492f1c8424` | `bf492f1c8424` | **未定义**（同上） | `chain_summary.ext_1_after_anchor2` |
| `state_22`（标量） | 1（`n = 1`） | `bbd61495cb5d` | `bbd61495cb5d` | **未定义**（同上） | `chain_summary.state_22_after_22_captions` |
| root 三环作一列（`n = 3`） | **3** | `45ef859b2be9` | `bf492f1c8424` | 未定义（字符串列）／代理 62,022,957,580,829.47 | 三环合并成列后现算 |
| root 三环 hex→int 代理 | 3 | 76,895,041,039,337 | 210,321,043,915,812 | **62,022,957,580,829.470**（ddof=0）／75,962,299,205,658.970（ddof=1） | 派生读数 |

**现值来源与一致性**：三环值与判定件独立复算行（`bbd61495cb5d`／`bf492f1c8424`／`45ef859b2be9`）**逐项同值**。
**旧 root 字面存在性实测**：`75596bbabdb8` 在 B3 产出件全文命中 **0**、在 `index_v3` 全文命中 **0**；新 root ≠ 旧 root（本件记为**读数事实**：`new_root_equals_old_root_bool = false`；**0 判档、0 判「修好成立」**）。

### §2.3 看护项 **3** ｜ 码长／`dual_hex_width` 字段（§9 #3 判据 `n_distinct ≤ 3`）

| 字段 | `n_distinct` | `min` | `max` | `std`（ddof=0） | `std`（ddof=1） | 现值来源 |
|---|---:|---:|---:|---:|---:|---|
| **`dual_hex_width`**（22 条） | **1** | **11** | **11** | **0.0** | 0.0 | B3 件 `per_caption[].dual_hex_width` 现算 |
| `semantic_hash` hex 宽度 | 1 | 5 | 5 | **0.0** | 0.0 | `len(semantic_hash)` |
| `byte_hash` hex 宽度 | 1 | 12 | 12 | **0.0** | 0.0 | `len(byte_hash)` |
| `dual` hex 宽度 | 1 | 11 | 11 | **0.0** | 0.0 | `len(dual)` |
| `semantic_hash` 18-bit popcount | 9 | 6 | 12 | **1.922571** | 1.967815 | 派生读数 |
| `byte_hash` popcount | 22 | 18 | 32 | **3.377429** | 3.456909 | 派生读数 |
| `dual` popcount（11 hex ＝ 42 bit） | 22 | 16 | 27 | **2.975451** | 3.045471 | 派生读数 |
| `link_input` 字符长度 | 22 | 27 | 47 | **6.939080** | 7.102374 | `len(chain.link_input)` |
| `caliber.code_len_bit`（标量） | 1 | 18 | 18 | 未定义（`n=1`） | 未定义 | `caliber.code_len_bit` |
| `caliber.hex_width`（标量） | 1 | 5 | 5 | 未定义（`n=1`） | 未定义 | `caliber.hex_width` |
| `caliber.d_over_2_reference`（标量） | 1 | 9.0 | 9.0 | 未定义（`n=1`） | 未定义 | 沿 `K-V3DF-5-2` 派生参照，**0 新设阈值** |

**⚠️ 读数事实登记（0 判定）**：宽度类字段（`dual_hex_width`／三处 hex 宽度）**恒定** ⇒ `n_distinct = 1`、`std = 0.0`。此为**结构性恒定**（构造定义即固定宽度），与「值坍缩」不同类；判定件 §1 行 `0-1` 已将其与「只报 `n_distinct`」并列为读数面缺失根因。**本件只登记该读数，不判其是否触发 §9 #3 警报**（`n_distinct ≤ 3` 字面比对归 verdict-keeper）。

### §2.4 看护项 **4** ｜ `byte_hash` 主键字段（§9 #4 判据 `n_distinct ≤ 3`；PI 批 5 ⑰ 裁「**不升 `byte_hash` 主键**」）

| 字段 | `n_distinct` | `min` | `max` | `std`（ddof=0） | `std`（ddof=1） | 现值来源 |
|---|---:|---:|---:|---:|---:|---|
| `byte_hash`（22 条，12 hex） | **22** | `0e89a90afea3` | `fbfa04f1128c` | 未定义（字符串列） | 未定义 | B3 件 `per_caption[].byte_hash` 现算 |
| `byte_hash` hex→int 代理 | 22 | 15,984,409,378,467 | 277,051,243,303,564 | **74,872,849,733,430.060** | 76,634,804,910,943.440 | 派生读数（12 hex ＝ SHA-256 前 48 bit 切片） |
| `byte_hash` popcount | 22 | 18 | 32 | **3.377429** | 3.456909 | 派生读数 |
| `byte_hash[:6]`（`dual` 前缀段） | **22** | `0e89a9` | `fbfa04` | 未定义／代理 4,462,769.525542 | 4,567,790.235981 | `byte_hash[:6]` 现算 |
| `byte_hash[6:]`（后 6 hex） | **22** | `0afea3` | `fbf9ba` | 未定义／代理 4,868,931.778694 | 4,983,510.555740 | `byte_hash[6:]` 现算 |
| `caption_id`（主键名） | **22** | `L_algorithm_process` | `S6_n60` | 未定义（字符串列，长度不等） | 未定义 | `per_caption[].caption_id` |
| `caption_id` 字符长度 | 22 | 2 | 22 | 见 §3 附表（未单列 std 统计，全 8 档） | — | `len(caption_id)` |

**现值校验**：`byte_hash` `n_distinct = 22` ⇒ 与修后读数件 `degradation_guard.byte_hash_primary_n_distinct = 22` 一致、判定件复算行一致。
**派生一致性实测**：`byte_hash[:6]` 与 `semantic_hash` 拼接后 22/22 ＝ `dual` 字面（构造 `byte_hash[:6] + semantic_hash` 22/22 成立）；前缀段 22 distinct ＋ `semantic_hash` 9 distinct ⇒ `dual` 22 distinct **可由两因子解释**（数学必然，非实验读数）。

### §2.5 看护项 **5** ｜ 22 节 `node_state`（§9 #5 判据「出现重复 `node_state`」）

| 字段 | `n_distinct` | `min` | `max` | `std`（ddof=0） | `std`（ddof=1） | 现值来源 |
|---|---:|---:|---:|---:|---:|---|
| **`node_state`**（22 条，12 hex） | **22** | `08a30c2cfe79` | `ec04dfa75fd0` | 未定义（字符串列）／代理 **78,944,833,746,749.520** | 80,802,613,423,271.060 | B3 件 `per_caption[].chain.node_state` 现算 |
| 重复值计数（出现重复的取值数） | **0** | — | — | — | — | `Counter` 现算 |
| 重复占用槽位数（Σcount−1） | **0** | — | — | — | — | `Counter` 现算 |
| `parent_state`（22 条） | **22** | `08a30c2cfe79` | `ec04dfa75fd0` | 未定义／代理 77,235,440,410,508.880 | 79,052,993,563,665.550 | `per_caption[].chain.parent_state` |
| `link_input`（22 条） | **22** | `08a30c2cfe79\|S4\|b1d3eb03eed` | `ec04dfa75fd0\|S5\|1cdcbd01ecd` | 未定义（长度不等，7 档） | — | `per_caption[].chain.link_input` |
| `link_verified`（bool→0/1） | 1 | 1 | 1 | **0.0** | 0.0 | 22/22 ＝ `true` |
| `self_verified_only`（bool→0/1） | 1 | 1 | 1 | **0.0** | 0.0 | 22/22 ＝ `true` |
| `diff_registration_vs_f4.semantic_hash_identical`（bool→0/1） | 1 | 0 | 0 | **0.0** | 0.0 | 22/22 ＝ `false` |
| `diff_registration_vs_v3phys.semantic_hash_identical`（bool→0/1） | 1 | 0 | 0 | **0.0** | 0.0 | 22/22 ＝ `false` |

**链式衔接现算（本人逐位核对）**：`parent_state[0] == anchors.values[0]`（`7d6d3d39fad8`）＝ **true**；`parent_state[i] == node_state[i−1]` 对 `i = 1..21` **21/21 全 true** ⇒ **0 断链**。
**判读边界**：§9 #5 判据为「**出现重复** `node_state`」；本件实测**重复 0 条**。**0 自判通过**（§9 归属条款明写「记入差异登记，**0 自行判为通过**」，判档归 verdict-keeper）。

---

## §3 附表 · `K-V3DF-0-1` 字面「**每个输入字段**／**每个输出读数列**」之补报（应报未报面）

> 依据：预登记 §4.0 字面覆盖面 ＝ 每输入字段 ＋ 每输出读数列。判定件指出读数面 0 报 `min`／`max`／`std`；下表为**盘上已有字段**之全量现算（**0 自设阈值、0 自拟判据**），供 verdict-keeper 复算时一次到位。

### §3.1 数值列（`index_v3` 输入面 ＋ B3 坐标面）

| 字段 | `n_distinct` | `min` | `max` | `mean` | `std`（ddof=0） | `std`（ddof=1） |
|---|---:|---:|---:|---:|---:|---:|
| `coords_k[0]` | — | −0.921827 | −0.522025 | −0.818380 | **0.129530** | 0.132579 |
| `coords_k[1]` | — | −0.167983 | 0.621236 | 0.043052 | **0.276760** | 0.283273 |
| `coords_k[2]` | — | −0.362677 | 0.514085 | 0.000256 | **0.166955** | 0.170883 |
| `coords_k` L2 范数 | 22 | 0.808010 | 0.931119 | 0.889764 | **0.034188** | 0.034992 |
| `graphs[].N` | 11 | 20 | 60 | 38.863636 | **11.382984** | 11.650855 |
| `graphs[].n_edges` | 15 | 19 | 88 | 43.863636 | **15.478124** | 15.842365 |
| `graphs[].n_named` | 16 | 7 | 59 | 25.272727 | **13.608760** | 13.929010 |
| `graphs[].n_filler` | 16 | 0 | 47 | 18.590909 | **13.272182** | 13.584512 |
| `graphs[].source` | 2 | 0 | 1 | 0.045455 | **0.208299** | 0.213201 |
| `graphs[].target` | 13 | 1 | 59 | 26.545455 | **17.785917** | 18.204466 |
| `graphs[].seed` | 22 | 200,101 | 1,634,062,263 | 232,589,474.272727 | **434,702,481.462804** | 444,932,174.744391 |
| `captions[].n_labels` | 11 | 20 | 60 | 38.863636 | **11.382984** | 11.650855 |
| `captions[].text` 字符长度 | — | 92 | 304 | 200.409091 | **59.499931** | 60.900120 |

### §3.2 字符串列（`index_v3` 输入面）

| 字段 | `n_distinct` | `min`（字典序） | `max`（字典序） | 宽度档 | `std` |
|---|---:|---|---|---|---|
| `captions[].family` | 2 | `L` | `S` | 1 | 未定义 |
| `captions[].structure` | 7 | `balanced_binary_tree` | `three_hub_competition` | 6 档（12–24） | 未定义 |

### §3.3 输出读数列（修后读数件 `2a7749da7c4d` 之各读数列 · 全部现算汇总）

| 读数列 | `n` | `min` | `max` | `mean` | `std`（ddof=0） | `std`（ddof=1） | 交叉校验 |
|---|---:|---:|---:|---:|---:|---:|---|
| Hamming 配对（全部 231 对，**本人由 22 码重算**） | 231 | **0** | **8** | 3.025974 | **2.630033** | 2.635744 | 盘上均值 3.026／零对 50／总对 231 **逐项吻合** |
| 簇大小分布（9 码） | 9 | 1 | 10 | 2.444444 | **2.753225** | 2.920236 | 与 `stored_distribution` 同源 |
| 类内 Hamming（4 类） | 4 | 1.33 | 5.33 | 3.415000 | **1.418529** | 1.637976 | 与盘上 3.6／5.33／3.4／1.33 同源 |
| 跨 seed 码数（42–48） | 7 | 6 | 9 | 7.142857 | **1.124858** | 1.214986 | 与盘上 9/7/8/6/6/8/6 同源 |
| 跨 seed Hamming 均值 | 7 | 1.632 | 3.766 | 2.665286 | **0.640959** | 0.692315 | 与盘上同源 |
| 跨 seed 零对 | 7 | 50 | 121 | 89.000000 | **26.153394** | 28.248894 | 与盘上同源 |
| 基线 12-bit 码数 | 7 | 3 | 6 | 4.285714 | **0.880631** | 0.951190 | 与盘上 6/4/4/4/4/3/5 同源 |
| `svd_var_explained`（k=2/3/4） | 3 | 0.764974 | 0.817153 | 0.791658 | **0.021319** | 0.026110 | 与盘上同源 |
| `d/2` 参照（9.0 ／ 18/2） | 2 | 9.0 | 9.0 | 9.000000 | **0.0** | 0.0 | 沿 `K-V3DF-5-2` 派生，0 新设阈值 |

**Hamming 全 231 对重算自证**：22 码两两配对＝231 对（`22·21/2`）；`bin(a^b).count("1")` 逐对计算 ⇒ 均值 **3.025974**（盘上 3.026，四舍五入一致）、零对 **50**（盘上 50）、最大对距 **8**、最小 **0**、`std_ddof0 = 2.630033`（**盘上 0 报此值**）。

---

## §4 修后读数件「应报未报」清单（**登记事实，0 判**）

| 项 | 实测 |
|---|---|
| 修后读数件全文 `"min"` 字面命中 | **0** |
| 修后读数件全文 `"max"` 字面命中 | **0** |
| 修后读数件全文 `"std"` 字面命中 | **0** |
| `degradation_guard` 已报字段（8 项） | `threshold_n_distinct_le`／`semantic_hash_codelen_n_distinct`＋`_alarm`／`root_predup_dual_n_distinct`＋`_alarm`／`byte_hash_primary_n_distinct`＋`_alarm`／`any_alarm` |
| 其中**只报 `n_distinct`、无 `min`／`max`／`std`** 者 | `degradation_guard.*` 三组 `n_distinct`；`KV3DF_5_1_four_readings.stored_n_distinct_codes`；`hamming_pairs_total`；`KV3DF_5_3_cross_seed.repaired_per_seed[].n_distinct` |
| 修后读数件 `per_caption[].coords_k`（3×22 浮点）**盘上未报任何 min/max/std** | 本件 §3.1 已补 |
| 判定件独立复算面已列读数 | `semantic_hash` 9／Hamming 231／零对 50／均值 3.026／类内 3.6·5.33·3.4·1.33／`dual` 22／`byte_hash` 22／跨 seed 三列／root 三环／`node_state` 22 distinct 0 重复 |

---

## §5 本件纪律自证

| 纪律 | 落实 |
|---|:-:|
| **0 判定** | ✅ 全文只给读数与派生；**不判** `K-V3DF-0-1` 是否转态、不判 §9 五项是否触发警报、不判「修好成立」——判档与转态归 **verdict-keeper** 复算 |
| **0 改既有件** | ✅ 5 件输入件 SHA-12 复核前后同值（`3ba2449cf986`／`33ad1c01f745`／`2a7749da7c4d`／`2fd8946cfe80`／`3fbf6b38a383`），**0 写入、0 重命名、0 删除** |
| **0 新设阈值** | ✅ 全部判据沿 §9 五项字面 ＋ 预登记 `n_distinct ≤ 3` 字面；`ddof` 口径、hex→int、popcount、L2 范数均**标注为读数派生**，非判定阈值 |
| **0 编造** | ✅ 一切数字本人盘上现算（脚本 `.tmp/c5_guard_minmaxstd_2026_10_01.py`），派工单给定指纹先核后引且 5/5 一致 |
| **R4 · 0 联网 · 0 读 key** | ✅ 纯本地 `json` ＋ `statistics` 读取与统计；无网络调用、无 key 读取 |
| **0 撞名 · 0 覆写** | ✅ 产出 `results/c5_guard_minmaxstd_report_2026_10_01.md` ＋ `results/c5_guard_minmaxstd_readings_2026_10_01.json` 均为新名（落盘前 `glob results/c5_guard_*` 命中 0） |
| **编码** | ✅ UTF-8；`.md` ＝ **LF** 行尾；JSON 沿族惯例（`indent=1`、`ensure_ascii=false`、`\n` 收尾） |
| **署名如实** | ✅ 出件方 ＝ **worker**（`mvs_03e34a7a4bce4bdfb6cd339c725b3813`）；不冒 verdict-keeper／verifier／protocol-keeper 名 |
| **1–2 件即停** | ✅ 2 件新名（md ＋ 伴随 JSON）；脚本落 `.tmp/` 工具面，0 计入产出件 |

---

## §6 移交（**0 代跑 · 0 代判**）

- **归 verdict-keeper**：`K-V3DF-0-1` 之**复算**——本件 §2／§3 全部 `n_distinct`／`min`／`max`／`std` 是否满足「每个输入字段／每个输出读数列」全覆盖，**及门是否转态**（PASS／FAIL／KD）。
- **归 verifier**：`results/c5_guard_minmaxstd_readings_2026_10_01.json` 之**独立复算**（本人已交叉校验：Hamming 231 对均值／零对、root 三环、`byte_hash`／`semantic_hash`／`dual` 逐字段同值、跨 seed 三列、链式衔接 21/21）。
- **归 protocol-keeper（若需）**：`caliber.dual_field_name_note` 自陈之字段命名问题（现名 `dual_24bit` 在 18-bit／42-bit 档名实不符）**本件 0 自拟改名**，沿原记。

**⚠️ 本件不含任何 PASS／FAIL／KD 落态**；`K-V3DF-0-1` 之当前档位 ＝ 判定件 `3fbf6b38a383` 所记 **FAIL**，是否因本补报而转态，**由 verdict-keeper 依本件读数复算后落档**。
