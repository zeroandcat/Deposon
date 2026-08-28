#!/usr/bin/env python3
"""v7 — 防退稿严审：版本谱系连续性与 §4.7 正文摄入验收。

验收范围（仅针对本轮修正）：
1) 版本不再断档在 v1.4：头注、Table C1、结论口径同步到 v1.5/v1.5.1/v1.6；
2) 脑图补全优势进入实验正文：中英文均存在 §4.7 + Table 13，且位于 §5 之前；
3) §5.3/§5.4 展望段只留指针，不再夹带长结果段；
4) 附录 D.4 配对统计补充存在且与 results/deposon_v16_paired_stats.json 对应；
5) 诚实限定保留：any_lambda_pass=false、0.294<0.412、先验方向反转、人工转译；
6) 安全：无 API key 泄漏。
exit 0=PASS, 1=FAIL。
"""
from pathlib import Path
import json, sys

ROOT = Path(__file__).resolve().parents[2]
CN = ROOT / "paper" / "deposon_paper_v1.md"
EN = ROOT / "paper" / "deposon_paper_v1_en.md"
STATS = ROOT / "results" / "deposon_v16_paired_stats.json"

fails = []
def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok:
        fails.append(name)

cn = CN.read_text(encoding="utf-8")
en = EN.read_text(encoding="utf-8")

# 1) version lineage
check("cn_header_v16", "+ v1.5/v1.5.1/v1.6" in cn)
check("en_header_v16", "+ v1.5/v1.5.1/v1.6" in en)
check("cn_table_title_v16", "版本沿革（v1.2 → v1.6）" in cn and "版本沿革（v1.2 → v1.4）" not in cn)
check("en_table_title_v16", "Version history (v1.2 → v1.6)" in en and "Version history (v1.2 → v1.4)" not in en)
for v in ["| v1.5 |", "| v1.5.1 |", "| v1.6 |"]:
    check(f"cn_table_row_{v}", v in cn)
    check(f"en_table_row_{v}", v in en)
check("cn_future_v17", "近期（v1.7–v2.0）" in cn)
check("en_future_v17", "Near term (v1.7–v2.0)" in en)

# 2) §4.7 in main experiments before §5
check("cn_sec47", "### 4.7 凝子场扩散生成原型：脑图补全（v1.5–v1.6）" in cn)
check("en_sec47", "### 4.7 Deposon Diffusion prototype: mind-map completion (v1.5–v1.6)" in en)
check("cn_table13", "**Table 13. 脑图留一边补全六臂 top-3 命中率" in cn)
check("en_table13", "**Table 13. Leave-one-out mind-map edge completion" in en)
check("cn_47_before_5", cn.find("### 4.7") != -1 and cn.find("### 4.7") < cn.find("## 5 讨论"))
check("en_47_before_5", en.find("### 4.7") != -1 and en.find("### 4.7") < en.find("## 5 Limitations and Ethics"))

# 3) outlook keeps pointer only
check("cn_outlook_pointer", "已按实验口径纳入 §4.7" in cn)
check("en_outlook_pointer", "reported as experiments in Sec. 4.7" in en)
check("cn_no_long_results_in_53", "named-path top-3 0.176 vs 0.412" not in cn.split("### 5.3 硬件同构展望",1)[1].split("## 6 结论",1)[0])
check("en_no_long_results_in_54", "named-path top-3 0.176 vs 0.412" not in en.split("### 5.4 Hardware-isomorphism outlook",1)[1].split("## 6 Conclusion",1)[0])

# 4) D.4 stats
check("cn_d4", "**D.4 脑图补全的配对统计补充（v1.6，新增）。**" in cn)
check("en_d4", "**D.4 Paired statistics for mind-map completion (v1.6, added).**" in en)
check("stats_json_exists", STATS.exists())
if STATS.exists():
    st = json.loads(STATS.read_text(encoding="utf-8"))
    ov = st["subsets"]["overall"]["comparisons"]["hybrid@1.0_vs_field_guided"]
    named = st["subsets"]["named_path"]["comparisons"]["hybrid@1.0_vs_random"]
    check("stats_values", abs(ov["bootstrap"]["diff_mean"] - 0.04081632653061229) < 1e-9 and named["mcnemar"]["p_exact"] == 0.6875)

# 5) honesty limits
check("honesty_any_lambda_false", "any_lambda_pass=false" in cn and "any_lambda_pass=false" in en)
check("honesty_named_below_random", "0.294<0.412" in cn and "0.294<0.412" in en)
check("honesty_inverted", "GOAL→分支" in cn and "GOAL→branches" in en)
check("honesty_manual_transcription", "人工转译" in cn and "manually transcribed" in en)

# 6) key leak scan (tracked text files only, skip .git)
leak = []
for p in ROOT.rglob("*"):
    if ".git" in p.parts or not p.is_file() or p.suffix.lower() not in {".py", ".md", ".json", ".txt", ".log", ".bib"}:
        continue
    try:
        t = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    if ("sk-" + "kimi-") in t:
        leak.append(str(p.relative_to(ROOT)))
check("no_key_leak", not leak, ",".join(leak[:3]))

print(f"FAILS: {len(fails)}")
sys.exit(1 if fails else 0)
