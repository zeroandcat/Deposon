#!/usr/bin/env python3
"""verifier/v5 — v1.6 LLM 先验臂基础设施验收（pending-key 态）。
与 v4 差异：对象从 v1.5 原型转为 v1.6 集成基建；接受 llm_arms=pending_no_key
为合法状态（真实评估待 key），但要求判据预登记且非 LLM 臂数字复现 v1.5.1。"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails, warns = [], []

def check(name, ok, warn=False):
    if not ok:
        (warns if warn else fails).append(name)
        print(("WARN " if warn else "FAIL ") + name)
    else:
        print("ok   " + name)

for f in ["llm_prior.py", "run_v16_llm_prior.py", "tests/test_llm_prior.py",
          "results/deposon_v16_llm_prior.json"]:
    check(f"exists {f}", os.path.isfile(os.path.join(ROOT, f)))

r = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"],
                   cwd=ROOT, capture_output=True, text=True)
tail = (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else ""
check(f"pytest green ({tail})", r.returncode == 0 and "failed" not in tail)

d = json.load(open(os.path.join(ROOT, "results/deposon_v16_llm_prior.json")))
check("判据预登记存在", bool(d.get("success_criteria_preregistered")))
st = d.get("llm_arms")
if st == "pending_no_key":
    check("pending 态合法标注", True)
    b = d.get("experiment_B", {})
    arms = b.get("arms", {})
    fg = arms.get("field_guided", {}).get("top3_hit_named_path", {})
    fg_mean = fg.get("mean") if isinstance(fg, dict) else fg
    check("非LLM臂复现 v1.5.1 (named=0.176)", fg_mean is not None and abs(fg_mean - 0.17647058823529413) < 1e-9)
    check("成功判据未求值(pending)", d.get("success_evaluation", {}).get("status") == "pending_no_key")
else:
    check("LLM 臂已真实评估(非 pending)", st == "evaluated", warn=True)

pat = "sk-kimi" + "-"
leak = subprocess.run(["grep", "-rl", pat, ROOT, "--include=*.py", "--include=*.json"],
                      capture_output=True, text=True)
hits = [p for p in leak.stdout.splitlines() if "/verifier/" not in p and "_backup_" not in p]
check("no key leak", len(hits) == 0)

print(f"\nFAILS: {len(fails)}  WARNS: {len(warns)}")
sys.exit(1 if fails else 0)
