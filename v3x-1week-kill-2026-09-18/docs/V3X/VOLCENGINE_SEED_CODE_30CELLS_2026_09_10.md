# 火山方舟 doubao-seed-code-preview-251028 30-Cell 边际验证报告

- **生成时间**: 2026-09-10 18:09 (Asia/Shanghai)
- **作者**: worker (mvs_2504905613ee4090b4615e10e3f98f3c)
- **parent**: mvs_bbeb804b1a6a41109be740636eed1709
- **任务来源**: user 2026-09-10 17:38 硬性指令(主线 = 火山引擎内 model,既不 GPT-6 也不 V4.1) + 17:41 硬性指令(只走 coding-plan)
- **数据落盘**: `D:\私人资料\deposon-repo\results\deposon_volcengine_seed_code_30cells_2026_09_10.json`
- **脚本**: `D:\私人资料\deposon-repo\scripts\run_volcengine_seed_code_30cells.py`
- **运行日志**: `D:\私人资料\deposon-repo\results\deposon_volcengine_seed_code_30cells_2026_09_10.log`

---

## §1 测试环境

| 字段 | 值 |
|---|---|
| gateway | **火山方舟 Coding Plan** (`https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions`) |
| model (字面,严格) | `doubao-seed-code-preview-251028` (Seed-Code preview, 自带 reasoning chain) |
| proxy | **已清空** — 显式 pop 6 个 proxy env var |
| auth | runtime 读 `LLM API.txt` GB18030 → `ark-[REDACTED]` (前 12 位 `ark-de0b484e`) |
| key 落盘 | **无** — JSON `auth` 字段只 `ark-de0b484e...` 截断,literal key 永不入盘 |
| `max_tokens` | **2048** (给 Seed-Code reasoning 空间) |
| `temperature` | 0.0 (固定) |
| `timeout_s` | 120s/cell (read timeout) |
| 30 cells 拆 | 15 GSM8K (id 1-15) + 15 StrategyQA (id 1-15) |
| prompt | GSM8K: `"Question: {q}\nAnswer in one number:"` / StrategyQA: `"Question: {q}\nAnswer Yes or No:"` |
| 限速 | 0.5s/cell sleep |
| 总耗时 | **~18.5 min** (17:51:23 start → 18:09:50 JSON write; 含 3 cells 走完 120s timeout) |

**唯一模型候选**: `doubao-seed-code-preview-251028` (沿用 5/5 PASS 的 chat sanity 选定 model)。**不切 model, 不切 endpoint, 不重试**(per user 17:38+17:41 硬性指令)。

---

## §2 1-cell Sanity Check

- **prompt**: `"What is 1+1?"`
- **model**: `doubao-seed-code-preview-251028` (严格字面,**不** fallback 到其他 Doubao/Seed 子模型)
- **max_tokens**: 2048
- **HTTP status**: 200 OK
- **response preview**: `"In standard basic arithmetic, the result of 1 + 1 is **2** — this is the most co..."`
- **结论**: **PASS** — 可达 + 答案含 "2" (与 5/5 chat smoke 同一 verdict)

---

## §3 30 Cells 结果明细

### 3.1 GSM8K (15 cells)

| ID | gold | llm_extracted | raw | correct | completion_tok | latency_ms | notes |
|---|---|---|---|---|---|---|---|
| gsm8k_1 | 18 | 18.0 | "18" | OK | 743 | 13,960 | clean |
| gsm8k_2 | 5 | 5.0 | "5" | OK | 154 | 4,616 | clean |
| **gsm8k_3** | 40 | 40.0 | "40" | OK | 2,180 | 37,932 | **completion_tokens > 2048 (API 报 2180)** — 答案仍可提取 |
| gsm8k_4 | 1430 | 1430.0 | "1430" | OK | 71 | 4,517 | clean |
| gsm8k_5 | 36 | 36.0 | "36" | OK | 110 | 7,852 | clean |
| gsm8k_6 | 8000 | 8000.0 | "8000" | OK | 65 | 6,875 | clean |
| **gsm8k_7** | 36 | None | None | **FAIL** | — | 120,000+ | **timeout (120s read)** — Status 0 |
| gsm8k_8 | 6 | 6.0 | "6" | OK | 1,012 | 12,664 | clean (Seed-Code 走长 reasoning) |
| gsm8k_9 | 40 | 40.0 | "40" | OK | 727 | 19,260 | clean |
| gsm8k_10 | 140 | 140.0 | "140" | OK | 1,344 | 27,734 | clean |
| **gsm8k_11** | 2125 | 2125.0 | "2125" | OK | **6,218** | **109,940** | **completion_tokens 6.2K, latency 110s** — 答案仍可提取(Seed-Code reasoning 大爆发) |
| **gsm8k_12** | 32 | 32.0 | "32" | OK | **4,633** | **75,248** | **completion_tokens 4.6K, latency 75s** — 答案仍可提取 |
| gsm8k_13 | 50 | 50.0 | "50" | OK | 277 | 11,620 | clean |
| gsm8k_14 | 122 | 122.0 | "122" | OK | 327 | 8,883 | clean |
| **gsm8k_15** | 34 | None | None | **FAIL** | — | 120,000+ | **timeout (120s read)** — Status 0 |

**GSM8K: 13/15 = 86.7%** (2 timeout, 0 数字算错, 0 语义判错)

### 3.2 StrategyQA (15 cells)

| ID | gold | llm_extracted | raw | correct | completion_tok | latency_ms | notes |
|---|---|---|---|---|---|---|---|
| strategyqa_1 | Yes | Yes | "Yes" | OK | 277 | 7,131 | clean |
| strategyqa_2 | No | No | "No" | OK | 168 | 6,023 | clean |
| strategyqa_3 | Yes | Yes | "Yes" | OK | 2,022 | 46,482 | clean (长 reasoning) |
| strategyqa_4 | No | No | "No" | OK | 511 | 11,209 | clean |
| **strategyqa_5** | Yes | Yes | "Yes" | OK | 2,543 | 43,888 | **completion_tokens > 2048** |
| strategyqa_6 | No | No | "No" | OK | 156 | 5,736 | clean |
| **strategyqa_7** | No | Yes | "Yes" | **FAIL** | 3,551 | 78,544 | **truncated + 判错** (Bengal cat Sotomayor) |
| strategyqa_8 | No | No | "No" | OK | 753 | 14,847 | clean |
| **strategyqa_9** | Yes | No | "No" | **FAIL** | 3,843 | 70,800 | **truncated + 判错** (Mercedes child driver) |
| **strategyqa_10** | No | Yes | "Yes" | **FAIL** | 877 | 33,777 | **semantic_misjudge** (Darth Vader vs Snape) |
| strategyqa_11 | No | No | "No" | OK | 110 | 4,731 | clean |
| strategyqa_12 | No | No | "No" | OK | 1,372 | 35,147 | clean |
| strategyqa_13 | Yes | Yes | "Yes" | OK | 745 | 15,282 | clean |
| **strategyqa_14** | Yes | None | None | **FAIL** | — | 120,000+ | **timeout (120s read)** — Status 0 (Bengal cat Sotomayor) |
| strategyqa_15 | Yes | Yes | "Yes" | OK | 317 | 6,357 | clean |

**StrategyQA: 11/15 = 73.3%** (1 timeout + 2 truncation-fail + 1 semantic_misjudge)

### 3.3 失败归因 (6 cells)

| 类型 | count | cells | 根因 |
|---|---|---|---|
| **timeout (120s read)** | **3** | gsm8k_7, gsm8k_15, strategyqa_14 | Seed-Code 在某些 cell 上 reasoning 死循环/超长生成,120s read timeout 触发。**根因在模型本身 + max_tokens=2048 不约束 reasoning 长度** |
| **completion_tokens > 2048** | **3 (但答案仍对)** | gsm8k_3 (2,180), gsm8k_11 (6,218), gsm8k_12 (4,633) | API 报告的 completion_tokens 超过 max_tokens 限制,**说明 reasoning 不计入 max_tokens 限制**,或火山方舟 API 不严格 enforce max_tokens=2048 给 Seed-Code。**但 final answer 仍可提取 → 标 OK** |
| **truncation-fail (答案错)** | **2** | strategyqa_7 (Yes vs No), strategyqa_9 (No vs Yes) | 截断 + 答案错。Seed-Code 在这些 cell 上 reasoning 后给出反向答案 |
| **semantic_misjudge** | **1** | strategyqa_10 (Yes vs No) | Darth Vader vs Snape "resemble" 语义陷阱,与 max_tokens 无关。**与 v4.1-flash v3 同样 cell 一致** |

**净观察**:
- **3 timeout 是真问题** (1 GSM8K + 1 GSM8K + 1 StrategyQA),占 30 cells 的 10%
- **3 截断 (但答案对) 实际是 "假问题"** — Seed-Code reasoning 太长但 final answer 完整,标 OK
- **1 语义判错 + 2 截断-错 = 3 cells** 归因于模型本体能力(与 V4.1-Flash v3 baseline 25/30 表现同量级)
- **6 cells 真失败** = 3 timeout + 3 模型本体缺陷

---

## §4 与 4 个 baseline 对比

| 实验 | model | gateway | max_tokens | 30 cells | verdict | 失败归因 |
|---|---|---|---|---|---|---|
| v4.1_flash_v2 (max_tokens=1024) | deepseek/deepseek-v4.1-flash | OpenRouter | 1024 | 24/30 (80%) | PASS | 3 截断 + 3 语义判错 |
| v4.1_flash_v3 (max_tokens=2048) | deepseek/deepseek-v4.1-flash | OpenRouter | 2048 | 25/30 (83.3%) | MARGINAL | 1 截断 + 3 语义判错 + 1 算错 |
| gpt6_teamorouter | gpt-6 (via TeamoRouter) | TeamoRouter | default | 22/30 (73.3%) | GRAY | 8 cells 失败 |
| **doubao_seed_code (本次)** | **doubao-seed-code-preview-251028** | **火山方舟 coding-plan** | **2048** | **24/30 (80%)** | **PASS** | **3 timeout + 2 trunc-fail + 1 misjudge** |

**关键观察**:

1. **doubao-seed-code 24/30 = 80% PASS (>=24 阈值)** — **与 V4.1-Flash v2 baseline 持平**,比 V4.1-Flash v3 (25/30) 略低 1 cell
2. **失败结构差异**:
   - V4.1-Flash v3 主要失败在**模型本体能力**(截断 + 判错 + 算错)
   - doubao-seed-code 主要失败在**API 行为**(timeout + reasoning 超过 max_tokens 但答案仍对)
3. **Seed-Code 的 reasoning 行为特征**:
   - 多数 cell 走长 reasoning (completion_tokens 200-2000)
   - 3 cells 极度长 reasoning (6218/4633/3843 tokens) — 答案仍对,只是慢
   - 3 cells reasoning 死循环触发 120s timeout — 答案 None
4. **GSM8K vs StrategyQA 表现**: 13/15 (86.7%) vs 11/15 (73.3%) — **数学题比常识题稳**,与其他 3 个 baseline 趋势一致

---

## §5 7 铁律自检

| # | 铁律 | 状态 | 证据 |
|---|---|---|---|
| 1 | coding-plan key runtime 读 LLM API.txt GB18030 → `os.environ['ARK_CODING_PLAN_KEY']` | ✅ | `re.search(r'ark-de0b484e-[a-zA-Z0-9-]+', content)` 提取,无 key 字面值入 prompt/JSON |
| 2 | 不设 proxy (火山国内) | ✅ | script 显式 pop 6 proxy env var (HTTP_PROXY/HTTPS_PROXY/http_proxy/https_proxy/ALL_PROXY/all_proxy) |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan (user 17:38+17:41 硬性指令) | ✅ | 全程只走 `ark.cn-beijing.volces.com/api/coding/v3`,无其他 endpoint;model 严格 `doubao-seed-code-preview-251028` |
| 4 | key 永不入 prompt / JSON / 落盘 | ✅ | JSON `auth` 字段仅 `ark-de0b484e...` 截断;prompt 全部是 GSM8K / StrategyQA question |
| 5 | 30 cells 严格 (不重试 / 不切 model) | ✅ | model 全程 `doubao-seed-code-preview-251028` 字面,无切换候选;无 retry (3 timeout 直接 FAIL) |
| 6 | 不动 5 锚 JSON `KT_ABC1_anchors_sha256_12.json` (沿用 `03c6c01f3697`) | ✅ | `LastWriteTime 2026-09-09 13:19:32` (任务前),**未动** |
| 7 | 不动 4 SPEC V0.1 冻结版 + v19 frozen JSON + v21 frozen JSON | ✅ | 本任务无 SPEC / v19 / v21 触碰;`KT_A1_SPEC_V0.1.md` 等冻结版 LastWriteTime 未变 |

**额外自检**:
- ✅ endpoint 严格 `/api/coding/v3`(非错误 `/v3`)
- ✅ `doubao-seed-code-preview-251028` 字面 model ID(非 v1-5-pro/256k 等被火山 404 的)
- ✅ `os.environ['ARK_CODING_PLAN_KEY']` 设入内存,`os.environ` 未持久化
- ✅ `auth` 字段 JSON 截断 `ark-de0b484e...`,无 IP 字面值

---

## §6 下一步(诚实声明,不替 Mavis 决定)

**本次任务目标 = 验证 doubao-seed-code-preview-251028 在火山 coding-plan 上 30 cells 边际能力**。**结果: 24/30 = 80% = PASS (>=24 阈值)**。

### 6.1 24/30 PASS 含义

per user task spec:
- **PASS** if >=24/30 ← 本次结果
- GRAY if 18-23
- FAIL if <18

**结论**: 火山方舟 doubao-seed-code-preview-251028 **可用作 V3.X 1 周预筛推理后端**,能力水平与 V4.1-Flash v2 baseline 持平。

### 6.2 失败根因诚实归因(给 parent 决策)

| 失败类型 | 计数 | 是否可优化 | 优化方向 (需 user 解禁约束) |
|---|---|---|---|
| **timeout (120s read)** | **3** | **部分** — timeout 120s 提升到 240s 可能修 2-3 cells,但违反"30 cells 严格"约束 | 提 timeout → 240s (单次任务 ~40-60 min);或 **改 max_tokens=4096** 强制 reasoning 收敛 |
| **truncation-fail (答案错)** | **2** | **否** — reasoning 已超 2048 但 final answer 错,根因在模型本体判错 | 换 model (违反约束) / CoT prompt 改写 (超出 30 cells scope) |
| **semantic_misjudge** | **1** | **否** — Darth Vader/Snape 语义陷阱,与 V4.1-Flash v3 同 cell 一致 | CoT / few-shot (超出 scope) |
| **3 截断(但答案对)** | **3** | **否** — 假问题,完成推理但 max_tokens 报告异常 | 已 OK,无优化必要 |

**净观察**: 3 timeout 是真正瓶颈,提 timeout 到 240s 可能 → 26-27/30。**但单次任务耗时翻倍(~36 min),边际收益低**。

### 6.3 给 user 端选项(per parent 决策权)

**option A (推荐)**: **接受 24/30 = 80% PASS**,沿用 V4.1-Flash v2 baseline 作为 1 周判死门槛。火山 doubao-seed-code 作为 V3.X 推理后端候选**之一**(可与 V4.1-Flash v3 25/30 互为备选)。

**option B**: 提 timeout 到 240s + max_tokens=4096 重跑 30 cells,看是否到 26-27/30。**单次任务 ~36 min,边际 +2-3 cells,性价比较低**。

**option C**: 接受 80% 为 V3.X 真实能力上限,继续 B 路径(火山主线),StrategyQA 缺陷靠 Wang 顾问 + 1 周判死来吸收。

**option D**: 切到其他 Seed-Code 子模型 (e.g. `doubao-seed-code-preview-251028-2` 如有) — **违反 user 硬约束**("严格 doubao-seed-code-preview-251028"),需 user 明确解禁。

### 6.4 本次任务边界声明(7 禁止条款 100% 守)

- 未把 key 写入任何文件
- 未在 print / echo 显示 key / IP 字面值 (sanity preview 是 LLM response,不是 key)
- 未设 proxy
- 未切任何 model(严格 `doubao-seed-code-preview-251028` 字面,5 cells sanity + 30 cells 边际全用)
- 未重试(3 timeout 直接 FAIL,不重试)
- 未调额外 API(只 `https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions`)
- 未让 Mavis 决定下一步 — 仅返回 K=13, L=11, total=24/30 = PASS, 3 timeout + 2 trunc-fail + 1 misjudge

**worker 交付完毕,等待 parent (mvs_bbeb804b1a6a41109be740636eed1709) 复审与下一步指令**。

---

## 附录 A: 关键代码位置

```python
# script: D:\私人资料\deposon-repo\scripts\run_volcengine_seed_code_30cells.py

# 0. 加载 key (GB18030) - 第 19-25 行
# 1. 显式 pop 6 proxy env var - 第 28-30 行
# 2. Force UTF-8 stdout - 第 37-39 行
# 3. Sanity check (1-cell, max_tokens=2048) - 第 75-103 行
# 4. 30 cells 边际 (max_tokens=2048) - 第 165-280 行
# 5. extract_number / extract_yes_no - 第 121-159 行
# 6. summary + JSON 落盘 - 第 282-348 行
# verdict: PASS if >=24/30, GRAY if 18-23, FAIL if <18 (per user task spec) - 第 297-302 行
```

## 附录 B: 与 V4.1-Flash v3 (25/30) 详细对比

| 维度 | V4.1-Flash v3 (OpenRouter) | doubao-seed-code (火山) |
|---|---|---|
| 总耗时 | ~120s | **~1,100s (18.5 min)** |
| 限速 | 0.5s/cell | 0.5s/cell |
| avg latency/cell | ~4.0s | **~37s/cell** (含 3 timeout) |
| 最慢 cell | 12.9s (strategyqa_9) | **110s (gsm8k_11)** |
| reasoning 行为 | strip (max_tokens=0) | **内置,完成 200-6200 tokens** |
| 30 cells 准确率 | 25/30 (83.3%) | 24/30 (80%) |
| 失败类型 | 1 截断 + 3 判错 + 1 算错 | 3 timeout + 2 trunc-fail + 1 misjudge |
| 网络 | OpenRouter 海外 (proxy 清空) | **火山方舟国内直连** |
| 成本 | OpenRouter 计费 | **火山方舟 coding-plan** |

**结论**: doubao-seed-code 慢 ~9x,但准确率只低 1 cell。**在 1 周预筛场景下,慢可接受,准确率 80% 已达 PASS 阈值**。

## 附录 C: 已知遗留与本任务未触及

1. **3 cells 触发 120s read timeout** (gsm8k_7, gsm8k_15, strategyqa_14) — 根因在 Seed-Code 在这些 cell 上 reasoning 死循环,**max_tokens=2048 不约束 reasoning 长度**。需 user 决定是否解禁提 timeout 到 240s。
2. **3 cells 报 completion_tokens > 2048 但答案对** (gsm8k_3, 11, 12) — 火山方舟 API 行为,Seed-Code reasoning 不计入 max_tokens。**假问题,无影响**。
3. **2 cells 截断 + 答案错** (strategyqa_7, 9) — reasoning 截断导致 final answer 反向,**模型本体能力问题**。
4. **1 cell 语义判错** (strategyqa_10, Darth Vader vs Snape) — 与 V4.1-Flash v3 同 cell 同错,模型共性。
5. **本任务不动**: 5 锚 JSON / 4 SPEC V0.1 冻结版 / v19 / v21 frozen JSON(per 7 铁律)。

---

**关键数字给 parent 复审**:
- K (gsm8k_passed) = **13** / 15
- L (strategyqa_passed) = **11** / 15
- K+L = **24** / 30 = **80%** = **PASS** (>=24 阈值)
- timeout = **3 cells** (gsm8k_7, gsm8k_15, strategyqa_14)
- truncation-fail = **2 cells** (strategyqa_7, 9)
- semantic_misjudge = **1 cell** (strategyqa_10)
- 假问题 (truncation 但答案对) = **3 cells** (gsm8k_3, 11, 12)
- 总耗时 = **~18.5 min** (含 3 timeout × 120s)
- avg latency = **~37s/cell** (Seed-Code reasoning 慢)
- max_tokens = **2048**, **API 实际不严格 enforce**(completion_tokens 最高 6218)
- 5 锚 JSON LastWriteTime = 2026-09-09 13:19:32(任务前,未动)
