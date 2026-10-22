# -*- coding: utf-8 -*-
"""Step 3 - bulk purge of the archive whitelist copy, per-item registration.

Channel: SHFileOperationW + FOF_ALLOWUNDO ONLY (sole permitted channel).
Per file: delete -> verify source gone -> new $I record -> decode -> paired $R ->
payload SHA-12 re-verified. Then the sub-dir and the root dir (same channel).
"""
import hashlib
import io
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recycle_channel as rc

TARGET = r"〔归档件引用·未上传:whitelist_backup_2026_10_17〕"
BACKUP = r"〔目录引用·未上传:whitelist_backup_2026_10_17〕"
SID = r"S-1-5-21-1515631758-409240343-2904948024-500"
INV = r"_repo_mirror/readout/final/inventory_compare.json"
OUT = r"_repo_mirror/readout/final/step3_bulk_result.json"


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
    out = []
    errs = []
    for dirpath, dirnames, filenames in os.walk(root):
        for n in filenames:
            full = os.path.join(dirpath, n)
            rel = os.path.relpath(full, root)
            out.append(rel)
    return out, errs


def bin_names():
    try:
        return set(os.listdir(rc.sid_bin_dir(SID)))
    except OSError:
        return set()


def main():
    inv = json.load(io.open(INV, encoding="utf-8"))
    tfiles = inv["target"]["files"]
    tlow = TARGET.lower().rstrip("\\") + "\\"

    rels, _ = walk(TARGET)
    rels.sort()
    rows = []
    kd = []
    t0 = time.time()

    for idx, rel in enumerate(rels, 1):
        src = os.path.join(TARGET, rel)
        if not src.lower().startswith(tlow):
            kd.append({"item": rel, "reason": "path_escaped_target"})
            continue
        exp_size, exp_sha = tfiles.get(rel, (None, None))
        before = bin_names()
        r = rc.recycle_delete(src, "file")
        after = bin_names()
        new = sorted(after - before)
        i_new = [n for n in new if n[:2].upper() == "$I"]
        rr_new = [n for n in new if n[:2].upper() == "$R"]
        row = {
            "n": idx, "rel": rel, "size": exp_size, "sha12_exp": exp_sha,
            "rc": r["rc"], "aborted": r["aborted"],
            "source_gone": not os.path.exists(src),
            "new_entries": new, "i_name": i_new[0] if i_new else None,
            "r_name": rr_new[0] if rr_new else None,
        }
        fails = []
        if r["rc"] != 0:
            fails.append("rc=%s" % r["rc"])
        if r["aborted"]:
            fails.append("aborted")
        if not row["source_gone"]:
            fails.append("source_still_present")
        if len(i_new) != 1 or len(rr_new) != 1:
            fails.append("I/R_record_count_%s_%s" % (len(i_new), len(rr_new)))
        if i_new and rr_new:
            binp = rc.sid_bin_dir(SID)
            if i_new[0][2:].upper() != rr_new[0][2:].upper():
                fails.append("I_R_not_paired")
            data = io.open(os.path.join(binp, i_new[0]), "rb").read()
            dec = rc.decode_i(data)
            row["i_path_offset"] = dec.get("path_offset")
            row["i_path"] = dec.get("path")
            row["i_orig_size"] = dec.get("orig_size")
            row["i_declared_nchars"] = dec.get("declared_nchars")
            dp = (dec.get("path") or "").replace("/", "\\").rstrip("\\").lower()
            if not dp.endswith(rel.replace("/", "\\").lower()):
                fails.append("I_path_mismatch")
            if dec.get("orig_size") != exp_size:
                fails.append("I_orig_size_%s_vs_%s" % (dec.get("orig_size"), exp_size))
            rp = os.path.join(binp, rr_new[0])
            if os.path.isfile(rp):
                got = sha12(rp)
                row["r_payload_sha12"] = got
                if got != exp_sha:
                    fails.append("R_sha_mismatch_%s_vs_%s" % (got, exp_sha))
            else:
                fails.append("R_payload_absent")
        row["ok"] = not fails
        if fails:
            row["fails"] = fails
            kd.append({"item": rel, "reason": ";".join(fails)})
        rows.append(row)
        if idx % 50 == 0:
            print("  ...%d/%d files (%.1fs)" % (idx, len(rels), time.time() - t0))

    print("FILES DONE: %d rows, failures=%d" % (len(rows), len(kd)))

    # directories: deepest-first, same channel
    drows = []
    subdirs = []
    for dirpath, dirnames, filenames in os.walk(TARGET, topdown=False):
        for d in dirnames:
            subdirs.append(os.path.join(dirpath, d))
    subdirs.append(TARGET)
    for dp in subdirs:
        before = bin_names()
        r = rc.recycle_delete(dp, "dir")
        after = bin_names()
        new = sorted(after - before)
        i_new = [n for n in new if n[:2].upper() == "$I"]
        rr_new = [n for n in new if n[:2].upper() == "$R"]
        row = {"abs": dp, "rc": r["rc"], "aborted": r["aborted"],
               "gone": not os.path.exists(dp), "new_entries": new,
               "i_name": i_new[0] if i_new else None, "r_name": rr_new[0] if rr_new else None}
        fails = []
        if r["rc"] != 0:
            fails.append("rc=%s" % r["rc"])
        if not row["gone"]:
            fails.append("dir_still_present")
        if len(i_new) != 1 or len(rr_new) != 1:
            fails.append("I/R_record_count_%s_%s" % (len(i_new), len(rr_new)))
        if i_new:
            data = io.open(os.path.join(rc.sid_bin_dir(SID), i_new[0]), "rb").read()
            dec = rc.decode_i(data)
            row["i_path_offset"] = dec.get("path_offset")
            row["i_path"] = dec.get("path")
            row["i_len"] = len(data)
            row["i_orig_size"] = dec.get("orig_size")
            row["i_declared_nchars"] = dec.get("declared_nchars")
            dp2 = (dec.get("path") or "").replace("/", "\\").rstrip("\\").lower()
            if not dp2.endswith(dp.replace("/", "\\").rstrip("\\").lower()):
                fails.append("I_path_mismatch")
        row["ok"] = not fails
        if fails:
            row["fails"] = fails
            kd.append({"item": dp, "reason": ";".join(fails)})
        drows.append(row)
        print("DIR:", dp, "->", row["i_name"], row["r_name"], "offset", row.get("i_path_offset"), "ok", row["ok"])

    # backup face must be untouched
    bfiles, _ = walk(BACKUP)
    inv_sha = set(v[1] for v in inv["backup"]["files"].values())
    now_sha = set()
    brels = sorted(bfiles)
    for rel in brels:
        now_sha.add(sha12(os.path.join(BACKUP, rel)))
    backup_intact = (len(brels) == 699 and now_sha == inv_sha)

    res = {
        "target": TARGET, "backup": BACKUP, "sid": SID,
        "n_files_attempted": len(rows), "n_files_ok": sum(1 for x in rows if x["ok"]),
        "dir_rows": drows, "kd": kd,
        "target_exists_after": os.path.exists(TARGET),
        "backup_files_after": len(brels),
        "backup_sha_set_equal": (now_sha == inv_sha),
        "backup_intact": backup_intact,
        "elapsed_s": round(time.time() - t0, 1),
        "rows": rows,
    }
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True))
    print("FILES ok=%d/%d  KD=%d  target_exists_after=%s  backup_intact=%s (%d files)"
          % (res["n_files_ok"], res["n_files_attempted"], len(kd),
             res["target_exists_after"], backup_intact, res["backup_files_after"]))
    print("WROTE", OUT, os.path.getsize(OUT), "bytes")
    return 0 if (not kd and not res["target_exists_after"] and backup_intact) else 1


if __name__ == "__main__":
    sys.exit(main())
