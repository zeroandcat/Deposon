#!/usr/bin/env python3
import json
import os

for r in ['r1','r2','r3','r4','r5','r6']:
    fp = f'results/_v4_supp_l14v3_batch4_{r}_result.json'
    if not os.path.exists(fp):
        print(f'batch4 {r}: MISSING')
        continue
    try:
        with open(fp, 'r', encoding='utf-8') as f:
            d = json.load(f)
        n = len(d.get('quadruples', []))
        agg = d.get('aggregate', {})
        finish = d.get('coze_teacher_side_finish')
        if finish:
            print(f'batch4 {r}: quads={n}, finish_status={finish.get("finish_status")}, all_22_met={finish.get("all_22_captions_met_target")}, total={finish.get("cumulative_calls_total")}, ok={finish.get("cumulative_ok")}, empty={finish.get("cumulative_empty")}')
        else:
            print(f'batch4 {r}: quads={n}, no finish yet, agg={list(agg.keys())[:6]}')
    except Exception as e:
        print(f'batch4 {r}: ERR {e}')