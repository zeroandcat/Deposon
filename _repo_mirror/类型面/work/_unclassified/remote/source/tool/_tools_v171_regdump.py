# -*- coding: utf-8 -*-
"""v171 登记件逐行编号输出（供抽取行号之可核性 + 逐字照录之程序化抽取）。
"""
import io

REG = r"_repo_mirror/verdict/pi/_pi_card_answers_register_2026_10_20_v171.md"
OUT = r"_repo_mirror/verdict/pi/_tools_v171_reg_lines.txt"

with io.open(REG, "r", encoding="utf-8", newline="") as f:
    raw = f.read()

lines = raw.split("\n")
o = io.open(OUT, "w", encoding="utf-8", newline="\n")
for i, ln in enumerate(lines, start=1):
    o.write("L%03d|%s\n" % (i, ln))
o.close()
print("LINES=" + str(len(lines)))
print("TOTAL_CHARS=" + str(len(raw)))
