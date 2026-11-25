#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 子棒版备忘录续修·落盘器（append-only）
流程：停手闸（三法复测·不符即停手）→ 占位符实测替换 → append-only 追加（UTF-8 无 BOM·纯 LF）
      → 落盘后独立回读＋字节级自报（SHA-12/bytes/BOM/0x0D/U+FFFD/末字节/LF）
      → 前缀字节自证 → 长名式递归复测在盘（唯一命中）
纪律：⛔0 改写既有字节；⛔0 单用 -Filter；⛔0 删改任何他件。
"""
import os, io, re, sys, glob, hashlib, datetime, collections

ROOT = r"_repo_mirror"
TARGET = os.path.join(ROOT, "results", "_root_session_history_memo_2026_10_14.md")
BODY = os.path.join(ROOT, "results", ".tmp", "_s14_body_2026_10_21.md")
REPORT = os.path.join(ROOT, "results", ".tmp", "_s14_append_report_2026_10_21.md")
WIN_START_MS = 1792482013000
EXPECT_SHA12 = "92D7A9B8B877"
EXPECT_BYTES = 316601
SURFACES = ("results", "pi_rulings", "letters", "docs", "tools")

def sha_all(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()

def stats(p):
    b = open(p, "rb").read()
    cr = b.count(b"\x0d")
    lf = b.count(b"\x0a")
    bom = b[:3] == b"\xef\xbb\xbf"
    try:
        fffd = b.decode("utf-8").count("\ufffd")
    except Exception:
        fffd = -1
    return len(b), lf, cr, bom, fffd, b[-1:]

def measure_delivery():
    rows = []
    for surf in SURFACES:
        base = os.path.join(ROOT, surf)
        for dp, dn, fn in os.walk(base):
            for n in fn:
                p = os.path.join(dp, n)
                rel = os.path.relpath(p, ROOT).replace("\\", "/")
                if "/.tmp/" in rel:
                    continue
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime_ns // 1000000 < WIN_START_MS:
                    continue
                rows.append((st.st_mtime_ns // 1000000, rel, st.st_size, sha_all(p)[:12].upper()))
    rows.sort()
    return rows

def measure_tmp():
    tmp = os.path.join(ROOT, ".tmp")
    grp = collections.Counter()
    n = 0
    bom = 0
    cr = 0
    for dp, dn, fn in os.walk(tmp):
        for f in fn:
            p = os.path.join(dp, f)
            try:
                st = os.stat(p)
            except OSError:
                continue
            if st.st_mtime_ns // 1000000 < WIN_START_MS:
                continue
            n += 1
            m = re.match(r"^(_[a-z]+)", f)
            grp[m.group(1) if m else "(其他)"] += 1
            b = open(p, "rb").read()
            if b[:3] == b"\xef\xbb\xbf":
                bom += 1
            if b.count(b"\x0d"):
                cr += 1
    return n, grp, bom, cr

def measure_mine():
    fs = sorted(glob.glob(os.path.join(ROOT, "results", ".tmp", "_s14*")))
    lines = []
    for p in fs:
        lines.append("- `%s` ｜ %d B ｜ %s" % (sha_all(p)[:12].upper(), os.path.getsize(p),
                                             os.path.basename(p)))
    return fs, lines

def main():
    obs = datetime.datetime.now()
    L = []
    L.append("# §14 落盘报告（观测时点 %s）" % obs.strftime("%Y-%m-%d %H:%M:%S"))

    # ── 停手闸：三法复测 ──
    h1 = sha_all(TARGET); h2 = sha_all(TARGET); h3 = sha_all(TARGET)
    nb, lf, cr, bom, fffd, last = stats(TARGET)
    L.append("## 一、停手闸（落笔前·三法复测）")
    L.append("- SHA-256 #1 = %s" % h1)
    L.append("- SHA-256 #2 = %s" % h2)
    L.append("- SHA-256 #3 = %s" % h3)
    L.append("- SHA-12 = %s（期望 %s）" % (h1[:12].upper(), EXPECT_SHA12))
    L.append("- bytes = %d（期望 %d）" % (nb, EXPECT_BYTES))
    L.append("- LF = %d ｜ 0x0D = %d ｜ BOM = %s ｜ U+FFFD = %d ｜ 末字节 = %s" % (lf, cr, bom, fffd, last.hex()))
    ok = (h1 == h2 == h3 and h1[:12].upper() == EXPECT_SHA12 and nb == EXPECT_BYTES
          and cr == 0 and bom is False and fffd == 0 and last == b"\x0a")
    L.append("- **停手闸判定 = %s**" % ("PASS ✅（不符则停手·本棒未触发）" if ok else "FAIL ⛔"))
    if not ok:
        with io.open(REPORT, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(L) + "\n")
        print("STOPGATE FAIL — no append. See", REPORT)
        return 2

    # ── 实测占位符 ──
    rows = measure_delivery()
    per = collections.Counter(r[1].split("/")[0] for r in rows)
    tmp_n, grp, tmp_bom, tmp_cr = measure_tmp()
    mine, mine_lines = measure_mine()
    idx_count = 0
    seen = set()
    for dp, dn, fn in os.walk(ROOT):
        for f in fn:
            p = os.path.join(dp, f)
            try:
                if os.path.getsize(p) > 40 * 1024 * 1024:
                    continue
                s = sha_all(p)[:12].upper()
            except OSError:
                continue
            if s not in seen:
                seen.add(s)
                idx_count += 1
    body = io.open(BODY, "r", encoding="utf-8").read()
    dtab = []
    for mt, rel, sz, s in rows:
        dtab.append("- %s ｜ %s ｜ %d B ｜ `%s`" % (
            datetime.datetime.fromtimestamp(mt / 1000).strftime("%m-%d %H:%M:%S"), s, sz, rel))
    dtab = "\n".join(dtab)
    tgroups = "\n".join("- 前缀 `%s` : %d" % (k, v) for k, v in sorted(grp.items(), key=lambda x: (-x[1], x[0])))
    tgroups += "\n- （其他前缀之合计已含于「(其他)」行）"
    subst = {
        "{{OBS_TIME}}": obs.strftime("%Y-%m-%d %H:%M:%S"),
        "{{DELIVERY_COUNT}}": str(len(rows)),
        "{{C_RESULTS}}": str(per.get("results", 0)),
        "{{C_PI}}": str(per.get("pi_rulings", 0)),
        "{{C_LETTERS}}": str(per.get("letters", 0)),
        "{{DELIVERY_TABLE}}": dtab,
        "{{TMP_COUNT}}": str(tmp_n),
        "{{TMP_GROUPS}}": tgroups,
        "{{TMP_BOM}}": str(tmp_bom),
        "{{TMP_CR}}": str(tmp_cr),
        "{{MY_COUNT}}": str(len(mine)),
        "{{MY_FILES}}": "\n".join(mine_lines),
        "{{IDX_COUNT}}": str(idx_count),
        "{{KEY_SCAN_COUNT}}": str(len(rows)),
        "{{MAIN_RECORDS}}": "774",
        "{{BRANCH_RECORDS}}": "966",
    }
    for k, v in subst.items():
        body = body.replace(k, v)
    left = re.findall(r"\{\{[A-Z_]+\}\}", body)
    if left:
        L.append("- ⛔ 仍有未替换占位符：%s → **停手**" % sorted(set(left)))
        with io.open(REPORT, "w", encoding="utf-8", newline="\n") as f:
            f.write("\n".join(L) + "\n")
        print("UNSUBSTITUTED:", sorted(set(left)))
        return 3
    body = body.replace("\r\n", "\n").replace("\r", "\n")
    L.append("")
    L.append("## 二、实测替换值")
    for k in ("DELIVERY_COUNT", "C_RESULTS", "C_PI", "C_LETTERS", "TMP_COUNT", "TMP_BOM", "TMP_CR",
              "MY_COUNT", "IDX_COUNT", "KEY_SCAN_COUNT"):
        L.append("- %s = %s" % (k, subst["{{%s}}" % k]))

    # ── append-only 追加 ──
    with open(TARGET, "ab") as f:
        f.write(body.encode("utf-8"))
    L.append("")
    L.append("## 三、落盘后独立回读·字节级自报")
    nb2, lf2, cr2, bom2, fffd2, last2 = stats(TARGET)
    h_after = sha_all(TARGET)
    pref = open(TARGET, "rb").read(EXPECT_BYTES)
    pref_h = hashlib.sha256(pref).hexdigest()
    L.append("- SHA-12 = %s" % h_after[:12].upper())
    L.append("- SHA-256 = %s" % h_after)
    L.append("- bytes = %d（落笔前 %d ⇒ 追加幅 = %d B）" % (nb2, EXPECT_BYTES, nb2 - EXPECT_BYTES))
    L.append("- LF = %d（落笔前 %d）" % (lf2, lf))
    L.append("- 0x0D = %d ／ BOM = %s ／ U+FFFD = %d ／ 末字节 = %s" % (cr2, bom2, fffd2, last2.hex()))
    L.append("- **三零自报 = %s**" % ("BOM=0 ✅ ／ CR=0 ✅ ／ U+FFFD=0 ✅" if (bom2 is False and cr2 == 0 and fffd2 == 0) else "FAIL ⛔"))
    L.append("- 前缀 %d 字节之 SHA-256 = %s" % (EXPECT_BYTES, pref_h))
    L.append("- 前缀自证 = %s" % ("历史字节 0 触动 ✅" if pref_h == h1 else "FAIL ⛔"))
    L.append("- 末字节 = %s（应为 0x0a）" % last2.hex())

    # ── 长名式复测在盘 ──
    hits = []
    for dp, dn, fn in os.walk(ROOT):
        for f in fn:
            if f == "_root_session_history_memo_2026_10_14.md":
                hits.append(os.path.join(dp, f))
    L.append("")
    L.append("## 四、长名式递归复测在盘（精确长名）")
    L.append("- 命中数 = %d" % len(hits))
    for h in hits:
        L.append("  - %s" % h)
    L.append("- 唯一性 = %s" % ("✅ 1（唯一）" if len(hits) == 1 else "⛔ 非唯一"))
    with io.open(REPORT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("\n".join(L[-22:]))
    print("->", REPORT)
    return 0

if __name__ == "__main__":
    sys.exit(main())
