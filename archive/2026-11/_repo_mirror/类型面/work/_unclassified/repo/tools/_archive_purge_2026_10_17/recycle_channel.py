# -*- coding: utf-8 -*-
"""Recycle-bin recoverable deletion channel (ONLY allowed channel for this purge).

SHFileOperationW + FOF_ALLOWUNDO is the sole permitted deletion channel.
Ref: any other mechanism (rm / shutil.rmtree / Remove-Item) is forbidden.
"""
import ctypes
import os
import struct
from ctypes import wintypes

FO_DELETE = 0x0003
FOF_SILENT = 0x0004
FOF_NOCONFIRMATION = 0x0010
FOF_NOERRORUI = 0x0400
FOF_NOCONFIRMMKDIR = 0x0200
FOF_ALLOWUNDO = 0x0040
FOF_WANTNUKEWARNING = 0x4000


class SHFILEOPSTRUCTW(ctypes.Structure):
    _fields_ = [
        ("hwnd", wintypes.HWND),
        ("wFunc", wintypes.UINT),
        ("pFrom", wintypes.LPCWSTR),
        ("pTo", wintypes.LPCWSTR),
        ("fFlags", ctypes.c_uint16),
        ("fAnyOperationsAborted", wintypes.BOOL),
        ("hNameMappings", ctypes.c_void_p),
        ("lpszProgressTitle", wintypes.LPCWSTR),
    ]


def _shell32():
    return ctypes.WinDLL("shell32", use_last_error=True)


def recycle_delete(path, expect_kind="file"):
    """Send ONE path to the recycle bin. Returns dict with rc/aborted."""
    flags = (FOF_ALLOWUNDO | FOF_NOCONFIRMATION | FOF_NOERRORUI | FOF_SILENT)
    if expect_kind == "dir":
        flags |= FOF_NOCONFIRMMKDIR
    op = SHFILEOPSTRUCTW()
    op.hwnd = None
    op.wFunc = FO_DELETE
    op.pFrom = ctypes.c_wchar_p(path + "\x00\x00")
    op.pTo = None
    op.fFlags = flags
    op.fAnyOperationsAborted = False
    op.hNameMappings = None
    op.lpszProgressTitle = None
    rc = _shell32().SHFileOperationW(ctypes.byref(op))
    return {"rc": int(rc), "aborted": bool(op.fAnyOperationsAborted), "flags": int(flags)}


def bin_dir(drive="〔本地路径已脱敏〕"):
    return os.path.join(drive, "$Recycle.Bin")


def sid_bin_dir(sid, drive="〔本地路径已脱敏〕"):
    return os.path.join(bin_dir(drive), sid)


def list_bin(sid, drive="〔本地路径已脱敏〕"):
    d = sid_bin_dir(sid, drive)
    out = {}
    try:
        for n in os.listdir(d):
            p = os.path.join(d, n)
            try:
                out[n] = (os.path.getsize(p), os.path.getmtime(p))
            except OSError:
                pass
    except OSError:
        return {}
    return out


def decode_i(data):
    """Decode a $I record. Report which byte offset the path actually starts at."""
    res = {"len": len(data)}
    if len(data) < 24:
        res["error"] = "too_short"
        return res
    res["version"] = struct.unpack_from("<Q", data, 0)[0]
    res["orig_size"] = struct.unpack_from("<Q", data, 8)[0]
    res["delete_filetime"] = struct.unpack_from("<Q", data, 16)[0]
    nchars = None
    if len(data) >= 28:
        nchars = struct.unpack_from("<I", data, 24)[0]
        res["declared_nchars"] = nchars
    for off in (28, 26, 24, 20):
        if off + 2 > len(data):
            continue
        cand_n = None
        if nchars is not None:
            cand_n = nchars
        else:
            # derive from remaining length
            cand_n = (len(data) - off) // 2 - 1
        if cand_n is None or cand_n <= 0:
            continue
        need = (cand_n + 1) * 2
        if off + need > len(data):
            need = len(data) - off
        raw = data[off:off + need]
        try:
            s = raw.decode("utf-16-le", errors="strict")
        except UnicodeDecodeError:
            continue
        s2 = s.split("\x00")[0]
        if s2 and (":" in s2 or "\\" in s2):
            res["path_offset"] = off
            res["path"] = s2
            res["has_null_terminator"] = raw.endswith(b"\x00\x00")
            return res
    res["error"] = "undecodable"
    return res
