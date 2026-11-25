/**
 * client.ts — OpenRouter 接入面（官方 SDK @openrouter/sdk）。
 *
 * 纪律：
 *   1) key 只从环境变量 OPENROUTER_API_KEY 读（loadApiKey）；未设 ⇒ 抛 MissingApiKeyError 并给出建 key 地址；
 *      key 不进日志、不进报文摘要、不进任何落盘件（scrub 兜底）。
 *   2) 不读请求体再转发：追踪钩子只读「方法 / 路径 / 响应头」，请求与响应体原样交给 SDK
 *      （读体后再转发 ＝ Request 已被消费，SDK 侧会报 Connection error —— 那是探针缺陷冒充的网络读数）。
 *   3) 缺省不重试（retries="none"）：一次调用＝一个请求，诊断读数才可逐例对表。
 */

import { HTTPClient, OpenRouter } from "@openrouter/sdk";
import { MissingApiKeyError } from "./errors.js";

export {
  classifyFailure,
  EXIT,
  KEY_HELP_URL,
  MissingApiKeyError,
  relayRefused,
  scrub,
} from "./errors.js";
export type { Failure, FailureKind } from "./errors.js";

/**
 * 预登记载体：开源（MIT）· 官网模型广场在架（选型规则与证据见 README「载体」段）。
 * 只许用 --model 参数覆盖；改这里的缺省＝改码＝新轮号。
 */
export const DEFAULT_MODEL = "xiaomi/mimo-v2.6-flash-mopd";

export type Fetcher = (req: Request) => Promise<Response>;

/** 每个出站请求的元数据（不含请求头、不含请求体、不含响应体） */
export interface TraceRecord {
  method: string;
  path: string;
  status: number;
  ms: number;
  release: string | null;
  ray: string | null;
}

export interface GatewayOptions {
  apiKey: string;
  /** 注入点：测试替身或自定义 fetch；缺省用全局 fetch */
  fetcher?: Fetcher;
  /** 单请求超时（毫秒） */
  timeoutMs?: number;
  /** 缺省 "none"；"backoff" 交给 SDK 的退避重试（连接错误也重试） */
  retries?: "none" | "backoff";
  /** 追踪回调（只收元数据） */
  onTrace?: (trace: TraceRecord) => void;
}

/** 从环境变量读 key；未设或为空 ⇒ MissingApiKeyError（提示去官网建 key） */
export function loadApiKey(env: NodeJS.ProcessEnv = process.env): string {
  const key = (env.OPENROUTER_API_KEY ?? "").trim();
  if (!key) throw new MissingApiKeyError();
  return key;
}

function tracingFetcher(next: Fetcher, onTrace?: (trace: TraceRecord) => void): Fetcher {
  return async (req: Request): Promise<Response> => {
    const t0 = Date.now();
    const res = await next(req);
    if (onTrace) {
      onTrace({
        method: req.method,
        path: new URL(req.url).pathname,
        status: res.status,
        ms: Date.now() - t0,
        release: res.headers.get("x-openrouter-release"),
        ray: res.headers.get("cf-ray"),
      });
    }
    return res;
  };
}

export function createClient(options: GatewayOptions): OpenRouter {
  const base: Fetcher = options.fetcher ?? ((req) => fetch(req));
  return new OpenRouter({
    apiKey: options.apiKey,
    httpClient: new HTTPClient({ fetcher: tracingFetcher(base, options.onTrace) }),
    timeoutMs: options.timeoutMs ?? 30_000,
    retryConfig:
      (options.retries ?? "none") === "none"
        ? { strategy: "none" }
        : { strategy: "backoff", retryConnectionErrors: true },
  });
}

function finite(value: unknown): number | null {
  return typeof value === "number" && Number.isFinite(value) ? value : null;
}

/** 读路径体检：GET /credits（读路径在 CN 出口实测 200）。SDK 1.5.139 的结构是 {data:{totalCredits,totalUsage}}（美元计）。 */
export interface CreditSnapshot {
  totalCredits: number | null;
  totalUsage: number | null;
}

export async function readHealth(client: OpenRouter): Promise<CreditSnapshot> {
  const res = await client.credits.getCredits();
  const data = (res?.data ?? {}) as Record<string, unknown>;
  return {
    totalCredits: finite(data.totalCredits ?? data.total_credits),
    totalUsage: finite(data.totalUsage ?? data.total_usage),
  };
}

export interface ChatRequestSpec {
  model: string;
  prompt: string;
  maxTokens?: number;
}

export interface ChatOutcome {
  model: string;
  returnedModel: string | null;
  text: string;
  promptTokens: number | null;
  completionTokens: number | null;
  latencyMs: number;
  responseId: string | null;
}

/** 一次生成请求：POST /chat/completions（messages 只放一条 user；maxTokens 缺省 16） */
export async function chatOnce(client: OpenRouter, spec: ChatRequestSpec): Promise<ChatOutcome> {
  const t0 = Date.now();
  const res = await client.chat.send({
    chatRequest: {
      model: spec.model,
      messages: [{ role: "user", content: spec.prompt }],
      maxTokens: spec.maxTokens ?? 16,
    },
  });
  const choice = (res?.choices?.[0] ?? {}) as { message?: { content?: unknown } };
  const usage = (res?.usage ?? {}) as Record<string, unknown>;
  return {
    model: spec.model,
    returnedModel: typeof res?.model === "string" ? res.model : null,
    text: typeof choice.message?.content === "string" ? choice.message.content : "",
    promptTokens: finite(usage.prompt_tokens ?? usage.promptTokens),
    completionTokens: finite(usage.completion_tokens ?? usage.completionTokens),
    latencyMs: Date.now() - t0,
    responseId: typeof res?.id === "string" ? res.id : null,
  };
}
