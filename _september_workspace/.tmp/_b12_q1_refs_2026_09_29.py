# b12 verify pack -- Q1 anchor-root reference census (worker, 2026-09-29).
#
# Task: build a PER-FILE reference list for the anchor file
#   results/_v3_v4_achievements_inventory_3dir_2026_09_24.md
# over the four named workspace trees (letters/ results/ docs/ .tmp/), and reconcile
# the measured count against the published "38".
#
# R4-safe: this searches for a FILE NAME, not a key. Matched lines are NOT echoed; only
# line numbers + a coarse "reference form" label + co-located SHA-12 presence are emitted.
import datetime
import hashlib
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:\私人资料\deposon-repo")
TREES = ["letters", "results", "docs", ".tmp"]
TARGET_NAME = "_v3_v4_achievements_inventory_3dir_2026_09_24.md"
TARGET_REL = "results/_v3_v4_achievements_inventory_3dir_2026_09_24.md"
SKIP = {"__pycache__", ".git"}

ENCODINGS = ["utf-8", "gb18030", "gbk"]
SHA12 = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{12}(?![0-9a-fA-F])")


def classify_form(text, idx):
    """Coarse reference-form label from the text immediately BEFORE the match. No content echoed."""
    pre = text[max(0, idx - 80):idx]
    if re.search(r"results[/\\]$", pre):
        return "rel_path_results"
    if re.search(r"deposon-sub[/\\].*results[/\\]$", pre):
        return "rel_path_deposon_sub"
    if re.search(r"[/\\]$", pre):
        return "abs_or_rel_dir_prefixed"
    if re.search(r"[`'\"]$", pre):
        return "quoted_bare_name"
    if re.search(r"[\s(（\[【>#|]$", pre):
        return "bare_name_in_prose"
    return "bare_name_other"


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    rows = []
    scanned = 0
    skipped_binary = 0
    for t in TREES:
        base = ROOT / t
        if not base.is_dir():
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in SKIP]
            for fn in filenames:
                p = pathlib.Path(dirpath) / fn
                scanned += 1
                try:
                    if p.stat().st_size == 0 or p.stat().st_size > 4 * 1024 * 1024:
                        continue
                    raw = p.read_bytes()
                except OSError:
                    continue
                rel = p.relative_to(ROOT).as_posix()
                if rel == TARGET_REL:
                    continue  # the anchor file itself is not a referencing file
                text = None
                for enc in ENCODINGS:
                    try:
                        text = raw.decode(enc, errors="strict")
                        break
                    except (UnicodeDecodeError, LookupError):
                        continue
                if text is None:
                    skipped_binary += 1
                    continue
                if TARGET_NAME not in text:
                    continue
                lines = text.split("\n")
                forms = {}
                linenos = []
                sha_flag = 0
                for i, ln in enumerate(lines, 1):
                    start = 0
                    while True:
                        idx = ln.find(TARGET_NAME, start)
                        if idx < 0:
                            break
                        linenos.append(i)
                        f = classify_form(ln, idx)
                        forms[f] = forms.get(f, 0) + 1
                        if SHA12.search(ln):
                            sha_flag += 1
                        start = idx + len(TARGET_NAME)
                mt = datetime.datetime.fromtimestamp(p.stat().st_mtime)
                rows.append({
                    "rel": rel,
                    "tree": t,
                    "bytes": len(raw),
                    "sha12": hashlib.sha256(raw).hexdigest()[:12].lower(),
                    "mtime": mt.strftime("%Y-%m-%d %H:%M:%S"),
                    "hit_count": len(linenos),
                    "lines": sorted(set(linenos)),
                    "forms": forms,
                    "lines_with_sha12": sha_flag,
                })
    rows.sort(key=lambda r: (r["tree"], r["rel"]))
    res = {"trees": TREES, "files_scanned": scanned, "binary_skipped": skipped_binary,
           "referencing_files": len(rows), "rows": rows}
    dest = pathlib.Path(r".tmp\_b12_q1_refs_results_2026_09_29.json")
    dest.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"scanned={scanned} binary_skipped={skipped_binary} referencing_files={len(rows)}")
    from collections import Counter
    print("by_tree:", dict(Counter(r["tree"] for r in rows)))
    for r in rows:
        print(f"{r['tree']:8s}|{r['sha12']}|h={r['hit_count']:2d}|sha_lines={r['lines_with_sha12']:2d}|"
              f"mtime={r['mtime']}|lines={r['lines']}|{r['forms']}|{r['rel']}")


if __name__ == "__main__":
    main()
