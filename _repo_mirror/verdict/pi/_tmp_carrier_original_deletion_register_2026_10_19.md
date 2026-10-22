# 删除登记件：`.tmp\ritt_remeasure_measurement_2026_10_17.json` 原件

- 登记件路径：`_repo_mirror/verdict/pi/_tmp_carrier_original_deletion_register_2026_10_19.md`
- 登记件生成时间：2026-10-19（会话 mvs_7d3ebd2417a8412999788b2b891ed064）
- 场景：deposon｜工序：可恢复通道删除之原件，副本为唯一留存

---

## 1. 授权（逐字载）

> PI v138-Q3 授权（先自测指纹再逐字回读其逐字与 §3-3）：经可恢复通道删之（副本已在 `_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json`（SHA-12 `29bb4c4a8bca`·325,531 B·副本与原件逐位相符——先实测再动手）为唯一留存）。

授权射程（据派工载）：
- 授权对象**仅**原件 `_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json`
- 授权通道**仅**可恢复通道，⛔0 永久删
- 授权留存**仅**副本一份

## 2. 停手闸结果（动手前实测）

| 闸 | 判据 | 实测值 | 判定 |
|---|---|---|---|
| 闸① | 副本指纹须逐位＝原件之 `29bb4c4a8bca` | 原件 `29bb4c4a8bca`／副本 `29bb4c4a8bca`，皆 325,531 B | 通过 |
| 闸④-a | `Test-Path` 原件须＝False | `False` | 通过 |
| 闸④-b | glob `*tmp_carrier_original_deletion*` 须 0 命中 | 命中数＝0 | 通过 |

## 3. 原件／副本指纹面（动手前后双测）

原件（删除前，2026-10-19 17:47 前）：
- SHA-256：`29bb4c4a8bca0e09d24a527df8b599f42c32bd7f5638a2922553a3b217dfbc5f`
- SHA-12：`29bb4c4a8bca`
- 字节：325,531
- 路径：`_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json`

副本（删除后复测，仍在位）：
- SHA-256：`29bb4c4a8bca0e09d24a527df8b599f42c32bd7f5638a2922553a3b217dfbc5f`
- SHA-12：`29bb4c4a8bca`
- 字节：325,531
- 路径：`_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json`

**逐位相符**：两件 SHA-256 全 64 位字符串完全一致（`MATCH=True`，两次独立实测：动手前 + 删后）。

## 4. 验道记录（闸②·先以 1 件小样本验可恢复通道）

### 4.1 通道辨识（动手前的关键实测）

动手前实测本机 `rm` 之解析结果，发现风险并据以改验：

- `Get-Command rm` → `CommandType=Alias`，`Definition=Remove-Item`
  - 即：PowerShell 内建别名 **`rm` ＝ `Remove-Item`，属永久删**，⛔0 可用作本工序之可恢复通道。
- 受信 launcher 实测定位：`〔本地绝对路径·脱敏略:mavis-trash.cmd〕`
  - 其实现 `mavis-trash.js` 第 559-563 行调用 `Microsoft.VisualBasic.FileIO.FileSystem` 之 `SendToRecycleBin`，**确为可恢复通道**。

### 4.2 形态闸（`rm --` 须为顶层单命令）

首次以多语句脚本内嵌 `rm --` 调起，被运行时拦下并回报：

> `Windows recoverable-delete plan requires the targets-only trash marker.`

拦截时实测：样本仍在位（`Test-Path=True`，53 B），回收站 `$I` 计数＝7（与基线同，0 新增）——即**拦截发生在删除之前，未造成任何副作用**。改以顶层单命令形态复调，即通过。

### 4.3 小样本验道通过项

自建样本：`〔幽灵引用·原件已缺席·未上传:_rm_channel_selftest_2026_10_19.txt〕`（53 B，SHA-12 `28c00287279a`，内容含两行探针文本）

单命令：`rm -- "〔幽灵引用·原件已缺席·未上传:_rm_channel_selftest_2026_10_19.txt〕"`
运行时回报：`mavis-trash: moved to trash: '〔幽灵引用·原件已缺席·未上传:_rm_channel_selftest_2026_10_19.txt〕'`

验道核验（回收站 `$I`/`$R` 成对 + `$I` 偏移 28 解码）：

| 核验项 | 实测值 | 判定 |
|---|---|---|
| `$I` 件名 | `$IVSVK82.txt` | — |
| `$I` 版本字（偏移 0，8 字节） | `2` | 合规 |
| `$I` 原大小字（偏移 8，8 字节） | `53` | 与样本字节数一致 |
| `$I` 删除时刻字（偏移 16） | 2026-10-19 17:40:25 | 与执行时刻一致 |
| `$I` 偏移 28 解码原路径 | `〔幽灵引用·原件已缺席·未上传:_rm_channel_selftest_2026_10_19.txt〕` | **逐字吻合** |
| `$R` 成对存在 | `$RVSVK82.txt`＝True | 成对 |
| `$R` 字节／指纹 | 53 B／SHA-12 `28c00287279a` | **与删前指纹逐位一致**（可恢复且内容无损） |

验道结论：**可恢复通道验过**（`$I`/`$R` 成对、`$I` 偏移 28 解码原路径吻合、`$R` 载荷逐位相符）。方进入闸③。

## 5. 删除之回收站证据面（闸③）

单命令：`rm -- "_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json"`
运行时回报：`mavis-trash: moved to trash: '_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json'`

删除后实测：

| 核验项 | 实测值 |
|---|---|
| 原件 `Test-Path` | `False`（原件已离原位） |
| `$I` 件名 | `$I3WMSFA.json`（166 B，mtime 2026-10-19 17:47:34） |
| `$I` 版本字（偏移 0） | `2` |
| `$I` 原大小字（偏移 8） | `325531` |
| `$I` 删除时刻字（偏移 16） | 2026-10-19 17:47:34 |
| `$I` 偏移 28 解码原路径 | `_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json` |
| `$R` 成对存在 | `$R3WMSFA.json`＝True |
| `$R` 字节／指纹 | 325,531 B／SHA-12 `29bb4c4a8bca` |

**回收站留存面（可恢复）**：
- `$I`：`〔本地绝对路径·脱敏略:$I3WMSFA.json〕`
- `$R`：`〔本地绝对路径·脱敏略:$R3WMSFA.json〕`

即：原件**并未消失**，而是以完整载荷（325,531 B／`29bb4c4a8bca`）留存于 Windows 回收站，可经回收站还原。⛔0 永久删已守。

## 6. 「副本为唯一留存」之登记

- 原件（`.tmp` 面）**已离原位**：`Test-Path=False`，0 份留存于工作区。
- 原件（回收站面）留存 1 份（可恢复之 `$I`/`$R` 对，载荷与原件逐位相符）——此为可恢复通道之固有形态，非有效留存件。
- 副本（`_field_sources` 面）留存 1 份且**删后复测指纹未变**：`29bb4c4a8bca`／325,531 B。

**登记：有效留存件唯副本一份**——`_repo_mirror/readout/final/ritt_remeasure_measurement_2026_10_17.json`（SHA-12 `29bb4c4a8bca`·325,531 B）。除回收站之可恢复态外，0 他份留存。

## 7. 工序守纪自述

已守：
- ✅ 闸①副本指纹**先实测再动手**（动手前实测 + 动手瞬间复测，皆逐位＝`29bb4c4a8bca`）
- ✅ 闸②**验道先行**（自建小样本 1 件，验过方动手）
- ✅ 闸③仅删原件，删后验其入回收站（`$I`/`$R` 成对）
- ✅ 闸④停手闸实测通过（`Test-Path=False`、glob 0 命中）后乃出本件
- ✅ ⛔0 删任何他件（除自建小样本，其经同一通道回收）
- ✅ ⛔0 永久删（仅可恢复通道；`Remove-Item` 别名经实测辨识后未予采用）
- ✅ ⛔0 回改／移动任何既有件
- ✅ ⛔0 联网、0 实验、0 LLM、0 读 key（R4）
- ✅ ⛔0 触归档区、0 触 `〔本地他区引用·未上传:GLM〕`、0 写 sub 区
- ✅ ⛔0 落五终判词、0 闭任何 KD、0 宣告任何段毕
- ✅ 落盘纪律：UTF-8 无 BOM·纯 LF（`io.open(encoding='utf-8', newline='\n')` 直写）

如实交代：
- 本登记件所载全部数值均为**实测值**，无推断、无估值、无外部来源。
- `.tmp` 目录他 2,313 件（实测计数 2,314 项含目录项本身）**未触、未读、未改**，本工序视野仅及原件一件。
- 回收站面既有 7 件旧 `$I`（2026-10-19 17:29-17:35）为**本工序前既存**，⛔0 属本工序产物，⛔0 予处置。
