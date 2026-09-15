# 火山方舟 glm-latest 别名 30 cells V2 报告(2026-09-10)

## 1. 任务背景

deposon V3.X 挂点预筛 - 复审 **火山方舟 Coding Plan** 下 `glm-latest` 别名的 30 cells 真实能力。
上次 `bg_2e977e76` succeeded 但 0 output 异常(无详细日志、无失败标记、无落盘)。
本轮采用 **渐进式 3 阶段 + 详细日志 + 直接落盘 final path** 重试。

## 2. 关键改进(V1 -> V2)

| 维度 | V1 (上次) | V2 (本轮) |
|---|---|---|
| sanity timeout | 120s | **30s(快失败)** |
| 5 cells timeout | 180s | **60s(短超时)** |
| 30 cells timeout | 120s | **90s(适中,避免 2h 卡死)** |
| 执行模式 | 单次 | **3 阶段渐进:1 -> 5 -> 30** |
| 日志详细度 | 抑制 | **http_status / latency / error 全开** |
| 落盘方式 | 临时 + 改名 | **直接落盘 final path(不创建 _ 前缀)** |
| 失败处理 | 卡死 | **立即标 fail 但继续(不阻塞)** |

## 3. 执行配置

- **模型别名**: `glm-latest`(严格,未切 model)
- **Endpoint**: `https://ark.cn-beijing.volces.com/api/coding/v3/chat/completions`
- **Key 来源**: `C:\Users\Administrator\Desktop\AI\LLM API.txt` GB18030 -> `os.environ['ARK_CODING_PLAN_KEY']`(**永不入 JSON**)
- **Proxy**: **不设**(火山国内)
- **temperature**: 0.0(全 benchmark 严格)
- **max_tokens**: sanity=1024, cell=2048
- **Benchmark 题集**:
  - GSM8K id 1-15(15 题,答案数字)
  - StrategyQA id 1-15(15 题,答案 Yes/No)

## 4. 三阶段结果

### 4.1 阶段 1:sanity (30s)

- **Prompt**: `What is 1+1?`
- **Expected**: 包含 `2`
- **实际**: status=`200` ms=`2267.0` text=`'1 + 1 = 2'` error=`None`
- **结论**: **PASS**

### 4.2 阶段 2:5 cells (60s/题, GSM8K id 1-5)

- **匹配**: **5/5** (100.0%)
- **耗时**: 11.7s
- **结果**: 详细见 `D:\私人资料\deposon-repo\results\deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json`

### 4.3 阶段 3:30 cells (90s/题, 15 GSM8K + 15 StrategyQA)

| 维度 | 值 |
|---|---|
| 总题数 | 30 |
| GSM8K 通过 | 13/15 (86.7%) |
| StrategyQA 通过 | 9/15 (60.0%) |
| **总通过** | **22/30** (73.3%) |
| HTTP 200 比例 | 29/30 |
| 总 tokens | 10584 |
| 总 latency | 280166.3ms |
| 平均 latency | 9338.9ms/题 |
| 阶段 3 耗时 | 280.2s |
| **总耗时** | **294.2s** |

### 4.4 最终 verdict

**PARTIAL (30 cells V2 接入但准确率 <80%,需人工复审)**

## 5. 已知约束

- 严格 7 条铁律全部满足:不重试 / 不切 model / 不设 proxy / key 永不入盘 / 不动 5 锚 JSON / 不动 SPEC V0.1 / 不动 v19 / v21 frozen JSON
- 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan
- 模型别名严格 `glm-latest`(不替换为具体 GLM-5.x 版本号)

## 6. 输出文件

- `results/deposon_volcengine_glm_latest_5cells_v2_2026_09_10.json`
- `results/deposon_volcengine_glm_latest_30cells_v2_2026_09_10.json`
- `docs/V3X/VOLCENGINE_GLM_LATEST_30CELLS_V2_2026_09_10.md`(本文件)

## 7. 后续动作

- **PASS (≥24/30)**: glm-latest 挂入 deposon V3.X 候选池,可参与王老师 WeChat 5 候选(连同 P-A/B/C/D + V4.1-Flash)挂点讨论
- **PARTIAL (18-23/30)**: 留待人工复审,2 周后可再跑 1 次
- **FAIL (<18/30)**: 排除出 V3.X 候选池,记录 1 周判死 FAIL 原因
