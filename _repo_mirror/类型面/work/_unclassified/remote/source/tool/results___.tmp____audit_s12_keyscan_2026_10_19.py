# -*- coding: utf-8 -*-
"""§12 夜链补录 · 锚链复算 + key 形态自扫（只读）
⛔ 0 写既有件 · 0 读 key/.env 本身 · 0 联网
⛔ key 形态命中一律只报「行号 + 形态 + 掩码形态」，⛔ 0 输出任何凭据明文
"""
import os, io, re, hashlib, time

ROOT = r"_repo_mirror"
OUT = os.path.join(ROOT, "results", ".tmp", "_audit_s12_keyscan_out_2026_10_19.txt")
_f = io.open(OUT, "w", encoding="utf-8", newline="\n")
def w(s=""):
    _f.write(s + "\n")

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

# ---------- 1. 锚链复算（登记值 ↔ 实测值） ----------
w("=" * 100)
w("[1] 锚链复算（MATCH / MISMATCH 逐件报）· 观测时点 %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
ANCHORS = [
    ("tools/exp_harness.py", "CE64B9B97489", "v141-Q3 码载重新锚定之新锚"),
    ("results/.tmp/exp_harness_pre_2026_10_17.py", "026575FF3829", "旧锚（v141 判为漂移·消解）"),
    ("results/_kd_mda8_arm2_kill_line_freeze_draft_2026_10_19.md", "B666077233C5", "MDA-8 肢二判死线冻结草案（v141-Q2 核锁生效）"),
    ("results/_kd_mda8_domain_readings_adjudication_2026_10_19.md", "42AF8A6E0703", "MDA-8 对象域三读判断件"),
    ("results/_kd_mda8_f1_two_senses_adjudication_2026_10_19.md", "9A960A574260", "字段① 一名两指效力辨判断件"),
    ("results/_kd_mda8_arm2_remaining11_recommendation_2026_10_19.md", "30E47F1181D3", "余 11 候裁位荐案"),
    ("results/_kd_mda8_preexp_dispatch_spec_draft_2026_10_19.md", "8A77B155FD64", "预实验派遣规格（v142-Q1 采认生效）"),
    ("results/_f3_payment_vector_reconstruction_2026_10_19.md", "56ED8250525B", "F3 补测/复算重建登记件"),
    ("results/_f3_payment_vector_reconstruction_data_2026_10_19.json", "7F80D5AE03BB", "F3 重建数据件"),
    ("results/_f3_payment_vector_third_party_recalc_2026_10_19.md", "D716CD3F1240", "F3 第三方独立复算登记件"),
    ("results/_kd_mda8_gate_resolution_and_new_exp_draft_2026_10_19.md", "EBE106D2DA47", "退化门清路＋新实验草案"),
    ("results/_kd_mda8_spec_rest_recommendation_2026_10_19.md", "242B7EA98EB7", "生效规格 §8 余项荐案"),
    ("results/_kd_cluster_verdict_pack_adjudication_2026_10_19.md", "D87A711B0ECF", "判定面族六面合并判断件"),
    ("results/_kd_history_pack_adjudication_2026_10_19.md", "FCE088063DBD", "史面与口径面族裁议件"),
    ("results/_eta_construct_face_freeze_draft_2026_10_19.md", "AFDB26047B79", "η 构造面冻结件草案"),
    ("results/_kd_h1_h7_hidden_gaps_register_2026_10_19.md", "7EEFEDD92808", "KD-H1…KD-H7 隐性缺口族登记件"),
    ("results/_gap_and_kd_flip_master_inventory_2026_10_19.md", "989F2DC022A5", "缺口与有望翻转 KD 全量清单"),
    ("results/_h5_session_census_2026_10_19_part1.md", "17826A907207", "H-5 会话普查 part1"),
    ("results/_h5_session_census_2026_10_19_part2.md", "105413BEE0BA", "H-5 会话普查 part2"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v139.md", "2574BFC61BCB", "卡答 v139"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v140.md", "4CADC98DEEB7", "卡答 v140"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v141.md", "6CA97131CEDD", "卡答 v141"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v142.md", "B7D985E28992", "卡答 v142"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v143.md", "667CAF48C4D3", "卡答 v143"),
    ("pi_rulings/_pi_card_answers_register_2026_10_19_v144.md", "0F4742AE0D44", "卡答 v144"),
    ("pi_rulings/_pi_card_answers_register_2026_10_17_v57.md", "0DD3510248E5", "v57 补登件"),
    ("letters/_letter_to_kimi_predecessor_history_invitation_2026_10_19.md", "660B5E10CAC3", "致 KIMI 前辈信"),
    ("letters/_reply_from_kimi_era_history_2026_10_19.md", "07F847096216", "KIMI 复函（口述史）"),
    ("docs/WORLDVIEW_GEOMETRY_LOOP_2026.md", "1568B3DFE5AE", "世界观-几何回路 立场声明"),
    ("results/_v139_adoption_effect_2026_10_19.md", "D02F0D4792A7", "v139 落账件"),
    ("results/_v140_adoption_effect_2026_10_19.md", "0E02218D80E5", "v140 落账件"),
    ("results/_v141_adoption_effect_2026_10_19.md", "5DBFDB48EA99", "v141 落账件"),
    ("results/_v142_adoption_effect_2026_10_19.md", "EB8C189C01F4", "v142 落账件"),
    ("results/_v143_v144_adoption_effect_2026_10_19.md", "23E5910D80C8", "v143+v144 落账件"),
    ("results/_kd_epw3_crw3_ffrep1_adjudication_2026_10_19.md", "85E5CAEB3478", "三面另议判断件"),
]
match_n = mismatch_n = absent_n = 0
for rel, reg, note in ANCHORS:
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    if not os.path.exists(p):
        w("  ABSENT   | %-70s | 登记 %s | %s" % (rel, reg, note)); absent_n += 1; continue
    act = sha12(p)
    st = "MATCH   " if act == reg else "MISMATCH"
    if act == reg: match_n += 1
    else: mismatch_n += 1
    w("  %s | %-70s | 登记 %s | 实测 %s | %s" % (st, rel, reg, act, note))
w("  => MATCH=%d  MISMATCH=%d  ABSENT=%d" % (match_n, mismatch_n, absent_n))

# ---------- 2. key 形态自扫（窗口内全部件） ----------
w("")
w("=" * 100)
w("[2] key 形态自扫（\\b 词边界）· 观测时点 %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
PATS = [
    ("sk-", re.compile(r"\bsk-[A-Za-z0-9_\-]{4,}")),
    ("tp-", re.compile(r"\btp-[A-Za-z0-9_\-]{4,}")),
    ("ark-", re.compile(r"\bark-[A-Za-z0-9_\-]{4,}")),
    ("API_KEY=", re.compile(r"\bAPI_KEY\s*=\s*\S+")),
    ("Authorization: Bearer", re.compile(r"Authorization\s*:\s*Bearer\s+\S+")),
    ("ghp_/gho_/ghs_", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{8,}")),
    ("AKIA", re.compile(r"\bAKIA[0-9A-Z]{8,}")),
    ("xoxb/xoxp", re.compile(r"\bxox[baprs]-[A-Za-z0-9\-]{8,}")),
    ("-----BEGIN * KEY", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("sk-ant-", re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{4,}")),
]
BREAK_MTIME = os.path.getmtime(os.path.join(ROOT, "results", "_root_session_history_memo_2026_10_14.md"))
SCAN_DIRS = ["results", "pi_rulings", "letters", "docs"]
total_hits = 0
for d in SCAN_DIRS:
    rp = os.path.join(ROOT, d)
    for dp, dn, fns in os.walk(rp):
        for fn in fns:
            p = os.path.join(dp, fn)
            if os.path.getmtime(p) <= BREAK_MTIME:
                continue
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel.endswith(".pyc"):
                continue
            try:
                txt = io.open(p, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for i, line in enumerate(txt.split("\n"), 1):
                for name, rx in PATS:
                    for mt in rx.finditer(line):
                        total_hits += 1
                        frag = mt.group(0)
                        masked = frag[:8] + ("…" if len(frag) > 8 else "") + "[len=%d]" % len(frag)
                        w("  HIT | %s | L%d | 形态=%s | 掩码=%s" % (rel, i, name, masked))
w("  => TOTAL_KEY_FORM_HITS=%d" % total_hits)

# ---------- 3. U+FFFD / 版式异常 ----------
w("")
w("=" * 100)
w("[3] 替换字符（U+FFFD）与版式异常（窗口内）")
for d in SCAN_DIRS:
    rp = os.path.join(ROOT, d)
    for dp, dn, fns in os.walk(rp):
        for fn in fns:
            p = os.path.join(dp, fn)
            if os.path.getmtime(p) <= BREAK_MTIME:
                continue
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel.endswith(".pyc"):
                continue
            b = open(p, "rb").read()
            try:
                b.decode("utf-8")
                valid = True
            except UnicodeDecodeError:
                valid = False
            txt = b.decode("utf-8", errors="replace")
            n = txt.count("\ufffd")
            if n or not valid or b"\r" in b or b[:3] == b"\xef\xbb\xbf":
                lines = txt.split("\n")
                pos = [i for i, l in enumerate(lines, 1) if "\ufffd" in l]
                w("  %s | %s | U+FFFD=%d | UTF8_valid=%s | CR=%d | BOM=%s | 行位=%s" % (
                    rel, sha12(p), n, valid, txt.count("\r"), b[:3] == b"\xef\xbb\xbf", pos[:8]))
_f.close()
print("OUT=%s" % OUT)
print("BYTES=%d" % os.path.getsize(OUT))
print("SHA12=%s" % sha12(OUT))
