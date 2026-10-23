# 查理 · FTFB R6 落稿自检记录（2026-10-20 落稿轮 · 单轮 17 锚）

- **执行口径**：管理员 19:11:18 派单【R6 落稿＋底账追加】（沿 18:15:42 首派令口径，撞窗轮后重派）——脚本化单轮执行，以 R6 改稿单 F01–F17 锚串对为唯一输入；R5 原件 `ba2f157196f5` 只读（sha256 前 12 位断言，本轮三次断言一致、零触碰）；R6 tex 落 `shared/查理_FTFB_R6重构稿_2026/`（18:42 撞窗残留目录，本轮**重跑刷新后交付**）。
- **执行依据**：PI 17:55:25「R6 合并单全按建议且暂无额外的诗」（底账 P15）——四组 19 项全按建议；K-2/K-3/K-5 逐字取爱丽丝 A 轨 v2 §四原文；题式按拍板**甲式入稿、乙式候裁**（管理员 19:11 确认「题式按你单」）。
- **重跑刷新记录**：撞窗残留 R6 tex（18:42:37 产物，sha12 `45887c4316d3`）已备份至查理私区 `agents/6a962cc259312f271f3f1e74/r6/residue_1842/`；本轮重跑 `apply_r6_final.py`（18:45:42 修订版：`inherits this paper's` 断言订正为 (1,1)——R5 既有 1 处 C-2 允许形本体；M-1 注记行日期数字白名单化）→ 产物与残留件**字节恒等**（同 sha12 `45887c4316d3`·132,269 B·690 行）——「复验采用」与「重跑覆盖」两路径在本轮归一：残留件即 R5＋定稿版 17 对的正确产物，重跑为独立再现证明。撞窗 json 两失败项系当时断言过严的已知误报，18:45 修订版全绿。

- **输入件**：R5 原件（`ba2f157196f5`／123,129 B／666 行）；改稿单 `查理_FTFB_R6改稿单_2026_10_20.md`（sha256-12 `31c006536445`）——17 对 (old,new) 全部逐字解析自其 fenced ```tex 块，0 手抄。
- **产物**：R6 tex `sha256-12=45887c4316d3`／132269 B／690 行；unified diff（13 hunks）；本记录；selfcheck_pairs_log.json（17 对全文机器可核）。

- **结论**：17/17 应用全中，0 失配 0 多写；回放反证 PASS；References 区块字节恒等；池 66 条目与正文引用实例双恒等；词族账全过（含 position paper 自报清除 3→1、Objection/Reply 0→4、来源箭头词族 0/0、匿名面恒等）。

## 一、执行与回放（无失配·无多写的形式证明）

| 项 | 结果 |
|---|---|
| 预检：17 锚串在 R5 原文各 count==1 | 17/17 ✓ |
| 顺序应用 F01→F17：每步当前文本 count==1 | 17/17 ✓ |
| 反向回放 F17→F01（new→old 逐条还原） | PASS（R6 反向回放 17 对后与 R5 字节恒等；R5→R6 差异恰为 17 对替换全集） |
| 体量 | R5 123,129 B/666 行 → R6 132269 B/690 行（净增 9140 B，含四 objection–reply、§1 概念段、§6 前置段、K-2/K-3/K-5、摘要重写） |

## 二、池 66 与引用冻结

| 项 | R5 | R6 | 结果 |
|---|---|---|---|
| References 区块（\section*{References} 至文末） | 14898 B | 14898 B | 字节恒等 ✓ |
| \item[Rxx.] 条目 | 66 | 66 | 66/66 ✓ |
| 正文 [Rxx] 引用实例（题录区前） | 190 | 190 | 恒等 ✓ |

## 三、词族账（匿名面／0 诗引文／0 来源箭头／C-2 禁用形／G-1／G-4／G-9）

| 词族 | R5 | R6 | 判 |
|---|---|---|---|
| position paper | 3 | 1 | ✓ |
| position statement | 4 | 4 | ✓ |
| anonymized in this edition | 2 | 2 | ✓ |
| KIMI | 0 | 0 | ✓ |
| kimi | 2 | 2 | ✓ |
| onewithdream | 0 | 0 | ✓ |
| inspired by | 0 | 0 | ✓ |
| originates in | 0 | 0 | ✓ |
| traces back to | 0 | 0 | ✓ |
| the source of | 0 | 0 | ✓ |
| Objection | 0 | 4 | ✓ |
| Reply | 0 | 4 | ✓ |
| kill | 32 | 33 | ✓ |
| death | 2 | 1 | ✓ |
| objection_lower | 0 | 14 | ✓ |
| groundbreaking | 0 | 0 | ✓ |
| revolutionary | 0 | 0 | ✓ |
| unprecedented | 0 | 0 | ✓ |
| has been generalized | 0 | 0 | ✓ |
| will show | 0 | 0 | ✓ |
| is expected to succeed | 0 | 0 | ✓ |
| inherits this paper's | 1 | 1 | ✓ |

- position paper 残 1 处＝「a position paper makes world models the core component」（LeCun [R22] 第三方描述语，非自报，改稿单 §六 G-1 登记豁免）。
- kimi 残 2 处＝§7.2 审计迹字段路径既有字面（`_kimi_ftfb_s7_independent_recompute` 等，装置级，B 轨审计在案），新文本 0 增。
- objection（小写族含题式 bold）R6 总计 14 处＝Objection 标题 4＋摘要句 1（G-4 配额 4 组强形式 objection＋reply 达标，各含让步条款）。
- kill 族净 +1＝K-5「kill verdicts」逐字携带（爱丽丝 A 轨 v2 原文，乙组拍板项）；death −1＝§7.2 题面「Death is the point」转位为概念式「The first action: verdicts before the runs」；其余 kill 族字面 32 处全在保留区（12 装置级＋2 声明级判死线句全保留，G-9 级配申报值内）。

## 四、数字字面与新文本数字 token

- 反向回放字节恒等 ⇒ 一切实验数字（GSM8K/StrategyQA 分数、p 值、λ、字节数、指纹前缀等）逐字保留。
- 新文本数字 token 清点：正文 1, 1.2, 2, 5, 6, 8（全为节号引用 §1.2／§2–§5／§6／§8／§8.3，0 实验数字、0 新字面）；注记行 09, 10, 18, 20, 2026, 27, 3, 4, 5, 6（M-1 版本沿革日期/版本号，注释行不渲染）。

## 五、hunk 映射（diff 对锚串）

| Hunk | R5 起始行 | 归属 |
|---|---|---|
| H1 | 57 | F17 |
| H2 | 72 | F01+F02 |
| H3 | 80 | F02 |
| H4 | 94 | F04 |
| H5 | 110 | F03 |
| H6 | 135 | F05 |
| H7 | 171 | F06 |
| H8 | 207 | F07 |
| H9 | 235 | F08 |
| H10 | 275 | F09+F10 |
| H11 | 396 | F11+F12 |
| H12 | 460 | F13+F14+F15 |
| H13 | 513 | F16 |

## 六、失败登记

- 空（本轮 0 失败项）。

## 七、笔误订正登记（改稿单 §九 字节数转写笔误 · 不触及恒等性结论）

改稿单 §九 两处字节数系转写笔误，实测值如下（恒等判定均以实测为准，两侧恒等结论不受影响，改稿单已入档不回改，沿「笔误订正走当轮记录」先例登记）：

| 项 | 改稿单 §九 申报 | 实测值 | 恒等判定 |
|---|---|---|---|
| R6 tex 体量 | 131,329 B | **132,269 B** | R5＋17 对正向产物与撞窗残留件字节恒等（sha12 `45887c4316d3` 双侧一致）✓ |
| References 区块 | 14,779 B | **14,898 B** | R5／R6 两侧区块字节恒等（含 `a57d7fe` 恰 1 处）✓ |

## 交接口（爱丽丝语义校验／阿兰体裁验收／鲍勃差量验收指引）

- 语义校验（爱丽丝）：F03 三检语法段与 A 轨 v2 §3.4-3 承接表映射一致性；F13 同源句措辞（AI-agent 描述式不点名）；F14 K-2 先行词位（precedent＝非欧先例）；F11 题式候选甲乙语义位。
- 体裁验收（阿兰）：G-1~G-12 逐项对改稿单 §六映射表（题录纠错值以其对标件为准）。
- 差量验收（鲍勃）：`R5_to_R6_unified_diff.txt` 对改稿单 F01–F17 逐 hunk 核；`selfcheck_pairs_log.json` 17 对 old/new 全文机器可核；机器复核＝重跑 `python3 apply_r6_final.py`（确定性：解析→单轮 17 锚→回放反证→全套自检，R5 原件全程只读）。
- 编译打包（戴夫）：官方引擎三遍四零＋页数实测＋metadata（M-1 版本沿革／M-3 摘要联动）；⚠ 群传二进制损坏（UTF-8 替换符化），R6 交付一律走 shared 正本路径，勿群内直传 tex。
- 底账联动：PI 17:55–18:09 拍板链闭合件（两包鉴别结论＝甲上传件）本轮已按续喂协议追加登记为底账 P18（§三总目双写）。
- 指纹：R5 `ba2f157196f5`；R6 `45887c4316d3`；diff/JSON/MD 指纹见交付通报（以群内通报实测值为准）。

—— 查理-论文主笔 ｜ 2026-10-20 19:38 ｜ R6 落稿轮（19:11 派单）· 单轮 17 锚 · 0 失配 0 多写 · 重跑刷新与残留件字节恒等 · 建议非裁


---

## 八、F18 摘要压缩增补轮（2026-10-20 20:14 派单 · 单锚 · 唯一阻断项清除）

- **任务来源**：群管理员 2026-10-20 20:14:23 派单【R6 增补轮·单点：摘要压缩】——唯一阻断项（戴夫 20:02 登记）：R6 摘要（M-3 版）1,973 字符（arXiv paste 口径）＞常设限 1,920（超 53），包不得提交；用户 20:17 追加指令「新元数据一并交付」。
- **执行**：`apply_r6_f18_abstract.py`（前置门 sha12 `45887c4316d3`）单锚 F18 应用。old＝自 tex 提取的摘要行（0 手抄）；new＝压缩稿（四刀）。反向回放（new→old）还原输入**字节恒等**；前缀/后缀字节恒等＝除摘要行外全文零改；落盘后复读复核指纹一致。
- **字符数实证**（whitespace-normalized＝arXiv paste caliber，与戴夫 20:02 登记同口径）：old **1,973** → new **1877**（Δ=**96** ≥ 53 ✓；≤ 1,880 ✓；距 1,920 限余 **43**）。词数 291 → 277。raw-between-markers 口径（戴夫表单同列）：old 1,978 → new 1882。
- **四刀账**（砍冗词不砍要点；每刀旧→新全文登记于 `selfcheck_f18_pairs_log.json`）：

| 刀 | 旧片段 | 新片段 | 字符 |
|---|---|---|---|
| F18-a | dispensability of the fictional input | dispensability | −23 |
| F18-b | The argument separates the four channels, each anchored in cases: | The four channels are each anchored in cases: | −20 |
| F18-c | demonstrated on one artifact at the stated power; one engineering-grade, mid-strength instance is examined with its negative results disclosed in full | demonstrated on one engineering-grade, mid-strength artifact at the stated power, with its negative results disclosed in full | −25 |
| F18-d | for the engineering record, | （删） | −28 |

  逐刀依据：a＝对齐 §1.2 itemize 正典命名「T (temporal priority)／D (dispensability)／R (operative residue)」，检查对象由主张句主题（fiction-as-input）默认承载，三检名全保；b＝「分离」纪律已由主张句「four channels — … — separate under three checks」承载，头句系摘要内重复申报，「each anchored in cases」与四例证清单逐字保留；c＝原句双 one 同指（artifact＝instance＝§7 同一受检件），五要素（one／engineering-grade／mid-strength／at the stated power／negative results in full）逐项保留，且「carrying a measurable price」（§4 逐字回声）与「with its negative results disclosed in full」（§1.2 逐字回声）两处两轮压缩存活资产句**逐字不动**；d＝范围标记冗词，存储链内容要素（冻结工件／全摘要存储／公开仓冻结 commit 引用）由其后各分句自身显式承载，沿 R4 摘要削减先例（删「on the same footing as the historical cases」类范围限定语）。
- **零漂移核验**：F01 四要点逐字在场——问题化开篇句（逐字）／主张句头「We argue that fiction is not evidence but a recurrent, checkable input:」（逐字）／objection 纪律句（逐字，＝爱丽丝 5b 引文「stated against its strongest available objection and answered on the record, concessions included」）／position paper 自报保持 0 命中。爱丽丝 19 点中唯一直接引用摘要的判定位＝5b（逐字保留）；其余 18 点锚位（F03＝§1.2／F13/F14＝§8.4／F11＝题式／论证链各面）全在摘要行外，前缀/后缀字节恒等 ⇒ 19 点结论零漂移。逐字保留锚串 21 段恰 1 次（全清单落 pairs log）。
- **词族账／匿名面**：新摘要内 position paper／position statement／KIMI／kimi／kill／death／C-2 四禁形／来源箭头四词族全 0；objection 小写恰 1（G-4 摘要句计数不变）；全文词族与匿名面计数逐项与输入恒等（machine log）。数字 token 集 {1, 5, 7.4} 不变；非 ASCII 仅 §／—／–（em 6／en 1／§ 1，与旧一致）。
- **池 66／引用冻结**：References 区块字节恒等；[R01]–[R66] 恰 66；正文引用实例 190→190；a57d7fe 恰 1；行数 689 不变。
- **新指纹登记**：R6-F18 tex sha12 `69125dd78382` · 132173 B · 689 行（体量 −96 B）。F18 前态正本备份：私区 `r6/pre_f18_45887c4316d3_fiction_that_feeds_back.tex`；戴夫 R6 打包目录内 `fiction_that_feeds_back.tex` 为同字节正本（其 manifest 可复核）。
- **随件**：`F18_abstract_unified_diff.txt`（1 hunk · 摘要行整行替换）＋`selfcheck_f18_pairs_log.json`（old/new 全文＋全部检查实测值）＋`arxiv_metadata_abstract_F18_2026_10_20.txt`（新元数据：Abstract 字段新值 paste 件；其余字段沿戴夫 R6 表逐字承用并申报；页数候其重编译实测刷新）。
- **行号漂移勘误追加登记（阿兰 §四.1 移交 · 只记录不回改）**：改稿单 §六/§九 行号系撞窗中间件（131,329 B）口径，R6 终稿（132,269 B，References 区 +119 B 增长）实测漂移——派单简称「6 处」，按阿兰原表逐行展开为 7 行号对（kimi 系两行；标签依爱丽丝观察③细分）：

| 词面 | 改稿单行号（中间件口径） | R6 终稿实测 |
|---|---|---|
| position paper（LeCun [R22] 第三方描述语豁免位） | L437 | L458 |
| position statement（companion 描述） | L461 | L482 |
| position statement（AI 披露节） | L518 | L541 |
| position statement（附录） | L524 | L547 |
| position statement（[R57] 池条目） | L648 | L671 |
| kimi（L271＝Mori 术语 bukimi no tani 罗马字子串） | L256 | L271 |
| kimi（L422＝冻结审计迹文件名） | L401 | L422 |

  内容零差异；改稿单已入档不回改（沿笔误订正先例）。本登记不触发任何文件改动。
- **历史件只读零改确认**：R5 tex `ba2f157196f5`、改稿单（F01–F17）、`apply_r6_final.py`、`R5_to_R6_unified_diff.txt`、`selfcheck_pairs_log.json`、戴夫 R6 打包目录全部文件——本轮零写入（本脚本写集＝tex 本体＋四随件＋本记录追加段＋私区前态备份）。
- **接力**：戴夫重编译重打包（Abstract 字段换 F18 新值；页数实测刷新；M-3 摘要联动以本轮为准）→ 最终提交候 PI 放行。

—— 查理-论文主笔 ｜ 2026-10-20 20:32 ｜ R6 增补轮 F18 · 单锚 · 摘要 1,973→1877（Δ96）· 0 失配 0 多写 · 建议非裁
