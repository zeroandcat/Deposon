# b12 Q4 -- determine the exact form-token anchoring that reproduces b12's published
# candidate set (deposon-sub 5 files @ 10026/99702/17833/19548/11105 B; archive 47 files).
#
# Literal-substring tokens over-match (sk- hits task-/disk-/risk-; tp- hits http-).
# This probe tests anchored variants and reports ONLY file counts + the 5 known sizes.
# NO matched content is printed.
import hashlib
import os
import pathlib
import re
import sys

ROOTS = {
    "deposon-sub": pathlib.Path(r"D:\私人资料\deposon-sub"),
    "archive": pathlib.Path(r"D:\私人资料\_non_upload_local_archive"),
}
TARGET_SIZES = {10026, 99702, 17833, 19548, 11105}
MAX_SIZE = 2 * 1024 * 1024
SKIP = {"__pycache__", ".git"}

# Each variant: name -> list of (label, compiled regex)
VARIANTS = {
    "literal_substring": [
        ("sk-", re.compile(re.escape("sk-"))),
        ("tp-", re.compile(re.escape("tp-"))),
        ("ark-", re.compile(re.escape("ark-"))),
        ("API_KEY=", re.compile(re.escape("API_KEY="))),
        ("AuthBearer", re.compile(re.escape("Authorization: Bearer"))),
    ],
    "no_letter_left": [
        ("sk-", re.compile(r"(?<![A-Za-z])sk-")),
        ("tp-", re.compile(r"(?<![A-Za-z])tp-")),
        ("ark-", re.compile(r"(?<![A-Za-z])ark-")),
        ("API_KEY=", re.compile(r"API_KEY=")),
        ("AuthBearer", re.compile(r"Authorization: Bearer")),
    ],
    "wordstart_tail": [
        ("sk-", re.compile(r"\bsk-\w")),
        ("tp-", re.compile(r"\btp-\w")),
        ("ark-", re.compile(r"\bark-\w")),
        ("API_KEY=", re.compile(r"API_KEY=")),
        ("AuthBearer", re.compile(r"Authorization: Bearer")),
    ],
    "no_letter_left_tail": [
        ("sk-", re.compile(r"(?<![A-Za-z])sk-\w")),
        ("tp-", re.compile(r"(?<![A-Za-z])tp-\w")),
        ("ark-", re.compile(r"(?<![A-Za-z])ark-\w")),
        ("API_KEY=", re.compile(r"API_KEY=")),
        ("AuthBearer", re.compile(r"Authorization: Bearer")),
    ],
    "keyish_len": [
        ("sk-", re.compile(r"(?<![A-Za-z])sk-[A-Za-z0-9]{4,}")),
        ("tp-", re.compile(r"(?<![A-Za-z])tp-[A-Za-z0-9]{4,}")),
        ("ark-", re.compile(r"(?<![A-Za-z])ark-[A-Za-z0-9]{4,}")),
        ("API_KEY=", re.compile(r"API_KEY=")),
        ("AuthBearer", re.compile(r"Authorization: Bearer")),
    ],
}


def walk_files():
    for label, root in ROOTS.items():
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP]
            for fn in filenames:
                p = pathlib.Path(dirpath) / fn
                try:
                    size = p.stat().st_size
                    if size == 0 or size > MAX_SIZE:
                        continue
                    yield label, p, size, p.read_bytes()
                except OSError:
                    continue


def main():
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    # decode cache per (path, encoding) is unnecessary; we test each variant on decoded text
    decoded = []
    for label, p, size, raw in walk_files():
        for enc in ("utf-8", "gb18030", "gbk", "utf-16-le", "utf-16-be", "big5"):
            try:
                decoded.append((label, p, size, enc, raw.decode(enc, errors="strict")))
            except (UnicodeDecodeError, LookupError):
                continue

    for vname, pats in VARIANTS.items():
        files = set()
        sizes = set()
        sub_hits = set()
        arch_hits = set()
        total = 0
        for label, p, size, enc, text in decoded:
            n = 0
            for lbl, rx in pats:
                n += len(rx.findall(text))
            if n:
                files.add(str(p))
                total += n
                if label == "deposon-sub":
                    sub_hits.add(str(p))
                    sizes.add(size)
                else:
                    arch_hits.add(str(p))
        hit5 = TARGET_SIZES <= sizes
        print(f"VARIANT={vname:22s} files={len(files):4d} (sub={len(sub_hits):3d} arch={len(arch_hits):3d}) "
              f"hits={total:5d} sub_sizes_match_b12_5={hit5} n_sub_sizes={len(sizes)}")


if __name__ == "__main__":
    main()
