# G4 追因续棒 · runtime-state 记录面取证（2026-10-01 · 纯只读 · 出 1 件即停）

> **棒别**：G4 追因续棒（worker 棒；parent 于卷D 收官登记件 `results/_pack_d_closeout_register_2026_10_01.md` §4 序号 **7**／§5.6 派工）。
> **前件**：`results/_g4_skill_read_scope_trace_2026_10_01.md`（`9196a608bb0d` / 26,906 B / 2026-10-01 14:31:34）。
> **承接任务**：在前件「已闭 C1／C2／C4／C5 ＋ 已定位 C3 载体」基础上，**在盘可达面**（本机 runtime 安装目录／runtime-state 面／既定只读面）**补全证据链**。
> **版式**：UTF-8 无 BOM · LF · 去版本前缀（沿 PI 09-29 命名裁 ＋ 10-01 补记「派工建议名亦须合规」），⛔ 无 `_v5_` 类阶段字样。
> **写入面**：**仅本件 1 件**（本棒全部操作为内联只读 PowerShell／文件读取，⛔ **0 落盘 scratch 脚本**）。

---

## §0 只读面清单与 R4 声明

| 面 | 路径（运行时 `activeDataDir`／`%APPDATA%`／安装目录） | 读法 | 状态 |
|---|---|---|---|
| 会话目录旧面 | `<dataDir>\sessions\` | 递归枚举＋计数 | 只读，0 写 |
| 会话记录新面 | `<dataDir>\v2\sessions\` | 递归枚举＋按日聚合 | 只读，0 写 |
| 事件流面 | `<dataDir>\v2\observability\events\2026\` | 逐件计数＋JSON 结构解析 | 只读，0 写 |
| 全量 runtime 日志 | `<dataDir>\v2\observability\logs\runtime-*.log`（12 件） | 逐件 `Select-String` 计数＋行型判别 | 只读，0 写 |
| 应用日志面 | `%APPDATA%\minimax\logs\*.log`（12 件，含 `main-10-01.log` 326,336,812 B） | 同上＋**时序切分判别** | 只读，0 写 |
| 日志清除脚本面 | `%APPDATA%\minimax\log-purge.ps1`、`…\logs\truncate-main-0929.ps1` | 整件读取 | 只读，0 写 |
| 锚件面 | 前件 `9196a608bb0d`／`9f5b73620b8a`／`0f1f94df75ba` | 读＋`Get-FileHash` | 只读，0 写 |

### §0.1 R4 遵守声明

- 本棒**未打开、未读取** `config.yaml`（含 `apiKey` 等密钥字段，**值未读**）；**未读取** `mcp.json`、`local-runtime.auth.json`、`minimax-agent-cn-config.json`、`observability-outbox.jsonl` 等含值文件。
- 本件**不含**任何密钥／token／端点值；`<dataDir>` 与 `%APPDATA%\minimax` 路径均**由本机探测得出**，**0 由配置值推导**。
- 本棒**0 落盘**任何被读文件的字节内容（仅记录结构、字段名、计数与短片段；片段均为日志元数据，⛔ 未摘录任何对话正文）。

---

## §1 结论摘要（先给结论，再给证据）

| id | 命题 | 判定 | 依据强度 |
|---|---|---|---|
| **C1／C2／C4／C5** | 前件已闭四条 | ✅ **照录沿用**（本棒 **0 复测**） | 前件 `9196a608bb0d` §2–§5 |
| **C3‑cont** | `allowedSkillNames` 载体机制（前件 §4） | ✅ 机制沿用 ｜ ⚠️ **取值面判定升级**（见 §5） | 前件 §4 ＋ 本棒 D1–D6 |
| **D1** | 旧 `sessions\` 面**纯目录壳**：会话身份只在目录名，内容 0 | ✅ **闭** | 725 目录／递归文件 0／非空目录 0 |
| **D2** | 新 `v2\sessions` 记录面**不覆盖 G4 观察窗口** | ✅ **闭（当前盘上态）** | 09-24→09-30 全 0 文件 |
| **D3** | observability 事件流**零 skill 事件** | ✅ **闭** | 09-28/29/30/10-01 全部 0 命中 |
| **D4** | **全量应用日志面原生 skill 记录 ＝ 0**（100% 回显） | ✅ **闭**（三重判别） | 时序＋行型＋`sessionId` 归属 |
| **D5** | 会话轨迹日志**只记元数据、无响应体** | ✅ **闭** | 字段全表＋长度分布 |
| **D6** | G4 观察日日志**已被清除**（机制可查、非「未开启」） | ✅ **闭** | `log-purge.ps1` 逐字＋逐日实测 |
| **D7** | 存在本地端点 `GET /minimax-desktop/api/v1/runtime/skills`（候选取证面） | ⚠️ **未验**（本棒 **0 调用**） | transport 留痕 379 次／主日志 16 条 |

**一句话**：本棒在**盘上可达面**把 G4 的缺口从「需 runtime 记录」**收窄为可指名的两处结构性缺证**——① **两观察会话的 `allowedSkillNames` 原值在本机任何记录面都不产生**（不落盘，非「暂不可见」）；② **两观察会话的 skill 读结果不在任何日志面**（全量日志 0 tool 结果通道）。同时查明 **09-24→09-29 的日志已被 `log-purge.ps1` 依授权清除**（D6），而 **G4 观察日（09-30）的会话记录面为 0 文件**（D1／D2）。

⇒ **G4 仍未闭**：**以当前可读面不可审结**。⛔ **0 下因果结论**、⛔ **0 硬凑**；所差证据见 §6 清单（4 项 · 逐项给出打点位置）。

---

## §2 D1／D2：会话态记录面 —— 观察窗口无任何记录

### §2.1 旧面 `<dataDir>\sessions\`（目录名即 sessionId）

| 指标 | 实测值 |
|---|---|
| 目录数 | **725**（`mvs_*`） |
| 递归**文件**数 | **0** |
| **非空**目录数 | **0** |
| mtime 跨度 | **2026-09-24 → 2026-10-01** |
| 2026-09-30 当日目录数 | **30**（其中 15:39:13、15:59:17 两枚为 G4 窗口最近邻） |

⇒ **判定 D1**：该面**只承载会话身份（目录名），不承载任何内容**。**G4 的两观察会话**（`9f5b73620b8a` §3 G5 字面时点：父级成功 ≈15:2x、子会话实验 15:46 起，2026-09-30）在该面**0 内容**。

### §2.2 新面 `<dataDir>\v2\sessions\`（`YYYY\MM\DD\HH-mm-ss-mmm-session_bXZz…\`）

| 日目录 | session 目录数 | 文件数 |
|---|---|---|
| 09-01 | 10 | 1,265 |
| 09-03 | 6 | 65 |
| 09-15 | 5 | 20 |
| 09-16 | 8 | 32 |
| 09-29 | 2 | 10 |
| **09-24／09-26／09-27／09-28／30** | **0** | **0** |
| 其余 16 个日目录 | 0 | 0 |

单会话内容面实测结构（09-01 样本）：`messages.jsonl`／`manifest.json`／`history-catalog.json`／`user-message-locators.jsonl`／`snapshots\*.jsonl`（788 件 / 1,035,978,514 B）／`tool-outputs\`（427 件 / 6,511,553 B）——即**会话轨迹记录面本身是存在的**。

⇒ **判定 D2**：**G4 观察窗口（09-24→09-30）在新面 0 记录**；有记录的最近日为 **09-29**（10 件）、最早为 **09-16**。
⚠️ **口径限制**：此为**当前盘上态**；若运行时补写／迁移该窗口记录，本判定即失效——**条件性闭**，⛔ 不推广。

---

## §3 D3：事件流面 —— 零 skill 事件

### §3.1 全量计数（`v2\observability\events\2026\`）

| 文件 | 字节 | `skill` | `LocalSkill` | `readSkill` | `allowedSkillNames` | `plugin:` |
|---|---|---|---|---|---|---|
| `runtime-events-2026-09-28.1.jsonl` | 2,601,197 | **0** | 0 | 0 | 0 | 0 |
| `runtime-events-2026-09-29.jsonl` | 16,776,847 | **0** | 0 | 0 | 0 | 0 |
| `runtime-events-2026-09-29.1.jsonl` | 16,776,869 | **0** | 0 | 0 | 0 | 0 |
| `runtime-events-2026-09-29.2.jsonl` | 130,955 | **0** | 0 | 0 | 0 | 0 |
| `runtime-events-2026-09-30.jsonl` | 62,919 | **0** | 0 | 0 | 0 | 0 |
| `runtime-events-2026-10-01.jsonl` | 9,144 | **0** | 0 | 0 | 0 | 0 |
| `im-runtime-20260929*.log`／`im-runtime-20260930*.log`／`im-runtime-20261001*.log`（24 件） | 2,574–8,980 | **0** | 0 | 0 | 0 | 0 |

### §3.2 09-30 事件流结构（G4 观察日）

- 字段集：`schemaVersion, tsMs, level, component, message, context, fields, privacy`；**101 件**；ts 区间 **2026-09-30 12:38:26 → 23:19:46**。
- component：`local-runtime.thread-goal` 57 ／ `local-runtime.mcp` 38 ／ `local-runtime.matrix-tools` 6。
- `context` 键：`dataDir` 101 ／ `runtimeMode` 101（**全部 `clean`**）／ `runtimeOwnerKind` 101（**全部 `electron`**）／ `sessionId` 63 ／ `turnId` 24。
- **唯一带 `sessionId` 的会话**：`mvs_bbeb804b…`（**16:17:53 → 19:47:32**，63 件）。
- **G4 窗口（≈15:2x／15:46）事件数 ＝ 0**；最近邻事件为 **14:35:41**（MCP connect/connected，无 sessionId）与 **16:17:53**。

⇒ **判定 D3**：事件流**不产出 skill 相关事件**，且 **G4 观察窗口无任何会话级记录**。
⚠️ **诚实边界**：窗口 0 事件**不能**反推「该窗口无会话」——事件流只记 thread-goal 决策与 MCP 生命周期两类业务，**普通轮次本就不落事件**。本棒只主张「**该窗口在此面不可观测**」。

---

## §4 D4／D5／D6：全量日志面 —— 原生 skill 记录 0 ＋ 缺证机制已定

### §4.1 D4 · 三重判别（关键：100% 为 agent 自撰命令回显）

本棒自身与前件的检索命令**文本内**含 `LocalSkill`／`readSkill`／`allowedSkillNames`／`Local skill not found` 等字面（沿 `9f5b73620b8a` §3 **G6「字面命中 100% 为回显」**之纪律），故**必须判别**，不可直接计数。判别三重：

1. **时序切分**：以本棒会话起点 **2026-10-01 16:08:59** 为界；
2. **行型**：区分「带时间戳前缀的日志行」与「**无时间戳前缀的 JSON 载荷续行**」（后者是权限检查器记录的 tool input／cmdPreview 载荷）；
3. **`sessionId` 归属**：读出行内 `"sessionId"`／`"session_id"`，看归属哪个会话。

**`main-10-01.log`（326,336,812 B · 10-01 活动写入）逐模式结果**：

| pattern | 计数（时序严格 <16:08:59） | 判别 |
|---|---|---|
| `tool_result` | **0** | — |
| `is_error` | **0** | — |
| `Local skill not found` | 0（严格）／ 7（含续行） | 7 处**全部 ECHO** |
| `readRegistrySkillByName` | 0（严格）／ 7（含续行） | 7 处**全部 ECHO** |
| `allowedSkillNames` | 0（严格）／ 7（含续行） | 7 处**全部 ECHO** |
| `LocalSkill` | 0（严格）／ 7（含续行） | 7 处**全部 ECHO** |
| `readSkill` | 0（严格）／ 8（含续行） | 8 处**全部 ECHO** |
| `/runtime/skills` | **16（原生·带时间戳）** | 15:49:51–16:06:04 连续 transport 记录 |

**ECHO 行的实测形态**（截 150 字符，判别依据）：
```
[ts=16:08:58] hasTs=False  ECHO(命令/权限载荷行)
   …"permReasonType":"safetyCheck","cmdPreview":"foreach($p in @('allowedSkillNames','LocalSkill','plugin:','readSkill')){"}…
[ts=16:08:58] hasTs=False  ECHO(命令/权限载荷行)
   …"sessionId":"mvs_95…                                     ← 携带调用者自己的 sessionId
```
⇒ 命中载体＝**无时间戳的权限载荷续行**，内容＝**调用者自己敲进去的检索式**，并**自带调用者 sessionId** ⇒ **不是运行时 skill 事件**。

**`runtime-2026100114.5.log`（52,301,346 B · 静态全量窗口 14:22–14:28 · 1,213 行）消息类型全表**（最完整日志层的结构证据）：

| 计数 | 消息类型前缀 |
|---|---|
| 392 | `subcommand`（权限） |
| 242 | `http`（传输） |
| 58 | `whole-command`（权限） |
| 47 ×5 | `permission.decision` / `permission.checker.decision` / `permission.enforcement` / `permission.core.decision` / `Created` |
| 36 | `llm_response_identifiers`（**仅标识符**） |
| 29 ×5 | `sandbox.process.started` / `sandbox.invocation.started` / `sandbox.process.command_dispatched` / `sandbox.exec.requested` / `sandbox.policy.resolved` |
| 28 | `sandbox.invocation.finished` |
| 其余 | `BashToolPermissionChecker` 29 ／ `FsToolPermissionChecker` 10 ／ `local` 6 ／ `review` 2 ／ `Plugin` 1 ／ `Workspace` 1 |

同件标记检测：`tool_result` **0** ／ `toolResult` **0** ／ `is_error` **0** ／ `tool_output` **0** ／ `Local skill not found` **0** ／ `read_skill` **0** ／ `mcp_invoke` **0** ／ `mcp__` **0**。

⇒ **判定 D4**：**全量应用日志面不设 tool 结果通道、不记 skill 解析/读取事件**；一切 skill 字面命中 100% 为 agent 自撰命令回显。⚠️ 样本为 **10-01 全日**（最忙碌、约 30 会话）；**不能排除**「当日恰有 skill 读取而未记录」——但 `tool_result`／`is_error` 双 0 ＋ 上表无 tool 结果类型，构成**结构性强证据**（非严格否证，见 §7-2）。

### §4.2 D5 · 会话轨迹日志只记元数据

`%APPDATA%\minimax\logs\chat-session-trace-10-01.log`（23,537,769 B）：

| 事件 | 行数 | 行长度 | 记录内容 |
|---|---|---|---|
| `chat-session-trace composer-render:window` / `send-stream:first-business-chunk` / `message-actions:commit` | 47,310（`<other>` 合计） | — | UI 层 trace（sessionId／messageId／queryId） |
| `runtime-transport-trace request-start` | **8,428** | min 317 ／ median 379 ／ max 421 | **仅元数据** |
| `… response-start`（`/runtime/skills`） | **379** | min 390 ／ median 392 ／ max 394 | **仅元数据** |
| `… first-response-chunk` ／ `terminal` | 379 ／ 379 | — | 仅元数据 |

`response-start` 字段全表（200 行采样，10/10 全覆盖）：`requestId` / `traceId` / `method` / `apiPattern` / `requestKind` / `timestampMs` / `activeRequestCount` / `responseStatus` / `requestToResponseStartMs` / `data`。
→ **0 响应体字段、0 结果字段**；`toolCallCount` 仅为**计数**（实测值 0／1／3），**不含工具名与参数**。

1,735 处 `skill` 字样经判别全部为：
- **1,516** ＝ 四类 transport-trace 事件各 379 行，命中体为 `"apiPattern":"/minimax-desktop/api/v1/runtime/skills"`；
- **219** ＝ `ui-panel:active-page` 的 `"source":"legacy:set-show-skills"` 等 UI 路由字样。
→ **无一处是 skill 清单内容或读取事件**。

⇒ **判定 D5**：会话轨迹日志**保留调用元数据，丢弃载荷与结果**。

### §4.3 D6 · 缺证机制已定：观察窗口日志**已被清除**

`%APPDATA%\minimax\log-purge.ps1`（SHA-12 `3ae804cfbf61` ／ 980 B ／ **2026-09-28 23:09:08**）**逐字**：

```
# MiniMax logs 轮转止血脚本（Mavis 布置 2026-09-28，PI 授权「你来解决止血」）
# 策略：①非当日 *.log 全清 ②当日 *.log 超 100MB 截断为 0 ③api/chat/remoteControl 小文件保留当日
…
    if ($_.LastWriteTime -lt $today) {
        Remove-Item $_.FullName -Force   # 非当日全清（可恢复通道由清理线机制处理，此处直删=PI 全删授权）
…
    } elseif ($_.Length -gt 100MB) {
        [System.IO.File]::Open($_.FullName, 'Open', 'Write', 'ReadWrite').SetLength(0)
```
（同面另有 `logs\truncate-main-0929.ps1`，SHA-12 `d94e5b999175` ／ 433 B ／ 09-29 23:44:47，头行逐字「一次性：main-09-29.log 活截断为 0 …；机制沿 log-purge.ps1」。）

**逐日实测（`runtime-YYYYMMDD*.log` 件数）**：

| 日期 | 20260924 | 20260925 | 20260926 | 20260927 | 20260928 | 20260929 | **20260930** | 20261001 |
|---|---|---|---|---|---|---|---|---|
| 件数 | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **12** |

`%APPDATA%\minimax\logs\` 当前 12 件（合计 353,410,109 B），**全部为 `-10-01`/`2026-10-01` 命名**（`main-10-01.log` 326,336,812 B 为最大件）。

⇒ **判定 D6**：**G4 观察窗口（09-24→09-30）的 runtime／主日志／会话轨迹日志在盘 0 件**；缺证**不是「日志未开启」，而是「已按授权清除」**。
⚠️ **口径限制**：脚本头内「PI 授权」字样为**脚本自述**，本棒 **0 核对**授权来源（⛔ 不引申）；机制与实测一致即止。

### §4.4 D7 · 已识别的唯一候选运行时取证面（**本棒 0 调用**）

`GET /minimax-desktop/api/v1/runtime/skills`（本地 HTTP 端点）——
- 留痕：主日志 **16 条**原生 transport 记录（10-01 15:49:51–16:06:04）；`chat-session-trace` **379** 次（`request-start`/`response-start`/`first-response-chunk`/`terminal` 各 379）；实测样例 `responseStatus: 200`、`requestToResponseStartMs: 2002`。

⚠️ **未验边界（三项，缺一不可）**：
1. **响应体从未被任何日志记录**（D5 已证）⇒ 本棒**0 读**其内容；
2. 该端点是否回含 **per-session allowlist（`allowedSkillNames` 等）**——**未验**，⛔ 不作任何主张；
3. 属**运行时面**（活进程 HTTP 接口）⇒ 本棒 ⛔ **0 发起调用**（沿前件「0 次实际调用」纪律），⛔ 0 联网。

---

## §5 C3 载体的**取值面**判定（对前件 §4.3 的续判，⛔ 不回改前件）

| 层级 | 前件判定 | 本棒实测 | 本棒判定 |
|---|---|---|---|
| 机制 | `allowedSkillNames` 唯一会话级载体（偏移 `100143457`／`100186675`） | 本棒 **0 复测源码** | **照录沿用** |
| 取值 | 「不在只读可及面」 | D1–D6：旧面 0 文件／新面窗口 0 记录／事件流 0 事件／全量日志 100% 回显／轨迹日志无载荷／窗口日志已被清除 | **升级判定**：该取值在本机**任何记录面都不产生**（**不落盘**），而非「暂不可见」 |

⛔ **本棒 0 复现、0 断言**：「C3 即 G4 之因」**仍是假设**，本棒只把它从「唯一在册候选载体」**收紧为「唯一在册载体 ＋ 其取值在任何在盘面均不可回溯」**。
⛔ **0 补写源码偏移**：本棒 **0 重扫 `app.asar`**（426,404,876 B ／ 2026-09-29 22:25:34，偏移沿用前件口径，升级后须按符号名重定位）。

---

## §6 未闭面：G4 判定 ＋ **所差证据清单**

> **G4（`9f5b73620b8a` §3「同写法同实体同日两会话结果相反」）＝ 仍未闭。**
> **判定形态**：**以当前可读面不可审结** —— 且缺口经 D1–D6 收窄为**两处结构性缺证**（非「暂未查到」）：
> **缺证‑1**：两观察会话各自的 `allowedSkillNames` / `allowedExtensionSkillNames` **原值**（含是否 `undefined`）——**本机任何记录面不产生**；
> **缺证‑2**：两观察会话 skill 读的**入参逐字**与**返回形态**——**任何日志面不记 tool 结果**，且观察窗口日志**已被清除**。

### §6.1 所差证据清单（4 项 · 供未来 runtime 记录面；⛔ 本棒 0 触碰）

| # | 所缺证据 | 为何是决定性的 | 建议打点位置（符号名，偏移沿用前件） | 备注 |
|---|---|---|---|---|
| **E1** | 两次调用时 `options.allowedSkillNames` / `allowedExtensionSkillNames` 的**集合内容与是否 `undefined`** | 唯一在册会话级载体；`undefined` ＝ 不设闸门，有值 ＝ 白名单外一律丢弃 | `readRegistrySkillByName` 入口（`100153797`） | 须记**归一后**选择器集（`toNormalizedSkillSelectorSet` `100144715`） |
| **E2** | 同一时刻 `agentName`（`resolveReadScope` 归一后）与 `compatibleAgentNames` 原值 | 判别 C2「条件性闭」是否在本窗口复活 | `resolveReadScope`（`100190947`）返回处 | 含 `mavis`／子 agent 两类取值 |
| **E3** | 两次调用的**返回形态**：`undefined` ／ 抛 `ambiguousSkillNameError` ／ 命中 `content` | 三者在用户侧分别呈现为「not found」／「ambiguous 报错」／成功，与 G4 现象形态直接对应 | `LocalSkillTool.execute` 出口（`52757967`）＋ `readSkillByName` 返回处（`100194348`） | 须记 `error.code`（409／`AMBIGUOUS_SKILL_NAME`，`100142516`） |
| **E4** | 调用入参 `input.name` 的**逐字原文** | 核「同写法」是否**字面成立**；`plugin:` 前缀若实际存在则 C1 可直接解释（G4 前提或失效） | `LocalSkillTool.execute` 入口（`52757967`，入参仅 `trim()`） | 与 E1–E3 同一批打点即可闭合 G4 判据 |

⚠️ **0 承诺**：以上 4 项**均需在运行时入口打点**（改 runtime）⇒ **超本棒 ⛔ 纯只读范围**，本棒 **0 实施、0 派工**，仅登记为未来取证面。
⚠️ **成本提示**：即便取得 E1–E3，仍需**同会话对、同实体、同日**的可比样本；一次性抓取历史两会话**不可行**（记录面已如 D6 清除）⇒ **G4 若要闭，须在可记录的运行期制造一次受控复现**（是否值得，属 PI 口径面，本棒 **0 主张**）。

---

## §7 反方意见与诚实边界（逐条 · 不夸大 · 不误导）

1. **⛔ 0 断言因果、0 复现**：本棒**未发起任何 skill 加载调用**、**未调用** `/runtime/skills` 端点 ⇒ §3–§4 全部为**盘上静态记录判读**，⛔ **0 由记录缺失推断 G4 成因**。
2. **D4 是「结构性强证据」而非严格否证**：样本为 10-01 全日最忙碌窗口；**不能排除**「当日恰有 skill 读取而未记录」。支撑其强度的是 `tool_result`／`is_error` 双 0 ＋ 1,213 行消息类型全表**无 tool 结果类型**，而**不是** skill 字面 0 命中本身（后者已被回显污染）。
3. **D1／D2／D6 均为「当前盘上态」**：日志随时可能被 `log-purge.ps1` 再次清空、会话记录可能被迁移补写 ⇒ 本件记录的清单具**时效性**，⛔ 不作长期断言。
4. **两处未验面（本棒 0 触碰，⛔ 不宣称其无记录）**：
   - `v2\sqlite\runtime-state.sqlite`（**474,656,768 B**，WAL 5,018,192 B 活动态，10-01 16:10 写入）——**本棒未打开**（打开活 WAL 库有改动风险，⛔ 0 触碰）⇒ **可能**含会话／工具记录表，**未验**；
   - `%APPDATA%\minimax\observability-outbox.jsonl`（8,402 B ／ 34 行）——**未逐条判读**（疑为待投递事件缓冲）⇒ **未验**。
5. **G4 观察日按 `9f5b73620b8a` §3 G5 字面取 2026-09-30**；本棒 **0 核对**该二会话的 sessionId 与任何盘上实体（旧面目录名／事件流 sessionId）的对应关系 ⇒ 旧面 15:39:13／15:59:17 两目录**仅作最近邻登记，⛔ 不主张其即观察会话**。
6. **前件 C1／C2／C4／C5 本棒 0 复测**：照录沿用（避免重复劳动、避免冒充复现）；其源码偏移基于本机 `app.asar`（426,404,876 B ／ 2026-09-29 22:25:34），**版本升级后失效**，须按符号名重定位。
7. **本棒自身污染已登记**：本棒与前棒的检索式文本内含目标字面，**已用时序＋行型＋`sessionId` 三重判别剥离**；残余风险＝**前棒会话（14:2x）若曾发起真实 skill 读取，其回显与原生记录在同一日志内不可分离**——⛔ 不主张已 100% 排除，仅主张**所测各件中可判定者 100% 为回显**。
8. **脚本自述不等于授权核实**：`log-purge.ps1` 头内「PI 授权」字样本棒 **0 核对**（§4.3）。
9. **本件自身 SHA-12／字节不可内嵌**（自引用悖论）——落盘后由 parent 对**终态**复算回填。

---

## §8 自核节

- **写入面**：**仅本件 1 件**（`results/_g4_runtime_state_trace_2026_10_01.md`）——本棒全部操作为**内联只读** PowerShell／文件读取，⛔ **0 落盘 scratch 脚本**、⛔ 0 临时件、⛔ 0 移动／重命名／删除。
- **命名**：`_主题_日期`（去版本前缀、⛔ 无 `_v5_` 类阶段字样，沿 PI 09-29 命名裁 ＋ 10-01 补记「派工建议名亦须合规」）。
- **撞名实测**：落名前 **2 候选 × 4 目录直查** ＝ **8/8 `exists=False`** ＋ **全仓递归扫描**（`Get-ChildItem -Recurse -Force`，文件名含 `g4_runtime_state` / `g4_session_state`）**0 命中** ⇒ **新建，0 覆写**。
- **0 回改自证**：三锚件 SHA-12／字节／mtime 于本棒**写盘前／写盘后**逐字一致（§9 表）。
- **R4**：`config.yaml` **0 打开 0 读值**；`mcp.json`／`local-runtime.auth.json`／`minimax-agent-cn-config.json` **0 读**；本件仅以「含密钥字段，值未读」表述。
- **⛔ 0 改 runtime**：未写 `app.asar`／安装目录／`<dataDir>` 下任何文件／`%APPDATA%\minimax` 下任何文件（全部为 `Get-ChildItem`／`Select-String`／`Get-FileHash`／`Get-Item`／`ReadAllLines` 只读调用）；**未打开** `runtime-state.sqlite`；**未调用** `/runtime/skills` 端点；**未发起**任何 skill 读取。
- **⛔ 0 联网**：全部证据来自本机盘上字节读取与目录枚举；⛔ 0 外部 URL、⛔ 0 LLM 调用、⛔ 0 API。
- **署名**：本件由 **G4 追因续棒（worker 棒，session `mvs_95be9aab6ca14431a956c153fba9db38`）** 产出；源码与运行时归属 **MiniMax Code 运行时（`app.asar`）原作者**；`log-purge.ps1` 之布置者字面为「Mavis 布置 2026-09-28」（**脚本自述，本棒 0 核对**）；**0 冒认**他方为出证方。

---

## §9 0 回改复核（锚件终态哈希 ＝ 写盘前基线）

| 锚件 | SHA-12 | 字节 | mtime |
|---|---|---|---|
| `results/_g4_skill_read_scope_trace_2026_10_01.md` | `9196a608bb0d` | 26,906 | 2026-10-01 14:31:34 |
| `results/_skill_load_failure_window_readonly_facts_2026_09_30.md` | `9f5b73620b8a` | 23,065 | 2026-09-30 16:16:36 |
| `results/_pack_d_closeout_register_2026_10_01.md` | `0f1f94df75ba` | 62,012 | 2026-10-01 14:54:17 |

（写盘前测 ＝ 写盘后测，**逐字一致**；本棒对三件**只读**。）

---

## §10 交棒指向（**0 派工 · 供 parent 裁**）

1. **G4 挂账可由「未闭·需 runtime 记录」细化为「未闭·两处结构性缺证 ＋ 4 项取证清单（E1–E4）」**，并附两项新事实：观察窗口记录面为 **0 文件**、窗口日志**已被清除**（机制可查）。
2. **E1–E4 属运行时打点面**（改 runtime）⇒ ⛔ 本棒 0 实施；是否派工、是否值得为闭 G4 制造受控复现，属 **PI 口径面**。
3. **两处未验面**（`v2\sqlite\runtime-state.sqlite` 474 MB 活 WAL 库、`observability-outbox.jsonl` 34 行）**仍可能有记录**；若 PI 要再推，须单独派只读棒（sqlite 须以 `mode=ro` 打开，⛔ 0 触发 WAL checkpoint／写迁移）。
4. **两处可监控的复活条件**（沿前件 §9-3）：`<dataDir>\agents\<name>\skills` 或安装目录 `assets\{skills,agents}` 出现 ⇒ C2 静默降级立即成为不可观测的一等差异源；`log-purge.ps1` 再次执行 ⇒ 本件 §4 的日志清单即刻失效。
5. **前件 C1 可照录回填**至 `4a3a2d0c5b95` §4.2／§6.3（`plugin:` 无处理器 ＝ 闭）——本棒 **0 回改**该件，**仅登记指向**。
