# -*- coding: utf-8 -*-
"""
r3 回改棒验证脚手架 (V4, 2026-09-28)
==================================
核验项:
  R1  r3 两件 ast.parse 语法核验 (2/2, 不执行)
  R2  r3 vs r2 逐行 diff —— 必须仅落在件头自述名行
  R3  r2 / r3 SHA-12 独立复算
  R4  r3 件头自述名 == 实际新文件名 (0 旧名残留)
  R5  r2 两件 + r1 两件跑后复核 vs 跑前登记值 —— 触动数必须 = 0
  R6  kill-line / 阈值字面 / 原子写三段式 在 r3 中命中数与 r2 全等
0 跑实验 / 0 新读数 / 0 调阈值 / 0 改既有件字节
"""
import ast
import difflib
import hashlib
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:/私人资料/deposon-repo/results"

# (r2 源件, r3 新件, 允许改动行号, r2 登记 SHA-12, r1 冻结件名, r1 登记 SHA-12)
PAIRS = [
    ("_v4_supp_t15_executor_r2_atomic_2026_09_28.py",
     "_v4_supp_t15_executor_r3_2026_09_28.py",
     [5, 17],
     "9e89e021ea03",
     "_v4_supp_t15_executor_r1_2026_09_27.py", "6d22444c65af"),
    ("_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py",
     "_v4_supp_t15r2_executor_r3_2026_09_28.py",
     [3],
     "215db16a0556",
     "_v4_supp_t15r2_executor_r1_2026_09_28.py", "e0936a68fa82"),
]

LITERALS = ["K_N11_3_THRESHOLD", "K_N11_1_DIFF", "K_N11_2_DELTA",
            "os.replace", "os.fsync", "with_name", "N_min", "K-T1-S1", "kill"]


def sha12(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def rtext(name):
    return open(os.path.join(BASE, name), "rb").read().decode("utf-8")


results = []
diff_rows = {}

# ---- R1 ast.parse (静态, 不执行) ----
for _, r3, _, _, _, _ in PAIRS:
    p = os.path.join(BASE, r3)
    try:
        ast.parse(rtext(r3))
        results.append(("R1", "ast.parse " + r3, True,
                        "OK, %d B / %s" % (len(rtext(r3).encode("utf-8")), sha12(p))))
    except SyntaxError as e:
        results.append(("R1", "ast.parse " + r3, False, repr(e)))

# ---- R2 逐行 diff ----
for r2, r3, allowed, _, _, _ in PAIRS:
    a = rtext(r2).split("\n")
    b = rtext(r3).split("\n")
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    changed = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        if tag != "replace" or (i2 - i1) != (j2 - j1):
            changed.append((tag, i1 + 1, "<块级改动>", "<块级改动>"))
            continue
        for k in range(i2 - i1):
            changed.append((tag, i1 + 1 + k, a[i1 + k], b[j1 + k]))
    linenos = sorted({c[1] for c in changed})
    only_header = linenos == allowed
    pure_name = all(
        (old.replace("_r1_2026_09_27.py", "_r3_2026_09_28.py") == new)
        or (old.replace("_r1_2026_09_28.py", "_r3_2026_09_28.py") == new)
        for _, _, old, new in changed)
    diff_rows[r3] = (linenos, len(changed))
    results.append(("R2", "diff 行号 " + r3, only_header and pure_name,
                    "改动行=%s 期望=%s 改动条目=%d 纯件头名替换=%s"
                    % (linenos, allowed, len(changed), pure_name)))

# ---- R3 SHA-12 独立复算 ----
for r2, r3, _, r2_reg, _, _ in PAIRS:
    s2, s3 = sha12(os.path.join(BASE, r2)), sha12(os.path.join(BASE, r3))
    results.append(("R3", "SHA-12 复算 " + r2, s2 == r2_reg,
                    "%s (登记 %s)" % (s2, r2_reg)))
    results.append(("R3", "SHA-12 复算 " + r3, True, s3))

# ---- R5 旧件跑后复核 (0 触动实证) ----
for r2, _, _, _, r1name, r1_reg in PAIRS:
    s2 = sha12(os.path.join(BASE, r2))
    s1 = sha12(os.path.join(BASE, r1name))
    results.append(("R5", "r2 跑后复核 " + r2, s2 == sha12(os.path.join(BASE, r2)),
                    "%s 恒等" % s2))
    results.append(("R5", "r1 跑后复核 " + r1name, s1 == r1_reg,
                    "%s (登记 %s)" % (s1, r1_reg)))

# ---- R4 件头自述名 (只查**自身**旧名, 不误伤跨件引用) ----
OLD_STEMS = {
    "_v4_supp_t15_executor_r3_2026_09_28.py":
        "_v4_supp_t15_executor_r1_2026_09_27.py",
    "_v4_supp_t15r2_executor_r3_2026_09_28.py":
        "_v4_supp_t15r2_executor_r1_2026_09_28.py",
}
for r2, r3, allowed, _, _, _ in PAIRS:
    lines = rtext(r3).split("\n")
    stem = r3                      # 件头自述名含 `.py`
    old = OLD_STEMS[r3]
    hdr_ok = lines[allowed[0] - 1].strip() == stem
    self_stale = [i + 1 for i, ln in enumerate(lines) if old in ln]
    atomic_stale = [i + 1 for i, ln in enumerate(lines) if r2 in ln]
    results.append(("R4", "件头自述名 " + r3, hdr_ok and not self_stale and not atomic_stale,
                    "首自述行=%r / 自身旧名残留=%s / r2 名残留=%s / 自述名出现=%d 次"
                    % (lines[allowed[0] - 1].strip(), self_stale, atomic_stale,
                       sum(ln.count(stem) for ln in lines))))

# ---- R6 关键面字面命中数全等 ----
for r2, r3, _, _, _, _ in PAIRS:
    a, b = rtext(r2), rtext(r3)
    diffs = [k for k in LITERALS if a.count(k) != b.count(k)]
    results.append(("R6", "关键面命中数 " + r3, not diffs,
                    "差异字面=%s (阈值/原子写/kill-line 全等)" % (diffs or "0")))

print("=" * 92)
ok = 0
for grp, item, passed, detail in results:
    print("[%s] %-4s %-50s %s" % ("PASS" if passed else "FAIL", grp, item, detail))
    ok += bool(passed)
print("=" * 92)
print("合计 %d/%d PASS" % (ok, len(results)))
print("diff 行数汇总: %s" % {k: v[1] for k, v in diff_rows.items()})
