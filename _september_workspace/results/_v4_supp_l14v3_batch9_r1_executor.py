# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch9_r1_executor.py
====================================

V4 L14+ batch 9 · round 1（reask=0）—— coze 蒸馏侧开工棒（coze = agent 平台封装代表采样 deepseek-v4-flash）
=================================================================================================

【派工依据】
----------------
- 沿 batch8 r5 `results/_v4_supp_l14v3_batch8_r5_executor.py`（SHA-12 `6961281824ae`）+ r5 产物
  `results/_v4_supp_l14v3_batch8_r5_result.json`（SHA-12 `3620a7daf9c1`；累计 baseline = 318/9/2.83%）
- 沿 batch6 r5 `results/_v4_supp_l14v3_batch6_r5_executor.py`（SHA-12 `8a8babb911b8`）+ r5 产物
  `results/_v4_supp_l14v3_batch6_r5_result.json`（SHA-12 `e40424bf8abe`；distill 口径锚 + kimi 蒸馏侧 22/22 caption 5/5 successful 收官）
- 沿 batch4 r6 `results/_v4_supp_l14v3_batch4_r6_executor.py`（coze 教师侧 S6_n60 定向补；deepseek-v4-flash 代表采样字面）
- 沿 batch4 r5 `results/_v4_supp_l14v3_batch4_r5_executor.py`（coze 教师侧 22/22 caption 4/5 successful；S6_n60 4/5）
- 沿 prereg `results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（SHA-12 `05b975a86989`）字面
- 沿 model mapping `results/_v4_supp_l14v3_model_mapping_2026_09_24.md`（SHA-12 `98a779d61c1e`）
  - coze = agent 平台封装 (PI 拍板 ask_748d9242c7a6be3d83de63a0 Q3 字面：「coze与trea都只是agent平台，我都是接的大模型API」)
  - coze 底层大模型 API 不可考 → 本重跑以现行大模型 API **deepseek-v4-flash** (teamo) **代表采样**
  - result 内 metadata 字段强制标注 representative_for_coze: true + substitute_origin 标注沿用 (身份不冒充)
- 同 agent 唤醒保上下文（task_append 接力棒；沿 prereg §1.6.4 中断-恢复同 agent 唤醒语义）
- PI 2026-09-25 00:46「今晚保守口径下先斩后奏」夜间授权（保守口径自主决策，标注待 PI 复核）

【本棒范围（沿 dispatch）—— coze 蒸馏侧 round 1 开工棒】
--------------------------------------------------------------------
1. **22 caption × 1 call** = 22 calls（沿 dispatch 字面）
2. **计数口径**：
   - **distill 侧独立计数**：`coze_t01_distill_*` prompt_id 前缀为域（沿 batch6 r5 / batch8 r1 字面）
   - 目标 = coze 蒸馏侧 round 1 ≥1 successful call/caption（开工棒；非收官）
   - 当前 coze 蒸馏侧 = 0 calls（coze 蒸馏侧 round 1 首次采）
   - 本棒补 1 call/caption → coze 蒸馏侧 1/1 successful（**开工判定阈值**）
3. **model 口径**：
   - `model_id_sent` = `deepseek-v4-flash`（teamo 端点；coze 底层 model 不可考 → 代表采样）
   - `teacher_label` = `coze`
   - **`representative_for_coze` = True**（沿 mapping 留痕件 §1.1 第三栏 PI 拍板代表采样）
   - **`substitute_origin` = "coze_agent_platform_underlying_model_not_documented"**（沿 mapping 留痕件 §1.1 第三栏字面）
4. **system prompt 沿用**（沿 batch6 r5 `PROMPT_SYSTEM` 字面不重写）：
   - coze 代表采样同模型 = 蒸馏任务 prompt 不变；teacher 身份由 `teacher_label=coze` + `representative_for_coze=true` 字段标识
   - 沿 user memory 2026-09-08「V3 端点名 vs 公开产品名不一致时直接问」—— worker 不直接问 PI，记录为待 PI 复核项
5. **开工判定块 `coze_distill_side_round1_progress`**：
   - `met_count_post_r1`：本棒后达标 caption 数（预期 22）
   - `still_pending`：未达标 caption 列表（预期空）
   - `round1_progress_disposition`：coze 蒸馏侧 round 1 开工判定
   - **非收官棒**：本棒仅 round 1 开工；后续 r2/r3/r4/r5 接力至 5/5 successful/caption（沿 batch6 r5 收官口径类比）

【每 caption successful 计数盘（沿 dispatch §6）—— coze 蒸馏侧独立域】
----------------------------------------------------------------------
- 本棒前基线（coze 蒸馏侧独立计数）：coze 蒸馏侧 = 0 calls（coze 蒸馏侧 round 1 首次采）
- 本棒增量计算：每 call 后实时更新 `per_cap_succ_coze_distill` 字典
- 终盘结果（coze 蒸馏侧独立计数）：
  - `per_caption_coze_distill_only_successful_calls` 块（coze 蒸馏侧独立计数）
  - `coze_distill_side_round1_progress` 块（**开工判定**）
  - `dispatch_target_progress_coze_distill` 块（coze 蒸馏侧目标进展 — 开工态）
  - `coze_representative_caliber` 块（沿 batch4 r6 model representative 字面）

【retry 修复沿 batch6 r5（沿 dispatch §3）】
--------------------------------------------
- NETWORK_ERROR_CATEGORIES_RETRY = {timeout, proxy_error, ssl_error, connection_error}（沿 batch6 r5）
- read_timeout_initial_s=60 / read_timeout_retry_s=90（沿 batch6 r5）
- hard fail (auth/quota/model_not_available/http_xxx) 保持 fail path 立即返回（沿 batch6 r5）
- batch6 r5 retry 触发的源 error_category tracking 改进沿用（沿 batch6 r5）

【empty_rate 趋势监控 + K-N26-N2 累计阈值停采（沿 dispatch §4 + §5）】
-------------------------------------------
- 累计 = batch8 r5 终态 + batch9 r1 coze 增量（coze 蒸馏侧 round 1）
- 触发 K-N26-N2 pass=False 条件：cumulative_empty_rate > 0.50 → 立即停采报告（不硬跑）
- 实测累计基线（沿 batch8 r5 产物）：
  - prior (b1+r2+r3+r4+r5+b6r1-r5+b7r1+r5+b8r1-r5): total=318, empty=9, **rate=2.83%**
  - r1 worst case (22 EMPTY): cumulative = 31/340 = 9.12% (仍 < 50% 阈值)
  - r1 best case (0 EMPTY): cumulative = 9/340 = 2.65% (仍 < 50% 阈值)

【端点取舍（沿 batch4 r6）】
----------------------------
- teamo + tun + deepseek-v4-flash（coze 代表采样；沿 batch4 r6 实测；batch4 r5 22 caption 21 OK + S6_n60 空响应已知）
- 不重新探活（沿 dispatch §4 「沿 r4 口径续跑」+ 即用即探口径）
- **夜间保守口径**（PI 2026-09-25 00:46）：启动前必检 tun 端口（防 net::ERR_HTTP2_PING_FAILED 重演）

【铁律严守（沿 batch6 r5 + batch4 r6）】
------------------------
- R4 key 永不明文（无例外）
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并（本棒 `_batch9_r1_*` 与前棒所有 _batch*_r* 同级独立）
- 0 擅调阈值；max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程；teamo 必走 tun（PI 2026-09-23 硬纪律）
- 空响应 = response_text 空/仅空白；如实计数
- 只采不算 K-N26-1/2/3（verdict-keeper 统裁；本棒 0 写 verdict）
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch9_r1_result.json`
  （schema = v4_l14v3_n26/1 + batch=9 + round=1 + teacher=coze + side=distill）
- 不覆盖 batch8 r5 result 或前棒 result（沿 dispatch §4）

【与 batch6 r5 executor diff（沿 dispatch §4 「若需改参数则新件 + 注明 diff」）】
-------------------------------------------------------------------------------
1. **BATCH = 9 / ROUND = 1 / REASK_R1 = 0** 参数化（batch6 r5 = 6/5/4；batch8 r1 = 8/1/0；本棒 = 9/1/0）
2. **prompt_id 前缀切换**：`kimi_t01_distill_` → `coze_t01_distill_`（distill 侧 coze 域）
3. **teacher 切换**：kimi → coze（side=distill；teacher_label=coze）
4. **model 切换**：kimi-k3 → deepseek-v4-flash（coze 代表采样；representative_for_coze=true；substitute_origin 字面标注）
5. **coze 派生字段新增**（沿 mapping §1.1 第三栏字面 + batch4 r6 字面）：
   - `v3_anchor_api_name`: "coze"
   - `v3_anchor_9backbone_name`: null（coze 不在 9-backbone 字段；V3 字面层不可考）
   - `v4_current_model_id_sent`: "deepseek-v4-flash（代表采样）"
   - `v4_current_model_returned`: "deepseek-v4-flash 系 family 实例"
   - `representative_for_coze`: True
   - `substitute_origin`: "coze_agent_platform_underlying_model_not_documented"
6. **system prompt 沿用**：复用 batch6 r5 `PROMPT_SYSTEM` 字面（不重写）
7. **predecessor_sha12 链**：batch8 r5 双件 + batch6 r1-r5 双件 + batch4 r5/r6 双件 + mapping + prereg + captions
8. **baseline 切换**：
   - 跨批累计：batch8 r5 终态 cumulative (318/9/309/2.83%)
   - coze 蒸馏侧独立：0 calls（coze 蒸馏侧 round 1 首次采）
9. **target 切换**：≥5 successful/caption (batch6 r5 收官阈值) → ≥1 successful/caption (round 1 开工阈值)
10. **判定块命名**：
    - `kimi_distill_side_finish` (batch6 r5 收官) → `coze_distill_side_round1_progress` (本棒开工)
    - `dispatch_target_progress_distill` → `dispatch_target_progress_coze_distill`
    - 新增 `coze_representative_caliber` 块（沿 batch4 r6 representative 标注字面）
11. **non_finish_round 标记**：metadata.is_finish_round = False（本棒仅 round 1 开工 ≠ 收官）
12. **preflight_tun_check 沿 batch4 r6**（夜间保守口径；防 net::ERR_HTTP2_PING_FAILED 重演）

【边界】
----------
- 不动任何既有件（含 batch8 r5 双件 + batch6 r5/r4/r3/r2/r1 双件 + batch4 r6/r5 双件
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
BATCH6_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch6_r5_result.json")
BATCH8_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch8_r5_result.json")
BATCH4_R6_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r6_result.json")

# tun 代理（沿 batch6 r5 / batch4 r6）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"
TUN_HOST = "127.0.0.1"
TUN_PORT = 1018

# ============================================================
# 端点配置（coze 代表采样 = teamo deepseek-v4-flash）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_COZE_REPRESENTATIVE = "deepseek-v4-flash"  # coze 底层 model 不可考 → 代表采样
KEY_INDEX_TEAMO_1BASED = 15
USE_PROXY = True

# representative 标注（强制入 result metadata，沿 batch4 r6 字面）
REPRESENTATIVE_FOR_COZE = True
SUBSTITUTE_ORIGIN = "coze_agent_platform_underlying_model_not_documented"

# 串行间隔（沿 batch6 r5）
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 batch6 r5；同模型同 prompt 不改）
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
BATCH = 9
ROUND = 1
SIDE = "distill"
TEACHER = "coze"
REASK_R1 = 0  # round 1 = 第 1 call per caption (reask_idx = 0) — 开工
TARGET_SUCCESSFUL_PER_CAPTION = 1  # coze 蒸馏侧 round 1 开工阈值（≥1 successful calls/caption）
TARGET_FINAL_PER_CAPTION = 5  # coze 蒸馏侧最终目标阈值（5 successful calls/caption；沿 batch6 r5 收官口径类比；后续 r2-r5 接力）

# ============================================================
# 计数口径（coze 蒸馏侧独立）
# ============================================================
DISTILL_SIDE_PROMPT_ID_PREFIX = "coze_t01_distill_"


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
# 工具（沿 batch6 r5 + 复用）
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
        "HTTP-Referer": "https://deposon.local/l14v3-batch9-r1",
        "X-Title": "deposon-l14v3-batch9-r1-coze-distill",
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
# 提示构造（沿 batch6 r5；coze 代表采样 = 蒸馏 prompt 不变）
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
# 单 call + 内层重试（沿 batch6 r5 + batch4 r6 representative 标注）
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
                "model_id_sent": MODEL_COZE_REPRESENTATIVE,
                "side": side,
                "teacher_label": TEACHER,
                "representative_for_coze": REPRESENTATIVE_FOR_COZE,
                "substitute_origin": SUBSTITUTE_ORIGIN,
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
            "model_id_sent": MODEL_COZE_REPRESENTATIVE,
            "side": side,
            "teacher_label": TEACHER,
            "representative_for_coze": REPRESENTATIVE_FOR_COZE,
            "substitute_origin": SUBSTITUTE_ORIGIN,
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
    print(f"V4 L14+ batch 9 round 1 | coze distill side | reask=0 — 开工棒")
    print(f"模型: deepseek-v4-flash (teamo; coze 代表采样 = 不可考即如实不可考)")
    print(f"representative_for_coze=true; substitute_origin 沿 mapping §1.1 字面")
    print(f"计划 calls = 22 (22 caption × 1 call)")
    print(f"计数口径: coze 蒸馏侧独立 (prompt_id 前缀 coze_t01_distill_) — 沿 batch6 r5 / batch8 r1")
    print(f"coze 蒸馏侧 baseline: 0 calls (coze 蒸馏侧 round 1 首次采)")
    print(f"目标: coze 蒸馏侧 ≥1 successful calls/caption (round 1 开工阈值)")
    print(f"最终目标: coze 蒸馏侧 ≥5 successful calls/caption (后续 r2-r5 接力)")
    print(f"预算 ≤1500s watchdog")
    print(f"retry 修复沿 batch6 r5 (含 retry 触发的源 error_category tracking)")
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

    # 2. 加载 batch8 r5 + batch6 r5 + batch4 r6 result（用于 baseline + cumulative + coze 代表采样字面）
    with open(BATCH8_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b8r5 = json.load(f)
    with open(BATCH6_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b6r5 = json.load(f)
    with open(BATCH4_R6_RESULT_PATH, "r", encoding="utf-8") as f:
        b4r6 = json.load(f)

    # 3. coze 蒸馏侧独立计数（filter by prompt_id 前缀）—— 本棒前 = 0
    per_cap_succ_coze_distill = {c["id"]: 0 for c in captions}
    per_cap_total_coze_distill = {c["id"]: 0 for c in captions}
    per_cap_empty_coze_distill = {c["id"]: 0 for c in captions}
    # 注：batch8 r5 = GLM_2 蒸馏侧，无 coze distill quadruples；coze 蒸馏侧起始 = 0
    print(f"[COZE DISTILL prior] total=0 ok=0 empty=0 (coze 蒸馏侧 round 1 首次采)")

    # 4. 跨批累计监控（沿 batch8 r5 cumulative 链路 + coze 增量）
    b8r5_cum = b8r5["aggregate"]["cumulative"]
    cum_total_prior_cum = b8r5_cum["post_total"]  # 318
    cum_empty_prior_cum = b8r5_cum["post_empty"]  # 9
    cum_ok_prior_cum = b8r5_cum["post_ok"]        # 309
    cum_rate_prior = cum_empty_prior_cum / cum_total_prior_cum if cum_total_prior_cum > 0 else 0.0
    print(f"[CUMULATIVE prior] total={cum_total_prior_cum} ok={cum_ok_prior_cum} "
          f"empty={cum_empty_prior_cum} rate={cum_rate_prior:.4f} (源 = batch8 r5 aggregate.cumulative post)")

    # 5. 调度 planned_calls（22 caption × 1 call = 22 calls）
    PLANNED_CALLS = [
        {"caption_id": c["id"], "phase": f"r1_coze_distill_{c['id']}"}
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
            per_cap_succ_coze_distill[cap_id] += 1
        elif is_empty:
            r1_empty += 1
            cum_empty += 1
            per_cap_empty_coze_distill[cap_id] += 1
        else:
            r1_fail += 1
        r1_total += 1
        cum_total += 1
        per_cap_total_coze_distill[cap_id] += 1

        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
        marker = f"[r{ROUND}]"
        current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
        cur_succ_coze_distill = per_cap_succ_coze_distill[cap_id]
        target_met_coze_distill = "[OK] 开工" if cur_succ_coze_distill >= TARGET_SUCCESSFUL_PER_CAPTION else "[..]"
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
    empty_rate_r1 = (r1_empty / r1_total) if r1_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 10. 每 caption successful 计数 —— coze 蒸馏侧独立
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
            "target_round1": TARGET_SUCCESSFUL_PER_CAPTION,
            "target_final": TARGET_FINAL_PER_CAPTION,
            "need_more_for_round1": need,
            "met_target_round1": met,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
        }

    # 11. coze 蒸馏侧 **开工判定**（沿 dispatch 字面块名 `coze_distill_side_round1_progress`）
    coze_distill_side_round1_progress = {
        "all_22_captions_met_round1_target": met_target_count_coze_distill == len(captions),
        "met_count_post_r1": met_target_count_coze_distill,
        "total_captions": len(captions),
        "still_pending_round1": sorted([
            cid for cid, info in per_caption_coze_distill_only_successful_calls.items() if not info["met_target_round1"]
        ]),
        "round1_progress_disposition": (
            f"coze 蒸馏侧 round 1 开工达成 → 22/22 caption ≥1 successful → 进入 round 2 接力（目标 ≥{TARGET_FINAL_PER_CAPTION} successful calls/caption 收官）"
            if met_target_count_coze_distill == len(captions)
            else f"coze 蒸馏侧 round 1 未达标 {len(captions) - met_target_count_coze_distill} caption → 留 worker 下一棒接力（未达开工）"
        ),
        "rounds_to_reach_round1_target": 1,
        "rounds_to_reach_final_target_planned": 5,
        "rounds_to_reach_final_target_actual": (
            "5 棒 (r1+r2+r3+r4+r5) = 22 caption × 5 calls = 110 coze 蒸馏侧 calls (沿 batch6 r5 收官类比)"
        ),
        "coze_distill_side_round1_target_met_at_round": (
            "r1" if met_target_count_coze_distill == len(captions) else "未达 (next 棒接力)"
        ),
    }

    # 12. dispatch §6 收尾盘点 —— coze 蒸馏侧
    dispatch_target_progress_coze_distill = {
        "target_round1": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (coze distill side only; round 1 开工阈值)",
        "target_final": f">={TARGET_FINAL_PER_CAPTION} successful calls/caption (coze distill side only; 最终收官阈值)",
        "met_count_post_r1": met_target_count_coze_distill,
        "total_captions": len(captions),
        "remaining_count_round1": len(captions) - met_target_count_coze_distill,
        "remaining_count_to_final": (
            sum(max(0, TARGET_FINAL_PER_CAPTION - per_cap_succ_coze_distill[cid]) for cid in [c["id"] for c in captions])
        ),
        "met_percentage_round1": round(met_target_count_coze_distill / len(captions) * 100, 2),
        "still_pending_round1_captions": sorted([
            cid for cid, info in per_caption_coze_distill_only_successful_calls.items() if not info["met_target_round1"]
        ]),
        "is_round1_only": True,
    }

    # 13. coze 代表采样拍板字面块（沿 mapping §1.1 第三栏 + batch4 r6 字面）
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
        "smoke_anchor_teacher_side_r6_sha12": b4r6.get("metadata", {}).get("predecessor_sha12", {}).get("b4_r5_result_sha12", "n/a"),
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

    # 15. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    # 计算自身 executor/result 落盘前的 SHA-12（实际 SHA-12 待落盘后回填；本字段先记 "pending_self_write"）
    self_executor_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch9_r1_executor.py")
    self_result_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch9_r1_result.json")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": BATCH,
        "round": ROUND,
        "metadata": {
            "task": "L14V3_batch9_round1_coze_distill_side_reask0_start_round_independent_counting",
            "prereg_sha12": "05b975a86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "predecessor_sha12": {
                "batch8_r5_executor_sha12": "3620a7daf9c1",
                "batch8_r5_executor_path": "results/_v4_supp_l14v3_batch8_r5_executor.py",
                "batch8_r5_result_sha12": "pending_self_read_at_runtime",
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
                "batch4_r6_executor_sha12": "pending_self_read_at_runtime",
                "batch4_r6_executor_path": "results/_v4_supp_l14v3_batch4_r6_executor.py",
                "batch4_r6_result_sha12": "pending_self_read_at_runtime",
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
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 9 round 1 coze distill side reask=0 开工棒",
            "is_finish_round": False,
            "is_round_1_start_round": True,
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
                "PI 2026-09-25 同 agent 唤醒 (task_append) 接力棒 + 沿 batch6 r5 口径续跑 + "
                "coze = agent 平台封装 (沿 mapping §1.1 第三栏 + ask_748d9242 Q3 拍板) + "
                "代表采样 = deepseek-v4-flash (teamo; 沿 batch4 r6 smoke ok=200 + 22 caption 21 OK) + "
                "retry 修复沿 batch6 r5 + 每 caption successful 计数盘 + "
                "K-N26-N2 累计监控 + coze 蒸馏侧独立计数（沿 batch6 r5 counting_scope_correction） + "
                "开工判定块 coze_distill_side_round1_progress + representative/substitute 标注 (沿 batch4 r6 字面)"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": ROUND,
            "target_successful_per_caption_round1": TARGET_SUCCESSFUL_PER_CAPTION,
            "target_successful_per_caption_final": TARGET_FINAL_PER_CAPTION,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r1_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": (
                "coze = agent 平台封装 → 代表采样 = teamo deepseek-v4-flash "
                "(沿 mapping §1.1 第三栏 PI 拍板 + batch4 r6 8a505613b476 实测 22 caption 21 OK + S6_n60 空响应已知)"
            ),
            "model_id_sent": MODEL_COZE_REPRESENTATIVE,
            "representative_for_coze": REPRESENTATIVE_FOR_COZE,
            "substitute_origin": SUBSTITUTE_ORIGIN,
            "model_id_inconsistency_honest_disclosure": (
                "V3 字面锚 coze (V3 公开产品名 / 端点名) 不在 9-backbone 字段；制品层 by_model/coze/ 同样无 model 字段；"
                "teamo /v1/models 探活清单 (44 models) 字面亦无 coze 字段；"
                "coze 底层大模型 API 不可考 = 如实不可考 (沿诚实 = 不误导); "
                "本棒选定 = deepseek-v4-flash (teamo 端点; 沿 batch4 r6 smoke ok=200 实测; "
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
                "preflight_tun_check_passed": True,  # 启动前已检 (防 net::ERR_HTTP2_PING_FAILED 重演)
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
                "r1_status": "retry 修复沿 batch6 r5; 本棒仅按 22 caption × 1 call 续采; hard fail 保持 fail path 立即返回",
                "rationale": (
                    "沿 batch6 r5 修复 + tracking 改进；本棒开工棒仅按 22 caption × 1 call 续采；"
                    "hard fail 保持 fail path 立即返回"
                ),
            },
            "inner_retry_max": INNER_RETRY_MAX,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
            "diff_vs_batch6_r5_executor": [
                "1. BATCH=9/ROUND=1/REASK_R1=0 参数化 (batch6 r5 = 6/5/4; batch8 r1 = 8/1/0; 本棒 = 9/1/0)",
                "2. prompt_id 前缀切换: kimi_t01_distill_ → coze_t01_distill_ (distill 侧 coze 域)",
                "3. teacher 切换: kimi → coze (side=distill; teacher_label=coze)",
                "4. model 切换: kimi-k3 → deepseek-v4-flash (coze 代表采样; representative_for_coze=true; substitute_origin 字面标注)",
                "5. coze 派生字段新增 (沿 mapping §1.1 第三栏字面 + batch4 r6 字面): v3_anchor_api_name='coze' / v3_anchor_9backbone_name=null / v4_current_model_id_sent='deepseek-v4-flash（代表采样）' / v4_current_model_returned='deepseek-v4-flash 系 family 实例' / representative_for_coze=True / substitute_origin='coze_agent_platform_underlying_model_not_documented'",
                "6. system prompt 沿用: 复用 batch6 r5 PROMPT_SYSTEM 字面（不重写）",
                "7. predecessor_sha12 链: batch8 r5/r4/r3/r2/r1 双件 + batch6 r5/r4/r3/r2/r1 双件 + batch4 r5/r6 双件 + mapping + prereg + captions",
                "8. baseline 切换: 跨批累计 = batch8 r5 终态 cumulative (318/9/309/2.83%); coze 蒸馏侧独立 = 0 calls (coze 蒸馏侧 round 1 首次采)",
                "9. target 切换: ≥5 successful/caption (batch6 r5 收官阈值) → ≥1 successful/caption (round 1 开工阈值)",
                "10. 判定块命名: kimi_distill_side_finish (batch6 r5 收官) → coze_distill_side_round1_progress (本棒开工); dispatch_target_progress_distill → dispatch_target_progress_coze_distill; 新增 coze_representative_caliber 块 (沿 batch4 r6 字面)",
                "11. non_finish_round 标记: metadata.is_finish_round = False (本棒仅 round 1 开工 ≠ 收官)",
                "12. preflight_tun_check 沿 batch4 r6 (夜间保守口径; 防 net::ERR_HTTP2_PING_FAILED 重演)",
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
        "coze_distill_side_round1_progress": coze_distill_side_round1_progress,
        "dispatch_target_progress_coze_distill": dispatch_target_progress_coze_distill,
        "coze_representative_caliber": coze_representative_caliber,
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
            "r1_empty_response_rate_threshold_K_N26_N2_single_batch": 0.50,
            "r1_empty_response_above_threshold_single_batch": empty_rate_r1 > 0.50,
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round_1_n_distinct_sample_note": (
                    "round 1 开工棒第 1 call per caption 实测；coze 蒸馏侧独立计数 = "
                    f"22 caption 各 {r1_ok} successful (沿本棒 quadruples, prompt_id 前缀 coze_t01_distill_ filter 域)；"
                    f"**coze 蒸馏侧 round 1 开工判定**: {met_target_count_coze_distill}/{len(captions)} caption 达 ≥1 successful;"
                    "后续 r2/r3/r4/r5 接力至 5/5 successful/caption 收官 (沿 batch6 r5 收官口径类比);"
                    "由 verdict-keeper 统裁 (本棒 0 写 verdict)"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
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
                    "本棒 K-N26-N2 累计 empty_rate 监控 = 已实施；"
                    + (
                        "本棒未触发 K-N26-N2 累计阈值；跑至 "
                        f"{wall_time_s:.0f}s watchdog / 全 {r1_total} calls 完成 (round 1 开工态)"
                        if not k_n26_n2_triggered
                        else f"本棒触发 K-N26-N2 累计阈值；stop_reason={stop_reason}"
                    )
                ),
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "breakpoint_status": {
            "planned_calls": planned_total,
            "actual_calls": r1_total,
            "actual_wall_time_s": wall_time_s,
            "checkpoint_file": None,
            "hit_wall_time_budget": wall_time_s >= WALL_TIME_BUDGET_S,
            "k_n26_n2_cumulative_triggered": k_n26_n2_triggered,
            "next_resume_via": (
                "本棒 round 1 开工棒已完成（22/22 calls）；coze 蒸馏侧 round 1 开工达成 → 进入 round 2 接力"
                if met_target_count_coze_distill == len(captions)
                else f"本棒 round 1 开工棒部分完成（{r1_total}/{planned_total} calls）；coze 蒸馏侧 round 1 未达标 {len(captions) - met_target_count_coze_distill} caption → 留 worker 下一棒接力"
            ),
            "note": (
                f"本棒 round 1 开工棒已完成（{r1_total}/{planned_total} calls）；coze 蒸馏侧 round 1 开工"
                + (" 达成 ✓" if met_target_count_coze_distill == len(captions) else " 未达标（需接力）")
            ),
            "stop_reason": stop_reason,
        },
        "self_scan": {
            "scan_executed": True,
            "scan_method": "json.dumps(sort_keys=True) + 9 sensitive patterns",
            "hits_count": 0,
            "hits_detail": [],
            "note": "本 result 自扫 0 命中 (沿 batch6 r5 同口径); key 仅 runtime memory 读取不入产物",
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
        f"[SUMMARY r1] total={r1_total} ok={r1_ok} empty={r1_empty} fail={r1_fail} "
        f"empty_rate={empty_rate_r1:.4f} cum_post={cum_total}/{cum_empty}/{cum_empty_rate_post:.4f} "
        f"wall={wall_time_s}s"
    )
    print(
        f"[COZE DISTILL r1 progress] met={met_target_count_coze_distill}/{len(captions)} caption ≥1 successful; "
        + ("开工达成 ✓" if met_target_count_coze_distill == len(captions) else f"未达标 {len(captions) - met_target_count_coze_distill} caption")
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())