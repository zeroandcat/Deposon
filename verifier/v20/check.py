#!/usr/bin/env python3
# verifier/v20 — 光子硬件映射验收（v19 冻结不可变）
import json, re, subprocess, sys, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 模块与产物
check("deposon_photonics.py 存在", (ROOT / "deposon_photonics.py").exists())
d = json.load(open(ROOT / "results/deposon_v20_photonics.json"))
check("范围声明（非流片/TYPICAL）", "非流片" in d["scope"] and "TYPICAL" in d["scope"])

# 2. P1 自洽性
p1 = d["P1_equivalence"]
check("P1 守恒偏差=0", p1["conservation_err"] == 0.0)
check("P1 S6 直接 named 9/9 可达", p1["s6_direct_named_reachable"] == "9/9")

# 3. P2 真实边界
p2 = d["P2_feasibility"]
check("P2 可探测 14/22（真实边界非全过）", p2["detectable_graphs"] == "14/22")
check("P2 边界注明每跳 dB 与跳数规则", "2.9 dB" in p2["feasibility_note"]
      and "14 跳" in p2["feasibility_note"])
check("P2 逐图明细含 loss_db 与 detectable", all(
    "loss_db" in v and "detectable" in v for v in p2["per_graph"].values()))

# 4. P3/P4
p3 = d["P3_topology_optimization"]
check("P3 三拓扑在案", set(p3["table"].keys()) ==
      {"naive_per_edge_mzi", "shared_bus_ring", "hybrid_tree"})
check("P3 指标最优 vs 工程推荐双口径", "工程推荐" in p3["note"]
      and "shared_bus_ring" in p3["recommended"])
p4 = d["P4_ramp_sensitivity"]
check("P4 σ=0.2 偏差在案且反馈稳相标注", p4["sensitivity"][-1]["sigma"] == 0.2
      and "反馈稳相" in p4["note"])

# 5. 文档与红线
fd = (ROOT / "docs/Findings_v2.0_photonics.md").read_text(encoding="utf-8")
for kw in ["PCM", "ring 谐振器", "14/22", "14 跳", "非流片", "TYPICAL", "跨层互证"]:
    check(f"Photonics 文档含「{kw}」", kw in fd)
watch = "sk-" + "kimi-"
leak = [str(p) for p in [ROOT / "deposon_photonics.py", ROOT / "run_v20_photonics.py",
        ROOT / "docs/Findings_v2.0_photonics.md",
        ROOT / "results/deposon_v20_photonics.json"]
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
