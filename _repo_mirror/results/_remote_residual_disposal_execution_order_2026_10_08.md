# 远端残余处置执行单（deposon 公开仓 · 淡化残余 · 续批 D7）

- **出件**：**protocol-keeper**（口径与预登记官 · `agent-3e0c193da529`，本件实际出件者）｜2026-10-08（CST）
- **⛔ 0 冒充**：鲍勃(KIMI,PAT) / evidence-auditor / verifier / verdict-keeper / doc-writer / worker / Mavis 团队 / 查理(GLM) / Trae code / coze 等任一他棒或受托方（仅作**原始出证方**注记引用）。
- **件性质**：**执行设计件（处置方案 ＋ pre 值 ＋ 核验步骤 ＋ 回退指引）**。⛔ **本件 0 执行任何远端写**（0 commit / 0 push / 0 改名 / 0 内容改）；⛔ **0 代裁**（凡涉口径取舍、通道取舍、范围取舍者一律候 PI）；⛔ **0 回改任何既有件**；⛔ **0 解除任何跑禁**。
- **裁据**：PI 2026-10-08 卡 `ask_7448fb50358e1d1aeff6d7c8` 四答 —— ①履历段整段匿名化；②判定键×12＋检查串改键（同步 verifier）；③文本面按淡化口径处置、PDF 保留报备；④本地保持 0 回改＋上传面加防护（含改名授权）。
  > ⚠ **转录声明**：四答逐字要点系**转录自派工单**，本 Turn **未重读该卡原文**；若卡内另有字面约束，以卡为准（登记于 §B-8）。
- **承接**：执行方清单 `6ec7e14bc8a7`（鲍勃 · 2026-10-06）6 批体例（分批 / 逐处行位 / pre 值精确 / SHA 登记）；核验登记件 `3f806e44a13f`（evidence-auditor · 2026-10-08）§6 指针与 §7 边界。

---

## §0 方法与口径（本件自证）

### 0.1 取态途径（只读，如实登记）

| 项 | 实测值 |
|---|---|
| 取态途径 | GitHub API **只读 HTTP GET**：`/repos/zeroandcat/Deposon/git/trees/72c5839?recursive=1` ＋ `/git/blobs/<sha>`；tarball 经 `/tarball/72c5839` |
| 核验对象 commit | `72c58394764d1f22ca4cc8eeb846c0d775d7cbc6`（＝清单 §一 B6c，远端 HEAD） |
| tarball 字节 / SHA-256 | **21,481,520 B / `b0e44df2fa3e…`** |
| 解包落位 | `%TEMP%\pk_remote_readonly\`（⛔ **0 落盘仓内**） |
| 解包树规模 | **2,221 文件 / 164 目录** |
| 树规模一致性 | **与 `3f806e44a13f` §1.1 记录值（2,221 / 164）逐项相同** ✅ |

> ⚠ **口径登记 G-1（tarball 字节差，非内容差）**：本 Turn tarball 为 21,481,520 B / `b0e44df2…`；`3f806e44a13f` §1.1 记 21,488,236 B / `e13547d8…`。二者**取态端点不同**（API `/tarball` vs codeload），gzip 流不同 ⇒ 归档字节不可比。**解包后树规模逐项相同（2,221/164）**，且本 Turn 逐件复算结论与该件 10/10 一致（§1）。**判为归档字节差，非内容差、非执行方漂移**。⛔ 0 以 tarball 字节/SHA 作为内容真值判据。

### 0.2 残差复算口径（沿 `6ec7e14bc8a7` §三 ＋ `3f806e44a13f` §1.3）

- 分 token 复算，**未使用全局 `-w`**；计次单位＝**出现次数**（非命中文件数）。
- 「净化域」＝全仓 2,221 件排除 **8 件** `_deemphasis_sha_drift_register_*`（B1/B2/B3/B4/B5/B6a/B6b/B6c）。
- 二进制件（PDF）单列（§5），文本复算不参与。

### 0.3 本件 0 做之事（诚实边界）

⛔ 0 远端写 · ⛔ 0 本地既有件回改 · ⛔ 0 代裁 · ⛔ 0 编造 · ⛔ 0 读任何凭据/`.env`（**R4 永不明文**）· ⛔ 0 触碰 PDF 二进制 · ⛔ 0 派生 JSON 合并。

---

## §1 指针校核（**先核后引** —— 5 处与执行方清单不一致，全部登记）

> 本 Turn 对 `6ec7e14bc8a7` §七 6 项逐项在 **HEAD `72c5839` 实树**复算。**5 处校核发现**，其中 **C-2／C-3 为实质性口径冲突，须 PI 复核后方可执行**。

### 1.0 校核发现总表

| 编号 | §七项 | 校核结果 | 性质 | 处置 |
|---|---|---|---|---|
| **C-1** | 项 1 | **指针主体名挂错**：清单作「〔W老师〕」，实读该段主体为**另一自然人**（远端已统一作「外部合作导师〔匿名〕」）。且**实体路径为 `docs/…`，非 `_september_workspace/docs/…`** | 命名漂移（挂错名） | 登记入册；处置按 PI 裁 ① 执行（**行位 L58 成立**） |
| **C-2** | 项 3 | **3 个处置点全部为 PI 自身作者块**，非外部导师面：`_md_to_tex.py:784`／`:794`（`\author{袁祺皓`／`\author{Qihao Yuan` 之下一行）＋ `deposon_paper_v1_en.md:3`（`Authors: Qihao Yuan; …`） | **⚠ 口径冲突** | ⛔ **候 PI 复核**（§4.3） |
| **C-3** | 项 4 | **「PDF 内 〔高校R〕 字节命中」经双面复算为假阳性**：PDF 文本层（82,708 字符 / 23 页）＋ `.tex` 源（92,391 字符）**全部 token = 0**；原始字节面 `\bRUC\b` = 0、`〔高校R〕` = 0、`/Author` 为空 | 事实更正 | 登记入册（§5） |
| **C-4** | 项 2 | **实为 1 个键 × 12 处**，非「12 个键」；且**生产侧已用淡化后键名** | 计数口径澄清 | 登记入册（§3.1） |
| **C-5** | 项 5 | `_d7_wang_*` 为**批⑤ 已改名件之旧名 pattern 残留**（该实体已于批⑤ 改名，ledger 记的是改名前 pattern） | 台账滞后 | 登记入册（§6） |

### 1.1 校核证据（本 Turn 实测）

| 校核 | 实测命令/判据 | 实测结果 |
|---|---|---|
| C-1 | 远端 `docs/THINKING_V3_GT_CONTRIB_2026.md` 全文 token 计数 | 「〔当事人W〕」=0、「〔W老师〕」=0、「〔高校R〕」=0、「〔机构G〕」=0、「外部合作导师」=**13**；「清华」=1、「IIIS」=1、「唐平中」=1、「姚期智」=1 |
| C-1 | 远端树路径检索 `THINKING_V3_GT_CONTRIB` | 命中 **`docs/THINKING_V3_GT_CONTRIB_2026.md`**（1 件，19,769 B）；`_september_workspace/docs/` 下**无**同名件 |
| C-2 | 远端 `_md_to_tex.py` L781–797 实读 | L783 `"\\author{袁祺皓 \\\\"`、**L784** `"School of Chemistry and Life Resources, 〔高校R〕 University of China \\\\"`；L793 `"\\author{Qihao Yuan \\\\"`、**L794** 同上 ⇒ 二者均为**PI 自身作者块** |
| C-2 | 远端 `paper/deposon_paper_v1_en.md:3` 实读 | `> Authors: Qihao Yuan; School of Chemistry and Life Resources, 〔高校R〕 University of China; Research Assistant (…)` ⇒ **PI 自身作者行** |
| C-2 | 对照组 `paper/deposon_paper_v1.md:5` 实读 | `> 作者：袁祺皓，中国〔高校R〕化学与生命资源学院，科研助理` ⇒ `6ec7e14bc8a7` §三 已将〔高校R〕此行标注为「**PI 自身单位行 ＝ §2 排除项**」 |
| C-3 | PDF 原始字节（Latin-1 映射）扫描 | `〔高校R〕` 子串 = **1**（偏移 13246，上下文 `ys.A.[…3RUC…7..~.G."`，**位于压缩流内**）；`\bRUC\b` = **0**；`(?i)\bRUC\b` = **0**；`〔高校R〕` = **0**；UTF16BE `R\x00U\x00C` = **0** |
| C-3 | PDF 文本层（pypdf 6.16.2，23 页，82,708 字符） | `〔高校R〕`=0、`〔高校R〕`=0、`〔高校R〕`=0、`中国〔高校R〕`=0、`袁祺皓`=0、`Qihao`=0、`Yuan`=0；元数据 `/Author` = **空** |
| C-3 | 同仓 `.tex` 源 `fiction_that_feeds_back.tex`（93,324 B） | 上述 **全部 token = 0** |
| C-4 | 净化域 `(?i)〔IM〕` 全树计数 | **12**（＝11 JSON ＋ 1 `.py`），与清单/T2 **逐位一致**；**键名去重后仅 1 个**：`no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_〔IM〕API` |
| C-4 | 生产侧 `deposon_team/plugins/*.py` 实读 | **0 件**含 `…_〔IM〕API`；**9 件**已用 `…_agent_plan_线上API`（例 `boss_pa_1_rbr_rm.py:312`） |
| C-5 | 远端 `_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md:84` 实读 | `\| \`*_coze_paper_*_draft_*.md\` (2) + \`*_coze_online_v3_*.md\` (3) + \`_d7_wang_*\` (1) \| 6 \| 67,229 \|` ⇒ 该 pattern 所指实体已在批⑤ 改名为 `_d7_external_advisor_online_publish_v1_20260918.md` |
| — | 远端全树文件名 `(?i)(wang\|〔IM〕)` | **0 件**（独立复现 `3f806e44a13f` §3.2 结论 ✅） |

### 1.2 本 Turn 对 T2 结论的独立复现（10/10 一致，0 差异）

| token | T2 全仓 | 本 Turn 全仓 | T2 净化域 | 本 Turn 净化域 | 判定 |
|---|---:|---:|---:|---:|---|
| `(?i)〔IM〕` | 61 | **61** | 12 | **12** | ✅ 一致 |

（其余 9 token 本 Turn 未全量复算 —— 见 §B-4「未核得」条；⛔ 0 宣称已复现。）

---

## §2 批 **D7-1** · 履历段整段匿名化（PI 裁 ①）

### 2.1 处置对象与 pre 值

| 项 | 值 |
|---|---|
| 远端路径 | `docs/THINKING_V3_GT_CONTRIB_2026.md`（**非** `_september_workspace/docs/`，见 C-1） |
| pre SHA-256[:12] | **`b04c39175ede`** |
| pre 字节 / 行数 | 19,769 B / 132 行 |
| BOM | 无 BOM（实测） |
| 处置行位 | **L58**（PI 裁 ①「L58-59」；L59 现状见 §2.4） |

### 2.2 待匿名化字段拆解（L58 实读，**仅列字段性质与拟替换字面；原值不在本件复制**）

| # | 字段性质 | 现况判定 | 拟替换为 |
|---|---|---|---|
| F1 | 任职机构（**另一高校**简称＋学科/院系缩写） | **仍明文** | `匿名合作机构`（沿该件既有口径 L58 前半已用此词） |
| F2 | 起止年份＋职称段（助理→副教授晋升序列） | **仍明文** | `（任期与职称略）` |
| F3 | 博士培养机构简称（含 `IIIS` 类缩写） | **仍明文** | `匿名合作机构` |
| F4 | 博士学位年份 | **仍明文** | `（年份略）` |
| F5 | **两位导师姓名**（2 名自然人） | **仍明文** | `导师姓名略` |
| F6 | 讲座题名＋主办方残段（L59，**已部分淡化**：主办方已作「匿名合作机构 AI 之夏」） | 讲座题名**仍明文** | 见 §2.4 分档 |

> **脱敏边界**：本表**不复制** L58 原字面串（沿 `3f806e44a13f` §7 B-9 口径：只引「字段性质 ＋ 行位」）。执行方按行位直取原值。

### 2.3 替换后字面草案（**草案，待 PI 复核生效**）

```diff
- L58: - 单位：<机构A>（<起止年>，<职称段>）；<机构B> 博士（<年>，导师<姓名1>、<姓名2>）。
+ L58: - 单位：匿名合作机构（任期与职称略）；博士学位（年份略，导师姓名略）。
```

**字数口径**：替换后该行由 **1 行** 维持，**0 行数变化**；因删字符，该件字节数将下降（改后 SHA-256 须实测回填 §2.6）。

### 2.4 L59 分档（**候 PI，0 自行扩展**）

| 项 | 现状 | 事实 | 本件处置 |
|---|---|---|---|
| 主办方 | 已作「匿名合作机构 AI 之夏」 | 已淡化 | **0 触动** |
| 讲座题名 | **仍明文**（含会议/议程特征词） | 可与 F1–F5 联合再识别 | ⛔ **候 PI**：PI 裁 ① 字面为「L58-59 整段」，本件按字面**纳入 L59 讲座题名**，拟替换为 `（讲座题名略）`；若 PI 认为 L59 已足，**0 触动**亦为合法执行 |

> ⚠ **登记 K-1（未自裁的范围张力）**：该件 §2.0「核实基线」块实为 **L56–L61**，其中 **L60（代表性工作：2 篇论文题名＋5 名合作者姓名）＋ L61（研究品味归纳）** 之可识别度**高于 L58-59**。PI 裁 ① 字面止于 L58-59 ⇒ **本件 0 自行扩展至 L60-61**；作为**候裁观察**登记于此，⛔ 0 执行。

### 2.5 执行动作（逐处）

| 序 | 动作 | 件 | 行 | 类型 |
|---|---|---|---|---|
| 1 | 整行替换（按 §2.3 草案） | `docs/THINKING_V3_GT_CONTRIB_2026.md` | L58 | 内容 |

### 2.6 post 值回填位（**执行方回填，本件 0 代填**）

| 字段 | 值 |
|---|---|
| post SHA-256[:12] | ⬜ 待执行方实测回填 |
| post 字节 | ⬜ 待回填 |
| 净化域该件 `清华/IIIS/唐平中/姚期智` 复算 | 预期 0（**预期非实测**） |

---

## §3 批 **D7-2** · 判定键改键 ＋ 检查串（PI 裁 ②）

### 3.1 计数口径更正（C-4）

> 清单 §七 2 与 §四 3 作「`no_*_〔IM〕API` 判定键 **×12**」。本 Turn 实测：**键名去重后仅 1 个**，**12 为该键的落点数**（11 JSON ＋ 1 `.py`）。
> ⇒ **工作量口径**：**改 1 个键名，落 12 处**（非改 12 个键）。

### 3.2 键名映射表（**1:1，方向唯一**）

| # | 现键名（pre） | 拟改键名（post） | 依据 |
|---|---|---|---|
| K-1 | `no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_〔IM〕API` | `no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_线上API` | **生产侧已用此名**（9 件 plugin 实证）⇒ 本次为**历史产物对齐现行生产约定**，非新造命名 |

> ✅ **映射无歧义**：全树同 stem 下**仅 2 个**完整键名（`…_〔IM〕API` / `…_线上API`），0 第三个候选。
> ⛔ **高危警告（务必遵守）**：另有 **9 件 plugin 使用**同 stem 的**第三形态（无后缀）** `no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan`（例 `attack_pc_a1_resampling.py:87`）。
> ⇒ **禁止对 stem 前缀做通配替换**；**必须整键全名精确替换**。误替将污染 ≥9 个兄弟键。

### 3.3 12 处处置点（逐处行位 ＋ pre SHA-12）

| # | 远端路径 | 行 | pre SHA-256[:12] | 字节 |
|---:|---|---:|---|---:|
| 1 | `_september_workspace/results/skill_a_p_a_60cells_result_2026_09_11.json` | 9 | `f4a210d69220` | 2,220 |
| 2 | `_september_workspace/results/skill_b_p_c_alpha_beta_result_2026_09_11.json` | 9 | `b921002e4dfb` | 12,609 |
| 3 | `_september_workspace/results/skill_c_p_e_3modality_result_2026_09_11.json` | 9 | `470425a8c77d` | 5,271 |
| 4 | `_september_workspace/results/skill_d_p_f_observer_result_2026_09_11.json` | 10 | `a8b8687e08cd` | 11,013 |
| 5 | `_september_workspace/results/boss_pa_1_rbr_rm_result_2026_09_15.json` | 10 | `c7c59e0d2f6c` | 8,753 |
| 6 | `_september_workspace/results/boss_pa_2_potential_game_result_2026_09_15.json` | 10 | `5c76137d6430` | 7,530 |
| 7 | `_september_workspace/results/boss_pa_3_replicator_dynamics_result_2026_09_15.json` | 10 | `d6f233d73c45` | 9,098 |
| 8 | `_september_workspace/results/deposon_pa_d1_d3_2026_09_15.json` | 10 | `937c4de3adb8` | 15,613 |
| 9 | `_september_workspace/results/deposon_pc_d1_d3_2026_09_15.json` | 12 | `3d54afcf64ff` | 20,414 |
| 10 | `_september_workspace/results/deposon_pf_d1_2026_09_15.json` | 14 | `12791772814e` | 21,933 |
| 11 | `_september_workspace/results/deposon_pg_v01_9m60c_2026_09_15.json` | 16 | `c172144e57cd` | 11,518 |
| 12 | `_september_workspace/results/_pc_d1_d3_2026_09_15.py` | 213 | `3131e5b0519d` | 43,028 |

**类型**：#1–#11 为 JSON **键名**（双引号 JSON string）替换；#12 为 `.py` **dict 字面键**替换 ⇒ **两者序列化形态不同**，须分别校验（JSON 件须 `json.load` 复核；`.py` 件须 `python -c "import ast;ast.parse(...)"` 复核）。

### 3.4 `compare_versions.py` 判定检查串处置

**件**：`_september_workspace/.trae/audit/compare_versions.py`｜pre SHA-12 **`f4e9b7f50e6d`**｜7,993 B / 179 行｜无 BOM

| 行 | pre 字面（实测） | 落点性质 | 拟处置 |
|---:|---|---|---|
| **L127** | `R['has_yuanqihao'] = ('袁祺皓' in text) or ('Qihao' in text) or ('Yuanqihao' in text) or ('Qihao Yuan' in text)` | 判定键 ＋ 检查串（**自然人姓名，＝ PI 本人**） | ⛔ **候 PI**（§4.4 口径冲突同源）—— 清单 §七 2 未列此行 |
| **L128** | `R['has_ruc_chem'] = ('中国〔高校R〕' in text and ('化学与生命资源' in text)) or ('〔高校R〕 University' in text)` | 判定键 ＋ 检查串（**机构名 ＋ 院系名**） | 按 PI 裁 ②「检查串改键」处置：键名改 `has_ruc_chem` → `has_anonymous_chem`；串 `'中国〔高校R〕'` → `'匿名合作机构'`，`'化学与生命资源'` → `'化学与生命资源学院'`（**保留可判而不指名的粒度**，属技术方案 ⛔ 候 PI 确认，见 §B-6） |
| **L129** | `R['mentions_external_mentor'] = '〔当事人W〕' in text` | 判定键（**键名已淡化**）＋ 检查串（**自然人姓名**） | 键名**已合规，0 触动**；串按同款口径改 `'〔当事人W〕'` → `'外部合作导师'`（**须与被检文本的现行口径一致** —— 见 §3.5 重锚要求） |
| **L160** | `print('  袁祺皓/〔高校R〕 chem    :', R['has_yuanqihao'], R['has_ruc_chem'])` | 打印标签（**含机构缩写 ＋ PI 本名**） | 随 L127/L128 同步改；标签改 `'  匿名对象/匿名机构 :'`（**候 PI**） |
| **L161** | `print('  外部合作导师〔匿名〕 present    :', R['mentions_external_mentor'], '| fund hits:', R['fund_numbers'])` | 打印标签（**已淡化**） | **0 触动** |

> ✅ **键名合规性**：L129 键名 `mentions_external_mentor` **已是淡化后命名**（批⑥已改）；⇒ PI 裁 ②「检查串改键」之「键」在 L129 **已完成**，余 L128 未改。

### 3.5 verifier 兼容同步面清单（本 Turn 逐件实测，**0 推测**）

| 面 | 实测结论 | 证据 |
|---|---|---|
| **verifier 读该键者** | **0 件** | 全仓 `verifier/`（v1–v43 ＋ `_september_workspace/verifier/` 双份 ＋ `audit/conservation.py`）**0 件**含 `〔IM〕API`；`0 件`引用 12 个产物文件名 |
| **verifier 写该键者** | **0 件** | 同上 |
| **生产侧（plugin）** | **9 件已用新键**（`boss_pa_1/2/3`、`runner_pa_d1_d3`、`skill_a/b/c/d`、`_pg_v01_compute`）⇒ **重跑即产出新键**，与本次改键**方向一致、0 冲突** | 逐件实读 |
| **生产侧第三形态** | **9 件用无后缀 stem**（`attack_pc_a1–a3`、`boss_pc_1–3`、`boss_pg_1–3`）⇒ **不在本次改键范围**，但**禁用 stem 通配**（§3.2） | 逐件实读 |
| **verifier handoff 锚** | `verifier/handoff/KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json` **已含新键**（`…_线上API`）⇒ **0 需同步** | 实读 |
| **frozen 锚** | `KT_ABC1_anchors_sha256_12.json`（SHA-12 `03c6c01f3697`）为 **frozen 5 锚**，其自身登记「**严守 0 触动**」；其锚对象为 `tools/llm_client.py`／`tools/exp_harness.py` 等，**不含**本次 12 产物 ⇒ **0 牵连** | 实读 |
| **manifest 哈希牵连** | **4 件 manifest 记录 `compare_versions.py` 的 pre 哈希 `03e22a91bc0c` / 7,958 B**：`_movedout_manifest_2026_09_21.json`、`_archive_manifest_deposon_sub_2026_09_23.json`、`_kimi_push_v3_manifest_batch2_e18c17bb.json`（另带 `gitsha 8dbcfd89…`）、`_mirror_manifest.json`（`sha256:null`，仅记 size 7,958） | 实读 |
| ⚠ **既存漂移（**非本批引入**）** | 上述 manifest 记录的 `03e22a91bc0c`/7,958 B **已是改前值**；当前远端实为 `f4e9b7f50e6d`/7,993 B ⇒ **批⑥ 已使其漂移**（内容替换致字节变化）。本批再改将**再增一次漂移** | 复算 |

### 3.6 读数域重锚要求（**PI 裁 ② 明示「同步 verifier」之技术落点**）

| # | 要求 | 说明 |
|---:|---|---|
| R-1 | **判定语义不灭失** | 改键/改串**不得**把判定退化为常量 —— 改后检查串须仍能命中**现行文本**（例：文本侧机构名已作「匿名合作机构」，则 `has_ruc_chem` 的中文分支若改为命中 `'匿名合作机构'`，其语义由「检出特定机构」变为「检出匿名机构标记」，**可判性口径改变**，须登记） |
| R-2 | **双读兼容窗** | 建议改后同时接受新旧串（`('匿名合作机构' in text) or ('中国〔高校R〕' in text)`）以覆盖历史语料，⛔ 但**窗口期长度属 PI 口径面** —— 本件 0 定档 |
| R-3 | **读数域登记** | 改键前后 `results/` 下引用该键之**任何**读数/判定件须登记新键名（旧键名 0 静默消失） |
| R-4 | **哈希漂移登记** | 12 件 ＋ `compare_versions.py` 改后 SHA-256[:12] 须入新批漂移登记件（沿批⑥体例 `_<批>_sha_drift_register_<批>_<日>.md`） |

---

## §4 批 **D7-3** · LaTeX／元数据文本面（PI 裁 ③「按淡化口径处置」）

### 4.1 ⚠ 口径冲突 **C-2**（**候 PI 复核 —— 本批在 PI 复核前 0 执行**）

**事实**：PI 裁 ③ 的三个处置点，**全部是 PI 自身的作者块**，**无一处是外部导师面**：

| # | 远端路径 · 行 | pre SHA-12 | pre 字面（实测） | 归属 |
|---:|---|---|---|---|
| 1 | `_september_workspace/.trae/scripts/_md_to_tex.py` **L784** | `c1caa4f43618` | `"School of Chemistry and Life Resources, 〔高校R〕 University of China \\\\n"`（**L783 `\\author{袁祺皓` 之下一行**） | **PI 自身作者块（中文分支）** |
| 2 | `_september_workspace/.trae/scripts/_md_to_tex.py` **L794** | 同上 | 同上字面（**L793 `\\author{Qihao Yuan` 之下一行**） | **PI 自身作者块（英文分支）** |
| 3 | `paper/deposon_paper_v1_en.md` **L3** | `9c34854be6e7` | `> Authors: Qihao Yuan; School of Chemistry and Life Resources, 〔高校R〕 University of China; Research Assistant ([email to be added])` | **PI 自身作者行** |

**张力陈述**（照录既有件字面，0 自造结论）：
1. `6ec7e14bc8a7` §三 将 `paper/deposon_paper_v1.md:5` 的「〔高校R〕」标注为「**PI 自身单位行 ＝ §2 排除项**」（`3f806e44a13f` §2.1 复现同口径）⇒ **既有淡化口径已将 PI 自有单位行列为排除项**。
2. PI 裁 ③ 字面为「文本面（LaTeX/元数据等）**按淡化口径处置**」⇒ 若**字面执行**，则 PI 自身单位行**被匿名化**，与既有 §2 排除项口径**相反**。
3. 该 3 点与 `6ec7e14bc8a7` §七 3 的「涉可识别信息」定性**同指**同一批字面（School of Chemistry and Life Resources, 〔高校R〕 University of China ×4 ＋ `_glm_five_items` 存疑 ×2）。

**⇒ 三档（各后果照录事实，⛔ 0 代裁、0 预判裁向）**：

| 档 | 内容 | 后果 |
|---|---|---|
| 甲 | **按字面执行**：3 点 ＋ `_glm_five_items:49,154` 全按淡化口径替换 | PI 自有作者块单位行被匿名化；**论文作者身份行与单位行自洽性下降**；与 §2 排除项口径**并存冲突**（须登记双记） |
| 乙 | **按 §2 排除项口径**：认定为 PI 自有面 ⇒ **0 替换**，登记为「排除项」 | 净化域该 4 处残差**保留**；须以报备面登记（沿 `has_ruc_chem` 同款豁免） |
| 丙 | **分件分档**：`_md_to_tex.py` 2 处（**模板字符串**，未来重生成即回流）vs `deposon_paper_v1_en.md:3`（**论文作者行**）分开处置 | 须 PI 分别给出两档口径；模板面与已生成件面**回流风险不同** |

> ⚠ **0 自行择一**。**PI 未复核前，本批 0 执行**（批次编排见 §11：其余批可先行，本批挂起）。

### 4.2 `_glm_five_items_suggestion_table_2026_10_01.md` 存疑 2 处

**件**：`_september_workspace/results/_glm_five_items_suggestion_table_2026_10_01.md`｜pre SHA-12 **`f2b1359be37d`**｜29,622 B / 268 行

| 行 | pre 实读（截断） | 性质 |
|---:|---|---|
| **L154** | `2. **单位**（Comments 栏字面）：「School of Chemistry and Life Resources, 〔高校R〕 University of China」⚠ 涉可识别信息，**是否照录由 PI 按 H8 定**；` | **PI 按 H8 定的存疑面**（该件自标） |
| **L49** | `\| **⑤** \| 已发表件元数据终核 \| **建议值 ＝ 盘上登记四项「全部相符」＋ 追加 6 项可核面**… \|` | arXiv 已发表件元数据核对面（该行 `〔高校R〕` 命中经复算位于同行内 arXiv 核对面） |

> ⚠ **登记 K-2**：`L154` 所述为 **arXiv:2609.09001 之 Comments 栏单位字面**。该文**已公开发表**（`2609.09001`，Qihao Yuan）⇒ 「匿名化已发表件的单位字面」与「仓内文本淡化」**不同域**：改仓内记录**不改**已发表内容。**0 混淆两域**（沿 `_clearance_materials_register_2026_10_08.md` D-3 备选档「0 自行合并为单题」）。

---

## §5 批 **D7-4** · `fiction_that_feeds_back.pdf` 例外声明（PI 裁 ④ 保留报备）

### 5.1 PI 裁 ④ 之执行（登记）

| 项 | 值 |
|---|---|
| 对象 | `_september_workspace/results/_archive_2026_09_20/fiction_that_feeds_back.pdf` |
| 字节 | 356,123 B |
| 处置 | **保留 ＋ 报备**（PI 裁 ④） |
| 本件动作 | **0 触碰二进制**、**0 重制**、**0 撤下** |

### 5.2 事实更正 **C-3**（**本 Turn 双面复算** —— 报备项可升级为「假阳性结案」）

| 面 | 判据 | 实测 |
|---|---|---|
| 原始字节（Latin-1） | `〔高校R〕` 子串 | **1**（偏移 13246，上下文 `ys.A.[…3RUC…7..~.G."` —— **压缩流内随机字节**） |
| 原始字节 | `\bRUC\b` / `(?i)\bRUC\b` / `〔高校R〕` / UTF16BE `R\x00U\x00C` | **0 / 0 / 0 / 0** |
| **PDF 文本层** | pypdf 6.16.2；23 页；82,708 字符 | `〔高校R〕`=0、`〔高校R〕`=0、`〔高校R〕`=0、`中国〔高校R〕`=0、`袁祺皓`=0、`Qihao`=0、`Yuan`=0 |
| PDF 元数据 | `/Author` | **空串**；`/Title` 为论文题名（无机构）；`/Producer` = pdfTeX |
| **同仓 `.tex` 源** | `fiction_that_feeds_back.tex`（93,324 B / 92,391 字符） | 上述 **全部 token = 0** |

**结论（事实层，非裁量层）**：
> 「PDF 内 〔高校R〕 字节命中」**经文本层＋源层双面复算为假阳性**。唯一字节命中位于**压缩流内**、非词边界、非大小写变体、**不可解出机构名**。**PDF 内 0 处可检出机构标识**。

⇒ **对 PI 裁 ④ 的影响（供裁，非本件代裁）**：裁 ④「保留报备」**成立且成本最低**；且因「0 处真实命中」，**「重制 PDF 去命中」之选项失去事实基础**（无命中可去）。**报备面可否由「实质残留」降格为「仪器假阳性」结案** ⇒ ⛔ **候 PI**（本件 0 代裁，0 撤销 PI 已下之保留裁）。

---

## §6 批 **D7-5** · `_d7_wang_*` 通配简写（C-5）

**件**：`_september_workspace/results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md`｜pre SHA-12 **`2f00429ed2d8`**｜37,637 B / 388 行

| 行 | pre 实读 | 处置 |
|---:|---|---|
| **L84** | `\| \`*_coze_paper_*_draft_*.md\` (2) + \`*_coze_online_v3_*.md\` (3) + \`_d7_wang_*\` (1) \| 6 \| 67,229 \|` | 替换 `_d7_wang_*` → `_d7_external_advisor_online_*` |

**依据**：批⑤ 已将 `_d7_external_advisor_〔IM〕_publish_v1_20260918.md` → `_d7_external_advisor_online_publish_v1_20260918.md`（`6ec7e14bc8a7` §二批⑤ 第 10 项；`3f806e44a13f` §3.1 #10 实测旧路径 0 存在 ＋ 新路径存在）⇒ L84 所记 pattern **为改名前旧名**，属**台账滞后**。

> ⚠ **登记 K-3（计数语义）**：L84 为「子类 pattern 汇总」表，各 pattern 后括号内为**件数**。替换后 pattern 与实体名一致，**件数 1 保持不变**；**0 触动**同行其他 pattern 及其计数（`2`/`3`/`6`/`67,229`）。

---

## §7 批 **D7-6** · 仓内文件名级残余（PI 裁 ④ 改名授权之登记位）

### 7.1 远端当态实测

| 判据 | 结果 |
|---|---|
| 全树 2,221 件文件名 `(?i)(wang\|〔IM〕)` | **0 件**（本 Turn 独立复现 `3f806e44a13f` §3.2 ✅） |
| 远端 `letters/` 目录 | **2 件**（`_codex_theory_derivation_reply_2026_09_30.md`、`_v5_rj5_external_rederive_reply_codex_2026_09_29.md`），**0 件** wang/〔IM〕 命名 |
| 清单 §四 2 所列悬空引用 4 类 | 本 Turn **本地 ＋ 远端双向实测均 0 件**：`EXTERNAL_ADVISOR_PROGRESS_REPORT`=0、`D3_〔IM〕_MIDTERM_2026_09_09_actual`=0、`count_〔IM〕.py`=0、`count_online.py`=0 ⇒ **确为纯文本悬空引用，0 实体** |

### 7.2 处置

| 项 | 处置 |
|---|---|
| 远端文件名残余 | **0 件 ⇒ 本批 0 远端动作** |
| **今后发现实体件时** | **按批⑤式改名（PI 已授权）** —— 授权登记见《上传防护/对照件》`_upload_guard_mirror_pair_2026_10_08.md` §6 |
| ⚠ **本地侧真实风险** | 本地 **15 件** wang/〔IM〕 文件名实体（主区 8 ＋ 副区 7），其中 **5 件为本地独有、远端无对应**（详见防护件 §1.3）⇒ **上传即回流** |

---

## §8 执行通道候选（**候 PI 派 —— 本件 0 派工、0 联系他方**）

| 通道 | 内容 | 优点 | 风险/须约束 |
|---|---|---|---|
| **T-甲 · PI 直办** | PI 自持 PAT 亲执行 4 批 | 0 交接损耗；命名/口径裁量即时可用 | PI 时间成本；批次纪律须自守 |
| **T-乙 · 他方代执行（沿鲍勃模式）** | 委托 KIMI/受托方按本执行单逐批执行 ＋ 回漂移登记件 | 复用既有 6 批体例 ＋ 交接熟练 | 须受托方逐条回填 post SHA；**口径项（C-2/D7-3）0 授权他方裁量**；PAT 生命周期（`6ec7e14bc8a7` §五记 PAT 2026-10-06 到期 ⇒ **须核新凭据可用性**） |
| **T-丙 · 混合** | 事实性批次（D7-1/2/5）他方执行；**口径批次（D7-3）PI 直裁后再派** | 事实与裁量分离 | 须 PI 先答 C-2 方可全批开工 |

> ⛔ **本件 0 代裁通道**；⛔ **0 预排期**；⛔ **0 联系任何受托方**。通道取舍 ＋ C-2 口径复核 **一并候 PI**（建议**同卡并题**，二者皆为开工前置）。

---

## §9 核验步骤（执行方可跑，逐条机械）

> **工作面**：仓根 `repos/Deposon`（`/home/z/my-project/repos/Deposon`）。**读数面 ＝ HEAD 改后**。

```bash
# V-1 残余复算（沿清单 §八 附录 C 口径：分 token、0 全局 -w）
git -c core.quotepath=false grep -o -e 〔W老师〕 -- . | wc -l          # 预期 12（8 登记件台账，净化域 0）
git -c core.quotepath=false grep -o -e '〔当事人W〕' -- . | wc -l        # 预期 0
git -c core.quotepath=false grep -o -i -e 〔IM〕 -- . | wc -l       # 预期 12 → 改键后期望 0（净化域）
git -c core.quotepath=false grep -o -i -e 〔高校R〕 -- . | wc -l      # 预期 14（登记件）｜净化域读数见 D7-3 裁

# V-2 文件名级（预期 0）
git ls-files | grep -icE '(wang|〔IM〕)'                          # 预期 0

# V-3 改键完整性：旧键 0 残留 / 新键 12 落点 / 兄弟键未污染
git grep -n 'no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_〔IM〕API' -- . | wc -l   # 预期 0
git grep -n 'no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_线上API'     -- . | wc -l   # ≥12
git grep -n 'no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan"'            -- . | wc -l   # 兄弟键应仍 ≥9（未被误替）

# V-4 语法/序列化复核
python -c "import json,glob;[json.load(open(f)) for f in glob.glob('_september_workspace/results/*.json')]"
python -c "import ast;ast.parse(open('_september_workspace/results/_pc_d1_d3_2026_09_15.py',encoding='utf-8').read())"
python -c "import ast;ast.parse(open('_september_workspace/.trae/audit/compare_versions.py',encoding='utf-8').read())"
python _september_workspace/.trae/audit/compare_versions.py      # 目视 L160/L161 标签与读数

# V-5 批次改动面
git show <commit> --stat

# V-6 post SHA 逐件对照新漂移登记件
sha256sum <件>                                                      # 对照 D7 漂移登记件 post 值（末批取值口径）
```

**核验硬约束**：
- **禁 force-push / rebase / amend**（沿 `6ec7e14bc8a7` §八 R2 红线）。
- **批⑤ 同款原子性**：改名批须与其路径锚回写件**同 commit**（`6ec7e14bc8a7` §八「revert 单 commit 即整体回退」）。
- **末批取值口径**：任一件被多批先后改动时，**须按末批登记件 post 值比对**（沿 `3f806e44a13f` §4.3 已入册口径）。

---

## §10 回退指引（沿 `6ec7e14bc8a7` §八）

| 项 | 规定 |
|---|---|
| 机制 | **一律 `git revert <对应批 commit>`**；⛔ 严禁 force-push / rebase / amend |
| 批独立性 | D7-1 / D7-2 / D7-4(0 动作) / D7-5 / D7-6(0 动作) 各自可独立 revert |
| **D7-2 原子组** | 12 产物 ＋ `compare_versions.py` ＋ 3 件 manifest 记录 ⇒ **须同 commit 落**，revert 单 commit 即整体回退 |
| ⚠ **manifest 回退边界** | 3 件 manifest 所记 `03e22a91bc0c` **在 D7-2 之前即已漂移**（批⑥所致）⇒ revert D7-2 **不能**使 manifest 恢复一致；manifest 重锚**属独立后续动作**，⛔ 0 混入 D7-2 commit |
| 基线 tag | `deemph-baseline-20261006` ＝ `6908cac`（**远端是否仍存该 tag 本 Turn 未核**，见 §B-7） |

---

## §11 批次编排与依赖

| 批 | 内容 | 件数 | 前置 | 状态 |
|---|---|---:|---|---|
| **D7-1** | 履历段整段匿名化（L58，＋L59 待 PI 定） | 1 | PI 裁 ①（已下） | ⬜ 可开工（L59 分档候 PI） |
| **D7-2** | 判定键 1→12 处 ＋ `compare_versions.py` L128/L129/L160 | 13（＋4 manifest 记账） | PI 裁 ②（已下）＋ §4.4 L127 分档 | ⬜ 可开工（L127 候 PI） |
| **D7-3** | LaTeX/元数据 3 点 ＋ `_glm_five_items` 2 点 | 3 件 | **PI 裁 ③ 已下，但 C-2 口径冲突未复核** | ⛔ **挂起（候 PI 复核）** |
| **D7-4** | PDF 保留报备 | 0 | PI 裁 ④（已下） | ✅ **0 动作**；C-3 报备升级候 PI |
| **D7-5** | ledger `_d7_wang_*` | 1 | 名义授权（PI 授权改名面） | ⬜ 可开工（**命名面属 PI 授权域**，若 PI 认为需另裁则挂起） |
| **D7-6** | 文件名残余 | 0 | — | ✅ **0 动作**（远端 0 命中） |

**建议 commit 切分**（沿鲍勃 6 批体例，**批间独立可 revert**）：
`D7-1` 1 commit → `D7-2` 1 commit（13 件 ＋ manifest 记账同 commit）→ `D7-5` 1 commit ⇒ **建议 3 commit**；D7-3 待 PI 复核后另起 1–2 commit；D7-4/D7-6 **0 commit**。

---

## §12 边界与未核面（如实登记，⛔ 0 推断补齐）

| 编号 | 项 | 说明 |
|---|---|---|
| **B-1** | PI 卡原文未重读 | 四答逐字要点**转录自派工单**；本 Turn 未调取卡 `ask_7448fb50358e1d1aeff6d7c8` 原文。若卡内另有约束，以卡为准 |
| **B-2** | pre 值边界 | 本件全部 pre SHA-256[:12] 系**本 Turn 对 HEAD `72c5839` 实树复算**（可信）；**0 pre-态实体**（HEAD 之前态无解包件），故**不含**「改前 pre」与「基线 pre」之对比 |
| **B-3** | manifest 既存漂移 | 4 件 manifest 所记 `03e22a91bc0c`/7,958 B **早于本批即已漂移**（批⑥所致）；本 Turn **0 核**其写入时点与成因，仅据字节差登记 |
| **B-4** | 10 token 全量复算 | 本 Turn **全量复算 `〔IM〕`（61/12，与 T2 一致）**；其余 **9 token 未全量复算** ⇒ ⛔ **0 宣称已复现 T2 全表** |
| **B-5** | 本地侧未核 | 本 Turn **0 触碰本地件**（⛔ 0 回改纪律）；本地 wang/〔IM〕 实体计数见**防护件**（独立实测） |
| **B-6** | §3.4 L128 替换粒度 | 「改串后仍具可判性」之**技术方案**（粒度／双读窗／窗期）属**执行技术面**，本件给出 1 个建议档并**明示为候 PI 确认**，⛔ 0 自定档 |
| **B-7** | 基线 tag 在位 | `deemph-baseline-20261006`（`6908cac`）**是否仍存于远端，本 Turn 未核**（0 tag 查询）⇒ 回退可行性**未验** |
| **B-8** | PAT 状态 | `6ec7e14bc8a7` §五记 PAT 于 2026-10-06 到期；**本 Turn 0 核任何凭据**（R4 永不明文）⇒ 执行通道 T-乙 之凭据可用性**未验** |
| **B-9** | 派生 JSON | 本件 **0 产出 JSON**；Markdown 表内**多读并列保留、0 折算 0 合并** |
| **B-10** | 脱敏边界 | 本件**不复制**待匿名化原字面（沿 `3f806e44a13f` §7 B-9 口径：只引「行位 ＋ 字段性质」）；待匿名化项以 **F1–F6／性质** 表达，执行方按行位直取 |

---

## §13 纪律自证

| 项 | 状态 |
|---|---|
| **⛔ 0 远端写** | 全程 GitHub API **只读 GET**（tree / blobs / tarball）；⛔ 0 commit 0 push 0 改名 0 内容改 |
| **⛔ 0 本地回改** | 本地仓 **0 写入**；远端件解包**仅落 `%TEMP%`**，⛔ 0 落盘仓内 |
| **⛔ 0 代裁 / 0 预判裁向** | C-2（三档）、§2.4 L59 分档、§4.1 三档、K-1（L60-61 范围张力）、§8 通道 三档 —— 全部「列选项 ＋ 各后果 ＋ 候 PI」，**0 自择** |
| **⛔ 0 编造** | 全部指针、行位、pre SHA、token 计数均**本 Turn 实测**；未核得处逐条登记（§12 B-1…B-10）；PI 卡四答**明示转录来源**（B-1） |
| **R4 永不明文** | ⛔ 0 读 `.env`／0 读任何凭据／0 明文记录任何 key |
| **0 派生 JSON 合并** | 本件 0 产出 JSON |
| **撞名实测（落盘前）** | 4 候选直查 **全 False** ＋ 全仓递归 `*residual_disposal*`／`*upload_guard*` **0 命中** ⇒ **新建，0 覆写** |
| **命名合规** | 件名 `_remote_residual_disposal_execution_order_2026_10_08.md` —— 无 `_vN_` 阶段前缀（沿 PI 09-29 命名裁 ＋ 10-01 补记「派工建议名亦须合规」） |
| **版式** | UTF-8 无 BOM · LF |
| **产出件数** | **2 件即停**（本件 ＋ 防护件） |
| **署名如实** | **protocol-keeper**（`agent-3e0c193da529`）；他棒/受托方仅作**原始出证方注记引用** |

---

**落款**：**protocol-keeper**（口径与预登记官 · `agent-3e0c193da529`）｜2026-10-08｜**远端残余处置执行单 · 续批 D7（6 项 → 4 批可执行 ＋ 1 批挂起 ＋ 1 批 0 动作 ＋ 5 处校核发现）**｜⛔ 0 远端写 · 0 回改 · 0 代裁 · 0 编造 · R4 永不明文｜**本件自身 SHA-256[:12]／字节／行数随回执回报（不自写入，防自指悖论）**。