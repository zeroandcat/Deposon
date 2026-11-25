# `L-4` 之 `U-3`／`U-4`／`U-9` ＋ `L-5` 项① 之**联网补件**（证据链面·只补证据·⛔0 落五终判）｜2026-10-27

> 📌 **件性质**：**补件**（`worker`·无名执行棒之补位——⛔0 顶替起草／判定／口径诸官）——为 `L-4`（`Z-4`）与 `L-5`（`Z-4`）**补足须联网面之证据**，**只补证据**。
> ⛔ **0** 落五终判（`pass`／`af`／`kd`／`fail`／`give-up` 之任一断言）｜⛔ **0** 代 PI 裁／释／择／给值｜⛔ **0** 代销记｜⛔ **0** 宣告 ①段毕·任何要件之零·任何门槛成就｜⛔ **0** 回改／移动／重命名／删除任何既有件（**既有件触动数 ＝ 0**）｜⛔ **0** 写远端（GitHub／arXiv 皆**匿名只读** GET）｜⛔ **0** 读 `〔本地路径已脱敏〕` 正文｜⛔ **0** 读归档区正文｜⛔ **0** 造新词·0 编造文献号。
> 📌 **本棒观测时点**：2026-10-27 **19:10 – 19:26**（GMT+8）｜**联网取用时刻**：GitHub 面 **19:14:02–19:24**（六轮）；arXiv 面 **19:14:17–19:22:47**（两轮）。
> 📌 **仪器**：①字节核 `_bcheck.py`（`python -P`）②GitHub REST API v3（匿名只读）③arXiv HTTP 匿名 GET（`/abs/`、`/pdf/`、`/e-print/`、`export.arxiv.org/api`）④Git blob sha1 独立复算（`sha1("blob %d\0" + content)`，本地自算）。
> 📌 **本件不载自身指纹**（自指回环之规避）——落盘后之 bytes／SHA-12 于件外回报；**落盘后之 `_bcheck.py` 五项读数载于 §9**（写入后复跑所得）。

---

## §0 · 一句话结论（先给判）

| 项 | **状态** | **一句话据** |
|:--|:--|:--|
| **`U-3`** | ✅ **FOUND**（附据） | 远端 `zeroandcat/Deposon` @ `main` 之**当前 HEAD ＝ `06045bceff07908aa38b8b5d3e626731b7326e7d`**（2026-10-23T07:17:11Z），**≠ 登记时点值 `f44996fb…`**；登记时点 commit **仍可达**（HTTP 200）且为当前 HEAD 之**祖先**（`compare` ＝ `ahead`／ahead_by **490**／behind_by **0**／merge_base ＝ `f44996fb…`）⇒ **登记时点值已非 HEAD，但可达**。 |
| **`U-4`** | ✅ **FOUND**（附据） | 远端全量件数**已核**（`truncated=False`·完整树）：**当前 HEAD ＝ 3,438 blobs**（185,403,899 B）／**登记时点 ＝ 3,063 blobs**（109,121,770 B）；**全量分区（按顶层目录·blob 件数）** 当前 ＝ `_repo_mirror` 3,003／`results` 106／`verifier` 78／根文件 68／`docs` 59／`reviews` 33／`letters` 28／`corpus` 24／`tests` 22／`paper` 12／`deposon_team` 2／`tools` 2／`.trae` 1；登记时点 ＝ `_september_workspace` **2,653**／`results` 107／…⇒ **461 确系差异件清单，非全量**。 |
| **`U-9`** | ✅ **FOUND**（附据）＋ **PI 终核面未解** | arXiv `2609.09001` **实读**（`/abs/` ＋ `/pdf/` ＋ `/e-print/` 源包 三面皆 200）：**Comments 栏载作者单位**＝「`School of Chemistry and Life Resources, 〔高校R〕 University of China`」**66 字符**·`sha256[:12]＝eccdb0565be7`——**与在册 `M-07` 登记之串指纹 `eccdb0565be7`／66 字符逐位相符**；同字面于 e-print 源包 `deposon_paper_en.tex` 内独立复现 ⇒ **「单位字面之来源」已实取**；**照录与否之终核仍归 PI**（本棒⛔0 代裁）。 |
| **`L-5` 项① 远端侧** | ✅ **FOUND**（附据） | 461 明细表之**远端侧实体**已逐件核：登记时点树 `f44996fb…` 之**路径命中 461/461**、**远端 blob sha1（40 位全值）逐位相符 461/461**、**bytes 逐位相符 461/461**；抽样 12 件经 `raw.githubusercontent.com` **取字节独立复算 git blob sha1 ＝ 12/12 相符** ⇒ **「某特定件在远端」之断言在登记时点已具凭**（在册「远端侧不可核」之缺已解）。 |

⚠ **本件之四项状态皆为「证据面已具凭」，⛔0 落五终判**；`U-9` 之照录与否、`U-5`／`U-6`／`U-7`／`U-10`、`U-2` 之择一、`L-5` 项③之调和与项④之成因——**皆不在本棒**（见 §8）。

---

## §1 · 输入件之指纹自测（**本棒实测·非转引**）

| # | 件（相对 `〔本地路径已脱敏〕`） | 题给 bytes／SHA-12 | **本棒实测 bytes／SHA-12** | 核 |
|:-:|:--|:--|:--|:-:|
| 1 | `results\verdict\judgement\_f04_l4_l5_item1_supplement_2026_10_27.md` | 36,946／`ce2508044c2c` | **36,946／`ce2508044c2c`** | ✅ 逐位相符 |
| 2 | `results\_book_03_achievements_inventory_full_2026_10_22.md` | 1,181,645／`ba8a1e0ebce8` | **1,181,645／`ba8a1e0ebce8`** | ✅ 逐位相符 |
| 3 | `_HANDOVER_MUST_READ.md`（仓根） | 29,809／`d3513a125be5` | **29,809／`d3513a125be5`** | ✅ 逐位相符 |
| 4 | `results\work\process\_zero_blockers_list_2026_10_26.md` | 41,376／`8edfcdce2b62` | **41,376／`8edfcdce2b62`** | ✅ 逐位相符 |
| 5 | `results\verdict\judgement\_l5_four_open_items_verification_2026_10_27.md` | 32,097／`db30cf540d52` | **32,097／`db30cf540d52`** | ✅ 逐位相符 |
| 6 | `results\_book_07_upload_side_desensitized_remote_sha_letter_kimi_2026_10_22.md` | 89,791／`a13ec23c4b3b` | **89,791／`a13ec23c4b3b`** | ✅ 逐位相符（⚠ `CR＝477`·**本棒 0 改**） |
| 7 | `letters\_commission_glm_dualtrack_paper_v0.6_2026_10_12.md` | 56,360／`6d1b14983555` | **56,360／`6d1b14983555`** | ✅ 逐位相符 |
| 8 | `letters\_commission_glm_dualtrack_paper_v0.7_2026_10_18.md` | 70,048／`07e068165dd5` | **70,048／`07e068165dd5`** | ✅ 逐位相符 |

> 📌 **8/8 逐位相符**（`python -P 〔幽灵引用·未上传:_bcheck.py〕` 逐件跑）｜**本棒所引他件之指纹皆自测**。

### §1-1 · 本棒所引他件之指纹（**凡引必自测**）

| 简写 | 件 | bytes／SHA-12（本棒自测） | 用途 |
|:--|:--|:--|:--|
| `_l4r` | `results\verdict\judgement\_l4_u1_u10_independent_carrier_recheck_2026_10_27.md` | **32,527／`9ab5f787e96c`** | `U-3`／`U-4`／`U-9` 之现态与所缺（§2-3／§2-4／§2-9） |
| `_l5v` | `results\verdict\judgement\_l5_four_open_items_verification_2026_10_27.md` | **32,097／`db30cf540d52`** | `L-5` 项①之本地侧与其远端侧之缺（§2-1） |
| `_v06` | `letters\_commission_glm_dualtrack_paper_v0.6_2026_10_12.md` | **56,360／`6d1b14983555`** | `U-3`／`U-4`／`U-9` 之**首次登记处**（§8 表 L371／L372／L377） |
| `_v07` | `letters\_commission_glm_dualtrack_paper_v0.7_2026_10_18.md` | **70,048／`07e068165dd5`** | `U-3`／`U-4`／`U-9` 之**最新登记处**（§8 表 L469／L470／L475） |
| `_book07` | `results\_book_07_upload_side_desensitized_remote_sha_letter_kimi_2026_10_22.md` | **89,791／`a13ec23c4b3b`** | 461 明细表之实体（册内 L37–L39 登记头 ＋ L43–L505 明细） |
| `_cb05` | `letters\_dualtrack_paper_clue_book_v0.5_2026_10_01.md` | **（本棒未全篇开卷·所引行字面经 grep 逐行实取）** | 「单位字面」之定义面（**转引·该件自身指纹未复测**） |
| `_v07p` | `pi_rulings\_pi_card_answers_register_2026_10_14_v7.md` | **（本棒未全篇开卷·所引行字面经 grep 逐行实取）** | `M-07` 之串指纹登记（**转引·该件自身指纹未复测**） |
| `_v188` | `pi_rulings\_pi_card_answers_register_2026_10_21_v188.md` | **（本棒未全篇开卷·所引行字面经 grep 逐行实取）** | PI「arXiv 预印本单位已释」之登记（**转引·该件自身指纹未复测**） |
| `_v234` | `pi_rulings\_pi_card_answers_register_2026_10_22_v234.md` | **（本棒未全篇开卷·所引行字面经 grep 逐行实取）** | 在册之远端全量读数（**转引·该件自身指纹未复测**） |

---

## §2 · **逐项回源**：四项之确切命题（**件名＋行号＋逐字**）

> 📌 **依铁律 3「引用不回源」**：本棒**逐项开卷**原始登记处取逐字命题，⛔0 以派工单之转述为准。

### §2-1 · `U-3`（远端 HEAD 之当前可达性）

- **首次登记**：`letters\_commission_glm_dualtrack_paper_v0.6_2026_10_12.md` **§8 表 L371** 逐字：「**远端 HEAD 之当前可达性**」｜状态「**未核得（本棒 0 联网 0 远端读）**」｜依据「`f44996fb…` ＝ **登记时点**值；⛔ 0 断言其当前仍为 HEAD」。
- **最新登记**：`_v07` **§8 表 L469** 逐字：「**远端 HEAD 之当前可达性**」｜状态「**未核得（本件 0 联网）**」｜依据「`f44996fb…` ＝ **登记时点**值（转引 v0.6 §3.1）；⛔ 0 断言其当前仍为 HEAD」。
- **独立复核件所述之缺**（`_l4r` **§2-3 L67–L71**）：所缺者＝「**远端仓库当前状态**」；且明书「**登记值本身可核**；**『当前是否仍为 HEAD』不可核**」。
- 📌 **本棒所查之确切命题**（**分两面**）：①**登记时点值 `f44996fb…` 当前是否仍为 `main` 之 HEAD**；②**该 commit 当前是否仍可达**（可达性之两面皆须给，不得混为一读）。

### §2-2 · `U-4`（远端全量件数与全量分区）

- **首次登记**：`_v06` **§8 表 L372** 逐字：「**远端全量件数与全量分区**」｜状态「**未核得**」｜依据「回函仅登记 **461 件**；自记『未列之件远端字节与本地原件相同』⇒ **0 断言全量**」。
- **最新登记**：`_v07` **§8 表 L470** 逐字：「**远端全量件数与全量分区**」｜状态「**未核得**」｜依据「回执仅登记 **461 件**；自记『未列之件远端字节与本地原件相同』⇒ **0 断言全量**」。
- **独立复核件所述之缺**（`_l4r` **§2-4 L73–L78**）：461 明细表实体在盘（`_book07`）且逐行索引 1–461 连续；然「**远端全量件数**仍 0 断言」；⚠「**⛔0 以『461 表逐行完整』充『远端全量已核』**」。
- 📌 **本棒所查之确切命题**：**远端 `main` 之 blob 全量件数** ＋ **其全量分区**（按顶层目录之 blob 件数分布）——**并须给 `truncated` 标志**（判定此读数是否覆盖全树）。

### §2-3 · `U-9`（arXiv 预印件之单位字面照录）

- **首次登记**：`_v06` **§8 表 L377** 逐字：「**arXiv 预印件之单位字面照录**」｜状态「**待 PI 终核**」｜依据「沿 v0.5 §1.1；**默认 0 照录**」。
- **最新登记**：`_v07` **§8 表 L475** 逐字：「arXiv 预印件之**单位字面照录**」｜状态「**待 PI 终核**」｜依据「沿 v0.5 §1.1；**默认 0 照录**；回函 `G-30` 载『未办』」。
- **独立复核件所述之缺**（`_l4r` **§2-9 L109–L113**）：「**『照录与否』及单位字面之来源须实读预印本**（PDF／源包 `47ccbbba1c47`／`8fa073e35fe0` 之实体 **0 在我方盘**）＋ **PI 终核** ⇒ **未立**」。
- 📌 **本棒所查之确切命题**：**单位字面之来源**——即「**预印本页面 Comments 栏所载作者单位**」之**逐字原文**（`letters\_dualtrack_paper_clue_book_v0.5_2026_10_01.md` **L45** 逐字之定义：「① **单位字面**（**页面 Comments 栏载有作者单位**）——**涉可识别信息，是否照录由 PI 按 H-I 隐私面定** ⇒ **默认 0 照录**」）＋ 其**可核指纹** ＋ **是否照录之终核**（**归 PI**）。
- 📌 **在册已存之指纹**：`pi_rulings\_pi_card_answers_register_2026_10_14_v7.md` **L21／L48** 逐字（**本棒经 grep 逐行实取该行字面·未全篇开卷·该件自身指纹未复测**）：「**单位字面串指纹 `eccdb0565be7`／66 字符**」；同件 **L36** 逐字：「🔴 H8 门控：字面实取成功，然 H8 载『以 PI 的 github 为唯一权威源』而 **README 0 载** ⇒ 公开面与权威源 0 重合」；**L38** 逐字：「**项25 采信**（字面可引用 · ⚠ 与 H8 门控冲突，**本选即 PI 明示豁免**——M-07 单位字面自此可照录／引用，串指纹 `eccdb0565be7`／66 字符）」。
- 📌 **PI 已释之登记**：`pi_rulings\_pi_card_answers_register_2026_10_21_v188.md` **L22** 逐字（**本棒经 grep 逐行实取该行字面·未全篇开卷·该件自身指纹未复测**）：「**arXiv 预印本单位已释**：G-30-b／H-6 之面＝**PI 已释**——⚠ **界分**：其释之内容面（单位字面之释之内容／照录与否（H8 之面）之裁之内容）**0 载于本令**（PI 未随令其字面——⛔0 自拟——**其字面之面之候裁/候补面存续**）」。
  ⇒ ⚠ **本棒据此之界**：PI「已释」**未随字面** ⇒ **照录与否之终核仍候 PI**（本棒⛔0 补字面·⛔0 代裁）。

### §2-4 · `L-5` 项①（461 件明细）之**远端侧**

- **首次登记**：`_v06` **§9.6 第 2 项 L414** 逐字：「**远端 461 件之逐件明细未逐行实读**｜本棒仅实读头部 130 行 ＋ 前缀统计 ＋ 尾部 20 行 ⇒ **0 断言某特定件在远端**，仅可依 §3.4 之类级判断」。
- **独立复核件所述之缺**（`_l5v` **§2-1 L31–L56**）：本地侧已具凭（明细表在盘、索引 1–461 连续）；然「⛔ **0 断言『某特定件在远端』**——远端 blob sha1 之**远端侧实体**（`zeroandcat/Deposon` @ `main`）**⛔0 联网** ⇒ **不可核**」。
- **登记件自身之登记头**（`_book07` 册内 **L37–L39**，**本棒逐字回读**）：
  - **L37**：「- 远端仓库：`zeroandcat/Deposon` @ `main`，登记时点 HEAD：`f44996fbfd9f386299442924f70585bb20d935fc`」
  - **L38**：「- 登记件数：**461** 件（全部经三方核验：远端 blob sha1 == 下表值，逐件实测于本函生成时刻，漂移 0 件）」
  - **L39**：「- 远端 SHA 口径：GitHub git blob sha1（40 位全值）；bytes 为远端字节数」
- 📌 **本棒所查之确切命题**：**461 件之每一件**（远端路径／远端 bytes／远端 blob sha1）在**登记时点远端**（`f44996fb…` 之树）是否**逐位相符**；**且**在**当前远端**（`main` 之树）是否仍存。

---

## §3 · 联网取证之**方法·射程·正控·阴性对照**（**方法学自明**）

### §3-1 · 检索式与端点（**逐条可复现**）

| 面 | 检索式（**逐字 URL**） | 取用时刻 |
|:--|:--|:--|
| 远端仓主体 | `GET https://api.github.com/repos/zeroandcat/Deposon` | 2026-10-27T19:14:02+0800 |
| 当前 HEAD | `GET https://api.github.com/repos/zeroandcat/Deposon/commits/main` | 19:14:03 |
| 登记时点 commit | `GET https://api.github.com/repos/zeroandcat/Deposon/commits/f44996fbfd9f386299442924f70585bb20d935fc` | 19:14:04 |
| 当前全树 | `GET https://api.github.com/repos/zeroandcat/Deposon/git/trees/main?recursive=1` | 19:14:07 |
| 登记时点全树 | `GET https://api.github.com/repos/zeroandcat/Deposon/git/trees/f44996fbfd9f386299442924f70585bb20d935fc?recursive=1` | 19:14:08 |
| 祖先关系 | `GET https://api.github.com/repos/zeroandcat/Deposon/compare/f44996fbfd9f386299442924f70585bb20d935fc...06045bceff07908aa38b8b5d3e626731b7326e7d` | 19:18:41 |
| 10-18 锚树 | `GET https://api.github.com/repos/zeroandcat/Deposon/git/trees/739a7daf533b6ead320667d924ab0884c9614edc?recursive=1` | 19:22（probe4） |
| 10-18 晚刻锚树 | `GET …/git/trees/5f6dc0b7baf317eea3ab8f2a3b2f165f60fd0c2a?recursive=1` | 19:23（probe5） |
| 远端内容取字节 | `GET https://raw.githubusercontent.com/zeroandcat/Deposon/<ref>/<path>`（抽样 12 件） | 19:20（probe3） |
| arXiv 摘要面 | `GET https://arxiv.org/abs/2609.09001` | 19:14:17 |
| arXiv 元数据面 | `GET https://export.arxiv.org/api/query?id_list=2609.09001` | 19:14:18 |
| arXiv PDF 本体 | `GET https://arxiv.org/pdf/2609.09001` | 19:14:18 |
| arXiv 源包 | `GET https://arxiv.org/e-print/2609.09001`（302→`https://arxiv.org/src/2609.09001`） | 19:14:23 |
| arXiv 远端仓 README | `GET https://raw.githubusercontent.com/zeroandcat/Deposon/<ref>/README.md`（两 ref ＋ 本地） | 19:22 |

### §3-2 · **射程**（**阴性断言必带**）

| 射程面 | 值 |
|:--|:--|
| **远端全量（N_full）** | `git/trees?recursive=1` 之 `truncated` 标志 ＝ **`false`**（**两树皆然**）⇒ **该读数为全量，非抽样** |
| 当前树（`06045bce…`） | `n_entries` ＝ **3,573**｜`n_blobs` ＝ **3,438**｜`n_trees` ＝ **135**｜blob 字节和 ＝ **185,403,899 B** |
| 登记时点树（`f44996fb…`） | `n_entries` ＝ **3,242**｜`n_blobs` ＝ **3,063**｜`n_trees` ＝ **179**｜blob 字节和 ＝ **109,121,770 B** |
| 10-18 锚树（`739a7daf…`） | `n_entries` ＝ 3,653｜`n_blobs` ＝ 3,456｜`n_trees` ＝ 197｜blob 字节和 ＝ 125,867,780 B |
| 10-18 晚刻锚树（`5f6dc0b7…`） | `n_entries` ＝ 3,659｜`n_blobs` ＝ **3,462**｜`n_trees` ＝ 197｜blob 字节和 ＝ **126,187,988 B** |
| **arXiv 面** | `/abs/` ＋ `/pdf/` ＋ `/e-print/` ＋ `export.arxiv.org/api` 四端点 ＋ 复测一轮 ＝ **5 次独立 GET**（同一 paper id） |
| **未及之面** | ①GitHub **blob API 逐件核**（`/git/blobs/{sha}`）——**匿名限额 60/时已耗尽**（`GET /rate_limit` → `core: limit 60／remaining 0／used 60`）⇒ 12 件抽样**全部 403** ⇒ 记 **`OUT_OF_RANGE`**（**限额之限·非阴性**）；②arXiv **PDF 内文**之全文级解析——本棒⛔0 装 PDF 解析器 ⇒ **仅取 PDF 之字节与指纹**（`%PDF-1.7`）＋以 **e-print 源包 `.tex` 之正文**代其文面（见 §4-3 之口径说明） |

### §3-3 · **正控**（**测法之活**）

| 正控 | 实测 | 意义 |
|:--|:--|:--|
| GitHub 树之 blob sha1 ↔ raw 内容自算 | **12/12 相符**（`sha1("blob %d\0"+content)` ＝ 树内 sha1 ＝ 表内 40 位值） | 树之 sha1 口径 ＝ Git blob sha1 之说**得证**；且 `raw.githubusercontent` 取字节之路**活** |
| 树内已知路径（`README.md`／`LICENSE`）逐字节复算 | 2/2 相符（`d829f45b…`／`67a73a5e…`） | 「远端 blob sha1」之比较法**活** |
| arXiv 已知论文面 | `GET https://arxiv.org/abs/2205.14135` → **200**·44,575 B·`sha256[:12]=08fc19eeceb6`·页内含 `2205.14135` ＝ **true** | arXiv 检索通路**活**（非通配返回） |
| arXiv 重复取（复测轮） | `abs`／`pdf`／`e-print` **三面 sha256[:12] 与首轮逐位相同** | 取值**可复现** |
| GitHub 树重复取（复测轮） | 第二次 tree 之 body `sha256[:12]＝29e20ffa698d` ＝ 首次；**blob sha1 集合逐位相同**（diff ＝ **0**／3,438） | 远端全量读数**可复现** |
| 在册读数之复现 | `5f6dc0b7…` 树之 blob 件数 **3,462**／字节和 **126,187,988**／镜像 **3,048 件／121,917,049 B** ＝ 在册 v234 所载**四项逐位相符** | 本棒之计数**与在册读数同口径**（见 §4-2 之口径辨析） |

### §3-4 · **阴性对照**（**证明 0 命中非因工具失灵**）

| 靶 | 端点 | 实测 | 判读 |
|:--|:--|:--|:--|
| 不存在之 commit（40 位全 0） | `GET /repos/zeroandcat/Deposon/commits/0000…000` | **HTTP 422** | GitHub 对非法 sha 之响应**确为 422** ⇒ 本棒所记之 200/404 皆为真判读 |
| 不存在之路径 | `GET /repos/zeroandcat/Deposon/contents/__probe_nonexistent_l4l5_9x7__` | **HTTP 404** | 路径面之阴性**确为 404** |
| 不存在之 blob sha（合法格式） | `GET /repos/zeroandcat/Deposon/git/blobs/0123456789abcdef0123456789abcdef01234567` | **HTTP 403**（限额） | ⚠ **403 ≠ 404** ⇒ **不得**据此判「blob 不存在」；本棒据此**记 `OUT_OF_RANGE`** |
| arXiv 页之「不存在」面 | `abs` 页内探针 `No paper` ＝ **false**／`not recognized` ＝ **false** | 取回为**真论文页** | 排除「返回空壳页」之可能 |

---

## §4 · 逐项查证结果（**附据·附口径·附出处**）

### §4-1 · `U-3` · 远端 HEAD 之当前可达性 → ✅ **FOUND**

**结论（两面分列·⛔0 混读）**：

| 面 | 实测值 | 口径 | 出处 URL |
|:--|:--|:--|:--|
| **① 当前 HEAD** | **`06045bceff07908aa38b8b5d3e626731b7326e7d`**（tree `63a6659a0f97a0073ee2a98573bf2f70eeea28d2`） | GitHub `main` 分支当前 tip commit sha | `https://api.github.com/repos/zeroandcat/Deposon/commits/main` |
| **① 之时刻** | commit date **2026-10-23T07:17:11Z**；repo `pushed_at` ＝ **2026-10-23T07:17:12Z**；repo `updated_at` ＝ 2026-10-23T07:17:16Z；`default_branch` ＝ **`main`**；`size` ＝ 94,014（KB，GitHub 之 size 口径） | 同上 | 同上 ＋ `https://api.github.com/repos/zeroandcat/Deposon` |
| **② 登记时点值是否仍为 HEAD** | **否**——`06045bce…` ≠ `f44996fb…` | commit sha 全 40 位逐位比对 | 同上 |
| **③ 登记时点值是否仍可达** | **是**——`GET /commits/f44996fb…` → **HTTP 200**（633,407 B） | commit 对象在远端仍可取 | `https://api.github.com/repos/zeroandcat/Deposon/commits/f44996fbfd9f386299442924f70585bb20d935fc` |
| **④ 与当前 HEAD 之关系** | `compare` → `status` ＝ **`ahead`**｜`ahead_by` ＝ **490**｜`behind_by` ＝ **0**｜`total_commits` ＝ **490**｜`merge_base_commit.sha` ＝ **`f44996fb…`** | GitHub compare 之 base…head 口径（base ＝ 登记时点值·head ＝ 当前 HEAD） | `https://api.github.com/repos/zeroandcat/Deposon/compare/f44996fbfd9f386299442924f70585bb20d935fc...06045bceff07908aa38b8b5d3e626731b7326e7d` |
| **⑤ 自登记时点可达之 commit 数** | 逐页枚举（`GET /repos/…/commits?sha=<REG_HEAD>&per_page=100`）：页 1–4 各 **100** ＋ 页 5 ＝ **9** ⇒ 合计 **409** | 以 `sha=` 为起点之历史枚举（含起点本身） | 同上 `/commits?sha=f44996fb…&per_page=100` |
| **⑥ 当前 HEAD 之提交消息头** | 「mirror content-face narrowing 2026-10-23 (-166 files: workflow bookkeeping only -- verification/acceptance receipts, ledgers/indexes/manifests, progress/status, push/upload/mirror registers; per PI 2026-10-23 14:46 content-only criterion, per admin 14:59 commission; 7 eta-chain pending items untouched) · pure deletion, 0 force, 0 content edit · by bob」 | commit message 原文（前 120 字符） | 同 `commits/main` |

⇒ 📌 **`U-3` 之断言面已具凭**：**登记时点值 `f44996fb…` 已非 `main` 之 HEAD**（当前 HEAD ＝ `06045bce…`），**然该 commit 仍可达且为当前 HEAD 之祖先**（`ahead`／`behind_by 0`／`merge_base` ＝ 自身）⇒ **「0 断言其当前仍为 HEAD」之旧述，由本棒以联网实测证否；且「其已不可达」之读亦证否**。
⚠ **本棒⛔0 断言**：`U-3` 之「核得态」（已立／未立／不可得）之判定权**不在本棒**（`_l4r` §2-0 判准之闭权归 PI／`verdict-keeper`）；本棒只供**证据面**。
⚠ **口径之辨（AC-5 之守）**：上表 ⑤ 之 **409**（`commits?sha=` 起点枚举·含起点·含其全部祖先）**与** ④ 之 **490**（`compare` 之 `ahead_by`·自 base 至 head 之增量）**是两种不同口径之数**——本棒**⛔0 相减**（`409` 与 `490` 之集合非包含关系：`409` 含 base 之前之祖先，490 为其上之增量）。

### §4-2 · `U-4` · 远端全量件数与全量分区 → ✅ **FOUND**

**全量读数（两时点·`truncated=false` ⇒ 全量非抽样）**：

| 时点 | commit | blob 件数 | tree 目录数 | entries 合计 | blob 字节和 | `truncated` |
|:--|:--|--:|--:|--:|--:|:--|
| **当前 HEAD** | `06045bce…` | **3,438** | 135 | 3,573 | **185,403,899 B** | **false** |
| **登记时点** | `f44996fb…` | **3,063** | 179 | 3,242 | **109,121,770 B** | **false** |
| 10-18 锚 | `739a7daf…` | 3,456 | 197 | 3,653 | 125,867,780 B | false |
| 10-18 晚刻锚 | `5f6dc0b7…` | 3,462 | 197 | 3,659 | 126,187,988 B | false |

**全量分区（按顶层目录·blob 件数）**：

| 顶层 | 当前 HEAD（`06045bce…`） | 登记时点（`f44996fb…`） | 10-18 晚刻锚（`5f6dc0b7…`） |
|:--|--:|--:|--:|
| `_repo_mirror/` | **3,003** | 0 | **3,048** |
| `_september_workspace/` | **0** | **2,653** | 0 |
| `results/` | 106 | 107 | 106 |
| `verifier/` | 78 | 78 | 78 |
| （根文件） | 68 | 69 | 68 |
| `docs/` | 59 | 60 | 59 |
| `reviews/` | 33 | 33 | 33 |
| `letters/` | 28 | 2 | 7 |
| `corpus/` | 24 | 24 | 24 |
| `tests/` | 22 | 22 | 22 |
| `paper/` | 12 | 10 | 11 |
| `deposon_team/` | 2 | 2 | 2 |
| `tools/` | 2 | 2 | 2 |
| `.trae/` | 1 | 1 | 1 |
| **合计** | **3,438** | **3,063** | **3,462** |

**「461 ＝ 差异件清单而非全量」之正面证实**：登记时点树之 `_september_workspace/` 前缀含 **2,653** blobs，而 461 表之**全部 461 行路径皆以 `_september_workspace/` 为前缀**（本棒逐行解析实测：`table_path_prefix2_dist` 之 `_september_workspace/results` 353／`docs` 48／`deposon_team` 33／`tmp_movedout_2026_09_28` 6／`tmp_movedout_2026_10_09` 6／`verifier` 5／`.trae` 2／其余 8 单一路径各 1）⇒ **461 ⊂ 2,653（登记时点该前缀之 blob 全量）** ⇒ **461 ≢ 远端全量**，在册「0 断言全量」之缺口**已具据**。

**口径辨析（AC-5 之守·本棒之要）**：在册 `_v234` **L89** 逐字载（**本棒经 grep 逐行实取该行字面·未全篇开卷·该件自身指纹未复测**）：「全树 **3,462 件／126,187,988 B**，其中镜像区 `_repo_mirror/` 占 **3,048 件／121,917,049 B**，镜像区之外的可见仓只有 **414 件**（results 仅 106 件、tools 仅 2 件）」。本棒独立实测之 commit `5f6dc0b7…`（2026-10-18T15:01:14Z）之树：blob 件数 ＝ **3,462**｜blob 字节和 ＝ **126,187,988**｜`_repo_mirror/` ＝ **3,048 件／121,917,049 B**｜`results` ＝ 106｜`tools` ＝ 2 ⇒ **四项逐位相符**。
⇒ 📌 **在册 v234 之「全树 3,462 件」之口径 ＝ `git/trees?recursive=1` 之 blob 条目数**（非含 tree 目录之 entries 合计 3,659）——**本棒之当前读数「3,438 件」与之同口径**（同端点·同计数法）⇒ **可比**。
⚠ **但时点不同**（在册 v234 之 `pushed_at` ＝ 2026-10-18T15:02:52Z；本棒当前读数 ＝ 2026-10-23T07:17:12Z 之后）⇒ **两数之差 ＝ 远端在此期间之变更量**，**非「缺失量」**；本棒⛔0 将其充「差额·缺失」（《交接指南》§10-8 第 17 型之守）。
⚠ **本棒⛔0 断言**：远端全量之**当前**值为 **3,438 blobs**；**⛔0 断言**其为「我方应传之件数」或「缺失之件数」（其工程目标之定归 PI）。

### §4-3 · `U-9` · arXiv 预印件之单位字面照录 → ✅ **FOUND**（字面之来源已实取）＋ **终核面候 PI**

**① 预印本本体之实读（三面皆 200）**：

| 面 | URL | HTTP | bytes | `sha256[:12]` | 取用时刻 |
|:--|:--|:-:|--:|:--|:--|
| 摘要页 | `https://arxiv.org/abs/2609.09001` | **200** | **43,768** | `a60046e736ca` | 19:14:17 |
| 元数据 API | `https://export.arxiv.org/api/query?id_list=2609.09001` | **200** | **3,295** | `054350cd9108` | 19:14:18 |
| PDF 本体 | `https://arxiv.org/pdf/2609.09001` | **200** | **1,939,567** | `fcb2a7ad9158` | 19:14:18 |
| 源包（e-print） | `https://arxiv.org/e-print/2609.09001` → `https://arxiv.org/src/2609.09001` | **200** | **1,636,722** | `88e1258bd06a` | 19:14:23 |
| **复测轮**（三面再取） | 同上三 URL | **200** ×3 | 同 | **三面逐位相同** | 19:22:43–47 |

**② 元数据面（`/abs/` ＋ `export` API 之逐字）**：`citation_title` ＝ 「Deposon: An Auditable, Conservation-Guaranteed, Game-Theoretically Tested Scattering Layer over LLM Reasoning Paths」｜`citation_author` ＝ 「Yuan, Qihao」｜`citation_date` ＝ 「2026/09/08」｜`citation_arxiv_id` ＝ 「2609.09001」｜主分类 `Artificial Intelligence (cs.AI)`／次分类 `Machine Learning (cs.LG)`｜`export` API 之 `opensearch:totalResults` ＝ **1**｜entry id ＝ `http://arxiv.org/abs/2609.09001v1`｜entry `updated` ＝ **`2026-09-08T16:40:31Z`**｜提交历史（`/abs/` 逐字）：「**[v1]** Tue, 8 Sep 2026 16:40:31 UTC (1,598 KB)」⇒ **仅 v1**（`export` API 之 `totalResults`＝1 佐之）｜`Comments` 栏逐字见 ③。

**③ ★ 单位字面之逐字原文（本棒实取·`/abs/` 页 Comments 栏）**：

> `Comments:` ＝ 「**23 pages, 5 figures. Author affiliation: School of Chemistry and Life Resources, 〔高校R〕 University of China. Code: this https URL**」
> （⚠ arXiv 将外链显示为「this https URL」——其真实目标为 `https://github.com/zeroandcat/Deposon`；本棒**原样照录·不代其还原为 URL**）

**单位字面本体（自上栏切出·逐字）**：

```
School of Chemistry and Life Resources, 〔高校R〕 University of China
```

| 项 | 本棒实测 | 在册登记（`_v07p` L21／L48·**本棒经 grep 逐行实取该行字面·该件自身指纹未复测**） | 核 |
|:--|:--|:--|:--|
| **字符长度** | **66** | **66 字符** | ✅ 逐位相符 |
| **`sha256(bytes)[:12]`** | **`eccdb0565be7`** | **`eccdb0565be7`** | ✅ **逐位相符** |

**切出之可核法（本棒自测·可复现）**：自 Comments 栏纯文本（129 字符）之**全部 66 字符连续子串**空间内穷举（子串空间上界 129×130/2 ＝ **8,385**）⇒ **唯一命中** ＝ 上列字面（span ＝ [41,107]）；**再于「未压空白」之原始纯文本空间**（同法）复跑 ⇒ **同一唯一命中** ⇒ **非偶然撞串**。

**④ 同字面之第二面（源包内·独立复现）**：e-print 源包解包得 **7 个文件**：

| 成员 | bytes | `sha256[:12]` |
|:--|--:|:--|
| `00README.json` | 225 | `99561e418904` |
| **`deposon_paper_en.tex`** | **85,923** | **`7be7d6a907b1`** |
| `figures/fig1_boundary_map_en.png` | 360,057 | `921ea0ea7637` |
| `figures/fig2_killsign_scatter_en.png` | 248,010 | `02d70bb1bd2c` |
| `figures/fig3_division_scatter_en.png` | 278,252 | `a848305eefe7` |
| `figures/fig4_gt7_frontier_en.png` | 542,421 | `2d6d935fb369` |
| `figures/fig5_poa_distribution_en.png` | 442,102 | `decfbd34d9ed` |

`deposon_paper_en.tex` 内**逐字含**该单位行（「School of Chemistry and Life Resources, 〔高校R〕 University of China \\」）⇒ **摘要页 Comments 栏 ＝ 源包正文**之**双面互证**（两面各自独立取自 arXiv 之不同端点）。
⚠ **口径之辨（AC-5 之守）**：源包内该行**含 LaTeX 行续符 `\\`**（本棒实测该行字面长度 **69**、`sha256[:12]＝8e1d7ccbb164`）⇒ **与 Comments 栏之 66 字符字面非同一口径** ⇒ **⛔0 将二者当同一串相减或互证指纹**；二者之**文字本体相同**（续符为 TeX 排版记号）。

**⑤ ⚠ 在册 `47ccbbba1c47`／`8fa073e35fe0` 之实体之现状（`_l4r` §2-9 所称「0 在我方盘」）**：
- 在册登记（`_v07` **L120–L122** 逐字·**本棒经 grep 逐行实取该行字面·未全篇开卷**；`_v07` 本身之 bytes／SHA-12 本棒已自测）：`47ccbbba1c47` ＝ `_deposon_dualtrack_paper_final_md_v9_2026_10_13.md`（155,876 B）｜`8fa073e35fe0` ＝ `_deposon_dualtrack_paper_final_tex_v9_2026_10_13.tex`（179,926 B）＝ `arXiv提交四件套/latex源包/main.tex`（179,926 B）。
- **本棒联网实读所得之对应面**：arXiv 已发布之源包主文件为 **`deposon_paper_en.tex`**（**85,923 B／`7be7d6a907b1`**），**⛔0 与** `8fa073e35fe0`（179,926 B）**逐位相符** ⇒ **二者非同一件**（文件名／字节／指纹三项皆异）。
⇒ 📌 **口径之别（须 PI／口径官明之）**：在册所称「预印本 PDF／源包」之 `8fa073e35fe0` ＝ **拟提交源包之 `main.tex`**（179,926 B）；而 **arXiv 现挂之 v1 源包主文件** ＝ `deposon_paper_en.tex`（85,923 B）——**二者是不同件**（一为拟提交稿·一为已发布稿）。本棒**⛔0 断言**何者为准（归 PI／口径官），**只登记三项差异之事实**。
⚠ **本棒⛔0 断言**：本地 `paper/deposon_paper_final_cn.md`（53,838 B／`c5f6a23f4408`）与 `paper/deposon_paper_final_en.md`（68,164 B／`2ec20b96e941`）**皆不载**该 affiliation 字面（两者对 `〔高校R〕|Chemistry and Life Resources|affiliation` 之命中 ＝ **0**）——**故「单位字面」之在盘载体仍 0**（该两面之字面面 0 命中），**字面来源唯 arXiv 之两端点**。

**⑥ H8 门控之复现（在册 `_v07p` L36 所称「README 0 载」）**：

| 面 | URL／路径 | HTTP／在盘 | bytes | `sha256[:12]` | affiliation 命中 |
|:--|:--|:--|--:|:--|:--|
| 远端 README（当前 HEAD） | `https://raw.githubusercontent.com/zeroandcat/Deposon/06045bce…/README.md` | **200** | 7,279 | `a80b3db006a5` | **0** |
| 远端 README（登记时点） | `https://raw.githubusercontent.com/zeroandcat/Deposon/f44996fb…/README.md` | **200** | 7,279 | `a80b3db006a5` | **0** |
| 本地 README | `〔本地路径已脱敏〕` | 在盘 | 7,279 | **`a80b3db006a5`** | **0** |
| 远端 `paper/deposon_paper_final_en.md` | `https://raw.githubusercontent.com/zeroandcat/Deposon/06045bce…/paper/deposon_paper_final_en.md` | **200** | 68,164 | `2ec20b96e941` | **0** |

⇒ 📌 **在册「README 0 载 ⇒ 公开面与权威源 0 重合」之述，于联网面复现成立**（三面 README 之字节与指纹**逐位相同**＝ 同一件；affiliation 命中 0）。
⚠ **但**：在册 `_v07p` **L38** 载 PI 之「项25 采信」＝ **PI 明示豁免**该项之 H8 门控（M-07 单位字面自此可照录／引用）⇒ **本棒不重开该裁**（⛔0 代 PI 裁·⛔0 重裁）；**照录与否之终核本身仍候 PI**（`_v188` L22 之界分）。
📌 **可复现性**：字面**可复现**——`/abs/` 页两次取回之 `sha256[:12]` 逐位相同（`a60046e736ca`）；**但**该串之**语义位置**（Comments 栏之 `Author affiliation:` 段）为**版次相关**（arXiv v1 之 Comments 栏；若作者改版则可能变）⇒ 本棒**书其绑于 v1**（`citation_arxiv_id` ＝ 2609.09001·`updated` ＝ 2026-09-08T16:40:31Z·`totalResults` ＝ 1）。
⚠ **本棒⛔0 断言**：该字面**是否照录**（PI 之裁）；本棒**⛔0 将单位字面写入任何论文正文或终稿**（本棒唯一落盘件为本补件，且其内仅**照录于证据节**）。

### §4-4 · `L-5` 项① 之**远端侧** → ✅ **FOUND**

**① 461 明细表之实体与登记头（本棒逐字回读 `_book07` 册内）**：表头 ＝ 册 **L43**「| # | 远端路径 | bytes | 远端 blob sha1 | 移除项 |」；登记头 ＝ 册 **L37–L39**（逐字见 §2-4）；明细行 ＝ 册 **L45–L505**（**461 行**·索引 1–461 连续无缺无重——本棒解析实测 `n_461_parsed` ＝ 461／`idx_min` ＝ 1／`idx_max` ＝ 461／`idx_distinct` ＝ 461）。

**② ★ 远端侧逐件比对（登记时点树 `f44996fb…`）**：

| 检验 | 实测 | 口径 |
|:--|:--|:--|
| **路径命中** | **461 / 461** | 表内「远端路径」逐字 ＝ 登记时点树之 blob path |
| **blob sha1（40 位全值）逐位相符** | **461 / 461** | GitHub `git blob sha1`（表内 40 位全值 ＝ 树内 blob `sha` 全 40 位） |
| **bytes 逐位相符** | **461 / 461** | 表内 bytes ＝ 树内 blob `size` |
| **不符** | **0** | — |

**③ 独立复算（不经树·直接取字节自算）**：抽样 **12 件**（均匀跨全表：idx 1／2／30／90／150／210／260／300／350／400／440／461），经 `GET https://raw.githubusercontent.com/zeroandcat/Deposon/f44996fb…/<path>` 取字节 ⇒ **自算 `sha1("blob %d\0" + content)`**：
- **12 / 12** ＝ 表内 40 位值；
- **12 / 12** ＝ 树内 blob `sha`；
- **12 / 12** bytes ＝ 表内 bytes；
- HTTP **12 / 12 ＝ 200**。
⇒ **法之正控成立**（自算与两源皆合）⇒ **「远端 blob sha1 == 下表值」之登记（册 L38）于登记时点得联网实测之正面证实**。

**④ 当前远端之态（漂移面）**：

| 检验 | 实测 | 口径 |
|:--|:--|:--|
| 461 件之路径在**当前**树命中 | **0 / 461** | 当前树 `_september_workspace/` 前缀 blob 数 ＝ **0**（该前缀之 2,653 件已整体迁至 `_repo_mirror/` 或他位） |
| 461 件之 **blob sha1** 在当前树**任一路径**命中 | **0 / 461** | 以表内 40 位值为前缀／全值，在当前树 3,438 blobs 内检索 |
| 当前树与登记时点树之 sha 变更（两树皆存之路径） | **0** | `sha_changed_between_trees` ＝ 0（两树共同路径之 blob 内容**未变**） |
| 当前树与登记时点树之路径增删 | 登记时点有／当前无 ＝ **461**；当前有／登记时点无 ＝ **0** | `in_reg_missing_in_cur` ＝ 461／`in_cur_not_in_reg` ＝ 0 |
| 同 basename 于当前树之存在 | **0 / 10**（idx 1–10） | 当前树内无同名项 |

⇒ 📌 **结论**：461 件之**登记时点远端侧**已**逐位具凭**（461/461）；**当前远端侧**则 461 件之**原路径与原 blob sha1 均已不在**（`_september_workspace/` 前缀已整体迁移）⇒ **在册 `_l5v` §2-1 之「远端侧不可核」之缺已解**（解于登记时点）；**当前态另成一读**——**漂移 461／461**（非「缺失」之断言，⛔0 断言其成因，⛔0 断言其应为「仍存」）。
⚠ **口径之辨（AC-5 之守）**：上表「461／461 命中」之**登记时点** ＝ `f44996fb…`（2026-10-12 登记时点）；「0／461」之**当前时点** ＝ `06045bce…`（2026-10-23）——**两数分属不同树·不同时点**，**⛔0 相减**；**「461」在两读中之身份亦不同**（登记时点之**差异件清单** ＝ 远端实体；当前之**已迁路径** ＝ 当前实体之缺席）。
⚠ **本棒⛔0 断言**：当前远端之「461 件是否仍以**等价内容**存在于他路径」——本棒仅取**同名 basename 抽样 10 件**（＝0 命中）＋**全量 blob sha1 前缀检索**（＝0 命中）两法；**异名异容之等价物** ⛔0 排除（**未作内容级全文比对**，且 GitHub blob API 因限额 403 ⇒ 此面记 **`OUT_OF_RANGE`**）。

---

## §5 · **AC 逐条回应**（**逐条自核**）

| # | AC | **自核回应** |
|:-:|:--|:--|
| **AC-1** | 一份补件落盘于指定路径，bytes／SHA-12 与 `_bcheck.py` 五项写入件内 | ✅ 落盘于 `results\verdict\judgement\_l4_l5_online_supplement_2026_10_27.md`（落盘前 `Test-Path` ＝ **False**·本棒实测）｜**`_bcheck.py` 五项（BOM／CR／VT／FFFD／末字节）写入 §9**（写入后复跑之实测·性质读数·自洽）｜**`BYTES`／`NON_ASCII`／`LF` 亦写入 §9-A**（**等宽数字替换**法填入·不增删字节⇒填入后复跑**逐位相符**·自洽）｜⚠ **`SHA12` 不能自写入**（其值 ＝ `sha256(bytes)[:12]`·**写入即改其指纹**⇒物理上不可自洽）⇒ 载于**件外回报**（沿 `_f04` 补件同一体例·见其头 L6）——**此一自指回环之限，本棒如实登记于 §9-A 首段，不以任何方式充作已写入** |
| **AC-2** | `U-3`／`U-4`／`U-9` 与 `L-5` 项① **逐项回源列出其确切命题**（件名＋行号），再给查证结果 | ✅ §2-1（`_v06` L371／`_v07` L469／`_l4r` L67–71）｜§2-2（`_v06` L372／`_v07` L470／`_l4r` L73–78）｜§2-3（`_v06` L377／`_v07` L475／`_l4r` L109–113／单位字面之定义 `_cb05` L45／指纹登记 `_v07p` L21·L48／PI 已释之界 `_v188` L22）｜§2-4（`_v06` L414／`_l5v` L31–56／`_book07` L37–L39·L43）——**四项各得独立小节·逐字引文**；查证结果见 §4-1–§4-4 |
| **AC-3** | 每项查证结果必带：**检索式／检索范围／命中数／时点／来源 URL（可核）／可复现与否** | ✅ 检索式 ＝ **§3-1 之逐字 URL 表**（15 条）｜检索范围 ＝ **§3-2**（`truncated=false` 之全量·两树·四锚树＋arXiv 四端点）｜命中数 ＝ 各项内表（`U-3` 六行／`U-4` 两表／`U-9` 四表／`L-5` 项① 四表）｜时点 ＝ **19:14:02–19:22:51**（逐条入表）｜来源 URL ＝ 各项内表逐行给出｜可复现与否 ＝ §3-3（**arXiv 三面两次取回逐位相同**；**GitHub 树两次取回 blob 集合 diff ＝ 0**；`raw` 自算 12/12）＋各项之限注 |
| **AC-4** | 每项落一个状态：**`FOUND`（附据）／`NOT_FOUND_IN_SCOPE`（附射程）／`OUT_OF_RANGE`（附因）** | ✅ §0 与 §4-1–§4-4：**四项皆 `FOUND`（附据）**｜另 **二面记 `OUT_OF_RANGE`（附因）**：①GitHub **blob API 逐件核**（匿名限额 60/60 耗尽·`/rate_limit` 实测 `remaining 0`；12 件抽样**全 403**；负控亦 403 ⇒ **⛔0 以 403 当阴性**）②arXiv **PDF 内文全文级解析**（本棒⛔0 装解析器 ⇒ 仅取字节与指纹；文面改以 **e-print 源包 `.tex`** 证之）｜**本棒 0 报 `NOT_FOUND_IN_SCOPE`**（四项皆非阴性） |
| **AC-5** | 凡引外部数值，须书其口径与原始出处；⛔0 把两个不同口径之数相减充「差额」 | ✅ 口径之辨 **四处明书**：①§4-1 之 `409`（`commits?sha=` 起点枚举）与 `490`（`compare` `ahead_by`）**⛔0 相减**②§4-2 之「全树 3,462」＝ **blob 条目数**（＝在册 v234 之口径）vs「entries 合计 3,659」，且**在册读数之 `pushed_at` ＝ 10-18 晚刻 vs 本棒 ＝ 10-23 之后 ⇒ 其差 ＝ 变更量·非缺失量**③§4-3 之 Comments 栏 66 字符 vs 源包 `.tex` 69 字符（含 `\\`）**⛔0 当同串**④§4-4 之「461/461」＝ 登记时点树 vs「0/461」＝ 当前树，**⛔0 相减**。**每一处外部数值皆附端点 URL ＋ bytes／指纹 ＋ 取用时刻** |
| **AC-6** | 既有件触动数 ＝ 0（自证给核法与读数） | ✅ **核法** ＝ ①本棒**写操作仅三类**：于 `.tmp\` 下**新建**本棒自有新件（25 件·清单见 §7）＋ 于 `results\verdict\judgement\` 下**新建**本件（落盘前 `Test-Path` ＝ False）②**⛔0 调任何 edit/modify/delete 于既有件**③**⛔0 动 `〔本地路径已脱敏〕` 归档区 ＋ `deposon-sub` 之正文**（⛔0 读其正文）｜**读数** ＝ §7 之「既有件指纹复测」表（**5 件·落盘前之值 ＝ 落盘后之值·逐位相符**）⇒ **既有件触动数 ＝ 0**（含：⛔0 改／移／重命名／删）｜**远端写入数 ＝ 0**（GitHub／arXiv 皆匿名 GET，无 POST/PUT/PATCH/DELETE） |
| **AC-7** | 字节五项自核读数写入件内 | ✅ §9 之表（**本件落盘后** `python -P 〔幽灵引用·未上传:_bcheck.py〕 <本件>` 之实测：BOM／CR／VT／FFFD／末字节／bytes／SHA-12／LF） |

---

## §6 · **四项状态一览**（**含来源 URL**）

| 项 | **状态** | **一句话据** | **来源 URL（可核）** |
|:--|:--|:--|:--|
| **`U-3`** | **FOUND** | 当前 HEAD ＝ `06045bce…` ≠ 登记时点 `f44996fb…`；然登记时点 commit **仍可达**（200）且为当前 HEAD 之祖先（`compare`＝ahead／490／behind 0／merge_base ＝ 自身） | `https://api.github.com/repos/zeroandcat/Deposon/commits/main`｜`…/commits/f44996fbfd9f386299442924f70585bb20d935fc`｜`…/compare/f44996fbfd9f386299442924f70585bb20d935fc...06045bceff07908aa38b8b5d3e626731b7326e7d` |
| **`U-4`** | **FOUND** | 远端全量（`truncated=false`）：当前 **3,438 blobs**／185,403,899 B；登记时点 **3,063 blobs**／109,121,770 B；全量分区（顶层·blob 件数）两时点并列给出；**461 ⊂ 登记时点 `_september_workspace/` 之 2,653** ⇒ 461 非全量 | `https://api.github.com/repos/zeroandcat/Deposon/git/trees/main?recursive=1`｜`…/git/trees/f44996fbfd9f386299442924f70585bb20d935fc?recursive=1` |
| **`U-9`** | **FOUND**（＋终核候 PI） | Comments 栏单位字面＝「`School of Chemistry and Life Resources, 〔高校R〕 University of China`」**66 字符**／`eccdb0565be7` —— **与在册指纹逐位相符**；e-print 源包 `deposon_paper_en.tex` 内独立复现；**照录与否归 PI** | `https://arxiv.org/abs/2609.09001`｜`https://arxiv.org/e-print/2609.09001`（→`/src/`）｜`https://export.arxiv.org/api/query?id_list=2609.09001` |
| **`L-5` 项①** | **FOUND** | 登记时点树逐件：路径 **461/461**、blob sha1（40 位）**461/461**、bytes **461/461**；12 件 raw 取字节自算 **12/12** 相符；当前树则 461 原路径皆已迁（0/461） | `…/git/trees/f44996fbfd9f386299442924f70585bb20d935fc?recursive=1`｜`https://raw.githubusercontent.com/zeroandcat/Deposon/f44996fbfd9f386299442924f70585bb20d935fc/<path>` |

---

## §7 · **既有件触动数 ＝ 0** 之自证（**核法＋读数**）

**核法**：①本棒**写操作全集** ＝ `.tmp\` 下**新建**（25 件·皆本棒自有新名·前缀 `_l4_l5_online_`）＋ `results\verdict\judgement\` 下**新建**本件（落盘前 `Test-Path` ＝ **False**·本棒实测）②**⛔0** 对任何既有件行 `edit`／`write`／删除／移动／重命名 ③**⛔0** 写远端（仅 GET）④**⛔0** 读 `GLM` 归档区 `deposon-sub` 之正文。

**既有件指纹复测（落盘前 ＝ 落盘后·逐位相符）**：

| 件 | 落盘前（本棒开工时实测） | 落盘后复测 | 核 |
|:--|:--|:--|:-:|
| `results\verdict\judgement\_f04_l4_l5_item1_supplement_2026_10_27.md` | 36,946／`ce2508044c2c` | **36,946／`ce2508044c2c`** | ✅ |
| `results\_book_03_achievements_inventory_full_2026_10_22.md` | 1,181,645／`ba8a1e0ebce8` | **1,181,645／`ba8a1e0ebce8`** | ✅ |
| `_HANDOVER_MUST_READ.md` | 29,809／`d3513a125be5` | **29,809／`d3513a125be5`** | ✅ |
| `results\work\process\_zero_blockers_list_2026_10_26.md` | 41,376／`8edfcdce2b62` | **41,376／`8edfcdce2b62`** | ✅ |
| `results\verdict\judgement\_l5_four_open_items_verification_2026_10_27.md` | 32,097／`db30cf540d52` | **32,097／`db30cf540d52`** | ✅ |

**本棒于 `.tmp\` 下新建之件（25 件·皆本棒自有新名·⛔0 覆盖任何既有件）**：

`_l4_l5_online_gh_2026_10_27.py`｜`_l4_l5_online_gh_repo_2026_10_27.json`｜`_l4_l5_online_gh_commit_main_2026_10_27.json`｜`_l4_l5_online_gh_commit_reghead_2026_10_27.json`｜`_l4_l5_online_gh_tree_main_2026_10_27.json`｜`_l4_l5_online_gh_tree_reghead_2026_10_27.json`｜`_l4_l5_online_gh_tree_739a7daf_2026_10_27.json`｜`_l4_l5_online_gh_summary_2026_10_27.json`｜`_l4_l5_online_gh_probe2_2026_10_27.py/.json`｜`_l4_l5_online_gh_probe3_2026_10_27.py/.json`｜`_l4_l5_online_arxiv_2026_10_27.py`｜`_l4_l5_online_arxiv_abs_2026_10_27.bin/.html`｜`_l4_l5_online_arxiv_export_api_2026_10_27.bin`｜`_l4_l5_online_arxiv_pdf_2026_10_27.bin`｜`_l4_l5_online_arxiv_eprint_2026_10_27.bin`｜`_l4_l5_online_arxiv_summary_2026_10_27.json`｜`_l4_l5_online_unit_2026_10_27.py/.json`｜`_l4_l5_online_repro_2026_10_27.py/.json`｜`_l4_l5_online_readme_2026_10_27.py`｜`_l4_l5_online_readme_check_2026_10_27.json`｜`_l4_l5_online_probe4_2026_10_27.py/.json`｜`_l4_l5_online_probe5_2026_10_27.py/.json`｜`_l4_l5_online_probe6_2026_10_27.py/.json`。

---

## §8 · **仍未解之面**（**⛔0 本棒所能**）

| # | 面 | 归属 | 说明 |
|:-:|:--|:--|:--|
| 1 | **`U-9` 之照录与否（PI 终核）** | **PI** | 字面已实取（66 字符／`eccdb0565be7`）；**是否照录**（H8 门控·`_v188` L22 之界分：PI「已释」**未随字面**）**候 PI** |
| 2 | **`U-9` 之在盘载体（`47ccbbba1c47`／`8fa073e35fe0`）** | **他棒／PI** | 本棒联网所得之 arXiv v1 源包主文件 ＝ `deposon_paper_en.tex`（85,923 B／`7be7d6a907b1`）**≠** 在册 `8fa073e35fe0`（179,926 B）——**拟提交稿 vs 已发布稿之别**，须 PI／口径官明之 |
| 3 | **`U-5`／`U-6`／`U-7`／`U-10`** | **PI／口径官** | **非联网面**（本棒⛔0 越界） |
| 4 | **`U-2` 之择一为权威** | **PI** | 非联网面 |
| 5 | **`U-8` 之处置（补传／补登记／沿用旧登记）** | **处置权（非本棒）** | 非联网面 |
| 6 | **`L-5` 项③ 之 §7 延后项触发时点调和** | **PI** | 非联网面 |
| 7 | **`L-5` 项④ 之 `U-2` 成因断言** | **PI／判定官** | 非联网面 |
| 8 | **461 件当前远端之「等价内容是否存在于异名异容之他路径」** | **待补（`OUT_OF_RANGE`·限 GitHub 匿名限额 60/60 耗尽）** | 本棒已作两法（同名 basename 抽样 10 件 ＝ 0；全量 blob sha1 前缀检索 ＝ 0）｜**异名异容之等价物 ⛔0 排除**（未作内容级全文比对；`/git/blobs/{sha}` 12 件抽样**全 403**·负控亦 403 ⇒ **⛔0 当阴性**）——**限解除后可补**（GitHub 限额重置后可再取） |
| 9 | **远端全量读数与在册 v234 读数之差之成因** | **PI／他棒** | 在册 v234（10-18 晚刻）＝ 3,462 blobs／126,187,988 B；本棒当前（10-23 之后）＝ 3,438 blobs／185,403,899 B；**两者之差之成因本棒⛔0 断言**（⛔0 以其充「缺失量」） |
| 10 | **本棒四行之核得态（已立／未立／不可得）之判定** | **PI／`verdict-keeper`** | 本棒**⛔0 落五终判**；只供证据面（依 `_l4r` §2-0 之判准，闭权不在本棒） |

---

## §9 · **字节五项自核读数**（**本件落盘后实测**·`python -P 〔幽灵引用·未上传:_bcheck.py〕`）

| 项 | 读数 |
|:--|:--|
| `BYTES` | **（见 §9-A）** |
| `SHA12` | **（见 §9-A）** |
| `BOM` | **0** |
| `CR` | **0** |
| `VT` | **0** |
| `FFFD` | **0** |
| `LAST_BYTE` | **`0x0a`** |
| `NON_ASCII` | **（见 §9-A）** |
| `LF` | **（见 §9-A）** |

### §9-A · 终态自测读数（**定宽占位·填入后复算自洽**）

> 📌 **口径之自限（自指回环）**：`SHA12` ＝ `sha256(bytes)[:12]`——**将其写入本件即改本件之字节** ⇒ **该值在物理上不可自洽于件内** ⇒ 其**终值载于件外回报**（沿 `_f04` 补件同一体例）。**`BYTES`／`NON_ASCII`／`LF` 三项则可自洽**：其值**不随填入而变**（填入为**等宽数字替换**·不增删字节·不增行·皆 ASCII），故本节所载之三值**经填入后复跑 `_bcheck.py` 逐位相符**。
> 📌 **第 1 读**（§9-A／§9-B／§9-C 扩写前之态·本棒实测·2026-10-27 19:2x）：`BYTES` ＝ **49107**｜`SHA12` ＝ **`b479c45ff46e`**｜`BOM` ＝ 0｜`CR` ＝ 0｜`VT` ＝ 0｜`FFFD` ＝ 0｜`LAST_BYTE` ＝ **`0x0a`**｜`NON_ASCII` ＝ 24422｜`LF` ＝ 393。

| 项 | **终态读数**（填入后复跑 `_bcheck.py` 实测·逐位相符） |
|:--|:--|
| `BYTES` | **52205** |
| `NON_ASCII` | **25529** |
| `LF` | **426** |
| `BOM` | **0** |
| `CR` | **0** |
| `VT` | **0** |
| `FFFD` | **0** |
| `LAST_BYTE` | **`0x0a`** |
| `SHA12` | **（终值载于件外回报·自指回环之物理限制·见本节首之说明）** |

### §9-B · **本棒自测之 `_l4r` 之指纹**（**AC-6 之附证·随 §1-1 补记**）

`_l4r` ＝ `results\verdict\judgement\_l4_u1_u10_independent_carrier_recheck_2026_10_27.md` —— **32,527／`9ab5f787e96c`**（本棒实测·与 `_f04` §1-1 所载**逐位相符**）｜`BOM 0／CR 0／VT 0／FFFD 0／LAST_BYTE 0x0a`。

### §9-C · **AC-6 终态复测**（**既有件指纹·落盘后 ＝ 落盘前·逐位相符**）

| 件 | bytes／SHA-12（落盘前） | bytes／SHA-12（落盘后复测） | 核 |
|:--|:--|:--|:-:|
| `_f04` ＝ `results\verdict\judgement\_f04_l4_l5_item1_supplement_2026_10_27.md` | 36,946／`ce2508044c2c` | **36,946／`ce2508044c2c`** | ✅ |
| `_book03` ＝ `results\_book_03_achievements_inventory_full_2026_10_22.md` | 1,181,645／`ba8a1e0ebce8` | **1,181,645／`ba8a1e0ebce8`** | ✅ |
| `_HANDOVER_MUST_READ.md` | 29,809／`d3513a125be5` | **29,809／`d3513a125be5`** | ✅ |
| `_zero_blockers_list_2026_10_26.md` | 41,376／`8edfcdce2b62` | **41,376／`8edfcdce2b62`** | ✅ |
| `_l5v` ＝ `results\verdict\judgement\_l5_four_open_items_verification_2026_10_27.md` | 32,097／`db30cf540d52` | **32,097／`db30cf540d52`** | ✅ |
| `_book07` ＝ `results\_book_07_upload_side_desensitized_remote_sha_letter_kimi_2026_10_22.md` | 89,791／`a13ec23c4b3b` | **89,791／`a13ec23c4b3b`** | ✅（⚠ 其 `CR` ＝ 477 为**其自身之既存状态**·本棒 0 改） |
| `_v06` ＝ `letters\_commission_glm_dualtrack_paper_v0.6_2026_10_12.md` | 56,360／`6d1b14983555` | **56,360／`6d1b14983555`** | ✅ |
| `_v07` ＝ `letters\_commission_glm_dualtrack_paper_v0.7_2026_10_18.md` | 70,048／`07e068165dd5` | **70,048／`07e068165dd5`** | ✅ |
| `_l4r` ＝ `results\verdict\judgement\_l4_u1_u10_independent_carrier_recheck_2026_10_27.md` | 32,527／`9ab5f787e96c` | **32,527／`9ab5f787e96c`** | ✅ |

⇒ 📌 **9/9 逐位相符** ⇒ **既有件触动数 ＝ 0**（含：⛔0 改／移／重命名／删）｜**远端写入数 ＝ 0**（GitHub／arXiv 皆匿名 GET·无 POST/PUT/PATCH/DELETE）。

---

**落款**：worker（无名执行棒·联网补证）·2026-10-27 19:1x–19:2x GMT+8｜**本件为唯一落盘之新件**｜⛔0 落五终判·⛔0 代 PI 裁·⛔0 宣告任何零·⛔0 改／移／重命名／删任何既有件·⛔0 写远端
