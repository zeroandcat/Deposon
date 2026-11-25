import os, sys
from collections import defaultdict

ROOT = r'〔本地路径已脱敏〕'
SUB = r'〔本地路径已脱敏〕'
BASE = os.path.join(ROOT, 'results', 'L1', 'V5')

def cat(head, fn):
    h = head
    if '回捞' in h or '清卷' in h or '落册册' in h:
        return 'SALVAGE'
    if h.startswith('V5 · GT') or 'GT 系' in h or 'GT-' in h or 'GT2' in h:
        return 'V3'
    if 'P-J' in h or 'P-M' in h or 'P-C' in h:
        return 'V3'
    if h.startswith('V4') or 'V4 ' in h[:8]:
        return 'V4'
    if 'V5' in h:
        return 'V5_KEEP'
    return 'UNSURE'

rows = []
for dp, _, fs in os.walk(BASE):
    for fn in fs:
        p = os.path.join(dp, fn)
        rel = os.path.relpath(p, BASE).replace('\\', '/')
        sz = os.path.getsize(p)
        head = ''
        if fn.lower().endswith(('.md', '.txt')):
            try:
                head = open(p, 'rb').read(220).decode('utf-8', errors='replace').split('\n')[0].lstrip('# ').strip()
            except Exception:
                pass
        rows.append((cat(head, fn), rel, sz, head[:70]))

g = defaultdict(list)
for c, rel, sz, head in rows:
    g[c].append((rel, sz, head))

print('TOTAL', len(rows))
for k in ('V3', 'V4', 'SALVAGE', 'V5_KEEP', 'UNSURE'):
    v = g.get(k, [])
    print('  %-9s %3d 件  %12d B' % (k, len(v), sum(x[1] for x in v)))
print()
for k in ('V3', 'SALVAGE', 'UNSURE'):
    print('=== %s ===' % k)
    for rel, sz, head in sorted(g.get(k, []), key=lambda x: -x[1])[:10]:
        print('  %8d %-46s %s' % (sz, rel[:46], head[:52]))
    print()
