# -*- coding: utf-8 -*-
"""
_v4_track2_endpoints_probe.py
================================

V4 Track 2 多模型补跑 - 三端点探活（PI 2026-09-23 派工）
================================================================

【设计锚定】
================================================================
- 复用既有 _v4_v5_multimodel_probe.py 的 key 读取 + proxy 设置惯例
- 三端点（PI 拍板，权威 URL）:
    qwen 槽 -> https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1
    mimo  槽 -> https://token-plan-cn.xiaomimimo.com/v1
    teamo 槽 -> https://api.teamorouter.cn/v1
- PI 2026-09-23 补充 2: teamo/openrouter 类端点必须走 tun/代理
  (https_proxy=http://127.0.0.1:1018 等); qwen/mimo 按原网络路径
- PI 2026-09-23 补充 2: 串行 + ≥2s 间隔（防封号）
- key 仅 runtime 内存读; 不落盘 / 不入 prompt / 不入 JSON / 不入 log / 不入回报
- 产物: _track2_endpoints_probe_2026_09_23.json
- URL ↔ 槽位映射由实测认证确定; 若某 URL 认证失败如实登记

【差异声明】
================================================================
- _v4_v5_multimodel_probe.py 内端点段仍为旧 URL (dashscope / mioplus / teamo.ai),
  与 PI 当条派工三 URL 不一致。PI 指示"以文件为准" + "如有出入在 verdict 声明"。
  本探针按 PI 当条三 URL 探活, 并在 verdict MD 显式声明差异, 不擅自改写 probe 文件
  (probe 文件沿用既有 SHA-12 `5FE4CBD93D92` 作为模板只读复用)。

【铁律】
================================================================
- R4 key 永不明文 (无例外): 产物 key 字段一律写 "runtime-env (redacted)"
- R5 V4 frozen 只追加: 本棒仅产出新增 JSON, 已有件 0 触动
- 不擅动 workspace 外 (key 文件仅读不写)
- 派生 JSON 不合并
- 不擅自调阈值

【产物落盘】
================================================================
- _track2_endpoints_probe_2026_09_23.json: 端点探活记录
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Tuple

import requests as _requests

# ============================================================
# 路径与常量
# ============================================================
ROOT = "D:/私人资料/deposon-repo"
RESULTS_DIR = os.path.join(ROOT, "results")
KEY_SOURCE_PATH = "C:/Users/Administrator/Desktop/AI/LLM API.txt"

# PI 拍板代理 (tun/127.0.0.1:1018; PI 2026-09-23 补充 2)
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# PI 拍板三 URL（当条派工权威）
# 注: PI 2026-09-23 ask_3ee5edf74be2d6ef53fbc4b4 Q4 给出 qwen/mimo;
#     PI 2026-09-23 补充 1 补 teamo (api.teamorouter.cn)
#     probe 文件 _v4_v5_multimodel_probe.py 端点段为旧 URL, 与本探针三 URL 不一致;
#     按 PI 指示在 verdict 声明差异。
URL_QWEN_TOKEN_PLAN = "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1"
URL_MIMO_TOKEN_PLAN = "https://token-plan-cn.xiaomimimo.com/v1"
URL_TEAMO_ROUTER = "https://api.teamorouter.cn/v1"

# 探针超时
PROBE_TIMEOUT = 30
# PI 2026-09-23 补充 2: 串行 + ≥2s 间隔
INTER_PROBE_SLEEP_S = 2.5

# ============================================================
# 候选路由 (PI 当条派工)
# 注: key_index_1based 沿 API.txt 当前行号 (PI 2026-09-23 11:30 后已迁移)
# 候选 model_id: 经 /v1/models 列表探查后选定 (PI 拍板实测认证确定)
# ============================================================
PROBES = [
    {
        "label": "qwen_plan",
        "endpoint_base": URL_QWEN_TOKEN_PLAN,
        "use_proxy": False,
        "key_index_1based": 23,  # Qwen-plan key 在 API.txt 第 23 行
        "candidates": [
            "qwen3.7-max",  # /v1/models 列表首选
            "qwen3.7-plus",
            "qwen3.6-flash",
        ],
    },
    {
        "label": "mimo",
        "endpoint_base": URL_MIMO_TOKEN_PLAN,
        "use_proxy": False,
        "key_index_1based": 27,  # mimo-plan key 在 API.txt 第 27 行
        "candidates": [
            "mimo-v2.6-pro",  # /v1/models 列表首选
            "mimo-v2.6-flash",
            "mimo-v2.5-pro",
        ],
    },
    {
        "label": "teamo",
        "endpoint_base": URL_TEAMO_ROUTER,
        "use_proxy": True,  # PI 2026-09-23 补充 2: teamo/openrouter 类必走代理
        "key_index_1based": 15,  # teamo key 在 API.txt 第 15 行
        "candidates": [
            "deepseek-v4-flash",  # /v1/models 列表首选; 响应 model 名 = deepseek-v4-flash-ga-260731
            "deepseek-v4-pro",
            "deepseek-flash",
        ],
    },
]


# ============================================================
# 工具
# ============================================================
def setup_proxy() -> None:
    """PI 2026-09-23 补充 2: 设置 tun/代理环境变量 + requests 显式代理。"""
    os.environ["https_proxy"] = PROXY_HTTP
    os.environ["http_proxy"] = PROXY_HTTP
    os.environ["all_proxy"] = PROXY_SOCKS5


def fetch_api_key(key_index_1based: int) -> str:
    raw = open(KEY_SOURCE_PATH, "rb").read()
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise RuntimeError("key source file: no decodable encoding found")
    lines = text.splitlines()
    key = lines[key_index_1based - 1].strip()
    if not key or len(key) < 20:
        raise RuntimeError(
            f"key line {key_index_1based} empty or too short; abort"
        )
    return key


def classify_status(sc: int) -> str:
    if sc == 401:
        return "auth_failed"
    if sc == 402:
        return "quota_exhausted"
    if sc == 404:
        return "endpoint_not_found"
    if sc == 429:
        return "rate_limited"
    if 400 <= sc < 500:
        return "client_error_4xx"
    if 500 <= sc < 600:
        return "server_error_5xx"
    return f"http_{sc}"


def probe_endpoint_with_model(
    api_key: str,
    endpoint: str,
    model: str,
    use_proxy: bool,
    timeout: int = PROBE_TIMEOUT,
) -> Dict[str, Any]:
    """单次最小 ping: max_tokens=1。"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if "openrouter" in endpoint or "teamorouter" in endpoint:
        headers["HTTP-Referer"] = "https://deposon.local/v5-multimodel-probe"
        headers["X-Title"] = "deposon-v5-multimodel-probe"

    body = {
        "model": model,
        "messages": [{"role": "user", "content": "ping"}],
        "max_tokens": 1,
        "temperature": 0.0,
        "stream": False,
    }
    proxies = {"http": PROXY_HTTP, "https": PROXY_HTTP} if use_proxy else None

    chat_url = endpoint.rstrip("/") + "/chat/completions"

    t0 = time.time()
    try:
        r = _requests.post(
            chat_url,
            headers=headers,
            json=body,
            proxies=proxies,
            timeout=timeout,
        )
        latency_ms = round((time.time() - t0) * 1000, 1)
        if r.status_code == 200:
            try:
                data = r.json()
                content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
                model_returned = data.get("model", "")
            except Exception:
                content = ""
                model_returned = ""
            return {
                "ok": True,
                "status_code": r.status_code,
                "latency_ms": latency_ms,
                "model": model,
                "model_returned": model_returned,
                "endpoint": chat_url,
                "content_preview": content[:80],
            }
        return {
            "ok": False,
            "status_code": r.status_code,
            "error_category": classify_status(r.status_code),
            "latency_ms": latency_ms,
            "model": model,
            "endpoint": chat_url,
            "error_body_snippet": r.text[:300],
        }
    except _requests.exceptions.ProxyError as e:
        return {
            "ok": False,
            "error_category": "proxy_error",
            "latency_ms": round((time.time() - t0) * 1000, 1),
            "model": model,
            "endpoint": chat_url,
            "error_snippet": str(e)[:200],
        }
    except _requests.exceptions.SSLError as e:
        return {
            "ok": False,
            "error_category": "ssl_error",
            "latency_ms": round((time.time() - t0) * 1000, 1),
            "model": model,
            "endpoint": chat_url,
            "error_snippet": str(e)[:200],
        }
    except _requests.exceptions.ConnectionError as e:
        return {
            "ok": False,
            "error_category": "connection_error",
            "latency_ms": round((time.time() - t0) * 1000, 1),
            "model": model,
            "endpoint": chat_url,
            "error_snippet": str(e)[:200],
        }
    except _requests.exceptions.Timeout as e:
        return {
            "ok": False,
            "error_category": "timeout",
            "latency_ms": round((time.time() - t0) * 1000, 1),
            "model": model,
            "endpoint": chat_url,
            "error_snippet": str(e)[:200],
        }
    except Exception as e:
        return {
            "ok": False,
            "error_category": "other",
            "latency_ms": round((time.time() - t0) * 1000, 1),
            "model": model,
            "endpoint": chat_url,
            "error_snippet": str(e)[:200],
        }


def self_scan_text(text: str) -> List[Tuple[str, int]]:
    hits: List[Tuple[str, int]] = []
    SENSITIVE = [
        ("api_key_literal", re.compile(r"(?i)api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{8,}")),
        ("sk_literal", re.compile(r"(?i)sk-[A-Za-z0-9_\-]{8,}")),
        ("Bearer_token", re.compile(r"(?i)Bearer\s+[A-Za-z0-9_\-\.]{20,}")),
        ("tp_token", re.compile(r"(?i)tp-[A-Za-z0-9]{8,}")),
        ("sp_key", re.compile(r"(?i)sk-sp-[A-Za-z0-9_\-\.]{8,}")),
        ("sk_teamo", re.compile(r"(?i)sk-teamo-[A-Za-z0-9]{8,}")),
    ]
    for name, pat in SENSITIVE:
        n = len(pat.findall(text))
        if n > 0:
            hits.append((name, n))
    return hits


def self_scan_obj(obj: Any) -> List[Tuple[str, int]]:
    s = json.dumps(obj, ensure_ascii=False, sort_keys=True)
    return self_scan_text(s)


def sha12_file(path: str) -> Tuple[str, int, int, bool, bool]:
    with open(path, "rb") as f:
        data = f.read()
    h = hashlib.sha256(data).hexdigest()[:12]
    n_bytes = len(data)
    has_bom = data.startswith(b"\xef\xbb\xbf")
    n_lines = data.decode("utf-8", errors="replace").count("\n")
    is_lf_only = b"\r" not in data
    return h, n_bytes, n_lines, is_lf_only, not has_bom


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 Track 2 多模型补跑 - 三端点探活 (PI 2026-09-23 派工)")
    print("=" * 60)
    print(f"Proxy (PI 2026-09-23 补充 2): {PROXY_HTTP} / {PROXY_SOCKS5}")
    print(f"Key source: {KEY_SOURCE_PATH} (workspace 外, PI 授权只读)")
    print(f"Probe interval: {INTER_PROBE_SLEEP_S}s (PI 防封号)")
    print(f"Probes: {len(PROBES)} (qwen_plan / mimo / teamo)")
    print()

    setup_proxy()

    # PowerShell console GBK: ensure stdout utf-8 safe
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass

    results: List[Dict[str, Any]] = []
    for i, p in enumerate(PROBES):
        print(f"\n--- [{i+1}/{len(PROBES)}] {p['label']} ---")
        print(f"  endpoint: {p['endpoint_base']}")
        print(f"  use_proxy: {p['use_proxy']}")
        print(f"  key_index_1based: {p['key_index_1based']}")

        try:
            api_key = fetch_api_key(p["key_index_1based"])
        except Exception as e:
            print(f"  KEY_READ FAIL: {e}")
            results.append({
                "label": p["label"],
                "endpoint_base": p["endpoint_base"],
                "use_proxy": p["use_proxy"],
                "key_index_1based": p["key_index_1based"],
                "key_source": "runtime-env (redacted)",
                "ok": False,
                "stage": "key_read",
                "error": str(e)[:200],
                "attempts": [],
                "mapped_slot": None,
                "mapped_model_id": None,
            })
            if i < len(PROBES) - 1:
                time.sleep(INTER_PROBE_SLEEP_S)
            continue

        attempts: List[Dict[str, Any]] = []
        ok_attempt = None
        for j, model_id in enumerate(p["candidates"]):
            print(f"  candidate {j+1}/{len(p['candidates'])}: {model_id}")
            r = probe_endpoint_with_model(
                api_key=api_key,
                endpoint=p["endpoint_base"],
                model=model_id,
                use_proxy=p["use_proxy"],
            )
            attempts.append({
                "model_id": model_id,
                "ok": r.get("ok", False),
                "status_code": r.get("status_code"),
                "error_category": r.get("error_category"),
                "latency_ms": r.get("latency_ms"),
                "model_returned": r.get("model_returned", ""),
                "error_body_snippet": r.get("error_body_snippet", "")[:200],
                "error_snippet": r.get("error_snippet", "")[:200],
            })
            if r.get("ok") and ok_attempt is None:
                ok_attempt = r
                print(f"    [OK] status={r['status_code']} model_returned={r.get('model_returned','')} latency={r['latency_ms']}ms")
                break  # 第一个成功即停止 (PI 防封号: 最小必要)
            else:
                print(f"    [FAIL] status={r.get('status_code','')} cat={r.get('error_category','')}")

        if ok_attempt:
            mapped = {
                "label": p["label"],
                "endpoint_base": p["endpoint_base"],
                "use_proxy": p["use_proxy"],
                "key_index_1based": p["key_index_1based"],
                "key_source": "runtime-env (redacted)",
                "ok": True,
                "stage": "ping",
                "ok_attempt": {
                    "model_id": ok_attempt["model"],
                    "status_code": ok_attempt["status_code"],
                    "latency_ms": ok_attempt["latency_ms"],
                    "model_returned": ok_attempt["model_returned"],
                    "endpoint_chat_url": ok_attempt["endpoint"],
                    "content_preview": ok_attempt["content_preview"],
                },
                "attempts": attempts,
                "mapped_slot": p["label"],
                "mapped_model_id": ok_attempt["model_returned"] or ok_attempt["model"],
                "slot_mapping_method": "实测认证 (PI 拍板三 URL ↔ 槽位)",
            }
        else:
            mapped = {
                "label": p["label"],
                "endpoint_base": p["endpoint_base"],
                "use_proxy": p["use_proxy"],
                "key_index_1based": p["key_index_1based"],
                "key_source": "runtime-env (redacted)",
                "ok": False,
                "stage": "all_candidates_failed",
                "attempts": attempts,
                "mapped_slot": None,
                "mapped_model_id": None,
                "slot_mapping_method": "认证失败: URL ↔ 槽位映射失败, 如实登记",
            }
        results.append(mapped)

        # PI 防封号: 端点之间 ≥2s
        del api_key  # 用完即 del
        if i < len(PROBES) - 1:
            print(f"\n  [sleep {INTER_PROBE_SLEEP_S}s 防封号]")
            time.sleep(INTER_PROBE_SLEEP_S)

    # 汇总
    print("\n" + "=" * 60)
    print("汇总")
    print("=" * 60)
    for r in results:
        sym = "[OK]" if r["ok"] else "[FAIL]"
        slot = r.get("mapped_slot") or "未映射"
        model = r.get("mapped_model_id") or "-"
        print(f"  {sym} {r['label']:12s} -> slot={slot:10s} model={model:32s} status={r.get('ok_attempt',{}).get('status_code') or r.get('attempts',[{}])[0].get('status_code','')}")

    # 落盘
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    out = {
        "metadata": {
            "task": "track2_endpoints_probe",
            "date": "2026-09-23",
            "author": "Mavis worker (Track 2 多模型补跑 子任务)",
            "freeze_day": "V5 补强 D1 (件 3 续, 端点探活)",
            "spec_conformance": "PI 2026-09-23 ask_3ee5edf74be2d6ef53fbc4b4 Q4 + 补充 1 (teamo) + 补充 2 (代理 + 串行)",
            "proxy_settings": {
                "http": PROXY_HTTP,
                "socks5": PROXY_SOCKS5,
                "rationale": "PI 2026-09-23 补充 2: teamo/openrouter 类端点必走代理防封号",
            },
            "serial_policy": {
                "inter_probe_sleep_s": INTER_PROBE_SLEEP_S,
                "rationale": "PI 2026-09-23 补充 2: 串行 ≥2s 防封号",
            },
            "key_discipline": {
                "source": KEY_SOURCE_PATH,
                "method": "runtime memory read",
                "redacted_in_products": "true",
                "rationale": "R4 key 永不明文 (无例外)",
            },
            "endpoint_set_discrepancy": {
                "pi_authoritative_urls": [
                    URL_QWEN_TOKEN_PLAN,
                    URL_MIMO_TOKEN_PLAN,
                    URL_TEAMO_ROUTER,
                ],
                "file_authoritative_urls": [
                    "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions (qwen_plan, 旧)",
                    "https://api.mioplus.mi.com/v1/chat/completions (mimo, 旧)",
                    "https://api.teamo.ai/v1/chat/completions (teamo, 旧)",
                ],
                "file_source": "_v4_v5_multimodel_probe.py",
                "discrepancy_resolution": "按 PI 当条派工三 URL 探活 (PI 2026-09-23 ask_3ee5edf74be2d6ef53fbc4b4 Q4 + 补充 1); probe 文件未触动 (沿用 SHA-12 5FE4CBD93D92); verdict MD 显式声明差异",
                "probe_file_sha12_before": "5FE4CBD93D92",
            },
            "predecessor_chain_sha12": {
                "track2_runner_template": "900A6D1E50AF",
                "measure_function": "21771E66AF67",
                "teacher_paths": "D2BD7521D651",
                "track2_product_openrouter": "61EDBE39A618",
                "track2_product_deepseek_direct": "1B05EBA8639B",
                "track2_product_qwen": "AE541E34781E",
                "track2_measure_v5": "7CCBE2C3E248",
                "track2_ablation_v5": "DC35655F8E7C",
                "track2_verdict_v5": "83D8E7A8BA12",
                "ablation_verdict_v5": "C2920AA9923A",
                "multimodel_compare_v5": "356BD6647796",
                "multimodel_verdict_v5": "C386251D94D6",
                "probe_template_v5": "5FE4CBD93D92",
            },
        },
        "results": results,
        "constraints_compliance": {
            "key_never_in_prompt_or_json": True,
            "key_never_on_disk": True,
            "no_proxy_regen": True,
            "serial_with_min_2s_gap": True,
            "proxy_for_teamo_endpoint": True,
            "probe_template_unchanged": True,
            "rationale": "PI 2026-09-23 补充 2 硬要求; R4 沿用",
        },
        "call_time_cst": now_iso,
    }

    out_path = os.path.join(RESULTS_DIR, "_track2_endpoints_probe_2026_09_23.json")

    pre_hits = self_scan_obj(out)
    if pre_hits:
        print(f"\nFATAL: pre-write 自扫命中 {pre_hits}")
        return 1
    print(f"\n  pre-write 自扫: 0 命中")

    body = json.dumps(out, ensure_ascii=False, sort_keys=False, indent=2)
    body = body.replace("\r\n", "\n").replace("\r", "")
    if body.startswith("\ufeff"):
        body = body[1:]

    with open(out_path, "wb") as f:
        f.write(body.encode("utf-8"))

    with open(out_path, "r", encoding="utf-8") as f:
        on_disk = f.read()
    post_hits = self_scan_text(on_disk)
    if post_hits:
        print(f"FATAL: 落盘后自扫命中 {post_hits}")
        return 1

    h12, n_bytes, n_lines, is_lf, no_bom = sha12_file(out_path)
    print(f"\n  probe JSON: SHA-12={h12}  bytes={n_bytes}  lines={n_lines}  LF={is_lf}  noBOM={no_bom}")
    print(f"  saved: {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())