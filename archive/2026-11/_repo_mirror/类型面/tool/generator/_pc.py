import sys, hashlib, os
from pypdf import PdfReader
p = sys.argv[1]
b = open(p, 'rb').read()
r = PdfReader(p)
print("file      :", os.path.basename(p))
print("bytes     :", len(b))
print("sha256_12 :", hashlib.sha256(b).hexdigest()[:12])
print("pages     :", len(r.pages))
try:
    t = r.pages[0].extract_text() or ""
    print("p1_head   :", " | ".join(t.split("\n")[:6])[:300])
except Exception as e:
    print("p1_err    :", e)
