# -*- coding: utf-8 -*-
"""§12 夜链补录 · 窗口指纹实测扫描器（只读）
窗口断点: 2026-10-19 19:36:05（子棒版备忘录 §11 落盘时点）
⛔ 只读扫描 · 0 写既有件 · 0 读 key/.env · 0 联网
"""
import os, sys, hashlib, io, json

ROOT = r"_repo_mirror"
BREAK_TS = 1787  # placeholder, replaced below by mtime compare

def ts(p):
    return os.path.getmtime(p)

BREAK_MTIME = ts(os.path.join(ROOT, "results", "_root_session_history_memo_2026_10_14.md"))
# 断点 = 子棒版备忘录自身落盘时点（19:36:05）— 严格大于此者为窗口内件
SCAN_DIRS = ["results", "pi_rulings", "letters", "docs", "tools", "scripts", "tests", "corpus",
             "attacks", "reviews", "verifier", "_field_sources", "paper", "deposon_team",
             "_remote_pullback_2026_10_17"]

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

rows = []
errors = []
for d in SCAN_DIRS:
    rp = os.path.join(ROOT, d)
    if not os.path.isdir(rp):
        continue
    for dirpath, dirnames, filenames in os.walk(rp):
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                m = os.path.getmtime(p)
            except OSError as e:
                errors.append((p, str(e)))
                continue
            if m <= BREAK_MTIME:
                continue
            try:
                b = open(p, "rb").read()
            except OSError as e:
                errors.append((p, str(e)))
                continue
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            txt = b.decode("utf-8", errors="replace")
            rows.append({
                "rel": rel,
                "sha12": sha256(p)[:12].upper(),
                "bytes": len(b),
                "lf": txt.count("\n"),
                "crlf": txt.count("\r\n"),
                "cr": txt.count("\r"),
                "bom": b[:3] == b"\xef\xbb\xbf",
                "fffd": txt.count("\ufffd"),
                "mtime": m,
                "mtimestr": __import__("time").strftime("%Y-%m-%d %H:%M:%S", __import__("time").localtime(m)),
            })

rows.sort(key=lambda r: r["mtime"])
print("BREAK_MTIME=%s" % __import__("time").strftime("%Y-%m-%d %H:%M:%S", __import__("time").localtime(BREAK_MTIME)))
print("COUNT=%d  WALK_ERRORS=%d" % (len(rows), len(errors)))
for r in rows:
    print("%-70s | %s | %9d | LF=%-5d CRLF=%-3d CR=%-3d BOM=%-5s FFFD=%d | %s" % (
        r["rel"], r["sha12"], r["bytes"], r["lf"], r["crlf"], r["cr"], r["bom"], r["fffd"], r["mtimestr"]))
if errors:
    print("ERRORS:")
    for p, e in errors:
        print("  ", p, e)
