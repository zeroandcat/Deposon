# Keep the Books — arXiv 投稿包（v6 收口修复候选，2026-09-16）

单文件投稿源：`keep_the_books_survey.tex`（article + thebibliography 内联，无外部 bib/图依赖）。tar.gz 包内容 = 本 tex ＋ 英文 README（不含 PDF，arXiv 由源码编译；编译验证 PDF 见打包源目录）。

- **内容链头**：查理_第二作综述收口修复版_2026-09-16.md（13,204 词 / wc -w 口径，487 行，61 条引用，10 张表；sha256 前缀 `74bba2fc8bb6`）。该 md 为双审修复后链头：在 v5 重写级源上折叠 P1 修复 21 处＋第二阶段收口 16 处（References 7 条修正 [39][43][44][48][49][51][54]、AI 披露点名 GLM、Table 2 图例行删除、四处簇引 [48–50]、§7.2/§7.3 改写）。
- **v6 与 v4/v5 的关系**：并列候选，非替代。v4/v5 打包基线字节不动仍放行；本 v6 包为送 KIMI 复审的收口修复候选。
- **排版基线**：沿 v5 管线（md2tex_v3 → md2tex_v5，源＝收口修复版 md，整篇重排；FN 机制、术语/连字排版规则、表格防溢出补丁不变）。
- **编译**：tectonic（XeTeX，DejaVu Serif）→ **30 页**；四零指标：**0 error／0 Overfull／0 缺字形／0 未定义引用**（Underfull 15 为间距提示，与 v4/v5 同口径非阻断）。
- **本轮专项核验**：① τ∗（U+2217）在 §9.3 T-P1c 句 PDF 页面级 3 处可见（逐字形无缺字，0 missing character），v5 的 τ\textit 吞字 bug 不再存在；② natbib sort&compress 下 \cite{key48,key49,key50} 全部渲染为压缩区间 [48–50]（PDF 6 处：§7.2、Table 3 ①/⑤/L4 行、§9.2c、OP3），[51] 两处独立成型（§7.2/§7.3 "out of scope [51]"），不并入区间；③ v5↔v6 tex 差异 31 行删改/29 行新增，全部位于两阶段申报变更点（摘要 five→six＋(vi)、§1.2 定位句、§1.3 内部代号清理、Table 2 图例行删除、§3.2 Tier-letter legend 段、§7.2/§7.3 ERC-8004 改写、Table 3/L4 行簇引、§9.2c 完备性措辞、§9.3 complete/underflow/收尾红线、OP3/OP8、Availability、AI 披露 GLM、References 7 条），无一例外。
- **自引重叠复算（v4 口径，重排后刷新）**：§9.3 = **4.62%**（60/1298 词：分子与 v4/v5 相同 60 词，分母 +1 词致 4.63%→4.62%）、全文其余 = 0.21%（26/12643）、8-gram 全文 0.91%；匹配片段均为申报锚定物＋两条共享参考文献题名。**tex Availability 句已按派单刷新为 4.62%/0.21%**（与 md 链头的唯一一处数字差异，已在重排说明申报）。
- **README 口径修正（总裁决项）**：v5 README 的「75 表行/138 token」为无口径声明、审稿方不可复现——本版 README 改为显式口径：表行 65（含表头）/55（数据行）（tabularx 环境内 `\\` 结尾行）；§9.3 数字 token 134（`re.findall(r'\d[\d,\.]*')` 口径）。稿件内容零改动。
- **双盲/合规扫描**：红线词（staking/composing protocol/PoA/Ethereum RFC/ethereum-magicians/Econometrica/exhaustive/second-round/final draft/phase draft/KIMI/GAP-/TODO 等）全零；作者名仅存于 hyperref pdfauthor、\author（公开署名惯例）与 [4] 自引披露三处；唯一 URL＝[51] 工程标准草案的 eips.ethereum.org 题录地址（文献字段，非作者信息）；v1/v2 字样仅存于 §9.3 冻结 SHA 锚文件名与 arXiv 版本注记（既有披露口径）。
- **口径（用户已拍板项）**：AI 披露点名 GLM；不引 GitHub 仓库；[4] 锚定 arXiv:2609.09001。
- **验证工件（内部）**：`agents/6a962cc259312f271f3f1e75/v6_retypeset/`（md2tex_v6.py、overlap_check_v6.py、编译日志、v5_v6.diff）。
