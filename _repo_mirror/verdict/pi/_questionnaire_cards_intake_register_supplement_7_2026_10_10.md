# 裁卡原件批量落册（第八批）· questionnaire 原件逐字转录 · 卡答落册补续批（2026-10-10）

## 文件头注

- **件名**：`results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md`
- **落册日期**：2026-10-10（CST）
- **件系**：第七批登记件 `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md`（SHA-12 `95ba771fa760`）之**补续落册（第八批）**；上承第七批 `95ba771fa760`、第六批 `edb57308170d`、第五批 `d6ff041a9df9`、第四批 `11681f0ad861`、第三批 `dc43e3cb7610`、第二批 `193386b9f23c`、第一批 `d917180db36f`。⛔ 0 编辑／覆写／修改前七批登记件；⛔ 0 重复转录其已收录之卡。
- **本批口径**：**卡答落册 · 补续批** —— 续录派工指定之**轮49～轮52 四卡**（第七批落册读时点之后所建、⛔ 尚未落册者）。合计 **4 卡／16 答**。
- **编制**：**doc-writer**（文稿起草官 · 分支会话 `mvs_6f4c99f0aebc4da3a76ac9373e2c769e`｜署名如实 · **0 冒充 PI／parent／protocol-keeper／verdict-keeper／verifier／worker**）
- **来源**：运行时库 `〔本地绝对路径·脱敏略:runtime-state.sqlite〕`，表 `questionnaire_requests`。本轮以 `sqlite3.connect("file:...?mode=ro", uri=True)` **只读实测**（0 写入、0 修改、0 建表、0 提交）。
- **备核源**：会话消息面 `〔本地绝对路径·脱敏略:02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5〕` 之 `messages.jsonl`（只读检索，作二次交叉核对）。
  - ⚠ **会话目录反解纪律**：目录名 ＝ `session_` ＋ 会话 id 之 URL-safe base64 无填充编码；该目录层存在**形近近邻陷阱**（`…X2IiZW…` 与 `…X2JiZW…` 仅差字符、并存同层）。本棒**先独立反解定位**（`[Convert]::ToBase64String` → 去填充 → URL-safe 替换）得 `bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5`，⛔ **0 凭记忆直接引用路径**；实际目录名含时间戳前缀 `02-38-47-809-`，实测命中。
- **窗口口径**：本批应录＝派工指定之 **4 张目标卡**（轮49～轮52）——**本件非全表扫描之应录全集**，系**指定目标行**之逐字转录（沿「库读取限 `questionnaire_requests` 目标行」之派工纪律）。
  - ⚠ **活库声明**：运行时库为**活库**，本件之读得时点即收录截止时点；库中或含他卡（含新建未答卡）——⛔ **不属本件应录面**，⛔ 0 转录。
  - ⚠ **活库较第七批之变动**：第七批落册读时点全表 **419** 行（`answered=416／pending=1／superseded=2`）；本批读时点全表 **423** 行（`answered=420／pending=1／superseded=2`）——其差为第七批之后另建之卡，**⛔ 0 超出派工指定 4 卡转录**。
- **转录纪律**：**逐字、0 省略、0 解释、0 判读**。题面（`request_json.steps` 之 id／header／question／options／selectionMode／required／allowOther／otherPlaceholder）与答文（`reply_payload` 全文，含 `selectedOther`／`otherText`）均按库中原文照录；本件**不含**任何分析、结论、裁断或建议。
- **效力声明**：本件**仅转录**。⛔ **0 当「裁录」**；⛔ **0 代替任何既有登记件的裁录效力**。本件不产生、不替代、不撤销任何裁决；一切裁断效力仍以其原登记件／生效件为准。
- **命名合规**：`_主题_日期` 体例；⛔ 0 带 V-阶段前缀（0 `_v3_`／`_v4_`／`_v5_`）。沿既有 `_supplement_` 续编体例（第一批 → `_supplement_` → `_supplement_2_` → `_supplement_3_` → `_supplement_4_` → `_supplement_5_` → `_supplement_6_` → 本件 `_supplement_7_`）。
- **版式**：UTF-8 无 BOM · LF（CRLF ＝ 0）｜**R4**：key 永不明文（本棒 0 读 key／0 读 `.env`／0 落盘凭据）｜**0 网络 · 0 skill · 0 LLM · 0 实验**。
- **编制方式**：程序化逐字转录（⛔ 0 人工改写任何字面）。

---

## 0 · 本轮读取基准（provenance）

- 库文件大小（读取时点）：`474656768` bytes
- 库文件 mtime（读取时点，CST）：`2026-10-10 16:40:20.847024+0800`
- 表 `questionnaire_requests` 总行数（全表，本轮实测）：`423`
- 全表 status 分布（全表实测）：`answered`=420；`pending`=1；`superseded`=2；
- 抽取口径：`SELECT ... FROM questionnaire_requests WHERE request_id IN (4 个目标 id)`（**指定目标行**，⛔ 0 全表内容扫描、⛔ 0 LIMIT 截断）；命中 **4**／4。
- 时间换算口径：`created_at`／`answered_at`／`submittedAt`／`createdAt` 均为 **INTEGER epoch 毫秒**，本件统一换算为 **CST（UTC+8）** 呈现，原值同时照录。
- 值形口径：SQL／JSON 空值一律呈为 `NULL`；布尔值一律呈为 JSON 小写字面 `true`／`false`（沿前七批体例）。
- **复核核对口径**：本件另以会话消息面 `messages.jsonl` 按各 `ask_…` requestId 检索卡片呈递与答复段落，作独立交叉核对源；`messages.jsonl` 读取时点字节 `535232`、行数 `34`、SHA-12 `574c13218127`。

---

## 1 · 逐卡转录（指定目标 4 件，按 `created_at` 升序）

### 01 · `ask_37de1297db68c580a2795fd5` · 轮49（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮49 · G5 段三与 U 面四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_37de1297db68c580a2795fd5
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮49 · G5 段三与 U 面四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName             = mavis
requester.runId                 = turn_28f720c6-175d-4e46-a5a4-ad05e01eff91
requester.sessionId             = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId            = call_00_TzZOfZ5oQRMqvjDpyAxf8497
request_json.createdAt (epoch ms)= 1791615374975   → 2026-10-10 14:56:14.975 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791615374975
created_at (CST 换算)            = 2026-10-10 14:56:14.975 +0800
answered_at (epoch ms)         = 1791616166317
answered_at (CST 换算)           = 2026-10-10 15:09:26.317 +0800
reply_payload.submittedAt(epoch ms)= 1791616166317   → 2026-10-10 15:09:26.317 +0800
injected_at (epoch ms)         = 1791616178827
injected_at (CST 换算)           = 2026-10-10 15:09:38.827 +0800
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／10 选项，原文照录）**

**题 1／4** — `id` = `eg5_1`

- `header`（原文照录）：`G5·E-G5-①`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
G5 段三落裁：A′ 新旧逐位持平（机制使然·NLED 不敏感于空→非空；A 线实升 +0.1038；17/24 位移为 T3）——「持平是否即否决」？
```

`options`（逐字原文，共 3 项）：

- `id` = `eg5_1_opt1`
  - `label`（逐字原文）：```甲：持平≠否决——触发不成立（沿「方向登记」窄读·步骤五可续）```
  - `description`（逐字原文）：（无此键）
- `id` = `eg5_1_opt2`
  - `label`（逐字原文）：```乙：持平＝否决——触发成立（开另开重判面·规格草案启动）```
  - `description`（逐字原文）：（无此键）
- `id` = `eg5_1_opt3`
  - `label`（逐字原文）：```丙：另议（含交 verdict-keeper 裁）```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `u5_disp`

- `header`（原文照录）：`U-5 处置`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
U-5 终裁：66f900b7598b「悬空」已证为指纹漂移（文件实存·现行 dc9cb0e02922·L115 逐字在位）——如何处置？
```

`options`（逐字原文，共 3 项）：

- `id` = `u5_disp_opt1`
  - `label`（逐字原文）：```甲：以现行指纹重定位（另立勘正件·更新引用面）```
  - `description`（逐字原文）：（无此键）
- `id` = `u5_disp_opt2`
  - `label`（逐字原文）：```乙：承认旧指纹失效（登记不可用·引述改用现行）```
  - `description`（逐字原文）：（无此键）
- `id` = `u5_disp_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `u3_e7`

- `header`（原文照录）：`U-3·E7`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
U-3 出口 E7：N-10「give-up 0 既有用法」登记已过期（B 判断件 13:17 引用之）——是否出勘误件？
```

`options`（逐字原文，共 2 项）：

- `id` = `u3_e7_opt1`
  - `label`（逐字原文）：```甲：出勘误件（更正 N-10 登记）```
  - `description`（逐字原文）：（无此键）
- `id` = `u3_e7_opt2`
  - `label`（逐字原文）：```乙：维持（另件登记已足）```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `u2_e6`

- `header`（原文照录）：`U-2·E6`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
U-2 出口 E6：是否连带修订 N-01/N-08（「独立档」与「读数口径」两层之辨之消解）？
```

`options`（逐字原文，共 2 项）：

- `id` = `u2_e6_opt1`
  - `label`（逐字原文）：```甲：连带修订（另出修订件）```
  - `description`（逐字原文）：（无此键）
- `id` = `u2_e6_opt2`
  - `label`（逐字原文）：```乙：维持（并存留痕即足）```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_37de1297db68c580a2795fd5","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"eg5_1","question":"G5 段三落裁：A′ 新旧逐位持平（机制使然·NLED 不敏感于空→非空；A 线实升 +0.1038；17/24 位移为 T3）——「持平是否即否决」？","selectionMode":"single","options":[{"id":"eg5_1_opt1","label":"甲：持平≠否决——触发不成立（沿「方向登记」窄读·步骤五可续）"},{"id":"eg5_1_opt2","label":"乙：持平＝否决——触发成立（开另开重判面·规格草案启动）"},{"id":"eg5_1_opt3","label":"丙：另议（含交 verdict-keeper 裁）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"G5·E-G5-①"},{"id":"u5_disp","question":"U-5 终裁：66f900b7598b「悬空」已证为指纹漂移（文件实存·现行 dc9cb0e02922·L115 逐字在位）——如何处置？","selectionMode":"single","options":[{"id":"u5_disp_opt1","label":"甲：以现行指纹重定位（另立勘正件·更新引用面）"},{"id":"u5_disp_opt2","label":"乙：承认旧指纹失效（登记不可用·引述改用现行）"},{"id":"u5_disp_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"U-5 处置"},{"id":"u3_e7","question":"U-3 出口 E7：N-10「give-up 0 既有用法」登记已过期（B 判断件 13:17 引用之）——是否出勘误件？","selectionMode":"single","options":[{"id":"u3_e7_opt1","label":"甲：出勘误件（更正 N-10 登记）"},{"id":"u3_e7_opt2","label":"乙：维持（另件登记已足）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"U-3·E7"},{"id":"u2_e6","question":"U-2 出口 E6：是否连带修订 N-01/N-08（「独立档」与「读数口径」两层之辨之消解）？","selectionMode":"single","options":[{"id":"u2_e6_opt1","label":"甲：连带修订（另出修订件）"},{"id":"u2_e6_opt2","label":"乙：维持（并存留痕即足）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"U-2·E6"}],"status":"pending","createdAt":1791615374975,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_28f720c6-175d-4e46-a5a4-ad05e01eff91","toolCallId":"call_00_TzZOfZ5oQRMqvjDpyAxf8497"},"title":"轮49 · G5 段三与 U 面四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_37de1297db68c580a2795fd5","answers":[{"stepId":"eg5_1","selectedOptionIds":["eg5_1_opt3"],"selectedOther":false},{"stepId":"u5_disp","selectedOptionIds":["u5_disp_opt1"],"selectedOther":false},{"stepId":"u3_e7","selectedOptionIds":["u3_e7_opt1"],"selectedOther":false},{"stepId":"u2_e6","selectedOptionIds":["u2_e6_opt1"],"selectedOther":false}],"submittedAt":1791616166317}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `eg5_1`：`selectedOptionIds` = ["eg5_1_opt3"]；`selectedOther` = false
答 2／4 — `stepId` = `u5_disp`：`selectedOptionIds` = ["u5_disp_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `u3_e7`：`selectedOptionIds` = ["u3_e7_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `u2_e6`：`selectedOptionIds` = ["u2_e6_opt1"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `eg5_1`：`eg5_1_opt3` → 选项字面（逐字）= `丙：另议（含交 verdict-keeper 裁）`
- 答 2／4 — `u5_disp`：`u5_disp_opt1` → 选项字面（逐字）= `甲：以现行指纹重定位（另立勘正件·更新引用面）`
- 答 3／4 — `u3_e7`：`u3_e7_opt1` → 选项字面（逐字）= `甲：出勘误件（更正 N-10 登记）`
- 答 4／4 — `u2_e6`：`u2_e6_opt1` → 选项字面（逐字）= `甲：连带修订（另出修订件）`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 10 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

## 1 · 逐卡转录（指定目标 4 件，按 `created_at` 升序）

### 02 · `ask_e88ff9f69f669b1a50fe8b83` · 轮50（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮50 · E-4 收口与生效四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_e88ff9f69f669b1a50fe8b83
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮50 · E-4 收口与生效四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName             = mavis
requester.runId                 = turn_9c24419c-c794-4c7c-8ce0-b060778abb3a
requester.sessionId             = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId            = call_00_ay4wb1MXmOspYDTDdadd0647
request_json.createdAt (epoch ms)= 1791616335412   → 2026-10-10 15:12:15.412 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791616335412
created_at (CST 换算)            = 2026-10-10 15:12:15.412 +0800
answered_at (epoch ms)         = 1791617477236
answered_at (CST 换算)           = 2026-10-10 15:31:17.236 +0800
reply_payload.submittedAt(epoch ms)= 1791617477236   → 2026-10-10 15:31:17.236 +0800
injected_at (epoch ms)         = 1791617488444
injected_at (CST 换算)           = 2026-10-10 15:31:28.444 +0800
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `e4b_merge`

- `header`（原文照录）：`E-4b·轴二并入`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-4 轴二（v1.1 基础面 4 件位移，已实跑在册）是否并入面 II（24→28）？
```

`options`（逐字原文，共 3 项）：

- `id` = `e4b_merge_opt1`
  - `label`（逐字原文）：```甲：不并入——面 II 维持 24 件；v1.1 4 件另案在册（现状）```
  - `description`（逐字原文）：（无此键）
- `id` = `e4b_merge_opt2`
  - `label`（逐字原文）：```乙：并入——面 II 扩为 28 件（须另立登记）```
  - `description`（逐字原文）：（无此键）
- `id` = `e4b_merge_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `w2bc_eff`

- `header`（原文照录）：`W-2b/c 生效`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
W-2 落实件之两项候核准——W-2b「状态轴不构成第 5 类」之生效＋W-2c 勘误件（17→12）之生效——核准否？
```

`options`（逐字原文，共 3 项）：

- `id` = `w2bc_eff_opt1`
  - `label`（逐字原文）：```甲：两项核准（生效即锁）```
  - `description`（逐字原文）：（无此键）
- `id` = `w2bc_eff_opt2`
  - `label`（逐字原文）：```乙：需改（Other 注明）```
  - `description`（逐字原文）：（无此键）
- `id` = `w2bc_eff_opt3`
  - `label`（逐字原文）：```丙：暂缓```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `ad5`

- `header`（原文照录）：`AD-5·q21 重名`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
AD-5：q21 之 q_id 跨面重名（v1.1 event 21 有语料 vs S4 冻结面 idx 1 空语料）——下游单键引用二义如何处置？
```

`options`（逐字原文，共 3 项）：

- `id` = `ad5_opt1`
  - `label`（逐字原文）：```甲：维持·登记即足（下游引用须带面域限定）```
  - `description`（逐字原文）：（无此键）
- `id` = `ad5_opt2`
  - `label`（逐字原文）：```乙：另立引用规范（另派拟制草案）```
  - `description`（逐字原文）：（无此键）
- `id` = `ad5_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `e4_type`

- `header`（原文照录）：`E-4·类型确认`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-4 轴二 4 件之类型判定确认：q10 之新层首现早于 V3 既有层（层被前插），4 件层集合皆不等——维持判 T1，或将「前插」另立一类？
```

`options`（逐字原文，共 3 项）：

- `id` = `e4_type_opt1`
  - `label`（逐字原文）：```甲：维持 T1（层集合不等·0 另立）```
  - `description`（逐字原文）：（无此键）
- `id` = `e4_type_opt2`
  - `label`（逐字原文）：```乙：另立「前插」类（须改词表——另议）```
  - `description`（逐字原文）：（无此键）
- `id` = `e4_type_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_e88ff9f69f669b1a50fe8b83","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"e4b_merge","question":"E-4 轴二（v1.1 基础面 4 件位移，已实跑在册）是否并入面 II（24→28）？","selectionMode":"single","options":[{"id":"e4b_merge_opt1","label":"甲：不并入——面 II 维持 24 件；v1.1 4 件另案在册（现状）"},{"id":"e4b_merge_opt2","label":"乙：并入——面 II 扩为 28 件（须另立登记）"},{"id":"e4b_merge_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-4b·轴二并入"},{"id":"w2bc_eff","question":"W-2 落实件之两项候核准——W-2b「状态轴不构成第 5 类」之生效＋W-2c 勘误件（17→12）之生效——核准否？","selectionMode":"single","options":[{"id":"w2bc_eff_opt1","label":"甲：两项核准（生效即锁）"},{"id":"w2bc_eff_opt2","label":"乙：需改（Other 注明）"},{"id":"w2bc_eff_opt3","label":"丙：暂缓"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"W-2b/c 生效"},{"id":"ad5","question":"AD-5：q21 之 q_id 跨面重名（v1.1 event 21 有语料 vs S4 冻结面 idx 1 空语料）——下游单键引用二义如何处置？","selectionMode":"single","options":[{"id":"ad5_opt1","label":"甲：维持·登记即足（下游引用须带面域限定）"},{"id":"ad5_opt2","label":"乙：另立引用规范（另派拟制草案）"},{"id":"ad5_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"AD-5·q21 重名"},{"id":"e4_type","question":"E-4 轴二 4 件之类型判定确认：q10 之新层首现早于 V3 既有层（层被前插），4 件层集合皆不等——维持判 T1，或将「前插」另立一类？","selectionMode":"single","options":[{"id":"e4_type_opt1","label":"甲：维持 T1（层集合不等·0 另立）"},{"id":"e4_type_opt2","label":"乙：另立「前插」类（须改词表——另议）"},{"id":"e4_type_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-4·类型确认"}],"status":"pending","createdAt":1791616335412,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_9c24419c-c794-4c7c-8ce0-b060778abb3a","toolCallId":"call_00_ay4wb1MXmOspYDTDdadd0647"},"title":"轮50 · E-4 收口与生效四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_e88ff9f69f669b1a50fe8b83","answers":[{"stepId":"e4b_merge","selectedOptionIds":["e4b_merge_opt3"],"selectedOther":false},{"stepId":"w2bc_eff","selectedOptionIds":["w2bc_eff_opt1"],"selectedOther":false},{"stepId":"ad5","selectedOptionIds":["ad5_opt3"],"selectedOther":false},{"stepId":"e4_type","selectedOptionIds":["e4_type_opt3"],"selectedOther":false}],"submittedAt":1791617477236}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `e4b_merge`：`selectedOptionIds` = ["e4b_merge_opt3"]；`selectedOther` = false
答 2／4 — `stepId` = `w2bc_eff`：`selectedOptionIds` = ["w2bc_eff_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `ad5`：`selectedOptionIds` = ["ad5_opt3"]；`selectedOther` = false
答 4／4 — `stepId` = `e4_type`：`selectedOptionIds` = ["e4_type_opt3"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `e4b_merge`：`e4b_merge_opt3` → 选项字面（逐字）= `丙：另议`
- 答 2／4 — `w2bc_eff`：`w2bc_eff_opt1` → 选项字面（逐字）= `甲：两项核准（生效即锁）`
- 答 3／4 — `ad5`：`ad5_opt3` → 选项字面（逐字）= `丙：另议`
- 答 4／4 — `e4_type`：`e4_type_opt3` → 选项字面（逐字）= `丙：另议`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 12 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

## 1 · 逐卡转录（指定目标 4 件，按 `created_at` 升序）

### 03 · `ask_44319d9e9bbc83311ddd034c` · 轮51（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮51 · G5 启动与两层方案四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_44319d9e9bbc83311ddd034c
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮51 · G5 启动与两层方案四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName             = mavis
requester.runId                 = turn_e8b94df0-960c-4530-811b-cb6f2cc151ef
requester.sessionId             = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId            = call_00_NPwFnfSw599PPE81j18h2559
request_json.createdAt (epoch ms)= 1791617641915   → 2026-10-10 15:34:01.915 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791617641915
created_at (CST 换算)            = 2026-10-10 15:34:01.915 +0800
answered_at (epoch ms)         = 1791619000794
answered_at (CST 换算)           = 2026-10-10 15:56:40.794 +0800
reply_payload.submittedAt(epoch ms)= 1791619000794   → 2026-10-10 15:56:40.794 +0800
injected_at (epoch ms)         = 1791619000878
injected_at (CST 换算)           = 2026-10-10 15:56:40.878 +0800
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `eg5_spec`

- `header`（原文照录）：`E-G5-①·规格核准`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-G5-① 裁后落实：甲案「另开重判面」规格草案（3015f2481df1 §6·条件已满足而激活）——核准启动？
```

`options`（逐字原文，共 3 项）：

- `id` = `eg5_spec_opt1`
  - `label`（逐字原文）：```甲：核准启动（开重判面·按规格草案）```
  - `description`（逐字原文）：（无此键）
- `id` = `eg5_spec_opt2`
  - `label`（逐字原文）：```乙：暂缓（候其他收口）```
  - `description`（逐字原文）：（无此键）
- `id` = `eg5_spec_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `eg5_x23`

- `header`（原文照录）：`E-G5-①·配套`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-G5-① 配套两草案：X-2（不修订 C 字面·以效力裁作登记）＋X-3（重判预登记增列「A′ 地板饱和」限制＋替代触发量口径）——按草案核准？
```

`options`（逐字原文，共 3 项）：

- `id` = `eg5_x23_opt1`
  - `label`（逐字原文）：```甲：两项按草案核准```
  - `description`（逐字原文）：（无此键）
- `id` = `eg5_x23_opt2`
  - `label`（逐字原文）：```乙：需改（Other 逐项注明）```
  - `description`（逐字原文）：（无此键）
- `id` = `eg5_x23_opt3`
  - `label`（逐字原文）：```丙：逐项细裁```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `e6a_plan`

- `header`（原文照录）：`E-6a·两层方案`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
N-01/N-08 修订件之方案择定（E-6a）：三案（甲推荐：层级分层双层并存／乙：收编附注／丙：新称谓）采何案？
```

`options`（逐字原文，共 3 项）：

- `id` = `e6a_plan_opt1`
  - `label`（逐字原文）：```甲：甲（推荐）—层级分层·双层并存（含 R-2a/R-2b）```
  - `description`（逐字原文）：（无此键）
- `id` = `e6a_plan_opt2`
  - `label`（逐字原文）：```乙：乙—收编为 af 档之附注·历史面```
  - `description`（逐字原文）：（无此键）
- `id` = `e6a_plan_opt3`
  - `label`（逐字原文）：```丙：丙—另给新层级称谓```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `th19_x1`

- `header`（原文照录）：`TH-v3-19·出口①`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
TH-v3-19 出口①：豁免读法之「应然解释语」是否溯及 v3 面（两面判读面结论已证一致·差别仅存解释语）？
```

`options`（逐字原文，共 3 项）：

- `id` = `th19_x1_opt1`
  - `label`（逐字原文）：```甲：0 溯及（v3 面字段维持落盘时口径·另注豁免后口径）```
  - `description`（逐字原文）：（无此键）
- `id` = `th19_x1_opt2`
  - `label`（逐字原文）：```乙：溯及（v3 面字段按豁免后口径重述）```
  - `description`（逐字原文）：（无此键）
- `id` = `th19_x1_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_44319d9e9bbc83311ddd034c","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"eg5_spec","question":"E-G5-① 裁后落实：甲案「另开重判面」规格草案（3015f2481df1 §6·条件已满足而激活）——核准启动？","selectionMode":"single","options":[{"id":"eg5_spec_opt1","label":"甲：核准启动（开重判面·按规格草案）"},{"id":"eg5_spec_opt2","label":"乙：暂缓（候其他收口）"},{"id":"eg5_spec_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-G5-①·规格核准"},{"id":"eg5_x23","question":"E-G5-① 配套两草案：X-2（不修订 C 字面·以效力裁作登记）＋X-3（重判预登记增列「A′ 地板饱和」限制＋替代触发量口径）——按草案核准？","selectionMode":"single","options":[{"id":"eg5_x23_opt1","label":"甲：两项按草案核准"},{"id":"eg5_x23_opt2","label":"乙：需改（Other 逐项注明）"},{"id":"eg5_x23_opt3","label":"丙：逐项细裁"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-G5-①·配套"},{"id":"e6a_plan","question":"N-01/N-08 修订件之方案择定（E-6a）：三案（甲推荐：层级分层双层并存／乙：收编附注／丙：新称谓）采何案？","selectionMode":"single","options":[{"id":"e6a_plan_opt1","label":"甲：甲（推荐）—层级分层·双层并存（含 R-2a/R-2b）"},{"id":"e6a_plan_opt2","label":"乙：乙—收编为 af 档之附注·历史面"},{"id":"e6a_plan_opt3","label":"丙：丙—另给新层级称谓"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-6a·两层方案"},{"id":"th19_x1","question":"TH-v3-19 出口①：豁免读法之「应然解释语」是否溯及 v3 面（两面判读面结论已证一致·差别仅存解释语）？","selectionMode":"single","options":[{"id":"th19_x1_opt1","label":"甲：0 溯及（v3 面字段维持落盘时口径·另注豁免后口径）"},{"id":"th19_x1_opt2","label":"乙：溯及（v3 面字段按豁免后口径重述）"},{"id":"th19_x1_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"TH-v3-19·出口①"}],"status":"pending","createdAt":1791617641915,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_e8b94df0-960c-4530-811b-cb6f2cc151ef","toolCallId":"call_00_NPwFnfSw599PPE81j18h2559"},"title":"轮51 · G5 启动与两层方案四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_44319d9e9bbc83311ddd034c","answers":[{"stepId":"eg5_spec","selectedOptionIds":["eg5_spec_opt1"],"selectedOther":false},{"stepId":"eg5_x23","selectedOptionIds":["eg5_x23_opt1"],"selectedOther":false},{"stepId":"e6a_plan","selectedOptionIds":["e6a_plan_opt1"],"selectedOther":false},{"stepId":"th19_x1","selectedOptionIds":["th19_x1_opt1"],"selectedOther":false}],"submittedAt":1791619000794}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `eg5_spec`：`selectedOptionIds` = ["eg5_spec_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `eg5_x23`：`selectedOptionIds` = ["eg5_x23_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `e6a_plan`：`selectedOptionIds` = ["e6a_plan_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `th19_x1`：`selectedOptionIds` = ["th19_x1_opt1"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `eg5_spec`：`eg5_spec_opt1` → 选项字面（逐字）= `甲：核准启动（开重判面·按规格草案）`
- 答 2／4 — `eg5_x23`：`eg5_x23_opt1` → 选项字面（逐字）= `甲：两项按草案核准`
- 答 3／4 — `e6a_plan`：`e6a_plan_opt1` → 选项字面（逐字）= `甲：甲（推荐）—层级分层·双层并存（含 R-2a/R-2b）`
- 答 4／4 — `th19_x1`：`th19_x1_opt1` → 选项字面（逐字）= `甲：0 溯及（v3 面字段维持落盘时口径·另注豁免后口径）`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 12 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

## 1 · 逐卡转录（指定目标 4 件，按 `created_at` 升序）

### 04 · `ask_fd3083aa317b7b3397f85f7d` · 轮52（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮52 · E-4 收口与称谓四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_fd3083aa317b7b3397f85f7d
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮52 · E-4 收口与称谓四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName             = mavis
requester.runId                 = turn_75baf36a-c403-43f3-a8ed-897a197482ea
requester.sessionId             = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId            = call_00_C02Bm1Z1KOSYZPGbFMTF1043
request_json.createdAt (epoch ms)= 1791619170250   → 2026-10-10 15:59:30.250 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791619170250
created_at (CST 换算)            = 2026-10-10 15:59:30.250 +0800
answered_at (epoch ms)         = 1791620108215
answered_at (CST 换算)           = 2026-10-10 16:15:08.215 +0800
reply_payload.submittedAt(epoch ms)= 1791620108215   → 2026-10-10 16:15:08.215 +0800
injected_at (epoch ms)         = 1791620119403
injected_at (CST 换算)           = 2026-10-10 16:15:19.403 +0800
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `e4b_a`

- `header`（原文照录）：`E-4b-a·终裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-4b 终裁（判断件倾向丙）：不并入面 II（维持 24）＋另名件载面域声明并陈？
```

`options`（逐字原文，共 3 项）：

- `id` = `e4b_a_opt1`
  - `label`（逐字原文）：```甲：按丙案（不并入＋另名面域声明件）```
  - `description`（逐字原文）：（无此键）
- `id` = `e4b_a_opt2`
  - `label`（逐字原文）：```乙：并入（24→28）```
  - `description`（逐字原文）：（无此键）
- `id` = `e4b_a_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `ad5_a`

- `header`（原文照录）：`AD-5a·终裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
AD-5 终裁（判断件倾向丙）：维持登记＋扩范围至 6 组（q17/q21/q27＋面内 3 组）＋loader 归因——另名件承载？
```

`options`（逐字原文，共 3 项）：

- `id` = `ad5_a_opt1`
  - `label`（逐字原文）：```甲：按丙案（维持登记＋扩 6 组＋loader 归因·另名件）```
  - `description`（逐字原文）：（无此键）
- `id` = `ad5_a_opt2`
  - `label`（逐字原文）：```乙：另立引用规范```
  - `description`（逐字原文）：（无此键）
- `id` = `ad5_a_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `type_a`

- `header`（原文照录）：`TYPE-a·终裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
类型确认终裁（判断件倾向甲）：维持 T1（前插与 T1 不正交·立第 5 类将使封闭词表不再是划分）？
```

`options`（逐字原文，共 3 项）：

- `id` = `type_a_opt1`
  - `label`（逐字原文）：```甲：按甲案（维持 T1·前插作属性留痕·4 类词表不扩充）```
  - `description`（逐字原文）：（无此键）
- `id` = `type_a_opt2`
  - `label`（逐字原文）：```乙：立「前插」类（须改词表）```
  - `description`（逐字原文）：（无此键）
- `id` = `type_a_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `e6b_name`

- `header`（原文照录）：`E-6b·称谓`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-6b：层级称谓定名（代立草案：「终判档位层／读数取值层」均取自盘上既有字面·0 新造）——按草案核准？
```

`options`（逐字原文，共 3 项）：

- `id` = `e6b_name_opt1`
  - `label`（逐字原文）：```甲：按草案核准（「终判档位层／读数取值层」生效）```
  - `description`（逐字原文）：（无此键）
- `id` = `e6b_name_opt2`
  - `label`（逐字原文）：```乙：需改（Other 注明）```
  - `description`（逐字原文）：（无此键）
- `id` = `e6b_name_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_fd3083aa317b7b3397f85f7d","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"e4b_a","question":"E-4b 终裁（判断件倾向丙）：不并入面 II（维持 24）＋另名件载面域声明并陈？","selectionMode":"single","options":[{"id":"e4b_a_opt1","label":"甲：按丙案（不并入＋另名面域声明件）"},{"id":"e4b_a_opt2","label":"乙：并入（24→28）"},{"id":"e4b_a_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-4b-a·终裁"},{"id":"ad5_a","question":"AD-5 终裁（判断件倾向丙）：维持登记＋扩范围至 6 组（q17/q21/q27＋面内 3 组）＋loader 归因——另名件承载？","selectionMode":"single","options":[{"id":"ad5_a_opt1","label":"甲：按丙案（维持登记＋扩 6 组＋loader 归因·另名件）"},{"id":"ad5_a_opt2","label":"乙：另立引用规范"},{"id":"ad5_a_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"AD-5a·终裁"},{"id":"type_a","question":"类型确认终裁（判断件倾向甲）：维持 T1（前插与 T1 不正交·立第 5 类将使封闭词表不再是划分）？","selectionMode":"single","options":[{"id":"type_a_opt1","label":"甲：按甲案（维持 T1·前插作属性留痕·4 类词表不扩充）"},{"id":"type_a_opt2","label":"乙：立「前插」类（须改词表）"},{"id":"type_a_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"TYPE-a·终裁"},{"id":"e6b_name","question":"E-6b：层级称谓定名（代立草案：「终判档位层／读数取值层」均取自盘上既有字面·0 新造）——按草案核准？","selectionMode":"single","options":[{"id":"e6b_name_opt1","label":"甲：按草案核准（「终判档位层／读数取值层」生效）"},{"id":"e6b_name_opt2","label":"乙：需改（Other 注明）"},{"id":"e6b_name_opt3","label":"丙：另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-6b·称谓"}],"status":"pending","createdAt":1791619170250,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_75baf36a-c403-43f3-a8ed-897a197482ea","toolCallId":"call_00_C02Bm1Z1KOSYZPGbFMTF1043"},"title":"轮52 · E-4 收口与称谓四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_fd3083aa317b7b3397f85f7d","answers":[{"stepId":"e4b_a","selectedOptionIds":["e4b_a_opt1"],"selectedOther":false},{"stepId":"ad5_a","selectedOptionIds":["ad5_a_opt1"],"selectedOther":false},{"stepId":"type_a","selectedOptionIds":["type_a_opt1"],"selectedOther":false},{"stepId":"e6b_name","selectedOptionIds":["e6b_name_opt1"],"selectedOther":false}],"submittedAt":1791620108215}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `e4b_a`：`selectedOptionIds` = ["e4b_a_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `ad5_a`：`selectedOptionIds` = ["ad5_a_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `type_a`：`selectedOptionIds` = ["type_a_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `e6b_name`：`selectedOptionIds` = ["e6b_name_opt1"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `e4b_a`：`e4b_a_opt1` → 选项字面（逐字）= `甲：按丙案（不并入＋另名面域声明件）`
- 答 2／4 — `ad5_a`：`ad5_a_opt1` → 选项字面（逐字）= `甲：按丙案（维持登记＋扩 6 组＋loader 归因·另名件）`
- 答 3／4 — `type_a`：`type_a_opt1` → 选项字面（逐字）= `甲：按甲案（维持 T1·前插作属性留痕·4 类词表不扩充）`
- 答 4／4 — `e6b_name`：`e6b_name_opt1` → 选项字面（逐字）= `甲：按草案核准（「终判档位层／读数取值层」生效）`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 12 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

## 2 · 对账（**0 漏录 · 0 重复 · 0 掩饰**）

| 序 | `request_id` | 轮 | 批次口径 | `created_at`（CST） | `answered_at`（CST） | `status` | 前七批是否已含 |
|---:|---|---|---|---|---|---|---|
| 1 | `ask_37de1297db68c580a2795fd5` | 轮49 | 续录（第七批之后新增轮次） | 2026-10-10 14:56:14.975 +0800 | 2026-10-10 15:09:26.317 +0800 | `answered` | ⛔ 未含（实测·前七批均无此 id 之正文收录） |
| 2 | `ask_e88ff9f69f669b1a50fe8b83` | 轮50 | 续录（第七批之后新增轮次） | 2026-10-10 15:12:15.412 +0800 | 2026-10-10 15:31:17.236 +0800 | `answered` | ⛔ 未含（实测·前七批均无此 id 之正文收录） |
| 3 | `ask_44319d9e9bbc83311ddd034c` | 轮51 | 续录（第七批之后新增轮次） | 2026-10-10 15:34:01.915 +0800 | 2026-10-10 15:56:40.794 +0800 | `answered` | ⛔ 未含（实测·前七批均无此 id 之正文收录） |
| 4 | `ask_fd3083aa317b7b3397f85f7d` | 轮52 | 续录（第七批之后新增轮次） | 2026-10-10 15:59:30.250 +0800 | 2026-10-10 16:15:08.215 +0800 | `answered` | ⛔ 未含（实测·前七批均无此 id 之正文收录） |

⇒ **4／4 件转录完成、0 失败**；逐字转录之 `steps` 合计 **16** 步、`options` 合计 **46** 项、`answers` 合计 **16** 条。

### 2.1 本批版本号核定（实测）

盘上存在七件 `_questionnaire_cards_intake_register*` 登记件（`_supplement_6_` 已于本棒之前存在）；故取**首个未用序号** ＝ **`_supplement_7_`。落前实测：`Test-Path` ＝ **False**；仓内 `*supplement_7*` glob 命中 **0**。

### 2.2 本件之边界（诚实交代）

1. **本件非全表应录全集** —— 系派工指定之 4 张目标卡（轮49～轮52）之逐字转录；⛔ **0 声称已覆盖本轮新建之全部卡**。实测全表 **423** 行，本件仅转录其中 4 行；其余额 **419** 行**未**在本件应录面。
2. **轮35～轮48 已由前七批收录** —— 实测该十四张卡已完整收录于 `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md`（SHA-12 `95ba771fa760`）及其之前各批之 §1；本件⛔ **0 重复转录**，⛔ **0 回改**该件。
3. **本件 0 核他件之内部正确性** —— ⛔ 0 复核前七批登记件之内容；仅核其**存在性与 SHA-12**（本棒当轮实测，见 §3.3）。
4. **题面之实质裁定 0 预判** —— 本件仅照录 PI 之所选；⛔ 0 判读其所选之对错、⛔ 0 预判后续处置。
5. **回指表之边界** —— §1 各卡「答文回指」小表仅为同一行内 `selectedOptionIds` → `options[].label` 之**机械字面对取**，未作任何判读；若与逐字原文有冲突，以**原文**为准。
6. **空 `selectedOptionIds` 之呈现** —— 本批 **0** 答走 Other 通道（`selectedOptionIds` ＝ `[]` 且 `selectedOther` ＝ `true` 者）；本件不设 `otherText` 呈现行，亦⛔ 0 替任何答补填选项 id。

### 2.3 Other 通道答文一览（机械展开 · 逐字照录 `otherText`）

| 轮 | `stepId` | `otherText`（逐字原文） |
|---|---|---|
| — | — | **本批 0 条**（四卡 16 答全数走选项通道，`selectedOther` 全为 `false`、无 `otherText`） |

### 2.4 差异登记

**对派工转录清单之字面差异：0。** 派工仅指定 4 个 `request_id`（未附任何预期答文字面），故本件之核对面为「4 个 id 之命中与逐字保真」：实测命中 **4／4**，每卡 `steps`／`options`／`answers` 三计数与库内一致（见 §1 各卡计数表），转录失败项合计 **0**。

**与既有登记件之差异登记：**

1. **四卡均为第七批之后新增轮次** —— 轮49～轮52 之 `created_at` 落在第七批读时点（第七批所录最晚一轮为轮48，`created_at` ＝ 2026-10-10 14:42:43.930 +0800）之后，本件为**首次逐字收录**；⛔ 0 与任何既有登记件重复。
2. **全表行数之活库变动** —— 第七批落册读时点 419 行 → 本批读时点 **423** 行（`answered` 416→420、`pending` 1→1、`superseded` 2→2）；其差 4 行与本批四卡之建卡相对应，另建之他卡（若存在）**⛔ 0 转录**。
3. **本批 0 条 Other 通道** —— 与第七批（7 条 Other）不同：四卡 16 答全数走选项通道；此为**转录事实**，⛔ 非判读。
4. **四卡 `status` 双读法** —— 表列 `status` 全为 `answered`，而 `request_json` 内嵌 `status` 全为 `pending`（建卡时快照）；本件二者**并列照录**（沿前七批体例），⛔ 0 择一改写。

---

## 3 · 0 回改确认 ＋ 落盘自证

### 3.1 0 回改确认

| 项 | 确认 |
|---|---|
| 既有件写动作 | **0** —— ⛔ 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除任何既有件（**含前七批落册登记件**） |
| 本棒写动作 | **新增 1 件**（本件）＋ 暂存区 4 件中间脚本／导出（`.tmp/`，非交付件，已于交付前清理） |
| 运行时库 | **只读**（`mode=ro`）—— 0 写入、0 修改、0 建表、0 提交 |
| 会话消息面 | **只读**（仅 `messages.jsonl` 检索）—— 0 写入 |
| 本件交付前之自身更正 | **0 处** —— 本件由程序化生成、一次性落盘；⛔ 0 交付前就地更正；逐字转录之库内字面（§1 全部题面与答文）**0 处更动** |
| 归档禁区 | **未触及** —— ⛔ 0 访问／0 读取 `〔归档件引用·未上传:〔归档区〕〕` |

### 3.2 落前撞名实测

| 项 | 实测结果 |
|---|---|
| 落前撞名 | `Test-Path 'results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md'` ＝ **False**；仓内 `*supplement_7*` glob 命中 **0** ⇒ ✅ **新名新建 · 0 覆写 · 0 重名** |

### 3.3 输入件指纹（本棒 `SHA256` **当轮实测** · **0 沿用他件登记值**）

| 件 | SHA-12 | 字节 |
|---|---|---:|
| `results/_questionnaire_cards_intake_register_2026_10_09.md` | `d917180db36f` | 442288 |
| `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `193386b9f23c` | 72199 |
| `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `dc43e3cb7610` | 262542 |
| `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | `11681f0ad861` | 67225 |
| `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | `d6ff041a9df9` | 116506 |
| `results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | `edb57308170d` | 77189 |
| `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | `95ba771fa760` | 106453 |

### 3.4 边界声明 · 0 编造

- **0 编造 PI 立场**：本件所载四卡之题面与答文**均取自运行时库原件**（程序化逐字转录）；⛔ **0 推测** PI 对任何一项之将来处置。
- **0 冒充他棒**：本件由 **doc-writer** 出件（分支会话 `mvs_6f4c99f0aebc4da3a76ac9373e2c769e`）；⛔ 0 顶任何他方名头。
- **0 网络 · 0 skill · 0 LLM · 0 实验**：本棒仅本机只读取证 ＋ 1 件新建。
- **R4**：⛔ 0 读 key、⛔ 0 读 `.env`、⛔ 0 落盘凭据、**key 永不明文**。
- **不编造专有名词／文献号／定理名**：本件**0 引用任何外部定理、文献或标准**。

**本件状态**：✅ **4 卡逐字转录完成 · 0 失败 · 0 判读 · 0 代裁 · 0 回改** ｜ ⛔ 0 网络 · 0 skill · 0 LLM
