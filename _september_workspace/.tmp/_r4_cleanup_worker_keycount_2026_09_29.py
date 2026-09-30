# R4 cleanup worker (worker, 2026-09-29) -- key PRESENCE scanner (targeted, R4-safe).
# Reuses the canonical R4 pattern set + encoding set from .tmp/_r4_key_scan_2026_09_24.py.
# Emits counts + SHA-12 fingerprints ONLY. Never prints/stores/logs any matched literal.
import hashlib
import pathlib
import re
import sys

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
ENCODINGS = ["utf-8", "gb18030", "gbk", "utf-16-le", "utf-16-be", "big5"]


def decode_strict(raw: bytes, enc: str):
    try:
        return raw.decode(enc, errors="strict")
    except (UnicodeDecodeError, LookupError):
        return None


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        if not p.is_file():
            print(f"MISSING {arg}")
            continue
        raw = p.read_bytes()
        found = []
        for enc in ENCODINGS:
            text = decode_strict(raw, enc)
            if text is None:
                continue
            for pat in KEY_PATTERNS:
                for m in re.finditer(pat, text):
                    found.append((enc, m.group(0), text.count("\n", 0, m.start()) + 1))
        fps = sorted(
            {hashlib.sha256(k.encode("utf-8")).hexdigest()[:12].upper() for _, k, _ in found}
        )
        locs = sorted({ln for _, _, ln in found})
        print(
            f"{p} | {len(raw)}B | SHA12={hashlib.sha256(raw).hexdigest()[:12]} "
            f"| hits={len(found)} | distinct_fp={len(fps)} | lines={locs} | fp={fps}"
        )


if __name__ == "__main__":
    main()
