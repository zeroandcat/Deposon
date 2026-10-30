# R27 对外节点交付册 · 公开镜像

> 基线：R26 正式门禁输出；R27 全量重建，不沿用 R22 状态结论。
> 授权与动作：upload_authorization=false；remote_write=NOT_PERFORMED；拟远端路径不是已上传证明。
> 快照边界：远端孤本依据 2026-10-29 既有镜像快照，R26 孤本来源未重采；R27 已另行完成当前远端全树精确字节拉回（HEAD 06045bceff07908aa38b8b5d3e626731b7326e7d，3,438 件），范围外非镜像文件 434 件已留档保护。

## 改了什么＋依据何在

- 以 R26 READY 分单和孤本 READY 决定逐键连接 R19 本地冻结清册；公开镜像记录为 4,069 条，范围账为本地 3,404＋孤本 665 条。
- 十二族固定为 V3、V4、V5、S3S4、G-E01、T、K-杀线、ηETAC、T5择优、39词、K-EXP8、委托面；每族保留 R1–R6。
- 公开代表证据恢复为旧十二件，逐件给出公开 target、源 SHA-256 与脱敏上传 SHA-256；不沿用 R22 的九件替换组合。
- R5 按 R26 实际上传件 upload_bytes 计；T5 是 T 的兼属视图，不重复加总。
- 对外册只列公开 READY 节点与代表证据；全量件级状态索引不进入公开交付树。

## 公开 READY 总账

| 公开镜像范围 | READY | 实际上传件字节 |
|:--|--:|--:|
| 本地 repo | 1,985 | — |
| 本地 sub | 1,419 | — |
| 本地合计 | 3,404 | 171,736,141 |
| 远端孤本既有救回副本 | 665 | 18,523,861 |
| 总计 | 4,069 | 190,260,002 |

本册只写可公开 READY 镜像，不列非公开件级账。R27 staging 预计 4,071 件，包含本外册与特殊根 README 各 1 件。

## 十二族 R5 主计

| 顺序 | 族 | READY 件数 | 实际上传件字节 | repo | sub |
|--:|:--|--:|--:|--:|--:|
| 1 | V3 | 193 | 8,559,324 | 103 | 90 |
| 2 | V4 | 162 | 8,514,982 | 30 | 132 |
| 3 | V5 | 98 | 2,827,924 | 49 | 49 |
| 4 | S3S4 | 105 | 3,145,514 | 60 | 45 |
| 5 | G-E01 | 49 | 1,638,706 | 47 | 2 |
| 6 | T | 75 | 2,689,128 | 64 | 11 |
| 7 | K-杀线 | 18 | 936,923 | 13 | 5 |
| 8 | ηETAC | 34 | 4,809,776 | 30 | 4 |
| 9 | T5择优 | 0 | 0 | 0 | 0 |
| 10 | 39词 | 3 | 148,630 | 3 | 0 |
| 11 | K-EXP8 | 9 | 531,011 | 9 | 0 |
| 12 | 委托面 | 84 | 1,609,495 | 67 | 17 |
| **实体族主计合计** | **十二族（T5 不重复）** | **830** | **35,411,413** | **475** | **355** |

T5择优为兼属视图，实体主计记 0 件／0 B；其两件已经计入 T。39词三件均 READY，上传字节分别为 measurement 41,623、judgement 54,594、prereg 52,413 B。

R26 独立验证为 PASS，READY 原始及上传 SHA-256 与 v11 snapshot SHA-256 的两类交集均为 0。规则检测不是未知敏感形态的数学穷尽；解析器不可见语义不作保证。

## FAMILY-01 · V3

**R1｜主题**：博弈论机制、判死协议、对抗与均衡分析及独立验证的记录族。

**R2｜做了什么**：R27 采用旧代表件 V3-01 位级判定，不以另一件产出层判定替换正式门禁证据。

**R3｜在册结论**：V3-01 位落 kd（known defects），对象是已辨明的四值不可识别缺陷；不是命题已死，也不代销记或宣告段毕。

**R4｜证据**：

- `R27-EVIDENCE-E01 | target=_repo_mirror/L1/V3/verdict/judgement/_v3_01_verdict_2026_10_28.md | source_sha256=4cb27e7352836d051ae6be505091ea5967e3a3d94428d889dde8a689db699e78 | sanitized_upload_sha256=4b399bf96b8aab9a09e996d64595b40b4b74980fd5dc9ceda58a99e5924dad4c | refs=R19 L560，R26-READY L354 | anchors=R19 源件 L1、L100–108；公开镜像对应段`

**R5｜实际 READY 体量**：193 件／8,559,324 B；repo 103／sub 90／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：只可外推至该位的缺陷面；不得扩张到 V3 全族、阻零清单其他位或任何命题存亡。

## FAMILY-02 · V4

**R1｜主题**：人类判断方法的蒸馏、探针与逐线判定记录族，目标是方法迁移而非行为画像。

**R2｜做了什么**：R27 保留 T1.5r2 判定中三条对象与门槛彼此独立的窄判词。

**R3｜在册结论**：K-N11-3 FAIL、K-N11-N1 FAIL、K-N11-N1_T1relax PASS；N=20 原线未过，放宽 N_min=10 的另一线通过。

**R4｜证据**：

- `R27-EVIDENCE-E02 | target=_repo_mirror/L1/V4/verdict/judgement/_v4_supp_t15r2_verdict.md | source_sha256=963725dbd82af674708c7ac97099726cf1d8c633b07da3024412277a0b72a0a1 | sanitized_upload_sha256=963725dbd82af674708c7ac97099726cf1d8c633b07da3024412277a0b72a0a1 | refs=R19 L676，R26-READY L397 | anchors=R19 源件 L42–57；公开镜像对应段`

**R5｜实际 READY 体量**：162 件／8,514,982 B；repo 30／sub 132／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可逐条引述三项判词及构造背景；不得合并成 V4 全族判词，也不得把放宽门槛的 PASS 写成原 N=20 门槛通过。

## FAMILY-03 · V5

**R1｜主题**：一个已命名方向的 SPEC 前置计划草案，不是已经启动的实验线。

**R2｜做了什么**：只整理方向、证据与措辞纪律、前置条件和决策点；目录名下可含跨线记录，须按各件卷首识别。

**R3｜在册结论**：未启动、未落终判；没有可据 READY 件数推出的新实验测量、结果或结论。

**R4｜证据**：无可公开代表证据三元组；未启动边界按根说明与计划草案口径保留，R5 只作目录标签门禁账。

**R5｜实际 READY 体量**：98 件／2,827,924 B；repo 49／sub 49／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可提计划草案和未启动边界；READY 件数与字节仅是该目录标签下的门禁体量，严禁据此宣称实验已跑。

体量释义：98 件／2,827,924 B 只对应目录标签的 R26 门禁结果，不是 V5 实验线启动或测量读数的证据。

## FAMILY-04 · S3S4

**R1｜主题**：S3／S4 采集与判读的分线记录族。

**R2｜做了什么**：R27 采用 S3 采集面三线终态，不以单一标签覆盖全族。

**R3｜在册结论**：K-V3S-3-1 与 K-V3S-3-2 PASS，K-V3S-3-3 为 KD；三线无 FAIL，且不外推命题面。

**R4｜证据**：

- `R27-EVIDENCE-E03 | target=_repo_mirror/L1/S3S4/verdict/judgement/_s3_kv3s_3_verdict_2026_10_01.md | source_sha256=e394bb6b5ddf55016860617253f3ce47beba6186744a4f9e55bc033a37db4422 | sanitized_upload_sha256=e394bb6b5ddf55016860617253f3ce47beba6186744a4f9e55bc033a37db4422 | refs=R19 L2640，R26-READY L2191 | anchors=R19 源件 L89–120；公开镜像对应段`

**R5｜实际 READY 体量**：105 件／3,145,514 B；repo 60／sub 45／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可提两项采集判据达成及一项已知缺陷；不得写成三线全部达标、判死线已清或 S3／S4 全族闭合。

## FAMILY-05 · G-E01

**R1｜主题**：G-E01 外部到位、实验就绪与相邻理论输入的记录面。

**R2｜做了什么**：R27 采用 2026-10-21 的到位判定建议件，区分事实复测、建议与 PI 裁决权。

**R3｜在册结论**：建议 G-5 外部到位闸未齐；该件未落到位终判、未宣告可开跑、未落五终判。

**R4｜证据**：

- `R27-EVIDENCE-E04 | target=_repo_mirror/L1/G-E01/verdict/judgement/_ge01_readiness_adjudication_2026_10_21.md | source_sha256=336500609b5cc59ff5b21dfc233e187d352af8dc3ca029ee44a71f67454dea20 | sanitized_upload_sha256=87dc84de69f36b55753d0a1773d2091a4df9193d891417d4544f35eec770fc24 | refs=R19 L304，R26-READY L108 | anchors=R19 源件 L1–19；公开镜像对应段`

**R5｜实际 READY 体量**：49 件／1,638,706 B；repo 47／sub 2／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可提候 PI 的就绪缺口及具体时点；不得把建议写成已生效裁决，也不得据此推称实验已完成。

## FAMILY-06 · T

**R1｜主题**：温度轴、构造分辨率、口径及相关消融的记录族。

**R2｜做了什么**：R27 采用 N-6 与 T-2 同件分位判定，并保留 T5 两件主记录在本族的归属。

**R3｜在册结论**：N-6 与 T-2 两位均落 kd，但对象层不同：前者是口径面缺陷，后者是载体与判准面缺陷；P_new 未验且未被证伪。

**R4｜证据**：

- `R27-EVIDENCE-E05 | target=_repo_mirror/L1/T/verdict/judgement/_n6_t2_verdict_2026_10_28.md | source_sha256=f582feeb797f1cde2ff582d82afb7d7562e6b12a23ce007e67b9213dacdf4d50 | sanitized_upload_sha256=7c4e79c9b81f804f2c2574595813a32a53a1feaad85e6ca1ab4f1f7f6c04d8fa | refs=R19 L420，R26-READY L220 | anchors=R19 源件 L1–27；公开镜像对应段`

**R5｜实际 READY 体量**：75 件／2,689,128 B；repo 64／sub 11／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：两位判词不得互相代替；不得由 T-2 的 kd 外推 P_new 不成立，也不得把 T5 预登记草案写成已开跑。

## FAMILY-07 · K-杀线

**R1｜主题**：判死线、阈值、估计量与测量前冻结纪律的记录族。

**R2｜做了什么**：R27 采用 KD-MDA-8 肢二测量面冻结草案，保留其候 PI 状态。

**R3｜在册结论**：草案立 K-MDA8A2-1…8、十四道依赖闸与十二项候裁位；对象域未裁则测量不可解释，且 0 实验、0 测量、0 新读数。

**R4｜证据**：

- `R27-EVIDENCE-E08 | target=_repo_mirror/L1/K-杀线/verdict/judgement/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md | source_sha256=b666077233c562441a8815ba01cd83a798e05c64c5d522f0b9e2e8f9b710e1f5 | sanitized_upload_sha256=7ae1ef523b80513cfa05a4213ab4f325efbcaaf1e3dd758e860741bda3e48118 | refs=R19 L324，R26-READY L128 | anchors=R19 源件 L1–17；公开镜像对应段`

**R5｜实际 READY 体量**：18 件／936,923 B；repo 13／sub 5／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可提草案构造及未决对象域；不得把候裁草案写成已生效、已施测或已有终判。

## FAMILY-08 · ηETAC

**R1｜主题**：η 面四档并列主实验及判据退化的记录族。

**R2｜做了什么**：R27 只采用主实验判定文书的候裁状态，不代替 PI 收口。

**R3｜在册结论**：四档并列主实验判定文书仍候 PI，未落五终判。

**R4｜证据**：

- `R27-EVIDENCE-E09 | target=_repo_mirror/L1/ηETAC/verdict/judgement/_kd_eta_main_run_verdict_2026_10_20.md | source_sha256=8a5727bc4c11889d8ef29db5cfce974c5bcac5ca7a711935229ff4efab31bb05 | sanitized_upload_sha256=8a5727bc4c11889d8ef29db5cfce974c5bcac5ca7a711935229ff4efab31bb05 | refs=R19 L764，R26-READY L476 | anchors=R19 源件 L1–9；公开镜像对应段`

**R5｜实际 READY 体量**：34 件／4,809,776 B；repo 30／sub 4／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可提判定文书存在与候裁边界；不得代 PI 落终判、关闭 KD 或宣告阶段完成。

## FAMILY-09 · T5择优

**R1｜主题**：T 主族下的择优跨属视图，不是另建的一套实体文件集合。

**R2｜做了什么**：R19 仅有两条跨属主记录，均主落 T、兼属 T5择优；R27 保留关系而不复制记录。

**R3｜在册结论**：两件在 R26 均 READY，但都只是待 PI 核准的预登记草案：基面二臂 K-T5B-1…20、构造三臂 K-T5C-1…25；两件均 0 实验、0 测量、0 读数。

**R4｜证据**：

- `R27-EVIDENCE-E06 | target=_repo_mirror/L1/T/work/process/_prereg_t5_baseface_two_arms_2026_10_23.md | source_sha256=7696699db2092ddc68a65943f60d0f34b5a23fb857614a69a14e5436c9b58017 | sanitized_upload_sha256=41470b23567a7eb4773a2269b278d81549f026e70e601e8d17d9278b2a300c8e | refs=R19 L440，R26-READY L240 | anchors=R19 源件 L1–20、L174–175；公开镜像对应段`
- `R27-EVIDENCE-E07 | target=_repo_mirror/L1/T/work/process/_prereg_t5_construction_three_arms_2026_10_23.md | source_sha256=2d240dfd504d3c22a828ff99b78d3ef43cfc4354547fa684eb7690e41a93ad32 | sanitized_upload_sha256=34f4d013e8261c8c77f6e31aa8da65e7d9ba00ce4aa9d702b6bdc602e4fc2185 | refs=R19 L441，R26-READY L241 | anchors=R19 源件 L1–20、L190–191；公开镜像对应段`

**R5｜实际 READY 体量**：0 件／0 B；repo 0／sub 0／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可公开两件草案的设计与未生效边界；不得预挑臂、代 PI 核准或宣称已开跑，且不得重复累计到 T 之外。

跨属对账：两件均主落 T 且已计入 T；本视图只展示两条公开证据，实体体量记 0 件／0 B，不复制、不重复加总。

## FAMILY-10 · 39词

**R1｜主题**：39词两读并存择优预实验的阅读、测量与判读材料。

**R2｜做了什么**：R27 采用判定收口件，并同时保留其构造／经验面与统计边界。

**R3｜在册结论**：18 条判死线无一违反，R36／R39 一致、D 非零，主读法落甲胜；分母 14／10／9，未做显著性检验。

**R4｜证据**：

- `R27-EVIDENCE-E10 | target=_repo_mirror/L1/39词/verdict/judgement/_judgement_w39_two_reading_2026_10_23.md | source_sha256=f35fe7d03551b2183063d80d98ac650c8b6205f29a08e82c334f999a2b7afd8c | sanitized_upload_sha256=abac0c1902c9de58d5a3cf09052e3a100e96a6ddb35948a6df00e14157c0a1b8 | refs=R19 L257，R26-READY L63 | anchors=R19 源件 L1–23、L68–97；公开镜像对应段`

**R5｜实际 READY 体量**：3 件／148,630 B；repo 3／sub 0／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：只可表述构造／经验面的机械读数落位；不是五终判或效力面结论，不作统计推断，不代 PI 裁权威面。

## FAMILY-11 · K-EXP8

**R1｜主题**：加权律、族权重与预实验择优设计的记录族。

**R2｜做了什么**：R27 恢复旧覆盖度裁决代表件，以其实际覆盖账替代候选拟案叙述。

**R3｜在册结论**：37 条中 23 条有逐条核、13 条前置未成就、1 条仅拟案无核；23 条中实测读数核为 0。

**R4｜证据**：

- `R27-EVIDENCE-E11 | target=_repo_mirror/L1/K-EXP8/verdict/judgement/_kexp8_coverage_adjudication_2026_10_22.md | source_sha256=80631fb4ce3df7356a101b6372c561ba13e811a5330b9ad01a93d7082eee338c | sanitized_upload_sha256=4ba0623b0a1a0c0eb20497aee3afecce6b4a05c537ebd0785a6912e88453e000 | refs=R19 L315，R26-READY L119 | anchors=R19 源件 L1–16；公开镜像对应段`

**R5｜实际 READY 体量**：9 件／531,011 B；repo 9／sub 0／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可提覆盖账及实验收束缺口；不得把纸面演算／合规比对写成实验核，也不得宣称①毕或可开跑。

## FAMILY-12 · 委托面

**R1｜主题**：受托执行、回执、引用路径与权源核验的记录面。

**R2｜做了什么**：R27 采用 2026-10-18 第三批历史执行回执，只复述该时点记录。

**R3｜在册结论**：原回执登记改名、拉回、删除与分批传输及 HEAD 链；它是历史执行记录，不是本轮动作或当前远端状态。

**R4｜证据**：

- `R27-EVIDENCE-E12 | target=_repo_mirror/L1/委托面/verdict/judgement/_batch3_execution_receipt_kimi_2026_10_18.md | source_sha256=10a3b36859d7958177c666cb56eeb052617806f15ba82bcfa387544092460c83 | sanitized_upload_sha256=f42d8baf6a5e62bc24db2262f8e30d42f4ba250bbb0d48430f5512a3a558e2cb | refs=R19 L829，R26-READY L526 | anchors=R19 源件 L1–18；公开镜像对应段`

**R5｜实际 READY 体量**：84 件／1,609,495 B；repo 67／sub 17／远端孤本 0。按 R26 READY 的 upload_bytes 重算。

**R6｜可提／须隐边界**：可提历史时点与原回执字面；不得据此推断当前远端实时状态，也不得把历史回执当成本轮上传授权。

## 交付边界

本册只提供公开 READY 镜像的十二族节点叙述和十二条代表证据，不提供非公开件名或内部状态附录。任何 READY 体量都不表示已获得上传授权或已经落远端。

内部册与 4,710 条全量索引只留工作区，不进入上传树；特殊根 README 另行登记完整门禁总账。

