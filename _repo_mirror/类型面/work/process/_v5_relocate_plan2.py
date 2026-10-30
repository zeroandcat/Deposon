import os
from collections import defaultdict

ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}

def cat(head, fn):
    low = fn.lower()
    h = head
    if '回捞' in h or '清卷' in h or '落册册' in h:
        return 'SALVAGE'
    if h.startswith('V5 · GT') or 'GT 系' in h or 'GT-' in h or 'GT2' in h:
        return 'V3'
    if 'P-J' in h or 'P-M' in h or 'P-C' in h:
        return 'V3'
    if h.startswith('V4 ') or h.startswith('V4·') or 'V4 论文面' in h or '确认批' in h:
        return 'V4'
    if '_v5_' in low or h.startswith('V5') or 'V5' in h:
        return 'V5_KEEP'
    return 'UNSURE'

tot = 0
g = defaultdict(list)
zone_cnt = defaultdict(int)
for zone, root in ROOTS.items():
    base = os.path.join(root, 'results', 'L1', 'V5')
    if not os.path.isdir(base):
        continue
    for dp, _, fs in os.walk(base):
        for fn in fs:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, base).replace('\\', '/')
            sz = os.path.getsize(p)
            tot += 1
            zone_cnt[zone] += 1
            head = ''
            if fn.lower().endswith(('.md', '.txt')):
                try:
                    head = open(p, 'rb').read(220).decode('utf-8', errors='replace').split('\n')[0].lstrip('# ').strip()
                except Exception:
                    pass
            g[cat(head, fn)].append((zone, rel, sz, head[:66]))

print('TOTAL', tot, dict(zone_cnt))
for k in ('V3', 'V4', 'SALVAGE', 'V5_KEEP', 'UNSURE'):
    v = g.get(k, [])
    print('  %-9s %3d 件  %12d B' % (k, len(v), sum(x[2] for x in v)))
print()
for k in ('V4', 'SALVAGE', 'UNSURE'):
    print('=== %s（前 12）===' % k)
    for zone, rel, sz, head in sorted(g.get(k, []), key=lambda x: -x[2])[:12]:
        print('  %-5s %8d %-44s %s' % (zone, sz, rel[:44], head[:48]))
    print()
