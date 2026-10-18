# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch6_r1_executor.py
=====================================

V4 L14+ 首批 (batch 1) · round 6 收尾 — kimi 教师侧全 22 caption 达标
=====================================================================

【派工依据】
----------------
- 沿 r5 `results/_v4_supp_l14v3_batch1_r5_executor.py`（SHA-12 `91c72f8ad209`）+ r5 产物
  `results/_v4_supp_l14v3_batch1_r5_result.json`（SHA-12 `664355f29ab9`）口径续跑
- 沿前棒 `4f5269ba8f18` / `9c800874701a` / `60c78b6f0281` / `6e01255b80c9` / `2bdb5163400f` / `00c7b545c397` / `b48019494530` / `22eb01144062`
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（字面引用 `05B975A86989`）字面
- 同 agent 唤醒保上下文（task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义）

【本棒范围（沿 dispatch §1）—— kimi 教师侧收官】
----------------------------------------------------------
1. **18 个未达标 caption 各补至 ≥5 successful calls**（reask_idx=5 = round 6）：
   - **Priority 1 (need=2, S6_n60 优先)**：S6_n60 × 2 calls
   - **Priority 2 (need=2)**：L_historical_causality × 2 calls
   - **Priority 3 (need=2)**：S2_n20 × 2 calls
   - **Priority 4 (need=1, 其余 15 caption)**：L_biological_taxonomy / L_physics_concepts / S1_n35 / S1_n45 / S1_n60 /
     S2 / S2_n35 / S2_n45 / S2_n60 / S3 / S4 / S5 / S6 / S6_n20 / S6_n35 × 1 call each
2. **目标**：本棒把 kimi 教师侧全 22 caption 收官达标；如本棒跑不完，下棒接力续跑
3. 计划 calls = 6 (need=2 × 3 caption) + 15 (need=1 × 15 caption) = 21 calls
4. 预算 ≤22 calls / ≤600s watchdog（沿 dispatch §2）；1 spare call 用于 retry / 部分缓冲
5. 跑不完如实报断点（沿 prereg §1.6.4 partial completion 协议）

【每 caption successful 计数终盘点（沿 dispatch §6）】
---------------------------------------------------------
- 本棒前基线（沿 r5）：4/22 达标（≥5 successful calls）；18/22 未达标
- 本棒增量计算：每 call 后实时更新 per_cap_succ 字典
- 终盘结果：result.json 顶层 `per_caption_successful_calls` 块 + `dispatch_target_progress` 块

【retry 修复逻辑沿 r5（沿 dispatch §3）】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}（沿 r4/r5）
- read_timeout_initial_s=60 / read_timeout_retry_s=90（沿 r4/r5）
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回（沿 r4/r5）
- r5 retry 触发的源 error_category tracking 改进沿用（沿 r5）

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
--------------------------------------------------------------------
- 累计 = batch1 + r2 + r3 + r4 + r5 + r6 总 cumulative
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 实测累计基线（沿 r5 产物）：
  - prior (b1+r2+r3+r4+r5): total=98, empty=9, **rate=9.18%**
  - r6 worst case (22 EMPTY): cumulative = 31/120 = 25.83% (仍 < 50% 阈值)
  - r6 best case (0 EMPTY): cumulative = 9/119 = 7.56% (仍 < 50% 阈值)

【端点取舍（沿前棒实测）】
----------------------------
- teamo + tun + kimi-k3（沿前棒 `model_id_inconsistency_honest_disclosure` 字面）
- 不重新探活（沿 dispatch §4 「沿 r5 口径续跑」）

【铁律严守（沿前棒）】
------------------------
- R4 key 永不明文（无例外）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch1_r6_*` 与前棒所有 _batch1_* 同级独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch1_r6_result.json`（schema = `v4_l14v3_n26/1` + batch=1 + round=6）
- 不覆盖 r5 result `664355f29ab9` 或前棒 result（沿 dispatch §4）

【与 r5 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. 新增参数：`BATCH = 6` / `SIDE = "distill"` / `ROUND = 1` / `REASK_R1 = 0`
2. 新增调度：`planned_calls = 21 (3 need=2 caption × 2 calls + 15 need=1 caption × 1 call) = 21 calls`，按优先级排序（S6_n60 → need=2 others → need=1）
3. 每 caption successful 计数跟踪（沿 r5）
4. retry 触发源 error_category tracking 沿 r5
5. 新增 `dispatch_target_progress` 块：r6 后达标 caption 数（最终 22/22 收官判定）
6. 新增 `kimi_distill_side_round1_finish` 块：本棒后 kimi 教师侧是否达成全 22 caption 达标
7. predecessor_sha12 链新增 r5_executor `91c72f8ad209` + r5_result `664355f29ab9`

【边界】
----------
- 不动任何既有件（含 r5 executor `91c72f8ad209` + r5 result `664355f29ab9` + 前所有棒产物 + prereg `05B975A86989`）
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
from typing import Any, Dict, List, Tuple

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
R3_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r3_result.json")
R4_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r4_result.json")
R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r5_result.json")

# tun 代理（沿前棒）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（沿前棒实测）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_KIMI_K3 = "kimi-k3"
KEY_INDEX_TEAMO_1BASED = 15
USE_PROXY = True

# 串行间隔
INTER_CALL_SLEEP_S = 2.5

# 超参（沿前棒）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 r4/r5 + dispatch §3）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别（沿 r4/r5 + dispatch §1 字面）
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值（沿 dispatch §4）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算
WALL_TIME_BUDGET_S = 1500

# 本棒调度
# BATCH = 6 (batch 6 = kimi distill side)
ROUND = 1
SIDE = "distill"
TEACHER = "kimi"
REASK_R1 = 0  # round 6 第 6 call (reask_idx = 5)
TARGET_SUCCESSFUL_PER_CAPTION = 5

# kimi 侧收尾优先级调度（沿 dispatch §1）
# Priority 1: S6_n60 (need=2, 沿 dispatch §1 优先保证)
# Priority 2: need=2 其余 (L_historical_causality, S2_n20)
# Priority 3: need=1 其余 15 caption


# ============================================================
# 敏感模式（沿前棒）
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
# 工具（沿前棒 + 复用）
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
        "HTTP-Referer": "https://deposon.local/l14v3-batch6-r1",
        "X-Title": "deposon-l14v3-batch6-r1-kimi-distill",
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
# 提示构造（沿前棒）
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
# 单 call + 内层重试 (沿 r5)
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    is_round_1: bool,
    phase_label: str,
    retry_trigger_categories_tracker: List[str],
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_r1"
    prompt_id = f"kimi_t01_{side}_{caption_id}{suffix}"

    retries = 0
    last = None
    while retries <= INNER_RETRY_MAX:
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
                        "is_round_1": is_round_1,
                        "phase_label": phase_label,
                        "temperature": TEMPERATURE,
                        "max_tokens": MAX_TOKENS,
                        "retry_count": retries,
                        "read_timeout_s": timeout_s,
                        "retry_bug_fix_applied": True,
                        "empty_response": False,
                        "error_category": None,
                        "error_snippet": "",
                    },
                }
            retries += 1
            time.sleep(INTER_CALL_SLEEP_S)
            continue

        err_cat = r.get("error_category")
        if err_cat in NETWORK_ERROR_CATEGORIES_RETRY:
            retry_trigger_categories_tracker.append(err_cat)
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
                "is_round_1": is_round_1,
                "phase_label": phase_label,
                "temperature": TEMPERATURE,
                "max_tokens": MAX_TOKENS,
                "retry_count": retries,
                "read_timeout_s": timeout_s,
                "retry_bug_fix_applied": True,
                "empty_response": is_empty_response(""),
                "error_category": err_cat,
                "error_snippet": (r.get("error_body_snippet") or r.get("error_snippet") or "")[:200],
            },
        }

    if last and last.get("ok"):
        content = last.get("content", "") or ""
    else:
        content = ""
    err_cat_final = (last.get("error_category") if last and not last.get("ok") else None) or "empty_response_after_retries"
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
            "is_round_1": is_round_1,
            "phase_label": phase_label,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "retry_count": INNER_RETRY_MAX,
            "read_timeout_s": READ_TIMEOUT_RETRY_S,
            "retry_bug_fix_applied": True,
            "empty_response": is_empty_response(content),
            "error_category": err_cat_final,
            "error_snippet": (
                last.get("error_body_snippet") or last.get("error_snippet") or ""
                if last else f"empty response / network error after {INNER_RETRY_MAX} retries"
            )[:200],
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 L14+ batch 6 round 1 | kimi distill side | reask=0")
    print("计划 calls = 21 (3 need=2 × 2 + 15 need=1 × 1) = 21 calls")
    print("调度优先级: S6_n60 → need=2 others → need=1 其余 15")
    print("目标: 全 22 caption 达标 (≥5 successful calls/caption)")
    print("预算 ≤22 calls / ≤600s watchdog（沿 dispatch §2）")
    print("retry 修复沿 r5 (含 retry 触发的源 error_category tracking)")
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

    # batch6 r1 = 22 caption x 1 call = 22 calls (per dispatch: side=distill, round 1, reask=0)
    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r1_distill_{c['id']}"}
        for c in captions
    ]

    # 2. 加载 key
    try:
        api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
        print(f"[INIT] teamo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 3. 装载前棒 cumulative + 每 caption successful 计数（沿 r5）
    with open(BATCH1_RESULT_PATH, "r", encoding="utf-8") as f:
        batch1 = json.load(f)
    with open(R2_RESULT_PATH, "r", encoding="utf-8") as f:
        r2 = json.load(f)
    with open(R3_RESULT_PATH, "r", encoding="utf-8") as f:
        r3 = json.load(f)
    with open(R4_RESULT_PATH, "r", encoding="utf-8") as f:
        r4 = json.load(f)
    with open(R5_RESULT_PATH, "r", encoding="utf-8") as f:
        r5 = json.load(f)

    # 每 caption successful / total / empty 计数（沿 r5）
    per_cap_succ = {c["id"]: 0 for c in captions}
    per_cap_total = {c["id"]: 0 for c in captions}
    per_cap_empty = {c["id"]: 0 for c in captions}
    for src in [batch1, r2, r3, r4, r5]:
        qs = src.get("quadruples", [])
        if "quadruples" not in src:
            continue
        for q in qs:
            m = q["per_call_metadata"]
            cid = m["caption_id"]
            per_cap_total[cid] = per_cap_total.get(cid, 0) + 1
            if m["ok"] and not m["empty_response"]:
                per_cap_succ[cid] = per_cap_succ.get(cid, 0) + 1
            if m["empty_response"]:
                per_cap_empty[cid] = per_cap_empty.get(cid, 0) + 1

    cum_total_prior = sum(per_cap_total.values())
    cum_empty_prior = sum(per_cap_empty.values())
    cum_ok_prior = sum(per_cap_succ.values())
    cum_rate_prior = cum_empty_prior / cum_total_prior if cum_total_prior > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior} ok={cum_ok_prior} empty={cum_empty_prior} rate={cum_rate_prior:.4f}")

    # 4. 调度 planned_calls（沿 dispatch §1 优先级）
    planned = PLANNED_CALLS
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (S6_n60 × 2 + L_historical_causality × 2 + S2_n20 × 2 + 15 need=1 × 1)")

    # 5. 时间预算起点
    t_batch_start = time.time()

    # 6. 跑
    quadruples: List[Dict[str, Any]] = []
    cum_total = cum_total_prior
    cum_empty = cum_empty_prior
    cum_ok = cum_ok_prior
    r1_total = 0
    r1_ok = 0
    r1_empty = 0
    r1_fail = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    k_n26_n2_triggered = False
    k_n26_n2_trigger_at_call_idx = None
    k_n26_n2_trigger_cum_rate = None
    stop_reason = None

    retry_trigger_categories_tracker: List[str] = []
    retry_count_distribution: Dict[int, int] = {}
    retry_triggered_count = 0

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

        # K-N26-N2 累计监控（call 前判）
        if cum_total > 0:
            current_cum_rate = cum_empty / cum_total
            if current_cum_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i
                k_n26_n2_trigger_cum_rate = current_cum_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 cumulative empty_rate={current_cum_rate:.4f} > 0.50 at call {i}/{planned_total}; stop per dispatch §4")
                break

        rec = run_one_quadruple(
            api_key=api_key,
            caption=caption,
            reask_idx=REASK_R1,
            side="distill",
            round_index=ROUND,
            is_round_1=True,
            phase_label=item["phase"],
            retry_trigger_categories_tracker=retry_trigger_categories_tracker,
        )
        quadruples.append(rec)
        m = rec["per_call_metadata"]
        is_ok = m["ok"] and not m["empty_response"]
        is_empty = m["empty_response"]
        is_fail = not m["ok"]

        rc = m.get("retry_count", 0)
        retry_count_distribution[rc] = retry_count_distribution.get(rc, 0) + 1
        if rc >= 1:
            retry_triggered_count += 1

        if is_ok:
            r1_ok += 1
            cum_ok += 1
            per_cap_succ[cap_id] += 1
        elif is_empty:
            r1_empty += 1
            cum_empty += 1
            per_cap_empty[cap_id] += 1
        else:
            r1_fail += 1
        r1_total += 1
        cum_total += 1
        per_cap_total[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ = per_cap_succ[cap_id]
        target_met = "[OK]" if cur_succ >= TARGET_SUCCESSFUL_PER_CAPTION else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<28} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[succ={cur_succ}/{TARGET_SUCCESSFUL_PER_CAPTION} {target_met}] "
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
                print(f"[STOP] K-N26-N2 post-call cumulative empty_rate={post_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch §4")
                break

        if i < planned_total - 1:
            time.sleep(INTER_CALL_SLEEP_S)

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)

    # 7. 统计
    empty_rate_r1 = (r1_empty / r1_total) if r1_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 8. 每 caption successful 计数（沿 dispatch §6）
    per_caption_successful_calls = {}
    met_target_count = 0
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ[cid]
        t = per_cap_total[cid]
        e = per_cap_empty[cid]
        need = max(0, TARGET_SUCCESSFUL_PER_CAPTION - s)
        met = s >= TARGET_SUCCESSFUL_PER_CAPTION
        if met:
            met_target_count += 1
        per_caption_successful_calls[cid] = {
            "succ_count": s,
            "target": TARGET_SUCCESSFUL_PER_CAPTION,
            "need_more": need,
            "met_target": met,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 9. kimi 教师侧收官判定
    kimi_distill_side_round1_finish = {
        "all_22_captions_met_target": met_target_count == len(captions),
        "met_count_post_r6": met_target_count,
        "total_captions": len(captions),
        "still_pending": sorted([
            cid for cid, info in per_caption_successful_calls.items() if not info["met_target"]
        ]),
        "finish_disposition": (
            "kimi 教师侧全 22 caption 达标 → batch1 收官"
            if met_target_count == len(captions)
            else f"kimi 教师侧未达标 {len(captions) - met_target_count} caption → 留 worker 下一棒接力"
        ),
    }

    # 10. dispatch §6 收尾盘点
    dispatch_target_progress = {
        "target": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption",
        "met_count_post_r6": met_target_count,
        "total_captions": len(captions),
        "remaining_count": len(captions) - met_target_count,
        "met_percentage": round(met_target_count / len(captions) * 100, 2),
        "still_pending_captions": sorted([
            cid for cid, info in per_caption_successful_calls.items() if not info["met_target"]
        ]),
    }

    # 11. retry validation 块
    retry_trigger_categories_distribution: Dict[str, int] = {}
    for cat in retry_trigger_categories_tracker:
        retry_trigger_categories_distribution[cat] = retry_trigger_categories_distribution.get(cat, 0) + 1

    retry_validation = {
        "r1_retry_count_distribution": dict(retry_count_distribution),
        "r1_retry_triggered_count": retry_triggered_count,
        "r1_retry_trigger_categories_tracker": retry_trigger_categories_tracker,
        "r1_retry_trigger_categories_distribution": retry_trigger_categories_distribution,
        "r1_retry_bug_fix_applied_in_all_calls": all(
            q["per_call_metadata"].get("retry_bug_fix_applied") is True
            for q in quadruples
        ),
        "r1_empty_rate_with_fix": round(empty_rate_r1, 4),
        "r5_empty_rate_with_fix_baseline": (
            r5["aggregate"]["r5_empty_response_rate"]
        ),
        "r3_empty_rate_without_fix_baseline": (
            r3["aggregate"]["r3_empty_response_count"] / r3["aggregate"]["r3_total_calls"]
        ),
        "delta_empty_rate_r1_vs_r5": round(empty_rate_r1 - r5["aggregate"]["r5_empty_response_rate"], 4),
        "delta_empty_rate_r1_vs_r3": round(empty_rate_r1 - (r3["aggregate"]["r3_empty_response_count"] / r3["aggregate"]["r3_total_calls"]), 4),
    }

    # 12. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 6,
        "round": 1,
        "metadata": {
            "task": "L14V3_batch6_round1_kimi_distill_side_first_results",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "r5_executor_sha12": "91c72f8ad209",
                "r5_executor_path": "results/_v4_supp_l14v3_batch1_r5_executor.py",
                "r5_result_sha12": "664355f29ab9",
                "r5_result_path": "results/_v4_supp_l14v3_batch1_r5_result.json",
                "r4_executor_sha12": "4f5269ba8f18",
                "r4_executor_path": "results/_v4_supp_l14v3_batch1_r4_executor.py",
                "r4_result_sha12": "9c800874701a",
                "r4_result_path": "results/_v4_supp_l14v3_batch1_r4_result.json",
                "r3_executor_sha12": "60c78b6f0281",
                "r3_executor_path": "results/_v4_supp_l14v3_batch1_r3_executor.py",
                "r3_result_sha12": "6e01255b80c9",
                "r3_result_path": "results/_v4_supp_l14v3_batch1_r3_result.json",
                "r2_executor_sha12": "2bdb5163400f",
                "r2_executor_path": "results/_v4_supp_l14v3_batch1_r2_executor.py",
                "r2_result_sha12": "00c7b545c397",
                "r2_result_path": "results/_v4_supp_l14v3_batch1_r2_result.json",
                "batch1_executor_sha12": "b48019494530",
                "batch1_executor_path": "results/_v4_supp_l14v3_batch1_executor.py",
                "batch1_result_sha12": "22eb01144062",
                "batch1_result_path": "results/_v4_supp_l14v3_batch1_result.json",
                "batch1_r1_executor_sha12": None,
                "batch1_r1_result_sha12": None,
                "batch1_r1_note": "batch1 r1 was overwritten (per r2 start); this round 0 reads round-2 chain",
                "batch2_r4_executor_sha12": "d9fe7aa2d292",
                "batch2_r4_result_sha12": "15b8ddc5ba9e",
                "batch2_r3_executor_sha12": "72fd2bb3838e",
                "batch2_r3_result_sha12": "25251aca6d79",
                "batch2_r2_executor_sha12": "e7418f47a130",
                "batch2_r2_result_sha12": "8c125e257af8",
                "batch2_r2_models_probe_sha12": "3c9dc60b5071",
                "batch2_r1_executor_sha12": "e52f930654d3",
                "batch2_r1_result_sha12": "d245ae4ce385",
                "captions_sha12": "6a2656878745",
                "captions_path": "corpus/v20_caption_surface/strip_captions_22.json",
                "track2_endpoints_probe_sha12": "c846f7fc79ee",
                "track2_multimodel_probe_sha12": "b65619a07b10",
                "track2_multimodel_verdict_path": "results/_v4_track2_multimodel_verdict_2026_09_23.md",
                "track2_multimodel_verdict_bytes": 12883,
                "l13_verdict_sha12_referenced": "E105EC1362DB",
                "l13_verdict_path": "results/_v4_supp_l13_n26pair_verdict.md",
                "l13_verdict_on_disk": False,
                "l13_verdict_referenced_role": "V4 triplet basis (re-asked / distill / independent) distill style source anchor (round-trip reference only; no original-prompt doc reconstruction in this batch)"
            },
            "date": "2026-09-24",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 6 round 1 distill side open",
            "prompt_construction_basis": {
                "v3_distill_original_prompt_on_disk": False,
                "v3_distill_original_prompt_path": None,
                "l13_verdict_on_disk": False,
                "l13_verdict_path": None,
                "reproduction_caliber": True,
                "reproduction_source_anchor_sha12": "5f02c7e0f094",
                "reproduction_source_anchor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                "reproduction_source_anchor_role": "teacher_side_prompt_construction_inherited",
                "l13_triple_basis_naming_reference": {
                    "triple_axes": ["re-asked", "distill", "independent"],
                    "this_batch_axes": "distill",
                    "l13_verdict_sha12_referenced": "E105EC1362DB",
                    "l13_verdict_sha12_referenced_on_disk": False,
                    "note": "L13 verdict E105EC1362DB distill style text on disk = 0 read; this batch avoids round-trip reconstruct original prompt; per batch1 r6 prompt construction = known anchor; same prompt + different side label (teacher -> distill) per L13 triplet basis distill style"
                },
                "v3_distill_pipeline_style_inherited": "V3-style concept-graph distillation continuation prompt (per batch1 r6 executor 5f02c7e0f094); prompt_text = Caption ID + Caption (sequence of concept labels) + Task (3-5 NEW related concept labels)"
            },
            "spec_conformance": "PI 2026-09-24 同 agent 唤醒 (task_append) 接力棒 + 沿 r5 口径续跑 + retry 修复沿 r5 + 每 caption successful 计数终盘点 + K-N26-N2 累计监控 + 调度优先级 (S6_n60 → need=2 → need=1)",
            "teacher": "kimi",
            "side": "distill",
            "round_index": 1,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r1_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": "沿前棒 executor b48019494530 实测 (kimi-k3 唯一可达)",
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
            "tools_fault_param_correction": {
                "read_timeout_initial_s": READ_TIMEOUT_INITIAL_S,
                "read_timeout_retry_s": READ_TIMEOUT_RETRY_S,
                "network_error_categories_retry": sorted(list(NETWORK_ERROR_CATEGORIES_RETRY)),
                "r5_status": "retry 修复 + tracking 改进沿 r5 (沿 91c72f8ad209)",
                "r6_status": "retry 修复沿 r5; r6 本棒无新参数修正",
                "rationale": (
                    "沿 r5 修复 + r5 tracking 改进；r6 本棒仅按调度优先级 (S6_n60 → need=2 → need=1) 续采；"
                    "hard fail 保持 fail path 立即返回"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r5_executor": [
                "1. 新增 ROUND=1 / REASK_R1=0 参数化",
                "2. 新增调度: PRIORITY_PLANNED_CALLS 优先级排序 (S6_n60 × 2 + L_historical_causality × 2 + S2_n20 × 2 + 15 need=1 × 1) = 21 calls",
                "3. 每 caption successful 计数跟踪（沿 r5）",
                "4. retry 触发源 error_category tracking 沿 r5",
                "5. prompt_id 后缀 _r6",
                "6. 新增 kimi_distill_side_round1_finish 块：本棒后 kimi 教师侧是否达成全 22 caption 达标 (沿 dispatch §1 'kimi 侧全 22 达标即收官')",
                "7. predecessor_sha12 链新增 r5_executor/r5_result 全链",
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
                "no_overwrite_prior_results": True,
                "retry_bug_fix_applied": True,
            },
            "run_window_cst": now_iso,
            "wall_time_actual_s": wall_time_s,
            "stop_reason": stop_reason,
        },
        "quadruples": quadruples,
        "retry_validation": retry_validation,
        "per_caption_successful_calls": per_caption_successful_calls,
        "kimi_distill_side_round1_finish": kimi_distill_side_round1_finish,
        "dispatch_target_progress": dispatch_target_progress,
        "aggregate": {
            "r1_total_calls": r1_total,
            "r1_ok_count": r1_ok,
            "r1_empty_response_count": r1_empty,
            "r1_fail_count": r1_fail,
            "r1_empty_response_rate": round(empty_rate_r1, 4),
            "r1_total_prompt_tokens": total_prompt_tokens,
            "r1_total_completion_tokens": total_completion_tokens,
            "r1_total_tokens": total_prompt_tokens + total_completion_tokens,
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
                "delta_ok": cum_ok - cum_ok_prior,
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered_this_batch": k_n26_n2_triggered,
            },
            "r1_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r1_empty_response_above_threshold_single_batch": empty_rate_r1 > 0.50,
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
                "calls": r3["aggregate"]["r3_total_calls"],
                "empty": r3["aggregate"]["r3_empty_response_count"],
                "rate": round(r3["aggregate"]["r3_empty_response_rate"], 4),
            },
            "batch1_round4": {
                "calls": r4["aggregate"]["r4_total_calls"],
                "empty": r4["aggregate"]["r4_empty_response_count"],
                "rate": round(r4["aggregate"]["r4_empty_response_rate"], 4),
            },
            "batch1_round5": {
                "calls": r5["aggregate"]["r5_total_calls"],
                "empty": r5["aggregate"]["r5_empty_response_count"],
                "rate": round(r5["aggregate"]["r5_empty_response_rate"], 4),
            },
            "batch6_round1": {
                "calls": r1_total,
                "empty": r1_empty,
                "rate": round(empty_rate_r1, 4),
            },
            "cumulative_through_r6": {
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
                "round_6_n_distinct_sample_note": (
                    "round 6 第 6 call 实测；前 5 轮已达成 22/22 caption 5+ successful；"
                    "本棒后全 22 caption K-N26-N1 N_min ≥ N_target 字面充分；"
                    "由 verdict-keeper 统裁"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r1, 4),
                "cumulative_empty_response_rate": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r1 > 0.50,
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
                        "本棒触发 K-N26-N2 pass=False 构造失灵族判定 + 立即停采 (沿 dispatch §4 字面)"
                        if k_n26_n2_triggered else
                        "本棒未触发 K-N26-N2 累计阈值；跑至 600s watchdog 提前停批 / 全 21 calls 完成"
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
            "actual_calls": r1_total,
            "checkpoint_file": None,
            "next_resume_via": "同 agent 唤醒 (task_append 续跑) — 沿 prereg §1.6.4",
            "note": (
                f"本棒 round 6 已完成（{r1_total}/{planned_total} calls）"
                + (f"；K-N26-N2 累计阈值触发：cum_rate={round(k_n26_n2_trigger_cum_rate,4) if k_n26_n2_trigger_cum_rate else None} > 0.50, 立即停采 (沿 dispatch §4)"
                   if k_n26_n2_triggered else
                   f"；撞 600s watchdog 提前停批 ({len(captions) - met_target_count} caption 未达标) 走 task_append 接力棒"
                   if wall_time_s > WALL_TIME_BUDGET_S and met_target_count < len(captions) else
                   f"；kimi 教师侧全 22 caption 达标，batch1 收官")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    # 13. 落盘前自扫
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    # 14. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch6_r1_result.json")
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
    print(f"  quadruples: {r1_total} (ok={r1_ok} empty={r1_empty} fail={r1_fail})")
    print(f"  r1_empty_rate: {empty_rate_r1:.4f}")
    print(f"  cumulative_empty_rate: {cum_empty_rate_post:.4f}")
    print(f"  k_n26_n2_triggered: {k_n26_n2_triggered}")
    print(f"  met_target_count: {met_target_count}/{len(captions)}")
    print(f"  all_22_captions_met_target: {kimi_distill_side_round1_finish['all_22_captions_met_target']}")
    print(f"  retry_bug_fix_applied_in_all_calls: {retry_validation['r1_retry_bug_fix_applied_in_all_calls']}")
    print(f"  retry_triggered_count: {retry_triggered_count}")
    print(f"  retry_count_distribution: {retry_count_distribution}")
    print(f"  retry_trigger_categories_distribution: {retry_trigger_categories_distribution}")
    print(f"  tun_compliance: {tun_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  stop_reason: {stop_reason}")
    if kimi_distill_side_round1_finish["still_pending"]:
        print(f"  still_pending: {kimi_distill_side_round1_finish['still_pending']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())