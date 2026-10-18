# V3-N 不明三条实测判定件 · #32 CPATH / #21 KT-B1 / #19 P-G boss_pg

> **出件方**：Mavis 团队 worker（agent: worker｜session `mvs_27b8782edc8b4fae97b9a678f01d7c81`）
> **日期**：2026-09-27
> **委托来源**：Trae 回函 `letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md` §1.2 标注表「不明」12 条中 3 条
> **PI 拍板**：ask_083f814db95739725522f993 Q1「三条全跑」（执行序 #32 → #21 → #19）
> **铁律执行**：0 新设阈值（三条判定值均由原报告/预注册判据机械产生）｜既有件 0 触动｜派生 JSON 不合并｜key 永不明文｜署名如实

---

## §0 结论速览

| # | 对象 | 原状 | 本次实跑 | 判定 | 「不明」是否解除 |
|---|---|---|---|---|---|
| **#32** | CPATH 理论模拟 | PARTIAL，边际 0%~+26.7%，报告自标「待实测」 | **端点配额耗尽阻断**，0.05 USD 实测未完成 | **未决**（不编造边际） | ✗ 未解除 |
| **#21** | KT-B1 BOSS-B1/B2/B3 | GRAY_BOTH_BELOW/ABOVE，deposon 侧为占位 0.5 | **真测得 2.220446049250313e-16**，占位已替换；B1/B2 标签翻转 | **仍不明**（占位问题解除，测法轴问题未解除） | ✗ 未解除（根因已换） |
| **#19** | P-G boss_pg 三项 | SCAFFOLDING (PRE-REGISTRATION) | **三项实跑完成：PASS 2 / GRAY 1 / FAIL 0** | **实跑成立，无 kill-line 触发** | ✓ 已解除（附前提更正 + 鉴别力警告） |

**三条均未产生「PI 可据此改写结论」的新证据。** #19 解除；#21 根因置换；#32 外部阻断。

---

## §1 输入链核验表（先核后用，逐件登记）

| 用途 | 件 | 存在 | 字节 | SHA-12 | 核验 |
|---|---|---|---|---|---|
| #32 baseline | `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json` | ✓ | 32,995 | `4EC04D3D7D8C` | 会话首测同值，**0 触动** |
| #32 caption 构造 | `results/deposon_volcengine_22caption_embedding_2026_09_10.json` | ✓ | — | — | 读出 `caption_construction` / 端点 / model |
| #32 caption 原文 | `corpus/v20/strip_captions_22.json` + `corpus/v20/index.json` | ✓ | — | — | 22 条原文可按 `caption_construction` 字面复原 |
| #32 OUT 件（原） | `results/deposon_cpath_simulation_2026_09_10.json` | ✓ | 6,351 | `9466FDBF9C95` | 与原报告自记值同，**0 触动** |
| #21 v19 | `results/deposon_v19_benchmark_fixes.json` | ✓ | 409,104 | `910C4333EEAD` | 与 KT_B1_REWORK §四自记锚同值 |
| #21 守恒检测器 | `verifier/audit/conservation.py` | ✓ | 22,105 | `4BDEC2683F06` | 与 KT_B1_REWORK §四自记锚同值 |
| #21 SPEC | `docs/V3X/KT_B1_SPEC_V0.1.md` | ✓ | 35,688 | `0410CA0FBDAE` | 与 §四自记锚同值 |
| #21 返工报告 | `docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md` | ✓ | 11,478 | `BAEF94E393DE` | 本条测法锚来源 |
| #19 540-cell 数据 | `results/deposon_pg_v01_9m60c_2026_09_15.json` | ✓ | 11,512 | `AB75889EE738` | 会话首测同值，**0 触动** |
| #19 计算器 | `deposon_team/plugins/_pg_v01_compute.py` | ✓ | 20,923 | `D511C545F88E` | 会话首测同值，**0 触动** |
| #19 SPEC | `docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` | ✓ | 12,501 | `2F0765A1D39D` | 与 `_pg_v01_compute` 自记 spec SHA 同值 |
| #19 预注册脚本 ×3 | `deposon_team/plugins/boss_pg_1/2/3_*.py` | ✓ | 5,996 / 5,285 / 5,517 | `97FEDE6C8A4E` / `F006D4CACA94` / `09F37C01A258` | 判定线字面来源，只读 |

**0 触动自证**：会话首测的 4 件输入，产出前后 SHA-12 逐一 **MATCH**（`4EC04D3D7D8C` / `9466FDBF9C95` / `AB75889EE738` / `D511C545F88E`）。
**frozen 面**：`_verify_15frozen.py` → `TOTAL: 16 frozen files | OK: 16 | FAIL: 0`（注：Trae 回函 E-15 记的 15/16 FAIL 属 09-17 路径补充前状态，现已 16/16）。

---

## §2 #32｜CPATH 理论模拟实测 —— **未决（端点配额阻断）**

### 2.1 设计字面（先核后用）
源件 `docs/V3X/CPATH_SIMULATION_REPORT_2026_09_10.md` §7.2「若实测 C 路径（成本 ~0.05 USD）」5 步：30 question → `doubao-embedding-vision-251215` 2048-d embedding → cos sim(30,22) 取 top-3 caption → 拼 `Question / Context / Answer` prompt → `glm-latest` 30 cells with context → 对比 no-RAG 22/30。判定带字面：**0% ~ +26.7%**（§5）。

### 2.2 实测数据摘要
| 项 | 结果 |
|---|---|
| 22 caption 原文复原 | **成功**（22/22，按 `caption_construction` 字面；样例 `Concept graph L_algorithm_process (family=L, structure=llm_generated_dag, N=38, n_named=29): 问题输入; 数据预处理; 特征工程`） |
| embedding（22 caption + 30 question，3+3 批） | 首跑 6/6 成功（2048-d） |
| top-3 检索 | 首跑 30/30 完成 |
| with-RAG 30 cells | **12/30 完成后阻断**（第 13 条起 HTTP 429） |
| 阻断原因 | `AccountQuotaExceeded`（HTTP 429），端点原文：月度配额耗尽，**2026-09-30 23:59:59 +0800 CST 重置** |
| with-RAG 边际 | **不判定**（12/30 不构成 30-cell 全体，不外推） |

**no-RAG 侧 0-LLM 成果（已落盘）**：baseline 件的 stored 抽取器本体不可得，故以本脚本显式声明的抽取器对**已存 30 条 response_text** 重判：
- 重判 **24/30 = 80.0%**（gsm8k **15/15**、strategyqa **9/15**）
- stored 值 **22/30 = 73.3%**（gsm8k 13/15、strategyqa 9/15）
- 差额 **−2**，**全部落在 gsm8k**（strategyqa 两侧同为 9/15）；根因 = 抽取器口径差异（我的抽取器优先首个 `**bold**` 数字/`\b(yes|no)\b`，原抽取器未落盘不可比对），**非 RAG 效应**。旁证：baseline 件 id=1 的 `response_text` 以 `**18**` 开头且 18.0 正是正确答案，但 stored `extracted_number` 记为 5.0 —— 原抽取器取了正文后续数字而非首个粗体答案。

**已观测但未落盘的 12 条**（首跑 stdout 存活，逐条 response_text 与 usage 随进程崩溃丢失，如实登记不做补写）：
`id=1→18.0✓ / 2→5.0✓ / 3→40.0✓ / 4→1430.0✓ / 5→36.0✓ / 6→8000.0✓ / 7→36.0✓ / 8→6.0✓ / 9→40.0✓ / 10→140.0✓ / 11→2125.0✓ / 12→32.0✓`（12 条全为 gsm8k，12/12 正确；baseline gsm8k 亦 13/15）。**此 12 条不可用于边际判定**（分母不齐）。

### 2.3 判定
**未决。** 30-cell with-RAG 实测未完成，理论边际带（0% ~ +26.7%）既未证伪也未成立。原报告 §7.3「若不实测，维持 no-RAG 22/30 = 73.3% 作为本轮 baseline」在实测缺席下**继续有效**。

### 2.4 根因
- **α（端点/预算）**：Volcengine Ark Coding Plan 月度配额耗尽（429 `AccountQuotaExceeded`），非代理/并发/节流问题；`2026-09-30 23:59:59 +0800` 自动重置。
- **β（调用规模）**：设计需 6 次 embedding + 30 次 chat = 36 次；会话内实际成功 18 次，耗尽于第 19 个请求之后。
- **γ（资产缺口）**：baseline 件只落盘抽取结果，**抽取器本体未落盘**，致 stored 22/30 与重判 24/30 口径不可比。
- **复合**：「不明」未解除，且根因由单因（「0.05 USD 未执行」）扩为**端点配额 + 抽取器口径**双因。即便配额恢复，仍须先统一抽取器口径，否则 22/30 与 with-RAG ?/30 不可比。

---

## §3 #21｜KT-B1 失真上界真测 —— **占位已除，仍不明（测法轴退化）**

### 3.1 设计字面与测法锚
原报告 `KT_B1_REWORK_REPORT_2026_09_10.md` §三 表给出三行（通用基线失真上界 / deposon 占位 / 裁定）；§六.2 遗留事项 2 给出**仓内唯一可算的真测字面**：

> 「如需真正判定差异化，**需从 v19 守恒残差（2.22e-16）反向估计 deposon 失真上界**」

内部判死线（`KT_B1_SPEC_V0.1` §1.1/§2.5）：**失真上界 ≥ 0.95** 达标（= 失真度 ≤ 0.05）。

### 3.2 实测数据摘要
| 项 | 结果 |
|---|---|
| 测法 | `conservation.check_conservation_graded(v19, v19).max_deviation` |
| 记录数 | **1,592**（v19 全量，非抽样） |
| 实测 deposon 失真上界 | **2.220446049250313e-16** |
| 十六进制 | `0x1.0000000000000p-52` = **2⁻⁵² = IEEE 754 双精度机器 epsilon** |
| layer1 / layer2 | 2.220446049250313e-16 / 0.0 |
| 分级审计裁定 | PASS（残差 < 1e-15） |
| stored vs 独立复算 | **一致**（`physics_audit.t_plus_r_plus_a_max_deviation` 同值） |
| 占位替换 | B1/B2 `0.5` → 2.220e-16；B3 `0.05` → 2.220e-16 |

**GRAY 标签语义自识别**（原 BOSS 脚本缺失，用原报告 §三 的 3 行三元组反推，不择一冒充）：

| 候选读法 | 含义 | 复现原标签 |
|---|---|---|
| A | ABOVE/BELOW = 相对 0.95 判死线的位置 | 2/3 |
| **B** | **ABOVE/BELOW = 通用基线值相对 deposon 值的高低** | **3/3 ✓ 唯一** |

**按识别语义重判**：

| BOSS | 通用基线（报告值） | deposon 占位 | deposon 实测 | 原裁定 | **重判** | 翻转 |
|---|---|---|---|---|---|---|
| B1 Sinkhorn OT | 0.0004 | 0.5 | 2.220e-16 | GRAY_BOTH_BELOW | **GRAY_BOTH_ABOVE** | ✎ BELOW→ABOVE |
| B2 KD | 0.0028 | 0.5 | 2.220e-16 | GRAY_BOTH_BELOW | **GRAY_BOTH_ABOVE** | ✎ BELOW→ABOVE |
| B3 LLMLingua | 0.4634 | 0.05 | 2.220e-16 | GRAY_BOTH_ABOVE | GRAY_BOTH_ABOVE | — |

对 0.95 内部判死线：deposon 侧 2.220e-16 ≪ 0.95 → **内部判死线 FAIL**（与攻击成功率 ≥ 50% PASS 交叉落 `GRAY_DOWN` 档，`KT_B1_SPEC` §9.2）。

### 3.3 判定
**仍标「不明」**，但根因置换：
- ✅ **占位问题解除** —— 0.5/0.05 已由实测值替换，B1/B2 标签随之翻转。
- ❌ **通用基线仍未真受审** —— B1/B2/B3 的真实脚本（锚 SHA `19325960b8be` / `1781ea2f742d` / `c0b55e0385a4`）与 P-B V0 §7 五锚之一 `tools/distortion_calculator.py` **本仓均不存在**；原始 `D(M,T)=E_π[Σ_t|u*(a_t)−u(a_t)|/max_u]` 无实现载体，无法复算通用基线值（表列 0.0004/0.0028/0.4634 只能**引用报告值，不可复算**）。
- ⚠️ **翻转是退化测法的产物，不是证据** —— 实测值 2.220e-16 是构造恒等 `T=(1−η)v, R=η·g_couple·(1−v), A=1−T−R ⇒ T+R+A≡1` 的双精度舍入极限（`conservation.py` L13 自述「合成恒守恒」），**不含任何关于 deposon 相对 Bayesian 基线信息失真的证据**。不得据此宣称 deposon 优于 OT/KD/LLMLingua。

### 3.4 根因
- **α（测法轴）**：守恒残差 = 构造恒等的舍入极限，2⁻⁵² 量级，**无鉴别力**。与 Trae §1.2 #5「540 cells 守恒 STRICT_CONSERVATION = 结构性恒等，不构成实验证据」同根因。
- **β（资产缺失）**：3 个 BOSS 脚本 + `tools/distortion_calculator.py` 仓内不存在 → 通用基线不可复算，失真上界只能取 proxy。
- **γ（语义）**：GRAY_BOTH_ABOVE/BELOW 语义此前未定；本次以原报告三元组**自识别并钉死为读法 B**（3/3 复现）——此项为净增量。
- **复合**：占位 → 真值的替换**已完成且可复算**；但因 α，B1/B2 的 BELOW→ABOVE 翻转**不构成差异化结论**。#21 若要真正解除，须补回 3 个 BOSS 脚本与 `distortion_calculator.py`，或改用非恒等的信息论失真度量。

---

## §4 #19｜P-G boss_pg 三项实跑 —— **成立（PASS 2 / GRAY 1 / FAIL 0）**

### 4.1 前提更正（对派工单与 Trae 回函 #19 均成立）
派工单与 Trae 回函 #19 均把「540」读作 **540 次 LLM 调用**。按源件字面核对：

- `P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC` §4.3 资源约束：「**0 LLM 调用** / 不设 proxy」；§5 铁律 1 同；§4.1 D5「9 model × 60 cells 双曲 transport 实算（**0 LLM**）」
- 3 个 `boss_pg_*.py` 的 `iron_rule_compliance` 全部：`0_LLM: True` / `no_proxy: True` / `no_api_key_read: True`
- `_pg_v01_compute.py` 方法声明：「0 LLM, 0 proxy, 0 API, pure numpy」

→ **540 = 9 model × 60 cells 的已实算 cell 数，非 LLM 调用次数**；且该 540-cell 数据**早已落盘**（`deposon_pg_v01_9m60c_2026_09_15.json`）。真实缺口不是「540-LLM 数据未落盘」，而是**3 个 BOSS 的真实逻辑为 SCAFFOLDING TODO**（`real_implementation_status: 'TODO (D5 launch pending)'`）。
→ **本条实跑 LLM 调用数 = 0；无需 tun 代理；无需 key。**

### 4.2 实测数据摘要（判定值全部由 PRE-REGISTRATION 判定线机械产生）
| BOSS | 统计量（实算） | 判定线（预注册字面） | 裁定 |
|---|---|---|---|
| **BOSS-PG-1** 黎曼退化 | median ‖T_{c=1}(x) − T_{c=0.001}(x)‖₂ = **0.041495**（min 0.027595 / max 0.061852） | <0.01 FAIL / [0.01,0.10) GRAY / ≥0.10 PASS | **GRAY** |
| **BOSS-PG-2** 双曲分类坍缩 | std of 36 pairwise d_H = **0.553613**（mean 1.005264 / min 0.154459 / max 2.276531） | <0.05 FAIL / [0.05,0.20) GRAY / ≥0.20 PASS | **PASS** |
| **BOSS-PG-3** 测地线违反 | median violation = **3.560e-16**（min 1.988e-16 / max 5.288e-16） | <1e-6 PASS / [1e-6,1e-3) GRAY / ≥1e-3 FAIL | **PASS** |

**SUMMARY：PASS 2 / GRAY 1 / FAIL 0 —— 无 kill-line 触发。**

**方法自纠（老实交代）**：BOSS-PG-3 首版实现把「切向增量范数」错写成 `‖log_0(x(t))‖`（绝对范数）对比 `t·‖v‖`，得 median 11.4 → 误报 FAIL。根因：`log_0` 是切空间线性映射，`log_0(x(t)) − log_0(x0) = (t−1)z₀ + t·v`，仅 t=1 时等于 `v`（实测该点 rel 8.4e-16）。**已改为检验双曲半径 `atanh(‖Exp_0(t·w)‖)` 对 `t·‖w‖` 的线性性**（`w = Log_0(x0)+v`，即 Exp_0 局部等距 → 双曲速度 `dg/dt` 恒定），复算得 3.560e-16 = 机器 epsilon 量级，与「Exp_0 与 Log_0 互逆」的理论预期一致。**首版 FAIL 属本 worker 实现缺陷，非实验发现，已弃用不引用。**

### 4.3 判定
**三项 SCAFFOLDING 实跑成立，无 FAIL。** P-G 方向通过其自设的三项自测：判别信号不坍缩（PG-2 PASS）、测地线严格保持（PG-3 PASS）、双曲 transport 相对欧几里得呈**边缘非退化**（PG-1 GRAY，0.0415 落在 [0.01, 0.10) 预注册 GRAY 带内）。
→ Trae §1.2 #19「不明」**解除**，改标 **真成立（0 FAIL）**。
→ 但 **BOSS-PG-1 的 GRAY 本身即结论**：双曲空间在 c=1 vs c=0.001 下仅中度分离，P-G 的「非欧增量」在预注册线上并未达到 PASS 所需的显著非退化。

### 4.4 根因
- **α（判据）**：三项均按预注册判定线机械判定，**0 FAIL**，无判死线触发；PG-1 停在 GRAY。
- **β（鉴别力警告）**：BOSS-PG-3 的 PASS 值 3.560e-16 是 **Exp_0/Log_0 互逆的构造恒等**的舍入量级，与 Trae #5 同根因 —— **该 PASS 不得引用为「测地线/平行移动性质经实验证实」**，它只证明实现自洽。另 BOSS-PG-1 的 delta 依赖 `_pg_v01_compute.main()` 既定 velocity `v=(0.08,−0.02)`（非预注册扫描量），故 GRAY 结论对该 velocity 敏感。
- **γ（前提）**：540 的性质（cell 数 ≠ LLM 调用数）与「数据未落盘」的记述均需更正，见 §4.1。
- **复合**：#19 从「不明（SCAFFOLDING 未实跑）」变为「真成立（0 FAIL）」，但需附带「PG-3 属构造恒等、PG-1 停在 GRAY」两条限定，方不误导。

---

## §5 LLM 调用账

| 项 | 值 |
|---|---|
| 成功调用 | **18**（embedding 6 = 3 caption 批 + 3 question 批；chat **12** = with-RAG cell 1–12） |
| 失败调用 | **6**（HTTP 429 `AccountQuotaExceeded`：首跑 cell 13 的 3 次重试 + 手工 chat 探针 1 + 手工 embedding 探针 1 + 末跑 embedding 1） |
| 会话内 HTTP 请求总数 | **24** |
| 串行 | 是（单进程 `for` 循环，**0 并发**） |
| 最小间隔 | **≥ 2.5 s**（脚本内 `_throttle()` 对每次请求强制；手工探针为单发，无突发） |
| 并发轰炸 | **无** |
| 端点 | `ark.cn-beijing.volces.com/api/coding/v3`（chat，`glm-latest`）与 `.../embeddings`（`doubao-embedding-vision-251215`） |
| tun 代理 | **未启用**——Volcengine Ark 既非 teamorouter 亦非 openrouter，铁律不适用（#19/#21 为 0 调用，不涉及） |
| key 读取 | runtime `os.environ['ARK_API_KEY']`（env 优先，key 文件 `C:/Users/Administrator/Desktop/AI/新建文本文档.txt` **不存在**，未回落） |
| key 明文自扫 | 6 件产出（3 数据 JSON + 3 脚本）全量扫 `完整 key` / `key 前 12 位` / `ark-` 三种模式 → **全部 clean** |
| 成本 | 12 次 chat 的 `usage` 随首跑崩溃丢失，**落盘件无法计算成本**；不估算不编造 |

---

## §6 产出件清单

| 件 | 路径 | 字节 | SHA-12 |
|---|---|---|---|
| 判定件 | `results/_v3_n_recheck_llm_verdict_2026_09_27.md` | （本件） | 见落盘实算 |
| #32 数据 | `results/_v3_n_cpath_live_data_2026_09_27.json` | 12,711 | `25374AF92F88` |
| #21 数据 | `results/_v3_n_ktb1_distortion_bound_data_2026_09_27.json` | 6,411 | `26C0D0B0FFB6` |
| #19 数据 | `results/_v3_n_pg_boss_live_data_2026_09_27.json` | 9,220 | `BE11C5274807` |
| #32 runner | `deposon_team/plugins/_v3n_cpath_live_2026_09_27.py` | 19,823 | `5248BA7AC21C` |
| #21 runner | `deposon_team/plugins/_v3n_ktb1_distortion_bound_2026_09_27.py` | 13,055 | `5572EF4055A5` |
| #19 runner | `deposon_team/plugins/_v3n_pg_boss_live_2026_09_27.py` | 14,223 | `B6040D34F0AC` |

三个 runner 均带 `if __name__ == '__main__'` guard、逐阶段 checkpoint（被阻断亦落盘已完成部分）、`PYTHONDONTWRITEBYTECODE=1` 下 `python -B` 实跑通过。

---

## §7 skill fallback 与老实交代

### 7.1 skill
派工单指定 skill `scientific-research-workflows:experimental-design`（plugin `@scientific-research-workflows`）。**本 session 未能在可及工具面加载该 skill**（catalog 仅列技能描述，session 内无 `skill` 加载工具）。故 **0 编造 skill 虚构指令**，全部实验设计取自**各条源件内的实验设计字面**（先核后用、逐件登记，见 §1 与各条 §x.1）：
- #32 ← `CPATH_SIMULATION_REPORT_2026_09_10.md` §4.1/§4.2/§4.3/§7.2/§7.3
- #21 ← `KT_B1_REWORK_REPORT_2026_09_10.md` §三/§六.2 + `KT_B1_SPEC_V0.1.md` §1.1/§2.5/§4.1-§4.3/§9.2
- #19 ← `P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md` §1.2/§4.3/§5 + 3 个 `boss_pg_*.py` 的 PRE-REGISTRATION 常数与判定线字面

### 7.2 老实交代清单
1. **#32 未完成** —— 端点月度配额 2026-09-30 23:59:59 +0800 重置前无法补跑；边际**不判定**。
2. **#19 派工单前提需更正** —— 540 是 cell 数不是 LLM 调用数；数据早已落盘；真实缺口是 3 个 BOSS 的 TODO。**本条实际 LLM 调用 0 次**，故「540 次串行 ≥22.5 分钟 / 1–2 小时 / 拆 3 批」的节流预算**不适用**。
3. **#21 三件资产仓内缺失** —— `.mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py`、`boss_b2_kd.py`、`boss_b3_llmlingua.py`、`tools/distortion_calculator.py`，故通用基线 0.0004/0.0028/0.4634 **只能引用报告值，不可复算**；原始 `D(M,T)` 失真度**无实现载体**。
4. **#21 抽取器不可得** —— baseline 30cells 的抽取器本体未落盘，stored 22/30 与重判 24/30 差 2（全部在 gsm8k）归因于口径差异，**该差额不可进一步分解**。
5. **BOSS-PG-3 首版 FAIL 是本 worker 的实现缺陷**（§4.2 方法自纠），已修，非实验发现。
6. **12 条 with-RAG 逐条读数未落盘** —— 逐条 `response_text`/`usage` 随进程崩溃丢失，仅存活 stdout 摘要（§2.2），**不可用于边际判定**。
7. **BOSS-PG-1 结论对 velocity 敏感** —— `v=(0.08,−0.02)` 取自既有实现而非预注册扫描量；GRAY 结论未做敏感性扫描（0 新设阈值下不擅自加扫描维度）。
8. **#21/#19 的若干 PASS/GRAY 值落在机器 epsilon 量级**（2.22e-16 / 3.56e-16），属构造恒等，**鉴别力为零**；已逐条标注，**不得作为正面实验证据引用**。
9. **未合并任何派生 JSON**；**未触动任何既有件**（4/4 首测输入 SHA-12 逐一 MATCH；16/16 frozen PASS）。

---

## §8 待 PI 拍板项（如实登记，未擅自处置）

1. **#32 补跑时点**：配额 2026-09-30 重置后是否补跑 30-cell with-RAG（需 6 embedding + 30 chat）？若不补跑，C 路径维持 §7.3 的「不实测」建议。
2. **#32 抽取器口径**：stored 22/30 与重判 24/30 的 −2 差额（全部在 gsm8k）需 PI 裁定采用哪一口径（须先定位/重写抽取器）。
3. **#21 是否补回缺失资产**：3 个 BOSS 脚本 + `tools/distortion_calculator.py` 是否从 archive 回填（属资产处置，超 worker 权限）。
4. **#21 失真上界测法**：现行 proxy（守恒残差）已证无鉴别力，是否改采非恒等信息论失真度量（属新设判据，须 PI 拍板，worker 不擅自）。
5. **#19 BOSS-PG-1 敏感性**：是否对 transport velocity 做扫描以确定 GRAY 结论的稳健性（属新增实验维度，须 PI 拍板）。
6. **#19 前提更正的回写对象**：Trae 回函 §1.2 #19 的「540-LLM 数据未落盘」表述需更正为「540-cell 数据已落盘 + BOSS 逻辑 SCAFFOLDING」；回写落点（勘误件 or 新件）请 PI 指定，worker 未擅改任何既有件。

---

**出件方**：Mavis 团队 worker（agent: worker）｜2026-09-27
**署名如实**：本件由 worker 出件；输入引用件（Trae 回函 / 09-10 报告 / 09-15 spec / 3 个 boss_pg 脚本 / v19 件 / conservation.py）均为**原始出证方**，本件只作引用，未以其名义出证。
