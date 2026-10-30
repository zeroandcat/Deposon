# 裁卡原件批量落册（第九批）· questionnaire 原件逐字转录 · 卡答落册补续批（2026-10-10）

## 文件头注

- **件名**：`results/_questionnaire_cards_intake_register_supplement_8_2026_10_10.md`
- **落册日期**：2026-10-10（CST）
- **件系**：第八批登记件 `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md`（SHA-12 `1fb8eac82781`）之**补续落册（第九批）**；上承第八批 `1fb8eac82781`（其账目补正件 `a651f76a6547`）、第七批 `95ba771fa760`（其回执 `0984955b0370`）、第六批 `edb57308170d`、第五批 `d6ff041a9df9`、第四批 `11681f0ad861`、第三批 `dc43e3cb7610`、第二批 `193386b9f23c`、第一批 `d917180db36f`。⛔ 0 编辑／覆写／修改前八批登记件；⛔ 0 重复转录其已收录之卡。
- **本批口径**：**卡答落册 · 补续批** —— 续录派工指定之**轮53～轮54 两卡**（第八批落册读时点之后所建、⛔ 尚未落册者）。合计 **2 卡／8 答**（选项通道 6 答 ＋ Other 通道 2 答）。
- **编制**：**doc-writer**（文稿起草官 · 分支会话 `mvs_cf54be9d09d54516bd6bad49e1aff82d`｜署名如实 · **0 冒充 PI／parent／protocol-keeper／verdict-keeper／verifier／worker**）
- **来源**：运行时库 `〔本地路径已脱敏〕`，表 `questionnaire_requests`。本棒以 `sqlite3.connect("file:...?mode=ro", uri=True)` **只读实测**（0 写入、0 修改、0 建表、0 提交、0 checkpoint）。
- **备核源**：会话消息面 `〔本地路径已脱敏〕` 之 `messages.jsonl`（只读检索，作二次交叉核对）。
  - ⚠ **会话目录反解纪律**：目录名 ＝ `session_` ＋ 会话 id `mvs_bbeb804b1a6a41109be740636eed1709` 之 URL-safe base64 无填充编码。本棒**先独立反解定位**（`base64.urlsafe_b64encode(...)` → 去填充 `=` → URL-safe）得 `bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5`，⛔ **0 凭记忆直接引用路径**；实测该名于 `2026\09\01\` 层**唯一命中**，实际目录名含时间戳前缀 `02-38-47-809-`。
  - ⚠ **形近近邻陷阱（本棒实测仍在位 · 未误取）**：同层另存 `02-38-47-809-session_bXZzX2IiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5` —— **时间戳前缀完全相同**，仅 base64 段第 6 字符起一字之差（`…X2JiZW…` ↔ `…X2IiZW…`）。二者反解分别为：本棒目标 → `mvs_bbeb804b1a6a41109be740636eed1709`（✅ 与派工所载会话 id **逐位相符**）；近邻 → `mvs_b"eb804b1a6a41109be740636eed1709`（⛔ **非**本会话）。本棒之核对源**取自目标目录**，⛔ **0 读取近邻目录**。
- **窗口口径**：本批应录＝派工指定之 **2 张目标卡**（轮53～轮54）——**本件非全表扫描之应录全集**，系**指定目标行**之逐字转录（沿「库读取限 `questionnaire_requests` 目标行」之派工纪律）。
  - ⚠ **活库声明**：运行时库为**活库**，本件之读得时点即收录截止时点；库中或含他卡（含新建未答卡）——⛔ **不属本件应录面**，⛔ 0 转录（身份面实测枚举见 §2.5 第 7 条；三次读时点之状态漂移见 §2.5 第 5 条）。
  - ⚠ **活库较第八批之变动**：第八批落册读时点全表 **423** 行（`answered=420／pending=1／superseded=2`）；本批读时点全表 **425** 行（`answered`=423／`pending`=0／`superseded`=2）——其差为第八批之后另建之卡，**⛔ 0 超出派工指定 2 卡转录**。⚠ 第八批之账目面引用**以补正件 `a651f76a6547` 为准**（见 §2.5 第 2 条）。
- **转录纪律**：**逐字、0 省略、0 解释、0 判读**。题面（`request_json.steps` 之 id／header／question／options／selectionMode／required／allowOther／otherPlaceholder）与答文（`reply_payload` 全文，含 `selectedOptionIds`／`selectedOther`／`otherText`）均按库中原文照录；本件**不含**任何分析、结论、裁断或建议。
- **效力声明**：本件**仅转录**。⛔ **0 当「裁录」**；⛔ **0 代替任何既有登记件的裁录效力**。本件不产生、不替代、不撤销任何裁决；一切裁断效力仍以其原登记件／生效件为准（轮53卡之效力面另由姊妹件承载，§2.3 第 3 条）。
- **命名合规**：`_主题_日期` 体例；⛔ 0 带 V-阶段前缀（0 `_v3_`／`_v4_`／`_v5_`）。沿既有 `_supplement_` 续编体例（第一批 → `_supplement_` → `_supplement_2_` → `_supplement_3_` → `_supplement_4_` → `_supplement_5_` → `_supplement_6_` → `_supplement_7_` → 本件 `_supplement_8_`）；⛔ 0 占用他件之勘正支命名（`_…_correction_`）。
- **版式**：UTF-8 无 BOM · LF（CRLF ＝ 0）｜**R4**：key 永不明文（本棒 0 读 key／0 读 `.env`／0 落盘凭据）｜**0 网络 · 0 skill · 0 LLM · 0 实验**。
- **编制方式**：程序化逐字转录（⛔ 0 人工改写任何字面）；落盘后实测复核（版式与指纹见 §3；自身更正之如实登记见 §3.1）。

---

## 0 · 本轮读取基准（provenance）

- 库文件大小（读得时点）：`474,656,768` bytes
- 库文件 mtime（`stat` 时点，CST）：`2026-10-10 17:50:54.329 +0800`
- WAL 面注记：读得时点 `runtime-state.sqlite-wal` ＝ **5,018,192** bytes；⛔ 本棒**未触发** checkpoint、**0 写入**（主文件 mtime 与计数之关系、三读时点状态漂移见 §2.5 第 5 条）
- 表 `questionnaire_requests` 总行数（全表，本棒实测）：**425**
- 全表 status 分布（全表实测）：`answered`=423；`pending`=0；`superseded`=2；
- 抽取口径：`SELECT ... FROM questionnaire_requests WHERE request_id IN (`ask_9bb02f1b68a419c8855fef60`, `ask_13c6f24eb02ba5b8de3e21af`)`（**指定目标行**，⛔ 0 全表内容扫描、⛔ 0 LIMIT 截断）；命中 **2**／2。
- 排序口径：两目标行按表列 `created_at` **升序**呈现（轮53 → 轮54），⛔ 0 按 `request_id` 字面序另排。
- 时间换算口径：`created_at`／`answered_at`／`submittedAt`／`injected_at`／`createdAt` 均为 **INTEGER epoch 毫秒**，本件统一换算为 **CST（UTC+8）** 呈现，原值同时照录。
- 值形口径：SQL 空值一律呈为 `NULL`；布尔值一律呈为 JSON 小写字面 `true`／`false`；空数组呈为 `[]`（沿前八批体例）。⚠ **本批选项含 `description` 键**（与第八批之「（无此键）」不同）——本件**照录**其原文。
- **复核核对口径**：本件另以会话消息面 `messages.jsonl` 按各 `ask_…` requestId 检索卡片呈递与答复段落，作独立交叉核对源；两次读得时点指纹与命中行集合见 §2.2（⛔ 本件以运行时库为**第一源**、消息面**仅作旁证**）。
- **落前撞名实测**：见 §3.2（`Test-Path` ＝ **false**；同名 glob 命中 **0**）。

## 1 · 逐卡转录（指定目标 2 件，按 `created_at` 升序）

### 01 · `ask_9bb02f1b68a419c8855fef60` · 轮53（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> deposon 轮53 卡 · 重判面预登记四题（候裁）

**卡级元数据（原文照录）**

```text
request_id                     = ask_9bb02f1b68a419c8855fef60
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = deposon 轮53 卡 · 重判面预登记四题（候裁）
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName             = mavis
requester.runId                 = turn_36b129db-fcae-486c-9d76-60a6ac87a26f
requester.sessionId             = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId            = call_01_rZwm4TX3hDKYEpHW76pW1688
request_json.createdAt (epoch ms)= 1791621647598   → 2026-10-10 16:40:47.598 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791621647598
created_at (CST 换算)            = 2026-10-10 16:40:47.598 +0800
answered_at (epoch ms)         = 1791622063018
answered_at (CST 换算)           = 2026-10-10 16:47:43.018 +0800
reply_payload.submittedAt(epoch ms)= 1791622063018   → 2026-10-10 16:47:43.018 +0800
injected_at (epoch ms)         = 1791622074241
injected_at (CST 换算)           = 2026-10-10 16:47:54.241 +0800
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／12 选项，原文照录）**

**题 1／4** — `id` = `e_rj_1`

- `header`（原文照录）：`E-RJ-① 冻结核准`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
重判面预登记 K-RJ-1…K-RJ-11 十一条判死线是否照此冻结生效？（生效即锁·冻后 0 改；须先于任何重判实跑——本条为 S0 必过门；条文全文见 results/_g5_rejudgment_face_prereg_2026_10_10.md §3-1）
```

`options`（逐字原文，共 3 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·照此冻结生效（生效即锁·冻后 0 改）```
  - `description`（逐字原文）：```K-RJ-1…K-RJ-11＋LIM-A′ 即行冻结（S0 闭）；重判链待触发量口径与 C 适用性落定后按 S1–S7 启动```
- `id` = `yi`
  - `label`（逐字原文）：```乙·先修后生效（请列修改项）```
  - `description`（逐字原文）：```指出须修订之条项；修订后另行确认再生效```
- `id` = `bing`
  - `label`（逐字原文）：```丙·暂不生效（维持候复核）```
  - `description`（逐字原文）：```重判链维持停发；预登记保持待复核状态```

**题 2／4** — `id` = `e_rj_2`

- `header`（原文照录）：`E-RJ-② 触发量口径`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
重判面之触发量口径择何？（K-RJ-4 候闭·须 PI 给值；⛔ 不得沿用 A′——LIM-A′ 已登记其对位移 9/9 无分辨力；候选与代价详见该预登记 §2.4-2）
```

`options`（逐字原文，共 3 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·触发量＝A 线之差（100% 构造内生·近乎恒真）```
  - `description`（逐字原文）：```代价：同一构造族下 A 恒动 ⇒ 判别力存疑```
- `id` = `yi`
  - `label`（逐字原文）：```乙·触发量＝T1-only 对照面之差（证据仅 2 件·受物理分离限制）```
  - `description`（逐字原文）：```须先解其「0 供下游直接引用」限制（即 E-RJ-④）```
- `id` = `bing`
  - `label`（逐字原文）：```丙·PI 另给第三口径（盘上 0 候选）```
  - `description`（逐字原文）：```若择丙，请给出该口径字面（卡内『其他』栏亦可直接写入）```

**题 3／4** — `id` = `e_rj_3`

- `header`（原文照录）：`E-RJ-③ C 适用性落裁`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
C 三段式（N*＝3 定死·T4 不计入·类型段·否决段）于重判面构造域之适用性落裁：沿用／改／另立＝？（重核归 protocol 先行留痕·落裁归 PI；详见该预登记 §5-1 E-RJ-③）
```

`options`（逐字原文，共 3 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·沿用（C 三段式于重判面适用）```
  - `description`（逐字原文）：```protocol 照出重核件留痕（K-RJ-3 以重核落盘＋本裁并记）；⛔ 0 回改 C 字面```
- `id` = `yi`
  - `label`（逐字原文）：```乙·改（需另给改动字面）```
  - `description`（逐字原文）：```请给改动字面或范围；落改另行出件```
- `id` = `bing`
  - `label`（逐字原文）：```丙·另立（重判面另立新判据）```
  - `description`（逐字原文）：```候 PI 另给纲要；C 本体 0 动```

**题 4／4** — `id` = `th_v3_19_2`

- `header`（原文照录）：`TH-v3-19② 落盘 schema`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
未来同类落盘之 th_v3_19_compliance，是否改为按「豁免后判读面（5 项）」计算、并另置「全 12 项面」原始读数于他字段？（v3r1 面该布尔现为硬编码字面；改之须触既有产出约定；详见 results/_e6_th_v3_19_alignment_register_2026_10_10.md §4 出口②）
```

`options`（逐字原文，共 3 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·改：判读面（5 项）计算＋全 12 项原始读数另置他字段```
  - `description`（逐字原文）：```未来同类落盘适用；既有落盘值 0 回改```
- `id` = `yi`
  - `label`（逐字原文）：```乙·维持现状（全 12 项机械施门）```
  - `description`（逐字原文）：```false 如实落盘＋note 解释之现制保留```
- `id` = `bing`
  - `label`（逐字原文）：```丙·暂缓另议（统一落盘规范时并议）```
  - `description`（逐字原文）：```维持现制；待后续统一规范```

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_9bb02f1b68a419c8855fef60","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"e_rj_1","question":"重判面预登记 K-RJ-1…K-RJ-11 十一条判死线是否照此冻结生效？（生效即锁·冻后 0 改；须先于任何重判实跑——本条为 S0 必过门；条文全文见 results/_g5_rejudgment_face_prereg_2026_10_10.md §3-1）","selectionMode":"single","options":[{"id":"jia","label":"甲·照此冻结生效（生效即锁·冻后 0 改）","description":"K-RJ-1…K-RJ-11＋LIM-A′ 即行冻结（S0 闭）；重判链待触发量口径与 C 适用性落定后按 S1–S7 启动"},{"id":"yi","label":"乙·先修后生效（请列修改项）","description":"指出须修订之条项；修订后另行确认再生效"},{"id":"bing","label":"丙·暂不生效（维持候复核）","description":"重判链维持停发；预登记保持待复核状态"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-RJ-① 冻结核准"},{"id":"e_rj_2","question":"重判面之触发量口径择何？（K-RJ-4 候闭·须 PI 给值；⛔ 不得沿用 A′——LIM-A′ 已登记其对位移 9/9 无分辨力；候选与代价详见该预登记 §2.4-2）","selectionMode":"single","options":[{"id":"jia","label":"甲·触发量＝A 线之差（100% 构造内生·近乎恒真）","description":"代价：同一构造族下 A 恒动 ⇒ 判别力存疑"},{"id":"yi","label":"乙·触发量＝T1-only 对照面之差（证据仅 2 件·受物理分离限制）","description":"须先解其「0 供下游直接引用」限制（即 E-RJ-④）"},{"id":"bing","label":"丙·PI 另给第三口径（盘上 0 候选）","description":"若择丙，请给出该口径字面（卡内『其他』栏亦可直接写入）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-RJ-② 触发量口径"},{"id":"e_rj_3","question":"C 三段式（N*＝3 定死·T4 不计入·类型段·否决段）于重判面构造域之适用性落裁：沿用／改／另立＝？（重核归 protocol 先行留痕·落裁归 PI；详见该预登记 §5-1 E-RJ-③）","selectionMode":"single","options":[{"id":"jia","label":"甲·沿用（C 三段式于重判面适用）","description":"protocol 照出重核件留痕（K-RJ-3 以重核落盘＋本裁并记）；⛔ 0 回改 C 字面"},{"id":"yi","label":"乙·改（需另给改动字面）","description":"请给改动字面或范围；落改另行出件"},{"id":"bing","label":"丙·另立（重判面另立新判据）","description":"候 PI 另给纲要；C 本体 0 动"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-RJ-③ C 适用性落裁"},{"id":"th_v3_19_2","question":"未来同类落盘之 th_v3_19_compliance，是否改为按「豁免后判读面（5 项）」计算、并另置「全 12 项面」原始读数于他字段？（v3r1 面该布尔现为硬编码字面；改之须触既有产出约定；详见 results/_e6_th_v3_19_alignment_register_2026_10_10.md §4 出口②）","selectionMode":"single","options":[{"id":"jia","label":"甲·改：判读面（5 项）计算＋全 12 项原始读数另置他字段","description":"未来同类落盘适用；既有落盘值 0 回改"},{"id":"yi","label":"乙·维持现状（全 12 项机械施门）","description":"false 如实落盘＋note 解释之现制保留"},{"id":"bing","label":"丙·暂缓另议（统一落盘规范时并议）","description":"维持现制；待后续统一规范"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"TH-v3-19② 落盘 schema"}],"status":"pending","createdAt":1791621647598,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"turn_36b129db-fcae-486c-9d76-60a6ac87a26f","toolCallId":"call_01_rZwm4TX3hDKYEpHW76pW1688"},"title":"deposon 轮53 卡 · 重判面预登记四题（候裁）"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_9bb02f1b68a419c8855fef60","answers":[{"stepId":"e_rj_1","selectedOptionIds":["jia"],"selectedOther":false},{"stepId":"e_rj_2","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"},{"stepId":"e_rj_3","selectedOptionIds":[],"selectedOther":true,"otherText":"另议"},{"stepId":"th_v3_19_2","selectedOptionIds":["jia"],"selectedOther":false}],"submittedAt":1791622063018}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `e_rj_1`：`selectedOptionIds` = ["jia"]；`selectedOther` = false
答 2／4 — `stepId` = `e_rj_2`：`selectedOptionIds` = []；`selectedOther` = true；`otherText` = `另议`
答 3／4 — `stepId` = `e_rj_3`：`selectedOptionIds` = []；`selectedOther` = true；`otherText` = `另议`
答 4／4 — `stepId` = `th_v3_19_2`：`selectedOptionIds` = ["jia"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → 同 `stepId` 之 `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `e_rj_1`：`jia` → 选项字面（逐字）= `甲·照此冻结生效（生效即锁·冻后 0 改）`
- 答 2／4 — `e_rj_2`：**Other 通道**（`selectedOptionIds` 为空数组、`selectedOther` = true）→ `otherText`（逐字）= `另议`；⛔ **0 对取任何 `options[].label`**（该答未选任何选项 id）
- 答 3／4 — `e_rj_3`：**Other 通道**（`selectedOptionIds` 为空数组、`selectedOther` = true）→ `otherText`（逐字）= `另议`；⛔ **0 对取任何 `options[].label`**（该答未选任何选项 id）
- 答 4／4 — `th_v3_19_2`：`jia` → 选项字面（逐字）= `甲·改：判读面（5 项）计算＋全 12 项原始读数另置他字段`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 12 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |


---

## 1 · 逐卡转录（指定目标 2 件，按 `created_at` 升序）

### 02 · `ask_13c6f24eb02ba5b8de3e21af` · 轮54（派工指定目标行 · 逐字全量收录）

**卡题（`request_json.title`，原文照录）：**

> deposon 轮54 卡 · G5 重判面终裁组

**卡级元数据（原文照录）**

```text
request_id                     = ask_13c6f24eb02ba5b8de3e21af
status（表列 questionnaire_requests.status）= answered
status（request_json 内嵌，建卡时快照）  = pending
mode                           = questionnaire
schemaVersion                  = 2
title                          = deposon 轮54 卡 · G5 重判面终裁组
presentation.allowBackNavigation= true
presentation.replaceComposer   = true
presentation.showProgress      = true
requester.agentName             = mavis
requester.runId                 = 6c9d0b1c-b33a-4ebf-9ab8-dcc9b8fd3c91
requester.sessionId             = mvs_bbeb804b1a6a41109be740636eed1709
requester.toolCallId            = call_01_G8dpZtbRYKNQQy9MNPof6815
request_json.createdAt (epoch ms)= 1791624400837   → 2026-10-10 17:26:40.837 +0800
session_id                     = mvs_bbeb804b1a6a41109be740636eed1709
agent_name                     = mavis
msg_id                         = NULL
created_at (epoch ms)          = 1791624400837
created_at (CST 换算)            = 2026-10-10 17:26:40.837 +0800
answered_at (epoch ms)         = 1791624806780
answered_at (CST 换算)           = 2026-10-10 17:33:26.780 +0800
reply_payload.submittedAt(epoch ms)= 1791624806780   → 2026-10-10 17:33:26.780 +0800
injected_at (epoch ms)         = 1791624806849
injected_at (CST 换算)           = 2026-10-10 17:33:26.849 +0800
dismissed_at (epoch ms)        = NULL
origin_channel_context_json    = NULL
```

**题面逐字（`request_json.steps`，共 4 步／13 选项，原文照录）**

**题 1／4** — `id` = `erj3_0`

- `header`（原文照录）：`E-RJ-③-⓪ 构造前置`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
重判面相对本轮构造：变更／不变更？（先于三择一——不变更则读数逐位复现、C 三段式三择一皆空转、重判 0 新证据；来源：重核件 results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md §6）
```

`options`（逐字原文，共 3 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·变更构造（须另定变更要素与范围）```
  - `description`（逐字原文）：```触发构造域声明失效 ⇒ K-RJ-3 重核＋链重启；变更要素（词表／分母／gold 口径／留出集任一）候 PI 给字面或另令```
- `id` = `yi`
  - `label`（逐字原文）：```乙·不变更构造（知悉：三择一空转、重判 0 新证据）```
  - `description`（逐字原文）：```知悉：C 三择一皆空转、重判 0 新证据；G5 出路另议（⛔ 0 代拟）```
- `id` = `bing`
  - `label`（逐字原文）：```丙·另议```
  - `description`（逐字原文）：```重判链维持停发，候 PI 另定```

**题 2／4** — `id` = `erj3_1`

- `header`（原文照录）：`E-RJ-③-① C 三择一`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
C 三段式于重判面构造域之落裁：沿用／改／另立＝？（重核推荐乙·改；若前题择『不变更』则三案同落空；来源：重核件 §6 E-RJ-③-①）
```

`options`（逐字原文，共 3 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·沿用（⛔ ④ 复制缺陷 ⇒ 空转）```
  - `description`（逐字原文）：```C 原样适用于重判面；已知否决段对位移无分辨力（A′ 9/9 恒 0）将复制```
- `id` = `yi`
  - `label`（逐字原文）：```乙·改（①②③沿用、④改押触发量）```
  - `description`（逐字原文）：```改押之量＝本卡第 3 题（TRJ-1）；⛔ 0 修订 C 之字面（X-2 维持）```
- `id` = `bing`
  - `label`（逐字原文）：```丙·另立（弃三段式·另立门柱）```
  - `description`（逐字原文）：```须 PI 另给纲要；重核反方之一所指方向```

**题 3／4** — `id` = `trj1`

- `header`（原文照录）：`TRJ-1 触发量口径`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
重判面之触发量口径择何？（K-RJ-4 候闭；判断件倾向乙；来源：判断件 results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md §9）
```

`options`（逐字原文，共 4 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·A 线之差（可核性最强·判别力为 0）```
  - `description`（逐字原文）：```其指示与『gold 是否变动』26/26 恒等 ⇒ 对『位移是否实质』无分辨力```
- `id` = `yi`
  - `label`（逐字原文）：```乙·T1-only 对照面之差（信息性较强）```
  - `description`（逐字原文）：```须先解 V-CLAUSE-1.4 引用限制（＝TRJ-2/E-RJ-④）＋须先补逐件层；边际实为 3 件净额（含 D8-27 反向 −0.2）```
- `id` = `bing`
  - `label`（逐字原文）：```丙·另给第三口径（拟案 R3 覆盖率口径候给字面）```
  - `description`（逐字原文）：```R3＝读数面覆盖 9/24＝37.5%；⚠ 其改变否决轴所测之物（TRJ-4 授权）```
- `id` = `ding`
  - `label`（逐字原文）：```丁·判『构造内生』本身致命 ⇒ 转构造变更```
  - `description`（逐字原文）：```须 PI 明示＋K-RJ-3 重核（与首题『变更构造』轨同向）```

**题 4／4** — `id` = `erj3_2`

- `header`（原文照录）：`E-RJ-③-② 段一分母`
- `selectionMode`（原文照录）：`single`
- `required`（原文照录）：`true`
- `allowOther`（原文照录）：`true`
- `otherPlaceholder`（原文照录）：`Others...`

`question`（逐字原文）：

```text
C 段一之分母在重判面取何口径？（⚠ 口径问题·⛔ 非调 N* 之值；来源：重核件 §6 E-RJ-③-②）
```

`options`（逐字原文，共 3 项）：

- `id` = `jia`
  - `label`（逐字原文）：```甲·全语料 179 行面（本轮 24 件）```
  - `description`（逐字原文）：```与面 II 计数面一致；含 held-out 外 15 件```
- `id` = `yi`
  - `label`（逐字原文）：```乙·K-RJ-9 限域之 held-out 内（上限 9）```
  - `description`（逐字原文）：```与面域纪律（0 纳入 held-out 外）一致；可数上限 9```
- `id` = `bing`
  - `label`（逐字原文）：```丙·PI 另给```
  - `description`（逐字原文）：```请给字面```

<details><summary>题面原始 `request_json`（整串逐字照录，未改格式）</summary>

```json
{"schemaVersion":2,"id":"ask_13c6f24eb02ba5b8de3e21af","mode":"questionnaire","presentation":{"replaceComposer":true,"showProgress":true,"allowBackNavigation":true},"steps":[{"id":"erj3_0","question":"重判面相对本轮构造：变更／不变更？（先于三择一——不变更则读数逐位复现、C 三段式三择一皆空转、重判 0 新证据；来源：重核件 results/_g5_rejudgment_c_applicability_recheck_2026_10_10.md §6）","selectionMode":"single","options":[{"id":"jia","label":"甲·变更构造（须另定变更要素与范围）","description":"触发构造域声明失效 ⇒ K-RJ-3 重核＋链重启；变更要素（词表／分母／gold 口径／留出集任一）候 PI 给字面或另令"},{"id":"yi","label":"乙·不变更构造（知悉：三择一空转、重判 0 新证据）","description":"知悉：C 三择一皆空转、重判 0 新证据；G5 出路另议（⛔ 0 代拟）"},{"id":"bing","label":"丙·另议","description":"重判链维持停发，候 PI 另定"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-RJ-③-⓪ 构造前置"},{"id":"erj3_1","question":"C 三段式于重判面构造域之落裁：沿用／改／另立＝？（重核推荐乙·改；若前题择『不变更』则三案同落空；来源：重核件 §6 E-RJ-③-①）","selectionMode":"single","options":[{"id":"jia","label":"甲·沿用（⛔ ④ 复制缺陷 ⇒ 空转）","description":"C 原样适用于重判面；已知否决段对位移无分辨力（A′ 9/9 恒 0）将复制"},{"id":"yi","label":"乙·改（①②③沿用、④改押触发量）","description":"改押之量＝本卡第 3 题（TRJ-1）；⛔ 0 修订 C 之字面（X-2 维持）"},{"id":"bing","label":"丙·另立（弃三段式·另立门柱）","description":"须 PI 另给纲要；重核反方之一所指方向"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-RJ-③-① C 三择一"},{"id":"trj1","question":"重判面之触发量口径择何？（K-RJ-4 候闭；判断件倾向乙；来源：判断件 results/_g5_rejudgment_trigger_caliber_judgment_2026_10_10.md §9）","selectionMode":"single","options":[{"id":"jia","label":"甲·A 线之差（可核性最强·判别力为 0）","description":"其指示与『gold 是否变动』26/26 恒等 ⇒ 对『位移是否实质』无分辨力"},{"id":"yi","label":"乙·T1-only 对照面之差（信息性较强）","description":"须先解 V-CLAUSE-1.4 引用限制（＝TRJ-2/E-RJ-④）＋须先补逐件层；边际实为 3 件净额（含 D8-27 反向 −0.2）"},{"id":"bing","label":"丙·另给第三口径（拟案 R3 覆盖率口径候给字面）","description":"R3＝读数面覆盖 9/24＝37.5%；⚠ 其改变否决轴所测之物（TRJ-4 授权）"},{"id":"ding","label":"丁·判『构造内生』本身致命 ⇒ 转构造变更","description":"须 PI 明示＋K-RJ-3 重核（与首题『变更构造』轨同向）"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"TRJ-1 触发量口径"},{"id":"erj3_2","question":"C 段一之分母在重判面取何口径？（⚠ 口径问题·⛔ 非调 N* 之值；来源：重核件 §6 E-RJ-③-②）","selectionMode":"single","options":[{"id":"jia","label":"甲·全语料 179 行面（本轮 24 件）","description":"与面 II 计数面一致；含 held-out 外 15 件"},{"id":"yi","label":"乙·K-RJ-9 限域之 held-out 内（上限 9）","description":"与面域纪律（0 纳入 held-out 外）一致；可数上限 9"},{"id":"bing","label":"丙·PI 另给","description":"请给字面"}],"allowOther":true,"otherPlaceholder":"Others...","required":true,"header":"E-RJ-③-② 段一分母"}],"status":"pending","createdAt":1791624400837,"requester":{"sessionId":"mvs_bbeb804b1a6a41109be740636eed1709","agentName":"mavis","runId":"6c9d0b1c-b33a-4ebf-9ab8-dcc9b8fd3c91","toolCallId":"call_01_G8dpZtbRYKNQQy9MNPof6815"},"title":"deposon 轮54 卡 · G5 重判面终裁组"}
```

</details>

**答文逐字（`reply_payload` 全文，原样照录）**

```json
{"schemaVersion":2,"requestId":"ask_13c6f24eb02ba5b8de3e21af","answers":[{"stepId":"erj3_0","selectedOptionIds":["bing"],"selectedOther":false},{"stepId":"erj3_1","selectedOptionIds":["yi"],"selectedOther":false},{"stepId":"trj1","selectedOptionIds":["yi"],"selectedOther":false},{"stepId":"erj3_2","selectedOptionIds":["jia"],"selectedOther":false}],"submittedAt":1791624806780}
```

**答文逐字（逐条展开，原文照录）**

答 1／4 — `stepId` = `erj3_0`：`selectedOptionIds` = ["bing"]；`selectedOther` = false
答 2／4 — `stepId` = `erj3_1`：`selectedOptionIds` = ["yi"]；`selectedOther` = false
答 3／4 — `stepId` = `trj1`：`selectedOptionIds` = ["yi"]；`selectedOther` = false
答 4／4 — `stepId` = `erj3_2`：`selectedOptionIds` = ["jia"]；`selectedOther` = false

**答文回指（机械展开：由同一行 `selectedOptionIds` → 同 `stepId` 之 `options[].label` 逐字对取；本表不含任何判读或结论）**

- 答 1／4 — `erj3_0`：`bing` → 选项字面（逐字）= `丙·另议`
- 答 2／4 — `erj3_1`：`yi` → 选项字面（逐字）= `乙·改（①②③沿用、④改押触发量）`
- 答 3／4 — `trj1`：`yi` → 选项字面（逐字）= `乙·T1-only 对照面之差（信息性较强）`
- 答 4／4 — `erj3_2`：`jia` → 选项字面（逐字）= `甲·全语料 179 行面（本轮 24 件）`

**题面／答文计数（逐字转录 0 失败核验）**

| 项 | 实测 |
|---|---:|
| `steps` 数 | 4 |
| `options` 总数 | 13 |
| `answers` 数 | 4 |
| 转录失败项 | **0** |

---

## 2 · 对账（**0 漏录 · 0 重复 · 0 掩饰**）

| 序 | `request_id` | 轮 | 批次口径 | `created_at`（CST） | `answered_at`（CST） | `status` | 前八批落册件是否已含 |
|---:|---|---|---|---|---|---|---|
| 1 | `ask_9bb02f1b68a419c8855fef60` | 轮53 | 续录（第八批之后新增轮次） | 2026-10-10 16:40:47.598 +0800 | 2026-10-10 16:47:43.018 +0800 | `answered` | ⛔ 未含（实测·见 §2.5 第 1 条） |
| 2 | `ask_13c6f24eb02ba5b8de3e21af` | 轮54 | 续录（第八批之后新增轮次） | 2026-10-10 17:26:40.837 +0800 | 2026-10-10 17:33:26.780 +0800 | `answered` | ⛔ 未含（实测·见 §2.5 第 1 条） |

⇒ **2／2 件转录完成、0 失败**；逐字转录之 `steps` 合计 **8** 步、`options` 合计 **25** 项、`answers` 合计 **8** 条。

### 2.1 本批版本号核定（实测）

盘上存在八件 `_questionnaire_cards_intake_register*_2026_10_10.md` 转录登记件（`_supplement_7_` 已于本棒之前存在，另另有其账目补正件 `_…_correction_`，⛔ **0 占批次序号**）；故取**首个未用序号** ＝ **`_supplement_8_`。落前实测：`Test-Path` ＝ **false**；全仓同名 glob 命中 **0**；`results/*supplement_8*` glob 命中 **0** ⇒ ✅ **新名新建 · 0 覆写 · 0 重名**。

### 2.2 交叉核对（独立第二源：会话消息面 `messages.jsonl`）

本件另以会话消息面按两个 `ask_…` requestId 检索，独立于运行时库**交叉核对**卡答（**0 判读 · 0 补写**）：

| 卡 | 消息面命中 | 关键证据 | 与库内 `reply_payload` 之关系 |
|---|---|---|---|
| 轮53 `ask_9bb02f1b68a419c8855fef60` | **14** 行（L31／L32／L35／L38／L43／L44／L47／L49／L52／L57／L83／L86／L101／L108） | L31 `toolResult·ask_user` 呈 `step_count=4`、`waiting_for_user=true`（timestamp 1791621647883）；**L47 `role=user` 之 `<questionnaire-response>` 逐字载**：`submittedAt`＝`1791622063018`；`e_rj_1`→`jia`；`e_rj_2`→`selectedOther=true`＋`otherText`＝`另议`；`e_rj_3`→`selectedOther=true`＋`otherText`＝`另议`；`th_v3_19_2`→`jia` | ✅ **四答逐位相符**（含两条 Other 之 `otherText`），**0 分歧** |
| 轮54 `ask_13c6f24eb02ba5b8de3e21af` | **4** 行（L104／L105／L107／L108） | L104 `toolResult·ask_user` 呈 `step_count=4`、`waiting_for_user=true`（timestamp 1791624407071）；**L107 `role=user` 之 `<questionnaire-response>` 逐字载**：`submittedAt`＝`1791624806780`；`erj3_0`→`bing`；`erj3_1`→`yi`；`trj1`→`yi`；`erj3_2`→`jia` | ✅ **四答逐位相符**，**0 分歧** |

📌 **回指标签面之旁证（机械对取之独立确认）**：消息面呈递回执于答后另给「Q／A」渲染行，其 `A:` 行字面与本件 §1 之机械回指**逐位相符** —— 轮53 之 `A:` 依次为 `甲·照此冻结生效（生效即锁·冻后 0 改）`／`其他: 另议`／`其他: 另议`／`甲·改：判读面（5 项）计算＋全 12 项原始读数另置他字段`；轮54 之 `A:` 依次为 `丙·另议`／`乙·改（①②③沿用、④改押触发量）`／`乙·T1-only 对照面之差（信息性较强）`／`甲·全语料 179 行面（本轮 24 件）` ⇒ **选项 id ↔ label 之映射经第二源确认**（本件**仅照录**，⛔ 0 因旁证而改动库内任一字）。

⚠ **序列化形态之如实差异（非内容差异）**：消息面以 XML 式 `<questionnaire-response>` 承载答文且非 ASCII 处作转义，故紧凑 JSON 探针 `"otherText":"另议"` 于消息面**命中 0**；⛔ 本件**不以此 0 命中判为内容不符**，改以 XML 节点 `otherText` 逐字命中为准（见上表）。

📌 **消息面两次读时点之漂移（如实登记 · 0 掩饰）**：首次读得 **1,527,839** bytes／SHA-12 `7fd3095d7206`；核对时再读得 **1,532,678** bytes／SHA-12 `de244e545a73`（活面追加）。两读时点**命中行集合逐位相同**（轮53 ＝ 14 行、轮54 ＝ 4 行，行号一致）⇒ 字节增长源自他行，**不涉两卡之核对结论**。

### 2.3 本件之边界（诚实交代）

1. **本件非全表应录全集** —— 系派工指定之 **2 张目标卡**（轮53～轮54）之逐字转录；⛔ **0 声称已覆盖本轮新建之全部卡**。实测全表 **425** 行，本件仅转录其中 2 行；其余额 **423** 行**未**在本件应录面。
2. **轮49～轮52 已由第八批收录** —— 实测该四张卡已完整收录于 `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md`（SHA-12 `1fb8eac82781`）之 §1；本件⛔ **0 重复转录**，⛔ **0 回改**该件。
3. **轮53卡之首次落册收录** —— 经账目补正件 `a651f76a6547` §4 之明示（「轮53卡之登记面 0 代为处置……转录与否属另一登记序列之裁量」）及本棒全仓 id 命中实测（§2.5 第 1 条）：该卡**从未被任何落册批次逐字转录** ⇒ 本件**为其首次落册逐字收录**；其**效力面**另已由姊妹件登记（`results/_round53_rejudge_prereg_freeze_effectivity_register_2026_10_10.md`、`results/_round53_th_v3_19_landfall_schema_effectivity_register_2026_10_10.md`）——**两序列并存、不相冲突**（落册＝字面；效力＝裁断），本件⛔ **0 复核**该二姊妹件之内容。
4. **本件 0 核他件之内部正确性** —— ⛔ 0 复核前八批落册登记件之内容；仅核其**存在性与 SHA-12**（本棒当轮实测，见 §3.3）。
5. **题面之实质裁定 0 预判** —— 本件仅照录 PI 之所选；⛔ 0 判读其所选之对错、⛔ 0 预判后续处置、⛔ 0 出五终判之一、⛔ 0 代裁。
6. **回指表之边界** —— §1 各卡「答文回指」小表仅为同一行 `selectedOptionIds` → 同 `stepId` 之 `options[].label` 之**机械字面对取**（⚠ 本批选项 id 为跨步复用之 `jia`／`yi`／`bing`／`ding`，故对取**必以 `(stepId, optionId)` 二元组**为准，⛔ 0 跨步取 label）；未作任何判读；若与逐字原文有冲突，以**原文**为准。
7. **Other 通道答文之呈现** —— 本批 **2** 答走 Other 通道（`selectedOptionIds` ＝ `[]` 且 `selectedOther` ＝ `true`）；其 `otherText` 已于 §1 逐条展开、§1 答文回指、§2.4 三处**逐字照录**；⛔ 本件**0 替任何 Other 答补填选项 id**、⛔ **0 以任何选项 label 替换 `otherText` 字面**。
8. **未转录之他卡（0 落盘其内容）** —— 见 §2.5 第 7 条之身份面实测枚举；本件**仅列其 `request_id` 与时点／状态**（账目核对所需），⛔ **0 转录其题面或答文一字**。

### 2.4 Other 通道答文一览（机械展开 · 逐字照录 `otherText`）

| 轮 | `stepId` | `otherText`（逐字原文） |
|---|---|---|
| 轮53 | `e_rj_2` | `另议` |
| 轮53 | `e_rj_3` | `另议` |

⇒ 本批 8 答之分布：**选项通道 6 答 ＋ Other 通道 2 答**（轮53：`jia`／Other「另议」／Other「另议」／`jia`；轮54：`bing`／`yi`／`yi`／`jia`）——与派工单所载**逐项相符、0 分歧**；此为**转录事实**，⛔ 非判读。

### 2.5 差异登记

**对派工转录清单之字面差异：0。** 派工指定 2 个 `request_id`（未附预期答文字面），故本件之核对面为「2 个 id 之命中与逐字保真」：实测命中 **2／2**；每卡 `steps`／`options`／`answers` 三计数与库内一致（见 §1 各卡计数表），转录失败项合计 **0**；四答分布与派工描述**逐项相符**。

**与既有登记件之关系（逐项实测）：**

1. **两卡均未见于前八批落册件之正文** —— 本棒全仓 id 命中实测：轮53 id 命中件 **5** 件、轮54 id 命中件 **2** 件；其中**落册族**（`*_questionnaire_cards_intake_register*`）**仅**账目补正件 `a651f76a6547` 命中，且该件**只载 id 与建卡／答毕时点（账目面）**、⛔ **0 载题面或答文正文** ⇒ 两卡于落册序列**首次逐字收录**（轮53卡另见 §2.3 第 3 条）。
2. **活库行数之变动（如实登记 · 沿补正面）** —— 第八批读时点全表 **423** 行；本批读时点全表 **425** 行（`answered`=423、`pending`=0、`superseded`=2）。实测 `created_at < 轮53卡建卡时点` 计 **422** 行、`created_at ≥ 之` 计 **3** 行（合计 425）。⚠ **引用规则**：第八批之账目面（419→423 之桥接断言）**以补正件 `a651f76a6547` §3 之「新旧并存·以新为准」为准**；原登记件 `1fb8eac82781` §2.4 第 2 条**原句一字不动、留存原状**，本件⛔ **0 追改、0 复述其已被补正之措辞**。
3. **本批 2 条 Other 通道（与第八批之 0 条不同）** —— 轮53之第 2、3 问以 `otherText`＝「另议」作答（`selectedOptionIds` 为空数组）；此为**转录事实**，⛔ **0 判读**其与同卡选项 `bing`（「丙·暂不生效（维持候复核）」／「丙·另立（重判面另立新判据）」）之关系 —— **库内字面即为「另议」，本件照录，不代其择定归入任何选项**。
4. **两卡 `status` 双读法** —— 表列 `status` 均为 `answered`，而 `request_json` 内嵌 `status` 均为 `pending`（建卡时快照）；本件二者**并列照录**（沿前八批体例），⛔ 0 择一改写。
5. **主文件 mtime 与计数之 WAL 面注记（如实登记）** —— 主库文件 mtime（`stat` 时点）为 **2026-10-10 17:50:54.329 +0800**；而本棒三次读时点所见之全表状态**有漂移**：读时点①（探查）**425** 行／`answered`=422、`pending`=1、`superseded`=2；读时点②（交叉核对时）同 **425** 行，其 `pending` 行 ＝ `ask_843b65b50a873462f8a56e80`（建卡 **2026-10-10 17:38:36.526 +0800**，`answered_at` ＝ `NULL`）；读时点③（**本件最终落盘时**）**425** 行／`answered`=423、`pending`=0、`superseded`=2 ⇒ 该行已答毕（`pending→answered`，其 `answered_at` ＝ **2026-10-10 17:40:50.668 +0800**）。**总行数 425 三读时点全程未变** ⇒ 此为**活库状态漂移**，⛔ **非**账目错误。**成因注记**：写入经 **WAL 面**可见（`runtime-state.sqlite-wal` 读得时点 **5,018,192** bytes，故主文件 mtime 滞后于行数变动）；⛔ 本棒**未触发 checkpoint**、⛔ **0 写入**。此项**仅涉读时点之记账基准**，⛔ **0 改写**任何既有件所载之时点。
6. **他棒临时件之如实注记** —— 本棒**早期**全仓检索曾命中仓根 `.tmp_r54_*` 若干他棒临时件；至本棒最终落盘时之全仓复扫，该等件已 **0 命中**（其间由其所属棒自行清理）——⛔ **本棒 0 删除、0 读取其内容以充转录、0 编辑／0 覆写／0 改名／0 移动**。本棒唯一写动作 ＝ 新建本件。
7. **第八批读时点之后新建之卡（身份面枚举 · ⛔ 0 转录其题面答文）** —— 实测 `created_at ≥ 轮52 建卡时点（2026-10-10 15:59:30.250 +0800）` 之全部行（**仅列 `request_id` 与时点／状态**，供账目核对；⛔ **0 落盘其题面或答文一字**）：

| # | `request_id` | 建卡（CST） | 答毕（CST） | `status` | 本件之处置 |
|---:|---|---|---|---|---|
| 1 | `ask_fd3083aa317b7b3397f85f7d` | 2026-10-10 15:59:30.250 +0800 | 2026-10-10 16:15:08.215 +0800 | `answered` | ⛔ **未转录**（不属派工指定应录面） |
| 2 | `ask_9bb02f1b68a419c8855fef60` | 2026-10-10 16:40:47.598 +0800 | 2026-10-10 16:47:43.018 +0800 | `answered` | ✅ **本件已逐字转录** |
| 3 | `ask_13c6f24eb02ba5b8de3e21af` | 2026-10-10 17:26:40.837 +0800 | 2026-10-10 17:33:26.780 +0800 | `answered` | ✅ **本件已逐字转录** |
| 4 | `ask_843b65b50a873462f8a56e80` | 2026-10-10 17:38:36.526 +0800 | 2026-10-10 17:40:50.668 +0800 | `answered` | ⛔ **未转录**（不属派工指定应录面） |

⇒ 枚举合计 **4** 行，其中本件转录 **2** 行、**未转录 2** 行（⛔ 依窗口口径 0 超出应录面）。⚠ 轮53卡之建卡行虽在本枚举内，其**落册转录**即为本件（首次收录，见 §2.3 第 3 条）；其未见于第八批**并非遗漏**，而系第八批读时点之应录面外（补正件 `a651f76a6547` §4 已明示）。

---

## 3 · 0 回改确认 ＋ 落盘自证

### 3.1 0 回改确认

| 项 | 确认 |
|---|---|
| 既有件写动作 | **0** —— ⛔ 0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除任何既有件（**含前八批落册登记件、其账目补正件与第七批回执**） |
| 本棒写动作 | **新增 1 件**（本件）＋ 系统临时目录（`%TEMP%`）内中间脚本／导出（**非交付件 · 非仓内** · 已于交付前清理） |
| 运行时库 | **只读**（`mode=ro`）—— 0 写入、0 修改、0 建表、0 提交、0 checkpoint |
| 会话消息面 | **只读**（仅 `messages.jsonl` 检索）—— 0 写入 |
| 派生 JSON | ⛔ **0 新建／0 合并**任何派生物 JSON |
| 本件交付前之自身更正 | **如实登记（非 0）**：本件首次生成后经**落盘实测复核**，发现 §2.5 之 WAL／状态项含一**因活库漂移而失效之 `pending` 断言**、并有一处交叉引用错指；该次生成件系**本棒自身之临时产物**，经 `rm --`（可恢复删除）清理后由生成器修正并**重新落盘**。**最终交付件之库内字面（§1 全部题面与答文）自始至终 0 处更动、0 人工改写**（逐字转录之保真性 0 受影响）；⛔ 本项 ⛔ **不冒充「0 次更正」** |
| 归档禁区 | **未触及** —— ⛔ 0 访问／0 读取 `〔归档区〕`（全仓检索时已显式跳过该路径） |

### 3.2 落前撞名实测

| 项 | 实测结果 |
|---|---|
| 落前撞名 | `Test-Path '_questionnaire_cards_intake_register_supplement_8_2026_10_10.md'` ＝ **false**；全仓同名 glob 命中 **0**；`results/*supplement_8*` glob 命中 **0** ⇒ ✅ **新名新建 · 0 覆写 · 0 重名** |

### 3.3 输入件指纹（本棒 `SHA256` **当轮实测** · **0 沿用他件登记值**）

| 件 | SHA-12 | 字节 | BOM | CRLF | 本件之关系 |
|---|---|---:|:--:|:--:|---|
| `results/_questionnaire_cards_intake_register_2026_10_09.md` | `d917180db36f` | 442,288 | 否 | 0 | **第一批落册登记件** |
| `results/_questionnaire_cards_intake_register_supplement_2026_10_09.md` | `193386b9f23c` | 72,199 | 否 | 0 | **第二批落册登记件** |
| `results/_questionnaire_cards_intake_register_supplement_2_2026_10_10.md` | `dc43e3cb7610` | 262,542 | 否 | 0 | **第三批落册登记件** |
| `results/_questionnaire_cards_intake_register_supplement_3_2026_10_10.md` | `11681f0ad861` | 67,225 | 否 | 0 | **第四批落册登记件** |
| `results/_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | `d6ff041a9df9` | 116,506 | 否 | 0 | **第五批落册登记件** |
| `results/_questionnaire_cards_intake_register_supplement_5_2026_10_10.md` | `edb57308170d` | 77,189 | 否 | 0 | **第六批落册登记件** |
| `results/_questionnaire_cards_intake_register_supplement_6_2026_10_10.md` | `95ba771fa760` | 106,453 | 否 | 0 |  |
| `results/_questionnaire_cards_intake_register_supplement_6_receipt_2026_10_10.md` | `0984955b0370` | 11,752 | 否 | 0 | **第七批回执**（回执面 · 体例参照） |
| `results/_questionnaire_cards_intake_register_supplement_7_2026_10_10.md` | `1fb8eac82781` | 52,602 | 否 | 0 | **第八批落册登记件**（本件之直接上承） |
| `results/_questionnaire_cards_intake_register_supplement_7_accounting_correction_2026_10_10.md` | `a651f76a6547` | 17,517 | 否 | 0 | 第八批账目补正件（账目面 · 引用以之为准） |

📌 **锚件指纹核验**：上表 10 件指纹**本棒当轮实测**，其中转录登记件八件 —— 第八批 `1fb8eac82781`／52,602 B；第七批 `95ba771fa760`／106,453 B；第六批 `edb57308170d`／77,189 B；第五批 `d6ff041a9df9`／116,506 B；第四批 `11681f0ad861`／67,225 B；第三批 `dc43e3cb7610`／262,542 B；第二批 `193386b9f23c`／72,199 B；第一批 `d917180db36f`／442,288 B；另计第八批账目补正件 `a651f76a6547`／17,517 B。**对照**：第八批 `1fb8eac82781`／52,602 B 与第七批 `95ba771fa760`／106,453 B 为补正件 §1 所载之自报值（**逐位相符**）；第八批 §3.3 所载七件（第一批～第七批）指纹与本棒实测**逐位相符** ⇒ **既有件触动数 ＝ 0**。

### 3.4 边界声明 · 0 编造

- **0 编造 PI 立场**：本件所载两卡之题面与答文**均取自运行时库原件**（程序化逐字转录，§1 之 `request_json`／`reply_payload` 为整串原文照录）；⛔ **0 推测** PI 对任何一项之将来处置。
- **0 冒充他棒**：本件由 **doc-writer** 出件（分支会话 `mvs_cf54be9d09d54516bd6bad49e1aff82d`）；⛔ 0 顶任何他方名头。⛔ 本件**不产生、不替代、不撤销**任何裁决；轮53卡之**效力面**另由姊妹件承载（§2.3 第 3 条），二者**并存不冲**。
- **0 网络 · 0 skill · 0 LLM · 0 实验**：本棒仅本机只读取证 ＋ 1 件新建。
- **R4**：⛔ 0 读 key、⛔ 0 读 `.env`、⛔ 0 落盘凭据、**key 永不明文**。
- **不编造专有名词／文献号／定理名**：本件**0 引用任何外部定理、文献或标准**；§1 所涉之盘上件名（`results/_g5_rejudgment_*`、`results/_e6_th_v3_19_alignment_register_2026_10_10.md` 等）均系**题面原文照录**之既有字面，⛔ 非本件所造。
- **体例锚之如实说明**：本件沿第八批登记件 `1fb8eac82781` 之全部栏目；⚠ **盘上并无「第八批回执」之独立成件**（`results/` 内回执族仅有第七批之 `_supplement_6_receipt_2026_10_10.md`，SHA-12 `0984955b0370`），故本件之**回执栏目体例**取自该第七批回执、**账目面口径**取自第八批补正件 `a651f76a6547` —— 此三项差异**如实登记**，⛔ **0 冒充已通读并不存在之件**。

**本件状态**：✅ **2 卡逐字转录完成 · 0 失败 · 0 判读 · 0 代裁 · 0 回改既有件** ｜ ⛔ 0 网络 · 0 skill · 0 LLM
