# EXP-05 · 阴性探测项重扫（E-24 之 ①② · 归档区／在途卡）· evidence-auditor · 2026-10-10

> **归口**：evidence-auditor（阴性证据面）· **本件即出**。
> **授权**：PI 轮 11 卡选认「**全数（03–06＆08）**」⇒ 本件属 EXP 批小项三件之一。
> **输入**：`_pending_pi_items_master_register_2026_10_09.md` §6.2 **第 2 项**（V3-01 两件）＋ **第 4 项**（`EMBEDDING_VISION_V1_IMPL`）——自定位。
> **缺口对位**：`_kd_resolvability_and_optional_experiments_2026_10_09.md` §**A-9**（E-24 之 ① ③）／§**OPT-5**（EXP-05 ＝「闭 E-24 之 ①②」）。
> **runtime**：纯本机只读扫描（`Get-FileHash`／`Test-Path`／`Get-ChildItem`／`grep`）＋ **1 次 `write`**（本件）。⛔ **0 网络**／⛔ **0 skill**／⛔ **0 端点调用**／⛔ **0 读 key**／⛔ **0 读 `.env`**（R4：key 永不明文）。
> **性质**：**阴性探测面** —— 只报告「在盘／未核得」两态读数，**0 判档**、**0 代裁**、**0 认定永久不存在**。

---

## §0 结论摘要（**先读此节**）

| 探测项 | 仓内（`deposon-repo`） | 归档区（`_non_upload_local_archive`） | 终态判定 |
|---|---|---|---|
| **①-a** `tools/distortion_calculator.py` | `Test-Path` ＝ **False** | **0 命中**（同名全盘递归扫描） | ⚠️ **未核得**（两处皆无 ⇒ 真缺件候选） |
| **①-b** `verifier/handoff/P_B_V0_anchors_sha256_12.json` | `Test-Path` ＝ **False** | **0 命中**（目录逐件列举确认） | ⚠️ **未核得**（两处皆无 ⇒ 真缺件候选） |
| **②** `EMBEDDING_VISION_V1_IMPL_2026_09_10.md` | **0 命中**（`docs\V3X` 目录在，但无此名文件） | ✅ **在盘 · 实存 20,392 B** | ✅ **FOUND_IN_ARCHIVE · 命中** |

**⛔ 关键登记**：① 两项之阴性**扩展了主账原探测范围**（主账 §6.2‑2 仅仓内 `Test-Path`；本轮**加扫归档区**）⇒ **仍为「未核得」**，但探测面由「仓内」扩至「仓内 ＋ 归档区」。**⛔ 0 断言其永久不存在** —— 归档区外（如 PI 私人盘／他机／未同步远端）**未探测**，不可由本次阴性外推。
**✅ 关键闭项**：② 由主账 §6.2‑4 之「**未核得**（本轮未复扫归档区）」⇒ **本轮复扫后转为「在盘 · 命中」**（E-24 之 ② **可闭**）。

---

## §1 探测范围声明（如实 · 0 掩饰）

| 项 | 内容 |
|---|---|
| **仓内扫描根** | `_september_workspace`（递归 · `-Force` 含隐藏项） |
| **归档区扫描根** | `〔本地归档区〕`（递归 · `-Force`）—— **只读 · 0 写入**（R5／归档区管理纪律） |
| **仓内探测手段** | `Test-Path`（逐件）＋ 递归 `Get-ChildItem -File` 名称正则匹配（`distortion_calculator｜P_B_V0_anchors`） |
| **归档区探测手段** | 递归 `Get-ChildItem -File` 名称正则匹配（`distortion_calculator｜P_B_V0_anchors｜^P_B`）＋ `verifier\handoff` 目录逐件列举 ＋ `tools\` 目录逐件列举 |
| **⛔ 0 探测面（如实声明）** | ① 归档区**之外**的任何位置（他机／外接盘／云端／未同步远端）**本轮 0 探测**；② 归档区 `tmp`／`cache`／`installers` 内部**未逐件内容级比对**（仅文件名层扫描）；③ 文件名被改动过者**不可由名称扫描命中**（**改名件漏检风险如实登记**） |
| **⛔ 0 断言** | 「未核得」**≠**「不存在」；「在盘」**≠**「已归位」——**归位须另行授权**（见 §5） |

---

## §2 逐件探测记录

### 2.1 ①-a `tools/distortion_calculator.py`

| 探测面 | 手段 | 实测 |
|---|---|---|
| 仓内 `tools\distortion_calculator.py` | `Test-Path -LiteralPath` | **False** |
| 仓内全域 | 递归文件名正则 `distortion_calculator` | **0 命中** |
| 归档区全域 | 递归文件名正则 `distortion` | **1 命中 ≠ 本件** —— `results/_remote_version_freeze_2026_09_26/P_B_DISTORTION_BOUND_V0_SPEC.md`（7,126 B，**spec 件非计算器**） |
| 归档区 `tools\` | 逐件列举（17 件） | **0 命中**（`ark_codingplan_30cells.py`／`deepseek_v41_flash_30cells.py`／`render_v3x_corpus_graphs.py` 等，**无一为本件**） |

**判定**：⚠️ **未核得**（MISSING_TRUE 候选）—— 仓内 ＋ 归档区**两处皆无实体**。**⛔ 0 断言永久不存在**（见 §1 未探测面）。

### 2.2 ①-b `verifier/handoff/P_B_V0_anchors_sha256_12.json`

| 探测面 | 手段 | 实测 |
|---|---|---|
| 仓内 `verifier\handoff\P_B_V0_anchors_sha256_12.json` | `Test-Path -LiteralPath` | **False** |
| 仓内 `verifier\handoff\` | 目录逐件列举（**4 件实存**） | `KT_ABC1_anchors_sha256_12.json`(6,680 B)／`KT_ABC1_anchors_sha256_12.root_session_11318B.bak_2026_09_23.json`(11,318 B)／`KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json`(5,049 B)／`P_F_PREDECISION_2026_09_09.json`(3,680 B)／`P_F_PREDECISION_2026_09_11_V0.1.json`(12,498 B) ⇒ **本件不在其中** |
| 仓内全域 | 递归文件名正则 `P_B_V0_anchors` | **0 命中** |
| 归档区 `verifier\handoff\` | 目录逐件列举 | **同仓内 4 件**（`KT_ABC1` ×2 ＋ `P_F` ×2）⇒ **本件不在其中** |
| 归档区全域 | 递归文件名正则 `^P_B｜P_B_` | **7 命中**，皆为 `P_B_DISTORTION_BOUND_V0_SPEC.md`(7,126 B) ＋ `_v4_supp_b_*`(6 件) ⇒ **0 件为本件** |

**⚠️ 同目录旁证（如实登记 · 非同件）**：仓内与归档区 `verifier\handoff` **各存有 `KT_ABC1_anchors_sha256_12.json`（6,680 B）** —— 命名族相近（`*_anchors_sha256_12.json`）但**首部为 `KT_ABC1` 非 `P_B_V0`** ⇒ **0 判定为同件**；⛔ **0 代替 PI 裁「是否改名／是否即本件另称」**。
**判定**：⚠️ **未核得**（MISSING_TRUE 候选）。

### 2.3 ② `EMBEDDING_VISION_V1_IMPL_2026_09_10.md` —— ✅ **命中**

| 探测面 | 手段 | 实测 |
|---|---|---|
| 仓内 `docs\V3X\` | 目录在；文件名扫描 | **0 命中**（该目录存在但**无此名文件**） |
| 归档区 `docs\V3X\` | 递归文件名正则 `EMBEDDING_VISION` | **3 命中** ✅ |

**✅ 命中件 · 实测指纹（落盘前实测 · 归位非破坏式 · 原件不动）**：

| 项 | 值 |
|---|---|
| **绝对路径（source）** | `〔本地归档区〕/docs/V3X/EMBEDDING_VISION_V1_IMPL_2026_09_10.md` |
| **仓内相对路径（建议 dest）** | `docs/V3X/EMBEDDING_VISION_V1_IMPL_2026_09_10.md`（**repo 相对路径规范** · 沿既有件体例） |
| **bytes** | **20,392** |
| **last-write** | 2026-09-17 23:00:18（目录时间戳口径） |
| **同目录同族伴件（非本件）** | `EMBEDDING_VISION_STRATEGY_V0.md`｜`EMBEDDING_VISION_STRATEGY_V1_GAMETHEORY.md` |

**拉回路径（PI 核准后照此执行 · 本轮 ⛔ 0 执行拉回）**：
```
source : 〔本地归档区〕/docs/V3X/EMBEDDING_VISION_V1_IMPL_2026_09_10.md
dest   : _september_workspace/docs/V3X/EMBEDDING_VISION_V1_IMPL_2026_09_10.md
方式   : 非破坏式复制（⛔ 0 覆盖现存件 · ⛔ 0 移动 · ⛔ 0 删除原件）
归位判据: 副本与原件 SHA-256 复算 MATCH ⇒ 方可宣告归位成功
回滚   : 删副本即可（原件始终不动）
```
> ⛔ **本轮 0 执行拉回** —— 归位属**写动作**，须 PI 核准；本件仅出**路径＋判据**。

---

## §3 幽灵引用对账（三方比对 · 五分支判定）

| 引用项 | 仓内实存 | 归档区实存 | 三方比对终态 | 分支 |
|---|:-:|:-:|---|---|
| `tools/distortion_calculator.py` | ❌ | ❌ | 引用面有、盘上两处皆无 | **MISSING_TRUE 候选**（真缺件候选 · **不造来源**） |
| `verifier/handoff/P_B_V0_anchors_sha256_12.json` | ❌ | ❌（同目录仅 `KT_ABC1`／`P_F` 族） | 同上 ＋ **同族旁证不构成同件** | **MISSING_TRUE 候选** |
| `EMBEDDING_VISION_V1_IMPL_2026_09_10.md` | ❌ | ✅ | **实件在仓外** | **GHOST_REF_OUTSIDE**（幽灵引用：实件仓外）→ **已登记可拉回** |

**✅ 无 CONFLICT 检出**：本轮所涉三名**未出现「同名不同哈希」**（仓内 ＋ 归档区两处均无同名实体）⇒ CONFLICT 面 **0 占用**。
**✅ 无 SAME_IDENTITY 检出**：无同哈希多份情形（`KT_ABC1_anchors_sha256_12.json` 仓内／归档区虽同名同字节，**不属本轮三探测项**；如实登记其**存在仓内＋归档区双份**，**不重复计数**于本轮）。

---

## §4 0 做与限制声明

- ⛔ **0 回改任何既有件**：全程只读 ＋ **1 次 `write`**（本件）；**0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除**任何既有件。
- ⛔ **0 写入归档区**：归档区全程**只读扫描**（R5 仓外只读 0 写入）——**归档区 byte 0 触动**。
- ⛔ **0 执行拉回**：命中件仅**出路径＋判据**，⛔ 0 复制／0 移动／0 删除（归位须 PI 核准）。
- ⛔ **0 断言永久不存在**：阴性读数**仅在 §1 声明的探测面内成立**，⛔ 外推至未探测面。
- ⛔ **0 编造来源**：两处皆无者**如实写「未核得」**，**不虚构文件出处**。
- ⛔ **0 代裁**：**不判** MISSING_TRUE 之最终法律效力（真缺件 ＝ 须 PI 裁「作废引用／补件／改指向」）；**不判** `KT_ABC1` 族是否即本件另称。
- ⛔ **0 判档**：本件**0 出 `K-*`／`KD`／`PASS`／`FAIL` 任何档位**。
- ⛔ **0 读 key／0 读 `.env`／0 落盘凭据**（R4：key 永不明文 · 本件 0 出现任何 key 片段）。

---

## §5 候 PI 面（如实列明 · 0 推荐次序）

| # | 候呈项 | 处置选项（**0 推荐 · 0 排序暗示**） |
|:-:|---|---|
| 1 | **② 命中件是否归位仓内** | ① 核准按 §2.3 拉回路径复制（副本 SHA-256 MATCH 后宣告）｜② 仅登记不归位（维持仓外）｜③ 另指 dest 路径 |
| 2 | **① 两项 MISSING_TRUE 候选之最终处置** | ① 裁「真缺件 · 作废引用」｜② 裁「改名件 · 另指实件」（如 `KT_ABC1` 族是否即本件）｜③ 裁「待外源补件」 |
| 3 | **归档区管理纪律承接** | 若执行归位 ⇒ 须**同批更新索引**（source→dest 映射＋件数/字节/哈希＋入库时点）、**0 重名**、**拉回路径可一键复原**（沿 PI 立「归档区管理」条） |

---

## §6 落盘自证

| 项 | 内容 |
|---|---|
| **落前撞名实测** | `Test-Path 'results/_exp05_negative_probe_rescan_2026_10_10.md'` ＝ **False**；`results/` 内 `*exp05*`／`*exp06*`／`*exp08*`／`*negative_probe*`／`*kcf4*`／`*prompt_face*`／`*s4_prompt*` glob **全部 0 命中** ⇒ ✅ **新名新建 · 0 覆写** |
| **命名合规** | `_exp05_negative_probe_rescan_2026_10_10.md` ＝ `_主题_日期` 形态；⛔ **0 带 `_v5_`／`_v4_`／`_v3_` 等 V-阶段前缀**（沿 `57024f2cd30a` §1.2②） |
| **本件写动作** | **新增 1 件**（本件）；⛔ **0 编辑／0 覆写／0 追加／0 改名／0 移动／0 删除**任何既有件 |
| **引用件只读** | 主账 `e4…` 面 ＋ `E-24` 对位件 ＋ `verifier/handoff` 5 件 ＋ 归档区 `tools` 17 件 ＋ 归档区 `docs\V3X` 3 件：**byte 0 触动** |
| **编码／行尾** | **UTF-8 无 BOM · LF**（落盘后按字节复核，见交付回执） |
| **网络／skill／LLM** | **0 网络** ｜ **0 skill** ｜ **0 LLM 代答** |
| **本件自身指纹** | ⛔ **不自写入本件**（自指回环）⇒ **随交付回执回报终态 SHA-256／SHA-12／bytes／BOM／CRLF**；外部观测者请以 `Get-FileHash -Algorithm SHA256` 独立复算 |
