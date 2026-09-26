#!/usr/bin/env python3
# verifier/v24 — 博弈论重构收口验收（v23 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. GT-5/5b/6 判定锚点
gt5 = json.load(open(ROOT / "results/deposon_v20_gt5.json"))
check("GT-5 inconclusive 如实判", "inconclusive" in gt5["verdict"]["verdict"])
gt5b = json.load(open(ROOT / "results/deposon_v20_gt5b.json"))
check("GT-5b 22/22 单调率 100%",
      gt5b["verdict"]["verdict"] == "supports_narrowed_monotonicity"
      and len(gt5b["verdict"]["graphs_with_full_monotonicity"]) == 22)
gt6 = json.load(open(ROOT / "results/deposon_v20_gt6.json"))
check("GT-6 势解释完备（中位口径）",
      gt6["verdict"]["verdict"] == "potential_game_explanation_complete"
      and gt6["verdict"]["median_residual_ratio"] < 0.10)
exc = [k for k, v in gt6["per_graph_summary"].items()
       if v["residual_ratio_mean"] > 0.10]
check("GT-6 三张高残余图如实披露", len(exc) == 3, str(exc))

# 2. 重构文档与评审闭环
gt_doc = (ROOT / "docs/GT_RECONSTRUCTION.md").read_text(encoding="utf-8")
for kw in ["势博弈", "探索-利用", "inconclusive", "22/22", "1.6e-29",
           "Monderer", "Candogan", "承诺装置"]:
    check(f"重构文档含「{kw}」", kw in gt_doc)
rv = (ROOT / "reviews/review_coach_v2X_outline.md").read_text(encoding="utf-8")
check("评审报告在库且总评 borderline", "borderline" in rv)
ol = (ROOT / "paper/v2/outline_v2X.md").read_text(encoding="utf-8")
bad = [ln for ln in ol.splitlines()
       if "92.5% vs 92.5%" in ln and "撤回" not in ln and "修订记录" not in ln]
check("M1 闭合（旧宣称仅存于修订记录元描述）", not bad, str(bad[:1]))
check("M2 闭合（H-A1 判死标注）", "判死" in ol and "0.0118" in ol)
check("M5 闭合（GT-3b 口径入骨架）", "W=1.0" in ol and "GT-3b" in ol)
rw = (ROOT / "paper/v2/related_work_v2X.md").read_text(encoding="utf-8")
check("related_work 同步（PoA=1.33 旧宣称 0 残留）", "PoA=1.33" not in rw
      and "巧合性对齐" in rw)

# 3. 红线与回归
leak = []
for w in ["sk-" + "kimi-", "ark-" + "589571"]:
    for p in list(ROOT.glob("run_v20_gt5*.py")) + [ROOT / "run_v20_gt6.py",
             ROOT / "docs/GT_RECONSTRUCTION.md",
             ROOT / "paper/v2/outline_v2X.md", ROOT / "paper/v2/related_work_v2X.md",
             ROOT / "reviews/review_coach_v2X_outline.md"]:
        if w in p.read_text(encoding="utf-8", errors="ignore"):
            leak.append(str(p))
check("本轮资产双 key 红线", not leak, str(leak[:3]))
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None,
      (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
