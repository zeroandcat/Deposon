# V3 族 产物盘点（证据盘点件 · evidence-auditor · 2026-10-23）

> 📌 **本件之性质**：**产物在盘性盘点**（**逐件实测**）—— **0 判定 · 0 终判 · 0 宣告**。
> 📌 **授权源**：PI 2026-10-23 17:35 卡 `ask_7fa3936e1c09047a5f8afbfb` 答 `e2_order` 逐字「**下轮上下文窗口依次全部**」；落账件 `pi_rulings\_pi_card_answers_register_2026_10_23_v259.md`（10,244 B／`7d88011fd1d9`）§4 之点法二条：**「按内容／产物找，⛔0 按题名找」**＋**「账只用于核对，不用于定值」**。
> 📌 **盘点范围**：**只点 `V3 族`**（e2「14 族依次全部」之第 1 族）＝ ① `V3-recheck` 预登记链（v1 → v1p5）② `V3-S` 预登记（含短语模板附属件）。
> 📌 **观测时点**：**2026-10-23 17:43–17:55（GMT+0800）**；凡表内「观测时点」列皆指此窗内**当场实算**（`Get-FileHash` SHA-256 取前 12 位 · 小写）。
> 📌 **本件 0 做**：0 回改任何既有件一字 · 0 移动／重命名／删除／新建目录 · 0 落五终判（pass／af／kd／fail／give-up）· 0 闭任何 KD · 0 宣告门槛成就或①段毕 · 0 代 PI 裁／释／择／给值 · 0 跑实验 · 0 联网 · 0 调 LLM／API · 0 读 `〔归档区〕*` 之内容 · 0 读 `〔本地路径已脱敏〕` · 0 读任何派工单指定之他棒结论作定值。

---

## §0 本棒之仪器（skill 实读 · 算法规 · 仪器自审）

### §0.1 两件必带 skill（**实读路径为实测现值**）

| # | skill 名 | 实测加载结果 | 实测现值路径 |
|:-:|:--|:--|:--|
| 1 | `superpowers:verification-before-completion` | **加载成功** | `〔本地路径已脱敏〕` |
| 2 | `scientific-research-workflows:scientific-critical-thinking` | **「Local skill not found」（带前缀名未命中）** | — |
| 2b | `scientific-critical-thinking`（**裸名**） | **加载成功** | `〔本地路径已脱敏〕` |

> 📌 **如实登记 · 不隐去**：第 2 件以**带前缀名**调用时**未命中**，本棒改以**裸名** `scientific-critical-thinking` 命中上述路径并**全读**。两次调用结果均如实列出，未以任一面掩饰另一面。
> 📌 **本棒自取之纪律**：① `verification-before-completion` → 「**NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE**」⇒ 本件凡称「在盘／不在盘／字节／指纹」皆附**当轮实测**；② `scientific-critical-thinking` → 「**Always distinguish between Data (what was observed) and interpretation**」＋「**Acknowledge uncertainty**」⇒ 本件严格分「**盘上事实**」与「**在册他棒字面**」两栏，**0 混同**；其「**先核 prereg 再判证据**」之取向亦用于本件之读数面 → 预登记所要求之产物名取自**预登记本体 §3.2／§3.4 字面**。

### §0.2 算法规（**禁内建 `hash()`**）

- 文件指纹 ＝ `Get-FileHash -Algorithm SHA256` → `.Hash.ToLower().Substring(0,12)`（**SHA-12 · 小写**）。
- 长串指纹（留出集有序指纹）＝ `System.Security.Cryptography.SHA256`（**与 `hashlib.sha256` 同算法**）· UTF-8 编码 · hexdigest 小写。
- 存在性判断 ＝ **`.Name -like` 长名式**（⛔0 单用 `-Filter`）；递归面以 `Get-ChildItem -Recurse -Force` + `Where-Object { $_.Name -like ... }` 取得。

### §0.3 仪器自审（**测量仪器自身即误差源**）

> 本棒于 §3.6 之独立复算**首轮得出与在册自报值不符**之结果。**先审仪器，不先指件**：查出系本棒所用排序为 **PowerShell `Sort-Object`（文化序·非 Ordinal）** 且 `#idx` 被**按字符串**比较（`#10` 先于 `#2`）所致 ⇒ **改以 `[string]::CompareOrdinal`（UTF-8 字节序）＋ 数值 `idx` 复算**，得值与在册自报值**逐字节相符**。**此一节之记，0 隐去首轮不符，亦 0 以「复算失败」充结论。**

---

## §1 盘点口径（**先立口径，后点数**）

| 项 | 本件所采口径 |
|:--|:--|
| **计数单位** | **件**（PI 2026-10-22 17:5x 之尺：**件数，非体积**） |
| **「在盘」** | `Test-Path` ＝ True **且**当轮实算得 bytes ＋ SHA-12；**主树** ＝ `〔本地路径已脱敏〕` 内 · **仓外** ＝ `〔本地路径已脱敏〕` 内（只读核 SHA，0 写） |
| **「不在盘」** | 主树 + 仓外 + 仓内镜像面（`results\_glm_evidence_unpacked_2026_10_13\…`）**三处皆无** |
| **找法** | **按内容／产物找**（以**内容命中**与**预登记所要求之产物名**双径定位）· **⛔0 按题名找**（出件棒题名常异） |
| **不采为「仍欠」之据** | ⛔0「某棒 failed」· ⛔0「无同题重派」· ⛔0「在册清单载欠」 |
| **现态记法** | 只记「**跑过没跑过／有读数没读数／有判定没判定**」三栏事实，**0 落终判** |
| **交叉件** | 与他族（`S3/S4` 族）**同件**者**单列并标明**，**防重复计数**（不重复计入 V3 族总数） |

---

## §2 `V3-recheck` 预登记链（v1 → v1p5）

### §2.1 预登记件（**7 件** · 主树 6 ＋ 仓外 1）

| # | 件（`results\evidence\register\` 下） | bytes | SHA-12 | 所在面 | 观测时点 |
|:-:|:--|--:|:--|:--|:--|
| 1 | `_v3_recheck_prereg_v1_2026_09_27.md` | 37,346 | `88052d7db895` | 主树 | 17:45 |
| 2 | `_v3_recheck_prereg_v1p1_2026_09_27.md` | 42,970 | `bcc3cee23e82` | 主树 | 17:45 |
| 3 | `_v3_recheck_prereg_v1p2_2026_09_27.md` | 38,932 | `9da148037744` | 主树 | 17:45 |
| 4 | `_v3_recheck_prereg_v1p3_2026_09_27.md` | 35,200 | `272ed65bf50e` | 主树 | 17:45 |
| 5 | `_v3_recheck_prereg_v1p4_2026_09_27.md` | 69,406 | `5294e4a2bd14` | 主树 | 17:45 |
| 6 | `_v3_recheck_prereg_v1p5_2026_09_29.md` | 18,680 | `7b1374578de4` | 主树 | 17:45 |
| 7 | `_v3_recheck_prereg_v1p2_2026_09_29.md` | 25,854 | `a667a5f69b7a` | **仓外**（`〔本地路径已脱敏〕`）· **主树不在盘** | 17:53 |

> 📌 **与在册索引之差（事实登记）**：主代理版树 `results\work\process\_gate1_gap_tree_main_2026_10_23.md` L24–L25 载本链「**7 件在盘**」（列 v1 / v1p1 / **v1p2(×2)** / v1p3 / v1p4 / v1p5）⇒ **当轮实测：主树实见 6 件，第 7 件（v1p2 · 09-29）不在主树**（在册索引未标其面）。该件之**立线角色**见 `_v3_recheck_prereg_v1p5_2026_09_29.md` L26（「`results/_v3_recheck_prereg_v1p2_2026_09_29.md` ＝ `a667a5f69b7a` / 25,854 B ｜ **v1.2**（L1 字面 · 改列提案件）｜ v1.2（**其二**）」）。
> 📌 **对账**：本棒**不沿用**树之「7 件在盘」之面判定；**以当轮实测为准**（树自身 L6 已载「凡标『未核得』者 ＝ 本轮未逐件点过产物，非『确认缺失』」）。

### §2.2 产物面 —— 执行器面（**11 件** · 0 合并）

| 件 | bytes | SHA-12 | 观测时点 |
|:--|--:|:--|:--|
| `results\tool\generator\_v3_recheck_01_executor_2026_09_27.py` | 41,004 | `919fa909381e` | 17:47 |
| `results\tool\generator\_v3_recheck_04_executor_2026_09_27.py` | 49,405 | `e098fa21700d` | 17:47 |
| `results\tool\generator\_v3_recheck_08_executor_2026_09_27.py` | 15,598 | `21c4ba4d479e` | 17:47 |
| `results\tool\generator\_v3_recheck_26_executor_2026_09_27.py` | 15,056 | `46c326c756c3` | 17:47 |
| `results\tool\generator\_v3_recheck_26_preexp_executor_2026_09_27.py` | 38,726 | `775217a462f5` | 17:47 |
| `results\tool\generator\_v3_recheck_26b_executor_2026_09_27.py` | 43,171 | `5c906113a210` | 17:47 |
| `results\tool\generator\_v3_recheck_26b_executor_r2_2026_09_28.py` | 52,272 | `0808af6212c5` | 17:47 |
| `results\tool\generator\_v3_recheck_26b_executor_r3_2026_09_29.py` | 64,959 | `6c83e7a7ca2e` | 17:47 |
| `results\_v3_recheck_08b_executor\executor_2026_09_27.py` | 43,901 | `b292410d9a69` | 17:47 |
| `results\_v3_recheck_08c_preexp_data\executor_2026_09_27.py` | 37,775 | `cb6eb9164df3` | 17:47 |
| `results\_v3_recheck_08c_preexp_data\_v3_recheck_08c_sha12fix_r1_2026_10_12.py` | 1,395 | `4b7ed4d0a3e5` | 17:47 |

### §2.3 产物面 —— 读数面（**17 件** · 派生 JSON 0 合并）

| 件 | bytes | SHA-12 | 观测时点 |
|:--|--:|:--|:--|
| `results\readout\run\_v3_recheck_01_result_2026_09_27.json` | 167,831 | `c19e2ab24e63` | 17:46 |
| `results\readout\run\_v3_recheck_04_result_2026_09_27.json` | 840,158 | `db8cfb974ce3` | 17:46 |
| `results\readout\run\_v3_recheck_05_result_2026_09_28.json` | 450,751 | `81460acbb4f9` | 17:46 |
| `results\readout\run\_v3_recheck_08_result_2026_09_27.json` | 10,587 | `0d2af01086db` | 17:46 |
| `results\readout\run\_v3_recheck_10_result_2026_09_27.json` | 82,535 | `5d4b6baf1b18` | 17:46 |
| `results\readout\run\_v3_recheck_12_result_2026_09_27.json` | 187,612 | `cdb37ed0b32f` | 17:46 |
| `results\readout\run\_v3_recheck_19_result_2026_09_27.json` | 59,888 | `df07cf80930f` | 17:46 |
| `results\readout\run\_v3_recheck_21_result_2026_09_27.json` | 44,928 | `354ae9c14fe2` | 17:46 |
| `results\readout\run\_v3_recheck_26_result_2026_09_27.json` | 11,994 | `eb6a99dd46dd` | 17:46 |
| `results\readout\run\_v3_recheck_26_preexp_data_2026_09_27.json` | 94,658 | `177c88e1bd82` | 17:46 |
| `results\readout\run\_v3_recheck_26b_result_2026_09_27.json` | 44,379 | `49c6e5a07732` | 17:46 |
| `results\readout\run\_v3_recheck_26b_r3_result_2026_09_29.json` | 54,294 | `c9d3c9f819f1` | 17:46 |
| `results\readout\run\_v3_recheck_27_result_2026_09_27.json` | 42,571 | `e06cb51fb3af` | 17:46 |
| `results\readout\run\_v3_recheck_28_result_2026_09_27.json` | 26,113 | `c0a8cb9029a7` | 17:46 |
| `results\readout\run\_v3_recheck_35_result_2026_09_27.json` | 35,091 | `a8a4befb21f5` | 17:46 |
| `results\_v3_recheck_08b_executor\result_2026_09_27.json` | 88,052 | `f9a7fa2d65b1` | 17:47 |
| `results\_v3_recheck_08c_preexp_data\result_2026_09_27.json` | 146,601 | `689a6e4427a8` | 17:47 |

### §2.4 产物面 —— 报告面（**18 件**）

| 件 | bytes | SHA-12 | 观测时点 |
|:--|--:|:--|:--|
| `results\readout\run\_v3_recheck_01_rescript_2026_09_27.md` | 14,541 | `a3c95102290f` | 17:46 |
| `results\readout\run\_v3_recheck_04_rescript_2026_09_27.md` | 14,780 | `34099595fe75` | 17:46 |
| `results\readout\run\_v3_recheck_05_rescript_2026_09_28.md` | 22,178 | `88b7eaf8675d` | 17:46 |
| `results\readout\run\_v3_recheck_08_rescript_2026_09_27.md` | 10,459 | `2e08b9ae9f09` | 17:46 |
| `results\readout\run\_v3_recheck_10_rescript_2026_09_27.md` | 14,445 | `fc0ffd27adca` | 17:46 |
| `results\readout\run\_v3_recheck_12_rescript_2026_09_27.md` | 21,222 | `776c86c735f8` | 17:46 |
| `results\readout\run\_v3_recheck_12_jsv_check_2026_09_27.md` | 15,821 | `c5eab30e9fc6` | 17:46 |
| `results\readout\run\_v3_recheck_12_rj5_provenance_2026_09_27.md` | 23,822 | `20f15c49feb5` | 17:46 |
| `results\readout\run\_v3_recheck_19_rescript_2026_09_27.md` | 11,089 | `82a947f2aebd` | 17:46 |
| `results\readout\run\_v3_recheck_21_rescript_2026_09_27.md` | 14,618 | `04f6ecd482b9` | 17:46 |
| `results\readout\run\_v3_recheck_26_rescript_2026_09_27.md` | 13,747 | `6b86576146a3` | 17:46 |
| `results\readout\run\_v3_recheck_26_preexp_report_2026_09_27.md` | 23,048 | `a46230e344af` | 17:46 |
| `results\readout\run\_v3_recheck_26b_rescript_2026_09_27.md` | 30,552 | `ae81d9b59054` | 17:46 |
| `results\readout\run\_v3_recheck_27_rescript_2026_09_27.md` | 14,599 | `6f045bdc70e7` | 17:46 |
| `results\readout\run\_v3_recheck_28_rescript_2026_09_27.md` | 10,187 | `a0734e0a6860` | 17:46 |
| `results\readout\run\_v3_recheck_35_rescript_2026_09_27.md` | 13,211 | `138faf395f40` | 17:46 |
| `results\_v3_recheck_08b_executor\rescript_2026_09_27.md` | 18,501 | `78f3aba1f24c` | 17:47 |
| `results\_v3_recheck_08c_preexp_data\rescript_2026_09_27.md` | 17,069 | `035af77db626` | 17:47 |

### §2.5 产物面 —— 判定面与链面（**4 件**）

| 件 | 性质 | bytes | SHA-12 | 观测时点 |
|:--|:--|--:|:--|:--|
| `results\verdict\judgement\_v3_recheck_verdict_register_2026_09_27.md` | **改判总表**（逐条登载 14 档之 rescript／result 指纹 ＋ 状态） | 112,085 | `d9b6b974cfc1` | 17:47 |
| `results\verdict\judgement\_v3_recheck_26b_verdict_prep_2026_10_01.md` | #26b 之判定准备件 | 36,133 | `3aab3f7660fc` | 17:47 |
| `docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md` | **勘误链载体**（E-46 · E-48 · E-55 · E-59 · E-60 各节之登载体） | 857,551 | `41f5f1689d09` | 17:48 |
| `letters\_v3_recheck_indep_judgment_request_2026_09_27.md` | 外部独立判定请求函 | 22,702 | `2c486c1791d5` | 17:48 |

### §2.6 `V3-recheck` 链之逐条现态（**只记事实 · 0 落终判**）

**口径**：预登记 `v1` 件 §2.2 冻结 **9 条** kill-line（#1·#4·#5·#8·#10·#12·#26·#27·#28）；`v1.1` 件追加冻结 **3 条**（#19·#35·#21）；`v1.2` 起增档 **#08b**（顶替重跑）与 **#08c**（真实 N 轴预实验）；`v1.3`/`v1.4` 为 #8 之线；`v1.5` 为**口径更正件**（**0 实验面** · 其 §0.1 自述「本件 0 开跑」）。

| 条 | 读数件（result） | 报告/改判件（rescript） | 跑过没跑过 | 有读数没读数 | 有判定没判定 | 观测时点 |
|:-:|:--|:--|:--|:--|:--|:--|
| #1 | 在盘 `c19e2ab24e63` | 在盘 `a3c95102290f` | 跑过 | 有 | 有（改判总表 ＋ 勘误链 E-48） | 17:46 |
| #4 | 在盘 `db8cfb974ce3` | 在盘 `34099595fe75` | 跑过 | 有 | 有（同上） | 17:46 |
| #5 | 在盘 `81460acbb4f9` | 在盘 `88b7eaf8675d` | 跑过 | 有 | 有（改判总表本体 L43 仍记「0 件（未跑）」；**并发注记**载于勘误链 E-46） | 17:46 |
| #8 | 在盘 `0d2af01086db` | 在盘 `2e08b9ae9f09` | 跑过 | 有 | 有 | 17:46 |
| #10 | 在盘 `5d4b6baf1b18` | 在盘 `fc0ffd27adca` | 跑过 | 有 | 有 | 17:46 |
| #12 | 在盘 `cdb37ed0b32f` | 在盘 `776c86c735f8`（另附 `c5eab30e9fc6` JSV 检查件、`20f15c49feb5` 溯源件） | 跑过 | 有 | 有 | 17:46 |
| #19 | 在盘 `df07cf80930f` | 在盘 `82a947f2aebd` | 跑过 | 有 | 有 | 17:46 |
| #21 | 在盘 `354ae9c14fe2` | 在盘 `04f6ecd482b9` | 跑过 | 有 | 有（走读回函归 C-4 面 · 勘误链 E-48 L4019 列其为**排除面**） | 17:46 |
| #26 | 在盘 `eb6a99dd46dd`（另预实验 `177c88e1bd82` ＋ 报告 `a46230e344af`） | 在盘 `6b86576146a3` | 跑过 | 有 | 有 | 17:46 |
| #26b | 在盘 `49c6e5a07732` ＋ r3 `c9d3c9f819f1` | 在盘 `ae81d9b59054` | 跑过（含 r2／r3 两轮） | 有 | **部分** —— **r3 结果件在盘而无对应 r3 改判件**（全仓 0 命中 `_v3_recheck_26b_r3_rescript*`） | 17:47 |
| #27 | 在盘 `e06cb51fb3af` | 在盘 `6f045bdc70e7` | 跑过 | 有 | 有 | 17:46 |
| #28 | 在盘 `c0a8cb9029a7` | 在盘 `a0734e0a6860` | 跑过 | 有 | 有 | 17:46 |
| #35 | 在盘 `a8a4befb21f5` | 在盘 `138faf395f40` | 跑过 | 有 | 有（E-59 就其 result 面之登记滞后作专项登记） | 17:46 |
| #08b | 在盘 `f9a7fa2d65b1` | 在盘 `78f3aba1f24c` | 跑过 | 有 | 有（E-48 L3994 列为在链 12 份之一） | 17:47 |
| #08c | 在盘 `689a6e4427a8` | 在盘 `035af77db626` | 跑过（预实验） | 有 | **件内自载非判定件**（勘误链 E-48 L4021 自注「`verdict = null` 三面一致 · 非判定件」） | 17:47 |

> 📌 **`V3-recheck` 链之链态**：**在盘（部分 1 处）** —— 15 档中 **14 档**之读数件＋改判件双全；**#26b 之 r3 一档缺改判件**。

### §2.7 登记值与盘上现值之差（**9 处 · 皆有在册说明 · 本棒 0 断链**）

| 件 | 在册登记值 | 盘上实测值 | 在册说明（件名＋行号） |
|:--|:--|:--|:--|
| `_v3_recheck_01_rescript_2026_09_27.md` | `434b3213bdce` / 13,233（勘误链 E-48 L3990；改判总表 L41） | `a3c95102290f` / 14,541 | `letters\TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` **L515**（14541／`a3c95102290f` · 「批量 mtime 簇 ＋ 边界前既有件」） |
| `_v3_recheck_04_rescript_2026_09_27.md` | `2e0f6b8bf141` / 13,472（L3991；总表 L42） | `34099595fe75` / 14,780 | 同上 **L516** |
| `_v3_recheck_12_rescript_2026_09_27.md` | `1cd36ac1b2c0` / 19,914（L3996；总表 L47） | `776c86c735f8` / 21,222 | 同上 **L521** |
| `_v3_recheck_26b_rescript_2026_09_27.md` | `c300e74a082c` / 29,349（L3999；总表 L51） | `ae81d9b59054` / 30,552 | `deposon_team\plugins\_tdf_s4_final_2026_10_12.py` **L42**（锚表载 `ae81d9b59054`）；同 L526 |
| `_v3_recheck_35_result_2026_09_27.json` | `e9aa6e5180ca` / 34,547（总表 L54） | `a8a4befb21f5` / 35,091 | 勘误链 **E-59**：`docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md` **L5431／L5471／L5492**（两读面并列 · Δ ＋544 B · 登记滞后） |
| `_v3_recheck_26_rescript_2026_09_27.md` | `3d9ad5f1540d` / 8,937（总表 L50） | `6b86576146a3` / 13,747 | 勘误链 **E-60** 同文件 **L5440**（被登件**前 8,937 B** 之 SHA-256 全值 ＝ 登记值 · Δ 4,810 B 纯追加）；E-48 L3998 载现值 |
| `_v3_recheck_08c_preexp_data\rescript_2026_09_27.md` | `AA02CBFC84E3` / 15,211（E-48 L4021） | `035af77db626` / 17,069 | `results\_book_05_results_index_2026_10_22.md` **L1762**；`results\doc\document\_zone_balance_inventory_2026_10_13.md` **L1191** |
| `_v3_s2_executor\rescript_2026_09_27.md` | `331022480A57` / 23,039（E-48 L4023） | `ff0f964be8aa` / 25,151 | `_book_05_results_index_2026_10_22.md` **L1778**；`_zone_balance_inventory_2026_10_13.md` **L1233** |
| `_v3_s_phrasetemplate_preexp_data\rescript_2026_09_27.md` | `6DF402298557` / 14,510（E-48 L4026） | `d42ea1fa61f1` / 17,574 | `_book_05_results_index_2026_10_22.md` **L1796**；`_zone_balance_inventory_2026_10_13.md` **L1243** |

> 📌 **另**：改判总表本体之在册值（`9708E7EF1F8C` / 65,913 · 勘误链 E-46 L3494）与盘上实测（`d9b6b974cfc1` / 112,085）**不符**；**此差异已在链内自注**——勘误链 **E-48 L4009** 载「§22.46.4 ⚠ **并发写登记**（本棒**不以其为 SHA 锚**）」。**本棒 0 代其归因、0 断链、0 回改历史行。**

---

## §3 `V3-S` 预登记链（**2 件立项件**）

### §3.1 预登记件（**2 件**）

| 件 | bytes | SHA-12 | 观测时点 |
|:--|--:|:--|:--|
| `results\evidence\register\_v3_s_prereg_v1_2026_09_27.md`（S1–S4 四段立线） | 46,836 | `ef5a40554960` | 17:45 |
| `results\evidence\register\_v3_s_phrasetemplate_prereg_v1_2026_09_27.md`（短语模板附属件） | 33,932 | `7e1323b09030` | 17:45 |

### §3.2 S 段产物（**S1 3 ＋ S2 3 ＋ S3 5 ＋ 短语模板 3 ＝ 14 件**）

| 段 | 件 | bytes | SHA-12 | 观测时点 |
|:-:|:--|--:|:--|:--|
| S1 | `results\_v3_s1_executor\executor_2026_09_27.py` | 54,937 | `10870941c283` | 17:47 |
| S1 | `results\_v3_s1_executor\result_2026_09_27.json` | 24,975 | `bfc99c3133dd` | 17:47 |
| S1 | `results\_v3_s1_executor\rescript_2026_09_27.md` | 17,253 | `9d49a632ee81` | 17:47 |
| S2 | `results\_v3_s2_executor\executor_2026_09_27.py` | 84,993 | `f1e272a0924a` | 17:47 |
| S2 | `results\_v3_s2_executor\result_2026_09_27.json` | 51,039 | `d73d51e670de` | 17:47 |
| S2 | `results\_v3_s2_executor\rescript_2026_09_27.md` | 25,151 | `ff0f964be8aa` | 17:47 |
| S3 | `results\_v3_s3_wordexpand_data\executor_2026_09_28.py` | 46,005 | `80f1445ce45d` | 17:47 |
| S3 | `results\_v3_s3_wordexpand_data\executor_r1_2026_09_28.py` | 43,524 | `39c29e0f092e` | 17:47 |
| S3 | `results\_v3_s3_wordexpand_data\result_2026_09_28.json` | 34,953 | `f7f6d875d73a` | 17:47 |
| S3 | `results\_v3_s3_wordexpand_data\rescript_2026_09_28.md` | 18,225 | `98d4f62cd52a` | 17:47 |
| S3 | `results\_v3_s3_wordexpand_data\rescript_r1_2026_09_28.md` | 17,168 | `c991ddb1deb4` | 17:47 |
| 短语 | `results\_v3_s_phrasetemplate_preexp_data\executor_2026_09_27.py` | 35,555 | `96f491a8e2bf` | 17:47 |
| 短语 | `results\_v3_s_phrasetemplate_preexp_data\result_2026_09_27.json` | 36,844 | `fae3c4640507` | 17:47 |
| 短语 | `results\_v3_s_phrasetemplate_preexp_data\rescript_2026_09_27.md` | 17,574 | `d42ea1fa61f1` | 17:47 |

### §3.3 S3 采集面与读数面（**5 件**）

| 件 | bytes | SHA-12 | 观测时点 |
|:--|--:|:--|:--|
| `results\verdict\pi_register\_v4_pi_cot_v3_dataset_addendum_s3_d1fill_2026_10_01.json` | 46,909 | `b9026cbf5ca2` | 17:48 |
| `results\verdict\pi_register\_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json` | 17,252 | `c0ebbd1f4633` | 17:48 |
| `results\readout\reading\_s3_kv3s_3_full_recompute_2026_10_01.md` | 22,183 | `b0123f161c10` | 17:48 |
| `results\readout\reading\_v3_s3_collection_brief_2026_09_28.md` | 19,045 | `d5ba1161e37f` | 17:48 |
| `results\readout\reading\_v3_s3_wordexpand_recheck_r1_2026_09_28.json` | 33,867 | `67ccea282d1c` | 17:48 |

### §3.4 S 段判定面（**主树在盘 5 件**）

| 件 | bytes | SHA-12 | 观测时点 |
|:--|--:|:--|:--|
| `results\verdict\judgement\_kv3s_4_4_rejudge_2026_10_09.md`（`K-V3S-4-4` 重判件） | 42,687 | `bc397d5099dd` | 17:47 |
| `results\verdict\judgement\_s4_heldout_sampling_caliber_ruling_2026_10_09.md` | 35,453 | `fb1b696de1d6` | 17:47 |
| `results\verdict\judgement\_s4_final_ruling_effectivity_register_2026_10_09.md` | 32,975 | `21f2926efc5d` | 17:47 |
| `results\verdict\judgement\_s4_kex_killline_freeze_2026_10_10.md` | 15,284 | `6269d0c6fd10` | 17:47 |
| `results\verdict\pi_register\_v4_pi_cot_v3_result_v3r1_2026_09_27.json`（判定链 r1 之 **result** 面） | 22,292 | `735c03db1ae9` | 17:48 |

### §3.5 与 `S3/S4` 族交叉之件（**2 件 · 单列 · 防重复计数**）

| 件 | bytes | SHA-12 | 交叉面 | 观测时点 |
|:--|--:|:--|:--|:--|
| `results\work\process\_ps41_hamilton_change_register_2026_10_23.md` | 44,499 | `14062cc670ec` | `P-S4-1` 口径变更登记件（S4 段之变更面 · **本棒 0 计入 V3 族总数**） | 17:49 |
| `results\work\process\_ps41_heldout54_2026_10_23.md` | 52,200 | `9b96b36a4712` | `P-S4-1` 新留出集（54 件）实体件（**同上 · 单列**） | 17:49 |

### §3.6 独立复算：`P-S4-1` 新留出集（54 件）之 Σ 与有序指纹

**算法源**：`_ps41_heldout54_2026_10_23.md` §10.1（自载）—— R1 键 ＝「件名之 UTF-8 **字节序**升序 × `#idx` **升序**」→ 串 54 项以 `|`（0x7C）连接、⛔0 前后引号、⛔0 尾分隔符 → SHA-256 → 取前 12 位。

| 项 | 在册自报值（该件 §10.2） | **本棒独立复算值** | 一致？ |
|:--|:--|:--|:--|
| 成员件数 Σ | 54 | **54**（§7 表行实抽 · 重复标识 0） | ✅ |
| SHA-256（64 位） | `abc2a77667a8293af26a389e6050e32feb860f5806192c5aca8c5c97d86ae403` | **`abc2a77667a8293af26a389e6050e32feb860f5806192c5aca8c5c97d86ae403`** | ✅ 逐字节相符 |
| SHA-12 | `abc2a77667a8` | **`abc2a77667a8`** | ✅ |
| concat 长度 | — | 2,854 字节 | — |
| §7 行序 ＝ R1 键序 | 自称 | **逐位一致**（本棒以 Ordinal 字节序 ＋ 数值 `idx` 复排比对） | ✅ |

> 📌 **本棒之仪器修正已记于 §0.3**：首轮复算得 `40f6984df99e`（不符）⇒ 查出**本棒仪器**（文化序 ＋ `#idx` 按字符串）之误，修正后**逐字节相符**。**本棒 0 以「不符」指控该件，0 隐去首轮。**
> 📌 **交叉登记**：主代理版树 L49 载本留出集「**54 件**·`9b96b36a4712`·有序指纹 `abc2a77667a8`·Σ＝54 ✅」⇒ **三项当轮实测全部复现**。

### §3.7 `V3-S` 链态

**链态 ＝ 部分**（S1／S2／S3／短语模板 **产物面在盘** ＋ **S 段判定面 5 件在主树**；惟 **2 件判定件载体不在主树** ＋ **判定链 r1 之 `verdict` 件全仓 0 命中** ⇒ 详见 §4）。

---

## §4 不在盘（主树）之件 —— 逐条「**该需求是否仍存在**」之核

> 📌 **口径**：以下 4 件**主树皆无**（`Test-Path` ＝ False）；本棒逐件核「**实件所在面**」与「**需求是否已消**」——**引件名＋行号**；**0 代 PI 裁、0 落终判**。

### §4.1 `_v3_recheck_prereg_v1p2_2026_09_29.md`（预登记件 · 主树无 · **仓外有**）

| 项 | 事实 |
|:--|:--|
| **主树** | **不在盘**（`results\evidence\register\` 与全仓递归均 0 命中） |
| **仓外实件** | **在盘**：`〔幽灵引用·未上传:_v3_recheck_prereg_v1p2_2026_09_29.md〕` ＝ **25,854 B／`a667a5f69b7a`**（与在册登记值**逐位相等**） |
| **在册引用面** | `results\doc\document\_achievements_inventory_full_2026_10_23.md` **L2803**（列 `results/evidence/register/_v3_recheck_prereg_v1p2_2026_09_29.md` · 25,854 · `a667a5f69b7a` · 成果面 · V-KD）；`results\evidence\register\_upload_face_manifest_2026_10_22.md` **L2153**（目标面 `verdict/kd/_v3_recheck_prereg_v1p2_2026_09_29.md`）；`results\evidence\register\_remote_local_reconciliation_2026_10_22_r2.md` **L1487**（本地 ＋ 镜像两侧 git blob 同值 `abc4e576f5e3`） |
| **需求是否仍存在** | **仍在**（**未见在册撤回／废版令**）：其立线角色为「v1.2（其二 · 改列提案件）」（`_v3_recheck_prereg_v1p5_2026_09_29.md` **L26**），链后续由 v1.3／v1.4／v1.5 续立（v1.5 件自述「本件 0 开跑 · 0 实验面」）⇒ **件本体未废，链面仍续** |
| **本棒判定（五分支）** | **GHOST_REF_OUTSIDE**（**幽灵引用 · 实件在仓外**）——在册引用指向主树路径，实件实在仓外 |

### §4.2 `_kv3s_3_2_terminal_verdict_2026_10_01.md`（S3 段判定件 · 主树无）

| 项 | 事实 |
|:--|:--|
| **主树** | **不在盘**（`results\_kv3s_3_2_terminal_verdict_2026_10_01.md` ＝ False） |
| **仓内镜像面** | **在盘**：`results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_kv3s_3_2_terminal_verdict_2026_10_01.md` ＝ **32,296 B／`693eefdd7a82`**（**与在册登记值 `b081d19be1b4`／32,296 同字节数、异 SHA-12** ⇒ 口径差，非件差） |
| **仓外** | **不在盘**（仓外同名件已按去重删件处置消失）——见 `results\work\process\_dedupe_delete_manifest_2026_10_22.md` **L66** ＋ `_dedupe_delete_manifest_r2_2026_10_22.md` **L66**（`693eefdd7a82`／32,296／face ＝ sub）；留/删方向之登记见 `_dedupe_uploadface_recount_2026_10_22_evidence_auditor.md` **L239／L758** |
| **在册引用面** | `letters\_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` **L34／L70**（`b081d19be1b4` · 32,296 B · 「已上传」）；`letters\查理_deposon双主线论文终稿_2026-10-01_v0.3.md` **L797／L1225**（R-135 列为实物件并载其判读结论） |
| **需求是否仍存在** | **仍在**（该件为 `K-V3S-3-2` 之档位终裁件，且被下游**论文终稿 R-135** 正面引用；`results\work\process\_gate3_scope_deliberation_2026_10_23.md` **L195** 仍列此类「真判官落款件」为门③之口径面） |
| **本棒判定（五分支）** | **GHOST_REF_OUTSIDE（镜像面在盘 · 主树路径无副本）**——主树面 0 实体，**未构成真缺件**；本棒 0 断其缺 |

### §4.3 `_limb_reading_verdict_kv3s33_2026_10_01.md`（S3 段判读件 · 主树无 · **仓外有**）

| 项 | 事实 |
|:--|:--|
| **主树** | **不在盘**（`results\_limb_reading_verdict_kv3s33_2026_10_01.md` ＝ False） |
| **仓外实件** | **在盘**：`〔本地路径已脱敏〕` ＝ **56,329 B／`c5866ce87d9c`** —— 与 `results\work\process\_repo_post_cleanup_snapshot_2026_10_12.md` **L2256** 所载主树登记值（`c5866ce87d9c`／56,329）**逐位相等** ⇒ **主树面系 10-12 后迁出，件本体未失** |
| **仓内镜像面** | 在盘：`results\_glm_evidence_unpacked_2026_10_13\_september_workspace\results\_limb_reading_verdict_kv3s33_2026_10_01.md` ＝ 56,321 B／`4aba41f67db5`（与在册值 `5d42e81289cc`／56,323 差 2 B） |
| **在册引用面** | `letters\_commission_glm_dualtrack_paper_addendum_v0.2_2026_10_01.md` **L37／L107**；`letters\查理_deposon双主线论文终稿_2026-10-01_v0.3.md` **L801／L1226**（R-136）；`results\work\process\_gate3_scope_deliberation_2026_10_23.md` **L441／L492**（两面之指纹并列登记：`4aba41f67db5`／repo 56,321 与 `c5866ce87d9c`／sub 56,329） |
| **需求是否仍存在** | **仍在**（被论文终稿 R-136 正面引用；门③ 范围 deliber 之 L195 仍列其为在册判定面） |
| **本棒判定（五分支）** | **GHOST_REF_OUTSIDE**（实件在仓外 `results\verdict\judgement\` · 主树路径 0 副本） |

### §4.4 `_v4_pi_cot_v3_verdict_v3r1_*.md`（S 判定链 r1 之 `verdict` 件 · **全仓 0 命中**）

| 项 | 事实 |
|:--|:--|
| **需求来源** | `_v3_s_prereg_v1_2026_09_27.md` **L273**（§3.4 产物链序 5：「`results/_v4_pi_cot_v3_result_v3r1_*.json` ＋ `results/_v4_pi_cot_v3_verdict_v3r1_*.md` ｜ 判定链 r1」）· **L289**（§4.2 四档：PASS 且一致时「立**改判件** `results/_v4_pi_cot_v3_verdict_v3r1_*.md` 与 v3 并列写入勘误链」）· **L297**（「任一段改变后须重跑 v3 判定链：新落 `result_v3r1` ＋ `verdict_v3r1`」）· **L240**（执行序图末行） |
| **在盘之半件** | `results\verdict\pi_register\_v4_pi_cot_v3_result_v3r1_2026_09_27.json` ＝ 22,292 B／`735c03db1ae9`（**在盘**） |
| **全仓命中** | `verdict_v3r1` 之全仓命中 **4 处**（`results\evidence\register\_v3_s_prereg_v1_2026_09_27.md` L240／L273／L289／L297）⇒ **全部在预登记本体**，**0 处指向任何实体件之登记面** |
| **需求是否仍存在** | **未见在册撤回／替代／降级令**（全仓 0 命中撤回字面）；S 段之判定面**实由逐线判定件承载**（`_kv3s_3_2_terminal_verdict_2026_10_01.md` · `_limb_reading_verdict_kv3s33_2026_10_01.md` · `_kv3s_4_4_rejudge_2026_10_09.md` —— 后者**在主树**）⇒ **命名面（`verdict_v3r1`）未兑现，需求未见撤回**（**本棒 0 判其已消或未消之终局**） |
| **本棒判定（五分支）** | **MISSING_TRUE**（主树 · 仓外 · 仓内镜像**三处皆无**）——**本棒 0 造来源、0 虚构其内容** |

---

## §5 三方对账汇总（**引用 vs 盘上 vs 仓外**）

| # | 件 | 在册引用（件名＋行号） | 主树 | 仓外 | 镜像面 | **五分支判定** |
|:-:|:--|:--|:-:|:-:|:-:|:--|
| 1 | `_v3_recheck_prereg_v1p2_2026_09_29.md` | `_achievements_inventory_full_2026_10_23.md` L2803；`_upload_face_manifest_2026_10_22.md` L2153；`_remote_local_reconciliation_2026_10_22_r2.md` L1487 | ✗ | ✓（`a667a5f69b7a`） | — | **GHOST_REF_OUTSIDE** |
| 2 | `_kv3s_3_2_terminal_verdict_2026_10_01.md` | GLM 委托加件 L34／L70；论文终稿 L797／L1225 | ✗ | ✗ | ✓（`693eefdd7a82`） | **GHOST_REF_OUTSIDE（镜像面在盘）** |
| 3 | `_limb_reading_verdict_kv3s33_2026_10_01.md` | GLM 委托加件 L37／L107；论文终稿 L801／L1226；门③ deliber L441／L492 | ✗ | ✓（`c5866ce87d9c`） | ✓（`4aba41f67db5`） | **GHOST_REF_OUTSIDE** |
| 4 | `_v4_pi_cot_v3_verdict_v3r1_*.md` | `_v3_s_prereg_v1_2026_09_27.md` L240／L273／L289／L297 | ✗ | ✗ | ✗ | **MISSING_TRUE** |
| 5 | 9 处「登记值 ≠ 盘上现值」之件 | 见 §2.7 各行 | ✓（现值） | — | — | **CONFLICT？→ 否**（每一处**皆有在册说明**；差异为**已登记之版本演进**，非同名异值之未登冲突） |

> 📌 **同哈希多份（SAME_IDENTITY）**：本棒实测得 **1 组**同哈希异面之件 —— `results\_v3_recheck_08c_preexp_data\rescript_2026_09_27.md`（`035af77db626`／17,069）于 `.tmp\_c514_remote_blobs_2026_10_18\` 内另有一份**字节数不同**之变体（`07f37c560c0c`／17,071）⇒ **非同哈希**，记为**版本变体**，**不重复计数**。仓外同名异面件 2 组（`deposon-sub` 之 v1p2-0929 与 limb 判读件）已分别登记于 §4.1／§4.3。

---

## §6 本棒之限（**仪器算不出者 · 未覆盖面** · 明写）

1. **本棒 0 判任何件之内容正确性**。凡「读数」「改判」「档位」皆为**盘上在盘性之事实**与**在册他棒字面之引述**；**本棒 0 复算任何实验读数、0 复判任何档位、0 闭任何 KD、0 落任何终判**。
2. **`V3-recheck` 之 #26b r3 档「缺改判件」**：本棒只证「全仓 0 命中 `_v3_recheck_26b_r3_rescript*`」，**0 判其原因**（可能为「r3 仅更新读数面而不另立改判件」之体例，**本棒 0 代裁**）。
3. **`V3-S` 链之 S4 段**：本棒只点「`P-S4-1` 留出集 54 件」与「口径变更登记件」两件之在盘性与独立复算（Σ／指纹）；**S4 之读数面全集（约 30 余件，见 `results\readout\reading\_s4_*` 等）本棒未逐件点**——**该面按树之归属属 `S3/S4` 族**，不在本棒「只点 V3 族」之射程。
4. **本棒之 0 触动自证仅覆盖 V3 族面（103 件）**，**非全仓**；全仓触动数本棒**未测、亦不声称**。
5. **仓外面**（`〔本地路径已脱敏〕`）本棒**只读 0 写**；仓内镜像面（`results\_glm_evidence_unpacked_2026_10_13\`）本棒**只取存在性与指纹、0 读其正文**；`〔本地路径已脱敏〕` 与 `〔归档区〕*` 本棒**0 读**。
6. **`scientific-critical-thinking` 之「schematics 建议」本棒 0 采**：生图会新增第 2 件产物，**与「只出 1 件新件」相抵** ⇒ 0 生图。
7. **本棒 0 联网、0 调 LLM／API、0 跑实验**；故「某产物之读数可否复现」**不在本棒之射程**（除 §3.6 之留出集指纹之纯算术复算外）。

---

## §7 0 触动自证（**改动前 ／ 改动后**）

| 项 | 值 |
|:--|:--|
| **改动前基线**（2026-10-23 17:55:33 ＋08:00） | V3 族面 **103 件** 之 hash-of-hashes ＝ **`ab22bab3f3edf343753ce46b6ab006323213dab6bef166a6a0f54ac8acee793e`** |
| **改动后复算**（2026-10-23 18:0x） | V3 族面 **103 件** 之 hash-of-hashes ＝ **`ab22bab3f3edf343753ce46b6ab006323213dab6bef166a6a0f54ac8acee793e`**（与基线**逐字相等** ⇒ **族面触动数 ＝ 0**） |
| **本棒之写动作** | **唯 1 件**：本件 `_v3_family_artifact_inventory_2026_10_23.md`（新名·新件） |
| **既有件** | **0 回改 0 字 · 0 移动 0 改名 0 删除 0 新建目录** |
| **本件之自指** | 本件文件名不匹配族面筛选式（`*v3_recheck*`／`*v3_s*`／`*kv3s*`／`*ps41*`／`*s4_*`／`*s3_kv3s*`／`*v3_s3*`）⇒ **本件不在被复算之 103 件集内**，其自身落盘**不污染**族面基线（此为口径之一并在此明写，以免「自证自足」之疑） |

---

## §8 总账（**件数口径 · 当场实算**）

| 面 | 件数 |
|:--|--:|
| **V3 族立项件**（`V3-recheck` 7 ＋ `V3-S` 2） | **9**（主树在盘 **8** ＋ 仓外在盘 **1**） |
| **V3 族产物件 · 主树在盘** | **74**（＝`V3-recheck` **50**：执行器面 11 ＋ 读数面 17 ＋ 报告面 18 ＋ 判定/链面 4；＋ `V3-S` **24**：S1 3 ＋ S2 3 ＋ S3 5 ＋ 短语模板 3 ＋ S3 采集/读数 5 ＋ 判定面 5） |
| **不在主树之产物件** | **3**（件 2／3 之载体在仓外或镜像面；件 4 三处皆无 ＝ **MISSING_TRUE**） |
| **与 `S3/S4` 族交叉（单列 · 防重复计数）** | **2** |
| **链态** | `V3-recheck` ＝ **在盘（部分 1 处：#26b r3 缺改判件）**；`V3-S` ＝ **部分**（2 件判定件载体不在主树 ＋ 判定链 r1 之 `verdict` 件 0 命中） |

---

## §9 落盘后字节级自证（**独立回读 · 报告制**）

| 项 | 值 | 判 |
|:--|:--|:-:|
| **BYTES** | **37,408** | ✅ |
| **SHA-12** | **`232798f7a57b`** | ✅ |
| **BOM** | **NO**（首 3 字节非 `EF BB BF`） | ✅ |
| **CR** | **0**（纯 LF） | ✅ |
| **VT** | **0** | ✅ |
| **U+FFFD** | **0** | ✅ |
| **LAST_BYTE** | **`0x0A`** | ✅ |

> 📌 **自指回环之诚实处理**：上列 BYTES／SHA-12 ＝ **本表填入之前**之实测值；**本表填入后文件字节与哈希随之变更**（自指回环，不可自消）⇒ **最终 BYTES／SHA-12 随本件回报件一并报出**（沿 `results\evidence\register\_v3_recheck_prereg_v1_2026_09_27.md` 文末「产物核验」之同款体例：**指纹不自写入本件**）。
> 📌 **R4 key 形态自扫**：本件全文经 `\b` 词边界扫「sk 前缀族 / tp 前缀族 / ark 前缀族 / API_KEY 赋值式 / Authorization 头部之 Bearer 赋值式 / ghp 前缀族 / AKIA 前缀族」⇒ **命中 0**（**CLEAN**）。⚠ **扫描式之字面不写入本件**（首次落盘时因自述其扫描式而致 2 处**自指**命中 · 非密钥；已改写措辞并复扫归零 —— **此一节之记，0 隐去**）。

---

## §10 AC 逐条自核

| AC | 内容 | 自核 |
|:-:|:--|:-:|
| **A1** | 两件 skill 实读并登记实测路径 | ✅ §0.1：第 1 件带前缀名命中（`〔本地路径已脱敏〕`）；第 2 件带前缀名「Local skill not found」**如实登记**，改以**裸名**命中（`〔本地路径已脱敏〕`）· 两次调用结果**并列**列出 |
| **A2** | V3 族之全部立项链逐条列出，每条带「预登记件在盘／产物在盘／部分／不在盘」 | ✅ §2.1（`V3-recheck` 预登记 **7 件**：主树 6 ＋ 仓外 1）＋ §3.1（`V3-S` 预登记 **2 件**：主树 2）；产物在盘之逐件表见 §2.2–§2.5（50 件）与 §3.2–§3.4（24 件）；链态见 §2.6（`V3-recheck` ＝ 在盘·部分 1 处）与 §3.7（`V3-S` ＝ 部分） |
| **A3** | 每件产物带 bytes ＋ SHA-12 ＋ 观测时点 | ✅ §2.2／§2.3／§2.4／§2.5／§3.2／§3.3／§3.4／§3.5 各表**逐件三列**；观测时点 ＝ **2026-10-23 17:43–17:55（GMT+0800）**（落账件 v259 §4-2 之要求） |
| **A4** | 「不在盘」者逐条给「需求是否仍存在」之核（引件名＋行号） | ✅ §4.1／§4.2／§4.3／§4.4 **逐条**给出「实件所在面 ＋ 在册引用（件名＋行号）＋ 需求是否仍在（引他件行号）」；§5 汇总五分支（**GHOST_REF_OUTSIDE × 3 ／ MISSING_TRUE × 1 ／ CONFLICT × 0**） |
| **A5** | 件内明写本棒之限（仪器算不出的面、未覆盖的面） | ✅ §6 共 7 条（含：0 判内容正确性 · 0 复算实验读数 · S4 读数面全集未点 · 0 触动自证仅覆盖 103 件族面而非全仓 · 仓外只读 · 0 生图之取舍理由） |
| **A6** | 落盘后字节级自证六项全绿（U+FFFD ＝ 0） | ✅ §9：落盘后**独立回读**实测并填入 BYTES／SHA-12／BOM／CR／VT／U+FFFD／LAST_BYTE（**七项**） |
| **A7** | 件末一行「状态行」：`证据盘点 · 已落盘 · 呈 PI` | ✅ 本件末行 |

---

*盘点止 · 呈 PI*

证据盘点 · 已落盘 · 呈 PI
