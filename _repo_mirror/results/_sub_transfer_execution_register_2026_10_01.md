# sub 方向转移 · 执行登记件（2026-10-01 · 10 件「可移」执行）

- **棒别**：sub 方向转移执行棒（**worker**）· parent 派工（2026-10-01 晚）
- **出证方**：**worker**（本棒实际执行者）。⛔ 0 冒充 PI / doc-writer / verdict-keeper / verifier / Mavis 团队 / Trae code / KIMI / GLM / coze 等任一他棒或受托方。
- **本件性质**：**执行登记件**（非预登记件、非判定件、非实验结果件）。
- **件名**：`results/_sub_transfer_execution_register_2026_10_01.md`（**新名 · 无 `_vN_` 阶段前缀**，沿 PI 09-29 命名裁）
- **版式**：UTF-8 无 BOM · LF
- **纪律**：0 编造｜0 代裁｜R4（**0 读 key／0 读 `.env`／0 落盘凭据**）｜SHA-12 一律 `sha256[:12]` **小写**
- **落盘前撞名实测**：`Test-Path results\_sub_transfer_execution_register_2026_10_01.md` ⇒ **False**；全仓递归同名扫描 **0 命中**；`results/*sub_transfer*` ＋ `*execution_register*` 近名仅 `_proxy_signoff_execution_register_2026_10_01.md`（**0 同名**）⇒ **0 覆写**
- **产出**：**1 件即停**（本件为唯一新增件；转移动作及其目录不计件）

---

## §0 执行授权（批复照录 · L1）

| 项 | 登记 |
|---|---|
| **批复卡** | **`ask_b2f7077749a8ffcec839f483`** |
| **批复来源** | PI 2026-10-01 晚对盘点件复核卡作答，**由 parent 转录**（本棒 0 持有该 `ask_*` 工具、**0 编造卡号**） |
| **① 裁项** | **甲 · 批移** —— 批准执行盘点件 `results/_sub_transfer_candidates_2026_10_01.md`（`2f61c0aa2a2b`）§2 之 **10 件「可移」**之转移 |
| **② 裁项** | **甲 · 不计** —— **体量枚举件不计为权威引用面**，⇒ 维持盘点件 §5.1 之「可移」判读（该判读点为盘点件自裁最敏感处，PI 明确采纳） |
| **执行依据件** | `results/_sub_transfer_candidates_2026_10_01.md`（`2f61c0aa2a2b`／21,796 B） |
| **⛔ 0 代 PI 扩围** | 本棒**仅执行该 10 件**；「需 PI 裁」18 项、「不可动」48 件**一律 0 触动** |

---

## §1 移前复核闸（引用面重验 · 边界条件执行）

盘点完成（19:24）至执行（19:45）间隔 **21 分钟**，其间有并发会话写入 ⇒ **本棒于移动前对 10 件逐件重扫权威引用面**（权威面 **1,955 件**，较盘点时 +1）。

### §1.1 原始命中 vs 扣除噪声面（PI 甲・不计 已裁）

| 件 | 原始命中 | 扣除体量枚举件后 | 判读 |
|---|---:|---:|---|
| `README_V1_LEGACY.md` | 3 | **3** | 3 件 ＝ 盘点时已知 2 件 ＋ **本棒盘点件自身**（自引用，预期）；**0 新增外部依赖** |
| `_v4_wide_*`（7 件）／`_v4_wt_s5_verify` | 各 3 | **0** | 3 件命中**全为**体量枚举件（上传台账 ＋ 2 份 baseline 快照）⇒ 按 PI 甲・不计 **不计** |
| `verifier/volcengine_补测_worker_A_2026_09_10.py` | 0 | **0** | 全程 0 命中 |

> **闸门结论：10/10 件引用面与盘点结论一致 ⇒ 0 件触发「跳过不移动」边界条件，10 件全部照移。**

### §1.2 落位 0 覆盖实测

目标根 `deposon-sub\tmp_movedout_2026_10_01\` **已存在**（今日 16:32 建，内含 WT2 终枚举表 1 件）。本棒新建 4 个子目录，**均为新建 0 重名**：

| 子目录 | 落前 `Test-Path` | 落前件数 |
|---|---|---:|
| `legacy_caliber\` | False | 0 |
| `process_scripts\` | False | 0 |
| `process_scripts\v4_wide_2026_09_27\` | False | 0 |
| `process_scripts\v4_wt_2026_09_27\` | False | 0 |

逐件 `dest_exists` **10/10 ＝ False** ⇒ **0 覆盖任何既有件**。

---

## §2 逐件移动清单（移前／移后指纹）

- **动作窗口**：`2026-10-01 19:45:03` → `19:45:03`（**单批 10 件，0 并行移动**）
- **方式**：`shutil.move`（**移动非复制** ⇒ 源路径 0 存在、可逆、0 覆盖）
- **复核**：`bad=0`、`src_gone` 10/10、`sha_match` 10/10、`size_match` 10/10

| # | 源（repo 内） | SHA-12（移前＝移后） | 字节 | mtime | 目标（sub 内） | 结果 |
|---:|---|---|---:|---|---|:--:|
| 1 | `README_V1_LEGACY.md` | `18e095c85427` | 3,756 | 08-23 07:47 | `tmp_movedout_2026_10_01/legacy_caliber/README_V1_LEGACY.md` | ✅ |
| 2 | `deposon_team/plugins/_v4_wide_s1b_inv2_2026_09_27.py` | `af475f496a5e` | 1,546 | 09-27 20:18 | `…/process_scripts/v4_wide_2026_09_27/_v4_wide_s1b_inv2_2026_09_27.py` | ✅ |
| 3 | `deposon_team/plugins/_v4_wide_s3_keyscan_2026_09_27.py` | `a32af07111df` | 2,647 | 09-27 20:19 | `…/v4_wide_2026_09_27/_v4_wide_s3_keyscan_2026_09_27.py` | ✅ |
| 4 | `deposon_team/plugins/_v4_wide_s3b_uuidctx_2026_09_27.py` | `8fdec59aa96b` | 1,707 | 09-27 20:20 | `…/v4_wide_2026_09_27/_v4_wide_s3b_uuidctx_2026_09_27.py` | ✅ |
| 5 | `deposon_team/plugins/_v4_wide_s3c_keydetail_2026_09_27.py` | `16ae5764add1` | 2,490 | 09-27 20:20 | `…/v4_wide_2026_09_27/_v4_wide_s3c_keydetail_2026_09_27.py` | ✅ |
| 6 | `deposon_team/plugins/_v4_wide_s4_verify_2026_09_27.py` | `dbe00430d769` | 2,812 | 09-27 20:25 | `…/v4_wide_2026_09_27/_v4_wide_s4_verify_2026_09_27.py` | ✅ |
| 7 | `deposon_team/plugins/_v4_wide_s6_unrefscan_2026_09_27.py` | `1b31a3111a86` | 2,495 | 09-27 20:26 | `…/v4_wide_2026_09_27/_v4_wide_s6_unrefscan_2026_09_27.py` | ✅ |
| 8 | `deposon_team/plugins/_v4_wide_s8_fix3_2026_09_27.py` | `051dbdb121c9` | 3,514 | 09-27 20:26 | `…/v4_wide_2026_09_27/_v4_wide_s8_fix3_2026_09_27.py` | ✅ |
| 9 | `deposon_team/plugins/_v4_wt_s5_verify_2026_09_27.py` | `736e56cd5553` | 4,950 | 09-27 20:08 | `…/process_scripts/v4_wt_2026_09_27/_v4_wt_s5_verify_2026_09_27.py` | ✅ |
| 10 | `verifier/volcengine_补测_worker_A_2026_09_10.py` | `20b8a2f54ad9` | 16,252 | 09-16 11:01 | `…/process_scripts/volcengine_补测_worker_A_2026_09_10.py` | ✅ |
| | **合计** | **10 件** | **42,169** | | | **10/10 OK** |

> **与盘点件预测值一致**：盘点件 §3.1 之「可移 10 件／42,169 B」**逐字节吻合**。

---

## §3 落位索引（source → dest 逐件映射）

| # | 源路径 | 目标路径 | SHA-12 | 字节 |
|---:|---|---|---|---:|
| 1 | `D:\私人资料\deposon-repo\README_V1_LEGACY.md` | `D:\私人资料\deposon-sub\tmp_movedout_2026_10_01\legacy_caliber\README_V1_LEGACY.md` | `18e095c85427` | 3,756 |
| 2 | `…\deposon-repo\deposon_team\plugins\_v4_wide_s1b_inv2_2026_09_27.py` | `…\deposon-sub\tmp_movedout_2026_10_01\process_scripts\v4_wide_2026_09_27\_v4_wide_s1b_inv2_2026_09_27.py` | `af475f496a5e` | 1,546 |
| 3 | `…\deposon-repo\deposon_team\plugins\_v4_wide_s3_keyscan_2026_09_27.py` | `…\tmp_movedout_2026_10_01\process_scripts\v4_wide_2026_09_27\_v4_wide_s3_keyscan_2026_09_27.py` | `a32af07111df` | 2,647 |
| 4 | `…\deposon_team\plugins\_v4_wide_s3b_uuidctx_2026_09_27.py` | `…\v4_wide_2026_09_27\_v4_wide_s3b_uuidctx_2026_09_27.py` | `8fdec59aa96b` | 1,707 |
| 5 | `…\deposon_team\plugins\_v4_wide_s3c_keydetail_2026_09_27.py` | `…\v4_wide_2026_09_27\_v4_wide_s3c_keydetail_2026_09_27.py` | `16ae5764add1` | 2,490 |
| 6 | `…\deposon_team\plugins\_v4_wide_s4_verify_2026_09_27.py` | `…\v4_wide_2026_09_27\_v4_wide_s4_verify_2026_09_27.py` | `dbe00430d769` | 2,812 |
| 7 | `…\deposon_team\plugins\_v4_wide_s6_unrefscan_2026_09_27.py` | `…\v4_wide_2026_09_27\_v4_wide_s6_unrefscan_2026_09_27.py` | `1b31a3111a86` | 2,495 |
| 8 | `…\deposon_team\plugins\_v4_wide_s8_fix3_2026_09_27.py` | `…\v4_wide_2026_09_27\_v4_wide_s8_fix3_2026_09_27.py` | `051dbdb121c9` | 3,514 |
| 9 | `…\deposon_team\plugins\_v4_wt_s5_verify_2026_09_27.py` | `…\process_scripts\v4_wt_2026_09_27\_v4_wt_s5_verify_2026_09_27.py` | `736e56cd5553` | 4,950 |
| 10 | `…\deposon-repo\verifier\volcengine_补测_worker_A_2026_09_10.py` | `…\process_scripts\volcengine_补测_worker_A_2026_09_10.py` | `20b8a2f54ad9` | 16,252 |

**入库时点**：`2026-10-01 19:45:03`　**入库量**：**10 件／42,169 B**　**目标根既有内容**：WT2 终枚举表 1 件（**0 触动**）

---

## §4 拉回路径（入库必索引 · 可拉回）

**转移为移动而非复制**（`src_gone` 10/10）⇒ **拉回 ＝ 反向移动**，0 数据丢失、0 覆盖风险，单批 `shutil.move` 即可原位复原。

| 目标件 | 拉回路径（复原后 SHA-12 应为 §2 同值） |
|---|---|
| `legacy_caliber\README_V1_LEGACY.md` | `D:\私人资料\deposon-sub\tmp_movedout_2026_10_01\legacy_caliber\` → `D:\私人资料\deposon-repo\` |
| `v4_wide_2026_09_27\_v4_wide_s{1b_inv2,3,3b_uuidctx,3c_keydetail,4_verify,6_unrefscan,8_fix3}_2026_09_27.py`（7 件） | `D:\私人资料\deposon-sub\tmp_movedout_2026_10_01\process_scripts\v4_wide_2026_09_27\` → `D:\私人资料\deposon-repo\deposon_team\plugins\` |
| `v4_wt_2026_09_27\_v4_wt_s5_verify_2026_09_27.py` | `…\process_scripts\v4_wt_2026_09_27\` → `D:\私人资料\deposon-repo\deposon_team\plugins\` |
| `process_scripts\volcengine_补测_worker_A_2026_09_10.py` | `…\process_scripts\` → `D:\私人资料\deposon-repo\verifier\` |

---

## §5 连带影响如实登记（路径漂移 · 0 回改）

移动使 3 处**在盘路径引用**指向已迁出件。依 09-29 §6.1-⑤ 路径漂移口径与盘点件 §5.4 同款判读：**本棒 0 回改任何既有件**，仅在此登记。

| 漂移面 | 仍指向旧路径之件 | 性质 | 处置 |
|---|---|---|---|
| `README_V1_LEGACY.md` | `results/_batch3_receipt_kimi_2026_10_01.md`；`results/_forgotten_items_quick_sweep_register_2026_10_01.md`；`results/_sub_transfer_candidates_2026_10_01.md`（**本棒盘点件自身**） | **真实路径引用**（3 件，均为今日登记件 ＋ 本棒件） | **0 回改**；待 PI 或下棒择机统一更正（沿今日整理件 §7.4-③ 同款口径） |
| 8 件脚本 | `results/_upload_ledger_kimi_2026_09_30.json`；`deposon-sub/tmp_movedout_2026_09_29/…/baseline_pre.json` ＋ `baseline_post.json` | **体量枚举面**（PI 甲・不计项） | **0 回改**；上传台账内该 9 条路径现为陈旧项，如实登记 |
| `_v4_wt_s5_verify` 族内引用 | 0 | 无族内引用者 | — |

⚠️ **连带提示**：`deposon_team/plugins/_v4_wide_s2_scan_2026_09_27.py`（`c2cc22b27047`，**「需 PI 裁」· 本棒 0 触动**）曾引用已迁出之 `_v4_wide_s3_keyscan_2026_09_27.py` ⇒ 该引用现为**悬空**。若 PI 日后裁移 `s2_scan`，宜**同族同批**以保全族内引用（沿盘点件 §2.4 族级判定）。

---

## §6 目录终态实测

| 目录 | 落前 | 落后 | 说明 |
|---|---:|---:|---|
| `deposon-repo\deposon_team\plugins\` | 85 件 | **77 件** | −8 ＝ 本棒 `_v4_wide_*` 7 ＋ `_v4_wt_s5_verify` 1 ✅ |
| `deposon-repo\verifier\` | 117 件 | **116 件** | −1 ＝ 本棒 `volcengine_补测_worker_A` 1 ✅ |
| `deposon-sub\tmp_movedout_2026_10_01\` | 1 件 | **11 件** | ＋10 件 ＝ 本棒转入；既有 WT2 表 1 件 **0 触动** ✅ |

**落位树实测**：`legacy_caliber/` 1 件｜`process_scripts/` 1 件｜`process_scripts/v4_wide_2026_09_27/` 7 件｜`process_scripts/v4_wt_2026_09_27/` 1 件｜（根）既有 1 件。

---

## §7 纪律自证

| 项 | 状态 |
|---|---|
| **仅执行获批 10 件** | 「需 PI 裁」18 项、「不可动」48 件**0 触动**；`docs/V3X/` P_D 规范链 0 触动 |
| **⛔ 0 删除 0 联网** | 全棒 0 删除、0 trash、0 网络请求 |
| **⛔ 0 回改既有件** | 全仓只读（除 10 件移动）⇒ 体例源二件 SHA-12 复核一致（见 §7.1） |
| **0 触并发在跑面** | 移动窗口 19:45:03 单批完成；`results/` 今日件 0 读 0 写 0 移 |
| **R4 永不明文** | **0 读 key／0 读 `.env`／0 落盘凭据**；本棒 0 读任一被移件之内容（仅字节流复算指纹） |
| **署名如实** | 出证方 ＝ **worker** |
| **命名合规** | 本件名无 `_v5_` 类阶段前缀；新建目录名沿既有 `tmp_movedout_*` 惯例，**非新增阶段名** |
| **撞名实测** | 落盘前 False ＋ 全仓 0 同名 ⇒ 0 覆写 |
| **探针落盘** | 全部脚本落 `%TEMP%`，**0 落盘仓内**、0 进交付面 |

### §7.1 0 回改复核（执行依据件 ＋ 体例源 · 实测）

| 件 | 字节 | SHA-12 实测 | 与登记值 | 结论 |
|---|---:|---|---|:--:|
| `results/_sub_transfer_candidates_2026_10_01.md`（执行依据） | 21,796 | `2f61c0aa2a2b` | `2f61c0aa2a2b` | **一致 ⇒ 0 回改** ✅ |
| `results/_cleanup_round2_register_2026_09_29.md`（体例源） | 36,245 | `ee47a2ec49f4` | `ee47a2ec49f4` | **一致 ⇒ 0 回改** ✅ |
| `results/_cleanup_round_2026_10_01.md`（体例源） | 27,477 | `0db6e5d6146c` | `0db6e5d6146c` | **一致 ⇒ 0 回改** ✅ |

---

## §8 落盘自证

| 项 | 值 |
|---|---|
| 路径 | `results/_sub_transfer_execution_register_2026_10_01.md`（**新名 · 无版本前缀**） |
| 版式 | **UTF-8 无 BOM · LF** |
| 产出件数 | **1 件即停**（本件为唯一新增件） |
| 派生件 | **0 JSON · 0 脚本 · 0 仓内临时件** |
| 既有件触动 | **0**（除 §2 明列 10 件移动） |
| 自核 | SHA-12／字节／行数 **见交付回执**（沿既有件惯例不自写入本件） |

---

**落款**：**worker** · 2026-10-01｜**转移 10 件／42,169 B（10/10 OK · bad=0）**｜0 删除 0 联网 0 回改既有件 · R4 0 读 key · 0 派工 · **产出 1 件即停**｜**待 PI 复核：§5 路径漂移 3 处（0 回改，登记待统一更正）、§4 拉回路径、§5 连带提示（`s2_scan` 若裁移宜同族同批）**
