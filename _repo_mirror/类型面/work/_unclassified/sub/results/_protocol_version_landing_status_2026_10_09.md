# `protocol_version` 产出层落实（V3-02）· 执行状态登记 · **停手候呈** · 2026-10-09

- **件性质**：**执行状态登记**（W4 波 · V3-02）｜**结论：0 执行 · 停手候呈 PI**（**未补跑、未改码、未改任何既有件**）
- **出件**：**worker**（W4-02 棒 · 分支会话 `mvs_2b422025488243c497e9ab786338c993`）｜⛔ 0 冒充 PI／verdict-keeper／protocol-keeper
- **授权锚**：PI 2026-10-09 卷⑨问卷（`ask_cfb9284519a5abf29d0f03eb`）Q1「五段全开·批准后当日即办」＋ W4 波许可（`results/_closing_round_8_decisions_register_2026_10_09.md`〔`a28a478e14a8`〕§1 Q4①「W4 产出链重走**许可**✓」／§2.4 待启清单）
- **版式**：UTF-8 无 BOM · LF｜**件名**：`results/_protocol_version_landing_status_2026_10_09.md`（新名 · 0 覆写）
- **命名裁定**：派工建议名 `results/_protocol_version_landing_2026_10_09.md`；本棒实读后取 `_landing_status_`（**「落实」未发生，实际态为「停手候呈」**，沿 PI 2026-09-29 命名裁 `57024f2cd30a`「去版本前缀：`_主题_日期`」之 `_主题_日期` 口径；**0 V-阶段前缀**）。落前 `Test-Path` ＝ False；全仓 glob `*protocol_version*` 仅命中既有补记件 1 件（0 撞名）。

---

## §0 状态一句话

**三件产出件 `protocol_version` 仍为 0 命中（缺口属实、维持未闭合）；「以产出链重走落实该键」在盘上 0 可执行路径**——重跑既有 runner **不产该键**（runner 字面 0 命中），而使其产键**必须改码**，改码被 PI 2026-10-01 裁**明文排除**且违 W-5 ⇒ **本棒 0 执行、停手候呈**。

---

## §1 三件产出件逐件态（本轮 `Select-String` 全文复算 · 0 猜测）

| # | 路径 | SHA-12（本轮实测） | 字节 | CRLF | `protocol_version` 命中 | 写入落实 | 是否重走 |
|:-:|---|---|---:|---:|---:|:-:|:-:|
| ① | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | 20,398 | 736 | **0** | **否** | **否** |
| ② | `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | 24,421 | 579 | **0** | **否** | **否** |
| ③ | `results/c5_b_group_fix_readings_2026_10_01.json` | `2a7749da7c4d` | 9,996 | 447 | **0** | **否** | **否** |

- **三件身份来源（0 猜测 · 逐件盘上核）**：三件之**列举**载于 `results/c5_b_group_verdict_2026_10_01.md`（`3fbf6b38a383`／30,118 B）L156 逐字：「产出层载体 **仍缺**：本人对三件产出件全文检索 `protocol_version` 命中数 ＝ **0**（① B3 产出件 `33ad1c01f745` ② `index_v3` `3ba2449cf986` ③ 修后读数件 `2a7749da7c4d`）」；本棒按该三路径**逐件独立复算** ＝ **三件均 0 命中** ⇒ **缺口属实、当轮复核仍成立**。
- **行尾口径**：三件均 **CRLF**（与 `results/`／`corpus/` 同族数据件一致，Python Windows `open` 默认）⇒ ⛔ **0 以行尾推定编码异常**、**0 归一化**（沿线索册条 2.88 同族纪律）。
- **上游语境（线索册 §2.14 · 条 2.92／2.93／2.91）**：`letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md`（`0fd7a26fc339`／109,614 B）L327 载「`U-V04-01` `protocol_version` **产出层缺口**（三件产出件 0 命中；规则面已由 V0.4 spec 承载，**缺口属实**、⛔ 0 声称已闭合）」；L326 禁述⑥「⛔ **0 声称 `protocol_version` 键已写入产出件**」**本棒 0 违反**。

---

## §2 产出链构成（逐件盘上核 · 0 猜测）

| 环节 | 实体 | SHA-12 | 字节 | 本轮实测要点 |
|---|---|---|---:|---|
| 规则载体（**唯一**） | `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | `c13449101ab3` | 34,367 | §2.4 L116/L121 载 `protocol_version = "V0.4"`（常量）**规则面已定且生效**；L122 载产出层缺口 |
| 产出链 runner（①② 之源） | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | `de16bc002198` | 20,322 | ⛔ **`protocol_version` 字面命中 ＝ 0**；`LSH_SEED=42`／`K_COMPONENTS=3`／`N_PLANE=18`／`HEX_WIDTH=5`／`DATE="2026-09-29"` 固定；**0 wall-clock 字段**；**0 CLI/argv 覆写出口**（仅 L453 `sys.exit(main())`） |
| ③ 之源（**独立生成器**） | `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` | `191efa7fe0b6` | 12,014 | ⛔ **`protocol_version` 字面命中 ＝ 0** |
| runner 输入料 | `results/_v5_v3_deg_c5_b_raw_embeddings_2026_09_29.json`／`corpus/v20/strip_captions_22.json`／`corpus/v20/index.json` | — | — | **三件均在盘**（`Test-Path` ＝ True）⇒ 阻断**0 源于缺料** |

**产出链覆盖缺口（关键）**：既有 runner 之 2 个写出目标（L62–63）＝ `corpus/v20/index_v3_2026_09_29.json` ＋ `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` ＝ **①②**；**③ 修后读数件不属该 runner 之产出**（属 `.tmp/_v5_c5_b_fix_readings_2026_10_01.py`）⇒ **单跑「产出链重走」连覆盖面都不达三件**。

---

## §3 停手依据（四项 · 逐条盘上字面锚）

**① 「重走」不产该键** —— runner `de16bc002198` 与 ③ 生成器 `191efa7fe0b6` 之 `protocol_version` 字面命中**均为 0** ⇒ 原样重跑**逐字复现既有产出面**，三件仍 0 命中，**验收字面「`protocol_version` 落实」不成立**。

**② 产键必改码，而改码被明文排除** —— 使产出件含该键，**唯一既有路径＝在 runner／生成器写入字典新增该键**（既有产出字典 L281–298／L256–270 无该键位）＝ **改码**。而：
- PI 2026-10-01 10:16:09 回执（`ask_d50c961a307949025a7b8d2d`）Q1② 裁（`results/_mini_round_3_decisions_register_2026_10_01.md` L100 逐字）：「`protocol_version` 缺口 ⇒ **另立补记件**（**非补跑／非改码**）」；
- V0.4 spec §2.4 **L123** 逐字：「⛔ **0 擅改 runner 既有字面**（W-5）⇒ **0 由本件回改 runner／产出 JSON**」；§7 `U-V04-01`（**L371**）归属 **verdict-keeper／PI**，0 代裁 0 代执行。

**③ 10-01 之「另立补记件」路径已执行完毕** —— `results/c5_protocol_version_annex_2026_10_01.md`（`2593ea7b93cf`／18,558 B／mtime 2026-10-01 10:25:17）**已在盘**，为该裁之唯一承载件；其 §8-3 逐字「⛔ **0 补跑**：0 重走 B3 chain、0 重算 root」、§7「补齐动作 **0 执行**……若 PI 日后裁「补跑」或授权「改码」⇒ **另派**」⇒ **V3-02 之既有方法面已闭合于「登记＋界定」，产出层按 10-01 裁维持未闭合**。

**④ 原样重跑另有覆盖写风险** —— runner 写出目标**硬编码＝①② 之现有路径**（0 覆写 pin 仅覆盖 2026-09-16 两件 `efe05ad775de`／`b5873afb9d29`，**不覆盖 ①②**）⇒ 原样重跑将**覆写已在册产出件**（违 0 回改既有件）；且 ③ 根本不由该 runner 产出。

> ⇒ 合并结论：**「产出链重走」＝ 原样重跑（不产键 ＋ 覆写 ①② ＋ 漏 ③）｜「改码」＝ 被 10-01 裁排除 ＋ 违 W-5**。两条路均不可执行 ⇒ **停手候呈**（沿派工单「若『产出链重走』之确切做法在盘上 0 明确规格，停手候呈，0 自创做法、0 擅改既有件」）。

---

## §4 附带发现（登记 · 0 回改母件）

**⚠ 缺口排期主件 V3-02 行规则载体引用错件**：`results/_v34_experiment_gap_plan_2026_10_08.md`（`996feb1db9cb`／36,066 B）L78 载「已由 **`423c84de20d5`** §2.4 承载规则」。本轮实测：**`423c84de20d5` ＝ `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`**（P-B 失真界 V0 规格件／15,457 B），该件 `protocol_version` 命中 **0**、其 §2 为「锚点（pre-registered SHA-256 前 12 位）」**无 protocol_version 规则面** ⇒ **V3-02 行所引非规则载体**。规则面真实唯一载体为 **`c13449101ab3` §2.4**（V0.4 spec）。**本棒 0 回改该母件一字**，仅登记差异（沿「0 回改既有件・漂移/差异仅登记」纪律）；供 parent 择机并入勘误链。

---

## §5 候呈 PI（0 代裁 · 三选项互斥）

| 档 | 内容 | 代价/风险（盘上依据） |
|---|---|---|
| **甲** | **维持 10-01 裁**（另立补记件已落 `2593ea7b93cf`）⇒ **V3-02 按 10-01 方法面销项**，验收字面由「产出件写入该键」改为「补记件在位 ＋ 缺口如实登记」 | 0 代价；产出层缺口**维持未闭合**（与 spec L122 一致） |
| **乙** | **授权改码**（另派 worker：runner／③ 生成器新增该键 ＋ **新名输出** 0 覆写） | 触 W-5 ＋ 违 10-01「非改码」裁 ⇒ **须 PI 明文覆裁**；root 漂移风险已登记（`reproduce_within_4dp = false`、偏差 `8.98e-03` ⇒ 触 root 候选件 §9 看护项 2 构造未变警报面） |
| **丙** | **授权补跑** | ⛔ **逻辑不成立**：不 concomitant 改码则键仍不落（§3①）；改码则 ＝ 乙 |

**最小问题（请 parent 转 PI 裁）**：**V3-02 是否覆裁 2026-10-01「非补跑／非改码」之裁？** 若否（甲档）⇒ 缺口按 10-01 面维持登记、W4 验收字面须改述；若拟推进（乙档）⇒ 须 PI 明文授权改码 ＋ 指定新名 ＋ 另立 kill-line 面。

---

## §6 0 回改与纪律自查

- **0 回改既有件**：本棒**唯一写入面 ＝ 本件（新名）**；三件产出件、runner、③ 生成器、V0.4 spec、缺口母件、线索册、批录件、卷⑧ 登记件 **byte 0 触动**（§1／§2 指纹为开棒前后同一实测值，登记于本件文末回执行）。
- **0 编造**：三件身份、runner／生成器身份、输入料存在性、全部指纹与命中数**均为本轮 `Get-FileHash`／`Select-String`／`Test-Path` 实测**；规则字面逐条引自盘上件行号。
- **0 代裁**：§5 三档 0 择定、0 预填；本棒仅呈报。
- **0 网络 · 0 端点 · 0 key**：0 网络调用、0 读 `.env`／key、**R4 key 永不明文**。
- **0 合并派生 JSON · 0 触 frozen · 0 阶段名自升**：本件 0 合并任何派生 JSON、0 触 frozen 面；所引 `V3`／`V0.4` 字样**均为既有件既有字面之引用**，本件名 0 含 V-阶段前缀。
- **0 自创做法**：产出链重走之做法缺口已如实呈报，**0 以自拟方案替代 PI 裁**。

---

## §7 本轮实测指纹回执行（本件 0 自指 SHA · 供 parent 复核）

| 路径 | SHA-12 | 字节 |
|---|---|---:|
| `results/_v34_experiment_gap_plan_2026_10_08.md` | `996feb1db9cb` | 36,066 |
| `results/_closing_round_8_decisions_register_2026_10_09.md` | `a28a478e14a8` | 2,151 |
| `results/_naming_ruling_note_2026_09_29.md` | `57024f2cd30a` | 7,843 |
| `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md` | `0fd7a26fc339` | 109,614 |
| `results/c5_b_group_verdict_2026_10_01.md` | `3fbf6b38a383` | 30,118 |
| `results/c5_protocol_version_annex_2026_10_01.md` | `2593ea7b93cf` | 18,558 |
| `docs/V3X/P_D_FINGERPRINT_V0_4_SPEC.md` | `c13449101ab3` | 34,367 |
| `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | 15,457 |
| `docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md` | `f119f2f30287` | 34,393 |
| `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_09_29.py` | `de16bc002198` | 20,322 |
| `.tmp/_v5_c5_b_fix_readings_2026_10_01.py` | `191efa7fe0b6` | 12,014 |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | 20,398 |
| `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | 24,421 |
| `results/c5_b_group_fix_readings_2026_10_01.json` | `2a7749da7c4d` | 9,996 |

> 本件落盘后自身 SHA-256／SHA-12／字节／行尾（UTF-8 无 BOM · LF）**由写入方实测回报**（0 自指）。
