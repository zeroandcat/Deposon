import os, re, io, datetime

ROOT = r'_repo_mirror'
FILES = [
 '_ablation_design_2026_10_20.md',
 '_cluster_k_eta_blockers_adjudication_2026_10_19.md',
 '_d13_eta_parts_1to4_caliber_2026_10_20.md',
 '_eta_construct_c1_c16_recommendation_2026_10_20.md',
 '_eta_construct_face_freeze_draft_2026_10_19.md',
 '_eta_missing_params_and_c1_adjudication_2026_10_19.md',
 '_eta_missing_params_literature_evidence_2026_10_19.md',
 '_eta_preexp_stop_register_2026_10_20.md',
 '_eta_sep_caliber_draft_2026_10_20.md',
 '_experiment_face_scope_column1_supplement_draft_2026_10_19.md',
 '_experiment_face_scope_list_draft_2026_10_19.md',
 '_field_table_c6_c8_o5_recommendation_draft_2026_10_19.md',
 '_gd03_caliber_note_2026_10_20.md',
 '_ge01_freeze_flow_execution_2026_10_20.md',
 '_ge02_adoption_freeze_register_2026_10_20.md',
 '_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md',
 '_kd_eta_main_run_verdict_2026_10_20.md',
 '_kd_eta_selection_verdict_2026_10_20.md',
 '_kd_eta_sep_measurement_verdict_2026_10_20.md',
 '_kd_h1_h7_disposition_draft_2026_10_20.md',
 '_kd_h1_lineage_declaration_2026_10_20.md',
 '_kd_h2_anchor_chain_erratum_2026_10_20.md',
 '_kd_h4_fingerprint_reanchor_register_2026_10_20.md',
 '_kd_h5_session_history_domain_caliber_2026_10_20.md',
 '_kd_h6_caliber_mapping_adjudication_2026_10_20.md',
 '_kd_history_pack_adjudication_2026_10_19.md',
 '_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md',
 '_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md',
 '_kd_mda8_domain_readings_adjudication_2026_10_19.md',
 '_kd_mda8_f1_two_senses_adjudication_2026_10_19.md',
 '_kd_mda8_first_reading_verdict_2026_10_20.md',
 '_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md',
 '_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md',
 '_kd_mda8_spec_rest_recommendation_2026_10_19.md',
 '_kd_two_gates_comparison_2026_10_20.md',
 '_l2_2_duplication_criterion_adjudication_2026_10_19.md',
 '_mda8_readlaw_o1_o4_c4_recommendation_2026_10_20.md',
 '_preexp_design_kmda8a24_degen_2026_10_20.md',
 '_preexp_design_new_construct_mda8a24_2026_10_20.md',
 '_preexp_mda8a24_c1_reading_2026_10_20.md',
 '_runface_vs_shape_caliber_draft_2026_10_20.md',
 '_runface_vs_shape_multidim_supplement_2026_10_20.md',
 '_stage1_eta_kill_line_freeze_draft_2026_10_19.md',
 '_stage1_eta_numeric_freeze_draft_2026_10_19.md',
 '_stage1_field_table_freeze_draft_2026_10_19.md',
 '_stage1_prereq_wave1_evidence_2026_10_20.md',
 '_v148_four_points_erratum_draft_2026_10_20.md',
]

# section headings that introduce a candidate-item table
KEYS = ['\u5019 PI \u88c1', '\u5f85 PI \u88c1', '\u5019 PI \u7ed9\u503c', '\u5f85 PI \u7ed9\u503c',
        '\u5019\u88c1', '\u5f85\u88c1', '\u5019 PI', '\u5f85 PI', '\u5019\u88c1\u9762',
        '\u5f85\u53d6\u8bc4', '\u5f85\u62cd\u677f', '\u62a5\u56de', '\u88c1\u9879\u6e05\u5355',
        '\u5f85\u88c1\u4f4d', '\u5019\u88c1\u4f4d']
HEAD = re.compile(r'^(#{2,4})\s*(.+?)\s*$')

out = io.StringIO()
for f in FILES:
    p = os.path.join(ROOT, 'results', f)
    if not os.path.exists(p):
        out.write('### MISSING %s\n' % f)
        continue
    raw = open(p, 'rb').read()
    text = raw.decode('utf-8', 'replace')
    lines = text.split('\n')
    out.write('\n########## %s  (sha12=%s bytes=%d)\n' % (f, __import__('hashlib').sha256(raw).hexdigest()[:12], len(raw)))
    i = 0
    n = len(lines)
    while i < n:
        m = HEAD.match(lines[i])
        if m and any(k in m.group(2) for k in KEYS):
            out.write('  -- HEADING L%d: %s\n' % (i + 1, m.group(2)))
            j = i + 1
            shown = 0
            while j < n and shown < 40:
                ln = lines[j]
                if HEAD.match(ln):
                    break
                if ln.startswith('|') and ln.count('|') >= 3 and not re.match(r'^\|[\〔本地绝对路径·脱敏略:-〕|]+\|$', ln):
                    out.write('     %s\n' % ln[:300])
                    shown += 1
                elif ln.strip().startswith('**') and shown < 20:
                    out.write('     %s\n' % ln[:300])
                    shown += 1
                j += 1
            i = j
            continue
        i += 1

open(os.path.join(ROOT, '_tools_docwriter_candidate_items.txt'), 'w', encoding='utf-8', newline='\n').write(out.getvalue())
print('WROTE', len(out.getvalue()), 'chars')
