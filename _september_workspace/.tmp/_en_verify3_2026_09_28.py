import re, hashlib
p_en="letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md"
p_cn="letters/_v5_rj5_external_rederive_request_2026_09_28.md"
raw_en=open(p_en,"rb").read(); raw_cn=open(p_cn,"rb").read()
en=raw_en.decode("utf-8"); cn=raw_cn.decode("utf-8")
print("EN bytes=%d  CR count=%d  BOM=%s" % (len(raw_en), raw_en.count(b"\r"), raw_en[:3]==b"\xef\xbb\xbf"))
print("EN sha256_12 =", hashlib.sha256(raw_en).hexdigest()[:12])
print("CN sha256_12 =", hashlib.sha256(raw_cn).hexdigest()[:12], " bytes=%d (must be cfd58ae66463 / 31381)" % len(raw_cn))
print()
# code blocks of EN vs CN: every fenced block must be byte-identical except the added anti-downgrade template
def blocks(t): return re.findall(r"```[^\n]*\n(.*?)```", t, re.S)
bc, be = blocks(cn), blocks(en)
print("fenced blocks: CN=%d  EN=%d" % (len(bc), len(be)))
be_wo = [b for b in be if "Model actually used:" not in b]
print("EN blocks excluding the 1 new anti-downgrade template: %d" % len(be_wo))
# align by exact content
setc=set(bc); sete=set(be_wo)
print("CN blocks NOT byte-identical in EN:", len(setc-sete))
for b in sorted(setc-sete): print("   >>>", repr(b[:90]))
print("EN-only blocks (beyond the new template):", len(sete-setc))
for b in sorted(sete-setc): print("   >>>", repr(b[:90]))
print()
# markdown table rows: every numeric cell from CN must appear in EN
print("=== section heading parity ===")
hc=[l for l in cn.split("\n") if re.match(r"^#{1,3} ", l)]
he=[l for l in en.split("\n") if re.match(r"^#{1,3} ", l)]
print("CN headings=%d EN headings=%d" % (len(hc), len(he)))
for l in hc: print("  CN:", l)
print()
for l in he: print("  EN:", l)
