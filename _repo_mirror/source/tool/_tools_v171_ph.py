# -*- coding: utf-8 -*-
"""将分片暂存稿中之逐字照录 fenced 块内容替换为占位符（由落盘器程序化抽取）。
纪律：仅改本棒自身所出之暂存稿；不改任何既有件。
"""
import io
import os

TMP = r"〔目录引用·未上传:.tmp〕"

# (文件名, fenced 块序号[1-based, 仅内容行], 占位符)
JOBS = [
    ("_v171_body_p1.md", 1, "@@BLK_S1_0@@"),
    ("_v171_body_p1.md", 2, "@@BLK_S1_0b@@"),
    ("_v171_body_p1.md", 3, "@@BLK_S3_1@@"),
    ("_v171_body_p1.md", 4, "@@BLK_S3_2@@"),
    ("_v171_body_p1.md", 5, "@@BLK_S3_3@@"),
    ("_v171_body_p1.md", 6, "@@BLK_S3_4@@"),
    ("_v171_body_p1.md", 7, "@@BLK_S3_5@@"),
    ("_v171_body_p3.md", 1, "@@BLK_S4_1@@"),
]

log = []
for fname, seq, ph in JOBS:
    p = os.path.join(TMP, fname)
    ls = io.open(p, "r", encoding="utf-8", newline="").read().split("\n")
    # 找第 seq 个 fenced 块
    opens = []
    infence = False
    cur = None
    blocks = []
    for i, l in enumerate(ls):
        if l.startswith("```"):
            if not infence:
                cur = {"open": i, "close": None, "content": []}
                infence = True
            else:
                cur["close"] = i
                blocks.append(cur)
                cur = None
                infence = False
        elif infence:
            cur["content"].append(i)
    b = blocks[seq - 1]
    log.append("%s blk#%d content_lines=%d L%d-L%d -> %s" % (
        fname, seq, len(b["content"]), b["open"] + 1, b["close"] + 1, ph))
    # 替换：保留 fenced 开闭行，内容行替换为单行占位符
    newls = []
    for i, l in enumerate(ls):
        if b["open"] < i < b["close"]:
            if i == b["open"] + 1:
                newls.append(ph)
        else:
            newls.append(l)
    io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(newls))

o = io.open(r"_repo_mirror/work/log/_tools_v171_ph.log", "w", encoding="utf-8", newline="\n")
for l in log:
    o.write(l + "\n")
o.close()
print("PLACEHOLDERIZED n=" + str(len(log)))
