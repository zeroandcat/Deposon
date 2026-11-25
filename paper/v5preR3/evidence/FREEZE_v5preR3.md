# FREEZE_v5preR3 · v1 — R3 谱系冻结事件（S-07 候立转立）

- 生成时间：2026-11-26 07:40:38　引擎：tectonic 0.15.0　页数：22　未定义引用：0　错误：0　TODO：0　吸收位：1（OPEN）
- 令源：群管理员 2026-11-26 07:21:08 派单（R3 全稿覆写·立 FREEZE_v5preR3·S-07 候立转立·含 rev2 中间锚 d924707）
- 谱系：分支 `private/v5preR3`·冻结时 HEAD `d924707`·rev2 中间锚 `d924707`·rev1 锚 `67a86e0`·自 R2 终态 `ac04a4b` 分出·0 推·不沿用 R2 冻结
- 吸收位：§2.8 Thermodynamic reconstruction: absorption slot (label sec:absorption) — **OPEN**（爱丽丝（热力学重构·同期在做）；其件到达后走 rev3 吸收→重冻 FREEZE_v5preR3 v2（加入重构件自身指纹））

## 甲｜R3 谱系对象（frozen）

| 件 | path | sha12 | 行 | 字节 | kind | 备注 |
|---|---|---|---|---|---|---|
| 论文 tex（rev3 全稿） | `paper/v5preR3/v5preR3_论文.tex` | `c0a80e4febe6` | 449 | 88265 | frozen | §1–§7 合流·0 TODO·§4/§5 块 sha12 dc2665f05529 与 rev2 字节同一 |
| 论文 pdf（tectonic 0.15.0） | `paper/v5preR3/v5preR3_论文.pdf` | `d832d1ab414c` | 970 | 164954 | frozen | 22 页·0 未定义引用·0 错误 |
| bib（R2 91 键整继承＋34 条） | `paper/v5preR3/v5preR3_related_work.bib` | `b5160e1df576` | 1508 | 56741 | frozen | 166 条·0 重键·65 条被引 |
| 点火件（立项件） | `paper/v5preR3/v5preR3_点火件.md` | `2e5735f29923` | 58 | 5559 | frozen | rev2 原件·0 动 |
| 版本谱系对照表 | `paper/v5preR3/v5preR3_版本谱系对照表.md` | `37563ab073de` | 33 | 2842 | frozen | rev3 更新：R3 状态＝全稿合流·S-07 候立转立 |
| 冻结生成器 | `paper/v5preR3/tools/gen_freeze_r3.py` | `57e846918d44` | 184 | 12129 | frozen | 本件 |
| 冻结比对器 | `paper/v5preR3/tools/compare_freeze_r3.py` | `0b67c81b55c2` | 84 | 3709 | frozen | 沿 R2 compare_freeze 链·R3 口径 |
| kimi round10 问单 | `paper/v5preR3/evidence/kimi_round10_prompt.txt` | `35c6858af9a5` | 34 | 4147 | frozen | F7/L2 原文贴入·逐字 |
| kimi round10 答复（逐字） | `paper/v5preR3/evidence/kimi_round10_answer_逐字.txt` | `85189b55b1c5` | 83 | 9274 | frozen | finish=stop·model kimi-k3.1-pro·0 代庖 |
| kimi round10 元数据 | `paper/v5preR3/evidence/kimi_round10_answer_逐字.txt.meta.json` | `345d7a91bcc5` | 25 | 518 | frozen | usage/finish/model 原样 |

## 乙｜R2 作废件（0 删·只记指纹）

| 件 | path | sha12 | 行 | 字节 |
|---|---|---|---|---|
| R2 论文 tex（VOIDED·0 删） | `paper/v5preR2_论文.tex` | `a6371ed71099` | 458 | 84678 |
| R2 作废标注 | `paper/v5preR2_作废标注.md` | `7428c110a23d` | 40 | 3046 |
| R2 冻结（不沿用·留档） | `paper/evidence/FREEZE_v5preR2.json` | `da8dc34085e6` | 663 | 21539 |

## 丙｜外部输入件（external·绝对路径·只记 sha12）

| 件 | sha12 | 状态 | 备注 |
|---|---|---|---|
| S-A 本体源·对话集 docx | `d8fc8fa798c9` | ok | M1–M4 原文 |
| S-B 定稿源·统一场论 v1 PDF | `c11d7007f857` | ok | T-CONGELON-003 |
| 阿兰 Lean 审读件包 | `cfd7ed7f9934` | ok | 目录·v3.1 独立复现·目录按 MANIFEST.sha256 记 |
| 爱丽丝 v3.1 Lean 件 | `0decb3a4059f` | ok | §4.7 引 0decb3a4059f |
| 爱丽丝 v3.1.1 Lean 件 | `277f63bff1ca` | ok | §4.7 引 277f63bff1ca |
| 爱丽丝 v3.1.1 执行器 | `58fe2c0fbca8` | ok | 工程包·0 动 |
| 爱丽丝 v3.1.1 自测日志 | `61fadba07043` | ok | D7a/D7b 否证探针两向 |
| 爱丽丝 定形件·两臂配对性（round9） | `5727b4d39e48` | ok | §6.4 paired |
| 鲍勃 判据收口 v1.1 | `f3c59c956a87` | ok | F1–F8·L1/L2/L3 |
| 鲍勃 实验线全谱系清点 | `f9ca8e9aaac1` | ok | H1/H2/H4·C01–C17 重述 |

## 丁｜规则（沿 R2 链·写清）

1. **现役为准**：冻结以当前现役版本为准；旧版指纹作废留档，不两版并存。
2. **失效即重冻**：任一 frozen 件指纹变动 ⇒ 冻结失效，须重跑 `tools/gen_freeze_r3.py --version N+1` 并记变动原因。
3. **比对**：`python3 tools/compare_freeze_r3.py evidence/FREEZE_v5preR3.json` 重算现态并逐位比对；任一 frozen 件 content_changed ⇒ 失配·须处置（退出码 1）。
4. **吸收位**：§2.8 OPEN；爱丽丝热力学重构件到达 → rev3 吸收 → v2 重冻并加入重构件指纹；本轮不等。
5. **认证范围**：本冻结只证明「所名之件即所比之件·指纹如记」；不证明任何读数（读数在各席证据包·本稿引用不重测）。

## 戊｜边界

- 0 推·0 动已验代码（harness/ mcp/ plugin/ tests/ scripts/ paper/tools/ paper/rag/ paper/evidence/ 中 R2 件 0 动；R3 工具为新增件·置于 paper/v5preR3/tools/）·0 改他席在册件。

*查理-论文主笔 · 2026-11-26 · FREEZE_v5preR3 v1*
