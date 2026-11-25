# R4 cleanup worker (worker, 2026-09-29) -- near-miss / redaction-shape probe, R4-safe.
# Purpose: distinguish "key literal absent" from "key literal redacted/masked" WITHOUT
# printing any literal. Emits counts only.
import pathlib
import re
import sys

NEARMISS = {
    "sk_dash_any": re.compile(r"sk-[^\s`'\"]{0,80}"),
    "sk_o_prefix": re.compile(r"sk-o"),
    "sk_t_prefix": re.compile(r"sk-t"),
    "sk_a_prefix": re.compile(r"sk-a"),
    "hex12_upper": re.compile(r"\b[0-9A-F]{12}\b"),
    "star_mask": re.compile(r"\*"),
}
ENC_FALLBACK = ["utf-8", "gb18030"]


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    for arg in sys.argv[1:]:
        p = pathlib.Path(arg)
        raw = p.read_bytes()
        best = None
        for enc in ENC_FALLBACK:
            text = raw.decode(enc, errors="replace")
            if best is None or text.count("�") < best[1]:
                best = (enc, text.count("�"), text)
        enc, bad, text = best
        counts = {k: len(rx.findall(text)) for k, rx in NEARMISS.items()}
        # distinct lengths of sk- runnables: redacted literals are usually short/masked
        lens = sorted({len(m.group(0)) for m in NEARMISS["sk_dash_any"].finditer(text)})
        print(f"{p} | enc={enc} | undecodable_chars={bad} | {counts} | sk_run_lengths={lens[:12]}")


if __name__ == "__main__":
    main()
