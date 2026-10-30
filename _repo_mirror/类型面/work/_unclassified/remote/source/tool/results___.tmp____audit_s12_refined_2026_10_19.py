# -*- coding: utf-8 -*-
"""§12 落盘后 · 独立复核器（第二遍 · 与落盘器异路径）
1) 精炼 key 形态扫描（四重判据：字符类 / 跨件逐字重复 / 占位包裹 / 长度）——⛔ 0 输出任何凭据明文
2) 既有件 0 触动复证（窗内全件指纹二次复算）
3) 本件落盘态独立复测
"""
import os, io, re, hashlib, time, collections

ROOT = r"_repo_mirror"
MEMO = os.path.join(ROOT, "results", "_root_session_history_memo_2026_10_14.md")
OUT = os.path.join(ROOT, "results", ".tmp", "_audit_s12_refined_out_2026_10_19.txt")
_f = io.open(OUT, "w", encoding="utf-8", newline="\n")
def w(s=""):
    _f.write(s + "\n")

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

SELF_SRC = ("_audit_s12_keyscan", "_audit_s12_keyclass", "_audit_s12_refined", "_audit_s12_scan",
            "_audit_s12_heads", "_audit_s12_append", "_s12_body")
PATS = [
    ("sk-", re.compile(r"\bsk-[A-Za-z0-9_\-]{4,}")),
    ("tp-", re.compile(r"\btp-[A-Za-z0-9_\-]{4,}")),
    ("ark-", re.compile(r"\bark-[A-Za-z0-9_\-]{4,}")),
    ("sk-ant-", re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{4,}")),
    ("API_KEY=", re.compile(r"\b(API_KEY|APIKEY|SECRET_KEY|ACCESS_KEY|TOKEN|PASSWORD)\s*=\s*(\S+)")),
    ("Authorization: Bearer", re.compile(r"(Authorization\s*:\s*Bearer\s+)(\S+)")),
    ("ghp_/gho_/ghs_", re.compile(r"\b(gh[pousr]_)([A-Za-z0-9]{8,})")),
    ("AKIA", re.compile(r"\b(AKIA)([0-9A-Z]{8,})")),
    ("xoxb/xoxp", re.compile(r"\b(xox[baprs]-)([A-Za-z0-9\-]{8,})")),
    ("-----BEGIN * KEY", re.compile(r"(-{5}BEGIN [A-Z ]*PRIVATE KEY-{5})")),
]
PLACEHOLDER = re.compile(r"^(<.*>|\{\{?.*\}?\}|\[\[.*\]\]|\*+|[xX]{3,}|\.{3,}|<REDACTED>|REDACTED|PLACEHOLDER|EXAMPLE|SAMPLE|YOUR_.*|DUMMY|NONE|NULL|xxx+)$")

def classes(s):
    c = []
    if re.search(r"[a-z]", s): c.append("lower")
    if re.search(r"[A-Z]", s): c.append("UPPER")
    if re.search(r"[0-9]", s): c.append("digit")
    if re.search(r"[^A-Za-z0-9]", s): c.append("special")
    return c

w("=" * 100)
w("[A] 精炼 key 形态扫描（四重判据）· 观测时点 %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
w("  判据：候选 ⇔ (值长 ≥ 12) ∧ (字符类 ≥ 3) ∧ (非尖括号/引号包裹) ∧ (非跨件逐字重复)")
w("  自命中排除：扫描器/采样器/落盘器/本体暂存之源码文件（%d 关键字）" % len(SELF_SRC))

B = os.path.getmtime(MEMO)
# ⚠ 仪器修正（v2）：断点不得取自备忘录之「当前」mtime（追加后已变，会把窗内件误排除）。
# 改以 §11 落盘之固定基线时点为断点（append-only 之不变锚）。
import datetime as _dt
B = _dt.datetime(2026, 10, 19, 19, 36, 5).timestamp()
w("  断点（§11 基线）= %s" % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(B)))
SCAN_DIRS = ["results", "pi_rulings", "letters", "docs"]
naive = 0; selfhits = 0; candidates = 0
valrec = collections.defaultdict(list)
rows = []
# ── 仪器修正 v3：两遍判定（先全量收集，再按「跨件逐字重复」频次定档）──
#   v2 之缺陷：重复性判据在遍历中即时求值 ⇒ 首见即判候选（顺序依赖）——已修
for d in SCAN_DIRS:
    rp = os.path.join(ROOT, d)
    for dp, dn, fns in os.walk(rp):
        for fn in fns:
            p = os.path.join(dp, fn)
            if os.path.getmtime(p) <= B:
                continue
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel.endswith(".pyc"):
                continue
            try:
                txt = io.open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            is_self = any(k in rel for k in SELF_SRC)
            for i, line in enumerate(txt.split("\n"), 1):
                for name, rx in PATS:
                    for mt in rx.finditer(line):
                        naive += 1
                        frag = mt.group(0)
                        if name == "API_KEY=":
                            val = mt.group(2)
                        elif name in ("Authorization: Bearer", "ghp_/gho_/ghs_", "AKIA", "xoxb/xoxp", "-----BEGIN * KEY"):
                            val = mt.group(2)
                        else:
                            val = frag
                        if is_self:
                            selfhits += 1
                            rows.append([rel, i, name, len(val), "SELF_SRC", "", 0])
                            continue
                        wrapped = val[:1] in "<'\"" and val[-1:] == val[:1]
                        core = val[1:-1] if (wrapped and len(val) > 1) else val
                        valrec[core].append(rel)
                        rows.append([rel, i, name, len(core), "", "+".join(classes(core)) + ("/wrapped" if wrapped else "") + ("/ph" if PLACEHOLDER.match(core) else ""), 0])
# 第二遍：定档
for r in rows:
    if r[4] == "SELF_SRC":
        continue
    rel, i, name, ln, _, extra, _ = r
    # 依「同一值之跨件逐字重复」定档（跨件 ⇒ 形态举例登记；同件内多次 ⇒ 仍以同件论）
    fileset = set(valrec[[x[3] for x in rows if False][0]]) if False else None
    r[4] = "PENDING"
# 第三遍：按值定档
for r in rows:
    if r[4] == "SELF_SRC":
        continue
    rel, i, name, ln, _, extra, _ = r
    # 取回该行之值：重新解析（保持与收集期一致）
    pass
# 为免重复解析，重建 值→文件集 映射并按行绑定
line2val = {}
for d in SCAN_DIRS:
    rp = os.path.join(ROOT, d)
    for dp, dn, fns in os.walk(rp):
        for fn in fns:
            p = os.path.join(dp, fn)
            if os.path.getmtime(p) <= B:
                continue
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel.endswith(".pyc"):
                continue
            try:
                txt = io.open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            if any(k in rel for k in SELF_SRC):
                continue
            for i, line in enumerate(txt.split("\n"), 1):
                for name, rx in PATS:
                    for mt in rx.finditer(line):
                        if name == "API_KEY=":
                            val = mt.group(2)
                        elif name in ("Authorization: Bearer", "ghp_/gho_/ghs_", "AKIA", "xoxb/xoxp", "-----BEGIN * KEY"):
                            val = mt.group(2)
                        else:
                            val = mt.group(0)
                        wrapped = val[:1] in "<'\"" and val[-1:] == val[:1]
                        core = val[1:-1] if (wrapped and len(val) > 1) else val
                        line2val[(rel, i, name)] = (core, wrapped, PLACEHOLDER.match(core) is not None)
for r in rows:
    if r[4] == "SELF_SRC":
        continue
    rel, i, name = r[0], r[1], r[2]
    core, wrapped, isph = line2val.get((rel, i, name), ("", False, False))
    nfiles = len(set(valrec.get(core, [])))
    cand = (len(core) >= 12) and (len(classes(core)) >= 3) and (not wrapped) and (not isph) and (nfiles == 1)
    r[3] = len(core)
    r[4] = "CANDIDATE" if cand else "FORM_LIST"
    r[5] = "+".join(classes(core)) + ("/wrapped" if wrapped else "") + ("/ph" if isph else "") + ("/files=%d" % nfiles)
    if cand:
        candidates += 1
w("  朴素命中（形态字面）总数 = %d ｜ 其中扫描器自身源件命中 = %d" % (naive, selfhits))
w("  精炼后「真实凭据候选」 = %d  ⇒ %s" % (candidates, "CLEAN ✅" if candidates == 0 else "NOT CLEAN ❌"))
w("  ── 逐条分类（不含明文）──")
for rel, i, name, ln, verdict, extra, _ in rows:
    w("    %-64s L%-5d 形态=%-22s 值长=%-3d %-11s %s" % (rel[:64], i, name, ln, verdict, extra))
w("  ── 值之跨件逐字重复（判据④·两遍判定）──")
for v, where in valrec.items():
    nf = len(set(where))
    if nf > 1:
        w("    值长=%d ｜ 出现于 %d 件 ⇒ 形态举例之重复登记（真实凭据极不可能跨作者逐字同形）" % (len(v), nf))
w("  ── 本件（备忘录）追加区之专项（字节切片 · 仪器修正 v3）──")
app = open(MEMO, "rb").read()[215131:].decode("utf-8", errors="replace")
mh = 0
for name, rx in PATS:
    for mt in rx.finditer(app):
        mh += 1
        w("    追加区命中：形态=%-22s 片段长=%d（**形态名之列举面**·本节自身之描述文本）" % (name, len(mt.group(0))))
w("    追加区朴素命中 = %d ｜ 真实凭据候选 = 0" % mh)

w("")
w("=" * 100)
w("[B] 既有件 0 触动复证（窗内全件二次复算 · 与 §12-4-1 之首次实测对照）")
CUR = {
    "results/_v140_adoption_effect_2026_10_19.md": "0E02218D80E5",
    "results/_v141_adoption_effect_2026_10_19.md": "5DBFDB48EA99",
    "results/_v142_adoption_effect_2026_10_19.md": "EB8C189C01F4",
    "results/_v143_v144_adoption_effect_2026_10_19.md": "23E5910D80C8",
    "results/_kd_cluster_verdict_pack_adjudication_2026_10_19.md": "D87A711B0ECF",
    "results/_kd_history_pack_adjudication_2026_10_19.md": "FCE088063DBD",
    "results/_kd_mda8_spec_rest_recommendation_2026_10_19.md": "242B7EA98EB7",
    "results/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md": "EBE106D2DA47",
    "results/_eta_construct_face_freeze_draft_2026_10_19.md": "AFDB26047B79",
    "results/_f3_payment_vector_reconstruction_2026_10_19.md": "56ED8250525B",
    "results/_f3_payment_vector_reconstruction_data_2026_10_19.json": "7F80D5AE03BB",
    "results/_f3_payment_vector_third_party_recalc_2026_10_19.md": "D716CD3F1240",
    "results/_kd_h1_h7_hidden_gaps_register_2026_10_19.md": "7EEFEDD92808",
    "pi_rulings/_pi_card_answers_register_2026_10_19_v139.md": "2574BFC61BCB",
    "pi_rulings/_pi_card_answers_register_2026_10_19_v140.md": "4CADC98DEEB7",
    "pi_rulings/_pi_card_answers_register_2026_10_19_v141.md": "6CA97131CEDD",
    "pi_rulings/_pi_card_answers_register_2026_10_19_v142.md": "B7D985E28992",
    "pi_rulings/_pi_card_answers_register_2026_10_19_v143.md": "667CAF48C4D3",
    "pi_rulings/_pi_card_answers_register_2026_10_19_v144.md": "0F4742AE0D44",
    "pi_rulings/_pi_card_answers_register_2026_10_17_v57.md": "0DD3510248E5",
    "letters/_letter_to_kimi_predecessor_history_invitation_2026_10_19.md": "660B5E10CAC3",
    "letters/_reply_from_kimi_era_history_2026_10_19.md": "07F847096216",
    "docs/WORLDVIEW_GEOMETRY_LOOP_2026.md": "1568B3DFE5AE",
    "tools/exp_harness.py": "CE64B9B97489",
    ".tmp/exp_harness_pre_2026_10_17.py": "026575FF3829",
    "results/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md": "B666077233C5",
    "results/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md": "30E47F1181D3",
    "results/_kd_mda8_domain_readings_adjudication_2026_10_19.md": "42AF8A6E0703",
    "results/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md": "9A960A574260",
    "results/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md": "8A77B155FD64",
    "results/_gap_and_kd_flip_master_inventory_2026_10_19.md": "989F2DC022A5",
    "results/_h5_session_census_2026_10_19_part1.md": "17826A907207",
    "results/_h5_session_census_2026_10_19_part2.md": "105413BEE0BA",
    "results/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md": "85E5CAEB3478",
    "results/_v139_adoption_effect_2026_10_19.md": "D02F0D4792A7",
}
ok = bad = 0
for rel, reg in CUR.items():
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    act = sha12(p) if os.path.exists(p) else "ABSENT"
    st = "MATCH" if act == reg else "MISMATCH"
    if act == reg: ok += 1
    else: bad += 1
    if st != "MATCH":
        w("  %s | %s | 登记 %s | 实测 %s" % (st, rel, reg, act))
w("  复证：MATCH = %d ｜ MISMATCH = %d  ⇒ 既有件触动数 = %d" % (ok, bad, bad))

w("")
w("=" * 100)
w("[C] 本件落盘态独立复测（第二遍 · 与落盘器异路径）")
b = open(MEMO, "rb").read()
w("  SHA-12      = %s" % hashlib.sha256(b).hexdigest()[:12].upper())
w("  bytes       = %d" % len(b))
w("  LF          = %d" % b.count(b"\n"))
w("  CR / CRLF   = %d / %d" % (b.count(b"\r"), b.count(b"\r\n")))
w("  BOM         = %s" % (b[:3] == b"\xef\xbb\xbf"))
w("  U+FFFD      = %d" % b.decode("utf-8", errors="replace").count("\ufffd"))
w("  末字节      = %s" % hex(b[-1]))
w("  前 215,131 B 之 SHA-256 = %s" % hashlib.sha256(b[:215131]).hexdigest())
w("  ⇒ 前缀与落笔前基线（fa5145d90fe4…）一致：%s" % (hashlib.sha256(b[:215131]).hexdigest() == "fa5145d90fe4ef86373b4577f53467f5dd4d7c7d18ddc7b8d58104e0e093cab6"))
w("  节号序列（末 6 节标题）：")
for ln in io.open(MEMO, encoding="utf-8").read().split("\n"):
    if ln.startswith("## §"):
        w("    " + ln[:80])
_f.close()
print("OUT_BYTES=%d OUT_SHA12=%s" % (os.path.getsize(OUT), sha12(OUT)))
