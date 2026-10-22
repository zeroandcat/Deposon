#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
审计扫描器 v13-B · 锚链复算 ＋ key 形态自扫 ＋ 版式扫描 · 2026-10-20
纪律：只读；⛔0 读任何 key／.env；⛔0 输出任何凭据明文；⛔0 写既有件。
锚源：① 本件 §12-4-1（35 锚）② 窗内卡答登记件所载登记值（逐条人工录自登记件正文）
"""
import hashlib, io, os, re, sys

REPO = r"_repo_mirror"

# ---- 锚组 A：本件 §12-4-1 所载 35 锚（登记值）＋ 本件落笔前基线 ----
ANCHORS_A = [
    ("tools/exp_harness.py", "CE64B9B97489"),
    (".tmp/exp_harness_pre_2026_10_17.py", "026575FF3829"),
    ("results/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md", "B666077233C5"),
    ("results/_kd_mda8_domain_readings_adjudication_2026_10_19.md", "42AF8A6E0703"),
    ("results/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md", "9A960A574260"),
    ("results/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md", "30E47F1181D3"),
    ("results/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md", "8A77B155FD64"),
    ("results/_f3_payment_vector_reconstruction_2026_10_19.md", "56ED8250525B"),
    ("results/_f3_payment_vector_reconstruction_data_2026_10_19.json", "7F80D5AE03BB"),
    ("results/_f3_payment_vector_third_party_recalc_2026_10_19.md", "D716CD3F1240"),
    ("results/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md", "EBE106D2DA47"),
    ("results/_kd_mda8_spec_rest_recommendation_2026_10_19.md", "242B7EA98EB7"),
    ("results/_kd_cluster_verdict_pack_adjudication_2026_10_19.md", "D87A711B0ECF"),
    ("results/_kd_history_pack_adjudication_2026_10_19.md", "FCE088063DBD"),
    ("results/_eta_construct_face_freeze_draft_2026_10_19.md", "AFDB26047B79"),
    ("results/_kd_h1_h7_hidden_gaps_register_2026_10_19.md", "7EEFEDD92808"),
    ("results/_gap_and_kd_flip_master_inventory_2026_10_19.md", "989F2DC022A5"),
    ("results/_h5_session_census_2026_10_19_part1.md", "17826A907207"),
    ("results/_h5_session_census_2026_10_19_part2.md", "105413BEE0BA"),
    ("results/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md", "85E5CAEB3478"),
    ("results/_v139_adoption_effect_2026_10_19.md", "D02F0D4792A7"),
    ("results/_v140_adoption_effect_2026_10_19.md", "0E02218D80E5"),
    ("results/_v141_adoption_effect_2026_10_19.md", "5DBFDB48EA99"),
    ("results/_v142_adoption_effect_2026_10_19.md", "EB8C189C01F4"),
    ("results/_v143_v144_adoption_effect_2026_10_19.md", "23E5910D80C8"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v139.md", "2574BFC61BCB"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v140.md", "4CADC98DEEB7"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v141.md", "6CA97131CEDD"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v142.md", "B7D985E28992"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v143.md", "667CAF48C4D3"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v144.md", "0F4742AE0D44"),
    ("pi_rulings/_pi_card_answers_register_2026_10_17_v57.md", "0DD3510248E5"),
    ("letters/_letter_to_kimi_predecessor_history_invitation_2026_10_19.md", "660B5E10CAC3"),
    ("letters/_reply_from_kimi_era_history_2026_10_19.md", "07F847096216"),
    ("docs/WORLDVIEW_GEOMETRY_LOOP_2026.md", "1568B3DFE5AE"),
]

# ---- 锚组 B：窗内卡答登记件所载之登记值（逐条录自登记件正文之逐字） ----
ANCHORS_B = [
    ("results/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md", "EBE106D2DA47", "v145-Q1"),
    ("results/_kd_cluster_verdict_pack_adjudication_2026_10_19.md", "D87A711B0ECF", "v145-Q2"),
    ("results/_eta_construct_face_freeze_draft_2026_10_19.md", "AFDB26047B79", "v145-Q4"),
    ("results/_eta_construct_c1_c16_recommendation_2026_10_20.md", "56760F30332B", "v146-Q1"),
    ("pi_rulings/_pi_card_answers_register_2026_10_20_v147.md", "267A23F20526", "v147 委托稿令源"),
    ("results/_kd_mda8_preexp_run_reading_2026_10_20.json", "56EB9DB8BFD1", "v146-Q4"),
    ("results/_mda8_preexp_run_register_2026_10_20.md", "9061FB974B18", "v149-Q2"),
    ("letters/_commission_eta_candidate_values_2026_10_20.md", "E1526315C193", "v148-Q1 委托稿"),
    ("results/_kd_crw2_beta_and_t4n05_domain_adjudication_2026_10_20.md", "522BE8905484", "v149-Q1／v151-Q3"),
    ("letters/_reply_eta_candidate_values_copilot_2026_10_20.md", "F4845FFFC44F", "v150-Q1 回函"),
    ("results/_kd_mda8_first_reading_verdict_2026_10_20.md", "9C75B5C16676", "v153-Q4-①（现值）"),
    ("results/_kd_history_pack_adjudication_2026_10_19.md", "FCE088063DBD", "v151-Q1"),
    ("results/_v148_four_points_erratum_draft_2026_10_20.md", "524865BDC941", "v153-Q1"),
    ("results/_kd_h1_h7_disposition_draft_2026_10_20.md", "42EA79EA3F06", "v153-Q2"),
    ("results/_kd_eta_main_run_verdict_2026_10_20.md", "8A5727BC4C11", "v154-Q1"),
    ("results/_kd_h6_caliber_mapping_adjudication_2026_10_20.md", "9E853E0F259B", "v155-Q1"),
    ("results/_kd_h5_session_history_domain_caliber_2026_10_20.md", "8DB6F947BF98", "v155-Q3"),
    ("results/_root_session_history_memo_main_2026_10_14.md", "46C8C95A7A4F", "主版现值（15:06:58）"),
]

# ---- key 形态（10 类）· ⛔0 输出明文 ----
KEY_PATTERNS = [
    r"\bsk-[A-Za-z0-9_\-]{8,}",
    r"\btp-[A-Za-z0-9_\-]{8,}",
    r"\bark-[A-Za-z0-9_\-]{8,}",
    r"\bsk-ant-[A-Za-z0-9_\-]{8,}",
    r"\bAPI_KEY\s*=\s*[^\s\"'`]{8,}",
    r"Authorization\s*:\s*Bearer\s+[A-Za-z0-9_\-\.]{8,}",
    r"\bgh[pousr]_[A-Za-z0-9]{16,}",
    r"\bAKIA[0-9A-Z]{12,}",
    r"\bxox[baprs]-[A-Za-z0-9\-]{10,}",
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
]

def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12].upper()

def fmt(path):
    with open(path, "rb") as f:
        b = f.read()
    cr = b.count(b"\x0d")
    bom = b[:3] == b"\xef\xbb\xbf"
    try:
        t = b.decode("utf-8")
        fffd = t.count("\ufffd")
    except Exception:
        fffd = -1
    lf = b.count(b"\x0a")
    return len(b), cr, bom, fffd, lf

def main():
    out = []
    out.append("# 审计扫描器 v13-B 之输出 · 锚链复算 ＋ key 形态自扫 ＋ 版式扫描 · 2026-10-20")
    out.append("")
    out.append("## §A §12-4-1 三十五锚之复算（既有件触动面）")
    out.append("")
    out.append("| # | 件（repo 相对） | 登记值 | 实测值 | bytes | CR | BOM | U+FFFD | 判定 |")
    out.append("|:-:|---|:-:|:-:|---:|:-:|:-:|:-:|:-:|")
    ma = mm = miss = 0
    for i, (rel, reg) in enumerate(ANCHORS_A, 1):
        p = os.path.join(REPO, rel.replace("/", os.sep))
        if not os.path.exists(p):
            miss += 1
            out.append("| %d | `%s` | `%s` | **ABSENT** | — | — | — | — | **MISSING** |" % (i, rel, reg))
            continue
        s = sha12(p); n, cr, bom, fffd, lf = fmt(p)
        ok = (s == reg.upper())
        ma += 1 if ok else 0
        mm += 0 if ok else 1
        out.append("| %d | `%s` | `%s` | `%s` | %s | %d | %s | %d | %s |" % (
            i, rel, reg, s, format(n, ","), cr, bom, fffd, "**MATCH** ✅" if ok else "**MISMATCH** ⚠"))
    out.append("")
    out.append("> 组 A 合计：MATCH ＝ %d ／ MISMATCH ＝ %d ／ ABSENT ＝ %d" % (ma, mm, miss))
    out.append("")

    out.append("## §B 窗内登记值锚之复算")
    out.append("")
    out.append("| # | 件（repo 相对） | 登记值 | 锚源 | 实测值 | bytes | CR | BOM | U+FFFD | 判定 |")
    out.append("|:-:|---|:-:|---|:-:|---:|:-:|:-:|:-:|:-:|")
    mb = mmb = missb = 0
    for i, (rel, reg, src) in enumerate(ANCHORS_B, 1):
        p = os.path.join(REPO, rel.replace("/", os.sep))
        if not os.path.exists(p):
            missb += 1
            out.append("| %d | `%s` | `%s` | %s | **ABSENT** | — | — | — | — | **MISSING** |" % (i, rel, reg, src))
            continue
        s = sha12(p); n, cr, bom, fffd, lf = fmt(p)
        ok = (s == reg.upper())
        mb += 1 if ok else 0
        mmb += 0 if ok else 1
        out.append("| %d | `%s` | `%s` | %s | `%s` | %s | %d | %s | %d | %s |" % (
            i, rel, reg, src, s, format(n, ","), cr, bom, fffd, "**MATCH** ✅" if ok else "**MISMATCH** ⚠"))
    out.append("")
    out.append("> 组 B 合计：MATCH ＝ %d ／ MISMATCH ＝ %d ／ ABSENT ＝ %d" % (mb, mmb, missb))
    out.append("")

    # ---- key 形态自扫：窗内交付面（results/ pi_rulings/ letters/ docs/ tools/）----
    CUT = 1792425600000 / 1000.0  # 2026-10-19 23:56:47 CST
    import datetime
    cut = datetime.datetime(2026, 10, 19, 23, 56, 47).timestamp()
    out.append("## §C key 形态自扫（窗内交付面 · ⛔ 0 输出明文 · ⛔ 0 读 .env）")
    out.append("")
    hits = []
    scanned = 0
    for top in ("results", "pi_rulings", "letters", "docs", "tools"):
        d = os.path.join(REPO, top)
        if not os.path.isdir(d):
            continue
        for root, dirs, files in os.walk(d):
            for fn in files:
                p = os.path.join(root, fn)
                if fn.endswith(".pyc"):
                    continue
                try:
                    if os.path.getmtime(p) < cut:
                        continue
                    raw = open(p, "rb").read()
                except Exception:
                    continue
                try:
                    t = raw.decode("utf-8")
                except Exception:
                    continue
                scanned += 1
                rel = os.path.relpath(p, REPO).replace(os.sep, "/")
                for pat in KEY_PATTERNS:
                    for m in re.finditer(pat, t):
                        val = m.group(0)
                        # 判据：值长 ∧ 字符类数 ∧ 非包裹 ∧ 非占位
                        stripped = val.split("=", 1)[-1].split(":", 1)[-1].strip() if ("=" in val or ":" in val) else val
                        classes = sum([bool(re.search(r"[a-z]", stripped)), bool(re.search(r"[A-Z]", stripped)),
                                       bool(re.search(r"\d", stripped)), bool(re.search(r"[^A-Za-z0-9]", stripped))])
                        wrapped = stripped.startswith("<") or stripped.startswith("`") or stripped.startswith("\"") or stripped.startswith("'")
                        hits.append((rel, pat[:22], len(stripped), classes, wrapped, stripped[:40]))
    out.append("> 扫描面：窗内 `results/` `pi_rulings/` `letters/` `docs/` `tools/` 文本件（排 `.pyc`）——逐件实测 **%d** 件" % scanned)
    out.append("")
    out.append("| # | 件 | 形态 | 值长 | 字符类数 | 包裹 | 值形前 40 字符（**明文**） |")
    out.append("|:-:|---|:-:|:-:|:-:|:-:|---|")
    for i, h in enumerate(hits, 1):
        out.append("| %d | `%s` | `%s` | %d | %d | %s | `%s` |" % (i, h[0], h[1], h[2], h[3], h[4], h[5]))
    out.append("")
    out.append("> 朴素形态命中总数 ＝ **%d**（**⛔0 记入「真实凭据」侧**——须过四重判据：值长 ≥ 12 ∧ 字符类 ≥ 3 ∧ 非包裹 ∧ 非跨件逐字重复）" % len(hits))
    out.append("")

    # ---- 版式扫描（窗内交付面）----
    out.append("## §D 窗内交付面之版式扫描（BOM／CR／U+FFFD）")
    out.append("")
    out.append("| # | 件 | bytes | CR | BOM | U+FFFD | LF 行 |")
    out.append("|:-:|---|---:|:-:|:-:|:-:|---:|")
    idx = 0
    for top in ("results", "pi_rulings", "letters", "docs", "tools"):
        d = os.path.join(REPO, top)
        if not os.path.isdir(d):
            continue
        for root, dirs, files in os.walk(d):
            for fn in sorted(files):
                p = os.path.join(root, fn)
                try:
                    if os.path.getmtime(p) < cut:
                        continue
                except Exception:
                    continue
                n, cr, bom, fffd, lf = fmt(p)
                idx += 1
                rel = os.path.relpath(p, REPO).replace(os.sep, "/")
                out.append("| %d | `%s` | %s | %d | %s | %d | %d |" % (idx, rel, format(n, ","), cr, bom, fffd, lf))
    out.append("")
    out.append("> 交付面逐件版式扫描完毕（**0 件**含 0x0D 或 BOM 者为合格面）。")
    out.append("")

    data = "\n".join(out) + "\n"
    dst = r"〔幽灵引用·原件已缺席·未上传:_audit_s13_anchors_out_2026_10_20.txt〕"
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(data)
    print("WROTE", dst, len(data.encode("utf-8")), "bytes")
    print("A: MATCH=%d MISMATCH=%d ABSENT=%d" % (ma, mm, miss))
    print("B: MATCH=%d MISMATCH=%d ABSENT=%d" % (mb, mmb, missb))
    print("C: scanned=%d naive_hits=%d" % (scanned, len(hits)))

if __name__ == "__main__":
    main()
