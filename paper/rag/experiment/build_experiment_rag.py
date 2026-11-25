#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================================
# build_experiment_rag.py — 实验 RAG · 索引重建（v5preR2 重做令③·就既有树·新写·0 改已验代码）
# ----------------------------------------------------------------------------
# 令源：群管理员 2026-11-25 10:37:13「两帐树要在**既有帐树**上更新，不得另起一套」
#       ＋前令「前版把 Python 事件树＋Lean 镜像树当『两帐树』，作废：它们降为实验帐树下的
#       证据件（Lean 镜像归实验侧机证）」＋PI 09:47 校正。
# 语料：**既有实验帐树固定名件**（不新建并行树）——
#   · 实验册树（查理_全量实验谱系总索引 1 件·含 N1–N15 增补）＋归档 4 件
#   · 证据件 5 件（Python 事件树·Lean 守恒镜像树·Lean 编译日志）——降位为证据件
#   · 仓内证据面 13 件（docs/thermo-generation.md 现役 0127ca353bef·mcp/·harness/）
# 本轮在原树上增了什么：实验册树 v3 增补 N 组 N1–N10（v5preR2 窗）＋ N11–N15（重做轮）
# 数字索引：使论文每个数字可回指证据位（来源路径＋行级锚）
# 纪律：纯案头 0 API 费·BM25（k1=1.5·b=0.75）·CJK 双字＋ASCII 词元·行级指针溯源·
#       索引只存 token→块映射与块元数据（不复制正文·凭据 0 入册）。
# 用法：python3 paper/rag/experiment/build_experiment_rag.py
# ============================================================================
import hashlib, json, os, re, sys, time
from collections import Counter
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
SHARED = "/home/z/my-project/shared"
OUT = os.path.join(HERE, "index.json")
RE_ASCII = re.compile(r"[A-Za-z0-9_.\-]{2,}")
RE_CJK = re.compile(r"[\u4e00-\u9fff]+")
RE_PCT = re.compile(r"\d+(?:\.\d+)?\s?%|\d+(?:\.\d+)?％")
RE_FRAC = re.compile(r"\b\d{1,7}\s*/\s*\d{1,7}\b")
RE_EQ = re.compile(r"\b\d{3,7}\s*=\s*\d[\d\s+＋]*")
RE_INT = re.compile(r"(?<![\d.])\d{2,7}(?![\d.])")

# 既有实验帐树固定名件（不另起一套）
EXPERIMENT_TREE = [
    ("实验册树", "查理_全量实验谱系总索引_2026_11_22.md"),
    ("实验册树", "02_归档/2026-11/_散件/爱丽丝_实验树记忆树并列审计_A轨主笔_20261116.md"),
    ("实验册树", "02_归档/2026-11/_散件/戴夫_实验树记忆树并列审计_B副签双盲复核_20261116.md"),
    ("实验册树", "02_归档/2026-11/_散件/戴夫_实验树记忆树审计_交叉对账合判_AB双审闭合_20261116.md"),
    ("实验册树", "02_归档/2026-11/_散件/查理_遗忘实验普查与实验册树增补_v1.2_20261119.md"),
]
EVIDENCE = [
    ("实验证据件", "paper/evidence/python_tree.json"),
    ("实验证据件", "paper/evidence/python_tree.md"),
    ("实验证据件", "paper/evidence/lean_tree.json"),
    ("实验证据件", "paper/evidence/lean_tree.md"),
    ("实验证据件", "paper/evidence/lean_build_66b53fc.log"),
]
REPO_EVIDENCE = [
    "docs/thermo-generation.md", "docs/evidence-rounds.md", "docs/readings-package-spec.md",
    "docs/slot-space-caliber.md", "README.md", "BENCHMARK.md",
    "mcp/thermo_core.py", "mcp/thermo_demo.py", "mcp/thermo_crosscheck.py",
    "harness/DeposonThermo.lean", "harness/lean_axiom_audit.py", "harness/thermo_live_round.py",
]
# 发射案现役 v3（真机 L1 根因分诊包·未入公开仓）
LAUNCH_V3 = os.path.join(SHARED, "爱丽丝_deposon热力学代preview.10_真机L1根因分诊包_20261125/docs/launch-v5preR2.md")


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


def norm_num(v):
    return v.replace(" ", "").replace("\u3000", "").replace("％", "%")


def add_chunk(chunks, postings, ci, l0, l1, ctext):
    cid = len(chunks)
    chunks.append({"c": ci, "l0": l0, "l1": l1, "n": len(ctext)})
    for tk, tfv in Counter(tokenize(ctext)).items():
        postings.setdefault(tk, []).extend([cid, tfv])


def build():
    t0 = time.time()
    entries = []
    for tree, rel in EXPERIMENT_TREE:
        entries.append((tree, os.path.join(SHARED, rel), rel))
    for tree, rel in EVIDENCE:
        entries.append((tree, os.path.join(REPO, rel), rel))
    for rel in REPO_EVIDENCE:
        entries.append(("仓内证据面", os.path.join(REPO, rel), rel))
    if os.path.exists(LAUNCH_V3):
        entries.append(("仓内证据面", LAUNCH_V3,
                        "爱丽丝_deposon热力学代preview.10_真机L1根因分诊包_20261125/docs/launch-v5preR2.md"))
    corpus_meta, chunks, postings, numbers = [], [], {}, []
    total = 0
    for ci, (tree, p, rel) in enumerate(entries):
        if not os.path.exists(p):
            corpus_meta.append({"tree": tree, "path": rel, "missing": True}); continue
        raw = open(p, "rb").read()
        corpus_meta.append({"tree": tree, "path": rel,
                            "fp": hashlib.sha256(raw).hexdigest()[:12],
                            "lines": raw.count(b"\n"), "bytes": len(raw)})
        lines = raw.decode("utf-8", errors="replace").split("\n")
        buf, l0, nch = [], None, 0
        for li, line in enumerate(lines, 1):
            for rx, kind in ((RE_PCT, "pct"), (RE_FRAC, "frac"), (RE_EQ, "eq")):
                for m in rx.finditer(line):
                    val = m.group(0).strip()
                    if 2 <= len(val) <= 60:
                        numbers.append({"v": norm_num(val), "kind": kind, "path": rel,
                                        "tree": tree, "line": li})
            for m in RE_INT.finditer(line):
                val = m.group(0)
                if len(val) >= 3:
                    numbers.append({"v": val, "kind": "int", "path": rel, "tree": tree, "line": li})
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
    nmap = {}
    for n in numbers:
        e = nmap.setdefault(n["v"], {"v": n["v"], "kind": n["kind"], "hits": [], "raw": []})
        e["hits"].append({"tree": n["tree"], "path": n["path"], "line": n["line"]})
        if n["v"] not in e["raw"]:
            e["raw"].append(n["v"])
    for v in nmap:
        seen, keep, last = set(), [], None
        for h in nmap[v]["hits"]:
            k = (h["path"], h["line"])
            if k in seen: continue
            seen.add(k)
            if last != h["tree"] or len([x for x in keep if x["tree"] == h["tree"]]) < 8:
                keep.append(h)
            last = h["tree"]
        nmap[v]["hits"] = keep
        nmap[v]["trees"] = sorted(set(h["tree"] for h in keep))
    idx = {"version": 1, "built": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
           "builder": "查理-论文主笔（v5preR2 重做令③·实验 RAG·就既有树）",
           "note": "实验 RAG——语料＝**既有实验帐树固定名件**（实验册树 5＋证据件 5＋仓内证据面 13），不另建并行树；与记忆 RAG 完全分立。Python 事件树与 Lean 守恒镜像树为本树证据件（Lean 镜像归实验侧机证）。本轮在原树增：实验册树 v3 增补 N1–N15。数字→证据位索引使论文每个数字可回指。纯案头 0 API 费·BM25（k1=1.5·b=0.75）·CJK 双字＋ASCII 词元·行级指针溯源·索引不复制正文（凭据 0 入册）。",
           "corpus": corpus_meta, "avgdl": (total / len(chunks)) if chunks else 0,
           "chunks": chunks, "postings": postings, "numbers": nmap,
           "n_numbers": len(nmap),
           "stats": {"chunks": len(chunks), "tokens": len(postings), "chars": total,
                     "elapsed_s": round(time.time() - t0, 2)}}
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(idx, f, ensure_ascii=False)
    print("实验 RAG index -> %s" % OUT)
    print("语料 %d 件（缺 %d）·块 %d·词元 %d·数字读数 %d 值·%.1fs" % (
        len(corpus_meta), sum(1 for c in corpus_meta if c.get("missing")),
        len(chunks), len(postings), len(nmap), time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(build())
