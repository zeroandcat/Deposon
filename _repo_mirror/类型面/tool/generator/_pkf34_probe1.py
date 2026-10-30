import json, io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

C8 = 'results/_v3_recheck_08c_preexp_data/result_2026_09_27.json'
CB = 'results/_v3_recheck_08b_executor/result_2026_09_27.json'
d8 = json.load(open(C8, encoding='utf-8'))
db = json.load(open(CB, encoding='utf-8'))

print('=== 08c fixtures keys ===')
print(json.dumps(d8['fixtures'], ensure_ascii=False)[:1500])
print('=== 08c schemes ===')
print(json.dumps(d8['schemes'], ensure_ascii=False)[:1200])
print('=== 08c runs[0] keys ===')
r0 = d8['runs'][0]
print(list(r0.keys()))
print(json.dumps(r0, ensure_ascii=False)[:2500])
