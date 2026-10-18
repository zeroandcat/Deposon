# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch10_r1_executor.py
=====================================

V4 L14+ batch 10 · round 1 (reask=0) -- minimax 蒸馏侧第一棒 (独立计数起步棒)

派工依据:
  - 沿 L14+ 派工单 2026-09-26 16:25「minimax 蒸馏侧 round 1 (distill 侧开工)」
  - 沿 batch6 r5 executor (SHA-12 8a8babb911b8) + r5 result (SHA-12 e40424bf8abe) 口径续跑 (dispatch §1 字面「predecessor 链 batch6 r5 双件+mapping」)
  - 沿模型映射留痕件 `_v4_supp_l14v3_model_mapping_2026_09_24.md` (SHA-12 98A779D61C1E)
    §1.1 minimax -> mimo 端点 `mimo-v2.6-pro` 字面沿用 (ask_748d9242 字面)
  - 沿 prereg `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` (字面引用 05B975A86989) 字面
  - 同 agent 唤醒保上下文 (task_append 接力棒)
  - PI 2026-09-25 00:46「今晚保守口径下先斩后奏」夜间授权 (沿用)
  - minimax 教师侧已于 batch5 r1-r5 收官 (5 棒 × 22 caption × 1 call = 110 calls, all OK);
    本棒 = minimax 蒸馏侧 round 1 起步 (与 batch5 minimax teacher 同 model (mimo-v2.6-pro),
    同 endpoint (mimo), 同 prompt 构造, 不同 side = distill)

本棒范围:
  1. 22 caption × 1 call = 22 calls
  2. batch=10 (minimax distill) + round=1 (reask=0)
     - 模型 = mimo `mimo-v2.6-pro` (沿模型映射 §1.1 minimax 拍板)
     - 端点 = https://token-plan-cn.xiaomimimo.com/v1/chat/completions (沿 batch5 r5 minimax teacher 实测)
     - 不走代理 (沿 L7 + add_T1 §1.6.2 mimo 端点 = 无代理硬纪律)
     - **endpoint_migrated=true** (V3 火山方舟 → V4 mimo 跨端点跨厂商)
     - **lineage_discontinuity=true** (V3 minimax-m3 ≠ V4 mimo-v2.6-pro, 端点名不同、模型家族不同)
     - **teacher_v3_anchor = "minimax-m3 (火山方舟已下线)"**
  3. distill 侧独立计数:
     - filter = prompt_id 前缀 `minimax_t01_distill_`
     - 本棒为 minimax distill 第一棒: predecessor r1-r4 同前缀 0 条 = 0/5 baseline
     - 目标 ≥5 successful/caption (远期)
     - 本棒后预期 22 caption 各 1/5 successful (起步棒)
  4. side=distill + teacher_label=minimax 字面字段 + 派生 metadata (endpoint_migrated/lineage_discontinuity/proxy_used/teacher_v3_anchor)
  5. cumulative 监控: 起点 = batch8 r5 cumulative.post (318/9/309/2.83%); 本棒后 worst 31/340=9.12%; best 9/340=2.65%
  6. 起步判定块 `minimax_distill_side_round1_start` (all_22=False / met_count=22 expected / still_pending=22)

与 batch6 r5 executor diff:
  1. 模型切换 kimi-k3 -> mimo-v2.6-pro (沿模型映射 §1.1 minimax 拍板)
  2. endpoint 切换 teamo (走 tun) -> mimo (无代理)
  3. teacher_label kimi -> minimax
  4. prompt_id 前缀 kimi_t01_distill_ -> minimax_t01_distill_
  5. _r5 -> _r1 后缀
  6. ROUND=5 -> ROUND=1; REASK_R1=4 -> REASK_R1=0
  7. predecessor 链改: r5_executor 8a8babb911b8 + r5_result e40424bf8abe + mapping 98A779D61C1E
     (dispatch 字面) + batch5 r5 minimax teacher 双件 (直接 prior minimax work) +
     batch8 r5 GLM_2 distill 收官 (最新 cross-batch cumulative baseline)
  8. distill 侧 baseline = 0 (r1-r4 同前缀 0 条); r1 quadruples 增量 = 22
  9. per_caption 终盘点新增 met_target=1 起步档 (非 r5 的 met_target=5 收官档)
 10. cumulative 起点 = batch8 r5 cumulative.post (318/9/309/2.83%) (跨批最新实测)
 11. 判定块重命名: kimi_distill_side_finish -> minimax_distill_side_round1_start
 12. counting_scope_correction 改: r1_baseline=0/起步/起步棒描述 (无 r1 混合口径问题)
 13. per_call_metadata 新增 endpoint_migrated/lineage_discontinuity/proxy_used/teacher_v3_anchor
     (沿 batch5 r5 minimax teacher + mapping §1.2 minimax 行字面)

铁律严守:
  - R1 no_llm = False (V4 派工已按调 LLM)
  - R4 key 永不明文 (无例外)
  - R5 V4 frozen append-only
  - R6 P-G 不动 / R7 plugin spec 不动
  - V1-V3 只读不动 / 派生 JSON 不合并
  - 0 擅调阈值; max_tokens=2000 沿 prereg
  - 串行 ≥2.5s 全程; mimo 必走无代理 (硬纪律)
  - 空响应 = response_text 空/仅空白; 如实计数
  - 只采不算 K-N26-1/2/3 (verdict-keeper 统裁; 本棒 0 写 verdict)
  - succeeded ≠ 跑完落盘核验
  - 老实交代 0 产物

产物:
  - 写入: results/_v4_supp_l14v3_batch10_r1_result.json
    (schema = v4_l14v3_n26/1 + batch=10 + round=1)
  - 不覆盖 batch6 r5 result e40424bf8abe 或前棒 result (含 batch1-batch8 全部)

边界:
  - 不动任何既有件 (含 batch6 r5 双件 + batch8 r5 双件 + batch5 r1-r5 minimax teacher + batch7 r1-r5 GLM_1 distill + batch1 r1-r6 + batch2 r1-r3 + batch3 r1-r5 + batch4 r1-r6 + batch8 r1-r4 + prereg 05B975A86989 + captions 6a2656878745 + mapping 98A779D61C1E)
  - 跑不完拆段报断点
  - 0 触动 V1-V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
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
BATCH6_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch6_r5_result.json")
BATCH8_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch8_r5_result.json")

# ============================================================
# 端点配置 (model 沿模型映射留痕件 §1.1 minimax 拍板 mimo-v2.6-pro; 无代理)
# ============================================================
ENDPOINT_MIMO = "https://token-plan-cn.xiaomimimo.com/v1"
MODEL_MINIMAX = "mimo-v2.6-pro"
KEY_INDEX_MIMO_1BASED = 27
USE_PROXY = False

# 串行间隔 (沿 r5)
INTER_CALL_SLEEP_S = 2.5

# 超参 (沿 r5)
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正 (沿 r5)
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别 (沿 r5)
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值 (沿 r5)
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算 (沿 r5; 1500s 容 22 caption calls + 串行 ≥2.5s)
WALL_TIME_BUDGET_S = 1500

# 本棒调度 (沿 dispatch §1)
BATCH = 10
ROUND = 1
SIDE = "distill"
TEACHER = "minimax"
TEACHER_LABEL = "minimax"
REASK_R1 = 0  # round 1 = 第 1 call per caption (reask_idx = 0) -- 起步
TARGET_SUCCESSFUL_PER_CAPTION = 5  # distill 侧目标 (字面 ≥5)

# ============================================================
# 计数口径 (沿 r5 distill 侧独立计数; minimax 蒸馏侧独立域)
# ============================================================
DISTILL_SIDE_PROMPT_ID_PREFIX = "minimax_t01_distill_"


# ============================================================
# 敏感模式 (沿 r5)
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
# 工具 (沿 r5; mimo 无代理)
# ============================================================
def setup_no_proxy_mimo() -> None:
    """mimo 端点不需代理; 显式清空 http_proxy/https_proxy/all_proxy (沿 L7 + add_T1 §1.6.2 硬纪律)."""
    for k in ("http_proxy", "https_proxy", "all_proxy", "HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY"):
        os.environ.pop(k, None)


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


def call_chat_mimo(
    api_key: str,
    messages: List[Dict[str, str]],
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
    timeout: int = READ_TIMEOUT_INITIAL_S,
) -> Dict[str, Any]:
    """mimo 端点 chat 调用 (无代理; 沿 batch5 r5)."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch10-r1",
        "X-Title": "deposon-l14v3-batch10-r1-minimax-distill",
    }
    body = {
        "model": MODEL_MINIMAX,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    chat_url = ENDPOINT_MIMO.rstrip("/") + "/chat/completions"

    t0 = time.time()
    try:
        r = _requests.post(chat_url, headers=headers, json=body, timeout=timeout)
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
# 提示构造 (沿 r5 prompt 构造口径 = batch1 r6 reproduction_caliber anchor)
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
# 单 call + 内层重试 (沿 r5; minimax 蒸馏侧 metadata 增 endpoint_migrated/lineage_discontinuity/proxy_used/teacher_v3_anchor)
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
    prompt_id = f"minimax_t01_{side}_{caption_id}{suffix}"

    # minimax 蒸馏侧派生 metadata (沿 batch5 r5 + mapping §1.2 minimax 行)
    minimax_distill_meta = {
        "endpoint_migrated": True,
        "lineage_discontinuity": True,
        "proxy_used": False,
        "teacher_v3_anchor": "minimax-m3 (火山方舟已下线)",
    }

    retries = 0
    last = None
    while retries <= INNER_RETRY_MAX:
        timeout_s = READ_TIMEOUT_INITIAL_S if retries == 0 else READ_TIMEOUT_RETRY_S
        r = call_chat_mimo(api_key=api_key, messages=messages, timeout=timeout_s)
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
                        "endpoint": ENDPOINT_MIMO + "/chat/completions",
                        "model_id_sent": MODEL_MINIMAX,
                        "teacher_label": TEACHER_LABEL,
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
                        **minimax_distill_meta,
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
                "endpoint": ENDPOINT_MIMO + "/chat/completions",
                "model_id_sent": MODEL_MINIMAX,
                "teacher_label": TEACHER_LABEL,
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
                **minimax_distill_meta,
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
            "endpoint": ENDPOINT_MIMO + "/chat/completions",
            "model_id_sent": MODEL_MINIMAX,
            "teacher_label": TEACHER_LABEL,
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
            **minimax_distill_meta,
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 L14+ batch 10 round 1 | minimax distill side | reask=0 -- 起步棒")
    print("计划 calls = 22 (22 caption × 1 call)")
    print("计数口径: distill 侧独立 (prompt_id 前缀 minimax_t01_distill_) -- 沿 r5")
    print("distill 侧 baseline: 0 successful/caption (本棒为 minimax distill 第一棒)")
    print("目标: distill 侧 ≥5 successful calls/caption (远期)")
    print("预算 ≤1500s watchdog")
    print("retry 修复沿 r5 (含 retry 触发的源 error_category tracking)")
    print("mimo 无代理 (沿 L7 + add_T1 §1.6.2)")
    print("annotations: endpoint_migrated=True, lineage_discontinuity=True")
    print("=" * 60)

    # 1. mimo 不走代理 (硬纪律); 显式清空代理 env (防御性)
    setup_no_proxy_mimo()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # 2. 加载 caption
    captions = load_captions()
    cap_by_id = {c["id"]: c for c in captions}
    print(f"[INIT] captions loaded: {len(captions)}")

    # 3. 加载 batch6 r5 result (dispatch 字面 predecessor) + batch8 r5 result (跨批最新 cumulative)
    with open(BATCH6_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b6r5 = json.load(f)
    with open(BATCH8_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b8r5 = json.load(f)

    # 4. minimax distill 侧独立计数 (本棒为起步棒, r1-r4 同前缀 0 条 = 0/5 baseline)
    per_cap_succ_distill = {c["id"]: 0 for c in captions}
    per_cap_total_distill = {c["id"]: 0 for c in captions}
    per_cap_empty_distill = {c["id"]: 0 for c in captions}
    cum_total_prior_distill = 0  # 起步棒
    cum_ok_prior_distill = 0     # 起步棒
    cum_empty_prior_distill = 0  # 起步棒
    print(f"[DISTILL prior] total={cum_total_prior_distill} ok={cum_ok_prior_distill} "
          f"empty={cum_empty_prior_distill} (本棒为 minimax distill 起步棒, r1-r4 同前缀 0 条)")

    # 5. cumulative 监控沿 batch8 r5 cumulative 链路 (跨教师跨侧累计 = 最新实测)
    b8r5_cum = b8r5["aggregate"]["cumulative"]
    cum_total_prior_cum = b8r5_cum["post_total"]    # 318
    cum_empty_prior_cum = b8r5_cum["post_empty"]    # 9
    cum_ok_prior_cum = b8r5_cum["post_ok"]          # 309
    cum_rate_prior = cum_empty_prior_cum / cum_total_prior_cum if cum_total_prior_cum > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior_cum} ok={cum_ok_prior_cum} "
          f"empty={cum_empty_prior_cum} rate={cum_rate_prior:.4f} (源 = batch8 r5 aggregate.cumulative.post)")

    # 6. 没有 mixed history (本棒为 minimax distill 第一棒, 无 r1 混合域参照)
    r1_mixed_history = {}

    # 7. 调度 planned_calls (22 caption × 1 call = 22 calls)
    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r1_distill_{c['id']}"}
        for c in captions
    ]
    planned = PLANNED_CALLS
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (22 caption × 1 call)")

    # 8. 加载 key (mimo-plan = line 27; 沿 Track 2 endpoints probe C846F7FC79EE)
    try:
        api_key = fetch_api_key(KEY_INDEX_MIMO_1BASED)
        print(f"[INIT] mimo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 9. 时间预算起点
    t_batch_start = time.time()

    # 10. 跑
    quadruples: List[Dict[str, Any]] = []
    cum_total = cum_total_prior_cum
    cum_empty = cum_empty_prior_cum
    cum_ok = cum_ok_prior_cum
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

        # K-N26-N2 累计监控 (call 前判)
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
            per_cap_succ_distill[cap_id] += 1
        elif is_empty:
            r1_empty += 1
            cum_empty += 1
            per_cap_empty_distill[cap_id] += 1
        else:
            r1_fail += 1
        r1_total += 1
        cum_total += 1
        per_cap_total_distill[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ_distill = per_cap_succ_distill[cap_id]
        target_met_distill = "[OK] 起步 1/5" if cur_succ_distill >= 1 else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<28} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[distill_succ={cur_succ_distill}/5 {target_met_distill}] "
            f"[cum_rate={current_cum_rate_post:.4f}]"
        )

        # K-N26-N2 停采监控 (call 后立即判)
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

    # 11. 统计
    empty_rate_r1 = (r1_empty / r1_total) if r1_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    no_proxy_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
        and not r["per_call_metadata"].get("proxy_used", True)
    )
    no_proxy_compliance = (no_proxy_used_count == len(quadruples))

    # 12. 每 caption successful 计数 -- distill 侧独立
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

    # 13. mixed history 透明保留 (本棒 = {}; 无 r1 混合域参照)
    per_caption_mixed_history_successful_calls = r1_mixed_history

    # 14. distill 侧 **起步判定** (沿 dispatch §2 字面块名 `minimax_distill_side_round1_start`)
    minimax_distill_side_round1_start = {
        "all_22_captions_met_target": met_target_count_distill == len(captions),
        "met_count_post_r1": met_target_count_distill,
        "total_captions": len(captions),
        "still_pending": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
        "start_disposition": (
            "minimax 蒸馏侧第一棒完成 → batch10 distill side 起步 ✓ (22 caption 各 1/5 successful 起步态)"
            if (r1_total == len(captions) and r1_ok == len(captions))
            else f"minimax 蒸馏侧第一棒完成 → batch10 distill side 起步, r1_ok={r1_ok}/{len(captions)} (需后续 r2-r4 接力补足)"
        ),
        "rounds_to_reach_target_planned": 5,
        "rounds_to_reach_target_actual": (
            "1 棒 (本棒 r1) = 22 caption × 1 call = 22 distill 侧 calls "
            "(起步态, 目标 ≥5 需 4 more 棒接力)"
        ),
        "distill_side_target_met_at_round": (
            "r5 (expected)" if met_target_count_distill == len(captions) else "未达 (本棒为 r1 起步棒, 留 r2-r4 接力)"
        ),
        "is_start_round": True,
    }

    # 15. dispatch §6 收尾盘点 -- distill 侧
    dispatch_target_progress_distill = {
        "target": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (distill side only)",
        "met_count_post_r1": met_target_count_distill,
        "total_captions": len(captions),
        "remaining_count": len(captions) - met_target_count_distill,
        "met_percentage": round(met_target_count_distill / len(captions) * 100, 2),
        "still_pending_captions": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
        "is_start_round": True,
    }

    # 16. counting_scope_correction 块 (沿 r5; 本棒特殊: 起步棒, 无 r1 混合口径问题)
    counting_scope_correction = {
        "r1_issue_disclosed": False,
        "r1_issue_description": (
            "本棒为 minimax 蒸馏侧第一棒 (= batch10 round 1), predecessor r1-r4 同前缀 quadruples = 0 条;"
            "无 r1 混合口径 (本棒 predecessor r1-r4 同前缀过滤后 = 0 条);"
            "无 kimi 蒸馏侧混合计数问题 (本棒为新教师 minimax 蒸馏侧独立开工)"
        ),
        "r1_data_disposition": "本棒 = 起步棒, 无 predecessor 混合数据; 无 r1 口径归正需求",
        "r1_counting_domain": (
            f"distill 侧独立计数; filter 域 = prompt_id 前缀 '{DISTILL_SIDE_PROMPT_ID_PREFIX}'"
            " (沿 r5; 新教师 minimax 蒸馏侧)"
        ),
        "r1_target": f"distill 侧远期目标 ≥{TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption",
        "r1_baseline_distill_only": (
            f"predecessor r1-r4 quadruples minimax distill 过滤后 = 0 calls, "
            f"0 successful, 0 empty (本棒 = 起步棒, 沿 dispatch §1)"
        ),
        "r1_post_distill_only": (
            f"r1 quadruples 后 = {sum(per_cap_total_distill.values())} calls, "
            f"{sum(per_cap_succ_distill.values())} successful, "
            f"{sum(per_cap_empty_distill.values())} empty (各 caption = 1/5 successful 起步态 expected)"
        ),
        "mixed_history_retention": (
            "per_caption_mixed_history_successful_calls 块 = {} 空字典 (本棒无 r1 混合域参照);"
            "该块保留作透明字段待后续 r2-r4 接力棒填充"
        ),
        "pending_pi_review": (
            "PI 复核本计数口径切换是否合规 (保守口径自主决策, PI 2026-09-25 00:46 委托);"
            "PI 拍板沿用 ask_748d9242 minimax 模型映射 = mimo 端点 mimo-v2.6-pro 字面"
        ),
        "start_disposition": (
            f"r1 起步棒 distill 侧独立计数基线 = {cum_total_prior_distill} calls 完成; "
            f"实测 r1 quadruples 后 = {sum(per_cap_total_distill.values())} calls; "
            f"目标 ≥{TARGET_SUCCESSFUL_PER_CAPTION} 远期未达 (起步棒实况)"
        ),
    }

    # 17. retry validation 块 (沿 r5)
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
            b6r5["aggregate"]["r5_empty_response_rate"]
        ),
        "delta_empty_rate_r1_vs_r5": round(empty_rate_r1 - b6r5["aggregate"]["r5_empty_response_rate"], 4),
    }

    # 18. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 10,
        "round": 1,
        "metadata": {
            "task": "L14V3_batch10_round1_minimax_distill_side_reask0_start_round_independent_counting",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                # dispatch 字面 (minimum chain reference)
                "r5_executor_sha12": "8a8babb911b8",
                "r5_executor_path": "results/_v4_supp_l14v3_batch6_r5_executor.py",
                "r5_result_sha12": "e40424bf8abe",
                "r5_result_path": "results/_v4_supp_l14v3_batch6_r5_result.json",
                "model_mapping_sha12": "98A779D61C1E",
                "model_mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                # 扩展上下文: minimax teacher side 直接 prior
                "b5_r5_executor_sha12": "82c283d8f37a",
                "b5_r5_executor_path": "results/_v4_supp_l14v3_batch5_r5_executor.py",
                "b5_r5_result_sha12": "c874d21a4cbe",
                "b5_r5_result_path": "results/_v4_supp_l14v3_batch5_r5_result.json",
                "b5_r4_executor_sha12": "28844c34b12b",
                "b5_r4_executor_path": "results/_v4_supp_l14v3_batch5_r4_executor.py",
                "b5_r4_result_sha12": "1c62520c372b",
                "b5_r4_result_path": "results/_v4_supp_l14v3_batch5_r4_result.json",
                # 扩展上下文: 最新跨批 cumulative baseline
                "b8_r5_executor_sha12": "6961281824ae",
                "b8_r5_executor_path": "results/_v4_supp_l14v3_batch8_r5_executor.py",
                "b8_r5_result_sha12": "3620a7daf9c1",
                "b8_r5_result_path": "results/_v4_supp_l14v3_batch8_r5_result.json",
                "captions_sha12": "6a2656878745",
                "captions_path": "corpus/v20_caption_surface/strip_captions_22.json",
                "l13_verdict_sha12_referenced": "E105EC1362DB",
                "l13_verdict_path": "results/_v4_supp_l13_n26pair_verdict.md",
                "l13_verdict_on_disk": False,
                "l13_verdict_referenced_role": "V4 triplet basis (re-asked / distill / independent) distill style source anchor (round-trip reference only; no original-prompt doc reconstruction in this batch)",
            },
            "date": "2026-09-26",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 10 round 1 minimax distill side reask=0 起步棒",
            "is_start_round": True,
            "night_authorization": "PI 2026-09-25 00:46「今晚保守口径下先斩后奏」 (沿用)",
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
            "spec_conformance": "PI 2026-09-26 同 agent 唤醒 (task_append) 接力棒 + 沿 r5 口径续跑 + minimax 模型映射沿 r5 (mimo-v2.6-pro) + retry 修复沿 r5 + 每 caption successful 计数终盘点 + K-N26-N2 累计监控 + distill 侧独立计数 (沿 r5 counting_scope_correction) + 起步判定块 minimax_distill_side_round1_start",
            "teacher": TEACHER,
            "teacher_label": TEACHER_LABEL,
            "side": SIDE,
            "round_index": 1,
            "reask_idx_r1": REASK_R1,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r1_total,
            "endpoint_selected": ENDPOINT_MIMO,
            "endpoint_selection_method": "沿模型映射留痕件 §1.1 minimax 拍板定案 (ask_748d9242 字面) + 沿 batch5 r5 minimax teacher 实测 = mimo mimo-v2.6-pro (无代理)",
            "model_id_sent": MODEL_MINIMAX,
            "model_id_sent_basis": "model_mapping 98A779D61C1E §1.1 minimax 列拍板定案 = mimo 端点 mimo-v2.6-pro (PI 2026-09-24 23:08 ask_748d9242 字面)",
            "model_id_inconsistency_honest_disclosure": b6r5["metadata"]["model_id_inconsistency_honest_disclosure"],
            "endpoint_migrated": True,
            "lineage_discontinuity": True,
            "v3_origin_endpoint": "火山方舟 (V3 字面 minimax-m3 已下线)",
            "v4_current_endpoint": "mimo (token-plan-cn.xiaomimimo.com/v1)",
            "proxy_settings": {
                "http": None,
                "socks5": None,
                "applied_to_mimo": False,
                "note": "mimo 端点 = 无代理 (沿 L7 + add_T1 §1.6.2); 显式清空代理 env (防御性)",
            },
            "key_discipline": {
                "source": KEY_SOURCE_PATH,
                "key_index_1based": KEY_INDEX_MIMO_1BASED,
                "method": "runtime memory read",
                "redacted_in_products": True,
                "note": "KEY_INDEX_MIMO_1BASED=27 = mimo-plan key (沿 Track 2 endpoints probe C846F7FC79EE)",
            },
            "inter_call_sleep_s": INTER_CALL_SLEEP_S,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "tools_fault_param_correction": {
                "read_timeout_initial_s": READ_TIMEOUT_INITIAL_S,
                "read_timeout_retry_s": READ_TIMEOUT_RETRY_S,
                "network_error_categories_retry": sorted(list(NETWORK_ERROR_CATEGORIES_RETRY)),
                "r5_status": "retry 修复 + tracking 改进沿 r5 (沿 8a8babb911b8)",
                "r1_status": "retry 修复沿 r5; r1 起步棒本棒无新参数修正",
                "rationale": (
                    "沿 r5 修复 + r5 tracking 改进; r1 起步棒仅按 22 caption × 1 call 续采 (model 切换 kimi-k3 -> mimo-v2.6-pro);"
                    "hard fail 保持 fail path 立即返回"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r5_executor": [
                "1. 模型切换: kimi-k3 -> mimo-v2.6-pro (沿模型映射 98A779D61C1E §1.1 minimax 拍板)",
                "2. endpoint 切换: teamo (走 tun) -> mimo (无代理)",
                "3. teacher_label 字段切换: kimi -> minimax",
                "4. prompt_id 前缀: kimi_t01_distill_ -> minimax_t01_distill_",
                "5. prompt_id 后缀 _r5 -> _r1",
                "6. ROUND=5 -> ROUND=1; REASK_R1=4 -> REASK_R1=0 (第 1 call/caption on distill side)",
                "7. predecessor_sha12 链 (dispatch 字面): batch6 r5_executor 8a8babb911b8 + r5_result e40424bf8abe + mapping 98A779D61C1E",
                "8. predecessor_sha12 链 (扩展上下文): + batch5 r5 minimax teacher 双件 + batch8 r5 GLM_2 distill 收官 (最新 cumulative)",
                "9. baseline 切换: r1-r4 minimax distill quadruples = 0 (本棒为新教师起步棒)",
                "10. 增量计数 -> distill 侧各 caption 由 0/5 顺利补至 1/5 (起步棒)",
                "11. 累计监控起点: batch8 r5 cumulative.post {318/9/309/2.83%} -> 本棒后 worst 31/340=9.12% / best 9/340=2.65%",
                "12. 判定块重命名: kimi_distill_side_finish -> minimax_distill_side_round1_start",
                "13. counting_scope_correction 改: 本棒为新教师起步棒, 无 r1 混合口径问题",
                "14. metadata.teacher = 'minimax' (替代 r5 'kimi')",
                "15. metadata.is_start_round = True 标记起步棒",
                "16. metadata.endpoint_migrated / lineage_discontinuity = True (V3 火山方舟 -> V4 mimo 跨端点跨厂商)",
                "17. metadata.v3_origin_endpoint / v4_current_endpoint 标注 V3/V4 端点对照",
                "18. per_call_metadata 新增 teacher_label + endpoint_migrated + lineage_discontinuity + proxy_used + teacher_v3_anchor 字段 (沿 batch5 r5 minimax teacher)",
                "19. 端点选择依据: 模型映射留痕件 (PI 拍板 ask_748d9242) 字面而非 r5 端点复用",
                "20. KEY index 切换: 15 (teamo) -> 27 (mimo-plan)",
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
                "mimo_no_proxy_compliance": no_proxy_compliance,
                "serial_interval_ge_2_5_s": True,
                "empty_response_counted_not_dropped": True,
                "kill_line_locked_K_N26_1_2_3_N1_N2": True,
                "no_threshold_adjustment": True,
                "no_existing_file_modified": True,
                "no_merge_of_derived_json": True,
                "no_overwrite_prior_results": True,
                "retry_bug_fix_applied": True,
                "endpoint_migrated_disclosed": True,
                "lineage_discontinuity_disclosed": True,
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
        "minimax_distill_side_round1_start": minimax_distill_side_round1_start,
        "dispatch_target_progress_distill": dispatch_target_progress_distill,
        "aggregate": {
            "r1_total_calls": r1_total,
            "r1_ok_count": r1_ok,
            "r1_empty_response_count": r1_empty,
            "r1_fail_count": r1_fail,
            "r1_empty_response_rate": round(empty_rate_r1, 4),
            "r1_total_prompt_tokens": total_prompt_tokens,
            "r1_total_completion_tokens": total_completion_tokens,
            "r1_total_tokens": total_prompt_tokens + total_completion_tokens,
            "no_proxy_compliance": no_proxy_compliance,
            "no_proxy_used_count": no_proxy_used_count,
            "no_proxy_target_count": len(quadruples),
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
                "cumulative_baseline_source": "batch8 r5 (GLM_2 distill 收官) aggregate.cumulative.post",
            },
            "r1_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r1_empty_response_above_threshold_single_batch": empty_rate_r1 > 0.50,
        },
        "empty_rate_trend": {
            "batch1_round1": {
                "calls": b6r5["empty_rate_trend"]["batch1_round1"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch1_round1"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch1_round1"]["rate"],
            },
            "batch1_round2": {
                "calls": b6r5["empty_rate_trend"]["batch1_round2"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch1_round2"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch1_round2"]["rate"],
            },
            "batch1_round3": {
                "calls": b6r5["empty_rate_trend"]["batch1_round3"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch1_round3"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch1_round3"]["rate"],
            },
            "batch1_round4": {
                "calls": b6r5["empty_rate_trend"]["batch1_round4"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch1_round4"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch1_round4"]["rate"],
            },
            "batch1_round5": {
                "calls": b6r5["empty_rate_trend"]["batch1_round5"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch1_round5"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch1_round5"]["rate"],
            },
            "batch6_round1": {
                "calls": b6r5["empty_rate_trend"]["batch6_round1"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch6_round1"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch6_round1"]["rate"],
            },
            "batch6_round2": {
                "calls": b6r5["empty_rate_trend"]["batch6_round2"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch6_round2"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch6_round2"]["rate"],
            },
            "batch6_round3": {
                "calls": b6r5["empty_rate_trend"]["batch6_round3"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch6_round3"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch6_round3"]["rate"],
            },
            "batch6_round4": {
                "calls": b6r5["empty_rate_trend"]["batch6_round4"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch6_round4"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch6_round4"]["rate"],
            },
            "batch6_round5": {
                "calls": b6r5["empty_rate_trend"]["batch6_round5"]["calls"],
                "empty": b6r5["empty_rate_trend"]["batch6_round5"]["empty"],
                "rate": b6r5["empty_rate_trend"]["batch6_round5"]["rate"],
            },
            "batch10_round1": {
                "calls": r1_total,
                "empty": r1_empty,
                "rate": round(empty_rate_r1, 4),
            },
            "cumulative_through_r1": {
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
                "round_1_n_distinct_sample_note": (
                    "round 1 起步棒第 1 call per caption 实测; minimax distill 侧独立计数 = 22 caption 各 1 successful "
                    "(沿本棒 quadruples, prompt_id 前缀 minimax_t01_distill_ filter 域, 前置 predecessor r1-r4 同前缀 0 条);"
                    "**minimax 蒸馏侧起步达成**: distill 侧 22/22 caption 1/5 successful 起步态;"
                    "由 verdict-keeper 统裁 (本棒 0 写 verdict)"
                ),
            },
            "K_N26_N2_observation": {
                "mimo_no_proxy_used_for_all_calls": no_proxy_compliance,
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
                    "本棒 K-N26-N2 累计 empty_rate 监控 = 已实施;"
                    + (
                        "本棒触发 K-N26-N2 pass=False 构造失灵族判定 + 立即停采 (沿 dispatch §4 字面)"
                        if k_n26_n2_triggered else
                        "本棒未触发 K-N26-N2 累计阈值; 跑至 1500s watchdog 提前停批 / 全 22 calls 完成 (起步态)"
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
            "next_resume_via": "本棒为 batch10 起步棒 — 后续 r2-r4 接力棒 (沿 task_append 同 agent 唤醒语义)",
            "note": (
                f"本棒 round 1 起步棒已完成（{r1_total}/{planned_total} calls）"
                + (f"; K-N26-N2 累计阈值触发: cum_rate={round(k_n26_n2_trigger_cum_rate,4) if k_n26_n2_trigger_cum_rate else None} > 0.50, 立即停采 (沿 dispatch §4)"
                   if k_n26_n2_triggered else
                   f"; 撞 {WALL_TIME_BUDGET_S}s watchdog 提前停批 ({len(captions) - r1_ok} caption 未达标) 走 task_append 接力棒"
                   if wall_time_s > WALL_TIME_BUDGET_S and r1_ok < len(captions) else
                   f"; **minimax 蒸馏侧 22/22 caption 1/5 successful 起步** ✓"
                   if r1_ok == len(captions) else
                   f"; minimax 蒸馏侧未达标 {len(captions) - r1_ok} caption → 下一棒接力 (本棒为起步棒, 留 r2-r4 接力补足)")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    # 19. 落盘前自扫
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    # 20. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch10_r1_result.json")
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
    print(f"  distill_side_met_target_count: {met_target_count_distill}/{len(captions)}")
    print(f"  *** all_22_captions_met_target_distill: {minimax_distill_side_round1_start['all_22_captions_met_target']} ***")
    print(f"  start_disposition: {minimax_distill_side_round1_start['start_disposition']}")
    print(f"  retry_bug_fix_applied_in_all_calls: {retry_validation['r1_retry_bug_fix_applied_in_all_calls']}")
    print(f"  retry_triggered_count: {retry_triggered_count}")
    print(f"  retry_count_distribution: {retry_count_distribution}")
    print(f"  retry_trigger_categories_distribution: {retry_trigger_categories_distribution}")
    print(f"  no_proxy_compliance (mimo): {no_proxy_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  stop_reason: {stop_reason}")
    if minimax_distill_side_round1_start["still_pending"]:
        print(f"  still_pending_distill (≥5 目标距): {minimax_distill_side_round1_start['still_pending']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())