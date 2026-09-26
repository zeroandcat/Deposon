# -*- coding: utf-8 -*-
"""再探测 - 基于 /v1/models 列表选正确 model_id"""
from __future__ import annotations
import os, sys, json, time
import requests as _requests

PROXY_HTTP = "http://127.0.0.1:1018"
KEY_SOURCE = "C:/Users/Administrator/Desktop/AI/LLM API.txt"

# 新选择: 每个端点用最相近的 deepseek / qwen / mimo 模型
PROBES = [
    ("qwen_plan", "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1", 23, False, ["qwen3.7-max", "qwen3.7-plus", "qwen3.6-flash"]),
    ("mimo", "https://token-plan-cn.xiaomimimo.com/v1", 27, False, ["mimo-v2.6-pro", "mimo-v2.6-flash", "mimo-v2.5-pro"]),
    ("teamo", "https://api.teamorouter.cn/v1", 15, True, ["deepseek-v4-flash", "deepseek-v4-pro", "deepseek-flash"]),
]

def fetch_key(idx):
    raw = open(KEY_SOURCE, "rb").read()
    for enc in ("utf-8", "gb18030", "gbk"):
        try: text = raw.decode(enc); break
        except: continue
    return text.splitlines()[idx - 1].strip()

def main():
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass
    os.environ["https_proxy"] = PROXY_HTTP
    os.environ["http_proxy"] = PROXY_HTTP

    for label, base, kidx, use_proxy, models in PROBES:
        print(f"\n=== {label} ===")
        key = fetch_key(kidx)
        proxies = {"http": PROXY_HTTP, "https": PROXY_HTTP} if use_proxy else None
        for m in models:
            url = base.rstrip("/") + "/chat/completions"
            headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
            body = {"model": m, "messages": [{"role":"user","content":"ping"}], "max_tokens": 1, "temperature": 0.0}
            try:
                r = _requests.post(url, headers=headers, json=body, proxies=proxies, timeout=20)
                if r.status_code == 200:
                    d = r.json()
                    mr = d.get("model","")
                    content = d.get("choices",[{}])[0].get("message",{}).get("content","")
                    print(f"  [OK] model={m} returned={mr} content={content[:60]!r}")
                    break
                else:
                    print(f"  [FAIL {r.status_code}] model={m} err={r.text[:200]}")
            except Exception as e:
                print(f"  [EXC] model={m} {e}")
        time.sleep(2.5)

if __name__ == "__main__":
    main()