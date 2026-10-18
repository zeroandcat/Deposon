# -*- coding: utf-8 -*-
"""Quick latency test for the actual call to estimate budget."""
import hashlib
import os
import re
import sys
import time
from pathlib import Path

PROXY_HTTP = "http://127.0.0.1:1018"
os.environ["https_proxy"] = PROXY_HTTP
os.environ["http_proxy"] = PROXY_HTTP

# Test mimo only (no proxy in mimo case)
def fetch_api_key(idx_1based):
    key_path = Path("C:/Users/Administrator/Desktop/AI/LLM API.txt")
    raw = key_path.read_bytes()
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    lines = text.splitlines()
    return lines[idx_1based - 1].strip()

import requests as _requests

api_key = fetch_api_key(27)  # mimo
print(f"key len: {len(api_key)} (redacted)")

endpoints = [
    ("qwen_plan", "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1", "qwen3.7-max", 23, False),
    ("mimo", "https://token-plan-cn.xiaomimimo.com/v1", "mimo-v2.6-pro", 27, False),
    ("teamo", "https://api.teamorouter.cn/v1", "deepseek-v4-flash", 15, True),
]

prompts = [
    "列出机器学习训练流程的 6 个步骤, 每步一行, 用中文.",
    "按 界-门-纲-目-科-属-种 给出 2 个动物分类例子, 每层一行, 用中文.",
]

for label, ep, model, kidx, needr in endpoints:
    print(f"\n=== {label} (proxy={needr}) ===")
    api_key = fetch_api_key(kidx)
    for pi, p in enumerate(prompts):
        body = {
            "model": model,
            "messages": [{"role": "user", "content": p}],
            "max_tokens": 80,
            "temperature": 0.0,
            "stream": False,
        }
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }
        proxies = {"http": PROXY_HTTP, "https": PROXY_HTTP} if needr else None
        t0 = time.time()
        try:
            kwargs = {"headers": headers, "json": body, "timeout": 25}
            if proxies is not None:
                kwargs["proxies"] = proxies
            r = _requests.post(ep.rstrip("/") + "/chat/completions", **kwargs)
            latency = round((time.time() - t0) * 1000, 1)
            if r.status_code == 200:
                data = r.json()
                usage = data.get("usage", {})
                resp_text = ""
                if data.get("choices"):
                    resp_text = data["choices"][0].get("message", {}).get("content", "")
                print(f"  prompt[{pi}] ok in {latency}ms; tokens: {usage.get('prompt_tokens')}/{usage.get('completion_tokens')}; resp[:80]={resp_text[:80]!r}")
            else:
                print(f"  prompt[{pi}] FAIL {r.status_code} in {latency}ms; body[:200]={r.text[:200]}")
        except Exception as e:
            latency = round((time.time() - t0) * 1000, 1)
            print(f"  prompt[{pi}] EXC {type(e).__name__} in {latency}ms: {str(e)[:100]}")
        time.sleep(2.5)