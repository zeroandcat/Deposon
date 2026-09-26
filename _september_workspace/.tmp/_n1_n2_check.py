#!/usr/bin/env python3
import json
import os

PREFIX = '_v4_supp_l14v3_'

# Check N1/N2 observability across 10 cells
# Each cell's terminal round:
terminal_rounds = {
    "teacher_kimi":    "batch1_r6",  # actually r6 = distill; teacher side = r5
    "teacher_GLM_1":   "batch2_r5",
    "teacher_GLM_2":   "batch3_r5",
    "teacher_coze":    "batch4_r6",
    "teacher_minimax": "batch5_r5",
    "distill_kimi":    "batch6_r5",
    "distill_GLM_1":   "batch7_r5",
    "distill_GLM_2":   "batch8_r5",
    "distill_coze":    "batch9_r5",
    "distill_minimax": "batch10_r5",
}

print(f"{'cell':20s} {'round':14s} {'K_N26_1_comp':14s} {'K_N26_2_comp':14s} {'cumul_empty_rate':18s} {'teamo_tun':10s} {'n1_note'}")
print('-' * 130)
for cell, r in terminal_rounds.items():
    fp = f'results/{PREFIX}{r}_result.json'
    if not os.path.exists(fp):
        print(f'  {cell:20s} {r}: MISSING')
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    obs = d.get('K_N26_observability_only', {})
    k1 = obs.get('K_N26_1_computed')
    k2 = obs.get('K_N26_2_computed')
    n1 = obs.get('K_N26_N1_observation', {})
    n2 = obs.get('K_N26_N2_observation', {})
    rate = n2.get('cumulative_empty_response_rate')
    tun = n2.get('teamo_tun_used_for_all_calls')
    n1_note = n1.get('round_6_n_distinct_sample_note') or n1.get('round_5_n_distinct_sample_note') or n1.get('round_3_n_distinct_sample_note') or str(n1)
    n1_note_short = (n1_note[:50] + '...') if len(n1_note) > 50 else n1_note
    print(f"  {cell:20s} {r:14s} {str(k1):14s} {str(k2):14s} {str(rate):18s} {str(tun):10s} {n1_note_short}")