#!/usr/bin/env python3
# verifier/v18 — 大型题库验证与空间释放验收（v17 冻结不可变）
import json, re, subprocess, sys, os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 大题库与评估产物
qb = json.load(open(ROOT / "results/quizbank_v20_big.json"))
check("大题库 ≥150 题（6 域全 named 边）", qb["n_items"] >= 150, f"n={qb['n_items']}")
check("6 域覆盖", len({q["domain"] for q in qb["items"]}) == 6)
qe = json.load(open(ROOT / "results/deposon_v20_bigquiz_eval.json"))
ov = qe["overall"]
check("先验大题库 ≥0.85", ov["llm_prior"] >= 0.85, f"{ov['llm_prior']:.3f}")
check("tfidf ≥ field（BOSS 规模化确认）", ov["ngram_tfidf"] > ov["field_mean"],
      f"{ov['ngram_tfidf']:.3f} vs {ov['field_mean']:.3f}")
check("rule_filter 低于机会（≤0.25）", ov["rule_filter"] <= 0.25,
      f"{ov['rule_filter']:.3f}")
check("CoT 映射复现 0.925", abs(qe["cot_arm"]["overall"] - 0.925) < 1e-9)

# 2. 新域资产 provenance
for d in ["geography_world", "project_management"]:
    check(f"新域图 {d} 在 corpus", (ROOT / f"corpus/v20/L_{d}.json").exists())
    for dd in ["familyL_prior_cache", "attacker_xl_cache"]:
        p = ROOT / f"results/{dd}/{d}.json"
        ok = p.exists()
        rec = json.load(open(p)) if ok else {}
        check(f"{dd}/{d}（sha+response）",
              ok and bool(rec.get("prompt_sha256")) and bool(rec.get("response_text")))
idx = json.load(open(ROOT / "corpus/v20/index.json"))
check("corpus index 已重建 22 图", idx["n_graphs"] == 22)

# 3. 空间释放留痕
rl = json.load(open(ROOT / "docs/space_release_log.json"))
check("释放日志存在且 ≥10 条 sha256", len(rl["released"]) >= 10)
check("gz.b64 残留已清除（.sha256 留痕件保留）",
      not list(ROOT.glob("paper/*.gz.b64"))
      and not list(ROOT.glob("paper/*.gz.b64.part-*")))
check("释放原则声明（sha256+再生）", "sha256" in rl["principle"])

# 4. 文档与红线
fd = (ROOT / "docs/Findings_v2.0_bigquiz.md").read_text(encoding="utf-8")
for kw in ["157", "reasoning_tokens", "空间释放", "低于机会", "BOSS"]:
    check(f"BigQuiz 文档含「{kw}」", kw in fd)
watch = "sk-" + "kimi-"
leak = [str(p) for p in [ROOT / "run_v20_bigquiz_fetch.py", ROOT / "run_v20_bigquiz_eval.py",
        ROOT / "docs/Findings_v2.0_bigquiz.md", ROOT / "docs/space_release_log.json",
        ROOT / "results/quizbank_v20_big.json", ROOT / "results/deposon_v20_bigquiz_eval.json"]
        if watch in p.read_text(encoding="utf-8", errors="ignore")]
check("本轮资产无密钥前缀", not leak, str(leak[:3]))

# 5. pytest
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
