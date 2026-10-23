# 戴夫·第三作 v0.4 终收尾交付报告（原链复测→回填→编译→合规）

**日期**：2026-09-28
**执行**：戴夫-格式专家
**任务书口径**：五件＝①8-gram 原链复测（与鲍勃重建值交叉验证）②R8/§22.5 回填（终值口径沿既定规则）③三遍收敛编译 ④arXiv 投稿合规检查 ⑤页数与双盲终审登记。

---

## 一、8-gram 原链复测（任务 1）

**工具链**：`agents/…e75/third_paper_v04/scripts/overlap8_final_v04.py`——v9 轮 `overlap_check_v2.py` 口径逐位复刻（norm_words 词级归一化／strip_tex／首现贪心扩展／覆盖率分母＝查询件），与 v0.3 轮 `overlap8_final.py` 同链。**参照件 sha 锁定**：第一作 arXiv tar 内 `deposon_paper_en.tex`（0d5679110aba…，即 v0.3 轮同件）、第二作 FTFB R4 `fiction_that_feeds_back.tex`（4f8c42319603…，与鲍勃同件）。
**措辞注记**：派单写「第一作 arXiv tar 内 md（v9 轮旧口径）」；v9 轮旧口径实际载体＝tar 内 **tex**（tar 内 md 仅 README 非正文），本轮沿 v9/v0.3 原链用 tex，未改口径。

**原链 v0.4 实测值**：

| 量 | vs 第一作（arXiv tex） | vs 第二作（FTFB R4 tex） |
|---|---|---|
| 全文 8-gram | **0.55%**（164 词／13 run／30,090 tokens） | **0.63%**（191 词／16 run／30,090 tokens） |
| 剔题录（净正文 28,146） | **0.46%**（130 词） | **0.32%**（91 词） |
| 题录块内（1,944） | 34 词 | 100 词 |
| §18.1 8-gram | 8.10%（103 词／1,271） | 7.16%（91 词／1,271） |
| §18.1 10-gram | **5.51%**（70 词） | 5.82%（74 词） |

分区闭合自证：164＝103（§18.1）＋27（正文他处）＋34（题录）；191＝91＋0＋100。

**同链对照（v0.3→v0.4）**：vs 一作 164w/13run→164w/13run、vs 二作 191w/16run→191w/16run，**零变化**——原链独立证实「v0.4 注册层新增 1,725 tokens 零 8-gram 匹配」。**C 类 14 run 逐条人工复核**：全部为申报锚定物（第一作/第二作各自注册转写的数字串、注册引语「keeps the books / machine verifiability / consistency evidence not formal proof」、账目语「T,R,A shares」、守恒句 2.22e-16、枚举口径 61 graphs/6,760 states、T-P1b 句），与鲍勃 v0.3 轮 §三分类吻合——**自由文本 0 词在原链口径下成立**。

## 二、两源对照与终值裁定（任务 2 前半）

| 量 | 原链（本轮） | 鲍勃重建（v0.4 报告） | 关系 |
|---|---|---|---|
| 分母（全文/题录/净正文/§18.1） | 30,090/1,944/28,146/1,271 | 同 | **全等**（分词器同构） |
| vs 一作 全文 | 0.55%（164w） | 0.71%（214w） | 词数 +30.5%，与 v0.3 轮两链差（164↔214）**同构零漂移** |
| vs 二作 全文 | 0.63%（191w） | 0.82%（246w） | 词数 +28.8%，同构零漂移 |
| 剔题录 | 0.46%/0.32% | 0.55%/0.44% | 同向偏高 |
| §18.1 十克 vs 一作 | **5.51%（70w）** | **5.51%（70w）** | **两链同值** |
| 注册层新增匹配 | 零（集合同 v0.3） | 零（+1,725 零匹配） | **结论互证** |
| 自由文本 | 0 词（14 run 逐条复核） | 0 词（37 run 逐条分类） | **结论互证** |

差异来源：参照面（其 final_en.md 10,743 tokens vs 原链 arXiv tex 10,173 词）＋贪心延伸细节；其自称「保守偏高 ~10%」系对 v9 单作先例校准（127→139），对第三作合并稿口径实际偏高 ~30%，如实登记。

**终值裁定（派单规则：原链复测成功→原链值为准）**：复测成功判据齐备（脚本运行、分母与鲍勃全等、匹配集与 v0.3 同链零漂移、C 类逐条复核通过）→ **终值＝原链值**：vs 一作 **0.55%**（164/30,090；净 0.46%）、vs 二作 **0.63%**（191/30,090；净 0.32%）、§18.1 十克 **5.51%**；鲍勃重建值（0.71%/0.82% 等）以交叉验证身份留档于 R8 条目内。

## 三、R8/§22.5 回填（任务 2 后半）

**四处回填**（tex 载体；**md 链头占位不回改**，沿旧例差异声明——md 三处占位原样，为内容记录面）：

1. **R8 条目**：`placeholder, open`→`registered, closed (backfilled at the typesetting round, 2026-09-28)`，载终值（含工具链口径、参照面、分类结论、v0.3 基线集不变、鲍勃重建交叉验证、终值依据＝same-chain precedent）；条目尾段（disclosure category 更名＋survey 单作先例三值）逐字保留。
2. **§22.5 披露句**：占位句→终值披露句（0.55%/0.63% 全文、0.46%/0.32% 净正文、锚定物/题录分类、零自由文本、R8 注册指向＋保守偏高重建值随档）。
3. **§21(8) deferral 子句同步改写**：「is deferred to the typesetting round (Section 22.5)」→「is registered in Section 22.5 and Appendix C (R8)」。
4. **tex 头部 deferred 注记改写**：两源值＋终值依据＋md 占位不回改声明全量登记。

**回填后终版保真：32 项零 FAIL**（`fidelity_check_v04_final.py`，可复跑）：原 20 项标准＋注册层专项沿旧全过；占位两查翻转为回填注册断言；新增回填在场/残留清零/头部两源登记/H3 声名改写归一化（归一化后 187 tok 全等，证除声明子句外零漂移）。

## 四、编译（任务 3）

三遍 pdflatex 全 exit 0（TeX Live 2026，v0.3 轮同环境）。**零 error／零 undefined reference／零 multiply defined**；页数 **55**（v0.3 语法自检版 52 页，增量＝v0.4 注册层＋回填＋表格重排）；PDF 667,746 B。

**Overfull 17→0 处置表**（全部格式层修复，零文字变化，修复后保真 32 项＋colspec 24/24 复验）：

| 处 | 原宽溢 | 修复 |
|---|---|---|
| 标题页（\maketitle 作者行） | 223.3pt（article 类作者行不折行，v0.3 轮同款遗留） | 作者行加 `\\` 断行（探针验证归零） |
| 表 0（§1.2）末列 | 3.0pt×2（"commitment"） | p{0.11}→p{0.125} |
| 表 9（§12.3）末列 | 3.0pt（"Measured"） | 末列 l→p{0.30}（Root-cause 长列不再挤压 X） |
| 表 4（六块链表） | 1.6–23.4pt×10 | 第 4 列 p{0.20}→p{0.145}，X 列回收 26pt |
| 表 5（合并矩阵） | 43.6/49.7pt（不可断斜杠复合词） | rationalization/、benchmark/、protocol/ 后加 `\allowbreak{}` 断点（渲染字符不变） |
| App C.1 表 | 19.7pt（行溢） | 首列 l→p{0.145}、末列 0.58→0.55 |

Underfull 残留 30（间距提示级，v1.1 体例接受带，如实登记）。

## 五、arXiv 投稿合规（任务 4）

- **体例**：英文 arXiv 预印、pdflatex、11pt article；宏包全标准（fontenc/inputenc/lmodern/geometry/booktabs/tabularx/longtable/array/pifont/CJKutf8/hyperref(unicode)）——arXiv 全支持。
- **包结构/文件名**：单 tex 自含（无图、无 .bib，References 手排）→上传件＝1 个 tex（建议上传时更名 `main.tex`）；PDF 667,746 B／tex 213,041 B，远低于限额。
- **注释残留**：20 行注释全在头部（英文，零姓名/路径/身份），系排版轮注册记录（源 SHA、两源值、终值依据），保留为溯源链；PI 可在上传时剥离，对 PDF 零影响。
- **双盲（人名向）**：PDF metadata Author 空／Title＝论文题／Creator＝LaTeX with hyperref；书签零疑点；正文/文本层人类作者名零命中（Qihao Yuan 等 0 处）；「Attribution withheld」三处（标题页作者块、摘要区作者注、References [4] 一作条目）均注册内容。
- **字体嵌入**：pdffonts 53 字体全嵌入＋子集化（LMRoman/LMMono/Dingbats/gbsnu CJK 系）——**v0.3 轮 pending 项关闭**。
- **披露项（交 PI 裁定，本轮未动）**：App A 三个溯源锚文件名含角色中文名（`查理_FTFB_R4更新交付…`、`戴夫_FTFB_R4编译交付…`、`鲍勃_v1.1新增数字补测复核…`）＋一处路径前缀 `dave-survey2-arxiv-20260915`。系 **md 注册内容**（v0.3/v0.4 保真链内，PDF 文本层随 CJK 渲染在场），非排版层引入；无人类作者身份泄露。先例：FTFB B01 卫生轮曾将中文注释英译、剥本地路径——如 PI 要求同标处置，属内容改动（锚字符串中性化），应开查理轮，本轮保持 md↔tex 保真未动。
- 口径侧证：模型名字面 md↔tex 全等（minimax 3=3／kimi 4=4／coze 3=3，注册内容）。

## 六、终审登记（任务 5）

- **页数**：55 页（A4？否——US letter 1in geometry，v1.1 体例）。
- **双盲终审**：metadata／书签／文本层人名零命中；**一项披露待 PI**（App A 角色名，见 §五）。
- **诚实张力登记（供 PI/查理后续轮参考，本轮未动正文）**：§22.5 前文「expected to be substantially higher than the survey's single-work values」——在匹配词数（164 vs 127）与案例节十克（5.51% vs 4.62%）口径成立；在全文率口径因分母翻倍（13,943→30,090）稀释不成立（0.55% vs 0.91%）。鲍勃 v0.3 轮已双向如实报告，本轮回填句取中性数值披露不预设立场。

## 七、交付物清单（shared/戴夫_第三作排版交付_2026-09-28/）

| 文件 | 指纹 | 说明 |
|---|---|---|
| `_v3v4_merged_paper_2026_09_27_v0.4_final.tex` | 213,041 B／884 行／SHA-12 `fd5f915699d4` | 回填后终版 tex（R8/§22.5/§21(8)/头部四处回填＋Overfull 归零修复） |
| `_v3v4_merged_paper_2026_09_27_v0.4_final.pdf` | 667,746 B／55 页／SHA-12 `178f367f2ca6` | 三遍收敛编译终版 PDF（零 error/undefined/multiply/Overfull） |
| `戴夫_第三作v0.4终收尾报告_2026-09-28.md` | 本报告 | 五任务全记录 |
| （前轮件不动）`_v3v4_merged_paper_2026_09_27_v0.4.tex`＋保真报告 | 4b513e2dc6e6 | 转换轮存档（占位版，本报告的前件） |

工具链（私有区可复跑）：`third_paper_v04/scripts/`＝`overlap8_final_v04.py`（原链复测，输出 `out/overlap8_v04_results.json`）＋`fidelity_check_v04_final.py`（32 项，输出 `out/fidelity_check_v04_final.json`）＋`build_third_tex_v3.py`（转换轮）；colspec 检查沿 v03 轮脚本。v0.3 轮交付目录零触碰。

—— 戴夫-格式专家 ｜ 2026-09-28 ｜ AI 生成
