import re

cn = open("letters/_v5_rj5_external_rederive_request_2026_09_28.md", encoding="utf-8").read()
en = open("letters/_v5_rj5_external_rederive_request_EN_2026_09_28.md", encoding="utf-8").read()


def get(t, key):
    return [b for b in re.findall(r"```[^\n]*\n(.*?)```", t, re.S) if key in b]


def skel(s):
    # strip CJK + fullwidth punctuation -> the "mathematical skeleton"
    return re.sub(r"[\u4e00-\u9fff\uff00-\uffef]", "", s)


cases = [
    ("r_K \u2261 K_lit", "DEFINITION-FACTOR READING FORMULA"),
    ("K* (sinh(2K*)", "\u00a72.1 NUMERIC BLOCK"),
    ("gap(L=8, h=0)", "\u00a72.2 PIN/RATIO BLOCK"),
    ("docs/Deposon_Requirements_v1.md", "\u00a72.7 ANCHOR COUNT BLOCK"),
]

for key, label in cases:
    bc, be = get(cn, key), get(en, key)
    print("=" * 72)
    print(label)
    if not bc or not be:
        print("  !! not found  CN=%d EN=%d" % (len(bc), len(be)))
        continue
    cl = bc[0].rstrip("\n").split("\n")
    el = be[0].rstrip("\n").split("\n")
    print("  CN lines=%d  EN lines=%d" % (len(cl), len(el)))
    for i in range(max(len(cl), len(el))):
        c = cl[i] if i < len(cl) else "<<MISSING>>"
        e = el[i] if i < len(el) else "<<MISSING>>"
        if c == e:
            print("  SAME             %s" % c)
        else:
            same_skel = "skeleton-MATCH" if skel(c) == skel(e) else "skeleton-DIFF"
            print("  DIFF [%s]" % same_skel)
            print("      CN: %s" % c)
            print("      EN: %s" % e)
