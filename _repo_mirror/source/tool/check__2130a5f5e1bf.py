# -*- coding: utf-8 -*-
# verifier v35 — 周一完备化波②：形式化判死检验 + GT-8c(Ark) real_semantics 扩样
# 与 v34 差异：v34 验收交付包；v35 验收博弈论定理化实证与 Ark 扩样。
import json, os, re, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
RED = "sk-" + "kimi-"
res = []
def check(n, ok, d=""): res.append((n, bool(ok), d))

# D1 形式化检验
p = os.path.join(ROOT, "run_v21_gtformal.py")
check("D1a run_v21_gtformal.py 存在", os.path.exists(p))
j = os.path.join(ROOT, "results", "deposon_v21_gtformal.json")
if os.path.exists(j):
    d = json.load(open(j))
    check("D1b 结果含 verdict", "verdict" in json.dumps(d)[:200000])
    check("D1c 无密钥", RED not in open(j).read())
else:
    check("D1 结果 JSON", False)
f = os.path.join(ROOT, "docs", "Findings_GT_FORMAL.md")
check("D1d Findings 存在", os.path.exists(f))

# D2 GT-8c(Ark)
s = os.path.join(ROOT, "docs", "SPEC_GT8C.md")
check("D2a SPEC_GT8C 存在", os.path.exists(s))
fs = os.path.join(ROOT, "run_v20_gt8c_fetch.py")
check("D2b fetch 脚本存在", os.path.exists(fs))
if os.path.exists(fs):
    t = open(fs).read()
    check("D2c fetch 用 Ark 端点且 key 仅 env", "ark.cn-beijing.volces.com" in t and "ARK_API_KEY" in t and RED not in t and "ark-589" not in t)
j2 = os.path.join(ROOT, "results", "deposon_v20_gt8c.json")
if os.path.exists(j2):
    d2 = json.load(open(j2))
    vd = d2.get("gt8c_verdict", {})
    check("D2d 判定在案", "verdict" in vd, str(vd.get("verdict")))
    check("D2e 域数≥2 有效", vd.get("n_valid_domains", 0) >= 2 or vd.get("verdict") == "inconclusive",
          f"n_valid={vd.get('n_valid_domains')}")
else:
    check("D2 gt8c 结果（fetch 后可缺失）", False, "fetch 未执行")

# D3 pytest 全绿
env = dict(os.environ); env.pop("VIRTUAL_ENV", None)
p3 = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"], cwd=ROOT, capture_output=True, text=True, env=env)
m = re.search(r"(\d+) passed", p3.stdout)
check("D3 pytest 全绿 ≥351", p3.returncode == 0 and m and int(m.group(1)) >= 351, m.group(0) if m else p3.stdout[-150:])

fails = [x for x in res if not x[1]]
for n, ok, d in res: print(f"[{'PASS' if ok else 'FAIL'}] {n} {d}")
print(f"\nv35: {len(res)-len(fails)} PASS / {len(fails)} FAIL")
sys.exit(1 if fails else 0)
