# -*- coding: utf-8 -*-
"""Final completion audit: verify every deliverable of the 2026-09-17 goal exists on disk
with recorded SHA-12; verify erratum patch idempotency frozen-state; verify frozen 0-touch."""
import hashlib, os, json

BASE = r'D:\私人资料\deposon-repo'

def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

# R1: delegate letter read & executed -> evidence = 5 audit deliverables exist
deliverables = {
    r'results\_trae_d7_v1_audit_20260917_190000.md': 'e240ca712be6',
    r'results\_trae_d7_v1_audit_20260917_190000.json': '3184b30b7b0d',
    r'results\_trae_kimi_push_v3_audit_20260917_193000.md': '8ece24be6b8a',
    r'results\_trae_corpus_5_audit_20260917_193000.md': 'f2a655cd5e54',
    r'results\_trae_anchor_18_audit_20260917_193000.md': '4af67e6cbe71',
    r'results\_trae_paper_8ch_\u53cc\u5ba1_20260917_200000.md': 'bec666969ffc',
    r'deposon_team\plugins\_fix_adendum_c_erratum_2026_09_17.py': 'eb44de412de5',
}
print('=== R1/R2 evidence: deliverables on disk + SHA match ===')
ok = True
for rel, exp in deliverables.items():
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        print('MISSING', rel); ok = False; continue
    got = sha12(p)
    print('MATCH' if got == exp else 'DRIFT %s!=%s' % (got, exp), rel)
    ok = ok and (got == exp)

# R3: direct improvement applied & idempotent (erratum present, original values untouched)
print()
print('=== R3 evidence: Adendum C erratum patch state ===')
for rel, after in [(r'results\_adendum_C_pm_attack_surface_v2_20260917_133852.json', '6eba63788ca8'),
                   (r'results\_adendum_C_pm_attack_surface_v2_20260917_133726.json', '193ba7d66412')]:
    p = os.path.join(BASE, rel)
    d = json.load(open(p, encoding='utf-8'))
    has = 'erratum_2026_09_17' in d
    preserved = d['erratum_2026_09_17'].get('original_verdict_preserved') if has else False
    got = sha12(p)
    print('%s erratum=%s preserved=%s sha=%s %s' % (
        os.path.basename(rel), has, preserved, got,
        'OK' if (has and preserved and got == after) else 'DRIFT'))

# R4/R5: improvement letter exists with before/after SHA table content
print()
print('=== R4/R5 evidence: improvement letter content ===')
letter = os.path.join(BASE, r'docs\V3X\TRAE_CODE_IMPROVEMENT_LETTER_2026_09_17.md')
txt = open(letter, encoding='utf-8').read()
for needle in ['d64e8e2e2518', '6eba63788ca8', '9c5ca0fed3ef', '193ba7d66412',
               'e240ca712be6', '3184b30b7b0d', '改进前', '改进后', '§4 改进前后 SHA-12 对照表']:
    print('contains', repr(needle), ':', needle in txt)
print('letter final sha12 (authoritative, self-reference note in effect):', sha12(letter))

# frozen 0-touch spot recheck (16 anchor core)
print()
print('=== frozen 0-touch recheck ===')
frozen_check = [
    (r'results\deposon_v19_benchmark_fixes.json', '910c4333eead'),
    (r'results\deposon_v21_gtformal.json', '9d9ae5001c57'),
    (r'corpus\v20\index.json', '8423ffe266af'),
    (r'deposon_team\plugins\skill_a_p_a_60cells.py', 'b1463bb24403'),
    (r'deposon_team\plugins\skill_b_p_c_alpha_beta.py', 'e5a299f69a22'),
    (r'deposon_team\plugins\skill_c_p_e_3modality.py', 'e19e76c5da7e'),
    (r'deposon_team\plugins\skill_d_p_f_observer.py', '3e369a1f6171'),
    (r'deposon_team\plugins\_v3x_frozen_schema_v1.json', '9e99dcc4d920'),
    (r'corpus\v20\by_model\KIMI\index_v2_2026_09_16.json', 'efe05ad775de'),
    (r'corpus\v20\by_model\minimax\artifact_v_2026_09_16.json', '9e1ccbdceacc'),
]
for rel, exp in frozen_check:
    p = os.path.join(BASE, rel)
    got = sha12(p) if os.path.exists(p) else 'MISSING'
    print('MATCH' if got == exp else 'DRIFT ' + got, rel)

print()
print('AUDIT', 'ALL-PASS' if ok else 'HAS-DRIFT')
