#!/usr/bin/env python3
# verifier/v21 — 深探整改验收（v20 冻结不可变；v17/v20 erratum 由本版承接新锚点）
import json, re, subprocess, sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. C1 斩杀线机械对照（新增强制项：文档-数据一致）
ev = json.load(open(ROOT / "results/deposon_v20_corpus_eval.json"))
kl = ev["verdicts"]["kill_lines"]["H_A_dead"]
check("斩杀线 triggered=true 在案（22 图 4 反转）", kl["triggered"] is True
      and kl["n_reversals_vs_random"] >= 4, str(kl["reversals_vs_random"]))
corr = (ROOT / "docs/Findings_v2.0_corrections.md").read_text(encoding="utf-8")
check("更正文档确认判死（不再称未触发）", "判死" in corr and "未触发" not in corr.split("判死")[0][-200:])
check("存活主张收缩（degree 稳健 + 边界证据）", "degree" in corr and "边界" in corr)

# 2. C2 撤回
check("C2 撤回声称在案", "撤回" in corr and "top-1" in corr)

# 3. C3 BOSS 门槛
b = json.load(open(ROOT / "results/deposon_v20_baselines.json"))
check("BOSS 门槛 ≥3 金边落盘", b.get("boss_gate_edges") == 3)
gated = [e for e in b["boss_events"] if e["gate_pass"]]
check("门槛后 BOSS = 6 事件（含 L_PM 三臂）", len(gated) == 6 and sum(
    1 for e in gated if e["graph_id"] == "L_project_management") == 3)
check("被拦事件保留（S5 抽签候选）", any(
    e["graph_id"] == "S5" for e in b["boss_events_below_gate"]))
check("tfidf 抽签披露（伪装随机臂）", any("伪装随机臂" in h for h in b["honesty"]))

# 4. C4 光子更正
ph = json.load(open(ROOT / "results/deposon_v20_photonics.json"))
p2 = ph["P2_feasibility"]
check("P2 可探测 18/22", p2["detectable_graphs"] == "18/22")
check("阈值 ≈27 跳且修正史在案", "27 跳" in p2["feasibility_note"]
      and "NEP 单位错" in p2["feasibility_note"])
hops = {k: v["path_hops"] for k, v in p2["per_graph"].items()}
check("真最长路径（S1_n60=59 跳）", hops.get("S1_n60") == 59)

# 5. C5 工程
am = (ROOT / "docs/SPEC_v2.0_amendment1.md").read_text(encoding="utf-8")
for kw in ["判死", "撤回", "margin ≥ 3", "18/22", "追认登记", "孤儿哨兵", "erratum"]:
    check(f"修正案含「{kw}」", kw in am)
src = (ROOT / "run_v20_familyL_ingest.py").read_text(encoding="utf-8")
check("摄入即建索引（build_index 调用）", "build_index(corpus_dir)" in src)
mc = (ROOT / "mindmap_corpus_v20.py").read_text(encoding="utf-8")
check("孤儿哨兵在案", "corpus orphan graphs" in mc)
check("run_v17_fusion_fix.py 本地在库", (ROOT / "run_v17_fusion_fix.py").exists())

# 6. 红线与回归
watch = "sk-" + "kimi-"
leak = [str(p) for p in [ROOT / "docs/SPEC_v2.0_amendment1.md",
        ROOT / "docs/Findings_v2.0_corrections.md",
        ROOT / "results/deposon_v20_photonics.json",
        ROOT / "results/deposon_v20_baselines.json"]
        if watch in p.read_text(encoding="utf-8", errors="ignore")]
check("本轮资产无密钥前缀", not leak, str(leak[:3]))
check("1.X CN 论文零改动", hashlib.md5(
    (ROOT / "paper/deposon_paper_v1.md").read_bytes()).hexdigest()
    == "7c22c9f8960787792e6dc14a4f06d8d0")
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
