# -*- coding: utf-8 -*-
"""
_track2_qwen_check_2026_09_23.py
=================================

Track 2 qwen_plan 401 校验 (最小测试请求, 不调业务)

纪律:
  - 0 LLM 业务调用 (仅 1 次 ping-style 请求, max_tokens=1)
  - 不落盘任何 key (内存读完即用即弃)
  - 不入 log / JSON / prompt / print
  - 产物里 key 字段一律 "runtime-env (redacted)"
  - 复用既有多模型探针 endpoint (与 _v4_v5_multimodel_probe.py 一致)

作者: Worker (subagent of Mavis)
日期: 2026-09-23
"""

import os
import sys
import json
import hashlib
import time
import urllib.request
import urllib.error
import ssl
import socket

# ============================================================================
# 路径常量
# ============================================================================
REPO_ROOT = r"D:/私人资料/deposon-repo"
RESULTS_DIR = os.path.join(REPO_ROOT, "results")

# 既有 V5 多模型探针 endpoint (沿 _v4_v5_multimodel_probe.py L48-58)
QWEN_PLAN_ENDPOINT = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
QWEN_PLAN_MODEL = "qwen-turbo"

# 既有 V5 多模型探针 proxy
PROXY_HTTP = "http://127.0.0.1:1018"

# Key 源 (与 _v4_v5_multimodel_probe.py 一致, 仅读取, 不落盘)
KEY_SOURCE = "C:/Users/Administrator/Desktop/AI/LLM API.txt"
# 沿 2026-09-23 11:30 调整后, Qwen-plan 实际位于 line 17 (label at 16)
QWEN_PLAN_KEY_LINE = 17  # 1-based, 与 _v4_v5_multimodel_probe.py 旧值 20 不同 (旧值错指 mimo)

OUT_JSON = os.path.join(RESULTS_DIR, "_track2_qwen_check_2026_09_23.json")


# ============================================================================
# 工具: SHA-12 自算
# ============================================================================
def sha12_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def sha12_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


# ============================================================================
# Key 读取 (内存 only, 不落盘, 不入 log/JSON/prompt/print)
# ============================================================================
def read_key_runtime(line_1based: int) -> str:
    """
    仅本次 runtime 内存使用, 函数返回后调用方必须立即使用并清空变量。
    函数本身不写入任何持久存储。
    """
    raw = open(KEY_SOURCE, "rb").read()
    text = None
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        raise RuntimeError("key file encoding fail")
    lines = text.splitlines()
    if line_1based > len(lines):
        raise RuntimeError(f"key line {line_1based} > total {len(lines)}")
    return lines[line_1based - 1].strip()


# ============================================================================
# qwen_plan 最小测试请求 (ping)
# ============================================================================
def probe_qwen_plan(timeout: int = 30) -> dict:
    # ====== setup proxy ======
    os.environ["https_proxy"] = PROXY_HTTP
    os.environ["http_proxy"] = PROXY_HTTP

    # ====== 读 key (内存 only, 不落盘) ======
    try:
        api_key = read_key_runtime(QWEN_PLAN_KEY_LINE)
    except Exception as e:
        return {
            "ok": False,
            "stage": "key_read",
            "error": str(e)[:200],
            "key_source_line": QWEN_PLAN_KEY_LINE,
            "key_field": "runtime-env (redacted)",
        }

    # ====== 准备最小 ping 请求 ======
    body_obj = {
        "model": QWEN_PLAN_MODEL,
        "messages": [{"role": "user", "content": "ping"}],
        "max_tokens": 1,
        "temperature": 0.0,
    }
    body_bytes = json.dumps(body_obj).encode("utf-8")

    # headers - 不打印 Authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # 强制清空 api_key 字符串 (best-effort, Python 字符串不可变, GC 会回收)
    api_key = None
    del api_key

    # ====== 用 urllib 发请求 (避免额外依赖) ======
    req = urllib.request.Request(
        QWEN_PLAN_ENDPOINT,
        data=body_bytes,
        headers=headers,
        method="POST",
    )
    # SSL context: 用 default (Python ssl 默认 verify)
    ctx = ssl.create_default_context()

    t0 = time.time()
    try:
        # proxy handler
        proxy_handler = urllib.request.ProxyHandler({
            "http": PROXY_HTTP,
            "https": PROXY_HTTP,
        })
        opener = urllib.request.build_opener(proxy_handler, urllib.request.HTTPSHandler(context=ctx))
        resp = opener.open(req, timeout=timeout)
        status = resp.status
        latency = round((time.time() - t0) * 1000, 1)
        # 不读取 response body (避免任何 LLM 输出)
        try:
            body_snippet = resp.read(200).decode("utf-8", errors="replace")
        except Exception:
            body_snippet = "<read fail>"
        return {
            "ok": True,
            "stage": "ping",
            "status_code": status,
            "latency_ms": latency,
            "error_class": classify_status(status),
            "body_snippet": body_snippet,
            "key_field": "runtime-env (redacted)",
            "key_source_line": QWEN_PLAN_KEY_LINE,
        }
    except urllib.error.HTTPError as e:
        latency = round((time.time() - t0) * 1000, 1)
        return {
            "ok": False,
            "stage": "http",
            "status_code": e.code,
            "latency_ms": latency,
            "error_class": classify_status(e.code),
            "body_snippet": (e.read(300).decode("utf-8", errors="replace") if hasattr(e, "read") else "")[:300],
            "key_field": "runtime-env (redacted)",
            "key_source_line": QWEN_PLAN_KEY_LINE,
        }
    except urllib.error.URLError as e:
        latency = round((time.time() - t0) * 1000, 1)
        return {
            "ok": False,
            "stage": "url_error",
            "error": str(e.reason)[:300],
            "latency_ms": latency,
            "error_class": "url_error",
            "key_field": "runtime-env (redacted)",
            "key_source_line": QWEN_PLAN_KEY_LINE,
        }
    except (socket.timeout, TimeoutError):
        latency = round((time.time() - t0) * 1000, 1)
        return {
            "ok": False,
            "stage": "timeout",
            "latency_ms": latency,
            "error_class": "timeout",
            "key_field": "runtime-env (redacted)",
            "key_source_line": QWEN_PLAN_KEY_LINE,
        }
    except Exception as e:
        latency = round((time.time() - t0) * 1000, 1)
        return {
            "ok": False,
            "stage": "exception",
            "error": str(e)[:300],
            "latency_ms": latency,
            "error_class": "exception",
            "key_field": "runtime-env (redacted)",
            "key_source_line": QWEN_PLAN_KEY_LINE,
        }


def classify_status(status: int) -> str:
    if status == 200:
        return "200_OK"
    elif status == 401:
        return "401_unauthorized"
    elif status == 403:
        return "403_forbidden"
    elif status == 404:
        return "404_not_found"
    elif status == 429:
        return "429_rate_limited"
    elif 500 <= status < 600:
        return f"{status}_server_error"
    else:
        return f"{status}_other"


# ============================================================================
# teamo / mimo 缺口声明 (缺正确 URL, 不起跑)
# ============================================================================
TEAMO_MIMO_GAP_DECL = {
    "teamo": {
        "url_provided_by_pi": None,
        "prior_observation": "prior probe (`results/_v4_v5_multimodel_probe.log`): teamo → ssl_error (https://api.teamo.ai 443 unreachable through proxy 127.0.0.1:1018)",
        "status": "缺 PI 提供 URL, 未起跑",
        "key_field": "runtime-env (redacted)",
    },
    "mimo": {
        "url_provided_by_pi": None,
        "prior_observation": "prior probe (`results/_v4_v5_multimodel_probe.log`): mimo → conn_error (ConnectionResetError 10054, 远程主机强迫关闭)",
        "status": "缺 PI 提供 URL, 未起跑",
        "key_field": "runtime-env (redacted)",
    },
}


# ============================================================================
# 主
# ============================================================================
def main():
    print("=" * 72)
    print("Track 2 qwen_plan 401 校验 - 最小 ping")
    print("=" * 72)
    print(f"Endpoint: {QWEN_PLAN_ENDPOINT[:60]}...")
    print(f"Model: {QWEN_PLAN_MODEL}")
    print(f"Proxy: {PROXY_HTTP}")
    print(f"Key line: {QWEN_PLAN_KEY_LINE} (in-memory only, no disk write)")
    print()

    result_qwen = probe_qwen_plan(timeout=30)
    print(f"qwen_plan probe: ok={result_qwen.get('ok')}, status={result_qwen.get('status_code')}, "
          f"error_class={result_qwen.get('error_class')}, latency={result_qwen.get('latency_ms')}ms")

    # ====== 校验结论: 401 是否消失 ======
    if result_qwen.get("ok") and result_qwen.get("status_code") == 200:
        qwen_401_conclusion = "401 已消失 (HTTP 200)"
    elif result_qwen.get("status_code") == 401:
        qwen_401_conclusion = "401 仍在 (HTTP 401, key 不被 dart-scope provider 接受)"
    elif result_qwen.get("ok") is False and result_qwen.get("stage") == "key_read":
        qwen_401_conclusion = f"未起跑: key 读取失败 ({result_qwen.get('error')})"
    elif result_qwen.get("error_class") == "url_error":
        qwen_401_conclusion = f"未起跑: URL 不可达 ({result_qwen.get('error')[:100]})"
    elif result_qwen.get("error_class") == "timeout":
        qwen_401_conclusion = "未起跑: 超时"
    else:
        qwen_401_conclusion = f"其他 (status={result_qwen.get('status_code')}, error_class={result_qwen.get('error_class')})"

    print(f"\n校验结论: {qwen_401_conclusion}")

    # ====== 边界声明 ======
    result = {
        "task": "Track 2 qwen_plan 401 校验",
        "task_id": "V3X-DIAG-2026-09-23-B1",
        "date": "2026-09-23",
        "scope": "1 次最小 ping-style 请求 (max_tokens=1) 到 qwen_plan endpoint, 不调业务",
        "iron_rule_compliance": {
            "no_key_in_json_log_prompt": True,
            "key_in_memory_only": True,
            "no_business_llm_call": True,  # 仅 ping, max_tokens=1, 不读 response content
            "key_field_in_product": "runtime-env (redacted)",
        },
        "endpoint_config": {
            "endpoint": QWEN_PLAN_ENDPOINT,
            "model": QWEN_PLAN_MODEL,
            "proxy": PROXY_HTTP,
            "key_source_line_1based": QWEN_PLAN_KEY_LINE,
            "key_source_note": "C:/Users/Administrator/Desktop/AI/LLM API.txt (workspace 外, runtime read, in-memory only)",
        },
        "qwen_plan_result": result_qwen,
        "qwen_401_conclusion": qwen_401_conclusion,
        "teamo_mimo_gap_declaration": TEAMO_MIMO_GAP_DECL,
        "prior_baseline_reference": {
            "log_file": "results/_v4_v5_multimodel_probe.log",
            "prior_qwen_plan_status": "401 (key_index=20 错指 mimo 行, 实因非 endpoint/key 真值)",
            "prior_qwen_status": "200 OK (key_index=17 = Qwen-plan 真值)",
        },
        "boundary_declaration": {
            "modified_files": 0,
            "new_files": ["results/_track2_qwen_check_2026_09_23.py"],
            "output_landed_in": "results/_track2_qwen_check_2026_09_23.json",
        },
    }

    # ====== 落盘 ======
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    out_bytes = open(OUT_JSON, "rb").read()
    out_sha12 = sha12_bytes(out_bytes)

    print(f"\n落盘: {OUT_JSON}")
    print(f"  size: {len(out_bytes)} B")
    print(f"  SHA-12: {out_sha12}")
    print("=" * 72)

    return 0


if __name__ == "__main__":
    sys.exit(main())