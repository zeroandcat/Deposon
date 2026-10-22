# 16 碰撞件之覆盖必要面核证件 ｜ 2026-10-18

- 棒：evidence-auditor（数据修订／资产处置之上位职责）
- 上位令：PI 2026-10-18 11:5x「核实 16 碰撞件是否需要覆盖」
- 标的登记件：`results/_thirdparty_collision_16_register_kimi_2026_10_18.md`（3,959 B·SHA-12 `58c0b02114ae`·主代理亲算）
- 判据冻结件：`.tmp/_16_overwrite_necessity_criteria_freeze_2026_10_18.md`（4,440 B·SHA-12 `be89bb020d7a`·0 BOM·0 CR）——**先于任何比对落盘**（FTFB），事后 0 调
- 网络面：匿名只读（`git ls-remote`／`raw.githubusercontent.com`／`api.github.com`）｜⛔0 远端写、⛔0 经手凭据｜**0 实验**

---

## 0 结论摘要（逐件三分支计数）

| 分支 | 件数 | 件号 |
|---|--:|---|
| **不需覆盖**（远端版应存） | **6** | #8 #9 #10 #11 #13 #14 |
| **需覆盖**（本地为权威、远端为失真／旧） | **9** | #1 #2 #3 #4 #5 #6 #7 #12 #15 |
| **须 PI 逐件裁**（判据互斥） | **1** | #16 |
| 合计 | **16** | — |

> ⛔ 本件**0 代裁**：三分支皆为证据面与推荐，**裁归 PI**。⛔0 闭既有 KD、⛔0 落五终判、⛔0 宣告任何段毕、⛔0 执行覆盖。

---

## 1 仪器自审（测量仪器自身即误差源）

**首轮 16/16 raw 取回全数 HTTP 404。** 按冻结判据 §3「⛔0 以 raw 404 反推『件不存在』——须同核 tree 面」，先行审仪器：

| 探针 | 实测 |
|---|---|
| `raw .../HEAD/README.md` | **HTTP 200 · 7,279 B** |
| `raw .../HEAD/LICENSE` | **HTTP 200 · 1,085 B** |
| `api /repos/zeroandcat/Deposon` | HTTP 200（`private=False`·`default_branch=main`） |
| `api .../git/trees/HEAD?recursive=1` | HTTP 200 · 3,938 entries · `truncated=False` |

⇒ 404 **非传输故障、非鉴权故障**，系路径实存性问题。**仪器判为可用**。

**破案**：远端实存路径为 `_september_workspace/<rel>`——仓根另有全工作区镜像目录 `_september_workspace/`（HEAD 树内 3,324 blobs），而登记件之 `rel` 记的是**本地区相对路径**（`results/…`、`tools/…`），其「remote git sha1」实测自 `_september_workspace/` 前缀路径。按登记件字面 `rel` 直取 ⇒ 16/16 404；按实存路径取回 ⇒ **16/16 命中且 git blob SHA-1 逐件相符**。

⚠ 此为登记件之**引用路径规范缺陷**（KD-23），**非其读数之失**：登记件所载 16 组 remote sha1 本身**准确无误**。

---

## 2 取件时效面与指纹核验

| 项 | 实测值 |
|---|---|
| live HEAD（`git ls-remote` 复测） | `7a5093f939b5e69d9b50e94a94cb2a7d74691bf8` |
| 登记件所载基线 | `74c7d769`（10-12 快照 · bob · 2026-10-12T13:13:26Z） |
| R2 终态 | `f44996fbfd9f`（R2 wave 4/4 · 2026-10-12T04:36:59Z） |
| 仓 `pushed_at` | 2026-10-18T03:40:01Z（＝11:40 CST·本次核证前约 20 分钟） |

- live HEAD 与主代理 10:5x 读数**一致**；依冻结判据 §3 两值**并列登记**，⛔0 以后者覆前者。
- 登记件序 0「16 件远端 sha 相对读数 0 漂移」——**本棒独立复测为真**：16 件远端 SHA-1 于 `74c7d769`、`7a5093f9` **两面逐件相符**，`remote bytes` 亦 **16/16 相符**。
- 本地面：两区在位面实测 **16/16 在位**；git blob SHA-1 复算 **16/16 MATCH** 登记值；跨区（REPO↔SUB）**0 重复身份**。
- 哈希口径：`hashlib`（`blob <len>\0<content>` ＋ SHA-1）＋ SHA-256 取 SHA-12；⛔0 内建 `hash()`。

---

## 3 逐件证据面与推荐

### 组 A ＝ 锚件引用值之差（#1 #2 #3 #4 #5 #6 #7 #12 #15）→ **需覆盖 9 件**

**唯一差异面**：所引锚件 `results/_d1_ruling_and_s3_transition_2026_10_01.md` 的指纹字面——本地作 `dc9cb0e02922`／28,370 B，远端作 `66f900b7598b`／28,352 B。**16 件之任何命题、判定、数值、节段 0 改动**。

**锚件真值实测**：

| 面 | SHA-12 | bytes |
|---|---|--:|
| 本地 SUB 在位 | `dc9cb0e02922` | 28,370 |
| 远端 `_september_workspace` @ `7a5093f9`（live HEAD） | `dc9cb0e02922` | 28,370 |
| 远端 @ `74c7d769` | `dc9cb0e02922` | 28,370 |
| 远端 @ R2 终态 `f44996fbfd9f` | `dc9cb0e02922` | 28,370 |
| **全盘搜 `66f900b7598b` 之实体** | **1 命中** | 28,352 |

`66f900b7598b`(28,352 B) 之唯一实体：`〔归档件引用·未上传:_d1_ruling_and_s3_transition_2026_10_01.md.remote_2026_10_12〕`（10-12 远端版冻结件）。

⇒ **远端 9 件所引之指纹，在其自身远端树中已无对应实体**（本地与远端树皆为 `dc9cb0e02922`）；本地 9 件所引与双区现态**相符**。

| # | rel | 区 | 行数 L/R | +/− | ratio | 一行之据 |
|--:|---|:-:|---|--:|--:|---|
| 1 | `results/_kd_19_ambiguous_tags_rejudge_rewrite_register_2026_10_10.md` | SUB | 230/230 | +14/−14 | 0.939 | 4 hunk 全为锚件 token `dc9cb0e02922`→`66f900b7598b`，无一句命题改 |
| 2 | `results/_kd_heteronym_classification_disposition_2026_10_09.md` | SUB | 311/311 | +6/−6 | 0.981 | 5 hunk 同 token，另含字节数 28,370→28,352 |
| 3 | `results/_kd_resolvability_and_optional_experiments_2026_10_09.md` | SUB | 476/476 | +1/−1 | 0.998 | 单 hunk 单 token |
| 4 | `results/_kd_writing_convention_guidance_2026_10_09.md` | REPO | 193/193 | +4/−4 | 0.979 | 4 hunk 同 token ＋ 字节数 |
| 5 | `results/_kv3s_3_2_terminal_verdict_2026_10_01.md` | SUB | 307/307 | +5/−5 | 0.984 | 5 hunk 同 token ＋ 字节数 |
| 6 | `results/_mini_round_6_7_settlement_register_2026_10_01.md` | SUB | 434/434 | +1/−1 | 0.998 | 单 hunk 同 token ＋ 字节数 |
| 7 | `results/_s3_d1_rulings_supplement_register_2026_10_01.md` | SUB | 280/280 | +7/−7 | 0.975 | 6 hunk 同 token ＋ 字节数 |
| 12 | `results/_t1_substrate_gap_precondition_2026_10_01.md` | REPO | 203/203 | +3/−3 | 0.985 | 3 hunk 同 token ＋ 字节数 |
| 15 | `results/_verdict_pack_d_prep_2026_10_01.md` | SUB | 429/429 | +1/−1 | 0.998 | 单 hunk 单 token |

**判读（依冻结判据 §2）**：① 本地为在册原件，其引用与双区现态相符；② 远端**仅失真**（过时引用，非版本回退）；③ 属 ③-2 第三方面——16 件**不在** 447 件 R2 域内，且此 9 件远端版**无任何脱敏内容差**（远端之劣不在脱敏面）⇒ 与 R2 体例无冲突。
⇒ **推荐：需覆盖**（证据面）。⚠ 域级警示见 KD-25。

### 组 B ＝ 绝对路径／根之差（#8 #9 #10 #11 #13 #14）→ **不需覆盖 6 件**

**唯一差异面**：本地硬编码机-specific 绝对路径／根，远端为区相对路径。

| # | rel | 区 | 行数 L/R | +/− | 差异 |
|--:|---|:-:|---|--:|---|
| 8 | `results/_s4_heldout_sampling_seedprime_extractor_2026_10_10.py` | SUB | 440/439 | +5/−6 | `REPO_RESULTS = r"〔目录引用·未上传:results〕"` → `RESULTS` |
| 9 | `results/_s4_heldout_sampling_seedthird_extractor_2026_10_11.py` | SUB | 842/841 | +11/−12 | 同上（9 处引用改写） |
| 10 | `results/_s4prime_readings_runner_2026_10_11.py` | SUB | 464/463 | +7/−8 | `REPO_RESULTS = pathlib.Path(r"〔本地绝对路径·脱敏略:�〕��")` → `RESULTS` |
| 11 | `results/_s5doubleprime_five_lines_runner_2026_10_11.py` | SUB | 592/591 | +5/−6 | 同上 ＋ `EXECUTOR` 归位 |
| 13 | `results/_v3_recheck_05_executor_2026_09_28.py` | SUB | 735/734 | +6/−7 | `REPO_ROOT = Path(r"_repo_mirror")` → `REPO`（含 `relative_to` 根） |
| 14 | `results/_v3_recheck_05_result_2026_09_28.json` | REPO | —（JSON·17 top keys 两面同） | 50 B | 4 处 `path` 剥 `deposon-repo/` `deposon-sub/` 前缀；一处 `exists: true→false` |

**#14 之 `exists` 差之定性**：`conservation_py` 归档回退路径 `_archive_deposon_2026_09_17/verifier/audit/conservation.py`——实测 **REPO 区 ABSENT**、**SUB 区 EXISTS**。故 `exists` 之差系**根差异（`REPO_ROOT.parent` vs `REPO`）之派生结果**，非独立内容争议。

**判读**：① 远端为 as-uploaded 之 R2 合规形态（相对路径）；② 远端**不含**本地所无之内容——其相对路径化恰为脱敏之体现；③ 提交面证据：commit `44d7b302f444`(2026-10-12T04:36:51Z) 与 R2 终态 `f44996fbfd9f`(04:36:59Z) 之题名均含「**abs-path correction** ＋ desensitiz…」——**R2 体例明载绝对路径纠正**。以本地覆盖 ＝ 将 `〔本地他区引用·未上传:�〕��` 复推入上传面 ＝ **逆转 R2 体例**。
⇒ **推荐：不需覆盖**（远端版应存）。附带资产缺陷登记见 KD-26。

### 组 C ＝ #16 `tools/exp_harness.py` → **须 PI 逐件裁**

| 面 | 值 |
|---|---|
| 本地（REPO） | **45,548 B · 803 行** · docstring 载 V0.2→**V0.3**(10-15 T5 生成族)→**V0.4**(10-15 T3 可答化)→**V0.5**(10-16 素材扩充＋Mixed 哨兵)→**V0.6**(10-17 K-C3 键面遮蔽) |
| 远端 `_september_workspace/tools/` | **10,090 B · 280 行** · 末次改动 `00e1978c6c53`（**2026-09-20**「Phase 1: mirror all 701 September files」） |
| diff | L803/R280（**d−523 行**）· +20/−543 · ratio **0.480** |

**判读之互斥点**：
- 判「**需覆盖**」之依据成立：远端为 **4 周前之镜像**，V0.3–V0.6 全块缺失（含 10-17 `K-C3` 键面遮蔽臂 `build_decision_observation`／`render_observation_text`／`MASKED_KEY_FIELDS`／`ExperimentHarness(mask_key_fields=…)`），本地为在册工作版（承 `_t5_anchor_drift_authorized_register_2026_10_15.md`、`_material_expansion_drift_authorized_register_2026_10_16.md`、`.tmp/harness_mask_kill_freeze_2026_10_17.json` 之登记面）。
- 判「**不需覆盖**」之依据亦成立：本地版**自身仍含**机-specific 绝对路径（L108 `〔幽灵引用·原件已缺席·未上传:deposon_v20_baselines.json〕`、L109 `…_v21_gtformal.json`），以本地直覆 ＝ 将绝对路径推入上传面，**与 R2「abs-path correction」面冲突**。
- 故**两判据互斥、正解非「直覆」**——应为「以当前版为准 ＋ 先出脱敏版」，然该取舍（是否脱敏、覆盖抑或另推）**属 PI 裁量**。
⇒ **推荐：须 PI 逐件裁**。⛔ 本棒 0 代裁、0 代取舍。

---

## 4 新出 KD 登记（编号域实测 0 占用）

> 编号域实测：`results/` 全件 `.md`／`.json`／`.txt`／`.py` 扫描，`KD-<N>` 形式之 N 已占用 ＝ {1…22, 215, 720, 1494}；**23 起 0 占用**。本件新出取 **KD-23 … KD-27**，⛔0 闭任何既有 KD。

| KD | 面 | 登记 |
|---|---|---|
| **KD-23** | 引用路径规范（远端前缀缺失） | 登记件之 `rel` 记本地区相对路径，远端实存为 `_september_workspace/<rel>`；按字面 `rel` 直取 raw 得 **16/16 HTTP 404**。登记件之 16 组 remote sha1 本身准确（0 读数之失），**失者在路径表述之可执行性**。建议后续登记件一律双列「本地区 rel」与「远端 rel」。 |
| **KD-24** | 同一性（CONFLICT／SAME_IDENTITY） | HEAD 树内：#5、#7 各有 **2 份副本且哈希相异**——canonical 副本载远端哈希（`e59531f0…`／`17ba92d2…`），`_september_workspace/results/_glm_evidence_unpacked_2026_10_13/_september_workspace/results/` 内副本载**本地**哈希（`826ea327…`／`d60daddd…`）⇒ **CONFLICT**（同名不同哈希，登记不覆盖）。#14 有 2 份副本、哈希**同为** `948ae3ec…` ⇒ **SAME_IDENTITY**（不重复计数）。其余 13 件 HEAD 树内单副本。 |
| **KD-25** | 域级漂移（单件处置不足） | 组 A 之锚件引用漂移**非 16 件独有**：本地全盘有 **115 件**引用字面 `66f900b7598b`。故 9 件虽逐件证据面支持「需覆盖」，**正解宜域级处置**（统一回填 `dc9cb0e02922` 或另立新锚），单件覆盖仅为局部。处置取舍属 PI。 |
| **KD-26** | 资产缺陷（跨区绝对路径依赖） | #8 #9 #10 #11 位于 **SUB 区**却硬编码指向 **REPO 区** `〔目录引用·未上传:results〕`——跨区绝对路径依赖；#16 两面**均**含 `〔幽灵引用·原件已缺席·未上传:�〕��`（L108/L109）。**缺陷层登记，⛔0 代修**（涉及运行语义，超本棒射程）。 |
| **KD-27** | 定性勘误（登记件前提） | 登记件将 16 件定性为「**第三方改动件**」（远端＝第三方之工作、0 覆盖）。实测时序与之**不合**：15/16 件之远端版为**较早之 as-uploaded 形态**（#8–#11 推于 10-12T03:19Z、#13 于 09-30），而本地版 mtime 更晚（10-12 23:53 → 10-14 14:07）；**惟 #16 例外**（远端为 09-20 镜像，远端更旧）。故「远端＝第三方改动」与「远端＝未随本地更新之旧镜像」二读并存。**定性之权属 PI，本棒 0 代裁**——仅登记，不翻案。 |

---

## 5 0 触动自证与如实交代

**0 触动**：本棒**未修改任何既有件**。新增仅两类——
- 交付件 1：`results/_thirdparty_16_overwrite_necessity_2026_10_18.md`（本件）
- 临时件：判据冻结件 1（`.tmp/_16_overwrite_necessity_criteria_freeze_2026_10_18.md`）＋ 核证脚本／读数 JSON 若干（`.tmp/_16_*`）

⛔ 未触碰 V1–V3 资产、⛔ 未回改冻结件、⛔ 未写仓外目录（`〔归档区〕` 与 `deposon-sub` **只读**）、⛔ 0 远端写。

**如实交代（未软化）**：
1. **登记件之 rel 不可直接执行**——按其字面取件 16/16 404。本棒系经全树 basename 搜索方定位实存路径；**若仅依登记件执行，将误判 16 件为远端缺失**。
2. **组 A 之 9 件「需覆盖」之推荐有域级保留**（KD-25）：漂移为仓全域现象，9 件单覆非正解。
3. **#16 之判读为互斥**，本棒 0 代裁；「以当前版为准 ＋ 先出脱敏版」乃建议之建议，**未经 PI 裁不得执行**。
4. **远端沿革面不完整**：`_september_workspace/tools/exp_harness.py` 之 commit 题名仅一（09-20 mirror），故「远端为何停在 09-20」之成因**未测得**，如实列为未知。
5. 本棒**0 实验**、⛔0 主张第三方改动之内容当否（仅出存在性／指纹／差异性质之证据面）。
6. R4：**0 密钥明文**入本件、0 入 prompt／JSON／log。

---

*核证完毕 ｜ 落盘即字节级自报见派工回报 ｜ 裁归 PI*
