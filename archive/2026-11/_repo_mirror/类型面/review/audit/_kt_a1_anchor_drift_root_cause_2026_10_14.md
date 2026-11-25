# KT-A1 锚漂移之根因判定（②锚：P_A_LLM_CLIENT / P_A_HARNESS）

> **件性质**：**审计判定件**（证据链面·**实测件**）——就 `KT-A1` 之 2 锚不符之**根因**作判，**0 宣告**任何条款「生效／不生效」之终局。
> **署名**：`evidence-auditor`｜**棒别**：①段收官 · 证据链审计（锚漂移根因）｜**件日**：2026-10-14
> **对象**：`P_A_LLM_CLIENT`（登记 `055e874ea5c1` vs 实测 `1722500da4aa`）／`P_A_HARNESS`（登记 `9f383935c00c` vs 实测 `275e480ba4d9`）
> **本件状态**：全篇推断与处置建议 **均标「候 PI 核准」**；⛔ **0 宣告**①毕；⛔ **0 宣告**停跑解除。

---

## §0 一句话结论

**该 2 锚不符之根因 ＝「已授权返工（2026-09-10 Option A 合法变更）＋ 登记面自始未 reconcile」之合成结果；本棒实测**排除**「未提交改动」与「他机差异」两假设**（远端首现即新值、父提交 404、跨机字节逐位一致）。
⇒ **L263／L54 之触发条件在「未授权漂移」意义上未成立**；但**字面条件**仍为真（2 锚 ≥ 1），**是否宣告生效／不生效之唯一通道 ＝ PI 明示**，本棒 ⛔ 0 宣告。

---

## §1 方法与源件回读（逐字·实测·0 沿用转引）

### §1-1 本棒方法

| **项** | **本棒做法** |
| :-- | :-- |
| **逐字回读** | 两件源件之相应节**逐字回读并录原文**；另回读 `baef94e393de` L119–L124／L132／L141／L178、`977fe1b48f75` L238–L250、`41f5f1689d09` L97／L114／L115／L120–L141、两 spec 之 L65／L260／L261／L263／L319 与 L44／L48–L54 ——⛔ **0 以他件转述充直读** |
| **指纹纪律** | 全部指纹**本棒实测**（`hashlib.sha256(bytes).hexdigest()[:12]` ＋ 字节数）｜⛔ **0 沿用**派工单元或他件自报值 |
| **联网核验** | GitHub API（`api.github.com`）＋ `raw.githubusercontent.com`，**只读**；⛔ **0 PAT**、⛔ **0 上传／0 远端写／0 推送** |
| **阴性结论** | **双通道**：① 路径列举（全树 `git/trees/main?recursive=1`，3,076 blobs 穷举 basename）② 内容／SHA 通道（raw 字节复算 `sha256[:12]`）；并列**实搜 URL 与 HTTP 状态码**；检索根含运行时附件面（`〔本地路径已脱敏〕`，见 §1-4） |
| **哈希工具** | `hashlib.sha256`（stdlib）｜⛔ **0 用**内建 `hash()` |

### §1-2 两件源件指纹（**本棒实测**·与派工单逐位相符）

| `sha256[:12]` | **bytes（本棒实测）** | 件名 | 本棒用途 |
| :-: | --: | :-- | :-- |
| `e2c35c2ac858` | **31,849** | `results\_kt_a1_v0_lineage_corrigendum_2026_10_14.md` | 世系与触发面（§2-5／KD-A） |
| `a68b2971b8e1` | **49,012** | `results\_batch8_deliberation_judgment_2026_10_14.md` | 授权链叙述（§2-3） |

### §1-3 源件回读所得（逐字·关键节）

**① `e2c35c2ac858`（世系补正件）·§2-5 全表（L134–L139）逐字**：

| 锚 ID | 登记 `value` | 盘上实体（实测） | 实测 SHA-12 | bytes | 判定 |
| :-: | :-: | :-: | :-: | --: | :-: |
| `P_A_LLM_CLIENT` | `055e874ea5c1` | `tools/llm_client.py` | **`1722500da4aa`** | 8,118 | 🔴 **不符** |
| `P_A_HARNESS` | `9f383935c00c` | `tools/exp_harness.py` | **`275e480ba4d9`** | 10,090 | 🔴 **不符** |

其 L139 逐字：「`78b71d404366` **L263**「任何 ≥ 1 锚漂移」之条件，**在盘上已字面成立**（2 锚 ≥ 1）」；L141 逐字：「⛔ **本棒 0 宣告**「全 KT-A1 撤回」或「全 V0 撤回」**已生效**；⛔ **0 宣告**不生效。撤回之宣告与执行通道唯一 ＝ **PI 明示**」；其 §6-4 第 3 项逐字：「**2 锚不符之根因未判**……**该判别直接决定 L263／L54 之条款是否适用**，本棒⛔ **0 预判**」。

> 📌 **本棒之任务即闭合该「0 预判」缺口**（§3）。

**② `a68b2971b8e1`（锚漂移另议件）·§2-4（L150–L170）逐字**：载因果链「2026-09-10 Option A 授权返工 ⇒ llm_client/exp_harness 内容变更（OLD→NEW）／2026-09-15 锚核验 ⇒ 两锚判 DRIFT_AUTHORIZED（合法返工）／2026-09-23 PI「你直接修正」⇒ 主路径【复位】回 6,680 B（03c6c01f3697，OLD 值）」；其 L170 逐字：「现盘「登记 OLD vs 实测 NEW」之状态……**正是**「**实体已按授权变更、登记面按冻结契约复原**」之二轨并存」。

**③ 三处授权出处（本棒逐字回读源件，非转述）**：

- `baef94e393de`（`KT_B1_REWORK_REPORT_2026_09_10.md`）**L121–L122 逐字**：
  > 「| `tools/llm_client.py` | `055e874ea5c1` | `1722500da4aa` | 返工 5 文件之一 |」
  > 「| `tools/exp_harness.py` | `9f383935c00c` | `275e480ba4d9` | 返工 5 文件之一 |」
  
  **L132 逐字**：「| KT-A1 锚（5） | 3 | **2（llm_client + exp_harness 合法返工）** | 0 |」；**L141 逐字**：「8 个 DIFF 全部查明：**5 个是 Option A 授权返工的合法变更**，3 个是未报告的 BOSS-B 漂移（已修复）。」；**L178 逐字**：「**锚 JSON 本身未更新**：`KT_ABC1_anchors_sha256_12.json` 保留旧 SHA-12（历史记录），**上表即替代关系报告**。后续如需冻结新锚，需走正式流程更新该 JSON。」
- `977fe1b48f75`（`P_A_D1_D3_REPORT_2026_09_15.md`）**L247–L248 逐字**：
  > 「| P_A_LLM_CLIENT | tools/llm_client.py | 055e874ea5c1 | 1722500da4aa | ✗ | **DRIFT_AUTHORIZED** (沿 KT_B1_REWORK_REPORT §四 2026-09-10 合法返工) |」
  > 「| P_A_HARNESS | tools/exp_harness.py | 9f383935c00c | 275e480ba4d9 | ✗ | **DRIFT_AUTHORIZED** (沿 KT_B1_REWORK_REPORT §四 2026-09-10 合法返工) |」
  
  **L250 逐字**：「**5 锚 9 子项综合**: 7 MATCH + 2 DRIFT_AUTHORIZED = **9/9 PASS (含合法返工)**」
- `41f5f1689d09`（`TRAE_V3_ASSET_ERRATUM_2026_09_23.md`）**L114 逐字**：「……**例外**：`verifier/handoff/KT_ABC1_anchors_sha256_12.json` 于 2026-09-23 经 PI 明示授权（「你直接修正」）按 E-15 处置复位——这是本件出具的唯一一处既有文件写入」；**L115 逐字**：「E-15 复位是**资产层修复**（恢复冻结契约所声明的字节状态），**不涉任何实验结论与判定本体**。」；**L137 逐字**：「**修后终验（机器复算）**：……`TOTAL: 16 frozen files | OK: 16 | FAIL: 0`、`0-touch declaration: PASS`——修前 15/16（唯一 FAIL = E-15）→ 修后 16/16。」
- **机器孪生** `results/deposon_pa_d1_d3_2026_09_15.json`（`e221792715f8`／15,604 B）：`DRIFT_AUTHORIZED` 计数 4、`055e874ea5c1` 4、`9f383935c00c` 4、`1722500da4aa` 4、`275e480ba4d9` 4。

### §1-4 两条 spec 之条款本体（本棒逐字回读·本地活件）

| 件 | SHA-12 | 行 | 逐字 |
| :-: | :-: | :-: | :-- |
| `docs/V3X/KT_A1_SPEC_V0.1.md` | `78b71d404366`／29,570 B | **L263** | 「**任何 ≥ 1 锚漂移 → 全 KT-A1 撤回**。」 |
| 同上 | 同上 | L65 | 「- 任何 ≥ 1 锚漂移 → 全 KT-A1 撤回(P-A V0 spec §2 + 本 SPEC §6)」 |
| 同上 | 同上 | L319 | 「- **5 锚漂移 ≥ 1** → 全 KT-A1 撤回」 |
| 同上 | 同上 | L260 | 「| `P_A_LLM_CLIENT` | `tools/llm_client.py` | SHA-256 全文 → 前 12 位 | Doubao + DeepSeek, runtime `Path().read_text()` 不入 prompt | **`055e874ea5c1`** |」 |
| 同上 | 同上 | L261 | 「| `P_A_HARNESS` | `tools/exp_harness.py` | SHA-256 全文 → 前 12 位 | 机制 M1/M2/M3 + 任务族 T1-T4 | **`9f383935c00c`** |」 |
| `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `bd1caab42b4c`／10,351 B | **L54** | 「任何 ≥ 1 锚漂移 → 全 V0 撤回。」 |
| 同上 | 同上 | L51／L52 | `P_A_LLM_CLIENT`／`P_A_HARNESS` 之**字段列**载「`version=2026-09-11`」；**全表 4 列，⛔ 0 `value` 列** |

---

## §2 远端核验（URL ＋ HTTP 状态 ＋ 实测值·全部实测非引述）

### §2-1 核验面

- **远端**：`zeroandcat/Deposon`（`https://api.github.com/repos/zeroandcat/Deposon` → **HTTP 200**）｜`full_name=zeroandcat/Deposon`｜`private=False`｜`default_branch=main`｜`size=38132` KB｜`created_at=2026-08-22T13:12:16Z`｜`pushed_at=2026-10-12T13:13:37Z`
- **分支**：`https://api.github.com/repos/zeroandcat/Deposon/branches?per_page=100` → **HTTP 200** → `["main"]`（**恰 1 分支**）
- **全树**：`https://api.github.com/repos/zeroandcat/Deposon/git/trees/main?recursive=1` → **HTTP 200**（883,343 B）｜`sha=74c7d7692cb8…`｜`tree entries=3,255`｜**`blobs=3,076`**｜**`truncated=False`**（⇒ **全树穷尽，非抽样**）
- **⛔ 0 PAT**；全部调用为匿名只读 GET

### §2-2 实搜 URL 与状态码（阴性通道之一）

| # | URL | **HTTP** | 结果 |
| :-: | :-- | :-: | :-- |
| 1 | `https://api.github.com/repos/zeroandcat/Deposon/contents/tools/llm_client.py?ref=main` | **404** | `message: Not Found` |
| 2 | `https://api.github.com/repos/zeroandcat/Deposon/contents/tools/exp_harness.py?ref=main` | **404** | `message: Not Found` |
| 3 | `https://raw.githubusercontent.com/zeroandcat/Deposon/main/tools/llm_client.py` | **404** | 14 B 之 404 页 |
| 4 | `https://raw.githubusercontent.com/zeroandcat/Deposon/main/tools/exp_harness.py` | **404** | 14 B 之 404 页 |
| 5 | `…/contents/verifier/handoff/KT_ABC1_anchors_sha256_12.json?ref=main` | **404** | `message: Not Found` |
| 6 | `…/contents/docs/V3X/KT_A1_SPEC_V0.1.md?ref=main` | **404** | `message: Not Found` |
| 7 | `…/contents/docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md?ref=main` | **404** | `message: Not Found` |
| 8 | `https://api.github.com/repos/zeroandcat/Deposon/contents/tools/llm_client.py?ref=1b7531167790` | **200** | ✅ **命中** |
| 9 | `https://raw.githubusercontent.com/zeroandcat/Deposon/1b7531167790/tools/llm_client.py` | **200** | 8,118 B／`1722500da4aa` |
| 10 | `https://raw.githubusercontent.com/zeroandcat/Deposon/1b7531167790/tools/exp_harness.py` | **200** | 10,090 B／`275e480ba4d9` |
| 11 | `https://raw.githubusercontent.com/zeroandcat/Deposon/f7d9cf1db1bb/tools/llm_client.py` | **404** | **父提交 0 载** |
| 12 | `https://raw.githubusercontent.com/zeroandcat/Deposon/f7d9cf1db1bb/tools/exp_harness.py` | **404** | **父提交 0 载** |
| 13 | `https://raw.githubusercontent.com/zeroandcat/Deposon/main/_september_workspace/tools/llm_client.py` | **200** | 8,118 B／`1722500da4aa`／CR=0 |
| 14 | `https://raw.githubusercontent.com/zeroandcat/Deposon/main/_september_workspace/tools/exp_harness.py` | **200** | 10,090 B／`275e480ba4d9`／CR=0 |
| 15 | `https://raw.githubusercontent.com/zeroandcat/Deposon/00e1978c6c53/_september_workspace/verifier/handoff/KT_ABC1_anchors_sha256_12.json` | **200** | 6,680 B／`03c6c01f3697` |
| 16 | `https://raw.githubusercontent.com/zeroandcat/Deposon/00e1978c6c53/…root_session_11318B.bak_2026_09_23.json` | **404** | **该备份件 09-20 尚 0 载** |
| 17 | `https://raw.githubusercontent.com/zeroandcat/Deposon/main/…root_session_11318B.bak_2026_09_23.json` | **200** | 11,318 B／`6e9cd8cd8e07` |
| 18 | `https://api.github.com/repos/zeroandcat/Deposon/commits?path=tools/llm_client.py&per_page=100` | **200** | **全史仅 2 提交** |
| 19 | `https://api.github.com/repos/zeroandcat/Deposon/commits?since=2026-09-14T00:00:00Z&until=2026-09-24T23:59:59Z&per_page=100` | **200** | 窗口内 **45 提交**，**09-20 之后至 09-24 无任何提交** |
| 20 | `https://raw.githubusercontent.com/zeroandcat/Deposon/main/_september_workspace/_mirror_manifest.json` | **200** | 192,689 B／`e4548dc95e27` |

### §2-3 远端内容判别：**旧值抑或新值**（内容／SHA 通道）

**⇒ 明确答复派工单之问：远端所载为「新值」，且旧值于远端任何时点 0 存在。**

| 面 | 登记 OLD 值 `055e874ea5c1`／`9f383935c00c` | 实测 NEW 值 `1722500da4aa`／`275e480ba4d9` |
| :-- | :-- | :-- |
| 远端**路径** `tools/llm_client.py`（`main`） | 🔴 **404（0 存在）** | — |
| 远端**路径** `_september_workspace/tools/llm_client.py` | 🔴 0 存在 | 🟢 **HTTP 200／8,118 B／`1722500da4aa`／CR=0** |
| 远端**路径** `_september_workspace/tools/exp_harness.py` | 🔴 0 存在 | 🟢 **HTTP 200／10,090 B／`275e480ba4d9`／CR=0** |
| 远端**提交史**（`tools/` 路径全史 2 提交） | 🔴 **0 存在** | 🟢 首现提交 `1b7531167790` 即 NEW；父提交 `f7d9cf1db1bb` **404** |
| 远端**锚 JSON** 载荷（`_september_workspace/verifier/…json`） | 🟡 **载 OLD**（`055e874ea5c1`×1、`9f383935c00c`×1） | 🔴 0 出现（`1722500da4aa`×0、`275e480ba4d9`×0） |
| 远端**子件 SPEC** 锚表（L260／L261） | 🟡 **载 OLD**（`055e874ea5c1`×4、`9f383935c00c`×2） | 🔴 0 出现 |
| 远端**.bak_2026_09_23**（C7 版） | 🔴 0 出现 | 🟡 **载 NEW**（`P_A_LLM_CLIENT=1722500da4aa`、`P_A_HARNESS=275e480ba4d9`） |

**远端锚表条文逐字**（`_september_workspace/docs/V3X/KT_A1_SPEC_V0.1.md`）：**L263 逐字**「**任何 ≥ 1 锚漂移 → 全 KT-A1 撤回**」；「任何 ≥ 1 锚漂移」出现 **3** 次（对应 L65／L263／L319）。
**远端上游 SPEC 逐字**（`_september_workspace/docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md`）：**L54 逐字**「任何 ≥ 1 锚漂移 → 全 V0 撤回。」；「任何 ≥ 1 锚漂移」出现 **1** 次。

### §2-4 远端提交史（**2026-09-15／09-23 附近之变更是否可见**）

| 提交 | 时间（UTC） | message（截断） | 与本组 2 锚之关系 |
| :-: | :-- | :-- | :-- |
| `9678ec40739e` | 2026-09-15T09:04:46Z | V3X 1-week kill-test artifacts (interim, pre-D7): 4-path D1-D3 reports, P-G V0.1, frozen anchors verified 16/1… | 🟡 **09-15 可见**（含 `977fe1b48f75` 之 D1-D3 报告面），**⛔ 0 触及 `tools/` 二件** |
| `bdfc90582456` 等 | 2026-09-15T04:33Z 前后 | paper: final EN manuscript (arXiv:2609.09001) 等 | ⛔ 0 关联 |
| `1b7531167790` | 2026-09-17T15:34:04Z | v3 final full-mirror batch 10/10 (28 files) | 🔴 **`tools/llm_client.py`＋`exp_harness.py` 之 `status=added`，载荷即 NEW 值**（`tools/exp_harness.py` +280／`tools/llm_client.py` +208） |
| `00e1978c6c53` | 2026-09-20T05:05:36Z | Phase 1: mirror all 701 September files into `_september_workspace/` (+ manifest with local mtimes/sha256; 1 file secret-redacted) | 🔴 **锚 JSON 于此刻进仓＝OLD 值 6,680 B（`00e1978c6c53` 处实测 `03c6c01f3697`）** |
| `32bf0054b5d3` | 2026-09-20T02:12:20Z | remove September internal letters / tmp logs / bak files (56 files) | ⛔ 0 关联 |
| `29f6fd264f2a` | 2026-09-20T05:07:04Z | Phase 3: separate September from main tree (remove 522 mirrored files); main tree = August… | 🔴 **`tools/` 二件自 `main` 移除**（⇒ §2-2 之 1–4 之 404 之成因） |
| `626824bc2c11` | **2026-09-26T14:03:15Z** | upload: 疑似件三门 CLEAN 放行 80 件（全批推送 98 件；另 102 件同内容已在位无动作）2026-09-26 by KIMI | 🔴 **`.bak_2026_09_23` 首次进远端即在此提交** |
| — | **2026-09-21 ～ 2026-09-24** | **窗口内 0 提交**（实测 `commits?since=2026-09-14&until=2026-09-24` → 45 件，末件为 `29f6fd264f2a` @ 09-20T05:07:04Z） | 🔴 **09-23 之授权复位在远端 git 0 可见** |

### §2-5 跨机字节同一性（remote ⇄ local 逐字节）

| 件 | 远端 `main`（`_september_workspace/` 副本） | 本地 `deposon-repo` | 判定 |
| :-- | :-- | :-- | :-: |
| `tools/llm_client.py` | `1722500da4aa`／8,118 B／CR=0 | `1722500da4aa`／8,118 B | 🟢 **逐字节一致**（`content_equal=True`） |
| `tools/exp_harness.py` | `275e480ba4d9`／10,090 B／CR=0 | `275e480ba4d9`／10,090 B | 🟢 **逐字节一致** |
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697`／6,680 B | `03c6c01f3697`／6,680 B | 🟢 **逐字节一致**（`byte_equal=True`） |
| `…root_session_11318B.bak_2026_09_23.json` | `6e9cd8cd8e07`／11,318 B | `6e9cd8cd8e07`／11,318 B | 🟢 **逐字节一致** |
| `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` | `baef94e393de`／11,478 B | `baef94e393de`／11,478 B | 🟢 **逐字节一致** |
| `docs/V3X/KT_A1_SPEC_V0.1.md` | `bbd937f73b93`／29,670 B | `78b71d404366`／29,570 B | 🔴 DIFF（**见 §2-6 脱敏判别**） |
| `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `42719898af98`／10,371 B | `bd1caab42b4c`／10,351 B | 🔴 DIFF（**见 §2-6**） |
| `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` | `31728c6fdcc8`／19,777 B | `977fe1b48f75`／19,751 B | 🔴 DIFF（**见 §2-6**） |
| `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | `1b6ceaef0290`／857,249 B | `41f5f1689d09`／857,551 B | 🔴 DIFF（**见 §2-6**） |
| `…KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | `d7e965b0affe`／5,055 B | `da517c115f3c`／5,049 B | 🔴 DIFF（**见 §2-6**） |

### §2-6 DIFF 之性质判别（**⛔ 0 以「DIFF」充「内容漂移」**）

**判别法**：先测 CR 计数与「CRLF→LF 归一后」之 SHA-12（排除纯行尾差异）；仍不等者以 `difflib.SequenceMatcher` 逐行对位并录差异块。

| 件 | CR（远／本） | 归一后相等？ | 逐行差异块数 | 差异性质（实测样本） |
| :-: | :-: | :-: | :-: | :-- |
| `KT_A1_SPEC_V0.1.md` | 0／0 | ❌ | **14**（行数同 ＝ 462／462） | 🟢 **脱敏改写**：「〔W老师〕」→「〔W老师〕」×8；「〔IM〕」→「〔IM〕」×2；「`〔本地路径已脱敏〕`」→「`〔本机用户目录〕/Desktop/AI/新建文本文档.txt`」×1；另 1 处为段落块整体前移 |
| `P_A_D1_D3_REPORT_2026_09_15.md` | 0／0 | ❌ | **3**（行数同 ＝ 349／349） | 🟢 **脱敏改写**：「〔IM〕」→「〔IM〕」、「〔W老师〕」→「〔W老师〕」 |
| `P_A_EQUILIBRIUM_…_V0_SPEC.md` | 0／0 | ❌ | **未逐块展开** | 🟡 **性质未判**（+20 B，**如实登记**） |
| `TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | 0／0 | ❌ | **未逐块展开** | 🟡 **性质未判**（−302 B，**如实登记**） |
| `…PATCH_2026_09_15.json` | 0／0 | ❌ | **未逐块展开** | 🟡 **性质未判**（+6 B，**如实登记**） |

**⇒ 判别结论**：已展开之 2 件差异**与远端提交面之 `[DEEMPHASIS-B6*] advisory literal anonymization batch 6a/6b/6c`（2026-10-06）相合**（脱敏批）⇒ **非锚值漂移**。
**关键点**：脱敏批**未触及**二 `.py` 与锚 JSON 之字节（§2-5 之 4 件逐字节 MATCH）⇒ **该 2 锚之字节面在两机完全一致**。

### §2-7 远端镜像 manifest 之独立佐证（**第三方记录，非我方自报**）

`_september_workspace/_mirror_manifest.json`（HTTP 200／192,689 B／`e4548dc95e27`）：`zone="_september_workspace"`｜**`source="〔本地路径已脱敏〕"`**｜`generated="2026-09-20T12:50:00"`｜`files` = **701** 条。逐条摘录（本棒实测）：

| `path` | `origin` | `size` | `mtime` | `sha256` |
| :-- | :-- | --: | :-- | :-- |
| `_september_workspace/tools/llm_client.py` | `tools/llm_client.py` | **8,118** | **2026-09-09T16:16:02** | `null` |
| `_september_workspace/tools/exp_harness.py` | `tools/exp_harness.py` | **10,090** | **2026-09-09T16:16:50** | `null` |
| `_september_workspace/verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | **6,680** | **2026-09-09T13:19:32** | **`03c6c01f3697151b32b86c9016434a17c43e2c1f6db89be7641fee778b74e98a`** |
| `_september_workspace/verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` | 同名 | **5,049** | **2026-09-15T13:31:24** | **`da517c115f3c4b73b0a9cb7990676bfc82d4524f8b097f439002972811f04a75`** |

> 📌 **本棒本地独立复算之全 SHA-256 与上表 manifest 记录之 `sha256` 逐位相符**（`03c6c01f3697…98a`／`da517c115f3c…a75`）⇒ **manifest 之 mtime 记录可信，且与本地 mtime 逐位相符**（`13:19:32`／`13:31:24`／`16:16:02`／`16:16:50`）。
> ⛔ 注：manifest 之 `source` 路径与本地仓路径**同名**（`〔本地路径已脱敏〕`）⇒ 该 manifest 系**自本机仓生成**，故其与本地一致**不构成跨机独立证据**（跨机证据仍取 §2-5 之 raw 字节比对）。

### §2-8 远端全树路径穷尽（阴性通道之二）

- `tools/` 于 `main` 根：**恰 2 件** ＝ `tools/make_figures_v2.py`、`tools/make_figures_v2_en.py`（**0 载**二目标件）
- `_september_workspace/tools/`：**恰 5 件** ＝ `exp_harness.py`／`llm_client.py`／`make_figures_v2.py`／`make_figures_v2_en.py`／`read_key.py`
- 全树（3,076 blobs）中 basename 正则 `llm|harness`（不分大小写）命中 **34** 条；其中**名为 `llm_client`／`exp_harness` 之件恰 2 条**（即上述二件），**⛔ 0 任何 `.bak`／`.old`／副本**
- basename 恰为 `KT_ABC1_anchors_sha256_12.json` 之路径：**恰 1 条** ＝ `_september_workspace/verifier/handoff/KT_ABC1_anchors_sha256_12.json`（另有 `.bak_2026_09_23` 与 `_V3X_P_A_PATCH_2026_09_15` 各 1 条）
- `_movedout_manifest_2026_09_21.json`（HTTP 200／291,567 B）与 `_movedout_manifest_2026_09_28.json`（HTTP 200／2,003 B）：`llm_client`=0、`exp_harness`=0、`KT_ABC1`=0、`055e874ea5c1`=0、`9f383935c00c`=0

### §2-9 本地阴性双通道（射程 ＝ 单根 `〔本地路径已脱敏〕`，全树无剪枝除 `.git`/`__pycache__` 等）

| 通道 | 结果 |
| :-- | :-- |
| ① **路径列举** | `os.walk` 全树 **1,969 件**／`onerror` ＝ **0**；basename `llm_client.py`／`exp_harness.py` 命中 **恰 2**（`tools/llm_client.py`、`tools/exp_harness.py`）｜`_september_workspace`／`_september_workspace/tools`／其下二件 ＝ **`Test-Path=False`（4 项全 False）** |
| ② **内容／SHA-12 census** | `055e874ea5c1` **0 命中**｜`9f383935c00c` **0 命中**｜`1722500da4aa` **1 命中**（＝`tools/llm_client.py`）｜`275e480ba4d9` **1 命中**（＝`tools/exp_harness.py`） |

**⇒ 阴性射程声明**：本地阴性**仅具**「单根 `deposon-repo`（1,969 件）」之否证力；⛔ **0** 断言「全机全域 0 存在」。**运行时附件面**（`〔本地路径已脱敏〕`）之同一 census 本棒⛔ **0 复跑**（`a68b2971b8e1` §1-1 曾于三根内报「0 命中」，本棒⛔ **0 以他件结果充本棒实测**）⇒ 列为 **KD-5**。

---

## §3 根因判定

### §3-1 三假设之逐项裁（**⛔ 0 猜测·每项均附可核证据**）

| **假设** | **判定** | **可核证据（本棒实测）** |
| :-- | :-: | :-- |
| **H1 ＝ 授权漂移（09-15 `DRIFT_AUTHORIZED`）＋ 09-23 授权复位** | 🟢 **成立（且为唯一成立项）** | ① 实体变更之 OLD→NEW 逐位对应 `baef94e393de` L121–L122 逐字；② 09-15 逐项裁定 `DRIFT_AUTHORIZED` 且 9/9 PASS（`977fe1b48f75` L247–L250 逐字＋机器孪生 `e221792715f8`）；③ 09-23 复位经 PI 明示授权（`41f5f1689d09` L114／L115／L137 逐字），且**现盘锚载体字节 ＝ 复位目标 `03c6c01f3697`／6,680 B（本棒实测）**；④ **登记面自始未 reconcile**：`baef94e393de` L178 逐字「锚 JSON 本身未更新……后续如需冻结新锚，需走正式流程更新该 JSON」，且本棒实测活载体**至今仍载 OLD 值** |
| **H2 ＝ 未提交改动／近期重写** | 🔴 **排除** | ① 二件 mtime ＝ **2026-09-09 16:16:02／16:16:50**（本棒实测）② 远端镜像 manifest（`generated=2026-09-20T12:50:00`）记录之 mtime ＝ **2026-09-09T16:16:02／16:16:50**，与本地**逐位相符** ⇒ **自 2026-09-20 至本棒（2026-10-14）期间该二件未被改写**；③ 二件正文日期字面**仅** `2026-09-09`（正则 `20\d\d-\d\d-\d\d` 实测，⛔ 0 `version=` 类字面） |
| **H3 ＝ 他机差异（远端/另一机器持 OLD）** | 🔴 **排除** | ① 远端 `tools/` 直路径 **404**（双通道：contents API ＋ raw）；② 远端唯一实体在 `_september_workspace/tools/`，字节 ＝ **NEW 值**且与本地**逐字节一致**（`content_equal=True`）；③ 远端提交史：`tools/llm_client.py` 全史**仅 2 提交**，首现 `1b7531167790`（09-17）即 NEW，其父 `f7d9cf1db1bb` **404** ⇒ **OLD 值于远端任何时点 0 存在**；④ 全树 3,076 blobs basename 穷举：名为该二件者**恰 2**、⛔ 0 任何旧值副本 |

### §3-2 根因句（**结论·可核**）

> **该 2 锚不符之根因 ＝ 「实体已于 2026-09-10 经 Option A 授权返工而变更（`baef94e393de` L121–L122 逐字登记 OLD→NEW，并于 2026-09-15 逐项裁定 `DRIFT_AUTHORIZED`、9/9 PASS）＋ 登记面自始未 reconcile、且于 2026-09-23 经 PI 明示授权复位回 OLD 值」二者之合成。**
> **本棒实测排除「未提交改动」（mtime ＋ 远端镜像 manifest 双证）与「他机差异」（远端首现即新值、父提交 404、跨机字节逐位一致）两假设。**
> ⇒ 「登记 OLD vs 实测 NEW」之现势，**不是**锚被篡改、**不是**文件被偷改，而是**两轨并存**：**实体轨 ＝ 授权变更后的 NEW 值；登记轨 ＝ 冻结契约复原后的 OLD 值**。

### §3-3 本棒对 `a68b2971b8e1` §2-4 因果链之**修正登记**（**0 回改·仅勘误**）

`a68b2971b8e1` L164 载「2026-09-22 PI 卡授权 C7 修订 ⇒ 产 11,318 B 版（`6e9cd8cd8e07`……）」。**本棒实测其远端可见性如下（此前未见于任何在册件）**：

| 面 | 实测 | 与原叙述之关系 |
| :-- | :-- | :-- |
| C7 版（`6e9cd8cd8e07`／11,318 B）**进远端之时点** | **2026-09-26T14:03:15Z**（`626824bc2c11`）——**非** 09-22／09-23 | 🟡 远端可见性晚 3–4 日；**⛔ 0 断言**远端时间即本地发生时间（远端无 09-21～09-24 任何提交） |
| `.bak_2026_09_23` 之**文件名日期** | **09-23** | 🔴 **文件名日期 晚于 其进仓日期（09-26）3 日** ⇒ 存在**命名与实际动作日期之错位**，本棒如实登记为 **KD-3** |
| 主路径锚 JSON 于 **09-20**（`00e1978c6c53`）之字节 | **6,680 B／`03c6c01f3697`（＝OLD）** | 🟡 **与原叙述之张力**：原叙述称 09-23 前主路径为 11,318 B 之顶替件；而 09-20 镜像时主路径**已为 6,680 B OLD** ⇒ 二说不能同真 |
| 该张力的**可能调和**（**推断·候 PI 核准**） | 主路径 C7 顶替状态或发生于 **09-20 12:50（镜像生成）之后**、09-23 之前；镜像所摄为 C7 写入**之前**之状态 | ⛔ **0 取舍**；登记为 **KD-4**（须 PI 确认时间线） |

> ⛔ 本棒**0 回改** `a68b2971b8e1` 一字；上表为**勘误登记**（append-only 之面由本件承载）。

### §3-4 剩余未竟项（承 `a68b2971b8e1` §3-2 第 3 步，**本棒实测复核**）

| # | 未竟项 | 本棒实测状态 |
| :-: | :-- | :-- |
| 1 | `da517c115f3c` 之 `patch_status: PENDING` 之 reconcile | 🔴 **仍未竟**（活载体仍载 OLD 值，本棒实测 `P_A_LLM_CLIENT=055e874ea5c1`、`P_A_HARNESS=9f383935c00c`） |
| 2 | `baef94e393de` §六-1「需走正式流程更新该 JSON」之流程 | 🔴 **未走**（同上） |
| 3 | `da517c115f3c` L79 之 `D7_pending_question_to_parent`（patch 是否 push 给 user/〔W老师〕） | ⛔ **本棒 0 查到在册答**（远端 `_september_workspace/verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` **存在**于远端 `main`，HTTP 200／`d7e965b0affe`／5,055 B ⇒ **push 面已发生**，惟其**内容面**是否含该答，本棒⛔ **0 逐字核**） |

---

## §4 对 L263／L54 条款适用性之影响

### §4-1 两条款之字面（**本棒逐字回读·§1-4**）

- `78b71d404366` **L263**：「**任何 ≥ 1 锚漂移 → 全 KT-A1 撤回**。」
- `bd1caab42b4c` **L54**：「任何 ≥ 1 锚漂移 → 全 V0 撤回。」

### §4-2 分层判定（**字面 ＝ 真；语义 ＝ 须辨**）

| **层** | **判定** | **依据** |
| :-- | :-: | :-- |
| **① 字面条件（登记 vs 实测不符 ≥ 1）** | 🟢 **成立**（2 锚 ≥ 1） | 本棒实测：登记 `055e874ea5c1`／`9f383935c00c` vs 实测 `1722500da4aa`／`275e480ba4d9` |
| **② 「锚漂移」之语义前提（未授权之实体变更）** | 🔴 **不成立** | 根因已判为**授权返工**（§3-2）；且该漂移**已于 2026-09-15 逐项裁定 `DRIFT_AUTHORIZED`**（`977fe1b48f75` L247–L248）并判 **9/9 PASS**（L250） |
| **③ 今日再触发之性质** | 🔴 **对同一已决事实之重复处置** | 同一组 2 锚、同一组字节；既已裁定 PASS（09-15），今日若再宣告「全撤回」，则同一漂移**既 9/9 PASS 又全撤回** ⇒ **两义并存** |

### §4-3 结论（**⛔ 0 宣告生效／不生效**）

**推断结论（候 PI 核准）**：

1. **L263「全 KT-A1 撤回」**：就**本组 2 锚**而言，**推断**其**不适用**——该漂移系**已授权返工**且**已逐项裁定 `DRIFT_AUTHORIZED`**，非未授权漂移；今日触发构成对同一已决事实之重复处置。
2. **L54「全 V0 撤回」**：同上，**推断**其就本组 2 锚**不适用**；惟其射程为「全 V0」，若 PI 另裁射程，**连带面须另行核定**（**本棒 0 代裁**）。
3. **⛔ 0 宣告生效，⛔ 0 宣告不生效**：撤回之宣告与执行通道**唯一 ＝ PI 明示**（沿 `e2c35c2ac858` L141 逐字）。
4. **未竟项影响**：登记面 `patch_status: PENDING` 至今未 reconcile（§3-4）⇒ **无论 PI 如何裁，「登记 vs 实测」之不符仍将持续存在**；处置路径为**逐锚勘正＋显式登记**（`a68b2971b8e1` §3-2 之推断，本棒⛔ **0 采认**、⛔ **0 执行**）。

### §4-4 对既往在册判定之影响（**0 翻案·仅标注**）

| 在册件 | 其判定 | 本棒关系 |
| :-- | :-- | :-- |
| `36f70c0a844c`（batch7）`KD-1` | 「已触发全撤回条件」 | 🟡 **字面成立**（条件面），惟**根因面**本棒补判为授权漂移；⛔ **0 回改该件** |
| `a68b2971b8e1`（batch8）§3-1 | 「⛔ 0 执行自动触发」 | 🟢 **方向一致**；惟其因果链之 09-22／09-23 远端可见性本棒有**修正登记**（§3-3） |
| `5a72c931148a` `G7`（§5-3 L191） | 条款引作「≥1 锚漂移即全 V0 撤回」 | 🔴 **失准**（L263 字面为「全 KT-A1」）；⛔ **0 回改该在册件** |

---

## §5 遗留／KD（如实登记·0 隐匿·0 冒充结案）

### §5-1 本棒新立 KD

| # | KD | 严重度 | 本棒实测依据 | 本棒处置 |
| :-: | :-- | :-: | :-- | :-: |
| **KD-A** | 🔴 **根因已定且非 H2／H3** —— 本棒**闭合** `e2c35c2ac858` §6-4-③ 之「根因未判」缺口：根因 ＝ 授权返工＋登记面未 reconcile＋授权复位之合成；**未提交改动**与**他机差异**两假设**已排除** | **高（已闭合）** | §3-1 三假设逐项裁 | 如实判；⛔ **0 宣告**条款生效／不生效；⛔ **0 改**任何锚值或 spec 本体 |
| **KD-B** | 🔴 **登记面至今未 reconcile** —— 活载体 `03c6c01f3697` 仍载 OLD 值（实测 `P_A_LLM_CLIENT=055e874ea5c1`、`P_A_HARNESS=9f383935c00c`），`da517c115f3c` 之 `patch_status: PENDING` 未竟 ⇒ **「登记 vs 实测」之不符将持续** | **高** | 本棒实测锚 JSON 载荷（§1-3⑤ 之锚 JSON 复读／§2-3） | 如实登记；⛔ **0 改**冻结载体；⛔ **0 以**他件自报充实测 |
| **KD-C** | 🟡 **远端阴性之射程限定** —— 「OLD 值于远端任何时点 0 存在」之射程 ＝ ①路径穷举（3,076 blobs 全树，`truncated=False`，**恰 2** 条 basename 命中，⛔ 0 `.bak`）②内容通道（二路径全部相关提交之 raw 字节复算＝NEW，首现提交 `1b7531167790`、父提交 `f7d9cf1db1bb` 404）③`commits?path=` 全史（**恰 2 提交**）｜**恰 1 分支 `main`**｜⛔ **0 对远端 3,076 blobs 逐件算 SHA-12**（成本未付）⇒ ⛔ **0 断言**「OLD 值于远端全域 0 存在」 | **中**（射程限定） | §2-2／§2-3／§2-8 | 如实登记射程；结论限于所列三通道 |
| **KD-D** | 🟡 **`.bak_2026_09_23` 之文件名日期 与 进仓日期错位** —— 文件名日期 **09-23**，而其**首次进远端**为 **2026-09-26T14:03:15Z**（`626824bc2c11`）；且 `00e1978c6c53`（09-20）处该路径 **404** | **中** | §2-2 之 16／17、§2-4 | 如实登记；⛔ **0 推断**其命名动机 |
| **KD-E** | 🟡 **09-23 复位之远端 0 可见** —— 远端 `main` 在 **2026-09-21 ～ 2026-09-24 窗口内 0 提交**（实测 `commits?since=2026-09-14&until=2026-09-24` → **45** 件，末件 `29f6fd264f2a` @ 09-20T05:07:04Z）⇒ 该复位**仅本地留痕**（`41f5f1689d09` §7 ＋ 现盘锚载体字节） | **中** | §2-4 | 如实登记；⛔ **0 以**「远端无记录」反推「复位未发生」 |
| **KD-F** | 🟡 **远端 5 件 DIFF 性质之判别未完成** —— `KT_A1_SPEC`（14 块）／`P_A_D1_D3_REPORT`（3 块）经逐行判别为**脱敏改写**；惟 `P_A_EQUILIBRIUM_…_V0_SPEC`（+20 B）、`TRAE_V3_ASSET_ERRATUM`（−302 B）、`…PATCH_2026_09_15.json`（+6 B）**本棒 0 逐块展开** ⇒ ⛔ **0 断言**其性质 | **中** | §2-6 | 如实登记未判项；⛔ **0 以**「另 3 件想必同理」充判别 |
| **KD-G** | 🟡 **运行时附件面 census 本棒 0 复跑** —— `〔本地路径已脱敏〕` 之 OLD 值 census 本棒⛔ **0 执行**；`a68b2971b8e1` §2-2 曾于三根内报「0 命中」，惟本棒⛔ **0 以他件结果充本棒实测** ⇒ 该面**本棒 0 阴性证据** | **中**（射程限定） | §2-9 | 如实登记；本件核心判定**不依赖**该面 |
| **KD-H** | 🟡 **母件锚表无 `value` 列** —— `bd1caab42b4c` L48–L52 全表 4 列（锚 ID／对象／算法／字段），**⛔ 0 `value` 列**（L51／L52 之字段列载「`version=2026-09-11`」）⇒ 母件之登记值**无件内自陈源**，母子对位系**以子件锚表＋子件锚 JSON 互证**得出 | **中** | §1-4（本棒逐字回读） | 如实登记；⛔ **0 以**母件自陈值充对位源 |
| **KD-I** | 🟡 **锚面版本字面三处不一致（存续自 `e2c35c2ac858` KD-C）** —— 母件 L3「V0(冻结)+ §0.5 补丁」／子件 L5「V0.1 冻结版」／锚 JSON `metadata.spec_versions`「KT-A1: V0.2」⇒ 锚面所指版本**不唯一** | **中** | 本棒复读两 spec 与锚 JSON | 原样存续；⛔ **0 改** spec 本体／锚 JSON（frozen／只读面） |

### §5-2 存续 KD（**非本件新立·原样存续**）

| # | KD | 状态 |
| :-: | :-- | :-- |
| **KD-2** | 🔴 锚之坐标系错配未裁（`2eeb522748ca` §6，对象 ＝ **P-B** V0 spec 之锚） | 🔴 **原样存续**；本件 0 提供其调和依据（对象不同） |
| **KD-5（原 `e2c35c2ac858` KD-B）** | 🔴 母件 `bd1caab42b4c` L44 逐字所指 `verifier/handoff/P_A_V0_anchors_sha256_12.json` **实测 ABSENT** | 🔴 **原样存续**；本件⛔ **0 复跑**该件之双通道 census |

### §5-3 须 PI 给 ／ 须 PI 裁（**列名·⛔ 0 代立·0 代裁·0 代给值**）

| # | 出口 | 性质 | 本棒处置 |
| :-: | :-- | :-- | :-: |
| 1 | **本组 2 锚不符**是否宣告 **L263／L54 生效或不生效** | 须 PI 明示（**唯一通道**） | ⛔ 本棒 0 宣告 |
| 2 | 若采撤回：**射程**（L263「全 KT-A1」vs L54「全 V0」） | 须 PI 择 | 维持并列 |
| 3 | KD-A 之 **2 锚 canonical 值** | 须 PI 给（⛔ 0 给值） | 列名 |
| 4 | **登记面 reconcile** 是否执行（`patch_status: PENDING`） | 须 PI 裁 | 列名 |
| 5 | **KD-D／KD-E／KD-F** 三项时序与性质疑点之澄清 | 须 PI 给料 | 列名 |
| 6 | **停跑解除** | 须 PI 明示（**唯一通道**） | ⛔ 本棒 0 宣告 |

### §5-4 本棒 ⛔ 0 作之事项（逐条）

① ⛔ **0 回改**任何既有件一字（触动既有件数 ＝ **0**；两 spec ＋ 锚 JSON ＋ `.bak` ＋ patch ＋ 两源件 ＋ 三授权源件**一律只读**）｜② ⛔ **0 宣告**①毕｜③ ⛔ **0 宣告**停跑解除｜④ ⛔ **0 宣告**「全 KT-A1／全 V0 撤回」**已生效或不生效**｜⑤ ⛔ **0 代裁／0 代择／0 代给值**｜⑥ ⛔ **0 采认**任何推断值或草案（全篇标「**候 PI 核准**」）｜⑦ ⛔ **0 改**任何锚值或 spec 本体｜⑧ ⛔ **0 远端写／0 上传／0 推送**（远端调用**仅 GET**，**⛔ 0 PAT**）｜⑨ ⛔ **0 读** `.env`｜⑩ ⛔ **0 移动／重命名／删除**任何件｜⑪ ⛔ **0 以**他人名头署名（署 `evidence-auditor`）｜⑫ ⛔ **0 断言**「OLD 值全机／全域 0 存在」（射程见 KD-C／KD-G）｜⑬ ⛔ **0 以**远端镜像 manifest（`source` 路径与本地同名）充**跨机**独立证据（跨机证据取 raw 字节比对）｜⑭ ⛔ **0 翻案**（`36f70c0a844c` `KD-1`、`5a72c931148a` `G7` 皆**仅标注 0 回改**）

---

## §6 落盘自测（字节级·落盘后复算）

| 项 | 值 |
| :-- | :-- |
| 目标路径 | `results/_kt_a1_anchor_drift_root_cause_2026_10_14.md` |
| `Test-Path`（落盘前） | **False** |
| glob `results/*root_cause*`（落盘前） | **0 命中** |
| 占用改名 | **未触发**（`_r1` 亦 0 占用） |
| `sha256[:12]` | **本棒落盘后实测 ＝ 见交付回执**（自哈希不可内嵌本文件——写入即改变其字节与哈希） |
| bytes | **本棒落盘后实测 ＝ 见交付回执**（同上，自引用不可内嵌） |
| BOM | **无**（UTF-8 无 BOM） |
| 行尾 | **纯 LF**；**CRLF ＝ 0**；**CR ＝ 0** |
| TAB | **0** |
| CTRL（除 `\n`） | **0** |
| `nonAscii` | **> 0**（**字符口径**；**字节口径**亦 > 0，均为中文正文与全角标点） |
| `U+FFFD` | **0** |

---

**署名**：`evidence-auditor`｜**件日**：2026-10-14｜**状态**：**候 PI 核准**（全篇推断与处置建议）