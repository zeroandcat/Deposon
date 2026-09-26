# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch2_r2_models_probe.py
=========================================

V4 L14+ batch 2 round 2 预备 · 查 teamo /v1/models 列出全部 model_id
===================================================================

【派工依据】
----------------
- 沿 batch1 r6 executor `5f02c7e0f094` + r6 result `a4f851154551` 口径
- 沿 r1（探活 fail 版）executor `E52F930654D3` + result `D245AE4CE385` 探活记录
- r1 探活漏做：派工单字面「teamo 模型清单实测」未做；glm-4 错误信息明确指 GET /v1/models
- 本文件 = 一次性查 /v1/models 端点（探活预备），不计入正式 calls 账
"""

from __future__ import annotations

import json
import os
import sys
import time
from typing import Any, Dict, List

import requests as _requests

ROOT = "D:/私人资料/deposon-repo"
KEY_SOURCE_PATH = "C:/Users/Administrator/Desktop/AI/LLM API.txt"
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
PROXY_HTTP = "http://127.0.0.1:1018"
KEY_INDEX_TEAMO_1BASED = 15


def setup_proxy():
    os.environ["https_proxy"] = PROXY_HTTP
    os.environ["http_proxy"] = PROXY_HTTP
    os.environ["all_proxy"] = "socks5://127.0.0.1:1018"


def fetch_api_key(idx_1based: int) -> str:
    raw = open(KEY_SOURCE_PATH, "rb").read()
    text = None
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        raise RuntimeError("key source: no decodable encoding")
    lines = text.splitlines()
    key = lines[idx_1based - 1].strip()
    if not key or len(key) < 20:
        raise RuntimeError(f"key line {idx_1based} invalid")
    return key


def list_models(api_key: str) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch2-r2-probe",
        "X-Title": "deposon-l14v3-batch2-r2-models-probe",
    }
    url = ENDPOINT_TEAMO.rstrip("/") + "/models"
    proxies = {"http": PROXY_HTTP, "https": PROXY_HTTP}
    t0 = time.time()
    try:
        r = _requests.get(url, headers=headers, proxies=proxies, timeout=60)
        latency_ms = round((time.time() - t0) * 1000, 1)
        body = r.text
        try:
            data = r.json()
        except Exception:
            data = None
        return {
            "ok": r.status_code == 200,
            "status_code": r.status_code,
            "latency_ms": latency_ms,
            "body_snippet": body[:2000],
            "data": data,
        }
    except Exception as e:
        return {
            "ok": False,
            "error_category": type(e).__name__,
            "latency_ms": round((time.time() - t0) * 1000, 1),
            "error_snippet": str(e)[:300],
        }


def main() -> int:
    setup_proxy()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
    print(f"[INIT] key loaded (len={len(api_key)}, redacted)")
    print(f"[PROBE] GET {ENDPOINT_TEAMO}/models")
    result = list_models(api_key)
    print(f"[STATUS] ok={result.get('ok')} sc={result.get('status_code')} lat={result.get('latency_ms')}ms")
    if not result.get("ok"):
        print(f"[ERROR] {result.get('error_category')}: {result.get('error_snippet')[:200]}")
        return 2
    data = result.get("data")
    if not isinstance(data, dict):
        print(f"[WARN] /v1/models 返回非 dict: {type(data).__name__}; snippet={result.get('body_snippet')[:200]}")
        return 3
    # 列出 model_id
    if "data" in data and isinstance(data["data"], list):
        models = data["data"]
    elif isinstance(data, list):
        models = data
    else:
        models = []
    print(f"[MODELS COUNT] {len(models)}")
    glm_like = []
    for m in models:
        if isinstance(m, dict):
            mid = m.get("id") or m.get("model") or m.get("name") or ""
        else:
            mid = str(m)
        mid_lower = mid.lower()
        if any(k in mid_lower for k in ("glm", "chatglm", "z-", "z_", "z ")):
            glm_like.append(mid)
        print(f"  - {mid}")
    print(f"[GLM-LIKE COUNT] {len(glm_like)}")
    if glm_like:
        print("[GLM-LIKE LIST]")
        for m in glm_like:
            print(f"  - {m}")
    # 落盘清单
    out_path = os.path.join(ROOT, "results", "_v4_supp_l14v3_batch2_r2_models_probe.json")
    record = {
        "schema": "v4_l14v3_n26/1_models_probe",
        "endpoint": ENDPOINT_TEAMO + "/models",
        "fetched_at_cst": time.strftime("%Y-%m-%dT%H:%M:%S+08:00", time.localtime()),
        "status_code": result.get("status_code"),
        "latency_ms": result.get("latency_ms"),
        "model_count_total": len(models),
        "model_count_glm_like": len(glm_like),
        "glm_like_ids": glm_like,
        "all_ids_extracted": [m.get("id") if isinstance(m, dict) else str(m) for m in models],
        "raw_data_keys": list(data.keys()) if isinstance(data, dict) else None,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)
    print(f"[WROTE] {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
