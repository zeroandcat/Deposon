"""P-6 切换落地棒：全仓基线快照器（新名件，落 .tmp，可复跑）。

口径：sha256 hexdigest()[:12] 小写 + 字节数；排除 .git / __pycache__ /
node_modules / *.pyc。输出 JSON：{rel_path: [sha12, bytes]}。
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SKIP_DIRS = {".git", "__pycache__", "node_modules", ".pytest_cache", ".mypy_cache"}


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def snapshot(root=ROOT):
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.endswith(".pyc"):
                continue
            p = os.path.join(dirpath, fn)
            rel = os.path.relpath(p, root).replace(os.sep, "/")
            try:
                out[rel] = [sha12(p), os.path.getsize(p)]
            except OSError as e:
                out[rel] = ["ERR:%s" % e.__class__.__name__, 0]
    return out


if __name__ == "__main__":
    dest = sys.argv[1]
    snap = snapshot()
    with open(dest, "w", encoding="utf-8") as f:
        json.dump(snap, f, ensure_ascii=False, indent=1, sort_keys=True)
    print("files=%d -> %s" % (len(snap), dest))
