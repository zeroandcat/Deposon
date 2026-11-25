#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Stage-2 append-only repair of tools/rag_index.py (2026-10-29).

Changes are deliberately implemented in this NEW file; the legacy tool and any
legacy index are not modified.

1. Recursively scan results/**/*.md and pi_rulings/*.md (the two memo books are
   therefore included), and require both memo paths to exist and be indexed.
2. Record the actual absolute source line of each heading.
3. Decode UTF-8 strictly. Read/decode failures are written to a separate JSON
   error manifest instead of being silently discarded.
4. Never overwrite an existing index or error manifest.

Usage:
    python -P tools/rag_index_stage2_fix_2026_10_29.py build
    python -P tools/rag_index_stage2_fix_2026_10_29.py q 接递之式 20
"""
import collections
import hashlib
import json
import os
import re
import sys

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


ROOT = r_dep_path("")
OUT = os.path.join(ROOT, "results", ".tmp", "_rag_index_stage2.jsonl")
ERR = os.path.join(ROOT, "results", ".tmp", "_rag_index_stage2_errors.json")
CHUNK_LINES = 40
HEAD_LEN = 160
TOP_KW = 24
REQUIRED = (
    "results/doc/document/_root_session_history_memo_main_2026_10_14.md",
    "results/work/process/_sub_agent_memo_2026_10_24_v4.md",
    "results/work/process/_experiment_tree_v2_main_2026_10_23.md",
)
CJK = re.compile(r"[\u4e00-\u9fff]")
LAT = re.compile(r"[A-Za-z][A-Za-z0-9_\-]{2,}")


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def kwbag(text):
    bag = collections.Counter()
    for word in LAT.findall(text):
        bag[word.lower()] += 1
    cjk = CJK.findall(text)
    for i in range(len(cjk) - 1):
        bag[cjk[i] + cjk[i + 1]] += 1
    return [word for word, _ in bag.most_common(TOP_KW)]


def targets():
    found = []
    for base in (os.path.join(ROOT, "results"), os.path.join(ROOT, "pi_rulings")):
        if not os.path.isdir(base):
            continue
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames.sort()
            for name in sorted(filenames):
                if name.lower().endswith(".md"):
                    found.append(os.path.join(dirpath, name))
    found = sorted(set(os.path.normcase(os.path.abspath(p)) for p in found))
    normalized = {os.path.normcase(os.path.abspath(os.path.join(ROOT, rel.replace("/", "\\")))) for rel in REQUIRED}
    missing = sorted(normalized - set(found))
    if missing:
        raise FileNotFoundError("Required memo files are absent from the index targets: " + repr(missing))
    return found


def build():
    if os.path.exists(OUT) or os.path.exists(ERR):
        raise FileExistsError("Refusing to overwrite an existing Stage-2 index or error manifest")
    files = targets()
    errors = []
    n_chunk = 0
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "x", encoding="utf-8", newline="\n") as writer:
        for path in files:
            rel = os.path.relpath(path, ROOT)
            try:
                raw = open(path, "rb").read()
                text = raw.decode("utf-8", errors="strict")
            except UnicodeDecodeError as exc:
                errors.append({"file": rel, "kind": "UTF8_DECODE", "start": exc.start, "reason": str(exc.reason)})
                continue
            except Exception as exc:
                errors.append({"file": rel, "kind": type(exc).__name__, "reason": str(exc)})
                continue
            lines = text.splitlines()
            fingerprint = sha12(path)
            heading = "(件首)"
            i = 0
            while i < len(lines):
                chunk = lines[i:i + CHUNK_LINES]
                for offset, line in enumerate(chunk):
                    if re.match(r"^#{1,4}\s", line):
                        absolute_line = i + offset + 1
                        heading = "L%d %s" % (absolute_line, line.strip()[:80])
                body = "\n".join(chunk)
                if body.strip():
                    rec = {
                        "file": rel,
                        "sha12": fingerprint,
                        "bytes": len(raw),
                        "start": i + 1,
                        "end": min(i + CHUNK_LINES, len(lines)),
                        "heading": heading,
                        "head": re.sub(r"\s+", " ", body.strip())[:HEAD_LEN],
                        "kws": kwbag(body),
                    }
                    writer.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n_chunk += 1
                i += CHUNK_LINES
    manifest = {
        "schema": "stage2-rag-errors-v1",
        "root": ROOT,
        "files_targeted": len(files),
        "chunks_written": n_chunk,
        "errors": errors,
        "required_memos": list(REQUIRED),
    }
    with open(ERR, "x", encoding="utf-8", newline="\n") as writer:
        writer.write(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print("files=%d chunks=%d errors=%d index=%s size=%d" % (
        len(files), n_chunk, len(errors), OUT, os.path.getsize(OUT)))
    print("error_manifest=%s" % ERR)


def query(term, topn=20):
    if not os.path.exists(OUT):
        print("索引不存在，先 build")
        return 2
    kws = kwbag(term)
    hits = []
    with open(OUT, encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            score = sum(1 for key in kws if key in rec["kws"])
            if term in rec["head"]:
                score += 3
            if term in rec["heading"]:
                score += 5
            if score:
                hits.append((score, rec))
    hits.sort(key=lambda item: -item[0])
    print("== 查询: %s ｜ 命中块 %d ｜ 显示前 %d ==" % (term, len(hits), min(topn, len(hits))))
    for score, rec in hits[:topn]:
        print("[%2d] %s L%d-%d ｜ %s" % (score, rec["file"], rec["start"], rec["end"], rec["heading"]))
        print("      %s" % rec["head"][:140])
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 0
    if argv[1] == "build":
        build()
        return 0
    if argv[1] == "q":
        if len(argv) < 3:
            print("q 需要查询词")
            return 2
        return query(argv[2], int(argv[3]) if len(argv) > 3 else 20)
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
