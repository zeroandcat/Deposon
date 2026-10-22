#!/usr/bin/env python3
# verifier/v22 — GT-3a 跨评估者验收（v21 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. SPEC 与缓存 provenance
spec = (ROOT / "docs/SPEC_GT3.md").read_text(encoding="utf-8")
check("SPEC_GT3 预登记在库（含斩杀线/预算/修正案）",
      "H_GT3_dead" in spec and "修正案 A1" in spec and "预算实耗 28" in spec)
caches = sorted((ROOT / "results/gt3_prior_cache").glob("*.json"))
check("GT3 缓存 12 个（6 域×2 评估者）", len(caches) == 12, str(len(caches)))
for p in caches:
    rec = json.load(open(p))
    check(f"{p.name} provenance（sha+model+attempts 落盘）",
          bool(rec.get("prompt_sha256")) and bool(rec.get("model"))
          and "attempts" in rec)

# 2. 结果锚点
gt3 = json.load(open(ROOT / "results/deposon_v20_gt3.json"))
check("H_GT3 支持且斩杀线未触发",
      gt3["verdict"]["H_GT3_supported"] is True
      and gt3["verdict"]["H_GT3_dead_triggered"] is False)
check("Kendall W ≥ 0.5", gt3["kendall_W"] is not None and gt3["kendall_W"] >= 0.5,
      f"W={gt3['kendall_W']:.3f}")
check("失败 3 缓存如实披露（不静默剔除）", len(gt3["failures"]) == 3,
      str(sorted(gt3["failures"])))
check("预算超支 1 次如实披露", gt3["budget"]["overrun"] == 1
      and gt3["budget"]["actual_total_attempts"] == 28)
ok_rows = [r for r in gt3["per_domain"]]
n_win = sum(1 for r in ok_rows for e, v in r["evaluators"].items()
            if v.get("named_hits3") is not None
            and v["named_hits3"] > v["field_mean_named_hits3"])
n_eval = sum(1 for r in ok_rows for v in r["evaluators"].values()
             if v.get("named_hits3") is not None)
check("全部已评估单元 先验>场", n_win == n_eval and n_eval >= 14, f"{n_win}/{n_eval}")

# 3. 同源污染降级声明
check("GT-3a 降级声明在 honesty", any("GT-3b" in h for h in gt3["honesty"]))

# 4. 红线与回归
leak = []
watch = "sk-" + "kimi-"
for p in [ROOT / "run_v20_gt3_fetch.py", ROOT / "run_v20_gt3_eval.py",
          ROOT / "docs/SPEC_GT3.md", ROOT / "results/deposon_v20_gt3.json"] + caches:
    if watch in p.read_text(encoding="utf-8", errors="ignore"):
        leak.append(str(p))
check("GT3 资产无密钥前缀", not leak, str(leak[:3]))
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None,
      (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
