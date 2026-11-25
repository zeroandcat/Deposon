/**
 * gateway.test.ts — 失败分类与解析的替身测试（0 网络：fetch 全部注入替身）。
 * 运行：npm test  ＝ node --test dist/gateway.test.js
 */

import assert from "node:assert/strict";
import test from "node:test";

import { chatOnce, createClient, loadApiKey, readHealth, type Fetcher } from "./client.js";
import { classifyFailure, EXIT, relayRefused } from "./errors.js";

const RELAY_BODY = {
  error: {
    message: "Request path cannot be relayed",
    code: 400,
    metadata: { provider_name: null, raw: '{"error-origin":"client"}' },
  },
};

const OK_BODY = {
  id: "gen-test",
  model: "vendor/model-test",
  choices: [{ index: 0, message: { role: "assistant", content: "pong" }, finish_reason: "stop", logprobs: null }],
  created: 1,
  object: "chat.completion",
  system_fingerprint: "fp_test",
  usage: { prompt_tokens: 5, completion_tokens: 1, total_tokens: 6 },
};

function mockFetch(status: number, body: unknown, headers: Record<string, string> = { "x-openrouter-error-origin": "client" }): {
  fetcher: Fetcher;
  calls: Array<{ method: string; path: string }>;
} {
  const calls: Array<{ method: string; path: string }> = [];
  const fetcher: Fetcher = async (req) => {
    calls.push({ method: req.method, path: new URL(req.url).pathname });
    return new Response(JSON.stringify(body), {
      status,
      headers: { "content-type": "application/json", ...headers },
    });
  };
  return { fetcher, calls };
}

async function failureOf(status: number, body: unknown, headers?: Record<string, string>) {
  const { fetcher, calls } = mockFetch(status, body, headers);
  const client = createClient({ apiKey: "sk-or-v1-PLACEHOLDER00", fetcher });
  try {
    await chatOnce(client, { model: "vendor/model-test", prompt: "hi" });
  } catch (err) {
    return { failure: classifyFailure(err, "sk-or-v1-PLACEHOLDER00"), calls };
  }
  throw new Error("expected a failure");
}

test("未设 key ⇒ MissingApiKeyError（exit 3），不发起任何请求", () => {
  assert.throws(() => loadApiKey({}), /https:\/\/openrouter\.ai\/keys/);
  assert.throws(() => loadApiKey({ OPENROUTER_API_KEY: "   " }), /OPENROUTER_API_KEY is not set/);
  const f = classifyFailure(Object.assign(new Error("x"), { name: "MissingApiKeyError" }));
  assert.equal(f.exitCode, EXIT.MISSING_KEY);
});

test("400 + cannot be relayed ⇒ GATEWAY_RELAY_REFUSED（exit 1·记 release 与 error-origin）", async () => {
  const { failure, calls } = await failureOf(400, RELAY_BODY, { "x-openrouter-release": "api;test-build" });
  assert.equal(failure.kind, "GATEWAY_RELAY_REFUSED");
  assert.equal(failure.httpStatus, 400);
  assert.equal(failure.exitCode, EXIT.RELAY_REFUSED);
  assert.equal(failure.retryable, false);
  assert.equal(failure.release, "api;test-build");
  assert.equal(failure.errorOrigin, "client");
  assert.equal(failure.message, "Request path cannot be relayed [code 400]");
  assert.deepEqual(calls, [{ method: "POST", path: "/api/v1/chat/completions" }]);
  // 头优先：真实网关把 error-origin 放在响应头（报文体里可以没有 metadata）
  const hdr = await failureOf(400, { error: { message: "Request path cannot be relayed", code: 400 } }, { "x-openrouter-error-origin": "client", "x-openrouter-release": "api;hdr" });
  assert.equal(hdr.failure.errorOrigin, "client");
  assert.equal(hdr.failure.release, "api;hdr");
  assert.equal(hdr.failure.kind, "GATEWAY_RELAY_REFUSED");
});

test("400 其它 ⇒ BAD_REQUEST（不冒充拒中继）", async () => {
  const { failure } = await failureOf(400, { error: { message: "Invalid model route", code: 400 } });
  assert.equal(failure.kind, "BAD_REQUEST");
  assert.equal(failure.exitCode, EXIT.API_ERROR);
  assert.equal(relayRefused(500, "cannot be relayed"), false, "非 400 不认拒中继");
});

test("401 ⇒ AUTH；404 ⇒ NOT_FOUND；429 ⇒ RATE_LIMITED（可重试）", async () => {
  assert.equal((await failureOf(401, { error: { message: "No auth credentials found", code: 401 } })).failure.kind, "AUTH");
  assert.equal((await failureOf(404, { error: { message: "model not found", code: 404 } })).failure.kind, "NOT_FOUND");
  const limited = (await failureOf(429, { error: { message: "Rate limit exceeded", code: 429 } })).failure;
  assert.equal(limited.kind, "RATE_LIMITED");
  assert.equal(limited.retryable, true);
});

test("500 / 502 / 504 ⇒ SERVER_ERROR（可重试）", async () => {
  for (const status of [500, 502, 504]) {
    const { failure } = await failureOf(status, { error: { message: "upstream error", code: status } });
    assert.equal(failure.kind, "SERVER_ERROR", String(status));
    assert.equal(failure.retryable, true);
  }
});

test("连接失败 ⇒ NETWORK（exit 4）", async () => {
  const fetcher: Fetcher = async () => {
    throw new TypeError("fetch failed");
  };
  const client = createClient({ apiKey: "sk-or-v1-PLACEHOLDER00", fetcher });
  await assert.rejects(chatOnce(client, { model: "vendor/model-test", prompt: "hi" }));
  let failure = classifyFailure(new Error("unreachable"));
  try {
    await chatOnce(createClient({ apiKey: "sk-or-v1-PLACEHOLDER00", fetcher }), { model: "m", prompt: "p" });
  } catch (err) {
    failure = classifyFailure(err);
  }
  assert.equal(failure.kind, "NETWORK");
  assert.equal(failure.exitCode, EXIT.NETWORK);
});

test("200 ⇒ 解析出文本与用量；读路径体检解析额度", async () => {
  const chat = mockFetch(200, OK_BODY);
  const out = await chatOnce(createClient({ apiKey: "k-test", fetcher: chat.fetcher }), { model: "vendor/model-test", prompt: "ping" });
  assert.equal(out.text, "pong");
  assert.equal(out.promptTokens, 5);
  assert.equal(out.completionTokens, 1);
  assert.equal(out.returnedModel, "vendor/model-test");
  assert.deepEqual(chat.calls, [{ method: "POST", path: "/api/v1/chat/completions" }]);

  const credits = mockFetch(200, { data: { total_credits: 12.5, total_usage: 0.25 } });
  const health = await readHealth(createClient({ apiKey: "k-test", fetcher: credits.fetcher }));
  assert.deepEqual(credits.calls, [{ method: "GET", path: "/api/v1/credits" }]);
  assert.deepEqual(health, { totalCredits: 12.5, totalUsage: 0.25 });
});

test("脱敏：诊断文字里的 key 一律替换", async () => {
  const { failure } = await failureOf(400, { error: { message: "bad key sk-or-v1-PLACEHOLDER00 rejected", code: 400 } });
  assert.equal(failure.message.includes("PLACEHOLDER00"), false);
  assert.equal(failure.errorBody?.includes("PLACEHOLDER00"), false);
});
