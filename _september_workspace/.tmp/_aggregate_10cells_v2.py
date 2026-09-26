#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Aggregate 10 cells quadruples correctly:
- For each cell, aggregate from all relevant rounds
- kimi teacher = batch1 r2+r3+r4+r5 (side=teacher)
- kimi distill = batch1 r6 + batch6 r1-r5 (side=distill)  -- but batch6 = distill 接力
- For other cells: batchN_r1-r5 (teacher side) + batch(N+5)_r1-r5 (distill side)
"""
import json
import os
import hashlib

# 10 cells = teacher/distill × 5 teachers
# Per the mapping + cumulative:
# teacher side: batch1_r2-r5 (kimi), batch2_r1-r5 (GLM_1), batch3_r1-r5 (GLM_2),
#               batch4_r1-r6 (coze, 110+r6sup=111), batch5_r1-r5 (minimax)
# distill side: batch1_r6 + batch6_r1-r5 (kimi), batch7_r1-r5 (GLM_1), batch8_r1-r5 (GLM_2),
#               batch9_r1-r5 (coze), batch10_r1-r5 (minimax)
#
# But wait: kimi has a quirk. Let me check all rounds
def all_rounds(batch):
    rounds = []
    for r in range(1, 8):
        for suffix in ['', '_result']:
            pass
        fp = f'results/_v4_supp_{batch}_r{r}_result.json'
        if os.path.exists(fp):
            rounds.append(fp)
    return rounds

# Teacher side files (where metadata.side == 'teacher' OR round label indicates teacher)
# Easier: rely on per-call metadata side field
def agg_by_side(file_list):
    teacher_quads = []
    distill_quads = []
    for fp in file_list:
        if not os.path.exists(fp):
            continue
        with open(fp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        for q in d.get('quadruples', []):
            side = q.get('per_call_metadata', {}).get('side')
            if side == 'teacher':
                teacher_quads.append(q)
            elif side == 'distill':
                distill_quads.append(q)
    return teacher_quads, distill_quads

# 10 cells: (batch_prefix, teacher_label)
cells_def = {
    "teacher_kimi":    "batch1",
    "teacher_GLM_1":   "batch2",
    "teacher_GLM_2":   "batch3",
    "teacher_coze":    "batch4",
    "teacher_minimax": "batch5",
    "distill_kimi":    "batch6",
    "distill_GLM_1":   "batch7",
    "distill_GLM_2":   "batch8",
    "distill_coze":    "batch9",
    "distill_minimax": "batch10",
}

# For teacher_kimi: it includes batch1 r2-r6 (since batch1 r6 might still be teacher side... but we saw r6=distill)
# Let me check what batch1 r6 actually contains

# kimi teacher: batch1 r2-r5 (r6 = distill)
# kimi distill: batch1 r6 + batch6 r1-r5 (since batch6 = distill 接力)
# Actually let's be precise: check each batch's metadata.side vs quadruples side

cells_data = {}
for cell_name, batch_prefix in cells_def.items():
    # Determine which rounds to look at
    rounds = all_rounds(batch_prefix)
    t_qs, d_qs = agg_by_side(rounds)
    # For teacher_kimi cell: take teacher-side quads from batch1
    # For distill_kimi cell: take distill-side quads from batch6 + batch1 r6 (if r6 has distill side)
    is_teacher = cell_name.startswith('teacher_')
    teacher_label = cell_name.split('_', 1)[1]
    if is_teacher:
        qs = t_qs  # teacher-side from this batch
    else:
        # distill side from this batch's rounds + maybe from previous batch's tail
        qs = d_qs
        # For distill_kimi: also include batch1 r6 (since batch1 ends with distill side)
        if batch_prefix == 'batch6':
            for r in range(1, 8):
                fp = f'results/_v4_supp_batch1_r{r}_result.json'
                if os.path.exists(fp):
                    with open(fp, 'r', encoding='utf-8') as f:
                        d = json.load(f)
                    for q in d.get('quadruples', []):
                        if q.get('per_call_metadata', {}).get('side') == 'distill':
                            qs.append(q)
    # Filter to keep only those with teacher_label == cell's teacher
    qs = [q for q in qs
          if (q.get('per_call_metadata', {}).get('teacher_label') == teacher_label
              or q.get('per_call_metadata', {}).get('teacher') == teacher_label
              or q.get('prompt_id', '').split('_t')[0:1])]  # fallback to prompt_id prefix
    # Use prompt_id as primary filter: e.g. 'kimi_t01_teacher_*' or 'kimi_t01_distill_*'
    prompt_prefix_teacher = f'{teacher_label.lower().replace("-","_")}_t'
    qs = [q for q in qs if prompt_prefix_teacher in q.get('prompt_id', '').lower()]
    cells_data[cell_name] = qs

print(f"{'cell':20s} {'quads':>6s} {'ok':>5s} {'empty':>6s} {'caption_set':>5s}")
for cell, qs in cells_data.items():
    ok = sum(1 for q in qs if q.get('per_call_metadata', {}).get('ok'))
    empty = sum(1 for q in qs if q.get('per_call_metadata', {}).get('empty_response'))
    cs = set(q.get('per_call_metadata', {}).get('caption_id') for q in qs)
    print(f"{cell:20s} {len(qs):6d} {ok:5d} {empty:6d} {len(cs):5d}")

# Save
with open('.tmp/_l14v3_aggregated_10cells_v2.json', 'w', encoding='utf-8') as f:
    json.dump(cells_data, f, ensure_ascii=False, indent=2)
sz = os.path.getsize('.tmp/_l14v3_aggregated_10cells_v2.json')
h = hashlib.sha256(open('.tmp/_l14v3_aggregated_10cells_v2.json','rb').read()).hexdigest()[:12]
print(f"\nSaved .tmp/_l14v3_aggregated_10cells_v2.json ({sz} B, SHA-12={h})")