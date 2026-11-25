# -*- coding: utf-8 -*-
"""[V4 checkpoint 尾 3 件修订棒 | 2026-09-29] 别名表引用面扫描 (可复算)

口径 (沿 3bc852e0d48b §6 先例): 全仓检索 3 件源件名; `.tmp/` 脚手架单列不计入生效面;
`__pycache__` / `.pyc` 不计; 本棒 3 件新出件单列 (其件内提及源件名 = 来源链登记, 非旧引用面)。
"""
import json
import os
from pathlib import Path

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


REPO = Path(r_dep_path(""))

TARGETS = {
    "A": ("_v4_supp_t15_executor.py", "results/_v4_supp_t15_executor_r0_atomic_2026_09_29.py"),
    "B": ("_v4_supp_t15r2_executor.py", "results/_v4_supp_t15r2_executor_r0_atomic_2026_09_29.py"),
    "C": ("l14_runner_v2.py", "results/_archive_2026_09_24/l14_runner_v2_r1_atomic_2026_09_29.py"),
}
NEW_FILES = {v[1] for v in TARGETS.values()}
SCAN_EXT = {".md", ".json", ".py", ".txt", ".jsonl"}
SKIP_DIR_PARTS = {"__pycache__", ".git", ".trae", "node_modules"}

out = {"scanned_at_label": "2026-09-29", "targets": {}}
for key, (needle, newf) in TARGETS.items():
    files_main, lines_main, files_tmp = [], 0, {}
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in SKIP_DIR_PARTS]
        for f in files:
            p = Path(root, f)
            rel = str(p.relative_to(REPO)).replace("\\", "/")
            if rel.endswith(".pyc") or p.suffix.lower() not in SCAN_EXT:
                continue
            if rel in NEW_FILES:
                continue
            try:
                t = p.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            n = t.count(needle)
            if not n:
                continue
            if rel.startswith(".tmp/"):
                files_tmp[rel] = n
            else:
                files_main.append((rel, n))
                lines_main += n
    out["targets"][key] = {
        "needle": needle,
        "new_file": newf,
        "main_files": len(files_main),
        "main_lines": lines_main,
        "main_detail": sorted(files_main, key=lambda x: (-x[1], x[0])),
        "tmp_scaffold_files": len(files_tmp),
        "tmp_scaffold_lines": sum(files_tmp.values()),
    }
    print(f"[{key}] {needle}")
    print(f"  非 .tmp 引用面: {len(files_main)} 件 / {lines_main} 行")
    for rel, n in sorted(files_main, key=lambda x: (-x[1], x[0])):
        print(f"    {n:>3}  {rel}")
    print(f"  .tmp 脚手架 (不计入生效面): {len(files_tmp)} 件 / {sum(files_tmp.values())} 行")

(REPO / ".tmp" / "_tail3_atomic_refs_2026_09_29.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n")
