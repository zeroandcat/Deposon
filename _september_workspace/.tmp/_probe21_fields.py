"""V5 #21 副本补丁棒 · 输入面字段形态实测（只读 v19 frozen）。

不 import 锚版，仅直读 v19 JSON，统计 E9.3 两个 benchmark 的 per_problem 字段形态。
"""
import hashlib
import json
from collections import Counter

V19 = "results/deposon_v19_benchmark_fixes.json"

h = hashlib.sha256()
with open(V19, "rb") as f:
    raw = f.read()
h.update(raw)
print("###V19_SHA12###", h.hexdigest()[:12], "bytes", len(raw))

d = json.loads(raw.decode("utf-8"))
e93 = d["experiments"].get("E9.3_high_couple_fix", {})
bms = e93.get("benchmarks", {})
print("###BENCHMARKS###", sorted(bms.keys()))

for bm_name in ("gsm8k", "strategyqa"):
    per = bms.get(bm_name, {}).get("per_problem", {})
    for cond, problems in per.items():
        keys = Counter()
        n_pred_null = n_pred_missing = n_ans_null = n_ans_missing = 0
        n_path_missing = n_bp_missing = n_bp_null = n_path_null = 0
        pred_types = Counter()
        for p in problems:
            for k in p.keys():
                keys[k] += 1
            if "pred" in p:
                if p["pred"] is None:
                    n_pred_null += 1
                pred_types[type(p["pred"]).__name__] += 1
            else:
                n_pred_missing += 1
            if "predicted" in p:
                if p["predicted"] is None:
                    n_pred_null += 1
            else:
                n_pred_missing += 1
            if "answer" in p:
                if p["answer"] is None:
                    n_ans_null += 1
            else:
                n_ans_missing += 1
            if "path" not in p:
                n_path_missing += 1
            elif p["path"] is None:
                n_path_null += 1
            if "best_path" not in p:
                n_bp_missing += 1
            elif p["best_path"] is None:
                n_bp_null += 1
        print("###COND###", bm_name, cond,
              "n=", len(problems),
              "keys=", sorted(keys.items()),
              "pred_null=", n_pred_null, "pred_missing=", n_pred_missing,
              "pred_types=", dict(pred_types),
              "answer_null=", n_ans_null, "answer_missing=", n_ans_missing,
              "path_missing=", n_path_missing, "path_null=", n_path_null,
              "best_path_missing=", n_bp_missing, "best_path_null=", n_bp_null)

# 抽样看一条 strategyqa / 一条 gsm8k 原始记录（截断）
per = bms["strategyqa"]["per_problem"]
first_cond = sorted(per.keys())[0]
print("###SAMPLE_SQA###", first_cond, json.dumps(per[first_cond][0], ensure_ascii=False)[:400])
perg = bms["gsm8k"]["per_problem"]
gcond = sorted(perg.keys())[0]
for p in perg[gcond]:
    if p.get("predicted") is None:
        print("###SAMPLE_GSM_NULL###", gcond, json.dumps(p, ensure_ascii=False)[:400])
        break
print("###SAMPLE_GSM###", gcond, json.dumps(perg[gcond][0], ensure_ascii=False)[:400])
