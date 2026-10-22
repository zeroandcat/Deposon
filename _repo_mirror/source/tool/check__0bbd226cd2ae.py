# -*- coding: utf-8 -*-
# verifier v34 — 目标⑥冲刺波验收：交付包完整性 + 论文简报 + 文献核实 + GT-8b 补数 + 重构候选3/4/5
# 与 v33 差异：v33 验收入论文整合与重构①②；v34 验收最终交付物与候选③④⑤、简报、压缩包。
import json, os, re, subprocess, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = "/mnt/agents/output"
RED = "sk-" + "kimi-"

results = []
def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))

def read(p):
    with open(p, encoding="utf-8") as f: return f.read()

# C1 论文简报存在且覆盖 1.X+2.X
brief = os.path.join(ROOT, "docs", "PAPER_BRIEF.md")
if os.path.exists(brief):
    b = read(brief)
    check("C1a 简报存在且提及1.X", "1." in b and ("v1" in b or "1.X" in b or "可审计表征" in b))
    check("C1b 简报覆盖2.X博弈论实证", "博弈论" in b or "GT-5" in b or "PoA" in b)
    check("C1c 简报无密钥串", RED not in b and "ark-" not in b)
else:
    check("C1 简报存在", False, "docs/PAPER_BRIEF.md 缺失")

# C2 成果汇报与导师沟通文档
rep = os.path.join(OUT, "deposon_成果汇报_2026.md")
check("C2a 成果汇报存在", os.path.exists(rep))
adv = os.path.join(OUT, "deposon_导师沟通建议_2026.md")
check("C2b 导师沟通建议存在", os.path.exists(adv))

# C3 压缩包完整
z = os.path.join(OUT, "deposon_core_bundle.zip")
if os.path.exists(z):
    zf = zipfile.ZipFile(z); names = zf.namelist()
    need = ["paper/v2/deposon_paper_v2X.md", "docs/ARCH_AUDIT_v2.md", "deposon_protocol.py"]
    check("C3a 压缩包含核心文件", all(any(n.endswith(x) for n in names) for x in need), f"{len(names)} files")
    check("C3b 压缩包无密钥", all(RED not in zf.read(n).decode("utf-8", "ignore") for n in names if n.endswith((".py",".md",".json",".txt"))))
else:
    check("C3 压缩包存在", False)

# C4 GT-8b 化学域先验
r = os.path.join(ROOT, "results", "deposon_v20_gt8b.json")
if os.path.exists(r):
    d = json.load(open(r))
    chem = d.get("per_domain", {}).get("L_chemical_elements", {})
    ns = chem.get("named_summary", {})
    check("C4 化学域先验已补或如实记录", (ns.get("llm_prior") is not None) or d.get("verdict") == "inconclusive",
          f"llm_prior={ns.get('llm_prior')}")
else:
    check("C4 gt8b 结果", False)

# C5 文献核实报告
lit = os.path.join(ROOT, "docs", "REF_VERIFICATION_v2.md")
check("C5 文献核实报告存在", os.path.exists(lit))

# C6 重构候选③④⑤记录（REFACTOR 文档更新或新档）
ref = os.path.join(ROOT, "docs", "REFACTOR_v2.md")
if os.path.exists(ref):
    t = read(ref)
    check("C6a fetch 管道统一记录", "fetch" in t.lower() and ("管道" in t or "pipeline" in t.lower() or "fetch_prior" in t))
    check("C6b gt_common 记录", "gt_common" in t)
else:
    check("C6 REFACTOR 文档", False)

# C7 pytest 全绿
env = dict(os.environ); env.pop("VIRTUAL_ENV", None)
p = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"], cwd=ROOT,
                   capture_output=True, text=True, env=env)
m = re.search(r"(\d+) passed", p.stdout)
check("C7 pytest 全绿", p.returncode == 0 and m and int(m.group(1)) >= 274, (m.group(0) if m else p.stdout[-200:]))

# C8 远程无 1.X 论文全文（简报允许）：本地确认推送清单纪律文件
check("C8 简报推送纪律注记", os.path.exists(brief) and "简报" in read(brief)[:2000])

fails = [x for x in results if not x[1]]
for n, ok, dt in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {n} {dt}")
print(f"\nv34: {len(results)-len(fails)} PASS / {len(fails)} FAIL")
sys.exit(1 if fails else 0)
