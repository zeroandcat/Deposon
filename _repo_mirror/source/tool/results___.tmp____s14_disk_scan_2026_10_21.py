#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 子棒版·盘上落盘面扫描器（长名式递归·mtime 序·逐件指纹自测）
纪律：⛔0 单用 -Filter；⛔0 读 key/.env；⛔0 删改任何件。
窗口：2026-10-20 15:40:13 CST → 观测时点
"""
import os, sys, hashlib, json, io, datetime

ROOT = r"_repo_mirror"
WIN_START_MS = 1792482013000  # 2026-10-20 15:40:13 CST（= §13-7 落盘 mtime）·复核修正：首版误设 1792510813000（=23:40:13·偏 +8h）已改
OBS_LABEL = sys.argv[1] if len(sys.argv) > 1 else "scan"

SURFACES = ["results", "pi_rulings", "letters", "docs", "tools", ".tmp"]

def sha12(p):
    h = hashlib.sha256()
    try:
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        return h.hexdigest()[:12].upper()
    except Exception as e:
        return "ERR:" + type(e).__name__

def scan_surface(rel):
    base = os.path.join(ROOT, rel)
    rows = []
    if not os.path.isdir(base):
        return rows
    for dp, dn, fn in os.walk(base):
        for n in fn:
            p = os.path.join(dp, n)
            try:
                st = os.stat(p)
            except OSError:
                continue
            if st.st_mtime_ns // 1000000 < WIN_START_MS:
                continue
            rows.append({
                "surface": rel,
                "relpath": os.path.relpath(p, ROOT).replace("\\", "/"),
                "bytes": st.st_size,
                "mtime_ms": st.st_mtime_ns // 1000000,
                "sha12": sha12(p),
            })
    return rows

def main():
    obs = datetime.datetime.now()
    allrows = []
    for s in SURFACES:
        allrows.extend(scan_surface(s))
    allrows.sort(key=lambda r: (r["mtime_ms"], r["relpath"]))
    by_surface = {}
    for r in allrows:
        by_surface.setdefault(r["surface"], []).append(r)
    lines = []
    lines.append("# §14 子棒版·盘上落盘面扫描 · 观测时点 " + obs.strftime("%Y-%m-%d %H:%M:%S"))
    lines.append("# 窗口下界 = 2026-10-20 15:40:13 CST（=%d ms）·长名式递归（⛔0 单用 -Filter）" % WIN_START_MS)
    lines.append("# 总件数 = %d" % len(allrows))
    lines.append("")
    for s in SURFACES:
        rows = by_surface.get(s, [])
        lines.append("## surface=%s  件数=%d" % (s, len(rows)))
        for r in rows:
            lines.append("%s | %d B | %s | %s" % (
                datetime.datetime.fromtimestamp(r["mtime_ms"] / 1000).strftime("%m-%d %H:%M:%S"),
                r["bytes"], r["sha12"], r["relpath"]))
        lines.append("")
    out = os.path.join(ROOT, "results", ".tmp", "_s14_disk_scan_out_%s.md" % OBS_LABEL)
    with io.open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    print("WROTE", out, "rows=", len(allrows))
    for s in SURFACES:
        print("  %-10s %d" % (s, len(by_surface.get(s, []))))

if __name__ == "__main__":
    main()
