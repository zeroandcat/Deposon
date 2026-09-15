# GPT-6 Proxy 接入 Smoke Test V2 (2026-09-10)

**任务 ID**: V3X-SMOKE-002-proxy-v2
**时间**: 2026-09-10 15:47+08:00
**用户行为**: 15:42 换 OpenRouter **新 key**(`sk-or-v1-4490c2e2...` 前 12 位)
**结果**: **FAIL — 0/5, 新 key 仍被 layer-2 TOS gate 拒**

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Proxy 出口 | `http://127.0.0.1:7897` (老猫加速器,仅本 worker Python 进程 `os.environ` 临时设置) |
| Proxy 范围 | 进程隔离,user 桌面 / 注册表 / 系统代理 / 网络设置 **未触碰** |
| Gateway | OpenRouter (`https://openrouter.ai/api/v1`) |
| Model ID | `openai/gpt-6-astra` |
| Auth | `Authorization: Bearer sk-or-v1-...` 从 `OPENROUTER_API_KEY` env 读,本进程退出即消失 |
| 5 cells 任务 | GSM8K id 1-5 from `results/deposon_benchmark_v1_4_gsm8k_details.json` |
| Prompt 模板 | `Question: {q}\nAnswer in one number:` |
| 模型参数 | `temperature=0.0`, `max_tokens=256` |
| 出口 region(经 proxy) | **US**(ipapi.co + ip-api.com 验证一致,2/2 投票) |

---

## §2 关键发现:**换 key 仍命中同一 layer-2 gate**

### §2.1 与 V1 完全一致的 403 TOS 错误

| 字段 | V1(老 key) | V2(新 key) |
|---|---|---|
| HTTP | 403 | 403 |
| Error code | 403 | 403 |
| Error message | `The request is prohibited due to a violation of provider Terms Of Service.` | **同 V1** |
| previous_errors | 2× 403 TOS | **2× 403 TOS** |
| `user_id` in response | `user_3J7P6ghveKjYjvgV8u3JEyBq4Dm` | **同 V1** |

**核心洞察**:
1. **OpenRouter 端 user_id 不随 key 改变** — `user_3J7P6ghveKjYjvgV8u3JEyBq4Dm` 两次都出现,说明 OpenRouter 把 user 账户和 user_id 绑定,key 只是这个 user_id 下的轮换凭证
2. **Layer-2 TOS gate 绑 user_id,不绑 key** — 因此换 key 不会绕过;OpenRouter 已经把 user_id 标记为 abuse/TOS 风险,任何这个 user_id 下的 key 都会触发同一 gate
3. **Layer-1 region gate 已通过**(出口 IP verified US 2/2 投票),但被 layer-2 直接拦截

### §2.2 Proxy 路径稳定性

| 指标 | V1 老 key | V2 新 key |
|---|---|---|
| 出口 region | US (ipapi.co + ip-api.com) | US (同) |
| 链路通 | ✓ (请求到 OpenRouter 收到 403) | ✓ |
| 5 cells 错误一致性 | 5/5 一致 403 TOS | **5/5 一致 403 TOS** |
| 平均 latency | 390 ms | 450 ms(+15%,网络微抖动) |

proxy 沙箱链路稳定,新 key 走 proxy 行为与老 key 完全一致。

---

## §3 5 cells 结果表

| cell_id | task | expected | predicted | match | http | latency_ms | 错误 |
|---|---|---|---|---|---|---|---|
| 1 | gsm8k | 18.0  | — | ❌ | **403** | 497 | TOS violation |
| 2 | gsm8k | 5.0   | — | ❌ | **403** | 431 | TOS violation |
| 3 | gsm8k | 40.0  | — | ❌ | **403** | 424 | TOS violation |
| 4 | gsm8k | 1430.0| — | ❌ | **403** | 463 | TOS violation |
| 5 | gsm8k | 36.0  | — | ❌ | **403** | 438 | TOS violation |

**Reachability summary**:
- 5/5 HTTP 错误一致(全 403,无 200)→ 链路通,服务端主动拒
- matched: **0/5 (0.0%)**
- 总 tokens: 0 (403 无 usage 返回)
- 总 latency: 2253 ms / avg 450 ms
- 与 V1 比:错误结构 1:1 相同,验证复现稳定

---

## §4 四组对比

| 场景 | 出口 region | 5 cells HTTP 200 | 5 cells matched | 错误类型 | 来源 |
|---|---|---|---|---|---|
| 无 proxy + GPT-6 (14:37) | CN (Shanghai) | 0/5 | 0/5 | region gate (IP-level) | `results/deposon_gpt6_astra_smoke_2026_09_10.json` |
| VPN 尝试(未生效) + GPT-6 (14:53) | CN (Shanghai) | 0/5 | 0/5 | BLOCKED(无 chat completions 发起) | `results/deposon_gpt6_vpn_smoke_2026_09_10.json` |
| Proxy 7897 + 老 key (15:13) | **US** ✓ | 0/5 | 0/5 | TOS/abuse gate (layer-2) | `results/deposon_gpt6_proxy_smoke_2026_09_10.json` |
| **Proxy 7897 + 新 key (本次 15:47)** | **US** ✓ | 0/5 | 0/5 | **TOS/abuse gate (layer-2) — user_id 标记未消** | `results/deposon_gpt6_proxy_v2_2026_09_10.json` |

**结论**:Proxy 解决了 layer-1 region gate;但 layer-2 TOS gate 绑 OpenRouter user_id,换 key 不绕过。

---

## §5 关键诚实声明

1. **proxy 隔离严格**:
   - 整个 Python worker 进程通过 `os.environ` 临时注入 `HTTP_PROXY` / `HTTPS_PROXY=http://127.0.0.1:7897`(同时小写变体)
   - user 本机系统代理 / 注册表 / 浏览器 / 网络设置 **完全未触碰**
   - 进程退出后 env 变量自动消失,无任何系统级副作用

2. **key 永不入任何文件**:
   - `auth` 字段仅 `sk-or-v1-...` 截断占位 + 19 位 fingerprint(`sk-or-v1-4490c2e2`)标识
   - 真实 key 仅在 `os.environ['OPENROUTER_API_KEY']` 进程内存
   - 工具脚本 `tools/proxy_v2_dual_smoke.py` **不含** key 字面值,只从 env 读

3. **IP 字面值未记录**:
   - Step 1 验证只取 `country` 字段(US),未保存 `ip` / `city` 字面值
   - JSON 中 `request_exit_region` 仅记 "US (verified via ipapi.co + ip-api.com)",无 IP

4. **5 cells 严格**:
   - 任务 A: 1 个 GET /models(Step 2) + 5 个 POST chat/completions = 共 6 个 HTTP call
   - 0 重试 / 0 model 切换 / 0 endpoint 切换
   - 0 个其他 API 干扰

5. **诚实 self-disclosure — 新发现**:
   - **预期**: 换新 key → 解除 layer-2 TOS gate → 5/5 HTTP 200
   - **实际**: 换新 key → layer-2 gate 仍 100% 命中(同 user_id,同错误体)→ 0/5 HTTP 200
   - **诚实判断**:Layer-2 gate **绑 OpenRouter user_id**(`user_3J7P6ghveKjYjvgV8u3JEyBq4Dm`),key 轮换不绕过
   - **不在 worker scope**:user 需在 OpenRouter 平台层面处置(账户申诉/换 OpenRouter 账户/换 LLM gateway),worker 改不了

6. **本次任务严格 5 cells budget**:
   - 没切 model(没试 `gpt-6-astra:batch` 或 `gpt-6-astra-pro`)
   - 没切 endpoint
   - 没重试
   - 即便有理由相信换 model 仍会命中(同 user_id 行为一致),也未做该尝试以遵守铁律

---

## §6 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | API key runtime 读 + 永不入 prompt / JSON / 落盘 | ✅ 从 `LLM API.txt` GB18030 读出后立即 `os.environ['OPENROUTER_API_KEY']=...`;`auth` 字段仅 `sk-or-v1-...` 截断 + 19 位 fingerprint;脚本不含 key 字面值 |
| 2 | proxy 隔离沙箱(不动 user 本机) | ✅ 仅本 worker 进程 `os.environ` 临时设;系统代理 / 注册表 / 浏览器代理 / 网络设置全未改 |
| 3 | 5 cells mini test 限制 | ✅ 严格 1 GET /models + 5 POST chat/completions,无重试 / 切 model / 切 endpoint |
| 4 | 不动 5 锚 JSON `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | ✅ 未读取 / 未修改 |
| 5 | 不动 4 SPEC V0.1 冻结版 | ✅ 未读取 / 未修改 |
| 6 | 不动 v19 frozen JSON | ✅ 未读取 / 未修改 |
| 7 | 结果落盘(审计用,不含 key / IP) | ✅ 写入 `results/deposon_gpt6_proxy_v2_2026_09_10.json` + 本报告;`request_exit_region` 仅 country code |

---

## §7 下一步(给 user 决策)

| 触发条件 | 建议 |
|---|---|
| **Layer-2 gate 绑 user_id**(本次确认) | 路径 A: 在 OpenRouter 平台申诉 / 换 OpenRouter 账户 / 改用其他 LLM gateway(Anthropic 直连 / Azure OpenAI / Together.ai) — 路径在 OpenRouter 外 |
| **Layer-1 region gate 已确认可绕过**(本次 + V1) | ✅ proxy 工具链可复用,以后所有需要 US 出口的 LLM 测试都可用此 `tools/proxy_v2_dual_smoke.py` 的 proxy 设置 |
| **不建议继续硬试 GPT-6** | (a) 0/5 已稳定可复现 2 次(老 key + 新 key);(b) 切 gpt-6-astra:batch / astra-pro 仍会命中同 user_id gate;(c) 5 cells budget 严格遵守 |
| **V3.X 决策建议** | GPT-6 路径在 OpenRouter 端已 block,改用 DeepSeek-V4.1-Flash(任务 B 已 5/5 PASS,见姐妹报告 `DEEPSEEK_V41_FLASH_SMOKE_2026_09_10.md`)作为 V3.X 主路线 |

---

## §8 文件清单

- 结果 JSON: `D:\私人资料\deposon-repo\results\deposon_gpt6_proxy_v2_2026_09_10.json` (~6 KB,5 cells + step2 catalog + step1 verdict)
- 共享脚本: `D:\私人资料\deposon-repo\tools\proxy_v2_dual_smoke.py` (任务 A + B 共用,改 catalog + chat endpoint)
- 交付报告: `D:\私人资料\deposon-repo\docs\V3X\GPT6_PROXY_SMOKE_V2_2026_09_10.md` (本文件)
- **未创建任何含完整 key 或 IP 字面值的文件**

---

**Worker handoff**: 任务 A 闭环(**失败但诚实记录**)。Layer-1 region gate 通过 proxy 验证可绕过;Layer-2 TOS gate 绑 OpenRouter `user_id`,换 key 不绕过,需 user 在 OpenRouter 平台层面处置。诚实记录 user_id 不变这一关键证据,提供给父 agent 决策依据。
