# -*- coding: utf-8 -*-
"""Reviewer-A import 口径验证 (沿 Trae §6 建议) - 2026-09-15"""
import importlib.util, os, sys, hashlib

BASE = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(BASE, 'deposon_team', 'plugins')

ALL12 = [
    'boss_pc_1_2d_ising_universality.py',
    'boss_pc_2_transverse_field_ising.py',
    'boss_pc_3_reservoir_computing.py',
    'attack_pc_a1_resampling.py',
    'attack_pc_a2_fitting.py',
    'attack_pc_a3_clipping.py',
    'boss_pg_1_riemannian_degenerate.py',
    'boss_pg_2_hyperbolic_classification_collapse.py',
    'boss_pg_3_geodesic_violation.py',
    'boss_pa_1_rbr_rm.py',
    'boss_pa_2_potential_game.py',
    'boss_pa_3_replicator_dynamics.py',
]
print('===== STEP 3: IMPORT 口径验证 12 尾块文件 =====')
ok, fail = 0, 0
fail_list = []
for fname in ALL12:
    p = os.path.join(PLUG, fname)
    try:
        spec = importlib.util.spec_from_file_location(fname[:-3], p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        ok += 1
        print(f'  [PASS] {fname}')
    except Exception as e:
        fail += 1
        fail_list.append((fname, type(e).__name__, str(e)))
        print(f'  [FAIL] {fname}: {type(e).__name__}: {e}')
print('-' * 60)
print(f'TOTAL: {len(ALL12)} | OK: {ok} | FAIL: {fail}')
if fail_list:
    print('FAIL DETAILS:')
    for fn, et, em in fail_list:
        print(f'  - {fn}: {et}: {em}')

# ===== STEP 4: 16 frozen verify (沿 _verify_15frozen.py + _verify_pg_v0.py) =====
FROZEN16 = [
    ('verifier/handoff/KT_ABC1_anchors_sha256_12.json', '03c6c01f3697', '5 anchors JSON'),
    ('docs/V3X/KT_A1_SPEC_V0.1.md', '78b71d404366', 'KT-A1 SPEC V0.1'),
    ('docs/V3X/KT_B1_SPEC_V0.1.md', '0410ca0fbdae', 'KT-B1 SPEC V0.1'),
    ('docs/V3X/KT_C1_SPEC_V0.1.md', '59d8f56347d5', 'KT-C1 SPEC V0.1'),
    ('docs/V3X/KT_D0_SPEC_V0.1.md', 'cce8e9a1b00e', 'KT-D0 SPEC V0.1'),
    ('docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md', 'b10fae0da66d', 'P-F V0.1 upgrade'),
    ('results/deposon_v19_benchmark_fixes.json', '910c4333eead', 'v19 benchmark'),
    ('results/deposon_v21_gtformal.json', '9d9ae5001c57', 'v21 gtformal'),
    ('corpus/v20/index.json', '8423ffe266af', 'corpus v20'),
    ('verifier/handoff/P_F_PREDECISION_2026_09_09.json', 'b41c98bf90cc', 'P-F V0 placeholder'),
    ('docs/V3X/P_F_SPEC_V0.md', 'de90faf362c5', 'P-F SPEC V0'),
    ('docs/V3X/P_F_RESEARCH_2026_09_09.md', '98085df7811a', 'P-F research'),
    ('deposon_team/plugins/skill_a_p_a_60cells.py', 'b1463bb24403', 'plugin_a 9078B'),
    ('deposon_team/plugins/skill_b_p_c_alpha_beta.py', 'e5a299f69a22', 'plugin_b 8699B'),
    ('deposon_team/plugins/skill_c_p_e_3modality.py', 'e19e76c5da7e', 'plugin_c 8915B'),
    ('deposon_team/plugins/skill_d_p_f_observer.py', '3e369a1f6171', 'plugin_d 15927B (D5 1A user 拍板)'),
]
print()
print('===== STEP 4: 16 frozen verify (修后) =====')
print('PATH'.ljust(70) + ' EXPECTED'.ljust(15) + ' OBSERVED'.ljust(15) + ' MATCH')
print('-' * 110)
fok, ffail = 0, 0
frozen_drift = []
for rel, expected, name in FROZEN16:
    p = os.path.join(BASE, rel)
    if not os.path.exists(p):
        print(rel.ljust(70) + ' MISSING'.ljust(15) + ' -'.ljust(15) + ' FAIL')
        ffail += 1
        frozen_drift.append((rel, expected, 'MISSING'))
        continue
    with open(p, 'rb') as f:
        sha12 = hashlib.sha256(f.read()).hexdigest()[:12]
    match = (sha12 == expected)
    print(rel.ljust(70) + ' ' + expected.ljust(15) + ' ' + sha12.ljust(15) + ' ' + str(match))
    if match:
        fok += 1
    else:
        ffail += 1
        frozen_drift.append((rel, expected, sha12))
print('-' * 110)
print(f'TOTAL: {len(FROZEN16)} | OK: {fok} | FAIL: {ffail}')
if frozen_drift:
    print('DRIFT DETAILS:')
    for rel, exp, got in frozen_drift:
        print(f'  - {rel}: expected={exp} got={got}')

# P-G V0 spec 自身 SHA
print()
print('===== P-G V0 spec verify =====')
pg_path = os.path.join(BASE, 'docs', 'V3X', 'P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md')
with open(pg_path, 'rb') as f:
    pg_sha = hashlib.sha256(f.read()).hexdigest()[:12]
print(f'  P-G V0 spec SHA-12: {pg_sha}')
print(f'  expected: 2f0765a1d39d')
print(f'  match: {pg_sha == "2f0765a1d39d"}')

print()
print('===== SUMMARY =====')
print(f'12 import: {ok}/{len(ALL12)} PASS')
print(f'16 frozen: {fok}/{len(FROZEN16)} PASS')
print(f'P-G V0 spec: {"PASS" if pg_sha == "2f0765a1d39d" else "FAIL"}')
