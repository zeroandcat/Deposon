# -*- coding: utf-8 -*-
"""注记件行号终校（工具件 · 0 属证据面）。"""
import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
BASE = Path(r"D:\私人资料\deposon-repo")
FIX = BASE / "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_fix_2026_10_10.py"
REN = BASE / "deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_10_09_selfverify_rename_2026_10_10.py"

print("① L20 内容:", repr(FIX.read_text(encoding="utf-8").split("\n")[19]))
print("① L18-L22:")
for i in range(18, 23):
    print(f"   L{i} | {FIX.read_text(encoding='utf-8').split(chr(10))[i-1][:100]}")

L = FIX.read_text(encoding="utf-8").split("\n")
print("\n① 5b 段全域 L365-L400:")
for i in range(365, 401):
    print(f"   L{i} | {L[i-1].strip()[:100]}")
print("\n① probe 段末 L260-L268:")
for i in range(260, 269):
    print(f"   L{i} | {L[i-1].strip()[:100]}")
print("\n① 顶层节 L531-L536 ＋ L553-L557 ＋ L575-L584:")
for rng in ((531, 536), (553, 557), (575, 584)):
    for i in range(rng[0], rng[1]):
        print(f"   L{i} | {L[i-1].strip()[:100]}")

R = REN.read_text(encoding="utf-8").split("\n")
print("\n② key_rename_migration 起止 L520-L522 ＋ L544-L549:")
for i in list(range(520, 523)) + list(range(544, 550)):
    print(f"   L{i} | {R[i-1].strip()[:100]}")
print("\n② runner_fix_notice L591-L599:")
for i in range(591, 600):
    print(f"   L{i} | {R[i-1].strip()[:100]}")
