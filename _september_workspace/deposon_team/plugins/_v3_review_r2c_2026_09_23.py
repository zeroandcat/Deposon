# -*- coding: utf-8 -*-
"""R2c: P-I~P-O runner 现状 (09-16 修复是否保留) + 09-16 悬挂项 + 报告幽灵引用抽样。"""
import hashlib, re
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
SUB = Path(r'D:\私人资料\deposon-sub')
sha12 = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12].upper()

PLUG = SUB / 'deposon_team' / 'plugins'
print('=== A. P-I~P-O runner 定位 (sub plugins) + 09-16 修复标记 ===')
for name in ['_p_i_real_labels_runner_2026_09_16.py', '_p_j_convergence_basin_runner_2026_09_16.py',
             '_p_k_blind_test_runner_2026_09_16.py', '_p_l_p_c_finite_size_scaling_runner_2026_09_16.py',
             '_p_m_attack_surface_cost_runner_2026_09_16.py', '_p_m_real_separation_runner_2026_09_16.py',
             '_p_n_curvature_potential_coupling_runner_2026_09_16.py', '_p_o_stranger_verification_runner_2026_09_16.py',
             '_p_l_real_data_collapse_runner_2026_09_16.py', '_unverified_marker' ]:
    p = PLUG / name
    if not p.exists():
        hits = list(SUB.rglob(name))
        p = hits[0] if hits else None
    if p and p.exists():
        s = p.read_text(encoding='utf-8', errors='ignore')
        marks = []
        for mk in ['TRAE_FIXED', 'UNVERIFIED', 'TRAE_SELFCHECK', '真标签', '伪造', 'and', 'or ']:
            if mk in s:
                marks.append(mk)
        # 关键: 判死判定行
        verdict_lines = [f'L{i}: '+l.strip()[:100] for i, l in enumerate(s.splitlines(), 1)
                         if re.search(r'(dang_verdict|final.*verdict|判死|UNVERIFIED)', l, re.I)][:4]
        print(f'  {name}: sha12={sha12(p)} size={p.stat().st_size} marks={marks[:5]}')
        for vl in verdict_lines:
            print(f'     {vl}')
    else:
        print(f'  {name}: NOT FOUND')

print()
print('=== B. _p_i 假标签 / _p_l 伪造 R2 / _p_m 量纲 现状 ===')
for name, kws in [
    ('_p_i_real_labels_runner_2026_09_16.py', ['true_labels', '[0]*8', 'and ', ' or ', 'UNVERIFIED']),
    ('_p_l_p_c_finite_size_scaling_runner_2026_09_16.py', ['0.4*exp', 'max_R2', 'UNVERIFIED', 'FAIL_ALL']),
    ('_p_m_attack_surface_cost_runner_2026_09_16.py', ['miss_rate', '0.5', 'budget']),
    ('_p_j_convergence_basin_runner_2026_09_16.py', ['0.1', 'convergence_rate', 'UNVERIFIED']),
]:
    hits = list(SUB.rglob(name))
    if not hits:
        print(f'  {name}: NOT FOUND'); continue
    p = hits[0]
    s = p.read_text(encoding='utf-8', errors='ignore')
    print(f'  {name}:')
    for kw in kws:
        cnt = s.count(kw)
        if cnt:
            ln = [f'L{i}' for i, l in enumerate(s.splitlines(), 1) if kw in l][:3]
            print(f'     "{kw}" x{cnt} at {ln}')

print()
print('=== C. 09-16 悬挂项现状 ===')
# skill_a/b/c/d frozen SELF-CHECK
for s_ in ['skill_a_p_a_60cells.py', 'skill_b_p_c_alpha_beta.py', 'skill_c_p_e_3modality.py', 'skill_d_p_f_observer.py']:
    for base in [REPO, SUB]:
        p = base / 'deposon_team' / 'plugins' / s_
        if p.exists():
            s = p.read_text(encoding='utf-8', errors='ignore')
            print(f'  {s_}: [{base.name}] sha12={sha12(p)} SELF-CHECK={"YES" if "SELF-CHECK" in s else "NO"}')
            break
# _p_k 绝对路径
for base in [REPO, SUB]:
    for cand in list(base.rglob('_p_k_blind_test_runner_2026_09_16.py')):
        s = cand.read_text(encoding='utf-8', errors='ignore')
        print(f'  _p_k_blind_test_runner: [{base.name}] sha12={sha12(cand)} repo外绝对路径={"YES" if "C:\\\\Users" in s else "no"}')

print()
print('=== D. 报告幽灵引用抽样: 19 报告引用的 results/*.json 在 repo 是否存在 ===')
rep_dir = REPO / 'docs' / 'V3X'
refs = set()
for rp in rep_dir.glob('*REPORT*'):
    s = rp.read_text(encoding='utf-8', errors='ignore')
    for m in re.findall(r'results[/\\]([A-Za-z0-9_.\-]+\.json)', s):
        refs.add(m)
print(f'  报告引用的 results/*.json 唯一名: {len(refs)}')
missing_repo, in_sub = [], []
for f in sorted(refs):
    rp = REPO / 'results' / f
    sp = SUB / 'results' / f
    if rp.exists():
        pass
    elif sp.exists():
        in_sub.append(f)
    else:
        missing_repo.append(f)
print(f'  repo 内不存在、但 deposon-sub 内有: {len(in_sub)} 件')
for f in in_sub[:20]:
    print(f'     {f}')
print(f'  两仓均无（真缺件）: {len(missing_repo)} 件')
for f in missing_repo[:25]:
    print(f'     {f}')
print()
print('  _r2c DONE')
