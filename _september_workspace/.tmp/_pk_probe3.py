import json
p = r"D:/私人资料/deposon-repo/results/_v3_recheck_08c_preexp_data/result_2026_09_27.json"
d = json.load(open(p, encoding="utf-8"))
print("=== runs[0] keys ===", list(d["runs"][0].keys()) if isinstance(d["runs"][0],dict) else type(d["runs"][0]))
# find FIX-D entries
for r in d["runs"]:
    if isinstance(r, dict) and str(r.get("fixture_id","")).upper().find("FIX-D")>=0:
        print(json.dumps(r, ensure_ascii=False, indent=1)[:1800]); break
