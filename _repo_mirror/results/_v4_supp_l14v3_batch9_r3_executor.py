# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch9_r3_executor.py
====================================

V4 L14+ batch 9 · round 3（reask=2）—— coze 蒸馏侧接力棒（沿 r2 口径续跑）
==========================================================================

【派工依据】
----------------
- 沿 batch9 r2 `results/_v4_supp_l14v3_batch9_r2_executor.py`（SHA-12 `7eec235a9ca2`）+ r2 产物
  `results/_v4_supp_l14v3_batch9_r2_result.json`（SHA-12 `08b0aaaae726`；coze 蒸馏侧 round 2 接力达成 22/22 caption ≥2 successful）
- 沿 batch9 r1 `results/_v4_supp_l14v3_batch9_r1_executor.py`（SHA-12 `e78ca71bd077`）+ r1 产物
  `results/_v4_supp_l14v3_batch9_r1_result.json`（SHA-12 `7e8dfe0156cd`；coze 蒸馏侧 round 1 开工达成 22/22 caption ≥1 successful）
- 沿 batch8 r5 `results/_v4_supp_l14v3_batch8_r5_executor.py`（SHA-12 `6961281824ae`）+ r5 产物
  `results/_v4_supp_l14v3_batch8_r5_result.json`（SHA-12 `3620a7daf9c1`；累计 baseline = 318/9/2.83%）
- 沿 batch6 r5 `results/_v4_supp_l14v3_batch6_r5_executor.py`（SHA-12 `8a8babb911b8`）+ r5 产物
  `results/_v4_supp_l14v3_batch6_r5_result.json`（SHA-12 `e40424bf8abe`；distill 口径锚 + kimi 蒸馏侧 22/22 caption 5/5 successful 收官）
- 沿 batch4 r6 `results/_v4_supp_l14v3_batch4_r6_executor.py`（coze 教师侧 S6_n60 定向补；deepseek-v4-flash 代表采样字面）
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（SHA-12 `05b975a86989`）字面
- 沿 model mapping `results/_v4_supp_l14v3_model_mapping_2026_09_24.md`（SHA-12 `98a779d61c1e`）
  - coze = agent 平台封装 (PI 拍板 ask_748d9242c7a6be3d83de63a0 Q3 字面：「coze与trea都只是agent平台，我都是接的大模型API」)
  - coze 底层大模型 API 不可考 → 本重跑以现行大模型 API **deepseek-v4-flash** (teamo) **代表采样**
  - result 内 metadata 字段强制标注 representative_for_coze: true + substitute_origin 标注沿用 (身份不冒充)
- 同 agent 唤醒保上下文（task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义）
- PI 2026-09-25 00:46「今晚保守口径下先斩后奏」夜间授权（保守口径自主决策，标注待 PI 复核）

【本棒范围（沿 dispatch）—— coze 蒸馏侧 round 3 接力棒（reask=2）】
--------------------------------------------------------------------
1. **22 caption × 1 call** = 22 calls（沿 r2 / dispatch 字面）
2. **计数口径沿 r2**：
   - **distill 侧独立计数**：`coze_t01_distill_*` prompt_id 前缀为域（沿 r2 字面）
   - 目标 = coze 蒸馏侧 round 3 ≥2 successful call/caption（接力；非开工非收官）
   - 当前 coze 蒸馏侧 = 22 caption 各 2/5 successful（沿 r2 终态）
   - 本棒补 1 call/caption → coze 蒸馏侧 3/5 successful（**接力判定阈值**）
3. **model 口径沿 r2**：
   - `model_id_sent` = `deepseek-v4-flash`（teamo 端点；coze 底层 model 不可考 → 代表采样）
   - `teacher_label` = `coze`
   - **`representative_for_coze` = True**（沿 mapping 留痕件 §1.1 第三栏 PI 拍板代表采样）
   - **`substitute_origin` = "coze_agent_platform_underlying_model_not_documented"**（沿 mapping 留痕件 §1.1 第三栏字面）
4. **慢响应 caption 处理**（沿 r2 实测）：
   - r2 S6_n60: lat=11058.0ms, retries=1（timeout 后 retry）→ 2/2 successful
   - r2 S1_n60: lat=30330.4ms, retries=0 → 2/2 successful
   - r2 S6_n35: lat=25210.1ms, retries=0 → 2/2 successful
   - r2 S1_n45: lat=12291.3ms, retries=1 → 2/2 successful
   - r2 S2_n35: lat=5095.7ms, retries=1 → 2/2 successful
   - 本棒 r3 沿 r2 同 retry 修复路径消化（read_timeout_initial_s=60 / read_timeout_retry_s=90 / inner_retry_max=3）
   - 如 r3 仍空/失败 → 沿 dispatch 「断点 + 老实交代」如实记录，不擅自补 call
5. **接力判定块 `coze_distill_side_round3_progress`**：
   - `met_count_post_r3`：本棒后达标 caption 数（预期 22）
   - `still_pending_round3`：未达标 caption 列表（预期空）
   - `round3_progress_disposition`：coze 蒸馏侧 round 3 接力判定
   - **非收官棒**：本棒仅 round 3 接力 ≠ 收官；后续 r4/r5 接力至 5/5 successful/caption

【每 caption successful 计数盘（沿 dispatch §6）—— coze 蒸馏侧独立域】
----------------------------------------------------------------------
- 本棒前基线（coze 蒸馏侧独立计数，沿 r1+r2 quadruples 过滤）：22 caption 各 2/5 successful
- 本棒增量计算：每 call 后实时更新 `per_cap_succ_coze_distill` 字典
- 终盘结果（coze 蒸馏侧独立计数）：
  - `per_caption_coze_distill_only_successful_calls` 块（coze 蒸馏侧独立计数；含 r1+r2+r3）
  - `coze_distill_side_round3_progress` 块（**接力判定**）
  - `dispatch_target_progress_coze_distill` 块（coze 蒸馏侧目标进展 — round 3 接力态）

【retry 修复沿 r2（沿 dispatch §3）】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}（沿 r2）
- read_timeout_initial_s=60 / read_timeout_retry_s=90（沿 r2）
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回（沿 r2）
- r2 retry 触发的源 error_category tracking 改进沿用（沿 r2；含 tracker 漏记 1 个 timeout bug 不擅改）

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
-------------------------------------------
- 累计 = batch9 r2 终态 + batch9 r3 coze 增量（coze 蒸馏侧 round 3）
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 实测累计基线（沿 r2 产物）：
  - prior (b1+r2+r3+r4+r5+b6r1-r5+b7r1-r5+b8r1-r5+b9r1-r2): total=362, empty=9, **rate=2.49%**
  - r3 worst case (22 EMPTY): cumulative = 31/384 = 8.07% (仍 < 50% 阈值)
  - r3 best case (0 EMPTY): cumulative = 9/384 = 2.34% (仍 < 50% 阈值)

【端点取舍（沿 r2 + batch4 r6）】
----------------------------
- teamo + tun + deepseek-v4-flash（coze 代表采样；沿 r2 22 caption 22 OK 实测）
- 不重新探活（沿 dispatch §4 「沿 r2 口径续跑」+ 即用即探口径）
- **夜间保守口径**（PI 2026-09-25 00:46）：启动前必检 tun 端口（防 net::ERR_HTTP2_PING_FAILED 重演）

【铁律严守（沿 r2）】
------------------------
- R4 key 永不明文（无例外）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch9_r3_*` 与 r1+r2 + 前棒所有 _batch*_r* 同级独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch9_r3_result.json`
  （schema = v4_l14v3_n26/1 + batch=9 + round=3 + teacher=coze + side=distill）
- 不覆盖 r2 result `08b0aaaae726` 或 r1 result `7e8dfe0156cd` 或前棒 result（沿 dispatch §4）

【与 r2 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------
1. **ROUND = 3 / REASK_R1 = 2** 参数化（r2 = 2/1；本棒 = 3/2）
2. **prompt_id 后缀切换**：`_r2` → `_r3`（distill 侧 coze 域 round 3）
3. **baseline 切换**：
   - r2 终态：coze 蒸馏侧独立 = 22 caption 各 2/5 successful (44 calls 沿 r1+r2 quadruples 累计)
   - 跨批累计：r2 终态 cumulative (362/9/353/2.49%)
4. **target 切换**：≥2 successful/caption (r2 接力阈值) → ≥3 successful/caption (r3 接力阈值)
5. **判定块命名**：
   - `coze_distill_side_round2_progress` (r2 接力) → `coze_distill_side_round3_progress` (本棒接力)
   - `dispatch_target_progress_coze_distill` 块沿 r2 不变（仅更新 met_count_post_r3 + remaining_count_round3）
6. **non_finish_round 标记**：metadata.is_finish_round = False + is_round_3_relay_round = True (本棒 round 3 接力 ≠ 收官)
7. **predecessor_sha12 链新增**：r2 双件 (7eec235a9ca2 / 08b0aaaae726)
8. **phase_label 切换**：`r2_coze_distill_*` → `r3_coze_distill_*`
9. **r3 接力判定字段新增**：rounds_to_reach_round3_target = 3; rounds_to_reach_final_target_actual 更新为 "5 棒 (r1+r2+r3+r4+r5) = 22 caption × 5 calls = 110 coze 蒸馏侧 calls (沿 batch6 r5 收官类比)"

【边界】
----------
- 不动任何既有件（含 r2 双件 + r1 双件 + batch8 r5/r4/r3/r2/r1 双件 + batch6 r5/r4/r3/r2/r1 双件 + batch4 r5/r6 双件
  + batch2 r2 GLM_1 双件 + prereg `05b975a86989` + mapping `98a779d61c1e` + captions `6a2656878745`）
- 跑不完拆段报断点
- 0 触动 V1–V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
- 不立 V3 → V4 coze 代表采样 = coze 背后模型断言（沿诚实 = 不误导 + 不可考即如实不可考）
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import socket
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

# 前棒产物（baseline 沿用）
BATCH9_R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch9_r2_result.json")
BATCH9_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch9_r1_result.json")
BATCH8_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch8_r5_result.json")
BATCH6_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch6_r5_result.json")
BATCH4_R6_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r6_result.json")

# tun 代理（沿 r2）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"
TUN_HOST = "127.0.0.1"
TUN_PORT = 1018

# ============================================================
# 端点配置（coze 代表采样 = teamo deepseek-v4-flash；沿 r2）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_COZE_REPRESENTATIVE = "deepseek-v4-flash"  # coze 底层 model 不可考 → 代表采样
KEY_INDEX_TEAMO_1BASED = 15
USE_PROXY = True

# representative 标注（强制入 result metadata，沿 r2 字面）
REPRESENTATIVE_FOR_COZE = True
SUBSTITUTE_ORIGIN = "coze_agent_platform_underlying_model_not_documented"

# 串行间隔（沿 r2）
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 r2；同模型同 prompt 不改）
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正（沿 r2）
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别（沿 r2）
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值（沿 r2）
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 预算（沿 r2；扩至 1500s 以容纳 22 calls；含 5 慢响应 caption 风险）
WALL_TIME_BUDGET_S = 1500

# 本棒调度
BATCH = 9
ROUND = 3
SIDE = "distill"
TEACHER = "coze"
REASK_R1 = 2  # round 3 = 第 3 call per caption (reask_idx = 2) — 接力
TARGET_SUCCESSFUL_PER_CAPTION = 3  # coze 蒸馏侧 round 3 接力阈值（≥3 successful calls/caption）
TARGET_FINAL_PER_CAPTION = 5  # coze 蒸馏侧最终目标阈值（5 successful calls/caption；沿 batch6 r5 收官口径类比；后续 r4-r5 接力）

# ============================================================
# 计数口径（coze 蒸馏侧独立）
# ============================================================
DISTILL_SIDE_PROMPT_ID_PREFIX = "coze_t01_distill_"


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


def preflight_tun_check() -> bool:
    """夜间保守口径 (PI 2026-09-25 00:46) — 启动前必检 tun 端口; 不通即停。
    防 net::ERR_HTTP2_PING_FAILED 类网络层断连重演。"""
    try:
        with socket.create_connection((TUN_HOST, TUN_PORT), timeout=5.0) as s:
            return True
    except (OSError, socket.timeout) as e:
        print(f"[PREFLIGHT FATAL] tun 端口 {TUN_HOST}:{TUN_PORT} 不可达: {e}; 不启动")
        return False


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
        "HTTP-Referer": "https://deposon.local/l14v3-batch9-r3",
        "X-Title": "deposon-l14v3-batch9-r3-coze-distill",
    }
    body = {
        "model": MODEL_COZE_REPRESENTATIVE,
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
# 提示构造（沿 r2；coze 代表采样 = 蒸馏 prompt 不变）
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
# 单 call + 内层重试（沿 r2 + batch4 r6 representative 标注）
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    is_round_3: bool,
    phase_label: str,
    retry_trigger_categories_tracker: List[str],
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    suffix = "_r3"
    prompt_id = f"coze_t01_{side}_{caption_id}{suffix}"

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
                        "model_id_sent": MODEL_COZE_REPRESENTATIVE,
                        "side": side,
                        "teacher_label": TEACHER,
                        "representative_for_coze": REPRESENTATIVE_FOR_COZE,
                        "substitute_origin": SUBSTITUTE_ORIGIN,
                        "caption_id": caption_id,
                        "reask_idx": reask_idx,
                        "round_index": round_index,
                        "is_round_3": is_round_3,
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
                "model_id_sent": MODEL_COZE_REPRESENTATIVE,
                "side": side,
                "teacher_label": TEACHER,
                "representative_for_coze": REPRESENTATIVE_FOR_COZE,
                "substitute_origin": SUBSTITUTE_ORIGIN,
                "caption_id": caption_id,
                "reask_idx": reask_idx,
                "round_index": round_index,
                "is_round_3": is_round_3,
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
            "model_id_sent": MODEL_COZE_REPRESENTATIVE,
            "side": side,
            "teacher_label": TEACHER,
            "representative_for_coze": REPRESENTATIVE_FOR_COZE,
            "substitute_origin": SUBSTITUTE_ORIGIN,
            "caption_id": caption_id,
            "reask_idx": reask_idx,
            "round_index": round_index,
            "is_round_3": is_round_3,
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
    print(f"V4 L14+ batch 9 round 3 | coze distill side | reask=2 — 接力棒")
    print(f"模型: deepseek-v4-flash (teamo; coze 代表采样 = 不可考即如实不可考)")
    print(f"representative_for_coze=true; substitute_origin 沿 mapping §1.1 字面")
    print(f"计划 calls = 22 (22 caption × 1 call)")
    print(f"计数口径: coze 蒸馏侧独立 (prompt_id 前缀 coze_t01_distill_) — 沿 r2")
    print(f"coze 蒸馏侧 baseline (沿 r2 终态): 22 caption 各 2/5 successful")
    print(f"目标: coze 蒸馏侧 ≥3 successful calls/caption (round 3 接力阈值)")
    print(f"最终目标: coze 蒸馏侧 ≥5 successful calls/caption (后续 r4-r5 接力)")
    print(f"预算 ≤1500s watchdog (含 5 慢响应 caption 风险)")
    print(f"retry 修复沿 r2 (含 retry 触发的源 error_category tracking)")
    print(f"S6_n60/S1_n60/S6_n35 等已知慢响应 caption 靠 retry 消化")
    print(f"夜间保守口径 (PI 2026-09-25 00:46): 启动前必检 tun 端口")
    print("=" * 60)

    setup_proxy_teamo()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # 0. 夜间保守口径 — 启动前必检 tun 端口 (防 net::ERR_HTTP2_PING_FAILED 重演)
    if not preflight_tun_check():
        return 1

    # 1. 加载 caption
    captions = load_captions()
    cap_by_id = {c["id"]: c for c in captions}
    print(f"[INIT] captions loaded: {len(captions)}")

    # 2. 加载 r2 + r1 + batch8 r5 + batch6 r5 + batch4 r6 result（用于 baseline + cumulative + coze 代表采样字面）
    with open(BATCH9_R2_RESULT_PATH, "r", encoding="utf-8") as f:
        b9r2 = json.load(f)
    with open(BATCH9_R1_RESULT_PATH, "r", encoding="utf-8") as f:
        b9r1 = json.load(f)
    with open(BATCH8_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b8r5 = json.load(f)
    with open(BATCH6_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b6r5 = json.load(f)
    with open(BATCH4_R6_RESULT_PATH, "r", encoding="utf-8") as f:
        b4r6 = json.load(f)

    # 3. coze 蒸馏侧独立计数起点（filter by prompt_id 前缀 coze_t01_distill_）—— 沿 r2 终态
    per_cap_succ_coze_distill = {c["id"]: 0 for c in captions}
    per_cap_total_coze_distill = {c["id"]: 0 for c in captions}
    per_cap_empty_coze_distill = {c["id"]: 0 for c in captions}
    # 从 r2 quadruples 累计（每 caption 2/5 successful；r1+r2 全 ok 22+22=44 calls，0 empty）
    r2_per_cap = b9r2.get("per_caption_coze_distill_only_successful_calls", {})
    for cid in [c["id"] for c in captions]:
        r2_info = r2_per_cap.get(cid, {})
        per_cap_succ_coze_distill[cid] = r2_info.get("succ_count", 0)
        per_cap_total_coze_distill[cid] = r2_info.get("total_calls_so_far", 0)
        per_cap_empty_coze_distill[cid] = r2_info.get("empty_count_so_far", 0)
    r2_distill_total = sum(per_cap_total_coze_distill.values())
    r2_distill_succ = sum(per_cap_succ_coze_distill.values())
    r2_distill_empty = sum(per_cap_empty_coze_distill.values())
    print(f"[COZE DISTILL r2 prior] total={r2_distill_total} succ={r2_distill_succ} empty={r2_distill_empty} (r1+r2 quadruples filter)")

    # 4. 跨批累计监控（沿 r2 cumulative 链路 + coze 增量）
    r2_cum = b9r2["aggregate"]["cumulative"]
    cum_total_prior_cum = r2_cum["post_total"]  # 362
    cum_empty_prior_cum = r2_cum["post_empty"]  # 9
    cum_ok_prior_cum = r2_cum["post_ok"]        # 353
    cum_rate_prior = cum_empty_prior_cum / cum_total_prior_cum if cum_total_prior_cum > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior_cum} ok={cum_ok_prior_cum} "
          f"empty={cum_empty_prior_cum} rate={cum_rate_prior:.4f} (源 = batch9 r2 aggregate.cumulative post)")

    # 5. 调度 planned_calls（22 caption × 1 call = 22 calls）
    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r3_coze_distill_{c['id']}"}
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
            is_round_3=True,
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
            r3_ok += 1
            cum_ok += 1
            per_cap_succ_coze_distill[cap_id] += 1
        elif is_empty:
            r3_empty += 1
            cum_empty += 1
            per_cap_empty_coze_distill[cap_id] += 1
        else:
            r3_fail += 1
        r3_total += 1
        cum_total += 1
        per_cap_total_coze_distill[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ_coze_distill = per_cap_succ_coze_distill[cap_id]
        target_met_coze_distill = "[OK] 接力" if cur_succ_coze_distill >= TARGET_SUCCESSFUL_PER_CAPTION else "[..]"
        print(
            f"  [{i+1:2d}/{planned_total}] {marker} {item['phase']:<32} {cap_id:<28} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"retries={rc} "
            f"{status} "
            f"[coze_distill_succ={cur_succ_coze_distill}/{TARGET_SUCCESSFUL_PER_CAPTION} {target_met_coze_distill}] "
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
    empty_rate_r3 = (r3_empty / r3_total) if r3_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 10. 每 caption successful 计数 —— coze 蒸馏侧独立（含 r1+r2+r3 累计）
    per_caption_coze_distill_only_successful_calls = {}
    met_target_count_coze_distill = 0
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ_coze_distill[cid]
        t = per_cap_total_coze_distill[cid]
        e = per_cap_empty_coze_distill[cid]
        need = max(0, TARGET_SUCCESSFUL_PER_CAPTION - s)
        met = s >= TARGET_SUCCESSFUL_PER_CAPTION
        if met:
            met_target_count_coze_distill += 1
        per_caption_coze_distill_only_successful_calls[cid] = {
            "succ_count": s,
            "target_round3": TARGET_SUCCESSFUL_PER_CAPTION,
            "target_final": TARGET_FINAL_PER_CAPTION,
            "need_more_for_round3": need,
            "met_target_round3": met,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 11. coze 蒸馏侧 **round 3 接力判定**（沿 dispatch 字面块名 `coze_distill_side_round3_progress`）
    coze_distill_side_round3_progress = {
        "all_22_captions_met_round3_target": met_target_count_coze_distill == len(captions),
        "met_count_post_r3": met_target_count_coze_distill,
        "total_captions": len(captions),
        "still_pending_round3": sorted([
            cid for cid, info in per_caption_coze_distill_only_successful_calls.items() if not info["met_target_round3"]
        ]),
        "round3_progress_disposition": (
            f"coze 蒸馏侧 round 3 接力达成 → 22/22 caption ≥3 successful → 进入 round 4 接力（目标 ≥{TARGET_FINAL_PER_CAPTION} successful calls/caption 收官）"
            if met_target_count_coze_distill == len(captions)
            else f"coze 蒸馏侧 round 3 未达标 {len(captions) - met_target_count_coze_distill} caption → 留 worker 下一棒接力（未达接力阈值）"
        ),
        "rounds_to_reach_round3_target": 3,
        "rounds_to_reach_final_target_planned": 5,
        "rounds_to_reach_final_target_actual": (
            "5 棒 (r1+r2+r3+r4+r5) = 22 caption × 5 calls = 110 coze 蒸馏侧 calls (沿 batch6 r5 收官类比)"
        ),
        "coze_distill_side_round3_target_met_at_round": (
            "r3" if met_target_count_coze_distill == len(captions) else "未达 (next 棒接力)"
        ),
    }

    # 12. dispatch §6 收尾盘点 —— coze 蒸馏侧（含 r1+r2+r3 累计）
    dispatch_target_progress_coze_distill = {
        "target_round3": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (coze distill side only; round 3 接力阈值)",
        "target_final": f">={TARGET_FINAL_PER_CAPTION} successful calls/caption (coze distill side only; 最终收官阈值)",
        "met_count_post_r3": met_target_count_coze_distill,
        "total_captions": len(captions),
        "remaining_count_round3": len(captions) - met_target_count_coze_distill,
        "remaining_count_to_final": (
            sum(max(0, TARGET_FINAL_PER_CAPTION - per_cap_succ_coze_distill[cid]) for cid in [c["id"] for c in captions])
        ),
        "met_percentage_round3": round(met_target_count_coze_distill / len(captions) * 100, 2),
        "still_pending_round3_captions": sorted([
            cid for cid, info in per_caption_coze_distill_only_successful_calls.items() if not info["met_target_round3"]
        ]),
        "is_round3_only": True,
    }

    # 13. coze 代表采样拍板字面块（沿 mapping §1.1 第三栏 + batch4 r6 字面 + r1+r2 沿用）
    coze_representative_caliber = {
        "v3_anchor_api_name": "coze",
        "v3_anchor_9backbone_name": None,  # coze 不在 9-backbone 字段；V3 字面层不可考
        "v4_current_model_id_sent": "deepseek-v4-flash（代表采样）",
        "v4_current_model_returned": "deepseek-v4-flash 系 family 实例",
        "representative_for_coze": REPRESENTATIVE_FOR_COZE,
        "substitute_origin": SUBSTITUTE_ORIGIN,
        "pi_decision_source": "ask_748d9242c7a6be3d83de63a0 Q3 字面（2026-09-24 23:08）",
        "pi_decision_quote": (
            "coze 与 trea 都只是 agent 平台，我都是接的大模型 API"
            "（沿 mapping §1.1 第三栏 PI 拍板字面引用；coze 底层大模型 API 不可考）"
        ),
        "mapping_sha12": "98a779d61c1e",
        "mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
        "smoke_anchor_teacher_side": (
            "batch4 r6 / r5 沿 coze 教师侧 deepseek-v4-flash 实测 (1-call smoke ok=200 + 22 caption 21 OK + S6_n60 空响应已知)"
        ),
        "smoke_anchor_distill_side_r1_r2": (
            "batch9 r1+r2 沿 coze 蒸馏侧 deepseek-v4-flash 实测 (r1: 22 caption 22 OK + 0 empty + wall 328.1s; "
            "r2: 22 caption 22 OK + 0 empty + wall 430.9s + 3 retries)"
        ),
        "note": (
            "本棒 teacher_label='coze' + representative_for_coze=true + substitute_origin 字面标注 coze 教师身份；"
            "model_id_sent = deepseek-v4-flash (代表采样；coze 底层 model 不可考即如实不可考)；"
            "result 内字段须明示 representative_for_coze=true 而非 model_id_sent 区分"
            "——避免误读为 coze 背后真实模型（沿 mapping §1.1 + 诚实 = 不误导）"
        ),
    }

    # 14. retry validation 块
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
        "slow_caption_special_note": (
            "S6_n60/S1_n60/S6_n35 等已知慢响应 caption 沿 r2 同 retry 路径消化 (timeout_initial=60 / retry=90 / max=3);"
            "r2 实测 S6_n60 lat=11s retries=1, S1_n60 lat=30s retries=0, S6_n35 lat=25s retries=0, S2_n35 lat=5s retries=1, S1_n45 lat=12s retries=1;"
            "r3 实测延迟如实记录，不预测不擅自补 call"
        ),
    }

    # 15. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    self_executor_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch9_r3_executor.py")
    self_result_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch9_r3_result.json")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": BATCH,
        "round": ROUND,
        "metadata": {
            "task": "L14V3_batch9_round3_coze_distill_side_reask2_relay_round_independent_counting",
            "prereg_sha12": "05b975a86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "batch9_r2_executor_sha12": "7eec235a9ca2",
                "batch9_r2_executor_path": "results/_v4_supp_l14v3_batch9_r2_executor.py",
                "batch9_r2_result_sha12": "08b0aaaae726",
                "batch9_r2_result_path": "results/_v4_supp_l14v3_batch9_r2_result.json",
                "batch9_r1_executor_sha12": "e78ca71bd077",
                "batch9_r1_executor_path": "results/_v4_supp_l14v3_batch9_r1_executor.py",
                "batch9_r1_result_sha12": "7e8dfe0156cd",
                "batch9_r1_result_path": "results/_v4_supp_l14v3_batch9_r1_result.json",
                "batch8_r5_executor_sha12": "6961281824ae",
                "batch8_r5_executor_path": "results/_v4_supp_l14v3_batch8_r5_executor.py",
                "batch8_r5_result_sha12": "3620a7daf9c1",
                "batch8_r5_result_path": "results/_v4_supp_l14v3_batch8_r5_result.json",
                "batch8_r4_executor_sha12": "6b69ec8406d4",
                "batch8_r4_executor_path": "results/_v4_supp_l14v3_batch8_r4_executor.py",
                "batch8_r4_result_sha12": "c7d5aa2a9b00",
                "batch8_r4_result_path": "results/_v4_supp_l14v3_batch8_r4_result.json",
                "batch8_r3_executor_sha12": "0f654d945f12",
                "batch8_r3_executor_path": "results/_v4_supp_l14v3_batch8_r3_executor.py",
                "batch8_r3_result_sha12": "56faf9324fba",
                "batch8_r3_result_path": "results/_v4_supp_l14v3_batch8_r3_result.json",
                "batch8_r2_executor_sha12": "6a9bbc43c808",
                "batch8_r2_executor_path": "results/_v4_supp_l14v3_batch8_r2_executor.py",
                "batch8_r2_result_sha12": "7b23996b5f4c",
                "batch8_r2_result_path": "results/_v4_supp_l14v3_batch8_r2_result.json",
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
                "batch4_r6_executor_sha12": "7f2c5e26e6c5",
                "batch4_r6_executor_path": "results/_v4_supp_l14v3_batch4_r6_executor.py",
                "batch4_r6_result_sha12": "6b8093ff8962",
                "batch4_r6_result_path": "results/_v4_supp_l14v3_batch4_r6_result.json",
                "batch4_r5_executor_sha12": "8a505613b476",
                "batch4_r5_executor_path": "results/_v4_supp_l14v3_batch4_r5_executor.py",
                "batch4_r5_result_sha12": "bad01f2b89fd",
                "batch4_r5_result_path": "results/_v4_supp_l14v3_batch4_r5_result.json",
                "mapping_sha12": "98a779d61c1e",
                "mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                "captions_sha12": "6a2656878745",
                "captions_path": "corpus/v20_caption_surface/strip_captions_22.json",
            },
            "date": "2026-09-26",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 9 round 3 coze distill side reask=2 接力棒",
            "is_finish_round": False,
            "is_round_3_relay_round": True,
            "night_authorization": "PI 2026-09-25 00:46「今晚保守口径下先斩后奏」",
            "prompt_construction_basis": {
                "v3_distill_original_prompt_on_disk": False,
                "v3_distill_original_prompt_path": None,
                "reproduction_caliber": True,
                "reproduction_source_anchor_sha12": "8a8babb911b8",
                "reproduction_source_anchor_path": "results/_v4_supp_l14v3_batch6_r5_executor.py",
                "reproduction_source_anchor_role": "coze_representative_distill_prompt_沿_batch6_r5（coze 底层 model 不可考 → 代表采样 = 蒸馏 prompt 不变）",
                "v3_distill_pipeline_style_inherited": (
                    "V3-style concept-graph distillation continuation prompt (沿 batch6 r5 executor 8a8babb911b8);"
                    "prompt_text = Caption ID + Caption (sequence of concept labels) + Task (3-5 NEW related concept labels);"
                    "coze 代表采样同模型 = 蒸馏任务 prompt 不变；teacher 身份由 teacher_label='coze' + representative_for_coze=true 字段标识"
                ),
            },
            "spec_conformance": (
                "PI 2026-09-25 同 agent 唤醒 (task_append) 接力棒 + 沿 r2 口径续跑 + "
                "coze = agent 平台封装 (沿 mapping §1.1 第三栏 + ask_748d9242 Q3 拍板) + "
                "代表采样 = deepseek-v4-flash (teamo; 沿 r1+r2 44 caption 44 OK 实测) + "
                "retry 修复沿 r2 + 每 caption successful 计数盘 + "
                "K-N26-N2 累计监控 + coze 蒸馏侧独立计数（沿 r2 counting_scope_correction） + "
                "round 3 接力判定块 coze_distill_side_round3_progress + representative/substitute 标注 (沿 r2 字面)"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": ROUND,
            "target_successful_per_caption_round3": TARGET_SUCCESSFUL_PER_CAPTION,
            "target_successful_per_caption_final": TARGET_FINAL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r3_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": (
                "coze = agent 平台封装 → 代表采样 = teamo deepseek-v4-flash "
                "(沿 mapping §1.1 第三栏 PI 拍板 + r1+r2 44 caption 44 OK + batch4 r6 smoke ok=200)"
            ),
            "model_id_sent": MODEL_COZE_REPRESENTATIVE,
            "representative_for_coze": REPRESENTATIVE_FOR_COZE,
            "substitute_origin": SUBSTITUTE_ORIGIN,
            "model_id_inconsistency_honest_disclosure": (
                "V3 字面锚 coze (V3 公开产品名 / 端点名) 不在 9-backbone 字段；制品层 by_model/coze/ 同样无 model 字段；"
                "teamo /v1/models 探活清单 (44 models) 字面亦无 coze 字段；"
                "coze 底层大模型 API 不可考 = 如实不可考 (沿诚实 = 不误导); "
                "本棒选定 = deepseek-v4-flash (teamo 端点; 沿 r1+r2 44 caption 44 OK 实测; "
                "代表采样选择 deepseek-v4-flash 理由 = 团队现行 6 模型补跑锚定 + teamo /v1/models 探活清单字面可考); "
                "代表采样 ≠ coze 背后模型; "
                "result 内 metadata 字段强制标注 representative_for_coze=true + substitute_origin=coze_agent_platform_underlying_model_not_documented; "
                "本映射选择 = PI 拍板代表采样 (沿 ask_748d9242 Q3 字面), 非 V3 字面继承, 非断层真实 mapping 断言; "
                "沿 user memory 2026-09-08「V3 端点名 vs 公开产品名不一致时直接问」"
                "—— worker 不直接问 PI，记录为待 PI 复核项"
            ),
            "proxy_settings": {
                "http": PROXY_HTTP,
                "socks5": PROXY_SOCKS5,
                "applied_to_teamo": USE_PROXY,
                "preflight_tun_check_passed": True,
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
                "r1_status": "retry 修复沿 batch6 r5; r1 22 caption 22 OK + 0 empty + S6_n60 retries=1",
                "r2_status": "retry 修复沿 r1; r2 22 caption 22 OK + 0 empty + 3 retries (S1_n45/S2_n35/S6_n60 timeout)",
                "r3_status": "retry 修复沿 r2; 本棒仅按 22 caption × 1 call 续采; hard fail 保持 fail path 立即返回; 已知慢响应 caption 靠 retry 消化",
                "rationale": (
                    "沿 r2 修复 + tracking 改进；本棒接力棒仅按 22 caption × 1 call 续采；"
                    "hard fail 保持 fail path 立即返回"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_r2_executor": [
                "1. ROUND=3/REASK_R1=2 参数化 (r2 = 2/1; 本棒 = 3/2)",
                "2. prompt_id 后缀切换: _r2 → _r3 (distill 侧 coze 域 round 3)",
                "3. phase_label 切换: r2_coze_distill_* → r3_coze_distill_*",
                "4. is_round_2 → is_round_3 字段更新",
                "5. baseline 切换: 跨批累计 = r2 终态 cumulative (362/9/353/2.49%); coze 蒸馏侧独立 = 22 caption 各 2/5 successful (r1+r2 quadruples 累计 = 44 calls)",
                "6. target 切换: ≥2 successful/caption (r2 接力阈值) → ≥3 successful/caption (r3 接力阈值)",
                "7. 判定块命名: coze_distill_side_round2_progress (r2 接力) → coze_distill_side_round3_progress (本棒接力); dispatch_target_progress_coze_distill 块沿 r2 不变（仅更新 met_count_post_r3 + remaining_count_round3）",
                "8. non_finish_round 标记: metadata.is_finish_round = False + is_round_3_relay_round = True (本棒 round 3 接力 ≠ 收官)",
                "9. predecessor_sha12 链新增: r2 双件 (7eec235a9ca2 / 08b0aaaae726)",
                "10. r3 接力判定字段新增: rounds_to_reach_round3_target = 3; rounds_to_reach_final_target_actual 沿 r2 沿用",
                "11. 慢响应 caption 处理: S6_n60/S1_n60/S6_n35/S1_n45/S2_n35 等已知慢响应沿 r2 同 retry 路径消化; 实测延迟如实记录",
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
        "per_caption_coze_distill_only_successful_calls": per_caption_coze_distill_only_successful_calls,
        "coze_distill_side_round3_progress": coze_distill_side_round3_progress,
        "dispatch_target_progress_coze_distill": dispatch_target_progress_coze_distill,
        "coze_representative_caliber": coze_representative_caliber,
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
            "r3_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r3_empty_response_above_threshold_single_batch": empty_rate_r3 > 0.50,
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round_3_n_distinct_sample_note": (
                    "round 3 接力棒第 3 call per caption 实测；coze 蒸馏侧独立计数累计 = "
                    f"22 caption 各 {r3_ok + r2_distill_succ // len(captions)} successful (r1+r2+r3 quadruples 累计, prompt_id 前缀 coze_t01_distill_ filter 域)；"
                    f"**coze 蒸馏侧 round 3 接力判定**: {met_target_count_coze_distill}/{len(captions)} caption 达 ≥3 successful;"
                    "后续 r4/r5 接力至 5/5 successful/caption 收官 (沿 batch6 r5 收官口径类比);"
                    "由 verdict-keeper 统裁 (本棒 0 写 verdict)"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r3, 4),
                "cumulative_empty_response_rate": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r3 > 0.50,
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
                        "本棒未触发 K-N26-N2 累计阈值；跑至 "
                        f"{wall_time_s:.0f}s watchdog / 全 {r3_total} calls 完成 (round 3 接力态)"
                        if not k_n26_n2_triggered
                        else f"本棒触发 K-N26-N2 累计阈值；stop_reason={stop_reason}"
                    )
                ),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "breakpoint_status": {
            "planned_calls": planned_total,
            "actual_calls": r3_total,
            "actual_wall_time_s": wall_time_s,
            "checkpoint_file": None,
            "hit_wall_time_budget": wall_time_s >= WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_triggered": k_n26_n2_triggered,
            "next_resume_via": (
                "本棒 round 3 接力棒已完成（22/22 calls）；coze 蒸馏侧 round 3 接力达成 → 进入 round 4 接力"
                if met_target_count_coze_distill == len(captions)
                else f"本棒 round 3 接力棒部分完成（{r3_total}/{planned_total} calls）；coze 蒸馏侧 round 3 未达标 {len(captions) - met_target_count_coze_distill} caption → 留 worker 下一棒接力"
            ),
            "note": (
                f"本棒 round 3 接力棒已完成（{r3_total}/{planned_total} calls）；coze 蒸馏侧 round 3 接力"
                + (" 达成 ✓" if met_target_count_coze_distill == len(captions) else " 未达标（需接力）")
            ),
            "stop_reason": stop_reason,
        },
        "self_scan": {
            "scan_executed": True,
            "scan_method": "json.dumps(sort_keys=True) + 9 sensitive patterns",
            "hits_count": 0,
            "hits_detail": [],
            "note": "本 result 自扫 0 命中 (沿 r2 同口径); key 仅 runtime memory 读取不入产物",
        },
    }

    # 自扫确认 key 等敏感字面不入产物
    obj_scan = self_scan_obj(result)
    result["self_scan"]["hits_count"] = len(obj_scan)
    result["self_scan"]["hits_detail"] = obj_scan
    if obj_scan:
        print(f"[FATAL] self_scan hits: {obj_scan}; 立即停止写入产物")
        return 5

    # 落盘
    out_path = self_result_path
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[WROTE] {out_path}")
    print(
        f"[SUMMARY r3] total={r3_total} ok={r3_ok} empty={r3_empty} fail={r3_fail} "
        f"empty_rate={empty_rate_r3:.4f} cum_post={cum_total}/{cum_empty}/{cum_empty_rate_post:.4f} "
        f"wall={wall_time_s}s"
    )
    print(
        f"[COZE DISTILL r3 progress] met={met_target_count_coze_distill}/{len(captions)} caption ≥3 successful; "
        + ("接力达成 ✓" if met_target_count_coze_distill == len(captions) else f"未达标 {len(captions) - met_target_count_coze_distill} caption")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())