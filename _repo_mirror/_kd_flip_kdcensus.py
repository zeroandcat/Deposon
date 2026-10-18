# -*- coding: utf-8 -*-
"""KD-FLIP-CENSUS: word-boundary kd census over the whole repo.

Discipline (per census precedent 0b9512c6b68b):
 - NEVER bare `kd` substring. Only \bkd\b with explicit terminal-verdict context.
 - Separate in-register (results/, pi_rulings/, letters/, docs/, verifier/...) from .tmp/.
 - Report per-file hit counts + the matched line classes, so a human/verifier can re-read.
Read-only. No builtin hash().
"""
import os
import re
from collections import Counter

ROOT = r"D:\私人资料\deposon-repo"

# \bkd\b but only where kd is a TERMINAL-VERDICT word, not part of a KD-* id, not "kd_" keys.
TERM = [
    r"终判[^\n]{0,24}?`?kd`?",
    r"`kd`[^\n]{0,12}?(known defects|Known Defect)",
    r"落[ `\u3000]*`?kd`?",
    r"判[ `\u3000]*`?kd`?\b",
    r"更改为?[ `\u3000]*`?kd`?",
    r"归[ `\u3000]*`?kd`?",
    r"由[ `\u3000]*`?kd`?",
]
TERM_RE = re.compile("|".join(TERM), re.IGNORECASE)

# negative guard: a hit is EXCLUDED if the kd token on that line is part of a KD-#### id
# or is a _kd / kd_ identifier or a filepath token.
IDENT = re.compile(r"(KD-[A-Z0-9]|_kd\b|\bkd_|\bkd-|/kd_|results\\_kd|\.tmp\\\\kd)", re.IGNORECASE)


def classify(line):
    has_term = bool(TERM_RE.search(line))
    has_ident = bool(IDENT.search(line))
    if has_term and not has_ident:
        return "TERMINAL"
    if has_term and has_ident:
        return "TERMINAL+ID"
    return None


def main():
    per_file = Counter()
    classes = Counter()
    n_files = 0
    n_err = 0
    skipped_big = 0
    samples = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        for name in filenames:
            if not name.lower().endswith((".md", ".json", ".txt")):
                continue
            p = os.path.join(dirpath, name)
            try:
                if os.path.getsize(p) > (4 << 20):
                    skipped_big += 1
                    continue
                with open(p, "r", encoding="utf-8", errors="replace") as f:
                    lines = f.readlines()
            except Exception:
                n_err += 1
                continue
            n_files += 1
            rel = os.path.relpath(p, ROOT)
            is_tmp = rel.replace("\\", "/").startswith(".tmp/") or "\\.tmp\\" in p
            for i, line in enumerate(lines, 1):
                c = classify(line)
                if c:
                    per_file[(rel, is_tmp, c)] += 1
                    classes[c] += 1
                    if len(samples) < 400 and c == "TERMINAL":
                        samples.append((rel, i, line.strip()[:190]))

    print("SCANNED_FILES=%d ERR=%d SKIPPED_GT4MiB=%d" % (n_files, n_err, skipped_big))
    print("HIT_LINES=%d  TERMINAL=%d  TERMINAL+ID=%d"
          % (classes["TERMINAL"] + classes["TERMINAL+ID"], classes["TERMINAL"], classes["TERMINAL+ID"]))
    print("=" * 100)
    print("--- per-file TERMINAL hits (in-register only) ---")
    reg = [(k, v) for k, v in per_file.items() if k[1] is False and k[2] == "TERMINAL"]
    reg.sort(key=lambda x: -x[1])
    tot = 0
    for (rel, _, _), v in reg:
        print("%5d  %s" % (v, rel))
        tot += v
    print("IN_REGISTER_TERMINAL_TOTAL=%d across %d files" % (tot, len(reg)))
    print("=" * 100)
    tmpn = sum(v for k, v in per_file.items() if k[1] is True and k[2] == "TERMINAL")
    print("TMP_TERMINAL_TOTAL=%d" % tmpn)
    print("=" * 100)
    print("--- sample TERMINAL lines (first 60) ---")
    for rel, i, ln in samples[:60]:
        print("%s:%d | %s" % (rel, i, ln))


if __name__ == "__main__":
    main()
