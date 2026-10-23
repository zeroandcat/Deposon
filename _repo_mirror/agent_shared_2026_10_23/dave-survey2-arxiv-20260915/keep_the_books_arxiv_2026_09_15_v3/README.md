# Keep the Books — arXiv 投稿包（第三轮暂存版，2026-09-15）

单文件投稿包：`keep_the_books_survey.tex`（article + thebibliography 内联，无外部 bib/图依赖）。

- **内容链头**：查理_第二作综述格式归位版_2026-09-15.md（12,895 词，61 条引用，10 张表）
- **排版**：戴夫第三轮重排（md2tex_v3 管线，表格防溢出补丁已内联；FN1/FN2 已落实为 \footnote）
- **编译**：tectonic 0.15.0（XeTeX，DejaVu Serif 主字体）→ 29 页；0 error／0 Overfull／0 缺字形／0 未定义引用
- **状态**：**tar.gz 打包件暂不出**——等独立双审结论；双审全 PASS 后以本目录 tex 为源直接打包（打包时须按双审结论更新本 README 状态行）
- **作者声明**：开放署名链（arXiv 式，Author: Qihao Yuan；CC BY 4.0；conflicts: none declared）

## 复现

```
tectonic -X compile keep_the_books_survey.tex   # 输出 29 页 PDF
```

校验工件（管线与复验脚本）：`agents/6a962cc259312f271f3f1e75/second_survey_arxiv/`（md2tex_v3.py、verify13_r3.py、overlap_check_v2.py）。
