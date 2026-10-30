# R4 cleanup worker (worker, 2026-09-29) -- literal SHAPE histogram, R4-safe.
# For every `sk-` runnable: prints only (len, masked?, alnum/digit/symbol counts). No literals.
import pathlib
import re
import sys

RUN = re.compile(r"sk-[^\s`'\"]{0,120}")


def shape(s: str) -> str:
    body = s[3:]
    alnum = sum(c.isalnum() for c in body)
    dig = sum(c.isdigit() for c in body)
    star = body.count("*")
    up = sum(c.isupper() for c in body)
    lo = sum(c.islower() for c in body)
    sym = len(body) - alnum
    return f"len={len(s)} alnum={alnum} digit={dig} upper={up} lower={lo} star={star} sym={sym}"


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        text = p.read_bytes().decode("utf-8", errors="replace")
        hist: dict[str, int] = {}
        for m in RUN.finditer(text):
            s = shape(m.group(0))
            hist[s] = hist.get(s, 0) + 1
        print(f"== {p}")
        for k, v in sorted(hist.items()):
            print(f"   n={v}  {k}")


if __name__ == "__main__":
    main()
