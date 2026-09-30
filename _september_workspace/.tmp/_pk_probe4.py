import json
p = r"D:/私人资料/deposon-repo/results/_v3_recheck_08b_executor/result_2026_09_27.json"
d = json.load(open(p, encoding="utf-8"))
print("TOP:", list(d.keys()))
