# 5 锚 v2 回填 · 锁记件（2026-10-15）

> 📌 **一句话结论**：PI 于卡 `ask_a0046eb056a849d802da0377` Q2 逐字裁「**授权另立v2·一次回填五面（推荐）**」⇒ 另立 `results/_ge01_prereg_5anchor_v2.json`（SHA-12 `f06313373fc6`／21,629 B），**五面全填**；**锁之载体 ＝ prereg 件之 SHA-12**，因自指悖论（prereg 内 ⛔ 0 写自身指纹）故**另立本件登记**；生效时刻 ＝ **卡提交时点 ms `1792033268243`**（PI 核准回执之时点 · 非棒自签）；既有 v1 `results/_ge01_prereg_5anchor.json`（`4b020eb04605`／10,701 B）**一字未动**——新旧并存以新为准、旧件留痕。

| 项 | 值 |
| :-- | :-- |
| **件名** | `results/_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md` |
| **件性质** | **锁记件**（§3-4 之锁载体：⛔ 0 自指 ⇒ 锁之外置）· ⛔ 0 代 PI 裁 · ⛔ 0 回改任何既有件 |
| **登记方** | `evidence-auditor`（deposon 证据链审计官） |
| **锁之载体** | **v2 prereg JSON 之 SHA-12 ＝ `f06313373fc6`**（本件 §2 载其全量指纹面） |
| **所锁件** | `results/_ge01_prereg_5anchor_v2.json`／SHA-12 `f06313373fc6`／**21,629 B** |
| **核准源** | 卡 `ask_a0046eb056a849d802da0377`（schemaVersion 2 · mode questionnaire）· Q2 · 选项 id `q2_4288761e_opt1` |
| **卡提交时点** | ms `1792033268243`（＝ 2026-10-15 11:01:08 CST）＝ **生效时刻** |
| **登记件** | `results/_pi_card_answers_register_2026_10_15_v12.md`／SHA-12 `97111fee4410`／6,081 B／**§1-Q2** |

> ⚠ **本件 0 做**：⛔ **0 回改**任何既有件一字（含 v1 锚 JSON `4b020eb04605`、锚载体 `c4f029f780d8`、KT-A1 活载体 `03c6c01f3697`）｜⛔ **0 移动／0 重命名／0 删除**任何既有件｜⛔ **0 代 PI 裁／释／择／确认／给值**（凡 PI 未裁者一律 §6 列候复核面）｜⛔ **0 宣告** `G-E01` 开跑就绪、⛔ **0 宣告**任何项之闭、⛔ **0 宣告**①毕｜⛔ **0 联网** · ⛔ **0 读** `.env` · ⛔ **0 经手**任何 key（R4：key 永不明文）｜⛔ **0 上传／0 远端写**｜⛔ **0 跑实验**。

---

## §1 授权面（逐字 · 可引证据）

- **PI 逐字答**：「**授权另立v2·一次回填五面（推荐）**」（选项 id `q2_4288761e_opt1`）。
- **登记件**：`results/_pi_card_answers_register_2026_10_15_v12.md`／SHA-12 `97111fee4410`／§1-Q2（本棒落盘前实测正身，非沿用）。
- **生效时刻**：**卡提交时点 ms `1792033268243`**——依 v12 §1-Q2 题面逐字「生效时刻＝PI 核准回执之时点（**非棒自签**）」。本棒 ⛔ 0 自设时点、⛔ 0 以落盘时点充生效时点。
- **回填范围**：五面**一次回填**（`P_B_ECR_BASELINE`／`P_B_KILL_LINE`／`P_B_FROZEN_RUNS`／`P_B_LLM_CLIENT`／`P_B_DISTORTION_CALC`），⛔ 0 部分回填、⛔ 0 留空壳。

---

## §2 锁之载体（v2 prereg JSON 指纹面 · 本棒直算）

| 项 | 值 |
| :-- | :-- |
| **所锁件路径** | `results/_ge01_prereg_5anchor_v2.json` |
| **SHA-12（本棒直算）** | **`f06313373fc6`** |
| **bytes** | **21,629** |
| **SHA-256 全量** | `f06313373fc63836d71eca2d87e9df683b2fa96f62efff4199e244bc3d5a3560` |
| **算法口径** | `hashlib.sha256(file bytes).hexdigest()[:12]`（stdlib；⛔ 0 用内建 `hash()`） |
| **独立通道复算** | ✅ 相符——PowerShell `Get-FileHash -Algorithm SHA256`（Windows crypto API，与 Python hashlib 非同一实现面）得同值 |
| **落盘前占用检查** | `Test-Path` ＝ **False**；glob `**/_ge01_prereg_5anchor_v2*` **0 命中**、`**/*5anchor_v2_lock*` **0 命中**（实测）⇒ 未占用，⛔ **0 覆盖**、⛔ **0 加 `_r1`** |

> 📌 **自指悖论之处置**：prereg JSON 内 ⛔ **0 写自身指纹**（自证循环）；故锁之外置于本件——**锁之载体 ＝ prereg 件之 SHA-12 `f06313373fc6`**，须以本件为锁之登记面方可验证（沿草案 `9898a19d9a1d` §3-4 之纪律，亦沿 GT 承载件「⛔ 0 自写入正式件自身」之同族纪律）。

---

## §3 五面回填 · 逐条证据指针

### 3-1 `P_B_ECR_BASELINE`（P-甲锚）

| 项 | 值 |
| :-- | :-- |
| **value** | `1.3333333333333333`（IEEE-754 double · 与冻结读数逐位相同） |
| **field** | `GT4_price_of_anarchy.verdict.median_poa`（⛔ **0 写 `ecr_median`**——该字面为禁用字面） |
| **family** | GT-4 分布级（甲族） |
| **系结实体** | `results/deposon_v20_gt.json`／`497b9c2d6746`／3,803 B（本棒直算） |
| **caliber 三事** | `denominator_arms`＝{{random, degree}}｜`graph_scope`＝冻结读数 20 图之 17 有限｜`infinity_rule`＝不入中位·单独计数 |
| **限制面** | 照录锚载体 `limitation_face`（worst-case 无邻接放置／乙族未锚／命名／H_A_dead 与 GT-4 判词之张力未和解） |
| **KD 披露** | 照录锚载体 `deviation_disclosure`：**KD-6**（分母退化偏倚·偏大）、**KD-5**（中位非连续·勿外推）、**KD-2**（20 图口径不可自当前在盘上游复现） |
| **定义段指针** | `docs/GT_FORMALIZATION_v1.md`／`aeefb8ef6972`／**L25**（本棒直算正身） |
| **复算** | 纯读纯算·0 runner·0 LLM；JSON 指针实测读值 `1.3333333333333333` ＝ 锚值（**相等为真**） |
| **证据指针** | 卡 `ask_a0046eb056a849d802da0377` ＋ 登记件 `97111fee4410` §1-Q2 ＋ 锚载体 `c4f029f780d8` |

### 3-2 `P_B_KILL_LINE`（GT 正式承载件）

| 项 | 值 |
| :-- | :-- |
| **path** | `verifier/kill_lines/GT_kill_line_carrier_v1.md` |
| **sha256_12 ／ bytes** | `9e09214cf088` ／ **18,905**（本棒直算；与迁移登记件所载正式锚值相符） |
| **field** | **「候 PI 给」**——Q-7 沿用占位·缺口 G-4·沿 H-4（field ＝ 表征说明·⛔ 非被哈希对象）；⛔ **0 自拟正式值**（沿迁移登记件 §7 **R-1**） |
| **载体系状态** | 正式·已核准·已生效（PI 卡 Q1 逐字「全部按棒之倾向档打包核准（推荐）」） |
| **草案态** | v0 `0f65a42e7a34`／16,486 B **保留并列**；其指纹 **⛔ 0 充当正式锚值** |
| **十成员终判分布** | `pass` 4／`fail` 1〔GT-5〕／`kd` 5／`af` 0／`give-up` 0／挂账 0 |
| **证据指针** | 卡 `ask_a0046eb056a849d802da0377` §1-Q1 ＋ 登记件 `97111fee4410` ＋ 迁移登记件 `e40f060fa3a3` §2／§3／§7 R-1 |

> ⚠ **本面之 `status` 系本棒依其授权面自定**（迁移登记件 §6 载「`status` 候该棒依其授权面自定（⛔ 本棒 0 代定）」）——本棒定为 `carrier_anchored_effective; field_pending_PI`，**如实反映「载体系已锚·field 候 PI 给」之两面**，⛔ 0 代 PI 裁 `field` 之值。

### 3-3 `P_B_FROZEN_RUNS`（甲案 · 多成员）

| # | path | SHA-12 | bytes |
| :-: | :-- | :-- | --: |
| 1 | `results/deposon_v20_baselines.json` | `6edb2aec1660` | 16,987 |
| 2 | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | 409,104 |
| 3 | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | 69,204 |
| 4 | `results/deposon_v18_api_supplements.json` | `62c1a41e1db8` | 80,624 |
| 5 | `results/deposon_v17_fusion_fix.json` | `af51da229652` | 106,164 |

- **value** ＝ **5 元数组**（上述 SHA-12，依 PI 裁之次序）；**field** ＝ `runs=5 frozen`。
- **⛔ 0 以松散表达式充路径**：逐成员给**独立 path 项**，另列 `path_windows`（先例 `03c6c01f3697` 之 `P_A_FROZEN_RUNS` 用 `v20 + v19 + ...` 之松散式，本棒 ⛔ 不承之）。
- **⛔ 甲案无 bytes 标量面**：锚级 `bytes` ＝ null，各成员 bytes 见上表（沿先例形态）。
- **三方相符**：本棒直算 ＝ v1 `members_measured` ＝ KT-A1 先例 `03c6c01f3697` 之数组——**5/5 逐位相符，0 例外**。
- **路径口径复测**：spec L10 载 `verifier/runs/`；本棒实测该目录 **0/5** 命中 `deposon_v*` JSON（仅 `.txt`/`.log`/`.jsonl`/`.md`），**5/5 在 `results/`** ⇒ SHA 为身份之记（沿 v1 KD-10）。
- **诚实交代**：`results/` 下另存其他 `deposon_v*.json`（v15/v16/v17 旁支、v20 GT 各子件、v22 等）；「5 元」系 **PI 裁定之 frozen-run 成员集**之计数，⛔ **非**「盘上仅存 5 个 run JSON」之陈述。
- **证据指针** | 卡 `ask_a0046eb056a849d802da0377` ＋ 登记件 `97111fee4410` §1-Q2 ＋ 先例 `03c6c01f3697`（只读参照·0 字节改动）。

### 3-4 `P_B_LLM_CLIENT`

| 项 | 值 |
| :-- | :-- |
| **path** | `tools/llm_client.py` |
| **sha256_12 ／ bytes** | `1722500da4aa` ／ **8,118**（本棒直算） |
| **canonical 之权威** | MQ-20 **项12** 勘误册 `results/_mq20_errata_register_2026_10_14.md`／`8bb4bbc28c16`／§4——PI 明示「两锚 canonical 值 ＝ 实测值」 |
| **取代之登记值** | `055e874ea5c1`（KT-A1 活载体 `03c6c01f3697` **至今仍载旧值**，⛔ **0 改其一字** ⇒ 并列关系照旧在册） |
| **证据指针** | 卡 `ask_a0046eb056a849d802da0377` ＋ 登记件 `97111fee4410` §1-Q2 ＋ 勘误册 `8bb4bbc28c16` §4 项12（PI 卡 `ask_f1bdf8de1358da35139bc51f`） |

> ⚠ **锚族辨析（KD-14）**：MQ-20 项12 之 canonical 系 **`P_A_LLM_CLIENT`（KT-A1 族）** 之面；本面为 `P_B_LLM_CLIENT`（P_B 族），**两者所系为同一文件实体**（`tools/llm_client.py`），故沿同一实测值——此为**实体同一性之转录**，⛔ 非跨族代裁。

### 3-5 `P_B_DISTORTION_CALC`

| 项 | 值 |
| :-- | :-- |
| **path** | `tools/distortion_calculator.py` |
| **sha256_12 ／ bytes** | `410a12482eef` ／ **40,611**（本棒直算） |
| **status** | `unfrozen_pending_PI`（PI 明定） |
| **superseded_value** | `"absent"`（首次实体化·PI 明定；⛔ **非**漂移） |
| **version** | `2026-09-11`——⛔ Q-2 卡**未裁**此子字段；此处逐字沿 P_B spec L30 之字面，本棒 ⛔ 0 以文件内容复核（另见 §6 U-2） |
| **证据指针** | 卡 `ask_a0046eb056a849d802da0377` ＋ 登记件 `97111fee4410` §1-Q2 ＋ 重建登记件 `_ge01_calculator_rebuild_register_2026_10_14.md`（S6 记录·逐位相符） |

---

## §4 路径面（跨平台口径）

- **JSON 内统一正斜杠 `/`**（与 spec／先例字面一致·跨平台）——⛔ 0 混入反斜杠致转义歧义（`\r`／`\t` 陷阱已避开：本棒全部 Windows 路径于写盘脚本内均以 raw string 承载）。
- **每锚另列 `path_windows`**（反斜杠面）供 Windows 侧直接取值。
- **逐成员亦然**：`P_B_FROZEN_RUNS` 之 5 名成员各带 `path`（正斜杠）＋ `path_windows`（反斜杠）。

---

## §5 新旧并存声明（以新为准 · 旧件留痕）

| 项 | 值 |
| :-- | :-- |
| **新件（本次交付）** | `results/_ge01_prereg_5anchor_v2.json`／`f06313373fc6`／21,629 B |
| **旧件（v1）** | `results/_ge01_prereg_5anchor.json`／`4b020eb04605`／10,701 B |
| **旧件状态** | **一字未动**（⛔ 0 回改 · 0 移动 · 0 重命名 · 0 删除）；其 `unresolved`／`kd` 面**原样留痕** |
| **并存规则** | **新旧并存以新为准**——锚值之效力面以 v2 为记；v1 作为**前态留痕**继续在册，⛔ 0 删 |
| **v1 触动数** | **0**（本棒落盘后复测 v1 指纹 ＝ `4b020eb04605`／10,701 B，与授权面前实测同值） |

> 📌 **归位与触动面**：本棒**写入面 ＝ 2 件新建**（v2 JSON ＋ 本锁记件）；**既有件触动数 ＝ 0**。
> 📌 **辅助件之处置**：本棒所用辅助脚本一律落于 `.tmp/`（⛔ 0 留 `results/`）。

---

## §6 候复核面（⛔ 0 视为已闭 · ⛔ 0 代 PI 裁）

| # | 候复核项 | 现状 | 何径可得 |
| :-: | :-- | :-- | :-- |
| **U-1** | **`P_B_KILL_LINE` 之 `field` 正式值**（Q-7 沿用占位·缺口 G-4） | 正式件 §6 G-4 载「登记面之 `field` 值 **候 PI 给**」**未改**；沿 H-4（`field` ＝ 表征说明·⛔ 非被哈希对象） | **PI 给值**；或 PI 明示「沿用占位」之具体字面（迁移登记件 `e40f060fa3a3` §7 **R-1**） |
| **U-2** | **`P_B_DISTORTION_CALC` 之 `version` 子字段** | Q-2 卡**未裁**此子字段；本棒逐字沿 spec L30 字面且 ⛔ 0 以文件内容复核 | **PI 给值**；或明示「维持 spec 字面」／「以文件内容为准」 |
| **KD-13** | **`P_B_ECR_BASELINE` 系结实体是否改系** | 本棒所系 ＝ P-甲锚载体**自指定**之 `value_anchor`（`results/deposon_v20_gt.json`），属**转录**⛔ 非本棒自择 | 若 PI 意在系于他实体（如 spec 本体或上游 `deposon_v20_corpus_eval.json`），**须另行裁面** |
| **KD-2** | **20 图口径不可自当前在盘上游复现** | 已随锚披露（照录 `deviation_disclosure`）；⛔ 0 因回填而消解 | 另棒／上游实体定版后自解 |
| **R-2/R-3** | **GT-2／GT-3／GT-7 解封 · GT-9／GT-10 归宿** | 正式件 §5-5 解封条件**未改**；GT-9／10 落 `kd` 在册 | 拆读载体＋PI 给 kill-line 字面；或 PI 裁改落他档（`af` 须先给实体规则） |

> 📌 本件 ⛔ **0 宣告** `G-E01` 开跑就绪、⛔ **0 宣告**任何项之闭、⛔ **0 宣告**①毕——开跑核验属另棒（v12 §2-D：Q9 门槛式·前置齐全即可开跑）。

---

## §7 缺陷登记（本棒新发现 · 只登记不代修）

| # | 缺陷 | 证据 | 处置 |
| :-: | :-- | :-- | :-- |
| **KD-A** | 锚载体 `c4f029f780d8` 所载 `definition_anchor.line_text` 为盘上 `docs/GT_FORMALIZATION_v1.md` **L25 之消元转写**（以 `；` 代 `;`、略去「**PoA**（`run_v20_gt.py` run_gt4）：」前缀、略去「如实退化」「≤1.05 ⇒ 判死」及尾括注）——语义一致、无矛盾，然标注为 `line_text` 易被读作逐字节引文 | 本棒逐字读 L25 并与载体字段比对 | **登记不代修**（⛔ 0 回改既有件）；v2 JSON 之 `definition_anchor` **双载**（`line_text_carrier_as_registered` ＋ `line_text_on_disk_measured_this_run`），差异显式留痕 |
| **KD-B** | `P_B_LLM_CLIENT` 之 `field` 表征说明逐字沿 KT-A1 先例，本棒 ⛔ 0 以文件内容复核其准确性 | 先例 `03c6c01f3697` L47 | 登记；v2 JSON 内以 `field_note` 标明 |
| **KD-14** | MQ-20 项12 之 canonical 系 `P_A_LLM_CLIENT`（KT-A1 族）之面，本 P_B 面沿同一值之依据为**实体同一性** | 勘误册 `8bb4bbc28c16` §4 | 登记于 v2 之 `canonical_authority.family_note` |
| **KD-10（复测）** | spec L10 载 `verifier/runs/`，实测 0/5 在该目录、5/5 在 `results/` | 本棒 glob 实测 | 沿 v1 KD-10 登记 |

---

## §8 源件核对（本棒直算 · 逐件相符）

| 源件 | 本棒实测 SHA-12 | bytes | 与简报/登记所载 |
| :-- | :-- | --: | :-- |
| `results/_pi_card_answers_register_2026_10_15_v12.md` | `97111fee4410` | 6,081 | ✅ 相符（授权面·正身实测） |
| `verifier/handoff/P_A_V0_anchors_sha256_12.json` | `c4f029f780d8` | 7,796 | ✅ 相符 |
| `results/_gt_kill_line_carrier_effect_register_2026_10_15.md` | `e40f060fa3a3` | 25,941 | ✅ 相符 |
| `results/_ge01_prereg_5anchor.json`（v1） | `4b020eb04605` | 10,701 | ✅ 相符（⛔ 一字未动） |
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（先例·只读） | `03c6c01f3697` | —— | ✅ 只读参照·0 字节改动 |
| `results/_mq20_errata_register_2026_10_14.md` | `8bb4bbc28c16` | 11,441 | ✅ 相符 |
| `verifier/kill_lines/GT_kill_line_carrier_v1.md` | `9e09214cf088` | 18,905 | ✅ 相符（本棒直算） |
| `tools/llm_client.py` | `1722500da4aa` | 8,118 | ✅ 相符（本棒直算） |
| `tools/distortion_calculator.py` | `410a12482eef` | 40,611 | ✅ 相符（本棒直算） |
| `results/deposon_v20_gt.json` | `497b9c2d6746` | 3,803 | ✅ 相符 |
| `docs/GT_FORMALIZATION_v1.md` | `aeefb8ef6972` | 19,100 | ✅ 相符 |
| `results/deposon_v20_corpus_eval.json` | `ca71aa6858e1` | 631,644 | ✅ 相符 |
| 五 frozen run 件 | 见 §3-3 | 见 §3-3 | ✅ 三方相符（直算 ＝ v1 ＝ 先例） |

> 📌 **全部指纹均以 `hashlib.sha256`／`Get-FileHash` 复算对照**；⛔ **0 用内建 `hash()`**（内建 hash 每进程随机化，⛔ 0 可作身份之记）。

---

## §9 纪律注记

1. **锁之外置**：prereg 内 ⛔ **0 写自身指纹**（自指悖论）⇒ 锁之载体 ＝ prereg 件之 SHA-12 `f06313373fc6`，由**本件**登记（沿草案 `9898a19d9a1d` §3-4 之纪律）。
2. **⛔ 0 回改既有件**：v1 锚 JSON（`4b020eb04605`）、锚载体（`c4f029f780d8`）、KT-A1 活载体（`03c6c01f3697`）**皆一字未动**；既有件之缺陷（KD-A 等）**只登记不代修**。
3. **⛔ 0 代 PI 裁**：`field` 正式值（U-1）、`version` 子字段（U-2）、ECR 系结实体改系（KD-13）**一律列候复核面**，⛔ 0 自拟、⛔ 0 择。
4. **⛔ 0 宣告**：本件 0 宣告 `G-E01` 开跑就绪、0 宣告任何项之闭、0 宣告①毕。
5. **R4**：⛔ 0 明文 key；本棒 ⛔ 0 读 `.env`、⛔ 0 经手任何 key。

---

**落款**：`evidence-auditor` · 2026-10-15｜**锁记件形态 · 5 锚 v2 回填之锁载体**｜**生效时刻** ＝ 卡 `ask_a0046eb056a849d802da0377` 提交时点 ms `1792033268243`（PI 核准回执之时点·非棒自签）｜**所锁件** `results/_ge01_prereg_5anchor_v2.json` = **`f06313373fc6`／21,629 B**（独立通道复算相符）｜**五面**：ECR `1.3333333333333333`（field `GT4_price_of_anarchy.verdict.median_poa`·GT-4 分布级）／KILL_LINE `9e09214cf088`／18,905 B（field 候 PI 给）／FROZEN_RUNS 5 元数组／LLM_CLIENT `1722500da4aa`／8,118 B／DISTORTION_CALC `410a12482eef`／40,611 B（status `unfrozen_pending_PI`·superseded `absent`）｜**v1 `4b020eb04605` 一字未动**（新旧并存以新为准）｜⛔ 0 代 PI 裁 · 0 自拟 field · 0 回改既有件 · 0 移动／重命名／删除 · 0 宣告开跑就绪 · 0 宣告闭 · 0 宣告①毕 · 0 跑实验 · 0 联网 · 0 读 `.env` · 0 经手 key · 0 上传／0 远端写。
