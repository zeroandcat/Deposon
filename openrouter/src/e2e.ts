#!/usr/bin/env node
/**
 * e2e.ts — 端到端一条请求（读路径体检 ＋ 一次生成），每步输出一行 JSON（不含 key），末行给人读的结论。
 *
 * 用法：node dist/e2e.js [--model <slug>] [--prompt <文本>] [--max-tokens <n>]
 * 退出码：0 通 · 1 网关拒中继(400 cannot be relayed) · 2 其它 API 错(401/400/404/429/5xx…) ·
 *        3 未设 key · 4 网络 · 5 客户端用法错
 */

import { chatOnce, createClient, DEFAULT_MODEL, loadApiKey, readHealth, type TraceRecord } from "./client.js";
import { classifyFailure, EXIT } from "./errors.js";

function arg(name: string, fallback: string): string {
  const i = process.argv.indexOf(`--${name}`);
  return i > 0 && process.argv[i + 1] !== undefined ? process.argv[i + 1] : fallback;
}

function emit(record: Record<string, unknown>): void {
  process.stdout.write(`${JSON.stringify(record)}\n`);
}

async function main(): Promise<number> {
  const model = arg("model", DEFAULT_MODEL);
  const prompt = arg("prompt", "Reply with the single word: pong");
  const maxTokens = Number.parseInt(arg("max-tokens", "16"), 10);

  let apiKey: string;
  try {
    apiKey = loadApiKey();
  } catch (err) {
    process.stderr.write(`${err instanceof Error ? err.message : String(err)}\n`);
    return EXIT.MISSING_KEY;
  }

  const traces: TraceRecord[] = [];
  const client = createClient({ apiKey, onTrace: (t) => traces.push(t) });

  // 步骤 1：读路径体检（GET /credits）—— 区分「key/额度正常」与「网络不通」
  let readOk = false;
  try {
    const credits = await readHealth(client);
    readOk = true;
    emit({ step: "read-path", ok: true, endpoint: "GET /credits", ...credits });
  } catch (err) {
    emit({ step: "read-path", ok: false, endpoint: "GET /credits", ...classifyFailure(err, apiKey) });
  }

  // 步骤 2：一次生成请求（POST /chat/completions）
  try {
    const out = await chatOnce(client, { model, prompt, maxTokens });
    emit({ step: "generation", ok: true, endpoint: "POST /chat/completions", ...out });
    emit({
      step: "summary",
      verdict: "PASS",
      readPathOk: readOk,
      model,
      text: out.text,
      completionTokens: out.completionTokens,
      traces,
    });
    process.stdout.write(`PASS — 生成请求走通（model=${model}）：${JSON.stringify(out.text)}\n`);
    return EXIT.OK;
  } catch (err) {
    const failure = classifyFailure(err, apiKey);
    emit({ step: "generation", ok: false, endpoint: "POST /chat/completions", model, ...failure });
    emit({ step: "summary", verdict: failure.kind, readPathOk: readOk, model, exitCode: failure.exitCode, traces });
    process.stdout.write(
      `FAIL[${failure.kind}] http=${failure.httpStatus ?? "-"} release=${failure.release ?? "-"} origin=${failure.errorOrigin ?? "-"} — ${failure.message}\n`,
    );
    return failure.exitCode;
  }
}

process.exitCode = await main();
