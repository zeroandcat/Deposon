# -*- coding: utf-8 -*-
"""V3 回审 R1 资产盘点: 19 REPORT + 数据 JSON + runner × 存在性/归档 + 3 BOSS 缺件核实 + V4 参照样本。0 LLM, read-only."""
import hashlib, os
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
sha12 = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12].upper()

def find_anywhere(name):
    """在 ROOT 全树找同名文件（含归档），返回相对路径列表。"""
    hits = [str(p.relative_to(ROOT)) for p in ROOT.rglob(name) if p.is_file()]
    return hits

print('=== A. 19 REPORT 存在性 (docs/V3X + 归档) ===')
REPORTS = [
    'P_A_D1_D3_REPORT_2026_09_10.md', 'P_C_ALPHA_BETA_REPORT_2026_09_10.md',
    'P_E_3MODALITY_REPORT_2026_09_10.md', 'P_F_D1_OBSERVER_REPORT_2026_09_10.md',
    'KT_B1_REWORK_REPORT_2026_09_10.md', 'KT_C1_RENAME_REPORT_2026_09_16.md',
    'BOSS_PA_2_REPORT_2026_09_15.md', 'BOSS_B1_REPORT_2026_09_15.md',
    'D_FIX2_REPORT_2026_09_11.md', 'D5_DECISIONS_2026_09_11.md',
    'D7_REPORT_2026_09_18.md', 'V3X_D7_V3_FINAL_REPORT_2026_09_11_V7.md',
    'V3X_1WEEK_KILL_REPORT_2026_09_11.md', 'V42_V2_REPORT_2026_09_11.md',
    'CPATH_SIMULATION_2026_09_11.md', 'P_G_V01_LANDING_2026_09_15.md',
    # TRAE 系列与 boss 系列可能部分在归档; glob 补齐
]
# 直接 glob docs/V3X 下所有 REPORT
print('  -- docs/V3X/ 下实存 REPORT (glob *REPORT*):')
for p in sorted((ROOT / 'docs' / 'V3X').glob('*REPORT*')):
    print('     %s  %s  %dB' % (sha12(p), p.name, p.stat().st_size))
print('  -- 归档目录中的 REPORT:')
for arch in ROOT.rglob('_archive*'):
    if arch.is_dir():
        for p in sorted(arch.glob('*REPORT*')):
            print('     %s  %s (in %s)' % (sha12(p), p.name, arch.name))

print()
print('=== B. 3 个疑似缺件 BOSS 结果 JSON 核实 ===')
BOSS3 = [
    'boss_pa_1_rbr_rm_result_2026_09_15.json',
    'boss_pa_2_potential_game_result_2026_09_15.json',
    'boss_pc_1_a1_resampling_2026_09_15.json',
]
for name in BOSS3:
    hits = find_anywhere(name)
    if hits:
        for h in hits:
            p = ROOT / h
            print(f'  FOUND   {name} -> {h}  {sha12(p)}  {p.stat().st_size}B')
    else:
        print(f'  MISSING {name} (全树 0 命中 → 真缺件)')

print()
print('=== C. results/ 全部 boss_* 与 d7/d_fix2/phase 数据 JSON ===')
for pat in ['boss_*.json', 'd7_*.json', 'd_fix2*.json', 'deposon_v2_phase*.json',
            'deposon_v19*.json', 'deposon_v21*.json', 'deposon_v42*.json']:
    files = sorted((ROOT / 'results').glob(pat))
    if files:
        print(f'  -- results/{pat}: {len(files)} 件')
        for p in files[:20]:
            print(f'     {sha12(p)}  {p.name}  {p.stat().st_size}B')
        if len(files) > 20:
            print(f'     ... +{len(files)-20} more')

print()
print('=== D. V4 参照样本可读性 ===')
V4REF = [
    'results/_v4_exec_seeds_batch_verdict.md',
    'results/_v4_v5_verdict_v1.md',
    'results/_v4_exec_methods_batch_verdict.md',
    'results/_v4_exec_n_batch_verdict.md',
]
for rel in V4REF:
    p = ROOT / rel
    if p.exists():
        print(f'  OK      {rel}  {sha12(p)}  {p.stat().st_size}B')
    else:
        hits = find_anywhere(p.name)
        print(f'  MISS    {rel}' + (f' -> 归档命中: {hits}' if hits else ' (全树 0 命中)'))

print()
print('=== E. corpus v19/v21/v22 目录核实 ===')
for d in ['corpus/v19', 'corpus/v21', 'corpus/v22']:
    p = ROOT / d
    print(f'  {d}: {"EXISTS" if p.exists() else "NOT-EXISTS"}')
print(f'  corpus/v20/strip_captions_22.json: {"EXISTS " + sha12(ROOT/"corpus/v20/strip_captions_22.json") if (ROOT/"corpus/v20/strip_captions_22.json").exists() else "MISSING"}')
lcount = len(list((ROOT / 'corpus' / 'v20').glob('L_*.json'))) + len(list((ROOT / 'corpus' / 'v20').glob('S*_*.json')))
print(f'  corpus/v20/{{L,S}}*.json: {lcount} 件')

print()
print('=== F. 30 runner 现存性（根目录 P-* + plugins） ===')
runner_pats = ['_p_i_*.py', '_p_j_*.py', '_p_k_*.py', '_p_l_*.py', '_p_m_*.py', '_p_n_*.py', '_p_o_*.py',
               '_pg_v01*.py', '_v3x_*.py', '_v42_*.py', '_d7_*.py', '_d05_*.py']
n_root = 0
for pat in runner_pats:
    fs = sorted(ROOT.glob(pat))
    n_root += len(fs)
n_boss = len(list((ROOT / 'deposon_team' / 'plugins').glob('boss_*.py')))
n_attack = len(list((ROOT / 'deposon_team' / 'plugins').glob('attack_*.py'))) + len(list((ROOT / 'attacks').glob('*.py')))
n_skill = len(list((ROOT / 'deposon_team' / 'plugins').glob('skill_*.py')))
print(f'  根目录 P-系 runner: {n_root} 件; plugins boss_*: {n_boss}; attack_*: {n_attack}; skill_*: {n_skill}')

print()
print('=== G. 09-16 悬挂项现状 ===')
# skill_a/b/c/d SELF-CHECK
for s in ['skill_a_p_a_60cells.py', 'skill_b_p_c_alpha_beta.py', 'skill_c_p_e_3modality.py', 'skill_d_p_f_observer.py']:
    p = ROOT / 'deposon_team' / 'plugins' / s
    if p.exists():
        has_sc = 'SELF-CHECK' in p.read_text(encoding='utf-8', errors='ignore')
        print(f'  {s}: sha12={sha12(p)}  SELF-CHECK={"YES" if has_sc else "NO(frozen 不动,仅报告)"}')
# _p_k 绝对路径
pk = ROOT / 'results' / '_p_k_blind_test_runner_2026_09_16.py'
if not pk.exists():
    pk_hits = find_anywhere('_p_k_blind_test_runner_2026_09_16.py')
    print(f'  _p_k_blind_test_runner: ' + (str(pk_hits) if pk_hits else 'MISSING'))
else:
    s = pk.read_text(encoding='utf-8', errors='ignore')
    print(f'  _p_k_blind_test_runner: {sha12(pk)}, repo 外绝对路径 {"STILL-PRESENT" if "C:\\\\Users" in s or "C:/Users" in s else "clean"}')

print()
print('_v3_review_r1_inventory DONE')
