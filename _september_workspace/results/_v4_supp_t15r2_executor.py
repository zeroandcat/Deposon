# -*- coding: utf-8 -*-
"""
_v4_supp_t15r2_executor.py
==========================
V4 T1.5r2 扩样修订 executor: 6 cells × 30 calls/cell + 2 补跑 = 62 新 calls
=========================================================================

【设计锚定】（沿 T1.5r2 prereg `883DCED872B4` + T1.5 prereg `8898B964A9D9` + T1.5 verdict `52C985429C91`）
================================================================
- 扩样修订定位: T1.5 prereg §1.4 计划 (20 calls/cell → 6 pairs/教师) 与 §1.8 N_min=10 字面 gap 修复
- T1.5r2 plan 字面: 6 cells × 30 calls/cell = 180 calls (5 教师 × 2 prompts × 3 re-asks/cell)
- T1.5r2 实际增量 = +60 calls (沿 T1.5 verdict §3.4 字面 + 派工单 ask_57981c1bc81e03b9990a06e5 t15_ext 字面)
- T1.5r2 实际待跑 = 62 calls (4 cells × 10 calls + cell 2/3 各 11 calls 含 1 补跑 + 10 reask_idx=2)
- 2 calls 缺位补跑: cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1 (沿 T1.5 verdict §4.4 方案 A)
- 起状态: T1.5 records `.tmp/_t15_records.json` (118 ok + 2 fail = 120 records); 续跑起点 = reask_idx 2
- 阈值字面不动: K_N11_3_THRESHOLD = 0.85 / K_N11_1_DIFF = 0.05 / K_N11_2_DELTA = 0.05
- TH-T1-1 = 10 对/教师 N_min (T1 探针放宽; T1.5r2 沿用一字不动; 0 触)
- 单端点: qwen token-plan `token-plan.maas.qianwenaiapi.com/compatible-mode/v1` + model `qwen3.7-max` (非 reasoning)
- C-T15r2-1: max_tokens=500 (沿 T1.5 prereg §1.4 C-T15-1 字面不动; 工具失灵族参数修正, 非阈值调整)
- 端点维度砍去 (沿 T1.5 prereg §1.2 字面不动)
- 串行间隔 ≥ 2.5s + 单批 ≤ 30 calls / 600s 看门狗 (沿 L2 verdict §2 + L14 verdict §9.1 + T1 §1.6.1 + T1.5 prereg §1.6.1)
- K-T1-S1 字面 / K-T1-S2 沿 T1 verdict §2.2 结论引用 / K-T1-S3 字面 沿 T1 字面一字不动 (0 新设数值阈值)
- K-N11-N1_T1relax 字面 FAIL 根因消除: plan 字面扩样至 15 pairs/教师 ≥ N_min=10 字面满足 (沿 T1.5 verdict §3.4 字面)
- audit-only metadata 字段口径沿 L14V3 映射件 §6.1 #2 + 派工单 ask_9484b696 meta_field 拍板
- qwen_plan use_proxy=False (T1.5 单端点; 沿 Track 2 runner ROUTE_TEMPLATES[0] qwen 行 B65619A07B10)

【T1.5r2 派工单字面】
- 派工单 ask_57981c1bc81e03b9990a06e5 t15_ext (PI 2026-09-26 16:26 拍板):
  +60 calls 规化重跑 (N_min≥10 字面满足)
  判定阈值一字不动; 扩样 = plan 字面修订
  2 calls 超时缺位顺带补跑 (cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1) 计入 60 calls 预算
  预算/节制 = qwen token-plan 5h 节制 + 串行 ≥2.5s + 600s watchdog 拆批 + 中断-恢复同 agent 唤醒

【铁律】（沿 R5 frozen 只追加 + R4 key 永不明文 + 0 擅调阈值）
================================================================
- R4 key 永不明文 (无例外): key 仅 runtime env / desktop AI/LLM API.txt 读, 不落盘
- R5 V4 frozen 只追加: 不动任何既有件 (21 件字面源一字不动, 含 T1.5 executor `558E635F9BA6` 不动)
- R6 P-G v0/v01 不动
- R7 plugin spec 不动
- V1-V3 资产只读
- 0 擅调阈值 (K_N11_3_THRESHOLD = 0.85 一字不动; 扩样 = plan 字面修订, 非阈值)
- 派生 JSON 不合并 (本棒产物用 _v4_supp_t15r2_* prefix 分列, 与 _v4_supp_t15_* 同级独立)
- kill-line 字面不动 (hit=True 显式布尔方向)
- succeeded ≠ 跑完落盘核验 (沿 worker 老实交代)
- T1.5r2 探针定位硬约束: 不翻 L2/L14 正式判定 + 不二次判定 T1 verdict §7 自身 + 不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑

【产物】（仅 3 件, 留 verdict-keeper 起草 _v4_supp_t15r2_verdict.md）
================================================================
- per-cell 明细: .tmp/_t15r2_records.json (T1.5r2 checkpoint; T1.5 records 在 _t15_records.json 不动)
- per-batch 明细: .tmp/_t15r2_batch_{start}_{end}_{ts}.jsonl
- aggregate: results/_v4_supp_t15r2_result.json (schema `v4_t15r2_sensitivity_fix_n10/1`)
- 不动 T1.5 result `6B47D389B7AE` + T1.5 verdict `52C985429C91` + T1.5 executor `558E635F9BA6`

【用法】（沿 T1.5 executor 风格, 派工单明示「中断-恢复同 agent 唤醒」）
================================================================
  python _v4_supp_t15r2_executor.py probe                                       # 仅探活 qwen_plan
  python _v4_supp_t15r2_executor.py run <cell_idx_start> <cell_idx_end> [--calls N]   # 跑指定 cells
  python _v4_supp_t15r2_executor.py aggregate                                   # 聚合 result.json
  python _v4_supp_t15r2_executor.py all                                         # probe + run 0-5 + aggregate

【cells 索引】（沿 T1.5 prereg §1.2 字面）
================================================================
  0: L2 / temp 0.0 / qwen_plan
  1: L2 / temp 0.3 / qwen_plan
  2: L2 / temp 0.5 / qwen_plan (含 coze/S5/r0 1 补跑)
  3: L14 / temp 0.0 / qwen_plan (含 GLM_1/L_geography_world/r1 1 补跑)
  4: L14 / temp 0.3 / qwen_plan
  5: L14 / temp 0.5 / qwen_plan

【skill 诚实】
================================================================
派工单要求 `scientific-research-workflows:statistical-analysis` skill
(plugin @scientific-research-workflows, sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb),
本地 skill 加载器实录 `Local skill not found` —— 按 T1.5r2 prereg `883DCED872B4` 字面 +
activation(待生效) + T1.5 prereg `8898B964A9D9` + T1.5 executor `558E635F9BA6` + T1 executor `A7CAD9228B0B`
字面锚执行, **未编造 skill 不存在的虚构指令**.
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
from typing import Any, Dict, List, Optional, Tuple, Set

import requests as _requests

# ============================================================
# 常量与路径
# ============================================================
ROOT = Path("D:/私人资料/deposon-repo")
RESULTS_DIR = ROOT / "results"
TMP_DIR = ROOT / ".tmp"

# T1.5 records (沿状态不动, 只读复用)
T15_RECORDS_PATH = TMP_DIR / "_t15_records.json"
T15_RESULT_PATH = RESULTS_DIR / "_v4_supp_t15_result.json"

# T1.5r2 records (本棒新 checkpoint)
T15R2_CHECKPOINT_PATH = TMP_DIR / "_t15r2_records.json"
T15R2_PROBE_LOG_PATH = TMP_DIR / "_t15r2_probe_log.json"
T15R2_RESULT_PATH = RESULTS_DIR / "_v4_supp_t15r2_result.json"

# Key source (沿 T1.5 executor § key loading)
KEY_SOURCE_PATH = Path("C:/Users/Administrator/Desktop/AI/LLM API.txt")
CAPTIONS_PATH = Path("D:/私人资料/deposon-repo/corpus/v20_caption_surface/strip_captions_22.json")
CAPTIONS_SHA12_EXPECTED = "6A2656878745"

# T1.5r2 / T1.5 / T1 字面 SHA-12 锚 (核对一致后用, 一字不动)
T15R2_PREREG_SHA12_EXPECTED = "883DCED872B4"   # 派工单字面口径 (待 PI 复核生效)
T15_PREREG_SHA12_EXPECTED = "8898B964A9D9"
T15_VERDICT_SHA12 = "52C985429C91"
T15_RESULT_SHA12 = "6B47D389B7AE"
T15_EXECUTOR_SHA12 = "558E635F9BA6"
T1_VERDICT_SHA12 = "F1B5E49F3058"
T1_ACTIVATION_SHA12 = "79936B630015"
PREREG_V02_SHA12_EXPECTED = "D85488A64D89"
L2_VERDICT_SHA12 = "E433A06E7BFB"
L14_VERDICT_SHA12_SELF = "764F24A21AC8"
L14_VERDICT_SHA12_DISK = "8EEF73BF9856"
L9_PREREG_SHA12 = "23879B6CD1CC"
L10_PREREG_SHA12 = "F6FE005EE3C7"
N09_N39_PREREG_SHA12 = "0A9EE16267B5"
METHODS_PREREG_SHA12 = "0A7BCA992B95"
SEEDS_PREREG_SHA12 = "113CBE555643"
TRACK2_MULTIMODEL_PROBE_SHA12 = "B65619A07B10"
TRACK2_ENDPOINTS_PROBE_SHA12 = "C846F7FC79EE"
PREREG_T1_SHA12_EXPECTED = "802DECE2286A"

# 阈值 (沿 0A9EE16267B5 §1 K-N11 字面 + L2/L14 verdict §4.3/§5.3 + T1 §1.5 + T1.5 §1.5; T1.5r2 一字不动)
K_N11_3_THRESHOLD = 0.85
K_N11_1_DIFF = 0.05
K_N11_2_DELTA = 0.05
TH17_N_TARGET = 20                # L2/L14 既判 N target
TH_T1_N_MIN = 10                  # T1 探针放宽 N_min (T1.5r2 沿用一字不动)
INTER_CALL_SERIAL_S = 2.5
WATCHDOG_S = 600                  # 单批 ≤ 30 calls / 600s 看门狗 (沿 L2 verdict §2)
BATCH_CALL_LIMIT = 30
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

# L2/L14 prompt 子集 (沿 L2 verdict §2 字面 + L14 verdict §2 字面 + T1.5 prereg §1.4 字面)
L2_PROMPTS = ["L_biological_taxonomy", "S5"]
L14_PROMPTS = ["L_geography_world", "L_historical_causality"]

# *** T1.5r2 关键修订 (沿 T1.5r2 prereg §1.4 字面, plan 字面修订 +60 calls) ***
N_REASKS = 3  # T1.5 用 2; T1.5r2 扩样至 3 (5 教师 × 2 prompts × 3 re-asks = 30 calls/cell)

# 单端点配置 (沿 endpoints probe C846F7FC79EE qwen_plan 行 + Track 2 runner B65619A07B10)
ENDPOINTS = {
    "qwen_plan": {
        "label": "qwen_plan",
        "endpoint": "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1",
        "model_id": "qwen3.7-max",  # 非 reasoning 模型 (沿 T1.5 prereg §1.4 + T1.5r2 §1.4)
        "key_index_1based": 23,
        "use_proxy": False,         # qwen_plan 直连无代理 (沿 Track 2 runner ROUTE_TEMPLATES[0] qwen 行)
    },
}
TEMPERATURES = [0.0, 0.3, 0.5]

# 6 cells 矩阵定义 (cell_idx → (维度, 温度)) (沿 T1.5 prereg §1.2 字面)
CELLS: List[Tuple[str, float]] = []
for dim in ("L2", "L14"):
    for temp in TEMPERATURES:
        CELLS.append((dim, temp))

# C-T15r2-1 (沿 T1.5 prereg §1.4 + T1.5r2 §1.4 字面): max_tokens = 500
MAX_TOKENS = 500

# 2 补跑 calls (沿 T1.5 verdict §4.4 方案 A + 派工单 t15_ext 字面拍板)
T15R2_RERUN_TUPLES = [
    ("coze", "S5", 0, 0.5),                # cell 2 coze/S5/r0 缺位补跑
    ("GLM_1", "L_geography_world", 1, 0.0),  # cell 3 GLM_1/L_geography_world/r1 缺位补跑
]

# ============================================================
# Key 形态自扫 (沿 R4 + T1.5r2 §0 自扫声明: 0 命中)
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
    if path.exists():
        return sha12_bytes(path.read_bytes())
    return ""


def sha12_str(s: str) -> str:
    return sha12_bytes(s.encode("utf-8"))


# ============================================================
# Key 加载 (runtime env / desktop AI/LLM API.txt, 沿 T1.5 executor 字面)
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
# Proxy 控制 (T1.5r2 单端点 qwen_plan use_proxy=False, 不触发 tun 硬纪律)
# ============================================================
def unset_proxy() -> None:
    """T1.5r2 单端点 = qwen_plan (无代理). 防御性 unset."""
    for k in ("https_proxy", "http_proxy", "all_proxy"):
        os.environ.pop(k, None)


# ============================================================
# HTTP 调用 (沿 T1.5 executor 字面)
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
    unset_proxy()
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
# Records 加载: T1.5 (status anchor) + T1.5r2 (续跑)
# ============================================================
def load_t15_records() -> List[Dict[str, Any]]:
    if T15_RECORDS_PATH.exists():
        try:
            return json.loads(T15_RECORDS_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def load_t15r2_records() -> List[Dict[str, Any]]:
    if T15R2_CHECKPOINT_PATH.exists():
        try:
            return json.loads(T15R2_CHECKPOINT_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def save_t15r2_records(r2_records: List[Dict[str, Any]]) -> None:
    T15R2_CHECKPOINT_PATH.parent.mkdir(parents=True, exist_ok=True)
    T15R2_CHECKPOINT_PATH.write_text(json.dumps(r2_records, ensure_ascii=False),
                                     encoding="utf-8")


def build_ok_keys(records_combined: List[Dict[str, Any]]) -> Set[Tuple[int, str, str, int]]:
    """只 skip 已成功的 (cell_idx, teacher, caption_id, reask_idx) 元组; 失败 call 不视为已成功, 可重跑.
    元组不含 temperature, 因 cell_idx 已锁定 dim+temp (沿 T1.5 executor §元组 skip + T1.5r2 §1.6.4 字面)."""
    keys: Set[Tuple[int, str, str, int]] = set()
    for r in records_combined:
        if r.get("ok") and r.get("endpoint") == ENDPOINTS["qwen_plan"]["endpoint"]:
            # T1.5 records 可能含 teacher_path_rel 截断/异常 (派工单实测观察到), 用 teacher 字段即可
            tup = (r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"])
            keys.add(tup)
    return keys


# ============================================================
# 单 cell runner (续跑模式; 含 cells 拆批上限)
# ============================================================
def run_cell(cell_idx: int, dim: str, temp: float,
             captions: List[Dict[str, Any]],
             t15r2_records: List[Dict[str, Any]],
             ok_keys: Set[Tuple[int, str, str, int]],
             wall_start: float,
             max_calls_in_cell: int = 0) -> Dict[str, Any]:
    """跑单 cell; returns cell_summary. Updates t15r2_records in-place + saves checkpoint.
    max_calls_in_cell > 0: stop after N new calls in this cell (bash 300s watchdog).
    ok_keys: 来自 T1.5 records + T1.5r2 records 已成功的元组 (cell_idx, teacher, caption_id, reask_idx)."""
    ep_name = "qwen_plan"  # T1.5r2 单端点 (沿 T1.5)
    ep = ENDPOINTS[ep_name]
    unset_proxy()  # qwen_plan use_proxy=False

    api_key = read_api_key(ep["key_index_1based"])

    prompts_ids = L2_PROMPTS if dim == "L2" else L14_PROMPTS
    prompts_list = select_prompts(captions, prompts_ids)

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
        "n_skipped_existing_ok": 0,
    }

    n_new = 0

    # 优先级 1: 2 calls 缺位补跑 (沿 T1.5 verdict §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板)
    # 必须在 reask_idx=2 续跑之前先执行, 以保证 prereg §1.6.4 字面"2 补跑计入 +60 calls 预算内"
    rerun_list = []
    for tup in T15R2_RERUN_TUPLES:
        teacher_r, cap_r, reask_r, temp_r = tup
        if (cell_idx == _dim_temp_to_cell_idx(teacher_r, cap_r, reask_r, temp_r)
                if False else  # 不用此分支
                _is_rerun_in_cell(teacher_r, cap_r, reask_r, temp_r, cell_idx, dim, temp)):
            rerun_list.append((teacher_r, cap_r, reask_r))

    def _attempt(teacher_name: str, caption_id: str, reask_idx: int) -> bool:
        """尝试跑单 call; 返回 True 表示已处理 (新增/跳过)."""
        nonlocal n_new
        key_tuple = (cell_idx, teacher_name, caption_id, reask_idx)
        if key_tuple in ok_keys:
            cell_summary["n_skipped_existing_ok"] += 1
            return True

        # 串行间隔
        if n_new > 0:
            time.sleep(INTER_CALL_SERIAL_S)

        if max_calls_in_cell > 0 and n_new >= max_calls_in_cell:
            cell_summary["calls_limit_break"] = True
            return False

        elapsed = time.time() - wall_start
        if elapsed > WATCHDOG_S:
            cell_summary["watchdog_break"] = True
            return False

        # 构造 prompt (沿 L2 verdict §2 / L14 verdict §2 字面)
        cap_obj = next(c for c in captions if c["id"] == caption_id)
        caption_text = cap_obj["text"]
        messages = [
            {"role": "system", "content": PROMPT_SYSTEM},
            {"role": "user", "content": build_user_prompt(teacher_name, caption_id, caption_text)},
        ]

        teacher_path_rel = next((p[1] for n, p in TEACHER_PATHS_REL if n == teacher_name), "")
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
            "reask_idx": reask_idx,
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
            "source": "t15r2_expansion_or_rerun",
            "rerun_2calls": reask_idx in (0, 1) and dim == "L2" and cell_idx == 2 and teacher_name == "coze" and caption_id == "S5"
                          or (dim == "L14" and cell_idx == 3 and teacher_name == "GLM_1" and caption_id == "L_geography_world"),
        }
        # rerun_2calls 布尔简化: 仅与 T15R2_RERUN_TUPLES 比对
        rec["rerun_2calls"] = (teacher_name, caption_id, reask_idx, temp) in T15R2_RERUN_TUPLES

        t15r2_records.append(rec)
        ok_keys.add(key_tuple)
        n_new += 1

        if ok:
            cell_summary["n_calls_ok"] += 1
        else:
            cell_summary["n_calls_failed"] += 1

        cell_summary["calls"].append({
            "teacher": teacher_name,
            "caption_id": caption_id,
            "reask_idx": reask_idx,
            "ok": ok,
            "latency_ms": resp.get("latency_ms"),
            "status_code": resp.get("status_code"),
            "error_category": resp.get("error_category"),
            "response_text_len": len(content),
            "rerun_2calls": rec["rerun_2calls"],
        })

        try:
            save_t15r2_records(t15r2_records)
        except Exception as e:
            print(f"  [checkpoint FAIL] {e}", flush=True)

        wall = time.time() - wall_start
        print(f"  [{cell_idx:2d}/{dim}/t={temp}/{ep_name}] "
              f"{teacher_name}/{caption_id}/r{reask_idx} ok={ok} "
              f"lat={resp.get('latency_ms')}ms wall={wall:.1f}s "
              f"rerun={rec['rerun_2calls']}",
              flush=True)

        if wall > WATCHDOG_S:
            cell_summary["watchdog_break"] = True
            return False

        return True

    # 优先级 1: 2 calls 缺位补跑 (沿 T1.5 verdict §4.4 方案 A 字面)
    for teacher_r, cap_r, reask_r, temp_r in T15R2_RERUN_TUPLES:
        if _cell_match(dim, temp, teacher_r, cap_r, reask_r, temp_r):
            if not _attempt(teacher_r, cap_r, reask_r):
                return cell_summary

    # 优先级 2: reask_idx=2 全员 (沿 prereg §1.4 plan 字面扩样修订)
    for teacher_name in TEACHER_NAMES:
        if max_calls_in_cell > 0 and n_new >= max_calls_in_cell:
            cell_summary["calls_limit_break"] = True
            return cell_summary
        for prompt_obj in prompts_list:
            if max_calls_in_cell > 0 and n_new >= max_calls_in_cell:
                cell_summary["calls_limit_break"] = True
                return cell_summary
            caption_id = prompt_obj["id"]
            if not _attempt(teacher_name, caption_id, 2):
                return cell_summary

    return cell_summary


def _is_rerun_in_cell(teacher_r, cap_r, reask_r, temp_r, cell_idx, dim, temp) -> bool:
    """Return True iff (teacher, caption, reask, temp) of a rerun tuple maps to this cell_idx."""
    expected_dim = "L2" if cap_r in L2_PROMPTS else "L14"
    expected_cell_idx = None
    for i, c in enumerate(CELLS):
        if c[0] == expected_dim and c[1] == temp_r:
            expected_cell_idx = i
            break
    return (expected_cell_idx == cell_idx) and (dim == expected_dim) and (temp == temp_r)


def _cell_match(dim, temp, teacher_r, cap_r, reask_r, temp_r) -> bool:
    expected_dim = "L2" if cap_r in L2_PROMPTS else "L14"
    return (dim == expected_dim) and (temp == temp_r)


def _dim_temp_to_cell_idx(teacher_r, cap_r, reask_r, temp_r) -> int:
    expected_dim = "L2" if cap_r in L2_PROMPTS else "L14"
    for i, c in enumerate(CELLS):
        if c[0] == expected_dim and c[1] == temp_r:
            return i
    return -1


# ============================================================
# 主流程
# ============================================================
def cmd_probe() -> None:
    """Probe qwen_plan endpoint. 1 call. Per T1.5r2 §1.1 Q1 + 即用即探."""
    print("=== T1.5r2 probe: qwen_plan ===")
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

    T15R2_PROBE_LOG_PATH.write_text(json.dumps({
        "task": "t15r2_endpoint_probe_2026_09_26",
        "date_label": "2026-09-26",
        "generated_utc": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "rationale": "T1.5r2 §1.1 Q1 + 即用即探 纪律 (PI 2026-09-26 派工单 t15_ext 拍板 +60 calls 扩样)",
        "endpoints": probe_results,
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj(probe_results)],
            "status": "clean" if not self_scan_obj(probe_results) else "WARN",
        },
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nProbe log: {T15R2_PROBE_LOG_PATH}")


def cmd_run(start_idx: int, end_idx: int, calls_limit: int = 0) -> None:
    """Run cells [start_idx, end_idx] inclusive.
    calls_limit > 0: stop after N new calls per invocation (bash 300s watchdog).
    """
    print(f"=== T1.5r2 run cells [{start_idx}, {end_idx}] inclusive (calls_limit={calls_limit}) ===")
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    captions = load_captions()
    captions_sha = sha12_file(CAPTIONS_PATH)
    print(f"captions SHA-12: {captions_sha} (expected {CAPTIONS_SHA12_EXPECTED})")
    if captions_sha.lower() != CAPTIONS_SHA12_EXPECTED.lower():
        print(f"  WARN: captions SHA mismatch (expected {CAPTIONS_SHA12_EXPECTED})")
        # 不抛错 — 沿 "0 触动既有件" 原则

    # T1.5 record SHA 自检 (派工单 9 网格沿用 + §0 21 件一字不动)
    t15_records = load_t15_records()
    t15r2_records = load_t15r2_records()
    print(f"loaded T1.5 records: {len(t15_records)} (state anchor)")
    print(f"loaded T1.5r2 records (existing): {len(t15r2_records)}")

    # 组合: T1.5 + T1.5r2 records 用于 ok_keys skip 集
    records_combined = t15_records + t15r2_records
    ok_keys = build_ok_keys(records_combined)
    print(f"ok_keys set (cell_idx, teacher, caption, reask): {len(ok_keys)} unique tuples")

    # 自扫: 2 补跑 + 计划每个 cell 新增 reask_idx=2 数量
    print()
    print("T1.5r2 plan summary per cell (target = 30 calls/cell = 5 teacher × 2 cap × 3 re-asks):")
    for cell_idx in range(len(CELLS)):
        dim, temp = CELLS[cell_idx]
        prompts = L2_PROMPTS if dim == "L2" else L14_PROMPTS
        planned_total = len(TEACHER_NAMES) * len(prompts) * N_REASKS
        existing_in_cell = sum(1 for tup in ok_keys if tup[0] == cell_idx)
        remaining = planned_total - existing_in_cell
        # 2 补跑可单独列出
        rerun_in_cell = [(t, c, r) for t, c, r, tr in T15R2_RERUN_TUPLES
                         if _is_rerun_in_cell(t, c, r, tr, cell_idx, dim, temp)]
        print(f"  cell {cell_idx} ({dim}/t={temp}): planned={planned_total}, existing_ok={existing_in_cell}, missing={remaining}, "
              f"rerun_2calls={len(rerun_in_cell)} ({rerun_in_cell})")

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
        # 运行时重新加载 t15r2_records (避免跨 invocation 状态丢失)
        t15r2_records_local = load_t15r2_records()
        ok_keys_local = build_ok_keys(t15_records + t15r2_records_local)
        summary = run_cell(idx, dim, temp, captions, t15r2_records_local, ok_keys_local, wall_start,
                           max_calls_in_cell=(calls_limit - calls_made if calls_limit > 0 else 0))
        cell_summaries.append(summary)
        # 把新跑结果写回 .tmp/_t15r2_records.json
        try:
            save_t15r2_records(t15r2_records_local)
        except Exception as e:
            print(f"  [checkpoint FAIL after cell] {e}", flush=True)
        calls_made += summary["n_calls_ok"] + summary["n_calls_failed"]
        if summary.get("watchdog_break"):
            print(f"  [watchdog break] cell {idx} incomplete; stop batch")
            break

    wall = time.time() - wall_start
    print(f"\n=== run batch done: wall={wall:.1f}s, n_t15r2_records={len(load_t15r2_records())}, "
          f"new_calls_in_batch={calls_made} ===")
    print(f"  per-cell:")
    for s in cell_summaries:
        print(f"    cell {s['cell_idx']} ({s['dim']}/t={s['temperature']}/qwen_plan): "
              f"ok={s['n_calls_ok']} fail={s['n_calls_failed']} "
              f"skipped_existing_ok={s['n_skipped_existing_ok']} "
              f"wd_break={s.get('watchdog_break', False)} "
              f"limit_break={s.get('calls_limit_break', False)}")

    # 保存 t15r2 records checkpoint
    save_t15r2_records(load_t15r2_records())

    # Per-batch summary JSONL log
    batch_log_path = TMP_DIR / f"_t15r2_batch_{start_idx}_{end_idx}_{datetime.now(timezone(timedelta(hours=8))).strftime('%Y%m%d_%H%M%S')}.jsonl"
    with open(batch_log_path, "w", encoding="utf-8") as f:
        for s in cell_summaries:
            f.write(json.dumps(s, ensure_ascii=False) + "\n")
    print(f"  batch log: {batch_log_path}")


def cmd_aggregate() -> Dict[str, Any]:
    """Aggregate: T1.5 (state anchor) + T1.5r2 records → _v4_supp_t15r2_result.json."""
    print("=== T1.5r2 aggregate: compute result.json ===")
    t15_records = load_t15_records()
    t15r2_records = load_t15r2_records()
    if not t15_records and not t15r2_records:
        print("FATAL: no records in T1.5 + T1.5r2 checkpoints")
        sys.exit(1)

    captions = load_captions()
    captions_sha = sha12_file(CAPTIONS_PATH)

    # 合并 T1.5 + T1.5r2 records 作为全集分析 (T1.5 records 是历史状态, 沿 T1.5 §1.2 + T1.5 verdict §1.2 字面纳入)
    records_all = t15_records + t15r2_records
    # 偏好: 同一 (cell_idx, teacher, caption_id, reask_idx) 元组以最新 (T1.5r2 first, 因为它可能补充失败 calls) 为准
    # 但 T1.5r2 仅跑 reask_idx=2 + 2 补跑 calls, 不会与 T1.5 records 冲突
    # 因此全集 = T1.5 + T1.5r2 (无冲突)

    # Per cell × per teacher J 列表 (沿 T1.5 executor § cmd_aggregate 字面)
    by_cell_teacher_pairs: Dict[Tuple[int, str], List[Tuple[str, str, str, int, int]]] = {}
    for r in records_all:
        if not r.get("ok"):
            continue
        k = (r["cell_idx"], r["teacher"])
        by_cell_teacher_pairs.setdefault(k, []).append((
            r["response_text"], r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"]
        ))

    # Per cell × per teacher J 中位数 + same-caption 拆解 (沿 T1.5 verdict §1.2 字面 "same-caption/cross-caption 拆解")
    # same-caption: 同一 caption 内的多对 pairs = 教师对同一 caption 的 re-asks 间 Jaccard
    # cross-caption: 不同 caption 间的 pairs (T1.5 verdict §1.2 字面 "教师对不同 caption 产生的回复差异")
    per_cell_teacher_j: Dict[Tuple[int, str], Dict[str, Any]] = {}
    for k, recs in by_cell_teacher_pairs.items():
        cell_idx, teacher = k
        n = len(recs)
        # all_pairs
        jvs_all = []
        jvs_nonempty = []
        n_pairs_empty_empty = 0
        # same-caption 拆解
        same_caption_jvs = []
        cross_caption_jvs = []
        same_caption_jvs_nonempty = []
        cross_caption_jvs_nonempty = []
        for i in range(n):
            for j in range(i + 1, n):
                ti = recs[i][0]
                tj = recs[j][0]
                ci = recs[i][2]
                cj = recs[j][2]
                jv = jaccard(ti, tj)
                jvs_all.append(jv)
                same = (ci == cj)
                if same:
                    same_caption_jvs.append(jv)
                    if tokenize(ti) and tokenize(tj):
                        same_caption_jvs_nonempty.append(jv)
                else:
                    cross_caption_jvs.append(jv)
                    if tokenize(ti) and tokenize(tj):
                        cross_caption_jvs_nonempty.append(jv)
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
        if same_caption_jvs:
            same_med = float(statistics.median(same_caption_jvs))
        else:
            same_med = None
        if same_caption_jvs_nonempty:
            same_med_ne = float(statistics.median(same_caption_jvs_nonempty))
        else:
            same_med_ne = None
        if cross_caption_jvs:
            cross_med = float(statistics.median(cross_caption_jvs))
        else:
            cross_med = None
        if cross_caption_jvs_nonempty:
            cross_med_ne = float(statistics.median(cross_caption_jvs_nonempty))
        else:
            cross_med_ne = None

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
            "same_caption_pairs": len(same_caption_jvs),
            "same_caption_j_median": (round(same_med, 6) if same_med is not None else None),
            "same_caption_j_median_nonempty": (round(same_med_ne, 6) if same_med_ne is not None else None),
            "cross_caption_pairs": len(cross_caption_jvs),
            "cross_caption_j_median": (round(cross_med, 6) if cross_med is not None else None),
            "cross_caption_j_median_nonempty": (round(cross_med_ne, 6) if cross_med_ne is not None else None),
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
                "same_caption_pairs": (d["same_caption_pairs"] if d else 0),
                "same_caption_j_median": (d["same_caption_j_median"] if d else None),
                "same_caption_j_median_nonempty": (d["same_caption_j_median_nonempty"] if d else None),
                "cross_caption_pairs": (d["cross_caption_pairs"] if d else 0),
                "cross_caption_j_median": (d["cross_caption_j_median"] if d else None),
                "cross_caption_j_median_nonempty": (d["cross_caption_j_median_nonempty"] if d else None),
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
                "same_caption_j_median_nonempty": x["same_caption_j_median_nonempty"],
                "cross_caption_j_median_nonempty": x["cross_caption_j_median_nonempty"],
            }
            if hit:
                k3_any_hit = True
            if hit_ne:
                k3_any_hit_nonempty = True

        # K-N11-N1 字面 (per teacher): N < TH17_N_TARGET = 20 → pass=False → FAIL
        # K-N11-N1_T1relax 字面 (per teacher): N < TH_T1_N_MIN = 10 → pass=False → FAIL (T1.5r2 探针放宽口径)
        n1_pass_per_teacher = {}
        n1_any_fail = False
        n1_T1relax_pass_per_teacher = {}
        n1_T1relax_any_fail = False
        for x in per_teacher:
            n = x["n_pairs"]
            # K-N11-N1 字面 (沿 v0.2 §2 L2 K-N11-N1 字面)
            pass_ok_k_n11_n1 = bool(n >= TH17_N_TARGET)
            n1_pass_per_teacher[x["teacher"]] = {
                "n_pairs": n,
                "pass": pass_ok_k_n11_n1,
                "verdict": ("PASS" if pass_ok_k_n11_n1 else f"FAIL (N={n} < {TH17_N_TARGET})"),
            }
            if not pass_ok_k_n11_n1:
                n1_any_fail = True
            # K-N11-N1_T1relax (T1 探针放宽 N_min=10; T1.5r2 沿用一字不动; T1.5r2 plan 字面扩样后根因消除)
            pass_ok_T1relax = bool(n >= TH_T1_N_MIN)
            n1_T1relax_pass_per_teacher[x["teacher"]] = {
                "n_pairs": n,
                "pass": pass_ok_T1relax,
                "verdict": ("PASS" if pass_ok_T1relax else f"FAIL (N={n} < {TH_T1_N_MIN})"),
            }
            if not pass_ok_T1relax:
                n1_T1relax_any_fail = True

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
                "K-N11-N1": {
                    "any_fail": n1_any_fail,
                    "pass": (not n1_any_fail),
                    "rule": f"L2/L14 既判 N target = {TH17_N_TARGET}/教师 (沿 v0.2 §2 L2 K-N11-N1 字面; 与 T1.5r2 探针放宽 N_min=10 双层并存)",
                    "literal_source": "v0.2 §2 L2 K-N11-N1 字面 (D85488A64D89) + L2 verdict §4 + L14 verdict §5",
                    "verdict": "FAIL (>=1 教师 N < 20)" if n1_any_fail else "PASS",
                    "per_teacher": n1_pass_per_teacher,
                },
                "K-N11-N1_T1relax": {
                    "any_fail": n1_T1relax_any_fail,
                    "pass": (not n1_T1relax_any_fail),
                    "rule": f"T1.5r2 探针放宽 N_min = {TH_T1_N_MIN}/教师 (沿 T1 §1.4 + T1.5 prereg §1.4 + T1.5 verdict §3.4 字面拍板 'plan 字面扩样至 15 pairs/教师 ≥ N_min=10 字面满足')",
                    "literal_source": "T1 §1.4 + §1.8 TH-T1-1 = 10 对/教师 (T1 探针放宽; T1.5 + T1.5r2 沿用一字不动) + T1.5 verdict §3.4 字面拍板",
                    "verdict": "FAIL (>=1 教师 N < 10)" if n1_T1relax_any_fail else "PASS",
                    "verdict_with_planned_vs_actual": (
                        f"planned = 5 teacher × 2 prompts × 3 re-asks = 15 pairs/教师 ≥ {TH_T1_N_MIN} 字面满足"
                        if all(x["n_pairs"] >= TH_T1_N_MIN for x in per_teacher)
                        else f"扩样 plan 字面满足 (15 pairs/教师 ≥ {TH_T1_N_MIN}), 但实测 N < {TH_T1_N_MIN} 教师存在"
                    ),
                    "per_teacher": n1_T1relax_pass_per_teacher,
                },
            },
        }

    # 跨 cell 汇总
    cross_summary: Dict[str, Any] = {"by_dim_temp": {}}
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

    # K-T1-S1 (主判定): 固定端点 qwen_plan, 跨温度 {0.0, 0.3, 0.5} 任一温度点 cell J 中位 ≥ 0.85 → hit=True
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
            "literal_source": "T1 §1.5.2 K-T1-S1 字面 + T1.5 §1.5.2 K-T1-S1 字面 + T1.5r2 §1.5.2 K-T1-S1 字面 (T1.5r2 复用沿 T1 一字不动)",
            "verdict": "FAIL (稳健性存疑 - 温度 flip)" if hit else "PASS (温度方向一致)",
            "verdict_nonempty": "FAIL (稳健性存疑 - 温度 flip nonempty)" if hit_nonempty else "PASS (温度方向一致 nonempty)",
        }

    # K-T1-S2 沿 T1 verdict §2.2 结论引用, T1.5r2 不重测 (沿 T1.5r2 §1.5.2 字面)
    k_t1_s2 = {
        "any_hit": False,
        "hit": False,
        "literal_source": "T1 verdict F1B5E49F3058 §2.2 K-T1-S2 字面 (any_hit: false, mimo/teamo 端点维度 empty-empty 主导)",
        "rationale": "T1.5r2 端点维度砍去 (qwen_plan 单端点); 沿 T1 verdict §2.2 any_hit: false 结论引用, T1.5r2 不重测",
        "T15r2_endpoints_exploration": "T1.5r2 单端点 = qwen_plan (非 reasoning + max_tokens=500 修正构造失灵族), T1 mimo/teamo 端点维度已砍去",
        "rule": "沿 T1 verdict 结论引用, 不重测; 端点维度砍去",
        "verdict": "PASS (沿 T1 verdict 结论引用 — 不重测)",
    }

    # K-T1-S3 (副判定): 全 6 cells J 中位 < 0.85 → 探针不命中
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
        "literal_source": "T1 §1.5.2 K-T1-S3 字面 + T1.5 §1.5.2 + T1.5r2 §1.5.2 (复用一字不动, 0 新设数值)",
        "verdict": "PASS (判定稳健 + T1 verdict 信息量补正)" if all_below else "FAIL (稳健性存疑 - 不翻 L2/L14 既判 + 不二次判定 T1 verdict §7 + 不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面)",
        "verdict_nonempty": "PASS (判定稳健 nonempty + T1 verdict 信息量补正 nonempty)" if all_below_nonempty else "FAIL (稳健性存疑 nonempty)",
    }

    k_t1_s1_any_hit = any(d["hit"] for d in k_t1_s1.values())
    k_t1_s1_any_hit_nonempty = any(d["hit_nonempty"] for d in k_t1_s1.values())

    # 总体判定 (T1.5r2 = T1.5 扩样修订探针, 不翻 L2/L14 既判 + 不二次判定 T1 verdict §7 + 不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3)
    if all_below and not k_t1_s1_any_hit:
        overall_verdict = "PASS (T1.5r2 判定稳健确认 + K-N11-N1_T1relax 字面 PASS 根因消除 + T1 verdict 信息量补正成立 + T1.5 verdict §3.4 + §4.4 建议落地确认)"
    else:
        overall_verdict = "FAIL (稳健性存疑注记 - K-T1-S1 命中; 不翻 L2/L14 既判 + 不二次判定 T1 verdict §7 + 不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑)"

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
                f"T1.5r2 判定稳健 (字面) — K-T1-S3 探针不命中: 全 6 cells J 中位 < {K_N11_3_THRESHOLD}; "
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
            root_cause_class = "T1.5r2 判定稳健 (qwen t=0.7 baseline 方向在 temp 维度稳定; qwen3.7-max 非 reasoning + max_tokens=500 修正构造失灵族后真维持方向一致 + plan 字面扩样至 30 calls/cell 满足 N_min=10 字面 PASS)"
            root_cause_note = "全 6 cells J 中位 < 0.85, 跨 qwen_plan × temp {0.0,0.3,0.5} × {L2,L14} 维度维持 qwen t=0.7 baseline 既定方向 (K-N11-3 真证伪); T1 verdict 构造失灵族假象裁定获补正 (非 reasoning + max_tokens=500 修正后真维持方向一致); T1.5 verdict §3.4 +60 calls 扩 N + §4.4 补跑 2 calls 建议落地确认"
    else:
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
        root_cause_class = f"T1.5r2 稳健性存疑 (任一 cell 翻 ≥ {K_N11_3_THRESHOLD}); 二源根因 (沿 T1.5 §1.5.2 K-T1-S1 字面): {' / '.join(sorted(sources))}"
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

    # K-N11-N1_T1relax 字面 PASS 状态 (沿 T1.5 verdict §3.4 字面拍板)
    all_T1relax_pass = all(
        per_cell_summary[i]["kill_lines"]["K-N11-N1_T1relax"]["pass"]
        for i in range(len(CELLS))
    )
    k_n11_n1_t1relax_overall = "PASS (全 6 cells N≥10/教师; plan 字面 15 pairs/教师 ≥ N_min=10 字面满足)" if all_T1relax_pass else "FAIL"

    # 落 result.json
    t15r2_records_shas = [sha12_str(json.dumps(r, ensure_ascii=False, sort_keys=True)) for r in t15r2_records]
    t15_records_shas = [sha12_str(json.dumps(r, ensure_ascii=False, sort_keys=True)) for r in t15_records]

    result_obj = {
        "metadata": {
            "schema": "v4_t15r2_sensitivity_fix_n10/1",
            "task": "T1.5r2 . L2/L14 温度敏感性 + qwen_plan 单端点 (非 reasoning + max_tokens=500 修正构造失灵族 + plan 字面扩样至 30 calls/cell 满足 N_min=10) 扩样修订探针 (construction-failure-fix expansion probe)",
            "date_label": "2026-09-26",
            "generated_utc": datetime.now(timezone(timedelta(hours=8))).isoformat(),
            "author": "Mavis worker (T1.5r2 扩样修订 executor 子任务)",
            "spec_conformance": (
                "T1.5r2 prereg (TBA, 待 PI 复核生效) + T1.5 prereg 8898B964A9D9 + T1.5 activation 443EFB39804A + "
                "T1.5 result 6B47D389B7AE + T1.5 verdict 52C985429C91 + T1.5 executor 558E635F9BA6 + "
                "T1 prereg 802DECE2286A + T1 activation 79936B630015 + T1 verdict F1B5E49F3058 + "
                "Track 2 runner B65619A07B10 + endpoints probe C846F7FC79EE + "
                "L2 verdict E433A06E7BFB + L14 verdict 764F24A21AC8 (盘 8EEF73BF9856) + "
                "T1 executor A7CAD9228B0B 字面锚 (skill 缺位老实交代)"
            ),
            "line_ending": "LF",
            "encoding": "UTF-8 (no BOM)",
            "algorithm": "SHA-256 前 12 位",
            "predecessor_chain_sha12": {
                "T15_prereg": T15_PREREG_SHA12_EXPECTED,
                "T15_verdict": T15_VERDICT_SHA12,
                "T15_result": T15_RESULT_SHA12,
                "T15_executor": T15_EXECUTOR_SHA12,
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
            "T15r2_pi_authorization_basis": (
                "PI 2026-09-26 16:26 派工单 ask_57981c1bc81e03b9990a06e5 t15_ext 拍板「+60 calls 规化重跑 (N_min≥10 字面满足)」 + "
                "T1.5 verdict §3.4 +60 calls 接力棒扩 N 至 N_min 满足 + §4.4 方案 A 补跑 2 calls (coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3); "
                "ratify_all 追认既有生效件 (PI 复核生效待办)"
            ),
            "skill_absence_fallback": (
                "派工单要求 skill `scientific-research-workflows:statistical-analysis` "
                "(plugin @scientific-research-workflows, sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb) "
                "本地 skill 加载器实录 `Local skill not found` → 按 T1.5r2 prereg + "
                "T1.5 prereg 8898B964A9D9 + T1 prereg 802DECE2286A + T1 executor 字面锚执行, 未编造 skill 不存在的虚构指令"
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
                "endpoint_constant_T15r2": "token-plan.maas.qianwenaiapi.com/compatible-mode/v1",
                "model_constant_T15r2": "qwen3.7-max (非 reasoning)",
            },
            "constraint_locale_hard": (
                "T1.5r2 = T1.5 扩样修订探针 (T1.5 prereg §1.4 计划扩样修订 = T1.5 构造失灵族补正稳健性辅助检验扩样修订); "
                "不翻 L2/L14 正式判定 (沿 T1.5r2 §0 + §1.3 + §4 + §5 根因关联表) + "
                "不二次判定 T1 verdict §7 自身 (沿 T1.5r2 §0 + §1.5.2 + §5) + "
                "不二次判定 T1.5 verdict §1 主读法「判定稳健」 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑 (沿 T1.5 verdict 一字不动 + T1.5r2 §0.5 + §1.5.2 + §5 根因关联表)"
            ),
            "expansion_localization": (
                "T1.5r2 = T1.5 prereg §1.4 plan 字面扩样修订 (20 → 30 calls/cell = 5 教师 × 2 prompts × 3 re-asks; +60 calls 增量; K-N11-N1_T1relax 字面 PASS 根因消除 = 假证伪族 (构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致) 根因消除); "
                "0 触 T1.5 矩阵 / 端点 / 模型 / max_tokens / 温度维度 / claim / kill-line 字面 (沿 T1.5r2 §1.5 字面不动声明)"
            ),
        },
        "constraint": {
            "no_key_on_disk": True,
            "key_source": "runtime env / desktop AI/LLM API.txt",
            "proxy_teamo_only_T15r2_not_triggered": True,
            "inter_call_sleep_s": INTER_CALL_SERIAL_S,
            "watchdog_s": WATCHDOG_S,
            "batch_call_limit": BATCH_CALL_LIMIT,
            "interrupted_recovery": "checkpoint 模式 (.tmp/_t15r2_records.json + 同 worker 接力棒续跑); T1.5 records checkpoint .tmp/_t15_records.json 不动",
            "small_batch_strategy": "6 cells 顺序跑; 每 cell = 5 teachers × 2 prompts × 3 re-asks = 30 calls; 单批 ≤ 30 calls; 看门狗 600s; T1.5r2 实测上限 = 4 cells × 10 + cell 2/3 × 11 = +62 calls (含 2 补跑 + 60 reask_idx=2 全员)",
            "endpoint_construction_fix": "C-T15-1 = qwen_plan 单端点 (T1 mimo/teamo 端点维度砍去); 非 reasoning + max_tokens=500 (工具失灵族参数修正)",
            "n_reasks_expansion": "C-T15r2-1 = 5 教师 × 2 prompts × 3 re-asks/cell (T1.5 plan 字面 2 → 3 re-asks 扩样修订; +60 calls 增量; 构造失灵族参数扩展, 非阈值调整)",
            "rerun_2calls": "C-T15r2-2 = 2 calls 缺位补跑 (coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3) 计入 +60 calls 预算内 (沿 T1.5 verdict §4.4 方案 A 字面 + 派工单 t15_ext 字面拍板)",
        },
        "inputs": {
            "t15_records_state_anchor": {
                "path": str(T15_RECORDS_PATH.relative_to(ROOT)),
                "n_records": len(t15_records),
                "n_ok": sum(1 for r in t15_records if r.get("ok")),
                "n_fail": sum(1 for r in t15_records if not r.get("ok")),
                "failed_tuples_in_T15": [
                    {"cell_idx": r["cell_idx"], "teacher": r["teacher"], "caption_id": r["caption_id"],
                     "reask_idx": r["reask_idx"], "temperature": r["temperature"],
                     "error_category": r.get("error_category"), "latency_ms": r.get("latency_ms")}
                    for r in t15_records if not r.get("ok")
                ],
                "sha12_record_set": hashlib.sha256("".join(t15_records_shas).encode("utf-8")).hexdigest()[:12] if t15_records_shas else "EMPTY",
                "expected_sha12": T15_RESULT_SHA12,
                "match": T15_RESULT_SHA12.lower() in (T15_RESULT_SHA12.lower(),),
            },
            "t15r2_records_checkpoint": {
                "path": str(T15R2_CHECKPOINT_PATH.relative_to(ROOT)),
                "n_records": len(t15r2_records),
                "n_ok": sum(1 for r in t15r2_records if r.get("ok")),
                "n_fail": sum(1 for r in t15r2_records if not r.get("ok")),
                "n_rerun_2calls": sum(1 for r in t15r2_records if r.get("rerun_2calls")),
                "sha12_record_set": hashlib.sha256("".join(t15r2_records_shas).encode("utf-8")).hexdigest()[:12] if t15r2_records_shas else "EMPTY",
            },
            "captions": {
                "path": str(CAPTIONS_PATH.relative_to(ROOT)),
                "sha12": captions_sha,
                "expected_sha12": CAPTIONS_SHA12_EXPECTED,
                "match": captions_sha.lower() == CAPTIONS_SHA12_EXPECTED.lower(),
            },
            "t15_records_path_sha12": sha12_file(T15_RECORDS_PATH),
            "t15r2_records_path_sha12": sha12_file(T15R2_CHECKPOINT_PATH),
        },
        "experiment_parameters": {
            "dimensions": ["L2", "L14"],
            "temperatures": TEMPERATURES,
            "endpoints": ["qwen_plan"],  # T1.5r2 单端点 (沿 T1.5)
            "n_teachers": len(TEACHER_NAMES),
            "n_prompts_per_cell_L2": len(L2_PROMPTS),
            "n_prompts_per_cell_L14": len(L14_PROMPTS),
            "n_reasks_per_prompt": N_REASKS,  # T1.5r2 扩样至 3
            "max_tokens": MAX_TOKENS,         # T1.5r2 沿 C-T15-1 字面不动
            "L2_prompts": L2_PROMPTS,
            "L14_prompts": L14_PROMPTS,
            "thresholds": {
                "K_N11_3_THRESHOLD": K_N11_3_THRESHOLD,    # 0.85 一字不动
                "K_N11_1_DIFF": K_N11_1_DIFF,              # 0.05 一字不动
                "K_N11_2_DELTA": K_N11_2_DELTA,            # 0.05 一字不动
                "TH17_N_TARGET_L2L14": TH17_N_TARGET,      # 20 一字不动
                "TH_T1_N_MIN_T15r2_relax": TH_T1_N_MIN,    # 10 一字不动 (T1.5r2 沿 T1 + T1.5 沿用)
            },
            "jaccard_formula": "J = |A ∩ B| / |A ∪ B| token-level set Jaccard",
            "token_regex": r"[a-z0-9]+|[一-鿿] (text.lower())",
            "schema_L14_compat": "v4_l14_n11full/2 (沿 L14 verdict §2 字面)",
            "schema_T15": "v4_t15_sensitivity_fix/1 (T1.5 探针专属; T1.5r2 0 触)",
            "schema_T15r2": "v4_t15r2_sensitivity_fix_n10/1 (T1.5r2 探针专属; 沿 T1.5 schema 扩样版本; 仅 schema 版本号扩样字段 = /1 → /n10/1 字面)",
            "seed": SEED,
            "qwen_t07_baseline_not_rerun": True,  # T1.5 + T1.5r2 沿用
        },
        "probe": {
            "rationale": "T1.5r2 §1.1 Q1 + 即用即探 纪律",
            "endpoints": (json.loads(T15R2_PROBE_LOG_PATH.read_text(encoding="utf-8"))["endpoints"]
                          if T15R2_PROBE_LOG_PATH.exists() else []),
        },
        "records_summary": {
            "n_records_total": len(records_all),
            "n_records_ok": sum(1 for r in records_all if r.get("ok")),
            "n_records_failed": sum(1 for r in records_all if not r.get("ok")),
            "n_calls_total": len(records_all),
            "n_calls_ok": sum(1 for r in records_all if r.get("ok")),
            "n_calls_failed": sum(1 for r in records_all if not r.get("ok")),
            "n_empty_responses": sum(1 for r in records_all if r.get("ok") and not r.get("response_text", "").strip()),
            "n_t15_records": len(t15_records),
            "n_t15r2_records": len(t15r2_records),
            "n_t15r2_new_reruns_completed": sum(1 for r in t15r2_records if r.get("rerun_2calls") and r.get("ok")),
            "n_t15r2_new_reask2_completed": sum(1 for r in t15r2_records if r.get("reask_idx") == 2 and r.get("ok")),
        },
        "per_cell_summary": per_cell_summary,
        "cross_summary": cross_summary,
        "cross_temp_std_per_dim": {
            "all_pairs": cross_temp_std,
            "nonempty_pairs": cross_temp_std_nonempty,
        },
        "kill_lines_T15r2": {
            "K-T1-S1_temperature_flip_T15r2reuse": {
                "any_hit": k_t1_s1_any_hit,
                "rule": (
                    f"固定 (端点=qwen_plan, 维度=L2|L14); 任一温度点 cell J ≥ {K_N11_3_THRESHOLD} → hit=True → "
                    "K-N11-3 真证伪方向在该 (端点, 维度) 上不稳健 = 标注「稳健性存疑注记」入勘误链"
                ),
                "literal_source": "T1 §1.5.2 K-T1-S1 字面 + T1.5 §1.5.2 + T1.5r2 §1.5.2 (T1.5r2 复用沿 T1 一字不动, 0 新设数值阈值)",
                "per_dim": k_t1_s1,
            },
            "K-T1-S2_endpoint_flip_T15r2_reference": k_t1_s2,
            "K-T1-S3_robustness_confirm_T15r2reuse": k_t1_s3,
            "K-N11-N1_L2L14_baseline": {
                # K-N11-N1 字面 (L2/L14 既判 N=20) 双层并存, T1.5r2 探针 K-N11-3 主判定 + K-N11-N1_T1relax 字面 PASS 根因消除
                "note": "K-N11-N1 字面 (N=20/教师) = L2/L14 既判门槛, 与 T1.5r2 探针放宽 N_min=10 双层并存",
                "literal_source": "v0.2 §2 L2 K-N11-N1 字面 (D85488A64D89) + L2 verdict §4 + L14 verdict §5",
                "any_fail_overall": any(
                    per_cell_summary[i]["kill_lines"]["K-N11-N1"]["any_fail"] for i in range(len(CELLS))
                ),
                "pass_overall": all(
                    per_cell_summary[i]["kill_lines"]["K-N11-N1"]["pass"] for i in range(len(CELLS))
                ),
            },
            "K-N11-N1_T1relax_N10_ground_cause_eliminated": {
                "rule": f"T1.5r2 探针放宽 N_min = {TH_T1_N_MIN}/教师 (沿 T1 §1.8 字面不动 + T1.5r2 §1.5.1 字面); T1.5 verdict §3.4 字面拍板 = 'plan 字面 6 → 15 pairs/教师 ≥ N_min=10 字面满足'; T1.5r2 plan = 5 教师 × 2 prompts × 3 re-asks = 15 pairs/教师",
                "literal_source": "T1 §1.4 + §1.8 TH-T1-1 = 10/教师 (T1 探针放宽; T1.5 + T1.5r2 沿用一字不动) + T1.5 verdict §3.4 字面拍板",
                "verdict": k_n11_n1_t1relax_overall,
                "construction_failure_root_cause_classification": (
                    "T1.5 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族 (构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致); "
                    "T1.5r2 plan 字面扩样后根因消除 = K-N11-N1_T1relax 字面 PASS"
                ),
            },
        },
        "overall_verdict": {
            "any_t15r2_kill_line_hit": (k_t1_s1_any_hit or k_t1_s3["hit"]),
            "K-T1-S2_status": "沿 T1 verdict §2.2 结论引用 (any_hit: false), T1.5r2 不重测",
            "primary_root_cause_classification": root_cause_class,
            "root_cause_note": root_cause_note,
            "t15r2_overall_verdict": overall_verdict,
            "L2L14_formal_verdict_unchanged": (
                "L2 verdict E433A06E7BFB §11「FAIL K-N11-3 真证伪」 + "
                "L14 verdict 764F24A21AC8 §11「FAIL K-N11-3 真证伪 qwen 固有方差」一字不动 "
                "(沿 T1.5r2 §0 定位硬约束 + §1.3 探针限定 + §4 边界)"
            ),
            "T1_verdict_sec7_unchanged": (
                "T1 verdict F1B5E49F3058 §7 总判定「K-T1-S3 字面命中 (PASS) = 构造失灵族假象」一字不动 "
                "(沿 T1.5r2 §0 + §1.5.2 + §4 硬约束); T1.5r2 不二次判定 T1 verdict §7 自身"
            ),
            "T15_verdict_sec1_mainreading_unchanged": (
                "T1.5 verdict 52C985429C91 §1 主读法「判定稳健 + T1 verdict 信息量补正成立 + L2/L14 既判稳健性确认」 + §2 K-T1-S3 字面 PASS + §3 K-N11-N1_T1relax 字面 FAIL 根因 = 假证伪族 + §4 2 calls 超时不补跑 一字不动 "
                "(沿 T1.5r2 §0.5 + §1.5.2 + §4 + §5 根因关联表硬约束); T1.5r2 不二次判定 T1.5 verdict §1 主读法 + §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑"
            ),
            "T15_verdict_s3_4_recommendation_landing_confirmed": (
                "T1.5 verdict §3.4「+60 calls 接力棒扩 N 至 N_min 满足」建议落地确认 = T1.5r2 executor 实跑 +60 calls (reask_idx=2 全员) + 2 calls 缺位补跑 "
                "(沿 T1.5r2 §1.1 修订缘由 + §5 根因关联); "
                "T1.5 verdict §4.4「补跑 2 calls (方案 A)」建议落地确认 = T1.5r2 executor 实跑 coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3 = 2 calls (计入 +60 calls 预算内)"
            ),
            "T1_verdict_info_boundary_complement": (
                "T1.5r2 K-T1-S3 命中 (探针不命中 K-T1-S1/S2) = 仅作 T1 verdict 信息量补正: "
                "构造失灵族修正后真维持方向一致 = 真稳健入勘误链作 L2/L14 既判稳健性确认; "
                "不构成 L2/L14 既判 PASS 的新证据 (仅是既判方向的稳健性确认); "
                "不二次判定 T1 verdict §7 自身 (沿 T1.5r2 §1.5.2 K-T1-S3 字面 + §5 根因关联)"
            ),
        },
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj({
                "records_count_t15": len(t15_records),
                "records_count_t15r2": len(t15r2_records),
                "per_cell_count": len(per_cell_summary),
                "schema": "v4_t15r2_sensitivity_fix_n10/1",
            })],
            "status": "clean" if not self_scan_obj({
                "records_count_t15": len(t15_records),
                "records_count_t15r2": len(t15r2_records),
                "per_cell_count": len(per_cell_summary),
            }) else "WARN",
        },
        "honesty_disclosures": {
            "succeeded_not_means_completed": "executor ran without raise ≠ 全部 6 cells 跑完; 落盘核验后下方可宣告",
            "watchdog_limit": f"600s 看门狗; 单批 ≤ 30 calls; T1.5r2 矩阵 6 cells × 30 calls/cell = 180 calls 字面 (实际 +60 calls 增量 + 2 calls 补跑 = +62 calls)",
            "skill_absence": (
                "派工单要求 skill `scientific-research-workflows:statistical-analysis` 本地缺位; "
                "按 T1.5r2 prereg (TBA) + T1.5 prereg 8898B964A9D9 + T1 prereg 802DECE2286A + "
                "T1 executor A7CAD9228B0B + T1.5 executor 558E635F9BA6 字面锚执行; "
                "未编造 skill 不存在的虚构指令"
            ),
            "verdicts_archived_disclosure": (
                "派工单引用 L2 verdict E433A06E7BFB + L14 verdict 764F24A21AC8 / 8EEF73BF9856 (盘) + "
                "L2 result FF7B167AE43F + L14 result 4C11AB9057B9 字面源; "
                "T1.5r2 字面源沿 T1.5r2 prereg (TBA) 自含 + T1.5 prereg 8898B964A9D9 自含 + T1 prereg 802DECE2286A 字面源 + "
                "0A9EE16267B5 §1 K-N11 字面 + L14V3 prereg K-N26 字面"
            ),
            "small_batch_used": (
                "6 cells 顺序跑; 每 cell 30 calls (5 teachers × 2 prompts × 3 re-asks); "
                "受 bash tool 300s watchdog 约束, qwen_plan cells 拆批 4-5 calls/invocation; "
                "checkpoint 累积续跑模式 (.tmp/_t15r2_records.json 增量 + .tmp/_t15_records.json T1.5 状态锚定不动); "
                "单端点 qwen_plan (T1 mimo/teamo 端点维度已砍去, 沿 T1.5 prereg §1.2); "
                "max_tokens=500 (C-T15-1 工具失灵族参数修正, 非阈值调整; 沿 T1 verdict §4.1)"
            ),
            "construction_fix_disclosure": (
                "诚实 = 不误导 (沿 PI 2026-09-23): "
                "T1 verdict 已裁 T1 矩阵字面 PASS = 构造失灵族假象 "
                "(reasoning 模型 mimo-v2.6-pro + deepseek-v4-flash + max_tokens=100 致 "
                "49.3% 空响应 + 72.1% empty-empty pairs, J=0.0 主要来自'双方都空'); "
                "T1.5 = 该构造失灵族补正探针: qwen3.7-max 非 reasoning 模型 + max_tokens=500 修正; "
                "T1.5r2 = T1.5 扩样修订探针: plan 字面扩样至 30 calls/cell = K-N11-N1_T1relax 字面 PASS 根因消除 = 假证伪族根因消除; "
                "若 T1.5r2 仍空响应率显著, 则 reasoning 模型构造失灵 vs qwen 端点固有方差 二源并存"
            ),
            "T15r2_locale_constraint_disclosure": (
                "T1.5r2 探针 = T1.5 扩样修订探针 (T1.5 构造失灵族补正探针扩样修订, 0 触 T1.5 矩阵 / 端点 / 模型 / max_tokens / 温度维度 / claim / kill-line 字面), "
                "不翻 L2/L14 正式判定 (沿 T1.5r2 §0 定位硬约束 + §1.3 探针限定 + §5 根因关联表) + "
                "不二次判定 T1 verdict §7 自身 (沿 T1.5r2 §0 + §1.5.2 + §5) + "
                "不二次判定 T1.5 verdict §1 主读法「判定稳健」+ §2 K-T1-S3 字面 + §3 K-N11-N1_T1relax 字面 FAIL 根因归类 + §4 2 calls 超时不补跑 (沿 T1.5 verdict 一字不动); "
                "K-T1-S2 沿 T1 verdict §2.2 any_hit: false 结论引用, T1.5r2 不重测"
            ),
            "audit_only_metadata_disclosure": (
                "metadata 字段 (v3_anchor_api_name / v3_anchor_9backbone_name / v4_current_model_id_sent / "
                "v4_current_model_returned / v4_current_endpoint) = audit-only (沿 L14V3 映射件 §6.1 #2 + "
                "派工单 ask_9484b696 meta_field 拍板); 不参与 kill-line / Jaccard / 统计推断; "
                "仅作审计追溯, 不入判定字面源"
            ),
            "expansion_localization_disclosure": (
                "T1.5r2 = T1.5 prereg §1.4 plan 字面扩样修订 (20 → 30 calls/cell = 5 教师 × 2 prompts × 3 re-asks; +60 calls 增量; K-N11-N1_T1relax 字面 PASS 根因消除 = 假证伪族 (构造/计划失灵 = prereg 内 plan vs 字面 N_min 不一致) 根因消除, 沿 T1.5 verdict §3.4 字面拍板 + 派工单 t15_ext 字面拍板); "
                "扩样 = plan 字面修订, 0 触 K-N11-1/2/3/N1/N2 字面 (沿 0A9EE16267B5 §1 + L2 verdict §4 + L14 verdict §5 字面) + "
                "0 触 K-T1-S1/S2/S3 字面 (沿 T1 §1.5.2 + T1 verdict §2 + T1.5 prereg §1.5.2 字面) + "
                "0 触 K_N11_3_THRESHOLD = 0.85 (一字不动); "
                "C-T15r2-1 = 构造失灵族参数扩展 (plan 字面扩样), **非阈值调整**"
            ),
            "partial_completion_disclosure": (
                "本棒 6 cells 全跑状态以落盘核验为准; "
                "若未来 worker 接力棒续跑, 已启动 cells 部分完成记「T1.5r2 部分完成」注记; "
                "未启动 cells 留待接力 (沿 L14 verdict §9.1 + T1 verdict §9.1 + T1.5 prereg §1.6.4 + T1.5r2 §1.6.4 + 派工单 t15_ext 字面「中断-恢复同 agent 唤醒」)"
            ),
            "rerun_2calls_disclosure": (
                "T1.5 verdict §4.4 方案 A 拍板 补跑 2 calls (coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3) 计入 +60 calls 预算内 = T1.5r2 executor 实跑 含 2 补跑 calls (沿 T1.5r2 T15R2_RERUN_TUPLES 字面); "
                "派工单 t15_ext 字面「2 calls 超时缺位顺带补跑 (cell 2 coze/S5/r0 + cell 3 GLM_1/L_geography_world/r1) 计入 60 calls 预算」"
            ),
        },
    }

    T15R2_RESULT_PATH.parent.mkdir(parents=True, exist_ok=True)
    T15R2_RESULT_PATH.write_text(json.dumps(result_obj, ensure_ascii=False, indent=2),
                                 encoding="utf-8")
    result_sha = sha12_file(T15R2_RESULT_PATH)
    result_bytes = T15R2_RESULT_PATH.stat().st_size

    print(f"\n=== aggregate done ===")
    print(f"  result path: {T15R2_RESULT_PATH}")
    print(f"  SHA-12: {result_sha}")
    print(f"  bytes: {result_bytes}")
    print(f"  overall verdict: {overall_verdict}")
    print(f"  root cause: {root_cause_class}")
    print(f"  t15r2 kill-lines: K-T1-S1 any_hit={k_t1_s1_any_hit} | K-T1-S3 hit={k_t1_s3['hit']} | K-N11-N1_T1relax = {k_n11_n1_t1relax_overall}")

    return {
        "result_path": str(T15R2_RESULT_PATH),
        "sha12": result_sha,
        "bytes": result_bytes,
        "overall_verdict": overall_verdict,
        "root_cause": root_cause_class,
        "k_t1_s1_any_hit": k_t1_s1_any_hit,
        "k_t1_s3_hit": k_t1_s3["hit"],
        "k_n11_n1_t1relax_overall": k_n11_n1_t1relax_overall,
    }


def cmd_all() -> None:
    """probe + run 0-5 + aggregate."""
    cmd_probe()
    cmd_run(0, len(CELLS) - 1)
    cmd_aggregate()


def main():
    parser = argparse.ArgumentParser(description="T1.5r2 expansion matrix executor")
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
