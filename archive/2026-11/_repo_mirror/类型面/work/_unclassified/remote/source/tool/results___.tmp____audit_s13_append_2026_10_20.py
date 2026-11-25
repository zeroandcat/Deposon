#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
追加器 v13 · 子棒版备忘录 §13 追加 · 2026-10-20
纪律：append-only（只追加于文件末尾·⛔0 回改既有字节）；UTF-8 无 BOM·纯 LF。
落盘前复检停手闸；落盘后独立回读＋字节级自报。
"""
import hashlib, io, os, sys, datetime

TARGET = r"_repo_mirror/work/note/_root_session_history_memo_2026_10_14.md"
BODY = r"〔幽灵引用·原件已缺席·未上传:_s13_body_2026_10_20.md〕"

EXPECT_SHA12 = "ABD08EC2150D"
EXPECT_BYTES = 260084
EXPECT_LF = 2082

def sha256(b):
    return hashlib.sha256(b).hexdigest()

def stats(b):
    return {
        "bytes": len(b),
        "sha12": sha256(b)[:12].upper(),
        "sha256": sha256(b),
        "cr": b.count(b"\x0d"),
        "bom": b[:3] == b"\xef\xbb\xbf",
        "lf": b.count(b"\x0a"),
        "last": b[-1],
        "fffd": b.decode("utf-8", errors="replace").count("\ufffd"),
    }

def main():
    # ---- 停手闸 ----
    if not os.path.exists(TARGET):
        print("GATE=FAIL target-missing")
        sys.exit(2)
    pre = open(TARGET, "rb").read()
    s = stats(pre)
    ok = (s["sha12"] == EXPECT_SHA12 and s["bytes"] == EXPECT_BYTES
          and s["lf"] == EXPECT_LF and s["cr"] == 0 and not s["bom"] and s["last"] == 0x0A)
    print("PRE_SHA12=%s PRE_BYTES=%d PRE_LF=%d PRE_CR=%d PRE_BOM=%s PRE_LAST=0x%02X GATE=%s"
          % (s["sha12"], s["bytes"], s["lf"], s["cr"], s["bom"], s["last"], "PASS" if ok else "FAIL"))
    if not ok:
        sys.exit(3)

    # ---- 正文稿（UTF-8 无 BOM·纯 LF）----
    body = open(BODY, "rb").read()
    if body[:3] == b"\xef\xbb\xbf":
        body = body[3:]
    body = body.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if not body.endswith(b"\n"):
        body += b"\n"
    bs = stats(body)
    print("BODY_BYTES=%d BODY_CR=%d BODY_BOM=%s BODY_LF=%d" % (bs["bytes"], bs["cr"], bs["bom"], bs["lf"]))
    if bs["cr"] != 0 or bs["bom"]:
        print("BODY_FORMAT=FAIL")
        sys.exit(4)

    # ---- append-only 追加（'ab' 模式：⛔0 截断·⛔0 回写既有字节）----
    with open(TARGET, "ab") as f:
        f.write(body)
        f.flush()
        os.fsync(f.fileno())

    # ---- 落盘后独立回读 ----
    post = open(TARGET, "rb").read()
    ps = stats(post)
    prefix = post[:EXPECT_BYTES]
    psha = sha256(prefix)
    prefix_ok = (psha == s["sha256"])
    print("POST_SHA12=%s POST_BYTES=%d POST_LF=%d POST_CR=%d POST_BOM=%s POST_FFFd=%d POST_LAST=0x%02X"
          % (ps["sha12"], ps["bytes"], ps["lf"], ps["cr"], ps["bom"], ps["fffd"], ps["last"]))
    print("APPEND_DELTA_BYTES=%d" % (ps["bytes"] - s["bytes"]))
    print("PREFIX_UNCHANGED=%s (prefix_sha256=%s)" % (prefix_ok, psha))
    print("POST_SHA256=%s" % ps["sha256"])
    if not prefix_ok:
        print("PREFIX_CHECK=FAIL")
        sys.exit(5)

    # ---- 长名式复测在盘 ----
    hits = []
    REPO = r"_repo_mirror"
    for root, dirs, files in os.walk(REPO):
        parts = os.path.relpath(root, REPO).split(os.sep)
        if parts and parts[0] in ("deposon-sub", ".git", "node_modules"):
            dirs[:] = []
            continue
        for fn in files:
            if fn == "_root_session_history_memo_2026_10_14.md":
                hits.append(os.path.join(root, fn))
    print("LONGNAME_EXACT=%d" % len(hits))
    for h in hits:
        print("  " + h)
    print("DONE_T=%s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()
