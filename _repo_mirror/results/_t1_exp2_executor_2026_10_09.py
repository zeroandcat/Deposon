# -*- coding: utf-8 -*-
"""
================================================================================
T1 温度轴 Exp2 执行棒 (D 先导探针 -> A 答案面换测基线 -> C 温度 5 水平 x R=6)
================================================================================
授权锚  : PI 2026-10-09 卡 ask_6455cd9f15bf7dc12ae673d9
          题① (r7a_start_opt1) 逐字:
          「并档＋放行——D 段入 ≈607；跑禁解除、即派执行棒（含 activation 补记）」
上承    : 预登记修订件 2FF15AEEB5D0 (_t1_prereg_revision_temp_axis_exp2_2026_10_09.md)
          §2 claim / §3 构造(D,A,C) / §4 kill-line 9 条 / §5 MDE / §6 规模档
          设计件 7AAA90EE6D50 / r2 判定件 9C18B9893579
体例    : 沿 r2 executor 38D0CF7FC9BA (只读底本) —— checkpoint / watchdog / 补跑 /
          finish_reason 与截段记录 / 答案面抽取 按预登记定义 / 三口径字段

构造    : D 段 = seed 受控重复调用 (新增 request body 字段 seed=42; 确认档 50 calls;
                       判读线未获 PI 给 ⇒ 只作事实登记, 0 承载任何 kill-line 判定)
          A 段 = 答案面换测基线 (自既有 180 条 r2 records 抽取, 0 新调用)
          C 段 = 温度 {0.0,0.2,0.35,0.5,0.7} x R=6 x 2 dims x 5 教师 x 2 captions
                 = 600 calls (与 r2 之 T=3/R=3 0 兼容 ⇒ 0 并入 r2 新读数)

纪律   : 0 判读 / 0 赋 k_* 布尔 / 0 落档 (判定归 verdict-keeper 面)
         0 合并派生 JSON (R5) / 0 覆写任何既有件 / 0 触 frozen
         R4: key 永不明文, 仅 runtime 读入内存, 0 落盘 0 回显 0 入 prompt/JSON/log
         中间产物仅落 .tmp/; 结果件落 results/ (新名)
         seed 字段: 仅 D 段上送; C 段 0 上送 (沿 r2 与设计件案 C 字面)
================================================================================
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import itertools
import json
import os
import random
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
# 常量与路径 (Exp2 独立 prefix, ⛔ 0 覆写 r1/r2 任一件)
# ============================================================
ROOT = Path("D:/私人资料/deposon-repo")
RESULTS_DIR = ROOT / "results"
TMP_DIR = ROOT / ".tmp"

# D 段 (seed 先导探针)
D_CHECKPOINT_PATH = TMP_DIR / "_t1_exp2_d_records.json"
D_RESULT_PATH = TMP_DIR / "_t1_exp2_d_readings.json"
# C 段 (温度 5 水平 x R=6)
C_CHECKPOINT_PATH = TMP_DIR / "_t1_exp2_c_records.json"
SELFCERT_PATH = TMP_DIR / "_t1_exp2_selfcert.json"
PROBE_LOG_PATH = TMP_DIR / "_t1_exp2_probe_log.json"
CALIB_PATH = TMP_DIR / "_t1_exp2_calib_2026_10_09.json"
# A 段 (答案面换测基线) -> 落 results/ (交付件)
A_BASELINE_PATH = RESULTS_DIR / "_t1_exp2_answer_face_baseline_2026_10_09.json"
# 汇总 -> 落 results/ (新名; ⛔ 0 合并派生 JSON)
RESULT_PATH = RESULTS_DIR / "_t1_exp2_result_2026_10_09.json"

KEY_SOURCE_PATH = Path("C:/Users/Administrator/Desktop/AI/LLM API.txt")
CAPTIONS_PATH = ROOT / "corpus/v20_caption_surface/strip_captions_22.json"
CAPTIONS_SHA12_EXPECTED = "6A2656878745"

# ============================================================
# 输入件 (⛔ 0 回改; 起跑前 SHA-12 硬闸 —— 含 activation 补记, 未闭则不得起跑)
# ============================================================
# activation 补记 (P-6) —— 本棒起跑之硬前置; 不存在或不符 => FATAL
ACTIVATION_PATH = RESULTS_DIR / "_t1_exp2_activation_supplement_2026_10_09.md"
ACTIVATION_SHA12_EXPECTED = "8DB3F88B5ED0"
# 唯一实验规格
PREREG_PATH = RESULTS_DIR / "_t1_prereg_revision_temp_axis_exp2_2026_10_09.md"
PREREG_SHA12_EXPECTED = "2FF15AEEB5D0"
# 设计件 (构造来源)
DESIGN_PATH = RESULTS_DIR / "_t1_temp_axis_new_experiment_design_2026_10_09.md"
DESIGN_SHA12_EXPECTED = "7AAA90EE6D50"
# r2 面 (只读底本与 A 段底稿)
R2_VERDICT_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_r2_verdict_2026_10_09.md"
R2_VERDICT_SHA12_EXPECTED = "9C18B9893579"
R2_REVISION_PATH = RESULTS_DIR / "_t1_prereg_revision_qwen_temp_sweep_2026_10_09.md"
R2_REVISION_SHA12_EXPECTED = "BDA5D5F3DFA0"
R2_ACTIVATION_PATH = RESULTS_DIR / "_t1_r2_activation_2026_10_09.md"
R2_ACTIVATION_SHA12_EXPECTED = "8E59B797AA2D"
R2_EXEC_REGISTER_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_r2_exec_register_2026_10_09.md"
R2_EXEC_REGISTER_SHA12_EXPECTED = "CF4826A731D6"
R2_RESULT_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_r2_result_2026_10_09.json"
R2_RESULT_SHA12_EXPECTED = "8D6242DA158C"
R2_EXECUTOR_PATH = RESULTS_DIR / "_t1_qwen_temp_sweep_r2_executor_2026_10_09.py"
R2_EXECUTOR_SHA12_EXPECTED = "38D0CF7FC9BA"
R2_RECORDS_PATH = TMP_DIR / "_t1_qwen_temp_sweep_r2_records.json"
R2_RECORDS_SHA12_EXPECTED = "BB511E7B0BAF"
R2_SELFCERT_PATH = TMP_DIR / "_t1_qwen_temp_sweep_r2_selfcert.json"
R2_SELFCERT_SHA12_EXPECTED = "124051B56295"

INPUT_GATES = [
    ("activation_supplement_p6", ACTIVATION_PATH, ACTIVATION_SHA12_EXPECTED),
    ("prereg_exp2", PREREG_PATH, PREREG_SHA12_EXPECTED),
    ("design", DESIGN_PATH, DESIGN_SHA12_EXPECTED),
    ("r2_verdict", R2_VERDICT_PATH, R2_VERDICT_SHA12_EXPECTED),
    ("r2_revision", R2_REVISION_PATH, R2_REVISION_SHA12_EXPECTED),
    ("r2_activation", R2_ACTIVATION_PATH, R2_ACTIVATION_SHA12_EXPECTED),
    ("r2_exec_register", R2_EXEC_REGISTER_PATH, R2_EXEC_REGISTER_SHA12_EXPECTED),
    ("r2_result", R2_RESULT_PATH, R2_RESULT_SHA12_EXPECTED),
    ("r2_executor", R2_EXECUTOR_PATH, R2_EXECUTOR_SHA12_EXPECTED),
    ("r2_records", R2_RECORDS_PATH, R2_RECORDS_SHA12_EXPECTED),
    ("r2_selfcert", R2_SELFCERT_PATH, R2_SELFCERT_SHA12_EXPECTED),
]

# ============================================================
# 阈值 (沿用, 0 新设) —— 本棒 0 判读, 仅登记读数
# ============================================================
K_N11_3_THRESHOLD = 0.85
TH_T1_N_MIN = 10
INTER_CALL_SERIAL_S = 2.5
WATCHDOG_S = 600
BATCH_CALL_LIMIT = 30
CALL_TIMEOUT_S = 90  # 沿 r1/r2 字面

# MDE 冻结段 (PI 决议③逐字; ⛔ 非判据线; ⛔ 0 代裁 0 微调)
MDE_NOMINAL_PP = 5.0      # 名义 MDE ≈ 5pp
MDE_CLUSTER_PP = (8.0, 15.0)  # 聚类保守 MDE 8-15pp
MDE_GROUP_PAIRED_PP = 43.0   # 组级配对检验 MDE ≈ 43pp (不可用于小效应)
# 置换检验次数 (预登记件 K-EXP2-A3 逐字: 10,000 次)
PERMUTATION_N = 10000

# ============================================================
# 5 教师 / captions (沿 r2 字面, 0 扩 caption)
# ============================================================
TEACHER_PATHS_REL = [
    ("kimi",    "corpus/v20/by_model/kimi/index_v2_2026_09_16.json"),
    ("GLM_1",   "corpus/v20/by_model/GLM_1/three_way_glm_slot_blind_test_2026_09_16.json"),
    ("GLM_2",   "corpus/v20/by_model/GLM_2/glm_artifact_v_2026_09_16.json"),
    ("coze",    "corpus/v20/by_model/coze/coze_artifact_v_2026_09_16.json"),
    ("minimax", "corpus/v20/by_model/minimax/artifact_v_2026_09_16.json"),
]
TEACHER_NAMES = [t[0] for t in TEACHER_PATHS_REL]
SEED = 42  # 沿既有登记值; D 段上送, C 段 0 上送

L2_PROMPTS = ["L_biological_taxonomy", "S5"]
L14_PROMPTS = ["L_geography_world", "L_historical_causality"]

# ============================================================
# 端点 (qwen 单端点, 沿 r1/r2/T15 executor 体例)
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
MAX_TOKENS = 500  # 沿 r1/r2; 该轴 0 漂移 (实测依据见 r2 activation §3.2)

# ---- D 段 (seed 受控先导探针) ----
# 构造: 5 教师 x 2 captions x 1 温度 x 5 重复 = 50 calls (确认档)
# 温度选取: 沿既有锚 t=0.5 (非 0 值 —— 判「端点是否遵守 seed」须在有随机性之温度下观测;
#           t=0.0 之确定性会使观测与「端点忽略 seed」混淆, 0 可分辨)
D_TEMPERATURE = 0.5
D_CAPTION_IDS = L2_PROMPTS  # 确认档取 L2 之 2 captions (5 教师 x 2 captions x 5 重复)
D_REPEATS = 5
D_CELL_LABEL = "D_seed_probe"

# ---- C 段 (温度 5 水平 x R=6) ----
TEMPERATURES = [0.0, 0.2, 0.35, 0.5, 0.7]  # 冻结 (预登记件 §3.3)
N_REASKS = 6  # R=6 (冻结; 由 r2 之 3 扩至 6)
CELLS: List[Tuple[str, float]] = []
for _dim in ("L2", "L14"):
    for _t in TEMPERATURES:
        CELLS.append((_dim, _t))

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
    """仅登记存在性/长度/形态类别 —— ⛔ 0 读出并回显 key 值 (沿 r2 体例)."""
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
# 端点调用 (度量对象 = 完整教师回复; seed_send=True 时上送 seed)
# ============================================================
def call_chat(api_key: str, endpoint: str, model: str,
              messages: List[Dict[str, str]], temperature: float,
              max_tokens: int, timeout: int = CALL_TIMEOUT_S,
              use_proxy: bool = False,
              seed_send: bool = False) -> Dict[str, Any]:
    headers = {"Authorization": f"Bearer {api_key}",
               "Content-Type": "application/json"}
    body = {"model": model, "messages": messages,
            "temperature": temperature, "max_tokens": max_tokens,
            "stream": False}
    if seed_send:
        # D 段唯一新增字段 (activation 补记 §3.2 已登记)
        body["seed"] = SEED
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
# 答案面抽取 (预登记件 §3.2 冻结规则)
#   规则: full_reply_text 之尾非空行, 逐字 = 答案
#   ⛔ 0 语义解析 / 0 LLM 改写 / 0 归一化
# ============================================================
def extract_answer(full_reply_text: str) -> str:
    lines = [ln for ln in (full_reply_text or "").split("\n") if ln.strip()]
    return lines[-1].strip() if lines else ""


# ============================================================
# Jaccard (沿 r1/r2 字面) / tokenize
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


def answer_dissim_exact(a: str, b: str) -> float:
    """精确相异 (0/1) —— 预登记件 §3.2 冻结之主口径."""
    return 0.0 if a == b else 1.0


def answer_dissim_edit(a: str, b: str) -> Optional[float]:
    """归一化编辑相异度 = 1 - SequenceMatcher ratio —— 预登记件 §3.2 冻结之辅口径.
    任一侧为空 => None (不可构造, ⛔ 0 以 0 充)."""
    if not a or not b:
        return None
    return 1.0 - difflib.SequenceMatcher(None, a, b).ratio()


# ============================================================
# Captions / prompts (全同 r2)
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
# Checkpoint (仅 .tmp/)
# ============================================================
def load_checkpoint(path: Path) -> List[Dict[str, Any]]:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return []
    return []


def save_checkpoint(records: List[Dict[str, Any]], path: Path) -> None:
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8", newline="\n")


def ok_map(records: List[Dict[str, Any]], keyf) -> Dict[Any, Dict[str, Any]]:
    m: Dict[Any, Dict[str, Any]] = {}
    for r in records:
        if r.get("ok"):
            m[keyf(r)] = r
    return m


# ============================================================
# 构造面自证 (开跑前落 .tmp)
# ============================================================
def stats(vals: List[Any]) -> Dict[str, Any]:
    n = len(vals)
    nd = len(set(vals))
    if n > 0 and all(isinstance(v, (int, float)) for v in vals):
        return {"n": n, "n_distinct": nd, "min": min(vals), "max": max(vals),
                "mean": round(statistics.fmean(vals), 6),
                "std": round(statistics.pstdev(vals), 6) if n > 1 else 0.0}
    return {"n": n, "n_distinct": nd, "min": "n/a(str)", "max": "n/a(str)",
            "mean": "n/a", "std": "n/a"}


def cmd_selfcert() -> None:
    print("=== T1-Exp2 构造面自证 (开跑前) ===", flush=True)
    gates = verify_input_gates()
    caps_sha = sha12_file(CAPTIONS_PATH)
    caps = load_captions()
    by_id = {c["id"]: c for c in caps}
    used_ids = L2_PROMPTS + L14_PROMPTS
    texts = [by_id[i]["text"] for i in used_ids]

    calib = {}
    if CALIB_PATH.exists():
        c = json.loads(CALIB_PATH.read_text(encoding="utf-8"))
        calib = c

    n_groups = 2 * 5 * len(used_ids)  # dim x teacher x caption
    report = {
        "task": "t1_exp2_temp_axis_selfcert",
        "generated_local": now_local(),
        "authorization": {
            "pi_card": "ask_6455cd9f15bf7dc12ae673d9",
            "q1_r7a_start_opt1_verbatim": "并档＋放行——D 段入 ≈607；跑禁解除、即派执行棒（含 activation 补记）",
            "activation_supplement": f"_t1_exp2_activation_supplement_2026_10_09.md ({ACTIVATION_SHA12_EXPECTED})",
            "upstream_prereg": "_t1_prereg_revision_temp_axis_exp2_2026_10_09.md (2FF15AEEB5D0)",
        },
        "input_gates": gates,
        "captions_sha12": caps_sha.upper(),
        "captions_sha12_expected": CAPTIONS_SHA12_EXPECTED,
        "matrix_c_segment": {
            "n_cells": len(CELLS),
            "cells": [{"cell_idx": i, "dim": d, "temperature": t}
                      for i, (d, t) in enumerate(CELLS)],
            "endpoint": ENDPOINTS["qwen_plan"]["endpoint"],
            "model_id": ENDPOINTS["qwen_plan"]["model_id"],
            "max_tokens": MAX_TOKENS,
            "n_teachers": len(TEACHER_NAMES),
            "n_reasks": N_REASKS,
            "temperatures": TEMPERATURES,
            "calls_per_cell": len(TEACHER_NAMES) * 2 * N_REASKS,
            "total_calls": len(CELLS) * len(TEACHER_NAMES) * 2 * N_REASKS,
            "records_per_group_per_cell": 2 * N_REASKS,
            "n_groups": n_groups,
            "pairs_within_temp_total": n_groups * len(TEMPERATURES) * (N_REASKS * (N_REASKS - 1) // 2),
            "pairs_cross_temp_reask_matched": n_groups * (len(TEMPERATURES) * (len(TEMPERATURES) - 1) // 2) * N_REASKS,
            "pairs_cross_temp_allcross": n_groups * (len(TEMPERATURES) * (len(TEMPERATURES) - 1) // 2) * N_REASKS * N_REASKS,
            "n_min_same_caption": 2 * (N_REASKS * (N_REASKS - 1) // 2),
            "n_min_all_pooled": (2 * N_REASKS) * (2 * N_REASKS - 1) // 2,
        },
        "matrix_d_segment": {
            "cell_label": D_CELL_LABEL,
            "endpoint": ENDPOINTS["qwen_plan"]["endpoint"],
            "model_id": ENDPOINTS["qwen_plan"]["model_id"],
            "max_tokens": MAX_TOKENS,
            "n_teachers": len(TEACHER_NAMES),
            "caption_ids": D_CAPTION_IDS,
            "temperature": D_TEMPERATURE,
            "repeats": D_REPEATS,
            "total_calls": len(TEACHER_NAMES) * len(D_CAPTION_IDS) * D_REPEATS,
            "seed_sent_in_body": True,
            "seed_value": SEED,
            "temperature_selection_note": "取 t=0.5 (非 0 值): t=0.0 之端点确定性会使观测与「端点忽略 seed」混淆, 0 可分辨; 0.5 系既有锚温度",
            "judgement_line": "⛔ 数值判读线未获 PI 给 ⇒ 本段读数只作事实登记, 0 承载任何 kill-line 判定",
        },
        "seed_field_registration": {
            "existing_r2_face": "SEED=42 仅定义 (executor 38D0CF7FC9BA L104), request body 0 含 seed (L244-246), L954 仅 selfcert 回显 ⇒ 既有 180 calls 实测未上送",
            "d_segment": "新增 request body 字段 seed=42 (activation 补记 §3.2 已登记)",
            "c_segment": "⛔ 不上送 seed (沿 r2 与设计件案 C 字面: SEED 仅登记)",
        },
        "input_field_stats": {
            "caption_ids_used": stats(used_ids),
            "caption_text_char_len": stats([len(t) for t in texts]),
            "caption_text_token_len": stats([len(tokenize(t)) for t in texts]),
            "temperature": stats(TEMPERATURES),
            "teacher_names": stats(TEACHER_NAMES),
            "reask_idx": stats(list(range(N_REASKS))),
            "dim": stats(["L2", "L2", "L14", "L14"]),
        },
        "kill_line_reference_only": {
            "note": "本棒 0 判读; 以下仅为引用预登记件字面, 本件 0 出任何 PASS/FAIL, 0 赋 k_* 布尔",
            "K-T1-R1-1_state": "构造性解除 (C 段 T=5/R=6 使 n_distinct<=3 触发条件 0 成立); ⛔ 0 视为豁免",
            "K-EXP2_kill_lines_count": 8,
            "MDE_nominal_pp": MDE_NOMINAL_PP,
            "MDE_cluster_pp": list(MDE_CLUSTER_PP),
            "MDE_group_paired_pp": MDE_GROUP_PAIRED_PP,
            "TH_T1_N_MIN": TH_T1_N_MIN,
            "K_N11_3_THRESHOLD": K_N11_3_THRESHOLD,
        },
        "calibration": calib,
        "key_slot_fact": key_slot_fact(ENDPOINTS["qwen_plan"]["key_index_1based"]),
        "key_reading_note": "key 仅 runtime 读入内存用于调用; 0 落盘 0 明文 0 回显 0 入 prompt/JSON/log (R4)",
    }
    report["key_shape_self_scan"] = {
        "hits": [{"name": n, "count": c} for n, c in self_scan_obj(report)],
        "status": "clean" if not self_scan_obj(report) else "WARN",
    }
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    SELFCERT_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2),
                             encoding="utf-8", newline="\n")
    print(f"selfcert written: {SELFCERT_PATH}", flush=True)
    print(f"input gates all_match: {gates['all_match']}", flush=True)
    for n in ("temperature", "reask_idx"):
        print(f"  {n} n_distinct = {report['input_field_stats'][n]['n_distinct']}", flush=True)
    if gates["failures"]:
        print("FATAL:", gates["failures"])
        sys.exit(1)


# ============================================================
# 即用即探 (单次)
# ============================================================
def cmd_probe() -> None:
    print("=== 即用即探: qwen_plan (1 call) ===", flush=True)
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
        "reasoning_present": bool(r.get("reason_content") or r.get("reasoning_content", "")),
        "full_reply_len": len(r.get("full_reply", "") or ""),
        "error_body_snippet": (r.get("error_body_snippet") or "")[:200],
        "error_snippet": (r.get("error_snippet") or "")[:200],
        "key_slot_fact": key_slot_fact(ep["key_index_1based"]),
        "note": "key 0 落盘 0 明文 (R4); 本条 0 含 key 值; 探活 0 上送 seed",
    }
    out["key_shape_self_scan"] = {
        "hits": [{"name": n, "count": c} for n, c in self_scan_obj(out)],
        "status": "clean" if not self_scan_obj(out) else "WARN",
    }
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    PROBE_LOG_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                              encoding="utf-8", newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2), flush=True)
    if not out["ok"]:
        print("FATAL: probe failed -> 停手上报 (0 绕过 0 改端点)")
        sys.exit(1)


# ============================================================
# 校准 (按需; 沿 r2 体例, 尽量省) —— 探 max_tokens=500 之 finish_reason
# ============================================================
def cmd_calibrate() -> None:
    print("=== 校准: max_tokens=500 x 1 call (finish_reason 核) ===", flush=True)
    gates = verify_input_gates()
    if not gates["all_match"]:
        print(f"FATAL: input gate mismatch: {gates['failures']}")
        sys.exit(1)
    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])
    caps = load_captions()
    prompts_list = select_prompts(caps, D_CAPTION_IDS)
    po = prompts_list[0]
    messages = [{"role": "system", "content": PROMPT_SYSTEM},
                {"role": "user", "content": build_user_prompt("kimi", po["id"], po["text"])}]
    r = call_chat(api_key, ep["endpoint"], ep["model_id"], messages,
                  temperature=D_TEMPERATURE, max_tokens=MAX_TOKENS, timeout=CALL_TIMEOUT_S)
    content = r.get("content", "") or ""
    reasoning = r.get("reasoning_content", "") or ""
    out = {
        "generated_local": now_local(),
        "max_tokens_requested": MAX_TOKENS,
        "temperature": D_TEMPERATURE,
        "seed_sent": False,
        "caption_id": po["id"], "teacher": "kimi",
        "ok": bool(r.get("ok")), "status_code": r.get("status_code"),
        "finish_reason": r.get("finish_reason"),
        "truncated": (r.get("finish_reason") == "length") if r.get("ok") else None,
        "content_len": len(content), "reasoning_len": len(reasoning),
        "reasoning_present": bool(reasoning),
        "usage_completion_tokens": (r.get("usage") or {}).get("completion_tokens"),
        "usage_reasoning_tokens": (r.get("usage") or {}).get("reasoning_tokens"),
        "latency_ms": r.get("latency_ms"),
        "answer_face": extract_answer(r.get("full_reply", "") or ""),
        "note": "沿 r2 体例: max_tokens=500 保留 (r2 校准 3 档实测 finish_reason 6/6 = stop, 0 截段); 本校准为单 call 复核",
    }
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    CALIB_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                          encoding="utf-8", newline="\n")
    print(json.dumps(out, ensure_ascii=False, indent=2), flush=True)


# ============================================================
# D 段: seed 受控先导探针 (确认档 50 calls; seed 上送)
# ============================================================
def d_key(r: Dict[str, Any]):
    return (r["teacher"], r["caption_id"], r["reask_idx"])


def cmd_run_d() -> None:
    print("=== T1-Exp2 D 段: seed 受控先导探针 (确认档 50 calls) ===", flush=True)
    gates = verify_input_gates()
    if not gates["all_match"]:
        print(f"FATAL: input gate mismatch: {gates['failures']}")
        sys.exit(1)
    caps_sha = sha12_file(CAPTIONS_PATH)
    if caps_sha.upper() != CAPTIONS_SHA12_EXPECTED.upper():
        print(f"FATAL: captions SHA-12 mismatch: {caps_sha}")
        sys.exit(1)

    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])
    captions = load_captions()
    prompts_list = select_prompts(captions, D_CAPTION_IDS)
    records = load_checkpoint(D_CHECKPOINT_PATH)
    print(f"input gates OK; loaded {len(records)} existing D records", flush=True)

    have_ok = ok_map(records, d_key)
    failed_here = [r for r in records if not r.get("ok")]
    wall_start = time.time()
    n_new = 0
    for teacher_name in TEACHER_NAMES:
        teacher_path_rel = next((p[1] for n, p in TEACHER_PATHS_REL if n == teacher_name), "")
        for po in prompts_list:
            caption_id, caption_text = po["id"], po["text"]
            for ri in range(D_REPEATS):
                kt = (teacher_name, caption_id, ri)
                if kt in have_ok:
                    continue
                if kt in {d_key(r) for r in failed_here}:
                    continue  # 0 重复计 calls; 补跑另档
                if n_new > 0:
                    time.sleep(INTER_CALL_SERIAL_S)
                if time.time() - wall_start > WATCHDOG_S:
                    print("  [watchdog] stopping D batch", flush=True)
                    save_checkpoint(records, D_CHECKPOINT_PATH)
                    break
                messages = [{"role": "system", "content": PROMPT_SYSTEM},
                            {"role": "user", "content": build_user_prompt(
                                teacher_name, caption_id, caption_text)}]
                t0 = time.time()
                resp = call_chat(api_key, ep["endpoint"], ep["model_id"], messages,
                                 temperature=D_TEMPERATURE, max_tokens=MAX_TOKENS,
                                 timeout=CALL_TIMEOUT_S, seed_send=True)
                elapsed = time.time() - t0
                ok = bool(resp.get("ok"))
                content = resp.get("content", "") if ok else ""
                reasoning = resp.get("reasoning_content", "") if ok else ""
                full = resp.get("full_reply", "") if ok else ""
                rec = {
                    "cell_label": D_CELL_LABEL, "segment": "D",
                    "endpoint_label": ep["label"], "endpoint": ep["endpoint"],
                    "endpoint_model": ep["model_id"], "dim": "L2",
                    "temperature": D_TEMPERATURE, "max_tokens": MAX_TOKENS,
                    "seed_sent": True, "seed_value": SEED,
                    "teacher": teacher_name, "teacher_path_rel": teacher_path_rel,
                    "caption_id": caption_id,
                    "caption_text_sha12": sha12_bytes(caption_text.encode("utf-8")),
                    "reask_idx": ri, "ok": ok,
                    "content_text": content, "reasoning_text": reasoning,
                    "full_reply_text": full,
                    "finish_reason": resp.get("finish_reason") if ok else None,
                    "truncated": (resp.get("finish_reason") == "length") if ok else None,
                    "content_len": len(content), "reasoning_len": len(reasoning),
                    "full_reply_len": len(full),
                    "full_reply_sha12": sha12_bytes(full.encode("utf-8")) if ok else "",
                    "answer_face": extract_answer(full) if ok else "",
                    "latency_ms": round(elapsed * 1000, 1),
                    "status_code": resp.get("status_code"),
                    "error_category": resp.get("error_category"),
                    "model_returned": resp.get("model_returned", ""),
                    "usage": resp.get("usage", {}) if ok else {},
                    "timestamp_local": now_local(),
                }
                records.append(rec)
                n_new += 1
                save_checkpoint(records, D_CHECKPOINT_PATH)
                if ok:
                    print(f"  {teacher_name}/{caption_id}/r{ri} ok "
                          f"(lat={rec['latency_ms']:.0f}ms, fr={rec['finish_reason']}, "
                          f"ans_sha12={sha12_bytes(rec['answer_face'].encode('utf-8'))})",
                          flush=True)
                else:
                    print(f"  {teacher_name}/{caption_id}/r{ri} FAIL "
                          f"{rec['error_category']} (lat={rec['latency_ms']:.0f}ms)", flush=True)

    save_checkpoint(records, D_CHECKPOINT_PATH)
    print(f"\n=== D 段 batch done: new_calls={n_new} total_records={len(records)} ===",
          flush=True)


def cmd_retry_d() -> None:
    records = load_checkpoint(D_CHECKPOINT_PATH)
    failed_keys = {d_key(r) for r in records if not r.get("ok")}
    if not failed_keys:
        print("D 段: 0 失败 tuple, 0 需补跑", flush=True)
        return
    print(f"D 段 补跑: {len(failed_keys)} failed tuples", flush=True)
    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])
    captions = load_captions()
    by_id = {c["id"]: c for c in captions}
    for kt in sorted(failed_keys):
        teacher_name, caption_id, ri = kt
        po = by_id[caption_id]
        time.sleep(INTER_CALL_SERIAL_S)
        messages = [{"role": "system", "content": PROMPT_SYSTEM},
                    {"role": "user", "content": build_user_prompt(
                        teacher_name, caption_id, po["text"])}]
        resp = call_chat(api_key, ep["endpoint"], ep["model_id"], messages,
                         temperature=D_TEMPERATURE, max_tokens=MAX_TOKENS,
                         timeout=CALL_TIMEOUT_S, seed_send=True)
        ok = bool(resp.get("ok"))
        full = resp.get("full_reply", "") if ok else ""
        rec = {
            "cell_label": D_CELL_LABEL, "segment": "D",
            "endpoint_label": ep["label"], "endpoint": ep["endpoint"],
            "endpoint_model": ep["model_id"], "dim": "L2",
            "temperature": D_TEMPERATURE, "max_tokens": MAX_TOKENS,
            "seed_sent": True, "seed_value": SEED,
            "teacher": teacher_name, "teacher_path_rel": next(
                (p[1] for n, p in TEACHER_PATHS_REL if n == teacher_name), ""),
            "caption_id": caption_id,
            "caption_text_sha12": sha12_bytes(po["text"].encode("utf-8")),
            "reask_idx": ri, "ok": ok,
            "content_text": resp.get("content", "") if ok else "",
            "reasoning_text": resp.get("reasoning_content", "") if ok else "",
            "full_reply_text": full,
            "finish_reason": resp.get("finish_reason") if ok else None,
            "truncated": (resp.get("finish_reason") == "length") if ok else None,
            "content_len": len(resp.get("content", "") if ok else ""),
            "reasoning_len": len(resp.get("reasoning_content", "") if ok else ""),
            "full_reply_len": len(full),
            "full_reply_sha12": sha12_bytes(full.encode("utf-8")) if ok else "",
            "answer_face": extract_answer(full) if ok else "",
            "latency_ms": resp.get("latency_ms"),
            "status_code": resp.get("status_code"),
            "error_category": resp.get("error_category"),
            "model_returned": resp.get("model_returned", ""),
            "usage": resp.get("usage", {}) if ok else {},
            "is_rerun_of_failed": True,
            "timestamp_local": now_local(),
        }
        records.append(rec)
        save_checkpoint(records, D_CHECKPOINT_PATH)
        print(f"  RERUN {teacher_name}/{caption_id}/r{ri} "
              f"{'ok' if ok else 'FAIL ' + str(rec['error_category'])}", flush=True)


# ============================================================
# D 段读数 (事实登记; ⛔ 0 判定, ⛔ 0 承载 kill-line)
# ============================================================
def cmd_aggregate_d() -> None:
    records = load_checkpoint(D_CHECKPOINT_PATH)
    ok = [r for r in records if r.get("ok")]
    by_group: Dict[Tuple[str, str], List[Dict[str, Any]]] = {}
    for r in ok:
        by_group.setdefault((r["teacher"], r["caption_id"]), []).append(r)

    total_pairs = 0
    total_identical = 0
    groups_out = []
    partial_any = False
    for (teacher, caption_id), rs in sorted(by_group.items()):
        n = len(rs)
        ident = 0
        pairs = 0
        for a, b in itertools.combinations(rs, 2):
            pairs += 1
            if a["full_reply_sha12"] == b["full_reply_sha12"]:
                ident += 1
        rate = (ident / pairs) if pairs else None
        if rate is not None and 0.0 < rate < 1.0:
            partial_any = True
        # 答案面全同 (辅事实)
        ans = [ans_of(r) for r in rs]
        ans_ident = sum(1 for x, y in itertools.combinations(ans, 2) if x == y)
        ans_pairs = len(list(itertools.combinations(ans, 2)))
        groups_out.append({
            "teacher": teacher, "caption_id": caption_id, "n_ok": n,
            "pairs": pairs, "identical_pairs_full_reply": ident,
            "identical_rate_full_reply": round(rate, 6) if rate is not None else None,
            "pairs_answer_face": ans_pairs, "identical_pairs_answer_face": ans_ident,
            "identical_rate_answer_face": round(ans_ident / ans_pairs, 6) if ans_pairs else None,
        })
        total_pairs += pairs
        total_identical += ident

    uniq_sha = len({r["full_reply_sha12"] for r in ok})
    uniq_ans = len({ans_of(r) for r in ok})
    out = {
        "task": "t1_exp2_d_seed_probe_readings",
        "generated_local": now_local(),
        "note": "事实登记; ⛔ 判读线未获 PI 给 ⇒ 本段 0 承载任何 kill-line 判定; 0 代裁「端点遵守/不遵守 seed」",
        "construction": {
            "temperature": D_TEMPERATURE, "seed_sent": True, "seed_value": SEED,
            "repeats": D_REPEATS, "caption_ids": D_CAPTION_IDS,
            "n_teachers": len(TEACHER_NAMES),
            "planned_calls": len(TEACHER_NAMES) * len(D_CAPTION_IDS) * D_REPEATS,
        },
        "counts": {"records_total": len(records), "records_ok": len(ok),
                   "records_failed": len(records) - len(ok)},
        "overall": {
            "pairs_total": total_pairs,
            "identical_pairs_full_reply": total_identical,
            "identical_rate_full_reply": round(total_identical / total_pairs, 6) if total_pairs else None,
            "uniq_full_reply_sha12": uniq_sha,
            "uniq_answer_face": uniq_ans,
        },
        "partial_identical_observed": partial_any,
        "partial_identical_note": "「部分全同」之归属未获 PI 给 ⇒ 本棒 0 代裁, 仅登记是否出现",
        "per_group": groups_out,
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj(ok)],
            "status": "clean" if not self_scan_obj(ok) else "WARN",
        },
    }
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    D_RESULT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                             encoding="utf-8", newline="\n")
    print(f"D readings written: {D_RESULT_PATH}", flush=True)
    print(f"  ok={len(ok)}/{len(records)}  identical_rate_full_reply="
          f"{out['overall']['identical_rate_full_reply']}  uniq_sha={uniq_sha}", flush=True)


# ============================================================
# C 段: 温度 5 水平 x R=6 (600 calls; ⛔ 不上送 seed)
# ============================================================
def c_key(r: Dict[str, Any]):
    return (r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"])


def run_cell_c(cell_idx: int, dim: str, temp: float,
               captions: List[Dict[str, Any]], records: List[Dict[str, Any]],
               wall_start: float, retry_failed: bool = False,
               max_calls_in_cell: int = 0) -> Dict[str, Any]:
    ep = ENDPOINTS["qwen_plan"]
    unset_proxy()
    api_key = read_api_key(ep["key_index_1based"])

    prompts_ids = L2_PROMPTS if dim == "L2" else L14_PROMPTS
    prompts_list = select_prompts(captions, prompts_ids)

    have_ok = ok_map(records, c_key)
    failed_here = [r for r in records if not r.get("ok") and r.get("cell_idx") == cell_idx]

    summary = {"cell_idx": cell_idx, "dim": dim, "temperature": temp,
               "endpoint_label": ep["label"], "endpoint": ep["endpoint"],
               "model_id": ep["model_id"], "max_tokens": MAX_TOKENS,
               "prompts": prompts_ids, "seed_sent": False,
               "n_calls_planned": len(TEACHER_NAMES) * len(prompts_list) * N_REASKS,
               "n_calls_ok": 0, "n_calls_failed": 0,
               "n_skipped_existing_ok": 0, "n_retried_failed": 0}

    n_new = 0
    for teacher_name in TEACHER_NAMES:
        teacher_path_rel = next((p[1] for n, p in TEACHER_PATHS_REL if n == teacher_name), "")
        for po in prompts_list:
            caption_id, caption_text = po["id"], po["text"]
            for ri in range(N_REASKS):
                kt = (cell_idx, teacher_name, caption_id, ri)
                if kt in have_ok:
                    summary["n_skipped_existing_ok"] += 1
                    continue
                if not retry_failed and kt in {(r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"])
                                               for r in failed_here}:
                    continue
                if n_new > 0:
                    time.sleep(INTER_CALL_SERIAL_S)
                if max_calls_in_cell > 0 and n_new >= max_calls_in_cell:
                    summary["calls_limit_break"] = True
                    save_checkpoint(records, C_CHECKPOINT_PATH)
                    return summary
                if time.time() - wall_start > WATCHDOG_S:
                    summary["watchdog_break"] = True
                    save_checkpoint(records, C_CHECKPOINT_PATH)
                    return summary

                messages = [{"role": "system", "content": PROMPT_SYSTEM},
                            {"role": "user", "content": build_user_prompt(
                                teacher_name, caption_id, caption_text)}]
                t0 = time.time()
                resp = call_chat(api_key, ep["endpoint"], ep["model_id"], messages,
                                 temperature=temp, max_tokens=MAX_TOKENS,
                                 timeout=CALL_TIMEOUT_S, use_proxy=ep["use_proxy"],
                                 seed_send=False)
                elapsed = time.time() - t0
                ok = bool(resp.get("ok"))
                content = resp.get("content", "") if ok else ""
                reasoning = resp.get("reasoning_content", "") if ok else ""
                full = resp.get("full_reply", "") if ok else ""
                usage = resp.get("usage", {}) if ok else {}
                is_rerun = any(
                    (r["cell_idx"], r["teacher"], r["caption_id"], r["reask_idx"]) == kt
                    for r in failed_here)
                rec = {
                    "cell_idx": cell_idx, "endpoint_label": ep["label"],
                    "endpoint": ep["endpoint"], "endpoint_model": ep["model_id"],
                    "use_proxy": ep["use_proxy"], "dim": dim, "temperature": temp,
                    "max_tokens": MAX_TOKENS, "seed_sent": False,
                    "teacher": teacher_name, "teacher_path_rel": teacher_path_rel,
                    "caption_id": caption_id,
                    "caption_text_sha12": sha12_bytes(caption_text.encode("utf-8")),
                    "reask_idx": ri, "ok": ok,
                    "content_text": content, "reasoning_text": reasoning,
                    "full_reply_text": full,
                    "finish_reason": resp.get("finish_reason") if ok else None,
                    "truncated": (resp.get("finish_reason") == "length") if ok else None,
                    "content_len": len(content), "reasoning_len": len(reasoning),
                    "full_reply_len": len(full),
                    "full_reply_sha12": sha12_bytes(full.encode("utf-8")) if ok else "",
                    "answer_face": extract_answer(full) if ok else "",
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
                save_checkpoint(records, C_CHECKPOINT_PATH)
                if ok:
                    summary["n_calls_ok"] += 1
                    if is_rerun:
                        summary["n_retried_failed"] += 1
                    print(f"  [{cell_idx}] {teacher_name}/{caption_id}/r{ri} ok "
                          f"(lat={rec['latency_ms']:.0f}ms, fr={rec['finish_reason']}, "
                          f"full_len={rec['full_reply_len']})"
                          f"{' RERUN' if is_rerun else ''}", flush=True)
                else:
                    summary["n_calls_failed"] += 1
                    print(f"  [{cell_idx}] {teacher_name}/{caption_id}/r{ri} FAIL "
                          f"{rec['error_category']} (lat={rec['latency_ms']:.0f}ms)", flush=True)
    return summary


def cmd_run_c(start_idx: int, end_idx: int, calls_limit: int = 0,
              retry_failed: bool = False) -> None:
    mode = "retry-failed" if retry_failed else "run"
    print(f"=== T1-Exp2 C 段 qwen 温扫 {mode} cells [{start_idx},{end_idx}] "
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
    records = load_checkpoint(C_CHECKPOINT_PATH)
    print(f"input gates OK; loaded {len(records)} existing C records", flush=True)

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
        s = run_cell_c(idx, dim, temp, captions, records, wall_start,
                       retry_failed=retry_failed,
                       max_calls_in_cell=calls_limit - calls_made if calls_limit > 0 else 0)
        summaries.append(s)
        calls_made += s["n_calls_ok"] + s["n_calls_failed"]
        if s.get("watchdog_break"):
            break

    save_checkpoint(records, C_CHECKPOINT_PATH)
    wall = time.time() - wall_start
    print(f"\n=== C batch done: wall={wall:.1f}s new_calls={calls_made} "
          f"total_records={len(records)} ===", flush=True)
    for s in summaries:
        print(f"  cell {s['cell_idx']} ({s['dim']}/t={s['temperature']}): "
              f"ok={s['n_calls_ok']} fail={s['n_calls_failed']} "
              f"skip_ok={s['n_skipped_existing_ok']} rerun={s['n_retried_failed']} "
              f"wd={s.get('watchdog_break', False)}")


# ============================================================
# 答案面分析 (A 段基线 + C 段读数; ⛔ 0 判读, ⛔ 0 赋 k_* 布尔)
#   配对口径 (预登记件 §3.2 冻结):
#     同温内: 同组 (dim/caption/teacher) 内 C(R,2)
#     跨温  : reask-matched (与判定件 §4.2 可比) + 全交叉 (提升统计量)
#   分层: ⛔ 0 跨 caption 汇总外推 (K-EXP2-A6) —— 分组级计算后再汇总
# ============================================================
def ans_of(r: Dict[str, Any]) -> str:
    """取答案面 —— 优先落盘之 answer_face 字段; 缺失/空 ⇒ 自 full_reply_text 尾非空行还原.
    (r2 records 无 answer_face 键 ⇒ 必须回退抽取, ⛔ 0 以空串充答案)"""
    a = r.get("answer_face")
    if a:
        return a
    return extract_answer(r.get("full_reply_text", "") or "")


def analyze_records(records: List[Dict[str, Any]], temperatures: List[float],
                    caption_set: Optional[List[str]] = None) -> Dict[str, Any]:
    ok = [r for r in records if r.get("ok")]
    if caption_set is not None:
        ok = [r for r in ok if r["caption_id"] in caption_set]
    # group = (dim, caption_id, teacher) —— 同题组
    groups: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = {}
    for r in ok:
        groups.setdefault((r["dim"], r["caption_id"], r["teacher"]), []).append(r)

    within_exact: List[float] = []
    within_edit: List[float] = []
    cross_exact: List[float] = []
    cross_edit: List[float] = []
    per_group = []

    for (dim, cap, teacher), rs in sorted(groups.items()):
        by_t: Dict[float, List[Dict[str, Any]]] = {}
        for r in rs:
            by_t.setdefault(float(r["temperature"]), []).append(r)

        g_within_exact, g_within_edit = [], []
        # 同温内对
        for t, lst in by_t.items():
            for a, b in itertools.combinations(lst, 2):
                g_within_exact.append(answer_dissim_exact(ans_of(a), ans_of(b)))
                e = answer_dissim_edit(ans_of(a), ans_of(b))
                if e is not None:
                    g_within_edit.append(e)
        # 跨温对 (reask-matched + 全交叉)
        g_cross_exact, g_cross_edit = [], []
        tlist = sorted(by_t.keys())
        for t1, t2 in itertools.combinations(tlist, 2):
            l1, l2 = by_t[t1], by_t[t2]
            # reask-matched
            m1 = {r["reask_idx"]: r for r in l1}
            m2 = {r["reask_idx"]: r for r in l2}
            for ri in sorted(set(m1) & set(m2)):
                g_cross_exact.append(answer_dissim_exact(ans_of(m1[ri]), ans_of(m2[ri])))
                e = answer_dissim_edit(ans_of(m1[ri]), ans_of(m2[ri]))
                if e is not None:
                    g_cross_edit.append(e)
            # 全交叉
            for a in l1:
                for b in l2:
                    if a["reask_idx"] == b["reask_idx"]:
                        continue
                    g_cross_exact.append(answer_dissim_exact(ans_of(a), ans_of(b)))
                    e = answer_dissim_edit(ans_of(a), ans_of(b))
                    if e is not None:
                        g_cross_edit.append(e)

        within_exact.extend(g_within_exact)
        within_edit.extend(g_within_edit)
        cross_exact.extend(g_cross_exact)
        cross_edit.extend(g_cross_edit)

        per_group.append({
            "dim": dim, "caption_id": cap, "teacher": teacher,
            "n_ok": len(rs),
            "temps_present": sorted(by_t.keys()),
            "n_within_pairs": len(g_within_exact),
            "n_cross_pairs": len(g_cross_exact),
            "within_exact_mean": round(statistics.fmean(g_within_exact), 6) if g_within_exact else None,
            "cross_exact_mean": round(statistics.fmean(g_cross_exact), 6) if g_cross_exact else None,
            "delta_exact": (round(statistics.fmean(g_cross_exact) - statistics.fmean(g_within_exact), 6)
                            if g_within_exact and g_cross_exact else None),
            "within_edit_mean": round(statistics.fmean(g_within_edit), 6) if g_within_edit else None,
            "cross_edit_mean": round(statistics.fmean(g_cross_edit), 6) if g_cross_edit else None,
            "delta_edit": (round(statistics.fmean(g_cross_edit) - statistics.fmean(g_within_edit), 6)
                           if g_within_edit and g_cross_edit else None),
        })

    def agg(v: List[float]) -> Optional[float]:
        return round(statistics.fmean(v), 6) if v else None

    w_ex, c_ex = agg(within_exact), agg(cross_exact)
    w_ed, c_ed = agg(within_edit), agg(cross_edit)

    # 组内置换检验 (置换温度标签, PERMUTATION_N 次) —— 单元 = 组之 Δ
    deltas = [g["delta_exact"] for g in per_group if g["delta_exact"] is not None]
    perm = None
    if len(deltas) >= 2:
        rng = random.Random(SEED)
        obs = statistics.fmean(deltas)
        null = []
        for _ in range(PERMUTATION_N):
            sample = [rng.choice(deltas) for _ in range(len(deltas))]
            null.append(statistics.fmean(sample))
        null_sorted = sorted(null)
        lo = null_sorted[int(0.025 * (PERMUTATION_N - 1))]
        hi = null_sorted[int(0.975 * (PERMUTATION_N - 1))]
        n_ge = sum(1 for v in null if v >= obs)
        perm = {
            "n_groups_used": len(deltas),
            "observed_mean_delta_exact": round(obs, 6),
            "null_mean": round(statistics.fmean(null), 6),
            "null_ci95_2p5": round(lo, 6),
            "null_ci95_97p5": round(hi, 6),
            "p_one_sided_greater": round(n_ge / PERMUTATION_N, 6),
            "note": "组内置换: 以组之 Δ 为单元, 自举组内 Δ 值构成 0 分布; CI 之读法归 verdict-keeper 面 (本棒 0 判读)",
        }

    return {
        "counts": {"records_ok": len(ok), "n_groups": len(groups)},
        "n_pairs": {"within_exact": len(within_exact), "cross_exact": len(cross_exact),
                    "within_edit": len(within_edit), "cross_edit": len(cross_edit)},
        "means": {"within_exact": w_ex, "cross_exact": c_ex,
                  "within_edit": w_ed, "cross_edit": c_ed},
        "delta": {"exact": (round(c_ex - w_ex, 6) if (w_ex is not None and c_ex is not None) else None),
                  "edit": (round(c_ed - w_ed, 6) if (w_ed is not None and c_ed is not None) else None)},
        "per_group": per_group,
        "permutation": perm,
    }


def cmd_answer_baseline() -> None:
    """A 段: 自既有 r2 records (BB511E7B0BAF) 抽取答案面并出基线读数 (0 新调用)."""
    print("=== T1-Exp2 A 段: 答案面换测基线 (0 新调用) ===", flush=True)
    gates = verify_input_gates()
    if not gates["all_match"]:
        print(f"FATAL: input gate mismatch: {gates['failures']}")
        sys.exit(1)
    records = json.loads(R2_RECORDS_PATH.read_text(encoding="utf-8"))
    ok = [r for r in records if r.get("ok")]

    # K-EXP2-A2: 答案抽取之尾非空行规则逐字沿用; 还原率 < 1.0 ⇒ 口径不成立
    n_tail_eq_content = 0
    for r in ok:
        a = extract_answer(r.get("full_reply_text", ""))
        if a == (r.get("content_text", "") or "").strip():
            n_tail_eq_content += 1
    restore_rate = n_tail_eq_content / len(ok) if ok else None

    analysis = analyze_records(records, [0.0, 0.3, 0.5])

    out = {
        "task": "t1_exp2_a_answer_face_baseline",
        "generated_local": now_local(),
        "note": "A 段基线 (0 新调用, 自既有 r2 180 ok 抽取); PI 决议④认可之轴探针读数面; ⛔ 本读数 0 构成判定, 仅设计基线",
        "source_records": {"path": str(R2_RECORDS_PATH), "sha12": R2_RECORDS_SHA12_EXPECTED,
                           "records_total": len(records), "records_ok": len(ok)},
        "extraction_rule": "full_reply_text 之尾非空行, 逐字 = 答案; ⛔ 0 语义解析 0 LLM 改写 0 归一化",
        "restore_check_K_EXP2_A2": {
            "tail_equals_content_count": n_tail_eq_content,
            "records_ok": len(ok),
            "restore_rate": round(restore_rate, 6) if restore_rate is not None else None,
            "rule_caliber_holds": (restore_rate == 1.0) if restore_rate is not None else False,
        },
        "answer_uniqueness": {"uniq_answers": len({extract_answer(r.get("full_reply_text", "")) for r in ok})},
        "dissimilarity_definitions": {
            "primary_exact": "精确相异 (0/1)",
            "secondary_edit": "1 - difflib.SequenceMatcher.ratio() (空侧 ⇒ None, 不可构造)",
            "effect_direction": "正 = 温度带来更多答案翻转 (⛔ 非「更相似」之反向表述)",
        },
        "pairing_definitions": {
            "within_temp": "同组 (dim/caption/teacher) 内 C(R,2)",
            "cross_temp_reask_matched": "跨温同 reask_idx (与 r2 判定件 §4.2 可比)",
            "cross_temp_allcross": "跨温全交叉 (除 reask-matched 外)",
            "stratification": "⛔ 0 跨 caption 汇总外推 (K-EXP2-A6); 本面按组计算后再汇总",
        },
        "analysis": analysis,
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj(analysis)],
            "status": "clean" if not self_scan_obj(analysis) else "WARN",
        },
    }
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    A_BASELINE_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2),
                                encoding="utf-8", newline="\n")
    print(f"A baseline written: {A_BASELINE_PATH}", flush=True)
    print(f"  restore_rate={out['restore_check_K_EXP2_A2']['restore_rate']} "
          f"uniq_answers={out['answer_uniqueness']['uniq_answers']} "
          f"delta_exact={analysis['delta']['exact']}", flush=True)


# ============================================================
# 汇总 (D + A + C -> results/ 新名 result JSON; ⛔ 0 判读)
# ============================================================
def cmd_aggregate() -> None:
    print("=== T1-Exp2 汇总 (D + A + C) ===", flush=True)
    gates = verify_input_gates()
    if not gates["all_match"]:
        print(f"FATAL: input gate mismatch: {gates['failures']}")
        sys.exit(1)

    d_records = load_checkpoint(D_CHECKPOINT_PATH)
    c_records = load_checkpoint(C_CHECKPOINT_PATH)
    d_readings = json.loads(D_RESULT_PATH.read_text(encoding="utf-8")) if D_RESULT_PATH.exists() else None
    a_base = json.loads(A_BASELINE_PATH.read_text(encoding="utf-8")) if A_BASELINE_PATH.exists() else None

    c_ok = [r for r in c_records if r.get("ok")]
    c_analysis = analyze_records(c_records, TEMPERATURES) if c_ok else None

    # t=0.7 baseline 并置 (K-EXP2-A5) —— 并置既有 qwen t=0.7 锚
    t07 = [r for r in c_ok if float(r["temperature"]) == 0.7]
    t07_summary = None
    if t07:
        by_g: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = {}
        for r in t07:
            by_g.setdefault((r["dim"], r["caption_id"], r["teacher"]), []).append(r)
        js = []
        for _, lst in by_g.items():
            for a, b in itertools.combinations(lst, 2):
                js.append(jaccard(a.get("full_reply_text", ""), b.get("full_reply_text", "")))
        t07_summary = {
            "n_ok": len(t07), "n_pairs_jaccard": len(js),
            "jaccard_mean_full_reply": round(statistics.fmean(js), 6) if js else None,
            "jaccard_median_full_reply": round(statistics.median(js), 6) if js else None,
            "existing_baseline_anchor": "qwen t=0.7 baseline (r2 activation §2.2: L2 0.41-0.52 / L14 0.36-0.39, Jaccard of full_reply)",
            "note": "本矩阵内 t=0.7 之 Jaccard 与既有 baseline 锚并置 (K-EXP2-A5); ⛔ 0 以矩阵内一致代替与 baseline 并置",
        }

    # per-cell / per-temp 读数 (三口径字段: full_reply Jaccard + 答案面)
    per_temp = {}
    for t in TEMPERATURES:
        lst = [r for r in c_ok if float(r["temperature"]) == t]
        if not lst:
            continue
        g: Dict[Tuple[str, str, str], List[Dict[str, Any]]] = {}
        for r in lst:
            g.setdefault((r["dim"], r["caption_id"], r["teacher"]), []).append(r)
        j, exact = [], []
        for _, rs in g.items():
            for a, b in itertools.combinations(rs, 2):
                j.append(jaccard(a.get("full_reply_text", ""), b.get("full_reply_text", "")))
                exact.append(answer_dissim_exact(ans_of(a), ans_of(b)))
        per_temp[str(t)] = {
            "n_ok": len(lst),
            "jaccard_mean_full_reply": round(statistics.fmean(j), 6) if j else None,
            "jaccard_median_full_reply": round(statistics.median(j), 6) if j else None,
            "answer_face_dissim_exact_mean": round(statistics.fmean(exact), 6) if exact else None,
        }

    # 截段 / finish_reason 面
    fr_counts: Dict[str, int] = {}
    for r in c_ok:
        fr = r.get("finish_reason") or "None"
        fr_counts[fr] = fr_counts.get(fr, 0) + 1

    calls_count = {
        "planned_D": len(TEACHER_NAMES) * len(D_CAPTION_IDS) * D_REPEATS,
        "planned_C": len(CELLS) * len(TEACHER_NAMES) * 2 * N_REASKS,
        "planned_A": 0,
        "actual_calls_D": len(d_records),
        "actual_calls_C": len(c_records),
        "actual_calls_A": 0,
        "ok_D": len([r for r in d_records if r.get("ok")]),
        "ok_C": len(c_ok),
        "failed_D": len([r for r in d_records if not r.get("ok")]),
        "failed_C": len([r for r in c_records if not r.get("ok")]),
        "calib_calls": 1,
        "probe_calls": 1,
        "total_actual_calls": len(d_records) + len(c_records) + 2,
        "quota_note": "PI 卡 ask_6455cd9f15bf7dc12ae673d9 题①: 「D 段入 ≈607」⇒ D+C+补跑 合计 ≲658",
    }

    result = {
        "task": "t1_exp2_temp_axis_result",
        "generated_local": now_local(),
        "authorization": {
            "pi_card": "ask_6455cd9f15bf7dc12ae673d9",
            "q1_verbatim": "并档＋放行——D 段入 ≈607；跑禁解除、即派执行棒（含 activation 补记）",
            "activation_supplement": f"_t1_exp2_activation_supplement_2026_10_09.md ({ACTIVATION_SHA12_EXPECTED})",
            "prereg": "_t1_prereg_revision_temp_axis_exp2_2026_10_09.md (2FF15AEEB5D0)",
        },
        "discipline": {
            "judgement": "⛔ 本件 0 判读, 0 赋 k_* 布尔, 0 落档 (判定归 verdict-keeper 面)",
            "no_softening": "现证据方向 (r2 Δ≈0, 方向为负) 预示大概率落「轴无效」侧; ⛔ 0 软化, ⛔ 0 预断",
            "no_extrapolation": "结论仅在本构造域内成立 (K-EXP2-A8)",
        },
        "input_gates": gates,
        "construction": {
            "endpoint": ENDPOINTS["qwen_plan"]["endpoint"],
            "model_id": ENDPOINTS["qwen_plan"]["model_id"],
            "max_tokens": MAX_TOKENS,
            "temperatures": TEMPERATURES,
            "n_reasks": N_REASKS,
            "n_teachers": len(TEACHER_NAMES),
            "caption_ids": L2_PROMPTS + L14_PROMPTS,
            "seed": {"value": SEED, "sent_in_D": True, "sent_in_C": False},
            "cells": [{"cell_idx": i, "dim": d, "temperature": t} for i, (d, t) in enumerate(CELLS)],
        },
        "calls_count": calls_count,
        "D_segment_readings": d_readings,
        "A_segment_baseline": a_base,
        "C_segment_readings": {
            "counts": {"records_total": len(c_records), "records_ok": len(c_ok)},
            "finish_reason_counts": fr_counts,
            "per_temperature": per_temp,
            "answer_face_analysis": c_analysis,
        },
        "t_0_7_baseline_colocation": t07_summary,
        "MDE_frozen": {
            "nominal_pp": MDE_NOMINAL_PP,
            "cluster_conservative_pp": list(MDE_CLUSTER_PP),
            "group_paired_pp": MDE_GROUP_PAIRED_PP,
            "note": "MDE ＝ 事先声明之设计分辨率基准, ⛔ 非判据线; ⛔ 0 以「Δ 未达 MDE」替代「CI 含 0」之判法",
        },
        "key_shape_self_scan": {
            "hits": [{"name": n, "count": c} for n, c in self_scan_obj(c_records)],
            "status": "clean" if not self_scan_obj(c_records) else "WARN",
        },
    }
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                           encoding="utf-8", newline="\n")
    print(f"result written: {RESULT_PATH}", flush=True)
    print(f"  calls: D={calls_count['actual_calls_D']} C={calls_count['actual_calls_C']} "
          f"total={calls_count['total_actual_calls']}", flush=True)
    if c_analysis:
        print(f"  C delta_exact={c_analysis['delta']['exact']} "
              f"perm_CI=[{c_analysis['permutation']['null_ci95_2p5']}, "
              f"{c_analysis['permutation']['null_ci95_97p5']}]" if c_analysis.get("permutation") else "",
              flush=True)


def main() -> None:
    ap = argparse.ArgumentParser(description="T1 温度轴 Exp2 执行棒")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selfcert")
    sub.add_parser("probe")
    sub.add_parser("calibrate")
    sub.add_parser("run-d")
    sub.add_parser("retry-d")
    sub.add_parser("aggregate-d")
    sub.add_parser("answer-baseline")
    pc = sub.add_parser("run-c")
    pc.add_argument("--start", type=int, default=0)
    pc.add_argument("--end", type=int, default=len(CELLS) - 1)
    pc.add_argument("--calls-limit", type=int, default=0)
    pc.add_argument("--retry-failed", action="store_true")
    sub.add_parser("aggregate")
    args = ap.parse_args()

    if args.cmd == "selfcert":
        cmd_selfcert()
    elif args.cmd == "probe":
        cmd_probe()
    elif args.cmd == "calibrate":
        cmd_calibrate()
    elif args.cmd == "run-d":
        cmd_run_d()
    elif args.cmd == "retry-d":
        cmd_retry_d()
    elif args.cmd == "aggregate-d":
        cmd_aggregate_d()
    elif args.cmd == "answer-baseline":
        cmd_answer_baseline()
    elif args.cmd == "run-c":
        cmd_run_c(args.start, args.end, args.calls_limit, args.retry_failed)
    elif args.cmd == "aggregate":
        cmd_aggregate()


if __name__ == "__main__":
    main()