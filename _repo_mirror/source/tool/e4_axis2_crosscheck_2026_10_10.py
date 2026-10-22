# -*- coding: utf-8 -*-
"""轴二实跑之交叉核验 (只读): (1) q_id 跨面冲突 (2) executor 面 72 唯一文本 (3) 词表来源例对读。"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"
spec = importlib.util.spec_from_file_location("exec_v3", RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)

# (1) executor 面 = load_all_events_v3 (v1.1 + 9 v2 addenda + D4) -> 唯一文本数
events, meta = ex.load_all_events_v3()
texts = [(ev.get("q_id", ""), ev.get("reasoning_full", "") or "") for ev in events]
uniq_all = {t for _, t in texts}
uniq_nonempty = {t for t in uniq_all if t.strip() != ""}
v11 = json.loads((RESULTS / "_v4_pi_cot_v2_dataset.json").read_text(encoding="utf-8"))
v11_texts = {ev.get("reasoning_full", "") or "" for ev in v11["events"]}
addendum_texts = uniq_all - v11_texts

# (2) q_id 跨面冲突: v1.1 事件 vs S4 冻结面
sampling = json.loads((RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json").read_text(encoding="utf-8"))
WAVE = {
    "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json": "D1_supp",
    "_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json": "D2_w1",
    "_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json": "D2_w2",
    "_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json": "D2_w3",
    "_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json": "D2_w4",
    "_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json": "D2_w5",
    "_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json": "D3_w1",
    "_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json": "D3_w2",
    "_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json": "D3_w3",
    "_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json": "D4_w1",
}
s4_rows = []
for fn in sampling["domain"]["r1_byte_sorted_files"]:
    ad = json.loads((RESULTS / fn).read_text(encoding="utf-8"))
    w = WAVE.get(fn, "S4_face_unregistered_wave")
    for i, sup in enumerate(ad.get("supplements", [])):
        ev = ex.load_addendum_event_v3(sup, w, fn)
        s4_rows.append({"file": fn, "idx": i, "q_id": ev.get("q_id", ""),
                        "rf": ev.get("reasoning_full", "") or ""})
s4_qid = {}
for r in s4_rows:
    s4_qid.setdefault(r["q_id"], []).append({"file": r["file"], "idx": r["idx"], "rf_len": len(r["rf"])})

axis2_qids = ["q10", "q13", "q14", "q21"]
collision = {}
for q in axis2_qids:
    v11_hit = next(({"q_id": ev.get("q_id", ""), "event_id": ev.get("event_id", "")}
                    for ev in v11["events"] if ev.get("q_id") == q), None)
    collision[q] = {"in_s4_face": q in s4_qid, "s4_rows": s4_qid.get(q, []), "v11_event": v11_hit}

# (3) 词表定稿件 §4 之逐字来源例 q_id 是否即此 4 件
kw = (RESULTS / "_s4_v31_keyword_table_final_2026_10_10.md").read_text(encoding="utf-8")
src_examples = {}
for word, qids in [("推翻", ["q10", "q13", "q21"]), ("检验", ["q14"])]:
    src_examples[word] = {q: (f"`{q}`" in kw) for q in qids}

out = {
    "executor_face": {
        "n_events": meta["n_total"], "n_v11": meta["n_v11"],
        "n_unique_texts_raw": len(uniq_all),
        "n_unique_texts_nonempty": len(uniq_nonempty),
        "n_v11_unique_texts": len(v11_texts),
        "n_addendum_only_unique_texts": len(addendum_texts),
        "face2_registered_executor_72": len(uniq_nonempty) == 72,
    },
    "axis2_qid_cross_face_collision": collision,
    "kwtable_source_examples_are_axis2_items": src_examples,
}
sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=1))
