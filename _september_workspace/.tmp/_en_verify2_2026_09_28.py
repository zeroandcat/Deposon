import re
cn = open("letters/_v5_rj5_external_rederive_request_2026_09_28.md", encoding="utf-8").read()
en = open("letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md", encoding="utf-8").read()
def show(name, s):
    print(f"--- {name} ---")
    print("  CN:", s in cn, " EN:", s in en)
    print("  repr:", repr(s))
    for lbl, t in (("CN", cn), ("EN", en)):
        if s in t:
            i = t.index(s)
            print(f"  {lbl} ctx: ...{t[max(0,i-40):i+len(s)+10]!r}...")
show("critical eq (no spaces)", "sinh(2K)\u00b7sinh(2\u0393)=1")
show("definition reading line CN form (fullwidth ;)", "r_K \u2261 K_lit/(\u03b2\u00b7c_ferro)\uff1br_\u0393 \u2261 \u0393_lit/(\u03b2\u00b7c_trans)")
show("definition reading line EN form (ascii ;)", "r_K \u2261 K_lit/(\u03b2\u00b7c_ferro); r_\u0393 \u2261 \u0393_lit/(\u03b2\u00b7c_trans)")
show("S1 p3 quote", "For the Ising model in a transverse \ufb01eld without three spin interaction, the gaps collapse at the Bril- louin zone boundaries, k = \u00b1\u03c0 at the self-dual point \u03bb1 = 1 and \u03bb2 = 0.")
print("  CN has 'transverse \ufb01eld':", "transverse \ufb01eld" in cn, "| EN:", "transverse \ufb01eld" in en)
show("S2 eq5 quote", "The Hamiltonian of the 1D TFIM reads HI = \u2212 M\u2211 j=\u2212M [ \u03bb\u03c3x j \u03c3x j+1 + \u03c3z j ] , (5) where \u03c3\u03b1 j (\u03b1 = x, y, z) is a Pauli matrix at site j, \u03bb is the Ising coupling constant in units of the transverse \ufb01eld, and periodic boundary conditions ( \u03c3\u2212M = \u03c3M ) are as- sumed.")
show("S2 shorter", "is a Pauli matrix at site j,")
print()
print("--- CN line 118 raw ---")
for line in cn.split("\n"):
    if "c_ferro)" in line and "r_K" in line:
        print(repr(line))
print("--- EN equivalent line ---")
for line in en.split("\n"):
    if "c_ferro)" in line and "r_K" in line:
        print(repr(line))
