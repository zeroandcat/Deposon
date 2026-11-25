#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rag_index.py — deposon 轻量 RAG 索引（建立 / 查询）

用途：备忘录（主版 29 万 B / 子棒版 61 万 B）与 results/（1 千余件 .md）体量已超线性通读之限；
      本工具把它们切成「节块」，抽关键词入索引，供按主题定位「哪件哪节讲到某面」。
      它不替代阅读，只回答「去哪读」。

用法：
    python tools/rag_index.py build            # 重建索引
    python tools/rag_index.py q 五零要件 20     # 查询，参数＝词 + 可选 topN

索引位置：results/.tmp/_rag_index.jsonl （每行一块）
    字段：file / sha12 / bytes / start / end / heading / head / kws
    - heading：该块所属之最近标题（含行号）
    - head   ：该块前 160 字（供扫读）
    - kws    ：该块之关键词袋（CJK 2-gram + 拉丁词，取频次前 24）

扫描面（默认）：results/ 根层 *.md、pi_rulings/ *.md、两份备忘录
    ⚠ 不扫 .tmp（工作面）、不扫归档区、不扫 sub、不读任何非 .md。
"""
import sys, os, json, re, hashlib, collections

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
OUT = os.path.join(ROOT, "results", ".tmp", "_rag_index.jsonl")
CHUNK_LINES = 40          # 每块最大行数
HEAD_LEN = 160
TOP_KW = 24

CJK = re.compile(r"[\u4e00-\u9fff]")
LAT = re.compile(r"[A-Za-z][A-Za-z0-9_\-]{2,}")


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12]


def kwbag(text):
    bag = collections.Counter()
    for m in LAT.findall(text):
        bag[m.lower()] += 1
    cjk = CJK.findall(text)
    for i in range(len(cjk) - 1):
        bag[cjk[i] + cjk[i + 1]] += 1
    return [w for w, _ in bag.most_common(TOP_KW)]


def targets():
    out = []
    res = os.path.join(ROOT, "results")
    for n in sorted(os.listdir(res)):
        p = os.path.join(res, n)
        if os.path.isfile(p) and n.lower().endswith(".md"):
            out.append(p)
    pr = os.path.join(ROOT, "pi_rulings")
    if os.path.isdir(pr):
        for n in sorted(os.listdir(pr)):
            p = os.path.join(pr, n)
            if os.path.isfile(p) and n.lower().endswith(".md"):
                out.append(p)
    return out


def build():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    files = targets()
    n_chunk = 0
    with open(OUT, "w", encoding="utf-8", newline="\n") as w:
        for p in files:
            try:
                raw = open(p, "rb").read()
                text = raw.decode("utf-8", errors="ignore")
            except Exception:
                continue
            lines = text.splitlines()
            fp = sha12(p)
            sz = len(raw)
            rel = os.path.relpath(p, ROOT)
            heading = "(件首)"
            i = 0
            while i < len(lines):
                chunk = lines[i:i + CHUNK_LINES]
                # 块内若出现标题，更新 heading（以块内最后一个标题为准）
                for ln in chunk:
                    if re.match(r"^#{1,4}\s", ln):
                        heading = "L%d %s" % (i + 1, ln.strip()[:80])
                body = "\n".join(chunk)
                if body.strip():
                    rec = {
                        "file": rel, "sha12": fp, "bytes": sz,
                        "start": i + 1, "end": min(i + CHUNK_LINES, len(lines)),
                        "heading": heading,
                        "head": re.sub(r"\s+", " ", body.strip())[:HEAD_LEN],
                        "kws": kwbag(body),
                    }
                    w.write(json.dumps(rec, ensure_ascii=False) + "\n")
                    n_chunk += 1
                i += CHUNK_LINES
    print("files=%d chunks=%d index=%s size=%d" % (len(files), n_chunk, OUT, os.path.getsize(OUT)))


def query(term, topn=20):
    if not os.path.exists(OUT):
        print("索引不存在，先 build")
        return
    kws = kwbag(term)
    hits = []
    with open(OUT, encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            score = sum(1 for k in kws if k in r["kws"])
            if term in r["head"]:
                score += 3
            if term in r["heading"]:
                score += 5
            if score:
                hits.append((score, r))
    hits.sort(key=lambda x: -x[0])
    print("== 查询: %s ｜ 命中块 %d ｜ 显示前 %d ==" % (term, len(hits), min(topn, len(hits))))
    for s, r in hits[:topn]:
        print("[%2d] %s L%d-%d ｜ %s" % (s, r["file"], r["start"], r["end"], r["heading"]))
        print("      %s" % r["head"][:140])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    cmd = sys.argv[1]
    if cmd == "build":
        build()
    elif cmd == "q":
        query(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 20)
    else:
        print(__doc__)
