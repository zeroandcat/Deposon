#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 · 仪器三则：①主版节标题结构面（⛔0 读正文一字）②.tmp 分组计数＋版式面
③交付面指纹复算（漂移闸）
"""
import os, io, re, hashlib, collections, datetime

ROOT = r"_repo_mirror"
MAINMEMO = os.path.join(ROOT, "results", "_root_session_history_memo_main_2026_10_14.md")
SUBMEMO = os.path.join(ROOT, "results", "_root_session_history_memo_2026_10_14.md")
OUT = r"〔幽灵引用·原件已缺席·未上传:_s14_instrument_out_2026_10_21.md〕"
WIN_START_MS = 1792482013000

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

def byte_stats(p):
    b = open(p, "rb").read()
    cr = b.count(b"\x0d")
    bom = b[:3] == b"\xef\xbb\xbf"
    try:
        t = b.decode("utf-8")
        fffd = t.count("\ufffd")
    except Exception:
        fffd = -1
    return len(b), cr, bom, fffd, b[-1:]

def main():
    L = []
    L.append("# §14 · 仪器输出（观测时点 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "）")
    L.append("")
    L.append("## 一、主版备忘录 · 节标题结构面（⛔0 读正文一字）")
    for tag, p in (("主版", MAINMEMO), ("子棒版", SUBMEMO)):
        if not os.path.isfile(p):
            L.append("- %s：MISSING" % tag); continue
        st = os.stat(p)
        L.append("- %s：%s · %d B · mtime %s" % (
            tag, os.path.basename(p), st.st_size,
            datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S")))
        heads = []
        with io.open(p, "r", encoding="utf-8", errors="replace") as f:
            for ln, line in enumerate(f, 1):
                if re.match(r"^#{1,4}\s", line):
                    heads.append((ln, line.rstrip()))
        L.append("  - 标题行数 = %d" % len(heads))
        for ln, h in heads:
            L.append("    L%d  %s" % (ln, h))
    L.append("")
    L.append("## 二、仓根 .tmp/ 分组计数与版式面（窗口下界 2026-10-20 15:40:13）")
    tmp = os.path.join(ROOT, ".tmp")
    grp = collections.Counter()
    inwin = 0
    allc = 0
    bomf = []
    crf = []
    for dp, dn, fn in os.walk(tmp):
        for n in fn:
            p = os.path.join(dp, n)
            try:
                st = os.stat(p)
            except OSError:
                continue
            allc += 1
            if st.st_mtime_ns // 1000000 < WIN_START_MS:
                continue
            inwin += 1
            pre = re.match(r"^(_[a-z]+)", n)
            grp[pre.group(1) if pre else "(其他)"] += 1
            nb, cr, bom, fffd, last = byte_stats(p)
            if bom:
                bomf.append((n, nb, os.path.relpath(p, ROOT)))
            if cr:
                crf.append((n, cr, nb))
    L.append("- .tmp/ 全量件数 = %d（观测时点同左）" % allc)
    L.append("- 窗内新增/改写件数 = %d" % inwin)
    for k, v in sorted(grp.items(), key=lambda x: (-x[1], x[0])):
        L.append("  - 前缀 %s : %d" % (k, v))
    L.append("- 含 BOM 件数 = %d" % len(bomf))
    for n, nb, rel in sorted(bomf)[:40]:
        L.append("    BOM  %s · %d B · %s" % (n, nb, rel))
    L.append("- 含 CR 字节件数 = %d" % len(crf))
    for n, cr, nb in sorted(crf)[:40]:
        L.append("    CR=%d  %s · %d B" % (cr, n, nb))
    L.append("")
    L.append("## 三、交付面漂移闸（results/ + pi_rulings/ 窗内件之指纹复算）")
    rows = []
    for surf in ("results", "pi_rulings", "letters"):
        base = os.path.join(ROOT, surf)
        for dp, dn, fn in os.walk(base):
            for n in fn:
                p = os.path.join(dp, n)
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime_ns // 1000000 < WIN_START_MS:
                    continue
                rel = os.path.relpath(p, ROOT).replace("\\", "/")
                if "/.tmp/" in rel:
                    continue
                rows.append((rel, st.st_size, sha12(p)))
    rows.sort()
    for rel, nb, s in rows:
        L.append("- %s | %d B | %s" % (s, nb, rel))
    L.append("- 交付面窗内件计数（除 .tmp）= %d" % len(rows))
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("ok ->", OUT, "| tmp_all=", allc, "tmp_inwin=", inwin, "| delivery_rows=", len(rows))

if __name__ == "__main__":
    main()
