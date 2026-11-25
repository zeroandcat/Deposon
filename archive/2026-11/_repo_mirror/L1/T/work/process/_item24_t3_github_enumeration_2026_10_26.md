# `项24` 之 `T-3` · GitHub 远端枚举（认可面·2026-10-26 夜）

> 📌 **本件性质**：**查证件**（认可面之枚举·射程·正控·零控·命中面）——⛔ **0** 落五终判｜⛔ **0** 代 PI 裁｜⛔ **0** 代销记｜⛔ **0** 改／移／重命名／删任何既有件（**既有件触动数 ＝ 0**）｜⛔ **0** 读 `〔本地路径已脱敏〕` 面｜⛔ **0** 读归档区正文｜⛔ **0** 派生 JSON 合并｜**本件联网仅限 `T-3` 远端枚举（PI 已授权此面）**。
> 📌 **观测时点**：2026-10-26 **22:5x–23:0x**（GMT+8）｜**本棒新件 ＝ 4**（本件＋`N-3`／`N-5`／`N-6` 三件；落盘前 `Test-Path` 皆 ＝ `False`）｜**skill 实带**：`evidence-contract`（**3,921／`e7fd7b39c22f`**·本棒自测）。
> 📌 **令源**：**裁 297**（`v413` **L18**）｜**裁 283**（`v409` **L18**）｜**PI 2026-10-18 之「GLM 只认 Github」射程面**〔经 `_item24_r4_gate_trigger_conditions_2026_10_25.md`（**24,633／`a51551bcb7d4`**·本棒自测）**L79** 转引 `84037fd8d0a6` **L12／L164／L172–L178**：「`F5` 之**认可面 ＝ GitHub 远端**；本地面（`〔本地路径已脱敏〕`）读数**一律标「非认可面」**」〕。

---

## §1 · 结论先行

**认可面（GitHub 远端）之全部分支·全 tag·全树·全 commits 已穷尽枚举**（1 分支／0 tag／**3,573** 路径／**654** commits）；**「回执」类可枚举实体在位者 ＝ 12（`receipt`）＋ 4（`回执`）＋ 16（`回函`）**，其中**最强候选 ＝ `_repo_mirror/agent_shared_2026_10_23/_dave__GLM回函交付包_2026_10_13/arXiv提交四件套/`**（论文撰写侧〔GLM〕之交付**在位**，四件套中三件经 `contents` 实取 ＝ **200**）。

**然：是否即 `T-2`／`T-3` 所指之「该收口包之回执」⇒ ⛔ 0 径认**——**`T-4`（「回执」之所指三解之择）至今未由 PI 界分**，且回执之**形态、字段、抬头与签发人**在册自陈「**未核得（⛔ 0 代拟）**」⇒ **无判准可据以认定** ⇒ 本件**登记之，不判之**。

---

## §2 · 枚举之射程（本棒实测·逐项明书）

| 项 | 射程 | 实测值 |
|:--|:--|:--|
| **仓** | `zeroandcat/Deposon`（在册唯一之 GitHub 远端仓；`letters/_commission_glm_dualtrack_paper_v0.6_2026_10_12.md`｜**56,360／`6d1b14983555`**·本棒自测｜**§3.1 L154** 逐字「**远端仓库**｜**`zeroandcat/Deposon`**」） | `GET /repos/zeroandcat/Deposon` ＝ **200**｜`default_branch` ＝ **`main`**｜`size` ＝ 94,014 KB｜`pushed_at` ＝ **2026-10-23T07:17:12Z** |
| **分支** | 全部分支（`/branches` ＋ `/git/refs`） | **1**：`main` ＝ **`06045bceff07908aa38b8b5d3e626731b7326e7d`**（本棒实测之当前 HEAD） |
| **tag** | 全部 tag（`/tags`） | **0**（返回 `[]`，2 B） |
| **refs** | 全 ref（`/git/refs`） | **1**：`refs/heads/main`（无其他 ref） |
| **树** | `main` 全树递归（`/git/trees/main?recursive=1`） | **3,573** entries，`truncated` ＝ **`False`** ⇒ **枚举完整** |
| **时间窗** | commits：`since=2026-09-01T00:00:00Z` → 今（2026-10-26）；**分页至末页**（`per_page=100`，**7 页**，末页 54 条 ⇒ 其后为空） | **654** commits（自 **2026-09-01** 至 **2026-10-23T07:17:11Z**） |
| **未取** | ❌ 未取 PDF 本体内容（`Deposon_II_v9_arXiv预印本.pdf` 之 `contents` **读超时**）｜❌ 未取 `arXiv` 站之任何页面（本面非其射程）｜❌ 未下载 tar.gz | 如实登记 |

---

## §3 · 枚举之法与 HTTP 逐条记录（本棒实测）

| # | 端点 | 状态 | 字节 |
|:-:|:--|:-:|--:|
| 1 | `GET /repos/zeroandcat/Deposon` | **200** | 5,348 |
| 2 | `GET /repos/zeroandcat/Deposon/branches` | **200** | 200 |
| 3 | `GET /repos/zeroandcat/Deposon/tags` | **200** | 2（`[]`） |
| 4 | `GET /repos/zeroandcat/Deposon/git/refs` | **200** | 336 |
| 5 | `GET /repos/zeroandcat/Deposon/git/trees/main?recursive=1` | **200** | 989,232 |
| 6 | `GET /repos/zeroandcat/Deposon/commits?since=2026-09-01T00:00:00Z&per_page=100&page=1…7` | **200** ×7 | 345,128／346,011／344,470／342,727／345,718／351,594／181,542 |
| 7 | `GET …/contents/README.md` | **200** | 10,800 |
| 8 | `GET …/contents/__probe_nonexistent_9x7__` | **404** | 127 |
| 9 | `GET …/contents/_s4_kv3s_4_123_readings_2026_10_12.json` | **404** | 127 |
| 10 | `GET …/contents/<GLM回函交付包>/arXiv提交四件套/_dave__v9提交元数据件_2026_10_12.md` | **200** | blob sha `becf449a6d1d`／**7,007 B** |
| 11 | `GET …/arXiv提交四件套/Deposon_II_v9_arXiv源包.tar.gz` | **200** | blob sha `0de13122a710`／**57,239 B** |
| 12 | `GET …/arXiv提交四件套/latex源包/body_v9_stripped.md` | **200** | blob sha `3620596bf23b`／**155,881 B** |
| 13 | `GET …/arXiv提交四件套/Deposon_II_v9_arXiv预印本.pdf` | **ERR（读超时）** | — ⇒ 其在位性由**树枚举**证之；**本棒未取其 sha／size** |

---

## §4 · 正控（**同一法对一已知存在之对象必命中**）

| 正控 | 期望 | 实测 | 判定 |
|:--|:--|:--|:--|
| **P-1 存在性**：`contents/README.md` | **200** | **200**｜blob sha `d829f45b928e`｜size **7,279** | ✅ **命中** |
| **P-2 内容性**：README 之内含本项目之实名 | 命中 | 「Deposon」＝ **True**；「arXiv」＝ **True**；87 行 | ✅ **命中** |
| **P-3 族级存在**：`letters/` 全族在远端 | 在位 | **28** 路径命中（逐条见 §5-4） | ✅ **命中**（⚠ 与在册 10-12 之「0 命中」**时点相牾**，见 §6-2） |
| **P-4 提交面存在**：GLM 回函交付包/arXiv 提交四件套 | 在位 | 路径在树内；三件经 `contents` **200** | ✅ **命中** |

---

## §5 · 零控（**对一必然不存在之对象须 0 命中**）

| 零控 | 期望 | 实测 | 判定 |
|:--|:--|:--|:--|
| **Z-1**：`contents/__probe_nonexistent_9x7__` | **404** | **404**（127 B） | ✅ **0 命中** |
| **Z-2**：`contents/_s4_kv3s_4_123_readings_2026_10_12.json` | **404** | **404** | ✅ **0 命中** |
| **Z-3**：全树检索 `_s4_kv3s_4_123_readings` | **0** | **0 命中**（3,573 路径） | ✅ **0 命中** ⇒ **补强**：`件-1` 之读数件在**认可面亦不存在**（本地之 0 命中见第二段件 §3-4） |
| **Z-4**：全树检索 `_september_workspace` | **0** | **0 命中** | ✅ **0 命中** ⇒ **锚链漂移**（见 §6-3） |

---

## §6 · 命中面与三条界

### §6-1 · 「回执」类实体之命中（**逐条路径**·均在 `main` 树内）

**A · `receipt`（12）**
`_repo_mirror/doc/letter/_supplement_execution_receipt_kimi_2026_10_18.md`｜`_repo_mirror/doc/letter/_upload_execution_receipt_kimi_2026_09_26.md`｜`_repo_mirror/doc/letter/_upload_execution_receipt_kimi_2026_09_30.md`｜`_repo_mirror/doc/letter/_upload_execution_receipt_kimi_2026_10_01.md`｜`_repo_mirror/doc/paper/_pending_supply_search_receipt_2026_10_08.md`｜`_repo_mirror/readout/final/_freeze_receipt_2026_10_01_q1.md`｜`_repo_mirror/verdict/pi/_batch3_execution_receipt_kimi_2026_10_18.md`｜`_repo_mirror/verdict/pi/_e2_glm2_distill_side_receipt_register_2026_10_09.md`｜`_repo_mirror/verdict/pi/_kimi_receipt_authority_rulings_effect_2026_10_18.md`｜`_repo_mirror/verdict/pi/_pack_d_closeout_confirm_receipt_note_2026_10_01.md`｜`_repo_mirror/verdict/pi/_receipt_disposition_register_2026_10_08.md`｜`_repo_mirror/verdict/pi/_stage4_close_and_batch3_receipt_register_2026_10_18.md`

**B · 「回执」（4）**｜`_repo_mirror/agent_shared_2026_10_23/_bob__v156裁答函独立复核回执_2026_10_20`（**目录**）＋ 其内 `bob_v156_result.json`／`verify_v156.py`｜`_repo_mirror/agent_shared_2026_10_23/_charlie__V4接受回执与D1首轮反馈_2026-09-20.md`

**C · 「回函」（16）**｜`_alice__37项主实验清点回函_2026_10_21.md`｜`_alice__采认五位处置回函_2026_10_22.md`｜`_bob__GLMV2回函模板待填栏值清单_deposon线_2026-09-18.md`｜`_bob__minimax委托回函_2026_10_12.md`｜`_bob__回函二次补遗_2026_10_12.md`｜`_bob__回函补遗_2026_10_12.md`｜`_bob__实验面处置回函_2026_10_22.md`｜`_charlie__致MiniMax回函_2026-09-18.md`｜`_dave__GLM回函交付包_2026_10_13`（**目录**）＋ 其内 `arXiv提交四件套`（**目录**）＋ `Deposon_II_v9_arXiv预印本.pdf`｜`Deposon_II_v9_arXiv源包.tar.gz`｜`_dave__v9提交元数据件_2026_10_12.md`｜`latex源包/body_v9_stripped.md`｜`latex源包/md2tex_v9.py`

### §6-2 · 最强候选（**论文撰写侧之交付在位**）——`arXiv提交四件套`

| 件 | 状态 | 字节 | **本棒自测指纹** | 可观测内容（逐字·截） |
|:--|:--|--:|:--|:--|
| `_dave__v9提交元数据件_2026_10_12.md` | **200** | 7,007 | **SHA-12 `c54a32fb4261`**（解码后全字节实算） | L1「# 戴夫·arXiv 提交元数据件（v9 轮，2026-10-12）」｜L3「**纪律**：作者字面＝PI 专留、0 代拟；全部字段供提交动作取用，提交动作归 PI」｜L12 题名「Deposon: An Auditable, Conservation-Guaranteed Scattering Layer over LLM Reasoning Paths — **II. One Audit Arc**…」｜L20「**本字段为 PI 专留项**」 |
| `latex源包/body_v9_stripped.md` | **200** | 155,881 | **SHA-12 `6b0612a355dc`** | L4「**Evidence-strength convention（before any reading）**…**closed (pre-registered)**…」｜L26「…two completed phases, already published together as the first paper…」 |
| `Deposon_II_v9_arXiv源包.tar.gz` | **200** | 57,239 | （未下载·未实测指纹） | — |
| `Deposon_II_v9_arXiv预印本.pdf` | **读超时** | — | — | **在树内**（路径枚举命中）；**本棒未取其 sha／size** |

### §6-3 · 三条界（**明书·不判**）

1. **`T-4` 未界分 ⇒ 不得径认**：「回执」之所指经 PI 界分（三解之择）**至今未给**〔`_item24_r4_gate_trigger_conditions_2026_10_25.md` **L80**：「在所指未界分之前，任何『是否已成就』之判读**皆缺前提**」）⇒ 本棒**只登记命中面**。
2. **回执之形态至今未定**：「coze 侧**实际**之回执形态、字段、抬头与签发人｜**未核得（⛔ 0 代拟）**｜PI 未给该形态 ⇒ 本件**0 代立草案**」〔`letters/_commission_coze_〔IM〕_closeout_pack_2026_10_12.md`｜**26,816／`7818cfe2d226`**·本棒自测｜**L237**〕⇒ **无判准可据以认定**。
3. **时点漂移三则（登记·⛔ 0 调和）**：
   - **HEAD 已迁移**：在册「登记时点 HEAD」＝ `f44996fbfd9f386299442924f70585bb20d935fc`〔`6d1b14983555` **L156**〕；**本棒实测当前 HEAD** ＝ `06045bceff07908aa38b8b5d3e626731b7326e7d`（`pushed_at` 2026-10-23T07:17:12Z）⇒ v0.6 **L160** 之预警（「登记时点 ≠ 你侧读取时点」）**已实证**。
   - **`letters/` 由 0 命中变为 28 命中**：在册逐字「`letters/` 全族经实测于远端 461 件中 **0 命中** ⇒ 必随包」〔`6d1b14983555` **L124**〕＝ **10-12 时点**；**本棒（10-26）实测 28 命中** ⇒ **时点之变**（10-23 之 mirror rebuild 批次补入），**非矛盾**。
   - **`_september_workspace/` 前缀已不存在**：在册登记之远端路径前缀〔`6d1b14983555` **L123**／**L205**〕在本棒之树枚举中 **0 命中** ⇒ **锚链漂移**（10-23「mirror rebuild … v0.6 旧镜像退役」之结构性变更）⇒ 后续引用须以本棒实测路径为准。

---

## §7 · 老实交代

1. 本棒**未落五终判·未代 PI 裁·未代销记**；**未宣告** `T-3` 已成就、**未宣告** `T-2` 已成就。
2. 本棒**联网仅限本面**（`T-3` 远端枚举·PI 已授权）；**未取** arXiv 站、**未取** PDF 本体、**未下载** tar.gz、**未写**远端任何一字节（只读 GET）。
3. 本棒**未读** `〔本地路径已脱敏〕` 面｜**未读**归档区正文｜**未派生 JSON 合并**｜**未派棒**｜**未改既有件一字**（**既有件触动数 ＝ 0**）。
4. 本棒**未开卷**远端之 12＋4＋16 件之正文（除 §6-2 之两件已解码者）⇒ **其是否即「论文撰写侧之回执」本棒未判**。

---

**状态行**：`项24 之 T-3 · GitHub 远端枚举（查证件）· 射程：zeroandcat/Deposon｜main 1 分支（HEAD 06045bceff07…实测）｜0 tag｜1 ref｜树 3,573（truncated=False）｜commits 654（since 2026-09-01·7 页至末页）· 正控 4/4 命中（README 200＋含 Deposon/arXiv；letters/ 28；提交四件套在位）· 零控 4/4 零命中（probe 404／读数件 404／树检索 0／_september_workspace 0）· 回执类命中 12 receipt＋4 回执＋16 回函；最强候选＝GLM 回函交付包/arXiv 提交四件套（元数据件 7,007/c54a32fb4261；正文 155,881/6b0612a355dc；源包 57,239；PDF 读超时未取指纹）· 三条界：T-4 未界分不得径认／回执形态未核得／HEAD 与 letters/ 与 _september_workspace 三处时点漂移已登记 · ⛔0 落五终判·⛔0 代裁·⛔0 宣告 T-3/T-2·⛔0 改既有件一字·⛔0 读 GLM·⛔0 派生 JSON 合并`
**落款**：**证据链审计官**（`evidence-auditor`）· deposon 证据链审计棒 · 2026-10-26 夜 · 本件为**查证件**·**不落终判·不代裁·不代销记**
