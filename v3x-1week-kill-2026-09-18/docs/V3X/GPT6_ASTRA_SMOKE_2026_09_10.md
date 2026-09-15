# GPT-6-Astra OpenRouter 接入 Smoke Test

- **日期**: 2026-09-10
- **任务 ID**: V3X-SMOKE-001
- **Worker**: Mavis worker (sub-agent)
- **结果 JSON**: `results/deposon_gpt6_astra_smoke_2026_09_10.json`

## §1 测试环境

| 项 | 值 |
| --- | --- |
| Gateway | OpenRouter (`https://openrouter.ai/api/v1`) |
| Model ID | `openai/gpt-6-astra` |
| Auth | `Authorization: Bearer sk-or-v1-...` (从 `OPENROUTER_API_KEY` 环境变量读) |
| 5 cells 任务 | GSM8K 前 5 题 (取自 `results/deposon_benchmark_v1_4_gsm8k_details.json` id 1-5) |
| Prompt 模板 | `Question: {q}\nAnswer in one number:` |
| 模型参数 | `temperature=0.0`, `max_tokens=256` |
| 用户申报 | OpenRouter billing 已改 US 虚拟地址 (袁祺皓 + 3088204160@qq.com + 1018 SW Main St, Portland, OR 97201 US) |
| 调用机器 region | `cn` (agent-context) |

## §2 5 cells 结果表

| cell_id | task | expected | predicted | match | prompt_tokens | completion_tokens | total | latency_ms | http_status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | gsm8k | 18 | — | ❌ | — | — | — | 1045 | **403** |
| 2 | gsm8k | 5 | — | ❌ | — | — | — | 700 | **403** |
| 3 | gsm8k | 40 | — | ❌ | — | — | — | 750 | **403** |
| 4 | gsm8k | 1430 | — | ❌ | — | — | — | 650 | **403** |
| 5 | gsm8k | 36 | — | ❌ | — | — | — | 759 | **403** |

所有 5 cells 错误信息一致:

```json
{"error":{"message":"This model is not available in your region.",
  "code":403,
  "metadata":{"routing_funnel":[{"step":"Initial Endpoints","endpoint_count":5}],
  "failed_routing_step":"Gate Endpoints with Geo Restrictions"}}}
```

> OpenRouter 错误 `failed_routing_step: "Gate Endpoints with Geo Restrictions"` 表明这是 **IP/请求级 region gate** 而非 billing-level;改 billing address 不绕开此 gate。

## §2.5 前期 GET /models 可达性验证 (Step 2)

| 项 | 结果 |
| --- | --- |
| HTTP 状态 | **200 OK** |
| Models 数量 | 436 |
| `openai/gpt-6-astra` 在列表中 | ✅ 存在 |
| `openai/gpt-6-astra-pro` 在列表中 | ✅ 存在 |
| `openai/gpt-6-astra:batch` 在列表中 | ✅ 存在 |
| 5.x 系列 | 5.6 / 5.5 / 5.4 / 5.3-codex 均存在 |

结论: **OpenRouter key 有效,模型已上架,但推理端 region-gated。**

## §3 总结

| 指标 | 值 |
| --- | --- |
| 5 cells 通过 | **0 / 5 (0.0%)** |
| 全部 PASS? | ❌ |
| 全部 HTTP 200? | ❌ |
| 总 token | 0 (5 cells 全部 403,无 usage 返回) |
| 总 latency | 3904 ms |
| 平均 latency | 780 ms / cell (含 5 次 403 网络往返) |

**最终判定: 接入 smoke test ❌ FAIL**。GPT-6-Astra 在中国 region IP 下被 OpenRouter 拦截,即使 billing 已切到 US 虚拟地址,billing 不影响 region gate。

## §4 7 铁律自检

| # | 铁律 | 状态 |
| --- | --- | --- |
| 1 | API key 只走 env,绝无字面值落盘 | ✅ key 仅在 `os.environ['OPENROUTER_API_KEY']` 内存;`tools/gpt6_astra_smoke.py` 与 `results/deposon_gpt6_astra_smoke_2026_09_10.json` 均不含 key 字面值 (仅以 `sk-or-v1-...` 截断占位) |
| 2 | 不调除 GPT-6 外其他 LLM | ✅ 仅 `openai/gpt-6-astra` (1 GET /models + 5 POST chat/completions) |
| 3 | 5 cells mini test | ✅ 严格 5 cells,无重试 |
| 4 | 5 锚 JSON 不动 | ✅ `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 未访问、未修改 |
| 5 | 4 SPEC V0.1 冻结版不动 | ✅ `docs/V3X/KT_?1_SPEC_V0.1.md` 未访问、未修改 |
| 6 | v19 frozen JSON 不动 | ✅ `results/deposon_v19_benchmark_fixes.json` 仅 read (提取前 5 题 id+answer),未修改 |
| 7 | 结果落盘 (审计用,不含 key) | ✅ 写入 `results/deposon_gpt6_astra_smoke_2026_09_10.json` + 本报告 |

## §5 关键诚实声明

1. **这不是完整判死,只是 smoke test**: 任务只验证 OpenRouter + GPT-6-Astra 可达性,不评估模型质量、不做 benchmark。
2. **5 cells 全部 403 失败**: 不代表 GPT-6-Astra 模型质量问题,代表 **OpenRouter 端 IP-level region gate 拒绝来自 cn 区域的请求**。即便 billing address 改成 US,billing ≠ request region;OpenRouter 的 `failed_routing_step: "Gate Endpoints with Geo Restrictions"` 是按请求出口 IP 判断。
3. **未尝试绕过** (VPN / 代理 / 改 endpoint / 重试): 严格遵守 5 cells 节省原则;任何"绕过 region gate"操作超出本任务 scope,需 parent 重新授权。
4. **建议后续路径** (留作 parent 决定,本 worker 不动):
   - (a) 在 US-region 出口 (如海外 VPS) 跑 5 cells,验证排除 IP 因素后模型本身质量;
   - (b) 改用 `:batch` 变体或非 region-gated 的 `gpt-5.x` 系列 (OpenRouter catalog 显示 5.6/5.5/5.4/5.3-codex 均可调,同样需 cell 验证);
   - (c) 维持判定: 接入失败,需换 gateway / 换 model。
5. **结果与 v1.4 cot 结果不可比**: v1.4 用 Kimi 跑 GSM8K,本次用 OpenRouter+GPT-6;两者 LLM backend 不同,即便本测试通过,也只能说明 OpenRouter 这条链路 OK,不能直接下"GPT-6 在 GSM8K 上 X% 准确率"的结论。
6. **数据完整性**: 5 cells 全部失败但 **不是网络断**,5 次 HTTP 请求都成功到达 OpenRouter 并拿到 403 JSON 响应,证明链路通畅,失败原因 = OpenRouter 服务端 region gate 主动拒绝。
