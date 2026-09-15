# GPT-6 Proxy 接入 Smoke Test (2026-09-10)

**任务 ID**: V3X-SMOKE-002(proxy path)
**时间**: 2026-09-10 15:13+08:00
**结果**: **PARTIAL — Proxy 出口 US ✓,但 GPT-6 仍 0/5;错误已从 region gate 升级到 TOS/fraud gate**

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Proxy 出口 | `http://127.0.0.1:7897` (老猫加速器,**仅本 worker Python 进程的 `os.environ` 临时设置,不动 user 本机系统**) |
| Proxy 范围 | 进程隔离:本脚本顶层 `os.environ['HTTP_PROXY']=...` + `HTTPS_PROXY=...`;user 桌面 / 注册表 / 系统代理 / 网络设置 **未触碰** |
| Gateway | OpenRouter (`https://openrouter.ai/api/v1`) |
| Model ID | `openai/gpt-6-astra` |
| Auth | `Authorization: Bearer sk-or-v1-...` (从 `OPENROUTER_API_KEY` env 读;本进程退出即消失) |
| 5 cells 任务 | GSM8K id 1-5 from `results/deposon_benchmark_v1_4_gsm8k_details.json` |
| Prompt 模板 | `Question: {q}\nAnswer in one number:` |
| 模型参数 | `temperature=0.0`, `max_tokens=256` |
| 用户申报 | OpenRouter billing 已改 US 虚拟地址(袁祺皓 + 3088204160@qq.com + 1018 SW Main St, Portland, OR 97201 US) |
| 出口 region(经 proxy) | **US**(ipapi.co + ip-api.com 验证一致;ipinfo.io 限流 429;ifconfig.co 返回 Brazil 异常) |
| 出口 region(不经 proxy baseline) | ERR_HTTPError(可能 ipinfo 限流叠加) |

---

## §2 关键发现:错误类型从 region gate 升级到 TOS gate

| 阶段 | 错误信息 | 含义 |
|---|---|---|
| 无 proxy(`results/deposon_gpt6_astra_smoke_2026_09_10.json` 14:37) | `"This model is not available in your region."` (failed_routing_step: `"Gate Endpoints with Geo Restrictions"`) | **IP-level region gate** |
| VPN 尝试(实际未生效) | (无 chat completions 发起) | — |
| **Proxy 7897(本次)** | `"The request is prohibited due to a violation of provider Terms Of Service."` (provider_name: null, previous_errors: 2× 403 TOS) | **Account-level TOS/abuse gate** |

**核心洞察**:proxy **成功绕过 region gate**(出口 IP 在 US 验证),但 OpenRouter/上游 OpenAI **在 account 层面识别出 TOS 违规并主动拒绝**。这说明:
1. 之前 region gate 失败的根因不在 user 本机出口 IP 单一因素,OpenRouter 还在做 **account-level abuse/fraud 检测**
2. 可能触发因素:虚拟 US billing 地址 + 实际 proxy 出口 IP 信誉(老猫加速器 IP 可能已被标记为 datacenter/proxy 信誉低) + 短期高频切换 region 的反常行为
3. 即便 region 改对,OpenRouter 仍可能在 account 维度 gate(这是 user 需要在 OpenRouter 平台层面处理的,worker 改不了)

---

## §3 5 cells 结果表

| cell_id | task | expected | predicted | match | http | latency_ms | 错误 |
|---|---|---|---|---|---|---|---|
| 1 | gsm8k | 18.0 | — | ❌ | **403** | 445 | TOS violation |
| 2 | gsm8k | 5.0  | — | ❌ | **403** | 383 | TOS violation |
| 3 | gsm8k | 40.0 | — | ❌ | **403** | 379 | TOS violation |
| 4 | gsm8k | 1430.0 | — | ❌ | **403** | 378 | TOS violation |
| 5 | gsm8k | 36.0 | — | ❌ | **403** | 369 | TOS violation |

完整错误体(全部 5 cells 一致):
```json
{"error":{"message":"The request is prohibited due to a violation of provider Terms Of Service.",
  "code":403,
  "metadata":{"provider_name":null,
    "previous_errors":[{"code":403,"message":"...TOS..."},{"code":403,"message":"...TOS..."}]}},
  "user_id":"user_3J7P6ghveKjYjvgV8u3JEyBq4Dm"}
```

**Reachability summary**:
- 5/5 HTTP 错误一致(全 403,无 200)→ 链路通,但服务端主动拒
- matched: **0/5 (0.0%)**
- 总 tokens: 0 (403 无 usage 返回)
- 总 latency: 1954 ms
- 平均 latency: 390 ms / cell(403 网络往返,比 no-proxy 的 780ms 快 ~50% — proxy 路径延迟更低)
- user_id 在响应中暴露: `user_3J7P6ghveKjYjvgV8u3JEyBq4Dm`(审计用,非敏感)

---

## §4 Step 1 + Step 2 验证记录

### §4.1 Step 1: Proxy 出口 IP 验证

| 验证服务 | 出口 country | 状态 |
|---|---|---|
| ipinfo.io/json | ERR_HTTP_429(限流) | 跳过 |
| ipapi.co/json | **US** ✓ | 通过 |
| ifconfig.co/json | Brazil(异常,服务不可靠) | 弃用 |
| ip-api.com/json | **US** ✓ | 通过 |

**判定**: **PROXY_ACTIVE_EXIT_US_OK**(2/3 有效服务一致,ifconfig.co 已知不可靠)

### §4.2 Step 2: OpenRouter catalog 验证

| 项 | 结果 |
|---|---|
| HTTP 状态 | **200 OK** |
| Models 数量 | 436 |
| `openai/gpt-6-astra` | ✅ 存在 |
| `openai/gpt-6-astra:batch` | ✅ 存在 |
| `openai/gpt-6-astra-pro` | ✅ 存在 |
| `openai/gpt-6-astra-pro:batch` | ✅ 存在 |

---

## §5 三组对比

| 场景 | 出口 region | 5 cells HTTP 200 | 5 cells matched | 错误类型 | 来源 |
|---|---|---|---|---|---|
| 无 proxy + GPT-6 | CN (Shanghai) | 0/5 | 0/5 | region gate (IP-level) | `results/deposon_gpt6_astra_smoke_2026_09_10.json` 14:37 |
| VPN 尝试(未生效) + GPT-6 | CN (Shanghai) | 0/5 | 0/5 | BLOCKED(无 chat completions) | `results/deposon_gpt6_vpn_smoke_2026_09_10.json` 14:53 |
| **Proxy 7897(本次)** | **US** ✓ | 0/5 | 0/5 | **TOS/abuse gate(account-level)** | 本次报告 |

**核心结论**:
- Proxy 解决了 **layer 1: region gate**
- 但暴露 **layer 2: account-level TOS gate** — 这超出 worker scope,需 user 在 OpenRouter 平台层面处理
- 即便 user 切到 "干净 US 住宅 IP"(非 datacenter 加速器) + billing 真实 US 卡,仍可能命中同 gate(若 OpenRouter 已对 user_id 标记)

---

## §6 关键诚实声明

1. **proxy 隔离严格**:
   - 整个 Python worker 进程通过 `os.environ` 临时注入 `HTTP_PROXY` / `HTTPS_PROXY=http://127.0.0.1:7897`(同时小写变体)
   - user 本机系统代理 / 注册表 / 浏览器 / 网络设置 **完全未触碰**
   - 进程退出后 env 变量自动消失,无任何系统级副作用

2. **key 永不入任何文件**:
   - `auth` 字段仅 `sk-or-v1-...` 截断占位 + "loaded from env"
   - 真实 key 仅在 `os.environ['OPENROUTER_API_KEY']` 进程内存
   - 工具脚本 `tools/gpt6_proxy_smoke.py` 不写 key 字面值,只从 env 读

3. **IP 字面值未记录**:
   - Step 1 验证只取 `country` 字段(US/CN),未保存 `ip` / `city` 字面值
   - JSON 中 `request_exit_region` 仅记 "US (verified via ipapi.co + ip-api.com)",无 IP

4. **5 cells 严格**:
   - 仅 1 个 GET /models(Step 2)+ 5 个 POST chat/completions(Step 3)= **共 6 个 HTTP call**
   - 0 重试 / 0 model 切换 / 0 endpoint 切换
   - 0 个其他 API 干扰

5. **诚实 self-disclosure — 错误类型变化**:
   - **预期**: proxy 改出口 US → region gate 解除 → 5/5 HTTP 200
   - **实际**: proxy 改出口 US → region gate 解除(✓)→ 但**新的** TOS gate 拦截(0/5 HTTP 200)
   - 这不是 worker 错误,是 **OpenRouter 端的双层 gate 设计**(IP + account),layer 1 由 worker 可控,layer 2 需 user 在 OpenRouter 平台申诉/换账户
   - 如实记录,不掩盖 layer 2 失败,也不强行跑超出 5 cells 的额外测试

6. **本次任务部分成功**:
   - ✅ Proxy 隔离方案技术验证通过(无副作用、不动 user 本机)
   - ✅ 出口 IP 验证链路可复用(以后所有走 proxy 的 LLM 测试都可用此 step1)
   - ✅ OpenRouter 端 region gate 可被 proxy 绕过(理论验证通过)
   - ❌ GPT-6 实际可用性仍 BLOCK(但原因从 IP gate 升级为 account gate,需 user 端处置)

---

## §7 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | API key runtime 读 + 永不入 prompt / JSON / 落盘 | ✅ 从 `LLM API.txt` GB18030 读出后立即 `os.environ['OPENROUTER_API_KEY']=...`;`auth` 字段仅 `sk-or-v1-...` 截断;`tools/gpt6_proxy_smoke.py` 不含 key 字面值 |
| 2 | proxy 隔离沙箱(不动 user 本机) | ✅ 仅本 worker 进程 `os.environ` 临时设;系统代理 / 注册表 / 浏览器代理 / 网络设置全未改 |
| 3 | 5 cells mini test 限制 | ✅ 严格 1 GET /models + 5 POST chat/completions,无重试 / 切 model / 切 endpoint |
| 4 | 不动 5 锚 JSON `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | ✅ 未读取 / 未修改 |
| 5 | 不动 4 SPEC V0.1 冻结版 | ✅ 未读取 / 未修改 |
| 6 | 不动 v19 frozen JSON | ✅ 未读取 / 未修改 |
| 7 | 结果落盘(审计用,不含 key / IP) | ✅ 写入 `results/deposon_gpt6_proxy_smoke_2026_09_10.json` + 本报告;`request_exit_region` 仅记 country code,无 IP 字面值 |

---

## §8 下一步建议(给 user 决策)

| 触发条件 | 建议 |
|---|---|
| **layer 1 region gate 已确认可绕过**(本次结果) | 路径技术 OK,可在 proxy 之上做其他 LLM 模型测试(海外开源 model 等) |
| **layer 2 TOS gate 需 user 端处置** | 建议 user 在 OpenRouter 后台: (a) 检查 account 状态/是否有 abuse 标记;(b) 考虑用真实 US 住宅 IP(非加速器 datacenter IP) + 真实 US 信用卡;(c) 或换 OpenRouter 账户 / 改用其他 LLM gateway |
| **本次 proxy 步骤仍可复用** | 即便 GPT-6 仍 fail,proxy 工具链(`tools/proxy_step1_exit_region.py` + `tools/gpt6_proxy_smoke.py` 的 proxy 设置)可复用于其他需要 US 出口的 LLM 测试 |
| **不建议** | (a) 继续硬试 GPT-6 — 0/5 已稳定可复现,5 cells budget 严格遵守;(b) 切到 gpt-6-astra:batch — 同样会命中 TOS gate(若 account-level flag 已挂) |

---

## §9 文件清单

- 结果 JSON: `D:\私人资料\deposon-repo\results\deposon_gpt6_proxy_smoke_2026_09_10.json` (~6 KB,5 cells + step2 catalog + step1 verdict)
- Step 1 验证: `D:\私人资料\deposon-repo\results\deposon_gpt6_proxy_step1_2026_09_10.json` (proxy 出口 US 验证)
- Step 1 脚本: `D:\私人资料\deposon-repo\tools\proxy_step1_exit_region.py`
- 主 smoke 脚本: `D:\私人资料\deposon-repo\tools\gpt6_proxy_smoke.py`
- 交付报告: `D:\私人资料\deposon-repo\docs\V3X\GPT6_PROXY_SMOKE_2026_09_10.md` (本文件)
- **未创建任何含完整 key 或 IP 字面值的文件**

---

**Worker handoff**: 任务 A 闭环(部分成功)。Layer 1 region gate 已通过 proxy 验证可绕过,Layer 2 TOS gate 需 user 在 OpenRouter 平台层面处置。本次诚实记录新发现的 account-level gate 现象,提供给父 agent 决策依据。
