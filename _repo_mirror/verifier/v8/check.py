#!/usr/bin/env python3
"""v8 — 区分度补实验与独立审校落实验收。

判据：独立审校汇总落盘；v1.7.1 同协议融合修复/阴性对照、fixed_sampler、多图稳健性三份结果存在；
论文 §4.7/D.5/Table C1 纳入 v1.7.1 且保留诚实降级（非显著、采样器敏感、synthetic_null、不回溯改写 v1.6）；
pytest 全绿；无 API key 泄漏。exit 0=PASS。"""
from pathlib import Path
import json, subprocess, sys
ROOT = Path(__file__).resolve().parents[2]
fails=[]
def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok: fails.append(name)

cn=(ROOT/"paper/deposon_paper_v1.md").read_text(encoding="utf-8")
en=(ROOT/"paper/deposon_paper_v1_en.md").read_text(encoding="utf-8")
check("review_file", (ROOT/"reviews/independent_review_20260823.md").exists())
for f in ["results/deposon_v17_fusion_fix.json", "results/deposon_v17_fixed_sampler.json",
          "results/deposon_v17_multigraph.json", "results/deposon_v17_fusion_fix_tieartifact_negativeresult.json",
          "docs/SPEC_v1.7.1.md", "run_v17_fusion_fix.py", "run_v17_fixed_sampler.py", "run_v17_multigraph.py"]:
    check("exists_"+f, (ROOT/f).exists())
fix=json.loads((ROOT/"results/deposon_v17_fusion_fix.json").read_text(encoding="utf-8"))
fixed=json.loads((ROOT/"results/deposon_v17_fixed_sampler.json").read_text(encoding="utf-8"))
mg=json.loads((ROOT/"results/deposon_v17_multigraph.json").read_text(encoding="utf-8"))
arms=fix["experiment_B"]["arms"]
check("hn2_named_0471", abs(arms["hybrid_norm@2.0"]["top3_hit_named_path"]["mean"]-0.47058823529411764)<1e-9)
check("fixed_overall_random_0388", abs(fixed["experiment_B"]["arms"]["random"]["top3_hit"]["mean"]-0.3877551020408163)<1e-9)
check("multigraph_k20", mg["k_graphs"]==20 and abs(mg["summary_graph_level"]["hybrid_norm@2.0"]["named_mean"]-0.47058823529411764)<1e-9)
for s,lang in [(cn,"cn"),(en,"en")]:
    check(lang+"_header_v171", "v1.7.1" in s.split("\n")[6 if lang=="cn" else 4])
    check(lang+"_tableC_v171", "v1.2 → v1.7.1" in s)
    check(lang+"_d5", "D.5" in s)
    check(lang+"_honest_nonsig", ("非统计显著" in s) if lang=="cn" else ("non-significant" in s))
    check(lang+"_sampler_sensitive", ("采样器敏感" in s) if lang=="cn" else ("sampler-sensitive" in s or "sampler definition" in s))
    check(lang+"_synthetic_null", "synthetic_null" in s)
    check(lang+"_no_retro", ("不回溯改写 v1.6" in s) if lang=="cn" else ("not a retroactive change" in s))
# pytest
r=subprocess.run([sys.executable,"-m","pytest","-q"],cwd=ROOT,text=True,capture_output=True)
check("pytest_green", r.returncode==0 and "109 passed" in r.stdout, r.stdout.strip().splitlines()[-1] if r.stdout else "")
# key leak scan (pattern assembled to avoid self-hit)
pat="sk-"+"kimi-"; leak=[]
for p in ROOT.rglob("*"):
    if ".git" in p.parts or not p.is_file() or p.suffix.lower() not in {".py",".md",".json",".txt",".log",".bib"}: continue
    try: t=p.read_text(encoding="utf-8",errors="ignore")
    except Exception: continue
    if pat in t: leak.append(str(p.relative_to(ROOT)))
check("no_key_leak", not leak, ",".join(leak[:3]))
print(f"FAILS: {len(fails)}")
sys.exit(1 if fails else 0)
