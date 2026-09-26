# -*- coding: utf-8 -*-
"""
_v4_track2_models_probe.py
================================

三端点 /v1/models 列表探查（验证可用 model_id）
PI 2026-09-23 拍板三 URL
"""

from __future__ import annotations
import os
import sys
import json
import time
import requests as _requests

PROXY_HTTP = "http://127.0.0.1:1018"
KEY_SOURCE = "C:/Users/Administrator/Desktop/AI/LLM API.txt"

URLS = [
    ("qwen_plan", "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1", 23, False),
    ("mimo", "https://token-plan-cn.xiaomimimo.com/v1", 27, False),
    ("teamo", "https://api.teamorouter.cn/v1", 15, True),
]

def fetch_key(idx):
    raw = open(KEY_SOURCE, "rb").read()
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc); break
        except: continue
    lines = text.splitlines()
    return lines[idx - 1].strip()

def setup_proxy():
    os.environ["https_proxy"] = PROXY_HTTP
    os.environ["http_proxy"] = PROXY_HTTP

def main():
    try: sys.stdout.reconfigure(encoding="utf-8")
    except: pass
    setup_proxy()
    for label, base, kidx, use_proxy in URLS:
        print(f"\n=== {label} ({base}) ===")
        try:
            key = fetch_key(kidx)
        except Exception as e:
            print(f"  KEY_FAIL: {e}")
            continue
        # try GET /v1/models
        url = base.rstrip("/") + "/models"
        headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
        proxies = {"http": PROXY_HTTP, "https": PROXY_HTTP} if use_proxy else None
        try:
            r = _requests.get(url, headers=headers, proxies=proxies, timeout=20)
            print(f"  GET /models status={r.status_code}")
            if r.status_code == 200:
                try:
                    data = r.json()
                    if "data" in data:
                        ids = [m.get("id","") for m in data["data"]]
                        print(f"  models ({len(ids)}): {ids[:30]}")
                    else:
                        print(f"  body keys: {list(data.keys())[:10]}")
                        print(f"  body preview: {r.text[:500]}")
                except Exception:
                    print(f"  body preview: {r.text[:500]}")
            else:
                print(f"  body preview: {r.text[:300]}")
        except Exception as e:
            print(f"  EXC: {e}")
        time.sleep(2.5)

if __name__ == "__main__":
    main()