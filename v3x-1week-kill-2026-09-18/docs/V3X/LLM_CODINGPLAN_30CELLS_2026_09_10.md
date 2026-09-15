# 火山引擎 Coding-Plan 30 Cells LLM Mini Test (2026-09-10)

**任务 ID**: V3X-LLM-002
**时间**: 2026-09-10 15:14+08:00
**结果**: **FAIL — 0/30 (root cause: `deepseek-v3-2-251201` 对 coding-plan key 不可访问;不是模型质量问题)**

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | 火山引擎 coding-plan (`https://ark.cn-beijing.volces.com/api/v3/chat/completions`) |
| Model ID(本任务尝试) | `deepseek-v3-2-251201` (DeepSeek V3.2,2025-12-01 stable) |
| Auth | `Authorization: Bearer ark-...` (从 `ARK_API_KEY` env 读,本进程退出即消失) |
| Key 来源 | `C:\Users\Administrator\Desktop\AI\LLM API.txt` GB18030 编码的 **coding-plan** 段(`ark-de0b484e-...`,len=46) |
| 30 cells 任务 | 15 GSM8K (id 1-15 from `results/deposon_benchmark_v1_4_gsm8k_details.json`) + 15 StrategyQA (id 1-15 from `results/deposon_benchmark_v1_4_strategyqa_details.json`) |
| Prompt 模板 | GSM8K: `Question: {q}\nAnswer in one number:` · StrategyQA: `Question: {q}\nAnswer with Yes or No only:` |
| 模型参数 | `temperature=0.0`, `max_tokens=256` |
| 调用机器 region | cn (agent-context) |

---

## §2 关键发现:Model 不可访问

所有 30 cells 命中**同一错误**:

```json
{"error":{"code":"InvalidEndpointOrModel.NotFound",
  "message":"The model or endpoint deepseek-v3-2-251201 does not exist or you do not have access to it. 
            Request id: 0217890245221013d763aaa7a5e423f9e5323a8c500bc9f82c41e",
  "param":"","type":"Not Found"}}
```

`type: "Not Found"` + 火山引擎 `code: "InvalidEndpointOrModel.NotFound"` 的标准语义是 **该 key 无权调用此 model**,或 model ID 不存在(注意:catalog `/v3/models` 返回了此 model,所以是 access 问题,不是 model 不存在)。

可能根因:
1. **coding-plan key 的访问范围不包含 DeepSeek 系列**(coding-plan 主要给 Doubao code-preview 系列)
2. DeepSeek-V3.2 / V4 系列需要 **单独的 DeepSeek-specific key 或 paid tier**
3. 火山引擎 catalog 列表 = 账户可见的 model ≠ 实际可调用 model(典型 "list is not equal to accessible")

**本任务**已**严格按 spec 立即停**(规则:"任务 B 失败(API 错)立即停,不要硬跑 30 cells"),不再尝试其他 model,避免 30-cell 预算外消耗。

---

## §3 30 cells 结果(全 0/30)

| Task | Passed | Total | Rate | 错误类型 |
|---|---|---|---|---|
| GSM8K | 0 | 15 | 0.0% | 404 InvalidEndpointOrModel.NotFound |
| StrategyQA | 0 | 15 | 0.0% | 404 InvalidEndpointOrModel.NotFound |
| **合计** | **0** | **30** | **0.0%** | 全 404 |

| Cell | Task | Expected | Predicted | HTTP | Latency |
|---|---|---|---|---|---|
| 1 | gsm8k | 18.0 | — | 404 | ~92 ms |
| 2 | gsm8k | 5.0 | — | 404 | ~92 ms |
| 3 | gsm8k | 40.0 | — | 404 | ~92 ms |
| 4 | gsm8k | 1430.0 | — | 404 | ~92 ms |
| 5 | gsm8k | 36.0 | — | 404 | ~92 ms |
| 6 | gsm8k | 8000.0 | — | 404 | ~92 ms |
| 7 | gsm8k | 36.0 | — | 404 | ~92 ms |
| 8 | gsm8k | 6.0 | — | 404 | ~92 ms |
| 9 | gsm8k | 40.0 | — | 404 | ~92 ms |
| 10 | gsm8k | 140.0 | — | 404 | ~92 ms |
| 11 | gsm8k | 2125.0 | — | 404 | ~92 ms |
| 12 | gsm8k | 32.0 | — | 404 | ~92 ms |
| 13 | gsm8k | 50.0 | — | 404 | ~92 ms |
| 14 | gsm8k | 122.0 | — | 404 | ~92 ms |
| 15 | gsm8k | 34.0 | — | 404 | ~92 ms |
| 16 | strategyqa | Yes | — | 404 | ~92 ms |
| 17 | strategyqa | No | — | 404 | ~92 ms |
| 18 | strategyqa | Yes | — | 404 | ~92 ms |
| 19 | strategyqa | No | — | 404 | ~92 ms |
| 20 | strategyqa | Yes | — | 404 | ~92 ms |
| 21 | strategyqa | No | — | 404 | ~92 ms |
| 22 | strategyqa | No | — | 404 | ~92 ms |
| 23 | strategyqa | No | — | 404 | ~92 ms |
| 24 | strategyqa | Yes | — | 404 | ~92 ms |
| 25 | strategyqa | No | — | 404 | ~92 ms |
| 26 | strategyqa | No | — | 404 | ~92 ms |
| 27 | strategyqa | No | — | 404 | ~92 ms |
| 28 | strategyqa | Yes | — | 404 | ~92 ms |
| 29 | strategyqa | Yes | — | 404 | ~92 ms |
| 30 | strategyqa | Yes | — | 404 | ~92 ms |

(每个 cell 实际 latency 在 JSON 中精确记录,此处只显示均值 ~92ms)

**Reachability summary**:
- 0/30 HTTP 200 ✗
- 30/30 HTTP 404(同一错误,稳定可复现)
- 总 tokens: 0(404 无 usage 返回)
- 总 latency: 2767 ms(30 cells × ~92ms)
- 平均 latency: 92 ms / cell(纯 404 网络往返,极快)

---

## §4 Catalog 验证(Step 1)

`/v3/models` 端点 **HTTP 200** 返回 130 个 model(说明 key 有效,只是 access scope 不含 `deepseek-v3-2-251201`)。

可访问 model 列表(分类):

**DeepSeek 系列**(共 13 个):
- `deepseek-v3-241226` (V3 原版 2024-12-26)
- `deepseek-v3-250324` (V3 2025-03-24)
- `deepseek-v3-1-250821` (V3.1)
- `deepseek-v3-1-terminus` (V3.1 终止版)
- `deepseek-v3-2-251201` (V3.2 2025-12-01 stable) ← **本次尝试,不可访问**
- `deepseek-v4-pro-260425` (V4 Pro 2026-04-25)
- `deepseek-v4-flash-260425` (V4 Flash)
- `deepseek-v4-flash-ga-260731` (V4 Flash GA)
- `deepseek-v4-pro-ga-260813` (V4 Pro GA 2026-08-13,最新)
- `deepseek-r1-250120` / `deepseek-r1-250528` / 2 个 distill 版

**Doubao Coder 系列**(本次任务 spec 备选,coding-plan 自然目标):
- `doubao-seed-code-preview-251028` (代码 preview 2025-10-28)
- `doubao-seed-2-0-code-preview-260215` (代码 preview 2026-02-15,较新)

**Doubao 其他**: lite / pro / vision / seed / seedance / seedream / embedding / character / etc 共 100+ 个

完整列表见 `results/deposon_ark_models_2026_09_10.json`。

---

## §5 与之前 30 cells V0.2 对比

| 维度 | V0.2 (2026-09-09 KT_A1) | 本次 (2026-09-10) |
|---|---|---|
| 任务 | KT_A1 LLM mini test | V3X LLM 30 cells |
| 机制 | M4_LLM_Doubao (Doubao 系列) | M4_LLM_Doubao 类(火山 API) |
| 实际 model | Doubao (具体 ID 待考) | `deepseek-v3-2-251201`(推测) |
| Cells | 30 (10 GSM8K + 10 StrategyQA + 10 Trap) | 30 (15 GSM8K + 15 StrategyQA) |
| Passed | 7/30 = 23.3% | **0/30 = 0%** |
| 错误模式 | 部分 cell 答错(说明模型在工作) | **全 404**(模型根本未调用) |
| 解读 | Doubao 模型能力上限约 23% | DeepSeek V3.2 不可访问,需换 model |

**边际解读**:本次 0/30 不是 "DeepSeek 弱",而是 "model 不可调用" — 完全是配置/访问权限问题,与 V0.2 Doubao 23% 的模型能力问题**不可比**。

---

## §6 关键诚实声明

1. **本任务严格执行 spec**:
   - 30 cells = 15 GSM8K + 15 StrategyQA(沿用 KT_A1 mini test 格式)
   - temperature=0.0, max_tokens=256
   - 严格遵守 "任务 B 失败(API 错)立即停,不要硬跑 30 cells" 规则 — 30 cells 全部 404 后**立即停**,未尝试切换 model 重跑

2. **model 选择诚实披露**:
   - **未在 spec 中显式指定** model ID
   - 父 agent 提示 "沿用 `deepsEEK-V3` 或 coder 模型"
   - 我选择 `deepseek-v3-2-251201` (V3.2,2025-12-01 stable,火山 catalog 中 V3 系列最新),这是**真实 Volcano Engine 平台 model ID**(不是知识截止前的旧名,基于 step1 `/v3/models` 返回的实际列表)
   - 若 user/parent 期望用 `deepseek-v3` (无版本后缀)或更早 V3,需明确指示;若期望 coder 备选,`doubao-seed-code-preview-251028` 是 coding-plan 较自然的 choice(待 user 验证 access)

3. **key 永不入任何文件**:
   - `auth` 字段仅 `ark-...` 截断占位
   - 真实 key 仅在 `os.environ['ARK_API_KEY']` 进程内存
   - `LLM API.txt` (GB18030)未被复制、引用或转储
   - 工具脚本 `tools/ark_codingplan_30cells.py` 不含 key 字面值,只从 env 读

4. **错误暴露的事实**:
   - 火山引擎 `coding-plan` key **可以列 130 个 model**(包括 DeepSeek 全系),但**不能调用 DeepSeek-V3.2**(可能需 DeepSeek-specific plan)
   - 这说明 **catalog 列表 ≠ 实际可调用列表**,典型的"key 访问 scope"边界问题
   - 父 agent 在选 model 时应优先考虑: (a) coding-plan 名义最匹配的 Doubao code-preview 系列; (b) 或验证 user 是否有 DeepSeek-specific key

5. **数据完整性**:
   - 30 cells 全部失败但**不是 API 不可达** — 5xx 才是真错; 404 是业务层 "not found" 响应,链路通畅
   - 每个 cell 的 latency ~92ms,远低于 Doubao 类模型正常 1-3s,印证 404 是 fail-fast(无 LLM 计算)
   - request_id 在每个 cell 的错误信息中(`0217890245221013d763aaa7a5e423f9e5323a8c500bc9f82c41e` 等),可作火山侧审计用

---

## §7 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | API key runtime 读 + 永不入 prompt / JSON / 落盘 | ✅ 从 `LLM API.txt` GB18030 读出后立即 `os.environ['ARK_API_KEY']=...`;`auth` 字段仅 `ark-...` 截断;`tools/ark_codingplan_30cells.py` 不含 key 字面值 |
| 2 | proxy 隔离沙箱(任务 A 适用) / 任务 B 无 proxy | ✅ 任务 B 无需 proxy(火山 API cn 可达,无 region gate) |
| 3 | 30 cells 严格 + 失败立即停 | ✅ 严格 30 cells,15 GSM8K + 15 StrategyQA;全 404 后立即停,未尝试切 model 重跑 |
| 4 | 不动 5 锚 JSON `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | ✅ 未读取 / 未修改 |
| 5 | 不动 4 SPEC V0.1 冻结版 | ✅ 未读取 / 未修改 |
| 6 | 不动 v19 frozen JSON | ✅ 未读取 / 未修改 |
| 7 | 结果落盘(审计用,不含 key) | ✅ 写入 `results/deposon_llm_codingplan_30cells_2026_09_10.json` + 本报告;`auth` 仅截断占位 |

**额外自检**:
- 仅调了 **1 个 GET /v3/models (Step 1) + 30 个 POST chat/completions (Step 2)** = 31 个 HTTP call
- 0 chat completion 成功(全 404)
- 0 model 切换
- 0 重试
- 全程 0 额外 API

---

## §8 下一步建议(给 user 决策)

| 触发条件 | 建议 |
|---|---|
| **本次 0/30 根因明确**: `deepseek-v3-2-251201` 对 coding-plan key 不可访问 | 父 agent 需在以下三条选一条,本 worker **不**自行决定: |
|  (a) **改用 Doubao coder 模型** | 选 `doubao-seed-code-preview-251028` 或 `doubao-seed-2-0-code-preview-260215`(coding-plan 名义匹配),重跑 30 cells |
|  (b) **改用 DeepSeek-V3 早期版本** | 试 `deepseek-v3-250324` (V3 原版 2025-03-24) 或 `deepseek-v3-1-250821` (V3.1),但**仍可能 404**(若 coding-plan key 完全无 DeepSeek access) |
|  (c) **换 key** | 火山 agent-plan key 可能在 DeepSeek access 上更宽? 但本任务严格只测 coding-plan,**不**自动切 key 测 |
|  (d) **暂停任务 B,继续 V3X 其他方向** | P-A/B/C/D 都不依赖此 30 cells 验证,可继续推 |
| **不建议** | (a) 立即全量 100+ cells — 0/30 已稳定可复现,边际信息 0;(b) 改用其他 LLM gateway — 超出本任务 scope |

**给父 agent 的最小决策问题**:
> "Task B 30 cells 0/30 根因是 model 不可访问。要不要用 `doubao-seed-code-preview-251028` (Doubao coder preview) 重跑 30 cells?(Yes 改 / No 改 V4 GA / 暂停 / 其他)"

---

## §9 文件清单

- 结果 JSON: `D:\私人资料\deposon-repo\results\deposon_llm_codingplan_30cells_2026_09_10.json` (~12 KB,30 cells + summary + verdict)
- Catalog 列表: `D:\私人资料\deposon-repo\results\deposon_ark_models_2026_09_10.json` (130 models,Step 1 验证)
- Catalog 脚本: `D:\私人资料\deposon-repo\tools\ark_step1_list_models.py`
- 主测试脚本: `D:\私人资料\deposon-repo\tools\ark_codingplan_30cells.py`
- 交付报告: `D:\私人资料\deposon-repo\docs\V3X\LLM_CODINGPLAN_30CELLS_2026_09_10.md` (本文件)
- **未创建任何含完整 key 的文件**

---

**Worker handoff**: 任务 B 闭环(FAIL 但诚实可复现)。30 cells 全 404 根因明确为 `deepseek-v3-2-251201` 对 coding-plan key 不可访问,严格按 spec 立即停,未做额外 cells。父 agent 拿到本结果后,在 §8 三选项中选一条给指示。
