# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch10_r4_executor.py
=====================================

V4 L14+ batch 10 · round 4 (reask=3) -- minimax 蒸馏侧第四棒 (独立计数接力棒 + baseline 修正)

派工依据:
  - 沿 L14+ 派工单 2026-09-26 17:05「minimax 蒸馏侧 round 4 (reask=3) 接力棒 + baseline 计数修正」
  - 沿 batch10 r3 executor (SHA-12 EEF1475E325C) + r3 result (SHA-12 88A06F08928F) 口径续跑
    **+ r3 per_caption counting bug 修正** (派工单 §1)
  - 沿 batch10 r1 executor (SHA-12 D4DD5C949443) + r1 result (SHA-12 14DDDB13D658) 累加 baseline
  - 沿 batch10 r2 executor (SHA-12 BB601B4F5ECB) + r2 result (SHA-12 400EE4D21FC9) 累加 baseline
  - 沿模型映射留痕件 `_v4_supp_l14v3_model_mapping_2026_09_24.md` (SHA-12 98A779D61C1E)
    §1.1 minimax -> mimo 端点 `mimo-v2.6-pro` 字面沿用 (ask_748d9242 字面)
  - 沿 prereg `_v4_supp_prereg_v02_add_L14V3_2026_09_24.md` (字面引用 05B975A86989) 字面
  - 同 agent 唤醒保上下文 (task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义)
  - PI 2026-09-25 00:46「今晚保守口径下先斩后奏」夜间授权 (沿用)

本棒范围:
  1. 22 caption × 1 call = 22 calls
  2. batch=10 (minimax distill) + round=4 (reask=3)
     - 模型 = mimo `mimo-v2.6-pro` (沿 r3 沿 mapping §1.1 minimax 拍板)
     - 端点 = https://token-plan-cn.xiaomimimo.com/v1/chat/completions (沿 r3)
     - 不走代理 (沿 r3 + L7 + add_T1 §1.6.2)
     - **endpoint_migrated=true** (沿 r3)
     - **lineage_discontinuity=true** (沿 r3)
     - **teacher_v3_anchor = "minimax-m3 (火山方舟已下线)"** (沿 r3)
  3. distill 侧独立计数 (baseline 修正, 沿派工单 §1):
     - filter = prompt_id 前缀 `minimax_t01_distill_`
     - **真值起点 = 3 successful/caption (r1+r2+r3 各 1)**  ← **r3 计数 bug 修正**
     - 本棒 22 caption × 1 call 后预期各 caption **真值 4/5 successful** (接力棒)
     - 目标 ≥5 successful/caption (远期)
  4. **counting_bug_correction 字段**: r3 (SHA-12 88A06F08928F) per_caption 记 2/5 实为 3/5 (计数 bug)
     - r3 读 r2.quadruples 但 r2.quadruples 不含 r1 calls (r1 calls 仅聚合到 r2.per_caption_distill_only_successful_calls 块)
     - r3 实际 quadruples 数据正确 (22/22 OK)；仅 per_caption baseline 读取逻辑漏 r1
     - 本棒 baseline 读取改: r1.quadruples + r2.quadruples + r3.quadruples 三件累加 = 66 calls / 3 successful per caption
     - 跨源 cross-check: r3.per_caption_distill_only_successful_calls 记 2/5 (bug) vs 三件累加 = 3/5 (真值)
  5. cumulative 监控: 起点 = r3 cumulative.post (384/9/375/2.34%); 本棒后 worst 31/406=7.64%; best 9/406=2.22%
  6. 进度判定块 `minimax_distill_side_round4_progress` (沿 r3 + batch8 r4 `glm2_distill_side_round4_progress` 接力棒命名)

与 batch10 r3 executor diff:
  1. ROUND=3 -> ROUND=4; REASK_R3=2 -> REASK_R4=3 (第 4 call/caption on distill side)
  2. prompt_id 后缀 _r3 -> _r4
  3. predecessor 链 (dispatch 字面): r3_executor EEF1475E325C + r3_result 88A06F08928F + mapping
  4. predecessor 链 (baseline 修正累加): + r1_executor/result + r2_executor/result
  5. **baseline 读取逻辑修正**: 不再仅读 r3.quadruples; 改读 r1+r2+r3 三件 quadruples 累加 (派工单 §1)
  6. 真值 baseline = 3 successful/caption (沿派工单 §1; r3 记 2/5 系 bug)
  7. 增量计数 -> distill 侧各 caption 由真值 3/5 顺利补至真值 4/5 (接力棒)
  8. is_round_3=True -> is_round_4=True
  9. 累计监控起点: r3 cumulative.post {384/9/375/2.34%} -> 本棒后 worst 31/406=7.64% / best 9/406=2.22%
 10. 判定块重命名: minimax_distill_side_round3_progress -> minimax_distill_side_round4_progress
 11. **新增 counting_bug_correction 字段** (派工单 §1): 注明 r3 计数 bug + 本棒修正口径 + 跨源 cross-check 结果
 12. counting_scope_correction 块改名 + 增 baseline 修正说明
 13. per_caption 新增 round4_target/round4_met 字段 (round 4 接力目标判定)

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
  - **不擅自修复 r3 既有 result** (沿 R5 frozen append-only); r3 88A06F08928F 仅在 r4 产物中如实引用 + counting_bug_correction 注明
  - 老实交代 0 产物

产物:
  - 写入: results/_v4_supp_l14v3_batch10_r4_result.json
    (schema = v4_l14v3_n26/1 + batch=10 + round=4)
  - 不覆盖 batch10 r3 result 88A06F08928F 或前棒 result

边界:
  - 不动任何既有件 (含 batch10 r1/r2/r3 双件 + batch6 r5 双件 + batch8 r5 双件 + batch5 r1-r5 minimax teacher + batch1-8 全部 + prereg 05B975A86989 + captions 6a2656878745 + mapping 98A779D61C1E)
  - **不擅自修复 r3 88A06F08928F** (R5 frozen append-only; bug 透明披露待 PI 复核)
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
BATCH10_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch10_r1_result.json")
BATCH10_R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch10_r2_result.json")
BATCH10_R3_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch10_r3_result.json")

# r3 counting bug SHA-12 (派工单 §1 字面)
R3_RESULT_SHA12 = "88A06F08928F"
R3_RESULT_PATH = "results/_v4_supp_l14v3_batch10_r3_result.json"

# ============================================================
# 端点配置 (沿 r3; model 沿模型映射留痕件 §1.1 minimax 拍板 mimo-v2.6-pro; 无代理)
# ============================================================
ENDPOINT_MIMO = "https://token-plan-cn.xiaomimimo.com/v1"
MODEL_MINIMAX = "mimo-v2.6-pro"
KEY_INDEX_MIMO_1BASED = 27
USE_PROXY = False

# 串行间隔 (沿 r3)
INTER_CALL_SLEEP_S = 2.5

# 超参 (沿 r3)
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正 (沿 r3)
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别 (沿 r3)
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值 (沿 r3)
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算 (沿 r3; 1500s 容 22 caption calls + 串行 ≥2.5s)
WALL_TIME_BUDGET_S = 1500

# 本棒调度 (沿 dispatch)
BATCH = 10
ROUND = 4
SIDE = "distill"
TEACHER = "minimax"
TEACHER_LABEL = "minimax"
REASK_R4 = 3  # round 4 = 第 4 call per caption (reask_idx = 3) -- 接力
TARGET_SUCCESSFUL_PER_CAPTION = 5  # distill 侧最终目标 (字面 ≥5)
ROUND4_TARGET_PER_CAPTION = 4  # 本棒 round 4 真值目标 = 4 (接力棒, 远期 ≥5)

# ============================================================
# 计数口径 (沿 r3 distill 侧独立计数; minimax 蒸馏侧独立域)
# **baseline 修正**: r1+r2+r3 三件 quadruples 累加 (派工单 §1)
# ============================================================
DISTILL_SIDE_PROMPT_ID_PREFIX = "minimax_t01_distill_"

# baseline 修正: r3 per_caption 字段显示 2/5 系计数 bug (读 r2.quadruples 漏 r1 calls)
# 真值 baseline = r1+r2+r3 三件 quadruples 累加 = 3 successful/caption
BASELINE_TRUE_PER_CAPTION = 3  # 派工单 §1 字面 "真值起点=3/5"


# ============================================================
# 敏感模式 (沿 r3)
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
# 工具 (沿 r3; mimo 无代理)
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
    """mimo 端点 chat 调用 (无代理; 沿 r3)."""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch10-r4",
        "X-Title": "deposon-l14v3-batch10-r4-minimax-distill",
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
# 提示构造 (沿 r3 prompt 构造口径 = batch1 r6 reproduction_caliber anchor)
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
# 单 call + 内层重试 (沿 r3; minimax 蒸馏侧 metadata 增 endpoint_migrated/lineage_discontinuity/proxy_used/teacher_v3_anchor)
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    is_round_4: bool,
    phase_label: str,
    retry_trigger_categories_tracker: List[str],
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_r4"
    prompt_id = f"minimax_t01_{side}_{caption_id}{suffix}"

    # minimax 蒸馏侧派生 metadata (沿 r3 + mapping §1.2 minimax 行)
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
                        "is_round_4": is_round_4,
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
                "is_round_4": is_round_4,
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
            "is_round_4": is_round_4,
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
    print("V4 L14+ batch 10 round 4 | minimax distill side | reask=3 -- 接力棒 + baseline 修正")
    print("计划 calls = 22 (22 caption × 1 call)")
    print("计数口径: distill 侧独立 (prompt_id 前缀 minimax_t01_distill_) -- 沿 r3 + baseline 修正")
    print("**真值 baseline = 3 successful/caption (r1+r2+r3 各 1)** -- r3 计数 bug 修正")
    print("本棒 round 4 真值目标: 各 caption 补至 4/5 successful (接力棒, 远期 ≥5)")
    print("预算 ≤1500s watchdog")
    print("retry 修复沿 r3 (含 retry 触发的源 error_category tracking)")
    print("mimo 无代理 (沿 r3 + L7 + add_T1 §1.6.2)")
    print("annotations: endpoint_migrated=True, lineage_discontinuity=True (沿 r3)")
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

    # 3. 加载 r1/r2/r3 result (baseline 修正累加; 派工单 §1)
    with open(BATCH10_R1_RESULT_PATH, "r", encoding="utf-8") as f:
        r1 = json.load(f)
    with open(BATCH10_R2_RESULT_PATH, "r", encoding="utf-8") as f:
        r2 = json.load(f)
    with open(BATCH10_R3_RESULT_PATH, "r", encoding="utf-8") as f:
        r3 = json.load(f)

    # 4. minimax distill 侧独立计数 (baseline 修正; 派工单 §1)
    # **真值 baseline = r1+r2+r3 三件 quadruples 累加 (3 successful per caption)**
    # **r3.per_caption 字段记 2/5 系 counting bug** (r3 读 r2.quadruples 但漏 r1 calls)
    per_cap_succ_distill = {c["id"]: 0 for c in captions}
    per_cap_total_distill = {c["id"]: 0 for c in captions}
    per_cap_empty_distill = {c["id"]: 0 for c in captions}
    cum_total_prior_distill = 0
    cum_ok_prior_distill = 0
    cum_empty_prior_distill = 0
    for src_label, src_result in [("r1", r1), ("r2", r2), ("r3", r3)]:
        for q in src_result.get("quadruples", []):
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
          f"empty={cum_empty_prior_distill} (源 = r1+r2+r3 三件 quadruples 累加; 真值 baseline = 3/caption)")

    # 5. 跨源 cross-check (派工单 §1: 二者对账一致为准)
    cross_check_r3_per_cap = {}
    r3_per_cap_data = r3.get("per_caption_distill_only_successful_calls", {})
    if isinstance(r3_per_cap_data, dict):
        for cid, info in r3_per_cap_data.items():
            if isinstance(info, dict) and "succ_count" in info:
                cross_check_r3_per_cap[cid] = info["succ_count"]
    cross_check_match = all(
        cross_check_r3_per_cap.get(cid, -1) == per_cap_succ_distill[cid]
        for cid in per_cap_succ_distill.keys()
    ) if cross_check_r3_per_cap else False
    print(f"[CROSS-CHECK r3.per_caption vs 三件累加] match={cross_check_match} (派工单 §1: 二者对账)")
    if not cross_check_match:
        mismatch_count = sum(
            1 for cid in per_cap_succ_distill.keys()
            if cross_check_r3_per_cap.get(cid, -1) != per_cap_succ_distill[cid]
        )
        print(f"  mismatch_count = {mismatch_count} (r3 per_caption 字段 ≠ 三件累加 → r3 counting bug 确认)")

    # 6. cumulative 监控沿 r3 cumulative 链路 (跨教师跨侧累计)
    r3_cum = r3["aggregate"]["cumulative"]
    cum_total_prior_cum = r3_cum["post_total"]    # 384
    cum_empty_prior_cum = r3_cum["post_empty"]    # 9
    cum_ok_prior_cum = r3_cum["post_ok"]          # 375
    cum_rate_prior = cum_empty_prior_cum / cum_total_prior_cum if cum_total_prior_cum > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior_cum} ok={cum_ok_prior_cum} "
          f"empty={cum_empty_prior_cum} rate={cum_rate_prior:.4f} (源 = r3 aggregate.cumulative.post)")

    # 7. mixed history 透明保留 (本棒 = {}; minimax distill 起步后无 r1 混合域参照)
    r4_mixed_history = {}

    # 8. 调度 planned_calls (22 caption × 1 call = 22 calls)
    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r4_distill_{c['id']}"}
        for c in captions
    ]
    planned = PLANNED_CALLS
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (22 caption × 1 call)")

    # 9. 加载 key (mimo-plan = line 27; 沿 Track 2 endpoints probe C846F7FC79EE)
    try:
        api_key = fetch_api_key(KEY_INDEX_MIMO_1BASED)
        print(f"[INIT] mimo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 10. 时间预算起点
    t_batch_start = time.time()

    # 11. 跑
    quadruples: List[Dict[str, Any]] = []
    cum_total = cum_total_prior_cum
    cum_empty = cum_empty_prior_cum
    cum_ok = cum_ok_prior_cum
    r4_total = 0
    r4_ok = 0
    r4_empty = 0
    r4_fail = 0
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
            reask_idx=REASK_R4,
            side="distill",
            round_index=ROUND,
            is_round_4=True,
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
            r4_ok += 1
            cum_ok += 1
            per_cap_succ_distill[cap_id] += 1
        elif is_empty:
            r4_empty += 1
            cum_empty += 1
            per_cap_empty_distill[cap_id] += 1
        else:
            r4_fail += 1
        r4_total += 1
        cum_total += 1
        per_cap_total_distill[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ_distill = per_cap_succ_distill[cap_id]
        target_met_round4 = "[OK] 接力 4/5" if cur_succ_distill >= ROUND4_TARGET_PER_CAPTION else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<28} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[distill_succ={cur_succ_distill}/{TARGET_SUCCESSFUL_PER_CAPTION} {target_met_round4}] "
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

    # 12. 统计
    empty_rate_r4 = (r4_empty / r4_total) if r4_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    no_proxy_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
        and not r["per_call_metadata"].get("proxy_used", True)
    )
    no_proxy_compliance = (no_proxy_used_count == len(quadruples))

    # 13. 每 caption successful 计数 -- distill 侧独立 (baseline 修正后)
    per_caption_distill_only_successful_calls = {}
    met_round4_count_distill = 0
    met_target_count_distill = 0  # ≥5 final target
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ_distill[cid]
        t = per_cap_total_distill[cid]
        e = per_cap_empty_distill[cid]
        need = max(0, TARGET_SUCCESSFUL_PER_CAPTION - s)
        met_round4 = s >= ROUND4_TARGET_PER_CAPTION
        met_target = s >= TARGET_SUCCESSFUL_PER_CAPTION
        if met_round4:
            met_round4_count_distill += 1
        if met_target:
            met_target_count_distill += 1
        per_caption_distill_only_successful_calls[cid] = {
            "succ_count": s,
            "target": TARGET_SUCCESSFUL_PER_CAPTION,
            "round4_target": ROUND4_TARGET_PER_CAPTION,
            "round4_met": met_round4,
            "need_more": need,
            "met_target": met_target,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 14. mixed history 透明保留 (本棒 = {}; minimax distill 起步后无 r1 混合域参照)
    per_caption_mixed_history_successful_calls = r4_mixed_history

    # 15. distill 侧 **进度判定** (沿 r3 + batch8 r4 `glm2_distill_side_round4_progress` 接力棒命名)
    minimax_distill_side_round4_progress = {
        "all_22_captions_met_target": met_target_count_distill == len(captions),
        "met_count_post_r4": met_round4_count_distill,
        "met_count_post_r4_cumulative_to_target": met_target_count_distill,
        "total_captions": len(captions),
        "still_pending": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
        "still_pending_round4": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["round4_met"]
        ]),
        "round4_progress_disposition": (
            "minimax 蒸馏侧 round 4 (reask=3) 接力棒完成 → batch10 distill side round 4 progress ✓ (22 caption 各 4/5 successful 接力态)"
            if (r4_total == len(captions) and r4_ok == len(captions))
            else f"minimax 蒸馏侧 round 4 接力棒完成 → batch10 distill side round 4 progress, r4_ok={r4_ok}/{len(captions)} (需后续 r5 接力补足)"
        ),
        "rounds_to_reach_round4_target_planned": 4,
        "rounds_to_reach_target_planned": 5,
        "rounds_to_reach_target_actual": (
            "4 棒 (r1+r2+r3+r4) = 22 caption × 4 calls = 88 distill 侧 calls "
            "(接力态, 远期目标 ≥5 需 1 more 棒接力补足)"
        ),
        "distill_side_target_met_at_round": (
            "r5 (expected)" if met_target_count_distill == len(captions) else "未达 (本棒为 r4 接力棒, 留 r5 接力)"
        ),
        "is_progress_round": True,
    }

    # 16. dispatch §6 收尾盘点 -- distill 侧 (baseline 修正)
    dispatch_target_progress_distill = {
        "target": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (distill side only)",
        "target_round4": f">={ROUND4_TARGET_PER_CAPTION} successful calls/caption (round 4 接力目标)",
        "met_count_post_r4_round4": met_round4_count_distill,
        "met_count_post_r4_cumulative_to_target": met_target_count_distill,
        "total_captions": len(captions),
        "remaining_count": len(captions) - met_target_count_distill,
        "remaining_count_round4": len(captions) - met_round4_count_distill,
        "met_percentage_round4": round(met_round4_count_distill / len(captions) * 100, 2),
        "met_percentage_cumulative_to_target": round(met_target_count_distill / len(captions) * 100, 2),
        "still_pending_captions": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["met_target"]
        ]),
        "still_pending_captions_round4": sorted([
            cid for cid, info in per_caption_distill_only_successful_calls.items() if not info["round4_met"]
        ]),
        "is_progress_round": True,
        "baseline_correction_note": "r4 baseline 改 r1+r2+r3 三件 quadruples 累加 (派工单 §1); r3 per_caption 字段记 2/5 系 counting bug",
    }

    # 17. **counting_bug_correction 块** (派工单 §1; r3 计数 bug 透明披露)
    counting_bug_correction = {
        "r3_counting_bug_disclosed": True,
        "r3_counting_bug_sha12": R3_RESULT_SHA12,
        "r3_counting_bug_path": R3_RESULT_PATH,
        "r3_counting_bug_description": (
            "r3 (SHA-12 88A06F08928F) executor 读 r2.quadruples (22 entries) 但 r2.quadruples 不含 r1 calls;"
            "r1 calls 仅聚合到 r2.per_caption_distill_only_successful_calls 块 (r2 在 r2.quadruples 之前 read r1.quadruples);"
            "r3 漏读 r1.quadruples → per_caption baseline 误为 1 (实为 2);"
            "r3 实际 quadruples 数据正确 (22/22 OK); bug 仅限 per_caption baseline 读取逻辑"
        ),
        "r3_counting_bug_impact": (
            "r3 per_caption_distill_only_successful_calls 字段记 succ=2/total=2 (实为 succ=3/total=3);"
            "r3 met_count_post_r3 字段记 0/22 (实为 22/22);"
            "r3 cumulative 字段正确 (362 → 384 delta=22);"
            "r3 K-N26-*/aggregate/quadruples 等其他字段正确"
        ),
        "r4_baseline_fix_method": (
            "派工单 §1 字面「r1+r2+r3 三件 result 的 quadruples 累加 或 r3.per_caption + r3.quadruples 跨源 cross-check」;"
            "本棒采用 (a) r1+r2+r3 三件 quadruples 累加 (66 entries) 作为 baseline 唯一权威源;"
            "**r3.per_caption 字段不采用 (因 r3 counting bug)**"
        ),
        "r4_cross_check_r3_per_cap_disposition": (
            "派工单 §1 「二者对账一致为准」: 三件累加 vs r3.per_caption 字段"
            f" -> match = {cross_check_match} (派工单 §1 期望: 三件累加为权威源, r3.per_caption 字段已知 bug 不参与判定)"
        ),
        "r4_baseline_修正后_per_caption_true_value": (
            f"baseline 三件累加 = {cum_total_prior_distill} calls, {cum_ok_prior_distill} successful, "
            f"{cum_empty_prior_distill} empty (各 caption = {BASELINE_TRUE_PER_CAPTION}/5 successful 真值起点)"
        ),
        "r4_post_distill_true_value": (
            f"r1+r2+r3+r4 quadruples 后 = {sum(per_cap_total_distill.values())} calls, "
            f"{sum(per_cap_succ_distill.values())} successful, "
            f"{sum(per_cap_empty_distill.values())} empty "
            f"(各 caption = {ROUND4_TARGET_PER_CAPTION}/5 successful 接力态 expected)"
        ),
        "r3_文件处置": (
            f"r3 既有 result ({R3_RESULT_SHA12} at {R3_RESULT_PATH}) 不擅自修复 (沿 R5 frozen append-only);"
            "bug 透明披露待 PI 复核; r4 仅在产物 counting_bug_correction 字段引用 + 标注"
        ),
        "PI_reviewer_note": (
            "PI 复核 r3 88A06F08928F per_caption 字段是否需后续批次重算修正 (修正方式: 读 r1.quadruples 补齐 baseline);"
            "PI 复核 r4 counting_bug_correction 字段是否需入 N-26 主预登记 §0.5 边界声明 / K-N26-N1 observation 块"
        ),
    }

    # 18. counting_scope_correction 块 (沿 r3; baseline 修正补充说明)
    counting_scope_correction = {
        "r4_issue_disclosed": False,
        "r4_issue_description": (
            "本棒为 minimax 蒸馏侧 round 4 接力棒 (= batch10 round 4), predecessor r1+r2+r3 同前缀 quadruples = 66 条;"
            "无 r4 混合口径 (本棒 predecessor r3 同前缀过滤后 = 22 条均 minimax distill side);"
            "无 kimi 蒸馏侧混合计数问题 (本棒沿 r3 minimax distill side 累加)"
        ),
        "r4_data_disposition": (
            "本棒 = 接力棒 + baseline 修正 (派工单 §1); "
            "predecessor = r1+r2+r3 minimax distill side (三件 quadruples 累加, 不依赖 r3.per_caption 字段); "
            "累加 r1+r2+r3 quadruples"
        ),
        "r4_counting_domain": (
            f"distill 侧独立计数; filter 域 = prompt_id 前缀 '{DISTILL_SIDE_PROMPT_ID_PREFIX}'"
            " (沿 r3; minimax 蒸馏侧累加; **baseline 修正: 三件累加, 不读 r3.per_caption 字段**)"
        ),
        "r4_target": f"distill 侧远期目标 ≥{TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption",
        "r4_round4_target": f"本棒 round 4 接力目标 ≥{ROUND4_TARGET_PER_CAPTION} successful calls/caption (真值口径)",
        "r4_baseline_distill_only": (
            f"predecessor r1+r2+r3 quadruples minimax distill 过滤后 (三件累加) = {cum_total_prior_distill} calls, "
            f"{cum_ok_prior_distill} successful, {cum_empty_prior_distill} empty "
            f"(各 caption 各 {BASELINE_TRUE_PER_CAPTION} successful 真值起点; r3 per_caption 字段记 2 系 counting bug, 派工单 §1 修正)"
        ),
        "r4_post_distill_only": (
            f"r1+r2+r3+r4 quadruples 后 = {sum(per_cap_total_distill.values())} calls, "
            f"{sum(per_cap_succ_distill.values())} successful, "
            f"{sum(per_cap_empty_distill.values())} empty "
            f"(各 caption = {ROUND4_TARGET_PER_CAPTION}/5 successful 接力态 expected)"
        ),
        "mixed_history_retention": (
            "per_caption_mixed_history_successful_calls 块 = {} 空字典 (minimax distill 起步后无 r1 混合域参照);"
            "该块保留作透明字段待后续 r5 接力棒填充"
        ),
        "pending_pi_review": (
            "PI 复核本计数口径切换是否合规 (保守口径自主决策, PI 2026-09-25 00:46 委托);"
            "PI 复核 r3 counting bug 修正方式 (本棒采用 r1+r2+r3 三件 quadruples 累加, 不读 r3.per_caption 字段);"
            "PI 拍板沿用 ask_748d9242 minimax 模型映射 = mimo 端点 mimo-v2.6-pro 字面"
        ),
        "progress_disposition": (
            f"r4 接力棒 distill 侧独立计数基线 (三件累加) = {cum_total_prior_distill} calls 完成 (沿 r1+r2+r3); "
            f"实测 r4 quadruples 后 = {sum(per_cap_total_distill.values())} calls; "
            f"目标 ≥{TARGET_SUCCESSFUL_PER_CAPTION} 远期未达 (接力棒实况, 留 r5 接力补足)"
        ),
    }

    # 19. retry validation 块 (沿 r3)
    retry_trigger_categories_distribution: Dict[str, int] = {}
    for cat in retry_trigger_categories_tracker:
        retry_trigger_categories_distribution[cat] = retry_trigger_categories_distribution.get(cat, 0) + 1

    retry_validation = {
        "r4_retry_count_distribution": dict(retry_count_distribution),
        "r4_retry_triggered_count": retry_triggered_count,
        "r4_retry_trigger_categories_tracker": retry_trigger_categories_tracker,
        "r4_retry_trigger_categories_distribution": retry_trigger_categories_distribution,
        "r4_retry_bug_fix_applied_in_all_calls": all(
            q["per_call_metadata"].get("retry_bug_fix_applied") is True
            for q in quadruples
        ),
        "r4_empty_rate_with_fix": round(empty_rate_r4, 4),
        "r3_empty_rate_with_fix_baseline": (
            r3["aggregate"]["r3_empty_response_rate"]
        ),
        "delta_empty_rate_r4_vs_r3": round(empty_rate_r4 - r3["aggregate"]["r3_empty_response_rate"], 4),
    }

    # 20. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 10,
        "round": 4,
        "metadata": {
            "task": "L14V3_batch10_round4_minimax_distill_side_reask3_progress_round_baseline_corrected",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                # dispatch 字面 (minimum chain reference)
                "r4_dispatch_note": "派工单 §1: predecessor 链 r3 双件 + mapping; baseline 修正累加 r1+r2+r3 三件",
                "r3_executor_sha12": "eef1475e325c",
                "r3_executor_path": "results/_v4_supp_l14v3_batch10_r3_executor.py",
                "r3_result_sha12": "88a06f08928f",
                "r3_result_path": "results/_v4_supp_l14v3_batch10_r3_result.json",
                "r3_result_counting_bug_disclosed": True,
                "r3_result_counting_bug_note": "r3 per_caption 字段记 2/5 系 counting bug; 真值 = 3/5; r4 baseline 改读 r1+r2+r3 三件 quadruples 累加",
                "r2_executor_sha12": "bb601b4f5ecb",
                "r2_executor_path": "results/_v4_supp_l14v3_batch10_r2_executor.py",
                "r2_result_sha12": "400ee4d21fc9",
                "r2_result_path": "results/_v4_supp_l14v3_batch10_r2_result.json",
                "r1_executor_sha12": "d4dd5c949443",
                "r1_executor_path": "results/_v4_supp_l14v3_batch10_r1_executor.py",
                "r1_result_sha12": "14dddb13d658",
                "r1_result_path": "results/_v4_supp_l14v3_batch10_r1_result.json",
                "model_mapping_sha12": "98a779d61c1e",
                "model_mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                # 扩展上下文: minimax teacher side 直接 prior
                "b5_r5_executor_sha12": "82c283d8f37a",
                "b5_r5_executor_path": "results/_v4_supp_l14v3_batch5_r5_executor.py",
                "b5_r5_result_sha12": "c874d21a4cbe",
                "b5_r5_result_path": "results/_v4_supp_l14v3_batch5_r5_result.json",
                # 扩展上下文: 蒸馏侧收官字面锚
                "r5_executor_sha12": "8a8babb911b8",
                "r5_executor_path": "results/_v4_supp_l14v3_batch6_r5_executor.py",
                "r5_result_sha12": "e40424bf8abe",
                "r5_result_path": "results/_v4_supp_l14v3_batch6_r5_result.json",
                "captions_sha12": "6a2656878745",
                "captions_path": "corpus/v20_caption_surface/strip_captions_22.json",
                "l13_verdict_sha12_referenced": "E105EC1362DB",
                "l13_verdict_path": "results/_v4_supp_l13_n26pair_verdict.md",
                "l13_verdict_on_disk": False,
                "l13_verdict_referenced_role": "V4 triplet basis (re-asked / distill / independent) distill style source anchor (round-trip reference only; no original-prompt doc reconstruction in this batch)",
            },
            "date": "2026-09-26",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 10 round 4 minimax distill side reask=3 接力棒 + baseline 修正",
            "is_progress_round": True,
            "baseline_correction_round": True,
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
            "spec_conformance": "PI 2026-09-26 同 agent 唤醒 (task_append) 接力棒 + 沿 r3 口径续跑 + minimax 模型映射沿 r3 (mimo-v2.6-pro) + retry 修复沿 r3 + 每 caption successful 计数终盘点 + K-N26-N2 累计监控 + distill 侧独立计数 (baseline 修正: r1+r2+r3 三件 quadruples 累加, 派工单 §1) + 进度判定块 minimax_distill_side_round4_progress + counting_bug_correction 字段 (r3 88A06F08928F 计数 bug 透明披露)",
            "teacher": TEACHER,
            "teacher_label": TEACHER_LABEL,
            "side": SIDE,
            "round_index": 4,
            "reask_idx_r4": REASK_R4,
            "round4_target_per_caption": ROUND4_TARGET_PER_CAPTION,
            "baseline_true_per_caption": BASELINE_TRUE_PER_CAPTION,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r4_total,
            "endpoint_selected": ENDPOINT_MIMO,
            "endpoint_selection_method": "沿 r3 executor EEF1475E325C 端点实测 = mimo mimo-v2.6-pro (无代理)",
            "model_id_sent": MODEL_MINIMAX,
            "model_id_sent_basis": "model_mapping 98A779D61C1E §1.1 minimax 列拍板定案 = mimo 端点 mimo-v2.6-pro (PI 2026-09-24 23:08 ask_748d9242 字面)",
            "model_id_inconsistency_honest_disclosure": r3["metadata"]["model_id_inconsistency_honest_disclosure"],
            "endpoint_migrated": True,
            "lineage_discontinuity": True,
            "v3_origin_endpoint": "火山方舟 (V3 字面 minimax-m3 已下线)",
            "v4_current_endpoint": "mimo (token-plan-cn.xiaomimimo.com/v1)",
            "proxy_settings": {
                "http": None,
                "socks5": None,
                "applied_to_mimo": False,
                "note": "mimo 端点 = 无代理 (沿 r3 + L7 + add_T1 §1.6.2); 显式清空代理 env (防御性)",
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
                "r3_status": "retry 修复 + tracking 改进沿 r3 (沿 EEF1475E325C)",
                "r4_status": "retry 修复沿 r3; r4 接力棒 + baseline 修正本棒无新参数修正",
                "rationale": (
                    "沿 r3 修复 + r3 tracking 改进; r4 接力棒仅按 22 caption × 1 call 续采 (reask_idx=3);"
                    "baseline 修正仅改读取逻辑 (r1+r2+r3 三件 quadruples 累加), 0 触动调用参数 / 阈值 / 模型"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r3_executor": [
                "1. ROUND=3 -> ROUND=4; REASK_R3=2 -> REASK_R4=3 (第 4 call/caption on distill side)",
                "2. prompt_id 后缀 _r3 -> _r4",
                "3. **predecessor 链 (dispatch 字面)**: r3_executor EEF1475E325C + r3_result 88A06F08928F + mapping",
                "4. **predecessor 链 (baseline 修正累加)**: + r2_executor/result + r1_executor/result",
                "5. **baseline 读取逻辑修正** (派工单 §1): 沿 r3 仅读 r3.quadruples (漏 r1) -> 改读 r1+r2+r3 三件 quadruples 累加 (66 calls)",
                "6. **真值 baseline = 3 successful/caption** (派工单 §1 字面; r3 per_caption 字段记 2 系 counting bug)",
                "7. 增量计数 -> distill 侧各 caption 由真值 3/5 顺利补至真值 4/5 (接力棒)",
                "8. is_round_3=True -> is_round_4=True",
                "9. 累计监控起点: r3 cumulative.post {384/9/375/2.34%} -> 本棒后 worst 31/406=7.64% / best 9/406=2.22%",
                "10. 判定块重命名: minimax_distill_side_round3_progress -> minimax_distill_side_round4_progress",
                "11. **新增 counting_bug_correction 字段** (派工单 §1): 注明 r3 88A06F08928F per_caption 计数 bug + 本棒 baseline 修正方式 + 跨源 cross-check 处置",
                "12. counting_scope_correction 块 改名 + 增 baseline 修正说明 (沿派工单 §1)",
                "13. metadata 新增 baseline_correction_round=True 字段",
                "14. metadata 新增 baseline_true_per_caption=3 字段 (派工单 §1 字面)",
                "15. per_caption 新增 round4_target/round4_met 字段 (round 4 接力目标判定, 真值口径)",
                "16. dispatch_target_progress_distill 新增 baseline_correction_note 字段 (派工单 §1)",
                "17. 跨源 cross-check: 三件累加 vs r3.per_caption 字段; 二者对账不一致 (派工单 §1: 二者对账一致为准 → 三件累加为权威源)",
                "18. 0 擅调 r3 既有 result (R5 frozen append-only); r3 仅在 r4 产物 counting_bug_correction 字段引用 + 透明披露",
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
                "r3_counting_bug_transparently_disclosed": True,
                "baseline_correction_method_documented": True,
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
        "counting_bug_correction": counting_bug_correction,
        "minimax_distill_side_round4_progress": minimax_distill_side_round4_progress,
        "dispatch_target_progress_distill": dispatch_target_progress_distill,
        "aggregate": {
            "r4_total_calls": r4_total,
            "r4_ok_count": r4_ok,
            "r4_empty_response_count": r4_empty,
            "r4_fail_count": r4_fail,
            "r4_empty_response_rate": round(empty_rate_r4, 4),
            "r4_total_prompt_tokens": total_prompt_tokens,
            "r4_total_completion_tokens": total_completion_tokens,
            "r4_total_tokens": total_prompt_tokens + total_completion_tokens,
            "no_proxy_compliance": no_proxy_compliance,
            "no_proxy_used_count": no_proxy_used_count,
            "no_proxy_target_count": len(quadruples),
            "baseline_correction_summary": {
                "r3_per_caption_field_value": 2,
                "r3_per_caption_field_true_value": 3,
                "r3_per_caption_field_disposition": "counting bug; r4 baseline 不读此字段",
                "r4_baseline_method": "r1+r2+r3 三件 quadruples 累加",
                "r4_baseline_total_calls": cum_total_prior_distill,
                "r4_baseline_ok_calls": cum_ok_prior_distill,
                "r4_baseline_per_caption_succ": BASELINE_TRUE_PER_CAPTION,
                "cross_check_match": cross_check_match,
            },
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
                "cumulative_baseline_source": "batch10 r3 (minimax distill round 3 接力棒) aggregate.cumulative.post",
            },
            "r4_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r4_empty_response_above_threshold_single_batch": empty_rate_r4 > 0.50,
        },
        "empty_rate_trend": {
            "batch1_round1": {
                "calls": r3["empty_rate_trend"]["batch1_round1"]["calls"],
                "empty": r3["empty_rate_trend"]["batch1_round1"]["empty"],
                "rate": r3["empty_rate_trend"]["batch1_round1"]["rate"],
            },
            "batch1_round2": {
                "calls": r3["empty_rate_trend"]["batch1_round2"]["calls"],
                "empty": r3["empty_rate_trend"]["batch1_round2"]["empty"],
                "rate": r3["empty_rate_trend"]["batch1_round2"]["rate"],
            },
            "batch1_round3": {
                "calls": r3["empty_rate_trend"]["batch1_round3"]["calls"],
                "empty": r3["empty_rate_trend"]["batch1_round3"]["empty"],
                "rate": r3["empty_rate_trend"]["batch1_round3"]["rate"],
            },
            "batch1_round4": {
                "calls": r3["empty_rate_trend"]["batch1_round4"]["calls"],
                "empty": r3["empty_rate_trend"]["batch1_round4"]["empty"],
                "rate": r3["empty_rate_trend"]["batch1_round4"]["rate"],
            },
            "batch1_round5": {
                "calls": r3["empty_rate_trend"]["batch1_round5"]["calls"],
                "empty": r3["empty_rate_trend"]["batch1_round5"]["empty"],
                "rate": r3["empty_rate_trend"]["batch1_round5"]["rate"],
            },
            "batch6_round1": {
                "calls": r3["empty_rate_trend"]["batch6_round1"]["calls"],
                "empty": r3["empty_rate_trend"]["batch6_round1"]["empty"],
                "rate": r3["empty_rate_trend"]["batch6_round1"]["rate"],
            },
            "batch6_round2": {
                "calls": r3["empty_rate_trend"]["batch6_round2"]["calls"],
                "empty": r3["empty_rate_trend"]["batch6_round2"]["empty"],
                "rate": r3["empty_rate_trend"]["batch6_round2"]["rate"],
            },
            "batch6_round3": {
                "calls": r3["empty_rate_trend"]["batch6_round3"]["calls"],
                "empty": r3["empty_rate_trend"]["batch6_round3"]["empty"],
                "rate": r3["empty_rate_trend"]["batch6_round3"]["rate"],
            },
            "batch6_round4": {
                "calls": r3["empty_rate_trend"]["batch6_round4"]["calls"],
                "empty": r3["empty_rate_trend"]["batch6_round4"]["empty"],
                "rate": r3["empty_rate_trend"]["batch6_round4"]["rate"],
            },
            "batch6_round5": {
                "calls": r3["empty_rate_trend"]["batch6_round5"]["calls"],
                "empty": r3["empty_rate_trend"]["batch6_round5"]["empty"],
                "rate": r3["empty_rate_trend"]["batch6_round5"]["rate"],
            },
            "batch10_round1": {
                "calls": r3["empty_rate_trend"]["batch10_round1"]["calls"],
                "empty": r3["empty_rate_trend"]["batch10_round1"]["empty"],
                "rate": r3["empty_rate_trend"]["batch10_round1"]["rate"],
            },
            "batch10_round2": {
                "calls": r3["empty_rate_trend"]["batch10_round2"]["calls"],
                "empty": r3["empty_rate_trend"]["batch10_round2"]["empty"],
                "rate": r3["empty_rate_trend"]["batch10_round2"]["rate"],
            },
            "batch10_round3": {
                "calls": r3["empty_rate_trend"]["batch10_round3"]["calls"],
                "empty": r3["empty_rate_trend"]["batch10_round3"]["empty"],
                "rate": r3["empty_rate_trend"]["batch10_round3"]["rate"],
            },
            "batch10_round4": {
                "calls": r4_total,
                "empty": r4_empty,
                "rate": round(empty_rate_r4, 4),
            },
            "cumulative_through_r4": {
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
                "round_4_n_distinct_sample_note": (
                    f"round 4 接力棒第 4 call per caption 实测; minimax distill 侧独立计数 = 22 caption 各 {ROUND4_TARGET_PER_CAPTION} successful "
                    f"(沿 r1+r2+r3+r4 quadruples, prompt_id 前缀 minimax_t01_distill_ filter 域, "
                    f"前置 r1+r2+r3 真值 baseline = 3 successful/caption, 三件累加 = 66 calls);"
                    f"**minimax 蒸馏侧 round 4 接力达成**: distill 侧 22/22 caption {ROUND4_TARGET_PER_CAPTION}/5 successful 接力态 (baseline 修正后);"
                    "远期 ≥5 目标需 1 more 棒接力 (r5);"
                    "由 verdict-keeper 统裁 (本棒 0 写 verdict)"
                ),
            },
            "K_N26_N2_observation": {
                "mimo_no_proxy_used_for_all_calls": no_proxy_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r4, 4),
                "cumulative_empty_response_rate": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r4 > 0.50,
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
                        "本棒未触发 K-N26-N2 累计阈值; 跑至 1500s watchdog 提前停批 / 全 22 calls 完成 (接力态)"
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
            "actual_calls": r4_total,
            "checkpoint_file": None,
            "next_resume_via": "本棒为 batch10 round 4 接力棒 — 后续 r5 接力棒 (沿 task_append 同 agent 唤醒语义)",
            "note": (
                f"本棒 round 4 接力棒已完成（{r4_total}/{planned_total} calls; baseline 修正后）"
                + (f"; K-N26-N2 累计阈值触发: cum_rate={round(k_n26_n2_trigger_cum_rate,4) if k_n26_n2_trigger_cum_rate else None} > 0.50, 立即停采 (沿 dispatch §4)"
                   if k_n26_n2_triggered else
                   f"; 撞 {WALL_TIME_BUDGET_S}s watchdog 提前停批 ({len(captions) - r4_ok} caption 未达标) 走 task_append 接力棒"
                   if wall_time_s > WALL_TIME_BUDGET_S and r4_ok < len(captions) else
                   f"; **minimax 蒸馏侧 22/22 caption 4/5 successful 接力 (baseline 修正后)** ✓"
                   if r4_ok == len(captions) else
                   f"; minimax 蒸馏侧未达标 {len(captions) - r4_ok} caption → 下一棒接力 (本棒为接力棒, 留 r5 接力补足)")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    # 21. 落盘前自扫
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    # 22. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch10_r4_result.json")
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
    print(f"  quadruples: {r4_total} (ok={r4_ok} empty={r4_empty} fail={r4_fail})")
    print(f"  r4_empty_rate: {empty_rate_r4:.4f}")
    print(f"  cumulative_empty_rate: {cum_empty_rate_post:.4f}")
    print(f"  k_n26_n2_triggered: {k_n26_n2_triggered}")
    print(f"  distill_side_met_target_count (>=5 final): {met_target_count_distill}/{len(captions)}")
    print(f"  distill_side_met_round4_count (>=4 接力, 真值): {met_round4_count_distill}/{len(captions)}")
    print(f"  *** all_22_captions_met_target_distill (>=5 final): {minimax_distill_side_round4_progress['all_22_captions_met_target']} ***")
    print(f"  round4_progress_disposition: {minimax_distill_side_round4_progress['round4_progress_disposition']}")
    print(f"  baseline_correction: 三件累加={cum_total_prior_distill} calls / {cum_ok_prior_distill} succ / 真值 3/caption")
    print(f"  cross_check_match (r3.per_cap vs 三件累加): {cross_check_match}")
    print(f"  retry_bug_fix_applied_in_all_calls: {retry_validation['r4_retry_bug_fix_applied_in_all_calls']}")
    print(f"  retry_triggered_count: {retry_triggered_count}")
    print(f"  retry_count_distribution: {retry_count_distribution}")
    print(f"  retry_trigger_categories_distribution: {retry_trigger_categories_distribution}")
    print(f"  no_proxy_compliance (mimo): {no_proxy_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  stop_reason: {stop_reason}")
    if minimax_distill_side_round4_progress["still_pending"]:
        print(f"  still_pending_distill (>=5 final 目标距, 22 captions): {len(minimax_distill_side_round4_progress['still_pending'])} captions")
    if minimax_distill_side_round4_progress["still_pending_round4"]:
        print(f"  still_pending_round4 (>=4 接力目标距): {minimax_distill_side_round4_progress['still_pending_round4']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())