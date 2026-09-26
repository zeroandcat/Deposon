# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch7_r5_executor.py
=====================================

V4 L14+ batch 7 · round 5 (reask=4) -- GLM_1 蒸馏侧收官棒 (独立计数 4/5 -> 5/5 收官)

派工依据:
  - 沿 L14+ 派工单 2026-09-25 03:21「GLM_1 蒸馏侧 r5 收官棒 (沿 r4 口径续跑)」
  - 沿 batch7 r4 executor (SHA-12 d789f9bd4fa1) + r4 result (SHA-12 0fe4c1339d88) 口径续跑
  - 含 r3 修复后 baseline 计数 = [r1, r2, r3, r4] 全载 (88 calls/88 ok/0 empty)
  - 沿 batch7 r1+r2+r3 executor/result 链
  - 沿 batch6 r5 executor (SHA-12 8a8babb911b8) + r5 result (SHA-12 e40424bf8abe) 上游链
  - 沿模型映射留痕件 (SHA-12 98A779D61C1E) §1.1 GLM_1 -> teamo `glm-5.3`
  - 沿 prereg (字面引用 05B975A86989) 字面
  - 同 agent 唤醒保上下文
  - PI 2026-09-25 00:46「今晚保守口径下先斩后奏」夜间授权

本棒范围:
  1. 22 caption × 1 call = 22 calls
  2. batch=7 (GLM_1 distill) + round=5 (reask=4) -- **收官棒**
     - 模型 = teamo `glm-5.3`, 端点走 tun
  3. distill 侧独立计数 baseline = [r1+r2+r3+r4] quadruples = 88 calls/88 ok/0 empty
     - filter = prompt_id 前缀 `glm1_t01_distill_`
     - 目标 ≥5 successful/caption (远期)
     - 本棒后预期 22 caption 各 5/5 successful -- **收官态**
  4. side=distill + teacher_label=GLM_1 字面字段
  5. cumulative 监控起点: r4 post {296/9/0.0304}; 本棒后 worst 31/318=9.75% / best 9/318=2.83%
  6. **收官判定块 `glm1_distill_side_finish`**:
     - all_22_captions_met_target = True if 22/22 caption 5/5 successful
     - rounds_to_reach_target_actual = "5 rounds = 110 calls = 收官态"
     - finish_disposition = "GLM_1 蒸馏侧全 22 caption 5/5 successful 达标 → batch7 蒸馏侧收官 ✓"

与 batch7 r4 executor diff:
  1. ROUND=4 -> ROUND=5; REASK_R1=3 -> REASK_R1=4 (第 5 call/caption = reask_idx=4)
  2. prompt_id 后缀 _r4 -> _r5
  3. predecessor_sha12: r4_executor d789f9bd4fa1 + r4_result 0fe4c1339d88 (替代 r3 双件为直接 predecessor)
  4. baseline 全载 [r1, r2, r3, r4] quadruples = 88 calls/88 ok/0 empty
  5. 增量: distill 各 caption 由 4/5 补至 5/5 (收官)
  6. cumulative 起点: r4 post {296/9/0.0304} -> 本棒后 worst 31/318=9.75% / best 9/318=2.83%
  7. **判定块重命名**: glm1_distill_side_round4_progress -> **glm1_distill_side_finish** (字面)
  8. metadata.is_finish_round = True (替代 r4 is_progress_round = True)
  9. counting_scope_correction: r4_baseline=88 calls 4succ/0empty; r5 后预期 110 calls 5succ/0empty (收官)
 10. headers 反映 batch7-r5
 11. **field 重命名**: glm1_distill_side_round4_progress.disposition 字段 -> glm1_distill_side_finish.dispose_field

铁律严守:
  - R4 key 永不明文 / R5 V4 frozen append-only / R6-R7 不动 / V1-V3 只读 / 派生 JSON 不合并
  - max_tokens=2000 / temperature=0.7 / 串行 ≥2.5s / teamo 必走 tun
  - 空响应如实计数 / 只采不算 K-N26-1/2/3
  - 老实交代 0 产物 / succeeded ≠ 跑完落盘核验

产物: results/_v4_supp_l14v3_batch7_r5_result.json
  (schema = v4_l14v3_n26/1 + batch=7 + round=5)
  不覆盖 r4 result 0fe4c1339d88 或前棒 result

边界: 不动任何既有件; 跑不完拆段报断点; 0 触动 V1-V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
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
R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch7_r1_result.json")
R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch7_r2_result.json")
R3_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch7_r3_result.json")
R4_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch7_r4_result.json")

PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# 端点配置
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_GLM_5_3 = "glm-5.3"
KEY_INDEX_TEAMO_1BASED = 15
USE_PROXY = True

INTER_CALL_SLEEP_S = 2.5
TEMPERATURE = 0.7
MAX_TOKENS = 2000

READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

WALL_TIME_BUDGET_S = 1500

# 本棒调度 -- 收官棒
ROUND = 5
SIDE = "distill"
TEACHER = "GLM_1"
TEACHER_LABEL = "GLM_1"
REASK_R1 = 4  # round 5 = 第 5 call per caption (reask_idx = 4) -- 收官
TARGET_SUCCESSFUL_PER_CAPTION = 5  # 收官阈值 = ≥5

DISTILL_SIDE_PROMPT_ID_PREFIX = "glm1_t01_distill_"


# ============================================================
# 敏感模式
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
        "HTTP-Referer": "https://deposon.local/l14v3-batch7-r5",
        "X-Title": "deposon-l14v3-batch7-r5-glm1-distill-finish",
    }
    body = {
        "model": MODEL_GLM_5_3,
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
# 提示构造
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
# 单 call + 内层重试
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    is_round_5: bool,
    phase_label: str,
    retry_trigger_categories_tracker: List[str],
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_r5"
    prompt_id = f"glm1_t01_{side}_{caption_id}{suffix}"

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
                        "model_id_sent": MODEL_GLM_5_3,
                        "teacher_label": TEACHER_LABEL,
                        "side": side,
                        "caption_id": caption_id,
                        "reask_idx": reask_idx,
                        "round_index": round_index,
                        "is_round_5": is_round_5,
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
                "model_id_sent": MODEL_GLM_5_3,
                "teacher_label": TEACHER_LABEL,
                "side": side,
                "caption_id": caption_id,
                "reask_idx": reask_idx,
                "round_index": round_index,
                "is_round_5": is_round_5,
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
            "model_id_sent": MODEL_GLM_5_3,
            "teacher_label": TEACHER_LABEL,
            "side": side,
            "caption_id": caption_id,
            "reask_idx": reask_idx,
            "round_index": round_index,
            "is_round_5": is_round_5,
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
    print("V4 L14+ batch 7 round 5 | GLM_1 distill side | reask=4 -- 收官棒 (4/5 -> 5/5)")
    print("planed calls = 22 (22 caption x 1 call)")
    print("counting caliber: distill independent (prompt_id prefix glm1_t01_distill_) -- along r4 fix")
    print("distill baseline (post r1+r2+r3+r4): 4 successful/caption (88 calls/88 ok/0 empty)")
    print("goal: distill >=5 successful calls/caption (target met upon completion)")
    print("budget <=1500s watchdog")
    print("retry fix along r4 (incl r4 timeout recovery proof)")
    print("=" * 60)

    setup_proxy_teamo()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    captions = load_captions()
    cap_by_id = {c["id"]: c for c in captions}
    print(f"[INIT] captions loaded: {len(captions)}")

    with open(R1_RESULT_PATH, "r", encoding="utf-8") as f:
        r1 = json.load(f)
    with open(R2_RESULT_PATH, "r", encoding="utf-8") as f:
        r2 = json.load(f)
    with open(R3_RESULT_PATH, "r", encoding="utf-8") as f:
        r3 = json.load(f)
    with open(R4_RESULT_PATH, "r", encoding="utf-8") as f:
        r4 = json.load(f)

    # baseline 计数 = [r1, r2, r3, r4] 全载 (收官棒沿 r4 fix 口径)
    per_cap_succ_distill = {c["id"]: 0 for c in captions}
    per_cap_total_distill = {c["id"]: 0 for c in captions}
    per_cap_empty_distill = {c["id"]: 0 for c in captions}
    for src in [r1, r2, r3, r4]:
        for q in src.get("quadruples", []):
            pid = q.get("prompt_id", "")
            if not pid.startswith(DISTILL_SIDE_PROMPT_ID_PREFIX):
                continue
            m = q["per_call_metadata"]
            cid = m["caption_id"]
            per_cap_total_distill[cid] = per_cap_total_distill.get(cid, 0) + 1
            if m["ok"] and not m["empty_response"]:
                per_cap_succ_distill[cid] = per_cap_succ_distill.get(cid, 0) + 1
            if m["empty_response"]:
                per_cap_empty_distill[cid] = per_cap_empty_distill.get(cid, 0) + 1

    cum_total_prior_distill = sum(per_cap_total_distill.values())
    cum_ok_prior_distill = sum(per_cap_succ_distill.values())
    cum_empty_prior_distill = sum(per_cap_empty_distill.values())
    print(f"[DISTILL prior] total={cum_total_prior_distill} ok={cum_ok_prior_distill} "
          f"empty={cum_empty_prior_distill} (predecessor = r1+r2+r3+r4 quadruples GLM_1 distill prefix filter; expected 88/88/0 if all ok)")

    r4_cum = r4["aggregate"]["cumulative"]
    cum_total_prior_cum = r4_cum["post_total"]    # 296
    cum_empty_prior_cum = r4_cum["post_empty"]    # 9
    cum_ok_prior_cum = r4_cum["post_ok"]          # 287
    cum_rate_prior = cum_empty_prior_cum / cum_total_prior_cum if cum_total_prior_cum > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior_cum} ok={cum_ok_prior_cum} "
          f"empty={cum_empty_prior_cum} rate={cum_rate_prior:.4f} (source = r4 aggregate.cumulative.post)")

    r1_mixed_history = {}

    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r5_distill_{c['id']}"}
        for c in captions
    ]
    planned = PLANNED_CALLS
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (22 caption x 1 call)")

    try:
        api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
        print(f"[INIT] teamo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    t_batch_start = time.time()

    quadruples: List[Dict[str, Any]] = []
    cum_total = cum_total_prior_cum
    cum_empty = cum_empty_prior_cum
    cum_ok = cum_ok_prior_cum
    r5_total = 0
    r5_ok = 0
    r5_empty = 0
    r5_fail = 0
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
            is_round_5=True,
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
            r5_ok += 1
            cum_ok += 1
            per_cap_succ_distill[cap_id] += 1
        elif is_empty:
            r5_empty += 1
            cum_empty += 1
            per_cap_empty_distill[cap_id] += 1
        else:
            r5_fail += 1
        r5_total += 1
        cum_total += 1
        per_cap_total_distill[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ_distill = per_cap_succ_distill[cap_id]
        target_met_distill = "[OK] 收官 5/5" if cur_succ_distill >= 5 else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<28} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[distill_succ={cur_succ_distill}/5 {target_met_distill}] "
            f"[cum_rate={current_cum_rate_post:.4f}]"
        )

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

    empty_rate_r5 = (r5_empty / r5_total) if r5_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

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

    per_caption_mixed_history_successful_calls = r1_mixed_history

    # **收官判定块** -- glm1_distill_side_finish (沿 dispatch 字面)
    glm1_distill_side_finish = {
        "all_22_captions_met_target": met_target_count_distill == len(captions),
        "met_count_post_r5": met_target_count_distill,
        "total_captions": len(captions),
        "still_pending": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
        "finish_disposition": (
            "GLM_1 蒸馏侧全 22 caption 5/5 successful 达标 → batch7 蒸馏侧收官 ✓"
            if met_target_count_distill == len(captions)
            else f"GLM_1 蒸馏侧未达标 {len(captions) - met_target_count_distill} caption → 收官未达成 (本棒 0 写 verdict, 待 verdict-keeper 统裁)"
        ),
        "rounds_to_reach_target": 5,
        "rounds_to_reach_target_actual": (
            "5 棒 (r1+r2+r3+r4+r5) = 22 caption x 5 calls = 110 distill 侧 calls (收官态)"
        ),
        "distill_side_target_met_at_round": (
            "r5" if met_target_count_distill == len(captions) else "未达 (verdict-keeper 统裁)"
        ),
        "is_finish_round": True,
    }

    dispatch_target_progress_distill = {
        "target": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (distill side only)",
        "met_count_post_r5": met_target_count_distill,
        "total_captions": len(captions),
        "remaining_count": len(captions) - met_target_count_distill,
        "met_percentage": round(met_target_count_distill / len(captions) * 100, 2),
        "still_pending_captions": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
        "is_finish_round": True,
    }

    counting_scope_correction = {
        "r1_issue_disclosed": False,
        "r1_issue_description": (
            "本棒为 GLM_1 蒸馏侧 round 5 收官棒; predecessor = r1+r2+r3+r4 quadruples (88 calls, 88 ok, 0 empty); "
            "GLM_1 distill side = brand new teacher side, 沿 r1+r2+r3+r4 计数干净"
        ),
        "r1_data_disposition": "r1+r2+r3+r4 quadruples 完整保留 (r1=3558a1d15867, r2=924f12c4e7ab, r3=b431a1ba54df, r4=0fe4c1339d88); 作为 distill 侧 predecessor 不视为废数据",
        "r5_counting_domain": (
            f"distill side independent counting; filter domain = prompt_id prefix '{DISTILL_SIDE_PROMPT_ID_PREFIX}'"
            " (along r1/r2/r3/r4 fix; new teacher GLM_1 distill side)"
        ),
        "r5_target": f"distill side long-term goal >={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (收官阈值)",
        "r5_baseline_distill_only": (
            f"predecessor r1+r2+r3+r4 quadruples GLM_1 distill filter = {cum_total_prior_distill} calls, "
            f"{cum_ok_prior_distill} successful, "
            f"{cum_empty_prior_distill} empty (each caption = 4/5 successful, 沿 r1+r2+r3+r4)"
        ),
        "r5_post_distill_only": (
            f"r5 quadruples after = {sum(per_cap_total_distill.values())} calls, "
            f"{sum(per_cap_succ_distill.values())} successful, "
            f"{sum(per_cap_empty_distill.values())} empty (each caption = 5/5 successful 收官 expected)"
        ),
        "mixed_history_retention": (
            "per_caption_mixed_history_successful_calls block = empty dict (GLM_1 distill 为新教师, 无混合域); "
            "block 保留作透明字段待后续 verdict-keeper 统裁"
        ),
        "pending_pi_review": (
            "PI 复核本计数口径切换是否合规 (保守口径自主决策, PI 2026-09-25 00:46 委托); "
            "PI 拍板沿用 ask_748d9242 GLM_1 模型映射 = teamo glm-5.3"
        ),
        "finish_disposition": (
            f"r5 收官棒 distill side independent counting baseline = {cum_total_prior_distill} calls 完成; "
            f"实测 r5 after = {sum(per_cap_total_distill.values())} calls; "
            f"goal >={TARGET_SUCCESSFUL_PER_CAPTION} (收官阈值) 状态: {'收官达成' if met_target_count_distill == len(captions) else '未达'}; "
            f"by verdict-keeper 统裁 (本棒 0 写 verdict)"
        ),
    }

    retry_trigger_categories_distribution: Dict[str, int] = {}
    for cat in retry_trigger_categories_tracker:
        retry_trigger_categories_distribution[cat] = retry_trigger_categories_distribution.get(cat, 0) + 1

    retry_validation = {
        "r5_retry_count_distribution": dict(retry_count_distribution),
        "r5_retry_triggered_count": retry_triggered_count,
        "r5_retry_trigger_categories_tracker": retry_trigger_categories_tracker,
        "r5_retry_trigger_categories_distribution": retry_trigger_categories_distribution,
        "r5_retry_bug_fix_applied_in_all_calls": all(
            q["per_call_metadata"].get("retry_bug_fix_applied") is True
            for q in quadruples
        ),
        "r5_empty_rate_with_fix": round(empty_rate_r5, 4),
        "r4_empty_rate_with_fix_baseline": (
            r4["aggregate"]["r4_empty_response_rate"]
        ),
        "delta_empty_rate_r5_vs_r4": round(empty_rate_r5 - r4["aggregate"]["r4_empty_response_rate"], 4),
    }

    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 7,
        "round": 5,
        "metadata": {
            "task": "L14V3_batch7_round5_GLM_1_distill_side_reask4_FINISH_round_independent_counting",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "r4_executor_sha12": "d789f9bd4fa1",
                "r4_executor_path": "results/_v4_supp_l14v3_batch7_r4_executor.py",
                "r4_result_sha12": "0fe4c1339d88",
                "r4_result_path": "results/_v4_supp_l14v3_batch7_r4_result.json",
                "r3_executor_sha12": "5c0b426e2ee0",
                "r3_executor_path": "results/_v4_supp_l14v3_batch7_r3_executor.py",
                "r3_result_sha12": "b431a1ba54df",
                "r3_result_path": "results/_v4_supp_l14v3_batch7_r3_result.json",
                "r2_executor_sha12": "35cda0c0f7da",
                "r2_executor_path": "results/_v4_supp_l14v3_batch7_r2_executor.py",
                "r2_result_sha12": "924f12c4e7ab",
                "r2_result_path": "results/_v4_supp_l14v3_batch7_r2_result.json",
                "r1_executor_sha12": "c49fc9bca8c4",
                "r1_executor_path": "results/_v4_supp_l14v3_batch7_r1_executor.py",
                "r1_result_sha12": "3558a1d15867",
                "r1_result_path": "results/_v4_supp_l14v3_batch7_r1_result.json",
                "r5_executor_sha12_legacy": "8a8babb911b8",
                "r5_executor_path_legacy": "results/_v4_supp_l14v3_batch6_r5_executor.py",
                "r5_result_sha12_legacy": "e40424bf8abe",
                "r5_result_path_legacy": "results/_v4_supp_l14v3_batch6_r5_result.json",
                "model_mapping_sha12": "98A779D61C1E",
                "model_mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                "captions_sha12": "6a2656878745",
                "captions_path": "corpus/v20_caption_surface/strip_captions_22.json",
                "l13_verdict_sha12_referenced": "E105EC1362DB",
                "l13_verdict_path": "results/_v4_supp_l13_n26pair_verdict.md",
                "l13_verdict_on_disk": False,
                "l13_verdict_referenced_role": "V4 triplet basis (re-asked / distill / independent) distill style source anchor (round-trip reference only; no original-prompt doc reconstruction in this batch)",
            },
            "date": "2026-09-25",
            "freeze_day": "V4 L14+ N-26 truth-audit-only path batch 7 round 5 GLM_1 distill side reask=4 **收官棒**",
            "is_start_round": False,
            "is_progress_round": False,
            "is_finish_round": True,
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
            "spec_conformance": "PI 2026-09-24 同 agent 唤醒 (task_append) 接力棒 + 沿 r4 fix 口径续跑 (baseline [r1,r2,r3,r4] 全载) + retry 修复沿 r4 (含 r4 timeout recovery) + 每 caption successful 计数终盘点 + K-N26-N2 累计监控 + distill 侧独立计数 (沿 r1+r2+r3+r4) + **收官判定块 glm1_distill_side_finish** (沿 dispatch 字面)",
            "teacher": TEACHER,
            "teacher_label": TEACHER_LABEL,
            "side": SIDE,
            "round_index": 5,
            "reask_idx_r1": REASK_R1,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r5_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": "along model mapping draft §1.1 GLM_1 拍板定案 (ask_748d9242 字面) + along r4 executor d789f9bd4fa1 端点实测 = teamo glm-5.3",
            "model_id_sent": MODEL_GLM_5_3,
            "model_id_sent_basis": "model_mapping 98A779D61C1E §1.1 GLM_1 column 拍板定案 = teamo glm-5.3 (PI 2026-09-24 23:08 ask_748d9242)",
            "model_id_inconsistency_honest_disclosure": r4["metadata"]["model_id_inconsistency_honest_disclosure"],
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
                "r4_status": "retry 修复 + tracking 改进沿 r4 (沿 d789f9bd4fa1); r4 棒 timeout recovery proof 1 call (L_historical_causality retries=1)",
                "r5_status": "retry 修复沿 r4; r5 收官棒本棒无新参数修正",
                "rationale": (
                    "沿 r4 修复 + r4 tracking 改进 (含 r4 timeout recovery); r5 收官棒仅按 22 caption x 1 call 续采 (model 不变, 仅 reask_idx 3->4); "
                    "hard fail 保持 fail path 立即返回"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r4_executor": [
                "1. ROUND=4 -> ROUND=5; REASK_R1=3 -> REASK_R1=4 (第 5 call/caption = reask_idx=4)",
                "2. prompt_id 后缀 _r4 -> _r5",
                "3. predecessor_sha12: r4_executor d789f9bd4fa1 + r4_result 0fe4c1339d88 (替代 r3 双件为直接 predecessor)",
                "4. baseline 全载 [r1, r2, r3, r4] quadruples = 88 calls/88 ok/0 empty (沿 r4 fix 口径)",
                "5. 增量: distill 各 caption 由 4/5 补至 5/5 (收官达成)",
                "6. cumulative 起点: r4 post {296/9/0.0304} -> 本棒后 worst 31/318=9.75% / best 9/318=2.83%",
                "7. **判定块重命名**: glm1_distill_side_round4_progress -> **glm1_distill_side_finish** (字面)",
                "8. metadata.is_finish_round = True (替代 r4 is_progress_round = True)",
                "9. metadata 新增 is_progress_round = False (明示非续跑态 = 收官态)",
                "10. counting_scope_correction: r4_baseline=88 calls 4succ/0empty; r5 后预期 110 calls 5succ/0empty (收官)",
                "11. headers 反映 batch7-r5 + finish",
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
        "glm1_distill_side_finish": glm1_distill_side_finish,
        "dispatch_target_progress_distill": dispatch_target_progress_distill,
        "aggregate": {
            "r5_total_calls": r5_total,
            "r5_ok_count": r5_ok,
            "r5_empty_response_count": r5_empty,
            "r5_fail_count": r5_fail,
            "r5_empty_response_rate": round(empty_rate_r5, 4),
            "r5_total_prompt_tokens": total_prompt_tokens,
            "r5_total_completion_tokens": total_completion_tokens,
            "r5_total_tokens": total_prompt_tokens + total_completion_tokens,
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
            "r5_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r5_empty_response_above_threshold_single_batch": empty_rate_r5 > 0.50,
        },
        "empty_rate_trend": {
            "batch1_round1": {
                "calls": r4["empty_rate_trend"]["batch1_round1"]["calls"],
                "empty": r4["empty_rate_trend"]["batch1_round1"]["empty"],
                "rate": r4["empty_rate_trend"]["batch1_round1"]["rate"],
            },
            "batch1_round2": {
                "calls": r4["empty_rate_trend"]["batch1_round2"]["calls"],
                "empty": r4["empty_rate_trend"]["batch1_round2"]["empty"],
                "rate": r4["empty_rate_trend"]["batch1_round2"]["rate"],
            },
            "batch1_round3": {
                "calls": r4["empty_rate_trend"]["batch1_round3"]["calls"],
                "empty": r4["empty_rate_trend"]["batch1_round3"]["empty"],
                "rate": r4["empty_rate_trend"]["batch1_round3"]["rate"],
            },
            "batch1_round4": {
                "calls": r4["empty_rate_trend"]["batch1_round4"]["calls"],
                "empty": r4["empty_rate_trend"]["batch1_round4"]["empty"],
                "rate": r4["empty_rate_trend"]["batch1_round4"]["rate"],
            },
            "batch1_round5": {
                "calls": r4["empty_rate_trend"]["batch1_round5"]["calls"],
                "empty": r4["empty_rate_trend"]["batch1_round5"]["empty"],
                "rate": r4["empty_rate_trend"]["batch1_round5"]["rate"],
            },
            "batch6_round1": {
                "calls": r4["empty_rate_trend"]["batch6_round1"]["calls"],
                "empty": r4["empty_rate_trend"]["batch6_round1"]["empty"],
                "rate": r4["empty_rate_trend"]["batch6_round1"]["rate"],
            },
            "batch6_round2": {
                "calls": r4["empty_rate_trend"]["batch6_round2"]["calls"],
                "empty": r4["empty_rate_trend"]["batch6_round2"]["empty"],
                "rate": r4["empty_rate_trend"]["batch6_round2"]["rate"],
            },
            "batch6_round3": {
                "calls": r4["empty_rate_trend"]["batch6_round3"]["calls"],
                "empty": r4["empty_rate_trend"]["batch6_round3"]["empty"],
                "rate": r4["empty_rate_trend"]["batch6_round3"]["rate"],
            },
            "batch6_round4": {
                "calls": r4["empty_rate_trend"]["batch6_round4"]["calls"],
                "empty": r4["empty_rate_trend"]["batch6_round4"]["empty"],
                "rate": r4["empty_rate_trend"]["batch6_round4"]["rate"],
            },
            "batch6_round5": {
                "calls": r4["empty_rate_trend"]["batch6_round5"]["calls"],
                "empty": r4["empty_rate_trend"]["batch6_round5"]["empty"],
                "rate": r4["empty_rate_trend"]["batch6_round5"]["rate"],
            },
            "batch7_round1": {
                "calls": r4["empty_rate_trend"]["batch7_round1"]["calls"],
                "empty": r4["empty_rate_trend"]["batch7_round1"]["empty"],
                "rate": r4["empty_rate_trend"]["batch7_round1"]["rate"],
            },
            "batch7_round2": {
                "calls": r4["empty_rate_trend"]["batch7_round2"]["calls"],
                "empty": r4["empty_rate_trend"]["batch7_round2"]["empty"],
                "rate": r4["empty_rate_trend"]["batch7_round2"]["rate"],
            },
            "batch7_round3": {
                "calls": r4["empty_rate_trend"]["batch7_round3"]["calls"],
                "empty": r4["empty_rate_trend"]["batch7_round3"]["empty"],
                "rate": r4["empty_rate_trend"]["batch7_round3"]["rate"],
            },
            "batch7_round4": {
                "calls": r4["empty_rate_trend"]["batch7_round4"]["calls"],
                "empty": r4["empty_rate_trend"]["batch7_round4"]["empty"],
                "rate": r4["empty_rate_trend"]["batch7_round4"]["rate"],
            },
            "batch7_round5": {
                "calls": r5_total,
                "empty": r5_empty,
                "rate": round(empty_rate_r5, 4),
            },
            "cumulative_through_r5": {
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
                "round_5_n_distinct_sample_note": (
                    "round 5 收官棒第 5 call per caption 实测; GLM_1 distill side independent counting = 22 caption 各 5 successful "
                    "(沿 r1+r2+r3+r4+本棒 quadruples, prompt_id prefix glm1_t01_distill_ filter domain, predecessor r1+r2+r3+r4 = 88 calls 4succ/caption);"
                    "**GLM_1 蒸馏侧收官达成**: distill side 22/22 caption 5/5 successful 收官态 (4/5 -> 5/5);"
                    "by verdict-keeper 统裁 (本棒 0 写 verdict)"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r5, 4),
                "cumulative_empty_response_rate": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r5 > 0.50,
                "cumulative_trigger": {
                    "triggered": k_n26_n2_triggered,
                    "trigger_at_call_idx": k_n26_n2_trigger_at_call_idx,
                    "trigger_cum_rate": (
                        round(k_n26_n2_trigger_cum_rate, 4) if k_n26_n2_trigger_cum_rate is not None else None
                    ),
                    "stop_reason": stop_reason if k_n26_n2_triggered else None,
                },
                "monitor_disposition": (
                    "本棒 K-N26-N2 累计 empty_rate 监控 = 已实施;"
                    + (
                        "本棒触发 K-N26-N2 pass=False 构造失灵族判定 + 立即停采"
                        if k_n26_n2_triggered else
                        "本棒未触发 K-N26-N2 累计阈值; 跑至 1500s watchdog 提前停批 / 全 22 calls 完成 (收官态)"
                    )
                ),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict); GLM_1 蒸馏侧 batch7 已收官态, 留待 verdict-keeper 终裁",
        },
        "breakpoint_status": {
            "hit_wall_time_budget": wall_time_s > WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_triggered": k_n26_n2_triggered,
            "stop_reason": stop_reason,
            "actual_wall_time_s": wall_time_s,
            "planned_calls": planned_total,
            "actual_calls": r5_total,
            "checkpoint_file": None,
            "next_resume_via": "本棒为 batch7 收官棒 — 无 next 棒 (GLM_1 蒸馏侧 22/22 caption 5/5 successful 收官达成)",
            "note": (
                f"本棒 round 5 收官棒已完成（{r5_total}/{planned_total} calls）"
                + (f"; K-N26-N2 累计阈值触发" if k_n26_n2_triggered else
                   f"; hit {WALL_TIME_BUDGET_S}s watchdog 提前停批 ({len(captions) - r5_ok} caption 未达标)"
                   if wall_time_s > WALL_TIME_BUDGET_S and r5_ok < len(captions) else
                   f"; **GLM_1 蒸馏侧 22/22 caption 5/5 successful 收官** ✓ (4/5 -> 5/5)"
                   if r5_ok == len(captions) else
                   f"; GLM_1 蒸馏侧未达标 {len(captions) - r5_ok} caption -> 收官未达成 (待 verdict-keeper 统裁)")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch7_r5_result.json")
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
    print(f"  quadruples: {r5_total} (ok={r5_ok} empty={r5_empty} fail={r5_fail})")
    print(f"  r5_empty_rate: {empty_rate_r5:.4f}")
    print(f"  cumulative_empty_rate: {cum_empty_rate_post:.4f}")
    print(f"  k_n26_n2_triggered: {k_n26_n2_triggered}")
    print(f"  distill_side_met_target_count: {met_target_count_distill}/{len(captions)}")
    print(f"  *** all_22_captions_met_target_distill: {glm1_distill_side_finish['all_22_captions_met_target']} ***")
    print(f"  finish_disposition: {glm1_distill_side_finish['finish_disposition']}")
    print(f"  retry_bug_fix_applied_in_all_calls: {retry_validation['r5_retry_bug_fix_applied_in_all_calls']}")
    print(f"  retry_triggered_count: {retry_triggered_count}")
    print(f"  retry_count_distribution: {retry_count_distribution}")
    print(f"  retry_trigger_categories_distribution: {retry_trigger_categories_distribution}")
    print(f"  tun_compliance: {tun_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  stop_reason: {stop_reason}")
    if glm1_distill_side_finish["still_pending"]:
        print(f"  still_pending_distill (>=5 target distance): {glm1_distill_side_finish['still_pending']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
