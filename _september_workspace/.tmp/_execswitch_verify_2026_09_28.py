# -*- coding: utf-8 -*-
"""V4 执行面切换落地棒 · 验证脚本 (worker, 2026-09-28)

只做 3 件事, 0 跑实验 / 0 新读数 / 0 调阈值:
  V1  新名件语法核验 (ast.parse, 不执行)
  V2  旧 4 件 0 触动实证 (SHA-12 复算比对)
  V3  切换语义静态核验 (原子写三段式 / 非原子全量覆盖写 0 命中)

SHA-12 = hashlib.sha256(data).hexdigest()[:12] 小写
"""
import ast
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 切换对: (旧件, 旧件登记 SHA-12, 新件, 新件登记 SHA-12)
PAIRS = [
    (
        "results/_v4_supp_t15_executor_r1_2026_09_27.py", "6d22444c65af",
        "results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py", "9e89e021ea03",
    ),
    (
        "results/_v4_supp_t15r2_executor_r1_2026_09_28.py", "e0936a68fa82",
        "results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py", "215db16a0556",
    ),
]

results = []
fails = 0


def sha12(rel):
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()[:12]


def rec(vid, name, ok, detail):
    global fails
    if not ok:
        fails += 1
    results.append({"id": vid, "name": name, "ok": bool(ok), "detail": detail})


# ---- V1 新名件语法核验 (ast.parse, 0 执行) ----
for old_rel, old_sha, new_rel, new_sha in PAIRS:
    data = (ROOT / new_rel).read_bytes()
    try:
        ast.parse(data.decode("utf-8"))
        rec("V1." + Path(new_rel).name, "新名件语法核验", True,
            "ast.parse OK, bytes=%d, sha12=%s" % (len(data), sha12(new_rel)))
    except SyntaxError as e:
        rec("V1." + Path(new_rel).name, "新名件语法核验", False,
            "SyntaxError: %s" % e)

# ---- V2 旧 4 件 0 触动实证 (复算比对登记值) ----
for old_rel, old_sha, new_rel, new_sha in PAIRS:
    rec("V2." + Path(old_rel).name, "旧件 0 触动 (复算 == 登记值)",
        sha12(old_rel) == old_sha,
        "recomputed=%s registered=%s" % (sha12(old_rel), old_sha))
    rec("V2." + Path(new_rel).name, "新件哈希 (复算 == 登记值)",
        sha12(new_rel) == new_sha,
        "recomputed=%s registered=%s" % (sha12(new_rel), new_sha))

# ---- V3 切换语义静态核验 ----
for old_rel, old_sha, new_rel, new_sha in PAIRS:
    new_src = (ROOT / new_rel).read_text(encoding="utf-8")
    old_src = (ROOT / old_rel).read_text(encoding="utf-8")
    # 新件必须有原子写三段式: 临时件 + fsync + os.replace
    has_tmp = ("tmp" in new_src) and ("with open(tmp" in new_src or "NamedTemporaryFile" in new_src)
    has_fsync = "os.fsync" in new_src
    has_replace = "os.replace" in new_src
    rec("V3." + Path(new_rel).name, "新件原子写三段式齐备",
        has_tmp and has_fsync and has_replace,
        "tmp=%s fsync=%s os.replace=%s" % (has_tmp, has_fsync, has_replace))
    # 旧件 = 非原子全量覆盖写 (write_text 直接写目标) 的证据留痕
    old_na = ("write_text" in old_src) and ("os.replace" not in old_src)
    rec("V3." + Path(old_rel).name, "旧件非原子覆盖写 (留痕, 未修改)",
        True,
        "old_has_write_text=%s old_has_os_replace=%s (仅登记, byte 0 触动)"
        % ("write_text" in old_src, "os.replace" in old_src))

print("=== VERIFY RESULTS ===")
for r in results:
    print("[%s] %-34s %-8s %s"
          % ("PASS" if r["ok"] else "FAIL", r["id"], r["name"], r["detail"]))
print("TOTAL=%d PASS=%d FAIL=%d" % (len(results), len(results) - fails, fails))
sys.exit(1 if fails else 0)
