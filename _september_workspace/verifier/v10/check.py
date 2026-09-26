#!/usr/bin/env python3
# verifier/v10 — v1.9 整改验收（在 v9 基础上新增；v9 目录不可变）
# 用法: python3 verifier/v10/check.py   （仓库根目录任意位置均可运行）
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILS = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        FAILS.append(name)

# ---------- 1. v1.9 实验文件与判定 ----------
spec = (ROOT / "docs/SPEC_v1.9.md").read_text(encoding="utf-8")
check("SPEC v1.9 Part A 存在", "Part A" in spec and "E9.1" in spec and "E9.6" in spec)
check("SPEC v1.9 Part B 存在", "Part B" in spec and "E9.3" in spec and "E9.5" in spec)

mf = json.load(open(ROOT / "results/deposon_v19_meanfield.json"))
se = mf["success_evaluation"]
check("E9.1 H1 成立", se["H1_random_init_is_root_cause"] is True)
check("E9.1 field_mean named=1.0", abs(se["field_mean_named"] - 1.0) < 1e-9)
check("E9.1 filler<0.15 骨架检测器", se["H2_skeleton_detector_filler_below_0.15"] is True)
check("E9.1 spec_version", mf["spec_version"] == "v1.9")

fr = json.load(open(ROOT / "results/deposon_v19_fullrank.json"))
check("E9.2 spec_version", fr["spec_version"] == "v1.9")
qw = json.load(open(ROOT / "results/deposon_v19_quickwins.json"))
st = qw["E9_6a_sign_tests"]
k_rh = [k for k in st if k.startswith("random_minus_hybrid")][0]
k_hf = [k for k in st if "minus_field" in k][0]
check("E9.6a 符号检验复现 R3 (random≥hybrid)",
      abs(st[k_rh]["p_exact"] - 0.001312) < 1e-4, str(st[k_rh]["p_exact"]))
check("E9.6a 符号检验复现 R3 (hybrid>field)",
      abs(st[k_hf]["p_exact"] - 0.007538) < 1e-4, str(st[k_hf]["p_exact"]))
bf = json.load(open(ROOT / "results/deposon_v19_benchmark_fixes.json"))
txt_bf = json.dumps(bf, ensure_ascii=False)
check("E9.3 high_couple=0.82 在案", "0.82" in txt_bf)
check("E9.4 等权对照记录在案", "flat" in txt_bf.lower() or "FLAT_WEIGHT" in txt_bf)
check("E9.5 规则基线在案", "rule" in txt_bf.lower())

# ---------- 2. 论文整改（CN/EN）----------
cn = (ROOT / "paper/deposon_paper_v1.md").read_text(encoding="utf-8")
en = (ROOT / "paper/deposon_paper_v1_en.md").read_text(encoding="utf-8")

for tag, t in [("CN", cn), ("EN", en)]:
    check(f"{tag} 头部 v1.9", "v1.9" in t.split("\n", 15)[0] or "v1.9" in t[:600])
    check(f"{tag} Table 10 更正 0.82", "0.82" in t)
    check(f"{tag} E9.4 等权对照写入", ("等权" in t or "flat" in t.lower() or "equal-weight" in t.lower()))
    check(f"{tag} E9.5 规则基线写入", ("规则" in t and "基线" in t) or "rule-based" in t.lower() or "rule baseline" in t.lower())
    check(f"{tag} mean-field named=1.000 写入", ("1.000" in t or "17/17" in t))
    check(f"{tag} overall 非劣效表述", ("非劣" in t) or ("non-inferior" in t.lower()))
    check(f"{tag} 单图个案证据声明", ("单图" in t and "个案" in t) or ("single-map" in t.lower()) or ("single-graph" in t.lower()) or ("case-study" in t.lower()))
    check(f"{tag} λ>1 反场 artifact 披露", ("artifact" in t.lower()) or ("伪影" in t))
    check(f"{tag} 骨架检测器表述", ("骨架检测器" in t) or ("skeleton detector" in t.lower()))

# 摘要长度（评审 B W1）
ab_en = re.search(r"(?is)abstract(.{200,4000}?)\n#", en)
if ab_en:
    w = len(re.findall(r"[A-Za-z']+", ab_en.group(1)))
    check("EN 摘要 ≤300 词", w <= 300, f"{w} 词")
else:
    check("EN 摘要可定位", False)

# 残留批注/乱版检查
check("CN 无残留编辑批注", "（表上方为表题）" not in cn and "(表上方为表题)" not in cn)
check("CN 无英文 Table/Fig 标签", not re.search(r"(?m)^\s*(Table|Fig\.)\s*\d", cn))

# 表格首引顺序（正文区间）
def first_citation_order(t, pattern):
    return [int(m.group(1)) for m in re.finditer(pattern, t)]
cn_body = cn.split("附录")[0]
nums = first_citation_order(cn_body, r"表\s*(\d+)")
seen, order_ok, nxt = set(), True, 1
for n in nums:
    if n not in seen:
        if n != nxt:
            order_ok = False
            break
        seen.add(n); nxt += 1
check("CN 表格首引顺序单调", order_ok, f"首引序列={nums[:20]}")

# ---------- 3. 口语与密钥红线 ----------
leak = "sk-" + "kimi-"
for p in ["docs/SPEC_v1.9.md", "docs/Roadmap_v1.9.md",
          "paper/deposon_paper_v1.md", "paper/deposon_paper_v1_en.md",
          "results/deposon_v19_meanfield.json", "results/deposon_v19_benchmark_fixes.json"]:
    check(f"无密钥残留 {Path(p).name}", leak not in (ROOT / p).read_text(encoding="utf-8", errors="ignore"))
check("CN 无口语「零 API」", "零 API" not in cn and "零API" not in cn)
check("EN 无口语 zero-api", not re.search(r"zero ?api", en, re.I))
check("无「补实验」口语（除修订记录）", not re.search(r"(?<!补充)补实验", cn))

# ---------- 4. pytest ----------
r = subprocess.run([sys.executable, "-m", "pytest", "-q", "--tb=no"],
                   cwd=ROOT, capture_output=True, text=True, timeout=1200)
m = re.search(r"(\d+) passed", r.stdout)
check("pytest 全绿", r.returncode == 0 and m is not None, (m.group(0) if m else r.stdout[-300:]))

print(f"\n===== FAILS={len(FAILS)} =====")
sys.exit(1 if FAILS else 0)
