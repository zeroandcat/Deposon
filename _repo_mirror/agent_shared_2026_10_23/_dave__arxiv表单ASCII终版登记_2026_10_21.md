# arXiv 表单元数据 ASCII 终版 · 戴夫独立复核登记

- 登记时刻：2026-10-21 00:24（Asia/Shanghai）
- 派单：群管理员 00:11:08「独立复核快检（PI 00:08 催速·单轮交付）」；PI 00:12:12 增补指令「Comments 不需要这么多要点」→ 处置见 §五（待 PI 择一）
- 复核对象：`shared/查理_arxiv表单ASCII修复_2026_10_20/arxiv_metadata_oneline_R6F18_ASCII_2026_10_20.txt`（表单粘贴正本）＋查理 00:09:38 群内直贴（同文）
- **结论：PASS——28 项实测全过（其中 P2 系首轮 glob 漏扫，已于归档正本＋外层 zip 包内件双位补验一致），定终版。PI 直贴源＝群内 00:09 直贴版，与终件同文（程序化逐字节一致，差仅文件末单个换行）。**
- **v2 轮（00:28 派单·PI 00:22 裁定「对标第一作」）后：现行表单粘贴正本＝v2 终件（见 §六）；v1 `3f0dd8095353` 转沿革留档。**

## 一 指纹链

| 件 | 路径 | SHA-256（全值） | 字节 |
|---|---|---|---|
| 源件（前态·留档勿贴） | shared/arxiv_metadata_oneline_R6F18_2026_10_20.txt | ff335b6143b4c150a5f8ca08c00a34530ef28d8005717660a327c1ca751b4635 | 2,584 |
| 终件 v1（00:09–00:28 粘贴正本·沿革留档） | shared/查理_arxiv表单ASCII修复_2026_10_20/arxiv_metadata_oneline_R6F18_ASCII_2026_10_20.txt | 3f0dd809535333894cc6bac0e5aaa0079b858600d1a32d3cd79bd169e558d047 | 2,515 |
| **v2 终件（现行表单粘贴正本）** | shared/戴夫_arxiv表单ASCII终版v2_2026_10_21/arxiv_metadata_oneline_R6F18_ASCII_v2_2026_10_21.txt | e580a9a0ef269b8fbdc18c4cf347878e1939c0fe405b10d864093aa34aadf40e | 2,279 |

## 二 独立复核读数（程序化实测；脚本 `agents/6a962cc259312f271f3f1e75/arxiv_ascii_verify_20261021/`）

1. **Abstract 1,881 字符**（源 1,877，Δ+4 全自 §7.4→Sec. 7.4）；纯 ASCII（—/–/§ 全零）；**措辞零漂移双证明**：①映射重放（—×6/–×1→"-"、§7.4→"Sec. 7.4"）输出与终值逐字符一致；②SequenceMatcher 逐字符 diff 恰 8 处非等块（—→"-"×6、–→"-"×1、§→"Sec. "×1）无第 9 处差异；≤1,920 硬限**余 39**。
2. **Comments 387 字符**（源 443）；纯 ASCII；≤400 硬限**余 13**；8 要点在场 8/8（31 pages／R6 edition／philosophical-register restructure／lineage R3 -> R4 -> R5, submission suspended -> R6／argument-first order＋falsifiability verdicts stated before the runs＋Sec. "The first action: verdicts before the runs"／abstract rewritten to the same register／measurement anchors＋reference pool unchanged／(66 entries)）。
3. **其余 6 字段**（Title 74／Authors 10／Subjects 39／License 9／Conflicts of interest 13／Date 10 字符）与源件 ff335b6143b4 逐字节一致。
4. **一行形态**：恰 8 行无空行、字段序与源件一致；每行「字段名: 值」、值内零换行；行/值无首尾空格、值内无双空格；CR/TAB/BOM 全零；零宽（U+200B/200C/200D/FEFF）与 U+FFFD 全零；全文纯 ASCII（最大码点 122）；文件末单个换行（与源件同制）。
5. **群内直贴同文**：查理 00:09:38 直贴 8 字段行与终件主体逐字节一致（2,514 B＋末单个换行）。

## 三 0 重打包承诺实测（提交件零改动）

- 外层运输 zip `f871ea04177d`（1,481,997 B·完整 11 件版）现盘指纹一致；
- F18 tar.gz `fbef35366d80acdd70cf98b0b05aa750f818b0be528e286fec87da3c905cb93c`（484,717 B）双位复核一致：`归档_F18targz_fbef3536/` 正本＋外层 zip 包内件；
- 精简夹/打包目录 `arxiv_metadata.txt` `b53ca46f3759`（分段式原件）两处现盘一致——**包未重打、包内 aux 件零改动**。

## 四 步骤单读数联动 · 差量登记（包内步骤单零改动，以本登记为准）

| 步骤单在册读数（`戴夫_R6一杆进洞提交步骤单_2026_10_20.md`·外层 zip 内） | 终版联动读数（表单粘贴值以此为准） |
|---|---|
| L29 metadata 件 `b53ca46f3759` 全字段 paste 就绪 | 粘贴源 → **ASCII 终版 `3f0dd8095353`**（b53ca46f 系分段式原件留档、包内不动） |
| L37 Abstract 1,877 字符 | → **1,881**（纯 ASCII 化＋Sec. 7.4，硬限余 39） |
| L30/L36 Comments 按件原样粘贴 | → **387**（压缩＋纯 ASCII，硬限余 13）；PI 00:12 指示要点精简，待择（§五） |
| L10 tar.gz 指纹 fbef35366d80…93c | 不受影响（0 重打包实测一致） |
| L49 Comments「31 pages」复测终值 | 31 pages 在场（V1–V3 三档候选均含） |

## 五 PI 00:12:12 增补指令 · Comments 要点精简（待 PI 择一）

现值 387 字符含 8 要点；PI 指示「不需要这么多要点」。三档纯 ASCII 直贴候选（程序化计数、均远低于 400 限）：

| 档 | 值 | 字符 |
|---|---|---|
| V1（R5 先例「29 pages R5 edition」同款） | `31 pages; R6 edition` | 20 |
| V2（+一句变更性质） | `31 pages; R6 edition (argument-first restructure)` | 49 |
| V3（+唯一实质不变性声明） | `31 pages; R6 edition (argument-first restructure); measurement anchors and reference pool unchanged (66 entries)` | 112 |

PI 择一（或直接给字面）→ 即出一行版 v2 终件：仅 Comments 行替换、其余 7 行逐字节沿用、全套合规检查重跑＋新指纹重登记，仍 0 重打包。未择前，现行终版 `3f0dd8095353` 与查理 00:09 群内直贴均为有效粘贴源。

**裁定（00:28 派单转达 PI 00:22）：「对标第一作即可」——弃三档候选，Comments 改第一作 v1 同款极简款，出一行版 v2（见 §六）。**

- 备注：shared 根下源一行版 `ff335b6143b4` 留档为历史前态，勿作粘贴源。

## 六 v2 终件 · PI 00:22 裁定「Comments 对标第一作」（00:28 派单，登记时刻 2026-10-21 00:34）

- 裁定链：PI 00:12「Comments 不需要这么多要点」→ §五三档候选 → **PI 00:22「对标第一作即可」弃三档**；tex 零改动。
- 第一作基准（2609.09001 v1）：`23 pages, 5 figures. Author affiliation: School of Chemistry and Life Resources, 〔高校R〕 University of China. Code: <裸URL>`（双源：鲍勃共享取证报告 L108——Author＝Qihao Yuan、Comments 前缀「23 pages, 5 figures…」、仅 v1；全文按 00:28 派单引用，取证原件在鲍勃私有目录未越权访问；abs 渲染层末项「this https URL」系 arXiv 文案，表单实际输入＝裸 URL）。
- 我稿替换要素（逐项实测）：**31 pages**＝compile_verification L23/L64/L67/L70 复测终值；**5 tables**＝tex `\begin{table}` ×5；**0 figures**＝tex `\begin{figure}` ×0＋`\includegraphics` ×0（figures 位→tables）；affiliation 行照搬第一作（同作者 Qihao Yuan）；**Code＝`https://github.com/zeroandcat/Deposon`**＝tex L362/L555 `\url{…}` 原文裸仓 URL（与派单建议一致）。
- **v2 Comments 值（151 字符纯 ASCII·≤400 余 249）**：`31 pages, 5 tables. Author affiliation: School of Chemistry and Life Resources, 〔高校R〕 University of China. Code: https://github.com/zeroandcat/Deposon`
- v2 终件：`shared/戴夫_arxiv表单ASCII终版v2_2026_10_21/arxiv_metadata_oneline_R6F18_ASCII_v2_2026_10_21.txt`（SHA-12 `e580a9a0ef26`·2,279 B·全值 `e580a9a0ef269b8fbdc18c4cf347878e1939c0fe405b10d864093aa34aadf40e`）；仅 Comments 行替换、其余 7 行与 v1 `3f0dd8095353` 逐字节一致（Abstract＝1,881 纯 ASCII 不动）；行形态全套检查重跑全过（8 行/值内零换行/无首尾空格/无 CR·TAB·BOM/零宽·FFFD 全零/末单个换行）。
- **现行粘贴源＝v2 终件＋本轮群内直贴（同文）**；Comments 值沿革链：F18 分段式 443（b53ca46f）→ 一行版 443（ff335b6143b4）→ ASCII v1 387（3f0dd8095353）→ **v2 对标第一作极简款 151（本件）**。
- 步骤单联动读数（L30/L36「Comments 按件原样粘贴」）→ 现行值＝v2（差量以本登记为准）；0 重打包实测复核：外层 zip `f871ea04177d`、F18 tar.gz `fbef35366d80`（归档正本＋外层 zip 包内件）、aux `b53ca46f` 指纹均一致、包内件零接触零改动；tex 零改动。

