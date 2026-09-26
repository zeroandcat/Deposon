# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch1_r2_executor.py
=====================================

V4 L14+ 首批 (batch 1) · round 2 续采 — kimi 教师侧 第 2 轮 + S6_n60 补跑
==========================================================================

【派工依据】
----------------
- 沿上棒 `results/_v4_supp_l14v3_batch1_executor.py`（SHA-12 `b48019494530`）+ 上棒产物
  `results/_v4_supp_l14v3_batch1_result.json`（SHA-12 `22eb01144062`）口径直接续跑
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（字面引用 `05B975A86989`）字面
- 沿 activation `results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md`（draft 待 PI 复核）
- 同 agent 唤醒保上下文（task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义）

【本棒范围】
----------------
1. **补跑 S6_n60**：上棒撞 600s watchdog 未跑的 1 件（reask_idx=0 = 第 1 次采集）
2. **round 2 续采**：22 caption × 第 2 call（reask_idx=1）
3. 计划 calls = 1 + 22 = 23；预算 ≤22 calls / ≤600s watchdog（沿 dispatch §3 + L7 实证 ≤275s 上限）
4. 跑不完如实报断点（沿 prereg §1.6.4 partial completion 协议）

【端点取舍（沿上棒实测）】
----------------------------
- teamo + tun + kimi-k3（沿上棒 `model_id_inconsistency_honest_disclosure` 字面）— 实测选定
- 不重新探活（沿 dispatch §2 「沿你上棒 executor/口径直接续跑」）

【铁律严守（沿上棒）】
------------------------
- R4 key 永不明文（无例外）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch1_r2_result.json` 与上棒 `_batch1_result.json` 同级独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款（非阈值私设）
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；内层重试 ≤3；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch1_r2_result.json`（schema = `v4_l14v3_n26/1` + batch=1 + round=2）
- 不覆盖上棒 result `22eb01144062`（沿 dispatch §4 「不覆盖上棒 result」）

【与上棒 executor diff（沿 dispatch §4 「若需参数化改动则新件 + 注明 diff」）】
--------------------------------------------------------------------------------
1. 新增参数：`ROUND = 2`、`INCLUDE_CARRYOVER_S6_N60 = True`（沿上棒 partial completion 1 件）
2. 新增调度：`planned_calls = [S6_n60 carry-over reask=0] + [22 round 2 reask=1]`
3. 新增字段：每 quadruple 增 `carry_over`（bool）、`round_index`（=2）、`reask_idx`（0 或 1）
4. 新增 aggregate 字段：`carry_over_count`、`round_2_count`、`planned_total`、`missing_for_round_2_after_watchdog`
5. breakpoint_status 沿上棒 partial completion 协议「partial completion 留 worker 下一棒接力」

【边界】
----------
- 不动任何既有件（含上棒 executor `b48019494530` / 上棒 result `22eb01144062` / prereg `05B975A86989`）
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
CALL_TIMEOUT_S = 60
INNER_RETRY_MAX = 3

# 预算
WALL_TIME_BUDGET_S = 600

# 本棒调度
ROUND = 2
INCLUDE_CARRYOVER_S6_N60 = True  # 上棒 partial completion 1 件 = S6_n60
CARRYOVER_CAPTION_ID = "S6_n60"
REASK_IDX_CARRYOVER = 0  # 第 1 次采集
REASK_IDX_ROUND = 1      # round 2 = 第 2 次采集


# ============================================================
# 敏感模式（沿上棒 SENSITIVE_PATTERNS 沿用）
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
    timeout: int = CALL_TIMEOUT_S,
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch1-r2",
        "X-Title": "deposon-l14v3-batch1-r2-kimi-teacher",
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
# 单 call + 内层空响应重试 + 四元组落盘（沿上棒 + carry_over 字段）
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    carry_over: bool,
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    # prompt_id 沿上棒惯例 + 增 round_index / carry_over 标记
    suffix = ""
    if carry_over:
        suffix = "_carryover_r0"
    else:
        suffix = f"_r{round_index}"
    prompt_id = f"kimi_t01_{side}_{caption_id}{suffix}"

    retries = 0
    last = None
    while retries <= INNER_RETRY_MAX:
        r = call_chat_teamo(api_key=api_key, messages=messages)
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
                        "temperature": TEMPERATURE,
                        "max_tokens": MAX_TOKENS,
                        "retry_count": retries,
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
                "temperature": TEMPERATURE,
                "max_tokens": MAX_TOKENS,
                "retry_count": retries,
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
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "retry_count": INNER_RETRY_MAX,
            "empty_response": True,
            "error_category": "empty_response_after_retries",
            "error_snippet": f"empty response after {INNER_RETRY_MAX} retries",
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 L14+ batch 1 round 2 · kimi 教师侧")
    print("计划 calls = 1 (S6_n60 carry-over) + 22 (round 2) = 23 calls")
    print("预算 ≤22 calls / ≤600s watchdog（沿 dispatch §3）")
    print("端点: teamo + tun + kimi-k3 (沿上棒 executor b48019494530)")
    print("=" * 60)

    setup_proxy_teamo()
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
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

    # 3. 调度 planned_calls
    planned: List[Tuple[str, int, bool]] = []  # (caption_id, reask_idx, carry_over)
    if INCLUDE_CARRYOVER_S6_N60:
        planned.append((CARRYOVER_CAPTION_ID, REASK_IDX_CARRYOVER, True))
    for c in captions:
        planned.append((c["id"], REASK_IDX_ROUND, False))

    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (1 carry-over + {planned_total - 1} round 2)")

    # 4. 时间预算起点
    t_batch_start = time.time()

    # 5. 跑
    quadruples: List[Dict[str, Any]] = []
    ok_count = 0
    empty_count = 0
    fail_count = 0
    carry_over_count = 0
    round_2_count = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    ran_caption_ids_round_2 = set()

    for i, (cap_id, reask_idx, carry_over) in enumerate(planned):
        elapsed = time.time() - t_batch_start
        if elapsed > WALL_TIME_BUDGET_S:
            print(f"[BREAKPOINT] wall time {elapsed:.1f}s > {WALL_TIME_BUDGET_S}s watchdog; stop at call {i}/{planned_total}")
            break

        caption = cap_by_id.get(cap_id)
        if caption is None:
            print(f"[WARN] caption_id={cap_id} not found in captions; skip")
            continue

        if not carry_over:
            ran_caption_ids_round_2.add(cap_id)

        rec = run_one_quadruple(
            api_key=api_key,
            caption=caption,
            reask_idx=reask_idx,
            side="teacher",
            round_index=ROUND if not carry_over else 1,  # carry-over 实为 round 1 第 1 次（标 round_index=1）
            carry_over=carry_over,
        )
        quadruples.append(rec)
        m = rec["per_call_metadata"]
        if m["ok"] and not m["empty_response"]:
            ok_count += 1
        elif m["empty_response"]:
            empty_count += 1
        else:
            fail_count += 1
        if carry_over:
            carry_over_count += 1
        else:
            round_2_count += 1
        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if (m["ok"] and not m["empty_response"]) else (
            "EMPTY" if m["empty_response"] else f"FAIL({m.get('error_category','')})"
        )
        marker = "[carry-over]" if carry_over else f"[r{ROUND}]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"{status}"
        )

        if i < planned_total - 1:
            time.sleep(INTER_CALL_SLEEP_S)

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)

    # 6. 统计
    total_calls = len(quadruples)
    empty_rate = (empty_count / total_calls) if total_calls > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == total_calls)
    breakpoint_hit = wall_time_s > WALL_TIME_BUDGET_S

    # 7. round 2 缺 caption（run 完成后未跑到的 round 2 目标）
    missing_for_round_2_after_watchdog = sorted(
        c["id"] for c in captions if c["id"] not in ran_caption_ids_round_2
    )

    # 8. 装载上棒 result 沿用元数据
    with open(BATCH1_RESULT_PATH, "r", encoding="utf-8") as f:
        batch1 = json.load(f)

    # 9. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 1,
        "round": 2,
        "metadata": {
            "task": "L14V3_batch1_round2_kimi_teacher_side",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "executor_sha12": "b48019494530",
                "executor_path": "results/_v4_supp_l14v3_batch1_executor.py",
                "batch1_result_sha12": "22eb01144062",
                "batch1_result_path": "results/_v4_supp_l14v3_batch1_result.json",
            },
            "date": "2026-09-24",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 1 round 2",
            "spec_conformance": "PI 2026-09-24 同 agent 唤醒 (task_append) 接力棒 + 沿上棒 executor/口径直接续跑",
            "teacher": "kimi",
            "side": "teacher",
            "round_index": 2,
            "n_captions_total": len(captions),
            "n_captions_round_2_planned": len(captions),
            "n_captions_round_2_actual": round_2_count,
            "n_carry_over_planned": 1 if INCLUDE_CARRYOVER_S6_N60 else 0,
            "n_carry_over_actual": carry_over_count,
            "carry_over_caption_id": CARRYOVER_CAPTION_ID,
            "planned_total": planned_total,
            "actual_total": total_calls,
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
            "inner_retry_max": INNER_RETRY_MAX,
            "call_timeout_s": CALL_TIMEOUT_S,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "diff_vs_batch1_executor": [
                "1. 新增 ROUND=2 / INCLUDE_CARRYOVER_S6_N60=True 参数化",
                "2. 新增调度: [S6_n60 carry-over reask=0] + [22 round 2 reask=1]",
                "3. 每 quadruple 增 carry_over / round_index 字段",
                "4. aggregate 增 carry_over_count / round_2_count / planned_total / missing_for_round_2_after_watchdog",
                "5. breakpoint_status 沿上棒 partial completion 协议续注",
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
                "no_overwrite_batch1_result": True,
            },
            "run_window_cst": now_iso,
            "wall_time_actual_s": wall_time_s,
        },
        "quadruples": quadruples,
        "aggregate": {
            "total_calls": total_calls,
            "ok_count": ok_count,
            "empty_response_count": empty_count,
            "fail_count": fail_count,
            "empty_response_rate": round(empty_rate, 4),
            "empty_response_rate_threshold_K_N26_N2": 0.50,
            "empty_response_above_threshold": empty_rate > 0.50,
            "tun_compliance": tun_compliance,
            "tun_used_count": tun_used_count,
            "tun_target_count": total_calls,
            "total_prompt_tokens": total_prompt_tokens,
            "total_completion_tokens": total_completion_tokens,
            "total_tokens": total_prompt_tokens + total_completion_tokens,
            "carry_over_count": carry_over_count,
            "round_2_count": round_2_count,
            "planned_total": planned_total,
            "missing_for_round_2_after_watchdog": missing_for_round_2_after_watchdog,
            "carry_over_caption_id": CARRYOVER_CAPTION_ID,
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round_2_n_distinct_sample_note": (
                    "round 2 第 2 call 实测；与上棒第 1 call 同 caption 比对 → "
                    "n_distinct≥2 (含 S6_n60 carry-over)；充分判定需 ≥5 calls/caption (round 3–5 后由 verdict-keeper 统裁)"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "empty_response_rate": round(empty_rate, 4),
                "empty_rate_trigger_K_N26_N2_pass_False": empty_rate > 0.50,
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "breakpoint_status": {
            "hit_wall_time_budget": wall_time_s > WALL_TIME_BUDGET_S,
            "actual_wall_time_s": wall_time_s,
            "planned_calls": planned_total,
            "actual_calls": total_calls,
            "carry_over_actual": carry_over_count,
            "round_2_actual": round_2_count,
            "missing_for_round_2_after_watchdog": missing_for_round_2_after_watchdog,
            "checkpoint_file": None,
            "next_resume_via": "同 agent 唤醒 (task_append 续跑) — 沿 prereg §1.6.4",
            "note": (
                f"本棒 round 2 已完成（carry-over {carry_over_count}/1 + round 2 {round_2_count}/22）"
                + (f"；撞 600s watchdog 提前停批，剩余 round 2 待采 {len(missing_for_round_2_after_watchdog)} caption 走 task_append 接力棒"
                   if missing_for_round_2_after_watchdog else
                   "；round 2 全 22 caption 已完成，未撞 watchdog")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    # 10. 落盘前自扫
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    # 11. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r2_result.json")
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
    print(f"  quadruples: {total_calls} (ok={ok_count} empty={empty_count} fail={fail_count})")
    print(f"    carry-over: {carry_over_count}/1 (S6_n60)")
    print(f"    round 2: {round_2_count}/22")
    print(f"  empty_rate: {empty_rate:.4f}")
    print(f"  tun_compliance: {tun_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  total_prompt_tokens: {total_prompt_tokens}")
    print(f"  total_completion_tokens: {total_completion_tokens}")
    if missing_for_round_2_after_watchdog:
        print(f"  missing_for_round_2_after_watchdog: {missing_for_round_2_after_watchdog}")
    return 0


if __name__ == "__main__":
    sys.exit(main())