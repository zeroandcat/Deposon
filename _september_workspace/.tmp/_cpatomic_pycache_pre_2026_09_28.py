# -*- coding: utf-8 -*-
"""CLEAN-A棒 · 清前登记：18 frozen 复算 + 8 个 __pycache__ 目录逐件 SHA-12 登记。

只读脚本（0 写入除本脚本自身落盘）。SHA-12 = hashlib.sha256(hexdigest)[:12] 小写。
铁律：0 LLM / key 永不明文 / 0 改实验逻辑 / 0 触动 frozen。
"""
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path("D:/私人资料/deposon-repo")
BASE = ROOT / "results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json"
OUT = ROOT / ".tmp/_cpatomic_pycache_pre_2026_09_28.json"

# 慢处置 B §3.3 登记的 8 个目录（repo 相对路径），逐字沿用，不新增不删减
PYCACHE_DIRS = [
    ".tmp/__pycache__",
    "verifier/kill_lines/__pycache__",
    "verifier/audit/__pycache__",
    "results/__pycache__",
    "results/_v3_recheck_08b_executor/__pycache__",
    "results/_v3_s1_executor/__pycache__",
    "results/_v3_s3_wordexpand_data/__pycache__",
    "deposon_team/plugins/__pycache__",
]

# 贴邻 frozen 的两个目录：清缓存不动 frozen 本体 -> 单独标 gated
GATED = {"verifier/audit/__pycache__", "verifier/kill_lines/__pycache__"}


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def frozen_scan():
    base = json.loads(BASE.read_text(encoding="utf-8"))["all_results"]
    rows = []
    for r in base:
        p = ROOT / r["path"]
        if p.exists():
            a = sha12(p)
            rows.append({"path": r["path"], "expected_sha12": r["expected_sha12"],
                         "actual_sha12": a, "bytes": p.stat().st_size,
                         "match": a == r["expected_sha12"]})
        else:
            rows.append({"path": r["path"], "expected_sha12": r["expected_sha12"],
                         "actual_sha12": None, "bytes": None, "match": False,
                         "note": "MISSING"})
    return rows


def pycache_scan():
    dirs = []
    for rel in PYCACHE_DIRS:
        d = ROOT / rel
        files = []
        if d.is_dir():
            for f in sorted(d.rglob("*")):
                if f.is_file():
                    files.append({"name": f.relative_to(d).as_posix(),
                                  "bytes": f.stat().st_size,
                                  "sha12": sha12(f)})
        dirs.append({
            "rel": rel,
            "exists": d.is_dir(),
            "gated_frozen_adjacent": rel in GATED,
            "n_files": len(files),
            "total_bytes": sum(x["bytes"] for x in files),
            "non_pyc": [x["name"] for x in files if not x["name"].endswith(".pyc")],
            "files": files,
        })
    return dirs


def main():
    frozen = frozen_scan()
    dirs = pycache_scan()
    rep = {
        "schema": "v4_cpatomic_pycache_pre/1",
        "date": "2026-09-28",
        "frozen_baseline_source": BASE.relative_to(ROOT).as_posix(),
        "n_frozen": len(frozen),
        "frozen_pass": sum(1 for r in frozen if r["match"]),
        "frozen_fail": [r["path"] for r in frozen if not r["match"]],
        "frozen_rows": frozen,
        "n_pyc_dirs": len(dirs),
        "pyc_total_files": sum(d["n_files"] for d in dirs),
        "pyc_total_bytes": sum(d["total_bytes"] for d in dirs),
        "pyc_dirs": dirs,
    }
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"frozen: {rep['frozen_pass']}/{rep['n_frozen']} PASS  fail={rep['frozen_fail']}")
    print(f"pycache dirs={rep['n_pyc_dirs']} files={rep['pyc_total_files']} bytes={rep['pyc_total_bytes']}")
    for d in dirs:
        gate = " [GATED:frozen-adjacent]" if d["gated_frozen_adjacent"] else ""
        print(f"  {d['rel']:52s} exists={d['exists']} files={d['n_files']:3d} "
              f"bytes={d['total_bytes']:8d} non_pyc={d['non_pyc']}{gate}")
    print(f"OUT -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
