# G4 追因棒 · `registryProvider.readSkillByName` 内部追因（2026-10-01 · 纯只读）

> **棒别**：G4 追因棒（worker 棒，parent 于 PI 卷 D-4 `ask_72a7168ab10822dc2585e594` D4-2 派工）。
> **任务**：追进 `registryProvider.readSkillByName` 内部——读 `plugin:` 前缀处理与闸门判定（`resolveReadScope(scope.agentName,…)` 按 agent 名分域 ＋ `allowedSkillNames` 闸门），解释 `9f5b73620b8a` §3 **G4**「同写法同实体同日两会话结果相反」。
> **版式**：UTF-8 无 BOM · LF · 去版本前缀（沿 PI 09-29 命名裁，⛔ 无 `_v5_` 类阶段字样）。
> **写入面**：**仅本件 1 件** ＋ `.tmp\g4_read_scope_trace_2026_10_01\` 下 5 个 scratch 脚本（不属交付件）。

---

## §0 只读面清单与读法

| 面 | 实体 | 读法 | 状态 |
|---|---|---|---|
| 锚件① | `results/_skill_directory_update_and_addressing_rule_2026_10_01.md`（`4a3a2d0c5b95`） | 读 §4.2／§7 | 只读，0 写 |
| 锚件② | `results/_skill_load_failure_window_readonly_facts_2026_09_30.md`（`9f5b73620b8a`） | 读 §3 G4／§4-2／§5 | 只读，0 写 |
| 代码面 | `%LOCALAPPDATA%\Programs\MiniMax Code\resources\app.asar`（**426,404,876 B** · mtime **2026-09-29 22:25:34**） | `open(path,'rb')` → `seek` → 按字节偏移逐行 dump（UTF-8 `errors='replace'`） | 只读，0 写 |
| 盘上存在性面 | `<dataDir>\skills`／`.builtin-skills`／`agents\*`／安装目录 `assets\*` | 仅 `Test-Path`／目录枚举 | 只读，0 写 |

### §0.1 R4 遵守声明（`config.yaml`）

- 本棒**未打开、未读取** `config.yaml`（含 `apiKey` 等密钥字段，**值未读**）。
- 本棒**未读取** `mcp.json`、`local-runtime.auth.json` 等含敏感值文件。
- 本件**不含**任何密钥／token／端点值；凡涉 `dataDir` 一律沿**运行时 `activeDataDir`**（`C:\Users\Administrator\.minimax`）与**存在性探测**得出，**0 由配置值推导**。
- 本棒**0 落盘**任何配置值（写入面仅本件 ＋ scratch 脚本）。

---

## §1 追因结论（先给结论，再给证据）

| id | 命题 | 判定 | 依据强度 |
|---|---|---|---|
| **C1** | **skill 读取路径上根本不存在 `plugin:` 前缀处理** | ✅ **闭**（确定性、**与会话无关**） | 全文件字面量穷举 ＋ 终判定式逐字 |
| **C2** | 「同写法同实体同日两会话结果相反」**不能**由 agent 域分域／`expectedAgentInstanceId` 解释 | ✅ **闭（本机）** | 源码 ＋ 盘上实测：agent 根域全不存在 ⇒ 零效力 |
| **C3** | 读取路径上**唯一**的会话级差异载体是 `allowedSkillNames`／`allowedExtensionSkillNames` | ⚠️ **机制闭・取值未闭**（**不下因果结论**） | 源码闭；取值不在盘上可读面 |
| **C4** | `disabledLocationUris` **不是**跨会话载体 | ✅ **闭** | 唯一实现为进程内存 `Set` |
| **C5** | beta flags／region／`frontmatter.listed`／`mcp-` 同名遮蔽 **均非**会话级 | ✅ **闭** | 逐条源码 |

**一句话**：追进内部后得到的是**否证**而非确认——`plugin:` 前缀在代码上**不存在**（故 `plugin:skill` 必败，且**与两会话无关**）；而 G4 的两会话差异，其在代码中**唯一**可承载者 `allowedSkillNames` **取值不在只读可及面**，agent 域假设在本机**实测无效**。⇒ **G4 仍未闭**，本棒交付的是**已闭的 C1／C2／C4／C5 ＋ 已定位的 C3 承载点**，⛔ **0 下因果结论于未读面**。

---

## §2 C1：`plugin:` 前缀处理 —— 穷举否证（本棒最硬的一条）

### §2.1 全文件字面量穷举（`app.asar` 全文 426,404,876 B）

| 检索形态 | 命中数 |
|---|---|
| `'plugin:'`（单引号字面量） | **0** |
| `"plugin:"`（双引号字面量） | **0** |
| `` `plugin: ``（模板串开头） | 15（**逐条查验，均非前缀解析**，见 §2.2） |
| `plugin:`（裸串） | 376 |
| `plugin://` | **0** |
| `PLUGIN_PREFIX` | **0** |
| `parsePluginSkill` / `splitPluginQualified` / `qualifySkillName` / `pluginQualified` / `pluginSkillName` / `plugin-qualified` | **各 0** |

⇒ **无任何前缀常量、无任何前缀切分函数**。

### §2.2 376 处 `plugin:` 的真实用途（抽样 41 条带引号/比较符的命中，逐条查验）

| 用途 | 例（偏移） | 是否前缀解析 |
|---|---|---|
| 对象属性键 `plugin:` | `93797313` `plugin: input.plugin,` | ❌ |
| 事件名 | `104610302` `'plugin:close'` | ❌ |
| React 列表 key | `306730540` `` key:`plugin:${t.name}` `` | ❌ |
| i18n 键 | `294084856` `"plugin_management.search_placeholders.plugin"` | ❌ |
| **App/MCP `tool_ref` 约定** | `118078432` `tool_ref: 'plugin:browser-use:browser-control'` | ❌（属 **MCP/App 工具寻址**，非 skill 寻址） |

### §2.3 ★ 终判定式（`app.asar` 偏移 `100153797` `readRegistrySkillByName`）

```js
export function readRegistrySkillByName(registry, name, options = {}) {
    const ambiguous = ambiguousLegacySkillNames(registry, options);
    const entry = filterInjectableRegistrySkills(registry.getAvailableSkills(), {
        agentName: options.agentName,
        compatibleAgentNames: options.compatibleAgentNames,
        builtinSkillNames: readShippedBuiltinSkillNames(registry),
        betaFlags: options.betaFlags,
        injectableBuiltinSkillNames: options.injectableBuiltinSkillNames,
        allowedSkillNames: options.allowedSkillNames,
        allowedExtensionSkillNames: options.allowedExtensionSkillNames,
        mcpServerNames: options.mcpServerNames,
    }).find((candidate) => candidate.name === name);
    if (!entry || options.disabledLocationUris?.has(entry.locationUri))
        return undefined;
    if (ambiguous.has(name)) {
        throw ambiguousSkillNameError(name, ambiguousLegacyLocations(registry, name, options), options.resourceAmbiguityTelemetry);
    }
    return { content: entry.content, locationUri: entry.locationUri, sourceKind: entry.rootKind };
}
```

**`.find((candidate) => candidate.name === name)` 是全等、大小写敏感、无归一化、无前缀剥离的比较。**

### §2.4 `name` 的来源全程无加工（偏移 `52757967` `LocalSkillTool.execute`）

```js
const name = (typeof input.name === 'string' && input.name.trim()) || 'unknown-skill';
const skill = await this.reader.readSkill(name, ctx.agentName, signal);
if (!skill) {
    const text = `Local skill not found: ${name}`;
```

⇒ 入参仅 `trim()`，**此后逐字透传**至 §2.3 的全等比较。

### §2.5 `plugin:skill` 形态字符串的唯一真实出处（偏移 `100190163`）

```js
function isDesktopExtensionSkillSelected(allowedSkillNames, selected, pluginName, skillName) {
    const name = normalizedSkillName(skillName);
    const qualified = `${normalizedSkillName(pluginName)}:${name}`;
    const includes = (values) => values?.some((candidate) => {
        const normalized = normalizedSkillName(candidate);
        return normalized === name || normalized === qualified;
    }) ?? true;
    return includes(allowedSkillNames) && includes(selected);
}
```

⚠️ **诚实边界**：此处确有 `plugin:skill` 形态，但它是**白名单选择器形态**（比对 `allowed*` 列表），且只服务于 `readNativeSkill` 的 `desktopSkills` **兜底路径**（`100189563`），**不服务** `LocalSkillTool`。且 `toNormalizedSkillSelectorSet`（`100144715`）**不按 `:` 切分** ⇒ 白名单里写 `plugin:skill` 也匹配不到名为 `skill` 的条目。

### §2.6 C1 判定

> **`plugin:` 前缀在 skill 读取路径上不存在任何处理器。** `plugin:<x>` 只可能命中「名字字面就是 `plugin:<x>`」的条目 ⇒ **必然 `Local skill not found`**，且该结果**与会话、日期、agent 域、闸门取值全部无关**（确定性）。
>
> ⇒ **C1 完全解释**前序件 `644e0666fbc4` 的「`plugin:skill` 8/8 全败」；⇒ **C1 不能解释 G4**（G4 是**同写法**两会话相反）。
> ⇒ 附带线索（非结论）：`plugin:` 的真实约定域是 **App/MCP `tool_ref`**（`118078432`），`plugin:skill` 写法**可能**源于两套约定混用——**本棒 0 证据**证明该写法从何而来。

---

## §3 C2：agent 域分域与 `expectedAgentInstanceId` —— 机制真实，本机实测无效

### §3.1 机制（逐字）

**（a）scope 归一（偏移 `100194348`）**
```js
async readSkillByName(name, scope = {}) {
    try {
        const readScope = await resolveReadScope(scope.agentName, scope.excludeAgentResources ||
            scope.skipAgentResolution ||
            Boolean(scope.expectedAgentInstanceId));
        const result = await registryProvider.readSkillByName(name, {
            agentName: readScope.canonicalName,
            ...(deps.resolveAgentReadScope ? { compatibleAgentNames: readScope.compatibleNames } : {}),
            workspaceDir: scope.workspaceDir,
            ...
            ...resolveRuntimeSkillOptions(scope),
        });
```
⚠️ **同一个 `Boolean(scope.expectedAgentInstanceId)` 同时**（i）跳过 agent 名解析、（ii）触发后续 §3.1(c) 的**静默降级**。

**（b）`resolveReadScope`（偏移 `100190947`）**
```js
const resolveReadScope = async (requestedName, skipAgentResolution = false) => {
    const requested = normalizeAgentName(requestedName);
    if (skipAgentResolution || !deps.resolveAgentReadScope) {
        return { canonicalName: requested, compatibleNames: [requested] };
    }
    const resolved = await deps.resolveAgentReadScope(requested);
    const canonicalName = resolved.canonicalName.trim() || requested;
    const compatibleNames = [canonicalName, ...(resolved.compatibleNames ?? [])].filter(...);
    return { canonicalName, compatibleNames };
};
```
`normalizeAgentName`（`100196313`）：`const trimmed = agentName?.trim(); return trimmed || 'mavis';`

**（c）★ 静默降级（偏移 `100138037` `createAgentResourceScopeReader`）**
```js
export function createAgentResourceScopeReader(dataDir) {
    return async (scope, read) => {
        const { expectedAgentInstanceId } = scope;
        if (!expectedAgentInstanceId || scope.excludeAgentResources)
            return read(scope);
        const matches = () => matchesAgentResourceInstance(dataDir(), scope.agentName, expectedAgentInstanceId);
        const unavailable = () => read({ ...scope, excludeAgentResources: true });
        if (!(await matches()))
            return unavailable();
        try {
            const result = await read(scope);
            // A cached URI or registry is not proof that the original Agent still owns the files.
            return (await matches()) ? result : unavailable();
        }
        catch (error) {
            if (!(await matches()))
                return unavailable();
            throw error;
        }
    };
}
```
⇒ **读前、读后各校验一次 ownership；任一次不过即静默改走 `excludeAgentResources: true`**——**不抛错、不记日志**。这与 `9f5b73620b8a` §2.2「日志中不存在 skill 加载事件」**方向一致**（该面无事件可查）。

**（d）ownership 判据（偏移 `125214721` `matchesAgentResourceInstance`）**
```js
export async function matchesAgentResourceInstance(dataDir, agentName, expectedInstanceId) {
    if (!agentName ||
        !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/iu.test(expectedInstanceId))
        return false;
    const agentsDir = resolve(dataDir, 'agents');
    const agentDir = resolve(agentsDir, agentName);
    if (dirname(agentDir) !== agentsDir) return false;
    const marker = join(agentDir, '.agent-instance-id');
    try {
        const directory = await lstat(agentDir);
        if (!directory.isDirectory() || directory.isSymbolicLink()) return false;
        const before = await lstat(marker);
        if (!before.isFile() || before.isSymbolicLink() || before.size > 128) return false;
        const value = (await readFile(marker, 'utf8')).trim();
        const after = await lstat(marker);
        return (value === expectedInstanceId && after.isFile() && !after.isSymbolicLink()
            && after.ino === before.ino && after.dev === before.dev && after.mtimeMs === before.mtimeMs);
    }
    catch {
        // Private resources are optional; a missing/unreadable marker cannot block a frozen Session.
        return false;
    }
}
```
⚠️ **本棒实测**：`.agent-instance-id` 仅存于 4 个 `agent-*` 目录（`agent-0032834a3e04`／`agent-11335500b168`／`agent-3a4d09ba3c90`／`agent-3e0c193da529`，mtime 均 **2026-09-16**）；**`mavis`／`verifier`／`.builtin` 三目录无该标记**。⇒ 若 `agentName='mavis'` 且带 `expectedAgentInstanceId`，`lstat(marker)` 抛错 ⇒ `catch` ⇒ **恒 `false`** ⇒ **恒走降级路径**。
⚠️ **本棒 0 读标记内容**（仅测存在性／字节数／mtime），故**不报**任何 id 值。

**（e）根域裁剪（偏移 `100165880` `getHandleForAgent`）**
```js
const { agentName, workspaceDir, compatibleAgentNames, excludeAgentResources = false, expectedAgentInstanceId, } = scope;
const resolvedAgentName = normalizeAgentName(agentName);
const configuredRoots = rootsGetter?.(resolvedAgentName, workspaceDir, compatibleAgentNames) ??
    readConfiguredSkillRoots(configGetter(), resolvedAgentName, workspaceDir, compatibleAgentNames);
const roots = excludeAgentResources
    ? configuredRoots.filter((root) => root.kind !== 'agent' && !(root.kind === 'builtin' && root.scope))
    : configuredRoots;
const rootsKey = JSON.stringify([expectedAgentInstanceId, roots]);
```
⇒ 降级**只**剔除 `agent-user:*` 与 `builtin-agent:*`（带 `scope` 的 builtin）两类根；**`user-global`、`builtin-seeded`、`builtin-global` 一律保留**。

### §3.2 根域全表（偏移 `100178053` `readConfiguredSkillRoots` 逐字）

| 根 id | kind | scope | rootPath | priority | 本机存在性（只读实测） |
|---|---|---|---|---|---|
| `agent-user:<name>` | `agent` | `<name>` | `<dataDir>/agents/<name>/skills` | 100（首）/ 90 | ❌ **7/7 全部不存在** |
| `user-global` | `global` | — | `<dataDir>/skills` | — | ✅ 存在，**223** 目录 |
| `builtin-seeded:<dir>` | `builtin` | — | `resolveBuiltinSkillsDir(config)` → `<dataDir>/.builtin-skills` | 20 | ✅ 存在，**20** 目录 |
| `builtin-agent:<primary>:<dir>` | `builtin` | `<primary>` | `<agentsDir>/<primary>/skills` | 10 | ❌ 候选目录（安装目录 `assets/agents`）**不存在** |
| `builtin-global:<dir>` | `builtin` | — | `<skillsDir>` 候选 | — | ❌ 候选目录（安装目录 `assets/skills`）**不存在** |

（`getBuiltinSkillsDirCandidates` / `getBuiltinAgentsDirCandidates`：偏移 `100015271` / `100015713`，候选为 `MAVIS_BUILTIN_*_DIR` 环境变量 ＋ 若干相对路径；本棒实测**全部不存在**。`BUILTIN_SKILLS_DIR_NAME = '.builtin-skills'` @ `100177865`。）

### §3.3 ★ C2 判定（本机）

> 本机 registry 的**有效 skill 集 100% 来自两个无 `scope` 的根**（`user-global` 223 ＋ `builtin-seeded` 20）。
> ⇒ `agentName` ／ `compatibleAgentNames` ／ `expectedAgentInstanceId` ／ `excludeAgentResources` 在本机**对该 243 项的可达性零效力**。
> ⇒ **agent 域假设不能解释本机的 G4 现象。C2 闭（本机）。**
>
> ⚠️ 口径限制：此判定**仅对本机当前盘上态**成立。若将来出现 `agents/<name>/skills` 或安装目录 `assets/*`，该机制**立即复活**——这是**条件性闭**，不是普适否证。

---

## §4 C3：`allowedSkillNames` 闸门 —— 唯一会话级载体，但取值未闭

### §4.1 闸门链（偏移 `100143457` `filterInjectableRegistrySkills`，逐字）

```js
export function filterInjectableRegistrySkills(entries, options = {}) {
    const betaFlags = options.betaFlags ?? {};
    const builtinSkillNames = options.builtinSkillNames ?? new Set();
    return filterSkillsVisibleToAgent(entries, options)
        .filter((entry) => !options.ambiguousSkillNames?.has(entry.name))
        .filter((entry) => entry.frontmatter.listed !== false)
        .filter((entry) => !entry.name.startsWith('mcp-') || !options.mcpServerNames?.has(entry.name.slice(4)))
        .filter((entry) => options.allowedSkillNames?.has(normalizeSkillSelectorName(entry.name)) ?? true)
        .filter((entry) => entry.rootKind === 'builtin' ||
        (options.allowedExtensionSkillNames?.has(normalizeSkillSelectorName(entry.name)) ?? true))
        .filter((entry) => {
        if (!options.injectableBuiltinSkillNames) return true;
        return (!builtinSkillNames.has(entry.name) ||
            (entry.rootKind !== 'builtin' && entry.rootKind !== 'agent') ||
            options.injectableBuiltinSkillNames.has(entry.name));
    })
        .filter((entry) => isSkillAllowedByBetaFlags(entry, betaFlags));
}
```

配套（`100144715` / `100144598`）：
```js
export function toNormalizedSkillSelectorSet(values) {
    return values === undefined
        ? undefined
        : new Set(values.map(normalizeSkillSelectorName).filter(Boolean));
}
function normalizeSkillSelectorName(value) {
    return value.trim().normalize('NFKC').toLocaleLowerCase('en-US');
}
```

**闸门语义**：`allowedSkillNames` **仅当 `!== undefined`** 时成为闸门；一旦有值，**不在集合内的条目一律被丢弃** ⇒ 同一 `name` 在「集合内会话」命中、在「集合外会话」返回 `undefined` ⇒ `Local skill not found`。选择器侧 NFKC＋小写归一，**条目侧（§2.3）却是全等** ⇒ 大小写/全半角差异只影响闸门、不影响查找。

### §4.2 载体位置（偏移 `100186675` `resolveHostedCatalogScope`）

```js
...(scope.allowedSkillNames === undefined ? {} : { allowedSkillNames: scope.allowedSkillNames }),
...(scope.allowedExtensionSkillNames === undefined ? {} : { allowedExtensionSkillNames: scope.allowedExtensionSkillNames }),
```
⇒ 二者**只在调用 scope 里逐层透传**；同函数中 `resolveHostedSelection`（`100187723`）**只**覆写 `builtinSkillNames`，**不**改 `allowed*`。

### §4.3 ★ C3 判定

> 这是本棒在读取路径上找到的**唯一**会话级差异载体，且它**只存在于调用 scope、不落任何状态文件** ⇒ 与 `9f5b73620b8a` §3 G4②「把全部可及注册面探完后，仍未找到任何『按会话区分』的 skill 状态载体」**并不矛盾、反而互补**：载体**不在文件里，在 scope 里**。
>
> ⛔ **本棒不下因果结论**：两观察会话的 `allowedSkillNames` 取值**不在只读可及面**（不在盘上、不在 `config.yaml`——后者本棒 0 读）。**0 复现、0 断言**。
> ⛔ **可闭性受限**：该运行时**不记 skill 加载事件**（`9f5b73620b8a` §2.2）⇒ 该取值**无法**从盘上回溯。

---

## §5 C4／C5：已闭的其余候选（逐条）

| id | 候选 | 源码依据 | 判定 |
|---|---|---|---|
| **C4** | `disabledLocationUris` 跨会话残留 | 偏移 `100177048` `createProcessLocalSkillEnabledState`：`const disabled = new Set();` 纯内存；`getDisabledLocationUris: async () => new Set(disabled)`。**全文件 `getDisabledLocationUris` 仅此一处实现**（另 23 处皆为调用点） | ✅ **闭**：进程退出即失，**不是**跨会话载体 |
| **C5-a** | beta flags 分会话 | 偏移 `100190681`／`100143188`：`betaFlags()` 取 `deps.configGetter().beta`（**全局配置**，非会话）；`isSkillAllowedByBetaFlags` 只看 `frontmatter.requiresBeta` | ✅ **闭**：全局量 |
| **C5-b** | region 差异 | 偏移 `100010164`／`100010227`：`CN_DISABLED_BUILTIN_SKILLS = new Set(['x-link-reader'])`；`isLocalBuiltinSkillEnabled(name) { return getRuntimeRegion() !== 'cn' || !CN_DISABLED_BUILTIN_SKILLS.has(name); }`（经 `isVisibleLocalSkill` @ `100143058` 生效） | ✅ **闭**：**机器级**量，**同机同日不可能变**；且仅影响 `x-link-reader` 一枚 |
| **C5-c** | `frontmatter.listed` | `100143776`：`.filter((entry) => entry.frontmatter.listed !== false)` | ✅ **闭**：**随实体**走，同实体同日同值 |
| **C5-d** | `mcp-` 前缀遮蔽 | `100143839`：`!entry.name.startsWith('mcp-') \|\| !options.mcpServerNames?.has(entry.name.slice(4))` | ✅ **闭**：随实体＋随 MCP 配置，**非会话量** |
| **C5-e** | 三面同名（`docx/pdf/pptx/xlsx`）致歧义**抛错** | `100153797`：`if (ambiguous.has(name)) throw ambiguousSkillNameError(...)`（`100142516`：`LocalSkillResolutionError(409, 'Skill name "…" is ambiguous; use location_uri', 'AMBIGUOUS_SKILL_NAME')`）；`ambiguousLegacySkillNames`（`100140865`）**只统计 `rootKind === 'agent'` 且 `rootScope` 跨域同名** | ✅ **闭（本机）**：本机 agent 根域全不存在 ⇒ 歧义集**恒空**；且歧义是**抛错**、**不是** `not found`，与 G4 的现象形态不同 |
| **C5-f** | registry 首次加载竞态 | 偏移 `100145889` `createRegistryHandle`：`registryPromise: (async () => { const createdRegistry = await createSkillRegistry(roots); … })()`；`100173342` `const registry = await handle.registryPromise;` | ⚠️ **减弱但未闭**：读前必 `await` ⇒ 同一 handle 内**无首读竞态**；但 `rootsKey` 含 `expectedAgentInstanceId`（`100166528`）⇒ 不同实例 id 持有**各自独立 registry**；watcher 驱动的刷新时序本棒**未读** |

---

## §6 反方意见与未闭面（逐条 · 诚实登记）

1. **⛔ G4 仍未闭。** 本棒交付的是 4 条已闭否证 ＋ 1 条已定位载体，**不是** G4 的答案。任何「G4 已解」的表述都超出本棒证据力。
2. **C2 是条件性闭。** §3.3 的效力依赖「agent 根域不存在」这一**当前盘上态**。若他机／他时刻存在 `agents/<name>/skills`，则 §3.1(c) 的静默降级**立即成为一等的会话差异机制**，且因「不抛错、不记日志」，外部**不可观测**。**0 推广为本机以外结论。**
3. **C3 不可验证。** `allowedSkillNames` 取值不在盘上可读面；本棒**未**读取任何会话态数据。⇒ 「C3 即 G4 之因」是**假设**，本棒**只**将其定位为唯一候选载体。
4. **`@mavis/skills` 包未整体反编译。** `createSkillRegistry`（`100145942`）的 internals——尤其 `snapshot.winners` 的**同名多根 winner 选定规则与优先级仲裁**——本棒**0 读**。⇒ 与 G2（`docx/pdf/pptx/xlsx` 三面同名）直接相关的**优先级语义仍未闭**，本棒**不冒认**已定位。
5. **两处「可能混淆」只登记、不主张。**（i）`plugin:` 的真实约定域是 App/MCP `tool_ref`（`118078432`）⇒ `plugin:skill` 写法**或**源于约定混用——**0 证据**。（ii）`isDesktopExtensionSkillSelected` 存在 `plugin:skill` 形态比较（`100190163`）⇒ **或**为该写法的另一来源——但它只服务 `desktopSkills` 兜底，**不服务** `LocalSkillTool`。**二者均未证。**
6. **0 复现、0 发起任何 skill 加载调用。** 本棒全程**只读字节读取**，`registryProvider.readSkillByName` **0 次实际调用** ⇒ §2–§5 全部为**静态源码判读**，非运行时行为实测。
7. **偏移引用为字节级。** 全部偏移基于本机 `app.asar`（426,404,876 B · 2026-09-29 22:25:34）；**版本升级后偏移失效**，须按符号名重新定位（每个引用均已附函数名，可复现）。
8. **`app.asar` 内同一逻辑存在两份**（打包 JS @ ~100M 段 ＋ TS 源码 @ ~117M 段，偏移不同）。本件**统一引打包段（~100M）**，已在 §4.2 附 TS 段对照偏移一处；**0 逐条双录**。
9. **`.agent-instance-id` 内容 0 读。** 仅测存在性／字节数（37 B）／mtime。**不报**任何 id 值。
10. **本件自身 SHA-12／字节不可内嵌**（自引用悖论）——落盘后由 parent 对**终态**复算回填。

---

## §7 自核节

- **写入面**：**仅本件 1 件**（`results/_g4_skill_read_scope_trace_2026_10_01.md`）＋ `.tmp\g4_read_scope_trace_2026_10_01\` 下 **5 个 scratch 脚本**（`scan_offsets.py`／`dump_window.py`／`scan_range.py`／`dump_ctx.py`／`scan_prefix_forms.py`）——**非交付件**、可随时重建，不计入 `results/` 件数。
- **命名**：`_主题_日期`（去版本前缀、无 `_v5_` 类阶段字样，沿 PI 09-29 命名裁 ＋ 10-01 补记「派工建议名亦须合规」）。
- **撞名实测**：落名前 **2 轮 × 4 目录直查**（`results\`／仓根／`deposon_team\`／`docs\`）＝ **8/8 `exists=False`** ＋ **全仓递归**（`Get-ChildItem -Recurse` 两种模式 ＋ `glob **/*g4_skill_read_scope*`）**0 命中** ⇒ **新建，0 覆写**。
- **0 回改自证**：锚件 SHA-12／字节／mtime 于**本棒开工前后**逐字一致（§8 表）。
- **R4**：`config.yaml` **0 打开 0 读值**；**0 落盘**；**0 入输出**。本件仅以「含密钥字段，值未读」表述。
- **⛔ 0 改 runtime**：未写 `app.asar`、未写安装目录、未写 `<dataDir>` 下任何文件（`Test-Path`／`Get-ChildItem`／`Get-FileHash` 皆只读）。
- **⛔ 0 改 skill 目录**：`<dataDir>\skills`（223）、`<dataDir>\.builtin-skills`（20）、plugin-cache、`.builtin-skills` **全部只读**。
- **0 LLM / 0 API / 0 外部 URL**：全部证据来自本机盘上 ＋ 本机 `app.asar` 字节读取。
- **署名**：本件由 **G4 追因棒（worker 棒）** 产出；源码引用归属 MiniMax Code 运行时（`app.asar`）原作者；**0 冒认**他方为出证方。

---

## §8 0 回改复核（锚件终态哈希）

| 锚件 | SHA-12 | 字节 | mtime |
|---|---|---|---|
| `results/_skill_directory_update_and_addressing_rule_2026_10_01.md` | `4a3a2d0c5b95` | 20,335 | 2026-10-01 10:26:01 |
| `results/_skill_load_failure_window_readonly_facts_2026_09_30.md` | `9f5b73620b8a` | 23,065 | 2026-09-30 16:16:36 |
| `results/_v4_closeout_bucket_register_2026_10_01.md` | `99355c24a03b` | 41,943 | 2026-10-01 10:49:39 |

（开工前测 ＝ 完工后测，**逐字一致**；本棒对三件**只读**。）

---

## §9 交棒指向（**0 派工 · 供 parent 裁**）

1. **C1 可直接回填至 `4a3a2d0c5b95` §4.2／§6.3**：`plugin:` 前缀**无处理器**这一条**闭**，且它**独立解释**前序 `644e0666fbc4` 的 `plugin:skill` 8/8 全败。
2. **C3 是 G4 的唯一在册候选载体**（`allowedSkillNames`／`allowedExtensionSkillNames`）。若 PI 要闭 G4，需**能记录 skill 读事件**的运行时（当前**不记**，见 `9f5b73620b8a` §2.2）——**属运行时面**，⛔ **本棒 0 触碰**。
3. **C2 的复活条件可监控**：一旦 `<dataDir>\agents\<name>\skills` 或安装目录 `assets\{skills,agents}` 出现，§3.1(c) 静默降级即成为**不可观测**的一等差异源。
4. **G2（三面同名 winner 仲裁）仍未闭**，落点＝ `createSkillRegistry` internals 的 `snapshot.winners` 选定规则——**超本棒范围**，需另派。
