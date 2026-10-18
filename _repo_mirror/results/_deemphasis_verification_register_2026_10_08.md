# 〔W老师〕淡化执行·独立核验登记件（N-6 改口径：独立核验＋残余收口）

- 核验日：2026-10-08（CST）｜核验方：evidence-auditor（证据链审计官）｜署名如实：本件为独立核验方出证，非执行方
- 裁定依据：PI 2026-10-08 卡 `ask_8eb9cafebdcf0394137c178e` 第 4 题＝「独立核验＋残余收口」
- 核验对象：GitHub 公开仓 `zeroandcat/Deposon`（main），commit `72c5839`
- 参考件：`鲍勃_操作清单_〔W老师〕淡化执行_2026-10-06.md`（执行方 2026-10-06 清单，全文已读）
- 纪律：只读远端｜⛔ 0 远端写｜⛔ 0 回改既有件｜⛔ 0 代裁（§6 只给证据指针）｜0 编造｜R4 永不明文（0 读 key／0 读 .env）

---

## 1. 方法与口径

### 1.1 远端取态方法（如实登记）
| 项 | 实测值 |
|---|---|
| 取态途径 | GitHub archive tarball（只读 HTTP GET）：`https://github.com/zeroandcat/Deposon/archive/72c58394764d1f22ca4cc8eeb846c0d775d7cbc6.tar.gz` |
| 下载结果 | **成功**（未需改用其它途径） |
| tarball 字节 | 21,488,236 B |
| tarball SHA-256 | `E13547D8908BDCE8A2A7DE8E57B5B56592B5DBB6F8539A249F609B5EC2B1BA1E` |
| 解包位置 | `%TEMP%\deposon_n6_audit\ex\Deposon-72c58394764d1f22ca4cc8eeb846c0d775d7cbc6`（⛔ 0 落盘仓内） |
| 解包树规模 | 2,221 文件 / 164 目录 |

### 1.2 commit 链核验（GitHub API 只读，`/repos/zeroandcat/Deposon/commits?sha=main`）
- 远端 HEAD ＝ `72c5839`（＝目标 commit）✅
- 自基线 `6908cac` 起的 8 连提交链 **逐个对位一致**，顺序与主题与清单 §一表全等：

| 序 | commit | UTC 时间 | 主题（截） | 对位 |
|---|---|---|---|---|
| 1 | `fed9a87` | 2026-10-06T14:11:49Z | B1 root machine-readable mentor dossier | ✅ |
| 2 | `429c065` | 14:13:08Z | B2 september workspace facade README | ✅ |
| 3 | `5bd6676` | 14:13:35Z | B3 C4 chain judgment texts | ✅ |
| 4 | `dacb5f7` | 14:29:39Z | B4 letter-family archive texts | ✅ |
| 5 | `5658f6a` | 14:36:22Z | B5 filename-level renames + path-anchor propagation | ✅ |
| 6 | `afd39a5` | 14:39:25Z | B6a V3X specs & drafts (47 files) | ✅ |
| 7 | `75cfae8` | 14:43:10Z | B6b results chain/artifacts/ledgers (88 files) | ✅ |
| 8 | `72c5839` | 14:46:29Z | B6c remainder union incl. main-tree docs (50 files) | ✅ |

- 基线 `6908cac`（2026-10-01T13:04:09Z，`override: ... Q1 甲`）为 `fed9a87` 之直接父提交 ✅；链型为纯追加，0 改写痕迹 ✅（清单 §一 R2 声明与实测一致）

### 1.3 残差复算口径（自审仪器）
- **分 token 复算**，逐 token 独立计次，**未使用全局 `-w`**（该选项对中文邻接形失效，见清单 §二批⑥「枚举口径勘误」条）。
- 分词口径：中文 token（〔W老师〕/〔当事人W〕/〔IM〕/〔高校R〕/〔机构G〕/〔高校R〕）＝字面子串计次；拉丁 token（〔IM〕/〔高校R〕/〔高校R〕/〔机构G〕）＝`\b` 词边界＋忽略大小写。
- 「全仓」＝解包树全量 2,221 文件；「净化域」＝全仓排除 8 件 `_deemphasis_sha_drift_register_*` 登记件（注：清单 §三称 7 个登记件为**台账注记**来源；实测盘上 B1/B2/B3/B4/B5/B6a/B6b/B6c **共 8 件**，见 §7 边界 B-1）。
- 计次单位：出现次数（occurrence），非命中文件数。
- 二进制件（PDF）不参与文本复算，列为报备面（见 §7 边界 B-2）。

### 1.4 哈希工具
一律 `Get-FileHash -Algorithm SHA256`（stdlib 级），未使用内建 `hash()`；全值对拍。

---

## 2. 对拍表：残差复算 vs 清单 §三 期望值

| token | 全仓·期望 | 全仓·实测 | 全仓·判定 | 净化域·期望 | 净化域·实测 | 净化域·判定 |
|---|---|---|---|---|---|---|
| 〔W老师〕 | 12 | **12** | 一致 | 0 | **0** | 一致 |
| 〔当事人W〕 | 15 | **15** | 一致 | 1 | **1** | 一致 |
| 〔IM〕 | 8 | **8** | 一致 | 0 | **0** | 一致 |
| 〔IM〕（-i） | 61 | **61** | 一致 | 12 | **12** | 一致 |
| 〔高校R〕 | 8 | **8** | 一致 | 0 | **0** | 一致 |
| 〔机构G〕 | 9 | **9** | 一致 | 0 | **0** | 一致 |
| 〔高校R〕 | 7 | **7** | 一致 | (1+1)=2 | **2** | 一致 |
| 〔高校R〕（-w） | 6 | **6** | 一致 | 1 | **1** | 一致 |
| 〔高校R〕（-i） | 14 | **14** | 一致 | 6 | **6** | 一致 |
| 〔机构G〕（-i） | 3 | **3** | 一致 | 0 | **0** | 一致 |

**逐项 10/10 一致，0 差异。** 未作任何对齐性修饰（实测数即登记数）。

### 2.1 净化域残差逐处落点（复算证据，残差上下文按脱敏边界截断 ≤60 字符）

| token | 件 · 行 | 落点性质（依清单 §四.3 判定链保护面归类） |
|---|---|---|
| 〔当事人W〕 | `_september_workspace/.trae/audit/compare_versions.py:129` | 判定检查串 `'〔当事人W〕' in text`（R1 判定读数域） |
| 〔IM〕 ×12 | `_september_workspace/results/*.json` ×11 件 + `_september_workspace/results/_pc_d1_d3_2026_09_15.py` ×1 件 | JSON 判定键 `no_*_〔IM〕API` 族（R1 判定读数域） |
| 〔高校R〕 ① | `paper/deposon_paper_v1.md:5` | PI 自身单位行（清单 §三标注＝§2 排除项） |
| 〔高校R〕 ② | `compare_versions.py:128` | 判定检查串 `'中国〔高校R〕' in text`（R1 域） |
| 〔高校R〕 | `compare_versions.py:160` | 打印标签 `袁祺皓/〔高校R〕 chem`（R1 读数域） |
| 〔高校R〕 ×6 | `paper/deposon_paper_v1_en.md:3`（1）、`_september_workspace/.trae/scripts/_md_to_tex.py:784,794`（2）、`compare_versions.py:128`（1，`〔高校R〕 University` 子串）、`_september_workspace/results/_glm_five_items_suggestion_table_2026_10_01.md:49,154`（2，PI 按 H8 定存疑面） | LaTeX/元数据引用面＋存疑面＋判定串 |
| 〔IM〕 / 〔高校R〕 / 〔机构G〕 / 〔机构G〕 | 净化域 0 命中 | 真实残留已清零 |

**读数**：净化域 6 类非零残差全部落在清单 §四.3 已声明的 R1 判定链保护面或 §2 排除项（PI 自有单位行）与 PI 存疑面，**0 例外**。此项与清单 §三结论「净化域人名/机构/渠道字面已清零或收敛至报备保留面」相符。

### 2.2 全仓 12/15/8/61… 的构成（自洽性验证）
全仓非零值 ＝ 净化域残差 ＋ 8 件登记件自身台账注记。以「〔W老师〕」为例：全仓 12 处**全部**落在 5 件登记件内（B4=2、B5=4、B6a=1、B6b=1、B6c=4），净化域 0 —— 构成自洽，非漏计。

---

## 3. 改名核（清单 §二批⑤ 10 件表）

### 3.1 逐件：旧路径 0 存在 ＋ 新路径存在

| # | 旧路径（清单口径） | 旧路径存在 | 新路径存在 | 判定 |
|---|---|---|---|---|
| 1 | `docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` | **否** | `_september_workspace/docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md` | ✅ |
| 2 | `docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` | **否** | `_september_workspace/docs/V3X/D7_EXTERNAL_ADVISOR_ONLINE_PUSH_REQUIREMENTS_2026_09_18.md` | ✅ |
| 3 | `…/_archive_2026_09_20/LETTER_TO_WANG_TEACHER_2026_09_18_FINAL.md` | **否** | `_september_workspace/results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | ✅ |
| 4 | `…/_archive_2026_09_20/_coze_〔IM〕_v3_d7format_2026_09_18.pdf` | **否** | `_september_workspace/results/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | ✅ |
| 5 | `…/_archive_2026_09_20/_letter_to_coze_〔IM〕_v2_2026_09_18.md` | **否** | `_september_workspace/results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | ✅ |
| 6 | `results/_coze_〔IM〕_v3_2026_09_18.md` | **否** | `_september_workspace/results/_coze_online_v3_2026_09_18.md` | ✅ |
| 7 | `results/_coze_〔IM〕_v3_d7format_2026_09_18.md` | **否** | `_september_workspace/results/_coze_online_v3_d7format_2026_09_18.md` | ✅ |
| 8 | `results/_coze_〔IM〕_v3_final_2026_09_18.md` | **否** | `_september_workspace/results/_coze_online_v3_final_2026_09_18.md` | ✅ |
| 9 | `results/_coze_〔IM〕_v4_d7format_2026_09_26.pdf` | **否** | `_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf` | ✅ |
| 10 | `results/_d7_wang_teacher_〔IM〕_publish_v1_20260918.md` | **否** | `_september_workspace/results/_d7_external_advisor_online_publish_v1_20260918.md` | ✅ |

**10/10 成立。** 清单 §二批⑤ 路径列以 `results/` 为基准书写，实盘位于 `_september_workspace/results/`（与 B5 登记件表 1 书写口径一致），非改名失败。

### 3.2 全树文件名残余扫描（防漏）
- 扫描解包树 2,221 件文件名，匹配 `(?i)(wang|〔IM〕)`：**命中 0 件**。
- 即：文件名级无任何 wang/〔IM〕 残留，清单 §七第 6 项所述「仓内文件名级残余风险」在 HEAD 态**未发现实体残留件**。
- 补充：远端 `letters/` 目录存在但仅 2 件（无 wang/〔IM〕 命名件）。

---

## 4. 漂移登记件抽验（post SHA-256 全值对拍）

### 4.1 登记件清单（实测 `_september_workspace/results/` 下，共 8 件）

| 件名 | 字节 |
|---|---|
| `_deemphasis_sha_drift_register_B1_2026_10_06.md` | 1,206 |
| `_deemphasis_sha_drift_register_B2_2026_10_06.md` | 1,418 |
| `_deemphasis_sha_drift_register_B3_2026_10_06.md` | 2,830 |
| `_deemphasis_sha_drift_register_B4_2026_10_06.md` | 11,715 |
| `_deemphasis_sha_drift_register_B5_2026_10_06.md` | 14,237 |
| `_deemphasis_sha_drift_register_B6a_2026_10_06.md` | 11,696 |
| `_deemphasis_sha_drift_register_B6b_2026_10_06.md` | 22,219 |
| `_deemphasis_sha_drift_register_B6c_2026_10_06.md` | 14,351 |

各批登记行数（解析实测）：B1=1、B2=1、B3=3、B4=15（SHA-12 缩写＋全值附录 A 格式，解析器按全值列 0 命中，属格式差异非缺件）、B5=47、B6a=47、B6b=88、B6c=50。

### 4.2 抽验结果（29 件，跨 B1/B2/B3/B4/B5/B6a/B6b/B6c，post 全值＝解包件实测）

| 批 | 件（相对远端根） | post SHA-256（前 12） | 判定 |
|---|---|---|---|
| B1 | `handoff_machine_readable.json` | `d5179de00915` | MATCH |
| B2 | `_september_workspace/README_V4_2026_09_29.md` | `9d4252898087` | MATCH |
| B3 | `_september_workspace/results/_c4_theory_source_caliber_correction_2026_09_30.md` | `356b341cc0d5` | MATCH |
| B3 | `_september_workspace/results/_theory_input_request_supplement_2026_09_29.md` | `20c4979626b2` | MATCH（B5 post，见 4.3） |
| B3 | `_september_workspace/results/_v5_theory_input_acquisition_request_2026_09_29.md` | `315e1fc71b5e` | MATCH |
| B4#1 | `…/results/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | `dc3e56adc3fc` | MATCH（B5 post，见 4.3） |
| B4#2 | `…/results/_archive_2026_09_20/LETTER_TO_TRAE_2026_09_11.md` | `b09251018102` | MATCH |
| B4#3 | `…/results/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | `ff37f39264bc` | MATCH（B5 post，见 4.3） |
| B4#4 | `…/results/_archive_2026_09_20/_letter_to_coze_paper_v1_委托_2026_09_17.md` | `f4610b0bb47c` | MATCH |
| B4#5 | `…/results/_archive_2026_09_20/_letter_to_trae_code_2026_09_17_final.md` | `b75ba5c152b7` | MATCH |
| B4#6 | `…/results/_archive_2026_09_20/_letter_to_kimi_upload_requirements_2026_09_18.md` | `8b22a026f30b` | MATCH（B5 post，见 4.3） |
| B4#7 | `…/results/_archive_2026_09_20/LETTER_TO_KIMI_GITHUB_UPLOAD_2026_09_18.md` | `00e5d185ef74` | MATCH |
| B4#8 | `…/results/_archive_2026_09_20/LETTER_TO_KIMI_PUSH_V3_委托_2026_09_17.md` | `05f92d837412` | MATCH |
| B4#9 | `_september_workspace/results/_external_letters_two_generation_values_note_2026_10_01.md` | `503543d46a95` | MATCH |
| B4#10 | `_september_workspace/docs/V3X/LETTER_FROM_TRAE_2026_09_11.md` | `0c1028b9500a` | MATCH |
| B5#1 | `_september_workspace/docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md` | `b3e00ba108a1` | MATCH |
| B5#2 | `_september_workspace/docs/V3X/D7_EXTERNAL_ADVISOR_ONLINE_PUSH_REQUIREMENTS_2026_09_18.md` | `244b76b690f0` | MATCH |
| B5#3 | `…/_archive_2026_09_20/LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | `ff37f39264bc` | MATCH |
| B5#4 | `…/_archive_2026_09_20/_coze_online_v3_d7format_2026_09_18.pdf` | `adc99e04ac53` | MATCH（rename only，pre＝post） |
| B5#5 | `…/_archive_2026_09_20/_letter_to_coze_online_v2_2026_09_18.md` | `dc3e56adc3fc` | MATCH |
| B5#6 | `_september_workspace/results/_coze_online_v3_2026_09_18.md` | `53c9c1ab2d12` | MATCH |
| B5#7 | `_september_workspace/results/_coze_online_v3_d7format_2026_09_18.md` | `debe3761c565` | MATCH |
| B5#8 | `_september_workspace/results/_coze_online_v3_final_2026_09_18.md` | `36439bc12bba` | MATCH |
| B5#9 | `_september_workspace/results/_coze_online_v4_d7format_2026_09_26.pdf` | `a82881653520` | MATCH（rename only，pre＝post） |
| B5#10 | `_september_workspace/results/_d7_external_advisor_online_publish_v1_20260918.md` | `788fbdd8c12f` | MATCH |
| B5t2 | `…/results/_archive_2026_09_20/_audit_secret_2026_09_20_anchor_guard.py` | `780a8adae5e8` | MATCH |
| B5t2 | `…/results/_archive_manifest_deposon_sub_2026_09_23.json` | `0cc79ff91a12` | MATCH |
| B5t2 | `results/_trae_d7_v1_audit_20260917_190000.md` | `41c142eab4a1` | MATCH |
| B6a | `_september_workspace/docs/V3X/AGENT_TEAM_OPT_V2_2026_09_11.md` | `56457880d656` | MATCH |
| B6a | `_september_workspace/docs/V3X/BOSS_PE_3_RESERVOIR_VERIFY_REPORT_2026_09_15.md` | `37600b667c3c` | MATCH |
| B6a | `_september_workspace/docs/V3X/V3X_D6_PAPER_zh.md` | `49f9463ae3e6` | MATCH（B6a post，见 4.3） |
| B6b | `_september_workspace/results/_archive_2026_09_18/_trae_5audit_aggregated_2026_09_17.md` | `4063f9a1882c` | MATCH |
| B6b | `_september_workspace/results/_archive_2026_09_18/_trae_code_improvement_v2_2026_09_18.md` | `cd56db6ad62a` | MATCH |
| B6c | `_september_workspace/.tmp/_audit_part3_out.txt` | `448098227c2a` | MATCH |
| B6c | `_september_workspace/.tmp/_audit_part4.txt` | `c1f48194bc26` | MATCH |

**抽验合计 34 件次，MATCH 34/34，真 MISMATCH 0。**（首轮曾出现 2 处标记 MISMATCH，经逐条追链后确认均为**批间链式中间态**，非终态不符 —— 见 4.3。）

### 4.3 批间链式终态追核（3+1 件，闭合验证）

核验方首轮按「单一批次登记 post」比对时，下列件出现表观不符；逐条追链后确认 **实测值＝该件最后一次被改批次的 post**，链式闭合：

| 件 | 链（pre → 中间 → 终态） | 终态实测 | 终态登记位置 |
|---|---|---|---|
| `V3X_D6_PAPER_zh.md` | `feae8af2`（pre）→ `f806c2d9`（B5 post）→ `49f9463a`（**终态**） | `49f9463ae3e6278fff7e2a24fb4bb5da167c246d8f68e667aea60f0f6864f2ab` | B6a 登记件 L62（批⑥a「B-3 回写补充 1 处 L211」） |
| `_theory_input_request_supplement_2026_09_29.md` | `d225c608`（pre）→ `cd2f23b3`（B3 post）→ `20c49796`（**终态**） | `20c4979626b249d1254f94af4ddbf981c5d982b5daf8ac383ca6263059b35e5a` | B5 登记件表 2（路径锚回写） |
| `_letter_to_coze_online_v2_2026_09_18.md` | `ecdbf3a7`（pre）→ `b32cd6da`（B4 post）→ `dc3e56ad`（**终态**） | `dc3e56adc3fc7be642a8feb25b365dfced7cbebc29bc868a3b408de8e6205444` | B5 登记件表 1 #5 |
| `LETTER_TO_EXTERNAL_ADVISOR_2026_09_18_FINAL.md` | `7d4b5dd9`（pre）→ `643d636f`（B4 post）→ `ff37f392`（**终态**） | `ff37f39264bc059e6216166979547c4dc97524e3e5e0fe30f91d71a6ccf5897d` | B5 登记件表 1 #3 |
| `_letter_to_kimi_upload_requirements_2026_09_18.md` | `…`（pre）→ `00545612`（B4 post）→ `8b22a026`（**终态**） | `8b22a026f30b430734b742ebfe0b786076398979475ad94236437a6983419eb3` | B5 登记件表 2 |

**核验要点（入册）**：同一件被多批先后改动时，**任一非末批登记件的 post 值均为中间态**，与 HEAD 终态必然不等。此为「登记值可能落后于盘上终态」族的**结构性表现**，非执行方登记错误。验收比对时须按「末批登记件」取值。本核验已按此口径复算，34 件次全等。

**pre 值边界**：本核验侧为 tarball 只读解包，**无 pre 态实体**。所有 pre 值仅作登记转录（清单/登记件原文），**未作实测复算**，不宣称其已验证。

### 4.4 mtime 时序旁证
`V3X_D6_PAPER_zh.md` 与 `_theory_input_request_supplement_2026_09_29.md` 的 mtime 均为 `2026-10-06 22:46:29`（＝72c5839 提交时刻 CST），与其终态归属 B6 批次一致，时序自洽。

---

## 5. 本地↔远端对照（防复发）

### 5.1 口径声明
- 扫描面：本地 `D:\私人资料\deposon-repo`（主区）与 `D:\私人资料\deposon-sub`（副区）递归全量，**文本类扩展名白名单**（`.md/.json/.py/.tsv/.txt/.yaml/.yml/.csv/.html/.js/.tex/.bib`），**未启用额外忽略规则**（任务书所述「默认忽略规则」＝ PowerShell 默认隐藏/系统件过滤；本核验已用 `-Force` 展开隐藏件，故口径较宽）。
- 命中判据：文件全文**含「〔W老师〕」三字**（逐字节 Unicode 匹配），计**文件数**。
- 对位规则：本地 `X` → 远端 `X`（同路径）／远端 `_september_workspace/X`（目录前缀归一）／改名映射表（§3.1）三路。

### 5.2 本地实测命中数

| 区 | 实测命中文件数 | 任务书预期 | 差 |
|---|---|---|---|
| `deposon-repo` | **111** | ~110 | +1（口径含 `.tmp/` 件，见 5.4） |
| `deposon-sub` | **46** | ~46 | 0 ✅ |

### 5.3 三分类（deposon-repo 111 件）

| 类 | 件数 | 说明 |
|---|---|---|
| ① 远端有对应 | **95** | PREFIX 92（本地无 `_september_workspace/` 前缀，远端有）＋ SAME 1 ＋ RENAME 2 |
| ② 远端无对应 | **0** | 无 |
| ③ 未判定 | **16** | 见 5.4 全列 |

其中 RENAME 类 2 件（＝本地仍持旧名、远端已改名，**重传即复发**）：
- 本地 `docs/V3X/D3_〔IM〕_MIDTERM_TEMPLATE.md` → 远端 `_september_workspace/docs/V3X/D3_ONLINE_MIDTERM_TEMPLATE.md`
- 本地 `docs/V3X/D7_WANG_TEACHER_〔IM〕_PUSH_REQUIREMENTS_2026_09_18.md` → 远端 `_september_workspace/docs/V3X/D7_EXTERNAL_ADVISOR_ONLINE_PUSH_REQUIREMENTS_2026_09_18.md`

### 5.4 ③ 未判定 16 件全列

| # | 本地相对路径 | 复核结论 |
|---|---|---|
| 1 | `.tmp/claude_spotcheck.py` | 远端无同名件 |
| 2 | `.tmp/recheck2.py` | 远端无同名件 |
| 3 | `docs/V3X/V7_§3_P_C_P_E_GRAY_NOTE_2026_09_11.md` | 远端无同名件 |
| 4 | `letters/_c4_theory_scan_reply_claude_code_2026_09_30.md` | 远端无同名件 |
| 5 | `letters/_commission_codex_theory_derivation_EN_2026_09_30.md` | 远端无同名件 |
| 6 | `letters/_commission_codex_theory_derivation_EN_v0.2_2026_09_30.md` | 远端无同名件 |
| 7 | `letters/_commission_glm_theory_derivation_2026_09_30.md` | 远端无同名件 |
| 8 | `letters/_v3_calibration_change_note_for_coze_glm_2026_09_27.md` | 远端无同名件 |
| 9 | `letters/_v4_distillation_acceptance_coze_2026_09_20.md` | 远端无同名件 |
| 10 | `letters/_walkthrough_bugfix_audit_reply_trae_code_2026_09_30.md` | 远端无同名件 |
| 11 | `letters/LETTER_FROM_TRAE_2026_09_11.md` | **远端有同名件**，但位于 `_september_workspace/docs/V3X/LETTER_FROM_TRAE_2026_09_11.md`（桶位不同，非改名）→ 归① |
| 12 | `letters/LETTER_FROM_TRAE_REVIEW_2026_09_16.md` | 远端无同名件 |
| 13 | `letters/TRAE_FIX_REQUEST_3RISKS_2026_09_11.md` | 远端无同名件 |
| 14 | `letters/TRAE_WALKTHROUGH_BUGFIX_AUDIT_REQUEST_2026_09_30.md` | 远端无同名件 |
| 15 | `letters/查理_deposon双主线论文终稿_2026-10-01_v0.3.md` | 远端无同名件 |
| 16 | `results/_refcheck_hash_change_reference_recheck_2026_09_30.md` | 远端无同名件 |

修正归并后：③ 实为 **15 件远端无对应** ＋ 1 件桶位不同（归①），② 类（远端无对应且已确认）＝ 15。

### 5.5 副区 `deposon-sub` 对照边界
- 命中 46 件。**未对 sub→远端做逐件路径对位**，因 sub 为仓外副区、其路径基准与远端仓不同构（远端无 `deposon-sub/` 前缀实体），强行按相对路径对位会产生系统性假「无对应」。
- 状态：**未验面**（见 §7 边界 B-3），如实登记，不作推断。

### 5.6 复发风险实证（防复发登记）
本地 `deposon-repo` 仍存 **111 件含「〔W老师〕」字面**，与远端净化域 0 形成**完全反向差**。含义：本地未随远端淡化同步，一旦自本地重传/上传，**字面将全量回流**。此项与既有记忆条目「公开仓淡化后本地未同步（0 回改）→ 上传防复发」一致，本核验为该风险的**独立复现实证**（计数级：111 vs 0）。
- 本核验 ⛔ 0 触碰本地件，未作任何同步/改名/替换（超出只读核验授权范围，且 PI 未就此下裁）。

---

## 6. 清单 §七「6 项待裁」逐项现状指针（⛔ 0 裁决建议，仅引证据位置）

| §七项 | 主题 | 现状指针（HEAD `72c5839` 实测） | 裁决 |
|---|---|---|---|
| 1 | `THINKING_V3_GT_CONTRIB_2026.md` L58-59 履历表外信息 | 本核验**未单独复算该件**（不在 §2 残差 10 token 复算面内，其字面为机构/职位类非本 10 token）；该件在远端存在性与内容未验 → **未验面**，见 B-4 | ⛔ 0 裁决 |
| 2 | `no_*_〔IM〕API` 判定键 ×12＋compare_versions.py 判定检查串 | **实测成立且数量吻合**：〔IM〕 净化域 12 处（＝`no_*_〔IM〕API` 族）；`compare_versions.py:128`（`has_ruc_chem` 检查串）与 `:129`（`mentions_external_mentor` 检查串）均在位。证据：§2、§2.1 | ⛔ 0 裁决 |
| 3 | LaTeX/元数据「School of Chemistry and Life Resources, 〔高校R〕 University of China」×4＋`_glm_five_items` 存疑 ×2 | **实测成立且数量吻合**：〔高校R〕 净化域 6 处 ＝ `_md_to_tex.py:784,794`（2）＋ `deposon_paper_v1_en.md:3`（1）＋ `compare_versions.py:128`（1）＋ `_glm_five_items_suggestion_table_2026_10_01.md:49,154`（2）。证据：§2.1 | ⛔ 0 裁决 |
| 4 | `fiction_that_feeds_back.pdf` 二进制 〔高校R〕 命中 | **本核验未验**（PDF 不参与文本复算，〔高校R〕 全仓 6 处均为文本命中）。状态：报备面确认存在，处置待裁。证据：§7 边界 B-2 | ⛔ 0 裁决 |
| 5 | `_d7_wang_*` 通配简写 1 处（表外变体） | 该简写位于 `_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md` L84（B5 登记件「表外变体登记」条已载）。本核验经全树文件名扫描确认**无以 `_d7_wang_*` 命名的实体件**（§3.2 命中 0），即该简写所指为**纯文本引用**，不涉实体残留 | ⛔ 0 裁决 |
| 6 | 仓内文件名级残余风险 | **实测未发现残留实体**：全树 2,221 件文件名匹配 `(?i)(wang\|〔IM〕)` 命中 **0 件**。远端 `letters/` 目录仅 2 件且无相关命名。证据：§3.2 | ⛔ 0 裁决 |

---

## 7. 边界与未验面

| 编号 | 项 | 说明 |
|---|---|---|
| B-1 | 登记件计数口径差 | 清单 §三表头称「含 **7** 个登记件台账注记」，§四.1 亦称「7 个漂移登记件（B1/B2/B3/B4/B5/B6a-c）」；**实测盘上为 8 件**（B1/B2/B3/B4/B5/B6a/B6b/B6c，见 §4.1）。二者相容（`B6a-c` 计为 1 组或 3 件之别），但字面计数不一致。本核验净化域一律按**实测 8 件**排除；残差数仍与期望 10/10 吻合，故该口径差不影响结论。**登记备查，不代改。** |
| B-2 | PDF 二进制内字面 | `fiction_that_feeds_back.pdf` 内 〔高校R〕 字节命中**无法经文本复算验证**（PDF 文本层/编码不保证可 grep）。本核验**未**对其做二进制字面判定，列为**报备项**（＝清单 §七第 4 项）。同族：批⑤ 2 件 rename-only PDF（`_coze_online_v3_d7format_2026_09_18.pdf`、`_coze_online_v4_d7format_2026_09_26.pdf`）post SHA 与 pre 全等（B5「rename only (PDF binary)」口径自洽），但**仅能证明字节未变，不能证明其内无目标字面**。 |
| B-3 | 副区 `deposon-sub` 未对位 | 命中 46 件已复算，但**未做 sub↔远端逐件路径对位**（路径基准不同构，强行对位会产生假「无对应」）。见 §5.5。 |
| B-4 | 清单 §七第 1 项件未验 | `THINKING_V3_GT_CONTRIB_2026.md` 不在 10 token 复算面内，其履历表外信息（清华 IIIS/导师/职位）**未单独复算**。见 §6 项 1。 |
| B-5 | pre 值未实测 | 所有 pre SHA-256 仅为登记转录，本侧无 pre 态实体，**不宣称已验证**。见 §4.3。 |
| B-6 | 提交链「0 改写」判据 | 本核验经 GitHub API 确认 8 连提交为纯追加且 HEAD 正确；**未**逐 commit 核对 tree diff 明细，故「0 force-push/rebase/amend」为**间接支持**，非直接证明（该判据最终依赖 git reflog，tarball 不含）。 |
| B-7 | 非 git 树差异 | tarball 不含 `.git`，故 `git ls-files` 类口径与「工作区 clean/0 未跟踪」判据**本核验无法直接复现**；树规模 2,221 件为 tarball 视角（含 `.gitignore` 未过滤）。 |
| B-8 | 核验方仪器自限 | 首轮改名核/三分类曾因 PowerShell 候选路径集不全与一处脚本拼写错误产生**假阴性**，均已重跑修正（见 §3.1 脚注、§5.3/5.4）。本登记件所有计数均以**修正后重跑值**为准。 |
| B-9 | 脱敏边界 | §2.1 残差上下文按 ≤60 字符截断，仅引「件＋行＋落点性质」，**未复制原字面串**；本件全文 0 处新增「〔W老师〕」等原始字面（除 §2.1 表中 token 名与 §5 路径名等结构性引用）。 |

---

## 8. key 形态自扫（R4）

- 扫描面：解包远端树 2,221 件（文本类扩展名全量）。
- 模式：`\b(sk-[A-Za-z0-9]{16,}|tp-[A-Za-z0-9]{16,}|ark-[A-Za-z0-9_-]{16,}|API_KEY\s*=|Authorization:\s*Bearer\s+[A-Za-z0-9._-]{16,})`
- 一轮命中 31 件 → **仪器假阳性自查**（占位符/环境变量名/日志脱敏痕逐件判别）→ **真 key 命中 0 件**，31 件均为 `API_KEY=` 空赋值、`os.environ` 引用、日志脱敏标记等良性形态。
- **R4 判定：CLEAN。** 本核验全程 0 读 `.env`、0 读任何凭据文件、0 明文记录任何 key。

---

## 9. 核验结论（只读范围内）

1. **远端态**：HEAD ＝ `72c5839`，自基线 `6908cac` 的 8 连提交链逐个对位一致，纯追加形态。
2. **残差对拍**：10 个 token 全仓/净化域**逐项 10/10 一致，0 差异**；净化域 6 类非零残差全部落在已声明的 R1 判定链保护面/§2 排除项/PI 存疑面，**0 例外**。
3. **改名核**：批⑤ 10 件「旧路径 0 存在＋新路径存在」**10/10 成立**；全树文件名 `wang|〔IM〕` 命中 **0 件**。
4. **SHA 抽验**：跨 8 批抽验 **34 件次，MATCH 34/34，真 MISMATCH 0**；4 处表观不符经追链确认为**批间链式中间态**（已逐条闭合），并入册为「末批取值」判读口径。
5. **本地↔远端**：主区命中 111 件 vs 远端净化域 0（**反向差，复发风险实证**）；对位 ① 95／② 0／③ 16（修正后 ③＝15 远端无对应＋1 桶位不同）；副区 46 件已复算未对位（B-3）。
6. **边界**：B-1…B-9 共 9 项未验/报备面如实登记，其中 PDF 二进制字面（B-2）与 §七第 1 项件（B-4）为实质性未覆盖面。
7. **⛔ 0 裁决**：§七 6 项待裁事项本件只给证据指针，未作任何处置建议；PI 未就此下裁前不推进。

---

- 出证：evidence-auditor（证据链审计官，deposon N-6 独立核验方）｜核验日 2026-10-08
- 声明：本件为**独立核验登记**，⛔ 0 回改任何既有件、⛔ 0 远端写、⛔ 0 代裁、⛔ 0 编造；所有「实测」均为本核验侧 hashlib/Get-FileHash 复算结果，「登记」值为执行方清单/登记件原文转录。
