# -*- coding: utf-8 -*-
"""§12 夜链补录 · 窗口件抬头/件止采样（只读）
⛔ 排除主代理版两件：_root_session_history_memo_main_2026_10_14.md / _deposon_full_history_main_2026_10_19.md
⛔ 0 写既有件 · 0 读 key/.env · 0 联网
"""
import os, io, sys, builtins

ROOT = r"_repo_mirror"
EXCLUDE = {
    "results/_root_session_history_memo_main_2026_10_14.md",
    "results/_deposon_full_history_main_2026_10_19.md",
}
TARGETS = [
    "results/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md",
    "results/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md",
    "results/_gap_and_kd_flip_master_inventory_2026_10_19.md",
    "results/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md",
    "results/_v139_adoption_effect_2026_10_19.md",
    "results/_kd_mda8_domain_readings_adjudication_2026_10_19.md",
    "results/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md",
    "results/_v140_adoption_effect_2026_10_19.md",
    "results/_v141_adoption_effect_2026_10_19.md",
    "results/_h5_session_census_2026_10_19_part1.md",
    "results/_h5_session_census_2026_10_19_part2.md",
    "results/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md",
    "results/_f3_payment_vector_reconstruction_2026_10_19.md",
    "results/_f3_payment_vector_reconstruction_data_2026_10_19.json",
    "results/_v142_adoption_effect_2026_10_19.md",
    "results/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md",
    "results/_kd_cluster_verdict_pack_adjudication_2026_10_19.md",
    "results/_f3_payment_vector_third_party_recalc_2026_10_19.md",
    "results/_kd_mda8_spec_rest_recommendation_2026_10_19.md",
    "results/_kd_history_pack_adjudication_2026_10_19.md",
    "results/_v143_v144_adoption_effect_2026_10_19.md",
    "results/_eta_construct_face_freeze_draft_2026_10_19.md",
    "results/_kd_h1_h7_hidden_gaps_register_2026_10_19.md",
    "results/.tmp/_audit_final_2026_10_19.py",
]

HEAD = 14
TAIL = 3
OUT = os.path.join(ROOT, "results", ".tmp", "_audit_s12_heads_out_2026_10_19.txt")
_f = io.open(OUT, "w", encoding="utf-8", newline="\n")
def print(*a, **k):
    k["file"] = _f
    builtins.print(*a, **k)
for rel in TARGETS:
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    if rel in EXCLUDE:
        print("=" * 100)
        print("EXCLUDED(主代理版·⛔0读正文): " + rel)
        continue
    if not os.path.exists(p):
        print("=" * 100)
        print("MISSING: " + rel)
        continue
    txt = io.open(p, encoding="utf-8", errors="replace").read()
    lines = txt.split("\n")
    print("=" * 100)
    print("### " + rel)
    for i, l in enumerate(lines[:HEAD], 1):
        print("H%02d| %s" % (i, l[:300]))
    print("   ...")
    for i, l in enumerate(lines[-TAIL:], len(lines) - TAIL + 1):
        print("T%03d| %s" % (i, l[:300]))
