#!/usr/bin/env python3
"""verifier/v33 — 重构不变量（REFACTOR_v2）+ 整合包不变量（REVISION_LOG 第 20 条）验收"""
import pathlib, re, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

md = (R/"paper/v2/deposon_paper_v2X.md").read_text(encoding="utf-8")
log = (R/"paper/v2/REVISION_LOG_v2X.md").read_text(encoding="utf-8")
findings = (R/"docs/Findings_v2.0_photonics.md").read_text(encoding="utf-8")

# --- A1. pytest 全绿且总数 >=274
p = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q"], capture_output=True, text=True, cwd=R)
m = re.search(r"(\d+) passed", p.stdout)
check("A1 pytest 全绿且 >=274", "failed" not in p.stdout and "error" not in p.stdout and m and int(m.group(1)) >= 274)
print("  [pytest]", p.stdout.strip().splitlines()[-1] if p.stdout.strip() else p.stderr.strip()[:200])

# --- A2. row_normalize 唯一且在 deposon_protocol.py；退火循环体唯一
loop = "for _t in range(cfg.n_steps, 0, -1)"
rn_files = []
loop_hits = 0
for f in R.rglob("*.py"):
    if "verifier" in f.parts or "__pycache__" in f.parts:
        continue
    t = f.read_text(encoding="utf-8")
    if "def row_normalize" in t:
        rn_files.append(f.name)
    loop_hits += t.count(loop)
check("A2a def row_normalize 全仓仅 1 处且在 deposon_protocol.py", rn_files == ["deposon_protocol.py"])
check("A2b 退火循环体全仓仅 1 份", loop_hits == 1)

# --- A3. deposon_diffusion.py 统一入口 denoise；四文件无复制循环体
diff = (R/"deposon_diffusion.py").read_text(encoding="utf-8")
check("A3a deposon_diffusion.py 含统一入口 denoise", re.search(r"def denoise\b", diff) is not None)
copiers = [f for f in ("run_v19_meanfield.py", "deposon_fast.py", "run_v20_gt5.py", "run_v20_gt7.py")
           if loop in (R/f).read_text(encoding="utf-8")]
check("A3b 四文件不再含复制循环体", not copiers)

# --- A4. import 不破且对象 is 同一
code = (
    "import deposon_protocol as dp\n"
    "import run_v15_experiment, run_v16_llm_prior, run_v19_fullrank, run_v19_meanfield\n"
    "assert run_v15_experiment.row_normalize is dp.row_normalize\n"
    "assert run_v16_llm_prior.prior_score_matrix is dp.prior_score_matrix\n"
    "assert run_v19_fullrank.full_candidate_mask is dp.full_candidate_mask\n"
    "assert run_v19_meanfield.field_scores_init is dp.field_scores_init\n"
    "print('identity-ok')\n"
)
q = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True, cwd=R)
check("A4 既有 import 不破且对象 is 同一", q.returncode == 0 and "identity-ok" in q.stdout)
if q.returncode != 0:
    print("  [A4 stderr]", q.stderr.strip()[:300])

# --- B5. 附录 A 误标清除 + per_graph_detail.S6 追溯
app = md.split("Appendix")[-1]
check("B5a 附录 A 无 deposon_v20_gt5.json 误标", ("无 `deposon_v20_gt5.json`" not in app) and ("无 deposon_v20_gt5.json" not in app))
check("B5b 附录 A 含 per_graph_detail.S6 追溯", "per_graph_detail.S6" in app)

# --- B6. 正文各节内容（run2：按节标题切片，避免全文级 grep 误报）
def section(num):
    m = re.search(rf"^#+\s*{re.escape(num)}\s", md, re.M)
    if not m:
        return ""
    nxt = re.search(r"^#{1,3}\s", md[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(md)
    return md[m.start():end]
s65 = section("6.5")
s56 = section("5.6")
s64 = section("6.4")
s63 = section("6.3")
check("B6a §6.5 硬件同构可行性段含 18/22 与方向性", bool(s65) and "硬件" in s65 and "18/22" in s65 and "方向性" in s65)
check("B6b §5.6 含 1740 与 0 违规", bool(s56) and "1740" in s56 and "0 违规" in s56)
check("B6c §6.4 含 GT-2B 选项自由度教训", bool(s64) and "GT-2B" in s64 and "自由度" in s64)
check("B6d §6.3 含 λ=2 反场 artifact", bool(s63) and "λ=2" in s63 and "artifact" in s63.lower())

# --- B7. Findings photonics 18/22 主结论；14/22 仅允许在更正注记段
main = findings
i = main.find("更正注记")
if i >= 0:
    # 排除更正注记段（到下一个同级标题或文末）
    m2 = re.search(r"\n#{1,3}\s", main[i+1:])
    main = main[:i] + (main[i+1+m2.start():] if m2 else "")
check("B7 Findings_v2.0_photonics 主结论 18/22 且无 14/22（更正注记段除外）",
      "18/22" in main and "14/22" not in main)

# --- B8. gt3b/gt3c fetch 错误路径过 _sanitize
for fn in ("run_v20_gt3b_fetch.py", "run_v20_gt3c_fetch.py"):
    t = (R/fn).read_text(encoding="utf-8")
    raises = [ln for ln in t.splitlines() if "raise RuntimeError" in ln]
    check(f"B8 {fn} 错误路径过 _sanitize", "_sanitize(" in t and raises and all("_sanitize" in ln for ln in raises))

# --- B9. 口径词计数快照
base = {"判死": 9, "inconclusive": 14, "no_separation": 7, "consistency": 4, "探索性": 6, "观察性规律": 3, "待核": 19}
bad9 = {w: md.count(w) for w, n in base.items() if md.count(w) != n}
check("B9 口径词计数快照逐一对照（判死9/inconclusive14/no_separation7/consistency4/探索性6/观察性规律3/待核19）", not bad9)
if bad9:
    print("  [B9 偏差]", {w: (md.count(w), base[w]) for w in bad9})

# --- B10. References [1]-[59] 连续无缺无重
refs = re.findall(r"^\[(\d+)\]", md.split("References")[-1], re.M)
check("B10 References 编号 [1]-[59] 连续无缺无重",
      refs == [str(i) for i in range(1, 60)])

# --- B11. 全仓密钥红线 = 0（拼接哨兵写法）
pat = "sk-" + "kimi-" + "[A-Za-z0-9]|ark-" + "589571" + "[0-9]"
bad = subprocess.run(["grep", "-rn", "-E", pat, ".", "--include=*.py", "--include=*.md", "--include=*.json"],
                     capture_output=True, cwd=R)
check("B11 全仓密钥红线 grep = 0", bad.returncode == 1)

# --- B12. REVISION_LOG 第 20 条
check("B12 REVISION_LOG_v2X.md 含第 20 条", re.search(r"^#*\s*20[.、]", log, re.M) is not None)

print(f"\nFAILS={len(FAILS)}")
for f in FAILS:
    print("  FAIL:", f)
sys.exit(1 if FAILS else 0)
