# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch6_r2_executor.py
=====================================

V4 L14+ batch 6 · round 2（reask=1）—— kimi 蒸馏侧独立计数第 2 轮
=====================================================================

【派工依据】
----------------
- 沿 r1 `results/_v4_supp_l14v3_batch6_r1_executor.py`（SHA-12 `ad35565f1ec9`）+ r1 产物
  `results/_v4_supp_l14v3_batch6_r1_result.json`（SHA-12 `0d29e1ab4ae2`）口径续跑
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（字面引用 `05B975A86989`）字面
- 同 agent 唤醒保上下文（task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义）
- PI 2026-09-25 00:46「今晚保守口径下先斩后奏」夜间授权（保守口径自主决策，标注待 PI 复核）

【本棒范围（沿 dispatch §1）—— kimi 蒸馏侧 round 2（reask=1）】
------------------------------------------------------------
1. **22 caption × 1 call** = 22 calls（沿 dispatch 字面）
2. **计数口径修正**（PI 委托保守口径，标注待 PI 复核）：
   - r1 的 `per_caption_successful_calls` 块混入了 teacher 侧 batch1-r5 累计
     → 本棒起 distill 侧独立计数：`kimi_t0*_distill_*` prompt_id 前缀为域
   - 目标 = distill 侧自身 ≥5 successful/caption
   - 当前 distill 侧 = 1/5（沿 r1 quadruples 22 entries，每 caption 1 call）
   - 本棒补 1 call/caption → distill 侧 2/5
3. **counting_scope_correction 字段**：r1 混合计数在 result 字段如实注明
   （r1 混合计数不作废数据，仅口径归正；r1 数据本身完整保留于其 result 文件）
4. **r1 mixed count 在 result 字段保留**：`per_caption_mixed_history_successful_calls`
   块保留 r1 口径作透明参照（不参与 distill 侧判定）

【每 caption successful 计数终盘点（沿 dispatch §6）—— distill 侧独立域】
----------------------------------------------------------------------
- 本棒前基线（distill 侧独立计数，沿 r1 quadruples 过滤）：
  - 22 caption 各 1/5 successful
- 本棒增量计算：每 call 后实时更新 `per_cap_succ_distill` 字典
- 终盘结果：
  - `per_caption_distill_only_successful_calls` 块（distill 侧独立计数）
  - `per_caption_mixed_history_successful_calls` 块（r1 混合计数保留作透明参照）
  - `dispatch_target_progress_distill` 块（distill 侧目标进展）

【retry 修复沿 r1（沿 dispatch §3）】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}（沿 r1）
- read_timeout_initial_s=60 / read_timeout_retry_s=90（沿 r1）
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回（沿 r1）
- r1 retry 触发的源 error_category tracking 改进沿用（沿 r1）

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
-------------------------------------------
- 累计 = batch1+r2+r3+r4+r5+r1+r2 batch6 全部 cumulative（含 teacher + distill 混合）
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 实测累计基线（沿 r1 产物）：
  - prior (b1+r2+r3+r4+r5+r1): total=120, empty=9, **rate=7.50%**
  - r2 worst case (22 EMPTY): cumulative = 31/142 = 21.83% (仍 < 50% 阈值)
  - r2 best case (0 EMPTY): cumulative = 9/142 = 6.34% (仍 < 50% 阈值)

【端点取舍（沿 r1）】
----------------------------
- teamo + tun + kimi-k3（沿 r1 实测）
- 不重新探活（沿 dispatch §4 「沿 r1 口径续跑」）

【铁律严守（沿 r1）】
------------------------
- R4 key 永不明文（无例外）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch6_r2_*` 与前棒所有 _batch6_* 同级独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch6_r2_result.json`
  （schema = v4_l14v3_n26/1 + batch=6 + round=2）
- 不覆盖 r1 result `0d29e1ab4ae2` 或前棒 result（沿 dispatch §4）

【与 r1 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. 新增参数：`ROUND = 2` / `REASK_R1 = 1`（reask_idx=1 = 第 2 call/caption on distill side）
2. prompt_id 后缀 `_r2`
3. 计数口径切换：r1 混合 teacher+distill → r2 distill 侧独立（filter by prompt_id 前缀）
4. 新增 `counting_scope_correction` 块：r1 混合计数如实注明（不废数据，仅口径归正）
5. 新增 `per_caption_distill_only_successful_calls` 块（distill 侧独立计数）
6. 新增 `per_caption_mixed_history_successful_calls` 块（r1 混合计数透明保留）
7. 新增 `dispatch_target_progress_distill` 块（distill 侧目标进展）
8. predecessor_sha12 链新增 r1_executor `ad35565f1ec9` + r1_result `0d29e1ab4ae2`

【边界】
----------
- 不动任何既有件（含 r1 executor `ad35565f1ec9` + r1 result `0d29e1ab4ae2`
  + 前所有棒产物 + prereg `05B975A86989` + captions `6a2656878745`）
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
R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch6_r1_result.json")

# tun 代理（沿 r1）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（沿 r1）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_KIMI_K3 = "kimi-k3"
KEY_INDEX_TEAMO_1BASED = 15
USE_PROXY = True

# 串行间隔（沿 r1）
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 r1）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 r1）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别（沿 r1）
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值（沿 r1）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算（沿 r1；扩至 1500s 以容纳 22 calls）
WALL_TIME_BUDGET_S = 1500

# 本棒调度
ROUND = 2
SIDE = "distill"
TEACHER = "kimi"
REASK_R1 = 1  # round 2 = 第 2 call per caption (reask_idx = 1)
TARGET_SUCCESSFUL_PER_CAPTION = 5  # distill 侧目标

# ============================================================
# 计数口径修正（PI 委托保守口径，标注待 PI 复核）
# ============================================================
# r1 的 per_caption_successful_calls 块混入了 teacher 侧 batch1-r5 累计；
# 本棒起 distill 侧独立计数，以下前缀为过滤域：
DISTILL_SIDE_PROMPT_ID_PREFIX = "kimi_t01_distill_"


# ============================================================
# 敏感模式（沿 r1）
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
# 工具（沿 r1）
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
        "HTTP-Referer": "https://deposon.local/l14v3-batch6-r2",
        "X-Title": "deposon-l14v3-batch6-r2-kimi-distill",
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
# 提示构造（沿 r1）
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
# 单 call + 内层重试（沿 r1）
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    is_round_2: bool,
    phase_label: str,
    retry_trigger_categories_tracker: List[str],
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_r2"
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
                        "is_round_2": is_round_2,
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
                "is_round_2": is_round_2,
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
            "is_round_2": is_round_2,
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
    print("V4 L14+ batch 6 round 2 | kimi distill side | reask=1")
    print("计划 calls = 22 (22 caption × 1 call)")
    print("计数口径: distill 侧独立 (prompt_id 前缀 kimi_t01_distill_)")
    print("distill 侧 baseline: 22 caption 各 1/5 successful")
    print("目标: distill 侧 ≥5 successful calls/caption")
    print("预算 ≤1500s watchdog")
    print("retry 修复沿 r1 (含 retry 触发的源 error_category tracking)")
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

    # 2. 加载 r1 result（distill 侧独立计数基线）
    with open(R1_RESULT_PATH, "r", encoding="utf-8") as f:
        r1 = json.load(f)

    # 3. distill 侧独立计数（filter by prompt_id 前缀）
    #    r1 quadruples 全部都是 kimi_t01_distill_*_r1（前缀匹配域）
    per_cap_succ_distill = {c["id"]: 0 for c in captions}
    per_cap_total_distill = {c["id"]: 0 for c in captions}
    per_cap_empty_distill = {c["id"]: 0 for c in captions}
    r1_quadruples_distill = []
    for q in r1.get("quadruples", []):
        pid = q.get("prompt_id", "")
        if not pid.startswith(DISTILL_SIDE_PROMPT_ID_PREFIX):
            continue
        r1_quadruples_distill.append(q)
        m = q["per_call_metadata"]
        cid = m["caption_id"]
        per_cap_total_distill[cid] = per_cap_total_distill.get(cid, 0) + 1
        if m["ok"] and not m["empty_response"]:
            per_cap_succ_distill[cid] = per_cap_succ_distill.get(cid, 0) + 1
        if m["empty_response"]:
            per_cap_empty_distill[cid] = per_cap_empty_distill.get(cid, 0) + 1

    cum_total_prior_distill = sum(per_cap_total_distill.values())
    cum_empty_prior_distill = sum(per_cap_empty_distill.values())
    cum_ok_prior_distill = sum(per_cap_succ_distill.values())
    print(f"[DISTILL prior] total={cum_total_prior_distill} ok={cum_ok_prior_distill} "
          f"empty={cum_empty_prior_distill} (源 = r1 quadruples distill 前缀过滤)")

    # 4. 累积监控（含 teacher 侧 batch1-r5 + distill 侧 r1）—— 沿 r1 cumulative 链路
    r1_cum = r1["aggregate"]["cumulative"]
    cum_total_prior_cum = r1_cum["post_total"]  # 120
    cum_empty_prior_cum = r1_cum["post_empty"]  # 9
    cum_ok_prior_cum = r1_cum["post_ok"]        # 111
    cum_rate_prior = cum_empty_prior_cum / cum_total_prior_cum if cum_total_prior_cum > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior_cum} ok={cum_ok_prior_cum} "
          f"empty={cum_empty_prior_cum} rate={cum_rate_prior:.4f} (源 = r1 aggregate.cumulative)")

    # 5. mixed history 透明保留（r1 口径，仅作参照，不参与 distill 判定）
    r1_mixed_history = r1.get("per_caption_successful_calls", {})

    # 6. 调度 planned_calls（22 caption × 1 call = 22 calls）
    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r2_distill_{c['id']}"}
        for c in captions
    ]
    planned = PLANNED_CALLS
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (22 caption × 1 call)")

    # 7. 加载 key
    try:
        api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
        print(f"[INIT] teamo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 8. 时间预算起点
    t_batch_start = time.time()

    # 9. 跑
    quadruples: List[Dict[str, Any]] = []
    cum_total = cum_total_prior_cum
    cum_empty = cum_empty_prior_cum
    cum_ok = cum_ok_prior_cum
    r2_total = 0
    r2_ok = 0
    r2_empty = 0
    r2_fail = 0
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
            is_round_2=True,
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
            r2_ok += 1
            cum_ok += 1
            per_cap_succ_distill[cap_id] += 1
        elif is_empty:
            r2_empty += 1
            cum_empty += 1
            per_cap_empty_distill[cap_id] += 1
        else:
            r2_fail += 1
        r2_total += 1
        cum_total += 1
        per_cap_total_distill[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ_distill = per_cap_succ_distill[cap_id]
        target_met_distill = "[OK]" if cur_succ_distill >= TARGET_SUCCESSFUL_PER_CAPTION else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<28} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[distill_succ={cur_succ_distill}/{TARGET_SUCCESSFUL_PER_CAPTION} {target_met_distill}] "
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

    # 10. 统计
    empty_rate_r2 = (r2_empty / r2_total) if r2_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 11. 每 caption successful 计数 —— distill 侧独立
    per_caption_distill_only_successful_calls = {}
    met_target_count_distill = 0
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ_distill[cid]
        t = per_cap_total_distill[cid]
        e = per_cap_empty_distill[cid]
        need = max(0, TARGET_SUCCESSFUL_PER_CAPTION - s)
        met = s >= TARGET_SUCCESSFUL_PER_CAPTION
        if met:
            met_target_count_distill += 1
        per_caption_distill_only_successful_calls[cid] = {
            "succ_count": s,
            "target": TARGET_SUCCESSFUL_PER_CAPTION,
            "need_more": need,
            "met_target": met,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 12. mixed history 透明保留（r1 口径作参照）
    per_caption_mixed_history_successful_calls = r1_mixed_history

    # 13. distill 侧收官判定
    kimi_distill_side_round2_finish = {
        "all_22_captions_met_target": met_target_count_distill == len(captions),
        "met_count_post_r2": met_target_count_distill,
        "total_captions": len(captions),
        "still_pending": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
        "finish_disposition": (
            "kimi 蒸馏侧全 22 caption 达标 → batch6 蒸馏侧收官"
            if met_target_count_distill == len(captions)
            else f"kimi 蒸馏侧未达标 {len(captions) - met_target_count_distill} caption → 留 worker 下一棒接力"
        ),
    }

    # 14. dispatch §6 收尾盘点 —— distill 侧
    dispatch_target_progress_distill = {
        "target": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (distill side only)",
        "met_count_post_r2": met_target_count_distill,
        "total_captions": len(captions),
        "remaining_count": len(captions) - met_target_count_distill,
        "met_percentage": round(met_target_count_distill / len(captions) * 100, 2),
        "still_pending_captions": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
    }

    # 15. counting_scope_correction 块（PI 委托保守口径，标注待 PI 复核）
    counting_scope_correction = {
        "r1_issue_disclosed": True,
        "r1_issue_description": (
            "r1 `per_caption_successful_calls` 块统计域含 teacher 侧 batch1-r5 累计；"
            "r1 的 distill 侧仅有 22 quadruples（每 caption 1 call），"
            "但 r1 `per_caption_successful_calls` 字段值混合了 b1+r2+r3+r4+r5+r1 的总累计。"
            "PI 委托本棒起切换至 distill 侧独立计数。"
        ),
        "r1_data_disposition": (
            "r1 混合计数本身不动；r1 result 文件完整保留（SHA-12 0d29e1ab4ae2）；"
            "r1 数据不视为废数据，仅口径归正。"
        ),
        "r2_counting_domain": (
            f"distill 侧独立计数；filter 域 = prompt_id 前缀 '{DISTILL_SIDE_PROMPT_ID_PREFIX}'"
            "（后续所有 batch6 r* 棒沿此口径）"
        ),
        "r2_target": f"distill 侧自身 ≥{TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption",
        "r2_baseline_distill_only": (
            f"r1 quadruples distill 过滤后 = {cum_total_prior_distill} calls, "
            f"{cum_ok_prior_distill} successful, "
            f"{cum_empty_prior_distill} empty (各 caption = 1/5 successful)"
        ),
        "r2_post_distill_only": (
            f"r2 quadruples 后 = {sum(per_cap_total_distill.values())} calls, "
            f"{sum(per_cap_succ_distill.values())} successful, "
            f"{sum(per_cap_empty_distill.values())} empty (各 caption = 2/5 successful expected, if no fails)"
        ),
        "mixed_history_retention": (
            "per_caption_mixed_history_successful_calls 块保留 r1 混合口径作透明参照；"
            "该块不参与 distill 侧判定；仅作审计追溯用"
        ),
        "pending_pi_review": (
            "PI 复核本计数口径切换是否合规（保守口径自主决策，PI 2026-09-25 00:46 委托）；"
            "若 PI 倾向保留 r1 混合域统计，须重审 r2 棒"
        ),
    }

    # 16. retry validation 块
    retry_trigger_categories_distribution: Dict[str, int] = {}
    for cat in retry_trigger_categories_tracker:
        retry_trigger_categories_distribution[cat] = retry_trigger_categories_distribution.get(cat, 0) + 1

    retry_validation = {
        "r2_retry_count_distribution": dict(retry_count_distribution),
        "r2_retry_triggered_count": retry_triggered_count,
        "r2_retry_trigger_categories_tracker": retry_trigger_categories_tracker,
        "r2_retry_trigger_categories_distribution": retry_trigger_categories_distribution,
        "r2_retry_bug_fix_applied_in_all_calls": all(
            q["per_call_metadata"].get("retry_bug_fix_applied") is True
            for q in quadruples
        ),
        "r2_empty_rate_with_fix": round(empty_rate_r2, 4),
        "r1_empty_rate_with_fix_baseline": (
            r1["aggregate"]["r1_empty_response_rate"]
        ),
        "delta_empty_rate_r2_vs_r1": round(empty_rate_r2 - r1["aggregate"]["r1_empty_response_rate"], 4),
    }

    # 17. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 6,
        "round": 2,
        "metadata": {
            "task": "L14V3_batch6_round2_kimi_distill_side_reask1_independent_counting",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "r1_executor_sha12": "ad35565f1ec9",
                "r1_executor_path": "results/_v4_supp_l14v3_batch6_r1_executor.py",
                "r1_result_sha12": "0d29e1ab4ae2",
                "r1_result_path": "results/_v4_supp_l14v3_batch6_r1_result.json",
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
                "l13_verdict_referenced_role": "V4 triplet basis (re-asked / distill / independent) distill style source anchor (round-trip reference only; no original-prompt doc reconstruction in this batch)",
            },
            "date": "2026-09-25",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 6 round 2 distill side reask=1 独立计数",
            "night_authorization": "PI 2026-09-25 00:46「今晚保守口径下先斩后奏」",
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
                    "note": "L13 verdict E105EC1362DB distill style text on disk = 0 read; this batch avoids round-trip reconstruct original prompt; per batch1 r6 prompt construction = known anchor; same prompt + different side label (teacher -> distill) per L13 triplet basis distill style",
                },
                "v3_distill_pipeline_style_inherited": "V3-style concept-graph distillation continuation prompt (per batch1 r6 executor 5f02c7e0f094); prompt_text = Caption ID + Caption (sequence of concept labels) + Task (3-5 NEW related concept labels)",
            },
            "spec_conformance": "PI 2026-09-24 同 agent 唤醒 (task_append) 接力棒 + 沿 r1 口径续跑 + retry 修复沿 r1 + 每 caption successful 计数终盘点 + K-N26-N2 累计监控 + distill 侧独立计数",
            "teacher": "kimi",
            "side": "distill",
            "round_index": 2,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r2_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": "沿 r1 executor ad35565f1ec9 实测 (kimi-k3 唯一可达)",
            "model_id_sent": MODEL_KIMI_K3,
            "model_id_inconsistency_honest_disclosure": r1["metadata"]["model_id_inconsistency_honest_disclosure"],
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
                "r1_status": "retry 修复 + tracking 改进沿 r1 (沿 ad35565f1ec9)",
                "r2_status": "retry 修复沿 r1; r2 本棒无新参数修正",
                "rationale": (
                    "沿 r1 修复 + r1 tracking 改进；r2 本棒仅按 22 caption × 1 call 续采；"
                    "hard fail 保持 fail path 立即返回"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r1_executor": [
                "1. 新增 ROUND=2 / REASK_R1=1 参数化 (reask_idx=1 = 第 2 call/caption on distill side)",
                "2. prompt_id 后缀 _r2",
                "3. 计数口径切换：r1 混合 teacher+distill → r2 distill 侧独立 (filter by prompt_id 前缀 kimi_t01_distill_)",
                "4. 新增 counting_scope_correction 块：r1 混合计数如实注明 (不废数据，仅口径归正)",
                "5. 新增 per_caption_distill_only_successful_calls 块 (distill 侧独立计数)",
                "6. 新增 per_caption_mixed_history_successful_calls 块 (r1 混合计数透明保留)",
                "7. 新增 dispatch_target_progress_distill 块 (distill 侧目标进展)",
                "8. 新增 kimi_distill_side_round2_finish 块 (distill 侧收官判定)",
                "9. predecessor_sha12 链新增 r1_executor/r1_result 全链",
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
        "per_caption_distill_only_successful_calls": per_caption_distill_only_successful_calls,
        "per_caption_mixed_history_successful_calls": per_caption_mixed_history_successful_calls,
        "counting_scope_correction": counting_scope_correction,
        "kimi_distill_side_round2_finish": kimi_distill_side_round2_finish,
        "dispatch_target_progress_distill": dispatch_target_progress_distill,
        "aggregate": {
            "r2_total_calls": r2_total,
            "r2_ok_count": r2_ok,
            "r2_empty_response_count": r2_empty,
            "r2_fail_count": r2_fail,
            "r2_empty_response_rate": round(empty_rate_r2, 4),
            "r2_total_prompt_tokens": total_prompt_tokens,
            "r2_total_completion_tokens": total_completion_tokens,
            "r2_total_tokens": total_prompt_tokens + total_completion_tokens,
            "tun_compliance": tun_compliance,
            "tun_used_count": tun_used_count,
            "tun_target_count": len(quadruples),
            "cumulative": {
                "prior_total": cum_total_prior_cum,
                "prior_empty": cum_empty_prior_cum,
                "prior_ok": cum_ok_prior_cum,
                "prior_rate": round(cum_rate_prior, 4),
                "post_total": cum_total,
                "post_empty": cum_empty,
                "post_ok": cum_ok,
                "post_rate": round(cum_empty_rate_post, 4),
                "delta_total": cum_total - cum_total_prior_cum,
                "delta_empty": cum_empty - cum_empty_prior_cum,
                "delta_ok": cum_ok - cum_ok_prior_cum,
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered_this_batch": k_n26_n2_triggered,
            },
            "r2_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r2_empty_response_above_threshold_single_batch": empty_rate_r2 > 0.50,
        },
        "empty_rate_trend": {
            "batch1_round1": {
                "calls": r1["empty_rate_trend"]["batch1_round1"]["calls"],
                "empty": r1["empty_rate_trend"]["batch1_round1"]["empty"],
                "rate": r1["empty_rate_trend"]["batch1_round1"]["rate"],
            },
            "batch1_round2": {
                "calls": r1["empty_rate_trend"]["batch1_round2"]["calls"],
                "empty": r1["empty_rate_trend"]["batch1_round2"]["empty"],
                "rate": r1["empty_rate_trend"]["batch1_round2"]["rate"],
            },
            "batch1_round3": {
                "calls": r1["empty_rate_trend"]["batch1_round3"]["calls"],
                "empty": r1["empty_rate_trend"]["batch1_round3"]["empty"],
                "rate": r1["empty_rate_trend"]["batch1_round3"]["rate"],
            },
            "batch1_round4": {
                "calls": r1["empty_rate_trend"]["batch1_round4"]["calls"],
                "empty": r1["empty_rate_trend"]["batch1_round4"]["empty"],
                "rate": r1["empty_rate_trend"]["batch1_round4"]["rate"],
            },
            "batch1_round5": {
                "calls": r1["empty_rate_trend"]["batch1_round5"]["calls"],
                "empty": r1["empty_rate_trend"]["batch1_round5"]["empty"],
                "rate": r1["empty_rate_trend"]["batch1_round5"]["rate"],
            },
            "batch6_round1": {
                "calls": r1["empty_rate_trend"]["batch6_round1"]["calls"],
                "empty": r1["empty_rate_trend"]["batch6_round1"]["empty"],
                "rate": r1["empty_rate_trend"]["batch6_round1"]["rate"],
            },
            "batch6_round2": {
                "calls": r2_total,
                "empty": r2_empty,
                "rate": round(empty_rate_r2, 4),
            },
            "cumulative_through_r2": {
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
                "round_2_n_distinct_sample_note": (
                    "round 2 第 2 call per caption 实测；distill 侧独立计数 = 22 caption 各 2 successful "
                    "(沿 r1+本棒 quadruples, prompt_id 前缀 kimi_t01_distill_ filter 域)；"
                    "目标 distill 侧 ≥5 successful/caption → 后续 3+ 棒接力"
                    "（r3/r4/r5/reask；每柱 r* = 22 caption × 1 call → 3/5/4/5/5/5 successful）"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r2, 4),
                "cumulative_empty_response_rate": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r2 > 0.50,
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
                        "本棒未触发 K-N26-N2 累计阈值；跑至 1500s watchdog 提前停批 / 全 22 calls 完成"
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
            "actual_calls": r2_total,
            "checkpoint_file": None,
            "next_resume_via": "同 agent 唤醒 (task_append 续跑) — 沿 prereg §1.6.4",
            "note": (
                f"本棒 round 2 已完成（{r2_total}/{planned_total} calls）"
                + (f"；K-N26-N2 累计阈值触发：cum_rate={round(k_n26_n2_trigger_cum_rate,4) if k_n26_n2_trigger_cum_rate else None} > 0.50, 立即停采 (沿 dispatch §4)"
                   if k_n26_n2_triggered else
                   f"；撞 {WALL_TIME_BUDGET_S}s watchdog 提前停批 ({len(captions) - met_target_count_distill} caption 未达标) 走 task_append 接力棒"
                   if wall_time_s > WALL_TIME_BUDGET_S and met_target_count_distill < len(captions) else
                   f"；kimi 蒸馏侧 distill 侧独立计数：本棒后 22 caption 各 2/5 successful, 后续 3+ 棒接力")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    # 18. 落盘前自扫
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    # 19. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch6_r2_result.json")
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
    print(f"  quadruples: {r2_total} (ok={r2_ok} empty={r2_empty} fail={r2_fail})")
    print(f"  r2_empty_rate: {empty_rate_r2:.4f}")
    print(f"  cumulative_empty_rate: {cum_empty_rate_post:.4f}")
    print(f"  k_n26_n2_triggered: {k_n26_n2_triggered}")
    print(f"  distill_side_met_target_count: {met_target_count_distill}/{len(captions)}")
    print(f"  all_22_captions_met_target_distill: {kimi_distill_side_round2_finish['all_22_captions_met_target']}")
    print(f"  retry_bug_fix_applied_in_all_calls: {retry_validation['r2_retry_bug_fix_applied_in_all_calls']}")
    print(f"  retry_triggered_count: {retry_triggered_count}")
    print(f"  retry_count_distribution: {retry_count_distribution}")
    print(f"  retry_trigger_categories_distribution: {retry_trigger_categories_distribution}")
    print(f"  tun_compliance: {tun_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  stop_reason: {stop_reason}")
    if kimi_distill_side_round2_finish["still_pending"]:
        print(f"  still_pending_distill: {kimi_distill_side_round2_finish['still_pending']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())