# -*- coding: utf-8 -*-
"""E-48 v30 追加执行器（doc-writer agent-0032834a3e04 / 2026-09-28）
四次顺序 byte 级 append 到勘误链；每次追加后即刻复算 558,966 B prefix SHA-12。
纯追加：0 回写前缀字节。落盘后报 v30 全文件 SHA-12 / 字节 / BOM / CRLF / 末行。
"""
import hashlib
import io
import os
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

CHAIN = r"D:\私人资料\deposon-repo\docs\V3X\TRAE_V3_ASSET_ERRATUM_2026_09_23.md"
TMP = r"D:\私人资料\deposon-repo\.tmp"
PREFIX_N = 558966
PREFIX_SHA = "99c17fdbe0d9"
CHUNKS = ["_e48_c1.md", "_e48_c2.md", "_e48_c3.md", "_e48_c4.md", "_e48_c5.md"]


def sha12(b):
    return hashlib.sha256(b).hexdigest()[:12]


def report(tag):
    d = open(CHAIN, "rb").read()
    print("[%s] total_bytes=%d total_sha12=%s prefix_sha12=%s prefix_ok=%s BOM=%s CRLF=%d" % (
        tag, len(d), sha12(d).upper(), sha12(d[:PREFIX_N]).upper(),
        sha12(d[:PREFIX_N]) == PREFIX_SHA,
        "BOM" if d[:3] == b"\xef\xbb\xbf" else "noBOM", d.count(b"\r\n")))
    return d


# --- 跑前核验 ---
d0 = report("BEFORE")
assert len(d0) == PREFIX_N, "追加前字节数与派工单不符：%d" % len(d0)
assert sha12(d0) == PREFIX_SHA, "追加前 SHA-12 与派工单不符"
assert d0[-1:] == b"\n", "追加前末字节非 LF"
print("BEFORE anchor OK\n")

# --- 四次顺序 append（第五段为新末行，计入第 4 次执行） ---
for i, name in enumerate(CHUNKS, 1):
    raw = open(os.path.join(TMP, name), "rb").read()
    if raw[:3] == b"\xef\xbb\xbf":
        raw = raw[3:]
    raw = raw.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    if not raw.endswith(b"\n"):
        raw += b"\n"
    with open(CHAIN, "ab") as f:      # byte 级 append：0 回写前缀
        f.write(raw)
    step = "append#%d(%s,+%dB)" % (i, name, len(raw))
    d = report(step)
    assert sha12(d[:PREFIX_N]) == PREFIX_SHA, "前缀被改动！中止"
    print("")

# --- 落盘终核 ---
df = report("AFTER")
t = df.decode("utf-8")
L = t.split("\n")
print("")
print("final_lines =", t.count("\n") + 1)
print("head3 =", df[:3])
print("tail8 =", df[-8:])
print("E-48 mentions =", t.count("E-48"))
print("footer_present =", "v30 续" in t)
print("sections =", [s for s in ["§22.46", "§22.47", "§22.48"] if s in t])
