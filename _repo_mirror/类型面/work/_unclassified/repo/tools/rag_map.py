#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rag_map.py — 树册 ↔ 双路备忘录 之**映射工具**（2026-10-29 立）

## 为什么另立此件（不改 rag_index.py）

`tools/rag_index.py` 之 `targets()` 只扫 `results/` **根层** `*.md` 与 `pi_rulings/*.md`
（其 docstring 虽称「两份备忘录」，代码未含）。而**双路备忘录在子目录**：
    主代理册 = results/doc/document/_root_session_history_memo_main_2026_10_14.md
    子代理册 = results/work/process/_sub_agent_memo_2026_10_24_v4.md
    树册     = results/work/process/_experiment_tree_v2_main_2026_10_23.md
⇒ 三者**永远进不了原索引**。本件自建索引，不依赖原件。

## 它回答什么

    树册的某一节，在双路备忘录里**有没有对口**？对口在哪一节？

其判据**不是**关键词相似，而是**共享锚**（硬证据）：
    件名（权重 3）｜指纹 12 位（3）｜裁号 vNNN（2）｜位号（1）｜节号 §NN-NN（1）

## 用法

    python -P tools/rag_map.py build     # 解析三册 ＋ 裁答册，建 results/.tmp/_rag_map.jsonl
    python -P tools/rag_map.py map 3     # 出映射表（每树节 top-3），并报无对口者
    python -P tools/rag_map.py audit     # 兼报：树节之无锚者（《体例之正》§10③ 第四职「据」之检）
    python -P tools/rag_map.py find v612 # **反查**：某裁号／件名片段／指纹前段／位号，在哪几节出现

扫描面：树册 ＋ 主代理册 ＋ 子代理册 ＋ `pi_rulings/`（619 件）。
反查之实用处：同一锚在「错的那节」与「正的那节」并列出现（实证：`find 5343345b7281`
并出树册 `§60-93-1`（反读）与 `§60-95-2`（其正））。

输出（map/audit）同时写 `results/.tmp/_rag_map_report.md`。
"""
import sys, os, re, json, hashlib, collections

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
OUT = os.path.join(ROOT, "results", ".tmp", "_rag_map.jsonl")
REP = os.path.join(ROOT, "results", ".tmp", "_rag_map_report.md")

BOOKS = [
    ("TREE", "results/work/process/_experiment_tree_v2_main_2026_10_23.md"),
    ("MAIN", "results/doc/document/_root_session_history_memo_main_2026_10_14.md"),
    ("SUB",  "results/work/process/_sub_agent_memo_2026_10_24_v4.md"),
]
# 裁答册（pi_rulings\*.md）单列一族：使 `find vNNN` 能直指其件，而不只命中三册。
PR_DIR = "pi_rulings"

RE_FN   = re.compile(r"[A-Za-z0-9_\-]{3,}?_\d{4}_\d{2}_\d{2}\.(?:md|json|py|txt|csv|tsv)")
RE_FP   = re.compile(r"`([0-9a-f]{12})`")
RE_RUL  = re.compile(r"\bv(\d{2,3})\b")
RE_SEC  = re.compile(r"§(\d{2}-\d{2}(?:-[a-z0-9]+)?)")
RE_POS  = re.compile(r"\b(KD-[A-Za-z0-9\-]{1,18}|R-\d{1,2}|T-[1-5]|F-\d{2}|E-\d{2}|N-\d|P-\d|U-\d{1,2}|D-\d{1,2}|项\s?\d{1,2})\b")
RE_HEAD = re.compile(r"^(#{2,3})\s+§?(\S{1,24})")


def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12]


def sections(text):
    """按 ## / ### 之 § 标题切节；返回 [(节号, 标题, 正文)]。"""
    lines = text.split("\n")
    marks = []
    for i, ln in enumerate(lines):
        m = RE_HEAD.match(ln)
        if m:
            marks.append((i, ln.strip()))
    out = []
    for k, (i, ln) in enumerate(marks):
        j = marks[k + 1][0] if k + 1 < len(marks) else len(lines)
        body = "\n".join(lines[i:j])
        out.append((ln, body))
    return out


def anchors(text):
    a = collections.Counter()
    for m in RE_FN.findall(text):
        a["FN:" + m] += 3
    for m in RE_FP.findall(text):
        a["FP:" + m] += 3
    for m in RE_RUL.findall(text):
        a["RU:v" + m] += 2
    for m in RE_SEC.findall(text):
        a["SE:" + m] += 1
    for m in RE_POS.findall(text):
        a["PO:" + m.replace(" ", "")] += 1
    return a


def build():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    recs = []
    targets = list(BOOKS)
    prdir = os.path.join(ROOT, PR_DIR)
    if os.path.isdir(prdir):
        for n in sorted(os.listdir(prdir)):
            if n.lower().endswith(".md"):
                targets.append(("PR", PR_DIR + "/" + n))
    for tag, rel in targets:
        p = os.path.join(ROOT, rel.replace("/", "\\"))
        if not os.path.exists(p):
            print("MISS", tag, rel)
            continue
        raw = open(p, "rb").read()
        text = raw.decode("utf-8", errors="ignore")
        secs = sections(text)
        if not secs:                      # 无节标题之件，整件作一节
            secs = [("(件首) " + rel.rsplit("/", 1)[-1], text)]
        fp = sha12(p)
        # 裁答册：把**文件名里的裁号**也作锚 —— 否则 `find v612` 查不到该册自身
        fname_rul = None
        if tag == "PR":
            mm = re.search(r"_(v\d{2,3})\.md$", rel)
            if mm:
                fname_rul = "RU:" + mm.group(1)
        for idx, (head, body) in enumerate(secs):
            a = anchors(body)
            # 只给「件首」一节盖文件名裁号锚 —— 否则该册每一节都会命中，反查失去分辨力
            if fname_rul and idx == 0:
                a[fname_rul] += 2
            recs.append({
                "book": tag, "file": rel, "sha12": fp, "bytes": len(raw),
                "heading": head[:120], "chars": len(body),
                "anchors": a,
            })
        if tag != "PR":
            print("BOOK %-4s %-8d 节 %s" % (tag, len(raw), len(secs)))
    n_pr = sum(1 for r in recs if r["book"] == "PR")
    print("BOOK PR   %d 件 → %d 节" % (len(targets) - len(BOOKS), n_pr))
    with open(OUT, "w", encoding="utf-8", newline="\n") as w:
        for r in recs:
            r["anchors"] = dict(r["anchors"])
            w.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("WROTE", OUT, len(recs), "节之记录")
    return recs


def load():
    if not os.path.exists(OUT):
        print("NO_INDEX — 先跑 build")
        sys.exit(1)
    return [json.loads(l) for l in open(OUT, encoding="utf-8")]


def score(a, b):
    s = 0
    keys = set(a) & set(b)
    for k in keys:
        s += a[k] * b[k]
    return s, keys


def map_(topn=3, audit=False):
    recs = load()
    tree = [r for r in recs if r["book"] == "TREE"]
    memo = [r for r in recs if r["book"] in ("MAIN", "SUB")]
    print("TREE 节 %d ｜ 备忘录 节 %d（主 %d／子 %d）" % (
        len(tree), len(memo),
        len([r for r in memo if r["book"] == "MAIN"]),
        len([r for r in memo if r["book"] == "SUB"])))

    lines = []
    lines.append("# 树册 ↔ 双路备忘录 映射报告\n")
    lines.append("> 判据＝**共享锚**（件名3／指纹3／裁号2／位号1／节号1），非关键词相似。\n")

    nohit = 0
    noanchor = 0
    for t in tree:
        ta = t["anchors"]
        if not ta:
            noanchor += 1
        cand = []
        for m in memo:
            s, keys = score(ta, m["anchors"])
            if s > 0:
                cand.append((s, m, keys))
        cand.sort(key=lambda x: -x[0])
        if not cand:
            nohit += 1
            lines.append("- `%s` （%d 字·锚 %d）｜**无对口**" % (
                t["heading"][:70], t["chars"], len(ta)))
            continue
        lines.append("- `%s` （%d 字·锚 %d）" % (t["heading"][:70], t["chars"], len(ta)))
        for s, m, keys in cand[:topn]:
            top = ",".join(sorted(keys)[:5])
            lines.append("    ← %s `%s` 分=%d （%s）" % (m["book"], m["heading"][:60], s, top))

    lines.append("\n## 汇总\n")
    lines.append("- 树节 %d｜**无对口 %d**｜**无锚 %d**" % (len(tree), nohit, noanchor))
    txt = "\n".join(lines) + "\n"
    open(REP, "w", encoding="utf-8", newline="\n").write(txt)
    print(txt[:4000])
    print("\nWROTE", REP)

    if audit:
        bad = [t for t in tree if not t["anchors"]]
        print("\n=== audit：树节之无锚者（《体例之正》§10③ 第四职「据」之检）===")
        print("无锚树节 %d / %d" % (len(bad), len(tree)))
        for t in bad[:25]:
            print("  -", t["heading"][:80], "｜%d 字" % t["chars"])


def find(tok, limit=40):
    """反查：某锚（件名／指纹／裁号／位号）在树册与两册的哪些节出现。"""
    recs = load()
    tok = tok.strip()
    cands = set()
    # 归一：容许用户直接给 v612 / 612 / 指纹前 8 位 / 件名片段
    if re.fullmatch(r"v?\d{2,3}", tok):
        cands.add("RU:v" + tok.lstrip("v"))
    if re.fullmatch(r"[0-9a-f]{6,12}", tok):
        for r in recs:
            for k in r["anchors"]:
                if k.startswith("FP:") and k[3:].startswith(tok):
                    cands.add(k)
    for r in recs:
        for k in r["anchors"]:
            body = k.split(":", 1)[1] if ":" in k else k
            if tok == body or tok in body:
                cands.add(k)
    if not cands:
        print("NO_ANCHOR_MATCH — 该串不在任何节之锚集内（射程：三册之锚面）")
        return
    print("命中锚 %d 枚：%s" % (len(cands), ", ".join(sorted(cands)[:12])))
    hits = []
    for r in recs:
        inter = cands & set(r["anchors"])
        if inter:
            hits.append((len(inter), r, sorted(inter)))
    hits.sort(key=lambda x: (-x[0], x[1]["book"]))
    print("出现于 %d 节（上限 %d）：\n" % (len(hits), limit))
    for n, r, inter in hits[:limit]:
        print("  [%s] %-58s 锚%d 命中%d （%s）" % (
            r["book"], r["heading"][:58], len(r["anchors"]), n, ",".join(inter[:3])))
    if len(hits) > limit:
        print("  …余 %d 节（调大 limit）" % (len(hits) - limit))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "map"
    if cmd == "build":
        build()
    elif cmd == "map":
        n = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        map_(n)
    elif cmd == "audit":
        map_(3, audit=True)
    elif cmd == "find":
        if len(sys.argv) < 3:
            print("用法：python -P tools/rag_map.py find <件名片段|指纹前段|vNNN|位号>")
        else:
            find(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 40)
    else:
        print(__doc__)
