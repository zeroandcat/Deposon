import os, hashlib, sys

repo = os.path.dirname(os.path.abspath(__file__))
parent = os.path.dirname(repo)
roots = [repo, os.path.join(parent, 'deposon-sub'), os.path.join(parent, 'GLM')]
want = set('f1ca2c59bed9 8995859e5a76 6d1b14983555 9c70140c7b02 b4f00e5a69c4 78fb8c47c944 4c60dcbec07f a48fd50d8247 658db4ffff47'.split())
skip = set(['.git', 'node_modules', '__pycache__', '.venv', 'venv'])


def safe(s):
    return s if s.isascii() else s.encode('unicode_escape').decode('ascii')


n = 0
err = 0
hits = {}
for ri, r in enumerate(roots):
    if not os.path.isdir(r):
        print('ROOT_MISSING', ri, safe(r))
        continue
    for dp, dn, fn in os.walk(r):
        dn[:] = [d for d in dn if d not in skip]
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
                hits.setdefault(h, []).append((ri, os.path.relpath(p, r), len(b)))

print('REPO', safe(repo))
print('SCANNED', n, 'ERR', err)
for k in sorted(hits):
    for ri, rel, ln in hits[k]:
        print('HIT', k, ln, 'root' + str(ri), safe(rel))
print('MISS', sorted(want - set(hits)))