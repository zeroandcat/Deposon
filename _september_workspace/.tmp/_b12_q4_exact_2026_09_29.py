# b12 verify pack -- Q4 form-candidate: EXACT reproduction of the b12 criterion set, then
# per-hit PRECISE CRITERIA classification (code-reference vs plaintext key).
#
# b12 criterion (verbatim from its own scaffolding, %TEMP%/b12_verify.py L53):
#   PAT = rb'(sk-[A-Za-z0-9]{8,}|tp-[A-Za-z0-9]{8,}|ark-[A-Za-z0-9]{8,}|API_KEY\s*[=:]|Authorization:\s*Bearer)'
#   - bytes mode (NO decode step), size cap >2_000_000 skipped, NO dir skipping.
#
# R4 discipline: counts + SHA-12 fingerprints + category labels ONLY.
# Matched text never leaves memory except as a sha256[:12] fingerprint.
import collections
import hashlib
import json
import os
import pathlib
import re
import sys

# --- b12 verbatim pattern (bytes) ---
B12_PAT = re.compile(
    rb'(sk-[A-Za-z0-9]{8,}|tp-[A-Za-z0-9]{8,}|ark-[A-Za-z0-9]{8,}'
    rb'|API_KEY\s*[=:]|Authorization:\s*Bearer)'
)
B12_SIZE_CAP = 2_000_000

# --- canonical R4 11-pattern set (text mode) ---
KEY_PATTERNS = [
    r"sk-or-v1-[A-Za-z0-9]{16,}",
    r"sk-teamo-[A-Za-z0-9]{16,}",
    r"sk-ad9b[A-Za-z0-9]{16,}",
    r"sk-[A-Za-z0-9]{20,}",
    r"ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}",
    r"AKIA[A-Z0-9]{16}",
    r"AIza[A-Za-z0-9_-]{35}",
    r"ghp_[A-Za-z0-9]{36}",
    r"gho_[A-Za-z0-9]{36}",
    r"xoxb-[A-Za-z0-9-]{20,}",
    r"xoxp-[A-Za-z0-9-]{20,}",
]
CANON = re.compile("|".join(f"(?:{p})" for p in KEY_PATTERNS))
CANON_ANY = re.compile("|".join(KEY_PATTERNS))

ROOTS = [
    (pathlib.Path(r"D:\私人资料\deposon-sub"), "deposon-sub"),
    (pathlib.Path(r"D:\私人资料\_non_upload_local_archive"), "archive"),
]

# words that end in sk-/tp-/ark- (b12 pattern has NO left guard -> these are false positives)
WORD_SUFFIX = re.compile(rb'.*?(ta|dis|ri|ma|da|le|li|ne|we|sla|tra|whi|ch)sk-[A-Za-z0-9]{8,}')
TP_SUFFIX = re.compile(rb'.*?(ht|ft)s?tp-[A-Za-z0-9]{8,}')
ARK_SUFFIX = re.compile(rb'.*?(m|d)ark-[A-Za-z0-9]{8,}')
ALNUM_RUN = re.compile(rb'[A-Za-z0-9]+')
ENVNAME = re.compile(r'[A-Za-z0-9_]*(?:API_KEY|APIKEY|_KEY|TOKEN|SECRET|CREDENTIAL)[A-Za-z0-9_]*')


def classify(tok: bytes, whole: bytes):
    """Return (category, sublabel, run_len). Never returns the literal."""
    t = tok.decode("ascii", "replace")
    # 1. env-var / header forms -> always code reference
    if t.startswith("API_KEY") or t.startswith("Authorization"):
        return ("CODE_REFERENCE", "env_or_header_reference", len(tok))
    # 2. expand to the full alnum run for the true length test
    m = ALNUM_RUN.match(whole)
    run = m.group(0) if m else tok
    rtxt = run.decode("ascii", "replace")
    # 3. canonical key literal?
    if CANON_ANY.fullmatch(rtxt):
        return ("PLAINTEXT_KEY", "canonical_fullmatch", len(run))
    # 4. word-suffix false positive (task-/disk-/http-/mark- ...)
    if WORD_SUFFIX.fullmatch(run) or TP_SUFFIX.fullmatch(run) or ARK_SUFFIX.fullmatch(run):
        return ("FALSE_POSITIVE", "word_suffix_not_a_key", len(run))
    # 5. bearer value shape
    if "Bearer" in t:
        return ("CODE_REFERENCE", "bearer_header_present", len(tok))
    # 6. provider prefix constant in code (e.g. "sk-or-v1-" as a literal, no real tail)
    if rtxt in ("sk-or-v1", "sk-teamo", "sk-ad9b", "ark", "tp"):
        return ("CODE_REFERENCE", "provider_prefix_constant", len(run))
    # 7. env var name shape
    if ENVNAME.fullmatch(rtxt):
        return ("CODE_REFERENCE", "env_var_name", len(run))
    # 8. short-ish alnum tail, below every canonical threshold -> reference/placeholder
    tail = rtxt.split("-", 1)[1] if "-" in rtxt else rtxt
    if len(tail) < 20:
        return ("CODE_REFERENCE", "short_alnum_tail_below_key_threshold", len(run))
    # 9. long tail but not canonical -> suspicious, needs human read
    return ("SUSPECT_REVIEW", "long_noncanonical_alnum_tail", len(run))


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    tot_files = 0
    tot_hits = 0
    per_root = {}
    rows = []
    for base, tag in ROOTS:
        c = 0
        for dp, dn, fn in os.walk(base):          # NO dir skipping, exactly like b12
            for f in fn:
                q = os.path.join(dp, f)
                try:
                    if os.path.getsize(q) > B12_SIZE_CAP:
                        continue
                    b = open(q, "rb").read()
                except OSError:
                    continue
                tot_files += 1
                hits = B12_PAT.findall(b)
                if not hits:
                    continue
                c += 1
                tot_hits += len(hits)
                cats = collections.Counter()
                fps = set()
                lens = []
                for tok in hits:
                    # locate the full alnum run around this match for the true-length test
                    st = b.find(tok)
                    lo = st
                    while lo > 0 and (48 <= b[lo - 1] <= 57 or 65 <= b[lo - 1] <= 90 or 97 <= b[lo - 1] <= 122):
                        lo -= 1
                    hi = st + len(tok)
                    while hi < len(b) and (48 <= b[hi] <= 57 or 65 <= b[hi] <= 90 or 97 <= b[hi] <= 122):
                        hi += 1
                    whole = b[lo:hi]
                    cat, sub, ln = classify(tok, whole)
                    cats[f"{cat}/{sub}"] += 1
                    lens.append(ln)
                    fps.add(hashlib.sha256(tok).hexdigest()[:12].lower())
                rows.append({
                    "root": tag, "rel": str(q)[len(str(base)) + 1:],
                    "bytes": len(b), "sha12": hashlib.sha256(b).hexdigest()[:12].lower(),
                    "hits": len(hits), "categories": dict(cats),
                    "run_len_min": min(lens), "run_len_max": max(lens),
                    "tok_fp": sorted(fps),
                })
        per_root[tag] = c
    cat = collections.Counter()
    for r in rows:
        for k, v in r["categories"].items():
            cat[k] += v
    res = {
        "criterion": "b12 verbatim (bytes, {8,}, no left guard, 2_000_000 cap, no dir skip)",
        "total_files_scanned": tot_files, "per_root_candidates": per_root,
        "candidates": len(rows), "total_hits": tot_hits,
        "category_tally": dict(cat), "rows": rows,
    }
    dest = pathlib.Path(r".tmp\_b12_q4_exact_criteria_2026_09_29.json")
    dest.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"scanned={tot_files} per_root={per_root} candidates={len(rows)} total_hits={tot_hits}")
    print("CATEGORY TALLY:")
    for k, v in cat.most_common():
        print(f"   {k:60s} {v}")
    print()
    for r in rows:
        if r["root"] == "deposon-sub":
            print(f"  SUB {r['bytes']:>7} B {r['sha12']} hits={r['hits']:<3} "
                  f"run={r['run_len_min']}-{r['run_len_max']} {r['categories']} {r['rel']}")
    dest2 = pathlib.Path(r".tmp\_b12_q4_exact_criteria_2026_09_29.txt")
    with dest2.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(f"{r['root']}|{r['bytes']}|{r['sha12']}|hits={r['hits']}|"
                    f"run={r['run_len_min']}-{r['run_len_max']}|{r['categories']}|{r['rel']}\n")


if __name__ == "__main__":
    main()
