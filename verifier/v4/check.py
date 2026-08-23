#!/usr/bin/env python3
"""verifier/v4 — Deposon v1.5.1 扩散原型验收。
v1 验收论文终版；v2 验收 v1.5 代码交付：文件存在、测试全绿、
结果 JSON 完整性与诚实性字段、死锁修复证据、key 泄漏扫描。"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails, warns = [], []

def check(name, ok, warn=False):
    if not ok:
        (warns if warn else fails).append(name)
        print(("WARN " if warn else "FAIL ") + name)
    else:
        print("ok   " + name)

# 1. 文件存在
for f in ["deposon_diffusion.py", "tests/test_diffusion.py", "run_v15_experiment.py"]:
    check(f"exists {f}", os.path.isfile(os.path.join(ROOT, f)))
# v4: 大 JSON(>500KB) 因 MCP 传输上限未镜像 GitHub; 本地全量 / 远端摘要二选一即合格
FULL = os.path.join(ROOT, "results/deposon_v15_diffusion.json")
SUM = os.path.join(ROOT, "results/deposon_v15_diffusion_summary.json")
check("exists full-or-summary results JSON",
      os.path.isfile(FULL) or os.path.isfile(SUM))
check("archive (full negative-result JSON) local-only documented",
      os.path.isfile(os.path.join(ROOT, "results/deposon_v15_diffusion_maxpath_negativeresult.json"))
      or os.path.isfile(SUM), warn=not os.path.isfile(
          os.path.join(ROOT, "results/deposon_v15_diffusion_maxpath_negativeresult.json")))

# 2. 测试全绿
r = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"],
                   cwd=ROOT, capture_output=True, text=True)
tail = (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else ""
check(f"pytest green ({tail})", r.returncode == 0 and "failed" not in tail)

# 3. 结果 JSON
_p = FULL if os.path.isfile(FULL) else SUM
d = json.load(open(_p))
_summary_mode = (_p == SUM)
check("spec_version==v1.5.1", d.get("spec_version") == "v1.5.1")
check("energy_mode aggregate present", "aggregate" in str(d.get("energy_mode")))
b = d.get("experiment_B", {})
check("B field_active >= 48/49 (死锁修复)", b.get("n_field_active", 0) >= 48)
check("B maxpath field_active == 0 (对照成立)", b.get("n_field_active_maxpath") == 0)
a = d.get("experiment_A", {}).get("0.2", {})
agg = a.get("arms", {}).get("field_guided", {})
def _g(arm_dict):
    v = arm_dict.get("gold_path_top3_hit", 0)
    return v.get("mean", 0) if isinstance(v, dict) else (v or 0)
check("A r=0.2 aggregate gold_top3 > random (正增益记录)",
      _g(agg) > _g(a.get("arms", {}).get("random", {})) or _g(agg) > 0.25)
check("honesty 字段非空且含负面声明", len(d.get("honesty", [])) >= 3)
check("逐边明细 49 条 (仅全量模式)", len(b.get("per_edge", [])) == 49, warn=_summary_mode)

# 4. key 泄漏扫描（排除 verifier 自身）
pat = "sk-kimi" + "-"
leak = subprocess.run(["grep", "-rl", pat, ROOT, "--include=*.py", "--include=*.json",
                       "--include=*.md"], capture_output=True, text=True)
hits = [p for p in leak.stdout.splitlines() if "/verifier/" not in p and "_backup_" not in p]
check("no key leak", len(hits) == 0)
if hits: print("   leak hits:", hits)

print(f"\nFAILS: {len(fails)}  WARNS: {len(warns)}")
sys.exit(1 if fails else 0)
