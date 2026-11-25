#!/usr/bin/env python3
import json
import os
for r in ['r2','r3','r4','r5','r6']:
    fp = f'results/_v4_supp_l14v3_batch1_{r}_result.json'
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    sides = [q.get('per_call_metadata', {}).get('side') for q in d.get('quadruples', [])]
    teachers = [q.get('per_call_metadata', {}).get('teacher_label') for q in d.get('quadruples', [])]
    md = d.get('metadata', {})
    print(f'batch1 {r}: quads={len(sides)}, sides={set(sides)}, teachers={set(teachers)}')
    print(f'  metadata.teacher = {md.get("teacher")}, metadata.side = {md.get("side")}')
    if 'kimi_distill_side_round1_finish' in d:
        print(f'  has kimi_distill_side_round1_finish block')

# Same for batch2 (GLM_1)
print()
print('--- batch2 GLM_1 ---')
for r in ['r1','r2','r3','r4','r5','r6']:
    fp = f'results/_v4_supp_l14v3_batch2_{r}_result.json'
    if not os.path.exists(fp):
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        d = json.load(f)
    sides = [q.get('per_call_metadata', {}).get('side') for q in d.get('quadruples', [])]
    teachers = [q.get('per_call_metadata', {}).get('teacher_label') for q in d.get('quadruples', [])]
    md = d.get('metadata', {})
    print(f'batch2 {r}: quads={len(sides)}, sides={set(sides)}, teachers={set(teachers)}')
    print(f'  metadata.teacher = {md.get("teacher")}, metadata.side = {md.get("side")}')