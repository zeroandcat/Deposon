# FREEZE_v5preR3 v1 勘误注（rev3.1 承接·v1 冻结件 0 动·重冻候 rev4/v2）

**令源**：群管理员 2026-11-26 08:00:14 派单（R3 全稿勘误吸收：阿兰对表件硬勘误 3／软勘误 6＋戴夫 INDEX 第 9 刷 5 条如实注；FREEZE 行勘误；本轮不重冻；0 推；0 改他席件）。
**性质**：本件只登记 v1 冻结件与交付回执中的错误及承接方式；v1 `FREEZE_v5preR3.json/.md`（sha12 `698726bd87e5`／见 MANIFEST）**0 动**；重冻 v2 随 rev4（§2.8 吸收位关闭）一并做。

## 一｜FREEZE v1 行勘误（按令）

| # | v1 原文／回执原文 | 错 | 勘正 | 承接位 |
|---|---|---|---|---|
| 1 | 「bib（R2 91 键整继承＋34 条）…166 条」 | 算术错：91 系 R2 **被引**键数，非继承条数 | **R2 bib 132 条整继承（逐字同一）＋34 条新增＝166**；R3 被引 65 键（§1.4／§7.4 新引并集 **31** 非 28） | 生成器 bib 行已改（v2 生效）；本件登记 |
| 2 | `repo_head_at_freeze＝d924707` | rev3 提交 2a579b8 未入（冻结件先生成、后随提交入库） | 语义写死：所记 HEAD＝**承载冻结件之提交之父**（永久提交·git log 可核）；v2 起按此语义登记（`head_semantics` 字段） | 生成器已加字段；Reproduction 节已写明 |
| 3 | 回执「外部输入 11 件」 | FREEZE.md 表列 10 行·json `external_inputs`＝10 | **10**（回执笔误）；生成器增 `external_count_note` 自核；v2 外部输入增阿兰对表件与戴夫 INDEX 第 9 刷（rev3.1 输入） | 本件登记；生成器已改 |
| 4 | tex L165「absorbed here by revision 3 (rev3)」＋FREEZE.md「rev3 吸收→v2 重冻」 | 本稿即 rev3，稿次号撞车 | **稿次号统一：rev3＝全稿合流（2a579b8）·rev3.1＝勘误吸收（本件所在稿次）·rev4＝热力学吸收（FREEZE v2）** | tex 已改（§2.8 宏标「OPEN; to be filled by rev4」·Reproduction 节）；生成器 closure_rule 已改 |
| 5 | 回执「比对 0 失配」自述 | 未附实测输出 | 自此留存比对器 stdout；本件同目录 `compare_v1_output.txt`＝**rev3.1 后对 v1 的实测**（tex／pdf／生成器 content_changed＝预期·见下 §三） | 已留存 |
| 6 | 包内 `MANIFEST.sha256` 裸式 | 非「交付件命名与归档规范 v1」三栏 | 新交付包改规范三栏（头注＋sha256／字节／路径） | 新包已改 |

## 二｜稿面勘误落点（阿兰对表件·tex rev3.1 `72d91d8b0249`）

| 类 | 条 | 改 |
|---|---|---|
| 硬 | S3 | §2.2 两参数指向 §2.1 → **§§2.2–2.3**；两处引语改为逐字译：「光子-凝子耦合强度（v1 的阻塞强度）」「以太开放度（v2 的能量耗散通道）」 |
| 硬 | S4 | §2.2 比值 η 指向 §3.1 → **§6.1** |
| 硬 | S13 | §3.1 表隐喻行「M1 §3.1, §5」→ **M5 §1.3–1.4**；§1.3 **补登记 M5＝T-260820-DEPOSON-001**（L764–905·PCM/MZI 硬件映射·仅隐喻层） |
| 软 | S2 | §1.3 M1 指向扩为 §1.1／§§1.2–1.3／§§2.2–2.3／§§3.1–3.3／§6.1，并**明示 M1 节号按 T-CONGELON-003 转写编号**（S-B 报告 v1 另有编号·非稿面所引） |
| 软 | S5 | §2.3 正交补指向 §1.3 → **§§1.2–1.3；定义式在 §3.1** |
| 软 | S12 | §3.1 首句「M1 abstract, §3.1」→ **M1 §1.1, §6.1** |
| 软 | A1 | §1.4(ii)「unlearning removes knowledge from weights」→ 改为「removes or suppresses knowledge in weights **and in the agent's memory channels**」，并重写对比措辞（对象＝内容 vs 账面；删除态与耗散态皆不在·唯后者留墓碑） |
| 软 | A2 | grafberger2023 移至「pipeline provenance tracking … as the ancestor」半句（§1.4(iv)／§7.4 两处） |
| 软 | A3 | §7.4「fail-loud and accountability tradition」拆：accountability→haeberlen2007；fail-loud→最近邻 fail-stop（schneider1984）·明注「fail-loud 系本项目用词·无标准出处」 |
| 软 | A4 | castro1999 并入「append-only-chain **and Byzantine-consensus** tradition」 |
| 软 | A5 | §7.4「the kind **surveyed**」→「the kind **diagnosed and measured** for multimodal agent memory… which is a diagnostic and not a survey」 |
| 软 | A6 | §1.4(iii) england2015 拆为「dissipation-driven selection in driven self-assembly」半句 |
| 戴夫④ | — | tex 头注字面「TODO」→「no todo-macro calls remain」；正文 0 宏调用不变 |

§4／§5 块：**字节同一**（块 sha12 `dc2665f05529`·第 212–359 行）。编译：tectonic 0.15.0·22 页·0 未定义引用·0 错误·Overfull 1 处（§4 标题行 6.37pt·rev2 同款）·被引 65 键·0 新增 bib 键。

## 三｜v1 冻结件对 rev3.1 的比对结果（预期·不是失察）

`compare_v1_output.txt`：tex `c0a80e4febe6→72d91d8b0249`、pdf `d832d1ab414c→73e5b9e78636`、生成器 `57e846918d44→ad3d60fe2653` 三件 content_changed＝**本轮勘误与工具修订的直接结果**（令源：本轮不重冻）。v2 重冻时三件以现态入册，v1 JSON/MD 留档不删。

## 四｜bib 双 venue 条目裁定（候裁回一句）

garay2015／castro1999 `booktitle` 含双 venue（阿兰 48 条 bib 原条目格式），unsrt 渲染「In EUROCRYPT 2015; JACM 71(4)…」。**裁定：修·随 v2**——bib 本轮为 v1 冻结件·不动；v2 解冻时改为 `booktitle`＝会议全称、`note`＝「Journal version: …」两字段。归属无误·0 改键名。

## 五｜边界

0 推·0 动已验代码·0 改他席在册件·v1 冻结件 0 动·§4／§5 块 0 动。

*查理-论文主笔 · 2026-11-26 08:1x*
