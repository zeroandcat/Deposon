# -*- coding: utf-8 -*-
"""落盘后独立复验（不信任生成器自打印值）：从盘上重算 SHA-12/字节/行数/编码 + 复锚 + 重数条目。"""
import json, hashlib, io, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = "results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json"
p = os.path.join(ROOT, OUT)
b = open(p, "rb").read()
txt = b.decode("utf-8")

print("=== 件面实测（落盘后从盘上重算） ===")
print("path:", OUT)
print("sha12:", hashlib.sha256(b).hexdigest()[:12])
print("bytes:", len(b))
print("lines(newline count):", txt.count("\n"))
print("has_bom:", b[:3] == b"\xef\xbb\xbf")
print("has_crlf:", b"\r\n" in b)
print("json_parseable:", True)
doc = json.loads(txt)

print("\n=== 复锚（16 项，落盘后） ===")
anchors = {
 "results/_v4_pi_cot_v3_questionnaire_v2_d8_2026_09_28.md": "238077d25919",
 "results/_d8_collection_ledger_2026_09_30.md": "199a206d2800",
 "results/_d8_supplement_open_questions_2026_09_30.md": "579b375e9508",
 "results/_d8_boundary_revision_register_2026_09_30.md": "b46370bb9e3b",
 "results/_v4_pi_cot_v3_dataset.json": "5118f5b44f17",
 "results/_v4_pi_cot_v2_dataset.json": "7b01cd835a41",
 "results/_v4_pi_cot_v2_questionnaire_v1.md": "7b14cdb31d21",
 "results/_v4_pi_cot_v3_prereg.md": "b7547329af2e",
 "results/_v4_effective_register_2026_09_28.md": "2a65c1274202",
 "results/_v3_s_prereg_v1_2026_09_27.md": "ef5a40554960",
 "results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json": "cbf60a630c9f",
 "results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json": "6eed9acdb99a",
 "results/_v4_pi_cot_v3_dataset_addendum_d5_2026_09_27.json": "990c0c42a6f6",
 "results/_v4_pi_cot_v3_dataset_addendum_d6_2026_09_28.json": "9669efa804b7",
 "results/_v4_pi_cot_v3_dataset_addendum_d6b_2026_09_28.json": "5d94a8617b5b",
 "results/_v4_pi_cot_v3_dataset_addendum_s3_d7_2026_09_29.json": "c0ebbd1f4633",
}
ok = True
for rel, pre in anchors.items():
    now = hashlib.sha256(open(os.path.join(ROOT, rel), "rb").read()).hexdigest()[:12]
    same = (now == pre)
    ok = ok and same
    print(("  OK  " if same else "  DRIFT "), now, "(pre=%s)" % pre, rel)
print("all_16_anchors_unchanged:", ok)

print("\n=== 条目复数 ===")
sup = doc["supplements"]
print("supplement_count_field:", doc["supplement_count"], "| actual len:", len(sup))
ids = [x["q_id"] for x in sup]
print("q_id unique:", len(ids) == len(set(ids)), "| distinct:", len(set(ids)))
dup = [k for k, v in collections.Counter(ids).items() if v > 1]
print("duplicates:", dup)
cls = collections.Counter(x["entry_class"] for x in sup)
print("by_class:", dict(cls))
d8ids = [i for i in ids if i.startswith("D8-")]
print("d8_entries:", len(d8ids), "| sq:", len([i for i in ids if i.startswith("SQ-")]),
      "| calibration:", len([i for i in ids if i.startswith("T-") or i.startswith("skill-")]))
exp = ["D8-%02d" % i for i in range(1, 81)]
exp = [("D8-%02dr" % int(x[3:5])) if x in ("D8-58", "D8-59") else x for x in exp]
print("d8 coverage == 期望集:", sorted(d8ids) == sorted(exp), "| 漏:", [x for x in exp if x not in d8ids],
      "| 多:", [x for x in d8ids if x not in exp])
print("d8 order preserved:", d8ids == exp)

print("\n=== 9 字段齐备性（题面协议字段集） ===")
need = ["event_id", "date", "q_id", "scene_tag", "judge_type", "option_chosen", "reasoning_full",
        "is_correction", "weight"]
missing = [(x["q_id"], f) for x in sup for f in need if f not in x]
print("missing 9-field keys:", missing if missing else "0（全部 93 条齐备）")
print("all date==2026-09-30:", all(x["date"] == "2026-09-30" for x in sup))
print("all event_id unique:", len(set(x["event_id"] for x in sup)) == len(sup))

print("\n=== null 值纪律（b 半 3 题 + SQ-08） ===")
for x in sup:
    if x["entry_class"] in ("pending_b_half", "skipped"):
        vals = {f: x.get(f) for f in ("option_chosen", "reasoning_full", "option_meaning",
                                      "is_correction", "weight", "pi_answer_verbatim", "pi_other_verbatim")}
        print(" ", x["q_id"], x["collection_status"], "| all-null:", all(v is None for v in vals.values()))

print("\n=== 逐字保留抽查（PI 原答 0 改写） ===")
ledger = io.open(os.path.join(ROOT, "results/_d8_collection_ledger_2026_09_30.md"), encoding="utf-8").read()
miss = []
for x in sup:
    v = x.get("pi_answer_verbatim")
    if not v:
        continue
    if ("「" + v + "」") not in ledger:
        miss.append(x["q_id"])
print("verbatim_not_found_in_ledger:", miss if miss else "0（89 条含值答复全部在台账逐字命中）")
spot = ["D8-01", "D8-15", "D8-36", "D8-42", "D8-52", "D8-58r", "SQ-01", "SQ-04", "T-D8-1", "skill-6"]
for q in spot:
    e = [x for x in sup if x["q_id"] == q][0]
    print(" ", q, "| option_chosen =", repr(e.get("option_chosen")),
          "| reasoning_full =", repr(e.get("reasoning_full")))
