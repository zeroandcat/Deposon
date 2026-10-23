# 《Fiction That Feeds Back》后半初稿（§6–§7）撰写说明

查理-论文主笔｜2026-09-16｜对应派单：群管理员 16:45（覆盖 16:14 后半任务，进一步缩小口径）。交付文件：`shared/查理_第二作FTFB后半初稿_2026-09-16.md`（§6–§7，与前半同构，无重复标题头，供组装直接拼接）。

## 1. 口径与边界
- 本轮只做：§6 方法节（M1–M5＋四段式管线＋I1 匿名接口句）＋§7 deposon 案例节（平视＋数字纪律），约 2,500 词。
- 未做（下轮派发）：三则裁断并入稿文件、§8–§9、摘要、全文组装。

## 2. 数字纪律执行记录（审计≠grep：语义走读回对）
核验方式：对冻结机器可读工件（handoff JSON，upload/6a963647a6bd91091f568e80_handoff_machine_readable.json）做递归结构 walk 并逐字段读语义；repo results 层 JSON 逐字段开箱核对；与冻结首作 tex/综述定稿英文口径三方交叉。**22 组数字全部在文且各挂字段路径**：

| # | 数字 | 字段路径 |
|---|---|---|
| 1 | 守恒残差 2.220446049250313e-16（容差 1e-6） | results/deposon_benchmark_v1_4_gsm8k.json · physics_audit.t_plus_r_plus_a_max_deviation（语义核对：键名即 T+R+A 最大偏差） |
| 2 | 五锚 SHA-12（aeefb8ef6972/9bbe43f41fa8/6e9673205dc0/68a5b08ef007/6b09de9911c0） | handoff · preregistration_anchors_sha256_12（五键逐字比对） |
| 3 | ECR median=4/3，覆盖 20/22（17 有限＋S1/S2/S5 Infinity；2 图无臂数据） | handoff · headline_results.GT4_ECR |
| 4 | 杀线范围：61 图（5 族）×338 任务×20 步=6,760 状态 | handoff · headline_results.enumeration_scope |
| 5 | P1a max_dev_inf=0.8569；T-P1b min cos −1.0；T-P1c 81 档 τ∈[0,4] min cos=−1.0＋逐状态 τ∗ min cos −1.0＋τ∗ 中位数 0（双杀） | handoff · headline_results.P1a_P1b_T_P1c；源 results/deposon_v22_p1c.json · verdict.min_cos_at_best_global_tau（=−1.0000000000000002）/verdict.min_cos_per_state_best_tau（=−1.0），正文按惯例取 −1.0 |
| 6 | 势博弈降级：含环中位残差 0.669 | handoff · headline_results.P2 |
| 7 | E9.5：filter 0.87 vs 层 0.85（McNemar p=0.5）；StrategyQA 0.899=0.899（p=1.0）；Newcombe CI −2pp[−11.8,+7.8]／0pp[−8.8,+8.8]；可检差阈 ≈±10pp | handoff · headline_results.E9_5_power_honest（工件 results/deposon_v22_e95ci.json） |
| 8 | GSM8K：CoT 0.97 vs 层 0.85 | results/deposon_benchmark_v1_4_gsm8k.json · cot_baseline_accuracy / unified_accuracy（实测 0.97/0.85） |
| 9 | 融合稀释 physics 0.484→0.452（historical 0.783→0.739），λ=0.5 | results/deposon_v20_crossval.json · hybrid_lambda_convex=0.5 逐图字段（经 docs/Findings_v2.0_crossval.md＋冻结首作 tex 双重锚定） |
| 10 | 重跑审计 PASS：逐位一致重算＋5 锚＋9 项溯源抽查 | handoff · headline_results.audit（AUDIT-2026-08-30.json） |
| 11 | pytest 398 / P3 双向皆死等 | 本轮未入文（蓝图数字清单之外，保持最小数字集） |

**审计≠grep 的实例**：检索 "0.484" 时曾命中 deposon_v17_fusion_fix.json 的 .experiment_B.arms.…top3_hit_filler.std=0.4841229…——语义核对为某臂命中率标准差，属**伪命中**，已排除；真值锁定 v20_crossval 逐图字段。此例即"逐一对回+语义确认"与纯 grep 的差别，供鲍勃复核参考。

## 3. 蓝图落点
- §6.1 判据域唯 R36/R37（R8 不自造）；§6.2 M1–M5 表（判据归属照蓝图：M1/M5←R37、M2/M3←R36、M4 硬侧←R32/R33、AI 侧←R38/R39）＋同构不变量「账可重算」＋**I1 匿名接口句**（keep the books 判据系统化出处，匿名引用，公开指针延至 camera-ready，D3）；§6.3 六条已在库＋止步点＋gap 声明挂 R3 双锚；§6.4 S/F/P/E 四段各配输入/产物/判据/失败模式＋杀线先行要求。
- §7 按 7.1 链路重放（S→F→P→E）/ 7.2 判死即硬度（判死三连＋重跑审计＝"账被第二双手重记"）/ 7.3 三重如实定位（通道属性：审计通道闭合、能力通道为零；量级属性：结构同构、量级不可比；尚未属性：缺第三方采纳——无 first/only 越权）/ 7.4 同表打分（T 过/R 过/D 出范围，总表 §9.1）。
- §7 开篇即声明档位纪律（预登记档≠史学档，R1）；平视句（同表同口径同披露标准）落 §7 开篇与 §7.4。

## 4. 裁断处置状态（按 16:45 派单：下轮并入，本轮未动稿文件）
下轮组装 delta 清单：
1. 爱丽丝①：§1.2 F-C4 收紧为「同一三检查下归入四形态之一」，删「四判据」措辞。
2. 爱丽丝②：References 旗标改挂——R12 去旗、R13 留旗、R14 加旗（vol/issue/page 锚定）；References 引言句 "Two entries, [R12] and [R13]" → "[R13]/[R14]"；正文 R12 引用处相应微调。
3. 阿兰：池扩展 R01–R41（追加不重编号）；§5.1 首句挂 R40（Sagan, Contact, Simon & Schuster, 1985）；documented hinge 句挂 R41（Thorne, Black Holes & Time Warps, 1994，可并挂 R11）；"the answer became…" 维持 R11；References 补 R40/R41 两条。
4. 组装时合并前半（§1–§5＋References）＋本轮（§6–§7）＋下轮（§8–§9＋摘要）为全稿单文件。

## 5. 红线与双盲执行（脚本扫描）
- 禁词扫描：first/only/our previous/proven/proof/phase transition/exhaustive/PoA/V1.X/统一终稿/阶段稿/存在性实证 全部 0 命中（4 处序数/限定语 first/only 已中性化改写后复扫通过）；unique 1 处为否定式（"No uniqueness claim is made"）。
- R1：§7 全程预登记档措辞（closed (pre-registered) 仅用于守恒审计产物）；§6 无史学档词；两档不混用。
- R2：平视句两处（§7 开篇、§7.4 收尾）。
- R4：全文 ECR（empirical coordination ratio），PoA 0 处；R5：杀线范围措辞照 renames（系统采样 61 图×状态全穷举 6760）。
- R9：无「证明回路存在」类强语；§7 结论=「判据＋实例＋打分＋工程级中强」。
- R10：零池外引用；§6–§7 引用闭合于 R30–R39（脚本验证）。
- D1：deposon 9 处全第三人称（"the deposon project/artifact"），无 our previous work；KTBooks 经 I1 匿名接口句引用（蓝图口径，名称为轴心短语非作者信息）。
- D3：§7.1 尾句匿名化工件指针＋公开仓库链接延至 camera-ready。
- D5：正文零元表述（脚本验证）；流程语言全在本说明。
- D6：arXiv 先行口径；D1–D3 已按生效执行。

## 6. 硬伤检查结论
**未发现停手级硬伤，按计划交付。** 备忘 1 条：M1–M5 两列的判据归属照蓝图转写，正文对 R36/R37/R38/R39 均为功能性转述、未直接引述原文措辞（书文不在手）；如需引文级对齐，建议随阿兰二轮查新一并补核。

## 7. 篇幅自估与下轮接口
- §6 1,268 词 ≈2.0–2.3 页（蓝图 2.5）；§7 1,060 词 ≈1.6–1.9 页（蓝图 2.0）；合计 2,328 词（派单约 2,500，−7%）。
- 前向指针：§6.4→§7（已兑现）；§7.4→§9.1（下轮组装时兑现总表）；§8 无悬挂指针（§6–§7 未引 §8，逆通道接口由 §1.2 F-C3 与 §8 承接）。
- 给戴夫：§6.2 含 md 管道表；正文含 τ/λ/Σ/±/×/→/−/·/‑¹⁶ 上标 Unicode；H = 未出现（本轮无公式）；M1–M5 建议排版为带表格线的三列或四列表。
