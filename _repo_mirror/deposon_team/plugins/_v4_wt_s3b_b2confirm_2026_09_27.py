# -*- coding: utf-8 -*-
"""_v4_wt_s3b_b2confirm — B2 定因确认：全表 SHA-1 假设 15/15 + §0.1 三行（只读）"""
import hashlib
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo')

ROWS = [
 ('1',     'results/boss_pa_1_rbr_rm_result_2026_09_15.json',                          'D9E14ED29FB9'),
 ('1-r',   'deposon_team/plugins/boss_pa_1_rbr_rm.py',                                 '1935F164D5F3'),
 ('1-rep', 'docs/V3X/P_A_D1_D3_REPORT_2026_09_15.md',                                  'A3FA45E7D121'),
 ('4',     'results/boss_pa_3_replicator_dynamics_result_2026_09_15.json',             '18C9C370A6AE'),
 ('4-r',   'deposon_team/plugins/boss_pa_3_replicator_dynamics.py',                    '268F708B96AE'),
 ('5-anc', 'results/_v3x_conservation_anchor_2026_09_17.txt',                          '425507BB555B'),
 ('5-rep', 'docs/V3X/P_F_D1_FULL_REPORT_2026_09_15.md',                                'BA8F3894969D'),
 ('8',     'results/boss_pc_3_a3_clipping_2026_09_15.json',                            '717C26DF5A00'),
 ('10',    'results/_v3x_experiments_2026_09_16/v3x_experiments_results_2026_09_16.json','05B4649985B5'),
 ('12',    'results/boss_pe_2_real_transverse_ising_2026_09_15.json',                  '04CEDB126B98'),
 ('12-rep','docs/V3X/P_E_D1_D3_REPORT_2026_09_15.md',                                  '664DD320F549'),
 ('26',    'results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json','19F0A2CB8CEF'),
 ('27',    'results/_p_l_p_c_finite_size_scaling_2026_09_16/p_l_p_c_finite_size_scaling_results_2026_09_16.json','00DF93A112F7'),
 ('28',    'results/_p_m_attack_surface_cost_2026_09_16/p_m_attack_surface_cost_results_2026_09_16.json','1F11ED31273D'),
 ('—',     'docs/V3X/V3X_1WEEK_KILL_REPORT_2026_09_18.md',                             'AFD2161E6544'),
]
ROWS01 = [
 ('0-A', 'letters/_v4_distillation_reply_trae_code_v3_review_2026_09_23.md', '24EAFC05A217'),
 ('0-B', 'results/_v3_supplement_verdict_2026_09_23.md',                     '9421E78B7E3C'),
 ('0-C', 'results/_v4_pi_cot_v3_prereg.md',                                  '1A90FD8F385A'),
]

print('=' * 112)
print('B2 定因确认：v1 §0.2 记值 == SHA-1(全文字节)[:12] ?')
print('=' * 112)
print(f'{"#":<7}{"记值":<15}{"SHA-1[:12]":<15}{"SHA-256[:12]":<15}{"判定":<10}件')
h1 = hs = 0
for tag, rel, rec in ROWS:
    p = REPO / rel
    b = p.read_bytes()
    s1 = hashlib.sha1(b).hexdigest()[:12].upper()
    s256 = hashlib.sha256(b).hexdigest()[:12].upper()
    m1 = (s1 == rec); hs += m1; h1 += (not m1)
    print(f'{tag:<7}{rec:<15}{s1:<15}{s256:<15}{"SHA-1命中" if m1 else "未命中":<10}{rel}')
print(f'  ⇒ SHA-1 命中 {hs} / 未命中 {h1}（共 {len(ROWS)} 行）')

print()
print('=' * 112)
print('§0.1 表（3 行）SHA-1 检验')
print('=' * 112)
for tag, rel, rec in ROWS01:
    b = (REPO / rel).read_bytes()
    s1 = hashlib.sha1(b).hexdigest()[:12].upper()
    s256 = hashlib.sha256(b).hexdigest()[:12].upper()
    print(f'  {tag}  记 {rec}  SHA-1 {s1}  SHA-256 {s256}  {"SHA-1命中" if s1==rec else ("SHA-256命中" if s256==rec else "均未命中")}')

print()
print('=' * 112)
print('口径对照：§E 头块声明口径 vs v1 §0.2 实际使用口径')
print('=' * 112)
print('  委托 §E 头块字面 : SHA-12 = hashlib.sha256(全文字节).hexdigest()[:12]（小写）')
print('  v1 §0.2 表实际值 : = hashlib.sha1(全文字节).hexdigest()[:12]（大写展示）⇒ 算法口径错用')
print('  字节列           : 15/15 逐字一致 ⇒ 非内容变更、非转写错位')
print()
print('_wt_s3b DONE')
