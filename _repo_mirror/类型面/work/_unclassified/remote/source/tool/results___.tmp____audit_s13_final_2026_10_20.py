#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
审计扫描器 v13-C · 落笔前最终一致测量 · 2026-10-20
纪律：只读；⛔0 读任何 key／.env；⛔0 输出凭据明文；⛔0 写既有件。
产出：§13 落笔所载之一切实测值（单一观测时点·避免 MATCH N 并发面之竞态）。
"""
import hashlib, io, os, re, datetime, json

REPO = r"_repo_mirror"
CUT = datetime.datetime(2026, 10, 19, 23, 56, 47).timestamp()
SKIP_TOP = ("deposon-sub", ".git", "node_modules", "__pycache__", ".venv", "venv")

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

def style(p):
    b = open(p, "rb").read()
    try:
        t = b.decode("utf-8")
        fffd = t.count("\ufffd")
    except Exception:
        fffd = -1
    return len(b), b.count(b"\x0d"), b[:3] == b"\xef\xbb\xbf", fffd, b.count(b"\x0a")

def main():
    obs = datetime.datetime.now()
    print("OBS_T=" + obs.strftime("%Y-%m-%d %H:%M:%S"))

    # ---- 全仓窗内枚举 ----
    win = []
    for root, dirs, files in os.walk(REPO):
        rel_root = os.path.relpath(root, REPO)
        parts = rel_root.split(os.sep)
        if parts and parts[0] in SKIP_TOP:
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if d not in SKIP_TOP]
        for fn in files:
            p = os.path.join(root, fn)
            try:
                st = os.stat(p)
            except Exception:
                continue
            if st.st_mtime < CUT:
                continue
            win.append((p, st.st_mtime, st.st_size))
    win.sort(key=lambda x: x[1])
    print("WINDOW_TOTAL=%d" % len(win))

    faces = {}
    for p, m, s in win:
        rel = os.path.relpath(p, REPO).replace(os.sep, "/")
        top = rel.split("/")[0]
        if top == "results" and rel.startswith("results/.tmp/"):
            key = "results/.tmp"
        elif top == ".tmp":
            key = ".tmp(仓根)"
        else:
            key = top
        faces.setdefault(key, []).append((p, m, s, rel))
    for k in sorted(faces):
        print("FACE %-14s = %d" % (k, len(faces[k])))

    # ---- 交付面（results/ pi_rulings/ letters/ docs/ tools/ 剔 .tmp）----
    deliv = []
    for k in ("results", "pi_rulings", "letters", "docs", "tools"):
        for p, m, s, rel in faces.get(k, []):
            if rel.startswith("results/.tmp/"):
                continue
            deliv.append((p, m, s, rel))
    deliv.sort(key=lambda x: x[1])
    print("DELIVERABLE_COUNT=%d" % len(deliv))

    print("\n=== DELIVERABLES (SHA-12 / bytes / CR / BOM / FFFD / LF) ===")
    for p, m, s, rel in deliv:
        h = sha12(p)
        n, cr, bom, fffd, lf = style(p)
        print("%s | %s | %d | CR=%d | BOM=%s | FFFD=%d | LF=%d | %s" % (
            datetime.datetime.fromtimestamp(m).strftime("%m-%d %H:%M:%S"), h, n, cr, bom, fffd, lf, rel))

    # ---- 重复哈希（同一性对账）----
    print("\n=== DUP HASH GROUPS (deliverables) ===")
    g = {}
    for p, m, s, rel in deliv:
        g.setdefault(sha12(p), []).append(rel)
    dup = 0
    for h, v in sorted(g.items()):
        if len(v) > 1:
            dup += 1
            print("  %s :: %d -> %s" % (h, len(v), "  ||  ".join(v)))
    print("DUP_GROUPS=%d" % dup)

    # ---- 交付面 key 形态自扫 ----
    print("\n=== KEY FORM SCAN (deliverables) ===")
    PATS = [r"\bsk-[A-Za-z0-9_\-]{8,}", r"\btp-[A-Za-z0-9_\-]{8,}", r"\bark-[A-Za-z0-9_\-]{8,}",
            r"\bsk-ant-[A-Za-z0-9_\-]{8,}", r"\bAPI_KEY\s*=\s*[^\s\"'`]{8,}",
            r"Authorization\s*:\s*Bearer\s+[A-Za-z0-9_\-\.]{8,}", r"\bgh[pousr]_[A-Za-z0-9]{16,}",
            r"\bAKIA[0-9A-Z]{12,}", r"\bxox[baprs]-[A-Za-z0-9\-]{10,}",
            r"-----BEGIN [A-Z ]*PRIVATE KEY-----"]
    scanned = 0
    hits = []
    for p, m, s, rel in deliv:
        raw = open(p, "rb").read()
        try:
            t = raw.decode("utf-8")
        except Exception:
            continue
        scanned += 1
        for pat in PATS:
            for mm in re.finditer(pat, t):
                hits.append((rel, pat[:20], mm.group(0)[:36]))
    print("SCANNED=%d NAIVE_HITS=%d" % (scanned, len(hits)))
    for h in hits:
        print("  HIT %s | %s | %s" % h)

    # ---- 锚组 B 更正复核（长名式·⛔0 单用 -Filter）----
    print("\n=== ANCHOR B CORRECTED (long-name probe) ===")
    B = [
        ("results/_mda8_preexp_run_reading_2026_10_20.json", "56EB9DB8BFD1", "v146-Q4"),
        ("results/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md", "EBE106D2DA47", "v145-Q1"),
        ("results/_kd_cluster_verdict_pack_adjudication_2026_10_19.md", "D87A711B0ECF", "v145-Q2"),
        ("results/_eta_construct_face_freeze_draft_2026_10_19.md", "AFDB26047B79", "v145-Q4"),
        ("results/_eta_construct_c1_c16_recommendation_2026_10_20.md", "56760F30332B", "v146-Q1"),
        ("pi_rulings/_pi_card_answers_register_2026_10_20_v147.md", "267A23F20526", "v147 令源"),
        ("results/_mda8_preexp_run_register_2026_10_20.md", "9061FB974B18", "v149-Q2"),
        ("letters/_commission_eta_candidate_values_2026_10_20.md", "E1526315C193", "v148-Q1"),
        ("results/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md", "522BE8905484", "v149-Q1/v151-Q3"),
        ("letters/_reply_eta_candidate_values_copilot_2026_10_20.md", "F4845FFFC44F", "v150-Q1"),
        ("results/_kd_mda8_first_reading_verdict_2026_10_20.md", "9C75B5C16676", "v153-Q4-①现值"),
        ("results/_kd_history_pack_adjudication_2026_10_19.md", "FCE088063DBD", "v151-Q1"),
        ("results/_v148_four_points_erratum_draft_2026_10_20.md", "524865BDC941", "v153-Q1"),
        ("results/_kd_h1_h7_disposition_draft_2026_10_20.md", "42EA79EA3F06", "v153-Q2"),
        ("results/_kd_eta_main_run_verdict_2026_10_20.md", "8A5727BC4C11", "v154-Q1"),
        ("results/_kd_h6_caliber_mapping_adjudication_2026_10_20.md", "9E853E0F259B", "v155-Q1"),
        ("results/_kd_h5_session_history_domain_caliber_2026_10_20.md", "8DB6F947BF98", "v155-Q3"),
        ("results/_root_session_history_memo_main_2026_10_14.md", "46C8C95A7A4F", "主版 15:06:58"),
        ("results/_root_session_history_memo_2026_10_14.md", "ABD08EC2150D", "本件基线"),
    ]
    ma = mm2 = 0
    for rel, reg, src in B:
        p = os.path.join(REPO, rel.replace("/", os.sep))
        if not os.path.exists(p):
            print("  %-70s %s %-16s ABSENT" % (rel, reg, src))
            continue
        s = sha12(p)
        ok = s == reg.upper()
        ma += 1 if ok else 0
        mm2 += 0 if ok else 1
        print("  %-70s %s -> %s  %s" % (rel, reg, s, "MATCH" if ok else "MISMATCH"))
    print("B_CORRECTED: MATCH=%d MISMATCH=%d" % (ma, mm2))

    # ---- 长名式探测：本件唯一性 ----
    print("\n=== LONG-NAME UNIQUENESS (this memo) ===")
    hits2 = []
    for root, dirs, files in os.walk(REPO):
        parts = os.path.relpath(root, REPO).split(os.sep)
        if parts and parts[0] in SKIP_TOP:
            dirs[:] = []
            continue
        dirs[:] = [d for d in dirs if d not in SKIP_TOP]
        for fn in files:
            if fn == "_root_session_history_memo_2026_10_14.md":
                hits2.append(os.path.join(root, fn))
    print("EXACT_LONGNAME=%d" % len(hits2))
    for h in hits2:
        print("  " + h)

    # ---- 仓根 .tmp 按归属棒分组 ----
    print("\n=== ROOT .tmp BY OWNER GROUP ===")
    def grp(n):
        for v in ("v145", "v146", "v147", "v148", "v149", "v150", "v151", "v152", "v153", "v154"):
            if n.startswith(v):
                return v + "落账棒"
        if n.startswith("_w_"): return "worker执行棒"
        if n.startswith("_vk_"): return "verdict-keeper棒"
        if n.startswith("_c514"): return "远端blob棒"
        if n.startswith("mda8") or n.startswith("readlaw"): return "MDA-8/读法棒"
        if n.startswith("eta_main"): return "eta主实验棒"
        if n.startswith("_xcheck") or n.startswith("_write_probe"): return "探针/杂件"
        return "其他"
    gg = {}
    for p, m, s, rel in faces.get(".tmp(仓根)", []):
        fn = rel.split("/")[-1]
        gg[grp(fn)] = gg.get(grp(fn), 0) + 1
    for k in sorted(gg, key=lambda x: -gg[x]):
        print("  %-20s :: %d" % (k, gg[k]))
    print("ROOT_TMP_TOTAL=%d" % len(faces.get(".tmp(仓根)", [])))

    # ---- 主版节标题结构面（仅结构·⛔0 读正文）----
    print("\n=== MAIN VERSION HEADINGS ONLY (structure面) ===")
    mp = os.path.join(REPO, "results", "_root_session_history_memo_main_2026_10_14.md")
    t = open(mp, "r", encoding="utf-8", errors="replace").read()
    hs = [l for l in t.split("\n") if re.match(r"^#{2,4}\s", l)]
    for h in hs[-8:]:
        print("  " + h)
    print("MAIN_HEADINGS_TOTAL=%d" % len(hs))

if __name__ == "__main__":
    main()
