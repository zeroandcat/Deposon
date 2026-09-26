import json
data = json.loads(open('D:/私人资料/deposon-repo/results/_tmp_v2_compare.json', encoding='utf-8').read())
v2 = data['v2_label_dist']
n_distinct = len([k for k in v2.keys() if k != 'UNKNOWN'])
print(f'v2 n_distinct types (excluding UNKNOWN): {n_distinct}')
print(f'v2 n_distinct (including UNKNOWN): {len(v2)}')
print(f'v2 UNK rate: {data["v2_unknown_rate"]:.3f}')
# 退化警报:n_distinct ≤3 即退化
verdict = 'PASS' if (len(v2) > 3 and max(v2.values()) / sum(v2.values()) < 0.85) else 'FAIL'
print(f'degeneracy verdict: {verdict}')
# 看最大类占比
total = sum(v2.values())
max_v = max(v2.values())
max_k = max(v2, key=v2.get)
print(f'max class: {max_k} = {max_v}/{total} = {max_v/total:.3f}')