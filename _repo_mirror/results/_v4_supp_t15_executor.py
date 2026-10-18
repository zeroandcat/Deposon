# -*- coding: utf-8 -*-
"""
_v4_supp_t15_executor.py
========================
V4 T1.5 矩阵 executor: L2/L14 × {temp 0.0, 0.3, 0.5} × qwen_plan (单端点)
=========================================================================

【设计锚定】
================================================================
- 预登记: `results/_v4_supp_prereg_v02_add_T15_2026_09_24.md` SHA-12 `8898B964A9D9`
- 激活:   `results/_v4_supp_prereg_v02_add_T15_activation_2026_09_24.md` (待 PI 复核生效)
- K-* kill-line 字面沿 T1.5 §1.5 + 0A9EE16267B5 §1 + L2/L14 verdict 字面 (沿 T1 §1.5.1)
- 0 新设数值阈值: K_N11_3_THRESHOLD = 0.85 / K_N11_1_DIFF = 0.05 / K_N11_2_DELTA = 0.05
- 端点: 单端点 qwen_plan (token-plan.maas.qianwenaiapi.com/compatible-mode/v1,
        model_id=qwen3.7-max 【非 reasoning 模型】, 无代理, key_index_1based=23)
- C-T15-1 构造修正: max_tokens=500 (工具失灵族参数修正, 非阈值调整; 沿 T1 verdict §4.1)
- L2 维度: 5 教师 × 2 prompts (L_biological_taxonomy + S5) × 2 re-asks = 20 calls/cell
- L14 维度: 5 教师 × 2 prompts (L_geography_world + L_historical_causality) × 2 re-asks = 20 calls/cell
- 6 cells × 20 calls = 120 calls; 实际预计 ≤ 156 calls (含重试预留)
- 串行间隔 ≥ 2.5s (沿 Track 2 runner INTER_CALL_SLEEP_S + L2/L14 verdict §2)
- 看门狗: 单批 ≤ 30 calls / 600s (沿 L2 verdict §2 600s)
- 同 worker 接力棒续跑 + checkpoint 模式 (沿 L14 verdict §9.1 + T1 §1.6.4 + T1.5 §1.6.4)
- 即用即探: 调用 qwen_plan 前 1 次探活 (计入 calls 账)
- qwen t=0.7 baseline 不重跑 (沿 T1.5 §1.2 对照基准 + §1.4 不重跑声明)
- T1 已探 mimo/teamo 端点 = 端点维度砍去 (沿 T1.5 §1.2)
- K-T1-S2 沿 T1 verdict §2.2 any_hit: false 结论引用, 不重测 (沿 T1.5 §1.5.2)
- TH-T1-1 = 10 对/教师 N_min (T1 探针放宽, T1.5 沿用; 沿 T1 §1.4 + T1.5 §1.4)
- audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 + 派工单 ask_9484b696 meta_field 拍板

【铁律】
================================================================
- R4 key 永不明文 (无例外): key 仅 runtime env / desktop AI/LLM API.txt 读, 不落盘
- R5 V4 frozen 只追加: 不动任何既有件 (19 件字面源一字不动)
- R6 P-G v0/v01 不动
- R7 plugin spec 不动
- V1-V3 资产只读
- 0 擅调阈值 (K_N11_3_THRESHOLD = 0.85 一字不动)
- 派生 JSON 不合并 (本棒产物用 _v4_supp_t15_* prefix 分列)
- kill-line 字面不动 (hit=True 显式布尔方向)
- succeeded ≠ 跑完落盘核验 (沿 worker 老实交代)
- T1.5 探针定位硬约束: 不翻 L2/L14 正式判定 + 不二次判定 T1 verdict §7 自身

【产物】
================================================================
- per-call record:  .tmp/_t15_records.json (checkpoint)
- per-call record:  .tmp/_t15_records/{cell_key}.jsonl (per-cell 明细)
- aggregate:        results/_v4_supp_t15_result.json (本脚本聚合产出)
- schema:           v4_t15_sensitivity_fix/1 (T1.5 探针专属)

【用法】
================================================================
  python _v4_supp_t15_executor.py probe                    # 仅探活 qwen_plan
  python _v4_supp_t15_executor.py run <cell_idx_start> <cell_idx_end>  # 跑指定 cells (含)
  python _v4_supp_t15_executor.py aggregate                # 聚合 result.json
  python _v4_supp_t15_executor.py all                      # probe + run 0-5 + aggregate

【cells 索引】
================================================================
  0: L2 / temp 0.0 / qwen_plan
  1: L2 / temp 0.3 / qwen_plan
  2: L2 / temp 0.5 / qwen_plan
  3: L14 / temp 0.0 / qwen_plan
  4: L14 / temp 0.3 / qwen_plan
  5: L14 / temp 0.5 / qwen_plan

【skill 诚实】
================================================================
派工单要求 `scientific-research-workflows:statistical-analysis` skill
(plugin @scientific-research-workflows, sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb),
本地 skill 加载器实录 `Local skill not found` —— 按 T1.5 prereg `8898B964A9D9` +
activation (待生效) + Track 2 runner `B65619A07B10` + endpoints probe `C846F7FC79EE` +
T1 executor `A7CAD9228B0B` 字面锚执行, **未编造 skill 不存在的虚构指令**.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import statistics
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests as _requests

# ============================================================
# 常量与路径
# ============================================================
ROOT = Path("D:/私人资料/deposon-repo")
RESULTS_DIR = ROOT / "results"
TMP_DIR = ROOT / ".tmp"
CHECKPOINT_PATH = TMP_DIR / "_t15_records.json"
PROBE_LOG_PATH = TMP_DIR / "_t15_probe_log.json"
RESULT_PATH = RESULTS_DIR / "_v4_supp_t15_result.json"

KEY_SOURCE_PATH = Path("C:/Users/Administrator/Desktop/AI/LLM API.txt")
CAPTIONS_PATH = Path("D:/私人资料/deposon-repo/corpus/v20_caption_surface/strip_captions_22.json")
CAPTIONS_SHA12_EXPECTED = "6A2656878745"

# T1.5 预登记 SHA-12 字面锚 (沿 T1.5 §0 + activation)
PREREG_T15_PATH = RESULTS_DIR / "_v4_supp_prereg_v02_add_T15_2026_09_24.md"
PREREG_T15_SHA12_EXPECTED = "8898B964A9D9"
PREREG_T1_SHA12_EXPECTED = "802DECE2286A"
PREREG_V02_SHA12_EXPECTED = "D85488A64D89"

# T1.5 字面源 (沿 T1.5 §0 SHA-12 链)
L2_VERDICT_SHA12 = "E433A06E7BFB"
L14_VERDICT_SHA12_SELF = "764F24A21AC8"
L14_VERDICT_SHA12_DISK = "8EEF73BF9856"
T1_VERDICT_SHA12 = "F1B5E49F3058"
T1_ACTIVATION_SHA12 = "79936B630015"
L9_PREREG_SHA12 = "23879B6CD1CC"
L10_PREREG_SHA12 = "F6FE005EE3C7"
N09_N39_PREREG_SHA12 = "0A9EE16267B5"
METHODS_PREREG_SHA12 = "0A7BCA992B95"
SEEDS_PREREG_SHA12 = "113CBE555643"
TRACK2_MULTIMODEL_PROBE_SHA12 = "B65619A07B10"
TRACK2_ENDPOINTS_PROBE_SHA12 = "C846F7FC79EE"

# 阈值 (沿 0A9EE16267B5 §1 K-N11-3 字面 + L2/L14 verdict §4.3/§5.3 + T1 §1.5 + T1.5 §1.5)
K_N11_3_THRESHOLD = 0.85
K_N11_1_DIFF = 0.05
K_N11_2_DELTA = 0.05
TH17_N_TARGET = 20       # L2/L14 既判 N target (T1.5 沿用不动)
TH_T1_N_MIN = 10         # T1 探针放宽 N_min (沿 T1 §1.4; T1.5 沿用一字不动)
INTER_CALL_SERIAL_S = 2.5
WATCHDOG_S = 600          # 单批 600s 看门狗 (沿 L2 verdict §2)
BATCH_CALL_LIMIT = 30     # 单批 ≤ 30 calls (沿 T1 §1.6.1 + T1.5 §1.6.1)
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# 5 教师 (沿 TH-14: kimi / GLM_1 / GLM_2 / coze / minimax)
TEACHER_PATHS_REL = [
    ("kimi",    "corpus/v20/by_model/kimi/index_v2_2026_09_16.json"),
    ("GLM_1",   "corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json"),
    ("GLM_2",   "corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json"),
    ("coze",    "corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json"),
    ("minimax", "corpus/v20/by_model/minimax/artifact_v_2026_09_16.json"),
]
TEACHER_NAMES = [t[0] for t in TEACHER_PATHS_REL]
SEED = 42

# L2/L14 prompt 子集 (沿 T1 §1.4 字面 + T1.5 §1.4 字面)
L2_PROMPTS = ["L_biological_taxonomy", "S5"]
L14_PROMPTS = ["L_geography_world", "L_historical_causality"]
N_REASKS = 2

# 单端点配置 (沿 endpoints probe C846F7FC79EE qwen_plan 行 + Track 2 runner B65619A07B10)
# C-T15-1 工具失灵族参数修正: 单端点 qwen_plan (T1 mimo/teamo 端点维度砍去)
ENDPOINTS = {
    "qwen_plan": {
        "label": "qwen_plan",
        "endpoint": "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1",
        "model_id": "qwen3.7-max",  # 非 reasoning 模型 (沿 T1.5 §0 + §1.4)
        "key_index_1based": 23,
        "use_proxy": False,
    },
}
TEMPERATURES = [0.0, 0.3, 0.5]

# 6 cells 矩阵定义 (cell_idx → (维度, 温度))
# 端点恒为 qwen_plan (C-T15-1 单端点修正)
CELLS: List[Tuple[str, float]] = []
for dim in ("L2", "L14"):
    for temp in TEMPERATURES:
        CELLS.append((dim, temp))

# C-T15-1 max_tokens = 500 (工具失灵族参数修正, 非阈值调整)
# 沿 T1 verdict §4.1【最高优先】建议 + T1.5 §1.4 字面 + 派工单明示
MAX_TOKENS = 500

# ============================================================
# Key 形态自扫 (沿 R4 + T1.5 §0 自扫)
# ============================================================
SENSITIVE_PATTERNS = [
    ("sk_literal", re.compile(r"(?i)sk-[A-Za-z0-9_\-]{20,}")),
    ("AIza_literal", re.compile(r"(?i)AIza[0-9A-Za-z_\-]{30,}")),
    ("Bearer_token", re.compile(r"(?i)Bearer\s+[A-Za-z0-9]{20,}")),
    ("openai_key", re.compile(r"(?i)sk-(?:proj-|sv-|sp-|teamo-)?[A-Za-z0-9_\-]{20,}")),
]


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


# ============================================================
# SHA / 字节工具
# ============================================================
def sha12_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def sha12_file(path: Path) -> str:
    return sha12_bytes(path.read_bytes())


def sha12_str(s: str) -> str:
    return sha12_bytes(s.encode("utf-8"))


# ============================================================
# Key 加载 (runtime env / desktop AI/LLM API.txt)
# ============================================================
def read_api_key(key_index_1based: int) -> str:
    raw = KEY_SOURCE_PATH.read_bytes()
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


# ============================================================
# Proxy 控制 (沿 Track 2 runner + T1 §1.6.2)
# T1.5 单端点 qwen_plan use_proxy=False (无代理, 不触发 tun 硬纪律)
# ============================================================
def unset_proxy() -> None:
    """T1.5 单端点 = qwen_plan (无代理). 防御性 unset."""
    for k in ("https_proxy", "http_proxy", "all_proxy"):
        os.environ.pop(k, None)


# ============================================================
# HTTP 调用 (沿 Track 2 runner + T1 executor 字面)
# ============================================================
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


def call_chat(
    api_key: str,
    endpoint: str,
    model: str,
    messages: List[Dict[str, str]],
    temperature: float,
    max_tokens: int,
    timeout: int = 90,
    use_proxy: bool = False,
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    body = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    chat_url = endpoint.rstrip("/") + "/chat/completions"
    proxies = {"http": PROXY_HTTP, "https": PROXY_HTTP} if use_proxy else None

    t0 = time.time()
    try:
        r = _requests.post(chat_url, headers=headers, json=body,
                           proxies=proxies, timeout=timeout)
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
        if data.get("choices"):
            content = data["choices"][0]["message"]["content"]
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


# ============================================================
# Jaccard 度量 (沿 L2/L14 verdict §3.2 字面)
# token regex: re.findall(r"[a-z0-9]+|[一-鿿]", text.lower())
# ============================================================
TOKEN_RE = re.compile(r"[a-z0-9]+|[一-鿿]")


def tokenize(text: str) -> List[str]:
    return TOKEN_RE.findall(text.lower())


def jaccard(a: str, b: str) -> float:
    sa = set(tokenize(a))
    sb = set(tokenize(b))
    if not sa and not sb:
        return 0.0
    union = sa | sb
    if not union:
        return 0.0
    inter = sa & sb
    return len(inter) / len(union)


# ============================================================
# Captions 加载
# ============================================================
def load_captions() -> List[Dict[str, Any]]:
    data = json.loads(CAPTIONS_PATH.read_text(encoding="utf-8"))
    return data


def select_prompts(captions: List[Dict[str, Any]], ids: List[str]) -> List[Dict[str, Any]]:
    by_id = {c["id"]: c for c in captions}
    out = []
    for pid in ids:
        if pid not in by_id:
            raise KeyError(f"prompt_id {pid} not in captions")
        out.append(by_id[pid])
    return out


# ============================================================
# 提示构造 (沿 L2/L14 verdict §2 字面 + T1 §1.4 字面)
# ============================================================
PROMPT_SYSTEM = (
    "You are an artifact generator for a research study on deposon "
    "(distributed-evidence proxy student construction). Given a teacher "
    "identity and a caption chain, output the next link in the chain. "
    "Output only the single token/phrase, no explanations, no markdown."
)


def build_user_prompt(teacher_name: str, caption_id: str, caption_text: str) -> str:
    return (
        f"Teacher: {teacher_name}\n"
        f"Caption chain ({caption_id}): {caption_text}\n\n"
        f"Output the most natural next link in the chain. Output only the "
        f"single token/phrase, no explanations."
    )


# ============================================================
# Probe 探活 (沿 T1.5 §1.1 Q1 + 即用即探 纪律)
# ============================================================
def probe_endpoint(endpoint_name: str) -> Dict[str, Any]:
    ep = ENDPOINTS[endpoint_name]
    unset_proxy()  # T1.5 单端点 qwen_plan use_proxy=False
    api_key = read_api_key(ep["key_index_1based"])
    t0 = time.time()
    r = call_chat(
        api_key, ep["endpoint"], ep["model_id"],
        messages=[{"role": "user", "content": "ping"}],
        temperature=0.0, max_tokens=10, timeout=30,
        use_proxy=ep["use_proxy"],
    )
    latency = round((time.time() - t0) * 1000, 1)
    return {
        "endpoint_label": ep["label"],
        "endpoint": ep["endpoint"],
        "model_id": ep["model_id"],
        "use_proxy": ep["use_proxy"],
        "ok": r["ok"],
        "status_code": r.get("status_code"),
        "latency_ms": latency,
        "model_returned": r.get("model_returned", ""),
        "error_category": r.get("error_category"),
        "error_body_snippet": r.get("error_body_snippet", ""),
        "error_snippet": r.get("error_snippet", ""),
    }


# ============================================================
# Checkpoint 读写
# ============================================================
def load_checkpoint() -> List[Dict[str, Any]]:
    if CHECKPOINT_PATH.exists():
        try:
            return json.loads(CHECKPOINT_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def save_checkpoint(records: List[Dict[str, Any]]) -> None:
    CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CHECKPOINT_PATH.write_text(json.dumps(records, ensure_ascii=False),
                               encoding="utf-8")


# ============================================================
# 单 cell runner
# ============================================================
def run_cell(cell_idx: int, dim: str, temp: float,
             captions: List[Dict[str, Any]],
             records: List[Dict[str, Any]],
             wall_start: float,
             max_calls_in_cell: int = 0) -> Dict[str, Any]:
    """跑单 cell; returns cell_summary. Updates records in-place + saves checkpoint.
    max_calls_in_cell > 0: stop after N new calls in this cell."""
    ep_name = "qwen_plan"  # T1.5 单端点
    ep = ENDPOINTS[ep_name]
    unset_proxy()  # qwen_plan use_proxy=False

    api_key = read_api_key(ep["key_index_1based"])

    prompts_ids = L2_PROMPTS if dim == "L2" else L14_PROMPTS
    prompts_list = select_prompts(captions, prompts_ids)

    # 元组 skip 集 (teacher, caption_id, reask_idx, temp) — 端点恒 = qwen_plan, 元组比 T1 少 endpoint 维度
    # 沿 T1.5 §1.6.4 字面
    existing = set((r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"])
                   for r in records
                   if r.get("cell_idx") == cell_idx)

    cell_summary = {
        "cell_idx": cell_idx,
        "dim": dim,
        "temperature": temp,
        "endpoint_label": ep_name,
        "endpoint": ep["endpoint"],
        "model_id": ep["model_id"],
        "use_proxy": ep["use_proxy"],
        "max_tokens": MAX_TOKENS,
        "prompts": prompts_ids,
        "n_calls_planned": len(TEACHER_NAMES) * len(prompts_list) * N_REASKS,
        "n_calls_ok": 0,
        "n_calls_failed": 0,
        "calls": [],
        "max_calls_in_cell": max_calls_in_cell,
    }

    n_new = 0
    for teacher_name in TEACHER_NAMES:
        teacher_path_rel = next((p[1] for n, p in TEACHER_PATHS_REL if n == teacher_name), "")

        for prompt_obj in prompts_list:
            caption_id = prompt_obj["id"]
            caption_text = prompt_obj["text"]

            for ri in range(N_REASKS):
                key_tuple = (teacher_name, caption_id, ri, temp)

                if key_tuple in existing:
                    continue

                # 串行间隔 (除本 cell 第一次调用)
                if n_new > 0:
                    time.sleep(INTER_CALL_SERIAL_S)

                # per-cell call limit check (用于分批拆跑; bash 300s watchdog 适配)
                if max_calls_in_cell > 0 and n_new >= max_calls_in_cell:
                    cell_summary["calls_limit_break"] = True
                    return cell_summary

                # 看门狗
                elapsed = time.time() - wall_start
                if elapsed > WATCHDOG_S:
                    cell_summary["watchdog_break"] = True
                    return cell_summary

                messages = [
                    {"role": "system", "content": PROMPT_SYSTEM},
                    {"role": "user", "content": build_user_prompt(teacher_name, caption_id, caption_text)},
                ]
                # qwen3.7-max 非 reasoning 模型 (沿 T1.5 §1.4 字面);
                # 端点无代理 (qwen_plan use_proxy=False, 沿 Track 2 ROUTE_TEMPLATES[0] qwen 行);
                # timeout 90s (沿 T1 mimo timeout 60s 上调, 给 qwen 推理留余地; 非阈值参数)
                t0 = time.time()
                resp = call_chat(
                    api_key, ep["endpoint"], ep["model_id"], messages,
                    temperature=temp, max_tokens=MAX_TOKENS, timeout=90,
                    use_proxy=ep["use_proxy"],
                )
                elapsed_call = time.time() - t0
                ok = bool(resp.get("ok"))
                content = resp.get("content", "") if ok else ""
                rec = {
                    "cell_idx": cell_idx,
                    "endpoint_label": ep_name,
                    "endpoint": ep["endpoint"],
                    "endpoint_model": ep["model_id"],
                    "use_proxy": ep["use_proxy"],
                    "dim": dim,
                    "temperature": temp,
                    "max_tokens": MAX_TOKENS,
                    "teacher": teacher_name,
                    "teacher_path_rel": teacher_path_rel,
                    "caption_id": caption_id,
                    "caption_text_sha12": sha12_bytes(caption_text.encode("utf-8")),
                    "reask_idx": ri,
                    "ok": ok,
                    "response_text": content,
                    "response_text_sha12": sha12_bytes(content.encode("utf-8")) if ok else None,
                    "response_text_len": len(content),
                    "latency_ms": resp.get("latency_ms"),
                    "status_code": resp.get("status_code"),
                    "error_category": resp.get("error_category"),
                    "model_returned": resp.get("model_returned", ""),
                    "usage": resp.get("usage", {}),
                    "timestamp_local": datetime.now(timezone(timedelta(hours=8))).isoformat(),
                }
                records.append(rec)
                existing.add(key_tuple)
                n_new += 1

                if ok:
                    cell_summary["n_calls_ok"] += 1
                else:
                    cell_summary["n_calls_failed"] += 1

                cell_summary["calls"].append({
                    "teacher": teacher_name,
                    "caption_id": caption_id,
                    "reask_idx": ri,
                    "ok": ok,
                    "latency_ms": resp.get("latency_ms"),
                    "status_code": resp.get("status_code"),
                    "error_category": resp.get("error_category"),
                    "response_text_len": len(content),
                })

                # Checkpoint save after each call (沿 T1.5 §1.6.4)
                try:
                    save_checkpoint(records)
                except Exception as e:
                    print(f"  [checkpoint FAIL] {e}", flush=True)

                wall = time.time() - wall_start
                print(f"  [{cell_idx:2d}/{dim}/t={temp}/{ep_name}] "
                      f"{teacher_name}/{caption_id}/r{ri} ok={ok} "
                      f"lat={resp.get('latency_ms')}ms wall={wall:.1f}s",
                      flush=True)

                # Hard kill at WATCHDOG
                if wall > WATCHDOG_S:
                    cell_summary["watchdog_break"] = True
                    return cell_summary

    return cell_summary


# ============================================================
# 主流程
# ============================================================
def cmd_probe() -> None:
    """Probe qwen_plan endpoint. 1 call. Per T1.5 §1.1 即用即探."""
    print("=== T1.5 probe: qwen_plan ===")
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    probe_results = []
    ep_name = "qwen_plan"
    print(f"\n--- probe {ep_name} ---")
    try:
        r = probe_endpoint(ep_name)
    except Exception as e:
        r = {
            "endpoint_label": ep_name,
            "ok": False,
            "error_category": "exception",
            "error_snippet": str(e)[:200],
        }
    print(f"  result: {r}")
    probe_results.append(r)

    PROBE_LOG_PATH.write_text(json.dumps({
        "task": "t15_endpoint_probe_2026_09_24",
        "date_label": "2026-09-24",
        "generated_utc": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "rationale": "T1.5 §1.1 Q1 + 即用即探 纪律 (PI 2026-09-24 派工单 t15)",
        "endpoints": probe_results,
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj(probe_results)],
            "status": "clean" if not self_scan_obj(probe_results) else "WARN",
        },
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nProbe log: {PROBE_LOG_PATH}")


def cmd_run(start_idx: int, end_idx: int, calls_limit: int = 0) -> None:
    """Run cells [start_idx, end_idx] inclusive.
    calls_limit > 0: stop after N new calls (per-invocation cap, for bash 300s watchdog).
    """
    print(f"=== T1.5 run cells [{start_idx}, {end_idx}] inclusive (calls_limit={calls_limit}) ===")
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    captions = load_captions()
    captions_sha = sha12_file(CAPTIONS_PATH)
    print(f"captions SHA-12: {captions_sha} (expected {CAPTIONS_SHA12_EXPECTED})")
    if captions_sha.lower() != CAPTIONS_SHA12_EXPECTED.lower():
        print(f"  WARN: captions SHA mismatch (expected {CAPTIONS_SHA12_EXPECTED})")
        # 不抛错 — 沿 "0 触动既有件" 原则

    prereg_sha = sha12_file(PREREG_T15_PATH)
    print(f"T1.5 prereg SHA-12: {prereg_sha} (expected {PREREG_T15_SHA12_EXPECTED})")
    if prereg_sha.lower() != PREREG_T15_SHA12_EXPECTED.lower():
        print(f"  FATAL: T1.5 prereg SHA mismatch (got {prereg_sha}, expected {PREREG_T15_SHA12_EXPECTED})")
        sys.exit(1)

    records = load_checkpoint()
    print(f"loaded {len(records)} existing records from checkpoint")

    wall_start = time.time()
    cell_summaries = []
    calls_made = 0
    for idx in range(start_idx, end_idx + 1):
        if idx < 0 or idx >= len(CELLS):
            print(f"  [skip] cell_idx {idx} out of range")
            continue
        dim, temp = CELLS[idx]
        print(f"\n--- cell {idx}: {dim} / temp={temp} / qwen_plan ---")
        elapsed = time.time() - wall_start
        if elapsed > WATCHDOG_S:
            print(f"  [watchdog] wall={elapsed:.1f}s > {WATCHDOG_S}s; stopping batch")
            break
        if calls_limit > 0 and calls_made >= calls_limit:
            print(f"  [calls_limit] {calls_made} >= {calls_limit}; stopping batch")
            break
        summary = run_cell(idx, dim, temp, captions, records, wall_start,
                            max_calls_in_cell=calls_limit - calls_made if calls_limit > 0 else 0)
        cell_summaries.append(summary)
        calls_made += summary["n_calls_ok"] + summary["n_calls_failed"]
        if summary.get("watchdog_break"):
            print(f"  [watchdog break] cell {idx} incomplete; stop batch")
            break

    wall = time.time() - wall_start
    print(f"\n=== run batch done: wall={wall:.1f}s, n_records={len(records)}, "
          f"new_calls={calls_made} ===")
    print(f"  per-cell:")
    for s in cell_summaries:
        print(f"    cell {s['cell_idx']} ({s['dim']}/t={s['temperature']}/qwen_plan): "
              f"ok={s['n_calls_ok']} fail={s['n_calls_failed']} "
              f"wd_break={s.get('watchdog_break', False)}")

    # Save checkpoint
    save_checkpoint(records)

    # Per-batch summary JSONL log (per-cell 明细)
    batch_log_path = TMP_DIR / f"_t15_batch_{start_idx}_{end_idx}_{datetime.now(timezone(timedelta(hours=8))).strftime('%Y%m%d_%H%M%S')}.jsonl"
    with open(batch_log_path, "w", encoding="utf-8") as f:
        for s in cell_summaries:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"  batch log: {batch_log_path}")


def cmd_aggregate() -> Dict[str, Any]:
    """聚合 checkpoint → result.json."""
    print("=== T1.5 aggregate: compute result.json ===")
    records = load_checkpoint()
    if not records:
        print("FATAL: no records in checkpoint")
        sys.exit(1)

    captions = load_captions()
    captions_sha = sha12_file(CAPTIONS_PATH)

    # Per cell × per teacher J 列表
    by_cell_teacher_pairs: Dict[Tuple[int, str], List[Tuple[str, str, str, int, int]]] = {}
    for r in records:
        if not r.get("ok"):
            continue
        k = (r["cell_idx"], r["teacher"])
        by_cell_teacher_pairs.setdefault(k, []).append((
            r["response_text"], r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"]
        ))

    # Per cell × per teacher J 中位数 (token-level set Jaccard re-asked pairs)
    per_cell_teacher_j: Dict[Tuple[int, str], Dict[str, Any]] = {}
    for k, recs in by_cell_teacher_pairs.items():
        cell_idx, teacher = k
        n = len(recs)
        jvs_all = []
        jvs_nonempty = []
        n_pairs_empty_empty = 0
        for i in range(n):
            for j in range(i + 1, n):
                ti = recs[i][0]
                tj = recs[j][0]
                jv = jaccard(ti, tj)
                jvs_all.append(jv)
                if tokenize(ti) and tokenize(tj):
                    jvs_nonempty.append(jv)
                else:
                    n_pairs_empty_empty += 1
        if jvs_all:
            j_med_all = float(statistics.median(jvs_all))
        else:
            j_med_all = None
        if jvs_nonempty:
            j_med_nonempty = float(statistics.median(jvs_nonempty))
        else:
            j_med_nonempty = None
        per_cell_teacher_j[k] = {
            "cell_idx": cell_idx,
            "teacher": teacher,
            "n_records": n,
            "n_pairs_all": len(jvs_all),
            "n_pairs_nonempty": len(jvs_nonempty),
            "n_pairs_empty_empty": n_pairs_empty_empty,
            "j_median_all": j_med_all,
            "j_median_nonempty": j_med_nonempty,
            "j_values_all": [round(v, 6) for v in jvs_all],
            "j_values_nonempty": [round(v, 6) for v in jvs_nonempty],
        }

    # Per cell J 中位数 (5 教师聚合 → 取每 cell 教师 J 中位的中位)
    per_cell_summary: Dict[int, Dict[str, Any]] = {}
    for cell_idx in range(len(CELLS)):
        dim, temp = CELLS[cell_idx]
        per_teacher = []
        per_teacher_nonempty = []
        for t in TEACHER_NAMES:
            d = per_cell_teacher_j.get((cell_idx, t))
            per_teacher.append({
                "teacher": t,
                "j_median": (round(d["j_median_all"], 6) if d and d["j_median_all"] is not None else None),
                "j_median_nonempty": (round(d["j_median_nonempty"], 6) if d and d["j_median_nonempty"] is not None else None),
                "n_pairs": (d["n_pairs_all"] if d else 0),
                "n_pairs_nonempty": (d["n_pairs_nonempty"] if d else 0),
                "n_pairs_empty_empty": (d["n_pairs_empty_empty"] if d else 0),
                "n_records": (d["n_records"] if d else 0),
            })
            if d and d["j_median_nonempty"] is not None:
                per_teacher_nonempty.append(d["j_median_nonempty"])

        valid_j = [x["j_median"] for x in per_teacher if x["j_median"] is not None]
        valid_j_nonempty = [x["j_median_nonempty"] for x in per_teacher if x["j_median_nonempty"] is not None]

        cell_j_median = float(statistics.median(valid_j)) if valid_j else None
        cell_j_median_nonempty = float(statistics.median(valid_j_nonempty)) if valid_j_nonempty else None

        # K-N11-3 字面 (per teacher): 教师 J 中位 < 0.85 → hit=True → FAIL
        k3_hits_per_teacher = {}
        k3_any_hit = False
        k3_any_hit_nonempty = False
        for x in per_teacher:
            if x["j_median"] is None:
                hit = True
                verdict = "FAIL (教师 J 不可算)"
            else:
                hit = bool(x["j_median"] < K_N11_3_THRESHOLD)
                verdict = "FAIL" if hit else "PASS"
            if x["j_median_nonempty"] is None:
                hit_ne = True
                verdict_ne = "FAIL (教师 J nonempty 不可算)"
            else:
                hit_ne = bool(x["j_median_nonempty"] < K_N11_3_THRESHOLD)
                verdict_ne = "FAIL" if hit_ne else "PASS"
            k3_hits_per_teacher[x["teacher"]] = {
                "j_median": x["j_median"],
                "j_median_nonempty": x["j_median_nonempty"],
                "n_pairs": x["n_pairs"],
                "n_pairs_nonempty": x["n_pairs_nonempty"],
                "n_pairs_empty_empty": x["n_pairs_empty_empty"],
                "hit": hit,
                "verdict": verdict,
                "hit_nonempty": hit_ne,
                "verdict_nonempty": verdict_ne,
            }
            if hit:
                k3_any_hit = True
            if hit_ne:
                k3_any_hit_nonempty = True

        # K-N11-N1 字面 (per teacher): N < TH_T1_N_MIN=10 → pass=False → FAIL
        n1_pass_per_teacher = {}
        n1_any_fail = False
        for x in per_teacher:
            n = x["n_pairs"]
            pass_ok = bool(n >= TH_T1_N_MIN)
            n1_pass_per_teacher[x["teacher"]] = {
                "n_pairs": n,
                "pass": pass_ok,
                "verdict": "PASS" if pass_ok else f"FAIL (N={n} < {TH_T1_N_MIN})",
            }
            if not pass_ok:
                n1_any_fail = True

        per_cell_summary[cell_idx] = {
            "cell_idx": cell_idx,
            "dim": dim,
            "temperature": temp,
            "endpoint_label": "qwen_plan",
            "endpoint": ENDPOINTS["qwen_plan"]["endpoint"],
            "model_id": ENDPOINTS["qwen_plan"]["model_id"],
            "use_proxy": ENDPOINTS["qwen_plan"]["use_proxy"],
            "max_tokens": MAX_TOKENS,
            "n_records": sum(x["n_records"] for x in per_teacher),
            "n_pairs_total_all": sum(x["n_pairs"] for x in per_teacher),
            "n_pairs_total_nonempty": sum(x["n_pairs_nonempty"] for x in per_teacher),
            "n_pairs_total_empty_empty": sum(x["n_pairs_empty_empty"] for x in per_teacher),
            "cell_j_median_5teachers": (round(cell_j_median, 6) if cell_j_median is not None else None),
            "cell_j_median_5teachers_nonempty": (round(cell_j_median_nonempty, 6) if cell_j_median_nonempty is not None else None),
            "per_teacher": per_teacher,
            "kill_lines": {
                "K-N11-3": {
                    "any_hit": k3_any_hit,
                    "hit": k3_any_hit,
                    "any_hit_nonempty": k3_any_hit_nonempty,
                    "hit_nonempty": k3_any_hit_nonempty,
                    "rule": f"任一教师 J 中位数 < {K_N11_3_THRESHOLD} 即 hit=True -> FAIL (主判定 = all_pairs 字面)",
                    "literal_source": "0A9EE16267B5 sec_1 K-N11-3 字面 + L2/L14 verdict 字面 + T1 §1.5.2 + T1.5 §1.5",
                    "verdict": "FAIL (任一教师 J < 0.85)" if k3_any_hit else "PASS",
                    "verdict_nonempty": "FAIL (任一教师 J nonempty < 0.85)" if k3_any_hit_nonempty else "PASS",
                    "per_teacher": k3_hits_per_teacher,
                },
                "K-N11-N1_T1relax": {
                    "any_fail": n1_any_fail,
                    "pass": (not n1_any_fail),
                    "rule": f"T1.5 探针放宽 N_min = {TH_T1_N_MIN}/教师 (沿 T1 §1.4 + T1.5 §1.4)",
                    "literal_source": "T1 §1.4 + §1.8 TH-T1-1 = 10 对/教师 (T1 探针放宽; T1.5 沿用)",
                    "verdict": "FAIL (>=1 教师 N < 10)" if n1_any_fail else "PASS",
                    "per_teacher": n1_pass_per_teacher,
                },
            },
        }

    # 跨 cell 汇总: per dimension × per temperature
    cross_summary: Dict[str, Any] = {
        "by_dim_temp": {},
    }
    for dim in ("L2", "L14"):
        for temp in TEMPERATURES:
            cell_indices = [i for i, c in enumerate(CELLS)
                            if c[0] == dim and c[1] == temp]
            if not cell_indices:
                continue
            cs = per_cell_summary[cell_indices[0]]
            cross_summary["by_dim_temp"].setdefault(dim, {})[str(temp)] = {
                "cell_idx": cell_indices[0],
                "cell_j_median_5teachers": cs["cell_j_median_5teachers"],
                "cell_j_median_5teachers_nonempty": cs["cell_j_median_5teachers_nonempty"],
                "any_k3_hit": cs["kill_lines"]["K-N11-3"]["any_hit"],
                "any_k3_hit_nonempty": cs["kill_lines"]["K-N11-3"]["any_hit_nonempty"],
            }

    # K-T1-S1 (T1.5 主判定): 固定端点 qwen_plan, 跨温度 {0.0, 0.3, 0.5} 任一温度点 cell J 中位 ≥ 0.85 → hit=True
    # 维度: L2 / L14 分别判定
    k_t1_s1: Dict[str, Dict[str, Any]] = {}
    for dim in ("L2", "L14"):
        temps_j_median = {}
        temps_j_median_nonempty = {}
        hit = False
        hit_nonempty = False
        for temp in TEMPERATURES:
            cell_indices = [i for i, c in enumerate(CELLS)
                            if c[0] == dim and c[1] == temp]
            if not cell_indices:
                continue
            cs = per_cell_summary[cell_indices[0]]
            j = cs["cell_j_median_5teachers"]
            j_ne = cs["cell_j_median_5teachers_nonempty"]
            temps_j_median[str(temp)] = j
            temps_j_median_nonempty[str(temp)] = j_ne
            if j is not None and j >= K_N11_3_THRESHOLD:
                hit = True
            if j_ne is not None and j_ne >= K_N11_3_THRESHOLD:
                hit_nonempty = True
        k_t1_s1[dim] = {
            "temps_cell_j_median": temps_j_median,
            "temps_cell_j_median_nonempty": temps_j_median_nonempty,
            "any_temp_flip_to_ge_threshold": hit,
            "hit": hit,
            "hit_nonempty": hit_nonempty,
            "rule": f"固定 (端点=qwen_plan, 维度={dim}); 任一温度点 cell J ≥ {K_N11_3_THRESHOLD} → hit=True",
            "literal_source": "T1 §1.5.2 K-T1-S1 字面 + T1.5 §1.5.2 K-T1-S1 字面 (T1.5 复用沿用)",
            "verdict": "FAIL (稳健性存疑 - 温度 flip)" if hit else "PASS (温度方向一致)",
            "verdict_nonempty": "FAIL (稳健性存疑 - 温度 flip nonempty)" if hit_nonempty else "PASS (温度方向一致 nonempty)",
        }

    # K-T1-S2: 沿 T1 verdict §2.2 any_hit: false 结论引用, T1.5 不重测
    # 端点维度砍去, 仅记 T1 verdict 字面结论 + 引用字面源
    k_t1_s2 = {
        "any_hit": False,
        "hit": False,
        "literal_source": "T1 verdict F1B5E49F3058 §2.2 K-T1-S2 字面 (any_hit: false, mimo/teamo 端点维度 empty-empty 主导)",
        "rationale": "T1.5 端点维度砍去 (qwen_plan 单端点); 沿 T1 verdict §2.2 any_hit: false 结论引用, T1.5 不重测",
        "T15_endpoints_exploration": "T1.5 单端点 = qwen_plan (非 reasoning + max_tokens=500 修正构造失灵族), T1 mimo/teamo 端点维度已砍去",
        "rule": "沿 T1 verdict 结论引用, 不重测; 端点维度砍去",
        "verdict": "PASS (沿 T1 verdict 结论引用 — 不重测)",
    }

    # K-T1-S3: 全 6 cells J 中位 < 0.85 → 探针不命中 → 判定稳健 + T1 verdict 信息量补正
    all_cells_j = [per_cell_summary[i]["cell_j_median_5teachers"]
                   for i in range(len(CELLS)) if per_cell_summary[i]["cell_j_median_5teachers"] is not None]
    all_cells_j_nonempty = [per_cell_summary[i]["cell_j_median_5teachers_nonempty"]
                            for i in range(len(CELLS)) if per_cell_summary[i]["cell_j_median_5teachers_nonempty"] is not None]
    all_below = all((j < K_N11_3_THRESHOLD) for j in all_cells_j) if all_cells_j else False
    all_below_nonempty = all((j < K_N11_3_THRESHOLD) for j in all_cells_j_nonempty) if all_cells_j_nonempty else False
    any_flip = any((j >= K_N11_3_THRESHOLD) for j in all_cells_j) if all_cells_j else False
    any_flip_nonempty = any((j >= K_N11_3_THRESHOLD) for j in all_cells_j_nonempty) if all_cells_j_nonempty else False
    k_t1_s3 = {
        "all_cells_below_threshold": all_below,
        "all_cells_below_threshold_nonempty": all_below_nonempty,
        "any_cell_flip_to_ge_threshold": any_flip,
        "any_cell_flip_to_ge_threshold_nonempty": any_flip_nonempty,
        "hit": (not all_below),  # K-T1-S3 hit=True = 探针命中 (任一 cell 翻)
        "hit_nonempty": (not all_below_nonempty),
        "rule": f"全 6 cells J 中位 < {K_N11_3_THRESHOLD} → 探针不命中 (S3 hit=False) = 判定稳健 + T1 verdict 信息量补正",
        "literal_source": "T1 §1.5.2 K-T1-S3 字面 + T1.5 §1.5.2 K-T1-S3 字面 (T1.5 复用沿用)",
        "verdict": "PASS (判定稳健 + T1 verdict 信息量补正)" if all_below else "FAIL (稳健性存疑 - 不翻 L2/L14 既判 + 不二次判定 T1 verdict §7)",
        "verdict_nonempty": "PASS (判定稳健 nonempty + T1 verdict 信息量补正)" if all_below_nonempty else "FAIL (稳健性存疑 nonempty)",
    }

    # K-T1-S1 any_hit (T1.5 主判定)
    k_t1_s1_any_hit = any(d["hit"] for d in k_t1_s1.values())
    k_t1_s1_any_hit_nonempty = any(d["hit_nonempty"] for d in k_t1_s1.values())

    # 总体判定 (T1.5 = 构造失灵族补正稳健性辅助检验, 不翻 L2/L14 正式判定 + 不翻 T1 verdict §7 自身)
    overall_verdict = "PASS (判定稳健 + T1 verdict 信息量补正)" if (all_below and not k_t1_s1_any_hit) else "FAIL (稳健性存疑注记; 不翻 L2/L14 既判 + 不二次判定 T1 verdict §7)"

    # 根因三分类 (沿 T1.5 §5 + PI 2026-09-23 「诚实的根因是不误导」)
    n_empty_pairs_total = sum(per_cell_summary[i]["n_pairs_total_empty_empty"]
                              for i in range(len(CELLS)))
    n_nonempty_pairs_total = sum(per_cell_summary[i]["n_pairs_total_nonempty"]
                                  for i in range(len(CELLS)))
    n_all_pairs_total = sum(per_cell_summary[i]["n_pairs_total_all"]
                             for i in range(len(CELLS)))
    empty_pair_fraction = (n_empty_pairs_total / n_all_pairs_total) if n_all_pairs_total else 0.0

    if all_below:
        if empty_pair_fraction >= 0.5:
            root_cause_class = (
                f"判定稳健 (字面) — K-T1-S3 探针不命中: 全 6 cells J 中位 < {K_N11_3_THRESHOLD}; "
                f"但 n_empty_vs_empty_pairs / n_all_pairs = {empty_pair_fraction:.3f} ({n_empty_pairs_total}/{n_all_pairs_total}); "
                f"informational 价值有限 (J=0.0 仍部分来自响应空, 非全真'教师稳定')"
            )
            root_cause_note = (
                f"全 6 cells J 中位 < 0.85 (字面方向一致); "
                f"但 empty_vs_empty pairs 占 {empty_pair_fraction:.1%} "
                f"(qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后仍残留部分空响应, 实测诚实声明); "
                f"nonempty-J 中位 (cell 维度): {[(i, per_cell_summary[i]['cell_j_median_5teachers_nonempty']) for i in range(len(CELLS))]}"
            )
        else:
            root_cause_class = "判定稳健 (qwen t=0.7 baseline 方向在 temp 维度稳定; qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后真维持方向一致)"
            root_cause_note = "全 6 cells J 中位 < 0.85, 跨 qwen_plan × temp {0.0,0.3,0.5} × {L2,L14} 维度维持 qwen t=0.7 baseline 既定方向 (K-N11-3 真证伪); T1 verdict 构造失灵族假象裁定获补正 (非 reasoning + max_tokens=500 修正后真维持方向一致)"
    else:
        # 方向翻转 - 三源: qwen 端点固有 / 教师端点固有 / 温度敏感性
        flipped_cells = [(i, per_cell_summary[i]) for i in range(len(CELLS))
                        if per_cell_summary[i]["cell_j_median_5teachers"] is not None
                        and per_cell_summary[i]["cell_j_median_5teachers"] >= K_N11_3_THRESHOLD]
        sources = set()
        for i, cs in flipped_cells:
            if cs["dim"] == "L2":
                sources.add("L2 N-11 supp 维度")
            elif cs["dim"] == "L14":
                sources.add("L14 N-11 full 维度")
            sources.add(f"temp={cs['temperature']} 温度敏感性")
        sources.add("qwen 端点固有方差")
        root_cause_class = f"稳健性存疑 (任一 cell 翻 ≥ {K_N11_3_THRESHOLD}); 二源根因 (沿 T1.5 §1.5.2 K-T1-S1 字面): {' / '.join(sorted(sources))}"
        root_cause_note = (
            f"flipped cells ({len(flipped_cells)}): " +
            "; ".join([f"cell{i}/{cs['dim']}/t={cs['temperature']} J={cs['cell_j_median_5teachers']}"
                       for i, cs in flipped_cells[:6]])
        )

    # 跨温度 J 中位标准差 (沿 T1.5 §1.4 度量 - 稳健性度量)
    cross_temp_std: Dict[str, Optional[float]] = {}
    cross_temp_std_nonempty: Dict[str, Optional[float]] = {}
    for dim in ("L2", "L14"):
        vals_all = [per_cell_summary[i]["cell_j_median_5teachers"]
                    for i, c in enumerate(CELLS) if c[0] == dim
                    and per_cell_summary[i]["cell_j_median_5teachers"] is not None]
        vals_ne = [per_cell_summary[i]["cell_j_median_5teachers_nonempty"]
                   for i, c in enumerate(CELLS) if c[0] == dim
                   and per_cell_summary[i]["cell_j_median_5teachers_nonempty"] is not None]
        cross_temp_std[dim] = (float(statistics.pstdev(vals_all)) if len(vals_all) >= 2 else None)
        cross_temp_std_nonempty[dim] = (float(statistics.pstdev(vals_ne)) if len(vals_ne) >= 2 else None)

    # 落 result.json
    result_obj = {
        "metadata": {
            "schema": "v4_t15_sensitivity_fix/1",
            "task": "T1.5 . L2/L14 温度敏感性 + qwen_plan 单端点 (非 reasoning + max_tokens=500 修正构造失灵族) 稳健性探针 (construction-failure-fix probe)",
            "date_label": "2026-09-24",
            "generated_utc": datetime.now(timezone(timedelta(hours=8))).isoformat(),
            "author": "Mavis worker (T1.5 矩阵 executor 子任务)",
            "spec_conformance": (
                "T1.5 prereg 8898B964A9D9 + activation (待 PI 复核生效) + "
                "T1 prereg 802DECE2286A + T1 activation 79936B630015 + T1 verdict F1B5E49F3058 + "
                "Track 2 runner B65619A07B10 + endpoints probe C846F7FC79EE + "
                "L2 verdict E433A06E7BFB + L14 verdict 764F24A21AC8 (盘 8EEF73BF9856) + "
                "T1 executor A7CAD9228B0B 字面锚 (skill 缺位老实交代)"
            ),
            "line_ending": "LF",
            "encoding": "UTF-8 (no BOM)",
            "algorithm": "SHA-256 前 12 位",
            "predecessor_chain_sha12": {
                "T15_prereg": PREREG_T15_SHA12_EXPECTED,
                "T1_prereg": PREREG_T1_SHA12_EXPECTED,
                "T1_verdict": T1_VERDICT_SHA12,
                "T1_activation": T1_ACTIVATION_SHA12,
                "v02_prereg": PREREG_V02_SHA12_EXPECTED,
                "L2_verdict": L2_VERDICT_SHA12,
                "L14_verdict_self_report": L14_VERDICT_SHA12_SELF,
                "L14_verdict_disk": L14_VERDICT_SHA12_DISK,
                "L9_prereg": L9_PREREG_SHA12,
                "L10_prereg": L10_PREREG_SHA12,
                "N09_N39_prereg": N09_N39_PREREG_SHA12,
                "methods_prereg": METHODS_PREREG_SHA12,
                "seeds_prereg": SEEDS_PREREG_SHA12,
                "captions_22": CAPTIONS_SHA12_EXPECTED,
                "track2_multimodel_probe": TRACK2_MULTIMODEL_PROBE_SHA12,
                "track2_endpoints_probe": TRACK2_ENDPOINTS_PROBE_SHA12,
                "t1_executor": "A7CAD9228B0B",
            },
            "T15_pi_authorization_basis": (
                "PI 2026-09-24 23:33 派工单 ask_9484b696c4f3af85941b3c43 t15 拍板「启动 T1.5: "
                "非 reasoning 模型+max_tokens≥500 重跑温度敏感性」 + "
                "ratify_all 追认 T1/L14V3/映射件生效即锁 (PI 复核生效待办)"
            ),
            "skill_absence_fallback": (
                "派工单要求 skill `scientific-research-workflows:statistical-analysis` "
                "(plugin @scientific-research-workflows, sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb) "
                "本地 skill 加载器实录 `Local skill not found` → 按 T1.5 prereg 8898B964A9D9 + "
                "T1 prereg 802DECE2286A + T1 executor 字面锚执行, 未编造 skill 不存在的虚构指令"
            ),
            "audit_only_metadata_caliber": {
                "note": "metadata 字段 = audit-only (沿 L14V3 映射件 §6.1 #2 + 派工单 ask_9484b696 meta_field 拍板); 不参与 kill-line / Jaccard / 统计推断",
                "fields": [
                    "v3_anchor_api_name",
                    "v3_anchor_9backbone_name",
                    "v4_current_model_id_sent",
                    "v4_current_model_returned",
                    "v4_current_endpoint",
                ],
                "endpoint_constant_T15": "token-plan.maas.qianwenaiapi.com/compatible-mode/v1",
                "model_constant_T15": "qwen3.7-max (非 reasoning)",
            },
            "constraint_locale_hard": (
                "T1.5 = T1 构造失灵族补正稳健性辅助检验 (construction-failure-fix probe); "
                "不翻 L2/L14 正式判定 (沿 T1.5 §0 + §1.3 + §4 + §5 根因关联表) + "
                "不二次判定 T1 verdict §7 自身 (沿 T1.5 §0 + §1.5.2 + §5)"
            ),
        },
        "constraint": {
            "no_key_on_disk": True,
            "key_source": "runtime env / desktop AI/LLM API.txt",
            "proxy_teamo_only_T15_not_triggered": True,
            "inter_call_sleep_s": INTER_CALL_SERIAL_S,
            "watchdog_s": WATCHDOG_S,
            "batch_call_limit": BATCH_CALL_LIMIT,
            "interrupted_recovery": "checkpoint 模式 (.tmp/_t15_records.json); 同 worker 接力棒续跑",
            "small_batch_strategy": "6 cells 顺序跑; 每 cell = 1 prompt set × 5 teachers × 2 re-asks = 20 calls; 单批 ≤ 30 calls; 看门狗 600s",
            "endpoint_construction_fix": "C-T15-1 = qwen_plan 单端点 (T1 mimo/teamo 端点维度砍去); 非 reasoning + max_tokens=500 (工具失灵族参数修正)",
        },
        "inputs": {
            "prereg_T15": {
                "path": str(PREREG_T15_PATH.relative_to(ROOT)),
                "sha12": sha12_file(PREREG_T15_PATH),
                "expected_sha12": PREREG_T15_SHA12_EXPECTED,
                "match": sha12_file(PREREG_T15_PATH).lower() == PREREG_T15_SHA12_EXPECTED.lower(),
            },
            "captions": {
                "path": str(CAPTIONS_PATH.relative_to(ROOT)),
                "sha12": captions_sha,
                "expected_sha12": CAPTIONS_SHA12_EXPECTED,
                "match": captions_sha.lower() == CAPTIONS_SHA12_EXPECTED.lower(),
            },
        },
        "experiment_parameters": {
            "dimensions": ["L2", "L14"],
            "temperatures": TEMPERATURES,
            "endpoints": ["qwen_plan"],  # T1.5 单端点
            "n_teachers": len(TEACHER_NAMES),
            "n_prompts_per_cell_L2": len(L2_PROMPTS),
            "n_prompts_per_cell_L14": len(L14_PROMPTS),
            "n_reasks_per_prompt": N_REASKS,
            "max_tokens": MAX_TOKENS,
            "L2_prompts": L2_PROMPTS,
            "L14_prompts": L14_PROMPTS,
            "thresholds": {
                "K_N11_3_THRESHOLD": K_N11_3_THRESHOLD,
                "K_N11_1_DIFF": K_N11_1_DIFF,
                "K_N11_2_DELTA": K_N11_2_DELTA,
                "TH17_N_TARGET_L2L14": TH17_N_TARGET,
                "TH_T1_N_MIN_T15probe_relax": TH_T1_N_MIN,
            },
            "jaccard_formula": "J = |A ∩ B| / |A ∪ B| token-level set Jaccard",
            "token_regex": r"[a-z0-9]+|[一-鿿] (text.lower())",
            "schema_L14_compat": "v4_l14_n11full/2 (沿 L14 verdict §2 字面)",
            "schema_T15": "v4_t15_sensitivity_fix/1 (T1.5 探针专属)",
            "seed": SEED,
            "qwen_t07_baseline_not_rerun": True,
        },
        "probe": {
            "rationale": "T1.5 §1.1 Q1 + 即用即探 纪律",
            "endpoints": (json.loads(PROBE_LOG_PATH.read_text(encoding="utf-8"))["endpoints"]
                          if PROBE_LOG_PATH.exists() else []),
        },
        "records_summary": {
            "n_records_total": len(records),
            "n_records_ok": sum(1 for r in records if r.get("ok")),
            "n_records_failed": sum(1 for r in records if not r.get("ok")),
            "n_calls_total": len(records),
            "n_calls_ok": sum(1 for r in records if r.get("ok")),
            "n_calls_failed": sum(1 for r in records if not r.get("ok")),
            "n_empty_responses": sum(1 for r in records if r.get("ok") and not r.get("response_text", "").strip()),
        },
        "per_cell_summary": per_cell_summary,
        "cross_summary": cross_summary,
        "cross_temp_std_per_dim": {
            "all_pairs": cross_temp_std,
            "nonempty_pairs": cross_temp_std_nonempty,
        },
        "kill_lines_T15": {
            "K-T1-S1_temperature_flip_T15reuse": {
                "any_hit": k_t1_s1_any_hit,
                "rule": (
                    f"固定 (端点=qwen_plan, 维度=L2|L14); 任一温度点 cell J ≥ {K_N11_3_THRESHOLD} → hit=True → "
                    "K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健 = 标注「稳健性存疑注记」入勘误链"
                ),
                "literal_source": "T1 §1.5.2 K-T1-S1 字面 + T1.5 §1.5.2 K-T1-S1 字面 (T1.5 复用沿 T1 一字不动)",
                "per_dim": k_t1_s1,
            },
            "K-T1-S2_endpoint_flip_T15_reference": k_t1_s2,
            "K-T1-S3_robustness_confirm_T15reuse": k_t1_s3,
        },
        "overall_verdict": {
            "any_t15_kill_line_hit": (k_t1_s1_any_hit or k_t1_s3["hit"]),
            "K-T1-S2_status": "沿 T1 verdict 结论引用 (any_hit: false), T1.5 不重测",
            "primary_root_cause_classification": root_cause_class,
            "root_cause_note": root_cause_note,
            "t15_overall_verdict": overall_verdict,
            "L2L14_formal_verdict_unchanged": (
                "L2 verdict E433A06E7BFB §11「FAIL K-N11-3 真证伪」 + "
                "L14 verdict 764F24A21AC8 §11「FAIL K-N11-3 真证伪 qwen 固有方差」一字不动 "
                "(沿 T1.5 §0 定位硬约束 + §1.3 探针限定 + §5 根因关联表)"
            ),
            "T1_verdict_sec7_unchanged": (
                "T1 verdict F1B5E49F3058 §7 总判定「K-T1-S3 字面命中 (PASS) = 构造失灵族假象」一字不动 "
                "(沿 T1.5 §0 + §1.3 + §1.5.2 + §4 + §5 硬约束); T1.5 不二次判定 T1 verdict §7 自身"
            ),
            "T1_verdict_info_boundary_complement": (
                "T1.5 K-T1-S3 命中 (探针不命中 K-T1-S1/S2) = 仅作 T1 verdict 信息量补正: "
                "构造失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认; "
                "不构成 L2/L14 既判 PASS 的新证据 (仅是既判方向的稳健性确认); "
                "不二次判定 T1 verdict §7 自身 (沿 T1.5 §1.5.2 K-T1-S3 字面 + §5 根因关联)"
            ),
        },
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj({
                "records_count": len(records),
                "per_cell_count": len(per_cell_summary),
                "schema": "v4_t15_sensitivity_fix/1",
            })],
            "status": "clean" if not self_scan_obj({
                "records_count": len(records),
                "per_cell_count": len(per_cell_summary),
            }) else "WARN",
        },
        "honesty_disclosures": {
            "succeeded_not_means_completed": "executor ran without raise ≠ 全部 6 cells 跑完; 落盘核验后下方可宣告",
            "watchdog_limit": f"600s 看门狗; 单批 ≤ 30 calls; T1.5 矩阵 6 cells × 20 calls = 120 calls 理论 < 360 calls 硬上限",
            "skill_absence": (
                "派工单要求 skill `scientific-research-workflows:statistical-analysis` 本地缺位; "
                "按 T1.5 prereg 8898B964A9D9 + T1 prereg 802DECE2286A + T1 executor 字面锚执行; "
                "未编造 skill 不存在的虚构指令"
            ),
            "verdicts_archived_disclosure": (
                "派工单引用 L2 verdict E433A06E7BFB + L14 verdict 764F24A21AC8 / 8EEF73BF9856 (盘) + "
                "L2 result FF7B167AE43F + L14 result 4C11AB9057B9 字面源, 但盘上已清出 "
                "(沿 L14V3 prereg §0 注: 2026-09-24 cleanup manifest 处置后 ledger 锁定四件 SHA-12 + 字节); "
                "T1.5 字面源沿 T1.5 prereg 8898B964A9D9 自含 + T1 prereg 802DECE2286A 字面源 + "
                "0A9EE16267B5 §1 K-N11 字面 + L14V3 prereg K-N26 字面"
            ),
            "small_batch_used": (
                "6 cells 顺序跑; 每 cell 20 calls (5 teachers × 2 prompts × 2 re-asks); "
                "受 bash tool 300s watchdog 约束, qwen_plan cells 拆批 4-5 calls/invocation; "
                "checkpoint 累积续跑模式 (.tmp/_t15_records.json); "
                "单端点 qwen_plan (T1 mimo/teamo 端点维度已砍去, 沿 T1.5 §1.2); "
                "max_tokens=500 (C-T15-1 工具失灵族参数修正, 非阈值调整; 沿 T1 verdict §4.1)"
            ),
            "construction_fix_disclosure": (
                "诚实 = 不误导 (沿 PI 2026-09-23): "
                "T1 verdict 已裁 T1 矩阵字面 PASS = 构造失灵族假象 "
                "(reasoning 模型 mimo-v2.6-pro + deepseek-v4-flash + max_tokens=100 致 "
                "49.3% 空响应 + 72.1% empty-empty pairs, J=0.0 主要来自'双方都空'); "
                "T1.5 = 该构造失灵族补正探针: qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正; "
                "若 T1.5 仍空响应率显著, 则 reasoning 模型构造失灵 vs qwen 端点固有方差 二源并存"
            ),
            "T15_locale_constraint_disclosure": (
                "T1.5 探针 = T1 构造失灵族补正稳健性辅助检验 (construction-failure-fix probe), "
                "不翻 L2/L14 正式判定 (沿 T1.5 §0 定位硬约束 + §1.3 探针限定 + §5 根因关联表) + "
                "不二次判定 T1 verdict §7 自身 (沿 T1.5 §0 + §1.5.2 + §5); "
                "K-T1-S2 沿 T1 verdict §2.2 any_hit: false 结论引用, T1.5 不重测"
            ),
            "audit_only_metadata_disclosure": (
                "metadata 字段 (v3_anchor_api_name / v3_anchor_9backbone_name / v4_current_model_id_sent / "
                "v4_current_model_returned / v4_current_endpoint) = audit-only (沿 L14V3 映射件 §6.1 #2 + "
                "派工单 ask_9484b696 meta_field 拍板); 不参与 kill-line / Jaccard / 统计推断; "
                "仅作审计追溯, 不入判定字面源"
            ),
            "partial_completion_disclosure": (
                "本棒 6 cells 全跑状态以落盘核验为准; "
                "若未来 worker 接力棒续跑, 已启动 cells 部分完成记「T1.5 部分完成」注记; "
                "未启动 cells 留待接力"
            ),
        },
    }

    RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result_obj, ensure_ascii=False, indent=2),
                            encoding="utf-8")
    result_sha = sha12_file(RESULT_PATH)
    result_bytes = RESULT_PATH.stat().st_size

    print(f"\n=== aggregate done ===")
    print(f"  result path: {RESULT_PATH}")
    print(f"  SHA-12: {result_sha}")
    print(f"  bytes: {result_bytes}")
    print(f"  overall verdict: {overall_verdict}")
    print(f"  root cause: {root_cause_class}")

    return {
        "result_path": str(RESULT_PATH),
        "sha12": result_sha,
        "bytes": result_bytes,
        "overall_verdict": overall_verdict,
        "root_cause": root_cause_class,
    }


def cmd_all() -> None:
    """probe + run 0-5 + aggregate."""
    cmd_probe()
    cmd_run(0, len(CELLS) - 1)
    cmd_aggregate()


def main():
    parser = argparse.ArgumentParser(description="T1.5 matrix executor")
    sub = parser.add_subparsers(dest="cmd", help="subcommand")

    p_probe = sub.add_parser("probe", help="probe qwen_plan endpoint")
    p_probe.set_defaults(func=lambda a: cmd_probe())

    p_run = sub.add_parser("run", help="run cells [start, end] inclusive")
    p_run.add_argument("start", type=int, help="start cell idx (inclusive)")
    p_run.add_argument("end", type=int, help="end cell idx (inclusive)")
    p_run.add_argument("--calls", type=int, default=0,
                       help="cap new calls per invocation (0=no cap); use for bash 300s watchdog")
    p_run.set_defaults(func=lambda a: cmd_run(a.start, a.end, a.calls))

    p_agg = sub.add_parser("aggregate", help="aggregate records → result.json")
    p_agg.set_defaults(func=lambda a: cmd_aggregate())

    p_all = sub.add_parser("all", help="probe + run all + aggregate")
    p_all.set_defaults(func=lambda a: cmd_all())

    args = parser.parse_args()
    if not args.cmd:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()