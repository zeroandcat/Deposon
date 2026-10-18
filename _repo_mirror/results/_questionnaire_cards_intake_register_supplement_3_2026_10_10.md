# 裁卡原件批量落册（第四批·追补）· questionnaire 原件逐字转录（2026-10-10）

## 文件头注

- **件名**：`results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md`
- **落册日期**：2026-10-10（CST）
- **件系**：第三批登记件 `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md`（SHA-12 `dc43e3cb7610`）之**追补落册（第四批）**；上承第二批 `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md`（SHA-12 `193386b9f23c`）、第一批 `results/_questionnaire_cards_intake_register_2026_10_09.md`（SHA-12 `d917180db36f`）。⛔ 0 编辑／覆写／修改前三批登记件；⛔ 0 重复转录其已收录之卡。
- **编制**：**protocol-keeper**（口径与预登记官 · 分支会话 `mvs_b98831be92624db1af580ccc2e7f66d4`｜署名如实 · **0 冒充 PI／parent／verdict-keeper／verifier／worker**）
- **来源**：运行时库 `〔本机用户目录〕/.minimax/v2/sqlite/runtime-state.sqlite`，表 `questionnaire_requests`。本轮以 `sqlite3.connect("file:...?mode=ro", uri=True)` **只读实测**（0 写入、0 修改、0 建表、0 提交）。
- **窗口口径**：本批应录＝派工指定之 **5 张目标卡**（`ask_2dbc05cc3725c7002935ed01`／`ask_92fd9e0ed5a2d6a64e4be94b`／`ask_906e23019db97965b62a29fa`／`ask_d638adfe6dcf33b095e26c25`／`ask_b56649e37d180c79e1ec47e7`）——**本件非全表扫描之应录全集**，系**指定目标行**之逐字转录（沿「库读取限 `questionnaire_requests` 目标行」之派工纪律）。
  - ⚠ **活库声明**：运行时库为**活库**，本件之读得时点即收录截止时点；**其后再建之卡不属本件应录面**。
- **转录纪律**：**逐字、0 省略、0 解释、0 判读**。题面（`request_json.steps` 之 id／header／question／options／selectionMode／required／allowOther／otherPlaceholder）与答文（`reply_payload` 全文，含 `selectedOther`／`otherText`／`source`）均按库中原文照录；本件**不含**任何分析、结论、裁断或建议。
- **效力声明**：本件**仅转录**。⛔ **0 当「裁录」**；⛔ **0 代替任何既有登记件的裁录效力**。本件不产生、不替代、不撤销任何裁决；一切裁断效力仍以其原登记件／生效件为准。
- **命名合规**：`_主题_日期` 体例；⛔ 0 带 V-阶段前缀（0 `_v3_`／`_v4_`／`_v5_`）。沿既有 `_supplement_` 续编体例（第一批 → `_supplement_` → `_supplement_2_` → 本件 `_supplement_3_`）。
- **版式**：UTF-8 无 BOM · LF（CRLF ＝ 0）｜**R4**：key 永不明文（本棒 0 读 key／0 读 `.env`／0 落盘凭据）｜**0 网络 · 0 skill · 0 LLM · 0 实验**。
- **编制方式**：程序化逐字转录（⛔ 0 人工改写任何字面）。

---

## 0 · 本轮读取基准（provenance）

- 库文件大小（读取时点）：`474656768` bytes
- 库文件 mtime（读取时点，CST）：`2026-10-10 01:11:28.562 +0800`
- 表 `questionnaire_requests` 总行数（全表，本轮实测）：`396`
- 全表 status 分布（全表实测）： `answered`=394 `superseded`=2；
- 抽取口径：`SELECT ... FROM questionnaire_requests WHERE request_id IN (5 个目标 id)`（**指定目标行**，⛔ 0 全表扫描、⛔ 0 LIMIT 截断）。
- 时间换算口径：`created_at`／`answered_at`／`submittedAt`／`createdAt` 均为 **INTEGER epoch 毫秒**，本件统一换算为 **CST（UTC+8）** 呈现，原值同时照录。
- 值形口径：SQL／JSON 空值一律呈为 `NULL`；布尔值一律呈为 JSON 小写字面 `true`／`false`（沿前三批体例）。

---

## 1 · 逐卡转录（指定目标 5 件，按 `created_at` 升序）

### 01 · `ask_2dbc05cc3725c7002935ed01` · 轮23（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮23 · S4 复核链＋D-07 呈裁（4 项：BC 择定复核／D-07 判断件／12-26 处置／复核方式）

**卡级元数据（原文照录）**

```text
request_id                     = ask_2dbc05cc3725c7002935ed01
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮23 · S4 复核链＋D-07 呈裁（4 项：BC 择定复核／D-07 判断件／12-26 处置／复核方式）
presentation.allowBackNavigation  = true
presentation.replaceComposer  = true
presentation.showProgress     = true
requester.agentName           = mavis
requester.runId               = turn_task_delivery_a3c007ec4ada4ba0aa2ac996b38b0f07
requester.sessionId           = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId          = call_00_JudBlIvA7wPj9MjGHEDi2943
request_json.createdAt (epoch ms) = 1791563500740   → 2026-10-10 00:31:40.740 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791563500740
created_at (CST 换算)          = 2026-10-10 00:31:40.740 +0800
answered_at (epoch ms)         = 1791563533949
answered_at (CST 换算)         = 2026-10-10 00:32:13.949 +0800
reply_payload.submittedAt(epoch ms) = 1791563533949   → 2026-10-10 00:32:13.949 +0800
injected_at (epoch ms)         = 1791563542014
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／13 选项，原文照录）**

**题 1／4** — `id` = `bc_review`

- `header`（原文照录）：`S4·B/C 构造择定复核（候呈 1·硬阻断）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4·B/C 构造择定之复核（独立判断件『e2fdb380cd3c』§7 候呈 1）。判断件判：「构造①（自身域 resample）为 K-2 判读面；构造②（全体 held-out resample）保留为敏感性面·并陈不删」。理由：estimand 同一性（合取两支同被估量）＋构造洁净度（② 退化支在 S4 面已激活·期望 3.876 次/1000）＋宽窄方向两面相反故不作择据。须 PI 复核后方生效（生效即锁）；判断件建议：先复核本择定、再给 K-1 等效门柱（次序分明）。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `bc_review_opt1`
  - `label`（逐字原文）：```核准本择定——① 为判读面、② 为敏感性面（推荐）```
  - `description`（逐字原文）：```生效即锁；后续 K-1 门柱施于① 之读数（B 0.1905／C 0.4）。```
- `id` = `bc_review_opt2`
  - `label`（逐字原文）：```改采构造②为判读面```
  - `description`（逐字原文）：```后果：K-2 单侧界落于复合分布，须与 K-2 同批相容而落（§7 出口 2 之配套）。```
- `id` = `bc_review_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `d07_verdict`

- `header`（原文照录）：`D-07 判断件呈裁（T1 温度轴）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 温度轴 D 段判读线之独立判断件（『60bd9ae98640』）已出。结论（推荐路线四）：维持「0 承载」之现状处置——该处置系预登记 §3.1 在 D 段起跑前明文规定的合法处置（非事后默认），故 FTFB 未被违反；并将 D 段读数按「构造域负面事实」升格入账、在 C 段判定面列为构造前提；0 重跑、0 事后给线、0 新设阈值。另揭示一处未调和分歧：主读法（full_reply 全同率 0.0）与替代读法（答案面高度收敛·S5 组内 4 组全同 1.0）结论方向相反。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `d07_verdict_opt1`
  - `label`（逐字原文）：```采信推荐路线四（维持 0 承载＋升格入账为构造前提）（推荐）```
  - `description`（逐字原文）：```D 段读数按「构造域负面事实」存档；C 段判定面列为构造前提；0 重跑。```
- `id` = `d07_verdict_opt2`
  - `label`（逐字原文）：```不采信```
  - `description`（逐字原文）：```所取路线在 Other 说明。```
- `id` = `d07_verdict_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `m08`

- `header`（原文照录）：`12/26 空序列素材面（M-08）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 素材面候呈 4：26 件 held-out 中 12 件（46.2%）判据序列为空 ⇒ A／A′／D 读数构成近半来自「无判据文本」之件（敏感性诊断：仅取 14 件非空者，nw_sim 均值 0.5949——非任何线之读数）。当前影响：A／A′／D 之真证伪判定受阻（0 可标真证伪）。处置候选（责任面：PI／worker 补采／protocol 口径）：
```

`options`（逐字原文，共 4 项）：

- `id` = `m08_opt1`
  - `label`（逐字原文）：```补采素材（先派补采评估棒·0 改现有读数）（推荐）```
  - `description`（逐字原文）：```评估 12 件空序列之根因与可补性；补采属 worker 执行面。```
- `id` = `m08_opt2`
  - `label`（逐字原文）：```登记为「不明」```
  - `description`（逐字原文）：```该面真证伪判定挂「不明」·如实入册。```
- `id` = `m08_opt3`
  - `label`（逐字原文）：```口径调整```
  - `description`（逐字原文）：```另立口径件处理空序列占比（protocol 面）。```
- `id` = `m08_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `bc_scope`

- `header`（原文照录）：`择定复核方式（候呈 3＋5）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
随本择定复核之两项配套（『e2fdb380cd3c』§7 候呈 3／5）：一是分面权限——v3 面先例 J3（『dac19ee9e66b』§4，判①但「待 PI 复核」未确认）与 S4 面本择定：分面分别裁定，抑或统一适用？（分面与否属 estimand 面）；二是先例 J3 建议与本择定同批复核。请裁复核方式：
```

`options`（逐字原文，共 3 项）：

- `id` = `bc_scope_opt1`
  - `label`（逐字原文）：```统一适用两面——本择定一并适用于 v3 面与 S4 面（J3 同批确认）```
  - `description`（逐字原文）：```避免「同向但未确认」长期悬置。```
- `id` = `bc_scope_opt2`
  - `label`（逐字原文）：```分面分别裁定```
  - `description`（逐字原文）：```S4 面按本择定；v3 面 J3 另行处置。```
- `id` = `bc_scope_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_2dbc05cc3725c7002935ed01","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"bc_review","question":"S4·B/C 构造择定之复核（独立判断件『e2fdb380cd3c』§7 候呈 1）。判断件判：「构造①（自身域 resample）为 K-2 判读面；构造②（全体 held-out resample）保留为敏感性面·并陈不删」。理由：estimand 同一性（合取两支同被估量）＋构造洁净度（② 退化支在 S4 面已激活·期望 3.876 次/1000）＋宽窄方向两面相反故不作择据。须 PI 复核后方生效（生效即锁）；判断件建议：先复核本择定、再给 K-1 等效门柱（次序分明）。请裁：","selectionMode":"single","options":[{"id":"bc_review_opt1","label":"核准本择定——① 为判读面、② 为敏感性面（推荐）","description":"生效即锁；后续 K-1 门柱施于① 之读数（B 0.1905／C 0.4）。","recommended":true},{"id":"bc_review_opt2","label":"改采构造②为判读面","description":"后果：K-2 单侧界落于复合分布，须与 K-2 同批相容而落（§7 出口 2 之配套）。"},{"id":"bc_review_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"S4·B/C 构造择定复核（候呈 1·硬阻断）"},{"id":"d07_verdict","question":"T1 温度轴 D 段判读线之独立判断件（『60bd9ae98640』）已出。结论（推荐路线四）：维持「0 承载」之现状处置——该处置系预登记 §3.1 在 D 段起跑前明文规定的合法处置（非事后默认），故 FTFB 未被违反；并将 D 段读数按「构造域负面事实」升格入账、在 C 段判定面列为构造前提；0 重跑、0 事后给线、0 新设阈值。另揭示一处未调和分歧：主读法（full_reply 全同率 0.0）与替代读法（答案面高度收敛·S5 组内 4 组全同 1.0）结论方向相反。请裁：","selectionMode":"single","options":[{"id":"d07_verdict_opt1","label":"采信推荐路线四（维持 0 承载＋升格入账为构造前提）（推荐）","description":"D 段读数按「构造域负面事实」存档；C 段判定面列为构造前提；0 重跑。","recommended":true},{"id":"d07_verdict_opt2","label":"不采信","description":"所取路线在 Other 说明。"},{"id":"d07_verdict_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"D-07 判断件呈裁（T1 温度轴）"},{"id":"m08","question":"S4 素材面候呈 4：26 件 held-out 中 12 件（46.2%）判据序列为空 ⇒ A／A′／D 读数构成近半来自「无判据文本」之件（敏感性诊断：仅取 14 件非空者，nw_sim 均值 0.5949——非任何线之读数）。当前影响：A／A′／D 之真证伪判定受阻（0 可标真证伪）。处置候选（责任面：PI／worker 补采／protocol 口径）：","selectionMode":"single","options":[{"id":"m08_opt1","label":"补采素材（先派补采评估棒·0 改现有读数）（推荐）","description":"评估 12 件空序列之根因与可补性；补采属 worker 执行面。","recommended":true},{"id":"m08_opt2","label":"登记为「不明」","description":"该面真证伪判定挂「不明」·如实入册。"},{"id":"m08_opt3","label":"口径调整","description":"另立口径件处理空序列占比（protocol 面）。"},{"id":"m08_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"12/26 空序列素材面（M-08）"},{"id":"bc_scope","question":"随本择定复核之两项配套（『e2fdb380cd3c』§7 候呈 3／5）：一是分面权限——v3 面先例 J3（『dac19ee9e66b』§4，判①但「待 PI 复核」未确认）与 S4 面本择定：分面分别裁定，抑或统一适用？（分面与否属 estimand 面）；二是先例 J3 建议与本择定同批复核。请裁复核方式：","selectionMode":"single","options":[{"id":"bc_scope_opt1","label":"统一适用两面——本择定一并适用于 v3 面与 S4 面（J3 同批确认）","description":"避免「同向但未确认」长期悬置。","recommended":true},{"id":"bc_scope_opt2","label":"分面分别裁定","description":"S4 面按本择定；v3 面 J3 另行处置。"},{"id":"bc_scope_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"择定复核方式（候呈 3＋5）"}],"status":"pending","createdAt":1791563500740,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_task_delivery_a3c007ec4ada4ba0aa2ac996b38b0f07","toolCallId":"call_00_JudBlIvA7wPj9MjGHEDi2943"},"purpose":"goal","goalId":"tg_zpe1d8l4usmv16a14x","expiresAt":1791563800740,"title":"轮23 · S4 复核链＋D-07 呈裁（4 项：BC 择定复核／D-07 判断件／12-26 处置／复核方式）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_2dbc05cc3725c7002935ed01","answers":[{"stepId":"bc_review","selectedOptionIds":["bc_review_opt1"],"selectedOther":false},{"stepId":"d07_verdict","selectedOptionIds":["d07_verdict_opt1"],"selectedOther":false},{"stepId":"m08","selectedOptionIds":["m08_opt1"],"selectedOther":false},{"stepId":"bc_scope","selectedOptionIds":["bc_scope_opt1"],"selectedOther":false}],"submittedAt":1791563533949,"source":"user"}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `bc_review`：`selectedOptionIds` = ["bc_review_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `d07_verdict`：`selectedOptionIds` = ["d07_verdict_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `m08`：`selectedOptionIds` = ["m08_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `bc_scope`：`selectedOptionIds` = ["bc_scope_opt1"]；`selectedOther` = false
**题面/答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 13 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 02 · `ask_92fd9e0ed5a2d6a64e4be94b` · 轮24（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮24 · ID／VK 面复核批（M-01／M-02／M-03／P1–P7＋N1–N5）

**卡级元数据（原文照录）**

```text
request_id                     = ask_92fd9e0ed5a2d6a64e4be94b
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮24 · ID／VK 面复核批（M-01／M-02／M-03／P1–P7＋N1–N5）
presentation.allowBackNavigation  = true
presentation.replaceComposer  = true
presentation.showProgress     = true
requester.agentName           = mavis
requester.runId               = turn_01a9a288-248e-4192-9fb0-e92d8435d3c3
requester.sessionId           = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId          = call_00_wk0a8kE15KveSCLE1gpY2128
request_json.createdAt (epoch ms) = 1791563813579   → 2026-10-10 00:36:53.579 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791563813579
created_at (CST 换算)          = 2026-10-10 00:36:53.579 +0800
answered_at (epoch ms)         = 1791563827306
answered_at (CST 换算)         = 2026-10-10 00:37:07.306 +0800
reply_payload.submittedAt(epoch ms) = 1791563827306   → 2026-10-10 00:37:07.306 +0800
injected_at (epoch ms)         = 1791563847421
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `m01`

- `header`（原文照录）：`ID 件三处修订处置（M-01）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
VK 两裁之 P-PI-①：『ad5c76111570』（C-1 定义件·被更正方）之 L40／L120／L130 三处（排列口径误悬于 bootstrap 表述处）如何处置？两候选：回改原件 vs 另立修订·同步件（沿既有体例『原件 0 回改·以件承载更正』）。注：归属面已固化（读法乙）；仅三处字面之处置形态待裁。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `m01_opt1`
  - `label`（逐字原文）：```另立修订·同步件（0 回改原件）（推荐）```
  - `description`（逐字原文）：```沿 b61321ba3b6e §4 既有体例；修订件承接三处更正。```
- `id` = `m01_opt2`
  - `label`（逐字原文）：```回改原件```
  - `description`（逐字原文）：```须先列回改范围与授权（三处逐行）；须明示 0 回改纪律之例外。```
- `id` = `m01_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `m02`

- `header`（原文照录）：`并列列名 vs 去冗（M-02）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
VK 两裁之 P-PI-②（N6）：C-1 细目 L130 之最终字面形态——「并列列名」则正确字面为并列两套（TH-v2-8／TH-v3-17＋TH-v2-7／TH-v3-16）；「去冗」则仅留 bootstrap 一套（排列 ID 不悬于 C-1 表述）。判断件 0 代裁此项。请裁呈现形态：
```

`options`（逐字原文，共 3 项）：

- `id` = `m02_opt1`
  - `label`（逐字原文）：```并列列名——两套并列保留```
  - `description`（逐字原文）：```读者可见完整谱系；但含非 C-1 所用之排列 ID。```
- `id` = `m02_opt2`
  - `label`（逐字原文）：```去冗——仅留 bootstrap 一套```
  - `description`（逐字原文）：```C-1 表述只载 TH-v2-8／TH-v3-17；排列 ID 归 S2/S4 perm 面。```
- `id` = `m02_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `m03`

- `header`（原文照录）：`状态字面统一（M-03）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
VK 两裁之 P-PI-③：两件旧登记仍载『ID 归属仍候 verifier』（『21f2926efc5d』L235、『356fe8509669』L107／L273）——盘上并存『已判』与『候裁』两种状态字面（均属旧态如实留痕）。是否另立勘误/同步件统一状态字面？请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `m03_opt1`
  - `label`（逐字原文）：```另立勘误·同步件统一（0 回改原件）（推荐）```
  - `description`（逐字原文）：```以新件承载状态统一；旧件留旧态留痕。```
- `id` = `m03_opt2`
  - `label`（逐字原文）：```不另立——新件承载已足```
  - `description`（逐字原文）：```旧字面保留为旧态留痕，不追补。```
- `id` = `m03_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `pn_review`

- `header`（原文照录）：`固化条款复核（P1–P7＋N1–N5）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
固化条款复核（D-06 闭条件构成项）。VK 两裁之两组条款候 PI 复核（待复核生效·生效即锁）：P1–P7（h₃ provenance 登记设计）——P1 四要素同随（h_cap 0.1100／h₃ 0.1326086957／源件 585714f9660c／字段路径＋数组逐字值）；P2 引用指引（凡引 0.1100 必书来历）；P3 四读 0 混算禁令；P4 构造域标注（0 外推为 S4 判读读数）；P5 两面命名强制（判据面/报告面同落）；P6 单位口径（0–1 量表）；P7 复核触发（改相对形或跨面非同构时须重钉）。N1–N5（C-1 ID 引用固化）——N1 bootstrap ID＝TH-v2-8／TH-v3-17；N2 seed ID＝TH-v3-15；N3 排列口径正名（TH-v2-7／TH-v3-16·0 悬于 C-1）；N4 0 新设任何 ID；N5 0 变更数值。（P8 已由 D-01 核准·不重列。）请复核：
```

`options`（逐字原文，共 3 项）：

- `id` = `pn_review_opt1`
  - `label`（逐字原文）：```复核通过——P1–P7＋N1–N5 全部生效（生效即锁）（推荐）```
  - `description`（逐字原文）：```D-06 闭条件构成项之一就此落实。```
- `id` = `pn_review_opt2`
  - `label`（逐字原文）：```部分通过```
  - `description`（逐字原文）：```调整项在 Other 说明。```
- `id` = `pn_review_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_92fd9e0ed5a2d6a64e4be94b","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"m01","question":"VK 两裁之 P-PI-①：『ad5c76111570』（C-1 定义件·被更正方）之 L40／L120／L130 三处（排列口径误悬于 bootstrap 表述处）如何处置？两候选：回改原件 vs 另立修订·同步件（沿既有体例『原件 0 回改·以件承载更正』）。注：归属面已固化（读法乙）；仅三处字面之处置形态待裁。请裁：","selectionMode":"single","options":[{"id":"m01_opt1","label":"另立修订·同步件（0 回改原件）（推荐）","description":"沿 b61321ba3b6e §4 既有体例；修订件承接三处更正。","recommended":true},{"id":"m01_opt2","label":"回改原件","description":"须先列回改范围与授权（三处逐行）；须明示 0 回改纪律之例外。"},{"id":"m01_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"ID 件三处修订处置（M-01）"},{"id":"m02","question":"VK 两裁之 P-PI-②（N6）：C-1 细目 L130 之最终字面形态——「并列列名」则正确字面为并列两套（TH-v2-8／TH-v3-17＋TH-v2-7／TH-v3-16）；「去冗」则仅留 bootstrap 一套（排列 ID 不悬于 C-1 表述）。判断件 0 代裁此项。请裁呈现形态：","selectionMode":"single","options":[{"id":"m02_opt1","label":"并列列名——两套并列保留","description":"读者可见完整谱系；但含非 C-1 所用之排列 ID。","recommended":true},{"id":"m02_opt2","label":"去冗——仅留 bootstrap 一套","description":"C-1 表述只载 TH-v2-8／TH-v3-17；排列 ID 归 S2/S4 perm 面。"},{"id":"m02_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"并列列名 vs 去冗（M-02）"},{"id":"m03","question":"VK 两裁之 P-PI-③：两件旧登记仍载『ID 归属仍候 verifier』（『21f2926efc5d』L235、『356fe8509669』L107／L273）——盘上并存『已判』与『候裁』两种状态字面（均属旧态如实留痕）。是否另立勘误/同步件统一状态字面？请裁：","selectionMode":"single","options":[{"id":"m03_opt1","label":"另立勘误·同步件统一（0 回改原件）（推荐）","description":"以新件承载状态统一；旧件留旧态留痕。","recommended":true},{"id":"m03_opt2","label":"不另立——新件承载已足","description":"旧字面保留为旧态留痕，不追补。"},{"id":"m03_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"状态字面统一（M-03）"},{"id":"pn_review","question":"固化条款复核（D-06 闭条件构成项）。VK 两裁之两组条款候 PI 复核（待复核生效·生效即锁）：P1–P7（h₃ provenance 登记设计）——P1 四要素同随（h_cap 0.1100／h₃ 0.1326086957／源件 585714f9660c／字段路径＋数组逐字值）；P2 引用指引（凡引 0.1100 必书来历）；P3 四读 0 混算禁令；P4 构造域标注（0 外推为 S4 判读读数）；P5 两面命名强制（判据面/报告面同落）；P6 单位口径（0–1 量表）；P7 复核触发（改相对形或跨面非同构时须重钉）。N1–N5（C-1 ID 引用固化）——N1 bootstrap ID＝TH-v2-8／TH-v3-17；N2 seed ID＝TH-v3-15；N3 排列口径正名（TH-v2-7／TH-v3-16·0 悬于 C-1）；N4 0 新设任何 ID；N5 0 变更数值。（P8 已由 D-01 核准·不重列。）请复核：","selectionMode":"single","options":[{"id":"pn_review_opt1","label":"复核通过——P1–P7＋N1–N5 全部生效（生效即锁）（推荐）","description":"D-06 闭条件构成项之一就此落实。","recommended":true},{"id":"pn_review_opt2","label":"部分通过","description":"调整项在 Other 说明。"},{"id":"pn_review_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"固化条款复核（P1–P7＋N1–N5）"}],"status":"pending","createdAt":1791563813579,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_01a9a288-248e-4192-9fb0-e92d8435d3c3","toolCallId":"call_00_wk0a8kE15KveSCLE1gpY2128"},"purpose":"goal","goalId":"tg_zpe1d8l4usmv16a14x","expiresAt":1791564113579,"title":"轮24 · ID／VK 面复核批（M-01／M-02／M-03／P1–P7＋N1–N5）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_92fd9e0ed5a2d6a64e4be94b","answers":[{"stepId":"m01","selectedOptionIds":["m01_opt1"],"selectedOther":false},{"stepId":"m02","selectedOptionIds":["m02_opt1"],"selectedOther":false},{"stepId":"m03","selectedOptionIds":["m03_opt1"],"selectedOther":false},{"stepId":"pn_review","selectedOptionIds":["pn_review_opt1"],"selectedOther":false}],"submittedAt":1791563827306,"source":"user"}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `m01`：`selectedOptionIds` = ["m01_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `m02`：`selectedOptionIds` = ["m02_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `m03`：`selectedOptionIds` = ["m03_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `pn_review`：`selectedOptionIds` = ["pn_review_opt1"]；`selectedOther` = false
**题面/答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 12 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 03 · `ask_906e23019db97965b62a29fa` · 轮25（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮25 · T1⑧ 判断件呈裁批（M-15／M-16／M-17／旧门槛重声明）

**卡级元数据（原文照录）**

```text
request_id                     = ask_906e23019db97965b62a29fa
status（表列 questionnaire_requests.status） = superseded
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮25 · T1⑧ 判断件呈裁批（M-15／M-16／M-17／旧门槛重声明）
presentation.allowBackNavigation  = true
presentation.replaceComposer  = true
presentation.showProgress     = true
requester.agentName           = mavis
requester.runId               = turn_b218d6ea-eb09-4cf1-ad74-f76af8a92dbd
requester.sessionId           = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId          = call_00_Z87MQxDc7r8TSvs57WWA4693
request_json.createdAt (epoch ms) = 1791564089033   → 2026-10-10 00:41:29.033 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791564089033
created_at (CST 换算)          = 2026-10-10 00:41:29.033 +0800
answered_at (epoch ms)         = 1791564163848
answered_at (CST 换算)         = 2026-10-10 00:42:43.848 +0800
reply_payload.submittedAt(epoch ms) = 1791564163848   → 2026-10-10 00:42:43.848 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／13 选项，原文照录）**

**题 1／4** — `id` = `m15_verdict`

- `header`（原文照录）：`M-15 升格判断件呈裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧·M-15 升格判断之独立判断件（『5f43775a3224』）已出。结论（分项裁断）：①『更新触发条件』判否——描述性准确化（未定任何口径值、不含义务）⇒存续；②『须于入链前裁断』判是——判断棒自设强制时点义务、在乙档已裁「不适用」之对象上设裁断时点，构成延伸干预⇒作废。反方：『入链前裁断』恰是维护乙档诚实之手段（防『不适用≠永免』无限悬空）——但义务之设立者不能是判断棒本身；若 PI 认须时点义务保障，应由 PI 明设。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `m15_verdict_opt1`
  - `label`（逐字原文）：```采信分项裁断（①存续・②作废・仅余 P-1）（推荐）```
  - `description`（逐字原文）：```升格分项裁断：①存续·②作废；P-1「同面处理」无条件存续。```
- `id` = `m15_verdict_opt2`
  - `label`（逐字原文）：```不采信——Other 说明```
  - `description`（逐字原文）：```可在 Other 说明（如：由 PI 明设时点义务）。```
- `id` = `m15_verdict_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `m16_verdict`

- `header`（原文照录）：`M-16 启用判断件呈裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧·M-16 启用判断之独立判断件（『1e97d06b6ec9』）已出。结论：推荐条件式启用——启用『真实面 N≥30』为 r2 面判据来源，须以『D-1 勘正落定』＋『36 侧构成逐对点名核验通过』双前置为生效条件；落法采 D-09 已核准之双列并报＋0 单列承载；不建议立即启用、亦不建议永久不启用。反方：启用收益系于两项未证之事（D-1 未落定＋36 侧未核验）——此时启用正落入『以待勘正之数为据』之病。另报一处新事实：N_min 之『对』计数口径＝all-pooled 已在样本量面生效、未裁定主度量面（口径串面防读条款之由来）。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `m16_verdict_opt1`
  - `label`（逐字原文）：```采信条件式启用（双前置）（推荐）```
  - `description`（逐字原文）：```双前置：D-1 勘正落定＋36 侧构成逐对点名核验通过；落法采 D-09 双列并报＋0 单列承载。```
- `id` = `m16_verdict_opt2`
  - `label`（逐字原文）：```改采「立即启用」```
  - `description`（逐字原文）：```不等双前置——启用即改判据面（须同批处置口径串面防读条款）。```
- `id` = `m16_verdict_opt3`
  - `label`（逐字原文）：```改采「不启用」```
  - `description`（逐字原文）：```维持现登记面、不新增读法（D-09／D-10 条款备用）。```
- `id` = `m16_verdict_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `m17`

- `header`（原文照录）：`M-17 配对口径并轨确认`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧·M-17 配对计数口径（all-pooled／same-caption）——与 D-09 同面并轨确认。D-09 已核准『双列并报』（same-caption 为判据来源列、all-pooled 为登记对照列、任一口径 0 单独承载判词）⇒ M-17 之『择一』是否即以并报处置？请确认：
```

`options`（逐字原文，共 3 项）：

- `id` = `m17_opt1`
  - `label`（逐字原文）：```以并报处置（同 D-09 并轨）（推荐）```
  - `description`（逐字原文）：```same-caption 判据来源列＋all-pooled 登记对照列；不再单独择一。```
- `id` = `m17_opt2`
  - `label`（逐字原文）：```仍须单独择一```
  - `description`（逐字原文）：```仍须单独择一（Other 指明所选）。```
- `id` = `m17_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `th_r1`

- `header`（原文照录）：`旧门槛重声明（V3-05）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·旧门槛（TH-V3R-1：1.3×／2.0×）重声明——先前已裁『须重声明·另定；具体值须 PI 另给』（β 半换域＋构造变更面后）；盘上 0 候选数值。请裁重声明方式：
```

`options`（逐字原文，共 3 项）：

- `id` = `th_r1_opt1`
  - `label`（逐字原文）：```派设计棒出重声明方案（推荐）```
  - `description`（逐字原文）：```判死线先于跑·不反推；方案件候 PI 复核后生效。```
- `id` = `th_r1_opt2`
  - `label`（逐字原文）：```PI 即时给值```
  - `description`（逐字原文）：```数值在 Other 给出（须声明非由本轮读数反推）。```
- `id` = `th_r1_opt3`
  - `label`（逐字原文）：```暂挂```
  - `description`（逐字原文）：```如实登记为未闭。```

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_906e23019db97965b62a29fa","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"m15_verdict","question":"T1⑧·M-15 升格判断之独立判断件（『5f43775a3224』）已出。结论（分项裁断）：①『更新触发条件』判否——描述性准确化（未定任何口径值、不含义务）⇒存续；②『须于入链前裁断』判是——判断棒自设强制时点义务、在乙档已裁「不适用」之对象上设裁断时点，构成延伸干预⇒作废。反方：『入链前裁断』恰是维护乙档诚实之手段（防『不适用≠永免』无限悬空）——但义务之设立者不能是判断棒本身；若 PI 认须时点义务保障，应由 PI 明设。请裁：","selectionMode":"single","options":[{"id":"m15_verdict_opt1","label":"采信分项裁断（①存续・②作废・仅余 P-1）（推荐）","description":"升格分项裁断：①存续·②作废；P-1「同面处理」无条件存续。","recommended":true},{"id":"m15_verdict_opt2","label":"不采信——Other 说明","description":"可在 Other 说明（如：由 PI 明设时点义务）。"},{"id":"m15_verdict_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"M-15 升格判断件呈裁"},{"id":"m16_verdict","question":"T1⑧·M-16 启用判断之独立判断件（『1e97d06b6ec9』）已出。结论：推荐条件式启用——启用『真实面 N≥30』为 r2 面判据来源，须以『D-1 勘正落定』＋『36 侧构成逐对点名核验通过』双前置为生效条件；落法采 D-09 已核准之双列并报＋0 单列承载；不建议立即启用、亦不建议永久不启用。反方：启用收益系于两项未证之事（D-1 未落定＋36 侧未核验）——此时启用正落入『以待勘正之数为据』之病。另报一处新事实：N_min 之『对』计数口径＝all-pooled 已在样本量面生效、未裁定主度量面（口径串面防读条款之由来）。请裁：","selectionMode":"single","options":[{"id":"m16_verdict_opt1","label":"采信条件式启用（双前置）（推荐）","description":"双前置：D-1 勘正落定＋36 侧构成逐对点名核验通过；落法采 D-09 双列并报＋0 单列承载。","recommended":true},{"id":"m16_verdict_opt2","label":"改采「立即启用」","description":"不等双前置——启用即改判据面（须同批处置口径串面防读条款）。"},{"id":"m16_verdict_opt3","label":"改采「不启用」","description":"维持现登记面、不新增读法（D-09／D-10 条款备用）。"},{"id":"m16_verdict_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"M-16 启用判断件呈裁"},{"id":"m17","question":"T1⑧·M-17 配对计数口径（all-pooled／same-caption）——与 D-09 同面并轨确认。D-09 已核准『双列并报』（same-caption 为判据来源列、all-pooled 为登记对照列、任一口径 0 单独承载判词）⇒ M-17 之『择一』是否即以并报处置？请确认：","selectionMode":"single","options":[{"id":"m17_opt1","label":"以并报处置（同 D-09 并轨）（推荐）","description":"same-caption 判据来源列＋all-pooled 登记对照列；不再单独择一。","recommended":true},{"id":"m17_opt2","label":"仍须单独择一","description":"仍须单独择一（Other 指明所选）。"},{"id":"m17_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"M-17 配对口径并轨确认"},{"id":"th_r1","question":"V3-05·旧门槛（TH-V3R-1：1.3×／2.0×）重声明——先前已裁『须重声明·另定；具体值须 PI 另给』（β 半换域＋构造变更面后）；盘上 0 候选数值。请裁重声明方式：","selectionMode":"single","options":[{"id":"th_r1_opt1","label":"派设计棒出重声明方案（推荐）","description":"判死线先于跑·不反推；方案件候 PI 复核后生效。","recommended":true},{"id":"th_r1_opt2","label":"PI 即时给值","description":"数值在 Other 给出（须声明非由本轮读数反推）。"},{"id":"th_r1_opt3","label":"暂挂","description":"如实登记为未闭。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"旧门槛重声明（V3-05）"}],"status":"pending","createdAt":1791564089033,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_b218d6ea-eb09-4cf1-ad74-f76af8a92dbd","toolCallId":"call_00_Z87MQxDc7r8TSvs57WWA4693"},"purpose":"goal","goalId":"tg_zpe1d8l4usmv16a14x","expiresAt":1791564389033,"title":"轮25 · T1⑧ 判断件呈裁批（M-15／M-16／M-17／旧门槛重声明）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_906e23019db97965b62a29fa","answers":[{"stepId":"m15_verdict","selectedOptionIds":["m15_verdict_opt1"],"selectedOther":false},{"stepId":"m16_verdict","selectedOptionIds":["m16_verdict_opt1"],"selectedOther":false},{"stepId":"m17","selectedOptionIds":["m17_opt1"],"selectedOther":false},{"stepId":"th_r1","selectedOptionIds":["th_r1_opt1"],"selectedOther":false}],"submittedAt":1791564163848,"source":"user"}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `m15_verdict`：`selectedOptionIds` = ["m15_verdict_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `m16_verdict`：`selectedOptionIds` = ["m16_verdict_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `m17`：`selectedOptionIds` = ["m17_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `th_r1`：`selectedOptionIds` = ["th_r1_opt1"]；`selectedOther` = false
**题面/答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 13 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 04 · `ask_d638adfe6dcf33b095e26c25` · 轮26（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮26 · 收尾批（M-13／M-14／补采档／M-09）——夜间最后一卡·明晨清卷

**卡级元数据（原文照录）**

```text
request_id                     = ask_d638adfe6dcf33b095e26c25
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮26 · 收尾批（M-13／M-14／补采档／M-09）——夜间最后一卡·明晨清卷
presentation.allowBackNavigation  = true
presentation.replaceComposer  = true
presentation.showProgress     = true
requester.agentName           = mavis
requester.runId               = turn_353188f0-2fcb-471f-ba74-f7b339856998
requester.sessionId           = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId          = call_00_zLXOYdG0DksKeWfQ7dVR1907
request_json.createdAt (epoch ms) = 1791565215009   → 2026-10-10 01:00:15.009 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791565215009
created_at (CST 换算)          = 2026-10-10 01:00:15.009 +0800
answered_at (epoch ms)         = 1791565255760
answered_at (CST 换算)         = 2026-10-10 01:00:55.760 +0800
reply_payload.submittedAt(epoch ms) = 1791565255760   → 2026-10-10 01:00:55.760 +0800
injected_at (epoch ms)         = 1791565255909
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `m13`

- `header`（原文照录）：`删裸词授权（M-13）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
词表·M-13：是否授权自 L1 删裸词『PI』（移入 L3 读数位）？语境：删词改既有表之构成；虽『8C5F83C3C4CF』§3.4 反方 1 已建议（裸词 PI 与『0 处 PI』系同一断言、不构成二次独立验证），原判词件 0 回改 ⇒ 须 PI 明文。关联：r19b 已采纳『分级（触发位）＋先立单一词表之家』——本项为立家构成之授权。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `m13_opt1`
  - `label`（逐字原文）：```授权——自 L1 删裸词『PI』（移入 L3）（推荐）```
  - `description`（逐字原文）：```沿判断件建议；立家时按此构成。```
- `id` = `m13_opt2`
  - `label`（逐字原文）：```不授权——维持 L1 现状（0 回改）```
  - `description`（逐字原文）：```裸词保留；立家体例另议。```
- `id` = `m13_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `m14`

- `header`（原文照录）：`L2 执行面归属（M-14）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
词表·M-14：L2 触发定性之执行面归属（三择一）——检棒自查 / 独立复核棒 / verifier。语境：涉『定性污染』之隔离（判断件 §2.4 反方二）⇒ 属分工面。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `m14_opt1`
  - `label`（逐字原文）：```独立复核棒（0 自查·隔离定性污染）（推荐）```
  - `description`（逐字原文）：```检棒与定性分属不同棒；成本居中。```
- `id` = `m14_opt2`
  - `label`（逐字原文）：```检棒自查```
  - `description`（逐字原文）：```最省；但采『命中即定性』的自查路径，有污染风险（判断件反方二所指）。```
- `id` = `m14_opt3`
  - `label`（逐字原文）：```verifier 面```
  - `description`（逐字原文）：```终审级；成本最高。```
- `id` = `m14_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `backfill`

- `header`（原文照录）：`补采执行处置（档 A/B）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 补采评估件（『41b75ffea7be』）已出：12/12 可补——档 A：9 件『可补·重生成』（词表覆盖缺口·文本已在库·0 新采样）；档 B：3 件『可补·候 PI 在席补录』（采集合规缺件·素材侧真缺）。请裁执行：
```

`options`（逐字原文，共 4 项）：

- `id` = `backfill_opt1`
  - `label`（逐字原文）：```档 A 先行（扩充词表·重生成 9 件）＋档 B 候 PI 补录（推荐）```
  - `description`（逐字原文）：```须先立扩充词表口径（protocol 面）；重生成另立新件并陈、0 改现读数。```
- `id` = `backfill_opt2`
  - `label`（逐字原文）：```仅档 A```
  - `description`（逐字原文）：```档 B 维持缺采登记。```
- `id` = `backfill_opt3`
  - `label`（逐字原文）：```暂缓（维持现读数）```
  - `description`（逐字原文）：```如实登记为未闭。```
- `id` = `backfill_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `m09`

- `header`（原文照录）：`标签偏斜/树深（M-09）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4·M-09：训练面标签偏斜（UNKNOWN=90/179）·树深触顶（6＝上限）——构造效度受限（0 掩饰）。其具体动作（提高上限／改模型）属执行面。请裁处置：
```

`options`（逐字原文，共 3 项）：

- `id` = `m09_opt1`
  - `label`（逐字原文）：```派 worker 评估构造调整（提高树深上限等）·0 改现读数（推荐）```
  - `description`（逐字原文）：```评估先行；调整与否据评估再裁。```
- `id` = `m09_opt2`
  - `label`（逐字原文）：```维持登记（构造效度受限留痕）```
  - `description`（逐字原文）：```不动构造；限制如实随读数。```
- `id` = `m09_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_d638adfe6dcf33b095e26c25","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"m13","question":"词表·M-13：是否授权自 L1 删裸词『PI』（移入 L3 读数位）？语境：删词改既有表之构成；虽『8C5F83C3C4CF』§3.4 反方 1 已建议（裸词 PI 与『0 处 PI』系同一断言、不构成二次独立验证），原判词件 0 回改 ⇒ 须 PI 明文。关联：r19b 已采纳『分级（触发位）＋先立单一词表之家』——本项为立家构成之授权。请裁：","selectionMode":"single","options":[{"id":"m13_opt1","label":"授权——自 L1 删裸词『PI』（移入 L3）（推荐）","description":"沿判断件建议；立家时按此构成。","recommended":true},{"id":"m13_opt2","label":"不授权——维持 L1 现状（0 回改）","description":"裸词保留；立家体例另议。"},{"id":"m13_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"删裸词授权（M-13）"},{"id":"m14","question":"词表·M-14：L2 触发定性之执行面归属（三择一）——检棒自查 / 独立复核棒 / verifier。语境：涉『定性污染』之隔离（判断件 §2.4 反方二）⇒ 属分工面。请裁：","selectionMode":"single","options":[{"id":"m14_opt1","label":"独立复核棒（0 自查·隔离定性污染）（推荐）","description":"检棒与定性分属不同棒；成本居中。","recommended":true},{"id":"m14_opt2","label":"检棒自查","description":"最省；但采『命中即定性』的自查路径，有污染风险（判断件反方二所指）。"},{"id":"m14_opt3","label":"verifier 面","description":"终审级；成本最高。"},{"id":"m14_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"L2 执行面归属（M-14）"},{"id":"backfill","question":"S4 补采评估件（『41b75ffea7be』）已出：12/12 可补——档 A：9 件『可补·重生成』（词表覆盖缺口·文本已在库·0 新采样）；档 B：3 件『可补·候 PI 在席补录』（采集合规缺件·素材侧真缺）。请裁执行：","selectionMode":"single","options":[{"id":"backfill_opt1","label":"档 A 先行（扩充词表·重生成 9 件）＋档 B 候 PI 补录（推荐）","description":"须先立扩充词表口径（protocol 面）；重生成另立新件并陈、0 改现读数。","recommended":true},{"id":"backfill_opt2","label":"仅档 A","description":"档 B 维持缺采登记。"},{"id":"backfill_opt3","label":"暂缓（维持现读数）","description":"如实登记为未闭。"},{"id":"backfill_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"补采执行处置（档 A/B）"},{"id":"m09","question":"S4·M-09：训练面标签偏斜（UNKNOWN=90/179）·树深触顶（6＝上限）——构造效度受限（0 掩饰）。其具体动作（提高上限／改模型）属执行面。请裁处置：","selectionMode":"single","options":[{"id":"m09_opt1","label":"派 worker 评估构造调整（提高树深上限等）·0 改现读数（推荐）","description":"评估先行；调整与否据评估再裁。","recommended":true},{"id":"m09_opt2","label":"维持登记（构造效度受限留痕）","description":"不动构造；限制如实随读数。"},{"id":"m09_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"标签偏斜/树深（M-09）"}],"status":"pending","createdAt":1791565215009,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_353188f0-2fcb-471f-ba74-f7b339856998","toolCallId":"call_00_zLXOYdG0DksKeWfQ7dVR1907"},"purpose":"goal","goalId":"tg_zpe1d8l4usmv16a14x","expiresAt":1791565515009,"title":"轮26 · 收尾批（M-13／M-14／补采档／M-09）——夜间最后一卡·明晨清卷"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_d638adfe6dcf33b095e26c25","answers":[{"stepId":"m13","selectedOptionIds":["m13_opt1"],"selectedOther":false},{"stepId":"m14","selectedOptionIds":["m14_opt1"],"selectedOther":false},{"stepId":"backfill","selectedOptionIds":["backfill_opt1"],"selectedOther":false},{"stepId":"m09","selectedOptionIds":["m09_opt1"],"selectedOther":false}],"submittedAt":1791565255760,"source":"user"}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `m13`：`selectedOptionIds` = ["m13_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `m14`：`selectedOptionIds` = ["m14_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `backfill`：`selectedOptionIds` = ["backfill_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `m09`：`selectedOptionIds` = ["m09_opt1"]；`selectedOther` = false
**题面/答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 14 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 05 · `ask_b56649e37d180c79e1ec47e7` · 轮旧门槛复核（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> V3-05 旧门槛重声明设计·复核（草案 fb85a8013f9d）

**卡级元数据（原文照录）**

```text
request_id                     = ask_b56649e37d180c79e1ec47e7
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = V3-05 旧门槛重声明设计·复核（草案 fb85a8013f9d）
presentation.allowBackNavigation  = true
presentation.replaceComposer  = true
presentation.showProgress     = true
requester.agentName           = mavis
requester.runId               = turn_e6337c9f-eff3-4f90-b6e9-255178e1a623
requester.sessionId           = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId          = call_00_4MUyHlNk9g9gb7qBM7eb5327
request_json.createdAt (epoch ms) = 1791565439744   → 2026-10-10 01:03:59.744 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791565439744
created_at (CST 换算)          = 2026-10-10 01:03:59.744 +0800
answered_at (epoch ms)         = 1791565492478
answered_at (CST 换算)         = 2026-10-10 01:04:52.478 +0800
reply_payload.submittedAt(epoch ms) = 1791565492478   → 2026-10-10 01:04:52.478 +0800
injected_at (epoch ms)         = 1791565492555
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 1 步／4 选项，原文照录）**

**题 1／1** — `id` = `th_review`

- `header`（原文照录）：`旧门槛重声明设计复核（V3-05）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05 旧门槛重声明设计件（『fb85a8013f9d』·33,847 B）已出（草案·候 PI 复核）。推荐：案③分层门槛为骨架（旧域沿 1.3×／2.0× 字面不动、新域另立）＋案①仅取构造侧推导程序、弃其预算比锚＋案④降格为报值纪律；终值仍由 PI 给（本件新设数值阈值＝0 个）。关键发现：①源流真源＝P-A V0 spec（bd1caab42b4c §1，boss_pa_1 为承载体，链闭合）；②溯通暴露 5 处口径漂移（最重：分子换了 D-2、CI 合取脱落 D-3）；③反方指出「TH-V3R-1 三项合取中两腿全仓 0 处读数（E-13）——门槛当前无判据可施，或应先闭输入面（授权 EXP-04）而非先立线」。请复核：
```

`options`（逐字原文，共 4 项）：

- `id` = `th_review_opt1`
  - `label`（逐字原文）：```复核通过——按推荐方案（案③骨架）推进（推荐）```
  - `description`（逐字原文）：```案③分层：旧域沿 1.3×／2.0× 字面不动、新域另立；终值候 PI 另给（0 自设）。```
- `id` = `th_review_opt2`
  - `label`（逐字原文）：```采反方路径——先闭输入面再立线```
  - `description`（逐字原文）：```先闭输入面（授权 EXP-04 类实验）再立线；门槛暂维持 0 判据可施之登记。```
- `id` = `th_review_opt3`
  - `label`（逐字原文）：```部分调整```
  - `description`（逐字原文）：```调整项在 Other 说明。```
- `id` = `th_review_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_b56649e37d180c79e1ec47e7","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"th_review","question":"V3-05 旧门槛重声明设计件（『fb85a8013f9d』·33,847 B）已出（草案·候 PI 复核）。推荐：案③分层门槛为骨架（旧域沿 1.3×／2.0× 字面不动、新域另立）＋案①仅取构造侧推导程序、弃其预算比锚＋案④降格为报值纪律；终值仍由 PI 给（本件新设数值阈值＝0 个）。关键发现：①源流真源＝P-A V0 spec（bd1caab42b4c §1，boss_pa_1 为承载体，链闭合）；②溯通暴露 5 处口径漂移（最重：分子换了 D-2、CI 合取脱落 D-3）；③反方指出「TH-V3R-1 三项合取中两腿全仓 0 处读数（E-13）——门槛当前无判据可施，或应先闭输入面（授权 EXP-04）而非先立线」。请复核：","selectionMode":"single","options":[{"id":"th_review_opt1","label":"复核通过——按推荐方案（案③骨架）推进（推荐）","description":"案③分层：旧域沿 1.3×／2.0× 字面不动、新域另立；终值候 PI 另给（0 自设）。","recommended":true},{"id":"th_review_opt2","label":"采反方路径——先闭输入面再立线","description":"先闭输入面（授权 EXP-04 类实验）再立线；门槛暂维持 0 判据可施之登记。"},{"id":"th_review_opt3","label":"部分调整","description":"调整项在 Other 说明。"},{"id":"th_review_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"旧门槛重声明设计复核（V3-05）"}],"status":"pending","createdAt":1791565439744,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_e6337c9f-eff3-4f90-b6e9-255178e1a623","toolCallId":"call_00_4MUyHlNk9g9gb7qBM7eb5327"},"purpose":"goal","goalId":"tg_zpe1d8l4usmv16a14x","expiresAt":1791565739744,"title":"V3-05 旧门槛重声明设计·复核（草案 fb85a8013f9d）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_b56649e37d180c79e1ec47e7","answers":[{"stepId":"th_review","selectedOptionIds":["th_review_opt1"],"selectedOther":false}],"submittedAt":1791565492478,"source":"user"}
```

**答文逐字（逐条展开，原文照录）**

答 1／1 — `stepId` = `th_review`：`selectedOptionIds` = ["th_review_opt1"]；`selectedOther` = false
**题面/答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 1 |
| `options` 总数 | 4 |
| `answers` 数 | 1 |
| 转录失败项 | **0** |

---

## 2 · 对账（**0 漏录 · 0 重复 · 0 掩饰**）

| 序 | `request_id` | 轮 | `created_at`（CST） | `answered_at`（CST） | `status` | 前三批是否已含 |
|---:|---|---|---|---|---|---|
| 1 | `ask_2dbc05cc3725c7002935ed01` | 轮23 | 2026-10-10 00:31:40.740 +0800 | 2026-10-10 00:32:13.949 +0800 | `answered` | ⛔ 未含（实测·前三批 39+17 件标题节无此 id） |
| 2 | `ask_92fd9e0ed5a2d6a64e4be94b` | 轮24 | 2026-10-10 00:36:53.579 +0800 | 2026-10-10 00:37:07.306 +0800 | `answered` | ⛔ 未含（实测·前三批 39+17 件标题节无此 id） |
| 3 | `ask_906e23019db97965b62a29fa` | 轮25 | 2026-10-10 00:41:29.033 +0800 | 2026-10-10 00:42:43.848 +0800 | `superseded` | ⛔ 未含（实测·前三批 39+17 件标题节无此 id） |
| 4 | `ask_d638adfe6dcf33b095e26c25` | 轮26 | 2026-10-10 01:00:15.009 +0800 | 2026-10-10 01:00:55.760 +0800 | `answered` | ⛔ 未含（实测·前三批 39+17 件标题节无此 id） |
| 5 | `ask_b56649e37d180c79e1ec47e7` | 轮旧门槛复核 | 2026-10-10 01:03:59.744 +0800 | 2026-10-10 01:04:52.478 +0800 | `answered` | ⛔ 未含（实测·前三批 39+17 件标题节无此 id） |

⇒ **5／5 件转录完成、0 失败**；逐字转录之 `steps` 合计 **17** 步、`options` 合计 **56** 项、`answers` 合计 **17** 条。

### 2.1 ⚠ 一处状态差异之如实登记（**0 判读 · 0 掩饰**）

卡 `ask_906e23019db97965b62a29fa`（轮25）之表列 `status` ＝ **`superseded`**（⛔ 非 `answered`）——即**该卡已被后续卡取代/覆盖**。本件**如实照录该状态字面**，⛔ **0 将其改呈为 `answered`**，⛔ **0 判读其被取代之原因**（**原因面盘上 0 有定义件**，如实登记为**未核得**）。

> 📌 **该状态对其 `reply_payload` 之效力含义**：本件**仅转录**其 `answers` 原文；其「已答毕」之事实由 `reply_payload.answers` 非空且 `submittedAt` 存在可证；但**「superseded」是否影响其答文之裁断效力**，属**效力面**，⛔ **本件 0 判读**——一切效力仍以其原登记件为准（见文件头「效力声明」）。

### 2.2 本件之边界（诚实交代）

1. **本件非全表应录全集** —— 系派工指定之 5 张目标卡之逐字转录；⛔ **0 声称已覆盖本轮新建之全部卡**。
2. **本件 0 核他件之内部正确性** —— ⛔ 0 复核 `dc43e3cb7610`／`193386b9f23c`／`d917180db36f` 三批登记件之内容；仅核其**存在性与 SHA-12**。
3. **`superseded` 之成因未核得**（见 §2.1）—— 如实登记，⛔ 0 推测。
4. **行号/定位引用之限定** —— 本件所载定位均为**卡内 step id**（稳定键），非文件行号；各该卡 ⛔ 0 回改 ⇒ step id 稳定。

---

## 3 · 0 回改确认 ＋ 落盘自证

### 3.1 0 回改确认

| 项 | 确认 |
|---|---|
| 既有件写动作 | **0** —— ⛔ 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除任何既有件（**含前三批落册登记件**） |
| 本棒写动作 | **新增 1 件**（本件） |
| 运行时库 | **只读**（`mode=ro`）—— 0 写入、0 修改、0 建表、0 提交 |

### 3.2 落前撞名实测

| 项 | 实测结果 |
|---|---|
| 落前撞名 | `Test-Path 'results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md'` ＝ **False**；`results/*supplement_3*` glob 命中 **0** ⇒ ✅ **新名新建 · 0 覆写 · 0 重名** |
| 编码 | **UTF-8 无 BOM** · **LF**（随回执自报实测） |

### 3.3 输入件指纹（本棒 `SHA256` **当轮实测** · **0 沿用他件登记值**）

| 件 | SHA-12 | 字节 |
|---|---|---:|
| `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `dc43e3cb7610` | 262542 |
| `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `193386b9f23c` | 72199 |
| `results/_questionnaire_cards_intake_register_2026_10_09.md` | `d917180db36f` | 442288 |

### 3.4 边界声明 · 0 编造

- **0 编造 PI 立场**：本件所载五卡之题面与答文**均取自运行时库原件**（程序化逐字转录）；⛔ **0 推测** PI 对任何一项之将来处置。
- **0 冒充他棒**：本件由 **protocol-keeper** 出件；⛔ 0 顶任何他方名头。
- **0 网络 · 0 skill · 0 LLM · 0 实验**：本棒仅本机只读取证 ＋ 1 件新建。
- **R4**：⛔ 0 读 key、⛔ 0 读 `.env`、⛔ 0 落盘凭据、**key 永不明文**。

**本件状态**：✅ **5 卡逐字转录完成 · 0 失败 · 0 判读 · 0 代裁 · 0 回改** ｜ ⛔ 0 网络 · 0 skill · 0 LLM
