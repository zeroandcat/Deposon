# -*- coding: utf-8 -*-
"""E-48 只读探测：改判总表并发写状态 + #1/#4 采纳面。一次性快照。"""
import hashlib
import io
import os
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

p = r"D:\私人资料\deposon-repo\results\_v3_recheck_verdict_register_2026_09_27.md"
d = open(p, "rb").read()
print("NOW sha12=", hashlib.sha256(d).hexdigest()[:12], "bytes=", len(d), "mtime=", os.path.getmtime(p))
t = d.decode("utf-8")
L = t.split("\n")
print("lines=", len(L))
pat = re.compile(r"(2026-09-28|采纳|双判|ask_90f108da8b781eece9c90088|ask_[0-9a-f]{24})")
n = 0
for i, ln in enumerate(L):
    if pat.search(ln):
        n += 1
        if n <= 40:
            print(i + 1, "|", ln.strip()[:180])
print("total_hits=", n)
print("--- last 6 lines ---")
for ln in L[-6:]:
    print("   ", ln[:180])
