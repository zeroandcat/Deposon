# 待PI补件四项（R-93／R-94／R-114／R-115）三面检索回执

> 任务：deposon · N-3③ · 检索回执（evidence-auditor 出件，署名如实）
> 出件时点：2026-10-08
> 依据件：`letters/查理_glm_dualtrack_paper_sole_letter_2026_10_01.md` §三 甲组第 1–4 行（缺件定义逐字来源）
> 命名：无版本／阶段前缀（沿 PI 命名裁 `_主题_日期` 口径）；件内引用的存量件名含 `_v4_v5_` 前缀者，系盘上历史事实，沿论文 v0.3 §5.6 H-K 口径 ⛔ 0 解读为阶段名／版本号

---

## 零、口径与方法

### 0.1 依据件锚值复核（本轮实测，先实测后引用）

| 项 | 派工／回函所载 | 本轮实测 | 判定 |
|---|---|---|---|
| 回函 SHA-12 | `3c5059319ffe` | `3c5059319ffe`（全值 `3c5059319ffe8438e530614e98a42b0e71422b6874f3c652d6ad35852dfd1dd9`） | **MATCH** |
| 回函字节 | — | 13,105 B | — |
| 回函 mtime | — | 2026-10-02 00:19:43 | 早于本轮（10-08）⇒ 非快照后修正态 |

哈希一律 `Get-FileHash -Algorithm SHA256` 取 `[:12]`（⛔ 0 用内建 `hash()`；⛔ 0 复用他人自报值）。

### 0.2 三面定义与规模（本轮 `Get-ChildItem -Recurse -File -Force` 实测）

| 面 | repo 相对前缀 | 件数 | 目录数 | 字节 | `.git` 计数 |
|---|---|---|---|---|---|
| 主仓 | `deposon-repo/` | 1,715 | 110 | 52,866,188 | **0** |
| 副仓 | `deposon-sub/` | 503 | 40 | 34,821,170 | **0** |
| 归档区 | `_non_upload_local_archive/` | 39,244 | 19,460 | 1,371,319,650 | **0** |
| 合计 | — | **41,462** | — | 1,458,007,008 | **0** |

- **本地 git 全史不可得**：三面 `.git` 目录计数实测全为 0 ⇒ 如实登记「本地 git 史不存在」，⛔ 0 以「查不到 git」推论实体不存在。
- 归档区按 PI 纪律**只读 0 写入**（本轮全部为读与哈希计算）。

### 0.3 检索式（多式并行 · 单一式未命中 ≠ 不存在）

| 式 | 内容 | 覆盖 |
|---|---|---|
| ① R 编号 | `R-93`／`R-94`／`R-114`／`R-115` | 内容面 |
| ② 登记指纹 | `57aba2cd26a6`／`f011c29944b9`／`c386251d94d6`／`356bd6647796`（ignoreCase） | 内容面 ＋ **实体哈希面** |
| ③ 登记件实名 | `_d8_closeout_protocol_recompute_2026_09_30.md`／`_refcheck_hash_change_reference_recheck_2026_09_30.md`／`_v4_v5_t2_multimodel_verdict.md`／`_v4_v5_t2_multimodel_compare.json` | 件名面（逐面精确名） |
| ④ 近名／变体 | `multimodel`／`closeout`／`refcheck`／`d8_closeout` 通配枚举（跨三面） | 件名面 |
| ⑤ 盲扫（不依赖文件名） | 三面 **41,462 件全量** SHA-256[:12] 比对四个登记值 | 实体面 |
| ⑥ 远端 git 史 | GitHub 只读 API（HEAD 面 ＋ 路径全史面） | 远端面 |

### 0.4 判定分支（本回执所用五分支）

`FOUND_IN_REPO`（仓内实存）／`GHOST_REF_OUTSIDE`（引用在、实体在本面外）／`MISSING_TRUE`（三处均无＝真缺件）／`SAME_IDENTITY`（同哈希多份，不重复计数）／`CONFLICT`（同名异哈希）。

---

## 一、逐件 × 逐面 命中表

### R-93 · D8 收尾重算件（4.11/4.12 读数锚）

登记值（册）：`57aba2cd26a6` · 31,007 B ｜ 登记路径：`results/_d8_closeout_protocol_recompute_2026_09_30.md`

| 面 | 结果 | 证据 |
|---|---|---|
| 主仓 `deposon-repo/` | **FOUND_IN_REPO** | `deposon-repo/results/_d8_closeout_protocol_recompute_2026_09_30.md` · SHA-12 `57aba2cd26a6` · **31,007 B** · mtime 2026-09-30 22:57:20 ⇒ **登记值双项 MATCH（指纹＋字节）** |
| 副仓 `deposon-sub/` | **未命中**（实体 0） | 全量哈希盲扫 503 件 0 命中；精确件名枚举 `NOT_FOUND_BY_NAME`；内容面检索仅登记值引用 0 件 |
| 归档区 | **未命中**（实体 0） | 全量哈希盲扫 39,244 件 0 命中；精确件名枚举 `NOT_FOUND_BY_NAME` |
| 远端 git 史 | **未命中** | HEAD `72c5839`：`contents` 探测 `_september_workspace/results/_d8_closeout_protocol_recompute_2026_09_30.md` → `404`；`commits?path=` → `[]` |

### R-94 · 引用点复查件

登记值（册）：`f011c29944b9` · 33,625 B ｜ 登记路径：`results/_refcheck_hash_change_reference_recheck_2026_09_30.md`

| 面 | 结果 | 证据 |
|---|---|---|
| 主仓 `deposon-repo/` | **FOUND_IN_REPO** | `deposon-repo/results/_refcheck_hash_change_reference_recheck_2026_09_30.md` · SHA-12 `f011c29944b9` · **33,625 B** · mtime 2026-09-30 22:57:31 ⇒ **登记值双项 MATCH（指纹＋字节）** |
| 副仓 `deposon-sub/` | **未命中**（实体 0） | 全量哈希盲扫 503 件 0 命中；精确件名枚举 `NOT_FOUND_BY_NAME`；内容面仅命中引用登记值 0 件 |
| 归档区 | **未命中**（实体 0） | 全量哈希盲扫 39,244 件 0 命中；精确件名枚举 `NOT_FOUND_BY_NAME` |
| 远端 git 史 | **未命中** | HEAD `72c5839`：`contents` → `404`；`commits?path=` → `[]` |

### R-114 · `_v4_v5_t2_multimodel_verdict.md`

登记值：沿 L97 `C386251D94D6`（大写原样）｜ 登记路径：`results/_v4_v5_t2_multimodel_verdict.md`

| 面 | 结果 | 证据 |
|---|---|---|
| 主仓 `deposon-repo/` | **未命中**（实体 0） | 全量哈希盲扫 1,715 件 0 命中；精确件名枚举 `NOT_FOUND_BY_NAME`（仅有引用登记的伴生件） |
| 副仓 `deposon-sub/` | **GHOST_REF_OUTSIDE**（引用在、实体不在本面） | 实体：全量哈希盲扫 503 件 0 命中、精确件名 `NOT_FOUND_BY_NAME`；引用面：`deposon-sub/results/_track2_endpoints_probe_2026_09_23.json:50` 载 `"multimodel_verdict_v5": "C386251D94D6"`（大写原样）⇒ 登记引用在副仓、实体在归档区 |
| 归档区 `_non_upload_local_archive/` | **FOUND（实存于仓外归档面）** | `_non_upload_local_archive/results/_v4_v5_t2_multimodel_verdict.md` · SHA-12 `c386251d94d6` ⇒ 归一后与登记值 `C386251D94D6` **MATCH** · **4,264 B** · mtime 2026-09-23 12:32:15（字节与主仓 `deposon-repo/results/_v4_track2_multimodel_verdict_2026_09_23.md:154` 登记的 4,264 一致；回函／论文表字节位为「—」） |
| 远端 git 史 | **未命中** | HEAD `72c5839`：`contents` → `404`；`commits?path=` → `[]` |

### R-115 · `_v4_v5_t2_multimodel_compare.json`

登记值：沿 L97 `356BD6647796`（大写原样）｜ 登记路径：`results/_v4_v5_t2_multimodel_compare.json`

| 面 | 结果 | 证据 |
|---|---|---|
| 主仓 `deposon-repo/` | **未命中**（实体 0） | 全量哈希盲扫 1,715 件 0 命中；精确件名枚举 `NOT_FOUND_BY_NAME` |
| 副仓 `deposon-sub/` | **GHOST_REF_OUTSIDE**（引用在、实体不在本面） | 实体：0 命中；引用面：`deposon-sub/results/_track2_endpoints_probe_2026_09_23.json:49` 载 `"multimodel_compare_v5": "356BD6647796"`（大写原样） |
| 归档区 `_non_upload_local_archive/` | **FOUND（实存于仓外归档面）** | `_non_upload_local_archive/results/_v4_v5_t2_multimodel_compare.json` · SHA-12 `356bd6647796` ⇒ 与登记值 **MATCH** · **32,393 B** · mtime 2026-09-23 12:32:15（字节与主仓 `_v4_track2_multimodel_verdict_2026_09_23.md:153` 登记的 32,393 一致） |
| 远端 git 史 | **未命中** | HEAD `72c5839`：`contents` → `404`；`commits?path=` → `[]` |

### 1.5 同一性／冲突面（全量盲扫收口）

- **SAME_IDENTITY（重复计数风险）**：**不成立** —— 四个登记哈希在 41,462 件全量扫描中**各恰 1 份实体**，无第二份副本。
- **CONFLICT（同名异哈希）**：**0 例** —— 四个登记件名逐面精确枚举，各自只在单一面存在唯一实体。
- **MISSING_TRUE（三处均无＝真缺件）**：**四项均不成立**。

---

## 二、登记链溯源（供销项方交叉核验）

| 登记面 | 位置 | 逐字内容要点 |
|---|---|---|
| 回函 §三甲 1–2 | `letters/查理_glm_dualtrack_paper_sole_letter_2026_10_01.md:42-43` | R-93／R-94 册登记值＋「v0.3 轮实测仓内仍 0 命中」 |
| 回函 §三甲 3–4 | 同上 `:44-45` | R-114／R-115 件名＋「沿 L97 登记值」＋「git 全史无」 |
| 论文附录 part3 | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md:1183-1185, 1204-1205` | R-93/94/114/115 四行登记位（现标「缺件 · 待PI补」） |
| 论文 §5.6 | 同上 `:848` | R-114/115 缺件记述＋「git 全史无」＋H-K 命名纪律 |
| 论文 §一 | 同上 `:200` | R-93 判定「仓内工作树、git 全史与镜像清单三面均无踪迹，判定为 PI 盘上 09-30 落盘但未推仓」 |
| 线索册 v0.5 | `letters/_dualtrack_paper_clue_book_v0.5_2026_10_01.md:401-402` | R-93／R-94 登记行，自载「**2026-09-30 盘上终态实测**」（册侧已记存在） |
| L97 来源件 | `deposon-repo/results/_v4_track2_multimodel_verdict_2026_09_23.md:97` | 「详见 `_v4_v5_t2_multimodel_verdict.md` (SHA-12 `C386251D94D6`) 与 `_v4_v5_t2_multimodel_compare.json` (SHA `356BD6647796`)」——即回函所称 L97 |
| L97 字节对照 | 同上 `:153-154` | 两件字节 32,393 ／ 4,264 ⇒ 与本轮归档区实测字节一致 |
| 归档 manifest | `deposon-repo/results/_archive_manifest_non_upload_v2_2026_09_28.json:6082-6089`（v3 同 `:5287-5294`） | 以原相对路径 `results/<名>` 在册 ＋ `sha12` 两值 ⇒ 归档转移在册可核 |
| 台账 | `deposon-repo/results/_sub_artifact_ledger_history_r5_2026_10_01.md:132-133` | R-93／R-94 行在册（含末行出件方注记） |

**口径差异定位（如实登记，不代裁）**：

1. 「**未推仓**」与「**盘上不存在**」是两件事。本轮实测：R-93／R-94 实体在本地主仓 `deposon-repo/results/`，且 SHA-12＋字节与册登记值逐字一致；线索册 v0.5 自载该两件 09-30 已盘上终态实测。
2. R-114／R-115 实体在**归档区**（按 PI 归档纪律 ＝ 未上传区），归档 manifest 以原 `results/` 相对路径在册 ⇒ 与「远端 git 全史无」**互不矛盾**，二者描述的是不同面。
3. 回函／论文所载「仓内 0 命中／git 全史无」，本轮独立复核**属实**（远端 HEAD 4/4 `404`、路径全史 4/4 `[]`）；未覆盖的是 PI 本地主仓盘面。

---

## 三、综合结论

1. **四项均不构成 `MISSING_TRUE`（真缺件）**：实体在盘，且与登记值逐字一致——
   - R-93：SHA-12 `57aba2cd26a6` ＋ 31,007 B **双项 MATCH**
   - R-94：SHA-12 `f011c29944b9` ＋ 33,625 B **双项 MATCH**
   - R-114：SHA-12 `c386251d94d6`（归一对 `C386251D94D6`）**MATCH**；4,264 B 与 L97 来源件登记一致
   - R-115：SHA-12 `356bd6647796`（归一对 `356BD6647796`）**MATCH**；32,393 B 与 L97 来源件登记一致
2. **四项的位置面已定位**：R-93／R-94 ＝ 本地主仓在盘·未推远端；R-114／R-115 ＝ 归档区在盘·未上传（manifest 在册）。
3. **未命中面如实列出**：`deposon-sub/` 实体面四项均 0（仅 2 行登记值引用 ⇒ GHOST_REF_OUTSIDE）；远端 HEAD 面与路径全史面四项均 0。
4. **⛔ 0 代裁**：是否将四项由「待PI补」销项、如何改写回函与论文附录 R-93/94/114/115 行，**不属审计职权**，归 PI ／ verdict-keeper 处置；本件只呈报实测面与其口径差异，**0 假定任何一方读数已被复核**。

---

## 四、边界（0 编造 · 0 代裁 · 0 回改）

- **写入面**：本轮仅新增本件 1 件；⛔ 0 修改／回改任何既有件（含回函、论文、线索册）。
- **归档区**：只读检索与哈希计算，**0 写入**。
- **R4**：本件 0 载任何 key／endpoint／凭据（落盘后已跑 key 形态自扫）。
- **未实读**：本轮对四件**仅做指纹＋字节实测与件名／引用面检索**，⛔ 0 声称通读正文；R-93 承载的 4.11／4.12 读数本轮**0 复算**（⛔ 0 跑实验、0 出判定）。
- **远端方法边界**：GitHub API **未认证**（code search 返 `401` 不可用）；`commits?path=` 仅覆盖默认分支、按路径精确匹配，⛔ 0 追踪重命名／内容级历史 ⇒ 「远端全史无」为**路径面**证据，非内容面穷举。
- **本地 git**：三面 `.git` 计数 0 ⇒ 本地 git 史不可得，已如实登记，⛔ 0 以此推论实体不存在。
- **绝对路径**：本件所载盘面路径为 PI 侧本机工作区口径（`〔本地资料区〕/…`）；仓内引用一律以 `deposon-repo/` ／ `deposon-sub/` ／ `_non_upload_local_archive/` 相对前缀表述（沿 FTFB 引用前缀纪律）。

---

出件：evidence-auditor（agent-11335500b168）｜ 0 顶他方名头
本件自指回环处置：本件自身 SHA-12 在落盘后即固定，外部观测者请以 `Get-FileHash -Algorithm SHA256` 独立复算。
