# -*- coding: utf-8 -*-
"""定位 p1/p2 中 fenced 块与标题行，供占位符替换。"""
import io
import os

TMP = r"〔目录引用·未上传:.tmp〕"
out = io.open(r"_repo_mirror/work/note/_tools_v171_idx.txt", "w", encoding="utf-8", newline="\n")

for name in ("_v171_body_p1.md", "_v171_body_p2.md"):
    p = os.path.join(TMP, name)
    ls = io.open(p, "r", encoding="utf-8", newline="").read().split("\n")
    out.write("=== " + name + " lines=" + str(len(ls)) + "\n")
    infence = False
    for i, l in enumerate(ls, start=1):
        if l.startswith("```"):
            out.write("L%03d|FENCE%s|%s\n" % (i, "OPEN" if not infence else "CLOSE", l[:80]))
            infence = not infence
        elif l.startswith("#### ") or l.startswith("### "):
            out.write("L%03d|HEAD|%s\n" % (i, l[:110]))
out.close()
print("IDX_OK")
