# -*- coding: utf-8 -*-
import tarfile, os, stat, sys
from pathlib import Path

build = Path(r"C:\deposon_compile")
deliv = Path(r"D:\私人资料\deposon-repo\.trae\deliverables")

# clean paper dirs only (keep miktex-config/data to preserve installed packages)
for lang in ("en", "cn"):
    d = build / f"deposon_arxiv_{lang}"
    if d.exists():
        def on_rm(func, path, exc):
            try:
                os.chmod(path, stat.S_IWRITE | stat.S_IREAD)
            except OSError:
                pass
            try:
                func(path)
            except OSError:
                pass
        import shutil
        shutil.rmtree(str(d), onerror=on_rm)

for lang in ("en", "cn"):
    d = build / f"deposon_arxiv_{lang}"
    with tarfile.open(str(deliv / f"deposon_arxiv_{lang}.tar.gz"), "r:gz") as tf:
        tf.extractall(str(build))
    n = 0
    for p in d.rglob("*"):
        try:
            os.chmod(str(p), stat.S_IWRITE | stat.S_IREAD)
        except OSError:
            pass
        if p.is_file():
            n += 1
    print("extracted %s: %d files" % (lang, n), flush=True)
print("EXTRACT_DONE", flush=True)
