#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# query_experiment.py — 实验 RAG · 检索入口（v5preR2 重做令③·就既有树·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-25 10:37:13「两帐树要在既有帐树上更新，不得另起一套」
#       ＋前令「Python 事件树＋Lean 镜像树降为实验帐树下的证据件（Lean 镜像归实验侧机证）」
#       ＋PI 09:47 校正「两帐树指记忆帐树与实验帐树，RAG同理」。
# 语料：仅**既有实验帐树固定名件** 23 件——不查记忆侧。
# 模式：检索（BM25）· --数字（数字→证据位回指）· --清单
# 纪律：纯案头只读 0 API 费·索引不复制正文·答案以行级指针为准。
# 用法：
#   python3 paper/rag/experiment/query_experiment.py 耗散通道利用率        # 检索
#   python3 paper/rag/experiment/query_experiment.py --数字 69.23        # 数字回指
#   python3 paper/rag/experiment/query_experiment.py --数字 313050        # 守恒核回指
#   python3 paper/rag/experiment/query_experiment.py --清单                # 语料清单
# ============================================================================
import argparse, json, math, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(HERE, "index.json")
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
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
        print("实验 RAG 索引未建：先运行 python3 paper/rag/experiment/build_experiment_rag.py")
        sys.exit(1)
    return json.load(open(IDX, encoding="utf-8"))


def real_path(p):
    if os.path.isabs(p):
        return p
    if p.startswith(("查理_", "02_归档", "爱丽丝_")):
        return os.path.join(SHARED, p)
    return os.path.join(REPO, p)


def snippet(path, l0, l1, width=220):
    try:
        lines = open(real_path(path), encoding="utf-8", errors="replace").read().split("\n")
    except OSError:
        return "（路径不可读：%s）" % path
    seg = " ⏎ ".join(x.strip() for x in lines[max(0, l0 - 1):min(len(lines), l1)][:6])
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
        print("实验 RAG 无命中：%r" % query); return
    print("【实验 RAG】检索：%r · 命中 %d 块" % (query, len(hits)))
    for rank, (cid, sc) in enumerate(hits, 1):
        c = idx["chunks"][cid]
        cm = idx["corpus"][c["c"]]
        print("%d. [%.3f] %s · %s#L%d-L%d" % (rank, sc, cm["tree"], cm["path"], c["l0"], c["l1"]))
        print("   ↳ %s" % snippet(cm["path"], c["l0"], c["l1"]))


def show_number(idx, val):
    val = val.strip().replace(" ", "").replace("\u3000", "").replace("％", "%")
    m = idx["numbers"].get(val)
    if not m and re.fullmatch(r"\d+(?:\.\d+)?", val):
        for cand in (val + "%", val + "％", val):
            if cand in idx["numbers"]:
                m = idx["numbers"][cand]; break
    if not m and re.fullmatch(r"0\.\d+", val):
        pctv = ("%.4f" % (float(val) * 100)).rstrip("0").rstrip(".") + "%"
        m = idx["numbers"].get(pctv)
    if not m:
        cand = [k for k in idx["numbers"] if val in k]
        if not cand:
            print("数字 %r 未入实验 RAG 索引（共 %d 值）" % (val, idx["n_numbers"])); return
        print("数字 %r 精确未命中·近邻：%s" % (val, "、".join(sorted(cand)[:6]))); return
    print("数字 %s · 类型 %s · 证据位 %d 处（树 %s）" % (m["v"], m["kind"], len(m["hits"]), "、".join(m["trees"])))
    for h in m["hits"]:
        print("  • [%s] %s#L%d" % (h["tree"], h["path"], h["line"]))
        print("    ↳ %s" % snippet(h["path"], h["line"], h["line"], 150))


def manifest(idx):
    print("=== 实验 RAG · 语料清单（%d 件·块 %d·词元 %d·数字 %d 值·建 %s）===" % (
        len(idx["corpus"]), idx["stats"]["chunks"], idx["stats"]["tokens"],
        idx["n_numbers"], idx["built"]))
    for c in idx["corpus"]:
        if c.get("missing"):
            print("  [缺件] %s · %s" % (c["tree"], c["path"]))
        else:
            print("  %-6s %-58s %s·%d 行·%d B" % (c["tree"], c["path"][-58:], c["fp"], c["lines"], c["bytes"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query", nargs="*")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--数字", dest="num", default=None)
    ap.add_argument("--清单", action="store_true")
    a = ap.parse_args()
    idx = load()
    if a.清单:
        manifest(idx)
    elif a.num:
        show_number(idx, a.num)
    elif a.query:
        show_hits(idx, bm25(idx, " ".join(a.query), a.top), " ".join(a.query))
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
