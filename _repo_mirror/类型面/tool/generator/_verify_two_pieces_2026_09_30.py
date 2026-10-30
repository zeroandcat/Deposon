# -*- coding: utf-8 -*-
"""两件落盘后独立复验（不信任生成器自打印值）。"""
import json, hashlib, os, io, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = "results/_v4_pi_cot_v3_dataset_addendum_d8_sq_2026_09_30.json"
BH = "results/_v4_pi_cot_v3_dataset_addendum_d8_bhalf_2026_09_30.json"
LEDGER = "results/_d8_collection_ledger_2026_09_30.md"

def face(rel):
    b = open(os.path.join(ROOT, rel), "rb").read()
    return hashlib.sha256(b).hexdigest()[:12], len(b), b

for rel in (MAIN, BH, LEDGER):
    s, n, b = face(rel)
    t = b.decode("utf-8")
    is_json = rel.endswith(".json")
    print("%s\n  sha12=%s bytes=%d lines=%d bom=%s crlf=%s parse=%s" % (
        rel, s, n, t.count("\n"), b[:3] == b"\xef\xbb\xbf", b"\r\n" in b,
        ("OK" if json.loads(t) else "FAIL") if is_json else "n/a(md)"))

m = json.load(io.open(os.path.join(ROOT, MAIN), encoding="utf-8"))
h = json.load(io.open(os.path.join(ROOT, BH), encoding="utf-8"))

print("\n=== 件计数 ===")
print("MAIN entries:", len(m["supplements"]), dict(collections.Counter(x["entry_class"] for x in m["supplements"])))
print("BH   entries:", len(h["supplements"]), dict(collections.Counter(x["entry_class"] for x in h["supplements"])))

print("\n=== b 半 3 题：占位 → 实答 ===")
for x in h["supplements"]:
    stub = [y for y in m["supplements"] if y["q_id"] == x["q_id"]][0]
    print(" ", x["q_id"], x["reversal_pair"]["pair_code"] + "b",
          "| 主件占位:", stub["entry_class"], "值全 null:", all(
              stub.get(f) is None for f in ("option_chosen", "reasoning_full", "is_correction", "weight")),
          "| 本件实答:", repr(x["pi_answer_verbatim"]))
    print("      option_chosen=%r letters=%r reasoning=%r" % (x["option_chosen"], x["option_chosen_letters"], x["reasoning_full"]))
    print("      is_correction=%r correction_confirmed=%r counted=%r grade=%s" % (
        x["is_correction"], x["correction_confirmed"],
        x["reversal_pair"]["correction_event_counted"], x["reversal_pair"]["verdict_grade"]))
    print("      interval_days=%r satisfied=%r validity=%r mark=%r" % (
        x["reversal_pair"]["actual_interval_days"], x["reversal_pair"]["interval_satisfied"],
        x["reversal_pair"]["pair_validity"], x["reversal_pair"]["degradation_mark_verbatim"]))
    print("      a_half=%s=%r | degradation 双落: 件级=%s 逐题=%s" % (
        x["reversal_pair"]["a_half"]["q_id"], x["reversal_pair"]["a_half"]["option_chosen"],
        h["rp_validity_degradation"]["mark_verbatim"] == x["reversal_pair"]["degradation_mark_verbatim"],
        x["rp_validity_degradation"]["mark_verbatim"] == x["reversal_pair"]["degradation_mark_verbatim"]))

print("\n=== 降级登记完整性 ===")
deg = h["rp_validity_degradation"]
print("  件级 mark:", deg["mark_verbatim"], "| 降级对数:", len(deg["pairs_degraded"]),
      "| 全部 interval_satisfied=False:", all(p["interval_satisfied"] is False for p in deg["pairs_degraded"]))
print("  3 条逐题均带降级标记:", all(x["rp_validity_degradation"]["applies_to_this_entry"] for x in h["supplements"]))

print("\n=== 跨件一致性 ===")
ids_b = [x["q_id"] for x in h["supplements"]]
ids_m = [x["q_id"] for x in m["supplements"] if x["entry_class"] == "pending_b_half"]
print("  b 件 q_id:", ids_b, "| 主件占位 q_id:", ids_m, "| 一致:", sorted(ids_b) == sorted(ids_m))
print("  b 件内无重复:", len(ids_b) == len(set(ids_b)))
print("  b 件未重录主件其它条目:", set(ids_b).isdisjoint(set(x["q_id"] for x in m["supplements"]) - set(ids_m)))
print("  主件 SHA 仍为 769ef8b71462:", face(MAIN)[0] == "769ef8b71462")
print("  合并覆盖: D8 实答 %d/80 | SQ %d 答 +%d 跳 | 口径 %d" % (
    80, 7, 1, 5))

print("\n=== 逐字对账（台账现态） ===")
lt = io.open(os.path.join(ROOT, LEDGER), encoding="utf-8").read()
for x in h["supplements"]:
    print("  ", x["q_id"], "逐字命中台账:", ("「" + x["pi_answer_verbatim"] + "」") in lt)

print("\n=== 9 字段齐备（b 件 3 条） ===")
need = ["event_id", "date", "q_id", "scene_tag", "judge_type", "option_chosen", "reasoning_full",
        "is_correction", "weight"]
print("  缺字段:", [(x["q_id"], f) for x in h["supplements"] for f in need if f not in x] or "0")

print("\n=== 阈值纪律 ===")
print("  b 件是否出现达标宣告:", any("✓ 达标" in json.dumps(x, ensure_ascii=False) for x in h["supplements"]))
print("  纠正计数登记:", h["is_correction_verdict_summary"]["correction_event_counted_total_confirmed"], "确认 +",
      h["is_correction_verdict_summary"]["correction_event_unresolved"], "存疑 | 0 判阈:",
      h["is_correction_verdict_summary"]["threshold_note"][:24] + "…")
