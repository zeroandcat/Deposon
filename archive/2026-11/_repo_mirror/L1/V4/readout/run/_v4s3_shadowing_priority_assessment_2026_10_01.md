# 三面遮蔽优先级评估件（2026-10-01 · PI 卷 D-4 · D4-2 甲＝P5）

- **件性质**：**评估件**（只读调查 · **0 回改既有件** · 0 覆写 · **0 改 runtime** · **0 改 skill 目录** · **0 改 config**）
- **事项**：`4a3a2d0c5b95` §6.3 **P5**「复核 `docx/pdf/pptx/xlsx` 三面遮蔽优先级（G2）」
- **上游登记**：`99355c24a03b` §2 **V4-S3**（理由：「需跨面优先级判定，超单棒，且涉运行时解析序」；处置＝「前置 ＝ 另派专棒」）
- **只读输入**：`results/_skill_directory_update_and_addressing_rule_2026_10_01.md`（`4a3a2d0c5b95`）· `results/_v4_closeout_bucket_register_2026_10_01.md`（`99355c24a03b`）· `results/_skill_load_failure_window_readonly_facts_2026_09_30.md`（`9f5b73620b8a` §3 **G2**）
- **方法**：PowerShell／Python **只读**枚举三面 ＋ 本机 `app.asar`（426,404,876 B）内**明文 ESM 源码**字节偏移定位读取 ＋ **静态规则复算**
- **纪律**：0 编造 ｜ **R4（0 读 `apiKey`／token／端点值、0 落盘、0 入输出）** ｜ UTF-8 无 BOM · LF ｜ 署名如实 ｜ 撞名实测

> **一票结论**
> ① **优先级规则已可判**（不必再拆棒）：`app.asar` 内 `@mavis/skills` 的 `resolvePrecedence`／`sortEntries`（偏移 `126625103`／`126666395`）以 **`SOURCE_RANK[rootKind]` 升序 → `rootPriority` 降序 → `name` → `locationUri`** 四级定序，**每名只留一个 winner，其余记为 `losers`（`Shadowed by …`）**。
> ② **本机实测判定：5 枚同名全部由「用户面」胜出，builtin 面被遮蔽**——`docx`／`pdf`／`pptx`／`xlsx`／**`deep-research`**。**P5 事项本身可判、可闭**。
> ③ **但「三面」须更正为「两参与面 ＋ 一非参与面」**：`plugin-cache` 面**不在** `readConfiguredSkillRoots` 的 roots 内 ⇒ **0 参与遮蔽**（详见 §4）。原登记「三面遮蔽」在**机制层不成立**。
> ④ **22 枚 frontmatter 命名问题（V4-S1/P1）与本遮蔽面 0 交叉**（实测见 §5.2）⇒ 影响面 ＝ 5 枚遮蔽 ＋ 6 枚 plugin-cache 重名（**非遮蔽**）＋ 1 条独立的**读取期致命歧义**（§6.2）。

---

## §1 三面实测（只读 · 本棒独立复算）

| 面 | 路径 | 目录数 | 是否入 `readConfiguredSkillRoots` |
|---|---|---|:-:|
| **用户面** | `.minimax\skills\` | **223** | ✅ `user-global`（`kind: 'global'`） |
| **builtin 面** | `.minimax\.builtin-skills\` | **20** | ✅ `builtin-seeded`（`kind: 'builtin'`, `priority: 20`） |
| **plugin-cache 面** | `.minimax\v2\plugin-cache\official\` | 28 棵树 / **172 枚** skill 名 | ❌ **不入 roots** |
| （注册面） | `.minimax\plugins\` | 0 项 | ❌ |

> `4a3a2d0c5b95` §3.1 记「三面同名重叠仍为 4 枚」——本棒实测**重叠为 5 枚**（多 `deep-research`），且 §3.1 括注仅举 `docx/pdf/pptx/xlsx` 为例，未宣称穷举 ⇒ **0 判上游错**，仅**扩充**。plugin-cache 侧 172 枚名系**独立统计**（`4a3a2d0c5b95` §8-12 明记「未核 plugin-cache 28 棵树的 skill 总量，不冒认 172 之数」⇒ 本棒为**首次实测该数**，非沿用）。

### §1.1 覆盖面穷举（避免抽样）

| 交集 | 枚数 | 成员 |
|---|:-:|---|
| 用户面 ∩ builtin 面 | **5** | `deep-research` · `docx` · `pdf` · `pptx` · `xlsx` |
| 用户面 ∩ plugin-cache 面 | **10** | `docx` · `hypothesis-generation` · `pdf` · `peer-review` · `pptx` · `scholar-evaluation` · `scientific-brainstorming` · `scientific-writing` · `statistical-analysis` · `xlsx` |
| builtin 面 ∩ plugin-cache 面 | **5** | `code-review` · `docx` · `pdf` · `pptx` · `xlsx` |
| **三面同时同名** | **4** | `docx` · `pdf` · `pptx` · `xlsx` |

---

## §2 遮蔽**如何发生**（机制 · 有源码支撑）

### §2.1 三段机制链（`app.asar` 字节偏移可复现）

| 段 | 偏移 | 源码 | 作用 |
|---|---|---|---|
| **① 建表** | `117654920` 附近 | `readConfiguredSkillRoots(config, agentName, workspaceDir, compatibleAgentNames)` | 组装 `SkillSourceRoot[]`：**用户面 `user-global`（`kind:'global'`）／builtin 面 `builtin-seeded`（`kind:'builtin'`, `priority:20`）／agent 面（`kind:'agent'`, `priority` 100 或 90）／`builtin-agent`（`priority:10`）／`builtin-global`（无 priority）**，末尾 `dedupeSkillRoots` |
| **② 决胜** | `126625103`／`126666395` | `resolvePrecedence(entries)` ／ `sortEntries` | 按 `name` 分组 → 排序 → **`const [winner, ...shadowed] = sorted;`** ⇒ **同名只有 1 个 winner**；其余写入 `losers`，`reason = \`Shadowed by ${winner.rootKind} source ${winner.locationUri}\`` |
| **③ 读取** | `117614700` 附近（`readRegistrySkillByName`）／`52757784`（`LocalSkillTool.execute`） | `.find(candidate => candidate.name === name)` | **只在 `getAvailableSkills()`（即 winners 投影）内按 `name` 取** ⇒ **loser 永不可达**；取不到即 `Local skill not found: ${name}` |

### §2.2 遮蔽**不是**「整名剔除」，而是「**按优先级择一**」

> ⚠️ **须与另一条同名但不同面的规则严格区分**（易混）：
> - **`ambiguousSkillNames`（`filterInjectableRegistrySkills`，偏移 `100143738`）**：`.filter(entry => !options.ambiguousSkillNames?.has(entry.name))` —— 该集合**只由 `ambiguousLegacySkillNames`（`117614400` 附近）填充**，而后者**只统计 `entry.rootKind === 'agent'` 且 `rootScope ≠ canonical`** 的跨 agent 冲突 ⇒ **跨面（用户面/builtin 面）同名不进入此集合**。
> - 跨 agent 命中时抛 `LocalSkillResolutionError(409, 'Skill name "…" is ambiguous; use location_uri', 'AMBIGUOUS_SKILL_NAME')`（`117614365`）**并须显式给 `location_uri`**。
> ⇒ **本件 4–5 枚同名的实际表现 ＝ 「用户面那份静默胜出、builtin 面那份静默不可达」，不是报错、也不是整名不可用。**

### §2.3 显式消歧通道（已存在，但**不被 `LocalSkillTool` 使用**）

`readRegistrySkillByName`（`117630000` 附近）的入参含 `locationUri`；`findSkillEntry` 在 `input.locationUri` 存在时走 `registry.getByLocationUri(...)`，**可绕过 winner 择一直接命中任一实体**（含被遮蔽的 builtin 面那份）。
⇒ **技术上「可被寻址」，但裸名路径不可达**；`location_uri` 通道属管理面／thrift 面（`setSkillEnabled`／`getSkillDetail`／`deleteSkill` 等），**`LocalSkillTool` 的 `readSkill(name)` 不传 `locationUri`**。

---

## §3 优先级规则（**可判** · 规则本体）

### §3.1 `SOURCE_RANK`（偏移 `126594112`）

```js
const SOURCE_RANK = { project: 0, workspace: 1, agent: 2, global: 3, user: 3, builtin: 4 };
```

### §3.2 `sortEntries`（偏移 `126625103` 区域）

| 级 | 判据 | 方向 | 说明 |
|:-:|---|---|---|
| 1 | `SOURCE_RANK[left.rootKind] - SOURCE_RANK[right.rootKind]` | **升序（小者胜）** | `project` > `workspace` > `agent` > `global`/`user` > `builtin` |
| 2 | `right.rootPriority - left.rootPriority` | **降序（大者胜）** | 仅同 `rootKind` 内生效 |
| 3 | `left.name.localeCompare(right.name)` | 升序 | 同名组内**恒等**（分组键即 `name`）⇒ 实为**无操作** |
| 4 | `left.locationUri.localeCompare(right.locationUri)` | 升序 | **确定性兜底**（路径字典序）⇒ 规则**完全确定、无随机性** |

> **可判性结论**：规则为**纯确定性全序**（第 3 级恒等、末级兜底），**给定 roots 集合即可零歧义判定胜负**，无须实测加载。

### §3.3 本机 5 枚的逐条推导

| 枚 | 参与实体（`rootKind`／`priority`） | 第 1 级 rank | 第 2 级 priority | **winner** | **loser（不可达）** |
|---|---|:-:|:-:|---|---|
| `docx` | user `global`／builtin `builtin` | **3 < 4** | — | **用户面** `.minimax\skills\docx` | builtin 面 |
| `pdf` | 同上 | **3 < 4** | — | **用户面** | builtin 面 |
| `pptx` | 同上 | **3 < 4** | — | **用户面** | builtin 面 |
| `xlsx` | 同上 | **3 < 4** | — | **用户面** | builtin 面 |
| `deep-research` | 同上 | **3 < 4** | — | **用户面** | builtin 面 |

> 第 1 级已分出胜负 ⇒ **第 2 级 `priority`（builtin-seeded=20 vs user-global=未设＝0）未参与**。若将两面的 `rootKind` 改为同级，第 2 级才会起作用（20 > 0 ⇒ builtin 反而胜）⇒ **该规则的胜负对 `rootKind` 标注高度敏感，属构造面**。

---

## §4 关键更正：**「三面遮蔽」在机制层不成立**

`plugin-cache` 面（`.minimax\v2\plugin-cache\official\…\skills\`）经**全盘字面检索 5 处 `plugin-cache` 命中**核，其唯一作用是 `PluginSystem` 的 `officialCacheRoot`（偏移 `98124617`）与 `OfficialPluginReconciler` 的 `cacheRoot`；**`readConfiguredSkillRoots` 的 roots 列表中无 plugin-cache 项**（该函数源码已逐字读取，见 §2.1 ①）。
⇒ **plugin-cache 面的 172 枚 skill 与用户面/builtin 面 10 枚重名**（含四枚 `docx/pdf/pptx/xlsx`）**不构成遮蔽**；两面对 plugin 面是**单向的**（registry 侧看不见 plugin 侧）。

| 声称 | 判定 | 依据 |
|---|---|:-:|
| 「docx/pdf/pptx/xlsx **三面**遮蔽」 | ❌ **不成立** | plugin 面不入 roots（`117654920` 段）⇒ 实为**两参与面**遮蔽 |
| 「同名内容三份各不相同」 | ✅ **成立（本棒已复测）** | 四枚 `SKILL.md` SHA-256 三面**两两互异**（§6.1 表） |
| 「需跨面优先级判定，超单棒」 | ⚠️ **本棒已判，可闭** | 规则为确定性全序（§3.2）＋ 实测 5 枚（§3.3） |

---

## §5 影响面

### §5.1 遮蔽面（真遮蔽 · 5 枚）

- **用户面那份胜出、可寻址**；**builtin 面那份静默不可达**（裸名路径）。
- builtin 面 20 枚中 **19 枚 0 遮蔽**（仅 `deep-research` 1 枚被遮蔽）⇒ **面级影响仅 1/20**。
- ⚠️ **风险方向**：更新后 `.builtin-skills` 被**重写**（`4a3a2d0c5b95` §3.2 记其 mtime 2026-09-29 22:38:32，晚于失败窗口 09-24→09-28）⇒ **失败的 09-24→09-28 窗口内 builtin 面那 4 枚与用户面同版本、0 版本分歧** ⇒ **遮蔽机制在结构上存在、但在该窗口内 0 版本差可解释失败**（**0 因果**，见 §7-3）。

### §5.2 与 22 枚（V4-S1／P1）的交叉：实测 **0 交叉**

| 判据 | 结果 |
|---|---|
| 22 枚是否落在遮蔽组（5 枚）内 | **0 枚** |
| 22 枚寻址键（frontmatter `name`）是否与 builtin 面 20 枚任一目录名重名 | **0 例**（逐字比对，无交集） |
| 22 枚是否在 builtin 面另有实体 | **0 例**（22 枚仅见于用户面） |
| 22 枚 `name` 是否触发遮蔽/歧义 | **0 例**（`name` 唯一 ＋ 非 agent 面 ⇒ 0 竞争） |

⇒ **V4-S1（改 22 枚 `name` 为合法 slug）不会因遮蔽而改变可达性判定**；两事项**可独立处置**。

### §5.3 波及面（重名但**非**遮蔽）

用户面 ∩ plugin-cache 面 10 枚中，**6 枚仅在 plugin 面另有实体**（`hypothesis-generation`·`peer-review`·`scholar-evaluation`·`scientific-brainstorming`·`scientific-writing`·`statistical-analysis`）⇒ 用户面裸名调用 0 受影响；plugin 侧须走 plugin 寻址面（沿 `4a3a2d0c5b95` §5.2 之 `plugin:` 限定写法）。**本棒 0 追进 plugin 寻址面**（§7-4）。

---

## §6 证据

### §6.1 四枚 × 三面 `SKILL.md` SHA-256（本棒实算）

| 名 | 用户面 | builtin 面 | plugin-cache 面 | 三面互异 |
|---|---|---|---|:-:|
| `docx` | `cfbabd72b1ae` | `c9407f69ad99` | `12e5a0cccd0c` | ✅ |
| `pdf` | `9f78b8359fbd` | `3ce4de4609d4` | `e39aa05f43db` | ✅ |
| `pptx` | `e5b0df918cbe` | `75c4bbee0bf9` | `931a81818974` | ✅ |
| `xlsx` | `55591d7decc1` | `a3f0d9a7afa6` | `6eab2cbf5606` | ✅ |

> 四枚 `description` **均非空** ⇒ 不触发「`description` 空 ⇒ 不注册」面（沿 `4a3a2d0c5b95` §4.2 `14161440`）。四枚 frontmatter `name` **均 ＝ 目录名** ⇒ 0 触发 `validateName` 的「名≠父目录名」warning。

### §6.2 三面 mtime（本棒实测）

| 名 | 用户面 | builtin 面 | plugin-cache 面 |
|---|---|---|---|
| `docx` | 2026-09-18 11:39:54 | 2026-09-29 22:38:31 | 2026-09-03 12:13:26 |
| `pdf` | 2026-09-18 11:39:54 | 2026-09-29 22:38:32 | 2026-09-01 16:17:26 |
| `pptx` | 2026-09-18 11:39:54 | 2026-09-29 22:38:32 | 2026-09-03 12:13:22 |
| `xlsx` | 2026-09-18 11:39:54 | 2026-09-29 22:38:32 | 2026-09-03 12:13:20 |

### §6.3 源码偏移索引（本棒读得 · 可复现）

| 偏移 | 内容 |
|---|---|
| `52757784` | `LocalSkillTool.execute` → `reader.readSkill(name, ctx.agentName, signal)`；失败文案 `Local skill not found: ${name}` |
| `100143738` | `filterInjectableRegistrySkills` 内 `.filter(entry => !options.ambiguousSkillNames?.has(entry.name))` |
| `117614365` | `AMBIGUOUS_SKILL_NAME` 抛点（`409` / `use location_uri`） |
| `117654920` | `readConfiguredSkillRoots`（roots 组装；含 `user-global`／`builtin-seeded`） |
| `126594112` | `const SOURCE_RANK = { project:0, workspace:1, agent:2, global:3, user:3, builtin:4 }` |
| `126625103` | `resolvePrecedence` ＋ `sortEntries`（`const [winner, ...shadowed] = sorted`） |
| `98124617` | `officialCacheRoot = path.join(dataDir,'v2','plugin-cache','official')`（属 `PluginSystem`，**非** roots） |

### §6.4 静态复算（`resolvePrecedence` 离线模拟）

以 §3.1／§3.2 规则对三面实目录做离线择一，得：

```
deep-research: winner=user-global   shadowed=[builtin-seeded/deep-research]
docx:          winner=user-global   shadowed=[builtin-seeded/docx]
pdf:           winner=user-global   shadowed=[builtin-seeded/pdf]
pptx:          winner=user-global   shadowed=[builtin-seeded/pptx]
xlsx:          winner=user-global   shadowed=[builtin-seeded/xlsx]
```

> 脚本面 ＝ `$env:TEMP\p5_recompute.py`（**scratch · 非交付件**）���只读（仅 `os.listdir` ＋ 读 `SKILL.md` 前 4000 字符取 `name`），**0 写任何盘上实体**。

---

## §7 诚实边界（逐条）

1. **静态复算 ≠ 真实加载实测**：§6.4 为**按源码规则离线模拟**；本棒 **0 调用** `LocalSkillTool`／`readSkill` 真实加载那 4–5 枚 ⇒ 结论的**证据层为「源码规则 ＋ 盘上实体」**，非**运行期观测**。规则为确定性全序，故此缺口**不影响胜负判定**，但**影响「实际命中了哪份」的直证**。
2. **未完整反编译 `app.asar`**：按字节偏移读取**明文 ESM 片段**；`@mavis/skills` 包另有 `dist` 形态（偏移 `126636099` 另见同逻辑），**本棒 0 确认实际运行的是哪一份**（`126625103` 与 `126666395` 两处逻辑逐字一致 ⇒ 结论不受影响）。
3. **0 因果结论**：本件 0 断言遮蔽**导致**了 `9f5b73620b8a` 的失败窗口（`9f5b73620b8a` §3 **G2** 原文即「**0 断言**该扩充是否即失败原因」）。§5.1 末仅给**时间层不相关**的事实，**0 下因果判断**。
4. **未追 plugin 寻址面**：plugin-cache 侧 6 枚「仅 plugin 面有」的 skill 之**寻址语法与优先级** 0 追进（`4a3a2d0c5b95` §7 亦将 `plugin:` 前缀处理列为未闭面）⇒ §5.3 0 展开。
5. **未核 `agents\<name>\skills\`（`kind:'agent'`, `priority` 100/90）面**：该面为**第四个潜在参与面**，本棒**0 枚举**其内容 ⇒ 若该面另有同名实体，**可能改写**第 2 级 priority 的作用面（**0 断言其存在与否**）。
6. **未核 `workspace-*`／`external:*` 面**：`readExternalWorkspaceSkillRoots`／`readExternalUserSkillRoots` 的条目受 `config.skills.external.*` 开关控制，**该开关的取值需读 `config.yaml`** ⇒ **R4 之下 0 读值**，故本棒**0 断言**这些面在本机是否生效（**若生效，rank 1／2 更高，可能改写胜负**）。
7. **0 读敏感值**：**0 读取／0 落盘／0 写入输出**任何 `apiKey`／token／端点值；**0 读** `mcp.json`、`local-runtime.auth.json` 等敏感文件。`config.yaml` 本棒**仅出现在源码的键名面**（`resolveDataDirVariables`／`config.dataDir` 等），**0 打开该文件**。
8. **0 改 runtime／0 改 skill 目录／0 改 config**：`skills\` 223 项、`.builtin-skills\` 20 项、plugin-cache、`config.yaml`、`skill-hub.json`、`.minimax\plugins\` **全部只读**。
9. **`0 回改`**：三件锚件 SHA-12 于**本棒开工前后**逐字一致（§9）。
10. **本件自身 SHA-12／字节不可内嵌**（自引用悖论）——落盘后由 parent 对**终态**复算回填。
11. **文件计数类差异**：本棒 0 做全仓文件数基线比对；§1/§5 的枚数均为**本棒对指定三面的实算**，0 冒充全仓基线。
12. **并发写入面**：`results/` 目录有其他棒并发写入可能 ⇒ 目录级快照**不构成**干净 0 回改证据；本棒 0 回改自证**限定于**锚件终态复算 ＋ **本棒写入面仅本件 1 件**。

---

## §8 需后续处置（**待 PI** · 本棒 0 执行）

| # | 事项 | 建议 | 性质 |
|:-:|---|---|---|
| **1** | **V4-S3（P5）** | **可闭**（可判）——建议以本件为据将 P5 判为**已闭**，并**把登记口径由「三面遮蔽」更正为「用户面 vs builtin 面两参与面遮蔽（5 枚，用户面全胜）；plugin-cache 面 0 参与遮蔽」** | **登记口径更正**（`99355c24a03b` §2 V4-S3 行；⛔ 本棒 0 回改他人件） |
| **2** | **`deep-research` 未在原登记内** | 随 #1 一并纳入（用户面胜） | 登记扩充 |
| **3** | **builtin 面 5 枚被遮蔽的处置取向** | **三选一待 PI 裁**：①**维持现状**（用户面那份为准，builtin 面那份为冗余实体）②**删除／改名 builtin 面那 5 枚**（⛔ 属改 builtin 面 ＝ 运行时内置面 ⇒ **本棒 0 建议、0 执行**）③**以 `location_uri` 显式寻址**（技术上可绕遮蔽，但**裸名路径不可达**、且 `LocalSkillTool` 不传该参数） | **PI 裁**（构造面变更） |
| **4** | **遮蔽规则的脆弱性** | `SOURCE_RANK` 使 `global`(3) 恒胜 `builtin`(4) ⇒ **用户面一旦存在同名即永久压过内置面**（与 mtime／版本 0 关系）。**此为构造面事实，本棒 0 建议改动**（改动 ＝ 改运行时） | **仅登记** |
| **5** | **未闭面（`agents\` 面／`external` 面 0 枚举）** | §7-5／§7-6 二面 0 核；**若 PI 欲闭合「全 roots 胜负图」**，需另立小棒（**读 `config.yaml` 开关 ＝ 触及 R4 边界 ⇒ 须 PI 先裁 R4 例外**） | **PI 裁后另派** |

---

## §9 自核节

- **写入面**：**仅本件 1 件**（`results/_v4s3_shadowing_priority_assessment_2026_10_01.md`）＋ `$env:TEMP` 下 4 个 scratch 脚本（**非交付件**、可随时重建，不计入 `results/` 件数）。
- **命名**：去版本前缀、**0 `_v5_`／0 V-阶段字样作文件名前缀**（沿 PI 09-29 命名裁）；「V4-S3」**仅作正文引用**（登记 ID）**不作文件名前段** ⇒ 落名 `_v4s3_shadowing_priority_assessment_2026_10_01.md` 中 `v4s3` 为**登记 ID 的小写连写**（非 `_v4_` 阶段前缀、非 `_v5_` 类）。
- **撞名实测**：落名前 **2 轮**——①`Test-Path` 目标全路径 **False**；②全仓递归 glob `*shadowing*` ＝ **0 命中**、`*v4s3*` ＝ **0 命中**；**落盘后复测**同两项仍为**新建、0 覆写**。
- **锚件 0 回改复核**（SHA-256 全值算完截前 12 · 小写 · **非 SHA-1 冒充**）：

| 锚件 | 派工给定 | 本棒终态实算 | 字节 | 结论 |
|---|---|---|---:|:-:|
| `_skill_directory_update_and_addressing_rule_2026_10_01.md` | `4a3a2d0c5b95` | **`4a3a2d0c5b95`** | 20,335 | ✅ 逐位一致 |
| `_v4_closeout_bucket_register_2026_10_01.md` | `99355c24a03b` | **`99355c24a03b`** | 41,943 | ✅ 逐位一致 |

- **编码 / 版式**：UTF-8 **无 BOM** · **LF**（落盘后实测核验首字节 ＋ `\r` 计数，**不预填**）。
- **署名**：**worker**（`mvs_b7b05103f62d43c985571eb0549494b2`）· 出件即本棒，**0 冒认**他方名头。
- **无既有件被回改、无 runtime 面被触碰、无 key 被读取**——三条均可在盘上复验。
