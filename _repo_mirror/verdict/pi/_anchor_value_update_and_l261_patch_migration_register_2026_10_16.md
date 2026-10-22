# `P_A_HARNESS` 锚值更新 ＋ L261／patch 载体同批处置登记件（2026-10-16）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_anchor_value_update_and_l261_patch_migration_register_2026_10_16.md` |
| **件性质** | **锚值更新 ＋ 连带同批处置之登记件（另立承载 · ⛔ 0 回改任何既有件一字）** |
| **落盘方** | `evidence-auditor`（锚面更新棒） |
| **对象** | `P_A_HARNESS` ＝ `tools/exp_harness.py` |
| **授权面（逐字）** | PI 2026-10-16 交互卡 `ask_83a44986f5d822a1ba7b83ad`（schemaVersion 2 · mode questionnaire · submittedAt ms `1792121360830` ≈ 2026-10-16 11:29:20 CST）§1 **Q3** 逐字答**「登记值随更新（另立锚版）（推荐）」**（选项 id `q3_bc7f19be_opt1`）· 登记件 `results/_pi_card_answers_register_2026_10_16_v20.md`（SHA-12 `44aa59715d21` ／ **6,075 B** · **本棒实测吻合正身**）· 题面摘要逐字：「现值 `7a097d7802d1` 于任何锚载体 0 出现（活载体仍载 `9f383935c00c`·patch 载体 PENDING 仍在盘）⇒ 不符持续存在。」 |
| **reconcile 指针** | `results/_harness_anchor_reconcile_register_2026_10_16.md#`4de10aad8f0b`（26,023 B · 本棒实测吻合）· 其 §4-2 候裁面即本卡所答之问 |
| **同批三面** | ① 锚版更新落账 → `results/_pa_harness_anchor_value_update_v2.json`｜② spec 锚表 L261 并立附注 → 本件 §3｜③ patch 载体状态迁移登记 → 本件 §4 |
| **件状态** | 已落盘 · ⛔ **0** 代 PI 裁 · ⛔ **0** 宣告①毕 · ⛔ **0** 回改／移动／重命名／删除任何既有件 |

---

## §0 一句话结论

PI 裁「登记值随更新（另立锚版）」之执行面已落为**三面并行承载**：锚值由 `9f383935c00c` 更新至**本棒直算之现值 `7a097d7802d1`**（15,708 B）并**另立锚版** `results/_pa_harness_anchor_value_update_v2.json`（⛔ 0 回改活载体 `03c6c01f3697` 与 spec 锚表）；spec L261 之关系由**并立附注**承载（本件 §3 · 含一条**勘误**：派工面所给 spec 哈希 `423c84de20d5` 与「L261／锚表」**不成立**，真身系 `78b71d404366` L261，双面并注）；patch 载体 `patch_status: PENDING` 之 `P_A_HARNESS` 项由**状态迁移登记面**承载（本件 §4 · 并**明载**该 PENDING 所待 reconcile 之值 `275e480ba4d9` 早已被第二·三层取代，迁移落**终值**而非其待值）。

---

## §1 指纹实测（本棒直算 · 全部 `hashlib.sha256(bytes).hexdigest()[:12]` ＋ 字节数 · ⛔ **0** 用内建 `hash()` · ⛔ **0** 沿用他件自报值）

| SHA-12（本棒实测） | bytes | 件名（repo 相对） | 本棒用途 |
| :-: | --: | :-- | :-- |
| `44aa59715d21` | 6,075 | `results/_pi_card_answers_register_2026_10_16_v20.md` | **本棒授权面正身** |
| `4de10aad8f0b` | 26,023 | `results/_harness_anchor_reconcile_register_2026_10_16.md` | reconcile 件（只读） |
| `652da23484e2` | 15,336 | `results/_mq_rollout_v2_effect_register_2026_10_14.md` | **授权漂移例外三要件**之出处（只读） |
| `03c6c01f3697` | 6,680 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | **活锚载体**（载 `9f383935c00c` · 只读） |
| `da517c115f3c` | 5,049 | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | 派生 patch 载体（载 `patch_status: PENDING` · 只读） |
| `6e9cd8cd8e07` | 11,318 | `verifier/handoff/KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | C7 版锚载体（载 `275e480ba4d9` · 只读） |
| `78b71d404366` | 29,570 | `docs/V3X/KT_A1_SPEC_V0.1.md` | **spec 锚表真身**（L261 之 `P_A_HARNESS` 行在位 · 只读） |
| `423c84de20d5` | 15,457 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | 派工面所给 spec 哈希（**勘误对象** · 只读） |
| `1308662a369a` | — | `results/_t5_anchor_drift_authorized_register_2026_10_15.md` | 第二层登记件（只读） |
| `aa8e9fce651c` | — | `results/_t3trap_answerable_drift_authorized_register_2026_10_15.md` | 第三层登记件（只读） |
| **`7a097d7802d1`** | **15,708** | **`tools/exp_harness.py`** | **实体面现值（本棒直算 · 本棒所更新之目标值）** |

**实体面现值复测（本棒直算 · 独立通道）**：`sha256[:12]` ＝ **`7a097d7802d1`**；bytes ＝ **15,708**；BOM ＝ **False**；CR ＝ **0**；CRLF ＝ **0**；TAB ＝ **0**；CTRL（除 `\n`）＝ **0**；U+FFFD ＝ **0**；mtime ＝ **2026-10-15 17:17:49**。内容标记实测：`M1` ×8／`M2` ×5／`M3` ×6／`T1_GSM8K` ×1／`T2_StrategyQA` ×1／`T3_Trap` ×2／`T4_2x2` ×1／`T5_LowResource` ×1／`LowResourceTask` ×3／`clues` ×2 ⇒ **第三层持有面 MATCH**。

**四值出现面实测（排除 `.git`／`__pycache__`／`.tmp`）**：`9f383935c00c` 96 次／35 件；`275e480ba4d9` 155 次／43 件；`7957bac14455` 44 次／7 件；**`7a097d7802d1` 44 次／8 件**。⚠ 本棒独立复现 reconcile §3-3 之关键事实：**`7a097d7802d1` 于任何锚载体（`KT_ABC1_anchors*`／`KT_A1_SPEC*`）0 出现** ⇒ 此即「另立锚版」之必要性所在。

---

## §2 面一 · 锚版更新落账（`results/_pa_harness_anchor_value_update_v2.json`）

| 项 | 值 |
| :-- | :-- |
| **登记值变更** | `P_A_HARNESS`：`9f383935c00c` → **`7a097d7802d1`** |
| **承载面** | **另立锚版 v2**：`results/_pa_harness_anchor_value_update_v2.json`（沿先例 `03c6c01f3697` 之 schema：`object`／`path`／`algorithm`／`value`／`field`） |
| **⛔ 未回改（逐字点名）** | 活锚载体 `03c6c01f3697` 之 `/anchors/KT-A1/P_A_HARNESS/value` 仍载 `9f383935c00c`；`.bak` `6e9cd8cd8e07` 仍载 `275e480ba4d9`；spec 锚表 `78b71d404366` L261 仍载 `9f383935c00c` —— **一律只读、0 字节改动** ⇒ **新旧并存以新为准** |
| **生效时点** | **卡提交时点**：submittedAt ms `1792121360830` ≈ 2026-10-16 11:29:20 CST（**非**本件落盘时点；落盘晚于授权面，已如实标注于锚版件 `effective_at`） |
| **`field` 之校正** | 活载体与 spec 皆载「任务族 T1-T4」，而实体面现含 `T5_LowResource`（第二层补造）⇒ 锚版 v2 之 `field` 校正为 **T1-T5** 并**逐项列出**；⛔ **0** 就地改活载体与 spec 之字面（校正仅存于新立锚版） |
| **三层漂移链之证据面** | 锚版件 `three_layer_drift_chain` 载逐层：授权链／OLD→NEW／delta bytes／显式声明／实体现状。链之合读：`9f383935c00c` → `275e480ba4d9` → `7957bac14455` → `7a097d7802d1`，**首尾相接、0 断点**；授权事件均先于实体变更 |
| **`anchor_status` 延续面** | `anchor_status: drift_authorized` ＋ `authorization_refs` 六条（沿 `1308662a369a` §4／`aa8e9fce651c` §4 之机器可读载荷形制）；**本 v2 未制造新漂移**，乃承载「登记值已追上第三层已授权漂移」之事实 |

---

## §3 面二 · spec 锚表 L261 之并立附注（另立承载 · ⛔ 0 回改 spec 一字）

### §3-1 附注之本体（口径即派工面所定）

> **L261 登记面 → 现值 `7a097d7802d1`（三层授权漂移链 · reconcile 件指针）→ 引证口径须并引本附注。**

| 项 | 值 |
| :-- | :-- |
| **登记面** | L261 之 `P_A_HARNESS` 行载 `9f383935c00c` |
| **现值面** | **`7a097d7802d1`** ／ 15,708 B（本棒直算） |
| **漂移链指针** | reconcile 件 `results/_harness_anchor_reconcile_register_2026_10_16.md#4de10aad8f0b`（三层逐层对照 ＋ 四分支对账） |
| **引证口径** | 凡引 L261 之 `P_A_HARNESS` 者，**须并引本附注**；引 `9f383935c00c` 为「登记面之历史值」、引 `7a097d7802d1` 为「现值」，二者**并存不冲突** |
| **撤回触发条（同面并录 · ⛔ 0 代裁其射程）** | `78b71d404366` **L263** 逐字「**任何 ≥ 1 锚漂移 → 全 KT-A1 撤回**」；其射程与触发属 PI 裁面，⛔ **0** 在本棒宣告触发与否 |

### §3-2 ⚠ 勘误：派工面所给 spec 哈希与「L261／锚表」不成立（本棒实测）

| 项 | 实测 |
| :-- | :-- |
| **派工面所述** | 「spec 锚表 L261（`423c84de20d5`）」 |
| **实测** | `423c84de20d5` ＝ `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md`（15,457 B · 本棒实测吻合正身）＝ **P-B 失真界 V0 规范**；全文共 **178 行** ⇒ **L261 不存在（越界）**；`P_A_HARNESS` 字面于该件 **0 次**；其 §2 五锚表（L20–L32）载 **`P_B_*`** 五锚，撤回触发条在 **L32／L134** 逐字「任何 ≥ 1 锚漂移 → 全 V0 撤回。」⇒ **系 P-B 锚表，⛔ 非 `P_A_HARNESS` 之登记值载体** |
| **L261 真身（本棒逐字回读）** | `docs/V3X/KT_A1_SPEC_V0.1.md`（SHA-12 `78b71d404366` ／ 29,570 B）**L261** 逐字：<br>`\| P_A_HARNESS \| tools/exp_harness.py \| SHA-256 全文 → 前 12 位 \| 机制 M1/M2/M3 + 任务族 T1-T4 \| **9f383935c00c** \|` |
| **独立佐证** | reconcile 件 `4de10aad8f0b` §3-1 L96 **独立记载**同一事实：「`docs/V3X/KT_A1_SPEC_V0.1.md`（spec 锚表 · 逐字回读 L261）｜`78b71d404366`｜29,570｜**`9f383935c00c`**」⇒ 本棒实测与既有记载吻合 |
| **溯源（⛔ 0 臆造）** | `423c84de20d5` 于 `P_A_HARNESS` 证据链中之**合法出现位置** ＝ `aa8e9fce651c`（`aa8e9fce651c`）**L120** 之 `spec_withdrawal_clause` 字段引用 `P_B_DISTORTION_BOUND_V0_SPEC.md:32` ⇒ 派工面或系自该引用面**误推至「L261／锚表」** |
| **同件第二处（并录）** | `78b71d404366` **L239** 逐字亦载 `P_A_HARNESS` ＝ `9f383935c00c`（实施细节段，非锚表行）⇒ 该件 `P_A_HARNESS` 字面共 **2 次**（L239＋L261） |

### §3-3 双面并注之处置（如实登记 · 不代裁）

本附注**同时**挂于两面：① `78b71d404366` L261（KT-A1 锚表 · `P_A_HARNESS` 行真身）＋其 L263 触发条；② `423c84de20d5` L32／L134（P-B 面 · 撤回触发条）。**⛔ 0** 回改任一件一字、**⛔ 0** 移动／重命名、**⛔ 0** 代裁「何者为正确之 spec 面」（属 PI 裁面）。本勘误之定性 ＝ **ERRATUM／连带登记**（登记，非静默改靶）。

---

## §4 面三 · patch 载体 `patch_status: PENDING` 之状态迁移登记（另立登记面 · ⛔ 0 回改该载体一字）

### §4-1 迁移登记（`P_A_HARNESS` —— 本卡之对象）

| 项 | 值 |
| :-- | :-- |
| **载体** | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json`（SHA-12 `da517c115f3c` ／ 5,049 B） |
| **盘上原状态（逐字仍在盘）** | `/p_a_patches/P_A_HARNESS/patch_status` ＝ **「PENDING（待 D7 后 5 锚 JSON V0.2 / V3X 正式升级 reconcile）」**；顶层 `/patch_summary/patch_status` ＝ 「DERIVED（原始 frozen 0 触动；本 JSON 为派生 patch 记录）」 |
| **迁移** | **PENDING → RESOLVED_BY_RECONCILE_AND_ANCHOR_VERSION_V2** |
| **消解依据** | ① reconcile 件 `4de10aad8f0b`（`reconcile_status` 于其登记面落为 `reconciled`）；② 锚版 v2 件 `_pa_harness_anchor_value_update_v2.json`（登记值 `9f383935c00c` → `7a097d7802d1`） |
| **⛔ 0 回改** | 该载体**一字未改**，其 `patch_status: PENDING` 字面**仍在盘**；迁移**另立承载**于本件（沿「新旧并存以新为准」） |

### §4-2 ⚠ 关键防误读注记（本棒实测 · 必录）

patch 载体之 `P_A_HARNESS/value_v3x_new` ＝ **`275e480ba4d9`**（其 2026-09-15 13:24 之观测值）——**该值早已被第二层（`275e480ba4d9`→`7957bac14455`）与第三层（`7957bac14455`→`7a097d7802d1`）取代**。故本次迁移所落之值为**终值 `7a097d7802d1`**，**⛔ 非** patch 所待之 `275e480ba4d9`。

> 📌 **诚实之根因是不误导**：若后续有人径引 patch 载体之 `value_v3x_new` 为「现值」，即被误导。故本注记**逐字在册**。同理，patch 之 `file_size_B_now` ＝ 10,090，与现值 15,708 B 不符（**已随三层漂移过时**）。

### §4-3 射程外未决项 · 明载（⛔ 0 代裁 · ⛔ 0 计入已消解）

| 项 | 值 |
| :-- | :-- |
| **锚 ID** | **`P_A_LLM_CLIENT`** |
| **盘上原状态** | `/p_a_patches/P_A_LLM_CLIENT/patch_status` ＝ **「PENDING」**（**仍在盘 · 本棒未动**） |
| **为何未随本批消解** | 本卡 Q3 之对象 ＝ `P_A_HARNESS`；reconcile 件 `4de10aad8f0b` 之射程亦仅 `P_A_HARNESS` ⇒ `P_A_LLM_CLIENT` 之 PENDING **不在**本批授权射程内 |
| **实测事实** | `tools/llm_client.py` ＝ **`1722500da4aa`** ／ 8,118 B（本棒直算）＝ patch 载体 `value_v3x_new` 之值 ⇒ 其**实体面**仍为该值（此为事实登记，⛔ 非消解之宣告） |
| **处置** | **列为 OPEN 未决项**；⛔ **0** 宣告已消解、⛔ **0** 代裁、⛔ **0** 移作本卡授权 ⇒ **须 PI 另给／另裁方动** |

---

## §5 与「授权漂移例外三要件」之逐要件符合性自核

**三要件之逐字原文**（卷 2 `652da23484e2` §2-3 `MQ-08` · 本棒逐字回读）：

> **要件 (a) 授权链** ＝ 授权事件 ＋ OLD→NEW 对照 ＋ 现值复测；
> **要件 (b) 登记面** ＝ `anchor_status: drift_authorized` ＋ `authorization_refs`；
> **要件 (c) 显式声明** ＝ 该漂移属「**合法返工**」抑或「**未授权变更**」—— **未授权者不在例外内，条款仍然自动触发**；设置理由照录「否则例外沦为**自证之门**」。

| # | 要件 | 本棒自核（事实层面） |
| :-: | :-- | :-- |
| 1 | **(a) 授权链** | ✅ **三要素齐备**：授权事件 ＝ 卡 `ask_83a44986f5d822a1ba7b83ad` Q3 ＋ 登记件 `44aa59715d21` §1 Q3／§2 派生动作 B；OLD→NEW ＝ `9f383935c00c` → `7a097d7802d1`；现值复测 ＝ 本棒 §1 独立通道实测 `7a097d7802d1`／15,708 B **MATCH** |
| 2 | **(b) 登记面** | ✅ **齐备且机器可读**：锚版 v2 件载 `anchor_status: drift_authorized` ＋ `authorization_refs` 六条；连带两面（本件 §3 附注、§4 迁移登记）**另立承载**，⛔ 0 写入既有锚 JSON／spec／patch 载体 |
| 3 | **(c) 显式声明** | ✅ **合法返工**（`legal_rework`）：三层逐层皆具独立显式声明（`1308662a369a` §5／`aa8e9fce651c` §5 逐字）；且 MQ-08 生效范围第 4 项「三要件第 ③ 项『合法返工』之推断 ＝ 随打包过获 PI 核准」⇒ 该推断**已获 PI 核准** |
| 4 | **并读：与三层漂移之关系** | ✅ 本件**未制造新漂移**：`7a097d7802d1` 之实体面早于本卡已落定（2026-10-15 17:17:49），本卡所裁者为**登记值之追平**（登记面落后于实体面之持续不符之消解）⇒ **⛔ 0** 以本卡授权充任三层任一层之变更授权（三层各有独立授权链） |

**自核之诚实边界（逐条）**：

1. ⛔ **0** 代裁「是否在例外内」之终局 —— 本棒自核仅止于「三要件齐备与否」之**事实层面**；终局宣告通道唯一 ＝ PI 明示。
2. ⛔ **0** 自证 —— 授权事件取自**他件**（卡 ＋ 登记件 ＋ reconcile 件 ＋ 漂移登记件），指纹取自**盘上实测**（§1），现值复测取自**本棒独立通道**。
3. ⛔ **0** 扩大化 —— §4-3 之 `P_A_LLM_CLIENT` 未决项、§3-2 之勘误、§3-1 之撤回触发条射程，三者**均只登记不处置**。

---

## §6 纪律自核

| # | 纪律 | 自核结果 |
| :-: | :-- | :-- |
| 1 | ⛔ 0 代 PI 裁 | ✅ 本件只做**登记与落账**；勘误、未决项、触发条射程**三处并列列出**，⛔ 0 代择／0 代给值 |
| 2 | ⛔ 0 回改既有件 | ✅ 活载体／`.bak`／patch 载体／spec（KT-A1 与 P-B 两件）／三登记件 —— **写后逐件复算，写前 ＝ 写后**（见 §7） |
| 3 | ⛔ 0 宣告①毕 | ✅ **0 宣告** |
| 4 | 指纹实测（⛔ 0 凭转述） | ✅ §1 全表**均为本棒直算**（`hashlib.sha256`）；关键节**逐字回读**（v20 §1 Q3／KT-A1 spec L239/L261/L263／P-B spec L20–L32／patch 载体全件／reconcile §3-1·§4-2·§5） |
| 5 | ⛔ 0 臆造来源 | ✅ 勘误之溯源（`aa8e9fce651c` L120）**有据方述**；无据处（第一层无卡号）**未虚构** |
| 6 | 哈希工具 | ✅ `hashlib.sha256`（stdlib）；⛔ **0** 用内建 `hash()` |
| 7 | 仓外只读 0 写入 | ✅ 本棒**未**扩至仓外目录 |
| 8 | 落盘纪律 | ✅ `io.open(encoding='utf-8', newline='\n', errors='strict')` 直写；⛔ **0** 经 PowerShell 管道中转 UTF-8 正文；辅助脚本落于 `.tmp/`；key 形态扫描**落盘前 0 命中**（R4） |

---

## §7 落盘自测（字节级 · 落盘后独立通道复算）

| 项 | 值 |
| :-- | :-- |
| 目标路径 ① | `results/_pa_harness_anchor_value_update_v2.json` |
| 目标路径 ② | `results/_anchor_value_update_and_l261_patch_migration_register_2026_10_16.md` |
| `Test-Path`（落盘前） | ① **False**　② **False** |
| glob（落盘前） | `results/_pa_harness*` **0 命中**；`results/*anchor_value_update*` **0 命中**；`results/*l261*` **0 命中** |
| 占用改名（`_r1`） | **未触发**（两件之 `_r1` 名亦 0 占用） |
| SHA-12 ／ bytes | **落盘后独立通道实测 ＝ 见交付回执**（自哈希不可内嵌本文件 —— 写入即改变其字节） |
| BOM ／ CRLF ／ CR ／ TAB ／ CTRL ／ U+FFFD | 逐件实测见交付回执（期望全 0／False） |
| 源件未被改动（写后复测） | §1 所列各件指纹**写前 ＝ 写后**（逐件复算，见交付回执） |

---

**署名**：`evidence-auditor`｜**件日**：2026-10-16｜**状态**：**已落盘**（PI 裁之执行面已落账；⛔ 0 代裁 · ⛔ 0 宣告①毕 · ⛔ 0 回改任何既有件一字）
