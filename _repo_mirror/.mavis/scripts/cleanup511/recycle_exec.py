# -*- coding: utf-8 -*-
"""
CLEANUP-EXEC-511 :: recoverable-channel executor (SHFileOperationW + FOF_ALLOWUNDO).

NEVER uses rm / Remove-Item / unlink / rmtree. The only delete primitive in this file is
shell32.SHFileOperationW(FO_DELETE) with FOF_ALLOWUNDO set, i.e. move-to-Recycle-Bin.

Success criterion (per work order) -- NOT the exit code:
    (1) target is gone from its original path        AND
    (2) a new $I<name> record exists in <drive>\\$Recycle.Bin\\<SID>\\   AND
    (3) the matching $R<name> payload exists with the same suffix          AND
    (4) $I decodes back to the ORIGINAL absolute path

usage:  python recycle_exec.py probe   <abs path> [abs path ...]
        python recycle_exec.py run     <manifest json> [--limit N] [--out report json]
"""
import os, io, sys, ctypes, json, time
from ctypes import wintypes

SHELL32 = ctypes.WinDLL("shell32", use_last_error=True)

FO_DELETE = 0x0003
FOF_SILENT          = 0x0004
FOF_NOCONFIRMATION  = 0x0010
FOF_ALLOWUNDO       = 0x0040   # <-- recoverable channel
FOF_NOERRORUI       = 0x0400
FOF_NOCONFIRMMKDIR  = 0x0200
FLAGS = FOF_SILENT | FOF_NOCONFIRMATION | FOF_ALLOWUNDO | FOF_NOERRORUI

SID = "S-1-5-21-1515631758-409240343-2904948024-500"


class SHFILEOPSTRUCTW(ctypes.Structure):
    _fields_ = [
        ("hwnd",                   wintypes.HWND),
        ("wFunc",                  wintypes.UINT),
        ("pFrom",                  wintypes.LPCWSTR),
        ("pTo",                    wintypes.LPCWSTR),
        ("fFlags",                 ctypes.c_uint16),
        ("fAnyOperationsAborted",  wintypes.BOOL),
        ("hNameMappings",          ctypes.c_void_p),
        ("lpszProgressTitle",      wintypes.LPCWSTR),
    ]


def bin_dir_for(path):
    d = os.path.splitdrive(os.path.abspath(path))[0]
    return os.path.join(d + "\\", "$Recycle.Bin", SID)


def list_bin(bindir):
    try:
        return set(os.listdir(bindir))
    except OSError:
        return set()


def decode_i(path_i):
    """Decode a $I record. Returns dict incl. the offset where the path ACTUALLY starts.
    Layout is measured, not assumed: we locate the expected UTF-16LE path ourselves and
    also report what a decode at the conventional offset 28 yields."""
    with open(path_i, "rb") as f:
        raw = f.read()
    out = {"bytes": len(raw)}
    if len(raw) >= 14:
        out["version"] = int.from_bytes(raw[0:2], "little")
        out["file_size"] = int.from_bytes(raw[2:6], "little")
        ft = int.from_bytes(raw[6:14], "little")
        if ft:
            # NB: the deletion-time field layout differs between $I versions and the
            # value can be out of gmtime range -> guard, never let it break verification.
            try:
                secs = ft / 10000000.0 - 11644473600
                out["deletion_time_utc"] = time.strftime(
                    "%Y-%m-%d %H:%M:%S", time.gmtime(secs)) if -6.2e10 < secs < 2.5e11 else None
                out["deletion_time_raw"] = ft
            except (OSError, OverflowError, ValueError):
                out["deletion_time_utc"] = None
                out["deletion_time_raw"] = ft
    txt = raw.decode("utf-16-le", "replace")
    out["decoded_at_28"] = txt[28:].split("\x00", 1)[0] if len(txt) > 28 else ""
    return out, raw


def send_to_bin(target):
    """One file per call (SHFileOperationW semantics for a single pFrom)."""
    op = SHFILEOPSTRUCTW()
    op.hwnd = None
    op.wFunc = FO_DELETE
    op.pFrom = os.path.abspath(target) + "\x00\x00"   # double-NUL terminated
    op.pTo = None
    op.fFlags = FLAGS
    op.fAnyOperationsAborted = False
    op.hNameMappings = None
    op.lpszProgressTitle = None
    rc = SHELL32.SHFileOperationW(ctypes.byref(op))
    return rc, bool(op.fAnyOperationsAborted)


def process_one(target, expect_exists=True):
    """Recoverable-delete ONE file and prove it landed in the recycle bin."""
    rec = {"path": target}
    if expect_exists:
        try:
            rec["bytes_before"] = os.path.getsize(target)
        except OSError as e:
            rec["pre_error"] = repr(e)
            rec["ok"] = False
            return rec
    bindir = bin_dir_for(target)
    rec["bindir"] = bindir
    before = list_bin(bindir)
    t0 = time.time()
    rc, aborted = send_to_bin(target)
    rec["shfileop_rc"] = rc
    rec["any_aborted"] = aborted
    rec["elapsed_s"] = round(time.time() - t0, 3)

    rec["gone_from_original"] = not os.path.exists(target)
    after = list_bin(bindir)
    new = sorted(after - before)
    rec["new_bin_entries"] = new
    i_recs = [n for n in new if n.startswith("$I")]
    r_recs = [n for n in new if n.startswith("$R")]
    rec["n_I"] = len(i_recs)
    rec["n_R"] = len(r_recs)

    ok = rec["gone_from_original"] and len(i_recs) == 1 and len(r_recs) == 1
    rec["ok"] = bool(ok)
    if i_recs and r_recs:
        ip = os.path.join(bindir, i_recs[0])
        rp = os.path.join(bindir, r_recs[0])
        dec, raw = decode_i(ip)
        # measured offset of the real path string
        want = os.path.abspath(target)
        wb = want.encode("utf-16-le")
        off = raw.find(wb)
        dec["path_found_at_offset"] = off if off >= 0 else None
        dec["expected_path"] = want
        dec["path_matches_at_found_offset"] = (off == 0 or (off >= 0 and
                                        raw[off:off + len(wb)].decode("utf-16-le", "replace") == want))
        if off >= 0:
            pre = raw[:off]
            dec["bytes_before_path"] = off
        rec["I"] = dec
        rec["I_name"] = i_recs[0]
        rec["R_name"] = r_recs[0]
        rec["pair_suffix_match"] = i_recs[0][2:] == r_recs[0][2:]
        try:
            rec["R_bytes"] = os.path.getsize(rp)
        except OSError as e:
            rec["R_bytes"] = repr(e)
        rec["ok"] = bool(rec["ok"] and rec["pair_suffix_match"]
                         and dec.get("path_found_at_offset") is not None)
    return rec


def main():
    mode = sys.argv[1]
    if mode == "probe":
        out = []
        for p in sys.argv[2:]:
            out.append(process_one(p))
            print(json.dumps(out[-1], ensure_ascii=False, indent=1))
        ok_all = all(o.get("ok") for o in out)
        print(json.dumps({"probe_all_ok": ok_all, "n": len(out)}, ensure_ascii=False))
        sys.exit(0 if ok_all else 3)
    elif mode == "run":
        raise SystemExit("batch mode not used in this step; see register")
    else:
        raise SystemExit("usage: probe <path>...")


if __name__ == "__main__":
    main()
