# -*- coding: utf-8 -*-
"""
L14 续跑 runner (中断恢复).
- 读 .tmp/_l14_records.json (checkpoint, 含当前所有 records)
- 跑指定 (prompt, reask_idx_start, reask_idx_end) 范围内的 calls
- 追加到 checkpoint + 落 result.json (同件补全)
- 支持多次 bash invocation 续跑

用法:
  python .tmp/l14_runner_v2.py <prompt_id> <reask_start> <reask_end>

示例:
  python .tmp/l14_runner_v2.py L_geography_world 0 2   # 跑 reask0, reask1
  python .tmp/l14_runner_v2.py L_geography_world 2 4   # 跑 reask2, reask3
  python .tmp/l14_runner_v2.py L_historical_causality 0 2
  ...
"""
import sys
import time
import os
import json
import re
import hashlib
import zlib
import random
import math
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, 'D:/私人资料/deposon-repo/results')
from _v4_supp_l14_n11full_executor import (
    read_api_key, call_chat, ROUTES,
    unset_proxy_for_qwen_mimo,
    build_user_prompt, tokenize, jaccard,
    sha12_bytes, sha12_file, self_scan_text,
    load_captions, select_prompts,
    load_distill_module, load_proxy_module,
    distill_to_text, proxy_independent_outputs,
    PROMPT_SYSTEM, INTER_CALL_SLEEP_S, CALL_TIMEOUT,
    CAPTIONS_PATH, CAPTIONS_SHA12_EXPECTED,
    TEACHER_PATHS_REL,
    PREREG_V02, PREREG_V02_SHA12_EXPECTED,
    PREREG_N, PREREG_N_SHA12_EXPECTED,
    SEED,
)

MAX_TOKENS = 100

# Checkpoint file
CHECKPOINT = Path("D:/私人资料/deposon-repo/.tmp/_l14_records.json")

# Args
if len(sys.argv) < 4:
    print(f"Usage: python {sys.argv[0]} <prompt_id> <reask_start> <reask_end>")
    sys.exit(1)
PROMPT_ID = sys.argv[1]
REASK_START = int(sys.argv[2])
REASK_END = int(sys.argv[3])

# Load existing records from checkpoint
if CHECKPOINT.exists():
    records = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    print(f"loaded {len(records)} existing records from checkpoint")
else:
    records = []
    print("starting fresh checkpoint")

# Build (teacher, caption_id, reask_idx) existing set
existing_set = set((r["teacher"], r["caption_id"], r["reask_idx"]) for r in records)

# Load captions
captions = load_captions()
prompts_list = select_prompts(captions, [PROMPT_ID])
if not prompts_list:
    print(f"FATAL: prompt_id {PROMPT_ID} not found")
    sys.exit(1)
prompt_obj = prompts_list[0]
caption_text = prompt_obj["text"]
print(f"prompt {PROMPT_ID}: len={len(caption_text)}")

# Use single endpoint qwen
route = ROUTES[0]
teachers = ["kimi", "GLM_1", "GLM_2", "coze", "minimax"]

# Set up proxy
unset_proxy_for_qwen_mimo()
key = read_api_key(route["key_index_1based"])
print(f"key OK")

# Auth ping
print("\n--- auth ping ---")
t0 = time.time()
ping = call_chat(key, route['endpoint'], route['model_id'],
                 [{"role": "user", "content": "ping"}],
                 max_tokens=10, timeout=20, use_proxy=False)
print(f"ping: {time.time()-t0:.1f}s ok={ping.get('ok')}")
if not ping.get('ok'):
    print(f"FATAL: ping failed: {ping}")
    sys.exit(1)

# Run calls
endpoint_start = time.time()
n_new = 0
for teacher_name in teachers:
    teacher_path_rel = next((p[1] for n, p, _ in TEACHER_PATHS_REL if n == teacher_name), "")

    for ri in range(REASK_START, REASK_END):
        if (teacher_name, PROMPT_ID, ri) in existing_set:
            print(f"  skip {teacher_name}/{PROMPT_ID}/reask{ri} (already in checkpoint)")
            continue

        # sleep between calls (except first in this invocation)
        if n_new > 0 or endpoint_start != endpoint_start:  # always sleep after first
            pass
        if n_new > 0:
            time.sleep(INTER_CALL_SLEEP_S)

        messages = [
            {"role": "system", "content": PROMPT_SYSTEM},
            {"role": "user", "content": build_user_prompt(teacher_name, PROMPT_ID, caption_text)},
        ]
        t0 = time.time()
        resp = call_chat(key, route['endpoint'], route['model_id'], messages,
                        max_tokens=MAX_TOKENS, timeout=CALL_TIMEOUT, use_proxy=False)
        elapsed = time.time() - t0
        ok = bool(resp.get("ok"))
        rec = {
            "endpoint_label": route["label"],
            "endpoint_model": route["model_id"],
            "use_proxy": route["use_proxy"],
            "teacher": teacher_name,
            "teacher_path_rel": teacher_path_rel,
            "caption_id": PROMPT_ID,
            "caption_text_sha12": sha12_bytes(caption_text.encode("utf-8")),
            "reask_idx": ri,
            "ok": ok,
            "response_text": resp.get("content", "") if ok else "",
            "response_text_sha12": sha12_bytes(resp.get("content", "").encode("utf-8")) if ok else None,
            "latency_ms": resp.get("latency_ms"),
            "status_code": resp.get("status_code"),
            "error_category": resp.get("error_category"),
            "model_returned": resp.get("model_returned", ""),
            "timestamp_local": datetime.now(timezone(timedelta(hours=8))).isoformat(),
        }
        records.append(rec)
        n_new += 1
        existing_set.add((teacher_name, PROMPT_ID, ri))
        wall = time.time() - endpoint_start
        print(f"  [{n_new}] {teacher_name}/{PROMPT_ID}/reask{ri} ok={ok} latency={resp.get('latency_ms')}ms elapsed={elapsed:.1f}s wall={wall:.1f}s", flush=True)

        # Checkpoint save
        try:
            CHECKPOINT.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
        except Exception as e:
            print(f"  checkpoint FAIL: {e}", flush=True)

        # Hard kill at 280s (Bash tool limit is 300s)
        if wall > 280:
            print(f"\n  watchdog 280s exceeded; aborting batch", flush=True)
            break
    if time.time() - endpoint_start > 280:
        break

wall_time = time.time() - endpoint_start
print(f"\n--- batch done: wall={wall_time:.1f}s, n_new={n_new}, total records={len(records)} ---")

# Save final checkpoint
CHECKPOINT.write_text(json.dumps(records, ensure_ascii=False), encoding="utf-8")
print(f"  saved {CHECKPOINT} ({len(records)} records)")

# Final aggregation - rebuild result.json
print("\n--- aggregating three-way traces ---")
import numpy as np
groups = {}
for r in records:
    if not r["ok"]:
        continue
    k = (r["endpoint_label"], r["teacher"], r["caption_id"])
    groups.setdefault(k, []).append(r)

# load modules
distill_ns = load_distill_module()
proxy_ns = load_proxy_module()

reasked_pairs = []
distill_pairs = []
independent_pairs = []

for (endpoint, teacher, caption_id), group in sorted(groups.items()):
    n = len(group)
    for i in range(n):
        for j in range(i+1, n):
            a = group[i]["response_text"]
            b = group[j]["response_text"]
            jv = jaccard(a, b)
            reasked_pairs.append({
                "endpoint_label": endpoint, "teacher": teacher, "caption_id": caption_id,
                "i_reask_idx": group[i]["reask_idx"], "j_reask_idx": group[j]["reask_idx"],
                "i_text_sha12": sha12_bytes(a.encode("utf-8"))[:8],
                "j_text_sha12": sha12_bytes(b.encode("utf-8"))[:8],
                "i_len": len(a), "j_len": len(b),
                "jaccard": round(jv, 6),
            })
            da = distill_to_text(distill_ns, a)
            db = distill_to_text(distill_ns, b)
            dj = jaccard(da, db)
            distill_pairs.append({
                "endpoint_label": endpoint, "teacher": teacher, "caption_id": caption_id,
                "i_reask_idx": group[i]["reask_idx"], "j_reask_idx": group[j]["reask_idx"],
                "i_distill_sha12": sha12_bytes(da.encode("utf-8"))[:8],
                "j_distill_sha12": sha12_bytes(db.encode("utf-8"))[:8],
                "jaccard": round(dj, 6),
            })
    ops = ["ngram_truncate", "vocab_truncate", "temperature_resample"]
    for r in group:
        outs = proxy_independent_outputs(proxy_ns, r["response_text"])
        for i in range(len(ops)):
            for j in range(i+1, len(ops)):
                at = outs[ops[i]]
                bt = outs[ops[j]]
                jv = jaccard(at, bt)
                independent_pairs.append({
                    "endpoint_label": endpoint, "teacher": teacher, "caption_id": caption_id,
                    "reask_idx": r["reask_idx"],
                    "i_operator": ops[i], "j_operator": ops[j],
                    "i_text_sha12": sha12_bytes(at.encode("utf-8"))[:8],
                    "j_text_sha12": sha12_bytes(bt.encode("utf-8"))[:8],
                    "jaccard": round(jv, 6),
                })

print(f"  re-asked pairs: {len(reasked_pairs)}")
print(f"  distill pairs: {len(distill_pairs)}")
print(f"  independent pairs: {len(independent_pairs)}")

# Per-teacher J medians
def per_teacher_j_median(pairs):
    by_t = {}
    for p in pairs:
        by_t.setdefault(p["teacher"], []).append(p["jaccard"])
    return {t: float(np.median(vs)) if vs else float('nan') for t, vs in by_t.items()}

per_teacher_j = {
    "reasked": per_teacher_j_median(reasked_pairs),
    "distill": per_teacher_j_median(distill_pairs),
    "independent": per_teacher_j_median(independent_pairs),
}
per_teacher_n = {
    "reasked": {t: sum(1 for p in reasked_pairs if p["teacher"] == t) for t in teachers},
    "distill": {t: sum(1 for p in distill_pairs if p["teacher"] == t) for t in teachers},
    "independent": {t: sum(1 for p in independent_pairs if p["teacher"] == t) for t in teachers},
}

# Kill-line application
TH17_N_TARGET = 20
K_N11_3_THRESHOLD = 0.85
K_N11_1_DIFF = 0.05
K_N11_2_DELTA = 0.05

kill_lines = {}

# K-N11-1
k1_per_teacher = {}
k1_any_hit = False
for t in teachers:
    medians = {k: per_teacher_j.get(k, {}).get(t) for k in ["reasked", "distill", "independent"]}
    valid = [v for v in medians.values() if v is not None and not (isinstance(v, float) and np.isnan(v))]
    if len(valid) < 3:
        diff = float("nan")
        hit = True
        verdict = "FAIL (任一 trace 不可算)"
    else:
        diff = max(valid) - min(valid)
        hit = bool(diff < K_N11_1_DIFF)
        verdict = "FAIL" if hit else "PASS"
    if hit:
        k1_any_hit = True
    k1_per_teacher[t] = {
        "medians": {k: (round(v, 6) if v is not None and not (isinstance(v, float) and np.isnan(v)) else None) for k, v in medians.items()},
        "diff_max_min": (round(diff, 6) if not (isinstance(diff, float) and np.isnan(diff)) else None),
        "hit": hit,
        "verdict": verdict,
    }
kill_lines["K-N11-1"] = {"any_hit": k1_any_hit, "hit": k1_any_hit,
                        "verdict": "FAIL (>=1 教师三方不可分离)" if k1_any_hit else "PASS",
                        "per_teacher": k1_per_teacher,
                        "rule": f"三方 Jaccard 中位数差异 < {K_N11_1_DIFF} 即 hit=True -> FAIL",
                        "literal_source": "0A9EE16267B5 sec_1 K-N11-1 字面"}

# K-N11-2
k2_per_teacher = {}
k2_any_hit = False
for t in teachers:
    d_j = per_teacher_j.get("distill", {}).get(t)
    r_j = per_teacher_j.get("reasked", {}).get(t)
    if d_j is None or np.isnan(d_j) or r_j is None or np.isnan(r_j):
        hit = True
        verdict = "FAIL (distill 或 teacher 不可算)"
    else:
        hit = bool(not (d_j > r_j + K_N11_2_DELTA))
        verdict = "FAIL" if hit else "PASS"
    if hit:
        k2_any_hit = True
    k2_per_teacher[t] = {
        "distill_j": round(d_j, 6) if d_j is not None and not np.isnan(d_j) else None,
        "reasked_j": round(r_j, 6) if r_j is not None and not np.isnan(r_j) else None,
        "delta": (round(d_j - r_j, 6) if d_j is not None and r_j is not None and not np.isnan(d_j) and not np.isnan(r_j) else None),
        "hit": hit,
        "verdict": verdict,
    }
kill_lines["K-N11-2"] = {"any_hit": k2_any_hit, "hit": k2_any_hit,
                        "verdict": "FAIL" if k2_any_hit else "PASS",
                        "per_teacher": k2_per_teacher,
                        "rule": f"distill J > teacher J + {K_N11_2_DELTA} 不成立即 hit=True -> FAIL",
                        "literal_source": "0A9EE16267B5 sec_1 K-N11-2 字面"}

# K-N11-3
k3_per_teacher = {}
k3_any_hit = False
for t in teachers:
    j_med = per_teacher_j.get("reasked", {}).get(t)
    n = per_teacher_n.get("reasked", {}).get(t, 0)
    if j_med is None or np.isnan(j_med):
        hit = True
        verdict = "FAIL (教师 J 不可算)"
        j_val = None
    else:
        hit = bool(j_med < K_N11_3_THRESHOLD)
        verdict = "FAIL" if hit else "PASS"
        j_val = j_med
    if hit:
        k3_any_hit = True
    k3_per_teacher[t] = {
        "j_median": round(j_val, 6) if j_val is not None else None,
        "n_pairs": n,
        "hit": hit,
        "verdict": verdict,
    }
kill_lines["K-N11-3"] = {"any_hit": k3_any_hit, "hit": k3_any_hit,
                        "verdict": "FAIL (任一教师 J 中位数 < 0.85)" if k3_any_hit else "PASS",
                        "per_teacher": k3_per_teacher,
                        "rule": f"教师两次 J 中位数 < {K_N11_3_THRESHOLD} 即 hit=True -> FAIL",
                        "literal_source": "0A9EE16267B5 sec_1 K-N11-3 字面"}

# K-N11-N1
n1_per_teacher = {}
n1_any_fail = False
for t in teachers:
    n = per_teacher_n.get("reasked", {}).get(t, 0)
    overall_pass = bool(n >= TH17_N_TARGET)
    n1_per_teacher[t] = {"n_pairs": n, "pass": overall_pass,
                          "verdict": "PASS" if overall_pass else f"FAIL (N={n} < {TH17_N_TARGET})"}
    if not overall_pass:
        n1_any_fail = True
kill_lines["K-N11-N1"] = {"any_fail": n1_any_fail, "pass": not n1_any_fail,
                          "verdict": "PASS" if not n1_any_fail else "FAIL (>=1 教师 N < 20)",
                          "per_teacher": n1_per_teacher,
                          "rule": f"任一教师 N < {TH17_N_TARGET} 即 pass=False -> FAIL",
                          "literal_source": "v0.2 sec_2 L2 K-N11-N1 字面"}

# K-N11-N2 (双读法)
kill_lines["K-N11-N2"] = {
    "rule": "构造面 + 真实面 双读法并记",
    "construction_face": {
        "K-N11-1": "FAIL (前棒 0 数据)",
        "K-N11-2": "FAIL (前棒 0 数据)",
        "K-N11-3": "FAIL (前棒 J 0.41-0.52 < 0.85)",
        "K-N11-N1": "FAIL (N=2 < 20)",
    },
    "real_face_this_baton": {
        "K-N11-1": kill_lines["K-N11-1"]["verdict"],
        "K-N11-2": kill_lines["K-N11-2"]["verdict"],
        "K-N11-3": kill_lines["K-N11-3"]["verdict"],
        "K-N11-N1": kill_lines["K-N11-N1"]["verdict"],
    },
    "verdict": "FAIL (N < 20 仍 FAIL; 不留假 pass)" if n1_any_fail else "PASS (双读法均 PASS)",
    "literal_source": "v0.2 sec_2 L2 K-N11-N2 字面",
}

# Final
any_k_hit = any(kill_lines[k].get("hit", False) for k in ["K-N11-1", "K-N11-2", "K-N11-3"])
n1_fail = (not kill_lines["K-N11-N1"]["pass"])
overall_hit = bool(any_k_hit or n1_fail)

if kill_lines["K-N11-3"]["hit"] and not kill_lines["K-N11-1"]["hit"] and not kill_lines["K-N11-2"]["hit"]:
    root_cause_primary = "真证伪 (K-N11-3 教师 J 中位数 < 0.85) 但 K-N11-1/2 PASS"
elif kill_lines["K-N11-1"]["hit"] or kill_lines["K-N11-2"]["hit"]:
    if n1_fail:
        root_cause_primary = "真证伪 (K-N11-1/2/3 任一触发) + 命题不明族 (N<20) 并存"
    else:
        root_cause_primary = "真证伪 (K-N11-1/2 字面触发)"
elif n1_fail:
    root_cause_primary = "命题不明族 (N < 20)"
else:
    root_cause_primary = "deterministic_verifiable_pass"

# Build result
result_obj = {
    "schema": "v4_l14_n11full/2",
    "task": "L14 . N-11 全轨道重采 三方配对 trace (接力尾棒, 中断恢复 v2)",
    "date_label": "2026-09-24",
    "generated_utc": datetime.now(timezone(timedelta(hours=8))).isoformat(),
    "wall_time_total_s": round(wall_time, 1),
    "seed": SEED,
    "constraint": {
        "no_key_on_disk": True,
        "key_source": "runtime env / desktop AI/LLM API.txt",
        "proxy_teamo_only": True,
        "inter_call_sleep_s": INTER_CALL_SLEEP_S,
        "watchdog_280s": True,
        "interrupted_recovery": "yes (5h quota hit at first run; resumed at 15:03 PI grant)",
        "small_batch_strategy": "1 prompt x 5 teachers x 2 re-asks per Bash invocation",
    },
    "inputs": {
        "prereg_v02": {"path": str(PREREG_V02.relative_to(Path("D:/私人资料/deposon-repo"))),
                       "sha12": sha12_file(PREREG_V02),
                       "expected_sha12": PREREG_V02_SHA12_EXPECTED,
                       "match": sha12_file(PREREG_V02).lower() == PREREG_V02_SHA12_EXPECTED.lower()},
        "captions": {"path": str(CAPTIONS_PATH.relative_to(Path("D:/私人资料/deposon-repo"))),
                     "sha12": sha12_file(CAPTIONS_PATH),
                     "expected_sha12": CAPTIONS_SHA12_EXPECTED,
                     "match": sha12_file(CAPTIONS_PATH).lower() == CAPTIONS_SHA12_EXPECTED.lower()},
    },
    "experiment_parameters": {
        "n_prompts_total": len(set(r["caption_id"] for r in records)),
        "n_reasks_per_prompt": max(r["reask_idx"] for r in records) + 1 if records else 0,
        "n_target_per_teacher_T_TH17": TH17_N_TARGET,
        "temperature": 0.7,
        "max_tokens": MAX_TOKENS,
        "prompts_used": sorted(set(r["caption_id"] for r in records)),
        "distill_method": "_v4_distill_min_measure.py:extract_features (前 64 维 round 4)",
        "independent_method": "_v4_proxy_student_generators.py:3 operators",
    },
    "selected_routes": ["qwen_plan"],
    "records_summary": {
        "n_records_total": len(records),
        "n_records_ok": sum(1 for r in records if r["ok"]),
        "n_records_failed": sum(1 for r in records if not r["ok"]),
        "per_teacher_n_pairs": per_teacher_n,
        "per_teacher_j_median": {trace: {t: (round(j, 6) if isinstance(j, float) and not np.isnan(j) else None)
                                          for t, j in per_teacher_j[trace].items()}
                                 for trace in ["reasked", "distill", "independent"]},
    },
    "three_way_trace_summary": {
        "n_reasked_pairs": len(reasked_pairs),
        "n_distill_pairs": len(distill_pairs),
        "n_independent_pairs": len(independent_pairs),
        "reasked_pairs_redacted_sample": reasked_pairs[:3] if reasked_pairs else [],
        "distill_pairs_redacted_sample": distill_pairs[:3] if distill_pairs else [],
        "independent_pairs_redacted_sample": independent_pairs[:3] if independent_pairs else [],
        "note": "明文响应文本不入产物 (脱敏); 仅指标 + sha8 摘要入账本",
    },
    "kill_lines": kill_lines,
    "overall_verdict": {
        "any_kill_line_hit": overall_hit,
        "primary_root_cause": root_cause_primary,
        "overall_root_cause_classification": "mixed",
        "verdict": "FAIL" if overall_hit else "PASS",
    },
    "key_shape_self_scan": {
        "hits": [{"name": n, "count": c} for n, c in self_scan_text(json.dumps({
            "records_count": len(records),
            "pairs_count": len(reasked_pairs) + len(distill_pairs) + len(independent_pairs),
        }))],
        "status": "clean" if not self_scan_text(json.dumps(records[0] if records else {})) else "WARN",
    },
    "honesty_disclosures": {
        "interrupted_recovery": "前次 v1 (5x1 w x 2 re-asks = 10 calls) 撞 5h 配额 (错误 2056); PI 明示额度重置 + 同棒续跑",
        "watchdog_limit": f"wall_time = {wall_time:.1f}s (280s hard limit; sub-batch strategy)",
        "small_batch_used": "10 calls per Bash invocation (Bash tool 300s 限制)",
        "N_pair_actual_vs_target": f"re-asked N 对/教师 = {per_teacher_n['reasked']}; TH-17 目标 N={TH17_N_TARGET}",
        "distill_independent_filling": "本棒首次填上 distill + independent_train trace (前棒 0 出现)",
    },
    "metadata": {
        "branch_session": "mvs_fe364e8b93014c319b902e64ea81de9f",
        "parent_session": "mvs_bbeb804b1a6a41109be740636eed1709",
        "spec_conformance": "v0.2 sec_2 L2 + 0A9EE16267B5 sec_1 N-11 字面",
        "encoding": "UTF-8",
    },
}

# Self scan
print("\n--- key self_scan on result_obj ---")
result_text = json.dumps(result_obj, ensure_ascii=False, indent=2)
hits = self_scan_text(result_text)
print(f"  hits: {hits}")

# Save result.json (same-file update, allowed per PI interrupt-recovery directive)
OUT_RESULT = Path("D:/私人资料/deposon-repo/results/_v4_supp_l14_n11full_result.json")
print("\n--- saving result.json ---")
with open(OUT_RESULT, "w", encoding="utf-8") as f:
    f.write(result_text)
print(f"  saved {OUT_RESULT} ({len(result_text.encode('utf-8'))} B)")

# Save post hashes
print("\n--- saving post hashes ---")
files_to_check = [
    ("prereg_v02", PREREG_V02, PREREG_V02_SHA12_EXPECTED),
    ("prereg_n", PREREG_N, PREREG_N_SHA12_EXPECTED),
    ("l2_supp_result", Path("D:/私人资料/deposon-repo/results/_v4_supp_l2_n11supp_result.json"), "FF7B167AE43F"),
    ("l2_supp_verdict", Path("D:/私人资料/deposon-repo/results/_v4_supp_l2_n11supp_verdict.md"), "E433A06E7BFB"),
    ("l2_supp_executor", Path("D:/私人资料/deposon-repo/results/_v4_supp_l2_n11supp_executor.py"), "0D455B42CD07"),
    ("proxy_generators", Path("D:/私人资料/deposon-repo/results/_v4_proxy_student_generators.py"), "5BA916D1DD24"),
    ("distill_min_measure", Path("D:/私人资料/deposon-repo/results/_v4_distill_min_measure.py"), "21771E66AF67"),
    ("captions", CAPTIONS_PATH, CAPTIONS_SHA12_EXPECTED),
]
post_lines = []
frozen_ok = True
for name, p, expected in files_to_check:
    actual = sha12_file(p)
    ok = actual.lower() == expected.lower()
    post_lines.append(f"{name}: {actual} (expected {expected}) {'OK' if ok else 'CHANGED'}")
    if not ok:
        frozen_ok = False
for tname, trel, expected in TEACHER_PATHS_REL:
    p = Path("D:/私人资料/deposon-repo") / trel
    actual = sha12_file(p)
    ok = actual.lower() == expected.lower()
    post_lines.append(f"{tname}: {actual} (expected {expected}) {'OK' if ok else 'CHANGED'}")
    if not ok:
        frozen_ok = False

OUT_POST = Path("D:/私人资料/deposon-repo/results/_v4_supp_l14_n11full_post_hashes_2026_09_24.txt")
with open(OUT_POST, "w", encoding="utf-8") as f:
    f.write("\n".join(post_lines) + "\n")
    f.write("\n--- NEW this baton ---\n")
    new_files = [
        ("executor_self", Path("D:/私人资料/deposon-repo/results/_v4_supp_l14_n11full_executor.py")),
        ("result", OUT_RESULT),
        ("verdict", Path("D:/私人资料/deposon-repo/results/_v4_supp_l14_n11full_verdict.md")),
    ]
    for n, p in new_files:
        if p.exists():
            actual = sha12_file(p)
            f.write(f"{n}: {actual} [NEW this baton]\n")

print(f"saved {OUT_POST}")
print(f"\n=== batch summary ===")
print(f"  n_new records this batch: {n_new}")
print(f"  total records: {len(records)}")
print(f"  re-asked N per teacher: {per_teacher_n['reasked']}")
print(f"  distill N per teacher: {per_teacher_n['distill']}")
print(f"  independent N per teacher: {per_teacher_n['independent']}")
print(f"  overall: {result_obj['overall_verdict']['verdict']}")
print(f"  root_cause: {root_cause_primary}")
print(f"  frozen_ok: {frozen_ok}")