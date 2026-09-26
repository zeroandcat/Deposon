#!/usr/bin/env python3
# verifier/v1/check.py — Deposon v1.4.0 终验清单（零 API，只读检查）
# 用法: python3 verifier/v1/check.py  (从仓库根目录运行)
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
fails, warns = [], []

def req(cond, msg):
    (fails if not cond else []).append(msg) if not cond else None
    return cond

def warn(cond, msg):
    if not cond: warns.append(msg)

P = lambda *a: os.path.join(ROOT, *a)

# 1. 安全闸：无 API key 泄漏
leak = False
PAT = "sk-kimi" + "-"  # 拆分以避免自检误报
for dp, dn, fn in os.walk(ROOT):
    if '.git' in dp or 'pdfbuild' in dp or '__pycache__' in dp or 'verifier' in dp: continue
    for f in fn:
        try:
            if PAT in open(os.path.join(dp, f), errors='ignore').read(): leak = True
        except Exception: pass
req(not leak, "API key 泄漏")

# 2. 关键文件存在
for f in ["paper/deposon_paper_v1.md", "paper/deposon_paper_v1_en.md", "paper/references.bib",
          "results/deposon_benchmark_v1_4_gsm8k.json", "results/deposon_benchmark_v1_4_gsm8k_details.json",
          "results/deposon_gsm8k_stratified.json", "results/deposon_g2_boltzmann_pathintegral_rewrite.json",
          "deposon_agents_v1_3.py", "deposon_agents_v1_4.py", "run_g2_ensemble.py",
          "tests/test_new_modes.py", "RELEASE_v1.4.0.md"]:
    req(os.path.exists(P(f)), f"缺失 {f}")

# 3. GSM8K 终版数字
g = json.load(open(P("results/deposon_benchmark_v1_4_gsm8k.json")))
req(abs(g["cot_baseline_accuracy"] - 0.97) < 1e-9, "CoT != 0.97")
req(abs(g["unified_accuracy"] - 0.85) < 1e-9, "unified != 0.85")
req(abs(g["mcnemar_unified_vs_cot"]["p_value"] - 0.00048828125) < 1e-9, "McNemar p 不符")
req(g["physics_audit"]["passed"], "物理审计未过")

# 4. 论文终版标记（无占位符、无旧 G2 数字、含新表）
for lang, f in [("CN", "deposon_paper_v1.md"), ("EN", "deposon_paper_v1_en.md")]:
    t = open(P("paper", f), encoding="utf-8").read()
    req("GSM8K_RESULTS" not in t, f"{lang} 残留占位符")
    req("Table 11" in t, f"{lang} 缺 Table 11")
    req("26.3" in t, f"{lang} 缺 G2 重写版数字")
    req("t_p^2" not in t and "t+r+a" not in t, f"{lang} 残留小写权重记号")
    req("97.0%" in t and "85.0%" in t, f"{lang} 缺 GSM8K 终版数字")
    warn("run_g2_ensemble.py" in t, f"{lang} 附录C未指向重写版 harness")

# 5. 条件等效声明存在性
cn = open(P("paper/deposon_paper_v1.md"), encoding="utf-8").read()
for kw in ["k=e", "min(1", "K=1", "T+R+A+B"]:
    warn(kw in cn, f"CN 缺条件等效/截断声明: {kw}")

# 6. 双版引用一致性
bib = open(P("paper/references.bib"), encoding="utf-8").read()
n_bib = len(re.findall(r"@\w+\{ref\d+", bib))
req(n_bib == 37, f"bib 条目数 {n_bib} != 37")

print(f"FAILS: {len(fails)}")
for m in fails: print("  [FAIL]", m)
print(f"WARNS: {len(warns)}")
for m in warns: print("  [WARN]", m)
sys.exit(1 if fails else 0)
