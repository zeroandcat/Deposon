#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 · 卡答登记件（v156–v172 + supplement）全文汇读（只读）
纪律：逐件全文读；每件记其宿主指纹（SHA-12）以便「同形异义」之锚。
"""
import os, io, glob, hashlib, datetime

ROOT = r"_repo_mirror"
OUT = r"〔幽灵引用·原件已缺席·未上传:_s14_cards_full_2026_10_21.md〕"

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

def main():
    files = sorted(glob.glob(os.path.join(ROOT, "pi_rulings", "_pi_card_answers_register_2026_10_20_*.md")))
    L = []
    L.append("# §14 子棒版·卡答登记件全文汇读 · 观测时点 " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    L.append("# 件数 = %d" % len(files))
    for p in files:
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        st = os.stat(p)
        L.append("")
        L.append("=" * 70)
        L.append("### 件 = %s" % rel)
        L.append("### 指纹 = SHA12 %s · %d B · mtime %s" % (
            sha12(p), st.st_size,
            datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S")))
        L.append("=" * 70)
        with io.open(p, "r", encoding="utf-8", errors="replace") as f:
            L.append(f.read().rstrip("\n"))
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("files=", len(files), "->", OUT)

if __name__ == "__main__":
    main()
