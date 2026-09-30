# 归档区清理扩展棒 · 三类清走＋论文产物冻结登记（2026-09-28 晚）

> 拍板来源：`ask_f25f4117ca57d71f000afb16`（2026-09-28 19:19）· PI 三项全放行 ＋ `rendered_arxiv` 冻结
> 承接棒：`results/_archive_cleanup_non_upload_2026_09_28.md`（`34f2c63306b8`，本棒 **0 触动**）
> 本棒为**新名件**，未覆盖、未回改、未移动上棒任何登记件/manifest

| 项 | 值 |
|---|---|
| 归档区 | `D:\私人资料\_non_upload_local_archive` |
| manifest v3 | `_archive_manifest_non_upload_v3_2026_09_28.json`（SHA-12 `a2e4c5a9b713`） |
| 清走 | **163 件 · 5,758,232 B（5.49 MiB）**，全部可恢复 |
| 减量留置 | **9 件** |
| 冻结登记 | **47 件 · 12,419,015 B（11.84 MiB）** `cache/cache/rendered_arxiv/` |
| 永久删除 / 绕过恢复机制 | **0 / 0** |
| 转移 | **0 件** |

## 1. 拍板执行口径与三类的实际重叠关系

PI 放行三类：① 清单式引用件（173）② 空日志余 84 ③ KaTeX 第三方 63。**实测三者并非互斥**：
上棒 §3.1 的 173 件清单**本身就包含**全部 84 件空日志与全部 63 件 KaTeX（84 + 63 均为 173 的真子集），
故**并集 = 173 件**，非 173 + 84 + 63。派工单预估「~8.5 MiB」系把 KaTeX（1.31 MiB）与空日志重复计入所致。

| 面 | 派工单口径 | 实测并集口径 | 关系 |
|---|---:|---:|---|
| 清单式引用 173 | 173 件 | 165 件可清 | 173 − 7 证据件 − 1 冻结件 |
| 空日志余 84 | 84 件 | 已含于上 | 84 ⊂ 173 |
| KaTeX 63 | 63 件 | 已含于上 | 63 ⊂ 173 |
| **并集** | 320 件（重复计） | **163 件 · 5.49 MiB** | 去重 + 减量 + 冻结 |

## 2. 173 件的逐件分解与减量判定

派工单授权「**若发现实质引用/证据属性如实减量**」。逐件过引用出处后 **减量留置 9 件**：

| # | 路径 | 字节 | 留置理由（实测） |
|---:|---|---:|---|
| 1 | `__pycache__/fingerprint_v0.cpython-312.pyc` | 9,586 | **证据式引用**：被 09-23 幽灵引用对账件以 sha12 为键判定，属判定链输入 |
| 2 | `cache/cache/v2/outline_v2X.md` | 0 | **论文正文唯一副本**：全仓无同值副本；同目录另 4 件论文正文上棒即按「论文正文与修订记录」留置 |
| 3 | `cache/cache/v2/related_work_v2X.md` | 0 | **论文正文唯一副本**：同上 |
| 4 | `deposon_team/plugins/__pycache__/boss_pa_1_rbr_rm.cpython-314.pyc` | 19,744 | **清理台账式引用**：09-24 清理台账以该件记录清走事实 |
| 5 | `deposon_team/plugins/__pycache__/boss_pa_3_replicator_dynamics.cpython-314.pyc` | 13,660 | **清理台账式引用**：同上 |
| 6 | `tmp/__pycache__/fingerprint_v0.cpython-312.pyc` | 9,586 | **证据式引用**：同上 |
| 7 | `verifier/audit/__pycache__/conservation.cpython-312.pyc` | 2,859 | **证据式引用**：同上 |
| 8 | `verifier/audit/__pycache__/conservation.cpython-314.pyc` | 3,266 | **证据式引用**：同上 |
| 9 | `verifier/kill_lines/__pycache__/kt_b1_kill_decision.cpython-314.pyc` | 3,046 | **证据式引用**：同上 |

**减量合计 9 件 · 61,747 B**，其中 7 件为「引用出处≠09-24 盘点表」的 `.pyc`（清单式引用之外的**证据/台账属性**），2 件为论文正文唯一副本。

## 3. 清走逐件表（三类并集 · 163 件 · 5,758,232 B）

| # | 路径 | SHA-12 | 字节 | 归类 |
|---:|---|---|---:|---|
| 1 | `cache/cache/deposon_arxiv_2026/figures/fig1_boundary_map_cn.png` | `cc1067863adc` | 360,334 | 图片派生(他处同值) |
| 2 | `cache/cache/deposon_arxiv_2026/figures/fig1_boundary_map_en.png` | `921ea0ea7637` | 360,057 | 图片派生(他处同值) |
| 3 | `cache/cache/deposon_arxiv_2026/figures/fig2_killsign_scatter_cn.png` | `239b1411d3dd` | 259,257 | 图片派生(他处同值) |
| 4 | `cache/cache/deposon_arxiv_2026/figures/fig2_killsign_scatter_en.png` | `02d70bb1bd2c` | 248,010 | 图片派生(他处同值) |
| 5 | `cache/cache/deposon_arxiv_2026/figures/fig3_division_scatter_cn.png` | `66c805d0d97a` | 286,354 | 图片派生(他处同值) |
| 6 | `cache/cache/deposon_arxiv_2026/figures/fig3_division_scatter_en.png` | `a848305eefe7` | 278,252 | 图片派生(他处同值) |
| 7 | `cache/cache/deposon_arxiv_2026/figures/fig4_gt7_frontier_cn.png` | `22af20586904` | 564,880 | 图片派生(他处同值) |
| 8 | `cache/cache/deposon_arxiv_2026/figures/fig4_gt7_frontier_en.png` | `2d6d935fb369` | 542,421 | 图片派生(他处同值) |
| 9 | `cache/cache/deposon_arxiv_2026/figures/fig5_poa_distribution_cn.png` | `b98338c10913` | 443,481 | 图片派生(他处同值) |
| 10 | `cache/cache/deposon_arxiv_2026/figures/fig5_poa_distribution_en.png` | `decfbd34d9ed` | 442,102 | 图片派生(他处同值) |
| 11 | `cache/cache/pdfbuild/auto-render.min.js` | `e5372d199bcd` | 3,486 | KaTeX3P |
| 12 | `cache/cache/pdfbuild/fig1_architecture.png` | `565e2bf0ad14` | 237,230 | 图片派生(他处同值) |
| 13 | `cache/cache/pdfbuild/fig1_architecture_en.png` | `2c50ac66e20f` | 358,536 | 图片派生(他处同值) |
| 14 | `cache/cache/pdfbuild/fonts/KaTeX_AMS-Regular.ttf` | `68534840bcfd` | 63,632 | KaTeX3P |
| 15 | `cache/cache/pdfbuild/fonts/KaTeX_AMS-Regular.woff` | `30da91e84c89` | 33,516 | KaTeX3P |
| 16 | `cache/cache/pdfbuild/fonts/KaTeX_AMS-Regular.woff2` | `0cdd387c9590` | 28,076 | KaTeX3P |
| 17 | `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Bold.ttf` | `07d8e303ce4f` | 12,368 | KaTeX3P |
| 18 | `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Bold.woff` | `1ae6bd747559` | 7,716 | KaTeX3P |
| 19 | `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Bold.woff2` | `de7701e42cf1` | 6,912 | KaTeX3P |
| 20 | `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Regular.ttf` | `ed0b74372fee` | 12,344 | KaTeX3P |
| 21 | `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Regular.woff` | `3398dd023025` | 7,656 | KaTeX3P |
| 22 | `cache/cache/pdfbuild/fonts/KaTeX_Caligraphic-Regular.woff2` | `5d53e70ad607` | 6,908 | KaTeX3P |
| 23 | `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Bold.ttf` | `9163df9c7122` | 19,584 | KaTeX3P |
| 24 | `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Bold.woff` | `9be7ceb88004` | 13,296 | KaTeX3P |
| 25 | `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Bold.woff2` | `74444efd593c` | 11,348 | KaTeX3P |
| 26 | `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Regular.ttf` | `1e6f9579e90e` | 19,572 | KaTeX3P |
| 27 | `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Regular.woff` | `5e28753be717` | 13,208 | KaTeX3P |
| 28 | `cache/cache/pdfbuild/fonts/KaTeX_Fraktur-Regular.woff2` | `51814d270d06` | 11,316 | KaTeX3P |
| 29 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Bold.ttf` | `138ac28d1663` | 51,336 | KaTeX3P |
| 30 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Bold.woff` | `c76c5d696297` | 29,912 | KaTeX3P |
| 31 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Bold.woff2` | `0f60d1b89793` | 25,324 | KaTeX3P |
| 32 | `cache/cache/pdfbuild/fonts/KaTeX_Main-BoldItalic.ttf` | `70ee1f64a20f` | 32,968 | KaTeX3P |
| 33 | `cache/cache/pdfbuild/fonts/KaTeX_Main-BoldItalic.woff` | `a6f7ec0d846a` | 19,412 | KaTeX3P |
| 34 | `cache/cache/pdfbuild/fonts/KaTeX_Main-BoldItalic.woff2` | `99cd42a3c072` | 16,780 | KaTeX3P |
| 35 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Italic.ttf` | `0d85ae7cc30f` | 33,580 | KaTeX3P |
| 36 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Italic.woff` | `f1d6ef86f3b1` | 19,676 | KaTeX3P |
| 37 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Italic.woff2` | `97479ca6cce9` | 16,988 | KaTeX3P |
| 38 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Regular.ttf` | `d0332f528683` | 53,580 | KaTeX3P |
| 39 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Regular.woff` | `c6368d87e8a1` | 30,772 | KaTeX3P |
| 40 | `cache/cache/pdfbuild/fonts/KaTeX_Main-Regular.woff2` | `c2342cd8b869` | 26,272 | KaTeX3P |
| 41 | `cache/cache/pdfbuild/fonts/KaTeX_Math-BoldItalic.ttf` | `f9377ab0271c` | 31,196 | KaTeX3P |
| 42 | `cache/cache/pdfbuild/fonts/KaTeX_Math-BoldItalic.woff` | `850c0af5c223` | 18,668 | KaTeX3P |
| 43 | `cache/cache/pdfbuild/fonts/KaTeX_Math-BoldItalic.woff2` | `dc47344dbb6c` | 16,400 | KaTeX3P |
| 44 | `cache/cache/pdfbuild/fonts/KaTeX_Math-Italic.ttf` | `08ce98e51b04` | 31,308 | KaTeX3P |
| 45 | `cache/cache/pdfbuild/fonts/KaTeX_Math-Italic.woff` | `8a8d24458137` | 18,748 | KaTeX3P |
| 46 | `cache/cache/pdfbuild/fonts/KaTeX_Math-Italic.woff2` | `7af58c5ec8f1` | 16,440 | KaTeX3P |
| 47 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Bold.ttf` | `1ece03f79f95` | 24,504 | KaTeX3P |
| 48 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Bold.woff` | `ece03cfd83e2` | 14,408 | KaTeX3P |
| 49 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Bold.woff2` | `e99ae51144bf` | 12,216 | KaTeX3P |
| 50 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Italic.ttf` | `3931dd81faed` | 22,364 | KaTeX3P |
| 51 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Italic.woff` | `91ee67500cc0` | 14,112 | KaTeX3P |
| 52 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Italic.woff2` | `00b26ac825e2` | 12,028 | KaTeX3P |
| 53 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Regular.ttf` | `f36ea897e19f` | 19,436 | KaTeX3P |
| 54 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Regular.woff` | `11e4dc8a6471` | 12,316 | KaTeX3P |
| 55 | `cache/cache/pdfbuild/fonts/KaTeX_SansSerif-Regular.woff2` | `68e8c73ef42a` | 10,344 | KaTeX3P |
| 56 | `cache/cache/pdfbuild/fonts/KaTeX_Script-Regular.ttf` | `1c67f068fea8` | 16,648 | KaTeX3P |
| 57 | `cache/cache/pdfbuild/fonts/KaTeX_Script-Regular.woff` | `d96cdf2b3bdd` | 10,588 | KaTeX3P |
| 58 | `cache/cache/pdfbuild/fonts/KaTeX_Script-Regular.woff2` | `036d4e95149b` | 9,644 | KaTeX3P |
| 59 | `cache/cache/pdfbuild/fonts/KaTeX_Size1-Regular.ttf` | `95b6d2f1a501` | 12,228 | KaTeX3P |
| 60 | `cache/cache/pdfbuild/fonts/KaTeX_Size1-Regular.woff` | `c943cc986384` | 6,496 | KaTeX3P |
| 61 | `cache/cache/pdfbuild/fonts/KaTeX_Size1-Regular.woff2` | `6b47c40166b6` | 5,468 | KaTeX3P |
| 62 | `cache/cache/pdfbuild/fonts/KaTeX_Size2-Regular.ttf` | `a6b2099fb555` | 11,508 | KaTeX3P |
| 63 | `cache/cache/pdfbuild/fonts/KaTeX_Size2-Regular.woff` | `2014c523c321` | 6,188 | KaTeX3P |
| 64 | `cache/cache/pdfbuild/fonts/KaTeX_Size2-Regular.woff2` | `d04c54219f9e` | 5,208 | KaTeX3P |
| 65 | `cache/cache/pdfbuild/fonts/KaTeX_Size3-Regular.ttf` | `500e04d54f0d` | 7,588 | KaTeX3P |
| 66 | `cache/cache/pdfbuild/fonts/KaTeX_Size3-Regular.woff` | `6ab6b62e9b62` | 4,420 | KaTeX3P |
| 67 | `cache/cache/pdfbuild/fonts/KaTeX_Size3-Regular.woff2` | `73d591271b16` | 3,624 | KaTeX3P |
| 68 | `cache/cache/pdfbuild/fonts/KaTeX_Size4-Regular.ttf` | `c647367d1dd4` | 10,364 | KaTeX3P |
| 69 | `cache/cache/pdfbuild/fonts/KaTeX_Size4-Regular.woff` | `99f9c6750b48` | 5,980 | KaTeX3P |
| 70 | `cache/cache/pdfbuild/fonts/KaTeX_Size4-Regular.woff2` | `a4af7d414440` | 4,928 | KaTeX3P |
| 71 | `cache/cache/pdfbuild/fonts/KaTeX_Typewriter-Regular.ttf` | `f01f3e87d9c6` | 27,556 | KaTeX3P |
| 72 | `cache/cache/pdfbuild/fonts/KaTeX_Typewriter-Regular.woff` | `e14fed02b1ab` | 16,028 | KaTeX3P |
| 73 | `cache/cache/pdfbuild/fonts/KaTeX_Typewriter-Regular.woff2` | `71d517d67827` | 13,568 | KaTeX3P |
| 74 | `cache/cache/pdfbuild/katex.min.css` | `0289a02cf451` | 23,827 | KaTeX3P |
| 75 | `cache/cache/pdfbuild/katex.min.js` | `a29d2961d314` | 272,537 | KaTeX3P |
| 76 | `logs/logs/_add_labels.log` | `e3b0c44298fc` | 0 | 空日志 |
| 77 | `logs/logs/_add_license.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 78 | `logs/logs/_check_2026.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 79 | `logs/logs/_check_abs.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 80 | `logs/logs/_chrome_cn.log` | `e3b0c44298fc` | 0 | 空日志 |
| 81 | `logs/logs/_chrome_en.log` | `e3b0c44298fc` | 0 | 空日志 |
| 82 | `logs/logs/_clean.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 83 | `logs/logs/_compr_qa.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 84 | `logs/logs/_compr_qa2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 85 | `logs/logs/_deep.log` | `e3b0c44298fc` | 0 | 空日志 |
| 86 | `logs/logs/_deep.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 87 | `logs/logs/_deep2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 88 | `logs/logs/_download.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 89 | `logs/logs/_final.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 90 | `logs/logs/_final2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 91 | `logs/logs/_final3.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 92 | `logs/logs/_final5.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 93 | `logs/logs/_final_render.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 94 | `logs/logs/_finalize.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 95 | `logs/logs/_find_cut.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 96 | `logs/logs/_find_miktex.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 97 | `logs/logs/_find_overflow.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 98 | `logs/logs/_find_overflow2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 99 | `logs/logs/_find_overfull.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 100 | `logs/logs/_find_pdflatex.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 101 | `logs/logs/_find_phrases.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 102 | `logs/logs/_find_secs.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 103 | `logs/logs/_find_strings.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 104 | `logs/logs/_find_wm.log` | `e3b0c44298fc` | 0 | 空日志 |
| 105 | `logs/logs/_find_wm.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 106 | `logs/logs/_fix_all.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 107 | `logs/logs/_fix_cn.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 108 | `logs/logs/_fix_cn2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 109 | `logs/logs/_fix_cn3.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 110 | `logs/logs/_fix_cn4.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 111 | `logs/logs/_fix_cn5.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 112 | `logs/logs/_fix_cn6.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 113 | `logs/logs/_fix_cn_fn.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 114 | `logs/logs/_fix_cn_v2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 115 | `logs/logs/_fix_en.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 116 | `logs/logs/_fix_layout.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 117 | `logs/logs/_fix_layout2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 118 | `logs/logs/_fix_overflow2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 119 | `logs/logs/_fix_overflow3.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 120 | `logs/logs/_fix_texttt.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 121 | `logs/logs/_fix_texttt2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 122 | `logs/logs/_fix_v3.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 123 | `logs/logs/_footnote.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 124 | `logs/logs/_list_overfull.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 125 | `logs/logs/_md2tex.log` | `e3b0c44298fc` | 0 | 空日志 |
| 126 | `logs/logs/_md2tex2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 127 | `logs/logs/_md2tex3.log` | `e3b0c44298fc` | 0 | 空日志 |
| 128 | `logs/logs/_miktex_help.log` | `e3b0c44298fc` | 0 | 空日志 |
| 129 | `logs/logs/_miktex_help.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 130 | `logs/logs/_miktex_install.log` | `e3b0c44298fc` | 0 | 空日志 |
| 131 | `logs/logs/_miktex_p3.log` | `e3b0c44298fc` | 0 | 空日志 |
| 132 | `logs/logs/_miktex_p3.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 133 | `logs/logs/_miktex_portable.log` | `e3b0c44298fc` | 0 | 空日志 |
| 134 | `logs/logs/_miktex_portable.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 135 | `logs/logs/_minor.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 136 | `logs/logs/_nsis_d.log` | `e3b0c44298fc` | 0 | 空日志 |
| 137 | `logs/logs/_nsis_d.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 138 | `logs/logs/_nsis_help.log` | `e3b0c44298fc` | 0 | 空日志 |
| 139 | `logs/logs/_nsis_help.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 140 | `logs/logs/_pages.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 141 | `logs/logs/_probe.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 142 | `logs/logs/_render2026.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 143 | `logs/logs/_repack_v2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 144 | `logs/logs/_retest.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 145 | `logs/logs/_rewrite2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 146 | `logs/logs/_scan2.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 147 | `logs/logs/_scan_layout.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 148 | `logs/logs/_show_after.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 149 | `logs/logs/_split.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 150 | `logs/logs/_tinytex_dl.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 151 | `logs/logs/_tl_dl.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 152 | `logs/logs/_trace.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 153 | `logs/logs/_trim.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 154 | `logs/logs/_try_miktex.log` | `e3b0c44298fc` | 0 | 空日志 |
| 155 | `logs/logs/_try_miktex.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 156 | `logs/logs/_try_tl_perl.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 157 | `logs/logs/_verify_tex.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 158 | `logs/logs/_w32tex.log` | `e3b0c44298fc` | 0 | 空日志 |
| 159 | `logs/logs/_w32tex.log.err` | `e3b0c44298fc` | 0 | 空日志 |
| 160 | `tmp/.pytest_cache/.gitignore` | `3ed731b65d06` | 37 | pytest缓存 |
| 161 | `tmp/.pytest_cache/CACHEDIR.TAG` | `37dc88ef9a0a` | 191 | pytest缓存 |
| 162 | `tmp/.pytest_cache/README.md` | `73fd6fccdd80` | 302 | pytest缓存 |
| 163 | `tmp/.pytest_cache/v/cache/nodeids` | `8515eeef6a89` | 366 | pytest缓存 |
| | **合计** | | **5,758,232** | 5.49 MiB |

> **SHA-12 全部为删除前 `hashlib.sha256(data).hexdigest()[:12]` 盘上实测**，且与上棒登记表所载 sha12 **逐件一致（163/163 吻合）**，
> 身份复验 0 偏差后再进删除集。

## 4. 论文产物冻结登记（rendered_arxiv · 47 件）

**定性：论文产物 · 永不入清理面。** 本棒 **0 清 0 触动**，逐件 `os.path.exists()` 复核 **47/47 在盘**。

| # | 路径 | SHA-12 | 字节 |
|---:|---|---|---:|
| 1 | `cache/cache/rendered_arxiv/OLD_chrome_render_cn_2026-09-08_11-34.pdf` | `f5f3052f37de` | 1,391,617 |
| 2 | `cache/cache/rendered_arxiv/OLD_chrome_render_en_2026-09-08_11-34.pdf` | `3c0c0f91e11a` | 340,324 |
| 3 | `cache/cache/rendered_arxiv/_add_emerg.py` | `b0f087035889` | 969 |
| 4 | `cache/cache/rendered_arxiv/_add_license_block.py` | `d323999284b6` | 1,272 |
| 5 | `cache/cache/rendered_arxiv/_add_sloppy.py` | `c07c731713a0` | 768 |
| 6 | `cache/cache/rendered_arxiv/_atomic_repack.py` | `6f5ec18a3ba3` | 3,401 |
| 7 | `cache/cache/rendered_arxiv/_audit_footnote.py` | `e1c0e69678b6` | 1,059 |
| 8 | `cache/cache/rendered_arxiv/_audit_items.py` | `2d0d4b6813e3` | 1,465 |
| 9 | `cache/cache/rendered_arxiv/_audit_lic_da.py` | `80dd56f59c21` | 1,042 |
| 10 | `cache/cache/rendered_arxiv/_audit_q1.py` | `42c25bebcb0a` | 1,265 |
| 11 | `cache/cache/rendered_arxiv/_check_2026_clarify.py` | `5e2d8feae061` | 2,325 |
| 12 | `cache/cache/rendered_arxiv/_check_2026_v2.py` | `2e8acb06e88e` | 3,194 |
| 13 | `cache/cache/rendered_arxiv/_check_fixes.py` | `dda84cc53beb` | 525 |
| 14 | `cache/cache/rendered_arxiv/_check_fn.py` | `aebb6f08d406` | 915 |
| 15 | `cache/cache/rendered_arxiv/_check_lt.py` | `9568cd00dbe9` | 358 |
| 16 | `cache/cache/rendered_arxiv/_check_tar.py` | `442c6db900fb` | 1,390 |
| 17 | `cache/cache/rendered_arxiv/_clean_repack.py` | `ae57e185bb24` | 16,441 |
| 18 | `cache/cache/rendered_arxiv/_compile_one.py` | `79ecf09c5505` | 1,595 |
| 19 | `cache/cache/rendered_arxiv/_count_break.py` | `b03d96306be5` | 489 |
| 20 | `cache/cache/rendered_arxiv/_dedup.py` | `450500663fc0` | 3,585 |
| 21 | `cache/cache/rendered_arxiv/_find_log_err.py` | `14f5cee1b8b6` | 801 |
| 22 | `cache/cache/rendered_arxiv/_fix_break_spacing.py` | `dffec17a0a8d` | 962 |
| 23 | `cache/cache/rendered_arxiv/_fix_break_spacing2.py` | `86753aa44091` | 859 |
| 24 | `cache/cache/rendered_arxiv/_fix_lt_break.py` | `148d26e774cd` | 2,012 |
| 25 | `cache/cache/rendered_arxiv/_fix_lt_cjk.py` | `579cd6402d2a` | 3,363 |
| 26 | `cache/cache/rendered_arxiv/_fix_lt_more_break.py` | `02242475f766` | 2,311 |
| 27 | `cache/cache/rendered_arxiv/_full_audit.py` | `93f28a1fb93d` | 5,742 |
| 28 | `cache/cache/rendered_arxiv/_list_ovf.py` | `fcde9fc1641d` | 567 |
| 29 | `cache/cache/rendered_arxiv/_list_sections.py` | `fba51491842f` | 429 |
| 30 | `cache/cache/rendered_arxiv/_move_aa.py` | `64ba44f2413c` | 2,496 |
| 31 | `cache/cache/rendered_arxiv/_move_ai.py` | `01c2f6f21ca0` | 3,966 |
| 32 | `cache/cache/rendered_arxiv/_move_da.py` | `1d41dd767959` | 4,019 |
| 33 | `cache/cache/rendered_arxiv/_rename.py` | `598d896eb659` | 826 |
| 34 | `cache/cache/rendered_arxiv/_repack.py` | `433326a5ca72` | 1,069 |
| 35 | `cache/cache/rendered_arxiv/_repack_clean.py` | `9353ffc3968a` | 1,838 |
| 36 | `cache/cache/rendered_arxiv/_restore_from_tar.py` | `bf7ede0a54f3` | 1,182 |
| 37 | `cache/cache/rendered_arxiv/_restore_full.py` | `e244ef24a176` | 5,766 |
| 38 | `cache/cache/rendered_arxiv/_restore_policy.py` | `0ddaec9dbc09` | 4,311 |
| 39 | `cache/cache/rendered_arxiv/_retry.py` | `1e785b2dc7fd` | 294 |
| 40 | `cache/cache/rendered_arxiv/_search_kimi.py` | `68fc3b1a8f53` | 1,245 |
| 41 | `cache/cache/rendered_arxiv/_verify_da_move.py` | `caaa78faa102` | 1,180 |
| 42 | `cache/cache/rendered_arxiv/_widen_lt_left.py` | `cfaed900eb14` | 596 |
| 43 | `cache/cache/rendered_arxiv/deposon_paper_cn.pdf` | `78567cf36c9c` | 2,600,098 |
| 44 | `cache/cache/rendered_arxiv/deposon_paper_cn_latex.pdf` | `c301c08f4a4f` | 2,594,145 |
| 45 | `cache/cache/rendered_arxiv/deposon_paper_en.pdf` | `2f0180e4230f` | 1,885,070 |
| 46 | `cache/cache/rendered_arxiv/deposon_paper_en_latex.pdf` | `bd7a83ea4fa1` | 1,880,367 |
| 47 | `cache/cache/rendered_arxiv/test_copy.tar.gz` | `b93889476b89` | 1,639,502 |
| | **合计** | | **12,419,015**（11.84 MiB） |

> **件数出入如实交代**：上棒 §3.2 记 46 件，本棒盘上实测与 v2 manifest 均为 **47 件**。
> 冻结清单按**盘上实测 47 件**全量登记（冻结面按超集登记更安全），差额 1 件为上棒计数出入，非本棒新增。

## 5. 删除通道实况

| 项 | 实况 |
|---|---|
| 通道 | 本地 runtime **可恢复删除通道**，`cd D:/私人资料/_non_upload_local_archive` 后顶层 `rm -- <相对路径…>` |
| 运行时回执 | `mavis-trash: moved to trash: '<path>'` **逐件 163 条** |
| 永久删除 / 绕过 | **0 / 0**（未用绝对路径删除命令、未用内联脚本删除、未直呼回收站） |
| 批次数 | **9 次顶层 `rm`**（20/20/20/17/20/15/15/11/15）；第 6 次命中 290 s 执行器上限被截断，**非删除失败**，余件按盘上实测续列 |
| 首次尝试 | 1 次以 `rm -- (Get-Content …)` 传参，拦截器按字面解析失败（回执 `No such file or directory`），**0 件被删**，改为字面相对路径重发 |
| 删除后复核 | 163 件逐一实测 **0 件在盘**（`still_on_disk = 0`） |
| 并行 | **0 并行**：回收站并发移动存在竞态风险，可能破坏「0 永久删除」铁律，故全程串行 |
| 回收站可恢复性 | 是（163 件原件在回收站内可取回） |

## 6. manifest v3 与 v2→v3 对账表

v3 落盘：`_archive_manifest_non_upload_v3_2026_09_28.json` · 204,256 B · SHA-12 `a2e4c5a9b713` · 逐件哈希全量重算（1,473 件）。

| 项 | v2 | v3 | 差 |
|---|---:|---:|---:|
| 件数 | 1,630 | 1,473 | -157 |
| 字节 | 337,169,408 | 331,522,763 | -5,646,645 |
| removed | | | **163** |
| added | | | **6** |
| changed | | | **0** |

| 对账项 | 实测 | 结论 |
|---|---:|---|
| v2→v3 removed | 163 | **= 本棒清走 163 件**，残差 **0** |
| removed 字节 | 5,758,232 | **= 本棒清走字节 5,758,232**，逐件吻合 |
| changed | 0 | **0 件**被改动，0 静默修改 |
| added | 6 | **非本棒所清**，为执行期间并发再生（见 §7） |
| v2 历史快照 | `84eef669234b` | **0 触动**（收尾复测同值） |

## 7. 执行期并发变动观察（如实登记，非本棒所为）

v2 生成于 19:02，本棒执行期间（19:20–20:05）盘上出现 **6 件 v2 未收录的 `.pyc`**：

| 路径 | 字节 | mtime |
|---|---:|---|
| `scripts/scripts/kt_b1/__pycache__/boss_b1_sinkhorn_ot.cpython-314.pyc` | 20,607 | — |
| `scripts/scripts/kt_b1/__pycache__/boss_b1_sinkhorn_ot.py.cpython-314.pyc` | 18,526 | — |
| `scripts/scripts/kt_b1/__pycache__/boss_b2_kd.cpython-314.pyc` | 19,562 | — |
| `scripts/scripts/kt_b1/__pycache__/boss_b2_kd.py.cpython-314.pyc` | 17,470 | — |
| `scripts/scripts/kt_b1/__pycache__/boss_b3_llmlingua.cpython-314.pyc` | 18,743 | — |
| `scripts/scripts/kt_b1/__pycache__/boss_b3_llmlingua.py.cpython-314.pyc` | 16,679 | — |

其中 3 件（`boss_b1_sinkhorn_ot/boss_b2_kd/boss_b3_llmlingua.cpython-314.pyc`）为**上棒已清的同名 `.pyc` 被重新编译再生**，
但 **SHA-12 与上棒登记值不同**（`3738cacf6dc2`→`8f5d7b425d55` 等），属新编译产物；另 3 件为新增 `*.py.cpython-314.pyc`。
本棒**未运行**任何 `kt_b1` 模块，**未清、未触、未改**这 6 件（不在派工授权面内）⇒ 按「拿不准 ⇒ 留」登记。

## 8. 引用同步核（清单/委托材料）

对 `deposon-repo/` 全仓 **1,269** 件 `md/txt/json/bib/tex/py/ps1/csv` 做全路径字符串检索：

| 项 | 结论 |
|---|---|
| `deposon-repo/letters/` 委托材料 | **0 处**引用本棒 163 件 ⇒ 委托材料所引路径 **0 失效**，**0 变更** |
| 引用本棒 163 件的件 | 仅 **5** 件：v3/v2/0923 三份 manifest、上棒清理登记件、**09-24 三目录盘点表** |
| 09-24 盘点表 | 163 处＝**清单式**（PI 2026-09-28 判「逐件列名但无实质引用」→ 放行） |
| 09-23 幽灵引用对账件 | 12 处（10 图 + 2 `fig1_architecture`），内容**均有同值副本留存**（图：`.trae/build`/`.trae/snapshots`/`.trae/source` 各有同值件；架构图：`paper/fig1_architecture*.png`）⇒ 无信息损失；其 sha12 判定键仍完整保存在 v2 历史快照中 |
| 需同步修订的清单/委托材料 | **0 件** ⇒ 登记「**0 变更**」 |

## 9. 铁律遵守表

| 铁律 | 遵守情况 |
|---|---|
| 可恢复删除，0 永久删除 0 绕过 | ✅ 9 次顶层 `rm -- <相对路径>`，回执 ×163；无绝对路径/内联脚本/直呼回收站 |
| `rendered_arxiv` 冻结 0 触动 | ✅ 47 件逐件复核全在盘，0 清 0 读改 |
| 上棒登记件 / manifest v2 **0 触动** | ✅ 收尾复测 `34f2c63306b8` / `84eef669234b` / `f56e6fbf04ef` 三件哈希与开棒首测同值 |
| `deposon-repo` 其余既有件 0 触动 | ✅ 仅**新增** v3 manifest ＋ 本登记件 2 件 |
| SHA-12 口径 | ✅ `hashlib.sha256().hexdigest()[:12]` 小写，全量实测 |
| 拿不准 ⇒ 留 | ✅ 证据引用 7 件、论文正文唯一副本 2 件、并发再生 6 件、执行期新增面 均**留＋登记** |
| 不编造 | ✅ 件数/字节/哈希全盘上实测；预估 8.5 MiB 与实测 5.49 MiB 差额已在 §1 归因 |
| 署名如实 | ✅ 出证 = worker；未冒名 doc-writer / verdict-keeper / Trae code 等 |
| key 永不明文 | ✅ 本棒 0 次 API 调用、0 处 key 相关字段 |

## 10. 老实交代与待拍板项

**未完成/受阻**：0。三类清走、冻结登记、v3 manifest、对账表均已落盘并经盘上复核。

**如实交代 3 项**：

1. 预估 ~8.5 MiB vs 实测 **5.49 MiB**：主因 ①三类重叠（KaTeX/空日志 ⊂ 173）；②减量 9 件；③1 件（`test_copy.tar.gz`，1.56 MiB）属冻结面。**未为凑回收量放宽判据**。
2. 冻结面件数 **47 ≠ 上棒 46**：按盘上实测 47 全量登记（上棒计数出入）。
3. 执行期并发再生 6 件 `.pyc`：非本棒所为，已登记未处置。

**新增待拍板项（3）**：

1. **减量留置的 9 件**是否一并放行清走（7 件证据/台账引用 `.pyc` ＋ 2 件论文正文唯一副本 `outline_v2X.md`/`related_work_v2X.md`）？
2. **并发再生的 6 件 `.pyc`** 是否清走（其中 3 件 SHA-12 已变，属新编译产物）？
3. **转移面**：上棒 §7 第 5 项「0 转移」本棒**未接到点名应转件清单**，维持「拿不准 ⇒ 留」，仍待 PI 指定。

---

出证：**worker**（deposon V4 归档区清理扩展棒 · 2026-09-28 晚 · session `mvs_ca9cc05ad50a4d8799d82339c969f5d7`）
