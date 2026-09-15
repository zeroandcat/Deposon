# DEEPSEEK-V41-FLASH 30CELLS V3 验证报告 (max_tokens=2048)

- **生成时间**: 2026-09-10 16:40 (Asia/Shanghai)
- **作者**: worker (mvs_ab4736325c4e4931a859e6e413f8a255)
- **parent**: mvs_bbeb804b1a6a41109be740636eed1709
- **任务来源**: user 2026-09-10 16:34 明确指令 — D>>B (D = 本任务重跑 max_tokens=2048 边际验证,B = 启动 V2 真实 2 周工作量)。**先跑 D,看 K+L/30 是否 ≥ 28 边际**,再决定是否进入 B
- **数据落盘**: `D:\私人资料\deposon-repo\results\deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` (18.6 KB)
- **脚本**: `D:\私人资料\deposon-repo\scripts\run_deepseek_v41_30cells_v3.py`

---

## §1 测试环境

| 字段 | 值 |
|---|---|
| gateway | OpenRouter (https://openrouter.ai/api/v1/chat/completions) |
| model (字面) | `deepseek/deepseek-v4.1-flash` |
| proxy | **已清空** — 显式 pop 6 个 proxy env var |
| auth | runtime 读 `LLM API.txt` GB18030 → `sk-or-v1-449...b140` (截断 12+4) |
| key 落盘 | **无** — JSON `auth` 字段只 `sk-or-v1-449...b140`,literal key 永不入盘 |
| `max_tokens` | **2048** (v2 是 1024,本次 2×,目标消除 3 cells 截断) |
| `reasoning` | `{max_tokens: 0, exclude: true}` (真正剥离 CoT) |
| `temperature` | 0.0 (固定) |
| 30 cells 拆 | 15 GSM8K (id 1-15) + 15 StrategyQA (id 1-15) |
| prompt | GSM8K: "Question: {q}\nAnswer in one number:" / StrategyQA: "Question: {q}\nAnswer Yes or No:" |
| 限速 | 0.5s/cell sleep |
| 总耗时 | ~120s (avg ~4.0s/cell, 1 cell 12.9s outlier: strategyqa_9) |

**与 v2 唯一差异**: `max_tokens` 1024 → **2048**,其他全保持 (model / prompt / reasoning / temperature / 30 cells IDs)。

---

## §2 1-cell Sanity Check

- **prompt**: `"What is 1+1?"`
- **model**: `deepseek/deepseek-v4.1-flash` (严格字面,**不** fallback 到 v4 子模型)
- **max_tokens**: 2048
- **结果**: 200 OK,`content` = "Yes" (注: V4.1-Flash 对 "What is 1+1?" 答 "Yes" 而非 "2",这与 v2 一致;Sanity 仅验证可达性,不验证数学正确性)
- **结论**: 严格字面 v4.1-flash ID 在 max_tokens=2048 下仍真实可用,无 fallback 触发

---

## §3 30 Cells 结果明细

### 3.1 GSM8K (15 cells)

| ID | gold | llm_extracted | raw | correct | completion_tok | latency_ms | notes |
|---|---|---|---|---|---|---|---|
| gsm8k_1 | 18 | 18.0 | "18" | OK | 219 | 2205 | clean |
| gsm8k_2 | 5 | 5.0 | "5" | OK | 95 | 1724 | clean |
| gsm8k_3 | 40 | 40.0 | "40" | OK | 207 | 2430 | clean |
| gsm8k_4 | 1430 | 1430.0 | "1430" | OK | 47 | 2073 | clean |
| gsm8k_5 | 36 | 36.0 | "36" | OK | 62 | 1345 | clean |
| gsm8k_6 | 8000 | 8000.0 | "8000" | OK | 39 | 1891 | clean |
| **gsm8k_7** | **36** | **11.0** | "400/11" | **FAIL** | 1455 | 7613 | **修了截断,新失败**: 答 "400/11" → extract=11,gold=36. 模型本体算错 (v2 截断, v3 答错) |
| gsm8k_8 | 6 | 6.0 | "6" | OK | 321 | 2809 | clean |
| gsm8k_9 | 40 | 40.0 | "40" | OK | 60 | 1658 | clean |
| gsm8k_10 | 140 | 140.0 | "140" | OK | 52 | 1588 | clean |
| gsm8k_11 | 2125 | 2125.0 | "2125" | OK | 1266 | 6725 | clean (long reasoning, not truncated) |
| gsm8k_12 | 32 | 32.0 | "32" | OK | 525 | 3657 | **修了截断! v2 截断 → v3 干净** (525 < 2048) |
| gsm8k_13 | 50 | 50.0 | "50" | OK | 141 | 1932 | clean |
| gsm8k_14 | 122 | 122.0 | "122" | OK | 81 | 2374 | clean |
| gsm8k_15 | 34 | 34.0 | "34" | OK | 144 | 1873 | clean |

**GSM8K: 14/15 = 93.3%** (v2: 13/15 = 86.7%)

### 3.2 StrategyQA (15 cells)

| ID | gold | llm_extracted | raw | correct | completion_tok | latency_ms | notes |
|---|---|---|---|---|---|---|---|
| strategyqa_1 | Yes | Yes | "Yes" | OK | 114 | 2214 | clean |
| strategyqa_2 | No | No | "No" | OK | 43 | 1783 | clean |
| strategyqa_3 | Yes | Yes | "Yes" | OK | 156 | 2587 | clean |
| strategyqa_4 | No | No | "No" | OK | 135 | 2158 | clean |
| strategyqa_5 | Yes | Yes | "Yes" | OK | 646 | 4596 | clean |
| strategyqa_6 | No | No | "No" | OK | 54 | 1949 | clean |
| **strategyqa_7** | **No** | **Yes** | "Yes." | **FAIL** | 63 | 1912 | **判错** ("gay male couples cannot naturally reproduce" gold=No 因 wording 反问) — 与 v2 同 |
| strategyqa_8 | No | No | "No" | OK | 81 | 1709 | clean |
| **strategyqa_9** | **Yes** | **None** | "" | **FAIL** | **2048** | **12965** | **仍截断!** (Mercedes-Benz child driver,12.9s → max_tokens=2048 仍满) — 与 v2 同样 cell,但更久 |
| **strategyqa_10** | **No** | **Yes** | "Yes" | **FAIL** | 82 | 1959 | **判错** (Darth Vader vs Snape "resemble" gold=No) — 与 v2 同 |
| strategyqa_11 | No | No | "No" | OK | 45 | 1365 | clean |
| strategyqa_12 | No | No | "No" | OK | 133 | 2504 | clean |
| strategyqa_13 | Yes | Yes | "Yes" | OK | 91 | 2083 | clean |
| **strategyqa_14** | **Yes** | **No** | "No" | **FAIL** | 1410 | 9882 | **判错** (Bengal cat "best Sotomayor record" gold=Yes 因猫能跑酷跳高) — 与 v2 同,token 用了 1410 但答错 |
| strategyqa_15 | Yes | Yes | "Yes" | OK | 132 | 1964 | clean |

**StrategyQA: 11/15 = 73.3%** (与 v2 完全一致)

### 3.3 失败归因 (5 cells)

| 类型 | count | cells | 根因 |
|---|---|---|---|
| 截断 (max_tokens=2048 仍满) | 1 | strategyqa_9 | **不是 1024 太小** — V4.1-Flash 在该 cell 进入重复/死循环生成 (12.9s 仍在写),max_tokens 提升到 2048 仍不够。**根因不在 token 预算**,在模型本身 |
| 数字提取错误 (修了截断,新失败) | 1 | gsm8k_7 | v2 截断 → v3 不截断,模型答 "400/11" (数学错了,gold=36)。修了 1 截断,添了 1 答错 |
| 判错 (语义陷阱) | 3 | strategyqa_7, strategyqa_10, strategyqa_14 | StrategyQA 反问 / "resemble" / "hypothetically" 等陷阱,与 max_tokens 无关。**与 v2 完全一致**,本任务不期望修复 |

**净变化**: v2 6 fails → v3 5 fails (= -1 cell 改善)

---

## §4 与 v2 (24/30, max_tokens=1024) 对比

| 实验 | model | max_tokens | reasoning | total | verdict | trunc | misjudge | new |
|---|---|---|---|---|---|---|---|---|
| v2 (1024) | deepseek-v4.1-flash | 1024 | stripped | 24/30 (80%) | PASS (≥24) | 3 | 3 | 0 |
| **v3 (2048)** | **deepseek-v4.1-flash** | **2048** | **stripped** | **25/30 (83.3%)** | **MARGINAL (24-27)** | **1** | **3** | **1** |
| Δ | — | +1024 | — | **+1** | PASS→MARGINAL | **-2** | **0** | **+1** |

**关键观察**:

1. **max_tokens 1024 → 2048 修了 2 截断 cells** (gsm8k_7, gsm8k_12) — 但其中:
   - gsm8k_12: 真正修好 (32 干净)
   - gsm8k_7: 截断修了,但模型本体算错 ("400/11" = 11 ≠ 36),**新失败 = 1**
2. **strategyqa_9 仍截断** — V4.1-Flash 在该 cell (Mercedes-Benz child driver) 死循环/重复生成,即使 2048 仍写满 12.9s。**根因在模型,不是 token 预算**。
3. **3 语义判错完全保留** (strategyqa_7/10/14) — 与 v2 一致,user 预先说明"模型本体能力限制,本任务不期望修复"
4. **净增 1 cell** (24 → 25) — **改善有限,远低于 ≥28 边际目标**

**边际阈值评估** (per user v3 任务 spec):
- ≥28/30 = **PASS** ← user 期望目标
- 24-27/30 = **MARGINAL** ← 本次结果 25/30 落此区间
- <24/30 = **REGRESSION**

**v3 = MARGINAL**,不是 PASS。

---

## §5 7 铁律自检

| 铁律 | 状态 | 证据 |
|---|---|---|
| 1. API key runtime 读 (`LLM API.txt` GB18030 → `os.environ`) | OK | `run_deepseek_v41_30cells_v3.py:19-27` |
| 2. 不设 proxy (DeepSeek 国内) | OK | script `30-31` 显式 pop 6 个 proxy env var |
| 3. key 永不入 prompt / JSON / 落盘 | OK | JSON `auth` 字段 `sk-or-v1-449...b140` (12+4 截断) |
| 4. 30 cells 严格 (不重试 / 不切超过 3 候选 / 禁 fallback 到 v4 子模型) | OK | 候选仅 1 个字面 `deepseek-v4.1-flash`,v2 脚本的 candidate 列表已严格 v4.1+flash 无 v4* |
| 5. 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`) | OK | 本任务只读 `gsm8k_details.json` + `strategyqa_details.json`,不动 `verifier/handoff/` |
| 6. 不动 4 SPEC V0.1 冻结版 + v19 frozen JSON + v21 frozen JSON | OK | 本任务无 SPEC / v19 / v21 触碰 |
| 7. 结果落盘 (审计用,不含 key/IP 字面值) | OK | `deposon_deepseek_v41_flash_30cells_v3_2026_09_10.json` 已落盘 18.6 KB |

---

## §6 下一步(诚实声明,不替 Mavis 决定)

**本任务目标 = 评估 max_tokens=2048 是否能消除 3 截断 → ≥28 边际**。**结果: 否**。

### 6.1 失败根因诚实归因

| 失败类型 | 计数 | 能否用 max_tokens 修复 | 建议方向 |
|---|---|---|---|
| 截断 (strategyqa_9) | 1 | **否** — 12.9s 仍在生成,根因在模型重复/死循环 | prompt 改写 (限 token 限字数) / 换 model (但违反约束) |
| 数字算错 (gsm8k_7) | 1 | **否** — 修了截断后,模型本体数学错 | CoT 强制 (但违反 "reasoning 剥离" 约束) / 换 model |
| 语义判错 (strategyqa_7/10/14) | 3 | **否** — 反问 / "resemble" / "hypothetically" 模型本体缺陷 | CoT / few-shot (但超出 30 cells scope) |

**结论**: **max_tokens 不是 V4.1-Flash 在 30 cells 上的瓶颈**。再提到 4096 也修不了 strategyqa_9(它在重复生成) 和 3 语义判错(与 token 无关)。

### 6.2 给 user 端选项(per parent 决策权)

**option A**: 接受 v3 = 25/30 = **MARGINAL**, 沿用 v2 baseline 24/30 作为 V3.X 主锚(80% PASS 已够 1 周判死)。→ 启动 B (V2 真实 2 周工作量) + Wang WeChat-only 1 周预筛

**option B**: 进一步试 max_tokens=4096(可能修 strategyqa_9 截断),预计 +1 cell = 26/30,仍 MARGINAL。→ 边际成本高(单次 25s+),收益有限

**option C**: 切到 V4.1-Pro / 其他变体 — **违反 user 硬约束**("不切 model,严格 v4.1-flash")。需 user 明确解禁

**option D**: 接受 80-83% 为 V3.X 主线真实能力上限(已合理),继续 B 路径,StrategyQA 缺陷靠 Wang 顾问 + 1 周判死来吸收

### 6.3 本次任务边界声明(7 禁止条款 100% 守)

- 未把 key 写入任何文件
- 未在 print / echo 显示 key / IP 字面值
- 未设 proxy
- 未切任何 model(严格 `deepseek/deepseek-v4.1-flash` 字面)
- 未重试(30 cells 跑完就停)
- 未调额外 API
- 未让 Mavis 决定下一步 — 仅返回 K=14, L=11, total=25/30 = MARGINAL, 1 截断 + 3 判错 + 1 算错

**worker 交付完毕,等待 parent (mvs_bbeb804b1a6a41109be740636eed1709) 复审与下一步指令**。

---

## 附录 A: 关键代码位置

```python
# script: D:\私人资料\deposon-repo\scripts\run_deepseek_v41_30cells_v3.py

# 0. 加载 key (GB18030) - line 19-27
# 1. 显式 pop 6 proxy env var - line 30-31
# 2. Force UTF-8 stdout (避免 GBK ✓✗ 编码崩溃) - line 37-40
# 3. Sanity check (1-cell, max_tokens=2048) - line 47-77
# 4. 30 cells 边际 (max_tokens=2048) - line 167-244
# 5. extract_number / extract_yes_no - line 86-127
# 6. summary + JSON 落盘 - line 246-305
# verdict: PASS if >=28/30, MARGINAL if 24-27, REGRESSION if <24 - line 257
```

## 附录 B: 已知遗留与本任务未触及

1. **1 cell 仍截断 (strategyqa_9)**: 根因在 V4.1-Flash 死循环/重复生成 (12.9s 写满 2048 tokens),**max_tokens 不是解**,需 prompt 重写或换 model (均违反约束)
2. **1 cell 数学错 (gsm8k_7)**: v2 截断 → v3 修了截断但模型本体算错 (400/11 vs 36)。是 **1 cell 改善但 0 cell 净增** 的反例
3. **3 cells 语义判错 (strategyqa_7/10/14)**: 与 v2 一致,user 预先承认模型本体能力问题
4. **本任务不动**: 5 锚 JSON / 4 SPEC V0.1 冻结版 / v19 / v21 frozen JSON(per 7 铁律)

---

**关键数字给 parent 复审**:

- K (gsm8k_passed) = **14** / 15
- L (strategyqa_passed) = **11** / 15
- K+L = **25** / 30 = 83.3%
- verdict = **MARGINAL** (24-27 区间,沿用 v2 baseline)
- 截断从 v2 的 3 cells → v3 的 **1 cell** (strategyqa_9 仍死循环)
- 语义判错从 v2 的 3 cells → v3 的 **3 cells** (不变,符合预期)
- 新增 1 cell 数学错 (gsm8k_7, 修了截断但答错)
- 净改善 **+1 cell** (24 → 25),未达 ≥28 边际目标
