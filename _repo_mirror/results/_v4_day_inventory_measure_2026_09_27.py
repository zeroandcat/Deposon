#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V4 收尾整理 · 今日（2026-09-27）文件夹四件套 ①盘点 ③台账 ④计数校正 实测器
=====================================================================
出件：Mavis 团队 evidence-auditor（agent-11335500b168）
性质：只读实测（不写不改任何既有件）；仅 stdout 输出 JSON
口径锚：results/_v4_maindir_count_monitor_2026_09_27.md（SHA-12 71e9cc179bec）
      results/_v4_maindir_cleanup_moves_ledger_v6_2026_09_26.md（SHA-12 CC498BC28525）
SHA-12 定义：hashlib.sha256(bytes).hexdigest()[:12]（hexdigest 已小写）
边界：R5 frozen 只追加 / V1-V3 只读 / 派生 JSON 不合并 / key 永不明文 / 0 擅调阈值
"""

import hashlib
import json
import os
import sys
from datetime import datetime

WS = r"D:\私人资料\deposon-repo"
SIB_ARCHIVE = r"D:\私人资料\_non_upload_local_archive"   # 归档目录
SIB_SUB = r"D:\私人资料\deposon-sub"                     # 副目录
TODAY = "2026-09-27"
SCAN_DIRS = ("results", "letters", "docs")

TEMP_DIR_SEG = "\\.tmp\\"
PYCACHE_SEG = "\\__pycache__\\"
TEMP_EXT = (".pyc", ".log", ".bak", ".tmp", ".swp", ".part")


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:12]


def walk_all(root):
    out = []
    for dirpath, dirnames, filenames in os.walk(root):
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            try:
                st = os.stat(p)
            except OSError as e:
                out.append({"path": p, "error": str(e)})
                continue
            out.append({
                "path": p,
                "rel": os.path.relpath(p, root).replace("\\", "/"),
                "bytes": st.st_size,
                "mtime": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "ctime": datetime.fromtimestamp(st.st_ctime).strftime("%Y-%m-%d %H:%M:%S"),
            })
    return out


def is_tempish(f):
    p = f["path"]
    low = p.lower()
    if TEMP_DIR_SEG in low + "\\":
        return True
    if PYCACHE_SEG in low + "\\":
        return True
    return f["rel"].rsplit(".", 1)[-1].lower() in [e[1:] for e in TEMP_EXT] if "." in f["rel"] else False


def main():
    rep = {"measured_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "ws": WS}

    # ---------- ④ 三口径计数（主目录） ----------
    all_main = walk_all(WS)
    git = [f for f in all_main if "\\.git\\" in f["path"]]
    maindir = [f for f in all_main if "\\.git\\" not in f["path"]]
    universal = [f for f in maindir if not is_tempish(f)]
    with_temp = maindir
    rep["counts"] = {
        "maindir": len(maindir),
        "universal": len(universal),
        "with_temp": len(with_temp),
        "git_excluded": len(git),
        "temp_zone_total": len(maindir) - len(universal),
    }

    # 临时区子类明细
    buckets = {".tmp_subtree": 0, "__pycache___subtree": 0, "pyc": 0, "log": 0, "other_temp_ext": 0}
    tmpfiles, pycaches, pycs, logs, othert = [], [], [], [], []
    for f in maindir:
        p, low, rel = f["path"], f["path"].lower(), f["rel"]
        ext = rel.rsplit(".", 1)[-1].lower() if "." in rel else ""
        if TEMP_DIR_SEG in low + "\\":
            tmpfiles.append(f); buckets[".tmp_subtree"] += 1
        elif PYCACHE_SEG in low + "\\":
            pycaches.append(f); buckets["__pycache___subtree"] += 1
        elif ext == "pyc":
            pycs.append(f); buckets["pyc"] += 1
        elif ext == "log":
            logs.append(f); buckets["log"] += 1
        elif ext in ("bak", "tmp", "swp", "part"):
            othert.append(f); buckets["other_temp_ext"] += 1
    rep["temp_buckets"] = buckets

    # 顶层目录文件数明细（复核 09-27 11:47 台账 §C.4 的 1012 vs 1009 疑点）
    top = {}
    for f in maindir:
        head = f["rel"].split("/")[0]
        top[head] = top.get(head, 0) + 1
    top_files = [f for f in maindir if "/" not in f["rel"]]
    rep["top_level"] = {
        "dirs": dict(sorted(top.items(), key=lambda kv: -kv[1])),
        "dir_sum": sum(top.values()),
        "top_scattered_files": len(top_files),
        "grand_total": len(maindir),
    }

    # ---------- ① 今日盘点（results / letters / docs） ----------
    today = []
    for f in maindir:
        head = f["rel"].split("/")[0]
        if head not in SCAN_DIRS:
            continue
        if not f["mtime"].startswith(TODAY):
            continue
        f = dict(f)
        f["sha12"] = sha12(f["path"])
        today.append(f)
    today.sort(key=lambda x: (x["mtime"], x["rel"]))
    rep["today_inventory"] = {
        "count": len(today),
        "total_bytes": sum(f["bytes"] for f in today),
        "by_topdir": {d: sum(1 for f in today if f["rel"].split("/")[0] == d) for d in SCAN_DIRS},
        "files": today,
    }

    # 今日件按 ctime / mtime 双口径
    rep["today_dual"] = {
        "mtime_0927": len(today),
        "ctime_0927_all_main": sum(1 for f in maindir if f["ctime"].startswith(TODAY)),
    }

    # ---------- ② .tmp 清前登记 ----------
    tmpdir = os.path.join(WS, ".tmp")
    tmp_inv = []
    for dirpath, dirnames, filenames in os.walk(tmpdir):
        for fn in filenames:
            p = os.path.join(dirpath, fn)
            st = os.stat(p)
            tmp_inv.append({
                "rel": os.path.relpath(p, WS).replace("\\", "/"),
                "bytes": st.st_size,
                "mtime": datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S"),
                "sha12": sha12(p),
            })
    tmp_inv.sort(key=lambda x: x["rel"])
    rep["tmp_before"] = {
        "count": len(tmp_inv),
        "total_bytes": sum(f["bytes"] for f in tmp_inv),
        "today_count": sum(1 for f in tmp_inv if f["mtime"].startswith(TODAY)),
        "today_bytes": sum(f["bytes"] for f in tmp_inv if f["mtime"].startswith(TODAY)),
        "files": tmp_inv,
    }

    # ---------- 三目录（主 / 归档 / 副） ----------
    tri = {}
    for label, root in (("main_主", WS), ("archive_归档", SIB_ARCHIVE), ("sub_副", SIB_SUB)):
        if not os.path.isdir(root):
            tri[label] = {"exists": False, "count": None}
            continue
        n = 0
        nbytes = 0
        for dirpath, dirnames, filenames in os.walk(root):
            if "\\.git\\" in dirpath + "\\":
                continue
            for fn in filenames:
                try:
                    nbytes += os.stat(os.path.join(dirpath, fn)).st_size
                    n += 1
                except OSError:
                    pass
        tri[label] = {"exists": True, "path": root, "count": n, "bytes": nbytes}
    rep["three_dirs"] = tri

    # ---------- key 形态自扫（严格 pattern，落盘前） ----------
    strict = re_strict = None
    try:
        import re
        strict = re.compile(
            r"\b(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|Bearer\s+[A-Za-z0-9]{20,}"
            r"|tp-[a-z0-9]{20,}|ark-[a-z0-9-]{20,})\b")
        wide = re.compile(
            r"\b(sk-[A-Za-z0-9]{20,}|AIza[0-9A-Za-z_-]{30,}|Bearer\s+[A-Za-z0-9]{20,}"
            r"|tp-[a-z0-9]{20,}|ark-[a-z0-9-]{20,}|api[_-]?key\s*[=:]\s*[\"'][^\"']{16,}"
            r"|Authorization\s*:\s*Bearer\s+\S{16,})\b", re.IGNORECASE)
        hits_s, hits_w = [], []
        for f in today:
            try:
                txt = open(f["path"], "r", encoding="utf-8", errors="ignore").read()
            except OSError:
                continue
            for name, rx, acc in (("strict", strict, hits_s), ("wide", wide, hits_w)):
                for m in rx.finditer(txt):
                    acc.append({"file": f["rel"], "pattern": name,
                                "snippet": m.group(0)[:60]})
        rep["key_scan"] = {"strict_hits": len(hits_s), "wide_hits": len(hits_w),
                           "strict_detail": hits_s[:20], "wide_detail": hits_w[:20]}
    except Exception as e:  # pragma: no cover
        rep["key_scan"] = {"error": str(e)}

    json.dump(rep, sys.stdout, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
