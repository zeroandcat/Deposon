# V5 批17 M-Q14 ② · 「1D 临界方程」文献级出处 · 外部调取结果件（lit-search）

> **性质**：**外部调取结果件（并列登记件）**。本件**不是**预登记件、**不是**判定件、**不是**复审登记件、**不是**实验结果件。
> **派工依据**：`results/_v5_confirm_b16_b17_decisions_register_2026_09_29.md`（本棒实测 SHA-12 `8e36a3e4c6ff` / 29,624 B）**M-Q14 ②** ＋ 该册 **§3 执行面表第 10 行**「外部调取 1D 临界方程文献级出处（派工方＝worker）」。
> **授权边界（沿册 §2.1 ② 逐字）**：⭐ 授权 ＝ 调取 1D 临界方程的**文献级出处**（书目 ＋ 正文 ＋ 页码/式号）；⛔ **0 含**「据外部文献改判据或改结论」；⛔ **0 含**「0 标注来源即引用」。
> **本件 0 做**：0 改任何既有件、0 改判 #12、0 预设 `γ-R1` 复审结论、0 代裁「定义因子」之争、0 编造文献号/题名/作者/DOI、0 用任何 key、0 加载 skill（派工单未指定 skill 名）、0 把「检索器 0 命中」记作「文献中无此式」。
> **出证方**：**Mavis 团队 worker**（本棒执行者）。**不冒充** PI / protocol-keeper / verdict-keeper / evidence-auditor / doc-writer / verifier / Trae code / 任一受托方。
> **补登 ≠ 回改**：本件**纯新增**；所引既有件**全部只读**。

---

## §0 一句话结论

> **「1D 临界方程」的文献级出处（正文 ＋ 页码/式号）本轮仍未取得，R-J5 状态不变。** 本轮取得的是：① 盘上既有三条候选 **C1/C2/C3 的书目级全部实测可达**（其中 **C3 由「间接」升级为 Crossref 直查 OK**）；② **1 条本轮新增的开放获取来源 C4**（arXiv:2203.15050 全文 PDF 实取 6,550,935 B），其正文 **p.26 式 (3.22)** 逐字给出 `sinh(2βcJ⊥) sinh(2βcJ‖) = 1`，⭐ 但其**对象是二维各向异性经典 Ising 模型、不是 1D TFIM** ⇒ **登记为「同函数形式、异对象」，0 充当 1D 方程出处**；③ **1 条已取全文但 0 命中目标式**的来源 C5。C1/C2/C3 今日实测**全文仍 closed**（OpenAlex 本轮复测 ＋ 沿 09-27 四渠道记录）。

---

## §1 指代核明（防转述失真 · 先读册再检索）

### §1.1 M-Q14 ② 中「1D 临界方程」的确切指代

沿册内引件链（册 L111-L118 → 清册 `results/_v5_r2h2_residual_merged_catalogue_2026_09_29.md` L314-L320 → `results/_v3_recheck_12_jsv_check_2026_09_27.md`（`2b9e886e729d`）L105-L109 / L121 → `results/_v3_recheck_12_rj5_provenance_2026_09_27.md`（`20f15c49feb5`）L58 / L92-L104）逐环定位，落点唯一：

| 项 | 内容（盘上字面，非本件改写） |
|---|---|
| **方程本体** | `sinh(2K) sinh(2Γ) = 1`（1D 横场 Ising 链 TFIM 的精确临界条件） |
| **等价闭式** | `h_c/J = 2·t_rel·asinh( 1 / sinh( 1/(2·t_rel) ) )` |
| **符号体系（deposon #12 声明）** | `H = -(J/4) Σ_i σ^z_i σ^z_{i+1} - (h/4) Σ_i σ^x_i`；`K ≡ βJ/4`；`Γ ≡ βh/4`；`t_rel ≡ k_BT/J = 1/(4K)` |
| **所属件** | V3-R **#12** 补审（`results/_v3_recheck_12_*` 四件套） |
| **权威落点** | `results/_v3_recheck_12_result_2026_09_27.json`（`cdb37ed0b32f`）键 **`(a)_critical_condition`** 三行：`convention` / `exact_condition` / `closed_form` |
| **与 γ-R1 的关系** | 争点**不是**该方程是否存在，而是**文献中 `K`、`Γ` 相对 `J`、`h` 的定义因子**（`20f15c49feb5` §2.3）⇒ **本件只交「方程出处」事实，对因子之争 0 表态** |

⚠️ **0 混同声明**：本件交付的是 M-Q14 **②**（方程的文献级出处）；**非** M-Q14 **③**（`#12` 复审登记，归 doc-writer）；**亦非** γ-R1 的「`r` 判读式」（A 级源四件套判定，归 protocol-keeper/verdict-keeper 线）。三者**不合并、不代裁**。

### §1.2 授权字面 vs 本件交付字的对照（如实登记）

| 授权要求的层级 | 本轮取得情况 |
|---|---|
| **书目** | ✅ C1 / C2 / C3 三条**本轮实测可达**（Crossref 直查，见 §4） |
| **正文** | ⚠️ C1 / C2 / C3 **正文 0 取得**（今日实测仍 closed）；C4 / C5 正文**已取得**（开放获取 arXiv PDF） |
| **页码/式号** | ❌ **对 1D TFIM 目标式 0 取得**；C4 取得的是**异对象**式号（p.26 式 (3.22)） |

---

## §2 盘上核验（先核后引 · 本棒实测）

### §2.1 方程在 deposon 盘上件的出现面

| # | 件 | 位置 | 字面/作用 |
|---|---|---|---|
| 1 | `results/_v3_recheck_12_executor_2026_09_27.py`（`4850b1cbb010` / 49,430 B） | **L120** | 注释：`sinh(2K) sinh(2G)=1`，自称「1D TFIM 的**标准精确临界条件**」 |
| 2 | 同上 | **L124-L125** | `TFIM_CONVENTION` ＝ 哈密顿量 ＋ `K ≡ βJ/4`、`Γ ≡ βh/4`、`t_rel ≡ k_BT/J = 1/(4K)` |
| 3 | 同上 | **L128-L130** | `tfim_critical_condition_residual()`：`sinh(2·κ)·sinh(2·γ) − 1` |
| 4 | 同上 | **L133-L148** | `tfim_h_c_over_j()`：由条件推闭式的**逐字推导**（`Γ_c = 0.5·asinh(1/sinh(2K))`、`h_c/J = 2·t_rel·asinh(1/sinh(1/(2·t_rel)))`） |
| 5 | 同上 | **L114-L122** | 件内自查勘误：初版 2×2 迁移矩阵简并推导**作废**，改用「标准精确条件」；作废值 `h_c/J = 2t·asinh(e^{−2/t})` **未参与任何判定** |
| 6 | `results/_v3_recheck_12_rescript_2026_09_27.md`（`1cd36ac1b2c0` / 19,914 B） | **L56-L60、L62** | (a)/(b) 两臂字面引该条件与闭式 ＋ 二分独立核验 |
| 7 | 同上 | **L73-L77、L183-L185** | 勘误留证 ＋ γ₀/γ₁/γ₂ 登记 |
| 8 | `results/_v3_recheck_12_result_2026_09_27.json`（`cdb37ed0b32f` / 187,612 B） | 键 **`(a)_critical_condition`** | `convention` / `exact_condition` / `closed_form` 三行逐字落盘 |
| 9 | `results/_v3_recheck_12_jsv_check_2026_09_27.md`（`2b9e886e729d` / 14,525 B） | **L79-L81** | C1 / C2 / C3 三条候选书目表（DOI 逐字给出） |
| 10 | 同上 | **L107-L109**（§4.3）、**L121**（J-5） | 缺口原文：「#12 §3.1 所引 1D 精确临界『方程』本身，本次未取得逐字文献出处」「其文献级引用仍是待补项」 |
| 11 | `results/_v3_recheck_12_rj5_provenance_2026_09_27.md`（`20f15c49feb5` / 23,822 B） | **L58**（§2.1 目标方程行）、**L59-L62**（C1/C2 页码・式号 ＝ `null`）、**L92-L104**（γ-R1 条件式）、**L148-L151**（§3.1 逐字对照表）、**L181**（R-1） | R-J5 缺口本体 ＋ 四渠道 closed 记录 |

### §2.2 盘上既有候选与本轮的关系（**事实陈述 · 0 判定**）

- 盘上 §2.1 表第 9 行的 **C1 / C2 / C3** ＝ 本轮 §4 的 **C1 / C2 / C3**，**同一 DOI 同一件**；本轮**未改动**其任何登记值，只把**核验层级**逐条升级（见 §4「本轮核验层级」列）。
- 盘上**全仓实测 0 出现**本轮新增的两个 arXiv ID（`2203.15050` / `1109.0104`）⇒ **C4 / C5 属盘上 0 出现的新增外部件**，与既有件**无覆盖、无合并**。
- **R-J5 缺口状态**：盘上登记为「四渠道 closed、页码/式号 ＝ `null`」；**本轮实测后该状态不变**（C1 今日 OpenAlex 复测仍 `closed`；C2/C3 沿 09-27 记录，本轮未另开渠道复测，见 §4 各条「本轮实测」列的诚实标注）。

---

## §3 外部调取：渠道清单与命中/失败留痕（全量 · 本轮实测）

> 全部联网动作发生在 **2026-09-29 17:05–17:30 CST 会话窗口**内（**本件未逐条打时间戳**，如实交代）；**0 注册、0 登录、0 提交表单、0 cookie**。
> 工具口径：结构化 API 经 `web_fetch`；arXiv 网页/PDF 经本机 `python urllib`（与 09-28 γ-R1 棒同路径）；PDF 文本抽取经本机 `pypdf`。
> **0 teamorouter / 0 openrouter / 0 LLM API 调用 ⇒ 0 代理需求**（PI「teamorouter/openrouter 必走 tun」口径**本棒不触发**）；**0 key 读取、0 key 落盘、0 key 入 prompt/JSON/log**（R4 无例外）。

| # | 端点 | 请求 | 实测返回 | 取得层级 | 判定 |
|---|---|---|---|---|---|
| n1 | `api.openalex.org` | `works?filter=fulltext.search:"sinh(2K)",fulltext.search:"sinh(2Γ)"` | `200`，`meta.count = 0` | 仅计数 | ⚠️ **0 命中 ≠ 文献无此式**（见 §7.2 检索器口径） |
| n2 | `api.crossref.org` | `works/10.1016/0003-4916(70)90270-8`（C1） | `200`，完整书目 | **书目级** | ✅ 可达 |
| n3 | `api.openalex.org` | `fulltext.search:"sinh(2K) sinh(2Γ)"` | **`429` Rate limit exceeded**（`retryAfter ≈ 30-39 s`） | 无 | 如实留痕 |
| n4 | `api.openalex.org` | `fulltext.search:"sinh(2K)"` | **`429`** | 无 | 如实留痕 |
| — | （等待） | `Start-Sleep 45` | — | — | 限流规避 |
| n5 | `api.openalex.org` | `fulltext.search:"sinh(2K) sinh(2Δ)"`（Δ 变体） | **`429`** | 无 | 如实留痕 |
| n6 | `api.openalex.org` | `fulltext.search:"sinh(2K)"` | `200`，`meta.count = 779` | 题录级 | **该串单独太宽**：top-25 多为 PDE/流体/数论等无关学科 |
| n7 | `api.openalex.org` | `+ fulltext.search:"transverse field Ising"` | `200`，`meta.count = 25` | 题录级 | 收敛到候选池（本件 C4/C5 即取自该池，**非凭记忆猜测**） |
| n8 | `api.openalex.org` | `fulltext.search:"sinh(2K) sinh(2Γ) = 1" + "Ising"` | `200`，`count = 0` | 仅计数 | ⚠️ 同 n1 |
| n9 | `eutils.ncbi.nlm.nih.gov` | `esearch db=pmc term="sinh(2K)" AND "transverse field Ising"` | `200`，`count = "0"`，`querytranslation` 将串**改写**为 `"sinh 2k"` | 仅计数 | ⚠️ PMC 收刊面有限，**0 推广**为全领域查无 |
| n10 | `zenodo.org/api` | `records?q="sinh(2K)" AND "transverse field Ising"` | `200`，`hits.total = 0` | 仅计数 | 如实留痕 |
| n11 | `www.bing.com`（`setmkt=en-US&ensearch=1`） | 精确串 `"sinh(2K) sinh(2Γ)" transverse field Ising` | `200` HTML，**结果区 0 条**：返回「Your country or region requires a strict Bing SafeSearch setting…」 | 无 | ⛔ **通用搜索引擎本轮不可用**（09-28 记「部分搜索结果未予显示」，本轮为地区 SafeSearch 限制，**同族不同根因**） |
| n12 | `api.openalex.org` | `fulltext.search:"sinh(2K) sinh(2G" + "Ising"` | `200`，`count = 0` | 仅计数 | ⚠️ 同 n1 |
| n13 | `www.ulri.kari.fi`（HEAD） | `/publications/lecture-notes.pdf` | **network request failed** | 无 | ⛔ 不可及（09-28 记 SSL EOF，**本轮同向不可及**） |
| n14 | `arxiv.org`（python） | `GET /abs/1109.0104` | `200`，42,879 B，12.5 s | 题录级 | ✅ arXiv 通道**可用** |
| n15 | `arxiv.org`（python） | `GET /pdf/1109.0104` | `200`，**1,978,856 B**，1.9 s | **正文级** | ✅ 已落 `.scratch_b16_lit/1109.0104.pdf` |
| n16 | `arxiv.org`（python） | `GET /pdf/2203.15050` | `200`，**6,550,935 B**，5.0 s | **正文级** | ✅ 已落 `.scratch_b16_lit/2203.15050.pdf` |
| n17 | `api.openalex.org` | `works/doi:10.1016/0003-4916(70)90270-8`（C1 **今日复测**） | `200`：`is_oa:false`、`oa_status:"closed"`、`any_repository_has_fulltext:false`、`best_oa_location:null` | 仅元数据 | ⛔ **C1 全文今日仍不可得** |
| n18 | `api.crossref.org` | `works/10.1007/978-3-540-49865-0`（C2） | `200`，完整书目 ＋ ISBN ＋ LNM 丛书 | **书目级** | ✅ 可达 |
| n19 | `api.crossref.org` | `works/10.1016/0003-4916(61)90115-4`（C3） | `200`，完整书目 | **书目级** | ⭐ **C3 由「间接」升级为直查 OK** |
| n20 | `www.googleapis.com/books` | `volumes?q="sinh(2K) sinh(2Γ)"` | **network request failed** | 无 | ⛔ 不可及（Google Books 全文检索本轮**用不上**） |
| n21 | `export.arxiv.org/api`（python） | `all:"transverse field Ising" AND all:"duality"`，`max_results=25` | `200`，25 条 ID | 题录级 | top-25 标题**全为** 2024–2026 Kramers–Wannier 算符/畴壁/非可逆对称类（**非**有限温临界线著述） |
| n22 | `export.arxiv.org/api` | `id_list=2203.15050,1109.0104` | `200`，完整题录 ＋ journal_ref ＋ DOI 字段 | 题录级 | ✅ C4/C5 书目**逐字取得** |

**失败/不可及根因汇总（3 类，不混淆）**：① **速率限制**（OpenAlex 429 ×3，规避后恢复）；② **地区/反自动化限制**（Bing 地区 SafeSearch、09-28 另有 Mojeek 403 / searx 域停放 / Semantic Scholar 429 —— **本棒 0 调用后三者**）；③ **网络不可达**（`googleapis.com`、`ulri.kari.fi`）。**另有 1 次** python 下载尝试挂起 > 2 min，本棒**主动取消**并如实留痕（`task_stop`，0 产物）。

---

## §4 候选清单（逐条带可追溯标识 ＋ 本轮实测可访问性）

> 判读纪律：**每条的「本轮实测」列只写本棒真的拿到的东西**；未取得的一律写「未取得」，**0 从摘要反推、0 声称已定位出处**。

### C1 ｜ Pfeuty 1970（本棒实测：书目级可达；正文仍不可得）

| 项 | 内容 |
|---|---|
| 书目 | Pfeuty, P. (1970). *The one-dimensional Ising model with a transverse field.* **Annals of Physics 57(1), 79–90** |
| 可追溯标识 | **DOI `10.1016/0003-4916(70)90270-8`**（Elsevier）；Crossref 另有 Elsevier TDM 文本挖掘链接（**需 key ⇒ 本棒 0 调用**） |
| 本轮实测 | ✅ `200` Crossref 直查：题名/作者/卷期/页 `79-90`/出版者/年份 `1970-03` 逐字一致，`is-referenced-by-count = 1545`；❌ 全文：`200` OpenAlex 复测仍 `closed`、`any_repository_has_fulltext:false` |
| 页码/式号 | **`null`**（正文 0 取得；沿 `2b9e886e729d` §3 / `20f15c49feb5` §2.1 登记，本件**未改写**） |
| 与盘上关系 | ＝ 盘上既有候选 **C1**（`2b9e886e729d` L79）**同一件**；盘上另记 `boss_pc_2_transverse_field_ising.py:30` `PFEUTY_H_C_OVER_J = 1.0` 冻结引用 |

### C2 ｜ Chakrabarti–Dutta–Sen 1996（本棒实测：书目级可达；正文仍不可得）

| 项 | 内容 |
|---|---|
| 书目 | Chakrabarti, B. K.; Dutta, A.; Sen, P. (1996). *Quantum Ising Phases and Transitions in Transverse Ising Models.* Lecture Notes in Physics Monographs, Springer, Berlin/Heidelberg |
| 可追溯标识 | **DOI `10.1007/978-3-540-49865-0`**；ISBN `9783540610335`（print）/ `9783540498650`（electronic）；ISSN 0940-7677 |
| 本轮实测 | ✅ `200` Crossref 直查（题名/三作者/丛书/出版地/年份 1996 逐字一致，被引 220）；❌ 全文：沿 09-27 记录 `closed`（OpenAlex `best_oa_location=null`、Springer 落地页 `<meta name="access" content="No">`、PDF 直查仅状态码）—— **本棒 0 另开渠道复测，如实标「沿 09-27 记录」** |
| 页码/式号 | **`null`**（沿盘上登记；09-27 实测章节信息：`_2` Transverse Ising Chain (Pure System) pp. 17–49） |
| 与盘上关系 | ＝ 盘上既有候选 **C2**（`2b9e886e729d` L80）**同一件**；盘上记其为「章节最对口」对象 |

### C3 ｜ Lieb–Schultz–Mattis 1961（⭐ **本轮核验层级升级**）

| 项 | 内容 |
|---|---|
| 书目 | Lieb, E.; Schultz, T.; Mattis, D. (1961). *Two soluble models of an antiferromagnetic chain.* **Annals of Physics 16(3), 407–466** |
| 可追溯标识 | **DOI `10.1016/0003-4916(61)90115-4`** |
| 本轮实测 | ✅ **Crossref 直查 `200`**（题名/三作者/卷 `16`/期 `3`/页 `407-466`/年份 `1961-12` 逐字一致，被引 3870）⇒ ⭐ **由盘上「间接（DOI 于 C1 参考文献列表中实测出现，未单独直查）」升级为「直查 OK」**；❌ 全文：Elsevier 闭源，**本棒 0 调用 TDM（需 key）** |
| 页码/式号 | **`null`**（正文 0 取得） |
| 与盘上关系 | ＝ 盘上既有候选 **C3**（`2b9e886e729d` L81）**同一件**；该 DOI 同时出现在 C1 的 Crossref 参考文献列表（BIB3，`first-page 407`）—— **本轮两处互证** |

### C4 ｜ **本轮新增** · arXiv:2203.15050（开放获取 · **正文级已取得** · ⭐ **异对象**）

| 项 | 内容 |
|---|---|
| 书目 | Dantchev, D. M.; Dietrich, S. *Critical Casimir Effect: Exact Results.* **arXiv:2203.15050v2 [cond-mat.stat-mech]**（v1 2022-03-28 / v2 2022-12-12；218 页） |
| 可追溯标识 | **arXiv ID `2203.15050`**；arXiv 记录载 **journal_ref**：*Physics Reports* **Vol. 1005**, 19 March 2023, pp. 1–130；**DOI `10.1016/j.physrep.2022.12.004`**（⚠️ 此 DOI 出自 arXiv 记录字段，**本棒未单独直查 Crossref**，故标「记录所载」） |
| 本轮实测 | ✅ PDF `200`：**6,550,935 B**，1.9 s 落盘 ＋ 实测 **SHA-12 `fad245b45631`**；`pypdf` 实测 **218 页**，正文可抽取 |
| **正文命中（逐字 · pypdf 抽取，PDF **第 26 页**，式号 **(3.22)**）** | `For this model the bulk critical temperature Tc = 1/(kBβc) is implicitly given by the equation [10, 374, 375] sinh(2βcJ⊥) sinh(2βcJ‖) = 1. (3.22)` |
| 抽取质量交代 | `⊥` / `‖` / `βc` 为 PDF 文本抽取所得上下标记号（**0 回改**）；同文自注式 (3.22) 所引文献编号为 `[10, 374, 375]` |
| ⭐ **对象判定（读法 · 0 判定）** | 该式所在小节为同文 §3.3.2「The two-dimensional Ising model」（自 PDF p.25 起），变量记号为**二维方格各向异性**的 `J⊥`、`J‖` ⇒ **其对象是二维经典各向异性 Ising 模型**，**不是** deposon #12 的 1D TFIM（`K ≡ βJ/4`、`Γ ≡ βh/4` 那一族）。⭐ **⇒ 本条登记为「同函数形式、异对象」；0 充当 1D 临界方程的出处；0 就其与 #12 约定的异同作任何判定** |
| 与盘上关系 | 盘上**全仓 0 出现**该 arXiv ID ⇒ 新增外部件；**与 C1/C2/C3 无覆盖、无合并**；**0 进入任何判定** |

### C5 ｜ **本轮新增** · arXiv:1109.0104（开放获取 · 正文已取得 · **0 命中目标式**）

| 项 | 内容 |
|---|---|
| 书目 | Matsueda, H. *Entanglement Entropy and Entanglement Spectrum for Two-Dimensional Classical Spin Configuration.* **arXiv:1109.0104v1 [cond-mat.stat-mech]**，2011-09-01，13 页（arXiv 记录**无 DOI 字段** ⇒ 如实记「无」） |
| 本轮实测 | ✅ PDF `200`：**1,978,856 B**，1.9 s 落盘 ＋ 实测 **SHA-12 `5effa9566a40`**；`pypdf` 实测 13 页 |
| 命中情况 | **0 命中目标式**。实测 `sinh(2` 的唯一出现位于 **p.6 式 (25)**，属 **2D 经典 Ising 的 Onsager 自由能** `−βf = ½ log(2 sinh 2K) + (1/2π)∫…`，且该文把 `K = βJ` 逐字定义（**`0 处** `asinh`、**0 处** 1D TFIM 临界线）⇒ **0 命中 ＝ 已取全文后的实测结果**（非「未取得」），**与 n1/n8/n12 的「检索器 0 命中」性质不同，不混记** |
| 与盘上关系 | 盘上 0 出现；**0 参与任何判定** |

### §4.1 候选计数（与派工单口径对齐）

| 口径 | 数量 |
|---|---|
| 候选出处条数 | **5**（C1 / C2 / C3 ＝ 盘上既有 ＋ C4 / C5 ＝ 本轮新增） |
| 书目级**本轮实测可达** | **3 / 5**（C1、C2、C3） |
| 正文级**本轮实测取得** | **2 / 5**（C4、C5，均为开放获取 arXiv） |
| **对 1D TFIM 目标式给出「正文 ＋ 页码/式号」者** | **0**（C4 为异对象；C5 0 命中；C1/C2/C3 全文不可得） |

---

## §5 结论分层（**只交事实 · 0 判定**）

1. **书目层**：1D 临界方程的最贴近文献候选（C1 Pfeuty 1970 / C2 Chakrabarti–Dutta–Sen 1996 / C3 Lieb–Schultz–Mattis 1961）**今日全部实测可达且标识逐字可核**；C3 核验层级由「间接」升为「直查 OK」。
2. **正文层**：**0 取得** 1D TFIM 目标式的正文与页码/式号；C1 今日复测仍 `closed`（OpenAlex 文献级 ＋ 位置级双证）。
3. **同形式异对象**：C4 提供 `sinh(2·)·sinh(2·) = 1` 这一函数形式在**二维各向异性经典 Ising**中的**页码/式号级**实证（p.26 式 (3.22)），⭐ 但**对象不同** ⇒ **0 视作 1D 方程的出处**。
4. **⇒ R-J5 状态不变**：`20f15c49feb5` §2.1 登记的「C1/C2 页码・式号 ＝ `null`、正文 0 取得」**未被本轮任何证据推翻**。
5. **本件 0 做**：0 判定 #12 对错、0 判定 γ-R1 前提成立与否、0 触发 `#12` 复审、0 改 R-J5 四渠道 closed 登记、0 放宽「JSV 1999 查无」入链边界。

---

## §6 与 γ-R1 / `#12` 复审面的关系（**防越权声明**）

| 项 | 本件立场 |
|---|---|
| 是否回答了 γ-R1 的「定义因子」之争 | **否**。本件只交「方程的文献级出处」可得性事实；`K`、`Γ` 相对 `J`、`h` 的因子判读属 `20f15c49feb5` §2.3 / §2.4 的一行可判伪核验式，**0 代裁** |
| 是否构成 `#12` 复审理由 | **否**。M-Q14 **③**（`#12` 复审登记）归 doc-writer；本件**0 预设复审结论、0 预先宣布 `(b)` 臂已翻转** |
| C4 能否用作 `(b)` 臂刻度的依据 | **本件不主张、亦不排除**；⭐ 其对象为二维经典模型 ⇒ **若要用于 1D TFIM 刻度，需先解决对象差异，属 PI / verdict-keeper / protocol-keeper 的裁面，0 在本件处理** |

---

## §7 诚实边界与自我更正

### §7.1 本棒 0 做的事（逐条）

- **0 改既有件**：`results/` 下无任何既有文件被写入、覆写、移动或删除（本棒写入仅 1 个新名件 ＋ `.scratch_b16_lit/` 临时抓取区）。只读引用件实测 SHA-12 见 §8.2。
- **0 编造**：本件所载全部题名/作者/年份/卷期/页码/DOI/arXiv ID/式号/页码，**全部来自本轮 §3 实测响应或本轮实取 PDF 的文本抽取**；C4 的期刊 DOI 明确标「记录所载，未直查」；C5 的「无 DOI」明确标「arXiv 记录无此字段」。
- **0 用 key**：Elsevier TDM / Springer TDM / Semantic Scholar / Unpaywall 等需 key 的通道**一律未调用**；**0 key 读取、0 key 落盘、0 key 入 prompt / JSON / log**。
- **0 加载 skill**：派工单未指定 skill 名 ⇒ **0 加载任何 skill、0 引用其条文、0 虚构其条文**。实质纪律锚沿盘上字面（M-Q14 ② 边界 ＋ `2b9e886e729d` §6「0 编造数值」＋ `20f15c49feb5` §1「0 从摘要反推」）。
- **0 代理 / 0 LLM 调用**：本棒 0 触发 teamorouter / openrouter 口径。

### §7.2 ⭐ **检索器 0 命中 ≠ 文献无此式**（三处必须区分，如实标级）

| 现象 | 本件定性 | 依据 |
|---|---|---|
| n1 / n8 / n12 OpenAlex `fulltext.search` 精确串 `count = 0` | ⚠️ **不记为「查无」**。该检索器对数学串执行**分词 ＋ 词干化**（响应 `x_query.oql` 自记 `stemmed "sinh(2K) sinh(2Γ) = 1"`），多 token 数学串与 `=` / `Γ` 字符**0 可靠匹配**；对照实验：单 token `"sinh(2K)"` 同接口 `count = 779`（top-25 多为无关学科 ⇒ 该串过宽） | n1 / n6 / n8 / n12 响应逐字 |
| n9 PMC `count = 0` | ⚠️ **不推广为全领域**。响应 `querytranslation` 已把 `"sinh(2K)"` 改写为 `"sinh 2k"`，且 PMC 收刊面以生物医学为主 | n9 响应逐字 |
| n11 Bing 0 结果 | ⛔ **渠道不可用**（地区 SafeSearch 限制），**非**「0 命中」 | n11 返回页原文 |

⇒ 本件对「1D 临界方程的文献级出处」采用的口径是：**「正文 ＋ 页码/式号 ＝ 本轮 0 取得」**（对 C1/C2/C3 为**实测不可得**，对 C4/C5 为**实测异对象 / 实测 0 命中**），**而非**「该式在文献中不存在」。

### §7.3 主动剔除的反证（不拿不成立的东西说事）

- python 首次下载尝试**挂起 > 2 min 且 0 产出** ⇒ 主动 `task_stop` 取消并如实留痕，**0 把「已下载」写成事实**；随后重试成功（1.9 s / 5.0 s）才登记字节数与 SHA-12。
- C5 取得正文后 `sinh(2` 确有 1 处命中 ⇒ **如实登记该处字面**（p.6 式 (25)），但同时**如实标明其对象是 2D 经典 Ising 自由能**，**0 以「有 `sinh`」包装成「命中 1D 临界式」**。
- OpenAlex 限流 3 次（n3/n4/n5）**0 静默重试轰炸**：等待 45 s 后串行续查，失败全部留痕。

---

## §8 落盘件与只读件实测（SHA-12 ＝ `hashlib.sha256(字节).hexdigest()[:12]`，小写）

### §8.1 本件

| 项 | 值 |
|---|---|
| 路径 | `results/_v5_b16_1dcritical_lit_search_2026_09_29.md` |
| 落盘前同名检查 | ✅ `glob **/*_v5_b16_1dcritical*` → **No files matched**（0 撞名） |
| 字节 / SHA-12 | **自哈希不可内含**（写进去即改自身哈希，自指悖论；沿 `2b9e886e729d` §8 同一惯例）—— 实测值由 worker 在**派工回报**中给出 |
| 编码 / 行尾 | UTF-8 **无 BOM** ＋ **LF**（沿盘上既有登记件实测口径） |

### §8.2 只读引用件（本棒落盘前后**未触动**）

| 件 | SHA-12 | 字节 |
|---|---|---|
| `results/_v5_confirm_b16_b17_decisions_register_2026_09_29.md` | `8e36a3e4c6ff` | 29,624 |
| `results/_v3_recheck_12_jsv_check_2026_09_27.md` | `2b9e886e729d` | 14,525 |
| `results/_v3_recheck_12_rj5_provenance_2026_09_27.md` | `20f15c49feb5` | 23,822 |
| `results/_v3_recheck_12_executor_2026_09_27.py` | `4850b1cbb010` | 49,430 |
| `results/_v3_recheck_12_rescript_2026_09_27.md` | `1cd36ac1b2c0` | 19,914 |
| `results/_v3_recheck_12_result_2026_09_27.json` | `cdb37ed0b32f` | 187,612 |

⭐ 前两件的 SHA-12 与册内 L316 所记 `2b9e886e729d` / `20f15c49feb5` **逐字一致** ⇒ 本件所引为**同一件**（防同名不同件）。

### §8.3 本棒临时抓取区（非交付件 · 可弃）

- `.scratch_b16_lit/1109.0104.pdf`（1,978,856 B / `5effa9566a40`）、`.scratch_b16_lit/2203.15050.pdf`（6,550,935 B / `fad245b45631`）、`.scratch_b16_lit/arxiv_ids.txt`。**0 计入交付面**；保留仅为留痕（沿 09-28 γ-R1 棒 `.scratch_gamma_r1/raw/` 同惯例）。

---

## §9 未决 / 待拍板清册（穷尽清点 · 本件 0 代裁）

| # | 项 | 性质 | 归口 |
|---|---|---|---|
| 1 | **C1/C2/C3 正文取得授权**（Elsevier TDM / Springer TDM / 机构订阅） | 需授权/需 key ⇒ **本棒 0 越权** | PI |
| 2 | **是否以 C4（二维经典模型、同形式异对象）作为 1D 方程的「形式旁证」入册** | 呈现面 ＋ 口径面：**对象不同，是否算数由 PI / verdict-keeper 裁** | PI / verdict-keeper |
| 3 | **1D TFIM 目标式的页码/式号 0 取得 ⇒ R-J5 仍 open** | 缺口状态（本件未改变） | protocol-keeper / evidence-auditor |
| 4 | **M-Q14 ①「JSV 1999 查无」入链**与 ③「`#12` 复审登记」两件 | **不在本棒范围**（归 doc-writer），本件 0 触碰 | doc-writer / parent |
| 5 | 若 PI 另行给出**1D TFIM 临界式文献线索**（册 §2.1 ② 已明示「PI 另给线索亦可」） | 采信面：**PI 记忆 > 本件检索结果** | PI |
| 6 | 通用搜索引擎（DDG / Mojeek / Bing-se / searx / Semantic Scholar）在本机**长期不可用** | 渠道可用性事实，影响后续检索口径 | parent（如需换检索面） |

---

## §10 署名

**Mavis 团队 worker 出件** ｜ 2026-09-29 ｜ 会话窗口 17:05–17:30 CST
配套只读锚件：`8e36a3e4c6ff`（落册册）· `2b9e886e729d`（JSV 查无件）· `20f15c49feb5`（R-J5 provenance 件）
本件**0 判定、0 改判、0 改既有件、0 编造、0 用 key、0 加载 skill**。
