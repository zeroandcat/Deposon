# -*- coding: utf-8 -*-
"""R1c: 追查消失资产去向 — 09_20/09_21 归档清单 + repo 外归档目录 + manifest 对照。"""
import hashlib, os
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
sha12 = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12].upper()

print('=== results/_archive_2026_09_20 内容 (3 files) ===')
for p in sorted((ROOT / 'results' / '_archive_2026_09_20').iterdir()):
    print(f'  {p.name}  {p.stat().st_size}B')

print()
print('=== results/_archive_2026_09_21 内容 (31 files) ===')
for p in sorted((ROOT / 'results' / '_archive_2026_09_21').iterdir()):
    print(f'  {p.name}  {p.stat().st_size}B')

print()
print('=== repo 外候选归档目录 (D:\\私人资料 一级) ===')
base = Path(r'D:\私人资料')
for p in sorted(base.iterdir()):
    if p.is_dir() and ('archive' in p.name.lower() or 'deposon' in p.name.lower()):
        n = sum(1 for _ in p.rglob('*') if _.is_file()) if p.name != 'deposon-repo' else '?'
        print(f'  {p.name}/  ({n} files)')

print()
print('=== 关键单件全盘定位（D:\\私人资料 全域搜索，限深 4） ===')
KEY = ['boss_pa_1_rbr_rm_result_2026_09_15.json',
       'boss_pa_2_potential_game_result_2026_09_15.json',
       'd7_5anchor_60cells_9model_verdict_2026_09_18.json',
       '_p_l_v3_phase1_runner_2026_09_17.py',
       'deposon_v3_v7_summary_2026_09_11.json',
       'attack_pc_a1_resampling_2026_09_15.json']
found = {}
for dp, dns, fns in os.walk(base):
    depth = dp.count(os.sep) - base.as_posix().count('/')
    if depth > 4 or '.git' in dp or '__pycache__' in dp:
        dns[:] = []
        continue
    for f in fns:
        if f in KEY and (os.path.join(dp, f) not in [str(v[0]) for v in found.values() if v]):
            p = Path(dp) / f
            if 'deposon-repo' in dp and 'results' in dp:
                pass  # repo 内 results 已核
            try:
                found.setdefault(f, []).append((str(p), p.stat().st_size))
            except OSError:
                pass
for k in KEY:
    v = found.get(k, [])
    repo_hits = [x for x in v if 'deposon-repo' in x[0] and '_archive' in x[0]]
    ext_hits = [x for x in v if 'deposon-repo' not in x[0]]
    print(f'  {k}:')
    print(f'    repo 归档命中: {[x[0] for x in repo_hits] if repo_hits else "无"}')
    print(f'    repo 外命中:   {[x[0] for x in ext_hits[:3]] if ext_hits else "无"}')

print()
print('=== results/ 根现存全部文件计数 ===')
allr = [p for p in (ROOT / 'results').iterdir() if p.is_file()]
print(f'  results/ 根: {len(allr)} files')
v4c = [p for p in allr if p.name.startswith('_v4')]
print(f'  其中 _v4_*: {len(v4c)}')
print(f'  其中非 _v4: {len(allr) - len(v4c)}')
nonv4 = sorted(p.name for p in allr if not p.name.startswith('_v4'))
for n in nonv4[:40]:
    print(f'    {n}')
if len(nonv4) > 40:
    print(f'    ... +{len(nonv4)-40}')

print()
print('_r1c DONE')
