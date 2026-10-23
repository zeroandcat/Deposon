# 查理 · 第三作 v0.1 联动换锚清单（FTFB R4 更新触发，2026-09-27）

- **用途**：FTFB 更新版（R4，`4f8c4231`，本包 `fiction_that_feeds_back.tex`）落库/解 hold 后，第三作合并稿（`_v3v4_merged_paper_2026_09_27_v0.1.md`）的换锚与口径同步作业单——**交 v0.2 修订轮一并处理**，本轮只登记不执行。
- **触发条件**：① R4 版 arXiv 重投提交（解 hold 生效日）；② 仓内归档三件同位刷新落库（新 SHA/字节/页数实测日）。两者任一发生即按本清单执行；均未发生前 v0.1 现锚继续有效（`2D9EDC8C7303` 在 a57d7fe 实测在位，本清单已核）。
- **纪律预告**：换锚只动锚值与状态口径句；正文论述、数字、判定零改动；触发器条款（§22.3/limitations 注）按注册表既有口径执行。

## 一、换锚位点总表（v0.1 全稿穷尽检索：`second work`/`Fiction That Feeds Back`/`2D9EDC8C7303`/`on hold`/`_archive_2026_09_20/fiction`）

| # | v0.1 行号 | 位点类型 | 现文（关键句） | 换锚动作 |
|---|---|---|---|---|
| S1 | L34（§1.2 口径句） | §1.2 状态＋锚 | 「*Fiction That Feeds Back…*, 23 pp.; submitted to arXiv and, as of the writing day (2026-09-27), on hold; on-disk anchor `results/_archive_2026_09_20/fiction_that_feeds_back.pdf`, 356,123 B, SHA-12 `2D9EDC8C7303`, measured 2026-09-26, writing-day freeze; an updated version is in preparation on the PI's side, so this digest will change, and the citation will be upgraded to the formal arXiv record upon public release」 | ①状态句：解 hold 生效后改「updated edition (R4) submitted to arXiv on 2026-09-27 in resolution of the hold; status per the arXiv record」；②锚行：换归档刷新后新值（字节/SHA-12/页数＝**待落库实测**，见槽位表）；③「更新版在制…digest will change」句**退役**（触发器已执行）；④锚路径补全仓相对全径 `_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.pdf`＋可加公开仓指针（github.com/zeroandcat/Deposon @ a57d7fe 引用冻结口径） |
| S2 | L636（§16.3 limitations 注(5)） | 触发器条款 | 「Companion-work citations are frozen at writing-day digests; the second work's update will change its digest, and its formal publication record, if any, supersedes the internal citation.」 | 触发条款执行：换新摘要值＋注明历史值沿革（writing-day `2D9EDC8C7303`→新值）；「will change」改完成时态或整句改「was updated (R4, 2026-09-27); the formal publication record, if any, supersedes the internal citation」 |
| S3 | L652（§22.3 source face） | 「不可达」表述 | 「The two archive-resident items…exist on the local disk and are outside the upload face: the second work is anchored in this paper at its local on-disk value only, and a reader relying on the upload face alone cannot reach it.」 | 与公开现实对齐：R4 版已将五锚/数字源件/源稿/重算件/归档三件的公开面锚定在 github.com/zeroandcat/Deposon@a57d7fe（FTFB 附录 availability terms）；「cannot reach it」句改「a reader relying on the public repository can reach the second work's frozen record at the cited commit」或按 PI 对「upload face」概念的口径裁定后重述（差异清单 §4.2-L2 同源指令） |
| S4 | L890（App A 行 47） | App A FTFB 锚 | 「`results/_archive_2026_09_20/fiction_that_feeds_back.pdf` (second work, 23 pp., writing-day freeze; the second work is submitted and, as of 2026-09-27, on hold; an updated version is in preparation on the PI's side and the digest will change) \| 356,123 \| 2D9EDC8C7303」 | 行值整体替换：新路径（全径）/新字节/新 SHA-12/新页数（**待落库实测**）；状态括注改 R4 已更新＋解 hold 状态；「writing-day freeze」沿革注明（历史值 2D9EDC8C7303 可留沿革注） |
| S5 | L968（App C 注册表 R1） | 工作序列注册 | 「second work (FTFB, submitted and on hold)」 | 「submitted and on hold」→「updated edition (R4) resubmitted 2026-09-27; hold status per arXiv record」 |
| S6 | L972（App C 注册表 R5） | **References 相应条目**（第二作引用形式注册） | 「cited at the writing-day frozen digest (356,123 B, 2D9EDC8C7303) with the status "submitted, on hold" recorded once (Section 1.2 and Appendix A); an updated version is in preparation on the PI's side; the digest will change; the citation will be upgraded upon formal publication.」 | R5 注册值整体改写：新冻结摘要值＋状态「R4 resubmitted (2026-09-27)」＋「升级触发器已执行」注明；正式 arXiv 标识符落位后（§5-③ 输入）再升正式引用 |
| S7 | L301（§4.1 提及） | 纯提名（无锚无状态） | 「instantiated as the second companion work, *Fiction That Feeds Back*.」 | **无需换锚**（登记备查，防 v0.2 漏检时误改） |

**References 编号条目说明**：v0.1 引用池 64 条中**无第二作编号条目**（第二作以 §1.2 锚引＋App A 行引用，非 References 编号项；编号池中的匿名 companion 条目属**第一作**，与本次 FTFB 更新无涉、不动）——「References 相应条目」的联动对象即上表 S6（R5 注册条目，引用形式的家）。

## 二、新值槽位（待落库实测填入）

| 槽位 | 来源 | 状态 |
|---|---|---|
| 新归档 PDF：字节/SHA-12/页数 | 排版轮 pdflatex 编译 R4 tex 后归库实测 | **pending**（R3 面 24 页 408,781 B；R4 净增约 3 KB 文字，预计 24 页） |
| 新归档 tex：字节/SHA-12 | 若按本包 R4 tex 原样归档＝101,928 B / `4f8c42319603`（SHA-256 全值见修订记录） | 已知（视 PI 归档面决定是否原样采用） |
| 新归档 source：形态与指纹 | 待 PI 裁定（R4 版源形态：tex 为源或另制 md） | **pending** |
| arXiv 标识符/版本号 | 重投受理后 | **pending**（差异清单 §5-③） |
| 解 hold 生效日 | arXiv 侧 | **pending** |

## 三、执行纪律（v0.2 轮）

1. 换锚前先实测仓内新值（sha256sum＋stat），不从本清单预测值落文；
2. 状态口径句以 arXiv 实况为准（若 hold 未如期解除，S1/S4/S5/S6 状态句按实况改写，不预写「已解」）；
3. 历史值沿革（356,123 B / 2D9EDC8C7303 / 23 pp.）在 App A 行与 R5 注册表保留一次沿革注记（沿 E-15 勘误链先例：注明历史值、判定件沿革、不回改历史记载）；
4. S3「不可达」句改写前需 PI 对「upload face」概念与公开仓现实的口径拍板（13 件 archive-resident 的治理口径 vs 可达性口径）；
5. 全部动作登记入 v0.2 修订记录，AI 生成落款。

—— 查理-论文主笔 ｜ 2026-09-27 ｜ AI 生成
