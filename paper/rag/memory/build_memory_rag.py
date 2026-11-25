#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# build_memory_rag.py — 记忆 RAG · 索引重建（v5preR2 重做令③·就既有树·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-25 10:37:13「两帐树要在**既有帐树**上更新，不得另起一套」
#       ＋前令「RAG 同理＝记忆 RAG＋实验 RAG，两套各自独立」＋PI 09:47 校正。
# 语料：**既有记忆帐树固定名件**（不新建并行树）——
#   · 记忆册树（查理_底账树 10 件：8 冻结分册＋根索引＋活跃分册）
#   · 帐树现态面（查理_帐树实例_现态快照面.md＋查理_帐树实例_鲜活例案面.md）
# 本轮在原树上增了什么：现态快照面第 176/177 轮（v5preR2 派单窗＋重做窗）
# 纪律：纯案头 0 API 费·BM25（k1=1.5·b=0.75）·CJK 双字＋ASCII 词元·行级指针溯源·
#       索引只存 token→块映射与块元数据（不复制正文·凭据 0 入册）。
# 用法：python3 paper/rag/memory/build_memory_rag.py
# ============================================================================
import hashlib, json, os, re, sys, time
from collections import Counter
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = "/home/z/my-project/shared"
OUT = os.path.join(HERE, "index.json")
RE_ASCII = re.compile(r"[A-Za-z0-9_.\-]{2,}")
RE_CJK = re.compile(r"[\u4e00-\u9fff]+")

# 既有记忆帐树固定名件（不另起一套）
CORPUS = [
    ("记忆册树", "查理_底账树/分册1_建账与故障恢复协议.md"),
    ("记忆册树", "查理_底账树/分册2_PI补喂逐字_P01-P54.md"),
    ("记忆册树", "查理_底账树/分册3_PI补喂逐字_P55-P93.md"),
    ("记忆册树", "查理_底账树/分册4_PI补喂逐字_P94-P133.md"),
    ("记忆册树", "查理_底账树/分册5_指令链与裁定总目_P01-P133.md"),
    ("记忆册树", "查理_底账树/分册6_诗面文本与R6约束.md"),
    ("记忆册树", "查理_底账树/分册7_尾注续跑清单.md"),
    ("记忆册树", "查理_底账树/分册8_尾行滚动史_折入53-147.md"),
    ("记忆册树", "查理_底账树/查理_底账树_根索引_2026_11_11.md"),
    ("记忆册树", "查理_底账树/查理_底账树_活跃分册_P134起_2026_11_11.md"),
    ("帐树现态面", "查理_帐树实例_现态快照面.md"),
    ("帐树现态面", "查理_帐树实例_鲜活例案面.md"),
]


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


def add_chunk(chunks, postings, ci, l0, l1, ctext):
    cid = len(chunks)
    chunks.append({"c": ci, "l0": l0, "l1": l1, "n": len(ctext)})
    for tk, tfv in Counter(tokenize(ctext)).items():
        postings.setdefault(tk, []).extend([cid, tfv])


def build():
    t0 = time.time()
    corpus_meta, chunks, postings = [], [], {}
    total = 0
    for ci, (tree, rel) in enumerate(CORPUS):
        p = os.path.join(SHARED, rel)
        if not os.path.exists(p):
            corpus_meta.append({"tree": tree, "path": rel, "missing": True}); continue
        raw = open(p, "rb").read()
        corpus_meta.append({"tree": tree, "path": rel,
                            "fp": hashlib.sha256(raw).hexdigest()[:12],
                            "lines": raw.count(b"\n"), "bytes": len(raw)})
        lines = raw.decode("utf-8", errors="replace").split("\n")
        buf, l0, nch = [], None, 0
        for li, line in enumerate(lines, 1):
            while len(line) > 24000:
                if buf:
                    add_chunk(chunks, postings, ci, l0, li - 1, "\n".join(buf)); buf, l0, nch = [], None, 0
                sub, line = line[:24000], line[24000:]
                add_chunk(chunks, postings, ci, li, li, sub)
            if l0 is None: l0 = li
            buf.append(line); nch += len(line) + 1; total += len(line) + 1
            if (len(buf) >= 40 and nch >= 3000) or nch >= 24000:
                add_chunk(chunks, postings, ci, l0, li, "\n".join(buf)); buf, l0, nch = [], None, 0
        if buf:
            add_chunk(chunks, postings, ci, l0, l0 + len(buf) - 1, "\n".join(buf))
    idx = {"version": 1, "built": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
           "builder": "查理-论文主笔（v5preR2 重做令③·记忆 RAG·就既有树）",
           "note": "记忆 RAG——语料＝**既有记忆帐树固定名件**（记忆册树 10＋帐树现态面 2），不另建并行树；与实验 RAG 完全分立。本轮在原树增：现态快照面第 176/177 轮。纯案头 0 API 费·BM25（k1=1.5·b=0.75）·CJK 双字＋ASCII 词元·行级指针溯源·索引不复制正文（凭据 0 入册）。",
           "corpus": corpus_meta, "avgdl": (total / len(chunks)) if chunks else 0,
           "chunks": chunks, "postings": postings,
           "stats": {"chunks": len(chunks), "tokens": len(postings), "chars": total,
                     "elapsed_s": round(time.time() - t0, 2)}}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False)
    print("记忆 RAG index -> %s" % OUT)
    print("语料 %d 件（缺 %d）·块 %d·词元 %d·%.1fs" % (
        len(corpus_meta), sum(1 for c in corpus_meta if c.get("missing")),
        len(chunks), len(postings), time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(build())
