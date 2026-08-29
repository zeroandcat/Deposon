#!/usr/bin/env python3
# verifier/v25 — 图语言纪律修复 + GT-7 验收（v24 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 图语言纪律
en = (ROOT / "paper/deposon_paper_v1_en.md").read_text(encoding="utf-8")
cn = (ROOT / "paper/deposon_paper_v1.md").read_text(encoding="utf-8")
check("EN 论文引用英文图", "fig1_architecture_en.png" in en
      and "fig1_architecture.png" not in en)
check("CN 论文引用中文图且未动", "fig1_architecture.png" in cn)
check("英文图文件存在且非空",
      (ROOT / "paper/fig1_architecture_en.png").stat().st_size > 100_000)
pol = (ROOT / "paper/FIGURE_LANGUAGE_POLICY.md").read_text(encoding="utf-8")
check("图语言纪律文件在库", "英文" in pol and "_en" in pol and "混用" in pol)
check("pdfbuild EN HTML 已同步英文图",
      "fig1_architecture_en.png" in (ROOT / "paper/pdfbuild/v1_en.html").read_text(encoding="utf-8"))

# 2. GT-7 锚点
gt7 = json.load(open(ROOT / "results/deposon_v20_gt7.json"))
check("GT-7 判定 mixed 如实", gt7["verdict"]["verdict"] == "mixed")
check("GT-7 前沿图 2/4（mixed 口径锚点）", gt7["verdict"]["n_graphs_with_frontier_temp"] == 2
      and gt7["verdict"]["frac_graphs_with_frontier_temp"] == 0.5)
txt = json.dumps(gt7, ensure_ascii=False)
check("GT-7 温度依赖披露", "alpha" in txt.lower() or "α" in txt)

# 3. 重构文档更新
gt = (ROOT / "docs/GT_RECONSTRUCTION.md").read_text(encoding="utf-8")
check("重构文档含 GT-7 与双赢不成立", "GT-7" in gt and "不可兼得" in gt)

# 4. 红线与回归
leak = []
for w in ["sk-" + "kimi-", "ark-" + "589571"]:
    for p in [ROOT / "run_v20_gt7.py", ROOT / "paper/FIGURE_LANGUAGE_POLICY.md",
              ROOT / "paper/deposon_paper_v1_en.md", ROOT / "docs/GT_RECONSTRUCTION.md"]:
        if w in p.read_text(encoding="utf-8", errors="ignore"):
            leak.append(str(p))
check("本轮资产双 key 红线", not leak, str(leak[:3]))
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿（≥228）", r.returncode == 0 and m and int(m.group(1)) >= 228,
      (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
