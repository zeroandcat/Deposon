# 查理 · 第三作 v0.2 修订记录（2026-09-27）

- **任务来源**：群管理员 2026-09-27 02:58:01 派单（第三作 v0.2 修订；v0.1 已落库，171,023 B/980 行/SHA-12 758E361397C2）。
- **输入件**：① 爱丽丝《v0.1 上半件蓝图符合性预检》（9 项发现：C-1–C-6 内容性＋M-1–M-4 措辞性）；② 查理《第三作 v0.1 联动换锚清单》（S1–S7 位点＋新值槽位表）；③ 鲍勃《v1.1 新增数字独立补测复核》（E-37 证据件，15,269 B/SHA-12 91E10F763316，本轮实测复核）。
- **交付物**：`shared/_v3v4_merged_paper_2026_09_27_v0.2.md`（178,244 B/986 行/SHA-12 C07E26383D2D，完整单件）＋本修订记录。
- **修订面**：17 个差异块（diff 实测），全部落在预定修订点；无一处计划外改动。

---

## 一、爱丽丝 9 项逐项对照（发现项 → 处置 → 落位）

| # | 发现项（爱丽丝预检原文要点） | 处置 | 落位（v0.2 行号） |
|---|---|---|---|
| C-1（高） | E-37 复测证据件无锚：惯例段引「the independent re-verification of 2026-09-27」但全文无该复测件的执行者/路径/指纹锚，E-37.1/E-37.2 两值违反「无锚不写」 | **已落实**：App A「Merged-draft input anchors」表补复测件行（路径 `鲍勃_v1.1新增数字补测复核_2026-09-27.md`，15,269 B，SHA-12 `91E10F763316`，measured 2026-09-27，注明 v20 append round 草拟载体身份）；§13.3/§14.2 两处 E-37 注记各补「the re-measurement's evidence file is anchored in Appendix A」指针；头部惯例段同步补锚（cover 该措辞的全部三个提及位） | App A L922；§13.3 L424；§14.2 L440；L10 |
| C-2（高） | v9 双处（§1.2 末＋availability）载 novelty search 2026-09-15＋超三十天须按同 query families 重跑；v0.1 §1.2 只留「completed novelty search (2026-09-15…)」、§22.4 条款已随下半件落位但时间线未如实陈述 | **已落实**：§22.4 保留条款原文语义（30 天/同 query families/提交前重跑）＋补 query families 枚举（auditability/reproducibility/verifiability/verification/integrity/accountability × survey × LLM/reasoning/test-time＋per-line targeted＋adjacent-survey tracking，使 §1.2「query families recorded in the availability section」指针可解析）＋补时间线如实陈述句（search 2026-09-15→窗口 2026-10-15 关闭；写作日 2026-09-27 窗口仍开；review/typesetting 在提交前；obligation live 且未解除；不预测是否触发）。时间线约束已随本通报呈报管理员/PI（见 §五） | §22.4 L658 |
| C-3（中） | E-37 处置合规但蓝图 F2「按 v1.1 字面一字不改」未登记 E-37 例外通道 | **已落实**：App C R3 条目扩写——「The E-37 family is hereby the explicitly registered exception channel to the frozen-literal carry rule」：仅以 drafted errata 注记＋App A 证据锚＋冻结件不改＋App B 同注记传播四要件入文；通道范围=E-37.1/E-37.2 两成员，不新增其他例外 | App C R3（L977） |
| C-4（中） | 占位目录 App A 段缺 O11 换锚指令：若 v1.1 AppA 含 upload_executor 委托件行（v2 已停用），照搬会把停用版带入 | **核实为不触发（N/A）**：v1.1 AppA letters family 仅 3 行（upload application 36,945/scoping verdict 68,449/v4 commission letter 31,531），grep 实测无 `_v4_commission_upload_executor_*` 行——v0.1/v0.2 App A 均未携带停用件，无需换锚（v3 锚 25,091/C20D4F58F5C8 备查未用）。C.0 已登记「no deprecated upload-executor row exists in the carried table」 | App C C.0（L940） |
| C-5（中） | §22 执行面状态句（415-of-415＋42 commits＋回执算术不自洽）数字须锚到公开执行链件；执行链件不在公开面则降为无数字表述 | **已落实＋锚分立**：本轮在公开仓实测——`git diff --stat`（执行前 c9b82e1→执行后 a57d7fe）＝**415 files changed**、`git log`＝**42 commits**，两数与 §22.3 句逐字一致，公开历史可复算；据此把句内锚分立写明（counts recomputable from the public release history；fingerprint-consistency 结果按回执原文转写——回执不在公开面，如实标注）。App C R6 补 v0.2 复测登记（含实测值） | §22.3 L654；R6 L980 |
| C-6（低） | signoff 双件并存（26,637/26,633 差 4 字节）未注记；可选补 App A 注记（PI 拍板后入） | **已注记（PI 拍板挂起）**：本轮独立盘上实测——公开仓 `results/`（＝_september_workspace/results/）件 26,637 B/`BA4D07BD7000`（与 App A 引用值一致）；同仓 `_september_workspace/` 根下存在第二件 26,633 B/SHA-12 `739245682D40`（差 4 字节）。因两值均可对回公开盘面（非周报引用），App A 原行补 v0.2 注记：两件并存登记、引用值仍为委托账本对、权威件归属 pending PI ruling | App A L830 |
| M-1 | §3.2「used in Table 3」无远距限定 | **实为错指（修正）**：装配轮把五线矩阵排为 Table 5（Table 4＝六块映射），全文已无 Table 3 实体（v0.1 的「Table 3」为悬空指针，非仅缺限定）——改为「Table 5 (the merged five-line matrix of Section 17.3)」；L944「survey's Table 3」为源件侧指称，保留不改 | §3.2 L150 |
| M-2 | App C 自重叠测量需注明双口径（v9 先例 10-gram vs R5 先例 8-gram），避免口径混写 | **核实为已在位**：R8 逐值带口径（4.62% (10-gram)/0.21% (10-gram)/0.91% (8-gram program record)）＋新测明示 8-gram deferred；§22.5 同样双口径分立。零改动，C.0 登记「dual-caliber self-overlap records verified in place」 | R8（L982） |
| M-3 | §13.3 三个调用数（180 全配额/60 裁定/62 实测）并存易混，建议加半句说明三者关系 | **已落实**：T1.5r2 verdict 锚句后补一句「The stage's three call counts stand in one recorded relation: 180 is the full-quota reference formula (5 × 2 × 3 × 6), the ruled expansion was confined to the re-ask-2 layer at +60 calls, and the measured execution is 62.」 | §13.3 L424 |
| M-4 | Abstract「36-entry append-only errata chain」保持 v19 冻结口径，E-37 入链前勿把 36 改 37 | **核实为一致**：Abstract 36-entry 保留；§10.2/惯例段「v19（E-1 through E-36）」；E-37 两注记均为「drafted for the next append round」——零改动，C.0 登记 | Abstract L16（未动） |

## 二、FTFB 联动（仅落当前可定项，其余槽位 pending 不编造）

| 位点 | v0.1 现状 | v0.2 处置 |
|---|---|---|
| S1（§1.2 口径句） | 「an updated version is in preparation…」 | **已落事实句**：「a revised edition of the second work (its revision R4) was completed on the PI's side on 2026-09-27 and is ready for resubmission to arXiv—this fact is recorded here without predicting the hold's outcome or the resubmission's acceptance」；on-hold 状态句与 356,123 B/2D9EDC8C7303 冻结锚**不动**（解 hold/归档两触发器均未发生） |
| S4（App A 第二作行） | 旧注记「in preparation…digest will change」 | **已补 R4 版本行×2**（workspace 交付面实测 2026-09-27）：tex `查理_FTFB_R4更新交付_2026-09-27/fiction_that_feeds_back.tex` 101,928 B/`4F8C42319603`；编译件 `戴夫_FTFB_R4编译交付_2026-09-27/fiction_that_feeds_back.pdf` 411,782 B/`0B0D9495508F`（25 页，戴夫 03:08 编译交付，本轮 pdfinfo 复核）。两行均注明 repository-archival anchor **pending**（未归档不写仓锚、不带远程标识符，S1-④ 的公开仓指针留归档后）；原行注记升级为「R4 ready for resubmission…digest will change when it is archived」 |
| S6（App C R5 注册） | 「in preparation…」 | **已改写**：R4-ready 事实＋**槽位 pending 登记**（刷新后归档摘要值/页数待归档实测；arXiv 重投日期与结果含 hold 变化按 arXiv 记录；正式引用升级待出版）——均不预填值；历史值沿革注记（356,123 B/2D9EDC8C7303/23 pp.）届时保留；「not this registry's entry R4」消歧 |
| S2（§21 (5) 触发器条款） | 「the second work's update will change its digest」 | **不动，登记 pending**：触发器（归档刷新）未发生，现文仍为真；重写留触发后 |
| S3（§22.3 不可达句） | 「a reader relying on the upload face alone cannot reach it」 | **不动，登记 pending**：13 件 archive-resident 的治理口径 vs 可达性口径需 PI 拍板（清单执行纪律第 4 条） |
| S5（App C R1） | 「second work (FTFB, submitted and on hold)」 | **不动，登记 pending**：重投尚未发生，「submitted and on hold」仍为真；S5 改写留解 hold 生效后 |
| S7（§9.1 纯提名） | 无锚无状态 | 无需换锚（登记备查） |

**新值槽位状态**（对照清单 §二）：新归档 PDF 字节/SHA/页数＝**pending**（仓内未归档；交付面编译件 411,782 B/0B0D9495508F/25 页已另行登记为 workspace 行，非仓锚）；新归档 tex＝交付面 101,928 B/4F8C42319603 已登记、仓锚 **pending**；归档 source 形态＝**pending PI 裁定**；arXiv 标识符/版本号＝**pending**（重投受理后）；解 hold 生效日＝**pending**。

## 三、版本号与过程登记

- L3 版本行升 v0.2（注明修订轮性质与 App C 登记）；§21 (6)/(9) 的「v0.1」表述同步改写为「v0.1 assembled, revised same-day to v0.2」（(9) 的「two-three sequence」笔误一并修正为「blueprint, drafting, assembly, revision」）。
- App A 头部补「Rows and notes added at the v0.2 revision round are marked inline and were measured on 2026-09-27」。
- App A 输入锚小节标题改为「added at merge and at the v0.2 revision round」。
- **新增 App C C.0「The v0.2 revision round (registered)」**：论文内注册本轮全部改动（逐项带落位）＋三项「verified in place」登记（C-4 letters family 版本纪律、M-2 双口径、M-4 36-entry）＋「No verdict, no frozen number, and no literal carry of the F-family discipline is altered by this round」承诺句。

## 四、纪律自检（程序化实测，全部只读）

| 检查 | 结果 |
|---|---|
| 差异面 | 17 块，全落预定修订点（L3/10/34/150/424/440/636/638/644/654/658/818/830/890-892/913/919a922/936a940/970-973）；无计划外改动 |
| 数字多重集比对 | **删除＝零**（F 系字面与全部冻结数字零改动）；新增 token 全部来自登记面（新指纹/日期/版本标签/指针/复述值） |
| verdict 字面 | TRIGGERED 14=14、NOT TRIGGERED 10=10、composite qualification 15=15、same-direction deepening 3=3；K-N26-2/0.5663/0.4459/49.3/239,387/849D76BE3A06 频次不变 |
| O 系零收束 | 新增表述仅「pending/not discharged/makes no prediction/predicts no outcome」开放语；R4 注册条目（pending-proof placeholder）原样未动 |
| 引用闭合 | [n] token ↔ References 64↔64 双向闭合，零跳号 |
| 双盲/保密 | a57d7fe=0、Qihao=0、2609.09001=0、〔当事人W〕/〔W老师〕=0、Coze 周报零引用（coze 4 处均为 v1.1 原有教师代号；Yuan 1 处＝参考文献作者名 Yuanyi Wang 的子串；D14 2 处＝SHA 十六进制子串）；无仓 URL/远程标识符；新增行内路径仅含角色代号（与 dave-survey2 先例同口径） |
| 无空节 | 章节旗标 18=18（与 v0.1 同基线，均为「## 后直接 ###」结构，非空节）；表格行管道数 4（3 列）一致 |
| 新增指纹实测 | 本记录 §一/§二 所列 6 组新值（91E10F763316/4F8C42319603/0B0D9495508F/739245682D40/26,633/25 页）均 sha256sum/pdfinfo/git 实测，可对回源件 |

## 五、C-2 时间线约束（呈报管理员/PI）

novelty search 完成于 2026-09-15，30 天窗口 **2026-10-15 关闭**；今日 2026-09-27（窗口内第 12 天），第三作合并稿流程尚余 review＋typesetting（8-gram 自重叠实测与 tex 版亦在排版轮）。**若提交越窗，须按同 query families 重跑 search 后再提交**——该约束已如实写入 §22.4，请管理员/PI 在排期时纳入。

## 六、老实交代

1. C-4 的「不触发」结论基于 v1.1 md 件 letters family grep（3 行，无 upload_executor 行）与 v0.2 App A 逐行目检；v1.1 tex 交付件未逐行复扫（md/tex 由鲍勃 v1.1 轮验证 1:1，风险极低）。
2. 415/42 复测所用区间（c9b82e1→a57d7fe）来自周报登记的执行前/后 HEAD——commit ID 本身未写入论文（双盲红线 2），论文仅以「the 2026-09-26 release batch」定位；读者可在公开史按日期复算同值（本轮已实测复核）。
3. R4 编译件（戴夫 03:08 交付）晚于派单（02:58）10 分钟落库，本轮已一并纳入 App A 登记面；若鲍勃后续打回致 tex 变更重编，App A 两行按新裁定版实测刷新（戴夫包待办条款）。
4. signoff 第二件（26,633 B）的存在性本轮由公开仓盘面独立实测确认，与 D14 记录一致；登记入 App A 系「盘上可对回」口径，非周报引用。
5. v0.1 件本动零触碰（工作区只读；v0.2 为 cp 后 Edit 逐块修订）；仓内（repos/Deposon）零写入零移档，git 状态干净。

—— 查理-论文主笔 ｜ 2026-09-27 03:1x 落版 ｜ AI 生成
