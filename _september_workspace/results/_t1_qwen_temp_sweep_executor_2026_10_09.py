# -*- coding: utf-8 -*-
"""
_t1_qwen_temp_sweep_executor_2026_10_09.py
===========================================
T1-r1 qwen 温度扫描 executor: {L2, L14} × {temp 0.0, 0.3, 0.5} × qwen 单端点 = 6 cells
=========================================================================================

【授权与对位】
=========================================================================================
- PI 2026-10-09 卷⑧ Q3 甲: 全案采认 = 修订件生效即锁 + K-T1-S2 登记不适用 + **授权起跑**
- 修订件: `results/_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md` SHA-12 `BDA5D5F3DFA0` (0 回改)
- 锚件:   `results/_v4_supp_prereg_v02_add_T1_2026_09_24.md` SHA-12 `802DECE2286A` (0 回改)
- 下游:   `results/_v4_supp_t1_verdict.md` SHA-12 `0AD42625F333` (0 回改)
- 修订件 R-1 端点轴 0 保留 / R-4 6 cells + t=0.7 baseline 对照锚 (不重跑) / R-7 阈值一字沿用
- 修订件 §3.1 K-T1-R1-1 防退化门禁: 开跑前构造面自证表须落盘 (本 executor `selfcert` 子命令)

【端点 (沿 T15 executor `558E635F9BA6` 已跑通的 qwen 单端点体例 + endpoints probe `C846F7FC79EE`)】
=========================================================================================
- endpoint: https://token-plan.maas.qianwenaiapi.com/compatible-mode/v1
- model_id: qwen3.7-max (非 reasoning; 沿 T15 C-T15-1 构造修正)
- key_index_1based = 23 (沿 T15 executor 体例; key 仅 runtime 读入内存, 0 落盘, 0 明文)
- use_proxy = False (qwen_plan 无代理, 沿 Track 2 ROUTE_TEMPLATES[0] qwen 行)
- max_tokens = 500 (沿 T15 C-T15-1 工具失灵族参数修正; 非阈值, 0 新设数值阈值)

【沿用字面 (0 新设 0 调整)】
=========================================================================================
- K_N11_3_THRESHOLD = 0.85 / K_N11_1_DIFF = 0.05 / K_N11_2_DELTA = 0.05 (沿 0A9EE16267B5)
- TH17_N_TARGET = 20 / TH_T1_N_MIN = 10 (两层并存, 沿锚件 §1.5.1)
- 5 教师: kimi / GLM_1 / GLM_2 / coze / minimax (沿 TH-14)
- L2 prompts: L_biological_taxonomy + S5; L14 prompts: L_geography_world + L_historical_causality
- Jaccard: token-level set J, token regex `[a-z0-9]+|[\u4e00-\u9fff]`, text.lower() (沿 L2/L14 verdict §3.2)
- 串行间隔 >= 2.5s / 看门狗 600s / 单批 <= 30 calls (沿锚件 §1.6.1)

【铁律】
=========================================================================================
- R4 key 永不明文 (无例外): 0 落盘 / 0 打印 / 0 回显长度以外信息; 本件 0 内嵌任何 key
- R5 V4 frozen 只追加: 0 动既有件; 派生 checkpoint/JSON 以本棒 prefix 分列, 0 合并
- 0 新设数值阈值 (0.85/0.05/20/10 逐字沿用)
- 0 出判定 (K-T1-S1/S3 判定归 verdict-keeper; 本件只出读数)
- 0 回改修订件/锚件/verdict 三件

【用法】
=========================================================================================
  python _t1_qwen_temp_sweep_executor_2026_10_09.py selfcert    # 防退化构造面自证表 (K-T1-R1-1 开跑前)
  python _t1_qwen_temp_sweep_executor_2026_10_09.py probe        # 即用即探 (1 call)
  python _t1_qwen_temp_sweep_executor_2026_10_09.py run <s> <e>  # 跑 cells [s,e] (含)
  python _t1_qwen_temp_sweep_executor_2026_10_09.py aggregate    # 聚合读数 JSON

【cells 索引】
=========================================================================================
  0: L2  / temp 0.0     1: L2  / temp 0.3     2: L2  / temp 0.5
  3: L14 / temp 0.0     4: L14 / temp 0.3     5: L14 / temp 0.5
"""

from __future__ import annotations

import argparse
import hashlib
import json
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

CHECKPOINT_PATH = TMP_DIR / "_t1_qwen_temp_sweep_records.json"
SELFCERT_PATH = TMP_DIR / "_t1_qwen_temp_sweep_selfcert.json"
PROBE_LOG_PATH = TMP_DIR / "_t1_qwen_temp_sweep_probe_log.json"
READINGS_PATH = TMP_DIR / "_t1_qwen_temp_sweep_readings.json"

KEY_SOURCE_PATH = Path("C:/Users/Administrator/Desktop/AI/LLM API.txt")
CAPTIONS_PATH = ROOT / "corpus/v20_caption_surface/strip_captions_22.json"
CAPTIONS_SHA12_EXPECTED = "6A2656878745"

REVISION_PATH = RESULTS_DIR / "_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md"
REVISION_SHA12_EXPECTED = "BDA5D5F3DFA0"
ANCHOR_PATH = RESULTS_DIR / "_v4_supp_prereg_v02_add_T1_2026_09_24.md"
ANCHOR_SHA12_EXPECTED = "802DECE2286A"

# ============================================================
# 阈值 (沿用, 0 新设)
# ============================================================
K_N11_3_THRESHOLD = 0.85
K_N11_1_DIFF = 0.05
K_N11_2_DELTA = 0.05
TH17_N_TARGET = 20
TH_T1_N_MIN = 10
INTER_CALL_SERIAL_S = 2.5
WATCHDOG_S = 600
BATCH_CALL_LIMIT = 30

# ============================================================
# 5 教师 (沿 TH-14)
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
N_REASKS = 2

# ============================================================
# 端点 (qwen 单端点, 沿 T15 executor 体例)
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

MAX_TOKENS = 500  # 沿 T15 C-T15-1 工具失灵族参数修正 (非阈值)

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


# ============================================================
# SHA / 字节
# ============================================================
def sha12_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()[:12]


def sha12_file(path: Path) -> str:
    return sha12_bytes(path.read_bytes())


# ============================================================
# Key 加载 (runtime 读入内存, 0 落盘, 0 明文)
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


def unset_proxy() -> None:
    for k in ("https_proxy", "http_proxy", "all_proxy"):
        __import__("os").environ.pop(k, None)


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


def call_chat(api_key: str, endpoint: str, model: str,
              messages: List[Dict[str, str]], temperature: float,
              max_tokens: int, timeout: int = 90,
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
        content = ""
        if data.get("choices"):
            content = data["choices"][0]["message"].get("content") or ""
        return {"ok": True, "status_code": r.status_code, "latency_ms": latency_ms,
                "model_returned": data.get("model", ""), "id": data.get("id", ""),
                "content": content, "usage": data.get("usage", {})}
    except _requests.exceptions.Timeout as e:
        return {"ok": False, "error_category": "timeout",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}
    except Exception as e:
        return {"ok": False, "error_category": "other",
                "latency_ms": round((time.time() - t0) * 1000, 1),
                "error_snippet": str(e)[:200]}


# ============================================================
# Jaccard (沿 L2/L14 verdict §3.2 字面)
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
# Captions
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
# K-T1-R1-1 防退化构造面自证 (开跑前落盘)
# ============================================================
def cmd_selfcert() -> None:
    """构造面自证: 每个输入字段 n_distinct / min / max / std + 退化信号预检 + t=0.7 并置."""
    print("=== K-T1-R1-1 构造面自证 (开跑前) ===")
    captions = load_captions()
    by_id = {c["id"]: c for c in captions}

    used_ids = L2_PROMPTS + L14_PROMPTS
    texts = [by_id[i]["text"] for i in used_ids]
    tok_counts = [len(tokenize(t)) for t in texts]
    char_counts = [len(t) for t in texts]

    # 输入字段 n_distinct 统计
    def stats(vals: List[Any]) -> Dict[str, Any]:
        n = len(vals)
        nd = len(set(vals))
        if all(isinstance(v, (int, float)) for v in vals) and n > 0:
            mean = statistics.fmean(vals)
            std = statistics.pstdev(vals) if n > 1 else 0.0
            return {"n": n, "n_distinct": nd, "min": min(vals), "max": max(vals),
                    "mean": round(mean, 6), "std": round(std, 6)}
        return {"n": n, "n_distinct": nd,
                "min": "n/a(str)", "max": "n/a(str)", "mean": "n/a", "std": "n/a"}

    # t=0.7 对照锚 (既有 baseline, 不重跑; 显式并置核)
    t07_baseline = {
        "source": "L2 verdict E433A06E7BFB §3.2 + L14 verdict 764F24A21AC8 §3.2",
        "temperature": 0.7,
        "endpoint": "qwen_plan / qwen3.7-max",
        "L2_j_median_range": [0.41, 0.52],
        "L14_j_median_range": [0.36, 0.39],
        "K_N11_3_THRESHOLD": K_N11_3_THRESHOLD,
        "rerun": False,
        "note": "对照锚不重跑 (沿修订件 R-4); 0 以『矩阵内一致』代替『与 baseline 并置』",
    }

    report = {
        "task": "t1_r1_qwen_temp_sweep_selfcert",
        "generated_local": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "revision_sha12": sha12_file(REVISION_PATH),
        "revision_sha12_expected": REVISION_SHA12_EXPECTED,
        "anchor_sha12": sha12_file(ANCHOR_PATH),
        "anchor_sha12_expected": ANCHOR_SHA12_EXPECTED,
        "captions_sha12": sha12_file(CAPTIONS_PATH),
        "captions_sha12_expected": CAPTIONS_SHA12_EXPECTED,
        "matrix": {
            "n_cells": len(CELLS),
            "cells": [{"cell_idx": i, "dim": d, "temperature": t} for i, (d, t) in enumerate(CELLS)],
            "endpoint": ENDPOINTS["qwen_plan"]["endpoint"],
            "model_id": ENDPOINTS["qwen_plan"]["model_id"],
            "max_tokens": MAX_TOKENS,
            "n_teachers": len(TEACHER_NAMES),
            "n_reasks": N_REASKS,
            "calls_per_cell": len(TEACHER_NAMES) * 2 * N_REASKS,
            "total_calls": len(CELLS) * len(TEACHER_NAMES) * 2 * N_REASKS,
        },
        "input_field_stats": {
            "caption_ids_used": stats(used_ids),
            "caption_text_char_len": stats(char_counts),
            "caption_text_token_len": stats(tok_counts),
            "temperature": stats(TEMPERATURES),
            "teacher_names": stats(TEACHER_NAMES),
            "reask_idx": stats(list(range(N_REASKS))),
        },
        "degenerate_signal_precheck": {
            "signal_1_empty_response_dominance": "跑后实测 n_empty_responses/n_calls_ok (0 预判; max_tokens=500 + qwen3.7-max 非 reasoning 沿 T15 C-T15-1 已验证 n_empty=0)",
            "signal_2_nonempty_pairs_too_thin": "跑后实测 per teacher n_pairs (≥ TH_T1_N_MIN=10 为门槛)",
            "signal_3_jmedian_always_zero": "跑后实测 per cell per teacher J 中位 (nonempty 子口径并报)",
            "signal_4_monotone_tautology": "温度轴 3 点 {0.0,0.3,0.5} 逐点实测, 0 单调预设; 判定布尔显式 (hit=True/pass=True)",
            "input_field_n_distinct_le_3": "见 input_field_stats; 任一 ≤3 即退化警报 -> 改构造或判不明",
        },
        "t07_baseline_juxtaposition": t07_baseline,
        "kill_line_literal": {
            "K_T1_S1": "任一 (维度,温度) cell 教师 J 中位 >= 0.85 -> hit=True (判定归 verdict-keeper)",
            "K_T1_S3": "6 cells 全 J 中位 < 0.85 -> 判定稳健 (须附本自证表)",
            "K_T1_S2": "本修订面 0 适用 (端点轴 0 保留, 沿修订件 R-6; 登记不适用, 0 删除 0 改写)",
            "K_T1_R1_1": "本表未落盘 或 任一输入字段 n_distinct <=3 未改构造 -> 禁止开跑",
        },
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj({"t07": t07_baseline})],
            "status": "clean",
        },
        "key_reading_note": "key 仅 runtime 读入内存用于调用; 0 落盘 0 明文 0 回显 (R4). 本表 0 含 key 值.",
    }

    hits = self_scan_obj(report)
    report["key_shape_self_scan"] = {
        "hits": [{"name": n, "count": c} for n, c in hits],
        "status": "clean" if not hits else "WARN",
    }

    TMP_DIR.mkdir(parents=True, exist_ok=True)
    SELFCERT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                             encoding="utf-8", newline="\n")
    print(f"selfcert written: {SELFCERT_PATH}")
    print(json.dumps(report["input_field_stats"], ensure_ascii=False, indent=2))
    print(f"t=0.7 baseline juxtaposed: {t07_baseline['L2_j_median_range']} (L2) / "
          f"{t07_baseline['L14_j_median_range']} (L14)")
    print(f"key self-scan: {report['key_shape_self_scan']['status']}")


# ============================================================
# Checkpoint
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


# ============================================================
# Probe
# ============================================================
def cmd_probe() -> None:
    print("=== 即用即探: qwen_plan (1 call) ===")
    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])
    r = call_chat(api_key, ep["endpoint"], ep["model_id"],
                  messages=[{"role": "user", "content": "ping"}],
                  temperature=0.0, max_tokens=10, timeout=30,
                  use_proxy=ep["use_proxy"])
    out = {
        "endpoint_label": ep["label"],
        "endpoint": ep["endpoint"],
        "model_id": ep["model_id"],
        "ok": bool(r.get("ok")),
        "status_code": r.get("status_code"),
        "error_category": r.get("error_category"),
        "latency_ms": r.get("latency_ms"),
        "model_returned": r.get("model_returned", ""),
        "error_body_snippet": r.get("error_body_snippet", "")[:200],
        "error_snippet": r.get("error_snippet", "")[:200],
        "key_shape_self_scan": {"hits": [{"name": n, "count": c} for n, c in self_scan_obj(r)],
                                "status": "clean" if not self_scan_obj(r) else "WARN"},
        "note": "key 0 落盘 0 明文 (R4); 本条 0 含 key 值",
    }
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    PROBE_LOG_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                              encoding="utf-8", newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"probe log: {PROBE_LOG_PATH}")


# ============================================================
# 单 cell runner
# ============================================================
def run_cell(cell_idx: int, dim: str, temp: float,
             captions: List[Dict[str, Any]], records: List[Dict[str, Any]],
             wall_start: float, max_calls_in_cell: int = 0) -> Dict[str, Any]:
    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])

    prompts_ids = L2_PROMPTS if dim == "L2" else L14_PROMPTS
    prompts_list = select_prompts(captions, prompts_ids)

    existing = set((r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"])
                   for r in records if r.get("cell_idx") == cell_idx)

    summary = {"cell_idx": cell_idx, "dim": dim, "temperature": temp,
               "endpoint_label": ep["label"], "endpoint": ep["endpoint"],
               "model_id": ep["model_id"], "max_tokens": MAX_TOKENS,
               "prompts": prompts_ids, "n_calls_planned": len(TEACHER_NAMES) * len(prompts_list) * N_REASKS,
               "n_calls_ok": 0, "n_calls_failed": 0}

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
                            {"role": "user", "content": build_user_prompt(teacher_name, caption_id, caption_text)}]
                t0 = time.time()
                resp = call_chat(api_key, ep["endpoint"], ep["model_id"], messages,
                                 temperature=temp, max_tokens=MAX_TOKENS, timeout=90,
                                 use_proxy=ep["use_proxy"])
                elapsed = time.time() - t0
                ok = bool(resp.get("ok"))
                content = resp.get("content", "") if ok else ""
                rec = {
                    "cell_idx": cell_idx, "endpoint_label": ep["label"],
                    "endpoint": ep["endpoint"], "endpoint_model": ep["model_id"],
                    "use_proxy": ep["use_proxy"], "dim": dim, "temperature": temp,
                    "max_tokens": MAX_TOKENS, "teacher": teacher_name,
                    "teacher_path_rel": teacher_path_rel, "caption_id": caption_id,
                    "caption_text_sha12": sha12_bytes(caption_text.encode("utf-8")),
                    "reask_idx": ri, "ok": ok, "response_text": content,
                    "response_text_sha12": sha12_bytes(content.encode("utf-8")) if ok else "",
                    "response_text_len": len(content) if ok else 0,
                    "latency_ms": round(elapsed * 1000, 1),
                    "status_code": resp.get("status_code"),
                    "error_category": resp.get("error_category"),
                    "model_returned": resp.get("model_returned", ""),
                    "usage": resp.get("usage", {}),
                    "timestamp_local": datetime.now(timezone(timedelta(hours=8))).isoformat(),
                }
                records.append(rec)
                n_new += 1
                save_checkpoint(records)
                if ok:
                    summary["n_calls_ok"] += 1
                    print(f"  [{cell_idx}] {teacher_name}/{caption_id}/r{ri} ok "
                          f"({rec['latency_ms']:.0f}ms, len={rec['response_text_len']})")
                else:
                    summary["n_calls_failed"] += 1
                    print(f"  [{cell_idx}] {teacher_name}/{caption_id}/r{ri} FAIL "
                          f"{rec['error_category']}")
    return summary


def cmd_run(start_idx: int, end_idx: int, calls_limit: int = 0) -> None:
    print(f"=== T1-r1 qwen 温扫 run cells [{start_idx},{end_idx}] (calls_limit={calls_limit}) ===")
    TMP_DIR.mkdir(parents=True, exist_ok=True)

    # K-T1-R1-1 门禁: 自证表未落盘 -> 禁止开跑
    if not SELFCERT_PATH.exists():
        print("FATAL: K-T1-R1-1 selfcert table not found -> 禁止开跑. Run `selfcert` first.")
        sys.exit(1)

    captions_sha = sha12_file(CAPTIONS_PATH)
    if captions_sha.upper() != CAPTIONS_SHA12_EXPECTED.upper():
        print(f"FATAL: captions SHA-12 mismatch: {captions_sha}")
        sys.exit(1)

    rev_sha = sha12_file(REVISION_PATH)
    if rev_sha.upper() != REVISION_SHA12_EXPECTED.upper():
        print(f"FATAL: revision SHA-12 mismatch: {rev_sha}")
        sys.exit(1)

    captions = load_captions()
    records = load_checkpoint()
    print(f"captions SHA-12 OK ({captions_sha}); revision SHA-12 OK ({rev_sha})")
    print(f"loaded {len(records)} existing records from checkpoint")

    wall_start = time.time()
    summaries = []
    calls_made = 0
    for idx in range(start_idx, end_idx + 1):
        if idx < 0 or idx >= len(CELLS):
            continue
        dim, temp = CELLS[idx]
        print(f"\n--- cell {idx}: {dim} / temp={temp} / qwen_plan ---")
        if time.time() - wall_start > WATCHDOG_S:
            print("  [watchdog] stopping batch")
            break
        if calls_limit > 0 and calls_made >= calls_limit:
            print("  [calls_limit] stopping batch")
            break
        s = run_cell(idx, dim, temp, captions, records, wall_start,
                     max_calls_in_cell=calls_limit - calls_made if calls_limit > 0 else 0)
        summaries.append(s)
        calls_made += s["n_calls_ok"] + s["n_calls_failed"]
        if s.get("watchdog_break"):
            break

    save_checkpoint(records)
    wall = time.time() - wall_start
    print(f"\n=== batch done: wall={wall:.1f}s new_calls={calls_made} total_records={len(records)} ===")
    for s in summaries:
        print(f"  cell {s['cell_idx']} ({s['dim']}/t={s['temperature']}): "
              f"ok={s['n_calls_ok']} fail={s['n_calls_failed']} "
              f"wd={s.get('watchdog_break', False)}")


# ============================================================
# Aggregate: 读数 (0 判定)
# ============================================================
def cmd_aggregate() -> None:
    print("=== aggregate: 读数 (判定归 verdict-keeper) ===")
    records = load_checkpoint()
    if not records:
        print("FATAL: no records")
        sys.exit(1)

    ok_recs = [r for r in records if r.get("ok")]
    n_empty = sum(1 for r in ok_recs if not tokenize(r.get("response_text", "")))

    by_cell_teacher: Dict[Tuple[int, str], List[Dict[str, Any]]] = {}
    for r in ok_recs:
        by_cell_teacher.setdefault((r["cell_idx"], r["teacher"]), []).append(r)

    per_cell_teacher_j: Dict[Tuple[int, str], Dict[str, Any]] = {}
    for k, recs in by_cell_teacher.items():
        n = len(recs)
        jvs_all, jvs_nonempty, n_ee = [], [], 0
        for i in range(n):
            for j in range(i + 1, n):
                ti, tj = recs[i]["response_text"], recs[j]["response_text"]
                jv = jaccard(ti, tj)
                jvs_all.append(jv)
                if tokenize(ti) and tokenize(tj):
                    jvs_nonempty.append(jv)
                else:
                    n_ee += 1
        per_cell_teacher_j[k] = {
            "cell_idx": k[0], "teacher": k[1], "n_records": n,
            "n_pairs_all": len(jvs_all), "n_pairs_nonempty": len(jvs_nonempty),
            "n_pairs_empty_empty": n_ee,
            "j_median_all": (float(statistics.median(jvs_all)) if jvs_all else None),
            "j_median_nonempty": (float(statistics.median(jvs_nonempty)) if jvs_nonempty else None),
            "j_values_all": [round(v, 6) for v in jvs_all],
        }

    cells_out = []
    for cell_idx, (dim, temp) in enumerate(CELLS):
        per_teacher = []
        for t in TEACHER_NAMES:
            d = per_cell_teacher_j.get((cell_idx, t))
            jm = d["j_median_all"] if d else None
            jn = d["j_median_nonempty"] if d else None
            per_teacher.append({
                "teacher": t,
                "j_median": (round(jm, 6) if jm is not None else None),
                "j_median_nonempty": (round(jn, 6) if jn is not None else None),
                "n_records": (d["n_records"] if d else 0),
                "n_pairs_all": (d["n_pairs_all"] if d else 0),
                "n_pairs_nonempty": (d["n_pairs_nonempty"] if d else 0),
                "n_pairs_empty_empty": (d["n_pairs_empty_empty"] if d else 0),
                "n_ge_0_85": (bool(jm >= K_N11_3_THRESHOLD) if jm is not None else None),
            })
        valid = [x["j_median"] for x in per_teacher if x["j_median"] is not None]
        valid_ne = [x["j_median_nonempty"] for x in per_teacher if x["j_median_nonempty"] is not None]
        cell_j = float(statistics.median(valid)) if valid else None
        cell_j_ne = float(statistics.median(valid_ne)) if valid_ne else None
        cells_out.append({
            "cell_idx": cell_idx, "dim": dim, "temperature": temp,
            "endpoint_label": "qwen_plan", "model_id": "qwen3.7-max",
            "max_tokens": MAX_TOKENS,
            "n_teachers_with_data": len(valid),
            "cell_j_median_5teachers": (round(cell_j, 6) if cell_j is not None else None),
            "cell_j_median_5teachers_nonempty": (round(cell_j_ne, 6) if cell_j_ne is not None else None),
            "cell_j_min": (round(min(valid), 6) if valid else None),
            "cell_j_max": (round(max(valid), 6) if valid else None),
            "n_cells_ge_threshold": sum(1 for x in valid if x >= K_N11_3_THRESHOLD),
            "per_teacher": per_teacher,
        })

    t07 = {"L2": [0.41, 0.52], "L14": [0.36, 0.39]}

    readings = {
        "task": "t1_r1_qwen_temp_sweep_readings",
        "generated_local": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        "revision_sha12": sha12_file(REVISION_PATH),
        "note": "本件只出读数; K-T1-S1/S3 判定归 verdict-keeper (沿修订件 §2/§4)",
        "K_N11_3_THRESHOLD": K_N11_3_THRESHOLD,
        "n_records_total": len(records),
        "n_records_ok": len(ok_recs),
        "n_records_failed": len(records) - len(ok_recs),
        "n_empty_responses": n_empty,
        "empty_response_rate": (round(n_empty / len(ok_recs), 6) if ok_recs else None),
        "cells": cells_out,
        "t07_baseline_juxtaposition": t07,
    }

    hits = self_scan_obj(readings)
    readings["key_shape_self_scan"] = {
        "hits": [{"name": n, "count": c} for n, c in hits],
        "status": "clean" if not hits else "WARN",
    }

    TMP_DIR.mkdir(parents=True, exist_ok=True)
    READINGS_PATH.write_text(json.dumps(readings, ensure_ascii=False, indent=2),
                             encoding="utf-8", newline="\n")
    print(json.dumps({k: v for k, v in readings.items() if k != "cells"},
                     ensure_ascii=False, indent=2))
    for c in cells_out:
        print(f"  cell {c['cell_idx']} ({c['dim']}/t={c['temperature']}): "
              f"J_med={c['cell_j_median_5teachers']} "
              f"ne={c['cell_j_median_5teachers_nonempty']} "
              f"min={c['cell_j_min']} max={c['cell_j_max']} "
              f"n_ge_0.85={c['n_cells_ge_threshold']}")
    print(f"\nreadings: {READINGS_PATH}")


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selfcert")
    sub.add_parser("probe")
    p_run = sub.add_parser("run")
    p_run.add_argument("start", type=int)
    p_run.add_argument("end", type=int)
    p_run.add_argument("--calls-limit", type=int, default=0)
    sub.add_parser("aggregate")
    a = ap.parse_args()
    if a.cmd == "selfcert":
        cmd_selfcert()
    elif a.cmd == "probe":
        cmd_probe()
    elif a.cmd == "run":
        cmd_run(a.start, a.end, a.calls_limit)
    elif a.cmd == "aggregate":
        cmd_aggregate()


if __name__ == "__main__":
    main()