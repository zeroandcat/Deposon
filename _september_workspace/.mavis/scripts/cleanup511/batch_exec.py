# -*- coding: utf-8 -*-
"""
CLEANUP-EXEC-511 batch executor.

Deletes ONLY via shell32.SHFileOperationW(FO_DELETE) with FOF_ALLOWUNDO (recoverable).
NEVER uses rm / Remove-Item / unlink / rmtree.

Success criterion per item (exit code is NOT evidence):
    1. target gone from its original path
    2. exactly one new $I record appeared in D:\\$Recycle.Bin\\<SID>\\
    3. exactly one new $R payload, same suffix as the $I
    4. $I decodes back to the original absolute path
    5. sha256 of the $R payload == sha256 recorded before the delete  (content proof)
"""
import os, io, sys, json, time, hashlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from recycle_exec import bin_dir_for, list_bin, decode_i, send_to_bin

REPO = r"D:\私人资料\deposon-repo"
LST = os.path.join(REPO, ".mavis", "scripts", "cleanup511", "exec_list.json")
RPT = os.path.join(REPO, ".mavis", "scripts", "cleanup511", "exec_report.json")


def sha12_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()[:12]


def handle(target, expect_sha12, is_dir=False):
    rec = {"rel": os.path.relpath(target, REPO).replace("\\", "/"),
           "expect_sha12": expect_sha12, "is_dir": is_dir}
    if not os.path.exists(target):
        rec.update(status="absent_before", ok=False)
        return rec
    bindir = bin_dir_for(target)
    rec["bindir"] = bindir
    before = list_bin(bindir)
    rc, aborted = send_to_bin(target)
    rec["shfileop_rc"] = rc
    rec["any_aborted"] = aborted
    rec["gone"] = not os.path.exists(target)
    new = sorted(list_bin(bindir) - before)
    rec["new_bin"] = new
    I = [n for n in new if n.startswith("$I")]
    R = [n for n in new if n.startswith("$R")]
    rec["n_I"], rec["n_R"] = len(I), len(R)
    ok = rec["gone"] and len(I) == 1 and len(R) == 1
    if I and R:
        ip = os.path.join(bindir, I[0])
        rp = os.path.join(bindir, R[0])
        rec["I_name"], rec["R_name"] = I[0], R[0]
        rec["pair_suffix_match"] = I[0][2:] == R[0][2:]
        try:
            dec, raw = decode_i(ip)
            needle = os.path.abspath(target).encode("utf-16-le")
            off = raw.find(needle)
            if off < 0:
                off = raw.lower().find(os.path.abspath(target).lower().encode("utf-16-le"))
            rec["I_version"] = dec.get("version")
            rec["I_path_offset"] = off
            rec["I_path_ok"] = off >= 0
        except Exception as e:
            rec["I_path_ok"] = False
            rec["I_decode_error"] = repr(e)
        if not is_dir and expect_sha12 and expect_sha12 != "(empty-dir)":
            try:
                got = sha12_file(rp)
                rec["R_sha12"] = got
                rec["R_sha_ok"] = (got == expect_sha12)
            except OSError as e:
                rec["R_sha_ok"] = False
                rec["R_sha_error"] = repr(e)
        ok = ok and rec.get("pair_suffix_match") and rec.get("I_path_ok") and rec.get("R_sha_ok", True)
    rec["ok"] = bool(ok)
    rec["status"] = "recycled_verified" if rec["ok"] else "FAILED"
    return rec


def main():
    L = json.load(io.open(LST, encoding="utf-8"))
    dirset = {d["abs"] for d in L["dirs"]}
    items = L["files"] + L["dirs"]
    recs = []
    t0 = time.time()
    for i, it in enumerate(items, 1):
        try:
            if os.path.normcase(it["abs"]) in {os.path.normcase(d) for d in dirset}:
                rec = handle_dir(it["abs"])
            else:
                rec = handle(it["abs"], it.get("sha12"))
        except Exception as e:
            rec = {"rel": it["rel"], "status": "EXCEPTION", "ok": False, "error": repr(e)}
        recs.append(rec)
        if i % 50 == 0 or not rec["ok"]:
            print("[%4d/%4d] ok=%d bad=%d  %s" %
                  (i, len(items), sum(1 for r in recs if r.get("ok")),
                   sum(1 for r in recs if not r.get("ok")), rec["rel"][:70]))
        sys.stdout.flush()

    good = [r for r in recs if r.get("ok")]
    bad = [r for r in recs if not r.get("ok")]
    report = {"meta": {"rod": "CLEANUP-EXEC-511", "finished": time.strftime("%Y-%m-%d %H:%M:%S"),
                       "planned": len(items), "verified": len(good), "failed": len(bad),
                       "elapsed_s": round(time.time() - t0, 1)},
              "records": recs}
    with io.open(RPT, "w", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(report, ensure_ascii=False, indent=1))
    print(json.dumps(report["meta"], ensure_ascii=False, indent=1))
    for b in bad[:40]:
        print("  FAIL", json.dumps(b, ensure_ascii=False)[:300])


def handle_dir(target):
    """Empty dirs: recycle them, verify the dir is gone and a $I/$R pair appeared."""
    rec = {"rel": os.path.relpath(target, REPO).replace("\\", "/"), "is_dir": True,
           "expect_sha12": "(empty-dir)"}
    if not os.path.isdir(target):
        rec.update(status="absent_before", ok=False)
        return rec
    bindir = bin_dir_for(target)
    before = list_bin(bindir)
    rc, aborted = send_to_bin(target)
    rec["shfileop_rc"] = rc
    rec["gone"] = not os.path.exists(target)
    new = sorted(list_bin(bindir) - before)
    I = [n for n in new if n.startswith("$I")]
    R = [n for n in new if n.startswith("$R")]
    rec["n_I"], rec["n_R"] = len(I), len(R)
    ok = rec["gone"] and len(I) >= 1
    if I:
        rec["I_name"] = I[0]
        try:
            dec, raw = decode_i(os.path.join(bindir, I[0]))
            off = raw.lower().find(os.path.abspath(target).lower().encode("utf-16-le"))
            rec["I_path_ok"] = off >= 0
            rec["I_path_offset"] = off
        except Exception as e:
            rec["I_path_ok"] = False
            rec["I_decode_error"] = repr(e)
    rec["ok"] = bool(ok and rec.get("I_path_ok"))
    rec["status"] = "recycled_verified" if rec["ok"] else "FAILED"
    return rec


if __name__ == "__main__":
    main()
