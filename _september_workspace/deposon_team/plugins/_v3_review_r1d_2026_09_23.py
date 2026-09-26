# -*- coding: utf-8 -*-
"""R1d: v7_summary 定位 + deposon-sub 结构概览 + _non_upload_local_archive 概览。"""
import os
from pathlib import Path

base = Path(r'D:\私人资料')
ROOT = base / 'deposon-repo'

print('=== v7_summary 全域搜索 (两个归档区) ===')
for zone in [base / 'deposon-sub', base / '_non_upload_local_archive']:
    if zone.exists():
        hits = list(zone.rglob('deposon_v3_v7_summary*'))
        print(f'  {zone.name}: {[str(h.relative_to(zone)) for h in hits] if hits else "无"}')

print()
print('=== deposon-sub 一级结构 ===')
sub = base / 'deposon-sub'
for p in sorted(sub.iterdir()):
    if p.is_dir():
        n = sum(1 for _ in p.iterdir() if _.is_file())
        print(f'  {p.name}/ ({n} files)')
    else:
        print(f'  {p.name}  {p.stat().st_size}B')

print()
print('=== deposon-sub/results 中与本委托相关件 (boss_*/d7_*/d_fix2/attack_*) ===')
sr = sub / 'results'
if sr.exists():
    for pat in ['boss_*.json', 'd7_*.json', 'attack_*.json', 'adendum_*.json', '_p_l*.json']:
        fs = sorted(sr.glob(pat))
        if fs:
            print(f'  {pat}: {len(fs)} 件')
            for f in fs[:8]:
                print(f'     {f.name}  {f.stat().st_size}B')
# P-系 runner 在 sub 根
print('  sub 根 _p_* runner:')
for p in sorted(sub.glob('_p_*')):
    print(f'     {p.name}  {p.stat().st_size}B')

print()
print('=== _non_upload_local_archive 一级结构 ===')
nu = base / '_non_upload_local_archive'
for p in sorted(nu.iterdir())[:25]:
    if p.is_dir():
        n = sum(1 for _ in p.iterdir() if _.is_file())
        print(f'  {p.name}/ ({n} files)')
    else:
        print(f'  {p.name}  {p.stat().st_size}B')

print()
print('_r1d DONE')
