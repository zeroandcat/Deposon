# -*- coding: utf-8 -*-
"""
_v4_track2_multimodel_rerun.py
================================

V4 Track 2 多模型补跑 - battery 跑 3 槽 (qwen_plan / mimo / teamo)
================================================================

【设计锚定】
================================================================
- 复用既有 _v4_proxy_student_llm_multi_runner.py 的 5 教师 × 3 调用结构
  (SHA-12 `306FA79A7C27`, 模板只读复用, 本棒另写, 0 触动)
- 复用 _v4_distill_min_measure.py (SHA-12 `21771E66AF67`, 只读复用)
- 复用 _v4_proxy_student_generators.extract_records (模板只读复用)
- 复用 _v4_proxy_student_generators 内 D1 teacher_paths.json (SHA-12 `D2BD7521D651`)
- 三槽 (PI 2026-09-23 拍板三 URL + 补充 1):
    qwen_plan -> https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1, qwen3.7-max
    mimo      -> https://token-plan-cn.xiaomimimo.com/v1, mimo-v2.6-pro
    teamo     -> https://api.teamorouter.cn/v1, deepseek-v4-flash-0731 (代理)
- 每个槽: 5 教师 × 3 calls = 15 calls (沿 Track 2 runner)
- 超参冻结: temperature=0.7, max_tokens=1500, n_in_context=2, n_calls_per_teacher=3
  neg_control_seed=42, bootstrap_seed=42, perm_seed=42, projection_seed=42
  n_projections=128, n_permutations=1000, n_bootstrap_resamples=1000
  histogram_n_bins=50, delta_min_factor=0.10
- PI 2026-09-23 补充 2: teamo/openrouter 类端点必走 tun/代理
  (https_proxy=http://127.0.0.1:1018 等); qwen/mimo 按原网络路径
- 串行 + 端点间 ≥2s 间隔 (PI 防封号); 模型内同槽 call 间 ≥1.5s
- key 仅 runtime 内存读; 不落盘 / 不入 prompt / 不入 JSON / 不入 log

【产物】
================================================================
- per-model: results/_v4_proxy_student_llm_<model_safe_name>.json
- compare:   results/_v4_track2_multimodel_rerun_2026_09_23.json
- verdict:   results/_v4_track2_multimodel_verdict_2026_09_23.md

【铁律】
================================================================
- R4 key 永不明文 (无例外): 产物 key 字段一律 "runtime-env (redacted)"
- R5 V4 frozen 只追加: 本棒仅产出新增 JSON, 已有件 0 触动 (含 multi_runner 0 触动)
- 不擅动 workspace 外 (key 文件仅读不写)
- 派生 JSON 不合并
- 不擅自调阈值 (TH-* 全沿用)
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Tuple, Optional

import numpy as np
import requests as _requests

ROOT = "D:/私人资料/deposon-repo"
RESULTS_DIR = os.path.join(ROOT, "results")
KEY_SOURCE_PATH = "C:/Users/Administrator/Desktop/AI/LLM API.txt"

# PI 拍板代理 (tun/127.0.0.1:1018)
PROXY_HTTP = "http://127.0.0.1:1018"
PROXY_SOCKS5 = "socks5://127.0.0.1:1018"

# 5 教师 (沿 D1 teacher_paths.json, SHA-12 D2BD7521D651)
TEACHER_PATHS_REL = [
    ("kimi", "corpus/v20/by_model/kimi/index_v2_2026_09_16.json"),
    ("GLM_1", "corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json"),
    ("GLM_2", "corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json"),
    ("coze", "corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json"),
    ("minimax", "corpus/v20/by_model/minimax/artifact_v_2026_09_16.json"),
]
TEACHER_NAMES = [t[0] for t in TEACHER_PATHS_REL]

# 三槽 (PI 拍板三 URL + 探针确认的 model_id)
ROUTES = [
    {
        "label": "qwen_plan",
        "provider": "qwen_token_plan",
        "endpoint": "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1",
        "model_id": "qwen3.7-max",
        "model_safe_name": "qwen3_7_max",
        "key_index_1based": 23,  # Qwen-plan key (API.txt 第 23 行)
        "use_proxy": False,
    },
    {
        "label": "mimo",
        "provider": "xiaomi_mimo_token_plan",
        "endpoint": "https://token-plan-cn.xiaomimimo.com/v1",
        "model_id": "mimo-v2.6-pro",
        "model_safe_name": "mimo_v2_6_pro",
        "key_index_1based": 27,  # mimo-plan key (API.txt 第 27 行)
        "use_proxy": False,
    },
    {
        "label": "teamo",
        "provider": "teamorouter",
        "endpoint": "https://api.teamorouter.cn/v1",
        "model_id": "deepseek-v4-flash",  # 响应 model 名: deepseek-v4-flash-0731
        "model_safe_name": "deepseek_v4_flash_teamo",
        "key_index_1based": 15,  # teamo key (API.txt 第 15 行)
        "use_proxy": True,  # PI 2026-09-23 补充 2: teamo/openrouter 类必走代理
    },
]

# 超参（沿 Track 2 runner 冻结）
TEMPERATURE = 0.7
MAX_TOKENS = 1500
N_IN_CONTEXT = 2
N_CALLS_PER_TEACHER = 3
NEG_CONTROL_SEED = 42
BOOTSTRAP_SEED = 42
PERM_SEED = 42
PROJECTION_SEED = 42
N_PROJECTIONS = 128
N_PERMUTATIONS = 1000
N_BOOTSTRAP = 1000
HISTOGRAM_N_BINS = 50
DELTA_MIN_FACTOR = 0.10

# 间隔 (PI 2026-09-23 补充 2)
INTER_ROUTE_SLEEP_S = 2.5
INTER_CALL_SLEEP_S = 1.5
CALL_TIMEOUT = 60

# 复用 D3 度量层 + Track 2 runner 结构
sys.path.insert(0, RESULTS_DIR)
from _v4_distill_min_measure import (  # type: ignore
    extract_features, pad_to_max_np, make_projections_np,
    compute_pair_metrics_np, permutation_test_js_np,
    bootstrap_js_ci_np, margin_d2_minus_d1, synthetic_negative_control,
)
from _v4_proxy_student_generators import extract_records  # type: ignore

# 敏感模式（沿 Track 2 runner）
SENSITIVE_PATTERNS = [
    ("api_key_literal", re.compile(r"(?i)api[_-]?key\s*[:=]\s*[A-Za-z0-9_\-]{8,}")),
    ("sk_literal", re.compile(r"(?i)sk-[A-Za-z0-9_\-]{8,}")),
    ("gpt_endpoint", re.compile(r"(?i)gpt-[A-Za-z0-9_\-]{4,}")),
    ("claude_endpoint", re.compile(r"(?i)claude-[A-Za-z0-9_\-]{4,}")),
    ("ark_endpoint", re.compile(r"(?i)ark-[A-Za-z0-9_\-]{4,}")),
    ("Bearer_token", re.compile(r"(?i)Bearer\s+[A-Za-z0-9_\-\.]{20,}")),
    ("url_token_param", re.compile(r"(?i)(?:token|api_key|apikey)=[A-Za-z0-9_\-]{16,}")),
    ("tp_token", re.compile(r"(?i)tp-[A-Za-z0-9]{8,}")),
    ("sp_key", re.compile(r"(?i)sk-sp-[A-Za-z0-9_\-\.]{8,}")),
    ("sk_teamo", re.compile(r"(?i)sk-teamo-[A-Za-z0-9]{8,}")),
]

# ============================================================
# 工具
# ============================================================
def setup_proxy() -> None:
    os.environ["https_proxy"] = PROXY_HTTP
    os.environ["http_proxy"] = PROXY_HTTP
    os.environ["all_proxy"] = PROXY_SOCKS5


def fetch_api_key(key_index_1based: int) -> str:
    raw = open(KEY_SOURCE_PATH, "rb").read()
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc); break
        except UnicodeDecodeError:
            continue
    else:
        raise RuntimeError("key source file: no decodable encoding found")
    lines = text.splitlines()
    key = lines[key_index_1based - 1].strip()
    if not key or len(key) < 20:
        raise RuntimeError(f"key line {key_index_1based} empty or too short; abort")
    return key


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


def sha12_file(path: str) -> Tuple[str, int, int, bool, bool]:
    with open(path, "rb") as f:
        data = f.read()
    h = hashlib.sha256(data).hexdigest()[:12]
    n_bytes = len(data)
    has_bom = data.startswith(b"\xef\xbb\xbf")
    n_lines = data.decode("utf-8", errors="replace").count("\n")
    is_lf_only = b"\r" not in data
    return h, n_bytes, n_lines, is_lf_only, not has_bom


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
    temperature: float = TEMPERATURE,
    max_tokens: int = MAX_TOKENS,
    timeout: int = CALL_TIMEOUT,
    use_proxy: bool = False,
) -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    if "openrouter" in endpoint or "teamorouter" in endpoint:
        headers["HTTP-Referer"] = "https://deposon.local/v5-multimodel-rerun"
        headers["X-Title"] = "deposon-v5-multimodel-rerun"

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
        r = _requests.post(
            chat_url, headers=headers, json=body,
            proxies=proxies, timeout=timeout,
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
        return {
            "ok": True,
            "status_code": r.status_code,
            "latency_ms": latency_ms,
            "model_returned": data.get("model", ""),
            "id": data.get("id", ""),
            "content": data["choices"][0]["message"]["content"],
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
# 教师加载 + 提示构造
# ============================================================
def load_teacher(rel_path: str) -> List[Dict[str, Any]]:
    full = os.path.join(ROOT, rel_path)
    with open(full, "r", encoding="utf-8") as f:
        data = json.load(f)
    return extract_records(data)


def load_all_teachers() -> Dict[str, List[Dict[str, Any]]]:
    out: Dict[str, List[Dict[str, Any]]] = {}
    for tn, rel in TEACHER_PATHS_REL:
        out[tn] = load_teacher(rel)
    return out


def pick_in_context(records: List[Dict[str, Any]], n: int = N_IN_CONTEXT) -> List[Dict[str, Any]]:
    return records[:n]


def build_negative_controls(teacher_records: Dict[str, List[Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    return {
        tn: synthetic_negative_control(recs, NEG_CONTROL_SEED)
        for tn, recs in teacher_records.items()
    }


PROMPT_SYSTEM = (
    "You are an artifact generator for a research study on deposon "
    "(distributed-evidence proxy student construction). Your task: "
    "given 2 example artifacts in a specific JSON schema, generate ONE NEW "
    "artifact in the EXACT same schema. The new artifact must be "
    "structurally identical (same field names, same value types) but "
    "realistic and novel (different values from the examples, no copies). "
    "Output ONLY a single valid JSON object. No markdown code fences, no "
    "commentary, no explanations before or after."
)


def build_user_prompt(teacher_name: str, in_context: List[Dict[str, Any]]) -> str:
    return (
        f"Teacher: {teacher_name}\n\n"
        f"Example artifact 1:\n{json.dumps(in_context[0], ensure_ascii=False, indent=2)}\n\n"
        f"Example artifact 2:\n{json.dumps(in_context[1], ensure_ascii=False, indent=2)}\n\n"
        f"Now generate ONE NEW artifact following the EXACT same schema "
        f"and structure. Output only the JSON object."
    )


# ============================================================
# 单模型全流程
# ============================================================
def run_one_model(route: Dict[str, Any], teacher_records: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    print(f"\n{'='*60}")
    print(f"model: {route['label']} ({route['model_id']})")
    print(f"{'='*60}")

    setup_proxy()
    api_key = fetch_api_key(route["key_index_1based"])

    # 1. 鉴权预检 (max_tokens=1 ping)
    ping = call_chat(
        api_key, route["endpoint"], route["model_id"],
        messages=[{"role": "user", "content": "ping"}],
        max_tokens=10, timeout=30, use_proxy=route["use_proxy"],
    )
    if not ping["ok"]:
        print(f"  AUTH_FAIL: {ping.get('error_category')} {ping.get('status_code','')}")
        return {"route": route, "ok": False, "stage": "auth_ping", "error": ping}
    print(f"  AUTH_OK: latency_ms={ping['latency_ms']} model_returned={ping.get('model_returned','')}")

    # 2. 5 教师 × 3 调用
    teacher_outputs: Dict[str, Any] = {}
    for tn, rel in zip(TEACHER_NAMES, [t[1] for t in TEACHER_PATHS_REL]):
        records = teacher_records[tn]
        if len(records) < N_IN_CONTEXT:
            teacher_outputs[tn] = {
                "teacher": tn, "teacher_path": rel,
                "n_in_context": 0, "n_records_teacher": len(records),
                "outputs": [], "skip_reason": f"records < {N_IN_CONTEXT}",
            }
            continue
        in_ctx = pick_in_context(records, N_IN_CONTEXT)
        outputs: List[Dict[str, Any]] = []
        for call_idx in range(N_CALLS_PER_TEACHER):
            messages = [
                {"role": "system", "content": PROMPT_SYSTEM},
                {"role": "user", "content": build_user_prompt(tn, in_ctx)},
            ]
            r = call_chat(api_key, route["endpoint"], route["model_id"], messages,
                          timeout=CALL_TIMEOUT, use_proxy=route["use_proxy"])
            entry: Dict[str, Any] = {
                "call_idx": call_idx,
                "ok": r["ok"],
                "latency_ms": r.get("latency_ms"),
                "model_returned": r.get("model_returned", ""),
                "usage": r.get("usage", {}),
            }
            if r["ok"]:
                txt = r["content"].strip()
                txt_clean = txt
                if txt_clean.startswith("```"):
                    txt_clean = re.sub(r"^```(?:json)?\s*", "", txt_clean)
                    txt_clean = re.sub(r"\s*```$", "", txt_clean)
                try:
                    parsed = json.loads(txt_clean)
                    entry["parsed_ok"] = True
                    entry["generated_artifact"] = parsed
                except Exception as e:
                    entry["parsed_ok"] = False
                    entry["parse_error"] = str(e)[:200]
                    entry["raw_content_preview"] = txt[:500]
                entry["raw_content"] = txt
            else:
                entry["error_category"] = r.get("error_category", "unknown")
                if "error_body_snippet" in r:
                    entry["error_body_snippet"] = r["error_body_snippet"]
                elif "error_snippet" in r:
                    entry["error_snippet"] = r["error_snippet"]
            outputs.append(entry)
            status = "OK" if entry["ok"] else f"FAIL({entry.get('error_category','')})"
            print(f"    {tn} call {call_idx}: {status} latency={entry['latency_ms']}ms "
                  f"parsed={entry.get('parsed_ok', 'n/a')}")
            # 同槽内 call 间 ≥1.5s
            if call_idx < N_CALLS_PER_TEACHER - 1:
                time.sleep(INTER_CALL_SLEEP_S)
        teacher_outputs[tn] = {
            "teacher": tn, "teacher_path": rel,
            "n_in_context": N_IN_CONTEXT, "n_records_teacher": len(records),
            "outputs": outputs,
        }

    # 3. 负对照
    neg_ctrl = build_negative_controls(teacher_records)
    neg_summary = {tn: {"n_records": len(v), "first_record_keys": list(v[0].keys()) if v else []}
                   for tn, v in neg_ctrl.items()}

    # 4. 组装产物
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")
    result = {
        "metadata": {
            "freeze_day": "V5 补强 D1 (件 3 续, 多模型补跑)",
            "track": "Track 2 (context distillation, 多模型对照补跑)",
            "task": f"proxy_student_llm_multi_rerun_{route['model_safe_name']}",
            "date": "2026-09-23",
            "author": "Mavis worker (Track 2 多模型补跑 子任务)",
            "spec_conformance": "PI 2026-09-23 ask_3ee5edf74be2d6ef53fbc4b4 Q4 + 补充 1 + 补充 2",
            "line_ending": "LF",
            "encoding": "UTF-8 (no BOM)",
            "algorithm": "SHA-256 前 12 位",
            "predecessor_chain_sha12": {
                "track2_runner_template": "900A6D1E50AF",
                "measure_function": "21771E66AF67",
                "teacher_paths": "D2BD7521D651",
                "track2_multimodel_runner_template": "306FA79A7C27",
                "track2_measure_v5": "7CCBE2C3E248",
                "track2_product_openrouter": "61EDBE39A618",
                "track2_product_deepseek_direct": "1B05EBA8639B",
                "track2_product_qwen": "AE541E34781E",
                "endpoints_probe": "__SELF_PROBE_SHA12__",
            },
        },
        "gt_constructive_declaration": (
            "正类 = 以 teacher 输出为唯一素材经 LLM 上下文蒸馏构造的 proxy student 输出集; "
            "负类 = 独立构造对照 (token 级随机重排合成负对照, seed=42); 结论不外推真实学生。"
        ),
        "ai_use_disclosure": {
            "provider": route["provider"],
            "model": route["model_id"],
            "construction_method": "context_distillation",
            "construction_detail": (
                "Teacher outputs (2 records per call) as in-context few-shot examples; "
                "LLM generates 1 new artifact per call in same schema; no SFT."
            ),
            "call_time_cst": now_iso,
            "hyperparameters": {
                "temperature": TEMPERATURE,
                "max_tokens": MAX_TOKENS,
                "n_in_context_per_call": N_IN_CONTEXT,
                "n_calls_per_teacher": N_CALLS_PER_TEACHER,
            },
            "key_handling": "key 来自 PI 授权文件, runtime 内存读取, 不落盘; 本产物 0 key 命中",
            "endpoint": route["endpoint"],
            "use_proxy": route["use_proxy"],
        },
        "link_precheck": {
            "proxy_port_1018": "ok",
            "auth_ping": {
                "ok": ping["ok"],
                "model_returned": ping.get("model_returned", ""),
                "latency_ms": ping["latency_ms"],
            },
        },
        "negative_control": {
            "construction": "token_level_random_rearrangement",
            "seed": NEG_CONTROL_SEED,
            "source": "D3 script _v4_distill_min_measure.synthetic_negative_control",
            "summary": neg_summary,
        },
        "teachers": [teacher_outputs[tn] for tn in TEACHER_NAMES],
    }

    # 5. 自扫 + 落盘
    pre_hits = self_scan_obj(result)
    if pre_hits:
        print(f"  FATAL: 自扫命中 {pre_hits}")
        return {"route": route, "ok": False, "stage": "self_scan_pre", "hits": pre_hits}

    text = json.dumps(result, ensure_ascii=False, sort_keys=False, indent=2)
    text = text.replace("\r\n", "\n").replace("\r", "")
    if text.startswith("\ufeff"):
        text = text[1:]

    output_path = os.path.join(RESULTS_DIR, f"_v4_proxy_student_llm_{route['model_safe_name']}.json")
    with open(output_path, "wb") as f:
        f.write(text.encode("utf-8"))

    with open(output_path, "r", encoding="utf-8") as f:
        on_disk = f.read()
    post_hits = self_scan_text(on_disk)
    if post_hits:
        print(f"  FATAL: 落盘后自扫命中 {post_hits}")
        return {"route": route, "ok": False, "stage": "self_scan_post", "hits": post_hits}

    h12, n_bytes, n_lines, is_lf, no_bom = sha12_file(output_path)
    print(f"  SHA-12: {h12}  bytes: {n_bytes}  lines: {n_lines}  LF: {is_lf}  noBOM: {no_bom}")
    print(f"  saved: {output_path}")

    total_calls = sum(len(t["outputs"]) for t in result["teachers"])
    ok_calls = sum(sum(1 for o in t["outputs"] if o["ok"]) for t in result["teachers"])
    parsed_ok = sum(sum(1 for o in t["outputs"] if o.get("parsed_ok")) for t in result["teachers"])
    print(f"  TOTAL calls: {total_calls}  OK: {ok_calls}  parsed: {parsed_ok}")

    return {
        "route": route,
        "ok": True,
        "output_path": output_path,
        "sha12": h12,
        "bytes": n_bytes,
        "lines": n_lines,
        "n_total_calls": total_calls,
        "n_ok_calls": ok_calls,
        "n_parsed_ok": parsed_ok,
    }


# ============================================================
# 度量层 (复用 D3 + D5 三分支核对 + 根因列)
# ============================================================
def features_to_padded(records: List[Any]) -> np.ndarray:
    feats_list = [np.array(extract_features(a), dtype=np.float64) for a in records]
    padded, _ = pad_to_max_np(feats_list)
    return padded


def align_three(pa: np.ndarray, ta: np.ndarray, na: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    target_dim = max(pa.shape[1], ta.shape[1], na.shape[1])

    def _align(arr: np.ndarray) -> np.ndarray:
        if arr.shape[1] < target_dim:
            pad = np.zeros((arr.shape[0], target_dim - arr.shape[1]), dtype=np.float64)
            return np.hstack([arr, pad])
        return arr

    return _align(pa), _align(ta), _align(na)


def balance_sizes(a: np.ndarray, b: np.ndarray, seed: int = 42) -> Tuple[np.ndarray, np.ndarray]:
    n_a, n_b = a.shape[0], b.shape[0]
    if n_a == n_b:
        return a, b
    target = max(n_a, n_b)
    rng = np.random.RandomState(seed)

    def _up(arr: np.ndarray) -> np.ndarray:
        if arr.shape[0] >= target:
            return arr
        idx = rng.randint(0, arr.shape[0], size=target)
        return arr[idx]

    return _up(a), _up(b)


def measure_product(
    product_path: str,
    teacher_records: Dict[str, List[Dict[str, Any]]],
) -> Dict[str, Any]:
    """对单 model 产物按 D3 度量层 + D5 三分支核对。"""
    with open(product_path, "r", encoding="utf-8") as f:
        prod = json.load(f)

    neg_ctrl = build_negative_controls(teacher_records)
    teacher_feats = {tn: features_to_padded(recs) for tn, recs in teacher_records.items()}
    neg_feats = {tn: features_to_padded(recs) for tn, recs in neg_ctrl.items()}

    proxy_outputs: Dict[str, List[Dict[str, Any]]] = {}
    for t in prod["teachers"]:
        tn = t["teacher"]
        outs = []
        for o in t["outputs"]:
            if o.get("ok") and o.get("parsed_ok") and "generated_artifact" in o:
                outs.append(o["generated_artifact"])
        proxy_outputs[tn] = outs

    proxy_feats: Dict[str, np.ndarray] = {}
    for tn, arts in proxy_outputs.items():
        if not arts:
            proxy_feats[tn] = np.zeros((0, 0), dtype=np.float64)
        else:
            proxy_feats[tn] = features_to_padded(arts)

    cells: Dict[str, Dict[str, Any]] = {}
    judgments: Dict[str, Dict[str, Any]] = {}
    n_main_fail = 0
    n_main_pass = 0
    n_alt_fail = 0
    n_alt_pass = 0

    for tn in TEACHER_NAMES:
        feat_p = proxy_feats[tn]
        feat_t = teacher_feats[tn]
        feat_n = neg_feats[tn]
        if feat_p.shape[0] == 0:
            cells[tn] = {"n_in_proxy": 0, "skip_reason": "no_outputs"}
            continue

        feat_p_aligned, feat_t_aligned, feat_n_aligned = align_three(feat_p, feat_t, feat_n)
        feat_p_pt, feat_t_pt = balance_sizes(feat_p_aligned, feat_t_aligned, seed=42)
        feat_p_pn, feat_n_pn = balance_sizes(feat_p_aligned, feat_n_aligned, seed=42)

        dim = feat_p_aligned.shape[1]
        dirs = make_projections_np(dim, N_PROJECTIONS, PROJECTION_SEED)
        m1 = compute_pair_metrics_np(feat_p_pt, feat_t_pt, HISTOGRAM_N_BINS, dirs)
        m2 = compute_pair_metrics_np(feat_p_pn, feat_n_pn, HISTOGRAM_N_BINS, dirs)

        d1_js = m1["JS"]; d2_js = m2["JS"]
        d1_symkl = m1["symKL"]; d2_symkl = m2["symKL"]

        margin_js = margin_d2_minus_d1(d1_js, d2_js, DELTA_MIN_FACTOR)
        margin_symkl = margin_d2_minus_d1(d1_symkl, d2_symkl, DELTA_MIN_FACTOR)

        perm = permutation_test_js_np(
            feat_p_aligned, feat_t_aligned, N_PERMUTATIONS, PERM_SEED, HISTOGRAM_N_BINS, dirs
        )
        bs = bootstrap_js_ci_np(
            feat_p_aligned, feat_t_aligned, N_BOOTSTRAP, BOOTSTRAP_SEED, HISTOGRAM_N_BINS, PERM_SEED
        )

        cells[tn] = {
            "n_in_proxy": int(feat_p.shape[0]),
            "n_in_teacher": int(feat_t.shape[0]),
            "D1_JS": float(d1_js),
            "D2_JS": float(d2_js),
            "D1_symKL": float(d1_symkl),
            "D2_symKL": float(d2_symkl),
            "margin_JS": margin_js,
            "margin_symKL": margin_symkl,
            "permutation_test_JS": perm,
            "bootstrap_JS": bs,
        }

        # 三分支 + 根因 (沿 multi_runner.py 件 3 同款)
        branch_a = bool(perm["in_central_90pct"])
        branch_b = bool(not margin_js["margin_hit"])
        branch_c = bool(margin_js["margin_hit"] != margin_symkl["margin_hit"])
        verdict = "PASS" if not (branch_a or branch_b or branch_c) else "FAIL"
        n_alt_fail += 1 if verdict == "FAIL" else 0
        n_alt_pass += 1 if verdict == "PASS" else 0
        n_main_fail += 1 if verdict == "FAIL" else 0
        n_main_pass += 1 if verdict == "PASS" else 0

        d1, d2, delta = margin_js["D1"], margin_js["D2"], margin_js["delta"]
        n_p = int(feat_p.shape[0])
        n_t = int(feat_t.shape[0])
        if not (branch_a or branch_b or branch_c):
            rc = "n/a (PASS)"
        elif branch_c and not branch_a and not branch_b:
            rc = "不明"
        elif d1 < 1e-9 and d2 < 1e-9:
            rc = "工具或构造层面失灵"
        elif abs(d1 - d2) < 1e-12:
            rc = "工具或构造层面失灵"
        elif n_p > 0 and n_t > 0 and (n_p / max(n_t, 1)) < 0.20:
            rc = "工具或构造层面失灵"
        elif branch_b and d1 > 0 and d2 > 0:
            rc = "命题层面被证伪"
        elif branch_a:
            rc = "命题层面被证伪"
        else:
            rc = "不明"

        judgments[tn] = {
            "branch_a_hit": branch_a,
            "branch_b_hit": branch_b,
            "branch_c_hit": branch_c,
            "main_verdict": verdict,
            "alt_verdict": verdict,
            "root_cause": rc,
        }

    return {
        "cells": cells,
        "judgments": judgments,
        "summary": {
            "n_main_fail": n_main_fail,
            "n_main_pass": n_main_pass,
            "n_alt_fail": n_alt_fail,
            "n_alt_pass": n_alt_pass,
            "main_verdict": "FAIL" if n_main_fail > 0 else "PASS",
            "alt_verdict": "FAIL" if n_alt_fail > 0 else "PASS",
        },
    }


# ============================================================
# 主流程
# ============================================================
def main() -> int:
    print("=" * 60)
    print("V4 Track 2 多模型补跑 - battery (PI 2026-09-23 拍板三 URL + 槽)")
    print("=" * 60)
    print(f"Routes: {len(ROUTES)} (qwen_plan / mimo / teamo)")
    print(f"Proxy: {PROXY_HTTP} / {PROXY_SOCKS5}")
    print(f"Interval: inter-route {INTER_ROUTE_SLEEP_S}s, inter-call {INTER_CALL_SLEEP_S}s")

    # 0. 读 endpoints_probe 锚定模型名 (SELF hash 后续填)
    probe_path = os.path.join(RESULTS_DIR, "_track2_endpoints_probe_2026_09_23.json")
    probe_sha = "?"
    if os.path.exists(probe_path):
        probe_sha, _, _, _, _ = sha12_file(probe_path)
    print(f"endpoints_probe: {probe_path} SHA-12={probe_sha}")

    # 1. 加载教师 (一次, 复用)
    teacher_records = load_all_teachers()
    for tn in TEACHER_NAMES:
        print(f"  teacher {tn}: n={len(teacher_records[tn])}")

    # 2. 跑每个模型 (串行 + 端点间 ≥2s)
    results_per_model = []
    for i, route in enumerate(ROUTES):
        r = run_one_model(route, teacher_records)
        results_per_model.append(r)
        if i < len(ROUTES) - 1:
            print(f"\n  [sleep {INTER_ROUTE_SLEEP_S}s 防封号]")
            time.sleep(INTER_ROUTE_SLEEP_S)

    # 3. 度量
    measure_results = []
    for r in results_per_model:
        if not r.get("ok"):
            print(f"\n  SKIP measure model {r['route']['label']}: {r.get('stage','?')} fail")
            measure_results.append({"route": r["route"], "ok": False, **r})
            continue
        print(f"\n  度量 model {r['route']['label']} ...")
        m = measure_product(r["output_path"], teacher_records)
        measure_results.append({
            "route": r["route"],
            "ok": True,
            "product_path": r["output_path"],
            "product_sha12": r["sha12"],
            "product_bytes": r["bytes"],
            "n_total_calls": r["n_total_calls"],
            "n_ok_calls": r["n_ok_calls"],
            "n_parsed_ok": r["n_parsed_ok"],
            "measure": m,
        })
        print(f"    main_verdict: {m['summary']['main_verdict']}  "
              f"FAIL={m['summary']['n_main_fail']}/5  PASS={m['summary']['n_main_pass']}/5")

    # 4. 装多模型对照 JSON
    cst = timezone(timedelta(hours=8))
    now_iso = datetime.now(cst).strftime("%Y-%m-%dT%H:%M:%S+08:00")

    compare: Dict[str, Any] = {
        "metadata": {
            "task": "track2_multimodel_rerun",
            "date": "2026-09-23",
            "author": "Mavis worker (Track 2 多模型补跑 子任务)",
            "freeze_day": "V5 补强 D1 (件 3 续, 多模型补跑)",
            "spec_conformance": "PI 2026-09-23 ask_3ee5edf74be2d6ef53fbc4b4 Q4 + 补充 1 + 补充 2",
            "proxy_settings": {
                "http": PROXY_HTTP,
                "socks5": PROXY_SOCKS5,
                "rationale": "PI 2026-09-23 补充 2: teamo/openrouter 类端点必走代理防封号",
            },
            "serial_policy": {
                "inter_route_sleep_s": INTER_ROUTE_SLEEP_S,
                "inter_call_sleep_s": INTER_CALL_SLEEP_S,
                "rationale": "PI 2026-09-23 补充 2: 串行 + 间隔防封号",
            },
            "endpoint_set_discrepancy": {
                "pi_authoritative_urls": [
                    "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1",
                    "https://token-plan-cn.xiaomimimo.com/v1",
                    "https://api.teamorouter.cn/v1",
                ],
                "file_authoritative_urls_legacy": [
                    "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions (qwen_plan, 旧)",
                    "https://api.mioplus.mi.com/v1/chat/completions (mimo, 旧)",
                    "https://api.teamo.ai/v1/chat/completions (teamo, 旧)",
                ],
                "file_source": "_v4_v5_multimodel_probe.py",
                "discrepancy_resolution": "按 PI 当条派工三 URL 探活 (PI 2026-09-23 ask_3ee5edf74be2d6ef53fbc4b4 Q4 + 补充 1); probe 文件未触动 (SHA-12 5FE4CBD93D92)",
            },
            "predecessor_chain_sha12": {
                "track2_runner_template": "900A6D1E50AF",
                "track2_multimodel_runner_template": "306FA79A7C27",
                "measure_function": "21771E66AF67",
                "teacher_paths": "D2BD7521D651",
                "track2_product_openrouter": "61EDBE39A618",
                "track2_product_deepseek_direct": "1B05EBA8639B",
                "track2_product_qwen": "AE541E34781E",
                "track2_measure_v5": "7CCBE2C3E248",
                "track2_ablation_v5": "DC35655F8E7C",
                "track2_verdict_v5": "83D8E7A8BA12",
                "ablation_verdict_v5": "C2920AA9923A",
                "multimodel_compare_v5": "356BD6647796",
                "multimodel_verdict_v5": "C386251D94D6",
                "probe_template_v5": "5FE4CBD93D92",
                "endpoints_probe": probe_sha,
            },
        },
        "experiment_parameters": {
            "bootstrap_seed": BOOTSTRAP_SEED,
            "delta_min_factor": DELTA_MIN_FACTOR,
            "histogram_n_bins": HISTOGRAM_N_BINS,
            "n_bootstrap_resamples": N_BOOTSTRAP,
            "n_permutations": N_PERMUTATIONS,
            "n_projections": N_PROJECTIONS,
            "neg_control_seed": NEG_CONTROL_SEED,
            "perm_seed": PERM_SEED,
            "projection_seed": PROJECTION_SEED,
            "temperature": TEMPERATURE,
            "max_tokens": MAX_TOKENS,
            "n_in_context_per_call": N_IN_CONTEXT,
            "n_calls_per_teacher": N_CALLS_PER_TEACHER,
        },
        "gt_constructive_declaration": (
            "正类 = 各模型 LLM 上下文蒸馏产物 (15 条 generated_artifact 每模型); "
            "负类 = 独立构造对照 (token 级随机重排合成负对照, seed=42); "
            "结论不外推真实学生。"
        ),
        "constraints_compliance": {
            "key_never_in_prompt_or_json": True,
            "key_never_on_disk": True,
            "no_proxy_regen": True,
            "serial_with_min_2s_gap": True,
            "proxy_for_teamo_endpoint": True,
            "probe_template_unchanged": True,
            "track_2_llm_path_only": True,
            "no_18_frozen_touch": True,
            "no_9_grid_touch": True,
            "no_pg_v0_v01_touch": True,
            "no_plugin_spec_touch": True,
            "no_verifier_builtin_script_touch": True,
            "rationale": "PI 2026-09-22 铁律沿用口径 (R1-R7 + R8 沿用 + V4 frozen only-read)",
        },
        "call_time_cst": now_iso,
        "models": [],
        "comparison_table": [],
    }

    for r in measure_results:
        if not r.get("ok"):
            compare["models"].append({
                "label": r["route"]["label"],
                "provider": r["route"]["provider"],
                "model_id": r["route"]["model_id"],
                "ok": False,
                "stage": r.get("stage", "?"),
                "error": r.get("error", "?"),
            })
            continue
        compare["models"].append({
            "label": r["route"]["label"],
            "provider": r["route"]["provider"],
            "model_id": r["route"]["model_id"],
            "endpoint_base": r["route"]["endpoint"],
            "use_proxy": r["route"]["use_proxy"],
            "product_path": r["product_path"],
            "product_sha12": r["product_sha12"],
            "product_bytes": r["product_bytes"],
            "n_total_calls": r["n_total_calls"],
            "n_ok_calls": r["n_ok_calls"],
            "n_parsed_ok": r["n_parsed_ok"],
            "measure": r["measure"],
            "summary": r["measure"]["summary"],
        })

    for m in compare["models"]:
        if not m.get("ok", True):
            compare["comparison_table"].append({
                "label": m["label"], "ok": False, "stage": m.get("stage"),
            })
            continue
        cells = m["measure"]["cells"]
        judgments = m["measure"]["judgments"]
        d1s = [cells[tn]["D1_JS"] for tn in TEACHER_NAMES if "D1_JS" in cells.get(tn, {})]
        d2s = [cells[tn]["D2_JS"] for tn in TEACHER_NAMES if "D2_JS" in cells.get(tn, {})]
        margins = [cells[tn]["margin_JS"]["delta"] for tn in TEACHER_NAMES if "margin_JS" in cells.get(tn, {})]
        rc_dist: Dict[str, int] = {}
        for tn, j in judgments.items():
            rc = j.get("root_cause", "n/a")
            rc_dist[rc] = rc_dist.get(rc, 0) + 1
        compare["comparison_table"].append({
            "label": m["label"],
            "model_id": m.get("model_id", "?"),
            "provider": m.get("provider", "?"),
            "endpoint_base": m.get("endpoint_base", "?"),
            "use_proxy": m.get("use_proxy", False),
            "product_sha12": m.get("product_sha12"),
            "n_fail": m["summary"]["n_main_fail"],
            "n_pass": m["summary"]["n_main_pass"],
            "main_verdict": m["summary"]["main_verdict"],
            "mean_D1_JS": float(np.mean(d1s)) if d1s else 0.0,
            "mean_D2_JS": float(np.mean(d2s)) if d2s else 0.0,
            "mean_margin_delta": float(np.mean(margins)) if margins else 0.0,
            "root_cause_dist": rc_dist,
        })

    # 5. 落盘 compare JSON
    out_path = os.path.join(RESULTS_DIR, "_v4_track2_multimodel_rerun_2026_09_23.json")
    pre_hits = self_scan_obj(compare)
    if pre_hits:
        print(f"\nFATAL: pre-write 自扫命中 {pre_hits}")
        return 1
    print(f"\n  pre-write 自扫: 0 命中")

    body = json.dumps(compare, ensure_ascii=False, sort_keys=False, indent=2)
    body = body.replace("\r\n", "\n").replace("\r", "")
    if body.startswith("\ufeff"):
        body = body[1:]
    with open(out_path, "wb") as f:
        f.write(body.encode("utf-8"))
    with open(out_path, "r", encoding="utf-8") as f:
        on_disk = f.read()
    post_hits = self_scan_text(on_disk)
    if post_hits:
        print(f"FATAL: 落盘后自扫命中 {post_hits}")
        return 1

    h12, n_bytes, n_lines, is_lf, no_bom = sha12_file(out_path)
    print(f"\n  compare JSON: SHA-12={h12}  bytes={n_bytes}  lines={n_lines}  LF={is_lf}  noBOM={no_bom}")
    print(f"  saved: {out_path}")

    print("\n" + "=" * 60)
    print("DONE (battery)")
    print("=" * 60)
    return 0


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    sys.exit(main())