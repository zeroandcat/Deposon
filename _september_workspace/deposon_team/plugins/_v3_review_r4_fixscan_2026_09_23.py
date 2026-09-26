# -*- coding: utf-8 -*-
"""
_v3_review_r4_fixscan — V3 回审 §3「走读与修复」可修复面扫描（只读，不修改任何文件）
- 判定：仓内 deposon_team/plugins/*.py 与 docs/V3X/* 中，哪些属 frozen / verifier 内置 / 报告正文（不可改），
        哪些属「非冻结可修复面」，并逐项检出 §3 所列缺陷（BOM / 缺 __main__ guard / 非 UTF-8 / 失效转义 / repo 外绝对路径）
"""
import hashlib, os, re, io, sys

REPO = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(REPO, 'deposon_team', 'plugins')

# 18 frozen（来自 _v3x_frozen_schema_v1.json / _verify_15frozen.py），全小写
FROZEN = {
    'verifier/handoff/KT_ABC1_anchors_sha256_12.json', 'docs/V3X/KT_A1_SPEC_V0.1.md',
    'docs/V3X/KT_B1_SPEC_V0.1.md', 'docs/V3X/KT_C1_SPEC_V0.1.md', 'docs/V3X/KT_D0_SPEC_V0.1.md',
    'docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md', 'results/deposon_v19_benchmark_fixes.json',
    'results/deposon_v21_gtformal.json', 'corpus/v20/index.json',
    'verifier/handoff/P_F_PREDECISION_2026_09_09.json', 'docs/V3X/P_F_SPEC_V0.md',
    'docs/V3X/P_F_RESEARCH_2026_09_09.md', 'deposon_team/plugins/skill_a_p_a_60cells.py',
    'deposon_team/plugins/skill_b_p_c_alpha_beta.py', 'deposon_team/plugins/skill_c_p_e_3modality.py',
    'deposon_team/plugins/skill_d_p_f_observer.py',
}
VERIFIER_BUILTIN = {'deposon_team/plugins/_verify_15frozen.py', 'deposon_team/plugins/_verify_15frozen_v1.py'}

def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

def scan_py(p):
    raw = open(p, 'rb').read()
    issues = []
    if raw[:3] == b'\xef\xbb\xbf':
        issues.append('BOM')
    try:
        txt = raw.decode('utf-8')
    except UnicodeDecodeError as e:
        return ['NON_UTF8:' + str(e)], None
    if '__main__' not in txt:
        issues.append('NO_MAIN_GUARD')
    # 失效转义（字符串中未配对的反斜杠 + 常见 Python 无效转义）
    for m in re.finditer(r'\\[^ntr\\\"\'abfv0-7xuUN]', txt):
        issues.append('ODD_ESCAPE')
        break
    # repo 外绝对路径
    for m in re.finditer(r'''(?P<q>['"])(?P<p>[A-Za-z]:[\\/][^'"]{3,})(?P=q)''', txt):
        pth = m.group('p')
        if not pth.lower().startswith(REPO.lower().replace('\\', '/').replace('d:/', 'd:').lower()) and \
           'deposon-repo' not in pth:
            issues.append('ABS_PATH_OUT:' + pth[:60])
            break
    return issues, sha12(p)

print('=' * 92)
print('A. 仓内 deposon_team/plugins 逐文件：冻结状态 / 缺陷 / SHA-12')
print('=' * 92)
rows = []
for fn in sorted(os.listdir(PLUG)):
    if not fn.endswith('.py'):
        continue
    p = os.path.join(PLUG, fn)
    rel = 'deposon_team/plugins/' + fn
    if rel.lower() in FROZEN:
        state = 'FROZEN-18'
    elif rel in VERIFIER_BUILTIN:
        state = 'VERIFIER-BUILTIN'
    elif fn.startswith('_v3_review_'):
        state = 'REVIEW-SCRATCH(本次新增)'
    else:
        state = 'NON-FROZEN'
    issues, s = scan_py(p)
    rows.append((fn, state, ','.join(issues) if issues else '-', s))
    print(f'  {fn:<52} {state:<20} {",".join(issues) if issues else "-":<28} {s}')

print()
print('=' * 92)
print('B. 非冻结可修复面（可改）清单')
print('=' * 92)
fixable = [r for r in rows if r[1] == 'NON-FROZEN']
print(f'  非冻结 *.py 共 {len(fixable)} 件：')
for fn, state, iss, s in fixable:
    print(f'    {fn:<52} issues={iss:<28} sha12={s}')

print()
print('=' * 92)
print('C. 判定')
print('=' * 92)
print('  frozen-18 内可改面 = 0（4 skill_* + 12 anchor 均为只读）')
print('  verifier 内置脚本可改面 = 0')
print('  19 REPORT 正文（docs/V3X/*REPORT*.md / V3X_D7_V3_FINAL / V3X_1WEEK_KILL）= 只读，数字矛盾走勘误清单')
print('  → 本轮 §3 的「修复」实际落点 = 勘误注记 + 新增勘误件；不改任何结论/判定')
print()
print('_r4 DONE')
