# V4 每日收尾整理棒 · 清理登记（2026-09-28 首轮）

**出证｜Mavis 团队 worker（agent 名：worker · 本棒执行棒）｜2026-09-28**
**状态｜2 件经可恢复删除通道清走 · 8 件经登记留痕转移至 deposon-sub · 0 永久删除 · 0 绕过恢复机制 · 权威去向件 SHA-12 删除前后同值（0 触动）**

---

## 0. 授权来源

| 项 | 内容 |
|---|---|
| 授权字面 | PI 2026-09-28 18:08「每日收尾惯例整理：清噪声＋改清单＋**垃圾直接清理**……**已归档的垃圾同样清**」 |
| 垃圾判据 | **内容已入权威件且后续无需复核**的临时件 = 垃圾 ⇒ 直接清理 |
| 反向铁律 | **宁留勿错删**：证据件／留痕件／待复核件／内容未完整入权威件的临时件／可复算脚手架 ⇒ 不清；**拿不准 ⇒ 留＋登记** |
| 派工棒 | 「deposon V4 每日收尾整理棒｜worker｜2026-09-28 首轮｜PI 惯例授权」 |
| skill 调用 | **0 调用**（本棒无适用 skill，按派工单字面执行） |

**判定执行顺序（先证后删）**：① 未被权威件按路径引用 → ② 内容已入权威件（逐行/逐哈希实测）→ ③ 或可证完全重复 → ④ 或可证环境派生物。**四步任一不成立 ⇒ 留＋登记。**

---

## 1. 清理面 1：`.tmp/` 与 `.scratch_*`

### 1.1 已清走（2 件 · 131,262 B）

| # | 路径 | SHA-12 | 字节 | 分类理由（实测） |
|---|---|---|---|---|
| 1 | `.tmp/_v1p4_append_section.md` | `b26180083d88` | 32,219 | **段缓冲 .md ＋ 内容已入权威件**：实质行（≥12 字符）**261/261 逐字命中** `results/_v3_recheck_prereg_v1p4_2026_09_27.md`（单一去向 100% 覆盖，缺 0 行）；全仓权威件语料（`results/*.md`＋`results/*.json`＋`letters/*.md`，435 件）中**无任何件按路径引用它** |
| 2 | `.tmp/_r1_syntax_check.pyc` | `cbc1889083d0` | 99,043 | **环境派生物**：CPython 3.14 字节码（magic `2b0e0d0a`，header 检定），syntax-check 探针副产物；权威审计件 `results/_v4_trae_remaining_audit_2026_09_28.md:421` 自身即将其归类为「**验证用 scratch 件**」；派工单 §三.3 明文授权「.pyc … 随清（环境派生物）」 |

**删除通道实况**

| 项 | 实况 |
|---|---|
| 通道 | 本地 runtime **可恢复删除通道**（单一顶层 `rm -- <两件>`，相对路径） |
| 运行时回执 | `mavis-trash: moved to trash: '.tmp/_v1p4_append_section.md'` / `mavis-trash: moved to trash: '.tmp/_r1_syntax_check.pyc'` |
| 永久删除 / 绕过恢复机制 | **0 / 0**（未用绝对路径删除命令、未用内联脚本删除） |
| 删除后盘上复核 | 2 件均 `GONE`（`Test-Path` / `pathlib.exists` 双重确认） |
| 回收站可恢复性 | 是（回收站内原件 SHA-12 应仍为 `b26180083d88` / `cbc1889083d0`） |

**0 触动证明（权威去向件删除前后复测）**

| 件 | 删除前 SHA-12 / 字节 | 删除后 SHA-12 / 字节 | 结论 |
|---|---|---|---|
| `results/_v3_recheck_prereg_v1p4_2026_09_27.md` | `5294e4a2bd14` / 69,406 B | **`5294e4a2bd14` / 69,406 B** | ✅ **同值，清走 0 信息损失** |

- `.tmp` 余量：158 件 → **156 件**（清走 2，其余 156 件 0 读写 0 删除），总字节 4,194,787 B → **4,063,528 B**。
- **（§4.4 追加）** 转移 8 件后 `.tmp` 收口余量 = **150 件**。

### 1.2 `.scratch_*`：**0 触动**（2 目录）

| 目录 | 最后写入 | 判定 | 理由 |
|---|---|---|---|
| `.scratch_gamma_r1/` | 2026-09-28 17:36:05 | **留痕 · 不清** | 派工单**明文**指定「`.scratch_gamma_r1/` 明确为『供第三方复核』= 留痕不清」 |
| `.scratch_rj5/` | 2026-09-28 **18:10:37**（本棒执行期间仍在写入） | **在用 · 不清** | 实测该目录在本棒执行窗口内仍被活跃写入（`raw/p1706_02322.pdf.txt` 18:10:37），属**未收割的在跑棒**，非垃圾 |

### 1.3 逐件三分类计数（`.tmp/`）

**本轮首判时点**（删除后、转移前，`.tmp` = 156 件）

| 分类 | 件数 | 处置 |
|---|---:|---|
| **垃圾（已清）** | **2** | 可恢复通道清走 |
| **留痕**（可复算脚手架 / 引证件 / 内容未完整入权威件） | **154** | 0 触动（其中 6 件为本棒自产探针，**已于 §4.4 转移**） |
| **证据**（登记件/结果件本体） | **0** | 本棒未在 `.tmp/` 见到落盘权威产物本体 |
| 小计 | **156** | — |

**本轮收口时点**（`.tmp` 现存 = 150 件）

| 项 | 件数 | 说明 |
|---|---:|---|
| 垃圾（已清） | **2** | §1.1 |
| 已转移（§4.4） | **8** | 源侧余留 `_cleanup_*` ＝ NONE |
| 本棒新产后未计入首判的探针 | −2 | `_cleanup_transfer_scan*` 于首判后生成，随即一并转移 |
| **留痕（现存）** | **150** | 全部 0 触动 |

---

## 2. 清理面 2：归档垃圾 → **0 件可清（0 触动）**

### 2.1 `results/_archive_2026_09_20 / _archive_2026_09_21 / _archive_2026_09_24`（17 件 · 335,279 B）

> **派工单与盘上实况的命名出入（按字面执行并交代）**：派工单写 `results_archive_2026_09_24/` ／ `results_archive_2026_09_18/`；盘上实为 `results/_archive_2026_09_24`、`_archive_2026_09_21`、`_archive_2026_09_20`，**无 `_archive_2026_09_18`**（其 manifest 已并入 `_archive_2026_09_20/_archive_manifest_2026_09_18.json`）。本棒按**盘上实名为准**清理，并在此交代。

| 件 | 字节 | 判定 | 理由 |
|---|---:|---|---|
| `_archive_2026_09_20/_archive_manifest_2026_09_18.json`、`_archive_manifest_2026_09_20.json` | 4,712 / 35,682 | **留痕** | 归档凭证 manifest（勘误链引证件） |
| `_archive_2026_09_21/_archive_manifest_2026_09_21.json` | 17,353 | **留痕** | 同上 |
| `_archive_2026_09_24/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md.bak_2026_09_22_gB_post.md` | 113,508 | **留（**非**垃圾）** | 名义 `.bak`，但实测**在世新版并不存在于 `results/`**（`results/_v4_pi_decision_questionnaire_2026_09_21_v1.1.md` = **不存在**）⇒ 本件是**唯一副本**，非「已被新版本完全取代」的冗余件 ⇒ 反向铁律优先，**不清** |
| `_archive_2026_09_24/_final_verify.py._moved_20260924_1830` | 2,279 | **留（**非**垃圾）** | 名义旧版残留，但与在旁 `_final_verify.py`（2,307 B）**并非同源旧版**：逐行 diff 108 行差异，逻辑不同（前者＝L9/L11 post-hash 比对；后者＝`_v4_rootcause_upgrade_review.md` 等 5 件的 key-pats 扫描）⇒ 删则丢失 L9/L11 比对逻辑 ⇒ **不清** |
| `_archive_2026_09_24/` 其余 10 件（`l14_runner_v2.py` / `l14_small_batch.py` / `latency_test.py` / `_final_verify.py` / `_inspect_captions.py` / `_l11_run1.json` / `_l13_latency_test.py` / `_l14_checkpoint.json` / `_l14_records.json` / `_verify_worker_c.py` / `_volc_22cap_emb.py` / `_worker_openrouter_rag_run.py`） | 220,079 合计 | **留痕/证据** | 历史产物与可复算脚本，无一为缓存/日志/无追溯价值临时件 |

⇒ **归档面 0 件可清**。逐件实测后未发现派工单列举的「.bak 旧版本副本（已被取代）／缓存/日志类」。

### 2.2 `D:/私人资料/_non_upload_local_archive/`（1,696 件 · 338,433,933 B）→ **0 触动**

| 项 | 实测 | 判定 |
|---|---|---|
| 候选垃圾类体量 | `*.pyc` 69 件 / 1,326,272 B；`__pycache__` 目录 14 个；`cache/` 141 件 / 19,372,872 B；`logs/` 219 件 / 510,315 B | 均**未清** |
| **决定性理由** | `results/_archive_manifest_non_upload_2026_09_23.json` 是 **`path`＋`size`＋`sha12` 三字段哈希追踪 manifest**，其 `files[]` **逐条登记了该归档内 66 个 `.pyc`**（含 `__pycache__/fingerprint_v0.cpython-312.pyc` → `be6528f29c19`、`attacks/__pycache__/*.pyc` 等） | 清 `.pyc` ⇒ **破坏该 manifest 的 `file_count` 与逐件哈希可复算性** ⇒ 拿不准 ⇒ **留＋登记** |
| 次级理由 | 该路径在**工作区根之外**（工作区＝`deposon-repo/`）；铁律「**不擅动 workspace 外**」与派工单点名授权并存时，以「宁留勿错删」收口 | 未越界处置 |

---

## 3. 清理面 3：`__pycache__` 复扫 → **0 处可清**

| 位置 | 文件/字节 | 判定 | 理由 |
|---|---|---|---|
| `.scratch_gamma_r1/__pycache__` | 1 件 / 5,681 B | **不清** | 位于派工单明定「留痕不清」的目录内 |
| `.scratch_rj5/__pycache__` | 2 件 / 10,087 B | **不清** | 位于**执行中在跑棒**目录内（18:04–18:07 仍生成） |
| `_non_upload_local_archive/**/__pycache__`（14 目录） | 69 `.pyc` / 1,326,272 B | **不清** | 被 `_archive_manifest_non_upload_2026_09_23.json` 哈希追踪（§2.2） |
| `deposon-repo/` 其余目录 | **0 处** | — | 全仓复扫：除上述两处外**无任何 `__pycache__`／`.pyc`** |

---

## 4. 留痕清单（含**拿不准留档件**）

### 4.1 拿不准 ⇒ 留＋登记（**未清**，逐条附实测依据）

| # | 件 | SHA-12 | 字节 | 拿不准的具体原因（实测） |
|---|---|---|---:|---|
| 1 | `.tmp/_e48_c1.md` … `_e48_c5.md`（5 件） | `c2a814a90330`／`4d3cae4cbcc0`／`769c71475404`／`8143d01ca0e1`／`2f7ab971f691` | 40,964 | **内容未完整入权威件**：实质行命中 `results/*.md` 仅 1/18、3/36、**0/18**、1/76、**0/1**。系 doc-writer E-48 续号段缓冲，**尚未并入 `_v3_recheck_verdict_register_2026_09_27.md`** ⇒ 反向铁律「内容未完整入权威件的临时件」⇒ 不清 |
| 2 | `.tmp/_v16_full_decoded.txt` ＋ `.tmp/_v16_tail_dump.txt` | 双方 `fdfe315ff54a` | 174,424 ×2 | **可证完全重复**（同哈希同字节），但两路径**均被两份 PI 面委托信按行引用**：`letters/_letter_to_pi_upload_scoping_verdict_2026_09_26.md:143-144`、`letters/_letter_to_pi_upload_application_local_unique_overwrite_2026_09_26.md:115-116` ⇒ 删一件即令委托信所引路径落空 ⇒ **引证件 ⇒ 不清**（另：`_v4_day_inventory_2026_09_27.md` 按**盘上件数**计数） |
| 3 | `.tmp/_recheck_r1_run{A,B,C,D}.log`（4 件） | `68c85cf076d1`×2／`b15384cff9f0`×2 | 2,634×2／2,568×2 | 同上：**可证完全重复**，但 `_v4_day_inventory_2026_09_27.md:252` 与 `_v4_noise_cleanup_manifest_v4_2026_09_27.md:129,132` **按路径逐件列名**且明示「件数仍按盘上 22 计」⇒ 删件即破坏盘上计数对账 ⇒ 不清 |
| 4 | `.tmp/` 9 件陈旧机器日志（`_d4_relabel_run1`／`_recheck_r1_run1`／`_run_output`／`_v3r1_run1`／`_v3r1_run2` 等） | — | 19,903 合计 | 派工单列「陈旧机器日志」为**重点候选垃圾**，但**内容已入权威件无法证实**：① 逐行覆盖对 `results/*.md` 命中 0（控制台转储行式与权威件正文不同构）；② **SHA-12 反查实测**（全仓＋归档共索引 **3,007 件 / 2,651 个唯一 SHA-12**）显示其断言的哈希**并非全部解析到现存实体**（如 `_run_output.log` 的 `2CD0D493A0D1` 为 ghost）⇒ 缓冲件持有**盘上别处没有的信息** ⇒ 「内容未完整入权威件」⇒ 不清 |
| 5 | `.tmp/_r6_evidence.txt`／`_audit3b.txt`／`_audit_part4.txt`／`_r11_ctx.txt`／`_e3536.txt`／`_r10.txt`／`_gaps2.txt`／`_final_sha.txt` | — | 104,277 合计 | 同上：SHA-12 反查各含 ghost（如 `_r6_evidence.txt` 43 token 中 1 ghost；`_audit3b.txt` 46 中 6 ghost；`_audit_part4.txt` 39 中 4 ghost）⇒ 断言事实**并未全部现仍在盘** ⇒ 不清 |
| 6 | `.tmp/_l14v3_aggregated_10cells_v4.json` 等 5 件大 JSON | `66a9b8b3dabf` 等 | 2,899,817 合计 | 大体量聚合中间件，**是否为在世结果的唯一中间态未证实**，且 `.py` 生成脚本同在 ⇒ 可复算脚手架 ⇒ 不清 |
| 7 | `.tmp/_r1_scratch_{bom,corrupt_a,good}.json`（3 件） | `339de051e817`／`40a850e41f3e`／`ac623f06604c` | 17／15／14 | 权威审计件 `results/_v4_trae_remaining_audit_2026_09_28.md:421` 按路径列为「验证用 scratch 件」，且 `_r1_alarm_test.py` 复跑时**可能就地复用** ⇒ 留（合计仅 46 B，清之无益） |

### 4.2 其余留痕（摘要）

- `.tmp/` 92 件 `.py`（可复算脚手架）、20 件 `.json`（含 `_cpatomic_*_2026_09_28` 原子/登记件族、`_r4_key_scan_*` 无 key 自扫结果）、4 件 `.ps1`、其余 `.txt`/`.md`/`.jsonl` 缓冲 —— **一律 0 触动**。
- ~~本棒自产探针 6 件（33,492 B）~~ → **已于 §4.4 转移至 `deposon-sub`**（本行按 §4.4 关联修订）。

### 4.4 第 4 动作：转移两方向（PI 2026-09-28 18:21 澄清）

**授权字面**：整理惯例新增第 4 动作「转移两方向」——非垃圾但非主仓核心的件转移到 `deposon-sub`（**项目衍生件**）或 `D:/私人资料/_non_upload_local_archive/`（**不上传留档件**）；拿不准 → 留＋登记待问。核心判定链/预登记/勘误链/`results` 权威件仍 **0 转移 0 触动**。转移走登记留痕，**0 静默移动**。

**筛选口径**（本棒自产可复算脚本 `deposon-sub/tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py`）
候选池＝`.tmp/` 中 LastWriteTime 落在 **2026-09-28** 的件（实测 **65 件**）。逐件四问：
① 件名是否出现在 `letters/*.md`（PI 面委托材料）？② 是否出现在 `results/*.md`（**排除**两份「按名枚举 `.tmp/`」性质的清单：`_v4_noise_cleanup_manifest_v4_2026_09_27.md`、`_v4_day_inventory_2026_09_27.md`）？③ 是否在途链段（E-48 段缓冲）？④ 其余 → 转移候选。

#### 4.4.1 已转移（8 件 · 41,708 B）→ **`deposon-sub/tmp_movedout_2026_09_28/`**

| # | 旧路径（`deposon-repo/`） | 新路径（`deposon-sub/`） | SHA-12 | 字节 | 转移理由 |
|---|---|---|---|---:|---|
| 1 | `.tmp/_cleanup_probe_2026_09_28.py` | `tmp_movedout_2026_09_28/_cleanup_probe_2026_09_28.py` | `20bd0972fa00` | 2,556 | 本棒自产**过程登记副本/分类探针**，非交付中间面件；全仓 `letters/`＋`results/` **0 引用** |
| 2 | `.tmp/_cleanup_probe_out_2026_09_28.txt` | `tmp_movedout_2026_09_28/_cleanup_probe_out_2026_09_28.txt` | `75f9058f8a51` | 12,365 | 同上（探针输出，§1.3 覆盖数判据的原始凭据） |
| 3 | `.tmp/_cleanup_classify_2026_09_28.py` | `tmp_movedout_2026_09_28/_cleanup_classify_2026_09_28.py` | `efb57dc056f0` | 3,232 | 同上（三分类判据实现） |
| 4 | `.tmp/_cleanup_classify_out_2026_09_28.txt` | `tmp_movedout_2026_09_28/_cleanup_classify_out_2026_09_28.txt` | `e1f9db7e1cab` | 11,347 | 同上（三分类逐件判定表） |
| 5 | `.tmp/_cleanup_resolve_2026_09_28.py` | `tmp_movedout_2026_09_28/_cleanup_resolve_2026_09_28.py` | `57085a643c33` | 2,735 | 同上（SHA-12 反查探针） |
| 6 | `.tmp/_cleanup_resolve_out_2026_09_28.txt` | `tmp_movedout_2026_09_28/_cleanup_resolve_out_2026_09_28.txt` | `1d163e68ed25` | 1,257 | 同上（ghost 统计） |
| 7 | `.tmp/_cleanup_transfer_scan_2026_09_28.py` | `tmp_movedout_2026_09_28/_cleanup_transfer_scan_2026_09_28.py` | `97291768f38d` | 3,229 | 同上（第 4 动作分流筛选） |
| 8 | `.tmp/_cleanup_transfer_scan_out_2026_09_28.txt` | `tmp_movedout_2026_09_28/_cleanup_transfer_scan_out_2026_09_28.txt` | `04d99d651df9` | 5,017 | 同上（分流判定表） |

**转移登记件**：`deposon-sub/_movedout_manifest_2026_09_28.json` · **SHA-12 `6b557f005a40`** · 2,003 B · 8 条目。
**schema 沿用 09-21 既有惯例**（`deposon-sub/_movedout_manifest_2026_09_21.json`，363 条目，字段 `src`/`dst`/`sha12`/`size`/`archived_at`）。
**两处与 09-21 先例的有据偏离**：① `sha12` 用**小写**（派工单 §三铁律口径 `hexdigest()[:12]` 小写；09-21 先例为 UPPERCASE 359/363）⇒ **消费方须 case-fold**；② `src` 用纯字符串（09-21 先例为 PowerShell `Get-Content` 管道对象，含 `PSPath` 等噪声字段）。

**转移实况**：`.tmp` 文件 156 → **150 件**；转移源侧余留 `_cleanup_*` ＝ **NONE**；目标侧 8 件 SHA-12 与源侧移动前实测同值（**0 内容损失**）。转移为**移动**（非删除），未走回收站、未永久删除、未覆盖既有件（`-Force` 仅作用于本棒新建空目录）。

#### 4.4.2 未转移 · 拿不准 → 留＋登记待问（**57 件**，逐类附实测依据）

| 类别 | 件数 | 未转移的实测依据 |
|---|---:|---|
| **权威件按路径点名** | 约 46 | 逐件核实为**真引用**（非子串误命中）：`_cpatomic_verify_2026_09_28.json` 等 12 件被 `results/_v4_checkpoint_atomic_and_pycache_2026_09_28.md` 以「路径＋字节＋SHA-12」三列表格逐件登记；`_pkf34_*` 12 件被 `results/_v3_recheck_prereg_v1p4_2026_09_27.md` 逐件登记；`_trae_audit_part1.py`／`_r10.*`／`_r6_evidence.*`／`_audit*.txt`／`_gaps*.txt`／`_e3536.txt`／`_final_sha.*` 被 `results/_v4_trae_remaining_audit_2026_09_28.md` 列表；`_r1_alarm_test.py`＋`_r1_scratch_*.json`＋`_t15r2_checkpoint_warn.jsonl` 被同件列表；`_t15r2_checkpoint_warn.jsonl` 另被 `results/_v4_exec_surface_switch_2026_09_28.md` 指为**在跑告警日志活路径** ⇒ 移动即令权威件所引路径落空 ⇒ 不转移 |
| **权威件简写点名** | 4 | `_trae_audit_part2/3/3b/4.py`：被 `results/_v4_trae_remaining_audit_2026_09_28.md` 以**简写** `` `_part2.py`／`_part3.py`／`_part3b`／`_part4.py` `` 枚举（字面非全名，故全文检索未命中，但**语义确为点名**）⇒ 拿不准 ⇒ 留 |
| **在途链段** | 11 | E-48 续号链：`_e48_c1…c5.md`（内容**尚未**并入 `results/_v3_recheck_verdict_register_2026_09_27.md`，实测命中 0/18–1/76）＋ `_e48_apply.py`／`_e48_docwriter_*.py`／`_e48_probe_register.py`／`_e47_docwriter_count.py` ⇒ **移动会打断在跑 doc-writer 链** ⇒ 留 |
| **可复算脚手架（服务权威结果）** | 2 | `_run_d6_addendum_2026_09_28.py`（23,204 B）／`_run_d6b_addendum_2026_09_28.py`（31,468 B）：二者是权威结果 `results/_v4_pi_cot_v3_dataset_addendum_d6(_b)_2026_09_28.json` 的**唯一就地生成器**，0 引用；**移出主仓即丧失就地可复算性** ⇒ 依「可复算脚手架标留痕」精神留（回收代价 54,672 B，就地可复算优先） |
| **同族旁证** | 1 | `_cpatomic_dump_pyc_2026_09_28.py`（468 B）：0 引用，但其 12 个同族件全部被 checkpoint 件逐件登记 ⇒ 族内一致性优先 ⇒ 留 |

**⇒ 转移面实际释放 41,708 B；65 件今日衍生件中 8 件转移、57 件留档（0 静默移动，全部登记在案）。** 另：本棒**未**向 `_non_upload_local_archive/` 转移任何件 —— 该区被 `_archive_manifest_non_upload_2026_09_23.json` 哈希追踪（§2.2），**新增件会令该 manifest `file_count` 与逐件哈希失配**，须先重生成 manifest，故本轮**不动该区**（宁可少转，不破坏可复算性）。

### 4.3 超出本棒清理面 · 仅登记 **0 触动**

- `results/_v4_supp_l14v3_batch2_r2_models_probe.log`（1,260 B）＋ 同名 `.err.log`（**0 B**）—— 位于 `results/`（结果面，铁律「结果 JSON 0 触动」相邻），**不属派工单所列 3 个清理面** ⇒ 未清，建议下一轮单独立项。
- `verifier/` 下 18 件历史 `.log`（2026-08-23～09-10）—— verifier 为受保护组件且不属清理面 ⇒ 未清。

---

## 5. 清单与委托材料同步核 → **0 变更**

| 项 | 结论 |
|---|---|
| 清理面是否改变布局 | **仅在 `.tmp/` 临时区内清走 2 件**，0 移动（清理动作本身），0 改他件 |
| **第 4 动作转移是否改变布局** | **是**，8 件由 `deposon-repo/.tmp/` → `deposon-sub/tmp_movedout_2026_09_28/`，**旧→新逐件对账表见 §4.4.1**，并落 `deposon-sub/_movedout_manifest_2026_09_28.json`（SHA-12 `6b557f005a40`） |
| 委托材料（`letters/`）受影响 | **0**。全仓检索证实：无任何 `letters/*` 引用被清两件，亦无任何 `letters/*` 引用被转移 8 件；两份引用 `_v16_*` 的委托信所引路径**本棒 0 触动**（两件均在留痕清单 §4.1） |
| `results/` 权威件受影响 | **0 触动**。删除后＋转移后复测 6 件关键权威件 SHA-12 全部同值：`5294e4a2bd14`（prereg v1p4）／`1a8648083228`（trae audit）／`52b3dec13e06`（checkpoint）／`3bc852e0d48b`（exec switch）／`432989b507b8`（item04 closeout）／`e6552a19acb0`（BOM U-1） |
| 需同步改的清单/委托材料 | **0 件** ⇒ 登记「**0 变更**」（转移登记本身已在 §4.4 与 deposon-sub manifest 双处留痕） |
| **须向下轮/PI 交代的口径出入** | `results/_v4_trae_remaining_audit_2026_09_28.md:413,421` **按路径列名** `.tmp/_r1_syntax_check.pyc`（归为「验证用 scratch 件」）。本棒依派工单 §三.3「.pyc … 随清（环境派生物）」授权清走该件 ⇒ **该审计件所列路径现已失效**，属**已知且授权在先**的口径出入，在此明文交代；本棒**未改写该审计件**（0 触动） |

---

## 6. 铁律遵守

| 铁律 | 遵守情况 |
|---|---|
| 可恢复删除通道（单一顶层 rm） | ✅ 单一顶层 `rm -- <两件>`，回执 `mavis-trash: moved to trash` ×2 |
| 0 永久删除 / 0 绕过 | ✅ 未用绝对路径删除命令、未用内联脚本删除、未触碰回收站 |
| 转移 0 静默移动 | ✅ 8 件转移**先筛选建表、后移动、再复算 SHA-12**，旧→新对账表 §4.4.1 ＋ `deposon-sub/_movedout_manifest_2026_09_28.json` 双处留痕 |
| 核心判定链/预登记/勘误链/`results` 权威件 0 转移 0 触动 | ✅ 8 件转移源全部在 `.tmp/`，目标 `deposon-sub/` 新建空目录；`results/` 0 写 0 移 0 删（6 件关键权威件 SHA-12 转移后复测同值） |
| frozen / 预登记 / 判定链 / 勘误链 / rescript / executor / 结果 JSON 0 触动 | ✅ 清走 2 件均在 `.tmp/`；权威去向件 SHA-12 删除前后同值；`results/`、`letters/`、`verifier/` 0 写 0 删 |
| SHA-12 口径 `sha256(data).hexdigest()[:12]` 小写 | ✅ 全部哈希 `hashlib` 实测；**注**：项目件内引用惯用 UPPERCASE 展示，本登记件与 transfer manifest 一律小写（派工单口径）；09-21 先例 manifest 为 UPPERCASE，消费方须 case-fold（已在 §4.4.1 交代） |
| 署名如实 | ✅ 出证 = worker；未冒名 protocol-keeper / verdict-keeper / doc-writer / Trae code 等他方名头 |
| 不编造 | ✅ 全部哈希/字节/计数/回执/覆盖数/ghost 数/引用核实结论为本棒实测；探针自身的一次大小写缺陷已在本棒修正并重跑（`_cleanup_resolve` v2），未以修正后结果冒充首跑 |
| skill 若 not found | 不适用（**0 调用 skill**，按派工单字面执行） |

---

## 7. 本棒老实交代

1. **回收量偏小，如实报数**：`.tmp/` 156 件仅清走 **2 件 / 131,262 B（≈128 KB）**。原因是判据为「**内容已入权威件且后续无需复核**」，而 `.tmp/` 内绝大多数件（陈旧日志、审计缓冲、大 JSON、doc-writer 段缓冲）**经实测无法证明该前提**（逐行覆盖 0 命中；SHA-12 反查存在 ghost）⇒ 依「拿不准 ⇒ 留＋登记」全部留存。**未为凑回收量而放宽判据。**
2. **归档面 0 垃圾可清**：派工单点名的 `.bak 旧版本副本` 经实测**均在世新版不存在**（是唯一副本）或**并非同源旧版**（逻辑不同），故按反向铁律留。
3. **`_non_upload_local_archive` 0 触动**：该面 338 MB 中可清类合计约 21 MB，但被 `results/_archive_manifest_non_upload_2026_09_23.json` 逐条哈希追踪，清则破坏可复算性 ⇒ 登记不删，**建议 PI 单独立项**「manifest 重生成后清 .pyc/cache/logs」。
4. **本棒 0 产物**：除本登记件 ＋ 8 件探针/探针输出（**已按 §4.4 转移至 `deposon-sub/tmp_movedout_2026_09_28/`**）＋ 1 件转移登记 manifest（`deposon-sub/_movedout_manifest_2026_09_28.json`）外，**0 新增任何 JSON / 派生结果件**；2 件删除 0 触发既有件改动。
5. **新增待拍板项 0**：本棒为纯清理执行，0 产生口径分歧。
6. **已知授权在先的口径出入 1 处**（见 §5 末行）：`.tmp/_r1_syntax_check.pyc` 曾被 `results/_v4_trae_remaining_audit_2026_09_28.md` 按路径列名，本棒依 §三.3 授权清走，该审计件路径现已失效，本棒未改写该件。
7. **未触碰其他棒在制品**：`.scratch_rj5/` 在本棒执行期间仍被写入（18:10:37），本棒 0 读 0 写 0 删；`.scratch_gamma_r1/` 依派工单明文留痕。
8. **第 4 动作「转移两方向」登记待问项 4 类**（详见 §4.4.2，本棒**未自行处置**、留待 PI 拍板）：
   ① 权威件按**简写**点名的 4 件（`_trae_audit_part2/3/3b/4.py`）——是否视为已点名而禁转移？
   ② 权威结果 JSON 的**唯一就地生成器** 2 件（`_run_d6*_addendum_2026_09_28.py`，54,672 B）——「可复算性」是否高于「主仓去核心化」？
   ③ `_non_upload_local_archive` 承接转移需**先重生成** `_archive_manifest_non_upload_2026_09_23.json`，是否授权本棒或下一棒执行？
   ④ 转移 manifest 的 `sha12` 大小写口径：本棒从派工单铁律取**小写**，与 09-21 先例（UPPERCASE）不一致 —— 以何为准？

---

**清理登记出证｜Mavis 团队 worker｜2026-09-28 首轮**
**状态｜已清 2 件（可恢复通道，回执 ×2）· 已转移 8 件（登记留痕，deposon-sub manifest `6b557f005a40`）· 拦截 0 · 命中 0 · 0 永久删除 0 绕过 · 权威去向件 SHA-12 `5294e4a2bd14` 删除前后同值 · 留痕 150 件（`.tmp` 收口余量）· 归档面 0 垃圾可清 · 委托材料同步核 0 变更**
