# -*- coding: utf-8 -*-
"""
================================================================================
T1 探针 · qwen 温度扫描 · r2 棒 (re-asks 2 -> 3 + 响应提取面并修)
================================================================================
授权锚  : PI 2026-10-09 卡 ask_52effb1125dc64e6dac3295f
          主裁 = 乙 (补构造至 >=10 对; re-asks 2->3; ~+60 calls; T15r2 先例)
          附款 = 「并修提取面 + 授权起跑」
上承    : 修订案 24DA21074CC2 (_th_t1_n_min_revision_proposal_2026_10_09.md) §2.2 乙档
          判定件 DFC858D3D930 (_t1_qwen_temp_sweep_verdict_2026_10_09.md) §2.3 / §4.2 / §7.1

构造 (沿 r1 全同, 仅两处并案修正):
  (i)  样本量面 : N_REASKS 2 -> 3   (2 prompts x 3 re-asks = 6 records/教师/cell
                                     => C(6,2)=15 pairs/教师 >= TH_T1_N_MIN=10)
  (ii) 响应提取面: 度量对象 = 完整教师回复 (message.reasoning_content + message.content);
                   ⛔ 0 只取 message.content; ⛔ 0 截段 (finish_reason 逐条落盘)

路线   : 全量 180 calls (0 承接 r1 120) —— 依据: r1 records (.tmp/_t1_qwen_temp_sweep_records.json,
         sha12 5B51AF62C640) 经实测 ⛔ 0 含 reasoning_content 字段 (仅 response_text=message.content),
         故 r1 之 120 records 不能充当已修提取面之度量对象; 沿用之即复现 1-9 字符残段缺陷。
         全量: 5 教师 x 2 prompts x 3 re-asks = 30 calls/cell x 6 cells = 180 calls。

纪律   : 0 判读 / 0 宣告达标 (判定归 verdict-keeper 新件)
         0 合并派生 JSON (R5) / 0 覆写 r1 任一件 / 0 触 frozen
         R4: key 永不明文, 0 落盘, 0 回显
         中间产物仅落 .tmp/; 唯一落 results/ 者 = aggregate 之 result JSON (新名)
================================================================================
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import statistics
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests as _requests

# 控制台安全: Windows GBK 控制台 ⛔ 0 能渲染 ⛔ 等非 ASCII 字面 (0 影响落盘内容)
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass

# ============================================================
# 常量与路径 (r2 独立 prefix, ⛔ 0 覆写 r1 任一件)
# ============================================================
ROOT = Path("D:/私人资料/deposon-repo")
RESULTS_DIR = ROOT / "results"
TMP_DIR = ROOT / ".tmp"

CHECKPOINT_PATH = TMP_DIR / "_t1_qwen_temp_sweep_r2_records.json"
SELFCERT_PATH = TMP_DIR / "_t1_qwen_temp_sweep_r2_selfcert.json"
PROBE_LOG_PATH = TMP_DIR / "_t1_qwen_temp_sweep_r2_probe_log.json"
CALIB_PATH = TMP_DIR / "_t1_r2_calib_max_tokens_2026_10_09.json"
RESULT_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_r2_result_2026_10_09.json"

KEY_SOURCE_PATH = Path("C:/Users/Administrator/Desktop/AI/LLM API.txt")
CAPTIONS_PATH = ROOT / "corpus/v20_caption_surface/strip_captions_22.json"
CAPTIONS_SHA12_EXPECTED = "6A2656878745"

# 输入件 (⛔ 0 回改; 起跑前 SHA-12 硬闸)
REVISION_PATH = RESULTS_DIR / "_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md"
REVISION_SHA12_EXPECTED = "BDA5D5F3DFA0"
ANCHOR_PATH = RESULTS_DIR / "_v4_supp_prereg_v02_add_T1_2026_09_24.md"
ANCHOR_SHA12_EXPECTED = "802DECE2286A"
VERDICT_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_verdict_2026_10_09.md"
VERDICT_SHA12_EXPECTED = "DFC858D3D930"
R1_EXECUTOR_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_executor_2026_10_09.py"
R1_EXECUTOR_SHA12_EXPECTED = "F0C845864603"
R1_REGISTER_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_exec_register_2026_10_09.md"
R1_REGISTER_SHA12_EXPECTED = "7AD31E741400"
PROPOSAL_PATH = RESULTS_DIR / "_th_t1_n_min_revision_proposal_2026_10_09.md"
PROPOSAL_SHA12_EXPECTED = "24DA21074CC2"

# ============================================================
# 阈值 (沿用, 0 新设) —— 本棒 0 判读, 仅登记读数
# ============================================================
K_N11_3_THRESHOLD = 0.85
TH_T1_N_MIN = 10
INTER_CALL_SERIAL_S = 2.5
WATCHDOG_S = 600
BATCH_CALL_LIMIT = 30
CALL_TIMEOUT_S = 90  # 沿 r1 字面

# ============================================================
# 5 教师 / 2 prompts (沿 TH-14, 全同 r1)
# ============================================================
TEACHER_PATHS_REL = [
    ("kimi",    "corpus/v20/by_model/kimi/index_v2_2026_09_16.json"),
    ("GLM_1",   "corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json"),
    ("GLM_2",   "corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json"),
    ("coze",    "corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json"),
    ("minimax", "corpus/v20/by_model/minimax/artifact_v_2026_09_16.json"),
]
TEACHER_NAMES = [t[0] for t in TEACHER_PATHS_REL]
SEED = 42

L2_PROMPTS = ["L_biological_taxonomy", "S5"]
L14_PROMPTS = ["L_geography_world", "L_historical_causality"]

# (i) 样本量面修正: re-asks 2 -> 3
N_REASKS = 3

# ============================================================
# 端点 (qwen 单端点, 沿 r1/T15 executor 体例)
# ============================================================
ENDPOINTS = {
    "qwen_plan": {
        "label": "qwen_plan",
        "endpoint": "https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1",
        "model_id": "qwen3.7-max",
        "key_index_1based": 23,
        "use_proxy": False,
    },
}
TEMPERATURES = [0.0, 0.3, 0.5]

CELLS: List[Tuple[str, float]] = []
for _dim in ("L2", "L14"):
    for _t in TEMPERATURES:
        CELLS.append((_dim, _t))

# (ii) 响应提取面修正 —— max_tokens 取值依据 (实测, 见 CALIB_PATH):
#   校准 3 档 {500, 2000, 4000} x 2 calls = 6 calls 实测:
#     finish_reason = stop 6/6 (⛔ 0 截段); usage.completion_tokens 705..4926 ≫ 请求值
#     => 端点 0 以 max_tokens 约束 reasoning_tokens; content_len 恒 1..3 字符 (与 max_tokens 0 相关)
#   => 无截断所需值 = 500 (r1 原值即已无截断); 上调 2000/4000 实测 0 改变 content_len、
#      且 2000 档实测 completion_tokens 4926 / latency 75.6s (抬高超时风险)
#   => 据实测保留 MAX_TOKENS=500 (与 r1 该轴 0 漂移); 提取面之实修 = 取 reasoning_content (全量回复)
MAX_TOKENS = 500

# ============================================================
# key 形态自扫 (R4)
# ============================================================
SENSITIVE_PATTERNS = [
    ("sk_literal", re.compile(r"(?i)sk-[A-Za-z0-9_\-]{20,}")),
    ("AIza_literal", re.compile(r"(?i)AIza[0-9A-Za-z_\-]{30,}")),
    ("Bearer_token", re.compile(r"(?i)Bearer\s+[A-Za-z0-9]{20,}")),
]


def self_scan_text(text: str) -> List[Tuple[str, int]]:
    hits: List[Tuple[str, int]] = []
    for name, pat in SENSITIVE_PATTERNS:
        n = len(pat.findall(text))
        if n > 0:
            hits.append((name, n))
    return hits


def self_scan_obj(obj: Any) -> List[Tuple[str, int]]:
    return self_scan_text(json.dumps(obj, ensure_ascii=False, sort_keys=True))


def sha12_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def sha12_file(path: Path) -> str:
    return sha12_bytes(path.read_bytes())


def now_local() -> str:
    return datetime.now(timezone(timedelta(hours=8))).isoformat()


# ============================================================
# Key 加载 (runtime 读入内存, 0 落盘, 0 明文, 0 回显)
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
    key = text.splitlines()[key_index_1based - 1].strip()
    if not key or len(key) < 20:
        raise RuntimeError(f"key line {key_index_1based} empty or too short; abort")
    return key


def key_slot_fact(key_index_1based: int) -> Dict[str, Any]:
    """仅登记存在性/长度/形态类别 —— ⛔ 0 读出并回显 key 值 (沿 r1 exec register §4 体例)。"""
    raw = KEY_SOURCE_PATH.read_bytes()
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    else:
        return {"slot": key_index_1based, "exists": False}
    lines = text.splitlines()
    exists = len(lines) >= key_index_1based
    val = lines[key_index_1based - 1].strip() if exists else ""
    prefix_class = (val.split("-")[0] + "-") if val.startswith("sk-") else (
        val[:4] if val else "")
    return {"slot": key_index_1based, "exists": exists, "len": len(val),
            "prefix_class": prefix_class, "value_read_into_artifacts": False}


def unset_proxy() -> None:
    for k in ("https_proxy", "http_proxy", "all_proxy"):
        os.environ.pop(k, None)


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


# ============================================================
# 端点调用 (含 (ii) 响应提取面修正)
# ============================================================
def call_chat(api_key: str, endpoint: str, model: str,
              messages: List[Dict[str, str]], temperature: float,
              max_tokens: int, timeout: int = CALL_TIMEOUT_S,
              use_proxy: bool = False) -> Dict[str, Any]:
    headers = {"Authorization": f"Bearer {api_key}",
               "Content-Type": "application/json"}
    body = {"model": model, "messages": messages,
            "temperature": temperature, "max_tokens": max_tokens,
            "stream": False}
    chat_url = endpoint.rstrip("/") + "/chat/completions"
    t0 = time.time()
    try:
        r = _requests.post(chat_url, headers=headers, json=body, timeout=timeout)
        latency_ms = round((time.time() - t0) * 1000, 1)
        if r.status_code != 200:
            return {"ok": False, "status_code": r.status_code,
                    "error_category": classify_status(r.status_code),
                    "latency_ms": latency_ms,
                    "error_body_snippet": r.text[:300]}
        data = r.json()
        choice0 = (data.get("choices") or [{}])[0]
        msg = choice0.get("message", {}) or {}
        content = msg.get("content") or ""
        reasoning = msg.get("reasoning_content") or ""
        finish_reason = choice0.get("finish_reason")
        # 度量对象 = 完整教师回复 (reasoning + content); ⛔ 0 只取 content; ⛔ 0 截段
        full = (reasoning + "\n\n" + content) if reasoning else content
        return {"ok": True, "status_code": r.status_code, "latency_ms": latency_ms,
                "model_returned": data.get("model", ""), "id": data.get("id", ""),
                "content": content, "reasoning_content": reasoning,
                "full_reply": full, "finish_reason": finish_reason,
                "usage": data.get("usage", {})}
    except _requests.exceptions.Timeout as e:
        return {"ok": False, "error_category": "timeout",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}
    except Exception as e:  # noqa: BLE001
        return {"ok": False, "error_category": "other",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}


# ============================================================
# Jaccard (沿 r1 字面)
# ============================================================
TOKEN_RE = re.compile(r"[a-z0-9]+|[\u4e00-\u9fff]")


def tokenize(text: str) -> List[str]:
    return TOKEN_RE.findall(text.lower())


def jaccard(a: str, b: str) -> float:
    sa, sb = set(tokenize(a)), set(tokenize(b))
    if not sa and not sb:
        return 0.0
    union = sa | sb
    if not union:
        return 0.0
    return len(sa & sb) / len(union)


# ============================================================
# Captions / prompts (全同 r1)
# ============================================================
def load_captions() -> List[Dict[str, Any]]:
    return json.loads(CAPTIONS_PATH.read_text(encoding="utf-8"))


def select_prompts(captions: List[Dict[str, Any]], ids: List[str]) -> List[Dict[str, Any]]:
    by_id = {c["id"]: c for c in captions}
    out = []
    for pid in ids:
        if pid not in by_id:
            raise KeyError(f"prompt_id {pid} not in captions")
        out.append(by_id[pid])
    return out


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
# 输入件硬闸 (⛔ 0 回改)
# ============================================================
INPUT_GATES = [
    ("revision", REVISION_PATH, REVISION_SHA12_EXPECTED),
    ("anchor", ANCHOR_PATH, ANCHOR_SHA12_EXPECTED),
    ("verdict_dfc858d3d930", VERDICT_PATH, VERDICT_SHA12_EXPECTED),
    ("r1_executor", R1_EXECUTOR_PATH, R1_EXECUTOR_SHA12_EXPECTED),
    ("r1_exec_register", R1_REGISTER_PATH, R1_REGISTER_SHA12_EXPECTED),
    ("proposal_24da21074cc2", PROPOSAL_PATH, PROPOSAL_SHA12_EXPECTED),
]


def verify_input_gates() -> Dict[str, Any]:
    out = {}
    bad = []
    for name, path, expected in INPUT_GATES:
        if not path.exists():
            out[name] = {"sha12": None, "expected": expected, "match": False, "exists": False}
            bad.append(f"{name}: MISSING")
            continue
        sha = sha12_file(path)
        ok = sha.upper() == expected.upper()
        out[name] = {"sha12": sha.upper(), "expected": expected.upper(),
                     "match": ok, "bytes": path.stat().st_size}
        if not ok:
            bad.append(f"{name}: {sha} != {expected}")
    return {"gates": out, "all_match": not bad, "failures": bad}


# ============================================================
# 构造面自证 (开跑前落 .tmp)
# ============================================================
def cmd_selfcert() -> None:
    print("=== T1-r2 构造面自证 (开跑前) ===")
    caps = load_captions()
    by_id = {c["id"]: c for c in caps}
    used_ids = L2_PROMPTS + L14_PROMPTS
    texts = [by_id[i]["text"] for i in used_ids]

    def stats(vals: List[Any]) -> Dict[str, Any]:
        n = len(vals)
        nd = len(set(vals))
        if all(isinstance(v, (int, float)) for v in vals) and n > 0:
            return {"n": n, "n_distinct": nd, "min": min(vals), "max": max(vals),
                    "mean": round(statistics.fmean(vals), 6),
                    "std": round(statistics.pstdev(vals), 6) if n > 1 else 0.0}
        return {"n": n, "n_distinct": nd, "min": "n/a(str)", "max": "n/a(str)",
                "mean": "n/a", "std": "n/a"}

    calib = {}
    if CALIB_PATH.exists():
        c = json.loads(CALIB_PATH.read_text(encoding="utf-8"))
        for row in c.get("rows", []):
            calib.setdefault(str(row.get("max_tokens_requested")), []).append({
                "finish_reason": row.get("finish_reason"),
                "content_len": row.get("content_len"),
                "reasoning_len": row.get("reasoning_len"),
                "reasoning_present": row.get("reasoning_present"),
                "usage_completion_tokens": row.get("usage_completion_tokens"),
                "usage_reasoning_tokens": row.get("usage_reasoning_tokens"),
                "latency_ms": row.get("latency_ms"),
            })

    report = {
        "task": "t1_r2_qwen_temp_sweep_selfcert",
        "generated_local": now_local(),
        "authorization": {
            "pi_card": "ask_52effb1125dc64e6dac3295f",
            "main_decision": "乙 (补构造至 >=10 对; re-asks 2->3; ~+60 calls)",
            "annex": "并修提取面 + 授权起跑",
            "upstream": ["24DA21074CC2 §2.2", "DFC858D3D930 §2.3/§4.2/§7.1"],
        },
        "input_gates": verify_input_gates(),
        "captions_sha12": sha12_file(CAPTIONS_PATH),
        "captions_sha12_expected": CAPTIONS_SHA12_EXPECTED,
        "matrix": {
            "n_cells": len(CELLS),
            "cells": [{"cell_idx": i, "dim": d, "temperature": t}
                      for i, (d, t) in enumerate(CELLS)],
            "endpoint": ENDPOINTS["qwen_plan"]["endpoint"],
            "model_id": ENDPOINTS["qwen_plan"]["model_id"],
            "max_tokens": MAX_TOKENS,
            "n_teachers": len(TEACHER_NAMES),
            "n_reasks": N_REASKS,
            "calls_per_cell": len(TEACHER_NAMES) * 2 * N_REASKS,
            "total_calls": len(CELLS) * len(TEACHER_NAMES) * 2 * N_REASKS,
            "records_per_teacher_per_cell": 2 * N_REASKS,
            "pairs_per_teacher_per_cell": 2 * N_REASKS,
            "pairs_ctor_C6_2": 15,
        },
        "construction_fixes": {
            "fix_1_sample_size": "N_REASKS 2 -> 3 (6 records/教师/cell => C(6,2)=15 pairs/教师)",
            "fix_2_response_extraction": {
                "measurement_object": "完整教师回复 = message.reasoning_content + message.content",
                "forbidden": ["只取 message.content", "截段"],
                "r1_defect_evidence": "r1 records 实测 ⛔ 0 reasoning_content 字段 (仅 response_text)",
                "max_tokens_determination": "实测保留 500 (finish_reason 6/6 = stop; completion_tokens 705..4926 ≫ 请求值 => 端点 0 以 max_tokens 约束 reasoning)",
                "calibration_rows_by_max_tokens": calib,
            },
        },
        "route_decision": "全量 180 calls (0 承接 r1 120)",
        "input_field_stats": {
            "caption_ids_used": stats(used_ids),
            "caption_text_char_len": stats([len(t) for t in texts]),
            "caption_text_token_len": stats([len(tokenize(t)) for t in texts]),
            "temperature": stats(TEMPERATURES),
            "teacher_names": stats(TEACHER_NAMES),
            "reask_idx": stats(list(range(N_REASKS))),
        },
        "kill_line_literal_reference_only": {
            "note": "本棒 0 判读; 以下仅为引用 r1/修订件字面, 本件 0 出任何 PASS/FAIL",
            "TH_T1_N_MIN": TH_T1_N_MIN,
            "K_N11_3_THRESHOLD": K_N11_3_THRESHOLD,
        },
        "key_slot_fact": key_slot_fact(ENDPOINTS["qwen_plan"]["key_index_1based"]),
        "key_reading_note": "key 仅 runtime 读入内存用于调用; 0 落盘 0 明文 0 回显 (R4)",
    }
    report["key_shape_self_scan"] = {
        "hits": [{"name": n, "count": c} for n, c in self_scan_obj(report)],
        "status": "clean" if not self_scan_obj(report) else "WARN",
    }
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    SELFCERT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                             encoding="utf-8", newline="\n")
    print(f"selfcert written: {SELFCERT_PATH}")
    print(f"input gates all_match: {report['input_gates']['all_match']}")
    if report["input_gates"]["failures"]:
        print("FATAL:", report["input_gates"]["failures"])
        sys.exit(1)


def cmd_probe() -> None:
    print("=== 即用即探: qwen_plan (1 call) ===")
    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])
    r = call_chat(api_key, ep["endpoint"], ep["model_id"],
                  messages=[{"role": "user", "content": "ping"}],
                  temperature=0.0, max_tokens=MAX_TOKENS, timeout=CALL_TIMEOUT_S)
    out = {
        "endpoint_label": ep["label"], "endpoint": ep["endpoint"],
        "model_id": ep["model_id"], "max_tokens": MAX_TOKENS,
        "ok": bool(r.get("ok")), "status_code": r.get("status_code"),
        "error_category": r.get("error_category"),
        "latency_ms": r.get("latency_ms"),
        "model_returned": r.get("model_returned", ""),
        "finish_reason": r.get("finish_reason"),
        "content_len": len(r.get("content", "") or ""),
        "reasoning_len": len(r.get("reasoning_content", "") or ""),
        "reasoning_present": bool(r.get("reasoning_content", "")),
        "full_reply_len": len(r.get("full_reply", "") or ""),
        "error_body_snippet": (r.get("error_body_snippet") or "")[:200],
        "error_snippet": (r.get("error_snippet") or "")[:200],
        "key_slot_fact": key_slot_fact(ep["key_index_1based"]),
        "note": "key 0 落盘 0 明文 (R4); 本条 0 含 key 值",
    }
    out["key_shape_self_scan"] = {
        "hits": [{"name": n, "count": c} for n, c in self_scan_obj(out)],
        "status": "clean" if not self_scan_obj(out) else "WARN",
    }
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    PROBE_LOG_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                              encoding="utf-8", newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    if not out["ok"]:
        print("FATAL: probe failed -> 停手上报 (0 绕过 0 改端点)")
        sys.exit(1)


# ============================================================
# Checkpoint (仅 .tmp/)
# ============================================================
def load_checkpoint() -> List[Dict[str, Any]]:
    if CHECKPOINT_PATH.exists():
        try:
            return json.loads(CHECKPOINT_PATH.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def save_checkpoint(records: List[Dict[str, Any]]) -> None:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    CHECKPOINT_PATH.write_text(json.dumps(records, ensure_ascii=False),
                               encoding="utf-8", newline="\n")


def rec_key(r: Dict[str, Any]) -> Tuple[int, str, str, int, float]:
    return (r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"])


def ok_map(records: List[Dict[str, Any]]) -> Dict[Any, Dict[str, Any]]:
    """cell -> tuple -> 最近一条 ok record (续跑锚)"""
    m: Dict[Any, Dict[str, Any]] = {}
    for r in records:
        if r.get("ok"):
            m.setdefault(r["cell_idx"], {})[rec_key(r)[1:]] = r
    return m


def run_cell(cell_idx: int, dim: str, temp: float,
             captions: List[Dict[str, Any]], records: List[Dict[str, Any]],
             wall_start: float, retry_failed: bool = False,
             max_calls_in_cell: int = 0) -> Dict[str, Any]:
    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])

    prompts_ids = L2_PROMPTS if dim == "L2" else L14_PROMPTS
    prompts_list = select_prompts(captions, prompts_ids)

    okm = ok_map(records)
    have_ok = okm.get(cell_idx, {})
    failed_here = [r for r in records
                   if not r.get("ok") and r.get("cell_idx") == cell_idx]

    summary = {"cell_idx": cell_idx, "dim": dim, "temperature": temp,
               "endpoint_label": ep["label"], "endpoint": ep["endpoint"],
               "model_id": ep["model_id"], "max_tokens": MAX_TOKENS,
               "prompts": prompts_ids,
               "n_calls_planned": len(TEACHER_NAMES) * len(prompts_list) * N_REASKS,
               "n_calls_ok": 0, "n_calls_failed": 0,
               "n_skipped_existing_ok": 0, "n_retried_failed": 0}

    n_new = 0
    for teacher_name in TEACHER_NAMES:
        teacher_path_rel = next((p[1] for n, p in TEACHER_PATHS_REL if n == teacher_name), "")
        for prompt_obj in prompts_list:
            caption_id = prompt_obj["id"]
            caption_text = prompt_obj["text"]
            for ri in range(N_REASKS):
                kt = (teacher_name, caption_id, ri, temp)
                if kt in have_ok:
                    summary["n_skipped_existing_ok"] += 1
                    continue
                if not retry_failed and kt in {(r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"])
                                               for r in failed_here}:
                    # 仅在 retry 模式下补跑失败 tuple; 否则跳过 (防重复计 calls)
                    continue
                if n_new > 0:
                    time.sleep(INTER_CALL_SERIAL_S)
                if max_calls_in_cell > 0 and n_new >= max_calls_in_cell:
                    summary["calls_limit_break"] = True
                    save_checkpoint(records)
                    return summary
                if time.time() - wall_start > WATCHDOG_S:
                    summary["watchdog_break"] = True
                    save_checkpoint(records)
                    return summary

                messages = [{"role": "system", "content": PROMPT_SYSTEM},
                            {"role": "user", "content": build_user_prompt(
                                teacher_name, caption_id, caption_text)}]
                t0 = time.time()
                resp = call_chat(api_key, ep["endpoint"], ep["model_id"], messages,
                                 temperature=temp, max_tokens=MAX_TOKENS,
                                 timeout=CALL_TIMEOUT_S, use_proxy=ep["use_proxy"])
                elapsed = time.time() - t0
                ok = bool(resp.get("ok"))
                content = resp.get("content", "") if ok else ""
                reasoning = resp.get("reasoning_content", "") if ok else ""
                full = resp.get("full_reply", "") if ok else ""
                usage = resp.get("usage", {}) if ok else {}
                is_rerun = any(
                    (r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"]) == kt
                    for r in failed_here)
                rec = {
                    "cell_idx": cell_idx, "endpoint_label": ep["label"],
                    "endpoint": ep["endpoint"], "endpoint_model": ep["model_id"],
                    "use_proxy": ep["use_proxy"], "dim": dim, "temperature": temp,
                    "max_tokens": MAX_TOKENS, "teacher": teacher_name,
                    "teacher_path_rel": teacher_path_rel, "caption_id": caption_id,
                    "caption_text_sha12": sha12_bytes(caption_text.encode("utf-8")),
                    "reask_idx": ri, "ok": ok,
                    "content_text": content,
                    "reasoning_text": reasoning,
                    "full_reply_text": full,
                    "finish_reason": resp.get("finish_reason") if ok else None,
                    "truncated": (resp.get("finish_reason") == "length") if ok else None,
                    "content_len": len(content),
                    "reasoning_len": len(reasoning),
                    "full_reply_len": len(full),
                    "full_reply_sha12": sha12_bytes(full.encode("utf-8")) if ok else "",
                    "latency_ms": round(elapsed * 1000, 1),
                    "status_code": resp.get("status_code"),
                    "error_category": resp.get("error_category"),
                    "model_returned": resp.get("model_returned", ""),
                    "usage": usage,
                    "is_rerun_of_failed": bool(is_rerun),
                    "timestamp_local": now_local(),
                }
                records.append(rec)
                n_new += 1
                save_checkpoint(records)
                if ok:
                    summary["n_calls_ok"] += 1
                    if is_rerun:
                        summary["n_retried_failed"] += 1
                    print(f"  [{cell_idx}] {teacher_name}/{caption_id}/r{ri} ok "
                          f"(lat={rec['latency_ms']:.0f}ms, full_len={rec['full_reply_len']}, "
                          f"reasoning_len={rec['reasoning_len']}, fr={rec['finish_reason']})"
                          f"{' RERUN' if is_rerun else ''}", flush=True)
                else:
                    summary["n_calls_failed"] += 1
                    print(f"  [{cell_idx}] {teacher_name}/{caption_id}/r{ri} FAIL "
                          f"{rec['error_category']} (lat={rec['latency_ms']:.0f}ms)", flush=True)
    return summary


def cmd_run(start_idx: int, end_idx: int, calls_limit: int = 0,
            retry_failed: bool = False) -> None:
    mode = "retry-failed" if retry_failed else "run"
    print(f"=== T1-r2 qwen 温扫 {mode} cells [{start_idx},{end_idx}] "
          f"(calls_limit={calls_limit}) ===", flush=True)
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    gates = verify_input_gates()
    if not gates["all_match"]:
        print(f"FATAL: input gate mismatch: {gates['failures']}")
        sys.exit(1)
    caps_sha = sha12_file(CAPTIONS_PATH)
    if caps_sha.upper() != CAPTIONS_SHA12_EXPECTED.upper():
        print(f"FATAL: captions SHA-12 mismatch: {caps_sha}")
        sys.exit(1)

    captions = load_captions()
    records = load_checkpoint()
    print(f"input gates OK; captions SHA-12 OK ({caps_sha}); "
          f"loaded {len(records)} existing records", flush=True)

    wall_start = time.time()
    summaries = []
    calls_made = 0
    for idx in range(start_idx, end_idx + 1):
        if idx < 0 or idx >= len(CELLS):
            continue
        dim, temp = CELLS[idx]
        print(f"\n--- cell {idx}: {dim} / temp={temp} / qwen_plan ---", flush=True)
        if time.time() - wall_start > WATCHDOG_S:
            print("  [watchdog] stopping batch")
            break
        if calls_limit > 0 and calls_made >= calls_limit:
            print("  [calls_limit] stopping batch")
            break
        s = run_cell(idx, dim, temp, captions, records, wall_start,
                     retry_failed=retry_failed,
                     max_calls_in_cell=calls_limit - calls_made if calls_limit > 0 else 0)
        summaries.append(s)
        calls_made += s["n_calls_ok"] + s["n_calls_failed"]
        if s.get("watchdog_break"):
            break

    save_checkpoint(records)
    wall = time.time() - wall_start
    print(f"\n=== batch done: wall={wall:.1f}s new_calls={calls_made} "
          f"total_records={len(records)} ===", flush=True)
    for s in summaries:
        print(f"  cell {s['cell_idx']} ({s['dim']}/t={s['temperature']}): "
              f"ok={s['n_calls_ok']} fail={s['n_calls_failed']} "
              f"skip_ok={s['n_skipped_existing_ok']} rerun={s['n_retried_failed']} "
              f"wd={s.get('watchdog_break', False)}")


# ============================================================
# Aggregate -> results/ (新名 result JSON; 0 判读)
# ============================================================
def compute_j(caliber: str, recs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """按 caliber 取文本; 返回 per (cell, teacher) J 中位 + 拆解。⛔ 0 出判定。"""
    def text_of(r: Dict[str, Any]) -> str:
        if caliber == "content_only":
            return r.get("content_text", "")
        if caliber == "reasoning_only":
            return r.get("reasoning_text", "")
        return r.get("full_reply_text", "")

    by_ct: Dict[Tuple[int, str], List[Dict[str, Any]]] = {}
    for r in recs:
        by_ct.setdefault((r["cell_idx"], r["teacher"]), []).append(r)

    out: Dict[str, Any] = {}
    for k, rs in by_ct.items():
        n = len(rs)
        jvs_all, jvs_ne, n_ee = [], [], 0
        same, cross = [], []
        for i in range(n):
            for j in range(i + 1, n):
                ti, tj = text_of(rs[i]), text_of(rs[j])
                jv = jaccard(ti, tj)
                jvs_all.append(jv)
                if tokenize(ti) and tokenize(tj):
                    jvs_ne.append(jv)
                else:
                    n_ee += 1
                if rs[i]["caption_id"] == rs[j]["caption_id"]:
                    same.append(jv)
                else:
                    cross.append(jv)
        out[f"{k[0]}|{k[1]}"] = {
            "cell_idx": k[0], "teacher": k[1], "n_records": n,
            "n_pairs_all": len(jvs_all), "n_pairs_nonempty": len(jvs_ne),
            "n_pairs_empty_empty": n_ee,
            "j_median_all": (float(statistics.median(jvs_all)) if jvs_all else None),
            "j_median_nonempty": (float(statistics.median(jvs_ne)) if jvs_ne else None),
            "j_median_same_caption": (float(statistics.median(same)) if same else None),
            "j_median_cross_caption": (float(statistics.median(cross)) if cross else None),
            "n_pairs_same": len(same), "n_pairs_cross": len(cross),
            "n_ge_0_85": (sum(1 for v in jvs_all if v >= K_N11_3_THRESHOLD)),
            "j_values_all": [round(v, 6) for v in jvs_all],
        }
    return out


def axis_divergence(caliber: str, recs: List[Dict[str, Any]]) -> Dict[str, Any]:
    """温度轴有效性面: t=0.3/0.5 对 t=0.0, 同 teacher 同 caption 文本全同计数。"""
    def text_of(r: Dict[str, Any]) -> str:
        if caliber == "content_only":
            return r.get("content_text", "")
        if caliber == "reasoning_only":
            return r.get("reasoning_text", "")
        return r.get("full_reply_text", "")

    idx: Dict[Tuple[int, str, str], Dict[float, List[str]]] = {}
    for r in recs:
        idx.setdefault((r["cell_idx"], r["teacher"], r["caption_id"]), {}) \
            .setdefault(r["temperature"], []).append(text_of(r))
    cell0 = {}
    for ci in range(len(CELLS)):
        dim, t = CELLS[ci]
        if t != 0.0:
            continue
        cell0[dim] = ci
    rows = []
    for ci, (dim, t) in enumerate(CELLS):
        if t == 0.0:
            continue
        base_ci = cell0[dim]
        n_cmp = n_same = 0
        for (c, teacher, cap), by_t in idx.items():
            if c != ci:
                continue
            a, b = by_t.get(t, []), idx.get((base_ci, teacher, cap), {}).get(0.0, [])
            for x in a:
                for y in b:
                    n_cmp += 1
                    if x == y:
                        n_same += 1
        rows.append({"cell_idx": ci, "dim": dim, "temperature": t,
                     "base_cell_idx": base_ci,
                     "n_compared": n_cmp, "n_identical": n_same,
                     "identical_rate": (round(n_same / n_cmp, 6) if n_cmp else None)})
    return {"caliber": caliber, "per_temp": rows}


def cmd_aggregate() -> None:
    print("=== aggregate: 读数登记 (⛔ 0 判读; 判定归 verdict-keeper 新件) ===")
    records = load_checkpoint()
    if not records:
        print("FATAL: no records")
        sys.exit(1)

    ok_recs = [r for r in records if r.get("ok")]
    fail_recs = [r for r in records if not r.get("ok")]

    # 自证项 1: 空响应率 (两口径: 度量对象 full_reply / content_only)
    n_empty_full = sum(1 for r in ok_recs if not tokenize(r.get("full_reply_text", "")))
    n_empty_content = sum(1 for r in ok_recs if not tokenize(r.get("content_text", "")))
    n_empty_reasoning = sum(1 for r in ok_recs if not tokenize(r.get("reasoning_text", "")))
    n_truncated = sum(1 for r in ok_recs if r.get("truncated") is True)
    n_finish_stop = sum(1 for r in ok_recs if r.get("finish_reason") == "stop")
    n_reasoning_present = sum(1 for r in ok_recs if r.get("reasoning_len", 0) > 0)

    # 自证项 2: pairs/教师 可达性 (构造上限 C(6,2)=15)
    per_cell_teacher_n = {}
    for r in ok_recs:
        per_cell_teacher_n[(r["cell_idx"], r["teacher"])] = \
            per_cell_teacher_n.get((r["cell_idx"], r["teacher"]), 0) + 1
    nrec_vals = sorted(per_cell_teacher_n.values())
    pairs_ctor = 15

    calib_results = {}
    for caliber in ("full_reply", "content_only", "reasoning_only"):
        jmap = compute_j(caliber, ok_recs)
        cells_out = []
        for ci, (dim, temp) in enumerate(CELLS):
            per_teacher = []
            for t in TEACHER_NAMES:
                d = jmap.get(f"{ci}|{t}")
                if not d:
                    continue
                per_teacher.append({
                    "teacher": t, "n_records": d["n_records"],
                    "n_pairs_all": d["n_pairs_all"],
                    "n_pairs_nonempty": d["n_pairs_nonempty"],
                    "n_pairs_empty_empty": d["n_pairs_empty_empty"],
                    "j_median_all": (round(d["j_median_all"], 6)
                                      if d["j_median_all"] is not None else None),
                    "j_median_nonempty": (round(d["j_median_nonempty"], 6)
                                          if d["j_median_nonempty"] is not None else None),
                    "j_median_same_caption": (round(d["j_median_same_caption"], 6)
                                              if d["j_median_same_caption"] is not None else None),
                    "j_median_cross_caption": (round(d["j_median_cross_caption"], 6)
                                               if d["j_median_cross_caption"] is not None else None),
                    "n_ge_0_85": d["n_ge_0_85"],
                })
            allm = [x["j_median_all"] for x in per_teacher if x["j_median_all"] is not None]
            cells_out.append({
                "cell_idx": ci, "dim": dim, "temperature": temp,
                "n_teachers_with_data": len(allm),
                "cell_j_median": (round(float(statistics.median(allm)), 6)
                                  if allm else None),
                "cell_j_min": (round(min(allm), 6) if allm else None),
                "cell_j_max": (round(max(allm), 6) if allm else None),
                "n_teachers_ge_0_85": sum(1 for x in allm if x >= K_N11_3_THRESHOLD),
                "per_teacher": per_teacher,
            })
        calib_results[caliber] = {
            "cells": cells_out,
            "axis_divergence": axis_divergence(caliber, ok_recs),
        }

    usage_completion = [ (r.get("usage", {}) or {}).get("completion_tokens")
                         for r in ok_recs ]
    usage_completion = [x for x in usage_completion if isinstance(x, int)]
    usage_reasoning = []
    for r in ok_recs:
        det = ((r.get("usage", {}) or {}).get("completion_tokens_details", {}) or {})
        v = det.get("reasoning_tokens")
        if isinstance(v, int):
            usage_reasoning.append(v)
    full_lens = sorted(r.get("full_reply_len", 0) for r in ok_recs)
    content_lens = sorted(r.get("content_len", 0) for r in ok_recs)

    # 失败 tuple 之补跑归属: 由 tuple 集合实算 (⛔ 不依赖 is_rerun_of_failed 标志)
    ok_tuples = {(r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"],
                  r["temperature"]) for r in ok_recs}
    superseded_tuples = sorted(
        (r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"])
        for r in fail_recs
        if (r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"],
            r["temperature"]) in ok_tuples)

    failed_tuples = [{
        "cell_idx": r["cell_idx"], "dim": r["dim"], "temperature": r["temperature"],
        "teacher": r["teacher"], "caption_id": r["caption_id"],
        "reask_idx": r["reask_idx"], "error_category": r.get("error_category"),
        "status_code": r.get("status_code"), "latency_ms": r.get("latency_ms"),
        "superseded_by_rerun": (r["cell_idx"], r["teacher"], r["caption_id"],
                                r["reask_idx"], r["temperature"]) in ok_tuples,
    } for r in fail_recs]

    result = {
        "metadata": {
            "schema": "t1_r2_qwen_temp_sweep_result.v1",
            "task": "T1 探针 · qwen 温度扫描 · r2 棒 (re-asks 2->3 + 响应提取面并修)",
            "date_label": "2026_10_09",
            "generated_local": now_local(),
            "author": "worker (r2 棒); 判定归 verdict-keeper 新件",
            "line_ending": "LF",
            "encoding": "UTF-8 no BOM",
            "algorithm": "SHA-256 (前 12 位)",
            "authorization": {
                "pi_card": "ask_52effb1125dc64e6dac3295f (2026-10-09)",
                "main_decision": "乙 — 补构造至 >=10 对 (re-asks 2->3, ~+60 calls; T15r2 先例)",
                "annex": "并修响应提取面 + 授权起跑",
                "upstream_proposal": "24DA21074CC2 §2.2 乙档",
                "upstream_verdict": "DFC858D3D930 §2.3/§4.2/§7.1",
            },
            "zero_derivation_merge": "⛔ 0 合并派生 JSON; ⛔ 0 覆写 r1 任一件; ⛔ 0 触 frozen (R5)",
            "no_judgment": "本件只出读数与自证实测; ⛔ 0 判读 (无任何 PASS/FAIL/达标宣告)",
        },
        "constraint": {
            "no_key_on_disk": True,
            "key_source": "C:/Users/Administrator/Desktop/AI/LLM API.txt (slot 23)",
            "key_value_in_artifacts": False,
            "inter_call_sleep_s": INTER_CALL_SERIAL_S,
            "watchdog_s": WATCHDOG_S,
            "call_timeout_s": CALL_TIMEOUT_S,
            "endpoint_construction_fix": "响应提取面并修 (DFC858D3D930 §4.2 第 1 项字面)",
            "n_reasks_expansion": "2 -> 3 (乙档样本量面修正)",
            "route": "全量 180 calls (0 承接 r1 120; 依据见 inputs.route_decision)",
            "intermediate_products": "仅 .tmp/ (checkpoint/selfcert/probe)",
        },
        "inputs": {
            "input_gates": verify_input_gates(),
            "captions": {"path": str(CAPTIONS_PATH),
                         "sha12": sha12_file(CAPTIONS_PATH),
                         "expected": CAPTIONS_SHA12_EXPECTED},
            "r1_records_state_anchor": {
                "path": str(TMP_DIR / "_t1_qwen_temp_sweep_records.json"),
                "sha12": (sha12_file(TMP_DIR / "_t1_qwen_temp_sweep_records.json")
                          if (TMP_DIR / "_t1_qwen_temp_sweep_records.json").exists() else None),
                "n_records": 120,
                "contains_reasoning_content": False,
                "reuse_decision": "⛔ 不可复用为已修提取面之度量对象 (0 reasoning_content 字段) => 全量重跑",
            },
            "calibration_max_tokens": {
                "path": str(CALIB_PATH),
                "sha12": (sha12_file(CALIB_PATH) if CALIB_PATH.exists() else None),
            },
        },
        "experiment_parameters": {
            "dimensions": ["L2", "L14"],
            "temperatures": TEMPERATURES,
            "endpoints": [{"label": "qwen_plan",
                           "endpoint": ENDPOINTS["qwen_plan"]["endpoint"],
                           "model_id": ENDPOINTS["qwen_plan"]["model_id"]}],
            "n_teachers": len(TEACHER_NAMES),
            "n_prompts_per_cell": 2,
            "n_reasks_per_prompt": N_REASKS,
            "records_per_teacher_per_cell": 2 * N_REASKS,
            "pairs_ctor_per_teacher_per_cell": pairs_ctor,
            "calls_per_cell": len(TEACHER_NAMES) * 2 * N_REASKS,
            "total_calls_planned": len(CELLS) * len(TEACHER_NAMES) * 2 * N_REASKS,
            "max_tokens": MAX_TOKENS,
            "max_tokens_basis": "实测保留 r1 原值 500: 校准 3 档 finish_reason 6/6 = stop (0 截段), usage.completion_tokens 705..4926 ≫ 请求值 => 端点 0 以 max_tokens 约束 reasoning; 上调 2000/4000 实测 content_len 恒 1..3 且抬高 latency (2000 档 completion 4926 / 75.6s)",
            "measurement_object": "完整教师回复 (message.reasoning_content + message.content); ⛔ 0 只取 content; ⛔ 0 截段",
            "L2_prompts": L2_PROMPTS,
            "L14_prompts": L14_PROMPTS,
            "teachers": TEACHER_NAMES,
            "seed": SEED,
            "thresholds_reference_only": {
                "TH_T1_N_MIN": TH_T1_N_MIN,
                "K_N11_3_THRESHOLD": K_N11_3_THRESHOLD,
                "note": "仅引用; 本棒 0 判读 0 宣告达标",
            },
            "jaccard_formula": "len(A∩B)/len(A∪B), A/B = set(re.findall(r'[a-z0-9]+|[\\u4e00-\\u9fff]', text.lower()))",
            "readout_calibers": ["full_reply (本棒度量对象)", "content_only (r1 可比)", "reasoning_only"],
        },
        "probe": {
            "rationale": "即用即探 (1 call, 计入账)",
            "log": ({"path": str(PROBE_LOG_PATH),
                     "sha12": (sha12_file(PROBE_LOG_PATH) if PROBE_LOG_PATH.exists() else None)}),
        },
        "records_summary": {
            "n_records_total": len(records),
            "n_records_ok": len(ok_recs),
            "n_records_failed": len(fail_recs),
            "n_calls_total": len(records),
            "n_calls_ok": len(ok_recs),
            "n_calls_failed": len(fail_recs),
            "n_rerun_of_failed": len(superseded_tuples),
            "superseded_failed_tuples": superseded_tuples,
            "n_finish_reason_stop": n_finish_stop,
            "n_truncated": n_truncated,
            "n_reasoning_present": n_reasoning_present,
            "usage_completion_tokens": {
                "min": (min(usage_completion) if usage_completion else None),
                "median": (float(statistics.median(usage_completion)) if usage_completion else None),
                "max": (max(usage_completion) if usage_completion else None),
                "n": len(usage_completion),
            },
            "usage_reasoning_tokens": {
                "min": (min(usage_reasoning) if usage_reasoning else None),
                "median": (float(statistics.median(usage_reasoning)) if usage_reasoning else None),
                "max": (max(usage_reasoning) if usage_reasoning else None),
                "n": len(usage_reasoning),
            },
            "failed_tuples": failed_tuples,
        },
        "self_certification": {
            "signal_1_empty_response": {
                "empty_rate_full_reply": (round(n_empty_full / len(ok_recs), 6) if ok_recs else None),
                "n_empty_full_reply": n_empty_full,
                "empty_rate_content_only": (round(n_empty_content / len(ok_recs), 6) if ok_recs else None),
                "n_empty_content_only": n_empty_content,
                "n_empty_reasoning_only": n_empty_reasoning,
                "note": "度量对象之空响应率 (full_reply) 为主; content_only 一并登记供 r1 可比",
            },
            "signal_2_pairs_reachability": {
                "records_per_teacher_per_cell": {"min": (min(nrec_vals) if nrec_vals else None),
                                                 "max": (max(nrec_vals) if nrec_vals else None),
                                                 "n_groups": len(nrec_vals)},
                "pairs_ctor_C6_2": pairs_ctor,
                "TH_T1_N_MIN": TH_T1_N_MIN,
                "pairs_ctor_vs_N_min": "ctor 15 >= N_min 10 (算式事实; ⛔ 0 判读 0 宣告达标)",
                "achieved_pairs_per_teacher_min": (min(nrec_vals) * (min(nrec_vals) - 1) // 2
                                                   if nrec_vals else None),
                "achieved_pairs_per_teacher_max": (max(nrec_vals) * (max(nrec_vals) - 1) // 2
                                                   if nrec_vals else None),
            },
            "signal_3_text_lengths": {
                "full_reply_char_len": {"min": (min(full_lens) if full_lens else None),
                                        "median": (float(statistics.median(full_lens)) if full_lens else None),
                                        "max": (max(full_lens) if full_lens else None)},
                "content_only_char_len": {"min": (min(content_lens) if content_lens else None),
                                          "median": (float(statistics.median(content_lens)) if content_lens else None),
                                          "max": (max(content_lens) if content_lens else None)},
                "r1_comparison": "r1 度量对象 (content_only) 实测 min 1 / 中位 2 / max 9 字符",
            },
            "signal_4_truncation_face": {
                "n_finish_reason_stop": n_finish_stop,
                "n_truncated": n_truncated,
                "truncated_rate": (round(n_truncated / len(ok_recs), 6) if ok_recs else None),
                "note": "finish_reason = length 之截段计数; ⛔ 本棒 0 预设通过",
            },
            "signal_5_axis_divergence": {
                "note": "温度轴有效性面 (t=0.3/0.5 对 t=0.0 同 teacher 同 caption 文本全同); "
                        "非本棒擅改范围, 逐档实测登记",
                "by_caliber": {k: v["axis_divergence"] for k, v in calib_results.items()},
            },
            "signal_6_distinct_texts": {
                caliber: {
                    "n_distinct": len({r.get(k2, "") for r in ok_recs}),
                    "n_records": len(ok_recs),
                }
                for caliber, k2 in (("full_reply", "full_reply_text"),
                                    ("content_only", "content_text"),
                                    ("reasoning_only", "reasoning_text"))
            },
        },
        "readings": calib_results,
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj(records)],
            "status": "clean" if not self_scan_obj(records) else "WARN",
        },
        "honesty_disclosures": {
            "zero_judgment": "本件 ⛔ 0 判读: 无 K-T1-S1/S3 裁定、无 PASS/FAIL、无达标宣告; 判定归 verdict-keeper 新件",
            "succeeded_not_means_completed": "HTTP 200 / 0 空响应 ⛔ 不等于读数有效 (沿 DFC858D3D930 §7.1)",
            "route_literal": "全量 180 calls; ⛔ 0 承接 r1 120 (r1 records 0 reasoning_content 字段)",
            "max_tokens_literal": "保留 500 (实测 3 档均 finish_reason=stop, 端点 0 以 max_tokens 约束 reasoning)",
            "caliber_literal": "full_reply 为本棒度量对象; content_only / reasoning_only 一并登记供下游择读 (0 替下游择定)",
            "temperature_axis_untouched": "温度轴有效性面 ⛔ 本棒 0 擅改, 仅实测登记",
            "no_key_leak": "key 0 落盘 0 明文 0 回显; 本件仅存 slot 存在性/长度/形态类别",
            "no_derivation_merge": "⛔ 0 合并派生 JSON; ⛔ 0 覆写 r1 任一件",
            "partial_or_failed_calls": "失败/重试逐条登记于 records_summary.failed_tuples",
        },
    }

    hits = self_scan_obj(result)
    result["key_shape_self_scan"] = {
        "hits": [{"name": n, "count": c} for n, c in hits],
        "status": "clean" if not hits else "WARN",
    }

    if RESULT_PATH.exists():
        alt = RESULTS_DIR / "_t1_qwen_temp_sweep_r2_result_b_2026_10_09.json"
        print(f"FATAL: result 目标名已存在 -> 0 覆写; 请改用: {alt}")
        sys.exit(2)

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                           encoding="utf-8", newline="\n")
    print(f"result written: {RESULT_PATH}")
    print(f"sha12={sha12_file(RESULT_PATH)} bytes={RESULT_PATH.stat().st_size}")
    rs = result["records_summary"]
    print(f"records ok={rs['n_records_ok']} fail={rs['n_records_failed']} "
          f"truncated={rs['n_truncated']} reasoning_present={rs['n_reasoning_present']}")
    sc = result["self_certification"]
    print(f"empty_rate(full_reply)={sc['signal_1_empty_response']['empty_rate_full_reply']}")
    print(f"records/teacher/cell min={sc['signal_2_pairs_reachability']['records_per_teacher_per_cell']['min']}")
    for caliber, v in calib_results.items():
        print(f"\n[{caliber}] axis divergence:")
        for row in v["axis_divergence"]["per_temp"]:
            print(f"  cell {row['cell_idx']} ({row['dim']}/t={row['temperature']}): "
                  f"identical {row['n_identical']}/{row['n_compared']} "
                  f"= {row['identical_rate']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selfcert")
    sub.add_parser("probe")
    p_run = sub.add_parser("run")
    p_run.add_argument("start", type=int)
    p_run.add_argument("end", type=int)
    p_run.add_argument("--calls-limit", type=int, default=0)
    p_retry = sub.add_parser("retry")
    p_retry.add_argument("start", type=int)
    p_retry.add_argument("end", type=int)
    sub.add_parser("aggregate")
    a = ap.parse_args()
    if a.cmd == "selfcert":
        cmd_selfcert()
    elif a.cmd == "probe":
        cmd_probe()
    elif a.cmd == "run":
        cmd_run(a.start, a.end, a.calls_limit, retry_failed=False)
    elif a.cmd == "retry":
        cmd_run(a.start, a.end, 0, retry_failed=True)
    elif a.cmd == "aggregate":
        cmd_aggregate()


if __name__ == "__main__":
    main()