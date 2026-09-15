# GPT-6 via TeamoRouter — 接入 smoke 测试报告

- **任务 ID**: `TEAMOROUTER-GPT6-001` (Mavis worker 派发)
- **时间**: 2026-09-10 16:48-16:50 CST
- **状态**: ❌ **BLOCKED at Step 1** — `api.teamorouter.com` 在本机不可达
- **判定**: 无法跑 5 cells,任务在 endpoint 验证阶段终止
- **配套 JSON**: `D:\私人资料\deposon-repo\results\deposon_gpt6_teamorouter_2026_09_10.json`

---

## §1 测试环境

| 项 | 值 |
|---|---|
| Gateway | TeamoRouter (国内第三方,带海外 endpoint) |
| base_url | `https://api.teamorouter.com/v1` (来自 dev.to 文章,worker 未做更改) |
| Auth | `sk-teamo-356b3...` (从 `C:\Users\Administrator\Desktop\AI\LLM API.txt` GB18030 提取,仅运行时注入 `os.environ`,未落盘) |
| Proxy | **无**(启动时显式 `os.environ.pop` 全部 `*_PROXY` 变量) |
| SDK | urllib(纯 stdlib,无第三方依赖) |
| 加速器 | 未启用(7897 端口已 ban 上游,本任务不依赖) |
| 计划 cell 数 | 5 (id 1-5 from `deposon_benchmark_v1_4_gsm8k_details.json`) |

---

## §2 TeamoRouter endpoint 验证 — DNS 异常 + TCP 不通

### 2.1 DNS 解析(关键异常)

| 域名 | 解析结果 | 备注 |
|---|---|---|
| `api.teamorouter.com` | `31.13.92.5` | ⚠️ 落在 Facebook IP 段 |
| `teamorouter.com` | `199.59.149.232` | 另一陌生段 |
| `www.teamorouter.com` | `31.13.75.5` | ⚠️ 同样 Facebook 段 |
| `api.openai.com` | `74.86.226.234` | 参考对照,正常 |

> **强异常信号**: `api.teamorouter.com` 和 `www.teamorouter.com` 都解析到 31.13.x.x — 该段为 Facebook 持有的 IP 段,**官方 AI gateway 几乎不可能落在该段**。最可能解释:
> 1. TeamoRouter 域名已失效/未续费,被抢注指向 Facebook CDN
> 2. dev.to 文章中此 base_url 已过期,TeamoRouter 换了新域名
> 3. 本地 DNS 解析被劫持(可能性低,因为 `api.openai.com` 正常)

### 2.2 TCP / HTTPS 测试

| 测试 | 结果 |
|---|---|
| `socket.create_connection(api.teamorouter.com, 443)` | ❌ `TimeoutError` (10s) |
| 重试 2 次 | ❌ 同样 timeout |
| `GET /v1/models` (Authorization Bearer +30s 超时) | ❌ `EXC` (urllib.urlopen 超时 21s) |
| `chat/completions` | ❌ 未尝试(Step 2 已无可用 model ID) |

### 2.3 结论

`https://api.teamorouter.com/v1` 在本机当前网络环境下**完全不可达**,且 DNS 解析结果指向 Facebook IP 段 — **强烈建议 user 在浏览器或带 proxy 的环境直接验证该 URL**,确认是:
- (a) base_url 已变更(可能 TeamoRouter 迁移了新域名)
- (b) 域名被抢注/下线
- (c) 本地运营商对该段 IP 屏蔽

---

## §3 5 cells 结果表

| cell | id | Q 预览 | gold | raw_answer | extracted | match | status | latency | finish |
|---|---|---|---|---|---|---|---|---|---|
| 1 | — | — | — | — | — | — | — | — | — |
| 2 | — | — | — | — | — | — | — | — | — |
| 3 | — | — | — | — | — | — | — | — | — |
| 4 | — | — | — | — | — | — | — | — | — |
| 5 | — | — | — | — | — | — | — | — | — |

> **未跑** — 因 Step 1 endpoint 不可达,Step 2 无 model ID 可选,Step 3 无 API 可调。

---

## §4 与 OpenRouter 4 路径对比

| 路径 | 结果 | 备注 |
|---|---|---|
| OpenRouter layer-1 (key 有效) | 0/20 全 403 | layer-2 user_id gate 锁 `user_3J7P6ghveKjYjvgV8u3JEyBq4Dm` |
| OpenRouter 换 key | 0/20 全 403 | 同 user_id gate,key 不影响 |
| OpenRouter 换 proxy | 0/20 全 403 | 同上 |
| OpenRouter 换 billing | 0/20 全 403 | 同上 |
| **TeamoRouter (本次)** | **0/5 (BLOCKED at Step 1)** | **base_url 不可达 + DNS 异常** |

### 4.1 根因假设

按可能性排序:
1. **dev.to 文章 base_url 已过期** — TeamoRouter 服务可能已迁移或下线,文档未更新
2. **域名被抢注** — 31.13.x.x Facebook 段 IP 强烈暗示域名过期后被他人占用
3. **本地网络层屏蔽** — 可能性次之(因为 DNS 能解析,但 TCP 丢包)

---

## §5 7 铁律自检

| # | 铁律 | 自检 | 备注 |
|---|---|---|---|
| 1 | TeamoRouter key runtime 读 LLM API.txt | ✅ PASS | GB18030 读 + regex `sk-teamo-[a-zA-Z0-9]+` 提取,运行时仅注入 `os.environ` |
| 2 | OpenRouter key 永不入 prompt | ✅ PASS | 本任务全程未触碰 OpenRouter key,任何日志/JSON/网络请求都仅含 TeamoRouter key 截断 `sk-teamo-356b3...` |
| 3 | 不设 proxy | ✅ PASS | 启动时 `os.environ.pop` 全部 `HTTP_PROXY/HTTPS_PROXY/all_proxy/NO_PROXY` 等 |
| 4 | key 永不入 prompt / JSON / 落盘 | ✅ PASS | JSON 中 `auth` 字段为 `sk-teamo-356b3...` 截断占位;literal key 仅在 Authorization header 传递 |
| 5 | 5 cells 严格,不切非 GPT-6 model | ✅ N/A | 因 Step 1 阻塞,未跑任何 cell,不存在 fallback 行为 |
| 6 | 不动 5 锚 JSON (`KT_ABC1_anchors_sha256_12.json`) | ✅ PASS | 本任务未读取/修改该文件 |
| 7 | 不动 4 SPEC V0.1 + v19 frozen + v21 frozen | ✅ PASS | 本任务未读取/修改任何 frozen JSON |

---

## §6 下一步建议(给 parent / user)

**任务本身已阻塞**,无法在本机推进。三个候选路径:

### 6.1 优先(user 必须介入)

让 **user 在浏览器直接访问** `https://api.teamorouter.com/v1/models`(在 `/v1/models` 之前应有文档/登录页):

- **如果浏览器也 404/超时** → TeamoRouter 服务/域名已失效,**该路径作废**,转 §6.2
- **如果浏览器能打开** → 可能是本机网络层问题(老猫加速器 ban 后无备用),但 base_url 本身有效,转 §6.3

### 6.2 若 TeamoRouter 失效 — 退回到 OpenRouter 4 路径剩余选项

| 选项 | 状态 | 备注 |
|---|---|---|
| 换账户 | 未尝试 | 需要 user 新 OpenRouter 账户 + key + 重新绑 user_id(可能也撞 layer-2 gate) |
| 放弃转开源 | 未尝试 | 不动 OpenRouter 账户,改用开源 LLM(Qwen / DeepSeek / Llama)做 V2 评估 |
| 自家模型 | 未尝试 | user 自训 / 私有部署,工作量大,不在 1 周判死范围 |

### 6.3 若 TeamoRouter 仍有效 — 重跑本次任务

- **修复 DNS 解析**(本机 hosts 绑定真实 IP,或换 DNS server 8.8.8.8 / 1.1.1.1)
- **worker 重新跑 5 cells**,输出最终 JSON
- 若 5 cells PASS (≥3/5 match),可继续:
  - **30 cells 边际验证**(V2 真实工作量的小样本)
  - **进入 V2 2 周正式评估**

### 6.4 不推荐

- 用任何 proxy 试 TeamoRouter — 老猫加速器 7897 已 ban 上游,临时切 proxy 不会让 base_url 突然变正常
- 改 base_url 为猜测的变体(如 `api.teamorouter.cn` / `teamorouter.com/v1`)— 没有文档依据,容易再撞同问题

---

## §7 结论

**TeamoRouter + GPT-6 接入 smoke 测试在 Step 1 阻塞**:
- ✅ 已按铁律约束安全执行(key 不落盘、不设 proxy、OpenRouter key 隔离、5 锚 + frozen JSON 未动)
- ❌ `https://api.teamorouter.com/v1` 在本机当前网络下**完全不可达**,DNS 解析到 Facebook IP 段(31.13.x.x),**强烈怀疑该 base_url 已失效/被抢注**
- ⏸ 任务已停在 Step 1,等待 user 验证 base_url 是否仍有效,或决定是否切换到其他 gateway

**未消耗 GPT-6 配额**(任何 API 调用都未发出),无外部成本。
