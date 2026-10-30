# 门① `F3` 面 · T-5 预报 json 复制回仓内 · 登记件

- **件名**：`results\verdict\judgement\_gate1_f3_json_pullback_2026_10_28.md`（新立）
- **立件时点**：2026-10-28 · 本棒（worker）· 承 PI 之裁而执行
- **PI 之裁**（2026-10-28 11:5x · 卡 `ask_2409c46678d4b216200dcc03`）逐字：「**须先复制回仓内**」（问：那份 json 在归档区，能以它为证据面吗）
- **本件之限**：⛔0 判 `F3` 面已消；⛔0 落五终判；⛔0 宣告任何零。判在 `verdict-keeper`／PI。
- ⚠ **本件是「复制之登记件」，与「被复制之 json」是两件事**——本件记复制之实与自证；被复制之 json 落于 `results\readout\reading\_s4_substrate_grid_availability_2026_10_08.json`（见 §3）。

---

## §0 源件实测（复制前 · 本棒自测，非采信派工单之值）

| 项 | 实测读数 |
|:--|:--|
| 源绝对路径 | `〔归档件引用·未上传:results____s4_substrate_grid_availability_2026_10_08.json〕` |
| 按名实列 | `Get-ChildItem -LiteralPath '…\_movedout_2026_10_22\readout\reading' -File \| Where-Object { $_.Name -like '*substrate_grid*' }` ⇒ **恰 1 件**：`results____s4_substrate_grid_availability_2026_10_08.json`（11,446 B／`2026-10-08 16:59:10`）——段名之多个下划线**以实列取之**，未凭派工单之路字符串盲取 |
| bytes | **11,446** |
| SHA-12 | **`66be80ab4b81`** |
| SHA-256（全） | `66be80ab4b819a1dcbdaff4a4146cd337937e034b4a57604499cc612a34986bf` |
| 字节五项 | `BOM 0`／`CR 0`／`VT 0`／`FFFD 0`／`LAST_BYTE 0x7d`／`NON_ASCII 0`／`LF 381` |
| mtime（复制前） | `2026-10-08T08:59:10.465Z`（本地 `2026-10-08 16:59:10.465`） |
| 与在册值之合 | 在册值 11,446／`66be80ab4b81`（口径件 `F3` 行）——**bytes 与 SHA-12 逐位合** ✅ |

> 测量器：`python -P '〔幽灵引用·未上传:_bcheck.py〕' '<绝对路径>'`。
> ⚠ 该器系为 `.md` 而设，对 json 之「末字节 `0x0a`」判不适用：源件末字节实为 `0x7d`（`}`），**本棒照实报读数、⛔0 为凑五项而改其内容**。
> ⛔0 读其内容：仅作字节级指纹核（读字节、统计 BOM／CR／VT／FFFD／末字节），未读其内容面。

---

## §1 落点之据（为何落此目录）

**落点 ＝ `〔幽灵引用·未上传:_s4_substrate_grid_availability_2026_10_08.json〕`（原位）**——⛔0 自选目录。

| # | 在册出处（件·行·指纹） | 内容 | 本棒核法 |
|:-:|:--|:--|:--|
| 1 | **口径件** `results\verdict\judgement\_gate1_readC_caliber_2026_10_28.md`（**自测 77,758／`17bf1d7654bf`**）· **L186 · `F3` 行** | 「`V4-04`（序 3）｜T-5 预报件 **md** `_s4_substrate_grid_availability_2026_10_08.md`（**主仓 `results\readout\reading\`**）**14,995／`7deaee06c41a`** ✅｜T-5 预报件 **json** `_s4_substrate_grid_availability_2026_10_08.json` —— **仓外归档区** …**11,446／`66be80ab4b81`**」；同行并引销号件 §2-4 ⑥ `R-2`（L290） | 开卷读该行；口径件自身指纹**自测**（77,758／`17bf1d7654bf`，与派工单所载逐位合 ✅） |
| 2 | **销号件** `results\evidence\register\_gate1_ten_items_writeoff_register_2026_10_24.md` · **L290 · `R-2`**（逐字） | 「**json 之归档可及性** —— `_s4_substrate_grid_availability_2026_10_08.json` 已移入仓外归档区；本棒 **0 复算其指纹**、⛔ 0 读其内容 ⇒ 若以其为证据面，**其可及性须 PI 一言**」 | 开卷读该行（**行号 L290 复核命中**）⇒ 采认面归 PI，本棒只执行复制 |
| 3 | **归档区段 ⇄ 仓内段之镜像**（本棒实测对照） | 归档区 `…\_movedout_2026_10_22\readout\reading\` 之段 ⇄ 仓内 `results\readout\reading\` 之段；归档文件名之 `results___` 前缀 ＝ 仓内顶层目录 `results` ＋ 分隔，故**原基名 ＝ `_s4_substrate_grid_availability_2026_10_08.json`**（`results___` ＋ `_s4_substrate…` ＝ 盘上实名 `results____s4_substrate…`，逐字合） | 列出归档 `readout\reading\` 与仓内 `results\readout\reading\` 两目录全量文件名逐一比对 |
| 4 | **同胞对照**（本棒实测） | 仓内 `results\readout\reading\_s4_substrate_grid_availability_2026_10_08.md`（**自测 14,995／`7deaee06c41a`**，与口径件 `F3` 行所载一致 ✅）**正在该目录**；其 mtime `2026-10-08T09:00:03Z` 与源 json 之 `2026-10-08T08:59:10Z` **相隔 53 秒** ⇒ 二者同批生成，json 原与 md 同居 `results\readout\reading\` | 自测 md 指纹 ＋ mtime 比对 |
| 5 | **旁证**（前棒自测脚本） | `.tmp\_g1_readc_selfmeasure.py:37` 之**主仓候选** ＝ `results\readout\reading\_s4_substrate_grid_availability_2026_10_08.json`；`.tmp\_g1_readc_pass2.txt:22` 之 `MISS` 行同载「主仓候选／归档区候选」二径 | 读该二件（只读） |

⇒ **落点取原位**：`results\readout\reading\`。落点文件名 ＝ 原基名 `_s4_substrate_grid_availability_2026_10_08.json`（**非**归档区带 `results____` 前缀之改名名——归档区前缀系移出时为避免同名而加，复制回仓内须还原原名）。

---

## §2 复制前之 `Test-Path`（落点无同名件）

| 测项 | 命令 | 实测 |
|:--|:--|:--|
| 落点件 | `Test-Path -LiteralPath '〔幽灵引用·未上传:_s4_substrate_grid_availability_2026_10_08.json〕'` | **False** ✅（AC-4） |
| 落点目录 | `Test-Path -LiteralPath '〔本地路径已脱敏〕'` | True（目录在位） |
| 仓内同名扫描 | `Get-ChildItem -LiteralPath '〔本地路径已脱敏〕' -Recurse -Force -File -Filter '*s4_substrate_grid_availability_2026_10_08*'` | **仅 1 件**：`〔幽灵引用·未上传:_s4_substrate_grid_availability_2026_10_08.md〕`（14,995）——**仓内 0 件 `.json`** ⇒ 无同名覆盖之虞 |
| 本登记件 | `Test-Path -LiteralPath '…\results\verdict\judgement\_gate1_f3_json_pullback_2026_10_28.md'` | **False**（新立） |

⇒ 落点可写、⛔0 覆盖任何既有件。

---

*（下接 §3 复制之实与 §4 自证；本件之分段落盘依派工单「两次落盘，任一成即有物」之序。）*

---

## §3 复制之实（AC-1 复制之实 ／ AC-2 源件未变之证）

**复制命令之原文（AC-5③）**

```powershell
$ErrorActionPreference='Stop'; Copy-Item -LiteralPath '〔归档件引用·未上传:results____s4_substrate_grid_availability_2026_10_08.json〕' -Destination '〔幽灵引用·未上传:_s4_substrate_grid_availability_2026_10_08.json〕' -ErrorAction Stop
```

> 仅 `Copy-Item`（读源、写副本）；**未加 `-Force`**（结构上即禁覆盖，且落前 `Test-Path`＝False）；⛔0 `Move-Item`／⛔0 `Rename-Item`／⛔0 `Remove-Item`／⛔0 对归档区之任何写。
> 首试之命令以变量承载 `$src`／`$dst`，被本机安全策略拦下（`recursive write/delete target cannot be verified inside the workspace`），**该次未产生任何复制**（复核：落点 `Test-Path` 仍为 False）；改用全字面路径重试即成——即上列一行。

### AC-1 复制之实

| 项 | 值 |
|:--|:--|
| 源绝对路径 | `〔归档件引用·未上传:results____s4_substrate_grid_availability_2026_10_08.json〕` |
| 副本绝对路径 | `〔幽灵引用·未上传:_s4_substrate_grid_availability_2026_10_08.json〕` |
| 源 bytes | 11,446 |
| 副本 bytes | 11,446 |
| 源 SHA-12 | `66be80ab4b81` |
| 副本 SHA-12 | `66be80ab4b81` |
| 源 SHA-256（全） | `66be80ab4b819a1dcbdaff4a4146cd337937e034b4a57604499cc612a34986bf` |
| 副本 SHA-256（全） | `66be80ab4b819a1dcbdaff4a4146cd337937e034b4a57604499cc612a34986bf` |
| **MATCH 判** | **✅ MATCH**（bytes 相同 ＋ SHA-256 全同 ＋ SHA-12 逐位同）⇒ **不须停手、不须删副本** |

### AC-2 源件未变之证（复制**前**／**后**各测一次，三者皆不变）

| 读数 | 复制前（§0） | 复制后 | 变否 |
|:--|:--|:--|:--|
| bytes | 11,446 | 11,446 | **不变** |
| SHA-12 | `66be80ab4b81` | `66be80ab4b81` | **不变** |
| mtime（UTC） | `2026-10-08T08:59:10.465Z` | `2026-10-08T08:59:10.465Z` | **不变** |
| mtime（本地） | `2026-10-08 16:59:10.465` | `2026-10-08 16:59:10.465` | **不变** |

**归档区零写入之证**（复制后实测该目录全量）：**仍为 7 件**（与复制前同数、同名、同大小、同 mtime）；源件**仍在归档区原位**，`LEN=11446`、`mtime=2026-10-08T08:59:10.465Z` ⇒ **归档区零写入、零删除**，源件**未**被移动。

> 副本之 mtime 亦为 `2026-10-08T08:59:10.465Z`（与源同）——`Copy-Item` 默认保留源之时间戳，故副本之 mtime **非**本次复制之时点；此为**读数如实**，非异常。

---

## §4 自证

### ① 副本之字节五项（`_bcheck.py` 实测）

| 项 | 读数 |
|:--|:--|
| BOM | **0**（无 BOM） |
| CR | **0**（纯 LF） |
| VT | **0** |
| FFFD | **0** |
| 末字节 | **`0x7d`**（＝ `}`） |
| NON_ASCII | 0 |
| LF 计数 | 381 |

⚠ **体例说明**：`_bcheck.py` 系为 `.md` 而设，其「末字节须为 `0x0a`」之判**不适用于本 json**——本件为 JSON 之体例，末字节为 `}`（`0x7d`）、无尾随换行；**本棒照实报其读数，⛔0 为凑五项而改其内容**。上列六项，源与副本**逐项相同**。

### ② 除本副本外触动既有件数 ＝ **0**

| 件 | 动 | 说明 |
|:--|:--|:--|
| `results\readout\reading\_s4_substrate_grid_availability_2026_10_08.json` | **新增**（本副本） | 唯一写入既有目录者 |
| `results\verdict\judgement\_gate1_f3_json_pullback_2026_10_28.md` | **新增**（本登记件，新立） | 非既有件（落前 `Test-Path`＝False） |
| 归档区全部 7 件 | **0 动** | 复制后实测：件数／名／大小／mtime 皆同 |
| 其余既有件 | **0 动** | 全程仅：只读枚举＋字节级读取＋1 次 `Copy-Item`＋本登记件之落盘写入＋1 个 `.tmp` 工作体（`_gate1_f3_pullback_part2.md`，新立） |

**全仓 60 分钟窗口扫描（佐证，非归因之唯一凭据）**：`Get-ChildItem -LiteralPath '〔本地路径已脱敏〕' -Recurse -Force -File | Where-Object { $_.LastWriteTime -gt (Get-Date).AddMinutes(-60) }` ⇒ 窗口内被改之既有件多属**并发之他棒**（`_f04_*`／`_g3_*`／`_v536–v540_body_*`／`_gate2_testgate_run_*`／`_gate3_111_filing_confirm_*`／`_gate1_f5_trace_audit_*` 等），**非本棒所触**；本棒于窗口内所增者仅二：本登记件（`12:07:18`／6,276 B）与本副本。
⚠ 本副本**不落在**该窗口之内——因 `Copy-Item` 保留源之时间戳（`2026-10-08T08:59:10.465Z`）；此本身即「忠实复制」之旁证。

### ③ 复制命令之原文

见 §3 首段（`Copy-Item` 一行，逐字）。

---

## §5 本件之限（照录，免误读）

1. 本棒**只执行复制并核指纹**：⛔0 判 `F3` 面已消、⛔0 落五终判、⛔0 宣告任何零——`F3`（项 `V4-04`）之消解与否，判在 `verdict-keeper`／PI。
2. **源件仍在归档区**（本次为**复制**非移动）：⛔0 移动、⛔0 重命名、⛔0 删除、⛔0 改源之内容；归档区**零写入**。
3. 副本之**内容面未读**：⛔0 读该 json 之内容（除为核指纹所需之字节读取）——其内容之判读不属本单。
4. 落点文件名**还原为原基名** `_s4_substrate_grid_availability_2026_10_08.json`；归档区名 `results____s4_substrate_grid_availability_2026_10_08.json` 之 `results____` 前缀系移出时为避同名所加，**未**将该前缀复制入仓。
5. 本件之登记路径在 `results\verdict\judgement\`，**与被复制之 json（`results\readout\reading\`）是两件事**。
6. PI 之裁「须先复制回仓内」之**前置**已由本棒执行；「以其为证据面」之**采认**仍属 PI／`verdict-keeper`，本棒**不代裁**。

---

**我落盘了：`〔幽灵引用·未上传:_gate1_f3_json_pullback_2026_10_28.md〕`**｜`Test-Path` ＝ **True**（实测）｜`Get-Item` 实测读数（**本末行写入前**、即 §0–§2 落成后之状态）：`LEN=6276`／`SHA-12=63b7dfafca9f`／`mtime=2026-10-28T04:07:18.563Z`（本地 `2026-10-28 12:07:18.563`）——因本件为 append-only，末行写入后其 bytes／SHA-12／mtime 必再变，**最终读数由本棒直陈于回报**。
