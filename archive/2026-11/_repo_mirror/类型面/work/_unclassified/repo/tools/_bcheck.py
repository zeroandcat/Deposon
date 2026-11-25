import hashlib, sys
p = sys.argv[1]
raw = open(p, "rb").read()
t = raw.decode("utf-8", "replace")
h = hashlib.sha256(raw).hexdigest()
print("BYTES %d" % len(raw))
print("SHA12 %s" % h[:12])
print("SHA256 %s" % h)
print("BOM %d CR %d VT %d FFFD %d" % (
    1 if raw[:3] == b"\xef\xbb\xbf" else 0, raw.count(b"\r"), raw.count(b"\x0b"), t.count("\ufffd")))
print("LAST_BYTE 0x%02x NON_ASCII %d LF %d" % (
    raw[-1], sum(1 for b in raw if b > 127), raw.count(b"\n")))
