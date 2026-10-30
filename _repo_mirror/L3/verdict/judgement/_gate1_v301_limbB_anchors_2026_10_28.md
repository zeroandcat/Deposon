# 门① `V3-01` 之**肢 B 锚件**落盘登记件 · `P_B_V0_anchors_sha256_12.json`

> 📌 **件性质**：**执行登记件**（落件 ＋ 自证 ＋ 回测）——**非判定件、非裁决件**｜**棒别**：`verifier`（successor 子代理·spec L22 逐字「D1 由 successor 子代理计算」）｜**件日**：2026-10-28
> 📌 **观测时点**：**2026-10-28 12:31:53 – 12:35:26 CST**（逐件 `Get-FileHash -Algorithm SHA256` 复算，SHA-256 前 12 位；⛔ 0 内建 `hash()`；⛔ 0 抄任何在册值）
> 📌 **本件之状态**：**已落盘 · 待 PI／`verdict-keeper` 采认**｜⛔ **不落五终判**·⛔ **不判肢 B 已解**·⛔ **不宣告门①成就**·⛔ **不宣告任何零**
> 📌 **本件所立之范围（构造面）**：`V3-01` 之肢 B 之**锚件**（spec L22 之落位件）之**结构锚**——即 5 锚之**件之存在与指纹**；⛔ 0 外推至肢 C／肢 D／肢 E；⛔ 0 外推至门②③④；⛔ 0 外推至 `V3-01` 之终判。

---

## §0 一句话

**肢 B 之锚件已落盘**：spec L22 指定路径 `verifier/handoff/P_B_V0_anchors_sha256_12.json` 之件**本棒新立**（**23,139 B／`2231c8184f6b`**），内含 spec §2（L24–L30）**五锚之逐锚指纹**——**5/5 锚实体皆在盘**（`P_B_ECR_BASELINE`／`P_B_KILL_LINE`／`P_B_FROZEN_RUNS` 之 5 成员／`P_B_LLM_CLIENT`／`P_B_DISTORTION_CALC`），**以本件为准逐锚复算：14/14 MATCH、0 MISMATCH、0 MISSING**。本版为**结构锚**（只锚存在与指纹，**不含任何理论值**）⇒ **理论侧待肢 C**。⚠ **本件不代 PI 请、不代裁、不宣告任何终判**。

---

## §1 回源之事实（本棒自测 · ⛔ 0 采信派工单所载之值）

### §1-1 spec 原卷（开卷回读）

| 项 | 本棒实测 |
|:--|:--|
| 件 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` |
| bytes ／ SHA-12 | **16,933 ／ `01b3fac02b5e`** |
| mtime | 2026-10-26 22:27:07 |
| 观测时点 | 2026-10-28 12:31:53 +08:00 |

📌 **与派工单所述之现值相符**（派工单载「已由 15,457／`423c84de20d5` 长为 16,933／`01b3fac02b5e`」）——**本棒复测确认**；且在册 5 锚载体 `results/evidence/register/_ge01_prereg_5anchor_v3.json`（35,911／`0c269b9558da`）之 `spec_ref` 面仍载旧值 `423c84de20d5`／15,457 ⇒ **spec 本尊已漂移**（本件以双面标承载，⛔ 0 回改 spec、⛔ 0 回改该载体）。

### §1-2 spec 之三处逐字（位号皆回源）

- **L22**：「D1 由 successor 子代理计算，路径 `verifier/handoff/P_B_V0_anchors_sha256_12.json`」
- **L24–L30**：五锚表（逐字照录于锚件之 `anchor_table_verbatim`）——`P_B_ECR_BASELINE`／`P_B_KILL_LINE`／`P_B_FROZEN_RUNS`／`P_B_LLM_CLIENT`／`P_B_DISTORTION_CALC`
- **L129**：「读 `verifier/handoff/P_B_V0_anchors_sha256_12.json` 验 5 锚」
- **L32／L134**：「任何 ≥ 1 锚漂移 → 全 V0 撤回。」

### §1-3 spec 之内容面实测（⚠ 三处缺陷之实证）

| 检索词 | 于 spec 全文之出现 | 判 |
|:--|:--|:--|
| `ECR` | **2 次**：L10（§1 目标与范围）、L26（§2 锚表之对象格） | **§3（L34–L83）内 0 次** ⇒ 锚表对象栏「本文 §3 ECR=1.333 基线」之**节号指针于盘上已断**（沿在册 KD-15） |
| `1.333` | **1 次**：L26（锚表之 field 格自身） | spec **全文无 `1.3333`／无 `1.3333333333333333`** ⇒ 字面精度止于 3 位小数（沿在册 KD-17） |
| `GT-` | **2 次**：L10（§1「GT-1 到 GT-8C」）、L27（锚表「GT 判死裁定族（10 个）」） | **规模三读并存**（§1 作「GT-1 到 GT-8C」／锚表作「10 个」／在册 `0e796a657868` L126 载规格包 §1.3 行 4 作「GT-1..GT-10」）⇒ **锚②之成员表口径本棒不代择** |

### §1-4 落点目录之 census（落盘前后各一次）

| 目录 | 落盘前 | 落盘后 |
|:--|:--|:--|
| 主仓 `verifier\handoff\` | **3 件**：`KT_ABC1_anchors_sha256_12.json`（6,680／`03c6c01f3697`）／`KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json`（11,318／`6e9cd8cd8e07`）／`P_F_PREDECISION_2026_09_11_V0.1.json`（12,498／`312d635e6259`） | **4 件**（＝ ＋ 本棒新立之锚件） |
| 子仓 `deposon-sub\verifier\handoff\` | **3 件**：`KT_ABC1_..._V3X_P_A_PATCH_2026_09_15.json`（5,049／`da517c115f3c`）／`P_A_V0_anchors_sha256_12.json`（7,796／`c4f029f780d8`）／`P_F_PREDECISION_2026_09_09.json`（3,680／`b41c98bf90cc`） | 3 件（0 触动） |
| 归档区 `〔归档区〕` | **0 件同名**（按名 `P_B_V0_anchors_sha256_12.json` 0 命中；`verifier\runs\` 目录**不存在**） | 同左（0 触动） |

📌 **落盘前置核**：`Test-Path` ＝ **False**（目标件与登记件二者皆 False）⇒ 落盘**未覆盖任何既有件**。

### §1-5 单列登记件之 `B` 肢行（本棒开卷回读）

`results/verdict/judgement/_gate1_v3_01_single_column_register_2026_10_28.md`（**52,391／`97175f1019f6`**·mtime 12:18:32）：

- **L25**（§1-2 表之 B 行）逐字：「**B**｜**锚件** `verifier\handoff\P_B_V0_anchors_sha256_12.json`｜——｜**可**（spec L22 逐字…；L129 逐字…）｜**不在盘** ❌（本棒实测；该目录现仅 3 件…）⇒ **我方可解而未做**」
- **L83**（§2-1 五肢表之 B 行）逐字要点：「**不在盘** ❌（三根按名 0 命中；主仓 3 件／子仓 3 件·逐件指纹见 §1-3）⇒ **我方可解而未做**」｜归属段「**`verifier`**（successor 子代理·spec L22「D1 由 successor 子代理计算」）」｜**可**｜其列：「①`V3-01` 之「工具件到位」面不解；②**单列三要件之②不得为「已尽」**；③肢 E（对位销项）以其为对位标的 ⇒ **肢 E 亦不得出**；④`V3-01` 之判死线悬空态不解」

📌 **本棒之范围与该件一致**：本棒**只做肢 B 之锚件**（不触肢 E 之对位销项——其形制与生效归 `protocol-keeper`；不触肢 C／D 之理论面）。

---

## §2 【AC-1】五锚之逐锚表（**bytes／`sha256_12` 皆本棒自跑**）

### §2-1 五锚主表

| # | 锚名 | 件相对路径（登记面） | bytes | `sha256_12`（自跑） | 在盘否 | 若缺则其因 |
|:-:|:--|:--|--:|:--|:-:|:--|
| 1 | `P_B_ECR_BASELINE` | `results/deposon_v20_gt.json` | **3,803** | **`497b9c2d6746`** | **在盘** ✔（归档区 `_movedout_2026_10_22/doc/document/results___deposon_v20_gt.json`；**主仓该路径 0 命中**） | 不缺 |
| 2 | `P_B_KILL_LINE` | `verifier/kill_lines/GT_kill_line_carrier_v1.md` | **18,905** | **`9e09214cf088`** | **在盘** ✔（**子仓** `deposon-sub/verifier/kill_lines/`；主仓 `verifier\kill_lines\` 仅存 `kt_b1_kill_decision.py`） | 不缺 |
| 3 | `P_B_FROZEN_RUNS` | 5 个 frozen run JSON（逐成员见 §2-2） | 5 件 | 5/5 逐位相符（见 §2-2） | **在盘** ✔（5/5，**皆不在主仓**） | 不缺 |
| 4 | `P_B_LLM_CLIENT` | `tools/llm_client.py` | **8,118** | **`1722500da4aa`** | **在盘** ✔（主仓·**在登记路径**） | 不缺 |
| 5 | `P_B_DISTORTION_CALC` | `tools/distortion_calculator.py` | **50,896** | **`ae7ff6e0bac5`** | **在盘** ✔（主仓·**在登记路径**） | 不缺；**但指纹 ≠ 登记值 `410a12482eef`／40,611 ⇒ 锚漂移（授权·见 §2-4）** |

### §2-2 锚③ `P_B_FROZEN_RUNS` 之 5 成员逐行

| # | 成员件名 | 件相对路径（登记面） | bytes | `sha256_12`（自跑） | 在盘否 | 实际落位（自测） |
|:-:|:--|:--|--:|:--|:-:|:--|
| 1 | `deposon_v20_baselines.json` | `results/deposon_v20_baselines.json` | 16,987 | **`6edb2aec1660`** | ✔ | 归档区 `_movedout_2026_10_22/doc/document/results___deposon_v20_baselines.json` |
| 2 | `deposon_v19_benchmark_fixes.json` | `results/deposon_v19_benchmark_fixes.json` | 409,104 | **`910c4333eead`** | ✔ | 归档区 `_movedout_2026_10_22/readout/run/results___deposon_v19_benchmark_fixes.json` |
| 3 | `deposon_v21_gtformal.json` | `results/deposon_v21_gtformal.json` | 69,204 | **`9d9ae5001c57`** | ✔ | 归档区 `_movedout_2026_10_22/doc/document/results___deposon_v21_gtformal.json` |
| 4 | `deposon_v18_api_supplements.json` | `results/deposon_v18_api_supplements.json` | 80,624 | **`62c1a41e1db8`** | ✔ | 归档区 `results/readout/run/deposon_v18_api_supplements.json` |
| 5 | `deposon_v17_fusion_fix.json` | `results/deposon_v17_fusion_fix.json` | 106,164 | **`af51da229652`** | ✔ | 归档区 `results/readout/run/deposon_v17_fusion_fix.json` |

📌 **本棒之定位法（防「按名在错目录找误报全缺」）**：**先按名扫三根**（主仓 `deposon_v*.json` ＝ **0 件**；子仓 16 件；归档区 37 件），**再以 SHA 全盘反查**（`Get-ChildItem -Recurse -Filter '*.json'` 三根共 **1,246 件** 逐件哈希）⇒ 上述 3 件之**改名落位**（`results___` 前缀）由**哈希面**寻得，非按名推定。**⛔ 0 升格为「全球确无」**；归档区**仅按名与指纹认人，⛔ 0 读其内容**。

### §2-3 锚① 之三伴随面（PI 裁丁所立 · 非系结面）

| `role` | 登记路径 | 登记 `sha256_12` | 本棒实测 `sha256_12` | bytes | 判 | 落位 |
|:--|:--|:--|:--|--:|:--|:--|
| `definition` | `docs/GT_FORMALIZATION_v1.md` | `aeefb8ef6972` | **`aeefb8ef6972`** | 19,100 | **MATCH** | 归档区 `_movedout_2026_10_22/doc/document/docs___GT_FORMALIZATION_v1.md`（主仓 `docs\` 下**无**此名件） |
| `upstream` | `results/deposon_v20_corpus_eval.json` | `ca71aa6858e1` | **`ca71aa6858e1`** | 631,644 | **MATCH** | 归档区 `results/readout/run/` |
| `spec_registration_primary` | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `423c84de20d5` | **`01b3fac02b5e`** | 16,933 | **DRIFT** | 主仓（mtime 2026-10-26 22:27:07 变更） |
| `spec_registration_precedent_bound` | `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `bd1caab42b4c` | **`bd1caab42b4c`** | 10,351 | **MATCH** | **子仓** `deposon-sub/docs/V3X/` |

### §2-4 锚⑤ 之漂移面（双面标）

- **登记值**（在册载体 `_ge01_prereg_5anchor_v3.json`／`0c269b9558da`，2026-10-15）：`410a12482eef`／40,611 B
- **现值**（本棒 2026-10-28 12:31:53 自测，主仓 `tools/distortion_calculator.py`，mtime 2026-10-17 23:55:07）：**`ae7ff6e0bac5`／50,896 B**
- **成因之在册裁向**：**「授权变更（PI 2026-10-17 卡 Q1 授权之 P-2 读侧改造）＋登记面滞后」之双成分**（PI 2026-10-21 v191 Q1 甲档·登记件 `pi_rulings/_pi_card_answers_register_2026_10_21_v191.md`＝7,718／`9e919c976d30`，本棒自测）；且 v191 Q2 丙档＝「**维持 v3／落位件不动·另立漂移登记面**」
- ⇒ 本件**采双面标**（登记值＋现值＋观测时点并列），⛔ **0 径改 v3／落位件**，⛔ **0 以现值充登记值**，⛔ **0 以旧登记值充现值**
- ⚠ **漂移门之触发与否属 PI／`verdict-keeper` 裁面**（spec L32／L134）——本件⛔ **不代裁**、⛔ **不宣告未触发**、⛔ **不宣告已触发**

### §2-5 ⚠ 同名义异指之件二例（验锚须以 SHA 为准）

| 同名件 | 本棒实测 | 与登记实体之关系 |
|:--|:--|:--|
| `〔归档区〕/results/readout/run/deposon_v20_gt.json` | 3,804／`d3377668fcc9`（mtime 2026-09-26 21:23:45） | 与锚①之登记实体**同名义异指**（差 1 B） |
| `〔归档区〕/results/readout/run/deposon_v20_baselines.json` | 14,068／`84ce9b028b0c`（mtime 2026-09-26 21:23:42） | 与锚③第 1 成员**同名义异指**（16,987／`6edb2aec1660`） |

⇒ **验锚流程须以 SHA 而非名名为准**（沿在册 KD-10 之同一原则）。

### §2-6 ⚠ spec L10 之路径陈述与盘面不符

spec L10 载「deposon 仓库 `verifier/runs/` 下 5 个 frozen run」；本棒实测：**三根之 `verifier/runs/` 内 0 个 `deposon_v*` JSON**（主仓仅 `.md`／`.log`／`.txt`／`.jsonl`；子仓 0；归档区**无该目录**）⇒ **5/5 落于 `results/` 实体面**（沿在册 KD-10·**SHA 为身份之记**）。
---

## §3 【AC-2】锚件本体已落

| 项 | 值 |
|:--|:--|
| 绝对路径 | `〔本地路径已脱敏〕` |
| bytes | **23,139** |
| SHA-12 | **`2231c8184f6b`**（全值 `2231c8184f6bd4aad5cb2ca887eb8c58779187d5551a4417f03ee27815a99b21`） |
| 落盘前置核 | `Test-Path` ＝ **False**（落盘前）⇒ 新立，未覆盖任何既有件 |
| 观测时点 | 2026-10-28 12:35:26 +08:00（落盘后复算） |

### §3-1 格式之声明（**自定 · 明书**）

📌 **spec 全文未规定 JSON 格式**（spec 仅给三样：§2 锚表 L20–L32、落位路径 L22、读法 L129）⇒ **本件之 JSON schema 系本棒自定**，自定之依据与体例（**明书于锚件之 `format_provenance` 面**）：

1. **体例底座**：沿**在册** 5 锚载体 `results/evidence/register/_ge01_prereg_5anchor_v3.json`（35,911／`0c269b9558da`）之字段集——`name`／`object`／`path`／`algorithm`／`field`／`sha256_12`／`bytes`／`path_windows`／`role`／`status`；多成员锚采**甲案**（`members[]` 逐成员 ＋ 无标量 `sha256_12` 面）。
2. **本棒所增**：每锚 `registered`（登记面·来源指明）／`measured`（**自测值＋观测时点＋实际落位**）／`match`（MATCH／DRIFT／DRIFT_AUTHORIZED）／`entity_on_disk`／`location_root`／`path_relative_to_root`／`on_disk_path`；顶层 `spec_version`／`generated_by`／`observed_at`／`algorithm`／`anchor_table_verbatim`／`theory_side_boundary`／`unresolved`／`kd`／`scope_limits`。
3. **双面标纪律**：登记值与现值**分面并列**（⛔ 0 以其一充其一）——沿在册 K-FZP-3 与 PI v191 Q2 丙档。
4. **⛔ 0 自指**：锚件内**不载自身指纹**（自指悖论）⇒ 锁之载体＝本件之 SHA-12，**另由本登记件承载**。
5. **正斜杠**：JSON 内路径一律正斜杠（与 spec／在册载体字面一致·跨平台可移植）；另列 `location_root` 以标其所属根。

---

## §4 【AC-3】回测（**以本棒新落之锚件为准**）

**方法**：解析锚件 JSON → 递归遍历其全部 `on_disk_path` 字段 → 逐件重算 SHA-256 前 12 位 → 与锚件内所载 `measured_sha256_12`／`sha256_12` 比对；另单核 `spec_ref` 面。

| 项 | 结果 |
|:--|:--|
| 回测面总数 | **14**（5 锚主面 ＋ 4 伴随面 ＋ 5 frozen-run 成员 + `spec_ref`） |
| **MATCH** | **14** |
| **MISMATCH** | **0** |
| **MISSING** | **0** |

📌 **逐面明细**（锚件自载值 → 本次回测实测）：

| 面 | 锚件所载 | 回测实测 | bytes | 判 |
|:--|:--|:--|--:|:--|
| `P_B_ECR_BASELINE/measured` | `497b9c2d6746` | `497b9c2d6746` | 3,803 | **MATCH** |
| `P_B_ECR_BASELINE/companion_faces[definition]` | `aeefb8ef6972` | `aeefb8ef6972` | 19,100 | **MATCH** |
| `P_B_ECR_BASELINE/companion_faces[upstream]` | `ca71aa6858e1` | `ca71aa6858e1` | 631,644 | **MATCH** |
| `P_B_ECR_BASELINE/companion_faces[spec_registration_primary]` | `01b3fac02b5e` | `01b3fac02b5e` | 16,933 | **MATCH**（其**登记值** `423c84de20d5` 之漂移已另记，非回测失败） |
| `P_B_ECR_BASELINE/companion_faces[spec_registration_precedent_bound]` | `bd1caab42b4c` | `bd1caab42b4c` | 10,351 | **MATCH** |
| `P_B_KILL_LINE/measured` | `9e09214cf088` | `9e09214cf088` | 18,905 | **MATCH** |
| `P_B_FROZEN_RUNS/members[0]` | `6edb2aec1660` | `6edb2aec1660` | 16,987 | **MATCH** |
| `P_B_FROZEN_RUNS/members[1]` | `910c4333eead` | `910c4333eead` | 409,104 | **MATCH** |
| `P_B_FROZEN_RUNS/members[2]` | `9d9ae5001c57` | `9d9ae5001c57` | 69,204 | **MATCH** |
| `P_B_FROZEN_RUNS/members[3]` | `62c1a41e1db8` | `62c1a41e1db8` | 80,624 | **MATCH** |
| `P_B_FROZEN_RUNS/members[4]` | `af51da229652` | `af51da229652` | 106,164 | **MATCH** |
| `P_B_LLM_CLIENT/measured` | `1722500da4aa` | `1722500da4aa` | 8,118 | **MATCH** |
| `P_B_DISTORTION_CALC/measured` | `ae7ff6e0bac5` | `ae7ff6e0bac5` | 50,896 | **MATCH**（**其登记值 `410a12482eef` 之漂移已另记**，见 §2-4） |
| `spec_ref` | `01b3fac02b5e` | `01b3fac02b5e` | 16,933 | **MATCH** |

⇒ **「照锚件可验」成立**（spec L129 之读法可施于本件）。

---

## §5 【AC-4】结构锚 ／ 理论侧之界

📌 **本版为「结构锚（structural anchor）」版**：**只锚件之存在与指纹**。

| 项 | 本件之内？ | 说明 |
|:--|:--:|:--|
| 5 锚之件之路径／bytes／`sha256_12`／观测时点 | ✅ 在 | 本件之全部内容 |
| 锚①之值（ECR 中位读数之数值） | ❌ 不在 | 仅存 `field` 指针字符串 `GT4_price_of_anarchy.verdict.median_poa`；**数值不载** |
| `u*(a_t)` 之值与公式 | ❌ 不在 | **理论侧待肢 C** |
| `L(M,T)`／`U(M,T)` 之值与公式 | ❌ 不在 | **理论侧待肢 C** |
| `max_u` 之值与口径 | ❌ 不在 | 待肢 D 之给值 |
| 任何五终判（pass／af／kd／fail／give-up） | ❌ 不在 | ⛔ 判在 PI／`verdict-keeper` |
| 任何宣告（门①成就／肢 B 已解／任何零） | ❌ 不在 | ⛔ 宣告权归 PI |

📌 **关于「须 PI 一言」之面**：单列登记件 L84／L86 载「肢 B 之**理论侧定义位**可能须等理论（肢 C）⇒ 或先落『不含理论值之结构锚』，**须 PI 一言**」。本棒**⛔ 0 代 PI 请、⛔ 0 代裁**——故**先落结构锚版**并于锚件之 `theory_side_boundary` 面**明书**：「此为结构锚之版，其理论侧待肢 C」。**PI 一言之面候 PI**（属结构锚版之采认，非本棒可自闭）。

---

## §6 【AC-5】自证

### §6-1 锚件之字节读数（`python -P .tmp\_bcheck.py` 实测 · 如实照录）

| 项 | 补末行 LF 前 | **补末行 LF 后（终态）** |
|:--|:--|:--|
| BYTES | 23,138 | **23,139** |
| SHA12 | `52e96af67366` | **`2231c8184f6b`** |
| BOM | 0 | **0** |
| CR | 0 | **0** |
| VT | 0 | **0** |
| FFFD | 0 | **0** |
| LAST_BYTE | `0x7d`（`}`） | **`0x0a`** |
| NON_ASCII | 6,142 | 6,142 |
| LF | 357 | 358 |

📌 **如实交代**：锚件初写时末字节为 `0x7d`（JSON 收尾花括号）。依 AGENTS.md §5 之字节规（「UTF-8 无 BOM／纯 LF／**末字节 `0x0a`**…新写之文常缺末换行，**须补**」），本棒**仅追加一个末行 LF**（**未改任何内容字节**，追加前后 JSON 均可 `ConvertFrom-Json` 解析、锚值与回测结论均不变）⇒ 终态字节读数如上表右栏。**两态指纹并列登记，⛔ 0 隐去补前之值**。

### §6-2 触动既有件数 ＝ **0**（除新立之二件）

| 动作面 | 件数 |
|:--|:--|
| **新立**（本棒） | **2**＝锚件（`verifier\handoff\P_B_V0_anchors_sha256_12.json`）＋ 本登记件（`results\verdict\judgement\_gate1_v301_limbB_anchors_2026_10_28.md`） |
| **改动／移动／重命名／删除既有件** | **0** |
| **触动件数合计** | **0**（除上列 2 件新立） |

📌 **落盘前后逐件指纹复核**（同值者即未触动）：

| 件 | 落盘前 | 落盘后 |
|:--|:--|:--|
| `verifier\handoff\KT_ABC1_anchors_sha256_12.json` | 6,680／`03c6c01f3697` | 6,680／`03c6c01f3697` ✔ |
| `verifier\handoff\KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json` | 11,318／`6e9cd8cd8e07` | 11,318／`6e9cd8cd8e07` ✔ |
| `verifier\handoff\P_F_PREDECISION_2026_09_11_V0.1.json` | 12,498／`312d635e6259` | 12,498／`312d635e6259` ✔ |
| `docs\V3X\P_B_DISTORTION_BOUND_V0_SPEC.md` | 16,933／`01b3fac02b5e` | 16,933／`01b3fac02b5e` ✔ |
| `tools\llm_client.py` | 8,118／`1722500da4aa` | 8,118／`1722500da4aa` ✔ |
| `tools\distortion_calculator.py` | 50,896／`ae7ff6e0bac5` | 50,896／`ae7ff6e0bac5` ✔ |
| `results\evidence\register\_ge01_prereg_5anchor_v3.json` | 35,911／`0c269b9558da` | 35,911／`0c269b9558da` ✔ |
| `results\verdict\judgement\_gate1_v3_01_single_column_register_2026_10_28.md` | 52,391／`97175f1019f6` | 52,391／`97175f1019f6` ✔ |

### §6-3 引证清单（**每一指纹皆本棒自测** · 附观测时点）

| # | 件 | bytes | SHA-12（自测） | 观测时点 | 用途 |
|:-:|:--|--:|:--|:--|:--|
| 1 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | 16,933 | `01b3fac02b5e` | 12:31:53 | 5 锚之定义源（§2 L24–L30）／落位路径 L22／读法 L129／漂移条 L32 |
| 2 | `results/evidence/register/_ge01_prereg_5anchor_v3.json` | 35,911 | `0c269b9558da` | 12:35:26 | **在册 5 锚载体**（PI 已裁之登记值来源） |
| 3 | `results/evidence/register/ge01_prereg_5anchor_landing_v1.json` | 50,650 | `5518346a5e61` | 12:35:26 | 5 锚落位记录件（其 U-3 明载本棒所补之路径仍 0 在盘） |
| 4 | `results/verdict/judgement/_gate1_v3_01_single_column_register_2026_10_28.md` | 52,391 | `97175f1019f6` | 12:35:26 | 单列登记件（L25／L83 之 B 肢行） |
| 5 | `results/verdict/judgement/_kd13_ecr_anchor_binding_deliberation_2026_10_15.md` | 32,067 | `99b578a1be2c` | 12:35:26 | 锚①系结之四案判断件 |
| 6 | `results/evidence/register/_ge01_5anchor_json_draft_2026_10_14.md` | 33,387 | `9898a19d9a1d` | 12:35:26 | 5 锚草案（体例先例·`423c84de20d5` 时点之 5 值表） |
| 7 | `results/evidence/register/_gt_kill_line_carrier_effect_register_2026_10_15.md` | 25,941 | `e40f060fa3a3` | 12:35:26 | 锚②载体之生效登记件 |
| 8 | `results/evidence/register/_ge01_prereg_5anchor_v2_lock_register_2026_10_15.md` | 17,808 | `ed3b544d33a6` | 12:35:26 | v2 锁记件 |
| 9 | `pi_rulings/_pi_card_answers_register_2026_10_21_v191.md` | 7,718 | `9e919c976d30` | 12:35:26 | 锚⑤漂移之在册裁向（v191 Q1 甲档／Q2 丙档） |
| 10 | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | 6,680 | `03c6c01f3697` | 12:35:26 | KT-A1 先例锚载体（只读·体例先例） |
| 11 | `deposon-sub/verifier/handoff/P_A_V0_anchors_sha256_12.json` | 7,796 | `c4f029f780d8` | 12:35:26 | P-A 锚载体（锚① definition 面之出处·只读） |
| 12 | `tools/llm_client.py` | 8,118 | `1722500da4aa` | 12:31:53 | 锚④之实体 |
| 13 | `tools/distortion_calculator.py` | 50,896 | `ae7ff6e0bac5` | 12:31:53 | 锚⑤之实体（现值面） |
| 14 | `verifier/handoff/P_B_V0_anchors_sha256_12.json` | **23,139** | **`2231c8184f6b`** | 12:35:26 | **本棒新立之锚件** |

---

## §7 本件之限

1. **本件只做「锚件存在与指纹」，不做判定**：⛔ 未落任何五终判（`pass`／`af`／`kd`／`fail`／`give-up`）；⛔ 未判肢 B 已解；⛔ 未宣告门①成就；⛔ 未宣告任何零。**判归 PI／`verdict-keeper`。**
2. **理论侧不在本件**：锚①之数值、`u*(a_t)`、`L`／`U`、`max_u` 皆不在本件内 ⇒ **理论侧待肢 C**；本件**不代 PI 请**那一句。
3. **锚⑤之漂移未被本件「消解」，仅被双面标**：现值 `ae7ff6e0bac5` 与登记值 `410a12482eef` 之**登记面滞后**仍在册；**漂移门（spec L32／L134）之触发与否本件不裁**。
4. **锚②之成员表口径未裁**：spec §1 作「GT-1 到 GT-8C」／§2 锚表作「10 个」／在册规格包作「GT-1..GT-10」——**三读并存**；本件采**在册已裁之 `field` 值 `kills=10 GT`**（PI 2026-10-15 Q1 C-甲）并**以载体指纹为准**，**⛔ 0 自拟成员表**、⛔ 0 以理论侧成员表充之。
5. **四锚实体不在主仓**：5 锚之系结实体中 **3 锚**（①、②、③）之实体落于**归档区／子仓**，**2 锚**（④、⑤）在主仓 ⇒ **以主仓为根之「读该件验 5 锚」流程将 0 命中 3 锚**（本件以 `on_disk_path` ＋ `location_root` 载明实落位，方可复验）。**本棒未复制任何件入主仓**（复制＝新增件·须 PI 逐单令）。
6. **阴性结论之射程**：本棒之「0 命中」皆带**射程**（指定根／指定文件名／指定扩展名）＋**正控**（如：按名 0 命中 `deposon_v20_gt.json` 于主仓，但按 SHA 全盘反查**命中**归档区 1 件 ⇒ 扫描行非恒真）；⛔ **0 升格为「全球确无」**。
7. **归档区之读取限制**：归档区**仅按名与指纹认人**，⛔ **0 读其文件内容**；本棒对归档区只做了**文件枚举与 SHA-256 复算**（只读）。
8. **本棒未跑任何实验**：0 runner／0 experiment import／0 LLM 调用／0 网络动作；一切算式系**纯读＋纯哈希**。⛔ 0 读 `.env`／0 读 key／0 触 `〔本地路径已脱敏〕`。
9. **本棒未代 PI 裁**：结构锚版之采认、理论侧之界、`U-1`–`U-5` 诸开口面，**皆候 PI**（锚件之 `unresolved`／`kd` 面已逐条登记）。

---

## §8 末行自证

**我落盘了：`〔本地路径已脱敏〕`**（锚件·23,139 B／`2231c8184f6b`）**与 `〔幽灵引用·未上传:_gate1_v301_limbB_anchors_2026_10_28.md〕`**（本登记件）。
**我落盘了：`〔本地路径已脱敏〕`** —— `Test-Path` ＝ **True**｜`Get-Item` 实测：`Length` ＝ **23139**｜`LastWriteTime` ＝ **2026-10-28 12:34:53**｜**SHA-12 ＝ `2231c8184f6b`**｜观测时点 2026-10-28 12:35:26 +08:00。（本登记件自身之指纹**不在件内自载**——自指悖论；其 bytes／SHA-12 由回报正文载明。）
