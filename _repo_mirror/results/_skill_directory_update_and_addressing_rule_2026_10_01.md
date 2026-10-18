# skill 目录更新与寻址规则（2026-10-01 · C4 核面 ＋ C5 目录更新面）

- **件性质**：**核面＋目录更新执行件**（新建 1 件 · **0 回改既有件** · 0 覆写 · **0 改 runtime 配置** · **0 改 skill 目录**）
- **触发**：PI 批 `ask_d50c961a307949025a7b8d2d` **Q4③** ＝「核『补满全量』是否已办，未办即按 PI 原裁补办」＋「skill 目录更新动作面」
- **上游快扫件**：`results/_forgotten_items_quick_sweep_register_2026_10_01.md`（`91103473289a`）**§2-C4／C5**（两事原态＝**未坐实**）
- **只读输入**（0 回改、0 冒认）：`_skill_reference_update_and_user_surface_survey_2026_09_30.md`（`16861e71305f` 族）· `_skill_load_failure_window_readonly_facts_2026_09_30.md`（`9f5b73620b8a`）· `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md`
- **出件**：**worker**（`mvs_2a45df1650f9406596ad515d03f78059`）· 依派工单执行
- **方法**：PowerShell／Python **只读**枚举 ＋ `findstr`／字节偏移定位读取 `app.asar` 内明文源码 ＋ 一次性只读一致性扫描脚本
- **纪律**：0 编造 ｜ 0 回改既有件 ｜ **R4（0 读 key）** ｜ UTF-8 无 BOM · LF ｜ 0 读 `apiKey`／`mcp.json`／`local-runtime.auth.json` 等敏感值

> **一票结论（三问各一句）**
> ① **「补满全量（＋补记照派）」＝ 已办**（快扫件的「未坐实」是**按文件名的漏检**，非事实）；**② 无需补办**；③ **skill 目录不需要「路径更新」**——实查证明用户面 223 项**自 2026-09-18 起未被触动**（更新未迁移它），而 `Local skill not found` 的**真实根因已定位到 `app.asar` 内加载器源码**：**寻址键＝frontmatter `name`，目录名仅作兜底**；另有**第二失败面（`description` 为空 ⇒ skill 完全不注册）**，本机实测**0 例**。真正要「更新」的是**我方寻址口径**（已随本件执行）＋**22 项 frontmatter 命名不合规**（属改 skill 目录 ⇒ **待 PI**）。

---

## §1 任务① 核面：「补满全量（＋补记照派）」是否已办

**结论：✅ 已办**（内容面证据，非文件名推断）。快扫件 C4 行记「0 件文件名含『补满全量』」——该判据为**文件名面**，而落地件**不以该词命名**，故漏检。

### §1.1 「补满全量」的对象是什么

PI 09-30 收尾小卷 `ask_61300ee638519d59d23a1d33` q2 裁「**改为补满全量**」＝ 把 skill **调用面**从**抽样**改为**全量**（首轮仅 40 枚样本）。

### §1.2 落盘证据链（沿名面定位）

| 环节 | 件 | 本棒独立复算 SHA-12 / 字节 |
|---|---|---|
| 首轮（抽样 40 枚 / 62 次） | `results/_skill_call_surface_probe_2026_09_30.md` | `112346df64fb` / 32,261 B ✅ |
| 补满·甲半（未测 183 枚之 1–92 位） | `results/_skill_call_surface_probe_supplement_a_2026_09_30.md` | `a06316c3c7f2` / 50,658 B ✅ |
| 补满·乙半（未测 183 枚之 93–183 位） | `results/_skill_call_surface_probe_supplement_b_2026_09_30.md` | `69d311e6a4c7` / 82,744 B ✅ |

**三件终值与 survey 件 §9「终值补正与全量结论」表逐字吻合**（本棒 10-01 重新哈希复算，**非转述**）。

### §1.3 全量并集结论已在册

survey 件 **§9**（父棒汇总续记 · 2026-09-30）载：**223/223 全覆盖** ＝ 40 ＋ 92 ＋ 91 ＝ 用户面 **223** 项**全部经真实加载实测**、**0 最终失败**、命中面 223/223 全为用户面。
**「＋补记照派」亦已落**：survey **§8**（文末追加补记）与本节 §9（父棒汇总续记）＝ 两处纯追加节；六项台账件 **§10** 亦记同卷 q2 ＝「补记照派」。

### §1.4 本棒的加强证据（**新**）

survey §9 的「用户面 223 项」**本棒独立坐实**：`C:\Users\Administrator\.minimax\skills\` 实测**恰为 223 个目录**，且 **223/223 均有 `SKILL.md`、0 例缺 frontmatter、0 例缺 `name`、0 例 `description` 为空** ⇒ 按加载器规则**全部可注册**（见 §4.2）。**223 这个数被从两个独立面互证。**

> **边界（照录 §9 原有边界，本棒 0 扩大）**：①「可加载」≠「可执行／质量达标」；②风险面仅及 `SKILL.md` 本体，`references/`／`scripts/` **0 加载 0 断言**；③**本棒未复现** 223 次加载（只读扫描**不等价于**加载实测）——§9 的 223/223 仍**以该件原载为准**。

---

## §2 任务② 补办面处置

**结论：⛔ 不补办。** PI 原裁的**行为目标已达成**（§1），「补办」的对象已不复存在。
**本棒唯一的「办」**＝ 把快扫件 C4 的**「未坐实」状态改正为「已办」并附证据**（即本件 §1）——此为**状态更正**，非新增补办动作，**0 重复上游工作**。
> **未越权**：快扫件 C4 行本身**0 回改**（只读输入）——更正只落在**本件**，由 parent 决定是否并册。

---

## §3 任务③-A 实查：skill 目录／路径现状

### §3.1 三面实测（沿 `9f5b73620b8a` §4-4「普查须按三面枚举」）

| 面 | 路径 | 本棒实测 | mtime |
|---|---|---|---|
| **用户面** | `.minimax\skills\` | **223 个目录** | 条目区间 **2026-09-03 13:35:15 → 2026-09-18 11:46:00** |
| **builtin 面** | `.minimax\.builtin-skills\` | **20 目录 ＋ 1 文件** | **2026-09-29 22:38:32** |
| **plugin-cache 面** | `.minimax\v2\plugin-cache\official\` | **28 棵树** | 单根 `official\` |
| （注册面） | `.minimax\plugins\` | **0 项** | 2026-09-10 14:17:58 |

**三面同名重叠仍为 4 枚**：`docx` / `pdf` / `pptx` / `xlsx`（用户面 ＋ builtin 面均在）——沿 `9f5b73620b8a` §1.5，**三份内容各不相同**（该三哈希本棒**0 复测**）。

### §3.2 运行时与版本面（PI「minimax code 更新了」的落点）

| 项 | 实测 |
|---|---|
| 应用 | `%LOCALAPPDATA%\Programs\MiniMax Code\MiniMax Code.exe` |
| **版本** | **ProductVersion ＝ FileVersion ＝ `3.1.0.170`** |
| 安装落盘 | exe／`app.asar` 均 **2026-09-29 22:25:34**；`resources\` 22:37:28；`.builtin-skills` 22:38:32 |
| `app.asar` | **426,404,876 B** |
| `app-update.yml` | `provider: generic` · `url: https://filecdn.minimax.chat/public/minimax-agent/release` · `updaterCacheDirName: @mmx-agentelectron-updater` |

### §3.3 **PI 假设的关键否证：用户面目录未被迁移**

- `skills\` 下 **223 个目录中，mtime ≥ 2026-09-24 的数量 ＝ 0**。
- 即：**失败窗口（09-24→09-28）内**与**本次更新（09-29 22:25–22:38）**两段时间里，**用户面 skill 目录一个字节都没动过**。
- 本次更新**确实重写**的是 `bin\`（4 个 wrapper；`mcode-tools.*` mtime **2026-10-01 08:47:42**）与 **`.builtin-skills\`（22:38:32）**——**用户面不在其内**。
- ⇒ **「路径变化致失败」对用户面不成立**。`9f5b73620b8a` §3 G3 已把 `.builtin-skills` 的 09-29 mtime 判为**晚于**失败窗口、**不能解释**该窗口；本棒从**另一面**（用户面同样未动）**独立同向**。

---

## §4 任务③-B 根因：`Local skill not found` 的代码级定位

**本棒只读检索了 `9f5b73620b8a` §4-2 指定的唯一未探代码面。** 结果分两步：先**关闭**该指向，再**在真正代码面**定位到根因。

### §4.1 §4-2 指向面已关闭

`.minimax\bin\`（该件记 mtime 2026-09-29 22:38:07）实测**仅 4 个文件**（`mavis-trash.cmd/.js` ＋ `mcode-tools.cmd/-cn.cmd`），**不含任何 skill 解析代码** ⇒ **该件「唯一未探代码面」此路径不成立**。
> 真正代码面 ＝ **Electron `app.asar`**（426 MB，内含**未压缩明文** ESM 源码，`findstr` 可直接命中）。

### §4.2 加载器源码（`app.asar` 字节偏移，可复现）

| 偏移 | 源码 | 含义 |
|---|---|---|
| `52757937`（另见 `54224136`／`95486440`／`107493978`／`107528535`） | `` const text = `Local skill not found: ${name}` `` | `LocalSkillTool.execute`：`readSkill(name)` 返回假值即抛此文案 |
| `14153749` | `export async function loadSkills(env, dirs)` | 递归扫目录，命中 `SKILL.md` 即装载 |
| `14160119` | `async function loadSkillFromFile(env, filePath)` | 单件装载 |
| **`14161217`** | **`const name = frontmatterName \|\| parentDirName;`** | **★ 寻址键 ＝ frontmatter `name`；目录名仅在「无 `name`」时兜底** |
| **`14161440`** | **`if (!description \|\| description.trim() === "") { return { skill: null, ... } }`** | **★ 第二失败面：`description` 空 ⇒ 该 skill 根本不注册 ⇒ 任何名字都 `not found`** |
| `14161793` | `function validateName(name, parentDirName)` | 产出 **`invalid_metadata` warning**（非拒绝）：名≠父目录名／长度 > `MAX_NAME_LENGTH`(`14152910` ＝ **64**)／非 `^[a-z0-9-]+$`／首尾连字符／含 `--` |
| `100194348` | `async readSkillByName(name, scope)` → `registryProvider.readSkillByName(...)` | 查找**纯按 name 键**；且经 `resolveReadScope(scope.agentName, …)` 取 `canonicalName`／`compatibleAgentNames` ⇒ **并按 agent 名分域**；另有 `allowedSkillNames`／`allowedExtensionSkillNames` 选择器闸门 |

### §4.3 根因判定（**有源码支撑**）

1. **主因**：`name` 键来自 frontmatter。**凡 frontmatter `name` ≠ 目录名者，按目录名调用必然 `not found`，按 `name` 值调用必然命中**——**与目录路径无关**。
2. **该主因已被上游实测过、且本棒独立复现**：survey §8 ② 记「22 枚按裸名 **0/22** 成功、22/22 失败形态均为 `Local skill not found`；按 `name` 值 **22/22** 成功」；**本棒 §5 扫描独立得出**同一 22 枚（清单逐项吻合）。
3. **次因（本机 0 例）**：`description` 空 ⇒ 完全不注册。本机 **0 例** ⇒ **不构成本机任何失败**。
4. **命名不合规 ＝ warning 而非拒绝**：`validateName` 的报错**只进 diagnostics**，**不影响注册** ⇒ 那 22 枚**仍可按其 `name` 值调用**（与 §4.3-2 实测一致）。

---

## §5 任务③-C 一致性扫描（223 项 · 按 §4.2 规则逐条复算）

扫描器：`.tmp\skill_conformance_scan_2026_10_01\scan.py`（**只读**；`errors='replace'` 容错；手写 frontmatter 解析，兼容 `name`／`description` 的标量／引号／块标量 `|` `>` 形态）。
输出：`.tmp\skill_conformance_scan_2026_10_01\out.json`（**scratch 面，非交付件**）。

| 指标 | 值 |
|---|---|
| 目录总数 | **223** |
| 缺 `SKILL.md` | **0** |
| 无 frontmatter | **0** |
| 无 `name` 键 | **0** |
| `description` 缺失／为空（⇒ 不注册） | **0** |
| **合计不可注册** | **0** |
| **可按目录名寻址** | **201** |
| **只能按 frontmatter `name` 寻址** | **22** |
| 带 `validateName` warning | **22**（与上同集） |

### §5.1 「只能按 `name` 值寻址」22 枚（**可操作核心**）

| # | 目录名（**不可**用作寻址键） | 实际寻址键（frontmatter `name`） |
|---|---|---|
| 1 | `abstract-writing` | `Abstract Writing` |
| 2 | `academic-paper-writing-expert-zip` | `论文写作专家` |
| 3 | `antimicrobial-stewardship` | `Antimicrobial Stewardship` |
| 4 | `bayesian-clinical-reasoning` | `Bayesian Clinical Reasoning` |
| 5 | `clinical-decision-rules` | `Clinical Decision Rules` |
| 6 | `critical-appraisal` | `Critical Appraisal` |
| 7 | `differential-diagnosis-generation` | `Differential Diagnosis Generation` |
| 8 | `dose-adjustment` | `Dose Adjustment` |
| 9 | `drug-interactions` | `Drug Interactions` |
| 10 | `evidence-levels-and-hierarchies` | `Evidence Levels and Hierarchies` |
| 11 | `grade-assessment` | `GRADE Assessment` |
| 12 | `hypothesis-testing` | `Hypothesis Testing` |
| 13 | `illness-scripts` | `Illness Scripts` |
| 14 | `imrad-structure` | `IMRAD Structure` |
| 15 | `lab-interpretation` | `Lab Interpretation` |
| 16 | `prd-to-prototype` | `PRD to Prototype` |
| 17 | `rct-design` | `RCT Design` |
| 18 | `regression-analysis` | `Regression Analysis` |
| 19 | `sample-size-calculation` | `Sample Size Calculation` |
| 20 | `sensitivity-and-specificity` | `Sensitivity and Specificity` |
| 21 | `shared-decision-making` | `Shared-Decision-Making`（frontmatter 值含 U+2011 非断行连字符） |
| 22 | `survival-analysis` | `Survival Analysis` |

> 第 2 项 `name` 经**逐码点复核** ＝ `U+8BBA U+6587 U+5199 U+F5C4 U+4E13 U+5BB6`（论／文／写／作／专／家）六字，**非**控制台乱码（控制台 mojibake 已排除）；该 `SKILL.md` 首 3 字节 ＝ `45,45,45` ＝ `---`，**无 BOM**。
> 22 枚**全部**同时触发两条 warning：①`name` 与父目录名不符；②含非法字符（空格／大写／CJK）。

### §5.2 失败窗口关键 skill 的本棒定位

| skill | 用户面 | 寻址键 | 可注册 |
|---|---|---|---|
| `scientific-writing` | **在** | `scientific-writing`（＝目录名） | ✅ |
| `peer-review` | **在** | `peer-review` | ✅ |
| `minimax-docx` | **在** | `minimax-docx` | ✅ |
| `experimental-design` | **不在用户面** | —（plugin-cache 面） | — |
| `verification-before-completion` | **不在用户面** | —（plugin-cache 面） | — |
| `academic-paper-polish` | **不在用户面** | —（plugin-cache 面） | — |

⇒ `9f5b73620b8a` §1.2 记「这 5 个关键 skill 在 `skill-hub.json` 各 0 命中」**在用户面得到分化解释**：其中 3 枚**本就在用户面**（且可按目录名寻址），另 3 枚（`experimental-design`／`verification-before-completion`／`academic-paper-polish`）**根本不在用户面** ⇒ 其 `plugin:skill` 限定写法**必须走 plugin-cache 面**，**不能**用用户面裸名试。

---

## §6 任务③-D 更新方案与执行

### §6.1 诊断改写（PI 假设 → 实测）

| PI 09-30 原述 | 本棒实测结论 |
|---|---|
| 「skill 目录需要更新了」 | **目录本身健康**：223/223 有 `SKILL.md`、0 例不可注册、0 例被迁移 ⇒ **不需要「目录更新」来修复加载** |
| 「minimax code 更新了，**不知道路径发生了什么改变**以致失败」 | **路径未变**（用户面 09-18 后未动）；变的是**寻址语义**——加载器按 frontmatter `name` 建键（§4.2 `14161217`） |
| 「致失败」 | 失败面 ＝ **寻址键用错**（22 枚）＋（潜在）`description` 空（本机 0 例） |

### §6.2 ✅ 已执行（**本棒，安全面**）

1. **产出本件**＝「目录更新」的可交付形态：**223 项寻址规则＋22 枚映射表**（§5），供全队遵用。
2. **寻址口径落定**（沿 survey §8 ② 已提示、该件 0 回改的「拟用口径应按 `name` 值寻址」）：
   - **默认按 frontmatter `name` 调用**；
   - 仅当 `name` ＝ 目录名时，目录名与 `name` **二者皆可用**（201 枚）；
   - **22 枚只能用 `name` 值**，目录名**必然** `not found`。
3. **登记 §4.2 源码偏移**（可复现定位 ＝ 后续棒 0 必重做）。
4. **关闭 `9f5b73620b8a` §4-2 指向**（`bin\` 无解析代码）并**给出真正代码面**（`app.asar`）。

### §6.3 ⛔ 未执行（**待 PI** · 敏感／运行时面）

| # | 动作 | 为何待 PI |
|---|---|---|
| P1 | 把 22 枚 `SKILL.md` 的 `name` 改成合法 slug（消除 2×22 warning） | **写 skill 目录**；且改 `name` **等于改运行时寻址键** ＝ 改运行时行为面。`9f5b73620b8a` 全程「0 改配置 / 0 改 skill 目录」，本棒**不越此界** |
| P2 | **重命名目录**去迁就 `name` | 同 P1 ＋ 目录重命名风险高于改 frontmatter，**0 建议** |
| P3 | 改 `config.yaml` / `skill-hub.json` / `.minimax\plugins\` / `.builtin-skills\` / plugin-cache | runtime 配置／内置面；且 `config.yaml` 含 `apiKey`（**R4：0 读值**） |
| P4 | 建软链／junction 兜底目录名 | 运行时面，且会**新增** 22 个实体目录，**0 建议** |
| P5 | 复核 `docx/pdf/pptx/xlsx` 三面遮蔽优先级（G2） | 需跨面优先级判定，**超单棒**，且涉运行时解析序 |
| P6 | 把本件并入快扫册 C4/C5 行 | **回改他人件**，由 parent 裁 |

---

## §7 仍未闭（原样承接，**0 冒充已解**）

`9f5b73620b8a` §3 **G4**（「同写法同实体同日两会话结果相反」）**本棒未闭**。新得**代码级线索**（**线索，非结论**）：`readSkillByName` 经 `resolveReadScope(scope.agentName, …)` 取 `canonicalName`／`compatibleAgentNames` ⇒ **查找按 agent 名分域**，且存在 `allowedSkillNames`／`allowedExtensionSkillNames` 闸门 ⇒ 父子会话结果差异**有可能**源于 agent 域／闸门差异。
**但本棒 0 追进 `registryProvider.readSkillByName` 内部**（未读其 `plugin:` 前缀处理与闸门判定）⇒ **不下因果结论**，仅登记为下棒指向。

---

## §8 诚实边界（逐条）

1. **0 回改既有件**：`_forgotten_items_quick_sweep_register_2026_10_01.md` / `_skill_reference_update_and_user_surface_survey_2026_09_30.md` / `_skill_load_failure_window_readonly_facts_2026_09_30.md` / `_fake_verdict_reverify_sixitem_ledger_2026_09_30.md` **全部只读**，0 写入、0 覆写、0 删除、0 重命名。
2. **0 改 skill 目录 / 0 改 runtime 配置**：`skills\` 223 项、`.builtin-skills\`、plugin-cache、`config.yaml`、`skill-hub.json`、`.minimax\plugins\` **全部只读**。
3. **R4 遵守**：**0 读取**任何 `apiKey`／token／端点值；**0 读** `mcp.json`、`local-runtime.auth.json` 等敏感文件。§3.2 只记**键名面**与**非敏感版本/URL 面**。
4. **0 LLM / 0 API / 0 外部 URL**：全部证据来自**本机盘上**与**本机 `app.asar`**。
5. **扫描 ≠ 加载**：§5 为**静态规则复算**，**不等价于**真实加载实测；§1.4 的 223/223 可注册是**规则层推断**，`survey` §9 的 223/223 加载实测**本棒 0 复现**。
6. **源码引用为偏移级**：§4.2 偏移与代码行为由**本机字节读取**确认；**未完整反编译** `app.asar`，故对 `plugin:` 前缀与闸门**0 断言**。
7. **`.minimax\bin\` 结论为「该 4 个文件内无」**——**不等价于**「整个运行时无此逻辑」；真正代码在 `app.asar`（已定位）。
8. **CJK 名字已复核**：以逐码点读取确认，**排除**控制台编码假象。
9. **`.tmp` 两件为 scratch**（扫描脚本与 JSON），**非交付件**、可随时重建，不计入 `results/` 件数。
10. **本件自身 SHA-12／字节不可内嵌**（自引用悖论）——落盘后由 parent 对**终态**复算回填。
11. **succeeded ≠ 跑完**：§3.3 的「0 目录 mtime ≥ 09-24」是**目录 mtime 口径**；若更新采取「复制到新目录后删旧」，理论上可使 mtime 不可见——本棒**0 见到**此类痕迹，但**0 排除**该可能（诚实记为口径限制）。
12. **未核 plugin-cache 28 棵树的 skill 总量**（沿 `9f5b73620b8a` §3.1，**不冒认** 172 之数）。

---

## §9 自核节

- **写入面**：**仅本件 1 件**（`results/_skill_directory_update_and_addressing_rule_2026_10_01.md`）＋ `.tmp\skill_conformance_scan_2026_10_01\` 下 2 个 scratch 文件。
- **命名**：去版本前缀、无 `_v5_` 类阶段字样（沿 PI 09-29 命名裁）；落名前 **2 轮撞名实测**（4 目录直查 5/5 `exists=False` ＋ 全仓递归 glob `*addressing*`／`*directory_update*` **0 命中**）⇒ **新建，0 覆写**。
- **哈希口径**：`Get-FileHash -Algorithm SHA256` 全值算完**截前 12**（小写）——**非** SHA-1 冒充。
- **编码 / 版式**：UTF-8 **无 BOM** · **LF**（落盘后实测核验首字节 ＋ `\r` 计数，**不预填**）。
- **0 回改自证**：三件锚件 SHA-12 于**本棒开工前后**逐字一致 ＝ `16861e71305f` 族／`9f5b73620b8a`／`91103473289a`（`91103473289a` 本身于 10:05:19 后**未再被本棒触动**）。
- **并发写入面**：本棒工作期间 `results/` 有其他棒并发写入可能 ⇒ 目录级件数／总字节快照**不构成**干净 0 回改证据；本棒 0 回改自证**限定于**上述锚件终态复算 ＋ **本棒写入面仅本件 1 件**。
- **署名**：**worker**（`mvs_2a45df1650f9406596ad515d03f78059`）· 出件即本棒，**不冒认**他方名头。
- **无既有件被回改、无 runtime 面被触碰、无 key 被读取**——三条均可在盘上复验。
