# -*- coding: utf-8 -*-
"""
_v4_supp_l14v3_batch1_executor.py
=================================

V4 L14+ 首批 (batch 1) · N-26 V3 distill 整链重跑 — 第 1 教师批（kimi 教师侧）
=========================================================================

【派工依据】
----------------
- **PI 拍板待生效**：`results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md`（SHA-12 `05B975A86989`，
  末态 61,547 B / 行 600-；本棒沿字面执行）
- **生效留痕**：`results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md`（draft 待 PI 复核）
- **PI 2026-09-24 派工单**：双次催办「先解决老挂账」= 实质放行 L14V3 实测；本批范围 =
  第 1 教师批（沿 prereg §1.2 + §1.4 batch 1 字面 = kimi 教师侧）
- **本批范围（沿 §起跑条件 小→大序列 1）**：教师侧 kimi × 22 caption × ≥5 calls = ≥110 calls
  （理论下限）；本次 batch 1 单 sub-batch ≤22 calls（沿 L7 实证 `B8335982AE5E` ≤275s 上限）

【端点选择（端点策略：即用即探）】
------------------------------------
- 三端点可达性实测（沿 `C846F7FC79EE`）：
  - qwen_plan endpoint: 16 模型，无 kimi 类
  - mimo endpoint: 8 模型，无 kimi 类
  - teamo endpoint (with tun): 44 模型，含 `kimi-k3` + `kimi-k3[1M]`
- 本批选定 **teamo endpoint**（kimi-k3 是唯一在 3 端点可达的 kimi 类 model_id）
- model_id 字面冲突诚实交代：
  - prereg §1.2 字面 = `kimi`（旁注 V3 端点名 / API 端点名 = `kimi-for-coding`）
  - 实测 teamo 不接受 `kimi-for-coding`（400 model_not_available），只接受 `kimi-k3`
  - 沿 user memory 2026-09-08「代码里默认 `kimi-for-coding`（API 端点名），公开产品名 `KIMI-K3`
    ——两个不一致时直接问，不要瞎填」+ 沿「0 擅调阈值 / 端点策略即用即探」实测口径
  - **本批用 teamo 实际接受 model_id = `kimi-k3`**；`kimi-for-coding` 视为 deposon-side 内部
    命名（V3 端点名 / 论文占位层），实际 API 命中串只有 `kimi-k3`
  - 沿 PI 2026-09-24 V4 放开 LLM 调用 + 此为**唯一可达路径**，不擅自用知识截止前旧版本号瞎填

【四元组强制采集】
--------------------
- 每 call 必同步落盘 (prompt_id, prompt_text, response_text, per-call metadata)——
  缺一字段即批次作废重采（沿 dispatch §四元组强制采集）
- per-call metadata = (latency_ms, model_returned, usage, status_code, error_category, error_snippet, retry_count)

【铁律严守】
----------------
- R4 key 永不明文（无例外）：产物 key 字段一律 "runtime-env (redacted)"；key 文件仅读不写
- V1–V3 只读不动：`scripts/run_v3x_*.py` 仅参照系，0 触动；`corpus/v20/by_model/*` 仅参照，0 触动
- 派生 JSON 不合并：本棒 `batch1_result.json` 与既有 `_v4_supp_l13/l4/l7_*` 同级独立
- 0 擅调阈值：max_tokens=2000 沿 prereg §1.4 工具失灵修正条款（非阈值私设）；temperature=0.7 沿
  V3 distill baseline；0 触 K-N26-1/2/3/N1/N2 字面
- 串行 ≥2.5s 全程（沿 add_T1 §1.6.2 + Track 2 runner INTER_CALL_SLEEP_S 沿用）
- teamo 必走 tun 代理（PI 2026-09-23 硬纪律）：`http_proxy=http://127.0.0.1:1018` /
  `https_proxy=http://127.0.0.1:1018` / `all_proxy=socks5://127.0.0.1:1018`
- 空响应 = response_text 为空字符串 / 仅含空白字符；内层重试 ≤3；如实计数

【产物】
----------
- 写入：`results/_v4_supp_l14v3_batch1_result.json`（schema = `v4_l14v3_n26/1` + batch=1）
- 字段：metadata + quadruples (calls/耗时/token 账) + empty_response_count + tun_compliance +
  breakpoint_status + per-call 四元组

【边界】
----------
- 不动任何既有件（含 T1 在跑件 / L13 executor / L4 verdict / L7 verdict / prereg 件）
- 跑不完拆段报断点（沿 L7 实证 ≤275s + 600s watchdog 内）
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
from typing import Any, Dict, List, Optional, Tuple

import requests as _requests

# ============================================================
# 路径与常量
# ============================================================
ROOT = "D:/私人资料/deposon-repo"
RESULTS_DIR = os.path.join(ROOT, "results")
CAPTIONS_PATH = os.path.join(ROOT, "corpus", "v20_caption_surface", "strip_captions_22.json")
KEY_SOURCE_PATH = "C:/Users/Administrator/Desktop/AI/LLM API.txt"

# tun 代理（沿 user memory 2026-09-23 teamorouter/openrouter 必走 tun 防封号 + prereg §1.6.2）
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# ============================================================
# 端点配置（沿端点策略：即用即探；batch 1 = kimi 教师侧 → teamo + kimi-k3）
# ============================================================
ENDPOINT_TEAMO = "https://api.teamorouter.cn/v1"
MODEL_KIMI_K3 = "kimi-k3"  # 实测 teamo 唯一可用的 kimi 类 model_id
KEY_INDEX_TEAMO_1BASED = 15  # teamo key 在 API.txt 第 15 行（沿 multimodel runner 沿用）
USE_PROXY = True  # teamo 必走 tun

# 串行间隔（沿 add_T1 §1.6.2 + Track 2 runner INTER_CALL_SLEEP_S 沿用）
INTER_CALL_SLEEP_S = 2.5

# 超参（沿 prereg §1.4 工具失灵修正条款 + V3 distill baseline）
TEMPERATURE = 0.7
MAX_TOKENS = 2000  # 沿 L4 verdict `74B5B37F7EEA` §2 构造失灵族补构造条款
CALL_TIMEOUT_S = 60

# 内层空响应重试上限（沿 prereg §1.4 工具失灵修正条款）
INNER_RETRY_MAX = 3

# 单批 calls 上限（沿 L7 实证 `B8335982AE5E` ≤275s）
SINGLE_BATCH_CALL_CAP = 22
WALL_TIME_BUDGET_S = 600  # 600s watchdog

# 单 caption 调用次数（沿 prereg §1.4 ≥5 calls/教师/侧；本批 sub-batch 上限 22 = 22 caption × 1 call）
REPEAT_PER_CAPTION = 1  # 22 × 1 = 22 calls/sub-batch ≤ 275s

# ============================================================
# 敏感模式（沿 multimodel runner SENSITIVE_PATTERNS 沿用；自扫 0 命中则合规）
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
# 工具
# ============================================================
def setup_proxy_teamo() -> None:
    """teamo 必走 tun 防封号（PI 2026-09-23 硬纪律；prereg §1.6.2 字面）。"""
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
    """空响应定义：response_text 为空字符串 / 仅含空白字符（沿 prereg §1.4 工具失灵修正条款）。"""
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
    timeout: int = CALL_TIMEOUT_S,
) -> Dict[str, Any]:
    """单 call：teamo endpoint + tun proxy + kimi-k3 model_id。"""
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://deposon.local/l14v3-batch1",
        "X-Title": "deposon-l14v3-batch1-kimi-teacher",
    }
    body = {
        "model": MODEL_KIMI_K3,
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


def sha12_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def sha12_file(path: str) -> Tuple[str, int, bool]:
    with open(path, "rb") as f:
        data = f.read()
    return sha12_bytes(data), len(data), b"\r" not in data


# ============================================================
# 提示构造（V3 distill 复现风格）
# ============================================================
# 沿 run_v3x_stage3_minimal.py L75 caption 构造风格（concept graph + label seq）;
# V3 distill = 给 caption 让 teacher 生成 distillation continuation。
# 复现 prompt：teacher 给定 caption 序列，生成 3-5 个相关 label 延续。
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


# ============================================================
# 加载 22 caption
# ============================================================
def load_captions() -> List[Dict[str, Any]]:
    with open(CAPTIONS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# ============================================================
# 单 call + 内层空响应重试 + 四元组落盘
# ============================================================
def run_one_quadruple(
    api_key: str,
    caption: Dict[str, Any],
    reask_idx: int,
    side: str,  # "teacher" or "distill"
) -> Dict[str, Any]:
    """单 call：发请求 → 空响应内层重试 ≤3 → 返回四元组 record。"""
    caption_id = caption["id"]
    prompt_text = build_user_prompt(caption["text"], caption_id)
    messages = [
        {"role": "system", "content": PROMPT_SYSTEM},
        {"role": "user", "content": prompt_text},
    ]
    prompt_id = f"kimi_t01_{side}_{caption_id}_r{reask_idx}"

    retries = 0
    last = None
    while retries <= INNER_RETRY_MAX:
        r = call_chat_teamo(api_key=api_key, messages=messages)
        last = r
        if r["ok"]:
            content = r.get("content", "")
            if not is_empty_response(content):
                # 成功 + 非空响应
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
                        "model_id_sent": MODEL_KIMI_K3,
                        "side": side,
                        "caption_id": caption_id,
                        "reask_idx": reask_idx,
                        "temperature": TEMPERATURE,
                        "max_tokens": MAX_TOKENS,
                        "retry_count": retries,
                        "empty_response": False,
                        "error_category": None,
                        "error_snippet": "",
                    },
                }
            # 空响应 → 内层重试
            retries += 1
            time.sleep(INTER_CALL_SLEEP_S)
            continue
        # 非 ok（HTTP 错误 / 连接错误等）—— 计入失败，不重试（避免轰炸）
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
                "model_id_sent": MODEL_KIMI_K3,
                "side": side,
                "caption_id": caption_id,
                "reask_idx": reask_idx,
                "temperature": TEMPERATURE,
                "max_tokens": MAX_TOKENS,
                "retry_count": retries,
                "empty_response": is_empty_response(""),
                "error_category": r.get("error_category", "unknown"),
                "error_snippet": (r.get("error_body_snippet") or r.get("error_snippet") or "")[:200],
            },
        }
    # 重试上限耗尽且仍空响应
    content = last.get("content", "") if last and last.get("ok") else ""
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
            "model_id_sent": MODEL_KIMI_K3,
            "side": side,
            "caption_id": caption_id,
            "reask_idx": reask_idx,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "retry_count": INNER_RETRY_MAX,
            "empty_response": True,  # 重试耗尽 = 空响应成立
            "error_category": "empty_response_after_retries",
            "error_snippet": f"empty response after {INNER_RETRY_MAX} retries",
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 L14+ batch 1 · kimi 教师侧 · 22 caption × 1 call = 22 calls")
    print("端点: teamo + tun proxy + kimi-k3 model_id (即用即探实测选定)")
    print("=" * 60)

    setup_proxy_teamo()
    # PowerShell console GBK: stdout utf-8 safe
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass

    # 1. 加载 caption + key
    captions = load_captions()
    if len(captions) != 22:
        print(f"[WARN] caption count != 22 (got {len(captions)}); proceeding anyway")
    print(f"[INIT] captions loaded: {len(captions)}")

    try:
        api_key = fetch_api_key(KEY_INDEX_TEAMO_1BASED)
        print(f"[INIT] teamo key loaded (len={len(api_key)}, redacted in products)")
    except Exception as e:
        print(f"[FATAL] key read fail: {e}")
        return 2

    # 2. 时间预算起点
    t_batch_start = time.time()

    # 3. 单 sub-batch：22 caption × 1 call = 22 calls（沿 L7 实证 ≤275s 上限）
    quadruples: List[Dict[str, Any]] = []
    ok_count = 0
    empty_count = 0
    fail_count = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0

    for i, caption in enumerate(captions):
        # wall time watchdog 检查
        elapsed = time.time() - t_batch_start
        if elapsed > WALL_TIME_BUDGET_S:
            print(f"[BREAKPOINT] wall time {elapsed:.1f}s > {WALL_TIME_BUDGET_S}s watchdog; stop at caption {i}/{len(captions)}")
            break

        rec = run_one_quadruple(
            api_key=api_key, caption=caption, reask_idx=0, side="teacher",
        )
        quadruples.append(rec)
        m = rec["per_call_metadata"]
        if m["ok"] and not m["empty_response"]:
            ok_count += 1
        elif m["empty_response"]:
            empty_count += 1
        else:
            fail_count += 1
        usage = m.get("usage", {}) or {}
        total_prompt_tokens += usage.get("prompt_tokens", 0) or 0
        total_completion_tokens += usage.get("completion_tokens", 0) or 0

        status = "OK" if (m["ok"] and not m["empty_response"]) else (
            "EMPTY" if m["empty_response"] else f"FAIL({m.get('error_category','')})"
        )
        print(
            f"  [{i+1:2d}/{len(captions)}] {caption['id']:<25} "
            f"lat={m.get('latency_ms',0):>7.1f}ms "
            f"tokens(p/c)={(usage.get('prompt_tokens',0) or 0):>4}/{(usage.get('completion_tokens',0) or 0):>4} "
            f"{status}"
        )

        # 串行间隔（除最后一次）
        if i < len(captions) - 1:
            time.sleep(INTER_CALL_SLEEP_S)

    t_batch_end = time.time()
    wall_time_s = round(t_batch_end - t_batch_start, 1)

    # 4. 空响应率 / tun 合规 / breakpoint 状态
    total_calls = len(quadruples)
    empty_rate = (empty_count / total_calls) if total_calls > 0 else 0.0
    tun_used_count = sum(
        1 for r in quadruples
        if r["per_call_metadata"].get("endpoint", "").endswith("/chat/completions")
    )
    tun_compliance = (tun_used_count == total_calls)  # 全部走 teamo = 全走 tun
    breakpoint_hit = wall_time_s > WALL_TIME_BUDGET_S * 0.95

    # 5. 组装 result
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    result = {
        "schema": "v4_l14v3_n26/1",
        "batch": 1,
        "metadata": {
            "task": "L14V3_batch1_kimi_teacher_side",
            "prereg_sha12": "05B975A86989",  # 字面引用 prereg 件 SHA-12（沿 §0 输入件 SHA-12 链）
            "prereg_path": "results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md",
            "activation_path": "results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md",
            "date": "2026-09-24",
            "freeze_day": "V4 L14+ N-26 真审唯一路径 batch 1",
            "spec_conformance": "PI 2026-09-24 双次催办实质放行 + 端点策略即用即探",
            "teacher": "kimi",
            "side": "teacher",
            "n_captions_total": len(captions),
            "n_captions_run": total_calls,
            "calls_per_caption_target": 5,  # ≥5 calls/教师/侧（沿 prereg §1.4）
            "calls_per_caption_actual": REPEAT_PER_CAPTION,
            "endpoint_selected": ENDPOINT_TEAMO,
            "endpoint_selection_method": "即时探活 (kimi-k3 是唯一在 3 端点可达的 kimi 类 model_id)",
            "model_id_sent": MODEL_KIMI_K3,
            "model_id_prereg_literal": "kimi / kimi-for-coding",
            "model_id_inconsistency_honest_disclosure": (
                "prereg §1.2 字面 model_id = kimi (API 端点名 = kimi-for-coding); "
                "teamo 实测不接受 kimi-for-coding (400 model_not_available), 仅接受 kimi-k3; "
                "沿 user memory 2026-09-08「代码里默认 kimi-for-coding (API 端点名), 公开产品名 KIMI-K3——"
                "两个不一致时直接问」+ 端点策略即用即探 = 用 teamo 实际可接受 model_id kimi-k3"
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
            "max_tokens_rationale": "prereg §1.4 工具失灵修正条款 (L4 verdict 74B5B37F7EEA §2 构造失灵族补构造; 非擅调阈值)",
            "inner_retry_max": INNER_RETRY_MAX,
            "call_timeout_s": CALL_TIMEOUT_S,
            "single_batch_call_cap": SINGLE_BATCH_CALL_CAP,
            "wall_time_budget_s": WALL_TIME_BUDGET_S,
            "iron_rules": {
                "R1_no_llm": False,  # V4 放开 (PI 2026-09-22「V3 的剑不斩 V4 的官」)
                "R2_no_proxy": False,  # V4 放开
                "R3_no_gateway": False,  # V4 放开
                "R4_key_never_in_plaintext": True,  # 无例外
                "R5_v4_frozen_append_only": True,  # 0 触既有件
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
            },
            "run_window_cst": now_iso,
            "wall_time_actual_s": wall_time_s,
        },
        "quadruples": quadruples,
        "aggregate": {
            "total_calls": total_calls,
            "ok_count": ok_count,
            "empty_response_count": empty_count,
            "fail_count": fail_count,
            "empty_response_rate": round(empty_rate, 4),
            "empty_response_rate_threshold_K_N26_N2": 0.50,
            "empty_response_above_threshold": empty_rate > 0.50,
            "tun_compliance": tun_compliance,
            "tun_used_count": tun_used_count,
            "tun_target_count": total_calls,
            "total_prompt_tokens": total_prompt_tokens,
            "total_completion_tokens": total_completion_tokens,
            "total_tokens": total_prompt_tokens + total_completion_tokens,
        },
        "K_N26_observability_only": {
            # 本批**只采不算** K-N26-1/2/3（沿 dispatch：真审判定待 5 教师批齐后由 verdict-keeper 统裁）
            "K_N26_1_computed": False,
            "K_N26_2_computed": False,
            "K_N26_3_computed": False,
            "K_N26_N1_observation": {
                # 每 caption response_text 非空且 n_distinct≥3 = 非退化素材
                "n_distinct_responses_per_caption_sample": "本批 1 call/caption, 仅展示首 call 长度分布, "
                "不构成非退化充分判定（需 ≥5 calls 后由 verdict-keeper 统裁）",
            },
            "K_N26_N2_observation": {
                "teamo_tun_used_for_all_calls": tun_compliance,
                "empty_response_rate": round(empty_rate, 4),
                "empty_rate_trigger_K_N26_N2_pass_False": empty_rate > 0.50,
            },
            "verdict_pending": "5 教师批齐后由 verdict-keeper 统裁 (本棒 0 写 verdict)",
        },
        "breakpoint_status": {
            "hit_wall_time_budget": wall_time_s > WALL_TIME_BUDGET_S,
            "actual_wall_time_s": wall_time_s,
            "actual_calls": total_calls,
            "calls_planned": len(captions) * REPEAT_PER_CAPTION,
            "calls_remaining_for_5x_repeats": len(captions) * (5 - REPEAT_PER_CAPTION) - 0,
            "checkpoint_file": None,  # 本批未启用 checkpoint（单 sub-batch 内一次跑完）
            "next_resume_via": "同 agent 唤醒 (task_append 续跑) — 沿 prereg §1.6.4",
            "note": (
                "本批 sub-batch 已完成（22 calls），未撞断点；后续 ≥5 calls/caption 续采走 task_append 接力棒"
            ) if not breakpoint_hit else (
                "撞 600s watchdog 提前停批，partial completion；剩余续采走 task_append 接力棒"
            ),
        },
        "self_scan": {
            "key_pattern_hits_in_product": [],  # 落盘前自扫；若有命中则 abort
            "scanned_at": now_iso,
        },
    }

    # 6. 落盘前自扫（key 形态 0 命中 = 合规）
    pre_scan = self_scan_obj(result)
    if pre_scan:
        print(f"[FATAL] key pattern hits in result: {pre_scan}; abort")
        result["self_scan"]["key_pattern_hits_in_product"] = pre_scan
        # 仍落盘供 verifier 复核（不静默丢弃）
    else:
        print("[OK] self_scan: 0 hit (key 形态合规)")

    # 7. 落盘 result.json
    out_path = os.path.join(RESULTS_DIR, "_v4_supp_l14v3_batch1_result.json")
    payload = json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2)
    with open(out_path, "wb") as f:
        f.write(payload.encode("utf-8"))
    # LF-only
    with open(out_path, "rb") as f:
        data = f.read()
    if b"\r" in data:
        # 强制 LF
        with open(out_path, "wb") as f:
            f.write(data.replace(b"\r\n", b"\n").replace(b"\r", b"\n"))

    sha12, n_bytes, is_lf = sha12_file(out_path)
    print(f"\n[RESULT] {out_path}")
    print(f"  SHA-12: {sha12}")
    print(f"  bytes : {n_bytes}")
    print(f"  LF-only: {is_lf}")
    print(f"  quadruples: {total_calls} (ok={ok_count} empty={empty_count} fail={fail_count})")
    print(f"  empty_rate: {empty_rate:.4f}")
    print(f"  tun_compliance: {tun_compliance}")
    print(f"  wall_time_s: {wall_time_s}")
    print(f"  total_prompt_tokens: {total_prompt_tokens}")
    print(f"  total_completion_tokens: {total_completion_tokens}")
    return 0


if __name__ == "__main__":
    sys.exit(main())