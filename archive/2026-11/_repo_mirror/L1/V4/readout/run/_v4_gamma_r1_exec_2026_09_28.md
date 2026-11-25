# V4 γ-R1 补审执行件（逐源检索核验 · worker · 2026-09-28）

> **性质**：预登记件 `_v4_gamma_r1_prereg_2026_09_28.md`（`02c072833cca`）§10 段 ② 的**执行棒**产物 —— 逐源检索核验 + 四件套留痕 + STOP 条件计数。
> **生效依据**：PI 2026-09-28 17:20 拍板「生效 + 接受 3 新立口径」（`r` 比值判读式 / A-B 源分级 / STOP-0 预算），**生效即锁**；本棒**0 修改**预登记件 §3 判死线、§6 STOP 条件、§8 阈值任何字面。
> **0 判定改判**：本棒**不出任何 verdict**（落支裁决归 verdict-keeper）；`#12` 档位**0 触碰**（预登记 §3.4）。
> **0 触动既有件**：`_v4_gamma_r1_prereg_2026_09_28.md`、`_v4_pending_decisions_2026_09_28.md`、`_v3_recheck_verdict_register_2026_09_27.md`、`_v3_recheck_12_executor_2026_09_27.py`、`_v3_recheck_12_rj5_provenance_2026_09_27.md`、任何既有 JSON —— 本棒对以上文件**全部只读 / 未打开写入**，**byte 0 触动、0 覆盖、0 合并**。
> **派生 JSON 0 合并**：本棒**0 新增 JSON、0 修改任何既有 JSON**；逐源记录为**独立新增 md**（预登记 `K-GR1-0-F`）。
> **署名如实**：出证方 = **worker**（本棒执行段），不冒充 protocol-keeper / verdict-keeper / evidence-auditor / doc-writer / PI / Trae code / 任一受托方。

---

## §0 一句话结论

**本棒 A 级合格源 = 0 ⇒ 落 `K-GR1-3`（分歧未决 / 输入不足），且系「因预算上限停止，非因穷尽」。** 面 A–D 已各完成 ≥1 次登记检索（面 E 未及检索，如实登记为**未执行**）；20 次在线查询预算**恰好触顶**（`STOP-0`）；4 份实际取得的开放获取全文**均未出现** `sinh`/`asinh`/`cosh` 任一形迹，亦**未定义** `K`、`Γ` ⇒ 四件套第 3、4 件缺失 ⇒ `r_K`、`r_Γ` 全部**不可判读（null）**；`K`、`Γ` 的定义因子**至今未核**。

---

## §1 本棒权限与执行边界

| 项 | 字面 |
|---|---|
| 检索面 | 预登记 §6.2 冻结面 **A–E**，**0 增删** |
| 判读式 | 预登记 §2.2 式 3（`r_K ≡ K_lit/(β·c_ferro)`、`r_Γ ≡ Γ_lit/(β·c_trans)`），**0 改写** |
| 停止条件 | 预登记 §6.3 `STOP-0 / STOP-1 / STOP-2`，**0 事后延长、0 中途改条** |
| 纪律 | `K-GR1-0-A…H` 全部沿用（0 注册 / 0 登录 / 0 cookie / **0 用任何 API key** / **key 永不明文**） |
| 网络 | 全部经本机 tun 代理 `http/https_proxy=http://127.0.0.1:1018`；串行、间隔 ≥2.5 s（脚本内强制）；**0 调用任何 LLM 端点**（预登记 `K-GR1-0-H` 本棒 0 触发） |

---

## §2 检索面逐面登记（`K-GR1-0-C`）

| 面 | 端点（实际发出） | 检索式 | 时刻(CST) | 返回条数 | 面级结论 |
|---|---|---|---|---|---|
| **A** | `http://export.arxiv.org/api/query` ×5；`https://arxiv.org/pdf/…` ×5 | `A1` `abs:"transverse-field Ising model" AND abs:"exact"`；`A3` `abs:"Ising chain" AND abs:"exact"`；`A5` `abs:"transverse-field Ising model" AND abs:"one-dimensional" AND abs:"critical"`；`A6` `abs:"anharmonic oscillator" AND abs:"transverse-field Ising"`；`A7` `abs:"sinh" AND abs:"transverse-field Ising" AND (cat:cond-mat.stat-mech OR cat:cond-mat.str-el OR cat:quant-ph)` | 17:25:14 / 17:27:21 / 17:28:50 / 17:30:12 / **17:35:05** | 151(total)/20、204(total)/30、109(total)/40、**1(total)/1**、**0(total)/0** | 5 次 API 检索中 **4 次返回大量条目但全文层 0 命中**（所列条目经本地筛查均非含 `K`/`Γ` 定义的 1D 精确临界方程所在处）；`A7` **0 命中**（全文逐字 `sinh` 未出现在任何相关摘要） |
| **B** | `https://doaj.org/api/search/articles/transverse%20field%20Ising%20one-dimensional%20exact%20critical` | 开放获取期刊聚合检索 | 17:32:58 | **total = 9** 篇 OA 期刊条目（NJP ×3、PRResearch ×2、SciPost ×2、JHEP ×1、PRResearch 1） | **元数据层有 9 条候选，全文层 0 取得**（`STOP-0` 预算耗尽，0 抓取任一篇全文）⇒ **0 判读、0 入级**；候选入 §8 队列 |
| **C** | `https://zenodo.org/api/records?q=%22sinh(2K)%22%20transverse%20field%20Ising&size=10` | 开放仓储检索 | 17:33:01 | `total = 385,811`（引号短语未被端点按短语执行，命中被退化为宽匹配）；返回前 10 条**全为 Dataset / Software / Notebook** | **0 命中**（在返回集内无含定义原文的出版物；`0 命中范围` = 前 10 条） |
| **D** | `https://www.bing.com/search` ×2；`https://www.ulri.kari.fi/publications/lecture-notes.pdf` ×1 | 见逐源记录 S5 | 17:29:23 / 17:30:38 / 17:29:55 | 200(100,184 B) / 200(101,170 B) / **握手失败** | **0 命中**：2 次网页检索返回 13 条外部链接**全为无关中文站点**（出口区域化）；讲义 PDF **TLS 握手被中断、正文 0 取得** |
| **E** | **无** | — | — | — | **未执行**（`STOP-0` 触顶前未及检索）⇒ 登记为**未执行**，**0 并入 0 命中计数**；C1/C2 的 OA 副本与引用链扩展**本棒未查** |

> 面 A–D **各 ≥1 次登记**已满足（含 0 命中与失败登记）；面 E 如实标注**未执行**。

---

## §3 查询预算台账（`STOP-0`：≤12 源 / ≤20 次查询 —— **触顶**）

`SHA-12` 定义沿派工单：`hashlib.sha256(data).hexdigest()[:12]`，小写。

| # | 面 | 端点 / URL | 时刻(CST) | 结果 |
|---|---|---|---|---|
| 1 | A | `export.arxiv.org/api/query?…abs:"transverse-field Ising model" AND abs:"exact"` | 17:25:14 | 200 · 37,127 B |
| 2 | B | `api.openalex.org/works?filter=fulltext.search:"sinh(2K)" AND fulltext.search:"sinh(2G"` | 17:25:46 | **429**（端点现需 API key ⇒ 依 `K-GR1-0-G` **0 用 key**，登记为不可用） |
| 3 | B | OpenAlex 同端点内联重试（单条件 `fulltext.search:"sinh(2K)"`） | ≈17:25:55 | **429**（⚠️ 本次为内联重试，**未写入** `query_log.jsonl`，**如实计入预算**） |
| 4 | D | `html.duckduckgo.com/html/?q="sinh(2K)" "sinh(2Γ)"…` | 17:26:30 | **SSL EOF** |
| 5 | A | `export.arxiv.org/api/query?…abs:"Ising chain" AND abs:"exact"` | 17:27:21 | 200 · 52,867 B |
| 6 | D | `www.mojeek.com/search?q=…` | 17:27:48 | **403** |
| 7 | A/B | `scholar.archive.org/search?q="sinh(2K)" "sinh(2G"` | 17:28:19 | **SSL EOF** |
| 8 | A | `export.arxiv.org/api/query?…abs:"transverse-field Ising model" AND abs:"one-dimensional" AND abs:"critical"` | 17:28:50 | 200 · 78,367 B |
| 9 | D | `www.bing.com/search?q=…filetype:pdf` | 17:29:23 | 200 · 100,184 B（0 命中） |
| 10 | D | `www.ulri.kari.fi/publications/lecture-notes.pdf` | 17:29:55 | **SSL EOF** |
| 11 | A | `export.arxiv.org/api/query?…abs:"anharmonic oscillator" AND abs:"transverse-field Ising"` | 17:30:12 | 200 · 2,890 B（total 1） |
| 12 | D | `www.bing.com/search?q=…site:arxiv.org` | 17:30:38 | 200 · 101,170 B（0 命中） |
| 13 | A | `https://arxiv.org/pdf/cond-mat/0206055v2` | 17:31:03 | **404**（版本号不存在） |
| 14 | A | `https://arxiv.org/pdf/2207.09547` | 17:31:43 | 200 · 1,168,885 B · **SHA-12 `eca05c215a3c`** |
| 15 | A | `https://arxiv.org/pdf/0808.1816` | 17:31:49 | 200 · 142,817 B · **SHA-12 `e377d6ef2afe`** |
| 16 | A | `https://arxiv.org/pdf/cond-mat/0512369` | 17:32:29 | 200 · 108,240 B · **SHA-12 `a35361b1dccc`** |
| 17 | B | `doaj.org/api/search/articles/…` | 17:32:58 | 200 · 25,502 B（total 9） |
| 18 | C | `zenodo.org/api/records?q=%22sinh(2K)%22…` | 17:33:01 | 200 · 59,768 B（total 385,811） |
| 19 | A | `https://arxiv.org/pdf/1910.12538` | 17:33:43 | 200 · 410,040 B · **SHA-12 `b622cd5c853c`** |
| 20 | A | `export.arxiv.org/api/query?…abs:"sinh" AND abs:"transverse-field Ising" AND (cats)` | 17:35:05 | 200 · 908 B（**total 0**） |

- **在线查询合计 = 20 ⇒ `STOP-0` 恰好触顶**（含 3 次失败握手、1 次 404、2 次 429）。
- **候选源合计 = 6**（4 份取得全文 + 1 份 404 + 1 份讲义握手失败）≤ 12 ⇒ 源数侧 `STOP-0` 未触顶，**查询次数侧触顶**。
- 触顶后**停止检索**，按当时读数走 §6 STOP 判定。

---

## §4 逐源判读（四件套逐项核对 + 逐字原文）

> 判读顺序遵守 §3.1「**先逐源分类、后计数**」；**0 先看结果后配读法**。
> 机器辅助负证据（`pypdf` 全文抽取后逐串计数，四份全文合计）：
> `sinh` = 0、`asinh` = 0、`cosh` = 0、`tanh` = 0、`K =` = 0、`K ≡` = 0、`κ` = 0；`Γ` 仅在 S4 出现 35 次，**逐处均为广义 Grüneisen 比**（S4 逐源记录已留痕防误挂）。

| 源 | 完整书目 | 公开 URL | 页码 / 式号 | `K`/`Γ` 定义逐字摘录 | 四件套 | `r_K` | `r_Γ` |
|---|---|---|---|---|---|---|---|
| **S1** | Yu & Chakravarty, 2022, *Quantum critical points, lines and surfaces*, arXiv:2207.09547v1 [cond-mat.str-el]（DOI 未核） | `https://arxiv.org/pdf/2207.09547` | 哈密顿量 PDF p2 式 (1)–(4)；critical line p3 | ❌ 无（全文 0 处 `K`/`Γ` 定义） | ❌ 缺 3、4 | **null** | **null** |
| **S2** | Ma, Xu & Wang, 2008, *Reduced fidelity susceptibility in the one-dimensional transverse field Ising model*, arXiv:0808.1816v1 [quant-ph]（DOI 未核） | `https://arxiv.org/pdf/0808.1816` | 哈密顿量 PDF p2 式 (5) | ❌ 无（只有零温 `λ_c = 1`） | ❌ 缺 3、4 | **null** | **null** |
| **S3** | Xiong & Wang, 2006, *A direct calculation of critical exponents of two-dimensional anisotropic Ising model*, arXiv:cond-mat/0512369v2 [cond-mat.stat-mech]（DOI 未核） | `https://arxiv.org/pdf/cond-mat/0512369` | 1D TFIM 方程 PDF p2 式 (9)–(12) | ❌ 无（只有零温 `t_c = h/|J| = 1`） | ❌ 缺 3、4 | **null** | **null** |
| **S4** | Zhang & Ding, 2023, *Finite-Size Scaling Theory at a Self-Dual Quantum Critical Point*, arXiv:1910.12538v2 [cond-mat.str-el]（DOI 未核） | `https://arxiv.org/pdf/1910.12538` | 哈密顿量 PDF p3 式 (10)；自对偶 p2 | ❌ 无（该文 `Γ` = Grüneisen 比，非无量纲横场） | ❌ 缺 3、4 | **null** | **null** |

**逐源要点（每源判读依据原文见各逐源记录件）**

- **S1**：3 自旋扩展 TFIM，`H = − Σ_i (h_i σ^x_i + λ_2 σ^x_i σ^z_{i−1} σ^z_{i+1} + λ_1 σ^z_i σ^z_{i−1})`；其 critical line 位于 `(λ_1, λ_2)` 参数面，**不是** §6.1 构造域（`sinh(2K)·sinh(2Γ) = 1` 所在处）。
- **S2**：`H_I = − M Σ_j [ λ σ^x_j σ^x_{j+1} + σ^z_j ]`，单一比参数 `λ`，临界点 `λ_c = 1`（**零温**）；未给有限温 `h_c(T)`，未给 `K`、`Γ` ⇒ §7.1「**两侧只取到一侧 / 分子侧缺失 ⇒ 不可判读**」。
- **S3**：`e_G(k) = −2 ( h + J cos k + √(h² + 2Jh cos k + J²) )`，`t ≡ h/|J|`，`ΔE = 2|J||t − 1|`，`t_c = 1`（**零温**）；同页式 (2) 抽取残缺（下标/指数被吞），本棒**因此 0 引用该式**、**0 凭残串推断**。
- **S4**：Jordan–Wigner 自由费米子式 `H(g) = − Σ_i (c_i − c†_i)(c†_{i+1}+c_{i+1}) − g Σ_i (2c†_i c_{i−1})`，自对偶点 `g_c = 1`；**未写** `sinh(2K)·sinh(2Γ) = 1`，**未定义**无量纲 `K`、`Γ`。

**0 反推声明**：以上四源**无一**给出 `K`、`Γ` 的定义式；本棒**未**由「方程形式」「零温临界比」或「他处惯例」反补任一因子（预登记 §7.1 明文禁止）。

---

## §5 三分类计数与判死线归属

### 5.1 先分类（逐源）

| 分类 | A 级合格源 |
|---|---|
| 「一半」（`r_K = r_Γ = 1/2` ⇒ `K-GR1-1`） | **0** |
| 「本身」（`r_K = r_Γ = 1` ⇒ `K-GR1-2`） | **0** |
| 「其他 / 不可判读」 | **0**（4 份候选源**未达 A 级**，在 §7.1 下**不进入三类计数**；其 `r_K`、`r_Γ` 记为 null） |
| **A 级合格源合计** | **0** |

### 5.2 构造面自证（预登记 §7.2）

- ① 合格源数 `n = 0`（< 2）⇒ **不构成可判读面**；
- ② 每源须同时给出 `r_K` 与 `r_Γ` ⇒ **0 源满足**；
- ③ `n_distinct` = **0** ⇒ **退化警报**（0 源可区分读数）⇒ **0 带病开跑**。

### 5.3 归属

> **`K-GR1-3`（分支 C · 分歧未决 / 输入不足）**
> 触发依据：A 级合格源 `< 2` ⇒ 落 `K-GR1-3`（预登记 §3.1 互斥穷尽表第三行 + `STOP-2`）。
> **`K-GR1-1` 与 `K-GR1-2` 均 0 触发。** 依 `K-GR1-4`：**「材料不足」不是任一主分支的证据**，本棒**0** 私自落 A 支或 B 支，**0** 软化「暂缓 / 倾向作废 / 有可能成立」。
> **因预算上限停止，非因穷尽**（`STOP-0` 字面要求随落 `K-GR1-3` 一并注明）。
> **本棒 0 出改判裁决**：落支归属的正式裁定归 verdict-keeper；`#12` 档位**0 触碰**（预登记 §3.4）。

---

## §6 STOP 状态

| STOP | 字面条件 | 本棒实测 | 触发 |
|---|---|---|---|
| `STOP-0` | 候选源 ≤ 12 **且** 在线查询 ≤ 20 | 候选源 6；**在线查询 20（恰好触顶）** | ✅ **触顶**（查询次数侧） |
| `STOP-1` | 面 A–D 各 ≥1 次登记**之后**，A 级 ≥ 2 **且** 读数全部同属一支 ⇒ 立即收 | 面 A–D 登记**已满足**；**A 级 = 0** ⇒ 触发条件不成立 | ❌ 未触发（0 凑数、0 提级） |
| `STOP-2` | 面 A–D 枚举穷尽（或 `STOP-0` 触顶）后，A 级 < 2 / 跨类不一致 / 出现「其他·不可判读」⇒ 收 | **`STOP-0` 已触顶** 且 **A 级 = 0** | ✅ **触发 ⇒ `K-GR1-3`** |

**本棒停止位置**：查询 20/20（触顶即停，0 事后延长）；面 E 未及检索（登记为**未执行**，**0 冒充已检索**）。

---

## §7 分歧面并列呈报（`K-GR1-3` 硬约束：逐源成行并排，**0 合并为单值**）

| 行 | 源 | 书目 | URL | 页码 / 式号 | 逐字原文（该文自己的写法） | `r_K` | `r_Γ` |
|---|---|---|---|---|---|---|---|
| ∥ 1 | S1 | Yu & Chakravarty 2022, arXiv:2207.09547v1 | `arxiv.org/pdf/2207.09547` | p2 式(1) | `The Hamiltonian, H, is H =− ∑ i (hiσx i +λ2σx iσz i−1σz i+1 +λ1σz iσz i−1) (1) written in terms of standard Pauli matrices.` | null | null |
| ∥ 2 | S2 | Ma, Xu & Wang 2008, arXiv:0808.1816v1 | `arxiv.org/pdf/0808.1816` | p2 式(5) | `The Hamiltonian of the 1D TFIM reads HI = − M∑ j=−M [ λσx j σx j+1 + σz j ] , (5) … λ is the Ising coupling constant in units of the transverse ﬁeld …` | null | null |
| ∥ 3 | S3 | Xiong & Wang 2006, arXiv:cond-mat/0512369v2 | `arxiv.org/pdf/cond-mat/0512369` | p2 式(10)–(12) | `eG(k) = −2 ( h + J cos k + √ h2 + 2J hcos k + J 2 ) . (10) Denote t = h \|J\| , (11) the excitation gap of ˆH is ∆ E = 2\|J\|\|t − 1\|. (12)` | null | null |
| ∥ 4 | S4 | Zhang & Ding 2023, arXiv:1910.12538v2 | `arxiv.org/pdf/1910.12538` | p3 式(10) | `The Hamiltonian is mapped to free fermions, H(g) =− ∑ i (ci−c† i)(c† i+1+ci+1)−g ∑ i (2c† ici− 1). (10)` | null | null |

**读数列**：`r_K` = (null, null, null, null) ∥；`r_Γ` = (null, null, null, null) ∥ ⇒ **0 择优、0 取均值、0 加权合并、0 以多数源裁决**（四行读数全同为空，非「一致同意某个值」）。

**0 命中面清单（随呈报）**：面 A `A7` 检索 0 命中（17:35:05）；面 B DOAJ 9 条元数据候选**全文 0 取得**；面 C Zenodo 返回集 0 相关出版物；面 D 3 次尝试 0 命中（2 次区域化无关 + 1 次握手失败）；面 E **未执行**。

---

## §8 候选队列（**0 判读、0 入级**，供下一棒在预算内优先抓取）

| 候选 | 面 | 定位 | 为何值得下一棒抓 |
|---|---|---|---|
| `10.1103/PhysRevResearch.6.043139` | B | *Exact Fisher zeros and thermofield dynamics across a quantum critical point*（PRResearch，全 OA） | 题面跨量子临界点，可能给出 1D TFIM 精确临界线与其约定 |
| `10.21468/SciPostPhys.20.6.180` | B | *Bosonization and Kramers-Wannier dualities in general dimensions*（SciPost Phys.，全 OA，PDF 可直取） | KW 对偶以 1D TFIM 为原型，自对偶线或以 `K`、`Γ` 写法给出 |
| `10.1007/JHEP11(2017)157` | B | *An exactly solvable quench protocol for integrable spin models*（JHEP，全 OA） | 精确可解自旋模型协议，可能写出 TFIM 哈密顿量约定与临界判据 |
| `10.21468/SciPostPhys.11.1.013` | B | *Exact thermal properties of free-fermionic spin chains*（SciPost Phys.，全 OA） | 自由费米子链精确热性质，常需引用 TFIM 精确临界点 |
| `10.1088/1367-2630/15/4/043032` | B | *Quantum criticality at high temperature revealed by spin echo*（NJP，全 OA） | 备选 |
| `10.1088/1367-2630/18/1/015001` | B | *Long-range Ising and Kitaev models*（NJP，全 OA） | 长程 Ising 需与短程精确解对照，备选 |

> 队列来源仅为**元数据检索结果**（DOAJ 17:32:58），**0 抓取正文、0 判读、0 预判其 `r` 值**。

---

## §9 纪律与铁律留痕

| 纪律 | 本棒执行 |
|---|---|
| `K-GR1-0-A` 逐源四件套 | 4 源逐项核对（缺项如实标 ❌），**0 凑齐、0 补引文** |
| `K-GR1-0-B` 摘要反推禁令 | **0 反推**；5 次 arXiv 摘要检索**仅用于定位候选**，摘要内容**未作任何因子证据** |
| `K-GR1-0-C` 0 命中登记 | 面 A/C/D 及面 B 全文层 0 命中**逐条登记**（端点 + 检索式 + 时刻 + 返回条数）；面 E **标未执行** |
| `K-GR1-0-D` 源数口径 | 按 DOI/arXiv 号级计源；**preprint 与期刊版、镜像计 1 源**（本棒 0 出现同一文献多载体重复计数） |
| `K-GR1-0-E` 既有件 0 触动 | 上游件全部只读/未写 |
| `K-GR1-0-F` 派生 JSON 不合并 | **0 新增 JSON**；逐源独立 md（见 §11） |
| `K-GR1-0-G` 纪律沿用 | **0 注册 / 0 登录 / 0 cookie / 0 API key**（OpenAlex 因需 key 而**放弃**，未申请、未使用）；**0 付费墙 / 0 越权下载**；**key 永不明文**（本棒全程 0 接触任何密钥） |
| `K-GR1-0-H` 端点纪律 | **0 调用任何 LLM 端点**；其余请求经 tun 代理、串行、间隔 ≥2.5 s |
| 阈值（§8） | `0.05 / 0.15 / 1.0` 等 **0 新设、0 擅调**；本棒**0 数值计算、0 重算 `h_c/J`** |
| 网络环境如实 | 全部经 `127.0.0.1:1018`；该出口 **TLS 中间人**致证书校验失败 ⇒ 校验**关闭**（仅公网只读取用）；**如实交代**，未据此放宽任何内容纪律 |

---

## §10 老实交代段

1. **A 级源 = 0**：`K`、`Γ` 的定义因子**至今未核**；`K-GR1-1`、`K-GR1-2` **均未触发**，本棒**0** 以任何方式暗示答案倾向。
2. **未获全文的检索面**：面 D 的开放讲义（Kari 讲义 PDF）**TLS 握手失败、正文 0 取得**；面 B 的 9 条 OA 期刊候选**全文 0 抓取**（预算触顶）。**0 声称**已读这些文献。
3. **面 E 未执行**（预算触顶前未及检索）⇒ 如实登记为**未执行**，**0 冒充 0 命中**。
4. **检索工具受限如实**：通用网页检索（DDG / Bing / Mojeek / scholar.archive.org）在该出口分别 SSL 失败 / 403 / 区域化无关结果；OpenAlex 现返回 429（需 API key，依铁律放弃）⇒ **发现面实际仅 arXiv 元数据 + DOAJ/Zenodo 元数据**，**全文层命中 0**。
5. **PDF 抽取质量**：S3 式 (2) 等处抽取残缺（下标/指数被吞）⇒ **0 引用残串、0 凭残串推断**；所有引用均为抽取可靠之式，抽取产生的连字/断词**保留原样未回改**。
6. **`Γ` 同名误挂已排除**：S4 全文 35 处 `Γ` **均为广义 Grüneisen 比**，**非**无量纲横场（依 §7.3 符号名 0 参与判定，0 因同名误挂）。
7. **DOI 未核**：四源书目 DOI 本棒**未查**，一律标「未核」，**0 编造** DOI/卷期页。
8. **未做的事**：0 联网 LLM 调用、0 重算 `h_c/J`、0 改判、0 改 `#12` 档位、0 修改预登记件任何字面、0 新增/修改 JSON、0 派工、0 代 verdict-keeper 裁支。
9. **计数类差异**：候选源 6、查询 20 均为**本棒实测口径**；与盘上其他计数口径的差异**归「V4 收尾整理」批量校正桶**，本棒**0 单独校正**（沿 PI 2026-09-27 口径）。
10. **succeeded ≠ 跑完**：本件以「MD 落盘 + 字节数 + SHA-12 实测」为准（见 §11）；**判定棒（verdict-keeper）与重算棒均未开始**。

---

## §11 产物清单（SHA-12 实测 · 小写）

| 件 | 路径 | SHA-12 | bytes |
|---|---|---|---|
| 执行件（本件） | `results/_v4_gamma_r1_exec_2026_09_28.md` | 见派工回报 | — |
| 逐源记录 S1 | `results/_v4_gamma_r1_sources_20260928_S1.md` | `3d6e997aa692` | 2,944 |
| 逐源记录 S2 | `results/_v4_gamma_r1_sources_20260928_S2.md` | `dcec110ca2e0` | 2,647 |
| 逐源记录 S3 | `results/_v4_gamma_r1_sources_20260928_S3.md` | `6b9761d710ca` | 2,554 |
| 逐源记录 S4 | `results/_v4_gamma_r1_sources_20260928_S4.md` | `16af6baf8463` | 3,050 |
| 面 D 0 命中登记 S5 | `results/_v4_gamma_r1_sources_20260928_S5_faceD.md` | `4f77d49756db` | 2,264 |

**输入件复核（本棒只读实测）**：预登记件 `results/_v4_gamma_r1_prereg_2026_09_28.md` ⇒ SHA-12 **`02c072833cca`**、32,186 B —— 与派工单所记**一致** ✅。

**过程留痕（非交付件，0 承诺为证据）**：`.scratch_gamma_r1/`（`fetch.py` 检索器 + `query_log.jsonl` 19 条机器台账 + `raw/` 原始响应与 PDF 抽取文本），供第三方复核逐次请求；**0 并入任何既有 JSON**。

---

**出证｜worker（本棒执行段）出件｜2026-09-28｜预登记输入 `02c072833cca`（生效即锁，0 改动）｜结论落支：`K-GR1-3`（分歧未决 / 输入不足）｜`STOP-0` 触顶（20/20）｜A 级源 = 0｜0 判定、0 改判、0 触动既有件**
