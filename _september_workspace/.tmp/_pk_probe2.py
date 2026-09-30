import json
p = r"D:/私人资料/deposon-repo/results/_v3_recheck_08c_preexp_data/result_2026_09_27.json"
d = json.load(open(p, encoding="utf-8"))
print("=== fixtures ===")
print(json.dumps(d["fixtures"], ensure_ascii=False, indent=1)[:2000])
print("=== runs[0] keys ===")
r0 = d["runs"][0]
print(json.dumps(r0, ensure_ascii=False, indent=1)[:2500])
