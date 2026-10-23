# 戴夫：minimax 双审结论本地确定性复核备忘

**复核人**：戴夫-格式专家（独立于 minimax 双审 worker）
**日期**：2026-09-17（深夜派单，单轮闭合）
**复核对象**：
- Pass 1：`ftfb_pass1_background_methodology_audit_2026_09_17.md`（挂载只读，实测 8257 B，SHA-12 = `70bd41d9722d`）
- Pass 2：`_ftfb_pass2_results_limitations_audit_2026_09_17.md`（挂载只读，实测 11390 B，SHA-12 = `cfab992cf939`）
- 被审交付件：`shared/戴夫_FTFB_v3正式版交付_2026-09-17/`（tex `d060f75dbe9f` / PDF `2d9edc8c7303`，23 页 356,123 B）＋ 源稿 `shared/鲍勃_FTFB全稿R2修订版_2026-09-17.md`（全文 `7a0a98289588` / 剥离后 `543479649b3e`）＋ `compile_verification.txt`（`62d86debeeea`）

**纪律**：挂载目录全程只读；交付件零改动（复核工作区为私有目录副本）；全部断言本端独立复算，不采信 minimax 报告的任何中间结论；零推断。三态裁定 = 复核一致 / 不一致（附本端实测值）/ 属判断性结论不可本地复核。

---

## 一、基线指纹复验（任务第一项）

| 工件 | 链头/简报期望 | 本端实测 | 裁定 |
|---|---|---|---|
| ftfb_v3.pdf | 2d9edc8c7303 | 2d9edc8c7303（23 页，356,123 B） | **一致** |
| ftfb_v3.tex | d060f75dbe9f | d060f75dbe9f（511 行） | **一致** |
| compile_verification.txt | 62d86debeeea | 62d86debeeea | **一致** |
| 源稿全文（416 行） | 7a0a98289588 | 7a0a98289588 | **一致** |
| 剥离正文（L9–L391，383 行） | 543479649b3e | 543479649b3e（`sed -n '9,391p'` 复算） | **一致** |

两报告的"包内链头指纹基线"与本端复算全部吻合。PDF 双盲元数据直验：`pdfinfo` Title=论文题、Author=空、Creator="LaTeX with hyperref"、Producer=pdfTeX-1.40.29。

---

## 二、Pass 1 断言逐条复核

### 2.1 R2 四触点（Pass 1 §2.1）

| # | 断言 | 本端实测 | 裁定 |
|---|---|---|---|
| C-1 | L176 让步句 = "the mapping below inherits these four demands — the distillation is this paper's, and the table below marks, row by row, which phrasings are the entry's record and which are this paper's formalization" | 逐字命中（L176，1 处）；旧句 "inherits exactly these four demands and nothing else" 全文 0 残留 | **一致** |
| C-2 | content/warrant-translatability 三触点 L100/L109/L267 | content-translatability 全文恰 1 次（L100）；warrant-translatability 恰 3 次（L100/L109/L267）；三处语义与 Pass 1 引述相符 | **一致** |
| C-3 | M1–M5 归属与直引＋R37 访问日期 | M1 行 "this paper's formalization, prompted by the guardrails recorded in [R37]"（L186 逐字）；M2/M3/M5 均挂 "(quote as cited in [R37])"（全文该短语恰 4 处：L176/187/188/190）；R37 题录含 "accessed 2026-09-17 (entry updated 7 April 2025)"（L354 逐字） | **一致** |
| C-3' | Pass 1 所引三段直引《the unnatural explanation》《no wilfully ignore》《established or carefully extrapolated》 | 前两段**非字面存在**（实际引语为 "natural rather than supernatural or transcendental explanations for the events and phenomena it describes" 与 "wilfully ignore or break known scientific principles"，均存在各 2 次）；第三段字面存在（2 次） | **不一致（缩略引语不逐字，实际引语存在，结论不受影响）** |
| C-4 | L60 收紧句＋L62 措辞＋R53/R54＋Helmholtz 仅提及＋年份未引入 | L60 含 "at the time of their construction no physical theory made use of them"（逐字）；L62 = "found the language available"（旧 "ready" 0 残留）；R53（L382）含 emis URL + retrieved 2026-09-17，Riemann 三段直引均在；R54（L383）含 wikisource URL + "1876 works"；Helmholtz 全文仅 L60 一处提及、无引号、未入 54 池；1854/1870/1873 全文 0 次 | **一致** |

### 2.2 五锚不变式（Pass 1 §2.2）

| 断言 | 本端实测 | 裁定 |
|---|---|---|
| 五锚各恰 1 次 | md：`aeefb8ef6972/9bbe43f41fa8/6e9673205dc0/68a5b08ef007/6b09de9911c0` 各 1 次；tex 同各 1 次 | **一致** |
| 全部位于 MD L229（§7.1 P 段） | 五锚同现于 L229 单行（GT_FORMALIZATION_v1.md / run_v21_gtformal.py / run_v22_p1c.py / SPEC_GT2B.md / SPEC_GT8C.md 对应关系与 Pass 1 引述逐字一致） | **一致** |
| §7 段 L219–L246 共 28 行 | `## 7.` 起于 L219，`## 8.` 起于 L247，区间 28 行 | **一致** |
| §1–§5 零命中 | 五锚仅出现于 L229（属 §7），§1–§5（L7–L137）零命中 | **一致** |
| PDF 渲染 p15 | pdftotext 分页验证：五锚全部且仅在第 15 页 | **一致** |
| tex 侧位置（Pass 2 §2.4 交叉引用） | tex L324 恰含全部五锚 | **一致** |

### 2.3 novelty 表（Pass 1 §2.3）

| 断言 | 本端实测 | 裁定 |
|---|---|---|
| M1/M3/M4 归属 "this paper's formalization" | L186/188/189 表格行逐字确认；M5 = "this paper's distillation"（L190）确认 | **一致** |
| "M1/M3/M4 标注 this paper's formalization **outright**" | "outright" 全文仅 1 次（L196 provenance 段，且该句只指 M3："it is this paper's formalization outright"）；表格 M1/M3/M4 行内无 "outright" 字样 | **不一致（表述将 provenance 段措辞误安到表格行标注上；实体归属声明存在，结论不受影响）** |
| M2 挂 [R39] 直述、R46/R38/R47–R52 依据、[R42] §1.3+§9.2 两次区分宣告 | L187 M2 行挂 [R39]；L186/188/190 挂 R46/R38/R47–R52 如 Pass 1 所列；[R42] 在 §1.3（L40–55 内 1 处）＋§9.2（1 处）恰两次 | **一致** |
| novelty 学术判断本体（与现有文献的区分度） | — | **属判断性结论，不可本地复核** |

### 2.4 D1–D6 双盲（Pass 1 §2.4）

| 项 | 断言 | 本端实测 | 裁定 |
|---|---|---|---|
| D1 | token 清单（deposon/keep-the-books/keep the books/zhipu/智谱/清言/〔用户U〕/〔用户U〕/orcid/github/acknowledg/funded by/grant no）tex 全零 | 13 个 token 在 tex（另加验 md 与 PDF 文本层）全部 0 命中 | **一致** |
| D2 | `\author{}`/`\date{}` 均空（tex L63/L64） | L63=`\author{}`、L64=`\date{}` 直验；全文无致谢节 | **一致** |
| D3 | PDF /Author=""，Creator="LaTeX with hyperref" | pdfinfo 直验：Author=空、Creator="LaTeX with hyperref" | **一致** |
| D4 | 无批注/附件 | 与 compile_verification L70 一致；PDF 无 Annots（链上验证记录） | **一致** |
| D5 | 5 行 CJK 仅在 TeX 前导注释（F7/F8/F10），PDF 文本层 CJK=0 | CJK 行恰为 tex L42/47/56/57/58 共 5 行（均为注释，110 汉字）；PDF 文本层 CJK 字符 0、CJK 标点 0 | **一致** |
| D6 | 邮箱 0 hits；"15 个 @ 全为 TeX 宏 `\@startsection/\@plus/\@minus`" | 邮箱：严格 email 正则 tex/md/PDF 全 0 ✅；但 **@ 归因不实**：tex 共 15 个 @ = `\@`类宏 8 + `\z@` 2 + tabularx 列规格 `@{}` 4 + `hybrid_norm@0.5` 1（末者为度量字段名，**非宏**，且渲染进 PDF 文本层 p16）。PDF 文本层 @ 仅 1 处即 hybrid_norm@0.5 | **邮箱结论一致；@ 归因描述不一致（4+1 处非 TeX 宏）** |

### 2.5 铁律声明（Pass 1 §7）

- 铁律 3"54 条零重编号（唯一 Rnn 数=54）"：本端复算正文唯一指针 54、覆盖 R01–R54 无缺失无多余 → **一致**。
- 铁律 1/2/4/5（未写字节、未动锚、未触碰阈值、未调 API/〔IM〕/push）与铁律 7（0 LLM 调用）：行为性自我声明，**不可本地复核**；但"未动论文"与指纹未变（本端四件+剥离全对）相容。
- **Pass 1 自报产物指纹**："本端产物 SHA-12 = 17AF43E49D57（8192 B）" → 本端实测该报告文件 **8257 B、SHA-12 = 70bd41d9722d**，字节数与指纹均不符（报告自带"本行计入后 SHA 再变"的自引用保留条款，且 8192≠8257 表明自报值对应某个中间快照而非最终稿）→ **不一致（自报指纹不可采信）**。

---

## 三、Pass 2 断言逐条复核

### 3.1 §4/§7.1 数字实位（任务指定的全部数字）

| 断言数字 | 本端实测（md 计数 / PDF 页位） | 裁定 |
|---|---|---|
| 2.220446049250313×10⁻¹⁶（M1 守恒恒等式最大偏差） | md 1 次（L231）；PDF p15 | **一致** |
| 字段 `physics_audit.t_plus_r_plus_a_max_deviation`（`anon_benchmark_v1_4_gsm8k.json`） | md 1 次；PDF p15（`\texttt` 内断行 `physics_audit.t_ plus_r_plus_a_max_deviation`，容忍断行匹配成立）；gsm8k json md 2 次（p15/p16） | **一致** |
| 0.8569（P1a 最大偏差，O(1) gap） | md 1 次（"maximum deviation 0.8569, an O(1) gap that does not vanish with step size"）；PDF p15 | **一致** |
| −1.0（T-P1b 最小方向余弦） | md/PDF p15 两处（"minimum directional cosine −1.0"；"reaching minimum cosine −1.0"） | **一致** |
| 81 点 τ 网格（T-P1c） | p15："killed on both lines, with an 81-point grid" | **一致** |
| 0.669（P2 循环图中位残差） | md 1 次（§7.1 E 段）；PDF p15 | **一致** |
| ECR=4/3，17 个 finite-valued graphs，覆盖 20/22（3 个 ∞＋2 个缺 arm 数据） | md（§7.1 E 段）："median ECR = 4/3 over the 17 finite-valued graphs, with coverage of 20 of 22 graphs — three graphs read Infinity, two graphs lack arm data, both disclosed as-is"；PDF p15 | **一致** |
| McNemar p=0.5（GSM8K）/ p=1.0（StrategyQA） | L239 逐字："(McNemar p=0.5)…(p=1.0)"；PDF p16 | **一致** |
| 检测差阈值"约 ±10pp" | 实际措辞为 "roughly ±10 percentage points, so smaller increments are not excluded"（L239，§7.3）；"±10pp" 为 Pass 2 缩写 | **一致（缩写形式，语义实体在位）** |
| 5 个结果 JSON（gsm8k/p1c/gtformal/crossval/e95ci） | 五件文件名 md/PDF 全部在位（p15–p16） | **一致** |
| 23 页渲染、p23 为 R54 条目 | 23 页；p23 以 R54 条目收尾（含 "1876 works"） | **一致** |
| v2 缺陷版 20 页、修复补 3 页 | 本端对 v2 参照 PDF 直验：20 页 | **一致** |

### 3.2 §2.2–§2.3 Discussion/Limitations 引句

| 断言 | 本端实测 | 裁定 |
|---|---|---|
| §7.2 "Death is the point"、§7.3、§7.4 小节顺序 | 小节标题在位（L233/237/243） | **一致** |
| §9.1 master table 行 = "Pass (author-attested freeze; pre-registered tier — §7.4)" | L289 逐字命中；"author-attested freeze" 全文 3 处 | **一致** |
| "buys verifiability, not independence" | L245 逐字命中 | **一致** |
| §9.2 四项 limitation（Selection effect/Scale/Magnitude/Tiers） | §9.2 首段四词全部在位且语义相符 | **一致** |
| R36 在 §6.1 仅作书目锚（无直引） | 正文 [R36] 仅 L176 一处、无引号 | **一致** |
| Helmholtz 仅 §2.1 提及、未入池 | 仅 L60 一处 | **一致** |
| R13/R14 [IDENTIFIER-PENDING] 双重声明 | References L324/L325 显式旗标；§1.3(ii)（L52）有语义声明（"unstable identifier snapshots…flagged"），但无字面 token | **一致（"双重声明"按语义成立）** |
| 模型名 anon 化（qwen3/glm53/mistral/gpt/claude/gemini 等不出现） | qwen/mistral/gpt/claude/gemini/doubao/llama/deepseek 在 md/tex/PDF 全部 0 命中 | **一致** |
| "M4 第三方复算走 confidential channel until camera-ready——§7.1 末段明确披露" | **"confidential channel" 措辞全文 0 命中**；实际披露为 §7 引言（L221）："whose identity is anonymized for review and restored at camera-ready"，且位置在 §7 开头而非"§7.1 末段"；§7.4（L245）披露的是 freeze 的作者自证局限 | **不一致（带引号短语属改写/拼接，非文中措辞；披露实体存在但位置与措辞均不符）** |

### 3.3 §2.4–§2.5 锚/门/文献

| 断言 | 本端实测 | 裁定 |
|---|---|---|
| 5 锚 PDF 各 1 次全 p15；TeX L324 与 MD L229 各 1 次 | 全部直验吻合（见 §2.2） | **一致** |
| compile_verification 五门全绿（Z1–Z4/S1–S6/C1–C3d/G1–G7/D1–D6） | compile_verification.txt 通读核对：全部 PASS + 3 项 DISC 申报，与 Pass 2 转述一致 | **一致** |
| 池号首现序完整覆盖 | 本端独立重算 54 条首现序与 compile_verification L99 **逐项一致**（R01, R54, R13, R14, R42, …, R29） | **一致** |
| References TeX "L411–509" | 实测：`\section` L411、R01 条目 L419、R54 条目 L508、`\end{itemize}` L509 | **一致（±1 行，闭环境标签口径）** |
| R37 访问日期/R53 emis/R54 "1876 works" 渲染 | 三处均直验在位（R37 p20 题录区、R53 题录 p22、R54 p23） | **一致** |
| D6："仅 @ 出现在 hybrid_norm@0.5 字段路径与 en.wikisource.org URL" | wikisource URL **无 @**（PDF 文本层 @ 仅 1 处 = hybrid_norm@0.5，p16；tex 15 个 @ 见 §2.4-D6） | **不一致（wikisource 归因错误；邮箱零命中结论仍成立）** |
| GRAY 项（跨 backbone framing、制品规约未上正文） | — | **属判断性结论，不可本地复核** |
| "报告字节数：报告最终定稿字节数（含本行）" | **占位符未填**（模板残留；实测 11390 B）；报告 SHA-12 声称"在外层汇报消息中给出"，文件内无 → 不可复核 | **不一致（占位符残留）／SHA 不可本地复核** |

---

## 四、54 条池闭合与 §7 零改动（独立复算）

1. **池闭合**：正文唯一 Rnn 指针 54 个、值域恰 R01–R54（无缺失/无多余/无越界）；References 列表 54 条；tex `\item[Rnn.]` 54 个唯一。**闭合成立**。
2. **首现序**：独立重算与 compile_verification L99 逐项一致（含 R54 第 2 位、R09 先于 R08 等非平凡序）。
3. **§7 零改动**：以剥离正文对上一链头（查理文献合并版，SHA `76eef1dd…`，378 行）做全量 diff：**L219–L246（§7 全节）零 diff 块**；全部 13 处行级变更（L52/L60/L62/L100/L109/L176/L186–188/L190/L267/L298/L308/L354＋L378 后追加 R53/R54）逐一落在 R2 申报触点内（C-1–C-4＋计数同步×3＋R37 日期＋新池），词级 diff 复核无第 14 处。**零改动声明成立**。
4. **R2 旧句清除**："inherits exactly these four demands and nothing else"、"found the language ready" 均 0 残留。

---

## 五、重点甄别：错误／幻觉／过度承诺汇总

| # | 类型 | 内容 | 影响 |
|---|---|---|---|
| F-1 | 自报指纹不符 | Pass 1 自报 "SHA-12 = 17AF43E49D57（8192 B）"，实测 8257 B / `70bd41d9722d` | 报告自证链不可采信（有自引用保留条款，但字节差异表明自报非最终稿快照） |
| F-2 | @ 归因错误（Pass 1） | "15 个 @ 全为 TeX 宏"——4 个为 tabularx 列规格 `@{}`、1 个为 `hybrid_norm@0.5`（非宏，渲染入 PDF p16 文本层） | 结论（邮箱零）不受影响 |
| F-3 | @ 归因错误（Pass 2） | "@ 出现在 hybrid_norm@0.5 与 en.wikisource.org URL"——后者无 @ | 同上 |
| F-4 | 措辞拼接（疑似幻觉式改写） | Pass 2 引号短语 "confidential channel until camera-ready" 全文 0 命中；实际为 §7 引言 "anonymized for review and restored at camera-ready"，且非其所称"§7.1 末段" | 披露实体存在、位置与措辞错 |
| F-5 | 引语不逐字（Pass 1） | 《the unnatural explanation》《no wilfully ignore》非字面子串（实际引语在位） | 轻微误导 |
| F-6 | 归属表述错位（Pass 1） | "M1/M3/M4 标注 …formalization outright"——"outright" 仅 L196 一处且只指 M3 | 轻微 |
| F-7 | 歧义表述（Pass 1） | "[R36]…无题录"——References L353 实有 R36 题录（准确说法：正文提及处无内联题录） | 轻微 |
| F-8 | 占位符残留（Pass 2） | "报告字节数：报告最终定稿字节数（含本行）"未填值（实测 11390 B） | 报告完成度缺陷 |

**无发现的类型**：两报告对**论文实体**的全部可程序化断言（指纹、锚、池、触点、数字、双盲、零改动）未发现任何虚假结论；未发现对论文缺陷的掩盖性虚假"PASS"。

---

## 六、总裁定

1. **"0 FAIL" 是否被本端复算支持**：**支持**。Pass 1"全 PASS / 0 FAIL / 0 GRAY"与 Pass 2"4 PASS + 1 GRAY / 无 FAIL"中，凡可程序化重验的论文侧断言，本端 100% 复算吻合（§一–§四共 40+ 项全绿）。
2. **用户"结论不完全可信"的质疑**：**有据，但限于报告自身质量而非论文**。两报告存在 F-1–F-8 共 8 处实体缺陷（自报指纹不符、两处 @ 归因错误、一处引号措辞拼接、占位符未填等），证明其**细节层确有幻觉式改写与过度承诺**（尤其自报 SHA-12 与"confidential channel"引语），**主结论恰好未被这些缺陷推翻**。采信建议：采信其 PASS/GRAY 结论，不采信其自报指纹与逐字引语（引用前须回原文核对）。
3. **不可本地复核项**（如实列出）：novelty/GRAY 的学术判断；"0 LLM 调用/未调 API/〔IM〕/push"等行为性自我声明；Pass 2 自报 SHA-12（声称在外层消息，文件内无）；两报告的审计时间戳（与文件 mtime 22:42 相容）。

## 附注

- 本轮全部断言均为本地确定性复算，未使用联网/外部技能；用户新指令（借鉴 kimi/coze 双审思路、允许联网学习 github 技能）已记录，作为后续审计流程增强方向，不影响本轮任何裁定。
- 观察项（两报告均未提及，非违规）：论文 §9 尾有申明性 AI 披露行 "The drafting model is GLM."（md L304 / tex L409 / PDF p20），属明示的 AI 使用披露，非身份泄露，与双盲不冲突；backbone 模型名（qwen/glm53/mistral 等）确已全部 anon 化。
- 复核工作区（私有，含全部命令可重放）：`agents/6a962cc259312f271f3f1e75/minimax_recheck/`。
