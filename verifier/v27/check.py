#!/usr/bin/env python3
"""verifier/v27 — GT-2B 多陷阱强度升级（题库轨）验收"""
import json, pathlib, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

d = json.loads((R/"results/deposon_v20_gt2b.json").read_text())
check("GT-2B verdict == inconclusive（如实，不美化）", d["verdict"] == "inconclusive")
per_T = d["per_T"]
check("T∈{1,2,3} 三档齐全", set(per_T.keys()) == {"1","2","3"})
def agg(t, arm):
    if "overall" in per_T[t]:
        return per_T[t]["overall"][arm]
    tot = c = 0
    for dom in per_T[t]["per_domain"].values():
        n = dom["n_items"]; acc = dom["accuracy"][arm]
        tot += n; c += round(acc*n)
    return c/tot
rf = [agg(t,"rule_filter") for t in ("1","2","3")]
fm = [agg(t,"field_mean") for t in ("1","2","3")]
check("rule_filter 非单调（0.15/0.275/0.20）", abs(rf[0]-0.15)<1e-9 and abs(rf[1]-0.275)<1e-9 and abs(rf[2]-0.20)<1e-9)
check("T=2 与既有题库 27.5% 逐点复现", abs(rf[1]-0.275)<1e-9)
check("场免疫破坏如实记录（field 随 T 上升）", fm[2] > fm[1] > fm[0])
spec = (R/"docs/SPEC_GT2B.md").read_text(encoding="utf-8")
check("SPEC 含判死线/单调判据/零 API 声明", "H_GT2B_dead" in spec and "单调" in spec and "零 LLM API" in spec)
find = (R/"docs/Findings_GT2B.md").read_text(encoding="utf-8")
check("Findings 披露选项构成假象（判据设计缺陷）", "假象" in find or "缺陷" in find)
bad = subprocess.run(["grep","-rn","-E","sk-kimi-[A-Za-z0-9]|ark-589571[0-9]",
    "docs/SPEC_GT2B.md","docs/Findings_GT2B.md","run_v20_gt2b.py","tests/test_v20_gt2b.py","results/deposon_v20_gt2b.json"],
    capture_output=True, cwd=R)
check("GT-2B 新文件无密钥串", bad.returncode == 1)
p = subprocess.run([sys.executable,"-m","pytest","tests/","-q"], capture_output=True, text=True, cwd=R)
check("pytest 246 全绿", "246 passed" in p.stdout and "failed" not in p.stdout)
print(f"\nFAILS={len(FAILS)}")
sys.exit(1 if FAILS else 0)
