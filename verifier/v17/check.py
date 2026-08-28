#!/usr/bin/env python3
# verifier/v17 — 算法加固（防超时）验收（v16 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 加固模块与验证产物
check("deposon_fast.py 存在", (ROOT / "deposon_fast.py").exists())
fc = json.load(open(ROOT / "results/deposon_v20_fastcheck.json"))
f1 = fc["F1_equivalence"]
check("F1 数值等价（max_abs_diff<1e-10）", f1["equivalent"] is True
      and f1["max_abs_diff"] < 1e-10 and f1["rank_mismatch"] == 0)
check("F2 轨迹共享提速 ≥1.2×", fc["F2_speedup"]["speedup_x"] >= 1.2,
      f"{fc['F2_speedup']['speedup_x']}×")
f3 = fc["F3_scaling"]
check("F3 缩放无爆炸（N=150 ≤0.5s/任务）",
      f3["S6_n150"]["sec_per_task"] <= 0.5, f"{f3['S6_n150']['sec_per_task']}")

# 2. 基线归纳终态
b = json.load(open(ROOT / "results/deposon_v20_baselines.json"))
check("基线终态 ≤250s（504s 已降）", b["runtime_sec"] <= 250, f"{b['runtime_sec']}s")
from collections import Counter
c = Counter(e["arm"] for e in b["boss_events"])
check("BOSS 复归诚实 6 事件（tfidf×5+CN×1）", len(b["boss_events"]) == 6
      and c.get("ngram_tfidf_cosine") == 5 and c.get("common_neighbors") == 1)
check("field_mean 15/20 第一", sum(
    1 for g, v in b["per_graph"].items()
    if all((v["field_mean"]["named"] or -1) >= (v[a]["named"] or -1)
           for a in v if a != "field_mean")) == 15)
check("转导泄漏教训披露", any("泄漏" in h for h in b["honesty"]))
check("双预算在案（cheap+full refs）", "n2v_budgets" in b and "node2vec_full" in
      json.dumps(b["per_graph"].get("S6", {})))

# 3. 早停拒绝记录
fd = (ROOT / "docs/Findings_v2.0_hardening.md").read_text(encoding="utf-8")
for kw in ["早停", "测试后拒绝", "泄漏事故", "1.34×", "162s", "归纳", "提速不得越过协议纯度"]:
    check(f"Hardening 文档含「{kw}」", kw in fd)

# 4. 密钥红线与 pytest（200 项）
watch = "sk-" + "kimi-"
leak = [str(p) for p in [ROOT / "deposon_fast.py", ROOT / "run_v20_fastcheck.py",
        ROOT / "run_v20_baselines.py", ROOT / "tests/test_fast.py",
        ROOT / "docs/Findings_v2.0_hardening.md"]
        if watch in p.read_text(encoding="utf-8", errors="ignore")]
check("本轮资产无密钥前缀", not leak, str(leak[:3]))
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 200 全绿", r.returncode == 0 and m is not None
      and int(m.group(1)) >= 200, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
