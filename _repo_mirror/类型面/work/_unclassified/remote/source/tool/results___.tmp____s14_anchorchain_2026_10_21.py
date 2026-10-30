#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 · 证据链核验面：窗内交付件所引指纹 ↔ 本棒实测指纹（MATCH／MISMATCH／ABSENT）
纪律：⛔0 以「似缺件」充断言——路径假阴性以全仓长名式递归复扫兜底；
      ⛔0 读 key 本身；⛔0 输出凭据明文。
"""
import os, io, re, json, glob, hashlib, datetime, collections

ROOT = r"_repo_mirror"
OUT = r"〔幽灵引用·原件已缺席·未上传:_s14_anchorchain_2026_10_21.md〕"
WIN_START_MS = 1792482013000

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

def build_index():
    """全仓长名式递归索引：sha12 -> [relpaths]"""
    idx = collections.defaultdict(list)
    for dp, dn, fn in os.walk(ROOT):
        for n in fn:
            p = os.path.join(dp, n)
            try:
                if os.path.getsize(p) > 40 * 1024 * 1024:
                    continue
            except OSError:
                continue
            try:
                idx[sha12(p)].append(os.path.relpath(p, ROOT).replace("\\", "/"))
            except OSError:
                continue
    return idx

def main():
    t0 = datetime.datetime.now()
    idx = build_index()
    L = []
    L.append("# §14 · 锚链核验（观测时点 %s）" % t0.strftime("%Y-%m-%d %H:%M:%S"))
    L.append("# 索引口径＝全仓长名式递归（⛔0 单用 -Filter）·索引件数 = %d 个唯一指纹" % len(idx))
    L.append("")
    # 源件：窗内 pi_rulings 卡答登记件 + 窗内 results 交付件（取含 12-hex 指纹者）
    srcs = []
    for surf in ("pi_rulings", "results"):
        for dp, dn, fn in os.walk(os.path.join(ROOT, surf)):
            for n in fn:
                p = os.path.join(dp, n)
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime_ns // 1000000 < WIN_START_MS:
                    continue
                if "/.tmp/" in p.replace("\\", "/"):
                    continue
                srcs.append(p)
    srcs.sort()
    L.append("# 源件（窗内交付面）件数 = %d" % len(srcs))
    L.append("")
    pat = re.compile(r"\b([0-9A-Fa-f]{12})\b")
    per_file = []
    total_ref = 0
    match = 0
    mismatch = 0
    absent = 0
    for p in srcs:
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        try:
            txt = io.open(p, "r", encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        toks = [m.group(1).upper() for m in pat.finditer(txt)]
        # 去重保序
        seen = []
        for t in toks:
            if t not in seen:
                seen.append(t)
        if not seen:
            continue
        mm = 0; mi = 0; ab = 0
        rows = []
        for t in seen:
            total_ref += 1
            if t in idx:
                mm += 1; match += 1
                rows.append((t, "MATCH", idx[t]))
            else:
                ab += 1; absent += 1
                rows.append((t, "ABSENT", []))
        per_file.append((rel, len(seen), mm, ab, rows))
    L.append("## 逐件锚链（源件 → 所引指纹 → 本棒索引）")
    for rel, n, mm, ab, rows in per_file:
        L.append("")
        L.append("### %s ｜ 引用 %d ｜ MATCH %d ｜ ABSENT %d" % (rel, n, mm, ab))
        for t, stt, paths in rows:
            ps = "；".join(paths[:3]) if paths else "—"
            L.append("- `%s` → %s ｜ %s" % (t, stt, ps))
    L.append("")
    L.append("## 合计")
    L.append("- 唯一指纹引用总数 = %d" % total_ref)
    L.append("- MATCH = %d" % match)
    L.append("- ABSENT = %d" % absent)
    L.append("- MISMATCH = 0（本棒索引为「按指纹寻址」之全仓索引——凡引指纹皆按值寻址，故不产生 MISMATCH 之目；MISMATCH 之可能仅见于「件名 → 指纹」之指名路径）")
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("srcs=", len(srcs), "refs=", total_ref, "match=", match, "absent=", absent, "->", OUT)

if __name__ == "__main__":
    main()
