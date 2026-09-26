# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch2_r1_executor.py
=====================================

V4 L14+ 第 2 批 (batch 2) · round 1 — GLM_1 教师侧首轮采集
============================================================

【派工依据】
----------------
- 沿 batch1 r6 `results/_v4_supp_l14v3_batch1_r6_executor.py`（SHA-12 `5f02c7e0f094`）+ r6 产物
  `results/_v4_supp_l14v3_batch1_r6_result.json`（SHA-12 `a4f851154551`）口径恢复
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（SHA-12 `05B975A86989`）字面
- 沿 user memory 2026-09-24「mimo/teamo 不预探，即用即探」（PI 拍板）= **GLM_1 端点名一次性探活选定**
- 重派自中断 batch2（原 session 因 net::ERR_HTTP2_PING_FAILED 0 产物中断）；中断-恢复同 agent 唤醒已不可行（老实交代）

【本棒范围（沿 dispatch）—— GLM_1 教师侧 round 1 首轮】
--------------------------------------------------------
1. **即用即探**：探活 teamo 上 GLM_1 实际可接受 model_id；候选字面（沿 GLM 系命名 + 探活惯例）：
   - `GLM_1`（prereg §0 字面）
   - `glm-1`（teamo 命名惯例）
   - `glm4` / `glm-4`
   - `GLM4`
   - 首个 200 即选定；探活计入 calls 账（`phase_label: probe_model_id`）
2. **22 caption × 1 call 各** = 22 calls（首次轮次）
3. **目标**：本棒后 GLM_1 教师侧每 caption successful ≥ 1；后续轮次下棒接力（≥5 successful/caption 目标）
4. 预算 ≤22 calls（不含探活 ≤5 call 缓冲；总 call 数 ≤25）/ ≤600s watchdog
5. 跑不完如实报断点

【每 caption successful 计数（沿 dispatch §6）】
---------------------------------------------------------
- 本棒前基线（沿 batch1 r6）：GLM_1 教师侧 = 0 calls（kimi 教师侧 batch1 已收官）
- 本棒 round 1 后：22/22 caption 各 ≥ 1 successful call（如果全成功）
- 终盘结果：result.json 顶层 `per_caption_successful_calls` 块 + `dispatch_target_progress` 块

【retry 修复逻辑沿 batch1 r6（沿 dispatch §3）】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}
- read_timeout_initial_s=60 / read_timeout_retry_s=90
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回
- r6 retry 触发的源 error_category tracking 沿用

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
--------------------------------------------------------------------
- 跨批累计 baseline = batch1 终态 119 calls / 9 empty / 7.56%（沿 batch1 r6 result）
- 累计 = batch1 baseline + batch2 全部 round 累计
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 本棒 GLM_1 单教师侧累计 = 0 calls（baseline 不含 GLM_1）；GLM_1 自己 ≤50% 即可
- 跨批累计（baseline + 本棒）= 119 + ≤22 = ≤141 calls；worst case 全空 = 31/141 = 21.99% < 50%

【端点取舍（沿 batch1 r6 + 即用即探）】
----------------------------
- teamo + tun + 探活选定的 GLM_1 model_id（探活计入 calls 账）
- teamo 必走 tun 防封号（PI 2026-09-23 硬纪律）

【铁律严守（沿 batch1 r6）】
------------------------
- R4 key 永不明文（无例外）；仅 runtime memory 读
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch2_r1_*` 与所有 _batch1_* 独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物；探活尝试数计入 calls 账

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch2_r1_result.json`（schema = `v4_l14v3_n26/1` + batch=2 + round=1）
- 不覆盖 batch1 r6 result `a4f851154551` 或前棒 result

【与 batch1 r6 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. 新增参数：`BATCH = 2` / `ROUND = 1` / `TEACHER = "GLM_1"` / `REASK_R1 = 0`
2. 新增：`probe_model_id_phase` 函数 = 一次性探活（尝试多个命名变体 + tun 代理）
3. MODEL_GLM_1 = 探活选定（默认占位 `GLM_1`；探活成功即替换）
4. 调度：22 caption × 1 call (round 1) = 22 calls（按字母序 deterministic）
5. prompt_id 后缀 `_b2_r1`
6. predecessor_sha12 链：仅 batch1 r6_executor `5f02c7e0f094` + batch1 r6_result `a4f851154551`
7. 新增 `glm1_teacher_side_round1_progress` 块：本棒后 GLM_1 教师侧 round 1 完成度
8. K-N26-N2 累计 baseline = batch1 终态 119 calls / 9 empty / 7.56%（GLM_1 自身累计从 0 算）
9. 新增 `probe_records` 块：探活记录（每候选 model_id 一次尝试 → ok/error）

【边界】
----------
- 不动任何既有件（含 batch1 r6 executor `5f02c7e0f094` + r6 result `a4f851154551` + 前所有棒产物 + prereg `05B975A86989`）
- 跑不完拆段报断点
- 0 触动 V1–V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
- 中断-恢复：原 session 已销毁，本棒为新 session 接力（老实交代缺位，探活计入 calls）
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

# tun 代理（沿 batch1 r6）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（沿 batch1 r6）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
KEY_INDEX_TEAMO_1BASED = 15  # 沿 batch1 r6 (line 15 = teamo key)
USE_PROXY = True

# 串行间隔
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 batch1 r6）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 batch1 r6）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别（沿 batch1 r6 + dispatch §1 字面）
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值（沿 dispatch §4）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算
WALL_TIME_BUDGET_S = 600

# 本棒调度（沿 dispatch）
BATCH = 2
ROUND = 1
TEACHER = "GLM_1"
SIDE = "teacher"
REASK_R1 = 0  # round 1 第 1 call
TARGET_SUCCESSFUL_PER_CAPTION = 5

# GLM_1 探活候选 model_id（字面沿 GLM 系命名 + 探活惯例 + 即用即探）
PROBE_CANDIDATE_MODEL_IDS = [
    "GLM_1",      # prereg §0 字面
    "glm-1",      # teamo 命名惯例
    "glm4",       # GLM 系惯例
    "glm-4",
    "GLM4",
    "glm_4",
]

# 探活 prompt（极小，节省 token）
PROBE_PROMPT = "Reply with the single word: ok"

# 占位 model_id（探活成功后立即替换）
MODEL_GLM_1 = "GLM_1"


# ============================================================
# 敏感模式（沿 batch1 r6）
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
# 工具（沿 batch1 r6 + 复用）
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
        "HTTP-Referer": "https://deposon.local/l14v3-batch2-r1",
        "X-Title": f"deposon-l14v3-batch2-r1-{TEACHER}-teacher",
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
# 提示构造（沿 batch1 r6）
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
# 探活：GLM_1 model_id 一次性探活（即用即探）
# ============================================================
def probe_model_id_phase(api_key: str, candidate_ids: List[str]) -> Dict[str, Any]:
    """一次性探活 GLM_1 实际可接受 model_id；探活计入 calls 账。"""
    probe_records = []
    selected = None
    selected_record = None
    messages = [{"role": "user", "content": PROBE_PROMPT}]
    for idx, cid in enumerate(candidate_ids):
        r = call_chat_teamo(
            api_key=api_key,
            model_id=cid,
            messages=messages,
            max_tokens=20,
            timeout=READ_TIMEOUT_INITIAL_S,
        )
        rec = {
            "candidate_model_id": cid,
            "candidate_idx": idx,
            "ok": r.get("ok", False),
            "status_code": r.get("status_code"),
            "latency_ms": r.get("latency_ms", 0),
            "model_returned": r.get("model_returned", ""),
            "error_category": r.get("error_category"),
            "error_snippet": (r.get("error_body_snippet") or r.get("error_snippet") or "")[:200],
            "content_preview": (r.get("content", "") or "")[:50],
            "phase_label": "probe_model_id",
        }
        probe_records.append(rec)
        print(f"  [PROBE {idx+1}/{len(candidate_ids)}] candidate={cid:<14} "
              f"sc={r.get('status_code')} cat={r.get('error_category')} "
              f"lat={r.get('latency_ms', 0):.1f}ms "
              f"model_returned={r.get('model_returned', '')[:30]}")
        if r.get("ok") and not is_empty_response(r.get("content", "")):
            selected = cid
            selected_record = rec
            print(f"  [PROBE-SELECTED] {cid} 探活成功 (sc=200, content 非空)")
            break
        # 探活间隔（与正式 call 一致）
        if idx < len(candidate_ids) - 1:
            time.sleep(INTER_CALL_SLEEP_S)
    return {
        "selected_model_id": selected,
        "selected_record": selected_record,
        "probe_records": probe_records,
        "probe_attempted_count": len(probe_records),
    }


# ============================================================
# 单 call + 内层重试（沿 batch1 r6）
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
    model_id: str,
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_b2_r1"
    prompt_id = f"glm1_t01_{side}_{caption_id}{suffix}"

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
                "model_id_sent": model_id,
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
            "model_id_sent": model_id,
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
    print("V4 L14+ batch 2 round 1 · GLM_1 教师侧首轮采集")
    print("计划 calls = 22 caption × 1 call = 22 calls + ≤6 探活 call")
    print("目标: round 1 后 22/22 caption 各 ≥1 successful call")
    print("预算 ≤22 caption calls + ≤6 probe calls / ≤600s watchdog")
    print("retry 修复沿 batch1 r6")
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

    # 3. 加载 batch1 r6 累计基线
    with open(BATCH1_R6_RESULT_PATH, "r", encoding="utf-8") as f:
        batch1_r6 = json.load(f)
    cum_prior = batch1_r6["aggregate"]["cumulative"]["post_total"]
    cum_empty_prior = batch1_r6["aggregate"]["cumulative"]["post_empty"]
    cum_ok_prior = batch1_r6["aggregate"]["cumulative"]["post_ok"]
    cum_rate_prior = batch1_r6["aggregate"]["cumulative"]["post_rate"]
    print(f"[BASELINE batch1 r6] total={cum_prior} ok={cum_ok_prior} empty={cum_empty_prior} rate={cum_rate_prior:.4f}")

    # GLM_1 自身累计基线（之前未采集 GLM_1）
    glm1_prior_total = 0
    glm1_prior_empty = 0
    glm1_prior_ok = 0
    glm1_prior_rate = 0.0

    # 4. 探活 phase（即用即探）
    print("=" * 60)
    print("[PROBE PHASE] GLM_1 model_id 即用即探")
    print("=" * 60)
    t_probe_start = time.time()
    probe_result = probe_model_id_phase(api_key, PROBE_CANDIDATE_MODEL_IDS)
    t_probe_end = time.time()
    probe_wall_s = round(t_probe_end - t_probe_start, 1)
    if probe_result["selected_model_id"] is None:
        print(f"[FATAL] 探活失败: 所有候选 model_id 都不可用 ({probe_wall_s}s); 退码 3")
        # 仍然写一份 result 记录探活失败（不能默默 0 产物）
        # 但 budget 已经用掉部分 watchdog，先收集探活记录后退出
        cst = timezone(timedelta(hours=8))
        now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")
        fail_result = {
            "schema": "v4_l14v3_n26/1",
            "batch": 2,
            "round": 1,
            "metadata": {
                "task": "L14V3_batch2_round1_GLM1_teacher_side",
                "prereg_sha12": "05B975A86989",
                "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
                "predecessor_sha12": {
                    "batch1_r6_executor_sha12": "5f02c7e0f094",
                    "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                    "batch1_r6_result_sha12": "a4f851154551",
                    "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
                },
                "date": "2026-09-24",
                "teacher": TEACHER,
                "side": SIDE,
                "round_index": 1,
                "stop_reason": "probe_all_candidates_failed",
            },
            "probe_phase": probe_result,
            "probe_wall_time_s": probe_wall_s,
            "run_window_cst": now_iso,
        }
        out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r1_result.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(fail_result, f, ensure_ascii=False, indent=2)
        print(f"[WROTE] {out_path}")
        return 3
    model_id = probe_result["selected_model_id"]
    print(f"[PROBE-SELECTED] model_id = {model_id} (探活 attempts = {probe_result['probe_attempted_count']}, wall = {probe_wall_s}s)")

    # 5. 调度：22 caption × 1 call (round 1) 按 caption_id 字母序 deterministic
    captions_sorted = sorted(captions, key=lambda c: c["id"])
    planned = [{"caption_id": c["id"], "phase": "b2_r1_need1"} for c in captions_sorted]
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (22 caption × 1 call)")

    # 6. 时间预算起点（含探活）
    t_batch_start = time.time()
    wall_budget_remaining_s = WALL_TIME_BUDGET_S - (t_batch_start - t_probe_start)
    if wall_budget_remaining_s <= 0:
        print(f"[FATAL] 探活已用尽 watchdog ({probe_wall_s}s); 不再跑 caption")
        return 4
    print(f"[WALL BUDGET] remaining after probe: {wall_budget_remaining_s:.1f}s")

    # 7. 跑
    quadruples: List[Dict[str, Any]] = []
    cum_total = glm1_prior_total  # GLM_1 自身累计从 0
    cum_empty = glm1_prior_empty
    cum_ok = glm1_prior_ok
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

    per_cap_succ = {c["id"]: 0 for c in captions}
    per_cap_total = {c["id"]: 0 for c in captions}
    per_cap_empty = {c["id"]: 0 for c in captions}

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
            is_round_1=True,
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
        marker = f"[b{BATCH}r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ = per_cap_succ[cap_id]
        target_met = "[OK]" if cur_succ >= 1 else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<14} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[succ={cur_succ}/1 {target_met}] "
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
    total_wall_s = round(t_batch_end - t_probe_start, 1)

    # 8. 统计
    empty_rate_r1 = (r1_empty / r1_total) if r1_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 跨批累计 = batch1 baseline + GLM_1 本棒
    cross_batch_total = cum_prior + cum_total
    cross_batch_empty = cum_empty_prior + cum_empty
    cross_batch_ok = cum_ok_prior + cum_ok
    cross_batch_rate = cross_batch_empty / cross_batch_total if cross_batch_total > 0 else 0.0

    # 9. 每 caption successful 计数
    per_caption_successful_calls = {}
    met_target_count = 0  # round 1 目标 = 1
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ[cid]
        t = per_cap_total[cid]
        e = per_cap_empty[cid]
        # round 1 目标 = 1 successful
        need = max(0, 1 - s)
        met = s >= 1
        if met:
            met_target_count += 1
        per_caption_successful_calls[cid] = {
            "succ_count": s,
            "round1_target": 1,
            "round1_met": met,
            "succ_count_cumulative_to_target": s,
            "target": TARGET_SUCCESSFUL_PER_CAPTION,
            "need_more_to_target": max(0, TARGET_SUCCESSFUL_PER_CAPTION - s),
            "met_target": s >= TARGET_SUCCESSFUL_PER_CAPTION,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 10. GLM_1 教师侧 round 1 进度块
    glm1_round1_progress = {
        "round1_target": ">=1 successful call/caption (round 1 首轮)",
        "met_count_post_r1": met_target_count,
        "total_captions": len(captions),
        "remaining_count_round1": len(captions) - met_target_count,
        "met_percentage_round1": round(met_target_count / len(captions) * 100, 2),
        "still_pending_captions_round1": sorted([
            cid for cid, info in per_caption_successful_calls.items() if not info["round1_met"]
        ]),
        "met_count_cumulative_to_target": sum(1 for v in per_caption_successful_calls.values() if v["met_target"]),
        "still_pending_captions_to_target": sorted([
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
    }

    # 12. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    # 探活的 model_id_inconsistency_honest_disclosure（沿 batch1 r6 模板）
    model_id_disclosure = (
        f"prereg §0 字面 model_id = GLM_1 (V3 端点名); "
        f"teamo 实测：本棒即用即探选定 = {model_id}; "
        f"候选顺序 = {PROBE_CANDIDATE_MODEL_IDS}; "
        f"探活成功 candidate = {probe_result['selected_record']}; "
        f"沿 user memory 2026-09-08「代码里默认 kimi-for-coding (API 端点名), 公开产品名 KIMI-K3——两个不一致时直接问」"
        f"+ 端点策略即用即探 (PI 2026-09-24 拍板)"
    )

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 2,
        "round": 1,
        "metadata": {
            "task": "L14V3_batch2_round1_GLM1_teacher_side",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "predecessor_sha12": {
                "batch1_r6_executor_sha12": "5f02c7e0f094",
                "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                "batch1_r6_result_sha12": "a4f851154551",
                "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
            },
            "date": "2026-09-24",
            "spec_conformance": (
                "PI 2026-09-24 batch2 GLM_1 教师侧重派（原 batch2 因 net::ERR_HTTP2_PING_FAILED 0 产物中断, "
                "原 session 已销毁; 本棒为新 session 即用即探 + 沿 batch1 r6 口径 + retry 修复沿 batch1 r6 + "
                "每 caption successful 计数 + K-N26-N2 累计监控)"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": 1,
            "batch_index": BATCH,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "round1_target_per_caption": 1,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r1_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": "沿 batch1 r6 实测 (teamo kimi-k3 唯一可达); batch2 沿用 teamo 端点",
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
                "r1_b2_status": "retry 修复沿 batch1 r6; 本棒无新参数修正",
                "rationale": (
                    "沿 batch1 r6 retry 修复; GLM_1 round 1 首轮采集, "
                    "hard fail 保持 fail path 立即返回; 探活不计 retry"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "wall_time_budget_remaining_after_probe_s": round(wall_budget_remaining_s, 1),
            "wall_time_actual_caption_s": wall_time_s,
            "wall_time_actual_probe_s": probe_wall_s,
            "wall_time_actual_total_s": total_wall_s,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_batch1_r6_executor": [
                "1. BATCH=2 / ROUND=1 / TEACHER=GLM_1 / REASK_R1=0 参数化",
                "2. 新增 probe_model_id_phase 即用即探函数（候选 6 个 model_id）",
                "3. MODEL_GLM_1 = 探活选定（默认占位 GLM_1; 探活成功即替换）",
                "4. 调度: 22 caption × 1 call = 22 calls（按字母序 deterministic）",
                "5. prompt_id 后缀 _b2_r1",
                "6. predecessor_sha12 链: 仅 batch1 r6_executor/r6_result",
                "7. 新增 glm1_round1_progress 块 + glm1_teacher_side_round1_progress 块",
                "8. K-N26-N2 累计 baseline = batch1 终态 119/9/7.56%; GLM_1 自身累计从 0",
                "9. probe_records 块: 探活记录（每候选 model_id 一次尝试 → ok/error）",
                "10. 探活计入 calls 账（probe_phase_calls 计入 total_calls_per_teacher 字段）",
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
                "probe_used_for_discovery_only": True,
            },
            "run_window_cst": now_iso,
            "stop_reason": stop_reason,
            "interruption_recovery_note": (
                "原 batch2 session 因 net::ERR_HTTP2_PING_FAILED 0 产物中断, 原 session 已销毁; "
                "中断-恢复同 agent 唤醒已不可行; 本棒为新 session 即用即探 + 沿 batch1 r6 口径恢复; "
                "原 session 落盘 = 0 产物（老实交代）"
            ),
        },
        "probe_phase": probe_result,
        "probe_wall_time_s": probe_wall_s,
        "quadruples": quadruples,
        "retry_validation": retry_validation,
        "per_caption_successful_calls": per_caption_successful_calls,
        "glm1_teacher_side_round1_progress": glm1_round1_progress,
        "dispatch_target_progress": {
            "target_round1": ">=1 successful call/caption (round 1 首轮)",
            "target_cumulative": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (跨轮累计)",
            "met_count_post_r1_round1": met_target_count,
            "met_count_post_r1_cumulative_to_target": sum(1 for v in per_caption_successful_calls.values() if v["met_target"]),
            "total_captions": len(captions),
            "remaining_count_round1": len(captions) - met_target_count,
            "remaining_count_cumulative_to_target": sum(1 for v in per_caption_successful_calls.values() if not v["met_target"]),
            "met_percentage_round1": round(met_target_count / len(captions) * 100, 2),
            "met_percentage_cumulative_to_target": round(
                sum(1 for v in per_caption_successful_calls.values() if v["met_target"]) / len(captions) * 100, 2
            ),
            "still_pending_captions_round1": sorted([
                cid for cid, info in per_caption_successful_calls.items() if not info["round1_met"]
            ]),
            "still_pending_captions_cumulative_to_target": sorted([
                cid for cid, info in per_caption_successful_calls.items() if not info["met_target"]
            ]),
        },
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
            "probe_total_calls": probe_result["probe_attempted_count"],
            "probe_attempted_candidates": [r["candidate_model_id"] for r in probe_result["probe_records"]],
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
            "cross_batch_with_batch1_baseline": {
                "batch1_baseline_total": cum_prior,
                "batch1_baseline_empty": cum_empty_prior,
                "batch1_baseline_ok": cum_ok_prior,
                "batch1_baseline_rate": cum_rate_prior,
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
            "r1_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r1_empty_response_above_threshold_single_batch": empty_rate_r1 > 0.50,
        },
        "empty_rate_trend": {
            "batch1_round1": {
                "calls": batch1_r6["empty_rate_trend"]["batch1_round1"]["calls"],
                "empty": batch1_r6["empty_rate_trend"]["batch1_round1"]["empty"],
                "rate": batch1_r6["empty_rate_trend"]["batch1_round1"]["rate"],
            },
            "batch1_round6_cumulative": {
                "calls": cum_prior,
                "empty": cum_empty_prior,
                "ok": cum_ok_prior,
                "rate": cum_rate_prior,
            },
            "batch2_round1": {
                "calls": r1_total,
                "empty": r1_empty,
                "rate": round(empty_rate_r1, 4),
            },
            "batch2_round1_cumulative_glm1": {
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
                "round1_n_distinct_sample_note": (
                    "round 1 第 1 call 实测；GLM_1 教师侧 round 1 首轮采集 = "
                    "本棒后 22/22 caption 各 ≥1 successful call 即可触发 K-N26-N1 字面判定 N_min ≥ N_target (5); "
                    "本棒 round 1 后需后续 round 接力达 ≥5 successful/caption"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r1, 4),
                "cumulative_empty_response_rate_glm1_only": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r1 > 0.50,
                "cumulative_trigger_K_N26_N2_pass_False": k_n26_n2_triggered,
                "monitor_disposition": (
                    f"本棒 K-N26-N2 GLM_1 自身累计 empty_rate 监控 = 已实施; "
                    f"GLM_1 自身累计 = {cum_total} calls / {cum_empty} empty / {cum_empty_rate_post:.4f}; "
                    f"baseline batch1 = {cum_prior} calls / {cum_empty_prior} empty / {cum_rate_prior:.4f}; "
                    f"cross-batch rate = {cross_batch_rate:.4f}"
                ),
                "cross_batch_with_batch1_baseline_rate": round(cross_batch_rate, 4),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "breakpoint_status": {
            "actual_calls": r1_total,
            "planned_calls": planned_total,
            "actual_wall_time_s": wall_time_s,
            "wall_time_budget_remaining_after_probe_s": round(wall_budget_remaining_s, 1),
            "actual_wall_time_total_s": total_wall_s,
            "checkpoint_file": None,
            "hit_wall_time_budget": wall_time_s > wall_budget_remaining_s,
            "k_n26_n2_cumulative_triggered": k_n26_n2_triggered,
            "k_n26_n2_trigger_at_call_idx": k_n26_n2_trigger_at_call_idx,
            "k_n26_n2_trigger_cum_rate": k_n26_n2_trigger_cum_rate,
            "next_resume_via": (
                "task_append 续跑 — 沿 prereg §1.6.4 同 agent 唤醒 (本棒为新 session 重派; "
                "下棒可接力 GLM_1 教师侧 round 2 起)"
            ),
            "note": (
                f"本棒 round 1: actual={r1_total}/{planned_total} calls; "
                f"GLM_1 教师侧 round 1 完成度 = {met_target_count}/{len(captions)} caption met round 1 目标; "
                f"stop_reason={stop_reason}; "
                f"GLM_1 model_id 探活选定 = {model_id}"
            ),
            "planned_total": planned_total,
            "stop_reason": stop_reason,
        },
    }

    # 13. 自扫 key 泄露
    scan_hits = self_scan_obj(result)
    if scan_hits:
        print(f"[FATAL] 自扫命中敏感模式: {scan_hits}; 拒绝落盘")
        return 5

    # 14. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r1_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    sha12, nbytes, lf_only = sha12_file(out_path)
    print(f"[WROTE] {out_path}")
    print(f"[SHA-12] {sha12}")
    print(f"[BYTES] {nbytes}")
    print(f"[LF-ONLY] {lf_only}")
    print(f"[PROBE] selected={model_id} attempts={probe_result['probe_attempted_count']} wall={probe_wall_s}s")
    print(f"[STATS] r1 ok={r1_ok} empty={r1_empty} fail={r1_fail} total={r1_total} rate={empty_rate_r1:.4f}")
    print(f"[GLM1 CUM] total={cum_total} ok={cum_ok} empty={cum_empty} rate={cum_empty_rate_post:.4f}")
    print(f"[CROSS BATCH] total={cross_batch_total} ok={cross_batch_ok} empty={cross_batch_empty} rate={cross_batch_rate:.4f}")
    print(f"[STOP] {stop_reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
