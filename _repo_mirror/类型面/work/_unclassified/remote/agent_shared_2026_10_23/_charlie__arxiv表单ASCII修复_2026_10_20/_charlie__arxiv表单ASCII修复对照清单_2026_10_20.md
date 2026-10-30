# arXiv 表单元数据 ASCII 合规值 · 替换/压缩对照清单（R6F18）

- 主笔：查理（论文主笔）· 2026-10-20 深夜轮（派单：群管理员 23:53；触发：PI 23:49 arXiv 提交表单报错截图）
- 范围纪律：**仅表单粘贴值**——本清单与一行版终件两个新件；源一行版／tex／PDF／一切既有件**零改动**
- 接力：戴夫独立复核出终版一行件 → PI 拿终值直贴表单

## 〇 基准与根因复核（本轮实测，与派单一致）

| 项 | 值 |
|---|---|
| 源件（只读零改） | shared/arxiv_metadata_oneline_R6F18_2026_10_20.txt |
| 源件指纹 | SHA-256 前 12 位 `ff335b6143b4` · 2,584 B · 8 字段行（每行「字段名: 值」） |
| PI 报错（截图） | Abstract「Bad character(s)」×7；Comments「cannot be longer than 400 characters」；Comments「Bad character(s)」×1 |
| 根因实测 | Abstract 值 1,877 字符、非 ASCII 8 处（— U+2014 ×6／– U+2013 en dash ×1／§ U+00A7 ×1）；Comments 值 443 字符（超 400 硬限 43）＋非 ASCII 1 处（— ×1） |
| 报错 7 vs 实测 8 | 报错 7 条恰合 —×6＋–×1；§ 疑似放行（管理员 23:53 口径）。本轮统一纯 ASCII 化：8 处全替换，任一计数口径下均归零 |

注：Abstract 源值即 F18 终值（此前轮交付，与 R6 tex 摘要区同源）；本轮零措辞改动。

## 一 Abstract：字符级替换（措辞零改动）

映射（3 条）：

| 非 ASCII | 码点 | 处数 | ASCII 等价 |
|---|---|---|---|
| —（em dash） | U+2014 | 6 | `-`（前后空格原样保留：` — ` → ` - `） |
| –（en dash） | U+2013 | 1 | `-`（M1–M5 → M1-M5） |
| §（section sign） | U+00A7 | 1 | `Sec.`（§7.4 → Sec. 7.4） |

逐处定位（8 处，按旧值字符位升序；旧片段在旧值唯一、新片段在新值唯一）：

| # | 旧值字符位（0 起） | 旧片段 | 新片段 |
|---|---|---|---|
| 1 | 180 | `four channels — formal` | `four channels - formal` |
| 2 | 226 | `narrative — separate` | `narrative - separate` |
| 3 | 991 | `(M1–M5)` | `(M1-M5)` |
| 4 | 1140 | `structural parallel — criteria` | `structural parallel - criteria` |
| 5 | 1251 | `declared as such — and` | `declared as such - and` |
| 6 | 1279 | `pipeline — setting` | `pipeline - setting` |
| 7 | 1334 | `experiment — ports` | `experiment - ports` |
| 8 | 1871 | `(§7.4)` | `(Sec. 7.4)` |

字符数前后账：
- **1,877 → 1,881**（Δ+4，全部来自 §7.4（4 字符）→ Sec. 7.4（8 字符）；—／– 均为 1:1 逐字符替换，不改计数）
- 硬限 ≤1,920：达标，余量 39；建议 ≤1,890：达标
- 修复后非 ASCII 0；换行／\r／控制符／零宽字符 0（逐字符扫描）
- 措辞零改动证明：新值 = 旧值仅经上述 3 条 replace 生成（脚本计数 assert 6/1/1 在案），除 8 处字符替换外逐字节一致

## 二 Comments：压缩 443 → 387（纯 ASCII，语义零损）

旧值（443 字符；—×1 位于字符位 168）：

> 31 pages; R6 edition (philosophical-register restructure; version lineage R3 -> R4 -> R5, submission suspended -> R6): the argument order is reversed to argument-first — the falsifiability verdicts are stated before the runs (Sec. on "The first action: verdicts before the runs"); the abstract rewritten to the same register; the argumentative register deepened throughout; measurement anchors unchanged, reference pool unchanged at 66 entries

新值（387 字符；非 ASCII 0；硬限 ≤400 达标余 13，建议 ≤395 达标）：

> 31 pages; R6 edition (philosophical-register restructure; version lineage R3 -> R4 -> R5, submission suspended -> R6): argument-first order, falsifiability verdicts stated before the runs (Sec. "The first action: verdicts before the runs"); abstract rewritten to the same register; argumentative register deepened throughout; measurement anchors and reference pool unchanged (66 entries)

压缩对照（5 处，旧→新；其余字符逐字沿用。**重组回放证明**：5 处替换依次施加于旧值，输出 == 新值，即 5 处完整覆盖全部差异）：

| # | 旧片段 | 新片段 | 字符数·处置 |
|---|---|---|---|
| 1 | `the argument order is reversed to argument-first — the falsifiability verdicts are stated before the runs` | `argument-first order, falsifiability verdicts stated before the runs` | 105 → 68（净 -37）· 删倒装冗语「the argument order is reversed to」；em dash → 逗号；删 the／are |
| 2 | `(Sec. on "The first action: verdicts before the runs")` | `(Sec. "The first action: verdicts before the runs")` | 54 → 51（净 -3）· 删介词 on |
| 3 | `; the abstract rewritten` | `; abstract rewritten` | 24 → 20（净 -4）· 删分句冠词 the |
| 4 | `; the argumentative register deepened` | `; argumentative register deepened` | 37 → 33（净 -4）· 删分句冠词 the |
| 5 | `measurement anchors unchanged, reference pool unchanged at 66 entries` | `measurement anchors and reference pool unchanged (66 entries)` | 69 → 61（净 -8）· 两个 unchanged 合并共享一个；「at 66 entries」→「(66 entries)」 |

字符数前后账：**443 → 387**（净 -56）。

要点保全核对（8/8 全保——砍冗词不砍要点）：

| 要点 | 在场证据（新值字面） |
|---|---|
| 31 pages | `31 pages` |
| R6 edition | `R6 edition` |
| register restructure | `philosophical-register restructure`（逐字沿用） |
| 版本沿革 R3 -> R4 -> R5，挂起 -> R6 | `version lineage R3 -> R4 -> R5, submission suspended -> R6`（逐字沿用） |
| argument-first | `argument-first order, falsifiability verdicts stated before the runs`（含 Sec. 节名指引 `The first action: verdicts before the runs`） |
| 摘要重写同 register | `abstract rewritten to the same register` |
| 测量锚不变 | `measurement anchors … unchanged` |
| 池 66 | `reference pool … unchanged (66 entries)` |

## 三 其余 6 字段：原样沿用（零改动）

| 字段 | 字符数 | 非 ASCII | 处置 |
|---|---|---|---|
| Title | 74 | 0 | 原样沿用 |
| Authors | 10 | 0 | 原样沿用 |
| Subjects | 39 | 0 | 原样沿用 |
| License | 9 | 0 | 原样沿用 |
| Conflicts of interest | 13 | 0 | 原样沿用 |
| Date | 10 | 0 | 原样沿用 |

## 四 终件与核验

- 一行版终件：`shared/查理_arxiv表单ASCII修复_2026_10_20/arxiv_metadata_oneline_R6F18_ASCII_2026_10_20.txt`
- 终件指纹（落盘后实测）：SHA-256 前 12 位 `3f0dd8095353` · 2515 B
- 终检：8 行；每行「字段名: 值」；值内零换行零折行；全文非 ASCII 0；无 ；文件末单个换行（与源件同制）
- 字符计数口径：Python len()＝Unicode 码点计数；新值纯 ASCII，码点／UTF-16 单元／字节三种口径计数一致
- Abstract／Comments 全文以终件为准（本清单只登记 delta）；群内直贴值由终件同内容生成
