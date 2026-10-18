"""Show 5 stage summaries"""
import json
for j in [1,2,3,4,5]:
    p = {1: r'D:\私人资料\deposon-repo\results\deposon_v2_phase1_60cells_2026_09_11.json',
         2: r'D:\私人资料\deposon-repo\results\deposon_v2_phase2_f2_2026_09_11.json',
         3: r'D:\私人资料\deposon-repo\results\deposon_v2_phase3_f3_2026_09_11.json',
         4: r'D:\私人资料\deposon-repo\results\deposon_v2_phase4_f4_2026_09_11.json',
         5: r'D:\私人资料\deposon-repo\results\deposon_v2_phase5_f5_2026_09_11.json'}[j]
    d = json.load(open(p,encoding='utf-8'))
    phase = d.get('phase', '?')
    print(f'=== Stage {j}: {phase[:80]} ===')
    if 'summary' in d:
        s = d['summary']
        if 'verdict' in s:
            print('  verdict:', s['verdict'])
        if 'total_passed' in s:
            print('  pass_rate:', s.get('total_passed'), '/', s.get('total_cells'), '=', s.get('pass_rate'))
    for k in ['verdict', 'root_cause', 'best_model', 'pb_verdict']:
        if k in d:
            v = d[k]
            if isinstance(v, dict):
                print(f'  {k}:', json.dumps(v, ensure_ascii=False)[:200])
            else:
                print(f'  {k}:', str(v)[:200])
    print()
