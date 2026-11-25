/**
 * errors.ts — 失败分类（只看三样：HTTP 状态码 / 响应体报文特征 / SDK 客户端错误类；不吞错、不猜因）。
 *
 * 分类口径（与 2026-11-25 实测逐项对表，见 README「实测读数」段）：
 *   401                AUTH                  —— key 无效/未带（路径可达、鉴权在前）
 *   400 +「cannot be relayed」 GATEWAY_RELAY_REFUSED —— 网关拒中继（发生在读模型名之前；error-origin=client）
 *   400（其它）        BAD_REQUEST           —— 请求参数错（未知 slug、字段非法等）
 *   404 / 402 / 403    NOT_FOUND / PAYMENT / FORBIDDEN
 *   429                RATE_LIMITED（可重试）
 *   408 / 5xx          SERVER_ERROR（可重试）
 *   连接失败 / 超时 / 中止  NETWORK（可重试）
 *   其余（SDK 用法错、校验错）CLIENT_ERROR
 */

export type FailureKind =
  | "MISSING_API_KEY"
  | "AUTH"
  | "PAYMENT"
  | "FORBIDDEN"
  | "GATEWAY_RELAY_REFUSED"
  | "BAD_REQUEST"
  | "NOT_FOUND"
  | "RATE_LIMITED"
  | "SERVER_ERROR"
  | "NETWORK"
  | "CLIENT_ERROR";

/** 进程退出码：调用方与 CI 只认这个 */
export const EXIT = {
  OK: 0,
  RELAY_REFUSED: 1,
  API_ERROR: 2,
  MISSING_KEY: 3,
  NETWORK: 4,
  CLIENT_ERROR: 5,
} as const;

/** key 未设时的唯一提示口径 */
export const KEY_HELP_URL = "https://openrouter.ai/keys";

/** 网关「拒中继」报文特征（只在 400 上认） */
const RELAY_MARKERS = ["cannot be relayed"];

const NETWORK_ERROR_NAMES = ["ConnectionError", "RequestTimeoutError", "RequestAbortedError"];

export interface Failure {
  kind: FailureKind;
  httpStatus: number | null;
  retryable: boolean;
  exitCode: number;
  /** 服务端给的错误文案（已脱敏：不含 key） */
  message: string;
  /** 响应头 x-openrouter-release（网关构建号；拒中继例带此头，鉴权失败例不带） */
  release: string | null;
  /** 响应体 error.metadata.raw 里的 error-origin（拒中继例为 "client"） */
  errorOrigin: string | null;
  /** 截断后的原始响应体（排障用；已脱敏） */
  errorBody: string | null;
}

export class MissingApiKeyError extends Error {
  readonly kind = "MISSING_API_KEY" as const;
  readonly exitCode: number = EXIT.MISSING_KEY;
  constructor() {
    super(
      `OPENROUTER_API_KEY is not set. Create a key at ${KEY_HELP_URL} and export it in your shell; never commit it.`,
    );
    this.name = "MissingApiKeyError";
  }
}

/** 诊断文字脱敏：key 中段一旦出现一律替换 */
export function scrub(text: string, secret?: string): string {
  let out = text;
  if (secret && secret.length >= 8) out = out.split(secret).join("<REDACTED>");
  return out.replace(/sk-or-v1-[A-Za-z0-9]{8,}/g, "<REDACTED>");
}

function nameOf(err: unknown): string {
  return typeof err === "object" && err !== null && typeof (err as { name?: unknown }).name === "string"
    ? (err as { name: string }).name
    : "";
}

/** 结构判别（不依赖 instanceof：防双包装载时类不一致） */
function isHttpError(err: unknown): err is { statusCode: number; body: string; headers?: { get(name: string): string | null } } {
  return (
    typeof err === "object" &&
    err !== null &&
    typeof (err as { statusCode?: unknown }).statusCode === "number" &&
    typeof (err as { body?: unknown }).body === "string"
  );
}

export function relayRefused(status: number | null, body: string): boolean {
  if (status !== 400) return false;
  const text = body.toLowerCase();
  return RELAY_MARKERS.some((marker) => text.includes(marker));
}

interface ParsedError {
  message: string;
  code: string | null;
  origin: string | null;
}

function parseErrorBody(body: string): ParsedError {
  try {
    const json = JSON.parse(body) as {
      error?: { message?: unknown; code?: unknown; metadata?: { raw?: unknown } };
    };
    let origin: string | null = null;
    const raw = json?.error?.metadata?.raw;
    if (typeof raw === "string") {
      try {
        const inner = JSON.parse(raw) as Record<string, unknown>;
        if (typeof inner["error-origin"] === "string") origin = inner["error-origin"];
      } catch {
        // raw 不是 JSON：按无 origin 处理
      }
    }
    return {
      message: typeof json?.error?.message === "string" ? json.error.message : body.slice(0, 300),
      code: json?.error?.code == null ? null : String(json.error.code),
      origin,
    };
  } catch {
    return { message: body.slice(0, 300), code: null, origin: null };
  }
}

function truncate(text: string, max = 600): string {
  return text.length > max ? `${text.slice(0, max)}…` : text;
}

function byStatus(status: number, relayed: boolean): { kind: FailureKind; retryable: boolean; exitCode: number } {
  if (relayed) return { kind: "GATEWAY_RELAY_REFUSED", retryable: false, exitCode: EXIT.RELAY_REFUSED };
  if (status === 401) return { kind: "AUTH", retryable: false, exitCode: EXIT.API_ERROR };
  if (status === 402) return { kind: "PAYMENT", retryable: false, exitCode: EXIT.API_ERROR };
  if (status === 403) return { kind: "FORBIDDEN", retryable: false, exitCode: EXIT.API_ERROR };
  if (status === 404) return { kind: "NOT_FOUND", retryable: false, exitCode: EXIT.API_ERROR };
  if (status === 429) return { kind: "RATE_LIMITED", retryable: true, exitCode: EXIT.API_ERROR };
  if (status === 408 || status >= 500) return { kind: "SERVER_ERROR", retryable: true, exitCode: EXIT.API_ERROR };
  if (status >= 400 && status < 500) return { kind: "BAD_REQUEST", retryable: false, exitCode: EXIT.API_ERROR };
  return { kind: "CLIENT_ERROR", retryable: false, exitCode: EXIT.CLIENT_ERROR };
}

/** 把任何抛出物归到 Failure（永不抛出） */
export function classifyFailure(err: unknown, apiKey?: string): Failure {
  const none = { release: null, errorOrigin: null, errorBody: null } as const;
  if (err instanceof MissingApiKeyError || nameOf(err) === "MissingApiKeyError") {
    return {
      kind: "MISSING_API_KEY",
      httpStatus: null,
      retryable: false,
      exitCode: EXIT.MISSING_KEY,
      message: scrub(err instanceof Error ? err.message : String(err), apiKey),
      ...none,
    };
  }
  if (isHttpError(err)) {
    const parsed = parseErrorBody(err.body);
    const relayed = relayRefused(err.statusCode, err.body);
    const mapped = byStatus(err.statusCode, relayed);
    const release = err.headers?.get("x-openrouter-release") ?? null;
    // error-origin 实测在响应头 x-openrouter-error-origin（报文体的 metadata.raw 里可以没有）；头优先、体兜底
    const originHeader = err.headers?.get("x-openrouter-error-origin") ?? null;
    return {
      kind: mapped.kind,
      httpStatus: err.statusCode,
      retryable: mapped.retryable,
      exitCode: mapped.exitCode,
      message: `${scrub(parsed.message, apiKey)}${parsed.code ? ` [code ${parsed.code}]` : ""}`,
      release,
      errorOrigin: originHeader ?? parsed.origin,
      errorBody: scrub(truncate(err.body), apiKey),
    };
  }
  if (NETWORK_ERROR_NAMES.includes(nameOf(err))) {
    return {
      kind: "NETWORK",
      httpStatus: null,
      retryable: true,
      exitCode: EXIT.NETWORK,
      message: scrub(err instanceof Error ? err.message : String(err), apiKey),
      ...none,
    };
  }
  return {
    kind: "CLIENT_ERROR",
    httpStatus: null,
    retryable: false,
    exitCode: EXIT.CLIENT_ERROR,
    message: scrub(err instanceof Error ? `${err.name}: ${err.message}` : String(err), apiKey),
    ...none,
  };
}
