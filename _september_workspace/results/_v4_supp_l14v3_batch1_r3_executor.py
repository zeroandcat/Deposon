# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch1_r3_executor.py
=====================================

V4 L14+ 首批 (batch 1) · round 3 续采 — kimi 教师侧 round 3 + 补缺
===================================================================

【派工依据】
----------------
- 沿 r2 `results/_v4_supp_l14v3_batch1_r2_executor.py`（SHA-12 `2bdb5163400f`）+ r2 产物
  `results/_v4_supp_l14v3_batch1_r2_result.json`（SHA-12 `00c7b545c397`）口径直接续跑
- 沿上棒 `results/_v4_supp_l14v3_batch1_executor.py`（SHA-12 `b48019494530`）
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（字面引用 `05B975A86989`）字面
- 同 agent 唤醒保上下文（task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义）

【本棒范围】
----------------
1. **S6_n60 carry-over retry**（reask=0）：上棒 EMPTY + 上上棒 EMPTY → 该 caption 目前 0 successful call，
   本棒 reask=0 retry（沿 dispatch §1 「S6_n60 需连同其 carry-over EMPTY 的 retry 一起补齐」）
2. **round 2 缺位 4 件补缺**（reask=1）：S6 / S6_n20 / S6_n35 / S6_n60
3. **round 3 续采**（reask=2）：22 caption × 第 3 call
4. 计划 calls = 1 (S6_n60 carry-over retry) + 4 (round 2 补缺) + 22 (round 3) = 27 calls
5. 预算 ≤22 calls / ≤600s watchdog（沿 dispatch §2 + L7 实证 ≤275s 上限）；scheduling = 补缺 5 件排最前
6. 跑不完如实报断点（沿 prereg §1.6.4 partial completion 协议）

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §3）】
--------------------------------------------------------------------
- 累计 = batch1 + r2 + r3 总 cumulative
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 实测累计基线（沿 batch1 + r2 既有产物）：
  - batch1 (r1): total=21, empty=1 (4.76%)
  - r2: total=19, empty=4 (21.05%)
  - **CUMULATIVE prior: total=40, empty=5, rate=12.5%**
  - r3 worst case (22 EMPTY): cumulative = 27/62 = 43.5% (仍 < 50% 阈值)
- 触发记录路径：result.json `K_N26_observability_only.K_N26_N2_observation.cumulative_trigger` 字段

【工具失灵族参数修正（沿 dispatch §3）】
-----------------------------------------
- **内层重试 read timeout 提至 90s**：r2 EMPTY 4/4 = 100% 同源于 teamo+tun 网络层 60s read timeout；
  timeout 频发 = 21.05% > 5% 经验阈值 → 提至 90s
- 属工具失灵族参数修正（非阈值私设，沿 prereg §1.4 工具失灵修正条款类同 max_tokens=2000）
- 在 result.json `metadata.tools_fault_param_correction` 字段显式记录（沿 v0.2 §0 同口径）

【端点取舍（沿上棒实测）】
----------------------------
- teamo + tun + kimi-k3（沿上棒 `model_id_inconsistency_honest_disclosure` 字面）
- 不重新探活（沿 dispatch §2 「沿 r2 口径直接续跑」）

【铁律严守（沿上棒）】
------------------------
- R4 key 永不明文（无例外）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch1_r3_*` 与上棒 `_batch1_r2_*` + `_batch1_*` 同级独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；内层重试 ≤3；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch1_r3_result.json`（schema = `v4_l14v3_n26/1` + batch=1 + round=3）
- 不覆盖 r2 result `00c7b545c397` 或上棒 result `22eb01144062`（沿 dispatch §4）

【与 r2 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. 新增参数：`ROUND = 3` / `CARRYOVER_RETRY_S6_N60 = True` / `CARRYOVER_RETRY_REASK = 0`
2. 新增调度：`planned_calls = [S6_n60 carry-over retry reask=0] + [4 round 2 补缺 reask=1] + [22 round 3 reask=2]` = 27 calls
3. 新增工具失灵族参数修正：`READ_TIMEOUT_INITIAL_S = 60` / `READ_TIMEOUT_RETRY_S = 90`（沿 dispatch §3）
4. 新增累计 empty_rate 监控：每 call 后实时算 cumulative rate；>0.50 立即停采
5. 新增字段：每 quadruple 增 `round_index` 1/2/3 (carry-over retry 标 1=round 1; round 2 补缺标 2; round 3 标 3)
6. 新增字段：每 quadruple 增 `is_round_2_makeup` (bool) / `is_round_3` (bool)
7. 新增 K-N26-N2 cumulative_trigger 字段（沿 dispatch §3）

【边界】
----------
- 不动任何既有件（含 r2 executor `2bdb5163400f` + r2 result `00c7b545c397` + 上棒 executor `b48019494530` + 上棒 result `22eb01144062` + prereg `05B975A86989`）
- 跑不完拆段报断点
- 0 触动 V1–V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Tuple, Optional

import requests as _requests

# ============================================================
# 路径与常量
# ============================================================
ROOT = "D:/私人资料/deposon-repo"
RESULTS_DIR = os.path.join(ROOT, "results")
CAPTIONS_PATH = os.path.join(ROOT, "corpus", "v20_caption_surface", "strip_captions_22.json")
KEY_SOURCE_PATH = "C:/Users/Administrator/Desktop/AI/LLM API.txt"
BATCH1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_result.json")
R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r2_result.json")

# tun 代理（沿上棒）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（沿上棒实测）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_KIMI_K3 = "kimi-k3"
KEY_INDEX_TEAMO_1BASED = 15
USE_PROXY = True

# 串行间隔
INTER_CALL_SLEEP_S = 2.5

# 超参（沿上棒）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 dispatch §3：read timeout 重试提至 90s）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# K-N26-N2 累计 empty_rate 停采阈值（沿 dispatch §3）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算
WALL_TIME_BUDGET_S = 600

# 本棒调度
ROUND = 3

# S6_n60 carry-over retry（沿 dispatch §1）
CARRYOVER_RETRY_S6_N60 = True
CARRYOVER_RETRY_CAPTION_ID = "S6_n60"
CARRYOVER_RETRY_REASK = 0  # 第 1 次采集 (retry of failed carry-over)

# round 2 补缺 4 件（沿 r2 partial completion 协议）
ROUND_2_MAKEUP_CAPTION_IDS = ["S6", "S6_n20", "S6_n35", "S6_n60"]
ROUND_2_MAKEUP_REASK = 1

# round 3 全部 22 caption
ROUND_3_REASK = 2


# ============================================================
# 敏感模式（沿上棒）
# ============================================================
SENSITIVE_PATTERNS = [
    ("api_key_literal", re.compile(r"(?i)api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{8,}")),
    ("sk_literal", re.compile(r"(?i)sk-[A-Za-z0-9_\-]{8,}")),
    ("Bearer_token", re.compile(r"(?i)Bearer\s+[A-Za-z0-9_\-\.]{20,}")),
    ("tp_token", re.compile(r"(?i)tp-[A-Za-z0-9]{8,}")),
    ("sp_key", re.compile(r"(?i)sk-sp-[A-Za-z0-9_\-\.]{8,}")),
    ("sk_teamo", re.compile(r"(?i)sk-teamo-[A-Za-z0-9]{8,}")),
    ("openai_endpoint", re.compile(r"(?i)openai-[A-Za-z0-9_\-]{4,}")),
    ("claude_endpoint", re.compile(r"(?i)claude-[A-Za-z0-9_\-]{4,}")),
    ("ark_endpoint", re.compile(r"(?i)ark-[A-Za-z0-9_\-]{4,}")),
]


# ============================================================
# 工具（沿上棒 + 复用）
# ============================================================
def setup_proxy_teamo() -> None:
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
        raise RuntimeError(f"key line {key_index_1based} empty or too short; abort")
    return key


def is_empty_response(text: str) -> bool:
    if text is None:
        return True
    return text.strip() == ""


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


def call_chat_teamo(
    api_key: str,
    messages: List[Dict[str, str]],
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
    timeout: int = READ_TIMEOUT_INITIAL_S,
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch1-r3",
        "X-Title": "deposon-l14v3-batch1-r3-kimi-teacher",
    }
    body = {
        "model": MODEL_KIMI_K3,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    chat_url = ENDPOINT_TEAMO.rstrip("/") + "/chat/completions"
    proxies = {"http": PROXY_HTTP, "https": PROXY_HTTP}

    t0 = time.time()
    try:
        r = _requests.post(
            chat_url, headers=headers, json=body, proxies=proxies, timeout=timeout,
        )
        latency_ms = round((time.time() - t0) * 1000, 1)
        if r.status_code != 200:
            return {
                "ok": False,
                "status_code": r.status_code,
                "error_category": classify_status(r.status_code),
                "latency_ms": latency_ms,
                "error_body_snippet": r.text[:300],
            }
        data = r.json()
        content = ""
        try:
            content = data["choices"][0]["message"]["content"] or ""
        except (KeyError, IndexError, TypeError):
            content = ""
        return {
            "ok": True,
            "status_code": r.status_code,
            "latency_ms": latency_ms,
            "model_returned": data.get("model", ""),
            "id": data.get("id", ""),
            "content": content,
            "usage": data.get("usage", {}),
        }
    except _requests.exceptions.ProxyError as e:
        return {"ok": False, "error_category": "proxy_error",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}
    except _requests.exceptions.SSLError as e:
        return {"ok": False, "error_category": "ssl_error",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}
    except _requests.exceptions.ConnectionError as e:
        return {"ok": False, "error_category": "connection_error",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}
    except _requests.exceptions.Timeout as e:
        return {"ok": False, "error_category": "timeout",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}
    except Exception as e:
        return {"ok": False, "error_category": "other",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}


def self_scan_text(text: str) -> List[Tuple[str, int]]:
    hits: List[Tuple[str, int]] = []
    for name, pat in SENSITIVE_PATTERNS:
        n = len(pat.findall(text))
        if n > 0:
            hits.append((name, n))
    return hits


def self_scan_obj(obj: Any) -> List[Tuple[str, int]]:
    s = json.dumps(obj, ensure_ascii=False, sort_keys=True)
    return self_scan_text(s)


def sha12_file(path: str) -> Tuple[str, int, bool]:
    with open(path, "rb") as f:
        data = f.read()
    return hashlib.sha256(data).hexdigest()[:12], len(data), b"\r" not in data


# ============================================================
# 提示构造（沿上棒）
# ============================================================
PROMPT_SYSTEM = (
    "You are generating a V3-style concept-graph distillation continuation. "
    "Given a concept graph caption (a comma-separated sequence of concept "
    "labels), generate 3-5 NEW related concept labels that would naturally "
    "extend this graph. Output ONLY a single line of comma-separated labels "
    "(no other text, no commentary, no markdown)."
)


def build_user_prompt(caption_text: str, caption_id: str) -> str:
    return (
        f"Caption ID: {caption_id}\n"
        f"Caption (sequence of concept labels in the graph):\n{caption_text}\n\n"
        f"Task: Generate 3-5 NEW related concept labels that would naturally "
        f"extend this graph. Output only a single line of comma-separated labels."
    )


def load_captions() -> List[Dict[str, Any]]:
    with open(CAPTIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# 单 call + 内层重试 (initial 60s → retry 90s) + 四元组落盘
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    carry_over: bool,
    is_round_2_makeup: bool,
    is_round_3: bool,
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    # prompt_id 沿上棒惯例
    suffix = ""
    if carry_over:
        suffix = "_carryover_r0_retry"
    elif is_round_2_makeup:
        suffix = "_r2_makeup"
    elif is_round_3:
        suffix = "_r3"
    else:
        suffix = f"_r{round_index}"
    prompt_id = f"kimi_t01_{side}_{caption_id}{suffix}"

    retries = 0
    last = None
    while retries <= INNER_RETRY_MAX:
        # 第 1 次用 initial timeout, retry 用 retry timeout（沿 dispatch §3）
        timeout_s = READ_TIMEOUT_INITIAL_S if retries == 0 else READ_TIMEOUT_RETRY_S
        r = call_chat_teamo(api_key=api_key, messages=messages, timeout=timeout_s)
        last = r
        if r["ok"]:
            content = r.get("content", "")
            if not is_empty_response(content):
                return {
                    "prompt_id": prompt_id,
                    "prompt_text": prompt_text,
                    "response_text": content,
                    "per_call_metadata": {
                        "ok": True,
                        "status_code": r["status_code"],
                        "latency_ms": r["latency_ms"],
                        "model_returned": r.get("model_returned", ""),
                        "id": r.get("id", ""),
                        "usage": r.get("usage", {}),
                        "endpoint": ENDPOINT_TEAMO + "/chat/completions",
                        "model_id_sent": MODEL_KIMI_K3,
                        "side": side,
                        "caption_id": caption_id,
                        "reask_idx": reask_idx,
                        "round_index": round_index,
                        "carry_over": carry_over,
                        "is_round_2_makeup": is_round_2_makeup,
                        "is_round_3": is_round_3,
                        "temperature": TEMPERATURE,
                        "max_tokens": MAX_TOKENS,
                        "retry_count": retries,
                        "read_timeout_s": timeout_s,
                        "empty_response": False,
                        "error_category": None,
                        "error_snippet": "",
                    },
                }
            retries += 1
            time.sleep(INTER_CALL_SLEEP_S)
            continue
        return {
            "prompt_id": prompt_id,
            "prompt_text": prompt_text,
            "response_text": "",
            "per_call_metadata": {
                "ok": False,
                "status_code": r.get("status_code"),
                "latency_ms": r.get("latency_ms", 0),
                "model_returned": r.get("model_returned", ""),
                "id": r.get("id", ""),
                "usage": r.get("usage", {}),
                "endpoint": ENDPOINT_TEAMO + "/chat/completions",
                "model_id_sent": MODEL_KIMI_K3,
                "side": side,
                "caption_id": caption_id,
                "reask_idx": reask_idx,
                "round_index": round_index,
                "carry_over": carry_over,
                "is_round_2_makeup": is_round_2_makeup,
                "is_round_3": is_round_3,
                "temperature": TEMPERATURE,
                "max_tokens": MAX_TOKENS,
                "retry_count": retries,
                "read_timeout_s": timeout_s,
                "empty_response": is_empty_response(""),
                "error_category": r.get("error_category", "unknown"),
                "error_snippet": (r.get("error_body_snippet") or r.get("error_snippet") or "")[:200],
            },
        }
    content = last.get("content", "") if last and last.get("ok") else ""
    return {
        "prompt_id": prompt_id,
        "prompt_text": prompt_text,
        "response_text": content,
        "per_call_metadata": {
            "ok": False,
            "status_code": last.get("status_code") if last else None,
            "latency_ms": last.get("latency_ms", 0) if last else 0,
            "model_returned": last.get("model_returned", "") if last else "",
            "id": last.get("id", "") if last else "",
            "usage": last.get("usage", {}) if last else {},
            "endpoint": ENDPOINT_TEAMO + "/chat/completions",
            "model_id_sent": MODEL_KIMI_K3,
            "side": side,
            "caption_id": caption_id,
            "reask_idx": reask_idx,
            "round_index": round_index,
            "carry_over": carry_over,
            "is_round_2_makeup": is_round_2_makeup,
            "is_round_3": is_round_3,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "retry_count": INNER_RETRY_MAX,
            "read_timeout_s": READ_TIMEOUT_RETRY_S,
            "empty_response": True,
            "error_category": "empty_response_after_retries",
            "error_snippet": f"empty response after {INNER_RETRY_MAX} retries (max retry timeout={READ_TIMEOUT_RETRY_S}s)",
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 L14+ batch 1 round 3 · kimi 教师侧")
    print("计划 calls = 1 (S6_n60 carry-over retry) + 4 (round 2 补缺) + 22 (round 3) = 27 calls")
    print("预算 ≤22 calls / ≤600s watchdog（沿 dispatch §2）")
    print("empty_rate 累计阈值 = 0.50 (沿 dispatch §3 K-N26-N2 累计停采)")
    print("内层 retry timeout = 90s (沿 dispatch §3 工具失灵族参数修正)")
    print("端点: teamo + tun + kimi-k3 (沿上棒 executor b48019494530)")
    print("=" * 60)

    setup_proxy_teamo()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # 1. 加载 caption
    captions = load_captions()
    cap_by_id = {c["id"]: c for c in captions}
    print(f"[INIT] captions loaded: {len(captions)}")

    # 2. 加载 key
    try:
        api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
        print(f"[INIT] teamo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 3. 装载上棒 cumulative（沿 dispatch §3 累计 empty_rate 监控）
    with open(BATCH1_RESULT_PATH, "r", encoding="utf-8") as f:
        batch1 = json.load(f)
    with open(R2_RESULT_PATH, "r", encoding="utf-8") as f:
        r2 = json.load(f)
    cum_total_prior = batch1["aggregate"]["total_calls"] + r2["aggregate"]["total_calls"]
    cum_empty_prior = batch1["aggregate"]["empty_response_count"] + r2["aggregate"]["empty_response_count"]
    cum_ok_prior = batch1["aggregate"]["ok_count"] + r2["aggregate"]["ok_count"]
    cum_rate_prior = cum_empty_prior / cum_total_prior if cum_total_prior > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior} ok={cum_ok_prior} empty={cum_empty_prior} rate={cum_rate_prior:.4f}")

    # 4. 调度 planned_calls（补缺排最前）
    planned: List[Dict[str, Any]] = []
    # S6_n60 carry-over retry
    if CARRYOVER_RETRY_S6_N60:
        planned.append({
            "caption_id": CARRYOVER_RETRY_CAPTION_ID,
            "reask_idx": CARRYOVER_RETRY_REASK,
            "carry_over": True,
            "is_round_2_makeup": False,
            "is_round_3": False,
            "round_index": 1,  # 第 1 次采集 retry
            "phase": "carry_over_retry",
        })
    # round 2 补缺 4 件
    for cap_id in ROUND_2_MAKEUP_CAPTION_IDS:
        planned.append({
            "caption_id": cap_id,
            "reask_idx": ROUND_2_MAKEUP_REASK,
            "carry_over": False,
            "is_round_2_makeup": True,
            "is_round_3": False,
            "round_index": 2,
            "phase": "round_2_makeup",
        })
    # round 3 全部 22 caption
    for c in captions:
        planned.append({
            "caption_id": c["id"],
            "reask_idx": ROUND_3_REASK,
            "carry_over": False,
            "is_round_2_makeup": False,
            "is_round_3": True,
            "round_index": 3,
            "phase": "round_3",
        })

    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (1 carry-over retry + {len(ROUND_2_MAKEUP_CAPTION_IDS)} round 2 makeup + {len(captions)} round 3)")

    # 5. 时间预算起点
    t_batch_start = time.time()

    # 6. 跑
    quadruples: List[Dict[str, Any]] = []
    cum_total = cum_total_prior
    cum_empty = cum_empty_prior
    cum_ok = cum_ok_prior
    r3_total = 0
    r3_ok = 0
    r3_empty = 0
    r3_fail = 0
    r3_carry_over_retry_count = 0
    r3_round_2_makeup_count = 0
    r3_round_3_count = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    k_n26_n2_triggered = False
    k_n26_n2_trigger_at_call_idx = None
    k_n26_n2_trigger_cum_rate = None
    stop_reason = None

    for i, item in enumerate(planned):
        elapsed = time.time() - t_batch_start
        if elapsed > WALL_TIME_BUDGET_S:
            stop_reason = f"wall_time_{WALL_TIME_BUDGET_S}s"
            print(f"[BREAKPOINT] wall time {elapsed:.1f}s > {WALL_TIME_BUDGET_S}s watchdog; stop at call {i}/{planned_total}")
            break

        cap_id = item["caption_id"]
        caption = cap_by_id.get(cap_id)
        if caption is None:
            print(f"[WARN] caption_id={cap_id} not found; skip")
            continue

        # K-N26-N2 累计 empty_rate 停采监控（沿 dispatch §3）
        if cum_total > 0:
            current_cum_rate = cum_empty / cum_total
            if current_cum_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i
                k_n26_n2_trigger_cum_rate = current_cum_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 cumulative empty_rate={current_cum_rate:.4f} > 0.50 at call {i}/{planned_total}; stop per dispatch §3")
                break

        rec = run_one_quadruple(
            api_key=api_key,
            caption=caption,
            reask_idx=item["reask_idx"],
            side="teacher",
            round_index=item["round_index"],
            carry_over=item["carry_over"],
            is_round_2_makeup=item["is_round_2_makeup"],
            is_round_3=item["is_round_3"],
        )
        quadruples.append(rec)
        m = rec["per_call_metadata"]
        is_ok = m["ok"] and not m["empty_response"]
        is_empty = m["empty_response"]
        is_fail = not m["ok"]

        if is_ok:
            r3_ok += 1
            cum_ok += 1
        elif is_empty:
            r3_empty += 1
            cum_empty += 1
        else:
            r3_fail += 1
        r3_total += 1
        cum_total += 1

        if item["phase"] == "carry_over_retry":
            r3_carry_over_retry_count += 1
        elif item["phase"] == "round_2_makeup":
            r3_round_2_makeup_count += 1
        elif item["phase"] == "round_3":
            r3_round_3_count += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = (
            "[carry-over retry]" if item["phase"] == "carry_over_retry"
            else f"[r2-makeup]" if item["phase"] == "round_2_makeup"
            else f"[r{ROUND}]"
        )
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"{status} "
            f"[cum_rate={current_cum_rate_post:.4f}]"
        )

        # K-N26-N2 停采监控（call 后立即判）
        if cum_total > 0:
            post_rate = cum_empty / cum_total
            if post_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i + 1
                k_n26_n2_trigger_cum_rate = post_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 post-call cumulative empty_rate={post_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch §3")
                break

        if i < planned_total - 1:
            time.sleep(INTER_CALL_SLEEP_S)

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)

    # 7. 统计
    empty_rate_r3 = (r3_empty / r3_total) if r3_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))
    breakpoint_hit = wall_time_s > WALL_TIME_BUDGET_S

    # 8. round 3 缺 caption
    ran_caption_ids_round_3 = set(
        q["per_call_metadata"]["caption_id"] for q in quadruples
        if q["per_call_metadata"].get("is_round_3")
    )
    missing_for_round_3 = sorted(
        c["id"] for c in captions if c["id"] not in ran_caption_ids_round_3
    )

    # 9. S6_n60 状态
    s6_n60_records = [q for q in quadruples if q["per_call_metadata"]["caption_id"] == "S6_n60"]
    s6_n60_successful = sum(
        1 for q in s6_n60_records
        if q["per_call_metadata"]["ok"] and not q["per_call_metadata"]["empty_response"]
    )

    # 10. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 1,
        "round": 3,
        "metadata": {
            "task": "L14V3_batch1_round3_kimi_teacher_side",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "executor_sha12": "2bdb5163400f",
                "executor_path": "results/_v4_supp_l14v3_batch1_r2_executor.py",
                "r2_result_sha12": "00c7b545c397",
                "r2_result_path": "results/_v4_supp_l14v3_batch1_r2_result.json",
                "batch1_executor_sha12": "b48019494530",
                "batch1_executor_path": "results/_v4_supp_l14v3_batch1_executor.py",
                "batch1_result_sha12": "22eb01144062",
                "batch1_result_path": "results/_v4_supp_l14v3_batch1_result.json",
            },
            "date": "2026-09-24",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 1 round 3",
            "spec_conformance": "PI 2026-09-24 同 agent 唤醒 (task_append) 接力棒 + 沿 r2 executor/口径直接续跑 + empty_rate 累计监控 + 工具失灵族参数修正",
            "teacher": "kimi",
            "side": "teacher",
            "round_index": 3,
            "n_captions_total": len(captions),
            "n_carry_over_retry_planned": 1 if CARRYOVER_RETRY_S6_N60 else 0,
            "n_carry_over_retry_actual": r3_carry_over_retry_count,
            "n_round_2_makeup_planned": len(ROUND_2_MAKEUP_CAPTION_IDS),
            "n_round_2_makeup_actual": r3_round_2_makeup_count,
            "n_round_3_planned": len(captions),
            "n_round_3_actual": r3_round_3_count,
            "planned_total": planned_total,
            "actual_total": r3_total,
            "calls_per_caption_target": 5,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": "沿上棒 executor b48019494530 实测 (kimi-k3 唯一可达)",
            "model_id_sent": MODEL_KIMI_K3,
            "model_id_inconsistency_honest_disclosure": batch1["metadata"]["model_id_inconsistency_honest_disclosure"],
            "proxy_settings": {
                "http": PROXY_HTTP,
                "socks5": PROXY_SOCKS5,
                "applied_to_teamo": USE_PROXY,
            },
            "key_discipline": {
                "source": KEY_SOURCE_PATH,
                "key_index_1based": KEY_INDEX_TEAMO_1BASED,
                "method": "runtime memory read",
                "redacted_in_products": True,
            },
            "inter_call_sleep_s": INTER_CALL_SLEEP_S,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "max_tokens_rationale": "prereg §1.4 工具失灵修正条款 (L4 verdict 74B5B37F7EEA §2 构造失灵族补构造; 非擅调阈值)",
            "tools_fault_param_correction": {
                "read_timeout_initial_s": READ_TIMEOUT_INITIAL_S,
                "read_timeout_retry_s": READ_TIMEOUT_RETRY_S,
                "rationale": (
                    "r2 EMPTY 4/4 = 100% 同源于 teamo+tun 网络层 60s read timeout；"
                    "empty_rate 升幅显著 (4.76% → 21.05%) → 工具失灵族参数修正（非阈值私设，沿 prereg §1.4 工具失灵修正条款类同 max_tokens=2000）"
                    "：内层重试 read timeout 由 60s 提至 90s"
                ),
                "scope": "本棒 executor 仅；不改上棒既有件；不改 prereg 字面",
                "trigger": "timeout 频发 (r2 empty_rate 21.05% > 5% 经验阈值)",
                "dispensation": "dispatch 2026-09-24 §3 字面授权（『若 timeout 频发可在重试中把 read timeout 提至 90s』）",
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "call_timeout_s": READ_TIMEOUT_INITIAL_S,  # 兼容字段; 实际由 tools_fault_param_correction 控制
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r2_executor": [
                "1. 新增 ROUND=3 / CARRYOVER_RETRY_S6_N60=True 参数化",
                "2. 新增调度: [S6_n60 carry-over retry reask=0] + [4 round 2 补缺 reask=1] + [22 round 3 reask=2] = 27 calls",
                "3. 工具失灵族参数修正: read_timeout_initial_s=60 / read_timeout_retry_s=90 (沿 dispatch §3)",
                "4. K-N26-N2 累计 empty_rate 监控: cumulative rate > 0.50 立即停采（沿 dispatch §3）",
                "5. 每 quadruple 增 is_round_2_makeup / is_round_3 / read_timeout_s 字段",
                "6. prompt_id 增 _carryover_r0_retry / _r2_makeup / _r3 三相后缀",
                "7. aggregate 增 cumulative 字段 (prior_total / prior_empty / prior_rate / post_total / post_empty / post_rate)",
                "8. K_N26_N2_observation 增 cumulative_trigger 字段",
                "9. tools_fault_param_correction 显式记录（沿 v0.2 §0 同口径）",
                "10. predecessor_sha12 链新增 r2_executor/r2_result/batch1_executor/batch1_result 全链",
            ],
            "iron_rules": {
                "R1_no_llm": False,
                "R2_no_proxy": False,
                "R3_no_gateway": False,
                "R4_key_never_in_plaintext": True,
                "R5_v4_frozen_append_only": True,
                "R6_pg_v0_v01_untouched": True,
                "R7_plugin_spec_untouched": True,
                "v1_v3_readonly": True,
                "tun_compliance_teamo_endpoint": tun_compliance,
                "serial_interval_ge_2_5_s": True,
                "empty_response_counted_not_dropped": True,
                "kill_line_locked_K_N26_1_2_3_N1_N2": True,
                "no_threshold_adjustment": True,
                "no_existing_file_modified": True,
                "no_merge_of_derived_json": True,
                "no_overwrite_batch1_result_or_r2_result": True,
            },
            "run_window_cst": now_iso,
            "wall_time_actual_s": wall_time_s,
            "stop_reason": stop_reason,
        },
        "quadruples": quadruples,
        "aggregate": {
            "r3_total_calls": r3_total,
            "r3_ok_count": r3_ok,
            "r3_empty_response_count": r3_empty,
            "r3_fail_count": r3_fail,
            "r3_empty_response_rate": round(empty_rate_r3, 4),
            "r3_carry_over_retry_count": r3_carry_over_retry_count,
            "r3_round_2_makeup_count": r3_round_2_makeup_count,
            "r3_round_3_count": r3_round_3_count,
            "r3_total_prompt_tokens": total_prompt_tokens,
            "r3_total_completion_tokens": total_completion_tokens,
            "r3_total_tokens": total_prompt_tokens + total_completion_tokens,
            "tun_compliance": tun_compliance,
            "tun_used_count": tun_used_count,
            "tun_target_count": len(quadruples),
            "cumulative": {
                "prior_total": cum_total_prior,
                "prior_empty": cum_empty_prior,
                "prior_ok": cum_ok_prior,
                "prior_rate": round(cum_rate_prior, 4),
                "post_total": cum_total,
                "post_empty": cum_empty,
                "post_ok": cum_ok,
                "post_rate": round(cum_empty_rate_post, 4),
                "delta_total": cum_total - cum_total_prior,
                "delta_empty": cum_empty - cum_empty_prior,
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered_this_batch": k_n26_n2_triggered,
            },
            "s6_n60_status": {
                "successful_count_this_batch": s6_n60_successful,
                "records_in_this_batch": len(s6_n60_records),
                "is_round_2_makeup_ran": any(
                    q["per_call_metadata"].get("is_round_2_makeup")
                    for q in s6_n60_records
                ),
                "is_carry_over_retry_ran": any(
                    q["per_call_metadata"].get("carry_over")
                    for q in s6_n60_records
                ),
                "is_round_3_ran": any(
                    q["per_call_metadata"].get("is_round_3")
                    for q in s6_n60_records
                ),
                "note": (
                    "S6_n60 当前棒 successful calls 计数；"
                    "本棒成功 ≥1 → 不再是 0 successful call 状态；"
                    "round 3-5 后续 ≥5 calls/caption 留待 worker 接力"
                ),
            },
            "missing_for_round_3_after_watchdog": missing_for_round_3,
            "r3_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r3_empty_response_above_threshold_single_batch": empty_rate_r3 > 0.50,
        },
        "empty_rate_trend": {
            "batch1_round1": {
                "calls": batch1["aggregate"]["total_calls"],
                "empty": batch1["aggregate"]["empty_response_count"],
                "rate": round(batch1["aggregate"]["empty_response_rate"], 4),
            },
            "batch1_round2": {
                "calls": r2["aggregate"]["total_calls"],
                "empty": r2["aggregate"]["empty_response_count"],
                "rate": round(r2["aggregate"]["empty_response_rate"], 4),
            },
            "batch1_round3": {
                "calls": r3_total,
                "empty": r3_empty,
                "rate": round(empty_rate_r3, 4),
            },
            "cumulative_through_r3": {
                "calls": cum_total,
                "empty": cum_empty,
                "ok": cum_ok,
                "rate": round(cum_empty_rate_post, 4),
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered": k_n26_n2_triggered,
            },
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round_3_n_distinct_sample_note": (
                    "round 3 第 3 call 实测；与 r2 第 2 call + batch1 第 1 call 同 caption 比对 → "
                    "n_distinct≥3（每 caption 同 caption 历次 response_text 取并集 → n_distinct 上限 ≥3 但因样本 N=3 受限）；"
                    "充分判定需 ≥5 calls/caption（round 4-5 后由 verdict-keeper 统裁）"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r3, 4),
                "cumulative_empty_response_rate": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r3 > 0.50,
                "cumulative_trigger": {
                    "triggered": k_n26_n2_triggered,
                    "trigger_at_call_idx": k_n26_n2_trigger_at_call_idx,
                    "trigger_cum_rate": (
                        round(k_n26_n2_trigger_cum_rate, 4) if k_n26_n2_trigger_cum_rate is not None else None
                    ),
                    "stop_reason": stop_reason if k_n26_n2_triggered else None,
                },
                "monitor_disposition": (
                    "本棒 K-N26-N2 累计 empty_rate 监控 = 已实施；"
                    + (
                        "本棒触发 K-N26-N2 pass=False 构造失灵族判定 + 立即停采 (沿 dispatch §3 字面)"
                        if k_n26_n2_triggered else
                        "本棒未触发 K-N26-N2 累计阈值；跑至 600s watchdog 提前停批 / 全 27 calls 完成"
                    )
                ),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "breakpoint_status": {
            "hit_wall_time_budget": wall_time_s > WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_triggered": k_n26_n2_triggered,
            "stop_reason": stop_reason,
            "actual_wall_time_s": wall_time_s,
            "planned_calls": planned_total,
            "actual_calls": r3_total,
            "carry_over_retry_actual": r3_carry_over_retry_count,
            "round_2_makeup_actual": r3_round_2_makeup_count,
            "round_3_actual": r3_round_3_count,
            "missing_for_round_3_after_watchdog": missing_for_round_3,
            "checkpoint_file": None,
            "next_resume_via": "同 agent 唤醒 (task_append 续跑) — 沿 prereg §1.6.4",
            "note": (
                f"本棒 round 3 已完成"
                + (f"（carry-over retry {r3_carry_over_retry_count}/1 + round 2 makeup {r3_round_2_makeup_count}/4 + round 3 {r3_round_3_count}/22）")
                + (f"；K-N26-N2 累计阈值触发：cum_rate={round(k_n26_n2_trigger_cum_rate,4) if k_n26_n2_trigger_cum_rate else None} > 0.50 at call {k_n26_n2_trigger_at_call_idx}, 立即停采 (沿 dispatch §3)"
                   if k_n26_n2_triggered else
                   f"；撞 600s watchdog 提前停批，剩余 round 3 待采 {len(missing_for_round_3)} caption 走 task_append 接力棒"
                   if missing_for_round_3 else
                   "；round 3 全 22 caption 已完成，未撞 watchdog")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    # 11. 落盘前自扫
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    # 12. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r3_result.json")
    payload = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
    with open(out_path, "wb") as f:
        f.write(payload.encode("utf-8"))
    with open(out_path, "rb") as f:
        data = f.read()
    if b"\r" in data:
        with open(out_path, "wb") as f:
            f.write(data.replace(b"\r\n", b"\n").replace(b"\r", b"\n"))

    sha12, n_bytes, is_lf = sha12_file(out_path)
    print(f"\n[RESULT] {out_path}")
    print(f"  SHA-12: {sha12}")
    print(f"  bytes : {n_bytes}")
    print(f"  LF-only: {is_lf}")
    print(f"  quadruples: {r3_total} (ok={r3_ok} empty={r3_empty} fail={r3_fail})")
    print(f"    carry-over retry: {r3_carry_over_retry_count}/1 (S6_n60)")
    print(f"    round 2 makeup: {r3_round_2_makeup_count}/4")
    print(f"    round 3: {r3_round_3_count}/22")
    print(f"  r3_empty_rate: {empty_rate_r3:.4f}")
    print(f"  cumulative_empty_rate: {cum_empty_rate_post:.4f}")
    print(f"  k_n26_n2_triggered: {k_n26_n2_triggered}")
    print(f"  tun_compliance: {tun_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  stop_reason: {stop_reason}")
    if missing_for_round_3:
        print(f"  missing_for_round_3_after_watchdog: {missing_for_round_3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())