# -*- coding: utf-8 -*-
"""R2 独立复算: 核实子代理报告的关键退化/矛盾结论。主仓 + deposon-sub。0 LLM read-only."""
import hashlib, json, re
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
SUB = Path(r'D:\私人资料\deposon-sub')
sha12 = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12].upper()

print('=== 1. boss_pa_1 degeneracy 复核 (rm_iter / rbr_multiplier / rm_multiplier) ===')
p = SUB / 'results' / 'boss_pa_1_rbr_rm_result_2026_09_15.json'
d = json.loads(p.read_text(encoding='utf-8'))
print('  sha12=', sha12(p), 'size=', p.stat().st_size)
def walk(obj, key, out):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                out.append(v)
            walk(v, key, out)
    elif isinstance(obj, list):
        for v in obj:
            walk(v, key, out)
for key in ['rm_iter', 'rbr_iter', 'bayes_iter', 'rbr_multiplier', 'rm_multiplier']:
    out = []
    walk(d, key, out)
    if out:
        uniq = sorted(set(out))[:8]
        print(f'  {key}: n={len(out)} distinct={uniq}{" ..." if len(set(out))>8 else ""}')

print()
print('=== 2. boss_pa_3 degeneracy 复核 (ess_freq / is_ess / ess_match) ===')
p3 = SUB / 'results' / 'boss_pa_3_replicator_dynamics_result_2026_09_15.json'
d3 = json.loads(p3.read_text(encoding='utf-8'))
print('  sha12=', sha12(p3))
for key in ['ess_freq', 'is_ess', 'ess_match']:
    out = []
    walk(d3, key, out)
    if out:
        print(f'  {key}: n={len(out)} distinct={sorted(set(map(str,out)))[:6]}')

print()
print('=== 3. runner_pa_d1_d3.py:553 常量返回 复核 ===')
rp = SUB / 'deposon_team' / 'plugins' / 'runner_pa_d1_d3.py'
if rp.exists():
    lines = rp.read_text(encoding='utf-8', errors='ignore').splitlines()
    for n in range(548, 558):
        if n <= len(lines):
            print('  L%d: %s' % (n, lines[n-1][:140]))
else:
    print('  MISSING', rp)

print()
print('=== 4. boss_pa_1_rbr_rm.py 的 simulate 函数 (主仓 vs sub) ===')
for base, tag in [(REPO, 'repo'), (SUB, 'sub')]:
    for cand in [base / 'deposon_team' / 'plugins' / 'boss_pa_1_rbr_rm.py', base / 'boss_pa_1_rbr_rm.py']:
        if cand.exists():
            lines = cand.read_text(encoding='utf-8', errors='ignore').splitlines()
            print(f'  [{tag}] {cand.relative_to(base)} sha12={sha12(cand)} lines={len(lines)}')
            for i, l in enumerate(lines, 1):
                if re.search(r'def (simulate_rm|simulate_rbr|bayesian_nash_iter|rbr_mult)', l):
                    print(f'    L{i}: {l.strip()[:110]}')

print()
print('=== 5. _adendum_A_degradation_precheck 内容 (自身即退化检测器) ===')
for base in [SUB, REPO]:
    pa = base / 'results' / '_adendum_A_degradation_precheck_20260917_132049.json'
    if pa.exists():
        da = json.loads(pa.read_text(encoding='utf-8'))
        print('  sha12=', sha12(pa), 'base=', base.name)
        print('  keys:', list(da.keys())[:12])
        s = json.dumps(da, ensure_ascii=False)
        for kw in ['unverified', 'UNVERIFIED', 'degenerate', 'constant', 'pass', 'gray']:
            n = s.lower().count(kw.lower())
            if n:
                print(f'    "{kw}" x{n}')

print()
print('=== 6. d7 verdict JSON (sub) 复核 ===')
pv = SUB / 'results' / 'd7_5anchor_60cells_9model_verdict_2026_09_18.json'
if pv.exists():
    dv = json.loads(pv.read_text(encoding='utf-8'))
    print('  sha12=', sha12(pv), 'size=', pv.stat().st_size)
    print('  top keys:', list(dv.keys()))

print()
print('=== 7. P_A 报告 L143-147 与 JSON 对账尝试 ===')
pr = REPO / 'docs' / 'V3X' / 'P_A_D1_D3_REPORT_2026_09_15.md'
if pr.exists():
    lines = pr.read_text(encoding='utf-8', errors='ignore').splitlines()
    print('  P_A report sha12=', sha12(pr))
    for n in range(140, 150):
        if n <= len(lines):
            print('  L%d: %s' % (n, lines[n-1][:150]))
# 对应 JSON 是否在任一仓
for base in [REPO, SUB]:
    for cand in list(base.rglob('boss_pa_1*result*.json')) + list(base.rglob('deposon_pa_d1_d3*.json')):
        print(f'  FOUND {cand.relative_to(base)} sha12={sha12(cand)}')

print()
print('=== 8. 守恒残差值复算 (v19 physics_audit) ===')
v19 = REPO / 'results' / 'deposon_v19_benchmark_fixes.json'
if v19.exists():
    dv19 = json.loads(v19.read_text(encoding='utf-8'))
    s = json.dumps(dv19, ensure_ascii=False)
    m = re.findall(r'"[^"]*(?:t_plus_r_plus_a|max_deviation)[^"]*"\s*:\s*[0-9.eE+-]+', s)[:5]
    print('  v19 conservation fields:', m)
print('  _v3_review_r2_verify DONE')
