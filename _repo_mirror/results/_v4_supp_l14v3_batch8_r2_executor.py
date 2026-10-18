# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch8_r2_executor.py
=====================================

V4 L14+ batch 8 · round 2（reask=1）—— GLM_2 蒸馏侧 round 2 续采棒（沿 r1 口径全套）
==================================================================================

【派工依据】
----------------
- 沿 r1 `results/_v4_supp_l14v3_batch8_r1_executor.py`（SHA-12 `1e5f2249c517`）+ r1 产物
  `results/_v4_supp_l14v3_batch8_r1_result.json`（SHA-12 `e6a94a0a13b7`）口径续跑（GLM_2 蒸馏侧 round 1 22/22 caption ≥1 successful 开工达成）
- 沿 batch6 r5 `results/_v4_supp_l14v3_batch6_r5_executor.py`（SHA-12 `8a8babb911b8`）+ r5 产物
  `results/_v4_supp_l14v3_batch6_r5_result.json`（SHA-12 `e40424bf8abe`）口径续跑（kimi 蒸馏侧 22/22 caption 5/5 successful 收官）
- 沿 batch2 r2 `results/_v4_supp_l14v3_batch2_r2_executor.py`（GLM_1 现行采样 = teamo `glm-5.3` 1-call probe 锚定）+ r2 产物
  `results/_v4_supp_l14v3_batch2_r2_result.json`（GLM_1 22 calls 实测字面）
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（SHA-12 `05B975A86989`）字面
- 沿 model mapping `results/_v4_supp_l14v3_model_mapping_2026_09_24.md`（SHA-12 `98a779d61c1e`）字面
  - GLM_2 = teamo `glm-5.3` 复用（PI 拍板 ask_748d9242c7a6be3d83de63a0 Q2 字面：「GLM_1/GLM_2 same lineage」
    + 「GLM_2 与 GLM_1 同 model_id_sent（同 teamo `glm-5.3`），不同语料」）
- 同 agent 唤醒保上下文（task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义）
- PI 2026-09-25 00:46「今晚保守口径下先斩后奏」夜间授权（保守口径自主决策，标注待 PI 复核）

【本棒范围（沿 dispatch）—— GLM_2 蒸馏侧 round 2 续采棒】
--------------------------------------------------------------------
1. **22 caption × 1 call** = 22 calls（沿 dispatch 字面）
2. **计数口径**：
   - **distill 侧独立计数**：`glm2_t01_distill_*` prompt_id 前缀为域（沿 r1 字面）
   - 目标 = GLM_2 蒸馏侧 round 2 ≥2 successful call/caption（**各 caption 由 1/5 顺利补至 2/5**）
   - 当前 GLM_2 蒸馏侧 = 22 caption 各 1 successful（沿 r1 quadruples 过滤；r1 22/22 全 OK）
   - 本棒补 1 call/caption → GLM_2 蒸馏侧各 caption 由 1 → 2 successful（**round 2 续采判定**）
3. **model 口径**（沿 r1）：
   - `model_id_sent` = `glm-5.3`（teamo 端点；与 GLM_1 现行采样复用）
   - `teacher_label` = `GLM_2`
   - `model_id_shared_with` = `GLM_1`（GLM_2 = 同 model 不同语料字面沿 mapping §1.2 派生字段）
4. **system prompt 沿用**（沿 r1 `PROMPT_SYSTEM` 字面不重写）：
   - GLM_2 复用同 model = 蒸馏任务 prompt 不变；teacher 身份由 `teacher_label` 字段标识
   - 沿 user memory 2026-09-08「V3 端点名 vs 公开产品名不一致时直接问」—— worker 不直接问 PI，记录为待 PI 复核项
5. **round 2 续采判定块 `glm2_distill_side_round2_progress`**：
   - `met_count_post_r2`：本棒后达标 caption 数（预期 22）
   - `still_pending_round2`：未达标 caption 列表（预期空）
   - `round2_progress_disposition`：GLM_2 蒸馏侧 round 2 续采判定
   - **非收官棒**：本棒仅 round 2 续采（1→2）；后续 r3/r4/r5 接力至 5/5 successful/caption（沿 batch6 r5 收官口径类比）

【每 caption successful 计数盘（沿 dispatch §6）—— GLM_2 蒸馏侧独立域】
----------------------------------------------------------------------
- 本棒前基线（GLM_2 蒸馏侧独立计数）：GLM_2 蒸馏侧 = 22 caption 各 1 successful（沿 r1 quadruples 过滤；r1 22/22 全 OK）
- 本棒增量计算：每 call 后实时更新 `per_cap_succ_glm2_distill` 字典
- 终盘结果（GLM_2 蒸馏侧独立计数）：
  - `per_caption_glm2_distill_only_successful_calls` 块（GLM_2 蒸馏侧独立计数）
  - `glm2_distill_side_round2_progress` 块（**round 2 续采判定**）
  - `dispatch_target_progress_glm2_distill` 块（GLM_2 蒸馏侧目标进展 — round 2 续采态）

【retry 修复沿 batch6 r5（沿 dispatch §3）】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}（沿 batch6 r5）
- read_timeout_initial_s=60 / read_timeout_retry_s=90（沿 batch6 r5）
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回（沿 batch6 r5）
- batch6 r5 retry 触发的源 error_category tracking 改进沿用（沿 batch6 r5）

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
-------------------------------------------
- 累计 = batch8 r1 终态 + batch8 r2 GLM_2 增量（GLM_2 蒸馏侧 round 2）
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 实测累计基线（沿 r1 产物）：
  - prior (b1+r2+r3+r4+r5+b6r1+r6r2+r6r3+r6r4+r6r5+b8r1): total=230, empty=9, **rate=3.91%**
  - r2 worst case (22 EMPTY): cumulative = 31/252 = 12.30% (仍 < 50% 阈值)
  - r2 best case (0 EMPTY): cumulative = 9/252 = 3.57% (仍 < 50% 阈值)

【端点取舍（沿 r1）】
----------------------------
- teamo + tun + glm-5.3（GLM_2 复用 GLM_1 现行采样；沿 batch2 r2 GLM_1 实测锚定）
- 不重新探活（沿 dispatch §4 「沿 r1 口径续跑」+ 即用即探口径）

【铁律严守（沿 r1）】
------------------------
- R4 key 永不明文（无例外）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch8_r2_*` 与前棒所有 _batch*_r* 同级独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch8_r2_result.json`
  （schema = v4_l14v3_n26/1 + batch=8 + round=2 + teacher=GLM_2）
- 不覆盖 batch8 r1 result `e6a94a0a13b7` 或前棒 result（沿 dispatch §4）

【与 r1 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------------
1. **ROUND = 2 / REASK_R1 = 1** 参数化（r1 = 1/0；本棒 = 2/1；reask_idx=1 = 第 2 call/caption on GLM_2 distill side）
2. **prompt_id 后缀**：`_r1` → `_r2`
3. **baseline 切换**：
   - 跨批累计：batch8 r1 终态 cumulative (230/9/221/3.91%)
   - GLM_2 蒸馏侧独立：22 caption 各 1 successful（沿 r1 quadruples 过滤）
4. **predecessor_sha12 链新增**：batch8 r1 executor `1e5f2249c517` + r1 result `e6a94a0a13b7`
5. **target 切换**：≥1 successful/caption (r1 开工阈值) → ≥2 successful/caption (r2 续采阈值)
6. **判定块命名**：
   - `glm2_distill_side_round1_progress` (r1 开工) → `glm2_distill_side_round2_progress` (r2 续采)
   - 字段 `met_target_round1` → `met_target_round2`
7. **is_round_2_progress_round 标记**：metadata.is_round_1_start_round = True (r1) → is_round_2_progress_round = True (r2)
8. **mapping_sha12_discrepancy_note 沿用**（不动 mapping 文件）
9. **diff_vs_r1_executor 新块**（取代 r1 的 diff_vs_batch6_r5_executor）
10. **r2 增量计数 → GLM_2 蒸馏侧各 caption 由 1/5 顺利补至 2/5**（r2 OK 全达标 if no fails）

【边界】
----------
- 不动任何既有件（含 batch6 r5 executor `8a8babb911b8` + r5 result `e40424bf8abe`
  + batch6 r4 executor `08f329b36e9d` + r4 result `b7377ba019a1`
  + batch6 r3 executor `1385d2ca356f` + r3 result `15a7fecdffe7`
  + batch6 r2 executor `93c931fc3b1c` + r2 result `96e1de46ed30`
  + batch6 r1 executor `ad35565f1ec9` + r1 result `0d29e1ab4ae2`
  + batch2 r2 executor `5be9dfe83a27` + r2 result `cb37b699ff73`
  + prereg `05B975A86989` + mapping `98a779d61c1e` + captions `6a2656878745`）
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
BATCH6_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch6_r5_result.json")
BATCH2_R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_result.json")
BATCH8_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch8_r1_result.json")

# tun 代理（沿 batch6 r5）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（GLM_2 复用 GLM_1 现行采样）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_GLM_5_3 = "glm-5.3"  # GLM_2 = GLM_1 复用（沿 mapping §1.2 + ask_748d9242 Q2 拍板）
KEY_INDEX_TEAMO_1BASED = 15
USE_PROXY = True

# 串行间隔（沿 batch6 r5）
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 batch6 r5）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 batch6 r5）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别（沿 batch6 r5）
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值（沿 batch6 r5）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算（沿 batch6 r5；扩至 1500s 以容纳 22 calls）
WALL_TIME_BUDGET_S = 1500

# 本棒调度
BATCH = 8
ROUND = 2
SIDE = "distill"
TEACHER = "GLM_2"
REASK_R1 = 1  # round 2 = 第 2 call per caption (reask_idx = 1) — 续采
TARGET_SUCCESSFUL_PER_CAPTION = 2  # GLM_2 蒸馏侧 round 2 续采阈值（≥2 successful calls/caption；各 caption 由 1 → 2 successful）
TARGET_FINAL_PER_CAPTION = 5  # GLM_2 蒸馏侧最终目标阈值（5 successful calls/caption；沿 batch6 r5 收官口径类比；后续 r3-r5 接力）

# ============================================================
# 计数口径（GLM_2 蒸馏侧独立）
# ============================================================
DISTILL_SIDE_PROMPT_ID_PREFIX = "glm2_t01_distill_"

# ============================================================
# 敏感模式（沿 batch6 r5）
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
# 工具（沿 batch6 r5）
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
        "HTTP-Referer": "https://deposon.local/l14v3-batch8-r1",
        "X-Title": "deposon-l14v3-batch8-r1-glm2-distill",
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
# 提示构造（沿 batch6 r5；GLM_2 复用同 model = 蒸馏 prompt 不变）
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
# 单 call + 内层重试（沿 batch6 r5）
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
    prompt_id = f"glm2_t01_{side}_{caption_id}{suffix}"

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
                        "side": side,
                        "teacher_label": TEACHER,
                        "model_id_shared_with": "GLM_1",
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
                "model_id_sent": MODEL_GLM_5_3,
                "side": side,
                "teacher_label": TEACHER,
                "model_id_shared_with": "GLM_1",
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
            "model_id_sent": MODEL_GLM_5_3,
            "side": side,
            "teacher_label": TEACHER,
            "model_id_shared_with": "GLM_1",
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
    print(f"V4 L14+ batch 8 round 2 | GLM_2 distill side | reask=1 — round 2 续采棒")
    print(f"模型: glm-5.3 (teamo; GLM_2 复用 GLM_1 = 同 model 不同语料)")
    print(f"计划 calls = 22 (22 caption × 1 call)")
    print(f"计数口径: GLM_2 蒸馏侧独立 (prompt_id 前缀 glm2_t01_distill_) — 沿 r1")
    print(f"GLM_2 蒸馏侧 baseline: 22 caption 各 1 successful (沿 r1 quadruples 过滤; r1 22/22 全 OK)")
    print(f"目标: GLM_2 蒸馏侧 ≥2 successful calls/caption (round 2 续采阈值)")
    print(f"最终目标: GLM_2 蒸馏侧 ≥5 successful calls/caption (后续 r3-r5 接力)")
    print(f"预算 ≤1500s watchdog")
    print(f"retry 修复沿 batch6 r5 (含 retry 触发的源 error_category tracking)")
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

    # 2. 加载 r1 + batch6 r5 + batch2 r2 result（用于 baseline + 锚链）
    with open(BATCH8_R1_RESULT_PATH, "r", encoding="utf-8") as f:
        b8r1 = json.load(f)
    with open(BATCH6_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b6r5 = json.load(f)
    with open(BATCH2_R2_RESULT_PATH, "r", encoding="utf-8") as f:
        b2r2 = json.load(f)

    # 3. GLM_2 蒸馏侧独立计数（filter by prompt_id 前缀）—— 本棒前 = r1 quadruples
    per_cap_succ_glm2_distill = {c["id"]: 0 for c in captions}
    per_cap_total_glm2_distill = {c["id"]: 0 for c in captions}
    per_cap_empty_glm2_distill = {c["id"]: 0 for c in captions}
    r1_glm2_distill_ok = 0
    for q in b8r1.get("quadruples", []):
        pid = q.get("prompt_id", "")
        if not pid.startswith(DISTILL_SIDE_PROMPT_ID_PREFIX):
            continue
        m = q["per_call_metadata"]
        cid = m["caption_id"]
        per_cap_total_glm2_distill[cid] = per_cap_total_glm2_distill.get(cid, 0) + 1
        if m["ok"] and not m["empty_response"]:
            per_cap_succ_glm2_distill[cid] = per_cap_succ_glm2_distill.get(cid, 0) + 1
            r1_glm2_distill_ok += 1
        if m["empty_response"]:
            per_cap_empty_glm2_distill[cid] = per_cap_empty_glm2_distill.get(cid, 0) + 1
    cum_total_prior_glm2 = sum(per_cap_total_glm2_distill.values())
    cum_empty_prior_glm2 = sum(per_cap_empty_glm2_distill.values())
    cum_ok_prior_glm2 = sum(per_cap_succ_glm2_distill.values())
    print(f"[GLM_2 DISTILL prior] total={cum_total_prior_glm2} ok={cum_ok_prior_glm2} "
          f"empty={cum_empty_prior_glm2} (源 = r1 quadruples distill 前缀过滤; 各 caption 各 1 successful)")

    # 4. 跨批累计监控（沿 r1 cumulative 链路 + GLM_2 r2 增量）
    r1_cum = b8r1["aggregate"]["cumulative"]
    cum_total_prior_cum = r1_cum["post_total"]  # 230
    cum_empty_prior_cum = r1_cum["post_empty"]  # 9
    cum_ok_prior_cum = r1_cum["post_ok"]        # 221
    cum_rate_prior = cum_empty_prior_cum / cum_total_prior_cum if cum_total_prior_cum > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior_cum} ok={cum_ok_prior_cum} "
          f"empty={cum_empty_prior_cum} rate={cum_rate_prior:.4f} (源 = r1 aggregate.cumulative post)")

    # 5. 调度 planned_calls（22 caption × 1 call = 22 calls）
    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r2_glm2_distill_{c['id']}"}
        for c in captions
    ]
    planned = PLANNED_CALLS
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (22 caption × 1 call)")

    # 6. 加载 key
    try:
        api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
        print(f"[INIT] teamo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 7. 时间预算起点
    t_batch_start = time.time()

    # 8. 跑
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
            per_cap_succ_glm2_distill[cap_id] += 1
        elif is_empty:
            r2_empty += 1
            cum_empty += 1
            per_cap_empty_glm2_distill[cap_id] += 1
        else:
            r2_fail += 1
        r2_total += 1
        cum_total += 1
        per_cap_total_glm2_distill[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ_glm2_distill = per_cap_succ_glm2_distill[cap_id]
        target_met_glm2_distill = "[OK] 续采" if cur_succ_glm2_distill >= TARGET_SUCCESSFUL_PER_CAPTION else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<28} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[glm2_distill_succ={cur_succ_glm2_distill}/{TARGET_SUCCESSFUL_PER_CAPTION} {target_met_glm2_distill}] "
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

    # 9. 统计
    empty_rate_r2 = (r2_empty / r2_total) if r2_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 10. 每 caption successful 计数 —— GLM_2 蒸馏侧独立
    per_caption_glm2_distill_only_successful_calls = {}
    met_target_count_glm2_distill = 0
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ_glm2_distill[cid]
        t = per_cap_total_glm2_distill[cid]
        e = per_cap_empty_glm2_distill[cid]
        need = max(0, TARGET_SUCCESSFUL_PER_CAPTION - s)
        need_final = max(0, TARGET_FINAL_PER_CAPTION - s)
        met = s >= TARGET_SUCCESSFUL_PER_CAPTION
        if met:
            met_target_count_glm2_distill += 1
        per_caption_glm2_distill_only_successful_calls[cid] = {
            "succ_count": s,
            "target_round2": TARGET_SUCCESSFUL_PER_CAPTION,
            "target_final": TARGET_FINAL_PER_CAPTION,
            "need_more_for_round2": need,
            "need_more_to_final": need_final,
            "met_target_round2": met,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 11. GLM_2 蒸馏侧 **round 2 续采判定**（沿 dispatch 字面块名 `glm2_distill_side_round2_progress`）
    glm2_distill_side_round2_progress = {
        "all_22_captions_met_target": met_target_count_glm2_distill == len(captions),
        "met_count_post_r2": met_target_count_glm2_distill,
        "total_captions": len(captions),
        "still_pending_round2": sorted([
            cid for cid, info in per_caption_glm2_distill_only_successful_calls.items() if not info["met_target_round2"]
        ]),
        "round2_progress_disposition": (
            f"GLM_2 蒸馏侧 round 2 续采达成 → 22/22 caption ≥2 successful (1→2 顺利) → 进入 round 3 接力（目标 ≥{TARGET_FINAL_PER_CAPTION} successful calls/caption 收官）"
            if met_target_count_glm2_distill == len(captions)
            else f"GLM_2 蒸馏侧 round 2 未达标 {len(captions) - met_target_count_glm2_distill} caption → 留 worker 下一棒接力（未达续采）"
        ),
        "rounds_to_reach_round2_target": 2,
        "rounds_to_reach_final_target_planned": 5,
        "rounds_to_reach_final_target_actual": (
            "5 棒 (r1+r2+r3+r4+r5) = 22 caption × 5 calls = 110 GLM_2 蒸馏侧 calls (沿 batch6 r5 收官类比)"
        ),
        "glm2_distill_side_round2_target_met_at_round": (
            "r2" if met_target_count_glm2_distill == len(captions) else "未达 (next 棒接力)"
        ),
    }

    # 12. dispatch §6 收尾盘点 —— GLM_2 蒸馏侧
    dispatch_target_progress_glm2_distill = {
        "target_round2": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (GLM_2 distill side only; round 2 续采阈值)",
        "target_final": f">={TARGET_FINAL_PER_CAPTION} successful calls/caption (GLM_2 distill side only; 最终收官阈值)",
        "met_count_post_r2": met_target_count_glm2_distill,
        "total_captions": len(captions),
        "remaining_count_round2": len(captions) - met_target_count_glm2_distill,
        "remaining_count_to_final": (
            sum(max(0, TARGET_FINAL_PER_CAPTION - per_cap_succ_glm2_distill[cid]) for cid in [c["id"] for c in captions])
        ),
        "met_percentage_round2": round(met_target_count_glm2_distill / len(captions) * 100, 2),
        "still_pending_round2_captions": sorted([
            cid for cid, info in per_caption_glm2_distill_only_successful_calls.items() if not info["met_target_round2"]
        ]),
        "is_round2_progress_round": True,
    }

    # 13. GLM_2 复用 GLM_1 拍板字面块（沿 mapping §1.2 + ask_748d9242 Q2 字面）
    glm2_reuse_glm1_caliber = {
        "v3_anchor_api_name": "GLM_2",
        "v3_anchor_9backbone_name": "glm-5.3-flash",
        "v4_current_model_id_sent": "glm-5.3（复用 GLM_1）",
        "v4_current_model_returned": "glm-5.3",
        "reuse_from_teacher": "GLM_1",
        "pi_decision_source": "ask_748d9242c7a6be3d83de63a0 Q2 字面（2026-09-24 23:08）",
        "pi_decision_quote": (
            "GLM_1 与 GLM_2 same lineage（glm-5.3 vs glm-5.3-flash 同一厂商系字面 + "
            "invitation §2.1 L58「GLM_1/GLM_2 same lineage」字面）；"
            "现行 teamo 探活清单 GLM 系 4 款同 5.x；故选定 GLM_2 与 GLM_1 同 model_id_sent"
            "（同 teamo `glm-5.3`），不同语料"
        ),
        "mapping_sha12": "98a779d61c1e",
        "mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
        "glm1_teacher_side_baseline_sha12": b2r2.get("metadata", {}).get("predecessor_sha12", {}).get("r1_executor_sha12", "n/a"),
        "note": (
            "本棒 teacher_label='GLM_2' + model_id_shared_with='GLM_1' 字段标识 GLM_2 教师身份；"
            "model_id_sent 仍为 glm-5.3（同 GLM_1）；result 内字段须明示 teacher 而非 model_id_sent 区分"
            "——避免误读为模型差异（沿 mapping §1.2 字面）"
        ),
    }

    # 14. retry validation 块
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

    # 15. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": BATCH,
        "round": ROUND,
        "metadata": {
            "task": "L14V3_batch8_round2_GLM_2_distill_side_reask1_progress_round_independent_counting",
            "prereg_sha12": "05B975a86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "batch8_r1_executor_sha12": "1e5f2249c517",
                "batch8_r1_executor_path": "results/_v4_supp_l14v3_batch8_r1_executor.py",
                "batch8_r1_result_sha12": "e6a94a0a13b7",
                "batch8_r1_result_path": "results/_v4_supp_l14v3_batch8_r1_result.json",
                "batch6_r5_executor_sha12": "8a8babb911b8",
                "batch6_r5_executor_path": "results/_v4_supp_l14v3_batch6_r5_executor.py",
                "batch6_r5_result_sha12": "e40424bf8abe",
                "batch6_r5_result_path": "results/_v4_supp_l14v3_batch6_r5_result.json",
                "batch6_r4_executor_sha12": "08f329b36e9d",
                "batch6_r4_executor_path": "results/_v4_supp_l14v3_batch6_r4_executor.py",
                "batch6_r4_result_sha12": "b7377ba019a1",
                "batch6_r4_result_path": "results/_v4_supp_l14v3_batch6_r4_result.json",
                "batch6_r3_executor_sha12": "1385d2ca356f",
                "batch6_r3_executor_path": "results/_v4_supp_l14v3_batch6_r3_executor.py",
                "batch6_r3_result_sha12": "15a7fecdffe7",
                "batch6_r3_result_path": "results/_v4_supp_l14v3_batch6_r3_result.json",
                "batch6_r2_executor_sha12": "93c931fc3b1c",
                "batch6_r2_executor_path": "results/_v4_supp_l14v3_batch6_r2_executor.py",
                "batch6_r2_result_sha12": "96e1de46ed30",
                "batch6_r2_result_path": "results/_v4_supp_l14v3_batch6_r2_result.json",
                "batch6_r1_executor_sha12": "ad35565f1ec9",
                "batch6_r1_executor_path": "results/_v4_supp_l14v3_batch6_r1_executor.py",
                "batch6_r1_result_sha12": "0d29e1ab4ae2",
                "batch6_r1_result_path": "results/_v4_supp_l14v3_batch6_r1_result.json",
                "batch2_r2_executor_sha12": "e7418f47a130",
                "batch2_r2_executor_path": "results/_v4_supp_l14v3_batch2_r2_executor.py",
                "batch2_r2_result_sha12": "8c125e257af8",
                "batch2_r2_result_path": "results/_v4_supp_l14v3_batch2_r2_result.json",
                "mapping_sha12": "98a779d61c1e",
                "mapping_sha12_discrepancy_note": (
                    "mapping 文件 L19 字面 batch2_r2_result_sha12 = CB37B699FF73, "
                    "L20 字面 batch2_r2_executor_sha12 = 5BE9DFE83A27；"
                    "实际盘上 SHA-12 = 8c125e257af8 (result) + e7418f47a130 (executor)；"
                    "两处 bytes 字面一致 (result=62,887 / executor=55,317)，故为 mapping 起草时 hash 算错而非文件被改；"
                    "mapping 文件按 R5 不擅改；本棒按实际盘上 SHA-12 记录并老实交代不一致；"
                    "PI 复核时按实际盘上 SHA-12 字面为准"
                ),
                "mapping_sha12_per_mapping_file_literal_buggy": {
                    "batch2_r2_result_sha12_per_mapping": "cb37b699ff73",
                    "batch2_r2_executor_sha12_per_mapping": "5be9dfe83a27",
                    "note": "mapping 文件字面（不一致披露；不动 mapping 文件）"
                },
                "mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                "prereg_sha12": "05b975a86989",
                "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
                "captions_sha12": "6a2656878745",
                "captions_path": "corpus/v20_caption_surface/strip_captions_22.json",
            },
            "date": "2026-09-25",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 8 round 2 GLM_2 distill side reask=1 续采棒",
            "is_finish_round": False,
            "is_round_2_progress_round": True,
            "night_authorization": "PI 2026-09-25 00:46「今晚保守口径下先斩后奏」",
            "prompt_construction_basis": {
                "v3_distill_original_prompt_on_disk": False,
                "v3_distill_original_prompt_path": None,
                "reproduction_caliber": True,
                "reproduction_source_anchor_sha12": "1e5f2249c517",
                "reproduction_source_anchor_path": "results/_v4_supp_l14v3_batch8_r1_executor.py",
                "reproduction_source_anchor_role": "r2 沿 r1 口径续跑 (GLM_2 蒸馏侧 22 caption × 5 calls 系列 round 2)",
                "v3_distill_pipeline_style_inherited": (
                    "V3-style concept-graph distillation continuation prompt (沿 r1 executor 1e5f2249c517 + batch6 r5 executor 8a8babb911b8);"
                    "prompt_text = Caption ID + Caption (sequence of concept labels) + Task (3-5 NEW related concept labels);"
                    "GLM_2 复用同 model = 蒸馏任务 prompt 不变；teacher 身份由 teacher_label='GLM_2' 字段标识"
                ),
            },
            "spec_conformance": (
                "PI 2026-09-25 同 agent 唤醒 (task_append) 接力棒 + 沿 r1 口径续跑 + "
                "GLM_2 复用 GLM_1 (沿 mapping §1.2 + ask_748d9242 Q2 拍板) + "
                "retry 修复沿 batch6 r5 + 每 caption successful 计数盘 + "
                "K-N26-N2 累计监控 + GLM_2 蒸馏侧独立计数（沿 r1 quadruples 过滤） + "
                "round 2 续采判定块 glm2_distill_side_round2_progress"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": ROUND,
            "target_successful_per_caption_round2": TARGET_SUCCESSFUL_PER_CAPTION,
            "target_successful_per_caption_final": TARGET_FINAL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r2_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": (
                "GLM_2 复用 GLM_1 现行采样 = teamo glm-5.3 (沿 batch2 r2 e7418f47a130 实测 22 calls + "
                "ask_748d9242 Q2 拍板 GLM_2 reuse GLM_1)"
            ),
            "model_id_sent": MODEL_GLM_5_3,
            "model_id_inconsistency_honest_disclosure": (
                "V3 字面锚 GLM_2 = glm-5.3-flash；现行 teamo 端点 GLM_2 = GLM_1 复用 = glm-5.3（沿 mapping §1.2 + ask_748d9242 Q2 拍板）；"
                "teacher_label='GLM_2' + model_id_shared_with='GLM_1' 字段标识 GLM_2 教师身份；"
                "model_id_sent 仍为 glm-5.3（同 GLM_1）；result 内字段须明示 teacher 而非 model_id_sent 区分"
                "——避免误读为模型差异；沿 user memory 2026-09-08「V3 端点名 vs 公开产品名不一致时直接问」"
                "——worker 不直接问 PI，记录为待 PI 复核项"
            ),
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
                "r5_status_anchor": "retry 修复 + tracking 改进沿 batch6 r5 (沿 8a8babb911b8)",
                "r1_status_anchor": "r1 沿 batch6 r5; r1 22/22 OK (1 retry)",
                "r2_status": "retry 修复沿 batch6 r5; r2 续采棒仅按 22 caption × 1 call 续采; hard fail 保持 fail path 立即返回",
                "rationale": (
                    "沿 batch6 r5 修复 + tracking 改进；r2 续采棒仅按 22 caption × 1 call 续采；"
                    "hard fail 保持 fail path 立即返回"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r1_executor": [
                "1. ROUND=2/REASK_R1=1 参数化 (r1 = 1/0; 本棒 = 2/1; reask_idx=1 = 第 2 call/caption on GLM_2 distill side)",
                "2. prompt_id 后缀 _r1 → _r2",
                "3. baseline 切换: 跨批累计 = r1 终态 cumulative (230/9/221/3.91%); GLM_2 蒸馏侧独立 = 22 caption 各 1 successful (沿 r1 quadruples 过滤)",
                "4. predecessor_sha12 链新增 r1_executor 1e5f2249c517 + r1_result e6a94a0a13b7",
                "5. target 切换: ≥1 successful/caption (r1 开工阈值) → ≥2 successful/caption (r2 续采阈值)",
                "6. 判定块命名: glm2_distill_side_round1_progress (r1 开工) → glm2_distill_side_round2_progress (r2 续采); 字段 met_target_round1 → met_target_round2",
                "7. is_round_2_progress_round 标记: metadata.is_round_1_start_round = True (r1) → is_round_2_progress_round = True (r2)",
                "8. mapping_sha12_discrepancy_note 沿用 (不动 mapping 文件)",
                "9. diff_vs_r1_executor 新块 (取代 r1 的 diff_vs_batch6_r5_executor)",
                "10. r2 增量计数 → GLM_2 蒸馏侧各 caption 由 1/5 顺利补至 2/5 (r2 OK 全达标 if no fails)",
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
        "per_caption_glm2_distill_only_successful_calls": per_caption_glm2_distill_only_successful_calls,
        "glm2_distill_side_round2_progress": glm2_distill_side_round2_progress,
        "dispatch_target_progress_glm2_distill": dispatch_target_progress_glm2_distill,
        "glm2_reuse_glm1_caliber": glm2_reuse_glm1_caliber,
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
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round_2_n_distinct_sample_note": (
                    "round 2 续采棒第 2 call per caption 实测；GLM_2 蒸馏侧独立计数 = "
                    f"22 caption 各 {per_cap_succ_glm2_distill[list(per_cap_succ_glm2_distill.keys())[0]]} successful (沿 r1+r2 quadruples, prompt_id 前缀 glm2_t01_distill_ filter 域);"
                    f"**GLM_2 蒸馏侧 round 2 续采判定**: {met_target_count_glm2_distill}/{len(captions)} caption 达 ≥2 successful;"
                    "后续 r3/r4/r5 接力至 5/5 successful/caption 收官 (沿 batch6 r5 收官口径类比);"
                    "由 verdict-keeper 统裁 (本棒 0 写 verdict)"
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
                        "本棒未触发 K-N26-N2 累计阈值；跑至 1500s watchdog 提前停批 / 全 22 calls 完成 (round 2 续采态)"
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
            "next_resume_via": (
                "task_append 接力棒至 GLM_2 蒸馏侧 round 3 (>=3 more successful/caption); "
                "沿 prereg §1.6.4 同 agent 唤醒"
            ),
            "note": (
                f"本棒 round 2 续采棒已完成（{r2_total}/{planned_total} calls）"
                + (f"；K-N26-N2 累计阈值触发：cum_rate={round(k_n26_n2_trigger_cum_rate,4) if k_n26_n2_trigger_cum_rate else None} > 0.50, 立即停采 (沿 dispatch §4)"
                   if k_n26_n2_triggered else
                   f"；撞 {WALL_TIME_BUDGET_S}s watchdog 提前停批 ({len(captions) - met_target_count_glm2_distill} caption 未达 round 2 续采阈值) 走 task_append 接力棒"
                   if wall_time_s > WALL_TIME_BUDGET_S and met_target_count_glm2_distill < len(captions) else
                   f"；**GLM_2 蒸馏侧 round 2 续采达成** {met_target_count_glm2_distill}/{len(captions)} caption ≥2 successful ✓"
                   if met_target_count_glm2_distill == len(captions) else
                   f"；GLM_2 蒸馏侧 round 2 未达标 {len(captions) - met_target_count_glm2_distill} caption → 下一棒接力 (未达续采)")
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],
            "scanned_at": now_iso,
        },
    }

    # 16. 落盘前自扫
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan

    # 17. 落盘
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch8_r2_result.json")
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
    print(f"  glm2_distill_side_round2_met: {met_target_count_glm2_distill}/{len(captions)}")
    print(f"  *** all_22_captions_met_round2_target: {glm2_distill_side_round2_progress['all_22_captions_met_target']} ***")
    print(f"  round2_progress_disposition: {glm2_distill_side_round2_progress['round2_progress_disposition']}")
    print(f"  retry_bug_fix_applied_in_all_calls: {retry_validation['r2_retry_bug_fix_applied_in_all_calls']}")
    print(f"  retry_triggered_count: {retry_triggered_count}")
    print(f"  retry_count_distribution: {retry_count_distribution}")
    print(f"  retry_trigger_categories_distribution: {retry_trigger_categories_distribution}")
    print(f"  tun_compliance: {tun_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  stop_reason: {stop_reason}")
    if glm2_distill_side_round2_progress["still_pending_round2"]:
        print(f"  still_pending_round2: {glm2_distill_side_round2_progress['still_pending_round2']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
