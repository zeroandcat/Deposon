# M-R14 裁项 B 执行件 · #26b 以 r3 件重跑正式档（双口径成对并报 ＋ U-3 登记）

**题源**：`_v5_r4_residual_merged_catalogue_2026_09_29.md`（`0c4bbd26ea55`）§癸组 `M-R14`｜PI 裁 **B：重跑并落盘（双口径成对并报）**。
**承接源件**：`_v5_exec_f2_r3_register_2026_09_29.md`（`9d64ee1d6996`）L140（`§3.3 未跑 executor` ＝ r4-H11-Z04）＋ L225–L231（`§9 U-1/U-2/U-3` ＝ r4-H11-Z05）。
**产出**：① `results/_v3_recheck_26b_r3_result_2026_09_29.json`（重跑产物）② 本注记件。
**署名**：**Mavis 团队 worker**（session `mvs_d8759c3914534b1db991bef2a1c0ea17`，本 Turn ＝ 重跑执行方）。
⚠️ **0 冒充**：重跑产物 JSON 内 `produced_by_r3` 字段载的是 **r3 实现棒** session `mvs_ce8c37cbf1944b19800d7c3a28543591`（改实现方）—— 那是**件内既有字面**，本 Turn **0 改写**（byte 0 触动）；「重跑执行方」与「r3 实现方」是**两个不同主体**，本件如实分标。

---

## §1 核明（先核后引 · 盘上实测 SHA-12）

| # | 件 | 盘上实测 SHA-12 | 字节 | 核明结论 |
|---|---|---|---|---|
| 1 | `results/_v5_r4_residual_merged_catalogue_2026_09_29.md` | `0c4bbd26ea55` | 102,410 | 题面在位（`M-R14` L468） |
| 2 | `results/_v5_exec_f2_r3_register_2026_09_29.md` | `9d64ee1d6996` | 24,177 | **与派工单给定值逐字相符** ✅（L140／L225 均在位） |
| 3 | `results/_v3_recheck_26b_executor_r3_2026_09_29.py` | `6c83e7a7ca2e` | 64,959 | 重跑所用 executor；LF only（1,063 LF／0 CRLF／0 BOM） |
| 4 | `results/_v3_recheck_26b_result_2026_09_27.json` | `49c6e5a07732` | 44,379 | as-run 3/3 PASS 历史派生件（0 回溯对象） |
| 5 | `results/_v3_recheck_26b_r3_result_2026_09_29.json` | **运行前不存在** | — | 落盘前实测 **MISSING** ✅（登记件 §3.3「0 落盘」属实） |

### ⚠️ §1.1 与派工单的一处**路径差异**（如实登记，0 调和）

派工单写 r3 executor 在 **`deposon_team/plugins/`** 下；**盘上实测：该路径不存在**，r3 executor 实际在 **`results/`**。
实测命令返回 `MISSING`（`deposon_team/plugins/_v3_recheck_26b_executor_r3_2026_09_29.py`）。
**本 Turn 处置**：以**盘上实际路径 `results/_v3_recheck_26b_executor_r3_2026_09_29.py`** 执行（内容与登记件 §3.2「r3」条目、`OUT` 常量 L159 指向的路径一致 ⇒ **该 executor 自身也把输出定为 `results/` 路径**，两处互证）。**0 移动文件、0 建目录、0 改派工单字面**。

---

## §2 重跑执行（本地 · 0 LLM／0 API／0 网络）

| 项 | 值 |
|---|---|
| 运行环境 | Windows · Python **3.14.7** · numpy **2.5.3** |
| 执行命令 | `python results/_v3_recheck_26b_executor_r3_2026_09_29.py`（cwd ＝ 仓库根） |
| executor 处置 | **只读运行** —— 跑前跑后 SHA-12 逐值复现 `6c83e7a7ca2e`／64,959 B（§7） |
| 输出路径 | `results/_v3_recheck_26b_r3_result_2026_09_29.json`（**新名**，executor 内 `OUT` 常量既定） |
| 覆写面 | **0 覆写任何既有 JSON**；未触碰 `_v3_recheck_26b_result_2026_09_27.json`（0 合并，沿 `K-V3R-0-D`） |

### §2.1 ⚠️ 第一次运行**异常终止**（如实交代，非失败掩盖）

- **现象**：第 1 次运行在 `main()` 的**收尾 print 段**（L1049）抛 `UnicodeEncodeError: 'gbk' codec can't encode character '\u21d2'` —— Windows 控制台默认编码 GBK 无法编码 `⇒`。
- **产物状态**：`OUT.write_text(...)`（L1040）**在该 print（L1049）之前**，故 **JSON 已完整落盘**（实测可 `json.loads` 解析，顶层 24 键齐全）。
- **第 2 次运行**：加 `PYTHONIOENCODING=utf-8` 后重跑，**exit 0 全程完成**，L1046–L1058 收尾打印**全部输出**。
- **两次落盘 SHA-12 逐字相同** = `c9d3c9f819f1`／54,294 B ⇒ 满足 executor 内 `reproducibility_in_process.note` 要求的**「进程外双跑比对（两次落盘件 SHA-12 逐字相同）由 worker 核验并登记」** ✅。
- **根因归属**：属**控制台编码层**，非计算层、非 executor 逻辑层 ⇒ **0 改 executor**（铁边界：executor 只读运行）。
- **诚实限定**：双跑同一性在**本机（Windows / CRLF 翻译）**成立；`Path.write_text` 在 Windows 把 `\n` 翻译为 `\r\n`（落盘 JSON 实测 1,175 CRLF），故该 SHA-12 **0 跨平台可复现性**——本件 0 声称跨平台复现。

---

## §3 新读数（读法乙 · `new_verdict` 面 · 本 Turn 实测）

| 本体 | `n_distinct` | `std` | `rel_std` | `new_verdict` | `kill_line_fail_hit` | `branch_id` |
|---|---|---|---|---|---|---|
| `O1_discrete_cell_redistribution` | **9** | **0.0012788884062167251** | 0.0864114 | **FAIL** | `True` | `READING_B_V2_ROW3_ND_GT_3_AND_STD_GT_0` |
| `O3_logit_normal_form` | **8** | **0.0044661691265184735** | 0.0129055 | **FAIL** | `True` | 同上 |
| `O5_replicator_ode_softlimit` | **9** | **16.980008842717528** | 0.412805 | **FAIL** | `True` | 同上 |

**汇总面**（executor 实测输出）：`same_direction = True`（3/3 本体新构造 verdict 一致 ＝ FAIL）｜`hit_tier = ["档3：FAIL（原标注维持）" ×3]`｜`hit_tier_all_same = True`｜`formal verdict = {O1: FAIL, O3: FAIL, O5: FAIL}`。
**旁证项**：`pre_run_degenerate_gate.degenerate_alarm_hit = False`｜`perturbation_table_sha12 = 0b23943c898c`，`matches_preexp = True`｜`O1 identical to landed 26 result = True`｜`consistency vs preexp` 3/3 `True`｜`C4 进程内全量二次重算` 3/3 `True`｜`O5 rho(min_component, n_iter_mean) = -0.36666666666666664`｜`payload_sha12 = 1630d518b7d9`。
**读法乙注记（executor 自身字面）**：「本读数域内 PASS 档已全域消失（归属表 v2）⇒ `new_verdict` 预期恒为 FAIL；**若出现 PASS 即为异常取值，须 γ 升级**」——**本 Turn 实测三本体全 FAIL，无异常取值触发**。

---

## §4 双口径成对并报（沿 `K-V5RB-0-G` 唯一豁免 · `K-V5RB-0-L` 双口径 0 豁免）

**两读数**（**同一读数域 · 不同读法口径**）**并存且分标**，0 单值化、0 覆盖：

| 面 | as-run 历史读数（`49c6e5a07732` · 读法甲 · F2 字面） | 本 Turn 新读数（r3 派生件 · 读法乙 · 归属表 v2） |
|---|---|---|
| O1 | `n=9, std=0.00127889` → **PASS** | `n=9, std=0.0012788884062167251` → **FAIL** |
| O3 | `n=8, std=0.00446617` → **PASS** | `n=8, std=0.0044661691265184735` → **FAIL** |
| O5 | `n=9, std=16.98` → **PASS** | `n=9, std=16.980008842717528` → **FAIL** |
| 档位 | 档2：PASS + 不一致 ×3 | 档3：FAIL（原标注维持）×3 |
| legacy 面 | `UNVERIFIED（判据退化）` | `UNVERIFIED（判据退化）`（**同一读数**） |
| 生效口径 | 读法甲（F2 字面 `n≥4 ∧ std>0 ⇒ PASS`） | 读法乙（**F2 字面已废止**，起算 2026-09-28 23:42 GMT+8） |

### ⚠️ §4.1 本 Turn 实测到的一项**关键事实**（比题面预期更强，如实登记）

题面预判是「同一读数域、**不同读法口径**」；**实测结果比这更强**：
**新读数的 `n_distinct` / `std` 与 as-run 历史件逐值全等**（三本体 9 项 `rates` 字段逐一 `==` 实测 `True`，非四舍五入相等，是 Python float 逐值相等）。
⇒ **差异面 ＝ 只有判读口径（verdict / 档位），读数面 ＝ 0 差异**。
**该事实的意义**（0 外推）：它证实本次 FAIL **不是**「重新采样得到的新数据」，而是**同一批读数在读法乙下的重新判读** ⇒ 对照面更干净，但也**意味着新 FAIL 与 as-run PASS 构成一对「同数据、异结论」的直接对撞**，0 可用「重跑得数不同」来解释。**此对照面仅限本读数域（`K-V5RB-0-H`）。**
**0 推断**：as-run 当初 3/3 PASS **是否已在读法乙口径下复核过**——**盘上无该记录**，本件**0 推断、0 代裁**（见 §9）。

---

## §5 U-3 登记面：`K-V5RB-0-L` 双口径系统性不一致（`K-V3R-0-C`「维持原标注 ＋ γ 升级」）

**登记事实（本 Turn 实测，0 代裁）**：

| 登记项 | 内容 |
|---|---|
| 不一致形态 | `new_verdict ≡ FAIL`（三本体全数）**vs** `legacy_verdict ≡ UNVERIFIED（判据退化）`（本体无关，逐本体共享同一读数） |
| 件内自记字面 | 「**系统性不一致**（读法乙 v2：new_verdict ≡ FAIL vs legacy_verdict=UNVERIFIED（判据退化） ⇒ `K-V3R-0-C`「维持原标注 + γ 升级」路径**必然触发**；沿 `K-V5RB-0-L` **0 豁免并报**）」 |
| 配对完整性 | `dual_caliber_pair_complete = True`（三本体全数）——**缺任一腿即无效登记**（judge 函数 docstring 自载） |
| 旧件对照 | as-run 件记的是「不一致（new **PASS** vs legacy UNVERIFIED/判据退化）」⇒ **同一登记位在两代读法下形态不同**，本 Turn **0 回改旧件字面**，两代字面**并存** |
| **「维持原标注」** | **as-run 3/3 PASS 终判维持不动、0 改判、byte 0 触动**（`49c6e5a07732` 复验 `UNCHANGED`）——**回溯效力 0**（沿生效登记件 §3.4） |
| **「γ 升级」** | γ 根因沿 **`K-V5RB-0-D` 强制改写**为：「**判据面恒定 ⇒ PASS 侧全域消失 ⇒ 判别力归零（读法乙结构性来源）**」——**禁**记为构造常量／弱分布／方差恒同等**构造类根因**（本域是真分布，禁记构造类根因 ＝ 0 误导） |
| γ 归属出处 | `gamma_source` 字段逐字载：归属表 **v2**（`7e2b0bb39cfe` §1.1 第 3 行 ＋ `_v5_bulk_activation_2026_09_28.md` §3.1 `K-V5RB-E-3` 四要素齐备，起算 2026-09-28 23:42 GMT+8）；**归属表 v1（`c353fbcdc753` §3.1 第 3 行 PASS）已失效 · 留历史快照 · byte 0 回改**（沿 `K-V5RB-0-J`） |
| 登记载体 | **本新注记件**（`K-V3R-0-C` 要求的新注记件面）；**0 改任何既有登记件** |

**登记落点声明**：本节即为 `U-3` 的**正式登记面**（按 `K-V3R-0-C`「维持原标注 ＋ γ 升级」）。**0 代 verdict-keeper 裁定档位、0 代 PI 拍板**——档位取 executor 依 prereg §2.3 机械给出的**档3**。

---

## §6 U-2 限制面：`γ-RB-7` 未排查 · **读法乙援引限制**（本 Turn 0 预判、0 外推）

| 项 | 内容 |
|---|---|
| `γ-RB-7` 状态 | **仍未排查**（`7e2b0bb39cfe` L205：`⚠️ 未排查` ＝「读法乙下『PASS 档不可达』对**该线全部补审**的影响面（若同域）」） |
| 援引限制（逐字） | 「**不得援引本件字面**；须另案」；同件 L223 §7.2 第 3 条：「『PASS 侧全域归零』的推演**仅限本读数域**……该面**本件未排查**（`γ-RB-7`）」 |
| **本 Turn 的适用面** | 本次执行**落在 `K-V3R-26` 本读数域内**（`convergence_rate` 的 `n_distinct` / `std`，构造面 `n ∈ [1,9]`）⇒ 读法乙在**该域**的效力**未被 `γ-RB-7` 动摇**（`γ-RB-7` 未排查的是**外推面**） |
| **本 Turn 0 做的事** | **0 预判** `γ-RB-7`、**0 排查** `γ-RB-7`、**0 评估**其影响面、**0 外推**为全项目口径（沿 `K-V5RB-0-H`）、**0** 将「PASS 档全域归零」推演至 v1 其余 8 条 kill-line 或任一其他判死线 |
| **未受影响的登记** | §5 的 γ 升级**仅在本读数域内成立**；若未来 `γ-RB-7` 排查结论动摇了读法乙的效力面，**§5 登记须重评**（本件**0 预判**该情形） |
| 归属 | **另案**（`γ-RB-7` 排查属**另轴**，不属本 M-R14 派工范围） |

---

## §7 0 回改自证（跑前 / 跑后两次逐字节实测 · 13 件全覆盖）

**方法**：跑前对 13 件（executor 6 个输入件 ＋ as-run 派生件 ＋ r3 executor ＋ 26b 原件/r2 件 ＋ prereg/26 rescript/preexp 三件）录 SHA-12 ＋ 字节；跑后逐一复算比对。

| # | 件 | 跑前 SHA-12 / 字节 | 跑后 SHA-12 / 字节 | 判定 |
|---|---|---|---|---|
| 1 | `results/_v3_recheck_prereg_v1_2026_09_27.md` | `88052d7db895` / 37,346 | `88052d7db895` / 37,346 | ✅ UNCHANGED |
| 2 | `results/_v3_recheck_26_executor_2026_09_27.py` | `46c326c756c3` / 15,056 | `46c326c756c3` / 15,056 | ✅ UNCHANGED |
| 3 | `results/_v3_recheck_26_result_2026_09_27.json` | `eb6a99dd46dd` / 11,994 | `eb6a99dd46dd` / 11,994 | ✅ UNCHANGED |
| 4 | `results/_v3_recheck_26_rescript_2026_09_27.md` | `6b86576146a3` / 13,747 | `6b86576146a3` / 13,747 | ✅ UNCHANGED |
| 5 | `results/_v3_recheck_26_preexp_data_2026_09_27.json` | `177c88e1bd82` / 94,658 | `177c88e1bd82` / 94,658 | ✅ UNCHANGED |
| 6 | `results/_v3_recheck_26_preexp_report_2026_09_27.md` | `0a2b5c837c83` / 21,855 | `0a2b5c837c83` / 21,855 | ✅ UNCHANGED |
| 7 | `results/_v3_recheck_26_preexp_executor_2026_09_27.py` | `775217a462f5` / 38,726 | `775217a462f5` / 38,726 | ✅ UNCHANGED |
| 8 | `results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json` | `a9ad1de618f5` / 1,669 | `a9ad1de618f5` / 1,669 | ✅ UNCHANGED |
| 9 | `results/deposon_v3_physical_opt_60cells_2026_09_11.json` | `c659695aa23c` / 17,732 | `c659695aa23c` / 17,732 | ✅ UNCHANGED |
| 10 | **`results/_v3_recheck_26b_result_2026_09_27.json`（as-run · 0 回溯对象）** | `49c6e5a07732` / 44,379 | `49c6e5a07732` / 44,379 | ✅ **UNCHANGED** |
| 11 | **`results/_v3_recheck_26b_executor_r3_2026_09_29.py`（只读运行）** | `6c83e7a7ca2e` / 64,959 | `6c83e7a7ca2e` / 64,959 | ✅ **UNCHANGED** |
| 12 | `results/_v3_recheck_26b_executor_r2_2026_09_28.py` | `0808af6212c5` / 52,272 | `0808af6212c5` / 52,272 | ✅ UNCHANGED |
| 13 | `results/_v3_recheck_26b_executor_2026_09_27.py` | `5c906113a210` / 43,171 | `5c906113a210` / 43,171 | ✅ UNCHANGED |

⇒ **13/13 逐值复现 ⇒ 对既有件的写入量 ＝ 0 字节。**
**补充自证**：第 11/12/13 行三件 SHA-12 与登记件 §4「0 触动实证」表所载（`6c83e7a7ca2e` 未在该表列出；`0808af6212c5`／`5c906113a210`／`49c6e5a07732` **逐值相符**）互证 ⇒ **本 Turn 0 撼动 r3 改造棒的任何产物**。
**本 Turn 唯一写入 ＝ 2 件新名件**（重跑 JSON ＋ 本注记件）。

---

## §8 重跑中新发现的事实（如实登记 · 0 编造）

| # | 新发现 | 性质 | 处置 |
|---|---|---|---|
| **1** | **r3 executor 实际位于 `results/` 而非 `deposon_team/plugins/`** | 路径事实（与派工单所述不符） | §1.1 如实登记，**0 调和、0 移动文件** |
| **2** | **第 1 次运行因 GBK 控制台编码在收尾 print 段抛 `UnicodeEncodeError`**（产物已落盘） | 环境事实 | §2.1 如实交代，**0 改 executor**，加 `PYTHONIOENCODING` 复跑取得 exit 0 |
| **3** | **新旧读数逐值全等**（§4.1） | 读数事实 | 如实登记，**0 外推** |
| **4** | **实现差异（布尔字段改名）**：as-run 件字段为 `kill_line_hit`；r3 件字段为 `kill_line_fail_hit` ＋ 新增 `kill_line_branch_id` ＋ `gamma_root_cause` ＋ `gamma_source` ＋ `dual_caliber_pair_complete` | **实现差异**（r2/r3 起的方向显式命名纪律，`S-40` 系） | 如实登记；**新旧字段名并存，0 回改旧件、0 统一命名** |
| **5** | **落盘 JSON 为 CRLF**（1,175 CRLF）——`Path.write_text` 在 Windows 的 `\n→\r\n` 翻译所致（executor 源码为 LF only） | 字节事实 | SHA-12 一律按**盘上实际字节**实测；**0 改 executor、0 手工转行尾**；**0 声称跨平台复现**（§2.1） |
| **6** | **r3 件新增顶层键 6 个**：`date_r2`／`date_r3`／`revision`／`revision_of`／`produced_by_r3`／`reading_b_attribution`；`OLD-only` ＝ 空 | 实现差异 | 如实登记 |

---

## §9 诚实边界（逐条 · 0 夸大）

1. **0 改既有件**：§7 表 13/13 逐字节复现，**写入量 0 字节**。
2. **0 回溯**：as-run 3/3 PASS 终判**维持不动**；本 Turn 新读数**只约束起算时刻（2026-09-28 23:42 GMT+8）之后的读数**（沿生效登记件 §3.4）。
3. **0 编造读数**：§3 全部数值取自 executor 实测 stdout ＋ 落盘 JSON 实测，**0 手工估算、0 四舍五入改写**（表内给足 float 全精度）。
4. **0 单值化**：新旧两读数**并存且分标**（§4），新件内 `new_verdict` 与 `legacy_verdict` **成对字段齐全**（`dual_caliber_pair_complete = True`），**0 任一腿单值化**。
5. **0 预判 U-2**：`γ-RB-7` 本 Turn **未排查、未评估、未外推**（§6）。
6. **0 LLM／0 API／0 网络**：纯本地 `python` 单脚本执行（numpy ＋ hashlib ＋ json）；**0 读取、0 记录任何 key／token／凭据**（R4 key 永不明文：0 破例）。
7. **0 代裁**：**0 代 PI 拍板、0 代 verdict-keeper 裁定档位、0 代 evidence-auditor 审链、0 代 verifier 独立复核**。本件是**执行回执 ＋ 登记面载体**，**非独立复核**。
8. **0 声称可复现范围超出实测**：双跑同一性仅在**本机**成立（§2.1）；**0 声称跨平台**。
9. **0 外推读法乙**：读法乙效力面仅限 `K-V3R-26` 本读数域（`K-V5RB-0-H`）；**0 外推**为全项目「空档归属」方法论或 v1 其余判死线。
10. **skill 交代**：本 Turn **未载入任何 skill**（派工单未指定）——按派工单字面执行。
11. **as-run 3/3 PASS 是否曾按读法乙口径复核过**：**盘上 0 条记录**。本件**如实登记该缺口**，**0 推断、0 代裁**（见 §10 U-4）。
12. **`deposon_team/plugins/` 路径差异**：本 Turn 以盘上实际路径执行（§1.1）。**该差异的正确处置（改派工单字面／移动文件／双份留存）0 代裁**，登记待裁。

---

## §10 未决项（穷尽清点 · 本件 0 代决）

| ID | 未决项 | 归属 | 状态 |
|---|---|---|---|
| **U-1** | 是否以 r3 件重跑 #26b 正式档、产出 `_v3_recheck_26b_r3_result_2026_09_29.json` | PI / verdict-keeper | ✅ **本 Turn 已执行**（PI 裁 B）· 产物已落盘（`c9d3c9f819f1`）· 双口径成对并报（§4） |
| **U-2** | `γ-RB-7` 仍未排查 | 另案 | ⏳ **仍未排查**；本 Turn **0 预判**，限制面已如实登记（§6） |
| **U-3** | `K-V5RB-0-L` 双口径系统性不一致的登记面 | verdict-keeper | ✅ **本 Turn 已按 `K-V3R-0-C` 登记**（维持原标注 ＋ γ 升级，见 §5）——登记载体 ＝ 本注记件；**档位沿 executor 机械输出 ＝ 档3，0 代裁** |
| **U-4** | as-run 3/3 PASS 登记**是否曾按读法乙口径复核过** | PI / evidence-auditor | ⏳ **盘上 0 条记录**（本 Turn 全程 0 见）⇒ 本件**如实登记缺口**，**0 推断**；若补记录则校准本件引注，**0 回改既有件** |
| **U-5** | `deposon_team/plugins/` 与 `results/` 的 r3 executor 路径差异如何处置 | PI / protocol-keeper | ⏳ **新登记**（§1.1）· 本 Turn 以盘上实际路径执行，**0 代裁** |
| **U-6** | GBK 控制台编码导致收尾 print 抛错（Windows 本机） | worker / PI（是否需统一环境约定） | ⏳ **如实登记**（§2.1）· 本 Turn 以 `PYTHONIOENCODING=utf-8` 绕行，**0 改 executor**；**是否立环境约定 0 代裁** |

> **穷尽自检**：本 Turn 触及的全部文件已逐件核过（§1 表 1–5 ＋ §7 表 13 件 ＋ 新件 2 件）；除上列 6 项外，**无其他由本次重跑直接派生、且本件可自决或必须上报的未决项**。

---

## §11 铁律自证（逐条）

| 铁律 | 本 Turn 处置 | 状态 |
|---|---|---|
| **新名件** | 重跑 JSON ＋ 本注记件，**2 件皆新名**；落盘前实测目标路径 **MISSING** | ✅ |
| **既有一切件 0 触动** | §7 表 **13/13** 逐字节复现 | ✅ |
| **executor 只读运行** | `6c83e7a7ca2e`／64,959 B 跑前跑后逐值复现 | ✅ |
| **派生 JSON 不合并** | 落新名件，**0 并入**任何既有派生件（`K-V3R-0-D`） | ✅ |
| **0 回溯** | as-run 3/3 PASS 维持不动、0 改判 | ✅ |
| **双口径成对并报** | §4 两读数并存且分标；件内 `dual_caliber_pair_complete = True`（`K-V5RB-0-G` 唯一豁免／`K-V5RB-0-L` 0 豁免） | ✅ |
| **0 新设阈值** | 本 Turn **0 改任何常量**（阈值面全在 executor 内，executor byte 0 触动 ⇒ 阈值面必然 0 触动） | ✅ |
| **0 新增第四态** | 终态仍只 PASS／FAIL／KD；KD 拦截分支保持 | ✅ |
| **判定布尔方向显式** | r3 件 `kill_line_fail_hit`（hit ＝ 触发 FAIL）／`kill_line_pass`（pass ＝ 合格）方向显式；**0 新增**无方向命名 | ✅ |
| **γ 根因不误导** | γ 沿 `K-V5RB-0-D` 记「判据面恒定 ⇒ … 判别力归零（读法乙结构性来源）」；**禁**记构造类根因（§5） | ✅ |
| **key 永不明文** | 本 Turn **0 读取、0 记录**任何 key／token／凭据 | ✅ |
| **0 LLM／0 proxy／0 gateway** | 纯本地 `python` 单脚本；**0 网络** | ✅ |
| **署名如实** | 本件 ＝ **worker（session `mvs_d8759c3914534b1db991bef2a1c0ea17`）**；**0 冒充** r3 实现棒（`mvs_ce8c37cbf1944b19800d7c3a28543591`，仅作「实现方」历史主体引用）／PI／verdict-keeper／evidence-auditor／verifier | ✅ |
| **指纹口径** | SHA-12 ＝ `hashlib.sha256(字节).hexdigest()[:12]` **小写**、**盘上实测**；**本件自身指纹不自写入本件**（沿 `7e2b0bb39cfe` §11 先例）—— 落盘后实测并随交付回执回报 | ✅ |

---

## §12 交付核验

| 项 | 值 |
|---|---|
| 产出 ① | `results/_v3_recheck_26b_r3_result_2026_09_29.json` |
| 产出 ② | `results/_v5_clearance_mr14_rerun_note_2026_09_29.md`（本件） |
| 指纹 | **不自写入本件**（自指指纹口径）—— 两件落盘后**实测**并随交付回执回报 |
| 状态 | **重跑已完成 · 新派生件已落盘 · as-run 3/3 PASS 维持不动 · U-3 登记面已开** |
| 读法 | **双口径成对并报**（读法甲 PASS ∥ 读法乙 FAIL，同读数域、异读法口径） |

**本件四行收口**：

1. **重跑面**：`results/_v3_recheck_26b_executor_r3_2026_09_29.py`（`6c83e7a7ca2e`）**只读运行** 2 次，产出新名件 `results/_v3_recheck_26b_r3_result_2026_09_29.json`（`c9d3c9f819f1`／54,294 B）；**双跑 SHA-12 逐字相同** ✅。
2. **新读数面**：三本体 `new_verdict` **全 FAIL**（O1 `n=9`／O3 `n=8`／O5 `n=9`），`legacy_verdict` 全 `UNVERIFIED（判据退化）`，配对完整；**读数逐值与 as-run 全等 ⇒ 差异面仅在读法口径**（§4.1）。
3. **登记面（U-3）**：`K-V5RB-0-L` 双口径**系统性不一致**按 `K-V3R-0-C`「**维持原标注 ＋ γ 升级**」正式登记（§5）：as-run PASS 终判**维持不动**，γ 沿 `K-V5RB-0-D` 升级为「判据面恒定 ⇒ 判别力归零（读法乙结构性来源）」。
4. **边界面**：既有 13 件 **SHA-12 ＋ 字节逐值复现（0 触动）**；`γ-RB-7`（U-2）**未排查**，本 Turn **0 预判、0 外推**，读法乙援引限制已如实登记（§6）；第 1 次运行的 GBK 编码异常、派工单与盘上的路径差异**均如实交代、0 掩盖**（§2.1／§1.1）。
