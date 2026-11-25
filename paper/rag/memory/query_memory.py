#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# query_memory.py — 记忆 RAG · 检索入口（v5preR2 重做令③·就既有树·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-25 10:37:13「两帐树要在既有帐树上更新，不得另起一套」
#       ＋前令「RAG 同理＝记忆 RAG＋实验 RAG，两套各自独立」＋PI 09:47 校正。
# 语料：仅**既有记忆帐树固定名件** 12 件（记忆册树 10＋帐树现态面 2）——不查实验侧。
# 模式：检索（BM25）· --基线（三对表：索引锚/实测/快照面锚）· --清单
# 纪律：纯案头只读 0 API 费·索引不复制正文·答案以行级指针为准。
# 用法：
#   python3 paper/rag/memory/query_memory.py 帐树两固定名件      # 检索
#   python3 paper/rag/memory/query_memory.py --基线              # 基线一致性核
#   python3 paper/rag/memory/query_memory.py --清单              # 语料清单
# ============================================================================
import argparse, hashlib, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "index.json")
SHARED = "/home/z/my-project/shared"
K1, B = 1.5, 0.75
RE_ASCII = re.compile(r"[A-Za-z0-9_.\-]{2,}")
RE_CJK = re.compile(r"[\u4e00-\u9fff]+")


def tokenize(text):
    toks = []
    for m in RE_ASCII.finditer(text):
        toks.append(m.group(0).lower())
    for m in RE_CJK.finditer(text):
        s = m.group(0)
        if len(s) >= 2:
            for i in range(len(s) - 1):
                toks.append(s[i:i + 2])
        else:
            toks.append(s)
    return toks


def load():
    if not os.path.exists(IDX):
        print("记忆 RAG 索引未建：先运行 python3 paper/rag/memory/build_memory_rag.py")
        sys.exit(1)
    return json.load(open(IDX, encoding="utf-8"))


def snippet(path, l0, l1, width=200):
    real = path if os.path.isabs(path) else os.path.join(SHARED, path)
    try:
        lines = open(real, encoding="utf-8", errors="replace").read().split("\n")
    except OSError:
        return "（路径不可读：%s）" % path
    seg = " ⏎ ".join(x.strip() for x in lines[max(0, l0 - 1):min(len(lines), l1)][:5])
    return (seg[:width] + "…") if len(seg) > width else seg


def bm25(idx, query, top):
    toks = tokenize(query)
    if not toks:
        return []
    N, avgdl = len(idx["chunks"]), max(idx["avgdl"], 1.0)
    scores = {}
    for tk in toks:
        pl = idx["postings"].get(tk)
        if not pl:
            continue
        pairs = [(pl[i], pl[i + 1]) for i in range(0, len(pl), 2)]
        idf = math.log(1 + (N - len(pairs) + 0.5) / (len(pairs) + 0.5))
        for cid, tf in pairs:
            c = idx["chunks"][cid]
            denom = tf + K1 * (1 - B + B * c["n"] / avgdl)
            scores[cid] = scores.get(cid, 0.0) + idf * (tf * (K1 + 1)) / denom
    return sorted(scores.items(), key=lambda x: -x[1])[:top]


def show_hits(idx, hits, query):
    if not hits:
        print("记忆 RAG 无命中：%r" % query); return
    print("【记忆 RAG】检索：%r · 命中 %d 块" % (query, len(hits)))
    for rank, (cid, sc) in enumerate(hits, 1):
        c = idx["chunks"][cid]
        cm = idx["corpus"][c["c"]]
        print("%d. [%.3f] %s · %s#L%d-L%d" % (rank, sc, cm["tree"], cm["path"], c["l0"], c["l1"]))
        print("   ↳ %s" % snippet(cm["path"], c["l0"], c["l1"]))


def baseline(idx):
    """三对表：索引锚 vs 实测 vs 快照面锚"""
    act = next((c for c in idx["corpus"] if c.get("path", "").endswith("活跃分册_P134起_2026_11_11.md")), None)
    if not act:
        print("索引未含活跃分册"); return
    p = os.path.join(SHARED, act["path"])
    raw = open(p, "rb").read()
    cur_fp = hashlib.sha256(raw).hexdigest()[:12]
    print("=== 记忆 RAG · 基线三对表（既有树·固定名件）===")
    print("索引锚（活跃分册）：%s" % act["fp"])
    print("当前实测（活跃分册）：%s·%d 行·%d B" % (cur_fp, raw.count(b"\n"), len(raw)))
    try:
        snap = open(os.path.join(SHARED, "查理_帐树实例_现态快照面.md"), encoding="utf-8").read().split("\n")
        line5 = snap[4][:160] if len(snap) > 4 else ""
    except OSError:
        line5 = ""
    m = re.search(r"`([0-9a-f]{12})`", line5)
    snap_fp = m.group(1) if m else None
    print("快照面第 5 行锚：%s" % line5)
    print("快照面锚（sha12）：%s" % snap_fp)
    if act["fp"] == cur_fp == snap_fp:
        print("判定：三对齐 ✓（索引/实测/快照面同一态——可直接检索引用）")
    else:
        print("判定：滞后呈报——以「当前实测＋快照面」为准；索引锚 %s ≠ 实测 %s → 运行 build_memory_rag.py 再锚"
              % (act["fp"], cur_fp))


def manifest(idx):
    print("=== 记忆 RAG · 语料清单（%d 件·块 %d·词元 %d·建 %s）===" % (
        len(idx["corpus"]), idx["stats"]["chunks"], idx["stats"]["tokens"], idx["built"]))
    for c in idx["corpus"]:
        if c.get("missing"):
            print("  [缺件] %s · %s" % (c["tree"], c["path"]))
        else:
            print("  %-8s %-56s %s·%d 行·%d B" % (c["tree"], c["path"][-56:], c["fp"], c["lines"], c["bytes"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="*")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--基线", action="store_true")
    ap.add_argument("--清单", action="store_true")
    a = ap.parse_args()
    idx = load()
    if a.清单:
        manifest(idx)
    elif a.基线:
        baseline(idx)
    elif a.query:
        show_hits(idx, bm25(idx, " ".join(a.query), a.top), " ".join(a.query))
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
