import json
p = r"D:/私人资料/deposon-repo/results/_v3_recheck_08b_executor/result_2026_09_27.json"
d = json.load(open(p, encoding="utf-8"))
print("=== controls keys ===", list(d["controls"].keys()) if isinstance(d["controls"],dict) else type(d["controls"]))
s=json.dumps(d["controls"], ensure_ascii=False, indent=1)
print(s[:3500])
