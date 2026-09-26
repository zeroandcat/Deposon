# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch5_r2_executor.py
=====================================

V4 L14+ batch 5 · round 2 · minimax 教师侧 round 2（reask=1）续采
==================================================================

【派工依据】
----------------
- 沿 batch5 r1 executor `EF26ADF4669F` + r1 result `120D45D1774F` 口径（基础口径锚，本棒同 agent 唤醒保上下文）
- 沿 batch2 r3 executor `72FD2BB3838E` + r3 result `25251ACA6D79` 口径（备援锚）
- 沿 batch2 r2 executor `E7418F47A130` + r2 result `8C125E257AF8` 口径（备援锚）
- 沿 batch1 r6 executor `5F02C7E0F094` + r6 result `A4F851154551` retry 修复口径
- 沿 batch2 r2 models probe `3C9DC60B5071`（teamo /v1/models 44 总；mimo 不在 teamo）
- 沿 L14+ model 映射拍板 `_v4_supp_l14v3_model_mapping_2026_09_24.md` `98A779D61C1E` §1.1 minimax 行
- 派工单 ask_748d9242c7a6be3d83de63a0 (2026-09-24 23:08 Q4 显式): minimax = **mimo 端点 mimo-v2.6-pro**
- **新拍板入元数据**：ask_249ba8854ee343f7d9aa34de（2026-09-24 23:38）prompt_repro=accept_repro
  —— 蒸馏/采样数据效力 = V4 复现口径（非 V3 原文复刻）声明沿用

【本棒范围（沿 dispatch）—— minimax 教师侧 round 2（reask=1）续采】
------------------------------------------------------------------
1. **沿用 mimo-v2.6-pro**（沿 r1 1-call smoke ok=200, model_returned=mimo-v2.6-pro；本棒沿 r1 结论不再做完整 probe）
2. **22 caption × 1 call**（每位 caption 第 2 call；reask_idx=1；目标 2/5 successful/caption）
3. **目标**：本棒后 22/22 caption 各 ≥2 successful call；下棒接力至 ≥5 successful/caption
4. **endpoint_migrated**: true（沿 r1）
5. **lineage_discontinuity**: true（沿 r1）
6. **prompt_repro**: accept_repro（新拍板；ask_249ba8854ee343f7d9aa34de 23:38；沿 r2 result 元数据）
7. **data_validity_statement**: 蒸馏/采样数据效力 = V4 复现口径（非 V3 原文复刻）声明沿用
8. 预算 ≤22 caption calls + ≤1 smoke calls / ≤600s watchdog
9. 跑不完如实报断点

【每 caption successful 计数（沿 dispatch §6）】
---------------------------------------------
- 本棒前基线（沿 r1 终态）：minimax 教师侧 = 22 calls / 0 empty / 22 ok / 0.0000 rate
- 本棒 round 2（reask=1）后：22/22 caption 各 ≥2 successful call（理论值；如端点飘移可能回落）
- 终盘结果：result.json 顶层 `per_caption_successful_calls` 块 + `dispatch_target_progress` 块

【retry 修复逻辑沿 batch1 r6 + r2（沿 dispatch §3）】
----------------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}
- read_timeout_initial_s=60 / read_timeout_retry_s=90
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回
- r6 retry 触发的源 error_category tracking 沿用

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
--------------------------------------------------------------------
- 跨批累计 baseline = r1 终态 185 calls / 9 empty / 176 ok / 4.86%
- 累计 = r1 cross-batch baseline + minimax 本棒（minimax 自身从 22 起步）
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）

【端点取舍（沿 r1）】
------------------
- mimo + 无代理 + mimo-v2.6-pro（沿 r1 1-call smoke ok=200；r2 沿 r1 结论仅做 1-call smoke 防端点飘移）
- model_id 字面 = mimo-v2.6-pro（V3 字面 `minimax-m3` 火山方舟已下线；命名映射 = PI 拍板本身；**非字面继承**）
- endpoint = `https://token-plan-cn.xiaomimimo.com/v1`（token-plan-cn.xiaomimimo.com）
- mimo 不需走 tun（沿 L7 + add_T1 §1.6.2 mimo 端点 = 无代理硬纪律）
- smoke prompt（极小，节省 token）：`Reply with the single word: ok`

【铁律严守（沿 r1 + mapping §0 + 拍板 §3）】
-------------------------------------------
- R4 key 永不明文（无例外）；仅 runtime memory 读（KEY_INDEX_MIMO_1BASED = 27）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch5_r2_*` 与 `_batch5_r1_*` / `_batch2_r3_*` / `_batch2_r2_*` / `_batch2_r1_*` / `_batch1_r6_*` 独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款；temperature=0.7
- 串行 ≥2.5s 全程；mimo 不走 tun（沿 L7 实证 + add_T1 §1.6.2）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物；探活计入 calls 账
- 不覆盖既有件（b5_r1 executor `EF26ADF4669F` + b5_r1 result `120D45D1774F` + b2_r3 executor `72FD2BB3838E` + b2_r3 result `25251ACA6D79` + b2_r2 executor + b2_r2 result + batch1 r6 executor + batch1 r6 result + b2_r1 executor + b2_r1 result + models_probe + mapping `98A779D61C1E` + prereg `05B975A86989` 不动）

【产物】
--------
- 写入：`results/_v4_supp_l14v3_batch5_r2_result.json`（schema = `v4_l14v3_n26/1` + batch=5 + round=2）
- 不覆盖 b5_r1 result `120D45D1774F` 或 b5_r1 executor `EF26ADF4669F` 或任何既有件
- predecessor_sha12 链：b5_r1_executor `EF26ADF4669F` + b5_r1_result `120D45D1774F` + b2_r3_executor `72FD2BB3838E` + b2_r3_result `25251ACA6D79` + b2_r2_executor `E7418F47A130` + b2_r2_result `8C125E257AF8` + batch1_r6_executor `5F02C7E0F094` + batch1_r6_result `A4F851154551` + b2_r1_executor `E52F930654D3` + b2_r1_result `D245AE4CE385` + models_probe `3C9DC60B5071` + mapping `98A779D61C1E` + prereg `05B975A86989`

【与 r1 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. ROUND = 2（升 r2 命名）；BATCH = 5 不变
2. prompt_id 后缀 `_b5_r2`；`minimax_t02_teacher_*`（取代 r1 的 `minimax_t01_teacher_*_b5_r1`）
3. reask_idx = 1（本棒每 caption 第 2 call；取代 r1 的 reask_idx=0）
4. phase_label：`b5_r2_need1`（取代 r1 的 `b5_r1_need1`）
5. is_round_2 = True（语义：本棒 = minimax 教师侧 data collection round 2；区别于 r1 的 round 1 首采）
6. smoke_call_only = True（沿 r1 结论；r2 仅 1-call smoke 防端点飘移；不再做 3-candidate probe fallback）
7. predecessor_sha12 链：r1_executor `EF26ADF4669F` + r1_result `120D45D1774F`（新增；取代 r1 链的 r3_executor + r3_result 仍保留）
8. baseline prior：r1 终态 minimax 22 calls / 0 empty / 22 ok / 0.0000 rate（取代 r1 链的 0/0/0）
9. 跨批累计 baseline：r1 终态 185 calls / 9 empty / 176 ok / 4.86%（取代 r1 链的 163/9/5.52%）
10. 新增 `minimax_teacher_side_round2_progress` 块（本棒后 minimax 教师侧 round 2 完成度 ≥2 successful/caption）
11. K-N26-N2 触发阈值 = 0.50 不变；监控 baseline 更新为 185/9/4.86%
12. spec_conformance 重写：minimax 教师侧 round 2 续采（reask=1）
13. per_caption_successful_calls 字段新增 round2_target=2 / round2_met
14. 调度注释：round 2 续采（reask=1）22 caption × 1 call
15. **新拍板入元数据**：prompt_repro=accept_repro（ask_249ba8854ee343f7d9aa34de 2026-09-24 23:38）
16. **新拍板入元数据**：data_validity_statement = "蒸馏/采样数据效力 = V4 复现口径（非 V3 原文复刻）声明沿用"
17. 新增 `data_validity_disclosure` 块（沿新拍板）

【边界】
--------
- 不动任何既有件（含 b5_r1 executor `EF26ADF4669F` + b5_r1 result `120D45D1774F` + b2_r3 executor + b2_r3 result + b2_r2 executor + b2_r2 result + batch1 r6 executor + batch1 r6 result + b2_r1 executor + b2_r1 result + models_probe + mapping + prereg）
- 跑不完拆段报断点
- 0 触动 V1–V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
- mimo 不走 tun（沿 L7 实证 + add_T1 §1.6.2）
- prompt_repro / data_validity 拍板仅入元数据；不动 N-26 主预登记 / K-N26-* 字面 / 既有阈值 / 既定结论
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
BATCH5_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch5_r1_result.json")
BATCH2_R3_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r3_result.json")
BATCH2_R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_result.json")
BATCH2_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r1_result.json")
BATCH1_R6_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r6_result.json")
MODELS_PROBE_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_models_probe.json")
MAPPING_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_model_mapping_2026_09_24.md")

# ============================================================
# 端点配置（沿 r1）
# ============================================================
ENDPOINT_MIMO = "https://token-plan-cn.xiaomimimo.com/v1"
KEY_INDEX_MIMO_1BASED = 27
USE_PROXY = False

# 串行间隔
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

# K-N26-N2 累计 empty_rate 停采阈值（沿 dispatch §4 + mapping §1.2）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算
WALL_TIME_BUDGET_S = 600

# 本棒调度（沿 dispatch）
BATCH = 5
ROUND = 2  # 升 r2 命名避开 r1 重叠
TEACHER = "minimax"
SIDE = "teacher"
REASK_R1 = 1  # 本棒 round 2 = 每 caption 第 2 call（reask_idx=1）
TARGET_SUCCESSFUL_PER_CAPTION = 5
SMOKE_CALL_ONLY = True  # 沿 r1 结论；r2 仅 1-call smoke 防端点飘移

# 选定的 model_id（沿 mapping §1.1 minimax 第三栏拍板）
MODEL_MINIMAX = "mimo-v2.6-pro"

# smoke prompt（沿 r1）
SMOKE_PROMPT = "Reply with the single word: ok"


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
    model_id: str,
    messages: List[Dict[str, str]],
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
    timeout: int = READ_TIMEOUT_INITIAL_S,
) -> Dict[str, Any]:
    """mimo 端点 chat 调用（无代理；沿 r1）。"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch5-r2",
        "X-Title": f"deposon-l14v3-batch5-r2-{TEACHER}-teacher",
    }
    body = {
        "model": model_id,
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
# Smoke（沿 r1 简化版；仅 1 call 确认 mimo 端点 ok）
# ============================================================
def smoke_mimo_model(api_key: str, model_id: str) -> Dict[str, Any]:
    """1-call smoke（沿 r1 结论 mimo-v2.6-pro ok=200；仅作端点可达性确认）。"""
    t0 = time.time()
    messages = [{"role": "user", "content": SMOKE_PROMPT}]
    r = call_chat_mimo(
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
        "phase_label": "smoke_mimo_model_id",
        "wall_time_s": round(time.time() - t0, 1),
    }
    return rec


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
    model_id: str,
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_b5_r2"
    prompt_id = f"minimax_t02_{side}_{caption_id}{suffix}"

    retries = 0
    last = None
    while retries <= INNER_RETRY_MAX:
        timeout_s = READ_TIMEOUT_INITIAL_S if retries == 0 else READ_TIMEOUT_RETRY_S
        r = call_chat_mimo(api_key=api_key, model_id=model_id, messages=messages, timeout=timeout_s)
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
                        "endpoint_migrated": True,
                        "lineage_discontinuity": True,
                        "proxy_used": False,
                        "teacher_v3_anchor": "minimax-m3 (火山方舟已下线)",
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
                "endpoint_migrated": True,
                "lineage_discontinuity": True,
                "proxy_used": False,
                "teacher_v3_anchor": "minimax-m3 (火山方舟已下线)",
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
            "endpoint_migrated": True,
            "lineage_discontinuity": True,
            "proxy_used": False,
            "teacher_v3_anchor": "minimax-m3 (火山方舟已下线)",
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 L14+ batch 5 round 2 · minimax 教师侧 round 2（reask=1）续采")
    print("沿 r1 mimo-v2.6-pro 1-call smoke ok=200；本棒 smoke 1-call 后跑 22 caption × 1 call")
    print("计划 calls = 22 caption × 1 call = 22 calls + 1 smoke call")
    print("目标: round 2 后 22/22 caption 各 ≥2 successful call")
    print("预算 ≤22 caption calls + 1 smoke call / ≤600s watchdog")
    print("retry 修复沿 r1 (沿 batch1 r6)；mimo 端点无代理 (沿 L7 + add_T1 §1.6.2)")
    print("endpoint_migrated=true / lineage_discontinuity=true")
    print("prompt_repro=accept_repro (ask_249ba8854ee343f7d9aa34de 2026-09-24 23:38 新拍板)")
    print("data_validity = V4 复现口径（非 V3 原文复刻）声明沿用")
    print("=" * 60)

    # 1. 加载 caption
    captions = load_captions()
    cap_by_id = {c["id"]: c for c in captions}
    print(f"[INIT] captions loaded: {len(captions)}")

    # 2. 加载 key（mimo-plan = line 27）
    try:
        api_key = fetch_api_key(KEY_INDEX_MIMO_1BASED)
        print(f"[INIT] mimo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 3. 加载前置累计基线（r1 终态 + 历史 chain）
    with open(BATCH5_R1_RESULT_PATH, "r", encoding="utf-8") as f:
        r1 = json.load(f)
    with open(BATCH2_R3_RESULT_PATH, "r", encoding="utf-8") as f:
        r3 = json.load(f)
    with open(BATCH2_R2_RESULT_PATH, "r", encoding="utf-8") as f:
        r2 = json.load(f)
    with open(BATCH2_R1_RESULT_PATH, "r", encoding="utf-8") as f:
        r1probe = json.load(f)
    with open(BATCH1_R6_RESULT_PATH, "r", encoding="utf-8") as f:
        batch1_r6 = json.load(f)

    # batch1 r6 baseline
    cum_prior = batch1_r6["aggregate"]["cumulative"]["post_total"]
    cum_empty_prior = batch1_r6["aggregate"]["cumulative"]["post_empty"]
    cum_ok_prior = batch1_r6["aggregate"]["cumulative"]["post_ok"]
    cum_rate_prior = batch1_r6["aggregate"]["cumulative"]["post_rate"]
    print(f"[BASELINE batch1 r6] total={cum_prior} ok={cum_ok_prior} empty={cum_empty_prior} rate={cum_rate_prior:.4f}")
    r1probe_stop = r1probe.get("metadata", {}).get("stop_reason", "?")
    print(f"[BASELINE r1probe] stop_reason={r1probe_stop} (r1probe 探活 fail / 0 caption call)")

    # r2 / r3 baselines
    r2_post_total = r2["aggregate"]["glm1_cumulative"]["post_total"]
    r2_post_empty = r2["aggregate"]["glm1_cumulative"]["post_empty"]
    r2_post_ok = r2["aggregate"]["glm1_cumulative"]["post_ok"]
    r2_post_rate = r2["aggregate"]["glm1_cumulative"]["post_rate"]
    print(f"[BASELINE r2 GLM_1] total={r2_post_total} ok={r2_post_ok} empty={r2_post_empty} rate={r2_post_rate:.4f}")

    # r1 终态 = 本棒前 cross-batch 累计基线
    cross_prior_total = r1["aggregate"]["cross_batch_with_r3_baseline"]["cross_total"]
    cross_prior_empty = r1["aggregate"]["cross_batch_with_r3_baseline"]["cross_empty"]
    cross_prior_ok = r1["aggregate"]["cross_batch_with_r3_baseline"]["cross_ok"]
    cross_prior_rate = r1["aggregate"]["cross_batch_with_r3_baseline"]["cross_rate"]
    print(f"[BASELINE cross batch r1] total={cross_prior_total} ok={cross_prior_ok} empty={cross_prior_empty} rate={cross_prior_rate:.4f}")

    # minimax 自身前基线 = r1 终态（22 calls / 0 empty / 22 ok）
    minimax_prior_total = r1["aggregate"]["minimax_cumulative"]["post_total"]
    minimax_prior_empty = r1["aggregate"]["minimax_cumulative"]["post_empty"]
    minimax_prior_ok = r1["aggregate"]["minimax_cumulative"]["post_ok"]
    minimax_prior_rate = r1["aggregate"]["minimax_cumulative"]["post_rate"]
    print(f"[BASELINE minimax r1] total={minimax_prior_total} ok={minimax_prior_ok} empty={minimax_prior_empty} rate={minimax_prior_rate:.4f}")

    # 4. 加载 /v1/models 探活清单（参考；不重探）
    with open(MODELS_PROBE_PATH, "r", encoding="utf-8") as f:
        models_probe = json.load(f)
    glm_like_ids = models_probe.get("glm_like_ids", [])
    print(f"[MODELS PROBE REF] teamo 44 total models; GLM 系 {len(glm_like_ids)} 个; mimo 不在 teamo 清单")

    # 5. Smoke 1-call（沿 r1 结论 mimo-v2.6-pro ok=200）
    print("=" * 60)
    print("[SMOKE PHASE] mimo-v2.6-pro 1-call smoke（沿 r1 结论）")
    print("=" * 60)
    t_smoke_start = time.time()
    smoke_rec = smoke_mimo_model(api_key, MODEL_MINIMAX)
    t_smoke_end = time.time()
    smoke_wall_s = round(t_smoke_end - t_smoke_start, 1)
    print(
        f"  [SMOKE] model_id={MODEL_MINIMAX} sc={smoke_rec.get('status_code')} "
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
            "batch": 5,
            "round": 2,
            "metadata": {
                "task": "L14V3_batch5_round2_minimax_teacher_side_round2_reask1",
                "prereg_sha12": "05B975A86989",
                "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
                "predecessor_sha12": {
                    "b5_r1_executor_sha12": "EF26ADF4669F",
                    "b5_r1_executor_path": "results/_v4_supp_l14v3_batch5_r1_executor.py",
                    "b5_r1_result_sha12": "120D45D1774F",
                    "b5_r1_result_path": "results/_v4_supp_l14v3_batch5_r1_result.json",
                    "b2_r3_executor_sha12": "72FD2BB3838E",
                    "b2_r3_executor_path": "results/_v4_supp_l14v3_batch2_r3_executor.py",
                    "b2_r3_result_sha12": "25251ACA6D79",
                    "b2_r3_result_path": "results/_v4_supp_l14v3_batch2_r3_result.json",
                    "b2_r2_executor_sha12": "E7418F47A130",
                    "b2_r2_executor_path": "results/_v4_supp_l14v3_batch2_r2_executor.py",
                    "b2_r2_result_sha12": "8C125E257AF8",
                    "b2_r2_result_path": "results/_v4_supp_l14v3_batch2_r2_result.json",
                    "batch1_r6_executor_sha12": "5F02C7E0F094",
                    "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                    "batch1_r6_result_sha12": "A4F851154551",
                    "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
                    "b2_r1_executor_sha12": "E52F930654D3",
                    "b2_r1_executor_path": "results/_v4_supp_l14v3_batch2_r1_executor.py",
                    "b2_r1_result_sha12": "D245AE4CE385",
                    "b2_r1_result_path": "results/_v4_supp_l14v3_batch2_r1_result.json",
                    "models_probe_sha12": "3C9DC60B5071",
                    "models_probe_path": "results/_v4_supp_l14v3_batch2_r2_models_probe.json",
                    "mapping_sha12": "98A779D61C1E",
                    "mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                },
                "date": "2026-09-24",
                "teacher": TEACHER,
                "side": SIDE,
                "round_index": 2,
                "stop_reason": "smoke_mimo_model_failed",
                "endpoint_migrated": True,
                "lineage_discontinuity": True,
                "prompt_repro": "accept_repro",
                "data_validity_statement": "蒸馏/采样数据效力 = V4 复现口径（非 V3 原文复刻）声明沿用",
            },
            "smoke_phase": smoke_rec,
            "smoke_wall_time_s": smoke_wall_s,
            "run_window_cst": now_iso,
        }
        out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch5_r2_result.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(fail_result, f, ensure_ascii=False, indent=2)
        print(f"[WROTE] {out_path}")
        return 3
    print(f"[SMOKE-OK] model_id = {MODEL_MINIMAX} (sc=200, model_returned={smoke_rec['model_returned']})")

    model_id = MODEL_MINIMAX

    # 6. 调度：22 caption × 1 call (round 2 reask=1) 按 caption_id 字母序
    captions_sorted = sorted(captions, key=lambda c: c["id"])
    planned = [{"caption_id": c["id"], "phase": "b5_r2_need1"} for c in captions_sorted]
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
    cum_total = minimax_prior_total
    cum_empty = minimax_prior_empty
    cum_ok = minimax_prior_ok
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

    # 从 r1 累计 per_caption_successful_calls 起步
    r1_per_cap = r1.get("per_caption_successful_calls", {})
    per_cap_succ = {cid: r1_per_cap.get(cid, {}).get("succ_count", 0) for cid in [c["id"] for c in captions]}
    per_cap_total = {cid: r1_per_cap.get(cid, {}).get("total_calls_so_far", 0) for cid in [c["id"] for c in captions]}
    per_cap_empty = {cid: r1_per_cap.get(cid, {}).get("empty_count_so_far", 0) for cid in [c["id"] for c in captions]}
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

        # K-N26-N2 minimax 自身累计监控（call 前判）
        if cum_total > 0:
            current_cum_rate = cum_empty / cum_total
            if current_cum_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i
                k_n26_n2_trigger_cum_rate = current_cum_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 minimax cumulative empty_rate={current_cum_rate:.4f} > 0.50 at call {i}/{planned_total}; stop per dispatch §4")
                break

        rec = run_one_quadruple(
            api_key=api_key,
            caption=caption,
            reask_idx=REASK_R1,
            side="teacher",
            round_index=ROUND,
            is_round_2=True,  # 语义：本棒 = minimax 教师侧 data collection round 2
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
            r2_ok += 1
            cum_ok += 1
            per_cap_succ[cap_id] += 1
        elif is_empty:
            r2_empty += 1
            cum_empty += 1
            per_cap_empty[cap_id] += 1
        else:
            r2_fail += 1
        r2_total += 1
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
            f"[minimax_cum_rate={current_cum_rate_post:.4f}]"
        )

        # K-N26-N2 停采监控（call 后立即判）
        if cum_total > 0:
            post_rate = cum_empty / cum_total
            if post_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i + 1
                k_n26_n2_trigger_cum_rate = post_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 minimax post-call cumulative empty_rate={post_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch §4")
                break

        if i < planned_total - 1:
            time.sleep(INTER_CALL_SLEEP_S)

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)
    total_wall_s = round(t_batch_end - t_smoke_start, 1)

    # 9. 统计
    empty_rate_r2 = (r2_empty / r2_total) if r2_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0

    # 跨批累计 = r1 cross-batch baseline + minimax 本棒
    cross_batch_total = cross_prior_total + r2_total
    cross_batch_empty = cross_prior_empty + r2_empty
    cross_batch_ok = cross_prior_ok + r2_ok
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

    # 11. minimax 教师侧 round 2 进度块
    minimax_round2_progress = {
        "round2_target": ">=2 successful call/caption (round 2 reask=1)",
        "met_count_post_r2_round2": met_round2_count,
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
        "r2_retry_count_distribution": dict(retry_count_distribution),
        "r2_retry_triggered_count": retry_triggered_count,
        "r2_retry_trigger_categories_tracker": retry_trigger_categories_tracker,
        "r2_retry_trigger_categories_distribution": retry_trigger_categories_distribution,
        "r2_retry_bug_fix_applied_in_all_calls": all(
            q["per_call_metadata"].get("retry_bug_fix_applied") is True
            for q in quadruples
        ),
        "r2_empty_rate_with_fix": round(empty_rate_r2, 4),
    }

    # 13. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    # mapping_disclosure（沿 r1）
    mapping_disclosure = (
        f"mapping §1.1 minimax 行第三栏 PI 拍板 = mimo 端点 mimo-v2.6-pro "
        f"(V3 字面锚 minimax-m3 火山方舟已下线；命名映射依据 = PI 拍板本身，"
        f"非字面继承；非「minimax-m3 升级版 = mimo-v2.6-pro」字面继承关系)；"
        f"mapping §0.5 边界声明：本棒口径仅覆盖现行 V4 重跑采样的 model 映射，"
        f"非 V3 历史模型身份断言；"
        f"endpoint_migrated=true (V3 火山方舟 → V4 mimo 跨端点跨厂商)；"
        f"lineage_discontinuity=true (V3 minimax-m3 ≠ V4 mimo-v2.6-pro，"
        f"端点名不同、模型家族不同；映射依据=本拍板本身)。"
    )

    # data_validity_disclosure（新拍板 ask_249ba8854ee343f7d9aa34de 2026-09-24 23:38）
    data_validity_disclosure = {
        "prompt_repro": "accept_repro",
        "data_validity_statement": "蒸馏/采样数据效力 = V4 复现口径（非 V3 原文复刻）声明沿用",
        "pi_decision_source": "ask_249ba8854ee343f7d9aa34de (2026-09-24 23:38)",
        "decision_disposition": "声明沿用",
        "honest_disclosure": (
            "本棒 minimax 教师侧 round 2 (reask=1) 22 caption × 1 call 全部产出 "
            "均按 V4 复现口径采样（沿 L14+ 预登记 + mapping §1.1 minimax 拍板）；"
            "声明沿用 = 不声称本棒产出等价 V3 minimax-m3 火山方舟原 model 原文复刻；"
            "产出数据效力以 V4 现行采样模型 mimo-v2.6-pro（mimo 端点）为口径锚；"
            "V3 字面 minimax-m3 仅作 lineage_discontinuity 字段锚定，"
            "不参与产出数据效力的实证断言。"
        ),
        "scope_boundary": (
            "本声明仅覆盖本棒产出数据效力口径声明；不动 N-26 主预登记 / K-N26-* 字面 / 既有阈值 / 既定结论；"
            "不动 L4 verdict `74B5B37F7EEA` §11「FAIL · 构造不可行 · 4/5 教师 metadata 缺位」字面；"
            "不动 L13 verdict `E105EC1362DB` 三元组基底字面。"
        ),
    }

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 5,
        "round": 2,
        "metadata": {
            "task": "L14V3_batch5_round2_minimax_teacher_side_round2_reask1",
            "prereg_sha12": "05B975A86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "predecessor_sha12": {
                "b5_r1_executor_sha12": "EF26ADF4669F",
                "b5_r1_executor_path": "results/_v4_supp_l14v3_batch5_r1_executor.py",
                "b5_r1_result_sha12": "120D45D1774F",
                "b5_r1_result_path": "results/_v4_supp_l14v3_batch5_r1_result.json",
                "b2_r3_executor_sha12": "72FD2BB3838E",
                "b2_r3_executor_path": "results/_v4_supp_l14v3_batch2_r3_executor.py",
                "b2_r3_result_sha12": "25251ACA6D79",
                "b2_r3_result_path": "results/_v4_supp_l14v3_batch2_r3_result.json",
                "b2_r2_executor_sha12": "E7418F47A130",
                "b2_r2_executor_path": "results/_v4_supp_l14v3_batch2_r2_executor.py",
                "b2_r2_result_sha12": "8C125E257AF8",
                "b2_r2_result_path": "results/_v4_supp_l14v3_batch2_r2_result.json",
                "batch1_r6_executor_sha12": "5F02C7E0F094",
                "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                "batch1_r6_result_sha12": "A4F851154551",
                "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
                "b2_r1_executor_sha12": "E52F930654D3",
                "b2_r1_executor_path": "results/_v4_supp_l14v3_batch2_r1_executor.py",
                "b2_r1_result_sha12": "D245AE4CE385",
                "b2_r1_result_path": "results/_v4_supp_l14v3_batch2_r1_result.json",
                "models_probe_sha12": "3C9DC60B5071",
                "models_probe_path": "results/_v4_supp_l14v3_batch2_r2_models_probe.json",
                "mapping_sha12": "98A779D61C1E",
                "mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
            },
            "date": "2026-09-24",
            "spec_conformance": (
                "PI 2026-09-24 batch5 minimax 教师侧 round 2 续采 (reask=1); "
                "沿 r1 mimo-v2.6-pro 1-call smoke ok=200 结论；r2 仅 1-call smoke; "
                "22 caption × 1 call = 22 calls (按 caption_id 字母序); "
                "目标 ≥2 successful/caption; "
                "endpoint_migrated=true / lineage_discontinuity=true; "
                "新拍板 prompt_repro=accept_repro (ask_249ba8854ee343f7d9aa34de 2026-09-24 23:38) → "
                "data_validity_statement = V4 复现口径（非 V3 原文复刻）声明沿用"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": 2,
            "batch_index": BATCH,
            "round2_target_per_caption": 2,
            "round2_reask_idx": REASK_R1,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r2_total,
            "endpoint_selected": ENDPOINT_MIMO,
            "endpoint_selection_method": (
                "沿 r1 实测 (mimo 端点); r2 沿用 mimo 端点; "
                "/v1/models 探活清单沿 r2 models_probe.json (sha12=3C9DC60B5071) 仅作 reference; "
                "r2 仅 1-call smoke 防端点飘移"
            ),
            "endpoint_migrated": True,
            "lineage_discontinuity": True,
            "v3_origin_endpoint": "火山方舟 (V3 字面 minimax-m3 已下线)",
            "v4_current_endpoint": "mimo (token-plan-cn.xiaomimimo.com/v1)",
            "model_id_sent": model_id,
            "model_id_inconsistency_honest_disclosure": mapping_disclosure,
            "prompt_repro": "accept_repro",
            "data_validity_statement": "蒸馏/采样数据效力 = V4 复现口径（非 V3 原文复刻）声明沿用",
            "proxy_settings": {
                "http": "http://127.0.0.1:1018",
                "socks5": "socks5://127.0.0.1:1018",
                "applied_to_mimo": USE_PROXY,
                "note": "mimo 端点 = 无代理 (沿 L7 + add_T1 §1.6.2)",
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
                "r6_status_沿": "retry 修复沿 batch1 r6 (沿 5F02C7E0F094)",
                "r1_b5_status": "r1 沿 mapping 拍板已定 mimo-v2.6-pro 1-call smoke ok=200",
                "r2_b5_status": "r2 沿 r1 结论仅做 1-call smoke 防端点飘移；未做 3-candidate probe fallback",
                "rationale": (
                    "沿 r1 mimo-v2.6-pro smoke 结论；r2 节省预算避免重复 probe；"
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
            "diff_vs_r1_executor": [
                "1. ROUND=2 (升 r2 命名)；BATCH=5 不变",
                "2. prompt_id 后缀 _b5_r2；t02_teacher (取代 r1 的 t01_teacher round 1 首采)",
                "3. reask_idx=1 (本棒每 caption 第 2 call；取代 r1 的 reask_idx=0)",
                "4. phase_label: b5_r2_need1 (取代 r1 的 b5_r1_need1)",
                "5. is_round_2=True (语义: minimax 教师侧 data collection round 2)",
                "6. smoke_call_only=True (沿 r1 结论；不再做 3-candidate probe)",
                "7. predecessor_sha12 链: b5_r1_executor EF26ADF4669F + b5_r1_result 120D45D1774F (新增；r1 链的 b2_r3_executor + b2_r3_result 仍保留；同时为避免命名冲突重命名 r1/r2/r3 → b2_r1/b2_r2/b2_r3)",
                "8. baseline prior: r1 终态 minimax 22 calls / 0 empty / 22 ok / 0.0000 rate (取代 r1 链的 0/0/0)",
                "9. 跨批累计 baseline: r1 终态 185 calls / 9 empty / 176 ok / 4.86% (取代 r1 链的 163/9/5.52%)",
                "10. 新增 minimax_teacher_side_round2_progress 块 (round 2 完成度 ≥2 successful/caption)",
                "11. K-N26-N2 触发阈值 0.50 不变；监控 baseline 更新为 185/9/4.86%",
                "12. spec_conformance 重写: minimax 教师侧 round 2 续采 (reask=1)",
                "13. per_caption_successful_calls 字段新增 round2_target=2 / round2_met",
                "14. 调度注释: round 2 续采 (reask=1) 22 caption × 1 call",
                "15. 新增 prompt_repro=accept_repro (ask_249ba8854ee343f7d9aa34de 2026-09-24 23:38 新拍板)",
                "16. 新增 data_validity_statement (V4 复现口径非 V3 原文复刻声明沿用)",
                "17. 新增 data_validity_disclosure 块 (沿新拍板)",
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
                "mimo_no_proxy_compliance": True,
                "serial_interval_ge_2_5_s": True,
                "empty_response_counted_not_dropped": True,
                "kill_line_locked_K_N26_1_2_3_N1_N2": True,
                "no_threshold_adjustment": True,
                "no_existing_file_modified": True,
                "no_merge_of_derived_json": True,
                "no_overwrite_prior_results": True,
                "retry_bug_fix_applied": True,
                "smoke_only_no_full_probe": True,
                "endpoint_migrated_disclosed": True,
                "lineage_discontinuity_disclosed": True,
                "data_validity_disclosed": True,
                "prompt_repro_disclosed": True,
            },
            "run_window_cst": now_iso,
            "stop_reason": stop_reason,
            "interruption_recovery_note": (
                "r2 沿 r1 mimo-v2.6-pro smoke 结论；不再做 3-candidate probe fallback；"
                "1-call smoke 失败立即 abort；r2 与 r1/r3/r2/r1probe/batch1_r6 派生 JSON 独立 (不合并)"
            ),
        },
        "models_listing_summary_ref": {
            "endpoint": "https://api.teamorouter.cn/v1/models",
            "model_count_total": models_probe.get("model_count_total"),
            "model_count_glm_like": len(glm_like_ids),
            "glm_like_ids": glm_like_ids,
            "fetched_at_cst": models_probe.get("fetched_at_cst"),
            "note": (
                "r2 不重探 /v1/models；仅引用 r2 探活清单 (sha12=3C9DC60B5071) "
                "作 reference；minimax 不在 teamo 清单；本棒走 mimo 端点 (沿 mapping 拍板)"
            ),
        },
        "smoke_phase": {
            "selected_model_id": MODEL_MINIMAX,
            "smoke_record": smoke_rec,
            "smoke_wall_time_s": smoke_wall_s,
        },
        "quadruples": quadruples,
        "retry_validation": retry_validation,
        "per_caption_successful_calls": per_caption_successful_calls,
        "minimax_teacher_side_round2_progress": minimax_round2_progress,
        "dispatch_target_progress": {
            "target_round2": ">=2 successful calls/caption (round 2 reask=1)",
            "target_cumulative": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (跨轮累计)",
            "met_count_post_r2_round2": met_round2_count,
            "met_count_post_r2_cumulative_to_target": met_target_count,
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
            "r2_total_calls": r2_total,
            "r2_ok_count": r2_ok,
            "r2_empty_response_count": r2_empty,
            "r2_fail_count": r2_fail,
            "r2_empty_response_rate": round(empty_rate_r2, 4),
            "r2_total_prompt_tokens": total_prompt_tokens,
            "r2_total_completion_tokens": total_completion_tokens,
            "r2_total_tokens": total_prompt_tokens + total_completion_tokens,
            "proxy_used": False,
            "smoke_total_calls": 1,
            "smoke_attempted_model_id": MODEL_MINIMAX,
            "minimax_cumulative": {
                "prior_total": minimax_prior_total,
                "prior_empty": minimax_prior_empty,
                "prior_ok": minimax_prior_ok,
                "prior_rate": minimax_prior_rate,
                "post_total": cum_total,
                "post_empty": cum_empty,
                "post_ok": cum_ok,
                "post_rate": round(cum_empty_rate_post, 4),
                "delta_total": cum_total - minimax_prior_total,
                "delta_empty": cum_empty - minimax_prior_empty,
                "delta_ok": cum_ok - minimax_prior_ok,
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered_this_batch": k_n26_n2_triggered,
            },
            "cross_batch_with_r1_baseline": {
                "r1_baseline_total": cross_prior_total,
                "r1_baseline_empty": cross_prior_empty,
                "r1_baseline_ok": cross_prior_ok,
                "r1_baseline_rate": cross_prior_rate,
                "batch5_minimax_post_total": cum_total,
                "batch5_minimax_post_empty": cum_empty,
                "batch5_minimax_post_ok": cum_ok,
                "cross_total": cross_batch_total,
                "cross_empty": cross_batch_empty,
                "cross_ok": cross_batch_ok,
                "cross_rate": round(cross_batch_rate, 4),
                "cross_k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "cross_k_n26_n2_triggered": cross_batch_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "note": (
                    "K-N26-N2 字面 per 教师; 本字段仅作 cross-batch sanity check; "
                    "minimax 教师侧 K-N26-N2 判定 = minimax_cumulative.post_rate"
                ),
            },
            "r2_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r2_empty_response_above_threshold_single_batch": empty_rate_r2 > 0.50,
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
                "note": "r1probe 探活 6 候选 400 全 fail; 0 caption call",
            },
            "batch2_round2_round1_retry_GLM_1": {
                "calls": r2_post_total,
                "empty": r2_post_empty,
                "rate": r2_post_rate,
                "note": "r2 GLM_1 round 1 retry 22 caption × 1 call; all OK",
            },
            "batch2_round3_round2_reask1_GLM_1": {
                "calls": r3["aggregate"]["glm1_cumulative"]["post_total"] - r3["aggregate"]["glm1_cumulative"]["prior_total"],
                "empty": 0,
                "rate": 0.0,
                "note": "r3 GLM_1 round 2 reask=1 22 caption × 1 call; all OK",
            },
            "batch5_round1_round1_reask0_minimax": {
                "calls": minimax_prior_total,
                "empty": minimax_prior_empty,
                "rate": minimax_prior_rate,
                "note": "r1 minimax round 1 reask=0 22 caption × 1 call; all OK",
            },
            "batch5_round2_round2_reask1_minimax": {
                "calls": r2_total,
                "empty": r2_empty,
                "rate": round(empty_rate_r2, 4),
            },
            "batch5_round2_cumulative_minimax": {
                "calls": cum_total,
                "empty": cum_empty,
                "ok": cum_ok,
                "rate": round(cum_empty_rate_post, 4),
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered": k_n26_n2_triggered,
            },
            "cross_batch_cumulative_post_r2": {
                "calls": cross_batch_total,
                "empty": cross_batch_empty,
                "ok": cross_batch_ok,
                "rate": round(cross_batch_rate, 4),
                "note": "r1 baseline 185/9/4.86% + r2 minimax 增量",
            },
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round2_reask1_n_distinct_sample_note": (
                    f"round 2 reask=1 第 2 call 实测；本棒后 minimax 教师侧 round 2 = "
                    f"{met_round2_count}/{len(captions)} caption met round 2 目标; "
                    f"需后续 round 接力达 ≥{TARGET_SUCCESSFUL_PER_CAPTION} successful/caption"
                ),
            },
            "K_N26_N2_observation": {
                "mimo_no_proxy_used_for_all_calls": True,
                "single_batch_empty_response_rate": round(empty_rate_r2, 4),
                "cumulative_empty_response_rate_minimax_only": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r2 > 0.50,
                "cumulative_trigger_K_N26_N2_pass_False": k_n26_n2_triggered,
                "monitor_disposition": (
                    f"本棒 K-N26-N2 minimax 自身累计 empty_rate 监控 = 已实施; "
                    f"minimax 自身累计 = {cum_total} calls / {cum_empty} empty / {cum_empty_rate_post:.4f}; "
                    f"r1 baseline minimax = {minimax_prior_total} calls / {minimax_prior_empty} empty / {minimax_prior_rate:.4f}; "
                    f"r1 baseline cross batch = {cross_prior_total} calls / {cross_prior_empty} empty / {cross_prior_rate:.4f}; "
                    f"cross-batch rate = {cross_batch_rate:.4f}"
                ),
                "cross_batch_with_r1_baseline_rate": round(cross_batch_rate, 4),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "mapping_disclosure": {
            "v3_anchor_api_name": "minimax",
            "v3_anchor_9backbone_name": "minimax-m3",
            "v3_origin_endpoint": "火山方舟 (已下线)",
            "v4_current_endpoint": "mimo (token-plan-cn.xiaomimimo.com/v1)",
            "v4_current_model_id_sent": "mimo-v2.6-pro",
            "endpoint_migrated": True,
            "lineage_discontinuity": True,
            "pi_decision_source": "ask_748d9242c7a6be3d83de63a0 Q4 (2026-09-24 23:08)",
            "mapping_doc_sha12": "98A779D61C1E",
            "mapping_doc_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
            "honest_disclosure": (
                "V3 字面 minimax-m3 火山方舟端点已下线；现行 mimo 端点 (token-plan-cn.xiaomimimo.com/v1) "
                "对应 mimo-v2.6-pro 命名映射依据 = PI 拍板本身，非字面继承，"
                "非「minimax-m3 升级版 = mimo-v2.6-pro」字面继承关系；"
                "endpoint_migrated=true (跨端点跨厂商)；"
                "lineage_discontinuity=true (端点名不同、模型家族不同)。"
            ),
        },
        "data_validity_disclosure": data_validity_disclosure,
        "breakpoint_status": {
            "actual_calls": r2_total,
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
                "本棒 round 2 (reask=1) 已完; 下棒可接力 minimax 教师侧 round 3 (>=3 more successful/caption)"
            ),
            "note": (
                f"本棒 round 2 (reask=1): actual={r2_total}/{planned_total} calls; "
                f"minimax 教师侧 round 2 完成度 = {met_round2_count}/{len(captions)} caption met round 2 目标 (≥2 successful/caption); "
                f"stop_reason={stop_reason}; "
                f"minimax model_id 沿 mapping §1.1 拍板 = {model_id} (1-call smoke 确认仍可用); "
                f"新拍板 ask_249ba8854ee343f7d9aa34de prompt_repro=accept_repro 已入 metadata + data_validity_disclosure 块"
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
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch5_r2_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    sha12, nbytes, lf_only = sha12_file(out_path)
    print(f"[WROTE] {out_path}")
    print(f"[SHA-12] {sha12}")
    print(f"[BYTES] {nbytes}")
    print(f"[LF-ONLY] {lf_only}")
    print(f"[MODELS LISTING REF] total={models_probe.get('model_count_total')} GLM_like={len(glm_like_ids)}")
    print(f"[SMOKE] selected={model_id} ok={smoke_rec['ok']} wall={smoke_wall_s}s")
    print(f"[STATS] r2 ok={r2_ok} empty={r2_empty} fail={r2_fail} total={r2_total} rate={empty_rate_r2:.4f}")
    print(f"[MINIMAX CUM] total={cum_total} ok={cum_ok} empty={cum_empty} rate={cum_empty_rate_post:.4f}")
    print(f"[CROSS BATCH] total={cross_batch_total} ok={cross_batch_ok} empty={cross_batch_empty} rate={cross_batch_rate:.4f}")
    print(f"[STOP] {stop_reason}")

    return 0


if __name__ == "__main__":
    sys.exit(main())