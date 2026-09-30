# -*- coding: utf-8 -*-
"""E-48 只读复算脚本 2：排除面（0 处 E-41 命中件）SHA-12 + 字节。"""
import glob
import hashlib
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

RES = r"D:\私人资料\deposon-repo\results"

# 排除面：全部 rescript 件（含子目录），逐件判定 E-41 命中
paths = []
for p in glob.glob(os.path.join(RES, "**", "*rescript*.md"), recursive=True):
    paths.append(p)
paths.sort()

print("total_rescript_md_on_disk =", len(paths))
print("")
print("path\tsha12\tbytes\tE41_hits\tdeclared_in_E48")
TARGET = {
    "434b3213bdce", "2e0f6b8bf141", "88b7eaf8675d", "2e08b9ae9f09",
    "78f3aba1f24c", "fc0ffd27adca", "1cd36ac1b2c0", "82a947f2aebd",
    "6b86576146a3", "c300e74a082c", "6f045bdc70e7", "a0734e0a6860",
}
n_t = 0
for p in paths:
    d = open(p, "rb").read()
    h = hashlib.sha256(d).hexdigest()[:12]
    t = d.decode("utf-8")
    hits = t.count("E-41")
    rel = os.path.relpath(p, RES).replace("\\", "/")
    mark = "YES" if h in TARGET else "no"
    if h in TARGET:
        n_t += 1
    print("%s\t%s\t%d\t%d\t%s" % (rel, h, len(d), hits, mark))
print("")
print("declared_in_E48_count =", n_t)
