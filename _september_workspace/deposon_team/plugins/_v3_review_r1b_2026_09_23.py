# -*- coding: utf-8 -*-
"""R1 补充: 定位 P-系 runner 归档位置 + 归档目录全景 + boss 结果 JSON 历史去向。"""
import hashlib
from pathlib import Path

ROOT = Path(r'D:\私人资料\deposon-repo')
sha12 = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12].upper()

print('=== 全部归档/迁移目录 ===')
for p in sorted(ROOT.rglob('_archive*')):
    if p.is_dir():
        n = sum(1 for _ in p.rglob('*') if _.is_file())
        print(f'  {p.relative_to(ROOT)}  ({n} files)')

print()
print('=== results/ 下一级目录全景 ===')
for p in sorted((ROOT / 'results').iterdir()):
    if p.is_dir():
        n = sum(1 for _ in p.iterdir() if _.is_file())
        print(f'  {p.name}/  ({n} files)')

print()
print('=== P-系 runner 定位 (全树 rglob _p_?.*) ===')
for pat in ['_p_i_*', '_p_j_*', '_p_k_*', '_p_l_*', '_p_m_*', '_p_n_*', '_p_o_*']:
    hits = [str(p.relative_to(ROOT)) for p in ROOT.rglob(pat) if p.is_file()]
    for h in hits[:3]:
        p = ROOT / h
        print(f'  {pat} -> {h}  {sha12(p)}  {p.stat().st_size}B')
    if len(hits) > 3:
        print(f'  {pat} ... +{len(hits)-3}')
    if not hits:
        print(f'  {pat} -> NONE')

print()
print('=== boss 结果 JSON 全树搜索 (boss_pa/boss_pc/boss_pe) ===')
for p in sorted(ROOT.rglob('boss_*.json')):
    print(f'  {p.relative_to(ROOT)}  {sha12(p)}  {p.stat().st_size}B')
print('  (若上方无输出 = 全树 0 件)')

print()
print('=== d7 / d_fix2 / 1week kill / v42 数据件定位 ===')
for pat in ['*d7_*.json', '*d_fix2*.json', '*1week*', '*v42*.json']:
    hits = sorted((ROOT / 'results').glob(pat)) + sorted((ROOT / 'docs' / 'V3X').glob(pat))
    for p in hits[:10]:
        print(f'  {p.relative_to(ROOT)}  {sha12(p)}  {p.stat().st_size}B')

print()
print('_r1b DONE')
