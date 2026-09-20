import json
from collections import defaultdict

d = json.load(open(r'D:\私人资料\deposon-repo\results\deposon_openrouter_5model_rag_30cells_2026_09_10.json', encoding='utf-8'))
rag = d.get('rag_results', [])
print('rag_results total:', len(rag))

by_model = defaultdict(list)
for r in rag:
    by_model[r['model']].append(r)
print('models:', list(by_model.keys()))

for m, rs in by_model.items():
    r0 = rs[0]
    cell = r0['cell_id']
    top3 = (r0.get('top3') or [])[:3]
    pred = r0['pred']
    gt = r0['gt']
    ok = r0['is_correct']
    print(f'  {m}: n={len(rs)}, sample cell={cell}, top3={top3}, pred={pred}, gt={gt}, ok={ok}')

print()
print('per_model:')
for p in d['per_model']:
    print(' ', p)

print()
print('sim ranges per model:')
for m, rs in by_model.items():
    sims = []
    for r in rs:
        for t in (r.get('top3') or []):
            sims.append(t.get('sim', 0))
    if sims:
        print(f'  {m}: n_sims={len(sims)}, min={min(sims):.4f}, max={max(sims):.4f}, mean={sum(sims)/len(sims):.4f}')
