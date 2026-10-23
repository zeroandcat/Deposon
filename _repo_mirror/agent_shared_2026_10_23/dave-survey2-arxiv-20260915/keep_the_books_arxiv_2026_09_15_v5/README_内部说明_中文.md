# Keep the Books — arXiv 投稿包（v5 重写级候选，2026-09-15）

单文件投稿源：`keep_the_books_survey.tex`（article + thebibliography 内联，无外部 bib/图依赖）。tar.gz 包内容 = 本 tex ＋ 本 README（不含 PDF，arXiv 由源码编译；编译验证 PDF 见打包源目录）。

- **内容链头**：查理_第二作综述英文重写版_2026-09-15.md（13,070 词，61 条引用，10 张表；sha256 前缀 3da418383ca37dd2；鲍勃独立复核全 PASS，2026-09-15 18:33）
- **v5 与 v4 的关系**：并列候选，非替代。不变式从 v4 tex 字节级承载：References（61 条）、全部 10 张表（75 表行）、FN1/FN2 脚注定义、§9.3 锚定段（self-stated limitations 含 5 枚 SHA-256 预登记锚、Matrix row 6、收尾红线段）与 v4 基线字节一致；例外＝申报的 1 处句读变化（Position and disclosure 冒号→句号）与 2 处定义句法变化（文首三档证据定义、§1.3 规则三句读）。其余差异全部位于重写版自由行文区（摘要、§1–§8 正文、§9.1–9.2、§10、back matter）
- **排版基线**：沿用 v4 管线（md2tex_v3 → md2tex_v5，源＝英文重写版 md，整篇重排；FN 注释行机制、术语/连字排版规则、表格防溢出补丁均不变）
- **编译**：tectonic（XeTeX，DejaVu Serif 主字体）→ **30 页**（v4 为 29 页，+167 词所致）；四零指标：**0 error／0 Overfull／0 缺字形／0 未定义引用**（Underfull 40 为间距提示，与 v4 同口径）
- **渲染级复核**：§9.3 清洗页码/断字伪影后逐字对照——唯一内容差异＝申报句读变化（`: i` → `. I`），其余为表格浮动位置随页流重排；全文数字 token 多重集与 v4 一致（唯一差异＝第 30 页页码）；正文流引用首现 1→61 严格单调（剔脚注体口径，FN1 脚注体 [31]/[51] 指称沿 v4 披露口径不计入）
- **自引重叠复算（v4 口径）**：§9.3 = 4.63%（v4 基线 4.63–4.65）、全文其余 = 0.21%、8-gram 全文 0.92%（v4 参考 0.93）——匹配片段均为申报锚定物＋两条共享参考文献题名
- **状态**：**并列候选（用户选定）**。v4 打包基线不动仍放行；本 v5 包为送 KIMI 严格双审的另一候选。旧 13:33 的 55 引用版 tar.gz 仍在 `_obsolete/` 隔离中
- **口径（用户已拍板项）**：AI 披露维持泛称（不点名工具）；不引 GitHub 仓库；[4] 锚定 arXiv:2609.09001
- **作者声明**：开放署名链（arXiv 式，Author: Qihao Yuan；CC BY 4.0；conflicts: none declared）

## 复现

```
tectonic -X compile keep_the_books_survey.tex   # 输出 30 页 PDF
```

校验工件（管线与复验脚本）：`agents/6a962cc259312f271f3f1e75/v5_retypeset/`（md2tex_v5.py、verify_v5_part1.py、verify_v5_part2.py）。
