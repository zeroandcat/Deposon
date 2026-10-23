# Keep the Books — arXiv 投稿包（v4 终版，2026-09-15）

单文件投稿源：`keep_the_books_survey.tex`（article + thebibliography 内联，无外部 bib/图依赖）。tar.gz 包内容 = 本 tex ＋ 本 README（不含 PDF，arXiv 由源码编译；编译验证 PDF 见打包源目录）。

- **内容链头**：查理_第二作综述P1修复版_2026-09-15.md（12,903 词，61 条引用，10 张表；sha256 前缀 bca87448991193f7）
- **v4 = v3 tex ＋ 单句同步**：§9.3 "Limitations, self-stated (compressed from [4])" 句第 3 子句改写（P1 修复，逐字回填第一作自述限制）——旧 "the claims are at the structural-isomorphism level, not magnitude claims" → 新 "apart from the closed verdicts and the kills, the game-theoretic positive evidence is consistency evidence, not formal proof"。**其余 tex 逐字节不动**（逐行核验：557 行中仅第 434 行变化，行内唯一变化片段即该子句）
- **排版基线**：戴夫第三轮重排管线（md2tex_v3，表格防溢出补丁内联，FN1/FN2 落实为 \footnote）——v4 未重跑管线，仅手工单句同步
- **编译**：tectonic 0.15.0（XeTeX，DejaVu Serif 主字体）→ **29 页**（与 v3 同页数）；四零指标：**0 error／0 Overfull／0 缺字形／0 未定义引用**（Underfull 为间距提示，非溢出，与 v3 同口径）
- **渲染级复核**：v3 PDF ↔ v4 PDF 文本逐行 diff——全文唯一变化区域即 §9.3 该段（子句替换＋段内重排换行），其余渲染文本逐行一致；引用 token、冻结数字、§9.3 其余限制子句均不动
- **状态**：**最终投稿包（打包放行）**。双审全 PASS（鲍勃独立双审 2026-09-15 17:20 终裁）→ 已于同日打包：`keep_the_books_arxiv_20260915.tar.gz`（本 tex＋本 README，61 引用 v4）。旧 13:33 的 55 引用版 tar.gz 已作废隔离至 `_obsolete/`，防误取。
- **口径（用户已拍板项）**：AI 披露维持泛称（不点名工具；若后续决定点名，单句重排＋重新打包）；不引 GitHub 仓库（缺省不引，Availability 无 URL 句）；[4] 锚定 arXiv:2609.09001
- **作者声明**：开放署名链（arXiv 式，Author: Qihao Yuan；CC BY 4.0；conflicts: none declared）

## 复现

```
tectonic -X compile keep_the_books_survey.tex   # 输出 29 页 PDF
```

校验工件（管线与复验脚本）：`agents/6a962cc259312f271f3f1e75/second_survey_arxiv/`（md2tex_v3.py、verify13_r3.py、overlap_check_v2.py）。
