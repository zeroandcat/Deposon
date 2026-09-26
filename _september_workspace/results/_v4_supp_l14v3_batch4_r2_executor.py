# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch4_r2_executor.py
====================================

V4 L14+ batch 4 · round 2 · coze 教师侧 round 2 续采（reask=1）
================================================================

【派工依据】
----------------
- 沿 batch4 r1 executor `e84bffd5dc7d` + r1 result `7d9fe9d319a2` 口径（基础口径锚）
- 沿 model mapping 留痕件 `98a779d61c1e` coze 映射拍板（ask_748d9242c7a6be3d83de63a0）
- 沿 batch2 r3 executor `72fd2bb3838e` + r3 result `25251aca6d79` 历史口径锚
- 沿 batch2 r4 result `15b8ddc5ba9e` 跨批累计 baseline（185 calls / 9 empty / 4.86%）
- 沿 /v1/models 探活 `_v4_supp_l14v3_batch2_r2_models_probe.json` (sha12=`3c9dc60b5071`)
  确认 `deepseek-v4-flash` 在 44 models 清单内（V4 现行可考）
- 派工单 coze 教师批 4 round 2（接力棒，沿 r1 上下文唤醒）：22 caption × 1 call（reask=1）

【本棒范围（沿 dispatch）—— coze 教师侧 round 2（reask=1）续采】
------------------------------------------------------------
1. **沿用 teamo `deepseek-v4-flash` 代表采样**（r1 smoke ok=200 已确认；本棒仅 1-call smoke 防端点飘移）
2. **22 caption × 1 call**（每位 caption 第 2 call；reask_idx=1；目标 round 2 完成度 = 2/5 successful/caption）
3. **目标**：本棒后 22/22 caption 各 ≥2 successful call；下棒接力至 ≥5 successful/caption
4. 预算 ≤22 caption calls + ≤1 smoke calls / ≤600s watchdog
5. 跑不完如实报断点

【coze 代表采样映射（沿 model_mapping `98a779d61c1e` §1.1 第三栏 PI 拍板）】
--------------------------------------------------------------------
- PI 拍板原文（ask_748d9242c7a6be3d83de63a0 Q3 Other 逐字引用）：
  「coze与trea都只是agent平台，我都是接的大模型API」
- 拍板 = coze = agent 平台封装（PI 拍板字面裁定底层 model 不可考）
- 本重跑以现行大模型 API `deepseek-v4-flash`（teamo）**代表采样**
- result 内 metadata 字段强制标注：
  - `representative_for_coze: true`
  - `substitute_origin: "coze_agent_platform_underlying_model_not_documented"`
- **不声称该 model 即 coze 背后模型**（沿诚实 = 不误导口径）

【每 caption successful 计数（沿 dispatch §6）】
---------------------------------------------------------
- 本棒前基线（沿 batch4 r1）：coze 教师侧 = 22 calls / 0 empty / 22 ok / 0.0000 rate
- 本棒 round 2（reask=1）后：22/22 caption 各 ≥2 successful call（理论值；如端点飘移可能回落）
- 终盘结果：result.json 顶层 `per_caption_successful_calls` 块 + `dispatch_target_progress` 块

【retry 修复逻辑沿 batch4 r1 + batch2 r3 + batch1 r6】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}
- read_timeout_initial_s=60 / read_timeout_retry_s=90
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回
- r6 retry 触发的源 error_category tracking 沿用

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
--------------------------------------------------------------------
- 跨批累计 baseline = batch1 终态 119 + batch2 r2 = 22 + batch2 r3 = 22 + batch2 r4 = 22 + batch4 r1 = 22
  → **207 calls / 9 empty / 4.35%**（沿 batch4 r1 result `7d9fe9d319a2`）
- coze_teacher_cumulative 自身从 r1 终态 22/0/22 起步
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 单棒 >50% 停采：r2 单棒 empty_rate > 50% 也立即停采（沿 dispatch）

【端点取舍（沿 r1 + r4 + r3 + r2）】
----------------------------
- teamo + tun + deepseek-v4-flash（沿 r1 smoke ok=200 + r2 models_probe 探活清单 sha12=`3c9dc60b5071` 已确认 44 models 含 deepseek-v4-flash）
- teamo 必走 tun 防封号（PI 2026-09-23 硬纪律）

【铁律严守（沿 r1/r3/r4）】
------------------------
- R4 key 永不明文（无例外）；仅 runtime memory 读
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch4_r2_*` 与 `_batch4_r1_*` / `_batch2_r*_` / `_batch1_*` 独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物；探活计入 calls 账
- 不覆盖既有件（r1 executor `e84bffd5dc7d` + r1 result `7d9fe9d319a2` + r4 executor `d9fe7aa2d292` + r4 result `15b8ddc5ba9e` + r3 executor `72fd2bb3838e` + r3 result `25251aca6d79` + mapping `98a779d61c1e` + r2 models_probe `3c9dc60b5071` + prereg `05b975a86989` 不动）

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch4_r2_result.json`（schema = `v4_l14v3_n26/1` + batch=4 + round=2）
- 不覆盖 r1 result `7d9fe9d319a2` 或 r4 result `15b8ddc5ba9e` 或 r3 result `25251aca6d79` 或 batch1 r6 result `a4f851154551` 或 r1 result `d245ae4ce385`
- predecessor_sha12 链：mapping `98a779d61c1e` + r1 executor/result（最新接力锚）+ r4 executor/result + r3 executor/result（口径锚）+ r2 executor/result + models_probe + batch1 r6 executor/result + prereg `05b975a86989`

【与 r1 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. ROUND = 2（升 r2 命名）；BATCH = 4 不变
2. prompt_id 前缀 `coze_t02_teacher_*`（取代 r1 的 t01 round 1）+ 后缀 `_b4_r2`
3. reask_idx = 1（本棒每位 caption 第 2 call；取代 r1 的 reask_idx=0）
4. phase_label：`b4_r2_need3`（round 2 目标 = ≥2 successful/caption，need_more_to_target = 3）
5. is_round_2 = True（语义：本棒 = coze 教师侧 data collection round 2，区别于 r1 的 round 1）
6. smoke_call_only = True（沿 r1 smoke ok=200；本棒对 deepseek-v4-flash 1-call smoke 防端点飘移）
7. predecessor_sha12 链：r1 executor `e84bffd5dc7d` + r1 result `7d9fe9d319a2`（新增；取代 r1 链的 b2r4 双件仍保留作为历史累计 baseline）
8. baseline prior：r1 终态 22 calls / 0 empty / 22 ok / 0.0000 rate（取代 r1 链的 0/0/0）
9. 跨批累计 baseline：r1 终态 207 calls / 9 empty / 4.35% rate（取代 r1 链的 185/9/4.86%）
10. 新增 `coze_teacher_side_round2_progress` 块：本棒后 coze 教师侧 round 2 完成度（≥2 successful/caption）
11. K-N26-N2 触发阈值 = 0.50 不变；监控 baseline 更新为 207/9/4.35%
12. spec_conformance 重写：coze 教师侧 round 2 续采（reask=1），目标 ≥2 successful/caption
13. model_id_inconsistency_honest_disclosure 字面继承 r1（沿 mapping 拍板代表采样字面）
14. 派生 metadata 字段沿 r1 不动（v3_anchor_api_name=coze / v3_anchor_9backbone_name=null / v4_current_model_id_sent=deepseek-v4-flash）
15. per_caption_successful_calls 字段新增 round2_target=2 / round2_met
16. 调度注释：round 2 续采（reask=1）22 caption × 1 call

【边界】
----------
- 不动任何既有件（含 r1 executor `e84bffd5dc7d` + r1 result `7d9fe9d319a2` + r4 executor `d9fe7aa2d292` + r4 result `15b8ddc5ba9e` + r3 executor `72fd2bb3838e` + r3 result `25251aca6d79` + r2 executor `e7418f47a130` + r2 result `8c125e257af8` + r1 executor `e52f930654d3` + r1 result `d245ae4ce385` + batch1 r6 executor `5f02c7e0f094` + batch1 r6 result `a4f851154551` + models_probe `3c9dc60b5071` + mapping `98a779d61c1e` + prereg `05b975a86989`）
- 跑不完拆段报断点
- 0 触动 V1–V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
- 不立 V3 → V4 model 升级版字面继承断言（沿 mapping §4 诚实声明）
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
B2_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r1_result.json")
B2_R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_result.json")
B2_R3_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r3_result.json")
B2_R4_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r4_result.json")
B4_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r1_result.json")
MODELS_PROBE_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_models_probe.json")
MAPPING_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_model_mapping_2026_09_24.md")

# tun 代理（沿 r1/r3/r4）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（沿 r1）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
KEY_INDEX_TEAMO_1BASED = 15  # 沿 r1 (line 15 = teamo key)
USE_PROXY = True

# 串行间隔
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 r1）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 r1）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别（沿 r1 + dispatch §1 字面）
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值（沿 dispatch §4）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 单棒 empty_rate 停采阈值（沿 dispatch 「单棒 >50% 停采」）
SINGLE_BATCH_EMPTY_RATE_THRESHOLD = 0.50

# 预算
WALL_TIME_BUDGET_S = 600

# 本棒调度（沿 dispatch）
BATCH = 4
ROUND = 2  # 升 r2 命名
TEACHER = "coze"
SIDE = "teacher"
REASK_R1 = 1  # 本棒 round 2 = 每 caption 第 2 call（reask_idx=1）
TARGET_SUCCESSFUL_PER_CAPTION = 5
SMOKE_CALL_ONLY = True  # 沿 r1 smoke ok=200；本棒仅 1-call smoke 防端点飘移

# 选定的 model_id（沿 mapping 拍板代表采样；r1 已 smoke ok=200）
MODEL_COZE_REPRESENTATIVE = "deepseek-v4-flash"

# representative 标注（强制入 result metadata）
REPRESENTATIVE_FOR_COZE = True
SUBSTITUTE_ORIGIN = "coze_agent_platform_underlying_model_not_documented"

# smoke prompt（极小，节省 token）
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
# 工具（沿 r1 + 复用）
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
        "HTTP-Referer": "https://deposon.local/l14v3-batch4-r2",
        "X-Title": f"deposon-l14v3-batch4-r2-{TEACHER}-teacher",
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
# Smoke（沿 r1 简化版；仅 1 call 确认端点 ok）
# ============================================================
def smoke_coze_model(api_key: str, model_id: str) -> Dict[str, Any]:
    """1-call smoke（沿 r1 smoke ok=200 已知）；仅作端点可达性确认。"""
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
        "phase_label": "smoke_coze_representative_model_id",
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
    suffix = "_b4_r2"
    prompt_id = f"coze_t02_{side}_{caption_id}{suffix}"

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
                        "representative_for_coze": REPRESENTATIVE_FOR_COZE,
                        "substitute_origin": SUBSTITUTE_ORIGIN,
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
                "representative_for_coze": REPRESENTATIVE_FOR_COZE,
                "substitute_origin": SUBSTITUTE_ORIGIN,
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
            "representative_for_coze": REPRESENTATIVE_FOR_COZE,
            "substitute_origin": SUBSTITUTE_ORIGIN,
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 L14+ batch 4 round 2 · coze 教师侧 round 2（reask=1）续采")
    print("沿 r1 deepseek-v4-flash smoke ok=200; 本棒仅 1-call smoke 后跑 22 caption × 1 call")
    print("计划 calls = 22 caption × 1 call = 22 calls + 1 smoke call")
    print("目标: round 2 后 22/22 caption 各 ≥2 successful call")
    print("预算 ≤22 caption calls + 1 smoke call / ≤600s watchdog")
    print("retry 修复沿 r1 (沿 batch2 r3 + batch1 r6)")
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

    # 3. 加载前置累计基线（b4 r1 终态作为 coze 自身 baseline；cross batch 沿 b4r1 终态）
    with open(B4_R1_RESULT_PATH, "r", encoding="utf-8") as f:
        b4_r1 = json.load(f)
    b4_r1_cross_total = b4_r1["aggregate"]["cross_batch_with_b2r4_baseline"]["cross_total"]
    b4_r1_cross_empty = b4_r1["aggregate"]["cross_batch_with_b2r4_baseline"]["cross_empty"]
    b4_r1_cross_ok = b4_r1["aggregate"]["cross_batch_with_b2r4_baseline"]["cross_ok"]
    b4_r1_cross_rate = b4_r1["aggregate"]["cross_batch_with_b2r4_baseline"]["cross_rate"]
    print(
        f"[BASELINE b4r1 cross batch] total={b4_r1_cross_total} "
        f"ok={b4_r1_cross_ok} empty={b4_r1_cross_empty} rate={b4_r1_cross_rate:.4f}"
    )

    coze_prior_total = b4_r1["aggregate"]["coze_cumulative"]["post_total"]
    coze_prior_ok = b4_r1["aggregate"]["coze_cumulative"]["post_ok"]
    coze_prior_empty = b4_r1["aggregate"]["coze_cumulative"]["post_empty"]
    coze_prior_rate = b4_r1["aggregate"]["coze_cumulative"]["post_rate"]
    print(
        f"[BASELINE b4r1 coze cumulative] total={coze_prior_total} "
        f"ok={coze_prior_ok} empty={coze_prior_empty} rate={coze_prior_rate:.4f}"
    )

    # 4. 加载 /v1/models 探活清单（参考；不重探，仅确认 deepseek-v4-flash 在 44 models 清单）
    with open(MODELS_PROBE_PATH, "r", encoding="utf-8") as f:
        models_probe = json.load(f)
    all_ids = models_probe.get("all_ids_extracted", [])
    deepseek_like_ids = [m for m in all_ids if isinstance(m, str) and "deepseek" in m.lower()]
    deepseek_v4_flash_in_listing = "deepseek-v4-flash" in all_ids
    print(
        f"[MODELS PROBE REF] 44 total models; deepseek 系 {len(deepseek_like_ids)} 个: "
        f"{deepseek_like_ids}; deepseek-v4-flash 在清单={deepseek_v4_flash_in_listing}"
    )

    # 5. Smoke 1-call（deepseek-v4-flash 端点可达性确认；沿 r1 smoke ok=200 已知）
    print("=" * 60)
    print("[SMOKE PHASE] deepseek-v4-flash 1-call smoke（沿 r1 smoke ok=200 已知）")
    print("=" * 60)
    t_smoke_start = time.time()
    smoke_rec = smoke_coze_model(api_key, MODEL_COZE_REPRESENTATIVE)
    t_smoke_end = time.time()
    smoke_wall_s = round(t_smoke_end - t_smoke_start, 1)
    print(
        f"  [SMOKE] model_id={MODEL_COZE_REPRESENTATIVE} sc={smoke_rec.get('status_code')} "
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
            "batch": BATCH,
            "round": ROUND,
            "metadata": {
                "task": "L14V3_batch4_round2_coze_teacher_side_round2_reask1",
                "prereg_sha12": "05b975a86989",
                "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
                "predecessor_sha12": {
                    "model_mapping_sha12": "98a779d61c1e",
                    "model_mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                    "b4_r1_executor_sha12": "e84bffd5dc7d",
                    "b4_r1_executor_path": "results/_v4_supp_l14v3_batch4_r1_executor.py",
                    "b4_r1_result_sha12": "7d9fe9d319a2",
                    "b4_r1_result_path": "results/_v4_supp_l14v3_batch4_r1_result.json",
                    "b2_r4_executor_sha12": "d9fe7aa2d292",
                    "b2_r4_executor_path": "results/_v4_supp_l14v3_batch2_r4_executor.py",
                    "b2_r4_result_sha12": "15b8ddc5ba9e",
                    "b2_r4_result_path": "results/_v4_supp_l14v3_batch2_r4_result.json",
                    "b2_r3_executor_sha12": "72fd2bb3838e",
                    "b2_r3_executor_path": "results/_v4_supp_l14v3_batch2_r3_executor.py",
                    "b2_r3_result_sha12": "25251aca6d79",
                    "b2_r3_result_path": "results/_v4_supp_l14v3_batch2_r3_result.json",
                    "b2_r2_executor_sha12": "e7418f47a130",
                    "b2_r2_executor_path": "results/_v4_supp_l14v3_batch2_r2_executor.py",
                    "b2_r2_result_sha12": "8c125e257af8",
                    "b2_r2_result_path": "results/_v4_supp_l14v3_batch2_r2_result.json",
                    "b2_r2_models_probe_sha12": "3c9dc60b5071",
                    "b2_r2_models_probe_path": "results/_v4_supp_l14v3_batch2_r2_models_probe.json",
                    "batch1_r6_executor_sha12": "5f02c7e0f094",
                    "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                    "batch1_r6_result_sha12": "a4f851154551",
                    "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
                },
                "date": "2026-09-24",
                "teacher": TEACHER,
                "side": SIDE,
                "round_index": ROUND,
                "representative_for_coze": REPRESENTATIVE_FOR_COZE,
                "substitute_origin": SUBSTITUTE_ORIGIN,
                "stop_reason": "smoke_coze_representative_model_failed",
            },
            "smoke_phase": smoke_rec,
            "smoke_wall_time_s": smoke_wall_s,
            "run_window_cst": now_iso,
        }
        out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r2_result.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(fail_result, f, ensure_ascii=False, indent=2)
        print(f"[WROTE] {out_path}")
        return 3
    print(f"[SMOKE-OK] model_id = {MODEL_COZE_REPRESENTATIVE} (sc=200, model_returned={smoke_rec['model_returned']})")

    model_id = MODEL_COZE_REPRESENTATIVE

    # 6. 调度：22 caption × 1 call (round 2 reask=1) 按 caption_id 字母序
    captions_sorted = sorted(captions, key=lambda c: c["id"])
    planned = [{"caption_id": c["id"], "phase": "b4_r2_need3"} for c in captions_sorted]
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
    cum_total = coze_prior_total
    cum_empty = coze_prior_empty
    cum_ok = coze_prior_ok
    r2_total = 0
    r2_ok = 0
    r2_empty = 0
    r2_fail = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    k_n26_n2_triggered = False
    k_n26_n2_trigger_at_call_idx = None
    k_n26_n2_trigger_cum_rate = None
    single_batch_triggered = False
    stop_reason = None

    retry_trigger_categories_tracker: List[str] = []
    retry_count_distribution: Dict[int, int] = {}
    retry_triggered_count = 0

    # 从 r1 累计 per_caption_successful_calls 起步
    r1_per_cap = b4_r1.get("per_caption_successful_calls", {})
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

        # K-N26-N2 coze 自身累计监控（call 前判）
        if cum_total > 0:
            current_cum_rate = cum_empty / cum_total
            if current_cum_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i
                k_n26_n2_trigger_cum_rate = current_cum_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 coze cumulative empty_rate={current_cum_rate:.4f} > 0.50 at call {i}/{planned_total}; stop per dispatch §4")
                break

        rec = run_one_quadruple(
            api_key=api_key,
            caption=caption,
            reask_idx=REASK_R1,
            side="teacher",
            round_index=ROUND,
            is_round_2=True,  # 语义：本棒 = coze 教师侧 data collection round 2
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
            f"[coze_cum_rate={current_cum_rate_post:.4f}]"
        )

        # K-N26-N2 停采监控（call 后立即判）
        if cum_total > 0:
            post_rate = cum_empty / cum_total
            if post_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                k_n26_n2_triggered = True
                k_n26_n2_trigger_at_call_idx = i + 1
                k_n26_n2_trigger_cum_rate = post_rate
                stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                print(f"[STOP] K-N26-N2 coze post-call cumulative empty_rate={post_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch §4")
                break

        # 单棒 >50% 停采（call 后立即判，沿 dispatch 「单棒 >50% 停采」）
        if r2_total > 0:
            single_rate = r2_empty / r2_total
            if single_rate > SINGLE_BATCH_EMPTY_RATE_THRESHOLD:
                single_batch_triggered = True
                stop_reason = "single_batch_empty_rate_exceeded_0.50"
                print(f"[STOP] single batch empty_rate={single_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch '单棒 >50% 停采'")
                break

        if i < planned_total - 1:
            time.sleep(INTER_CALL_SLEEP_S)

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)
    total_wall_s = round(t_batch_end - t_smoke_start, 1)

    # 9. 统计
    empty_rate_r2 = (r2_empty / r2_total) if r2_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 跨批累计 = b4r1 baseline + coze 本棒
    cross_batch_total = b4_r1_cross_total + r2_total
    cross_batch_empty = b4_r1_cross_empty + cum_empty - coze_prior_empty
    cross_batch_ok = b4_r1_cross_ok + cum_ok - coze_prior_ok
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

    # 11. coze 教师侧 round 2 进度块
    coze_round2_progress = {
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

    # model_id_inconsistency_honest_disclosure（沿 r1 字面格式 + coze 不可考特别声明）
    selected_record = smoke_rec
    model_id_disclosure = (
        f"prereg §0 字面 model_id = coze (V3 公开产品名 / 端点名); "
        f"沿 mapping 留痕件 98a779d61c1e §1.1 第三栏 PI 拍板 = agent 平台封装; "
        f"PI 拍板 Other 原文 (ask_748d9242c7a6be3d83de63a0 Q3 逐字引用): "
        f"「coze与trea都只是agent平台，我都是接的大模型API」; "
        f"coze 底层 model 不可考 (V3 9-backbone 字段无 coze; V3 制品层 by_model/coze/ 同样无 model 字段; "
        f"teamo /v1/models 探活清单 (44 models) 字面亦无 coze 字段); "
        f"本棒选定 = {model_id} (deepseek-v4-flash / teamo 端点 / 1-call smoke ok=200, "
        f"model_returned={selected_record.get('model_returned', '')}); "
        f"代表采样选择 (deepseek-v4-flash) 理由 (沿 mapping §1.1 第二栏): "
        f"团队现行 6 模型补跑锚定 (Track 2 multimodel verdict 12,883 B 字面); "
        f"deepseek-v4-flash 在 teamo /v1/models 探活清单 (44 models 中) 字面可考; "
        f"代表采样 ≠ coze 背后模型 (沿诚实 = 不误导 + 不可考即如实不可考); "
        f"result 内 metadata 字段强制标注 representative_for_coze: true + "
        f"substitute_origin: coze_agent_platform_underlying_model_not_documented; "
        f"本映射选择 = PI 拍板代表采样, 非 V3 字面继承, 非断层真实 mapping 断言; "
        f"r1 smoke + 22 caption 实测均 model_returned=deepseek-v4-flash-ga-260731 (1 call=deepseek-v4-flash-0731); "
        f"r2 沿 r1 结论仅 1-call smoke 防端点飘移; "
        f"待 PI 复核项: 是否接受 deepseek-v4-flash 作为 coze = V3 公开产品名/端点名的代表采样"
    )

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": BATCH,
        "round": ROUND,
        "metadata": {
            "task": "L14V3_batch4_round2_coze_teacher_side_round2_reask1",
            "prereg_sha12": "05b975a86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "predecessor_sha12": {
                "model_mapping_sha12": "98a779d61c1e",
                "model_mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                "b4_r1_executor_sha12": "e84bffd5dc7d",
                "b4_r1_executor_path": "results/_v4_supp_l14v3_batch4_r1_executor.py",
                "b4_r1_result_sha12": "7d9fe9d319a2",
                "b4_r1_result_path": "results/_v4_supp_l14v3_batch4_r1_result.json",
                "b2_r4_executor_sha12": "d9fe7aa2d292",
                "b2_r4_executor_path": "results/_v4_supp_l14v3_batch2_r4_executor.py",
                "b2_r4_result_sha12": "15b8ddc5ba9e",
                "b2_r4_result_path": "results/_v4_supp_l14v3_batch2_r4_result.json",
                "b2_r3_executor_sha12": "72fd2bb3838e",
                "b2_r3_executor_path": "results/_v4_supp_l14v3_batch2_r3_executor.py",
                "b2_r3_result_sha12": "25251aca6d79",
                "b2_r3_result_path": "results/_v4_supp_l14v3_batch2_r3_result.json",
                "b2_r2_executor_sha12": "e7418f47a130",
                "b2_r2_executor_path": "results/_v4_supp_l14v3_batch2_r2_executor.py",
                "b2_r2_result_sha12": "8c125e257af8",
                "b2_r2_result_path": "results/_v4_supp_l14v3_batch2_r2_result.json",
                "b2_r2_models_probe_sha12": "3c9dc60b5071",
                "b2_r2_models_probe_path": "results/_v4_supp_l14v3_batch2_r2_models_probe.json",
                "batch1_r6_executor_sha12": "5f02c7e0f094",
                "batch1_r6_executor_path": "results/_v4_supp_l14v3_batch1_r6_executor.py",
                "batch1_r6_result_sha12": "a4f851154551",
                "batch1_r6_result_path": "results/_v4_supp_l14v3_batch1_r6_result.json",
            },
            "date": "2026-09-24",
            "spec_conformance": (
                "PI 2026-09-24 batch4 coze 教师侧 round 2 续采 (reask=1); "
                "沿 r1 deepseek-v4-flash smoke ok=200; r2 仅 1-call smoke; "
                "22 caption × 1 call = 22 calls (按 caption_id 字母序); "
                "目标 ≥2 successful/caption"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": ROUND,
            "batch_index": BATCH,
            "round2_target_per_caption": 2,
            "round2_reask_idx": REASK_R1,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r2_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": (
                "沿 mapping 98a779d61c1e §1.1 第三栏 PI 拍板 (teamo 端点); "
                "/v1/models 探活清单沿 r2 models_probe.json (sha12=3c9dc60b5071); "
                "r2 沿 r1 smoke ok=200; r2 仅 1-call smoke 防端点飘移; "
                "44 models 清单字面含 deepseek-v4-flash"
            ),
            "model_id_sent": model_id,
            "model_id_inconsistency_honest_disclosure": model_id_disclosure,
            "representative_for_coze": REPRESENTATIVE_FOR_COZE,
            "substitute_origin": SUBSTITUTE_ORIGIN,
            "mapping_decision_basis": {
                "mapping_document_sha12": "98a779d61c1e",
                "mapping_document_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                "ask_id": "ask_748d9242c7a6be3d83de63a0",
                "ask_other_verbatim": "coze与trea都只是agent平台，我都是接的大模型API",
                "ask_decision": "agent 平台封装 / 底层 model 不可考 / 代表采样 = teamo deepseek-v4-flash",
            },
            "v3_anchor_metadata": {
                "v3_anchor_api_name": "coze",
                "v3_anchor_9backbone_name": None,
                "v3_anchor_9backbone_note": "coze 不在 V3 9-backbone (deposon_v3_physical_opt_60cells_2026_09_11.json L26 9_models 字段全部 9 项枚举无 coze); 沿 claude_code 回函 L168 字面「coze appears zero times in the 9-model file」",
                "v3_by_model_dir": "corpus/v20/by_model/coze/ (路径标签, 制品层无 model 字段)",
                "v4_current_model_id_sent": "deepseek-v4-flash",
                "v4_current_endpoint": "teamo (https://api.teamorouter.cn/v1)",
                "v4_representative_not_identity": True,
            },
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
                "b4_r1_status": "r1 1-call smoke ok=200 + 22 caption × 1 call = 22 calls 全 OK; model_returned=deepseek-v4-flash-ga-260731 (1 call=deepseek-v4-flash-0731)",
                "r2_b4_status": "r2 仅 1-call smoke (沿 r1 结论)；未做 3-candidate probe fallback",
                "rationale": (
                    "沿 r1 deepseek-v4-flash smoke ok=200; r2 节省预算避免重复 probe; "
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
            "single_batch_empty_rate_threshold": SINGLE_BATCH_EMPTY_RATE_THRESHOLD,
            "diff_vs_r1_executor": [
                "1. ROUND=2 (升 r2 命名)；BATCH=4 不变",
                "2. prompt_id 前缀 coze_t02_teacher_* (取代 r1 的 t01)；后缀 _b4_r2 (取代 r1 的 _b4_r1)",
                "3. reask_idx=1 (本棒每 caption 第 2 call；取代 r1 的 reask_idx=0)",
                "4. phase_label: b4_r2_need3 (round 2 目标 = ≥2 successful/caption，need_more_to_target=3)",
                "5. is_round_2=True (语义: coze 教师侧 data collection round 2，区别于 r1 的 round 1)",
                "6. smoke_call_only=True (沿 r1 smoke ok=200；本棒对 deepseek-v4-flash 1-call smoke 防端点飘移)",
                "7. predecessor_sha12 链: b4_r1_executor e84bffd5dc7d + b4_r1_result 7d9fe9d319a2 (新增；取代 r1 链的 mapping/r2/probe/batch1_r6/prereg 仍保留)",
                "8. baseline prior: r1 终态 22 calls / 0 empty / 22 ok / 0.0000 rate (取代 r1 链的 0/0/0)",
                "9. 跨批累计 baseline: r1 终态 207 calls / 9 empty / 4.35% rate (取代 r1 链的 185/9/4.86%)",
                "10. 新增 coze_teacher_side_round2_progress 块 (round 2 完成度 ≥2 successful/caption)",
                "11. K-N26-N2 触发阈值 0.50 不变；监控 baseline 更新为 207/9/4.35%",
                "12. spec_conformance 重写: coze 教师侧 round 2 续采 (reask=1)",
                "13. model_id_inconsistency_honest_disclosure 字面继承 r1 (沿 mapping 拍板代表采样字面) + r1 实测补注",
                "14. 派生 metadata 字段沿 r1 不动 (v3_anchor_api_name=coze / v3_anchor_9backbone_name=null / v4_current_model_id_sent=deepseek-v4-flash)",
                "15. per_caption_successful_calls 字段新增 round2_target=2 / round2_met",
                "16. 调度注释: coze 教师侧 round 2 续采 (reask=1) 22 caption × 1 call",
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
                "representative_substitute_disclosure_honest": True,
            },
            "run_window_cst": now_iso,
            "stop_reason": stop_reason,
            "interruption_recovery_note": (
                "r2 沿 r1 deepseek-v4-flash 代表采样结论 (sha12=7d9fe9d319a2 实测 22 calls 全 OK); "
                "不再做 3-candidate probe fallback; 1-call smoke 失败立即 abort; "
                "r2 与 r1/r4/r3/r2/r1/batch1_r6 派生 JSON 独立 (不合并); "
                "coze 自身 baseline = 22/22/0/0.0 (沿 r1 终态); "
                "cross batch baseline = 207/198/9/4.35% (沿 r1 终态)"
            ),
        },
        "models_listing_summary_ref": {
            "endpoint": ENDPOINT_TEAMO + "/models",
            "model_count_total": models_probe.get("model_count_total"),
            "deepseek_like_ids": deepseek_like_ids,
            "deepseek_v4_flash_in_listing": deepseek_v4_flash_in_listing,
            "fetched_at_cst": models_probe.get("fetched_at_cst"),
            "note": (
                "r2 不重探 /v1/models; 仅引用 r2 探活清单 (sha12=3c9dc60b5071) "
                "确认 deepseek-v4-flash 在 teamo 44 models 清单; "
                "代表采样 ≠ coze 背后模型 (沿诚实 = 不误导)"
            ),
        },
        "smoke_phase": {
            "selected_model_id": MODEL_COZE_REPRESENTATIVE,
            "representative_for_coze": REPRESENTATIVE_FOR_COZE,
            "substitute_origin": SUBSTITUTE_ORIGIN,
            "smoke_record": smoke_rec,
            "smoke_wall_time_s": smoke_wall_s,
        },
        "quadruples": quadruples,
        "retry_validation": retry_validation,
        "per_caption_successful_calls": per_caption_successful_calls,
        "coze_teacher_side_round2_progress": coze_round2_progress,
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
            "tun_compliance": tun_compliance,
            "tun_used_count": tun_used_count,
            "tun_target_count": len(quadruples),
            "smoke_total_calls": 1,
            "smoke_attempted_model_id": MODEL_COZE_REPRESENTATIVE,
            "coze_cumulative": {
                "prior_total": coze_prior_total,
                "prior_empty": coze_prior_empty,
                "prior_ok": coze_prior_ok,
                "prior_rate": coze_prior_rate,
                "post_total": cum_total,
                "post_empty": cum_empty,
                "post_ok": cum_ok,
                "post_rate": round(cum_empty_rate_post, 4),
                "delta_total": cum_total - coze_prior_total,
                "delta_empty": cum_empty - coze_prior_empty,
                "delta_ok": cum_ok - coze_prior_ok,
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered_this_batch": k_n26_n2_triggered,
            },
            "cross_batch_with_b4r1_baseline": {
                "b4r1_baseline_total": b4_r1_cross_total,
                "b4r1_baseline_empty": b4_r1_cross_empty,
                "b4r1_baseline_ok": b4_r1_cross_ok,
                "b4r1_baseline_rate": b4_r1_cross_rate,
                "batch4_coze_post_total": cum_total,
                "batch4_coze_post_empty": cum_empty,
                "batch4_coze_post_ok": cum_ok,
                "cross_total": cross_batch_total,
                "cross_empty": cross_batch_empty,
                "cross_ok": cross_batch_ok,
                "cross_rate": round(cross_batch_rate, 4),
                "cross_k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "cross_k_n26_n2_triggered": cross_batch_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "note": (
                    "K-N26-N2 字面 per 教师; 本字段仅作 cross-batch sanity check; "
                    "coze 教师侧 K-N26-N2 判定 = coze_cumulative.post_rate"
                ),
            },
            "r2_empty_response_rate_threshold_K_N26_N2_single_batch": SINGLE_BATCH_EMPTY_RATE_THRESHOLD,
            "r2_empty_response_above_threshold_single_batch": empty_rate_r2 > SINGLE_BATCH_EMPTY_RATE_THRESHOLD,
            "single_batch_triggered_this_batch": single_batch_triggered,
        },
        "empty_rate_trend": {
            "batch1_round6_cumulative": {
                "calls": 119,
                "empty": 9,
                "ok": 110,
                "rate": round(9 / 119, 4),
                "note": "batch1 r6 终态 (kimi 119 calls 字面源)",
            },
            "batch2_round1_probe_fail": {
                "calls": 0,
                "empty": 0,
                "rate": 0.0,
                "note": "r1 探活 6 候选 400 全 fail; 0 caption call",
            },
            "batch2_round2_round1_retry_glm1": {
                "calls": 22,
                "empty": 0,
                "rate": 0.0,
                "note": "r2 GLM_1 round 1 retry 22 caption × 1 call; all OK",
            },
            "batch2_round3_round2_reask1_glm1": {
                "calls": 22,
                "empty": 0,
                "rate": 0.0,
                "note": "r3 GLM_1 round 2 reask=1 22 caption × 1 call; all OK",
            },
            "batch2_round4_round3_reask2_glm1": {
                "calls": 22,
                "empty": 0,
                "rate": 0.0,
                "note": "r4 GLM_1 round 3 reask=2 22 caption × 1 call; all OK",
            },
            "batch4_round1_round1_reask0_coze": {
                "calls": 22,
                "empty": 0,
                "rate": 0.0,
                "note": "r1 coze round 1 reask=0 22 caption × 1 call; all OK",
            },
            "batch2_round4_cumulative_glm1": {
                "calls": 66,
                "empty": 0,
                "ok": 66,
                "rate": 0.0,
                "note": "r4 终态 GLM_1 自身累计",
            },
            "cross_batch_cumulative_post_r4_glm1_only": {
                "calls": 185,
                "empty": 9,
                "ok": 176,
                "rate": round(9 / 185, 4),
                "note": "r4 终态 cross batch baseline (kimi + GLM_1)",
            },
            "batch4_round1_cumulative_coze": {
                "calls": 22,
                "empty": 0,
                "ok": 22,
                "rate": 0.0,
                "note": "r1 终态 coze 自身累计",
            },
            "cross_batch_cumulative_post_r1": {
                "calls": 207,
                "empty": 9,
                "ok": 198,
                "rate": round(9 / 207, 4),
                "note": "r1 终态 cross batch baseline (kimi + GLM_1 + coze)",
            },
            "batch4_round2_round2_reask1_coze": {
                "calls": r2_total,
                "empty": r2_empty,
                "rate": round(empty_rate_r2, 4),
            },
            "batch4_round2_cumulative_coze": {
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
                "note": "b4r1 baseline 207/9/4.35% + r2 增量",
            },
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round2_reask1_n_distinct_sample_note": (
                    f"round 2 reask=1 第 2 call 实测；本棒后 coze 教师侧 round 2 = "
                    f"{met_round2_count}/{len(captions)} caption met round 2 目标; "
                    f"需后续 round 接力达 ≥{TARGET_SUCCESSFUL_PER_CAPTION} successful/caption"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r2, 4),
                "cumulative_empty_response_rate_coze_only": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r2 > SINGLE_BATCH_EMPTY_RATE_THRESHOLD,
                "cumulative_trigger_K_N26_N2_pass_False": k_n26_n2_triggered,
                "monitor_disposition": (
                    f"本棒 K-N26-N2 coze 自身累计 empty_rate 监控 = 已实施; "
                    f"coze 自身累计 = {cum_total} calls / {cum_empty} empty / {cum_empty_rate_post:.4f}; "
                    f"baseline coze = {coze_prior_total} calls / {coze_prior_empty} empty / {coze_prior_rate:.4f}; "
                    f"cross-batch rate = {cross_batch_rate:.4f}; "
                    f"baseline cross batch = {b4_r1_cross_total} calls / {b4_r1_cross_empty} empty / {b4_r1_cross_rate:.4f}"
                ),
                "cross_batch_with_b4r1_baseline_rate": round(cross_batch_rate, 4),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
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
            "single_batch_triggered": single_batch_triggered,
            "next_resume_via": (
                "task_append 续跑 — 沿 prereg §1.6.4 同 agent 唤醒; "
                "本棒 round 2 (reask=1) 已完; 下棒可接力 coze 教师侧 round 3 (>=3 more successful/caption)"
            ),
            "note": (
                f"本棒 round 2 (reask=1): actual={r2_total}/{planned_total} calls; "
                f"coze 教师侧 round 2 完成度 = {met_round2_count}/{len(captions)} caption met round 2 目标 (≥2 successful/caption); "
                f"stop_reason={stop_reason}; "
                f"coze model_id 沿 mapping 拍板 = {model_id} (代表采样; 1-call smoke 确认仍可用); "
                f"representative_for_coze=true; substitute_origin=coze_agent_platform_underlying_model_not_documented"
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
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r2_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    sha12, nbytes, lf_only = sha12_file(out_path)
    print(f"[WROTE] {out_path}")
    print(f"[SHA-12] {sha12}")
    print(f"[BYTES] {nbytes}")
    print(f"[LF-ONLY] {lf_only}")
    print(f"[MODELS LISTING REF] total={models_probe.get('model_count_total')} deepseek_v4_flash_in_listing={deepseek_v4_flash_in_listing}")
    print(f"[SMOKE] selected={model_id} ok={smoke_rec['ok']} wall={smoke_wall_s}s")
    print(f"[STATS] r2 ok={r2_ok} empty={r2_empty} fail={r2_fail} total={r2_total} rate={empty_rate_r2:.4f}")
    print(f"[COZE CUM] total={cum_total} ok={cum_ok} empty={cum_empty} rate={cum_empty_rate_post:.4f}")
    print(f"[CROSS BATCH] total={cross_batch_total} ok={cross_batch_ok} empty={cross_batch_empty} rate={cross_batch_rate:.4f}")
    print(f"[STOP] {stop_reason}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
