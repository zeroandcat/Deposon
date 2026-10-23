# FTFB 双审修复 · 第二阶段（文献合并轮）合并说明

- **合并对象**：`查理_FTFB全稿文献合并版_2026-09-16.md`（新链头，未覆盖旧版）
- **前链头**：`查理_FTFB全稿双审修复版_2026-09-16.md`，SHA-256 `bf35c37f5264…8ad535`
- **新链头 SHA-256**：`76eef1dd2294…d7864d0f`（378 行；前链头 368 行）
- **输入**：阿兰补源备忘（7 条一手核验题录）＋鲍勃复核报告（PASS＋4 项观察）
- **改动面**：diff 共 9 hunk，全部为计划内改动（见下），零意外扰动

---

## 一、新条目编号映射表（备忘建议号 → 最终号）

| 备忘号 | 题录 | 最终号 | 首现位置 |
|---|---|---|---|
| R52 | Toulmin 1958, *The Uses of Argument* | **R46** | §6.2 M1 单元格（表行序最先） |
| R46 | Nosek et al. 2018, PNAS 预注册革命 | **R47** | §6.2 M4 单元格 |
| R47 | Chambers & Tzavella 2022, NHB Registered Reports | **R48** | §6.2 M4 单元格 |
| R50 | Pineau et al. 2021, JMLR NeurIPS 可复算计划（主推） | **R49** | §6.2 M4 单元格（另挂 §7.1） |
| R51 | Stodden et al. 2016, Science（备选，已并挂） | **R50** | §6.2 M4 单元格 |
| R48 | Popper 1959, *Logic of Scientific Discovery* | **R51** | §6.2 M5 单元格 |
| R49 | Leavitt & Morcos 2020, 可证伪可解释性 | **R52** | §6.2 M5 单元格 |

**编号依据**：新池内部按正文真实首现序（M1→M4→M5→§7.1）排列，故与备忘的类别序号不同；后续轮次请以本表最终号为准。

## 二、重排影响面（零重编号决策）

- **采用方案**：新条目以独立池块追加——`**Pool R46–R52 (adjunct to §6, §7; added at the dual-review source-supplement pass, 2026-09-16)**`，置于 R45 之后。
- **为什么零重编号**：论文自身惯例＝基础池＋「按轮次附加池」——R40–R41（added at verification）与 R42–R45（added at second-round verification）均为附加式并入，从未回插重编号；本轮沿同惯例。R01–R45 全部既有 [Rnn] 指针（含表格、正文 112 处引用中的 105 处）**零扰动**（脚本核验：排除区间表达后 R01–R45 计数无任何变化）。
- **首现顺序自检**：排除 `[R01]–[R52]`、`[R42]–[R45]`、`[R46]–[R52]` 三处区间端点后，R46→R52 真实首现序与编号序完全一致（已脚本核验）。
- 区间表达同步刷新：§1.3(ii) 与 References 头注的 `[R01]–[R45]` → `[R01]–[R52]`。

## 三、挂点明细（对应派单①）

| 挂点 | 内容 |
|---|---|
| §6.2 M1 单元格 | 追加 `(claim–support correspondence: [R46])`——「本论文形式化」声明保留，Toulmin 作为论证理论原典挂入 |
| §6.2 M4 单元格 | 追加 `(pre-registration: [R47], [R48]; third-party recomputation: [R49], [R50])` |
| §6.2 M5 单元格 | 追加 `(falsifiability: [R51], [R52])` |
| §6.2 归因段 | 「scheduled verification pass」接口句兑现为实引：逐源定位（Toulmin 带文体声明／Nosek＋Chambers 预注册／Pineau＋Stodden 第三方可重算／Popper＋Leavitt 可证伪），并新增 M3 无池内原始文献的如实声明；结尾句改为「The originals supply the practices the criteria formalize; the formalization itself, and the mapping, remain this paper's.」 |
| §7.1 缺口声明 | 挂 R49 作规范依据：「The ask is not ad hoc: making the record and its checks available to reviewers during evaluation is the standard the machine-learning reproducibility program set for its own venues [R49].」——不替代 M4 形式化声明 |

**自裁事项记录**：
1. **M1 挂 R52（Toulmin）＝采纳**。理由：M1 判据原文「the support covers what is asserted」正是 Toulmin claim–data–warrant 布局的核心对应；备忘保留意见（文体差异）以挂点内「a theory of argument rather than a methodology paper, mounted with that genre declared」如实声明消化，不构成名实落差。若不挂则 M1 无任何原始文献，反而落回 Reviewer A 4.1 的批评点。
2. **R51（Stodden）＝并挂**（非仅备选）。理由：Pineau 是 ML 场域审稿期语境的最准来源，Stodden 是跨学科规范层来源；M4 行的第三方可重算判据在论文中是跨体裁移植（hard-SF→AI），两级来源都与挂点匹配，且备忘已一手核验。
3. **M3 不挂**：备忘未给 M3 来源（anchoring 无单独原始文献），归因段已显式声明。

## 四、鲍勃观察 B/C 落点（派单③）

- **观察 B（已落，行 118）**：`The third channel runs on quantities, and its input is an abstraction…` → `Channel III (the quantitative channel) runs on quantities, and its input is an abstraction…`——桥接论文类型名「quantitative」与§4 新分类「abstract quantity」。
- **观察 C（已落，行 298）**：`so the uniform T and R passes are, in part, a product of case selection` → 删 `uniform`（该词与 Channel III scoped pass 的口径冲突）。
- **观察 A（已消化，行 308）**：References 头注 `the closed pool of forty-five verified items` → `the closed pool of fifty-two items`——去 `verified` 一词，核验状态统一由 §1.3(ii) 口径承载。
- **观察 D**：修复说明文档瑕疵，本轮未动论文（派单已明示）。

## 五、计数句全面刷新清单

| 位置 | 旧 | 新 |
|---|---|---|
| §1.3(ii)（行 52） | forty-five items / [R01]–[R45] / forty-three verified / R42–R45 口径 | fifty-two items / [R01]–[R52] / fifty entries verified＋2 pending＋R42–R45 与 R46–R52 各自核验口径 |
| §9.2（行 298） | forty-five items | fifty-two items |
| References 头注（行 308） | forty-five verified items / [R01]–[R45] | fifty-two items / [R01]–[R52] |

## 六、引用闭合自检（脚本核验）

- 正文引用集＝References 表集：52＝52；**悬空（引而无列）0；孤儿（列而无引）0**。
- R46–R52 真实引用计数（排除区间端点）：R46×2、R47×2、R48×2、R49×3、R50×2、R51×2、R52×2（单元格＋归因段＋§7.1）。
- R01–R45 真实指针计数与前一链头**逐项相同**（零扰动）；R45 表观 3→2 系 `[R01]–[R45]` 区间端点随计数句更新为 `[R01]–[R52]`，非真实指针删除。

## 七、纪律自检

| 项 | 结果 |
|---|---|
| 五锚 SHA＋冻结数字 | 2.220446049250313 / 0.8569 / 4/3 / 0.484→0.452 / 0.783→0.739 / 6,760 / 0.669 / 五锚前缀全部 1:1 不动 |
| thesis 与主张句 | 出现 2 次、逐字一致、本轮零改动（纯文献层） |
| 负面结果披露 | §7 全部负面数字与措辞未触碰（diff 9 hunk 中行 231 仅追加 R49 规范依据句） |
| 双盲 | 新题录全部为外部文献，无作者身份 token；deposon / keep the books 残留 0 |
| 红线 | 无 first/only 优先权表述（「only to that extent」为普通范围限定）；References 既有 45 条逐字节未动，仅追加新池块 |
| [R38]/[R39] 声明 | 「this paper's formalization」声明全文保留，新文献仅作方法学原始来源并列挂入 |

## 八、下轮建议（供调度参考）

1. 戴夫排版轮：`#` 残留＋PDF 标题重复＋R-3（引用表新增块随本轮链头 76eef1dd2294 取源）。
2. R14/R36/R37/R12 引用核验仍在阿兰另线（备忘明示「另行安排」），完成后如需改列，将触发首次真实重编号，建议届时仍按附加池或最小扰动原则处理。
3. Reviewer A 未派单项（F-C1/F-C4 强度、F-C3 元条件、structural isomorphism 措辞、Fail 反例）依旧未动。
