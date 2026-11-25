# OpenRouter 接入子包（`@deposon/openrouter-gateway`）

把 OpenRouter 接到本项目（`dsh-plugin-deposon`）的**新增**子包：官方 SDK `@openrouter/sdk`（TypeScript / Node ≥ 22），key 只从环境变量 `OPENROUTER_API_KEY` 读，失败按类型分类并给出退出码。

- 位置：`openrouter/`，自带 `package.json`；**已验代码 0 改**（主包 `package.json`、`plugin/`、`harness/`、`mcp/`、`gates/` 未动）。
- 并入主包（把本子包加进主 `package.json` 的 `dependencies` / `files`）是 PI 的一行决定，本子包不替裁。
- 依赖锁定：`@openrouter/sdk` 钉 `1.5.139`；`package-lock.json` 随仓；`typescript` / `@types/node` 只在 devDependencies。

## 目录

```
openrouter/
├─ package.json / package-lock.json / tsconfig.json / .gitignore
├─ src/
│  ├─ errors.ts        失败分类（classifyFailure·退出码·脱敏）
│  ├─ client.ts        接入面（loadApiKey·createClient·readHealth·chatOnce）
│  ├─ e2e.ts           端到端一条请求（CLI）
│  └─ gateway.test.ts  替身测试（0 网络·fetch 全注入）
├─ dist/               tsc 产物（不进仓）
└─ README.md
```

## 怎么装

```bash
cd openrouter
npm ci            # 按 package-lock.json 装（实测 npm 11.16 / Node 24.18；装约 10 s）
npm run build     # tsc → dist/
npm test          # node --test dist/gateway.test.js（8 条替身用例）
```

## 怎么设 key

key 只走环境变量，**不写文件、不进命令行参数、不提交**：

```bash
export OPENROUTER_API_KEY="<你的 key>"      # 没有就去 https://openrouter.ai/keys 创建
```

未设时 `loadApiKey()` 抛 `MissingApiKeyError`，CLI 打印建 key 地址并以退出码 3 结束，不发起任何请求。

## 怎么跑

```bash
npm run e2e                                            # 缺省载体·缺省提示词
node dist/e2e.js --model <slug> --prompt "你好" --max-tokens 32
```

每步输出一行 JSON（不含 key），末行是人读的结论：

1. **读路径体检**：`GET /api/v1/credits`（验证 key 与出口可达）；
2. **一次生成**：`POST /api/v1/chat/completions`（`messages` 一条 user；`maxTokens` 缺省 16；缺省不重试）。

| 退出码 | 含义 | 对应分类 |
|---:|---|---|
| 0 | 生成请求走通 | — |
| 1 | 网关拒中继 | `GATEWAY_RELAY_REFUSED`（400 且报文含 `cannot be relayed`） |
| 2 | 其它 API 错 | `AUTH`(401) / `PAYMENT`(402) / `FORBIDDEN`(403) / `BAD_REQUEST`(400·404·413) / `RATE_LIMITED`(429) / `SERVER_ERROR`(408·5xx) |
| 3 | 未设 key | `MISSING_API_KEY` |
| 4 | 网络 | `NETWORK`（连接失败 / 超时 / 中止） |
| 5 | 客户端用法错 | `CLIENT_ERROR` |

诊断字段随失败一起给出：`httpStatus`、`release`（响应头 `x-openrouter-release`）、`errorOrigin`（响应头 `x-openrouter-error-origin`）、`message`、`errorBody`（截断）。实测**鉴权失败（401）不带 release 头、拒中继（400）带 release 头**，这是两者的判别位。

在代码里调用：

```ts
import { chatOnce, createClient, classifyFailure, loadApiKey } from "./client.js";

const client = createClient({ apiKey: loadApiKey(), retries: "backoff" }); // 生产建议开退避重试
try {
  const out = await chatOnce(client, { model: "xiaomi/mimo-v2.6-flash-mopd", prompt: "ping" });
  console.log(out.text, out.completionTokens, out.latencyMs);
} catch (err) {
  const f = classifyFailure(err);        // 永不抛出；f.kind / f.exitCode / f.retryable
}
```

## 载体（按 slug 选型）

| 项 | 内容 |
|---|---|
| 缺省 slug | `xiaomi/mimo-v2.6-flash-mopd`（`DEFAULT_MODEL`，只许用 `--model` 覆盖） |
| 许可 | **MIT**——模型卡 `cardData.license`、`LICENSE` 原文、README 三源一致（11-25 11:2x 经模型枢纽镜像站读取；非 gated） |
| 发布日 | 2026-11-23（官网模型页「Released」；接口 `created=1795456634` 仅作对照） |
| 在架证据 | 官网模型页 11-25 **13:03（平台侧渲染，刷新帧；12:45 首帧同）**：在列·1 个供应商（Featherless）·近 3 天可用率 100%／可服务率 95.71%；Endpoints API 12:45:34：`status 0`。页面渲染文本不显示许可字段，许可名取自模型卡三源 |
| 闭源排除 | 用户示例 `anthropic/claude-opus-5.5` 属闭源，按「闭源一律排除」不选 |

「在架」以官网模型广场 / 模型页为准，接口返回值只作对照。

## 实测读数（11-25·本席沙箱出口 loc=CN）

| 时刻 | 条件 | 读路径 `GET /credits` | 生成 `POST /chat/completions` | 退出码 |
|---|---|---|---|---:|
| 12:41:04 | 未设 key | —（不发请求） | —（不发请求） | 3 |
| 12:41:05 | 错 key | 传输层抖动 `fetch failed` → `NETWORK` | **401** `User not found.` → `AUTH`（无 release 头） | 2 |
| 12:41:08 | 真 key | **200**（`total_credits` / `total_usage` 两字段读回·659 ms） | **400** `Request path cannot be relayed` → `GATEWAY_RELAY_REFUSED`（release `api;3e05b712-d9f7-4400-993a-7cb63338fd89`·error-origin `client`·cf-ray LAX·244 ms） | 1 |
| 12:42:40 | 错 key（复跑） | **401** `User not found.` → `AUTH` | 传输层抖动 `fetch failed` → `NETWORK` | 4 |
| 12:42:43 | 真 key（复跑） | 传输层抖动 `fetch failed` → `NETWORK` | **400** 同上（release 同·error-origin `client`·1093 ms） | 1 |
| 13:03:57–13:04:01 | 三条件再复跑（key 取自值守进程环境·0 落盘） | 未设：不发请求；错 key：`fetch failed` → `NETWORK`；真 key：**200**（20 / 11.313·958 ms） | 错 key：**401** `User not found.` → `AUTH`；真 key：**400** 同上（release 同·error-origin `client`·cf-ray LAX·321 ms） | 3／2／1 |
| 13:29:38–13:29:53 | GLM 系诊断（沙箱·AS37963 阿里云北京·httpx 直连）：`GET /credits`／无鉴权／`z-ai/glm-5.3`×2／mimo×2／`z-ai/glm-agentmore`（广场无此 slug）×2 | **200**（20 / 11.313·814 ms） | 无鉴权 **401**；带鉴权 6 例**全 400** 同报文（release 同·error-origin `client`·PoP LAX·240–297 ms·响应体 sha256 逐位相同） | — |
| 13:35:44–13:35:50 | 服务器出口复证（41995·AS4837 联通·同一把 key·urllib 直连·用户令「已开机，即试即关」） | **200**（20 / 11.313·872 ms） | 无鉴权 **401**；带鉴权 4 例（mimo×2／`glm-5.3`／`glm-agentmore`）**全 400** 同报文（release 同·error-origin `client`·PoP LAX·672–1779 ms） | — |

- **结论：生成路径在 CN 出口被网关拒中继（BLOCKED），与 11-25 全天各轮逐字相同；读路径通。** 不填估值。
- 两台 GPU 服务器出口同为 CN（见交付包盘点表）；**13:35 已在 41995（AS4837 联通·呼和浩特·与沙箱不同 ASN 不同 IP）用同一把 key 复证**：读 200／生成 400，与沙箱逐位相同 ⇒ 拒绝跟的是「CN 出口」这个属性，**不是 AgentMore 工作区网关、不是模型、不是账户**（不存在的 slug 同报文 ⇒ 拒中继发生在读模型名之前）。未分辨的只剩「按 loc=CN 地理规则」vs「逐个 ASN 封」，对项目等价。
- 传输层抖动：真/错 key 六轮共 12 个请求里 **4 个**遇 `TypeError: fetch failed`（SDK 归 `ConnectionError`·被本子包判 `NETWORK`）——本子包缺省 `retries: "none"` 是为诊断读数逐例可对表；**生产调用请设 `retries: "backoff"`**。
- 替身测试 8/8 通过（未设 key / 400 拒中继 / 400 其它 / 401·404·429 / 500·502·504 / 连接失败 / 200 解析 / 脱敏）。

## 打包归属（自择·用户 13:11 令·2026-11-25）

**不并入主包 `dependencies`，保持私有可选子包。** 理由：

1. 主包运行时（`plugin`／`gates`／`mcp`／`harness`）不 import 本子包；`harness/thermo_live_round.py` 走自己的 HTTP 路径——并入是纯增依赖、零功能收益。
2. 改主包 `package.json`／lock／`files` 即改已验包的 tarball 内容，按规矩要换轮号（preview.11）重做装出包实测；当前没有触发它的需求。
3. `@openrouter/sdk` 及其传递依赖会进每一次 `npx deposon-quickcheck` 的安装面，而生成路径在 CN 出口是 BLOCKED（上表）——把一条不通的路当成硬依赖发出去。
4. 转正条件（三条同时满足才做）：主包出现真实消费者 → 以 `optionalDependencies`／懒加载接入 → 换轮号＋装出包实测＋`THIRD_PARTY_NOTICES.md` 更新。

## 纪律

- key：0 落盘、0 回显、0 提交；诊断文字经 `scrub()` 兜底脱敏；`.gitignore` 挡 `.env` / `*.key`。
- 追踪钩子只读「方法 / 路径 / 响应头」，**不读请求体再转发**（读体后转发＝Request 已被消费，SDK 侧会报 Connection error，那是探针缺陷冒充的网络读数）。
- 改 `DEFAULT_MODEL` 的缺省＝改码＝新轮号；换载体走 `--model` 参数。
