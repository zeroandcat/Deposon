# v5preR3 版本谱系对照表

| 版本 | 分支／目录 | 状态 | 主线 | 处置 |
|---|---|---|---|---|
| v5pre（R1.3 及前） | 历史线 | 已被 R2 沿袭／重构 | 外部记忆层热力学账本 | 归档·只读 |
| v5preR2 | `private/v5preR2` HEAD `ac04a4b` | **作废**（范畴错位·2026-11-26） | 热力学账本（第一律四账·自解结算） | 0 删·头注 VOIDED·`paper/v5preR2_作废标注.md`；数据级资产（bib 132 条逐字继承／读数／工具链）被 R3 继承 |
| **v5preR3** rev1 | `private/v5preR3` commit `67a86e0` | 骨架＋§4／§5 v1（kimi round6 回修） | 仿物理散射-耗散理论（T+R+A=1·(g_couple, g_aether)·D 单调） | 七节骨架·§4／§5 正文·其余 TODO |
| **v5preR3** rev2 | commit `d924707` | **中间锚**（E3 拆两定理·键可见性边界句·aux-CI 策略层·F3 升格） | 同上 | 10 页·0 未定义·§1–§3／§6／§7 仍 TODO |
| **v5preR3** rev3 | commit `2a579b8`（父 d924707） | **全稿合流**（2026-11-26） | 同上 | abstract／§1／§2／§3／§6／§7／Reproduction 七处成文·§1–§7 一篇·0 TODO·§4／§5 字节同一（块 sha12 `dc2665f05529`）·22 页·0 未定义引用·1 吸收位 OPEN（§2.8）·tex `c0a80e4febe6`·**FREEZE_v5preR3 v1 冻结时点** |
| **v5preR3** rev3.1 | `private/v5preR3`（本轮提交） | **勘误吸收**（2026-11-26） | 同上 | 阿兰对表件硬勘误 3（S3／S4／S13）＋软勘误 6（A1–A6·S2／S5／S12）落稿；§1.3 补登记 M5＝T-260820-DEPOSON-001·明示 M1 节号按转写编号；稿次号统一（rev3／rev3.1／rev4）；§4／§5 块字节同一（`dc2665f05529`）·22 页·0 未定义·tex `72d91d8b0249`·pdf `73e5b9e78636`·**本轮不重冻**（FREEZE v1 0 动·勘误见 `evidence/FREEZE_v5preR3_v1_errata.md`） |
| **v5preR3** rev3.2 | `private/v5preR3`（本轮提交） | **阿兰三处吸收**（2026-11-26·管理员 08:29/14:35 令·阿兰 08:18 三件） | 同上 | ①§4.4（L270）读回熵产生句追加限定＝本理论读回事件含 A 份额所致·非读出普遍律（Bennett 1982／Sagawa–Ueda 2008·080403／2009·250602·书目外源核实）②§2.6（L158）Feshbach form 加引原典三支（feshbach1958＝Ann.Phys.5:357–390／feshbach1962＝19(2):287–313／fano1961＝Phys.Rev.124(6):1866–1878）③自引锁 v2（deposon2026 howpublished＝arXiv:2609.09001v2 (2026-11-03)）；bib 166→171 条；§4／§5 块 rev3.1 基线 `dc2665f05529a9d6` 复算恒等·块内变更实测仅 L270（令面点名豁免位·其余 147 行逐字节恒等）·块外仅 L158·新块 `6a724a0013f22381`；23 页·0 未定义·tex `cb88ca99f7890653`·pdf `ae170ea413a8061c`·bib `55ef44f36dafb51c`·**本轮不重冻**（FREEZE v1 0 动·v2 随 rev4·A4 甲） |
| **v5preR3** rev4 | commit `23e2423`（父 3b3b8cb） | **热力学吸收**（2026-11-26·A4 甲·PI 12:47:01 裁决·管理员 15:05:04 催派） | 同上 | §2.8 吸收位闭合（OPEN 宏移除·改题 "the ledger layer absorbed"·DeposonThermoRecon.lean `45c56f1e5487` 承接声明·58 定理对表 0 取代/11 继承/47 划界/7 增补·15 定理件 15/15 逐字继承·候裁位留注不代裁）；§4/§5 块沿 rev3.2 现态 0 动（L218-365·漂移 +6·`6a724a0013f22381` 全文窗口扫描实测恒等）；23 页·0 未定义·tex `faa0ae5c67d35d27`·pdf `51c9605ba26edeb4`·**FREEZE_v5preR3 v2 重冻随本轮** |

## 稿次号（统一口径·自 rev3.1 起）

rev3＝全稿合流（2a579b8）｜rev3.1＝勘误吸收｜rev4＝热力学吸收（FREEZE v2）。首单令源中「其件到达后走 rev3 吸收」之「rev3」按本口径读作「下一稿次」＝rev4。

## 取代对照

| 位 | 旧 | 新 | 性质 |
|---|---|---|---|
| S-05 | `查理_v5preR3骨架案头件_v2_20261125.md`（P474 包） | `paper/v5preR3/v5preR3_论文.tex`（骨架案头件 v2 的节位→tex 节位一一对应） | 升版（非取代·案头件仍可引） |
| S-06 | R2 冻结 `FREEZE_v5preR2` v5 | — | 旧位留档·不沿用·不建双冻结 |
| **S-07** | `FREEZE_v5preR3`（候立） | **`paper/v5preR3/evidence/FREEZE_v5preR3.json/.md` v1（候立转立·冻结时点 rev3 `c0a80e4febe6`）** | 新立冻结事件·含 rev2 中间锚 `d924707`·工具 `paper/v5preR3/tools/gen_freeze_r3.py`／`compare_freeze_r3.py`（沿 R2 链·生成器 rev3.1 修订供 v2）·v1 勘误注 `evidence/FREEZE_v5preR3_v1_errata.md`·比对实测 `evidence/compare_v1_output.txt`·**v2 已立（2026-11-26 rev4·吸收位 CLOSED）**：`evidence/FREEZE_v5preR3_v2.json/.md`·重构件指纹 `45c56f1e5487` 入 external·frozen 11＋r2_voided 3＋external 18＝32 项对拍 0 失配·`evidence/compare_v2_output.txt`（v1 旧件原路径原指纹 0 动） |

## 编译态（rev4）

- tectonic 0.15.0·**23 页**·0 未定义引用·0 错误·0 todo 宏调用·70 条被引（bib 171 条＝R2 132 条逐字继承＋34 条新增＋rev3.2 原典五条·0 重键·0 缺键）。
- rev3.1 编译态（22 页·bib 166）随谱系留存于 rev3.1 提交 dc45d43；rev3.2 三处吸收后页数 23（rev3.2 提交 3b3b8cb）。
- Overfull 1 处＝§4 标题行 6.37pt（与 rev2 同款·§4／§5 0 改·非本轮范围）。
- tex 侧 CJK 警告仅来自中文标题行（ptmb8t 无 CJK 字形）＝R2 同款既有状态；**正文 0 CJK**（词源以罗马字 ning／ningzi／ninghua／ninggu 书写）。

## 吸收位

- §2.8「Thermodynamic reconstruction: absorption slot」（label `sec:absorption`）**OPEN**：爱丽丝热力学重构件到达后走 **rev4** 吸收→`FREEZE_v5preR3` **v2** 重冻。

## kimi round10

- F7／L2 多重性一问已办（贴原文·`kimi-k3.1-pro`·finish=stop·逐字见 `paper/v5preR3/evidence/`）：F7/L2 与 G-A2 同一检验标签层（是）；G-A2／G-B 须重登（荐固定序列门控）；配对下 F7 文本不改；0 冲突。采位归 PI。

*查理-论文主笔 · 2026-11-26 · 版本谱系对照表（rev4·v2 重冻随本轮·S-07 双版在案）*
