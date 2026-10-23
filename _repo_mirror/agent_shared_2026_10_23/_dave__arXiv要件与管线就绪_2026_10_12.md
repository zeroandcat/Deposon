# 戴夫·arXiv 提交要件与管线就绪报告（2026-10-12）

**任务**：arXiv 提交要件清单＋md→LaTeX→PDF 工具链就绪检查＋查重与格式自检方案（轻量准备面，不跑全稿）。
**纪律确认**：0 按期刊模板、0 声称投稿目标、未改动任何他人原件；烟测为小样级。本报告内容版本无关——论文从头重写后直接适用。
**附带**：应用户指令从 GitHub 获取的论文可读性技能已安装（§4 附录）。

---

## 1. arXiv 提交要件清单（对照第一作先例）

先例来源：`repos/Deposon/paper/`（正文 md/bib）＋第一作 arXiv 源码包（deposon_arxiv_2026_en，2026-09-08 四轮修复版 README）。

| # | 要件 | 第一作先例 | 双主线新稿建议 | 状态 |
|---|---|---|---|---|
| 1 | 题名 | 英文描述性长题名（Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths） | 待查理重写后定；沿用「机制＋保证＋对象」命名式即可 | ⏳ 待新稿 |
| 2 | 作者 | 单作者 Qihao Yuan，School of Chemistry and Life Resources, 〔高校R〕 University of China；首页头部行带仓库链接 github.com/zeroandcat/Deposon | **占位沿用第一作作者块**；线索册「待补面：作者字面」仍开口，PI 终确认（含是否加致谢/合作者） | ⏳ PI 确认 |
| 3 | 摘要 | FTFB 先例 1,846 字符；第三作终稿 1,879 字符 | arXiv 硬限 **1,920 字符**（纯摘要体；Keywords 行并入则计入）。写作时逐字计数，第三作有先例口径（Keywords 行单独交 PI 裁决） | ⏳ 待新稿＋计数 |
| 4 | 主分类 | **cs.AI**（README 明记） | cs.AI（管理员派单指定） | ✅ 定 |
| 5 | 次分类 | 第一作**未挂**次分类（cs.AI 单分类） | 双主线内容（V3 博弈论×V4 蒸馏）候选：cs.GT / cs.LG / cs.CL；**建议新稿成形后按实际重心选 0–2 个，PI 定**。不预设 | ⏳ PI 定 |
| 6 | License | 提交表单选 **CC BY 4.0**（第一作建议同）；**正文内不断言任何许可** | 沿第一作：CC BY 4.0，表单选择、正文不写 | ✅ 定 |
| 7 | Comments 字段 | FTFB 先例格式：「24 pages; ［版本/附录说明一行］」 | 「N pages; 全量补实验版说明」，页数以终稿为准 | ⏳ 待新稿 |
| 8 | AI 使用声明 | arXiv 2026 政策三要素：AI 工具与版本、协助范围、作者全责。第一作有完整成段措辞（KIMI 声明先例） | 结论后独立 `\section*`（第一作 R4 体例），措辞套先例三要素，工具名/版本按实际 | ⏳ 待新稿 |
| 9 | Data/Artifact availability | 结论后独立 `\section*` 两个（Data availability / Artifact availability），R4 从脚注升级的定稿体例 | 沿 R4 体例；冻结记录/摘要可得性表述按新稿实际 | ⏳ 待新稿 |
| 10 | 参考文献 | **inline `thebibliography`（0 bibtex 依赖）**，单 tex 自含；[1]–[62] 全引核验先例；references.bib 37 条在库 | 沿 inline 方案（arXiv 单文件最稳）；新稿引用池由阿兰文献线供 | ⏳ 待新稿 |
| 11 | Funding/COI | 无资助声明（none declared），COI 无 | 沿用，提交前如有变化再补 | ✅ 定 |
| 12 | 引用编号 | 正文 [n] 与文末列表一一对应，逐项核验 | 新稿定稿后跑引用完整性检查（见 §3.2-8） | ⏳ 待新稿 |

**小结**：可现在锁定的＝主分类 cs.AI、License CC BY 4.0、inline 参考文献、AI 声明/availability 的 R4 体例；其余要件均依赖新稿成形，无需提前施工。

---

## 2. md→LaTeX→PDF 工具链就绪

### 2.1 双引擎链（均已烟测通过 ✅）

| 链 | 引擎与体例 | 烟测结果 |
|---|---|---|
| **A（第一作体例）** | tectonic 0.15.0（XeLaTeX）＋ fontspec ＋ DejaVu Serif（AutoFakeSlant=0.25 补无斜体）＋ IfFontExistsTF 回退 | `smoke_xelatex.pdf`：1 页 0 error；DejaVu CID TrueType 全嵌入；★/≫ 等 Unicode 字形渲染正常 |
| **B（第三作体例）** | TeX Live 2026 本地树 pdflatex ＋ T1/lmodern ＋ CJKutf8 预备 ＋ newunicodechar | `smoke_pdflatex.pdf`：1 页 0 error 0 missing char；13/13 字体全嵌入；amsmath/booktabs/交叉引用/bibtex 全链解析 |

小样源文件：`agents/…/arxiv_prep_20261012/smoke/`（smoke_pdflatex.tex + smoke.bib、smoke_xelatex.tex）。
两份烟测 PDF 副本：`shared/戴夫_arXiv烟测小样_2026_10_12/`。

**附加证据（归档件，不作为交付）**：本轮早前对 v0.2 全稿的干跑（build_dryrun.py 转换＋pdflatex 编译）30 页 0 error 成功——工具链对真实稿件规模已被验证；该 v0.2 稿已随重写决定归档，仅留档 `agents/…/arxiv_prep_20261012/work/`。

### 2.2 字体可用性

- DejaVu Serif/Sans：系统在位（fc-list 确认），链 A 直接可用；
- Latin Modern（pdflatex 默认西文）：TeX Live 树内；
- fandol（CJK 回退）：tectonic 按需下载可用（第一作 R3 已在纯净环境验证 fandol-first 回退链；新稿如为 EN 单语包则用不到）。

### 2.3 转换与构建脚本

- `build_dryrun.py`（md→tex 转换内核：表格/代码/列表/数学/加粗）：**可复用**，新稿重写后按新结构适配入口即可，本轮未改动；
- 已知环境坑（登记防复发）：shell 会话间 cwd 会重置，脚本内路径须写绝对路径；tectonic 首次编译需联网拉包（msam10.pfb 等），离线场景用链 B。

---

## 3. 查重与格式自检方案

### 3.1 查重（自重叠链，项目既有成熟口径）

- **工具**：overlap8 链（`agents/…/third_paper_v05_final/scripts/overlap8_final_v05.py`；口径＝norm_words / strip_tex / 首现贪心扩展 / 覆盖率分母＝查询件，参照件 SHA 锁定，与 v0.3/v0.4 轮同链可比）。
- **新稿流程**：① 查理新稿 md 定稿 → ② 改查询件路径＋刷新三处 SHA 锁（新稿 md、第一作 tex、第二作 FTFB tex）→ ③ 8-gram 自重叠对第一作＋第二作 → ④ 案例节加测 10-gram（先例同型）→ ⑤ References 块分区归属、出剔题录值。
- **阈值沿用**：以第三作轮先例值为参照系（vs 一作/二作百分位量级），不另设新线。
- **外部查重**：本环境无 iThenticate/Turnitin 商用权限，不虚构报告。可行替代：(a) 抽样特征短语 web 检索核未发表撞句（可与阿兰文献线配合）；(b) 引用完整性检查——引而不标才是抄袭主险，新稿按 claim-to-evidence 纪律写（§4 技能已内置该纪律）。

### 3.2 格式自检清单（可复用；源出第三作 v0.5 终收尾轮＋第一作四轮修复先例）

1. `pdffonts` 全部 emb=yes（逐行）；
2. 页面尺寸一致性登记（US letter / A4 按实际编译体例**如实登记**，第一作 US letter、第三作 A4 均有先例）；
3. 摘要 ≤1,920 字符（含 Keywords 行是否计入的 PI 裁决登记）；
4. 单 tex 自含（inline thebibliography 或 bbl 并入，0 外部依赖）；
5. hyperref metadata：pdftitle/pdfsubject 填写；pdfauthor 按 PI 指示（实名沿第一作 / 占位待终稿）；
6. 文本层与书签零身份词泄露（pdftotext 后 rg 扫中文名＋候选身份词；第三方作者名子串假阳性须查上下文，先例教训已登记）；
7. Overfull=0（先例技法：`\tolerance=9999`＋`\emergencystretch=3em`；Underfull 以基线对齐登记不强清）；
8. 图/表/式编号按首现顺序，交叉引用 0 undefined；
9. 冻结锚点（实验数字）在 PDF 逐项复核（项目特有，鲍勃冻结 JSON 为准）；
10. 编译三遍收敛（pass2==pass3 才收）。

---

## 4. 附录：论文可读性技能安装（用户指令「从 GitHub 获取相关技能，论文还局限于罗列成果而非真正可读」）

已从 GitHub 获取并安装 4 个技能至 `/home/z/my-project/skills/`（来源、许可证与依赖注意详见 `skills/_SOURCES_paper_skills_2026_10_12.md`）：

| 技能 | 来源 | 对症点 |
|---|---|---|
| **manuscript-builder** | juanmontiz/peper-skills-suite | **论证主线先行**：写前先立「一句话主张→缺口→贡献类型→主图职责」的 paper spec，逐节起草并强制每条定量断言挂证据（图/式/引文/脚本）——直接治「罗列成果」 |
| **paper-sections** | s-choung/Research-Skills（MIT） | IMRAD 各节叙事手册：引言四段式、Results 每段一个发现＋机理收尾、引用密度分节控制 |
| **paper-style** | s-choung/Research-Skills（MIT） | 文体档案＋AI 腔轻清理（禁用词表/破折号限频/三项并列削减） |
| **humanizer_eng** | s-choung/Research-Skills（MIT） | 英文去机翻感三律：不虚构、去机械信号、恢复具体性 |

**依赖注意**：paper-sections 依赖 STYLE_PROFILE.md 文体档案（原作者个人档案，本地无）——建议下一步从第一作 `deposon_paper_final_en.md` 提炼团队版 profile，或先只用其 playbook 结构。journal-selector 等 peper 其余技能**刻意未装**（与「0 声称投稿目标」纪律冲突）。
**对查理的可用性**：技能已入共享技能目录，重写轮可直接调用；与本报告 §1 要件、§3 自检清单配合使用。

---

## 5. 交付物清单

- 本报告：`shared/戴夫_arXiv要件与管线就绪_2026_10_12.md`
- 烟测小样 ×2：`shared/戴夫_arXiv烟测小样_2026_10_12/`（smoke_pdflatex.pdf / smoke_xelatex.pdf）
- 可读性技能 ×4＋来源说明：`skills/{manuscript-builder,paper-sections,paper-style,humanizer_eng}`＋`skills/_SOURCES_paper_skills_2026_10_12.md`
