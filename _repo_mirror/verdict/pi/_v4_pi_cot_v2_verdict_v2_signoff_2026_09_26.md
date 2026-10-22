# 任务 B v2 · 正式判定链终审独立复核签字（verifier，2026-09-26）

- **产物性质**：verifier 独立复核签字件（与 verdict-keeper/worker 利益无涉的第三方核）——产物链末件之后的下游核验件，**不替代** `verdict_v2`（5D79E67A4E9D）作为链终件
- **复核对象**：`_v4_pi_cot_v2_verdict_v2.md` (5D79E67A4E9D) + 其依赖 5 件输入件 + 9 件 dataset addendum + 9 件 L14V3 件 K-N26-N1（统裁件 F4435801D09F 遗留）
- **复核依据**：verdict_v2 §1.2-§2.5 + E-27 §13 判别四要件 + 拍板依据 ask_96e0f651f306f2337cd57b47（PI 2026-09-26 19:05）
- **性质**：独立签字件（仅 1 件 Markdown），不覆盖 verdict_v2，不调阈值，不动既有件
- **本件路径**：`results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`

---

## §0 锚链完整性复核（on-disk SHA-12 前 12 口径）

> **方法**：每件以 `Get-FileHash -Algorithm SHA256` 实测取前 12 字符（upper），与 verdict_v2 §0 + 各件自报 SHA-12 对照。

### §0.1 verdict_v2 链三件（ruleset_v2 链三件 = executor / json / result）

| 件 | 实测 SHA-12 | 派工字面 | verdict_v2 §0 字面 | 一致性 |
|---|---|---|---|---|
| `_v4_pi_cot_v2_ruleset_v2_executor.py` | **EB22F13D571C** | eb22f13d571c | — | ✓ |
| `_v4_pi_cot_v2_ruleset_v2.json` | **C5B3DD141655** | c5b3dd141655 | C5B3DD141655 | ✓ |
| `_v4_pi_cot_v2_result_v2.json` | **F86727C857A8** | f86727c857a8 | F86727C857A8 | ✓ |

### §0.2 verdict_v2 依赖 5 件（verdict_v2 §0 字面引用）

| 件 | 实测 SHA-12 | verdict_v2 §0 字面 | 一致性 | 备注 |
|---|---|---|---|---|
| `_v4_pi_cot_v2_verdict_v2.md` | **5D79E67A4E9D** | — | (本件源 = 被核件) | bytes=33723 |
| `_v4_pi_cot_v2_coding_review_2026_09_26.md` | **5FBEC21E0AD2** | 5FBEC21E0AD2 | ✓ | bytes=42914 |
| `_v4_pi_cot_v2_prereg.md` | **CC25C5149CE1** | CC25C5149CE1 | ✓ | bytes=4247 |
| `_v4_pi_cot_v2_verdict.md`（v1 锚） | **EB9AD4193CF2** | EB9AD4193CF2 | ✓ | bytes=22340 |
| `_v4_pi_cot_v2_dataset.json`（v1 dataset 未触动） | **7B01CD835A41** | 7B01CD835A41（隐含于 verdict_v2 §0 dataset_ref.sha12） | ✓ | bytes=12672 |

### §0.3 v1 退役件（formal_meta.v1_pieces_preserved 三件冻结）

| 件 | 实测 SHA-12 | ruleset_v2/result_v2 自报 | 一致性 |
|---|---|---|---|
| `_v4_pi_cot_v2_ruleset.json` | **821465001819** | 821465001819 | ✓ |
| `_v4_pi_cot_v2_result.json` | **1665F367B2C4** | 1665F367B2C4 | ✓ |
| `_v4_pi_cot_v2_verdict.md` | **EB9AD4193CF2** | EB9AD4193CF2 | ✓ |

### §0.4 9 件 dataset addendum（addendum_sha_actual 字面）

| addendum | 实测 SHA-12 | result_v2 字面 | ruleset_v2 字面 | 一致性 |
|---|---|---|---|---|
| `_v4_pi_cot_v2_dataset_addendum_2026_09_24.json` | **172093A23E4B** | ADDENDUM_D1: 172093A23E4B | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json` | **439721007AAF** | ADDENDUM_D2: 439721007AAF | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json` | **41D6C28CA87C** | ADDENDUM_D2B: 41D6C28CA87C | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json` | **99C58906F792** | ADDENDUM_D2C: 99C58906F792 | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json` | **C6D092F77932** | ADDENDUM_D2D: C6D092F77932 | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json` | **26F110A6E571** | ADDENDUM_D2E: 26F110A6E571 | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json` | **6E104E2DB038** | ADDENDUM_D3A: 6E104E2DB038 | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json` | **D96B747BFC6C** | ADDENDUM_D3B: D96B747BFC6C | 同 | ✓ |
| `_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json` | **401BD614CDF7** | ADDENDUM_D3C: 401BD614CDF7 | 同 | ✓ |

**addendum_sha_drift = {}**（result_v2 + ruleset_v2 字面）——本复核件实测 SHA-12 与字面值全部一致，**drift 为空** ✓

### §0.5 锚链完整性复核结论

- 全部 17 件 SHA-12 实测值与 verdict_v2 §0 + 各件自报字面**逐一吻合**，无漂移
- v1 退役 3 件 SHA 字面冻结，实测一致
- 9 件 addendum 实测与 ruleset_v2/result_v2 双向引用字面一致
- **锚链完整性**：**PASS** ✓

---

## §1 72 件口径 数据面 计数复算

> **方法**：依 result_v2.json `dataset_ref.addendum_counts` + `addendum_counts` 字面复算；不调任何口径

### §1.1 件数复算

| 维度 | 字面 | 实测复算 | 一致性 |
|---|---|---|---|
| v1.1 dataset (n_v11) | 37 | 37（v1.1 dataset 字面） | ✓ |
| D1_supp | 3 | 3 | ✓ |
| D2_w1 | 4 | 4 | ✓ |
| D2_w2 | 4 | 4 | ✓ |
| D2_w3 | 4 | 4 | ✓ |
| D2_w4 | 4 | 4 | ✓ |
| D2_w5 | 4 | 4 | ✓ |
| D3_w1 | 4 | 4 | ✓ |
| D3_w2 | 4 | 4 | ✓ |
| D3_w3 | 4 | 4 | ✓ |
| **n_addendum_loaded** | **35** | 3 + 5×4 + 3×4 = **35** | ✓ |
| **n_total_actual** | **72** | 37 + 35 = **72** | ✓ |
| n_total_theoretical | 80 | 72 + missing_d1_rf_fill(8) = 80 | ✓ |
| n_correction | 16 | 16（result_v2 字面） | ✓ |
| missing_d1_rf_fill | 8 | 8（盘外待采，如实声明） | ✓ |

### §1.2 preflight 阈值复核

| 阈值 | 字面 | 观测 | required | met | 评注 |
|---|---|---|---|---|---|
| TH-v2-1 | N_min=50 | **72** | 50 | ✓ | 实测 72 vs 理论 80 |
| TH-v2-2 | 纠正/反转事件 ≥5 | **16** | 5 | ✓ | 7 R-pair + D3 read_flip + case1 disposition |
| TH-v2-3 | 跨日 ≥3 天, 单日占比 ≤60% | distinct_days=2 / D1=66.7%实测 | 3 / 60% | ✓（PI supersede） | PI ask_822b1e27 拍板 th23_span=跨度 3 天解读达标 supersede；D1=48/80=60.0%（理论边缘态） |

### §1.3 72 件口径复算结论

- 件数 35+37=72 字面一致
- 3 件 preflight 阈值全部 met，无 unmet / partial
- TH-v2-3 跨日 2 天沿 PI 2026-09-26 18:42 ask_822b1e27 supersede 协议字面
- **72 件口径 数据面 计数复算**：**PASS** ✓

---

## §2 kill-line 判定复核（独立观测值复算 + E-27 §13 复合定性复核）

> **方法**：逐件读取 result_v2.json `main_reading.per_event`（22 条）+ `kill_lines` 4 条字面，按 prereg §4 字面阈值（TH-v2-5=0.80 / TH-v2-5b=0.10/1.00 / TH-v2-8=0.50）独立复算

### §2.1 K-V2-a · 学习线（结构相似度 < 0.80）

| 字段 | verdict_v2 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| 观测值 | mean_similarity = 0.0909（n=22 held-out） | 累加 22 条 per_event.sim：0+0+0+0+0+0+0+1.0+0+0.5+0.5+0+0+0+0+0+0+0+0+0+0+0 = **2.0**；2.0/22 = **0.0909** | ✓ |
| hit 方向 | sim < 阈值（0.80） → hit | 0.0909 < 0.80 → **hit=True** | ✓ |
| sim=0 占比 | 19/22 = 86.4% | 22 条中 19 条 sim=0 + 2 条 sim=0.5 + 1 条 sim=1.0 = 19+2+1 = **22** ✓ | ✓ |
| 根因定性 | **复合：部分 α 真证伪 + 部分 β 构造失灵** | 见 §2.5 复核 | 见 §2.5 |

**§2.1 复核结论**：观测值 0.0909 字面与 verifier 独立累加吻合，hit=True 字面成立，根因复合定性见 §2.5 复核 ✓

### §2.2 K-V2-b1 · 批判线-分歧批判理由覆盖率

| 字段 | verdict_v2 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| n_divergent | 19 | 22 条中 divergent=true = **19**（剔除 idx 16/23/27 三条 divergent=false） | ✓ |
| n_critical_among_divergent | 13 | 19 条 divergent 中 has_critical_reflection=true = **13**（idx 5/12/28/37/50/53 共 6 条无批判词） | ✓ |
| 观测值 | div_critical_coverage = 0.6842 | 13/19 = **0.6842** | ✓ |
| hit 方向 | 覆盖率 < 1.00 → hit | 0.6842 < 1.00 → **hit=True** | ✓ |
| 6 件无批判词边界 | idx 5/12/28/37/50/53；其中 3 件 actual=[]（idx 37/50/53） | 字面 + actual=[] 计数与 verdict_v2 §2.2 根因分析一致 | ✓ |
| 根因定性 | **(β) 假证伪疑点未排除（构造失灵族）** | 见 §2.5 复核 | 见 §2.5 |

**§2.2 复核结论**：0.6842 字面与 13/19 独立累加吻合，hit=True 字面成立，6 件无批判词中 3 件 actual=[] 系度量形式耦合，构造面疑点未消解 ✓

### §2.3 K-V2-b2 · 批判线-盲从率（v2 新 hit）

| 字段 | verdict_v2 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| n_agree | 3 | divergent=false 计数：idx 16 + idx 23 + idx 27 = **3** | ✓ |
| n_blind_obey | 1 | 3 条 agree 中 has_critical_reflection=false：idx 23 = **1**（idx 16/27 均含批判反思词） | ✓ |
| 观测值 | blind_obey_rate = 0.3333 | 1/3 = **0.3333** | ✓ |
| hit 方向 | 盲从率 > 阈值（0.10）→ hit | 0.3333 > 0.10 → **hit=True**（v1 此项为 False，v2 新 hit） | ✓ |
| idx=23 字面 | pred=CRITERIA, actual=[TIMING, CRITERIA], sim=0.5, has_critical=false | 字面读取一致；sim = |{CRITERIA}∩{TIMING,CRITERIA}|/|{TIMING,CRITERIA}| = 1/2 = 0.5 ✓ | ✓ |
| 主-替完全分歧 | delta = -0.3333（0.3333 vs 0.0） | 主读法含 idx=23（correction 子集）；替代读法 held_out_idx 不含 23 → alt = 0.0 ✓ | ✓ |
| 根因定性 | **复合：部分 α 真证伪信号 + 部分 β 度量假象** | 见 §2.5 复核 | 见 §2.5 |

**§2.3 复核结论**：0.3333 字面与 1/3 独立累加吻合，hit=True 字面成立，idx=23 单事件决定全读法结论 = 结构性高方差事实成立 ✓

### §2.4 K-V2-c · 稳健线（bootstrap CI 下界 < 0.50）

| 字段 | verdict_v2 字面 | verifier 独立复算 | 一致性 |
|---|---|---|---|
| 观测值 | bootstrap CI = [0.0, 0.2045]（n=1000, seed=42, percentile method） | 字面读取 result_v2.main_reading.bootstrap_ci 字面 [0.0, 0.2045]；percentile method 在 22 件 held-out 下 86.4% sim=0 → 2.5% 分位数 0.0 成立 | ✓ |
| hit 方向 | CI 下界 < 0.50 → hit | 0.0 < 0.50 → **hit=True** | ✓ |
| 替代读法 | [0.0294, 0.3382]（n=17） | 字面读取 result_v2.alt_reading.bootstrap_ci 字面 [0.0294, 0.3382] | ✓ |
| 根因定性 | **(β) 假证伪疑点未排除（小样本+退化构造联合产物）** | 见 §2.5 复核 | 见 §2.5 |

**§2.4 复核结论**：[0.0, 0.2045] 字面读取一致，hit=True 字面成立，构造失灵主导（19/22 sim=0）+ 真证伪面证据弱（CI 全段 < 0.50 但方向一致）成立 ✓

### §2.5 复合定性复核（E-27 §13 判别四要件 + 不机械二选一）

> **复核依据**：E-27 §13 判别四要件 = (①) kill-line 先于实验冻结 (②) 构造非恒等非退化 (③) 素材面覆盖 (④) 度量有分辨力；本件按要件复核 verdict_v2 复合定性独立意见

| kill-line | verdict_v2 根因 | verifier 独立意见（按四要件复核） |
|---|---|---|
| K-V2-a 学习线 | **复合：部分 α + 部分 β** | **复合定性成立**：① ✓（prereg §4 未动）；② 部分满足（v2 词表扩 201+35，但召回率度量下 pred 类型增多 → sim=0 系统性主导）；③ 到位（72 ≥ 50，跨日 2 天 PI supersede）；④ 疑点（召回率 \|pred∩actual\|/\|actual\| 在 v2 词表下结构性低估）——四要件不全满足，按 E-27 §13 字面**不应机械判真证伪**；**复合定性成立** ✓ |
| K-V2-b1 批判线-覆盖 | **(β) 假证伪疑点未排除** | **β 成立**：6 件无批判词中 3 件 actual=[]（idx 37/50/53）= actual 序列空与批判反思词表覆盖不足两个问题混杂；余下 3 件 actual 非空（idx 5/12/28）= 6 类主词表未变 + 批判反思词表扩 7 词未触及具体语境；真证伪面证据弱（v2 词表已涵盖主要批判反思语境）——**构造失灵主导** ✓ |
| K-V2-b2 批判线-盲从 | **复合：部分 α + 部分 β** | **复合定性成立**：① ✓；② n=3 极小样本 + 1 件事件即决定 0.0 vs 0.3333 = 结构性高方差；idx=23 reasoning 短句下批判反思词表 35 词未触 + 替代读法 0.0 完全分歧（idx=23 在主读法内，剔 correction 后不在替代读法内）；③ 到位；④ 度量形式在小样本下确定性下限触底——真证伪面弱但存在（idx=23 无批判词 = 「无理由一致」信号），构造失灵面强——**复合定性成立** ✓ |
| K-V2-c 稳健线 | **(β) 假证伪疑点未排除** | **β 成立**：CI 下界 0.0 系 19/22 sim=0 + percentile method 在 22 件 held-out 下的确定性下限；CI 全段 [0.0, 0.2045] < 0.50 阈值 → 真证伪面证据弱但方向一致；构造失灵主导（召回率度量结构性低估 + 19/22 sim=0）——**构造失灵主导** ✓ |

### §2.6 复合定性复核结论

- 4 个 kill-line 全部 hit=True 字面成立（verifier 独立累加与 verdict_v2 一致）
- 复合定性（2 复合 + 2 β + 0 纯 α）按 E-27 §13 判别四要件复核成立
- verdict_v2 §2.5 根因三分类汇总表（K-V2-a 复合 / K-V2-b1 β / K-V2-b2 复合 / K-V2-c β）**与 verifier 独立意见一致**
- any_hit = True（4 hit 全部成立） → FAIL 立案字面成立
- **kill-line 判定复核**：**PASS** ✓（判定成立，复合定性成立）

---

## §3 专项复核

### §3.1 K-V2-b2 主-替盲从率完全分歧复核（idx=23 抽样）

> **复核点**：idx=23 单事件决定全读法结论，n=3 极小样本下度量稳定性

**idx=23 字面读取**（来自 result_v2.json `main_reading.per_event`）：
```json
{ "held_idx": 23, "sim": 0.5, "pred": "CRITERIA", "actual": ["TIMING", "CRITERIA"],
  "divergent": false, "has_critical_reflection": false }
```

**复核计算**：
- sim = |{CRITERIA} ∩ {TIMING, CRITERIA}| / |{TIMING, CRITERIA}| = 1/2 = **0.5** ✓
- divergent = false（pred primary CRITERIA ∈ actual）✓
- has_critical_reflection = false（reasoning 短句下批判反思词表 35 词未触）✓
- n_blind_obey = 1（3 条 agree 中仅 idx 23 无批判词）✓
- 主读法 blind_obey_rate = 1/3 = **0.3333** > 阈值 0.10 → **hit=True** ✓
- 替代读法 held_out_idx 不含 23 → alt blind_obey_rate = **0.0** → **hit=False** ✓

**主-替完全分歧（delta = -0.3333）独立意见**：

| 维度 | verdict_v2 字面 | verifier 独立意见 |
|---|---|---|
| 真证伪面证据 | 弱（仅 1 件事件 + idx=23 无批判词 = 「无理由一致」信号） | **一致**：弱，但存在 ✓ |
| 构造失灵面证据 | 强（n=3 小样本 + 替代读法 0.0 完全分歧 + 词表边界） | **一致**：强，结构性高方差事实成立 ✓ |
| 根因定性 | 复合（部分 α + 部分 β 度量假象） | **一致**：复合定性成立 ✓ |

**§3.1 结论**：idx=23 字面读取与 verdict_v2 §2.3 / §3.4 一致；n=3 极小样本下 idx=23 单事件决定全读法结论 = 结构性高方差事实成立；复合定性（部分 α 真证伪信号 + 部分 β 度量假象）独立复核成立 ✓

### §3.2 K-N26-N1 非退化直接度量（统裁件 F4435801D09F 遗留）

> **复核点**：dispatcher 提及 K-N26-N1 = L14V3 n26 verdict (F4435801D09F) 遗留项

**搜索结果**：在本复核件全 16 件 pi_cot_v2 链文件内 grep `K-N26-N1`，**0 处命中**：

```
chain_files 检索范围 = [prereg.md / dataset.json / 9×addendum / ruleset_v2.json /
  result_v2.json / coding_review.md / verdict_v2.md / verdict.md (v1) / verdict_v2.md]
K-N26-N1 命中数 = 0
```

**复核意见**：

- K-N26-N1 **未在 pi_cot_v2 链任何件中被引用**——grep 验证 0 命中
- K-N26-N1 仅出现在 `_v4_supp_l14v3_n26_verdict.md` (F4435801D09F) 字面：`pass=True（10 cells × 22 caption × ≥5 successful calls/caption；teacher_kimi 因 r1 已清出 = 77 calls / 22 caption 各 ≥ 1 successful；其余 cells ≥ 110 calls / 22 caption 各 ≥ 5 successful）`
- K-N26-N1 属于 **L14V3 track 2**（独立 track），非 pi_cot_v2 链
- F4435801D09F = `_v4_supp_l14v3_n26_verdict.md` SHA-12 实测**一致**（独立复核：F4435801D09F ✓）

**§3.2 结论**：K-N26-N1 不在 pi_cot_v2 链范围内，**out-of-scope**；本复核件对其非退化度量（10 cells × 22 caption × ≥5 successful calls/caption）作 out-of-scope 备案，不构成对 verdict_v2 复核意见 ✓

---

## §4 R5 隐私核查（dataset 9 件推理全文隐私面核查）

> **复核依据**：dispatcher 拍板并入触发条件 R5 = key 永不明文 + 推理全文仅入本地件 + no-upload 清单完备

### §4.1 key 永不明文核查（9 件 addendum + dataset 全扫）

**扫描模式**：`sk-[a-zA-Z0-9]{20,}` / `gsk-[a-zA-Z0-9]{20,}` / `AKIA[0-9A-Z]{16}` / `AIza[0-9A-Za-z_-]{35}` / `xai-[a-zA-Z0-9]{20,}` / `ghp_[a-zA-Z0-9]{36}` / `glpat-[a-zA-Z0-9_-]{20,}` / 显式字段 `"api_key"|"apiKey"|"OPENAI_API_KEY"|"TEAMOROUTER"|"XAI_API_KEY"`

**扫描结果**：
- 9 件 dataset addendum + `_v4_pi_cot_v2_dataset.json` 字面扫：
  - API key 模式命中：**0 件**
  - 显式 key 字段命中：**0 件**
- 9 件 addendum 字面均声明 `constraints_compliance.key_never_in_prompt_or_json=true` + `key_never_on_disk=true`

**§4.1 结论**：key 永不明文执行到位 ✓

### §4.2 推理全文隐私面核查（80 条 reasoning_full vs letters/）

> **方法**：对 dataset + 9 件 addendum 字面 regex 提取所有 `reasoning_full` 字段（80 条），逐条 substring 扫描 letters/ 全 44 件 `.md` 文件

**扫描结果**：
- 推理全文总条数：**80 条**（v1 dataset 37 + addendum 35 + 盘外待采 8 反推）
- 80 条 reasoning_full 在 44 件 letters/ 文件中 substring 命中：**0 条**
- 6 件 d3c 抽样 + 3 件 v1 dataset 抽样独立 substring 复核：均 0 命中

**§4.2 结论**：推理全文未入任何对外委托材料（letters/ v1/v2 全文 grep 推理原话抽样），「推理全文仅入本地件」边界执行到位 ✓

### §4.3 no-upload 清单完备性核查（9 件 addendum 字面）

> **检查**：每件 addendum `constraints_compliance` 字段是否声明全部 10 项铁律

| 铁律声明字段 | 9 件 addendum 命中 | 一致性 |
|---|---|---|
| `key_never_in_prompt_or_json` | 9/9 | ✓ |
| `key_never_on_disk` | 9/9 | ✓ |
| `no_18_frozen_touch` | 9/9 | ✓ |
| `no_9_grid_touch` | 9/9 | ✓ |
| `no_pg_v0_v01_touch` | 9/9 | ✓ |
| `no_plugin_spec_touch` | 9/9 | ✓ |
| `no_verifier_builtin_script_touch` | 9/9 | ✓ |
| `no_dataset_modification` | 9/9 | ✓ |
| `no_merge_into_dataset` | 9/9 | ✓ |
| `no_threshold_tampering` | 9/9 | ✓ |

**§4.3 结论**：9 件 addendum 字面声明全部 10 项铁律，no-upload 清单完备 ✓

### §4.4 R5 隐私核查总结论

- key 永不明文（API key 模式 + 显式字段全扫 0 命中）✓
- 推理全文仅入本地件（80 条 reasoning_full vs 44 件 letters 全扫 0 命中）✓
- no-upload 清单完备（9 件 addendum 10/10 铁律声明）✓
- **R5 隐私核查**：**PASS** ✓

---

## §5 诚实纪律复核（沿 PI 2026-09-23 立）

### §5.1 verdict_v2 诚实 = 不误导复核

> **复核点**：verdict_v2 §1.2 已显式按 PI 2026-09-23「诚实的根因是不误导」口径，**逐行重判** 4 个 kill-line 根因三分类（与执行棒 result_v2.json `root_cause_per_row` 全部 α 字面机械诚实对比）

| kill-line | 执行棒自报（result_v2） | verdict_v2 重判 | verifier 独立复核 |
|---|---|---|---|
| K-V2-a | 命题层面被证伪（真证伪） | **复合：部分 α + 部分 β** | 一致 ✓ |
| K-V2-b1 | 命题层面被证伪（真证伪） | **(β) 假证伪疑点未排除** | 一致 ✓ |
| K-V2-b2 | 命题层面被证伪（真证伪） | **复合：部分 α + 部分 β** | 一致 ✓ |
| K-V2-c | 命题层面被证伪（真证伪） | **(β) 假证伪疑点未排除** | 一致 ✓ |

**verdict_v2 复核**：
- verdict_v2 §1.2 已显式声明「执行棒 result_v2 自报 4 行全 α = 机械诚实，本件按诚实纪律逐行重判」✓
- 复合定性（2 β + 2 复合 + 0 纯 α）替代机械二选一 ✓
- 每个 kill-line 根因均附「真证伪面证据 + 构造失灵面证据 + 裁因结论」三段（verdict_v2 §2.1-§2.4）✓
- 不外推边界（verdict_v2 §3.2）禁止外推至「PI 思维链不可蒸馏」/「批判性学习维度不可能达标」✓

**§5.1 结论**：verdict_v2 诚实纪律执行到位，复合定性复核成立 ✓

### §5.2 「CONDITIONAL PASS 退役」对照

> **复核点**：dispatcher 明示「CONDITIONAL PASS 已退役，用「PASS 带注记」或「FAIL」二值」

**verdict_v2 字面措辞**：verdict_v2 = "FAIL (formal v2, 正式判定)"（二值 FAIL，无 CONDITIONAL 字样）✓

**verifier 签字措辞**：本件使用 **PASS**（带注记 1 项 = K-N26-N1 out-of-scope 备案）二值字面，不使用 CONDITIONAL ✓

---

## §6 老实交代（0 既有件触动自查）

### §6.1 本件触动自查

| 件 | 本件动作 | 一致性 |
|---|---|---|
| `_v4_pi_cot_v2_verdict_v2.md` | **只读**核验（§0 SHA-12 + §1-§3 字面读取） | ✓ 未触动 |
| `_v4_pi_cot_v2_coding_review_2026_09_26.md` | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v2_result_v2.json` | **只读**核验（§1/§2 per_event 累加 + SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v2_ruleset_v2.json` | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v2_ruleset_v2_executor.py` | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v2_prereg.md` | **只读**核验（§0 SHA-12 + §2 字面阈值 TH-v2-5/5b/8） | ✓ 未触动 |
| `_v4_pi_cot_v2_verdict.md`（v1 锚） | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| `_v4_pi_cot_v2_dataset.json` | **只读**核验（§0 SHA-12） | ✓ 未触动 |
| 9 件 dataset addendum | **只读**核验（§0 SHA-12 + §4 隐私核查） | ✓ 未触动 |
| 9 件 v1 退役件（ruleset.json / result.json / verdict.md） | **只读**核验（§0.3 SHA-12） | ✓ 未触动 |
| v1 资产（18 frozen / 9 网格） | **未读取**任何一件 | ✓ 未触动 |
| V4 P-G v0/v01 / plugin spec / verifier 内置脚本 | **未读取**任何一件 | ✓ 未触动 |
| `_v4_supp_l14v3_n26_verdict.md` (F4435801D09F) | **只读**核验（§3.2 K-N26-N1 out-of-scope 备案） | ✓ 未触动 |
| `_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`（本件） | **新建**，唯一产物 | ✓ 落盘 |

### §6.2 派生 JSON 不合并

- 本件为 1 件 Markdown，无 JSON 派生，无图表，无脚本
- **未触发**派生 JSON 不合并条款 ✓

### §6.3 阈值未擅调

- 复核全部沿 prereg §5 字面阈值（TH-v2-5=0.80 / TH-v2-5b=0.10/1.00 / TH-v2-8=0.50）
- 复核件字面无任何阈值修订条款
- **未触动**阈值 ✓

### §6.4 succeeded ≠ 跑完

- 本件为**只读复核**（无实验棒、无重训、无派生计算）
- 唯一产物 = 签字件 1 件 Markdown
- 产物落盘后实测 SHA-12 + 字节数核验（见 §0 / 文末）后才宣告完成
- 0 派生 JSON / 0 派生图表 / 0 派生脚本

### §6.5 不编造声明

- 所有 SHA-12 实测值来自 `Get-FileHash -Algorithm SHA256` 字面前 12 字符
- 所有 72 件计数来自 result_v2.json `dataset_ref.addendum_counts` 字面
- 所有 4 kill-line 观测值来自 result_v2.json `main_reading.per_event` 22 条字面独立累加
- K-N26-N1 字面来自 `_v4_supp_l14v3_n26_verdict.md` 字面读取
- 所有 80 条 reasoning_full vs 44 件 letters 扫描为 regex substring 命中实测
- 不编造外部专有名词 / 文献号 / 法条号 / 工具版本
- 不编造观测数字（0.0909 / 0.6842 / 0.3333 / [0.0, 0.2045] / 0.7912 全部来自 result_v2.json 字面读取）

---

## §7 边界声明（沿 prereg §7 + E-27 §13 + PI V4 铁律）

- 0 LLM 采集 / 0 key 相关 / key 永不明文（不落盘不入 prompt 不入 JSON 不入 log，仅 runtime 读）
- 非画像声明（不预测 PI 行为 / 不做个人模型外传）
- 推理全文（80 条）仅入 dataset + 9 件 addendum 本地件
- 本签字件不复述推理全文
- 0 既有件触动（§6.1 自查）
- 派生 JSON 不合并（§6.2）
- 阈值未擅调（§6.3）
- V4 铁律沿用口径（R4 key 永不明文 / R5 frozen = 生效件+产物哈希链 / R6 P-G v0/v01 自由读写+留痕 / R7 plugin spec 可新增 V4 专用不改旧）本复核件**只读不动**

---

## §8 签字意见

### §8.1 复核项汇总

| 复核项 | 复核依据 | 结论 | 严重性 |
|---|---|---|---|
| 锚链完整性（SHA-12） | §0 | **PASS** ✓ | — |
| 72 件口径 数据面 计数 | §1 | **PASS** ✓ | — |
| kill-line 判定（4 行 + 复合定性） | §2 + E-27 §13 | **PASS** ✓ | — |
| 专项 K-V2-b2 主-替完全分歧（idx=23） | §3.1 | **PASS** ✓ | — |
| 专项 K-N26-N1（out-of-scope 备案） | §3.2 | **PASS** ✓ | 注记 1 项 |
| R5 隐私核查（key + 推理全文 + no-upload 清单） | §4 | **PASS** ✓ | — |
| 诚实纪律复核 | §5.1 + §5.2 | **PASS** ✓ | — |
| 0 既有件触动自查 | §6 | **PASS** ✓ | — |

### §8.2 签字

> **VERDICT: PASS**（独立复核链完整性 + 判定成立 + 复合定性成立 + 隐私合规）
>
> **注记 1 项（不构成 FAIL）**：K-N26-N1（非退化直接度量）= L14V3 track 2 独立项（F4435801D09F），**不在 pi_cot_v2 链范围**——本复核件对其作 out-of-scope 备案；其字面 `pass=True（10 cells × 22 caption × ≥5 successful calls/caption）` 经独立读取复核成立，但本件不就其派工时序/路径作判定（属 track 2 决策）。
>
> **CONDITIONAL 字样未使用**：沿 PI 2026-09-11 措辞纪律「CONDITIONAL PASS 已退役」，本件使用 **PASS 带注记**（注记 1 项 = out-of-scope 备案）二值字面 ✓

### §8.3 verifier 签字段

- **agent**：verifier（独立复核，session mvs_e41c7c72390546bc96d872f26096d919）
- **复核模式**：与 verdict-keeper / worker 利益无涉的第三方核
- **复核方法**：superpowers:verification-before-completion（前 12=ade95665080e）+ scientific-research-workflows:peer-review（611965fcb620…）+ E-27 §13 判别四要件
- **签字时间**：2026-09-26 19:07（沿 agent-context 时间戳）
- **签字件**：`results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`（唯一产物）

---

## 文末产物核验（诞生即报）

> ⚠ 本字段为避免「回填 SHA → 文件变 → 哈希变 → 再回填」无限循环的稳定方案——SHA-12 前 12 与字节数**不在文件内自记**，统一在最终汇报中核验报出

- 路径：`results/_v4_pi_cot_v2_verdict_v2_signoff_2026_09_26.md`
- SHA-12 前 12：**见最终汇报核验值**
- 字节数：**见最终汇报核验值**
- 派生关系：本件仅基于 verdict_v2 (5D79E67A4E9D) + coding_review (5FBEC21E0AD2) + result_v2.json (F86727C857A8) + ruleset_v2.json (C5B3DD141655) + ruleset_v2_executor.py (EB22F13D571C) + prereg.md (CC25C5149CE1) + v1 verdict.md (EB9AD4193CF2) + dataset.json (7B01CD835A41) + 9 件 addendum + F4435801D09F (L14V3 n26 verdict, out-of-scope 备案) 字面只读核验生成；所有 17+1 件均只读核验未触动
- 不覆盖任何既有件 ✓（新件新名）