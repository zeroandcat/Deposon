# 戴夫_FTFB_v4重排说明（arXiv上传版）_2026-09-18

- 任务：FTFB v4 重排（arXiv 上传版）＋上传包＋元数据。基线＝新链头 `shared/鲍勃_FTFB全稿R3全额修订版_2026-09-18.md`（sha256 前缀 **cea0a8254e22**，427 行；工件边界：头部 L1–L8 blockquote 说明块、尾部双 `---` 分隔＋附录 L402–L427；正文 L9–L396 共 388 行，末条 R56）。
- 管线：`build_ftfb_tex_v4.py`（基线＝B01 卫生修复版管线，解析器/inline 规则零改动）。B01 防复发全开：tex CJK=0 与内部引用 token 零命中的**生成期断言**在位并通过；v4 未引入任何内部版本引用（上轮剥离的 "(v9 system)" 未恢复）。
- 交付目录：`shared/戴夫_FTFB_v4_arXiv上传版_2026-09-18/`（五件并列，不覆盖旧版）。

## 一、指纹链

| 工件 | SHA-256 前 16 位 | 说明 |
|---|---|---|
| 链头源稿 | cea0a8254e227c3e | 427 行（含工件） |
| 剥离后论文正文 | a94845bd82b15a20 | 388 行（L9–L396，行级断言钉死边界） |
| 交付 tex | 1e447164acc5a506 | fiction_that_feeds_back.tex |
| 交付 PDF | 555e1fe41399f5fa | 24 页 A4，388,031 B，pdfTeX-1.40.29 |
| 中性 compile_verification.txt | 9a2f2a7f85f3ed9c | 英文中性版（四零/视觉门/结构/卫生扫描/指纹） |
| arXiv 上传包 | d122b737c823f962 | ftfb_arxiv_2026_09_18.tar.gz（36,765 B，包内三件） |
| arXiv 元数据表 | 56f23ae824da640a | arxiv_metadata_2026-09-18.txt |

既有交付件零改动复核：R2 链头 7a0a98289588、v3 tex d060f75dbe9f、v3 PDF 2d9edc8c7303 均未触碰。

## 二、四零指标与门禁（全绿）

- **四零**：编译错误 0／Overfull 0／缺字形 0／未定义引用 0；三遍编译收敛（pass2.log＝pass3.log 逐字节）。
- **T-1 视觉门**：PASS——24 页；p1 窄栏签名行 23（标题块＋信息行＋摘要区，正常）；**p2 起全零**（无 abstract 越页）。
- 结构：标题全文 1 次；五锚不变式各 1 次（全在 p16）；References 56 条全列；指针 56/56 全覆盖；表头 "No." 改写在位。
- 字形页面级：τ→p15、Σ→p8、×10⁻¹⁶→p15、五锚串→p16、直引内引号渲染正常。
- 披露项：Underfull 3 行（badness 2103/5548/1990，内容层固有错配，emergencystretch 标准机制吸收，v3 同款三行）；其他警告 0。

## 三、信息行落版（沿 Keep the Books v9 惯例）

- 标题块：`\author{Qihao Yuan}`、`\date{2026-09-18}`、`pdfauthor={Qihao Yuan}`（PDF 元数据 Author＝Qihao Yuan 已验证）。
- 信息行（\maketitle 后，v9 同构样式：`\noindent\textbf{arXiv subjects}: cs.AI (primary) $\cdot$ physics.hist-ph $\cdot$ cs.CY \quad \textbf{License}: CC BY 4.0 \quad \textbf{Conflicts of interest}: none declared \quad \textbf{Date}: 2026-09-18`，上下 `\vspace{0.5em}`＋`\hrule`）。
- 渲染核验（V1 门）：五要素（subjects/License/COI/Date/Author）首页全渲染；信息行为单段自然折行（"Conflicts | of interest" 跨行），与 v9 视觉惯例一致。

## 四、与 v3 差异分布（diff 全量审阅）

v4 tex vs v3 交付 tex：**30 个 hunk（删 32 行／增 47 行）**，两类：

1. **v4 排版层（5 hunk，本轮设计）**：pdfauthor 填名；双盲版注释改 arXiv 版注释；`\author{}`/`\date{}` 填入；新增信息行 5 行（vspace/noindent/hrule）。
2. **R3 内容层（25 hunk，全部对应鲍勃《R3 逐项修订说明》申报项）**：C-1 摘要降格重写（含 §7.4 保密渠道句）；F-C1–F4 阈值操作化；§1.3 范围声明扩展（fifty-six 池口径＋[R56] 匿名声明＋三线检索协议披露）；§2.1 Helmholtz 四段直引＋formal fiction 定义重写；熵公式 "same functional form up to…" 措辞；isomorphism→structural parallel 全局降格（多处单行 hunk）；M4 行 "Provisional pass (author-attested freeze; pre-registered …)"；§9 局限与方法句同步；AI 披露句扩展（"used for drafting and …"）；池计数 54→56；References 新增 R55/R56 池组块（含 `[AUTHOR-ANONYMIZED ENTRY]` 标记）。

**无未申报差异**；正文逐字一致性由管线断言组背书（cite 多重集 152/F-C 12/refs 56/五锚/标题单现）＋diff 全量审阅确认。

## 五、arXiv 版合规扫描（变体口径）

- 工作流 token（deposon/keep-the-books/zhipu/智谱/清言/〔用户U〕/〔用户U〕/orcid/github.com/邮箱域/acknowledg/funded by/grant no）：tex 与 PDF **零命中**（本地路径/shared/ 亦零命中）。
- **作者名自洽**：'Qihao Yuan' 全文恰 2 次（\author＋pdfauthor），**正文 0 次**——R56 匿名条目（companion study，题名/作者/标识符隐去）与署名不冲突，camera-ready 恢复路径由 §1.3/References 卷首声明交代。
- tex 源层 CJK＝0（含注释，B01 断言在位）；PDF 文本层 CJK＝0；无批注/附件（Annots 无）。
- 元数据表/README/中性 CV/包内 tex 四件卫生扫描 CLEAN（唯一 "b01" 命中系冻结锚哈希串 "tb01338" 子串，论文内容非工作流引用）。

## 六、arXiv 上传包与自包含复现

- 包 `ftfb_arxiv_2026_09_18.tar.gz`（d122b737c823f962，36,765 B）内三件：`fiction_that_feeds_back.tex`（与交付 tex 同 sha）＋`README.md`（中性英文，构建说明＋提交注意事项）＋`compile_verification.txt`（中性版）。
- pdflatex 兼容：无 fontspec/系统字体依赖（沿 v8 教训，全标准宏包）。
- **包内自包含复现验证**：解包至干净临时目录，TL2026 三遍编译——0 错误/0 Overfull、24 页、**PDF 文本层与交付 PDF 逐字节一致**。

## 七、⚠ 摘要超长警示（需内容侧裁决，零推断挂起）

- 元数据摘要与正文摘要**逐字一致**（源级校验：md 摘要段落在 tex abstract 环境内逐字在位）。
- 但摘要 **2216 字符 > arXiv 元数据 1920 上限（超 296 字符）**——arXiv 提交表单将拒绝该字段。内容削减属内容层修订权（鲍勃/查理线），本轮未动；元数据表中已按原文交付并附警示。PDF 排版版摘要不受限。
- 字符合规：纯 Unicode 文本，非 ASCII 仅 U+00A7/U+2013/U+2014，无 TeX 标记，UTF-8 安全。

## 八、边界与交接

- 本轮为排版/打包轮：内容层未动一字；正式内容修订（摘要削减等）到位后如需 v5 重排，管线切链头即可。
- 用户新提及的 Deep Academic Survey (DAS) 自动综述生成系统：属文献调研/内容生成线工具选型，与本轮排版无关，建议管理员派发阿兰/查理线评估（如用于下一轮查新或综述辅助）。
- B01 管线卫生断言已固化为生成期门禁，后续轮次自动防复发。

—— 戴夫-格式专家｜2026-09-18 00:4x CST
