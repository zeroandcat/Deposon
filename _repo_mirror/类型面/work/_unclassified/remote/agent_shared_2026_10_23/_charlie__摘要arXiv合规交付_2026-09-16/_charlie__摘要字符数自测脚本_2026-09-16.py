#!/usr/bin/env python3
"""arXiv abstract self-test: character count / ASCII / red-line vocabulary / fidelity checklist.
Usage: python3 查理_摘要字符数自测脚本_2026-09-16.py
"""
import re, sys, pathlib

TXT = pathlib.Path(__file__).with_name("查理_第二作综述摘要_arXiv合规版_2026-09-16.txt")
t = TXT.read_text(encoding="utf-8").rstrip("\n")

print(f"Character count (including spaces, excluding trailing newline): {len(t)}")
print(f"Word count: {len(t.split())}")
print(f"arXiv hard limit 1920 margin: {1920 - len(t)} | dispatch target 1850 margin: {1850 - len(t)}")

# 1) ASCII check (arXiv form Bad character)
bad = [(i, c, hex(ord(c))) for i, c in enumerate(t) if ord(c) > 127]
print(f"Non-ASCII characters: {bad if bad else 'none (pure ASCII)'}")
for ch in "\u2013\u2014\u2018\u2019\u201c\u201d\u00b7\u2460":
    assert ch not in t, f"Found illegal character: {ch!r}"

# 2) Character budget
assert len(t) <= 1850, "Exceeds 1850-character dispatch cap"
assert len(t) <= 1920, "Exceeds arXiv 1920 hard limit"

# 3) Terminology red lines: no first/only priority claims (first-class not counted)
assert re.findall(r"\bfirst\b", t, re.I) in (["first"], []), "first anomaly"
assert t.count("first") == t.count("first-class")
assert not re.findall(r"\bonly\b", t, re.I), "Contains only"
assert t.count("pre-registered") == 3

# 4) Fidelity checklist
for k in ["keep the books", "on-axis", "frozen record",
          "process verification", "chain-of-thought faithfulness",
          "evaluation integrity", "game-theoretic verification",
          "conservation and physical priors",
          "(i)", "(ii)", "(iii)", "(iv)", "(v)", "(vi)",
          "full parity", "three-tier discipline", "three falsified claims",
          "pre-registered controls", "60-entry verified base", "self-citation",
          "negative results as first-class content", "closing problem"]:
    assert k in t, f"Missing keep item: {k}"
print("Fidelity checklist: all 22 items PASS")

# 5) Number-anchor consistency (60 base / 3 falsified / 3-tier / 3-axis / 5 lines / 6 attributes)
for pat in [r"60-entry", r"three falsified", r"three-tier", r"three-axis", r"five-line", r"six attributes"]:
    assert re.search(pat, t), f"Missing number anchor: {pat}"
print("Number anchors: PASS")
print("ALL CHECKS PASS")
