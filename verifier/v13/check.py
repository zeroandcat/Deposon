#!/usr/bin/env python3
# verifier/v13 — v2.0 横向对比（先验臂 × GT-2）验收（v12 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 缓存 provenance
for d in ["physics_concepts", "biological_taxonomy", "algorithm_process", "historical_causality"]:
    for kind, dd in [("prior", "familyL_prior_cache"), ("attacker", "gt2_attacker_cache")]:
        p = ROOT / f"results/{dd}/{d}.json"
        ok = p.exists()
        rec = json.load(open(p)) if ok else {}
        check(f"缓存 {kind}/{d}（sha+response_text）",
              ok and bool(rec.get("prompt_sha256")) and bool(rec.get("response_text")))

# 2. 横向对比判定锚点
d = json.load(open(ROOT / "results/deposon_v20_crossval.json"))
pe = d["prior_arm_eval"]
check("先验臂 4/4 图 named 第一", all(
    pe[g]["llm_prior"]["named"] >= max(pe[g][a]["named"] or 0 for a in pe[g])
    for g in pe))
check("biology 先验 named=1.000", abs(pe["L_biological_taxonomy"]["llm_prior"]["named"] - 1.0) < 1e-9)
check("historical 先验 named≈0.783", abs(pe["L_historical_causality"]["llm_prior"]["named"] - 0.7826) < 0.01)
check("融合不增（hybrid≤prior 逐图）", all(
    pe[g]["hybrid_norm@0.5"]["named"] <= pe[g]["llm_prior"]["named"] + 1e-9 for g in pe))
da = d["direction_analysis"]
check("GOAL 反向=0 全四图", all(a["hub_reversed_edges"] == 0 for a in da.values()))
check("方向一致率 ≥0.95 全四图", all(
    (a["direction_agreement_on_shared"] or 0) >= 0.95 for a in da.values()))
check("同源污染声明在案", "同源污染" in json.dumps(d["honesty"], ensure_ascii=False))

# 3. GT-2 判定锚点
m = d["gt2_attacker_meta"]
check("攻击 evasion_rate=1.0 全四图", all(v["evasion_rate"] == 1.0 for v in m.values()))
gv = d["gt2_verdict"]
check("GT-2 verdict=no_separation（预登记机械规则）",
      gv["verdict"] == "no_separation_adaptive_attack_not_decisive")
check("field_mean 塌陷=0 全四图",
      all(c["field_mean"] == 0.0 for c in gv["per_graph_collapse"].values()))
check("rule 塌陷均值≈7.5pp", abs(gv["rule_collapse_mean_pp"] - 0.075) < 0.01)

# 4. 文档与红线
fd = (ROOT / "docs/Findings_v2.0_crossval.md").read_text(encoding="utf-8")
for kw in ["横向对比", "同源污染", "GOAL 中心反向未复现", "no_separation", "分工叙事"]:
    check(f"CrossVal 文档含「{kw}」", kw in fd)
watch = "sk-" + "kimi-"
leak = []
for p in [ROOT / "run_v20_crossval_fetch.py", ROOT / "run_v20_crossval_eval.py",
          ROOT / "docs/Findings_v2.0_crossval.md"] + \
         list((ROOT / "results/familyL_prior_cache").glob("*.json")) + \
         list((ROOT / "results/gt2_attacker_cache").glob("*.json")) + \
         [ROOT / "results/deposon_v20_crossval.json"]:
    if watch in p.read_text(encoding="utf-8", errors="ignore"):
        leak.append(str(p))
check("横向对比资产无密钥前缀", not leak, str(leak[:3]))

# 5. pytest
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
mm = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and mm is not None, (mm.group(0) if mm else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
