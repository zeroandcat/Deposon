# b12 verify pack -- Q4 form-candidate re-derivation + precise criteria classification (worker, 2026-09-29).
#
# R4 discipline: counts + SHA-12 fingerprints ONLY. Never prints / stores / logs any matched literal.
# Matched text is used in-memory only, to derive a CATEGORY LABEL and a sha256 fingerprint.
#
# Stage 1: re-derive the b12 form-candidate set (tokens: sk- / tp- / ark- / API_KEY= / Authorization: Bearer)
#          over the two out-of-repo read-only roots.
# Stage 2: per-hit precise criteria -> PLAINTEXT_KEY vs CODE_REFERENCE (with sub-labels).
#          PLAINTEXT_KEY requires a full canonical key literal (11-pattern set) OR a high-entropy
#          literal adjacent to an assignment. CODE_REFERENCE = env-var name / provider prefix constant.
import hashlib
import json
import pathlib
import re
import sys

ROOTS = [
    pathlib.Path(r"D:\私人资料\deposon-sub"),
    pathlib.Path(r"D:\私人资料\_non_upload_local_archive"),
]

MAX_SIZE = 2 * 1024 * 1024  # b12 stated "0 volume cap 2 MB"
SKIP_DIRS = {"__pycache__", ".git"}

# b12 form tokens (literal, count-only)
FORM_TOKENS = ["sk-", "tp-", "ark-", "API_KEY=", "Authorization: Bearer"]

# canonical R4 11-pattern set (from .tmp/_r4_key_scan_2026_09_24.py)
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
CANON = [re.compile(p) for p in KEY_PATTERNS]

# provider prefix constants (a hit that is EXACTLY one of these, or ends at a quote/paren)
PREFIX_CONSTS = {"sk-", "sk-or-v1-", "sk-teamo-", "sk-ad9b", "ark-", "tp-", "sk-or-v1", "tp"}

# env-var name shapes that are references, not values
ENVNAME = re.compile(r"[A-Za-z0-9_]*(?:API_KEY|APIKEY|_KEY|TOKEN|SECRET|CREDENTIAL)[A-Za-z0-9_]*")
BEARER = re.compile(r"Authorization\s*[:=]>?\s*Bearer\s+(\S+)")


def decode_strict(raw: bytes, enc: str):
    try:
        return raw.decode(enc, errors="strict")
    except (UnicodeDecodeError, LookupError):
        return None


def classify_tok(tok: str, ctx: str):
    """Return (category, sublabel, length_bucket). Never returns the literal."""
    for c in CANON:
        if c.fullmatch(tok) or c.match(tok):
            return ("PLAINTEXT_KEY", "canonical_pattern_fullmatch", len(tok))
    # Bearer header: inspect the token value shape only
    if tok.startswith("Bearer") or "Bearer" in ctx:
        m = BEARER.search(ctx)
        if m:
            val = m.group(1)
            if ENVNAME.fullmatch(val) or val.startswith("$") or val.startswith("{") or val.startswith("%"):
                return ("CODE_REFERENCE", "bearer_envvar_reference", len(val))
            if len(val) >= 20 and re.fullmatch(r"[A-Za-z0-9_\-\.]+", val):
                return ("PLAINTEXT_KEY", "bearer_literal_suspect", len(val))
            if re.fullmatch(r"[A-Za-z0-9_\-\.]*", val):
                return ("CODE_REFERENCE", "bearer_placeholder", len(val))
    if tok in PREFIX_CONSTS:
        return ("CODE_REFERENCE", "provider_prefix_constant", len(tok))
    if ENVNAME.fullmatch(tok):
        return ("CODE_REFERENCE", "env_var_name", len(tok))
    if tok.startswith(("$", "{", "%")) or tok.endswith("}"):
        return ("CODE_REFERENCE", "shell_expansion", len(tok))
    return ("CODE_REFERENCE", "prefix_like_short", len(tok))


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    out = []
    total_files = 0
    for root in ROOTS:
        for dirpath, dirnames, filenames in __import__("os").walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                p = pathlib.Path(dirpath) / fn
                total_files += 1
                try:
                    size = p.stat().st_size
                    if size == 0 or size > MAX_SIZE:
                        continue
                    raw = p.read_bytes()
                except OSError:
                    continue
                tok_counts = {}
                cats = {}
                fps = set()
                hit_total = 0
                for enc in ENCODINGS:
                    text = decode_strict(raw, enc)
                    if text is None:
                        continue
                    for t in FORM_TOKENS:
                        for m in re.finditer(re.escape(t), text):
                            hit_total += 1
                            tok_counts[t] = tok_counts.get(t, 0) + 1
                            # context window for Bearer/env classification (in-memory only)
                            lo = max(0, m.start() - 64)
                            hi = min(len(text), m.end() + 64)
                            ctx = text[lo:hi]
                            # candidate literal = the run of key-ish chars starting at the token
                            lit_m = re.match(r"[A-Za-z0-9_\-\.]*", text[m.start():m.start() + 120])
                            lit = lit_m.group(0) if lit_m else t
                            cat, sub, ln = classify_tok(lit, ctx)
                            cats[f"{cat}/{sub}"] = cats.get(f"{cat}/{sub}", 0) + 1
                            fps.add(hashlib.sha256(lit.encode("utf-8")).hexdigest()[:12].lower())
                if hit_total:
                    out.append({
                        "path": str(p),
                        "root": root.name,
                        "bytes": size,
                        "sha12": hashlib.sha256(raw).hexdigest()[:12].lower(),
                        "form_hits": hit_total,
                        "token_counts": tok_counts,
                        "categories": cats,
                        "distinct_token_fp": len(fps),
                        "token_fps": sorted(fps),
                    })
    res = {"total_files_scanned": total_files, "candidates": len(out), "rows": out}
    dest = pathlib.Path(r".tmp\_b12_q4_formcand_results_2026_09_29.json")
    dest.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"total_files={total_files} candidates={len(out)} out={dest}")
    for r in out:
        print(f"{r['root']}|{r['bytes']}|{r['sha12']}|hits={r['form_hits']}|{r['categories']}|{r['path']}")


if __name__ == "__main__":
    main()
