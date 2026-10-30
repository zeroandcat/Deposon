# -*- coding: utf-8 -*-
"""§12 夜链补录 · key 形态命中之结构判定（⛔ 0 输出任何凭据明文）
只报：行号 / 形态 / 长度 / 占位符类别 / 字符类签名 / 是否疑似真实凭据
"""
import os, io, re

ROOT = r"_repo_mirror"
OUT = os.path.join(ROOT, "results", ".tmp", "_audit_s12_keyclass_2026_10_19.txt")
_f = io.open(OUT, "w", encoding="utf-8", newline="\n")
def w(s=""):
    _f.write(s + "\n")

CASES = [
    ("results/_f3_payment_vector_third_party_recalc_2026_10_19.md", [378, 379]),
    ("results/_kd_cluster_verdict_pack_adjudication_2026_10_19.md", [734]),
    ("results/_v143_v144_adoption_effect_2026_10_19.md", [718, 853]),
]
rx = re.compile(r"\b(API_KEY|APIKEY|SECRET_KEY|ACCESS_KEY|TOKEN|PASSWORD)\s*=\s*(\S+)")
PLACEHOLDER_PAT = re.compile(r"^(<.*>|\{\{?.*\}?\}|\[\[.*\]\]|\*+|[xX]{3,}|\.{3,}|<REDACTED>|REDACTED|PLACEHOLDER|EXAMPLE|SAMPLE|YOUR_.*|DUMMY|NONE|NULL|xxx+)$")

for rel, lns in CASES:
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    lines = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
    w("### %s" % rel)
    for ln in lns:
        line = lines[ln - 1]
        found = rx.findall(line)
        if not found:
            w("  L%d | 未能以赋值形态解析（该行含 'API_KEY=' 字面但值形态非 <name>=<value> 之简单赋值）" % ln)
            i = line.find("API_KEY=")
            tail = line[i + 8: i + 8 + 60]
            masked = re.sub(r"[A-Za-z0-9]", "#", tail)
            w("      | 其后 60 字符之字符类掩码 = %s" % masked)
            w("      | 该行总长 = %d" % len(line))
            continue
        for name, val in found:
            cls = []
            if re.search(r"[a-z]", val): cls.append("lower")
            if re.search(r"[A-Z]", val): cls.append("UPPER")
            if re.search(r"[0-9]", val): cls.append("digit")
            if re.search(r"[^A-Za-z0-9]", val): cls.append("special")
            is_ph = bool(PLACEHOLDER_PAT.match(val))
            w("  L%d | 键名=%s | 值长度=%d | 字符类=%s | 占位符形态=%s | 疑似真实凭据=%s" % (
                ln, name, len(val), "+".join(cls) or "none", is_ph, (not is_ph and len(val) >= 12)))
    w("")

w("### 跨件字面重复性检验（同一值是否在多件多行出现）")
vals = {}
for rel, lns in CASES:
    p = os.path.join(ROOT, rel.replace("/", os.sep))
    lines = io.open(p, encoding="utf-8", errors="replace").read().split("\n")
    for ln in lns:
        for name, val in rx.findall(lines[ln - 1]):
            vals.setdefault(val, []).append("%s:L%d" % (rel.split("/")[-1][:42], ln))
for val, where in vals.items():
    w("  值长度=%d | 出现处数=%d | %s" % (len(val), len(where), "；".join(where)))
w("")
w("### 结论用事实")
w("  · 值之出现处数 > 1 且跨件逐字相同 ⇒ 系形态清单（举例用）之重复登记，非独立凭据之散落")
w("  · 每处值长度与占位符类别如上；⛔ 本输出 ⛔ 0 含任何凭据明文")
_f.close()
print("BYTES=%d" % os.path.getsize(OUT))
