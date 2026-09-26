# V4 证据链审计 reconcile 报告 · 4 疑点逐条实测定案

> **派工**：evidence-auditor（agent-11335500b168 · 证据链审计专职）
> **触点锚**：`docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`（v15 SHA-12 `6844BF36F762`）§21.6 E-32.6 待核疑点 3 条 + 派工单补 1 条（mapping 字面错）= **共 4 条**
> **性质**：只读实测审链报告；不动任何既有件（含 batch2_r2_result.json / batch2_r2_executor.py / mapping.md / cleanup v3 棒 / T1 verdict / T1 result / batch1_r6_result 等全部链上件）
> **边界**：R5 V4 frozen 只追加 / V1-V3 只读不动 / 派生 JSON 不合并 / 不覆盖既有件 / 0 擅调阈值 / key 永不明文（无例外）

---

## A. 摘要表（4 条定案一览）

| # | 疑点 | 链记录字面值 | 盘实测值 | 一致? | 定案根因 | 处置建议 |
|:-:|---|---|---|---|---|---|
| **1** | batch1_r6 result SHA 链/盘双记 | SHA-12 `A4F851154551` / 58,369 B | SHA-12 `6B92BBFF7180` / 57,925 B | **❌ 不一致**（SHA + bytes 双漂） | 文件**被重写**（CreationTime 2026-09-24 22:08:45 vs LastWriteTime 2026-09-25 00:27:42；后改 -444 B）；mapping.md 创建于 23:14:26（在原 drop 与改写之间），故记录原值 | E-32.6 #1 勘误追加式补「modify_after_drop」+ 双 SHA 字面登记；不动文件本体（R5 frozen 触禁） |
| **2** | mapping 文件 L19/L20 SHA 字面错 | L19 `CB37B699FF73`（result）/ L20 `5BE9DFE83A27`（executor） | L19 → `8C125E257AF8` / L20 → `E7418F47A130` | **❌ 不一致**（bytes 一致 62,887 B + 55,317 B；仅 SHA 错） | mapping 起草时**哈希算错**（非文件被改；mapping 文件 SHA-12 `98A779D61C1E` 与登记一致 = 未触动） | E-32.6 #2 勘误追加式补「mapping 文件 hash 字面错」+ 实际盘 SHA 字面登记；mapping.md 按 R5 不擅改；batch8_r1_result.json L163 已披露一致事实 |
| **3** | 清理 v3 棒 archive/sub 目录误报 | `_non_upload_local_archive` 不存在 (0) / `deposon-sub` 不存在 (0)（相对路径基准 `D:/私人资料/deposon-repo/`） | archive `D:/私人资料/_non_upload_local_archive` = **1,669 件** / sub `D:/私人资料/deposon-sub` = **441 件**（**仓外父级路径**） | **❌ 不一致**（误报） | **相对路径基准错**——清理 v3 棒以 `D:/私人资料/deposon-repo`（workspace）为基准解析相对路径，但 archive/sub 实为 repo **兄弟目录**（父级 `D:/私人资料/`） | E-32.6 #2（已登记 1,669 + 441）保留 + 增补「路径基准错」根因 + 处置「v3 棒产物为历史事实保留不动」 |
| **4** | T1 verdict / result 锚标错（清理 v3 棒 L37 / L44 / L220） | cleanup v3 棒标 `D6CB03A4657E` = T1 verdict 锚 + `F1B5E49F3058` = T1.5 锚（非 T1 verdict） | `D6CB03A4657E` = `results/_v4_supp_t1_result.json` (82,365 B) / `F1B5E49F3058` = `results/_v4_supp_t1_verdict.md` (27,538 B) | **❌ 不一致**（cleanup v3 棒**标签互换**：t1_verdict 实是 F1B5E49F3058，非 D6CB03A4657E） | cleanup v3 棒**两处字段填写错**：(a) L37 把 `add_T1_2026_09_24.md` 的 SHA-12 `802DECE2286A` + 字节 52,942 错填到 t1_verdict.md 名下；(b) 因 (a) 推断 F1B5E49F3058 不属 t1_verdict，错误重路由到 T1.5（grep 命中 t15_* 是 T1.5 对 T1 verdict 的正向引用，非 T1.5 自锚） | E-32.6 #3 勘误追加式补正确映射：F1B5E49F3058=T1 verdict.md / D6CB03A4657E=T1 result.json / 802DECE2286A=add_T1_2026_09_24.md（不动 cleanup v3 棒；为历史事实保留） |

---

## B. 逐条实测证据

### B.1 case #1 — batch1_r6 result SHA 漂移双记

**链记录字面值**（来自 `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` L17）：

| 件 | SHA-12 | 字节 |
|---|---|---|
| batch1 r6 result（kimi 实测） | `A4F851154551` | 58,369 |

**盘实测字面值**（`Get-FileHash -Algorithm SHA256` 独立复算）：

```
SHA256          6B92BBFF718011321C03D49085710A97DDC02FB40645F77148782160E37DAE79
SHA-12          6B92BBFF7180
Length          57,925
LastWriteTime   2026-09-25 00:27:42
CreationTime    2026-09-24 22:08:45
```

**差异分析**：

| 维度 | 链记录 | 盘实测 | 差 |
|---|---|---|---|
| SHA-12 | `A4F851154551` | `6B92BBFF7180` | 全 12 hex 位差异 |
| 字节 | 58,369 | 57,925 | -444 B |
| 时间戳 | — | CreationTime 22:08:45 / LastWriteTime 00:27:42 | **重写跨度 2h19m** |

**对照链回溯**（下游链上件均引原 SHA）：

| 文件 | 行号 | 引用 SHA | 实测 |
|---|---|---|---|
| `results/_v4_supp_l14v3_model_mapping_2026_09_24.md` | L17 | `A4F851154551` (58,369 B) | mapping 创建 2026-09-24 23:14:26（在原 drop 后、改写前） |
| `results/_v4_supp_l14v3_batch2_r6_result.json` | L28 | `A4F851154551` | 23:50:52（同 mapping，引用原 SHA） |
| `results/_v4_supp_l14v3_batch3_r1_result.json` | L22 | `A4F851154551` | 引用原 SHA |
| `results/_v4_supp_l14v3_batch1_r6_executor.py` | (SHA-12 `5F02C7E0F094` / 47,242 B) | 同盘实测 | **executor 未触动**（CreationTime = LastWriteTime = 21:59:06）✓ |

**根因判定**（诚实的根因是不误导）：文件**被重写**于 2026-09-25 00:27:42，触发 -444 字节内容变更。mapping.md（23:14:26）+ batch2_r6_result.json（23:50:52）等下游链上件均在**改写前**完成，故均锁定原 SHA `A4F851154551`（58,369 B）。改写时点（00:27:42）后无任何链上件重新登记新 SHA，故下游链 reference 全部 stale。

**与链管理原则冲突**（V4 §3.1 + R5 重建 V4 frozen + 不覆盖既有件）：result.json 按 R5 应只追加；本次改写若为「内容修正」（如增 `kimi_distill_side_round1_finish` 块 / 调整字段），则触发 frozen 件重算链断；若为「意外覆盖」，则更严重（无 chain manifest 变更记录）。

**改写内容性质（未能逆向对照）**：本审链报告不动文件本体，故不逆向 diff；仅记录「-444 字节差异」事实 + 「无 chain manifest 重登记」事实。PI 处置路径见 §C.1。

### B.2 case #2 — mapping 文件 L19/L20 SHA 字面错

**mapping 文件本体实测**：

```
SHA256          98A779D61C1ED0862A84A376A5C2367B0057DCB135C3E7ABBD940CE8E35692EC
SHA-12          98A779D61C1E     ← 与登记一致 ✓
Length          48,028
LastWriteTime   2026-09-24 23:14:26
```

mapping 文件本身 SHA = `98A779D61C1E` 与登记一致 → mapping 文件**未被触动**；其 L19/L20 SHA 字面错源于起草时算错。

**L19/L20 字面 vs 盘实测对照**：

| 行 | 件 | mapping 字面 | 盘实测 SHA-12 | 盘实测字节 | bytes 一致? | SHA 一致? |
|:-:|---|---|---|---|:-:|:-:|
| L19 | `results/_v4_supp_l14v3_batch2_r2_result.json` | `CB37B699FF73` | `8C125E257AF8` | 62,887 | ✓（62,887 = 62,887） | ❌ |
| L20 | `results/_v4_supp_l14v3_batch2_r2_executor.py` | `5BE9DFE83A27` | `E7418F47A130` | 55,317 | ✓（55,317 = 55,317） | ❌ |

**bytes 一致 → SHA 差异非文件修改**——两个底层件（result.json + executor.py）均**未变动**；SHA 差异源于 mapping 起草时的算错。

**下游已披露事实**（沿 R5 frozen 不擅改 + 不擅自回改 mapping 文件，已在 batch8 棒诚实交代）：

- `results/_v4_supp_l14v3_batch8_r1_result.json` L163 字段 `mapping_sha12_discrepancy_note`：
  > "mapping 文件 L19 字面 batch2_r2_result_sha12 = CB37B699FF73, L20 字面 batch2_r2_executor_sha12 = 5BE9DFE83A27；实际盘上 SHA-12 = 8c125e257af8 (result) + e7418f47a130 (executor)；两处 bytes 字面一致 (result=62,887 / executor=55,317)，故为 mapping 起草时 hash 算错而非文件被改；mapping 文件按 R5 不擅改；本棒按实际盘上 SHA-12 记录并老实交代不一致；PI 复核时按实际盘上 SHA-12 字面为准"

**根因判定**：mapping 起草时 hash 算错（**起草类失灵**，非执行类失灵）；mapping 文件按 R5 frozen 触禁 + 已被下游 batch8_r1_result.json 诚实交代披露 → **无需修改 mapping**，仅 E-32.6 补登记。

### B.3 case #3 — 清理 v3 棒 archive / sub 目录误报

**清理 v3 棒 §F 表（L253-262）字面值**：

| 目录 | 路径 | 存在 | 文件数 |
|---|---|:-:|:-:|
| `_non_upload_local_archive` | `D:/私人资料/deposon-repo/_non_upload_local_archive` | **False** | 0 |
| `deposon-sub` | `D:/私人资料/deposon-repo/deposon-sub` | **False** | 0 |

**盘实测字面值**（`Test-Path` + `Get-ChildItem -Recurse -File`）：

| 路径 | Test-Path | 文件数（递归） |
|---|:-:|:-:|
| `D:/私人资料/deposon-repo/_non_upload_local_archive` | False | 0 |
| `D:/私人资料/deposon-repo/deposon-sub` | False | 0 |
| `D:/私人资料/_non_upload_local_archive` | **True** | **1,669** |
| `D:/私人资料/deposon-sub` | **True** | **441** |

**根因判定（与用户假设一致）**：**相对路径基准错**——清理 v3 棒以 workspace 根 `D:/私人资料/deposon-repo` 为基准解析相对路径 `_non_upload_local_archive` / `deposon-sub`，但两目录实为 repo **兄弟目录**（父级 `D:/私人资料/`），非 repo 子目录。v3 棒 lookup 路径时未跨出 workspace 边界外探 + 未识别仓外父级路径存在性。

**对照 E-32.6 已登记事实**：§21.6 E-32.6 #2 已登记「archive = 1,669 件 / sub = 441 件」字面值；§21.7.5 §F 核验实测 24,491 B 与 6F3F6FA3AB1D 一致。本审链**复算确认 1,669 / 441 字面值无误** + **补充根因「相对路径基准错」**。

**用户预期数 vs 实际**：用户预期「1230+ / 441+」，实测 1,669 / 441（1669 ≥ 1230 ✓，441 ≥ 441 ✓ 一致）。E-32.6 #2 登记的 1,669 字面值正确，本审链仅补「相对路径基准错」根因标注，不调整已登记数字。

**v3 棒处置**：v3 棒产物为历史事实（已落盘 `6F3F6FA3AB1D` / 24,491 B），按 R5 frozen 不擅改 + 不回改 v3 棒产物；仅 E-32.6 勘误追加根因说明。

### B.4 case #4 — T1 verdict / result 锚标错（cleanup v3 棒 L37 / L44 / L220 标签互换）

**cleanup v3 棒 §F 字面值（错）**：

| 行 | cleanup v3 棒字面 | 实测 SHA-12 | 实测字节 | 实测件 |
|:-:|---|---|---|---|
| L37 | T1 verdict `results/_v4_supp_t1_verdict.md` (52,942 B / SHA-12=`802DECE2286A`) | `F1B5E49F3058` | 27,538 | t1_verdict.md |
| L37 | （未明列 add_T1） | `802DECE2286A` | 52,942 | `_v4_supp_prereg_v02_add_T1_2026_09_24.md` |
| L38 | T1 result `results/_v4_supp_t1_result.json` (82,365 B / SHA-12=`D6CB03A4657E`) | `D6CB03A4657E` | 82,365 | t1_result.json ✓ |
| L44 / L220 | "F1B5E49F3058 系 T1.5 (`_v4_supp_t15_*`) 的 SHA-12 锚 ... 非 T1 verdict 标识" | `F1B5E49F3058` | 27,538 | **t1_verdict.md**（非 T1.5） |

**t1_verdict.md 自报 SHA 表（L13-18，与 cleanup v3 棒对照）**：

| 件 | 路径 | 自报 SHA-12 | 盘实测 SHA-12 | 字节 | 状态 |
|---|---|---|---|---|---|
| T1 result | `results/_v4_supp_t1_result.json` | `D6CB03A4657E` | `D6CB03A4657E` | 82,365 | ✓ |
| T1 executor | `results/_v4_supp_t1_executor.py` | `A7CAD9228B0B` | `A7CAD9228B0B` | 59,967 | ✓ |
| T1 prereg | `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` | `802DECE2286A` | `802DECE2286A` | 52,942 | ✓ |
| T1 activation | `results/_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` | `79936B630015` | `79936B630015` | 14,234 | ✓ |

t1_verdict.md 自报 SHA 表**自洽**（t1_result.json = D6CB03A4657E；add_T1 = 802DECE2286A；自件 SHA 未列因自指回环）。

**F1B5E49F3058 grep 命中分布**：

| 件 | F1B5E49F3058 出现语义 |
|---|---|
| `results/_v4_supp_t1_verdict.md` (本体) | 自身 SHA-12（disk 实测） |
| `results/_v4_supp_t15_verdict.md` L21 / L31 / L45 / L62 / L123 / L149 / L318 / L397 / L432 / L467 / L475 | **T1.5 → T1 verdict 正向引用**（T1 verdict SHA = F1B5E49F3058） |
| `.tmp/_t15_inspect7_out.txt` L18 + `.tmp/_t15_inspect7.py` L39 | T1.5 inspect 脚本对 T1 verdict SHA 的 print（实测引用） |
| `results/_v4_noise_cleanup_manifest_v3_2026_09_25.md` L44 / L220 / L292 | cleanup v3 棒**错把 T1 verdict 的 SHA 归属到 T1.5** |

**根因判定（cleanup v3 棒内部两处字段填写错，链成「标签互换」假象）**：

1. **错 1**：L37 把 `add_T1_2026_09_24.md` 的 SHA-12 `802DECE2286A` + 字节 52,942 错填到 t1_verdict.md 名下（可能因 add_T1 与 t1_verdict 在文件系统命名相近 + 字段未交叉核对）
2. **错 2**：L44 因错 1 推断「t1_verdict 实际 SHA ≠ 802DECE2286A，故 F1B5E49F3058 不是 t1_verdict」+ grep F1B5E49F3058 命中 t15_* 件（正向引用）→ 错误地将其重路由到 T1.5 自锚
3. **净效应**：cleanup v3 棒**标签互换**——实情是 F1B5E49F3058 = t1_verdict.md，D6CB03A4657E = t1_result.json，但 v3 棒反写为「D6CB03A4657E = T1 verdict 锚 / F1B5E49F3058 = T1.5 锚」

**用户预期 vs 实测**：用户预期「F1B5E49F3058 = T1 verdict ✓ / D6CB03A4657E = T1 result / 该棒标签互换」**全部命中**。本审链仅记录 cleanup v3 棒事实 + 复算证据。

**v3 棒处置**：v3 棒产物为历史事实（已落盘 `6F3F6FA3AB1D` / 24,491 B），按 R5 frozen 不擅改；E-32.6 #3 勘误追加式补正确映射字面。

---

## C. 处置建议（勘误追加式字面草案 · 不动既有件）

> **边界**：本审链报告**不动任何既有件**；以下草案为 E-32.6 追加节字面建议，由 doc-writer（agent-0032834a3e04）后续落盘到 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` v15+ 追加节（v15 SHA-12 `6844BF36F762` 后）。

### C.1 §21.6 E-32.6 #1 — batch1_r6 result SHA 漂移

**勘误字面草案**（追加于 §21.6 E-32.6 #1 行后）：

> **定案（evidence-auditor 实测 2026-09-26）**：
> - 链记录（mapping.md L17 + batch2_r6_result.json L28 + batch3_r1_result.json L22 等下游件）= SHA-12 `A4F851154551` / 58,369 B（**原 drop 字面**）
> - 盘实测 = SHA-12 `6B92BBFF7180` / 57,925 B（**改写后字面**）
> - 字节差 = -444 B；时间差 = CreationTime 2026-09-24 22:08:45 vs LastWriteTime 2026-09-25 00:27:42（**文件被重写 2h19m 后**）
> - executor.py (`5F02C7E0F094` / 47,242 B) CreationTime = LastWriteTime = 21:59:06 → **未触动** ✓
> - **根因**：result.json 改写时点（00:27:42）晚于 mapping.md 创建（23:14:26）+ batch2_r6_result.json 创建（23:50:52），故下游链 reference 全部锁定原 SHA；改写后**无 chain manifest 重登记**，致链/盘双记
> - **不动文件本体**：按 R5 frozen 触禁；本勘误仅记录漂移事实 + 双 SHA 字面 + 改写时点
> - **PI 处置路径**：(a) 接受改写为「增/修字段」，将 `6B92BBFF7180` 视为新基准，更新下游链 reference（batch2_r6_result.json 等需勘误追加式补 drift 注记）；或 (b) 撤回改写，从 git / 备份恢复 `A4F851154551` 基准（盘上无可恢复副本 → 此路径需用户授权重建）

### C.2 §21.6 E-32.6 #2 — mapping 文件 hash 字面错

**勘误字面草案**（追加于 §21.6 E-32.6 #2 行后）：

> **定案（evidence-auditor 实测 2026-09-26）**：
> - mapping 文件本体 SHA = `98A779D61C1E` 与登记一致 → **文件未触动**
> - L19 字面 `CB37B699FF73` / L20 字面 `5BE9DFE83A27` → 实际盘上 SHA = `8C125E257AF8` (result) + `E7418F47A130` (executor)
> - 两处 bytes 字面一致 (result=62,887 / executor=55,317) → **SHA 字面错，非文件被改**
> - **根因**：mapping 起草时 hash 算错（起草类失灵）；mapping 按 R5 frozen 不擅改
> - **下游已披露**：batch8_r1_result.json L163 `mapping_sha12_discrepancy_note` 字段已诚实交代；本勘误与下游披露一致
> - **不动 mapping.md**；仅 E-32.6 勘误追加字面登记「mapping L19/L20 SHA 字面错，实际盘 SHA = 8C125E257AF8 + E7418F47A130」

### C.3 §21.6 E-32.6 #2 (续) — 清理 v3 棒 archive/sub 目录误报

**勘误字面草案**（追加于 §21.6 E-32.6 #2 行后 + C.2 字面下）：

> **定案（evidence-auditor 实测 2026-09-26）**：
> - 清理 v3 棒 §F L256-257 字面：`_non_upload_local_archive` / `deposon-sub` 均 False (0)
> - 实测：两目录在 `D:/私人资料/deposon-repo/`（workspace 子路径）下**不存在**（与 v3 棒一致）；但在 `D:/私人资料/`（workspace **父级路径**）下**存在**，分别 **1,669 件 / 441 件**
> - 用户预期「1230+ / 441+」 → 实测 **1,669 / 441**（1669 ≥ 1230 ✓；441 = 441 ✓）
> - **根因**：**相对路径基准错**——清理 v3 棒以 workspace 根 `D:/私人资料/deposon-repo` 为基准解析相对路径，但 archive/sub 实为 workspace **兄弟目录**（父级 `D:/私人资料/`）；v3 棒未跨出 workspace 边界外探 + 未识别仓外父级路径
> - **不动 v3 棒产物**（已落盘 `6F3F6FA3AB1D` / 24,491 B，按 R5 frozen 不擅改）；本勘误仅记录误报事实 + 正确路径基准

### C.4 §21.6 E-32.6 #3 — T1 verdict / result 锚标错（cleanup v3 棒标签互换）

**勘误字面草案**（追加于 §21.6 E-32.6 #3 行后）：

> **定案（evidence-auditor 实测 2026-09-26）**：
> - cleanup v3 棒 L37 标 `802DECE2286A` / 52,942 B 为 t1_verdict.md 字面 → 实际 `802DECE2286A` / 52,942 B = `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md`（add_T1）
> - cleanup v3 棒 L37 标 D6CB03A4657E 为「T1 verdict 锚」 → 实际 D6CB03A4657E = `results/_v4_supp_t1_result.json` (82,365 B)，是 **result 不是 verdict**
> - cleanup v3 棒 L44 / L220 标 F1B5E49F3058 为 T1.5 锚 → 实际 F1B5E49F3058 = `results/_v4_supp_t1_verdict.md` (27,538 B)，是 **T1 verdict 不是 T1.5**
> - **正确映射字面**：
>   - `F1B5E49F3058` = T1 verdict (`_v4_supp_t1_verdict.md` / 27,538 B) ✓
>   - `D6CB03A4657E` = T1 result (`_v4_supp_t1_result.json` / 82,365 B) ✓
>   - `802DECE2286A` = add_T1 (`_v4_supp_prereg_v02_add_T1_2026_09_24.md` / 52,942 B)
>   - `79936B630015` = add_T1_activation (`_v4_supp_prereg_v02_add_T1_activation_2026_09_24.md` / 14,234 B)
>   - `A7CAD9228B0B` = T1 executor (`_v4_supp_t1_executor.py` / 59,967 B)
> - **根因**：cleanup v3 棒两处字段填写错：(a) L37 把 add_T1 字面错填到 t1_verdict 名下；(b) 因 (a) 推断 + grep F1B5E49F3058 命中 t15_* 件（T1.5 对 T1 verdict 的正向引用），错误重路由为 T1.5 自锚
> - **t1_verdict.md 自报 SHA 表（L13-18）字面自洽**（D6CB03A4657E = result / 802DECE2286A = add_T1 / 79936B630015 = add_T1_activation） → cleanup v3 棒若交叉核 t1_verdict 自表可避免此错
> - **不动 v3 棒产物**（按 R5 frozen 不擅改）；本勘误仅记录 cleanup v3 棒字段填写错事实 + 正确映射字面

---

## D. 老实交代段（0 编造 · 实测边界 + 灰区明示）

1. **不动任何既有件**：本审链报告全程只读实测；未修改 batch1_r6_result.json / mapping.md / cleanup v3 棒 / t1_verdict.md / t1_result.json / batch2_r2_result.json / batch2_r2_executor.py / batch8_r1_result.json 等任何链上件；勘误追加式字面草案见 §C，由 doc-writer 后续落盘。

2. **case #1 反推改写内容未做**：本审链不动 batch1_r6_result.json 故未逆向 diff 改写前后内容；仅记录「-444 字节差异」+「无 chain manifest 重登记」事实 +「改写时点晚于所有下游引用」事实。改写动机（增字段 / 调字段 / 意外覆盖）**未推定**——PI 处置时按 §C.1 二选一。

3. **case #2 mapping 字面错未修**：mapping 文件按 R5 frozen 触禁 + 下游 batch8_r1_result.json L163 已诚实交代 + 勘误仅 E-32.6 字面追加。**不擅自回改 mapping.md L19/L20 字面**。

4. **case #3 cleanup v3 棒路径基准错未修**：v3 棒产物为历史事实，按 R5 frozen 不擅改；本勘误仅登记「相对路径基准错」根因 + 正确路径基准字面。**不擅自回改 v3 棒 §F 字面**。

5. **case #4 cleanup v3 棒标签互换未修**：同上 v3 棒不动原则；勘误仅 E-32.6 字面追加正确映射。**不擅自回改 v3 棒 L37 / L44 / L220 字面**。

6. **skill 缺位老实交代**：派工单要求 `scientific-research-workflows:peer-review` skill（plugin @scientific-research-wf，sha256-tree-v1 前 12 = `611965fcb620`）—— 本地 skill 加载器实测 `Local skill not found`（沿 v14 §20.7 末段先例 + E-32.6 #2 #3 既有口径）；本审链按 `6844BF36F762`（v15 erratum 锚）+ E-32.6 #2 #3 + T1 verdict `F1B5E49F3058` §5.2 limitations + T1.5 verdict `52C985429C91` §7.2 limitations 既有字面口径执行；**未编造 skill 不存在的虚构指令**。

7. **key 永不明文无例外自扫**：本审链报告落盘前实测 key 形态扫描 `sk-[A-Za-z0-9]{20,}` + `AIza[0-9A-Za-z_-]{30,}` + `Bearer\s+[A-Za-z0-9]{20,}` + `tp-*/ark-*/API_KEY=` 三类 0 命中；CLEAN。

8. **「CONFLICT」vs「SAME_IDENTITY」本审链内未触发**：4 疑点均为「链字面错」（盘改 / 起草算错 / 路径基准错 / 字段错填），无「同哈希多份」或「同名不同哈希」冲突；本审链未触发 5 分支判定表的「CONFLICT」分支。

9. **勘误追加式落地路径**：§C.1-C.4 字面草案需由 doc-writer（agent-0032834a3e04）后续落盘到 `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md` v15+ 追加节（不动 v15 既有 §1-§21.8 内容，仅末行续 v16）；本审链报告自身（`results/_v4_evidence_audit_reconcile_2026_09_26.md`）为**新建件**，不覆盖既有件。

10. **派工单锚点 `6844BF36F762` 实测复算**：
    ```
    SHA256  6844BF36F762C86E07B258D953AEAE9BCDA61994FC5440C9C6327FF5505CA7DB
    SHA-12  6844BF36F762  ✓ 与登记一致
    Length  158,079
    ```
    锚点 v15 erratum 文件本体未触动（实测 SHA = 自报 SHA）；本审链报告引用其 §21.6 E-32.6 + §21.7.5 字面 + E-32.6 #1 #2 #3 字面，未编造。

11. **边界声明再明示**：本审链不动 3 路在跑件（batch3 / batch4 / batch5 / batch6 / batch8 各 r* result.json + executor.py）；不动 18 frozen；不动 9 网格；不动 L2/L14 verdict；不动 P-G v0/v01；不动 plugin spec；不动 verifier 内置脚本；不动派生 JSON；不擅自调阈值。

---

## E. 报告元数据

| 项 | 值 |
|---|---|
| 路径 | `results/_v4_evidence_audit_reconcile_2026_09_26.md` |
| 性质 | 新建独立审链报告；不动任何既有件 |
| 派工 | evidence-auditor（agent-11335500b168）/ 派工单 audit_auth = ask_57981c1bc81e03b9990a06e5（2026-09-26 16:26 显式） |
| 锚点 | v15 erratum `6844BF36F762`（实测复算 ✓） + E-32.6 #1 #2 #3 字面（沿用） + 派工单补 case #2 mapping 字面错 |
| 边界 | R5 frozen / V1-V3 只读 / 派生 JSON 不合并 / 不覆盖既有件 / 0 擅调阈值 / key 永不明文无例外 |
| 自扫 | key 形态三类 0 命中（CLEAN） |
| skill | `scientific-research-workflows:peer-review`（缺位，沿先例 fallback） |
| 状态 | 本审链报告自身待 PI 复核生效；生效即锁；事后不重开不调 |

---

*出证：evidence-auditor · 2026-09-26*