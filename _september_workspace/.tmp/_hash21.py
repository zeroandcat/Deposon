import hashlib, json
for p in ("results/_v5_item21_anchor_recompute_2026_09_28.json",
          "results/_v5_item21_anchor_recompute_2026_09_28.md"):
    b = open(p, "rb").read()
    print(p, "bytes=%d" % len(b), "sha12=%s" % hashlib.sha256(b).hexdigest()[:12])
# JSON 合法性 + 关键断言
d = json.load(open("results/_v5_item21_anchor_recompute_2026_09_28.json", encoding="utf-8"))
ar = d["anchor_readings"]
print("anchor_executable_flags:", [ar[k]["executable"] for k in ("B1_Sinkhorn_OT","B2_KD","B3_LLMLingua")])
print("anchor_readings_all_null:", all(ar[k]["reading"] is None for k in ("B1_Sinkhorn_OT","B2_KD","B3_LLMLingua")))
print("anchor_sha_pre_eq_post:", all(ar[k]["anchor_sha12_pre"]==ar[k]["anchor_sha12_post"] for k in ("B1_Sinkhorn_OT","B2_KD","B3_LLMLingua")))
dr = d["drift_recompute_for_comparison"]
print("drift_bitwise_all_true:", all(dr[k]["bitwise_identical"] for k in ("B1_Sinkhorn_OT","B2_KD","B3_LLMLingua")))
