# 裁卡原件批量落册（第三批·追补）· questionnaire 原件逐字转录（2026-10-10）

## 文件头注

- **件名**：`results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md`
- **落册日期**：2026-10-10（CST）
- **件系**：第二批登记件 `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` 之**追补落册（第三批）**；上承第一批 `results/_questionnaire_cards_intake_register_2026_10_09.md`（SHA-12 `d917180db36f`）。⛔ 0 编辑／覆写／修改前两批登记件；⛔ 0 重复转录其已收录之卡（对账见 §2）。
- **编制**：**protocol-keeper**（口径与预登记官 · 分支会话 `mvs_b930412a4f984b478c9a6697d4b8a391`｜署名如实 · **0 冒充 PI／parent／verdict-keeper／verifier／worker**）
- **来源**：运行时库 `〔本机用户目录〕/.minimax/v2/sqlite/runtime-state.sqlite`，表 `questionnaire_requests`。本轮以 `sqlite3.connect("file:...?mode=ro", uri=True)` **只读实测**（0 写入、0 修改、0 建表、0 提交）。
- **窗口口径（第二批截止 ＋ 本批起讫）**：
  - **第一批窗口**：`created_at >= 2026-10-08 00:00:00 +0800`（epoch ms `1791388800000`）；实录 34 件。
  - **第二批窗口**：`created_at >= 2026-10-09 17:00:00 +0800`（epoch ms `1791536400000`）；实录 5 件（另 5 件仅列对账行）。
  - **本批窗口**：`created_at >= 2026-10-09 17:00:00 +0800`（沿用第二批口径以覆盖**重叠区对账**）——即本批应录全集＝**本窗口内前两批未含者**。
  - **本件读得时点实测末件**：`ask_54975ff7d6a836cad213377f`（`2026-10-10 00:18:36.640 +0800` 建卡 ／ `00:19:14.834 +0800` 答毕）＝**本件之收录截止**。
  - ⚠ **活库声明**：运行时库为**活库**，本件之读得时点即收录截止时点；**其后再建之卡不属本件应录面**（沿第二批同款「读得时点末件」体例），**0 静默丢弃**——另卡者由后续批次续编。
- **转录纪律**：**逐字、0 省略、0 解释、0 判读**。题面（`request_json.steps` 之 id／header／question／options）与答文（`reply_payload` 全文，含 `selectedOther`／`otherText`）均按库中原文照录；本件**不含**任何分析、结论、裁断或建议。
- **效力声明**：本件**仅转录**。⛔ **0 当「裁录」**；⛔ **0 代替任何既有登记件的裁录效力**。本件不产生、不替代、不撤销任何裁决；一切裁断效力仍以其原登记件／生效件为准。
- **命名合规**：`_主题_日期` 体例；⛔ 0 带 V-阶段前缀（0 `_v3_`／`_v4_`／`_v5_`）。沿第二批之 `_supplement_` 续编体例（第一批 34 件 → 第二批 `_supplement_` 5 件 → 本批 `_supplement_2_`）。
- **编制方式**：`〔本机路径〕/Python314/python.exe` 只读抽取 → 程序化逐字转录（⛔ 0 人工改写任何字面）。

## 0 · 本轮读取基准（provenance）

- 库文件大小（读取时点）：`474656768` bytes
- 库文件 mtime（读取时点，CST）：`2026-10-10 00:21:14.505 +0800`
- 表 `questionnaire_requests` 总行数（全表，本轮实测）：`390`
- 全表 status 分布：`answered`=389；`superseded`=1
- 抽取口径：`SELECT ... FROM questionnaire_requests ORDER BY created_at ASC, request_id ASC`（⛔ 0 LIMIT · 全表扫描）
- 未入册判定口径：**全表 `request_id` 集合 减去 前两批登记件标题节已收录之 39 个 id**（集合差，非窗口近似）
- 时间换算口径：`created_at`／`answered_at`／`submittedAt`／`createdAt` 均为 **INTEGER epoch 毫秒**，本件统一换算为 **CST（UTC+8）** 呈现，原值同时照录。
- 字段长度口径：同时给出**字符数**（Unicode 码位，Python `len`）与**字节数**（UTF-8 编码后 `len`）。
- 值形口径：SQL／JSON 空值一律呈为 `NULL`；布尔值一律呈为 JSON 小写字面 `true`／`false`（沿前两批体例）。
- 计数增量（对账用）：全表行数自第二批读取时点的 `373` 增至本轮实测 `390`（+`17`）。

## 0bis · 「未入册」全集之口径界定（**三段分账 · 0 掩饰**）

派工口径为「`status='answered'` 且不在已入册清单」。按该集合差口径，本轮实测 **全表未入册共 `349` 件**（`answered`）＋ `1` 件（`superseded`）＝ `350` 件。然该 350 件**并非同一性质**，须分账登记：

```text
全表行数（全表实测）                                    : 390
前两批登记件已收录之 request_id（标题节口径）            : 39
未入册全集（集合差，含 status != answered）             : 351
  ├─ 其中 status='answered'                            : 350
  └─ 其中 status='superseded'                          : 1   （ask_05992739fd9e46f8e8acd23d · created_at=2026-09-30 10:38:44.260 +0800）

【第①段】早于第一批窗口下界（created_at < 2026-10-08 00:00 +0800）: 334 件
    → 2026-09-01 11:22:59.763 +0800 ～ 2026-10-02 01:04:00.164 +0800
    → 两批登记件既已明载此类「早于窗口下界……故不属本轮应录面」
    → 本轮处置：逐 id 全量登记（§6）、⛔ 0 逐字转录、0 掩饰、0 静默丢弃
【第②段】第一批窗口内（2026-10-08 00:00 ～ 2026-10-09 17:00 +0800） : 0 件
    → 0 漏录复核通过（第一批实录 34 ＋ 第二批实录 5 ＝ 39 ＝ 该窗口全表实测 39）
【第③段】第二批窗口内前两批未含者（created_at >= 2026-10-09 17:00 +0800）: 17 件
    → **本件 §1 逐字全量收录**（本批应录全集）

  ① + ② + ③ = 334 + 0 + 17 = 351（与集合差 351 一致，0 件外溢、0 件重复计）
```

**⇒ 口径声明（本件立面 · 防误读）**：本件之「追补」对象 ＝ **第③段 17 件**（前两批截止后新建之卡）。第①段 334 件系**历史存量**（2026-09-01 ～ 2026-10-02），两批登记件依其窗口体例既已明载「不属应录面」；本件**逐 id 全量登记其存在与规模**（§6）、**0 逐字转录**，理由与成本如实载于 §6。**此为口径界定，非代裁、0 隐瞒**——是否就第①段另派存量回填，属**另派事项**，登记见 §6.3 候呈。

## 1 · 逐卡转录（本批窗口内前两批未含者，共 17 件，按 `created_at` 升序）

范围口径：本批应录＝本窗口 27 件 − 前两批已含 10 件 ＝ **17 件**（即本节实录全集，无重复计）。

### 01 · `ask_a750c05e5a2a31d0189898b4` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> S4 取法复核＋T1 残余＋KD P-2（四题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_a750c05e5a2a31d0189898b4
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = S4 取法复核＋T1 残余＋KD P-2（四题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_90bd866a-e39c-4f14-9747-19257e3cdfde
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_6U0yJgX9HfpLGVGiX6tO1769
request_json.createdAt (epoch ms) = 1791553590805   → 2026-10-09 21:46:30.805 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791553590805
created_at (CST 换算)          = 2026-10-09 21:46:30.805 +0800
answered_at (epoch ms)         = 1791553712851
answered_at (CST 换算)         = 2026-10-09 21:48:32.851 +0800
reply_payload.submittedAt(epoch ms) = 1791553712851   → 2026-10-09 21:48:32.851 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `r1r4_approve`

- `header`（原文照录）：`取法复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4·取法裁定复核（件 fb1b696de1d6）：推荐组合＝①R1 件名字节序×#idx 升序；②R2 np.random.RandomState(42) 全局单流；③R3 shuffle 后取前 k（按集合认定）；④R4 格序 b→s→o 升序＋floor=0 之格 0 抽取（补钉）。未生效前逐件 26 件集不可开跑。是否核准生效？
```

`options`（逐字原文，共 3 项）：

- `id` = `r1r4_approve_opt1`
  - `label`（逐字原文）：```核准生效——即派逐件集执行棒（S4 解锁）```
  - `description`（逐字原文）：（无此键）
- `id` = `r1r4_approve_opt2`
  - `label`（逐字原文）：```择替代组合——须同时给全六项（排序键／RNG 家族／流式／跨格序／零消耗／平局）```
  - `description`（逐字原文）：（无此键）
- `id` = `r1r4_approve_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `t1_dual`

- `header`（原文照录）：`T1 ② 双口径`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 残余②（双口径分离确认）：N_min 计数已裁 all-pooled；主度量 J 之配对＝same-caption（r1 §2.1 冻结）地位是否维持？（r2 判定件按冻结字面以 same-caption 为主读法、逐格并报 all-pooled。）
```

`options`（逐字原文，共 3 项）：

- `id` = `t1_dual_opt1`
  - `label`（逐字原文）：```维持 same-caption 为冻结主配对（all-pooled 并报）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_dual_opt2`
  - `label`（逐字原文）：```改以 all-pooled 为主配对（same-caption 降为并报）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_dual_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `t1_d2`

- `header`（原文照录）：`T1 ⑥ D-2`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 残余⑥（D-2 留痕追认）：activation（8E59B797AA2D）所载 executor 指纹 37D550D827F9 已过期（实测 38D0CF7FC9BA）；且 activation 晚于起跑落盘。如何处置？
```

`options`（逐字原文，共 3 项）：

- `id` = `t1_d2_opt1`
  - `label`（逐字原文）：```追认——留痕在册（沿 D-2 登记；0 改既有件）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_d2_opt2`
  - `label`（逐字原文）：```另出补正注记（沿革说明件；0 回改）```
  - `description`（逐字原文）：（无此键）
- `id` = `t1_d2_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `kd_p2`

- `header`（原文照录）：`KD P-2`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 归类·候呈 P-2（并置式维持/归一）：存量「不明（KD）」并置写法 8 件 229 处——维持原写法＋归一登记（0 回改；判读按 Known Defect 第三档），抑或转 verdict-keeper 出书写体例指引？
```

`options`（逐字原文，共 3 项）：

- `id` = `kd_p2_opt1`
  - `label`（逐字原文）：```维持原写法＋归一登记（0 回改存量）```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p2_opt2`
  - `label`（逐字原文）：```转 verdict-keeper——出书写体例指引件```
  - `description`（逐字原文）：（无此键）
- `id` = `kd_p2_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_a750c05e5a2a31d0189898b4","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r1r4_approve","question":"S4·取法裁定复核（件 fb1b696de1d6）：推荐组合＝①R1 件名字节序×#idx 升序；②R2 np.random.RandomState(42) 全局单流；③R3 shuffle 后取前 k（按集合认定）；④R4 格序 b→s→o 升序＋floor=0 之格 0 抽取（补钉）。未生效前逐件 26 件集不可开跑。是否核准生效？","selectionMode":"single","options":[{"id":"r1r4_approve_opt1","label":"核准生效——即派逐件集执行棒（S4 解锁）"},{"id":"r1r4_approve_opt2","label":"择替代组合——须同时给全六项（排序键／RNG 家族／流式／跨格序／零消耗／平局）"},{"id":"r1r4_approve_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"取法复核"},{"id":"t1_dual","question":"T1 残余②（双口径分离确认）：N_min 计数已裁 all-pooled；主度量 J 之配对＝same-caption（r1 §2.1 冻结）地位是否维持？（r2 判定件按冻结字面以 same-caption 为主读法、逐格并报 all-pooled。）","selectionMode":"single","options":[{"id":"t1_dual_opt1","label":"维持 same-caption 为冻结主配对（all-pooled 并报）"},{"id":"t1_dual_opt2","label":"改以 all-pooled 为主配对（same-caption 降为并报）"},{"id":"t1_dual_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1 ② 双口径"},{"id":"t1_d2","question":"T1 残余⑥（D-2 留痕追认）：activation（8E59B797AA2D）所载 executor 指纹 37D550D827F9 已过期（实测 38D0CF7FC9BA）；且 activation 晚于起跑落盘。如何处置？","selectionMode":"single","options":[{"id":"t1_d2_opt1","label":"追认——留痕在册（沿 D-2 登记；0 改既有件）"},{"id":"t1_d2_opt2","label":"另出补正注记（沿革说明件；0 回改）"},{"id":"t1_d2_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1 ⑥ D-2"},{"id":"kd_p2","question":"KD 归类·候呈 P-2（并置式维持/归一）：存量「不明（KD）」并置写法 8 件 229 处——维持原写法＋归一登记（0 回改；判读按 Known Defect 第三档），抑或转 verdict-keeper 出书写体例指引？","selectionMode":"single","options":[{"id":"kd_p2_opt1","label":"维持原写法＋归一登记（0 回改存量）"},{"id":"kd_p2_opt2","label":"转 verdict-keeper——出书写体例指引件"},{"id":"kd_p2_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"KD P-2"}],"status":"pending","createdAt":1791553590805,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_90bd866a-e39c-4f14-9747-19257e3cdfde","toolCallId":"call_00_6U0yJgX9HfpLGVGiX6tO1769"},"title":"S4 取法复核＋T1 残余＋KD P-2（四题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_a750c05e5a2a31d0189898b4","answers":[{"stepId":"r1r4_approve","selectedOptionIds":["r1r4_approve_opt1"],"selectedOther":false},{"stepId":"t1_dual","selectedOptionIds":["t1_dual_opt3"],"selectedOther":false},{"stepId":"t1_d2","selectedOptionIds":["t1_d2_opt1"],"selectedOther":false},{"stepId":"kd_p2","selectedOptionIds":["kd_p2_opt2"],"selectedOther":false}],"submittedAt":1791553712851}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r1r4_approve", "selectedOptionIds": ["r1r4_approve_opt1"], "selectedOther": false}
```

- `stepId`：`r1r4_approve`
- `selectedOptionIds`（逐字）：`["r1r4_approve_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r1r4_approve_opt1` → `label`: ```核准生效——即派逐件集执行棒（S4 解锁）```
      → `description`: （无此键）

答 2／4 — 原始对象：

```json
{"stepId": "t1_dual", "selectedOptionIds": ["t1_dual_opt3"], "selectedOther": false}
```

- `stepId`：`t1_dual`
- `selectedOptionIds`（逐字）：`["t1_dual_opt3"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `t1_dual_opt3` → `label`: ```另议```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "t1_d2", "selectedOptionIds": ["t1_d2_opt1"], "selectedOther": false}
```

- `stepId`：`t1_d2`
- `selectedOptionIds`（逐字）：`["t1_d2_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `t1_d2_opt1` → `label`: ```追认——留痕在册（沿 D-2 登记；0 改既有件）```
      → `description`: （无此键）

答 4／4 — 原始对象：

```json
{"stepId": "kd_p2", "selectedOptionIds": ["kd_p2_opt2"], "selectedOther": false}
```

- `stepId`：`kd_p2`
- `selectedOptionIds`（逐字）：`["kd_p2_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `kd_p2_opt2` → `label`: ```转 verdict-keeper——出书写体例指引件```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 2210    字节数(UTF-8) = 3038
reply_payload  字符数 = 424      字节数(UTF-8) = 424
steps 步数 = 4 ／ options 总数 = 12 ／ answers 条数 = 4
question 字符数（逐 step）: r1r4_approve=169; t1_dual=128; t1_d2=115; kd_p2=114
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 02 · `ask_6455cd9f15bf7dc12ae673d9` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮7·补送（T1 放行＋KD P-3＋门禁方向＋RPQ 边界）

**卡级元数据（原文照录）**

```text
request_id                     = ask_6455cd9f15bf7dc12ae673d9
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮7·补送（T1 放行＋KD P-3＋门禁方向＋RPQ 边界）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = e7efc47f-8015-4e5d-84d3-0af7db397316
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_SGFDaTt3pM2MN0dNZq1o1457
request_json.createdAt (epoch ms) = 1791554784554   → 2026-10-09 22:06:24.554 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791554784554
created_at (CST 换算)          = 2026-10-09 22:06:24.554 +0800
answered_at (epoch ms)         = 1791554989370
answered_at (CST 换算)         = 2026-10-09 22:09:49.370 +0800
reply_payload.submittedAt(epoch ms) = 1791554989370   → 2026-10-09 22:09:49.370 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／13 选项，原文照录）**

**题 1／4** — `id` = `r7a_start`

- `header`（原文照录）：`起跑放行包`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 Exp2·起跑放行（两前置）：预登记修订已落（2ff15aeeb5d0）——①D 段先导探针 ≤51 calls 未含于 ≈607 档（须并档或单列）；②跑禁解除（执行面独立前置）。是否放行起跑？
```

`options`（逐字原文，共 3 项）：

- `id` = `r7a_start_opt1`
  - `label`（逐字原文）：```并档＋放行——D 段入 ≈607；跑禁解除、即派执行棒（含 activation 补记）```
  - `description`（逐字原文）：（无此键）
- `id` = `r7a_start_opt2`
  - `label`（逐字原文）：```D 单列＋放行——另计 6/51；跑禁解除、即派```
  - `description`（逐字原文）：（无此键）
- `id` = `r7a_start_opt3`
  - `label`（逐字原文）：```暂不放行——候更多前置闭齐```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `r7b_kdp3`

- `header`（原文照录）：`KD P-3`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 归类·候呈 P-3（族③扩域）：同形异义 KD＝Knowledge Distillation（16 处/10 件，docs/V3X）——判断件提议「另表登记·不入判定域·维持原字面」。是否确认？
```

`options`（逐字原文，共 3 项）：

- `id` = `r7b_kdp3_opt1`
  - `label`（逐字原文）：```确认——族③维持另表登记、不入判定域（维持原字面）```
  - `description`（逐字原文）：（无此键）
- `id` = `r7b_kdp3_opt2`
  - `label`（逐字原文）：```扩至判定域——须另定档位映射（候另议）```
  - `description`（逐字原文）：（无此键）
- `id` = `r7b_kdp3_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `r7c_gate`

- `header`（原文照录）：`门禁方向`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 门禁·修订件方向择定（草案＝50e8b2440346：正案 9 条〔R-1 适用条件逐条举名／R-3 生效三要件／R-8 失效／R-9 回顾…〕；替代案拟-B 分轴豁免〔E-1–E-6 具文〕；拟-C 维持不豁免）。择何方向推进（正式修订件按所选出，仍须你核准＋复核生效）？
```

`options`（逐字原文，共 4 项）：

- `id` = `r7c_gate_opt1`
  - `label`（逐字原文）：```采正案 9 条——出正式修订件（候你核准）```
  - `description`（逐字原文）：（无此键）
- `id` = `r7c_gate_opt2`
  - `label`（逐字原文）：```采拟-B——分轴豁免路线（E-1–E-6 具文）```
  - `description`（逐字原文）：（无此键）
- `id` = `r7c_gate_opt3`
  - `label`（逐字原文）：```采拟-C——维持不豁免（0 加条款）```
  - `description`（逐字原文）：（无此键）
- `id` = `r7c_gate_opt4`
  - `label`（逐字原文）：```暂缓——候 Exp2 结果一并裁```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `r7d_rpq`

- `header`（原文照录）：`RPQ 边界`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair「非画像」·判定面边界（RPQ 候呈 5，件 8c5f83c3c4cf）：现判按题面面（题面正文）；是否须扩至全件面（含 §5/§6 纪律行 73/68 处「PI」）？若扩 ⇒ 该判词须重审。明示边界：
```

`options`（逐字原文，共 3 项）：

- `id` = `r7d_rpq_opt1`
  - `label`（逐字原文）：```题面面为准——现判维持（全件面不适用）```
  - `description`（逐字原文）：（无此键）
- `id` = `r7d_rpq_opt2`
  - `label`（逐字原文）：```扩至全件面——指示重审该判词```
  - `description`（逐字原文）：（无此键）
- `id` = `r7d_rpq_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_6455cd9f15bf7dc12ae673d9","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r7a_start","question":"T1 Exp2·起跑放行（两前置）：预登记修订已落（2ff15aeeb5d0）——①D 段先导探针 ≤51 calls 未含于 ≈607 档（须并档或单列）；②跑禁解除（执行面独立前置）。是否放行起跑？","selectionMode":"single","options":[{"id":"r7a_start_opt1","label":"并档＋放行——D 段入 ≈607；跑禁解除、即派执行棒（含 activation 补记）"},{"id":"r7a_start_opt2","label":"D 单列＋放行——另计 6/51；跑禁解除、即派"},{"id":"r7a_start_opt3","label":"暂不放行——候更多前置闭齐"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"起跑放行包"},{"id":"r7b_kdp3","question":"KD 归类·候呈 P-3（族③扩域）：同形异义 KD＝Knowledge Distillation（16 处/10 件，docs/V3X）——判断件提议「另表登记·不入判定域·维持原字面」。是否确认？","selectionMode":"single","options":[{"id":"r7b_kdp3_opt1","label":"确认——族③维持另表登记、不入判定域（维持原字面）"},{"id":"r7b_kdp3_opt2","label":"扩至判定域——须另定档位映射（候另议）"},{"id":"r7b_kdp3_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"KD P-3"},{"id":"r7c_gate","question":"T1 门禁·修订件方向择定（草案＝50e8b2440346：正案 9 条〔R-1 适用条件逐条举名／R-3 生效三要件／R-8 失效／R-9 回顾…〕；替代案拟-B 分轴豁免〔E-1–E-6 具文〕；拟-C 维持不豁免）。择何方向推进（正式修订件按所选出，仍须你核准＋复核生效）？","selectionMode":"single","options":[{"id":"r7c_gate_opt1","label":"采正案 9 条——出正式修订件（候你核准）"},{"id":"r7c_gate_opt2","label":"采拟-B——分轴豁免路线（E-1–E-6 具文）"},{"id":"r7c_gate_opt3","label":"采拟-C——维持不豁免（0 加条款）"},{"id":"r7c_gate_opt4","label":"暂缓——候 Exp2 结果一并裁"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"门禁方向"},{"id":"r7d_rpq","question":"R_pair「非画像」·判定面边界（RPQ 候呈 5，件 8c5f83c3c4cf）：现判按题面面（题面正文）；是否须扩至全件面（含 §5/§6 纪律行 73/68 处「PI」）？若扩 ⇒ 该判词须重审。明示边界：","selectionMode":"single","options":[{"id":"r7d_rpq_opt1","label":"题面面为准——现判维持（全件面不适用）"},{"id":"r7d_rpq_opt2","label":"扩至全件面——指示重审该判词"},{"id":"r7d_rpq_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"RPQ 边界"}],"status":"pending","createdAt":1791554784554,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"e7efc47f-8015-4e5d-84d3-0af7db397316","toolCallId":"call_00_SGFDaTt3pM2MN0dNZq1o1457"},"title":"轮7·补送（T1 放行＋KD P-3＋门禁方向＋RPQ 边界）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_6455cd9f15bf7dc12ae673d9","answers":[{"stepId":"r7a_start","selectedOptionIds":["r7a_start_opt1"],"selectedOther":false},{"stepId":"r7b_kdp3","selectedOptionIds":["r7b_kdp3_opt1"],"selectedOther":false},{"stepId":"r7c_gate","selectedOptionIds":["r7c_gate_opt1"],"selectedOther":false},{"stepId":"r7d_rpq","selectedOptionIds":["r7d_rpq_opt2"],"selectedOther":false}],"submittedAt":1791554989370}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r7a_start", "selectedOptionIds": ["r7a_start_opt1"], "selectedOther": false}
```

- `stepId`：`r7a_start`
- `selectedOptionIds`（逐字）：`["r7a_start_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r7a_start_opt1` → `label`: ```并档＋放行——D 段入 ≈607；跑禁解除、即派执行棒（含 activation 补记）```
      → `description`: （无此键）

答 2／4 — 原始对象：

```json
{"stepId": "r7b_kdp3", "selectedOptionIds": ["r7b_kdp3_opt1"], "selectedOther": false}
```

- `stepId`：`r7b_kdp3`
- `selectedOptionIds`（逐字）：`["r7b_kdp3_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r7b_kdp3_opt1` → `label`: ```确认——族③维持另表登记、不入判定域（维持原字面）```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "r7c_gate", "selectedOptionIds": ["r7c_gate_opt1"], "selectedOther": false}
```

- `stepId`：`r7c_gate`
- `selectedOptionIds`（逐字）：`["r7c_gate_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r7c_gate_opt1` → `label`: ```采正案 9 条——出正式修订件（候你核准）```
      → `description`: （无此键）

答 4／4 — 原始对象：

```json
{"stepId": "r7d_rpq", "selectedOptionIds": ["r7d_rpq_opt2"], "selectedOther": false}
```

- `stepId`：`r7d_rpq`
- `selectedOptionIds`（逐字）：`["r7d_rpq_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r7d_rpq_opt2` → `label`: ```扩至全件面——指示重审该判词```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 2178    字节数(UTF-8) = 3167
reply_payload  字符数 = 430      字节数(UTF-8) = 430
steps 步数 = 4 ／ options 总数 = 13 ／ answers 条数 = 4
question 字符数（逐 step）: r7a_start=101; r7b_kdp3=100; r7c_gate=140; r7d_rpq=107
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 03 · `ask_e98a16382e277b4918bf9853` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 配对口径复核＋KD VK 三项（补送）

**卡级元数据（原文照录）**

```text
request_id                     = ask_e98a16382e277b4918bf9853
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 配对口径复核＋KD VK 三项（补送）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_task_delivery_115c0217edfd43ac8d21bb4331c629b1
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_e61A6zIVBJQESRUuyNcc0095
request_json.createdAt (epoch ms) = 1791555452496   → 2026-10-09 22:17:32.496 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791555452496
created_at (CST 换算)          = 2026-10-09 22:17:32.496 +0800
answered_at (epoch ms)         = 1791555676231
answered_at (CST 换算)         = 2026-10-09 22:21:16.231 +0800
reply_payload.submittedAt(epoch ms) = 1791555676231   → 2026-10-09 22:21:16.231 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `r8a2_pairing`

- `header`（原文照录）：`配对口径复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 配对口径裁定复核（件 2ded8091114a）：①主配对维持 same-caption（all-pooled 强制并报）；②F-1 采纳复本对齐订正（跨温 0.5335＞同温内 0.5300、方向维持且更强；勘误注记另件承载、0 回改 r2 件）。是否核准生效？
```

`options`（逐字原文，共 3 项）：

- `id` = `r8a2_pairing_opt1`
  - `label`（逐字原文）：```核准——两项生效即锁```
  - `description`（逐字原文）：（无此键）
- `id` = `r8a2_pairing_opt2`
  - `label`（逐字原文）：```仅核准 F-1 订正——主配对另议```
  - `description`（逐字原文）：（无此键）
- `id` = `r8a2_pairing_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `r8b2_vk1`

- `header`（原文照录）：`KD VK-1`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 指引·须你给①（VK-1）：并置式存量 8 件 229 处——是否须逐处改写？（指引主张 0 改写、维持原写法＋归一登记）
```

`options`（逐字原文，共 3 项）：

- `id` = `r8b2_vk1_opt1`
  - `label`（逐字原文）：```维持 0 改写——原写法留存＋归一登记```
  - `description`（逐字原文）：（无此键）
- `id` = `r8b2_vk1_opt2`
  - `label`（逐字原文）：```须逐处改写——另派改写棒（候方案）```
  - `description`（逐字原文）：（无此键）
- `id` = `r8b2_vk1_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `r8c2_vk1b`

- `header`（原文照录）：`KD VK-1b`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 指引·须你给②（VK-1b）：判定第三档是否允许中文档名「不明」独立存在？（指引主张 ⛔0——统一以 KD（不可判）形式）
```

`options`（逐字原文，共 3 项）：

- `id` = `r8c2_vk1b_opt1`
  - `label`（逐字原文）：```同意 ⛔0 独立档名——统一 KD 形式```
  - `description`（逐字原文）：（无此键）
- `id` = `r8c2_vk1b_opt2`
  - `label`（逐字原文）：```允许「不明」作独立档名```
  - `description`（逐字原文）：（无此键）
- `id` = `r8c2_vk1b_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `r8d2_vk3`

- `header`（原文照录）：`KD VK-3`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 指引·须你给③（VK-3）：「不可判」是否升格为判定域正式中文档名？（指引仅作括注、0 主张升格）
```

`options`（逐字原文，共 3 项）：

- `id` = `r8d2_vk3_opt1`
  - `label`（逐字原文）：```不升格——仅作括注（KD 形式保留）```
  - `description`（逐字原文）：（无此键）
- `id` = `r8d2_vk3_opt2`
  - `label`（逐字原文）：```升格——「不可判」列为正式档名（须另定体例）```
  - `description`（逐字原文）：（无此键）
- `id` = `r8d2_vk3_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_e98a16382e277b4918bf9853","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r8a2_pairing","question":"T1 配对口径裁定复核（件 2ded8091114a）：①主配对维持 same-caption（all-pooled 强制并报）；②F-1 采纳复本对齐订正（跨温 0.5335＞同温内 0.5300、方向维持且更强；勘误注记另件承载、0 回改 r2 件）。是否核准生效？","selectionMode":"single","options":[{"id":"r8a2_pairing_opt1","label":"核准——两项生效即锁"},{"id":"r8a2_pairing_opt2","label":"仅核准 F-1 订正——主配对另议"},{"id":"r8a2_pairing_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"配对口径复核"},{"id":"r8b2_vk1","question":"KD 指引·须你给①（VK-1）：并置式存量 8 件 229 处——是否须逐处改写？（指引主张 0 改写、维持原写法＋归一登记）","selectionMode":"single","options":[{"id":"r8b2_vk1_opt1","label":"维持 0 改写——原写法留存＋归一登记"},{"id":"r8b2_vk1_opt2","label":"须逐处改写——另派改写棒（候方案）"},{"id":"r8b2_vk1_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"KD VK-1"},{"id":"r8c2_vk1b","question":"KD 指引·须你给②（VK-1b）：判定第三档是否允许中文档名「不明」独立存在？（指引主张 ⛔0——统一以 KD（不可判）形式）","selectionMode":"single","options":[{"id":"r8c2_vk1b_opt1","label":"同意 ⛔0 独立档名——统一 KD 形式"},{"id":"r8c2_vk1b_opt2","label":"允许「不明」作独立档名"},{"id":"r8c2_vk1b_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"KD VK-1b"},{"id":"r8d2_vk3","question":"KD 指引·须你给③（VK-3）：「不可判」是否升格为判定域正式中文档名？（指引仅作括注、0 主张升格）","selectionMode":"single","options":[{"id":"r8d2_vk3_opt1","label":"不升格——仅作括注（KD 形式保留）"},{"id":"r8d2_vk3_opt2","label":"升格——「不可判」列为正式档名（须另定体例）"},{"id":"r8d2_vk3_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"KD VK-3"}],"status":"pending","createdAt":1791555452496,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_task_delivery_115c0217edfd43ac8d21bb4331c629b1","toolCallId":"call_00_e61A6zIVBJQESRUuyNcc0095"},"title":"配对口径复核＋KD VK 三项（补送）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_e98a16382e277b4918bf9853","answers":[{"stepId":"r8a2_pairing","selectedOptionIds":["r8a2_pairing_opt1"],"selectedOther":false},{"stepId":"r8b2_vk1","selectedOptionIds":["r8b2_vk1_opt2"],"selectedOther":false},{"stepId":"r8c2_vk1b","selectedOptionIds":[],"selectedOther":true,"otherText":"不明即挂账，立即真判"},{"stepId":"r8d2_vk3","selectedOptionIds":[],"selectedOther":true,"otherText":"同语境下KD含义唯一，子代理再判，如依旧不可判则惯例外派委托"}],"submittedAt":1791555676231}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r8a2_pairing", "selectedOptionIds": ["r8a2_pairing_opt1"], "selectedOther": false}
```

- `stepId`：`r8a2_pairing`
- `selectedOptionIds`（逐字）：`["r8a2_pairing_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r8a2_pairing_opt1` → `label`: ```核准——两项生效即锁```
      → `description`: （无此键）

答 2／4 — 原始对象：

```json
{"stepId": "r8b2_vk1", "selectedOptionIds": ["r8b2_vk1_opt2"], "selectedOther": false}
```

- `stepId`：`r8b2_vk1`
- `selectedOptionIds`（逐字）：`["r8b2_vk1_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r8b2_vk1_opt2` → `label`: ```须逐处改写——另派改写棒（候方案）```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "r8c2_vk1b", "selectedOptionIds": [], "selectedOther": true, "otherText": "不明即挂账，立即真判"}
```

- `stepId`：`r8c2_vk1b`
- `selectedOptionIds`（逐字）：`[]`
- `selectedOther`（逐字）：`true`
- `otherText`：

```text
不明即挂账，立即真判
```

答 4／4 — 原始对象：

```json
{"stepId": "r8d2_vk3", "selectedOptionIds": [], "selectedOther": true, "otherText": "同语境下KD含义唯一，子代理再判，如依旧不可判则惯例外派委托"}
```

- `stepId`：`r8d2_vk3`
- `selectedOptionIds`（逐字）：`[]`
- `selectedOther`（逐字）：`true`
- `otherText`：

```text
同语境下KD含义唯一，子代理再判，如依旧不可判则惯例外派委托
```

**关键字段长度（实测）**

```text
request_json   字符数 = 1942    字节数(UTF-8) = 2647
reply_payload  字符数 = 477      字节数(UTF-8) = 553
steps 步数 = 4 ／ options 总数 = 12 ／ answers 条数 = 4
question 字符数（逐 step）: r8a2_pairing=135; r8b2_vk1=64; r8c2_vk1b=64; r8d2_vk3=52
selectedOther=true 条数 = 2 ／ 含 otherText 键条数 = 2 ／ otherText 字符数合计 = 40
```

---

### 04 · `ask_3f9c696f405cd7a384861048` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> R_pair 候呈三题（字面/歧义/勘误）

**卡级元数据（原文照录）**

```text
request_id                     = ask_3f9c696f405cd7a384861048
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = R_pair 候呈三题（字面/歧义/勘误）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_688209f8-290b-41e1-a419-ae2e2535cb31
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_V84UP601R3jC8Lm0KlrN6121
request_json.createdAt (epoch ms) = 1791555882677   → 2026-10-09 22:24:42.677 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791555882677
created_at (CST 换算)          = 2026-10-09 22:24:42.677 +0800
answered_at (epoch ms)         = 1791555919115
answered_at (CST 换算)         = 2026-10-09 22:25:19.115 +0800
reply_payload.submittedAt(epoch ms) = 1791555919115   → 2026-10-09 22:25:19.115 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 3 步／10 选项，原文照录）**

**题 1／3** — `id` = `r9a_rp3b`

- `header`（原文照录）：`RP3b 新字面`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair·候呈①（RP3b C 档新字面）：若采「理由括注随变量同步」口径，则 RP3b 之 C 档须随情境改写（现字面与 a 半相同、未随动——全 24 档中唯一「0 edit-site」者）。如何处置？
```

`options`（逐字原文，共 3 项）：

- `id` = `r9a_rp3b_opt1`
  - `label`（逐字原文）：```维持原字面——记为有意钉死（以形式处置隔离变量）```
  - `description`（逐字原文）：（无此键）
- `id` = `r9a_rp3b_opt2`
  - `label`（逐字原文）：```由你给新字面——于 Other 填（以现场字面为准、原字面留存备核）```
  - `description`（逐字原文）：（无此键）
- `id` = `r9a_rp3b_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／3** — `id` = `r9b_rp2`

- `header`（原文照录）：`RP2 歧义`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair·候呈②（RP2 之 C 跨半翻转歧义）：RP2a/b 之 C 在两半指向相反判定方向（同字母不同向），落地读法（同字母同向 vs 实质方向）须你定；实测暂未触发（你作 C／A）。何时处置？
```

`options`（逐字原文，共 4 项）：

- `id` = `r9b_rp2_opt1`
  - `label`（逐字原文）：```暂缓——候触发再裁（登记在册）```
  - `description`（逐字原文）：（无此键）
- `id` = `r9b_rp2_opt2`
  - `label`（逐字原文）：```现在定——按同字母同向（元动作）读法```
  - `description`（逐字原文）：（无此键）
- `id` = `r9b_rp2_opt3`
  - `label`（逐字原文）：```现在定——按实质方向读法```
  - `description`（逐字原文）：（无此键）
- `id` = `r9b_rp2_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／3** — `id` = `r9c_errata`

- `header`（原文照录）：`区间勘误`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair·候呈④（区间陈述勘误）：`f793c5d9128f` L26／L232 载「0.696／0.482 落在既有三对区间（0.493／0.645／0.677）内」——独立实测两值皆在区间外（且 0.482 属跨档比较）⇒ 该自述句字面不成立（数值本身复算命中、非造假）。是否出勘误件？
```

`options`（逐字原文，共 3 项）：

- `id` = `r9c_errata_opt1`
  - `label`（逐字原文）：```出勘误注记件（另件承载、0 回改原件）```
  - `description`（逐字原文）：（无此键）
- `id` = `r9c_errata_opt2`
  - `label`（逐字原文）：```仅登记不勘误```
  - `description`（逐字原文）：（无此键）
- `id` = `r9c_errata_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_3f9c696f405cd7a384861048","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r9a_rp3b","question":"R_pair·候呈①（RP3b C 档新字面）：若采「理由括注随变量同步」口径，则 RP3b 之 C 档须随情境改写（现字面与 a 半相同、未随动——全 24 档中唯一「0 edit-site」者）。如何处置？","selectionMode":"single","options":[{"id":"r9a_rp3b_opt1","label":"维持原字面——记为有意钉死（以形式处置隔离变量）"},{"id":"r9a_rp3b_opt2","label":"由你给新字面——于 Other 填（以现场字面为准、原字面留存备核）"},{"id":"r9a_rp3b_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"RP3b 新字面"},{"id":"r9b_rp2","question":"R_pair·候呈②（RP2 之 C 跨半翻转歧义）：RP2a/b 之 C 在两半指向相反判定方向（同字母不同向），落地读法（同字母同向 vs 实质方向）须你定；实测暂未触发（你作 C／A）。何时处置？","selectionMode":"single","options":[{"id":"r9b_rp2_opt1","label":"暂缓——候触发再裁（登记在册）"},{"id":"r9b_rp2_opt2","label":"现在定——按同字母同向（元动作）读法"},{"id":"r9b_rp2_opt3","label":"现在定——按实质方向读法"},{"id":"r9b_rp2_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"RP2 歧义"},{"id":"r9c_errata","question":"R_pair·候呈④（区间陈述勘误）：`f793c5d9128f` L26／L232 载「0.696／0.482 落在既有三对区间（0.493／0.645／0.677）内」——独立实测两值皆在区间外（且 0.482 属跨档比较）⇒ 该自述句字面不成立（数值本身复算命中、非造假）。是否出勘误件？","selectionMode":"single","options":[{"id":"r9c_errata_opt1","label":"出勘误注记件（另件承载、0 回改原件）"},{"id":"r9c_errata_opt2","label":"仅登记不勘误"},{"id":"r9c_errata_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"区间勘误"}],"status":"pending","createdAt":1791555882677,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_688209f8-290b-41e1-a419-ae2e2535cb31","toolCallId":"call_00_V84UP601R3jC8Lm0KlrN6121"},"title":"R_pair 候呈三题（字面/歧义/勘误）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_3f9c696f405cd7a384861048","answers":[{"stepId":"r9a_rp3b","selectedOptionIds":["r9a_rp3b_opt3"],"selectedOther":false},{"stepId":"r9b_rp2","selectedOptionIds":["r9b_rp2_opt4"],"selectedOther":false},{"stepId":"r9c_errata","selectedOptionIds":["r9c_errata_opt1"],"selectedOther":false}],"submittedAt":1791555919115}
```

**答文逐字（逐条展开，原文照录）**

答 1／3 — 原始对象：

```json
{"stepId": "r9a_rp3b", "selectedOptionIds": ["r9a_rp3b_opt3"], "selectedOther": false}
```

- `stepId`：`r9a_rp3b`
- `selectedOptionIds`（逐字）：`["r9a_rp3b_opt3"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r9a_rp3b_opt3` → `label`: ```另议```
      → `description`: （无此键）

答 2／3 — 原始对象：

```json
{"stepId": "r9b_rp2", "selectedOptionIds": ["r9b_rp2_opt4"], "selectedOther": false}
```

- `stepId`：`r9b_rp2`
- `selectedOptionIds`（逐字）：`["r9b_rp2_opt4"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r9b_rp2_opt4` → `label`: ```另议```
      → `description`: （无此键）

答 3／3 — 原始对象：

```json
{"stepId": "r9c_errata", "selectedOptionIds": ["r9c_errata_opt1"], "selectedOther": false}
```

- `stepId`：`r9c_errata`
- `selectedOptionIds`（逐字）：`["r9c_errata_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r9c_errata_opt1` → `label`: ```出勘误注记件（另件承载、0 回改原件）```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1723    字节数(UTF-8) = 2452
reply_payload  字符数 = 350      字节数(UTF-8) = 350
steps 步数 = 3 ／ options 总数 = 10 ／ answers 条数 = 3
question 字符数（逐 step）: r9a_rp3b=105; r9b_rp2=101; r9c_errata=147
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 05 · `ask_98891be57dbc7ffaa2cb6935` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 门禁核准＋T1 遗留＋RPQ 口径（四题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_98891be57dbc7ffaa2cb6935
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 门禁核准＋T1 遗留＋RPQ 口径（四题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_78401bc7-73de-441a-a7ff-8077b97c03bd
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_rRlgyOyKvVR13XfDZfNF2327
request_json.createdAt (epoch ms) = 1791556103611   → 2026-10-09 22:28:23.611 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791556103611
created_at (CST 换算)          = 2026-10-09 22:28:23.611 +0800
answered_at (epoch ms)         = 1791556132763
answered_at (CST 换算)         = 2026-10-09 22:28:52.763 +0800
reply_payload.submittedAt(epoch ms) = 1791556132763   → 2026-10-09 22:28:52.763 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `r10a_gate`

- `header`（原文照录）：`门禁正式件核准`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 门禁·正式修订件核准（件 0e0cb002c5de）：9 条定稿（R-1–R-9，逐字照采草案）；R-3 三要件之「PI 明文」步由你认定（题③是否构成显式明文）；R-8① 失效触发（Exp2 温度集 3→5 已备于预登记修订）须你定；K-EXP2-A1 默认不及于（如需及之须另出条款）。如何处置？
```

`options`（逐字原文，共 4 项）：

- `id` = `r10a_gate_opt1`
  - `label`（逐字原文）：```核准生效——并认定 R-8① 触发（温度集 3→5 已备）```
  - `description`（逐字原文）：（无此键）
- `id` = `r10a_gate_opt2`
  - `label`（逐字原文）：```核准生效——但 R-8① 触发候 Exp2 结果再定```
  - `description`（逐字原文）：（无此键）
- `id` = `r10a_gate_opt3`
  - `label`（逐字原文）：```暂缓——须修订若干条（Other 说明）```
  - `description`（逐字原文）：（无此键）
- `id` = `r10a_gate_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `r10b_c5`

- `header`（原文照录）：`T1 C-5`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 r1 遗留·候呈 C-5（锚定哈希失效勘误链）：①L2 verdict 实存于归档区（_non_upload_local_archive，E433A06E7FBF/15,671B）——r1 件「缺失」判断不成立（检索范围限仓内所致）；②L14 verdict 哈希漂移属实（盘上 8EEF73BF9856/19,697B ≠ 锚件所载 764F24A21AC8/19,708B，差 11B）。勘误链如何处理？
```

`options`（逐字原文，共 3 项）：

- `id` = `r10b_c5_opt1`
  - `label`（逐字原文）：```派 EA 出勘误链注记（0 回改；含两处事实更正）```
  - `description`（逐字原文）：（无此键）
- `id` = `r10b_c5_opt2`
  - `label`（逐字原文）：```仅登记在册（并入收口件）```
  - `description`（逐字原文）：（无此键）
- `id` = `r10b_c5_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `r10c_c1`

- `header`（原文照录）：`T1 C-1`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 r1 遗留·候呈 C-1（「Q2 拍板档」指认）：r1 判定件载该候裁项仍未消、须你明示其所指（起跑授权已由卷⑧ Q3 甲独立给出、不依赖该档）。请指认（Other 填）或注销：
```

`options`（逐字原文，共 3 项）：

- `id` = `r10c_c1_opt1`
  - `label`（逐字原文）：```注销该候裁项（无需指认）```
  - `description`（逐字原文）：（无此键）
- `id` = `r10c_c1_opt2`
  - `label`（逐字原文）：```确须指认——于 Other 写明所指```
  - `description`（逐字原文）：（无此键）
- `id` = `r10c_c1_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `r10d_rpq3`

- `header`（原文照录）：`RPQ 三择一`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair·候呈③（「只动 1 变量」准口径三择一，件 8c5f83c3c4cf §6.2）：①语义变量数〔4 对各 1〕⇒成立；②字面 edit-site 数〔3–4 处/对〕⇒不成立；③主干钉死·理由随动〔11/12 槽〕⇒基本成立。择一为准（直接决定 RPQ-6 单一判词）：
```

`options`（逐字原文，共 4 项）：

- `id` = `r10d_rpq3_opt1`
  - `label`（逐字原文）：```择①语义口径——RPQ-6＝成立```
  - `description`（逐字原文）：（无此键）
- `id` = `r10d_rpq3_opt2`
  - `label`（逐字原文）：```择②字面口径——RPQ-6＝不成立```
  - `description`（逐字原文）：（无此键）
- `id` = `r10d_rpq3_opt3`
  - `label`（逐字原文）：```择③主干口径——RPQ-6＝基本成立（RP2-C 例外）```
  - `description`（逐字原文）：（无此键）
- `id` = `r10d_rpq3_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_98891be57dbc7ffaa2cb6935","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r10a_gate","question":"T1 门禁·正式修订件核准（件 0e0cb002c5de）：9 条定稿（R-1–R-9，逐字照采草案）；R-3 三要件之「PI 明文」步由你认定（题③是否构成显式明文）；R-8① 失效触发（Exp2 温度集 3→5 已备于预登记修订）须你定；K-EXP2-A1 默认不及于（如需及之须另出条款）。如何处置？","selectionMode":"single","options":[{"id":"r10a_gate_opt1","label":"核准生效——并认定 R-8① 触发（温度集 3→5 已备）"},{"id":"r10a_gate_opt2","label":"核准生效——但 R-8① 触发候 Exp2 结果再定"},{"id":"r10a_gate_opt3","label":"暂缓——须修订若干条（Other 说明）"},{"id":"r10a_gate_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"门禁正式件核准"},{"id":"r10b_c5","question":"T1 r1 遗留·候呈 C-5（锚定哈希失效勘误链）：①L2 verdict 实存于归档区（_non_upload_local_archive，E433A06E7FBF/15,671B）——r1 件「缺失」判断不成立（检索范围限仓内所致）；②L14 verdict 哈希漂移属实（盘上 8EEF73BF9856/19,697B ≠ 锚件所载 764F24A21AC8/19,708B，差 11B）。勘误链如何处理？","selectionMode":"single","options":[{"id":"r10b_c5_opt1","label":"派 EA 出勘误链注记（0 回改；含两处事实更正）"},{"id":"r10b_c5_opt2","label":"仅登记在册（并入收口件）"},{"id":"r10b_c5_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1 C-5"},{"id":"r10c_c1","question":"T1 r1 遗留·候呈 C-1（「Q2 拍板档」指认）：r1 判定件载该候裁项仍未消、须你明示其所指（起跑授权已由卷⑧ Q3 甲独立给出、不依赖该档）。请指认（Other 填）或注销：","selectionMode":"single","options":[{"id":"r10c_c1_opt1","label":"注销该候裁项（无需指认）"},{"id":"r10c_c1_opt2","label":"确须指认——于 Other 写明所指"},{"id":"r10c_c1_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1 C-1"},{"id":"r10d_rpq3","question":"R_pair·候呈③（「只动 1 变量」准口径三择一，件 8c5f83c3c4cf §6.2）：①语义变量数〔4 对各 1〕⇒成立；②字面 edit-site 数〔3–4 处/对〕⇒不成立；③主干钉死·理由随动〔11/12 槽〕⇒基本成立。择一为准（直接决定 RPQ-6 单一判词）：","selectionMode":"single","options":[{"id":"r10d_rpq3_opt1","label":"择①语义口径——RPQ-6＝成立"},{"id":"r10d_rpq3_opt2","label":"择②字面口径——RPQ-6＝不成立"},{"id":"r10d_rpq3_opt3","label":"择③主干口径——RPQ-6＝基本成立（RP2-C 例外）"},{"id":"r10d_rpq3_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"RPQ 三择一"}],"status":"pending","createdAt":1791556103611,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_78401bc7-73de-441a-a7ff-8077b97c03bd","toolCallId":"call_00_rRlgyOyKvVR13XfDZfNF2327"},"title":"门禁核准＋T1 遗留＋RPQ 口径（四题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_98891be57dbc7ffaa2cb6935","answers":[{"stepId":"r10a_gate","selectedOptionIds":["r10a_gate_opt1"],"selectedOther":false},{"stepId":"r10b_c5","selectedOptionIds":["r10b_c5_opt1"],"selectedOther":false},{"stepId":"r10c_c1","selectedOptionIds":["r10c_c1_opt1"],"selectedOther":false},{"stepId":"r10d_rpq3","selectedOptionIds":["r10d_rpq3_opt4"],"selectedOther":false}],"submittedAt":1791556132763}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r10a_gate", "selectedOptionIds": ["r10a_gate_opt1"], "selectedOther": false}
```

- `stepId`：`r10a_gate`
- `selectedOptionIds`（逐字）：`["r10a_gate_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r10a_gate_opt1` → `label`: ```核准生效——并认定 R-8① 触发（温度集 3→5 已备）```
      → `description`: （无此键）

答 2／4 — 原始对象：

```json
{"stepId": "r10b_c5", "selectedOptionIds": ["r10b_c5_opt1"], "selectedOther": false}
```

- `stepId`：`r10b_c5`
- `selectedOptionIds`（逐字）：`["r10b_c5_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r10b_c5_opt1` → `label`: ```派 EA 出勘误链注记（0 回改；含两处事实更正）```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "r10c_c1", "selectedOptionIds": ["r10c_c1_opt1"], "selectedOther": false}
```

- `stepId`：`r10c_c1`
- `selectedOptionIds`（逐字）：`["r10c_c1_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r10c_c1_opt1` → `label`: ```注销该候裁项（无需指认）```
      → `description`: （无此键）

答 4／4 — 原始对象：

```json
{"stepId": "r10d_rpq3", "selectedOptionIds": ["r10d_rpq3_opt4"], "selectedOther": false}
```

- `stepId`：`r10d_rpq3`
- `selectedOptionIds`（逐字）：`["r10d_rpq3_opt4"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r10d_rpq3_opt4` → `label`: ```另议```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 2330    字节数(UTF-8) = 3328
reply_payload  字符数 = 430      字节数(UTF-8) = 430
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: r10a_gate=153; r10b_c5=207; r10c_c1=92; r10d_rpq3=142
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 06 · `ask_7afd6a8e4721444e9899a761` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> V3-05 决议＋EXP 择认（四题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_7afd6a8e4721444e9899a761
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = V3-05 决议＋EXP 择认（四题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_91797167-b195-48dc-919a-ec2765a21f94
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_VUlLzADuvLKGSdkzB5DR5900
request_json.createdAt (epoch ms) = 1791556521641   → 2026-10-09 22:35:21.641 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791556521641
created_at (CST 换算)          = 2026-10-09 22:35:21.641 +0800
answered_at (epoch ms)         = 1791556644743
answered_at (CST 换算)         = 2026-10-09 22:37:24.743 +0800
reply_payload.submittedAt(epoch ms) = 1791556644743   → 2026-10-09 22:37:24.743 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／15 选项，原文照录）**

**题 1／4** — `id` = `r11a_family`

- `header`（原文照录）：`构造族指定`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·构造族指定（补齐方案件 9f5675633e03 §4）：α＝去镜像-非对称交叉（换域：A 策略空间「选标签」→「选 arm」；解 A–E 全部簇；换域风险最大）／β＝保标签语义·off-diagonal 引入 arm 差（半换域；解 A·C·D·E）／γ＝不指定新构造·走门字面第二出口「判不明」＝KD＋γ（0 解任何簇）／δ＝纯口径裁定（仅 D-2 双口径、只解 1 列）。择定（可多案并跑）：
```

`options`（逐字原文，共 4 项）：

- `id` = `r11a_family_opt1`
  - `label`（逐字原文）：```α——去镜像-非对称交叉（换域·解 A–E 全部；风险最大）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11a_family_opt2`
  - `label`（逐字原文）：```β——保标签语义·off-diagonal arm 差（半换域·解 A·C·D·E）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11a_family_opt3`
  - `label`（逐字原文）：```γ——不修构造·走第二出口判不明＝KD 收口```
  - `description`（逐字原文）：（无此键）
- `id` = `r11a_family_opt4`
  - `label`（逐字原文）：```δ 或组合——于 Other 指定```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `r11b_alpha`

- `header`（原文照录）：`α 门槛条件`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·起跑条件⑥：若采 α（换域）⇒「换域后旧门槛（TH-V3R-1 之 1.3×／2.0×）是否仍适用」须你明确（属口径问题、0 自裁）。如何？
```

`options`（逐字原文，共 4 项）：

- `id` = `r11b_alpha_opt1`
  - `label`（逐字原文）：```旧门槛仍适用```
  - `description`（逐字原文）：（无此键）
- `id` = `r11b_alpha_opt2`
  - `label`（逐字原文）：```须重声明（另定）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11b_alpha_opt3`
  - `label`（逐字原文）：```候 α 设计件后再定```
  - `description`（逐字原文）：（无此键）
- `id` = `r11b_alpha_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `r11c_h`

- `header`（原文照录）：`H 对照口径`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·缺项④·H 对照口径（新发现 N-3）：pa_h1/pa_h0 对照读数走 ECR 口径（锚 1.333）抑或 T_frac60 口径（0.7111）？二量为不同量不可混用；且 ECR 锚注释自谬（(T+R+A) 守恒恒 ≡1）须先修。走何口径？
```

`options`（逐字原文，共 3 项）：

- `id` = `r11c_h_opt1`
  - `label`（逐字原文）：```ECR 口径——须先派 ECR 锚修订件（授权）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11c_h_opt2`
  - `label`（逐字原文）：```T_frac60 口径（0.7111）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11c_h_opt3`
  - `label`（逐字原文）：```另议——派独立判断棒```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `r11d_exp`

- `header`（原文照录）：`EXP 择认`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 梳理 v2·可选项择认（EXP-03＝刀锋口径专项复核／04＝deposon vs Bayesian 倍数读数〔须授权〕／05＝归档区重扫〔零成本〕／06＝K-CF-4 校验位补落／08＝S4 补采题面落册；EXP-01/02/07/09 已在办或已处置）——择认哪些？
```

`options`（逐字原文，共 4 项）：

- `id` = `r11d_exp_opt1`
  - `label`（逐字原文）：```全数（03–06＆08）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11d_exp_opt2`
  - `label`（逐字原文）：```仅零成本项（05·08）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11d_exp_opt3`
  - `label`（逐字原文）：```仅 04（授权倍数读数）```
  - `description`（逐字原文）：（无此键）
- `id` = `r11d_exp_opt4`
  - `label`（逐字原文）：```暂不择认（候后续）```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_7afd6a8e4721444e9899a761","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r11a_family","question":"V3-05·构造族指定（补齐方案件 9f5675633e03 §4）：α＝去镜像-非对称交叉（换域：A 策略空间「选标签」→「选 arm」；解 A–E 全部簇；换域风险最大）／β＝保标签语义·off-diagonal 引入 arm 差（半换域；解 A·C·D·E）／γ＝不指定新构造·走门字面第二出口「判不明」＝KD＋γ（0 解任何簇）／δ＝纯口径裁定（仅 D-2 双口径、只解 1 列）。择定（可多案并跑）：","selectionMode":"single","options":[{"id":"r11a_family_opt1","label":"α——去镜像-非对称交叉（换域·解 A–E 全部；风险最大）"},{"id":"r11a_family_opt2","label":"β——保标签语义·off-diagonal arm 差（半换域·解 A·C·D·E）"},{"id":"r11a_family_opt3","label":"γ——不修构造·走第二出口判不明＝KD 收口"},{"id":"r11a_family_opt4","label":"δ 或组合——于 Other 指定"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"构造族指定"},{"id":"r11b_alpha","question":"V3-05·起跑条件⑥：若采 α（换域）⇒「换域后旧门槛（TH-V3R-1 之 1.3×／2.0×）是否仍适用」须你明确（属口径问题、0 自裁）。如何？","selectionMode":"single","options":[{"id":"r11b_alpha_opt1","label":"旧门槛仍适用"},{"id":"r11b_alpha_opt2","label":"须重声明（另定）"},{"id":"r11b_alpha_opt3","label":"候 α 设计件后再定"},{"id":"r11b_alpha_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"α 门槛条件"},{"id":"r11c_h","question":"V3-05·缺项④·H 对照口径（新发现 N-3）：pa_h1/pa_h0 对照读数走 ECR 口径（锚 1.333）抑或 T_frac60 口径（0.7111）？二量为不同量不可混用；且 ECR 锚注释自谬（(T+R+A) 守恒恒 ≡1）须先修。走何口径？","selectionMode":"single","options":[{"id":"r11c_h_opt1","label":"ECR 口径——须先派 ECR 锚修订件（授权）"},{"id":"r11c_h_opt2","label":"T_frac60 口径（0.7111）"},{"id":"r11c_h_opt3","label":"另议——派独立判断棒"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"H 对照口径"},{"id":"r11d_exp","question":"KD 梳理 v2·可选项择认（EXP-03＝刀锋口径专项复核／04＝deposon vs Bayesian 倍数读数〔须授权〕／05＝归档区重扫〔零成本〕／06＝K-CF-4 校验位补落／08＝S4 补采题面落册；EXP-01/02/07/09 已在办或已处置）——择认哪些？","selectionMode":"single","options":[{"id":"r11d_exp_opt1","label":"全数（03–06＆08）"},{"id":"r11d_exp_opt2","label":"仅零成本项（05·08）"},{"id":"r11d_exp_opt3","label":"仅 04（授权倍数读数）"},{"id":"r11d_exp_opt4","label":"暂不择认（候后续）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"EXP 择认"}],"status":"pending","createdAt":1791556521641,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_91797167-b195-48dc-919a-ec2765a21f94","toolCallId":"call_00_VUlLzADuvLKGSdkzB5DR5900"},"title":"V3-05 决议＋EXP 择认（四题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_7afd6a8e4721444e9899a761","answers":[{"stepId":"r11a_family","selectedOptionIds":[],"selectedOther":true,"otherText":"AB预实验并跑，择优转正"},{"stepId":"r11b_alpha","selectedOptionIds":["r11b_alpha_opt2"],"selectedOther":false},{"stepId":"r11c_h","selectedOptionIds":["r11c_h_opt3"],"selectedOther":false},{"stepId":"r11d_exp","selectedOptionIds":["r11d_exp_opt1"],"selectedOther":false}],"submittedAt":1791556644743}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r11a_family", "selectedOptionIds": [], "selectedOther": true, "otherText": "AB预实验并跑，择优转正"}
```

- `stepId`：`r11a_family`
- `selectedOptionIds`（逐字）：`[]`
- `selectedOther`（逐字）：`true`
- `otherText`：

```text
AB预实验并跑，择优转正
```

答 2／4 — 原始对象：

```json
{"stepId": "r11b_alpha", "selectedOptionIds": ["r11b_alpha_opt2"], "selectedOther": false}
```

- `stepId`：`r11b_alpha`
- `selectedOptionIds`（逐字）：`["r11b_alpha_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r11b_alpha_opt2` → `label`: ```须重声明（另定）```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "r11c_h", "selectedOptionIds": ["r11c_h_opt3"], "selectedOther": false}
```

- `stepId`：`r11c_h`
- `selectedOptionIds`（逐字）：`["r11c_h_opt3"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r11c_h_opt3` → `label`: ```另议——派独立判断棒```
      → `description`: （无此键）

答 4／4 — 原始对象：

```json
{"stepId": "r11d_exp", "selectedOptionIds": ["r11d_exp_opt1"], "selectedOther": false}
```

- `stepId`：`r11d_exp`
- `selectedOptionIds`（逐字）：`["r11d_exp_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r11d_exp_opt1` → `label`: ```全数（03–06＆08）```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 2352    字节数(UTF-8) = 3339
reply_payload  字符数 = 444      字节数(UTF-8) = 464
steps 步数 = 4 ／ options 总数 = 15 ／ answers 条数 = 4
question 字符数（逐 step）: r11a_family=205; r11b_alpha=76; r11c_h=129; r11d_exp=138
selectedOther=true 条数 = 1 ／ 含 otherText 键条数 = 1 ／ otherText 字符数合计 = 12
```

---

### 07 · `ask_524267a93d323e0cf9db5b96` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> RPQ 收尾＋T1 ⑧（三题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_524267a93d323e0cf9db5b96
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = RPQ 收尾＋T1 ⑧（三题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_c98467c0-23d9-47a8-b4c7-f30d668f893a
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_ET_v3LxO4QEHNxv43UJq00t0557
request_json.createdAt (epoch ms) = 1791556923876   → 2026-10-09 22:42:03.876 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791556923876
created_at (CST 换算)          = 2026-10-09 22:42:03.876 +0800
answered_at (epoch ms)         = 1791557023456
answered_at (CST 换算)         = 2026-10-09 22:43:43.456 +0800
reply_payload.submittedAt(epoch ms) = 1791557023456   → 2026-10-09 22:43:43.456 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 3 步／8 选项，原文照录）**

**题 1／3** — `id` = `r12a_rpq`

- `header`（原文照录）：`RPQ 判据口径`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
RPQ 重审·判据径择定（件 D8D5E4D2154F）：全件面 138 处「PI」逐处定性——语义禁令口径下＝合规（0 处行为预测/0 画像）；若采「字面零出现」口径则＝不合规（141 处裸串）但该判据自反（禁令句本身含「PI」）。采何口径？
```

`options`（逐字原文，共 3 项）：

- `id` = `r12a_rpq_opt1`
  - `label`（逐字原文）：```语义禁令口径——判合规（现重审结论维持）```
  - `description`（逐字原文）：（无此键）
- `id` = `r12a_rpq_opt2`
  - `label`（逐字原文）：```字面零出现——判不合规（须先解自反问题）```
  - `description`（逐字原文）：（无此键）
- `id` = `r12a_rpq_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／3** — `id` = `r12b_words`

- `header`（原文照录）：`词表补裸形`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
RPQ 重审·词表补裸形（新查出）：裸形「倾向/偏好/习惯/人格/画像/多半」不在 14 词黑名单亦不在扩面 18 词内（实测题面面命中：A「倾向」×2〔会上一致倾向〕、B「多半」×1〔经济性〕——均非画像）。是否补入词表？
```

`options`（逐字原文，共 3 项）：

- `id` = `r12b_words_opt1`
  - `label`（逐字原文）：```补入（下版词表；登记注）```
  - `description`（逐字原文）：（无此键）
- `id` = `r12b_words_opt2`
  - `label`（逐字原文）：```不补（维持现表）```
  - `description`（逐字原文）：（无此键）
- `id` = `r12b_words_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／3** — `id` = `r12c_t1p2`

- `header`（原文照录）：`T1 ⑧`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1·残余⑧（P-2 重启可能）：聚合维度未废止——维持「不适用 ≠ 永免」登记（未来任何读数面援引「真实面 N≥30」时另裁）？
```

`options`（逐字原文，共 2 项）：

- `id` = `r12c_t1p2_opt1`
  - `label`（逐字原文）：```确认——维持登记```
  - `description`（逐字原文）：（无此键）
- `id` = `r12c_t1p2_opt2`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_524267a93d323e0cf9db5b96","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r12a_rpq","question":"RPQ 重审·判据径择定（件 D8D5E4D2154F）：全件面 138 处「PI」逐处定性——语义禁令口径下＝合规（0 处行为预测/0 画像）；若采「字面零出现」口径则＝不合规（141 处裸串）但该判据自反（禁令句本身含「PI」）。采何口径？","selectionMode":"single","options":[{"id":"r12a_rpq_opt1","label":"语义禁令口径——判合规（现重审结论维持）"},{"id":"r12a_rpq_opt2","label":"字面零出现——判不合规（须先解自反问题）"},{"id":"r12a_rpq_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"RPQ 判据口径"},{"id":"r12b_words","question":"RPQ 重审·词表补裸形（新查出）：裸形「倾向/偏好/习惯/人格/画像/多半」不在 14 词黑名单亦不在扩面 18 词内（实测题面面命中：A「倾向」×2〔会上一致倾向〕、B「多半」×1〔经济性〕——均非画像）。是否补入词表？","selectionMode":"single","options":[{"id":"r12b_words_opt1","label":"补入（下版词表；登记注）"},{"id":"r12b_words_opt2","label":"不补（维持现表）"},{"id":"r12b_words_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"词表补裸形"},{"id":"r12c_t1p2","question":"T1·残余⑧（P-2 重启可能）：聚合维度未废止——维持「不适用 ≠ 永免」登记（未来任何读数面援引「真实面 N≥30」时另裁）？","selectionMode":"single","options":[{"id":"r12c_t1p2_opt1","label":"确认——维持登记"},{"id":"r12c_t1p2_opt2","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1 ⑧"}],"status":"pending","createdAt":1791556923876,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_c98467c0-23d9-47a8-b4c7-f30d668f893a","toolCallId":"call_00_ET_v3LxO4QEHNxv43UJq00t0557"},"title":"RPQ 收尾＋T1 ⑧（三题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_524267a93d323e0cf9db5b96","answers":[{"stepId":"r12a_rpq","selectedOptionIds":["r12a_rpq_opt1"],"selectedOther":false},{"stepId":"r12b_words","selectedOptionIds":["r12b_words_opt3"],"selectedOther":false},{"stepId":"r12c_t1p2","selectedOptionIds":["r12c_t1p2_opt2"],"selectedOther":false}],"submittedAt":1791557023456}
```

**答文逐字（逐条展开，原文照录）**

答 1／3 — 原始对象：

```json
{"stepId": "r12a_rpq", "selectedOptionIds": ["r12a_rpq_opt1"], "selectedOther": false}
```

- `stepId`：`r12a_rpq`
- `selectedOptionIds`（逐字）：`["r12a_rpq_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r12a_rpq_opt1` → `label`: ```语义禁令口径——判合规（现重审结论维持）```
      → `description`: （无此键）

答 2／3 — 原始对象：

```json
{"stepId": "r12b_words", "selectedOptionIds": ["r12b_words_opt3"], "selectedOther": false}
```

- `stepId`：`r12b_words`
- `selectedOptionIds`（逐字）：`["r12b_words_opt3"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r12b_words_opt3` → `label`: ```另议```
      → `description`: （无此键）

答 3／3 — 原始对象：

```json
{"stepId": "r12c_t1p2", "selectedOptionIds": ["r12c_t1p2_opt2"], "selectedOther": false}
```

- `stepId`：`r12c_t1p2`
- `selectedOptionIds`（逐字）：`["r12c_t1p2_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r12c_t1p2_opt2` → `label`: ```另议```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1545    字节数(UTF-8) = 2186
reply_payload  字符数 = 354      字节数(UTF-8) = 354
steps 步数 = 3 ／ options 总数 = 8 ／ answers 条数 = 3
question 字符数（逐 step）: r12a_rpq=122; r12b_words=112; r12c_t1p2=65
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 08 · `ask_3a67d55dc36ba9660d788266` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> R_pair 三项复核（口径/选线/字面）

**卡级元数据（原文照录）**

```text
request_id                     = ask_3a67d55dc36ba9660d788266
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = R_pair 三项复核（口径/选线/字面）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_8b622622-551a-4da1-ae57-9a63f873c23a
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_ET_pomtGzBK2MEyhhJbeJih7148
request_json.createdAt (epoch ms) = 1791557336798   → 2026-10-09 22:48:56.798 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791557336798
created_at (CST 换算)          = 2026-10-09 22:48:56.798 +0800
answered_at (epoch ms)         = 1791557431025
answered_at (CST 换算)         = 2026-10-09 22:50:31.025 +0800
reply_payload.submittedAt(epoch ms) = 1791557431025   → 2026-10-09 22:50:31.025 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 3 步／9 选项，原文照录）**

**题 1／3** — `id` = `r13a_cal3`

- `header`（原文照录）：`口径③ 入册`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair·口径③入册复核（判件 5FAA16446171）：RPQ-6 单判词＝成立（口径③「主干钉死·理由随动」）·附 1 具名例外（RP2-C）——核准入册？
```

`options`（逐字原文，共 3 项）：

- `id` = `r13a_cal3_opt1`
  - `label`（逐字原文）：```核准入册（生效即锁）```
  - `description`（逐字原文）：（无此键）
- `id` = `r13a_cal3_opt2`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）
- `id` = `r13a_cal3_opt3`
  - `label`（逐字原文）：```暂缓```
  - `description`（逐字原文）：（无此键）

**题 2／3** — `id` = `r13b_dir`

- `header`（原文照录）：`判断②选线`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair·判断②选线复核（判件 5FAA16446171）：RP2-C 跨半翻转之落地判据——采「实质判定方向」为主线（弃纯元动作读法；附收窄条款）？
```

`options`（逐字原文，共 3 项）：

- `id` = `r13b_dir_opt1`
  - `label`（逐字原文）：```核准——实质判定方向为主线（字段层按此映射）```
  - `description`（逐字原文）：（无此键）
- `id` = `r13b_dir_opt2`
  - `label`（逐字原文）：```改采同字母同向（元动作）```
  - `description`（逐字原文）：（无此键）
- `id` = `r13b_dir_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／3** — `id` = `r13c_rp3b`

- `header`（原文照录）：`RP3b-C 处置`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
R_pair·RP3b-C 处置（判件 5FAA16446171）：采「有意钉死·实质自洽」——不改字面，补例外登记（口径面）；如你判改写则给新字面（0 代拟）。如何处置？
```

`options`（逐字原文，共 3 项）：

- `id` = `r13c_rp3b_opt1`
  - `label`（逐字原文）：```核准——不改字面＋例外登记（0 改盘）```
  - `description`（逐字原文）：（无此键）
- `id` = `r13c_rp3b_opt2`
  - `label`（逐字原文）：```判改写——于 Other 给新字面```
  - `description`（逐字原文）：（无此键）
- `id` = `r13c_rp3b_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_3a67d55dc36ba9660d788266","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r13a_cal3","question":"R_pair·口径③入册复核（判件 5FAA16446171）：RPQ-6 单判词＝成立（口径③「主干钉死·理由随动」）·附 1 具名例外（RP2-C）——核准入册？","selectionMode":"single","options":[{"id":"r13a_cal3_opt1","label":"核准入册（生效即锁）"},{"id":"r13a_cal3_opt2","label":"另议"},{"id":"r13a_cal3_opt3","label":"暂缓"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"口径③ 入册"},{"id":"r13b_dir","question":"R_pair·判断②选线复核（判件 5FAA16446171）：RP2-C 跨半翻转之落地判据——采「实质判定方向」为主线（弃纯元动作读法；附收窄条款）？","selectionMode":"single","options":[{"id":"r13b_dir_opt1","label":"核准——实质判定方向为主线（字段层按此映射）"},{"id":"r13b_dir_opt2","label":"改采同字母同向（元动作）"},{"id":"r13b_dir_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"判断②选线"},{"id":"r13c_rp3b","question":"R_pair·RP3b-C 处置（判件 5FAA16446171）：采「有意钉死·实质自洽」——不改字面，补例外登记（口径面）；如你判改写则给新字面（0 代拟）。如何处置？","selectionMode":"single","options":[{"id":"r13c_rp3b_opt1","label":"核准——不改字面＋例外登记（0 改盘）"},{"id":"r13c_rp3b_opt2","label":"判改写——于 Other 给新字面"},{"id":"r13c_rp3b_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"RP3b-C 处置"}],"status":"pending","createdAt":1791557336798,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_8b622622-551a-4da1-ae57-9a63f873c23a","toolCallId":"call_00_ET_pomtGzBK2MEyhhJbeJih7148"},"title":"R_pair 三项复核（口径/选线/字面）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_3a67d55dc36ba9660d788266","answers":[{"stepId":"r13a_cal3","selectedOptionIds":["r13a_cal3_opt1"],"selectedOther":false},{"stepId":"r13b_dir","selectedOptionIds":["r13b_dir_opt1"],"selectedOther":false},{"stepId":"r13c_rp3b","selectedOptionIds":["r13c_rp3b_opt1"],"selectedOther":false}],"submittedAt":1791557431025}
```

**答文逐字（逐条展开，原文照录）**

答 1／3 — 原始对象：

```json
{"stepId": "r13a_cal3", "selectedOptionIds": ["r13a_cal3_opt1"], "selectedOther": false}
```

- `stepId`：`r13a_cal3`
- `selectedOptionIds`（逐字）：`["r13a_cal3_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r13a_cal3_opt1` → `label`: ```核准入册（生效即锁）```
      → `description`: （无此键）

答 2／3 — 原始对象：

```json
{"stepId": "r13b_dir", "selectedOptionIds": ["r13b_dir_opt1"], "selectedOther": false}
```

- `stepId`：`r13b_dir`
- `selectedOptionIds`（逐字）：`["r13b_dir_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r13b_dir_opt1` → `label`: ```核准——实质判定方向为主线（字段层按此映射）```
      → `description`: （无此键）

答 3／3 — 原始对象：

```json
{"stepId": "r13c_rp3b", "selectedOptionIds": ["r13c_rp3b_opt1"], "selectedOther": false}
```

- `stepId`：`r13c_rp3b`
- `selectedOptionIds`（逐字）：`["r13c_rp3b_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r13c_rp3b_opt1` → `label`: ```核准——不改字面＋例外登记（0 改盘）```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1546    字节数(UTF-8) = 2066
reply_payload  字符数 = 352      字节数(UTF-8) = 352
steps 步数 = 3 ／ options 总数 = 9 ／ answers 条数 = 3
question 字符数（逐 step）: r13a_cal3=83; r13b_dir=77; r13c_rp3b=86
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 09 · `ask_f67e504b3fb68eb81c173270` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> S4 候呈＋VK 待核（三题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_f67e504b3fb68eb81c173270
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = S4 候呈＋VK 待核（三题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_4eb4a9a0-ca44-41a1-bf4d-f3aad28c9237
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_bz4YNMGYPJYoOSmjl1Nj9016
request_json.createdAt (epoch ms) = 1791557623244   → 2026-10-09 22:53:43.244 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791557623244
created_at (CST 换算)          = 2026-10-09 22:53:43.244 +0800
answered_at (epoch ms)         = 1791557712887
answered_at (CST 换算)         = 2026-10-09 22:55:12.887 +0800
reply_payload.submittedAt(epoch ms) = 1791557712887   → 2026-10-09 22:55:12.887 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 3 步／9 选项，原文照录）**

**题 1／3** — `id` = `r14a_leg`

- `header`（原文照录）：`分层含纠正`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4·候呈1（重判件 9cde399502ba）：「分层含纠正」腿于本 substrate 结构性不可达——11 个 b=1 占格 n 全 ≤2 ⇒  floor(0.30·n) ≡ 0 ⇒ 该腿任何取法下恒 0 达成（取法不敏感）。是否另立替代判据／扩域／改分层维度？
```

`options`（逐字原文，共 3 项）：

- `id` = `r14a_leg_opt1`
  - `label`（逐字原文）：```不另立——维持现状登记（两线 FAIL 维持）```
  - `description`（逐字原文）：（无此键）
- `id` = `r14a_leg_opt2`
  - `label`（逐字原文）：```另立替代判据——派设计棒出案```
  - `description`（逐字原文）：（无此键）
- `id` = `r14a_leg_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／3** — `id` = `r14b_h3`

- `header`（原文照录）：`VK·h₃`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
VK 待核·h₃ 基线钉死案复核：h₃＝0.1326086957 已钉于 585714f9660c 主读 bootstrap_ci（四读 0 混算）；因你择绝对固定常数形 ⇒ h₃ 仅作 provenance、不参与门之判据比较。是否核准登记？
```

`options`（逐字原文，共 3 项）：

- `id` = `r14b_h3_opt1`
  - `label`（逐字原文）：```核准——h₃ 仅作 provenance 登记```
  - `description`（逐字原文）：（无此键）
- `id` = `r14b_h3_opt2`
  - `label`（逐字原文）：```须重钉（另议）```
  - `description`（逐字原文）：（无此键）
- `id` = `r14b_h3_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／3** — `id` = `r14c_id`

- `header`（原文照录）：`VK·ID 系属`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
VK 待核·bootstrap 口径 ID 系属（两读未决）：读法甲 TH-v2-7／v3-16／v3-17 vs 读法乙——择定何读（C-1 细目之 ID 引用面据此固化）？
```

`options`（逐字原文，共 3 项）：

- `id` = `r14c_id_opt1`
  - `label`（逐字原文）：```读法乙——TH-v2-8／v3-17（bootstrap 组）```
  - `description`（逐字原文）：（无此键）
- `id` = `r14c_id_opt2`
  - `label`（逐字原文）：```读法甲——TH-v2-7／v3-16／v3-17```
  - `description`（逐字原文）：（无此键）
- `id` = `r14c_id_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_f67e504b3fb68eb81c173270","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r14a_leg","question":"S4·候呈1（重判件 9cde399502ba）：「分层含纠正」腿于本 substrate 结构性不可达——11 个 b=1 占格 n 全 ≤2 ⇒  floor(0.30·n) ≡ 0 ⇒ 该腿任何取法下恒 0 达成（取法不敏感）。是否另立替代判据／扩域／改分层维度？","selectionMode":"single","options":[{"id":"r14a_leg_opt1","label":"不另立——维持现状登记（两线 FAIL 维持）"},{"id":"r14a_leg_opt2","label":"另立替代判据——派设计棒出案"},{"id":"r14a_leg_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"分层含纠正"},{"id":"r14b_h3","question":"VK 待核·h₃ 基线钉死案复核：h₃＝0.1326086957 已钉于 585714f9660c 主读 bootstrap_ci（四读 0 混算）；因你择绝对固定常数形 ⇒ h₃ 仅作 provenance、不参与门之判据比较。是否核准登记？","selectionMode":"single","options":[{"id":"r14b_h3_opt1","label":"核准——h₃ 仅作 provenance 登记"},{"id":"r14b_h3_opt2","label":"须重钉（另议）"},{"id":"r14b_h3_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"VK·h₃"},{"id":"r14c_id","question":"VK 待核·bootstrap 口径 ID 系属（两读未决）：读法甲 TH-v2-7／v3-16／v3-17 vs 读法乙——择定何读（C-1 细目之 ID 引用面据此固化）？","selectionMode":"single","options":[{"id":"r14c_id_opt1","label":"读法乙——TH-v2-8／v3-17（bootstrap 组）"},{"id":"r14c_id_opt2","label":"读法甲——TH-v2-7／v3-16／v3-17"},{"id":"r14c_id_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"VK·ID 系属"}],"status":"pending","createdAt":1791557623244,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_4eb4a9a0-ca44-41a1-bf4d-f3aad28c9237","toolCallId":"call_00_bz4YNMGYPJYoOSmjl1Nj9016"},"title":"S4 候呈＋VK 待核（三题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_f67e504b3fb68eb81c173270","answers":[{"stepId":"r14a_leg","selectedOptionIds":["r14a_leg_opt2"],"selectedOther":false},{"stepId":"r14b_h3","selectedOptionIds":["r14b_h3_opt3"],"selectedOther":false},{"stepId":"r14c_id","selectedOptionIds":["r14c_id_opt3"],"selectedOther":false}],"submittedAt":1791557712887}
```

**答文逐字（逐条展开，原文照录）**

答 1／3 — 原始对象：

```json
{"stepId": "r14a_leg", "selectedOptionIds": ["r14a_leg_opt2"], "selectedOther": false}
```

- `stepId`：`r14a_leg`
- `selectedOptionIds`（逐字）：`["r14a_leg_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r14a_leg_opt2` → `label`: ```另立替代判据——派设计棒出案```
      → `description`: （无此键）

答 2／3 — 原始对象：

```json
{"stepId": "r14b_h3", "selectedOptionIds": ["r14b_h3_opt3"], "selectedOther": false}
```

- `stepId`：`r14b_h3`
- `selectedOptionIds`（逐字）：`["r14b_h3_opt3"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r14b_h3_opt3` → `label`: ```另议```
      → `description`: （无此键）

答 3／3 — 原始对象：

```json
{"stepId": "r14c_id", "selectedOptionIds": ["r14c_id_opt3"], "selectedOther": false}
```

- `stepId`：`r14c_id`
- `selectedOptionIds`（逐字）：`["r14c_id_opt3"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r14c_id_opt3` → `label`: ```另议```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1658    字节数(UTF-8) = 2170
reply_payload  字符数 = 344      字节数(UTF-8) = 344
steps 步数 = 3 ／ options 总数 = 9 ／ answers 条数 = 3
question 字符数（逐 step）: r14a_leg=135; r14b_h3=122; r14c_id=88
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 10 · `ask_efa1af545065d7de7f9094c1` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> S4 五线两项＋V3-05 H 两项（四题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_efa1af545065d7de7f9094c1
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = S4 五线两项＋V3-05 H 两项（四题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_f6db5787-72ad-4c55-bda0-d21c2de04b22
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_ET_TtioayqvYTVwKzamltZ30203
request_json.createdAt (epoch ms) = 1791558125235   → 2026-10-09 23:02:05.235 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791558125235
created_at (CST 换算)          = 2026-10-09 23:02:05.235 +0800
answered_at (epoch ms)         = 1791558176072
answered_at (CST 换算)         = 2026-10-09 23:02:56.072 +0800
reply_payload.submittedAt(epoch ms) = 1791558176072   → 2026-10-09 23:02:56.072 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `r15a_bc`

- `header`（原文照录）：`B/C 构造择`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 五线·B/C 构造①②之择（读数件 73550514152d）：①自身域 resample（该件主推；B L=0.23810／C U=1.0）vs ②全体 held-out resample（B L=0.22727／C U=1.0）——属 estimand/口径面（≠阈值调整）。择一为 B/C 之 K-2 读数口径：
```

`options`（逐字原文，共 4 项）：

- `id` = `r15a_bc_opt1`
  - `label`（逐字原文）：```构造①（自身域 resample·主推）```
  - `description`（逐字原文）：（无此键）
- `id` = `r15a_bc_opt2`
  - `label`（逐字原文）：```构造②（全体 held-out resample）```
  - `description`（逐字原文）：（无此键）
- `id` = `r15a_bc_opt3`
  - `label`（逐字原文）：```两读并陈候判```
  - `description`（逐字原文）：（无此键）
- `id` = `r15a_bc_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `r15b_aper`

- `header`（原文照录）：`A′ 范围面`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 五线·A′ 之 CI 是否入 C-1 判读面（estimand／范围面；读数件 §3.2/§5-4，沿 bee0f1f0bdb2 §8 候呈 1/2）：
```

`options`（逐字原文，共 3 项）：

- `id` = `r15b_aper_opt1`
  - `label`（逐字原文）：```入判读面```
  - `description`（逐字原文）：（无此键）
- `id` = `r15b_aper_opt2`
  - `label`（逐字原文）：```不入——仅登记```
  - `description`（逐字原文）：（无此键）
- `id` = `r15b_aper_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `r15c_h`

- `header`（原文照录）：`H 口径复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·H 对照口径判断复核（件 1c2b5f40e15d）：两候选皆不可直接采用（ECR 锚自指失效已实证；T 口径无对照基线）——处置：
```

`options`（逐字原文，共 4 项）：

- `id` = `r15c_h_opt1`
  - `label`（逐字原文）：```采双轨并报设计（E‖T）＋另定主次```
  - `description`（逐字原文）：（无此键）
- `id` = `r15c_h_opt2`
  - `label`（逐字原文）：```指定单一口径 E（配套 doc-writer 修锚）```
  - `description`（逐字原文）：（无此键）
- `id` = `r15c_h_opt3`
  - `label`（逐字原文）：```指定单一口径 T（配套正命名）```
  - `description`（逐字原文）：（无此键）
- `id` = `r15c_h_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `r15d_bayes`

- `header`（原文照录）：`Bayesian 基线`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·缺项④·Bayesian 对照基线：pa_h1/h0 判「deposon vs Bayesian 倍数」而 E/T 皆不含 Bayesian 对家 ⇒ 对照基线须一并定（判件 O-4）：
```

`options`（逐字原文，共 3 项）：

- `id` = `r15d_bayes_opt1`
  - `label`（逐字原文）：```另派设计棒出基线方案```
  - `description`（逐字原文）：（无此键）
- `id` = `r15d_bayes_opt2`
  - `label`（逐字原文）：```指定现有件为基线（Other 指明）```
  - `description`（逐字原文）：（无此键）
- `id` = `r15d_bayes_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_efa1af545065d7de7f9094c1","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r15a_bc","question":"S4 五线·B/C 构造①②之择（读数件 73550514152d）：①自身域 resample（该件主推；B L=0.23810／C U=1.0）vs ②全体 held-out resample（B L=0.22727／C U=1.0）——属 estimand/口径面（≠阈值调整）。择一为 B/C 之 K-2 读数口径：","selectionMode":"single","options":[{"id":"r15a_bc_opt1","label":"构造①（自身域 resample·主推）"},{"id":"r15a_bc_opt2","label":"构造②（全体 held-out resample）"},{"id":"r15a_bc_opt3","label":"两读并陈候判"},{"id":"r15a_bc_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"B/C 构造择"},{"id":"r15b_aper","question":"S4 五线·A′ 之 CI 是否入 C-1 判读面（estimand／范围面；读数件 §3.2/§5-4，沿 bee0f1f0bdb2 §8 候呈 1/2）：","selectionMode":"single","options":[{"id":"r15b_aper_opt1","label":"入判读面"},{"id":"r15b_aper_opt2","label":"不入——仅登记"},{"id":"r15b_aper_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"A′ 范围面"},{"id":"r15c_h","question":"V3-05·H 对照口径判断复核（件 1c2b5f40e15d）：两候选皆不可直接采用（ECR 锚自指失效已实证；T 口径无对照基线）——处置：","selectionMode":"single","options":[{"id":"r15c_h_opt1","label":"采双轨并报设计（E‖T）＋另定主次"},{"id":"r15c_h_opt2","label":"指定单一口径 E（配套 doc-writer 修锚）"},{"id":"r15c_h_opt3","label":"指定单一口径 T（配套正命名）"},{"id":"r15c_h_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"H 口径复核"},{"id":"r15d_bayes","question":"V3-05·缺项④·Bayesian 对照基线：pa_h1/h0 判「deposon vs Bayesian 倍数」而 E/T 皆不含 Bayesian 对家 ⇒ 对照基线须一并定（判件 O-4）：","selectionMode":"single","options":[{"id":"r15d_bayes_opt1","label":"另派设计棒出基线方案"},{"id":"r15d_bayes_opt2","label":"指定现有件为基线（Other 指明）"},{"id":"r15d_bayes_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"Bayesian 基线"}],"status":"pending","createdAt":1791558125235,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_f6db5787-72ad-4c55-bda0-d21c2de04b22","toolCallId":"call_00_ET_TtioayqvYTVwKzamltZ30203"},"title":"S4 五线两项＋V3-05 H 两项（四题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_efa1af545065d7de7f9094c1","answers":[{"stepId":"r15a_bc","selectedOptionIds":["r15a_bc_opt4"],"selectedOther":false},{"stepId":"r15b_aper","selectedOptionIds":["r15b_aper_opt1"],"selectedOther":false},{"stepId":"r15c_h","selectedOptionIds":["r15c_h_opt4"],"selectedOther":false},{"stepId":"r15d_bayes","selectedOptionIds":["r15d_bayes_opt1"],"selectedOther":false}],"submittedAt":1791558176072}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r15a_bc", "selectedOptionIds": ["r15a_bc_opt4"], "selectedOther": false}
```

- `stepId`：`r15a_bc`
- `selectedOptionIds`（逐字）：`["r15a_bc_opt4"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r15a_bc_opt4` → `label`: ```另议```
      → `description`: （无此键）

答 2／4 — 原始对象：

```json
{"stepId": "r15b_aper", "selectedOptionIds": ["r15b_aper_opt1"], "selectedOther": false}
```

- `stepId`：`r15b_aper`
- `selectedOptionIds`（逐字）：`["r15b_aper_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r15b_aper_opt1` → `label`: ```入判读面```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "r15c_h", "selectedOptionIds": ["r15c_h_opt4"], "selectedOther": false}
```

- `stepId`：`r15c_h`
- `selectedOptionIds`（逐字）：`["r15c_h_opt4"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r15c_h_opt4` → `label`: ```另议```
      → `description`: （无此键）

答 4／4 — 原始对象：

```json
{"stepId": "r15d_bayes", "selectedOptionIds": ["r15d_bayes_opt1"], "selectedOther": false}
```

- `stepId`：`r15d_bayes`
- `selectedOptionIds`（逐字）：`["r15d_bayes_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r15d_bayes_opt1` → `label`: ```另派设计棒出基线方案```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 2096    字节数(UTF-8) = 2677
reply_payload  字符数 = 430      字节数(UTF-8) = 430
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: r15a_bc=162; r15b_aper=79; r15c_h=72; r15d_bayes=99
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 11 · `ask_13e341cca46a973ec61c9f0f` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> V3-05 AB 处置＋Q-3 勘误＋S4 149 面（三题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_13e341cca46a973ec61c9f0f
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = V3-05 AB 处置＋Q-3 勘误＋S4 149 面（三题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_task_delivery_c7a8b75f2f2e427b96475906b2e5fa75
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_Yxase98r4WOqxQT3yhVQ6285
request_json.createdAt (epoch ms) = 1791558668698   → 2026-10-09 23:11:08.698 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791558668698
created_at (CST 换算)          = 2026-10-09 23:11:08.698 +0800
answered_at (epoch ms)         = 1791558714974
answered_at (CST 换算)         = 2026-10-09 23:11:54.974 +0800
reply_payload.submittedAt(epoch ms) = 1791558714974   → 2026-10-09 23:11:54.974 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 3 步／9 选项，原文照录）**

**题 1／3** — `id` = `r16a_ab`

- `header`（原文照录）：`AB 结果处置`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·AB 预实验结果处置（对比件 bdd2a1d7e6c5）：α K-RO-0-1 13/20、β 16/20——两案皆不过全门；β 多解簇 C（n_distinct 5）、换域风险低 ⇒ 择优建议 β（相对更优；5 条反方同权并陈）。如何处置？
```

`options`（逐字原文，共 4 项）：

- `id` = `r16a_ab_opt1`
  - `label`（逐字原文）：```择优 β 转正——派正式跑＋verifier＋判定链```
  - `description`（逐字原文）：（无此键）
- `id` = `r16a_ab_opt2`
  - `label`（逐字原文）：```γ——不修构造、判不明＝KD＋γ 收口```
  - `description`（逐字原文）：（无此键）
- `id` = `r16a_ab_opt3`
  - `label`（逐字原文）：```δ——纯口径裁定（仅 D-2 双口径）```
  - `description`（逐字原文）：（无此键）
- `id` = `r16a_ab_opt4`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／3** — `id` = `r16b_q3`

- `header`（原文照录）：`Q-3 勘误路由`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·AB 棒新发现·Q-3 转置面（件 7761f2c339e6 L282）：镜像矩阵下为 no-op（0/88、0 翻案）；非对称构造下逐格不等（α 48/88・β 80/88）⇒ 换域后静默出错。修正/勘误如何路由？
```

`options`（逐字原文，共 3 项）：

- `id` = `r16b_q3_opt1`
  - `label`（逐字原文）：```派勘误注记件（doc-writer 出；0 回改原件）```
  - `description`（逐字原文）：（无此键）
- `id` = `r16b_q3_opt2`
  - `label`（逐字原文）：```随转正链一并处置（先修再跑）```
  - `description`（逐字原文）：（无此键）
- `id` = `r16b_q3_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／3** — `id` = `r16c_149`

- `header`（原文照录）：`S4·149 面`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4·149 分母面 FAIL 指向（扩样前历史面）并陈未闭（-1/-2 重判件候呈 7）——处置：
```

`options`（逐字原文，共 2 项）：

- `id` = `r16c_149_opt1`
  - `label`（逐字原文）：```维持并陈登记（现状）```
  - `description`（逐字原文）：（无此键）
- `id` = `r16c_149_opt2`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_13e341cca46a973ec61c9f0f","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r16a_ab","question":"V3-05·AB 预实验结果处置（对比件 bdd2a1d7e6c5）：α K-RO-0-1 13/20、β 16/20——两案皆不过全门；β 多解簇 C（n_distinct 5）、换域风险低 ⇒ 择优建议 β（相对更优；5 条反方同权并陈）。如何处置？","selectionMode":"single","options":[{"id":"r16a_ab_opt1","label":"择优 β 转正——派正式跑＋verifier＋判定链"},{"id":"r16a_ab_opt2","label":"γ——不修构造、判不明＝KD＋γ 收口"},{"id":"r16a_ab_opt3","label":"δ——纯口径裁定（仅 D-2 双口径）"},{"id":"r16a_ab_opt4","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"AB 结果处置"},{"id":"r16b_q3","question":"V3-05·AB 棒新发现·Q-3 转置面（件 7761f2c339e6 L282）：镜像矩阵下为 no-op（0/88、0 翻案）；非对称构造下逐格不等（α 48/88・β 80/88）⇒ 换域后静默出错。修正/勘误如何路由？","selectionMode":"single","options":[{"id":"r16b_q3_opt1","label":"派勘误注记件（doc-writer 出；0 回改原件）"},{"id":"r16b_q3_opt2","label":"随转正链一并处置（先修再跑）"},{"id":"r16b_q3_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"Q-3 勘误路由"},{"id":"r16c_149","question":"S4·149 分母面 FAIL 指向（扩样前历史面）并陈未闭（-1/-2 重判件候呈 7）——处置：","selectionMode":"single","options":[{"id":"r16c_149_opt1","label":"维持并陈登记（现状）"},{"id":"r16c_149_opt2","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"S4·149 面"}],"status":"pending","createdAt":1791558668698,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_task_delivery_c7a8b75f2f2e427b96475906b2e5fa75","toolCallId":"call_00_Yxase98r4WOqxQT3yhVQ6285"},"title":"V3-05 AB 处置＋Q-3 勘误＋S4 149 面（三题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_13e341cca46a973ec61c9f0f","answers":[{"stepId":"r16a_ab","selectedOptionIds":["r16a_ab_opt1"],"selectedOther":false},{"stepId":"r16b_q3","selectedOptionIds":["r16b_q3_opt2"],"selectedOther":false},{"stepId":"r16c_149","selectedOptionIds":["r16c_149_opt2"],"selectedOther":false}],"submittedAt":1791558714974}
```

**答文逐字（逐条展开，原文照录）**

答 1／3 — 原始对象：

```json
{"stepId": "r16a_ab", "selectedOptionIds": ["r16a_ab_opt1"], "selectedOther": false}
```

- `stepId`：`r16a_ab`
- `selectedOptionIds`（逐字）：`["r16a_ab_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r16a_ab_opt1` → `label`: ```择优 β 转正——派正式跑＋verifier＋判定链```
      → `description`: （无此键）

答 2／3 — 原始对象：

```json
{"stepId": "r16b_q3", "selectedOptionIds": ["r16b_q3_opt2"], "selectedOther": false}
```

- `stepId`：`r16b_q3`
- `selectedOptionIds`（逐字）：`["r16b_q3_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r16b_q3_opt2` → `label`: ```随转正链一并处置（先修再跑）```
      → `description`: （无此键）

答 3／3 — 原始对象：

```json
{"stepId": "r16c_149", "selectedOptionIds": ["r16c_149_opt2"], "selectedOther": false}
```

- `stepId`：`r16c_149`
- `selectedOptionIds`（逐字）：`["r16c_149_opt2"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r16c_149_opt2` → `label`: ```另议```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1627    字节数(UTF-8) = 2140
reply_payload  字符数 = 344      字节数(UTF-8) = 344
steps 步数 = 3 ／ options 总数 = 9 ／ answers 条数 = 3
question 字符数（逐 step）: r16a_ab=127; r16b_q3=114; r16c_149=50
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 12 · `ask_7a159c56037e3c8bb7239d6a` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> KD 指引生效＋S4 两重判复核（两题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_7a159c56037e3c8bb7239d6a
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = KD 指引生效＋S4 两重判复核（两题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = bd8efc27-1c0d-40bb-864b-279a59e683b9
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_vAHtC5654zePrHuWrkqn0649
request_json.createdAt (epoch ms) = 1791559526390   → 2026-10-09 23:25:26.390 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791559526390
created_at (CST 换算)          = 2026-10-09 23:25:26.390 +0800
answered_at (epoch ms)         = 1791559562420
answered_at (CST 换算)         = 2026-10-09 23:26:02.420 +0800
reply_payload.submittedAt(epoch ms) = 1791559562420   → 2026-10-09 23:26:02.420 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 2 步／6 选项，原文照录）**

**题 1／2** — `id` = `r17a_kd`

- `header`（原文照录）：`KD 指引生效`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
KD 书写体例指引件（708dfac55be9）：其 VK-1／1b／2／3 已分头裁（逐处改写令／不明即挂账／族③确认／子代理再判）——指引本体（21 条规则）是否复核生效？
```

`options`（逐字原文，共 3 项）：

- `id` = `r17a_kd_opt1`
  - `label`（逐字原文）：```核准生效（生效即锁）```
  - `description`（逐字原文）：（无此键）
- `id` = `r17a_kd_opt2`
  - `label`（逐字原文）：```暂缓```
  - `description`（逐字原文）：（无此键）
- `id` = `r17a_kd_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／2** — `id` = `r17b_verdicts`

- `header`（原文照录）：`两重判复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4 两重判件复核：-1/-2（`9cde399502ba`：FAIL／FAIL·真证伪）与 -4（`bc397d5099dd`：五线 hit 全触发·form A 合取不成立·真证伪 0）——两件档位是否复核确认（ⓘ 入链伴 verifier 签字，EA 批 b2 在候槽）？
```

`options`（逐字原文，共 3 项）：

- `id` = `r17b_verdicts_opt1`
  - `label`（逐字原文）：```复核确认两件档位```
  - `description`（逐字原文）：（无此键）
- `id` = `r17b_verdicts_opt2`
  - `label`（逐字原文）：```候 verifier 批 b2 一并复核```
  - `description`（逐字原文）：（无此键）
- `id` = `r17b_verdicts_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_7a159c56037e3c8bb7239d6a","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r17a_kd","question":"KD 书写体例指引件（708dfac55be9）：其 VK-1／1b／2／3 已分头裁（逐处改写令／不明即挂账／族③确认／子代理再判）——指引本体（21 条规则）是否复核生效？","selectionMode":"single","options":[{"id":"r17a_kd_opt1","label":"核准生效（生效即锁）"},{"id":"r17a_kd_opt2","label":"暂缓"},{"id":"r17a_kd_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"KD 指引生效"},{"id":"r17b_verdicts","question":"S4 两重判件复核：-1/-2（`9cde399502ba`：FAIL／FAIL·真证伪）与 -4（`bc397d5099dd`：五线 hit 全触发·form A 合取不成立·真证伪 0）——两件档位是否复核确认（ⓘ 入链伴 verifier 签字，EA 批 b2 在候槽）？","selectionMode":"single","options":[{"id":"r17b_verdicts_opt1","label":"复核确认两件档位"},{"id":"r17b_verdicts_opt2","label":"候 verifier 批 b2 一并复核"},{"id":"r17b_verdicts_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"两重判复核"}],"status":"pending","createdAt":1791559526390,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"bd8efc27-1c0d-40bb-864b-279a59e683b9","toolCallId":"call_00_vAHtC5654zePrHuWrkqn0649"},"title":"KD 指引生效＋S4 两重判复核（两题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_7a159c56037e3c8bb7239d6a","answers":[{"stepId":"r17a_kd","selectedOptionIds":["r17a_kd_opt1"],"selectedOther":false},{"stepId":"r17b_verdicts","selectedOptionIds":["r17b_verdicts_opt1"],"selectedOther":false}],"submittedAt":1791559562420}
```

**答文逐字（逐条展开，原文照录）**

答 1／2 — 原始对象：

```json
{"stepId": "r17a_kd", "selectedOptionIds": ["r17a_kd_opt1"], "selectedOther": false}
```

- `stepId`：`r17a_kd`
- `selectedOptionIds`（逐字）：`["r17a_kd_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r17a_kd_opt1` → `label`: ```核准生效（生效即锁）```
      → `description`: （无此键）

答 2／2 — 原始对象：

```json
{"stepId": "r17b_verdicts", "selectedOptionIds": ["r17b_verdicts_opt1"], "selectedOther": false}
```

- `stepId`：`r17b_verdicts`
- `selectedOptionIds`（逐字）：`["r17b_verdicts_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r17b_verdicts_opt1` → `label`: ```复核确认两件档位```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1226    字节数(UTF-8) = 1569
reply_payload  字符数 = 274      字节数(UTF-8) = 274
steps 步数 = 2 ／ options 总数 = 6 ／ answers 条数 = 2
question 字符数（逐 step）: r17a_kd=88; r17b_verdicts=139
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 13 · `ask_995f776b589725afdd44ea6d` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 收口批①：B/C 复核＋β 三项（四题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_995f776b589725afdd44ea6d
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 收口批①：B/C 复核＋β 三项（四题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = 77f72e45-5061-4afb-91d2-8e4ae81dbae0
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_T3tuHNhPWNVnFS2Chcck4570
request_json.createdAt (epoch ms) = 1791560530658   → 2026-10-09 23:42:10.658 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791560530658
created_at (CST 换算)          = 2026-10-09 23:42:10.658 +0800
answered_at (epoch ms)         = 1791560560612
answered_at (CST 换算)         = 2026-10-09 23:42:40.612 +0800
reply_payload.submittedAt(epoch ms) = 1791560560612   → 2026-10-09 23:42:40.612 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／11 选项，原文照录）**

**题 1／4** — `id` = `r18a_bc`

- `header`（原文照录）：`B/C 择定复核`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S4·B/C 构造择定复核（件 E2FDB380CD3C）：采「构造①（自身域 resample）为 K-2 判读口径，构造②保留为敏感性面·并陈不删」（依据 estimand 同一性与构造洁净度；拒绝以宽窄作择据）——核准生效？
```

`options`（逐字原文，共 2 项）：

- `id` = `r18a_bc_opt1`
  - `label`（逐字原文）：```核准生效（生效即锁）```
  - `description`（逐字原文）：（无此键）
- `id` = `r18a_bc_opt2`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `r18b_q3`

- `header`（原文照录）：`Q-3 修否`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·β 正式跑·Q-3 修否（勘误件 659c4101f10b）：全仓唯一生产性转置点 7761f2c339e6 L282（镜像下 no-op、既往读数 0 变动；非对称构造下逐格出错）——修与不修？
```

`options`（逐字原文，共 3 项）：

- `id` = `r18b_q3_opt1`
  - `label`（逐字原文）：```修——派另棒出修正/同步件（0 回改原件）```
  - `description`（逐字原文）：（无此键）
- `id` = `r18b_q3_opt2`
  - `label`（逐字原文）：```不修——仅勘误登记在册```
  - `description`（逐字原文）：（无此键）
- `id` = `r18b_q3_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `r18c_gate`

- `header`（原文照录）：`门偏离追认`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·β 正式跑·K-RO-0-1 门偏离是否成立（register 2e5f080eab6c §11）：16/20 列过门、4 列取值集中 ⇒ 门字面未满足、依你授权起跑（偏离已登记）——是否追认偏离成立？
```

`options`（逐字原文，共 3 项）：

- `id` = `r18c_gate_opt1`
  - `label`（逐字原文）：```追认——偏离成立·留痕```
  - `description`（逐字原文）：（无此键）
- `id` = `r18c_gate_opt2`
  - `label`（逐字原文）：```不成立——另有处置```
  - `description`（逐字原文）：（无此键）
- `id` = `r18c_gate_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `r18d_th`

- `header`（原文照录）：`旧门槛重声明`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·旧门槛：β 半换域＋构造变更 ⇒ TH-V3R-1 之 1.3×／2.0× 解释是否仍适用？（α 路此前亦裁「须重声明·另定」）
```

`options`（逐字原文，共 3 项）：

- `id` = `r18d_th_opt1`
  - `label`（逐字原文）：```须重声明——另定```
  - `description`（逐字原文）：（无此键）
- `id` = `r18d_th_opt2`
  - `label`（逐字原文）：```旧门槛仍适用```
  - `description`（逐字原文）：（无此键）
- `id` = `r18d_th_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_995f776b589725afdd44ea6d","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r18a_bc","question":"S4·B/C 构造择定复核（件 E2FDB380CD3C）：采「构造①（自身域 resample）为 K-2 判读口径，构造②保留为敏感性面·并陈不删」（依据 estimand 同一性与构造洁净度；拒绝以宽窄作择据）——核准生效？","selectionMode":"single","options":[{"id":"r18a_bc_opt1","label":"核准生效（生效即锁）"},{"id":"r18a_bc_opt2","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"B/C 择定复核"},{"id":"r18b_q3","question":"V3-05·β 正式跑·Q-3 修否（勘误件 659c4101f10b）：全仓唯一生产性转置点 7761f2c339e6 L282（镜像下 no-op、既往读数 0 变动；非对称构造下逐格出错）——修与不修？","selectionMode":"single","options":[{"id":"r18b_q3_opt1","label":"修——派另棒出修正/同步件（0 回改原件）"},{"id":"r18b_q3_opt2","label":"不修——仅勘误登记在册"},{"id":"r18b_q3_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"Q-3 修否"},{"id":"r18c_gate","question":"V3-05·β 正式跑·K-RO-0-1 门偏离是否成立（register 2e5f080eab6c §11）：16/20 列过门、4 列取值集中 ⇒ 门字面未满足、依你授权起跑（偏离已登记）——是否追认偏离成立？","selectionMode":"single","options":[{"id":"r18c_gate_opt1","label":"追认——偏离成立·留痕"},{"id":"r18c_gate_opt2","label":"不成立——另有处置"},{"id":"r18c_gate_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"门偏离追认"},{"id":"r18d_th","question":"V3-05·旧门槛：β 半换域＋构造变更 ⇒ TH-V3R-1 之 1.3×／2.0× 解释是否仍适用？（α 路此前亦裁「须重声明·另定」）","selectionMode":"single","options":[{"id":"r18d_th_opt1","label":"须重声明——另定"},{"id":"r18d_th_opt2","label":"旧门槛仍适用"},{"id":"r18d_th_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"旧门槛重声明"}],"status":"pending","createdAt":1791560530658,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"77f72e45-5061-4afb-91d2-8e4ae81dbae0","toolCallId":"call_00_T3tuHNhPWNVnFS2Chcck4570"},"title":"收口批①：B/C 复核＋β 三项（四题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_995f776b589725afdd44ea6d","answers":[{"stepId":"r18a_bc","selectedOptionIds":["r18a_bc_opt1"],"selectedOther":false},{"stepId":"r18b_q3","selectedOptionIds":["r18b_q3_opt1"],"selectedOther":false},{"stepId":"r18c_gate","selectedOptionIds":["r18c_gate_opt1"],"selectedOther":false},{"stepId":"r18d_th","selectedOptionIds":["r18d_th_opt1"],"selectedOther":false}],"submittedAt":1791560560612}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r18a_bc", "selectedOptionIds": ["r18a_bc_opt1"], "selectedOther": false}
```

- `stepId`：`r18a_bc`
- `selectedOptionIds`（逐字）：`["r18a_bc_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r18a_bc_opt1` → `label`: ```核准生效（生效即锁）```
      → `description`: （无此键）

答 2／4 — 原始对象：

```json
{"stepId": "r18b_q3", "selectedOptionIds": ["r18b_q3_opt1"], "selectedOther": false}
```

- `stepId`：`r18b_q3`
- `selectedOptionIds`（逐字）：`["r18b_q3_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r18b_q3_opt1` → `label`: ```修——派另棒出修正/同步件（0 回改原件）```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "r18c_gate", "selectedOptionIds": ["r18c_gate_opt1"], "selectedOther": false}
```

- `stepId`：`r18c_gate`
- `selectedOptionIds`（逐字）：`["r18c_gate_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r18c_gate_opt1` → `label`: ```追认——偏离成立·留痕```
      → `description`: （无此键）

答 4／4 — 原始对象：

```json
{"stepId": "r18d_th", "selectedOptionIds": ["r18d_th_opt1"], "selectedOther": false}
```

- `stepId`：`r18d_th`
- `selectedOptionIds`（逐字）：`["r18d_th_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r18d_th_opt1` → `label`: ```须重声明——另定```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1887    字节数(UTF-8) = 2552
reply_payload  字符数 = 426      字节数(UTF-8) = 426
steps 步数 = 4 ／ options 总数 = 11 ／ answers 条数 = 4
question 字符数（逐 step）: r18a_bc=115; r18b_q3=104; r18c_gate=107; r18d_th=70
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 14 · `ask_4ad2d308aee5ec669a3a438d` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 收口批②：报值口径＋词表两项＋T1⑧（四题）

**卡级元数据（原文照录）**

```text
request_id                     = ask_4ad2d308aee5ec669a3a438d
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 收口批②：报值口径＋词表两项＋T1⑧（四题）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_89eaf689-a12b-461a-b288-1573536047be
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_Jo2thgg4tfICASLaRz6A3202
request_json.createdAt (epoch ms) = 1791560623175   → 2026-10-09 23:43:43.175 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791560623175
created_at (CST 换算)          = 2026-10-09 23:43:43.175 +0800
answered_at (epoch ms)         = 1791560650081
answered_at (CST 换算)         = 2026-10-09 23:44:10.081 +0800
reply_payload.submittedAt(epoch ms) = 1791560650081   → 2026-10-09 23:44:10.081 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `r19a_caliber`

- `header`（原文照录）：`报值口径修订`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
V3-05·β 正式跑·Q-3 报值口径是否修订：预实验报 48/88・80/88（计数器×2 放大）vs 精确定义实测 24/88・40/88（α证据段・β本跑）——已登记双读、0 回改。是否出勘误补记？
```

`options`（逐字原文，共 3 项）：

- `id` = `r19a_caliber_opt1`
  - `label`（逐字原文）：```修订——出勘误补记（0 回改预实验件）```
  - `description`（逐字原文）：（无此键）
- `id` = `r19a_caliber_opt2`
  - `label`（逐字原文）：```不修订——双读并报维持```
  - `description`（逐字原文）：（无此键）
- `id` = `r19a_caliber_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 2／4** — `id` = `r19b_grades`

- `header`（原文照录）：`词表分级设计`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
RPQ 词表·分级设计（判件 246CE35C4DDC ①）：是否采「命中即强制语义定性」之分級（触发位、非判据位）＋先立单一词表之家（现两表分居）？
```

`options`（逐字原文，共 3 项）：

- `id` = `r19b_grades_opt1`
  - `label`（逐字原文）：```采——分级（触发位）＋先立单一词表之家```
  - `description`（逐字原文）：（无此键）
- `id` = `r19b_grades_opt2`
  - `label`（逐字原文）：```简单增补——裸形并入现表```
  - `description`（逐字原文）：（无此键）
- `id` = `r19b_grades_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 3／4** — `id` = `r19c_external`

- `header`（原文照录）：`对外件面适用`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
RPQ 词表·对外件面适用（判件倾向排除——「画像」在对外面属正当方法论表述、字面同形）：对外件面是否同表适用？
```

`options`（逐字原文，共 3 项）：

- `id` = `r19c_external_opt1`
  - `label`（逐字原文）：```排除——对外件面不同表适用```
  - `description`（逐字原文）：（无此键）
- `id` = `r19c_external_opt2`
  - `label`（逐字原文）：```适用——对外件面同表```
  - `description`（逐字原文）：（无此键）
- `id` = `r19c_external_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

**题 4／4** — `id` = `r19d_t1p2`

- `header`（原文照录）：`T1⑧ 升格`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧·处置（判件 246CE35C4DDC ②）：升格「一裁三带」＋§10②⑤⑧ 合并一行＋即刻激活（以 D-1 落定为前置）——接受否？
```

`options`（逐字原文，共 3 项）：

- `id` = `r19d_t1p2_opt1`
  - `label`（逐字原文）：```接受——升格＋合并一行＋激活前置 D-1```
  - `description`（逐字原文）：（无此键）
- `id` = `r19d_t1p2_opt2`
  - `label`（逐字原文）：```部分接受（Other 说明）```
  - `description`（逐字原文）：（无此键）
- `id` = `r19d_t1p2_opt3`
  - `label`（逐字原文）：```另议```
  - `description`（逐字原文）：（无此键）

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_4ad2d308aee5ec669a3a438d","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"r19a_caliber","question":"V3-05·β 正式跑·Q-3 报值口径是否修订：预实验报 48/88・80/88（计数器×2 放大）vs 精确定义实测 24/88・40/88（α证据段・β本跑）——已登记双读、0 回改。是否出勘误补记？","selectionMode":"single","options":[{"id":"r19a_caliber_opt1","label":"修订——出勘误补记（0 回改预实验件）"},{"id":"r19a_caliber_opt2","label":"不修订——双读并报维持"},{"id":"r19a_caliber_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"报值口径修订"},{"id":"r19b_grades","question":"RPQ 词表·分级设计（判件 246CE35C4DDC ①）：是否采「命中即强制语义定性」之分級（触发位、非判据位）＋先立单一词表之家（现两表分居）？","selectionMode":"single","options":[{"id":"r19b_grades_opt1","label":"采——分级（触发位）＋先立单一词表之家"},{"id":"r19b_grades_opt2","label":"简单增补——裸形并入现表"},{"id":"r19b_grades_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"词表分级设计"},{"id":"r19c_external","question":"RPQ 词表·对外件面适用（判件倾向排除——「画像」在对外面属正当方法论表述、字面同形）：对外件面是否同表适用？","selectionMode":"single","options":[{"id":"r19c_external_opt1","label":"排除——对外件面不同表适用"},{"id":"r19c_external_opt2","label":"适用——对外件面同表"},{"id":"r19c_external_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"对外件面适用"},{"id":"r19d_t1p2","question":"T1⑧·处置（判件 246CE35C4DDC ②）：升格「一裁三带」＋§10②⑤⑧ 合并一行＋即刻激活（以 D-1 落定为前置）——接受否？","selectionMode":"single","options":[{"id":"r19d_t1p2_opt1","label":"接受——升格＋合并一行＋激活前置 D-1"},{"id":"r19d_t1p2_opt2","label":"部分接受（Other 说明）"},{"id":"r19d_t1p2_opt3","label":"另议"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1⑧ 升格"}],"status":"pending","createdAt":1791560623175,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_89eaf689-a12b-461a-b288-1573536047be","toolCallId":"call_00_Jo2thgg4tfICASLaRz6A3202"},"title":"收口批②：报值口径＋词表两项＋T1⑧（四题）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_4ad2d308aee5ec669a3a438d","answers":[{"stepId":"r19a_caliber","selectedOptionIds":["r19a_caliber_opt1"],"selectedOther":false},{"stepId":"r19b_grades","selectedOptionIds":["r19b_grades_opt1"],"selectedOther":false},{"stepId":"r19c_external","selectedOptionIds":["r19c_external_opt3"],"selectedOther":false},{"stepId":"r19d_t1p2","selectedOptionIds":["r19d_t1p2_opt1"],"selectedOther":false}],"submittedAt":1791560650081}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "r19a_caliber", "selectedOptionIds": ["r19a_caliber_opt1"], "selectedOther": false}
```

- `stepId`：`r19a_caliber`
- `selectedOptionIds`（逐字）：`["r19a_caliber_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r19a_caliber_opt1` → `label`: ```修订——出勘误补记（0 回改预实验件）```
      → `description`: （无此键）

答 2／4 — 原始对象：

```json
{"stepId": "r19b_grades", "selectedOptionIds": ["r19b_grades_opt1"], "selectedOther": false}
```

- `stepId`：`r19b_grades`
- `selectedOptionIds`（逐字）：`["r19b_grades_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r19b_grades_opt1` → `label`: ```采——分级（触发位）＋先立单一词表之家```
      → `description`: （无此键）

答 3／4 — 原始对象：

```json
{"stepId": "r19c_external", "selectedOptionIds": ["r19c_external_opt3"], "selectedOther": false}
```

- `stepId`：`r19c_external`
- `selectedOptionIds`（逐字）：`["r19c_external_opt3"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r19c_external_opt3` → `label`: ```另议```
      → `description`: （无此键）

答 4／4 — 原始对象：

```json
{"stepId": "r19d_t1p2", "selectedOptionIds": ["r19d_t1p2_opt1"], "selectedOther": false}
```

- `stepId`：`r19d_t1p2`
- `selectedOptionIds`（逐字）：`["r19d_t1p2_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `r19d_t1p2_opt1` → `label`: ```接受——升格＋合并一行＋激活前置 D-1```
      → `description`: （无此键）

**关键字段长度（实测）**

```text
request_json   字符数 = 1936    字节数(UTF-8) = 2674
reply_payload  字符数 = 456      字节数(UTF-8) = 456
steps 步数 = 4 ／ options 总数 = 12 ／ answers 条数 = 4
question 字符数（逐 step）: r19a_caliber=103; r19b_grades=75; r19c_external=56; r19d_t1p2=70
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 15 · `ask_4bf0d908084b3646a40ad4d6` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮20 · 代立草案核准批（4/10 项：D-07 / D-08 / D-03 / D-06）

**卡级元数据（原文照录）**

```text
request_id                     = ask_4bf0d908084b3646a40ad4d6
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮20 · 代立草案核准批（4/10 项：D-07 / D-08 / D-03 / D-06）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = 5718916d-309c-402b-b248-2ecf60e0092a
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_DkDlZ9Q4nE1oQtojuKNR5607
request_json.createdAt (epoch ms) = 1791561828100   → 2026-10-10 00:03:48.100 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791561828100
created_at (CST 换算)          = 2026-10-10 00:03:48.100 +0800
answered_at (epoch ms)         = 1791562030140
answered_at (CST 换算)         = 2026-10-10 00:07:10.140 +0800
reply_payload.submittedAt(epoch ms) = 1791562030140   → 2026-10-10 00:07:10.140 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `d07`

- `header`（原文照录）：`T1·D 段判读线（D-07）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1 温度轴 D 段（seed 探针）判读线。事实：D 段已于今日 22:45 跑毕——50/50 calls 成功；100 对重复中 full_reply 全同 0 对（全同率 0.0）、50 条 full_reply 哈希全异、答案面取值仅 6 种。草案 D-07 主张维持现状：D 段读数只作事实登记、不承载任何 kill-line（无需 PI 给值，即刻成立）。注意硬约束『给线须早于起跑』：D 段已跑毕，现在给线属事后给线（须注明瑕疵），或须重跑 D 段。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `d07_opt1`
  - `label`（逐字原文）：```维持 0 承载——读数只作事实登记（推荐）```
  - `description`（逐字原文）：```沿草案 D-07①；无需给值。D 段值作为 seed 端点支持性的事实证据存档（实测 0/100 全同）。```
- `id` = `d07_opt2`
  - `label`（逐字原文）：```给线·接受事后瑕疵——三项在 Other 给出```
  - `description`（逐字原文）：```须给 (a) 判定线形式、(b) 数值；并注明给线时点晚于起跑。```
- `id` = `d07_opt3`
  - `label`（逐字原文）：```重跑 D 段——候线给齐后重跑```
  - `description`（逐字原文）：```当前读数存档保留；重跑前须先给 (a)(b) 两项与 D-08 归属。```

**题 2／4** — `id` = `d08`

- `header`（原文照录）：`『部分全同』归属（D-08）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
『部分全同』之归属。事实：本次 D 段实测『部分全同』0 出现（50 条中未观测到半同形态），但归属定义仍缺、未来面仍会遇到。草案 D-08 主张三态并列：seed_support 取值 full / partial / none，partial 作为独立第三态（不归 full、不归 none），三态各计件数与占比并报。请裁归属：
```

`options`（逐字原文，共 4 项）：

- `id` = `d08_opt1`
  - `label`（逐字原文）：```三态并列＋seed_support 字段（推荐）```
  - `description`（逐字原文）：```full/partial/none 各计件数占比，不折叠中间态；可机器核验。```
- `id` = `d08_opt2`
  - `label`（逐字原文）：```二态·partial 归 none（保守）```
  - `description`（逐字原文）：```未全同即视为无支持；会掩盖部分遵守之信息。```
- `id` = `d08_opt3`
  - `label`（逐字原文）：```二态·partial 归 full```
  - `description`（逐字原文）：```草案明确反对：将部分遵守充作完全遵守，属读数拔高。```
- `id` = `d08_opt4`
  - `label`（逐字原文）：```不设字段·仅正文描述```
  - `description`（逐字原文）：```不可机器核验，草案不建议。```

**题 3／4** — `id` = `d03`

- `header`（原文照录）：`B/C 等效门柱（D-03）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
B/C『等效门柱』数值。现状：K-1 已生效——B/C 暂免 0.1100，半宽仅报、不入判读。草案 D-03 主张三段式：一是维持暂免（即刻成立、无需给值）；二是形式先行（若欲令 B/C 受约束，先裁口径形式，即按分母规模归一之等效门柱）；三是数值后给（数值须在当轮基线面重算后另给，禁止由本轮读数反推）。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `d03_opt1`
  - `label`（逐字原文）：```三段式——暂挂·形式先行·数值后给（推荐）```
  - `description`（逐字原文）：```维持现状默认段；B/C 精度面继续只报不判，如实登记。```
- `id` = `d03_opt2`
  - `label`（逐字原文）：```永久暂挂且不裁形式```
  - `description`（逐字原文）：```B/C 半宽永久不入判读；与『不知亦为挂账』相悖，须如实登记为长期未闭。```
- `id` = `d03_opt3`
  - `label`（逐字原文）：```现在给数值——数值在 Other 给出```
  - `description`（逐字原文）：```须声明来源非本轮读数反推；否则违判死线先于实验纪律。```
- `id` = `d03_opt4`
  - `label`（逐字原文）：```分线给柱——B、C 各一柱```
  - `description`（逐字原文）：```数值在 Other 给出，同样须声明非反推。```

**题 4／4** — `id` = `d06`

- `header`（原文照录）：`P-S4-1 闭条件（D-06）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
P-S4-1『重立』面之闭条件。现状：候 C-1 细目落定（盘上无结法）。草案 D-06 主张单一闭条件式：P-S4-1 仅以『C-1 细目齐备』为唯一闭条件（细目齐备＝A 组 P1–P8 含 D-01 字段名、加 N1–N5，全部经 PI 复核生效）；在此之前维持候裁，之后自动闭为『重立完成』，不再以任何其他条件另开闭条件。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `d06_opt1`
  - `label`（逐字原文）：```单一闭条件＝C-1 细目齐备（推荐）```
  - `description`（逐字原文）：```闭条件唯一、可逐项点名核验。```
- `id` = `d06_opt2`
  - `label`（逐字原文）：```双条件＝细目齐备 ∧ 五线 CI 读数落盘```
  - `description`（逐字原文）：```更严；但二者混为一条后口径面与采集面互相等待，本面长期不可闭。```
- `id` = `d06_opt3`
  - `label`（逐字原文）：```维持无限期候裁```
  - `description`（逐字原文）：```挂账未清，草案不建议。```

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_4bf0d908084b3646a40ad4d6","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"d07","question":"T1 温度轴 D 段（seed 探针）判读线。事实：D 段已于今日 22:45 跑毕——50/50 calls 成功；100 对重复中 full_reply 全同 0 对（全同率 0.0）、50 条 full_reply 哈希全异、答案面取值仅 6 种。草案 D-07 主张维持现状：D 段读数只作事实登记、不承载任何 kill-line（无需 PI 给值，即刻成立）。注意硬约束『给线须早于起跑』：D 段已跑毕，现在给线属事后给线（须注明瑕疵），或须重跑 D 段。请裁：","selectionMode":"single","options":[{"id":"d07_opt1","label":"维持 0 承载——读数只作事实登记（推荐）","description":"沿草案 D-07①；无需给值。D 段值作为 seed 端点支持性的事实证据存档（实测 0/100 全同）。"},{"id":"d07_opt2","label":"给线·接受事后瑕疵——三项在 Other 给出","description":"须给 (a) 判定线形式、(b) 数值；并注明给线时点晚于起跑。"},{"id":"d07_opt3","label":"重跑 D 段——候线给齐后重跑","description":"当前读数存档保留；重跑前须先给 (a)(b) 两项与 D-08 归属。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1·D 段判读线（D-07）"},{"id":"d08","question":"『部分全同』之归属。事实：本次 D 段实测『部分全同』0 出现（50 条中未观测到半同形态），但归属定义仍缺、未来面仍会遇到。草案 D-08 主张三态并列：seed_support 取值 full / partial / none，partial 作为独立第三态（不归 full、不归 none），三态各计件数与占比并报。请裁归属：","selectionMode":"single","options":[{"id":"d08_opt1","label":"三态并列＋seed_support 字段（推荐）","description":"full/partial/none 各计件数占比，不折叠中间态；可机器核验。"},{"id":"d08_opt2","label":"二态·partial 归 none（保守）","description":"未全同即视为无支持；会掩盖部分遵守之信息。"},{"id":"d08_opt3","label":"二态·partial 归 full","description":"草案明确反对：将部分遵守充作完全遵守，属读数拔高。"},{"id":"d08_opt4","label":"不设字段·仅正文描述","description":"不可机器核验，草案不建议。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"『部分全同』归属（D-08）"},{"id":"d03","question":"B/C『等效门柱』数值。现状：K-1 已生效——B/C 暂免 0.1100，半宽仅报、不入判读。草案 D-03 主张三段式：一是维持暂免（即刻成立、无需给值）；二是形式先行（若欲令 B/C 受约束，先裁口径形式，即按分母规模归一之等效门柱）；三是数值后给（数值须在当轮基线面重算后另给，禁止由本轮读数反推）。请裁：","selectionMode":"single","options":[{"id":"d03_opt1","label":"三段式——暂挂·形式先行·数值后给（推荐）","description":"维持现状默认段；B/C 精度面继续只报不判，如实登记。"},{"id":"d03_opt2","label":"永久暂挂且不裁形式","description":"B/C 半宽永久不入判读；与『不知亦为挂账』相悖，须如实登记为长期未闭。"},{"id":"d03_opt3","label":"现在给数值——数值在 Other 给出","description":"须声明来源非本轮读数反推；否则违判死线先于实验纪律。"},{"id":"d03_opt4","label":"分线给柱——B、C 各一柱","description":"数值在 Other 给出，同样须声明非反推。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"B/C 等效门柱（D-03）"},{"id":"d06","question":"P-S4-1『重立』面之闭条件。现状：候 C-1 细目落定（盘上无结法）。草案 D-06 主张单一闭条件式：P-S4-1 仅以『C-1 细目齐备』为唯一闭条件（细目齐备＝A 组 P1–P8 含 D-01 字段名、加 N1–N5，全部经 PI 复核生效）；在此之前维持候裁，之后自动闭为『重立完成』，不再以任何其他条件另开闭条件。请裁：","selectionMode":"single","options":[{"id":"d06_opt1","label":"单一闭条件＝C-1 细目齐备（推荐）","description":"闭条件唯一、可逐项点名核验。"},{"id":"d06_opt2","label":"双条件＝细目齐备 ∧ 五线 CI 读数落盘","description":"更严；但二者混为一条后口径面与采集面互相等待，本面长期不可闭。"},{"id":"d06_opt3","label":"维持无限期候裁","description":"挂账未清，草案不建议。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"P-S4-1 闭条件（D-06）"}],"status":"pending","createdAt":1791561828100,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"5718916d-309c-402b-b248-2ecf60e0092a","toolCallId":"call_00_DkDlZ9Q4nE1oQtojuKNR5607"},"title":"轮20 · 代立草案核准批（4/10 项：D-07 / D-08 / D-03 / D-06）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_4bf0d908084b3646a40ad4d6","answers":[{"stepId":"d07","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"},{"stepId":"d08","selectedOptionIds":["d08_opt1"],"selectedOther":false},{"stepId":"d03","selectedOptionIds":["d03_opt1"],"selectedOther":false},{"stepId":"d06","selectedOptionIds":["d06_opt1"],"selectedOther":false}],"submittedAt":1791562030140}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "d07", "selectedOptionIds": [], "selectedOther": true, "otherText": "另议"}
```

- `stepId`：`d07`
- `selectedOptionIds`（逐字）：`[]`
- `selectedOther`（逐字）：`true`
- `otherText`：

```text
另议
```

答 2／4 — 原始对象：

```json
{"stepId": "d08", "selectedOptionIds": ["d08_opt1"], "selectedOther": false}
```

- `stepId`：`d08`
- `selectedOptionIds`（逐字）：`["d08_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d08_opt1` → `label`: ```三态并列＋seed_support 字段（推荐）```
      → `description`: ```full/partial/none 各计件数占比，不折叠中间态；可机器核验。```

答 3／4 — 原始对象：

```json
{"stepId": "d03", "selectedOptionIds": ["d03_opt1"], "selectedOther": false}
```

- `stepId`：`d03`
- `selectedOptionIds`（逐字）：`["d03_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d03_opt1` → `label`: ```三段式——暂挂·形式先行·数值后给（推荐）```
      → `description`: ```维持现状默认段；B/C 精度面继续只报不判，如实登记。```

答 4／4 — 原始对象：

```json
{"stepId": "d06", "selectedOptionIds": ["d06_opt1"], "selectedOther": false}
```

- `stepId`：`d06`
- `selectedOptionIds`（逐字）：`["d06_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d06_opt1` → `label`: ```单一闭条件＝C-1 细目齐备（推荐）```
      → `description`: ```闭条件唯一、可逐项点名核验。```

**关键字段长度（实测）**

```text
request_json   字符数 = 3074    字节数(UTF-8) = 5056
reply_payload  字符数 = 396      字节数(UTF-8) = 400
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: d07=236; d08=166; d03=157; d06=167
selectedOther=true 条数 = 1 ／ 含 otherText 键条数 = 1 ／ otherText 字符数合计 = 2
```

---

### 16 · `ask_a6f1d49c7337342253351ccd` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮21 · 代立草案核准批（4/10 项：D-04 / D-05 / D-01 / D-02）

**卡级元数据（原文照录）**

```text
request_id                     = ask_a6f1d49c7337342253351ccd
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮21 · 代立草案核准批（4/10 项：D-04 / D-05 / D-01 / D-02）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_02bc970c-8c71-4c99-9941-17d98c0e7dca
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_cClJGwRSC2Nw3x6mRiT70937
request_json.createdAt (epoch ms) = 1791562437016   → 2026-10-10 00:13:57.016 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791562437016
created_at (CST 换算)          = 2026-10-10 00:13:57.016 +0800
answered_at (epoch ms)         = 1791562460022
answered_at (CST 换算)         = 2026-10-10 00:14:20.022 +0800
reply_payload.submittedAt(epoch ms) = 1791562460022   → 2026-10-10 00:14:20.022 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `d04`

- `header`（原文照录）：`C 线分母扩充（D-04）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
C 线分母仅 5——上界触顶、近乎恒触发、判别力弱（v3 面为 9）。草案 D-04 拟三步：一是以 held-out 全域 26 件为母体重抽样至 n＝9（对齐 v3 面规模），逐件登记抽取路径；二是先立 kill-line K-C-DEN-1（C 之 CI 上界＜0.10 达标／≥0.10 不达标／不可构造即不明）方可跑——判死线先于实验；三是扩充读数另立新件并陈，不覆写既有读数件。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `d04_opt1`
  - `label`（逐字原文）：```三步案——n=9＋新 kill-line＋并陈（推荐）```
  - `description`（逐字原文）：```①以 held-out 全域 26 件为母体重抽样至 n=9（对齐 v3 面规模），逐件登记抽取路径；②先立 K-C-DEN-1 后方可跑；③扩充读数另立新件并陈。```
- `id` = `d04_opt2`
  - `label`（逐字原文）：```维持 n=5 不动```
  - `description`（逐字原文）：```C 判别力弱永久登记为构造效度限制（非失败，是 0 判定）。```
- `id` = `d04_opt3`
  - `label`（逐字原文）：```扩至其它规模```
  - `description`（逐字原文）：```数值在 Other 给出；须声明非由本轮读数反推。```
- `id` = `d04_opt4`
  - `label`（逐字原文）：```改用非比例型 C 统计量```
  - `description`（逐字原文）：```须另立口径，不沿用现构造。```

**题 2／4** — `id` = `d05`

- `header`（原文照录）：`B 巧合排除（D-05）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
B 点估计 9/21 与 v3 面 6/14 皆约分至 3/7——逐位同值之巧合未排除（0 断言两面等价）。草案 D-05 拟三检并施：一是约分同值检（以 held-out 全域改分母重算；如实标注『该分母下未复现』）；二是同源数据检（v3 与 S4 之件集交集核对）；三是构造差异检（仅 v3 有、S4 无之件上施测——素材不可得则如实登记『不可施』，0 以检一二冒充）。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `d05_opt1`
  - `label`（逐字原文）：```三检并施（③不可施则如实登记）（推荐）```
  - `description`（逐字原文）：```①约分同值检（改分母重算）；②同源数据检（件集交集核对）；③构造差异检（不可施则如实登记）。```
- `id` = `d05_opt2`
  - `label`（逐字原文）：```仅施检一```
  - `description`（逐字原文）：```省；但 0 排除同源解释。```
- `id` = `d05_opt3`
  - `label`（逐字原文）：```维持『巧合未排除』永久登记```
  - `description`（逐字原文）：```属挂账未清面，草案不建议。```
- `id` = `d05_opt4`
  - `label`（逐字原文）：```写入『两面等价』口径```
  - `description`（逐字原文）：```草案明确反对——0 证据之断言。```

**题 3／4** — `id` = `d01`

- `header`（原文照录）：`h₃ provenance 字段名（D-01）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
h₃ 退为 provenance（不参与判据比较），须随 C-1 判读落盘字段化随附、不得仅内存留——具体字段名待 PI 定（盘上 0 候选）。草案 D-01 拟三项一组：一是字段 h3_provenance（对象型，含 h_cap／h3／source_ref／field_path 四要素）；二是 source_ref 内嵌件名＋SHA-12＋字段路径＋数组逐字值＋held_out_count 23＋bootstrap_n 1000＋α 0.05；三是 h3_no_mix_rule 禁令串（0 与 0.1164…／0.1444…／0.1111… 混算）。落位＝C-1 判读件同层字段。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `d01_opt1`
  - `label`（逐字原文）：```三项一组·对象型（推荐）```
  - `description`（逐字原文）：```含四要素＋source_ref 内嵌全指针＋禁令串；可机器校验。```
- `id` = `d01_opt2`
  - `label`（逐字原文）：```扁平四字段（h_cap／h3／h3_source_sha12／h3_field_path）```
  - `description`（逐字原文）：```较简，但丢数组逐字值（基线取哪一读将失仲裁材料）。```
- `id` = `d01_opt3`
  - `label`（逐字原文）：```仅给对象名、不给子字段（自由文本）```
  - `description`（逐字原文）：```违『字段化随附』，0 可机器校验（草案不建议）。```

**题 4／4** — `id` = `d02`

- `header`（原文照录）：`perm 两口径互换（D-02）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
S2／S4 perm 面『排列口径（产 p 值，α=0.05）与 bootstrap 口径（产 CI 95%，n=1000）可否互换／共用一次抽样』——盘上 0 定义件、0 候选。草案 D-02 拟三条：一是两口径输出量纲不同（p 值对区间）⇒ 0 视为同一抽样之两种表述；二是若欲共用一次抽样，须明文载为新口径、0 以『沿用』含混带过；三是共用成立条件＝同 resample 序列＋α 与 CI 之边界对应另裁。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `d02_opt1`
  - `label`（逐字原文）：```不可互换·各须一次抽样（推荐）```
  - `description`（逐字原文）：```各产各的（p 值对区间）；下游引用不得混读。```
- `id` = `d02_opt2`
  - `label`（逐字原文）：```可共用一次抽样```
  - `description`（逐字原文）：```须明文新立口径（含 α 与 CI 边界之对应关系附裁）。```
- `id` = `d02_opt3`
  - `label`（逐字原文）：```维持 0 定义·永久挂账```
  - `description`（逐字原文）：```草案不建议——属『不知亦为挂账』之病面。```

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_a6f1d49c7337342253351ccd","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"d04","question":"C 线分母仅 5——上界触顶、近乎恒触发、判别力弱（v3 面为 9）。草案 D-04 拟三步：一是以 held-out 全域 26 件为母体重抽样至 n＝9（对齐 v3 面规模），逐件登记抽取路径；二是先立 kill-line K-C-DEN-1（C 之 CI 上界＜0.10 达标／≥0.10 不达标／不可构造即不明）方可跑——判死线先于实验；三是扩充读数另立新件并陈，不覆写既有读数件。请裁：","selectionMode":"single","options":[{"id":"d04_opt1","label":"三步案——n=9＋新 kill-line＋并陈（推荐）","description":"①以 held-out 全域 26 件为母体重抽样至 n=9（对齐 v3 面规模），逐件登记抽取路径；②先立 K-C-DEN-1 后方可跑；③扩充读数另立新件并陈。"},{"id":"d04_opt2","label":"维持 n=5 不动","description":"C 判别力弱永久登记为构造效度限制（非失败，是 0 判定）。"},{"id":"d04_opt3","label":"扩至其它规模","description":"数值在 Other 给出；须声明非由本轮读数反推。"},{"id":"d04_opt4","label":"改用非比例型 C 统计量","description":"须另立口径，不沿用现构造。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"C 线分母扩充（D-04）"},{"id":"d05","question":"B 点估计 9/21 与 v3 面 6/14 皆约分至 3/7——逐位同值之巧合未排除（0 断言两面等价）。草案 D-05 拟三检并施：一是约分同值检（以 held-out 全域改分母重算；如实标注『该分母下未复现』）；二是同源数据检（v3 与 S4 之件集交集核对）；三是构造差异检（仅 v3 有、S4 无之件上施测——素材不可得则如实登记『不可施』，0 以检一二冒充）。请裁：","selectionMode":"single","options":[{"id":"d05_opt1","label":"三检并施（③不可施则如实登记）（推荐）","description":"①约分同值检（改分母重算）；②同源数据检（件集交集核对）；③构造差异检（不可施则如实登记）。"},{"id":"d05_opt2","label":"仅施检一","description":"省；但 0 排除同源解释。"},{"id":"d05_opt3","label":"维持『巧合未排除』永久登记","description":"属挂账未清面，草案不建议。"},{"id":"d05_opt4","label":"写入『两面等价』口径","description":"草案明确反对——0 证据之断言。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"B 巧合排除（D-05）"},{"id":"d01","question":"h₃ 退为 provenance（不参与判据比较），须随 C-1 判读落盘字段化随附、不得仅内存留——具体字段名待 PI 定（盘上 0 候选）。草案 D-01 拟三项一组：一是字段 h3_provenance（对象型，含 h_cap／h3／source_ref／field_path 四要素）；二是 source_ref 内嵌件名＋SHA-12＋字段路径＋数组逐字值＋held_out_count 23＋bootstrap_n 1000＋α 0.05；三是 h3_no_mix_rule 禁令串（0 与 0.1164…／0.1444…／0.1111… 混算）。落位＝C-1 判读件同层字段。请裁：","selectionMode":"single","options":[{"id":"d01_opt1","label":"三项一组·对象型（推荐）","description":"含四要素＋source_ref 内嵌全指针＋禁令串；可机器校验。"},{"id":"d01_opt2","label":"扁平四字段（h_cap／h3／h3_source_sha12／h3_field_path）","description":"较简，但丢数组逐字值（基线取哪一读将失仲裁材料）。"},{"id":"d01_opt3","label":"仅给对象名、不给子字段（自由文本）","description":"违『字段化随附』，0 可机器校验（草案不建议）。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"h₃ provenance 字段名（D-01）"},{"id":"d02","question":"S2／S4 perm 面『排列口径（产 p 值，α=0.05）与 bootstrap 口径（产 CI 95%，n=1000）可否互换／共用一次抽样』——盘上 0 定义件、0 候选。草案 D-02 拟三条：一是两口径输出量纲不同（p 值对区间）⇒ 0 视为同一抽样之两种表述；二是若欲共用一次抽样，须明文载为新口径、0 以『沿用』含混带过；三是共用成立条件＝同 resample 序列＋α 与 CI 之边界对应另裁。请裁：","selectionMode":"single","options":[{"id":"d02_opt1","label":"不可互换·各须一次抽样（推荐）","description":"各产各的（p 值对区间）；下游引用不得混读。"},{"id":"d02_opt2","label":"可共用一次抽样","description":"须明文新立口径（含 α 与 CI 边界之对应关系附裁）。"},{"id":"d02_opt3","label":"维持 0 定义·永久挂账","description":"草案不建议——属『不知亦为挂账』之病面。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"perm 两口径互换（D-02）"}],"status":"pending","createdAt":1791562437016,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_02bc970c-8c71-4c99-9941-17d98c0e7dca","toolCallId":"call_00_cClJGwRSC2Nw3x6mRiT70937"},"title":"轮21 · 代立草案核准批（4/10 项：D-04 / D-05 / D-01 / D-02）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_a6f1d49c7337342253351ccd","answers":[{"stepId":"d04","selectedOptionIds":["d04_opt1"],"selectedOther":false},{"stepId":"d05","selectedOptionIds":["d05_opt1"],"selectedOther":false},{"stepId":"d01","selectedOptionIds":["d01_opt1"],"selectedOther":false},{"stepId":"d02","selectedOptionIds":["d02_opt1"],"selectedOther":false}],"submittedAt":1791562460022}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "d04", "selectedOptionIds": ["d04_opt1"], "selectedOther": false}
```

- `stepId`：`d04`
- `selectedOptionIds`（逐字）：`["d04_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d04_opt1` → `label`: ```三步案——n=9＋新 kill-line＋并陈（推荐）```
      → `description`: ```①以 held-out 全域 26 件为母体重抽样至 n=9（对齐 v3 面规模），逐件登记抽取路径；②先立 K-C-DEN-1 后方可跑；③扩充读数另立新件并陈。```

答 2／4 — 原始对象：

```json
{"stepId": "d05", "selectedOptionIds": ["d05_opt1"], "selectedOther": false}
```

- `stepId`：`d05`
- `selectedOptionIds`（逐字）：`["d05_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d05_opt1` → `label`: ```三检并施（③不可施则如实登记）（推荐）```
      → `description`: ```①约分同值检（改分母重算）；②同源数据检（件集交集核对）；③构造差异检（不可施则如实登记）。```

答 3／4 — 原始对象：

```json
{"stepId": "d01", "selectedOptionIds": ["d01_opt1"], "selectedOther": false}
```

- `stepId`：`d01`
- `selectedOptionIds`（逐字）：`["d01_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d01_opt1` → `label`: ```三项一组·对象型（推荐）```
      → `description`: ```含四要素＋source_ref 内嵌全指针＋禁令串；可机器校验。```

答 4／4 — 原始对象：

```json
{"stepId": "d02", "selectedOptionIds": ["d02_opt1"], "selectedOther": false}
```

- `stepId`：`d02`
- `selectedOptionIds`（逐字）：`["d02_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d02_opt1` → `label`: ```不可互换·各须一次抽样（推荐）```
      → `description`: ```各产各的（p 值对区间）；下游引用不得混读。```

**关键字段长度（实测）**

```text
request_json   字符数 = 3228    字节数(UTF-8) = 5274
reply_payload  字符数 = 390      字节数(UTF-8) = 390
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: d04=198; d05=190; d01=298; d02=210
selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

---

### 17 · `ask_54975ff7d6a836cad213377f` · 新增（前两批未含 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> 轮22 · T1⑧ 启用链（M-16 上位＋D-09／D-10 下位＋M-15 升格判断）

**卡级元数据（原文照录）**

```text
request_id                     = ask_54975ff7d6a836cad213377f
status（表列 questionnaire_requests.status） = answered
status（request_json 内嵌，建卡时快照）     = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = 轮22 · T1⑧ 启用链（M-16 上位＋D-09／D-10 下位＋M-15 升格判断）
presentation.allowBackNavigation = true
presentation.replaceComposer = true
presentation.showProgress = true
requester.agentName              = mavis
requester.runId                  = turn_328d7b4d-45d2-4416-aa24-64871dff4766
requester.sessionId              = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId             = call_00_jE7AjNOuIL0iwjKgC1OX0114
request_json.createdAt (epoch ms) = 1791562716640   → 2026-10-10 00:18:36.640 +0800
session_id                     = NULL
agent_name                     = NULL
msg_id                         = NULL
created_at (epoch ms)          = 1791562716640
created_at (CST 换算)          = 2026-10-10 00:18:36.640 +0800
answered_at (epoch ms)         = 1791562754834
answered_at (CST 换算)         = 2026-10-10 00:19:14.834 +0800
reply_payload.submittedAt(epoch ms) = 1791562754834   → 2026-10-10 00:19:14.834 +0800
injected_at (epoch ms)         = NULL
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／14 选项，原文照录）**

**题 1／4** — `id` = `m16`

- `header`（原文照录）：`T1⑧ 启用与否（M-16·上位裁）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧ 是否启用『真实面 N≥30』作为 r2 面之判据来源（§3.6.2 序 2）——沿 `02F44F5BF2DD` §5-1 逐字：『启用与否决定是否新增第二读法 ＝ 判据面选择』。背景：r2 之 same-caption 跨 6 cells＝36（≥30）／同温度＝12（<30）——两读法给出相反后果；启用即新增第二读法（36 侧）。注意：本项为 D-09／D-10／M-17 之共同上位裁（不启用则各下位项 0 对象）。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `m16_opt1`
  - `label`（逐字原文）：```不启用```
  - `description`（逐字原文）：```维持现登记面，不新增读法；D-09／D-10 随之下位自然 0 对象。```
- `id` = `m16_opt2`
  - `label`（逐字原文）：```启用```
  - `description`（逐字原文）：```B 侧读法新增（36≥30 侧入判据面）；D-09／D-10 两下位项随之启用。```
- `id` = `m16_opt3`
  - `label`（逐字原文）：```暂缓```
  - `description`（逐字原文）：```候更多信息（也可在 Other 写明具体条件）。```

**题 2／4** — `id` = `d09`

- `header`（原文照录）：`聚合维度（D-09·若启用）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧ 若启用之『聚合维度』（0 径定单一维度）。§3.6.2 序 3 沿 `02F44F5BF2DD` §5-2 逐字：`24DA21074CC2` §3.2 明载 0 径定。草案 D-09 拟：不设单一聚合维度，改采双列并报——以 same-caption 为判据来源列、all-pooled 为登记对照列（并列落盘、各自标注口径名），任一口径 0 单独承载判词。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `d09_opt1`
  - `label`（逐字原文）：```双列并报＋0 单列承载（推荐）```
  - `description`（逐字原文）：```两口径并列落盘、各自标注口径名，任一口径 0 单独承载判词。```
- `id` = `d09_opt2`
  - `label`（逐字原文）：```径定 same-caption 单列```
  - `description`（逐字原文）：```若其选择依据含 r2 读数，即违『0 事后调』。```
- `id` = `d09_opt3`
  - `label`（逐字原文）：```径定 all-pooled 单列```
  - `description`（逐字原文）：```同上之病。```
- `id` = `d09_opt4`
  - `label`（逐字原文）：```0 对象（M-16 未启用）```
  - `description`（逐字原文）：```随 M-16 未启用而自然无对象。```

**题 3／4** — `id` = `d10`

- `header`（原文照录）：`外推边界与硬隔离（D-10·若启用）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧ 若启用之外推边界与硬隔离——五条拟条款：①硬隔离：0 溯及 r1 面（`DFC858D3D930` 全件一字不动，『已消解 1』记载保持历史真实）；②0 阈值变动（0.85／0.05／20／10／N_min=10／N≥30 一字不动；属口径定义、非阈值调整）；③分轴不合并（⑧与 K-T1-R1-1 门禁为两独立面）；④端点面不外推（mimo／teamo、t=0.7 baseline、content_only、K-N11-N1、任何真实面）；⑤生效即锁（0 事后调、0 溯及——硬约束）。请裁：
```

`options`（逐字原文，共 3 项）：

- `id` = `d10_opt1`
  - `label`（逐字原文）：```五条全采（推荐）```
  - `description`（逐字原文）：```五条全采——含③分轴不合并（⑧与 K-T1-R1-1 门禁两独立面）与④端点面不外推。```
- `id` = `d10_opt2`
  - `label`（逐字原文）：```采①②⑤```
  - `description`（逐字原文）：```略去③④两条。```
- `id` = `d10_opt3`
  - `label`（逐字原文）：```另加第六条『溯及须另裁』例外机制```
  - `description`（逐字原文）：```草案不建议——设例外即事后调参入口敞开。```

**题 4／4** — `id` = `m15`

- `header`（原文照录）：`两项升格判断（M-15）`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
T1⑧ 复核之两项「升格」性质判断（§3.6.2 序 1）：①『更新触发条件』（由『未来任何』改为『已于 r2 具条件』）是否属径定之实质？②『须于入链前裁断』是否构成对乙档裁决之延伸干预？说明：若 PI 判任一为『是』⇒ 判断件相应部分作罢，仅余 P-1『同面处理』（该项无条件成立）。请裁：
```

`options`（逐字原文，共 4 项）：

- `id` = `m15_opt1`
  - `label`（逐字原文）：```两项皆『否』——升格存续```
  - `description`（逐字原文）：```升格建议存续（『一裁三带』升格可按判断件进）。```
- `id` = `m15_opt2`
  - `label`（逐字原文）：```①为『是』```
  - `description`（逐字原文）：```『更新触发条件』属径定之实质。```
- `id` = `m15_opt3`
  - `label`（逐字原文）：```②为『是』```
  - `description`（逐字原文）：```『须于入链前裁断』构成对乙档之延伸干预。```
- `id` = `m15_opt4`
  - `label`（逐字原文）：```两项皆『是』```
  - `description`（逐字原文）：```相应部分作罢，仅余 P-1『同面处理』（该项无条件成立）。```

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_54975ff7d6a836cad213377f","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"m16","question":"T1⑧ 是否启用『真实面 N≥30』作为 r2 面之判据来源（§3.6.2 序 2）——沿 `02F44F5BF2DD` §5-1 逐字：『启用与否决定是否新增第二读法 ＝ 判据面选择』。背景：r2 之 same-caption 跨 6 cells＝36（≥30）／同温度＝12（<30）——两读法给出相反后果；启用即新增第二读法（36 侧）。注意：本项为 D-09／D-10／M-17 之共同上位裁（不启用则各下位项 0 对象）。请裁：","selectionMode":"single","options":[{"id":"m16_opt1","label":"不启用","description":"维持现登记面，不新增读法；D-09／D-10 随之下位自然 0 对象。"},{"id":"m16_opt2","label":"启用","description":"B 侧读法新增（36≥30 侧入判据面）；D-09／D-10 两下位项随之启用。"},{"id":"m16_opt3","label":"暂缓","description":"候更多信息（也可在 Other 写明具体条件）。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"T1⑧ 启用与否（M-16·上位裁）"},{"id":"d09","question":"T1⑧ 若启用之『聚合维度』（0 径定单一维度）。§3.6.2 序 3 沿 `02F44F5BF2DD` §5-2 逐字：`24DA21074CC2` §3.2 明载 0 径定。草案 D-09 拟：不设单一聚合维度，改采双列并报——以 same-caption 为判据来源列、all-pooled 为登记对照列（并列落盘、各自标注口径名），任一口径 0 单独承载判词。请裁：","selectionMode":"single","options":[{"id":"d09_opt1","label":"双列并报＋0 单列承载（推荐）","description":"两口径并列落盘、各自标注口径名，任一口径 0 单独承载判词。"},{"id":"d09_opt2","label":"径定 same-caption 单列","description":"若其选择依据含 r2 读数，即违『0 事后调』。"},{"id":"d09_opt3","label":"径定 all-pooled 单列","description":"同上之病。"},{"id":"d09_opt4","label":"0 对象（M-16 未启用）","description":"随 M-16 未启用而自然无对象。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"聚合维度（D-09·若启用）"},{"id":"d10","question":"T1⑧ 若启用之外推边界与硬隔离——五条拟条款：①硬隔离：0 溯及 r1 面（`DFC858D3D930` 全件一字不动，『已消解 1』记载保持历史真实）；②0 阈值变动（0.85／0.05／20／10／N_min=10／N≥30 一字不动；属口径定义、非阈值调整）；③分轴不合并（⑧与 K-T1-R1-1 门禁为两独立面）；④端点面不外推（mimo／teamo、t=0.7 baseline、content_only、K-N11-N1、任何真实面）；⑤生效即锁（0 事后调、0 溯及——硬约束）。请裁：","selectionMode":"single","options":[{"id":"d10_opt1","label":"五条全采（推荐）","description":"五条全采——含③分轴不合并（⑧与 K-T1-R1-1 门禁两独立面）与④端点面不外推。"},{"id":"d10_opt2","label":"采①②⑤","description":"略去③④两条。"},{"id":"d10_opt3","label":"另加第六条『溯及须另裁』例外机制","description":"草案不建议——设例外即事后调参入口敞开。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"外推边界与硬隔离（D-10·若启用）"},{"id":"m15","question":"T1⑧ 复核之两项「升格」性质判断（§3.6.2 序 1）：①『更新触发条件』（由『未来任何』改为『已于 r2 具条件』）是否属径定之实质？②『须于入链前裁断』是否构成对乙档裁决之延伸干预？说明：若 PI 判任一为『是』⇒ 判断件相应部分作罢，仅余 P-1『同面处理』（该项无条件成立）。请裁：","selectionMode":"single","options":[{"id":"m15_opt1","label":"两项皆『否』——升格存续","description":"升格建议存续（『一裁三带』升格可按判断件进）。"},{"id":"m15_opt2","label":"①为『是』","description":"『更新触发条件』属径定之实质。"},{"id":"m15_opt3","label":"②为『是』","description":"『须于入链前裁断』构成对乙档之延伸干预。"},{"id":"m15_opt4","label":"两项皆『是』","description":"相应部分作罢，仅余 P-1『同面处理』（该项无条件成立）。"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"两项升格判断（M-15）"}],"status":"pending","createdAt":1791562716640,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_328d7b4d-45d2-4416-aa24-64871dff4766","toolCallId":"call_00_jE7AjNOuIL0iwjKgC1OX0114"},"title":"轮22 · T1⑧ 启用链（M-16 上位＋D-09／D-10 下位＋M-15 升格判断）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_54975ff7d6a836cad213377f","answers":[{"stepId":"m16","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"},{"stepId":"d09","selectedOptionIds":["d09_opt1"],"selectedOther":false},{"stepId":"d10","selectedOptionIds":["d10_opt1"],"selectedOther":false},{"stepId":"m15","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"}],"submittedAt":1791562754834}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — 原始对象：

```json
{"stepId": "m16", "selectedOptionIds": [], "selectedOther": true, "otherText": "另议"}
```

- `stepId`：`m16`
- `selectedOptionIds`（逐字）：`[]`
- `selectedOther`（逐字）：`true`
- `otherText`：

```text
另议
```

答 2／4 — 原始对象：

```json
{"stepId": "d09", "selectedOptionIds": ["d09_opt1"], "selectedOther": false}
```

- `stepId`：`d09`
- `selectedOptionIds`（逐字）：`["d09_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d09_opt1` → `label`: ```双列并报＋0 单列承载（推荐）```
      → `description`: ```两口径并列落盘、各自标注口径名，任一口径 0 单独承载判词。```

答 3／4 — 原始对象：

```json
{"stepId": "d10", "selectedOptionIds": ["d10_opt1"], "selectedOther": false}
```

- `stepId`：`d10`
- `selectedOptionIds`（逐字）：`["d10_opt1"]`
- `selectedOther`（逐字）：`false`
- `otherText`：（无此键）

  - 所选 `option id` → 其 `label`／`description` **原文照录**（机械索引，无判读）：
    - `d10_opt1` → `label`: ```五条全采（推荐）```
      → `description`: ```五条全采——含③分轴不合并（⑧与 K-T1-R1-1 门禁两独立面）与④端点面不外推。```

答 4／4 — 原始对象：

```json
{"stepId": "m15", "selectedOptionIds": [], "selectedOther": true, "otherText": "另议"}
```

- `stepId`：`m15`
- `selectedOptionIds`（逐字）：`[]`
- `selectedOther`（逐字）：`true`
- `otherText`：

```text
另议
```

**关键字段长度（实测）**

```text
request_json   字符数 = 2994    字节数(UTF-8) = 4796
reply_payload  字符数 = 402      字节数(UTF-8) = 410
steps 步数 = 4 ／ options 总数 = 14 ／ answers 条数 = 4
question 字符数（逐 step）: m16=219; d09=187; d10=252; m15=147
selectedOther=true 条数 = 2 ／ 含 otherText 键条数 = 2 ／ otherText 字符数合计 = 4
```

---

## 2 · 与前两批登记件逐件对账（按 `request_id`）

**前两批已含者（本件 0 重复转录）**：第一批 34 件 ＋ 第二批 5 件 ＝ **39** 件；其原文见对应登记件，本件不重录。

**本件转录者（本批 17 件）**：

| 本件序 | request_id | 批次处置 | 前批序号 | 卡题（`title` 逐字） | status（表列） | created_at (CST) | answered_at (CST) |
|---|---|---|---|---|---|---|---|
| 1 | `ask_a750c05e5a2a31d0189898b4` | **本批转录（本件第 1 件）** | —（前两批未含） | S4 取法复核＋T1 残余＋KD P-2（四题） | `answered` | 2026-10-09 21:46:30.805 +0800 | 2026-10-09 21:48:32.851 +0800 |
| 2 | `ask_6455cd9f15bf7dc12ae673d9` | **本批转录（本件第 2 件）** | —（前两批未含） | 轮7·补送（T1 放行＋KD P-3＋门禁方向＋RPQ 边界） | `answered` | 2026-10-09 22:06:24.554 +0800 | 2026-10-09 22:09:49.370 +0800 |
| 3 | `ask_e98a16382e277b4918bf9853` | **本批转录（本件第 3 件）** | —（前两批未含） | 配对口径复核＋KD VK 三项（补送） | `answered` | 2026-10-09 22:17:32.496 +0800 | 2026-10-09 22:21:16.231 +0800 |
| 4 | `ask_3f9c696f405cd7a384861048` | **本批转录（本件第 4 件）** | —（前两批未含） | R_pair 候呈三题（字面/歧义/勘误） | `answered` | 2026-10-09 22:24:42.677 +0800 | 2026-10-09 22:25:19.115 +0800 |
| 5 | `ask_98891be57dbc7ffaa2cb6935` | **本批转录（本件第 5 件）** | —（前两批未含） | 门禁核准＋T1 遗留＋RPQ 口径（四题） | `answered` | 2026-10-09 22:28:23.611 +0800 | 2026-10-09 22:28:52.763 +0800 |
| 6 | `ask_7afd6a8e4721444e9899a761` | **本批转录（本件第 6 件）** | —（前两批未含） | V3-05 决议＋EXP 择认（四题） | `answered` | 2026-10-09 22:35:21.641 +0800 | 2026-10-09 22:37:24.743 +0800 |
| 7 | `ask_524267a93d323e0cf9db5b96` | **本批转录（本件第 7 件）** | —（前两批未含） | RPQ 收尾＋T1 ⑧（三题） | `answered` | 2026-10-09 22:42:03.876 +0800 | 2026-10-09 22:43:43.456 +0800 |
| 8 | `ask_3a67d55dc36ba9660d788266` | **本批转录（本件第 8 件）** | —（前两批未含） | R_pair 三项复核（口径/选线/字面） | `answered` | 2026-10-09 22:48:56.798 +0800 | 2026-10-09 22:50:31.025 +0800 |
| 9 | `ask_f67e504b3fb68eb81c173270` | **本批转录（本件第 9 件）** | —（前两批未含） | S4 候呈＋VK 待核（三题） | `answered` | 2026-10-09 22:53:43.244 +0800 | 2026-10-09 22:55:12.887 +0800 |
| 10 | `ask_efa1af545065d7de7f9094c1` | **本批转录（本件第 10 件）** | —（前两批未含） | S4 五线两项＋V3-05 H 两项（四题） | `answered` | 2026-10-09 23:02:05.235 +0800 | 2026-10-09 23:02:56.072 +0800 |
| 11 | `ask_13e341cca46a973ec61c9f0f` | **本批转录（本件第 11 件）** | —（前两批未含） | V3-05 AB 处置＋Q-3 勘误＋S4 149 面（三题） | `answered` | 2026-10-09 23:11:08.698 +0800 | 2026-10-09 23:11:54.974 +0800 |
| 12 | `ask_7a159c56037e3c8bb7239d6a` | **本批转录（本件第 12 件）** | —（前两批未含） | KD 指引生效＋S4 两重判复核（两题） | `answered` | 2026-10-09 23:25:26.390 +0800 | 2026-10-09 23:26:02.420 +0800 |
| 13 | `ask_995f776b589725afdd44ea6d` | **本批转录（本件第 13 件）** | —（前两批未含） | 收口批①：B/C 复核＋β 三项（四题） | `answered` | 2026-10-09 23:42:10.658 +0800 | 2026-10-09 23:42:40.612 +0800 |
| 14 | `ask_4ad2d308aee5ec669a3a438d` | **本批转录（本件第 14 件）** | —（前两批未含） | 收口批②：报值口径＋词表两项＋T1⑧（四题） | `answered` | 2026-10-09 23:43:43.175 +0800 | 2026-10-09 23:44:10.081 +0800 |
| 15 | `ask_4bf0d908084b3646a40ad4d6` | **本批转录（本件第 15 件）** | —（前两批未含） | 轮20 · 代立草案核准批（4/10 项：D-07 / D-08 / D-03 / D-06） | `answered` | 2026-10-10 00:03:48.100 +0800 | 2026-10-10 00:07:10.140 +0800 |
| 16 | `ask_a6f1d49c7337342253351ccd` | **本批转录（本件第 16 件）** | —（前两批未含） | 轮21 · 代立草案核准批（4/10 项：D-04 / D-05 / D-01 / D-02） | `answered` | 2026-10-10 00:13:57.016 +0800 | 2026-10-10 00:14:20.022 +0800 |
| 17 | `ask_54975ff7d6a836cad213377f` | **本批转录（本件第 17 件）** | —（前两批未含） | 轮22 · T1⑧ 启用链（M-16 上位＋D-09／D-10 下位＋M-15 升格判断） | `answered` | 2026-10-10 00:18:36.640 +0800 | 2026-10-10 00:19:14.834 +0800 |

**第一批窗口漏录复核（沿第二批同款复核）**：以第一批窗口下界 `1791388800000` 重扫全表，本轮实测该窗口 `39` 件，第一批实录 `34` ＋ 第二批实录 `5` ＝ `39`（**0 漏录**）。

**第一批 `request_id` 计数依据（如实记录，⛔ 0 判读）**：第一批登记件内以 `### NN · \`ask_…\`` 标题形式收录 `34` 个；第二批同款标题节收录 `5` 个；二者合计 `39` 个，**0 重复**。

## 3 · 枚举完整性对账

```text
本批应录 N 件（本批窗口 created_at>=2026-10-09 17:00:00 +0800 内，前两批未含者）
  ＝ 本窗口记录总数        : 27
  － 前两批已含（重叠区）  : 10
  － 第二批转录但读得时待答者（已含·0 重录·答文另见 §4）: 0
  ⇒ 本批应录全集（去重）  : 17
实录 N 件（本件已逐字转录的卡节数）: 17
miss = 应录 − 实录 : 0
重复转录数（前两批已含者被本件重录）: 0
```

**miss 明细：0（无遗漏）。** 逐项核验：

- 本窗口 27 件逐一 `SELECT` 实查，27/27 命中。
- 其中前两批未含者 17 件已在本件 §1 **逐字全量收录**（卡题＋题面全文字面＋答文全文＋关键字段长度）。
- 前两批已含者 10 件**仅列对账行**（§2），⛔ 0 重复转录其题面／答文。
- 重复 id：0（`request_id` 为表主键，全表唯一）。

**status 与答文完整性（⛔ 0 将待答冒充已答）**

```text
本窗口 status != 'answered' 的记录数 : 0
本窗口 answered_at 为 NULL 的记录数   : 0
本窗口 reply_payload 为 NULL/空的记录数: 0
```

- 本窗口 17 件**全部** `status = answered`、`answered_at` 非空、`reply_payload` 非空，已全量转录答文。
- 全表 `superseded` 记录 1 条（`ask_05992739fd9e46f8e8acd23d`，`created_at` = `2026-09-30 10:38:44.260 +0800`），**早于**本窗口下界，故不属本轮应录范围，**未转录**（仅于 §0bis 登记）。

## 4 · 第二批「读得时待答」卡之答文追补（**口径漂移如实登记 · 0 冒充**）

第二批登记件 §1 第 5 件 `ask_6db74cbbb4c70cf8c0c6cc1e`（`T1 温度轴·新实验决议四题`）于第二批读得时 `status = pending`、`answered_at` 为 `NULL`、`reply_payload` 为 `NULL`，该件据实以「元数据 ＋ 题面全文字面照录」入册并明载「⏔ 0 冒充已答」。

**本轮实测（`created_at` 未变、仅状态面变动）**：该卡现为 `status = answered`、`answered_at = 1791553014333`（`2026-10-09 21:36:54.333 +0800`）、`reply_payload` 非空。

**处置口径（0 回改第二批原件）**：⛔ 0 编辑第二批登记件；⛔ 0 重录其题面（题面已在第二批 §1 第 5 件在册）。本节**仅追补该卡之新增可得之答文**，并如实标注其为**答文追补**（非新卡）。

```text
request_id                       = ask_6db74cbbb4c70cf8c0c6cc1e
status（表列 · 本轮实测）        = answered
第二批登记件读得时 status         = pending   （口径已随时间变动）
created_at (epoch ms)            = 1791552214280
created_at (CST 换算)            = 2026-10-09 21:23:34.280 +0800
answered_at (epoch ms)           = 1791553014333
answered_at (CST 换算)           = 2026-10-09 21:36:54.333 +0800
第二批读得时 answered_at         = NULL      （该面当时不可得）
```

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_6db74cbbb4c70cf8c0c6cc1e","answers":[{"stepId":"t1e_path","selectedOptionIds":["t1e_path_opt1"],"selectedOther":false},{"stepId":"t1e_prereg","selectedOptionIds":["t1e_prereg_opt1"],"selectedOther":false},{"stepId":"t1e_mde","selectedOptionIds":["t1e_mde_opt1"],"selectedOther":false},{"stepId":"t1e_p1","selectedOptionIds":["t1e_p1_opt1"],"selectedOther":false}],"submittedAt":1791553014333}
```

**答文逐字（逐条展开 · 题面不重录 · 机械索引无判读）**

| 答序 | `stepId` | `selectedOptionIds`（逐字） | `selectedOther`（逐字） | `otherText` |
|---|---|---|---|---|
| 1 | `t1e_path` | `["t1e_path_opt1"]` | `false` | （无此键） |
| 2 | `t1e_prereg` | `["t1e_prereg_opt1"]` | `false` | （无此键） |
| 3 | `t1e_mde` | `["t1e_mde_opt1"]` | `false` | （无此键） |
| 4 | `t1e_p1` | `["t1e_p1_opt1"]` | `false` | （无此键） |

**关键字段长度（实测）**

```text
reply_payload  字符数 = 428      字节数(UTF-8) = 428
answers 条数 = 4 ／ selectedOther=true 条数 = 0 ／ 含 otherText 键条数 = 0 ／ otherText 字符数合计 = 0
```

⛔ **0 增设条款、0 判读其答文之效力**——该答文之裁断效力仍以其原登记件／生效件为准。

## 5 · 早于首批窗口之未入册存量（第①段 · 逐 id 全量登记 · ⛔ 0 逐字转录）

**为何 0 逐字转录（口径依据 · 非回避）**：

- 第一批登记件 §1 明载范围口径：「本轮应录＝**必录清单 9 件 ＋ 窗口内全部问卷记录**……故全量清单 34 件即为应录全集」；
- 第二批登记件 §2 明载：「上列二 id 均经本轮实测**早于本批窗口下界**，故**不属本轮应录面**」——即**窗口外存量既已确立为不属应录面之体例**；
- 本件沿该体例界定「追补」对象＝前两批截止后新建之卡；**第①段存量之逐字回填属另立事项**（§5.3 候呈），**本件 0 代为决定**。

**规模与成本实测（供另派决策之依据 · 非裁量）**：

```text
第①段件数                                          : 334
  其中 status='answered'                           : 333
  其中 status='superseded'                         : 1
created_at 跨度                                     : 2026-09-01 11:22:59.763 +0800 ～ 2026-10-02 01:04:00.164 +0800
全段 request_json + reply_payload 原始字节合计     : 1151667 bytes（≈ 1.1 MB · 仅原始载荷，不含逐字转录之展开体例开销）
```

⛔ **0 掩饰**：上列 334 件**确实存在于运行时库且 `status='answered'`**，仅**未逐字落册**。本件**不以「不属应录面」之名行隐瞒之实**——逐 id 如实列于 §5.2。

### 5.1 处置声明

| 项 | 处置 |
|---|---|
| 存在性 | ✅ 已实测确认（334 件，全表 `questionnaire_requests` 可查） |
| 逐 id 登记 | ✅ 已列（§5.2） |
| 逐字转录 | ⏸ **0 逐字转录**——须另立「存量回填」事项后另行处置 |
| 是否遗漏 | **⛔ 0 遗漏**：0 静默丢弃、0 静默改述 |
| 是否代裁 | **⛔ 0 代裁**：是否回填、于何时回填，属 PI／parent 出口 |

### 5.2 逐 id 全量清单（`request_id` · `created_at` CST · `status` · 卡题逐字）

| # | request_id | status | created_at (CST) | 卡题（`title` 逐字） |
|---:|---|---|---|---|
| 1 | `ask_dff9fcf1bc8caf29f127999c` | `answered` | 2026-09-01 11:22:59.763 +0800 | P-D V0 试刀剩余步骤如何处理？ |
| 2 | `ask_6358226c7291cf28c5fe6a00` | `answered` | 2026-09-02 14:00:24.903 +0800 | NULL |
| 3 | `ask_5bb0cc55b3c59a85869ac665` | `answered` | 2026-09-02 14:03:38.948 +0800 | NULL |
| 4 | `ask_8b055a5d403516bb1647673b` | `answered` | 2026-09-02 14:04:38.502 +0800 | NULL |
| 5 | `ask_5d23bb986530d52b5cb5e4b4` | `answered` | 2026-09-02 14:05:15.653 +0800 | NULL |
| 6 | `ask_4236bc2f67964b5db7c038ce` | `answered` | 2026-09-02 14:06:29.122 +0800 | NULL |
| 7 | `ask_992541e44cab77d2a74174df` | `answered` | 2026-09-02 14:11:18.276 +0800 | NULL |
| 8 | `ask_749da14b4f590090970e400f` | `answered` | 2026-09-03 12:23:06.769 +0800 | NULL |
| 9 | `ask_31d2b0b38ee560484100719d` | `answered` | 2026-09-03 12:24:27.668 +0800 | NULL |
| 10 | `ask_74335f84c5016fc71577ee6e` | `answered` | 2026-09-03 12:26:43.745 +0800 | NULL |
| 11 | `ask_76283ed9d86eb86f55137bb9` | `answered` | 2026-09-03 12:29:47.515 +0800 | NULL |
| 12 | `ask_19243c61912236fd5e508e3b` | `answered` | 2026-09-03 12:34:37.585 +0800 | NULL |
| 13 | `ask_71dcaeaf8d8750fd67946204` | `answered` | 2026-09-03 12:39:54.959 +0800 | NULL |
| 14 | `ask_8ab3dd96b4cf6ba0938952cc` | `answered` | 2026-09-03 12:55:50.877 +0800 | NULL |
| 15 | `ask_0b3b31b50a10a1c21d827125` | `answered` | 2026-09-03 19:00:47.837 +0800 | NULL |
| 16 | `ask_6d5894479c6156238500b785` | `answered` | 2026-09-03 21:24:20.077 +0800 | Review implementation plan |
| 17 | `ask_09b79f07adab1724208917eb` | `answered` | 2026-09-04 09:32:24.809 +0800 | 根因已坐实,下一步? |
| 18 | `ask_c92afc45ff74178f5c238539` | `answered` | 2026-09-04 09:43:15.885 +0800 | 日志改完,下一步? |
| 19 | `ask_9039e5f75c8712fef67b00e4` | `answered` | 2026-09-04 11:02:20.722 +0800 | PixiJS 从哪起步? |
| 20 | `ask_177bd0a60a2b38887c6b0852` | `answered` | 2026-09-04 11:14:23.260 +0800 | 重制哪个？ |
| 21 | `ask_76fc17c338db3a5bf3c4bf69` | `answered` | 2026-09-04 12:51:02.845 +0800 | v3 PixiJS APK 就绪,下一步? |
| 22 | `ask_5659fd05d58a2a3e5fdf086a` | `answered` | 2026-09-07 16:40:43.723 +0800 | NULL |
| 23 | `ask_158bc5e0a251de8514320362` | `answered` | 2026-09-07 17:10:20.798 +0800 | 历史整理方案选择 |
| 24 | `ask_b78a588b94f7426fb883917c` | `answered` | 2026-09-07 17:15:59.796 +0800 | V8 Phase B 启动决策 |
| 25 | `ask_e8934a58c03adf45af09a404` | `answered` | 2026-09-08 15:36:42.811 +0800 | Data availability 位置选择 |
| 26 | `ask_d2782506eb37009528852336` | `answered` | 2026-09-08 15:42:04.902 +0800 | Artifact availability 位置 |
| 27 | `ask_3c7b1a3b4ed223b48b019080` | `answered` | 2026-09-08 15:48:11.150 +0800 | AI 声明位置选择 |
| 28 | `ask_4abf7b653c4c3326531c5a31` | `answered` | 2026-09-08 17:03:21.012 +0800 | 重打包精简版 tar.gz？ |
| 29 | `ask_959893c8b0c71e53d2b5154c` | `answered` | 2026-09-09 13:41:11.346 +0800 | V3X D5 进展报告 + 后续节奏 |
| 30 | `ask_0dcd65beae34199fd917f515` | `answered` | 2026-09-11 10:50:08.442 +0800 | 读完了,下一步? |
| 31 | `ask_7719a7503aa4e6e6833bf22c` | `answered` | 2026-09-11 16:20:55.492 +0800 | 遣散范围 |
| 32 | `ask_e64886f6f84ae29b54de1ce9` | `answered` | 2026-09-15 13:43:08.450 +0800 | Review implementation plan |
| 33 | `ask_55992c560467e359a0bf97a0` | `answered` | 2026-09-15 14:11:09.455 +0800 | D_fix2 PARTIAL_PASS 拍板 |
| 34 | `ask_a5284e1b3a07ddba6676867b` | `answered` | 2026-09-16 13:01:35.461 +0800 | Review implementation plan |
| 35 | `ask_6e7afaa1f7149eec5788d293` | `answered` | 2026-09-16 23:14:59.759 +0800 | 拍板问卷 |
| 36 | `ask_b13039f58d22ffbe599b9eca` | `answered` | 2026-09-17 00:14:44.750 +0800 | NULL |
| 37 | `ask_b481516fd7489b9ae85c0028` | `answered` | 2026-09-17 00:16:46.613 +0800 | NULL |
| 38 | `ask_25fcc02ec3a75baffdf2f94c` | `answered` | 2026-09-17 09:56:20.736 +0800 | NULL |
| 39 | `ask_173f34e583ad15f057616904` | `answered` | 2026-09-17 16:08:22.604 +0800 | NULL |
| 40 | `ask_604d637640344a4b5f0e0722` | `answered` | 2026-09-17 16:11:59.303 +0800 | NULL |
| 41 | `ask_4240f9c7b9a419ba0def85ae` | `answered` | 2026-09-17 16:17:42.525 +0800 | NULL |
| 42 | `ask_102f41ba4c1f797a91d042af` | `answered` | 2026-09-17 22:42:41.947 +0800 | NULL |
| 43 | `ask_545cb28b19c179a26b54f316` | `answered` | 2026-09-20 13:29:31.610 +0800 | NULL |
| 44 | `ask_25e22176a42347afe7348992` | `answered` | 2026-09-20 15:38:04.944 +0800 | NULL |
| 45 | `ask_4cf30b9a6de2bfcb783be3d8` | `answered` | 2026-09-21 15:10:35.519 +0800 | V4 整合稿 / 问卷 待拍板项（4 项） |
| 46 | `ask_e81afcb8b8d23dead103796b` | `answered` | 2026-09-21 15:22:51.443 +0800 | V4 整合稿第二轮 · 剩余 2 项待拍板 |
| 47 | `ask_80d090b6975fa9430d247e71` | `answered` | 2026-09-21 17:10:35.291 +0800 | NULL |
| 48 | `ask_3069f0d076414b139131ecb2` | `answered` | 2026-09-21 18:27:08.314 +0800 | NULL |
| 49 | `ask_4caaed46acb4322f039a2903` | `answered` | 2026-09-22 09:51:55.468 +0800 | NULL |
| 50 | `ask_bd9f4d0b940e8a8cfd69c4c6` | `answered` | 2026-09-22 09:59:26.139 +0800 | V4 问卷作答 · 组 D 第一批（4 题；不定/暂不裁定/自定义路径请用 Other 填写） |
| 51 | `ask_193da82dd431bd4c180cf250` | `answered` | 2026-09-22 10:42:50.020 +0800 | NULL |
| 52 | `ask_399793e0607d727285e3c88a` | `answered` | 2026-09-22 11:15:57.811 +0800 | V4 组 D 收尾批（2 题）：§4.6 三套术语 + §2.9.a addendum 761 |
| 53 | `ask_f8837a5b3c168ef3d6e8c18a` | `answered` | 2026-09-22 11:47:56.944 +0800 | V4 问卷 v1.1 · 组 A 首批 4 题（§4.6 追问 + §1.1.1–§1.1.3） |
| 54 | `ask_e938cb2ef840f540ca5c9a68` | `answered` | 2026-09-22 13:45:44.820 +0800 | V4 问卷 v1.1 · 组 A 批 2（3 题：§1.1.4 / §1.1.5 / §1.1.7） |
| 55 | `ask_549dc488523e6f3b3b0842a7` | `answered` | 2026-09-22 13:58:38.013 +0800 | V4 问卷 v1.1 · 批 3（§1.1.6）收法拍板 |
| 56 | `ask_c011e0a587bdef603426cf4c` | `answered` | 2026-09-22 14:03:42.863 +0800 | V4 问卷 v1.1 · 批 3 R1/10（§1.1.6 种子生产性 · S-01–S-04 · Dimension 1） |
| 57 | `ask_a1eec04a2c64280da45c9cc4` | `answered` | 2026-09-22 14:27:11.450 +0800 | NULL |
| 58 | `ask_f0ae3cf32f0bc8c83a1a8870` | `answered` | 2026-09-22 14:38:02.462 +0800 | NULL |
| 59 | `ask_5b15ae2e55eb7c84f405f1d4` | `answered` | 2026-09-22 14:57:12.681 +0800 | NULL |
| 60 | `ask_ecd9aa4264fba3e90ce9f1f8` | `answered` | 2026-09-22 15:10:02.991 +0800 | NULL |
| 61 | `ask_8d358fbd6bf16f3c06e5389b` | `answered` | 2026-09-22 15:17:56.445 +0800 | NULL |
| 62 | `ask_ce27618f5b56dd102c5b8f72` | `answered` | 2026-09-22 15:29:51.370 +0800 | NULL |
| 63 | `ask_289d8f39de0f5c98f6439ae7` | `answered` | 2026-09-22 15:34:09.403 +0800 | NULL |
| 64 | `ask_1fe637a6cd3d83f0805572f7` | `answered` | 2026-09-22 15:48:12.239 +0800 | NULL |
| 65 | `ask_cb79050aa39a368890583212` | `answered` | 2026-09-22 16:09:17.106 +0800 | NULL |
| 66 | `ask_6e9e00999a5baaa858ebfaef` | `answered` | 2026-09-22 16:12:08.224 +0800 | NULL |
| 67 | `ask_eef3408f2c709638993da79a` | `answered` | 2026-09-22 16:14:02.322 +0800 | NULL |
| 68 | `ask_79d3565003c731b358adbb4c` | `answered` | 2026-09-22 16:16:15.412 +0800 | NULL |
| 69 | `ask_e9ad9dddbb20cbd53f2d96bf` | `answered` | 2026-09-22 16:23:14.989 +0800 | NULL |
| 70 | `ask_4e6dbcd296637dfdfc3809ed` | `answered` | 2026-09-22 16:30:39.315 +0800 | NULL |
| 71 | `ask_6edb65315059347a916a44ea` | `answered` | 2026-09-22 16:38:11.547 +0800 | NULL |
| 72 | `ask_4e7f5a1dab009cdabd8c71e9` | `answered` | 2026-09-22 16:58:20.143 +0800 | Review implementation plan |
| 73 | `ask_07db793218ff72c7149ee558` | `answered` | 2026-09-22 16:59:58.719 +0800 | NULL |
| 74 | `ask_c3130abe93316b5c76e1ba4a` | `answered` | 2026-09-22 17:20:54.498 +0800 | NULL |
| 75 | `ask_35b24d8fdb5a88505fb1d349` | `answered` | 2026-09-22 17:37:16.350 +0800 | NULL |
| 76 | `ask_3ca76bc4958574f762d506cf` | `answered` | 2026-09-22 17:51:09.621 +0800 | NULL |
| 77 | `ask_e5369878e8f7a36df3776c84` | `answered` | 2026-09-22 17:54:23.783 +0800 | NULL |
| 78 | `ask_d79953cb9b94fab70bcc9dee` | `answered` | 2026-09-22 17:59:33.168 +0800 | NULL |
| 79 | `ask_b4840febdd312d096d18a3f2` | `answered` | 2026-09-22 18:02:31.236 +0800 | NULL |
| 80 | `ask_4af3d5c30f3bb4dccc54d6ac` | `answered` | 2026-09-23 10:07:30.232 +0800 | NULL |
| 81 | `ask_7c34417657df33180f0c4806` | `answered` | 2026-09-23 10:23:06.997 +0800 | NULL |
| 82 | `ask_cf4e72cc4d1db4ec4c62ea55` | `answered` | 2026-09-23 10:44:19.971 +0800 | NULL |
| 83 | `ask_bf3b0f4de8859df14067d5bf` | `answered` | 2026-09-23 10:54:35.311 +0800 | NULL |
| 84 | `ask_6e615110f1494c576534dd8a` | `answered` | 2026-09-23 11:17:07.349 +0800 | NULL |
| 85 | `ask_8b344bce4c0de2156cda85fd` | `answered` | 2026-09-23 11:26:03.510 +0800 | NULL |
| 86 | `ask_69fd25197665bc9ff353ed86` | `answered` | 2026-09-23 11:42:07.798 +0800 | NULL |
| 87 | `ask_fb3a9318e26d49aff2ca49ed` | `answered` | 2026-09-23 12:40:21.803 +0800 | NULL |
| 88 | `ask_eb72a49108c637b47b94ce75` | `answered` | 2026-09-23 12:50:16.673 +0800 | NULL |
| 89 | `ask_f9c0b6e67a7b457af5c324cc` | `answered` | 2026-09-23 13:07:24.740 +0800 | Review implementation plan |
| 90 | `ask_3c79ce9a704bfd0a2c9c6660` | `answered` | 2026-09-23 14:00:07.957 +0800 | V3/V4 补实验待拍板项（4 题，缺件翻案后） |
| 91 | `ask_3ee5edf74be2d6ef53fbc4b4` | `answered` | 2026-09-23 14:42:43.947 +0800 | V3/V4 补实验拍板项（补实验收割后，4 题） |
| 92 | `ask_559be3e5c562961f0a51ec97` | `answered` | 2026-09-23 15:13:45.736 +0800 | 挂账清点 · 余 4 项拍板（勘误处置/补实验深度/V3 退化修复/P-A 标注） |
| 93 | `ask_fc39c0f020834291496fcd88` | `answered` | 2026-09-23 15:30:22.342 +0800 | 穷尽清点 · 尾批 3 项拍板（R11 口径/N 档遗留/P-A2 冲突） |
| 94 | `ask_7844adffe9c7d56b73a8d2ca` | `answered` | 2026-09-23 15:40:25.573 +0800 | 补充拍板 2 题（N-29 重做 / probe URL 更新） |
| 95 | `ask_aa8626c2d2d6cf9f2026cc3e` | `answered` | 2026-09-23 16:35:47.056 +0800 | N-22/N-19 预登记复核（生效拍板 + 4 项决定项） |
| 96 | `ask_1a7aaa88fbda0233b5c8262a` | `answered` | 2026-09-23 17:20:17.398 +0800 | 任务 B 收口 · 尾批 3 项拍板（v2 口径 / N-22s margin / scratch） |
| 97 | `ask_211b58032bf56a2adb8e06b2` | `answered` | 2026-09-23 17:44:41.511 +0800 | 特制蒸馏问卷 · 第 1 波（思维链采集，推理必采） |
| 98 | `ask_d74e45fb825f9b37be00ddc4` | `answered` | 2026-09-23 18:01:53.656 +0800 | 收工前清点 · 2 项拍板（v2.2 复核 / 明日补测范围） |
| 99 | `ask_116c56eb866724102b47e794` | `answered` | 2026-09-23 18:03:17.803 +0800 | 加派补测内容（Q2 b-more 补充） |
| 100 | `ask_702b66e42656ca7bf1386575` | `answered` | 2026-09-24 10:27:34.824 +0800 | NULL |
| 101 | `ask_bcd961f9373c5b1ac39d85db` | `answered` | 2026-09-24 10:30:46.453 +0800 | 大拍板轮第 1 批/4：E-27 定稿阻塞项（归类口径 4 问） |
| 102 | `ask_4de06d953f657dd9c767bd25` | `answered` | 2026-09-24 10:34:23.718 +0800 | 大拍板轮第 2 批/4：动作类 4 问 |
| 103 | `ask_053da3ada6160c9ac7ae985b` | `answered` | 2026-09-24 10:37:42.990 +0800 | 大拍板轮第 3 批/4：路径类 4 问 |
| 104 | `ask_d394778f3a291d5699285111` | `answered` | 2026-09-24 10:39:33.193 +0800 | 大拍板轮第 4 批/4：收尾 4 问 |
| 105 | `ask_76d33b7b85257fcf3f3d5f71` | `answered` | 2026-09-24 10:53:38.505 +0800 | 噪声收尾 1 问：其他 `_` 前缀族扩展盘点？ |
| 106 | `ask_c0b37684f7c9696c95275796` | `answered` | 2026-09-24 11:04:48.989 +0800 | 预登记 v0.2 复核生效（8 线执行闸门） |
| 107 | `ask_b15a39edc998bdb65e86b36d` | `answered` | 2026-09-24 11:26:36.341 +0800 | 假 pass 处置：A2 5 条改标 + E-28 勘误 |
| 108 | `ask_f0e75ca4a1b9653491cc4701` | `answered` | 2026-09-24 11:32:53.864 +0800 | L9 生效闸门 + D-2 口径（A2 重跑开闸） |
| 109 | `ask_b7bb6076bd4c0a6aa787845f` | `answered` | 2026-09-24 12:59:42.053 +0800 | 8 线收口拍板（第 1 批/2）：4 项方向决策 |
| 110 | `ask_b172e4d64edb83c25e00aab7` | `answered` | 2026-09-24 13:03:12.234 +0800 | 8 线收口拍板（第 2 批/2）：收尾 2 问 |
| 111 | `ask_ca36f095948d0814b008d0f5` | `answered` | 2026-09-24 13:10:09.915 +0800 | L10 生效闸门（D-Rényi 重跑开闸） |
| 112 | `ask_c35a13553babada5c8050ec2` | `answered` | 2026-09-24 13:32:22.296 +0800 | 任务 B 思维采集 1/10（判据优先序 1-4） |
| 113 | `ask_c115f75244c94c9a66073dcd` | `answered` | 2026-09-24 13:46:59.320 +0800 | 任务 B 思维采集 2/10（判据优先序 5-8） |
| 114 | `ask_14f610b9a7726f18bd213058` | `answered` | 2026-09-24 13:55:33.028 +0800 | 任务 B 思维采集 3/10（权衡模式 9-12） |
| 115 | `ask_2adc78b391c34ce8720dc81c` | `answered` | 2026-09-24 14:09:26.063 +0800 | 任务 B 思维采集 4/10（13-16） |
| 116 | `ask_cd1f936071e6615c62aeeca0` | `answered` | 2026-09-24 14:16:27.171 +0800 | 任务 B 思维采集 5/10（分界标准 17-20） |
| 117 | `ask_50752b5317d1a101214719af` | `answered` | 2026-09-24 14:31:48.847 +0800 | 任务 B 思维采集 6/10（21-24） |
| 118 | `ask_a34e7f5d2659edaeaf026734` | `answered` | 2026-09-24 14:47:27.064 +0800 | 任务 B 思维采集 7/10（25-28） |
| 119 | `ask_05992739fd9e46f8e8acd23d` | `superseded` | 2026-09-24 14:52:04.260 +0800 | 任务 B 思维采集 8/10（29-32） |
| 120 | `ask_7fcd4f7f2ea58c0b9ab4e561` | `answered` | 2026-09-24 15:00:41.596 +0800 | Token Plan 用量耗尽：资源决策 |
| 121 | `ask_e35671e9224af4eed0e89f52` | `answered` | 2026-09-24 15:05:20.344 +0800 | 任务 B 思维采集 8/10 重发（29-32） |
| 122 | `ask_bd1eb66b0cc0d054265da828` | `answered` | 2026-09-24 15:12:48.249 +0800 | 任务 B 思维采集 9/10（33-36） |
| 123 | `ask_9caea85b7cd033d59dbc7851` | `answered` | 2026-09-24 15:18:28.107 +0800 | 任务 B 思维采集 10/10（37） |
| 124 | `ask_e2eedfdfc38b28b2cf41fb28` | `answered` | 2026-09-24 15:29:21.979 +0800 | 预实验补推理 1/3（q6/q7/q15/q16） |
| 125 | `ask_7d3fd58fde756997d20265e7` | `answered` | 2026-09-24 15:37:30.970 +0800 | 预实验补推理 2/3（q19/q25/q27/q28） |
| 126 | `ask_04e0a4be4ec269ef6d7cd98a` | `answered` | 2026-09-24 15:48:43.002 +0800 | 预实验补推理 3/3（q32/q36/q37） |
| 127 | `ask_09549f28396f623d10620a5d` | `answered` | 2026-09-24 17:25:07.593 +0800 | 清单元决策 1 题：分类口径细化 3 项 |
| 128 | `ask_721b8b46601f0b96a6989a0f` | `answered` | 2026-09-24 18:18:02.017 +0800 | 待拍板 4 项：清理路径 + verdict 复核 3 项 |
| 129 | `ask_a0d8e8333d22b65807c55eb6` | `answered` | 2026-09-24 18:22:42.334 +0800 | K-V2-b1：3 件分歧事件批判反思字面补充 |
| 130 | `ask_78da95120311ddbe4a811c45` | `answered` | 2026-09-24 18:30:59.539 +0800 | 批判反思逐件补充（3 题，每题 1 句原话） |
| 131 | `ask_6ee335d6f1a3ed88a6a412c7` | `answered` | 2026-09-24 18:45:17.912 +0800 | 主目录 <1000 差额 +324 扩容拍板 |
| 132 | `ask_d38952e0b8edb60bd854a470` | `answered` | 2026-09-24 18:59:26.409 +0800 | R4 key 明文处置 4 项待拍板 |
| 133 | `ask_42de296578f97f8faa3afd99` | `answered` | 2026-09-24 19:40:51.283 +0800 | 终局 +43：<1000 最后一棒方案 |
| 134 | `ask_748d9242c7a6be3d83de63a0` | `answered` | 2026-09-24 23:00:42.040 +0800 | L14V3 五教师 model 映射 4 项拍板 |
| 135 | `ask_9484b696c4f3af85941b3c43` | `answered` | 2026-09-24 23:31:36.631 +0800 | 待拍板第 1 轮：追认 + T1.5 + metadata 字段 + SHA 漂移 |
| 136 | `ask_249ba8854ee343f7d9aa34de` | `answered` | 2026-09-24 23:37:12.165 +0800 | 待拍板第 2 轮：V3 历史断层 3 条 + prompt 复现口径 |
| 137 | `ask_259658a4ffadd6f8aeb12f34` | `answered` | 2026-09-24 23:41:54.918 +0800 | GLM_2「不同语料」实操口径（影响分布可区分性） |
| 138 | `ask_57981c1bc81e03b9990a06e5` | `answered` | 2026-09-26 16:26:19.422 +0800 | 回归拍板 4 题：追认 + 计数口径 + T1.5 扩展 + 审链授权 |
| 139 | `ask_e041b1bc408d9b418cbc84df` | `answered` | 2026-09-26 16:44:16.531 +0800 | 任务 B 跨天采集 D2 · 第 1 波（R1b–R4b 反转变体） |
| 140 | `ask_d4f8e4a39e91ad0941c610ea` | `answered` | 2026-09-26 16:52:30.964 +0800 | 任务 B 跨天采集 D2 · 第 2 波（R5b/R6b + Q38/Q39） |
| 141 | `ask_a384fba6bba8931943280d83` | `answered` | 2026-09-26 17:02:29.616 +0800 | 任务 B 跨天采集 D2 · 第 3 波（Q40–Q43） |
| 142 | `ask_1d03472fa4042ed23c58de42` | `answered` | 2026-09-26 17:11:51.466 +0800 | 任务 B 跨天采集 D2 · 第 4 波（Q44–Q47） |
| 143 | `ask_c4c1b896880ba5e6292a6a5c` | `answered` | 2026-09-26 17:18:03.504 +0800 | 任务 B 跨天采集 D2 · 终波（Q48–Q50 + case#1 拍板） |
| 144 | `ask_2c1f40e361b54a9b76a3fa6c` | `answered` | 2026-09-26 18:02:12.850 +0800 | D3 第 1 波（Q1/Q2/Q4/Q5 第三读·判定稳定性） |
| 145 | `ask_03cf2812a9858024d1e5a41d` | `answered` | 2026-09-26 18:07:44.770 +0800 | D3 第 2 波（Q6/Q8/Q9/Q10 第三读） |
| 146 | `ask_fca627aa3ccad1f2b46be5a3` | `answered` | 2026-09-26 18:14:09.471 +0800 | D3 终波（Q11/Q12/Q16/Q17 第三读） |
| 147 | `ask_822b1e27a43f2bf8ff86785d` | `answered` | 2026-09-26 18:27:24.462 +0800 | TH-v2-3 口径拍板 + 正式判定放行（补发） |
| 148 | `ask_9c8751ec504487fa66303b28` | `answered` | 2026-09-26 18:55:54.728 +0800 | 收尾补充项：GLM github 来源 + 委托信补充口径 |
| 149 | `ask_96e0f651f306f2337cd57b47` | `answered` | 2026-09-26 19:04:48.568 +0800 | 拍板遗留第 1 轮（4 题）：追认打包 + D1 补填 + 锚链口径 + 小项打包 |
| 150 | `ask_9aa5f0c1433db0ff2d7f77c9` | `answered` | 2026-09-26 19:38:49.107 +0800 | KIMI 停手回函 4 项裁定 |
| 151 | `ask_63c7017788705498adf0e791` | `answered` | 2026-09-26 19:41:29.460 +0800 | GitHub 通道指认（补问：上次 Other 未填） |
| 152 | `ask_2532cbe17fba7df27aa2cbea` | `answered` | 2026-09-26 21:12:39.981 +0800 | 上传圈定 8 项拍板 · 轮 1（4 题） |
| 153 | `ask_ffcda4c4fd3a281ae1a6d417` | `answered` | 2026-09-26 21:15:42.583 +0800 | 上传圈定 8 项拍板 · 轮 2（2 题收尾） |
| 154 | `ask_905fffd4e03e5cbc989e49fa` | `answered` | 2026-09-26 21:19:43.506 +0800 | 严禁 13 件逐件复审（3 题分组） |
| 155 | `ask_508073ac495a485359eed804` | `answered` | 2026-09-26 22:28:08.770 +0800 | COZE 回函 2 题拍板 |
| 156 | `ask_0526e879767327abb6d548f7` | `answered` | 2026-09-26 23:08:08.369 +0800 | Phase 1 后续计划待拍板（4 项） |
| 157 | `ask_f4146275655e5b22f3ea8ebb` | `answered` | 2026-09-26 23:19:31.309 +0800 | Review implementation plan |
| 158 | `ask_08f9643bfc821cdcb52e0a57` | `answered` | 2026-09-27 11:51:18.580 +0800 | Phase 1 收口拍板（4 项） |
| 159 | `ask_fb7143a315d6296643e623d1` | `answered` | 2026-09-27 12:00:50.394 +0800 | G3/G4 遗留 2 项续问 |
| 160 | `ask_06d9754d01d894277a6baa90` | `answered` | 2026-09-27 12:50:31.100 +0800 | 链③前置与 V3 悬挂裁定（3 项） |
| 161 | `ask_d56013a4a88755666a19cfff` | `answered` | 2026-09-27 12:53:33.909 +0800 | PG 口径冲突裁决内容（1 项） |
| 162 | `ask_788e151d33bee18b6aee8a96` | `answered` | 2026-09-27 13:02:46.419 +0800 | 收工前 2 小项确认 |
| 163 | `ask_c86c0fab91c811210dec5a5c` | `answered` | 2026-09-27 13:08:53.767 +0800 | 任务 B 采集 · D5 波（2 题，各 <30 秒；选定后可随手附 1 句推理，可跳过） |
| 164 | `ask_0ec0da85da47b18a9696065e` | `answered` | 2026-09-27 13:24:38.937 +0800 | V3 假判处决（2 项） |
| 165 | `ask_0d48e1becd0c7f50e8c1677d` | `answered` | 2026-09-27 13:54:40.162 +0800 | F1 装载缺陷处置深度（2 项） |
| 166 | `ask_083f814db95739725522f993` | `answered` | 2026-09-27 14:01:33.261 +0800 | 不明涉成本 3 条＋遗留拍板 3 项（4 题） |
| 167 | `ask_044bc79d96b1bf88fac9dd1f` | `answered` | 2026-09-27 14:19:50.508 +0800 | 不明清障 2 项遗留拍板 |
| 168 | `ask_93ec7918b810126d294c7b1b` | `answered` | 2026-09-27 14:24:14.416 +0800 | 三条实测遗留拍板（4 题，余 1 项下轮） |
| 169 | `ask_f99730fee0fe6f8d2149eacc` | `answered` | 2026-09-27 14:31:27.261 +0800 | V3-R 生效与执行组织（3 题） |
| 170 | `ask_b93ba45b5e10366f1c883861` | `answered` | 2026-09-27 14:47:04.852 +0800 | v1.1 生效与授权（3 题） |
| 171 | `ask_a7c5bc961c47a5271542252a` | `answered` | 2026-09-27 14:54:21.350 +0800 | verdict_v3 §4 触发条件（1 题） |
| 172 | `ask_167a54be6af9f2090ee5c900` | `answered` | 2026-09-27 14:59:47.359 +0800 | 第一梯队遗留 2 项拍板 |
| 173 | `ask_ee8102884179fd206517c5b6` | `answered` | 2026-09-27 15:05:13.654 +0800 | #26 动力学本体指定（1 题） |
| 174 | `ask_08db3d4c21c5595d3dbad6bd` | `answered` | 2026-09-27 15:15:59.282 +0800 | §4 启动项指定（组合可在 Other 写明） |
| 175 | `ask_041a38e508e2c2b165b3702d` | `answered` | 2026-09-27 15:32:11.618 +0800 | V3-S 生效拍板（4 题，余 3 项下轮） |
| 176 | `ask_75126c38abf2c134a1591672` | `answered` | 2026-09-27 15:37:02.575 +0800 | #26 正式实验本体择定（1 题） |
| 177 | `ask_421d7df4aa0929633c265c47` | `answered` | 2026-09-27 16:08:11.828 +0800 | 三梯队 A＋S2 遗留拍板（4 题，余 3 项下轮） |
| 178 | `ask_b4491e8edd992f6baf8015a0` | `answered` | 2026-09-27 16:23:37.935 +0800 | 收口拍板 4 题（#12(b) 改挂＋余项） |
| 179 | `ask_2298f97cc6731d7a9baf4803` | `answered` | 2026-09-27 16:51:33.883 +0800 | 拍板批次（4 题） |
| 180 | `ask_c07cb22a0c7d5ace449935f0` | `answered` | 2026-09-27 17:02:17.657 +0800 | #35/#21 口径归属（2 题） |
| 181 | `ask_ad37c9c9282a3edb0b881fe8` | `answered` | 2026-09-27 17:21:02.768 +0800 | 总收口拍板第一轮（4 题实质项） |
| 182 | `ask_554d56d3cab4badeb5b0d2c3` | `answered` | 2026-09-27 18:00:46.661 +0800 | 择优择定＋第二轮拍板（4 题） |
| 183 | `ask_5b410e39e24d8e4d3def7cad` | `answered` | 2026-09-27 19:26:50.726 +0800 | 终收 2 项小择定 |
| 184 | `ask_502d4db0f8a9d0f6d0627475` | `answered` | 2026-09-27 20:47:02.660 +0800 | Trae 回函处置拍板（4 题） |
| 185 | `ask_605c0b8230ace6d78bb95383` | `answered` | 2026-09-28 13:41:35.332 +0800 | 任务 B 采集 · D6 波（2 题，<30 秒/题；推理 1 句可随手附，可跳过） |
| 186 | `ask_cee68b459ec10b7ea9912f66` | `answered` | 2026-09-28 13:43:37.501 +0800 | 余项拍板 4 题（T-S3 余项＋#5 档位） |
| 187 | `ask_b01f898512b014e6f26d4267` | `answered` | 2026-09-28 14:12:32.386 +0800 | 拍板清账（4 题） |
| 188 | `ask_cd4b4a2f8c829197481a86af` | `answered` | 2026-09-28 14:43:19.815 +0800 | 采集 · 今日第 2 波（2 题，推理 1 句可跳过） |
| 189 | `ask_eeac0436167f475406e3f1d3` | `answered` | 2026-09-28 15:07:21.482 +0800 | 遗忘项处置（2 题） |
| 190 | `ask_79fd9fad41e57ba8040361a8` | `answered` | 2026-09-28 15:33:22.675 +0800 | 慢处置收口拍板（4 题） |
| 191 | `ask_e80cbe75756d66b71799c635` | `answered` | 2026-09-28 15:55:42.081 +0800 | 隐性遗忘处置（3 题） |
| 192 | `ask_90f108da8b781eece9c90088` | `answered` | 2026-09-28 16:01:05.604 +0800 | #1/#4 第三方判断采纳（2 题） |
| 193 | `ask_0c42eceb62edbe56673976da` | `answered` | 2026-09-28 17:04:51.682 +0800 | NULL |
| 194 | `ask_273b21c32e4ae33e0b401a09` | `answered` | 2026-09-28 17:17:20.835 +0800 | NULL |
| 195 | `ask_8d6a044fcb80f30cfa9dfea3` | `answered` | 2026-09-28 17:54:42.133 +0800 | Review implementation plan |
| 196 | `ask_577b95bf8620614e98567bca` | `answered` | 2026-09-28 17:57:01.830 +0800 | NULL |
| 197 | `ask_46a378d24827fff58917f478` | `answered` | 2026-09-28 18:16:51.263 +0800 | NULL |
| 198 | `ask_049a92f9a9bbe4a00c4cc815` | `answered` | 2026-09-28 18:21:00.455 +0800 | NULL |
| 199 | `ask_ddebd3637cef1fe364ee6fe7` | `answered` | 2026-09-28 18:32:28.734 +0800 | NULL |
| 200 | `ask_f25f4117ca57d71f000afb16` | `answered` | 2026-09-28 19:13:49.162 +0800 | NULL |
| 201 | `ask_81b14bef512f00fe3d077f9e` | `answered` | 2026-09-28 19:25:20.637 +0800 | NULL |
| 202 | `ask_49fcd1238ef6fa91025daf7a` | `answered` | 2026-09-28 19:28:27.902 +0800 | NULL |
| 203 | `ask_b3cd4d21826a755e71b516c3` | `answered` | 2026-09-28 19:37:48.719 +0800 | NULL |
| 204 | `ask_b99f19657653ae3b70d35629` | `answered` | 2026-09-28 20:01:20.943 +0800 | NULL |
| 205 | `ask_92c2d2005a86c8e47ac9eb95` | `answered` | 2026-09-28 20:09:47.308 +0800 | NULL |
| 206 | `ask_c200e23a72698238ae70f54f` | `answered` | 2026-09-28 20:22:39.890 +0800 | Review implementation plan |
| 207 | `ask_d340097f06276e0152c866c2` | `answered` | 2026-09-28 20:26:52.226 +0800 | NULL |
| 208 | `ask_f96e17374c45c4c213ba71c0` | `answered` | 2026-09-28 22:14:21.599 +0800 | NULL |
| 209 | `ask_c6721836fb0a2e1af6c12f37` | `answered` | 2026-09-28 22:38:54.817 +0800 | NULL |
| 210 | `ask_64480a3591664eadec28e7c2` | `answered` | 2026-09-28 22:45:15.446 +0800 | NULL |
| 211 | `ask_0d80934d1d5045349d25f712` | `answered` | 2026-09-28 22:49:20.184 +0800 | NULL |
| 212 | `ask_0755918ed1cdd55725e63056` | `answered` | 2026-09-28 22:56:19.473 +0800 | NULL |
| 213 | `ask_a6b825a923fe2b884057cee9` | `answered` | 2026-09-28 23:17:07.278 +0800 | NULL |
| 214 | `ask_c7f297823ff964c19ca89aa1` | `answered` | 2026-09-28 23:38:22.380 +0800 | NULL |
| 215 | `ask_90009bd33020f0b43a270672` | `answered` | 2026-09-29 10:39:03.710 +0800 | NULL |
| 216 | `ask_e8c605dd1d9b662df6a33923` | `answered` | 2026-09-29 10:53:05.990 +0800 | NULL |
| 217 | `ask_0b4c1577f0d727e239e55095` | `answered` | 2026-09-29 11:00:48.793 +0800 | NULL |
| 218 | `ask_e1bdb06e5eee79a2d5b47559` | `answered` | 2026-09-29 11:19:58.705 +0800 | NULL |
| 219 | `ask_1e658ed52e7856a0bb3647ed` | `answered` | 2026-09-29 11:28:02.950 +0800 | NULL |
| 220 | `ask_d567d67c17eb09b825559dab` | `answered` | 2026-09-29 11:49:55.269 +0800 | NULL |
| 221 | `ask_ce9d69e725691a5494da3827` | `answered` | 2026-09-29 12:00:16.644 +0800 | NULL |
| 222 | `ask_8977a7e8e133d10c513d1aad` | `answered` | 2026-09-29 13:00:41.903 +0800 | deposon 确认批 1：V3 修复执行裁项（①②④）＋ N-2 |
| 223 | `ask_7401b6bf4adf17f662a96be7` | `answered` | 2026-09-29 13:05:54.902 +0800 | deposon 确认批 2：V3 余项（③⑤⑥）＋ 锚 2/3 数值补遗 |
| 224 | `ask_86d90858fa05cb4a3078a9b5` | `answered` | 2026-09-29 13:11:04.695 +0800 | deposon 确认批 3：姊妹件生效 / P-7 三案 / P-6 两项 |
| 225 | `ask_8ddf56e4aa246a021f837afd` | `answered` | 2026-09-29 13:21:31.727 +0800 | deposon 确认批 4（合并卷）：V3 重开跑 2 题 ＋ #35/GT 收尾打包 |
| 226 | `ask_e302d05c00d67fab89b1f72b` | `answered` | 2026-09-29 13:30:06.801 +0800 | deposon 确认批 5（合并卷）：件1 / 件2 / C5 / 杂项 四包 |
| 227 | `ask_65caab28a0c757e01be87300` | `answered` | 2026-09-29 13:43:00.019 +0800 | deposon 确认批 6（③类合并卷）：论文面 / FTFB / 哈希锚件 / R4 |
| 228 | `ask_01a52035ac0816bbf2b585b4` | `answered` | 2026-09-29 13:51:54.377 +0800 | deposon 确认批 7：V3 重开跑 5 项 / ③-改机制 / C5 两项 |
| 229 | `ask_b0ec007610797299c477b790` | `answered` | 2026-09-29 13:57:23.481 +0800 | deposon 确认批 8：γ-END-1 / 命名打包 / 运维包 / 信息包 |
| 230 | `ask_afc8fbae02169e6f98dbdc8f` | `answered` | 2026-09-29 14:05:21.095 +0800 | deposon 确认批 9：件A / 件B / 留痕纪律 / KIMI 映射 |
| 231 | `ask_55ef16c0a6e86d0d814a1921` | `answered` | 2026-09-29 14:09:32.653 +0800 | deposon 确认批 10：归档 / 扩面 / V4 提案 / 杂项 |
| 232 | `ask_ffc0a23298498dcbb9061946` | `answered` | 2026-09-29 14:13:26.931 +0800 | deposon 确认批 11：r2 残项四题 |
| 233 | `ask_58ea45aadddbefba952ffd51` | `answered` | 2026-09-29 14:17:40.721 +0800 | deposon 确认批 12：R4 收尾 / 清走 / 锚件 / 回收站 |
| 234 | `ask_65ac61d9906cdf1d56f32262` | `answered` | 2026-09-29 14:27:07.843 +0800 | deposon 确认批 13（补救线合卷）：Q1–Q4 |
| 235 | `ask_0fac5b64abcf41c1ff667dd3` | `answered` | 2026-09-29 14:35:46.671 +0800 | deposon：Token Plan 达限处置 |
| 236 | `ask_4b432182e1d04cfdbdd61fa0` | `answered` | 2026-09-29 14:41:09.979 +0800 | deposon 确认批 14（清卷·r2 清册）：M-Q1–M-Q4 |
| 237 | `ask_658f3c5a1fb70fb7de696065` | `answered` | 2026-09-29 14:43:09.693 +0800 | deposon 确认批 15（清卷·r2 清册）：M-Q5–M-Q8 |
| 238 | `ask_1bab5619530e1229291f8f22` | `answered` | 2026-09-29 14:47:34.642 +0800 | deposon 确认批 16（清卷·r2 清册）：M-Q9–M-Q12 |
| 239 | `ask_e7249e680b6ea6ecf3a0aeab` | `answered` | 2026-09-29 14:50:34.540 +0800 | deposon 确认批 17（清卷·r2 清册）：M-Q14–M-Q17 |
| 240 | `ask_8da72bcae40e10a9e87f88aa` | `answered` | 2026-09-29 14:55:54.221 +0800 | deposon 确认批 18（清卷·r2 清册收官）：M-Q18–M-Q20 ＋ 开放式项 |
| 241 | `ask_646069956ced5ec1d5ef58f4` | `answered` | 2026-09-29 14:59:57.343 +0800 | deposon 确认批 19（清卷）：开放式项输入＋V4-23 卷A |
| 242 | `ask_275b2331c006d3fc3fc71565` | `answered` | 2026-09-29 15:05:36.280 +0800 | deposon 确认批 20（清卷）：V4-23 卷B ＋ 尺寸档 |
| 243 | `ask_23fc5151ac4e6e8bb55e8cd0` | `answered` | 2026-09-29 15:07:08.134 +0800 | deposon 确认批 21（清卷·族线）：R-01–R-04 |
| 244 | `ask_ebf5a205cc8eb87986ffed4b` | `answered` | 2026-09-29 18:01:33.860 +0800 | 批 19 重发卷（4 题）· O-1..O-8 开放式项 ＋ V4-23 卷A Q2–Q4 |
| 245 | `ask_9645765295024dcc42165ef9` | `answered` | 2026-09-29 18:06:34.025 +0800 | 批 22 重发卷（4 题）· R-05/R-06/R-07 ＋ 批 12「澄清三项」指认 |
| 246 | `ask_8734bb559a000111389fd729` | `answered` | 2026-09-29 18:15:14.918 +0800 | 清卷轮 3（4 题）· Q4「改选目标」补明 ＋ O-8/O-7/O-6（拆分逐项） |
| 247 | `ask_bf3f45eb7a070f26058895fa` | `answered` | 2026-09-29 18:24:06.435 +0800 | 清卷轮 4（4 题）· O-1..O-4 选项化（预读包已解出细节） |
| 248 | `ask_f97683c569bd56030663f12d` | `answered` | 2026-09-29 18:27:19.292 +0800 | 清卷轮 5（4 题）· O-5 三组并列决策（「择一」框架已更正）＋ O-1 的 N 补问 |
| 249 | `ask_67b75c4762645f32c03828c7` | `answered` | 2026-09-29 18:32:14.414 +0800 | 清卷轮 6（4 题）· 新积批起：仓外授权勾选＋#01 刀锋＋H2-31＋P-10 三大择一 |
| 250 | `ask_34eea842473d1c4dc04b5356` | `answered` | 2026-09-29 18:40:52.543 +0800 | 清卷轮 7（4 题）· P-10 门口径确认＋回收站/b12核验/b14留白 三大打包 |
| 251 | `ask_b2243a228cc93629a2dcd2e4` | `answered` | 2026-09-29 18:44:19.100 +0800 | 清卷轮 8（4 题）· P-L 门②门③＋#08c R-3 二择一＋γ_A KD 反证 |
| 252 | `ask_f14ec2f3ccb1df6ce64c2c52` | `answered` | 2026-09-29 18:49:18.266 +0800 | 清卷轮 9（4 题）· 判准释义＋R-07 规则选＋v1.2 序列号＋P4-1C 值 |
| 253 | `ask_c9b0aaf3f817c45e91e67713` | `answered` | 2026-09-29 18:52:15.750 +0800 | 清卷轮 10（4 题）· P-L 门④＋M-Q11 载体＋#35 十二件＋O-8 口径 |
| 254 | `ask_cf3e00148b5d315b9d0b4f33` | `answered` | 2026-09-29 18:57:28.490 +0800 | 清卷轮 11（4 题）· r4 清册轮1：高利害四题（#26b 重跑 / SHA-1 勘误 / S-40 双因 / D5 立项） |
| 255 | `ask_4f9b84461f4c12e26bf2885d` | `answered` | 2026-09-29 19:07:17.875 +0800 | 清卷轮 12（4 题）· r4 轮2/3：标注族＋归因3路径＋端点族10条＋embedding/RAG |
| 256 | `ask_5a56da32ab91ecbf2d510519` | `answered` | 2026-09-29 19:16:53.254 +0800 | 清卷轮 13（4 题）· r4：扩样/未跑实迹＋V2 交付优先级＋文档漂移＋SELF-CHECK 终态 |
| 257 | `ask_49b3c5c2429c45b1bab31386` | `answered` | 2026-09-29 19:22:32.281 +0800 | 清卷轮 14（4 题）· P4-1C 给值＋M-R13/M-R21/M-R15 |
| 258 | `ask_72b5cfcc4fcee177a5def527` | `answered` | 2026-09-29 19:27:18.784 +0800 | 清卷轮 15（4 题）· r4：命名冲突面＋默认档确认＋上传裁定族＋校准披露面 |
| 259 | `ask_70e3b6e1bbdedea447ef3e4f` | `answered` | 2026-09-29 19:30:19.018 +0800 | 清卷轮 16（4 题）· r4 收官：P-F 五条＋开放式 6 条（方向题/外部核验族/CoT-as-audit） |
| 260 | `ask_6291c6ea5c1cf6ae580bc22f` | `answered` | 2026-09-29 19:39:27.236 +0800 | 清卷轮 17（4 题）· V3 判定 13 项（一）：T1 效力射程／4-2 落法／第二出口／af 口径 |
| 261 | `ask_91f0884efa593efe160db1a9` | `answered` | 2026-09-29 19:49:13.852 +0800 | 清卷轮 18（4 题）· V3 余项：4-2 落法确认／门域完备性／C5 面／145.8× 定性 |
| 262 | `ask_fca71bee33ee7652e4e49b47` | `answered` | 2026-09-29 21:03:40.984 +0800 | 两件待拍板：README 扶正 / C5 cron |
| 263 | `ask_73ba71c58ba577c4a33d741f` | `answered` | 2026-09-29 21:13:09.094 +0800 | 三件待裁：V5 命名处置 |
| 264 | `ask_1aca8ed0bef608fff8298b2c` | `answered` | 2026-09-29 22:42:45.105 +0800 | 新待拍板合并卷（4 题） |
| 265 | `ask_79496aa9b225033bdd1fb829` | `answered` | 2026-09-29 22:58:54.657 +0800 | F2 · U-1 关系裁定 |
| 266 | `ask_c3f17304fcb64cefbf49275d` | `answered` | 2026-09-29 23:37:52.560 +0800 | README 勘误处置 & C5 重派方式 |
| 267 | `ask_dfe136b00e25ad4fae7a81cf` | `answered` | 2026-09-30 12:46:54.381 +0800 | NULL |
| 268 | `ask_72adb71ea07edc063ceed334` | `answered` | 2026-09-30 12:52:09.479 +0800 | D8 开卷·第 1 批 ｜ 直接点选；想附 1 句推理就在 Other 框写「字母＋理由」（可跳过） |
| 269 | `ask_a6f88ff30bf89a8e804239d9` | `answered` | 2026-09-30 13:01:02.617 +0800 | D8 开卷·第 2 批 ｜ 直接点选；想附 1 句推理就在 Other 框写「字母＋理由」 |
| 270 | `ask_ffe8cdf9d2b1d84294afd1c6` | `answered` | 2026-09-30 13:09:09.375 +0800 | D8 开卷·第 3 批 ｜ 直接点选；想附 1 句推理就在 Other 框写「字母＋理由」 |
| 271 | `ask_d36d1fa8c5265673a67fcdd1` | `answered` | 2026-09-30 13:15:40.748 +0800 | D8 开卷·第 4 批 ｜ 直接点选；想附 1 句推理就在 Other 框写「字母＋理由」 |
| 272 | `ask_5901a28baa3485800e376ac1` | `answered` | 2026-09-30 13:25:42.754 +0800 | D8 开卷·第 5 批 ｜ 直接点选；想附 1 句推理就在 Other 框写「字母＋理由」 |
| 273 | `ask_cd08e7bacaa1cb99ecceaa34` | `answered` | 2026-09-30 13:35:40.987 +0800 | D8 开卷·第 6 批（重推） ｜ 直接点选；想附推理就用 Other 框写「字母＋理由」 |
| 274 | `ask_de8dbebee79a8e9ebde007fa` | `answered` | 2026-09-30 13:43:57.635 +0800 | D8 开卷·第 7 批 ｜ 直接点选；想附推理就用 Other 框写「字母＋理由」 |
| 275 | `ask_4642a816a64ef5f31728c28d` | `answered` | 2026-09-30 13:53:13.490 +0800 | D8 · 边界处置（单问） ｜ 三选一，或 Other 写你的处置 |
| 276 | `ask_242e4155096181f4f16cd14b` | `answered` | 2026-09-30 14:08:08.136 +0800 | D8 边界修订·四项裁决 ｜ 直接点选，或 Other 写你的处置 |
| 277 | `ask_4341a4423c517f0e41c99abd` | `answered` | 2026-09-30 14:11:43.159 +0800 | D8 重启·第 8 批（修订版生效） ｜ 直接点选；想附推理就用 Other 框写「字母＋理由」 |
| 278 | `ask_16f0f4dc3ae9321ef79de182` | `answered` | 2026-09-30 14:22:00.750 +0800 | D8 开卷·第 9 批（D8-33～35 ＋ 16 组采纳） ｜ 直接点选；想附推理就用 Other 框 |
| 279 | `ask_faf9de6def9e1c2384a5954b` | `answered` | 2026-09-30 14:37:31.576 +0800 | D8 开卷·第 10 批（D8-36〔R11a〕/38/39/40） ｜ 直接点选；想附推理就用 Other 框 |
| 280 | `ask_a5bf873f436ba5a68a808567` | `answered` | 2026-09-30 14:42:35.140 +0800 | D8 开卷·第 11 批（D8-41～44） ｜ 直接点选；想附推理就用 Other 框 |
| 281 | `ask_1d3dd509d148173cc4baa95f` | `answered` | 2026-09-30 14:47:04.620 +0800 | D8 开卷·第 12 批（D8-45～48） ｜ 直接点选；想附推理就用 Other 框 |
| 282 | `ask_e6b4fcbe7b00e25aab4d69fa` | `answered` | 2026-09-30 14:50:39.449 +0800 | D8 开卷·第 13 批（D8-49～52） ｜ 直接点选；想附推理就用 Other 框 |
| 283 | `ask_cba2075ac4faf0f4f4d28ae7` | `answered` | 2026-09-30 14:58:07.308 +0800 | D8 开卷·第 14 批（D8-53～56） ｜ 直接点选；想附推理就用 Other 框 |
| 284 | `ask_882bdceab49d3ed97d4f73b0` | `answered` | 2026-09-30 15:03:54.008 +0800 | D8 开卷·第 15 批（D8-57／58r／59r／60） ｜ 直接点选；想附推理就用 Other 框 |
| 285 | `ask_721f00fa3e4977bcc0f56d45` | `answered` | 2026-09-30 15:07:23.590 +0800 | D8 开卷·第 16 批（D8-61～64） ｜ 直接点选；想附推理就用 Other 框 |
| 286 | `ask_2c5426e79464ebd78d48c8fc` | `answered` | 2026-09-30 15:14:50.443 +0800 | D8 开卷·第 17 批（D8-65～68） ｜ 直接点选；想附推理就用 Other 框 |
| 287 | `ask_10e87126e314e298e0ed6db4` | `answered` | 2026-09-30 15:20:55.698 +0800 | D8 开卷·第 18 批（D8-69～72） ｜ 直接点选；想附推理就用 Other 框 |
| 288 | `ask_fa8b654cc5221cd654e880dc` | `answered` | 2026-09-30 15:25:49.545 +0800 | D8 开卷·第 19 批（D8-73～76） ｜ 直接点选；想附推理就用 Other 框 |
| 289 | `ask_91c25e9740d3cef10f18cd49` | `answered` | 2026-09-30 15:32:29.932 +0800 | D8 开卷·第 20 批（终段：D8-77～80） ｜ 直接点选；想附推理就用 Other 框 |
| 290 | `ask_e829a3e1bb17f57d6029fbba` | `answered` | 2026-09-30 15:36:47.886 +0800 | SQ 开卷·批 1（SQ-01～03＋skill 4 项） ｜ 作答写进 Other 框，1–3 句、可只写一句 |
| 291 | `ask_921f42b832970a9d5274fbfb` | `answered` | 2026-09-30 15:46:53.495 +0800 | SQ 开卷·批 2（SQ-04～07） ｜ 作答写进 Other 框，1–3 句、可只写一句 |
| 292 | `ask_a8ebc92a2538769f44ebcd87` | `answered` | 2026-09-30 15:59:30.464 +0800 | SQ 终批（SQ-08＋skill 6 项） ｜ 作答写进 Other 框；skill 项直接点选 |
| 293 | `ask_830fd0fa7bfa20129daf254e` | `answered` | 2026-09-30 16:09:52.228 +0800 | T-D8-3 · b 半作答日（单问·收讫收尾） ｜ 直接点选 |
| 294 | `ask_83f2b8ed7f0c33818cf97fb1` | `answered` | 2026-09-30 16:12:22.861 +0800 | T-D8-3（更正版） ｜ 我题面有误，重新点一下 |
| 295 | `ask_5cd9bea3d315db200aa19dee` | `answered` | 2026-09-30 16:13:03.259 +0800 | D8 b 半（即刻·降级标注口径）：D8-11〔R9b〕/ D8-19〔R10b〕/ D8-37〔R11b〕 |
| 296 | `ask_788da4cb0d031d6328c2848a` | `answered` | 2026-09-30 16:36:37.506 +0800 | skill 收口遗留 · 2 项待拍板 |
| 297 | `ask_3109ce0430454d83459db9e5` | `answered` | 2026-09-30 16:51:32.149 +0800 | 【PI】拍板卷（4 题） |
| 298 | `ask_61300ee638519d59d23a1d33` | `answered` | 2026-09-30 17:12:14.003 +0800 | 【人机协同】收尾小卷（2 题） |
| 299 | `ask_57366a35340cf2ef58a24e3e` | `answered` | 2026-09-30 17:53:10.070 +0800 | 【人机协同】整理·S 清单小卷（2 题） |
| 300 | `ask_ec9b5c63e9e914ab05a8f99a` | `answered` | 2026-09-30 18:22:53.322 +0800 | 【人机协同】整理·收口小卷（2 题） |
| 301 | `ask_bd0a92cff709bea7e783f54d` | `answered` | 2026-09-30 18:30:04.394 +0800 | 【人机协同】S1 清源（补发 · 1 题） |
| 302 | `ask_01cef387cd393b46cc567656` | `answered` | 2026-09-30 18:51:13.552 +0800 | 【人机协同】S1 清源·终裁（1 题） |
| 303 | `ask_3b8a6489fb38917e42a69ecd` | `answered` | 2026-09-30 19:35:20.839 +0800 | 【人机协同】合并全卷 · 待拍板清卷（4 题·16 子项） |
| 304 | `ask_da8ce88762c1f39cb62e95f4` | `answered` | 2026-09-30 20:04:05.377 +0800 | 【人机协同】C4 推导·择定卡（3 题） |
| 305 | `ask_ead0d2f7dc818155041ee0cb` | `answered` | 2026-09-30 20:29:31.835 +0800 | 【人机协同】三裁执行·回收确认（2 题） |
| 306 | `ask_47fd494df6eff37c2872c79d` | `answered` | 2026-09-30 22:46:08.461 +0800 | Review implementation plan |
| 307 | `ask_18489cb1d042b5b86c527094` | `answered` | 2026-10-01 00:26:15.254 +0800 | deposon 确认卷 · 待拍板清（4 题） |
| 308 | `ask_6d484dd0e096ceb3d06736fb` | `answered` | 2026-10-01 09:38:50.032 +0800 | deposon 确认卷（二）｜待拍板清（4 题） |
| 309 | `ask_d50c961a307949025a7b8d2d` | `answered` | 2026-10-01 10:13:26.313 +0800 | deposon 小卷（三）｜散项清卷（4 题） |
| 310 | `ask_4f4a407baa1ab2135309574f` | `answered` | 2026-10-01 10:59:13.385 +0800 | 清卷·四题（S3/TH 收口 · GLM 审发 · 复核批 · U-V04） |
| 311 | `ask_c75a54724c35b47dcc069d5b` | `answered` | 2026-10-01 11:24:27.012 +0800 | Mini App 第一个 demo 做什么? |
| 312 | `ask_55c27fabffecdc84df39a69e` | `answered` | 2026-10-01 11:39:02.329 +0800 | 清卷·四题（GLM 点定 · D1 裁定 · U-V04 采纳 · S3 收口包） |
| 313 | `ask_66bf71aa7505f43b37074a1c` | `answered` | 2026-10-01 12:06:02.701 +0800 | 卷B·四题（本批收口 · 补采前置裁 · 77 两裁 · P-4 收口） |
| 314 | `ask_bf32b2c8f6065a0aaa998886` | `answered` | 2026-10-01 12:18:36.832 +0800 | 卷C·三题（B3–B7 点定 · T-SUP-1 启动 · 命名漂移） |
| 315 | `ask_e7893ea112fd5591b6325918` | `answered` | 2026-10-01 12:34:40.363 +0800 | D1 补采·DF 采集轮 R-1（DF1-2／DF1-3）· 1–2 题/轮 |
| 316 | `ask_0f95c8bc0e07d7515add6441` | `answered` | 2026-10-01 12:37:42.571 +0800 | D1 补采·DF 采集轮 R-2（DF1-4／DF1-5）· 1–2 题/轮 |
| 317 | `ask_313ef5eb946d81cc6bc9b24e` | `answered` | 2026-10-01 12:43:38.681 +0800 | D1 补采·DF 采集轮 R-3（DF1-6／DF1-7）· 末轮 |
| 318 | `ask_f9646da2052bdd7ceb063ac1` | `answered` | 2026-10-01 12:45:34.260 +0800 | D1 补采·B4 新 id 前缀终核（1 题） |
| 319 | `ask_f18799ce3f4ea455f3224d23` | `answered` | 2026-10-01 12:57:34.769 +0800 | 乐音方向 + 对齐范围 |
| 320 | `ask_371ad9b2ba960cb6a3e503a0` | `answered` | 2026-10-01 13:24:41.573 +0800 | 卷D-1·四题（S3 判读面：K-V3S-3-2／B3 口径／A2 措辞／T-1 处置） |
| 321 | `ask_c610e18cdeefb1afe93aa991` | `answered` | 2026-10-01 13:32:50.932 +0800 | 卷D-2·四题（计数不可复现／互斥择一／77 口径／D-4 落位） |
| 322 | `ask_0d09e7ee420b72042260d9c2` | `answered` | 2026-10-01 13:38:34.695 +0800 | 卷D-3·四题（批 9 册双记／命名张力／资产 6 项／E2・E3） |
| 323 | `ask_72a7168ab10822dc2585e594` | `answered` | 2026-10-01 13:53:51.003 +0800 | 卷D-4·四题（U-V04 生效／skill 三项／PAT 两说／GLM 外发知会） |
| 324 | `ask_e843b72953ea31ec2062da37` | `answered` | 2026-10-01 14:11:13.406 +0800 | 末微卷·四题（N-1 落位／N-2・N-3・N-5／T-1 输入面／_s3_ 命名） |
| 325 | `ask_d34594f704876ccbbf182fcf` | `answered` | 2026-10-01 14:26:41.655 +0800 | 末微卷·补二题（N-2/N-3 随甲档？／E3 副本形态） |
| 326 | `ask_ec6e8c16d5e1374ea766e9de` | `answered` | 2026-10-01 14:44:20.252 +0800 | U-V04 一次性复核签核（R1–R6＋R7 生效）· 重发 |
| 327 | `ask_754e869def6f370db70c6292` | `answered` | 2026-10-01 15:47:56.839 +0800 | 复核确认（工具留档） |
| 328 | `ask_1f1e746e790d7e8395263060` | `answered` | 2026-10-01 16:05:18.432 +0800 | 挂账清卷（口径批） |
| 329 | `ask_f945a03b66ad250c7e329c17` | `answered` | 2026-10-01 16:58:20.521 +0800 | 今日收尾・候示两问 |
| 330 | `ask_b2f7077749a8ffcec839f483` | `answered` | 2026-10-01 19:37:59.610 +0800 | sub 转移・候批两问 |
| 331 | `ask_8a04bb5c4f9ded71e2de43a3` | `answered` | 2026-10-01 20:11:30.501 +0800 | 候裁四问（含 KIMI 圈选） |
| 332 | `ask_46c5eb5f48af77626dcf7c52` | `answered` | 2026-10-02 00:26:05.094 +0800 | Review implementation plan |
| 333 | `ask_f10adfa7afa10c50a47c7914` | `answered` | 2026-10-02 00:33:11.795 +0800 | Review implementation plan |
| 334 | `ask_9a88e793dc915c3c4e25b70a` | `answered` | 2026-10-02 01:04:00.164 +0800 | Review implementation plan |

### 5.3 候呈（**本件 0 代裁 · 0 自行处置**）

- **候呈 A**：第①段 334 件是否另派「存量回填」落册棒？规模见 §5.1（原始载荷 ≈ 1.1 MB；按前两批逐字展开体例，成件将显著大于原始载荷）。
- **候呈 B**：若回填，是否按年月分段为多件（**建议按月分件**，0 单件承载），抑或另定分段口径。
- **候呈 C**：第①段 1 件 `superseded`（`ask_05992739fd9e46f8e8acd23d`）是否随回填一并收录（其面为「已取代」，与 `answered` 面性质不同）。
- **候呈 D**：第①段卡片之 `mode` 面是否与现役登记体例一致（部分或为 `plan` 面／含 `modePayload` 长载荷，**转录体例须先定**）。

## 6 · 本轮读取方式合规确认

- 连接串：`sqlite3.connect("file:<db>?mode=ro", uri=True)` —— **只读**。⛔ 0 `INSERT`/`UPDATE`/`DELETE`/`CREATE`/`DROP`。
- ⛔ 0 网络访问；⛔ 0 调用任何 skill；⛔ 0 调用 LLM；⛔ 0 跑实验；⛔ 0 编辑或覆写任何既有工作档案（本件为新建，落前实测 `Test-Path=False` 且 glob 0 命中）。
- 读取范围：⛔ **仅** `questionnaire_requests` 表目标行之 `request_json`／`reply_payload` 等字段；**0 触其他表**。
- R4 key：对本件全部转录字面（17 件卡之 `request_json` ＋ `reply_payload` 原串，及 §4 追补答文原串）做正则扫描 —— OpenAI 式 `sk-[A-Za-z0-9]{16,}`／GitHub 式 `gh[pousr]_[A-Za-z0-9]{16,}`／AWS 式 `AKIA[0-9A-Z]{16}`／Slack 式 `xox[baprs]-…`／Google 式 `AIza[0-9A-Za-z_-]{35}`／PEM `BEGIN … PRIVATE KEY`／`Bearer <长 token>`／`*api_key*`／`*token*`／`*password*` 后接赋值符与非空值／JWT 三段点分形，各族命中均为 **0**，本件**不含任何 key／凭证明文**。
- 0 冒充：本件由 **protocol-keeper** 署名，⛔ 0 冒充 PI／parent／verdict-keeper／verifier／worker；⛔ 0 代替任何既有登记件的裁录效力。

---

*（本件完 · 逐字转录 · 0 解释 · 0 判读 · 0 代裁）*
