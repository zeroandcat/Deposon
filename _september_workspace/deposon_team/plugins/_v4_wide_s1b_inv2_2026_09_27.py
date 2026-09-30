# -*- coding: utf-8 -*-
"""_v4_wide_s1b_inv2 — 新件精分类（按目录 + 文件名前缀 + 扩展名）只读"""
import os, re
from datetime import datetime
from collections import defaultdict

CUTOFF = datetime(2026, 9, 23, 12, 0, 0).timestamp()
ROOTS = [r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub']
SKIP = {'__pycache__', '.git', 'node_modules', '.trae'}

rows = []
for root in ROOTS:
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            p = os.path.join(dp, fn)
            try: st = os.stat(p)
            except OSError: continue
            if st.st_mtime >= CUTOFF:
                rows.append((st.st_mtime, st.st_size, p))
rows.sort()

def rel(p): return p.replace(r'D:\私人资料' + os.sep, '')

# 按 (repo, 二级目录) 分组
g = defaultdict(list)
for mt, sz, p in rows:
    r = rel(p); parts = r.split(os.sep)
    key = os.sep.join(parts[:2]) if len(parts) > 2 else parts[0]
    g[key].append((mt, sz, r))

for k in sorted(g, key=lambda x: -len(g[x])):
    items = g[k]
    print(f'\n### {k}  ({len(items)} 件)')
    # 按文件名前缀聚类
    pref = defaultdict(int)
    for _, _, r in items:
        fn = os.path.basename(r)
        m = re.match(r'(_v4[a-z0-9_]*)', fn)
        if m: pref[m.group(1)[:26]] += 1
        elif fn.startswith('_'): pref[fn[:26]] += 1
        else: pref[fn[:26]] += 1
    for pfx in sorted(pref, key=lambda x: -pref[x])[:40]:
        print(f'    {pref[pfx]:>3}x  {pfx}')
print('\n_wide_s1b DONE')
