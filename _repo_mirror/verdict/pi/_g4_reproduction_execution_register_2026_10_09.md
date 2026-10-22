# G4 受控复现 · 执行登记件（2026-10-09 · M／P 已执行 · R 未实施〔硬闸拦停〕）

> **棒别**：worker（G4 受控复现执行棒；PI 卷⑧ Q1 丙「M＋P＋R 全授权〔含 runtime 改造〕」之执行）。
> **session**：`mvs_ab1ceef5f0c149f6bd362bd7ca73b460`（署名如实，0 冒认他方）。
> **设计件**：`results/_g4_controlled_reproduction_design_2026_10_09.md`（SHA-12 `b1c7c24926bb`／23,675 B／mtime 2026-10-09 09:47:11）§2／§3／§4——⛔ 本棒**只读引用**，未回改。
> **探件**：`results/_g4_residual_probe_2026_10_08.md`（`3554aa156e08`）——⛔ 本棒**只读引用**，未回改。
> **版式**：UTF-8 无 BOM · LF · `_主题_日期`（⛔ 无版本前缀、⛔ 无 `_v5_` 类阶段字样）。
> **写入面**：**仅本件 1 件**（仓内）；运行时安装产物**0 写入**（R 未实施，见 §5）。

---

## §0 执行摘要（先结论）

| 阶段 | 计划 | 实际结果 | 硬闸判定 |
|---|---|---|---|
| **M · 源码面静态校准** | 按符号名重定位四打点位，产出「符号仍在／已改名／已不存在」三态表 | ✅ **完成**：四打点符号**全部仍在**（10 符号键级命中均 >0，四目标打点位均定位到**定义体**而非仅引用），并取得**新偏移** | 硬闸① **不触发** ⇒ R 原为可行 |
| **P · 本地端点取证** | 对 `GET /minimax-desktop/api/v1/runtime/skills` 当场读响应体、落结构登记 | ❌ **失败**：端点**进程外不可达**（非 TCP 监听；回环 13 端口实测 0 命中该路由）；**响应体 0 读到** | 硬闸② **触发** |
| **R · 运行时打点** | 四打点位各增一条打点、写入独立件 | ⛔ **未实施**（按派工硬闸②「M 或 P 阶段失败 ⇒ 停手报告、0 硬闯 R」） | **停手** |

**一句话**：**M 成功且给出比设计件乐观的结论（四符号全在、可改）**，但 **P 阶段失败**——失败原因**不是**设计件预期的「端点返回静态清单不含 allowlist」，而是**更前置的一层：端点根本不对进程外开放**（传输面为 renderer↔main 的进程内 IPC）⇒ 按硬闸②，**R 本棒 0 实施**，G4 受控复现**停在此处待 PI 裁**。

⚠️ **0 判档**：本件**不宣布** G4 闭、**不宣布** G4 永不可闭、**0 主张** §1.2 的 A／B／C 哪分支命中、**0 判** C‑G4 生死。

---

## §1 只读面清单与 R4 声明

| 面 | 路径／对象 | 本棒读法 | 状态 |
|---|---|---|---|
| 运行时安装产物 | `〔本地绝对路径·脱敏略:MiniMax〕 Code\resources\app.asar` | `mmap` **只读**字节扫描 ＋ `Get-FileHash` ＋ `Get-Item` | **只读，0 写入** |
| 监听／进程面 | `Get-NetTCPConnection`／`Get-Process`／`Get-CimInstance` | 只读枚举 | 只读 |
| 回环端点 | `http://127.0.0.1:<各监听端口>/minimax-desktop/api/v1/runtime/skills` | **1 轮** `Invoke-WebRequest`（仅 127.0.0.1／::1） | 只读（GET，无状态变更） |
| 设计件／探件 | `results/_g4_controlled_reproduction_design_2026_10_09.md` 等 | 读 ＋ `Get-FileHash` | 只读，0 写 |

### §1.1 R4 遵守声明

- 本件**只登记**：符号名、命中数、**字节偏移**、结构名／字段名／字段路径名、路由与传输面判定、HTTP 状态码、计数、枚举分布、判据与判死线结论；⛔ **0 转述任何载荷值**（会话正文、工具入参取值、工具返回、skill 实体名、key／token 值均**不落件**）。
- 本棒⛔ **0 打开／读取** `config.yaml`／`mcp.json`／`local-runtime.auth.json`／`minimax-agent-cn-config.json`；⛔ **0 读取**任何 key／token／secret 值；⛔ **0 打开** `runtime-state.sqlite`；⛔ **0 调用**任何 skill。
- 命令行读取（`Win32_Process.CommandLine`）⛔ **0 落件原文**——本件仅登记**布尔判定**（是否含 `--port`／是否含 `runtime` 字样）与**字符长度**，**0 落原文**（防 K‑CF‑6）。
- 本件**不含**任何 sessionId 值；会话一律以「本棒 session」指称。
- **网络面**：⛔ **0 外网**。P 阶段 13 次请求**全部指向 `127.0.0.1`／`::1`**（本地回环），性质如实登记见 §3.4。

---

## §2 M 阶段 · 源码面静态校准（按符号名 · 0 改造）

### §2.1 面基线（版本漂移已实证）

| 项 | 前件②／设计件在册值（2026‑09‑29 版） | **本棒实测（2026‑10‑09）** | 判定 |
|---|---|---|---|
| `app.asar` 路径 | 在册安装产物 | `〔本地绝对路径·脱敏略:MiniMax〕 Code\resources\app.asar` | 路径可得 |
| 字节 | **426,404,876 B** | **395,844,226 B** | ⚠️ **不等**（−30,560,650 B） |
| mtime | 2026‑09‑29 22:25:34 | **2026‑10‑04 20:46:02** | ⚠️ **已变更**（版本升级） |
| SHA‑256 | 未在册 | `ce221e8d84c045c6cffd751ba834dcbd4b9a4805867d9748d639fcae4f36338d` | 本棒新增登记 |

⇒ **前件② §6.1 四个旧偏移（`100153797`／`100190947`／`52757967`／`100194348`）确实已失效**（沿设计件 §6.2 判定），本棒⛔ **0 复用**旧偏移，全部**按符号名**重新定位。

### §2.2 四打点位重定位结果（新偏移 · 2026‑10‑09 版）

| 打点位（符号名） | 目标面 | 符号命中数 | **本棒新偏移** | 旧偏移（已失效） | 三态判定 | **是否为定义体** |
|---|---|---|---|---|---|---|
| `readRegistrySkillByName` | **E1** | 6 | **100,209,391** | `100153797` | ✅ **仍在** | ✅ 是（`export function readRegistrySkillByName(registry, name, options = {})`） |
| `toNormalizedSkillSelectorSet` | E1 归一化 | 8 | **100,200,309** | `100144715` | ✅ **仍在** | ✅ 是（`export function toNormalizedSkillSelectorSet(values)`） |
| `resolveReadScope` | **E2** | 36 | **100,246,584**（闭包内 `const resolveReadScope = async (...)`） | `100190947` | ✅ **仍在** | ✅ 是（`createRuntimeSkillReads` 内定义） |
| `LocalSkillTool` | **E3／E4** | 33 | **54,125,479**（`export class LocalSkillTool`）／`execute` 方法体紧随其后 | `52757967` | ✅ **仍在** | ✅ 是（`async execute(ctx, input, signal?)`） |
| `readSkillByName` | E3 | 51 | **100,175,644**（`readSkillByName: (name, scope) => runtime.readSkillByName(name, scope)`）／`100,248,150**（实现面） | `100194348` | ✅ **仍在** | ✅ 是 |

**关联字段字面命中**（E1／E2 取值面在源码中存在性）：

| 字面 | 命中数 | 判定 |
|---|---|---|
| `allowedSkillNames` | **102** | ✅ 存在于运行时（作**入参**传递，见 §2.3） |
| `allowedExtensionSkillNames` | **130** | ✅ 同上 |
| `compatibleAgentNames` | **93** | ✅ 同上 |
| `ambiguousSkillNameError` | 8 | ✅ 存在 |
| `AMBIGUOUS_SKILL_NAME` | 2 | ✅ 存在 |

⇒ **M 阶段判定：四打点符号「全部仍在」，无改名、无消失 ⇒ 硬闸① 不触发 ⇒ R 在技术上「可行」。**

### §2.3 M 阶段附带结构发现（对 E1–E4 打点设计的**偏差**，如实登记）

| # | 发现 | 对 E1–E4 的影响 |
|---|---|---|
| **M‑1** | `toNormalizedSkillSelectorSet(values)` 的实现为 `values === undefined ? undefined : new Set(...)` ⇒ **三态区分（`undefined`／空集／非空集）在源码层是天然可判的**，打点 E1 无需自造标志位 | ✅ **利好 E1**：机械可取 |
| **M‑2** | `LocalSkillTool.execute` 的返回形态为**二分支**：`if (!skill) → details.found:false`（文本 `Local skill not found: …`）／否则 `details.found:true`（含 `source`／`location`）。**未见** `ambiguousSkillNameError` 由 `execute` 抛出的路径 | ⚠️ **偏差**：E3 原定义三态（`undefined`／ambiguous／命中 `content`）在本版**未按原样出现在 `execute` 出口**；ambiguous 判定发生在**更内层**（`readRegistrySkillByName` 侧）。⇒ **R 打点须改落点或改记法**，否则 E3 会误判 |
| **M‑3** | `resolveHostedCatalogScope` 中 `allowedSkillNames === undefined ? {} : {...}` ⇒ `undefined` 与「空集」在**对象构造层已被区分**，可打点 | ✅ 利好 E1 |
| **M‑4** | `listRuntimeSkills` **入参**含 `allowedSkillNames`／`allowedExtensionSkillNames`（§3.2） | ✅ 说明 E1 面在运行时确有载体 |
| **M‑5** | `LocalSkillTool.execute` 对 `input.name` 仅 `trim()` 后使用（`(typeof input.name === 'string' && input.name.trim()) \|\| 'unknown-skill'`） | ✅ 与前件记载一致 ⇒ E4 逐字原文可取（须在 `trim()` **之前**取） |

---

## §3 P 阶段 · 本地端点取证（❌ 失败 · 端点进程外不可达）

> **性质如实登记**：本阶段 13 次 HTTP GET **全部指向 `127.0.0.1`／`::1` 本地回环地址**，⛔ **0 外网**、⛔ **0 LLM 调用**、⛔ **0 skill 调用**、GET 无状态变更。**本地回环**之「是否算联网」口径仍属 PI 面（本棒沿设计件 §8‑2 **0 代裁**），但本棒登记：**技术上未出本机**。

### §3.1 传输面判定（进程内 IPC · 非 TCP）

| 步骤 | 实测 | 判定 |
|---|---|---|
| 进程面 | `MiniMax Code.exe` 共 11–14 个进程（含渲染／工具进程） | — |
| 监听面 | `Get-NetTCPConnection -State Listen` 逐条回溯进程 ⇒ **MiniMax Code 名下 0 条 Listen** | ⛔ **无本地 HTTP 监听端口** |
| 出站面 | 该进程组仅 `Established` 至 `:443`（外连）与 `:1018`（本机出站） | 无入站服务 |
| 命令行 | 14 个进程命令行中 **0 个**含 `--port`（仅登记布尔，⛔ 0 落原文） | 无显式端口 |
| 源码面 | 路由字面在源码内 6 处；传输标记 `transport: 'metadataOnly'`；宿主类 `LocalRuntimeApiHost`（`api/host.js`）；测试代码中请求源为 **`http://local/minimax-desktop/api/v1/…`** | ⇒ **虚拟源 `http://local`，进程内 renderer↔main 通道**，⛔ 非 TCP |

### §3.2 端点结构（源码面 · 决定 P 能否承载 E1／E2）

| 项 | 实测（源码） |
|---|---|
| 路由 | `GET /minimax-desktop/api/v1/runtime/skills`；服务 `DesktopService`／方法 `ListRuntimeSkills` |
| **请求绑定**（4 个查询参数） | `agent_name`（optional）、`session_id`（optional）、`workspace_dir`（optional）、`include_plugin_skills`（optional）、`base_req` |
| ⛔ 请求侧 | **0** 暴露 `allowed_skill_names`／`compatible_agent_names` 等查询参数 |
| **响应结构** `ListRuntimeSkillsResp` | **仅 3 字段**：`skills`（`list<SkillInfo>`）、`refreshed_at`（scalar）、`base_resp`（scalar） |
| ⛔ 响应侧 | **0 含** allowlist 字段、**0 含** `compatibleAgentNames` |
| 服务端实现 | `listRuntimeSkills(input)` **内部**读取 `scopedInput.allowedSkillNames`／`allowedExtensionSkillNames`／`compatibleAgentNames` 并传给 `listRegistryRuntimeSkills` ⇒ **E1／E2 面在服务端存在，但⛔ 不出现在响应体中** |

### §3.3 实测调用（1 轮 · 13 个回环端口）

| 端点 | 结果 |
|---|---|
| `http://127.0.0.1:<13 个回环监听端口>/minimax-desktop/api/v1/runtime/skills` | **0 个 200**；返回 `404`／`400`／`503`／无 HTTP 响应；**0 命中该路由** |
| 结论 | ⇒ **端点进程外不可达** ⇒ **响应体 0 读到** ⇒ **P 阶段的「当场读响应体」这一前提不成立** |

### §3.4 P 阶段判定（与设计件预期的**偏差**，如实登记）

| 项 | 设计件 §3.1 预期 | **本棒实测** |
|---|---|---|
| P 的失败模式 | 「端点返回静态清单，不含 per-session allowlist ⇒ P 对 E1／E2 不成立」 | **更前置**：端点**根本不对进程外开放**（进程内 IPC）⇒ P **连响应体都取不到** |
| P 对 E1／E2 | 「候取；可能免 R」 | ❌ **不成立**（0 取证） |
| P 对 E3／E4 | 「⛔ 不预期覆盖」 | ❌ 同上（⛔ 0 取证） |
| 设计件 §3.2 的前提 | 「响应体**当场不读即永失**」（D5） | ⚠️ 本棒**未能读**（0 到达）⇒ 该「一次性窗口」风险**未被消费**、亦未被证实 |

⇒ **P 阶段 = 失败** ⇒ 触发派工**硬闸②**：「M 或 P 阶段失败 ⇒ **停手**报告、⛔ **0 硬闯 R**」。

---

## §4 判死线自证（沿设计件 §4.2 · K‑CF‑1…6）

| id | 判死线 | 本棒适用性判定 |
|---|---|---|
| **K‑CF‑1** | E1–E4 任一面在受控触发后**键级 0 命中**（＝不落盘） | **未触发**（R 未实施 ⇒ 0 受控触发 ⇒ 0 键级判定）。⚠️ **0 提前宣告**「不落盘」 |
| **K‑CF‑2** | 可比样本三条件任一不满足 ⇒ 样本作数 | **未触发**（0 样本构造） |
| **K‑CF‑3** | 目标字面**仅子串级命中、键级 0 命中** ⇒ 判回显污染、**0 采信** | ✅ **已适用并遵守**：M 阶段的命中全部**取自二进制安装产物的源码字节**（非日志、非棒方检索文本）⇒ **0 回显污染面**。本棒**未**以子串命中推断任何运行时行为；§3.2 的响应字段结论取自 **schema 结构体定义**（键级），⛔ 非仅子串 |
| **K‑CF‑4** | 任一目标字段 `n_distinct ≤ 3` ⇒ 该面判「不明」 | **未触发**（0 受控触发、0 取值样本） |
| **K‑CF‑5** | 复活条件触发（purge 再执行／schema 变更／偏移失效） | ✅ **本棒已实证「偏移失效」一项**：asar 字节与 mtime 均已变更（§2.1）⇒ 前件② 四旧偏移**确认失效**，本棒已按符号名重定位并登记新偏移 |
| **K‑CF‑6** | 取证件含 key／token／secret/端点值**明文** ⇒ 该件作废 | ✅ **未触发**：本件 0 含任何凭据、0 含端点 host／port 值、0 含 sessionId 值、0 含 skill 实体名 |

**§4 判定汇总**：无判死线被触发；**K‑CF‑5 已实证部分触发**（版本漂移致偏移失效，已处置）。⇒ **本棒 0 依 K‑* 宣告 G4 生死。**

---

## §5 R 阶段 · 状态与「改前清单」

### §5.1 执行状态

⛔ **R 未实施**（按派工硬闸②：P 阶段失败 ⇒ 停手，0 硬闯 R）。

### §5.2 R 改前清单（**已探明 · 未动**；供 PI 裁后复用）

> ⚠️ 派工要求「**R 实施前**须先在本件列明『将改何物、改前态、回退法』」——本棒**未进入 R**，故以下为**候 R 面的预登记**（⛔ 0 执行、⛔ 0 声称已改）。

| 项 | 将改何物 | **改前态（2026‑10‑09 实测）** | 回退法 |
|---|---|---|---|
| **目标文件** | `〔本地绝对路径·脱敏略:MiniMax〕 Code\resources\app.asar`（内嵌 JS chunk） | SHA‑256 `ce221e8d84c0…f36338d`／395,844,226 B／mtime 2026‑10‑04 20:46:02 | ① **改前先全量字节备份**为 `app.asar.g4cf.bak`（同目录）；② 回退＝用备份**整文件覆盖**；③ 备份存在期间⛔ 0 让应用自更新 |
| **E1 打点** | `readRegistrySkillByName` 函数**入口**（新偏移 **100,209,391**）＋ `toNormalizedSkillSelectorSet`（**100,200,309**） | 原样（⛔ 0 改） | 同上（整文件回退） |
| **E2 打点** | `createRuntimeSkillReads` 内 `resolveReadScope` 的 `return { canonicalName, compatibleNames }` 处（新偏移 **100,246,584** 起） | 原样（⛔ 0 改） | 同上 |
| **E3 打点** | ⚠️ **落点须重定**：`LocalSkillTool.execute` 出口（**54,125,479** 起）为**二分支**（§2.3 M‑2），与 E3 原定义三态**不一致** ⇒ 须改落 `readRegistrySkillByName`／`readSkillByName` 内层判定处（**100,248,150**），或改记法 | 原样（⛔ 0 改） | 同上 |
| **E4 打点** | `LocalSkillTool.execute` 入口、`trim()` **之前**（**54,125,479** 起） | 原样（⛔ 0 改） | 同上 |
| **打点件落面** | 独立新文件（如 `<dataDir>\…\g4_probe.jsonl`），⛔ **0** 写既有记录面 | 不存在（新建） | 删除该新文件即可 |
| **⛔ 0 触面** | frozen 资产／V1–V3 资产／`runtime-state.sqlite`／`config.yaml`／`mcp.json`／`local-runtime.auth.json`／仓内既有件 | — | — |

### §5.3 R 的未决阻塞（如实登记，不代裁）

1. **P 失败 ⇒ 硬闸② 拦停**（本棒执行依据）。
2. **E3 落点与定义不一致**（§2.3 M‑2）：若 PI 授权 R，须先裁定「E3 按 `execute` 二分支记」还是「下移至内层 ambiguous 判定记」。
3. **asar 内嵌 chunk 的可写性未验**：本棒⛔ **0 试写**（备份未建前不试）⇒ 「能否安全改、是否有 ASAR 完整性校验／签名」**未验**。
4. **打点件落面路径**未定（`<dataDir>` 下具体位置）⇒ 属实施细节，须 PI 裁或 parent 指定。

---

## §6 0 回改自证（三锚件 · 写盘前／写盘后）

| 锚件 | 写盘前 SHA-12 ／ 字节 ／ mtime | 与在册派工单比对 | 判定 |
|---|---|---|---|
| `results/_g4_controlled_reproduction_design_2026_10_09.md` | `b1c7c24926bb` ／ 23,675 ／ 2026-10-09 09:47:11 | ✅ 逐字一致 | ✅ **0 回改** |
| `results/_g4_residual_probe_2026_10_08.md` | `3554aa156e08` ／ 23,025 ／ 2026-10-08 16:19:49 | ✅ 逐字一致 | ✅ **0 回改** |
| `results/_g4_runtime_state_trace_2026_10_01.md` | `e0ae0ad66acb` ／ 25,631 ／ 2026-10-01 16:31:10 | ✅ 逐字一致 | ✅ **0 回改** |

| 运行时面 | 本棒操作 | 判定 |
|---|---|---|
| `app.asar` | 仅 `mmap` **只读**扫描 ＋ `Get-FileHash`／`Get-Item` | ✅ **0 写入**（SHA‑256 与 §5.2 改前态逐字一致） |
| 安装目录其余文件 | 仅 `Get-ChildItem` 只读列举 | ✅ 0 写入 |
| `<dataDir>`／`%APPDATA%\minimax` | ⛔ **0 写入** | ✅ 0 写入 |
| `runtime-state.sqlite` | ⛔ **0 打开** | ✅ 0 触 |
| 仓内既有件 | ⛔ **0 回改**（本棒写入面＝仅本件 1 件） | ✅ 0 回改 |

**本棒写入面**：**仅本件 1 件**（`results/_g4_reproduction_execution_register_2026_10_09.md`）。⛔ **0 落盘 scratch 脚本**（全部为 `-c` 内联调用）；⛔ **0 移动／重命名／删除**任何文件；⛔ **0 外网**；⛔ **0 skill 调用**。

---

## §7 撞名实测

- 落名前 `glob results/_g4_reproduction_execution*` ＝ **0 命中**；`Test-Path` 拟落名 ＝ **`False`**。
- `results/_g4_*` 现存：`_g4_skill_read_scope_trace_2026_10_01.md`／`_g4_runtime_state_trace_2026_10_01.md`／`_g4_residual_probe_2026_10_08.md`／`_g4_controlled_reproduction_design_2026_10_09.md`——**0 与本件同名**。
- ⇒ **新建，0 覆写**。

---

## §8 交棒指向（**0 派工 · 候 PI 裁**）

1. **M 阶段的净增量结论**：四打点符号**全部仍在**，且已取得**2026‑10‑09 版新偏移**（设计件所载旧偏移确认失效）⇒ **「R 技术上不可行」这一担忧被排除**。
2. **P 阶段的净增量结论**：端点**进程外不可达**（进程内 IPC，`http://local` 虚拟源）⇒ 设计件 §3.2 假设的「低成本先探」路径**在本机不成立**；同时**证实响应 schema 结构层不含 E1／E2 字段**（3 字段：skills／refreshed_at／base_resp）⇒ **即便日后打通进程内取法，P 仍大概率不能免 R**。
3. **⚠️ 一项须 PI 注意的机制偏差**：E3 原定义三态（`undefined`／`ambiguousSkillNameError`／命中 `content`）在本版 `LocalSkillTool.execute` 出口**只呈现二分支**（`found:false`／`found:true`）⇒ 若照原设计打点，**E3 会误判**；此为 R 实施前的**必裁项**。
4. **0 派工**：R 是否实施（及其 E3 记法裁定、asar 备份与回退授权、打点件落面）**均属 PI 口径面**，本棒 0 代裁、0 排期。

---

## §9 自核节

- **写入面**：仅本件 1 件；⛔ 0 scratch 落盘、0 临时件、0 删除／移动／重命名；⛔ 0 改运行时安装产物。
- **命名**：`_g4_reproduction_execution_register_2026_10_09.md` ＝ `_主题_日期`，⛔ 无版本前缀、⛔ 无 `_v5_` 类阶段字样。
- **撞名实测**：见 §7 ⇒ 新建，0 覆写。
- **0 回改自证**：见 §6（三锚件 ＋ 运行时面）。
- **R4**：`config.yaml`／`mcp.json`／`local-runtime.auth.json`／`minimax-agent-cn-config.json` **0 打开 0 读值**；命令行仅布尔判定、0 落原文；⛔ 0 读取任何 key／token／secret。
- **网络**：⛔ 0 外网；P 阶段 13 次请求全部 `127.0.0.1`／`::1` 本地回环（GET，无状态变更），「回环是否算联网」之口径 0 代裁。
- **署名**：本件由 **worker（G4 受控复现执行棒 · session `mvs_ab1ceef5f0c149f6bd362bd7ca73b460`）** 产出；运行时与源码归属 **MiniMax Code 运行时原作者**；⛔ **0 冒认**他方为出证方。
