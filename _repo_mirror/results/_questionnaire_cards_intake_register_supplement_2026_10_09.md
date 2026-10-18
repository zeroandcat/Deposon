# 裁卡原件批量落册（第二批·追补）· questionnaire 原件逐字转录（2026-10-09）

## 文件头注

- **件名**：`results/_questionnaire_cards_intake_register_supplement_2026_10_09.md`
- **落册日期**：2026-10-09（CST）
- **件系**：第一批登记件 `results/_questionnaire_cards_intake_register_2026_10_09.md`（SHA-12 `d917180db36f`，读取时点 2026-10-09 18:08 前后）之**追补落册（第二批）**。⛔ 0 编辑／覆写／修改第一批登记件；⛔ 0 重复转录其已收录之卡（对账见 §2）。
- **来源**：运行时库 `〔本机用户目录〕/.minimax/v2/sqlite/runtime-state.sqlite`，表 `questionnaire_requests`。本轮以 `sqlite3.connect("file:...?mode=ro", uri=True)` **只读实测**（0 写入、0 修改、0 建表、0 提交）。
- **窗口口径（第一批截止 ＋ 本批起讫）**：
  - **第一批窗口**：`created_at >= 2026-10-08 00:00:00 +0800`（epoch ms `1791388800000`）；第一批读取时点（库 mtime `2026-10-09 18:08:26.683 +0800`）该窗口共 `34` 件，其中最后一件为 `ask_33471ffa5c68d4bbd8571e40`（`2026-10-09 17:24:20.757 +0800`）＝**第一批截止**。
  - **本批窗口**：`created_at >= 2026-10-09 17:00:00 +0800`（epoch ms `1791536400000`）——起于第一批截止之前（含重叠区，专用于对账），迄于**本件读得时点**实测末件 `ask_6db74cbbb4c70cf8c0c6cc1e`（`2026-10-09 21:23:34.280 +0800`）。
  - **本批应录**＝本窗口内**第一批未含**者（逐字全量收录）＋第一批已含者（仅列对账行，0 重复转录）。
- **转录纪律**：**逐字、0 省略、0 解释、0 判读**。题面（`request_json.steps` 之 id／header／question／options）与答文（`reply_payload` 全文，含 `selectedOther`／`otherText`）均按库中原文照录；本件**不含**任何分析、结论、裁断或建议。
- **效力声明**：本件**仅转录**。⛔ **0 当「裁录」**；⛔ **0 代替任何既有登记件的裁录效力**。本件不产生、不替代、不撤销任何裁决；一切裁断效力仍以其原登记件／生效件为准。
- **命名合规**：`_主题_日期` 体例；⛔ 0 带 V-阶段前缀（0 `_v3_`／`_v4_`／`_v5_`）。
- **编制**：worker（受派棒）；**编制方式**：`〔本机路径〕/Python314/python.exe` 只读抽取 → 程序化逐字转录（⛔ 0 人工改写任何字面）。

## 0 · 本轮读取基准（provenance）

- 库文件大小（读取时点）：`474656768` bytes
- 库文件 mtime（读取时点，CST）：`2026-10-09 21:28:02.311 +0800`
- 表 `questionnaire_requests` 总行数（全表，本轮实测）：`373`
- 全表 status 分布：`answered`=371；`pending`=1；`superseded`=1
- 抽取口径：`SELECT ... FROM questionnaire_requests WHERE created_at >= 1791536400000 ORDER BY created_at ASC, request_id ASC`（⛔ 0 LIMIT）
- 窗口下界换算：`created_at >= 1791536400000` ≡ `2026-10-09 17:00:00 +0800`（epoch 毫秒）
- 时间换算口径：`created_at`／`answered_at`／`submittedAt`／`createdAt` 均为 **INTEGER epoch 毫秒**，本件统一换算为 **CST（UTC+8）** 呈现，原值同时照录。
- 字段长度口径：同时给出**字符数**（Unicode 码位，Python `len`）与**字节数**（UTF-8 编码后 `len`）。
- 值形口径：SQL／JSON 空值一律呈为 `NULL`；布尔值一律呈为 JSON 小写字面 `true`／`false`（沿第一批体例）。
- 计数增量（对账用）：全表行数自第一批读取时点的 `368` 增至本轮实测 `373`（+`5`）；第一批窗口（`created_at >= 1791388800000`）本轮实测 `39` 件（第一批实录 `34` ＋ 新增 `5`）。

## 1 · 逐卡转录（本批窗口内第一批未含者，共 5 件，按 `created_at` 升序）

范围口径：本批应录＝本窗口 10 件 − 第一批已含 5 件 ＝ **5 件**（即本节实录全集，无重复计）。

### 01 · `ask_bd9193285d3d02c0dcd98f26` · 新增（第一批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> S4 判档·候呈四题（收口前置）

**卡级元数据（原文照录）**

```text
request_id                     = ask_bd9193285d3d02c0dcd98f26
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = S4 判档·候呈四题（收口前置）
presentation.allowBackNavigation = true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_32987ebc-a1dc-4b93-b173-258bb899f24d
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_eoR8gVacb5wJnUzCtK1x2543
request_json.createdAt (epoch ms) = 1791550327880   → 2026-10-09 20:52:07.880 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791550327880
created_at (CST 换算)          = 2026-10-09 20:52:07.880 +0800
answered_at (epoch ms)         = 1791550449897
answered_at (CST 换算)         = 2026-10-09 20:54:09.897 +0800
reply_payload.submittedAt(epoch ms) = 1791550449897   → 2026-10-09 20:54:09.897 +0800
injected_at (epoch ms)         = 1791550449972
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `s4_26`

- `header`（原文照录）：`held-out 记录项`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 判档候呈①：held-out「26」（逐格 floor(0.30·n) 之和）现为必报记录项（不达 50 不构成不达标）。移出合取面后如何处置？（含 P-S4-1 合取面状态；「择一」面已消解、「重立」面候 C-1 细目。K-4-1/-2 现为 KD 不可判；seed 42 分层抽样盘上 0 执行。）
```

`options`（逐字原文，共 3 项）：

- `id` = `s4_26_opt1`
  - `label`（逐字原文）：```维持记录项——26 继续必报、0 参与判定；抽样暂不执行（-1/-2 维持 KD）```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_26_opt2`
  - `label`（逐字原文）：```授权执行分层抽样（seed 42）——worker 执行、以实测面更新 26；-1/-2 候实测重判```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_26_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒出建议件后再裁```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `s4_ratio`

- `header`（原文照录）：`留出比例口径`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 判档候呈②：「留出比例」计量口径二读并存——名义 0.30（T-5 登记式）对聚合读法（floor 和 26/N，指向 FAIL）。该口径决定 §5.2 之 KD 与 FAIL 分歧归属（关乎 -1 档位；两读均非 PASS）。以何为准？
```

`options`（逐字原文，共 4 项）：

- `id` = `s4_ratio_opt1`
  - `label`（逐字原文）：```名义 0.30 为准——维持现读数；-1 维持 KD、聚合读法维持「已识别·未采信」```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_ratio_opt2`
  - `label`（逐字原文）：```聚合读法（26/N）为准——采信 R-AGG；KD 与 FAIL 归属随之裁```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_ratio_opt3`
  - `label`（逐字原文）：```双读并陈——两读并列、0 单择；档位维持 KD、分歧挂册```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_ratio_opt4`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `s4_freeze`

- `header`（原文照录）：`S4 冻结面`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 判档候呈③：S4 substrate 冻结面登记仍为 167 面（G5/ARR-3）；终 N 面读数（179/171）未充任何冻结终值。是否就 179 面正式重冻？
```

`options`（逐字原文，共 3 项）：

- `id` = `s4_freeze_opt1`
  - `label`（逐字原文）：```维持 167 登记、暂不重冻——179/171 继续为未冻结面读数```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_freeze_opt2`
  - `label`（逐字原文）：```就 179 面正式重冻——派 worker 执行；冻结面登记随动更新```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_freeze_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `s4_domain`

- `header`（原文照录）：`K-V3S-4-2 域`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 判档候呈④：「分母 171」域裁（K-4-3 已适用）是否及于 K-V3S-4-2 之 substrate 腿？现读数面 179（+29）；若及于则 171（+21）。两域均满足 ≥150，但①之满足性具域敏感性；VK 本件 0 代裁扩域。
```

`options`（逐字原文，共 4 项）：

- `id` = `s4_domain_opt1`
  - `label`（逐字原文）：```不及于——-2 substrate 腿维持 179 域（+29）```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_domain_opt2`
  - `label`（逐字原文）：```及于——以 171 域重读（+21，与 K-4-3 主读域统一）```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_domain_opt3`
  - `label`（逐字原文）：```双读并陈——两域并列、0 单择```
  - `description`（逐字原文）：（无此键）
- `id` = `s4_domain_opt4`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_bd9193285d3d02c0dcd98f26","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"s4_26","question":"S4 判档候呈①：held-out「26」（逐格 floor(0.30·n) 之和）现为必报记录项（不达 50 不构成不达标）。移出合取面后如何处置？（含 P-S4-1 合取面状态；「择一」面已消解、「重立」面候 C-1 细目。K-4-1/-2 现为 KD 不可判；seed 42 分层抽样盘上 0 执行。）","selectionMode":"single","options":[{"id":"s4_26_opt1","label":"维持记录项——26 继续必报、0 参与判定；抽样暂不执行（-1/-2 维持 KD）"},{"id":"s4_26_opt2","label":"授权执行分层抽样（seed 42）——worker 执行、以实测面更新 26；-1/-2 候实测重判"},{"id":"s4_26_opt3","label":"另议——派独立判断棒出建议件后再裁"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"held-out 记录项"},{"id":"s4_ratio","question":"S4 判档候呈②：「留出比例」计量口径二读并存——名义 0.30（T-5 登记式）对聚合读法（floor 和 26/N，指向 FAIL）。该口径决定 §5.2 之 KD 与 FAIL 分歧归属（关乎 -1 档位；两读均非 PASS）。以何为准？","selectionMode":"single","options":[{"id":"s4_ratio_opt1","label":"名义 0.30 为准——维持现读数；-1 维持 KD、聚合读法维持「已识别·未采信」"},{"id":"s4_ratio_opt2","label":"聚合读法（26/N）为准——采信 R-AGG；KD 与 FAIL 归属随之裁"},{"id":"s4_ratio_opt3","label":"双读并陈——两读并列、0 单择；档位维持 KD、分歧挂册"},{"id":"s4_ratio_opt4","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"留出比例口径"},{"id":"s4_freeze","question":"S4 判档候呈③：S4 substrate 冻结面登记仍为 167 面（G5/ARR-3）；终 N 面读数（179/171）未充任何冻结终值。是否就 179 面正式重冻？","selectionMode":"single","options":[{"id":"s4_freeze_opt1","label":"维持 167 登记、暂不重冻——179/171 继续为未冻结面读数"},{"id":"s4_freeze_opt2","label":"就 179 面正式重冻——派 worker 执行；冻结面登记随动更新"},{"id":"s4_freeze_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"S4 冻结面"},{"id":"s4_domain","question":"S4 判档候呈④：「分母 171」域裁（K-4-3 已适用）是否及于 K-V3S-4-2 之 substrate 腿？现读数面 179（+29）；若及于则 171（+21）。两域均满足 ≥150，但①之满足性具域敏感性；VK 本件 0 代裁扩域。","selectionMode":"single","options":[{"id":"s4_domain_opt1","label":"不及于——-2 substrate 腿维持 179 域（+29）"},{"id":"s4_domain_opt2","label":"及于——以 171 域重读（+21，与 K-4-3 主读域统一）"},{"id":"s4_domain_opt3","label":"双读并陈——两域并列、0 单择"},{"id":"s4_domain_opt4","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"K-V3S-4-2 域"}],"status":"pending","createdAt":1791550327880,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_32987ebc-a1dc-4b93-b173-258bb899f24d","toolCallId":"call_00_eoR8gVacb5wJnUzCtK1x2543"},"title":"S4 判档·候呈四题（收口前置）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_bd9193285d3d02c0dcd98f26","answers":[{"stepId":"s4_26","selectedOptionIds":["s4_26_opt2"],"selectedOther":false},{"stepId":"s4_ratio","selectedOptionIds":["s4_ratio_opt2"],"selectedOther":false},{"stepId":"s4_freeze","selectedOptionIds":["s4_freeze_opt2"],"selectedOther":false},{"stepId":"s4_domain","selectedOptionIds":["s4_domain_opt4"],"selectedOther":false}],"submittedAt":1791550449897}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "s4_26", "selectedOptionIds": ["s4_26_opt2"], "selectedOther": false}
```

- `stepId`：`s4_26`
- `selectedOptionIds`（逐字）：["s4_26_opt2"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `s4_26_opt2` → `label`: ```授权执行分层抽样（seed 42）——worker 执行、以实测面更新 26；-1/-2 候实测重判```

答 2／4 — 原始对象：

```json
{"stepId": "s4_ratio", "selectedOptionIds": ["s4_ratio_opt2"], "selectedOther": false}
```

- `stepId`：`s4_ratio`
- `selectedOptionIds`（逐字）：["s4_ratio_opt2"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `s4_ratio_opt2` → `label`: ```聚合读法（26/N）为准——采信 R-AGG；KD 与 FAIL 归属随之裁```

答 3／4 — 原始对象：

```json
{"stepId": "s4_freeze", "selectedOptionIds": ["s4_freeze_opt2"], "selectedOther": false}
```

- `stepId`：`s4_freeze`
- `selectedOptionIds`（逐字）：["s4_freeze_opt2"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `s4_freeze_opt2` → `label`: ```就 179 面正式重冻——派 worker 执行；冻结面登记随动更新```

答 4／4 — 原始对象：

```json
{"stepId": "s4_domain", "selectedOptionIds": ["s4_domain_opt4"], "selectedOther": false}
```

- `stepId`：`s4_domain`
- `selectedOptionIds`（逐字）：["s4_domain_opt4"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `s4_domain_opt4` → `label`: ```另议——派独立判断棒```

**关键字段长度（实测）**

```text
request_json   字符数 = 2400     字节数(UTF-8) = 3480
reply_payload  字符数 = 428      字节数(UTF-8) = 428
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: s4_26=154; s4_ratio=122; s4_freeze=85; s4_domain=123
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 02 · `ask_92998b73d1b6cb2255391499` · 新增（第一批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> C-1 收束·候呈三题（复核与确认）

**卡级元数据（原文照录）**

```text
request_id                     = ask_92998b73d1b6cb2255391499
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = C-1 收束·候呈三题（复核与确认）
presentation.allowBackNavigation = true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_8b9a92bc-9228-4fe1-a921-f37ca842c24b
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_rMzWfazLAB6sPjOmGyrp8568
request_json.createdAt (epoch ms) = 1791550634334   → 2026-10-09 20:57:14.334 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791550634334
created_at (CST 换算)          = 2026-10-09 20:57:14.334 +0800
answered_at (epoch ms)         = 1791550685214
answered_at (CST 换算)         = 2026-10-09 20:58:05.214 +0800
reply_payload.submittedAt(epoch ms) = 1791550685214   → 2026-10-09 20:58:05.214 +0800
injected_at (epoch ms)         = 1791550685262
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 3 步／8 选项，原文照录）**

**题 1／3** — `id` = `c1_k1`

- `header`（原文照录）：`K-1 复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
C-1 收束·候呈①（K-1 复核）：B/C 两线之 CI 半宽门适用面，独立判断结论＝「条件适用（同门柱·分母口径化）」——B/C 半宽为 0.1100 门柱之 2.27–2.84 倍、S4 构造域内结构性不可达；未另给分母口径化等效门柱前，0.1100 对 B/C 恒不适用（若坚持受门，数值须 PI 另给）。是否核准 K-1？
```

`options`（逐字原文，共 3 项）：

- `id` = `c1_k1_opt1`
  - `label`（逐字原文）：```核准 K-1（条件适用）——B/C 暂免 0.1100 之门；等效门柱留待另给```
  - `description`（逐字原文）：（无此键）
- `id` = `c1_k1_opt2`
  - `label`（逐字原文）：```不核准——B/C 须受门；等效门柱数值我另行给（可于 Other 填数）```
  - `description`（逐字原文）：（无此键）
- `id` = `c1_k1_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒再核```
  - `description`（逐字原文）：（无此键）

**题 2／3** — `id` = `c1_k2`

- `header`（原文照录）：`K-2 复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
C-1 收束·候呈②（K-2 复核）：estimand 归属之独立判断＝「CI 参与判据、只以单侧界与阈值比较之形式参与」——B 取 CI 下界 < 1.00、C 取 CI 上界 > 0.10；点估计仍为准入面；0 改 1.00/0.10 阈值。是否核准？
```

`options`（逐字原文，共 3 项）：

- `id` = `c1_k2_opt1`
  - `label`（逐字原文）：```核准 K-2（单侧界形式）```
  - `description`（逐字原文）：（无此键）
- `id` = `c1_k2_opt2`
  - `label`（逐字原文）：```不核准——维持纯点估计判读（CI 不参与）```
  - `description`（逐字原文）：（无此键）
- `id` = `c1_k2_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒再核```
  - `description`（逐字原文）：（无此键）

**题 3／3** — `id` = `c1_confirm`

- `header`（原文照录）：`免比≠免约束`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
C-1 收束·候呈③：「免比 ≠ 免约束」原则须显式确认——B/C 即使暂免 0.1100 之对比，C-1 之其余约束与判读对 B/C 仍恒适用。是否确认？
```

`options`（逐字原文，共 2 项）：

- `id` = `c1_confirm_opt1`
  - `label`（逐字原文）：```确认——免比≠免约束（C-1 其余约束照旧适用）```
  - `description`（逐字原文）：（无此键）
- `id` = `c1_confirm_opt2`
  - `label`（逐字原文）：```不确认——另议其边界（派独立判断棒）```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_92998b73d1b6cb2255391499","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"c1_k1","question":"C-1 收束·候呈①（K-1 复核）：B/C 两线之 CI 半宽门适用面，独立判断结论＝「条件适用（同门柱·分母口径化）」——B/C 半宽为 0.1100 门柱之 2.27–2.84 倍、S4 构造域内结构性不可达；未另给分母口径化等效门柱前，0.1100 对 B/C 恒不适用（若坚持受门，数值须 PI 另给）。是否核准 K-1？","selectionMode":"single","options":[{"id":"c1_k1_opt1","label":"核准 K-1（条件适用）——B/C 暂免 0.1100 之门；等效门柱留待另给"},{"id":"c1_k1_opt2","label":"不核准——B/C 须受门；等效门柱数值我另行给（可于 Other 填数）"},{"id":"c1_k1_opt3","label":"另议——派独立判断棒再核"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"K-1 复核"},{"id":"c1_k2","question":"C-1 收束·候呈②（K-2 复核）：estimand 归属之独立判断＝「CI 参与判据、只以单侧界与阈值比较之形式参与」——B 取 CI 下界 < 1.00、C 取 CI 上界 > 0.10；点估计仍为准入面；0 改 1.00/0.10 阈值。是否核准？","selectionMode":"single","options":[{"id":"c1_k2_opt1","label":"核准 K-2（单侧界形式）"},{"id":"c1_k2_opt2","label":"不核准——维持纯点估计判读（CI 不参与）"},{"id":"c1_k2_opt3","label":"另议——派独立判断棒再核"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"K-2 复核"},{"id":"c1_confirm","question":"C-1 收束·候呈③：「免比 ≠ 免约束」原则须显式确认——B/C 即使暂免 0.1100 之对比，C-1 之其余约束与判读对 B/C 仍恒适用。是否确认？","selectionMode":"single","options":[{"id":"c1_confirm_opt1","label":"确认——免比≠免约束（C-1 其余约束照旧适用）"},{"id":"c1_confirm_opt2","label":"不确认——另议其边界（派独立判断棒）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"免比≠免约束"}],"status":"pending","createdAt":1791550634334,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_8b9a92bc-9228-4fe1-a921-f37ca842c24b","toolCallId":"call_00_rMzWfazLAB6sPjOmGyrp8568"},"title":"C-1 收束·候呈三题（复核与确认）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_92998b73d1b6cb2255391499","answers":[{"stepId":"c1_k1","selectedOptionIds":["c1_k1_opt1"],"selectedOther":false},{"stepId":"c1_k2","selectedOptionIds":["c1_k2_opt1"],"selectedOther":false},{"stepId":"c1_confirm","selectedOptionIds":["c1_confirm_opt1"],"selectedOther":false}],"submittedAt":1791550685214}
```

**答文逐字（逐条展开，原文照录）**

答 1／3 — 原始对象：

```json
{"stepId": "c1_k1", "selectedOptionIds": ["c1_k1_opt1"], "selectedOther": false}
```

- `stepId`：`c1_k1`
- `selectedOptionIds`（逐字）：["c1_k1_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `c1_k1_opt1` → `label`: ```核准 K-1（条件适用）——B/C 暂免 0.1100 之门；等效门柱留待另给```

答 2／3 — 原始对象：

```json
{"stepId": "c1_k2", "selectedOptionIds": ["c1_k2_opt1"], "selectedOther": false}
```

- `stepId`：`c1_k2`
- `selectedOptionIds`（逐字）：["c1_k2_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `c1_k2_opt1` → `label`: ```核准 K-2（单侧界形式）```

答 3／3 — 原始对象：

```json
{"stepId": "c1_confirm", "selectedOptionIds": ["c1_confirm_opt1"], "selectedOther": false}
```

- `stepId`：`c1_confirm`
- `selectedOptionIds`（逐字）：["c1_confirm_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `c1_confirm_opt1` → `label`: ```确认——免比≠免约束（C-1 其余约束照旧适用）```

**关键字段长度（实测）**

```text
request_json   字符数 = 1691     字节数(UTF-8) = 2458
reply_payload  字符数 = 340      字节数(UTF-8) = 340
steps 步数 = 3 ／ options 总数 = 8 ／ answers 条数 = 3
question 字符数（逐 step）: c1_k1=166; c1_k2=128; c1_confirm=78
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 03 · `ask_b77ea3aa0480fc80b5ff3531` · 新增（第一批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> T1 r2 判定·候呈四题（处置与确认）

**卡级元数据（原文照录）**

```text
request_id                     = ask_b77ea3aa0480fc80b5ff3531
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = T1 r2 判定·候呈四题（处置与确认）
presentation.allowBackNavigation = true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_task_delivery_327e78902f294b49af66162d68777ffb
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_oau93faqTeCTStfCq7F57146
request_json.createdAt (epoch ms) = 1791551191930   → 2026-10-09 21:06:31.930 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791551191930
created_at (CST 换算)          = 2026-10-09 21:06:31.930 +0800
answered_at (epoch ms)         = 1791551259249
answered_at (CST 换算)         = 2026-10-09 21:07:39.249 +0800
reply_payload.submittedAt(epoch ms) = 1791551259249   → 2026-10-09 21:07:39.249 +0800
injected_at (epoch ms)         = 1791551259292
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `t1_gate`

- `header`（原文照录）：`门禁处置`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 r2 判定·候呈①（K-T1-R1-1 门禁处置）：乙档扩样 2→3 未使门禁脱离 ≤3，门在 r2 面恒成立（hit=True ⇒ 实验面「不明」）。豁免须 PI 显式明文＋修订件条款＋复核生效（三条缺一即 0 生效；若采分轴豁免须具 E-1–E-6 六要素）。如何处置？
```

`options`（逐字原文，共 4 项）：

- `id` = `t1_gate_opt1`
  - `label`（逐字原文）：```维持不豁免——门禁照旧（沿 O-1 结论）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_gate_opt2`
  - `label`（逐字原文）：```新出修订件·加例外条款——派起草棒（条文候 PI 核准）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_gate_opt3`
  - `label`（逐字原文）：```采分轴豁免——按 E-1–E-6 六要素具文（派起草棒；须 PI 明文）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_gate_opt4`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `t1_calibers`

- `header`（原文照录）：`三口径择定`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 r2 判定·候呈③（三口径择定确认）：本件按派工面字面择定 full_reply 为主用口径；content_only／reasoning_only 登记不采（content_only×same-caption 下 5/6 格 ≥0.85 之 hit=True 已如实登记不隐匿）。是否确认 full_reply 为主用？
```

`options`（逐字原文，共 3 项）：

- `id` = `t1_calibers_opt1`
  - `label`（逐字原文）：```确认——full_reply 为主用（其余两口径维持登记不采）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_calibers_opt2`
  - `label`（逐字原文）：```改采其他口径——于 Other 指明（含理由）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_calibers_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `t1_temp`

- `header`（原文照录）：`温度轴处置`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 r2 判定·候呈④（温度轴有效性处置）：独立重算显示温度轴未获证实——同温内 3 复本 full_reply 0/180 全同；跨温 J 中位 0.5285 ≈ 同温内 0.5300；@t=0.3 同温内 0.4280 低于跨温 0.5197（方向不利该假说）。「发散幅度与可分辨性」是否达标、是否须换度量对象或换实验设计——PI 四答未处置。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `t1_temp_opt1`
  - `label`（逐字原文）：```维持现状——留「未证」登记，S1/S3 维持不明（0 加阈、0 新跑）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_temp_opt2`
  - `label`（逐字原文）：```PI 给阈值——就「发散幅度与可分辨性」给定达标判据（Other 填）后按之重判```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_temp_opt3`
  - `label`（逐字原文）：```换测/换设计——授权新实验（设计棒另派）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_temp_opt4`
  - `label`（逐字原文）：```另议——派独立判断棒出建议件```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `t1_d1`

- `header`（原文照录）：`D-1 勘正`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 r2 判定·候呈⑤（差异 D-1 勘正）：实测 cell_j_median／n_teachers_ge_0_85 系由 all-pooled（j_median_all）导出，与 activation §2.2 冻结之 same-caption 主度量口径不符——r1 同类错位在 r2 未修（字段命名层）。如何处置？
```

`options`（逐字原文，共 3 项）：

- `id` = `t1_d1_opt1`
  - `label`（逐字原文）：```派勘正件（另件承载·0 回改既有件）——注明字段口径并修正下游引用指引```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_d1_opt2`
  - `label`（逐字原文）：```仅登记、暂不勘正——挂册候统一处置```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_d1_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_b77ea3aa0480fc80b5ff3531","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"t1_gate","question":"T1 r2 判定·候呈①（K-T1-R1-1 门禁处置）：乙档扩样 2→3 未使门禁脱离 ≤3，门在 r2 面恒成立（hit=True ⇒ 实验面「不明」）。豁免须 PI 显式明文＋修订件条款＋复核生效（三条缺一即 0 生效；若采分轴豁免须具 E-1–E-6 六要素）。如何处置？","selectionMode":"single","options":[{"id":"t1_gate_opt1","label":"维持不豁免——门禁照旧（沿 O-1 结论）"},{"id":"t1_gate_opt2","label":"新出修订件·加例外条款——派起草棒（条文候 PI 核准）"},{"id":"t1_gate_opt3","label":"采分轴豁免——按 E-1–E-6 六要素具文（派起草棒；须 PI 明文）"},{"id":"t1_gate_opt4","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"门禁处置"},{"id":"t1_calibers","question":"T1 r2 判定·候呈③（三口径择定确认）：本件按派工面字面择定 full_reply 为主用口径；content_only／reasoning_only 登记不采（content_only×same-caption 下 5/6 格 ≥0.85 之 hit=True 已如实登记不隐匿）。是否确认 full_reply 为主用？","selectionMode":"single","options":[{"id":"t1_calibers_opt1","label":"确认——full_reply 为主用（其余两口径维持登记不采）"},{"id":"t1_calibers_opt2","label":"改采其他口径——于 Other 指明（含理由）"},{"id":"t1_calibers_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"三口径择定"},{"id":"t1_temp","question":"T1 r2 判定·候呈④（温度轴有效性处置）：独立重算显示温度轴未获证实——同温内 3 复本 full_reply 0/180 全同；跨温 J 中位 0.5285 ≈ 同温内 0.5300；@t=0.3 同温内 0.4280 低于跨温 0.5197（方向不利该假说）。「发散幅度与可分辨性」是否达标、是否须换度量对象或换实验设计——PI 四答未处置。请裁：","selectionMode":"single","options":[{"id":"t1_temp_opt1","label":"维持现状——留「未证」登记，S1/S3 维持不明（0 加阈、0 新跑）"},{"id":"t1_temp_opt2","label":"PI 给阈值——就「发散幅度与可分辨性」给定达标判据（Other 填）后按之重判"},{"id":"t1_temp_opt3","label":"换测/换设计——授权新实验（设计棒另派）"},{"id":"t1_temp_opt4","label":"另议——派独立判断棒出建议件"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"温度轴处置"},{"id":"t1_d1","question":"T1 r2 判定·候呈⑤（差异 D-1 勘正）：实测 cell_j_median／n_teachers_ge_0_85 系由 all-pooled（j_median_all）导出，与 activation §2.2 冻结之 same-caption 主度量口径不符——r1 同类错位在 r2 未修（字段命名层）。如何处置？","selectionMode":"single","options":[{"id":"t1_d1_opt1","label":"派勘正件（另件承载·0 回改既有件）——注明字段口径并修正下游引用指引"},{"id":"t1_d1_opt2","label":"仅登记、暂不勘正——挂册候统一处置"},{"id":"t1_d1_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"D-1 勘正"}],"status":"pending","createdAt":1791551191930,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_task_delivery_327e78902f294b49af66162d68777ffb","toolCallId":"call_00_oau93faqTeCTStfCq7F57146"},"title":"T1 r2 判定·候呈四题（处置与确认）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_b77ea3aa0480fc80b5ff3531","answers":[{"stepId":"t1_gate","selectedOptionIds":["t1_gate_opt2"],"selectedOther":false},{"stepId":"t1_calibers","selectedOptionIds":["t1_calibers_opt1"],"selectedOther":false},{"stepId":"t1_temp","selectedOptionIds":["t1_temp_opt3"],"selectedOther":false},{"stepId":"t1_d1","selectedOptionIds":["t1_d1_opt1"],"selectedOther":false}],"submittedAt":1791551259249}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "t1_gate", "selectedOptionIds": ["t1_gate_opt2"], "selectedOther": false}
```

- `stepId`：`t1_gate`
- `selectedOptionIds`（逐字）：["t1_gate_opt2"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `t1_gate_opt2` → `label`: ```新出修订件·加例外条款——派起草棒（条文候 PI 核准）```

答 2／4 — 原始对象：

```json
{"stepId": "t1_calibers", "selectedOptionIds": ["t1_calibers_opt1"], "selectedOther": false}
```

- `stepId`：`t1_calibers`
- `selectedOptionIds`（逐字）：["t1_calibers_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `t1_calibers_opt1` → `label`: ```确认——full_reply 为主用（其余两口径维持登记不采）```

答 3／4 — 原始对象：

```json
{"stepId": "t1_temp", "selectedOptionIds": ["t1_temp_opt3"], "selectedOther": false}
```

- `stepId`：`t1_temp`
- `selectedOptionIds`（逐字）：["t1_temp_opt3"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `t1_temp_opt3` → `label`: ```换测/换设计——授权新实验（设计棒另派）```

答 4／4 — 原始对象：

```json
{"stepId": "t1_d1", "selectedOptionIds": ["t1_d1_opt1"], "selectedOther": false}
```

- `stepId`：`t1_d1`
- `selectedOptionIds`（逐字）：["t1_d1_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `t1_d1_opt1` → `label`: ```派勘正件（另件承载·0 回改既有件）——注明字段口径并修正下游引用指引```

**关键字段长度（实测）**

```text
request_json   字符数 = 2489     字节数(UTF-8) = 3706
reply_payload  字符数 = 426      字节数(UTF-8) = 426
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: t1_gate=140; t1_calibers=164; t1_temp=178; t1_d1=161
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 04 · `ask_10d9b3f27e4bcf9e964d67d6` · 新增（第一批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> KD 复核·三题＋另议复核

**卡级元数据（原文照录）**

```text
request_id                     = ask_10d9b3f27e4bcf9e964d67d6
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = KD 复核·三题＋另议复核
presentation.allowBackNavigation = true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_603acbd1-de86-4619-b14c-76866398e46d
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_5xLCkXh5YGPqOBUnziLs3842
request_json.createdAt (epoch ms) = 1791551517434   → 2026-10-09 21:11:57.434 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791551517434
created_at (CST 换算)          = 2026-10-09 21:11:57.434 +0800
answered_at (epoch ms)         = 1791551623644
answered_at (CST 换算)         = 2026-10-09 21:13:43.644 +0800
reply_payload.submittedAt(epoch ms) = 1791551623644   → 2026-10-09 21:13:43.644 +0800
injected_at (epoch ms)         = 1791551623776
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `kd_p1`

- `header`（原文照录）：`P-1 收编层界`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 归类·候呈 P-1（收编层界，件 c0cfd21d57a8）：独立判断将「三态不可判」（PASS/FAIL/KD 之 KD 档）语义收编为 Known Defect 第三档、拟仅限称谓层（0 新立判据、0 赋布尔）；反方曾提「是否构成事后调」之虑。是否核准「仅限称谓层」？
```

`options`（逐字原文，共 3 项）：

- `id` = `kd_p1_opt1`
  - `label`（逐字原文）：```核准——仅限称谓层（0 新立判据，判读行为不变）```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p1_opt2`
  - `label`（逐字原文）：```不核准——另行处置（请于 Other 说明方向）```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p1_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `kd_p5`

- `header`（原文照录）：`P-5 裁面性质`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 归类·候呈 P-5（裁面性质）：实测「Known Defect」字面全仓 0 命中（KD 命中 2433 处均无该英文全称字面）——你之裁录所对为语义面（判定语汇之义）还是须补立字面面？
```

`options`（逐字原文，共 4 项）：

- `id` = `kd_p5_opt1`
  - `label`（逐字原文）：```语义面为主——裁录覆盖判定语汇之义，不动既有字面```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p5_opt2`
  - `label`（逐字原文）：```字面面为主——须另行补立「Known Defect」字面承载（落表/登记件）```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p5_opt3`
  - `label`（逐字原文）：```两面并要——语义面生效＋字面补立（候后续件）```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p5_opt4`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `kd_p4`

- `header`（原文照录）：`P-4 拆名`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 归类·候呈 P-4（拆名与否）：Known Defect 现兼跨「编号域缺陷（历史勘误链）」与「判定第三档（不可判）」两域——是否拆名或维持一名两域？
```

`options`（逐字原文，共 3 项）：

- `id` = `kd_p4_opt1`
  - `label`（逐字原文）：```维持一名两域——以分域标注区分（编号域/判定档）```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p4_opt2`
  - `label`（逐字原文）：```拆名——判定第三档与编号域缺陷分用两名```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p4_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `aside_k2`

- `header`（原文照录）：`另议复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
另议件复核（171 域及于 -2 腿，件 a802af7ac3bc）：独立结论＝「不及于」（K-4-3 单日占比腿之裁不溢出至 -2 substrate 腿；-2 维持 179，+29）；次位出口＝双读并列。是否核准生效？
```

`options`（逐字原文，共 4 项）：

- `id` = `aside_k2_opt1`
  - `label`（逐字原文）：```核准——不及于（-2 维持 179，+29）```
  - `description`（逐字原文）：（无此键）
- `id` = `aside_k2_opt2`
  - `label`（逐字原文）：```采双读并列——171(+21)／179(+29) 并陈、0 单择```
  - `description`（逐字原文）：（无此键）
- `id` = `aside_k2_opt3`
  - `label`（逐字原文）：```及于——改以 171 域读数（+21，与 K-4-3 主读域统一）```
  - `description`（逐字原文）：（无此键）
- `id` = `aside_k2_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_10d9b3f27e4bcf9e964d67d6","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"kd_p1","question":"KD 归类·候呈 P-1（收编层界，件 c0cfd21d57a8）：独立判断将「三态不可判」（PASS/FAIL/KD 之 KD 档）语义收编为 Known Defect 第三档、拟仅限称谓层（0 新立判据、0 赋布尔）；反方曾提「是否构成事后调」之虑。是否核准「仅限称谓层」？","selectionMode":"single","options":[{"id":"kd_p1_opt1","label":"核准——仅限称谓层（0 新立判据，判读行为不变）"},{"id":"kd_p1_opt2","label":"不核准——另行处置（请于 Other 说明方向）"},{"id":"kd_p1_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"P-1 收编层界"},{"id":"kd_p5","question":"KD 归类·候呈 P-5（裁面性质）：实测「Known Defect」字面全仓 0 命中（KD 命中 2433 处均无该英文全称字面）——你之裁录所对为语义面（判定语汇之义）还是须补立字面面？","selectionMode":"single","options":[{"id":"kd_p5_opt1","label":"语义面为主——裁录覆盖判定语汇之义，不动既有字面"},{"id":"kd_p5_opt2","label":"字面面为主——须另行补立「Known Defect」字面承载（落表/登记件）"},{"id":"kd_p5_opt3","label":"两面并要——语义面生效＋字面补立（候后续件）"},{"id":"kd_p5_opt4","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"P-5 裁面性质"},{"id":"kd_p4","question":"KD 归类·候呈 P-4（拆名与否）：Known Defect 现兼跨「编号域缺陷（历史勘误链）」与「判定第三档（不可判）」两域——是否拆名或维持一名两域？","selectionMode":"single","options":[{"id":"kd_p4_opt1","label":"维持一名两域——以分域标注区分（编号域/判定档）"},{"id":"kd_p4_opt2","label":"拆名——判定第三档与编号域缺陷分用两名"},{"id":"kd_p4_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"P-4 拆名"},{"id":"aside_k2","question":"另议件复核（171 域及于 -2 腿，件 a802af7ac3bc）：独立结论＝「不及于」（K-4-3 单日占比腿之裁不溢出至 -2 substrate 腿；-2 维持 179，+29）；次位出口＝双读并列。是否核准生效？","selectionMode":"single","options":[{"id":"aside_k2_opt1","label":"核准——不及于（-2 维持 179，+29）"},{"id":"aside_k2_opt2","label":"采双读并列——171(+21)／179(+29) 并陈、0 单择"},{"id":"aside_k2_opt3","label":"及于——改以 171 域读数（+21，与 K-4-3 主读域统一）"},{"id":"aside_k2_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"另议复核"}],"status":"pending","createdAt":1791551517434,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_603acbd1-de86-4619-b14c-76866398e46d","toolCallId":"call_00_5xLCkXh5YGPqOBUnziLs3842"},"title":"KD 复核·三题＋另议复核"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_10d9b3f27e4bcf9e964d67d6","answers":[{"stepId":"kd_p1","selectedOptionIds":["kd_p1_opt1"],"selectedOther":false},{"stepId":"kd_p5","selectedOptionIds":["kd_p5_opt3"],"selectedOther":false},{"stepId":"kd_p4","selectedOptionIds":["kd_p4_opt1"],"selectedOther":false},{"stepId":"aside_k2","selectedOptionIds":["aside_k2_opt1"],"selectedOther":false}],"submittedAt":1791551623644}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "kd_p1", "selectedOptionIds": ["kd_p1_opt1"], "selectedOther": false}
```

- `stepId`：`kd_p1`
- `selectedOptionIds`（逐字）：["kd_p1_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `kd_p1_opt1` → `label`: ```核准——仅限称谓层（0 新立判据，判读行为不变）```

答 2／4 — 原始对象：

```json
{"stepId": "kd_p5", "selectedOptionIds": ["kd_p5_opt3"], "selectedOther": false}
```

- `stepId`：`kd_p5`
- `selectedOptionIds`（逐字）：["kd_p5_opt3"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `kd_p5_opt3` → `label`: ```两面并要——语义面生效＋字面补立（候后续件）```

答 3／4 — 原始对象：

```json
{"stepId": "kd_p4", "selectedOptionIds": ["kd_p4_opt1"], "selectedOther": false}
```

- `stepId`：`kd_p4`
- `selectedOptionIds`（逐字）：["kd_p4_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `kd_p4_opt1` → `label`: ```维持一名两域——以分域标注区分（编号域/判定档）```

答 4／4 — 原始对象：

```json
{"stepId": "aside_k2", "selectedOptionIds": ["aside_k2_opt1"], "selectedOther": false}
```

- `stepId`：`aside_k2`
- `selectedOptionIds`（逐字）：["aside_k2_opt1"]
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `aside_k2_opt1` → `label`: ```核准——不及于（-2 维持 179，+29）```

**关键字段长度（实测）**

```text
request_json   字符数 = 2194     字节数(UTF-8) = 3226
reply_payload  字符数 = 412      字节数(UTF-8) = 412
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: kd_p1=139; kd_p5=96; kd_p4=78; aside_k2=111
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 05 · `ask_6db74cbbb4c70cf8c0c6cc1e` · 新增（第一批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> T1 温度轴·新实验决议四题

**卡级元数据（原文照录）**

```text
request_id                     = ask_6db74cbbb4c70cf8c0c6cc1e
status（表列 questionnaire_requests.status） = pending
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = T1 温度轴·新实验决议四题
presentation.allowBackNavigation = true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_task_delivery_75433cec0be742c592b85d4a3eb9e537
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_slxX1GUue8n6Aon9Uwix5104
request_json.createdAt (epoch ms) = 1791552214280   → 2026-10-09 21:23:34.280 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791552214280
created_at (CST 换算)          = 2026-10-09 21:23:34.280 +0800
answered_at (epoch ms)         = NULL
answered_at (CST 换算)         = NULL
reply_payload.submittedAt(epoch ms) = NULL   → NULL
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `t1e_path`

- `header`（原文照录）：`路径与额度`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 温度轴·决议①（路径与调用额度）：新实验设计已出（件 7aaa90ee6d50）——候选 D 先导探针（≤51 调用）／A 答案面换测（0 新调用）／B 同温加密（364）／C 温度 5 水平×复本≥4（404，构造性解除门禁）；推荐链 D→A×C（≈607 调用、约 3.4h）。请择定：
```

`options`（逐字原文，共 4 项）：

- `id` = `t1e_path_opt1`
  - `label`（逐字原文）：```采全案 D→A×C——按 ≈607 调用额度起跑（换测基线 0 调用先行）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_path_opt2`
  - `label`（逐字原文）：```先 D 先导探针（≤51 调用）——看结果再裁全案```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_path_opt3`
  - `label`（逐字原文）：```仅 A 换测加基线（0 新调用）——先取换测读数```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_path_opt4`
  - `label`（逐字原文）：```暂缓——留设计待判（0 起跑）```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `t1e_prereg`

- `header`（原文照录）：`预登记修订`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 温度轴·决议②（预登记修订）：全案须修订预登记（温度集 3→5 水平、复本 R=6 等；生效即锁、0 溯及）。是否核准（候案定后随件落）？
```

`options`（逐字原文，共 4 项）：

- `id` = `t1e_prereg_opt1`
  - `label`（逐字原文）：```核准全案修订方向——按决议①所选案随件落定```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_prereg_opt2`
  - `label`（逐字原文）：```仅核准先导探针最小修订```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_prereg_opt3`
  - `label`（逐字原文）：```暂不核准——候全案细目再议```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_prereg_opt4`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `t1e_mde`

- `header`（原文照录）：`判据与 MDE`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 温度轴·决议③（判据冻结·含 MDE）：设计建议双向判据（CI 下界 > 0 ⇒ 轴有效；含 0 ⇒ 轴无效）＋名义 MDE≈5pp（聚类保守 8–15pp 为粗估）。MDE 数值线须你定：
```

`options`（逐字原文，共 3 项）：

- `id` = `t1e_mde_opt1`
  - `label`（逐字原文）：```按设计建议冻结——名义 5pp／保守 8–15pp（随案定）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_mde_opt2`
  - `label`（逐字原文）：```另给数值——于 Other 填 MDE 线```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_mde_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒核估```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `t1e_p1`

- `header`（原文照录）：`P-1 口径张力`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 温度轴·决议④（口径张力 P-1）：案 A 之「答案面」可由既有 full_reply 尾行 100% 还原（180/180 实证），与 activation §3.1 禁一「只取 message.content」存在语境张力（设计称非 r1 残段复活）。是否认可答案面为轴探针读数面？
```

`options`（逐字原文，共 3 项）：

- `id` = `t1e_p1_opt1`
  - `label`（逐字原文）：```认可——答案面作轴探针读数面（非残段复活；以 180/180 实证为据）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_p1_opt2`
  - `label`（逐字原文）：```不认可——严守禁一（轴探针不得用答案面）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1e_p1_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_6db74cbbb4c70cf8c0c6cc1e","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"t1e_path","question":"T1 温度轴·决议①（路径与调用额度）：新实验设计已出（件 7aaa90ee6d50）——候选 D 先导探针（≤51 调用）／A 答案面换测（0 新调用）／B 同温加密（364）／C 温度 5 水平×复本≥4（404，构造性解除门禁）；推荐链 D→A×C（≈607 调用、约 3.4h）。请择定：","selectionMode":"single","options":[{"id":"t1e_path_opt1","label":"采全案 D→A×C——按 ≈607 调用额度起跑（换测基线 0 调用先行）"},{"id":"t1e_path_opt2","label":"先 D 先导探针（≤51 调用）——看结果再裁全案"},{"id":"t1e_path_opt3","label":"仅 A 换测加基线（0 新调用）——先取换测读数"},{"id":"t1e_path_opt4","label":"暂缓——留设计待判（0 起跑）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"路径与额度"},{"id":"t1e_prereg","question":"T1 温度轴·决议②（预登记修订）：全案须修订预登记（温度集 3→5 水平、复本 R=6 等；生效即锁、0 溯及）。是否核准（候案定后随件落）？","selectionMode":"single","options":[{"id":"t1e_prereg_opt1","label":"核准全案修订方向——按决议①所选案随件落定"},{"id":"t1e_prereg_opt2","label":"仅核准先导探针最小修订"},{"id":"t1e_prereg_opt3","label":"暂不核准——候全案细目再议"},{"id":"t1e_prereg_opt4","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"预登记修订"},{"id":"t1e_mde","question":"T1 温度轴·决议③（判据冻结·含 MDE）：设计建议双向判据（CI 下界 > 0 ⇒ 轴有效；含 0 ⇒ 轴无效）＋名义 MDE≈5pp（聚类保守 8–15pp 为粗估）。MDE 数值线须你定：","selectionMode":"single","options":[{"id":"t1e_mde_opt1","label":"按设计建议冻结——名义 5pp／保守 8–15pp（随案定）"},{"id":"t1e_mde_opt2","label":"另给数值——于 Other 填 MDE 线"},{"id":"t1e_mde_opt3","label":"另议——派独立判断棒核估"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"判据与 MDE"},{"id":"t1e_p1","question":"T1 温度轴·决议④（口径张力 P-1）：案 A 之「答案面」可由既有 full_reply 尾行 100% 还原（180/180 实证），与 activation §3.1 禁一「只取 message.content」存在语境张力（设计称非 r1 残段复活）。是否认可答案面为轴探针读数面？","selectionMode":"single","options":[{"id":"t1e_p1_opt1","label":"认可——答案面作轴探针读数面（非残段复活；以 180/180 实证为据）"},{"id":"t1e_p1_opt2","label":"不认可——严守禁一（轴探针不得用答案面）"},{"id":"t1e_p1_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"P-1 口径张力"}],"status":"pending","createdAt":1791552214280,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_task_delivery_75433cec0be742c592b85d4a3eb9e537","toolCallId":"call_00_slxX1GUue8n6Aon9Uwix5104"},"title":"T1 温度轴·新实验决议四题"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
NULL
```

- 本件读得时该卡：表列 `status` = `pending`；`request_json` 内嵌 status ＝ `pending`；`answered_at` = NULL；`reply_payload` = NULL；`injected_at` = NULL。
- ⛔ **0 将待答冒充已答**：本件**不补答、不推演、不改状态**，仅照录库中现状（元数据 ＋ 题面全文字面）。

**答文逐字（逐条展开，原文照录）**

- （本件读得时该卡 `reply_payload` 为 NULL，无 `answers` 可展开。）

**关键字段长度（实测）**

```text
request_json   字符数 = 2272     字节数(UTF-8) = 3350
reply_payload  字符数 = NULL     字节数(UTF-8) = NULL（库中为 NULL）
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 0
question 字符数（逐 step）: t1e_path=148; t1e_prereg=72; t1e_mde=98; t1e_p1=146
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

## 2 · 与第一批登记件逐件对账（按 `request_id`，本批窗口全部 10 件）

| 窗口序 | request_id | 批次处置 | 第一批序号 | 卡题（`title` 逐字） | status（表列） | created_at (CST) | answered_at (CST) |
|---|---|---|---|---|---|---|---|
| 1 | `ask_68df18a1976c91fb18d19497` | 对账行（0 重复转录） | 第 30 件 | ①段·C-1 细化复核卷 | `answered` | 2026-10-09 17:04:09.068 +0800 | 2026-10-09 17:05:47.070 +0800 |
| 2 | `ask_ced8de9fd514ccc30f4e16e2` | 对账行（0 重复转录） | 第 31 件 | ①段·收束裁卷（计数口径／分母域／U04-1／P-1） | `answered` | 2026-10-09 17:14:29.030 +0800 | 2026-10-09 17:16:38.809 +0800 |
| 3 | `ask_69d695f301f12d158e102652` | 对账行（0 重复转录） | 第 32 件 | ①段·V3-05/U04 残卷 | `answered` | 2026-10-09 17:18:10.089 +0800 | 2026-10-09 17:18:45.302 +0800 |
| 4 | `ask_a9ce5b284c10bf1e36077e35` | 对账行（0 重复转录） | 第 33 件 | ①段·C-1 续卷 | `answered` | 2026-10-09 17:22:15.304 +0800 | 2026-10-09 17:23:19.556 +0800 |
| 5 | `ask_33471ffa5c68d4bbd8571e40` | 对账行（0 重复转录） | 第 34 件 | ①段·RP 收尾卷 | `answered` | 2026-10-09 17:24:20.757 +0800 | 2026-10-09 17:26:37.760 +0800 |
| 6 | `ask_bd9193285d3d02c0dcd98f26` | **本批转录（本件第 1 件）** | —（第一批未含） | S4 判档·候呈四题（收口前置） | `answered` | 2026-10-09 20:52:07.880 +0800 | 2026-10-09 20:54:09.897 +0800 |
| 7 | `ask_92998b73d1b6cb2255391499` | **本批转录（本件第 2 件）** | —（第一批未含） | C-1 收束·候呈三题（复核与确认） | `answered` | 2026-10-09 20:57:14.334 +0800 | 2026-10-09 20:58:05.214 +0800 |
| 8 | `ask_b77ea3aa0480fc80b5ff3531` | **本批转录（本件第 3 件）** | —（第一批未含） | T1 r2 判定·候呈四题（处置与确认） | `answered` | 2026-10-09 21:06:31.930 +0800 | 2026-10-09 21:07:39.249 +0800 |
| 9 | `ask_10d9b3f27e4bcf9e964d67d6` | **本批转录（本件第 4 件）** | —（第一批未含） | KD 复核·三题＋另议复核 | `answered` | 2026-10-09 21:11:57.434 +0800 | 2026-10-09 21:13:43.644 +0800 |
| 10 | `ask_6db74cbbb4c70cf8c0c6cc1e` | **本批转录（本件第 5 件）** | —（第一批未含） | T1 温度轴·新实验决议四题 | `pending` | 2026-10-09 21:23:34.280 +0800 | NULL |

**重叠区（`2026-10-09 17:00:00` ～ `2026-10-09 18:08:26.683 +0800`，第一批读取时点）实测 5 件——全部已含于第一批登记件，本批 0 重复转录：**

- `ask_68df18a1976c91fb18d19497` → 第一批第 30 件· ★必录（C-1 四答） → 原文见第一批登记件对应节（本件不重录）
- `ask_ced8de9fd514ccc30f4e16e2` → 第一批第 31 件· ★必录（收束四答） → 原文见第一批登记件对应节（本件不重录）
- `ask_69d695f301f12d158e102652` → 第一批第 32 件· ★必录（V3-05 三答） → 原文见第一批登记件对应节（本件不重录）
- `ask_a9ce5b284c10bf1e36077e35` → 第一批第 33 件· ★必录（C-1 续卷四答） → 原文见第一批登记件对应节（本件不重录）
- `ask_33471ffa5c68d4bbd8571e40` → 第一批第 34 件· ★必录（R_pair 四答） → 原文见第一批登记件对应节（本件不重录）

**第一批截止后新增（`2026-10-09 18:08:26.683 +0800` 之后建卡）实测 5 件——本批逐字全量收录：**

- `ask_bd9193285d3d02c0dcd98f26`（`created_at` = 1791550327880 epoch ms ／ 2026-10-09 20:52:07.880 +0800）→ 本件第 1 件
- `ask_92998b73d1b6cb2255391499`（`created_at` = 1791550634334 epoch ms ／ 2026-10-09 20:57:14.334 +0800）→ 本件第 2 件
- `ask_b77ea3aa0480fc80b5ff3531`（`created_at` = 1791551191930 epoch ms ／ 2026-10-09 21:06:31.930 +0800）→ 本件第 3 件
- `ask_10d9b3f27e4bcf9e964d67d6`（`created_at` = 1791551517434 epoch ms ／ 2026-10-09 21:11:57.434 +0800）→ 本件第 4 件
- `ask_6db74cbbb4c70cf8c0c6cc1e`（`created_at` = 1791552214280 epoch ms ／ 2026-10-09 21:23:34.280 +0800）→ 本件第 5 件（读得时 `status = pending`、答文未达 → 元数据＋题面照录）

**第一批窗口漏录复核**：以第一批窗口下界 `1791388800000` 重扫全表，本轮实测 `39` 件，第一批实录 `34` 件、本批新增 `5` 件，`34 ＋ 5 ＝ 39`（**0 漏录**）。

**第一批 `request_id` 计数依据（如实记录，⛔ 0 判读）**：

- 第一批登记件内以 `### NN · \`ask_…\`` 标题形式收录的 `request_id`：**34** 个（对应其 §1 全量清单 34 件）。
- 该文件全文出现的 `ask_[0-9a-f]{24}` 唯一值共 **36** 个，其中 **2** 个仅出现在正文（0 独立卡节）：`ask_05992739fd9e46f8e8acd23d`、`ask_8a04bb5c4f9ded71e2de43a3`
  ——本件据其**标题节**口径对账；上列二 id 均经本轮实测**早于本批窗口下界**，故不属本轮应录面。

## 3 · 枚举完整性对账

```text
本批应录 N 件（本批窗口 created_at>=2026-10-09 17:00:00 +0800 内，第一批未含者）
  ＝ 本窗口记录总数        : 10
  － 第一批已含（重叠区）  : 5
  ⇒ 本批应录全集（去重）  : 5
实录 N 件（本件已逐字转录的卡节数）: 5
  其中 答文已达（answered）: 4 ／ 读得时待答（仅元数据＋题面照录）: 1
miss = 应录 − 实录 : 0
重复转录数（第一批已含者被本件重录）: 0
```

**miss 明细：0（无遗漏）。** 逐项核验：

- 本窗口 10 件逐一 `SELECT` 实查，10/10 命中；其中 `status = answered` 9 件、`status != answered` 1 件（后者见本节「status 与答文完整性」）。
- 其中第一批未含者 5 件已在本件 §1 **逐字全量收录**（卡题＋题面全文字面＋答文全文或待答现状＋关键字段长度）。
- 第一批已含者 5 件**仅列对账行**（§2），⛔ 0 重复转录其题面／答文。
- 重复 id：0（`request_id` 为表主键，全表唯一）。

**status 与答文完整性（⛔ 0 将待答冒充已答）**

```text
本窗口 status != 'answered' 的记录数 : 1
本窗口 answered_at 为 NULL 的记录数 : 1
本窗口 reply_payload 为 NULL/空的记录数: 1
```

- 本窗口内有 **1** 件在本件读得时**尚未作答**（`status = pending`、`answered_at` 为 NULL、`reply_payload` 为 NULL），该（等）件在 §1 中**以元数据 ＋ 题面全文字面照录**，⛔ **0 冒充已答**、⛔ 0 推演答文：
  - `ask_6db74cbbb4c70cf8c0c6cc1e`（`created_at` = 2026-10-09 21:23:34.280 +0800）——待答状态如实登记；其答文之落册（若日后作答）**不属本件范围**。
- 其余 9 件 `answered` 且 `answered_at` 非空、`reply_payload` 非空，已全量转录答文。
- 全表 `superseded` 记录 1 条，其 `created_at` **早于**本窗口下界，故不属本轮应录范围，**未转录**。

**本轮读取方式合规确认**

- 连接串：`sqlite3.connect("file:<db>?mode=ro", uri=True)` —— **只读**。⛔ 0 `INSERT`/`UPDATE`/`DELETE`/`CREATE`/`DROP`。
- ⛔ 0 网络访问；⛔ 0 调用任何 skill；⛔ 0 编辑或覆写任何既有工作档案（本件为新建，落前实测 `Test-Path=False` 且 glob 0 命中）。
- R4 key：对**本件全部转录字面**（5 件卡的 `request_json` ＋ `reply_payload` 原串）做正则扫描 —— OpenAI 式 `sk-[A-Za-z0-9]{16,}`／GitHub 式 `gh[pousr]_[A-Za-z0-9]{16,}`／AWS 式 `AKIA[0-9A-Z]{16}`／Slack 式 `xox[baprs]-…`／Google 式 `AIza[0-9A-Za-z_-]{35}`／PEM `BEGIN … PRIVATE KEY`／`Bearer <长 token>`／`*api_key*`／`*token*`／`*password*` 后接赋值符与非空值／JWT 三段点分形，各族命中均为 **0**，本件**不含任何 key／凭证明文**。

---

*（本件完 · 逐字转录 · 0 解释 · 0 判读 · 0 代裁）*
