import os, hashlib, json, sys

ROOT = r'_repo_mirror'
want = set(['609943436a0d', 'a8a9018fd67e', '3ea469e5a6f3'])
skip_dirs = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', '.tmp', '.mavis', '.trae'}


def safe(s):
    return s if s.isascii() else s.encode('unicode_escape').decode('ascii')


n = 0
err = 0
hits = {}
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in skip_dirs]
    for f in fn:
        if f.lower().startswith('.env'):
            continue
        p = os.path.join(dp, f)
        try:
            b = open(p, 'rb').read()
        except Exception:
            err += 1
            continue
        n += 1
        h = hashlib.sha256(b).hexdigest()[:12]
        if h in want:
            hits.setdefault(h, []).append((os.path.relpath(p, ROOT), len(b)))

print('SCANNED', n, 'ERR', err)
for k in sorted(hits):
    for rel, ln in hits[k]:
        print('HIT', k, ln, safe(rel))
print('MISS', sorted(want - set(hits)))
