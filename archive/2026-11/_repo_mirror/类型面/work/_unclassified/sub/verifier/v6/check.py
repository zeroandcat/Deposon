#!/usr/bin/env python3
"""verifier/v6 — v1.6 LLM 先验臂真实评估验收（evaluated 态）。
与 v5 差异：v5 验收 pending 基建；v6 验收真实 API 评估结果——
llm_arms=completed、缓存存在且含 9 条先验、判据已求值、
融合增益方向断言（hybrid named > 物理臂、hybrid 总 top3 为六臂最高）、
预登记强判据未达必须如实记录、泄漏扫描。"""
import json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails, warns = [], []

def check(name, ok, warn=False):
    if not ok:
        (warns if warn else fails).append(name)
        print(("WARN " if warn else "FAIL ") + name)
    else:
        print("ok   " + name)

d = json.load(open(os.path.join(ROOT, "results/deposon_v16_llm_prior.json")))
check("llm_arms == completed", d.get("llm_arms") == "completed")
cache_p = os.path.join(ROOT, "results/llm_prior_cache.json")
check("先验缓存存在", os.path.isfile(cache_p))
c = json.load(open(cache_p))
check("缓存 9 条先验 + prompt_sha 在案", c.get("n_prior_edges") == 9 and bool(c.get("prompt_sha256")))
ev = d.get("success_evaluation", {})
check("判据已求值", ev.get("status") == "evaluated")
check("预登记强判据未达且如实记录 (any_lambda_pass=false)",
      ev.get("any_lambda_pass") is False)
arms = d["experiment_B"]["arms"]
named = {a: arms[a]["top3_hit_named_path"]["mean"] for a in arms}
overall = {a: arms[a]["top3_hit"]["mean"] for a in arms}
check("融合增益方向: hybrid named > 物理臂 named",
      all(named[f"hybrid@{l}"] > named["field_guided"] for l in ("0.25","0.5","1.0","2.0")))
check("脑图总任务优势: hybrid 总 top3 为六臂最高",
      all(overall[f"hybrid@{l}"] == max(overall.values()) for l in ("0.25","0.5","1.0","2.0"))
      and overall["hybrid@1.0"] > overall["field_guided"])
check("named 弱于 random 如实保留 (0.294<0.412)",
      named["hybrid@1.0"] < named["random"])
check("honesty 字段覆盖 LLM 来源与判据求值", len(d.get("honesty", [])) >= 6)

r = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"],
                   cwd=ROOT, capture_output=True, text=True)
tail = (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout or r.stderr) else ""
check(f"pytest green ({tail})", r.returncode == 0 and "failed" not in tail)

pat = "sk-kimi" + "-"
leak = subprocess.run(["grep", "-rl", pat, ROOT, "--include=*.py", "--include=*.json",
                       "--include=*.md"], capture_output=True, text=True)
hits = [p for p in leak.stdout.splitlines() if "/verifier/" not in p and "_backup_" not in p]
check("no key leak", len(hits) == 0)

print(f"\nFAILS: {len(fails)}  WARNS: {len(warns)}")
sys.exit(1 if fails else 0)
