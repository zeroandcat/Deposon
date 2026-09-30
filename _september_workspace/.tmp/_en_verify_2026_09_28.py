import re, hashlib, collections
cn = open("letters/_v5_rj5_external_rederive_request_2026_09_28.md", encoding="utf-8").read()
en = open("letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md", encoding="utf-8").read()

def hex12(t): return set(re.findall(r"(?<![0-9a-fA-F])[0-9a-f]{12}(?![0-9a-fA-F])", t))
def decnums(t): return collections.Counter(re.findall(r"(?<![A-Za-z0-9_.\-])\d+(?:\.\d+)?(?:[eE][+-]?\d+)?(?![A-Za-z0-9_.])", t))

hc, he = hex12(cn), hex12(en)
print("=== 12-hex tokens (SHA-12 style) ===")
print("CN count:", len(hc), " EN count:", len(he))
print("in CN but NOT in EN:", sorted(hc - he))
print("in EN but NOT in CN (expected: only newly-measured EN self-report extras):", sorted(he - hc))

dc, de = decnums(cn), decnums(en)
print()
print("=== decimal-number tokens ===")
print("CN distinct:", len(dc), " EN distinct:", len(de))
missing = {k: v for k, v in dc.items() if k not in de}
print("numbers in CN absent from EN:", sorted(missing.items(), key=lambda x: -x[1]))
extra = {k: v for k, v in de.items() if k not in dc}
print("numbers in EN absent from CN (new, e.g. '5 working days'/'3' enumerations):")
print(sorted(extra.items(), key=lambda x: -x[1]))
print()
print("=== key formula strings verbatim check ===")
forms = [
 "sinh(2K\u2081) \u00b7 sinh(2K\u2082) = 1",
 "K\u2081* = -\u00bd ln(tanh K\u2082)",
 "sinh(2K\u00b7)\u00b7sinh(2\u0393)=1",
 "sinh(2K) \u00b7 sinh(2\u0393) = 1",
 "r_K \u2261 K_lit/(\u03b2\u00b7c_ferro); r_\u0393 \u2261 \u0393_lit/(\u03b2\u00b7c_trans)",
 "H_lit = -c_ferro\u00b7\u03a3_i S^z_i\u00b7S^z_{i+1} - c_trans\u00b7\u03a3_i S^x_i",
 "\u03b2 \u2261 1/(k_B\u00b7T)",
 "residual(\u03ba, \u03b3) = sinh(2\u03ba) \u00b7 sinh(2\u03b3) \u2212 1",
 "h_c/J = 2 \u00b7 t_rel \u00b7 asinh( 1 / sinh( 1/(2 \u00b7 t_rel) ) )",
 "PFEUTY_H_C_OVER_J = 1.0",
 "sinh(\u03b2J/2)\u00b7sinh(\u03b2h/2) = 1",
 "\u0393_c \u2248 e^{-\u03b2J/2} \u2192 0",
 "h_c/J = 2\u00b7t_rel\u00b7asinh(1/sinh(1/(2\u00b7t_rel)))",
 "K = c_K\u00b7\u03b2\u00b7J",
 "\u0393 = c_\u0393\u00b7\u03b2\u00b7h",
 "TFIM_CONVENTION = (\"H = -(J/4)",
 "residual(2.220446049250313e-16",
]
for f in forms:
    print(("  OK  " if (f in cn and f in en) else "  MISS"), repr(f[:60]), "| CN:", f in cn, "EN:", f in en)

print()
print("=== bibliography / DOI / URL verbatim check ===")
bib = ["10.1016/0003-4916(70)90270-8","10.1007/978-3-540-49865-0","arXiv:2207.09547v1","arXiv:0808.1816v1",
       "arXiv:cond-mat/0512369v2","arXiv:1910.12538v2","https://arxiv.org/pdf/2207.09547",
       "https://arxiv.org/pdf/0808.1816","https://arxiv.org/pdf/cond-mat/0512369","https://arxiv.org/pdf/1910.12538",
       "Ann. Phys. 57(1), 79\u201390.","pp. 17\u201349","ask_577b95bf8620614e98567bca",
       "Pfeuty, P. (1970)","Chakrabarti, B. K.; Dutta, A.; Sen, P. (1996)"]
for b in bib:
    print(("  OK  " if (b in cn and b in en) else "  MISS"), b)

print()
print("=== verbatim S1-S4 quoted passages (English quotes must be byte-identical) ===")
quotes = [
 "The Hamiltonian, H, is H =\u2212 \u2211 i (hi\u03c3x i +\u03bb2\u03c3x i\u03c3z i\u22121\u03c3z i+1 +\u03bb1\u03c3z i\u03c3z i\u22121) (1) written in terms of standard Pauli matrices. In this section we discuss its phase diagram. We shall set hi =h =cst.",
 "For the Ising model in a transverse \ufb01 eld without three spin interaction, the gaps collapse at the Bril- louin zone boundaries, k = \u00b1\u03c0 at the self-dual point \u03bb1 = 1 and \u03bb2 = 0.",
 "The Hamiltonian of the 1D TFIM reads HI = \u2212 M\u2211 j=\u2212M [ \u03bb\u03c3x j \u03c3x j+1 + \u03c3z j ] , (5) where \u03c3\u03b1 j (\u03b1 = x, y, z) is a Pauli matrix at site j, \u03bb is the Ising coupling constant in units of the transverse \ufb01 eld, and periodic boundary conditions ( \u03c3\u2212M = \u03c3M ) are as- sumed.",
 "\u2026As is well known, there is a critical point exactly at \u03bbc = 1 in the thermodynamic limit.",
 "eG(k) = \u22122 ( h + J cos k + \u221a h2 + 2J hcos k + J 2 ) . (10) Denote t = h |J| , (11) the excitation gap of \u02c6H is \u2206 E = 2|J||t \u2212 1|. (12) Thus the critical point of the ground-state CPT of the 1D TFIM is at t = tc = 1 where \u2206 E vanishes.",
 "The 1DTFIM can be exactly solved with the Jordan- Wigner transformation [11, 12],\u03c3z i =\u220f l<i (2c\u2020 lcl\u22121)(ci\u2212c\u2020 i) and \u03c3x i = 2c\u2020 ici\u2212 1, in which ci and c\u2020 i are fermion operators. The Hamiltonian is mapped to free fermions, H(g) =\u2212 \u2211 i (ci\u2212c\u2020 i)(c\u2020 i+1+ci+1)\u2212g \u2211 i (2c\u2020 ici\u2212 1). (10)",
 "The Hamiltonian H(g) is mapped into gH(1/g), thus the QCP at gc = 1 is self-dual.",
 "\u0393(T,g ) = \u2202Tvg(T,g ) \u2202T\u03f5(T,g ) . (1)",
 "Following the duality of the two dimensional Ising model on square lattice [2.1], one can show [2.2] the self-duality, and thereby make exact estimate of the critical tunnelling (transverse) field of the one-dimensional spin-1/2 transverse Ising model. Before\u2026",
]
for q in quotes:
    print(("  OK  " if (q in cn and q in en) else "  MISS"), (q[:70]+"...") if len(q)>70 else q, "| CN:", q in cn, "EN:", q in en)

print()
print("=== data table values verbatim ===")
vals = ["7.378176e+01","1.492331e+01","2.813658e+00","7.719368e-01","6.581609e-02","2.695220e-03","9.079986e-06","7.714999e-24",
        "0.4406867935","1.0000000000001301","1.0000000000002602","1.000000000000","0.5062","2.000000",
        "0.5266","0.5112","0.5108","0.5230","1.5","2.220446049250313e-16","4.440892098500626e-16",
        "0.05, 1.2","31,381","22,145","9,226","49,430","23,822","14,525","32,186","21,496","2,944","2,647","2,554","3,050","7,053","13,914","3,756","3,441","22,702","7,510"]
bad=[v for v in vals if not (v in cn and v in en)]
print("values missing from one side:", bad if bad else "NONE - all present in both")
print()
print("EN sha256_12 =", hashlib.sha256(open("letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md","rb").read()).hexdigest()[:12])
print("CN sha256_12 =", hashlib.sha256(open("letters/_v5_rj5_external_rederive_request_2026_09_28.md","rb").read()).hexdigest()[:12])
