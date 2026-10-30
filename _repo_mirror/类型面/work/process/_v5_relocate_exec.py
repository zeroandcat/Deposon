import os, sys, json, shutil, datetime, hashlib

DRY = '-Execute' not in sys.argv
ROOTS = {'repo': r'〔本地路径已脱敏〕', 'sub': r'〔本地路径已脱敏〕'}
ARCH = r'〔归档区〕'
MAN = os.path.join(ROOTS['repo'], 'results', 'work', 'process', '_archive_move_manifest_2026_10_29.jsonl')

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

plan = []
for zone, root in ROOTS.items():
    base = os.path.join(root, 'results', 'L1', 'V5')
    if not os.path.isdir(base):
        continue
    for dp, _, fs in os.walk(base):
        for fn in fs:
            p = os.path.join(dp, fn)
            rel = os.path.relpath(p, base).replace('\\', '/')
            head = ''
            if fn.lower().endswith(('.md', '.txt')):
                try:
                    head = open(p, 'rb').read(220).decode('utf-8', errors='replace').split('\n')[0].lstrip('# ').strip()
                except Exception:
                    pass
            c = cat(head, fn)
            if c == 'V3':
                dst_root = os.path.join(root, 'results', 'L1', 'V3')
            elif c == 'V4':
                dst_root = os.path.join(root, 'results', 'L1', 'V4')
            elif c == 'SALVAGE':
                dst_root = os.path.join(root, 'results', 'work')
            else:
                continue
            dst = os.path.join(dst_root, rel.replace('/', os.sep))
            plan.append((c, zone, p, dst, rel, os.path.getsize(p)))

print('DRY_RUN' if DRY else 'EXECUTE')
print('PLAN', len(plan), 'BYTES', sum(x[5] for x in plan))
from collections import Counter
print(Counter(x[0] for x in plan))
collide = [x for x in plan if os.path.exists(x[3])]
print('COLLIDE', len(collide))
for c, zone, p, dst, rel, sz in collide[:8]:
    print('   ', zone, rel)

if not DRY:
    done, fail = 0, []
    with open(MAN, 'ab') as mf:
        for c, zone, p, dst, rel, sz in plan:
            if os.path.exists(dst):
                fail.append(('EXISTS', zone + ':' + rel)); continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            try:
                shutil.move(p, dst)
                mf.write(json.dumps({'ts': datetime.datetime.now().isoformat(timespec='seconds'),
                                     'zone': zone, 'src': p, 'dst': dst, 'bytes': sz,
                                     'why': 'PI令Q1/Q2：V5目录归位->' + c}, ensure_ascii=False).encode('utf-8') + b'\n')
                done += 1
            except Exception as e:
                fail.append((str(e), zone + ':' + rel))
    print('MOVED', done, 'FAILED', len(fail), fail[:6])
