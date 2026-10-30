#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Append-only repair of tools/rag_map.py (2026-10-29).

The original mapper recognizes only ##/### headings and silently ignores decode
failures. This NEW mapper accepts #{1,3}, records source lines, uses strict
UTF-8, writes errors separately, and never overwrites existing artifacts.
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
OUT = os.path.join(ROOT, "results", ".tmp", "_rag_map_stage2.jsonl")
REP = os.path.join(ROOT, "results", ".tmp", "_rag_map_stage2_report.md")
ERR = os.path.join(ROOT, "results", ".tmp", "_rag_map_stage2_errors.json")
BOOKS = [
    ("TREE", "results/work/process/_experiment_tree_v2_main_2026_10_23.md"),
    ("MAIN", "results/doc/document/_root_session_history_memo_main_2026_10_14.md"),
    ("SUB", "results/work/process/_sub_agent_memo_2026_10_24_v4.md"),
]
RE_FN = re.compile(r"[A-Za-z0-9_\-]{3,}?_\d{4}_\d{2}_\d{2}\.(?:md|json|py|txt|csv|tsv)")
RE_FP = re.compile(r"`([0-9a-f]{12})`")
RE_RUL = re.compile(r"\bv(\d{2,3})\b")
RE_SEC = re.compile(r"§(\d{2}-\d{2}(?:-[a-z0-9]+)?)")
RE_POS = re.compile(r"\b(KD-[A-Za-z0-9\-]{1,18}|R-\d{1,2}|T-[1-5]|F-\d{2}|E-\d{2}|N-\d|P-\d|U-\d{1,2}|D-\d{1,2}|项\s?\d{1,2})\b")
RE_HEAD = re.compile(r"^(#{1,3})\s+§?(\S{1,24})")


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def sections(text):
    lines = text.split("\n")
    marks = [(i, ln.strip()) for i, ln in enumerate(lines) if RE_HEAD.match(ln)]
    out = []
    for k, (i, heading) in enumerate(marks):
        j = marks[k + 1][0] if k + 1 < len(marks) else len(lines)
        out.append((heading, "\n".join(lines[i:j]), i + 1))
    return out


def anchors(text):
    found = collections.Counter()
    for m in RE_FN.findall(text):
        found["FN:" + m] += 3
    for m in RE_FP.findall(text):
        found["FP:" + m] += 3
    for m in RE_RUL.findall(text):
        found["RU:v" + m] += 2
    for m in RE_SEC.findall(text):
        found["SE:" + m] += 1
    for m in RE_POS.findall(text):
        found["PO:" + m.replace(" ", "")] += 1
    return found


def build():
    if os.path.exists(OUT) or os.path.exists(REP) or os.path.exists(ERR):
        raise FileExistsError("Refusing to overwrite Stage-2 rag-map artifacts")
    records = []
    errors = []
    for tag, rel in BOOKS:
        path = os.path.join(ROOT, rel.replace("/", "\\"))
        try:
            raw = open(path, "rb").read()
            text = raw.decode("utf-8", errors="strict")
        except UnicodeDecodeError as exc:
            errors.append({"book": tag, "file": rel, "kind": "UTF8_DECODE", "start": exc.start, "reason": exc.reason})
            continue
        except Exception as exc:
            errors.append({"book": tag, "file": rel, "kind": type(exc).__name__, "reason": str(exc)})
            continue
        fingerprint = sha12(path)
        for heading, body, source_line in sections(text):
            records.append({
                "book": tag,
                "file": rel,
                "sha12": fingerprint,
                "bytes": len(raw),
                "heading": heading[:120],
                "source_line": source_line,
                "chars": len(body),
                "anchors": dict(anchors(body)),
            })
        print("BOOK %-4s %-8d 节 %s" % (tag, len(raw), len(sections(text))))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "x", encoding="utf-8", newline="\n") as writer:
        for rec in records:
            writer.write(json.dumps(rec, ensure_ascii=False) + "\n")
    with open(ERR, "x", encoding="utf-8", newline="\n") as writer:
        writer.write(json.dumps({"schema": "stage2-rag-map-errors-v1", "records": len(records), "errors": errors}, ensure_ascii=False, indent=2) + "\n")
    print("WROTE", OUT, len(records), "节之记录; errors=%d" % len(errors))
    return records


def load():
    if not os.path.exists(OUT):
        print("NO_INDEX — 先跑 build")
        sys.exit(1)
    return [json.loads(line) for line in open(OUT, encoding="utf-8")]


def score(a, b):
    keys = set(a) & set(b)
    return sum(a[k] * b[k] for k in keys), keys


def map_(topn=3, audit=False):
    recs = load()
    tree = [r for r in recs if r["book"] == "TREE"]
    memo = [r for r in recs if r["book"] in ("MAIN", "SUB")]
    counts = {tag: len([r for r in recs if r["book"] == tag]) for tag in ("TREE", "MAIN", "SUB")}
    print("TREE 节 %d ｜ 备忘录 节 %d（主 %d／子 %d）" % (len(tree), len(memo), counts["MAIN"], counts["SUB"]))
    lines = ["# 树册 ↔ 双路备忘录 映射报告（Stage-2 修复版）\n", "> 判据＝共享锚；标题识别范围 `#{1,3}`。\n"]
    nohit = 0
    noanchor = 0
    for tree_rec in tree:
        tree_anchors = tree_rec["anchors"]
        if not tree_anchors:
            noanchor += 1
        candidates = []
        for memo_rec in memo:
            value, keys = score(tree_anchors, memo_rec["anchors"])
            if value > 0:
                candidates.append((value, memo_rec, keys))
        candidates.sort(key=lambda item: -item[0])
        if not candidates:
            nohit += 1
            lines.append("- `%s` （%d 字·锚 %d）｜**无对口**" % (tree_rec["heading"][:70], tree_rec["chars"], len(tree_anchors)))
            continue
        lines.append("- `%s` （%d 字·锚 %d）" % (tree_rec["heading"][:70], tree_rec["chars"], len(tree_anchors)))
        for value, memo_rec, keys in candidates[:topn]:
            lines.append("    ← %s `%s` 分=%d （%s）" % (memo_rec["book"], memo_rec["heading"][:60], value, ",".join(sorted(keys)[:5])))
    lines.append("\n## 汇总\n")
    lines.append("- 树节 %d｜**无对口 %d**｜**无锚 %d**" % (len(tree), nohit, noanchor))
    lines.append("- 节数：TREE %d｜MAIN %d｜SUB %d" % (counts["TREE"], counts["MAIN"], counts["SUB"]))
    if audit:
        bad = [r for r in tree if not r["anchors"]]
        lines.append("\n## 树节之无锚者（审计）\n")
        for rec in bad:
            lines.append("- `%s` ｜%d 字" % (rec["heading"][:80], rec["chars"]))
    text = "\n".join(lines) + "\n"
    with open(REP, "x", encoding="utf-8", newline="\n") as writer:
        writer.write(text)
    print("WROTE", REP)


if __name__ == "__main__":
    command = sys.argv[1] if len(sys.argv) > 1 else "map"
    if command == "build":
        build()
    elif command == "map":
        map_(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    elif command == "audit":
        map_(3, audit=True)
    else:
        print(__doc__)
