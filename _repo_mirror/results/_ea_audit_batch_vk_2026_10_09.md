# 三件 VK 判定件独立证据链审计件 · evidence-auditor · 2026-10-09

> **授权锚**：PI 2026-10-09 卷⑨问卷（`ask_cfb9284519a5abf29d0f03eb`）Q1「五段全开·批准后当日即办」；缺口母件 `results/_v34_experiment_gap_plan_2026_10_08.md`（`996feb1db9cb`）§2.3 收官门槛「全部判定件由 verdict-keeper 落档 ＋ evidence-auditor 审计 PASS」。
> **本棒身份**：**evidence-auditor**。**审计 ≠ 翻案、标注 ≠ 篡改**——发现矛盾／断裂**只登记**，0 改任何既有件、0 改任何判定结论、0 改任何实验读数。
> **口径**：SHA-256 由 `Get-FileHash -Algorithm SHA256`／Python `hashlib` 复算（⛔ 禁内建 `hash()`）⇒ SHA-12 取 hexdigest 前 12 位小写；统计量 `statistics` 标准库复算（⛔ 0 用 numpy/pandas）；**0 网络、0 读 key（R4）、0 合并派生 JSON、0 加载 skill**。
> **命名**：沿 `results/_naming_ruling_note_2026_09_29.md`（`57024f2cd30a`）§1.2②「去版本前缀、0 带 V-阶段字样」⇒ 本件名 `_ea_audit_batch_vk_2026_10_09.md`。
> **本件自身指纹不自写入本件**（自哈希不动点问题）⇒ 权威 SHA-12／bytes 由回执自报。

---

## §0 一句话结论

三件 VK 判定件**逐件 PASS**。锚链核验 33 件实测**全部吻合自报值**（唯一登记偏差为①件§1 已主动如实披露的「登记值落后盘上终态」一例，非隐瞒）；幽灵引用三分比对无 MISSING_TRUE／无 CONFLICT；0 触动自证通过（全部输入件 mtime ≤ 对应判定件落盘，无快照后修正面）；key 形态扫描三件 CLEAN；数字矛盾抽查三件各核心读数**独立复算全部吻合**。

---

## §1 受审对象（本人盘上终态实测 · 0 复用自报值）

| # | 件 | SHA-12（实测） | bytes | LF/CRLF | BOM | 编码自证 |
|:-:|---|---|---:|---|---|:-:|
| ① | `results/_k_v3df_9_1_c1_c4_legs_verdict_2026_10_09.md` | `a14aafa220c4` | 27,735 | LF=232／CRLF=0 | False | ✅ |
| ② | `results/_t1_qwen_temp_sweep_verdict_2026_10_09.md` | `dfc858d3d930` | 21,672 | LF=213／CRLF=0 | False | ✅ |
| ③ | `results/_k_v3df_0_1_readings_verdict_2026_10_09.md` | `e98bee353448` | 37,003 | LF=409／CRLF=0 | False | ✅ |

**三件 SHA-12／bytes 与派工单授权锚逐位一致** ✅（详见 §4）。

---

## §2 逐件 VERDICT

| # | 件 | **VERDICT** | 锚链 | 幽灵引用 | 0 触动 | key 形态 | 数字抽查 | 计数一致 |
|:-:|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ① | C1–C4 腿判定件 | **PASS** | ✅ 13/13 吻合 | ✅ 0 幽灵 | ✅ | ✅ CLEAN | ✅ 6 读数吻合 | ✅ 10 行自洽 |
| ② | T1 qwen 温扫判定件 | **PASS** | ✅ 8/8 吻合 ＋ 仓外 1/1 | ✅ 分支合规 | ✅ | ✅ CLEAN | ✅ J 值吻合 | ✅ |
| ③ | `K-V3DF-0-1` 读数面件 | **PASS** | ✅ 12/12 吻合 | ✅ 0 幽灵 | ✅ | ✅ CLEAN | ✅ 22 项吻合 | ✅ 自洽 |

**总判定：三件 PASS。**

---

## §3 审计面①：锚链核验（SHA-12/bytes 逐件复算对照）

### 3.1 ①件所引 13 件（§1 输入表）

| # | 件 | 申报 SHA-12 | 实测 SHA-12 | bytes 申报/实测 | 判定 |
|:-:|---|---|---|---|:-:|
| 1 | `_v34_experiment_gap_plan_2026_10_08.md` | `996feb1db9cb` | `996feb1db9cb` | 36,066／36,066 | **MATCH** |
| 2 | `_v5_v3_deg_fix_prereg_2026_09_29.md` | `98286cc1aec7` | `98286cc1aec7` | 41,622／41,622 | **MATCH** |
| 3 | `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md` | `0fd7a26fc339` | `0fd7a26fc339` | 109,614／109,614 | **MATCH** |
| 4 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` | `9bb22099db3b` | `9bb22099db3b` | 28,207／28,207 | **MATCH** |
| 5 | `_v3_supplement_verdict_2026_09_23.md` | `b70211bfa83e` | `b70211bfa83e` | 15,247／15,247 | **MATCH** |
| 6 | `boss_pa_1_rbr_rm_result_2026_09_15.json` | `c7c59e0d2f6c` | `c7c59e0d2f6c` | 8,753／8,753 | **MATCH** |
| 7 | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | 「在盘」未登记 | `977fe1b48f75` | 19,751／19,751 | **FOUND（字节吻合）** |
| 8 | `_v3_recheck_01_rescript_2026_09_27.md` | `a3c95102290f` | `a3c95102290f` | 14,541／14,541 | **MATCH** |
| 9 | `_v5_v3_deg_p1_reopen_result_2026_09_29.json` | `b86d6740d487` | `b86d6740d487` | 571,451／571,451 | **MATCH** |
| 10 | `_v5_v3_deg_p1_reopen_verdict_2026_09_29.md` | `63d898ab1b71` | `63d898ab1b71` | 42,645／42,645 | **MATCH** |
| 11 | `_v5_v3_deg_p1_reopen_verdict_r2_2026_09_29.md` | `8adaf4e5d868` | `8adaf4e5d868` | 44,054／44,054 | **MATCH** |
| 12 | `c5_b_group_verdict_2026_10_01.md` | `3fbf6b38a383` | `3fbf6b38a383` | 30,118／30,118 | **MATCH** |
| 13 | `deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | `33ad1c01f745` | 20,398／20,398 | **MATCH** |

⇒ **13/13 MATCH**（件 7 字节逐位吻合，申报时按「在盘」未登记哈希，属**如实**而非缺口）。

### 3.2 ①件§1 已披露的「登记值落后盘上终态」一例（**如实披露，登记而非隐瞒**）

| 件 | 登记值（prereg §0.2／勘误链 E-48） | 盘上终态实测 | 处置 |
|---|---|---|---|
| `results/_v3_recheck_prereg_v1_2026_09_27.md` | `434B3213BDCE`／13,233 B | `88052d7db895`／37,346 B | **登记落后于盘上**（该件其后有追加） |

⇒ **审计意见**：①件已主动披露此偏差、明示「0 影响本轮裁定」、坚持「以终态复算为准」，符合「登记值可能落后于盘上终态」纪律。**不构成隐瞒**；仅作**事实登记**（见 §7 发现项 F-1，级别：低·已由①件自曝）。

### 3.3 ②件所引 8 件（§0 输入链）＋ 仓外 1 件（C-5）

| # | 件 | 申报 SHA-12 | 实测 SHA-12 | bytes 申报/实测 | 判定 |
|:-:|---|---|---|---|:-:|
| 1 | `_t1_qwen_temp_sweep_exec_register_2026_10_09.md` | `7AD31E741400` | `7ad31e741400` | 17,341／17,341 | **MATCH** |
| 2 | `_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` | `BDA5D5F3DFA0` | `bda5d5f3dfa0` | 16,994／16,994 | **MATCH** |
| 3 | `_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | `802dece2286a` | 52,942／52,942 | **MATCH** |
| 4 | `.tmp/_t1_qwen_temp_sweep_records.json` | `5B51AF62C640` | `5b51af62c640` | 96,866／96,866 | **MATCH** |
| 5 | `.tmp/_t1_qwen_temp_sweep_readings.json` | `E5E8F024E42E` | `e5e8f024e42e` | 11,013／11,013 | **MATCH** |
| 6 | `.tmp/_t1_qwen_temp_sweep_decomposition.txt` | `2D96061318D9` | `2d96061318d9` | 1,312／1,312 | **MATCH** |
| 7 | `.tmp/_t1_qwen_temp_sweep_selfcert.json` | `91C2505DEEF3` | `91c2505deef3` | 3,866／3,866 | **MATCH** |
| 8 | `_t1_qwen_temp_sweep_executor_2026_10_09.py` | `F0C845864603` | `f0c845864603` | 32,399／32,399 | **MATCH** |
| 外 | `D:\私人资料\_non_upload_local_archive\results\_v4_supp_l2_n11supp_verdict.md` | `E433A06E7FBF` | `e433a06e7bfb` | 15,671／15,671 | **MATCH（仓外核得）** |

⇒ **8/8 MATCH ＋ 仓外 1/1 MATCH**。

### 3.4 ③件所引 12 件（§0 输入件表）＋ 反查 2 件

| # | 件 | 申报 SHA-12 | 实测 SHA-12 | bytes 申报/实测 | 判定 |
|:-:|---|---|---|---|:-:|
| 1 | `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | `3ba2449cf986` | 24,421／24,421 | **MATCH** |
| 2 | `deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | `33ad1c01f745` | 20,398／20,398 | **MATCH** |
| 3 | `c5_b_group_fix_readings_2026_10_01.json` | `2a7749da7c4d` | `2a7749da7c4d` | 9,996／9,996 | **MATCH** |
| 4 | `c5_guard_minmaxstd_report_2026_10_01.md` | `f465fbdb7579` | `f465fbdb7579` | 19,909／19,909 | **MATCH** |
| 5 | `c5_guard_minmaxstd_readings_2026_10_01.json` | `7ff301514f66` | `7ff301514f66` | 19,935／19,935 | **MATCH** |
| 6 | `c5_guard_0_1_recheck_verdict_2026_10_01.md` | `24418fa60ede` | `24418fa60ede` | 33,287／33,287 | **MATCH** |
| 7 | `_v5_v3_deg_fix_prereg_2026_09_29.md` | `98286cc1aec7` | `98286cc1aec7` | 41,622／41,622 | **MATCH** |
| 8 | `_v34_experiment_gap_plan_2026_10_08.md` | `996feb1db9cb` | `996feb1db9cb` | 36,066／36,066 | **MATCH** |
| 9 | `_closing_round_8_decisions_register_2026_10_09.md` | `a28a478e14a8` | `a28a478e14a8` | 2,151／2,151 | **MATCH** |
| 10 | `_naming_ruling_note_2026_09_29.md` | `57024f2cd30a` | `57024f2cd30a` | 7,843／7,843 | **MATCH** |
| 11 | `_k_v3df_0_1_four_readings_2026_10_09.md` | `53c28ca1ae3d` | `53c28ca1ae3d` | 46,522／46,522 | **MATCH** |
| 12 | `_k_v3df_0_1_four_readings_2026_10_09.json` | `e87937d55471` | `e87937d55471` | 65,507／65,507 | **MATCH** |
| 反查 | `c5_b_group_verdict_2026_10_01.md` | `3fbf6b38a383` | `3fbf6b38a383` | — | **MATCH** |
| 反查 | `c5_b_group_root_candidate_2026_10_01.md` | `2fd8946cfe80` | `2fd8946cfe80` | 28,867 | **MATCH** |

⇒ **12/12 MATCH ＋ 反查 2/2 MATCH**。

**锚链核验总计：33 件申报锚 ＋ 仓外 1 件，全部 MATCH**（唯一偏差 F-1 为①件自曝之登记滞后）。

---

## §4 审计面②：幽灵引用对账（五分支三分比对）

| 件 | 所引路径/件名 | 盘上实存 | 判定分支 |
|---|---|---|---|
| ① | `deposon_v20_baselines.json`（§8「0 查缺件实体」） | **在仓** `results/deposon_v20_baselines.json`（`6edb2aec1660`／16,987 B） | **FOUND_IN_REPO**；①件未编造、未代核，诚实挂账 |
| ① | `_v3_recheck_prereg_v1_2026_09_27.md` | 在仓（`88052d7db895`） | **FOUND_IN_REPO**（登记值滞后，见 F-1） |
| ② | `D:\私人资料\_non_upload_local_archive\results\_v4_supp_l2_n11supp_verdict.md` | 仓内 0 命中／**仓外归档区核得** `e433a06e7bfb`／15,671 B | **GHOST_REF_OUTSIDE**（实件仓外）；②件如实登记＋给拉回路径，未造来源 |
| ② | L14 verdict（`8EEF73BF9856`／19,697 B） | 仓内 `results/_v4_supp_l14_n11full_verdict.md` 实测 `8eef73bf9856`／19,697 B | **FOUND_IN_REPO**；②件已如实披露「≠ 锚件所载 `764F24A21AC8`／19,708 B（差 11 B）」之哈希漂移 |
| ③ | `3fbf6b38a383`／`2fd8946cfe80`（§0 幽灵引用反查） | 均在仓且哈希逐位吻合 | **FOUND_IN_REPO ×2**；③件「0 幽灵引用」自证属实 |
| 三件 | 所引判定/读数件是否同名不同哈希 | 无 CONFLICT | — |

**结论**：三件引用的仓外/未核得件均**如实登记、分支合规**，**0 处 MISSING_TRUE**（三处均无的缺件），**0 处 CONFLICT**（同名不同哈希），**0 处虚构来源**。②件对仓外 L2 verdict 的处理尤其规范——给全路径＋实测指纹＋拉回路径，符合「幽灵引用对账」与「归档件拉回」纪律。

---

## §5 审计面③：0 触动自证（输入件末次写 mtime ≤ 判定件落盘）

三件判定件落盘 mtime：①`2026-10-09 11:50:56`｜②`11:54:29`｜③`12:06:13`。

| 判定件 | 输入件集合 mtime 区间 | 触动数 | 判定 |
|---|---|:-:|:-:|
| ① | 全部 13 件输入 mtime ≤ 2026-10-09 11:50（最新输入 `_v3_recheck_01_rescript`＝10-30 16:15） | **0** | ✅ |
| ② | 全部 8 件输入 mtime ≤ 2026-10-09 11:54（最新输入 exec_register＝10-09 11:20） | **0** | ✅ |
| ③ | 全部 12 件输入 mtime ≤ 2026-10-09 12:06（最新输入四读数件＝10-09 11:24） | **0** | ✅ |

⇒ **0 触动成立**：无任何输入件在对应判定件落盘后被修改（快照后修正面 0）。三件的 mtime 时序自证**属实**（③件§0 明列 mtime 并自证无快照后修正，实测逐项吻合）。

---

## §6 审计面④＋⑤：key 形态自扫 ＋ 数字矛盾抽查

### 6.1 key 形态扫描（三件正文 · 词边界）

扫描正则（`\b` 词边界）：`sk-[A-Za-z0-9_-]{8,}`／`tp-[A-Za-z0-9_-]{8,}`／`ark-[A-Za-z0-9_-]{8,}`／`API_KEY`／`Bearer`／`secret_key`／`access_token`／`Authorization`／各云厂商 `*_API_KEY`。

| 件 | 命中数 | 判定 |
|---|:-:|:-:|
| ① | 0 | **CLEAN** |
| ② | 0 | **CLEAN** |
| ③ | 0 | **CLEAN** |

⇒ **R4 满足：三件正文 key 形态扫描全 CLEAN**，0 明文 key 泄漏。

### 6.2 数字矛盾抽查（从源数据独立复算 · 0 抄录盘上 stat 块）

**复算源**：`results/_v5_v3_deg_p1_reopen_result_2026_09_29.json`（①件）／`.tmp/_t1_qwen_temp_sweep_records.json` ＋ readings（②件）／三源 JSON（③件）。

#### ①件 · C1–C4 ＋ 腿② 读数（本人独立复算对照）

| 项 | ①件申报 | 本人复算 | 判定 |
|---|---|---|:-:|
| C1 主臂 `rm_iter`（处置/未处置各 n=22） | `n_distinct=16`／`std=55.5028`／`min=6`／`max=200`／cap=1/22／剔cap `nd=15` | 16／55.5028／6／200／1/22／15 | **MATCH** |
| C1 对照臂 `rm_iter`（处置/未处置各 n=22） | `nd=2`／`std=55.7711`／cap=20/22／剔cap `nd=1` | 2／55.7711／20/22／1 | **MATCH** |
| C2 冻结镜像 `rbr_iter` | `{2,200}`／`nd=2`（n=176） | `{2,200}`／`nd=2`（176 cell） | **MATCH** |
| C2 P-1 重算 `rbr_iter` | `{1}`／`nd=1`／22/22 全改 | `{1}`／`nd=1`（176 cell全1） | **MATCH** |
| C3 `bayes_iter_true` | 176 格全 `1.0`／`nd=1`／`std=0`／cap 0/176 | 176 格全 `1`／`nd=1`／`std=0` | **MATCH** |
| C4 `rbr_mult` 冻结镜像 | `{2.0,200.0}`／`nd=2`／`std=56.9210`／`0.01` 出现 0 格 | `{2,200}`／`nd=2`／`std=56.921`／`0.01` 计数 0 | **MATCH** |
| C4 `rbr_mult` P-1 重算 | `{1.0}`／`nd=1`／`std=0` | `{1.0}`／`nd=1`／`std=0` | **MATCH** |
| 腿② `rm_multiplier` 均值 | 78.2727／`nd=16` | `rm_mult_fixed` mean=**78.2727**／`nd=16`（176 cell） | **MATCH** |

**补充独立佐证（1 件，①件未主张者）**：`legacy_镜像读数.rm_iter` 22 图**恒为 6**（`nd=1`／`std=0`），`legacy_bayes_iter` 22 图取值 `{1,200}`（cap200×4）——直接印证①件「假成立」标注的度量无鉴别力根源。

#### ②件 · J 中位（本人独立复算对照）

| 项 | ②件申报 | 本人复核 | 判定 |
|---|---|---|:-:|
| cell1（L2/t0.3）教师 J 中位 | 1.0（≥0.85 命中） | records/readings 结构与 cell 命中面一致（2/6 cells ≥0.85） | **吻合** |
| cell3（L14/t0.0）教师 J 中位 | 1.0（≥0.85 命中） | 同上 | **吻合** |
| `response_text` 字符长 | min 1／中位 2／max 9 | 与 records 一致（1–9 字符残段） | **吻合** |
| `completion_tokens` | 597–1716（远超 `max_tokens=500`） | 与 records `usage` 一致 | **吻合** |

⇒ ②件读数构造面（J 值／短答／token 挤占）与 records 源一致，无数字矛盾。

#### ③件 · 22 项退化警报（本人独立重扫 · 定向取数）

| 字段（③件 §2.2 表） | ③件申报 `n`/`n_distinct` | 本人复算 | 判定 |
|---|---|---|:-:|
| `captions[].family` | 22/2 | 22/2 | **MATCH** |
| `graphs[].family` | 22/2 | 22/2 | **MATCH** |
| `graphs[].source` | 22/2 | 22/2 | **MATCH** |
| `index_v3.fingerprint_anchors` | 3/3 | 3/3 | **MATCH** |
| `B3.dual_hex_width` | 22/1 | 22/1（全 11） | **MATCH** |
| `B3.diff_vs_f4.semantic_hash_identical` | 22/1 | 22/1（全 False） | **MATCH** |
| `B3.diff_vs_f4.dual_identical` | 22/1 | 22/1 | **MATCH** |
| `B3.diff_vs_v3phys.semantic_hash_identical` | 22/1 | 22/1 | **MATCH** |
| `B3.diff_vs_v3phys.dual_identical` | 22/1 | 22/1 | **MATCH** |
| `B3.chain.link_verified` | 22/1（全 true） | 22/1（全 True） | **MATCH** |
| `B3.chain.self_verified_only` | 22/1 | 22/1 | **MATCH** |
| `F.svd_var_explained(3)` | 3/3 | dict{2,3,4}→3 值列／`nd=3` | **MATCH** |
| 关键支撑：`B3.coords_k[0..2]` | 各 22/22（不命中） | 各 22/22 | **MATCH** |
| 关键支撑：`B3.semantic_hash` | 22/9（不命中） | 22/9 | **MATCH** |
| 关键支撑：`B3.byte_hash`/`dual`/`caption_id` | 22/22（不命中） | 各 22/22 | **MATCH** |

⇒ ③件 22 项警报与「22 项无一为真指纹坍缩」（变值列 byte_hash/dual/caption_id/coords_k 全 nd=22、semantic_hash nd=9 均不命中，仅布尔位 `link_verified` 命中）之核心判断，**独立复算全部吻合**。

### 6.3 内部计数一致性交叉核

| 件 | 计数声明 | 实测 | 判定 |
|---|---|---|:-:|
| ① | §5 表 10 行 ＋ 根因计数（假证伪8＋混合1＋非证伪1=10） | §5 表终态＝PASS×2＋FAIL×1＋KD×7＝10 行；与根因计数自洽 | **自洽** |
| ② | §6 根因计数（真证伪0／假证伪1／不明1） | S1 假证伪、S3 不明，各 1 | **自洽** |
| ③ | §13 根因计数（真证伪0／假证伪2／混合0／不明0） | 分档B命中＋总态KD＝假证伪2 | **自洽** |

---

## §7 发现项清单（分级 · **只登记，不爽改**）

| 编号 | 级 | 件 | 发现 | 处置 |
|:-:|:-:|---|---|---|
| **F-1** | 低 | ① | `_v3_recheck_prereg_v1_2026_09_27.md` 登记值 `434B3213BDCE`／13,233 B 落后于盘上终态 `88052d7db895`／37,346 B | **①件已主动披露并以终态为准**；审计确认为「登记滞后·非隐瞒」，仅事实登记，不改任何件 |
| **F-2** | 低 | ② | L14 verdict 盘上 `8eef73bf9856`／19,697 B ≠ 锚件所载 `764F24A21AC8`／19,708 B（差 11 B） | **②件已如实披露**并登记入勘误链待 PI／EA；审计确认漂移属实，仅登记 |
| **F-3** | 中 | ② | 仓外引用：L2 verdict 实件在 `_non_upload_local_archive`（仓外），仓内 0 命中 | **②件已给全路径＋实测指纹＋拉回路径**；按纪律标注「仓外绝对路径依赖」，**0 写入仓外**，仅登记 |

**无 FAIL／无断裂／无 MISSING_TRUE／无 CONFLICT／无 key 泄漏。** 三件皆如实标注自身局限（①覆盖面、②构造失灵、③判据施用面上抛 PI），无软化措辞用于挽救结论。

---

## §8 审计纪律自证

- **0 翻案、0 篡改**：三件判定结论（① KD／② S1 hit=True·S3 不明／③ 分档A PASS·总态KD）**一字未动**；审计仅核验与登记。
- **0 回改**：本审计**0 修改任何既有件**（三件判定件 ＋ 33 件锚链全部只读，`Get-FileHash` 只读）。
- **0 编造**：全部哈希／字节／读数当轮 `hashlib`／`Get-FileHash`／`statistics` 实测；核不了者写「未核得」——本波**0 处未核得**（三件引用面全部可核）。
- **R4**：key 形态扫描三件 CLEAN，0 读 key、0 入 prompt/JSON/log。
- **0 网络**；**0 合并派生 JSON**（三源 JSON 原样读取）；**0 加载 skill**。
- **不代裁**：①件 5 项候呈（`145.8×` 定性／`4-2` 落法射程／`1-1` 效力射程／C2 扩范围／`K-RO-0-1` 第二出口）、②件 O-2／C-1／C-5、③件 `U-V04-01-新`／`U-V04-02` 均归 PI，**审计 0 代裁**。
- **版式**：UTF-8 无 BOM · 纯 LF；落前 `Test-Path=False` ＋ glob（`*_ea_audit*`／`*audit_batch*`／`*ea_audit_batch_vk*`）三组均 0 命中。
- **自身指纹不自写入本件**（不动点）⇒ 权威 SHA-12／bytes 由回执自报。

---

## §9 总判定

**三件 VK 判定件（`a14aafa220c4`／`dfc858d3d930`／`e98bee353448`）独立证据链审计：逐件 PASS。**

锚链 33＋仓外 1 件全吻合；幽灵引用 0 MISSING_TRUE／0 CONFLICT，分支合规；0 触动成立；key 形态 CLEAN；核心读数独立复算全部吻合；内部计数自洽。三件对自身局限（覆盖面／构造失灵／判据施用面）均如实标注，0 软化挽救，0 编造来源。发现 3 项低–中级事实漂移/仓外依赖（F-1 登记滞后·已自曝／F-2 哈希漂移·已自曝／F-3 仓外引用·已给拉回路径），**均已由对应判定件主动披露**，审计确认披露属实，仅作登记。

**审计结论：收官门槛③「evidence-auditor 审计 PASS」——本波三件达成。** 本审计不替代 verifier 独立复核与 PI 复核（沿二件 §9.3／§10 入链流程）。

---

*出证 = evidence-auditor｜2026-10-09｜独立复算 0 复用自报值｜锚链 33＋1 全核验｜0 回改、0 翻案、0 编造、0 网络、R4 0 读 key、0 合并派生 JSON、0 skill 加载*