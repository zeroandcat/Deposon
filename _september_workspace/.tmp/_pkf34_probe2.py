import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
db = json.load(open(CB, encoding='utf-8'))
print('TOP', list(db.keys()))
print('=== controls keys ===')
print(list(db.get('controls', {}).keys()) if isinstance(db.get('controls'), dict) else type(db.get('controls')))
c = db.get('controls')
if isinstance(c, dict):
    for k, v in c.items():
        print('---', k, type(v).__name__, len(v) if isinstance(v,(list,dict)) else '')
        print(json.dumps(v, ensure_ascii=False)[:1600])
