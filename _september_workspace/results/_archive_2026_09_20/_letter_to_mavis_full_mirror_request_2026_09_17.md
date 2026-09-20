# 「完备一致」全量镜像申请

**致**：Mavis（项目统筹）、用户本人
**自**：KIMI 凝子-agent
**日期**：2026-09-17
**主题**：申请授权将 GitHub 仓 `zeroandcat/Deposon`（`main`）与本地 canonical 仓 `D:\私人资料\deposon-repo\` 做成「完备一致」镜像

## 一、目的与背景

deposon 守恒账 / 博弈论化研究已收束，终稿中英双版双审 PASS 已交付。此前已由 KIMI 完成三批安全推送（commit bb1f085f 10 件、5dd8221b 55 件、ee0b82fc 48 件，及 manifest 镜像 commit 292ba94d），三批均核验 ALL_PASS；当前 GitHub HEAD 为 `292ba94dd5d5843dd78d8edff79deec86e34f794`。现申请授权执行全量镜像，使两端达「完备一致」。既定红线不变：完整论文永不推 GitHub（仅推 PAPER_BRIEF），PNG 二进制由用户侧推送。

## 二、现状盘点

2026-09-17 22:02 CST 全量 diff（脚本 `mirror_diff.py`，tree 未截断）：

| 项 | 件数 |
| --- | --- |
| 远端 blob | 875 |
| 本地文件 | 1044 |
| 一致 | 244 |
| 内容不同（changed） | 19 |
| 本地独有（local_only） | 781 |
| 远端独有（remote_only） | 612 |

changed + local_only 合计 70,081,464 字节（约 66.8 MiB）。

## 三、镜像范围提案

口径定义（用户裁决）：「完备一致」= 文件内容级双向一致：以 git-SHA1 判定，任一文件内容在另一端可找到即一致，不要求目录结构 / 路径对应。

### A. 推送：可推集合 442 件 / 15.5 MiB

按内容口径拆为：**必推 282 件 / 10.4 MiB**（内容远端缺失，含全部 14 件 changed；topdir：results 102、deposon_team 43、corpus 23、docs 23、.trae 19、reviews 16、scripts 10、attacks 4、tests 3、tools 3，仓根散落 36 件）与**可选推 160 件**（内容经 kill 快照等他径远端已有；价值在恢复 canonical 路径便于审计，见决策点 4）。清单见工作区 `_mirror_pushable.json`。

下表仍按 442 件全量描述（路径口径）：

| 维度 | 分布 |
| --- | --- |
| 扩展名 | .json 173、.py 140、.md 99、.csv 15、.txt 7、.ps1 5、.sh 1、.jsonl 1、.note 1 |
| 顶层目录 | results 173、docs 85、deposon_team 69、corpus 24、.trae 19、reviews 16、scripts 10；其余 46 件为仓根散落脚本及 1–4 件小目录（attacks 4、tests 3、tools 3 等） |

changed 可推 14 件点名：`RELEASE_v1.4.0.md`、`audits_dataset_health.json`、`audits_security.json`、`docs/Findings_v2.0_corrections.md`、`docs/Findings_v2.0_crossval.md`、`docs/PAPER_BRIEF.md`、`docs/space_release_log.json`、`reviews/literature_scan_v2X_A.md`、`run_benchmark_v1_4_gsm8k.py`、`run_v20_baselines.py`、`run_v20_bigquiz_eval.py`、`run_v20_familyL_ingest.py`、`run_v20_fastcheck.py`、`run_v20_photonics.py`。

### B. 排除：358 件，六类

| # | 类别 | 件数 | 大小 |
| --- | --- | --- | --- |
| 1 | 垃圾 / 缓存 / 临时（log/tmp/bak/cache/err/flag/aux/out、probe、sanity、__pycache__、_worker_temp） | 219 | 2407.8 KB |
| 2 | PNG（铁律：PNG 二进制由用户侧推送） | 74 | 20382.8 KB |
| 3 | Trae 论文构建残留（.trae/build、.trae/source、.trae/snapshots 下：快照脚本 py 15、README.md 4、references.bib 5、verify_report.txt 1；tex 见第 5 类） | 25 | 210.0 KB |
| 4 | 完整论文红线（paper/ 全目录） | 21 | 11946.4 KB |
| 5 | 论文二进制 / 源（pdf/tex/tar.gz，散落 paper/ 之外，如 .trae/audit 编译证据） | 14 | 16772.8 KB |
| 6 | 历史排除项（PHASE_B_TMP、strategyqa_train.json 等） | 5 | 842.1 KB |

其中红线 changed 5 件（默认不推）：`paper/deposon_paper_final_cn.md`、`paper/deposon_paper_final_en.md`、`paper/deposon_paper_v1.md`、`paper/deposon_paper_v1_en.md`、`paper/references.bib`。

### C. 远端独有 612 件：按内容口径重分

612 = 246 已一致 + 366 内容独有。

| # | 范围 | 件数 | 处置提案 |
| --- | --- | --- | --- |
| ① | 内容本地已有（kill 184、verifier 61、other 1） | 246 | 新口径下已一致，无需动作 |
| ② | 内容独有：kill 215（179 路径独有 + 36 同路径旧版/分歧版）、verifier 38、other 113（含 paper/v2 4 件、docs/V3X/KIMI_D05 与 GLM 两件 2026-09-17 提案、docs 旧 SPEC/Roadmap/验证报告 11 件、results 旧 json 与 cache 96 件中独有部分等） | 366 | 回拉本地（GitHub→本地，只读远端、不改远端），或明示豁免；提交决策点 3 |

路径口径对照（以内容口径为准）：verifier/ 99、v3x-1week-kill-2026-09-18/ 399、其余 114。

kill 399 件路径口径：同路径同内容 178（纯冗余）；同路径内容不同 36（kill 存旧版/分歧，如 `deposon_team/plugins/_verify_15frozen.py`、`docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md`、`results/deposon_embedding_dual_2026_09_10.json`）；异路径同内容 6；内容独有 179 = docs 114 + results 64 + .gitattributes 1（多为 V3X 实验文档与结果，如 D7_ONE_PAGE_SUMMARY、DEEPSEEK_V41_FLASH、EMBEDDING_VISION_STRATEGY 系列）。映射：178+6=184 已一致，179+36=215 独有。

## 四、重大决策点

**决策点 1：完整论文远端遗留 4+1 件。** 上述 4 个完整论文 md 及 `references.bib` 已存在于 GitHub 远端（历史批次遗留），本次 diff 显示本地版本已有更新（changed）。铁律 7 规定完整论文永不推 GitHub。请裁决：

- (a) 冻结远端现状，不更新；
- (b) 从远端移除该 4+1 个文件（destructive，需明确批准）；
- (c) 例外授权，推送本地更新版。

起草者不持倾向，仅陈述选项；未获明确批准前，对远端这些文件不做任何变更。

**决策点 2：v3x-1week-kill-2026-09-18/ 399 件去留。** 新口径下 184 件已一致，不受去留影响；215 件内容独有（179+36）须先回拉本地再议删除。默认保留归档；删除属 destructive，须明确批准。

**决策点 3：内容独有 366 件回拉。** 批准回拉内容独有 366 件（verifier 38 + kill 215 + other 113）回本地 canonical 仓，或指示分档 / 豁免范围。回拉为 GitHub→本地只读远端操作，不改远端，不涉铁律 7 推送红线（paper/v2 4 件亦仅回拉本地）。

**决策点 4：可选推 160 件。** 内容远端已有；价值在恢复 canonical 路径便于审计——推或不推。

## 五、执行方案与核验方法（获批后）

1. 分批推送，每批 ≤50 件：必推 282 件按目录切分，可选推 160 件获批后另排。
2. 每批走 git-data API（blob→tree→commit→ref PATCH，非 force）。
3. 每批推后 `GET git/trees/<commit>?recursive=1` 做 git-SHA1 全量比对核验（contents API 对 >1MB 文件返回空 content，核验必须用 tree 比对）。
4. 每批写 manifest 镜像入 `results/`。
5. 推送前对候选文件做密钥扫描；正则必须泛化，绝不写入真实密钥片段（历史教训：check.sh 曾因写入真实密钥片段自身泄漏）。
6. frozen 工件绝不触碰；任何重跑审计在 /tmp 副本执行。
7. API key 永不落盘、永不进提示词。

## 六、红线合规自检表

| 红线 | 自检结论 |
| --- | --- |
| 完整论文不推 GitHub | 符合：paper/ 全目录排除；远端遗留 4+1 件提交裁决，未擅自处理 |
| PNG 由用户侧推送 | 符合：74 件 PNG 全部排除 |
| 密钥扫描正则泛化 | 符合：扫描规则不含、亦不写入真实密钥片段 |
| frozen 工件不触碰 | 符合：重跑审计仅在 /tmp 副本执行 |
| manifest 入库 | 符合：每批 manifest 镜像写入 results/ |
| 术语红线 | 符合：本函不涉及受限术语；相关表述一律按既定口径 |

## 七、请求裁决清单

- [ ] 批准必推 282 件 / 10.4 MiB（内容远端缺失，含全部 14 件 changed；分批 ≤50）。
- [ ] 决策点 4：可选推 160 件（恢复 canonical 路径、便于审计）——推或不推。
- [ ] 确认排除集合 358 件（六类口径，含 PNG 74 件与 paper/ 21 件）。
- [ ] 确认 246 件内容远端已有，新口径下已一致，无需动作。
- [ ] 决策点 1：完整论文远端遗留 4+1 件——(a) 冻结 / (b) 移除 / (c) 例外更新，请择一。
- [ ] 决策点 2：kill 399 件——184 件已一致不受影响；215 件独有先回拉再议删除；默认保留归档。
- [ ] 决策点 3：批准回拉内容独有 366 件（verifier 38 + kill 215 + other 113），或指示分档 / 豁免。
- [ ] 批准执行方案与核验方法（git-data API 非 force、tree 比对核验、manifest 入库）。

## 八、溯源附录

- 数据源 1：`C:\Users\Administrator\Documents\kimi\tasks\2026-08-31\05-20-23-c0a47add\_mirror_diff.json`（全量 diff 输出；脚本 `mirror_diff.py`；diff 时间 2026-09-17 22:02 CST；tree 未截断）
- 数据源 2：`C:\Users\Administrator\Documents\kimi\tasks\2026-08-31\05-20-23-c0a47add\_mirror_pushable.json`（可推 442 件清单）
- 数据源 3：`C:\Users\Administrator\Documents\kimi\tasks\2026-08-31\05-20-23-c0a47add\_kill_analysis.json`（kill 目录 399 件四分类核查；方法：剥前缀按路径 + git-SHA1 内容比对；核查时间 2026-09-17 22:55 CST）
- 数据源 4：`C:\Users\Administrator\Documents\kimi\tasks\2026-08-31\05-20-23-c0a47add\_remote_only_content_analysis.json`（612 件内容口径重分；方法：git-SHA1 内容比对；时间 2026-09-17 23:05 CST）
- 数据源 5：`C:\Users\Administrator\Documents\kimi\tasks\2026-08-31\05-20-23-c0a47add\_pushable_content_split.json`（442 件必推 / 可选拆；方法：git-SHA1 内容比对；时间 2026-09-17 23:05 CST）
- GitHub HEAD：`292ba94dd5d5843dd78d8edff79deec86e34f794`
- 声明：本函每个数字均可在上述 JSON 中复算。
