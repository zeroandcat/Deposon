# -*- coding: utf-8 -*-
"""Step 2 - SMALL SAMPLE channel verification (hard prerequisite for bulk purge).

Verifies on ONE file: $I/$R pair creation, path decoding (offset 28 for files),
and payload SHA-12 re-verification against the inventory taken before deletion.
"""
import hashlib
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import recycle_channel as rc

TARGET = r"〔归档件引用·未上传:whitelist_backup_2026_10_17〕"
SID = r"S-1-5-21-1515631758-409240343-2904948024-500"
INV = r"_repo_mirror/readout/final/inventory_compare.json"
OUT = r"_repo_mirror/readout/final/step2_sample_verify.json"


def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        while True:
            b = f.read(1024 * 1024)
            if not b:
                break
            h.update(b)
    return h.hexdigest()[:12]


def bin_base(name):
    """$I<base> / $R<base> -> <base>; pairing key is the shared base name."""
    return name[2:] if name[:2].upper() in ("$I", "$R") else name


def main():
    inv = json.load(io.open(INV, encoding="utf-8"))
    tfiles = inv["target"]["files"]
    cands = [(v[0], k, v[1]) for k, v in tfiles.items() if v[0] > 0]
    cands.sort()
    if not cands:
        print("STOP: no non-empty file to sample")
        return 2
    size, rel, sha = cands[0]
    src = os.path.join(TARGET, rel)
    print("SAMPLE: rel=%s size=%d sha12=%s" % (rel, size, sha))
    print("SAMPLE src exists:", os.path.isfile(src))

    before = rc.list_bin(SID)
    print("bin entries before:", len(before))

    r = rc.recycle_delete(src, "file")
    print("SHFileOperationW result:", r)
    gone = not os.path.exists(src)
    print("source gone after call:", gone)

    after = rc.list_bin(SID)
    new = sorted(set(after) - set(before))
    print("new bin entries:", new)

    report = {
        "sample_rel": rel, "sample_abs": src, "sample_size": size,
        "sample_sha12_expected": sha, "op": r, "source_gone": gone,
        "bin_entries_before": len(before), "bin_entries_after": len(after),
        "new_bin_entries": new, "checks": [], "ok": False,
    }

    def chk(name, cond, detail=""):
        report["checks"].append({"check": name, "pass": bool(cond), "detail": str(detail)})
        print("  [%s] %s %s" % ("PASS" if cond else "FAIL", name, detail))
        return cond

    chk("op_rc_zero", r["rc"] == 0, "rc=%s" % r["rc"])
    chk("not_aborted", not r["aborted"], "aborted=%s" % r["aborted"])
    chk("source_removed", gone, src)

    i_files = [n for n in new if n.upper().startswith("$I")]
    r_files = [n for n in new if n.upper().startswith("$R")]
    chk("one_new_I_record", len(i_files) == 1, i_files)
    chk("one_new_R_record", len(r_files) == 1, r_files)

    if i_files and r_files:
        binp = rc.sid_bin_dir(SID)
        ipath = os.path.join(binp, i_files[0])
        rpath = os.path.join(binp, r_files[0])
        chk("I_R_stem_paired",
            bin_base(i_files[0]) == bin_base(r_files[0]),
            "%s <-> %s" % (i_files[0], r_files[0]))
        data = io.open(ipath, "rb").read()
        dec = rc.decode_i(data)
        report["i_decode"] = dec
        report["i_name"] = i_files[0]
        report["r_name"] = r_files[0]
        report["i_len"] = len(data)
        chk("I_path_offset_is_28", dec.get("path_offset") == 28, dec.get("path_offset"))
        dec_path = (dec.get("path") or "").replace("/", "\\").rstrip("\\").lower()
        exp_tail = rel.replace("/", "\\").lower()
        chk("I_decoded_path_matches_source",
            dec_path.endswith(exp_tail) and dec_path.startswith("d:"),
            "decoded=%r" % dec.get("path"))
        chk("I_orig_size_matches", dec.get("orig_size") == size,
            "%s vs %s" % (dec.get("orig_size"), size))
        if os.path.isfile(rpath):
            got = sha12(rpath)
            report["R_payload_sha12"] = got
            chk("R_payload_sha12_matches_inventory", got == sha, "%s vs %s" % (got, sha))
        else:
            chk("R_payload_present", False, rpath)

    report["ok"] = all(c["pass"] for c in report["checks"])
    report["verdict"] = "CHANNEL_VERIFIED" if report["ok"] else "CHANNEL_FAILED_STOP"
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(report, ensure_ascii=False, indent=1, sort_keys=True))
    print("VERDICT:", report["verdict"])
    print("WROTE", OUT, os.path.getsize(OUT), "bytes")
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
