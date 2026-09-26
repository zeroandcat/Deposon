# -*- coding: utf-8 -*-
"""R3: 汇总回函所需全部 SHA-12。"""
import hashlib
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
SUB = Path(r'D:\私人资料\deposon-sub')
sha12 = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12].upper()

print('=== 新建/将引用件 ===')
for p in [REPO / 'docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md',
          REPO / 'letters/TRAE_V3_REVIEW_LETTER_2026_09_23.md',
          REPO / 'deposon_team/plugins/boss_pa_1_rbr_rm.py',
          REPO / 'results/deposon_pa_d1_d3_2026_09_15.json',
          SUB / 'results/boss_pa_1_rbr_rm_result_2026_09_15.json',
          SUB / 'results/boss_pa_3_replicator_dynamics_result_2026_09_15.json',
          SUB / 'results/d7_5anchor_60cells_9model_verdict_2026_09_18.json',
          SUB / 'results/_adendum_A_degradation_precheck_20260917_132049.json',
          SUB / '_movedout_manifest_2026_09_21.json',
          SUB / 'deposon_team/plugins/runner_pa_d1_d3.py',
          SUB / 'deposon_team/plugins/_p_i_real_labels_runner_2026_09_16.py',
          SUB / 'deposon_team/plugins/_p_l_p_c_finite_size_scaling_runner_2026_09_16.py',
          SUB / 'deposon_team/plugins/_p_m_real_separation_runner_2026_09_16.py']:
    if p.exists():
        print(f'  {sha12(p)}  {p.stat().st_size:>8}B  {p.name}' + ('' if 'deposon-repo' in str(p) else '  [sub]'))
    else:
        print(f'  MISSING  {p}')

print()
print('=== V4 参照样本 ===')
for rel in ['results/_v4_exec_seeds_batch_verdict.md', 'results/_v4_v5_verdict_v1.md',
            'results/_v4_exec_methods_batch_verdict.md', 'results/_v4_exec_n_batch_verdict.md']:
    p = REPO / rel
    print(f'  {sha12(p) if p.exists() else "MISSING"}  {rel}')

print()
print('=== 19 REPORT 复核 ===')
for p in sorted((REPO / 'docs/V3X').glob('*REPORT*')):
    print(f'  {sha12(p)}  {p.name}')
print()
print('_r3 DONE')
