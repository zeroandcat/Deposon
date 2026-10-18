# G4 · E3「打点定义与实现不一致」裁量料件（2026-10-09 · 供 PI 裁定 · ⛔ 0 代裁）

> **棒别**：worker（E3 定义裁量料棒；PI 2026-10-09 问卷 Q3「先裁 E3 定义再定 R」项下之**备料**）。
> **授权锚**：PI 2026-10-09 问卷（`ask_cfb9284519a5abf29d0f03eb`）Q3 选「先裁 E3 定义再定 R」——G4 受控复现的 R（运行时改造）暂缓，先由 PI 裁定「E3 打点定义与实现不一致」问题。
> **主输入**：`results/_g4_reproduction_execution_register_2026_10_09.md`（SHA-12 `4daaf68cbf0e`／20,414 B）§2.3 M‑2／§5.2／§5.3‑2／§8‑3。
> **旁证输入**：① `results/_g4_controlled_reproduction_design_2026_10_09.md`（`b1c7c24926bb`）§2／§4.1／§5.2；② `results/_g4_runtime_state_trace_2026_10_01.md`（`e0ae0ad66acb`）§6.1；③ `results/_g4_skill_read_scope_trace_2026_10_01.md`（`9196a608bb0d`）§2.3／§2.4／§7 C5‑e；④ `results/_g4_residual_probe_2026_10_08.md`（`3554aa156e08`）§4。**以上四件均只读引用，⛔ 0 回改。**
> **件性质**：**裁量料件**——只做「现状＋沿革＋选项＋后果＋验证路径」的备料。⛔ **0 代 PI 拍板**、⛔ 0 推荐、⛔ 0 排期、⛔ 0 实施、⛔ 0 触发。
> **版式**：UTF-8 无 BOM · LF · `_主题_日期`（沿 PI 09‑29 命名裁 `57024f2cd30a` ＋ 10‑01 补记「派工建议名亦须合规」；⛔ 无版本前缀、⛔ 无 `_v5_` 类阶段字样）。
> **写入面**：**仅本件 1 件**（仓内）。运行时安装产物**只读**核验，⛔ 0 改造、⛔ 0 试写。
> **R4／K‑CF 纪律（沿登记件 §1.1）**：本件⛔ 0 含任何 key／token／secret 值、⛔ 0 含端点 host／port 值、⛔ 0 含任何 sessionId 值、⛔ 0 含 skill 实体名与会话正文；⛔ 0 打开 `config.yaml`／`mcp.json`／`local-runtime.auth.json`／`minimax-agent-cn-config.json`／`runtime-state.sqlite`；⛔ 0 调用任何 skill；⛔ 0 网络。

---

## §0 一页速览（供 PI 先看结论面）

| 项 | 结论 |
|---|---|
| **争议本体** | E3 原定义要求在 `LocalSkillTool.execute` 出口取**三态**（`undefined`／抛 `ambiguousSkillNameError`／命中 `content`）；本版 `execute` 出口**只呈现二分支返回**（`found:false`／`found:true`） |
| **本棒实测补充（非约束性）** | ① `execute` **无 try/catch** ⇒ 内层 ambiguous 抛出路径**在本版并未消失**，只是**不呈现为返回值分支**；② 三态的**真实出处是内层** `readRegistrySkillByName`，其本版逐字与 10‑01 前件**完全一致**（三态仍成立）⇒ **漂移的是「打点位选择」，不是「三态语义本身」**；③ 内层 `readSkillByName` 已存在 metrics 计数 `skill_load_total{status: ok／not_found／error}`，**与三态天然对应**；④ 内层 `readNativeSkill` 在 registry 未命中后**还有 desktop 兜底路径** ⇒ 内层 `undefined` ⇏ 工具侧 not found（存在第四种语义）；⑤ 本机 7 个 agent 根域 `skills/` **全部不存在** ⇒ ambiguous 集**恒空** ⇒ 本机**不可造** ambiguous 态 |
| **选项数** | **4 个（A／B／C／D）**，D 为留白候 PI 补 |
| **⛔ 本件立场** | **0 代裁**：不主张 A／B／C 哪项正确、0 排序、0 推荐；§7 为**候裁勾选页**，裁与不裁、选与不选全属 PI |
| **写入面** | 仅本件 1 件；既有件 0 回改（§9 三锚复算） |

---

## §1 E3 原设计定义（原文与语义 · 含三态假设出处）

### §1.1 定义原文（逐字照录，不擅改）

| 出处 | 原文 |
|---|---|
| **源头** `_g4_runtime_state_trace_2026_10_01.md:245`（§6.1 所差证据清单第 3 项） | 「**E3**｜两次调用的**返回形态**：`undefined` ／ 抛 `ambiguousSkillNameError` ／ 命中 `content`｜三者在用户侧分别呈现为「not found」／「ambiguous 报错」／成功，与 G4 现象形态直接对应｜`LocalSkillTool.execute` 出口（`52757967`）＋ `readSkillByName` 返回处（`100194348`）｜**须记 `error.code`（409／`AMBIGUOUS_SKILL_NAME`，`100142516`）**」 |
| **设计件照录** `_g4_controlled_reproduction_design_2026_10_09.md:67`（§2 E3 行） | 同上三态＋「**仅路径 R**（路径 P 为清单面，⛔ 不预期含返回形态）」 |
| **设计件验收判据** `_g4_controlled_reproduction_design_2026_10_09.md:113`（§4.1 E3 判据） | 「① 返回形态字段在场且取值属**三态枚举之一**；② 若为 ambiguous 分支，则 `error.code` 在场且等于在册码值；③ **0** 仅以「无 error 键」反推 `undefined`」 |

### §1.2 三态假设的**真实出处**（本棒追溯所得 · 关键）

E3 三态枚举**不是**在 `LocalSkillTool.execute` 处观察到后写下的，而是照录自**内层** `readRegistrySkillByName` 的逐字源码：

`results/_g4_skill_read_scope_trace_2026_10_01.md:68-90`（§2.3「★ 终判定式」，09‑29 版偏移 `100153797`）：

```js
export function readRegistrySkillByName(registry, name, options = {}) {
    const ambiguous = ambiguousLegacySkillNames(registry, options);
    const entry = filterInjectableRegistrySkills(/* … allowedSkillNames … */).find((candidate) => candidate.name === name);
    if (!entry || options.disabledLocationUris?.has(entry.locationUri))
        return undefined;                                  // ← 态①
    if (ambiguous.has(name)) {
        throw ambiguousSkillNameError(/* … */);           // ← 态②
    }
    return { content: entry.content, locationUri: entry.locationUri, sourceKind: entry.rootKind };  // ← 态③
}
```

⇒ **语义定位**：三态是**内层读函数的判定结果**，其用户侧映射（not found／ambiguous 报错／成功）经由工具层透出。设计件把 `execute` 出口与 `readSkillByName` 返回处**并列为两个打点位**，但**枚举本身属内层**。

⚠️ **口径澄清（供裁，非结论）**：登记件 §2.3 M‑2 表述为「未见 `ambiguousSkillNameError` 由 `execute` 抛出的路径」——本棒实测**未推翻**该表述（`execute` 内确无抛点）；但见 §2.2‑②：**内层抛出可穿透 `execute` 逸出**，「无抛点」≠「无该态」。

### §1.3 沿革链（E3 定义的四次演进）

| # | 时点 | 件 | 对 E3 的动作 |
|---|---|---|---|
| ① | 09‑30 | `9f5b73620b8a` §3 | G4 现象提出：「同写法同实体同日两会话结果相反」——**E3 尚未成形** |
| ② | 10‑01 14:31 | `9196a608bb0d` §2.3／C5‑e | 追进 `readRegistrySkillByName`，**逐字录得三态判定体**；同件 C5‑e 判定「歧义是**抛错**、不是 not found，与 G4 的现象形态不同」 |
| ③ | 10‑01 16:31 | `e0ae0ad66acb` §6.1 | 将三态**上升为取证面 E3**，指定打点位 `execute` 出口＋`readSkillByName` 返回处，指定记 `error.code`（409／`AMBIGUOUS_SKILL_NAME`） |
| ④ | 10‑08 | `3554aa156e08` §4 | 实测两载体（sqlite 消息面／outbox）：E3 判定「**无**」（窗口内 `error` 键 0 行、`ambiguousSkillName` 族 0 行）⇒ 强化「**不落盘**」 |
| ⑤ | 10‑09 09:47 | `b1c7c24926bb` §2／§4.1 | 列为 G4 四目标面之一，判据定为三态枚举＋`error.code`；判定「仅路径 R」 |
| ⑥ | 10‑09 10:21 | `4daaf68cbf0e` §2.3 M‑2／§5.3‑2 | **发现定义与实现不一致**（`execute` 出口二分支）⇒ 列为「R 实施前的**必裁项**」⇒ **本件**（Q3 授权）备料 |

---

## §2 实测现状（本棒 2026-10-09 只读复核 · 版本漂移实证）

### §2.1 面基线（版本漂移）

| 项 | 在册旧值（09‑29 版） | **本棒实测（2026-10-09）** | 判定 |
|---|---|---|---|
| `app.asar` 路径 | 在册安装产物 | `C:\Users\Administrator\AppData\Local\Programs\MiniMax Code\resources\app.asar` | 可得 |
| 字节 | **426,404,876 B** | **395,844,226 B** | ⚠️ 不等（**−30,560,650 B**） |
| mtime | 2026‑09‑29 22:25:34 | **2026-10-04 20:46:02** | ⚠️ 已变更 |
| SHA‑256 | 未在册 | `ce221e8d84c045c6cffd751ba834dcbd4b9a4805867d9748d639fcae4f36338d` | **与登记件 §2.1 逐字一致** ⇒ 版本未再漂移 |
| 旧偏移 `100153797`／`100190947`／`52757967`／`100194348` | 在册 | ⛔ **0 复用**（K‑CF‑5 部分触发） | 全部失效 |

### §2.2 现状实测（逐点 · 本棒只读字节读取）

**②‑1 `LocalSkillTool.execute` 出口＝二分支（与登记件 M‑2 一致，本棒复核）**

ESM 源副本（偏移 **54,125,479** 起）逐字要点：
- `const name = (typeof input.name === 'string' && input.name.trim()) || 'unknown-skill';`
- `const skill = await this.reader.readSkill(name, ctx.agentName, signal);`
- `if (!skill) { … details: { …, found: false, readable: false, … }; return {…}; }`
- 命中分支 `details: { …, found: true, readable: true, source, location }`
- ⚠️ 另存在**第二份编译副本**（tsc 产物 `local-skill.js`，`execute` 体于偏移 **52,643,478** 起，形态逐字同构）⇒ **同版双副本事实**（对 R 落点数量有影响，见 §5）。

**②‑2 本棒新增实测（本棒只读复核所得 · 非约束性）**：`execute` 内**只有两次 `signal?.aborted` 判定，⛔ 无 try/catch** ⇒ 内层 `ambiguousSkillNameError`（若触发）**以未捕获异常形式穿透 `execute` 逸出**，而**非**呈现为返回值分支。
⇒ 含义：**「`execute` 出口只有二分支」与「ambiguous 态在本版仍可能发生」两件事同时成立**；二者不矛盾，但**记法**必须区分「返回值分支」与「逸出异常」。

**②‑3 三态在内层仍成立（本版逐字复核）**：`readRegistrySkillByName`（偏移 **100,209,391**）与 10‑01 前件 §2.3 **逐字一致**——`return undefined`／`if (ambiguous.has(name)) throw ambiguousSkillNameError(...)`／`return { content, locationUri, sourceKind }` 三态齐在。
错误类定义同版复核（偏移 **100,198,156**）：`ambiguousSkillNameError(name, locations, telemetryHost)` → `new LocalSkillResolutionError(409, \`Skill name "${name}" is ambiguous; use location_uri\`, 'AMBIGUOUS_SKILL_NAME', { name, locations })` ⇒ **在册码值（409／`AMBIGUOUS_SKILL_NAME`）本版未变**。

**②‑4 完整调用链（本棒只读定位 · 供 R 落点计数）**

| 环节 | 符号 | 本版偏移 |
|---|---|---|
| 工具出口 | `LocalSkillTool.execute`（ESM 副本） | **54,125,479** |
| 工具出口（编译副本） | 同上（tsc 产物） | **52,643,478** |
| reader 适配 | `readSkill: (name, agentName) => requireSkillRuntime(…).readNativeSkill({ name, policy, gates, scope:{ agentName, excludeAgentResources?, expectedAgentInstanceId?, skipAgentResolution?, workspaceDir, allowedSkillNames, allowedExtensionSkillNames }, desktopSkills })` | 两处调用点 **57,900,106**／**62,604,965** |
| 原生读 | `readNativeSkill(reads, input)` | **100,244,810** |
| 会话读包装 | `createRuntimeSkillReads` 内 `async readSkillByName(name, scope = {})` | **100,248,150** 附近 |
| 作用域归一 | `resolveReadScope`（E2 打点位） | **100,246,584** 附近 |
| 底层判定 | `readRegistrySkillByName`（**三态出处**） | **100,209,391** |
| 错误码 | `ambiguousSkillNameError` 定义 | **100,198,156** |
| E1 闸门 | `toNormalizedSkillSelectorSet` | **100,200,309** |

**②‑5 内层已有 metrics 三态对应（本棒新发现 · 非约束性）**：`createRuntimeSkillReads` 内 `readSkillByName` 逐字含
`deps.metricsClient?.counter('skill_load_total', 1, { status: result ? 'ok' : 'not_found' })`，catch 段 `{ status: 'error' }` 后再抛。
⇒ 与 E3 三态**天然对应**（`ok`≙命中／`not_found`≙`undefined`／`error`≙ambiguous 抛出路径之一）。
⚠️ 该面**是否可读、是否含 `error.code`** 本棒**未验**（⛔ 0 读任何 metrics 落地面），仅登记「源码面存在此计数」。

**②‑6 内层存在 desktop 兜底第四语义（本棒新发现 · 非约束性）**：`readNativeSkill` 在 `reads.readSkillByName` 返回假值后，**继续**走 `input.desktopSkills?.find(candidate => normalizedSkillName(candidate.name) === normalizedSkillName(name) && isDesktopExtensionSkillSelected(allowedSkillNames, allowedExtensionSkillNames, candidate.pluginName, candidate.name))`，命中则返回该 skill，未命中才返 `undefined`。
⇒ 含义：**内层 `undefined`（E3 态①）⏏ 工具侧 `found:false`**；二者之间隔着一层兜底判定（该兜底本身以 E1 的 `allowed*` 集为门）。

**②‑7 本机 ambiguous 态**可达性**（本棒只读核实）**：`agents/` 下 7 个根域目录（`.builtin`／`agent-0032834a3e04`／`agent-11335500b168`／`agent-3a4d09ba3c90`／`agent-3e0c193da529`／`mavis`／`verifier`）**其 `skills/` 子目录 7/7 全部不存在**；`skills/` 主目录存在（223 目录）。
⇒ 沿 C5‑e 机制（`ambiguousLegacySkillNames` 只统计 `rootKind === 'agent'` 且 `rootScope` 跨域同名）⇒ **本机歧义集恒空** ⇒ **本机无法通过受控触发造出 ambiguous 态**。
⚠️ 这是**条件性**结论：仅对本机当前盘上态成立；若 `agents/<name>/skills` 出现即复活（沿 `b1c7c24926bb` §6.3 复活条件）。

**②‑8 版本漂移实证小结**：四旧偏移失效**已二次确认**（字节数、mtime 双变；SHA‑256 本棒与登记件逐字一致 ⇒ 10‑09 当日**未再漂移**）。

---

## §3 差异矩阵（设计 vs 实现 · 逐点）

| # | 维度 | **设计（E3 原定义）** | **本版实现（实测）** | 差异性质 |
|---|---|---|---|---|
| **Δ1** | 打点位归属 | 主位 `LocalSkillTool.execute` 出口；副位 `readSkillByName` 返回处 | 三态实际只存在于**更内层** `readRegistrySkillByName`；`readSkillByName` 为**包装层**（透传＋metrics） | **落点错位**（主位不产出三态） |
| **Δ2** | 出口返回形态 | 三态枚举（`undefined`／抛错／`content`） | **`execute` 出口＝二分支返回**（`found:false`／`found:true`），均为**正常的 `ToolResult`** | **形态不符**（登记件 M‑2） |
| **Δ3** | ambiguous 的呈现方式 | 作为**三态之一**与另两态并列枚举 | `execute` ⛔ 无 try/catch ⇒ ambiguous（若触发）以**逸出异常**呈现，**不是返回值分支** | **呈现层错位**（本棒新发现） |
| **Δ4** | 态①（`undefined`）的可取性 | 直接在 `execute` 出口可见 | `execute` **从不返回 `undefined`**；态①在内层被 `if (!skill)` 折叠为 `found:false` | **需重述** |
| **Δ5** | 态②（ambiguous）的可造性 | 列为须取证的三态之一 | 本版**态②机制仍在**（错误类与抛出点逐字未变），但**本机歧义集恒空** ⇒ 7/7 agent 根域无 `skills/` ⇒ **受控触发造不出** | **可观测性受限**（本棒新发现） |
| **Δ6** | 内层 `undefined` 的语义 | 态① ≡ 「not found」 | 内层 `undefined` 之后**尚有 desktop 兜底判定** ⇒ 内层假值 ⇏ 工具侧 not found | **语义不等价**（本棒新发现） |
| **Δ7** | `error.code` 的取法 | 「若为 ambiguous 分支，则 `error.code` 在场且等于在册码值（409／`AMBIGUOUS_SKILL_NAME`）」 | 错误类逐字仍带 `409`／`AMBIGUOUS_SKILL_NAME`；但该值**只在逸出异常对象上**，不在任何返回值分支内 | **可取面随 Δ3 一同移位** |
| **Δ8** | 判据③「0 由「无 error 键」反推 `undefined`」 | 设计件 §4.1 明列 | 二分支形态下 `details.found:false` **不含** `error` 键 ⇒ 若照记法极易触犯该判据 | **与判据直接冲突** |
| **Δ9** | 打点位数量（同版副本） | 设计件按**单点**记（1 个 offset） | `execute` 在本版有 **2 份副本**（ESM 54,125,479／tsc 52,643,478），逐字同构 | **落点计数差**（本棒新发现） |
| **Δ10** | 现成观测面 | 未登记 | 内层已有 `skill_load_total{status: ok／not_found／error}`，与三态**天然对应** | **既有面被漏记**（本棒新发现） |

---

## §4 选项（**4 个 · 0 排序 · 0 推荐 · ⛔ 0 代裁**）

> 以下四选项互斥性未验（可组合），**取舍全属 PI 口径面**。本件仅陈述各选项「改什么／代价／后果／自证法」。

### 选项 A · 修订 E3 定义，以本版二分支实现为准

**改什么**：E3 的取值面**重述**为「`execute` 出口二分支：`details.found:false` ／ `details.found:true`」；`error.code` 条款**移出 E3 主判据**（或降为附注）。打点位**留在** `execute`（0 移层）。

**A‑1 变体**：保留三态语义但**改以「返回值分支 ＋ 逸出异常」双轨表述**（打点位仍在 `execute`：包一层 try/catch 记异常支路，命中／未命中仍记 `found` 二值）。
**A‑2 变体**：打点位留在 `execute` 出口，但**打点自产第三态标记位**（如 `found:false` 且附带「内层返回假值」标志）⇒ 与设计件 §5.2「自造标志位」原则相抵（M‑1 曾以「无需自造标志位」为 E1 利好，E3 则相反）。

### 选项 B · 维持三态定义，打点位改落内层 ambiguous 判定分支

**改什么**：E3 枚举与 `error.code` 条款**原文保留**；打点位由 `execute` 出口**下移**至 `readRegistrySkillByName`（态① `return undefined` 前／态② `throw` 前／态③ `return` 前三处，或以单点包裹记录三值）。

**B‑1 变体**：打点落 `createRuntimeSkillReads` 内 `readSkillByName`（既有 metrics 位邻处），三态以 `result` 真值／异常捕获二分记录。

### 选项 C · E3 降级或移出 G4 范围

**改什么**：E3 由「G4 四目标面之一」降为「**旁注／不参与闭合判据**」或整体移出 G4；G4 判据改由 E1／E2／E4 三面承担（或改记「E3 缺证 ⇒ 走 K‑CF‑1『不明』分支」）。

### 选项 D · 其他（留白 · 候 PI 自拟）

**说明**：留空，候 PI 补写新口径（如「合并打点」「先补口径固化流程再定」「暂缓 R 并将 E3 整项挂账」等）。本件⛔ 0 预填 D 之内容。

---

## §5 每选项后果（三维度：R 改造面／E1·E2·E4 影响／G4 结论效力）

| 维度 | **A**（二分支为准） | **B**（保三态·移内层） | **C**（降级/移出） | **D** |
|---|---|---|---|---|
| **打点位** | 仍在 `execute` 出口（ESM 54,125,479 ＋ tsc 52,643,478，**同版双副本** ⇒ 若两副本均被加载则**须同改两处**） | 下移至 `readRegistrySkillByName`（**100,209,391**）单点或三点；或落 `readSkillByName`（**100,248,150** 附近） | 无（不实施 E3 打点） | 候 PI |
| **成本** | **较低**：单层包裹；不触碰内层判定逻辑 ⇒ 对运行时行为扰动面小 | **较高**：须在**判定逻辑体内**插桩（`undefined` 分支前／`throw` 前／`return` 前）⇒ 触碰核心读路径，且**入参含 `allowed*`／`agentName` 上下文**（与 E1／E2 打点**同层**，三者可能并点以省一次改造） | **最低**（0 改 runtime）⇒ 但代价落在**判据效力**上 | 候 PI |
| **回退法** | 整文件备份覆盖（沿登记件 §5.2 口径）；**打点代码为自包含块 ⇒ 可按块摘除**，扰动面小于 B | 同左；但因改在判定体内，**回退需精确还原语句序列**（备份覆盖仍为最终保障） | 无需回退（0 改） | 候 PI |
| **对 E1 影响** | 无（E1 打点位 `readRegistrySkillByName` 入口不变） | ⚠️ **同层并点**：E1 与 E3 若同在 `readRegistrySkillByName`，一次改造可覆盖两面 ⇒ **E1 打点须与 E3 记法一并裁**，否则出现「E1 已改、E3 未定」的半成品状态 | E1 独立，不受影响 | 候 PI |
| **对 E2 影响** | 无（E2 打点位 `resolveReadScope` 独立） | 无（E2 仍在 `resolveReadScope`） | 无 | 候 PI |
| **对 E4 影响** | ✅ **同点位同层**：E4 在 `execute` 入口 `trim()` 之前（**54,125,479** 起）⇒ 与 E3-A **一次改造同点完成**，A 方案下 E3／E4 改造**可合并** | ⚠️ **分处两层**：E4 留 `execute`、E3 移内层 ⇒ 一次 R 需**两处**改造 | 无 | 候 PI |
| **对 G4 结论效力** | E3 变为「**用户侧实际可见形态**」（not found／成功）⇒ 与 G4 现象形态**直接对应**；⚠ 但**丢失「ambiguous 报错」这一用户侧形态的独立可辨性** | E3 三态齐 ⇒ 判据完整；⚠ 但本机**态②不可造**（Δ5）⇒ 实际可得常为**二态**，有触发 **K‑CF‑4（`n_distinct ≤ 3` ⇒ 该面判「不明」）** 与设计件 §5.2「码本坍缩」的风险 | E3 **不参与闭合** ⇒ G4 判据由四面降为三面 ⇒ 若 E1／E2／E4 满足，可判「以三面闭合」；⚠ 若 PI 选择走 **K‑CF‑1**，则 G4 判「**不明**」⇒ **G4 仍挂账**，但**挂账理由由「缺 E3 面」改为「PI 已裁 E3 不参与」** | 候 PI |
| **对判死线的影响** | K‑CF‑4（退化）风险降低（值域二值化）；K‑CF‑3（子串/键级）须照常 | K‑CF‑4 风险**上升**（三态枚举塌缩为二态） | K‑CF‑1 成为 E3 的正式出口 | 候 PI |

---

## §6 验证路径（每选项如何自证 · 均 0 改造即可做的**前置自证**与 R 后自证分列）

> ⚠️ **前提**：以下路径**不构成 0 代裁**；**R 是否实施仍属 PI 口径面**（PI Q3 已选「先裁 E3 定义再定 R」）⇒ 本节仅备「裁完之后各自怎么验」。

### §6.1 共用前置自证（⛔ 0 改造 · 本棒已完成大半）

| id | 内容 | 状态 |
|---|---|---|
| **V‑0** | 符号重定位（⛔ 不用旧偏移）＋ 判定「符号仍在／已改名／已不存在」 | ✅ 本棒完成（§2.2‑4，10 符号逐一定位） |
| **V‑1** | 版本漂移复核（字节／mtime／SHA‑256） | ✅ 本棒完成（SHA‑256 与登记件逐字一致） |
| **V‑2** | `execute` 出口形态逐字判读（分支数／有无 try/catch） | ✅ 本棒完成（§2.2‑①②） |
| **V‑3** | 内层三态逐字判读＋错误码复核 | ✅ 本棒完成（§2.2‑③） |
| **V‑4** | 同版双副本核查（ESM／tsc） | ✅ 本棒完成（§2.2‑②‑1） |
| **V‑5** | ambiguous 可造性预检（agent 根域 `skills/` 存在性） | ✅ 本棒完成（§2.2‑⑦，7/7 不存在） |
| **V‑6** | ⛔ **未验项（如实登记）**：① `app.asar` 内嵌 chunk 是否**可安全改**／有无 ASAR 完整性校验或签名；② 打点件落面具体路径；③ `skill_load_total` metrics 是否可读、是否含 `error.code`；④ 同一偏移在**升级后**的存续 | ⛔ **本棒 0 试写、0 读 metrics 面、0 打开 sqlite** ⇒ 四项均**未验** |

### §6.2 逐选项自证

| 选项 | **裁后、R 前**可做（0 改造） | **R 后**自证要点 |
|---|---|---|
| **A** | ① 以 §2.2‑① 逐字为准，产出「E3‑A 二分支定义稿」交 PI 复核（**本件 0 起草正式定义**）；② 核对 `details` 字段清单与判据③的冲突（Δ8）已在定义稿中处置 | ① 键级命中：每次 skill 读调用各一条、含 `found` 布尔；② 值域＝2 ⇒ 过 K‑CF‑4；③ **0** 以「无 `error` 键」反推态①（判据③）；④ 若 A‑1：逸出异常轨须**单独计数**，不得混入 `found` 分布 |
| **B** | ① 核对内层三态与在册码值仍一致（V‑3 ✅）；② **明示态②在本机不可造**（V‑5 ✅）⇒ 请 PI 裁定：是否接受「三态定义 ＋ 实测仅二态」并预备 K‑CF‑4 处置口径；③ 与 E1 打点**同层并点**的改造合并方案（成本面） | ① 内层三点各留痕（或单点三分支记法）；② **样本须含同会话对／同实体／同日**（设计件 §4.1 样本判据）；③ 态②若始终 0 命中 ⇒ 该面判「**不明**」（K‑CF‑4／K‑CF‑2），⛔ 禁以该面下「支持／否证」结论 |
| **C** | ① 产出「E3 退出 G4 判据」的影响面清单（G4 判据由四面降三面之连锁）；② 明确挂账新口径（若走 K‑CF‑1 ⇒ G4 判「不明」） | 0（不实施 E3 打点）；仅需验证「E1／E2／E4 三面齐备」即可判三面闭合 |
| **D** | 候 PI 补口径后另行备料 | 候 PI |

---

## §7 候裁页（供 PI 勾选 · **⛔ 本件 0 代裁 · 0 推荐 · 0 排序**）

### §7.1 主裁项（单选或多选 · 由 PI 勾）

| ☐ | 选项 | 一句话内容 | 主要代价落点 |
|---|---|---|---|
| ☐ | **A** | 修订 E3 定义以本版 `execute` 二分支为准（打点不移层） | 丢失 ambiguous 态的独立可辨性 |
| ☐ | **B** | 维持三态定义，打点位改落内层 ambiguous 判定分支 | 改在判定体内；本机态②不可造 ⇒ K‑CF‑4 风险 |
| ☐ | **C** | E3 降级／移出 G4 范围 | G4 判据降为三面；或走 K‑CF‑1 判「不明」 |
| ☐ | **D** | 其他（PI 自拟） | — |

### §7.2 附属勾选项（随主裁项生效 · 可留空）

| ☐ | 附属项 | 说明 |
|---|---|---|
| ☐ | **A‑1** | A 的双轨表述变体（返回值分支 ＋ 逸出异常各记一轨） |
| ☐ | **A‑2** | A 的自产第三态标记位变体（与设计件 §5.2 原则相抵，请一并裁） |
| ☐ | **B‑1** | B 落 `readSkillByName`（metrics 位邻处）而非 `readRegistrySkillByName` |
| ☐ | **E1 同层并点** | 若选 B：是否将 E1 打点与 E3 合并为**同层一次改造**（省一次 R，但 E1 记法随之冻结） |
| ☐ | **双副本同改** | 若选 A：是否要求 ESM ＋ tsc **两份副本同改**（防只改其一而运行期未生效） |
| ☐ | **K‑CF‑4 预授权** | 若选 B：是否预先授权「三态定义但实测二态 ⇒ 该面判『不明』」的处置口径 |

### §7.3 勾选后 PI 需另行定的事（本件⛔ 0 预裁）

1. **R 是否实施**（PI Q3 已定「先裁 E3 定义再定 R」⇒ 仍在待定）。
2. **asar 备份与回退授权**（V‑6‑① 可写性／完整性校验未验）。
3. **打点件落面路径**（V‑6‑②）。
4. **E3 定义修订件的起草与复核归属**（本棒⛔ 0 起草正式定义稿）。

---

## §8 诚实边界（本件自限 · 逐条）

1. ⛔ **0 代裁**：本件不主张 A／B／C 哪项正确、0 排序、0 推荐、0 排期；§7 为候裁勾选页，**裁与不裁、选与不选全属 PI**。
2. ⛔ **0 触发 · 0 改造 · 0 试写**：本棒⛔ 0 调用任何 skill、⛔ 0 写 `app.asar`／安装目录／`<dataDir>`、⛔ 0 打开 `runtime-state.sqlite`、⛔ 0 读 metrics 落地面。
3. **静态判读 ≠ 运行时实测**：§2 全部结论来自**源码字节静态判读**（只读 `app.asar`）⇒ **0 主张**「本版运行时实际走到哪一分支」；尤其 §2.2‑⑦ 的「歧义集恒空」为**盘上态推论**，非运行观测。
4. **§2.2‑⑤（metrics 三态对应）／②‑⑥（desktop 兜底第四语义）／②‑1（双副本）／Δ9** 为**本棒新增发现**，前件未载 ⇒ 属**待 PI 与原棒交叉复核**的新事实，⛔ 0 主张前件有误（前件 M‑2 关于「`execute` 无抛点」的表述经复核**成立**）。
5. **偏移纪律**：⛔ 0 复用四旧偏移；§2.2 偏移均为本棒按符号名重定位所得，**仅对本版 SHA‑256 `ce221e8d…f36338d` 有效**。
6. **外推边界**：即便日后受控复现命中任一分支，⛔ 0 据此宣称已解释 2026‑09‑30 的那次自然发生（沿 `b1c7c24926bb` §5.3 外推边界＝构造域）。
7. ⛔ **0 冒认**：运行时／源码归属 **MiniMax Code 运行时原作者**；本件 0 冒认为出证方。
8. **本件自身 SHA‑12／字节不可内嵌**（自引用悖论）——落盘后复算，随回执回报。

---

## §9 0 回改自证（三锚件 · 写盘前基线 ／ 写盘后复算）

| 锚件 | 写盘前 SHA-12 ／ 字节 ／ mtime | 写盘后 | 判定 |
|---|---|---|---|
| `results/_g4_reproduction_execution_register_2026_10_09.md` | `4daaf68cbf0e` ／ 20,414 ／ 2026-10-09 10:21:25 | 见回执 | 待填 |
| `results/_g4_controlled_reproduction_design_2026_10_09.md` | `b1c7c24926bb` ／ 23,675 ／ 2026-10-09 09:47:11 | 见回执 | 待填 |
| `results/_g4_runtime_state_trace_2026_10_01.md` | `e0ae0ad66acb` ／ 25,631 ／ 2026-10-01 16:31:10 | 见回执 | 待填 |
| `results/_g4_skill_read_scope_trace_2026_10_01.md` | `9196a608bb0d` ／ 26,906 ／ 2026-10-01 14:31:34 | 见回执 | 待填 |
| `results/_g4_residual_probe_2026_10_08.md` | `3554aa156e08` ／ 23,025 ／ 2026-10-08 16:19:49 | 见回执 | 待填 |

| 运行时面 | 本棒操作 | 判定 |
|---|---|---|
| `app.asar` | 仅只读字节读取（`FileStream` 只读打开）＋ `Get-FileHash`／`Get-Item` | ✅ **0 写入**（SHA‑256／字节／mtime 与登记件逐字一致） |
| 安装目录其余文件／`<dataDir>` | 仅 `Test-Path`／`Get-ChildItem -Directory` 只读枚举 | ✅ 0 写入 |
| `runtime-state.sqlite`／`config.yaml`／`mcp.json`／`local-runtime.auth.json` | ⛔ **0 打开** | ✅ 0 触 |

**本棒写入面**：**仅本件 1 件**（`results/_g4_e3_definition_ruling_material_2026_10_09.md`）；⛔ 0 落盘 scratch 脚本（全为 `-Command` 内联调用）；⛔ 0 移动／重命名／删除任何文件；⛔ 0 外网；⛔ 0 skill 调用。

---

## §10 撞名实测

- 落名前 `Test-Path`（拟落名 `results/_g4_e3_definition_ruling_material_2026_10_09.md`）＝ **`False`**。
- `results/_g4_*` 现存：`skill_read_scope_trace_2026_10_01`／`runtime_state_trace_2026_10_01`／`residual_probe_2026_10_08`／`controlled_reproduction_design_2026_10_09`／`reproduction_execution_register_2026_10_09`——**0 与本件同名**。
- ⇒ **新建，0 覆写**。

---

## §11 交棒指向（**0 派工 · 0 排期 · 候 PI 裁**）

1. **争议的精确形状**（供 PI 一句话把握）：**漂移的是「打点位选择」，不是「三态语义本身」**——三态在内层 `readRegistrySkillByName` 本版**逐字未变**；`execute` 出口本就**不是**三态的产生处（沿革见 §1.2／§1.3）。
2. **一条易被忽略的实测**：内层已有 `skill_load_total{status: ok／not_found／error}` 与三态**天然对应**；且本机**歧义集恒空**（7/7 agent 根域无 `skills/`）⇒ **B 方案下态②不可造**、A 方案下则**无态可失**。二者对 G4 效力影响不同（§5 末行）。
3. **一条与判据直接冲突的实测**：二分支形态下 `details.found:false` **不含 `error` 键** ⇒ 若不先裁定义便照原判据③取证，将**必然触犯**「0 由结构推断取值」纪律。
4. **0 派工**：R 是否实施、E3 定义修订归属、asar 备份与回退授权、打点件落面，**均属 PI 口径面**，本棒 0 代裁、0 排期。