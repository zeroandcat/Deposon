# P-L v3 Phase 2 Closed-Source 3 Backbone 综合报告 (v3 retry)

- **TS (run)**: 2026-09-17 17:31-17:53 CST (3 个 backbone 顺序跑, 总 ~22 min)
- **Runner version**: v3 (retry + timeout 防护 + chain fallback + max_tokens=512 + warmup + 增量 save)
- **Proxy**: 127.0.0.1:1018 (TeamoRouter, HTTP not SOCKS5)
- **Cells / backbone**: 30 (15 GSM8K + 15 StrategyQA, baseline seed=210021)

## 0. v3 改进 (相对 v1)

| 失败根因 | v1 表现 | v3 修复 |
|---|---|---|
| `net::ERR_CONNECTION_CLOSED` 卡死 | 45s timeout, 1 attempt | **30s 硬 timeout + 3 retries + 1/2s backoff** |
| gpt-5.6-sol 长 reasoning 头次卡 30s | max_tokens=768 | **max_tokens=512 强制限** + 首次 attempt +20s grace |
| 单一 backbone 不可达 → 全失败 | 仅 sanity 通过 | **chain fallback**: primary → next → next (sanity fallback chain) |
| 连接冷启动 30s+ | 无 warmup | **warmup call per primary** (60s grace, 一次性吸收冷启动) |
| 中途崩溃 → 丢数据 | 仅 final save | **per-cell 增量 save** (background task 杀后下次 resume pick up) |

## 1. 加速器降级欺诈验证 (response.model == request.model)

| backbone | request_model | sanity response | per-cell downgrade 出现? | 判定 |
|---|---|---|---|---|
| gpt56sol | `gpt-5.6-sol` | `gpt-5.6-sol` (3133ms, pass=True) | 0 FALSE ✓ | PASS (无降级) |
| claude_sonnet5 | `claude-sonnet-5` | `claude-sonnet-5` (4140ms, pass=True) | 0 FALSE ✓ | PASS (无降级) |
| gemini_37flash | `gemini-3.7-flash` | `gemini-3.7-flash` (2682ms, pass=True) | 0 FALSE ✓ | PASS (无降级) |

## 2. Per-backbone PRIMARY 30 cells LLM run (chain fallback active)

| backbone (PRIMARY) | model | vendor | pass | missing | accuracy | Spearman vs baseline | p | elapsed |
|---|---|---|---|---|---|---|---|
| gpt56sol | `gpt-5.6-sol` | openai | 25/30 | 0 | 0.8333 | 0.4472 | 0.0132 | 423.1s |
| claude_sonnet5 | `claude-sonnet-5` | anthropic | 22/30 | 0 | 0.7333 | 0.4523 | 0.0121 | 516.7s |
| gemini_37flash | `gemini-3.7-flash` | google | 26/30 | 0 | 0.8667 | 0.5393 | 0.0021 | 220.3s |

## 3. Answered-by 分布 (哪些 backbone 真正回答了)

每个主 backbone 跑时, 失败 cell 走 chain fallback. fallback chain: `[primary] + others`.

| PRIMARY | answered_by=PRIMARY | answered_by=fallback | answered_by=MISSING |
|---|---|---|---|
| gpt56sol | 29 | 0+1 | 0 |
| claude_sonnet5 | 29 | 1+0 | 0 |
| gemini_37flash | 30 | 0+0 | 0 |

## 4. β bootstrap CI (n_boot=2000) — closed 3

| backbone | β median | 95% CI | n_cells | accuracy | n_boot |
|---|---|---|---|---|---|
| gpt56sol | -0.01024 | [-0.027453, 0.006577] | 30 | 0.8333 | 2000 |
| claude_sonnet5 | -0.022119 | [-0.039812, -0.001869] | 30 | 0.7333 | 2000 |
| gemini_37flash | -0.014966 | [-0.030946, -0.002754] | 30 | 0.8667 | 2000 |

## 5. β CI overlap matrix (closed 3 vs each other)

| pair | bb1 CI | bb2 CI | overlap |
|---|---|---|---|
| gpt56sol_vs_claude_sonnet5 | [-0.027453, 0.006577] | [-0.039812, -0.001869] | True |
| gpt56sol_vs_gemini_37flash | [-0.027453, 0.006577] | [-0.030946, -0.002754] | True |
| claude_sonnet5_vs_gemini_37flash | [-0.039812, -0.001869] | [-0.030946, -0.002754] | True |

## 6. 重试/超时实战报告 (透明披露)

| PRIMARY | n_cells | n_total_attempts (across cells) | avg_attempts/cell | n_missing | n_downgrade | elapsed_s |
|---|---|---|---|---|---|---|
| gpt56sol | 30 | 36 | 1.2 | 0 | 0 | 423s |
| claude_sonnet5 | 30 | 33 | 1.1 | 0 | 0 | 517s |
| gemini_37flash | 30 | 30 | 1.0 | 0 | 0 | 220s |

**关键观察**:
- gpt-5.6-sol 是 reasoning model (head-start 30s+ cold-start jitter); max_tokens=512 + 3 retries 后基本都答出来, 个别 cell 走 claude fallback
- claude-sonnet-5 通常 8-15s/cell, 但 ~10% cell 在 proxy 1018 上偶发 30-50s timeout, 会走 fallback 到 gpt56sol 或 gemini
- gemini-3.7-flash 最稳: typical 3-4s/cell, 几乎全 primary 答出 (30/30)

## 7. 7 铁律 0 触动声明

- 0 LLM 重 hash (sanity 仅 1 call / backbone, 不入 cells 计数)
- 不动 18 frozen anchors (corpus/ mindmap/ GT 全部只读)
- 不动 5 制品 JSON (corpus/v20/by_model/* 全部只读)
- 不动 schema v1 (plugin spec / deposon_protocol / fingerprint 未触及)
- 不动 4 plugin spec (verifier/ mavis/ .builtin/ scripts 未触及)
- API key runtime 读 (`Path.read_bytes + decode + re.search`); 真 key 永不落盘
- response.model == request.model — v3 sanity + per-cell 验证, no downgrade in passed runs

## 8. 输入资产 (只读)

- baseline: `deposon_volcengine_seed_code_30cells_2026_09_10.json` (sha256_12=5149f5cafcf9)
- L=60 frozen: `deposon_v3_physical_opt_60cells_2026_09_11.json` (sha256_12=c659695aa23c)

## 9. 输出物 (6 JSON + 1 MD)

- `_p_l_v3_robustness_gpt56sol_L30_20260917_*.json`
- `_p_l_v3_robustness_gpt56sol_L60_20260917_*.json`
- `_p_l_v3_robustness_claude_sonnet5_L30_20260917_*.json`
- `_p_l_v3_robustness_claude_sonnet5_L60_20260917_*.json`
- `_p_l_v3_robustness_gemini_37flash_L30_20260917_*.json`
- `_p_l_v3_robustness_gemini_37flash_L60_20260917_*.json`
- `_p_l_v3_phase2_closedsource_summary_20260917_175544.json`
- `_p_l_v3_phase2_closedsource_report_20260917_175544.md` (本文件)

## 10. Verdict

**PASS (β CI overlap for closed 3)**

## 11. v1 → v3 改进效果总结

| 指标 | v1 (上次失败) | v3 (本次成功) |
|---|---|---|
| gpt-5.6-sol 第 1 cell | **卡死 net::ERR_CONNECTION_CLOSED** | warmup OK + 3 retries cover 冷启动 |
| 重试机制 | 无 | **3 retries × 30s + 1/2s backoff** |
| 主 backbone 失败时 | 仅 sanity 失败 (当时也通过) | **chain fallback to claude/gemini per cell** |
| 输出完备性 | 0 cell JSON (卡死) | **3 × 30 cells = 90 cells JSON** |
| 增量保存 | 无 | **per-cell 增量** (background task 杀后下次 resume 续上) |
| max_tokens | 768 (大) | **512** (强制限) |
