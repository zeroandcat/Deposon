# GPT-6 VPN 接入烟雾测试报告 (2026-09-10)

**任务 ID**: VPN+GPT-6 5 cells mini test
**时间**: 2026-09-10 14:53:45+08:00
**结果**: **FAIL — VPN 出口 IP 实际仍在 CN (Shanghai),未生效**

---

## §1 测试环境

| 项 | 值 |
|---|---|
| 模型 | `openai/gpt-6-astra` |
| 网关 | OpenRouter (`https://openrouter.ai/api/v1/chat/completions`) |
| 5 cells | GSM8K id 1-5 from `results/deposon_benchmark_v1_4_gsm8k_details.json` |
| 出口 IP 实际 region | **CN (Shanghai)** ← 期望 US |
| 出口 IP 字面值 | **未记录(只记 country code)** |
| /models catalog 状态 | 200 (436 模型;gpt-6 系列 4 个:`openai/gpt-6-astra` / `:batch` / `-pro` / `-pro:batch`) |
| Temperature | 0.0 |
| max_tokens | 256 |
| prompt 模板 | `Question: {question}\nAnswer in one number:` |

**VPN 状态**: `inactive` (按 `ipinfo.io/json` 的 `country` 字段判定)

---

## §2 5 cells 结果

| cell | task | expected | predicted | match | http | error |
|---|---|---|---|---|---|---|
| 1 | gsm8k | 18.0 | — | ✗ | 0 | BLOCKED: exit country=CN (not US), VPN not active; per task spec do not retry |
| 2 | gsm8k | 5.0  | — | ✗ | 0 | BLOCKED: exit country=CN (not US), VPN not active; per task spec do not retry |
| 3 | gsm8k | 40.0 | — | ✗ | 0 | BLOCKED: exit country=CN (not US), VPN not active; per task spec do not retry |
| 4 | gsm8k | 1430.0 | — | ✗ | 0 | BLOCKED: exit country=CN (not US), VPN not active; per task spec do not retry |
| 5 | gsm8k | 36.0 | — | ✗ | 0 | BLOCKED: exit country=CN (not US), VPN not active; per task spec do not retry |

**全部 0/5 命中**。**0 chat completions 被发起**(按 7 铁律 #3,不重试、不切 model,CN 出口下阻断以避免 region gate 403 噪声)。

---

## §3 三组对比

| 场景 | 出口 region | 5 cells | 来源 |
|---|---|---|---|
| 无 VPN + GPT-6 | CN (Shanghai) | 0/5 (全 403 region gate) | `results/deposon_gpt6_astra_smoke_2026_09_10.json` (2026-09-10T14:37) |
| 无 VPN + Llama 3.3 70B | (待补) | K/5 | 另一 worker `bg_a5f54e9e` |
| **有 VPN + GPT-6 (本次)** | **CN (Shanghai)** | **0/5 (BLOCKED)** | 本次报告;VPN 未生效,未发起 chat completion |

**核心结论**: 本次未能验证 "VPN 改 US 出口 → GPT-6 可调通" 这个假设链。**VPN 实际没生效**,所以无法判别 region gate 是否能通过。

---

## §4 关键诚实声明

1. **接入测试 ≠ 完整判死**: 本任务只验证 OpenRouter + GPT-6 + VPN 接入可达性,即使 5/5 通过也只是"能调",不等同于 P-A/B/C/D 任一方向的判死结论。
2. **VPN 由 user 在 OS 层处理,worker 进程继承**: worker 子进程(`mvs_7a82862a...`)启动时继承 OS 网络栈,如果 user 在自己桌面已连 VPN,worker 应继承同一出口。但本次检测到出口是 Shanghai,说明:
   - 可能 (a) user 当前实际并未连 VPN(配置了但没启动),
   - 或 (b) VPN 客户端在后台但路由规则没生效(需要全局/全局代理模式),
   - 或 (c) worker 进程启动瞬间的快照与 user 当前状态不一致(系统级 VPN 通常全局继承,但应用级 / 浏览器代理不会)。
   - **本 worker 没有做"先停 user VPN 再让 user 重连"这种带副作用的步骤,只做了 1 次 ipinfo.io 检测后即按 spec 停**。
3. **key 永不入任何文件**:
   - `auth` 字段仅写 `sk-or-v1-...` 截断占位 + "loaded from env"
   - 真实 key 仅在 `os.environ` 内驻留于 worker 进程内存,进程退出即消失
   - `LLM API.txt` (GB18030 源文件) 未被复制、引用或转储
4. **IP 字面值未记录**: 全程只取 `country` 字段("US"/"CN"),未保存 `ip` 字段。
5. **数据修正**: 任务 spec 提到 key 在 `C:\Users\Administrator\Desktop\AI\新建文本文档.txt`,但**该文件实际不存在**,key 实际在 `LLM API.txt` (327 字节 GB18030,内含 4 个键:火山 agent-plan / 火山 coding-plan / OpenRouter / VPN 订阅 URL)。本次从 `LLM API.txt` 提取。

---

## §5 7 铁律自检

| # | 铁律 | 状态 |
|---|---|---|
| 1 | OpenRouter key runtime 读,`os.environ` | ✅ 从 `LLM API.txt` GB18030 读出后立即 `os.environ['OPENROUTER_API_KEY']=...`,本地变量 `del` |
| 2 | key / VPN config 永不入 prompt / JSON / 落盘 | ✅ JSON 中仅 `sk-or-v1-...` 截断占位;`auth` 字段元注释;VPN 订阅 URL 全程未引用 |
| 3 | 5 cells mini test 限制(不重试 / 不切 model) | ✅ VPN 失效即停,0 chat completions 发起;未切模型;未重试 |
| 4 | 不动 5 锚 JSON | ✅ 未访问 `verifier/handoff/KT_ABC1_anchors_sha256_12.json` |
| 5 | 不动 4 SPEC V0.1 冻结版 | ✅ 未访问 `docs/V3X/KT_?1_SPEC_V0.1.md` |
| 6 | 不动 v19 frozen JSON | ✅ 未访问 `results/deposon_v19_benchmark_fixes.json` |
| 7 | 结果落盘 | ✅ 写入 `results/deposon_gpt6_vpn_smoke_2026_09_10.json` + 本 md |

**额外自检**: 仅调了 2 个验证接口 (`ipinfo.io/json` 1 次 + `openrouter.ai/api/v1/models` 1 次) + 0 次 chat completion,**未发起任何"5 cells 之外"的额外 API**。

---

## §6 下一步建议(给 user)

**由于 VPN 未生效,核心问题在 user 端**,而不是 GPT-6 接入本身。需 user 检查:

1. **VPN 客户端状态**: 现在 desktop 上 VPN 客户端是否真的"已连接"(不是只启动了配置窗口,而是 tunnel 已建)?
2. **路由模式**: 是全局模式还是分流模式?如果是分流,需要把 `api.openrouter.ai` 和 `ipinfo.io` 加入代理列表,或者直接切全局。
3. **system proxy vs TUN 模式**: 如果是 system proxy,Mavis 子进程可能没继承;如果是 TUN/全局网卡,会继承。请在 VPN 客户端选 TUN 或全局。
4. **Mavis 网络出口**: Mavis 父进程 / worker 子进程是否走 OS 默认路由?可重启 Mavis 让它重新读 OS 路由表。

**如果 user 修复 VPN 后重跑**: 重跑本任务(同 spec),预期:
- 出口 country=US ✓
- /models 200 + 4 个 gpt-6 模型 ✓
- 5 cells chat completion 200 + 数字抽取;若 5/5 → 跑 30 cells 边际验证;若 <5/5 → 单独看 cell 错误(MoE 路由 / 模型拒答 / token 截断 / 抽取误判)。
- 不必改任何代码,只需 user 端 VPN 真正生效后重跑同一脚本 `tools/gpt6_vpn_smoke.py`。

---

**签字**: Worker `mvs_7a82862a229d420dbbda178d29824f3b` · 报告时间 2026-09-10 14:55 +08:00
