#!/usr/bin/env python3
# verifier/v16 — v2.X 文献调研与论文准备验收（v15 冻结不可变）
import json, re, subprocess, sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

def md5(p):
    return hashlib.md5(p.read_bytes()).hexdigest()

# 1. 1.X 论文零改动（哈希基线 2026-08-28 记录值）
check("1.X CN 论文未被覆盖", md5(ROOT / "paper/deposon_paper_v1.md")
      == "7c22c9f8960787792e6dc14a4f06d8d0")
check("1.X EN 论文未被覆盖", md5(ROOT / "paper/deposon_paper_v1_en.md")
      == "458ec3597ee1d445943d8f36fcbfe20b")

# 2. 文献扫描产物
for f, kw in [("reviews/literature_scan_v2X_A.md", ["Monderer", "Sandholm", "Pigou", "Roughgarden"]),
              ("reviews/literature_scan_v2X_B.md", ["Reversal Curse", "KitBuild", "Tramèr", "Underclaiming"])]:
    p = ROOT / f
    ok = p.exists()
    t = p.read_text(encoding="utf-8") if ok else ""
    check(f"{Path(f).name} 存在且 ≥10KB", ok and len(t) > 10000, f"{len(t)}B")
    for k in kw:
        check(f"{Path(f).name} 含锚点「{k}」", k in t)

# 3. 论文 v2 骨架与 Related Work
ol = (ROOT / "paper/v2/outline_v2X.md").read_text(encoding="utf-8")
check("骨架首选定位已定稿（boundary mapping）", "文献已确认" in ol)
check("骨架含接续声明（不覆盖 1.X）", "接续而非覆盖" in ol or "独立新稿" in ol)
rw = (ROOT / "paper/v2/related_work_v2X.md").read_text(encoding="utf-8")
for k in ["Monderer", "Sandholm", "Reversal Curse", "KitBuild", "Pigou",
          "Tramèr", "Underclaiming", "KICGPT", "Ruiz-Primo", "Proof-of-Learning"]:
    check(f"RW 含「{k}」", k in rw)
check("RW 含同源污染降级", "同源污染" in rw)
check("RW 含 KitBuild 显式承认", "必须显式承认" in rw or "KitBuild" in rw)

# 4. 密钥红线与 pytest
watch = "sk-" + "kimi-"
leak = [str(p) for p in [ROOT / "paper/v2/outline_v2X.md", ROOT / "paper/v2/related_work_v2X.md",
        ROOT / "reviews/literature_scan_v2X_A.md", ROOT / "reviews/literature_scan_v2X_B.md"]
        if watch in p.read_text(encoding="utf-8", errors="ignore")]
check("本轮资产无密钥前缀", not leak, str(leak[:3]))
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
