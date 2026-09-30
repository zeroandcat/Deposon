# V4 论文面「补救档」· **棒 1 追源件**（R-2 三阈值 + R-4 P-F）｜worker · **纯只读检索＋哈希复算**

- 产出件：`results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md`（**新件**）
- 承接 agent：worker（执行类：只读检索 + 哈希复算）→ evidence-auditor（审来源链真实性）→ verifier（0 独立复核）→ verdict-keeper（裁因）
- 署名：**worker**（实际出件 agent；沿「产物署名如实，不冒充他方名头」）
- 日期：2026-09-29

---

## §0 控制件核验（先核哈希后引用）

| 控制件 | 派工给定 SHA-12 | 本棒 SHA-256 复算（前 12 位小写） | 字节 | 结论 |
|---|---|---|---:|---|
| 编排件 `results/_v5_paper_remedy_line_orchestration_2026_09_29.md` | `d911674e68cf` | **`d911674e68cf`** | 48,292 | **MATCH** |
| 来源台账 `results/_v5_sub_artifact_ledger_history_r3_2026_09_29.md` | `e04a46b02d13` | **`e04a46b02d13`** | 128,760 | **MATCH** |

- 执行口径：编排件 **§2-R-2**（L59–L69）＋ **§2-R-4**（L83–L93）两节；PI 批 13 裁项 Q1＝**丙档**（`results/_v5_confirm_b13_decisions_register_2026_09_29.md` L49 逐字）。
- **0 设阈值、0 改判据、0 跑实验、0 补写来源、0 动任何既有件**（本棒产出仅本件 1 件）。

---

## §1 检索范围与方法（供下游对账）

**范围**：`D:\私人资料\deposon-repo`（主仓，本棒 0 写入）＋ sibling `D:\私人资料\deposon-sub`（**只读**）。检索面 = 全树 `*.md / *.json / *.py / *.tex`。

**诚实交代 1 · 源件路径的两面**：
- 编排件 / 台账所列 `results/_archive_2026_09_20/review_*.md` 与 `results/_glm_v3_双审报告_2026_09_18.md` 在**主仓内 0 命中**；实体在 sibling `D:\私人资料\deposon-sub\results\`（**同相对路径**）。
- 本棒 6 件审稿 / 报告源件 SHA-12 **逐件复算全部 MATCH**：`0d36d7cd0589` / `09784ff172b3` / `5198a7059c06` / `26537967db82` / `8d00c6d4a242` / `fe80bad08eef`。

**诚实交代 2 · mtime 不可作唯一定序键**：
- 盘上多批件 mtime 与件内自陈日期**不一致**（例：`results/_v3x_d0_5_proposal_trae_2026_09_17.md` mtime 09-20 17:11:14 而件尾自陈「2026-09-17」；`docs/V3X/D7_WANG_TEACHER_WECHAT_PUSH_REQUIREMENTS_2026_09_18.md` mtime 09-16 11:08:22）。
- ⇒ 本件每条「最早出处」**双口径并列给出**（mtime ＋ 件内自陈日期），**0 单独以 mtime 断言定序**。

**诚实交代 3 · 计数工具**：
- 字面计数用 `[IO.File]::ReadAllText()` ＋ `[regex]::Matches()`（含否定前瞻以区分「`0.9`」与「`0.95`」）；文件哈希用 `Get-FileHash -Algorithm SHA256` 取前 12 位小写。

---

## §2 R-2 · 三阈值追源（Q-H6-2）

> 逐条格式：**结论（来源有 / 无）＋ 最早可核出处（件 ＋ SHA-12 ＋ 行号）＋ 原文摘录**。**0 编造任何未在盘上命中的出处。**

### T-1 · 靶点「`0.9` × 2 处语境」（编排件 §2-R-2 拟动作 ①）

**盘上件**：`results/_v3x_p_l_v3_external_spec_2026_09_17.md` ＝ **`6a5b6eb635f0`**（5,769 B / mtime 09-17 11:03:24）

**机械计数**：`0.9` ＝ **2** ｜ `0.95` ＝ **2** ｜ `0.9(?!5)`（独立 `0.9`）＝ **0** ｜ `0.15` ＝ **0** ｜ `R2` ＝ **0** ｜ `R^2` ＝ **0** ｜ `R²`（U+00B2）＝ **3** ｜ `Q` ＝ **6**（与台账 X-25 口径一致）

**逐处语境原文摘录（逐字，0 概括代替原文）**：

- **L91**：`- Spearman < 0.95 → data collapse 假设成立 (≥ 95% 置信)`
- **L92**：`- Spearman ∈ [0.95, 1.0) → 部分破单调, 需补测另一 backbone`

**事实登记**：spec 内 `0.9` 两处**均系 `0.95` 的字符前缀**，且位于 §3.4「期望阈值」的 **Spearman 档位**；spec 内 R² 字面只出现在 L15（§0 做项「算 Spearman + R² + data collapse fit 状态」）、L80（§3.3 标题）、L139（MD 报告模板 §2），**0 任何阈值数字**；`0.15` ＝ 0 ⇒ **spec 内无 Q 阈值**。

**结论**：**「spec 内 `0.9` ＝ R² 阈值」不成立**（该前提本棒已否）。spec 对 R² / Q **只给计算要求，未给判死阈值**。

---

### T-2 · 靶点「Phase 1 `R² ≥ 0.9`」（P1 尺寸标度判死线）

**结论：阈值字面＝有源；其「由来」＝0 命中（无文献 / 无校准 / 无模拟）**

**最早可核出处（mtime 升序）**：

| # | 件 | SHA-12 | 字节 | mtime | 行号 | 原文摘录 |
|---|---|---|---:|---|---|---|
| 1 | `results/_v3x_d0_5_proposal_coze_2026_09_17.md` | **`759c25b21ed4`** | 13,200 | **09-17 11:06:19** | **L84** | `\| P1 尺寸标度 \| log-log \`O(L)\` 线性 Pearson **R²** \| \`R² ≥ 0.9\` 幂律标度成立；\`< 0.9\` 无标度 \| 无标度 → **P-L 证伪**，入 paper §7.2 \|`（表所在节标题 L80：`## §4 期望阈值（预注册三态 + 双重判据，禁止 reassign）`） |
| 2 | `docs/V3X/TRAE_PL_V2_EXPERIMENT_PROPOSAL_2026_09_17.md` | **`4020b1809780`** | 8,849 | 09-17 11:12:54 | **L67** | `\| \`0 < discordant_pairs\` 且 \`collapse_R2 ≥ 0.9\` \| 连续轴坍缩 → **P-L 真实 data collapse**，入 P-L v3 paper \|`（节标题 L60：`## §4 期望阈值（预注册，修正中间档盲区）`） |
| 3 | `results/_v3x_d0_5_aggregation_2026_09_17.md` | **`ddf0d1aa96d2`** | 12,010 | 09-17 13:08:30 | L78 | `\| P1 尺寸标度 \| log-log \`O(L)\` 拟合 R² \| ≥0.9 幂律；<0.9 无幂律 \| … \|` |
| 4 | `results/_v3x_d0_5_proposal_trae_2026_09_17.md` | **`b1c227d54a82`** | 13,254 | 09-20 17:11:14 | L70 | `\| 单参数幂律退路 \`R²(log-log)\` \| \`≥0.9\` 接受幂律标度；\`<0.9\` 连幂律都不成立 → P-L 更强证伪 \| 仅当无控制参数时启用 \|` |

**上游无源（母件已核）**：`results/_v3x_d0_5_experiment_invitation_2026_09_17.md` ＝ **`d8f2b99aa527`**（7,617 B / **mtime 09-17 09:34:32**，09-17 层最早件）
- 机械计数：`0.9` ＝ 3 ｜ `0.95` ＝ 3 ⇒ **独立 `0.9` ＝ 0**；`0.15` ＝ **0**；`0.05` ＝ **0**
- §4 期望阈值表（L76–L81）**只含 Spearman 三档**：L79 `| < 0.95 | data collapse 假设成立 | ≥ 95% 置信，可直接入 P-L v3 paper |`、L80 `| [0.95, 1.0) | 部分破单调 | 需补测另一 backbone |`、L81 `| = 1.0 | 同序单调实证 | P-L 假设证伪 |`
- ⇒ **`R² ≥ 0.9` 相对母件邀请函是新增项**：coze 提案 L89 自陈「邀请函 §4 原表把 Spearman 作为 data collapse 判死依据…P-L 的判死依据应为 `Q` + 幂律 `R²` + β CI 三者分离」。

**依据来源：0 命中**。上述 4 件的阈值表 **0 一句给出 0.9 的文献出处 / 0 校准 / 0 模拟**。

**下游另记（不属本靶点，登记不裁决）**：`R² ≥ 0.9` 作为 **P-L P-C FSS 治理腿** 另见 `results/_v3_recheck_prereg_v1_2026_09_27.md` L84（`| 27 | P-L P-C finite-size scaling | UNVERIFIED | 假证伪 | \`max_R2 = 0.327492\` 恒 < 0.9 → …`）与 `results/_v3_recheck_27_rescript_2026_09_27.md` L19；该层为 **09-27 V4 预登记**，晚于 09-17 实验 ⇒ **不能充当 09-17 的预注册凭证**（事实陈述，0 评价其效力）。

---

### T-3 · 靶点「`Q > 0.15`」（P3 标度塌缩判死线 · 定义公式 / 归一化方式 / 残差类型 / 阈值来源）

**结论：阈值字面＝有源；「Q 的定义公式 / 归一化方式 / 残差类型」＝ 0 可核出处；阈值由来＝ 0 命中**

**（a）阈值字面最早可核出处（同 T-2 四件，行号）**
- coze **`759c25b21ed4`** **L86**：`\| P3 标度塌缩 \| 归一化塌缩残差 **Q** \| \`Q < 0.05\` 塌缩成立；\`0.05–0.15\` 边缘，补一档尺寸；\`> 0.15\` 无塌缩 \| \`> 0.15\` → **P-L data collapse 主张证伪** \|`
- trae **`b1c227d54a82`** **L69**：`\| 塌缩残差 \`Q\`（主曲线拟合，归一化） \| \`Q < 0.05\` 塌缩成立；\`0.05 ≤ Q ≤ 0.15\` 边缘态，补一档尺寸；\`Q > 0.15\` 无塌缩 → **P-L 数据塌缩主张证伪**入 paper §7.2 \| 这是 P-L 的真正判死指标 \|`
- aggregation **`ddf0d1aa96d2`** L80：`\| P3 标度塌缩 \| 归一化残差 Q \| <0.05 成立；0.05–0.15 边缘；>0.15 无塌缩 \| … \|`
- 三处给出的**分档结构一致**（`<0.05` / 中间档 / `>0.15`）；「归一化」二字仅作定语，**0 公式、0 分母定义、0 相对/绝对残差类型声明**。

**（b）Q 的计算层检索：Phase 1 数据件内 0 命中**
- `results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` ＝ **`523b5941c30c`**（16,835 B / mtime 09-17 11:52:29）
  - 顶层 16 键逐字：`target_hypothesis` / `new_backbone_used` / `api_vendor` / `cells_completed` / `cells_breakdown` / `spearman` / `spearman_p_value` / `spearman_definition` / `r_squared` / `r_squared_definition` / `slope` / `intercept` / `fit_status` / `iron_7_compliance` / `_meta` / `per_cell_detail`
  - 机械计数：**`Q` ＝ 0** ｜ **`residual` ＝ 0** ｜ **`normaliz` ＝ 0** ｜ **`formula` ＝ 0**
  - 件内另记：`r_squared` ＝ **−0.77939**；`r_squared_definition` ＝ `linear regression of log(accuracy) vs log(cell-index), quartile-binned (n=4)`；`fit_status` ＝ `PASS`
- ⇒ **判死读数 `Q = 0.1929` 在 Phase 1 数据件内 0 出现**。

**（c）`Q = 0.1929` 的最早可核出处＝脚本硬编码文本行**
- `deposon-sub\_p_l_v3_phase1_finalize_2026_09_17.py` ＝ **`cf8fd1178ab1`**（19,226 B / mtime 09-17 13:35:21）
  - **L119**：`lines.append("- P3 Q=0.1929 > 0.15 → 数据未塌缩到主曲线, P-L data collapse **未通过**.")`
  - L228：`lines.append("| GLM | R^2 ≥0.9 幂律 | Q <0.05 塌缩 | FAIL (0.7447) | FAIL (0.1929) | 主指标 FAIL |")`
  - L238：`lines.append("- **v3 Phase 1 (本轮)**: 沿 Mistral Large 2512 × 4 尺寸 (30/45/60/100) 三态分离 → P1 FAIL (R^2=0.7447 < 0.9), P3 FAIL (Q=0.1929 > 0.15), Spearman 30 档 PASS")`
- ⇒ **`0.1929` 与 `0.7447` 在盘上最早可核处为上述 `lines.append(...)` 硬编码文本**，**0 命中**产生这两个数的计算代码（本棒检索范围内）。

**（d）口径差登记（0 裁定）**：`523b5941c30c` 的 `r_squared` ＝ **−0.77939**（定义：log(accuracy) vs log(cell-index) 四分位分箱，n=4）与判死所用 `0.7447`（单 backbone 30/45/100 三点 log-log 拟合）**属不同构造、0 同值**；两值**同层并存**，本棒 0 判哪条为 Phase 1 权威读数。

**（e）阈值来源**：同 T-2，**0 文献 / 0 校准 / 0 模拟（0 命中）**。

---

### T-4 · 靶点「P-C『双低于阈值』数字」

**结论：数字在实验层＝有源（0.3）；在叙述层＝无源（该句 0 给数字）；且该阈值的规范载体（kill-line 件）不在盘**

**（a）「双低于阈值」字面全树仅 2 命中**
1. 审稿件 `deposon-sub\results\_archive_2026_09_20\review_tech_B1_grok46.md` ＝ **`09784ff172b3`** **L46**（批评语，逐字片段）：`P-C 只写「双低于阈值」，本文从未给出该阈值数字。`
2. `deposon-sub\results\_archive_2026_09_20\_letter_to_coze_wechat_v2_2026_09_18.md` **L43**：`\| **P-C 跨模态幂律** \| **FAIL_H0** \| R²=0.1986/0.2670 双低于阈值; dpath 判定 8/9 (分母 9 模型) \|` ⇒ **该处 0 给数字**

**（b）数字 0.3 的可核出处**
| # | 件 | SHA-12 | 字节 | mtime | 行号 | 原文摘录 |
|---|---|---|---:|---|---|---|
| 1（最早） | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` | **`0d1e88c258aa`** | 9,844 | **09-09 10:55:24** | **L25** | `\| **KT-C1** \| 残余 r vs 维数 d log-log, R²<0.3 死 \| P-C 两相结构 V0 spec(6.3KB) \| η 扫描相变点 ± 20% \| 王老师版"图族回归"vs Mavis 版"参数扫描" — **数据集同源 v21,可双跑** \|` |
| 2 | `docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` | **`79c7321056b8`** | 13,419 | 09-15 15:08:22 | **L109** | `**判死线 (KT_C1_KILL_LINE 77b49c0f8b54)**: \`R^2<0.3 OR b_CI 含 0\` → FAIL_H0 (幂律死)  ` |
| 2b | 同上 | 同上 | 同上 | 同上 | L110 / L111 | 判活线 `**判活线**: \`R^2>0.7 AND b_lo>0\` → PASS_H1 (幂律成立)  ` ／ 灰区 `**灰区**: \`0.3 <= R^2 <= 0.7 AND b 显著非 0\` → GRAY (Mavis 自主扩 cell 重判)` |
| 2c | 同上 | 同上 | 同上 | 同上 | L121 / L133 | `- 条件 1 (R^2<0.3): \`True\` → R^2=0.1986` ／ `- 条件 1 (R^2<0.3): \`True\` → R^2=0.2670` |

**（c）关键缺口 · kill-line 件不在盘**：本棒在 **两树** 对全部 `*.md/*.json/*.py/*.tex` 复算 SHA-256，**`77b49c0f8b54` 0 命中** ⇒ **`R²<0.3` 的规范载体（`KT_C1_KILL_LINE` 件）0 可核，盘上只剩报告层转录**。
- 同件 `docs/V3X/KT_C1_SPEC_V0.md` **MISSING**；在盘的 `docs/V3X/KT_C1_SPEC_V0.1.md` ＝ **`59d8f56347d5`**（31,241 B / 09-09 13:42:23）——`0d1e88c258aa` L25 所指的「P-C 两相结构 V0 spec(6.3KB)」**字节数与该 V0.1 件（31 KB）不符** ⇒ 二者**不同件**（0 断言即该 V0.1）。

**（d）0.3 自身来源**：两件内 **0 文献 / 0 校准 / 0 模拟（0 命中）**。

**（e）同名异物登记（沿盘上既有字面，0 裁决）**：`letters\_v3_calibration_change_note_for_coze_glm_2026_09_27.md` **L295** 逐字：`**「王老师侧 KT-C1」**（幂律主张，**R²=0.0007**，外部源件所载）≠ 本仓 \`KT_C1\`（跨模态 dpath 实验，**R²=0.1986 / 0.2670**，FAIL_H0）= **同名异物**，各归各源**不得混写**`。审稿件 L124 另记「挂点 3 KT-C1 R²=0.0007」为外部件。

---

### T-5 · 附带「第 4 面」（X-36：FPR `<1%` ＋ P-A `STRONG_PASS` 无阈值）——**登记待决，0 并入本棒**

- **本棒 0 追源、0 判定其是否追加为第 4 条阈值面**（PI 择项，编排件 §7-Q1 附带项、批 13 登记件 L69 字面「属台账外新面，须 PI 拍板方入」）。
- **同靶点判定（事实登记）**：三阈值靶点（T-2 / T-3 / T-4）全部落在 **P-L v3 Phase 1 + P-C 幂律 = 09-17 D+0.5 提案层**；`FPR <1%` 与 `STRONG_PASS` 落在 **P-K / P-A = 09-15 → 09-18 D 系列层**（审稿 `09784ff172b3` L45–L46 与 L115、L120 与 P-L 阈值同段并列，但**载体件不同层**）⇒ **不属同一追源靶点 ⇒ 0 并入、0 代裁**。
- 0 追源面（备下游）：`STRONG_PASS` 的盘上字面在 `results/deposon_v2_phase1_60cells_2026_09_10.json` ＝ `A18BBC703B42`（沿 `letters\_v4_distillation_reply_claude_code_2026_09_20.md` L92 转录，**本棒 0 打开该 JSON 复核**，如实标注为转录口径）。

---

## §3 R-4 · P-F 追源（Q-H6-9：档位与数据来源两项存疑）

> **本节只交事实 ＋ 可核出处，0 代裁**。台账 4 问（PARTIAL_PASS 事后改写？/ 6 次 fresh LLM 计划外？/ T-R-A 互斥穷尽？/ 「外部并行账本」复制同件？）逐条给「有源 / 无源」二值事实。

### T-6 · 靶点「`PARTIAL_PASS` 是否为冻结函数值域元素」（X-31）

**结论：不是**（就守恒冻结函数而言）——`PARTIAL_PASS` 在盘上的最早可核载体是**报告层字段字面**，不是冻结函数输出值。

**（a）冻结守恒函数的值域**
- `verifier/audit/conservation.py` ＝ **`4bdec2683f06`**（22,105 B / mtime 09-10 09:29:22；**与 coze 提案 `759c25b21ed4` L96 记的「\`conservation.py\` V0=\`4bdec2683f06\`」逐字一致**）
- L343–348 逐字：
  ```
  if max_dev < PASS_THRESHOLD:
      verdict = 'PASS'
  elif max_dev < GRAY_THRESHOLD:
      verdict = 'GRAY'
  else:
      verdict = 'FAIL'
  ```
  ⇒ 值域 ＝ **{`PASS`, `GRAY`, `FAIL`} 三值；0 `PARTIAL_PASS`**。

**（b）`PARTIAL_PASS` 最早可核出处**
- `docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` ＝ **`0a63824f0805`**（7,352 B / mtime 09-15 14:07:47）
  - **L53**：`- **metric_truth_verdict**: \`PARTIAL_PASS\``
  - L65 复述：`**D_fix2 metric truth verdict**: \`PARTIAL_PASS\``
  - L95 / L96 逐字：`- 等 user 拍板 D_fix2 metric 真值验证 PARTIAL_PASS → 推进王老师 1 周判死` ／ `- 若 user 接受 PARTIAL_PASS verdict + 阈值调整 → 沿 V0.1 沿用 + 王老师 WeChat 选挂点`
  - ⇒ **报告层字段 ＋ 写「等 user 拍板」**，0 冻结函数输出痕迹。

**（c）D7 终档冻结 JSON 内的分布（本棒逐行复核）**
- `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` ＝ **`4505cca79c15`**（2,456 B / mtime 09-16 11:00:06）
  - `P-A_cross_modal_dpath`（L22–59）：**8 PASS ＋ 1 GRAY**（`deepseek-v4-pro` ＝ GRAY）
  - `P-C_two_phase`（L60）：`"FAIL_H0 (幂律死)"`
  - `P-E_3modal`（L61–98）：**6 PASS ＋ 2 GRAY（`kimi-k2.7-code` / `doubao-seed-2.1-turbo`）＋ 1 FAIL（`deepseek-v4-pro`）** ⇒ **该段 0 处 `PARTIAL_PASS`**
  - `P-F_D_fix2_strict`（L99）：`"8+1+0 (PARTIAL_PASS, A channel timing 敏感)"`；`P-F_D_fix2_loose`（L100）：`"8+1+0 (PARTIAL_PASS)"` ⇒ `PARTIAL_PASS` 在本件**只出现在 P-F 两行的自由文本串内**
  - `P-G_V0.1_dH_dE`（L101）：`"≈ 5x (range 4.4-8.0)"`
- ⇒ **P-E 的 `PARTIAL_PASS` 不在冻结 D7 终档 JSON 内**；其在盘上的载体是 `docs/V3X/D7_WANG_TEACHER_WECHAT_PUSH_REQUIREMENTS_2026_09_18.md` ＝ **`935cb6ee3566`**（8,037 B / mtime 09-16 11:08:22）：**L60** `| **P-E physics** | **PARTIAL_PASS** | 9 model: 6 PASS + 2 GRAY + 1 FAIL (deepseek-v4-pro)(沿 user 12:01 拍板 A 接受 + 阈值调整)|`、**L78** `#### 2.1.4 D_fix2 metric PARTIAL_PASS(user 12:01 拍板 A 接受)`、**L128** `- P-E PARTIAL_PASS (沿 A 接受 + 阈值调整)`。

**（d）0 裁声明**：X-31 的二分（「D7 拍板＝事后人工改写」vs「未全过＋经裁决接受＝叠床架屋」）属**档位与纪律判断**，**本棒 0 代裁** ⇒ 交 verdict-keeper。本棒只交上述值域事实（守恒函数值域不含 `PARTIAL_PASS`；P-E 段 0 处该字样）。

---

### T-7 · 靶点「生成层 6 次 fresh LLM 调用：计划内 or 计划外」（X-32）

**结论：数字 6 有源，但**其件内自陈归属＝「D_fix2 worker」而非 P-F 自身 fresh 调用**；P-F 主结果 JSON 内的 fresh 口径是「1 model ＋ 5 cells ＋ 8 复用」，且 **0 记录调用次数**。计划内/计划外 ＝ 0 代裁。

**（a）「6 次」的最早可核出处**
- `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` ＝ **`4ffb21bb6bfa`**（8,526 B / mtime 09-16 11:03:10）
  - 节位置：§1.4「P-F observer（沿 P_F_V0_1_UPGRADE_2026_09_11 SHA-12 b10fae0da66d）」
  - **L69** 逐字：` - 6 fresh volcengine LLM 调用(沿 D_fix2 worker PARTIAL_PASS 实算)`
  - 上下文字面：L65 `- **D1-D3 verdict**:**PASS**(9 model × 5 cells 真实 API 抽样 + 4 BOSS INLINE)`；L66 `- **D7 5 锚终极**:**PASS**(9m×5c 45/45 守恒)`；L68 ` - 9m × 5c 守恒 45/45(T=41 R=0 A=4,residual=0)`
  - ⇒ **括号内自陈其来源是 D_fix2 worker**（D_fix2 属 P-E 侧，见 `0a63824f0805`）
- 同一口径的传播件：`935cb6ee3566` **L61** `| **P-F observer** | **PASS** | 9m × 5c 45/45 守恒 + 6 fresh volcengine LLM + 4 BOSS INLINE 锁住 |`

**（b）三口径对账表（0 混计 · 逐口径分列）**

| 口径 | 值 | 可核出处（件 ＋ SHA-12 ＋ 位置） |
|---|---:|---|
| 报告层「fresh 调用次」 | **6** | `4ffb21bb6bfa` L69（括号自陈「沿 D_fix2 worker」） |
| P-F JSON 内「调用次」字段 | **0 出现** | `fcb5105df0b6` 全文 |
| fresh **model** 数 | **1**（`doubao-seed-2.0-lite`） | `fcb5105df0b6` → `data_sources` 键 `"doubao-seed-2.0-lite"`：`path` ＝ `FRESH_API_CALLS_TODAY_2026-09-15`、`cells_extracted` ＝ `5` |
| fresh **cells** 数 | **5** | 同上 `cells_extracted` |
| **复用** model 数 | **8** | `fcb5105df0b6` → `data_sources` 其余 8 键，路径为 `deposon_volcengine_worker_{a,b,c,d}_2026_09_10.json` 各 `cells_extracted` ＝ `5` |
| 调用授权字面 | `RELAXED (user 11:28 拍板, 仅 volcengine coding-plan)` | `fcb5105df0b6` → `metadata.iron_rule_status.rule_1_0_LLM_calls` |
| P-F 主结果件自身档位字面 | `D1 mid-term (NOT final PASS/FAIL)` | `fcb5105df0b6` → `metadata.phase` |

**（c）P-F 主结果件锚**：`results/deposon_pf_d1_full_9m5c_2026_09_15.json` ＝ **`fcb5105df0b6`**（33,829 B / mtime 09-16 11:01:12）—— SHA-12 与编排件 §2-R-4 所记一致。
- `metadata.method` 逐字：`9 model × 5 cells REAL API sampling (volcengine coding-plan). 8 models from existing 30-cell worker JSONs (2026-09-10 real API sampling); 1 model (doubao-seed-2.0-lite) from fresh API calls (2026-09-15). Pure Python stdlib + hashlib.`
- **0 裁声明**：「授权 ≠ 计划内」是纪律判断（沿编排件 §2-R-4 盘上现状②的既有口径），**本棒 0 代裁**；本棒只交「6 的件内自陈归属 ≠ P-F 自身 fresh 调用」与三口径计数表。

---

### T-8 · 靶点「T/R/A 是否互斥穷尽 ＋ 全文是否定义」（X-37）

**结论：守恒式在盘上有定义、且 `A` 定义为残差项；「互斥穷尽」类断言全库 0 命中；冻结 schema v1 内 0 处 T/R/A 定义**

**（a）守恒层的定义（可核原文）**
- `verifier/audit/conservation.py` ＝ **`4bdec2683f06`** **L73–74** 逐字：
  ```
  def tra_decomposition(pred_value, eta=0.5, g_couple=1.0):
      """T+R+A 三相分解, 严格恒等和=1: T=(1-eta)v, R=eta*g_couple*(1-v), A=1-T-R.
  ```
  ⇒ **`A` 由 `1-T-R` 定义**；同件 L74 标题字面「严格恒等和=1」。
- **0 裁声明**：由此**不能**由本棒断言任何档位结论；「残差 0 由构造保证 ⇒ 9/9 PASS 无信息量」是**推论**，登记为可核机械事实（构造式 + 定义式），**推论与裁断交 verdict-keeper**。

**（b）「互斥 / 穷尽」字面：0 命中**
- `4bdec2683f06` 机械计数：`exhaustive` ＝ **0**、`mutually` ＝ **0**；全树 `*.md/*.json/*.py/*.tex` 检索「互斥穷尽 / mutually exclusive / exhaustive」类断言 **0 命中**。

**（c）冻结 schema v1 内 0 定义**
- `deposon_team/plugins/_v3x_frozen_schema_v1.json` ＝ **`9e99dcc4d920`**（12,919 B / mtime 09-17 10:27:19）
  - 顶层 7 键：`schema_reconcile_doc` / `anchors` / `schema_description` / `schema_version` / `schema_changelog` / `pg_anchors` / `schema_generated_at` / `schema_author`
  - 机械计数：`transmission` ＝ **0**、`reflection` ＝ **0**、`absorption` ＝ **0**、`T_frac` ＝ **0**、`R_frac` ＝ **0**、`A_frac` ＝ **0**、`exhaustive` ＝ **0**、`mutually` ＝ **0**、`PASS` ＝ **0**、`GRAY` ＝ **0**、`PARTIAL` ＝ **0**
  - ⇒ **schema v1 内 0 处 T/R/A 定义、0 处 PASS/GRAY 标签值域**

**（d）盘上两套 T/R/A 字面并存（登记，0 判同构）**
- **连续分解式（守恒层）**：如上 `4bdec2683f06` L73–74；P-A 侧实例 `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` ＝ **`977fe1b48f75`**（19,751 B / 09-15 11:31:34）**L85** 逐字：`T540 + R540 + A540 = 384 + 78 + 78 = 540  (期望 540)  residual = 0`
- **逐 cell 类别标签（P-F 侧）**：`docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md` ＝ **`817efdc2f0ad`**（15,985 B / 09-15 12:15:12）**L93** 逐字：`- 每个 cell 的 \`status_class ∈ {T, R, A}\` 中 T+R+A=1: **✅ 45/45 PASS**`
- ⇒ **两者 0 同构证明、0 互替**；台账 X-37 所指「全文不定义三者」，在**守恒层**已有一处定义（L73–74），在**冻结 schema v1** 仍 0 定义（0 推广为「全仓 0 定义」）。

---

### T-9 · 靶点「384/78/78 与 26/30 是否同一冻结件」（X-38）

**结论：两数在盘上各自可核、且分别挂在不同实验；「是否同一冻结件」＝ 0 可核结清（被审手稿不在盘）**

**（a）384/78/78**
- 唯一实验层出处：`977fe1b48f75` **L85**（见上）——**P-A，9 model × 60 cells ＝ 540**
- 转录处：`docs/V3X/REVIEWER_A_STATIC_AUDIT_2026_09_15.md` ＝ **`575572872e9a`**（34,647 B / 09-15 14:22:04）**L82** 逐字：`- §2.2 v3 9 model × 60 cells 守恒表:\`T540+R540+A540 = 384+78+78 = 540\` (residual = 0) ✅ 整数守恒`
- 另一转录：`docs/V3X/V3X_FULL_EXPERIMENT_DESIGN_2026_09_16.md` ＝ **`3d847f9f3151`**（22,427 B / 09-16 12:28:47）**L132** 逐字：`**9m × 5c 守恒 45/45**(T=41 R=0 A=4, residual=0) — 沿 P-F D1 完整版 协议`

**（b）26/30**
- 最早可核出处：`docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` ＝ **`e4ee3999f7ce`**（26,460 B / mtime 09-16 11:01:12）
  - **L9** 逐字：`> **D 路径状态**: ✅ **VERDICT = PASS(25/30 = 83.3%)**,但**净 -1 vs no-RAG baseline 26/30 = 86.7%**`
  - **L273** 逐字：`| **no-RAG** | \`doubao-seed-2.0-lite\` 直答 | **26/30** | **86.7%** | \`deposon_doubao_seed_2_0_lite_30cells_2026_09_10.json\` (9model JSON) |`
  - **L357** 逐字：`| **P-A 均衡稳定化** | 2 model 26/30 | 25/30 ≈ 0.833 ∈ [0.80, 0.90] | **锁定** V3X 默认(doubao-seed-2.0-lite 或 glm-5.3) |`
- 同值双源互证：`docs/V3X/P_D_B3_MERKLE_22_CAPTION_VERIFICATION_2026_09_16.md` **L133**／**L135** 逐字：`- "doubao-seed-2.0-lite (26/30=0.867) + glm-5.3 (26/30=0.867) form the v2 equilibrium cluster at exact T_frac=0.867. …"` ／ `主源 9 model 表中 doubao-seed-2.0-lite 与 glm-5.3 的 T_frac = 0.8667 (26/30), 与交叉源 0.867 重合 — 双源互相印证。`
- 数据实体：`results/deposon_volcengine_9model_30cells_2026_09_10.json` ＝ **`58ab335ca341`**（4,894 B / 09-16 11:01:12）
- 审稿侧的对照（`09784ff172b3` L115／L116）要求「外部账本满长哈希与 diff」——**该 diff 件不在盘**（见下）

**（c）0 可核结清的原因（诚实交代）**
- 审稿件 `09784ff172b3` **L64–L67**（M7）逐字要点：位置＝`§4.7「外部账本侧：T＝384＋R＝78＋A＝78＝540，残差 0」；§4.1 同一组数；双主线 \`T＝26/30\` 与本文 \`new_30：T＝26/R＝4\` 相同`；修改要求＝`披露数据是否同一冻结件。若是，删除「外部／并行」表述；若否，提交两边原始账本的满长哈希与 diff。`
- 本棒在两树检索「外部账本 / 并行账本 / 外部研究者」，**命中仅 2 处**：审稿件自身 L64–L67，＋ 编排件 `d911674e68cf` 的转录 ⇒ **被审手稿（§4.1 / §4.7 所在件）0 命中，不在盘**。
- ⇒ **0 从「同值」推「同件」，亦 0 反推**；披露与否属 doc-writer / verdict-keeper 面。

---

## §4 「来源有 / 无」双列表（回执表 · 逐靶点二值）

| 靶点 | 阈值/数字 **来源** | **定义 / 载体 / 归属** | 最早可核出处（件 ＋ SHA-12 ＋ 行号） |
|---|---|---|---|
| T-1 spec 内 `0.9` × 2 | **有**（= `0.95` 的 2 处前缀，Spearman 档位） | — | `results/_v3x_p_l_v3_external_spec_2026_09_17.md` **`6a5b6eb635f0`** L91／L92 |
| T-2 `R² ≥ 0.9` 字面 | **有** | **由来无**（0 文献/0 校准/0 模拟） | `results/_v3x_d0_5_proposal_coze_2026_09_17.md` **`759c25b21ed4`** L84（09-17 11:06:19） |
| T-2 上游母件（邀请函） | **无**（`0.9`/`0.15`/`0.05` 全 0 独立命中） | — | `results/_v3x_d0_5_experiment_invitation_2026_09_17.md` **`d8f2b99aa527`** L76–L81（09-17 09:34:32） |
| T-3 `Q > 0.15` 字面 | **有** | **由来无** | 同上 `759c25b21ed4` L86 ／ `b1c227d54a82` L69 ／ `ddf0d1aa96d2` L80 |
| T-3 Q 的**定义公式 / 归一化 / 残差类型** | **无**（全树 0 命中） | Phase 1 数据件内 `Q`＝0／`residual`＝0／`normaliz`＝0 | （负证据件）`results/_v3x_p_l_v3_mistral_large_2512_20260917_115049.json` **`523b5941c30c`** 顶层 16 键 |
| T-3 `0.1929` / `0.7447` **产生代码** | **无**（0 命中计算代码） | 最早可核＝脚本硬编码文本行 | `deposon-sub\_p_l_v3_phase1_finalize_2026_09_17.py` **`cf8fd1178ab1`** L119／L228／L238（09-17 13:35:21） |
| T-4 P-C「双低于阈值」数字 | **有（0.3，实验层）** | **手稿层无**（该句 0 给数字）；**kill-line 件不在盘** | `docs/V3X/D0_FREEZE_PREP_2026_09_09.md` **`0d1e88c258aa`** L25（09-09 10:55:24）；`docs/V3X/P_C_D1_D3_REPORT_2026_09_15.md` **`79c7321056b8`** L109／L121／L133 |
| T-4 `KT_C1_KILL_LINE 77b49c0f8b54` 件 | **无**（两树 0 命中） | — | （负证据）转录见 `79c7321056b8` L109 |
| T-6 `PARTIAL_PASS` 值域 | **不在冻结函数值域**（守恒函数 ＝ PASS/GRAY/FAIL） | 最早载体＝报告层字段 | 值域：`verifier/audit/conservation.py` **`4bdec2683f06`** L343–348；载体：`docs/V3X/D_FIX2_METRIC_VERIFY_REPORT_2026_09_15.md` **`0a63824f0805`** L53 |
| T-6 P-E 的 `PARTIAL_PASS` 在冻结 D7 终档件内 | **无**（P-E 段 0 处） | 载体＝D7 requirements 报告 | `results/d7_5anchor_60cells_9model_verdict_2026_09_18.json` **`4505cca79c15`** L61–98；`docs/V3X/D7_WANG_TEACHER_WECHAT_PUSH_REQUIREMENTS_2026_09_18.md` **`935cb6ee3566`** L60／L78／L128 |
| T-7 「6 次 fresh LLM 调用」 | **有** | **件内自陈归属＝「沿 D_fix2 worker」**；P-F JSON 内调用次 0 出现 | `docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md` **`4ffb21bb6bfa`** L69（09-16 11:03:10） |
| T-7 P-F fresh 口径 | **有** | 1 model ＋ 5 cells ＋ 8 复用 | `results/deposon_pf_d1_full_9m5c_2026_09_15.json` **`fcb5105df0b6`** → `data_sources` |
| T-8 T/R/A **守恒层定义** | **有**（`A=1-T-R`） | 「互斥穷尽」断言 **0 命中**；schema v1 **0 定义** | `4bdec2683f06` L73–74；负证据 `deposon_team/plugins/_v3x_frozen_schema_v1.json` **`9e99dcc4d920`** |
| T-9 `384/78/78` | **有** | 挂 **P-A 540 格守恒** | `docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md` **`977fe1b48f75`** L85 |
| T-9 `26/30` | **有** | 挂 **no-RAG 30 格基线通过率** | `docs/V3X/DPATH_CROSS_MODAL_2026_09_10.md` **`e4ee3999f7ce`** L9／L273／L357 |
| T-9 两者**是否同一冻结件** | **0 可核结清**（被审手稿不在盘） | — | 负证据：两树「外部账本／并行账本／外部研究者」仅命中审稿件 `09784ff172b3` L64–L67 ＋ 编排件转录 |
| T-5 附带第 4 面（FPR `<1%` ＋ STRONG_PASS） | **本棒 0 追源（登记待决）** | 层位不同 ⇒ 0 并入 | 派工口径：编排件 `d911674e68cf` §7-Q1 附带项 ＋ `results/_v5_confirm_b13_decisions_register_2026_09_29.md` L69 |

---

## §5 0 判据自陈（本棒**未**做的事，逐条显式）

1. **0 设阈值、0 改判据、0 跑实验、0 补写来源**：本件全部数字 ＝ 盘上既有字面（`0.9` / `0.95` / `0.15` / `0.05` / `0.3` / `0.7` / `0.1986` / `0.2670` / `0.7447` / `0.1929` / `−0.77939` / `384` / `78` / `26/30` / `45/45` / `T=41 R=0 A=4` / `51/60` / `6` / `1` / `5` / `8`）**或本棒机械计数**（0 命中次数），**0 引入任何盘上未有的数值**。
2. **0 代裁**：① `Q>0.15` / `R²≥0.9` / P-C `0.3` 三阈值**是否降为探索性**（PI 择项，编排件 §7-Q1）；② X-31 二分（事后改写 vs 叠床架屋）；③ 6 次调用计划内/计划外；④ T/R/A 推论是否使 9/9 PASS 无信息量；⑤ P-F 是否降 consistency 档 —— **五条全部交 verdict-keeper / PI，本棒 0 表态**。
3. **0 合并两条 R² 读数**（`523b5941c30c` 的 −0.77939 与 finalize 脚本的 0.7447）：并列登记。
4. **0 触发阈值变更程序**：本棒**未改任何切点** ⇒ 编排件 §5.3 二次确认程序**0 触发**。
5. **0 动既有件**：本棒对两树**0 写入、0 改名、0 删除**；产出**仅本件 1 件**。
6. **0 读 key（R4）**：本棒**0 读取任何 key / 凭据文件**；`fcb5105df0b6` 的 `auth_note` 字段本棒**只记录「该字段存在」这一事实，0 转写其字面**（该字段含 key 片段前缀）。
7. **0 联网**：本棒 **0 网络请求、0 外部检索** ⇒ 全部结论只落在盘上字面；「0 文献 / 0 校准」类判断均为**盘上 0 命中**事实，**0 拿相似文献顶替**。
8. **skill 0 加载**：派工单**未指定 skill 名** ⇒ 本棒 **0 加载任何 skill**，纪律锚 ＝ 派工单字面 ＋ 既有件惯例（SHA-12 小写 12 位、附来源件行号、0 遗漏、署名如实、既有件 0 触动、落盘后实测复核）。
9. **0 冒充**：本件署名 worker；审稿 / 报告源件（Trae code / Coze / dsv4pro / grok46 / qwen3max / GLM 双审）的字面**均以「转录」标注**，**0 以其名义出证**。

---

## §6 老实交代（failures & limitations）

1. **0 逐行通读大件**：本棒**定向检索 + 定点读取**，**0 逐行通读** `e04a46b02d13`（128,760 B）、`d911674e68cf`（48,292 B）、`4ffb21bb6bfa`、`4505cca79c15`（全 103 行已读）、`fcb5105df0b6`（只读 metadata / data_sources / asset_info 三块，其余 0 逐行）。
2. **被审手稿不在盘 ⇒ T-9 无法结清**（详见 §3 T-9(c)）：X-38 的「同一冻结件」问题**结构上不可由本棒回答**。
3. **`77b49c0f8b54`（KT_C1_KILL_LINE）件不在盘** ⇒ `R²<0.3` 只剩报告层转录；`docs/V3X/KT_C1_SPEC_V0.md` 亦 MISSING（详见 §2 T-4(c)）。
4. **`Q = 0.1929` / `R² = 0.7447` 的产生代码 0 命中**：本棒**0 定位**到计算这两个数的函数；负证据是「Phase 1 数据 JSON 内 `Q`／`residual`／`normaliz` 全 0」＋「最早可核处为 `lines.append(...)` 硬编码文本」两条。**0 断言二者无来源，只登记 0 可核出处。**
5. **`STRONG_PASS` 的载体件 `A18BBC703B42` 本棒 0 打开**：该处为沿 letters 面转录口径（见 §2 T-5），**未独立复核**。
6. **6 件审稿 / 报告源件在 sibling 仓**：本棒只读该目录，**0 写入**；若下游要求「仓内可核」，须由 evidence-auditor 决定是否登记跨仓路径口径（**本棒 0 自行裁定**）。
7. **mtime 与件内日期系统性不一致**（详见 §1 诚实交代 2）⇒ 本件「最早」一律双口径并列，**0 单以 mtime 定序**。
8. **本棒 0 复核 `d7_5anchor_60cells_9model_verdict_2026_09_18.json` 的 P-A 段与 `asset_info` 以外字段**；P-E 段已逐行复核（L61–98）。
9. **PI 批 13 登记件 L69 逐字**已引（`results/_v5_confirm_b13_decisions_register_2026_09_29.md`），但**本棒 0 打开该件复核上下文**（沿编排件 §8-5 的同样口径：批 6 登记册盘上 0 命中、事实来源为派工单字面）——**本棒对批 13 登记件的存在与路径未独立核验**。

---

## §7 复算与自报（本件落盘后实测）

| 项 | 值 |
|---|---|
| 本件路径 | `results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md` |
| 引用控制件（本棒复算） | 编排件 `d911674e68cf` ＝ MATCH ｜ 台账 `e04a46b02d13` ＝ MATCH |
| 既有件触动 | **0**（两树 0 写入 / 0 改名 / 0 删除） |
| 行尾 | LF（沿同目录既有 V5 件行尾实测：编排件 CRLF=0 / LF=327） |
| 产出件数 | **1 件 `.md`** |

| 本件 SHA-12 | **自指不可内嵌**（写入哈希会改变哈希）⇒ 实测值随本棒收口**回执**给出，核验方以 `Get-FileHash results/_v5_paper_remedy_r2_r4_sourcetrace_2026_09_29.md -Algorithm SHA256` 取前 12 位对回 |

**—— worker · deposon V4 论文面补救线 · 棒 1 追源 · 2026-09-29 · 0 设阈值 0 改判据 0 跑实验 0 代裁**

