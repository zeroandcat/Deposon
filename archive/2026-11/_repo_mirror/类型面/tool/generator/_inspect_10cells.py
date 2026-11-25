#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inspect 10 cells L14V3 quadruples + per_call_metadata structure
"""
import json
import os
import hashlib

files = {
    "teacher_kimi":    "results/_v4_supp_l14v3_batch1_r6_result.json",
    "teacher_GLM_1":   "results/_v4_supp_l14v3_batch2_r5_result.json",
    "teacher_GLM_2":   "results/_v4_supp_l14v3_batch3_r5_result.json",
    "teacher_coze":    "results/_v4_supp_l14v3_batch4_r6_result.json",
    "teacher_minimax": "results/_v4_supp_l14v3_batch5_r5_result.json",
    "distill_kimi":    "results/_v4_supp_l14v3_batch6_r5_result.json",
    "distill_GLM_1":   "results/_v4_supp_l14v3_batch7_r5_result.json",
    "distill_GLM_2":   "results/_v4_supp_l14v3_batch8_r5_result.json",
    "distill_coze":    "results/_v4_supp_l14v3_batch9_r5_result.json",
    "distill_minimax": "results/_v4_supp_l14v3_batch10_r5_result.json",
}

print(f"{'cell':20s} {'SHA-12':12s} {'bytes':>7s} {'quads':>6s} {'ok':>5s} {'empty':>6s} {'schema'}")
print("-" * 90)
for k, fp in files.items():
    if not os.path.exists(fp):
        print(f"MISSING: {k} -> {fp}")
        continue
    sz = os.path.getsize(fp)
    h = hashlib.sha256(open(fp, 'rb').read()).hexdigest()[:12]
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    quads = d.get('quadruples', [])
    schema = d.get('schema', '?')
    n_ok = sum(1 for q in quads if q.get('per_call_metadata', {}).get('ok', False))
    n_empty = sum(1 for q in quads if q.get('per_call_metadata', {}).get('empty_response', False))
    print(f"{k:20s} {h:12s} {sz:7d} {len(quads):6d} {n_ok:5d} {n_empty:6d} {schema}")

print()
print("=== per_call_metadata key union ===")
key_union = set()
for k, fp in files.items():
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for q in d.get('quadruples', []):
        m = q.get('per_call_metadata', {})
        if isinstance(m, dict):
            key_union.update(m.keys())
print(f"keys = {sorted(key_union)}")
print(f"count = {len(key_union)}")

print()
print("=== usage keys union ===")
uk = set()
for k, fp in files.items():
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    for q in d.get('quadruples', []):
        u = q.get('per_call_metadata', {}).get('usage', {})
        if isinstance(u, dict):
            uk.update(u.keys())
print(f"usage keys = {sorted(uk)}")