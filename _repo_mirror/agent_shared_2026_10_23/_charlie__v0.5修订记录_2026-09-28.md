# 查理·第三作 v0.5 中性化修订记录（2026-09-28）

**执行**：查理-论文主笔
**派单**：群管理员 2026-09-28 16:18（PI 2026-09-28 裁定落地：①中性化（含 Mavis 即 minimax 口径）②FTFB 已重投）
**基线**：`_v3v4_merged_paper_2026_09_27_v0.4.md`＝191,119 B／1009 行（wc 口径）／SHA-12 `E6C76F9BE292`（v0.4 存档未触碰，实测重核全等）
**新件**：`_v3v4_merged_paper_2026_09_27_v0.5.md`＝195,460 B／1013 行（wc 口径）／SHA-12 `9D53F1464AB0`
**修订面（双口径申报）**：编辑位点 **13** ＝改写行 12（v0.4 基线行号 L3/L34/L636/L638/L644/L890/L891/L892/L921/L924/L934/L1001）＋插入段 1（L964 后 4 行＝C.0.3 注册节）；difflib hunk 数 **11**（L890–L892 三行相邻并入同一 hunk；插入段 1 hunk）。口径注明：位点数按编辑动作计，hunk 数按 difflib 相邻合并计。

---

## 一、App A 中性化（戴夫终审登记项＋全文扫描同类项）

### 1.1 处置项（5 行，路径显示改中性表述；字节与 SHA-12 全部不动）

| App A 行（v0.4 基线） | 原字面（仅内部审计用，不入论文） | v0.5 中性显示 | 字节／SHA-12（不变） |
|---|---|---|---|
| Companion works and V1，L891 | `查理_FTFB_R4更新交付_2026-09-27/fiction_that_feeds_back.tex` | `ftfb-r4-text-delivery_2026-09-27/fiction_that_feeds_back.tex` | 101,928／`4F8C42319603` |
| Companion works and V1，L892 | `戴夫_FTFB_R4编译交付_2026-09-27/fiction_that_feeds_back.pdf` | `ftfb-r4-typeset-delivery_2026-09-27/fiction_that_feeds_back.pdf` | 411,782／`0B0D9495508F` |
| Merged-draft input anchors，L921 | `dave-survey2-arxiv-20260915/keep_the_books_arxiv_2026_09_16_v9/keep_the_books_survey.tex` | `survey2-arxiv-20260915/keep_the_books_arxiv_2026_09_16_v9/keep_the_books_survey.tex` | 102,686／`02acb6d563eb` |
| Merged-draft input anchors，L924 | `鲍勃_v1.1新增数字补测复核_2026-09-27.md` | `v1.1-added-numbers-re-verification_2026-09-27.md` | 15,269／`91E10F763316` |
| R4 re-adjudication evidence，L934 | `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md`（内嵌工具标签） | `letters/_v4_distillation_reply_code_v3_review_2026_09_23.md` | 28,207／`9BB22099DB3B` |

**审计桥**：五行原字面↔中性显示的完整映射即本表（工作链载体＝本修订记录）；论文内各行带「path tag-neutralized at the v0.5 round, the original string being registered in the program's working chain」注记，C.0.3 注册节登记处置类别与机制。账本可审计性经「字节＋SHA-12」二元组保持不变（§四 自检 7 实测五行数值列均在）。

### 1.2 全文扫描结果（扫描类：中文角色名／内部路径前缀／以标签形态出现的工具·团队名）

- 中文角色名（阿兰｜爱丽丝｜鲍勃｜查理｜戴夫）＋英文角色名（charlie/dave/bob/alan/alice，词边界、不分大小写）＋`dave-` 前缀＋`shared/`、`agents/`、`/home/`、`upload/`、`mount_agent`、仓 URL（github.com/zeroandcat）：**v0.5 全部 0 命中**（v0.4 侧同法扫描，命中即 §1.1 五处＋§1.3 例外，无遗漏）。
- Mavis（不分大小写）：论文内 **0 命中**——校准专件文件名在 v0.4 轮已决定「论文内不带文件名，fingerprint-only 外显」（App A L935 行），无需处置。PI 2026-09-28 口径「Mavis 即 minimax」经查不涉及论文任何字面：minimax 仅以教师代号形态出现在 Part II 冻结文本与 App B 字面表内（见 §1.3 例外）。
- trae（不分大小写）：v0.5 命中 3 处＝L323/L865/L936，均为仓内公开路径 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 的三次出现（§10.2 链引用＋Governance 表＋R4-evidence 表）——**登记为例外披露，不改动**，理由见 §1.3。
- CJK 字符：v0.5 命中 15 字符，全部位于 L468（§15.2 PI 裁定中文原文「GLM_2 蒸馏实验失败／假证伪根因／不得外推」，冻结携带字面）——**登记为例外披露，不改动**，理由见 §1.3。
- `_september_workspace`：v0.5 命中 1 处＝L830（signoff 第二副本行）——**登记为例外披露，不改动**，理由见 §1.3。

### 1.3 保留例外登记（四处类别，均已写入论文 C.0.3 注册节）

1. **教师代号（kimi/GLM_1/GLM_2/coze/minimax）**：出现在 Part II 冻结文本与 App B 字面表内——冻结字面与 verdict 字面零改动纪律直接适用（派单明文「冻结字面与 verdict 字面内出现的不改动，如涉及登记为例外披露」），保留并披露。
2. **errata 链仓内路径的三次出现（§10.2／Governance 表／R4-evidence 表）**：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 为仓库公开路径上的真实文件名——该行三元组（路径＋字节＋SHA-12）须对仓可解析；文件名内的工作环境名属仓侧命名事实，非本稿可单方面改名（改名须 PI 侧仓内重命名并触发再锚定轮），且工具环境名不携带作者身份。§10.2 位置在 Part II 冻结分区，改之即破 F 系分区字节全等。保留并披露；如 PI 裁定仓内重命名，另开再锚定轮。
3. **§15.2 中文裁定字面**：commission letter 裁定原文的冻结携带（v1.1 源携带内容），15 个 CJK 字符经逐字核验不含角色名／路径／标签，无身份要素。保留。
4. **`_september_workspace` 前缀（L830 signoff 行）**：仓内公开路径组成部分，日期型命名、无身份 token，三元组须对仓可解析。保留并披露（与例外 2 同理）。

另登记两处**历史字面保留**：①R1（App C 工作序列注册项）中「second work (FTFB, submitted and on hold)」——该括注描述原投稿状态（此状态无变化信息，未解除），FTFB 重投事实已由 §1.2/App A/R5 承载；v0.2/v0.4 轮面对同类状态更新时 R1 亦未联动（先例一致），本轮不改动。②C.0（v0.2 轮注册节）内「revised-edition-ready-for-resubmission fact is recorded without prediction」——该句是 v0.2 轮对当时事实的历史注册（round record 不可变，v0.3/v0.4 轮同样未触碰此句），当前状态由 C.0.3 承载，形成轮间时序链，不构成读者面矛盾。

## 二、FTFB 状态句更新（PI 口径：已重投，不预判）

| 位点（v0.4 基线行号） | 改法 |
|---|---|
| §1.2 事实句（L34） | 「completed … 2026-09-27 and is ready for resubmission to arXiv—…without predicting the hold's outcome or the resubmission's acceptance」→「completed … 2026-09-27, **was resubmitted to arXiv on 2026-09-28 per the PI's notification**—…without predicting the resubmission's outcome, including any change in the original submission's hold status」；句尾「citation upgraded to the formal arXiv record upon public release」保留（＝「公开后升级正式引用」） |
| App A 冻结档行（L890） | 「is ready for resubmission as of 2026-09-27」→「was resubmitted to arXiv on 2026-09-28 per the PI's notification」；冻结锚 356,123／`2D9EDC8C7303` 与「as of 2026-09-27, on hold」原状不动 |
| App A R4 文本行（L891） | 「the ready-for-resubmission text」→「the text of the entry above, resubmitted to arXiv on 2026-09-28 per the PI's notification, without prediction of the outcome」；「the arXiv resubmission and the resulting digest refresh are pending events」→「the resulting digest refresh remains a pending event」（重投已发生，归档与摘要刷新仍 pending） |
| R5（App C，L1001） | 「is ready for resubmission」→「was resubmitted to arXiv on 2026-09-28 per the PI's notification」；槽位改「the resubmission's **arXiv identifier** and its outcome (including any change in hold status …)」——**arXiv ID 等槽位仍 pending、未编造、未预判**（「this draft predicts no outcome」句保留） |
| §22.1 一致性位点（L644） | 派单枚举范围外的联动一致性触点：「ready-for-resubmission revised edition」被取代属性删除，改为指向 §1.2/App A/R5 的重投注册句（真值维护规则：§1.2 改后原句将成内部矛盾，故联动；已计入位点数与 hunk 数） |

## 三、版本联动（3 处＋新增注册节 1 处）

- L3 前言版本行：v0.4→v0.5，轮次描述改「tag-neutralizing … five workspace-face ledger rows, bytes and SHA-12 values unchanged … one external status fact」。
- L636（§21-(6)）与 L638（§21-(9)）轮次历史句：追加 v0.5 轮（「tag-neutralization and status registration」；v0.4 与 v0.5 同为 next-day 轮）。
- 新增 **C.0.3 注册节**（App C，C.0.2 与 C.1 之间）：登记 (i) 五行中性化＋机制＋原字面在工作链；(ii) 全文扫描四类例外披露（如 §1.3）；(iii) FTFB 重投注册（不预判、槽位 pending）；(iv) 正文触点清单＋轮纪律声明。C.0/C.0.1/C.0.2/C.1–C.4 历史注册均不动。

## 四、纪律自检（实测）

1. **F 系分区字节级全等（v0.4→v0.5，sha256）**：Abstract 2,051 B `2FAEDD5E8279`＝全等；Part I 46,167 B `DE34A9A8DE81`＝全等；Part II 34,454 B `C47B359E1FA2`＝全等；References 13,061 B `9E1AA39E97C6`＝全等；App B 2,009 B `4585CF9D31E0`＝全等。**F 系字面零改动最强证明成立。**
2. **verdict 五族频次（\b 词边界、全文口径）**：FAIL 32＝32／hit 9＝9／TRIGGERED 14＝14／NOT TRIGGERED 10＝10／composite qualification 15＝15，全等（口径注记：与 v0.4 修订记录所用计数法不同，本轮以词边界法对两版本同法计数，等值即不变式成立；五族字面本身另由分区字节全等覆盖）。
3. **数值 token 多重集差（全文）**：净删除仅「27」×1（L890 被取代 ready 状态句中的 2026-09-27，该行另一处 as-of 日期保留）；净新增均为注册层 token（2026-09-28 日期族、v0.5 版本号族、§1.2/§10.2/§15.2/§21/§22.1/C.0.3 节引、轮次历史句中的 v0.2–v0.5 计数）。冻结数字零触碰。
4. **引用 token**：`[N]` 总数 220＝220；[41] 6＝6、[45] 5＝5。新增引用 0、删除引用 0（保密件零引用维持，C.4 不动）。
5. **结构完整性**：标题 116→117（＋1＝C.0.3）；空节 18＝18（无新增空节）；标题直跟表 0＝0（同法口径等值）。
6. **扫描类复检（v0.5）**：中文角色名 0／dave- 0／mavis 0／英文角色名 0／workspace 路径形态 0／仓 URL 0；例外仅 trae×3（L323/L865/L936，仓内路径）＋`_september_workspace`×1（L830）＋CJK×15 字符（L468 判定字面）——与 C.0.3 登记的例外清单一一对应，无未登记残留。
7. **账本可审计性**：五行中性化行的字节＋SHA-12 实测均在（101,928/4F8C42319603、411,782/0B0D9495508F、102,686/02acb6d563eb、15,269/91E10F763316、28,207/9BB22099DB3B）；仓内行路径全部原样（Governance 表 v19 239,387/849D76BE3A06、v22 292,215/083087218A8D、signoff 26,637/BA4D07BD7000 抽验在位）。
8. **O 系零收束**：R5 槽位（arXiv ID/结果/hold 变化/刷新摘要/正式引用升级）全部 pending 未填；R8 placeholder 仍 open；version-pending 项不动；signoff 双指纹归一仍 pending。本轮未收束任何开放项。
9. **双盲**：作者身份零出现（author block 占位不动；扫描类 6 全零）；论文不含仓 URL 维持。

## 五、交付与下轮

- 本轮交付：`shared/_v3v4_merged_paper_2026_09_27_v0.5.md`（完整单件）＋本记录。v0.4 md 及 tex/pdf 存档未触碰。
- 下轮（本轮不做，另待派单）：验证（8-gram 自重叠重测口径沿戴夫 v0.4 原链）、重排（md→tex 转换）、编译。C.0.3 中「byte-identical to the v0.4 baseline (verified at this round)」声明即依本记录 §四-1 实测。
- 遗交 PI 事项：①仓内 `TRAE_V3_ASSET_ERRATUM_2026_09_23.md` 如需真中性化＝仓侧重命名＋再锚定轮（论文侧已按例外披露处理）；②R5 槽位待 PI 回传（arXiv ID 等）；③novelty 窗口 2026-10-15（阿兰决策说明另线）。

—— 查理-论文主笔 ｜ 2026-09-28 ｜ AI 生成
