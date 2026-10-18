# G4 剩面只读探 · runtime-state.sqlite ＋ observability-outbox.jsonl（2026-10-08 · 纯只读 · 出 1 件即停）

> **棒别**：N-7（worker 棒；已批准排期计划 N-7「未闭项①」，源自 G4「未闭·收窄」）。
> **session**：`mvs_100536c3deaf4bd7a28834c385f05061`（署名如实，不冒认他方）。
> **前件（授权锚）**：`results/_g4_runtime_state_trace_2026_10_01.md`（SHA-256 前 12 位 `e0ae0ad66acb` ／ 25,631 B ／ mtime 2026-10-01 16:31:10）——本棒**探前实测复核**与派工一致。
> **承接**：前件 §7‑4 与 §10‑3 登记的两处**未验载体**（`v2\sqlite\runtime-state.sqlite`、`%APPDATA%\minimax\observability-outbox.jsonl`），并载明「sqlite 须以 `mode=ro` 打开，⛔ 0 触发 WAL checkpoint／写迁移」。
> **版式**：UTF-8 无 BOM · LF · `_主题_日期`（⛔ 无版本前缀、⛔ 无 `_v5_` 类阶段字样）。
> **写入面**：**仅本件 1 件**；全部探查为内联只读调用（`Get-ChildItem`／`Get-Item`／`Get-FileHash`／Python `sqlite3` **URI `mode=ro`**／`os.stat`＋只读文本读），⛔ **0 落盘 scratch 脚本**。

---

## §0 只读面清单与 R4 声明

| 面 | 路径 | 读法 | 状态 |
|---|---|---|---|
| 载体① 主库 | `C:\Users\Administrator\.minimax\v2\sqlite\runtime-state.sqlite` | Python `sqlite3` 以 `file:…?mode=ro` URI 打开 ＋ `PRAGMA query_only=1` | 只读，0 写 |
| 载体① 附属 | 同目录 `runtime-state.sqlite-wal`、`-shm` | `Get-ChildItem`／`Get-Item` 元数据 | 只读，0 写 |
| 载体② | `C:\Users\Administrator\AppData\Roaming\MiniMax\observability-outbox.jsonl` | `os.stat` ＋ 只读文本读 ＋ JSON **结构解析**（字段路径枚举） | 只读，0 写 |
| 锚件 | 前件 `_g4_runtime_state_trace_2026_10_01.md` | 读 ＋ `Get-FileHash` | 只读，0 写 |

### §0.1 R4 遵守声明

- 本棒**只登记结构名、字段名、字段路径名、计数、枚举分布与时间跨度**；⛔ **0 转述任何载荷值**（会话正文、工具名、工具入参、工具返回、端点、路径取值均**不落件**）。
- **存在性探测的字面**（`allowedSkillNames` 等 9 个 E1–E4 目标字面、凭据形态关键词）**仅用于「命中／未命中」计数**，**0 摘录上下文、0 输出命中行内容、0 输出邻近片段**。
- **凭据形态字段**：`runtime-state.sqlite` 全库 78 表字段名扫描命中 **31 个含 `key`／`token` 形态的字段名**，逐个判读后**全部为缓存键／迁移键／去重键／token 计数类命名**（如 `cache_key`、`migration_key`、`*_tokens`），⛔ **0 发现 `api_key`／`secret`／`password`／凭据类命名**；载体② 命中 2 个含 `auth` 形态的路径名，**均属启动阶段计时字段名**（非凭据）。
  ⇒ **判定：存在凭据形态字段名（0 明示其值；本棒 0 读取任何值）**，已如实上报。
- 本棒**0 打开** `config.yaml`／`mcp.json`／`local-runtime.auth.json`／`minimax-agent-cn-config.json`；⛔ **0 联网**；⛔ **0 发起** `/runtime/skills` 端点调用；⛔ **0 发起**任何 skill 读取。

---

## §1 结论摘要（先结论，后证据）

**两载体均「可读」；但 E1–E4 所缺之值在两载体中「不存在」。**

| id | 命题 | 判定（三态） | 依据强度 |
|---|---|---|---|
| **P1** | 载体① `runtime-state.sqlite` 可只读打开 | ✅ **有**（`mode=ro` 打开成功，263 个 schema 对象／78 张表，journal=wal） | 直接实测 |
| **P2** | 载体② `observability-outbox.jsonl` 可只读读取 | ✅ **有**（6,824 B ／ 26 行，全部行 JSON 解析成功） | 直接实测 |
| **P3** | 载体① 的**会话消息面覆盖 G4 观察窗口**（09-24→09-30） | ✅ **有**（`local_runtime_message_rows` 窗口内 **2,654 行 ／ 4 个 session_id**；其中含工具调用结构行 **1,656**） | 直接实测 |
| **P4** | 载体① 全库**无任何 allowlist／skill 白名单结构**（表名或列名） | ✅ **无**（78 表字段名全扫，`allowed`／`skill`／`compat` 命中 **0**） | 直接实测 |
| **P5** | E1（`allowedSkillNames`／`allowedExtensionSkillNames` 取值） | ❌ **无**（作 **JSON 键**：全时段 0 行；作子串：全时段 18／4 行，**窗口内 0 行**） | 直接实测 |
| **P6** | E2（`compatibleAgentNames`） | ❌ **无**（键级 0 行；子串全时段 5 行，**窗口内 0 行**） | 直接实测 |
| **P7** | E3（返回形态／`error` 码） | ❌ **无**（`error` 键全时段 **9 行、窗口内 0 行**；`ambiguousSkillName` 形态子串全时段 4 行、**窗口内 0 行**） | 直接实测 |
| **P8** | E4（入参 `input.name` 逐字／`plugin:` 前缀） | ❌ **无**（`plugin:` 子串全时段 83 行，**窗口内 0 行**） | 直接实测 |
| **P9** | 载体② 含任何 E1–E4 面 | ❌ **无**（26 行对 9 个目标字面 ＋ `skill` 字面 **全 0 命中**） | 直接实测 |
| **P10** | 载体① 文件面可被**普通进程**按字节读取 | ⚠️ **不可及**（`Get-FileHash` 三件全部报「正由另一进程使用」）——**仅 SQLite 自身以 `mode=ro` 可读** | 直接实测 |

**一句话**：前件登记的两处未验载体**已探完且均可读**；载体① 的消息面**确实覆盖 G4 观察窗口**，但 **E1–E4 目标字面在窗口内 0 命中**（键级与子串两级均 0）⇒ **「不可得」不是「载体未覆盖窗口」，而是「这些字段本就不落盘」**，与前件 §5 的升级判定**同向且在本载体上得到直接实测支持**；载体② 与 E1–E4 **无关**（当日启动/事件投递缓冲，0 命中）。

⛔ **0 判档**：本棒**不宣布 G4 闭合**，亦**不宣布 G4 因 E1–E4 永不可得而不可闭**。见 §5。

---

## §2 载体① `runtime-state.sqlite` 逐项探表

### §2.1 文件面

| 项 | 实测值 |
|---|---|
| 路径 | `C:\Users\Administrator\.minimax\v2\sqlite\runtime-state.sqlite` |
| 字节 | 474,656,768（与前件 §7‑4 所记**同值**） |
| mtime | 探前 2026-10-08 16:08:41 → 探后 2026-10-08 16:16:35（**活写入面**） |
| `-wal` | 5,018,192 B，mtime 16:08:43 → 16:16:35 |
| `-shm` | 32,768 B，mtime **15:26:10 全程未变** |
| 同目录 | `backups\`（子目录，本棒 0 进入） |
| 字节级读取 | ⛔ **不可及**：`Get-FileHash` 对三件均报「正由另一进程使用」⇒ **0 取得本载体 SHA**（不伪造） |

### §2.2 库面（`mode=ro` 只读打开）

| 项 | 实测值 |
|---|---|
| 打开 | **成功**（URI `file:…/runtime-state.sqlite?mode=ro` ＋ `PRAGMA query_only=1`） |
| SQLite 版本 | 3.50.4（Python 3.14.7） |
| `journal_mode` | `wal` |
| `page_size` ／ `page_count` ／ `freelist_count` ／ `user_version` | 4,096 ／ 115,883 ／ 44,628 ／ 0 |
| schema 对象 | **263** 个（表 78 ／ 索引 ／ 触发器 ／ FTS 虚表） |

⚠️ **活载体告警**：本棒三次读取间，`local_runtime_message_rows` 总行数由 **9,252 → 9,258 → 9,261 → 9,264** 递增，库与 `-wal` mtime 同步前移 ⇒ **本载体在探查期间正被活进程写入**；所有计数均为**时点快照**，具**时效性**（沿前件 §7‑3 纪律）。

### §2.3 结构面：E1–E4 相关字段名（78 表全扫，仅结构名）

| 目标面 | 相关表.列（结构名） | 行数 |
|---|---|---|
| **E1／E2 候选** | `local_runtime_sessions.agent_name`、`local_runtime_sessions.record_json`、`local_runtime_sessions.extra_data_json` | 33 |
| **E1／E2 候选** | `local_runtime_session_agent_definitions.definition_json` | 5 |
| **E1 候选** | `local_runtime_preferences.key` / `.value_json` | 5 |
| **E2／E3 候选** | `local_runtime_message_rows.data_json` / `.source_context_json` / `.role` / `.source` | 9,264 |
| **E3／E4 候选** | `local_runtime_turn_diff_journal.tool_name` / `.tool_status` / `.tool_call_id` / `.ambiguity_reason` / `.paths_json` / `.before_json` / `.after_json` | 1,235 |
| **E3 候选** | `local_runtime_session_agent_state.terminal_outcome` / `.event_id` | 17 |
| 登记表 | `agents.agent_name` / `.agent_role` / `.main_session_id` | 24 |
| 工具差分 | `local_runtime_turn_diffs.file_changes_json` / `.raw_diff` | 138 |
| 空面（0 行） | `local_runtime_queue_items`、`session_resources`、`session_turn_resources`、`local_runtime_communication_messages`、`local_runtime_agents`、`local_runtime_plugin_local_disabled` | 0 |

⚠️ **语义澄清（避免误读）**：`turn_diff_journal` 的 `before_json`／`after_json` 属**文件内容差分**（配合 `paths_json`），**不是工具入参／工具返回** ⇒ 该表虽含 `tool_name`／`tool_status`，**并非 E3／E4 的载荷面**。
⚠️ **0 主张**：表名／列名中**未出现** `allowedSkillNames`、`compatibleAgentNames` 或任何 `skill` 字样；⛔ 本棒**不据此断言**「运行时不存在这些字段」，仅登记「**该载体无此结构**」。

### §2.4 窗口面：G4 观察窗口（2026-09-24 00:00 → 2026-10-01 00:00）覆盖

| 表.时间列 | 最早 | 最新 | **窗口内** | 全表 |
|---|---|---|---|---|
| `local_runtime_message_rows.created_at_ms` | 2026-09-01 09:46 | 2026-10-08 16:15 | **2,654** | 9,264 |
| `local_runtime_sessions.created_at_ms` | 2026-09-01 09:46 | 2026-10-08 16:08 | **2** | 33 |
| `local_runtime_sessions.updated_at_ms` | 2026-09-01 09:46 | 2026-10-08 16:13 | **3** | 33 |
| `local_runtime_session_agent_state.updated_at_ms` | 2026-09-01 10:39 | 2026-10-08 16:13 | **3**（会话） | 17 |
| `local_runtime_turn_diff_journal.created_at_ms` | 2026-09-01 09:46 | 2026-10-08 16:12 | **0** | 1,235 |
| `local_runtime_turn_diffs.captured_at_ms` | 2026-09-01 10:40 | 2026-10-08 16:13 | **0** | 138 |

- 窗口内 `message_rows` 覆盖 **4 个 distinct session_id**，且 **4/4 均能在 `local_runtime_sessions` 表中 join 到** ⇒ **窗口内会话的消息面在本载体确有留存**。
- ⛔ **0 对应核对**：本棒**未**将窗口内 4 个 session_id 与前件 §7‑5 所指 G4 观察二会话做身份比对（比对须读取 sessionId 值，超出「值级 0 转述」）⇒ **不主张**窗口内 4 会话即观察二会话。

### §2.5 存在性面：E1–E4 字面两级命中（0 摘录 · 0 上下文）

对 `local_runtime_message_rows.data_json`（及其余 §2.3 候选 JSON 列）逐行 JSON 解析后统计：**键级**＝该字面作为 JSON **键**出现；**子串级**＝该字面出现在行文本内。

| 目标字面 | 键级（全时段／窗口内） | 子串级（全时段／窗口内） |
|---|---|---|
| `allowedSkillNames` | **0 ／ 0** | 18 ／ **0** |
| `allowedExtensionSkillNames` | **0 ／ 0** | 4 ／ **0** |
| `compatibleAgentNames` | **0 ／ 0** | 5 ／ **0** |
| `agentName` | **0 ／ 0** | 未单列（同族键级 0） |
| `toolName` ／ `toolCallId` | **0 ／ 0** | 未单列（同族键级 0） |
| `error`（E3 形态相关） | 9 ／ **0** | — |
| `LocalSkillTool` | — | 6 ／ **0** |
| `readRegistrySkillByName` | — | 6 ／ **0** |
| `readSkillByName` | — | 20 ／ **0** |
| `ambiguousSkillName` ／ `AMBIGUOUS_SKILL_NAME` | — | 4 ／ **0** ／ 3 ／ **0** |
| `plugin:`（E4 前缀） | — | 83 ／ **0** |
| **工具调用结构键**（`tool_calls` 类） | — | **6,258 ／ 1,656** |

⚠️ **子串级命中的归因（⛔ 0 断言来源，仅登记形态）**：全部子串级命中**落在 G4 观察窗口之外**；其中多数字面属**源码标识符形态**，与前件 §7‑7 登记的同类风险一致（**棒方自身检索式文本内含目标字面**）⇒ 本棒**不主张**这些命中代表真实运行时调用，**亦不主张**其已 100% 排除回显污染。
⚠️ **工具调用结构的存在性含义**：窗口内 **1,656 行**含工具调用结构键 ⇒ 该面**记工具调用事件**，但 **E1–E4 所需的具体取值（白名单、agent 作用域、入参原字、返回形态）在窗口内 0 命中** ⇒ ⛔ **0 由「结构存在」推断「取值可得」**。

---

## §3 载体② `observability-outbox.jsonl` 逐项探表

### §3.1 文件面

| 项 | 实测值 |
|---|---|
| 路径 | `C:\Users\Administrator\AppData\Roaming\MiniMax\observability-outbox.jsonl` |
| 副本数 | **1**（`…\AppData\Roaming\minimax\…` 小写路径经实测**为同一文件**——Windows 路径大小写不敏感；`%APPDATA%` ＝ `C:\Users\Administrator\AppData\Roaming`） |
| 字节／行 | 6,335 B（15:58:25）→ **6,824 B ／ 26 行**（16:12:37）——**探查期间仍在写入** |
| 三时点体积 | 派工单记 3,113 B ／ 前件 §7‑4 记 8,402 B·34 行（10-01）／ 本棒 6,824 B·26 行 ⇒ **三个时点三个值** |

⚠️ **前件记载已不属当前盘上态**：前件 §7‑4 所记「8,402 B ／ 34 行」在当前盘上态**不成立**（现为 6,824 B ／ 26 行）⇒ 该面**只反映当前当日**，⛔ **0 主张**其保留历史事件，⛔ **0 推断**清空机制（前件未验，本棒 0 查脚本面）。

### §3.2 结构面（字段名与字段路径，0 值级）

| 项 | 实测值 |
|---|---|
| 解析 | **26／26 行解析成功**（0 失败行） |
| 顶层形态 | **2 种**：13 行 `{id, eventName, createdAt, payload}`；13 行 `{ack}` |
| 字段路径总数 | **59** |
| `payload` 子字段性质 | 启动阶段耗时与事件投递类（形如 `*_duration_ms`、`renderer_to_*_ms`、`app_ready_to_ipc_ready_ms`、`startup_to_runtime_ready_ms` 等计时字段 ＋ `outcome`／`stage`／`failure_phase`／`reason_code`／`incident_id`／`attempt_count`／`domain`／`platform`／`app_version`／`arch`／`source_process`／`initial_surface`／`fileCount`／`totalBytes`／`owner_user_id` 等事件元数据） |
| 时间跨度 | `createdAt` 全部落在 **2026-10-08 单日**（distinct 天数 ＝ 1） |
| 事件类别 | `eventName` distinct **7** 个；`payload.kind` distinct **1** 个（⛔ **值级 0 转述**） |
| 会话／工具内容 | ⛔ **0 字段**：59 条路径中**无** session／turn／tool／skill／message 类字段 |

### §3.3 存在性面：E1–E4 目标字面

| 目标字面 | 命中行数 |
|---|---|
| `allowedSkillNames` ／ `allowedExtensionSkillNames` ／ `compatibleAgentNames` | **0** |
| `LocalSkillTool` ／ `readRegistrySkillByName` ／ `readSkillByName` | **0** |
| `ambiguousSkillName` ／ `AMBIGUOUS_SKILL_NAME` | **0** |
| `plugin:` | **0** |
| `skill`（族） | **0** |

⇒ **判定：载体② 与 E1–E4 无结构关系（无）**，其内容为**当日应用启动/事件投递缓冲**。

---

## §4 E1–E4 面现状（逐项 · 依前件 §6.1 定义）

> 前件 §6.1 的 E1–E4 定义原文见 `_g4_runtime_state_trace_2026_10_01.md:243-246`。
> ⚠️ **派工指针偏差（如实登记）**：派工要求实读前件「§6／**§6.3**」；实读结果为前件 §6 **仅含 §6.1**（所差证据清单 4 项），**不存在 §6.3**（前件 §10‑5 所提「§6.3」系**另一件** `4a3a2d0c5b95` 的章节号）⇒ 本棒按 §6 ＋ §6.1 执行，⛔ **0 臆造** §6.3 内容。

| # | 所缺证据（前件 §6.1） | 载体① | 载体② | 三态判定 |
|---|---|---|---|---|
| **E1** | `allowedSkillNames`／`allowedExtensionSkillNames` 的**集合内容与是否 `undefined`** | 全库**无此结构**；键级 0 行；子串级全时段 18／4 行但**窗口内 0 行** | 无此结构，0 命中 | ❌ **无**（不落盘） |
| **E2** | `agentName`（归一后）与 `compatibleAgentNames` 原值 | `agent_name` 列存在于 `sessions`／`token_usage`／`turn_diffs` 等表，但 `compatibleAgentNames` **键级 0**；子串级窗口内 **0** | 0 命中 | ❌ **无**（作用域字段不落盘；⚠️ 仅 `agent_name` **列名**存在，⛔ 本棒 0 读其值，故**不主张**其等于 E2 所需归一后取值） |
| **E3** | 返回形态（`undefined`／`ambiguousSkillNameError`／命中 `content`）与 `error.code` | 窗口内 `error` 键 **0 行**；`ambiguousSkillName` 族窗口内 **0 行**；`turn_diff_journal` 为**文件差分面**，非返回面 | 0 命中 | ❌ **无** |
| **E4** | 入参 `input.name` **逐字原文**（含 `plugin:` 前缀） | `plugin:` 子串全时段 83 行、**窗口内 0 行**；工具调用结构存在但入参原字窗口内 0 命中 | 0 命中 | ❌ **无** |

**⇒ E1–E4 四项在两载体中均为「无」。**
**⇒ 但缺证形态已被本棒收紧为更强的表述**：载体① 消息面**覆盖 G4 窗口**（2,654 行、4 会话、1,656 行含工具调用结构），而四项目标字面**窗口内 0 命中** ⇒ **「不可得」归因于「本就不落盘」，而非「载体未覆盖该窗口」或「记录已被清除」**——此与前件 §5 的升级判定**同向**（前件结论基于日志面与记录面枚举，本棒首次在**唯一未验的 sqlite 载体**上取得同向直接证据）。

---

## §5 依赖与边界

### §5.1 闭环门依赖（如实标注，⛔ 0 假闭环）

1. **闭环门「G4 仍需 runtime 打点 E1–E4」**：**成立且未被本棒解除**。E1–E4 属**运行时入口打点面**（改 runtime），本棒**0 实施、0 派工**。
2. **本棒解除的**只是「两处未验载体是否可能藏有 E1–E4」这一**不确定性**：载体① 可读但无该取值；载体② 与该面无关 ⇒ **「未验」项已转为「已验·无」**，⛔ **不构成** G4 闭合的充分条件。
3. **若 PI 调整启动口径**（是否为闭 G4 制造受控复现、是否值得投入 runtime 改造），**属 PI 口径面**：本棒⛔ **0 预设、0 主张、0 建议时点**，仅登记两载体的客观所见。
4. **可比样本问题仍在**：即便日后取得 E1–E3，仍需**同会话对、同实体、同日**可比样本（前件 §6.1 成本提示）；本棒**0 主张**该条件已具备。

### §5.2 边界（诚实限制，逐条）

1. **活载体时点性**：两载体在探查期间**均被写入**（`message_rows` 9,252→9,264 行；outbox 6,335→6,824 B）⇒ 本件所有计数为**时点快照**，⛔ **不作长期断言**（沿前件 §7‑3）。
2. **时点**：本件探查窗口约 2026-10-08 16:08–16:17；⛔ **0 核对**该窗口与前件各实测时点之间的差异原因。
3. **0 值级**：本棒⛔ **未读取**任何会话正文、工具名、工具入参、工具返回、路径取值 ⇒ 对「结构面是否实际承载目标事件」**只作存在性判断，不作内容判断**。
4. **0 身份比对**：窗口内 4 个 session_id ⛔ 未与 G4 观察二会话比对 ⇒ **不主张**窗口内会话即观察会话。
5. **前件字节未复核**：前件 `_g4_skill_read_scope_trace_2026_10_01.md`、`_skill_load_failure_window_readonly_facts_2026_09_30.md`、`_pack_d_closeout_register_2026_10_01.md` 三锚件本棒⛔ **0 读取、0 哈希**（不属本棒范围）。
6. **哈希不可及**：载体① 三件**字节级 SHA 不可得**（活进程独占）⇒ 本件**不含**载体① 的哈希，⛔ **0 以大小／mtime 冒充分身校验值**。
7. **子串级命中的污染风险**：见 §2.5 告警（棒方检索文本自身含目标字面）⇒ ⛔ **0 断言**这些命中的来源。
8. **源码偏移**：本棒⛔ **0 重扫** `app.asar`、⛔ **0 补写源码偏移**，前件偏移按前件 §7‑6 口径**已因版本升级失效**。
9. **本件自身 SHA-12／字节不可内嵌**（自引用悖论）——落盘后由 parent 对**终态**复算回填。

---

## §6 0 回改自证

| 锚件／载体 | 探前 | 探后 | 判定 |
|---|---|---|---|
| `results/_g4_runtime_state_trace_2026_10_01.md` | SHA-12 `e0ae0ad66acb`／25,631 B／2026-10-01 16:31:10 | **逐字一致** | ✅ **0 回改** |
| `runtime-state.sqlite` | 474,656,768 B／16:08:41 | 474,656,768 B／16:16:35 | 字节同值、mtime 前移＝**活进程自身写入**（旁证：同期 `message_rows` 行数递增） |
| `runtime-state.sqlite-wal` | 5,018,192 B／16:08:43 | 5,018,192 B／16:16:35 | 同上 |
| `runtime-state.sqlite-shm` | 32,768 B／15:26:10 | 32,768 B／**15:26:10（未变）** | ✅ 观察到**无 shm 写入**证据 |
| `observability-outbox.jsonl` | 6,335 B／15:58:25 | 6,824 B／16:12:37 | 体积增长＝**活进程自身写入**（本棒⛔ 0 写） |

**本棒写入面**：**仅本件 1 件**（`results/_g4_residual_probe_2026_10_08.md`）。⛔ **0 落盘 scratch 脚本／临时件**；⛔ **0 移动／重命名／删除**任何文件；⛔ **0 网络**；⛔ **0 触发 WAL checkpoint／写迁移**（仅 URI `mode=ro` ＋ `PRAGMA query_only=1`，⛔ 未执行任何 `INSERT`／`UPDATE`／`DELETE`／`VACUUM`／`PRAGMA wal_checkpoint`）。

---

## §7 交棒指向（**0 派工 · 供 parent 裁**）

1. **前件 §7‑4／§10‑3 的两处「未验面」可结为「已验·无」**：载体① 可读、无 E1–E4 取值；载体② 与 E1–E4 无关。⇒ G4 挂账表述可由「两处结构性缺证 ＋ 两载体未验」更新为「**两处结构性缺证 ＋ E1–E4 在唯一未验载体上亦不落盘**」。
2. **新增可闭的机制性事实（建议 parent 考虑是否单列）**：`local_runtime_message_rows` 覆盖 G4 观察窗口（2,654 行／4 会话、1,656 行含工具调用结构），而四项目标字面窗口内 0 命中 ⇒ 「不可得」的归因**锁定为「不落盘」**，排除「载体未覆盖窗口」与「窗口记录已清除」两种替代解释。
3. **两处可监控的复活条件**（沿前件 §10‑4，本棒 0 变更）：`log-purge.ps1` 再次执行、或 runtime 升级使 sqlite schema 变更（新增 allowlist/skill 落盘字段）⇒ 本件 §2.3／§2.5 即刻失效，须重探。
4. **0 派工**：是否为闭 G4 制造受控复现、是否改造 runtime 打点 ⇒ **PI 口径面**，本棒 0 主张。

---

## §8 自核节

- **写入面**：仅本件 1 件；⛔ 0 scratch 落盘、⛔ 0 临时件、⛔ 0 删除／移动／重命名。
- **命名**：`_g4_residual_probe_2026_10_08.md`＝`_主题_日期`，⛔ 无版本前缀、⛔ 无 `_v5_` 类阶段字样（沿 PI 09‑29 命名裁 ＋ 10‑01 补记「派工建议名亦须合规」）。
- **撞名实测**：落名前 `glob **/_g4_residual_probe*`（全仓递归）＝ **0 命中** ⇒ **新建，0 覆写**。
- **只读性**：载体① 以 `mode=ro` ＋ `query_only=1` 打开（⛔ 0 写事务、⛔ 0 checkpoint）；载体② 以 `os.stat` ＋ 只读文本读；全部操作为内联只读。
- **R4**：本件仅含**结构名／字段路径名／计数／枚举分布／时间跨度**；⛔ **0 载荷值、0 会话正文、0 工具入参与返回、0 摘录片段**；**存在凭据形态字段名（0 明示其值）**已如实上报（§0.1）。
- **0 判档**：§4 的「无」为**存在性判定**，⛔ **非**「G4 已闭」或「G4 永不可闭」之判档；闭环门依赖见 §5.1。
- **署名**：本件由 **N‑7 worker 棒（session `mvs_100536c3deaf4bd7a28834c385f05061`）** 产出；sqlite／JSONL 之内容归属 **MiniMax Code 运行时**原作者；⛔ **0 冒认**他方为出证方。