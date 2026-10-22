# -*- coding: utf-8 -*-
"""轴二实跑之附加口径核 (只读): 空文本 / 计数单位 / 词表来源例之对读。"""
from __future__ import annotations
import importlib.util, json, sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RESULTS = REPO / "results"

spec = importlib.util.spec_from_file_location(
    "run1", REPO / ".tmp" / "e4_axis2_v11_displacement_run_2026_10_10.py")
# 复用上一次运行的输出即可; 此处独立复算空文本口径。
sampling = json.loads((RESULTS / "_s4_heldout_sampling_seed42_items_2026_10_09.json").read_text(encoding="utf-8"))
spec2 = importlib.util.spec_from_file_location("exec_v3", RESULTS / "_v4_pi_cot_v3_ruleset_v3_executor.py")
exec_v3 = importlib.util.module_from_spec(spec2)
spec2.loader.exec_module(exec_v3)
load_addendum_event_v3 = exec_v3.load_addendum_event_v3

WAVE_MAP = {
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
for fname in sampling["domain"]["r1_byte_sorted_files"]:
    ad = json.loads((RESULTS / fname).read_text(encoding="utf-8"))
    wave = WAVE_MAP.get(fname, "S4_face_unregistered_wave")
    for i, sup in enumerate(ad.get("supplements", [])):
        ev = load_addendum_event_v3(sup, wave, fname)
        rows.append((fname, i, ev.get("q_id", ""), ev.get("reasoning_full", "") or ""))

texts = [r[3] for r in rows]
all_uniq = set(texts)
nonempty_uniq = {t for t in all_uniq if t.strip() != ""}
empty_rows = [(f, i, q) for f, i, q, t in rows if t.strip() == ""]

ds = json.loads((RESULTS / "_v4_pi_cot_v2_dataset.json").read_text(encoding="utf-8"))
v11_texts = [(ev.get("q_id", ""), ev.get("reasoning_full", "") or "") for ev in ds["events"]]
v11_uniq = {t for _, t in v11_texts}

# 轴二 4 件之 q_id 是否与 S4 冻结面 q_id 冲突
axis2_qids = ["q10", "q13", "q14", "q21"]
s4_qids = {r[2] for r in rows}
qid_collision = {q: (q in s4_qids) for q in axis2_qids}

# 词表定稿件 §4 之「逐字来源例」是否正为此 4 件
kw = (RESULTS / "_s4_v31_keyword_table_final_2026_10_10.md").read_text(encoding="utf-8")
src_example_hits = {
    w: kw.count(f"`{w}`｜") for w in ["复核", "质量", "保证", "回退", "遗忘", "推翻",
                                      "对齐", "失实", "记忆效应", "噪声", "缺陷",
                                      "观察者效应", "检验", "挂起", "后面"]
}

out = {
    "s4_rows": len(rows),
    "s4_unique_texts_raw": len(all_uniq),
    "s4_unique_texts_excl_empty": len(nonempty_uniq),
    "empty_rows_n": len(empty_rows),
    "empty_rows": [{"file": f, "idx": i, "q_id": q} for f, i, q in empty_rows],
    "v11_unique_texts_raw": len(v11_uniq),
    "v11_empty_texts": len([t for _, t in v11_texts if t.strip() == ""]),
    "union_raw": len(all_uniq | v11_uniq),
    "union_excl_empty": len(nonempty_uniq | v11_uniq),
    "face2_registered_s4_uniq": 131,
    "face2_registered_union_uniq": 168,
    "reconcile_131": len(nonempty_uniq) == 131,
    "reconcile_168": len(nonempty_uniq | v11_uniq) == 168,
    "axis2_qid_collision_with_s4": qid_collision,
    "v11_qids": [q for q, _ in v11_texts],
    "kwtable_source_example_counts": src_example_hits,
}
sys.stdout.write(json.dumps(out, ensure_ascii=False, indent=1))
