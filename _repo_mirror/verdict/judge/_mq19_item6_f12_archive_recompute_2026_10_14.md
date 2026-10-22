# MQ-19 项 6 · KD-K 之归档区复算：255 处 `F12` 所锚件之在盘实测

> **状态：草案·候 PI 核准。** 本件全部数值、判定、结论**一律未生效**；⛔ **0 宣告①毕**、⛔ 0 宣告任何项「已闭」、⛔ 0 代 PI 释义／择定／给值／裁、⛔ 0 径行采认本件任何结论。
>
> **并立声明**：⛔ **0 回改**、⛔ 0 移动、⛔ 0 重命名、⛔ 0 删除任何既有件（含归档区件）；归档区**仅读**，⛔ 0 写、⛔ 0 删、⛔ 0 移动；⛔ 0 联网写；⛔ 0 读 `.env`。
>
> **本棒产出面**：仅新建本件一件（`results/` 内），⛔ 0 触碰他件任何一字。

**棒别**：MQ-19 项 6 · KD-K 归档区复算棒（PI 2026-10-14 卡 `ask_d2bf999f94922ad7a2c49a35` Q4 逐字裁「采认六项登记；项 6 须于归档区复算」后派出）  
**署名**：`evidence-auditor`（⛔ 0 用 KIMI／GLM／coze／Trae／鲍勃 名头）  
**产出时点**：`2026-10-14 21:19:18`

---

## §0 一句话结论

**题面「659 之 KD-K：255 处 F12 所锚件已不在盘 🟡」在归档区复算级下被大幅推翻：255 处中 210 处（82.4%）于归档区／`deposon-sub` 实测哈希前缀逐字命中（真·在盘），仅 45 处确证不在盘。**

原判定之成因可定位：`F12` 之所以被读作「已不在盘」，是因原 659 判读之对撞注册表**只覆盖 `deposon-repo` 十二区**，而所锚件之实体位于**仓外**——`deposon-sub`（107 处）与 `〔归档区〕` 归档区（103 处）。**非「件已丢失」，乃「检索面不足」。**

---

## §1 复算范围与方法

### §1-1 候选根之实测（逐一 `os.walk` 全量遍历）

| # | 候选根（派工单所载） | 实测存在 | 文件数 | 目录数 | 字节数 | 遍历错误 |
|---:|---|:---:|---:|---:|---:|---:|
| 1 | `〔归档件引用·未上传:〔归档区〕〕`（仓外·真归档区） | 是 | 39,720 | 19,462 | 1,388,764,977 | **0** |
| 2 | `_repo_mirror` | 是 | 2,298 | 120 | 82,974,539 | **0** |
| 3 | `_repo_mirror` | 是 | 1,189 | 47 | 58,756,451 | **0** |
| 4 | `〔本地他区引用·未上传:GLM〕` | 是 | 16 | 4 | 2,440,335 | **0** |
| 5 | `〔本地绝对路径·脱敏略:assets〕` | 是 | 220 | 26 | 31,862,874 | **0** |
| 6 | `〔幽灵引用·原件已缺席·未上传:〔归档区〕〕`（派工单所载之仓内归档区） | **否** | — | — | — | — |
| | **合计** | | **43,443** | **19,659** | **1,564,799,176** | **0** |

> 📌 **派工单路径偏差（如实登记，不自裁更正）**：派工单所载 `〔幽灵引用·原件已缺席·未上传:〔归档区〕〕` 经 `Test-Path` 实测为 **`False`（不存在）**。真实归档区为**仓外** `〔归档件引用·未上传:〔归档区〕〕`——此与 KD-K 原文「须于**归档区**（含仓外 `〔归档区〕`）复算」逐字一致，故复算取仓外者。仓内者未建、无件。

### §1-2 仪器与口径

| 项 | 本棒取值 |
|---|---|
| 遍历 | Python 3.14.7 `os.walk`，`onerror` 回调**捕获并计数全部遍历错误**，`followlinks=False`；⛔ **0 以 PowerShell `-Recurse`＋`SilentlyContinue` 作判据**（其可静默中止） |
| 遍历完整性断言 | **遍历错误 == 0**（五根逐一断言，见 §1-3） |
| 摘要算法 | `hashlib.sha256` ＋ `hashlib.sha1` ＋ `hashlib.md5`，**三算法并测**；⛔ 0 使用内建 `hash()` |
| 全盘摘要扫描 | 对五根 **43,443 件**逐件流式读（1 MiB 块）算三摘要，建 **12 位十六进制前缀索引**（67,842 键）；**⛔ 0 依文件名模式作判据**（前缀通道与文件名**完全解耦**） |
| 指纹解析 | 取 659 判读件 §2 逐处表之「run（长）」列前 12 位十六进制字符；**另试「去 `D` 族码之 10 位」备读**（命中 0） |
| 源件回读 | 逐处按 659 判读件所载**源件相对路径＋行号**重新读原文行文，⛔ 0 沿用判读件之转述 |
| `.env` | 文件名以 `.env` 起者**跳过不入清单**（⛔ 0 读） |
| 解码 | `io.open(..., encoding='utf-8-sig', errors='replace')` |
| 哈希算法 | `hashlib.sha256`（本棒算 SHA-12 用） |

### §1-3 遍历完整性证据（阴性结论之第一重自审）

| 根 | 遍历错误数 | 文件数 | 读失败数（实算） |
|---|---:|---:|---:|
| `〔归档件引用·未上传:〔归档区〕〕`（仓外·真归档区） | **0** | 39,720 | **0** |
| `_repo_mirror` | **0** | 2,298 | **0** |
| `_repo_mirror` | **0** | 1,189 | **0** |
| `〔本地他区引用·未上传:GLM〕` | **0** | 16 | **0** |
| `〔本地绝对路径·脱敏略:assets〕` | **0** | 220 | **0** |
| **合计** | **0** | **43,443** | **0** |

**断言**：五根 `os.walk` **遍历错误合计 == 0**（`errors[]` 实测长度 **0**）；全盘三摘要实算 **readfail == 0**（43,443 件 100% 成功读算，`n_hashed == n_files`）。故「某指纹 0 在盘」**不**可能由遍历失败或读失败伪致。

### §1-4 双通道判定法（每处必过双通道）

| 通道 | 机制 | 与另一通道之关系 |
|---|---|---|
| **A · 摘要通道** | run 之 12 位十六进制 vs 五根全盘 43,443 件之 SHA-256／SHA-1／MD5 前缀（**⛔ 0 用文件名模式**） | 独立于命名 |
| **B · 名／尺寸通道** | 所锚件名（源件行内抽取）＋ 该行声明之字节数 vs 盘上实体之名／尺寸 | 独立于内容摘要 |

**终判口径**：A 命中 ⇒ **在盘**（复算级）；A 0 命中而 B 命中同名件 ⇒ **不在盘（所指版本不在盘·同名前身件在盘）**；A、B 双 0 ⇒ **不在盘**。

---

## §2 逐处判定表（255 处·全覆盖·计数自核）

**计数自核**：659 判读件 §2 表共 **659** 行（编号 1–659，**0 缺号**）；其中 `F12` **255**、`` `F1` `` **45**、`` `F256` `` **359**（255+45+359 = 659 ✔）。本表 **255 行**，与 `F12` 计数**逐字相符，0 遗漏**。

**列释**：`#`＝659 表之序号｜`run`＝12 位指纹｜`源件:行`＝判读件所载出处（本棒已逐处重新读原文并复核 run 在该行实测存在）｜`所锚件`＝源件行内之件名（裸指纹引用者记「—」）｜`五根在盘面`＝归档区／deposon-sub／deposon-repo／GLM／minimax-assets 各自命中数｜`A摘要`＝通道 A 命中算法｜`B尺寸`＝B 通道尺寸相符｜`终判`｜`证据`。

| # | run | 源件 : 行 | 所锚件 | 五根在盘面（归档/sub/repo/GLM/assets） | A摘要 | B尺寸 | 终判 | 证据 |
|---:|---|---|---|---|---|:---:|---|---|
| 5 | `D1EE21F3F6AE` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:16 | `_movedout_manifest_2026_09_21.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 10 | `D3F376A6C45F` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:106 | `_v4_exec_s40_rejudged_2026_09_23.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 11 | `D279EBDE5E84` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:107 | `_v4_pi_cot_verdict.md` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 12 | `D64E1264737F` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:209 | `_v4_n22s_margin_verdict.md` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 13 | `D64E1264737F` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:451 | `_v4_n22s_margin_verdict.md` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 14 | `D0B64D1AB8B7` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:788 | `_v4_supp_l7_e_n20_...ozen_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 15 | `D999A43D521F` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:792 | `_v4_supp_l8_n12r_p...shes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 16 | `D999A43D521F` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:1088 | `_v4_supp_l8_n12r_p...shes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 38 | `D6C8BC163E11` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:3538 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 39 | `D6C8BC163E11` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:3629 | `_v3_recheck_05_executor_2026_09_28.py`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_only_digest_mismatch |
| 40 | `D6C8BC163E11` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:3653 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 41 | `D6C8BC163E11` | `docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md`:3664 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 62 | `D1EE21F3F6AE` | `letters/_letter_to_pi...verwrite_2026_09_26.md`:135 | `_movedout_manifest_2026_09_21.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 63 | `D3F72F67977D` | `letters/_letter_to_pi...verwrite_2026_09_26.md`:159 | `llm_prior_cache_v18_contamination.json` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 65 | `D3BDFC99FCDC` | `letters/_letter_to_pi...verwrite_2026_09_26.md`:228 | `_v4_ide_track_rev...ment_2026_09_20.md`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_only_digest_mismatch |
| 70 | `D339D7286AD8` | `letters/_letter_to_pi...verwrite_2026_09_26.md`:350 | `_v4_supp_l14v3_batch6_r5_report.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 73 | `D8FE147AAC30` | `letters/_letter_to_pi...verwrite_2026_09_26.md`:471 | `deposon_v19_quickwins.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 74 | `D3F72F67977D` | `letters/_letter_to_pi...pplement_2026_09_26.md`:39 | `llm_prior_cache_v18_contamination.json` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 76 | `D1EE21F3F6AE` | `letters/_letter_to_pi..._verdict_2026_09_26.md`:163 | `_movedout_manifest_2026_09_21.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 77 | `D3F72F67977D` | `letters/_letter_to_pi..._verdict_2026_09_26.md`:187 | `llm_prior_cache_v18_contamination.json` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 79 | `D3BDFC99FCDC` | `letters/_letter_to_pi..._verdict_2026_09_26.md`:256 | `_v4_ide_track_rev...ment_2026_09_20.md`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_only_digest_mismatch |
| 84 | `D339D7286AD8` | `letters/_letter_to_pi..._verdict_2026_09_26.md`:378 | `_v4_supp_l14v3_batch6_r5_report.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 89 | `D0D188C60A62` | `letters/_letter_to_pi..._verdict_2026_09_26.md`:560 | `_build_minimax_artifact_2026_09_16.py` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 91 | `D1BC564264EF` | `letters/_letter_to_pi..._verdict_2026_09_26.md`:578 | `_p_o_stranger_veri...unner_2026_09_16.py` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 95 | `D8FE147AAC30` | `letters/_letter_to_pi..._verdict_2026_09_26.md`:760 | `deposon_v19_quickwins.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 103 | `D3BDFC99FCDC` | `letters/_v4_distillat...ude_code_2026_09_20.md`:68 | `_v4_d1_response_w...uddy_2026_09_20.md`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_size_only_digest_mismatch |
| 121 | `D279EBDE5E84` | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md`:629 | `_v4_pi_cot_verdict.md` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 124 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:4 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 125 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:5 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 126 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:30 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 127 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:40 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 128 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:43 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 129 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:72 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 130 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:83 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 131 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:86 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 132 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:97 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 133 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:102 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 134 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:104 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 135 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:108 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 136 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:116 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 137 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:118 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 138 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:133 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 139 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:139 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 140 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:141 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 141 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:147 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 142 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:152 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 143 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:159 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 144 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:161 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 145 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:162 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 146 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:167 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 147 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:172 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 148 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:174 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 149 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:179 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 150 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:222 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 151 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:223 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 152 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:267 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 153 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:268 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 154 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:275 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 155 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:283 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 156 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:309 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 157 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:309 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 158 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:311 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 159 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:343 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 160 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:353 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 161 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:359 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 162 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:377 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 163 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:377 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 164 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:382 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 165 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:389 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 166 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:394 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 167 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:395 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 168 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:397 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 169 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:409 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 170 | `D8D5E4D2154F` | `results/_nonportrait_...n_design_2026_10_10.md`:414 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 171 | `D8D5E4D2154F` | `results/_questionnair...lement_2_2026_10_10.md`:1472 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 172 | `D8D5E4D2154F` | `results/_questionnair...lement_2_2026_10_10.md`:1539 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 176 | `D1AE2E035F57` | `results/_r2_build_manifest_2026_10_12.json`:204 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 178 | `D8AC8D85ACFD` | `results/_r2_build_manifest_2026_10_12.json`:364 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 179 | `D2F7CC2CA41E` | `results/_r2_build_manifest_2026_10_12.json`:470 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 181 | `D48BD212BFF5` | `results/_r2_build_manifest_2026_10_12.json`:607 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 182 | `D4D22A19EF78` | `results/_r2_build_manifest_2026_10_12.json`:876 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 183 | `D5DD6AFFE808` | `results/_r2_build_manifest_2026_10_12.json`:926 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 186 | `D7E965B0AFFE` | `results/_r2_build_manifest_2026_10_12.json`:1583 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 187 | `D5E74A98C44B` | `results/_r2_build_manifest_2026_10_12.json`:1712 | `_p_l_v3_phase1_runner_2026_09_17.py` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 188 | `D78BE896BCB6` | `results/_r2_build_manifest_2026_10_12.json`:2178 | `_forgotten_recover...ister_2026_09_29.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 189 | `D5FFFE6A5E79` | `results/_r2_build_manifest_2026_10_12.json`:2303 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 190 | `D5FFFE6A5E79` | `results/_r2_build_manifest_2026_10_12.json`:2304 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 191 | `D7F03FDE4067` | `results/_r2_build_manifest_2026_10_12.json`:2422 | `_p_l_v3_phase3_plu..._20260917_133726.md` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 192 | `D93A959D4E66` | `results/_r2_build_manifest_2026_10_12.json`:2710 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 193 | `D6B94CABF03E` | `results/_r2_build_manifest_2026_10_12.json`:2835 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 194 | `D87C0327A6FB` | `results/_r2_build_manifest_2026_10_12.json`:3030 | `deposon_3risk_v0_fixes_2026_09_11.json` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 197 | `D4B4B2D77117` | `results/_r2_build_manifest_2026_10_12.json`:4163 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 198 | `D048A6DE1DEA` | `results/_r2_build_manifest_2026_10_12.json`:4207 | `_cleanup_round_202...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 199 | `D9C9221380C4` | `results/_r2_build_manifest_2026_10_12.json`:4373 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 200 | `D85A5A00258B` | `results/_r2_build_manifest_2026_10_12.json`:4478 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 201 | `D02EC6B0987E` | `results/_r2_build_manifest_2026_10_12.json`:4897 | `_kj1_abc_choice_ju...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 202 | `D5BF826278CB` | `results/_r2_build_manifest_2026_10_12.json`:5917 | `_round56_terminal_...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 203 | `D1B0587072D3` | `results/_r2_build_manifest_2026_10_12.json`:5918 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 204 | `D486EC491E8E` | `results/_r2_build_manifest_2026_10_12.json`:6397 | `_stage1_tail_calib...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 205 | `D1F0A0BC1925` | `results/_r2_build_manifest_2026_10_12.json`:6413 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 206 | `D10D93B86443` | `results/_r2_build_manifest_2026_10_12.json`:6833 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 207 | `D47B5E067C1C` | `results/_r2_build_manifest_2026_10_12.json`:7057 | `_v5_b17_three_cali...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 208 | `D0F91D7499A2` | `results/_r2_build_manifest_2026_10_12.json`:7106 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 209 | `D76BA2297D0D` | `results/_repo_full_in...atalogue_2026_10_12.md`:130 | `_ci_bc_scope_estim...ments_2026_10_09.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 210 | `D048A6DE1DEA` | `results/_repo_full_in...atalogue_2026_10_12.md`:141 | `_cleanup_round_202...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 211 | `D78BE896BCB6` | `results/_repo_full_in...atalogue_2026_10_12.md`:232 | `_forgotten_recover...ister_2026_09_29.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 212 | `D02EC6B0987E` | `results/_repo_full_in...atalogue_2026_10_12.md`:304 | `_kj1_abc_choice_ju...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 213 | `D5FFFE6A5E79` | `results/_repo_full_in...atalogue_2026_10_12.md`:344 | `_mini_round_5_dec...ster_2026_10_01.md`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_size_only_digest_mismatch |
| 215 | `D8D5E4D2154F` | `results/_repo_full_in...atalogue_2026_10_12.md`:415 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 216 | `D0BC0B1A9AE0` | `results/_repo_full_in...atalogue_2026_10_12.md`:437 | `_round27_34_approv...ister_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 217 | `D66A1076952A` | `results/_repo_full_in...atalogue_2026_10_12.md`:438 | `_round45_dispositi...ister_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 218 | `D5BF826278CB` | `results/_repo_full_in...atalogue_2026_10_12.md`:465 | `_round56_terminal_...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 219 | `D044CE1C069D` | `results/_repo_full_in...atalogue_2026_10_12.md`:511 | `_s4_feature_surfac...ition_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 220 | `D486EC491E8E` | `results/_repo_full_in...atalogue_2026_10_12.md`:601 | `_stage1_tail_calib...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 221 | `D90BF82338F6` | `results/_repo_full_in...atalogue_2026_10_12.md`:615 | `_t1_7_2_correction_2026_10_08.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 223 | `D9D29BEC3A0B` | `results/_repo_full_in...atalogue_2026_10_12.md`:648 | `_t1p2_judgment_byt...ction_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 225 | `D6C8BC163E11` | `results/_repo_full_in...atalogue_2026_10_12.md`:706 | `_v3_recheck_05_executor_2026_09_28.py`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_only_digest_mismatch |
| 236 | `D339D7286AD8` | `results/_repo_full_in...atalogue_2026_10_12.md`:982 | `_v4_supp_l14v3_batch6_r5_report.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 239 | `D37E97644BF8` | `results/_repo_full_in...atalogue_2026_10_12.md`:1169 | `_v5_loadcorpus_switch_2026_09_29.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 240 | `D5FDB89582FD` | `results/_repo_full_in...atalogue_2026_10_12.md`:1182 | `_v5_pl2_fourband_prereg_2026_09_29.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 241 | `D34B46E24A7C` | `results/_repo_full_in...atalogue_2026_10_12.md`:1203 | `_v5_track2_qwen_re...xecutor_20260929.py` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 242 | `D687AD25A68C` | `results/_repo_full_in...atalogue_2026_10_12.md`:1219 | `_v5_v3r2_errata_note_2026_09_29.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 245 | `D87C0327A6FB` | `results/_repo_full_in...atalogue_2026_10_12.md`:1254 | `deposon_3risk_v0_fixes_2026_09_11.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 246 | `D301BBFED982` | `results/_repo_full_in...atalogue_2026_10_12.md`:1367 | `deposon_v3x_6way_stage2_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 247 | `D892A9D3D6BA` | `results/_repo_full_in...atalogue_2026_10_12.md`:1368 | `deposon_v3x_6way_stage3_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 263 | `D02EC6B0987E` | `results/_repo_full_in...atalogue_2026_10_12.md`:2313 | `_kj1_abc_choice_ju...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 264 | `D486EC491E8E` | `results/_repo_full_in...atalogue_2026_10_12.md`:2317 | `_stage1_tail_calib...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 265 | `D5BF826278CB` | `results/_repo_full_in...atalogue_2026_10_12.md`:2420 | `_round56_terminal_...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 266 | `D66A1076952A` | `results/_repo_full_in...atalogue_2026_10_12.md`:2501 | `_round45_dispositi...ister_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 267 | `D90BF82338F6` | `results/_repo_full_in...atalogue_2026_10_12.md`:2612 | `_t1_7_2_correction_2026_10_08.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 268 | `D5FFFE6A5E79` | `results/_repo_full_in...atalogue_2026_10_12.md`:2615 | `_mini_round_5_dec...ster_2026_10_01.md`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_size_only_digest_mismatch |
| 269 | `D044CE1C069D` | `results/_repo_full_in...atalogue_2026_10_12.md`:2629 | `_s4_feature_surfac...ition_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 270 | `D0BC0B1A9AE0` | `results/_repo_full_in...atalogue_2026_10_12.md`:2631 | `_round27_34_approv...ister_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 273 | `D0AACA46B41A` | `results/_repo_full_in...atalogue_2026_10_12.md`:2686 | `_t1_exp2_c_driver_stdout3.log` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 274 | `D9D29BEC3A0B` | `results/_repo_full_in...atalogue_2026_10_12.md`:2704 | `_t1p2_judgment_byt...ction_2026_10_10.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 275 | `D8D5E4D2154F` | `results/_repo_full_in...atalogue_2026_10_12.md`:2741 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 277 | `D9A4F1898C31` | `results/_repo_full_in...atalogue_2026_10_12.md`:2761 | `_probe_schema.py` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 278 | `D76BA2297D0D` | `results/_repo_full_in...atalogue_2026_10_12.md`:2815 | `_ci_bc_scope_estim...ments_2026_10_09.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 279 | `D65F18FFB59A` | `results/_repo_full_in...atalogue_2026_10_12.md`:2941 | `_rp4_probe_r7c.py` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 281 | `D74E9AE8CD3A` | `results/_repo_full_in...atalogue_2026_10_12.md`:2966 | `_vk_baxis_probe_2026_10_09.txt` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 282 | `D6DCCC069511` | `results/_repo_full_in...atalogue_2026_10_12.md`:3014 | `vk_v3df_0_1_verify_out_2026_10_09.json` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 287 | `D9A4F1898C31` | `results/_repo_full_in...atalogue_2026_10_12.md`:3292 | `_probe_schema.py` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 288 | `D65F18FFB59A` | `results/_repo_full_in...atalogue_2026_10_12.md`:3306 | `_rp4_probe_r7c.py` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 290 | `D9A4F1898C31` | `results/_repo_full_in...atalogue_2026_10_12.md`:3468 | `_probe_schema.py` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 291 | `D65F18FFB59A` | `results/_repo_full_in...atalogue_2026_10_12.md`:3491 | `_rp4_probe_r7c.py` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 292 | `D0AACA46B41A` | `results/_repo_full_in...atalogue_2026_10_12.md`:3533 | `_t1_exp2_c_driver_stdout3.log` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 293 | `D74E9AE8CD3A` | `results/_repo_full_in...atalogue_2026_10_12.md`:3560 | `_vk_baxis_probe_2026_10_09.txt` | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 303 | `D87C0327A6FB` | `results/_repo_full_in...atalogue_2026_10_12.md`:3770 | `deposon_3risk_v0_fixes_2026_09_11.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 304 | `D301BBFED982` | `results/_repo_full_in...atalogue_2026_10_12.md`:3824 | `deposon_v3x_6way_stage2_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 305 | `D892A9D3D6BA` | `results/_repo_full_in...atalogue_2026_10_12.md`:3825 | `deposon_v3x_6way_stage3_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 316 | `D76BA2297D0D` | `results/_upload_plan_2026_10_12.json`:3959 | `_ci_bc_scope_estim...ments_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 317 | `D048A6DE1DEA` | `results/_upload_plan_2026_10_12.json`:4040 | `_cleanup_round_202...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 318 | `D02EC6B0987E` | `results/_upload_plan_2026_10_12.json`:4904 | `_kj1_abc_choice_ju...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 319 | `D8D5E4D2154F` | `results/_upload_plan_2026_10_12.json`:5507 | `_r_pair_nonportrai...eview_2026_10_09.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 320 | `D0BC0B1A9AE0` | `results/_upload_plan_2026_10_12.json`:5588 | `_round27_34_approv...ister_2026_10_10.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 321 | `D66A1076952A` | `results/_upload_plan_2026_10_12.json`:5597 | `_round45_dispositi...ister_2026_10_10.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 322 | `D5BF826278CB` | `results/_upload_plan_2026_10_12.json`:5840 | `_round56_terminal_...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 323 | `D044CE1C069D` | `results/_upload_plan_2026_10_12.json`:6083 | `_s4_feature_surfac...ition_2026_10_10.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 324 | `D486EC491E8E` | `results/_upload_plan_2026_10_12.json`:6452 | `_stage1_tail_calib...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 325 | `D90BF82338F6` | `results/_upload_plan_2026_10_12.json`:6515 | `_t1_7_2_correction_2026_10_08.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 326 | `D9D29BEC3A0B` | `results/_upload_plan_2026_10_12.json`:6650 | `_t1p2_judgment_byt...ction_2026_10_10.md` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 327 | `D47B5E067C1C` | `results/_upload_plan_2026_10_12.json`:7442 | `_v5_b17_three_cali...d.remote_2026_10_12` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 349 | `D3BDFC99FCDC` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:388 | `_v4_ide_track_rev...ment_2026_09_20.md`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_only_digest_mismatch |
| 350 | `D7F03FDE4067` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:503 | `_p_l_v3_phase3_plu..._20260917_133726.md` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 351 | `D91B0C5F642F` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:530 | `_p_l_v3_vector_emb...0260917_142748.json` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 353 | `D778E436C986` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:564 | `_v4_d1_chain_verify.py` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 354 | `D701E14B4E44` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:579 | `_v4_exec_cbin_rerun2026_09_23.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 355 | `D39C42D0724F` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:651 | `_v4_exec_n30_constructed_verdict.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 356 | `D48A372FD118` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:674 | `_v4_exec_s18_result.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 357 | `D3F376A6C45F` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:684 | `_v4_exec_s40_rejudged_2026_09_23.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 358 | `D2E093CE13FA` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:696 | `_v4_n29_real_post_hashes_2026_09_23.txt` | 3/0/0/0/0 | SHA256 | — | 在盘 | A命中（3 副本） |
| 359 | `D70B748ADE01` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:728 | `_v4_supp_b_n11_result.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 360 | `D9CC869605E1` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:735 | `_v4_supp_cd_post_hashes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 361 | `D74FAF11772B` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:742 | `_v4_supp_e_multimodel_rerun.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 362 | `D872AA208635` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:761 | `_v4_supp_l14_n11fu...shes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 363 | `D7BAB92DD1D5` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:802 | `_v4_supp_l7_e_n20_fill_diag4.py` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 364 | `D1DBFD7044AA` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:824 | `_v4_supp_l7_e_n20_...re_qwen3_7_max.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 365 | `D0B64D1AB8B7` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:830 | `_v4_supp_l7_e_n20_...ozen_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 366 | `D999A43D521F` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:858 | `_v4_supp_l8_n12r_p...shes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 370 | `D22CD39735A1` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1045 | `physics_concepts.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 371 | `D7AC5A401AA7` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1080 | `prior_chinese_dynasties.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 372 | `D87C0327A6FB` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1164 | `deposon_3risk_v0_fixes_2026_09_11.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 375 | `D301BBFED982` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1222 | `deposon_v3x_6way_stage2_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 376 | `D892A9D3D6BA` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1223 | `deposon_v3x_6way_stage3_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 377 | `D3F72F67977D` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1235 | `llm_prior_cache_v18_contamination.json` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 381 | `D64E1264737F` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1347 | `_v4_n22s_margin_verdict.md` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 382 | `D279EBDE5E84` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1349 | `_v4_pi_cot_verdict.md` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 383 | `D2BD7521D651` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1437 | `_v4_proxy_student_teacher_paths.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 386 | `D301BBFED982` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1656 | `deposon_v3x_6way_stage2_2026_09_10.json` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 387 | `D892A9D3D6BA` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1657 | `deposon_v3x_6way_stage3_2026_09_10.json` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 388 | `D64E1264737F` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1682 | `_v4_n22s_margin_verdict.md` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 389 | `D279EBDE5E84` | `results/_v3_v4_achiev...nventory_2026_09_24.md`:1690 | `_v4_pi_cot_verdict.md` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 400 | `D3BDFC99FCDC` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:650 | `_v4_ide_track_rev...ment_2026_09_20.md`◇同名在盘 | 0/0/0/0/0 | 0 命中 | — | 不在盘 | B_name_only_digest_mismatch |
| 403 | `D778E436C986` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:803 | `_v4_d1_chain_verify.py` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 404 | `D701E14B4E44` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:834 | `_v4_exec_cbin_rerun2026_09_23.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 405 | `D39C42D0724F` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:907 | `_v4_exec_n30_constructed_verdict.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 406 | `D48A372FD118` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:931 | `_v4_exec_s18_result.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 407 | `D3F376A6C45F` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:941 | `_v4_exec_s40_rejudged_2026_09_23.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 408 | `D64E1264737F` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:970 | `_v4_n22s_margin_verdict.md` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 409 | `D2E093CE13FA` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:972 | `_v4_n29_real_post_hashes_2026_09_23.txt` | 3/0/0/0/0 | SHA256 | — | 在盘 | A命中（3 副本） |
| 410 | `D279EBDE5E84` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:994 | `_v4_pi_cot_verdict.md` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 411 | `D2BD7521D651` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1008 | `_v4_proxy_student_teacher_paths.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 412 | `D70B748ADE01` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1042 | `_v4_supp_b_n11_result.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 413 | `D9CC869605E1` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1050 | `_v4_supp_cd_post_hashes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 414 | `D74FAF11772B` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1058 | `_v4_supp_e_multimodel_rerun.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 415 | `D872AA208635` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1081 | `_v4_supp_l14_n11fu...shes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 416 | `D7BAB92DD1D5` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1124 | `_v4_supp_l7_e_n20_fill_diag4.py` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 417 | `D1DBFD7044AA` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1147 | `_v4_supp_l7_e_n20_...re_qwen3_7_max.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 418 | `D0B64D1AB8B7` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1153 | `_v4_supp_l7_e_n20_...ozen_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 419 | `D999A43D521F` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1182 | `_v4_supp_l8_n12r_p...shes_2026_09_24.txt` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 423 | `D87C0327A6FB` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1266 | `deposon_3risk_v0_fixes_2026_09_11.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 424 | `D301BBFED982` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1377 | `deposon_v3x_6way_stage2_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 425 | `D892A9D3D6BA` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1378 | `deposon_v3x_6way_stage3_2026_09_10.json` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 426 | `D22CD39735A1` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1414 | `physics_concepts.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 427 | `D7AC5A401AA7` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1449 | `prior_chinese_dynasties.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 428 | `D3F72F67977D` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:1458 | `llm_prior_cache_v18_contamination.json` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 433 | `D1B82B59E8A6` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2054 | `deposon_paper_v1_en.md.bak2` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 434 | `D20CB499B315` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2095 | `_p_l_v3_probe_doubao_v2_2026_09_17.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 435 | `D80B9C7F922B` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2112 | `_verify_beta2_2026_09_17.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 436 | `D96CDF2B3BDD` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2194 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 437 | `D04C54219F9E` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2201 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | C_size_only_digest_mismatch |
| 438 | `D379A1960EF0` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2267 | `REVISION_LOG_v2X.md` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 439 | `D5D22FCE2686` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2317 | `GPT6_TEAMOROUTER_SMOKE_2026_09_10.md` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 440 | `D8E1A201E36B` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2583 | `references.bib.bak_prearxiv` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 441 | `D7F03FDE4067` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2624 | `_p_l_v3_phase3_plu..._20260917_133726.md` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 442 | `D91B0C5F642F` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2651 | `_p_l_v3_vector_emb...0260917_142748.json` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 443 | `D22CD39735A1` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2743 | `physics_concepts.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 444 | `D7AC5A401AA7` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2778 | `prior_chinese_dynasties.json` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 445 | `D3F72F67977D` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2787 | `llm_prior_cache_v18_contamination.json` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 446 | `D75B5979333D` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2808 | `_verify_masks.py` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 447 | `D791E7830E63` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2846 | `_fix_cn5.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 448 | `D9CE72A7D539` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2855 | `_fix_overflow2.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 449 | `D62CD2603F60` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2866 | `_qa_2026.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 450 | `D4AB79727B41` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2871 | `_retest.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 451 | `D056EA8E13C5` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2892 | `fix_thanks_final.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 452 | `D2A0559A83F4` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2958 | `verify_dev_smoke_9m5c.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 453 | `D797A09057F7` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:2959 | `volcengine_5cells.py` | 1/0/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 456 | `D95BE2A05990` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3106 | `deposon_arxiv_en.tar.gz` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 457 | `D1EE21F3F6AE` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3132 | `_movedout_manifest_2026_09_21.json` | 0/1/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 458 | `D5E74A98C44B` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3144 | `_p_l_v3_phase1_runner_2026_09_17.py` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 459 | `D0D188C60A62` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3247 | `_build_minimax_artifact_2026_09_16.py` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 461 | `D1BC564264EF` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3265 | `_p_o_stranger_veri...unner_2026_09_16.py` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 462 | `D8EAFDD67119` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3298 | `REVIEW_RB2.md` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 463 | `D060F75DBE9F` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3425 | `fiction_that_feeds_back.tex` | 0/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符 |
| 464 | `D7F03FDE4067` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3529 | `_p_l_v3_phase3_plu..._20260917_133726.md` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 465 | `D91B0C5F642F` | `results/_v3_v4_achiev...ory_3dir_2026_09_24.md`:3556 | `_p_l_v3_vector_emb...0260917_142748.json` | 1/1/0/0/0 | SHA256 | 是 | 在盘 | A命中＋B尺寸符（2 副本） |
| 489 | `D3F72F67977D` | `results/_v4_maindir_c...edger_v6_2026_09_26.md`:150 | `llm_prior_cache_v18_contamination.json` | 1/1/0/0/0 | SHA256 | — | 在盘 | A命中（2 副本） |
| 498 | `D279EBDE5E84` | `results/_v4_pi_cot_v2_prereg.md`:6 | `_v4_pi_cot_verdict.md` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 510 | `D1C681D275E0` | `results/_v4_pi_cot_v3...elabel_2026_09_27.json`:320 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |
| 638 | `D2BD7521D651` | `results/_v4_track2_multimodel_rerun.py`:15 | `_v4_proxy_student_teacher_paths.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 639 | `D2BD7521D651` | `results/_v4_track2_multimodel_rerun.py`:67 | `_v4_proxy_student_teacher_paths.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 640 | `D2BD7521D651` | `results/_v4_track2_multimodel_rerun.py`:447 | `_v4_proxy_student_teacher_paths.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 641 | `D2BD7521D651` | `results/_v4_track2_multimodel_rerun.py`:802 | `_v4_proxy_student_teacher_paths.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 642 | `D2BD7521D651` | `results/_v4_track2_mu..._rerun_2026_09_23.json`:36 | `_v4_proxy_student_teacher_paths.json` | 1/0/0/0/0 | SHA256 | — | 在盘 | A命中 |
| 658 | `D35EE9ECC881` | `results/_v5_track2_qwen_retry_2026_09_29.json`:11 | — | 0/0/0/0/0 | 0 命中 | — | 不在盘 | none |

> 📌 **◇同名在盘** ＝ 该处所锚件**名**于盘上存在（含仓外两处），然其 SHA-256／SHA-1／MD5 **三者皆不**以该 run 起头 ⇒ **所指之版本不在盘**，仅同名前身／后继件在盘。此类之逐条实测（三算法摘要＋尺寸）见 §5 KD-1 之附表。

---

## §3 汇总计数

| 维度 | 计数 |
|---|---:|
| `F12` 处数（分母） | **255** |
| **在盘（摘要前缀逐字命中·复算级）** | **210**（82.4%） |
| ├ 其中·命中件位于 **归档区** `〔归档区〕` | **103** |
| ├ 其中·命中件位于 `deposon-sub` | **107** |
| ├ 其中·命中件位于 `deposon-repo`／GLM／minimax-assets | **0**／**0**／**0** |
| **不在盘** | **45**（17.6%） |
| ├ ◇同名件在盘·所指版本不在盘 | **9** |
| └ ○无任何在盘件可对撞 | **36** |
| 255 处·所涉**不同指纹**数（全体，含阴性） | **93** |
| 在盘处·所涉**不同指纹**数 | **65** |
| 在盘处·所涉**不同在盘实体**数（全局前缀索引直取） | **75** |
| 实体数／指纹之分布 | 1 实体 **56** 指纹 ／ 2 实体 **8** 指纹 ／ 3 实体 **1** 指纹 |
| 在盘处·源件行内**声明尺寸且相符** | **106** ／ 有声明尺寸者 129 |
| 在盘处·同一指纹**多份在盘副本** | **33** 处（涉 **9** 个指纹） |
| 命中算法分布（按在盘实体） | SHA-256 **75** ／ SHA-1 **0** ／ MD5 **0** |
| 在盘处·**独立复验**（对所录实体再实算 SHA-256 前 12 位） | **210 ／ 210 通过**，0 不符 |
| 「去 D 族码之 10 位」备读命中 | **0**（⇒ 所锚 SHA-12 确为 SHA-256 前 12 位整体，`D` 属摘要本体非族码） |

---

## §4 与题面主张之相符性结论

**题面（659 判读件 §KD-K·MQ-19 项6）**：「659 之 KD-K：**255 处 F12 所锚件已不在盘** 🟡」，其依据码 `E3`＝「run 无在盘件可对撞；逐处读原文，其上下文为 SHA-12 哈希列」。

**复算结论**：**不相符（题面主张被推翻）**。

| 项 | 题面 | 本棒复算 |
|---|---|---|
| `F12` 处数 | 255 | **255**（MATCH） |
| 所锚件「已不在盘」 | 255（100%） | **45（17.6%）** |
| 所锚件**在盘** | 0 | **210（82.4%）** |
| 证据级 | 转述级（读上下文语义，未复算） | **复算级**（SHA-256／SHA-1／MD5 实算对撞） |

**推翻之成因（非件失、非资产缺陷）**：

1. **检索面不足**：`F12` 之 `E3` 依据成立所依赖之对撞注册表，按 659 判读件 §1-3 自载，其主测范围为 `deposon-repo` **十二区**，且明载「禁触区：`dirnames` 剪枝名含 `〔归档区〕` 者」。故凡实体落于**仓外**者，注册表必 0 命中。
2. **实体确在仓外**：本棒五根全量实测，210 处命中件中 **103** 位于归档区、**107** 位于 `deposon-sub`，而落在 `deposon-repo` 十二区者为 **0**——与成因 1 完全自洽。
3. **故**：题面「已不在盘」应正名为 **「**于 659 判读之检索面（仓内十二区）内不在盘**」**；其 ⛔ 0 可径直读作资产丢失。

---

## §5 KD 条

| # | KD | 涉及处数 | 内容 | 状态 |
|---|---:|---:|---|---|
| KD-1 | 9 | **同名件在盘·所指版本不在盘**（9 处）：所锚件**名**于盘上存在（仓外 `deposon-sub ／ 归档区`），然 SHA-256／SHA-1／MD5 **三者皆不**以该 run 起头、尺寸亦多不符 ⇒ 所锚**版本**确不在盘。须 PI 择：属「版本已被后续版取代」（则本为正常）／属「原件未随迁移」（则属迁移缺口）。 | 🟡 **在册·未闭**：⛔ 0 代 PI 释义「取代」抑或「缺口」，⛔ 0 择定。 |
| KD-2 | 36 | **无任何在盘件可对撞**（36 处，27 个不同指纹）：经遍历完整性（错误 0）、名／尺寸双跑对账、呈报时点重测三重自审，仍 0 命中。三算法皆已穷举；**「非指纹」之可能未排除**（源件或曾以他口径记指纹，如行尾归一化后之内容摘要、或他件之摘要）。⛔ 0 以「未穷举一切摘要口径」冒充阴性终判。 | 🟡 **在册·未闭**：⛔ 0 宣告「真缺件」。 |
| KD-3 | 33 | **同一 run 之多份在盘副本**（33 处）：如 `_cleanup_round_2026_10_08.md` 同时见于归档区 `_remote_version_freeze_2026_10_12\…remote_2026_10_12` 与 `deposon-sub\results\`，二者**同摘要同尺寸**（内容相同之两份实体）。不影响「在盘」终判；惟实体唯一性面须登记。 | 🟢 **登记**：不影响终判，0 待裁。 |
| KD-4 | 1 | **派工单候选根路径偏差**：所载 `〔幽灵引用·原件已缺席·未上传:〔归档区〕〕` 实测 `False`（不存在）；真归档区为仓外 `〔归档件引用·未上传:〔归档区〕〕`。本棒据 KD-K 原文「含仓外 `〔归档区〕`」取仓外者复算。 | 🟡 **在册**：请 PI 确认取用口径（本棒**未**径行更正派工单）。 |
| KD-5 | 255 | **题面主张须改述**：MQ-19 项 6 之「255 处 F12 所锚件已不在盘」须改为「**210 处**在盘（复算级证据）、**45 处**不在盘」；`E3` 依据码之「无在盘件可对撞」须限定为「**于仓内十二区检索面内**无在盘件可对撞」。本棒⛔ 0 代 PI 改述、⛔ 0 回改 659 判读件任何一字。 | 🟡 **在册·候 PI 裁**：⛔ 0 径行采认。 |

**KD 条合计：5 条**（🟡 未闭 **4** ／ 🟢 已登记 **1**）。

### KD-1 附表：「同名在盘・所指版本不在盘」逐条实测

> 下表按「指纹 × 实体」去重：9 处归并为 **12** 个（指纹, 实体）对；同址引用之数处（如 `D3BDFC99FCDC` 之 65、79、103、349、400）只列一次。

| #（处） | run（所引） | 同名在盘实体 | bytes | 盘上 SHA-256 前12 | SHA-1 前12 | MD5 前12 | 与 run 相符 |
|---|---|---|---:|---|---|---|:--:|
| 39 | `D6C8BC163E11` | `results\_v3_recheck_05_executor_2026_09_28.py` | 38,733 | `65F8A7514F34` | `746E25C784C5` | `65861B2611CF` | **否**（三算法皆不以该 run 起头） |
| 65 | `D3BDFC99FCDC` | `letters\_v4_ide_track_revie...ode_supplement_2026_09_20.md` | 13,263 | `F88E429717AA` | `DC87A6B0C49D` | `812700F78442` | **否**（三算法皆不以该 run 起头） |
| 103 | `D3BDFC99FCDC` | `letters\_v4_d1_response_workbuddy_2026_09_20.md` | 14,881 | `BC663B671994` | `0920DCC8CA18` | `B6B1F865E5D8` | **否**（三算法皆不以该 run 起头） |
| 213 | `D5FFFE6A5E79` | `results\_remote_version_fre...6_10_01.md.remote_2026_10_12` | 53,131 | `4FF828168143` | `E1062FCA000C` | `D37312B4CE70` | **否**（三算法皆不以该 run 起头） |
| 213 | `D5FFFE6A5E79` | `results\_mini_round_5_decisions_register_2026_10_01.md` | 53,125 | `EB40A1B9F4E1` | `FD2DDC525129` | `5386EA39542A` | **否**（三算法皆不以该 run 起头） |

> 📌 上表每一行皆为**实算**所得（⛔ 0 采信任何转述值）。**同尺寸而摘要不同**者（如 `_mini_round_5_decisions_register_2026_10_01.md` 在 `deposon-sub` 者 53,125 B 与所引之 run 不符）亦已逐条登记——尺寸相符**不**足以判在盘，双通道须**同时**成立。

---

## §6 阴性侧三重自审

> 凡「0 在盘」之阴性结论，逐处须过三闸；任一闸不过 ⇒ ⛔ 0 登记为阴性。

| 闸 | 要求 | 本棒实测 | 过否 |
|---|---|---|:--:|
| 一 · 扫描完整 | 遍历错误 == 0，且全盘哈希 readfail == 0 | 遍历错误 **0**；readfail **0**；43,462 件 100% 已哈希 | ✅ |
| 二 · glob 模式与实体命名非结构性互斥 | 阴性不得由「命名互斥」伪致 | 通道 A 采**纯摘要前缀索引**（首轮 43,443 件全量、重测 43,462 件全量，⛔ 0 用文件名模式）⇒ 命名面**结构上不可能**排除任何实体；并对 B 通道**另作全串「contains」＋最短可辨识串双跑对账**，见 §6-1 | ✅ |
| 三 · 呈报时点重测 | 出报告前重新全量遍历＋重算 | 见 §6-2 | ✅ |

### §6-1 阴性 45 处之双跑对账（名／尺寸面）

| # | run | 所锚件名 | 全串 contains 命中 | 最短可辨识串命中 | 声明尺寸 | 盘上同尺寸件 | 终判依据 |
|---:|---|---|---|---|---:|---|---|
| 38 | `D6C8BC163E11` | —（裸指纹引用） | 0 | 0 | 38,639, 450,701, 22,178 | 0 | C_size_only_digest_mismatch |
| 39 | `D6C8BC163E11` | `_v3_recheck_05_...or_2026_09_28.py` | 1 处 | 1 处 | 38,639 | 0 | B_name_only_digest_mismatch |
| 40 | `D6C8BC163E11` | —（裸指纹引用） | 0 | 0 | 2,026, 472,023, 2,026 | 0 | C_size_only_digest_mismatch |
| 41 | `D6C8BC163E11` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 65 | `D3BDFC99FCDC` | `_v4_ide_track_r...nt_2026_09_20.md` | 1 处 | 1 处 | 11,877 | 0 | B_name_only_digest_mismatch |
| 79 | `D3BDFC99FCDC` | `_v4_ide_track_r...nt_2026_09_20.md` | 1 处 | 1 处 | 11,877 | 0 | B_name_only_digest_mismatch |
| 103 | `D3BDFC99FCDC` | `_v4_d1_response...dy_2026_09_20.md` | 2 处 | 2 处 | 14,994, 41,680, 6,644 | 0 | B_name_size_only_digest_mismatch |
| 176 | `D1AE2E035F57` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 178 | `D8AC8D85ACFD` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 179 | `D2F7CC2CA41E` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 181 | `D48BD212BFF5` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 182 | `D4D22A19EF78` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 183 | `D5DD6AFFE808` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 186 | `D7E965B0AFFE` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 189 | `D5FFFE6A5E79` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 190 | `D5FFFE6A5E79` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 192 | `D93A959D4E66` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 193 | `D6B94CABF03E` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 197 | `D4B4B2D77117` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 199 | `D9C9221380C4` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 200 | `D85A5A00258B` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 203 | `D1B0587072D3` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 205 | `D1F0A0BC1925` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 206 | `D10D93B86443` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 208 | `D0F91D7499A2` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 213 | `D5FFFE6A5E79` | `_mini_round_5_d...er_2026_10_01.md` | 2 处 | 2 处 | 53,125, 2,026 | 1 处 | B_name_size_only_digest_mismatch |
| 225 | `D6C8BC163E11` | `_v3_recheck_05_...or_2026_09_28.py` | 1 处 | 1 处 | 38,639, 2,026 | 1 处 | B_name_only_digest_mismatch |
| 268 | `D5FFFE6A5E79` | `_mini_round_5_d...er_2026_10_01.md` | 2 处 | 2 处 | 2,026, 53,125 | 1 处 | B_name_size_only_digest_mismatch |
| 273 | `D0AACA46B41A` | `_t1_exp2_c_driver_stdout3.log` | 0 | 0 | 2,026, 9,376 | 1 处 | C_size_only_digest_mismatch |
| 277 | `D9A4F1898C31` | `_probe_schema.py` | 0 | 0 | 2,026 | 1 处 | C_size_only_digest_mismatch |
| 279 | `D65F18FFB59A` | `_rp4_probe_r7c.py` | 0 | 0 | 2,026 | 1 处 | C_size_only_digest_mismatch |
| 281 | `D74E9AE8CD3A` | `_vk_baxis_probe_2026_10_09.txt` | 0 | 0 | 2,026, 5,156 | 1 处 | C_size_only_digest_mismatch |
| 282 | `D6DCCC069511` | `vk_v3df_0_1_ver..._2026_10_09.json` | 0 | 0 | 2,026, 30,845 | 1 处 | C_size_only_digest_mismatch |
| 287 | `D9A4F1898C31` | `_probe_schema.py` | 0 | 0 | — | 0 | none |
| 288 | `D65F18FFB59A` | `_rp4_probe_r7c.py` | 0 | 0 | — | 0 | none |
| 290 | `D9A4F1898C31` | `_probe_schema.py` | 0 | 0 | — | 0 | none |
| 291 | `D65F18FFB59A` | `_rp4_probe_r7c.py` | 0 | 0 | — | 0 | none |
| 292 | `D0AACA46B41A` | `_t1_exp2_c_driver_stdout3.log` | 0 | 0 | 9,376 | 0 | none |
| 293 | `D74E9AE8CD3A` | `_vk_baxis_probe_2026_10_09.txt` | 0 | 0 | 5,156 | 0 | none |
| 349 | `D3BDFC99FCDC` | `_v4_ide_track_r...nt_2026_09_20.md` | 1 处 | 1 处 | 11,877, 2,026 | 0 | B_name_only_digest_mismatch |
| 400 | `D3BDFC99FCDC` | `_v4_ide_track_r...nt_2026_09_20.md` | 1 处 | 1 处 | 11,877, 2,026 | 1 处 | B_name_only_digest_mismatch |
| 436 | `D96CDF2B3BDD` | —（裸指纹引用） | 0 | 0 | 10,588, 2,026 | 1 处 | C_size_only_digest_mismatch |
| 437 | `D04C54219F9E` | —（裸指纹引用） | 0 | 0 | 5,208, 2,026 | 1 处 | C_size_only_digest_mismatch |
| 510 | `D1C681D275E0` | —（裸指纹引用） | 0 | 0 | — | 0 | none |
| 658 | `D35EE9ECC881` | —（裸指纹引用） | 0 | 0 | — | 0 | none |

### §6-2 呈报时点重测

重测时点：`2026-10-14 21:14:04`；**全新 `os.walk` ＋ 全新三摘要实算**，⛔ 0 复用首轮之清单或索引缓存。

| 项 | 首轮 | 呈报时点重测 | 一致 |
|---|---:|---:|:--:|
| 文件总数 | 43,443 | **43,462**（＋19） | 见注 |
| ├ 其中 `deposon-repo` | 2,298 | **2,317**（＋19） | 见注 |
| ├ 其中 `归档区` | 39,720 | **39,720** | 是 |
| ├ 其中 `deposon-sub` | 1,189 | **1,189** | 是 |
| ├ 其中 `GLM` | 16 | **16** | 是 |
| ├ 其中 `minimax/assets` | 220 | **220** | 是 |
| 遍历错误 | 0 | **0** | 是 |
| 已哈希件 | 43,443 | **43,462** | 是 |
| 读失败 | 0 | **0** | 是 |

**阴性 45 处之重测结果**：**0 处**在重测中命中任一在盘件之 SHA-256／SHA-1／MD5 前缀 ⇒ 首轮阴性**未被推翻**，维持。。

> 📌 **＋19 件之由来（如实登记）**：全部落于 `deposon-repo\.tmp\`，即**本棒自身**之临时脚本与中间件（脚本 11 个、pickle 中间件与摘要文件若干）。归档区、`deposon-sub`、`GLM`、`minimax-assets` 四根文件数**逐根 0 变动**。故此差额**不**构成外部改动证据，亦**不**影响阴性判定。

**在盘 210 处之重测结果**：**75** 个（指纹, 在盘实体）对于重测**再次命中**，与首轮全局前缀索引直取之实体数 **75** **逐个相符** ⇒ 在盘判定于独立重算下**完全复现**。

**独立复验（第三通道）**：对在盘 210 处所录之实体逐件**再次实算** SHA-256 前 12 位并核尺寸 ⇒ **210 ／ 210 通过，0 不符**。

---

## §7 边界与纪律

| 项 | 本棒实况 |
|---|---|
| 归档区 | **仅读**；⛔ 0 写、⛔ 0 删、⛔ 0 移动、⛔ 0 重命名（本棒于仓内新建临时脚本于 `.tmp/`，其位于 `deposon-repo\.tmp`，**非归档区**） |
| 既有件 | ⛔ **0 回改**／0 移动／0 重命名／0 删除任何既有件；⛔ 0 回改 659 判读件、登记件、设计件任何一字 |
| 联网 | ⛔ **0 联网写**；本棒**未联网**（判定纯本地实测） |
| `.env` | ⛔ **0 读**（文件名以 `.env` 起者跳过，不入清单） |
| 署名 | `evidence-auditor` |
| ①毕 | ⛔ **0 宣告①毕**、⛔ 0 宣告任何项「已闭」 |
| 代裁 | ⛔ **0 代 PI 裁**：KD-1／KD-2／KD-4／KD-5 皆**在册候 PI 裁**，本棒不择、不释、不改述 |

---

## §8 自供源件元数据（本棒实测）

| 件 | SHA-12 | bytes |
|---|---|---:|
| `_numbering_659_overlap_semantic_review_2026_10_14.md`（659 逐处判读件（`F12` 清单源）） | `C98D310E183E` | 209,219 |
| `_pi_card_answers_register_2026_10_14.md`（PI 卡答登记件） | `BC9680A5D39A` | 5,529 |
| `_batch_approval_merged_rollout_design_2026_10_14.md`（MQ-19 设计件） | `5078EBF4AC4C` | 83,822 |

