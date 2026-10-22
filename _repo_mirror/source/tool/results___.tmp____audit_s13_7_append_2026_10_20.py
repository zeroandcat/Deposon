#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
追加器 v13-2 · 子棒版备忘录 §13-7 勘误补记追加 · 2026-10-20
纪律：append-only；UTF-8 无 BOM·纯 LF；落盘前复检闸；落盘后独立回读自证。
"""
import hashlib, io, os, sys, datetime

TARGET = r"_repo_mirror/work/note/_root_session_history_memo_2026_10_14.md"
BODY = r"〔幽灵引用·原件已缺席·未上传:_s13_7_body_2026_10_20.md〕"

EXPECT_SHA12 = "47EBD4E89592"
EXPECT_BYTES = 311626
EXPECT_LF = 2423

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def stats(b):
    return {"bytes": len(b), "sha12": sha256(b)[:12].upper(), "sha256": sha256(b),
            "cr": b.count(b"\x0d"), "bom": b[:3] == b"\xef\xbb\xbf", "lf": b.count(b"\x0a"),
            "last": b[-1], "fffd": b.decode("utf-8", errors="replace").count("\ufffd")}

def main():
    pre = open(TARGET, "rb").read()
    s = stats(pre)
    ok = (s["sha12"] == EXPECT_SHA12 and s["bytes"] == EXPECT_BYTES
          and s["lf"] == EXPECT_LF and s["cr"] == 0 and not s["bom"] and s["last"] == 0x0A)
    print("PRE_SHA12=%s PRE_BYTES=%d PRE_LF=%d GATE=%s" % (s["sha12"], s["bytes"], s["lf"], "PASS" if ok else "FAIL"))
    if not ok:
        sys.exit(3)

    body = open(BODY, "rb").read()
    if body[:3] == b"\xef\xbb\xbf":
        body = body[3:]
    body = body.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if not body.endswith(b"\n"):
        body += b"\n"
    bs = stats(body)
    print("BODY_BYTES=%d BODY_CR=%d BODY_BOM=%s" % (bs["bytes"], bs["cr"], bs["bom"]))
    if bs["cr"] != 0 or bs["bom"]:
        sys.exit(4)

    with open(TARGET, "ab") as f:
        f.write(body)
        f.flush()
        os.fsync(f.fileno())

    post = open(TARGET, "rb").read()
    ps = stats(post)
    prefix = post[:EXPECT_BYTES]
    prefix_ok = (sha256(prefix) == s["sha256"])
    print("POST_SHA12=%s POST_BYTES=%d POST_LF=%d POST_CR=%d POST_BOM=%s POST_FFFd=%d POST_LAST=0x%02X"
          % (ps["sha12"], ps["bytes"], ps["lf"], ps["cr"], ps["bom"], ps["fffd"], ps["last"]))
    print("APPEND_DELTA_BYTES=%d" % (ps["bytes"] - s["bytes"]))
    print("PREFIX_UNCHANGED=%s (prefix_sha256=%s)" % (prefix_ok, sha256(prefix)))
    print("POST_SHA256=%s" % ps["sha256"])
    if not prefix_ok:
        sys.exit(5)
    print("DONE_T=%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
