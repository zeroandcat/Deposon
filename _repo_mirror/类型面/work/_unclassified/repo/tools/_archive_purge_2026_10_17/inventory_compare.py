# -*- coding: utf-8 -*-
"""ARCHIVE-WHITELIST-PURGE / step 1: dual-face inventory + SHA-12 comparison.

Target (to purge):  〔归档件引用·未上传:whitelist_backup_2026_10_17〕
Backup (DO NOT TOUCH): 〔幽灵引用·未上传:whitelist_backup_2026_10_17〕
"""
import hashlib
import io
import json
import os
import sys

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


TARGET = r"〔归档件引用·未上传:whitelist_backup_2026_10_17〕"
BACKUP = r_dep_path(".tmp/whitelist_backup_2026_10_17")
OUT = r_dep_path("tools/_archive_purge_2026_10_17/inventory_compare.json")


def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while True:
            b = f.read(1024 * 1024)
            if not b:
                break
            h.update(b)
    return h.hexdigest()[:12]


def walk(root):
    files = {}
    dirs = set()
    errors = []
    for dirpath, dirnames, filenames in os.walk(root):
        rel_d = os.path.relpath(dirpath, root)
        rel_d = "" if rel_d == "." else rel_d
        dirs.add(rel_d)
        for n in filenames:
            rel = os.path.join(rel_d, n) if rel_d else n
            full = os.path.join(dirpath, n)
            try:
                files[rel] = (os.path.getsize(full), sha12(full))
            except Exception as exc:  # noqa: BLE001
                errors.append([rel, repr(exc)])
    return files, dirs, errors


def main():
    res = {"target": TARGET, "backup": BACKUP}
    for key, root in (("target", TARGET), ("backup", BACKUP)):
        if not os.path.isdir(root):
            res[key] = {"exists": False}
            print("[%s] MISSING: %s" % (key, root))
            continue
        files, dirs, errors = walk(root)
        res[key] = {
            "exists": True,
            "n_files": len(files),
            "n_dirs": len(dirs),
            "total_bytes": sum(v[0] for v in files.values()),
            "errors": errors,
            "files": files,
            "dirs": sorted(dirs),
        }
        print("[%s] files=%d dirs=%d bytes=%d walk_errors=%d"
              % (key, len(files), len(dirs), sum(v[0] for v in files.values()), len(errors)))

    t, b = res.get("target", {}), res.get("backup", {})
    if not t.get("exists") or not b.get("exists"):
        res["compare"] = {"verdict": "STOP_MISSING_FACE"}
        print("VERDICT: STOP_MISSING_FACE")
    else:
        tf, bf = t["files"], b["files"]
        only_t = sorted(set(tf) - set(bf))
        only_b = sorted(set(bf) - set(tf))
        common = sorted(set(tf) & set(bf))
        mismatch = [
            [k, tf[k][0], tf[k][1], bf[k][0], bf[k][1]]
            for k in common if tf[k][1] != bf[k][1]
        ]
        size_mismatch = [[k, tf[k][0], bf[k][0]] for k in common if tf[k][0] != bf[k][0]]
        td, bd = set(t["dirs"]), set(b["dirs"])
        res["compare"] = {
            "n_common": len(common),
            "only_in_target": only_t,
            "only_in_backup": only_b,
            "sha12_mismatch": mismatch,
            "size_mismatch": size_mismatch,
            "dirs_only_in_target": sorted(td - bd),
            "dirs_only_in_backup": sorted(bd - td),
            "target_walk_errors": t["errors"],
            "backup_walk_errors": b["errors"],
            "verdict": (
                "IDENTICAL_699" if (
                    len(tf) == 699 and len(bf) == 699 and not only_t and not only_b
                    and not mismatch and not size_mismatch and not t["errors"] and not b["errors"]
                    and td == bd
                ) else "NOT_IDENTICAL_OR_OTHER"
            ),
        }
        print("VERDICT:", res["compare"]["verdict"],
              "| only_t=%d only_b=%d sha_mismatch=%d size_mismatch=%d dirs_equal=%s"
              % (len(only_t), len(only_b), len(mismatch), len(size_mismatch), td == bd))
        for m in mismatch[:10]:
            print("  SHA MISMATCH:", m)
        for m in size_mismatch[:10]:
            print("  SIZE MISMATCH:", m)
        for m in only_t[:10]:
            print("  ONLY TARGET:", m)
        for m in only_b[:10]:
            print("  ONLY BACKUP:", m)

    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
    print("WROTE", OUT, os.path.getsize(OUT), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
