# arXiv:2609.09001 元数据级快照（取证时点 2026-10-20）

> **本件效力面（开篇即界）**
> - 本件＝**元数据级快照**（题名／作者／提交时点／版本史／字节面 ＋ 摘要文本）——依派工单之「**只元数据面＋摘要文本之快照件**」之口径。
> - **⛔ 0 截留 PDF 本体**：PDF 本体之截留属**外部资产入库之裁**，该裁**未下**；本棒仅取 PDF 之**元数据面**（存在性／HTTP 状态／arXiv 自标体量），**未 GET PDF 字节**。
> - **⛔ 0 截留 TeX 源包本体**（`/src/2609.09001` 之字节）、**⛔ 0 截留 HTML 版全文**（`/html/2609.09001v1` 之字节）——二者之 URL 仅作**存在性之索引登记**。
> - **本快照不充当 GLM 认可面**（PI 2026-10-18 卡答 Other 栏逐字「**GLM 只认 Github**」）——本地面之一切读数 **⛔ 0 产认可效力**。
> - **⛔ 0 充全文之证**（⛔ 0 充论文内容之任何判读依据）·**⛔ 0 落五终判**·**⛔ 0 闭 `KD-H3`**·**⛔ 0 宣告段毕**·**⛔ 0 代 PI 裁**。

---

## §1 取证面登记（来源／方法／观测时点）

| # | 来源 URL | 方法 | 观测时点（本地 +08:00） | 结果 |
| :-: | :-- | :-: | :-- | :-- |
| S1 | `http://export.arxiv.org/api/query?id_list=2609.09001` | GET | 服务器侧 `<updated>`＝**2026-10-20T05:15:43Z**（＝本地 13:15:43） | ✅ Atom XML 取得（`totalResults`＝1） |
| S2 | `http://export.arxiv.org/api/query?id_list=2609.09001v1&max_results=1` | GET | 服务器侧 `<updated>`＝**2026-10-20T05:16:35Z**（＝本地 13:16:35） | ✅ Atom XML 取得（`totalResults`＝1） |
| S3 | `https://export.arxiv.org/abs/2609.09001` | GET | 与 S2 同轮（≈本地 13:16:35 之后·至 S5 轮之前）·**逐秒本地时戳未单独留存** | ✅ 摘要页全文（HTML）取得 |
| S4 | `http://export.arxiv.org/pdf/2609.09001` | **HEAD** | 与 S3 同轮（≈本地 13:16:35 之后） | ✅ **HTTP 200**（存在性证实） |
| S5 | `https://export.arxiv.org/pdf/2609.09001`／`https://arxiv.org/pdf/2609.09001v1`／`http://export.arxiv.org/pdf/2609.09001v1` | **HEAD** ×3 | 紧随 S3–S4 轮（≈本地 13:17:0x–13:18:0x 窗口） | ✅ **HTTP 200** ×3（仅状态码·**未暴露 `Content-Length`**） |

### §1-1 取件失败面（如实登记·⛔ 0 隐去）

| 尝试 | 方法 | 结果 | 本棒处置 |
| :-- | :-: | :-- | :-- |
| `https://arxiv.org/abs/2609.09001` | GET ×2 | ❌ `web_fetch network request failed` | 改由 S3（`export.arxiv.org` 之同内容镜像出口）取得·**未采信任何失败回退值** |
| `https://arxiv.org/pdf/2609.09001` | HEAD ×2 | ❌ 同上 | 改由 S4／S5 取得 |
| `http://arxiv.org/abs/2609.09001` | GET | ⚠ 返回 **MIWIFI 路由器诊断页**（`xiaqiang/web/css/bc.css` 之网关拦截页·非 arXiv 内容） | **⛔ 0 采信**·⛔ 0 视为取证失败之证据·⛔ 0 视为 arXiv 之应答 |

> 📌 **仪器面之诚实交代**：本棒之联网**出口**受本机网关影响（`arxiv.org` 主站直连失败／明文 `http` 触发网关拦截页）⇒ **同一内容由 `export.arxiv.org` 之出口取得**；两出口所载**同一 arXiv 记录**（题名／作者／时点／分类互校全等），故 S3 与 S1/S2 之内容**互为印证**。

---

## §2 元数据面（逐字登记）

### §2-1 题名

> Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths

- 摘要页 `<title>`：`[2609.09001] Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths`
- `og:title`／`citation_title`／`dc:title`／API `<title>`／摘要页 `<h1 class="title">` —— **五处逐字一致**（前缀除外）。

### §2-2 作者

| 项 | 逐字 |
| :-- | :-- |
| 作者 | **Qihao Yuan** |
| 摘要页作者块 | `Authors: Qihao Yuan`（链接 `arxiv.org/search/cs?searchtype=author&query=Yuan,+Q`） |
| `citation_author` | `Yuan, Qihao` |
| API `<author><name>` | `Qihao Yuan` |
| 投稿人（Submission history） | `From: Qihao Yuan` |
| 自称单位（`Comments` 内） | `School of Chemistry and Life Resources, 〔高校R〕 University of China` |

> 📌 **作者数 ＝ 1**（摘要页作者块仅 1 条·API `<author>` 仅 1 条 ⇒ 两面一致·**⛔ 0 外推**为「完整作者贡献面」）。

### §2-3 提交时点（两面互校）

| 面 | 逐字 |
| :-- | :-- |
| 摘要页 dateline | `[Submitted on 8 Sep 2026]` |
| 摘要页 Submission history | `[v1] Tue, 8 Sep 2026 16:40:31 UTC (1,598 KB)` |
| API `<published>` | `2026-09-08T16:40:31Z` |
| API `<updated>` | `2026-09-08T16:40:31Z` |
| `citation_date` | `2026/09/08` |
| `citation_online_date` | `2026/09/08` |

> 📌 **`published` ＝ `updated` ＝ `2026-09-08T16:40:31Z`** ⇒ 与「**仅 v1**」互证（**⛔ 0 存在后续版**）。

### §2-4 版本史（**全史仅 1 版**）

```
Submission history
From: Qihao Yuan
    [v1]  Tue, 8 Sep 2026 16:40:31 UTC (1,598 KB)
```

| 版本 | 提交时点（UTC） | 体量（arXiv 自标） | API 之 entry id |
| :-: | :-- | :-- | :-- |
| **v1** | **2026-09-08 16:40:31** | **1,598 KB** | `http://arxiv.org/abs/2609.09001v1` |

- 摘要页「Cite as」：`arXiv:2609.09001` [cs.AI]；本版本作 `arXiv:2609.09001v1` [cs.AI]。
- API 查询 `id_list=2609.09001v1` 之 `totalResults` ＝ **1** ⇒ **v1 之存在性**两面互证。
- **⛔ 0 存在 v2 及以后**（Submission history 仅列 v1·API `<updated>` ＝ `<published>`）。
- 📌 **本快照只反映 2026-10-20 观测时点之状态**——外部可变（⛔ 0 充「此后永无新版」之证）。

### §2-5 分类／主题

| 项 | 逐字 |
| :-- | :-- |
| 主分类（`primary-subject`／`arxiv:primary_category`） | **Artificial Intelligence (cs.AI)** |
| 次分类 | **Machine Learning (cs.LG)** |
| API `<category>` 集合 | `cs.AI`（primary）＋ `cs.LG` |

### §2-6 其他元数据

| 项 | 逐字 |
| :-- | :-- |
| `Comments` | `23 pages, 5 figures. Author affiliation: School of Chemistry and Life Resources, 〔高校R〕 University of China. Code: https://github.com/zeroandcat/Deposon` |
| DOI | `https://doi.org/10.48550/arXiv.2609.09001`（arXiv-issued DOI via DataCite） |
| `citation_arxiv_id` | `2609.09001` |
| 许可 | `http://creativecommons.org/licenses/by/4.0/`（**CC BY 4.0**·摘要页 `abs-license` 之图标与链接） |
| canonical | `https://arxiv.org/abs/2609.09001` |
| `og:url` | `https://arxiv.org/abs/2609.09001v1` |
| Full-text links（**仅索引登记·⛔ 0 取其字节**） | `/pdf/2609.09001`｜`https://arxiv.org/html/2609.09001v1`（HTML (experimental)）｜`/src/2609.09001`（TeX Source） |
| `citation_pdf_url` | `https://arxiv.org/pdf/2609.09001` |
| 摘要页 `description` | `Abstract page for arXiv paper 2609.09001: Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths` |

---

## §3 字节面（PDF 之体量衡）

| 项 | 读数 | 取法 | 精度面 |
| :-- | :-- | :-- | :-- |
| PDF 之**存在性** | **HTTP 200**（S4·S5 ×4 次，全部 200） | HEAD（**⛔ 0 GET 字节**） | 确证 |
| PDF 之**体量（arXiv 自标）** | **1,598 KB** | 摘要页 Submission history 行内标注 | **四舍五入至 KB·非精确字节数** |
| PDF 之**精确 `Content-Length`** | **未取得** | 本棒所用抓取工具之 HEAD **仅返状态行「HTTP 200」·未暴露 `Content-Length` 头** | ⛔ 0 以估算充实测 |
| `Content-Type` 头 | **未取得** | 同上（工具未暴露响应头全集） | ⛔ 0 断言 |
| `ETag`／`Last-Modified` 头 | **未取得** | 同上 | ⛔ 0 断言 |

> 📌 **折算说明（如实登记·⛔ 0 断言精确字节）**：arXiv 自标「1,598 KB」若按 **1024 B/KB** 折算 ≈ **1,636,352 B**；若按 **1000 B/KB** 折算 ≈ **1,598,000 B** ⇒ 二者**相差 38,352 B** ⇒ 本件**仅登记「1,598 KB（arXiv 自标·四舍五入）」**，**⛔ 0 充精确字节数**。
> 📌 **⛔ 0 截留 PDF 本体之理由（依派工单口径）**：PDF 本体之截留属**外部资产入库之裁**（第三方资产之著作权／入库政策），该裁**未下** ⇒ 本棒仅取**元数据面**；**是否以体量为由截留 PDF 本体 之裁**归 PI。

---

## §4 摘要文本（快照·逐字）

> **逐字来源**：API Atom XML 之 `<summary>`（`https://export.arxiv.org/api/query?id_list=2609.09001`·观测时点 2026-10-20T05:15:43Z）。
> **等价性说明**：摘要页 `<blockquote class="abstract">` 之 HTML 转义形（`&#34;`＝`"`、`&#39;`＝`'`、`&gt;`＝`>`）与本节文本**内容等价**，仅转义层不同。

```
Multi-step LLM reasoning lacks a machine-recheckable ledger: discarded reasoning paths leave no auditable record. We propose the Deposon scattering layer, which binds each node of an LLM-generated concept-decomposition graph to a two-parameter Deposon state; paths undergo three-channel scattering -- transmission, reflection, irreversible dissipation -- obeying T+R+A=1 for arbitrary parameters, with a maximum per-path energy-audit deviation of 2.2E-16 (machine epsilon). We report all three evidence tiers honestly. On synthetic trap benchmarks the path-filtering gain is closed (pre-registered): unified reaches 100% versus a decoy-capture baseline at 7%/10%. On real benchmarks the layer is indistinguishable from a trivial six-keyword rule filter (GSM8K 0.87 >= 0.85, McNemar p=0.5; StrategyQA 0.899 = 0.899); no difference is detected here, so we sharpen the claim to "the differential value lies solely in machine verifiability." Fusion yields a second negative result: convex combinations with a semantic prior never improve (physics 0.484 -> 0.452), and the apparent lambda=2 gain is an anti-field artifact; any fusion gain must be nonlinear. Modeling the reverse dynamics as a potential game on the graph, we evidence an auditable scalar's monotonicity and near-gradientness and quantify the empirical coordination ratio (ECR). The three formalized dynamical-equivalence propositions (P1a/P1b/T-P1c) are falsified under the pre-registered kill protocol, and the potential-game claim is downgraded to approximate (cyclic-graph median residual 0.669): only consistency-level evidence survives at the dynamical level. Code: github.com/zeroandcat/Deposon.
```

> 📌 **本段之射程**：**摘要文本之快照**——⛔ 0 充全文之证·⛔ 0 充论文内部任一实验／数据／图表之核（⛔ 0 读 PDF·⛔ 0 读 HTML 全文·⛔ 0 读 TeX 源包）·⛔ 0 对摘要所载**任何数值**（如 `2.2E-16`／`0.87`／`0.899`／`0.484`／`0.669`）作任何之复算或判读（**⛔ 0 跑实验**）。
> 📌 **摘要所载之 GitHub 地址**（`github.com/zeroandcat/Deposon`）系**第三方元数据所载之字符串**——本棒 **⛔ 0 访问该 URL**、**⛔ 0 核其存在性**（超出本面射程）。

---

## §5 与在册面之对账（**照录层·非本棒之核**）

| # | 在册锚 | 载文 | 本棒观测 | 判读 |
| :-: | :-- | :-- | :-- | :-- |
| A1 | 处置草案 §3-2 之 **A3**（照录自 `review_content_A2_kimik3.md`） | `arXiv:2609.09001` 之盘上**最早出现** ＝ 2026-09-18 09:28；全域命中 68 件；`README.md` 载 arXiv 链接、DOI `10.48550/arXiv.2609.09001`、作者 Qihao Yuan、cs.AI、23 页 5 图 | 本棒**独立实测**：DOI・作者・cs.AI・23 页 5 图（`Comments` 内）**与在册载文逐字相合** | ✅ **相合**（本棒 0 复核「最早出现」之全史·⛔ 0 外推） |
| A2 | 处置草案 §3-2 之 **A4**（照录） | 「arXiv 投稿动作『**0 件直接回执**』；『🔴 最高风险：编号本身有 68 件交叉引用，但『谁在何时投稿』**无一手凭证**』」 | 本棒所取**为第三方公开索引面之元数据**——**非**投稿回执（⛔ 0 含投稿凭证·⛔ 0 含提交确认） | ⚠ **该风险面未被本件消解**（见 §6 开口登记） |
| A3 | 处置草案 §7-1 之 **A7**（照录 PI 逐字） | 「GLM 只认 Github」 | 本件**照录该注记**（§0 开篇） | ✅ 注记在位 |

---

## §6 开口登记（**⛔ 0 闭·⛔ 0 落终判**）

1. 🔴 **「谁在何时投稿」之回执面仍开口**：本件所证者＝**arXiv 公开索引面之元数据**（题名／作者／提交时点／版本史／体量），**非**投稿动作之一手回执（**⛔ 0 含**「投稿成功」之凭证面·⛔ 0 含任何回执编号）⇒ 处置草案 §3-2 之 **A4** 风险面**未被本件消解**，**仍 🔴 开口**。
2. 🟡 **PDF 精确字节面未取得**（工具 HEAD 未暴露 `Content-Length`）⇒ **⛔ 0 断言精确字节数**（仅登记 arXiv 自标 `1,598 KB`）。
3. 🟡 **「元数据级快照」≠「内容级证据」**：本件 ⛔ 0 充全文之证・⛔ 0 充论文结论之任何支撑。
4. 📌 **外部可变**：本件仅反映 2026-10-20 观测时点之 arXiv 面；**⛔ 0 充「此后状态不变」之证**。
5. 📌 **本件 0 闭 `KD-H3`**・**0 落五终判**（`pass`／`af`／`kd`／`fail`／`give-up` 之任一）・**0 宣告段毕**・**0 代 PI 裁**（外部资产入库之裁归 PI）。

---

## §7 落盘自证（口径）

- **落盘路径**：`results/_arxiv_2609_09001_metadata_snapshot_2026_10_20.md`（仓根相对路径）。
- **编码／行尾**：**UTF-8 无 BOM** ＋ **纯 LF**（落盘后回读实测）。
- **本件自身之 SHA-12 与字节数**：**见派工回执**（本件⛔ 0 自含其自身指纹——自含将改其字节）。
- **回读检验**：落盘后由本棒**独立重读**（重算哈希、查 BOM、查 CR 字节）⇒ 结论与字节数一并报回。
- **本棒对既有件之触动数 ＝ 0**（依：results 目录 1,333 件既有件之清单哈希 改动前后全等；16 冻结锚之仓内侧 8 件 改动前后全等）——**数字与比对式见回执**。
