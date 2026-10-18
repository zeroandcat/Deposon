# 裁卡原件批量落册（第六批）· questionnaire 原件逐字转录（2026-10-10）

## 文件头注

- **件名**：`results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md`
- **落册日期**：2026-10-10（CST）
- **件系**：第五批登记件 `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md`（SHA-12 `d6ff041a9df9`）之**追补落册（第六批）**；上承第四批 `11681f0ad861`、第三批 `dc43e3cb7610`、第二批 `193386b9f23c`、第一批 `d917180db36f`。⛔ 0 编辑／覆写／修改前五批登记件；⛔ 0 重复转录其已收录之卡。
- **编制**：**doc-writer**（文稿起草官 · 分支会话 `mvs_b498c4eaba5242c8a39e7e24dd206ba0`｜署名如实 · **0 冒充 PI／parent／protocol-keeper／verdict-keeper／verifier／worker**）
- **来源**：运行时库 `〔本机用户目录〕/.minimax/v2/sqlite/runtime-state.sqlite`，表 `questionnaire_requests`。本轮以 `sqlite3.connect("file:...?mode=ro", uri=True)` **只读实测**（0 写入、0 修改、0 建表、0 提交）。
- **备核源**：本会话消息面 `〔本机用户目录〕/.minimax/v2/sessions/2026/09/01/02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5`之 `messages.jsonl`（只读检索，作二次交叉核对）。
- **窗口口径**：本批应录＝派工指定之 **6 张目标卡**（轮39～轮44）——**本件非全表扫描之应录全集**，系**指定目标行**之逐字转录（沿「库读取限 `questionnaire_requests` 目标行」之派工纪律）。
  - ⚠ **活库声明**：运行时库为**活库**，本件之读得时点即收录截止时点；**其后再建之卡不属本件应录面**。
- **转录纪律**：**逐字、0 省略、0 解释、0 判读**。题面（`request_json.steps` 之 id／header／question／options／selectionMode／required／allowOther／otherPlaceholder）与答文（`reply_payload` 全文，含 `selectedOther`／`otherText`）均按库中原文照录；本件**不含**任何分析、结论、裁断或建议。
- **效力声明**：本件**仅转录**。⛔ **0 当「裁录」**；⛔ **0 代替任何既有登记件的裁录效力**。本件不产生、不替代、不撤销任何裁决；一切裁断效力仍以其原登记件／生效件为准。
- **命名合规**：`_主题_日期` 体例；⛔ 0 带 V-阶段前缀（0 `_v3_`／`_v4_`／`_v5_`）。沿既有 `_supplement_` 续编体例（第一批 → `_supplement_` → `_supplement_2_` → `_supplement_3_` → `_supplement_4_` → 本件 `_supplement_5_`）。
- **版式**：UTF-8 无 BOM · LF（CRLF ＝ 0）｜**R4**：key 永不明文（本棒 0 读 key／0 读 `.env`／0 落盘凭据）｜**0 网络 · 0 skill · 0 LLM · 0 实验**。
- **编制方式**：程序化逐字转录（⛔ 0 人工改写任何字面）。

---

## 0 · 本轮读取基准（provenance）

- 库文件大小（读取时点）：`474656768` bytes
- 库文件 mtime（读取时点，CST）：`2026-10-10 13:54:31.614 +0800`
- 表 `questionnaire_requests` 总行数（全表，本轮实测）：`415`
- 全表 status 分布（全表实测）：`answered`=413 `superseded`=2；
- 抽取口径：`SELECT ... FROM questionnaire_requests WHERE request_id IN (6 个目标 id)`（**指定目标行**，⛔ 0 全表内容扫描、⛔ 0 LIMIT 截断）；命中 **6**／6。
- 时间换算口径：`created_at`／`answered_at`／`submittedAt`／`createdAt` 均为 **INTEGER epoch 毫秒**，本件统一换算为 **CST（UTC+8）** 呈现，原值同时照录。
- 值形口径：SQL／JSON 空值一律呈为 `NULL`；布尔值一律呈为 JSON 小写字面 `true`／`false`（沿前五批体例）。
- **复核核对口径：**本件另以会话消息面 `messages.jsonl` 按各 `ask_…` requestId 检索卡片呈递与答复段落，作独立交叉核对源。

---

## 1 · 逐卡转录（指定目标 6 件，按 `created_at` 升序）

### 01 · `ask_c8d8c049d9c68775ba5f03ee` · 轮39（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮39 · E-6（judge_type_J5 补料）四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_c8d8c049d9c68775ba5f03ee
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮39 · E-6（judge_type_J5 补料）四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_42388949-9f70-43d0-8be3-0606f05c244a
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_2R7ydmxzVfDUsDv7cRFG0275
request_json.createdAt (epoch ms)= 1791606167604   → 2026-10-10 12:22:47.604 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791606167604
created_at (CST 换算)            = 2026-10-10 12:22:47.604 +0800
answered_at (epoch ms)         = 1791606232013
answered_at (CST 换算)           = 2026-10-10 12:23:52.013 +0800
reply_payload.submittedAt(epoch ms)= 1791606232013   → 2026-10-10 12:23:52.013 +0800
injected_at (epoch ms)         = 1791606244719
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／11 选项，原文照录）**

**题 1／4** — `id` = `e6_q1`

- `header`（原文照录）：`E-6 处置案`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-6（judge_type_J5 补料·旧未决 E-42.3）之实质处置采何案？层1已证内部可解、且有 09-27 v3r1 重标先例（依据件 c888158b3263）。
```

`options`（逐字原文，共 4 项）：

- `id` = `e6_q1_opt1`
  - `label`（逐字原文）：```案甲（推荐）：承认 v3r1 补料面为正式判定面```
  - `description`（逐字原文）：```result_v3r1／dataset v1.3 取代 result_v3；0 新采、0 外派、0 回改；hit 6/6 同向；须 verdict-keeper 复核＋PI 拍板```
- `id` = `e6_q1_opt2`
  - `label`（逐字原文）：```案乙：维持 result_v3，v3r1 仅作留痕登记```
  - `description`（逐字原文）：```最保守；旧面 n_distinct=1 未决状态原样存续，E-6 未实质消解```
- `id` = `e6_q1_opt3`
  - `label`（逐字原文）：```案丙：新采 J5（E 组）题面扩容```
  - `description`（逐字原文）：```须 PI 交互采集；新面另立面系谱、不溯及旧 77 件面```
- `id` = `e6_q1_opt4`
  - `label`（逐字原文）：```案丁：仅裁二值特征豁免门（不动判定面）```
  - `description`（逐字原文）：```只裁 TH-v3-19 门对二值特征之适用（与 Q2 联动）```

**题 2／4** — `id` = `e6_q2`

- `header`（原文照录）：`豁免门`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
TH-v3-19 之 n_distinct≥4 门是否豁免二值指示特征（J1–J6＋is_corr_pair 共 7 项）？二值上界＝2、恒低于 4；与 J2=b 配套体例相涉。
```

`options`（逐字原文，共 3 项）：

- `id` = `e6_q2_opt1`
  - `label`（逐字原文）：```豁免（7 项一并厘清）```
  - `description`（逐字原文）：（无此键）
- `id` = `e6_q2_opt2`
  - `label`（逐字原文）：```不豁免```
  - `description`（逐字原文）：（无此键）
- `id` = `e6_q2_opt3`
  - `label`（逐字原文）：```仅 J5 单独裁```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `e6_q3`

- `header`（原文照录）：`复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
若 Q1 采案甲：result_v3r1 升格是否即刻派 verdict-keeper 复核？
```

`options`（逐字原文，共 2 项）：

- `id` = `e6_q3_opt1`
  - `label`（逐字原文）：```即刻派```
  - `description`（逐字原文）：（无此键）
- `id` = `e6_q3_opt2`
  - `label`（逐字原文）：```暂不派```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `e6_q4`

- `header`（原文照录）：`并案`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
「三项必启用」三处同源字面（prereg §1.2.2／executor L30／L333，属 E-5 另案）是否并案同裁？
```

`options`（逐字原文，共 2 项）：

- `id` = `e6_q4_opt1`
  - `label`（逐字原文）：```并案```
  - `description`（逐字原文）：（无此键）
- `id` = `e6_q4_opt2`
  - `label`（逐字原文）：```另议（沿 E-5 边界）```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_c8d8c049d9c68775ba5f03ee","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"e6_q1","question":"E-6（judge_type_J5 补料·旧未决 E-42.3）之实质处置采何案？层1已证内部可解、且有 09-27 v3r1 重标先例（依据件 c888158b3263）。","selectionMode":"single","options":[{"id":"e6_q1_opt1","label":"案甲（推荐）：承认 v3r1 补料面为正式判定面","description":"result_v3r1／dataset v1.3 取代 result_v3；0 新采、0 外派、0 回改；hit 6/6 同向；须 verdict-keeper 复核＋PI 拍板"},{"id":"e6_q1_opt2","label":"案乙：维持 result_v3，v3r1 仅作留痕登记","description":"最保守；旧面 n_distinct=1 未决状态原样存续，E-6 未实质消解"},{"id":"e6_q1_opt3","label":"案丙：新采 J5（E 组）题面扩容","description":"须 PI 交互采集；新面另立面系谱、不溯及旧 77 件面"},{"id":"e6_q1_opt4","label":"案丁：仅裁二值特征豁免门（不动判定面）","description":"只裁 TH-v3-19 门对二值特征之适用（与 Q2 联动）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-6 处置案"},{"id":"e6_q2","question":"TH-v3-19 之 n_distinct≥4 门是否豁免二值指示特征（J1–J6＋is_corr_pair 共 7 项）？二值上界＝2、恒低于 4；与 J2=b 配套体例相涉。","selectionMode":"single","options":[{"id":"e6_q2_opt1","label":"豁免（7 项一并厘清）"},{"id":"e6_q2_opt2","label":"不豁免"},{"id":"e6_q2_opt3","label":"仅 J5 单独裁"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"豁免门"},{"id":"e6_q3","question":"若 Q1 采案甲：result_v3r1 升格是否即刻派 verdict-keeper 复核？","selectionMode":"single","options":[{"id":"e6_q3_opt1","label":"即刻派"},{"id":"e6_q3_opt2","label":"暂不派"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"复核"},{"id":"e6_q4","question":"「三项必启用」三处同源字面（prereg §1.2.2／executor L30／L333，属 E-5 另案）是否并案同裁？","selectionMode":"single","options":[{"id":"e6_q4_opt1","label":"并案"},{"id":"e6_q4_opt2","label":"另议（沿 E-5 边界）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"并案"}],"status":"pending","createdAt":1791606167604,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_42388949-9f70-43d0-8be3-0606f05c244a","toolCallId":"call_00_2R7ydmxzVfDUsDv7cRFG0275"},"title":"轮39 · E-6（judge_type_J5 补料）四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_c8d8c049d9c68775ba5f03ee","answers":[{"stepId":"e6_q1","selectedOptionIds":["e6_q1_opt1"],"selectedOther":false},{"stepId":"e6_q2","selectedOptionIds":["e6_q2_opt1"],"selectedOther":false},{"stepId":"e6_q3","selectedOptionIds":["e6_q3_opt1"],"selectedOther":false},{"stepId":"e6_q4","selectedOptionIds":["e6_q4_opt2"],"selectedOther":false}],"submittedAt":1791606232013}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `e6_q1`：`selectedOptionIds` = ["e6_q1_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `e6_q2`：`selectedOptionIds` = ["e6_q2_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `e6_q3`：`selectedOptionIds` = ["e6_q3_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `e6_q4`：`selectedOptionIds` = ["e6_q4_opt2"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `e6_q1`：`e6_q1_opt1` → 选项字面（逐字）= `案甲（推荐）：承认 v3r1 补料面为正式判定面`
- 答 2／4 — `e6_q2`：`e6_q2_opt1` → 选项字面（逐字）= `豁免（7 项一并厘清）`
- 答 3／4 — `e6_q3`：`e6_q3_opt1` → 选项字面（逐字）= `即刻派`
- 答 4／4 — `e6_q4`：`e6_q4_opt2` → 选项字面（逐字）= `另议（沿 E-5 边界）`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 11 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 02 · `ask_6e588d3357c1df300749b686` · 轮40（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮40 · D-04 与档A（S4 重生成）四项

**卡级元数据（原文照录）**

```text
request_id                     = ask_6e588d3357c1df300749b686
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮40 · D-04 与档A（S4 重生成）四项
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_893e8e9b-2d61-4bae-a0dc-845daab18912
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_C9MYd0ratHJJKvTq2Cyg2736
request_json.createdAt (epoch ms)= 1791608055605   → 2026-10-10 12:54:15.605 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791608055605
created_at (CST 换算)            = 2026-10-10 12:54:15.605 +0800
answered_at (epoch ms)         = 1791608175261
answered_at (CST 换算)           = 2026-10-10 12:56:15.261 +0800
reply_payload.submittedAt(epoch ms)= 1791608175261   → 2026-10-10 12:56:15.261 +0800
injected_at (epoch ms)         = 1791608175370
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／13 选项，原文照录）**

**题 1／4** — `id` = `d04_disp`

- `header`（原文照录）：`D-04 处置`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
D-04（C 线分母扩充）实测未达授权目标：分母 5→4、两构造 CI 上界 U≡1.0（与基线逐位相同）、构造②退化重抽样 2→5。处置采何案？
```

`options`（逐字原文，共 4 项）：

- `id` = `d04_disp_opt1`
  - `label`（逐字原文）：```甲：收束·按构造①落档——两构造读数并列在册，K-C-DEN-1 交 verdict-keeper 按 U=1.0 落档；授权目标未达如实登记```
  - `description`（逐字原文）：```构造①＝自身域（一致子集内）重采样；最小动作、0 新预登记。```
- `id` = `d04_disp_opt2`
  - `label`（逐字原文）：```乙：收束·按构造②落档——同一收束，落档基准取构造②（全体 held-out 重采样）```
  - `description`（逐字原文）：```构造②退化更重（5 次），区间质量较低。```
- `id` = `d04_disp_opt3`
  - `label`（逐字原文）：```丙：重试·改抽取域/母体/估计量（estimand 面）——另立新预登记后重跑```
  - `description`（逐字原文）：```触及 estimand 口径，须先立新抽取向导与判死线。```
- `id` = `d04_disp_opt4`
  - `label`（逐字原文）：```丁：暂缓·挂账——本线暂不推进，入挂账候后议```
  - `description`（逐字原文）：```0 落档、0 重跑；D-04 保持未闭。```

**题 2／4** — `id` = `za_x5`

- `header`（原文照录）：`档A·C-3 择案`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
档A（S4 重生成执行方案）C-3 模型侧处置之择案采何案？背景：模型侧对 V3 词表双耦合（训练标签＋n_keywords_hit 特征层）；方案件推荐案甲。
```

`options`（逐字原文，共 3 项）：

- `id` = `za_x5_opt1`
  - `label`（逐字原文）：```案甲（推荐）：持 V3 树＋显式标注混合——训练标签与 n_keywords_hit 皆沿 V3；新读数附机械效应折扣声明```
  - `description`（逐字原文）：```单一变量可归因、成本最低、0 需新预登记；诚实折扣：新读数大概率不如旧读数好看，差值含覆盖扩大之机械效应。```
- `id` = `za_x5_opt2`
  - `label`（逐字原文）：```案乙：shadow 双树对照——V3.1 训练标签＋V3.1 特征，双树并出对照读数```
  - `description`（逐字原文）：```可分离版本效应；成本约 2 倍。```
- `id` = `za_x5_opt3`
  - `label`（逐字原文）：```案丙：暂缓出读数面——0 出读数，仅出逐件 gold/登记```
  - `description`（逐字原文）：```工作量最省；读数面候后议。```

**题 3／4** — `id` = `za_x7`

- `header`（原文照录）：`档A·V3.1 范围`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3.1 词表采纳范围采何案？（T2 边际 9 词中「检验」「后面」为 D8-38 转非空之全部依据；S4Q-04 之「保证／质量」层级归属另候）
```

`options`（逐字原文，共 3 项）：

- `id` = `za_x7_opt1`
  - `label`（逐字原文）：```全 15 词（T1 6＋T2 9）```
  - `description`（逐字原文）：```held-out 已非空 7/9。```
- `id` = `za_x7_opt2`
  - `label`（逐字原文）：```仅 T1 6 词（复核/质量/保证/回退/遗忘/推翻）```
  - `description`（逐字原文）：```held-out 已非空 5/9。```
- `id` = `za_x7_opt3`
  - `label`（逐字原文）：```全 15 词但弃「检验」＋「后面」```
  - `description`（逐字原文）：```held-out 已非空 6/9；二者为 D8-38 转非空之全部依据。```

**题 4／4** — `id` = `za_x1x4`

- `header`（原文照录）：`档A·四代立草案`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
档A 四代立草案是否按草案字面核准？（X1「C-3」专指模型侧处置；X2 择案集扩充为甲/乙/丙且禁训练推理混口径；X3 漂移登记以 26 件全量逐件为分母；X4 V-CLAUSE-1.6 改「新件内位移＋不覆写」字面。草案全文见方案件 §8）
```

`options`（逐字原文，共 3 项）：

- `id` = `za_x1x4_opt1`
  - `label`（逐字原文）：```按草案核准（四项全准）```
  - `description`（逐字原文）：（无此键）
- `id` = `za_x1x4_opt2`
  - `label`（逐字原文）：```需改字（Other 逐项注明）```
  - `description`（逐字原文）：（无此键）
- `id` = `za_x1x4_opt3`
  - `label`（逐字原文）：```暂缓（另轮逐项评）```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_6e588d3357c1df300749b686","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"d04_disp","question":"D-04（C 线分母扩充）实测未达授权目标：分母 5→4、两构造 CI 上界 U≡1.0（与基线逐位相同）、构造②退化重抽样 2→5。处置采何案？","selectionMode":"single","options":[{"id":"d04_disp_opt1","label":"甲：收束·按构造①落档——两构造读数并列在册，K-C-DEN-1 交 verdict-keeper 按 U=1.0 落档；授权目标未达如实登记","description":"构造①＝自身域（一致子集内）重采样；最小动作、0 新预登记。"},{"id":"d04_disp_opt2","label":"乙：收束·按构造②落档——同一收束，落档基准取构造②（全体 held-out 重采样）","description":"构造②退化更重（5 次），区间质量较低。"},{"id":"d04_disp_opt3","label":"丙：重试·改抽取域/母体/估计量（estimand 面）——另立新预登记后重跑","description":"触及 estimand 口径，须先立新抽取向导与判死线。"},{"id":"d04_disp_opt4","label":"丁：暂缓·挂账——本线暂不推进，入挂账候后议","description":"0 落档、0 重跑；D-04 保持未闭。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"D-04 处置"},{"id":"za_x5","question":"档A（S4 重生成执行方案）C-3 模型侧处置之择案采何案？背景：模型侧对 V3 词表双耦合（训练标签＋n_keywords_hit 特征层）；方案件推荐案甲。","selectionMode":"single","options":[{"id":"za_x5_opt1","label":"案甲（推荐）：持 V3 树＋显式标注混合——训练标签与 n_keywords_hit 皆沿 V3；新读数附机械效应折扣声明","description":"单一变量可归因、成本最低、0 需新预登记；诚实折扣：新读数大概率不如旧读数好看，差值含覆盖扩大之机械效应。"},{"id":"za_x5_opt2","label":"案乙：shadow 双树对照——V3.1 训练标签＋V3.1 特征，双树并出对照读数","description":"可分离版本效应；成本约 2 倍。"},{"id":"za_x5_opt3","label":"案丙：暂缓出读数面——0 出读数，仅出逐件 gold/登记","description":"工作量最省；读数面候后议。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"档A·C-3 择案"},{"id":"za_x7","question":"V3.1 词表采纳范围采何案？（T2 边际 9 词中「检验」「后面」为 D8-38 转非空之全部依据；S4Q-04 之「保证／质量」层级归属另候）","selectionMode":"single","options":[{"id":"za_x7_opt1","label":"全 15 词（T1 6＋T2 9）","description":"held-out 已非空 7/9。"},{"id":"za_x7_opt2","label":"仅 T1 6 词（复核/质量/保证/回退/遗忘/推翻）","description":"held-out 已非空 5/9。"},{"id":"za_x7_opt3","label":"全 15 词但弃「检验」＋「后面」","description":"held-out 已非空 6/9；二者为 D8-38 转非空之全部依据。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"档A·V3.1 范围"},{"id":"za_x1x4","question":"档A 四代立草案是否按草案字面核准？（X1「C-3」专指模型侧处置；X2 择案集扩充为甲/乙/丙且禁训练推理混口径；X3 漂移登记以 26 件全量逐件为分母；X4 V-CLAUSE-1.6 改「新件内位移＋不覆写」字面。草案全文见方案件 §8）","selectionMode":"single","options":[{"id":"za_x1x4_opt1","label":"按草案核准（四项全准）"},{"id":"za_x1x4_opt2","label":"需改字（Other 逐项注明）"},{"id":"za_x1x4_opt3","label":"暂缓（另轮逐项评）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"档A·四代立草案"}],"status":"pending","createdAt":1791608055605,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_893e8e9b-2d61-4bae-a0dc-845daab18912","toolCallId":"call_00_C9MYd0ratHJJKvTq2Cyg2736"},"title":"轮40 · D-04 与档A（S4 重生成）四项"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_6e588d3357c1df300749b686","answers":[{"stepId":"d04_disp","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"},{"stepId":"za_x5","selectedOptionIds":["za_x5_opt1"],"selectedOther":false},{"stepId":"za_x7","selectedOptionIds":["za_x7_opt1"],"selectedOther":false},{"stepId":"za_x1x4","selectedOptionIds":["za_x1x4_opt1"],"selectedOther":false}],"submittedAt":1791608175261}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `d04_disp`：`selectedOptionIds` = []；`selectedOther` = true；`otherText` = "另议"
答 2／4 — `stepId` = `za_x5`：`selectedOptionIds` = ["za_x5_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `za_x7`：`selectedOptionIds` = ["za_x7_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `za_x1x4`：`selectedOptionIds` = ["za_x1x4_opt1"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `d04_disp`：**Other**（`selectedOther` = true），`otherText`（逐字）= `另议`；`selectedOptionIds` = []（空）
- 答 2／4 — `za_x5`：`za_x5_opt1` → 选项字面（逐字）= `案甲（推荐）：持 V3 树＋显式标注混合——训练标签与 n_keywords_hit 皆沿 V3；新读数附机械效应折扣声明`
- 答 3／4 — `za_x7`：`za_x7_opt1` → 选项字面（逐字）= `全 15 词（T1 6＋T2 9）`
- 答 4／4 — `za_x1x4`：`za_x1x4_opt1` → 选项字面（逐字）= `按草案核准（四项全准）`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 13 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 03 · `ask_38cfeded4238be5321e93cef` · 轮41（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮41 · 落档与续项四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_38cfeded4238be5321e93cef
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮41 · 落档与续项四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_9a558a23-58e2-4762-8ece-e4213977e1c4
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_DtFEZ20pbLbotMbMZMcE3208
request_json.createdAt (epoch ms)= 1791608427136   → 2026-10-10 13:00:27.136 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791608427136
created_at (CST 换算)            = 2026-10-10 13:00:27.136 +0800
answered_at (epoch ms)         = 1791608743679
answered_at (CST 换算)           = 2026-10-10 13:05:43.679 +0800
reply_payload.submittedAt(epoch ms)= 1791608743679   → 2026-10-10 13:05:43.679 +0800
injected_at (epoch ms)         = 1791608743842
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／10 选项，原文照录）**

**题 1／4** — `id` = `e6_j5sem`

- `header`（原文照录）：`E-6·J5 语义`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-6 升格件（4e65c53f68e8）发现 judge_type_J5 语义两处互斥：prereg/ruleset＝「RISK 子类判定」 vs 题库＝「时机」（重标采题库读法）。以何者为准？
```

`options`（逐字原文，共 2 项）：

- `id` = `e6_j5sem_opt1`
  - `label`（逐字原文）：```甲：采题库读法「时机」——维持现有升格（AC-1/AC-3 语义成立）```
  - `description`（逐字原文）：```沿 09-27 D4 重标所采读法；升格件现行状态不变。```
- `id` = `e6_j5sem_opt2`
  - `label`（逐字原文）：```乙：采 prereg/ruleset 读法「RISK 子类」——升格之 AC-1/AC-3 语义失效，须另行处置```
  - `description`（逐字原文）：```升格件已设条件性条款；若选此，另派处置棒。```

**题 2／4** — `id` = `b_close`

- `header`（原文照录）：`B·巧合落档`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
B 线「3/7 逐位同值」之落档采何结论？（三检＋复核链已结：改分母 9/26·6/23、交集 2 件、5/12 均未复现；「构造依赖之计数巧合」为最相容解释）
```

`options`（逐字原文，共 3 项）：

- `id` = `b_close_opt1`
  - `label`（逐字原文）：```甲：登记为「构造依赖之计数巧合」（最相容解释）·不宣告排除```
  - `description`（逐字原文）：```沿 D-05 与复核件之未宣告口径。```
- `id` = `b_close_opt2`
  - `label`（逐字原文）：```乙：宣告「已排除」```
  - `description`（逐字原文）：```与两件未宣告口径相悖；须以更强论证为据。```
- `id` = `b_close_opt3`
  - `label`（逐字原文）：```丙：另议```
  - `description`（逐字原文）：```派独立判断棒。```

**题 3／4** — `id` = `exp05_e1`

- `header`（原文照录）：`EXP-05·E1`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
EXP-05（P-B V0 MISSING_TRUE 两件）E1：C4 四值（u*(a_t)／L／U／max_u）仍候 PI 另给，或确认无法给料？
```

`options`（逐字原文，共 2 项）：

- `id` = `exp05_e1_opt1`
  - `label`（逐字原文）：```甲：仍候 PI 另给（挂账继续候）```
  - `description`（逐字原文）：```候补件通道维持。```
- `id` = `exp05_e1_opt2`
  - `label`（逐字原文）：```乙：确认无法给料 ⇒ 依五终判新令落 KD```
  - `description`（逐字原文）：```「实在无法给料→可判KD」；候补/对冲条款随该档处置。```

**题 4／4** — `id` = `za_x6`

- `header`（原文照录）：`档A·X6`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
档A：档B 三件（Q39／DF6-1／DF1-6，与本轮同属 held-out 26 件面）与本轮 V3.1 重生成是否同施？
```

`options`（逐字原文，共 3 项）：

- `id` = `za_x6_opt1`
  - `label`（逐字原文）：```甲（推荐）：不同施——本轮仅 V3.1 抽取，档B 另棒```
  - `description`（逐字原文）：```版本冲突面（RK-5）归零；沿方案件「0 主张同施」。```
- `id` = `za_x6_opt2`
  - `label`（逐字原文）：```乙：同施——两链叠加，须另立合成口径```
  - `description`（逐字原文）：```须先立合成口径预登记。```
- `id` = `za_x6_opt3`
  - `label`（逐字原文）：```丙：先闭 T-S3-3 判死线口径再议```
  - `description`（逐字原文）：```T-S3-3 残留处置先行。```

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_38cfeded4238be5321e93cef","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"e6_j5sem","question":"E-6 升格件（4e65c53f68e8）发现 judge_type_J5 语义两处互斥：prereg/ruleset＝「RISK 子类判定」 vs 题库＝「时机」（重标采题库读法）。以何者为准？","selectionMode":"single","options":[{"id":"e6_j5sem_opt1","label":"甲：采题库读法「时机」——维持现有升格（AC-1/AC-3 语义成立）","description":"沿 09-27 D4 重标所采读法；升格件现行状态不变。"},{"id":"e6_j5sem_opt2","label":"乙：采 prereg/ruleset 读法「RISK 子类」——升格之 AC-1/AC-3 语义失效，须另行处置","description":"升格件已设条件性条款；若选此，另派处置棒。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-6·J5 语义"},{"id":"b_close","question":"B 线「3/7 逐位同值」之落档采何结论？（三检＋复核链已结：改分母 9/26·6/23、交集 2 件、5/12 均未复现；「构造依赖之计数巧合」为最相容解释）","selectionMode":"single","options":[{"id":"b_close_opt1","label":"甲：登记为「构造依赖之计数巧合」（最相容解释）·不宣告排除","description":"沿 D-05 与复核件之未宣告口径。"},{"id":"b_close_opt2","label":"乙：宣告「已排除」","description":"与两件未宣告口径相悖；须以更强论证为据。"},{"id":"b_close_opt3","label":"丙：另议","description":"派独立判断棒。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"B·巧合落档"},{"id":"exp05_e1","question":"EXP-05（P-B V0 MISSING_TRUE 两件）E1：C4 四值（u*(a_t)／L／U／max_u）仍候 PI 另给，或确认无法给料？","selectionMode":"single","options":[{"id":"exp05_e1_opt1","label":"甲：仍候 PI 另给（挂账继续候）","description":"候补件通道维持。"},{"id":"exp05_e1_opt2","label":"乙：确认无法给料 ⇒ 依五终判新令落 KD","description":"「实在无法给料→可判KD」；候补/对冲条款随该档处置。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"EXP-05·E1"},{"id":"za_x6","question":"档A：档B 三件（Q39／DF6-1／DF1-6，与本轮同属 held-out 26 件面）与本轮 V3.1 重生成是否同施？","selectionMode":"single","options":[{"id":"za_x6_opt1","label":"甲（推荐）：不同施——本轮仅 V3.1 抽取，档B 另棒","description":"版本冲突面（RK-5）归零；沿方案件「0 主张同施」。"},{"id":"za_x6_opt2","label":"乙：同施——两链叠加，须另立合成口径","description":"须先立合成口径预登记。"},{"id":"za_x6_opt3","label":"丙：先闭 T-S3-3 判死线口径再议","description":"T-S3-3 残留处置先行。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"档A·X6"}],"status":"pending","createdAt":1791608427136,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_9a558a23-58e2-4762-8ece-e4213977e1c4","toolCallId":"call_00_DtFEZ20pbLbotMbMZMcE3208"},"title":"轮41 · 落档与续项四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_38cfeded4238be5321e93cef","answers":[{"stepId":"e6_j5sem","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"},{"stepId":"b_close","selectedOptionIds":["b_close_opt3"],"selectedOther":false},{"stepId":"exp05_e1","selectedOptionIds":[],"selectedOther":true,"otherText":"外派英文委托稿"},{"stepId":"za_x6","selectedOptionIds":["za_x6_opt1"],"selectedOther":false}],"submittedAt":1791608743679}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `e6_j5sem`：`selectedOptionIds` = []；`selectedOther` = true；`otherText` = "另议"
答 2／4 — `stepId` = `b_close`：`selectedOptionIds` = ["b_close_opt3"]；`selectedOther` = false
答 3／4 — `stepId` = `exp05_e1`：`selectedOptionIds` = []；`selectedOther` = true；`otherText` = "外派英文委托稿"
答 4／4 — `stepId` = `za_x6`：`selectedOptionIds` = ["za_x6_opt1"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `e6_j5sem`：**Other**（`selectedOther` = true），`otherText`（逐字）= `另议`；`selectedOptionIds` = []（空）
- 答 2／4 — `b_close`：`b_close_opt3` → 选项字面（逐字）= `丙：另议`
- 答 3／4 — `exp05_e1`：**Other**（`selectedOther` = true），`otherText`（逐字）= `外派英文委托稿`；`selectedOptionIds` = []（空）
- 答 4／4 — `za_x6`：`za_x6_opt1` → 选项字面（逐字）= `甲（推荐）：不同施——本轮仅 V3.1 抽取，档B 另棒`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 10 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 04 · `ask_36de432448367350571a9de7` · 轮42（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮42 · 终裁与开跑门四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_36de432448367350571a9de7
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮42 · 终裁与开跑门四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_05898c21-e09d-4c1c-9a31-80d9a4badf76
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_QONlx41nNJuh5ugFSYua8168
request_json.createdAt (epoch ms)= 1791609168246   → 2026-10-10 13:12:48.246 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791609168246
created_at (CST 换算)            = 2026-10-10 13:12:48.246 +0800
answered_at (epoch ms)         = 1791609209981
answered_at (CST 换算)           = 2026-10-10 13:13:29.981 +0800
reply_payload.submittedAt(epoch ms)= 1791609209981   → 2026-10-10 13:13:29.981 +0800
injected_at (epoch ms)         = 1791609210074
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／10 选项，原文照录）**

**题 1／4** — `id` = `d04_final`

- `header`（原文照录）：`D-04 终裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
D-04 终裁：判断件推荐「收束并陈＋保留 K-C-DEN-1 并登记空门」；「n 所指」张力＝固定登记「目标 9 于现基底不可达」（母体一致件恒 5·组合学不可达；U≡1.0 系机械上界）。采何处置？
```

`options`（逐字原文，共 3 项）：

- `id` = `d04_final_opt1`
  - `label`（逐字原文）：```甲：接受推荐——收束并陈（两构造并列）＋保留线并登记空门＋n 张力固定登记```
  - `description`（逐字原文）：（无此键）
- `id` = `d04_final_opt2`
  - `label`（逐字原文）：```乙：改域重试——另立新基底预登记（判断件载：非重试、乃新基底）```
  - `description`（逐字原文）：（无此键）
- `id` = `d04_final_opt3`
  - `label`（逐字原文）：```丙：暂缓——挂账候后议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `s4q04_g3`

- `header`（原文照录）：`开跑门 G3`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
档A·开跑门 G3：S4Q-04 之「保证／质量」层级归属采何者？此门与已闭之 G4（档B 同施）并列阻断重生成开跑，G3 闭后方可开跑。沿 6efddab54ca5 §6 反方一之真实争议面。
```

`options`（逐字原文，共 2 项）：

- `id` = `s4q04_g3_opt1`
  - `label`（逐字原文）：```甲：归 CRITERIA```
  - `description`（逐字原文）：（无此键）
- `id` = `s4q04_g3_opt2`
  - `label`（逐字原文）：```乙：归 DELEGATE```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `za_eff`

- `header`（原文照录）：`档A 四件生效`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
档A 四件（词表定稿／K-EX 冻结／执行序／V-CLAUSE-1.6′）是否复核生效（生效即锁）？四件已随附并落盘。
```

`options`（逐字原文，共 3 项）：

- `id` = `za_eff_opt1`
  - `label`（逐字原文）：```甲：四件全准·生效```
  - `description`（逐字原文）：（无此键）
- `id` = `za_eff_opt2`
  - `label`（逐字原文）：```乙：需改（Other 逐件注明）```
  - `description`（逐字原文）：（无此键）
- `id` = `za_eff_opt3`
  - `label`（逐字原文）：```丙：暂缓（另轮逐件评）```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `e6_exit1`

- `header`（原文照录）：`E-6 出口①`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-6 出口①：升格后判定面（v3r1）与原裁因件（verdict_v3）口径错配（升格面上 perm_p 0.0160→0.1279 等）——裁因是否随之重出？
```

`options`（逐字原文，共 2 项）：

- `id` = `e6_exit1_opt1`
  - `label`（逐字原文）：```甲：另出裁因复核/重出件（随升格面）```
  - `description`（逐字原文）：（无此键）
- `id` = `e6_exit1_opt2`
  - `label`（逐字原文）：```乙：不重出——登记口径错配即可（0 回改裁因件）```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_36de432448367350571a9de7","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"d04_final","question":"D-04 终裁：判断件推荐「收束并陈＋保留 K-C-DEN-1 并登记空门」；「n 所指」张力＝固定登记「目标 9 于现基底不可达」（母体一致件恒 5·组合学不可达；U≡1.0 系机械上界）。采何处置？","selectionMode":"single","options":[{"id":"d04_final_opt1","label":"甲：接受推荐——收束并陈（两构造并列）＋保留线并登记空门＋n 张力固定登记"},{"id":"d04_final_opt2","label":"乙：改域重试——另立新基底预登记（判断件载：非重试、乃新基底）"},{"id":"d04_final_opt3","label":"丙：暂缓——挂账候后议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"D-04 终裁"},{"id":"s4q04_g3","question":"档A·开跑门 G3：S4Q-04 之「保证／质量」层级归属采何者？此门与已闭之 G4（档B 同施）并列阻断重生成开跑，G3 闭后方可开跑。沿 6efddab54ca5 §6 反方一之真实争议面。","selectionMode":"single","options":[{"id":"s4q04_g3_opt1","label":"甲：归 CRITERIA"},{"id":"s4q04_g3_opt2","label":"乙：归 DELEGATE"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"开跑门 G3"},{"id":"za_eff","question":"档A 四件（词表定稿／K-EX 冻结／执行序／V-CLAUSE-1.6′）是否复核生效（生效即锁）？四件已随附并落盘。","selectionMode":"single","options":[{"id":"za_eff_opt1","label":"甲：四件全准·生效"},{"id":"za_eff_opt2","label":"乙：需改（Other 逐件注明）"},{"id":"za_eff_opt3","label":"丙：暂缓（另轮逐件评）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"档A 四件生效"},{"id":"e6_exit1","question":"E-6 出口①：升格后判定面（v3r1）与原裁因件（verdict_v3）口径错配（升格面上 perm_p 0.0160→0.1279 等）——裁因是否随之重出？","selectionMode":"single","options":[{"id":"e6_exit1_opt1","label":"甲：另出裁因复核/重出件（随升格面）"},{"id":"e6_exit1_opt2","label":"乙：不重出——登记口径错配即可（0 回改裁因件）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-6 出口①"}],"status":"pending","createdAt":1791609168246,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_05898c21-e09d-4c1c-9a31-80d9a4badf76","toolCallId":"call_00_QONlx41nNJuh5ugFSYua8168"},"title":"轮42 · 终裁与开跑门四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_36de432448367350571a9de7","answers":[{"stepId":"d04_final","selectedOptionIds":["d04_final_opt1"],"selectedOther":false},{"stepId":"s4q04_g3","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"},{"stepId":"za_eff","selectedOptionIds":["za_eff_opt1"],"selectedOther":false},{"stepId":"e6_exit1","selectedOptionIds":["e6_exit1_opt1"],"selectedOther":false}],"submittedAt":1791609209981}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `d04_final`：`selectedOptionIds` = ["d04_final_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `s4q04_g3`：`selectedOptionIds` = []；`selectedOther` = true；`otherText` = "另议"
答 3／4 — `stepId` = `za_eff`：`selectedOptionIds` = ["za_eff_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `e6_exit1`：`selectedOptionIds` = ["e6_exit1_opt1"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `d04_final`：`d04_final_opt1` → 选项字面（逐字）= `甲：接受推荐——收束并陈（两构造并列）＋保留线并登记空门＋n 张力固定登记`
- 答 2／4 — `s4q04_g3`：**Other**（`selectedOther` = true），`otherText`（逐字）= `另议`；`selectedOptionIds` = []（空）
- 答 3／4 — `za_eff`：`za_eff_opt1` → 选项字面（逐字）= `甲：四件全准·生效`
- 答 4／4 — `e6_exit1`：`e6_exit1_opt1` → 选项字面（逐字）= `甲：另出裁因复核/重出件（随升格面）`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 10 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 05 · `ask_e5c5a8e874391fc6845971f1` · 轮43（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮43 · 判断终裁与委托定发四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_e5c5a8e874391fc6845971f1
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮43 · 判断终裁与委托定发四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_7c952016-11bb-4fa9-af53-5749968f5fb4
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_8wf56CjeOCNdycLx2AuZ4854
request_json.createdAt (epoch ms)= 1791609821339   → 2026-10-10 13:23:41.339 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791609821339
created_at (CST 换算)            = 2026-10-10 13:23:41.339 +0800
answered_at (epoch ms)         = 1791609931818
answered_at (CST 换算)           = 2026-10-10 13:25:31.818 +0800
reply_payload.submittedAt(epoch ms)= 1791609931818   → 2026-10-10 13:25:31.818 +0800
injected_at (epoch ms)         = 1791609931885
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／13 选项，原文照录）**

**题 1／4** — `id` = `e6j5_final`

- `header`（原文照录）：`E-6·J5 终裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
E-6·J5 语义互斥终裁：判断件推荐「题库读法（J5＝时机／executor TIMING）」；RISK 读法支撑未弱化；另有第三径「语义层与计算层分离」。采何者？
```

`options`（逐字原文，共 3 项）：

- `id` = `e6j5_final_opt1`
  - `label`（逐字原文）：```甲：题库读法（推荐）——另出勘误注记＋同批处置 L60，0 回改```
  - `description`（逐字原文）：（无此键）
- `id` = `e6j5_final_opt2`
  - `label`（逐字原文）：```乙：RISK 读法——重标重做、AC-1/AC-3 语义失效、另出新判定件（六线方向不翻）```
  - `description`（逐字原文）：（无此键）
- `id` = `e6j5_final_opt3`
  - `label`（逐字原文）：```丙：第三径——语义层与计算层分离，数值层成立、描述偏差登记不溯及```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `b_final`

- `header`（原文照录）：`B 落档终裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
B 线「3/7 逐位同值」落档终裁：判断件载三检近乎无判别力、「巧合」不成立为结论；推荐闭合转口径事实登记（kd）·不建议宣告排除。采何者？
```

`options`（逐字原文，共 4 项）：

- `id` = `b_final_opt1`
  - `label`（逐字原文）：```甲（推荐）：闭合——按判断件四层转口径事实登记（kd），维持「0 断言两面等价」```
  - `description`（逐字原文）：（无此键）
- `id` = `b_final_opt2`
  - `label`（逐字原文）：```乙：先派率检验棒（PI 先立零假设）——测后再闭```
  - `description`（逐字原文）：（无此键）
- `id` = `b_final_opt3`
  - `label`（逐字原文）：```丙：维持开放——原措辞＋「不可判」限定（挂账）```
  - `description`（逐字原文）：（无此键）
- `id` = `b_final_opt4`
  - `label`（逐字原文）：```丁：宣告「已排除」（判断件不建议）```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `s4q04_final`

- `header`（原文照录）：`G3·S4Q-04 终裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
档A·G3 终裁：S4Q-04「保证／质量」层级——判断件倾向甲 CRITERIA（F4 下仅甲相容）；两读法数值全同（pred 恒 UNKNOWN、位移 19 同、已出读数 0 影响），被裁者系归属方法正当性；另有 E-1b（「质量→TIMING」有面证据）/E-1c（分词定层）。采何者？
```

`options`（逐字原文，共 3 项）：

- `id` = `s4q04_final_opt1`
  - `label`（逐字原文）：```甲：CRITERIA（判断件倾向）```
  - `description`（逐字原文）：（无此键）
- `id` = `s4q04_final_opt2`
  - `label`（逐字原文）：```乙：DELEGATE```
  - `description`（逐字原文）：（无此键）
- `id` = `s4q04_final_opt3`
  - `label`（逐字原文）：```丙：分词定层（「保证」「质量」分别定层——沿 E-1c）```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `exp05_send`

- `header`（原文照录）：`EXP-05 委托稿`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
EXP-05 英文委托稿（草案）——是否定发？收件方与期限未定；稿含 5 出口：不发／canonical 点名方／另一外部方／PI 自身／人力源。
```

`options`（逐字原文，共 3 项）：

- `id` = `exp05_send_opt1`
  - `label`（逐字原文）：```甲：照稿定发——收件方与期限请于 Other 指定```
  - `description`（逐字原文）：（无此键）
- `id` = `exp05_send_opt2`
  - `label`（逐字原文）：```乙：需改（Other 逐项注明）```
  - `description`（逐字原文）：（无此键）
- `id` = `exp05_send_opt3`
  - `label`（逐字原文）：```丙：暂缓```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_e5c5a8e874391fc6845971f1","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"e6j5_final","question":"E-6·J5 语义互斥终裁：判断件推荐「题库读法（J5＝时机／executor TIMING）」；RISK 读法支撑未弱化；另有第三径「语义层与计算层分离」。采何者？","selectionMode":"single","options":[{"id":"e6j5_final_opt1","label":"甲：题库读法（推荐）——另出勘误注记＋同批处置 L60，0 回改"},{"id":"e6j5_final_opt2","label":"乙：RISK 读法——重标重做、AC-1/AC-3 语义失效、另出新判定件（六线方向不翻）"},{"id":"e6j5_final_opt3","label":"丙：第三径——语义层与计算层分离，数值层成立、描述偏差登记不溯及"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-6·J5 终裁"},{"id":"b_final","question":"B 线「3/7 逐位同值」落档终裁：判断件载三检近乎无判别力、「巧合」不成立为结论；推荐闭合转口径事实登记（kd）·不建议宣告排除。采何者？","selectionMode":"single","options":[{"id":"b_final_opt1","label":"甲（推荐）：闭合——按判断件四层转口径事实登记（kd），维持「0 断言两面等价」"},{"id":"b_final_opt2","label":"乙：先派率检验棒（PI 先立零假设）——测后再闭"},{"id":"b_final_opt3","label":"丙：维持开放——原措辞＋「不可判」限定（挂账）"},{"id":"b_final_opt4","label":"丁：宣告「已排除」（判断件不建议）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"B 落档终裁"},{"id":"s4q04_final","question":"档A·G3 终裁：S4Q-04「保证／质量」层级——判断件倾向甲 CRITERIA（F4 下仅甲相容）；两读法数值全同（pred 恒 UNKNOWN、位移 19 同、已出读数 0 影响），被裁者系归属方法正当性；另有 E-1b（「质量→TIMING」有面证据）/E-1c（分词定层）。采何者？","selectionMode":"single","options":[{"id":"s4q04_final_opt1","label":"甲：CRITERIA（判断件倾向）"},{"id":"s4q04_final_opt2","label":"乙：DELEGATE"},{"id":"s4q04_final_opt3","label":"丙：分词定层（「保证」「质量」分别定层——沿 E-1c）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"G3·S4Q-04 终裁"},{"id":"exp05_send","question":"EXP-05 英文委托稿（草案）——是否定发？收件方与期限未定；稿含 5 出口：不发／canonical 点名方／另一外部方／PI 自身／人力源。","selectionMode":"single","options":[{"id":"exp05_send_opt1","label":"甲：照稿定发——收件方与期限请于 Other 指定"},{"id":"exp05_send_opt2","label":"乙：需改（Other 逐项注明）"},{"id":"exp05_send_opt3","label":"丙：暂缓"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"EXP-05 委托稿"}],"status":"pending","createdAt":1791609821339,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_7c952016-11bb-4fa9-af53-5749968f5fb4","toolCallId":"call_00_8wf56CjeOCNdycLx2AuZ4854"},"title":"轮43 · 判断终裁与委托定发四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_e5c5a8e874391fc6845971f1","answers":[{"stepId":"e6j5_final","selectedOptionIds":["e6j5_final_opt1"],"selectedOther":false},{"stepId":"b_final","selectedOptionIds":["b_final_opt1"],"selectedOther":false},{"stepId":"s4q04_final","selectedOptionIds":["s4q04_final_opt1"],"selectedOther":false},{"stepId":"exp05_send","selectedOptionIds":[],"selectedOther":true,"otherText":"不指定收件方与期限"}],"submittedAt":1791609931818}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `e6j5_final`：`selectedOptionIds` = ["e6j5_final_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `b_final`：`selectedOptionIds` = ["b_final_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `s4q04_final`：`selectedOptionIds` = ["s4q04_final_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `exp05_send`：`selectedOptionIds` = []；`selectedOther` = true；`otherText` = "不指定收件方与期限"

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `e6j5_final`：`e6j5_final_opt1` → 选项字面（逐字）= `甲：题库读法（推荐）——另出勘误注记＋同批处置 L60，0 回改`
- 答 2／4 — `b_final`：`b_final_opt1` → 选项字面（逐字）= `甲（推荐）：闭合——按判断件四层转口径事实登记（kd），维持「0 断言两面等价」`
- 答 3／4 — `s4q04_final`：`s4q04_final_opt1` → 选项字面（逐字）= `甲：CRITERIA（判断件倾向）`
- 答 4／4 — `exp05_send`：**Other**（`selectedOther` = true），`otherText`（逐字）= `不指定收件方与期限`；`selectedOptionIds` = []（空）

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 13 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

### 06 · `ask_dde5c7e4cb782427cde5f2ad` · 轮44（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮44 · 草案核准与收口四问

**卡级元数据（原文照录）**

```text
request_id                     = ask_dde5c7e4cb782427cde5f2ad
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮44 · 草案核准与收口四问
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName            = mavis
requester.runId                = turn_e022fcbd-3716-4ffd-95bf-559a838b4f3c
requester.sessionId            = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId           = call_00_JRhO7tQQqrGJqfZKWo2O3667
request_json.createdAt (epoch ms)= 1791610872005   → 2026-10-10 13:41:12.005 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791610872005
created_at (CST 换算)            = 2026-10-10 13:41:12.005 +0800
answered_at (epoch ms)         = 1791610906564
answered_at (CST 换算)           = 2026-10-10 13:41:46.564 +0800
reply_payload.submittedAt(epoch ms)= 1791610906564   → 2026-10-10 13:41:46.564 +0800
injected_at (epoch ms)         = 1791610908774
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／9 选项，原文照录）**

**题 1／4** — `id` = `u23_approve`

- `header`（原文照录）：`U-2/U-3 草案核准`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
五终判 U-2/U-3 代立草案包：推荐组合＝U-2a-A（af 为终判档·独立落档）＋U-2b-A（仅剔装载缺陷族·单侧·逐件 idx·强制限定语）＋U-3 G-1+G-2（主体终止＋资源耗尽）。采何？
```

`options`（逐字原文，共 3 项）：

- `id` = `u23_approve_opt1`
  - `label`（逐字原文）：```甲：按推荐组合核准（两件草案据此生效）```
  - `description`（逐字原文）：（无此键）
- `id` = `u23_approve_opt2`
  - `label`（逐字原文）：```乙：需改（Other 逐项注明）```
  - `description`（逐字原文）：（无此键）
- `id` = `u23_approve_opt3`
  - `label`（逐字原文）：```丙：逐项细裁（另轮逐出口评）```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `za_x8`

- `header`（原文照录）：`档A·X8（G5）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
档A·X8（G5 位移处置）：若新读数实质位移（尤以 A′ 为要——其精度面已落定「不达标」），采何处置？另：位移显著阈值口径盘上未载，可于 Other 一并给。
```

`options`（逐字原文，共 2 项）：

- `id` = `za_x8_opt1`
  - `label`（逐字原文）：```甲：另开重判面```
  - `description`（逐字原文）：（无此键）
- `id` = `za_x8_opt2`
  - `label`（逐字原文）：```乙：新旧并存并陈（沿 a330273b981c §9 E3）```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `kd_x7`

- `header`（原文照录）：`KD·X-7`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD·X-7：登录件 §6-5 之点名不成立（708dfac55be9 对 13 枚旧指纹 0 命中；点名 3 件中 1 件不成立；漏载 40 件）——是否更正？
```

`options`（逐字原文，共 2 项）：

- `id` = `kd_x7_opt1`
  - `label`（逐字原文）：```甲：另出修订件更正（0 回改登录件）```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_x7_opt2`
  - `label`（逐字原文）：```乙：维持原样```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `wf_u1`

- `header`（原文照录）：`五终判·U-1`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
五终判·U-1：三态框架指引件（708dfac55be9）之 0 回改处置——维持原字＋新件取代（裁定件主张），或另出 v2 修订指引件正文？
```

`options`（逐字原文，共 2 项）：

- `id` = `wf_u1_opt1`
  - `label`（逐字原文）：```甲：维持原字＋新件取代```
  - `description`（逐字原文）：（无此键）
- `id` = `wf_u1_opt2`
  - `label`（逐字原文）：```乙：另出 v2 修订正文```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_dde5c7e4cb782427cde5f2ad","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"u23_approve","question":"五终判 U-2/U-3 代立草案包：推荐组合＝U-2a-A（af 为终判档·独立落档）＋U-2b-A（仅剔装载缺陷族·单侧·逐件 idx·强制限定语）＋U-3 G-1+G-2（主体终止＋资源耗尽）。采何？","selectionMode":"single","options":[{"id":"u23_approve_opt1","label":"甲：按推荐组合核准（两件草案据此生效）"},{"id":"u23_approve_opt2","label":"乙：需改（Other 逐项注明）"},{"id":"u23_approve_opt3","label":"丙：逐项细裁（另轮逐出口评）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"U-2/U-3 草案核准"},{"id":"za_x8","question":"档A·X8（G5 位移处置）：若新读数实质位移（尤以 A′ 为要——其精度面已落定「不达标」），采何处置？另：位移显著阈值口径盘上未载，可于 Other 一并给。","selectionMode":"single","options":[{"id":"za_x8_opt1","label":"甲：另开重判面"},{"id":"za_x8_opt2","label":"乙：新旧并存并陈（沿 a330273b981c §9 E3）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"档A·X8（G5）"},{"id":"kd_x7","question":"KD·X-7：登录件 §6-5 之点名不成立（708dfac55be9 对 13 枚旧指纹 0 命中；点名 3 件中 1 件不成立；漏载 40 件）——是否更正？","selectionMode":"single","options":[{"id":"kd_x7_opt1","label":"甲：另出修订件更正（0 回改登录件）"},{"id":"kd_x7_opt2","label":"乙：维持原样"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"KD·X-7"},{"id":"wf_u1","question":"五终判·U-1：三态框架指引件（708dfac55be9）之 0 回改处置——维持原字＋新件取代（裁定件主张），或另出 v2 修订指引件正文？","selectionMode":"single","options":[{"id":"wf_u1_opt1","label":"甲：维持原字＋新件取代"},{"id":"wf_u1_opt2","label":"乙：另出 v2 修订正文"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"五终判·U-1"}],"status":"pending","createdAt":1791610872005,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_e022fcbd-3716-4ffd-95bf-559a838b4f3c","toolCallId":"call_00_JRhO7tQQqrGJqfZKWo2O3667"},"title":"轮44 · 草案核准与收口四问"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_dde5c7e4cb782427cde5f2ad","answers":[{"stepId":"u23_approve","selectedOptionIds":["u23_approve_opt1"],"selectedOther":false},{"stepId":"za_x8","selectedOptionIds":["za_x8_opt1"],"selectedOther":false},{"stepId":"kd_x7","selectedOptionIds":["kd_x7_opt1"],"selectedOther":false},{"stepId":"wf_u1","selectedOptionIds":["wf_u1_opt1"],"selectedOther":false}],"submittedAt":1791610906564}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `u23_approve`：`selectedOptionIds` = ["u23_approve_opt1"]；`selectedOther` = false
答 2／4 — `stepId` = `za_x8`：`selectedOptionIds` = ["za_x8_opt1"]；`selectedOther` = false
答 3／4 — `stepId` = `kd_x7`：`selectedOptionIds` = ["kd_x7_opt1"]；`selectedOther` = false
答 4／4 — `stepId` = `wf_u1`：`selectedOptionIds` = ["wf_u1_opt1"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `u23_approve`：`u23_approve_opt1` → 选项字面（逐字）= `甲：按推荐组合核准（两件草案据此生效）`
- 答 2／4 — `za_x8`：`za_x8_opt1` → 选项字面（逐字）= `甲：另开重判面`
- 答 3／4 — `kd_x7`：`kd_x7_opt1` → 选项字面（逐字）= `甲：另出修订件更正（0 回改登录件）`
- 答 4／4 — `wf_u1`：`wf_u1_opt1` → 选项字面（逐字）= `甲：维持原字＋新件取代`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 9 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

## 2 · 对账（**0 漏录 · 0 重复 · 0 掩饰**）

| 序 | `request_id` | 轮 | `created_at`（CST） | `answered_at`（CST） | `status` | 前五批是否已含 |
|---:|---|---|---|---|---|---|
| 1 | `ask_c8d8c049d9c68775ba5f03ee` | 轮39 | 2026-10-10 12:22:47.604 +0800 | 2026-10-10 12:23:52.013 +0800 | `answered` | ⛔ 未含（实测·前五批全文均无此 id） |
| 2 | `ask_6e588d3357c1df300749b686` | 轮40 | 2026-10-10 12:54:15.605 +0800 | 2026-10-10 12:56:15.261 +0800 | `answered` | ⛔ 未含（实测·前五批全文均无此 id） |
| 3 | `ask_38cfeded4238be5321e93cef` | 轮41 | 2026-10-10 13:00:27.136 +0800 | 2026-10-10 13:05:43.679 +0800 | `answered` | ⛔ 未含（实测·前五批全文均无此 id） |
| 4 | `ask_36de432448367350571a9de7` | 轮42 | 2026-10-10 13:12:48.246 +0800 | 2026-10-10 13:13:29.981 +0800 | `answered` | ⛔ 未含（实测·前五批全文均无此 id） |
| 5 | `ask_e5c5a8e874391fc6845971f1` | 轮43 | 2026-10-10 13:23:41.339 +0800 | 2026-10-10 13:25:31.818 +0800 | `answered` | ⛔ 未含（实测·前五批全文均无此 id） |
| 6 | `ask_dde5c7e4cb782427cde5f2ad` | 轮44 | 2026-10-10 13:41:12.005 +0800 | 2026-10-10 13:41:46.564 +0800 | `answered` | ⛔ 未含（实测·前五批全文均无此 id） |

⇒ **6／6 件转录完成、0 失败**；逐字转录之 `steps` 合计 **24** 步、`options` 合计 **66** 项、`answers` 合计 **24** 条。

### 2.1 本批版本号核定（实测）

盘上存在五件 `_questionnaire_cards_intake_register*` 登记件（无 `supplement_5`）；故取**首个未用序号** ＝ **`_supplement_5_`。落前实测：`Test-Path` ＝ **False**；仓内 `*supplement_5*` glob 命中 **0**。

### 2.2 本件之边界（诚实交代）

1. **本件非全表应录全集** —— 系派工指定之 6 张目标卡（轮39～轮44）之逐字转录；⛔ **0 声称已覆盖本轮新建之全部卡**。
2. **本件未转录轮35～轮38** —— 实测该四张卡不在本件应录面（详见 §2.4），本件不超出派工指定范围转录它们。
3. **本件 0 核他件之内部正确性** —— ⛔ 0 复核前五批登记件之内容；仅核其**存在性与 SHA-12**。
4. **题面之实质裁定 0 预判** —— 本件仅照录 PI 之所选；⛔ 0 判读其所选之对错、⛔ 0 预判后续处置。
5. **回指表之边界** —— §1 各卡「答文回指」小表仅为同一行内 `selectedOptionIds` → `options[].label` 之**机械字面对取**，未作任何判读；若与逐字原文有冲突，以**原文**为准。

### 2.3 差异登记（对派工转录清单 · 逐条比对）

本批 24 答逐条比对派工转录清单，结果见回执「24 答逐字核对结果表」：
**字面差异 0**（24／24 相符）。一处**机制提示**（非差异）如下：

- **轮41 第 2 答（`b_close`）**：派工清单记为「B 落档＝另议」，库中實体为 **`selectedOther` = false 且选 `b_close_opt3`（选项字面「丙：另议」）**；即「另议」事实成立，但其**取值通道**为选项而非 Other。余 3 处「另议 / 外派 / 不指定」类答均为 `selectedOther` = true（Other）。

### 2.4 轮35～轮38 落册面存在性核实（本件越出派工范围，仅列口）

实测（全仓搜索五件 `_questionnaire_cards_intake_register*.md`）：轮35～轮38 四张卡均**未出现**于任一登记件。余以作后续落册之导线：

| 轮 | `request_id` | 卡题 | `status` |
|---|---|---|:--:|
| 轮35 | `ask_c235565928c3dbd333a15d10` | 师委审核：prereg 修订件／EXP-05 退录 / EMBEDDING 落柜 / KD 改写授权 | `answered` |
| 轮36 | `ask_90373daee410768058a3e852` | 清卷续项：EXP-05／E1／T-S3-3／runner 修改授权 | `answered` |
| 轮37 | `ask_f20086bee6d76d9d83e49d8d` | KD19 处置：E-3/E-5/E-6／S4 开跑门 | `answered` |
| 轮38 | `ask_8650c331424f2cb3f71931e2` | 裁因复核：T-S3-3／runner 授权 / E-5 / KD 改写授权 | `answered` |

⚠ 本件未转录上表四卡（越出派工指定的 6 张目标卡），仅作落册面缺口登记。

⚠ **活库变动如实登记**：`ask_d43f9ff0f507b8ba55ec72ff`（轮45）在本棒**两次读取之间**由 `pending` 变为 **`answered`** —— 本棒首读（全表 415 行、`answered`=412／`pending`=1／`superseded`=2）时其 `status` 为 `pending`；落册读时点复测已为 `answered`（`answered_at` = 1791611721969 ＝ 2026-10-10 13:55:21.969 +0800，`reply_payload` 已具 4 答）。故落册读时点全表分布为 `answered`=413／`superseded`=2。本件**仅转录指定之 6 张目标卡**，⛔ **0 顺带转录轮45**（超出派工范围）；轮45 之落册留待后续批次。

---

## 3 · 0 回改确认 ＋ 落盘自证

### 3.1 0 回改确认

| 项 | 确认 |
|---|---|
| 既有件写动作 | **0** —— ⛔ 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除任何既有件（**含前五批落册登记件**） |
| 本棒写动作 | **新增 1 件**（本件） |
| 运行时库 | **只读**（`mode=ro`）—— 0 写入、0 修改、0 建表、0 提交 |
| 会话消息面 | **只读**（仅 `messages.jsonl` 检索）—— 0 写入 |
| 本件交付前之自身更正 | **4 类 / 6 处**（如实登记）—— 本件初稿落盘后、交付前，经本棒自查发现并就地更正：① 轮次区间记法误用「｜」，共 5 处（文件头注「窗口口径」、§2.2 第 1 条、§2.2 第 2 条、§2.4 标题、§2.4 正文），一并更正为「～」；② §0 之「复核核对口径」误植一字（回揥），更正为「复核」；③ §2.4 关于轮45 `status` 之记述过时（活库于本棒两读之间变动），依复测值改写；④ 本行更正计数随之同步。**以上均属本棒自身新件、交付前之更正，⛔ 0 触及任何既有件**；逐字转录之库内字面（§1 全部题面与答文）**0 处更动**。 |

### 3.2 落前撞名实测

| 项 | 实测结果 |
|---|---|
| 落前撞名 | `Test-Path 'results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md'` ＝ **False**；仓内 `*supplement_5*` glob 命中 **0** ⇒ ✅ **新名新建 · 0 覆写 · 0 重名** |

### 3.3 输入件指纹（本棒 `SHA256` **当轮实测** · **0 沿用他件登记值**）

| 件 | SHA-12 | 字节 |
|---|---|---:|
| `results/_questionnaire_cards_intake_register_2026_10_09.md` | `d917180db36f` | 442288 |
| `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `193386b9f23c` | 72199 |
| `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `dc43e3cb7610` | 262542 |
| `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | `11681f0ad861` | 67225 |
| `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | `d6ff041a9df9` | 116506 |

### 3.4 边界声明 · 0 编造

- **0 编造 PI 立场**：本件所载六卡之题面与答文**均取自运行时库原件**（程序化逐字转录）；⛔ **0 推测** PI 对任何一项之将来处置。
- **0 冒充他棒**：本件由 **doc-writer** 出件；⛔ 0 顶任何他方名头。
- **0 网络 · 0 skill · 0 LLM · 0 实验**：本棒仅本机只读取证 ＋ 1 件新建。
- **R4**：⛔ 0 读 key、⛔ 0 读 `.env`、⛔ 0 落盘凭据、**key 永不明文**。
- **不编造专有名词／文献号／定理名**：本件**0 引用任何外部定理、文献或标准**。

**本件状态**：✅ **6 卡逐字转录完成 · 0 失败 · 0 判读 · 0 代裁 · 0 回改** ｜ ⛔ 0 网络 · 0 skill · 0 LLM
