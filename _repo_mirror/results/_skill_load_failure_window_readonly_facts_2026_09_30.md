# skill 加载失败窗口 · 只读排障事实与候选（2026-09-30）

- **件性质**：**只读排障登记件**（PI 六项执行之 ③；新建 1 件 · **0 回改既有件** · 0 覆写 · **0 改配置** · **0 改 skill 目录**）
- **触发**：PI 2026-09-30 裁定「六项全办」，其中 ③失败窗口专项排障 归本棒
- **问题面**：`644e0666fbc4` §4-3 待裁项「失败会话/时段是否派专项排障」→ PI 裁**派**；本件即该专项
- **待解释的现象**：**同一日、同一 skill 名（`scientific-writing`）、同一写法（`plugin:skill` 限定名）、同一份盘上实体**——parent 会话 1/1 成功（命中 plugin-cache 面），子会话 2/2 失败（`Local skill not found`）
- **前置件**：`results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md`（`644e0666fbc4`）· `results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md`（`c14489750416`）
- **姊妹件（本棒同日）**：`results/_skill_erratum_and_parent_success_note_2026_09_30.md`（①勘误拆件 · ②强制口径 · ⑤父级成功补记）
- **出件**：**doc-writer**（`agent-0032834a3e04`）· 依派工单执行 · 0 LLM / 0 API / 0 外部 URL / **0 key 值读取或写入**
- **方法**：PowerShell 只读枚举 ＋ `Get-FileHash -Algorithm SHA256` ＋ `grep` 只读搜索 ＋ 单遍流式逐行统计；**本棒 0 次 skill 加载调用**、**0 次配置写入**
- **探查面**：`config.yaml` · `skill-hub.json` · `.minimax\plugins\` · plugin-cache 树与各树 `.minimax-plugin\plugin.json` · `.builtin-skills\` · `v2\observability\logs\`（15:00–16:1x 时间窗）· `v2\workspaces\…\captures\` · `.minimax\sessions\` · `.minimax\agents\`
- **命名**：去版本前缀 · `_主题_日期`；落名前 **2 轮撞名实测**（4 目录 × 2 ＋ 全仓递归 glob 近名）**0 命中** → 新建，**0 覆写**

> **一票结论（先看这条）**：本棒把**三个候选注册面全部探完**——`config.yaml` **0 个 skill 相关键**、`skill-hub.json` **只登记 2 个 hub skill（不含任一关键 skill）**、`.minimax\plugins\` **仍为 0 项** ⇒ **三面均不含失败的那些 skill**。同时发现两项**足以改变后续判读的事实**：①**runtime 日志根本不记 skill 加载事件**（`toolName=Skill`/`SkillTool` = 0，组件标签仅 `proto.js:234`）⇒ 失败窗口**无法**从日志重建；②**同名 skill 实为「三面」而非「两面」**（`.builtin-skills\` 亦含 `docx/pdf/pptx/xlsx`，且哈希与另两面**均不同**）。
> **本件 0 断言因果**：只列事实与候选，**不判定「为什么」**（见 §5）。

---

## §0 输入链与读面清单（终态实测 · 全部只读）

| # | 件 | 实测 SHA-12 | 字节 | mtime | 本件引用面 |
|---|---|---|---|---|---|
| 1 | `results/_v3_v4_achievements_inventory_2026_09_24.md` | `2fb5987f544d` | 192,292 | 2026-09-29 12:12:41 | 0 回改自证锚 |
| 2 | `results/_skill_cache_inventory_and_reference_update_advice_2026_09_30.md` | `c14489750416` | 31,692 | 2026-09-30 15:32:36 | C1–C6 候选来源 |
| 3 | `results/_skill_reference_erratum_and_runtime_anchor_experiment_2026_09_30.md` | `644e0666fbc4` | 25,901 | 2026-09-30 15:51:37 | 现象面（18 例加载结果） |

> 三件 SHA-12 与派工单/前序件登记值**逐字一致** ⇒ 前序件**未被触动**，本件对其结论**只读引用、0 冒认、0 回改**。

---

## §1 只读面逐面事实

### §1.1 `config.yaml`（5,598 B · mtime **2026-09-30 16:08:29**）

| 项 | 实测 |
|---|---|
| **顶层键（8 个）** | `logLevel` · `provider`（`minimax`，含 `MiniMax-M2.7` / `MiniMax-M2.7-highspeed` / `MiniMax-M3` / `MiniMax-M3.1-Flash-Preview` 及各自 `models/options/thinking_config/capabilities`）· `defaultModel` · `memory`（`proactive`）· `permissionMode` · `custom_provider`（`provider-d59e1d`：`mimo-v2.6-flash` / `mimo-v2.6-pro` / `deepseek-flash` / `deepseek-v4-pro`）· `dataContribution`（`enabled`）· `review`（`turnDiffCard`） |
| **skill / plugin / cache / hub / builtin 键** | **0 个**（全文 233 行逐行正则 `skill\|plugin\|cache\|hub\|builtin` ⇒ **0 命中**） |
| **含敏感值的键** | `apiKey` 出现 **3 处**（`provider.minimax.options` 1 处、`custom_provider.mimo` 1 处、`custom_provider.deepseek` 1 处）——**本棒只统计键名与出现次数，0 读取值、0 记录值、0 写入** |

> **事实**：**`config.yaml` 内不存在任何 skill 解析相关的配置项**。

### §1.2 `skill-hub.json`（8,598 B · mtime 2026-09-18 11:46:00 · SHA-12 `c36d6b7f46de`）

| 项 | 实测 |
|---|---|
| 顶层键 | **仅 2 个**：`skills` · `installed` |
| `skills` | **Object[]，2 项**：`dep-updates`（`source_type:2`，`source_url` = github `trufflesecurity/trufflehog` 路径）、`agent-safety`（`source_type:2`，github `compass-soul/agent-safety-skill` 路径）——**两者均含完整 `content` 正文** |
| `installed` | **2 键**：`{"dep-updates":1789703143719, "agent-safety":1789703160333}`（仅时间戳） |
| 关键 skill 名命中 | `scientific-writing` / `experimental-design` / `peer-review` / `academic-paper-polish` / `verification-before-completion` ⇒ **各 0 命中** |
| 注册面字面命中 | `plugin-cache` / `sha256-tree-v1` / `plugin:` / `611965` / `ade95665080e` ⇒ **各 0 命中** |

> **事实**：`skill-hub.json` 是一份**只登记 2 个「从 hub 安装的 skill」**的台账（附 `source_url` 与 `content`），**既不含任何 plugin-cache skill，也不含任何 builtin skill**。

### §1.3 `.minimax\plugins\`（mtime 2026-09-10 14:17:58）

**0 项（空目录）** —— 沿 `c14489750416` F4 口径，**今日仍成立**（本棒独立复测，非转述）。

### §1.4 plugin-cache 树与**每树** manifest（本棒新测，含对既有件的**表述修正**）

| 项 | 实测 |
|---|---|
| `v2\plugin-cache\` 下 | **仅 1 个来源根** `official\`（mtime 2026-09-24 09:22:05） |
| `official\` 下树数 | **28** |
| 带 `.minimax-plugin\plugin.json` 的树 | **28 / 28**（**0 棵缺 manifest**） |
| manifest 位置 | **每棵树各自一个**：`<树>/.minimax-plugin/plugin.json` |
| **表述修正** | `official\.minimax-plugin\plugin.json`（单一大清单）**不存在**；`644e0666fbc4` §0.3 记「清单在 `.minimax-plugin\plugin.json`」**未指明层级**，本棒**精确化**为**逐树各一**（`01afed…` 1,002 B ↔ `611965fcb620…` 1,245 B ↔ `ade95665080e…` 1,322 B 等） |
| 树 mtime 区间 | 最早 **2026-09-01 16:17:03**（`01afed677637`）→ 最新 **2026-09-24 09:21:17**（`74e227dec1c2`） |

### §1.5 `.builtin-skills\`（**第三面** · 本棒新测）

| 项 | 实测 |
|---|---|
| 项数 | **20 个目录 ＋ 1 个文件**（`.seed-fingerprint`，64 B）＝ **21 项**；既有件记「20 个目录」**不矛盾**（本棒 21 为含文件计数） |
| 目录 mtime | 全部 **2026-09-29 22:38:31 / 22:38:32** |
| **与另两面重叠的 skill** | **`docx` · `pdf` · `pptx` · `xlsx` 四个均在此面**，且**四者在用户面亦全部存在** |
| 与 `scientific-*` / `experimental-design` / `peer-review` / `verification-before-completion` | **0 重叠**（沿 `c14489750416` F9，本棒独立复测成立） |

**同名 skill 实测为「三面」、且三份内容各不相同**（本棒新测 · 对 `c14489750416` §2.2「两面」模型的**扩充**）：

| skill | 用户面 SHA-12 / 字节 | plugin-cache 面 SHA-12 / 字节 | **builtin 面 SHA-12 / 字节**（本棒新测） | 相异份数 |
|---|---|---|---|---|
| `docx` | `cfbabd72b1ae` / 20,084 | `12e5a0cccd0c` / 11,619 | **`c9407f69ad99` / 11,536** | **3 / 3** |
| `pdf` | `9f78b8359fbd` / 8,072 | `e39aa05f43db` / 28,593 | **`3ce4de4609d4` / 28,863** | **3 / 3** |
| `pptx` | `e5b0df918cbe` / 9,182 | `931a81818974` / 32,801 | **`75c4bbe0bf93` / 13,049** | **3 / 3** |
| `xlsx` | `55591d7decc1` / 11,464 | `6eab2cbf5606` / 27,366 | **`a3f0d9a7afa6` / 26,848** | **3 / 3** |

> 前两列转述自 `c14489750416` §2.2（**本棒未复测**）；第三列**为本棒实测**。

### §1.6 会话与代理注册面

| 项 | 实测 |
|---|---|
| `.minimax\sessions\` | **616 个会话目录**；**均不含** `mvs_bbeb804b1a6a41109be740636eed1709`，亦不含本棒自身会话 `mvs_cf101c266f884802bc3b84fbbccbd2fc` |
| parent 会话记录实际位置 | `v2\workspaces\d7079be4…\captures\mvs_bbeb804b1a6a41109be740636eed1709\revision_*/` —— 每 revision 一对 `manifest.json` ＋ `workspace.zip`；最新 `revision_munsj06y_i542oeuh` @ **2026-09-30 15:35:18** |
| `manifest.json` 顶层键 | `schemaVersion, workspaceId, sessionId, revisionId, kind, createdAtMs, rootHash, baseRevisionId, baseRootHash, fileCount, totalBytes, entries[1,323], archive` ⇒ **workspace 文件清单快照**（`fileCount` / `totalBytes` / `entries`），**非工具调用轨迹** |
| `.minimax\agents\` | **7 项**：`.builtin` · `mavis` · `verifier` · `agent-0032834a3e04`（本棒）· `agent-11335500b168` · `agent-3a4d09ba3c90` · `agent-3e0c193da529` |
| `v2\plugin-data\local-minimax\` | **仅 `dsh\`**（5 项，mtime 2026-09-10 14:17:59）；`v2\plugin-hook-cache\.leases\` mtime 2026-09-10 14:17:58 |

---

## §2 时间窗日志面：**该面无法用于本问题**（本棒最重要的负向发现）

### §2.1 日志形态实测

| 文件 | 字节 | 覆盖时段 | 组件标签（逐行统计） |
|---|---|---|---|
| `v2\observability\logs\runtime-2026093015.log` | 52,297,066 | 15:00–15:30 | — |
| `v2\observability\logs\runtime-2026093015.1.log` | 48,481,557 | 15:30–15:59 | **仅 `proto.js:234`**（1,584 / 1,593 行） |
| `v2\observability\logs\runtime-2026093016.log` | 实时追加 | 16:00– | 复测前 1,069 行：**仅 `proto.js:234`**（1,067 行） |

> 目录内共 **21 个日志项**（`runtime-YYYYMMDDHH[.N].log` 逐小时轮转 ＋ 体量极小的 `im-runtime-*.log`；`im-runtime-2026093015.log` 仅 **480 B**，7 项 skill 相关字面**全 0**）。

### §2.2 **日志中不存在 skill 加载事件**（关键否证）

对窗口内全部日志探针：

| 探针字面 | `runtime-…15.log` | `runtime-…15.1.log` | `runtime-…16.log` |
|---|---|---|---|
| `toolName=Skill` | **0** | **0** | **0** |
| `SkillTool` | **0** | **0** | **0** |
| `skillLoader` / `resolveSkill` / `localSkill` | **0** | **0** | — |
| `builtin-skills` / `skill-hub` / `skills\` / `/skills/` | **0** | **0** | 有（**见 §2.4 计数不可用**） |

> **事实**：runtime 日志的组件标签**只有 `proto.js:234`（权限校验流）**；**不含任何 skill 加载/解析事件**。
> **推论边界（事实层，不涉因果）**：**父级的成功与子会话的失败，在该日志面内均无记录** ⇒ **失败窗口无法由这些日志重建**。这**同时否证**了「读更新日志/changelog 定位」（`c14489750416` C4 的一部分路径）与「按字面统计日志中的失败次数」两类做法在本运行时上的可行性。

### §2.3 **字面统计被回显污染**（本棒新发现 · 已落为强制口径强-8）

窗口日志对 `Local skill not found` 的命中数：15.log **20** 处、15.1.log **9** 处。**本棒逐行查看其上下文后确认：全部为回显，0 条为加载器事件**——

| 命中类型 | 实际内容（实测摘引） |
|---|---|
| **工具入参回显** | `FsToolPermissionChecker checkPermissions called, toolName=grep, input={"pattern":"plugin-cache\|sha256-tree-v1\|Local skill not found","path":"D:\\私人资料\\deposon-repo",…}` |
| **命令文本回显** | `BashToolPermissionChecker … input={"command":"…Select-String… -Pattern 'Local skill not found' -SimpleMatch…"}` |
| **写入件正文回显** | `FsToolPermissionChecker … toolName=write, input={"path":"…\\_skill_cache_inventory_and_reference_update_advice_2026_09_30.md","content":"# skill 目录 / plugin-cache 现状盘点…"}` |

同理，`scientific-research-workflows:scientific-writing` 在 15.log **0 命中**、在 15.1.log **6 命中**——后者经查看**全部**是 `_skill_cache_inventory…md`（15:32:36 写入）与 `_skill_reference_erratum…md`（15:51:37 写入）两份件的**正文回显**，**无一条是加载调用**。

> **可复述的否定结论（事实层）**：❌「在 runtime 日志里 grep `Local skill not found` 就能数出失败次数」→ **不成立**（回显占 100%），**会系统性高估**。
> 该条已写入姊妹件 §3.1 **强-8（强制口径）**。

### §2.4 计数方法缺陷登记（**不引用不稳定数字**）

`runtime-2026093016.log` 为**实时追加**文件：本棒整文件文本计数得 `builtin-skills` **147** 次，改为单遍流式前 1,069 行计数得 **63** 次，**两次不一致**。⇒ 该文件的**任何字面计数均不可复现**。本件**不引用**该类数字作任何结论，仅引用**组件标签**与 **`toolName=Skill`/`SkillTool` = 0** 两项稳定事实。

---

## §3 差异候选（**事实 ＋ 候选 · 0 断言因果**）

> **口径**：本节只登记「本棒新测/复测了哪些事实」与「该候选的事实层状态」。**不写「因此导致」「故原因是」**——因果判定超出本棒只读证据力。

| id | 候选 | 本棒新测/复测**事实** | 事实层状态 |
|---|---|---|---|
| **G1** | **注册面缺失**（`c14489750416` C6） | **三个候选注册面全部探完且全部为「零」**：`config.yaml` 0 个 skill 键（§1.1）· `skill-hub.json` 仅 2 个 hub skill、无一关键 skill（§1.2）· `.minimax\plugins\` 仍 0 项（§1.3） | **加强并收窄**：可排除的面**增加**为「这三个都不是解析面」；**仍未识别**真正决定解析的面 |
| **G2** | **同名遮蔽 / 解析面优先级**（C2） | **同名实为三面而非两面**：`.builtin-skills\` 亦含 `docx/pdf/pptx/xlsx`，且 `docx` 等四枚在**三面各有不同哈希**（§1.5） | **须扩充**：`c14489750416` §2.2 的「两面」模型**不完整**；任何同名冲突分析**必须枚举三面**（**0 断言**该扩充是否即失败原因） |
| **G3** | **运行时/组件边界 · 时序邻接**（C4） | ①`.builtin-skills` 全部 mtime 为 **2026-09-29 22:38:31/32**，**晚于**失败窗口 **09-24→09-28** ⇒ 该事件**不能解释**该窗口（C4 就此窗口**被否证**）；②最新 plugin 树 materialized 于 **09-24 09:21:17**，**落在**窗口首日（邻接关系**维持**，仍仅邻接）；③**更新日志/changelog 路径被 §2.2 否证**（该面无记录可读） | **部分否证 ＋ 部分维持 ＋ 一条路径关闭** |
| **G4** | **会话级状态差异 / 调用形态差异**（C5） | ①**同写法同实体同日两会话结果相反**——事实沿 `644e0666fbc4` 与姊妹件 §2.2，**本棒 0 复现**；②**本棒把全部可及注册面探完后，仍未找到任何「按会话区分」的 skill 状态载体**：`.minimax\sessions\` 无该会话项、captures 为 workspace 文件清单、`.minimax\run\` 仅 1 个 44 B 租约文件、`v2\plugin-data` 仅 `dsh`、`v2\plugin-hook-cache\.leases` mtime 停在 09-10（§1.6） | **维持且被「无处可藏」所限**：差异**确实存在**，但**只读面内找不到承载该差异的状态文件** ⇒ 候选**既未被证实、也未被推翻** |
| **G5** | **配置项差异** | `config.yaml` mtime **2026-09-30 16:08:29**，**晚于**父级成功（≈15:2x）与子会话实验（15:46 起）**两个时点**；且其内容**无任何 skill 键**（§1.1） | **不可关联**：在**两个现象之后**才变动，且**不含** skill 项 ⇒ **不能**用配置变更解释任一现象（**0 因果**） |
| **G6** | **字面统计口径污染**（本棒新增） | §2.3：**字面命中 100% 为回显** | **新增候选成立**（影响的是**统计口径**，不是加载行为本身） |

### §3.1 本棒**未推进**的候选（诚实记为空白，不以沉默充作「无变化」）

- **`644e0666fbc4` §2.4 C4 中「未读更新日志/changelog/版本号」一项** → 本棒**路径已关闭**（§2.2：日志面无该类记录）；**版本号面未查**（`config.yaml` 无 version 键，未在 `bin/` 或包元数据中定位版本字面）。
- **加载器实现（解析优先级、同名冲突判定、`plugin:` 前缀解析代码）** → **0 读**。`.minimax\bin\`（mtime 2026-09-29 22:38:07）**存在但本棒未探查**——列为下棒可行动指向（§4-2），**不在本件断言其含或不含相关代码**。
- **UI 侧插件安装/启用状态** → **0 查**（不开任何设置界面）。
- **28 棵树 / 172 skill 的总量** → 本棒**只统计树数 28 与 manifest 齐备度 28/28**，**未重数** skill 子目录总量（沿前序件，**不冒认**）。

---

## §4 可行动指向（**面向后续棒的建议 · 0 派工**）

1. **本面已尽**：注册面（`config.yaml` / `skill-hub.json` / `.minimax\plugins\`）与 runtime 日志面**均已探完且均为负** ⇒ 后续排障**不应再重复探这三个面**。
2. **唯一未探的代码面**：`.minimax\bin\`（mtime 2026-09-29 22:38:07）——若要进一步逼近因果，**只读**检索其中 skill 解析相关的 `plugin:` 前缀解析与面优先级逻辑，是**本棒未做、且只读可做**的下一步。
3. **日志盲区不可绕**：若需事件级证据，**当前运行时无该类日志**；任何「按日志复盘失败窗口」的方案在本运行时**均不成立**。
4. **普查面须按三面枚举**：任何可解析性普查（PI 六项之 ⑥）**必须把 `.builtin-skills\` 计为独立第三面**，否则同名冲突分析**会系统性漏掉一份不同内容**（`docx/pdf/pptx/xlsx` 四枚已实证三面三哈希）。

---

## §5 诚实边界（逐条 · 不夸大 · 不误导）

1. **0 断言因果**：全件**不回答**「为什么失败」。§3 只登记事实与候选状态。
2. **0 次加载调用**：本棒**未发起任何 skill 加载调用** ⇒ **0 复现**失败、**0 复现**成功；§3 中 G4 涉及的现象沿前序件与姊妹件，**本棒 0 复现**。
3. **0 改配置 / 0 改 skill**：`config.yaml`、`skill-hub.json`、`.minimax\plugins\`、`.builtin-skills\`、plugin-cache 全部**只读**；**0 写入、0 移动、0 重命名、0 删除**。
4. **`config.yaml` 含 `apiKey` 值**：本棒**只统计键名与出现次数**（3 处），**0 读取值、0 记录值**；本件**不含**任何密钥/token/端点。`mcp.json`、`local-runtime.auth.json` 等含敏感值文件**未读**。
5. **转述不冒认**：§1.5 表中前两列（用户面 / plugin-cache 面哈希）转述自 `c14489750416` §2.2，**本棒未复测**；builtin 面一列为**本棒实测**。
6. **计数方法差异未即时校正**：本件涉及的行数/项数差异（如 `.builtin-skills` 20 目录 vs 21 项、既有件行数 vs 本棒行数）依 PI 现行口径**归 V4 收尾整理批量校正**，本棒**只如实登记**。
7. **并发写入面**：本棒开工时 `results/` 内有 parent 于 **16:09:26** 编辑的 `_d8_collection_ledger_2026_09_30.md`，且**另两只姊妹棒在跑**（可能于本棒之后写入 `results/`）⇒ **目录级「件数/总字节」前后快照不构成干净的 0 回改证据**；本棒 0 回改自证**限定于 §0 三件锚件的 SHA-12/字节/mtime 终态复算** ＋ **本棒写入面仅本件 1 件**。
8. **实时日志不可复现**：`runtime-2026093016.log` 处于追加中，其**字节数与字面计数随时间变化**（§2.4），本件所记**仅为时点值**。
9. **未读加载器实现**：解析优先级、同名冲突判定、`plugin:` 前缀解析代码**均未读**（§3.1、§4-2）。
10. **本件自身 SHA-12 无法内嵌**（自引用悖论）——落盘后由 parent 对**终态**复算并回填回执，本件**不预填**。

---

## §6 自核节

- **写入面**：**仅本件 1 件**（`results/_skill_load_failure_window_readonly_facts_2026_09_30.md`）。`results/` `docs/` `letters/` `deposon_team/` 内**既有件 0 回改、0 覆写、0 删除、0 重命名**。
- **0 回改自证**：§0 三件锚件于本棒**开工前后** SHA-12 / 字节 / mtime **逐字一致**（`2fb5987f544d` / `c14489750416` / `644e0666fbc4`）；并发写入面已在 §5-7 划界。
- **撞名实测**：落名前 **2 轮**：4 目录直查 8/8 `exists=False` ＋ 全仓递归 glob 近名（`*erratum*` / `*load_failure*` / `*parent_success*` / `*readonly_facts*`）**0 命中**本件名（仅命中 5 个他件，**均非本件名**）；本件为**新建**，**0 覆写**。
- **编码 / 版式**：UTF-8 **无 BOM** · **LF**（0 CRLF）——落盘后**实测**核验（首字节 ＋ 全量 `\r` 计数），**不预填**。
- **哈希口径**：一律 `Get-FileHash -Algorithm SHA256`，全值算完**截前 12**；**非** SHA-1 冒充。
- **0 凭据**：**0 LLM 调用、0 API 调用、0 外部 URL**。
- **V1–V3 只读**：未触动任何 V1–V3 资产；`.minimax\skills\` / `.builtin-skills\` / plugin-cache / `.minimax\plugins\` / `config.yaml` **全部 0 写入**。
- **succeeded ≠ 跑完**：§1 / §2 逐面**列出实测值与 0 命中项**；§2.2 的「0 条加载器事件」如实计为**负向结果**，**未**以「已尽力查找」包装成正面结论。
- **署名**：**doc-writer**（`agent-0032834a3e04`）· 出件即本棒，**不冒认**他方名头。
- **本件自身 SHA-12 / 字节 / 行数**：由 parent **落盘后对终态复算**并回填回执（**自引用不可内嵌**，见 §5-10）。

---

## §7 追记（**追加行 · 2026-09-30 16:2x · 0 回改历史行**）

> **体例**：**追加**，**不回改** §0–§6 任何既有行。

### §7.1 锚件 #1 于本棒落盘后被**兄弟棒追加**（**非本棒所为**）

| 项 | 本棒实测（§0） | 追记时实测（终态） |
|---|---|---|
| `_v3_v4_achievements_inventory_2026_09_24.md` SHA-12 | `2fb5987f544d` | **`189ba84fc12e`** |
| 字节 / 行 / mtime | 192,292 / 1,915 / 2026-09-29 12:12:41 | **193,632 / 1,926 / 2026-09-30 16:15:41** |

- **变更方**：**兄弟棒 worker**（parent 派工第④项，执行件 `results/_skill_reference_update_and_user_surface_survey_2026_09_30.md`）；**本棒 0 写入该文件**。
- **变更形态**：**纯追加**（新增第 1917–1926 行）；**第 14 行逐字未变**（本棒亲验）。
- **对 §5-7 的收窄**：本棒 0 回改自证**范围＝写入面仅本件与姊妹件 2 个新件**；锚件哈希变化**归属兄弟棒**。原值 `2fb5987f544d` 仍登记于本件 §0 · `644e0666fbc4` §0.1 · `c14489750416` §0 #11。
- **对 §1.5 结论无影响**：本件关于三面哈希、注册面、日志面的全部实测值**均不涉及该原册**。
- **交叉引用**：该追加注记把正式勘误指向 `644e0666fbc4` §1，而 PI 拆件裁定后**正式落点为姊妹件 §1 E-01**；**本棒 0 回改他棒产出**，已如实登记于姊妹件 §6.3，**待 parent 裁**。

<!-- self-check-tail -->
