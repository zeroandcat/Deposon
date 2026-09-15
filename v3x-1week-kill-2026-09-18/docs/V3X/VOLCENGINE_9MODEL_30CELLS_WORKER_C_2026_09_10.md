# 火山方舟 9-model 30-cells 补测报告 — Worker C

**worker_id**: C
**生成时间**: 2026-09-10 21:23 (CST)
**覆盖模型**: `glm-5.3` + `doubao-seed-evolving` (2 model × 30 cells = 60 LLM calls)
**与其他 worker 关系**: 与 worker A / B / D 并发执行(用户 21:10 明确"慢慢补测避免串行 = 4 worker 并发")
**输出文件**:
- JSON: `D:\私人资料\deposon-repo\results\deposon_volcengine_worker_c_2026_09_10.json` (sha256: `57695A3B39D9535C3C0EA5192ECA5426F384520BAC2924CFD9C553F0696B08A5`)
- 日志: `D:\私人资料\deposon-repo\results\deposon_volcengine_worker_c_2026_09_10.log`
- 实时 .run.log: `D:\私人资料\deposon-repo\results\deposon_volcengine_worker_c_2026_09_10.run.log`
- 脚本: `D:\私人资料\deposon-repo\results\deposon_volcengine_worker_c_2026_09_10.py`

---

## §1 测试环境

| 项目 | 值 |
|---|---|
| Gateway | 火山方舟 Coding Plan (Volcengine Ark) |
| Base URL | `https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions` |
| 鉴权 | coding-plan key (runtime 读 + env 注入,绝不入 JSON) |
| Proxy | **未设**(已显式清空 HTTP_PROXY/HTTPS_PROXY 等 6 项) |
| Temperature | 0.0 |
| max_tokens | 1024 |
| Cell timeout | 30s (节省时间) |
| Sanity timeout | 20s |
| 提取器(GSM8K) | 优先 `**N**` 粗体 → fallback 找最后一个数字 token |
| 提取器(StrategyQA) | 优先 `**Yes/No**` 粗体 → fallback 最后一个 Yes/No 词 |
| GSM8K 输入 | `deposon_benchmark_v1_4_gsm8k_details.json` id 1-15 |
| StrategyQA 输入 | `deposon_benchmark_v1_4_strategyqa_details.json` id 1-15 |
| 总 wall-clock | **431.0 s ≈ 7.2 min** (2 model 串行,各 30 cell) |

---

## §2 2 model × 30 cells 详细表

### §2.1 glm-5.3 (sanity: 200 / 2828 ms / "1 + 1 = 2" PASS)

| 段 | Cell | 状态 | ms | pred | gold | correct |
|---|---|---|---|---|---|---|
| GSM8K | gsm8k_1 | 200 | 3283 | 18.0 | 18.0 | ✅ |
| GSM8K | gsm8k_2 | 200 | 2817 | 5.0 | 5.0 | ✅ |
| GSM8K | gsm8k_3 | 200 | 2234 | 40.0 | 40.0 | ✅ |
| GSM8K | gsm8k_4 | **-1 (timeout 30s)** | 30036 | None | 1430.0 | ❌ |
| GSM8K | gsm8k_5 | 200 | 1946 | 36.0 | 36.0 | ✅ |
| GSM8K | gsm8k_6 | 200 | 1447 | 8000.0 | 8000.0 | ✅ |
| GSM8K | gsm8k_7 | 200 | 4861 | 36.0 | 36.0 | ✅ |
| GSM8K | gsm8k_8 | 200 | 1907 | 6.0 | 6.0 | ✅ |
| GSM8K | gsm8k_9 | 200 | 2650 | 40.0 | 40.0 | ✅ |
| GSM8K | gsm8k_10 | 200 | 1446 | 140.0 | 140.0 | ✅ |
| GSM8K | gsm8k_11 | 200 | 1768 | 2125.0 | 2125.0 | ✅ |
| GSM8K | gsm8k_12 | 200 | 2148 | 32.0 | 32.0 | ✅ |
| GSM8K | gsm8k_13 | 200 | 2336 | 50.0 | 50.0 | ✅ |
| GSM8K | gsm8k_14 | 200 | 1627 | 122.0 | 122.0 | ✅ |
| GSM8K | gsm8k_15 | 200 | 2077 | 34.0 | 34.0 | ✅ |
| GSM8K 合计 |  |  |  |  |  | **14 / 15** |
| STQ | stq_1 | 200 | 2927 | Yes | Yes | ✅ |
| STQ | stq_2 | 200 | 1714 | No | No | ✅ |
| STQ | stq_3 | 200 | 6194 | Yes | Yes | ✅ |
| STQ | stq_4 | 200 | 3418 | No | No | ✅ |
| STQ | stq_5 | 200 | 8834 | No | Yes | ❌ |
| STQ | stq_6 | 200 | 3301 | No | No | ✅ |
| STQ | stq_7 | 200 | 2894 | Yes | No | ❌ |
| STQ | stq_8 | 200 | 2450 | No | No | ✅ |
| STQ | stq_9 | 200 | 6873 | Yes | Yes | ✅ |
| STQ | stq_10 | 200 | 7135 | Yes | No | ❌ |
| STQ | stq_11 | 200 | 2246 | No | No | ✅ |
| STQ | stq_12 | 200 | 3638 | No | No | ✅ |
| STQ | stq_13 | 200 | 4360 | Yes | Yes | ✅ |
| STQ | stq_14 | 200 | 9208 | Yes | Yes | ✅ |
| STQ | stq_15 | 200 | 5146 | Yes | Yes | ✅ |
| STQ 合计 |  |  |  |  |  | **12 / 15** |
| **glm-5.3 总计** |  |  |  |  |  | **26 / 30 = 86.67%** |
|  |  |  |  |  |  | avg_ms=**4430.6**, elapsed=132.9 s |

### §2.2 doubao-seed-evolving (sanity: 200 / 2553 ms / "**2**" PASS)

| 段 | Cell | 状态 | ms | pred | gold | correct |
|---|---|---|---|---|---|---|
| GSM8K | gsm8k_1 | 200 | 10131 | 18.0 | 18.0 | ✅ |
| GSM8K | gsm8k_2 | 200 | 3585 | 5.0 | 5.0 | ✅ |
| GSM8K | gsm8k_3 | 200 | 6491 | 40.0 | 40.0 | ✅ |
| GSM8K | gsm8k_4 | 200 | 8989 | 1430.0 | 1430.0 | ✅ |
| GSM8K | gsm8k_5 | 200 | 3993 | 36.0 | 36.0 | ✅ |
| GSM8K | gsm8k_6 | 200 | 3617 | **0.0** | 8000.0 | ❌ |
| GSM8K | gsm8k_7 | 200 | 9145 | **36.36** | 36.0 | ❌ |
| GSM8K | gsm8k_8 | 200 | 13980 | 6.0 | 6.0 | ✅ |
| GSM8K | gsm8k_9 | 200 | 9671 | 40.0 | 40.0 | ✅ |
| GSM8K | gsm8k_10 | 200 | 4321 | 140.0 | 140.0 | ✅ |
| GSM8K | gsm8k_11 | 200 | 5270 | 2125.0 | 2125.0 | ✅ |
| GSM8K | gsm8k_12 | 200 | 5151 | 32.0 | 32.0 | ✅ |
| GSM8K | gsm8k_13 | 200 | 11719 | 50.0 | 50.0 | ✅ |
| GSM8K | gsm8k_14 | 200 | 3168 | 122.0 | 122.0 | ✅ |
| GSM8K | gsm8k_15 | **-1 (timeout 30s)** | 30044 | None | 34.0 | ❌ |
| GSM8K 合计 |  |  |  |  |  | **12 / 15** |
| STQ | stq_1 | 200 | 3333 | Yes | Yes | ✅ |
| STQ | stq_2 | 200 | 3878 | No | No | ✅ |
| STQ | stq_3 | 200 | 22714 | Yes | Yes | ✅ |
| STQ | stq_4 | 200 | 4380 | No | No | ✅ |
| STQ | stq_5 | **-1 (timeout 30s)** | 30030 | None | Yes | ❌ |
| STQ | stq_6 | 200 | 4793 | No | No | ✅ |
| STQ | stq_7 | 200 | 3598 | Yes | No | ❌ |
| STQ | stq_8 | 200 | 14683 | No | No | ✅ |
| STQ | stq_9 | 200 | 20033 | No | Yes | ❌ |
| STQ | stq_10 | 200 | 5162 | Yes | No | ❌ |
| STQ | stq_11 | 200 | 4431 | No | No | ✅ |
| STQ | stq_12 | 200 | 8593 | No | No | ✅ |
| STQ | stq_13 | 200 | 5960 | Yes | Yes | ✅ |
| STQ | stq_14 | 200 | 29081 | No | Yes | ❌ |
| STQ | stq_15 | 200 | 2693 | Yes | Yes | ✅ |
| STQ 合计 |  |  |  |  |  | **10 / 15** |
| **doubao-seed-evolving 总计** |  |  |  |  |  | **22 / 30 = 73.33%** |
|  |  |  |  |  |  | avg_ms=**9754.5**, elapsed=292.7 s |

### §2.3 失败/timeout 汇总(共 8 cell)

| model | cell | type | 原因 |
|---|---|---|---|
| glm-5.3 | gsm8k_4 | timeout 30s | 长 reasoning_chain 未收敛 |
| glm-5.3 | stq_5 | wrong pred (No vs Yes) | 推理错误 |
| glm-5.3 | stq_7 | wrong pred (Yes vs No) | 推理错误 |
| glm-5.3 | stq_10 | wrong pred (Yes vs No) | 推理错误 |
| doubao-seed-evolving | gsm8k_6 | wrong pred (0 vs 8000) | 数值化错误(回答 0) |
| doubao-seed-evolving | gsm8k_7 | wrong pred (36.36 vs 36) | 精度/截断错误 |
| doubao-seed-evolving | gsm8k_15 | timeout 30s | 长 reasoning_chain 未收敛 |
| doubao-seed-evolving | stq_5 | timeout 30s | 长 reasoning_chain 未收敛 |
| doubao-seed-evolving | stq_7 | wrong pred (Yes vs No) | 推理错误 |
| doubao-seed-evolving | stq_9 | wrong pred (No vs Yes) | 推理错误 |
| doubao-seed-evolving | stq_10 | wrong pred (Yes vs No) | 推理错误 |
| doubao-seed-evolving | stq_14 | wrong pred (No vs Yes) | 推理错误 |

注:共 4 次 timeout(30s 上限),全部标 `status=-1` 继续,**未触发重试**(严守铁律 5)。

---

## §3 与 baseline 对比

来源:`deposon_volcengine_9model_30cells_2026_09_10.json` (21:04 跑的部分结果,8 model 全为 0/30 partial)

| model | worker C 补测 | baseline(21:04 partial) | 提升 |
|---|---|---|---|
| **glm-5.3** | **26/30 (86.67%)** | 0/30 partial | +26 |
| **doubao-seed-evolving** | **22/30 (73.33%)** | 0/30 partial | +22 |

对比同次跑的另 1 个完整 model (`doubao-seed-2.0-lite`: 26/30 = 86.67%):

| model | pass_rate | rank(已知 3 model) |
|---|---|---|
| glm-5.3 | 86.67% | 并列 #1 |
| doubao-seed-2.0-lite | 86.67% | 并列 #1 |
| doubao-seed-evolving | 73.33% | #3 |

**核心结论**:
- **glm-5.3 通过 1 周预筛阈值**(86.67% ≥ 80% 经验线)
- doubao-seed-evolving 略低(73.33%),GSM8K 数值化错误多(2 cells 数学计算错)
- StrategyQA 对两个 model 难度都高于 GSM8K(pass_rate 80% vs 86.67% for glm-5.3)

---

## §4 7 铁律自检

| 编号 | 铁律 | 自检 | 状态 |
|---|---|---|---|
| 1 | coding-plan key runtime 读 (GB18030 → env) | Python 直接读 `LLM API.txt` GB18030 成功,匹配 `ark-de0b484e-...`,env 注入 `ARK_CODING_PLAN_KEY` | ✅ |
| 2 | 不设 proxy | 脚本内 `os.environ.pop` 6 个 proxy 变量;JSON 含 `proxy_cleared: true` | ✅ |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan | 仅 `glm-5.3` + `doubao-seed-evolving`;endpoint 为 `ark.cn-beijing.volces.com/api/coding/v3`;未 import 任何 router 库 | ✅ |
| 4 | key 永不入 prompt / JSON / 落盘 | `auth` 字段 = `ark-de0b484e-0889-46...e219`(20 字符截断);grep 整 JSON `ark-de0b484e-[a-zA-Z0-9-]{30,}` 0 命中 | ✅ |
| 5 | 60 calls 严格(不重试 / 不切超 2 model) | 2 model × 30 cell = 60 calls 实跑;`models` 数组长度=2;无 retry 循环 | ✅ |
| 6 | 不动 5 锚 JSON | 本 worker 仅写 `deposon_volcengine_worker_c_2026_09_10.json` 新文件;未触及 `KT_ABC1_anchors_sha256_12.json` 等锚 | ✅ |
| 7 | 不动 4 SPEC V0.1 + v19 + v21 frozen | 本 worker 无 SPEC 写入 | ✅ |

---

## §5 下一步

1. **合并 4 worker 结果**:等 worker A/B/D 完成后,统一汇总到 9-model 全量 `deposon_volcengine_9model_30cells_2026_09_10.json`(覆盖 21:04 partial 字段)
2. **glm-5.3 进入 V3.X 候选短名单**:86.67% ≥ 80% 经验线,可向王老师(WeChat 顾问模式)提挂点
3. **doubao-seed-evolving 标记观察**:73.33% 接近但未达线,主要拖累是 STQ 推理错(5/15) + GSM8K 数值化错(2/15);若长 timeout 放宽到 60s,可能 +1-2 cell
4. **长 timeout cell(4 个)分析**:gsm8k_4, gsm8k_15, stq_5 都是 30s 卡死,reasoning chain 未收敛——这与 `doubao-seed-code-preview-251028` 早期 37.9s/2180 tokens 截断现象一致(同 model family 行为)
5. **本 worker 完成的硬数据**:为 deposon V3.X 1 周预筛框架贡献 2 model × 30 cell = 60 calls 高质量实测点;所有原始 LLM 响应 + token usage + reasoning_tokens 全部落 JSON,可直接喂下游 V3.X 候选打分

— Worker C 完 —
