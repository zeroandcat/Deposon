# R4 cleanup worker (worker, 2026-09-29) -- read-only structural extraction helper.
# R4 discipline: raw file text is NEVER printed. Two output modes, both key-safe:
#   paths : only path-like tokens (+ line numbers)
#   mask  : line text with every latin/digit run >=5 chars (outside path tokens) masked
import hashlib
import pathlib
import re
import sys

PATH = re.compile(
    r"[A-Za-z0-9_./\\\-㐀-鿿]*\.(?:md|json|py|log|txt|jsonl|yaml|yml|pdf|csv|docx|xlsx)"
)
KEYISH = re.compile(r"^(sk-|sk_|pk-|api_|key|token|or-v1|sess-)", re.I)
LATIN = re.compile(r"[A-Za-z0-9_\-]{5,}")


def decode(raw: bytes) -> str:
    for enc in ("utf-8-sig", "utf-8", "gb18030"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def sha12(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def mask_line(line: str) -> str:
    spans = []
    for m in PATH.finditer(line):
        base = m.group(0).replace("\\", "/").split("/")[-1]
        if KEYISH.match(base) or len(base) > 120:
            continue
        spans.append((m.start(), m.end()))
    out = []
    last = 0
    for m in LATIN.finditer(line):
        if any(s <= m.start() < e for s, e in spans):
            continue
        out.append(line[last:m.start()])
        out.append("#" * len(m.group(0)))
        last = m.end()
    out.append(line[last:])
    return "".join(out)


def main() -> None:
    mode = sys.argv[1]
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    target = pathlib.Path(sys.argv[2])
    pats = sys.argv[3].split("|") if len(sys.argv) > 3 and sys.argv[3] else ["."]
    raw = target.read_bytes()
    text = decode(raw)
    print(f"FILE={target.name} SHA12={sha12(target)} BYTES={len(raw)}")
    rx = re.compile("|".join(pats), re.I)
    for i, line in enumerate(text.splitlines(), 1):
        if not rx.search(line):
            continue
        if mode == "mask":
            print(f"L{i}: {mask_line(line)}")
            continue
        toks = []
        for t in PATH.findall(line):
            base = t.replace("\\", "/").split("/")[-1]
            if KEYISH.match(base) or len(base) > 120:
                continue
            if base and base not in toks:
                toks.append(base)
        print(f"L{i}: " + " ; ".join(toks))


if __name__ == "__main__":
    main()
