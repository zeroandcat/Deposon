# 5 锚 v3 锁记件（2026-10-15 · 锁之外置 · ⛔ 0 自指）

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md` |
| **件性质** | **锁记件**（登记被锁件之指纹 · 逐条证据指针 · 新旧并存声明 · KD 照录面） |
| **落款** | `evidence-auditor`（证据链审计官）· 2026-10-15 |
| **被锁件** | `results/_ge01_prereg_5anchor_v3.json` |
| **授权源卡** | `ask_207b060a5273ab88912e451f`（schemaVersion 2 · mode questionnaire · 提交 2026-10-15 12:49 CST） |
| **登记件** | `results/_pi_card_answers_register_2026_10_15_v13.md` · SHA-12 `693181b9354b` · 3,661 B（本棒直算复核相符） |
| **生效时点** | **＝ 卡提交时点** ms `1792039740320`（≈ 2026-10-15 12:49:00 CST）· ⛔ 非棒自签 |
| **跑禁** | **0 跑任何实验**（本棒全文 0 次实验调用） |

> 📌 依「锁之外置」纪律：被锁件 `v3.json` **⛔ 0 载自身指纹**（自指悖论）⇒ 其指纹由**本件**登记。本件**亦不自载自身指纹**（同一悖论）⇒ 本件之 SHA-12／bytes 载于**交付回执**（盘上实测）。

---

## §1 被锁件之指纹（本棒直算 · 非转述）

| 项 | 盘上实测值 | 要求 | 判 |
| :-- | :-- | :-- | :-: |
| 路径 | `results/_ge01_prereg_5anchor_v3.json` | —— | ✅ |
| **SHA-12** | **`0c269b9558da`** | 锁之载体 | ✅ |
| **bytes** | **`35911`** | —— | ✅ |
| 算法 | `hashlib.sha256(全文字节).hexdigest()[:12]`（stdlib；⛔ 0 用内建 `hash()`） | —— | ✅ |
| 自含自身指纹 | **False**（逐字扫描：`0c269b9558da` 于本件内 0 命中） | ⛔ 0 自含 | ✅ |

---

## §2 生效时点

| 项 | 值 | 出处 |
| :-- | :-- | :-- |
| **生效时点** | **ms `1792039740320`** ＝ 卡提交时点 | 登记件 v13 `693181b9354b` 表头逐字：「提交时点 \| submittedAt ms `1792039740320`（≈ 2026-10-15 12:49:00 CST）」 |
| 口径 | 生效时刻 ＝ **PI 核准回执之时点 ＝ 卡提交时点**（⛔ 非棒自签） | 登记件 v13 `693181b9354b` 之提交时点行 ＋ v2 之同口径先例 |
| 三裁 | Q1「C-甲 kills=10 GT（推荐）」／Q2「裁丁（推荐）」／Q3「授权另立 v3＋锁记件（推荐）」 | 登记件 v13 `693181b9354b` §1-Q1／§1-Q2／§1-Q3 |
| 选项 id | `q1_31ecdfd0_opt1`／`q2_33b33471_opt1`／`q3_6a78f263_opt1` | 登记件 v13 `693181b9354b` §1 |

---

## §3 变更面之一 · `P_B_KILL_LINE.field`（＝ `kills=10 GT`）

### §3-1 变更逐字

| 项 | v2（未动·留痕） | v3（新立） |
| :-- | :-- | :-- |
| `field` | `候 PI 给` | **`kills=10 GT`** |
| 随变子键 | `field_status` 载「⏳ 候 PI 给……」；`status` 载「field_pending_PI」 | 已随之改（见 v3 之 `v3_change_face.face_1`） |

⚠ **随变子键之理由（如实登记）**：若仅改 `field` 而留「候 PI 给」／「field_pending_PI」字样，则 v3 **内部自相矛盾**；且双路取值件 `e5615b993000` **§8 逐字**载：「PI 择毕之后（另棒执行，本棒 ⛔ 0 预行）：回填 v2 之 `field`／`field_status`／`field_note` ＋ 更新 U-1」⇒ 本棒执行之授权面即含此三键 ＋ U-1。

### §3-2 ⛔ 0 触锚值（H-4 之实证）

| 项 | v2 登记值 | 本棒直算复核 | 判 |
| :-- | :-- | :-- | :-: |
| `sha256_12` | `9e09214cf088` | **`9e09214cf088`** | ✅ **逐位相符 · 0 漂移** |
| `bytes` | `18905` | **`18905`** | ✅ **逐位相符 · 0 漂移** |

⇒ `field` 系**表征说明 · ⛔ 非被哈希对象**（H-4）⇒ 其变 ⛔ 0 触承载件 `verifier/kill_lines/GT_kill_line_carrier_v1.md` 之字节流。**本棒对承载件只读，0 开写。**

### §3-3 逐条证据指针

| # | 证据 | 指纹（本棒直算） | 取用面 |
| :-: | :-- | :-: | :-: |
| 1 | **PI 卡** `ask_207b060a5273ab88912e451f` | ——（交互卡 · 交互面） | §1-Q1 |
| 2 | **卡答登记件** v13 | **`693181b9354b`** · 3,661 B | §1-Q1 逐字「C-甲 kills=10 GT（推荐）」＋ 选项 id |
| 3 | **双路取值件** `results/_kill_line_field_value_sourcing_2026_10_15.md` | **`e5615b993000`** · 19,471 B | §4 之 C-甲 候选行 ＋ §5-1 首选 ＋ §8 之回填授权面 |
| 4 | **先例件** `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（**只读参照**） | **`03c6c01f3697`** · 6,680 B | L22–L28 之 `P_A_KILL_LINE.field` 逐字 `kills=10 GT`（本棒直读复核相符） |
| 5 | **承载件** `verifier/kill_lines/GT_kill_line_carrier_v1.md`（**只读**） | **`9e09214cf088`** · 18,905 B | 锚值复核（§3-2） |

---

## §4 变更面之二 · `P_B_ECR_BASELINE` 系结＝**裁丁**

### §4-1 变更逐字

| # | 变更项 | v2（未动·留痕） | v3（新立） |
| :-: | :-- | :-- | :-- |
| 1 | 主面 `role` | `ecr_baseline` | **`value_determining`** |
| 2 | `definition_anchor.role` | **无 role 面** | **`definition`** |
| 3 | `upstream_anchor.role` | **无 role 面** | **`upstream`** |
| 4 | `spec_registration` 面 | **不存在** | **新增**（双 spec 指纹） |
| 5 | `drift_gate_face` 面 | **不存在** | **新增**（门判别面 ＝ `value_determining`） |
| 6 | `binding_adjudication` 面 | **不存在** | **新增**（择据补记 · 闭 KD-16） |
| 7 | 顶层 `path`／`sha256_12`／`bytes` | `results/deposon_v20_gt.json`／`497b9c2d6746`／`3803` | **同 · ⛔ 0 改**（主面维持） |
| 8 | `value`／`field`／`family`／`caliber`／限制面／披露面 | v2 逐字 | **逐字沿录 · ⛔ 0 改** |

### §4-2 三伴随 `role` 面之指纹（全部本棒直算复核相符）

| 面 | `role` | 实体 | SHA-12 | bytes | 口径 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| **主面** | `value_determining` | `results/deposon_v20_gt.json` | `497b9c2d6746` | 3,803 | ⛔ **门判别面** |
| 伴随 1 | `upstream` | `results/deposon_v20_corpus_eval.json` | `ca71aa6858e1` | 631,644 | 复算源 · ⛔ 非门判别面 |
| 伴随 2 | `definition` | `docs/GT_FORMALIZATION_v1.md` **L25** | `aeefb8ef6972` | 19,100 | 定义文 · ⛔ 非门判别面 |
| 伴随 3 | `spec_registration` | P_B spec `423c84de20d5`（15,457 B）＋ P_A spec `bd1caab42b4c`（10,351 B） | 见左 | 见左 | 规格登记 · ⛔ 非门判别面 |

### §4-3 漂移门判别面（**随锚载明**）

- 门规则逐字：**「任何 ≥ 1 锚漂移 → 全 V0 撤回。」** —— 出处 `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` **L32**；同件 **L134** 另载「5 锚漂移 ≥ 1 → 全 V0 撤回」。
- **本棒直读 L32／L134 逐字复核相符（非转述）**。
- **判别面 ＝ `value_determining`**（即 `results/deposon_v20_gt.json`／`497b9c2d6746`／3,803 B）；三伴随面之指纹变动 **⛔ 0 单独触发本门**（惟仍照旧登记以备检出）。
- 依据：PI 裁丁·Q2（登记件 v13 §1-Q2 登记注记逐字载「漂移门判别面＝`value_determining`」）＋ 另议判断件 `99b578a1be2c` §3-丁-反2 之建议。

### §4-4 逐条证据指针

| # | 证据 | 指纹（本棒直算） | 取用面 |
| :-: | :-- | :-- | :-: |
| 1 | **PI 卡** `ask_207b060a5273ab88912e451f` | —— | §1-Q2 |
| 2 | **卡答登记件** v13 | **`693181b9354b`** | §1-Q2 逐字「裁丁（推荐）」＋ **登记注记**（选项全文义 ＋ 漂移门面） |
| 3 | **另议判断件** `results/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md` | **`99b578a1be2c`** · 32,067 B | §3-丁 之丁案 · §3-甲-反1/反2 · §3-丁-反1/反2 · §4-5 变更清单 · §5 之 KD-15～KD-20 |
| 4 | **P_B spec**（门规则之直读源） | **`423c84de20d5`** · 15,457 B | §2 锚表 L24–L30 · L32／L134 门规则 |
| 5 | **P_A spec**（先例系结实体） | **`bd1caab42b4c`** · 10,351 B | 先例 `03c6c01f3697` 之 `P_A_ECR_BASELINE` 所系实体 |
| 6 | **主面** `results/deposon_v20_gt.json` | **`497b9c2d6746`** · 3,803 B | 值 1.3333333333333333（沿 v2，未复核其运行语义） |

---

## §5 新旧并存声明（**以新为准 · 旧件一字未动 · 全部留痕**）

| 版本 | 路径 | SHA-12 | bytes | 本棒态度 |
| :-: | :-- | :-- | :-- | :-- |
| **v1** | `results/_ge01_prereg_5anchor.json` | `4b020eb04605` | 10,701 | ⛔ **0 改 0 移 0 改名 0 删**；其 `unresolved` Q1–Q8 与 `candidates_unadjudicated` 面**原样留痕** |
| **v2** | `results/_ge01_prereg_5anchor_v2.json` | `f06313373fc6` | 21,629 | ⛔ **0 改 0 移 0 改名 0 删**；其 `P_B_KILL_LINE.field` 之「候 PI 给」占位与 `P_B_ECR_BASELINE` 之 `role=ecr_baseline`／无 `spec_registration` 面**原样留痕** |
| **v3（本件所锁）** | `results/_ge01_prereg_5anchor_v3.json` | **`0c269b9558da`** | **35,911** | **以新为准**；⛔ 0 载自身指纹 |

**统一血缘**：v1 → v2 → v3 **并存递进**，每一旧版**原样在册**；v3 之 `supersession` 面逐字载此链（`unified_lineage_policy`）。**本棒 0 删除任何旧版**（⛔ 0 以新代旧）。

---

## §6 KD-15／KD-16／KD-18 之照录面（**逐字照录 · ⛔ 0 回改既有件原文**）

> 照录源：`results/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md`（`99b578a1be2c`）§5 表。**本棒 0 代修 · 0 回改两 spec · 0 回改既有件 KD-2 原文。**

### §6-1 KD-15（**只登记 · ⛔ 0 代修**）

> **KD-15** | **spec 对象栏之节号指针于盘上已断**：`P_A_ECR_BASELINE`（L48）与 `P_B_ECR_BASELINE`（L26）之对象栏皆作「**本文 §3** ECR=1.333 基线」，然 **ECR 于两 spec 之 §3 内各 0 次**（P_A §3 ＝ L56–L85；P_B §3 ＝ L34–L83），全文 2 次皆落于 §1／§2 | **M1/M2**（逐行扫描计数） | 登记不代修（⛔ 0 回改两 spec）；**建议**：若裁 A，载于 v3 之 KD 面并以 `spec_registration` 面标注之

**本棒执行之**：PI 已裁**丁** ⇒ 依 KD-15 之建议，KD-15 **载于 v3 之 `kd` 面**并以 **v3 之 `spec_registration` 面标注之**（该面之 `primary_spec_object_face` 逐字载 P_B spec §2 之对象格「本文 §3 ECR=1.333 基线」与字段格「ecr_median=1.333」）。**本棒直读复核**：P_B spec **L26** 逐字为「本文 §3 ECR=1.333 基线」——**相符**。

### §6-2 KD-16（**本棒经 PI 裁而闭**）

> **KD-16** | **v2 所系实体不在 v1 明列候选之内**：v1 `candidates_unadjudicated` ＝ {`423c84de20d5`（P_B spec 自指读）、`bd1caab42b4c`（P_A spec 之先例值）}；v2 顶层系 `497b9c2d6746`（gt.json），**非该二候选之一** ⇒ 系结之**择据在册面缺环** | **M12**（v1/v2 双件直读） | 登记不代修；**建议**：随 §4-5 项 5 补记择据

**本棒执行之**：PI 2026-10-15 卡 `ask_207b060a5273ab88912e451f` §1-Q2 **裁丁** ＋ v3 新增之 `binding_adjudication` 面（含 `chosen_entity_is_in_v1_candidates: false` 之明示与 `choice_rationale` 之择据补记）⇒ **择据缺环已闭**。**⛔ 0 回改 v1 之 `candidates_unadjudicated` 面**（v1 `4b020eb04605` 原样留痕）。

### §6-3 KD-18（**KD-2 之精确化 · 只登记**）

> **KD-18** | **KD-2 之精确化**：既有表述「20 图口径不可自当前在盘上游复现」**过宽**；实测「**取冻结 20 图子集则可复现**（逐图 20/20 逐位相符、有限 17、中位同值）」；真正不可复现者 ＝ **全 22 之原生口径**，且「取哪 20 图」之子集规则**未被任何实体记录** | **M9/M10**（冻结公式逐字转写复算；0 runner／0 import／0 LLM） | 登记不代修；⛔ **0 回改既有件 KD-2 原文**；建议随 §4-5 项 6 于 v3 并列新表述

**本棒执行之**：KD-18 **并列新表述于 v3 之 `kd` 面**；**⛔ 0 回改既有件 KD-2 原文**，且 **⛔ 0 触 v3 之 `P_B_ECR_BASELINE.deviation_disclosure` 面**（该面**逐字沿 v2**，KD-2 之原文在其中原样在册）。**本棒 0 跑实验**（0 runner／0 import／0 LLM）⇒ 复现性之实测属 M9/M10 之既有在册证据，本棒**未重算、未据以改值**。

---

## §7 其余四面沿 v2 之**逐字节一致证明**

| 锚／面 | 判 | 证法 |
| :-- | :-: | :-- |
| `P_B_FROZEN_RUNS` | ✅ **逐字节一致** | 以 v2／v3 各自解析后按同序列化参数重建字符串比对 ⇒ **IDENTICAL** |
| `P_B_LLM_CLIENT` | ✅ **逐字节一致** | 同上 ⇒ **IDENTICAL** |
| `P_B_DISTORTION_CALC` | ✅ **逐字节一致** | 同上 ⇒ **IDENTICAL** |
| ECR 之 `value`／`value_form`／`field`／`field_note`／`family`／`family_note`／`caliber`／`limitation_face`／`deviation_disclosure`／`caliber_spectrum_note`／`recompute_evidence`／`verbatim_source`／`name`／`path`／`path_windows`／`sha256_12`／`bytes` | ✅ **逐项 IDENTICAL**（17/17） | 逐键规范序列化比对 |
| ECR 之 `definition_anchor`（除新增 `role`）／`upstream_anchor`（除新增 `role`）／`value_anchor`（除 `sha256_12_binding`） | ✅ 逐键 IDENTICAL | 同上 |
| KILL_LINE 之 `sha256_12`／`bytes` | ✅ **SAME**（`9e09214cf088`／18,905） | 直算复核 |
| KILL_LINE 之变更子键 | ⚠ **仅 4 键**：`field`／`field_status`／`field_note`／`status` | 逐键差异集（`diffkeys`）实测 |
| 顶层沿录面 `algorithm`／`created`／`generator`／`path_convention`／`resolved_from_v1`／`spec_ref` | ✅ **逐字节一致** | 逐键规范序列化比对 |

**序列化不扰动之自证**：以 v2 原件作往返检验（`json.loads → json.dumps(indent=2) → ＋尾换行`）得 **roundtrip identical: True**、21,629 B、`f06313373fc6` ⇒ 上列「一致」之比对基准确为**字节面**而非解析面。

---

## §8 0 触动自证

| 项 | 值 |
| :-- | :-- |
| v1 `4b020eb04605` | **未动**（本棒开写 0 次 · 未移动 · 未重命名 · 未删除） |
| v2 `f06313373fc6` | **未动**（本棒**只读**用于逐字沿录与比对） |
| 承载件 `9e09214cf088` | **未动**（只读复核） |
| 草案件 `0f65a42e7a34` | **未动**（未触及） |
| 两 spec `423c84de20d5`／`bd1caab42b4c` | **只读**（本棒直读 L26／L32／L134 之内容，不写入） |
| 登记件 v13 `693181b9354b` | **只读** |
| **触动既有件数** | **0** |
| 移动／重命名／删除 | **0／0／0** |

---

## §9 字节级自报（**被锁件 v3 · 落盘后盘上实测**）

| 项 | 本棒实测 | 要求 | 判 |
| :-- | :-- | :-- | :-: |
| 落盘方式 | Python `io.open(..., encoding='utf-8', newline='\n', errors='strict')` **直写** | ⛔ 0 经 PowerShell 管道中转 | ✅ |
| Windows 路径 | **一律 raw 字符串**（⛔ 0 中转转义） | —— | ✅ |
| SHA-12 | **`0c269b9558da`** | —— | ✅ |
| bytes | **`35911`** | —— | ✅ |
| BOM | **False** | False | ✅ |
| CRLF | **0** | 0 | ✅ |
| CR | **0** | 0 | ✅ |
| TAB | **0** | 0 | ✅ |
| 控制字符（含 0x7F） | **0** | 0 | ✅ |
| U+FFFD（以 `chr(0xFFFD)` 构造探针计） | **0** | 0 | ✅ |
| 落盘前闸 | `Test-Path=False` ＋ glob **0 命中**（`Test-Path` 两目标皆 `False`） | —— | ✅ 已实测 |

---

## §10 key 形态扫描（**R4 · ⛔ 0 明文 key**）

| 项 | 结果 |
| :-- | :-- |
| 扫描对象 | `results/_ge01_prereg_5anchor_v3.json` ＋ **本锁记件** |
| 扫描项（⛔ 0 入正文） | 见 §12 之回执（扫描项字面 ⛔ 0 落入正文） |
| 判 | **CLEAN** |

---

## §11 纪律边界自查（**逐项**）

| 项 | 状态 |
| :-- | :-- |
| ⛔ 0 回改 v1／v2 一字 | ✅ 未动（§8 逐项） |
| ⛔ 0 移动／重命名／删除既有件 | ✅ 未动 |
| ⛔ 0 代 PI 裁 | ✅ 三裁**逐字沿录**卡答登记件 v13 `693181b9354b`（⛔ 0 增 0 减 0 改字面） |
| ⛔ 0 宣告①毕 | ✅ 未宣告 |
| ⛔ 0 宣告项闭／阶段闭 | ✅ 未宣告（`status` 明载「pending／awaiting PI final close-out」） |
| ⛔ 0 回改实验结论本体 | ✅ 未动（ECR 各面沿 v2；⛔ 0 触运行语义） |
| ⛔ 0 跑实验 | ✅ 0 跑（0 runner／0 import／0 LLM） |
| ⛔ 0 读 `.env` | ✅ 未读 |
| ⛔ 0 上传／0 远端写 | ✅ 未写远端 |
| ⛔ 0 经手 key（R4） | ✅ 未读未取未写 |
| ⛔ 0 编造来源 | ✅ 全部指针件本棒直算复核（§3-3／§4-4 之 10 件指纹逐位相符） |
| ⛔ 0 旧版代新 | ✅ 三版并存（§5） |
| 遗留开口项 | **U-2**（`P_B_DISTORTION_CALC.version` 子字段 · Q-2 卡未裁）——**如实登记 · ⛔ 0 自行归结** |

---

## §12 交付回执（**待派工单读取 · 非终判**）

- **本件**（锁记件）之 SHA-12／bytes：⛔ **不自含**（自指悖论）⇒ **盘上实测值见派工回执**。
- **被锁件**（v3 JSON）之 SHA-12／bytes：已载于本件 §1（**`0c269b9558da`**／**35,911 B**）。
- **两处变更各一句**：
  1. `P_B_KILL_LINE.field` 由「候 PI 给」回填为 **`kills=10 GT`**（PI 裁 C-甲 · 卡 `ask_207b060a5273ab88912e451f` §1-Q1）——**⛔ 0 触** `sha256_12`／`bytes`（`9e09214cf088`／18,905 B 直算复核未漂移）。
  2. `P_B_ECR_BASELINE` 之系结按 **裁丁** 落定：主面维持 `results/deposon_v20_gt.json`（`497b9c2d6746`／3,803 B）并标 **`role: value_determining`**，另立 `role` 标注之三伴随面（`upstream`／`definition`／`spec_registration`），**漂移门判别面 ＝ `value_determining`** 随锚载明。

---

**落款**：`evidence-auditor`（证据链审计官）· 2026-10-15｜**件名** `_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md`｜**件性质** 锁记件（锁之外置 · ⛔ 0 自指）｜**被锁件** `results/_ge01_prereg_5anchor_v3.json`／`0c269b9558da`／35,911 B｜**生效时点** ＝ 卡提交时点 ms `1792039740320`｜**授权源** 卡 `ask_207b060a5273ab88912e451f` ＋ 登记件 v13 `693181b9354b`｜**变更面** 仅两处 · 余面逐字沿 v2（3 锚逐字节一致 ＋ ECR 17 面逐项一致）｜**KD 照录** KD-15／KD-16（闭）／KD-18｜⛔ 0 回改 v1／v2 · 0 移动／重命名／删除 · 0 代 PI 裁 · 0 宣告①毕 · 0 宣告项闭 · 0 跑实验 · 0 读 `.env` · 0 经手 key · 0 上传／0 远端写。
