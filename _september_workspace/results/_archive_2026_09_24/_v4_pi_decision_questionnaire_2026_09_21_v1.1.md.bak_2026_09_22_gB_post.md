# V4 PI 拍板问卷（deposon V4 蒸馏主题重建）

**文档类型**：待 PI 逐条作答的拍板问卷（不裁决、不推荐、不排序）
**版本**：v1.1（2026-09-21 第二轮更新）
**Prior 版本**：v1.0（2026-09-21）
**日期**：2026-09-21
**起草方**：`doc-writer`（Mavis 8-agent team，deposon 工作区）。人类 principal investigator 是本文件唯一可作答主；AI 不是作者。
**密级**：内部；与邀请函 §6.1、§6.2 一致的边界纪律。
**边界**：read-only against V1–V3 资产；未触动 18 frozen 制品、未触动 P-G v0+v01、未触动 schema v1、未触动 verifier/、未触动 plugin spec；未调用任何 LLM API；未抓取任何外部 URL；未引入任何密钥、端点或专有提示词。

**行数与哈希自测双口径**：本文件自身不内嵌自身 SHA-12 / 字节 / 行数（避免自指哈希反复自修改的循环）；本文件自身的 SHA-256[:12]、字节数与两种口径行数在本会话的最终回报中给出。本文件内部所有引用一律按 `ReadAllLines`（UTF-8）口径计行。**PI 拍板 P6（2026-09-21）**：以 `ReadAllLines` UTF-8 为 canonical 口径；早前 `Get-Content` 不指定 `-Encoding` 的 636 / 277 行数作废。

## 本版本变更摘要（v1.0 → v1.1，第二轮）

本版在 v1.0 基底上做**最小增量改动**，改动按 PI 2026-09-21 拍板（P1–P6）+ 三组 worker 复算结论（组 A / B / C）落点分布：

- **P1（GLM 回函归属）**：v1.1 §0 新增 GLM 查理件锚表；§4 系列按 P1 给出 GLM 接收侧 paper-track 通道归属。
- **P2（豆包工作归属 + 756/761 唯一归属 GLM）**：v1.1 §2.9 改为「已拍板：唯一归属 GLM（2026-09-21）」；§4.1 拍板字段列 GLM 路径 A；§0 表 747/766 维持豆包工作归属。
- **P3（coze / codex 引用形态）**：v1.1 §2.10 改为「已落盘 results/」；§4.3 拍板字段列结果/路径 A；§4.2 维持 §1.0 的「results/ 与附件同哈希」原文。
- **P4（全部派 worker 复算）**：v1.1 §7 新增「第二轮复算结论汇总」（组 A / B / C 全量）；§4.4 / §4.5 拍板字段回填组 B 7 命中 + 组 C 8 条（C1 / C2 / C3 / C4 / C5 / C6 / C7 / C8）。
- **P5（A-4 断行自检）**：v1.1 §6 末段标注「PI 已接受（2026-09-21），按此定稿」。
- **P6（行数口径）**：v1.1 文首明示 canonical = `ReadAllLines` UTF8；§0.4 / §6 末段显式说明 636 / 277 误口径作废。
- **§5 逐条作答表**：把 P1–P6 六项拍板回填到对应行；其余未答行保持「待答」；表下方列「已答行号清单」。
- **§6 末段老实交代更新**：含 worker 无法加载 superpowers plugin 端点、仅以方法论执行这一事实；含 v1.0 整合稿 + v1.0 问卷原件 SHA-12 不变（自验 4 实证）。

---

## §0 本问卷的性质与用法

**谁作答**：本问卷的答主是唯一的人类 principal investigator。各方回函（Mavis / Trae code / Trae work / Claude Code / coze / workbuddy / kimi / 豆包工作 / 署名 `an invited reader team (multi-agent)` 的 756+761 联合件 / codex）已各自提交了一份批注；这些批注在盘上被本文件引为"新增问题"或"结构性分歧"的依据，但答主不是这些回函方。任何一位回函方不可代 PI 作答。

**答完去哪**：本问卷**不**指定任何后续流程，不把答完通往哪一个产物（更新邀请函 / 重发某个章节 / 落盘到 results / 落盘到 corpus / 落盘到 docs/V3X / 不落盘仅作答）。PI 在每条作答栏内可自由决定答完后该条的去向；本文件不替 PI 预设路径。

**不定项的后果**：本问卷的每一条都是开放项；PI 选择"不定"/"暂不裁定"或留空，会导致该条继续以未决状态存在于邀请函与各回函方之间。任何一条留空**不**自动触发冻结、不自动触发升级、不自动把决定权下放给任何 agent。PI 的留空是 PI 的留空。

**不引入框架词汇。本文件不构造"上一步 / 下一步 / 必须 / 应当 / 建议 / 推荐"等措辞**。每条决策点把可选路径**并列**列出，PI 选哪条、不选哪条、是否选新条都属 PI 自由。本文件逐字逐行回避禁框架词（详见派工单 §3 第 1 条所列禁词，本段不枚举）；例外为逐字引用来源原文，已逐条标注「引文」并给 path + SHA-12 + 行号。本文件下文凡出现禁框架词，均为 (a) 邀请函 §5.1 L270–L279 的「paper-track reviewer / IDE-track reviewer」逐字引用、或 (b) 盘上文件名内含的 phase1 / phase2 / phase4 / phase B 等字符串——均已就近标注。v1.1 注：v1.0 L22 原版的禁词清单枚举在 v1.1 中删除（避免框架词自命中），约定未变。

**回函方的措辞纪律**：本文件不重述回函方的"建议选 X"。回函方提出的新种子、新方向、新问题，本文件以"提出方 / 原文要点 / 锚（path:SHA-12:行号）/ 挂在哪一条既有未决项上"四列**并列**呈现。

**v1.1 §0.x 锚表新增（PI 拍板 P1）**：

GLM 查理件：附件路径 `C:\Users\Administrator\.minimax\v2\assets\2026\09\20\15-30-44-659-asset_20260920-153044-659_ac74a04efeb2_0a7da13e-查理_V4接受回执与D1首轮反馈_2026-09-20.md`，SHA-12 `ac74a04efeb2`；对象为 `results/_v4_experiment_invitation_2026_09_20.md` (`4E8C0EA57028`，实验邀请函 draft v0.1，**非**蒸馏邀请函)；署名「GLM 接收侧 paper-track 审查」，5-agent 团队执笔标注为查理。本件不在本问卷的蒸馏主题未决项内占位（详见 §7 第二轮复算结论汇总）。

---

## §1 邀请函自身的未决项（待答基线）

本节把邀请函 §4 开放问题与 §7 未决项的**全部**编号逐条抄出，作为 PI 作答的基线。邀请函两份清单均**编号跳号**（§4 缺 2/6/8/10/12，§7 缺 7/9/11/13/15）；跳号本身要记录。邀请函原文括注内"同行其他字句"在本节以**引文**标注。

邀请函全文：`results/_v4_distillation_invitation_2026_09_20_v1.0.md`，SHA-256[:12] `3D9F73519F6C`，53,539 B；下文行号一律对应该邀请函物理行。

### §1.1 邀请函 §4 开放问题（共 7 条；编号 1, 3, 4, 5, 7, 9, 11；缺 2, 6, 8, 10, 12）

> 引文（邀请函 §4.0 L250）："The following questions are *not* seeds … and *not* commitments … They are *open questions the rebuild leaves on the table*, and the principal investigator invites the recipient community to surface their own additions or replacements. **No ordering is implied.**" — `3D9F73519F6C:250`

| 邀请函编号 | 决策点（邀请函原文要点） | 邀请函原文锚 | PI 作答栏 |
|---|---|---|---|
| §4.1 | "**What is the smallest, falsifiable experiment that can distinguish "distilled from teacher X" from "trained independently on similar data"?** This is the *minimum* claim a distillation-detection benchmark would need to support. The reviewers flagged multiple blockers (R5 from KIMI-K3 on divergence definitions; B6 from Trae code on binning/KDE) that any answer would have to overcome." | `3D9F73519F6C:252` | |
| §4.3 | "**Can the V1–V3 evaluation grid be treated as a *student*-side signal surface at all?** The grid is a *teacher-side* evaluation; treating it as a student-side signal surface requires a hypothesis about what a distilled student would look like that has no current on-disk support." | `3D9F73519F6C:253` | |
| §4.4 | "**Is the 22-caption fingerprint a viable "stealth watermark" seed?** The 22-caption fingerprint was built for discrimination, not for output-watermarking (S-13, S-19). Re-using it as an output-watermark prototype is a re-fit hypothesis, not a calibrated finding." | `3D9F73519F6C:254` | |
| §4.5 | "**What would a *reverse*-distillation claim even look like, given that deposon's artifacts are teacher-side and have no student-side ground truth?** This is the GT dilemma (S-36). Any distillation-themed experiment must declare its GT source." | `3D9F73519F6C:255` | |
| §4.7 | "**Does the theme have a defensible scope that excludes the cross-disciplinary seeds (Dimension 6)**? Or is the analogy space (curvature, observer effect, no-cloning, Bell) part of the theme's natural vocabulary? This is a *scope* question, not a *priority* question." | `3D9F73519F6C:256` | |
| §4.9 | "**Which of the 40 seeds are *productive* questions and which are *non-productive*?** Productivity here means: would a concrete, falsifiable experiment that falsifies the question also falsify a substantive claim? The principal investigator does not pre-judge this for any seed." | `3D9F73519F6C:257` | |
| §4.11 | "**Does the *theme-driven, framework-free* invitation actually help the recipient community engage, or does it leave them without enough scaffolding to contribute?** This is a question about the invitation itself." | `3D9F73519F6C:258` | |

**跳号本身**：邀请函 §4 列出 7 条；数字 2, 6, 8, 10, 12 未出现。邀请函 §4 末尾"**The list is open**"（L260）与本节无关。PI 是否在跳号处插条目、保持跳号、或在数字上承认第 12 处由 PI 自定，均属 PI 自由。锚：`3D9F73519F6C:260`。

### §1.2 邀请函 §7 未决项（共 11 条；编号 1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16；缺 7, 9, 11, 13, 15）

> 引文（邀请函 §7.0 L348）："This section names items the rebuild leaves explicitly unresolved. The principal investigator invites corrections, additions, and replacements." — `3D9F73519F6C:348`

| 邀请函编号 | 决策点（邀请函原文要点） | 邀请函原文锚 | PI 作答栏 |
|---|---|---|---|
| §7.1 | "**The 9-backbone / 5-artifact mapping (Claude Code §2 finding).** V1–V3's evaluation grid is 9-backbone × 60 cells. The `corpus/v20/by_model/` layer is 5 artifacts. The reviewer community has not been told which of the 9 backbones map to which of the 5 artifacts, and on disk the mapping is not declared. **Until the principal investigator declares a mapping, any claim about 'the 9 teachers' or 'the 5 teachers' is under-specified.** `[待 PI 裁定]`" | `3D9F73519F6C:350` | |
| §7.2 | "**The 21-vs-22 caption count (B4).** The on-disk count is 22 (`corpus/v20/strip_captions_22.json`). The V0.1 prose said '21 caption-fingerprint pairs.' The two numbers describe different things (entries vs. pairs). `[待 PI 裁定]`" | `3D9F73519F6C:351` | |
| §7.3 | "**The `M3` / `minimax` directory name (B1, F1).** The on-disk name is `minimax`. V0.1 prose wrote `M3`. `[待 PI 裁定]`" | `3D9F73519F6C:352` | |
| §7.4 | "**The KIMI public-vs-API naming.** On disk: `kimi-for-coding` is the API endpoint (per the principal investigator's 2026-09-08 rule). In deposon-side prose: `KIMI-K3` is the public product name. The two are not the same string. `[待 PI 裁定]`" | `3D9F73519F6C:353` | |
| §7.5 | "**The `V7` / `R5` version identifier (F4).** On disk: V7. The principal investigator must rule on whether deposon-side prose should ever write `R5`. `[待 PI 裁定]`" | `3D9F73519F6C:354` | |
| §7.6 | "**The P-G v01 verdict_pending status.** P-G v01 is **scaffolding tier, verdict_pending=true**. The principal investigator must rule on whether deposon-side prose may treat P-G v01 as anything other than a scaffold. `[待 PI 裁定]`" | `3D9F73519F6C:355` | |
| §7.8 | "**The `_v4_experiment_invitation_2026_09_20_v0.2.md` lineage.** This rebuild is *not* a successor-version of v0.2 in the strict semantic-versioning sense. v0.1 and v0.2 are framework-bearing proposals; v1.0 is a theme-first rebuild. `[待 PI 裁定]`" | `3D9F73519F6C:356` | |
| §7.10 | "**The seed-field's cross-disciplinary seeds (Dimension 6).** The author of the seed field has flagged Dimension 6 as 'optional; not steered toward or away from.' `[待 PI 裁定]`" | `3D9F73519F6C:357` | |
| §7.12 | "**The non-framework principle itself.** This rebuild is framework-free by the principal investigator's instruction. A future revision may decide that *some* scaffolding … would help the recipient community engage. `[待 PI 裁定]`" | `3D9F73519F6C:358` | |
| §7.14 | "**The recipient list (§5.1).** The principal investigator has named 8 existing recipient communities plus 'any new collaborator.' A future revision may add, retire, or merge recipients. `[待 PI 裁定]`" | `3D9F73519F6C:359` | |
| §7.16 | "**The reviewer-burndown.** The V0.2 framework absorbed nine independent reviewer responses … Each of those responses contained a *theme-level* observation buried inside a *framework-level* critique. The principal investigator may wish to recover the theme-level observations explicitly; this rebuild does not do so, because doing so would re-import the framework the rebuild has set aside. `[待 PI 裁定]`" | `3D9F73519F6C:360` | |

**跳号本身**：邀请函 §7 列出 11 条；数字 7, 9, 11, 13, 15 未出现。锚：`3D9F73519F6C:362`。PI 是否在跳号处插条目、保持跳号、或在数字上承认第 15 处由 PI 自定，均属 PI 自由。

### §1.3 邀请函 §6.4 命名占位符（已在 §7.3, §7.4, §7.5, §7.6 中显式化为未决项；其余两行作为基线附录）

> 引文（邀请函 §6.4 L332）："The following proper nouns appear in this invitation or its supporting seed file, but the principal investigator has not, in writing, confirmed a canonical form for each. Recipients are asked to read placeholders as placeholders." — `3D9F73519F6C:332`

- 占位符表第 4 行 `P-G v01`：与 §7.6 同议题；锚：`3D9F73519F6C:339`。
- 占位符表第 1 行 `KIMI-K3`：与 §7.4 同议题；锚：`3D9F73519F6C:336`。
- 占位符表第 2 行 `M3` / `minimax`：与 §7.3 同议题；锚：`3D9F73519F6C:337`。
- 占位符表第 3 行 `21 caption-fingerprint pairs` / `22 captions`：与 §7.2 同议题；锚：`3D9F73519F6C:338`。

---

## §2 各方新增的开放问题

本节按参与方分组，每条：提出方 / 原文要点 / 锚（path:SHA-12:行号）/ 挂在哪一条既有未决项上。每条**并列**列出；PI 选哪条、不选哪条、是否选新条均属 PI 自由。

### §2.1 Mavis / `doc-writer`（主题回复 v1.2）

- **§2.1.a** Mavis 提议加入邀请函 §4 的开放问题第 8 条：「**Is the V1–V3 asset stack large enough to support a theme that, by construction, requires both teacher-side and student-side samples?**」原文："the stack contains one generic knowledge-distillation baseline" of Mavis 主张，盘上**有** KT-B1 系列（见 §3.3）。挂：§1.1 §4.5 与 §3.2。锚：`D:\私人资料\deposon-repo\results\_v4_theme_reply_mavis_2026_09_20_v1.2.md`（SHA-12 `3ECF5B38048E`）§4 (d) L196；36,826 B。

### §2.2 Trae code / IDE-track（逐字引用邀请函 §5.1 L271；邀请函 `3D9F73519F6C:271`）

- **§2.2.a** Trae code 提议加入邀请函 §4 的开放问题："**what is the chance-level attribution rate for the existing five-artifact panel (two same-lineage artifacts, one differently-shaped record), and is the recorded 4.4% FPR distinguishable from it?**" 原文："Without a null model, the number has no reference class; with one, the same number becomes evidence." 挂：§1.1 §4.5、§1.2 §7.1、§3.2。锚：`D:\私人资料\deposon-repo\results\_v4_distillation_reply_trae_code_2026_09_20.md`（SHA-12 `E87EC8F7E2FE`）§(d) L79 与 Addendum I A L85–L92；43,570 B。
- **§2.2.b** Trae code 提出"trap-benchmark spec, brought on disk"（Addendum I B），作为 S-36 的"most worth pursuing" 路径——把 V1 paper 的 trap design（arXiv:2609.09001）首次落到盘上，作 S-36 的"who labels GT"问题的可执行答案之一。挂：§1.1 §4.5、§3.2。锚：`E87EC8F7E2FE:96–101`（Addendum I B 段）。
- **§2.2.c** Trae code 提出"Measurement-instrument stability probe"（Addendum I C）作为邀请函 §4 缺失种子；该种子挂在 §3.3 第 8 条与 §3.3 第 9 条的盘上实测案例。锚：`E87EC8F7E2FE:103–110`。

### §2.3 Trae work / IDE-track（逐字引用邀请函 §5.1 L272；邀请函 `3D9F73519F6C:272`）

- **§2.3.a** Trae work 提议加入邀请函 §4 的开放问题："**For every cross-vendor statistic in this stack, how many independent sides does the denominator actually contain — and which on-disk artifact states that number?**" 原文："Until that is answered, 'cross-vendor' is a claim about directories, not about independence." 挂：§1.1 §4.5、§1.2 §7.1、§3.4（5 厂商同谱系问题）。锚：`D:\私人资料\deposon-repo\results\_v4_theme_reply_trae_work_2026_09_20_v1.2.md`（SHA-12 `6BEE6EC434BD`）Closing 段 L139；28,395 B。

### §2.4 Claude Code / IDE-track（含跨子代理复算）（逐字引用邀请函 §5.1 L274 GLM/271 paper-track 旁类 IDE-track 回函通道；邀请函 `3D9F73519F6C:271–279`）

- **§2.4.a** Claude Code 报告"邀请函 §0.2 L26 'V1–V3 has zero distillation experiments on disk' 与盘上 KT-B1 系列抵触"（见 §3.3 第 3 条详细引文）。该报告本身不是新开放问题，但它把邀请函 §0.2 推入"需要 PI 重新裁定"的状态。挂：§3.3 第 3 条。锚：`D:\私人资料\deposon-repo\results\_v4_distillation_reply_claude_code_2026_09_20.md`（SHA-12 `D39CB17B051B`）§5.11 L360–L385；64,212 B。
- **§2.4.b** Claude Code 报告"邀请函 §8 表 8 行未填 SHA-12"——`_v4_brainstorm_seeds_2026_09_20.md` 等 8 处被 PI 标 `(see SHA-12)`；该报告对"长期引用"留下 open question。挂：§1.2 §7.16、§3.9。锚：`D39CB17B051B:68`。

### §2.5 coze / paper-track（逐字引用邀请函 §5.1 L274；邀请函 `3D9F73519F6C:274`）

- **§2.5.a** coze 提议"种子场性质标签取值域不闭合"：邀请函 §3.0 L140 用 `disk fact` / `pure speculative` 二分；§2 用 `re-fit hypothesis (not calibrated)` 第三档；§3 的 40 条种子没有任何一条带 `disk fact` 标签；21/40 条在 Related asset 行点名了盘上制品但仍标 `pure speculative`。coze 提议合并取值域：`re-fit hypothesis` 并入 §3.0。挂：§1.1 §4.9、§3.4。锚：`D:\私人资料\deposon-repo\results\_v4_distillation_reply_coze_2026_09_20.md`（SHA-12 `00593014CBD3`）Engagement 段 L21–L33；71,084 B。
- **§2.5.b** coze 提出 N-01 ~ N-08 八条候选种子；其中 **N-01 "端点在不在冒充它自己宣称的那个教师"** 的载体是 `results/_p_l_v3_phase2_closedsource_report_20260917_175544.md`（盘上文件名内含 phase2 字符串，非创作层 phase 框架；5,909 B · SHA-12 `02443DD300CE`）。挂：§1.1 §4.7（Dimension 6 in-scope 讨论相邻）。锚：`00593014CBD3:300–309`（N-01 段）。
- **§2.5.c** coze 提出 N-04 "评测的参照推理本身就是某个模型的输出"，载体是 `results/deposon_benchmark_v1_4_strategyqa_details.json`（235,779 B · SHA-12 `A63EBEA7B29A`），L13/L18 等 396 处来源标签全部为 `kimi_api`。挂：§1.1 §4.5、§3.2。锚：`00593014CBD3:336–346`。

### §2.6 workbuddy / workplace-bundle

- **§2.6.a** workbuddy 在 part 1 / part 2 / brainstorm 三遍中均未在 §4 末尾提议新增开放问题；其 C1–C5 站不住的 5 条全部已在邀请函本身 §4 / §7 范围内处理，挂载见各条原始锚。
- **§2.6.b** workbuddy brainstorm 提出"把 anti-distillation 反转"为"教师主动移除散射层使其不可被提取"——是 S-25/S-26/S-27 维度的"教学侧反向操作"提法，挂：§1.1 §4.7（Dimension 6 / 反蒸馏的语义边界）。锚：`D:\私人资料\deposon-repo\results\_v4_distillation_theme_reply_workbuddy_brainstorm_2026_09_21.md`（SHA-12 `CDB27CD3008C`）透镜① 条目 7 L26；13,553 B。
- **§2.6.c** workbuddy brainstorm 提出"用 embedding 全 NOISE 做负向预注册"，载体是 `deposon_v3_v7_summary_2026_09_11.json` 高 2 失败原因。挂：§1.1 §4.9、§3.6。锚：`CDB27CD3008C:37`。

### §2.7 kimi / paper-track（逐字引用邀请函 §5.1 L270；邀请函 `3D9F73519F6C:270`）

- **§2.7.a** kimi 提议加入邀请函 §4 的开放问题：「**哪些盘上工件真的含模型输出原文，哪些只有哈希或判别值？**」原文："§8 资产表只列字节与哈希、不列内容形状，这是核资产清单的盲区。" 挂：§1.2 §7.1、§3.5、§3.8。锚：`D:\私人资料\deposon-repo\results\_kimi_v4_theme_reply_2026_09_20.md` §4 (d) L45；7,372 B。
- **§2.7.b** kimi 提议加入种子场："同输入跨厂商输出对比作为行为基线，今天能建成什么样"——直接坐在 by_model 层与 `deposon_v2_phase1_60cells_2026_09_11.json`（盘上文件名内含 phase1 字符串，非创作层 phase 框架）逐格输出上。挂：§1.1 §4.5。锚：`_kimi_v4_theme_reply_2026_09_20.md:45` §4 (c)。

### §2.8 豆包工作 / workplace-bundle

- **§2.8.a** 豆包工作（v1.0 主题回复 + 21 条 brainstorm）提议加入邀请函 §4 的开放问题："**V1–V3 资产的采集时间窗口是否足以捕捉蒸馏效应的时间维度？**" 原文："现有 artifacts 均为 2026-09-11 至 09-18 期间的冻结快照。若蒸馏效应存在延迟显现或行为漂移，则单一时点快照可能低估或高估蒸馏信号的稳定性。" 挂：§1.1 §4.11、§3.5。锚：`C:\Users\Administrator\.minimax\v2\assets\2026\09\21\11-12-20-747-asset_20260921-111220-747_19c97b5cff3c_6cf18b87-_v4_theme_reply_doubao_2026_09_20_v1.0.md`（SHA-12 `19C97B5CFF3C`）§结尾 (d) L83；8,070 B。
- **§2.8.b** 豆包工作 brainstorm 提出 24 条新种子（均不带 `orig-asset` 标注，纯猜测或重拟合假设）。前两类为"词表分布在温度缩放下的不变性残留"与"教师侧系统性认知噪声注入作为可控反蒸馏机制"。挂：§1.1 §4.7（Dimension 6 in-scope 讨论相邻）。锚：`C:\Users\Administrator\.minimax\v2\assets\2026\09\21\11-12-20-766-asset_20260921-111220-766_a18e58c8e2a3_bdb4bc12-_v4_theme_brainstorm_doubao_2026_09_21_v1.0.md`（SHA-12 `A18E58C8E2A3`）§一 想法 1–2 L13–L17；19,389 B。

### §2.9 署名 `an invited reader team (multi-agent)`（PI 拍板 P2 已拍板：唯一归属 GLM（2026-09-21）；磁盘署名如实并存）

756 + 761 联合件；v1.1 按 PI 拍板 P2 唯一归属 GLM；磁盘署名原文 `From: an invited reader team (multi-agent)` 在 §2.9 / §4.1 并存记录，不删除。

- **§2.9.a** 提议加入邀请函 §4 的开放问题："the referent of **'output-distribution baseline'** — four of five `by_model/` slots store in-repo artifact hashes or indices rather than model-output text, and the only text-bearing slot contains 0–7 character answers; whether a teacher baseline means text or artifact bytes is a ruling the PI can make now." 挂：§1.1 §4.5、§3.5、§3.4。锚：`C:\Users\Administrator\.minimax\v2\assets\2026\09\21\11-12-20-756-asset_20260921-111220-756_c78cfb42e33d_e371e458-_v4_distillation_theme_reply_2026_09_20_v1.0.md`（SHA-12 `C78CFB42E33D`）Closing (d) L87；18,841 B。
- **§2.9.b** 提议"common-cause vs. direct-cause separability"作为邀请函缺失种子：给定一个学生与若干候选教师共享公开语料，哪些可观测量把"共享数据"与"蒸馏"分开，分离在多大样本量下消失。挂：§1.1 §4.5。锚：`C78CFB42E33D:87`（Closing (c) 段）。

### §2.10 codex（D1 review + brainstorm 已落盘 results/，PI 拍板 P3，2026-09-21）

v1.1 按 PI 拍板 P3：codex 两件从附件副本升级为 `results/` 副本：

- `results/_v4_d1_review_codex_2026_09_20.md`（`48387412B109`，4,506 B，46 行，与附件 778 同字节）；
- `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md`（`0FF6C042B845`，9,048 B，39 行，与附件 782 同字节）。

落地动作为 worker 字节级复制（详见 §7 / 整合稿 §6.5.1）。

- **§2.10.a** codex D1 review 提出 Track 3 "black-box extractor threat model" 的 utility / resistance / cost 三项作为 V4 防御侧的可验证基线。该提议在邀请函 v1.0（theme-first, framework-free）框架下并非邀请函已宣告的格式——codex 承认这是"proposal, not a commitment or a request to modify frozen inputs"。挂：§1.2 §7.12（framework-free 原则）、§1.1 §4.7（Dimension 4 / Dimension 5 in-scope 讨论相邻）。锚：`results/_v4_d1_review_codex_2026_09_20.md`（SHA-12 `48387412B109`）§Suggested Track 3 definition L23–L31；4,506 B。
- **§2.10.b** codex brainstorm 提议"Serialization as an information bottleneck"（file summary L61）与"Formatting invariants versus model fingerprints"（file summary L63）——两者均挂在 §3.5（资产覆盖缺口）与 §3.6（邀请函数字内部矛盾）的载体上。锚：`results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md`（SHA-12 `0FF6C042B845`）§1 + §3；9,048 B。

---

## §3 结构性决策点（不来自单一参与方；多方回函交叉后浮现、必须 PI 表态的分歧）

本节每条决策点把可选路径**并列**列出；PI 选哪条、不选哪条、是否选新条均属 PI 自由。每条不得出现"建议选"/"推荐"/"应当选"措辞。

### §3.1 铁律边界（no_llm / no_proxy / no_gateway / no_key 落盘 / no 18 frozen 触动 / no P-G v0+v01 触动 / no plugin spec 触动）

**决策点**：邀请函与各回函均默认沿用 deposon 8-agent 团队的 7+9 铁律（见派工单 §3）。本条要让 PI 决定的是：V4 这一轮"主题重建"是否在以下任一维度打破既有铁律？

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**保持 7+9 铁律全开**，V4 的所有工作（包括本问卷）继续约束为 read-only against 18 frozen / schema v1 / verifier / / P-G v0+v01 / plugin spec；不动 `no_llm` / `no_proxy` / `no_gateway` / `no_key 落盘`。
- **路径 B**：**放开 `no_llm`**——把 V4 重述为"教师侧可提取性研究"，允许调用外部 LLM 来生成被蒸馏的代理学生输出（proxy student）以补足 §3.2 "无学生侧"缺口。其它铁律保留。
- **路径 C**：**放开 `no_proxy`**——允许在 V4 资产外构造任何额外的反向代理集合（同样为补 §3.2 缺口）。其它铁律保留。
- **路径 D**：**放开 `no_gateway`**——允许调用任何模型网关（如 coze / GLM / KIMI / Claude Code 等）作为学生侧生成器。其它铁律保留。
- **路径 E**：**把 V4 重述为"教师侧可提取性研究"**——明文承认 V4 不试图回答任何学生侧问题；与 §3.2 "无学生侧"问题的处理是同一枚硬币的两面。其它铁律保留。
- **路径 F**：PI 自定义路径。

**盘上锚**：

- 派工单 §3（"7 铁律 / 9 铁律"原文）：本任务的输入文件第 5 段。
- 邀请函 §6.2 L317–L322（"No LLM API was called … No external URL was fetched … No proprietary prompt, model endpoint, API key, or token appears in this document."）：`3D9F73519F6C:317–322`。
- coze 主题回复 §0（AI-use disclosure）："未调用任何外部 LLM API，未抓取任何外部 URL"：`00593014CBD3:9`。
- Claude Code 主题回复 §0 AI-use disclosure：`D39CB17B051B:1`（"Sections §5.6, §5.10 and §5.5 also required *executing* repository code read-only"）。
- Trae code 主题回复 §0 AI-use disclosure：`E87EC8F7E2FE:7–11`。
- Mavis 主题回复 v1.2 §0 AI-use disclosure：`3ECF5B38048E:10–12`。

**未定项**：PI 是否在 §3.1 给出任意一条路径之前，先在 §1.2 §7.6 / §7.8 / §7.12 / §7.16 各项上作相应裁定？本节留待 PI 在 §5 作答表中决定与 §1 / §2 的勾连。

### §3.2 「无学生侧」问题（盘上只有教师侧、没有任何对象是学生，而铁律禁止造一个）

**决策点**：邀请函 §2.10 L120、§0.2 L26、§3.1 多个种子、§4.5 多个开放问题、§7.16 多个回函均指出 V1–V3 资产栈不含任何学生侧（student-side）样本。这是 V4 主题重建的最大单一缺口。本条要让 PI 决定的是：在不违反 §3.1 铁律的前提下，盘上"无学生侧"这一事实对 V4 主题意味着什么？

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**严格不构造 proxy student**——V4 主题严格限定在教师侧可观察量；"无学生侧"是 V4 的硬约束，不试图补足。
- **路径 B**：**构造 proxy student 输出集合**——在 §3.1 路径 B / C / D 已放开的前提下，由派工 worker 生成有限个 proxy student 输出并落盘到 `results/_v4_proxy_student_*`；盘上 18 frozen 与 9 网格完全不动。
- **路径 C**：**把问题限定在教师侧**——明示 V4 只回答"教师侧可观察量如何用作蒸馏检测特征"；不回答"该特征是否真能区分蒸馏与独立训练"。S-15、S-36 等种子因此只产出教师侧描述统计。
- **路径 D**：**承认 GT 不可得**——S-36（GT 困境）作为 V4 的根本边界被锁定为不可越；任何种子凡需学生侧 GT 的，均标 `[no on-disk artifact]` + `[no in-scope proxy]`。
- **路径 E**：PI 自定义路径。

**盘上锚**：

- 邀请函 §0.2 L26："V1–V3 has zero distillation, reverse-distillation, or anti-distillation experiments on disk."：`3D9F73519F6C:26`。
- 邀请函 §2.10 L120："No V1–V3 distillation, reverse-distillation, or anti-distillation experiment asset exists on disk."：`3D9F73519F6C:120`。
- 邀请函 §3.7 S-36（GT 困境）："who labels the GT for distillation detection — the teacher themselves, the distiller themselves, a third-party auditor?": `3D9F73519F6C:230`。
- 邀请函 §4.5："What would a reverse-distillation claim even look like, given that deposon's artifacts are teacher-side and have no student-side ground truth?": `3D9F73519F6C:255`。
- coze N-04 "评测的参照推理本身就是某个模型的输出"（396/396 来源标签全部 `kimi_api`）：`00593014CBD3:336–346`。
- Trae code 主题回复 §5.11（KD baseline 反驳）—— 这是 §3.3 第 3 条的锚，但与本条"无学生侧"问题相邻。
- 豆包工作主题回复 §二 S-36："GT 是**不存在**的，而非不唯一"：`19C97B5CFF3C:23`。

**注**：Claude Code §5.11（见 §3.3 第 3 条）报告盘上有 KT-B1 系列 KD baseline；该 baseline 是 student-side 输出器的一个特殊形态，但其目的是"对照 deposon 失真界"，不是 V4 的学生侧样本。本条决策点对该 baseline 是否被视为 V4 主题内可用学生侧素材，**留 PI 在 §5 表的勾连栏中决定**。

### §3.3 邀请函 §0.2 「V1–V3 零蒸馏实验」与盘上 KT-B1 系列文档之间的抵触

**决策点**：邀请函 §0.2 L26 把"V1–V3 has zero distillation experiments on disk"作为该邀请函要求每位读者内化的"single most important on-disk fact"。Claude Code 主题回复 §5.11 报告该命题被盘上 KT-B1 系列文档反驳——`docs/V3X/KT_B1_SPEC_V0.1.md:267-274` 含 BOSS-B2 Hinton-2015 KD 测法，`verifier/handoff/KT_ABC1_anchors_sha256_12.json:157-161` 把同一脚本注册到 KT-B1 锚组，`docs/V3X/BOSS_SELFTEST_PHASE_B_2026_09_09.md:33` 记录首次执行失败（`TypeError`），`docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md:83` 记录 GRAY_BOTH_BELOW 失真上界 0.0028。

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**维持邀请函 §0.2 L26 原文**，由 PI 在 v1.x 后续版本对"zero distillation experiments"加限定语（如 Claude Code 提议的："V1–V3 contains one generic knowledge-distillation baseline, run as a BOSS adversary against a placeholder deposon bound and adjudicated GRAY, and no experiment in which a deposon artifact is the teacher or the student."）。
- **路径 B**：**承认盘上确有 KT-B1 KD baseline**，邀请函 v1.x 后续版本重写 §0.2 L26 为新句子（不指定新句子文本，留 PI 在 §5 表的作答栏内写）。
- **路径 C**：**把 KT-B1 KD baseline 与 §3.2 "无学生侧"决策点合并处理**：若 §3.2 选路径 B（构造 proxy student），则 KT-B1 KD baseline 可作为先例；若 §3.2 选路径 A，则 KT-B1 KD baseline 不视为 V4 学生侧素材。
- **路径 D**：**承认抵触，冻结邀请函 v1.0 至下次有别的版本作为决策基线前**——即把 §0.2 L26 标记为"已知与 KT-B1 系列抵触；该抵触本身即为 PI 拍板项"，不动现有 v1.0 文字。
- **路径 E**：PI 自定义路径。

**盘上锚**：

- Claude Code §5.11 L362–L385："§0.2 line 26 states: 'V1–V3 has zero distillation, reverse-distillation, or anti-distillation experiments on disk.' On disk there is a pre-registered knowledge-distillation protocol, a hashed script anchor for it, a recorded execution failure, a bug fix, and a numeric result."：锚 `D39CB17B051B:362–385`。
- KT-B1 SPEC V0.1 §4.2 "BOSS-B2: Knowledge Distillation 测法"：`docs\V3X\K T_B1_SPEC_V0.1.md:267-274`（SHA-12 `0410CA0FBDAE`，449 行，35,688 B）。
- KT 锚文件 KT-B1 锚组（SHA-12 `03C6C01F3697`，6,680 B / 189 行，实测）：`verifier\handoff\KT_ABC1_anchors_sha256_12.json:157-161`。
- BOSS-B2 首次失败：`docs\V3X\BOSS_SELFTEST_PHASE_B_2026_09_09.md`（盘上文件名内含 PHASE_B 字符串，非创作层 phase 框架）:33（SHA-12 `4485443757E7`，15,478 B）。
- BOSS-B2 修复后数值：`docs\V3X\KT_B1_REWORK_REPORT_2026_09_10.md:83`（SHA-12 `BAEF94E393DE`，11,478 B / 实测 215 行）。

**【待 PI 裁定】注**：Claude Code §5.11 明确写其无法核实 `.mavis/scripts/kt_b1/boss_b2_kd.py` 当前是否在盘上："`.mavis/` returns no matches to a glob for `*.py`"。PI 在 §5 表作答时，若需引用该脚本，须由 PI 自定是否在盘上再核一次。

### §3.4 命名漂移：`KIMI-K3` / `kimi-for-coding` / `kimi-k2.7-code` / `minimax` / `M3` / `V7` / `R5` 等串在盘上并存

**决策点**：盘上多处出现以下串共存：

- KIMI：邀请函散文 `KIMI-K3`、邀请函 §6.4 占位符 `kimi-for-coding`、D7 verdict 文件 `kimi-k2.7-code`、by_model 目录名 `kimi`。
- 第五 by_model 目录：邀请函散文 `M3`、邀请函 §6.4 占位符 `minimax`、盘上目录名 `minimax`、D7 verdict 文件 `minimax-m3`、prompt pack §4 索引字面名 `minimax`。
- 终判版本：邀请函散文 `V7`、D7 verdict 文件名 `V7`、盘上最终报告 `V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md`、codex D1 review §D1 action items 第 4 项 "Verify all SHA-12 placeholders against the V3 final R5 manifest"。

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**维持邀请函 §6.4 + §7.3 + §7.4 + §7.5 的 [待 PI 裁定]**：每条由 PI 在 §1.2 各项的作答栏内分别给出（散文形态 / API 端点 / 盘上目录名 / D7 verdict 字面 / 终判版本）。
- **路径 B**：**一次性统一处理**：PI 在本条给出统一答案，覆盖 §1.2 §7.3 + §7.4 + §7.5 + §7.6 全部。
- **路径 C**：**承认命名漂移是 V4 重建的一部分**：每条命名在不同场景下保留其所在层（散文层用 `KIMI-K3`、API 层用 `kimi-for-coding`、盘上层用 `kimi-k2.7-code`）；PI 在本条批准该分层。
- **路径 D**：PI 自定义路径。

**盘上锚**：

- 邀请函 §6.4 L332–L341（占位符表 + [待 PI 裁定]）：`3D9F73519F6C:332–341`。
- 邀请函 §7.3 / §7.4 / §7.5 / §7.6：`3D9F73519F6C:352–355`。
- D7 verdict 文件 9-backbone 字面名：`results\d7_5anchor_60cells_9model_verdict_2026_09_18.json`（SHA-12 `4505CCA79C15`，2,456 B；L22–L58 P-A 表、L61–L98 P-E 表）。
- coze 主题回复 §四 "距离列与排序列都不能从该表自身复算"（涉及 `kimi-k2.7-code` 行 L141）：`00593014CBD3:118–134`。
- coze §五 "九个模型来自四份互不校准的提交"（涉及 `minimax-m3` 行 L121）：`00593014CBD3:146–152`。
- coze §三 横向事实二 "跨层命名不稳定有第三个实例"：`00593014CBD3:285–287`（GLM_2 制品 schema 名错挂 `kimi_artifact_v/1.0`）。
- kimi 主题回复 §3："我在盘上同时以三个名字出现——散文中的 KIMI-K3、§6.4 声称的端点 kimi-for-coding、D7 verdict 实载的 kimi-k2.7-code。我无法仅凭盘上材料裁定哪一个是'我'。"：`3E37352EFB4B:3`。
- codex D1 review "V3 final R5 manifest"：`48387412B109:44`。
- 豆包主题回复 §一 第 5 项："§7 未决项编号为 1–6,8,10,12,14,16（缺 7,9,11,13,15）。两处均未解释跳号原因"：`19C97B5CFF3C:13`。

### §3.5 邀请函对资产的覆盖缺口：`results/` 实有 202 条 JSON 而邀请函只引用其中一部分；`_p_l_v3_vector_embedding_*` 家族 21 个文件 / 19 JSON 一条都不在 prompt pack §4 的 31 条清单内

**决策点**：本会话实测（`Get-ChildItem -Path 'D:\私人资料\deposon-repo\results\' -Filter '*.json' | Measure-Object`）返回 202 个 JSON；邀请函 §8 资产表共 30 行（25 行有完整路径 + 字节 + SHA-12，5 行 "(see SHA-12)" 占位符），prompt pack §4 索引共 31 条；`_p_l_v3_vector_embedding_*` 家族在 `results/` 实有 21 个文件（19 个 `.json` + 2 个 `.md`），prompt pack §4 的 31 条一条都没列它。Claude Code §5.12 L391 报告 "results/ holds 202" 与 "the invitation references 14 distinct `results/*.json` paths" 之比。本条要让 PI 决定的是：V4 是否纳入 prompt pack §4 / 邀请函 §8 未列的资产？

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**保持邀请函 §8 / prompt pack §4 范围不动**——V4 在原 30+31 条清单内工作；其余 170+ 个 JSON 与 21 个 `_p_l_v3_vector_embedding_*` 文件视为 V4 不引用。
- **路径 B**：**把 `_p_l_v3_vector_embedding_*` 家族 21 个文件全部纳入邀请函 §8**——v1.x 后续版本扩表；本问卷作答完毕后再决定邀请函升版。
- **路径 C**：**把 `_p_l_v3_vector_embedding_*` 家族作 V4 主题的"对照组"**——它在 prompt pack §4 的 31 条之外，但其跨厂商跨口径样本可作 §3.5 已知缺口的对照基线；PI 决定该家族是否升级为邀请函主资产。
- **路径 D**：**PI 在本条给出清单**：哪些原本被忽略的 JSON / MD 进入 V4；哪些不进。
- **路径 E**：PI 自定义路径。

**盘上锚**：

- `Get-ChildItem -Path 'D:\私人资料\deposon-repo\results\' -Filter '*.json' | Measure-Object` 返回 202（派工单 §2.5 派给本任务的"派单 5 件"实测数字）。
- `Get-ChildItem -Path 'D:\私人资料\deposon-repo\results\' -Filter '_p_l_v3_vector_embedding_*'` 返回 21 个文件（19 `.json` + 2 `.md`）。
- 邀请函 §8 L368–L401（30 行资产表）：`3D9F73519F6C:368–401`。
- prompt pack §4（31 条索引）：`results\_v4_distillation_prompt_pack_2026_09_20_v1.0.md:30–60`（具体行号可未抽查，已用派工单"§2.5"实测）。
- Claude Code §5.12 L391："The invitation references 14 distinct `results/*.json` paths. `results/` holds 202. That ratio is not an accusation — the invitation is theme-first and deliberately does not inventory the program — but it is the reason ideas 5.1 through 5.4 were available to an outside reader at all"：`D39CB17B051B:391`。
- coze 主题回复 §二 S-38 "同一口径重跑，七到八成载荷变了"（`_p_l_v3_vector_embedding_*` 4 对同口径实测）：`00593014CBD3:260–276`。

### §3.6 邀请函数字内部矛盾（同一会话内字节数不一致、编号跳号、`~600 edges/anchors` 无明细）

**决策点**：本工作实盘以上邀请函与 prompt pack 文件的字节数、行数与 SHA-12 时，记录到以下不一致：

- 邀请函 §2.2 L66 写 8,674 B vs §8 L383 写 8,753 B（`boss_pa_1_rbr_rm_result_2026_09_15.json`，盘上 8,753 B）。
- 邀请函 §4 编号 1, 3, 4, 5, 7, 9, 11（缺 2, 6, 8, 10, 12）。
- 邀请函 §7 编号 1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16（缺 7, 9, 11, 13, 15）。
- 邀请函 §0.2 L127 "`~600 edges/anchors`" 与 §3.2 S-11 L168 列出的 18 frozen anchors + 22 caption entries + 5 KT anchors = 45 数字差一个数量级。
- 行数双口径（**PI 拍板 P6，2026-09-21**：canonical = `ReadAllLines` UTF8；早前 `Get-Content` 不指定 `-Encoding` 的 636 / 277 行数作废）：邀请函 411 行 / 384 / 294 / 436 全部为 `ReadAllLines` UTF8 口径。
- D7 verdict 文件名 `2026_09_18` 与文件内时间戳 `2026-09-16T11:00`（L2）不一致。
- V3 summary 第 10 行 / 第 336 行写 "P-A: 37047 bytes, SHA-12 待算" 与盘上 38,545 B / SHA-12 `4A08521F8DE1` 不一致（Trae work v1.2 第 29 行报告）。
- V3 summary 同文件 L47–L49 (`60_cells_total_passed: 51`, `pass_rate_60: 0.85`) 与 L62 (`merged_60_cells: {T_count: 52, R_count: 7, A_count: 1, T_frac: 0.8667, …}`) 两处都挂在"V2 60 cells"名下，数字不一致（51 vs 52 / 0.85 vs 0.8667）。

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**承认 §0.2 L26 与 KT-B1 系列抵触，修正邀请函原文**——在 v1.x 后续版本改正 §2.2 L66 与 §0.2 L26。
- **路径 B**：**承认 §2.2 L66 笔误，§8 L383 为准**——与 §3.1 路径 A 一致，不动其它。
- **路径 C**：**承认编号跳号是编辑选择**——PI 在本条表态是否在跳号处插条目、保持跳号、或在 §5 表的作答栏内指定每个新数字。
- **路径 D**：**承认 `~600 edges/anchors` 是估算**——v1.x 后续版本给出明细（仍可写 `~600`，但需附"明细见 §X"），或改正数字。
- **路径 E**：**以 `ReadAllLines` UTF8 行数（PI 拍板 P6）为权威**——邀请函、prompt pack、seeds、v0.2 都不改行数；v1.x 后续版本用 `ReadAllLines` UTF8 行数（411 / 384 / 294 / 436）。
- **路径 F**：**以 `Get-Content | Measure-Object -Line` 不指定 `-Encoding` 行数为权威**——同上，但 PI 此前未排除 F，故 v1.x 后续版本可裁择。
- **路径 G**：**双口径并列保留**——邀请函 v1.x 后续版本在文件首页同时给出两口径行数；PI 在本条批准。
- **路径 H**：**V3 summary 51 vs 52 / 0.85 vs 0.8667 不一致**：PI 在 §5 表作答栏内指明 P-A 的"V2 60 cells"应取 51 / 0.85 还是 52 / 0.8667。
- **路径 I**：PI 自定义路径。

**盘上锚**：

- 邀请函 §2.2 L66（"8,674 bytes"）vs §8 L383（"8,753"）：`3D9F73519F6C:66, 383`。
- 邀请函 §0.2 L127（"`~600 edges/anchors`"）vs §3.2 S-11 L168（"18 + 22 + 5"）：`3D9F73519F6C:127, 168`。
- 邀请函 §4 跳号：`3D9F73519F6C:252–258`。
- 邀请函 §7 跳号：`3D9F73519F6C:350–360`。
- D7 verdict 文件名 `2026_09_18` vs 内 L2 `2026-09-16T11:00`：kimi 主题回复 §一 第 3 项 L15。
- V3 summary 第 10 / 336 行 "37047 / 待算" vs 盘上 38,545 / `4A08521F8DE1`：Trae work v1.2 §Where the Invitation Departures from Disk 第 6 项 L29：`6BEE6EC434BD:29`。
- V3 summary 51 vs 52：coze 主题回复 §二 S-06 第 2 段 L51–L53：`00593014CBD3:51–53`。

### §3.7 公开表与程序不符（`docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` 的表与产生它的脚本不可能对应）

**决策点**：`docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md`（19,751 B，SHA-12 `977FE1B48F75`）第 143–147 行打印的参考表第一行 `L_algorithm_process | 199 | 1 | 32 | 6.2188 | 0.0312` 与 `results/boss_pa_1_rbr_rm_result_2026_09_15.json` 同一图给出的 `200 | 6 | 200` 不符（Claude Code §5.6 L294）。RM iteration count of 1 和 Bayes count of 32 是该脚本（`deposon_team/plugins/boss_pa_1_rbr_rm.py`）不能发射的值。

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**承认公开表与程序不符**——v1.x 后续版本改正 P_A_D1_D3_REPORT 的 143–147 表，或改正 JSON 中的 row。
- **路径 B**：**冻结 P_A_D1_D3_REPORT**——不改正，但邀请函 v1.x 后续版本在 §X 增加 §3.7 同型 footnote。
- **路径 C**：**作为 V4 前置修正项**——V4 不引用 `P_A_D1_D3_REPORT` 的 143–147 表，直到该表与 JSON 之一被修。
- **路径 D**：PI 自定义路径。

**盘上锚**：

- P_A_D1_D3_REPORT 路径 / 字节 / SHA-12：`docs\V3X\P_A_D1_D3_REPORT_2026_09_15.md`，19,751 B，`977FE1B48F75`，268 行。
- Claude Code §5.6 L288–L296（含 verbatim 引文 "An RM iteration count of 1 and a Bayes count of 32 are values this code cannot emit — my sweep shows RM is identically 6 and Bayes is confined to {1, 200}. The published reference table was not produced by this script."）：`D39CB17B051B:288–296`。
- `results/boss_pa_1_rbr_rm_result_2026_09_15.json`（8,753 B，SHA-12 `C7C59E0D2F6C`）的 `boss_pa1_22graph_simulation` 块（22 graph rows）：`results\boss_pa_1_rbr_rm_result_2026_09_15.json:37–337`。

### §3.8 已坐实不稳健的读数（simulate_rm 恒同值、bayesian_nash_iter 名为迭代实为二值返回、rbr_mult 只取三值、22 条映射到 6 个 12-bit 码且 62/231 对汉明距离为 0、双曲 transport 保距宣称与实测偏差、`conservation_residual` 实为球内含性检查）——V4 是否先处理，还是原样带过

**决策点**：盘上以下读数已在 Claude Code §5.6 / §5.9 / §5.10 与 Mavis / Trae code 等回函中**坐实不稳健**：

- `simulate_rm` 在 22 graph × 20,000 sweep 中恒返回 6；`simulate_rbr` 在 22 graph × 20,000 sweep 中 20 个图返回 200、2 个图返回 2（少数 1）；`bayesian_nash_iter` 名为迭代实为 `return 1 if nash else 200`；`rbr_mult` 跨 22 图只取 3 个值（200.0 ×16 / 1.0 ×4 / 2.0 ×2）。
- `results/deposon_v2_phase4_f4_2026_09_11.json`（盘上文件名内含 phase4 字符串，非创作层 phase 框架；5,212 B，SHA-12 `CF7682348617`）22 概念项 → 6 个 12-bit LSH 码（分布 10/6/2/2/1/1）；231 对中 62 对汉明距离为 0；平均 1.961（独立应是 6.0）。
- 双曲 transport 在 2000 个随机点对上 `max |d_H(Tx1,Tx2) − d_H(x1,x2)| = 0.18869`；`POINCARE_C = 1.0` 在 `deposon_team/plugins/_pg_v01_compute.py:55` 后再无引用，模块内**无任何函数取曲率参数**。
- `conservation_residual` 在 `deposon_team/plugins/_pg_v01_compute.py:194` 实际定义为 `abs(min(1-1e-9, ||x_T||) − min(1-1e-9, ||x||))`——球内含性检查，注释 "验证 transport 不破坏 ball 约束"，与 V3 守恒律同名但定义不同。
- `results/deposon_dpath_cross_modal_2026_09_10.json`（75,964 B，SHA-12 `AB0C2EAFF0D1`）L9 列 22 个图路径（`figures/v3x/corpus_pngs/graph_001.png … graph_022.png`）；**本机核实 `figures/v3x/corpus_pngs/` 目录存在但文件数为 0**，盘上 `*.png` 总数为 0。

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**V4 先处理**：在 v1.x 后续版本或 V4 启动前改正以上 5 条读数；不改正则 V4 不得引用。
- **路径 B**：**V4 原样带过**：把以上 5 条作为"V1–V3 不稳健读数史"明示写进 v1.x 邀请函 §2 或 §X，但不动其 JSON。
- **路径 C**：**把 5 条分两类**：simulate_rm / rbr_mult / bayesian_nash_iter / LSH 汉明 / 双曲 transport 归"程序不稳健"（代码可修）；`conservation_residual` 字段名冲突、corpus_pngs 缺失归"档案管理不稳健"（V4 不必修）。
- **路径 D**：**V4 不引用**：所有 5 条读数在 V4 的引用清单一律标 `[no on-disk calibrated finding]`。
- **路径 E**：PI 自定义路径。

**盘上锚**：

- `simulate_rm` / `simulate_rbr` / `bayesian_nash_iter` / `rbr_mult`：Claude Code §5.6 L286–L296：`D39CB17B051B:286–296`；`deposon_team/plugins/boss_pa_1_rbr_rm.py`（行号在 §5.6 引用为 181–189）。
- 22 → 6 码 / 62/231 汉明 0：Claude Code §5.9 L331–L340：`D39CB17B051B:331–340`；`results/deposon_v2_phase4_f4_2026_09_11.json`（盘上文件名内含 phase4 字符串，非创作层 phase 框架；SHA-12 `CF7682348617`）line-level：coze §5.9 L334 段落。
- 双曲 transport 不保距 / `POINCARE_C = 1.0` 无引用：Claude Code §5.10 L342–L358：`D39CB17B051B:342–358`；`deposon_team/plugins/_pg_v01_compute.py:55, 114–121`。
- `conservation_residual` 实为球内含性：Claude Code §5.10 L356：`D39CB17B051B:356`；`_pg_v01_compute.py:194`。
- `corpus_pngs/` 目录存在但文件数为 0：coze 主题回复 §3 N-05 L355：`00593014CBD3:355`。

### §3.9 引用形态：盘上原话与二手转述混用时的引用纪律（邀请函与各方回函对同一资产的转述互相不一致时以谁为准）

**决策点**：本会话收集到的 12+ 份回函与邀请函对同一资产（如 `boss_pa_1_rbr_rm_result_2026_09_15.json`、`deposon_v3_v7_summary_2026_09_11.json`、`strip_captions_22.json`、`KT_ABC1_anchors_sha256_12.json`、`corpus/v20/by_model/` 五件）的转述出现以下不一致：

- 字节数不一致：邀请函 §2.2 L66 vs §8 L383（见 §3.6）。
- 字节数不一致：V3 summary 第 10 行 vs 盘上（见 §3.6）。
- "5 KT-ABC1 anchors" vs "15 KT-ABC1 anchors" vs "18 frozen anchors"（邀请函 §2.6 L93、S-11 L168、coze §一 S-11 L65、Claude Code §1.7 L54–L62、kimi §一 第 4 项 L16）。
- "21 caption-fingerprint pairs" vs "22 captions" vs "22 entries"（邀请函 §2.6 L96、§6.4 L338、§7.2 L351、coze §一 S-11 L63、kimi §一 第 6 项 L18）。
- "5 vendor / 5 artifact" vs "4 vendor lineage / 5 artifact"（邀请函 §2.1 L52 + §8 L372–376、§7.1 L350、coze §二 S-03 §二 S-17 L39、trae code §S-17 L43、workbuddy part 1 C4 L39–L49、Mavis §3.1 S-03 L56、L60）。
- "540 cells 是 evaluation" vs "540 cells 是 conservation check"（邀请函 §2.2 L66 vs Claude Code §1.3 L30–L34、workbuddy part 1 C2 L33）。
- "9 models" 命名在不同文件中以 `9model_complete` / `worker_a` / `worker_b` / `worker_c` / `worker_d` / `minimax-m3_standalone` 6 种 source 字段出现（coze §四 第 5 项 L148）。
- `coze` 与 `minimax` 跨层命名（coze §三 横向事实二 L286–L287）。
- 邀请函 §8 表 8 行 "(see SHA-12)" 占位符（Claude Code §1.8 L68）。**v1.1 §7 / 整合稿 §6.5.2 已给出 worker 实测的 8 行补全表（7 个 PI 给定串全部命中 + 第 8 行由 worker 独立补 SHA-12 `0EB1CFAA2992`）**。

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A**：**邀请函 §8 资产表为唯一权威**：回函方与本问卷凡引用与 §8 不符的，标 `(cross-ref §8, see SHA-12)`；PI 在 §5 表的作答栏内给出 §8 表 8 行空白的具体值。**v1.1 注**：组 B worker 已实测给出 8 行 SHA-12（详见 §7 / 整合稿 §6.5.2）。
- **路径 B**：**回函方各自独立 SHA-12 重算为补充权威**：每位读者重算 SHA-12 + 字节 + 行数；邀请函 §8 与回函方一致即引用，否则以重算为准。
- **路径 C**：**双口径并列**：邀请函 §8 不动；每个引用以 `path + §8 表行号 + 实际 SHA-12（实测） + 行号` 四要素给出。
- **路径 D**：**冻结 §8 表为 read-only**：v1.x 后续版本不改 §8 表内任何行；空白的 8 行由 PI 在本条作答栏一次性补完。**v1.1 注**：整合稿 §6.5.2 已给出完整 8 行补全表，供 PI 一次性采纳。
- **路径 E**：PI 自定义路径。

**盘上锚**：

- 邀请函 §8 L368–L401（30 行表，5 行 "(see SHA-12)"）：`3D9F73519F6C:368–401`。**v1.1 注**：5 行之外的另外 3 行（即 8 行占位）由组 B 实测已补全，整合稿 §6.5.2。
- 邀请函 §8 L394–L401 8 行 `(see SHA-12)` 占位：`3D9F73519F6C:394–401`。
- Claude Code §1.8 L68（"Eight rows in §8 are left as '(see SHA-12)' placeholders. Filling them is not my call, but the values are: ..."）：`D39CB17B051B:68`。
- Claude Code §1.7 L54–L62（"18 frozen" 与 "15 anchors" 与 "16 anchors" 三套术语）：`D39CB17B051B:54–L62`。
- Mavis §2.3 L42–L46（"boss_pa_1 byte-count contradiction"）：`3ECF5B38048E:42–46`。
- coze §一 "性质标签的取值域不闭合" L21–L33：`00593014CBD3:21–33`。
- coze §三 横向事实二 L286–L287（跨层命名第三个实例）：`00593014CBD3:286–287`。

---

## §4 归属与档案决策点

### §4.1 归属未定项（756 / 761）— PI 拍板 P2（2026-09-21）：唯一归属 GLM

**决策点**：附件侧有两份文件署名 `an invited reader team (multi-agent)`，文件名无厂商：

- 756：`C:\Users\Administrator\.minimax\v2\assets\2026\09\21\11-12-20-756-asset_20260921-111220-756_c78cfb42e33d_e371e458-_v4_distillation_theme_reply_2026_09_20_v1.0.md`，18,841 B，SHA-12 `C78CFB42E33D`，89 行（PowerShell `ReadAllLines` UTF8）。
- 761：`C:\Users\Administrator\.minimax\v2\assets\2026\09\21\11-12-20-761-asset_20260921-111220-761_8295c3201f20_ee5ad31d-_v4_distillation_theme_reply_addendum_2026_09_20_v1.0.md`，14,153 B，SHA-12 `8295C3201F20`，91 行（PowerShell `ReadAllLines` UTF8）。

761 是 756 的 addendum（self-stated "Same drafting agent, same channel per §5.4"）。两份均无厂商署名。派工单 §2.3 标其为「**归属未定**」。

**v1.1 PI 拍板 P2**：756 / 761 唯一归属 GLM（PI 拍板 P2：「唯一归属 = GLM」）；磁盘署名 `an invited reader team (multi-agent)` 原文保留（如实并存）。

**并列可选路径**（PI 任选其一、不选、并列、提新路径）：

- **路径 A（PI 拍板）**：**已拍板 (2026-09-21)：唯一归属 GLM**——756 / 761 归属 GLM；磁盘署名 `an invited reader team (multi-agent)` 原文保留；如实在盘（as-on-disk）记录两件。v1.1 整合稿 §0.3 / §0.6 / §4.12 / §4.13 / §6.1 已同步。
- **路径 B**：**归到 §2.7（kimi）**——把两份并入 kimi 主题回函簇（与 `_kimi_v4_theme_reply_*.md` 同期）。**v1.1 注**：与 PI 拍板 P2 抵触。
- **路径 C**：**归到 §2.4（Claude Code）**——把两份并入 Claude Code 主题回函簇（与 `_v4_distillation_reply_claude_code_2026_09_20.md` 同期）。**v1.1 注**：与 PI 拍板 P2 抵触。
- **路径 D**：**归到 §2.5（coze）**——把两份并入 coze 主题回函簇（与 `_v4_distillation_reply_coze_2026_09_20.md` 同期）。**v1.1 注**：与 PI 拍板 P2 抵触。
- **路径 E**：**PI 给出新归属**（PI 在 §5 表的作答栏内写出具体厂商 / 团队名）。**v1.1 注**：与 PI 拍板 P2 抵触；PI 在 P2 后续回合可改。
- **路径 F**：**两份作废不引用**：本问卷与任何 v1.x 后续版本不引用 756 / 761；§2.9 两条提议作废。**v1.1 注**：与 PI 拍板 P2 抵触。

**盘上锚**：

- 756 路径 / 字节 / SHA-12：`C:\Users\Administrator\.minimax\v2\assets\2026\09\21\11-12-20-756-asset_20260921-111220-756_c78cfb42e33d_e371e458-_v4_distillation_theme_reply_2026_09_20_v1.0.md`，18,841 B，`C78CFB42E33D`，89 行。
- 761 路径 / 字节 / SHA-12：同目录 `11-12-20-761-asset_...md`，14,153 B，`8295C3201F20`，91 行。
- 761 文件第 3 行："Assembled by the same drafting agent from four parallel brainstorm files by our LLM multi-agent team"（指 756 + 761 是同一团队，但团队名仅为 `an invited reader team (multi-agent)`）。
- 派工单 §2.3 第 6 项："归属未定（署名 `an invited reader team (multi-agent)`，文件名无厂商）"。
- **v1.1 PI 拍板 P2 落点**：「747 / 766 为豆包工作，756 / 761 要么 GLM 要么 workbuddy 要么豆包工作的 agent 团队模式成果」（首轮 Q2），「唯一归属 = GLM」（次轮 Q1）。

### §4.2 coze 件 results 与附件同哈希该引哪个 — PI 拍板 P3（2026-09-21）：引用统一取 results/

**决策点**：派工单 §2.2 第 11 项标 coze 件为 `D:\私人资料\deposon-repo\results\_v4_distillation_reply_coze_2026_09_20.md`，71,084 B，SHA-12 `00593014CBD3`，459 行。派工单 §2.3 也列了 coze 件的附件副本 `11-12-20-773-asset_..._00593014cbd3_...md`（与 results/ 同哈希 / 同字节）。

**v1.1 PI 拍板 P3**：codex 778/782 复制落盘 results/ 后引用（已执行）；coze 件 results/ 与附件同哈希（00593014CBD3），引用统一取 results/ 件。

**并列可选路径**：

- **路径 A（PI 拍板）**：**已拍板 (2026-09-21)：只引 `results/` 副本（统一取 results/）**——`results/_v4_distillation_reply_coze_2026_09_20.md` (SHA-12 `00593014CBD3`) 为唯一权威；附件副本（`11-12-20-773-...md`）仅作 SHA-12 / 字节对齐证据保留。v1.1 整合稿 §0.3 / §7.3 已同步。
- **路径 B**：**只引附件副本**——`results/` 副本冻结；V4 后续引用走附件。**v1.1 注**：与 PI 拍板 P3 抵触。
- **路径 C**：**两副本并列**——引用时给 `results/path + 附件/path` 双路径；PI 决定主路径。**v1.1 注**：与 PI 拍板 P3 抵触。
- **路径 D**：PI 自定义路径。

**盘上锚**：

- results/ 副本：`D:\私人资料\deposon-repo\results\_v4_distillation_reply_coze_2026_09_20.md`，71,084 B，SHA-12 `00593014CBD3`。
- 附件副本（SHA-12 同 `00593014CBD3`）：`C:\Users\Administrator\.minimax\v2\assets\2026\09\21\11-12-20-773-asset_20260921-111220-773_00593014cbd3_80c74bcd-_v4_distillation_reply_coze_2026_09_20.md`。

### §4.3 codex / 豆包 / 未定件（756 / 761）仅有附件副本、是否要落盘到 results/ — PI 拍板 P3（2026-09-21）：codex 已落盘 / 豆包维持 / 756/761 维持附件

**决策点**：以下 5 份文件 PI 拍板 P3 的落点（v1.1 落地实况）：

| 件 | v1.0 状态 | v1.1 PI 拍板 P3 后状态 |
|---|---|---|
| codex D1 review | 仅在附件（`11-12-20-778-...md`） | 已落盘到 `results/_v4_d1_review_codex_2026_09_20.md`，与附件同字节 (`48387412B109`, 4,506 B, 46 行) |
| codex brainstorm | 仅在附件（`11-12-20-782-...md`） | 已落盘到 `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md`，与附件同字节 (`0FF6C042B845`, 9,048 B, 39 行) |
| 豆包工作 `747` | 仅在附件 | 维持仅在附件（PI 拍板未要求落盘） |
| 豆包工作 `766` | 仅在附件 | 维持仅在附件（PI 拍板未要求落盘） |
| 未定件 `756` / `761` | 仅在附件（已拍板 P2 唯一归属 GLM） | 维持仅在附件（PI 拍板 P3 未要求落盘） |

**并列可选路径**：

- **路径 A（PI 拍板 P3）**：**codex 已落盘（动作为 worker 字节级复制 identical，详见 §7 / 整合稿 §6.5.1）；其余四份维持原状**。v1.1 整合稿 §0.2 / §0.5 / §4.10 / §4.11 已同步。
- **路径 B**：**保持只在附件侧**——本任务不写盘到 results/，仅以附件侧为引用源；**v1.1 注**：与 PI 拍板 P3 已落盘 codex 两件的现实抵触（v1.0 时未落盘；v1.1 已落盘）。
- **路径 C**：**部分落盘**——PI 在 §5 表的作答栏内逐件决定。**v1.1 注**：与 PI 拍板 P3 部分抵触；PI 后续回合可指定其它批次。
- **路径 D**：**全部作废**——5 份附件副本不引用。
- **路径 E**：PI 自定义路径。

**盘上锚**：

- 派工单 §2.3 第 1–5 项（5 份附件）。
- 5 份附件实测哈希 / 字节 / 行数（见上）。
- 已落盘 codex 两件：`results/_v4_d1_review_codex_2026_09_20.md` + `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md`（worker 实测字节级复制 identical；详见 §7 / 整合稿 §6.5.1）。

### §4.4 邀请函 §8 表 8 行 "(see SHA-12)" 占位符由谁补全 — 组 B worker 已实测补全

**决策点**：邀请函 §8 L394–L401 共 8 行写 `(see SHA-12)` 占位符（`_v4_brainstorm_seeds_2026_09_20.md` 等 8 处）。Claude Code §1.8 L68 报告其建议值（PI 给定的 7 个 SHA-12，见下）。

**v1.1 组 B 复算结论**（PI 拍板 P4 + worker 实测）：

| 行号 | 文件名 | PI 给定 SHA-12 | worker 实测命中 |
|---|---|---|---|
| L394 | `_v4_brainstorm_seeds_2026_09_20.md` | （未给出；非 PI 7 串） | `0EB1CFAA2992`（worker 独立补 SHA-12；14,994 B / 294 行） |
| L395 | `_v4_experiment_invitation_2026_09_20_v0.2.md` | `8E1E7434905D` | `8E1E7434905D`（41,680 B / 470 行） |
| L396 | `_kimi_v4_t12_review_2026_09_20.md` | `38070FD12F31` | `38070FD12F31`（6,644 B / 80 行） |
| L397 | `_v4_acceptance_coze_2026_09_20.md` | `B2BF2A073AC8` | `B2BF2A073AC8`（5,467 B / 70 行） |
| L398 | `_v4_acceptance_trae_code_2026_09_20.md` | `3205593030BC` | `3205593030BC`（6,301 B / 86 行） |
| L399 | `_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | `D3BDFC99FCDC` | `D3BDFC99FCDC`（11,877 B / 102 行） |
| L400 | `_v4_d1_response_workbuddy_2026_09_20.md` | `BC663B671994` | `BC663B671994`（14,881 B / 158 行） |
| L401 | `_v4_review_claude_code_2026_09_20.md` | `B6F9956BCF5C` | `B6F9956BCF5C`（7,004 B / 55 行） |

**关键事实**：7 个 PI 给定 SHA-12 **均不出现在邀请函正文内**（ripgrep + PowerShell 双通道大小写不敏感 0 命中）；§8 表 L394–L401 共 8 行实为 `(see SHA-12)` 占位符。7 个串是会话内 PI 提供的文件外宣称对应关系。worker 全 `results/` 递归扫描（排除 `_archive_2026_09_20`，0 Get-FileHash 失败）实测全部命中。

**并列可选路径**：

- **路径 A（v1.1 worker 路径）**：**组 B 补全表为权威**——8 行 SHA-12 一次性采纳：第 1 行 worker 独立补 `0EB1CFAA2992`、第 2-8 行采纳 PI 给定 7 串；PI 后续回合可在 §5 表填入接受 / 不接受。
- **路径 B**：**PI 在 §5 表的作答栏内逐行给出**——PI 不采信组 B 补全表，自行核盘后写入。
- **路径 C**：**8 行占位符保持空白**——v1.x 后续版本在 §8 表头加注 "8 rows withheld pending PI ruling"；PI 在本条作答栏决定是否补完。
- **路径 D**：PI 自定义路径。

**盘上锚**：

- 邀请函 §8 L394–L401（8 行占位符）：`3D9F73519F6C:394–401`。
- Claude Code §1.8 L68 报告的 7 SHA-12（PI 给定）；`D39CB17B051B:68`。
- 实测：`_v4_brainstorm_seeds_2026_09_20.md` 14,994 / `0EB1CFAA2992` / 294 行（PowerShell + `ReadAllLines` UTF8；v1.1 worker 实测确认）。
- v1.1 整合稿 §6.5.2 给出完整 8 行补全表 + 标签说明。

### §4.5 KT 五值与 KT 锚文件内 15 锚的同源不一致 — 组 C C1 / C6 / C5 / C7 已实测

**决策点**：

- `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（6,680 B，SHA-12 `03C6C01F3697`）含 15 锚（KT-A1 / KT-B1 / KT-C1 × 5）。
- `deposon_team/_designs/V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md`（SHA-12 `C41C1D6AA794`）L42–L46 含 KT 五值（`78b71d404366` / `0410ca0fbdae` / `59d8f56347d5` / `cce8e9a1b00e` + 该锚文件自身 `03c6c01f3697`）。
- `deposon_v3_v7_summary_2026_09_11.json`（25,049 B，SHA-12 `063AC8D00542`）L290 列 KT 五值，与上同源。
- `deposon_v3_v7_summary_2026_09_11.json` L369–L377 记录 canonical 五锚的算法重构得到"UNVERIFIED" / "幽灵路径" / "trusted source swapped to d78c42f7bab4 family"——coze §二 S-36 L117 与 L290 引。

**v1.1 组 C 复算结论**（worker 实测）：

| 编号 | 议题 | worker 实测 | 标签 |
|---|---|---|---|
| C1 | KT 锚文件条数 | `03C6C01F3697`（6,680 B / 189 行）；**顶层 15 条**（KT-A1 L14–L56、KT-B1 L57–L93、KT-C1 L94–L130，各 5 条）；distinct value **16 个**；coze (`00593014CBD3:65`) 自报 "13 条 distinct" 漏数了 `P_A_FROZEN_RUNS` 数组 (`03C6C01F3697:34–38`) 里 3 个独有元素（`6edb2aec1660` / `62c1a41e1db8` / `af51da229652`）。 | on-disk fact（coze 13-vs-16 属口径分歧） |
| C5 | `deposon_v20_baselines.json` (`6edb2aec1660`) | `results/` 全目录（475 文件）+ 整库递归 0 命中；`results/` 下 v20 系仅有 `deposon_v20_gt2b.json` (`A2AE7997EE67`, 123,331 B / 500 行，SHA-12 不符)。同锚文件内 v19 (`910c4333eead`)、v21 (`9d9ae5001c57`)、`P_A_KILL_LINE` (`bd1caab42b4c`)、`KT_B1_KILL_LINE` (`9f351078e5bf`) 四处实测匹配。 | no on-disk artifact |
| C6 | KT_B1 口径冲突 | **非实质冲突**。`BAEF94E393DE` L83 同一行同时含 `| B2 KD | 0.0028 | 0.5(占位) | GRAY_BOTH_BELOW | <1 min |` 三属性；coze (`00593014CBD3:420`) 取数字层、VS/claude (`D39CB17B051B:375, 377`) 取裁定层，同源同值。`BAEF94E393DE:86, 179` 解释 GRAY 来自 deposon 占位值。 | on-disk fact |
| C7 | 同一锚文件内**声明值与实测不一致** | `P_A_LLM_CLIENT` 声明 `tools/llm_client.py` = `055e874ea5c1`；实测 = `1722500DA4AA`。`P_A_HARNESS` 声明 `tools/exp_harness.py` = `9f383935c00c`；实测 = `275E480BA4D9`。frozen_runs 的 `62c1a41e1db8`（v18）与 `af51da229652`（v17）未找到。 | on-disk fact（声明值与实测不一致这一事实本身） |

**并列可选路径**：

- **路径 A**：**承认 15 锚 ≠ KT 五值 ≠ 18 frozen**：三种"锚"在不同文件层用不同语义；PI 在 §5 表的作答栏内给出每条的最终定义。
- **路径 B**：**以 KT 锚文件自身为准**：任何引用 KT 锚必须引用 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 的 15 锚；V3 summary L290 / PATCH V2 L42–L46 的 KT 五值在 V4 引用一律标 `[deprecated]`。
- **路径 C**：**以 KT 五值为准**（v3 终判 lineage）：邀请函 §2.6 "5 KT-ABC1 anchors" 的 5 指 KT 五值（coze §一 S-11 提议"主锚为本文件自身 SHA-12 + 4 个 SPEC V0.1 值"）；15 锚在 V4 引用标 `[re-fit hypothesis]`。
- **路径 D**：PI 自定义路径。**v1.1 注**：组 C C7 已实测声明值与实测不一致，建议 PI 在 §5 表作答栏明示后续如何处置（修订锚文件 / 增加 8 行向 v19/v18/v17 增加 explicit path / 不修）。

**盘上锚**：

- KT 锚文件：`verifier\handoff\KT_ABC1_anchors_sha256_12.json:13–131`（实测 189 行）。
- PATCH V2 五值：`deposon_team\_designs\V3X_PATCH_5ANCHOR_RECONCILE_V2_2026_09_17.md:42–46`，SHA-12 `C41C1D6AA794`。
- V3 summary KT 五值记录：`results\deposon_v3_v7_summary_2026_09_11.json:290`（coze §二 S-36 L117 引文），`results\deposon_v3_v7_summary_2026_09_11.json:369–377`（同源 swap 记录）。
- Claude Code §1.7 L54–L62（"18 frozen vs 15 anchors vs 16 anchors" 三术语）：`D39CB17B051B:54–62`。
- kimi §一 第 4 项 L16（"KT 五值（78b71d404366 等四值）不在 KT 锚文件内"）：`_kimi_v4_theme_reply_2026_09_20.md:16`。
- v1.1 整合稿 §6.5.3 组 C C1 / C5 / C6 / C7 完整复算记录。

### §4.6 18 frozen anchors / 16 frozen schema anchors / 15 KT-ABC1 anchors 三套术语的语义区分

**决策点**：Claude Code §1.7 L54–L62 报告三套不同"锚"被邀请函与种子场混用：

- "18 frozen" 仅在 `results/_adendum_FGK_complete_20260917_143033.md:20,166` 与 `results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md:19,22,120,132,159` 出现。
- "15 anchors" = `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 的 KT-A1 / KT-B1 / KT-C1 × 5。
- "16 anchors" = `deposon_team/plugins/_v3x_frozen_schema_v1.json` 的 7 spec + 4 plugin + 2 anchor_json + 2 benchmark + 1 corpus。

**并列可选路径**：

- **路径 A**：**三套术语冻结**——18 frozen / 15 KT / 16 schema 各有自指的盘上来源，V4 不试图统一。
- **路径 B**：**统一为单一锚**——PI 在 §5 表的作答栏内写出 V4 该用什么术语，并指出每条原引用应如何重写。
- **路径 C**：**任 V4 选其一**：邀请函 v1.x 后续版本在 §2 / §3 / §6.4 任一处明示"18 / 15 / 16 系不同物"，PI 在本条批准。
- **路径 D**：PI 自定义路径。

**盘上锚**：

- Claude Code §1.7 L54–L62（"18 frozen"、"15 anchors"、"16 anchors" 各自盘上来源）：`D39CB17B051B:54–62`。
- 邀请函 §3.2 S-11 L168（"18 frozen anchors + 22 caption entries + 5 KT anchors" 表达式）：`3D9F73519F6C:168`。

---

## §5 逐条作答表

每行：编号 / 决策点 / 可选路径 / 依赖的其他条目 / PI 作答栏留空。

作答表的编号与 §1 / §2 / §3 / §4 一一对应。PI 可在"PI 作答栏"内自由写：选定路径 / 不定 / 暂不裁定 / 写新路径 / 标注"见附件 X"等。

**v1.1 P1–P6 拍板回填区**：

| 拍板项 | §5 对应行 | PI 拍板内容 | 结果落点 |
|---|---|---|---|
| P1 | §2.9 / §4.1 | GLM 回函归属：两份都在附件中，agentmore 模式，5-agent 团队，标注为查理；查理件（ac74a04efeb2）补入 §0 锚表 + §4.14 | §2.9 标题、§4.1 路径 A、§0 末段锚表 |
| P2 | §4.1 / §2.9 | 唯一归属 = GLM（756/761）；747/766 维持豆包工作 | §4.1 路径 A 标「已拍板」、§2.9 标题 |
| P3 | §4.3 / §4.2 | codex 778/782 落盘 results/；coze 结果/与附件同哈希统一取 results/ | §4.3 路径 A 标「codex 已落盘」、§4.2 路径 A 标「已拍板」 |
| P4 | §4.4 / §4.5 / §4.5-C1–C8 | 全部派 worker 复算 | §4.4 / §4.5 / §7 汇总 |
| P5 | §6 末段 | A-4 断行自检：除已修复 A-1（descriptive 拆词）外全文无其他拆词实例 | §6 末段 + 整合稿 §8 末段 |
| P6 | §6.2 + §0 头部 | 行数 canonical = `ReadAllLines` UTF8；整合稿 1,041 / 问卷 587；Get-Content 不带 -Encoding 的 636/277 误口径作废 | §0 头部 + §6.2 + 整合稿 §6.2 + §8 末段 |

| 编号 | 决策点 | 可选路径 | 依赖的其他条目 | PI 作答栏 |
|---|---|---|---|---|
| **§1.1.1** | 邀请函 §4.1：最小可证伪化反蒸馏实验——**已代拟**（PI 委托 2026-09-22）：双轨 Track 1（铁律现状 0 LLM：确定性退化算子族——n-gram 截断 / 词表收缩 / 温度式重采样 / 嵌入投影回归，全超参钉死）+ Track 2（真 LLM 学生，启动前提已随 §3.1 拍板解锁——PI 2026-09-22「V3的剑不斩V4的官」）；GT 构造性声明（S-36 锁定：正类 = proxy student 构造集，负类 = 独立对照，不外推真实学生）；分布构造三选一（KDE / Voronoi / 闭式 sliced-Wasserstein）+ JS 主度量 + 对称 KL 稳健性；证伪判据三分支 (a)(b)(c) 预注册（任一成立即 FAIL）；R3 排列检验 n≥1000 / R6 冻结集外负对照校准 τ / R7 margin δ=D₂−D₁ 并列 top-2 判 GRAY / R8 held-out D1 前冻结；产物 6 件诞生即 SHA-12；KT-B1 KD baseline 默认不纳入学生侧素材（留 PI 随 §3.2 注 L215 裁定）。详见代拟稿 `results/_v4_gA1_experiment_outline_2026_09_22.md`（SHA-12 `F4A6BDD43962`；**PI 复核通过，已生效**（PI 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870）） | (无并列；PI 在 §1.1.1 作答栏内给具体实验轮廓) | §3.1, §3.2, §3.8 | 已代拟已生效（PI 委托 2026-09-22 + PI 复核通过 2026-09-22） |
| **§1.1.2** | 邀请函 §4.3：V1–V3 网格能否作为学生侧信号面——**已拍板**（PI 2026-09-22）：§3.2 路径 B「构造 proxy student 输出集」（启动前提已随 §3.1 拍板解锁——PI 2026-09-22「V3的剑不斩V4的官」；落盘 `results/_v4_proxy_student_*`；教师侧素材只读，18 frozen 与 9 网格不动） | §3.2 路径 A / B / C / D / E | §3.2 | §3.2 路径 B「PI 拍板 (2026-09-22)」 |
| **§1.1.3** | 邀请函 §4.4：22-caption 指纹作为隐写水印——**已拍板**（PI 2026-09-22，自定义）：邀请函阶段关闭 | §3.5 路径 A / B / C / D / E（V4 引用范围） | §3.5, §3.8 | 自定义「邀请函阶段关闭」(PI 2026-09-22) |
| **§1.1.4** | 邀请函 §4.5：逆蒸馏 claim 形态——**已拍板**（PI 2026-09-22）：§3.2 路径 B「构造 proxy student 输出集合」（claim 层面，与素材层面 §1.1.2 同路径）；逆蒸馏 claim 的 GT 来源 = proxy student 构造集（构造性声明：正类 = proxy 构造集，负类 = 独立对照，不外推真实学生，沿 §1.1.1 代拟稿同一立场，代拟稿待 PI 复核）；proxy 输出落盘 results/_v4_proxy_student_*；18 frozen 与 9 网格不动；启动前提已随 §3.1 拍板解锁（PI 2026-09-22「V3的剑不斩V4的官」）；§3.2 路径 B 于组 C 批 1 正式确认 | §3.2 路径 A / B / C / D / E | §3.2, §3.8 | §3.2 路径 B「PI 拍板 (2026-09-22)」 |
| **§1.1.5** | 邀请函 §4.7：Dimension 6 跨学科种子是否 in-scope——**已拍板**（PI 2026-09-22）：In-scope——跨学科种子正式纳入 V4 主题范围；类比空间（curvature / observer effect / no-cloning / Bell）属主题自然词汇；邀请函 §7.10 三态裁定 = in-scope；同步落 §1.2.8 | §3.1 路径 A / B / C / D / E / F 与 §4.1 各路径 | §3.1, §4.1 | In-scope「PI 拍板 (2026-09-22)」（同步 §1.2.8） |
| **§1.1.6** | 邀请函 §4.9：40 种子生产性判定——**批 3 走法已拍**（PI 2026-09-22）：分批问卷逐种子判（R1 = Dimension 1 首四条 S-01–S-04）；**判定依据已立**（PI 2026-09-22，R1 批）：deposon 项目核心准则「大材小用，落到实处，与死同行」（PI 原文逐字，已录入长期记忆）；**R1 已答**（PI 2026-09-22）：S-01 / S-02 / S-03 / S-04 均答「沿用 deposon 核心准则」（S-01 原文：「请记忆deposon项目核心准则：大材小用，落到实处，与死同行」）；**S-05–S-40 走法已拍**（PI 2026-09-22，问卷 ask_a1eec04a2c64280da45c9cc4）：Mavis 按准则代拟草案——**已代拟**：36 条判定草案落盘 results/_v4_gA3_seeds_judgment_draft_2026_09_22.md（SHA-12 F4EABBDADEB9/13,755 B/120 行；判定框架 = 核心准则三问映射 Q1 小/Q2 实/Q3 死；17 productive / 19 non-productive，borderline 均带条件注记；底物共离观察 4 组；**PI 复核通过，已生效**（PI 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870：「确认生效且前2条也补为你的具体口径而非模糊的deposon准则」）——R1 前 2 条 S-01/S-02 已按 PI 指示补具体口径：均 **non-productive**（当前资产面；S-01 阻断 = 权重白盒通道不存在，S-02 阻断 = 嵌入导出通道不存在、与 S-08/S-30 同阻断同复评条件）；S-03/S-04 后随 PI 同日数字更正（「前4条都补为你的具体口径……之前输错数字了」）亦补为具体口径：S-03 productive（borderline：停顿节奏时间维度冻结纯文本不可观测，行为指纹操作化收窄为措辞/词频/句法层面，与 S-07/S-21 共底物）、S-04 non-productive（当前资产面：盘上无推理链形态样本——V20 系盲测判别输出、V7 系 verdict，与 S-34 同阻断同复评条件）；40 条全景（R1 更正后）= 18 productive / 22 non-productive / 0 沿用核心准则；种子稿演进链 `9FFD5DF08586` → `80BFEFED178A`（V1–V2 注记）→ `9119BB791DC1`/19,772 B/147 行（R1 数字更正后现态）；**V1–V2 方法学底物注记已补录**（PI 2026-09-22，问卷 ask_5b15ae2e55eb7c84f405f1d4 拍板「维持判定 + 补注记」+ ask_ecd9aa4264fba3e90ce9f1f8 过目通过：S-25/S-28 复评条件扩写为「收窄为静态博弈形式化版本可复评」——借 V1–V2 GT_FORMALIZATION_v1 + ECR 型标量账 + 系统采样协议底物，S-27/S-29 维持原判，36 条判定与 40 条全景统计不变；准则口径随录「准则才是根，已发表论文的章节只是一处外显」；种子稿注记后态 SHA-12 `80BFEFED178A`/18,304 B/145 行——该态后被 R1 数字更正演进取代，见前） | (PI 在 §1.1.6 作答栏内逐种子给判定) | §2.5.a, §3.6 | 36 条判定已生效（PI 复核 2026-09-22）：17 productive / 19 non-productive；R1 四条已全部补具体口径（PI 数字更正 2026-09-22）：S-01/S-02/S-04 non-productive（当前资产面）、S-03 productive（borderline）；40 条全景 = 18/22/0；V1–V2 注记已补录（PI 拍板 2026-09-22） |
| **§1.1.7** | 邀请函 §4.11：framework-free 是否真有帮助——**已答**（PI 2026-09-22，自由作答，逐字）：「帮助有限，于是我追加了提示词：“and more idea? write in reply. let you brainstorm. let your sub brainstorm.” 可以发现回函效果不错」——framework-free 单独效力有限，PI 以追加 brainstorm 提示词补足后回函效果良好；同步落 §1.2.9（non-framework 原则时效细分未单独拍板） | (PI 在 §1.1.7 作答栏内作答) | §1.2 §7.12 | 自由作答（PI 2026-09-22）→ 帮助有限 + 追加提示词后回函效果不错（同步 §1.2.9） |
| **§1.2.1** | 邀请函 §7.1：9-backbone / 5-artifact 映射 | §3.5 路径 A / B / C / D / E | §3.5, §3.4 | (待答) |
| **§1.2.2** | 邀请函 §7.2：21 vs 22 caption 计数 | §3.6 路径 G / H / I | §3.6 | (待答) |
| **§1.2.3** | 邀请函 §7.3：M3 / minimax 目录名——**已拍板**（PI 2026-09-22，随 §3.4「建立别名表即可」；别名表 PI 复核通过 2026-09-22）：五层并存——散文层 `M3` / §6.4 API 占位层 `minimax` / by_model 目录层 `minimax` / D7 verdict 层 `minimax-m3` / prompt pack §4 索引层 `minimax`；详见 `results/_v4_alias_table_2026_09_22.md`（SHA-12 `56538D381BB6`，生效版）表 2 | §3.4 路径 A / B / C / D | §3.4 | 随 §3.4「建立别名表」（PI 2026-09-22）；具体值已随别名表生效回填 |
| **§1.2.4** | 邀请函 §7.4：KIMI 公开 vs API 命名——**已拍板**（PI 2026-09-22，随 §3.4「建立别名表即可」；别名表 PI 复核通过 2026-09-22）：四层并存——散文层 `KIMI-K3` / §6.4 API 占位层 `kimi-for-coding` / D7 verdict 层 `kimi-k2.7-code` / by_model 目录层 `kimi`；详见 `results/_v4_alias_table_2026_09_22.md`（SHA-12 `56538D381BB6`，生效版）表 1 | §3.4 路径 A / B / C / D | §3.4 | 随 §3.4「建立别名表」（PI 2026-09-22）；具体值已随别名表生效回填 |
| **§1.2.5** | 邀请函 §7.5：V7 / R5 版本标识——**已拍板**（PI 2026-09-22，随 §3.4「建立别名表即可」；别名表 PI 复核通过 2026-09-22）：四层并存——散文层 `V7` / D7 verdict 文件名层 `V7` / 最终报告层 `V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md` / codex D1 review 层 `R5`（"V3 final R5 manifest"）；V7 与 R5 语义关系盘上材料不足，别名表标注待 PI 补注；详见 `results/_v4_alias_table_2026_09_22.md`（SHA-12 `56538D381BB6`，生效版）表 3 | §3.4 路径 A / B / C / D | §3.4 | 随 §3.4「建立别名表」（PI 2026-09-22）；具体值已随别名表生效回填；V7–R5 关系待 PI 补注 |
| **§1.2.6** | 邀请函 §7.6：P-G v01 verdict_pending 状态 | §3.8 路径 A / B / C / D / E | §3.8, §3.1 | (待答) |
| **§1.2.7** | 邀请函 §7.8：v0.2 lineage | (PI 在 §1.2.7 作答栏内作答) | §3.6 | (待答) |
| **§1.2.8** | 邀请函 §7.10：Dimension 6 in-scope——**已同步**（自 §1.1.5，PI 2026-09-22）：In-scope（跨学科种子正式纳入主题范围，邀请函 §7.10 三态裁定 = in-scope） | §1.1.5 同 | §3.1, §4.1 | 同步自 §1.1.5：In-scope「PI 拍板 (2026-09-22)」 |
| **§1.2.9** | 邀请函 §7.12：non-framework 原则——**已同步**（自 §1.1.7，PI 2026-09-22 自由作答）：帮助有限 + 追加 brainstorm 提示词后回函效果不错（逐字原文见 §1.1.7 行）；non-framework 原则时效（V4 全程 vs 仅初始重建）与 §3.1 路径归属未单独拍板，留 PI 后续 | §3.1 路径 A / B / C / D / E / F | §3.1, §3.5 | 同步自 §1.1.7（PI 2026-09-22）；时效细分未单独拍板 |
| **§1.2.10** | 邀请函 §7.14：recipient list | (PI 在 §1.2.10 作答栏内逐回函方给 add / retire / merge) | §4.1 | (待答) |
| **§1.2.11** | 邀请函 §7.16：reviewer-burndown 主题层 recovery | §3.9 路径 A / B / C / D / E | §3.9 | (待答) |
| **§2.1.a** | Mavis 加入 §4 第 8 条提议 | (PI 在 §2.1.a 作答栏内接受 / 不接受 / 修改) | §3.2, §3.3 | (待答) |
| **§2.2.a** | Trae code 加入 §4 开放问题 | (PI 同上) | §3.8, §3.2 | (待答) |
| **§2.2.b** | Trae code trap-benchmark spec 提议 | (PI 同上) | §3.2, §3.3 | (待答) |
| **§2.2.c** | Trae code measurement-instrument probe 提议 | (PI 同上) | §3.8, §3.9 | (待答) |
| **§2.3.a** | Trae work 加入 §4 开放问题 | (PI 同上) | §3.4, §1.2 §7.1 | (待答) |
| **§2.4.a** | Claude Code §5.11 报告（§0.2 vs KT-B1） | §3.3 路径 A / B / C / D / E | §3.3, §3.1 | (待答) |
| **§2.4.b** | **已拍板**（PI 2026-09-22，随 §4.4 路径 A 联动关闭）：Claude Code §1.8 报告（§8 表 8 行空白）与组 B 8 行补全表一并按 §4.4 路径 A 采信 | §4.4 路径 A / B / C / D | §4.4 | §4.4 路径 A「PI 拍板 (2026-09-22)」（联动关闭） |
| **§2.5.a** | coze 性质标签取值域提议 | (PI 在 §2.5.a 作答栏内接受 / 不接受 / 修改) | §3.5 | (待答) |
| **§2.5.b** | coze N-01 ~ N-08 新种子 | (PI 在 §2.5.b 作答栏内逐条接受 / 不接受 / 修改) | §1.1 §4.7, §3.2 | (待答) |
| **§2.5.c** | coze N-04 评测参照推理本身 | (PI 同上) | §3.2, §1.1 §4.5 | (待答) |
| **§2.6.a** | workbuddy 未在 §4 末尾加提议 | (无作答必要) | — | (无作答必要) |
| **§2.6.b** | workbuddy anti-distillation 反转提议 | (PI 在 §2.6.b 作答栏内接受 / 不接受 / 修改) | §1.1 §4.7 | (待答) |
| **§2.6.c** | workbuddy embedding 全 NOISE 预注册提议 | (PI 同上) | §3.6, §1.1 §4.9 | (待答) |
| **§2.7.a** | kimi 加入 §4 开放问题 | (PI 同上) | §3.5, §3.8, §1.2 §7.1 | (待答) |
| **§2.7.b** | kimi 同输入跨厂商输出对比新种子 | (PI 同上) | §1.1 §4.5 | (待答) |
| **§2.8.a** | 豆包工作加入 §4 开放问题 | (PI 同上) | §3.5, §1.1 §4.11 | (待答) |
| **§2.8.b** | 豆包工作 brainstorm 24 条新种子 | (PI 在 §2.8.b 作答栏内逐条接受 / 不接受 / 修改) | §1.1 §4.7 | (待答) |
| **§2.9.a** | **已拍板**（PI 2026-09-21）→ 唯一归属 GLM（详见 §4.1）。v1.1 worker 已对 GLM 主件给出完整引用。**已拍板**（PI 2026-09-22，组 D 收尾批）→ 引用面扩展到 addendum 761：主件 756 `C78CFB42E33D` + addendum 761 一并按 GLM 引用 | (PI 在 §2.9.a 作答栏内接受 / 不接受 GLM 归属下 9.a) | §3.5, §3.4, §4.1 | §4.1 路径 A 扩展到 761「PI 拍板 (2026-09-22)」 |
| **§2.9.b** | **已拍板**（PI 2026-09-21）→ GLM addendum 同 §2.9.a。 | (PI 同上) | §1.1 §4.5 | (GLM addendum 已引用) |
| **§2.10.a** | codex Track 3 utility/resistance/cost 提议 | (PI 同上，且先决 §1.2 §7.12) | §1.2 §7.12 | (待答) |
| **§2.10.b** | codex brainstorm serialization / formatting 提议 | (PI 同上) | §3.5, §3.6 | (待答) |
| **§3.1** | 铁律边界——**已拍板**（PI 2026-09-22，自定义路径 F，原文逐字）：「V3的剑不斩V4的官」——V3 时期 7+9 铁律不构成 V4 工作的封禁；结构性推论（老实注记）：no_llm / no_proxy / no_gateway 在 V4 proxy student 生成语境下放开，§1.1.1 Track 2 与 §1.1.2 / §1.1.4 已拍路径的启动前提解锁；资产保护不受影响（18 frozen 与 9 网格不动，沿 §3.2 路径 B 选项原文） | §3.1 路径 A / B / C / D / E / F | §3.2, §3.3 | 自定义「V3的剑不斩V4的官」（PI 2026-09-22） |
| **§3.2** | 无学生侧——**已拍板**（PI 2026-09-22）：路径 B「构造 proxy student 输出集合」——与 §1.1.2（素材层面）/ §1.1.4（claim 层面）已拍同路径正式确认；启动前提已随 §3.1 拍板满足；18 frozen 与 9 网格完全不动；KT-B1 KD baseline 维持默认不纳入学生侧素材（PI 未在作答中改判，沿 §1.1.1 已录默认） | §3.2 路径 A / B / C / D / E | §3.1, §3.3 | §3.2 路径 B「PI 拍板 (2026-09-22)」 |
| **§3.3** | §0.2 vs KT-B1——**已拍板**（PI 2026-09-22，自定义，原文逐字）：「说过了，17份回函已全部回收，且不再邀请函，后续涉邀请函问题同样处置」——邀请函流程终止（17 份回函全部回收），不再出邀请函 v1.x 后续版本；§0.2 L26 与 KT-B1 系列抵触不再经邀请函版本演进修正（沿 §1.1.3「邀请函阶段关闭」同一口径延伸）；后续凡涉邀请函的处置问题均按此口径 | §3.3 路径 A / B / C / D / E | §3.1, §3.2, §2.4.a | 自定义「不再邀请函，后续涉邀请函问题同样处置」（PI 2026-09-22） |
| **§3.4** | 命名漂移——**已拍板**（PI 2026-09-22，自定义，原文逐字）：「建立别名表即可」——建立跨层别名对照表（KIMI-K3 / kimi-for-coding / kimi-k2.7-code / kimi 目录名；M3 / minimax / minimax-m3；V7 / R5 等所在层映射），一次性处置；覆盖 §1.2.3 / §1.2.4 / §1.2.5（§7.3 / §7.4 / §7.5）；别名表制品起草沿三稿先例走 Mavis 代拟 → PI 复核生效 | §3.4 路径 A / B / C / D | §1.2 §7.3 / §7.4 / §7.5 / §7.6 | 自定义「建立别名表即可」（PI 2026-09-22） |
| **§3.5** | 资产覆盖缺口——**已拍板**（PI 2026-09-22，自定义，原文逐字）：「说过了涉邀请函问题无需再问」——随 §3.3 口径处置：邀请函流程终止（17 份回函全收，不再出 v1.x），邀请函 §8 / prompt pack §4 覆盖缺口不再经邀请函扩表或修版裁决；V4 引用范围由 V4 自有文档确定，引用值以盘上实测为补充权威（沿 §3.9 路径 B 已拍口径） | §3.5 路径 A / B / C / D / E | §1.2 §7.1, §2.7.a | 自定义「随 §3.3 口径：涉邀请函不再问」（PI 2026-09-22） |
| **§3.6** | 数字内部矛盾——**已拍板**（PI 2026-09-22，自定义，原文逐字）：「同上」——随 §3.3/§3.5 同口径处置：邀请函内部数字矛盾（L66 vs L383 字节、§4/§7 跳号、~600 vs 45、D7 文件名日期 vs 内时间戳、V3 summary 37047 vs 38545、51 vs 52）不再经邀请函修版裁决；V4 文档引用上述资产时以盘上实测值为补充权威（沿 §3.9 路径 B + P6 行数口径）；盘上文件自身矛盾（V3 summary 两处数值不一致等）保持现状不修 | §3.6 路径 A / B / C / D / E / F / G / H / I | §2.5.a, §2.6.c, §2.10.b | 自定义「随 §3.3 口径：涉邀请函不再问」（PI 2026-09-22） |
| **§3.7** | 公开表与程序不符——**已拍板**（PI 2026-09-22）：路径 C「作为 V4 前置修正项」——V4 不引用 `P_A_D1_D3_REPORT` 的 143–147 参考表（该行 RM iteration count=1 / Bayes count=32 系 `boss_pa_1_rbr_rm.py` 不能发射的值），直到该表与 `boss_pa_1_rbr_rm_result_2026_09_15.json` 之一被修；V4 其余引用不受影响 | §3.7 路径 A / B / C / D | §3.8 | §3.7 路径 C「PI 拍板 (2026-09-22)」 |
| **§3.8** | 不稳健读数——**已拍板**（PI 2026-09-22）：路径 C「五条分两类」——程序不稳健类（simulate_rm 恒同值 / bayesian_nash_iter 二值返回 / rbr_mult 三值 / 22→6 码 62/231 对汉明 0 / 双曲 transport 保距偏差，代码可修）与档案管理不稳健类（`conservation_residual` 字段名冲突实为球内含性检查 / `corpus_pngs/` 目录存在但 0 文件，V4 不必修）；V4 引用上述读数时按类标注 | §3.8 路径 A / B / C / D / E | §1.2 §7.6, §3.1 | §3.8 路径 C「PI 拍板 (2026-09-22)」 |
| **§3.9** | **已拍板**（PI 2026-09-22）：路径 B「回函方各自独立 SHA-12 重算为补充权威」——邀请函 §8 与回函方一致即引用，否则以重算为准 | §3.9 路径 A / B / C / D / E | §1.2 §7.16, §2.4.b | §3.9 路径 B「PI 拍板 (2026-09-22)」 |
| **§4.1** | **已拍板**（PI 2026-09-21）：756 / 761 唯一归属 GLM；磁盘署名原文保留 | (PI 在 §4.1 作答栏内接受 / 不接受 GLM 归属) | §2.9.a / §2.9.b | §4.1 路径 A「PI 拍板 (2026-09-21)」 |
| **§4.2** | **已拍板**（PI 2026-09-21）：coze 件统一取 results/ 副本 | (PI 同上) | — | §4.2 路径 A「PI 拍板 (2026-09-21)」 |
| **§4.3** | **已落盘**（PI 2026-09-21）：codex 两件已落盘到 results/；其余四份维持原状 | (PI 同上) | §4.1 | §4.3 路径 A「PI 拍板 (2026-09-21)」 |
| **§4.4** | **已拍板**（PI 2026-09-22）：路径 A「组 B 补全表为权威」——8 行 SHA-12 一次性采纳（L394 行 worker 独立补 `0EB1CFAA2992`；L395–L401 采纳 PI 给定 7 串） | §4.4 路径 A / B / C / D（v1.1 worker 已实测补全 8 行） | §2.4.b | §4.4 路径 A「PI 拍板 (2026-09-22)」 |
| **§4.5** | **已拍板**（PI 2026-09-22）：路径 A「承认 15 锚 ≠ KT 五值 ≠ 18 frozen」三种锚语义不同；C7 处置 = 修订锚文件（已于 2026-09-22 执行：`03C6C01F3697` 6,680 B/189 行 → `6E9CD8CD8E07` 11,318 B/219 行；详见 §6 末段 C7 注记 + §7.3.2）；「每条最终定义」已收（§4.6 代拟稿 PI 复核通过 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870：主术语 `18 frozen` + 保留术语三条 + 重写规则 R-1~R-7，详见 `results/_v4_gA1_terminology_draft_2026_09_22.md`，SHA-12 `0A2CAF0A2BD2`，已生效） | §4.5 路径 A / B / C / D（含 §6.5.3 组 C C1 / C5 / C6 / C7 复算） | §4.6 | §4.5 路径 A「PI 拍板 (2026-09-22)」 |
| **§4.6** | **已拍板**（PI 2026-09-22，组 D 收尾批）：路径 B「统一为单一术语」——**已代拟**（PI 委托 2026-09-22，组 A 首批）：主术语 `18 frozen`（= 16 链上锚 + 2 anchor JSON 自身，口径 `_verify_15frozen.py:4`）；保留术语三条：KT 锚文件 15 条目 / schema anchors 16 条 / KT 五值（限定词不可省略）；重写规则 R-1~R-7（适用范围：邀请函后续版 + V4 新文档；V1–V3 冻结资产、已收 letters 回函、deposon-sub 资产不回改）。详见代拟稿 `results/_v4_gA1_terminology_draft_2026_09_22.md`（SHA-12 `0A2CAF0A2BD2`；**PI 复核通过，已生效**（PI 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870）） | §4.6 路径 A / B / C / D | §4.5 | §4.6 路径 B「PI 拍板 (2026-09-22)」+ 已代拟已生效（PI 复核通过 2026-09-22） |

**§5 v1.1 已答行号清单**（PI 拍板 P1–P6（2026-09-21）+ 组 D 第一批（2026-09-22）+ 组 D 收尾批（2026-09-22）+ 组 A 首批（2026-09-22：§1.1.1 + §4.6 PI 委托代拟 / §1.1.2 §3.2 路径 B / §1.1.3 自定义「邀请函阶段关闭」）+ 组 A 批 2（2026-09-22：§1.1.4 §3.2 路径 B / §1.1.5 In-scope / §1.1.7 自由作答；§1.2.8 / §1.2.9 同步）+ 批 3 R1（2026-09-22：§1.1.6 判定依据 = deposon 核心准则「大材小用，落到实处，与死同行」；S-01–S-04 沿用核心准则）+ 批 3 36 条走法与代拟（2026-09-22：PI 拍板 Mavis 按准则代拟 → 判定落盘 F4EABBDADEB9）+ 三代拟稿复核（2026-09-22：PI 确认生效——种子稿/术语稿/实验稿，S-01/S-02 补具体口径，种子稿终态 9FFD5DF08586）+ V1–V2 方法学底物注记（2026-09-22：PI 拍板维持判定+补注记，S-25/S-28 复评条件扩写，过目通过后落盘，种子稿新终态 80BFEFED178A）+ R1 数字更正（2026-09-22：前4条均补具体口径——S-03 productive / S-04 non-productive，40 条全景更新 18/22/0，种子稿现态 9119BB791DC1；组B 口径同步更正——各回函方新提议来自 17 个文件、远不止 17 条，处理与 R1 一致走 Mavis 具体口径代拟）+ 组 C 批 1（2026-09-22：§3.1 自定义「V3的剑不斩V4的官」/ §3.2 路径 B「构造 proxy student」/ §3.3 自定义「不再邀请函，后续涉邀请函问题同样处置」/ §3.4 自定义「建立别名表即可」；§1.1.1 / §1.1.2 / §1.1.4 启动前提解锁联动；§1.2.3–§1.2.5 处置方式随 §3.4 别名表拍板）+ 组 C 批 2（2026-09-22：别名表复核通过生效——代拟 C03735762BF1 → 生效版 56538D381BB6 → §1.2.3–§1.2.5 具体值回填；§3.5 / §3.6 随 §3.3 口径「涉邀请函不再问」；§3.7 路径 C「前置修正项」/ §3.8 路径 C「五条分两类」——组 C 结构性决策点 §3.1–§3.9 全收）已回填到下列行；其余行保持「待答」）：

- P1 → §2.9 (标题) / §4.1 (路径 A 标 [已拍板]) / §0 (末段新增 GLM 查理件锚表) / §4.14 (整合稿新增)
- P2 → §4.1 (路径 A「唯一归属 GLM」) / §2.9 (标题)
- P3 → §4.3 (路径 A「codex 已落盘」) / §4.2 (路径 A「统一取 results/」) / §0 表 §0.2 (§0.2 / §0.5 / §4.10 / §4.11) / 整合稿对应节
- P4 → §4.4 / §4.5 / §7 / 整合稿 §6.5.1 / §6.5.2 / §6.5.3 / §6.5.4
- P5 → §6 末段「PI 已接受（2026-09-21），按此定稿」 / 整合稿 §8 末段
- P6 → §0 头部 / §6.2 (本节) / 整合稿 §6.2 / §8 末段
- 组 D 第一批（PI 2026-09-22）→ §3.9 (路径 B「重算为补充权威」) / §4.4 (路径 A「组 B 补全表为权威」) / §4.5 (路径 A「三种锚语义不同」+ C7 锚文件修订 `6E9CD8CD8E07`) / §2.4.b (随 §4.4 路径 A 联动关闭) / §6 末段 (C7 锚修订注记) / §7.3.2 (锚哈希变更注记)
- 组 D 收尾批（PI 2026-09-22）→ §4.6 (路径 B「统一为单一术语」，具体统一术语与原引用重写规则待 PI 指定) / §2.9.a (后半：引用面扩展到 addendum 761，主件 756 + addendum 761 一并按 GLM 引用)
- 组 A 首批（PI 2026-09-22）→ §1.1.1 (PI 委托 Mavis 代拟 → 已代拟已生效（PI 复核通过 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870）：`results/_v4_gA1_experiment_outline_2026_09_22.md`，SHA-12 `F4A6BDD43962`) / §1.1.2 (§3.2 路径 B「构造 proxy student」，前提 §3.1 路径 B/C/D 放开待组 C) / §1.1.3 (自定义「邀请函阶段关闭」) / §4.6 (PI 委托 Mavis 代拟 → 已代拟已生效（PI 复核通过 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870）：`results/_v4_gA1_terminology_draft_2026_09_22.md`，SHA-12 `0A2CAF0A2BD2`；§4.5 尾注联动收口)
- 组 A 批 2（PI 2026-09-22）→ §1.1.4 (§3.2 路径 B「构造 proxy student 输出集合」claim 层面，与 §1.1.2 素材层面同路径；GT 来源 = proxy 构造集构造性声明；启动前提系 §3.1 路径 B/C/D 放开待组 C) / §1.1.5 (In-scope：跨学科种子正式纳入主题范围，同步落 §1.2.8) / §1.1.7 (自由作答：帮助有限 + 追加提示词“and more idea? write in reply. let you brainstorm. let your sub brainstorm.”后回函效果不错，同步落 §1.2.9；non-framework 时效细分未单独拍板)
- 批 3 R1（PI 2026-09-22）→ §1.1.6 (批 3 走法拍板：分批问卷逐种子判；判定依据立 deposon 核心准则「大材小用，落到实处，与死同行」PI 原文逐字；S-01 / S-02 / S-03 / S-04 均答「沿用deposon核心准则」；S-05–S-40 共 36 条走法待拍：全部沿用一笔收 / 继续逐批 / 点名例外 / Mavis 按准则代拟草案)
- 批 3 36 条（PI 2026-09-22，问卷 ask_a1eec04a2c64280da45c9cc4）→ §1.1.6 (S-05–S-40 走法拍板：Mavis 按准则代拟草案；代拟稿 results/_v4_gA3_seeds_judgment_draft_2026_09_22.md SHA-12 F4EABBDADEB9/13,755 B/120 行——判定框架 = 核心准则三问映射（Q1 小/Q2 实/Q3 死），36 条 = 17 productive / 19 non-productive，borderline 均带条件注记，non-productive 多数系当前资产面无落点（非永久判定），Dim 6 六条系生产性判定（In-scope 范围裁定不受影响）；**PI 复核通过已生效**（PI 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870）；S-01/S-02 按 PI 指示补具体口径 non-productive（当前资产面，与 S-08/S-30 同阻断同复评条件），S-03/S-04 维持「沿用核心准则」原答；40 条全景 = 17 productive / 21 non-productive / 2 沿用核心准则；种子稿终态 9FFD5DF08586/135 行)
- 三代拟稿复核（PI 2026-09-22，问卷 ask_f0ae3cf32f0bc8c83a1a8870）→ 种子判定稿（确认生效 + S-01/S-02 补具体口径 non-productive，S-03/S-04 维持原答；终态 `9FFD5DF08586`/15,597 B/135 行）/ 术语统一稿（确认生效：主术语 18 frozen + 保留术语三条 + R-1~R-7，`0A2CAF0A2BD2`）/ 实验轮廓稿（确认生效：双轨 + 算子族 + 证伪判据三分支 + R3/R6/R7/R8，`F4A6BDD43962`）——§1.1.1 / §1.1.6 / §4.5 / §4.6 四行同步更新
- V1–V2 方法学底物注记（PI 2026-09-22，问卷 ask_5b15ae2e55eb7c84f405f1d4 拍板「维持判定 + 补方法学底物注记」+ ask_ecd9aa4264fba3e90ce9f1f8 注记文本过目通过）→ §1.1.6（拍板行 + 作答栏同步）：种子稿追加「V1–V2 博弈论方法学底物注记」节——S-25/S-28 复评条件扩写为「收窄为静态博弈形式化版本可复评」（借 V1–V2 GT_FORMALIZATION_v1 + ECR 型标量账 + 6760 状态系统采样协议底物），S-27/S-29 维持原判（V1–V2 资产无助于解除阻断），36 条判定与 40 条全景统计不变；准则口径随录「准则才是根，已发表论文的章节只是一处外显」（PI 原文）；种子稿新终态 `80BFEFED178A`/18,304 B/145 行
- R1 数字更正 + 组B 口径更正（PI 2026-09-22 原文：「前4条都补为你的具体口径，而非模糊的deposon准则，之前输错数字了，来自17个文件而远不止17条的各回函方新提议也一致」）→ §1.1.6：S-03/S-04 补具体口径——S-03 **productive**（borderline：停顿节奏时间维度冻结纯文本不可观测，操作化收窄为措辞/词频/句法层面；Q1✓✓ V20 5 制品现成行为样本基线、Q2✓ 算子强度×行为指纹留存率实验可设计、与 S-07/S-21 共底物）、S-04 **non-productive**（当前资产面：V20 系盲测判别输出、V7 系 verdict，盘上无推理链形态样本；与 S-34 同阻断同复评条件）；40 条全景更新 = 18 productive / 22 non-productive / 0 沿用核心准则；种子稿演进 `9FFD5DF08586`→`80BFEFED178A`→`9119BB791DC1`/19,772 B/147 行；组B（各回函方新提议）计数更正 = 来自 17 个文件、远不止 17 条，处理与 R1 一致走 Mavis 具体口径代拟（PI 复核后生效）——组B 待办描述同步修正；**R1 更正口径已确认生效**（PI 2026-09-22，问卷 ask_ce27618f5b56dd102c5b8f72：「确认生效，进组C」）
- 组 C 批 1（PI 2026-09-22，问卷 ask_289d8f39de0f5c98f6439ae7）→ §3.1（自定义路径 F，原文「V3的剑不斩V4的官」：V3 时期 7+9 铁律不构成 V4 工作封禁；no_llm / no_proxy / no_gateway 在 V4 proxy student 生成语境放开；18 frozen 与 9 网格不动沿 §3.2 路径 B 选项原文）/ §3.2（路径 B「构造 proxy student 输出集合」，与 §1.1.2 / §1.1.4 同路径正式确认；KT-B1 KD baseline 维持默认不纳入）/ §3.3（自定义，原文「说过了，17份回函已全部回收，且不再邀请函，后续涉邀请函问题同样处置」：邀请函流程终止，不出 v1.x，§0.2 L26 与 KT-B1 抵触不再经邀请函版本演进修正，沿 §1.1.3「邀请函阶段关闭」同一口径延伸）/ §3.4（自定义，原文「建立别名表即可」：跨层别名对照表一次性处置，覆盖 §1.2.3–§1.2.5，制品起草走 Mavis 代拟 → PI 复核）；联动：§1.1.1 Track 2 / §1.1.2 / §1.1.4 启动前提解锁注记、§1.2.3 / §1.2.4 / §1.2.5 三行处置已拍（具体值待别名表）
- 组 C 批 2 + 别名表复核（PI 2026-09-22，问卷 ask_1fe637a6cd3d83f0805572f7）→ 别名表 `results/_v4_alias_table_2026_09_22.md`（代拟版 SHA-12 `C03735762BF1`/3,735 B → **生效版 `56538D381BB6`/3,860 B/49 行**，PI 复核后状态行更新）**PI 复核通过，已生效**：KIMI 四层（散文 KIMI-K3 / §6.4 API 占位 kimi-for-coding / D7 verdict kimi-k2.7-code / by_model 目录 kimi）+ 第五模型五层（散文 M3 / API 占位 minimax / 目录 minimax / D7 verdict minimax-m3 / prompt pack §4 索引 minimax）+ V7/R5 四层（散文 V7 / D7 verdict V7 / 最终报告 _V7.md / codex D1 review R5）；不裁正名只列层-名-锚；V7–R5 语义关系待 PI 补注；§1.2.3 / §1.2.4 / §1.2.5 具体值随表回填；§3.5（原文「说过了涉邀请函问题无需再问」——随 §3.3 口径：覆盖缺口不经邀请函裁决，V4 引用范围由 V4 自有文档定，引用值以盘上实测为补充权威沿 §3.9 路径 B）/ §3.6（原文「同上」——邀请函内部数字矛盾不再经邀请函修版，V4 引用以盘上实测为补充权威，盘上文件自身矛盾保持现状）/ §3.7（路径 C「前置修正项」：V4 不引用 P_A_D1_D3_REPORT 143–147 表直到表或 JSON 之一被修）/ §3.8（路径 C「五条分两类」：程序不稳健类代码可修 vs 档案管理不稳健类 V4 不必修，引用时按类标注）——**组 C 结构性决策点 §3.1–§3.9 全收**

---

## §6 末段老实交代

v1.1 本版本在 v1.0 基底上做最小增量改动；本文件未触动任何 V1–V3 资产（results/、corpus/、docs/V3X/、deposon_team/、verifier/、attacks/、deposon_team/plugins/、scripts/ 全树未读 / 未写）。本文件未触动任何 frozen 制品 / frozen schema / frozen 锚文件。本文件未调用任何 LLM API / 任何外部 URL / 任何 GitHub 操作 / 任何 WeChat 操作。本文件未引入任何密钥 / 端点 / 专有提示词。

本文件仅**新增**了 `D:\私人资料\deposon-repo\results\_v4_pi_decision_questionnaire_2026_09_21_v1.1.md` 一份文件；该文件为 PI 拍板问卷 v1.1 版草稿，不视为邀请函的 v1.x 后续版本，也不视为对邀请函任何条目的实质修订。

§3 九条中未能核到出处的条目清单（待 §6 自测报告一并出）：本会话已对 §3.1、§3.2、§3.3、§3.4、§3.5、§3.6、§3.7、§3.8、§3.9 每条均给出至少一条 `path:SHA-12:行号` 锚；其中 §3.2 注中关于"Claude Code §5.11 报告的 KT-B1 KD baseline 是否被视为 V4 学生侧素材"已留 PI 在 §5 表勾连栏中决定。

**v1.1 新增诚实交代**：

- **plugin 端点老实交代**：本会话未注入 `academic-paper-assistant:academic-paper-polish` 与 `superpowers:verification-before-completion` 两个 skill plugin 端点；按方法论（独立锚 → 多源核对 → 不宣布未跑通步骤）执行两 skill 的核心约束；锚复核 / 自验 5 项 / 双算 SHA-256 / 三方陈列均按方法论执行，未依赖具体 skill 端点。`doc-writer` agent 本轮由父会话派单，所有产物的归属、签名、版本号、回执由 agent 自管，父会话在本回报内读取。
- **A-4 断行自检**：PI 已接受（2026-09-21）按此定稿。除已修复的 A-1（`descriptive` 拆词）外，整合稿 v1.1 与问卷 v1.1 全文无其它词中断行实例。
- **行数口径 PI 拍板 P6**：本稿 canonical 行数 = `[System.IO.File]::ReadAllLines(path, [System.Text.Encoding]::UTF8).Length`；v1.0 整合稿 = 1,041 行 / 119,732 B / SHA-12 `4B10CDE29C27`；v1.0 问卷 = 587 行 / 67,686 B / SHA-12 `6A3A2D8EE357`（两份原件未被动过；详见自验 4）。`Get-Content` 不指定 `-Encoding` 所得的 636 / 277 行数作废。
- **GLM 查理件（ac74a04efeb2）老实交代**：本会话 worker 仅读该件摘要要点（§0 锚表），未逐行重核；v1.1 §0 / §4.14 仅以 PI 拍板 P1 提供的要点呈现；详细原文在 P1 后续 PI 裁定是否独立重读。
- **0 LLM / 0 API / 0 WeChat / 0 GitHub**：本稿与整合稿 v1.1 同守。
- **codex 落盘脚手架遗留**：组 A 复算动作的执行 worker 在仓库根目录留了 6 个脚手架文件（`_worker_drop_c2a1.ps1` 等），已如实上报；PI 尚未裁定是否清理。本稿与整合稿 v1.1 不引用、不清理、不修改这些脚手架。
- **C7 锚文件修订注记（2026-09-22）**：`verifier/handoff/KT_ABC1_anchors_sha256_12.json` 已于 2026-09-22 按 PI 单件明示授权（组 D 第一批 C7 处置拍板 + 微确认 4 题，两轮问卷）修订：SHA-12 由 `03C6C01F3697`（6,680 B / 189 行）变为 `6E9CD8CD8E07`（11,318 B / 219 行）。修订内容：frozen_runs 5→3（v17/v18 按 PI 微确认移除、v20 改远端实测 `84CE9B028B0C`）、P_A_LLM_CLIENT（`1722500DA4AA`）/ P_A_HARNESS（`275E480BA4D9`）/ KT_B1_AUDIT_FUNCTION（`4BDEC2683F06`）改实测值、15 处 `.mavis/scripts` 系保留原值 + not_found 注记、新增 metadata.revision 块。上文「本文件未触动任何 frozen 制品 / frozen schema / frozen 锚文件」声明仅指 v1.1 撰写会话（2026-09-21）本身；本修订为会话外 PI 授权的独立动作。修订前原件已备份（scratch `_backup_KT_ABC1_anchors_pre_C7fix_2026_09_22.json`，实测 `03C6C01F3697`）。远端 `_september_workspace/verifier/handoff/` 孪生副本仍为旧版未同步（已在锚文件 metadata.revision.remote_twin_note 声明）；全仓引用旧哈希 `03C6C01F3697` 的文档本轮一律未动（2026-09-22 ripgrep 全量实测：repo 106 件 / 293 处 + sub 71 件 / 143 处，合计 177 件 / 436 处，含归档目录、问卷/整合稿各版本、letters、docs/V3X、sub 插件与锚文件自身 metadata 自引用；先前 174 件清单为锚文件修订前口径，以本轮实测为准）。

未能核到的引用清单（v1.1 已更新）：

- 本会话对以下邀请函 §8 表内的 `(see SHA-12)` 占位符**已**由 worker 复算补全 8 行（v1.1 §4.4 / 整合稿 §6.5.2 / §7.4）：7 个 PI 给定 SHA-12（`8E1E7434905D` / `38070FD12F31` / `B2BF2A073AC8` / `3205593030BC` / `D3BDFC99FCDC` / `BC663B671994` / `B6F9956BCF5C`）+ 第 1 行 worker 独立补 `0EB1CFAA2992`，全部命中。
- v1.0 中未能核到的引用清单（CLB §6 末段第 3 段）：KIMI 模型名 `kimi-for-coding`（API 端点）/ `KIMI-K3`（公开产品名）/ `kimi-k2.7-code`（D7 verdict 字面）三串，PI 此前已给出 2026-09-08 规则：`kimi-for-coding` 是 API 端点名（代码内默认），`KIMI-K3` 是公开产品名；这两个不一致时**直接问 PI**，不瞎填。v1.1 未改动此事实。

本文件未完成段落：无。本任务全部回答均已落入本文件，未发现 abort / 未完成段落。

---

## §7 第二轮复算结论汇总（2026-09-21，worker 实测）

按 PI 拍板 P4（全部派 worker 复算）由 worker 在本会话内执行三组复算。**本节为 v1.1 新增节段**。本节内所有 SHA-12 / 字节 / 行数均为 worker 在本会话内实测（PowerShell .NET SHA256 + `ReadAllLines` UTF8）。

### §7.1 组 A：codex 两件落盘字节级复制

worker 实测：

- `results/_v4_d1_review_codex_2026_09_20.md`（`48387412B109`，4,506 B，46 行）字节级复制等于附件 `778-asset_..._48387412b109_...md`（4,506 B，46 行）。
- `results/_v4_distillation_brainstorm_reply_codex_2026_09_21.md`（`0FF6C042B845`，9,048 B，39 行）字节级复制等于附件 `782-asset_..._0ff6c042b845_...md`（9,048 B，39 行）。

**PowerShell .NET SHA256 + Python `hashlib.sha256`** 双算一致（identical）。该 worker 在仓库根目录留了 6 个脚手架文件（`_worker_drop_c2a1.ps1` 等），已如实上报，PI 尚未裁定是否清理——本问卷与整合稿 v1.1 不引用这些脚手架。**标签：on-disk fact。**

### §7.2 组 B：邀请函 §8 表 8 个 `(see SHA-12)` 占位回盘 + 8 行占位补全表

worker 实测（`Get-FileHash` + 全 `results/` 递归扫描，排除 `_archive_2026_09_20` 的 138 文件，命中 0 失败）：

- **关键事实**：7 个 SHA-12 串**均不出现在邀请函正文内**（`ripgrep` + PowerShell 双通道大小写不敏感 0 命中）；§8 表 L394–L401 共 8 行写的是 `(see SHA-12)` 占位符。7 个串是会话内 PI 提供的文件外宣称对应关系。
- **7 个 SHA-12 在 `results/` 实测命中**：

| SHA-12 | 文件名 | 字节 | 行 |
|---|---|---|---|
| `8E1E7434905D` | `_v4_experiment_invitation_2026_09_20_v0.2.md` | 41,680 | 470 |
| `38070FD12F31` | `_kimi_v4_t12_review_2026_09_20.md` | 6,644 | 80 |
| `B2BF2A073AC8` | `_v4_acceptance_coze_2026_09_20.md` | 5,467 | 70 |
| `3205593030BC` | `_v4_acceptance_trae_code_2026_09_20.md` | 6,301 | 86 |
| `D3BDFC99FCDC` | `_v4_ide_track_review_trae_code_supplement_2026_09_20.md` | 11,877 | 102 |
| `BC663B671994` | `_v4_d1_response_workbuddy_2026_09_20.md` | 14,881 | 158 |
| `B6F9956BCF5C` | `_v4_review_claude_code_2026_09_20.md` | 7,004 | 55 |

- **第 8 行**（L394）`_v4_brainstorm_seeds_2026_09_20.md` 不在 PI 给的 7 个之列；该文件实测 `0EB1CFAA2992` / 14,994 B / 294 行（本会话 worker 实测，确认与 §0 锚表一致）。

邀请函 §8 表 L394–L401 共 8 行 + 文件名 + 实测 SHA-12 完整补全表（PI 给的 7 SHA-12 全部命中；第 8 行由 worker 独立补 SHA-12）：本表已置于 §4.4。**标签：on-disk fact**（8 行文件全部命中 SHA-12；邀请函正文实为 `(see SHA-12)` 占位符、PI 7 串是文件外宣称）。

### §7.3 组 C：5 项旧矛盾 + KT_B1 口径冲突回盘（C1–C8，每条带路径:SHA-12:行号与三选一标签）

每条三选一标签：**on-disk fact** / **no on-disk artifact** / **unreproducible**。

| 编号 | 议题 | 锚 + 实测 | 标签 |
|---|---|---|---|
| C1 | KT 锚文件条数 | 锚文件 `verifier/handoff/KT_ABC1_anchors_sha256_12.json`（`03C6C01F3697`，6,680 B / 189 行，实测）。**顶层 15 条**（KT-A1 L14–L56、KT-B1 L57–L93、KT-C1 L94–L130，各 5 条）；distinct value **16 个**；coze 回函 (`00593014CBD3:65`) 自报 "13 条 distinct" 漏数了 `P_A_FROZEN_RUNS` 数组 (`03C6C01F3697:34–38`) 里 3 个独有元素（`6edb2aec1660` / `62c1a41e1db8` / `af51da229652`）。 | on-disk fact（coze 13-vs-16 属口径分歧） |
| C2 | BOSS 家族三对同字节 | boss_pc_1 / boss_pe_1_real_2d_ising (`43D9CE160FC8`, 2,460 B, 99 行)；boss_pc_2 / boss_pe_2_real_transverse_ising (`8933D61B180A`, 3,553 B, 136 行)；boss_pc_3 / boss_pe_3_real_reservoir (`94B5398BE76C`, 2,364 B, 96 行)；6 件内容的 boss_id 字段全为 BOSS-PE-1/2/3（`pc_` 前缀文件名与内容不符）。 | on-disk fact |
| C3 | D_fix2 | 制品 `results/deposon_d_fix2_metric_verify_9m60c_2026_09_15.json`（`9F88A212A77C`, 204,441 B / 6,722 行，实测）+ 日志（仅 `_archive_2026_09_20` 在盘）存在；`docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` L20 / L91–L92 声明的 `results/.tmp/_verify_d_fix2_metric_9m60c_2026_09_15.py` + `_postproc_d_fix2_metric_9m60c_2026_09_15.py` **均不在盘**（`.tmp/` 目录不存在）。数学部分（cos 相似度公式）确定性可复算，完整制品不可复算。 | unreproducible |
| C4 | V7 summary 派生列 | `results/deposon_v3_v7_summary_2026_09_11.json`（`063AC8D00542`，25,049 B / 380 行，实测）L121–129 九行含 `distance_to_ideal_1_0_0` 与 `rank` 列具体值（rank1 doubao-seed-2.0-lite distance 0.1800、rank1 glm-5.3 0.1700、rank9 deepseek-v4-pro 0.6182；L150 mean 0.3611；L151 range [0.1700, 0.6182]）；T / R / A 与 `frac` 列可与源制品静态对照，但 `distance` 与 `rank` 两列公式未声明（无 formula / metric 键）、生成脚本不在盘、Euclidean 反推多行不严格成立（rank1 重算 0.188 vs 记录 0.180）。 | unreproducible |
| C5 | `deposon_v20_baselines.json` (`6edb2aec1660`) | `results/` 全目录（475 文件）+ 整库递归 0 命中；`results/` 下 v20 系仅有 `deposon_v20_gt2b.json` (`A2AE7997EE67`, 123,331 B / 500 行，实测 / SHA-12 不符)。锚文件 `03C6C01F3697:31` 声明路径 "results/deposon_v20_baselines.json + v19 + v21 + v18 + v17"；`03C6C01F3697:34` value `6edb2aec1660`。同锚文件内 v19 (`910c4333eead`)、v21 (`9d9ae5001c57`)、`P_A_KILL_LINE` (`bd1caab42b4c`)、`KT_B1_KILL_LINE` (`9f351078e5bf`) 四处实测匹配。 | no on-disk artifact |
| C6 | KT_B1 口径冲突 | **非实质冲突**。`docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` (`BAEF94E393DE`, 11,478 B / 215 行，实测) L83 同一行同时含 `| B2 KD | 0.0028 | 0.5(占位) | GRAY_BOTH_BELOW | <1 min |` 三属性；coze (`00593014CBD3:420`) 取数字层，VS / claude (`D39CB17B051B:375, 377`) 取裁定层，同源同值。`BAEF94E393DE:86` / `BAEF94E393DE:179` 解释 GRAY 来自 deposon 占位值。 | on-disk fact |
| C7 | 同一锚文件内**声明值与实测不一致**（C1 附带新发现，原任务外） | `P_A_LLM_CLIENT` 声明 `tools/llm_client.py` = `055e874ea5c1`；实测 = `1722500DA4AA`。`P_A_HARNESS` 声明 `tools/exp_harness.py` = `9f383935c00c`；实测 = `275E480BA4D9`。frozen_runs 的 `62c1a41e1db8`（v18）与 `af51da229652`（v17）未找到。如实记录，不做裁定。 | on-disk fact（声明值与实测不一致这一事实本身） |
| C8 | §2.2 vs §8 表字节标定不一致 | §2.2 L66 (邀 8,674) vs §8 L383 (邀 8,753) vs 磁盘 8,753——与 v1.0 整合稿 §1.1 / 问卷 §3.6 相关，保持原有记录即可，不新增裁定。 | （沿用 §3.6 / 整合稿 §1.1：on-disk fact） |

#### §7.3.1 组 C 综述

- 8 条中 **on-disk fact**：C1 / C2 / C6 / C7 / C8 共 5 条。
- **no on-disk artifact**：C5 共 1 条（`deposon_v20_baselines.json`）。
- **unreproducible**：C3 / C4 共 2 条（数学可复算 / 派生列公式缺失）。

本节为 v1.1 **新增**复算汇总；v1.0 问卷 §6 / 整合稿 §6.4 仅保留 KT-B1 一项，本轮扩展到 8 条（其中 C7 / C8 为附带新发现，标注「如实记录，不做裁定」）。

#### §7.3.2 锚哈希变更注记（2026-09-22）

上表 C1 / C5 / C7 行所引锚文件 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 哈希 `03C6C01F3697`（6,680 B / 189 行）为 2026-09-22 C7 修订前旧值；该锚文件已按 PI 单件授权修订为 `6E9CD8CD8E07`（11,318 B / 219 行），修订细节见 §4.5 回填与 §6 末段 C7 注记。C1 行「顶层 15 条 / distinct value 16 个」、C5 行「v19 / v21 / P_A_KILL_LINE / KT_B1_KILL_LINE 四处实测匹配」、C7 行五值实测，均系对修订前旧版的实测记录，作为历史事实保留不改；修订后锚文件 frozen_runs 为 3 值（`84CE9B028B0C` / `910C4333EEAD` / `9D9AE5001C57`），distinct value 口径相应变化。

---

— `doc-writer`, Mavis 8-agent team, deposon 工作区, 2026-09-21.
