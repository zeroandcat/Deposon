# v5preR3 版本谱系对照表

| 版本 | 分支／目录 | 状态 | 主线 | 处置 |
|---|---|---|---|---|
| v5pre（R1.3 及前） | 历史线 | 已被 R2 沿袭／重构 | 外部记忆层热力学账本 | 归档·只读 |
| v5preR2 | `private/v5preR2` HEAD `ac04a4b` | **作废**（范畴错位·2026-11-26） | 热力学账本（第一律四账·自解结算） | 0 删·头注 VOIDED·`paper/v5preR2_作废标注.md`；数据级资产（bib 132 条逐字继承／读数／工具链）被 R3 继承 |
| **v5preR3** rev1 | `private/v5preR3` commit `67a86e0` | 骨架＋§4／§5 v1（kimi round6 回修） | 仿物理散射-耗散理论（T+R+A=1·(g_couple, g_aether)·D 单调） | 七节骨架·§4／§5 正文·其余 TODO |
| **v5preR3** rev2 | commit `d924707` | **中间锚**（E3 拆两定理·键可见性边界句·aux-CI 策略层·F3 升格） | 同上 | 10 页·0 未定义·§1–§3／§6／§7 仍 TODO |
| **v5preR3** rev3 | commit `2a579b8`（父 d924707） | **全稿合流**（2026-11-26） | 同上 | abstract／§1／§2／§3／§6／§7／Reproduction 七处成文·§1–§7 一篇·0 TODO·§4／§5 字节同一（块 sha12 `dc2665f05529`）·22 页·0 未定义引用·1 吸收位 OPEN（§2.8）·tex `c0a80e4febe6`·**FREEZE_v5preR3 v1 冻结时点** |
| **v5preR3** rev3.1 | `private/v5preR3`（本轮提交） | **勘误吸收**（2026-11-26） | 同上 | 阿兰对表件硬勘误 3（S3／S4／S13）＋软勘误 6（A1–A6·S2／S5／S12）落稿；§1.3 补登记 M5＝T-260820-DEPOSON-001·明示 M1 节号按转写编号；稿次号统一（rev3／rev3.1／rev4）；§4／§5 块字节同一（`dc2665f05529`）·22 页·0 未定义·tex `72d91d8b0249`·pdf `73e5b9e78636`·**本轮不重冻**（FREEZE v1 0 动·勘误见 `evidence/FREEZE_v5preR3_v1_errata.md`） |
| **v5preR3** rev4 | （候） | 热力学吸收（候爱丽丝重构件） | 同上 | §2.8 吸收位关闭→FREEZE_v5preR3 **v2** 重冻（加入重构件指纹·bib 双 venue 两条格式修·HEAD 语义按 v2 口径） |

## 稿次号（统一口径·自 rev3.1 起）

rev3＝全稿合流（2a579b8）｜rev3.1＝勘误吸收｜rev4＝热力学吸收（FREEZE v2）。首单令源中「其件到达后走 rev3 吸收」之「rev3」按本口径读作「下一稿次」＝rev4。

## 取代对照

| 位 | 旧 | 新 | 性质 |
|---|---|---|---|
| S-05 | `查理_v5preR3骨架案头件_v2_20261125.md`（P474 包） | `paper/v5preR3/v5preR3_论文.tex`（骨架案头件 v2 的节位→tex 节位一一对应） | 升版（非取代·案头件仍可引） |
| S-06 | R2 冻结 `FREEZE_v5preR2` v5 | — | 旧位留档·不沿用·不建双冻结 |
| **S-07** | `FREEZE_v5preR3`（候立） | **`paper/v5preR3/evidence/FREEZE_v5preR3.json/.md` v1（候立转立·冻结时点 rev3 `c0a80e4febe6`）** | 新立冻结事件·含 rev2 中间锚 `d924707`·工具 `paper/v5preR3/tools/gen_freeze_r3.py`／`compare_freeze_r3.py`（沿 R2 链·生成器 rev3.1 修订供 v2）·v1 勘误注 `evidence/FREEZE_v5preR3_v1_errata.md`·比对实测 `evidence/compare_v1_output.txt` |

## 编译态（rev3.1）

- tectonic 0.15.0·**22 页**·0 未定义引用·0 错误·0 todo 宏调用·65 条被引（bib 166 条＝R2 132 条逐字继承＋34 条新增·0 重键·0 缺键·本轮 0 新增键）。
- Overfull 1 处＝§4 标题行 6.37pt（与 rev2 同款·§4／§5 0 改·非本轮范围）。
- tex 侧 CJK 警告仅来自中文标题行（ptmb8t 无 CJK 字形）＝R2 同款既有状态；**正文 0 CJK**（词源以罗马字 ning／ningzi／ninghua／ninggu 书写）。

## 吸收位

- §2.8「Thermodynamic reconstruction: absorption slot」（label `sec:absorption`）**OPEN**：爱丽丝热力学重构件到达后走 **rev4** 吸收→`FREEZE_v5preR3` **v2** 重冻。

## kimi round10

- F7／L2 多重性一问已办（贴原文·`kimi-k3.1-pro`·finish=stop·逐字见 `paper/v5preR3/evidence/`）：F7/L2 与 G-A2 同一检验标签层（是）；G-A2／G-B 须重登（荐固定序列门控）；配对下 F7 文本不改；0 冲突。采位归 PI。

*查理-论文主笔 · 2026-11-26 · 版本谱系对照表（rev3.1）*
