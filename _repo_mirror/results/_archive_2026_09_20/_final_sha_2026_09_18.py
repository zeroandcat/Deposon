# -*- coding: utf-8 -*-
"""Trae 2026-09-18 最终 SHA 汇总 (修复后全量)"""
import hashlib
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

GROUPS = {
    'P0 修复': [
        'results/_d05_main_run_results_20260918_100853.json',
        'results/_d05_main_run_results_qwen3_failed_20260918_100853.json',
        'results/_D05_DATA_RESCUE_NOTE_2026_09_18.md',
        'results/_ftfb_external_review_v3_20260917_extracted/ftfb_external_review_v3_20260917/戴夫_FTFB双审包简报v3_2026-09-17.md',
        'results/_letter_to_glm_ftfb_deep_revision_2026_09_18.md',
        'results/_coze_paper_v1_review_2026_09_17/_coze_paper_v1_双审报告_2026_09_17.md',
    ],
    'P1 修复': [
        'volcengine_glm_latest_30cells_v2_runner_2026_09_10.py',
        'deposon_team/plugins/_deposon_v2scripts_reverify_worker_2026_09_18.py',
        'results/_ftfb_v3_pass1_audit_2026_09_18_corrected.md',
        'results/_ftfb_v3_pass2_audit_2026_09_18_corrected.md',
        'verifier/v36/check.sh',
        'verifier/v37/check.sh',
        '_d05_verify_sha_2026_09_18.py',
    ],
    'P1-2/P2 extract+dead+跨平台': [
        '_p_l_v3_phase1_runner_2026_09_17.py',
        '_p_l_v3_phase2_runner_2026_09_17.py',
        '_p_l_v3_phase2_glm53_only_2026_09_17.py',
        '_p_l_v3_phase2_closedsource_runner_2026_09_17.py',
        '_p_l_v3_phase2_closedsource_runner_v2_2026_09_17.py',
        '_p_l_v3_phase2_or_embedding_v3_2026_09_17.py',
        '_p_l_v3_phase2_or_embedding_2026_09_17.py',
        'deposon_agents.py',
        '_merge_or_stub_overlap_table_v3_2026_09_17.py',
    ],
    'P2 注记': [
        'results/_ftfb_external_review_v3_20260917_extracted/ftfb_external_review_v3_20260917/compile_verification.txt',
        'results/_kimi_safe_batch_push_v3_full_2026_09_17.json',
        'results/_kimi_push_v3_manifest_verifier21_cc3c92d0.json',
    ],
    '修复工具': [
        'deposon_team/plugins/_fix_d05_rescue_2026_09_18.py',
        'deposon_team/plugins/_fix_batch2_2026_09_18.py',
        'deposon_team/plugins/_fix_batch3_2026_09_18.py',
        'deposon_team/plugins/_fix_batch4_2026_09_18.py',
        'deposon_team/plugins/_fix_batch6_2026_09_18.py',
        'deposon_team/plugins/_fix_batch7_2026_09_18.py',
        'deposon_team/plugins/_verify_batch5_2026_09_18.py',
    ],
}

for g, files in GROUPS.items():
    print('=== %s ===' % g)
    for f in files:
        p = ROOT / f
        if p.exists():
            print('  %s  %d B  %s' % (sha12(p), p.stat().st_size, f))
        else:
            print('  MISSING  %s' % f)
    print()
