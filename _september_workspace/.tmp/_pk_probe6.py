import json
p = r"D:/私人资料/deposon-repo/results/_v3_recheck_08b_executor/result_2026_09_27.json"
d = json.load(open(p, encoding="utf-8"))
s=json.dumps(d["controls"]["CTRL2_NOOP_emulation_of_v3_defect"], ensure_ascii=False, indent=1)
print(s[:4000])
