#!/usr/bin/env python3
# verifier/v23 — GT-3b 三模型族跨厂商验收（v22 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

spec = (ROOT / "docs/SPEC_GT3.md").read_text(encoding="utf-8")
for kw in ["修正案 A2", "修正案 A3", "doubao-seed-evolving", "deepseek-v4-pro-260425"]:
    check(f"SPEC_GT3 含「{kw}」", kw in spec)

caches = sorted((ROOT / "results/gt3_prior_cache").glob("*.json"))
check("GT3 缓存 24 个（4 新评估者×6 域）", len(caches) == 24, str(len(caches)))
nb_d = sum(1 for p in caches if "doubao" in p.name)
nb_ds = sum(1 for p in caches if "deepseek" in p.name)
check("doubao×6 + deepseek×6", nb_d == 6 and nb_ds == 6)

gt3 = json.load(open(ROOT / "results/deposon_v20_gt3.json"))
check("H_GT3 支持且斩杀线未触发",
      gt3["verdict"]["H_GT3_supported"] is True
      and gt3["verdict"]["H_GT3_dead_triggered"] is False)
check("W=1.0（5 评估者全 ok 域）", gt3["kendall_W"] == 1.0)
c = gt3["criteria"]
check("E3 doubao 4/4 且 0 败", c["E3_doubao-seed-evolving"]["domains_prior_gt_field"] == 4
      and c["E3_doubao-seed-evolving"]["domains_prior_le_field"] == 0)
check("E4 deepseek 6/6 且 0 败", c["E4_deepseek-v4-pro"]["domains_prior_gt_field"] == 6
      and c["E4_deepseek-v4-pro"]["domains_prior_le_field"] == 0)
check("失败 5 缓存如实披露", len(gt3["failures"]) == 5, str(len(gt3["failures"])))

fd = (ROOT / "docs/Findings_GT3.md").read_text(encoding="utf-8")
for kw in ["ByteDance", "DeepSeek", "W=1.0", "同源污染", "局限", "预算"]:
    check(f"Findings_GT3 含「{kw}」", kw in fd)

leak = []
for w in ["sk-" + "kimi-", "ark-" + "589571"]:
    for p in [ROOT / "run_v20_gt3b_fetch.py", ROOT / "run_v20_gt3c_fetch.py",
              ROOT / "run_v20_gt3_eval.py", ROOT / "docs/SPEC_GT3.md",
              ROOT / "docs/Findings_GT3.md", ROOT / "results/deposon_v20_gt3.json"] + caches:
        if w in p.read_text(encoding="utf-8", errors="ignore"):
            leak.append(f"{p}:{w[:6]}")
check("双 key 红线（kimi+ark 前缀）", not leak, str(leak[:3]))

r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None,
      (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
