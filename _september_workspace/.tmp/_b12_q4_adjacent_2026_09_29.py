# b12 verify pack -- Q4 decisive near-miss / adjacency probe over the 52 exact-reproduction candidates.
#
# Closes two rigor gaps in the first pass:
#   (a) `Authorization: Bearer` and `API_KEY=` were classified by header presence alone,
#       without inspecting the ADJACENT VALUE. A literal key behind a header would be missed.
#   (b) tail lengths near the canonical thresholds were not individually inspected.
#
# R4 discipline: shape class + character length + sha256[:12] fingerprint ONLY.
# No matched value is printed, stored, or logged.
import collections
import hashlib
import json
import os
import pathlib
import re
import sys

ROOTS = [
    (r"D:\私人资料\deposon-sub", "deposon-sub"),
    (r"D:\私人资料\_non_upload_local_archive", "archive"),
]
B12_PAT = re.compile(
    rb'(sk-[A-Za-z0-9]{8,}|tp-[A-Za-z0-9]{8,}|ark-[A-Za-z0-9]{8,}'
    rb'|API_KEY\s*[=:]|Authorization:\s*Bearer)'
)
CANON_ANY = re.compile("|".join([
    r"sk-or-v1-[A-Za-z0-9]{16,}", r"sk-teamo-[A-Za-z0-9]{16,}", r"sk-ad9b[A-Za-z0-9]{16,}",
    r"sk-[A-Za-z0-9]{20,}", r"ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}", r"AKIA[A-Z0-9]{16}",
    r"AIza[A-Za-z0-9_-]{35}", r"ghp_[A-Za-z0-9]{36}", r"gho_[A-Za-z0-9]{36}",
    r"xoxb-[A-Za-z0-9-]{20,}", r"xoxp-[A-Za-z0-9-]{20,}",
]))
ENCODINGS = ["utf-8", "gb18030", "gbk", "utf-16-le", "utf-16-be", "big5"]
VAL = re.compile(rb'[^\s,;"\'\)\]\}]{0,80}')
HEX_OR_MASK = re.compile(rb'^(0x[0-9a-fA-F]+|\$\{?[A-Za-z_][A-Za-z0-9_]*\}?|%[A-Za-z_]+%|\$[A-Za-z_][A-Za-z0-9_]*|\{\{.*\}\}|<[^>]*>|\.\.\.|\*+)$', re.S)
UPPER_UNDERSCORE = re.compile(rb'^[A-Z][A-Z0-9_]*$')
ENVNAME = re.compile(rb'^[A-Za-z0-9_]*(?:API_KEY|APIKEY|_KEY|TOKEN|SECRET|CREDENTIAL)[A-Za-z0-9_]*$')


def shape(v: bytes):
    """Classify an adjacent value by shape. Returns (label, length)."""
    if v == b"":
        return ("value_absent", 0)
    if HEX_OR_MASK.match(v):
        return ("placeholder_or_expansion", len(v))
    if ENVNAME.match(v):
        return ("env_var_name", len(v))
    if v in (b"true", b"false", b"True", b"False", b"None", b"null"):
        return ("literal_sentinel", len(v))
    s = v.decode("ascii", "replace")
    if CANON_ANY.fullmatch(s):
        return ("PLAINTEXT_KEY_canonical", len(v))
    alnum = sum(c.isalnum() for c in s)
    if alnum == len(s) and len(s) >= 16:
        return ("long_alnum_literal_NOT_canonical", len(v))
    if UPPER_UNDERSCORE.match(v):
        return ("uppercase_constant_name", len(v))
    if alnum / max(len(s), 1) > 0.85 and len(s) >= 12:
        return ("mostly_alnum_short", len(v))
    return ("prose_or_mixed", len(v))


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    adj = collections.Counter()
    adj_rows = []
    tail_max = 0
    tail_top = []
    canon_text_hits = []
    n_files = 0
    for base, tag in ROOTS:
        for dp, dn, fn in os.walk(base):
            for f in fn:
                q = pathlib.Path(dp) / f
                try:
                    if q.stat().st_size > 2_000_000:
                        continue
                    b = q.read_bytes()
                except OSError:
                    continue
                hits = B12_PAT.findall(b)
                if not hits:
                    continue
                n_files += 1
                # (a) adjacent-value inspection
                for m in B12_PAT.finditer(b):
                    tok = m.group(0)
                    v = VAL.match(b, m.end())
                    val = v.group(0) if v else b""
                    lab, ln = shape(val)
                    adj[f"{tok.decode('ascii','replace')[:14]}->{lab}"] += 1
                    if lab in ("PLAINTEXT_KEY_canonical", "long_alnum_literal_NOT_canonical"):
                        adj_rows.append({"file": str(q), "shape": lab, "len": ln,
                                         "val_fp": hashlib.sha256(val).hexdigest()[:12].lower()})
                    # (b) tail length after prefix
                    tm = re.match(rb'(sk|tp|ark)-([A-Za-z0-9]+)', tok)
                    if tm:
                        t = len(tm.group(2))
                        tail_max = max(tail_max, t)
                        tail_top.append((t, str(q)[len(base) + 1:]))
                # (c) canonical scan in TEXT mode across 6 encodings
                for enc in ENCODINGS:
                    try:
                        text = b.decode(enc, errors="strict")
                    except (UnicodeDecodeError, LookupError):
                        continue
                    for cm in CANON_ANY.finditer(text):
                        canon_text_hits.append({"file": str(q), "enc": enc,
                                                "fp": hashlib.sha256(cm.group(0).encode()).hexdigest()[:12].lower()})
    print(f"candidate files re-visited = {n_files}")
    print(f"max tail length after sk-/tp-/ark- prefix = {tail_max}  (canonical thresholds: 16 / 20)")
    print("top-5 tails:", sorted(tail_top, reverse=True)[:5])
    print()
    print("ADJACENT-VALUE SHAPE TALLY (header/assignment -> value shape):")
    for k, v in adj.most_common():
        print(f"   {k:56s} {v}")
    print()
    print(f"adjacent values flagged long/canonical : {len(adj_rows)}")
    for r in adj_rows:
        print("   FLAG", r)
    print(f"CANONICAL KEY HITS (text mode, 6 encodings) over the 52 files: {len(canon_text_hits)}")
    for r in canon_text_hits:
        print("   CANON", r)
    pathlib.Path(r".tmp\_b12_q4_adjacent_probe_2026_09_29.json").write_text(
        json.dumps({"adj_tally": dict(adj), "flagged": adj_rows, "canon_text_hits": canon_text_hits,
                    "max_tail": tail_max}, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
