# -*- coding: utf-8 -*-
"""
_v4_wide_s1_inventory — 自 2026-09-23 12:00 起，deposon-repo 与 deposon-sub 全部新件盘点
口径：mtime >= 2026-09-23 12:00:00 (本机时区)。只读，仅 stdout。
"""
import os, time
from datetime import datetime
from collections import defaultdict

CUTOFF = datetime(2026, 9, 23, 12, 0, 0).timestamp()
ROOTS = [r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub']
SKIP_DIR = {'__pycache__', '.git', 'node_modules', '.trae'}

rows = []
for root in ROOTS:
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIR]
        for fn in fns:
            p = os.path.join(dp, fn)
            try:
                st = os.stat(p)
            except OSError:
                continue
            if st.st_mtime >= CUTOFF:
                rows.append((st.st_mtime, st.st_size, p))

rows.sort()
print(f'=== 新件总数（mtime >= 2026-09-23 12:00）= {len(rows)} ===')
print()

by_top = defaultdict(list)
for mt, sz, p in rows:
    # 归组：repo名 + 一级/二级目录
    parts = p.split(os.sep)
    tag = os.sep.join(parts[:4]) if len(parts) > 4 else os.sep.join(parts[:-1])
    by_top[tag].append((mt, sz, p))

print('=== 按目录归组 ===')
tot = 0
for tag in sorted(by_top, key=lambda t: -len(by_top[t])):
    g = by_top[tag]
    tot += len(g)
    print(f'  {len(g):>4} 件  {tag}')
print(f'  ---- 合计 {tot}')

print()
print('=== 逐件（时间 / 字节 / 路径） ===')
for mt, sz, p in rows:
    ts = datetime.fromtimestamp(mt).strftime('%m-%d %H:%M:%S')
    rel = p.replace(r'D:\私人资料' + os.sep, '')
    print(f'  {ts}  {sz:>9,}  {rel}')
print('_wide_s1 DONE')
