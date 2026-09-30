import hashlib, os, sys

targets = set(sys.argv[1:])
base = 'D:/私人资料/deposon-repo'
skip = {'.git', 'node_modules', '__pycache__', '.venv', 'venv'}
n = 0
for root, dirs, files in os.walk(base):
    dirs[:] = [d for d in dirs if d not in skip]
    for f in files:
        p = os.path.join(root, f)
        try:
            b = open(p, 'rb').read()
        except Exception:
            continue
        n += 1
        h = hashlib.sha256(b).hexdigest()[:12]
        if h in targets:
            print(h, len(b), os.path.relpath(p, base).replace('\\', '/'))
print('SCANNED', n, file=sys.stderr)
