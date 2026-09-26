#!/usr/bin/env python3
"""R4 key plaintext scan: multi-encoding (UTF-8/GB18030/GBK/UTF-16LE/UTF-16BE/Big5).

Output: file path + encoding + key 4-char prefix + key SHA-12 (never echo key text).
Saves JSON to .tmp/_r4_key_scan_results_2026_09_24.json for downstream manifest.
"""
import os, sys, re, json, hashlib
from pathlib import Path

ROOTS = [
    r"D:\私人资料\deposon-repo",
    r"D:\私人资料\_non_upload_local_archive",
    r"D:\私人资料\deposon-sub",
]

# Key form prefixes (strict)
KEY_PATTERNS = [
    r"sk-or-v1-[A-Za-z0-9]{16,}",
    r"sk-teamo-[A-Za-z0-9]{16,}",
    r"sk-ad9b[A-Za-z0-9]{16,}",
    r"sk-[A-Za-z0-9]{20,}",          # generic OpenAI-style (must be >=20 to avoid sk_<short> false positives)
    r"ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}",  # volcengine ark
    r"AKIA[A-Z0-9]{16}",              # AWS
    r"AIza[A-Za-z0-9_-]{35}",         # Google
    r"ghp_[A-Za-z0-9]{36}",           # GitHub PAT
    r"gho_[A-Za-z0-9]{36}",           # GitHub OAuth
    r"xoxb-[A-Za-z0-9-]{20,}",        # Slack bot
    r"xoxp-[A-Za-z0-9-]{20,}",        # Slack user
]

# Encode fallbacks
ENCODINGS = ["utf-8", "gb18030", "gbk", "utf-16-le", "utf-16-be", "big5"]

# File size cap (skip >10MB to avoid hanging)
MAX_SIZE = 10 * 1024 * 1024

# Skip these directories (we still scan; mavis-trash already moves anything)
SKIP_DIRS = set()

def key_sha12(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:12].upper()

def scan_file(path: str) -> list:
    """Return list of (encoding, line_no, key_prefix4, key_sha12) hits."""
    results = []
    try:
        size = os.path.getsize(path)
        if size == 0 or size > MAX_SIZE:
            return results
        with open(path, "rb") as f:
            data = f.read()
    except (OSError, IOError):
        return results

    for enc in ENCODINGS:
        try:
            text = data.decode(enc, errors="strict")
        except (UnicodeDecodeError, LookupError):
            continue
        for pat in KEY_PATTERNS:
            for m in re.finditer(pat, text):
                key = m.group(0)
                # line number
                line_no = text.count("\n", 0, m.start()) + 1
                prefix4 = key[:4]
                ks = key_sha12(key)
                results.append((enc, line_no, prefix4, ks))
    return results

def walk():
    total = 0
    hits = []
    for root in ROOTS:
        for dirpath, dirnames, filenames in os.walk(root):
            # don't descend into heavy cache dirs but do scan results
            # we still walk; skip pycache for speed
            dirnames[:] = [d for d in dirnames if d != "__pycache__"]
            for fn in filenames:
                p = os.path.join(dirpath, fn)
                total += 1
                hs = scan_file(p)
                if hs:
                    hits.append({"path": p, "hits": hs})
                if total % 500 == 0:
                    print(f"[scan] {total} files processed...", file=sys.stderr)
    return total, hits

if __name__ == "__main__":
    total, hits = walk()
    out = {
        "total_files_scanned": total,
        "files_with_hits": len(hits),
        "hits": hits,
    }
    out_path = ".tmp/_r4_key_scan_results_2026_09_24.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"[scan] DONE. total={total}, files_with_hits={len(hits)}")
    print(f"[scan] out={out_path}")
    # Print summary table (no plaintext keys)
    print("---FILES WITH HITS---")
    for h in hits:
        p = h["path"]
        n = len(h["hits"])
        first = h["hits"][0]
        print(f"  {p}  enc={first[0]} line={first[1]} prefix4={first[2]} sha12={first[3]}  total_hits={n}")