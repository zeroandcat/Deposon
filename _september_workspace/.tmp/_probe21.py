import json, sys
d = json.load(open("results/_v3_recheck_21_result_2026_09_27.json", encoding="utf-8"))
f3 = d["face_3_d_dec"]
out = ["===== face_3 field_availability_audit =====",
       json.dumps(f3.get("field_availability_audit"), ensure_ascii=False, indent=1)[:2500]]
out.append("")
out.append("===== face_3 per_benchmark keys =====")
pb = f3.get("per_benchmark")
out.append(json.dumps({k: (list(v.keys()) if isinstance(v, dict) else v) for k, v in pb.items()},
                      ensure_ascii=False, indent=1)[:1200])
sys.stdout.write("\n".join(out))
