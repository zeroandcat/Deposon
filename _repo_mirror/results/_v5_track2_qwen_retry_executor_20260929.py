"""
_v5_track2_qwen_retry_executor_20260929.py
==========================================
V4 Track 2 qwen_plan 401 重试棒（PI 2026-09-29 ask_0b4c1577f0d727e239e55095 q2 授权）

【PI 处置】401 重试须使用**最新文件**中的 URL 与 key（非旧版 key 文件）
【设计锚定】
- 目标槽 = qwen_plan（PI 2026-09-23 拍板三 URL 之一）：
    URL   = L22 host token-plan.maas.qianwenaiapi.com
    key   = L23（1-based 第 23 行）
    model = qwen3.7-max
- qwen **非** teamo/openrouter 系 ⇒ 按 PI 口径**直连**，不强制 tun
  （teamo/openrouter 走 tun 的纪律本棒不触发；如实登记）
- key 仅 runtime 内存读：0 落盘 / 0 入 prompt / 0 入 JSON / 0 入 log / 0 入 stdout
- 串行、间隔 >=2s、最小次数：全棒共 2 次调用（models 诊断 + chat 验证）
- 防降级核对：记录 response.model 与请求 model 比对

【四态判别设计（关键）】
单看 chat 401 无法区分「key 失效」与「model 端点 mismatch」。
故先用**同一 key** 打 /v1/models（认证面）：
  models 200 + chat 401  => key 有效，401 落在 chat 面 => 非 key 失效
  models 401             => key 失效实锤
  models 404 / chat 404  => 端点不认该路径 => 口径问题
  conn/ssl/timeout       => 环境阻（不冒充 401 结论）

【产物】results/_v5_track2_qwen_retry_2026_09_29.json（0 key 明文）
"""

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

import requests

# ---------------------------------------------------------------- 配置
KEY_FILE = r"C:\Users\Administrator\Desktop\AI\LLM API.txt"
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

URL_QWEN_TOKEN_PLAN = "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1"
KEY_LINE_1BASED = 23          # 探针实测：qwen_plan key 在第 23 行
MODEL_PRIMARY = "qwen3.7-max"
MODEL_FALLBACKS = ["qwen3.7-plus", "qwen3.6-flash"]

INTER_CALL_SLEEP_S = 2.0
TIMEOUT_S = 30
MAX_RESPONSE_CAPTURE = 600

OUT_JSON = r"D:\私人资料\deposon-repo\results\_v5_track2_qwen_retry_2026_09_29.json"

# 明文泄露防护：任何输出/产物前统一过一遍
SECRET_RX = re.compile(
    r"\b(?:sk-|sk-ant-|ark-)[A-Za-z0-9_\-]{8,}"
    r"|\b[A-Za-z0-9_\-]{60,}\b"
)


def scrub(s):
    """把疑似 key 明文抹成 <REDACTED>，防落盘/防 log。"""
    if s is None:
        return None
    return SECRET_RX.sub("<REDACTED>", str(s))


def load_key():
    """runtime 读 key；返回值只在本进程内存，绝不 print。"""
    with open(KEY_FILE, "r", encoding="utf-8", errors="replace") as f:
        lines = f.read().splitlines()
    return lines[KEY_LINE_1BASED - 1].strip()


def file_meta():
    st = os.stat(KEY_FILE)
    raw = open(KEY_FILE, "rb").read()
    return {
        "path": KEY_FILE,
        "size_bytes": st.st_size,
        "mtime_local": datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds"),
        "mtime_utc": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(timespec="seconds"),
        "sha256_12": hashlib.sha256(raw).hexdigest()[:12].upper(),
        "lines_total": len(raw.splitlines()),
    }


def call(session, url, headers, payload, label):
    """单次调用；返回四态可判的结构化结果（0 明文）。"""
    rec = {"label": label, "url": scrub(url), "t_start": datetime.now().isoformat(timespec="seconds")}
    t0 = time.time()
    try:
        r = session.post(url, headers=headers, json=payload, timeout=TIMEOUT_S)
        rec["http_status"] = r.status_code
        rec["latency_ms"] = round((time.time() - t0) * 1000, 1)
        ctype = r.headers.get("content-type", "")
        rec["content_type"] = ctype
        body_txt = r.text[:MAX_RESPONSE_CAPTURE]
        if "json" in ctype:
            try:
                j = r.json()
                rec["error_class"] = (j.get("error") or {}).get("type") if isinstance(j.get("error"), dict) else None
                rec["error_code"] = (j.get("error") or {}).get("code") if isinstance(j.get("error"), dict) else None
                rec["error_msg_scrubbed"] = scrub(
                    ((j.get("error") or {}).get("message") if isinstance(j.get("error"), dict) else None)
                )
                rec["response_model"] = j.get("model")            # 防降级核对用
                rec["object"] = j.get("object")
                if "data" in j and isinstance(j["data"], list):
                    rec["models_listed_count"] = len(j["data"])
                    rec["models_listed"] = [m.get("id") for m in j["data"][:40]]
                if "choices" in j and isinstance(j["choices"], list) and j["choices"]:
                    ch = j["choices"][0]
                    msg = (ch.get("message") or {}) if isinstance(ch, dict) else {}
                    txt = msg.get("content") or ""
                    rec["finish_reason"] = ch.get("finish_reason")
                    rec["completion_chars"] = len(txt)
                    rec["completion_head_scrubbed"] = scrub(txt[:160])
                if "usage" in j:
                    rec["usage"] = j["usage"]
            except Exception as e:
                rec["json_parse_error"] = scrub(e)
                rec["body_head_scrubbed"] = scrub(body_txt[:300])
        else:
            rec["body_head_scrubbed"] = scrub(body_txt[:300])
        rec["transport"] = "RESPONSE_RECEIVED"
    except requests.exceptions.ProxyError as e:
        rec["transport"] = "PROXY_ERROR"
        rec["error_class"] = "proxy_error"
        rec["error_msg_scrubbed"] = scrub(e)[:200]
        rec["latency_ms"] = round((time.time() - t0) * 1000, 1)
    except requests.exceptions.SSLError as e:
        rec["transport"] = "SSL_ERROR"
        rec["error_class"] = "ssl_error"
        rec["error_msg_scrubbed"] = scrub(e)[:200]
        rec["latency_ms"] = round((time.time() - t0) * 1000, 1)
    except requests.exceptions.ConnectTimeout as e:
        rec["transport"] = "CONNECT_TIMEOUT"
        rec["error_class"] = "connect_timeout"
        rec["error_msg_scrubbed"] = scrub(e)[:200]
    except requests.exceptions.ReadTimeout:
        rec["transport"] = "READ_TIMEOUT"
        rec["error_class"] = "read_timeout"
    except requests.exceptions.ConnectionError as e:
        rec["transport"] = "CONN_ERROR"
        rec["error_class"] = "conn_error"
        rec["error_msg_scrubbed"] = scrub(e)[:200]
        rec["latency_ms"] = round((time.time() - t0) * 1000, 1)
    except Exception as e:
        rec["transport"] = "OTHER_ERROR"
        rec["error_class"] = type(e).__name__
        rec["error_msg_scrubbed"] = scrub(e)[:200]
    return rec


def classify(models_rec, chat_rec):
    """四态判定。"""
    mt = models_rec.get("transport")
    ms = models_rec.get("http_status")
    ct = chat_rec.get("transport")
    cs = chat_rec.get("http_status")

    if mt in ("PROXY_ERROR", "SSL_ERROR", "CONN_ERROR", "CONNECT_TIMEOUT", "READ_TIMEOUT", "OTHER_ERROR") \
       or ct in ("PROXY_ERROR", "SSL_ERROR", "CONN_ERROR", "CONNECT_TIMEOUT", "READ_TIMEOUT", "OTHER_ERROR"):
        return "④ 网络/端点阻"

    if cs == 200 and chat_rec.get("completion_chars", 0) > 0:
        return "① 成功（401 解除）"
    if ms == 200 and cs == 401:
        return "② 仍 401（认证面矛盾：models 200 但 chat 401）"
    if ms == 401 or cs == 401:
        return "② 仍 401（key 失效实锤）"
    if cs == 404 or chat_rec.get("error_code") in ("model_not_found", "ModelNotFound") \
       or "model" in str(chat_rec.get("error_msg_scrubbed", "")).lower() and "not" in str(chat_rec.get("error_msg_scrubbed", "")).lower():
        return "③ model mismatch / 端点不认"
    if cs in (403, 429, 500, 502, 503):
        return "④ 网络/端点阻（HTTP %s）" % cs
    return "④ 未能归入四态（HTTP %s）" % cs


def main():
    print("=" * 68)
    print("V4 Track 2 qwen_plan 401 重试棒（PI 2026-09-29 授权）")
    print("=" * 68)
    meta = file_meta()
    print(f"key file : {meta['path']}")
    print(f"  mtime  : {meta['mtime_local']}   sha12={meta['sha256_12']}  {meta['size_bytes']}B")
    print(f"endpoint : {URL_QWEN_TOKEN_PLAN}   model={MODEL_PRIMARY}")
    print("key      : runtime 内存读（0 明文 / 0 落盘 / 0 入 log）")
    print("proxy    : 直连（qwen 非 teamo/openrouter 系，本棒不触发 tun 纪律）")
    print("-" * 68)

    key = load_key()
    session = requests.Session()
    session.trust_env = False   # 直连：不吃系统 env 代理
    headers = {"Authorization": "Bearer " + key, "Content-Type": "application/json"}
    del key

    # --- ① /v1/models 认证面诊断（PI 处置：换 key 方向验证）---
    print(f"[call 1/2] GET /v1/models  (认证面判别)")
    models_rec = call(session, URL_QWEN_TOKEN_PLAN + "/models", headers, None, "GET /v1/models")
    print(f"           -> {models_rec.get('transport')} status={models_rec.get('http_status')} "
          f"error={models_rec.get('error_class')}")
    time.sleep(INTER_CALL_SLEEP_S)

    # --- ② chat 验证（防降级核对 response.model）---
    print(f"[call 2/2] POST /chat/completions  model={MODEL_PRIMARY}")
    chat_rec = call(
        session,
        URL_QWEN_TOKEN_PLAN + "/chat/completions",
        headers,
        {
            "model": MODEL_PRIMARY,
            "messages": [{"role": "user", "content": "Reply with the single word: OK"}],
            "max_tokens": 16,
            "temperature": 0,
        },
        f"POST /chat/completions [{MODEL_PRIMARY}]",
    )
    print(f"           -> {chat_rec.get('transport')} status={chat_rec.get('http_status')} "
          f"err={chat_rec.get('error_class')} resp.model={chat_rec.get('response_model')}")

    state = classify(models_rec, chat_rec)
    print("-" * 68)
    print(f"四态判定 = {state}")

    result = {
        "task": "V4 Track 2 qwen_plan 401 retry",
        "pi_authorization": "ask_0b4c1577f0d727e239e55095 q2 (2026-09-29) - 须用最新文件的 URL+key",
        "generated_at_local": datetime.now().isoformat(timespec="seconds"),
        "author": "worker (Mavis)",  # 署名如实
        "key_file": meta,
        "key_disclosure": "0 明文：key 仅 runtime 内存读；不入文件/JSON/prompt/log/stdout",
        "endpoint": URL_QWEN_TOKEN_PLAN,
        "model_requested": MODEL_PRIMARY,
        "key_line_1based": KEY_LINE_1BASED,
        "proxy_policy": "直连（qwen_plan 非 teamo/openrouter 系；tun 纪律本棒未触发）",
        "call_budget": {"planned": 2, "actual": 2, "interval_s": INTER_CALL_SLEEP_S, "serial": True},
        "calls": [models_rec, chat_rec],
        "four_state_verdict": state,
        "downgrade_check": {
            "requested_model": MODEL_PRIMARY,
            "response_model": chat_rec.get("response_model"),
            "downgraded": (
                bool(chat_rec.get("response_model"))
                and chat_rec.get("response_model") != MODEL_PRIMARY
            ),
            "note": "response_model 与请求一致则无降级；为 null（未取到响应）则本面不可判",
        },
        "model_candidates_declared": [MODEL_PRIMARY] + MODEL_FALLBACKS,
    }

    # 落盘前最后一道明文闸
    blob = json.dumps(result, ensure_ascii=False, indent=2)
    blob = scrub(blob)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        f.write(blob)
    print(f"产物落盘 : {OUT_JSON}")
    print(f"产物 sha12: {hashlib.sha256(blob.encode('utf-8')).hexdigest()[:12].upper()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
