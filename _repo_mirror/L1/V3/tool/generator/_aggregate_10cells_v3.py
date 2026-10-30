#!/usr/bin/env python3
import json
import os
import hashlib

# 10 cells: teacher / distill × 5 teachers
# batch number mapping:
# teacher_kimi = batch1 r2-r5 (side=teacher); r6 = distill (skip for teacher)
# teacher_GLM_1 = batch2 r1-r5 (or r6)
# teacher_GLM_2 = batch3 r1-r5
# teacher_coze = batch4 r1-r6 (coze special: 6 rounds)
# teacher_minimax = batch5 r1-r5
# distill_kimi = batch1 r6 + batch6 r1-r5 (distill side)
# distill_GLM_1 = batch7 r1-r5
# distill_GLM_2 = batch8 r1-r5
# distill_coze = batch9 r1-r5
# distill_minimax = batch10 r1-r5

def all_rounds(batch):
    rounds = []
    for r in range(1, 10):
        fp = f'results/_v4_supp_{batch}_r{r}_result.json'
        if os.path.exists(fp):
            rounds.append((r, fp))
    return rounds

cells_def = {
    "teacher_kimi":    [("batch1", "teacher", 2, 6)],  # batch1 r2-r5 (teacher side) [r6 is distill]
    "teacher_GLM_1":   [("batch2", "teacher", 1, 7)],
    "teacher_GLM_2":   [("batch3", "teacher", 1, 7)],
    "teacher_coze":    [("batch4", "teacher", 1, 7)],
    "teacher_minimax": [("batch5", "teacher", 1, 7)],
    "distill_kimi":    [("batch1", "distill", 6, 7), ("batch6", "distill", 1, 7)],  # batch1 r6 + batch6 r1-r5
    "distill_GLM_1":   [("batch7", "distill", 1, 7)],
    "distill_GLM_2":   [("batch8", "distill", 1, 7)],
    "distill_coze":    [("batch9", "distill", 1, 7)],
    "distill_minimax": [("batch10", "distill", 1, 7)],
}

cells_data = {}
for cell_name, sources in cells_def.items():
    qs = []
    for batch, expected_side, r_start, r_end in sources:
        for r in range(r_start, r_end):
            fp = f'results/_v4_supp_{batch}_r{r}_result.json'
            if not os.path.exists(fp):
                continue
            with open(fp, 'r', encoding='utf-8') as f:
                d = json.load(f)
            for q in d.get('quadruples', []):
                side = q.get('per_call_metadata', {}).get('side')
                if side == expected_side:
                    qs.append(q)
    cells_data[cell_name] = qs

print(f"{'cell':20s} {'quads':>6s} {'ok':>5s} {'empty':>6s} {'captions':>9s} {'model_ids':>10s}")
print('-' * 80)
for cell, qs in cells_data.items():
    ok = sum(1 for q in qs if q.get('per_call_metadata', {}).get('ok'))
    empty = sum(1 for q in qs if q.get('per_call_metadata', {}).get('empty_response'))
    captions = set(q.get('per_call_metadata', {}).get('caption_id') for q in qs)
    models = set(q.get('per_call_metadata', {}).get('model_id_sent', '?') for q in qs)
    print(f"{cell:20s} {len(qs):6d} {ok:5d} {empty:6d} {len(captions):9d} {models}")

# Save
with open('.tmp/_l14v3_aggregated_10cells_v3.json', 'w', encoding='utf-8') as f:
    json.dump(cells_data, f, ensure_ascii=False, indent=2)
sz = os.path.getsize('.tmp/_l14v3_aggregated_10cells_v3.json')
h = hashlib.sha256(open('.tmp/_l14v3_aggregated_10cells_v3.json','rb').read()).hexdigest()[:12]
print(f"\nSaved .tmp/_l14v3_aggregated_10cells_v3.json ({sz} B, SHA-12={h})")