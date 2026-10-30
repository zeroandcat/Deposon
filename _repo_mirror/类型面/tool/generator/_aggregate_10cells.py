#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aggregate 10 cells quadruples from L14V3 batch results.
For teacher_coze: aggregate from batch4_r1-r6 (111 calls).
For other cells: take the final batch's quadruples (22 each, per dispatcher accumulation model).
"""
import json
import os
import hashlib

cells = {
    "teacher_kimi":    ["results/_v4_supp_l14v3_batch1_r6_result.json"],
    "teacher_GLM_1":   ["results/_v4_supp_l14v3_batch2_r5_result.json"],
    "teacher_GLM_2":   ["results/_v4_supp_l14v3_batch3_r5_result.json"],
    "teacher_coze":    ["results/_v4_supp_l14v3_batch4_r1_result.json",
                         "results/_v4_supp_l14v3_batch4_r2_result.json",
                         "results/_v4_supp_l14v3_batch4_r3_result.json",
                         "results/_v4_supp_l14v3_batch4_r4_result.json",
                         "results/_v4_supp_l14v3_batch4_r5_result.json",
                         "results/_v4_supp_l14v3_batch4_r6_result.json"],
    "teacher_minimax": ["results/_v4_supp_l14v3_batch5_r5_result.json"],
    "distill_kimi":    ["results/_v4_supp_l14v3_batch6_r5_result.json"],
    "distill_GLM_1":   ["results/_v4_supp_l14v3_batch7_r5_result.json"],
    "distill_GLM_2":   ["results/_v4_supp_l14v3_batch8_r5_result.json"],
    "distill_coze":    ["results/_v4_supp_l14v3_batch9_r5_result.json"],
    "distill_minimax": ["results/_v4_supp_l14v3_batch10_r5_result.json"],
}

aggregated = {}
for cell, fps in cells.items():
    quads = []
    for fp in fps:
        if not os.path.exists(fp):
            print(f"  WARN {cell}: missing {fp}")
            continue
        with open(fp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        quads.extend(d.get('quadruples', []))
    aggregated[cell] = quads

# print summary
print(f"{'cell':20s} {'quads':>6s} {'ok':>5s} {'empty':>6s} {'fail':>5s} {'n_captions':>11s} {'model_ids'}")
print('-' * 110)
for cell, qs in aggregated.items():
    ok = sum(1 for q in qs if q.get('per_call_metadata', {}).get('ok'))
    empty = sum(1 for q in qs if q.get('per_call_metadata', {}).get('empty_response'))
    fail = sum(1 for q in qs if (not q.get('per_call_metadata', {}).get('ok', False)))
    captions = set(q.get('per_call_metadata', {}).get('caption_id') for q in qs)
    models = set(q.get('per_call_metadata', {}).get('model_id_sent', '?') for q in qs)
    print(f"{cell:20s} {len(qs):6d} {ok:5d} {empty:6d} {fail:5d} {len(captions):11d} {models}")

# save aggregated quadruples to a single combined json for use later
out = {}
for cell, qs in aggregated.items():
    out[cell] = qs
os.makedirs('.tmp', exist_ok=True)
with open('.tmp/_l14v3_aggregated_10cells.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f'\nSaved aggregated 10 cells -> .tmp/_l14v3_aggregated_10cells.json')
sz = os.path.getsize('.tmp/_l14v3_aggregated_10cells.json')
h = hashlib.sha256(open('.tmp/_l14v3_aggregated_10cells.json','rb').read()).hexdigest()[:12]
print(f'  bytes={sz}, SHA-12={h}')