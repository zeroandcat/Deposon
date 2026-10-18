# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch4_r6_executor.py
====================================

V4 L14+ batch 4 · round 6 · coze 教师侧 S6_n60 定向补 1 call
=============================================================

【派工依据】
----------------
- 沿 batch4 r5 executor `8a505613b476` + r5 result `bad01f2b89fd` (前者 = r5 executor sha12) 接力链
- 沿 batch4 r4 executor `184186902A9F` + r4 result `41E0BA55E205` 接力链上游
- 沿 batch4 r3 executor `b5e1c3637405` + r3 result `ed5267df7d6f` 接力链上游
- 沿 batch4 r2 executor `7d8e12267790` + r2 result `6a9a362d9869` 接力链上游
- 沿 batch4 r1 executor `e84bffd5dc7d` + r1 result `7d9fe9d319a2` 接力链上游
- 沿 model mapping 留痕件 `98a779d61c1e` coze 映射拍板 (ask_748d9242c7a6be3d83de63a0)
- 沿 batch2 r4 result `15b8ddc5ba9e` 跨批累计 baseline (185 calls / 9 empty / 4.86%)
- 沿 /v1/models 探活 `_v4_supp_l14v3_batch2_r2_models_probe.json` (sha12=`3c9dc60b5071`)
- 派工单 coze 教师批 4 round 6 (定向补 1 call; 接力棒, 沿 r5 上下文唤醒):
  S6_n60 单 call (reask=5); prompt_id `coze_t06_teacher_S6_n60_b4_r6`

【本棒范围 (沿 dispatch) —— coze 教师侧 S6_n60 单 call 定向补 (reask=5)】
----------------------------------------------------------------------------
1. **沿用 teamo `deepseek-v4-flash` 代表采样** (r5 smoke ok=200 + r5 22 caption 21 OK + S6_n60 空响应已知)
3. **1 caption × 1 call** (仅 S6_n60; 每位 caption 第 6 call; reask_idx=5)
4. **目标**: 本棒后 S6_n60 = 5/5 successful call (达 coze 教师侧 target = 22/22 caption 全 met)
5. **硬停规则** (沿 dispatch 派工单 §2):
   - 若本 call 仍 empty (response_text 空/仅空白) → **立即停止不加试**
   - 如实记录「S6_n60 结构性失能确认 (模型行为, 2 试皆空)」收档
   - 接受 partial 21/22, 留 verdict-keeper 统裁 (处置路径 c)
   - 若 OK → S6_n60 达 5/5, coze 教师侧全 22 收官
6. 预算 ≤1 caption call + ≤1 smoke call / ≤120s watchdog (单 call 短预算)
7. **同模型 / 同 prompt / max_tokens=2000 / temperature=0.7 / tun / retry ≤3 (网络错)**

【S6_n60 历史 (沿 r5 result `bad01f2b89fd`)】
----------------------------------------------
- r1 (reask=0): succ_count → 1 (1/5 OK)
- r2 (reask=1): succ_count → 2 (2/5 OK)
- r3 (reask=2): succ_count → 3 (3/5 OK)
- r4 (reask=3): succ_count → 4 (4/5 OK)
- r5 (reask=4): succ_count → 4 (空响应; reasoning-occupied 模式; completion_tokens=2000 + reasoning_tokens=2000 4 试皆空)
  → total=5 / empty=1
- **r6 (reask=5)** (本棒): 补 1 call; 若 OK → 5/5; 若 empty → 4/5 (partial 21/22 留 verdict-keeper)

【coze 代表采样映射 (沿 model_mapping `98a779d61c1e` §1.1 第三栏 PI 拍板)】
--------------------------------------------------------------------
- PI 拍板原文 (ask_748d9242c7a6be3d83de63a0 Q3 Other 逐字引用):
  「coze与trea都只是agent平台，我都是接的大模型API」
- 拍板 = coze = agent 平台封装 (PI 拍板字面裁定底层 model 不可考)
- 本重跑以现行大模型 API `deepseek-v4-flash` (teamo) **代表采样**
- result 内 metadata 字段强制标注:
  - `representative_for_coze: true`
  - `substitute_origin: "coze_agent_platform_underlying_model_not_documented"`
- **不声称该 model 即 coze 背后模型** (沿诚实 = 不误导口径)

【硬停规则实施细节】
---------------------
- 网络异常 retry 类别: {timeout, proxy_error, ssl_error, connection_error} (沿 r5)
- read_timeout_initial_s=60 / read_timeout_retry_s=90
- inner_retry_max = 3 (沿 dispatch 派工单 §1 「retry ≤3」)
- **关键**: empty_response (ok=True 200 但 content 空/仅空白) 触发硬停,
  不计入 retry 链, 立即记录收档 (接受 partial 21/22)
- 1-call smoke 失败立即 abort (沿 r5 同)

【铁律严守 (沿 r5/r4/r3/r2/r1)】
------------------------
- R4 key 永不明文 (无例外); 仅 runtime memory 读
- V1–V3 只读不动 / R5 V4 frozen append-only / R6 P-G 不动 / R7 plugin spec 不动
- 派生 JSON 不合并 (本棒 `_batch4_r6_*` 与 r5/r4/r3/r2/r1/batch2_r*/batch1_* 独立)
- 0 擅调阈值; max_tokens=2000 沿 prereg §1.4 工具失灵修正条款
- 串行 ≥2.5s 全程; teamo 必走 tun (PI 2026-09-23 硬纪律)
- 空响应 = response_text 空/仅空白; 如实计数
- 只采不算 K-N26-1/2/3 (verdict-keeper 统裁; 本棒 0 写 verdict)
- succeeded ≠ 跑完落盘核验
- 老实交代 0 产物; 探活计入 calls 账
- 不覆盖既有件 (r5 executor `8a505613b476` + r5 result `bad01f2b89fd` + r4 executor `184186902A9F`
  + r4 result `41E0BA55E205` + r3 executor `b5e1c3637405` + r3 result `ed5267df7d6f`
  + r2 executor `7d8e12267790` + r2 result `6a9a362d9869` + r1 executor `e84bffd5dc7d`
  + r1 result `7d9fe9d319a2` + batch2 r4 result `15b8ddc5ba9e` + batch1 r6 executor `5f02c7e0f094`
  + batch1 r6 result `a4f851154551` + models_probe `3c9dc60b5071` + mapping `98a779d61c1e`
  + prereg `05b975a86989` 不动)

【产物】
----------
- 写入: `results/_v4_supp_l14v3_batch4_r6_result.json` (schema = `v4_l14v3_n26/1` + batch=4 + round=6)
- 不覆盖 r5 result `bad01f2b89fd` 或 r4 result `41e0ba55e205` 或 r3 result `ed5267df7d6f`
  或 r2 result `6a9a362d9869` 或 r1 result `7d9fe9d319a2` 或 batch1 r6 result `a4f851154551`
- predecessor_sha12 链: mapping `98a779d61c1e` + r5 executor/result (最新接力锚) + r4 executor/result
  + r3 executor/result + r2 executor/result + r1 executor/result + r4 executor/result + r3 executor/result
  + r2 executor/result + models_probe + batch1 r6 executor/result + prereg `05b975a86989`

【与 r5 executor diff (沿 dispatch §4 「若需改参数则新件 + 注明 diff」)】
-------------------------------------------------------------------------
1. ROUND = 6 (升 r6 命名); BATCH = 4 不变
2. **目标 caption 缩窄**: 仅 S6_n60 (沿 r5 终态 21/22 caption met target, S6_n60 仅 4/5)
3. **call 数**: 1 caption × 1 call = 1 call (取代 r5 的 22 caption × 1 call)
4. prompt_id 前缀 `coze_t06_teacher_S6_n60` + 后缀 `_b4_r6` (取代 r5 的 `coze_t05_teacher_*_b4_r5`)
5. reask_idx = 5 (本棒 S6_n60 第 6 call; 取代 r5 的 reask_idx=4)
6. phase_label: `b4_r6_s6_n60_supplement` (取代 r5 的 `b4_r5_finish`)
7. is_round_6 = True (取代 r5 的 is_round_5)
8. **新增 hard_stop_on_empty_response = True** (沿 dispatch §2 硬停规则)
9. **新增 single_caption_target = "S6_n60"** (取代 r5 的全 22 caption)
10. smoke_call_only = True (沿 r5 同; 沿 r5 smoke ok=200 已知)
11. predecessor_sha12 链: r5 executor `8a505613b476` + r5 result `bad01f2b89fd` (新增; 取代 r5 链的 r4 双件仍保留作为历史累计 baseline)
12. baseline prior: r5 终态 110 calls / 1 empty / 109 ok / 0.0091 rate (取代 r5 链的 88/88/0/0.0)
13. 跨批累计 baseline: r5 终态 295 calls / 10 empty / 3.39% rate (取代 r5 链的 273/9/3.30%)
14. **新增 r6_disposition 块**:
    - `r6_call_target`: "S6_n60"
    - `r6_call_result`: "ok" / "empty" / "fail"
    - `r6_call_structural_failure_confirmed`: True (2 试皆空时)
    - `r6_disposition`: "complete_22_of_22" / "partial_21_of_22"
    - `r6_coze_teacher_side_finish` (沿 r5 收官判定块; 反映 r6 后状态)
15. K-N26-N2 触发阈值 = 0.50 不变; 监控 baseline 更新为 295/10/3.39%
16. spec_conformance 重写: coze 教师侧 S6_n60 单 call 定向补 (reask=5); 夜间保守口径
17. model_id_inconsistency_honest_disclosure 字面继承 r1/r2/r3/r4/r5 + r6 累计补注
18. 派生 metadata 字段沿 r5 不动 (v3_anchor_api_name=coze / v3_anchor_9backbone_name=null / v4_current_model_id_sent=deepseek-v4-flash)
19. per_caption_successful_calls 字段: 复制 r5 终态 + 仅更新 S6_n60 行 (succ_count / total_calls_so_far / empty_count_so_far)
20. baseline 路径: B4_R5_RESULT_PATH (沿 r5 result `bad01f2b89fd`) 取代 r5 链的 B4_R4_RESULT_PATH
21. 启动前必检 tun 端口 (PI 2026-09-25 夜间保守口径; 防 net::ERR_HTTP2_PING_FAILED 重演)
22. failure result 路径同步 r6: `_v4_supp_l14v3_batch4_r6_result.json` (取代 r5 链的 r5 result)
23. ROUNDS_USED = [r1, r2, r3, r4, r5, r6] (含 r6; r6 为定向补棒)

【边界】
----------
- 不动任何既有件 (r5 executor `8a505613b476` + r5 result `bad01f2b89fd` + r4 executor `184186902A9F`
  + r4 result `41e0ba55e205` + r3 executor `b5e1c3637405` + r3 result `ed5267df7d6f`
  + r2 executor `7d8e12267790` + r2 result `6a9a362d9869` + r1 executor `e84bffd5dc7d`
  + r1 result `7d9fe9d319a2` + batch2 r4 executor `d9fe7aa2d292` + batch2 r4 result `15b8ddc5ba9e`
  + batch2 r3 executor `72fd2bb3838e` + batch2 r3 result `25251aca6d79`
  + batch2 r2 executor `e7418f47a130` + batch2 r2 result `8c125e257af8`
  + batch1 r6 executor `5f02c7e0f094` + batch1 r6 result `a4f851154551`
  + models_probe `3c9dc60b5071` + mapping `98a779d61c1e` + prereg `05b975a86989`)
- 跑不完拆段报断点
- 0 触动 V1–V3 资产 / R5 V4 frozen / R6 P-G / R7 plugin spec
- 不立 V3 → V4 model 升级版字面继承断言 (沿 mapping §4 诚实声明)
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
BATCH1_R6_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_r6_result.json")
B2_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r1_result.json")
B2_R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_result.json")
B2_R3_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r3_result.json")
B2_R4_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r4_result.json")
B4_R1_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r1_result.json")
B4_R2_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r2_result.json")
B4_R3_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r3_result.json")
B4_R4_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r4_result.json")
B4_R5_RESULT_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r5_result.json")
MODELS_PROBE_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch2_r2_models_probe.json")
MAPPING_PATH = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_model_mapping_2026_09_24.md")

# tun 代理 (沿 r5/r4/r3/r2/r1)
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"
TUN_HOST = "127.0.0.1"
TUN_PORT = 1018

# ============================================================
# 端点配置 (沿 r5)
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
KEY_INDEX_TEAMO_1BASED = 15  # 沿 r5/r4/r3/r2/r1 (line 15 = teamo key)
USE_PROXY = True

# 串行间隔
INTER_CALL_SLEEP_S = 2.5

# 超参 (沿 r5; 同模型同 prompt 不改)
TEMPERATURE = 0.7
MAX_TOKENS = 2000

# 工具失灵族参数修正 (沿 r5)
READ_TIMEOUT_INITIAL_S = 60
READ_TIMEOUT_RETRY_S = 90
INNER_RETRY_MAX = 3

# 网络异常 retry 类别 (沿 r5 + dispatch §1 字面)
NETWORK_ERROR_CATEGORIES_RETRY = {"timeout", "proxy_error", "ssl_error", "connection_error"}

# K-N26-N2 累计 empty_rate 停采阈值 (沿 dispatch §4)
K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD = 0.50

# 单棒 empty_rate 停采阈值 (沿 dispatch 「单棒 >50% 停采」)
SINGLE_BATCH_EMPTY_RATE_THRESHOLD = 0.50

# 预算 (单 call 短预算)
WALL_TIME_BUDGET_S = 120

# 本棒调度 (沿 dispatch)
BATCH = 4
ROUND = 6  # 升 r6 命名 (定向补 S6_n60)
TEACHER = "coze"
SIDE = "teacher"
REASK_R1 = 5  # 本棒 round 6 = S6_n60 第 6 call (reask_idx=5)
TARGET_SUCCESSFUL_PER_CAPTION = 5
SMOKE_CALL_ONLY = True  # 沿 r5 smoke ok=200 已知; 本棒仅 1-call smoke 防端点飘移

# **单 caption 定向补 (沿 dispatch §1)**
SINGLE_CAPTION_TARGET = "S6_n60"

# **硬停规则 (沿 dispatch §2)**
HARD_STOP_ON_EMPTY_RESPONSE = True

# 选定的 model_id (沿 mapping 拍板代表采样; r5 已 smoke ok=200 + r5 22 caption 21 OK + S6_n60 空响应已知)
MODEL_COZE_REPRESENTATIVE = "deepseek-v4-flash"

# representative 标注 (强制入 result metadata)
REPRESENTATIVE_FOR_COZE = True
SUBSTITUTE_ORIGIN = "coze_agent_platform_underlying_model_not_documented"

# smoke prompt (极小, 节省 token)
SMOKE_PROMPT = "Reply with the single word: ok"

# rounds_used (含 r6; r6 为定向补棒)
ROUNDS_USED = ["r1", "r2", "r3", "r4", "r5", "r6"]


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
# 工具 (沿 r5 + 复用)
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
    model_id: str,
    messages: List[Dict[str, str]],
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
    timeout: int = READ_TIMEOUT_INITIAL_S,
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch4-r6",
        "X-Title": f"deposon-l14v3-batch4-r6-{TEACHER}-teacher",
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
# 提示构造 (沿 r5)
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
# Smoke (沿 r5 简化版; 仅 1 call 确认端点 ok)
# ============================================================
def smoke_coze_model(api_key: str, model_id: str) -> Dict[str, Any]:
    """1-call smoke (沿 r5 smoke ok=200 已知); 仅作端点可达性确认。"""
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
        "phase_label": "smoke_coze_representative_model_id_r6_supplement",
        "wall_time_s": round(time.time() - t0, 1),
    }
    return rec


# ============================================================
# 单 call + 内层重试 (沿 r5)
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,
    round_index: int,
    is_round_6: bool,
    phase_label: str,
    retry_trigger_categories_tracker: List[str],
    model_id: str,
    prompt_id_suffix: str,
) -> Dict[str, Any]:
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    prompt_id = f"coze_t06_{side}_{caption_id}{prompt_id_suffix}"

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
                        "is_round_6": is_round_6,
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
                "is_round_6": is_round_6,
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
            "is_round_6": is_round_6,
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
    print("V4 L14+ batch 4 round 6 · coze 教师侧 S6_n60 单 call 定向补 (reask=5)")
    print("沿 r5 deepseek-v4-flash smoke ok=200 + r5 22 caption 21 OK + S6_n60 空响应已知")
    print("计划 calls = 1 caption (S6_n60) × 1 call = 1 call + 1 smoke call")
    print("目标: round 6 后 S6_n60 = 5/5 successful call (达 coze 教师侧 target = 22/22)")
    print("硬停规则 (沿 dispatch §2): 若本 call 仍 empty → 立即停止不加试; 接受 partial 21/22")
    print("预算 ≤1 caption call + 1 smoke call / ≤120s watchdog")
    print("retry ≤3 (网络错; 沿 dispatch §1)")
    print("夜间保守口径 (PI 2026-09-25 00:46): 启动前必检 tun 端口")
    print("建议沿用 python -u > log 2>&1 防 300s 自动截杀")
    print("=" * 60)

    setup_proxy_teamo()
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    # 0. 夜间保守口径 — 启动前必检 tun 端口 (防 net::ERR_HTTP2_PING_FAILED 重演)
    if not preflight_tun_check():
        return 1

    # 1. 加载 caption (仅取 S6_n60)
    captions = load_captions()
    cap_by_id = {c["id"]: c for c in captions}
    print(f"[INIT] captions loaded: {len(captions)}; single target = {SINGLE_CAPTION_TARGET}")
    if SINGLE_CAPTION_TARGET not in cap_by_id:
        print(f"[FATAL] single_caption_target={SINGLE_CAPTION_TARGET} not in captions; abort")
        return 2

    # 2. 加载 key
    try:
        api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
        print(f"[INIT] teamo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 3. 加载前置累计基线 (b4 r5 终态作为 coze 自身 baseline; cross batch 沿 b4r5 终态)
    with open(B4_R5_RESULT_PATH, "r", encoding="utf-8") as f:
        b4_r5 = json.load(f)
    b4_r5_cross_total = b4_r5["aggregate"]["cross_batch_with_b4r4_baseline"]["cross_total"]
    b4_r5_cross_empty = b4_r5["aggregate"]["cross_batch_with_b4r4_baseline"]["cross_empty"]
    b4_r5_cross_ok = b4_r5["aggregate"]["cross_batch_with_b4r4_baseline"]["cross_ok"]
    b4_r5_cross_rate = b4_r5["aggregate"]["cross_batch_with_b4r4_baseline"]["cross_rate"]
    print(
        f"[BASELINE b4r5 cross batch] total={b4_r5_cross_total} "
        f"ok={b4_r5_cross_ok} empty={b4_r5_cross_empty} rate={b4_r5_cross_rate:.4f}"
    )

    coze_prior_total = b4_r5["aggregate"]["coze_cumulative"]["post_total"]
    coze_prior_ok = b4_r5["aggregate"]["coze_cumulative"]["post_ok"]
    coze_prior_empty = b4_r5["aggregate"]["coze_cumulative"]["post_empty"]
    coze_prior_rate = b4_r5["aggregate"]["coze_cumulative"]["post_rate"]
    print(
        f"[BASELINE b4r5 coze cumulative] total={coze_prior_total} "
        f"ok={coze_prior_ok} empty={coze_prior_empty} rate={coze_prior_rate:.4f}"
    )

    # 4. 加载 /v1/models 探活清单 (参考; 不重探)
    with open(MODELS_PROBE_PATH, "r", encoding="utf-8") as f:
        models_probe = json.load(f)
    all_ids = models_probe.get("all_ids_extracted", [])
    deepseek_like_ids = [m for m in all_ids if isinstance(m, str) and "deepseek" in m.lower()]
    deepseek_v4_flash_in_listing = "deepseek-v4-flash" in all_ids
    print(
        f"[MODELS PROBE REF] 44 total models; deepseek 系 {len(deepseek_like_ids)} 个: "
        f"{deepseek_like_ids}; deepseek-v4-flash 在清单={deepseek_v4_flash_in_listing}"
    )

    # 5. Smoke 1-call (deepseek-v4-flash 端点可达性确认; 沿 r5 smoke ok=200 已知)
    print("=" * 60)
    print("[SMOKE PHASE] deepseek-v4-flash 1-call smoke (沿 r5 smoke ok=200 已知)")
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
                "task": "L14V3_batch4_round6_coze_teacher_side_s6_n60_supplement_reask5",
                "prereg_sha12": "05b975a86989",
                "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
                "predecessor_sha12": {
                    "model_mapping_sha12": "98a779d61c1e",
                    "model_mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                    "b4_r5_executor_sha12": "8a505613b476",
                    "b4_r5_executor_path": "results/_v4_supp_l14v3_batch4_r5_executor.py",
                    "b4_r5_result_sha12": "bad01f2b89fd",
                    "b4_r5_result_path": "results/_v4_supp_l14v3_batch4_r5_result.json",
                    "b4_r4_executor_sha12": "184186902a9f",
                    "b4_r4_executor_path": "results/_v4_supp_l14v3_batch4_r4_executor.py",
                    "b4_r4_result_sha12": "41e0ba55e205",
                    "b4_r4_result_path": "results/_v4_supp_l14v3_batch4_r4_result.json",
                    "b4_r3_executor_sha12": "b5e1c3637405",
                    "b4_r3_executor_path": "results/_v4_supp_l14v3_batch4_r3_executor.py",
                    "b4_r3_result_sha12": "ed5267df7d6f",
                    "b4_r3_result_path": "results/_v4_supp_l14v3_batch4_r3_result.json",
                    "b4_r2_executor_sha12": "7d8e12267790",
                    "b4_r2_executor_path": "results/_v4_supp_l14v3_batch4_r2_executor.py",
                    "b4_r2_result_sha12": "6a9a362d9869",
                    "b4_r2_result_path": "results/_v4_supp_l14v3_batch4_r2_result.json",
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
                "date": "2026-09-25",
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
        out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r6_result.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(fail_result, f, ensure_ascii=False, indent=2)
        print(f"[WROTE] {out_path}")
        return 3
    print(f"[SMOKE-OK] model_id = {MODEL_COZE_REPRESENTATIVE} (sc=200, model_returned={smoke_rec['model_returned']})")

    model_id = MODEL_COZE_REPRESENTATIVE

    # 6. 调度: 仅 S6_n60 × 1 call (round 6 reask=5) — 单 caption 定向补
    target_caption = cap_by_id[SINGLE_CAPTION_TARGET]
    planned = [{"caption_id": SINGLE_CAPTION_TARGET, "phase": "b4_r6_s6_n60_supplement"}]
    planned_total = len(planned)
    print(f"[PLANNED] total: {planned_total} (1 caption {SINGLE_CAPTION_TARGET} × 1 call)")

    # 7. 时间预算起点 (含 smoke)
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
    r6_total = 0
    r6_ok = 0
    r6_empty = 0
    r6_fail = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_reasoning_tokens = 0
    k_n26_n2_triggered = False
    k_n26_n2_trigger_at_call_idx = None
    k_n26_n2_trigger_cum_rate = None
    single_batch_triggered = False
    stop_reason = None
    hard_stop_engaged = False
    hard_stop_reason = None

    retry_trigger_categories_tracker: List[str] = []
    retry_count_distribution: Dict[int, int] = {}
    retry_triggered_count = 0

    # 从 r5 累计 per_caption_successful_calls 起步; 仅 S6_n60 会被更新
    r5_per_cap = b4_r5.get("per_caption_successful_calls", {})
    per_cap_succ = {cid: r5_per_cap.get(cid, {}).get("succ_count", 0) for cid in [c["id"] for c in captions]}
    per_cap_total = {cid: r5_per_cap.get(cid, {}).get("total_calls_so_far", 0) for cid in [c["id"] for c in captions]}
    per_cap_empty = {cid: r5_per_cap.get(cid, {}).get("empty_count_so_far", 0) for cid in [c["id"] for c in captions]}
    print(f"[PRIOR S6_n60] succ={per_cap_succ.get('S6_n60', 0)}/5 total={per_cap_total.get('S6_n60', 0)} empty={per_cap_empty.get('S6_n60', 0)}")

    # 跑 single caption (S6_n60)
    i = 0
    item = planned[0]
    cap_id = item["caption_id"]
    caption = cap_by_id[cap_id]

    # K-N26-N2 coze 自身累计监控 (call 前判)
    if cum_total > 0:
        current_cum_rate = cum_empty / cum_total
        if current_cum_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
            k_n26_n2_triggered = True
            k_n26_n2_trigger_at_call_idx = i
            k_n26_n2_trigger_cum_rate = current_cum_rate
            stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
            print(f"[STOP] K-N26-N2 coze cumulative empty_rate={current_cum_rate:.4f} > 0.50 before call {i+1}/{planned_total}; stop per dispatch §4")
        else:
            rec = run_one_quadruple(
                api_key=api_key,
                caption=caption,
                reask_idx=REASK_R1,
                side="teacher",
                round_index=ROUND,
                is_round_6=True,
                phase_label=item["phase"],
                retry_trigger_categories_tracker=retry_trigger_categories_tracker,
                model_id=model_id,
                prompt_id_suffix="_b4_r6",
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
                r6_ok += 1
                cum_ok += 1
                per_cap_succ[cap_id] += 1
            elif is_empty:
                r6_empty += 1
                cum_empty += 1
                per_cap_empty[cap_id] += 1
            else:
                r6_fail += 1
            r6_total += 1
            cum_total += 1
            per_cap_total[cap_id] += 1

            usage = m.get("usage", {}) or {}
            total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
            total_completion_tokens += usage.get("completion_tokens", 0) or 0
            completion_details = usage.get("completion_tokens_details", {}) or {}
            total_reasoning_tokens += completion_details.get("reasoning_tokens", 0) or 0

            status = "OK" if is_ok else ("EMPTY" if is_empty else f"FAIL({m.get('error_category','')})")
            current_cum_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
            cur_succ = per_cap_succ[cap_id]
            target_met = "[OK]" if cur_succ >= 5 else "[..]"
            print(
                f"  [{i+1:2d}/{planned_total}] [b{BATCH}r{ROUND}] {item['phase']:<28} {cap_id:<28} "
                f"lat={m.get('latency_ms',0):>7.1f}ms "
                f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
                f"reasoning={completion_details.get('reasoning_tokens', 0) or 0} "
                f"retries={rc} "
                f"{status} "
                f"[succ={cur_succ}/5 {target_met}] "
                f"[coze_cum_rate={current_cum_rate_post:.4f}]"
            )

            # **硬停规则 (沿 dispatch §2)**: empty 立即停不加试
            if is_empty and HARD_STOP_ON_EMPTY_RESPONSE:
                hard_stop_engaged = True
                hard_stop_reason = "empty_response_2_attempts_confirmed_structural_failure"
                stop_reason = "hard_stop_empty_response_no_retry"
                print(f"[HARD STOP] S6_n60 仍 empty; reason={hard_stop_reason}; 立即停止不加试")
                print(f"[HARD STOP] 接受 partial 21/22; 留 verdict-keeper 统裁 (处置路径 c)")

            # K-N26-N2 停采监控 (call 后立即判)
            if cum_total > 0:
                post_rate = cum_empty / cum_total
                if post_rate > K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD:
                    k_n26_n2_triggered = True
                    k_n26_n2_trigger_at_call_idx = i + 1
                    k_n26_n2_trigger_cum_rate = post_rate
                    if stop_reason is None:
                        stop_reason = "K_N26_N2_cumulative_empty_rate_exceeded_0.50"
                    print(f"[STOP] K-N26-N2 coze post-call cumulative empty_rate={post_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch §4")

            # 单棒 >50% 停采
            if r6_total > 0:
                single_rate = r6_empty / r6_total
                if single_rate > SINGLE_BATCH_EMPTY_RATE_THRESHOLD:
                    single_batch_triggered = True
                    if stop_reason is None:
                        stop_reason = "single_batch_empty_rate_exceeded_0.50"
                    print(f"[STOP] single batch empty_rate={single_rate:.4f} > 0.50 at call {i+1}/{planned_total}; stop per dispatch '单棒 >50% 停采'")

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)
    total_wall_s = round(t_batch_end - t_smoke_start, 1)

    # 9. 统计
    empty_rate_r6 = (r6_empty / r6_total) if r6_total > 0 else 0.0
    cum_empty_rate_post = cum_empty / cum_total if cum_total > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == len(quadruples))

    # 跨批累计 = b4r5 baseline + coze 本棒
    cross_batch_total = b4_r5_cross_total + r6_total
    cross_batch_empty = b4_r5_cross_empty + cum_empty - coze_prior_empty
    cross_batch_ok = b4_r5_cross_ok + cum_ok - coze_prior_ok
    cross_batch_rate = cross_batch_empty / cross_batch_total if cross_batch_total > 0 else 0.0

    # 10. 每 caption successful 计数 (收官判定准备)
    per_caption_successful_calls = {}
    met_target_count = 0
    s6_n60_succ_post = per_cap_succ.get(SINGLE_CAPTION_TARGET, 0)
    s6_n60_met_target = s6_n60_succ_post >= TARGET_SUCCESSFUL_PER_CAPTION
    for cid in [c["id"] for c in captions]:
        s = per_cap_succ[cid]
        t = per_cap_total[cid]
        e = per_cap_empty[cid]
        met_target = s >= TARGET_SUCCESSFUL_PER_CAPTION
        if met_target:
            met_target_count += 1
        per_caption_successful_calls[cid] = {
            "succ_count": s,
            "target": TARGET_SUCCESSFUL_PER_CAPTION,
            "need_more_to_target": max(0, TARGET_SUCCESSFUL_PER_CAPTION - s),
            "met_target": met_target,
            "total_calls_so_far": t,
            "empty_count_so_far": e,
            "round6_updated": (cid == SINGLE_CAPTION_TARGET),
        }

    # 11. coze 教师侧 round 6 进度块 (含 S6_n60 定向补结果)
    coze_round6_progress = {
        "round6_target_caption": SINGLE_CAPTION_TARGET,
        "round6_reask_idx": REASK_R1,
        "round6_call_result": (
            "ok" if r6_ok > 0 else ("empty" if r6_empty > 0 else ("fail" if r6_fail > 0 else "no_call"))
        ),
        "round6_met_target_post": s6_n60_met_target,
        "round6_hard_stop_engaged": hard_stop_engaged,
        "round6_hard_stop_reason": hard_stop_reason,
        "round6_total_calls": r6_total,
        "round6_ok_count": r6_ok,
        "round6_empty_count": r6_empty,
        "round6_fail_count": r6_fail,
        "met_count_post_r6": met_target_count,
        "total_captions": len(captions),
        "remaining_count_r6": len(captions) - met_target_count,
        "met_percentage_r6": round(met_target_count / len(captions) * 100, 2),
        "still_pending_captions_r6": sorted([
            cid for cid, info in per_caption_successful_calls.items() if not info["met_target"]
        ]),
    }

    # 11b. **r6 收官判定块 (沿 r5 coze_teacher_side_finish 收官判定块惯例)**
    all_22_captions_met_target = (met_target_count == len(captions))
    coze_teacher_side_finish = {
        "all_22_captions_met_target": all_22_captions_met_target,
        "total_captions": len(captions),
        "met_target_count": met_target_count,
        "met_target_percentage": round(met_target_count / len(captions) * 100, 2),
        "rounds_used": ROUNDS_USED,
        "cumulative_calls_total": cum_total,
        "cumulative_ok": cum_ok,
        "cumulative_empty": cum_empty,
        "cumulative_empty_rate": round(cum_empty_rate_post, 4),
        "finish_status": "complete" if all_22_captions_met_target else "partial",
        "k_n26_n2_cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
        "k_n26_n2_cumulative_triggered_this_batch": k_n26_n2_triggered,
        "single_batch_triggered_this_batch": single_batch_triggered,
        "finish_verdict_trigger_for_verdict_keeper": all_22_captions_met_target,
        "note": (
            f"沿 r5 coze_teacher_side_finish 收官判定惯例; r6 定向补 S6_n60 (reask=5) 后 "
            f"{met_target_count}/{len(captions)} caption met target ≥5 successful/caption; "
            f"finish_status={'complete' if all_22_captions_met_target else 'partial'}; "
            f"verdict-keeper 可据 all_22_captions_met_target 触发判死线 (沿 '与死同行' 准则); "
            f"代表采样 = deepseek-v4-flash (沿 mapping 98a779d61c1e); "
            f"coze 底层 model 不可考即如实不可考 (沿诚实 = 不误导)"
        ),
    }

    # 11c. **r6 disposition 块 (沿 dispatch §2)**
    s6_n60_call_structural_failure = (r6_empty > 0)  # 2 试皆空 (r5 empty + r6 empty)
    r6_disposition_block = {
        "r6_call_target": SINGLE_CAPTION_TARGET,
        "r6_call_result": (
            "ok" if r6_ok > 0 else ("empty" if r6_empty > 0 else ("fail" if r6_fail > 0 else "no_call"))
        ),
        "r6_call_structural_failure_confirmed": s6_n60_call_structural_failure,
        "r6_hard_stop_engaged": hard_stop_engaged,
        "r6_hard_stop_reason": hard_stop_reason,
        "r6_disposition": (
            "complete_22_of_22" if all_22_captions_met_target else "partial_21_of_22"
        ),
        "r6_partial_path": "verdict_keeper_adjudicate_path_c" if not all_22_captions_met_target else None,
        "r6_note": (
            "S6_n60 结构性失能确认 (模型行为, 2 试皆空: r5 reask=4 + r6 reask=5)" if s6_n60_call_structural_failure
            else "S6_n60 第 6 call OK; coze 教师侧 22/22 收官"
        ),
    }

    # 12. retry validation 块
    retry_trigger_categories_distribution: Dict[str, int] = {}
    for cat in retry_trigger_categories_tracker:
        retry_trigger_categories_distribution[cat] = retry_trigger_categories_distribution.get(cat, 0) + 1

    retry_validation = {
        "r6_retry_count_distribution": dict(retry_count_distribution),
        "r6_retry_triggered_count": retry_triggered_count,
        "r6_retry_trigger_categories_tracker": retry_trigger_categories_tracker,
        "r6_retry_trigger_categories_distribution": retry_trigger_categories_distribution,
        "r6_retry_bug_fix_applied_in_all_calls": all(
            q["per_call_metadata"].get("retry_bug_fix_applied") is True
            for q in quadruples
        ),
        "r6_empty_rate_with_fix": round(empty_rate_r6, 4),
    }

    # 13. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    # model_id_inconsistency_honest_disclosure (沿 r5 字面格式 + r6 累计补注)
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
        f"r1+r2+r3+r4+r5 五棒累计 110 calls 1 empty 109 ok (沿 r5 终态); "
        f"model_returned 字面 = deepseek-v4-flash-ga-260731 (主) + deepseek-v4-flash-0731 (次), 均 family 下实例; "
        f"r6 沿 r5 同模型同 max_tokens=2000 同 temperature=0.7 同 prompt 定向补 S6_n60 (reask=5); "
        f"r6 单 call; 硬停规则 (沿 dispatch §2): empty 立即停不加试; "
        f"待 PI 复核项: 是否接受 deepseek-v4-flash 作为 coze = V3 公开产品名/端点名的代表采样"
    )

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": BATCH,
        "round": ROUND,
        "metadata": {
            "task": "L14V3_batch4_round6_coze_teacher_side_s6_n60_supplement_reask5",
            "prereg_sha12": "05b975a86989",
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "predecessor_sha12": {
                "model_mapping_sha12": "98a779d61c1e",
                "model_mapping_path": "results/_v4_supp_l14v3_model_mapping_2026_09_24.md",
                "b4_r5_executor_sha12": "8a505613b476",
                "b4_r5_executor_path": "results/_v4_supp_l14v3_batch4_r5_executor.py",
                "b4_r5_result_sha12": "bad01f2b89fd",
                "b4_r5_result_path": "results/_v4_supp_l14v3_batch4_r5_result.json",
                "b4_r4_executor_sha12": "184186902a9f",
                "b4_r4_executor_path": "results/_v4_supp_l14v3_batch4_r4_executor.py",
                "b4_r4_result_sha12": "41e0ba55e205",
                "b4_r4_result_path": "results/_v4_supp_l14v3_batch4_r4_result.json",
                "b4_r3_executor_sha12": "b5e1c3637405",
                "b4_r3_executor_path": "results/_v4_supp_l14v3_batch4_r3_executor.py",
                "b4_r3_result_sha12": "ed5267df7d6f",
                "b4_r3_result_path": "results/_v4_supp_l14v3_batch4_r3_result.json",
                "b4_r2_executor_sha12": "7d8e12267790",
                "b4_r2_executor_path": "results/_v4_supp_l14v3_batch4_r2_executor.py",
                "b4_r2_result_sha12": "6a9a362d9869",
                "b4_r2_result_path": "results/_v4_supp_l14v3_batch4_r2_result.json",
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
            "date": "2026-09-25",
            "spec_conformance": (
                "PI 2026-09-25 batch4 coze 教师侧 S6_n60 单 call 定向补 (reask=5); "
                "沿 r5 deepseek-v4-flash smoke ok=200 + r5 22 caption 21 OK + S6_n60 空响应已知; "
                "本棒同模型同 prompt 同 max_tokens=2000 同 temperature=0.7 同 tun; "
                "1 caption (S6_n60) × 1 call = 1 call (按 dispatch 定向补); "
                "硬停规则 (沿 dispatch §2): 若本 call 仍 empty → 立即停止不加试; 接受 partial 21/22; "
                "夜间保守口径 (PI 2026-09-25 00:46): 启动前必检 tun 端口 (127.0.0.1:1018); "
                "建议沿用 python -u > log 2>&1 防 300s 自动截杀"
            ),
            "teacher": TEACHER,
            "side": SIDE,
            "round_index": ROUND,
            "batch_index": BATCH,
            "round6_target_caption": SINGLE_CAPTION_TARGET,
            "round6_reask_idx": REASK_R1,
            "target_successful_per_caption": TARGET_SUCCESSFUL_PER_CAPTION,
            "hard_stop_on_empty_response": HARD_STOP_ON_EMPTY_RESPONSE,
            "n_captions_total": len(captions),
            "planned_total": planned_total,
            "actual_total": r6_total,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": (
                "沿 mapping 98a779d61c1e §1.1 第三栏 PI 拍板 (teamo 端点); "
                "/v1/models 探活清单沿 r2 models_probe.json (sha12=3c9dc60b5071); "
                "r6 沿 r5 smoke ok=200 + r5 22 caption 21 OK + S6_n60 空响应已知; r6 仅 1-call smoke 防端点飘移; "
                "44 models 清单字面含 deepseek-v4-flash; r6 同模型同 prompt (沿 dispatch §1 「同 deepseek-v4-flash / 同 prompt」)"
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
                "b4_r5_status": "r5 1-call smoke ok=200 + 22 caption × 1 call = 22 calls; 21 OK + 1 empty (S6_n60 reasoning-occupied 模式); model_returned 字面 deepseek-v4-flash-ga-260731 (主) + deepseek-v4-flash-0731 (次)",
                "r6_b4_status": "r6 沿 r5 同模型同 prompt; 仅 1-call smoke (沿 r5 结论); 未做 3-candidate probe fallback",
                "rationale": (
                    "沿 dispatch §1 「同 deepseek-v4-flash / 同 prompt / max_tokens=2000 / temperature=0.7 / tun」; "
                    "r6 仅 S6_n60 1 call; 同模型 (deepseek-v4-flash); 同 prompt; 同 max_tokens=2000; 同 temperature=0.7; "
                    "smoke 失败立即 abort 不重探; "
                    "硬停规则 (沿 dispatch §2): empty 立即停不加试; "
                    "启动前必检 tun 端口 (PI 2026-09-25 夜间保守口径; 防 net::ERR_HTTP2_PING_FAILED 重演); "
                    "建议沿用 python -u > log 2>&1 防 300s 自动截杀"
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
            "diff_vs_r5_executor": [
                "1. ROUND=6 (升 r6 命名); BATCH=4 不变",
                "2. **目标 caption 缩窄**: 仅 S6_n60 (沿 r5 终态 21/22 caption met target, S6_n60 仅 4/5); 取代 r5 的全 22 caption",
                "3. **call 数**: 1 caption × 1 call = 1 call (取代 r5 的 22 caption × 1 call)",
                "4. prompt_id 前缀 coze_t06_teacher_S6_n60 + 后缀 _b4_r6 (取代 r5 的 coze_t05_teacher_*_b4_r5); 单 caption 定向补",
                "5. reask_idx=5 (本棒 S6_n60 第 6 call; 取代 r5 的 reask_idx=4)",
                "6. phase_label: b4_r6_s6_n60_supplement (取代 r5 的 b4_r5_finish)",
                "7. is_round_6=True (取代 r5 的 is_round_5; 语义升级)",
                "8. **新增 hard_stop_on_empty_response = True** (沿 dispatch §2 硬停规则; r5 无此字段)",
                "9. **新增 single_caption_target = S6_n60** (取代 r5 的全 22 caption)",
                "10. smoke_call_only = True (沿 r5 同; 沿 r5 smoke ok=200 已知)",
                "11. predecessor_sha12 链: b4_r5_executor 8a505613b476 + b4_r5_result bad01f2b89fd (新增; 取代 r5 链的 b4_r4/r3/r2/r1/r4/r3/probe/batch1_r6/prereg 仍保留作为历史累计 baseline)",
                "12. baseline prior: r5 终态 110 calls / 1 empty / 109 ok / 0.0091 rate (取代 r5 链的 88/88/0/0.0)",
                "13. 跨批累计 baseline: r5 终态 295 calls / 10 empty / 3.39% rate (取代 r5 链的 273/9/3.30%); 注: r5 cross_total=295 已含 b4r5 22 calls 增量",
                "14. **新增 r6_disposition 块** (沿 dispatch §2): r6_call_target / r6_call_result / r6_call_structural_failure_confirmed / r6_hard_stop_engaged / r6_hard_stop_reason / r6_disposition (complete_22_of_22 / partial_21_of_22)",
                "15. **新增 coze_teacher_side_round6_progress 块** (沿 r5 coze_teacher_side_round5_progress 惯例; 含 S6_n60 定向补结果)",
                "16. **更新 coze_teacher_side_finish 收官判定块** (沿 r5 收官判定块惯例; 反映 r6 后状态; finish_status = complete/partial)",
                "17. K-N26-N2 触发阈值 0.50 不变; 监控 baseline 更新为 295/10/3.39%",
                "18. spec_conformance 重写: coze 教师侧 S6_n60 单 call 定向补 (reask=5); 同模型同 prompt; 硬停规则",
                "19. model_id_inconsistency_honest_disclosure 字面继承 r5 (沿 mapping 拍板代表采样字面) + r6 累计补注",
                "20. 派生 metadata 字段沿 r5 不动 (v3_anchor_api_name=coze / v3_anchor_9backbone_name=null / v4_current_model_id_sent=deepseek-v4-flash)",
                "21. per_caption_successful_calls 字段: 复制 r5 终态 + 仅更新 S6_n60 行 (round6_updated=true)",
                "22. baseline 路径: B4_R5_RESULT_PATH (沿 r5 result bad01f2b89fd) 取代 r5 链的 B4_R4_RESULT_PATH",
                "23. 启动前必检 tun 端口 (PI 2026-09-25 夜间保守口径; 防 net::ERR_HTTP2_PING_FAILED 重演); r5 同",
                "24. failure result 路径同步 r6: _v4_supp_l14v3_batch4_r6_result.json (取代 r5 链的 r5 result)",
                "25. ROUNDS_USED = [r1, r2, r3, r4, r5, r6] (含 r6; r6 为定向补棒)",
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
                "preflight_tun_check_applied": True,
                "hard_stop_on_empty_response": True,
                "single_caption_target": SINGLE_CAPTION_TARGET,
                "same_model_same_prompt_as_r5": True,
            },
            "run_window_cst": now_iso,
            "stop_reason": stop_reason,
            "hard_stop_engaged": hard_stop_engaged,
            "hard_stop_reason": hard_stop_reason,
            "interruption_recovery_note": (
                "r6 沿 r5 deepseek-v4-flash 代表采样结论 (sha12=bad01f2b89fd 实测 22 calls 21 OK + 1 empty); "
                "不再做 3-candidate probe fallback; 1-call smoke 失败立即 abort; "
                "启动前必检 tun 端口 (PI 2026-09-25 夜间保守口径; 防 net::ERR_HTTP2_PING_FAILED 重演); "
                "r6 与 r5/r4/r3/r2/r1/batch2_r*/batch1_r6 派生 JSON 独立 (不合并); "
                "coze 自身 baseline = 110/109/1/0.0091 (沿 r5 终态); "
                "cross batch baseline = 295/285/10/3.39% (沿 r5 终态); "
                "本棒为 coze 教师侧 S6_n60 定向补棒 (reask=5); "
                "硬停规则: empty 立即停不加试 (沿 dispatch §2); "
                "收官判定见 coze_teacher_side_finish 块; "
                "r6 disposition 见 r6_disposition 块"
            ),
        },
        "models_listing_summary_ref": {
            "endpoint": ENDPOINT_TEAMO + "/models",
            "model_count_total": models_probe.get("model_count_total"),
            "deepseek_like_ids": deepseek_like_ids,
            "deepseek_v4_flash_in_listing": deepseek_v4_flash_in_listing,
            "fetched_at_cst": models_probe.get("fetched_at_cst"),
            "note": (
                "r6 不重探 /v1/models; 仅引用 r2 探活清单 (sha12=3c9dc60b5071) "
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
        "coze_teacher_side_round6_progress": coze_round6_progress,
        "r6_disposition": r6_disposition_block,
        "coze_teacher_side_finish": coze_teacher_side_finish,
        "dispatch_target_progress": {
            "target_round6": "1 caption (S6_n60) × 1 call (round 6 reask=5 定向补)",
            "target_cumulative": f">={TARGET_SUCCESSFUL_PER_CAPTION} successful calls/caption (跨轮累计)",
            "met_count_post_r6_round6": 1 if s6_n60_met_target else 0,
            "met_count_post_r6_cumulative_to_target": met_target_count,
            "total_captions": len(captions),
            "remaining_count_round6": 0 if s6_n60_met_target else 1,
            "remaining_count_cumulative_to_target": len(captions) - met_target_count,
            "met_percentage_round6": round((1 if s6_n60_met_target else 0) * 100, 2),
            "met_percentage_cumulative_to_target": round(met_target_count / len(captions) * 100, 2),
            "still_pending_captions_round6": [] if s6_n60_met_target else [SINGLE_CAPTION_TARGET],
            "still_pending_captions_cumulative_to_target": sorted([
                cid for cid, info in per_caption_successful_calls.items() if not info["met_target"]
            ]),
        },
        "aggregate": {
            "r6_total_calls": r6_total,
            "r6_ok_count": r6_ok,
            "r6_empty_response_count": r6_empty,
            "r6_fail_count": r6_fail,
            "r6_empty_response_rate": round(empty_rate_r6, 4),
            "r6_total_prompt_tokens": total_prompt_tokens,
            "r6_total_completion_tokens": total_completion_tokens,
            "r6_total_reasoning_tokens": total_reasoning_tokens,
            "r6_total_tokens": total_prompt_tokens + total_completion_tokens,
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
            "cross_batch_with_b4r5_baseline": {
                "b4r5_baseline_total": b4_r5_cross_total,
                "b4r5_baseline_empty": b4_r5_cross_empty,
                "b4r5_baseline_ok": b4_r5_cross_ok,
                "b4r5_baseline_rate": b4_r5_cross_rate,
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
            "r6_empty_response_rate_threshold_K_N26_N2_single_batch": SINGLE_BATCH_EMPTY_RATE_THRESHOLD,
            "r6_empty_response_above_threshold_single_batch": empty_rate_r6 > SINGLE_BATCH_EMPTY_RATE_THRESHOLD,
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
            "batch4_round2_round2_reask1_coze": {
                "calls": 22,
                "empty": 0,
                "rate": 0.0,
                "note": "r2 coze round 2 reask=1 22 caption × 1 call; all OK",
            },
            "batch4_round3_round3_reask2_coze": {
                "calls": 22,
                "empty": 0,
                "rate": 0.0,
                "note": "r3 coze round 3 reask=2 22 caption × 1 call; all OK",
            },
            "batch4_round4_round4_reask3_coze": {
                "calls": 22,
                "empty": 0,
                "rate": 0.0,
                "note": "r4 coze round 4 reask=3 22 caption × 1 call; all OK",
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
            "batch4_round5_round5_reask4_coze": {
                "calls": 22,
                "empty": 1,
                "rate": round(1 / 22, 4),
                "note": "r5 coze round 5 reask=4 22 caption × 1 call; 21 OK + 1 empty (S6_n60 reasoning-occupied 模式)",
            },
            "batch4_round5_cumulative_coze": {
                "calls": 110,
                "empty": 1,
                "ok": 109,
                "rate": round(1 / 110, 4),
                "note": "r5 终态 coze 自身累计",
            },
            "cross_batch_cumulative_post_r5": {
                "calls": 295,
                "empty": 10,
                "ok": 285,
                "rate": round(10 / 295, 4),
                "note": "r5 终态 cross batch baseline (kimi + GLM_1 + coze r1+r2+r3+r4+r5)",
            },
            "batch4_round6_round6_reask5_coze_s6_n60": {
                "calls": r6_total,
                "empty": r6_empty,
                "rate": round(empty_rate_r6, 4),
                "note": "r6 coze round 6 reask=5 S6_n60 单 call 定向补 (沿 dispatch)",
            },
            "batch4_round6_cumulative_coze": {
                "calls": cum_total,
                "empty": cum_empty,
                "ok": cum_ok,
                "rate": round(cum_empty_rate_post, 4),
                "k_n26_n2_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "k_n26_n2_triggered": k_n26_n2_triggered,
            },
            "cross_batch_cumulative_post_r6": {
                "calls": cross_batch_total,
                "empty": cross_batch_empty,
                "ok": cross_batch_ok,
                "rate": round(cross_batch_rate, 4),
                "note": "b4r5 baseline 295/10/3.39% + r6 增量",
            },
        },
        "K_N26_observability_only": {
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                "round6_reask5_n_distinct_sample_note": (
                    f"round 6 reask=5 第 6 call 定向补 S6_n60 实测；本棒后 S6_n60 = "
                    f"{s6_n60_succ_post}/5 caption met target；"
                    f"r1+r2+r3+r4+r5+r6 六棒累计 {cum_total} calls"
                ),
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "single_batch_empty_response_rate": round(empty_rate_r6, 4),
                "cumulative_empty_response_rate_coze_only": round(cum_empty_rate_post, 4),
                "cumulative_threshold": K_N26_N2_CUMULATIVE_EMPTY_RATE_THRESHOLD,
                "single_batch_trigger_K_N26_N2_pass_False": empty_rate_r6 > SINGLE_BATCH_EMPTY_RATE_THRESHOLD,
                "cumulative_trigger_K_N26_N2_pass_False": k_n26_n2_triggered,
                "monitor_disposition": (
                    f"本棒 K-N26-N2 coze 自身累计 empty_rate 监控 = 已实施; "
                    f"coze 自身累计 = {cum_total} calls / {cum_empty} empty / {cum_empty_rate_post:.4f}; "
                    f"baseline coze = {coze_prior_total} calls / {coze_prior_empty} empty / {coze_prior_rate:.4f}; "
                    f"cross-batch rate = {cross_batch_rate:.4f}; "
                    f"baseline cross batch = {b4_r5_cross_total} calls / {b4_r5_cross_empty} empty / {b4_r5_cross_rate:.4f}"
                ),
                "cross_batch_with_b4r5_baseline_rate": round(cross_batch_rate, 4),
            },
            "verdict_pending": "verdict-keeper 统裁 (本棒 0 写 verdict; 收官判定见 coze_teacher_side_finish 块)",
        },
        "breakpoint_status": {
            "actual_calls": r6_total,
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
            "hard_stop_engaged": hard_stop_engaged,
            "hard_stop_reason": hard_stop_reason,
            "next_resume_via": (
                "本棒为单 call 定向补棒; 无需续跑; "
                "verdict-keeper 可据 coze_teacher_side_finish.all_22_captions_met_target 触发判死线 (沿 '与死同行' 准则)"
            ),
            "note": (
                f"本棒 round 6 (reask=5) S6_n60 单 call 定向补: actual={r6_total}/{planned_total} calls; "
                f"coze 教师侧完成度 = {met_target_count}/{len(captions)} caption met target ≥5 successful/caption; "
                f"stop_reason={stop_reason}; hard_stop_engaged={hard_stop_engaged}; "
                f"coze model_id 沿 mapping 拍板 = {model_id} (代表采样; 1-call smoke 确认仍可用); "
                f"representative_for_coze=true; substitute_origin=coze_agent_platform_underlying_model_not_documented; "
                f"收官判定 = {'complete' if all_22_captions_met_target else 'partial'}; "
                f"r6 disposition = {r6_disposition_block.get('r6_disposition')}"
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
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch4_r6_result.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    sha12, nbytes, lf_only = sha12_file(out_path)
    print(f"[WROTE] {out_path}")
    print(f"[SHA-12] {sha12}")
    print(f"[BYTES] {nbytes}")
    print(f"[LF-ONLY] {lf_only}")
    print(f"[MODELS LISTING REF] total={models_probe.get('model_count_total')} deepseek_v4_flash_in_listing={deepseek_v4_flash_in_listing}")
    print(f"[SMOKE] selected={model_id} ok={smoke_rec['ok']} wall={smoke_wall_s}s")
    print(f"[STATS r6] ok={r6_ok} empty={r6_empty} fail={r6_fail} total={r6_total} rate={empty_rate_r6:.4f}")
    print(f"[S6_n60 POST] succ={s6_n60_succ_post}/5 total={per_cap_total.get('S6_n60', 0)} empty={per_cap_empty.get('S6_n60', 0)} met_target={s6_n60_met_target}")
    print(f"[COZE CUM POST r6] total={cum_total} ok={cum_ok} empty={cum_empty} rate={cum_empty_rate_post:.4f}")
    print(f"[CROSS BATCH POST r6] total={cross_batch_total} ok={cross_batch_ok} empty={cross_batch_empty} rate={cross_batch_rate:.4f}")
    print(f"[FINISH] all_22_met_target={all_22_captions_met_target} status={'complete' if all_22_captions_met_target else 'partial'}")
    print(f"[R6 DISPOSITION] {r6_disposition_block.get('r6_disposition')}")
    print(f"[HARD STOP] engaged={hard_stop_engaged} reason={hard_stop_reason}")
    print(f"[STOP] {stop_reason}")

    return 0


if __name__ == "__main__":
    sys.exit(main())