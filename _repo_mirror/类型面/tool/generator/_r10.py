# -*- coding: utf-8 -*-
import hashlib
import pathlib
import re

o = []
for p in sorted(pathlib.Path("results").glob("_v4_pi_cot_v2_dataset_addendum_*")):
    if p.suffix.lower() != ".json":
        continue
    b = p.read_bytes()
    act = hashlib.sha256(b).hexdigest()[:12].upper()
    t = b.decode("utf-8-sig", errors="replace")
    m = re.search(r'fingerprint_self_hash_after_birth"\s*:\s*"([^"]*)"', t)
    sch = re.search(r'"schema"\s*:\s*"([^"]+)"', t)
    o.append("%-56s %6d B actual=%s self=%-12s drift=%-5s bom=%-5s schema=%s"
             % (p.name, len(b), act, m.group(1) if m else None,
                (m.group(1).upper() != act) if m else None,
                b[:3] == b"\xef\xbb\xbf", sch.group(1) if sch else None))

cr = pathlib.Path("results/_v4_pi_cot_v2_coding_review_2026_09_26.md")
if cr.exists():
    o.append("")
    o.append("coding review fingerprint/drift lines:")
    for i, ln in enumerate(cr.read_text(encoding="utf-8").splitlines(), 1):
        if re.search(r"fingerprint|七件|drift", ln, re.I):
            o.append("  L%d: %s" % (i, ln.strip()[:240]))

d3c = pathlib.Path("results/_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json")
if d3c.exists():
    o.append("")
    o.append("d3c self-description lines:")
    for i, ln in enumerate(d3c.read_text(encoding="utf-8-sig").splitlines(), 1):
        if re.search(r"七件|fingerprint", ln):
            o.append("  L%d: %s" % (i, ln.strip()[:240]))

pathlib.Path(".tmp/_r10.txt").write_text("\n".join(o), encoding="utf-8")
print("ok")
