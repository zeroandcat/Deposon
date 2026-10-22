#!/usr/bin/env python3
# verifier/v15 — 基线注册表 + BOSS 扫描 + CoT 收编 + 向量属性审计验收（v14 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 注册表与产物
reg = (ROOT / "docs/BASELINE_REGISTRY.md").read_text(encoding="utf-8")
for kw in ["Common Neighbors", "Preferential Attachment", "PageRank",
           "Katz", "Node2Vec", "TF-IDF", "直接 CoT", "大 BOSS 测试", "KGE"]:
    check(f"注册表含「{kw}」", kw in reg)
for p in ["results/deposon_v20_baselines.json", "results/deposon_v20_cot_quiz.json",
          "results/deposon_v20_vector_audit.json"]:
    check(f"产物存在 {Path(p).name}", (ROOT / p).exists())

# 2. BOSS 扫描锚点
b = json.load(open(ROOT / "results/deposon_v20_baselines.json"))
check("boss_alert=True（如实触发）", b["boss_alert"] is True)
arms_bossed = {e["arm"] for e in b["boss_events"]}
check("tfidf 与 common_neighbors 双 BOSS 在案",
      "ngram_tfidf_cosine" in arms_bossed and "common_neighbors" in arms_bossed)
check("field_mean 仍 15/20 第一", sum(
    1 for g, v in b["per_graph"].items()
    if all((v["field_mean"]["named"] or -1) >= (v[a]["named"] or -1)
           for a in b["new_arms"])) == 15)
check("node2vec 浅近似标注", any("浅近似" in h or "非完整" in h for h in b["honesty"]))

# 3. CoT 收编锚点
c = json.load(open(ROOT / "results/deposon_v20_cot_quiz.json"))
check("CoT 题库准确率 0.925", abs(c["overall_cot_accuracy"] - 0.925) < 1e-9)
check("CoT n_items=40", c["n_items"] == 40)
check("CoT 信息通道差异披露", any("信息通道" in h for h in c["honesty"]))

# 4. 向量属性审计锚点
v = json.load(open(ROOT / "results/deposon_v20_vector_audit.json"))
check("向量审计 1740 任务", v["n_tasks"] == 1740)
check("向量审计全过（0 违规 ×4 项）", v["all_pass"] is True
      and all(x == 0 for x in v["violation_counts"].values()))

# 5. 文档与红线
fd = (ROOT / "docs/Findings_v2.0_boss.md").read_text(encoding="utf-8")
for kw in ["BOSS", "tfidf", "92.5%", "单纯形", "1740"]:
    check(f"BOSS 文档含「{kw}」", kw in fd)
watch = "sk-" + "kimi-"
leak = [str(p) for p in [ROOT / "run_v20_baselines.py", ROOT / "run_v20_cot_fetch.py",
        ROOT / "run_v20_vector_audit.py", ROOT / "docs/Findings_v2.0_boss.md",
        ROOT / "docs/BASELINE_REGISTRY.md",
        ROOT / "results/deposon_v20_baselines.json",
        ROOT / "results/deposon_v20_cot_quiz.json",
        ROOT / "results/deposon_v20_vector_audit.json"]
        if watch in p.read_text(encoding="utf-8", errors="ignore")]
check("本轮资产无密钥前缀", not leak, str(leak[:3]))

# 6. pytest
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
