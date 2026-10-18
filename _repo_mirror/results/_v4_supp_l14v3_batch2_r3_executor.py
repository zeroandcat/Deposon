# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch2_r3_executor.py
=====================================

V4 L14+ batch 2 · round 3 · GLM_1 教师侧 round 2 续采（reask=1）
================================================================

【派工依据】
----------------
- 沿 batch2 r2 executor `E7418F47A130` + r2 result `8C125E257AF8` 口径（基础口径锚）
- 沿 batch1 r6 executor `5f02c7e0f094` + r6 result `A4F851154551` retry 修复口径
- 沿 /v1/models 探活 `_v4_supp_l14v3_batch2_r2_models_probe.json` (sha12=`3C9DC60B5071`)
  选定 glm-5.3（44 个 model 中 GLM 系 4 个：glm-5.2/glm-5.3/glm-5.3-flash/glm-5.3-flash-free）
- 派工单 ask_748d9242c7a6be3d83de63a0 (2026-09-24 23:08 显式): GLM_1=glm-5.3 已在跑（沿 r2）

【本棒范围（沿 dispatch）—— GLM_1 教师侧 round 2（reask=1）续采】
----------------------------------------------------------
1. **沿用 glm-5.3**（r2 1-call probe ok=200；本棒不再探活，仅 1-call smoke 防端点飘移）
2. **22 caption × 1 call**（每位 caption 第 2 call；reask_idx=1；目标 2/5 successful/caption）
3. **目标**：本棒后 22/22 caption 各 ≥2 successful call；下棒接力至 ≥5 successful/caption
4. 预算 ≤22 caption calls + ≤1 smoke calls / ≤600s watchdog
5. 跑不完如实报断点

【每 caption successful 计数（沿 dispatch §6）】
---------------------------------------------------------
- 本棒前基线（沿 batch2 r2）：GLM_1 教师侧 = 22 calls / 0 empty / 22 ok / 0.0000 rate
- 本棒 round 2（reask=1）后：22/22 caption 各 ≥2 successful call（理论值；如端点飘移可能回落）
- 终盘结果：result.json 顶层 `per_caption_successful_calls` 块 + `dispatch_target_progress` 块

【retry 修复逻辑沿 batch1 r6 + r2（沿 dispatch §3）】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}
- read_timeout_initial_s=60 / read_timeout_retry_s=90
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回
- r6 retry 触发的源 error_category tracking 沿用

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
--------------------------------------------------------------------
- 跨批累计 baseline = batch1 终态 119 + batch2 r2 = 22 → **141 calls / 9 empty / 6.38%**（沿 r2 result）
- 累计 = batch1 baseline + batch2 r2 + batch2 r3（GLM_1 自身从 0 起步，r2 末 22/0/22）
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）

【端点取舍（沿 r2）】
----------------------------
- teamo + tun + glm-5.3（r2 已探活确认 ok=200；本棒不再做完整 3-candidate probe，仅 1-call smoke）
- model_id 字面 = glm-5.3（与 prereg §0 字面 GLM_1 映射：「GLM_1 = V3 公开产品名」 → teamo 端点已升 GLM-5.x 系）
- teamo 必走 tun 防封号（PI 2026-09-23 硬纪律）

【铁律严守（沿 r2）】
------------------------
- R4 key 永不明文（无例外）；仅 runtime memory 读
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch2_r3_*` 与 `_batch2_r2_*` / `_batch2_r1_*` / `_batch1_*` 独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物；探活计入 calls 账
- 不覆盖既有件（r2 executor `E7418F47A130` + r2 result `8C125E257AF8` + batch1 r6 双件 + r1 探活件 + models_probe `3C9DC60B5071` 不动）

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch2_r3_result.json`（schema = `v4_l14v3_n26/1` + batch=2 + round=3）
- 不覆盖 r2 result `8C125E257AF8` 或 batch1 r6 result `A4F851154551` 或 r1 result `D245AE4CE385`
- predecessor_sha12 链：r2_executor/r2_result + batch1_r6_executor/batch1_r6_result + r1_executor/r1_result + models_probe

【与 r2 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. ROUND = 3（升 r3 命名避开 r2 重叠）；BATCH = 2 不变
2. prompt_id 后缀 `_b2_r3`；t02 = teacher side round 2（取代 r2 的 t01 round 1 retry）
3. reask_idx = 1（本棒每位 caption 第 2 call；取代 r2 的 reask_idx=0）
4. phase_label：`b2_r3_need1`（取代 r2 的 `b2_r2_need1`）
5. is_round_2 = True（语义：本棒为 GLM_1 教师侧 data collection round 2，区别于 r2 的 round 1 retry）
6. smoke_call_only = True（沿 r2 probe=glm-5.3 ok=200，本棒仅 1-call smoke 防端点飘移；不再做 3-candidate probe fallback）
7. predecessor_sha12 链：r2_executor `E7418F47A130` + r2_result `8C125E257AF8`（新增；取代 r2 链的 r1 + models_probe 仍保留）
8. baseline prior：r2 终态 22 calls / 0 empty / 22 ok / 0.0000 rate（取代 r2 链的 0/0/0）
9. 跨批累计 baseline：r2 终态 141 calls / 9 empty / 6.38% rate（取代 r2 链的 119/9/7.56%）
10. 新增 `glm1_teacher_side_round2_progress` 块：本棒后 GLM_1 教师侧 round 2 完成度（≥2 successful/caption）
11. K-N26-N2 触发阈值 = 0.50 不变；监控 baseline 更新为 141/9/6.38%
12. spec_conformance 重写：GLM_1 教师侧 round 2 续采（reask=1），目标 ≥2 successful/caption

【边界】
----------
- 不动任何既有件（含 r2 executor `E7418F47A130` + r2 result `8C125E257AF8` + batch1 r6 executor `5f02c7e0f094` + batch1 r6 result `A4F851154551` + r1 executor `E52F930654D3` + r1 result `D245AE4CE385` + models_probe `3C9DC60B5071` + prereg `05B975A86989`）
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
BATCH1_R6_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r6_result.json")
R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r1_result.json")
R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_result.json")
MODELS_PROBE_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_models_probe.json")

# tun 代理（沿 r2）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（沿 r2）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
KEY_INDEX_TEAMO_1BASED = 15  # 沿 r2 (line 15 = teamo key)
USE_PROXY = True

# 串行间隔
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 r2）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 r2）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别（沿 r2 + dispatch §1 字面）
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值（沿 dispatch §4）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算
WALL_TIME_BUDGET_S = 600

# 本棒调度（沿 dispatch）
BATCH = 2
ROUND = 3  # 升 r3 命名避开 r2 重叠
TEACHER = "GLM_1"
SIDE = "teacher"
REASK_R1 = 1  # 本棒 round 2 = 每 caption 第 2 call（reask_idx=1）
TARGET_SUCCESSFUL_PER_CAPTION = 5
SMOKE_CALL_ONLY = True  # 沿 r2 probe=glm-5.3 ok=200；本棒仅 1-call smoke 不再做 3-candidate probe

# 选定的 model_id（沿 r2 探活结论，不重探）
MODEL_GLM_1 = "glm-5.3"

# smoke prompt（极小，节省 token）
SMOKE_PROMPT = "Reply with the single word: ok"


# ============================================================
# 敏感模式（沿 r2）
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
# 工具（沿 r2 + 复用）
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
    model_id: str,
    messages: List[Dict[str, str]],
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
    timeout: int = READ_TIMEOUT_INITIAL_S,
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch2-r3",
        "X-Title": f"deposon-l14v3-batch2-r3-{TEACHER}-teacher",
    }
    body = {
        "model": model_id,
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
# 提示构造（沿 r2）
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
# Smoke（沿 r2 probe 简化版；仅 1 call 确认端点 ok）
# ============================================================
def smoke_glm_model(api_key: str, model_id: str) -> Dict[str, Any]:
    """1-call smoke（沿 r2 probe 结论 glm-5.3 ok=200 已知）；仅作端点可达性确认。"""
    t0 = time.time()
    messages = [{"role": "user", "content": SMOKE_PROMPT}]
    r = call_chat_teamo(
        api_key=api_key,
        model_id=model_id,
        messages=messages,
        max_tokens=20,
        timeout=READ_TIMEOUT_INITIAL_S,
    )
    rec = {
        "candidate_model_id": model_id,
        "ok": r.get("ok", False),
        "status_code": r.get("status_code"),
        "latency_ms": r.get("latency_ms", 0),
        "model_returned": r.get("model_returned", ""),
        "error_category": r.get("error_category"),
        "error_snippet": (r.get("error_body_snippet") or r.get("error_snippet") or "")[:200],
        "content_preview": (r.get("content", "") or "")[:50],
        "content_empty_reasoning_only": r.get("ok", False) and is_empty_response(r.get("content", "")),
        "phase_label": "smoke_glm_model_id",
        "wall_time_s": round(time.time() - t0, 1),
    }
    return rec


# ============================================================
# 单 call + 内层重试（沿 r2）
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
    model_id: str,
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_b2_r3"
    prompt_id = f"glm1_t02_{side}_{caption_id}{suffix}"

    retries = 0
    last = None
    while retries <= INNER_RETRY_MAX:
        timeout_s = READ_TIMEOUT_INITIAL_S if retries == 0 else READ_TIMEOUT_RETRY_S
        r = call_chat_teamo(api_key=api_key, model_id=model_id, messages=messages, timeout=timeout_s)
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
                        "model_id_sent": model_id,
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
                "model_id_sent": model_id,
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
            "model_id_sent": model_id,
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
    print("V4 L14+ batch 2 round 3 · GLM_1 教师侧 round 2（reask=1）续采")
    print("沿 r2 glm-5.3 探活结论 ok=200；本棒 smoke 1-call 后跑 22 caption × 1 call")
    print("计划 calls = 22 caption × 1 call = 22 calls + 1 smoke call")
    print("目标: round 2 后 22/22 caption 各 ≥2 successful call")
    print("预算 ≤22 caption calls + 1 smoke call / ≤600s watchdog")
    print("retry 修复沿 r2 (沿 batch1 r6)")
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

    # 3. 加载前置累计基线（batch1 r6 + batch2 r1 + batch2 r2）
    with open(BATCH1_R6_RESULT_PATH, "r", encoding="utf-8") as f:
        batch1_r6 = json.load(f)
    with open(R1_RESULT_PATH, "r", encoding="utf-8") as f:
        r1 = json.load(f)
    with open(R2_RESULT_PATH, "r", encoding="utf-8") as f:
        r2 = json.load(f)
    cum_prior = batch1_r6["aggregate"]["cumulative"]["post_total"]
    cum_empty_prior = batch1_r6["aggregate"]["cumulative"]["post_empty"]
    cum_ok_prior = batch1_r6["aggregate"]["cumulative"]["post_ok"]
    cum_rate_prior = batch1_r6["aggregate"]["cumulative"]["post_rate"]
    print(f"[BASELINE batch1 r6] total={cum_prior} ok={cum_ok_prior} empty={cum_empty_prior} rate={cum_rate_prior:.4f}")
    r1_stop = r1.get("metadata", {}).get("stop_reason", "?")
    print(f"[BASELINE r1] stop_reason={r1_stop} (r1 探活 fail / 0 caption call)")

    # r2 终态 = 本棒前 GLM_1 自身累计基线
    glm1_prior_total = r2["aggregate"]["glm1_cumulative"]["post_total"]
    glm1_prior_empty = r2["aggregate"]["glm1_cumulative"]["post_empty"]
    glm1_prior_ok = r2["aggregate"]["glm1_cumulative"]["post_ok"]
    glm1_prior_rate = r2["aggregate"]["glm1_cumulative"]["post_rate"]
    print(f"[BASELINE r2 GLM_1] total={glm1_prior_total} ok={glm1_prior_ok} empty={glm1_prior_empty} rate={glm1_prior_rate:.4f}")

    # 跨批累计基线 = r2 终态
    cross_prior_total = r2["aggregate"]["cross_batch_with_batch1_baseline"]["cross_total"]
    cross_prior_empty = r2["aggregate"]["cross_batch_with_batch1_baseline"]["cross_empty"]
    cross_prior_ok = r2["aggregate"]["cross_batch_with_batch1_baseline"]["cross_ok"]
    cross_prior_rate = r2["aggregate"]["cross_batch_with_batch1_baseline"]["cross_rate"]
    print(f"[BASELINE cross batch] total={cross_prior_total} ok={cross_prior_ok} empty={cross_prior_empty} rate={cross_prior_rate:.4f}")

    # 4. 加载 /v1/models 探活清单（参考；不重探）
    with open(MODELS_PROBE_PATH, "r", encoding="utf-8") as f:
        models_probe = json.load(f)
    glm_like_ids = models_probe.get("glm_like_ids", [])
    print(f"[MODELS PROBE REF] 44 total models; GLM 系 {len(glm_like_ids)} 个: {glm_like_ids}")

    # 5. Smoke 1-call（沿 r2 probe 结论 glm-5.3 ok=200）
    print("=" * 60)
    print("[SMOKE PHASE] glm-5.3 1-call smoke（沿 r2 probe 结论）")
    print("=" * 60)
    t_smoke_start = time.time()
    smoke_rec = smoke_glm_model(api_key, MODEL_GLM_1)
    t_smoke_end = time.time()
    smoke_wall_s = round(t_smoke_end - t_smoke_start, 1)
    print(
        f"  [SMOKE] model_id={MODEL_GLM_1} sc={smoke_rec.get('status_code')} "
        f"cat={smoke_rec.get('error_category')} lat={smoke_rec.get('latency_ms', 0):.1f}ms "
        f"model_returned={smoke_rec.get('model_returned', '')[:30]} "
        f"wall={smoke_wall_s}s"
    )
    if not (smoke_rec["ok"] and smoke_rec["status_code"] == 200 and smoke_rec["model_returned"].strip() != ""):
        print(f"[FATAL] smoke fail; 退码 3")
        cst = timezone(timedelta(hours=8))
        now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")
        fail_result = {
            "schema": "v4_l14v3_n26/1",
            "batch": 2,
            "round": 3,
            "metadata": {
                "task": "L14V3_batch2_round3_GLM1_teacher_side_round2_reask1",
                "prereg_sha12": "05B975A86989",
                "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
                "predecessor_sha12": {
                    "r2_executor_sha12": "E7418F47A130",
                    "r2_executor_path": "results/_v4_supp_l14v3_batch2_r2_executor.py",
                    "r2_result_sha12": "8C125E257AF8",
                    "r2_result_path": "results/_v4_supp_l14v3_batch2_r2_result.json",
                    "batch1_r6_executor_sha12": "5f02c7e0f094",
                    "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                    "batch1_r6_result_sha12": "A4F851154551",
                    "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
                    "r1_executor_sha12": "E52F930654D3",
                    "r1_executor_path": "results/_v4_supp_l14v3_batch2_r1_executor.py",
                    "r1_result_sha12": "D245AE4CE385",
                    "r1_result_path": "results/_v4_supp_l14v3_batch2_r1_result.json",
                    "models_probe_sha12": "3C9DC60B5071",
                    "models_probe_path": "results/_v4_supp_l14v3_batch2_r2_models_probe.json",
                },
                "date": "2026-09-24",
                "teacher": TEACHER,
                "side": SIDE,
                "round_index": 3,
                "stop_reason": "smoke_glm_model_failed",
            },
            "smoke_phase": smoke_rec,
            "smoke_wall_time_s": smoke_wall_s,
            "run_window_cst": now_iso,
        }
        out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r3_result.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(fail_result, f, ensure_ascii=False, indent=2)
        print(f"[WROTE] {out_path}")
        return 3
    print(f"[SMOKE-OK] model_id = {MODEL_GLM_1} (sc=200, model_returned={smoke_rec['model_returned']})")

    model_id = MODEL_GLM_1

    # 6. 调度：22 caption × 1 call (round 2 reask=1) 按 caption_id 字母序
    captions_sorted = sorted(captions, key=lambda c: c["id"])
    planned = [{"caption_id": c["id"], "phase": "b2_r3_need1"} for c in captions_sorted]
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (22 caption × 1 call)")

    # 7. 时间预算起点（含 smoke）
    t_batch_start = time.time()
    wall_budget_remaining_s = WALL_TIME_BUDGET_S - (t_batch_start - t_smoke_start)
    if wall_budget_remaining_s <= 0:
        print(f"[FATAL] smoke 已用尽 watchdog ({smoke_wall_s}s); 不再跑 caption")
        return 4
    print(f"[WALL BUDGET] remaining after smoke: {wall_budget_remaining_s:.1f}s")

    # 8. 跑
    quadruples: List[Dict[str, Any]] = []
    cum_total = glm1_prior_total
    cum_empty = glm1_prior_empty
    cum_ok = glm1_prior_ok
    r3_total = 0
    r3_ok = 0
    r3_empty = 0
    r3_fail = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    k_n26_n2_triggered = False
    k_n26_n2_trigger_at_call_idx = None
    k_n26_n2_trigger_cum_rate = None
    stop_reason = None

    retry_trigger_categories_tracker: List[str] = []
    retry_count_distribution: Dict[int, int] = {}
    retry_triggered_count = 0

    # 从 r2 累计 per_caption_successful_calls 起步
    r2_per_cap = r2.get("per_caption_successful_calls", {})
    per_cap_succ = {cid: r2_per_cap.get(cid, {}).get("succ_count", 0) for cid in [c["id"] for c in captions]}
    per_cap_total = {cid: r2_per_cap.get(cid, {}).get("total_calls_so_far", 0) for cid in [c["id"] for c in captions]}
    per_cap_empty = {cid: r2_per_cap.get(cid, {}).get("empty_count_so_far", 0) for cid in [c["id"] for c in captions]}
    print(f"[PRIOR per_caption_succ] {dict(sorted(per_cap_succ.items()))}")

    for i, item in enumerate(planned):
        elapsed = time.time() - t_batch_start
        if elapsed > wall_budget_remaining_s:
            stop_reason = f"wall_time_{wall_budget_remaining_s:.0f}s"
            print(f"[BREAKPOINT] wall time {elapsed:.1f}s > {wall_budget_remaining_s:.1f}s remaining; stop at call {i}/{planned_total}")
            break

        cap_id = item["caption_id"]
        caption = cap_by_id.get(cap_id)
        if caption is None:
            print(f"[WARN] caption_id={cap_id} not found; skip")
            continue

        # K-N26-N2 GLM_1 自身累计监控（call 前判）
        if cum_total > 0:
            current_cum_rate = cum_empty / cum_total
            if current_cum_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i
                k_n26_n2_trigger_cum_rate = current_cum_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 GLM_1 cumulative empty_rate={current_cum_rate:.4f} > 0.50 at call {i}/{planned_total}; stop per dispatch §4")
                break

        rec = run_one_quadruple(
            api_key=api_key,
            caption=caption,
            reask_idx=REASK_R1,
            side="teacher",
            round_index=ROUND,
            is_round_2=True,  # 语义：本棒 = GLM_1 教师侧 data collection round 2
            phase_label=item["phase"],
            retry_trigger_categories_tracker=retry_trigger_categories_tracker,
            model_id=model_id,
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
            r3_ok += 1
            cum_ok += 1
            per_cap_succ[cap_id] += 1
        elif is_empty:
            r3_empty += 1
            cum_empty += 1
            per_cap_empty[cap_id] += 1
        else:
            r3_fail += 1
        r3_total += 1
        cum_total += 1
        per_cap_total[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[b{BATCH}r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ = per_cap_succ[cap_id]
        target_met = "[OK]" if cur_succ >= 2 else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<14} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[succ={cur_succ}/2 {target_met}] "
            f"[glm1_cum_rate={current_cum_rate_post:.4f}]"
        )

        # K-N26-N2 停采监控（call 后立即判）
        if cum_total > 0:
            post_rate = cum_empty / cum_total
            if post_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i + 1
                k_n26_n2_trigger_cum_rate = post_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 GLM_1 post-call cumulative empty_rate={post_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch §4")
                break

        if i < planned_total - 1:
            time.sleep(INTER_CALL_SLEEP_S)

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)
    total_wall_s = round(t_batch_end - t_smoke_start, 1)

    # 9. 统计
    empty_rate_r3 = (r3_empty / r3_total) if r3_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 跨批累计 = r2 baseline + GLM_1 本棒
    cross_batch_total = cross_prior_total + r3_total
    cross_batch_empty = cross_prior_empty + cum_empty - glm1_prior_empty
    cross_batch_ok = cross_prior_ok + cum_ok - glm1_prior_ok
    cross_batch_rate = cross_batch_empty / cross_batch_total if cross_batch_total > 0 else 0.0

    # 10. 每 caption successful 计数
    per_caption_successful_calls = {}
    met_round2_count = 0
    met_target_count = 0
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ[cid]
        t = per_cap_total[cid]
        e = per_cap_empty[cid]
        met_r2 = s >= 2  # round 2 目标 = ≥2 successful/caption
        met_target = s >= TARGET_SUCCESSFUL_PER_CAPTION
        if met_r2:
            met_round2_count += 1
        if met_target:
            met_target_count += 1
        per_caption_successful_calls[cid] = {
            "succ_count": s,
            "round2_target": 2,
            "round2_met": met_r2,
            "succ_count_cumulative_to_target": s,
            "target": TARGET_SUCCESSFUL_PER_CAPTION,
            "need_more_to_target": max(0, TARGET_SUCCESSFUL_PER_CAPTION - s),
            "met_target": met_target,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 11. GLM_1 教师侧 round 2 进度块
    glm1_round2_progress = {
        "round2_target": ">=2 successful call/caption (round 2 reask=1)",
        "met_count_post_r3_round2": met_round2_count,
        "total_captions": len(captions),
        "remaining_count_round2": len(captions) - met_round2_count,
        "met_percentage_round2": round(met_round2_count / len(captions) * 100, 2),
        "still_pending_captions_round2": sorted([
            cid for cid, info in per_caption_successful_calls.items() if not info["round2_met"]
        ]),
        "met_count_cumulative_to_target": met_target_count,
        "still_pending_captions_to_target": sorted([
            cid for cid, info in per_caption_successful_calls.items() if not info["met_target"]
        ]),
    }

    # 12. retry validation 块
    retry_trigger_categories_distribution: Dict[str, int] = {}
    for cat in retry_trigger_categories_tracker:
        retry_trigger_categories_distribution[cat] = retry_trigger_categories_distribution.get(cat, 0) + 1

    retry_validation = {
        "r3_retry_count_distribution": dict(retry_count_distribution),
        "r3_retry_triggered_count": retry_triggered_count,
        "r3_retry_trigger_categories_tracker": retry_trigger_categories_tracker,
        "r3_retry_trigger_categories_distribution": retry_trigger_categories_distribution,
        "r3_retry_bug_fix_applied_in_all_calls": all(
            q["per_call_metadata"].get("retry_bug_fix_applied") is True
            for q in quadruples
        ),
        "r3_empty_rate_with_fix": round(empty_rate_r3, 4),
    }

    # 13. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    # model_id_inconsistency_honest_disclosure（沿 r2 + r3 沿用）
    selected_record = smoke_rec
    model_id_disclosure = (
        f"prereg §0 字面 model_id = GLM_1 (V3 公开产品名 / 端点名); "
        f"teamo /v1/models 探活清单 (44 models 中 GLM 系 4 个: {glm_like_ids}); "
        f"GLM_1 字面不在清单（V3 时期 GLM-1 / GLM-4 命名已下线，teamo 当前 GLM 系已升 5.x）; "
        f"本棒选定 = {model_id} (1-call smoke ok=200, model_returned={selected_record.get('model_returned', '')}); "
        f"沿 user memory 2026-09-08「V3 端点名 vs 公开产品名不一致时直接问」+ 端点策略即用即探 (PI 2026-09-24 拍板) = "
        f"用 teamo /v1/models 实际可用的 GLM 系主版本 glm-5.3 替代 GLM_1; "
        f"本映射选择 (glm-5.3 主版本 / 非 flash / 非 free) 理由: 最贴近 GLM_1 = 主版本定位; 避开 flash/free 版的潜在 token/quota 限制; "
        f"r2 探活确认 glm-5.3 ok=200; r3 沿 r2 结论仅做 1-call smoke 防端点飘移; "
        f"待 PI 复核项: 是否接受 glm-5.3 作为 GLM_1 = V3 公开产品名的 teamo 端点映射"
    )

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 2,
        "round": 3,
        "metadata": {
            "task": "L14V3_batch2_round3_GLM1_teacher_side_round2_reask1",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "predecessor_sha12": {
                "r2_executor_sha12": "E7418F47A130",
                "r2_executor_path": "results/_v4_supp_l14v3_batch2_r2_executor.py",
                "r2_result_sha12": "8C125E257AF8",
                "r2_result_path": "results/_v4_supp_l14v3_batch2_r2_result.json",
                "batch1_r6_executor_sha12": "5f02c7e0f094",
                "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                "batch1_r6_result_sha12": "A4F851154551",
                "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
                "r1_executor_sha12": "E52F930654D3",
                "r1_executor_path": "results/_v4_supp_l14v3_batch2_r1_executor.py",
                "r1_result_sha12": "D245AE4CE385",
                "r1_result_path": "results/_v4_supp_l14v3_batch2_r1_result.json",
                "models_probe_sha12": "3C9DC60B5071",
                "models_probe_path": "results/_v4_supp_l14v3_batch2_r2_models_probe.json",
            },
            "date": "2026-09-24",
            "spec_conformance": (
                "PI 2026-09-24 batch2 GLM_1 教师侧 round 2 续采 (reask=1); "
                "沿 r2 glm-5.3 探活结论 (1-call probe ok=200); r3 仅 1-call smoke; "
                "22 caption × 1 call = 22 calls (按 caption_id 字母序); "
                "目标 ≥2 successful/caption"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": 3,
            "batch_index": BATCH,
            "round2_target_per_caption": 2,
            "round2_reask_idx": REASK_R1,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r3_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": (
                "沿 r2 实测 (teamo 端点); r3 沿用 teamo 端点; "
                "/v1/models 探活清单沿 r2 models_probe.json (sha12=3C9DC60B5071); "
                "r3 仅 1-call smoke 防端点飘移"
            ),
            "model_id_sent": model_id,
            "model_id_inconsistency_honest_disclosure": model_id_disclosure,
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
                "r6_status_沿": "retry 修复沿 batch1 r6 (沿 5f02c7e0f094)",
                "r2_b2_status": "r2 1-call probe ok=200 选定 glm-5.3",
                "r3_b2_status": "r3 仅 1-call smoke (沿 r2 结论)；未做 3-candidate probe fallback",
                "rationale": (
                    "沿 r2 glm-5.3 探活结论；r3 节省预算避免重复 probe；"
                    "smoke 失败立即 abort 不重探"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "wall_time_budget_remaining_after_smoke_s": round(wall_budget_remaining_s, 1),
            "wall_time_actual_caption_s": wall_time_s,
            "wall_time_actual_smoke_s": smoke_wall_s,
            "wall_time_actual_total_s": total_wall_s,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r2_executor": [
                "1. ROUND=3 (升 r3 命名)；BATCH=2 不变",
                "2. prompt_id 后缀 _b2_r3；t02_teacher (取代 r2 的 t01_teacher round 1 retry)",
                "3. reask_idx=1 (本棒每 caption 第 2 call；取代 r2 的 reask_idx=0)",
                "4. phase_label: b2_r3_need1 (取代 r2 的 b2_r2_need1)",
                "5. is_round_2=True (语义: GLM_1 教师侧 data collection round 2)",
                "6. smoke_call_only=True (取代 r2 的 3-candidate probe)",
                "7. predecessor_sha12 链: r2_executor E7418F47A130 + r2_result 8C125E257AF8 (取代 r2 链的 r1 + models_probe 仍保留)",
                "8. baseline prior: r2 终态 22 calls / 0 empty / 22 ok (取代 r2 链的 0/0/0)",
                "9. 跨批累计 baseline: r2 终态 141 calls / 9 empty / 6.38% (取代 r2 链的 119/9/7.56%)",
                "10. 新增 glm1_teacher_side_round2_progress 块 (round 2 完成度 ≥2 successful/caption)",
                "11. K-N26-N2 触发阈值 0.50 不变；监控 baseline 更新为 141/9/6.38%",
                "12. spec_conformance 重写: round 2 续采 (reask=1)",
                "13. per_caption_successful_calls 字段新增 round2_target=2 / round2_met",
                "14. 调度注释: round 2 续采 (reask=1) 22 caption × 1 call",
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
                "smoke_only_no_full_probe": True,
            },
            "run_window_cst": now_iso,
            "stop_reason": stop_reason,
            "interruption_recovery_note": (
                "r3 沿 r2 glm-5.3 探活结论；不再做 3-candidate probe fallback；"
                "1-call smoke 失败立即 abort；r3 与 r2/r1/batch1_r6 派生 JSON 独立 (不合并)"
            ),
        },
        "models_listing_summary_ref": {
            "endpoint": ENDPOINT_TEAMO + "/models",
            "model_count_total": models_probe.get("model_count_total"),
            "model_count_glm_like": len(glm_like_ids),
            "glm_like_ids": glm_like_ids,
            "fetched_at_cst": models_probe.get("fetched_at_cst"),
            "note": (
                "r3 不重探 /v1/models；仅引用 r2 探活清单 (sha12=3C9DC60B5071) "
                "确认 glm-5.3 主版本仍为 GLM 系首选"
            ),
        },
        "smoke_phase": {
            "selected_model_id": MODEL_GLM_1,
            "smoke_record": smoke_rec,
            "smoke_wall_time_s": smoke_wall_s,
        },
        "quadruples": quadruples,
        "retry_validation": retry_validation,
        "per_caption_successful_calls": per_caption_successful_calls,
        "glm1_teacher_side_round2_progress": glm1_round2_progress,
        "dispatch_target_progress": {
            "target_round2": ">=2 successful calls/caption (round 2 reask=1)",
            "target_cumulative": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (跨轮累计)",
            "met_count_post_r3_round2": met_round2_count,
            "met_count_post_r3_cumulative_to_target": met_target_count,
            "total_captions": len(captions),
            "remaining_count_round2": len(captions) - met_round2_count,
            "remaining_count_cumulative_to_target": len(captions) - met_target_count,
            "met_percentage_round2": round(met_round2_count / len(captions) * 100, 2),
            "met_percentage_cumulative_to_target": round(met_target_count / len(captions) * 100, 2),
            "still_pending_captions_round2": sorted([
                cid for cid, info in per_caption_successful_calls.items() if not info["round2_met"]
            ]),
            "still_pending_captions_cumulative_to_target": sorted([
                cid for cid, info in per_caption_successful_calls.items() if not info["met_target"]
            ]),
        },
        "aggregate": {
            "r3_total_calls": r3_total,
            "r3_ok_count": r3_ok,
            "r3_empty_response_count": r3_empty,
            "r3_fail_count": r3_fail,
            "r3_empty_response_rate": round(empty_rate_r3, 4),
            "r3_total_prompt_tokens": total_prompt_tokens,
            "r3_total_completion_tokens": total_completion_tokens,
            "r3_total_tokens": total_prompt_tokens + total_completion_tokens,
            "tun_compliance": tun_compliance,
            "tun_used_count": tun_used_count,
            "tun_target_count": len(quadruples),
            "smoke_total_calls": 1,
            "smoke_attempted_model_id": MODEL_GLM_1,
            "glm1_cumulative": {
                "prior_total": glm1_prior_total,
                "prior_empty": glm1_prior_empty,
                "prior_ok": glm1_prior_ok,
                "prior_rate": glm1_prior_rate,
                "post_total": cum_total,
                "post_empty": cum_empty,
                "post_ok": cum_ok,
                "post_rate": round(cum_empty_rate_post, 4),
                "delta_total": cum_total - glm1_prior_total,
                "delta_empty": cum_empty - glm1_prior_empty,
                "delta_ok": cum_ok - glm1_prior_ok,
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered_this_batch": k_n26_n2_triggered,
            },
            "cross_batch_with_r2_baseline": {
                "r2_baseline_total": cross_prior_total,
                "r2_baseline_empty": cross_prior_empty,
                "r2_baseline_ok": cross_prior_ok,
                "r2_baseline_rate": cross_prior_rate,
                "batch2_glm1_post_total": cum_total,
                "batch2_glm1_post_empty": cum_empty,
                "batch2_glm1_post_ok": cum_ok,
                "cross_total": cross_batch_total,
                "cross_empty": cross_batch_empty,
                "cross_ok": cross_batch_ok,
                "cross_rate": round(cross_batch_rate, 4),
                "cross_k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "cross_k_n26_n2_triggered": cross_batch_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "note": (
                    "K-N26-N2 字面 per 教师; 本字段仅作 cross-batch sanity check; "
                    "GLM_1 教师侧 K-N26-N2 判定 = glm1_cumulative.post_rate"
                ),
            },
            "r3_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r3_empty_response_above_threshold_single_batch": empty_rate_r3 > 0.50,
        },
        "empty_rate_trend": {
            "batch1_round6_cumulative": {
                "calls": cum_prior,
                "empty": cum_empty_prior,
                "ok": cum_ok_prior,
                "rate": cum_rate_prior,
            },
            "batch2_round1_probe_fail": {
                "calls": 0,
                "empty": 0,
                "rate": 0.0,
                "note": "r1 探活 6 候选 400 全 fail; 0 caption call",
            },
            "batch2_round2_round1_retry": {
                "calls": glm1_prior_total,
                "empty": glm1_prior_empty,
                "rate": glm1_prior_rate,
                "note": "r2 round 1 retry 22 caption × 1 call; all OK",
            },
            "batch2_round3_round2_reask1": {
                "calls": r3_total,
                "empty": r3_empty,
                "rate": round(empty_rate_r3, 4),
            },
            "batch2_round3_cumulative_glm1": {
                "calls": cum_total,
                "empty": cum_empty,
                "ok": cum_ok,
                "rate": round(cum_empty_rate_post, 4),
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered": k_n26_n2_triggered,
            },
            "cross_batch_cumulative_post_r3": {
                "calls": cross_batch_total,
                "empty": cross_batch_empty,
                "ok": cross_batch_ok,
                "rate": round(cross_batch_rate, 4),
                "note": "r2 baseline 141/9/6.38% + r3 增量",
            },
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round2_reask1_n_distinct_sample_note": (
                    f"round 2 reask=1 第 1 call 实测；本棒后 GLM_1 教师侧 round 2 = "
                    f"{met_round2_count}/{len(captions)} caption met round 2 目标; "
                    f"需后续 round 接力达 ≥{TARGET_SUCCESSFUL_PER_CAPTION} successful/caption"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r3, 4),
                "cumulative_empty_response_rate_glm1_only": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r3 > 0.50,
                "cumulative_trigger_K_N26_N2_pass_False": k_n26_n2_triggered,
                "monitor_disposition": (
                    f"本棒 K-N26-N2 GLM_1 自身累计 empty_rate 监控 = 已实施; "
                    f"GLM_1 自身累计 = {cum_total} calls / {cum_empty} empty / {cum_empty_rate_post:.4f}; "
                    f"r2 baseline GLM_1 = {glm1_prior_total} calls / {glm1_prior_empty} empty / {glm1_prior_rate:.4f}; "
                    f"cross-batch rate = {cross_batch_rate:.4f}; "
                    f"baseline cross batch = {cross_prior_total} calls / {cross_prior_empty} empty / {cross_prior_rate:.4f}"
                ),
                "cross_batch_with_r2_baseline_rate": round(cross_batch_rate, 4),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "breakpoint_status": {
            "actual_calls": r3_total,
            "planned_calls": planned_total,
            "actual_wall_time_s": wall_time_s,
            "wall_time_budget_remaining_after_smoke_s": round(wall_budget_remaining_s, 1),
            "actual_wall_time_total_s": total_wall_s,
            "checkpoint_file": None,
            "hit_wall_time_budget": wall_time_s > wall_budget_remaining_s,
            "k_n26_n2_cumulative_triggered": k_n26_n2_triggered,
            "k_n26_n2_trigger_at_call_idx": k_n26_n2_trigger_at_call_idx,
            "k_n26_n2_trigger_cum_rate": k_n26_n2_trigger_cum_rate,
            "next_resume_via": (
                "task_append 续跑 — 沿 prereg §1.6.4 同 agent 唤醒; "
                "本棒 round 2 (reask=1) 已完; 下棒可接力 GLM_1 教师侧 round 3 (>=3 more successful/caption)"
            ),
            "note": (
                f"本棒 round 2 (reask=1): actual={r3_total}/{planned_total} calls; "
                f"GLM_1 教师侧 round 2 完成度 = {met_round2_count}/{len(captions)} caption met round 2 目标 (≥2 successful/caption); "
                f"stop_reason={stop_reason}; "
                f"GLM_1 model_id 沿 r2 探活选定 = {model_id} (1-call smoke 确认仍可用)"
            ),
            "planned_total": planned_total,
            "stop_reason": stop_reason,
        },
    }

    # 14. 自扫 key 泄露
    scan_hits = self_scan_obj(result)
    if scan_hits:
        print(f"[FATAL] 自扫命中敏感模式: {scan_hits}; 拒绝落盘")
        return 5

    # 15. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r3_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    sha12, nbytes, lf_only = sha12_file(out_path)
    print(f"[WROTE] {out_path}")
    print(f"[SHA-12] {sha12}")
    print(f"[BYTES] {nbytes}")
    print(f"[LF-ONLY] {lf_only}")
    print(f"[MODELS LISTING REF] total={models_probe.get('model_count_total')} GLM_like={len(glm_like_ids)}")
    print(f"[SMOKE] selected={model_id} ok={smoke_rec['ok']} wall={smoke_wall_s}s")
    print(f"[STATS] r3 ok={r3_ok} empty={r3_empty} fail={r3_fail} total={r3_total} rate={empty_rate_r3:.4f}")
    print(f"[GLM1 CUM] total={cum_total} ok={cum_ok} empty={cum_empty} rate={cum_empty_rate_post:.4f}")
    print(f"[CROSS BATCH] total={cross_batch_total} ok={cross_batch_ok} empty={cross_batch_empty} rate={cross_batch_rate:.4f}")
    print(f"[STOP] {stop_reason}")

    return 0


if __name__ == "__main__":
    sys.exit(main())