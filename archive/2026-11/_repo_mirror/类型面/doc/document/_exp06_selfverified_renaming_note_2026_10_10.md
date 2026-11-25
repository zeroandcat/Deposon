# EXP-06 · 10-09 版 runner 同式修正 ＋ `self_verified_only` 键名改 · 勘正/注记件 · 2026-10-10 · 新名件

> **定位**：本件 ＝ PI 2026-10-10 11:06「轮 36」卡（`ask_90373daee410768058a3e852` step `runner_two`）裁「**两者都办（含键名改）**」之**落地承载**（勘误/迁移注记），配套交付：① 10-09 版同式修正副本 ＋ ② 键名勘正副本 ＋ 本注记件 ③。
> ⛔ **0 回改原件 `7c095c54fb99` 1 byte**（跑前＝跑后复测一致，见 §6）｜⛔ **0 回改前棒修正副本 `041525fd05a2`**｜⛔ **0 重跑任何实验载荷**（两副本 **0 运行**、未生成任何产出）｜⛔ **0 改任何既有产出件**（含 `33ad1c01f745`／`95f3f0957be8`）｜⛔ **0 网络**／⛔ **0 skill**／⛔ **0 LLM**／⛔ **0 读 key**。
> ⚠️ **0 判档（铁律）**：本件 **0 判任何档位**、⛔ **0 出 PASS/FAIL/KD**、⛔ **0 断「豁免成立否」** —— 判定归口＝verdict-keeper。

**授权锚**：PI 2026-10-10 11:06「轮 36」卡（`ask_90373daee410768058a3e852` step `runner_two`）逐字 ——「**两者都办（含键名改）**」
**前棒锚**：PI 2026-10-10 10:39「轮 34」卡（`ask_2901c721b5788ebbb00670a5` step `exp06_finds`）逐字 ——「**授权 runner 修正**」
**体例底本**：`results/_exp06_selfverified_runner_fix_note_2026_10_10.md`（`247398b687e6`）§7 残留登记第 1／2 项 ＝ 本棒两项之由来；配套修正副本 `_p_d_b3_merkle_22caption_runner_selfverify_fix_2026_10_10.py`（`041525fd05a2`）之四件套形式 ＝ 本棒逐项复刻之形
**勘误源**：`results/_exp06_supplement_four_gaps_2026_10_10.md`（`9f86cc5be8e9`）§2.3.3 ＋ §3 勘误登记 `E-EXP06-S3`
**规格源**：`results/_criterion_application_scope_prereg_2026_10_01.md`（`c4e3338619c6`）§3.3①②③④ ＋ §5 逐字段分类表 L173

**棒序**：`worker` · EXP-06 修正/勘正/同步件 · 2026-10-10。

---

## §1 交付物与指纹（逐件实测）

| # | 件 | 路径 | SHA-12 | bytes | 行 | BOM | CRLF |
|:-:|---|---|---|:-:|:-:|:-:|:-:|
| ① | **10-09 版同式修正副本** | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py` | `341b6726ac4e` | 33,994 | 646 | NO | 0 |
| ② | **键名勘正副本**（修正 ＋ 改名 合一） | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py` | `cd43c41716f0` | 35,321 | 661 | NO | 0 |
| ③ | **勘正/注记件**（本件） | `results/_exp06_selfverified_renaming_note_2026_10_10.md` | 见**回执**（自指不可内嵌） | — | — | NO | 0 |
| — | 工具件 · **0 属证据面** | `.tmp/_exp06_1009fix_build_2026_10_10.py` | `e5acb3c0bca2` | 29,412 | 453 | NO | 0 |
| — | 工具件 · **0 属证据面** | `.tmp/_exp06_1009fix_verify_2026_10_10.py` | `47fdf9673acc` | 7,817 | 167 | NO | 0 |
| — | 工具件 · **0 属证据面** | `.tmp/_exp06_1009fix_lnref_2026_10_10.py`／`…_lnref2_…py` | `9c7096147878`／`3ff21d556306` | 1,508／1,505 | 27／35 | NO | 0 |

**落前 0 命中确认**：① ② 两新名件落前 `Test-Path=False` 且 `glob` 0 命中（构建器内置 `assert not p.exists()` 硬门，见 §4‑13）｜③ 同。

**读盘锚（逐件复算一致 · 本棒跑后复测）**

| 锚 | SHA-12 | 路径 | 本棒角色 |
|---|---|---|:-:|
| 原件（本棒修正对象） | `7c095c54fb99` | `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_v0_4_2026_10_09.py`（21,826 B · 474 行） | ⛔ **0 回改** |
| 09-29 版原件 | `de16bc002198` | `..._runner_v0_4_2026_09_29.py`（20,322 B · 453 行） | ⛔ **0 触及**（前棒已修） |
| 前棒修正副本（**体例底本**） | `041525fd05a2` | `..._runner_selfverify_fix_2026_10_10.py`（31,457 B · 616 行） | ⛔ **0 回改** |
| 10-09 版产出（读数面） | `95f3f0957be8` | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json`（21,176 B） | ⛔ **0 改**；读数 0 变 |
| 10-09 版索引产出 | `74b27393574f` | `corpus/v20/index_v3_2026_10_09.json`（24,837 B） | ⛔ **0 改** |
| 09-29 版产出（读数面） | `33ad1c01f745` | `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json`（20,398 B） | ⛔ **0 改**；读数 0 变 |
| 09-29 版索引产出 | `3ba2449cf986` | `corpus/v20/index_v3_2026_09_29.json` | ⛔ **0 改** |

**两副本之输出路径（新名 · 本棒 0 生成 · `Test-Path` 实测 False）**
- ① `corpus/v20/index_v3_selfverify_fix_1009base_2026_10_10.json` ／ `results/deposon_p_d_b3_merkle_22_caption_selfverify_fix_1009base_2026_10_10.json`
- ② `corpus/v20/index_v3_selfverify_rename_1009base_2026_10_10.json` ／ `results/deposon_p_d_b3_merkle_22_caption_selfverify_rename_1009base_2026_10_10.json`

⇒ 四者均为新名，⛔ **不可能覆写** 10-09／09-29 两版之任何既有产出（原件输出路径已在副本内改写，见 §2.3）。

---

## §2 ① 10-09 版同式修正（沿 09-29 版之修正体例）

### §2.1 缺陷实体 · 逐字（原件 `7c095c54fb99` L246‑L248）

```python
    for c in per_caption:
        c["chain"]["link_verified"] = rewalk_ok
        c["chain"]["self_verified_only"] = True      # ← 硬写：无条件字面量
```

**语义上下文（原件 L236‑L245 逐行核）**：`rewalk_ok` 为**真求值**变量 —— 初值 `True`（L238），任一 `node_state` 不符即翻 `False`（L241‑L242），再与重导 `rw_ext1`／`rw_root` 比对并 AND（L245）。
**故**：`link_verified = rewalk_ok` ✅ 真求值；紧邻之 `self_verified_only = True` ❌ **不读 `rewalk_ok`、0 任何比较、0 任何探测** ⇒ **该位之 `true` 值并非由任何验证面求出**。
**与 09-29 版之关系**：L246‑L248 与 09-29 版 L230‑L232 **逐字同构**（两版该循环体完全一致）⇒ 同一缺陷、同一修正形式、同一规格依据。

### §2.2 规格要求（`c4e3338619c6` §3.3② · 逐字）

> **② 全 `true` 独立验证件** ｜ 最小落面要求：**全 `true` 字段须附独立验证件（可核、0 与被验证件同源）；0 预置为 `true`** ｜ 缺位后果：**豁免不成立 ⇒ 回落受门**

配套 §3.3①：**取值语义声明**（逐字段声明**置位者／置位时机／依据件**三要素）。配套 §3.3④ 之同族纪律：**0 记为通过、0 静默**。

### §2.3 修正内容（唯一语义改动 ＋ 身份改写，严格分离登记）

**语义修正 · 1 处站点（原 L248 → ① 副本 L373）· 唯一**

| 项 | 行（原件 → 副本） | 原字面 | 修正字面 |
|:-:|---|---|---|
| ★ | **L248 → L373** | `c["chain"]["self_verified_only"] = True` | `c["chain"]["self_verified_only"] = bool(rewalk_ok) and not indep_verified` |

**配套新增站点（非独立改动面，为使该修正成立所必需，逐项登记 · 行号为 ① 副本）**

| # | 副本行 | 内容 | 为何必需 |
|:-:|---|---|---|
| 1 | L367‑L368 | `indep = probe_independent_evidence(BASE, GENERATOR)`／`indep_verified = indep["status"] == "verified"` | `indep_verified` 之定义源；⛔0 则修正式无变量可依 |
| 2 | L215 | `INDEP_VERIFY_DECL = None` | §3.3②「须附独立验证件」之**声明位**（本副本 0 声明 ⇒ status=`not_declared`） |
| 3 | L218‑L264 | `probe_independent_evidence()`（47 行） | 独立验证面之**运行期实测**（在位／哈希／异源三判） |
| 4 | L364‑L392 | 5b 段：随件声明三要素 ＋ `independent_verification_ref`／`_status`／`independence_deficiency_alarm` | §3.3① 三要素落面 ＋ §3.3②「附件」指针 ＋ §3.3④ 同族「0 静默」 |
| 5 | L533‑L555 | 顶层 `independence_verification` 节（23 行） | 布尔位**全局**判定面（三要素 ＋ 探测记录 ＋ burden 满足与否） |
| 6 | L577‑L582 | `runner_fix_notice`（6 行） | 产出件自述「由修正版副本生成」，供后续读者溯源 |

**身份改写 · 0 语义影响（必要性逐项给据）**：`DATE`（原件 `2026-10-09` → 副本落盘日）／`GENERATOR` → 副本自身路径／`task_id` → `V3X-C5B-RUNNER-2026-10-10-A1-FIXCOPY-1009`／两组输出路径常量（4 行 → 新名）＋ 段注释 ／docstring 件名与 out件名 ／`PINNED` 追加 3 件 pin（10-09 版两产出 ＋ 其原件；**0 覆写既有产出须 pin**，沿 10-09 原件 L82‑L86 同款纪律）。
**最硬之必要性**：输出路径若不改写，本副本一跑即覆写 `95f3f0957be8`／`74b27393574f` ⇒ 违反 0 回改。

**0 改动面（逐项明示）**
- **常量**：`K_COMPONENTS=3`／`PLANES_PER_DIM=6`／`N_PLANE=18`／`CODE_LEN_BIT=18`／`HEX_WIDTH=5`／`D_OVER_2=9.0`／`LSH_SEED=42` —— **一字未动**。
- **10-09 版之独有新增（相对 09-29 版）**：`PROTOCOL_VERSION`／`PROTOCOL_VERSION_AXIS` 两常量 ＋ `index_v3["protocol_version"]`／`["protocol_version_axis"]` 协议版本键面 ＋ `results["protocol_version"]` —— **一字未动、0 回退**（本棒只增 0 减：10-09 版既有能力全部保留）。
- **`ANCHORS`／`PINNED` 原 8 项／`SPEC_REF_*`／`ANCHORS_REF`／`FORBIDDEN_TOKENS`／`SPEC_REF_V04` 之「待 doc-writer 棒 2b 新增」字面** —— 一字未动。
- **链式构造四式（L227‑L231）、自证复走段（L236‑L245）** —— 一字未动。
- **索引件装配段／`diff_registration` 段／`decision_lines_36_substitute` 段／`cross_source_2model_087` 段／收尾三写与红线段** —— 一字未动。
- **该位赋值站点数不变**：原件 1 处 → 副本 1 处（仅值表达式改）。

### §2.4 逐行 diff 登记（机器复算 · `difflib.SequenceMatcher`；副本落位行号**逐条实测**）

**① 10-09 版同式修正副本（原 474 行 → 646 行）**

| 区 | tag | 原件锚 | 副本落位 | 原行数 | 副本行数 |
|:-:|---|---|---|:-:|:-:|
| 1 | insert | L1 后 | L2‑L57 | 0 | **56** |
| 2 | insert | L3 后 | L60 | 0 | 1 |
| 3 | replace | L5‑L8 | L62‑L65 | 4 | 4 |
| 4 | replace | L49 | L106 | 1 | 1 |
| 5 | replace | L72‑L75 | L129‑L133 | 4 | 5 |
| 6 | insert | L88 前 | L146‑L149 | 0 | **4** |
| 7 | replace | L94 | L156 | 1 | 1 |
| 8 | insert | L148 后 | L211‑L266 | 0 | **56** |
| 9 | insert | L246 前 | L364‑L369 | 0 | **6** |
| 10 | replace | **L248** | L372‑L392 | **1** | **21** |
| 11 | replace | L302 | L446 | 1 | 1 |
| 12 | insert | L388 后 | L533‑L555 | 0 | **23** |
| 13 | insert | L409 后 | L577‑L582 | 0 | **6** |

**② 键名勘正副本（原 474 行 → 661 行）**

| 区 | tag | 原件锚 | 副本落位 | 原行数 | 副本行数 |
|:-:|---|---|---|:-:|:-:|
| 1 | insert | L1 后 | L2‑L41 | 0 | **40** |
| 2 | insert | L3 后 | L44 | 0 | 1 |
| 3 | replace | L5‑L8 | L46‑L49 | 4 | 4 |
| 4 | replace | L49 | L90 | 1 | 1 |
| 5 | replace | L72‑L75 | L113‑L117 | 4 | 5 |
| 6 | insert | L88 前 | L130‑L136 | 0 | **7** |
| 7 | replace | L94 | L143 | 1 | 1 |
| 8 | insert | L148 后 | L198‑L253 | 0 | **56** |
| 9 | insert | L246 前 | L351‑L356 | 0 | **6** |
| 10 | replace | **L248** | L359‑L379 | **1** | **21** |
| 11 | replace | L302 | L433 | 1 | 1 |
| 12 | insert | L388 后 | L520‑L569 | 0 | **50**（迁移注记 27 ＋ `independence_verification` 23） |
| 13 | insert | L409 后 | L591‑L597 | 0 | **7** |

- **改动区数：① 13 ｜ ② 13**（区数与 09-29 版修正副本之 13 同数，体例一致）
- **唯一语义改动**：两副本之区 **10**（原 L248 单行 → 副本 21 行）；其余 12 区 ＝ 头块插入 ＋ 身份改写 ＋ 配套新增站点。
- 区 9 ＋ 区 10 之关系：区 9 ＝ 5b 段头 ＋ 两行求值准备（6 行）；区 10 ＝ 循环内该位之求值 ＋ 三要素声明 ＋ 附件指针 ＋ 状态 ＋ 警报（21 行，含原 L246‑L247 之 `for`／`link_verified` 两行之对齐命中）。
- ② 与 ① 之差（**构成不同，非逐行对应**）：头块 **40 行 vs 56 行**（① 载「键名 0 改 ＋ 为何不改名」说明段，② 载「张力论证 ＋ 键名拟案 ＋ 偏离登记 ＋ 0 双写」段）＋ 区 12 多 **27 行**（`key_rename_migration`）＋ 区 13 多 **1 行**（改名溯源句）＋ 身份段 `task_id`／输出名之字符级差异。⛔0 将两件头块当作同文比对。

---

## §3 ② 键名改：拟案 ＋ 论证 ＋ 执行形式 ＋ 影响面 ＋ 迁移注记

### §3.1 键名与规格之张力（缺陷实体 · 定义层）

| 项 | 内容 |
|---|---|
| **旧键名** | `self_verified_only` —— 语义为「**验证仅由自证支撑**」 |
| **所受规格** | `c4e3338619c6` §3.3②「**全 `true` 字段须附独立验证件**（可核、0 与被验证件同源）；0 预置为 `true`」 |
| **张力** | 若该位读 `true`，按**键名自身定义**即「验证仅由自证支撑」⇒ **无独立验证件可附**；而 §3.3② 要求全 `true` 须附该件 ⇒ **一个按定义恒不可能满足其自身所受配套校验的字段** |
| **根因（棒方判断 · 已给据）** | 旧键名把**证据依据面（basis）**与**豁免宣称面（claim）**压在同一个键名里：既被读作「自证已通过」之断言，又须承担「全 `true` 须附独立件」之负担 ⇒ 0 稳定读法 |
| **前棒处置** | `247398b687e6` §7‑2：**0 代裁**「改键名／拆位／改语义」，只落「可求值化 ＋ 可核化 ＋ 不静默」三项；**是否进一步改键名须 PI 另裁** ⇒ 本棒依轮 36 卡裁执行 |

### §3.2 新键名拟案（4 候选 ＋ 推荐 · 逐条论证）

| # | 候选键名 | 语义 | 采纳 | 论证 |
|:-:|---|---|:-:|---|
| **A** | **`verification_basis_self_rewalk_only`** | 「本记录之验证**依据**仅为自证复走」 | ✅ **推荐** | ① **纯描述位**：只陈述**证据依据**，⛔0 承担「已附独立验证件」之宣称 ⇒ §3.3② 之负担改由 `independence_burden_satisfied`／`independence_deficiency_alarm` **二位独立承载**，与「依据面」解耦；② **与新值表达式逐字自洽**：`bool(rewalk_ok) and not indep_verified` 恰好读作「自证复走成功 **且** 独立验证面未取得 verified」＝ 依据仅自证；③ **0 引入新事实**（不改读数、不改语义边界，仅改称呼）；④ 键名自带 `basis` 词根 ⇒ 读者**结构上**不会再把它当「已获豁免」之断言位读；⑤ 命名合规（`snake_case`、无阶段号） |
| B | `self_rewalk_only_no_independent_artifact` | 「仅自证复走 ＋ 无独立验证件」 | ❌ 备选 | 语义最直白，但把 burden **未满足**写成**键名之恒常事实** ⇒ 日后独立件在位、值翻 `false` 时**键名本身即失准**（值诚实 ＋ 名不诚）。仅在 PI 认为「直白性优先于长久语义」时取用 |
| C | `self_verified_without_independent_artifact` | 「已自证而无独立件」 | ❌ 备选 | 以 `self_verified` 为前缀，**仍易被读作「自证已通过」之断言位** ⇒ 只换了措辞、**未消解**「断言 vs 负担」之结构问题；且 `self_verified` 与既有 `link_verified`（真求值位）形近 ⇒ **易生误挂**（新增误读风险） |
| D | `self_verified_only_flag` | 旧名 ＋ 布尔后缀 | ❌ **不建议** | 最小改动、**⛔0 消解张力**（仍宣称「仅自证」而 §3.3② 要求全 `true` 附件）⇒ 缺陷原样留存；仅作对照以证明「改名 ≠ 加后缀」 |

**推荐结论（一句）**：`self_verified_only` → **`verification_basis_self_rewalk_only`**（候选 A）—— 理由：把该位由「豁免宣称位」改为「证据依据描述位」，令 §3.3② 之独立验证件负担**另由 alarm/burden 二位显式承载**，从而在不改动任何读数、不新增任何事实的前提下消解定义层张力；**值表达式 `bool(rewalk_ok) and not indep_verified` 0 变动**。

### §3.3 执行形式（沿「另立勘正/修正副本」体例）

| 项 | 处置 |
|---|---|
| **形式** | **另立勘正副本 ②**（`_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py`）—— ⛔ **0 回改** ① 修正副本、⛔ **0 回改** 既有产出件（`33ad1c01f745`／`95f3f0957be8`）、⛔ **0 回改** 原件 |
| **为何 ① 不直接改名** | ① 与 09-29 版修正副本（`041525fd05a2`）**schema 完全一致** ⇒ 读数面可比、且**保留 `c4e3338619c6` §5 逐字段分类表所锁之键名**（该表 L173「随本件生效即锁」）；改名后果 ⛔0 由棒方独自承担（见 §3.5 偏离登记）⇒ ② 与 ① 分离，PI 若另择键名**只须改 ② 一件**，不必重出 ① |
| **② 之改动面** | **13 区**（与 ① 同数）：语义改动区 10 ＝ 键名替换（**值表达式 0 变**，站点 ② L360）；另加 `key_rename_migration` 迁移注记节（**L520‑L546**，27 行）＋ 头块 40 行（含张力论证 ＋ 偏离登记 ＋ 0 双写声明）＋ 区 13 之改名溯源句（7 行） |
| **⛔0 双写** | ② **0** 同时输出旧键（双键并存 ＝ schema 歧义 ＋ 0 单一事实源）⇒ AST 级实测：② 之 `self_verified_only` **赋值站点 ＝ 0**（§4‑2） |
| **值表达式** | **0 变动**：`bool(rewalk_ok) and not indep_verified`（AST 级实测 ② L360 站点逐字一致） |
| **产出件内生迁移注记** | ② 顶层落 `key_rename_migration` 节（27 行）：载旧/新键名、双方语义、`value_expression_unchanged=true`、`dual_write=false`、读旧件须知、`spec_divergence` 偏离登记、授权锚 |

### §3.4 下游引用影响面（**全仓逐件实测** · 旧键名命中 **35 件**）

**A · 源码面（5 件 · ⛔0 改 3 件 ＋ 本棒新出 2 件）**

| 件 | 命中 | 处置 |
|---|:-:|---|
| `..._runner_v0_4_2026_10_09.py`（`7c095c54fb99`） | 1（L248） | ⛔ **0 回改** |
| `..._runner_v0_4_2026_09_29.py`（`de16bc002198`） | 1（L232） | ⛔ **0 回改**（前棒已修其产出） |
| `..._runner_selfverify_fix_2026_10_10.py`（`041525fd05a2`） | 14 | ⛔ **0 回改**（前棒件；键名改面 ② 承担） |
| ① 本棒新出 | 15 | 新名件 |
| ② 本棒新出 | 9（全部为**溯源/迁移/偏离登记**之文档引用；**AST 赋值 0**） | 新名件 |

**B · 工具面（`.tmp/` · 12 件）—— ⛔0 改；旧读法须迁（见 §3.5‑T1）**

| 件 | 命中 | 旧读法实体 |
|---|:-:|---|
| `u04_1_chain_verify.py` | 1 | `for k in ['link_verified', 'self_verified_only']` |
| `c5_guard_minmaxstd_2026_10_01.py` | 2 | `c["chain"]["self_verified_only"]` 取值列 |
| `k_v3df_0_1_four_readings_2026_10_09.py` | 4 | `pc_chain("self_verified_only")` 读数列 |
| `vk_v3df_0_1_verify_2026_10_09.py` | 2 | `p["chain"]["self_verified_only"]` |
| `vk_v3df_0_1_agree.py` | 2 | 字段名映射表项 |
| `u04_1_make_data.py` | 3 | `bv('self_verified_only')` 布尔列 |
| `exp06_supplement_probe_2026_10_10.py` | 2 | `cnt(lambda c: c["chain"][...])` |
| `exp06_independent_json_gen_2026_10_10.py` | 5 | 缺陷登记/读数生成 |
| `_exp06_fixcopy_verify_probe_2026_10_10.py` | 7 | 前棒静态探针 |
| `vk_v3df_0_1_verify_out_2026_10_09.json` | 4 | 探针产出 |
| 本棒 `_exp06_1009fix_build_…py` | 15 | 本棒构建器（工具件 0 属证据面） |
| 本棒 `_exp06_1009fix_verify_…py` | 1 | 本棒探针（工具件 0 属证据面） |

**C · 产出/读数件（`results/*.json` · 6 件 · ⛔0 改）**

| 件 | 命中 | 处置 |
|---|:-:|---|
| `deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json`（`33ad1c01f745`） | **22** | ⛔ **0 回改**；仍载**旧键名** ＋ 22/22 `true` |
| `deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json`（`95f3f0957be8`） | **22** | ⛔ **0 回改**；仍载**旧键名** ＋ 22/22 `true` |
| `c5_guard_minmaxstd_readings_2026_10_01.json` | 1 | ⛔ 0 改（读数件 ＋ 自校验链） |
| `_k_v3df_0_1_four_readings_2026_10_09.json` | 3 | ⛔ 0 改 |
| `_u04_1_exemption_precondition_verification_2026_10_09.json` | 2 | ⛔ 0 改 |
| `_exp06_independent_check_2026_10_10.json` | 5 | ⛔ 0 改 |
| （旁证）`corpus/v20/index_v3_2026_10_09.json` | **0** | index_v3 件**不含** `chain` 面 ⇒ 该键名不涉入 |

**D · 规格/判定/登记件（`results/*.md` · 16 件 · ⛔0 改）**

| 件 | 命中 | 处置与理由 |
|---|:-:|---|
| **`_criterion_application_scope_prereg_2026_10_01.md`（`c4e3338619c6`）** | **1（L173）** | ⚠️ **偏离源** —— §5 逐字段分类表**「随本件生效即锁」**，L173 逐字锁 `chain.self_verified_only` 之名 ＋ 配套位。⛔ **0 回改**；**是否发规格附录/勘误件归 PI / protocol-keeper**（§7‑2） |
| `_exp06_supplement_four_gaps_2026_10_10.md` | 9 | ⛔ 0 改（勘误源，历史记录 ＝ 旧键名之**当时事实**） |
| `_exp06_selfverified_runner_fix_note_2026_10_10.md` | 15 | ⛔ 0 改（前棒件；本件承接其 §7‑1／§7‑2） |
| `_exp06_kcf4_check_bit_landing_2026_10_10.md` | 4 | ⛔ 0 改 |
| `c5_guard_0_1_recheck_verdict_2026_10_01.md` | 6 | ⛔ 0 改（**判定件**：⛔0 以新键名覆写其历史判读面） |
| `c5_guard_minmaxstd_report_2026_10_01.md` | 1 | ⛔ 0 改 |
| `_k_v3df_0_1_four_readings_2026_10_09.md` | 3 | ⛔ 0 改 |
| `_k_v3df_0_1_readings_verdict_2026_10_09.md` | 3 | ⛔ 0 改（**判定件**） |
| `_k_cf_4_effectivity_register_2026_10_09.md` | 1 | ⛔ 0 改 |
| `_k_cf_4_low_cardinality_recure_2026_10_09.md` | 1 | ⛔ 0 改 |
| `_u04_1_exemption_precondition_verification_2026_10_09.md` | 1 | ⛔ 0 改 |
| `_u_v04_01_criterion_scope_determination_2026_10_01.md` | 3 | ⛔ 0 改 |
| `_mini_round_3_decisions_register_2026_10_01.md` | 1 | ⛔ 0 改 |
| `_v3_02_override_register_2026_10_09.md` | 1 | ⛔ 0 改 |
| `_questionnaire_cards_intake_register_supplement_4_2026_10_10.md` | 2 | ⛔ 0 改（含轮 34 卡原文 ＝ 授权锚） |
| `_ea_audit_batch_vk_2026_10_09.md` | 1 | ⛔ 0 改 |

> **0 改之总原则**：C／D 两面**一律 0 回改** —— 其字面为**历史事实之记录**，改名覆写之即**伪改历史**；正确做法为**另立新件**（本件 ③ ＋ ② 即该另立面）。

### §3.5 迁移注记（旧→新之三轨路径 · 逐轨给据与归属）

| 轨 | 面 | 迁移动作 | 现状与归属 |
|:-:|---|---|---|
| **T1** | **旧读法工具**（B 面 7 件真读件） | 读取键改为**兼容双读**：`c["chain"].get(NEW_KEY, c["chain"].get(OLD_KEY))`（⛔0 以 `or` 短取 ＝ `false` 值会被吞）；或按产出件 `generator` 分派读法 | ⛔ **本棒 0 代改**（非本棒所有权 ＋ 0 回改既有件）⇒ **候派**：读法迁移须另派一棒，或 PI 裁「暂不改读法」⇒ 见 §7‑3 之风险登记 |
| **T2** | **产出侧** | 本棒 ② 之产出用**新键名**；⛔ **0 双写**、⛔ **0 回改**既有产出 | ✅ 本棒已落（② ＋ `key_rename_migration` 节 ＋ `spec_divergence` 登记） |
| **T3** | **规格侧** | `c4e3338619c6` §5 逐字段分类表 L173 之锁定键名 | ⛔ **未落 · 归 PI / protocol-keeper**：改名与「随本件生效即锁」之表产生**形式偏离**（`spec_divergence` 节已逐字登记）。是否发附录/勘误件**须 PI 另裁** |

**生效条件（如实登记 · ⛔0 夸大）**
- ① ② **均 0 运行** ⇒ 盘上**无**任何新产出 ⇒ **本棒之键名改对任何在盘读数 0 影响**。
- 日后若以 ② 重跑：新产出之该位键名为**新键**，值 ＝ `bool(rewalk_ok) and not indep_verified`（当 `INDEP_VERIFY_DECL` 仍为 `None` 时读 `true`，读数与现状同 ＋ `independence_deficiency_alarm=true` 显式亮起）；**此时 T1 未迁则旧读法工具对该新产出 `KeyError`** ⇐ 此即 §7‑3。
- 若日后填入**异源**独立验证件并重跑 → `independence_verification_status` 转 `verified` → `independence_burden_satisfied=true` → 该位**翻 `false`**（**设计意图之诚实表现**，⛔ 非读数错误）。
- ⚠️ 重跑会产出**新名产出件（新指纹）**；既有 `33ad1c01f745`／`95f3f0957be8` **不受影响**，⛔0 需翻案。

---

## §4 验证（静态级 · **0 运行本棒两副本**）

| # | 项 | 方法 | 结果 |
|:-:|---|---|---|
| 1 | 语法/语义可编译 | `ast.parse` ＋ `compile()` | ✅ ① ② **双 PASS** |
| 2 | **硬写残留**（AST 级） | 遍历 `ast.Assign` 之 `Subscript` 目标键 | ✅ 原件 `self_verified_only` L248 ＝ `True`；**① L373** ＝ `bool(rewalk_ok) and (not indep_verified)`；**② L360**（新键）＝ 同式；**② 旧键赋值站点 ＝ 0**（⛔0 双写成立） |
| 3 | 硬写字面量站点（AST 级） | 同上，取 `ast.Constant` 值节点 | ✅ ① **0 处** ／ ② **0 处** |
| 4 | 字面量残留（全文计数） | 计数 `"self_verified_only"] = True` | ① 命中 **1** 处 ＝ **L21 头块之「文档引述」**（沿 09-29 版探针之审计提示：**⛔0 以注释判读站点**）；② **0** 处 |
| 5 | 新增键面/函数面在位 | 逐面文本在位性 | ✅ 两副本 8 面全在位（`INDEP_VERIFY_DECL`／`probe_independent_evidence`／`independence_verification`／`independence_deficiency_alarm`／`independent_verification_ref`／`independent_verification_status`／`runner_fix_notice`／`prescription_ref`）；② 另 `key_rename_migration` 在位、① 另 `self_verified_only_basis` 在位（② 因键名改而为其新键 `_basis`） |
| 6 | 身份接线 | 输出路径／`GENERATOR`／`task_id`／`DATE` 逐一核 | ✅ ① ② 全指向新名；`task_id` ＝ `…-FIXCOPY-1009` ／ `…-RENAME-1009`；`DATE` ＝ `2026-10-10` |
| 7 | 0 覆写之结构保证 | 副本 4 个输出常量逐一 `Test-Path` | ✅ 4 条**全为新名且不在盘**（`exists=False`）⇒ 结构上 0 可能覆写既有产出 |
| 8 | **两副本 PINNED 面**（含本棒新增） | `ast.literal_eval` 取 `PINNED` ＋ 逐件哈希 | ✅ ① **11/11 MATCH** ／ ② **12/12 MATCH**（① 追加 pin ＝ 10-09 版两产出 ＋ 其原件；② 追加 pin ＝ 上述 3 件 ＋ ① 修正副本） |
| 9 | 原件既有 PINNED 面 | 逐件哈希 | ✅ **8/8 MATCH** ⇒ 两副本若跑，其 0-覆写断言**不会**因 pin 漂移而误中止 |
| 10 | 键名出现分布 | 非注释行／注释行分离计数 | ① ＝ 非注释 9 处（赋值 ＋ `_basis` ＋ `value_rule` ＋ 顶层 4 处 ＋ 通知）／注释 6 处；② ＝ 非注释 5 处（**全为溯源/迁移/偏离登记**）／注释 4 处 ⇒ **0 处旧键 emission** |
| 11 | **既有件 0 回改** | 跑后逐件复测 9 件 | ✅ **9/9 一致**（§6） |
| 12 | 编码/行尾 | 逐件字节实测 | ✅ 五件全 **BOM=NO · CRLF=0**（沿原件 LF 体例） |
| 13 | 落前 0 命中 | 构建器内置 `assert not p.exists()` ＋ `Test-Path` ＋ `glob` | ✅ ① ② ③ 落前全 `False` ／ 0 命中 |
| 14 | 改动区登记 | `difflib.SequenceMatcher` 机器复算 | ✅ ① **13 区** ／ ② **13 区**（登记见 §2.4 与 §3.3） |

**⛔ 本棒 0 做**：⛔ **0 运行** ① ②（故其输出 JSON **不存在**）｜⛔ **0 生成任何产出件**｜⛔ **0 网络**｜⛔ **0 skill**｜⛔ **0 LLM**｜⛔ **0 读 key**｜⛔ **0 判档**（**0 出 PASS/FAIL/KD**；判定归口＝verdict-keeper）｜⛔ **0 改任何既有产出件**。

> **构建过程登记（如实 · 供审计）**：本棒之两副本经**两次废件重出**方达上表状态。① 次缺陷 ＝ 构建器多行替换只覆盖 1 行（`PINNED`／输出常量／docstring／循环四块**尾部残留重复**）⇒ `ast.parse` 报 `unexpected indent`（L156）**当场拦下**；② 次缺陷 ＝ `after` 型插入点差 1 行（头块落到 coding 声明之上，`# -*- coding: utf-8 -*-` 被挤至 L57）⇒ 行号复核**当场拦下**。两次废件均经 `mavis-trash` 丢弃（可复原），**0 进入证据面、0 被任何下游件引用**；最终两副本另立新名重生并通过 §4 全部 14 项。
> **由此得一条可复用纪律（建议入册）**：**多行替换必须按跨度（span）锚定 ＋ 逐块首行断言**，⛔0 以「单行替换 + 目测」施于成块文本 —— 本棒两次拦下皆源于此。

> **诚实限度登记**：① ② 之**运行时行为未证**（本棒 0 运行）—— 沿勘误源 §2.3.4 ＋ 前棒注记 §7‑4 同款限度。静态级验证只能证明「求值表达式与结构正确」，⛔0 证明「运行后读数符合预期」。

---

## §5 影响面

### §5.1 对既有产出件与既有读数：**读数字面 0 变 ＋ 键名 0 变**

| 面 | 读数现状 | 本棒之影响 |
|---|---|---|
| `33ad1c01f745`（09-29 产出）之 `chain.self_verified_only` | **22/22 `true`** | **0 变** ⛔0 回改、0 重跑 ⇒ 仍载原件所写之 `true` ＋ **旧键名**；其求值来源之缺失已由 ① **面向未来**解决 |
| `95f3f0957be8`（10-09 产出）之 `chain.self_verified_only` | **22/22 `true`** | **0 变**（同上） |
| `link_verified`／`chain_summary.independent_rewalk_ok` | 22/22 ／ `true` | **0 变**（二者本已真求值） |
| 链根三环（`state_22`／`ext_1`／`b3_merkle_root`） | 09-29：`bbd61495cb5d`／`bf492f1c8424`／`45ef859b2be9` | **0 变**（本棒 0 触链式构造与四式） |
| `protocol_version` 键面（**10-09 版独有**） | `V0.4` ＋ 伴生轴声明串 | **0 变**（本棒 0 动该两面） |
| 自校验链（`content_sha256`／`path_sha256`／`anchor_sha256`） | 各件三条全 MATCH | **0 变**（⛔0 写既有件 ⇒ 哈希不动） |
| 既有 16 件判定/登记件之字面 | 各件之当时事实 | **0 变**（⛔0 以改名伪改历史） |

### §5.2 对前棒件之影响：**0**（`041525fd05a2` 一字未动，见 §6）

---

## §6 0 回改确认（逐件复测 · 跑前＝跑后）

| 件 | 跑前 SHA-12 | 跑后 SHA-12 | 判定 |
|---|---|---|:-:|
| `..._runner_v0_4_2026_10_09.py`（本棒修正对象） | `7c095c54fb99` | `7c095c54fb99` | ✅ **0 回改**（21,826 B · 474 行 · 未动） |
| `..._runner_v0_4_2026_09_29.py` | `de16bc002198` | `de16bc002198` | ✅ **0 触及** |
| `..._runner_selfverify_fix_2026_10_10.py`（前棒件／体例底本） | `041525fd05a2` | `041525fd05a2` | ✅ **0 回改** |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_10_09.json` | `95f3f0957be8` | `95f3f0957be8` | ✅ **0 触及** |
| `corpus/v20/index_v3_2026_10_09.json` | `74b27393574f` | `74b27393574f` | ✅ **0 触及** |
| `results/deposon_p_d_b3_merkle_22_caption_v0_4_2026_09_29.json` | `33ad1c01f745` | `33ad1c01f745` | ✅ **0 触及** |
| `corpus/v20/index_v3_2026_09_29.json` | `3ba2449cf986` | `3ba2449cf986` | ✅ **0 触及** |
| `results/_criterion_application_scope_prereg_2026_10_01.md`（规格源） | `c4e3338619c6` | `c4e3338619c6` | ✅ **0 触及** |
| `results/_exp06_supplement_four_gaps_2026_10_10.md`（勘误源） | `9f86cc5be8e9` | `9f86cc5be8e9` | ✅ **0 触及** |
| `results/_exp06_selfverified_runner_fix_note_2026_10_10.md`（前棒注记） | `247398b687e6` | `247398b687e6` | ✅ **0 触及** |

---

## §7 残留与未代裁项（如实登记 · **0 推断 · 0 代裁**）

| # | 项 | 事实 | 处置／归属 |
|:-:|---|---|---|
| **1** | **两副本 0 运行** | ① ② 均 0 执行 ⇒ 运行时行为**未证**；其输出 JSON **不在盘** | 如实登记（§4 诚实限度）；⛔0 重跑（授权面仅「修正／改键名」）；跑否**归 PI** |
| **2** | **⚠️ 键名改与锁定规格表之偏离** | `c4e3338619c6` §5 逐字段分类表 **L173 逐字锁** `chain.self_verified_only`（表头「**随本件生效即锁**」）⇒ ② 之日后产出所载键名**与之不一致** ＝ **形式偏离** | 本棒 ⛔ **0 回改该规格件**、⛔ **0 代裁**是否发附录/勘误件 ⇒ ② 产出件以 `key_rename_migration.spec_divergence` 节**显式登记**；**归 PI / protocol-keeper** |
| **3** | **旧读法工具未迁（T1 未落）** | B 面 7 件真读工具按**旧键名**取值；若日后以 ② 重跑并以其产出为输入，旧读法将 **`KeyError`** | 本棒 ⛔0 代改（非本棒所有权）⇒ **候派**一棒作读法迁移（兼容双读 ＋ 禁 `or` 短取），或 PI 裁「暂不迁」；**风险已登记 0 隐瞒** |
| **4** | **`INDEP_VERIFY_DECL = None`** | ① ② 均 **0 声明**独立验证件（⛔0 以自身产出充当独立件，违 §3.3②「0 与被验证件同源」）⇒ status=`not_declared` | **设计态**而非缺陷；填入**异源**件后重跑即生效（§3.5） |
| **5** | **硬写是否为有意设计** | 原件源码 **0 陈述**该位之设计意图 | ⛔ **0 推断**（沿勘误源 §2.3.3 同款限度） |
| **6** | **键名拟案系棒方所拟** | 轮 36 卡裁「含键名改」之**方向**；**具体键名**为棒方拟案（候选 A‑D ＋ 推荐 A） | ② 之实现 ＝ 候选 A ＝ **拟案 · 候 PI 核准**；PI 若择 B/C/D，**只须改 ② 一件**（① 0 动）⇒ 见 §3.3 |
| **7** | **未审面** | 本棒 **0 核读**冻结升级件 `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` 正文；**0 核读** 10-09 版之产生经过（为何两版均含同形硬写：⛔0 推断） | 如实登记（沿勘误源 §2.3.4 同款限度） |
| **8** | **影响面计数口径** | §3.4 之 35 件 ＝ 全仓 `self_verified_only` 文本命中件 39 减去本棒新出 4 件（① ② ＋ 2 工具件）；`.tmp/vk_v3df_0_1_verify_out_2026_10_09.json` 计于工具面（探针产出） | 口径随附，避免计数歧义 |

---

## §8 体例与纪律自检

| 项 | 状态 |
|---|:-:|
| 命名合规（`_主题_日期`、⛔0 `_v5_`/`_v4_`/`_v3_` 等 V-阶段前缀、⛔0 阶段号作首段） | ✅ `…_2026_10_09_selfverify_fix_2026_10_10.py`／`…_2026_10_09_selfverify_rename_2026_10_10.py`／`_exp06_selfverified_renaming_note_2026_10_10.md`（沿 09-29 前棒件命名法） |
| 副本与注记件**分离**（副本头块内载注记件路径） | ✅ ① ② 头块均载 `results/_exp06_selfverified_renaming_note_2026_10_10.md` |
| 修正与勘正**分离成件**（① 保留锁名 ＋ ② 承载改名） | ✅ §3.3 |
| 身份改写与语义改动**严格分离登记** | ✅ §2.3 ＋ §3.3 |
| 拟案给据（≥2 备选 ＋ 推荐 ＋ 论证） | ✅ §3.2（候选 **4** 项 ＋ 推荐 A ＋ 逐条论证 ＋ 逐否理由） |
| 影响面清单 ＋ 迁移注记 | ✅ §3.4（**35 件** · 分 4 面）＋ §3.5（**T1/T2/T3** 三轨） |
| 逐件实测指纹（SHA-256／SHA-12／bytes／行／BOM／CRLF） | ✅ §1 ＋ 回执 |
| 工具件标注（**0 属证据面**） | ✅ `.tmp/_exp06_1009fix_build_2026_10_10.py`／`.tmp/_exp06_1009fix_verify_2026_10_10.py`（沿先例 `.tmp/_exp06_fixcopy_verify_probe_2026_10_10.py`） |
| 0 判档 | ✅ §0 铁律 ＋ §4 末 |
