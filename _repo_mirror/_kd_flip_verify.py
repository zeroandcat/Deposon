# -*- coding: utf-8 -*-
"""Post-write verify for _kd_flip_census_2026_10_17.md: read back from disk,
hash with hashlib (never builtin hash), byte-level self-report."""
import hashlib
import io
import os

P = r"_repo_mirror\results\_kd_flip_census_2026_10_17.md"

with io.open(P, "rb") as f:
    raw = f.read()

digest = hashlib.sha256(raw).hexdigest()
bom = raw[:3] == b"\xef\xbb\xbf"
cr = raw.count(b"\r")
lf = raw.count(b"\n")
tab = raw.count(b"\t")
fffd = raw.count("\ufffd".encode("utf-8"))
try:
    text = raw.decode("utf-8")
    dec = "UTF-8 OK"
except Exception as e:
    dec = "DECODE FAIL %s" % e

print("PATH        = %s" % P)
print("EXISTS      = %s" % os.path.exists(P))
print("SHA256      = %s" % digest)
print("SHA12       = %s" % digest[:12])
print("bytes       = %d" % len(raw))
print("BOM         = %s" % bom)
print("CR          = %d" % cr)
print("CRLF        = %d" % raw.count(b"\r\n"))
print("LF          = %d" % lf)
print("TAB         = %d" % tab)
print("U+FFFD      = %d" % fffd)
print("decode      = %s" % dec)
print("lines       = %d" % (text.count("\n") + 1))
print("-" * 70)
print("READBACK head:")
for line in text.split("\n")[:6]:
    print("  " + line[:150])
print("READBACK tail:")
for line in text.split("\n")[-6:]:
    print("  " + line[:150])
print("-" * 70)
# key-form scan (R4): word-boundary key shapes must be CLEAN
import re
KEYS = [
    r"\bsk-[A-Za-z0-9_\-]{8,}",
    r"\btp-[A-Za-z0-9_\-]{8,}",
    r"\bark-[A-Za-z0-9_\-]{8,}",
    r"\bAPI_KEY\s*=",
    r"\bAuthorization\s*:\s*Bearer",
    r"\bBearer\s+[A-Za-z0-9_\-\.]{12,}",
]
hits = 0
for pat in KEYS:
    for m in re.finditer(pat, text, re.IGNORECASE):
        hits += 1
        print("KEY_HIT %s -> %r" % (pat, m.group(0)[:40]))
print("KEY_SCAN    = %s (%d hit(s))" % ("CLEAN" if hits == 0 else "NOT_CLEAN", hits))
