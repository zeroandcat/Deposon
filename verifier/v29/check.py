#!/usr/bin/env python3
"""verifier/v29 — GT-8b real_semantics 轴 API 复现验收"""
import json, pathlib, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

d = json.loads((R/"results/deposon_v20_gt8b.json").read_text())
v = d["gt8b_verdict"]
check("GT-8b verdict == inconclusive（有效域 1<2，不美化）", v["verdict"] == "inconclusive" and v["n_valid_domains"] == 1)
check("有效域 chinese_dynasties 满足阈值且在 satisfied 清单", v["domains_satisfied"] == ["chinese_dynasties"])
ns = d["per_domain"]["L_chinese_dynasties"]["named_summary"]
check("先验 0.7805 ≫ field 0.0732（阈值 ≥0.6 且 margin>0.2）",
      abs(ns["llm_prior"]-0.7805) < 1e-4 and abs(ns["field_mean"]-0.0732) < 1e-4)
check("chemical_elements 记 cache_missing", "chemical_elements" in d.get("cache_missing", []))
spec = (R/"docs/SPEC_GT8B.md").read_text(encoding="utf-8")
check("修正案 B1 登记（240s/预算 9/写于重试前声明）", "修正案 B1" in spec and "240" in spec)
find = (R/"docs/Findings_GT8B.md").read_text(encoding="utf-8")
check("Findings 披露 fetch_failed 全细节", "ReadTimeout" in find and "fetch_failed" in find)
check("Findings 披露自选择偏差局限", "自选择" in find or "选择偏差" in find)
check("Findings 含预算台账 9 次", "9" in find and "预算" in find)
bad = subprocess.run(["grep","-rn","-E","sk-kimi-[A-Za-z0-9]|ark-589571[0-9]",
    "docs/SPEC_GT8B.md","docs/Findings_GT8B.md","run_v20_gt8b_fetch.py","run_v20_gt8b_ingest.py",
    "run_v20_gt8b_eval.py","tests/test_v20_gt8b.py","results/deposon_v20_gt8b.json","results/gt8b_cache"],
    capture_output=True, cwd=R)
check("GT-8b 全部新文件/缓存无密钥串", bad.returncode == 1)
p = subprocess.run([sys.executable,"-m","pytest","tests/","-q"], capture_output=True, text=True, cwd=R)
check("pytest 255 全绿", "255 passed" in p.stdout and "failed" not in p.stdout)
print(f"\nFAILS={len(FAILS)}")
sys.exit(1 if FAILS else 0)