# V5 回收站补算复核件 — 2026-09-25 T1 噪声清理 47 件删除件 SHA-12（2026-09-29）

> by worker（执行类 / 只读盘点 / 回收站元数据解析 + 逐件指纹）
> 执行面来源：PI 确认批 12 §4 **㊷**（「回收站补算 ＝ 另起复核棒」· 47 件删除件 SHA-12）
> 上游册：`results/_v5_confirm_b12_decisions_register_2026_09_29.md`（§4 ㊷ / §1.4）
> 源件：`results/_v4_noise_cleanup_manifest_v3_2026_09_25.md`（SHA-12 `6f3f6fa3ab1d` / 24,491 B / 47 件 §B 表 SHA-12 全部留空）
> 口径：SHA-12 ＝ `hashlib.sha256(字节).hexdigest()[:12]`（**小写**、盘上实测）
> **本件 0 覆盖既有件、0 恢复件、0 永久删除、0 清空回收站**

---

## A. 结论摘要（先读这一节）

| 项 | 实测结果 |
|---|---|
| **目标** | 对 2026-09-25 T1 噪声清理经 `mavis-trash` 删除的 **47 件**逐件补算 SHA-12 |
| **回收站可达性** | ✅ **两处回收站全部可达、0 权限拒绝**（D 盘 + C 盘，同一 SID） |
| **本棒全量清点** | **571 件**（D 87 + C 484，递归含 `$R` 目录嵌套）｜**207 条** `$I` 元数据全部解析成功 |
| **47 件匹配结果** | ⭐ **0 / 47 命中**（按原路径 + 文件名双路匹配，见 §C） |
| **根因（事实观察）** | ⭐ **回收站现存最早删除时间为 `2026-09-28 16:12:28`（CST）**，即 2026-09-25 清理窗口（00:51–01:02）的**全部条目已不在回收站内** ⇒ 47 件**当前不可及**，**0 编造补算** |
| **替代回填面（实测发现）** | ⭐ 源件 §B.1 字面「如需 SHA 须另起复核棒**从回收站恢复或从 v2 manifest 反查**」的**第二路径成立**：`results/_v4_noise_cleanup_manifest_v2_2026_09_24.md` §D.1 **载有 11 件历史 SHA-12**（见 §D） |
| **本棒实际产出** | 207 条 `$I` 逐条元数据 + 201 件 `$R` **实测 SHA-12** + 5 个 `$R` 目录的**逐文件清单**（附录 A/B）⇒ **回收站现状面完整留痕**（**0 编造**） |
| **0 混同** | 本件 §A 的「47 件删除件」≠ `rendered_arxiv` 冻结 47 件 ≠ archive key 形态候选 47 件 ⇒ **三者互不混同，数字巧合不构成证据** |

---

## B. 匹配方法节（可复算）

### B.1 盘点范围（穷尽 · 0 抽样）

| 回收站根 | 递归文件数 | 顶层条目 | `$I` 元数据 | `$R` 内容件 | `$R` 目录件 | 其它 |
|---|---|---|---|---|---|---|
| `D:\$Recycle.Bin\S-1-5-21-1515631758-409240343-2904948024-500\` | **87** | 27 | 13 | 9 | 4 | 1（`desktop.ini`） |
| `C:\$Recycle.Bin\S-1-5-21-1515631758-409240343-2904948024-500\` | **484** | 388 | 194 | 192 | 1 | 1（`desktop.ini`） |
| **合计** | **571** | **415** | **207** | **201** | **5** | **2** |

- **递归口径**：`os.walk` 全深度遍历（覆盖 `$R` 目录嵌套，如 `$R2AWLTS` 形如目录的删除件）⇒ 递归文件数 **571**（与派工单 root 先前实测的「D 约 87 / C 约 484」**逐位一致**）
- **0 漏项证明**：415 顶层条目 ＝ 207 `$I` + 201 `$R` 文件 + 5 `$R` 目录 + 2 `desktop.ini` ⇒ **每一条目均已归类，0 未解释残项**
- **配对核验**：207 条 `$I` 中 **206 条** `$R` 实体在盘；**1 条** `$R` 缺失（`$I52NDVM`，`\Users\Administrator\Downloads\修复施工总册…`，2026-09-28 16:12:28）⇒ 事实登记（**附录 A 第 1 行 ＋ §E 边界 13**）
- **盘符穷尽**：`Get-CimInstance Win32_LogicalDisk` 实测本机仅 **C: / D: 两个固定盘** ⇒ **无第三处回收站遗漏面**
- **SID 穷尽**：两处 `$Recycle.Bin` 下**各仅 1 个 SID 目录**，且与 `whoami /user` 当前身份 SID **完全一致** ⇒ **0 他人 SID 面遗漏**

### B.2 `$I` 元数据解析（格式 · 实测）

Windows 回收站 `$I*` 文件布局（实测 version ＝ **2**，207/207 一致）：

| 偏移 | 长度 | 含义 |
|---|---|---|
| 0 | 8 B | 版本号（实测全为 `2`） |
| 8 | 8 B | 原文件大小（小端 uint64） |
| 16 | 8 B | 删除时间（FILETIME，1601-01-01 起 100 ns 刻度） |
| 24 | 4 B | 原路径长度 |
| 28 | 4 B | 路径长度（v2） |
| 32 | 余 | 原路径（**UTF-16LE**） |

- 解析实现：`<Q` 解 0/8/16 偏移；v2 取 32 起 UTF-16LE 解码，**遇 `\x00` 截断**
- **207 / 207 解析成功、0 解析失败、0 短文件**
- FILETIME → CST 换算：`1970-01-01 + (ft/1e7 − 11644473600) + 8h`（本机时区实测 ＝ 中国标准时间 UTC+8）

### B.3 匹配判据（双路 · 逐件）

对 47 件**逐件**执行两路匹配，任一路命中即记为命中：

1. **原路径匹配**：`$I` 解析原路径 basename ＝ 源件 §B 表登记 basename（**47/47 逐一比对**）
2. **件族模糊匹配**：`$R` 实体文件名 regex ＝ `_t1_batch_|_t15_batch_|_t1_records|_t1_probe_log|_grep_out|l14v3_batch2_r\d`（**两盘全深度 571 件全扫**）

⭐ **模糊匹配面同时覆盖「文件名被回收站改写」的可能**（回收站会把原名替换为 `$R<6位随机><扩展名>`，故 basename 匹配本身已天然覆盖改名情形；模糊面为冗余保险）。

---

## C. 对账节（实测 vs 47）

### C.1 逐件对账结果

| 源件分区 | 件数 | 源件 SHA-12 | **本棒实测命中** | 状态 |
|---|---|---|---|---|
| §B.1 `.tmp/_t1_*`（29 batch + records + probe_log） | 31 | 留空 | **0** | ⭐ **不在当前回收站内** |
| §B.2 `.tmp/_t15_batch_*.jsonl` | 7 | 留空 | **0** | ⭐ **不在当前回收站内** |
| §B.3 `results/_v4_supp_l14v3_batch2_r*_console*.log` | 8 | 留空 | **0** | ⭐ **不在当前回收站内** |
| §B.4 `.tmp/_grep_out.txt` | 1 | 留空 | **0** | ⭐ **不在当前回收站内** |
| **合计** | **47** | **0 件有值** | **0 / 47** | — |

### C.2 ⭐ 根因（事实观察 · 0 推定）

**本棒实测到的决定性事实**：

| 观测项 | 实测值 |
|---|---|
| 回收站 `$I` **最早**删除时间 | **2026-09-28 16:12:28**（CST） |
| 回收站 `$I` **最晚**删除时间 | 2026-09-29 15:25:09（CST） |
| 按日分布 | **2026-09-28：1 件**｜**2026-09-29：206 件** |
| **2026-09-24 / 09-25（47 件清理窗口）条目** | **0 件** |
| 现有 `$I` 中原路径含 `deposon-repo` 者 | 13 件（**全部为 2026-09-29 删除**，`_tail3_scratch` / `_tmp_*` / `mindmap_corpus_v20_r1.py` 等，**0 件属 47 件家族**） |

⇒ **两处回收站在 2026-09-25 之后已被清空并重新累积**（现存 207 件的最早条目已是 2026-09-28）⇒ **2026-09-25 清理的 47 件当前不在回收站内**。

⚠️ **0 推定清空主体**：本棒**0 判定**清空动作的发起者、时点或授权状态 —— 仓内 grep `EmptyRecycleBin|清空回收站|清空回收|回收站清空` **仅命中批 12 册 §4 ㊷ 自身的「0 直呼回收站清空」纪律行**，**0 命中任何实际清空回执**。⇒ **只登记「47 件当前不可及」这一事实，不编造差异说明**。

### C.3 47 件逐条不可及登记

47 件**逐条**登记（0 合并、0 省略）：

| # | 源件登记路径 | 源件 bytes | 源件 SHA-12 | 本棒回收站命中 | 不可及面归因 |
|---|---|---|---|---|---|
| 1 | `.tmp/_t1_batch_0_0_20260924_205614.jsonl` | 298 | 留空 | 0 | 当前回收站无此条目（**0 命中 basename / 0 命中件族**） |
| 2 | `.tmp/_t1_batch_1_1_20260924_210448.jsonl` | 1320 | 留空 | 0 | 同上 |
| 3 | `.tmp/_t1_batch_2_2_20260924_210842.jsonl` | 3713 | 留空 | 0 | 同上 |
| 4 | `.tmp/_t1_batch_3_3_20260924_211107.jsonl` | 1196 | 留空 | 0 | 同上 |
| 5 | `.tmp/_t1_batch_3_3_20260924_211959.jsonl` | 1028 | 留空 | 0 | 同上 |
| 6 | `.tmp/_t1_batch_3_3_20260924_212028.jsonl` | 1015 | 留空 | 0 | 同上 |
| 7 | `.tmp/_t1_batch_3_3_20260924_212129.jsonl` | 1001 | 留空 | 0 | 同上 |
| 8 | `.tmp/_t1_batch_4_4_20260924_212417.jsonl` | 3714 | 留空 | 0 | 同上 |
| 9 | `.tmp/_t1_batch_5_5_20260924_214058.jsonl` | 841 | 留空 | 0 | 同上 |
| 10 | `.tmp/_t1_batch_5_5_20260924_214433.jsonl` | 1024 | 留空 | 0 | 同上 |
| 11 | `.tmp/_t1_batch_5_5_20260924_215206.jsonl` | 640 | 留空 | 0 | 同上 |
| 12 | `.tmp/_t1_batch_6_6_20260924_215432.jsonl` | 3904 | 留空 | 0 | 同上 |
| 13 | `.tmp/_t1_batch_7_7_20260924_215555.jsonl` | 1076 | 留空 | 0 | 同上 |
| 14 | `.tmp/_t1_batch_7_7_20260924_215634.jsonl` | 1068 | 留空 | 0 | 同上 |
| 15 | `.tmp/_t1_batch_7_7_20260924_215750.jsonl` | 1070 | 留空 | 0 | 同上 |
| 16 | `.tmp/_t1_batch_7_7_20260924_215901.jsonl` | 1065 | 留空 | 0 | 同上 |
| 17 | `.tmp/_t1_batch_7_7_20260924_215941.jsonl` | 1049 | 留空 | 0 | 同上 |
| 18 | `.tmp/_t1_batch_8_8_20260924_220322.jsonl` | 3891 | 留空 | 0 | 同上 |
| 19 | `.tmp/_t1_batch_9_9_20260924_220745.jsonl` | 1066 | 留空 | 0 | 同上 |
| 20 | `.tmp/_t1_batch_9_9_20260924_220858.jsonl` | 1069 | 留空 | 0 | 同上 |
| 21 | `.tmp/_t1_batch_9_9_20260924_221240.jsonl` | 1077 | 留空 | 0 | 同上 |
| 22 | `.tmp/_t1_batch_9_9_20260924_221347.jsonl` | 1065 | 留空 | 0 | 同上 |
| 23 | `.tmp/_t1_batch_9_9_20260924_221717.jsonl` | 1053 | 留空 | 0 | 同上 |
| 24 | `.tmp/_t1_batch_10_10_20260924_220629.jsonl` | 3893 | 留空 | 0 | 同上 |
| 25 | `.tmp/_t1_batch_11_11_20260924_221835.jsonl` | 1066 | 留空 | 0 | 同上 |
| 26 | `.tmp/_t1_batch_11_11_20260924_222001.jsonl` | 1070 | 留空 | 0 | 同上 |
| 27 | `.tmp/_t1_batch_11_11_20260924_222334.jsonl` | 1071 | 留空 | 0 | 同上 |
| 28 | `.tmp/_t1_batch_11_11_20260924_222514.jsonl` | 1066 | 留空 | 0 | 同上 |
| 29 | `.tmp/_t1_batch_11_11_20260924_222838.jsonl` | 1053 | 留空 | 0 | 同上 |
| 30 | `.tmp/_t1_records.json` | 180445 | 留空 | 0 | 同上 |
| 31 | `.tmp/_t1_probe_log.json` | 1079 | 留空 | 0 | 同上 |
| 32 | `.tmp/_t15_batch_0_0_20260925_000924.jsonl` | 2948 | 留空 | 0 | 同上 |
| 33 | `.tmp/_t15_batch_0_0_20260925_001255.jsonl` | 1211 | 留空 | 0 | 同上 |
| 34 | `.tmp/_t15_batch_1_1_20260925_000356.jsonl` | 526 | 留空 | 0 | 同上 |
| 35 | `.tmp/_t15_batch_2_2_20260925_001932.jsonl` | 3779 | 留空 | 0 | 同上 |
| 36 | `.tmp/_t15_batch_3_3_20260925_002639.jsonl` | 3956 | 留空 | 0 | 同上 |
| 37 | `.tmp/_t15_batch_4_4_20260925_003327.jsonl` | 3948 | 留空 | 0 | 同上 |
| 38 | `.tmp/_t15_batch_5_5_20260925_004137.jsonl` | 3951 | 留空 | 0 | 同上 |
| 39 | `results/_v4_supp_l14v3_batch2_r1_console.log` | 未取 | 留空 | 0 | 同上 |
| 40 | `results/_v4_supp_l14v3_batch2_r1_console.err.log` | 未取 | 留空 | 0 | 同上 |
| 41 | `results/_v4_supp_l14v3_batch2_r2_console.log` | 未取 | 留空 | 0 | 同上 |
| 42 | `results/_v4_supp_l14v3_batch2_r2_console.err.log` | 未取 | 留空 | 0 | 同上 |
| 43 | `results/_v4_supp_l14v3_batch2_r3_console.log` | 未取 | 留空 | 0 | 同上 |
| 44 | `results/_v4_supp_l14v3_batch2_r4_console.log` | 未取 | 留空 | 0 | 同上 |
| 45 | `results/_v4_supp_l14v3_batch2_r5_console.log` | 未取 | 留空 | 0 | 同上 |
| 46 | `results/_v4_supp_l14v3_batch2_r6_console.log` | 未取 | 留空 | 0 | 同上 |
| 47 | `.tmp/_grep_out.txt` | 1664 | 留空 | 0 | 同上 |

> ⚠️ 「不可及面归因」栏统一记为**观测事实**（回收站无对应条目），**0 推定**其消失原因（可能已被后续清理 / 已被清出回收站 / 其它），**0 编造差异说明**。

### C.4 既有删除回执面（只读参考 · 0 推定归属）

| 回执件 | 记件数 | 通道 | 本棒关系 |
|---|---|---|---|
| `_archive_cleanup_extension_2026_09_28.md` | **163** | `rm -- <相对路径…>`（9 次顶层调用） | **0 推定** 47 件属该批（该批原件面 ＝ `deposon-sub` archive，**非 `.tmp` / `results` 清理面**） |
| `_archive_cleanup_non_upload_2026_09_28.md` | **66** | 同上（6 次顶层调用） | **0 推定** 47 件属该批（同上） |

⚠️ **两批合计 229 件 ＝ 2026-09-28 清理**；但**回收站现存最早条目亦为 2026-09-28 16:12:28**，二者**时间窗部分重叠** ⇒ 本棒**只登记该重叠事实，0 判定**二者是否同源、**0 推定** 47 件属哪一批。

### C.5 `mavis-trash` 通道核实（只读 · 0 执行）

为确认「47 件当时确曾进入回收站」这一前提，本棒**只读**核对了删除通道实现（**0 执行任何删除**）：

- `C:\Users\Administrator\.minimax\bin\mavis-trash.cmd` → `mavis-trash.js`
- `mavis-trash.js` 内 `trashFile()` 调用 PowerShell `SendToRecycleBin`（Microsoft.VisualBasic.FileIO.FileSystem）⇒ **确为 Windows 原生回收站通道**，**非自建影子目录**
- 临时载荷 `mavis-trash-reparse-<pid>-<ts>-<rand>.json` 落 `os.tmpdir()` 并在 `finally` 中 `unlinkSync` 清理 ⇒ **0 影子副本面**（本棒实测 `%TEMP%` 无残留 `mavis-trash-reparse*`）
- 实测 `C:\Users\Administrator\.minimax\trash` / `.trash` / `D:\.trash` 等候选影子根 **0 存在**

⇒ **源件 v3 §A「所有删除件可从 Windows Recycle Bin 恢复」在删除时点成立**；**当前不可及系时点差异（回收站此后被清空重积），非通道错误**。

---

## D. ⭐ 替代回填面（v2 manifest 历史 SHA-12 · 11 件）

源件 v3 §E.5 字面：「如需 SHA-12 须另起复核棒**从回收站恢复或从 v2 manifest 反查**」⇒ **回收站路径本棒实测 0 命中（§C），第二路径 v2 manifest 实测成立**。

`results/_v4_noise_cleanup_manifest_v2_2026_09_24.md`（SHA-12 `90253e8342da`，与 v3 §D.5 登记锚一致）§D.1 载 **11 件** `.tmp/_t1_*` 历史 SHA-12：

| v2 §D.1 编号 | 文件 | v2 bytes | **v2 SHA-12** | v2 状态 | 与 v3 §B.1 交叉核 |
|---|---|---|---|---|---|
| t1-01 | `.tmp/_t1_batch_0_0_20260924_205614.jsonl` | 298 | `ea56e031e281` | 健在 | ＝ v3 #1（bytes 298 **同值**） |
| t1-02 | `.tmp/_t1_batch_1_1_20260924_210448.jsonl` | 1320 | `bebad997825c` | 健在 | ＝ v3 #2（bytes 1320 **同值**） |
| t1-03 | `.tmp/_t1_batch_2_2_20260924_210842.jsonl` | 3713 | `98d43d33a69e` | 健在 | ＝ v3 #3（bytes 3713 **同值**） |
| t1-04 | `.tmp/_t1_batch_3_3_20260924_211107.jsonl` | 1196 | `1183452b155a` | 健在 | ＝ v3 #4（bytes 1196 **同值**） |
| t1-05 | `.tmp/_t1_batch_3_3_20260924_211959.jsonl` | 1028 | `699ad8382989` | 健在 | ＝ v3 #5（bytes 1028 **同值**） |
| t1-06 | `.tmp/_t1_batch_3_3_20260924_212028.jsonl` | 1015 | `3ca109852b20` | 健在 | ＝ v3 #6（bytes 1015 **同值**） |
| t1-07 | `.tmp/_t1_batch_3_3_20260924_212129.jsonl` | 1001 | `45fdc5e47eed` | 健在 | ＝ v3 #7（bytes 1001 **同值**） |
| t1-08 | `.tmp/_t1_batch_4_4_20260924_212417.jsonl` | 3714 | `90b1c5fd901f` | 健在 | ＝ v3 #8（bytes 3714 **同值**） |
| t1-09 | `.tmp/_t1_batch_5_5_20260924_214058.jsonl` | 841 | `0b437ae8bccd` | 新增 | ＝ v3 #9（bytes 841 **同值**） |
| t1-10 | `.tmp/_t1_probe_log.json` | 1079 | `41ab30dba57f` | 健在 | ＝ v3 #31（bytes 1079 **同值**） |
| t1-11 | `.tmp/_t1_records.json` | **83680** | `5a3c77e96ee4` | 健在（T1 在跑实时增长） | ⚠️ ＝ v3 #30，但 **bytes 不同**（v3 记 **180445**）⇒ 见下方警告 |

⚠️ **⚠️ 诚实边界 · `t1-11` 不可用作删除件指纹**：v2 §D.1 实测时点该件为 **83,680 B**（v2 字面「派单时 79873 bytes，实测 83680 bytes，**T1 在跑实时增长**」），v3 删除时点为 **180,445 B** ⇒ **两者非同一字节内容**，`5a3c77e96ee4` **不可**作为 180,445 B 版的 SHA-12。**本棒 0 将其登记为 47 件之补算值**，仅作 v2 面历史记录留痕。

⚠️ **⚠️ 诚实边界 · 剩余 36 件 0 回填面**：47 件中 **11 件**有 v2 历史 SHA-12（其中 1 件因字节漂移不成立 ⇒ **净可用 10 件**），**36 件 0 任何来源的 SHA-12**（v2 manifest 仅覆盖 T1 区 11 件；`_t15_batch_*` 7 件 / `batch2 console` 8 件 / `_grep_out.txt` 1 件 / `_t1_batch_*` 余 18 件 全无历史 SHA 记录）⇒ **0 编造补齐**。

---

## E. 诚实边界节

| # | 边界 | 内容 |
|---|---|---|
| **1** | ⭐ **任务面 0 完成（指 47 件补算）** | 47 件 SHA-12 **补算 0 / 47 完成** —— **实体已不在回收站内**（§C.2 实测）⇒ **0 编造、0 由 v3 登记值反推、0 由 v2 值冒充删除件指纹**（除 §D 已明示的 10 件历史值） |
| **2** | ⭐ **0 混同三处「47」** | `rendered_arxiv` 冻结 47 件 ≠ archive key 形态候选 47 件 ≠ **本件 47 件删除件** ⇒ 三者互不混同，**数字巧合不构成证据** |
| **3** | ⭐ **0 推定 47 件归属** | 163 件批 / 66 件批**均 0 推定**；时间窗重叠仅作**事实登记**，0 判定同源 |
| **4** | ⭐ **0 判定回收站清空主体** | 仓内 **0 命中**任何实际清空回执 ⇒ **只登记「47 件当前不可及」，不编造清空主体 / 时点 / 授权** |
| **5** | ⭐ **只读铁边界（0 违反）** | **0 恢复件、0 永久删除、0 清空回收站、0 移动、0 改 ACL**；全程仅 `os.listdir` / `os.scandir` / `os.walk` / `os.stat` / `open(...,'rb')` ⇒ **回收站内容 0 变更** |
| **6** | ⭐ **key 永不明文** | 回收站内含 `.py` / `.json` / `.pyc` 等潜在配置/脚本件 ⇒ 本棒**仅算 SHA-12 + 解析 `$I` 元数据（路径/大小/时间）**，**0 打印任何文件内容、0 读 key 值、0 做形态扫描**（脚本输出仅：$R 名 / SHA-12 / 字节 / 原路径 / 删除时间） |
| **7** | **0 复制件入工作区** | 哈希**就地计算**（`open($R,'rb')` 流式）；中间件与清册落 **`%TEMP%`**，**0 复制任何回收站实体到 `deposon-repo`** ⇒ 工作区 0 沾染删除件 |
| **8** | **0 覆盖既有件** | 本件为**新建件**；源件 v3 `6f3f6fa3ab1d` / v2 `90253e8342da` / 批 12 册 / 两份 09-28 回执 **全部只读、0 写 0 改**（本棒落盘前实测两份 manifest SHA-12 复测同值） |
| **9** | **本件 0 派生 JSON** | 0 产出任何 JSON 派生件（中间 JSON 落 `%TEMP%`，**不落仓**）⇒ 沿「派生 JSON 不合并 / 不新增」纪律 |
| **10** | **0 冻结触动** | 18 frozen 与 9 网格 **0 读改**；本棒全部产出 ＝ 本新名件 1 件 |
| **11** | **0 新设阈值** | **0 个**（匹配判据 ＝ 字面 basename + 件族 regex，无阈值） |
| **12** | ⚠️ **附录 B 的目录件面** | 5 个 `$R` 目录件（`_tail3_scratch` ×3 / `_tmp_v3df` / `$RLZBOVM`）**0 属 47 件**；其逐文件 SHA-12 仅为**回收站现状留痕**，**0 宣称与 T1 清理的关系** |
| **13** | ⚠️ **`$R52NDVM` 元数据孤儿** | 207 条 `$I` 中 1 条 `$R` 实体缺失（2026-09-28 16:12:28，Downloads 面）⇒ **事实登记，0 判定原因** |
| **14** | **时间口径** | `$I` FILETIME → CST（本机 UTC+8，实测 `time.tzname` ＝ 中国标准时间）；**删除时间 ≠ 文件 mtime**，二者不可混用 |
| **15** | **本棒 0 引外部名** | **0 新增**外部专有名词 / 文献号 / 定理名 |
| **16** | **skill** | **0 加载任何 skill**（派工单未指定 skill 名）⇒ 纪律锚 ＝ 派工单字面 ＋ FTFB 内核 ＋ 既有件惯例 |

---

## F. 铁边界核验

| 铁律 | 遵守情况 |
|---|---|
| **0 恢复、0 永久删除、0 直呼回收站清空** | ✅ 全程只读（`listdir` / `scandir` / `walk` / `stat` / `open('rb')`）；**0 次写入回收站、0 次删除、0 次 ACL 变更** |
| **0 绕过恢复机制** | ✅ 未调用任何恢复/清空 API（**0 调 `SendToRecycleBin` 之外的删除面**；`mavis-trash.js` **仅只读查阅、0 执行**） |
| **key 永不明文** | ✅ **0 打印任何回收站文件内容、0 读 key 值**；输出仅 `$R` 名 / SHA-12 / 字节 / 元数据 |
| **0 触动既有件 / 0 覆盖** | ✅ 既有件全部只读；本棒仅新增本件 1 件（新名，落盘前 glob 查重 **0 同名**） |
| **0 派工文件数矛盾外扩** | ✅ 47 件对账 0 推定；163/66 两回执 0 推定归属 |
| **PI 确认批 12 §4 ㊷** | ✅ 另起复核棒、只读回收站、逐件补算 —— **执行面已落地，结论为「0/47 命中 + 根因实测登记」** |

---

## G. 待拍板项（0 代裁）

| # | 项 | 说明 |
|---|---|---|
| **1** | ⭐ **47 件 SHA-12 面是否结案为「不可及」** | 回收站路径已实测 0 命中且**通道核实在删除时点成立**（§C.5）⇒ **0 自行释义**：「结案为不可及」vs「另寻其它回填面（如 result.json 复刻面 / executor 日志面）」**请 PI 裁** |
| **2** | ⭐ **v2 manifest 11 件历史 SHA-12 的采信口径** | §D 已登记 10 件**净可用**（bytes 与 v3 同值）+ 1 件**字节漂移不成立** ⇒ **是否采信为 47 件之部分回填**，**0 代裁** |
| **3** | **回收站清空事件是否立项** | 仓内 0 命中清空回执，47 件去向**无台账** ⇒ **是否另起核查棒**，**请 PI 裁**（本棒 0 调查、0 推定） |
| **4** | **回收站现状面（207 条 + 201 SHA-12）是否留档** | 本件已完整留痕于附录 A/B ⇒ **是否需另立冻结登记**，**请 PI 裁** |

---

<div id="appendix"></div>

## 附录 A · 回收站全量 207 条 `$I` 元数据 + 201 件 `$R` SHA-12（实测）

> **口径**：`$I` 逐条解析（version 2 / UTF-16LE 原路径 / FILETIME → CST）；`$R` 文件件 SHA-12 ＝ `sha256(字节).hexdigest()[:12]` 小写实测；`$R` 目录件在附录 B 逐文件展开
> **排序**：按 `$I` 删除时间升序

| # | 盘 | $R 名 | 形态 | SHA-12 | 字节 | 删除时间 (CST) | $I 解析原路径 |
|---|---|---|---|---|---|---|---|
| 1 | C | `$R52NDVM` | **$R 缺失** | `—` | 378100 | 2026-09-28 16:12:28 | `\Users\Administrator\Downloads\修复施工总册-唯一版-附属文件夹（补丁终态12枚＋冒烟证据）` |
| 2 | D | `$R965RZA` | 目录（19 件 / 75443047 B） | `—` | 75443047 | 2026-09-29 11:16:43 | `\私人资料\deposon-repo\.tmp\_tail3_scratch` |
| 3 | D | `$R2AWLTS` | 目录（19 件 / 69960477 B） | `—` | 69960477 | 2026-09-29 11:17:59 | `\私人资料\deposon-repo\.tmp\_tail3_scratch` |
| 4 | D | `$RCVN2DZ` | 目录（19 件 / 74865042 B） | `—` | 74865042 | 2026-09-29 11:19:29 | `\私人资料\deposon-repo\.tmp\_tail3_scratch` |
| 5 | D | `$RR6ZZ50.py` | 文件 | `cab5cec06c0d` | 417 | 2026-09-29 11:20:43 | `\私人资料\deposon-repo\_tmp_fix_tail.py` |
| 6 | D | `$R6HAJGU.txt` | 文件 | `7e67b73325b8` | 2592 | 2026-09-29 11:20:51 | `\私人资料\deposon-repo\_tmp_run_out.txt` |
| 7 | D | `$R4K4HJJ.tsv` | 文件 | `4c69d56c74ba` | 6516 | 2026-09-29 11:43:40 | `\私人资料\deposon-repo\.h2h5_list.tsv` |
| 8 | C | `$RXWJ74S.py` | 文件 | `d752c24f2185` | 771 | 2026-09-29 11:44:01 | `\Users\Administrator\AppData\Local\Temp\big.py` |
| 9 | C | `$RMU8PES.txt` | 文件 | `8b322b459b07` | 13126 | 2026-09-29 11:44:09 | `\Users\Administrator\AppData\Local\Temp\BIG.txt` |
| 10 | C | `$R4Q46ZH.py` | 文件 | `05ec1e7358d7` | 477 | 2026-09-29 11:44:15 | `\Users\Administrator\AppData\Local\Temp\cat.py` |
| 11 | C | `$RVDV55O.py` | 文件 | `c3a3aa83890a` | 441 | 2026-09-29 11:44:24 | `\Users\Administrator\AppData\Local\Temp\cat2.py` |
| 12 | C | `$RC8ZI63.py` | 文件 | `858ef0afb13b` | 1437 | 2026-09-29 11:44:31 | `\Users\Administrator\AppData\Local\Temp\cat3.py` |
| 13 | C | `$RX8OC80.py` | 文件 | `0cd001813d38` | 1834 | 2026-09-29 11:44:40 | `\Users\Administrator\AppData\Local\Temp\cat4.py` |
| 14 | C | `$RFBRDCC.txt` | 文件 | `e974d78f6981` | 13256 | 2026-09-29 11:44:48 | `\Users\Administrator\AppData\Local\Temp\sec_h2_05b975a86989.txt` |
| 15 | C | `$RCRCHPV.py` | 文件 | `1162cfa8cf5a` | 370 | 2026-09-29 11:44:53 | `\Users\Administrator\AppData\Local\Temp\ctx.py` |
| 16 | C | `$RTHYYPC.txt` | 文件 | `af14eb352efd` | 8918 | 2026-09-29 11:45:02 | `\Users\Administrator\AppData\Local\Temp\sec_h4_0a2b5c837c83.txt` |
| 17 | C | `$RZPOQC1.txt` | 文件 | `ee8910adabc4` | 3450 | 2026-09-29 11:45:02 | `\Users\Administrator\AppData\Local\Temp\sec_h2_272e8c752406.txt` |
| 18 | C | `$RAC2A64.txt` | 文件 | `710e15bad08e` | 840 | 2026-09-29 11:45:08 | `\Users\Administrator\AppData\Local\Temp\ctx.txt` |
| 19 | C | `$RT5F7UK.txt` | 文件 | `37707448ddaa` | 2203 | 2026-09-29 11:45:15 | `\Users\Administrator\AppData\Local\Temp\sec_h2_29a853444d42.txt` |
| 20 | C | `$R74T7HT.txt` | 文件 | `5bdc55d9fadf` | 6159 | 2026-09-29 11:45:17 | `\Users\Administrator\AppData\Local\Temp\sec_h4_2e08b9ae9f09.txt` |
| 21 | C | `$ROP90PN.py` | 文件 | `09f38a6c25bb` | 857 | 2026-09-29 11:45:22 | `\Users\Administrator\AppData\Local\Temp\ctx2.py` |
| 22 | C | `$RPQO1D2.txt` | 文件 | `71f0a2e77939` | 3401 | 2026-09-29 11:45:30 | `\Users\Administrator\AppData\Local\Temp\sec_h4_2e0f6b8bf141.txt` |
| 23 | C | `$RF4FKY4.txt` | 文件 | `b81882e4b70e` | 5262 | 2026-09-29 11:45:31 | `\Users\Administrator\AppData\Local\Temp\sec_h2_32cc61d394f2.txt` |
| 24 | C | `$R8279ZC.py` | 文件 | `d907b9c77675` | 1077 | 2026-09-29 11:45:36 | `\Users\Administrator\AppData\Local\Temp\ctx3.py` |
| 25 | C | `$RI5OXVY.txt` | 文件 | `bf4f44c44bef` | 243 | 2026-09-29 11:45:45 | `\Users\Administrator\AppData\Local\Temp\sec_h2_3e4e90fb48e1.txt` |
| 26 | C | `$RKESHF0.txt` | 文件 | `068c2468dbc9` | 20360 | 2026-09-29 11:45:46 | `\Users\Administrator\AppData\Local\Temp\sec_h4_41d29f4deb70.txt` |
| 27 | C | `$RCKIJ1G.py` | 文件 | `de0c74bdbaa4` | 1718 | 2026-09-29 11:45:50 | `\Users\Administrator\AppData\Local\Temp\dedup.py` |
| 28 | C | `$RI6TLUO.txt` | 文件 | `3c04de0a8a8a` | 7999 | 2026-09-29 11:45:57 | `\Users\Administrator\AppData\Local\Temp\sec_h2_4025e871726b.txt` |
| 29 | C | `$RYKKSQD.txt` | 文件 | `8fe6785e4bc4` | 6489 | 2026-09-29 11:45:58 | `\Users\Administrator\AppData\Local\Temp\sec_h4_426cfe18cf65.txt` |
| 30 | C | `$RN7C26J.txt` | 文件 | `b0e1eddb22e4` | 8861 | 2026-09-29 11:46:07 | `\Users\Administrator\AppData\Local\Temp\sec_h2_443efb39804a.txt` |
| 31 | C | `$RU6U2NS.txt` | 文件 | `fdd34b10e0c0` | 4407 | 2026-09-29 11:46:08 | `\Users\Administrator\AppData\Local\Temp\sec_h4_434b3213bdce.txt` |
| 32 | C | `$R7V40IO.txt` | 文件 | `1dfa0d1d864d` | 2515 | 2026-09-29 11:46:16 | `\Users\Administrator\AppData\Local\Temp\sec_h2_55cd332f66f2.txt` |
| 33 | C | `$RI2QGDQ.txt` | 文件 | `48a52bada964` | 7026 | 2026-09-29 11:46:18 | `\Users\Administrator\AppData\Local\Temp\sec_h4_6f045bdc70e7.txt` |
| 34 | C | `$RGCURQW.txt` | 文件 | `302207566e62` | 3632 | 2026-09-29 11:46:28 | `\Users\Administrator\AppData\Local\Temp\sec_h2_5bf4d9ad2877.txt` |
| 35 | C | `$R1152IR.txt` | 文件 | `742523670534` | 5405 | 2026-09-29 11:46:29 | `\Users\Administrator\AppData\Local\Temp\sec_h4_6f9b865280a3.txt` |
| 36 | C | `$RBWMCER.txt` | 文件 | `0e6a1459e9ea` | 34803 | 2026-09-29 11:46:38 | `\Users\Administrator\AppData\Local\Temp\sec_h2_64c4ef850025.txt` |
| 37 | C | `$RT0BWBZ.txt` | 文件 | `87469f0330ea` | 4854 | 2026-09-29 11:46:40 | `\Users\Administrator\AppData\Local\Temp\sec_h4_71e9cc179bec.txt` |
| 38 | C | `$RLI895D.txt` | 文件 | `12a24bc04bb4` | 6189 | 2026-09-29 11:46:48 | `\Users\Administrator\AppData\Local\Temp\sec_h2_79936b630015.txt` |
| 39 | C | `$RX6DU3H.txt` | 文件 | `221546a6927f` | 6616 | 2026-09-29 11:46:50 | `\Users\Administrator\AppData\Local\Temp\sec_h4_78f3aba1f24c.txt` |
| 40 | C | `$RNW44XB.txt` | 文件 | `b06bb906b97c` | 1635 | 2026-09-29 11:47:01 | `\Users\Administrator\AppData\Local\Temp\sec_h2_7b14cdb31d21.txt` |
| 41 | C | `$RF1S511.txt` | 文件 | `d021b9e35301` | 4406 | 2026-09-29 11:47:06 | `\Users\Administrator\AppData\Local\Temp\sec_h4_82a947f2aebd.txt` |
| 42 | C | `$R7B6UO8.txt` | 文件 | `8d1dc740fbfe` | 13776 | 2026-09-29 11:47:17 | `\Users\Administrator\AppData\Local\Temp\sec_h2_802dece2286a.txt` |
| 43 | C | `$RJA0OOD.txt` | 文件 | `afcc64a52c6e` | 57015 | 2026-09-29 11:47:19 | `\Users\Administrator\AppData\Local\Temp\H2_read.txt` |
| 44 | C | `$RNW7K81.txt` | 文件 | `2cccc2892b97` | 11833 | 2026-09-29 11:47:23 | `\Users\Administrator\AppData\Local\Temp\sec_h4_88052d7db895.txt` |
| 45 | C | `$RN15ZHJ.txt` | 文件 | `3f707f329f0f` | 5527 | 2026-09-29 11:47:32 | `\Users\Administrator\AppData\Local\Temp\sec_h2_843e42ef4d2a.txt` |
| 46 | C | `$RUOATHS.txt` | 文件 | `9cf16076b83c` | 134879 | 2026-09-29 11:47:32 | `\Users\Administrator\AppData\Local\Temp\H2_read2.txt` |
| 47 | C | `$RACWOMK.txt` | 文件 | `c1c519167ada` | 5969 | 2026-09-29 11:47:38 | `\Users\Administrator\AppData\Local\Temp\sec_h4_9d49a632ee81.txt` |
| 48 | C | `$RS9LKTZ.txt` | 文件 | `962424d7c40c` | 19961 | 2026-09-29 11:47:46 | `\Users\Administrator\AppData\Local\Temp\sec_h2_8898b964a9d9.txt` |
| 49 | C | `$RCRKVEC.py` | 文件 | `7fc6af89cf88` | 5455 | 2026-09-29 11:47:46 | `\Users\Administrator\AppData\Local\Temp\h2h5_final.py` |
| 50 | C | `$RS49W89.txt` | 文件 | `dccad6195289` | 3262 | 2026-09-29 11:47:52 | `\Users\Administrator\AppData\Local\Temp\sec_h4_a0734e0a6860.txt` |
| 51 | C | `$RFS4M6C.txt` | 文件 | `fd6f97249b44` | 9423 | 2026-09-29 11:48:01 | `\Users\Administrator\AppData\Local\Temp\sec_h2_8bbfe831e7c3.txt` |
| 52 | C | `$RIKQIWR.txt` | 文件 | `b74691bc156a` | 1810 | 2026-09-29 11:48:03 | `\Users\Administrator\AppData\Local\Temp\h2h5_final_out.txt` |
| 53 | C | `$RMUY08M.txt` | 文件 | `031c5dedbaba` | 7177 | 2026-09-29 11:48:06 | `\Users\Administrator\AppData\Local\Temp\sec_h4_b7547329af2e.txt` |
| 54 | C | `$RXD3E2K.txt` | 文件 | `98d4661c955d` | 6276 | 2026-09-29 11:48:15 | `\Users\Administrator\AppData\Local\Temp\sec_h2_8f5136e176b8.txt` |
| 55 | C | `$R5UMX1Q.py` | 文件 | `16e7a418685c` | 26146 | 2026-09-29 11:48:15 | `\Users\Administrator\AppData\Local\Temp\h2h5_fix1.py` |
| 56 | C | `$R0ZRCA1.txt` | 文件 | `b566d97c04f9` | 15591 | 2026-09-29 11:48:20 | `\Users\Administrator\AppData\Local\Temp\sec_h4_bb44fdc7ab0f.txt` |
| 57 | C | `$RHPUFLL.py` | 文件 | `2c2982e79096` | 1262 | 2026-09-29 11:48:29 | `\Users\Administrator\AppData\Local\Temp\h2h5_hash.py` |
| 58 | C | `$RA2QKB4.txt` | 文件 | `84413d14774d` | 2506 | 2026-09-29 11:48:30 | `\Users\Administrator\AppData\Local\Temp\sec_h2_90253e8342da.txt` |
| 59 | C | `$R2Q1XGX.txt` | 文件 | `51276980e5ed` | 13178 | 2026-09-29 11:48:36 | `\Users\Administrator\AppData\Local\Temp\sec_h4_bcc3cee23e82.txt` |
| 60 | C | `$R5TAGFP.py` | 文件 | `c6bb21f121ed` | 5434 | 2026-09-29 11:48:46 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass2.py` |
| 61 | C | `$ROKBY3N.txt` | 文件 | `d1b021c00487` | 16793 | 2026-09-29 11:48:46 | `\Users\Administrator\AppData\Local\Temp\sec_h2_98a779d61c1e.txt` |
| 62 | C | `$RDLUSE7.txt` | 文件 | `95d85f39369d` | 7913 | 2026-09-29 11:48:51 | `\Users\Administrator\AppData\Local\Temp\sec_h4_c300e74a082c.txt` |
| 63 | C | `$RFKXGGM.txt` | 文件 | `874e594fc612` | 8611 | 2026-09-29 11:48:59 | `\Users\Administrator\AppData\Local\Temp\sec_h2_9bd8932fa214.txt` |
| 64 | C | `$RHGYSQI.txt` | 文件 | `9f09d82fd754` | 5234 | 2026-09-29 11:49:00 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass2_out.txt` |
| 65 | C | `$RAAI835.txt` | 文件 | `473f044fabf0` | 11805 | 2026-09-29 11:49:04 | `\Users\Administrator\AppData\Local\Temp\sec_h4_ef5a40554960.txt` |
| 66 | C | `$RD6RAVD.py` | 文件 | `a273f82023fb` | 3067 | 2026-09-29 11:49:13 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass3.py` |
| 67 | C | `$RZP5GU9.txt` | 文件 | `415a8619d86c` | 3850 | 2026-09-29 11:49:14 | `\Users\Administrator\AppData\Local\Temp\sec_h2_c64146c4ccac.txt` |
| 68 | C | `$RVVQF55.txt` | 文件 | `616607dafc0b` | 6977 | 2026-09-29 11:49:18 | `\Users\Administrator\AppData\Local\Temp\sec_h4_fc0ffd27adca.txt` |
| 69 | C | `$RUN47RE.py` | 文件 | `d7983c298807` | 8327 | 2026-09-29 11:49:27 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass4.py` |
| 70 | C | `$RS4S5AP.txt` | 文件 | `4983bb64827f` | 5755 | 2026-09-29 11:49:29 | `\Users\Administrator\AppData\Local\Temp\sec_h2_eb9ad4193cf2.txt` |
| 71 | C | `$RNRT6UV.txt` | 文件 | `6f4220c2f364` | 2832 | 2026-09-29 11:49:31 | `\Users\Administrator\AppData\Local\Temp\sec_h5_04f6ecd482b9.txt` |
| 72 | C | `$RIDUMY9.py` | 文件 | `41b03518fffd` | 3614 | 2026-09-29 11:49:40 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass5.py` |
| 73 | C | `$RPSQ6CE.txt` | 文件 | `7a2dcd69f5d4` | 9347 | 2026-09-29 11:49:42 | `\Users\Administrator\AppData\Local\Temp\sec_h2_f1b5e49f3058.txt` |
| 74 | C | `$RGULDLI.txt` | 文件 | `2b758b56a2de` | 7138 | 2026-09-29 11:49:47 | `\Users\Administrator\AppData\Local\Temp\sec_h5_138faf395f40.txt` |
| 75 | C | `$RIN0R46.py` | 文件 | `09c517704154` | 1469 | 2026-09-29 11:49:56 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass6.py` |
| 76 | C | `$RMTAO6E.txt` | 文件 | `b83f78360b32` | 1398 | 2026-09-29 11:49:57 | `\Users\Administrator\AppData\Local\Temp\sec_h3_080f9caf313c.txt` |
| 77 | C | `$RRWK3Q4.txt` | 文件 | `475948834055` | 5113 | 2026-09-29 11:50:01 | `\Users\Administrator\AppData\Local\Temp\sec_h5_1cd36ac1b2c0.txt` |
| 78 | C | `$RU8979B.py` | 文件 | `06ad4492edb9` | 1396 | 2026-09-29 11:50:09 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass7.py` |
| 79 | C | `$RVIKYVW.txt` | 文件 | `9f4082e70c08` | 1495 | 2026-09-29 11:50:10 | `\Users\Administrator\AppData\Local\Temp\sec_h3_0d0edc68cd35.txt` |
| 80 | C | `$RJXXEQ8.txt` | 文件 | `b65756999913` | 2206 | 2026-09-29 11:50:14 | `\Users\Administrator\AppData\Local\Temp\sec_h5_20f15c49feb5.txt` |
| 81 | C | `$RAMLPDK.py` | 文件 | `ec828cdde7ba` | 3397 | 2026-09-29 11:50:22 | `\Users\Administrator\AppData\Local\Temp\h2h5_pass8.py` |
| 82 | C | `$RA0UX8Y.txt` | 文件 | `e9097a0ba284` | 8823 | 2026-09-29 11:50:24 | `\Users\Administrator\AppData\Local\Temp\sec_h3_24c64cc23907.txt` |
| 83 | C | `$RZT62V9.txt` | 文件 | `08f4bfca0dc8` | 4486 | 2026-09-29 11:50:28 | `\Users\Administrator\AppData\Local\Temp\sec_h5_2b9e886e729d.txt` |
| 84 | C | `$R8PJ8YU.py` | 文件 | `c52e941b47c4` | 1678 | 2026-09-29 11:50:34 | `\Users\Administrator\AppData\Local\Temp\h2h5_scan1.py` |
| 85 | C | `$RKOVTTC.txt` | 文件 | `cdc9ba485b3a` | 5069 | 2026-09-29 11:50:37 | `\Users\Administrator\AppData\Local\Temp\sec_h3_4c731a625868.txt` |
| 86 | C | `$RW7A6S6.txt` | 文件 | `70a26f57081b` | 4782 | 2026-09-29 11:50:38 | `\Users\Administrator\AppData\Local\Temp\sec_h5_331022480a57.txt` |
| 87 | C | `$R0T52ZN.txt` | 文件 | `b53c32e875f2` | 380195 | 2026-09-29 11:50:45 | `\Users\Administrator\AppData\Local\Temp\h2h5_scan1.txt` |
| 88 | C | `$R04DE19.txt` | 文件 | `ba5187f57d5e` | 22657 | 2026-09-29 11:50:48 | `\Users\Administrator\AppData\Local\Temp\sec_h3_52c985429c91.txt` |
| 89 | C | `$RLRHXRR.txt` | 文件 | `4e49912edfcb` | 3775 | 2026-09-29 11:50:49 | `\Users\Administrator\AppData\Local\Temp\sec_h5_58ed6be022ed.txt` |
| 90 | C | `$RALHZD8.py` | 文件 | `ab50857c490e` | 2612 | 2026-09-29 11:50:57 | `\Users\Administrator\AppData\Local\Temp\h2h5_sec.py` |
| 91 | C | `$R54COKM.txt` | 文件 | `844a17209718` | 7865 | 2026-09-29 11:51:00 | `\Users\Administrator\AppData\Local\Temp\sec_h3_5d79e67a4e9d.txt` |
| 92 | C | `$RTY73P6.txt` | 文件 | `782ae100e08a` | 5139 | 2026-09-29 11:51:00 | `\Users\Administrator\AppData\Local\Temp\sec_h5_6b86576146a3.txt` |
| 93 | C | `$RWT83D5.txt` | 文件 | `691b08175cd7` | 630203 | 2026-09-29 11:51:08 | `\Users\Administrator\AppData\Local\Temp\h2h5_sec.txt` |
| 94 | C | `$RYKYYJ2.txt` | 文件 | `c57654e20689` | 11475 | 2026-09-29 11:51:11 | `\Users\Administrator\AppData\Local\Temp\sec_h3_5fbec21e0ad2.txt` |
| 95 | C | `$R0DK3AL.txt` | 文件 | `475a0476fa15` | 1235 | 2026-09-29 11:51:12 | `\Users\Administrator\AppData\Local\Temp\sec_h5_6df402298557.txt` |
| 96 | C | `$REPPZWT.py` | 文件 | `6c2ec5bdf800` | 503 | 2026-09-29 11:51:19 | `\Users\Administrator\AppData\Local\Temp\h2h5_secsplit.py` |
| 97 | C | `$R65DHBL.txt` | 文件 | `3ebf4c780b06` | 5578 | 2026-09-29 11:51:21 | `\Users\Administrator\AppData\Local\Temp\sec_h3_68f66904c0c8.txt` |
| 98 | C | `$RUNCFL1.txt` | 文件 | `69e4b88dc136` | 11736 | 2026-09-29 11:51:23 | `\Users\Administrator\AppData\Local\Temp\sec_h5_7662d5058a7d.txt` |
| 99 | C | `$RH85B56.py` | 文件 | `9ef71e1b2a50` | 522 | 2026-09-29 11:51:30 | `\Users\Administrator\AppData\Local\Temp\h2h5_split.py` |
| 100 | C | `$RS9U3GN.txt` | 文件 | `15cc29c10f20` | 1432 | 2026-09-29 11:51:32 | `\Users\Administrator\AppData\Local\Temp\sec_h3_6ef770d61308.txt` |
| 101 | C | `$R7YD93Z.txt` | 文件 | `42c999df4a99` | 14751 | 2026-09-29 11:51:34 | `\Users\Administrator\AppData\Local\Temp\sec_h5_7e1323b09030.txt` |
| 102 | C | `$RH7FFKE.txt` | 文件 | `66d3e43dba17` | 7891 | 2026-09-29 11:51:42 | `\Users\Administrator\AppData\Local\Temp\h2h5_todelete.txt` |
| 103 | C | `$RON7NK5.txt` | 文件 | `d43093e57549` | 6862 | 2026-09-29 11:51:44 | `\Users\Administrator\AppData\Local\Temp\sec_h3_6f3f6fa3ab1d.txt` |
| 104 | C | `$RLC6REQ.txt` | 文件 | `d6cc7fdb833c` | 7754 | 2026-09-29 11:51:47 | `\Users\Administrator\AppData\Local\Temp\sec_h5_82e90ff496ae.txt` |
| 105 | C | `$RBGKY1F.py` | 文件 | `6a24ad011067` | 5901 | 2026-09-29 11:51:53 | `\Users\Administrator\AppData\Local\Temp\h2h5_verify.py` |
| 106 | C | `$RP62XQQ.txt` | 文件 | `277492bb7ba5` | 26271 | 2026-09-29 11:51:56 | `\Users\Administrator\AppData\Local\Temp\sec_h3_8355724a26e3.txt` |
| 107 | C | `$RQ4JAIX.txt` | 文件 | `80707c3727eb` | 13756 | 2026-09-29 11:51:58 | `\Users\Administrator\AppData\Local\Temp\sec_h5_a8da321b64d2.txt` |
| 108 | C | `$RD0V2F1.txt` | 文件 | `a0cdab8b3673` | 4111 | 2026-09-29 11:52:05 | `\Users\Administrator\AppData\Local\Temp\h2h5_verify_out.txt` |
| 109 | C | `$RZ226UV.txt` | 文件 | `ffa1c0b5a935` | 19551 | 2026-09-29 11:52:08 | `\Users\Administrator\AppData\Local\Temp\sec_h3_883dced872b4.txt` |
| 110 | C | `$RKBRAAH.txt` | 文件 | `b2992eb81168` | 2644 | 2026-09-29 11:52:11 | `\Users\Administrator\AppData\Local\Temp\sec_h5_aa02cbfc84e3.txt` |
| 111 | C | `$REJ6AER.py` | 文件 | `98b1dc6b1d0a` | 4221 | 2026-09-29 11:52:19 | `\Users\Administrator\AppData\Local\Temp\h2h5_verify2.py` |
| 112 | C | `$R0ZJYNL.txt` | 文件 | `1043215a9f6c` | 1850 | 2026-09-29 11:52:21 | `\Users\Administrator\AppData\Local\Temp\sec_h3_b4ac31f917f3.txt` |
| 113 | C | `$RLIMWY2.txt` | 文件 | `eca0c8c6e1a4` | 8600 | 2026-09-29 11:52:24 | `\Users\Administrator\AppData\Local\Temp\sec_h5_bc68854a6eba.txt` |
| 114 | C | `$RDD1D22.txt` | 文件 | `f11e6e3ade8b` | 13644 | 2026-09-29 11:52:34 | `\Users\Administrator\AppData\Local\Temp\h2h5_verify2_out.txt` |
| 115 | C | `$RKX5WUQ.txt` | 文件 | `1a002c5c0988` | 6352 | 2026-09-29 11:52:35 | `\Users\Administrator\AppData\Local\Temp\sec_h3_ba4d07bd7000.txt` |
| 116 | C | `$RG8NBHA.txt` | 文件 | `1db1d647b683` | 3826 | 2026-09-29 11:52:40 | `\Users\Administrator\AppData\Local\Temp\sec_h5_fbf88f8ac7a6.txt` |
| 117 | C | `$RTXYMB5.txt` | 文件 | `850f6af0b26d` | 71682 | 2026-09-29 11:52:48 | `\Users\Administrator\AppData\Local\Temp\H3a.txt` |
| 118 | C | `$RTDY1CV.txt` | 文件 | `5cc6e5ff4ad9` | 7744 | 2026-09-29 11:52:49 | `\Users\Administrator\AppData\Local\Temp\sec_h3_cc498bc28525.txt` |
| 119 | C | `$R02801L.txt` | 文件 | `1ab91efa58b6` | 104210 | 2026-09-29 11:52:59 | `\Users\Administrator\AppData\Local\Temp\H3b.txt` |
| 120 | C | `$RUSUSEF.txt` | 文件 | `d870ef5de4ff` | 2317 | 2026-09-29 11:53:00 | `\Users\Administrator\AppData\Local\Temp\sec_h3_d339d7286ad8.txt` |
| 121 | C | `$RBPRFS9.txt` | 文件 | `12f053065a49` | 14338 | 2026-09-29 11:53:10 | `\Users\Administrator\AppData\Local\Temp\H3gap.txt` |
| 122 | C | `$R7H5SP4.txt` | 文件 | `5fdb58d61d4c` | 22528 | 2026-09-29 11:53:12 | `\Users\Administrator\AppData\Local\Temp\sec_h3_f4435801d09f.txt` |
| 123 | C | `$RE0B0SM.txt` | 文件 | `6f387d693da7` | 155795 | 2026-09-29 11:53:22 | `\Users\Administrator\AppData\Local\Temp\H4a.txt` |
| 124 | C | `$RVAQ5SB.txt` | 文件 | `05749469fe37` | 3999 | 2026-09-29 11:53:23 | `\Users\Administrator\AppData\Local\Temp\sec_h3_f586a5a21584.txt` |
| 125 | C | `$RB22PG8.txt` | 文件 | `a97f3ab68f1f` | 61465 | 2026-09-29 11:53:33 | `\Users\Administrator\AppData\Local\Temp\H5a.txt` |
| 126 | C | `$RO3K2BP.txt` | 文件 | `2890aa8eac38` | 12609 | 2026-09-29 11:53:35 | `\Users\Administrator\AppData\Local\Temp\sec_h3_f6ed61c25572.txt` |
| 127 | C | `$RLAH4HA.txt` | 文件 | `423d509901c2` | 38322 | 2026-09-29 11:53:44 | `\Users\Administrator\AppData\Local\Temp\H5b.txt` |
| 128 | C | `$RDUKQ02.py` | 文件 | `390c84bb10f4` | 847 | 2026-09-29 11:53:54 | `\Users\Administrator\AppData\Local\Temp\kw.py` |
| 129 | C | `$R2RV6NA.txt` | 文件 | `f08aa1c86dc0` | 11472 | 2026-09-29 11:54:03 | `\Users\Administrator\AppData\Local\Temp\kw.txt` |
| 130 | C | `$R287PXE.py` | 文件 | `f37a43494aa9` | 554 | 2026-09-29 11:54:12 | `\Users\Administrator\AppData\Local\Temp\q.py` |
| 131 | C | `$RSEXGIV.txt` | 文件 | `0546d05cd5f9` | 4484 | 2026-09-29 11:54:21 | `\Users\Administrator\AppData\Local\Temp\q.txt` |
| 132 | C | `$RS9Z106.py` | 文件 | `41a3669aa13a` | 901 | 2026-09-29 11:54:29 | `\Users\Administrator\AppData\Local\Temp\rescan.py` |
| 133 | C | `$RPK4AWQ.py` | 文件 | `39e081f4d3c6` | 851 | 2026-09-29 11:54:40 | `\Users\Administrator\AppData\Local\Temp\sha2path.py` |
| 134 | C | `$RGMQLER.txt` | 文件 | `8154b1ab055f` | 647 | 2026-09-29 11:54:51 | `\Users\Administrator\AppData\Local\Temp\sha2path.txt` |
| 135 | C | `$R1VDMEN.lnk` | 文件 | `88e6918bc3ba` | 1947 | 2026-09-29 11:56:06 | `\Users\Public\Desktop\Git Bash.lnk` |
| 136 | D | `$REQ4HDX.tmp_v3df` | 目录（7 件 / 17288 B） | `—` | 17288 | 2026-09-29 12:10:46 | `\私人资料\deposon-repo\.tmp_v3df` |
| 137 | C | `$RSIJ1GK.txt` | 文件 | `7d466119e230` | 452059 | 2026-09-29 12:34:18 | `\Users\Administrator\AppData\Local\Temp\h6h7_all_0.txt` |
| 138 | C | `$RXCH4X5.py` | 文件 | `e508f5ad84e0` | 118791 | 2026-09-29 12:34:24 | `\Users\Administrator\AppData\Local\Temp\h6h7_build.py` |
| 139 | C | `$RJD6COD.py` | 文件 | `9dd2729d7848` | 2668 | 2026-09-29 12:34:30 | `\Users\Administrator\AppData\Local\Temp\h6h7_byprod.py` |
| 140 | C | `$RZ45VVY.txt` | 文件 | `80f7cd8bf46c` | 162150 | 2026-09-29 12:34:37 | `\Users\Administrator\AppData\Local\Temp\h6h7_byprod.txt` |
| 141 | C | `$RHG52GC.txt` | 文件 | `efa2e97ebebd` | 115695 | 2026-09-29 12:34:44 | `\Users\Administrator\AppData\Local\Temp\h6h7_chunk0.txt` |
| 142 | C | `$RCS3U8R.txt` | 文件 | `d0385a145723` | 155548 | 2026-09-29 12:34:50 | `\Users\Administrator\AppData\Local\Temp\h6h7_chunk1.txt` |
| 143 | C | `$R94FE2S.txt` | 文件 | `f4423ea89488` | 176996 | 2026-09-29 12:34:58 | `\Users\Administrator\AppData\Local\Temp\h6h7_chunk2.txt` |
| 144 | C | `$RB8PBKM.txt` | 文件 | `8e3a35b2424b` | 3814 | 2026-09-29 12:35:07 | `\Users\Administrator\AppData\Local\Temp\h6h7_chunk3.txt` |
| 145 | C | `$RYCDQNS.py` | 文件 | `c65200ba9957` | 855 | 2026-09-29 12:35:15 | `\Users\Administrator\AppData\Local\Temp\h6h7_combine.py` |
| 146 | C | `$RSV3JPM.txt` | 文件 | `f94ef1261762` | 284 | 2026-09-29 12:35:22 | `\Users\Administrator\AppData\Local\Temp\h6h7_err.txt` |
| 147 | C | `$RZ0PY7A.py` | 文件 | `4c2391648189` | 2439 | 2026-09-29 12:35:29 | `\Users\Administrator\AppData\Local\Temp\h6h7_extract.py` |
| 148 | C | `$RWWCI53.txt` | 文件 | `28f25d9dd602` | 49 | 2026-09-29 12:35:37 | `\Users\Administrator\AppData\Local\Temp\h6h7_fill_out.txt` |
| 149 | C | `$RH1687W.py` | 文件 | `38381cd31780` | 8115 | 2026-09-29 12:35:46 | `\Users\Administrator\AppData\Local\Temp\h6h7_fill14.py` |
| 150 | C | `$R4X1QS6.py` | 文件 | `ec366fbc670f` | 2094 | 2026-09-29 12:35:55 | `\Users\Administrator\AppData\Local\Temp\h6h7_fixq.py` |
| 151 | C | `$RDV0K3Q.py` | 文件 | `d6356c37ed2f` | 3525 | 2026-09-29 12:36:06 | `\Users\Administrator\AppData\Local\Temp\h6h7_inventory.py` |
| 152 | C | `$R9SF0UZ.py` | 文件 | `b63b0e2f4161` | 3528 | 2026-09-29 12:36:32 | `\Users\Administrator\AppData\Local\Temp\h6h7_lines.py` |
| 153 | C | `$RA8VIN1.txt` | 文件 | `8a1f85da83c3` | 375857 | 2026-09-29 12:36:39 | `\Users\Administrator\AppData\Local\Temp\h6h7_lines.txt` |
| 154 | C | `$R90V28M.py` | 文件 | `2998597e39b6` | 1125 | 2026-09-29 12:36:46 | `\Users\Administrator\AppData\Local\Temp\h6h7_list.py` |
| 155 | C | `$RE4NCYF.json` | 文件 | `78dea3225624` | 23494 | 2026-09-29 12:36:53 | `\Users\Administrator\AppData\Local\Temp\h6h7_manifest.json` |
| 156 | C | `$RVY3G8A.py` | 文件 | `b14cfb91b189` | 931 | 2026-09-29 12:37:00 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe.py` |
| 157 | C | `$RCNEW80.py` | 文件 | `ebbd045feb8d` | 1074 | 2026-09-29 12:37:08 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe2.py` |
| 158 | C | `$RKIGBO9.py` | 文件 | `0df03523a544` | 1926 | 2026-09-29 12:37:16 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe3.py` |
| 159 | C | `$RSWRE3A.py` | 文件 | `c69347f8b222` | 930 | 2026-09-29 12:37:24 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe4.py` |
| 160 | C | `$RW1ZIYU.py` | 文件 | `6a0b47c19d0c` | 497 | 2026-09-29 12:37:32 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe5.py` |
| 161 | C | `$RK5WZG7.py` | 文件 | `08c30f60e612` | 2318 | 2026-09-29 12:37:41 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe6.py` |
| 162 | C | `$RHH7UPZ.py` | 文件 | `0ed8b1e6c300` | 2752 | 2026-09-29 12:37:48 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe7.py` |
| 163 | C | `$R112NRG.py` | 文件 | `63ee431f8626` | 1505 | 2026-09-29 12:37:55 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe8.py` |
| 164 | C | `$RYMFFB7.py` | 文件 | `dd6c3d5d77d9` | 796 | 2026-09-29 12:38:03 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe9.py` |
| 165 | C | `$RV40BQB.py` | 文件 | `9a45a565944a` | 1027 | 2026-09-29 12:38:10 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe10.py` |
| 166 | C | `$R23DQ59.py` | 文件 | `7838a6caefd5` | 1139 | 2026-09-29 12:38:18 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe11.py` |
| 167 | C | `$RI2V77W.py` | 文件 | `e3bf3799f515` | 913 | 2026-09-29 12:38:25 | `\Users\Administrator\AppData\Local\Temp\h6h7_probe12.py` |
| 168 | C | `$RH2KMMJ.txt` | 文件 | `4d698c25e8da` | 32650 | 2026-09-29 12:38:32 | `\Users\Administrator\AppData\Local\Temp\h6h7_sec_index.txt` |
| 169 | C | `$RUJTMSJ.py` | 文件 | `c2716250232a` | 2373 | 2026-09-29 12:38:40 | `\Users\Administrator\AppData\Local\Temp\h6h7_secindex.py` |
| 170 | C | `$RL0CHJ6.py` | 文件 | `8545d8b3e9ae` | 2169 | 2026-09-29 12:38:49 | `\Users\Administrator\AppData\Local\Temp\h6h7_sections.py` |
| 171 | C | `$R94T21G.txt` | 文件 | `e3622d41ad1d` | 293795 | 2026-09-29 12:38:57 | `\Users\Administrator\AppData\Local\Temp\h6h7_sections.txt` |
| 172 | C | `$RSMZ5TI.json` | 文件 | `820690332b89` | 89119 | 2026-09-29 12:39:05 | `\Users\Administrator\AppData\Local\Temp\h6h7_sub.json` |
| 173 | C | `$R653ZF2.py` | 文件 | `6c3d4b8a4aa9` | 8780 | 2026-09-29 12:39:13 | `\Users\Administrator\AppData\Local\Temp\h6h7_verify.py` |
| 174 | C | `$R88LCET.json` | 文件 | `6081d3fe749a` | 1679 | 2026-09-29 12:39:23 | `\Users\Administrator\AppData\Local\Temp\h6h7_verify_final.json` |
| 175 | C | `$RBCFAHM.json` | 文件 | `b449cab1ae58` | 1679 | 2026-09-29 12:39:33 | `\Users\Administrator\AppData\Local\Temp\h6h7_verify_out.json` |
| 176 | C | `$R0IM7W5.json` | 文件 | `e826a273dd93` | 25051 | 2026-09-29 12:39:47 | `\Users\Administrator\AppData\Local\Temp\prior_rows.json` |
| 177 | C | `$RDYNXVC.txt` | 文件 | `4b04319ebf80` | 28922 | 2026-09-29 12:39:56 | `\Users\Administrator\AppData\Local\Temp\bp_chunk0.txt` |
| 178 | C | `$RBMB64B.txt` | 文件 | `3b7771b59b5d` | 23301 | 2026-09-29 12:40:05 | `\Users\Administrator\AppData\Local\Temp\bp_chunk1.txt` |
| 179 | C | `$R3PTSCQ.txt` | 文件 | `8e336580a259` | 28764 | 2026-09-29 12:40:14 | `\Users\Administrator\AppData\Local\Temp\bp_chunk2.txt` |
| 180 | C | `$RYOZ6V8.txt` | 文件 | `df24997f675c` | 30592 | 2026-09-29 12:40:22 | `\Users\Administrator\AppData\Local\Temp\bp_chunk3.txt` |
| 181 | C | `$RXE5YPL.txt` | 文件 | `07affcc51325` | 50855 | 2026-09-29 12:40:31 | `\Users\Administrator\AppData\Local\Temp\bp_chunk4.txt` |
| 182 | C | `$RIH2FNA.txt` | 文件 | `f225161ffc47` | 100413 | 2026-09-29 12:40:39 | `\Users\Administrator\AppData\Local\Temp\ln_chunk0.txt` |
| 183 | C | `$R0VTTAY.txt` | 文件 | `8c630d36ad42` | 144942 | 2026-09-29 12:40:48 | `\Users\Administrator\AppData\Local\Temp\ln_chunk1.txt` |
| 184 | C | `$R6QRC8O.txt` | 文件 | `bc183425aad4` | 128598 | 2026-09-29 12:40:57 | `\Users\Administrator\AppData\Local\Temp\ln_chunk2.txt` |
| 185 | C | `$R6AHO5Z.txt` | 文件 | `48ecb97fd806` | 1898 | 2026-09-29 12:41:05 | `\Users\Administrator\AppData\Local\Temp\ln_chunk3.txt` |
| 186 | C | `$R6JCGCR.txt` | 文件 | `3a9299a7e83b` | 37688 | 2026-09-29 12:41:14 | `\Users\Administrator\AppData\Local\Temp\sec_chunk0.txt` |
| 187 | C | `$RU9PL8Y.txt` | 文件 | `be5fa7a158b9` | 36889 | 2026-09-29 12:41:24 | `\Users\Administrator\AppData\Local\Temp\sec_chunk1.txt` |
| 188 | C | `$RGPQY6G.txt` | 文件 | `fc9ba557b105` | 33824 | 2026-09-29 12:41:33 | `\Users\Administrator\AppData\Local\Temp\sec_chunk2.txt` |
| 189 | C | `$RMHJW2E.txt` | 文件 | `4d5f3413ee1e` | 46475 | 2026-09-29 12:41:42 | `\Users\Administrator\AppData\Local\Temp\sec_chunk3.txt` |
| 190 | C | `$RKXK8MS.txt` | 文件 | `cff961540e2c` | 39092 | 2026-09-29 12:41:49 | `\Users\Administrator\AppData\Local\Temp\sec_chunk4.txt` |
| 191 | C | `$RQLUCKW.txt` | 文件 | `78c15ec0e40b` | 55114 | 2026-09-29 12:41:56 | `\Users\Administrator\AppData\Local\Temp\sec_chunk5.txt` |
| 192 | C | `$RUBTUU5.txt` | 文件 | `b5975c9656c9` | 45459 | 2026-09-29 12:42:05 | `\Users\Administrator\AppData\Local\Temp\sec_chunk6.txt` |
| 193 | C | `$RLZBOVM` | 目录（97 件 / 443572 B） | `—` | 443572 | 2026-09-29 12:42:12 | `\Users\Administrator\AppData\Local\Temp\h6h7_ext` |
| 194 | C | `$RZ887S3.py` | 文件 | `ae5199214856` | 2528 | 2026-09-29 12:45:09 | `\Users\Administrator\AppData\Local\Temp\vfinal.py` |
| 195 | C | `$RP4IA7W.txt` | 文件 | `26d12a756bab` | 249 | 2026-09-29 12:45:17 | `\Users\Administrator\AppData\Local\Temp\vfinal.txt` |
| 196 | C | `$RHZ0J57.py` | 文件 | `e5b2fc2faf53` | 1140 | 2026-09-29 12:45:24 | `\Users\Administrator\AppData\Local\Temp\vz.py` |
| 197 | C | `$RVCXR4F.txt` | 文件 | `b624b08da59f` | 2632 | 2026-09-29 12:45:32 | `\Users\Administrator\AppData\Local\Temp\vz.txt` |
| 198 | C | `$RFZADPH.py` | 文件 | `70311764e613` | 528 | 2026-09-29 12:45:39 | `\Users\Administrator\AppData\Local\Temp\vscan.py` |
| 199 | C | `$R9STEGJ.txt` | 文件 | `fef29bfff350` | 266 | 2026-09-29 12:45:47 | `\Users\Administrator\AppData\Local\Temp\vscan.txt` |
| 200 | C | `$RS2LDKV.py` | 文件 | `1042e2ca4bd1` | 2186 | 2026-09-29 12:45:54 | `\Users\Administrator\AppData\Local\Temp\vfin.py` |
| 201 | C | `$R2A7NED.txt` | 文件 | `93a2e8f2c8db` | 232 | 2026-09-29 12:46:03 | `\Users\Administrator\AppData\Local\Temp\vfin.txt` |
| 202 | D | `$RJVEZ6D.py` | 文件 | `e77e7f3455e0` | 25791 | 2026-09-29 13:17:54 | `\私人资料\deposon-repo\mindmap_corpus_v20_r1.py` |
| 203 | D | `$RWGK8KN.pyc` | 文件 | `5c8edd9c4230` | 37254 | 2026-09-29 13:38:15 | `\私人资料\deposon-repo\__pycache__\mindmap_corpus_v20_r1.cpython-314.pyc` |
| 204 | D | `$RYGPU3D.py` | 文件 | `7f5cf2a5eca7` | 1701 | 2026-09-29 13:45:02 | `\私人资料\deposon-repo\results\_v5_pjpm_pc_closeout_probe_2026_09_29.py` |
| 205 | D | `$RK03QDA.txt` | 文件 | `09bc1688c519` | 59106 | 2026-09-29 15:24:54 | `\私人资料\deposon-repo\_tmp_vk_dump.txt` |
| 206 | D | `$RCCO0GP.txt` | 文件 | `cf3564c40e56` | 6548 | 2026-09-29 15:25:01 | `\私人资料\deposon-repo\_tmp_vk_dump2.txt` |
| 207 | D | `$RVOMPMK.txt` | 文件 | `4a9268d7f822` | 808 | 2026-09-29 15:25:09 | `\私人资料\deposon-repo\_tmp_vk_dump3.txt` |

## 附录 B · 5 个 `$R` 目录件逐文件 SHA-12 清单

#### `$R965RZA`（D · 原路径 `\私人资料\deposon-repo\.tmp\_tail3_scratch` · 2026-09-29 11:16:43 · 19 件）

| 相对路径 | 字节 | SHA-12 |
|---|---|---|
| `_child0.py` | 1374 | `108e9597a80f` |
| `_child1.py` | 1374 | `108e9597a80f` |
| `_child2.py` | 1374 | `108e9597a80f` |
| `payload.json` | 5508890 | `13425104558a` |
| `v4a0.json` | 5508890 | `13425104558a` |
| `v4a1.json` | 5508890 | `13425104558a` |
| `v4a2.json` | 5508890 | `13425104558a` |
| `v4b0.json` | 5508890 | `13425104558a` |
| `v4b1.json` | 5508890 | `13425104558a` |
| `v4b2.json` | 5508890 | `13425104558a` |
| `v50.json` | 5508890 | `13425104558a` |
| `v50.json.tmp_8272` | 4088425 | `d4bf98e51199` |
| `v51.json` | 5508890 | `13425104558a` |
| `v51.json.tmp_1896` | 123395 | `b634d9b33a2f` |
| `v52.json` | 412090 | `6d61e84adfbc` |
| `v52.json.tmp_13004` | 4708335 | `54e0e26f8f8f` |
| `v5c0.json` | 5508890 | `13425104558a` |
| `v5c1.json` | 5508890 | `13425104558a` |
| `v5c2.json` | 5508890 | `13425104558a` |

#### `$R2AWLTS`（D · 原路径 `\私人资料\deposon-repo\.tmp\_tail3_scratch` · 2026-09-29 11:17:59 · 19 件）

| 相对路径 | 字节 | SHA-12 |
|---|---|---|
| `_child0.py` | 1374 | `108e9597a80f` |
| `_child1.py` | 1374 | `108e9597a80f` |
| `_child2.py` | 1374 | `108e9597a80f` |
| `payload.json` | 5508890 | `13425104558a` |
| `v4a0.json` | 5508890 | `13425104558a` |
| `v4a1.json` | 5508890 | `13425104558a` |
| `v4a2.json` | 5508890 | `13425104558a` |
| `v4b0.json` | 5508890 | `13425104558a` |
| `v4b1.json` | 5508890 | `13425104558a` |
| `v4b2.json` | 5508890 | `13425104558a` |
| `v50.json` | 412090 | `6d61e84adfbc` |
| `v50.json.tmp_6296` | 3220915 | `2be4ff9d1c97` |
| `v51.json` | 412090 | `6d61e84adfbc` |
| `v51.json.tmp_9428` | 5453535 | `caca7dc7beb5` |
| `v52.json` | 412090 | `6d61e84adfbc` |
| `v52.json.tmp_6520` | 4956735 | `54ace63bb5a9` |
| `v5c0.json` | 5508890 | `13425104558a` |
| `v5c1.json` | 5508890 | `13425104558a` |
| `v5c2.json` | 5508890 | `13425104558a` |

#### `$RCVN2DZ`（D · 原路径 `\私人资料\deposon-repo\.tmp\_tail3_scratch` · 2026-09-29 11:19:29 · 19 件）

| 相对路径 | 字节 | SHA-12 |
|---|---|---|
| `_child0.py` | 1374 | `108e9597a80f` |
| `_child1.py` | 1374 | `108e9597a80f` |
| `_child2.py` | 1374 | `108e9597a80f` |
| `payload.json` | 5508890 | `13425104558a` |
| `v4a0.json` | 5508890 | `13425104558a` |
| `v4a1.json` | 5508890 | `13425104558a` |
| `v4a2.json` | 5508890 | `13425104558a` |
| `v4b0.json` | 5508890 | `13425104558a` |
| `v4b1.json` | 5508890 | `13425104558a` |
| `v4b2.json` | 5508890 | `13425104558a` |
| `v50.json` | 412090 | `6d61e84adfbc` |
| `v50.json.tmp_4676` | 5080935 | `990c390ce477` |
| `v51.json` | 5508890 | `13425104558a` |
| `v51.json.tmp_3940` | 2849125 | `736b9cd09525` |
| `v52.json` | 412090 | `6d61e84adfbc` |
| `v52.json.tmp_876` | 5508890 | `13425104558a` |
| `v5c0.json` | 5508890 | `13425104558a` |
| `v5c1.json` | 5508890 | `13425104558a` |
| `v5c2.json` | 5508890 | `13425104558a` |

#### `$REQ4HDX.tmp_v3df`（D · 原路径 `\私人资料\deposon-repo\.tmp_v3df` · 2026-09-29 12:10:46 · 7 件）

| 相对路径 | 字节 | SHA-12 |
|---|---|---|
| `final_audit.py` | 5139 | `4eb7fba16f8c` |
| `inspect_c1.py` | 2016 | `842482bf2f15` |
| `legacy_dist.py` | 1074 | `f332ddddacbe` |
| `probe_payoff.py` | 1258 | `b9c5c6dd17d4` |
| `sha_check.py` | 1149 | `9ce9b253d507` |
| `summary.py` | 3220 | `6c65dcaed8fc` |
| `verify.py` | 3432 | `a5c8adfa12e5` |

#### `$RLZBOVM`（C · 原路径 `\Users\Administrator\AppData\Local\Temp\h6h7_ext` · 2026-09-29 12:42:12 · 97 件）

| 相对路径 | 字节 | SHA-12 |
|---|---|---|
| `0011b7924dfb.txt` | 6499 | `ef6a8223d3b1` |
| `02443dd300ce.txt` | 1040 | `e152f88715b5` |
| `042fa374a63f.txt` | 1217 | `acecdfd43324` |
| `09784ff172b3.txt` | 5188 | `f95f44b6d20e` |
| `0a2caf0a2bd2.txt` | 2586 | `583fc912d3e8` |
| `0d36d7cd0589.txt` | 23084 | `593fc394be21` |
| `0fda737a2203.txt` | 5327 | `aeb3bd9b0e15` |
| `11cd57800bd6.txt` | 4356 | `b48876c3498b` |
| `120295a19655.txt` | 324 | `e1bf3e0c27b5` |
| `125998731621.txt` | 896 | `74ef5a682401` |
| `183205baa9ac.txt` | 2687 | `20b53de6faea` |
| `1c0885d2b1fa.txt` | 1373 | `85732f34e63e` |
| `2185433b1f32.txt` | 675 | `95fe2de076ef` |
| `229d76e1b86f.txt` | 2801 | `a7fd55fda527` |
| `23bb7d39bf58.txt` | 3927 | `3a207b44e839` |
| `26537967db82.txt` | 6562 | `eca30f116959` |
| `27db4950f710.txt` | 659 | `94f947672a8d` |
| `2e3ec17259e2.txt` | 2149 | `c86d174466e6` |
| `2e6a31af5e4b.txt` | 1312 | `e07ac2f8469d` |
| `2efdc3d7741d.txt` | 2427 | `25de4504be8f` |
| `3594378e7d1d.txt` | 11353 | `14ffba3b586e` |
| `3de722dc9e39.txt` | 8261 | `adc42d969192` |
| `3fbc7f4dfd22.txt` | 4393 | `9291b6238c3e` |
| `40dda52e5d92.txt` | 2038 | `3404e1f66f93` |
| `413ddb0bd00e.txt` | 9466 | `fd7f823d826f` |
| `43265e4bf2be.txt` | 3760 | `e37a68b8461e` |
| `4af67e6cbe71.txt` | 1367 | `ecb3fe28d060` |
| `4b10cde29c27.txt` | 16024 | `fe4658265d7b` |
| `5198a7059c06.txt` | 8877 | `5776034b6a11` |
| `543479649b3e.txt` | 146 | `4340df6c42fa` |
| `54859cf2217a.txt` | 801 | `8c090b29c6b4` |
| `588b45430e88.txt` | 6737 | `2695e3b4f33e` |
| `58e15c07af33.txt` | 1865 | `835063949897` |
| `67aafb57a8ed.txt` | 706 | `5941e52caed6` |
| `6952b3b02b96.txt` | 1593 | `4c4a171be837` |
| `6a5b6eb635f0.txt` | 742 | `6179de601178` |
| `6a7b0c20a133.txt` | 2807 | `8e0ee53c62aa` |
| `6d72e74b3482.txt` | 3444 | `ee8ba095ac98` |
| `6e23b54727e6.txt` | 3882 | `1f162278a223` |
| `70bd41d9722d.txt` | 1057 | `a7d2967446cb` |
| `71d5c23d9f76.txt` | 803 | `f5b250ccdf02` |
| `759c25b21ed4.txt` | 6215 | `fb0ee28638a5` |
| `772112cf5bd4.txt` | 357 | `0edbdcbe5d0b` |
| `7a95307a3293.txt` | 8404 | `c0c29849c570` |
| `7d4b5dd967e2.txt` | 3317 | `f6a3c7cec26b` |
| `85c3a5cfd84d.txt` | 1838 | `1e2652b1d9d9` |
| `8875bf0bc50d.txt` | 1732 | `ceb5ae16e65e` |
| `8c07ab5aa968.txt` | 3950 | `facedb685508` |
| `8cd736ba9f91.txt` | 1621 | `a42732fead18` |
| `8d00c6d4a242.txt` | 3989 | `f975416a1787` |
| `8ece24be6b8a.txt` | 1961 | `0f90a6ef2632` |
| `8fcdd872dc07.txt` | 427 | `25b838ce70bf` |
| `905544775aee.txt` | 3124 | `9487b23a2ff7` |
| `90ba7f7a7fbe.txt` | 519 | `395709de75f5` |
| `9119bb791dc1.txt` | 845 | `6d42434c848e` |
| `958188c83cf0.txt` | 5094 | `75c80399345d` |
| `95925a562597.txt` | 6059 | `20ac5751f868` |
| `972401e056f6.txt` | 15389 | `30028e9a8316` |
| `99b835595dfb.txt` | 9088 | `470d8a8182f9` |
| `a964defb923d.txt` | 4693 | `7adf9eadd3e7` |
| `ace3c6b390cb.txt` | 3194 | `4e8ea384b99d` |
| `b1c227d54a82.txt` | 5505 | `c007470ed32e` |
| `b41a17eda169.txt` | 3539 | `dc23361dcda3` |
| `be7aa1c479b2.txt` | 2051 | `ef9cd01a13e8` |
| `bec666969ffc.txt` | 3840 | `6a0b65655f43` |
| `c08e7abf5ee3.txt` | 11444 | `8051e72c1244` |
| `c0d629df69d8.txt` | 1276 | `eea895247a36` |
| `c1791a7811f3.txt` | 2037 | `7effd68c65a9` |
| `c350e420eca6.txt` | 357 | `900bbbb29f9f` |
| `c3de25e6df57.txt` | 56553 | `5e665a9806d1` |
| `c41c1d6aa794.txt` | 150 | `8b5ae1071755` |
| `c87eb8974268.txt` | 2995 | `ffe38641c3d4` |
| `cfab992cf939.txt` | 4374 | `7efb2076ef80` |
| `d66388b6532d.txt` | 473 | `65c5c5ac277b` |
| `d7f03fde4067.txt` | 357 | `260a9ee0f075` |
| `d8eafdd67119.txt` | 12313 | `818b7bbcb83d` |
| `d8f2b99aa527.txt` | 2784 | `254b09a3dfcd` |
| `ddf0d1aa96d2.txt` | 1593 | `6393a380f9b4` |
| `deee45f45c5d.txt` | 3697 | `3046d09a76d8` |
| `e151e48ab4b4.txt` | 7593 | `70547e8d7053` |
| `e240ca712be6.txt` | 3973 | `52cd077be6f2` |
| `e4320f20cad4.txt` | 3566 | `301f5907a249` |
| `e6f8ded3c4ff.txt` | 1518 | `6a5956e674f3` |
| `ecb406570615.txt` | 2445 | `2f8a824f874d` |
| `ecdbf3a7a9c2.txt` | 4737 | `ca63ec665aae` |
| `ee005ea1f031.txt` | 208 | `fae92e33fd7e` |
| `eecbe2b1341d.txt` | 3751 | `7a8b6c753b31` |
| `ef648f34a3a3.txt` | 383 | `eb2459e024fc` |
| `f2934e5279e6.txt` | 3149 | `c843f253bed2` |
| `f2a655cd5e54.txt` | 936 | `d29fa6c62d77` |
| `f4a6bdd43962.txt` | 2901 | `4ba6b7726ee9` |
| `f4d5b755736a.txt` | 2593 | `654f923d1a10` |
| `fa5da7a307bd.txt` | 1120 | `5e7e71033d39` |
| `fa9cd7ffa3f2.txt` | 2119 | `dedb1929d38a` |
| `fb5656993071.txt` | 23637 | `720c5e64aba9` |
| `fd38a2a1ea05.txt` | 5770 | `c7a75b82dbec` |
| `fe80bad08eef.txt` | 10808 | `32cc1e6accd1` |
