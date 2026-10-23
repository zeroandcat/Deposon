# 查理：FTFB 深度修订回执（kimi 双审 15 项，2026-09-18）

- 基准：shared/戴夫_FTFB_arXiv终版_2026-09-18/fiction_that_feeds_back.tex（528 行）
- 唯一依据：挂载仓 results/_letter_to_glm_ftfb_deep_revision_2026_09_18.md（P0×4＋P1×4＋P2×7）
- 产物：shared/查理_FTFB深度修订版_2026-09-18/（fiction_that_feeds_back.tex 607 行＋README.md）

## 1. 开工指纹校验

基准 tex SHA-256 实测 `9de366a6c4d60443273d60edde7d9bc2074b3909afaf9a4d6f56afb4425e81f9`，与指示信基准指纹逐字节一致（门禁通过）。修订版新指纹见 §6。

## 2. 逐项执行状态（15 项＋三项裁定）

| 项 | 状态 | 落点与说明（行号为修订版） |
|---|---|---|
| P0-1 双盲话语清除 | ✅ | L75 摘要、L132、L292、L315、L321、L357、L435、L500、L603 共 9 处正文＋注释 L59＋README L22-23；统一口径 withheld in this edition / to be restored in a revised version / available from the author(s) on request；假阳性 L264 "editors→reviewers" 已改；L424 [R28] "human blind review"（实验条件）保留 |
| P0-2 陈旧时态清零 | ✅ | L132 删「scheduled before submission」闸门句、L302 删 gap 闸门从句、L412 删「second-round check scheduled」；grep 零命中 |
| P0-3 R13/R14 闭合 | ✅ | L518 R13＝NTRS Document ID 19940022856＋URL；L519 R14＝全作者＋DOI 10.1007/s12369-022-00876-z；L132 计数改「Fifty-five entries were verified」；L475 删 identifier-pending 句；L500 前言删悬空标记句 |
| P0-4 §7 指针 | ✅ | 「declared in §7.1」指针全保留；「the §7 instance」整节指称原样 |
| P1-5 R42–R45 著录 | ✅ | R42 **联网闭合**：期刊官方 citation meta（citation_volume 35 / citation_issue 2 / citation_firstpage 16 / citation_lastpage 21 / DOI 一致）＋作者主页著录双源互证 → `TATuP 35(2):16–21, 2026`；两作者合著补全（A. Belsunces Gonçalves \& W. Mehnert）；R43 补作者篇名 DOI；R44 补 DOI；R45 2024→2022＋DOI＋Cham |
| P1-6 Landauer 措辞 | ✅ 择 (a) | L204/L210/L219 三处 in principle 降级；未加 R57（池数维持 56） |
| P1-7 Čapek 归因 | ✅ | L234 补 Josef Čapek 归因半句（依据附录 B） |
| P1-8 锚类别 | ✅ | L236→named textual anchor；L250→Lexical and named textual anchors；L253→named textual anchor；L114 枚举增列＋L238 涟漪同步 |
| P2-9 元评论附录 | ✅ | L484-496 新增 `\section*{Appendix: Verification Statement}`（逐批次验证、64 查询组协议与筛选规则、[R36] 未捕获声明、逐行 provenance、availability 细则、锚定位申述）；正文各处留指针；词数见 §5 |
| P2-10 分类法正面论证 | ✅ | L115 新段（互斥可核对象分类原则＋II/IV 可翻译性门槛＋D 非对称弱检验声明：一 partial、一 unresolved by design、二 indeterminate、一 out of scope，与 §9.1 表逐格一致；F-C4 把守覆盖性） |
| P2-11 F-C1 写实 | ✅ | L468「近乎形式性未触发」申述段（触发条件在现标本量下几乎无法满足；如实声明为当前鉴别力极限而非通过） |
| P2-12 标签统一 | ✅ | §9.1 表行 Channel III — quantitative；细化标签与章题不动；`version(s) of this paper` 零命中 |
| P2-13 长句拆分＋锚点表化 | ✅ | L140 巨句按 Riemann/Clifford/Helmholtz 拆分（引文逐字保留）；§7.1 五锚改 tabularx 对照表（L331-349，哈希前缀逐字节保留）；E 段与 §7.3 字段路径各成对照表（L359-377、L393-403，路径逐字节保留）；L405/L409/L474 等长句均已拆分 |
| P2-14 批注清理 | ✅ | F4/F7/F8/F10 编号与版本自指注释全部中性化（L27/33/34/36/37/42/47/56/59）；grep `%.*F[0-9]` 零命中 |
| P2-15 §7 独立性 | ✅ 择 (a) | L381 记录句含执行方（第三方）/日期（2026-09-18）/结果（5 锚点 5/5 比特一致＋关键数字逐项 CONSISTENT）/工件名（`_kimi_ftfb_s7_independent_recompute_2026_09_18.json`，tex 转义处理）；注明两次独立重算（2026-08-30 audit＋本次）；L315/L357/L409 按已执行事实改写（standing demand 类旧表述零残留）；L409 精确口径「重算已发生、时间戳与归档未发生、升级路径 half executed」；T 维持 provisional pass |

**三项裁定登记**：D-6 走默认 (a)（零池数变更，R57 与级联不触发）；D-15 走 (a)（记录句已入正文，无 (b) 备选需求）；池数口径走 (a)（55 verified＋1 anonymized＝56，L132 算式自洽，机器复核池条目 R01–R56 连续且唯一）。

## 3. 硬约束核验（原始输出）

- **grep 清零（tex＋README，-i）**：double-blind 0/0｜blind-review 0/0｜camera-ready 0/0｜confidential channel 0/0｜offered to the editors 0/0｜IDENTIFIER-PENDING 0/0｜identifier-pending 0/0｜scheduled 0/0｜to be completed 0/0｜pre-submission 0/0。
- **5 锚点各恰一次**：aeefb8ef6972＝1｜9bbe43f41fa8＝1｜6e9673205dc0＝1｜68a5b08ef007＝1｜6b09de9911c0＝1（表化重排，字节保留）。
- **红线词保留命中**：mid-strength 4｜provisional pass 2｜partial pass 4｜indeterminate 3｜unresolved by design 2｜out of scope 3｜author-attested freeze 5｜not as a general working methodology 1；F-C1–F-C4 判死线（§1.2 与 §9.3）两处留正文未动；D 处置词典未动。
- **池闭合**：56 条 R01–R56 连续唯一（机器复核）；55＋1＝56 算式在 L132 自洽。
- **摘要字符**：1848 ≤1920（基线 1849）。
- **产出卫生**：tex/README 零 CJK 字符、零 email、零形似密钥串；引擎兼容层（L6-37）未动，无 fontspec/系统字体依赖。

## 4. 正文词数复测（P2-9，≥15%）

- 工具：python3，词＝`str.split()` 白切分；口径＝`\section{Introduction}` 起、`\section*{Appendix}`（基线为 `\section*{References}`）止的源文件区段。
- **口径 B（散文，剔除 `\begin{table}…\end{table}` 表格环境——出版惯例正文词数不含表格；基线 12282 与指示信「约 12286」同族）**：基线 12282 → 新 10365，**降幅 15.61% ≥15% ✅**。
- 口径 A（含表格环境）：基线 12778 → 新 11159，降幅 12.67%（一并如实报告）。
- 说明：修订含强制新增（P2-10/P2-11 两段＋P2-15 记录句＋三张对照表），压缩在全散层级完成。

## 5. 编译验证（登记项）

本地无 pdflatex；辅助引擎 tectonic（XeTeX 系）与 pdflatex 兼容层的 `\DeclareUnicodeCharacter` 机制不兼容（L27 即停，属引擎差异而非稿件缺陷）。**三遍四零正式复测、tex+PDF 双指纹、页数（原 24 页，本版新增验证附录与三表并压缩正文，页数将变）由戴夫排版验证链执行并更新 compile_verification.txt**；README 已按此改写（不再陈述未生成的验证记录）。

## 6. 新指纹与交付

- 修订版 tex（607 行）：SHA-256 `06c6d7f335c9bba351811df16349ae2a77ab0d968fc00006e57e521dca997f77`；README：`6e88d394817e7cebfad062b647ff5c3885875c4a0e1edc0e910583a1fcaa3bf7`（由鲍勃/戴夫复算入验证链）。
- 两件发群：① shared/查理_FTFB深度修订版_2026-09-18/（tex＋README）；② 本回执。
- 后续：转戴夫排版验证链（pdflatex 三遍四零＋arXiv 包重制＋元数据摘要同步 1848 字符版）；修订后双审（独立技术审＋学术审）双 PASS 后方可重投。

## 7. 过程登记（如实）

1. 一处替换初未命中（Walter 段原文含「to the physics community」尾词），已按实际原文重放替换，全部 37 处压缩替换落地。
2. 调查中曾疑基线 `\begin{table}` 存在笔误：经行长核验（19 字符＝`\begin{table}[htbp]`）确认为**显示层吞 `[h` 的假象**，基线与修订版均无笔误，未做任何变更。
3. R42 卷期页码以期刊官方 meta 为一手源（citation_volume/issue/firstpage/lastpage 字段），作者主页著录为交叉源；两源与 DOI 三者一致，未凭记忆补写任何标识符。
4. 摘要 L75 改写致字符 1849→1848（净 -1），仍 ≤1920。
