#!/usr/bin/env python3
# verifier/v11 — v1.9 充分收尾 + v2.X 博弈论转向验收（v10 冻结不可变）
import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# 1. 收尾审计产物
sec = json.load(open(ROOT / "audits_security.json"))
check("安全扫描 critical/high=0", sec["summary"]["critical"] == 0 and sec["summary"]["high"] == 0)
check("密钥泄露=0", len(sec.get("secrets", {}).get("findings", [])) == 0)
dh = json.load(open(ROOT / "audits_dataset_health.json"))
score = dh.get("overall_score") or dh.get("total_score") or dh.get("summary", {}).get("total_score")
check("数据健康 ≥90", (score or 0) >= 90, f"score={score}")
out = json.load(open(ROOT / "audits_outliers.json"))
na = out.get("needs_attention") or out.get("classified", {}).get("needs_attention") or []
check("异常扫描 需关注=0", len(na) == 0)
check("审计输入表归档", (ROOT / "results/v19_edges_audit_input.csv").exists())

# 2. 转向文档
doc = (ROOT / "docs/CLOSURE_v19_and_v2X_gametheory.md").read_text(encoding="utf-8")
for kw in ["量变质变", "否定之否定", "对立统一", "势博弈", "cheap talk", "机制设计",
           "GT-1", "GT-2", "GT-3", "GT-4", "斩杀线", "大材小用", "落到实处", "与死同行"]:
    check(f"转向文档含「{kw}」", kw in doc)

# 3. 既有资产未被破坏
check("Roadmap v2X 仍在", (ROOT / "docs/Roadmap_v2X.md").exists())
check("LESSONS 仍在", (ROOT / "docs/LESSONS_v19.md").exists())
check("SPEC v1.9 仍在", (ROOT / "docs/SPEC_v1.9.md").exists())

# 4. 密钥红线（含新 key 模式，拼接构造避免自匹配）
new_key_frag = "sk-" + "kimi-7BI2"
leak_found = []
for p in ROOT.rglob("*"):
    if p.is_file() and p.suffix in (".py", ".md", ".json", ".csv", ".txt") and "verifier" not in str(p):
        try:
            t = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if new_key_frag in t or ("sk-" + "kimi-7u1h") in t:
            leak_found.append(str(p))
check("全仓库无两个 key 泄露", not leak_found, str(leak_found[:3]))
check("转向文档无 key", new_key_frag not in doc and ("sk-" + "kimi-") not in doc)

# 5. pytest 仍全绿
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1200)
import re
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
