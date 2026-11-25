# -*- coding: utf-8 -*-
"""轴二实跑之终校 (只读): (1) 面 I 26 件回归 (2) executor 面 5 件位移 (3) 类型判据之 T1/T2 边界核。"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"
spec = importlib.util.spec_from_file_location("exec_v3", RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py")
ex = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ex)

KW3 = ex.KEYWORDS_V3
PAT = ex.PHRASE_PATTERNS_V3
NEW = {
    "CRITERIA": ["复核", "质量", "保证", "对齐", "失实"],
    "RISK": ["回退", "遗忘", "记忆效应", "噪声", "缺陷", "观察者效应"],
    "KILL_LINE": ["推翻", "检验"],
    "TIMING": ["挂起", "后面"],
}
KW31 = {k: tuple(v) for k, v in KW3.items()}
for L, ws in NEW.items():
    KW31[L] = tuple(KW31[L]) + tuple(ws)

def seq_of(r, kw):
    if not r or not r.strip():
        return []
    e = []
    for jt, kws in kw.items():
        p = -1
        for kw2 in kws:
            i = r.find(kw2)
            if i >= 0 and (p < 0 or i < p):
                p = i
        if p >= 0:
            e.append((p, jt))
    e.sort(key=lambda x: x[0])
    s, seen = [], set()
    for _, jt in e:
        if jt not in seen:
            seen.add(jt); s.append(jt)
    for p in PAT:
        if p["pattern"] in r:
            for jt in p["target_seq"]:
                if jt not in seen:
                    seen.add(jt); s.append(jt)
    return s

def is_sub(sm, bg):
    if len(sm) >= len(bg):
        return False
    it = iter(bg)
    return all(any(x == y for y in it) for x in sm)

def cls(a, b):
    if not a and b: return "T3"
    if not a and not b: return "T4"
    if is_sub(a, b): return "T1"
    if set(a) == set(b): return "T2"
    return "OUT_OF_VOCAB"

# ---------- (1) 面 I 回归: held-out 26 件 ----------
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
rows = []
for fn in sampling["domain"]["r1_byte_sorted_files"]:
    ad = json.loads((RESULTS / fn).read_text(encoding="utf-8"))
    w = WAVE.get(fn, "S4_face_unregistered_wave")
    for i, sup in enumerate(ad.get("supplements", [])):
        ev = ex.load_addendum_event_v3(sup, w, fn)
        rows.append({"file": fn, "idx": i, "q_id": ev.get("q_id", ""), "rf": ev.get("reasoning_full", "") or ""})
for r in rows:
    r["a"] = seq_of(r["rf"], KW3); r["b"] = seq_of(r["rf"], KW31)
held_keys = {(it["file"], it["idx"]) for it in sampling["heldout_items"]}
held = [r for r in rows if (r["file"], r["idx"]) in held_keys]
held_disp = [r for r in held if r["a"] != r["b"]]
held_same = [r for r in held if r["a"] == r["b"]]

face1 = json.loads((RESULTS / "_s4_v31_regen_gold_items_2026_10_10.json").read_text(encoding="utf-8"))
f1_items = face1["items"] if isinstance(face1, dict) and "items" in face1 else face1
f1_by_qid = {it["q_id"]: it for it in f1_items}
f1_mismatch = []
for r in held:
    it = f1_by_qid.get(r["q_id"])
    if it is None:
        f1_mismatch.append({"q_id": r["q_id"], "issue": "not_in_face1_json"}); continue
    if list(it.get("seq_v3", [])) != r["a"] or list(it.get("seq_v31", [])) != r["b"]:
        f1_mismatch.append({"q_id": r["q_id"], "face1": [it.get("seq_v3"), it.get("seq_v31")],
                            "mine": [r["a"], r["b"]]})

face1_doc = (RESULTS / "_s4_v31_drift_register_face1_2026_10_10.md").read_text(encoding="utf-8")
empty_qids = [r["q_id"] for r in held if r["rf"].strip() == ""]

# ---------- (2) executor 面: 72 唯一文本之位移 ----------
events, meta = ex.load_all_events_v3()
uniq = {}
for ev in events:
    t = ev.get("reasoning_full", "") or ""
    if t.strip() == "":
        continue
    uniq.setdefault(t, ev)
ex_disp = []
for t, ev in uniq.items():
    a, b = seq_of(t, KW3), seq_of(t, KW31)
    if a != b:
        ex_disp.append({"q_id": ev.get("q_id", ""), "a": a, "b": b, "t": cls(a, b)})

# ---------- (3) 轴二 4 件之 T1/T2 边界逐件核 ----------
v11 = json.loads((RESULTS / "_v4_pi_cot_v2_dataset.json").read_text(encoding="utf-8"))
axis2_boundary = []
for ev in v11["events"]:
    t = ev.get("reasoning_full", "") or ""
    a, b = seq_of(t, KW3), seq_of(t, KW31)
    if a == b:
        continue
    layer_first_v3 = {jt: min((t.find(kw2) for kw2 in KW3[jt] if t.find(kw2) >= 0), default=-1) for jt in a}
    layer_first_v31 = {jt: min((t.find(kw2) for kw2 in KW31[jt] if t.find(kw2) >= 0), default=-1) for jt in b}
    new_layer_pos = {jt: layer_first_v31[jt] for jt in b if jt not in a}
    axis2_boundary.append({
        "q_id": ev.get("q_id", ""), "event_id": ev.get("event_id", ""),
        "seq_v3": a, "seq_v31": b, "type": cls(a, b),
        "set_equal": set(a) == set(b),
        "v3_is_proper_subseq": is_sub(a, b),
        "new_layers": sorted(new_layer_pos),
        "new_layer_first_pos": new_layer_pos,
        "new_layer_at_front": bool(new_layer_pos) and min(new_layer_pos.values()) < min(layer_first_v3.values()),
    })

out = {
    "face1_regression": {
        "n_heldout": len(held), "n_displaced": len(held_disp), "n_unchanged": len(held_same),
        "identity_9_plus_17": len(held_disp) + len(held_same) == 26,
        "face1_json_field_mismatches": f1_mismatch,
        "heldout_empty_corpus_qids": sorted(empty_qids),
        "face1_doc_states_3_empty": "语料 0 字 ＝ **3**" in face1_doc,
    },
    "executor_face_displacement": {
        "n_unique_nonempty": len(uniq),
        "n_displaced": len(ex_disp),
        "matches_face2_registered_5": len(ex_disp) == 5,
        "items": [{k: v for k, v in d.items() if k != "t"} for d in sorted(ex_disp, key=lambda z: z["q_id"])],
    },
    "axis2_boundary_check": axis2_boundary,
}
sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=1))
