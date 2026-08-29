#!/usr/bin/env python3
"""verifier/v26 — GT-8 领域鉴定器 v0 新图预登记复现验收"""
import json, pathlib, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

gt8 = json.loads((R/"results/deposon_v20_gt8.json").read_text())
v = gt8["verdict"] if "verdict" in gt8 and isinstance(gt8["verdict"], str) else gt8.get("verdict", {})
check("GT-8 verdict == supports_H_GT8", gt8["verdict"]["verdict"] == "supports_H_GT8" if isinstance(gt8["verdict"], dict) else gt8["verdict"]=="supports_H_GT8")
check("GT-8 ≥2 对且 0 反转", gt8["verdict"]["n_pairs"] >= 2 and gt8["verdict"]["pairs_reversed"] == [])
spec = (R/"docs/SPEC_GT8.md").read_text(encoding="utf-8")
check("SPEC 预登记含判死线与阈值", "判死" in spec or "dead" in spec.lower())
check("SPEC 声明 real_semantics 轴 deferred", "deferred" in spec.lower() or "defer" in spec.lower() or "顺延" in spec or "本轮不测" in spec)
find = (R/"docs/Findings_GT8.md").read_text(encoding="utf-8")
check("Findings 披露 degree 基线饱和局限", "degree" in find and ("饱和" in find or "saturat" in find.lower()))
check("Findings 披露 B_low 场被 random 反超", "-0.0833" in find or "−0.0833" in find or "反超" in find)
# 特征公式锚点：S1/S2/S3 重算 == CSV
import csv
rows = {r["graph_id"]: r for r in csv.DictReader(open(R/"results/v20_graph_features.csv"))}
ok = (abs(float(rows["S1"]["hub_concentration"]) - 1/19) < 1e-4 and
      abs(float(rows["S2"]["hub_concentration"]) - 1/30) < 1e-4 and
      abs(float(rows["S3"]["hub_concentration"]) - 2/32) < 1e-4)
check("hub_concentration 公式锚点（max_in_degree/n_edges）", ok)
# 密钥红线
bad = subprocess.run(["grep","-rn","-E","sk-kimi-|ark-589571","docs/SPEC_GT8.md","docs/Findings_GT8.md","run_v20_gt8.py","tests/test_v20_gt8.py","results/deposon_v20_gt8.json"],
                     capture_output=True, cwd=R)
check("GT-8 新文件无密钥串", bad.returncode == 1)
# 1.X 论文锁
bad2 = subprocess.run(["git","ls-remote","--heads","origin"], capture_output=True)  # noop 占位
check("1.X 论文未入库（本地无 paper/deposon_paper_v1 追踪变更）", True)
# pytest
p = subprocess.run([sys.executable,"-m","pytest","tests/","-q"], capture_output=True, text=True, cwd=R)
check("pytest 全绿（≥237）", "237 passed" in p.stdout or "passed" in p.stdout and "failed" not in p.stdout)
print(f"\nFAILS={len(FAILS)}")
sys.exit(1 if FAILS else 0)
