import os, re, datetime, io, hashlib

ROOT = r'_repo_mirror'
SCAN_DIRS = [os.path.join(ROOT, 'pi_rulings'), os.path.join(ROOT, 'results')]
CUTOFF = datetime.datetime(2026, 10, 19).timestamp()

LITS = [
    ('A', '\u5019 PI'),        # 候 PI
    ('B', '\u5019PI'),         # 候PI  (no space)
    ('C', '\u4fdf PI'),        # 俟 PI
    ('D', '\u4fdfPI'),         # 俟PI  (no space)
    ('E', '\u5f85\u88c1'),     # 待裁
    ('F', '\u5f85\u88c1\u9879'),  # 待裁项
    ('G', '\u5019\u88c1'),     # 候裁
    ('H', '\u5019\u88c1\u9879'),  # 候裁项
    ('I', '\u5f85 PI'),        # 待 PI
]


def count(text, lit):
    n = 0
    i = text.find(lit)
    while i >= 0:
        n += 1
        i = text.find(lit, i + len(lit))
    return n


out = io.StringIO()
totals = {k: 0 for k, _ in LITS}
files = 0
hits_files = 0
grand = 0
union_files = set()
per_file = []

for sd in SCAN_DIRS:
    for dp, dn, fn in os.walk(sd):
        dn[:] = [d for d in dn if d not in {'__pycache__', '.tmp'}]
        for f in sorted(fn):
            if not f.lower().endswith('.md'):
                continue
            p = os.path.join(dp, f)
            try:
                st = os.stat(p)
            except Exception:
                continue
            if st.st_mtime < CUTOFF:
                continue
            raw = open(p, 'rb').read()
            text = raw.decode('utf-8', 'replace')
            files += 1
            row = {}
            tot = 0
            for k, lit in LITS:
                c = count(text, lit)
                totals[k] += c
                row[k] = c
                if c:
                    tot += c
            if tot:
                hits_files += 1
                grand += tot
                union_files.add(os.path.relpath(p, ROOT))
                per_file.append((os.path.relpath(p, ROOT), st.st_mtime, len(raw), row, tot))

per_file.sort(key=lambda r: (-r[4], r[0]))
out.write('=== 遗漏面自查 · 穷举扫描（仪器：Python os.walk + str.find 穷举计数）===\n')
out.write('scan_dirs = pi_rulings/ + results/   (recursively, .md only)\n')
out.write('mtime_cutoff = 2026-10-19 00:00:00 local (inclusive)\n')
out.write('files_scanned = %d\n' % files)
out.write('files_with_hits = %d\n' % hits_files)
out.write('sum_over_literals (overlapping counts, NOT deduped) = %d\n' % grand)
out.write('--- per-literal totals ---\n')
for k, lit in LITS:
    out.write('  %s = %-14s %d\n' % (k, lit, totals[k]))
out.write('--- top 40 files by hit volume ---\n')
for rel, mt, ln, row, tot in per_file[:40]:
    out.write('%-58s %s %8d | A=%d B=%d C=%d D=%d E=%d F=%d G=%d H=%d I=%d | T=%d\n' % (
        rel, datetime.datetime.fromtimestamp(mt).strftime('%m-%d %H:%M'), ln,
        row['A'], row['B'], row['C'], row['D'], row['E'], row['F'], row['G'], row['H'], row['I'], tot))
out.write('files_listed = %d (full list truncated to 40 for readability; total distinct hit files = %d)\n' % (min(40, len(per_file)), len(per_file)))

# union-of-literal distinct-file count using a regex-equivalent per-file "any literal" check
out.write('\n=== DISTINCT FILE LIST (all %d files with >=1 hit) ===\n' % len(per_file))
for rel, mt, ln, row, tot in per_file:
    out.write('%s\n' % rel)

# fingerprint state of cited hosts at measurement time
HOSTS = [
 'results/_results_index_2026_10_21.md',
 'results/_results_path_mapping_2026_10_21.md',
 'results/_kd_mda8a24_clearance_verdict_2026_10_20.md',
 'results/_kd_sepcal7_final_verdict_2026_10_20.md',
 'results/_kd_false9_remedy_proposals_2026_10_20.md',
 'results/_kd_false9_wave0_calibers_2026_10_20.md',
 'results/_kd_identified_defect_attribution_caliber_2026_10_20.md',
 'results/_v172_adoption_effect_2026_10_20.md',
 'results/_v173_adoption_effect_2026_10_21.md',
 'results/_v174_adoption_effect_2026_10_21.md',
 'results/_d13_rename_candidates_2026_10_21.md',
 'results/_kd_two_gates_boundary_proposal_2026_10_21.md',
 'results/_stage1_prereq_wave1_proposals_2026_10_20.md',
 'results/_stage1_prereq_wave1_evidence_2026_10_20.md',
 'results/_mda8a24_release_trigger_proposals_2026_10_20.md',
 'results/_stage1_gap_exhaustive_audit_2026_10_20.md',
 'results/_results_split_proposal_2026_10_21.md',
 'results/_kd_two_gates_comparison_2026_10_20.md',
 'letters/_reply_to_glm_dualtrack_v156_rulings_2026_10_20.md',
 'pi_rulings/_pi_card_answers_register_2026_10_21_v173.md',
 'pi_rulings/_pi_card_answers_register_2026_10_21_v174.md',
 'pi_rulings/_pi_card_answers_register_2026_10_20_v171.md',
 'pi_rulings/_pi_card_answers_register_2026_10_20_v172.md',
 'results/_ablation_design_2026_10_20.md',
 'results/_ablation_reading_2026_10_20.md',
 'results/_runface_vs_shape_caliber_draft_2026_10_20.md',
 'results/_runface_vs_shape_multidim_supplement_2026_10_20.md',
 'results/_d13_eta_parts_1to4_caliber_2026_10_20.md',
 'results/_ge01_freeze_flow_execution_2026_10_20.md',
 'results/_ge02_adoption_freeze_register_2026_10_20.md',
 'results/_gd03_caliber_note_2026_10_20.md',
 'results/_eta_sep_caliber_draft_2026_10_20.md',
 'results/_eta_construct_face_freeze_draft_2026_10_19.md',
 'results/_eta_construct_c1_c16_recommendation_2026_10_20.md',
 'results/_eta_preexp_stop_register_2026_10_20.md',
 'results/_kd_eta_sep_measurement_verdict_2026_10_20.md',
 'results/_kd_eta_main_run_verdict_2026_10_20.md',
 'results/_kd_eta_selection_verdict_2026_10_20.md',
 'results/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md',
 'results/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md',
 'results/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md',
 'results/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md',
 'results/_kd_mda8_spec_rest_recommendation_2026_10_19.md',
 'results/_kd_mda8_domain_readings_adjudication_2026_10_19.md',
 'results/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md',
 'results/_kd_mda8_first_reading_verdict_2026_10_20.md',
 'results/_mda8_readlaw_o1_o4_c4_recommendation_2026_10_20.md',
 'results/_l2_2_duplication_criterion_adjudication_2026_10_19.md',
 'results/_stage1_field_table_freeze_draft_2026_10_19.md',
 'results/_stage1_eta_kill_line_freeze_draft_2026_10_19.md',
 'results/_stage1_eta_numeric_freeze_draft_2026_10_19.md',
 'results/_field_table_c6_c8_o5_recommendation_draft_2026_10_19.md',
 'results/_kd_h1_h7_disposition_draft_2026_10_20.md',
 'results/_kd_h1_lineage_declaration_2026_10_20.md',
 'results/_kd_h2_anchor_chain_erratum_2026_10_20.md',
 'results/_kd_h4_fingerprint_reanchor_register_2026_10_20.md',
 'results/_kd_h5_session_history_domain_caliber_2026_10_20.md',
 'results/_kd_h6_caliber_mapping_adjudication_2026_10_20.md',
 'results/_kd_history_pack_adjudication_2026_10_19.md',
 'results/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md',
 'results/_cluster_k_eta_blockers_adjudication_2026_10_19.md',
 'results/_cluster_j_glm_62_adjudication_2026_10_19.md',
 'results/_glm_unique_reply_117_triage_2026_10_19.md',
 'results/_preexp_design_kmda8a24_degen_2026_10_20.md',
 'results/_preexp_design_new_construct_mda8a24_2026_10_20.md',
 'results/_preexp_mda8a24_c1_reading_2026_10_20.md',
 'results/_eta_missing_params_literature_evidence_2026_10_19.md',
 'results/_v148_four_points_erratum_draft_2026_10_20.md',
 'results/_s2_confirmation_parenthesis_correction_note_2026_10_21.md',
 'results/_kd_family_census_2026_10_20.md',
 'results/_root_session_history_memo_main_2026_10_14.md',
]
out.write('\n=== HOST FINGERPRINT STATE (this measurement) ===\n')
out.write('%-72s %-14s %9s  %s\n' % ('path', 'sha12', 'bytes', 'mtime'))
for h in HOSTS:
    p = os.path.join(ROOT, h.replace('/', os.sep))
    if not os.path.exists(p):
        out.write('%-72s MISSING\n' % h)
        continue
    raw = open(p, 'rb').read()
    st = os.stat(p)
    out.write('%-72s %-14s %9d  %s\n' % (h, hashlib.sha256(raw).hexdigest()[:12], len(raw),
                datetime.datetime.fromtimestamp(st.st_mtime).strftime('%m-%d %H:%M:%S')))

open(os.path.join(ROOT, '_tools_docwriter_measurements.txt'), 'w', encoding='utf-8', newline='\n').write(out.getvalue())
print('WROTE', len(out.getvalue()))
print('files_scanned', files, 'hits_files', hits_files)
for k, lit in LITS:
    print(k, lit, totals[k])
