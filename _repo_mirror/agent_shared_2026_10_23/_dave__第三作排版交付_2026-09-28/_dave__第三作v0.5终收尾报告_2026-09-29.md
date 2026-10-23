# 戴夫·第三作 v0.5 终收尾交付报告（原链复测→回填→修复重放→编译→合规）

**日期**：2026-09-29（派单 00:19，落库 00:33）
**执行**：戴夫-格式专家
**任务书口径**：五件＝①8-gram 原链复测（v9 轮原工具链 vs v0.5 md，参照件 sha 锁定，与鲍勃重建值交叉验证）②R8/§22.5 回填（原链值为准，deferred 注记同步改写，md 链头占位不回改）③v0.4 终收尾 6 处格式修复重放＋v0.5 新增面全量 Overfull 重跑 ④三遍收敛编译 ⑤arXiv 合规全套＋页数与双盲终审登记。

---

## 一、8-gram 原链复测（任务 1）

**工具链**：`agents/…e75/third_paper_v05_final/scripts/overlap8_final_v05.py`——v9 轮 `overlap_check_v2.py` 口径逐位复刻（norm_words 词级归一化／strip_tex／首现贪心扩展／覆盖率分母＝查询件），与 v0.3 轮 `overlap8_final.py`、v0.4 轮 `overlap8_final_v04.py` 同链。**参照件 sha 锁定核验通过**：查询件＝`shared/_v3v4_merged_paper_2026_09_27_v0.5.md`（SHA-256 `9d53f1464ab0…`，与派单一致）；第一作 arXiv tar 内 `deposon_paper_en.tex`（`0d5679110aba…`）；第二作 FTFB R4 `fiction_that_feeds_back.tex`（`4f8c42319603…`，与鲍勃同件）。

**原链 v0.5 实测值（终值口径）**：

| 量 | vs 第一作（arXiv tex） | vs 第二作（FTFB R4 tex） |
|---|---|---|
| 全文 8-gram | **0.53%**（164 词／13 run／30,857 tokens） | **0.62%**（191 词／16 run／30,857 tokens） |
| 剔题录（净正文 28,913） | **0.45%**（130 词） | **0.31%**（91 词） |
| 题录块内（1,944） | 34 词 | 100 词 |
| §18.1 8-gram | 8.10%（103 词／1,271） | 7.16%（91 词／1,271） |
| §18.1 10-gram | **5.51%**（70 词） | 5.82%（74 词） |
| 自由文本 | **0 词** | **0 词** |

**与 v0.4 同链对照（零新增验证）**：匹配词数/run 数零变化（164/13、191/16）；run 级 (pos, words, text) 集合逐项全等（companion 脚本 `regenerate_v04_runs.py` 同逻辑重算 v0.4 基线——重算聚合值与 v0.4 轮存档 JSON 全字段全等，工具链确定性成立）；v0.5 注册层新增 767 tokens **零 8-gram 匹配**（原链独立证实）。率值变动（0.55→0.53、0.63→0.62）纯系分母稀释（30,090→30,857，−0.02/−0.01pp），与鲍勃「率值变动纯系分母稀释」结论一致。C 类 14 run（8＋6）逐条复核与 v0.4 同集：全部归共享题录、§18.1 案例引用（数字串／枚举口径／T,R,A 账目语／2.22e-16 守恒句）与申报锚定物（一作纲领句×2、一致性证据句、机器可验证性句、二作冻结锚串、App A 锚行）——**自由文本 0 词成立**。

**与鲍勃重建值交叉验证（两源对照）**：

| 量 | 原链（本轮，终值） | 鲍勃重建（交叉验证留档） |
|---|---|---|
| 分母（全文/题录/净正文/§18.1） | 30,857／1,944／28,913／1,271 | **全等** |
| 全文 vs 一作 | 0.53%（164w／13run） | 0.69%（214w／17run） |
| 全文 vs 二作 | 0.62%（191w／16run） | 0.80%（246w／20run） |
| 剔题录 | 0.45%／0.31% | 0.54%／0.43% |
| §18.1 十克 | 5.51%／5.82% | 5.51%／5.82%（**同值**） |
| 新增匹配／自由文本 | 零／0 词 | 零／0 词 |

两源系统差与 v0.4 轮完全一致（164↔214、191↔246，+30.5%／+28.8%，重建口径保守偏高注记随行）；分母全等、十克同值、零新增与零自由文本双向吻合。**终值依据**：原链复测成功，按「原链为准（先例同链）」规则取原链值回填，鲍勃值交叉验证留档（本表＋`out/overlap8_v05_results.json`）。

## 二、R8/§22.5 回填（任务 2）

**4 处回填，逐项锚点唯一断言**：
1. **tex 头部注记**：占位 deferred 两行 → 终值登记块（两源值＋终值依据：工具链口径、参照面、0.53%/0.62% 及分子分母、十克 5.51%、零自由文本、v0.3 基线起匹配集零变化〔v0.4/v0.5 注册层 +1,725/+767 tokens 均零新增〕、鲍勃交叉验证值、md 链头占位不回改声明）。
2. **§21(8)**：「is deferred to the typesetting round (Section 22.5)」→「is registered in Section 22.5 and Appendix C (R8)」（与 v0.4 final 同字面；§21(9) v0.5 轮史句保持 md 原文不动）。
3. **§22.5 占位句**→终值披露句（0.53%/0.62%＋净正文 0.45%/0.31%＋锚定物构成＋零自由文本＋交叉验证随行登记；句式沿 v0.4 final，数值更新为 v0.5 口径）。
4. **R8 登记条**：「placeholder, open」→「registered, closed (backfilled at the terminal typesetting round, 2026-09-29)」——完整登记工具链口径、参照面、两源值、匹配集谱系（v0.3 基线零变化）、鲍勃重建值与「终值取自记录工具链（同链先例）」依据。

**边界处置**：md 链头占位零触碰（`9d53f1464ab0` 复验一致）；C.0.2 历史轮记录「remain deferred as before」按 v0.4 final 先例保留（轮史记录，描述 v0.4 轮时点状态）；C.0.3（v0.5 轮注册节）无 deferral 引用、零改动。

## 三、格式修复重放＋Overfull 全量重跑（任务 3）

**6 处重放（与 v0.4 final 字面全等，脚本断言逐一通过）**：①作者行折行（`decision;\\` 换行）②表 0 末列 `p{0.11}`→`p{0.125}` ③表 9（verdict 复合裁定表）末列 `l`→`>{\raggedright\arraybackslash}p{0.30\textwidth}`（锚点全文出现 2 次，位置限定于「The formal verdict is FAIL」之后——预注册阈值表按 v0.4 final 保持 `l l` 不动）④表 4 第 4 列 `p{0.20}`→`>{\raggedright\arraybackslash}p{0.145\textwidth}` ⑤表 5 两行 `\allowbreak{}`（`rationalization/`、`benchmark/`、`protocol/`）⑥App C.1 首列 `l`→`>{\raggedright\arraybackslash}p{0.145\textwidth}`＋末列 `0.58`→`0.55`。

**漂移审计**：final↔占位版 diff 恰 **10 hunk**（4 回填＋6 修复），与计划集全等，零计划外改动；v0.4 轮转换 hunk（轮史句／中性化五行／C.0.3／R5 重投句等）零触碰。

**Overfull/Underfull 全量重跑（含 v0.5 新增面：中性化五行、C.0.3、重投句）**：**Overfull 0**（v0.4 final 同为零，6 处修复重放后新增面全过）；Underfull 30（=v0.4 基线，ragged-right 表格与 CJK 块固有 badness，先例登记不改）。

## 四、三遍收敛编译（任务 4）

pdflatex（TeX Live 2026 便携环境，隔离 TEXMF 三变量）×3：**零 error、零 undefined reference、零 multiply defined**；pass2 与 pass3 stdout 全等（收敛成立）。产出 56 页 PDF。

## 五、arXiv 合规＋页数与双盲终审（任务 5）

- **字体**：pdffonts 42 字体实例**全嵌入＋子集化**（LMRoman/LMMono/Dingbats/gbsnu CJK 系）。
- **页面尺寸**：US letter 612×792 pt（沿 v1.1 模板体例，v0.3/v0.4 同；派单清单写「A4」——本作既定体例为 US letter，arXiv 两者均收，如实登记未改体例）。
- **摘要预算**：摘要正文（Abstract→Keywords 前）文本层 **1,879 字符 ≤ 1,920 PASS**；若提交时并入 Keywords 行（145 字符）合计 2,025 将超限——arXiv 摘要字段内容可选，建议仅填摘要正文（或裁关键词），**交 PI 裁定**（摘要系 F 族冻结内容，排版轮不动）。
- **双盲 [4]**：References [4]＝「Attribution withheld for double-blind review」，作者块与标识符扣留声明在位（标题页作者块「Attribution withheld」＋摘要区作者注＋[4] 条目，三处均注册内容）。
- **单 tex 自含**：零 `\input`／`\includegraphics`／`.bib`／图件，上传件＝1 个 tex（建议上传时更名 `main.tex`）；PDF 628,487 B 远低于限额。
- **页数登记**：**56 页**（v0.4 final 55 页；+1 系 C.0.3 新节＋回填文本所致）。
- **双盲终审（本轮中性化后）**：PDF metadata Author 空／Title＝论文题／Creator＝LaTeX with hyperref；书签 115 条零身份词；页眉页脚仅默认页码；文本层全扫——PI 人名 0 命中（「Yuan」1 命中系参考文献 [48] 第三方作者「Yuanyi Wang」子串假阳性）、角色名 CJK/英文词边界均 0 命中、`/home/`／`dave-`／`/agents/`／`/tmp/` 0 命中；CJK 15 字符＝L427 冻结字面一处（「蒸馏实验失败假证伪根因不得外推」，注册内容，零身份）；TRAE 路径×3＝C.0.3 申报例外（`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` errata 链仓内路径，工具标签非个人身份，鲍勃轮已核）；tex 注释 20 行全头部（英文，零姓名/路径/身份）。**v0.4 轮登记的披露项（App A 三个角色中文名文件名＋`dave-survey2-` 前缀）经 v0.5 中性化后全部关闭；本轮双盲零新增披露项，仅余 C.0.3 已申报例外（TRAE×3）与冻结字面（CJK 15 字符）两处注册内容。**

## 六、交付物清单（shared/戴夫_第三作排版交付_2026-09-28/）

| 文件 | 指纹 | 说明 |
|---|---|---|
| `_v3v4_merged_paper_2026_09_27_v0.5_final.tex` | 217,494 B／887 行（wc -l）／SHA-12 `23b2d1357c10` | 回填＋修复重放终版 tex（4 回填＋6 修复，diff 恰 10 hunk 计划内） |
| `_v3v4_merged_paper_2026_09_27_v0.5_final.pdf` | 628,487 B／56 页／SHA-12 `637e8a8ff4e7` | 三遍收敛编译终版 PDF（零 error/undefined/multiply/Overfull） |
| `戴夫_第三作v0.5终收尾报告_2026-09-29.md` | 本报告 | 五任务全记录（含两源 8-gram 值对照与终值依据） |
| （存档不动）`_v3v4_merged_paper_2026_09_27_v0.5.tex` | `3aa18594354e` | v0.5 占位版（本报告前件，零触碰） |
| （前轮件不动）v0.4 两 tex＋PDF＋两报告 | `4b513e2dc6e6`／`fd5f915699d4`／`178f367f2ca6` | v0.4 转换轮与终收尾轮存档 |

工具链（私有区可复跑）：`third_paper_v05_final/scripts/`＝`overlap8_final_v05.py`（原链复测，输出 `out/overlap8_v05_results.json`＋`out/v05_runs.json`）＋`regenerate_v04_runs.py`（v0.4 基线重算对照，输出 `out/regen_v04_results.json`＋`out/v04_runs.json`，聚合值与 v0.4 存档全字段全等）＋`build_v05_final.py`（回填＋修复重放，锚点唯一断言内建）；编译产物 `out/walking_with_the_verdicts_v05.{tex,pdf,log}`＋pass1-3.stdout。md 源件与占位版 tex 零触碰。

—— 戴夫-格式专家 ｜ 2026-09-29 ｜ AI 生成
