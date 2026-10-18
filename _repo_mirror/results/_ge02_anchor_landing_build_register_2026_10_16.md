# G-E02 **5 锚落位件** 造件登记件 · GE02-ANCHOR-LANDING-BUILD · 2026-10-16

> ## ⚠⚠ 状态：**候 PI 核准**（`pending_PI_approval`）——⛔ **0 径行采认** · ⛔ **0 入锚面** · ⛔ **0 自签生效**
>
> 本棒产出**另立两件**，一字未回改任何既有件。**本件⛔ 非** spec L22 所指之 `verifier/handoff/P_B_V0_anchors_sha256_12.json`（该件本棒实测 `Test-Path=False`）⇒ **S-1 之③「5 锚落位件补齐」之闭候 PI 裁其读法**（见 §7 KD-4）。
>
> **棒别**：GE02-ANCHOR-LANDING-BUILD（①段 · PI 第四批卡裁答之执行 · worker 产出执行棒）｜**署名**：`worker`｜**件日**：2026-10-16｜**主仓**：`_repo_mirror`

---

## §1 交付物（两件 · 全另立）

| # | 路径 | SHA-12 | bytes | 性质 |
|:-:|:--|:--|--:|:--|
| **1** | `results/ge01_prereg_5anchor_landing_v1.json` | **`5518346a5e61`** | **50,650** | **G-E02 验收结果 JSON**（5 锚落位记录 ＋ 自检向量面） |
| **2** | `results/_ge02_anchor_landing_build_register_2026_10_16.md` | **（自指悖论·⛔ 0 自载）** | **（同）** | **造件登记件**（本件） |

> 📌 **落盘前撞名核查**：两件落盘前 `Test-Path` 均 ＝ **`False`**；全仓递归同名 glob **0 命中** ⇒ **0 覆写任何既有件**。

---

## §2 造件之方法（⛔ 0 转述他件自报 · 逐字回读源件后落笔）

1. **5 锚现版之认定**：glob 定位 `results/_ge01_prereg_5anchor*.json` 得 v1／v2／v3 三版 ＋ 两锁记件；**v3 为现版**（`0c269b9558da` / 35,911 B · 逐字载 v2 之 superseded 面及 lineage）。**5 锚之 field/value 面以 v3 JSON 为准**，本棒逐字沿录未动。
2. **实测复算**：对 5 锚之 **9 个实体文件**逐件 `hashlib.sha256(file bytes).hexdigest()[:12]`（stdlib hashlib；**built-in `hash()` 从未使用**）＋ `os.path.getsize` 取 bytes ＋ mtime 时点新鲜性留痕。
3. **自检轨实跑**：`python tools/distortion_calculator.py --self-test`（**纯本地 · 0 网络 · 0 LLM calls · calculator 铁律 1 自载**）——结果照录（§5）。
4. **阴性结论三通道**（§6）：文件名模式 ＋ 内容逐字节 SHA-12 直算 ＋ 字面转录/实体之分面。
5. **键名口径**：新出件一律 `anchor_status` 主键 ＋ `status_detail` 承载明细（沿 `_anchor_status_naming_note_2026_10_16.md` `d042dd66e3c7` 之 `N-1`／`N-4` **已裁口径**）。

---

## §3 源件指纹（**本棒直算** · 逐件 `Get-FileHash` ＋ Python 双通道）

| SHA-12 | bytes | 源件（`results\` 除注明） | 本棒取用面 |
|:--|--:|:--|:--|
| **`0c269b9558da`** | **35,911** | `_ge01_prereg_5anchor_v3.json` | **5 锚 field/value/status 面之正身**（逐字沿录） |
| `4b020eb04605` | 10,701 | `_ge01_prereg_5anchor.json`（v1） | lineage 沿录（⛔ 0 动） |
| `f06313373fc6` | 21,629 | `_ge01_prereg_5anchor_v2.json`（v2） | lineage 沿录（⛔ 0 动） |
| `deea2ccb2643` | 17,885 | `_ge01_prereg_5anchor_v3_lock_register_2026_10_15.md` | 锁之载体外置纪律之先例（⛔ 0 动） |
| **`410a12482eef`** | **40,611** | `tools/distortion_calculator.py` | **自检轨被调件 · 锚⑤实体**（⛔ 0 改一字） |
| **`7551c47d3ece`** | **35,956** | `_ge01_epsilon_sensitivity_grid_design_r1_2026_10_13.md` | **§2-2 自检向量期望值面**（20／10 · ε=0.1） |
| **`890e923b0f9d`** | **62,353** | `_killface_v1_design_draft_2026_10_16.md` | **§3-1 S-1 之③ ／ §6 `K-D-9`**（5 锚落位件 0 在盘） |
| `423c84de20d5` | 15,457 | `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | §2 L20–L32 逐字（L22 落位路径 · L32 撤回条款） |
| `d042dd66e3c7` | 11,716 | `_anchor_status_naming_note_2026_10_16.md` | `N-1`／`N-2`／`N-4` 命名口径之已裁面 |
| `bfcc14f8a4ce` | 16,960 | `_pi_card_answers_register_2026_10_16_v29.md` | §2-2 之 3「5 锚落位件补齐·候 PI 授权 ＋ 后续棒补齐」 |
| `98aabe87ae11` | 21,872 | `_killface_v1_effect_register_2026_10_16.md` | `K-D-3` 同族之登记缺口口径 |
| `7d1482b239c7` | 50,344 | `_root_session_history_memo_main_2026_10_14.md` | 第四批卡之登记缺口（**⚠ 活动追加件·见 §8**） |

---

## §4 5 锚落位记录（**9 实体逐件实测复算 · 0 例外**）

| 锚 ID | 实体 path | SHA-12（直算 ＝ 登记） | bytes | 相符 |
|:--|:--|:--|--:|:--:|
| **`P_B_ECR_BASELINE`** | `results/deposon_v20_gt.json` | `497b9c2d6746` | 3,803 | ✅ |
| **`P_B_KILL_LINE`** | `verifier/kill_lines/GT_kill_line_carrier_v1.md` | `9e09214cf088` | 18,905 | ✅ |
| **`P_B_FROZEN_RUNS`**（甲案·5 成员） | `results/deposon_v20_baselines.json` | `6edb2aec1660` | 16,987 | ✅ |
| | `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | 409,104 | ✅ |
| | `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | 69,204 | ✅ |
| | `results/deposon_v18_api_supplements.json` | `62c1a41e1db8` | 80,624 | ✅ |
| | `results/deposon_v17_fusion_fix.json` | `af51da229652` | 106,164 | ✅ |
| **`P_B_LLM_CLIENT`** | `tools/llm_client.py` | `1722500da4aa` | 8,118 | ✅ |
| **`P_B_DISTORTION_CALC`** | `tools/distortion_calculator.py` | `410a12482eef` | 40,611 | ✅ |

**合计：9/9 逐位相符 · 0 漂移 · 0 例外。**

**落位要点（五条）**：

1. **比对基准之分面**：`P_B_FROZEN_RUNS` 采**甲案**（多成员）形态，v3 之锚级 `sha256_12`／`bytes` 为 **`null`** ⇒ 其 5 成员之比对基准取 **v3 `members[]` 逐成员登记值**；其余 4 锚取锚级登记值。（⚠ 若误以成员值比锚级 `null`，将误报 5 例不符——本棒首测即触发此误，经复核修正。）
2. **`P_B_ECR_BASELINE` 之值面**：除指纹复算外，另**独立复读 JSON 指针** `/GT4_price_of_anarchy/verdict/median_poa` 得 `1.3333333333333333`，与登记 `value` **逐位相符**；**0 runner 执行 · 0 LLM calls**（纯读 ＋ 纯算术）。
3. **锚⑤之自证**：自检轨内部 `T8` 指纹面独立复算得 `410a12482eef` / `40,611`，与本棒外部直算**同值**（双通道自证相符）。
4. **`value`／`field` 缺键之处理**：v3 中 `P_B_KILL_LINE`／`P_B_LLM_CLIENT`／`P_B_DISTORTION_CALC` **0 `value` 键**、`P_B_DISTORTION_CALC` **0 `field` 键** ⇒ 本件置 **`null`** 以保持字段集齐整，**⛔ 0 新拟值 · ⛔ 0 由他锚代填**。
5. **`U-2` 仍开口**：`P_B_DISTORTION_CALC` 之 `version` 子字段仍沿 v3 之 **U-2**（逐字沿 spec L30 之 `version=2026-09-11`，**0 以文件内容复核**）⇒ **⛔ 0 闭该面**。

---

## §5 自检轨实跑留痕（**`T1–T9` · ε 固定 0.1 · 退出码 0 · 9/9**）

- **命令**：`python tools/distortion_calculator.py --self-test`｜**cwd**：`_repo_mirror`｜**Python**：3.14.7
- **退出码**：**`0`**｜**`all_pass=True`**｜**小计：9/9 通过**
- **网络 calls**：**0**｜**LLM calls**：**0**｜**calculator 写盘**：**0**（唯一输出面 ＝ stdout）
- **期望值面**：`7551c47d3ece` §2-2 逐字——`D2_example_c1_equals_20`／`D2_example_c2_equals_10`，由 `G_L＝2, G_B＝0 ⇒ G_L/(c·ε)＝2/ε`；`c＝1` 得 20 ⟺ **ε＝0.1**；`c＝2` 得 10 ⟺ **ε＝0.1** ⇒ **期望值仅在 ε=0.1 时成立**（KC-1 丙案：自检轨 ε 固定 0.1）。

| # | 结果 | 逐字摘要 |
|:-:|:--:|:--|
| **T1** | ✅ PASS | 正典例向量 `G_L=2,G_B=0,eps=0.1 -> c=1 得 20 / c=2 得 10`（实得 `c=1 得 20`；`c=2 得 10`） |
| **T2** | ✅ PASS | 守卫两支路：无守卫支路 c 精确消去（分母=5）／守卫支路 c 不消去（c=1 分母=1/10 倍数=20；c=2 分母=1/5 倍数=10） |
| **T3** | ✅ PASS | 代数恒等式网格 `D2_identity_grid_10k`：网格点数 10000（期望 10000） |
| **T4** | ✅ PASS | `D∈[0,H]` 边界 ＋ B10 基数不入 D（全拒 D=33） |
| **T5** | ✅ PASS | 枚举面：A 非空键集=15（期望 15）／C 对象 3H/4：可达 25 例 · 非整除 75 例／D 三处更正代数（网格 ＋ 例值 20/10）全过 |
| **T6** | ✅ PASS | 聚合面：手算 D=2 实现 D=2；异长轨迹 (2,1) 均匀权 D=1/2（决策数加权将给 1/3） |
| **T7** | ✅ PASS | 双轨一致率 S7：逐位相符 200/200（一致率 1）；最大相对偏差 0 |
| **T8** | ✅ PASS | 指纹面：本件 `sha256_12=410a12482eef` `bytes=40611`；内建散列调用 0 次；BOM=False CR=0 TAB=0 U+FFFD=0 |
| **T9** | ✅ PASS | 判死面转引：五例逐字相符 `FAIL_H0 ×2 / PASS_H1 ×1 / GRAY ×2`；边界点（mean 1.5/1.8/2.0，ci_hi 1.8/2.0，hit 0.1/0.3）全用 |

> 📌 **测试侧修正留痕栏**（`0a031a9795a9` §6 L178 之体例）**照录 4 条**（T1 ε 以 `Fraction(1,10)` 给／T5 `C` 对象非整除如实登记／T6 首写用例系**用例侧**之误已复测／T7 双轨对照规则盘上 0 候选故⛔ 0 代定判据）——**逐字全文见 JSON 件 `landing_self_test_vector.test_side_correction_trail_verbatim` ＋ `stdout_verbatim`**。

---

## §6 阴性结论（**三通道 ＋ 三重自审**）

**对象**：`f5da17e62b07`（G-E02 验收结果 JSON · 自检向量之被引指纹）

| 通道 | 方法 | 结果 |
|:--|:--|:--|
| **①** 文件名 | 全仓递归 `*f5da17e62b07*` | **0 命中** |
| **②** 内容 SHA-12 | `os.walk` 全仓 **2,663 件**逐件 `hashlib.sha256` 直算 | **0 命中**（**遍历错误 0**） |
| **③** 字面 vs 实体 | 该字面作**被引指纹转录**出现于 **21 件**既有件 | **实体面仍 0 在盘** |

**三重自审**：

1. **`os.walk` 遍历错误断言**：`onerror` 回调已挂载并计数 ⇒ **遍历错误数 ＝ 0**（errors 列表为空即遍历无失败）。
2. **模式非结构性互斥**：三通道分别独立取证（文件名／逐字节 SHA-12／字面转录与实体之分面），**无一通道以他通道之结果充抵**。
3. **时点新鲜性**：测量时点 **2026-10-16 夜**；全仓 **2,663 件**；各锚实体 mtime 皆早于测量时点（详见 JSON 件 `per_anchor.entries[].mtime`）⇒ 测量前后未变动。

> ⚠ **KD-5（分面登记 · 沿 v3 KD-18 同族）**：「0 在盘」**仅及实体面**，⛔ **0 扩为「全仓 0 次出现」**——该字面作为转录确实在册于 21 件。
> ⚠ **KD-4／U-4**：本件⛔ **0 自认**即 `f5da17e62b07` 之继任者或等价物；若 PI 欲以其为该指纹之实体，须**另行明裁并重算指纹**。

---

## §7 `KD` 清单（**本棒新立 · 候 PI 核准 · ⛔ 0 代裁**）

| # | KD | 状态 |
|:-:|:--|:--|
| **KD-1** | **新字段候裁**：本 JSON 新增顶层面 `landing_measurement`／`landing_self_test_vector` —— 不在 v3 顶层键集内。落笔理由：派工明载「实跑自测 T1–T9 之结果照录」而无既存键可承载 ⇒ ⛔ 0 以新键充 v3 原键、⛔ 0 改 v3 一字。**PI 若裁「另立他键名或另立他件」，照裁改** | 🟠 **候 PI 核准** |
| **KD-2** | `status`→`anchor_status` ＋ 加 `status_detail` 系**已裁命名口径**（`d042dd66e3c7` `N-1`／`N-4`）之遵行，⛔ 非自创新键；⚠ **沿用不外推**——该裁射程仅及键名与语义面，⛔ 0 等同 schema 入锁 | ✅ 已裁·沿录 |
| **KD-3** | **授权面缺口**：卡 `ask_b9ba5971d9c3d61e0e863375` 之 PI 逐字答**于盘上 0 登记件**（全仓该卡号仅命中 `7d1482b239c7` §18，且该处仅载「第四批卡已呈候 PI」＋ Q3 之**问句**「5 锚落位件造件授权（S-1 缺口二）」，**未见其答**）⇒ 本件所据逐字答系**派工单元转述**，⛔ 0 独立验明（沿 `98aabe87ae11` §7 `K-D-3` 同族） | 🔴 **未成就** |
| **KD-4** | **落位面界分**：本件⛔ 非 spec L22 之 `verifier/handoff/P_B_V0_anchors_sha256_12.json`（`Test-Path=False`·沿 v3 KD-9／KD-19 复测确认）⇒ **不满足 spec L22 字面路径**；S-1 之③之闭**候 PI 裁其读法** | 🔴 **候 PI 裁** |
| **KD-5** | **阴性结论分面**：`f5da17e62b07` 实体面 0 命中；字面转录 21 件 ⇒ 「0 在盘」仅及实体面 | 🟡 **如实登记** |
| **KD-6** | 5 锚之 `field`／`status`／`limitation_face`／`deviation_disclosure` 等面**逐字沿录 v3**，含 v3 自身在册之 KD-3／KD-9／KD-10／KD-11／KD-15／KD-17／KD-18／KD-22 **⛔ 0 闭 · ⛔ 0 改 · ⛔ 0 调和**；**登记不代修** | ✅ 遵行 |

---

## §8 诚实交代（**failures ＆ limitations**）

1. **授权链未在盘可验（KD-3）**：本棒所据之 PI 逐字答**无盘上登记件**可核 ⇒ 全部授权字面**系转述**，本棒 ⛔ 0 独立验明。
2. **源件之一为活动追加件**：`_root_session_history_memo_main_2026_10_14.md` 于本棒**两次独立测量之间即发生变化**（`f0a5c8c61d15` / 47,890 B → `7d1482b239c7` / 50,344 B）⇒ 其指纹**具时点性、可能已再变**；**其余 7 件源件指纹两次测量间一致（0 变动）**。本件所据之事实面（第四批卡之登记缺口）**不随其变动而改变**。
3. **本棒 0 跑实验**：除 calculator `--self-test`（其设计即为 0 calls 自测）外，⛔ 0 跑任何 runner／网格枚举；ECR 值面系**指针复读 ＋ 纯算术**，非重算上游。
4. **落位 ≠ 入锚**：本棒产出**候 PI 核准后**方可入锚；**本棒⛔ 0 宣告入锚、⛔ 0 宣告 S-1 之③已成就、⛔ 0 宣告①毕**。
5. **`U-2` 仍开口**：`P_B_DISTORTION_CALC.version` 未以文件内容复核（沿 v3）。
6. **自比对误报之修正已留痕**（§4 要点 1）：首轮复算误将甲案成员值比锚级 `null` ⇒ 误报 5 例不符；经复核改为取 `members[]` 后 **9/9 相符**。如实登记以备复核。

---

## §9 版式与纪律自证（**逐项实测**）

| 项 | 要求 | 实测 |
|:-:|:--|:--|
| 1 | **UTF-8 无 BOM** | JSON 件 `BOM=False` ✅ |
| 2 | **纯 LF（0 CR · 0 TAB）** | JSON 件 `CR=0` `TAB=0` ✅ |
| 3 | **尾换行 `\n`** | JSON 件 `endswith"}\n"` ✅ |
| 4 | **JSON `ensure_ascii=False` ＋ `indent=2`** | ✅（中文直书 ＋ 2 空格缩进） |
| 5 | **Python `io.open` 直写 · Windows raw 路径** | ✅（`r"_repo_mirror"`） |
| 6 | **落盘前 `Test-Path=False` ＋ glob 0 命中** | ✅ 两件皆然 |
| 7 | **⛔ 0 回改任何既有件一字** | ✅ v1 `4b020eb04605` / v2 `f06313373fc6` / v3 `0c269b9558da` / calculator `410a12482eef` / llm_client `1722500da4aa` / spec `423c84de20d5` / gt.json `497b9c2d6746` / kill_line `9e09214cf088` / v3 锁记件 `deea2ccb2643` —— **落盘后复算全部与落盘前逐位一致** |
| 8 | **⛔ 0 网络 · ⛔ 0 LLM calls** | ✅ 自检轨纯本地（0/0） |
| 9 | **⛔ 0 宣告①毕 · ⛔ 0 代 PI 裁** | ✅ 全文无此宣告 |
| 10 | **⛔ 0 入锚面 · ⛔ 0 自签生效** | ✅ 本件与 JSON 件均标「候 PI 核准」 |

---

## §10 件止

> **本棒毕** —— 两件落盘，指纹已直算自报（§1）。**产出标「候 PI 核准」：⛔ 0 径行采认、⛔ 0 入锚面、⛔ 0 宣告 S-1 之③已成就、⛔ 0 宣告①毕。**
>
> **待 PI 面**：`KD-1`（新字段候裁）· `KD-3`（授权登记缺口·须补入登记正身）· `KD-4`（落位面界分·S-1 之③之闭读法）· `U-4`（是否以本件充 `f5da17e62b07` 之继任者）。
>
> *（件止 · `worker` · GE02-ANCHOR-LANDING-BUILD · 2026-10-16 夜 · 署名如实·⛔ 0 冒充 PI／parent／doc-writer／verdict-keeper／verifier）*
