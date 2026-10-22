#!/usr/bin/env python3
# verifier/v14 — 新技能三联验证验收（v13 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 三联产物存在
for p in ["results/v20_graph_features.csv", "results/v20_statcheck_fm_vs_rand.json",
          "results/v20_statcheck_fm_vs_deg.json", "results/v20_regression_field.json",
          "results/v20_regression_field_v2.json", "results/quizbank_v20.json",
          "results/deposon_v20_quiz_eval.json"]:
    check(f"产物存在 {Path(p).name}", (ROOT / p).exists())

# 2. 统计复核锚点
sr = json.load(open(ROOT / "results/v20_statcheck_fm_vs_rand.json"))
txt = json.dumps(sr, ensure_ascii=False)
check("Wilcoxon p≈0.0031 在案", "0.003052" in txt or "0.0031" in txt)
check("Wilcoxon 显著结论", "显著" in txt)
sd = json.load(open(ROOT / "results/v20_statcheck_fm_vs_deg.json"))
check("vs degree p<0.0001 在案", "0.0001" in json.dumps(sd, ensure_ascii=False))

# 3. 回归锚点
rg = json.load(open(ROOT / "results/v20_regression_field_v2.json"))
check("回归 R²≥0.6", rg["r_squared"] >= 0.6, f"R2={rg['r_squared']}")
check("hub_concentration β>0 且 p<0.001",
      rg["coefficients"]["hub_concentration"]["coefficient"] > 0
      and rg["coefficients"]["hub_concentration"]["p_value"] < 0.001)
check("real_semantics β<0 且 p<0.05",
      rg["coefficients"]["real_semantics"]["coefficient"] < 0
      and rg["coefficients"]["real_semantics"]["p_value"] < 0.05)

# 4. 题库锚点
qb = json.load(open(ROOT / "results/quizbank_v20.json"))
check("题库 40 题", qb["n_items"] == 40)
check("干扰项 provenance 在案", all(
    it["distractor_provenance"]["source"].startswith("gt2_attacker_cache")
    for it in qb["items"]))
qe = json.load(open(ROOT / "results/deposon_v20_quiz_eval.json"))
ov = qe["overall"]
check("先验题库准确率 ≥0.9", ov["llm_prior"] >= 0.9, f"{ov['llm_prior']:.3f}")
check("rule_filter ≈ 机会水平（<0.35）", ov["rule_filter"] < 0.35)
check("机制免疫披露在案", "机制性免疫" in json.dumps(qe["honesty"], ensure_ascii=False))

# 5. 文档与红线
fd = (ROOT / "docs/Findings_v2.0_skills.md").read_text(encoding="utf-8")
for kw in ["领域鉴定器", "Wilcoxon", "hub_concentration", "题库", "92.5%"]:
    check(f"Skills 文档含「{kw}」", kw in fd)
watch = "sk-" + "kimi-"
leak = [str(p) for p in [ROOT / "run_v20_quizbank.py", ROOT / "docs/Findings_v2.0_skills.md",
        ROOT / "results/quizbank_v20.json", ROOT / "results/deposon_v20_quiz_eval.json",
        ROOT / "results/v20_graph_features.csv"]
        if watch in p.read_text(encoding="utf-8", errors="ignore")]
check("三联资产无密钥前缀", not leak, str(leak[:3]))

# 6. pytest
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
