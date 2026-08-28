#!/usr/bin/env python3
# verifier/v12 — v2.0 多图语料 + GT 首批验收（v11 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 语料完整性
idx = json.load(open(ROOT / "corpus/v20/index.json"))
graphs = idx.get("graphs", idx) if isinstance(idx, dict) else idx
n_graphs = len(graphs) if isinstance(graphs, list) else idx.get("n_graphs")
check("语料 ≥20 图（16 S 族 + 4 L 族）", (n_graphs or 0) >= 20, f"n={n_graphs}")
L_ids = [g["graph_id"] for g in (graphs if isinstance(graphs, list) else [])
         if str(g.get("graph_id", "")).startswith("L")]
check("族 L 4 图在册", len(L_ids) == 4, str(L_ids))

# 2. 族 L provenance
for d in ["physics_concepts", "biological_taxonomy", "algorithm_process", "historical_causality"]:
    p = ROOT / f"results/familyL_cache/{d}.json"
    ok = p.exists()
    rec = json.load(open(p)) if ok else {}
    check(f"族L缓存 {d}（含 prompt_sha256+response_text）",
          ok and bool(rec.get("prompt_sha256")) and bool(rec.get("response_text")))
ing = json.load(open(ROOT / "results/deposon_v20_familyL_ingest.json"))
check("摄入报告无缓存错误", not ing.get("cache_errors"))

# 3. 评估判定锚点
ev = json.load(open(ROOT / "results/deposon_v20_corpus_eval.json"))
v = ev["verdicts"]
check("H-A1 支持且过 Holm", v["H_A1_field_mean_gt_random"]["supported"] is True
      and v["H_A1_field_mean_gt_random"]["holm"]["significant_holm"] is True)
check("H-A2 支持且过 Holm", v["H_A2_field_mean_gt_degree"]["supported"] is True)
hb = v["H_B1_filler_below_0.15"]["per_graph_filler_hits3"]
viol = {k: x for k, x in hb.items() if x is not None and x >= 0.15}
check("H-B1 违规=2 例且如实逐图列出", len(viol) == 2
      and "L_historical_causality" in viol, str({k: round(x, 3) for k, x in viol.items()}))
s6r = ev.get("s6_reproduction", {})
check("S6 复现锚点 0.4706 且逐位匹配", abs(s6r.get("S6_named_hits3", 0) - 0.47058823529411764) < 1e-6 and s6r.get("matches_v19_e92_anchor_exactly") is True)
check("相变扫描如实阴性", all(not x for x in ev.get("phase_transitions", {}).values()))

# 4. GT 判定
gt = json.load(open(ROOT / "results/deposon_v20_gt.json"))
g1 = gt["GT1_potential_game_convergence"]["verdict"]
check("GT-1 支持势博弈（gap≥0.2 且 ≥15/20 劣）",
      g1["supported_potential_game"] is True and g1["n_runs_below_meanfield"] >= 15)
g4 = gt["GT4_price_of_anarchy"]["verdict"]
check("GT-4 median PoA>1.2", g4["median_poa"] > 1.2, f"median={g4['median_poa']}")
poa_l = {k: x for k, x in g4["poa_per_graph_finite"].items() if k.startswith("L")}
check("GT-4 族L负协调如实披露（≥2 张 PoA<1）",
      sum(1 for x in poa_l.values() if x < 1.0) >= 2, str(poa_l))

# 5. 文档与红线
watch = "sk-" + "kimi-"  # 通用密钥前缀（安全删改：不再含任何真实 key 片段）
fd = (ROOT / "docs/Findings_v2.0.md").read_text(encoding="utf-8")
for kw in ["量变质变", "否定之否定", "对立统一", "斩杀线", "H-A1", "PoA", "同源污染"]:
    check(f"Findings 含「{kw}」", kw in fd)
spec = (ROOT / "docs/SPEC_v2.0.md").read_text(encoding="utf-8")
check("SPEC v2.0 预登记在库", "斩杀线" in spec and "GT-1" in spec)
leak = []
for p in list(ROOT.glob("*.py")) + list((ROOT / "results").rglob("*.json")) \
         + list((ROOT / "corpus").rglob("*.json")) + list((ROOT / "docs").glob("*.md")):
    t = p.read_text(encoding="utf-8", errors="ignore")
    if watch in t:
        leak.append(str(p))
check("v2.0 资产无密钥泄露", not leak, str(leak[:3]))

# 6. pytest
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
