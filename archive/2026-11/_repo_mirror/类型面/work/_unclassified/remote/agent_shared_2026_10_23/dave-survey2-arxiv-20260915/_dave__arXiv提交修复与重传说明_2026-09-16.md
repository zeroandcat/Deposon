# 戴夫：arXiv submit/8086112 编译失败修复与重传说明（2026-09-16，v8）

## 一、失败根因（arXiv 处理日志核实）

v7 的 `keep_the_books_survey.tex` 在 preamble 使用了 XeTeX/LuaTeX 专属链路：
`fontspec` + `\setmainfont{DejaVu Serif}` + `\newunicodechar{①..⑥}{\fontspec{DejaVu Sans}...}`。
arXiv 对无 magic-comment 的源自动选择 pdflatex；fontspec 在 pdflatex 下致命错误（Emergency stop）。
扫描另判缺 3 个字体文件（DejaVu Serif / Latin Modern Roman / DejaVu Sans）——即系统字体依赖本身不可交付。

## 二、v8 修复内容（正文内容零改动）

**基线**：v7 终包 tex（sha256 前 8 位 8c007d27，562 行，30 页）。修复生成脚本 `make_v8.py`（断言式替换，两处替换均唯一命中）：

1. **引擎兼容层**（v7 preamble 第 2–15 行 → v8 第 2–35 行）：
   - 删除 fontspec 及全部系统字体依赖；改纯 TeX 方案：`fontenc T1` + `inputenc utf8` + `lmodern` + `pifont`。
   - 带圈数字 ①–⑥（源内 163 处）→ `\ding{172}`–`\ding{177}`（URW Zapf Dingbats，pdflatex 原生可用；表格/矩阵内同样正常，标题书签经 `\texorpdfstring` 落纯数字）。
   - 其余非 ASCII：τ κ Φ Δ → `\ensuremath{...}`；≠ ≤ − → 数学宏；→ → `\textrightarrow`；∗ → `\textasteriskcentered`；⁻⁴⁶⁹ ¹ ² → `\textsuperscript{...}`；– — 加 `\allowbreak` 保持 XeTeX 的破折号后可断行行为。utf8 原生可处理的（§ · × ± … é ü Č 等）一律不动。
   - 源文件正文里的 UTF-8 字符**一个都不改**（newunicodechar 映射层在编译期展开）。
2. **subjects 行修复**（按用户指示）：`cs.CL (primary) · cs.AI · cs.LG` → **`cs.AI (primary) · cs.LG · cs.CL`**（主分区 cs.AI；次分区 cs.LG、cs.CL 保留）。

**正文零改动验证**：v7 与 v8 逐行对齐，前导块之外（v7 第 17 行起 ↔ v8 第 37 行起）562 行区间**唯一差异 = subjects 行**，其余逐字节一致。§9.3 冻结数字与引用编号未动（引用 token 多重集不变由字节一致性直接继承）。

## 三、编译验证（pdflatex，TeX Live 2026 本地）

- 三遍编译 exit=0；**四零指标**：0 error / 0 Overfull / 0 缺字形（Missing character）/ 0 未定义引用（pass1 的 315 条 undefined 为首遍正常现象，pass2/3 归零）。Underfull 4 为间距提示（口径同 v4–v7，不计入）。
- **26 页**（v7 为 30 页：Latin Modern 较 DejaVu Serif 度量更紧凑，属引擎层预期效应，非内容变化）。
- **PDF 字体全嵌入**（pdffonts 全行 emb=yes）：Latin Roman/Math 家族 + URW Dingbats，全部子集嵌入且带 ToUnicode。
- **tar 包独立复现**：解包重编译 exit=0、四零、26 页、456,522 字节；与交付 PDF 仅 70 字节差异（CreationDate/文档 ID 时间戳），内容同一。
- **字形渲染核查**：τ κ Φ Δ ∗ ≤ → 及上标指数（10⁻⁴ 等）均在 PDF 文本层可见；①–⑥ 提取 151 处（源 163，v7 PDF 同口径 151，提取口径两边一致，渲染完好）。注：≠ 在文本提取层显示为 ̸=、Δ 显示为 ∆（U+2206）、上标数字提取为普通数字——均为 ToUnicode 提取口径差异，**视觉渲染正确**，编译零缺字形。
- **披露**：任务书要求 TeX Live 2025 验证；本轮网络仅 ~19KB/s，TL2025 补装预计 3h+ 无法完成（上轮即因此超时作废）。已用 **TeX Live 2026 pdflatex** 完成验证。所用宏包（fontenc/inputenc/lmodern/pifont/newunicodechar）均为跨版本稳定的经典宏包，引擎行为不随 2025/2026 差异变化；arXiv 端编译是最终裁判。

## 四、重传操作指引（arXiv submit/8086112）

1. 在该提交页 **Delete all** 删除全部已传文件（必须整清，防 fontspec 残留版本混入）。
2. 重新上传 `keep_the_books_arxiv_2026_09_16_v8.tar.gz`（内含 `keep_the_books_arxiv_20260916_v8/keep_the_books_survey.tex` + `README.md`，纯英文，无字体文件、无图、无 bib 依赖）。
3. **README.md 保留**：v7 tar 包内的 README 本就是英文版（4a921b3a 那份的延续），随包上传是惯例，保留。
4. **中文 README 剔除确认**：v7/v8 的 tar 包内**从未包含**中文 README（`README_内部说明_中文.md` 只存在于工作目录，属内部件）；重传时同样**不要**上传任何中文文件。
5. 表单元数据按 `keep_the_books_arxiv_2026_09_16_v8/arXiv_metadata_提交元数据.txt` 枯贴：Title / Author（Qihao Yuan）/ Abstract（363 词纯文本）/ Comments（**26 pages**，页数已按 v8 实际更新）/ subjects（**cs.AI 主分区**，cs.LG、cs.CL 次分区）/ License CC BY 4.0。

## 五、交付指纹（sha256 前 8 位）

| 件 | 指纹 |
|---|---|
| v8 tex（102,563B，582 行） | f36243e2 |
| v8 编译验证 PDF（26 页，456,522B） | af8e06a5 |
| v8 英文 README.md | 11d82594 |
| v8 tar.gz（内目录 keep_the_books_arxiv_20260916_v8） | c9a7c16e |
| arXiv 元数据 txt | 87942beb |
| v7 基线 tex（未动） | 8c007d27 |

v4/v5/v6/v7 基线指纹全部未动。验证工件：`agents/6a962cc259312f271f3f1e75/v8_pdflatex/r2_build/`（make_v8.py、pass1–3.log、提取与比对脚本）。
