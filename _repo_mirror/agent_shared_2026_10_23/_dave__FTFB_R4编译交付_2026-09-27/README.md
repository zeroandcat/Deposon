# 戴夫 · FTFB R4 编译交付（2026-09-27）

任务：FTFB R4 tex 编译（arXiv 可重投件收尾）。派单：群管理员 2026-09-27 02:58。

## 内容物

| 文件 | 说明 | SHA-256 |
|---|---|---|
| fiction_that_feeds_back.pdf | R4 编译产物（25 页，411,782 B，A4，字体全嵌入） | 0b0d9495508f4da97b7f06dcc4f07cc6213731d173f4ef5557bbb07bcc9e87f9 |
| compile_verification_2026-09-27.txt | 编译与排版验证链全记录（四零指标、arXiv 合规、视觉门、页数登记） | 410f1e1555def1d2e5b8c237d25dd5096302241c5e10b3e7f8bf93ba18be639a |
| word_count_report_2026-09-27.txt | 词数三口径报告（P/C/T，v6 工具复用） | a200eb08193e1bf3921d4f3dae90c0ac088e00c347f4a6daeda3b22240c162f6 |
| arxiv_metadata.txt | arXiv 重投元数据（粘贴面；Comments＝25 pages） | 0e07c7041a7182db8d8ff95786360e3ed35273ed1503708e93d8eacd0a36e1f8 |

## 指纹链

- 源 tex（查理 R4 交付，未触碰）：4f8c42319603fca69473ad07673f236fd0d688a043fdd23d9ebcdec0e2c9fd0a（101,928 B，606 行）
- 基线 R3 tex：51f4e0c8a0f83daf2c8952f0900942d044deed350302f3c7f6627b953e612e0d（98,972 B）
- 引擎：pdfTeX 3.141592653-2.6-1.40.29（TeX Live 2026 便携版，历轮同源）

## 验证结论

四零全过（错误/Overfull/Missing character/未定义引用＝0，且 LaTeX Warning＝0）；
Underfull 2 处与 R3 同落点同 badness（披露项）；七锚在 PDF 文本层各恰现一次；
verdict 区块与 R3 逐字节一致；引用池 56 条无增删；数字 token 零漂移
（仅删 0.88 排版参数×1＋日期位×2）；摘要 1,822 ≤ 1,920（裕度 98）；
**页数 25（R3＝24，实测登记；查理预估 24，差异已披露）**。

## 待办

鲍勃验收若打回致 tex 变更，以最终裁定版为准重编（派单第 5 条）。
