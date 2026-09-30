# -*- coding: utf-8 -*-
"""CLEAN-A棒 · 清后复验：8 个 __pycache__ 清零确认 + 18 frozen 0 触动自证。

清前登记表 = .tmp/_cpatomic_pycache_pre_2026_09_28.json（本件 0 覆盖, 只读对照）。
"""
import hashlib
import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path("D:/私人资料/deposon-repo")
BASE = ROOT / "results/_v3x_18frozen_remeasure_2026_09_16/v3x_18frozen_remeasure_results_2026_09_16.json"
PRE = ROOT / ".tmp/_cpatomic_pycache_pre_2026_09_28.json"
OUT = ROOT / ".tmp/_cpatomic_pycache_post_2026_09_28.json"


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def main():
    pre = json.loads(PRE.read_text(encoding="utf-8"))

    # ---- 清后: 全仓 __pycache__ 目录复扫 (不限 8 个, 防遗漏 + 防新增)
    found = sorted(p.relative_to(ROOT).as_posix()
                   for p in ROOT.rglob("__pycache__") if p.is_dir())
    # ---- 清后: 8 个目标目录逐个确认
    dirs_post = []
    for d in pre["pyc_dirs"]:
        p = ROOT / d["rel"]
        n = sum(1 for _ in p.rglob("*") if _.is_file()) if p.is_dir() else 0
        dirs_post.append({"rel": d["rel"], "exists_after": p.is_dir(),
                          "files_after": n, "files_before": d["n_files"],
                          "bytes_before": d["total_bytes"],
                          "gone": (not p.is_dir())})

    # ---- 18 frozen 复算
    base = json.loads(BASE.read_text(encoding="utf-8"))["all_results"]
    frozen_post = []
    for r in base:
        p = ROOT / r["path"]
        a = sha12(p) if p.exists() else None
        frozen_post.append({"path": r["path"], "expected_sha12": r["expected_sha12"],
                            "actual_sha12": a,
                            "bytes": p.stat().st_size if p.exists() else None,
                            "match": a == r["expected_sha12"]})

    # ---- 贴邻 frozen 的清缓存面: conservation.py 清前/清后
    cons = ROOT / "verifier/audit/conservation.py"
    cons_pre_row = next(r for r in pre["frozen_rows"]
                        if r["path"] == "verifier/audit/conservation.py")
    cons_post = {"path": "verifier/audit/conservation.py",
                 "pre_sha12": cons_pre_row["actual_sha12"],
                 "post_sha12": sha12(cons), "pre_bytes": cons_pre_row["bytes"],
                 "post_bytes": cons.stat().st_size}

    # ---- 被引原件 (修复面源件) 清后 0 触动复验
    srcs = [
        "results/_v4_supp_t15r2_executor_r1_2026_09_28.py",
        "results/_v4_supp_t15r2_executor.py",
        "results/_v4_supp_t15_executor_r1_2026_09_27.py",
        "results/_v4_supp_t15_executor.py",
    ]
    src_pre = {"results/_v4_supp_t15r2_executor_r1_2026_09_28.py": "e0936a68fa82",
               "results/_v4_supp_t15r2_executor.py": "4b5b720d5cda",
               "results/_v4_supp_t15_executor_r1_2026_09_27.py": "6d22444c65af",
               "results/_v4_supp_t15_executor.py": "558e635f9ba6"}
    src_post = []
    for f in srcs:
        p = ROOT / f
        a = sha12(p) if p.exists() else None
        src_post.append({"path": f, "pre_sha12": src_pre[f], "post_sha12": a,
                         "untouched": a == src_pre[f]})

    rep = {
        "schema": "v4_cpatomic_pycache_post/1", "date": "2026-09-28",
        "pre_registration_ref": PRE.relative_to(ROOT).as_posix(),
        "pycache_dirs_targeted": len(dirs_post),
        "pycache_dirs_all_gone": all(d["gone"] for d in dirs_post),
        "pyc_files_before": pre["pyc_total_files"],
        "pyc_bytes_before": pre["pyc_total_bytes"],
        "pycache_dirs_post_repo_wide_scan": found,
        "dirs_post": dirs_post,
        "frozen_n": len(frozen_post),
        "frozen_pass": sum(1 for r in frozen_post if r["match"]),
        "frozen_fail": [r["path"] for r in frozen_post if not r["match"]],
        "frozen_rows": frozen_post,
        "frozen_touched_n": sum(1 for r in frozen_post if not r["match"]),
        "conservation_adjacent": cons_post,
        "source_files_untouched": src_post,
    }
    OUT.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"目标 8 目录全清 = {rep['pycache_dirs_all_gone']}")
    for d in dirs_post:
        print(f"  {'GONE ' if d['gone'] else 'STILL'} {d['rel']:52s} "
              f"files {d['files_before']}->{d['files_after']}  bytes_before={d['bytes_before']}")
    print(f"清后全仓 __pycache__ 残留 = {found if found else 'NONE'}")
    print(f"18 frozen: {rep['frozen_pass']}/{rep['frozen_n']} PASS  触动数={rep['frozen_touched_n']}"
          f"  fail={rep['frozen_fail']}")
    print(f"conservation.py 清前 {cons_post['pre_sha12']}/{cons_post['pre_bytes']}B -> "
          f"清后 {cons_post['post_sha12']}/{cons_post['post_bytes']}B  "
          f"untouched={cons_post['pre_sha12'] == cons_post['post_sha12']}")
    for s in src_post:
        print(f"  源件 0 触动 {'OK ' if s['untouched'] else 'FAIL'} {s['path']}  {s['post_sha12']}")
    print(f"OUT -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
