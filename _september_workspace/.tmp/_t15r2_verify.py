# -*- coding: utf-8 -*-
"""Final verify T1.5r2 deliverables."""
import json
import hashlib
import re
from pathlib import Path

ROOT = Path("D:/私人资料/deposon-repo")

# 1. 落盘文件确认
files = {
    ".tmp/_t15r2_records.json": "T1.5r2 checkpoint",
    ".tmp/_t15r2_probe_log.json": "T1.5r2 probe log",
    "results/_v4_supp_t15r2_result.json": "T1.5r2 aggregate result",
    "results/_v4_supp_t15r2_executor.py": "T1.5r2 executor",
}
print("=== 1. 落盘核验 ===")
for path, label in files.items():
    p = ROOT / path
    if not p.exists():
        print(f"MISSING: {path}")
        continue
    sha = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
    sz = p.stat().st_size
    print(f"  OK {path}  SHA-12={sha}  bytes={sz}  ({label})")

# 2. 既有件不应触动
print()
print("=== 2. 既有件不动核验 ===")
frozen = {
    "results/_v4_supp_t15_executor.py": "558E635F9BA6",
    "results/_v4_supp_t15_result.json": "6B47D389B7AE",
    "results/_v4_supp_t15_verdict.md": "52C985429C91",
    "results/_v4_supp_prereg_v02_add_T15r2_2026_09_26.md": "883DCED872B4",
}
for path, expected_sha in frozen.items():
    p = ROOT / path
    if not p.exists():
        print(f"WARN: {path} not found")
        continue
    sha = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
    match = "OK" if sha.lower() == expected_sha.lower() else "MISMATCH"
    print(f"  {match} {path}  SHA-12={sha} (expected {expected_sha})")

# 3. T1.5 records 不动
print()
print("=== 3. T1.5 records (state anchor) 不动 ===")
p = ROOT / ".tmp/_t15_records.json"
sha = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
with open(p, encoding="utf-8") as f:
    rs = json.load(f)
n_ok = sum(1 for r in rs if r.get("ok"))
print(f"  T1.5 records: {len(rs)} records  ok={n_ok} fail={len(rs)-n_ok}  SHA-12={sha}")

# 4. T1.5r2 records 完整
print()
print("=== 4. T1.5r2 records 完整 (62 calls) ===")
p = ROOT / ".tmp/_t15r2_records.json"
sha = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
with open(p, encoding="utf-8") as f:
    rs = json.load(f)
n_ok = sum(1 for r in rs if r.get("ok"))
print(f"  T1.5r2 records: {len(rs)} records  ok={n_ok} fail={len(rs)-n_ok}  SHA-12={sha}")
from collections import Counter
by_cell = Counter(r["cell_idx"] for r in rs)
by_teacher = Counter(r["teacher"] for r in rs)
print(f"  by cell: {dict(sorted(by_cell.items()))}")
print(f"  by teacher: {dict(by_teacher)}")
n_rerun = sum(1 for r in rs if r.get("rerun_2calls"))
print(f"  rerun_2calls count: {n_rerun} (expect 2: coze/S5/r0 cell 2 + GLM_1/L_geography_world/r1 cell 3)")

# 5. result.json 关键字段
print()
print("=== 5. result.json 关键字段 ===")
p = ROOT / "results/_v4_supp_t15r2_result.json"
with open(p, encoding="utf-8") as f:
    r = json.load(f)
md = r["metadata"]
print(f"  schema: {md['schema']}")
print(f"  date_label: {md['date_label']}")
ba = md.get("T15r2_pi_authorization_basis", "")
print(f"  has +60 calls: {'+60 calls' in ba}")
print(f"  has §3.4: {'§3.4' in ba}")
print(f"  has §4.4: {'§4.4' in ba}")

print()
ov = r["overall_verdict"]
print(f"  overall verdict: {ov['t15r2_overall_verdict']}")
print(f"  K-T1-S1/S3 any_hit (False = PASS): {ov['any_t15r2_kill_line_hit']}")

ks = r["kill_lines_T15r2"]
print(f"  K-T1-S1 any_hit: {ks['K-T1-S1_temperature_flip_T15r2reuse']['any_hit']}")
print(f"  K-T1-S3 hit: {ks['K-T1-S3_robustness_confirm_T15r2reuse']['hit']}")
print(f"  K-T1-S3 all_cells_below: {ks['K-T1-S3_robustness_confirm_T15r2reuse']['all_cells_below_threshold']}")
print(f"  K-N11-N1_T1relax verdict: {ks['K-N11-N1_T1relax_N10_ground_cause_eliminated']['verdict']}")

# 6. per_cell_summary 简要
print()
print("=== 6. per-cell summary ===")
for ci_str, cs in r["per_cell_summary"].items():
    jmed = cs["cell_j_median_5teachers"]
    jmed_ne = cs["cell_j_median_5teachers_nonempty"]
    same_avgs = [x.get("same_caption_j_median_nonempty") for x in cs["per_teacher"] if x.get("same_caption_j_median_nonempty") is not None]
    cross_avgs = [x.get("cross_caption_j_median_nonempty") for x in cs["per_teacher"] if x.get("cross_caption_j_median_nonempty") is not None]
    same_avg = round(sum(same_avgs)/len(same_avgs), 4) if same_avgs else None
    cross_avg = round(sum(cross_avgs)/len(cross_avgs), 4) if cross_avgs else None
    n_pairs = cs["n_pairs_total_all"]
    n_pairs_ne = cs["n_pairs_total_nonempty"]
    n_pairs_ee = cs["n_pairs_total_empty_empty"]
    print(f"  cell {ci_str} ({cs['dim']}/t={cs['temperature']}): j_med={jmed}, j_med_ne={jmed_ne}, "
          f"same_ne={same_avg}, cross_ne={cross_avg}, "
          f"pairs={n_pairs} (ne={n_pairs_ne}, ee={n_pairs_ee})")

# 7. K-N11-N1_T1relax per_teacher 字面确认
print()
print("=== 7. K-N11-N1_T1relax per cell 字面 PASS 确认 ===")
for ci_str, cs in r["per_cell_summary"].items():
    k_relax = cs["kill_lines"]["K-N11-N1_T1relax"]
    n_pass = sum(1 for t, p in k_relax["per_teacher"].items() if p["pass"])
    n_total = len(k_relax["per_teacher"])
    n_pairs = [p["n_pairs"] for p in k_relax["per_teacher"].values()]
    print(f"  cell {ci_str} ({cs['dim']}/t={cs['temperature']}): {n_pass}/{n_total} 教师 N≥10; n_pairs per cell per teacher: {n_pairs};  verdict: {k_relax['verdict']}")

# 8. 跨温度 J 中位标准差
print()
print("=== 8. 跨温度 J 中位标准差 (T1.5 §5 稳健性度量) ===")
for k, v in r["cross_temp_std_per_dim"]["all_pairs"].items():
    print(f"  dim={k}: stdev all_pairs={v} | stdev nonempty={r['cross_temp_std_per_dim']['nonempty_pairs'].get(k)}")

# 9. key 形态自扫
print()
print("=== 9. key 形态自扫 (R4) ===")
patterns = [
    ("sk_literal", re.compile(r"(?i)sk-[A-Za-z0-9_\-]{20,}")),
    ("AIza_literal", re.compile(r"(?i)AIza[0-9A-Za-z_\-]{30,}")),
    ("Bearer_token", re.compile(r"(?i)Bearer\s+[A-Za-z0-9]{20,}")),
]
for path in [".tmp/_t15r2_records.json", "results/_v4_supp_t15r2_result.json", "results/_v4_supp_t15r2_executor.py"]:
    p = ROOT / path
    text = p.read_text(encoding="utf-8", errors="ignore")
    hits = []
    for name, pat in patterns:
        n = len(pat.findall(text))
        if n > 0:
            hits.append((name, n))
    status = "CLEAN" if not hits else f"WARN: {hits}"
    print(f"  {path}: {status}")

# 10. 关键诚实声明验证
print()
print("=== 10. 诚实声明字段 ===")
hd = r["honesty_disclosures"]
print(f"  'succeeded ≠ 跑完' 老实交代: {'落盘核验' in hd['succeeded_not_means_completed']}")
print(f"  watchdog 字面 600s: {'600s' in hd['watchdog_limit']}")
print(f"  skill 缺位老实交代: {'Local skill not found' in hd['skill_absence']}")
print(f"  T1.5 构造失灵族补正: {'构造失灵族' in hd['construction_fix_disclosure']}")
print(f"  T1.5r2 定位约束: {len(hd['T15r2_locale_constraint_disclosure']) > 200}")
