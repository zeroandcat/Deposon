#!/usr/bin/env python3
# verifier/v19 — 综合文档（Deposon×复杂思维×互补共进）验收（v18 冻结不可变）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

fd = (ROOT / "docs/SYNTHESIS_mind_game.md").read_text(encoding="utf-8")
check("综合文档存在且 ≥3500字", len(fd) > 3500, f"{len(fd)}B")
# 三部结构
for kw in ["映射下的复杂思维", "映射下的复杂行为", "互补矩阵"]:
    check(f"含「{kw}」", kw in fd)
# 每条映射有证据锚（反空泛纪律）
for kw in ["E9.1", "锚定效应", "GT-2", "E9.2", "GT-4", "Pigou", "β=2.12",
           "同源污染", "GT-3", "E9.4", "19.6%"]:
    check(f"证据锚「{kw}」", kw in fd)
# 互补五桥
for kw in ["机制选择器", "基线二维评估", "协议即机制", "裁判独立性公理", "双重门控"]:
    check(f"共进桥「{kw}」", kw in fd)
# 行动清单可执行
check("共进行动清单 ≥4 条", fd.count("**势阱深度测量**") + fd.count("**基线双指标制**")
      + fd.count("**协议审计三问**") + fd.count("**GT-3 跨模型先验**")
      + fd.count("**双重门控声明**") >= 4)
# 既有资产未被改动（抽锁）
import hashlib
check("1.X CN 论文零改动", hashlib.md5(
    (ROOT / "paper/deposon_paper_v1.md").read_bytes()).hexdigest()
    == "7c22c9f8960787792e6dc14a4f06d8d0")
# 红线
watch = "sk-" + "kimi-"
check("文档无密钥前缀", watch not in fd)
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1800)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-200:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
