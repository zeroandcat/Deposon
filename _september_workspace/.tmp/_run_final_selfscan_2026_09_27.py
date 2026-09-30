import hashlib
import os
import re

WS = r"D:\私人资料\deposon-repo"
TARGETS = [
    r"results\_v4_day_inventory_2026_09_27.md",
    r"results\_v4_day_inventory_measure_2026_09_27.py",
    r".tmp\_run_frozen_0touch_verify_2026_09_27.py",
    r".tmp\_run_day_inventory_table_2026_09_27.py",
]

STRICT = re.compile(
    r"\b(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|Bearer\s+[A-Za-z0-9]{20,}"
    r"|tp-[a-z0-9]{20,}|ark-[a-z0-9-]{20,})\b")
WIDE = re.compile(
    r"\b(api[_-]?key\s*[=:]\s*[\"'][^\"']{16,}"
    r"|Authorization\s*:\s*Bearer\s+\S{16,})\b", re.IGNORECASE)

print("%-9s %-12s %9s  %-5s %-5s %-5s %s" %
      ("SHA-12", "BOM", "bytes", "str", "wide", "esc", "path"))
for rel in TARGETS:
    p = os.path.join(WS, rel)
    b = open(p, "rb").read()
    h = hashlib.sha256(b).hexdigest()[:12]
    bom = "YES" if b[:3] == b"\xef\xbb\xbf" else "no"
    t = b.decode("utf-8")
    s = len(STRICT.findall(t))
    w = len(WIDE.findall(t))
    # invalid escape / lone surrogate style issues
    try:
        t.encode("utf-8").decode("utf-8")
        esc = 0
    except Exception:
        esc = 1
    print("%-12s %-9s %9d  %-5d %-5d %-5d %s" % (h, bom, len(b), s, w, esc, rel))

print("")
print("KEY SCAN VERDICT:", "CLEAN" if all(
    len(STRICT.findall(open(os.path.join(WS, r), "rb").read().decode("utf-8"))) == 0 for r in TARGETS)
    else "HIT")
