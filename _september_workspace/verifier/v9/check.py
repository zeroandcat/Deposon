#!/usr/bin/env python3
"""v9 — v1.8.1 API 补实验整合与论文措辞正式化验收。

判据：v1.8 结果文件齐备（汇总 spec_version=v1.8.1、四缓存、E3 畸形归档）；
E1 置换不变性/E4 弃权/E2 弱反证/E3 稳健性判定落盘；论文（中英）纳入 v1.8.1
（文头串、§4.7 标题范围、§4.7 新段、附录 D.6、Table C1 行）；「零 API/补实验」
口语化措辞零残留；既有数字锚点不变（v1.7.1 关键值）；设计缺陷/自陈探针披露在文；
SPEC v1.8.1 修正案存在；pytest 全绿（134）；无 API key 泄漏。exit 0=PASS。"""
from pathlib import Path
import json, re, subprocess, sys
ROOT = Path(__file__).resolve().parents[2]
fails = []
def check(name, ok, detail=""):
    print(("PASS" if ok else "FAIL"), name, detail)
    if not ok: fails.append(name)

cn = (ROOT/"paper/deposon_paper_v1.md").read_text(encoding="utf-8")
en = (ROOT/"paper/deposon_paper_v1_en.md").read_text(encoding="utf-8")

# ---- 1. v1.8 结果文件齐备
for f in ["results/deposon_v18_api_supplements.json",
          "results/llm_prior_cache_v18_labelshuffle.json",
          "results/llm_prior_cache_v18_contamination.json",
          "results/llm_prior_cache_v18_direction.json",
          "results/llm_prior_cache_v18_direction_run1_malformed_archive.json",
          "results/llm_prior_cache_v18_contentless.json",
          "run_v18_api_supplements.py", "tests/test_v18.py"]:
    check("exists_" + f, (ROOT/f).exists())

d = json.loads((ROOT/"results/deposon_v18_api_supplements.json").read_text(encoding="utf-8"))
check("v18_spec_version", d["spec_version"] == "v1.8.1", d["spec_version"])
v = d["verdicts"]
check("E1_invariance", v["E1"].get("permutation_invariant") is True
      and v["E1"].get("design_flaw_disclosed") is True)
check("E2_weak_counter", v["E2"].get("contamination_alarm") is False)
check("E3_robust", v["E3"].get("robust_to_prompt_wording") is True)
check("E4_abstention", v["E4"].get("mode") == "abstention"
      and v["E4"].get("supports_semantic_claim") is True)
e3c = json.loads((ROOT/"results/llm_prior_cache_v18_direction.json").read_text(encoding="utf-8"))
check("E3_cache_13edges", len(e3c["prior"]) == 13 and isinstance(e3c["prior"], list))
e4c = json.loads((ROOT/"results/llm_prior_cache_v18_contentless.json").read_text(encoding="utf-8"))
check("E4_cache_abstained", e4c.get("status") == "abstained" and e4c["prior"] == [])
check("E1_edge_set", d["experiments"]["E1"]["permutation_invariance"]["edge_set_identical"] is True
      and d["experiments"]["E1"]["permutation_invariance"]["shared_edges"] == 9)

# ---- 2. 论文整合 v1.8.1（中英）
for s, lang in [(cn, "cn"), (en, "en")]:
    check(lang + "_header_v181", "v1.8.1" in s.split("\n")[6 if lang == "cn" else 4])
    check(lang + "_s47_title_range", ("（v1.5–v1.8.1）" in s) if lang == "cn"
          else ("(v1.5–v1.8.1)" in s))
    check(lang + "_tableC_v181", "v1.2 → v1.8.1" in s and "| v1.8.1 |" in s)
    check(lang + "_d6", "D.6" in s)
    check(lang + "_e1_disclosure", ("口径作废" in s or "置换不变" in s) if lang == "cn"
          else ("voided" in s or "permutation-invar" in s or "permutation invar" in s))
    check(lang + "_e4_abstain", ("弃权" in s) if lang == "cn"
          else ("abstain" in s.lower()))
    check(lang + "_e2_selfreport", ("自陈" in s) if lang == "cn"
          else ("self-report" in s.lower()))
    # 新增 v1.8 数字锚点
    check(lang + "_num_pearson", "0.724" in s)
    check(lang + "_num_jaccard", "0.692" in s)
    # 既有数字锚点不变（v1.7.1 关键值）
    for anchor in ["0.367", "0.294", "0.471", "0.176", "0.227", "0.388"]:
        check(lang + "_anchor_" + anchor, anchor in s)
    # 诚实降级保留
    check(lang + "_honest_nonsig", ("非统计显著" in s) if lang == "cn"
          else ("non-significant" in s))
    check(lang + "_sampler_sensitive", ("采样器敏感" in s) if lang == "cn"
          else ("sampler" in s and "sensitive" in s))

# ---- 3. 口语化措辞零残留
for s, lang in [(cn, "cn"), (en, "en")]:
    check(lang + "_no_lingAPI", "零 API" not in s and "零API" not in s)
    check(lang + "_no_bushiyan", re.search(r"(?<!补充)补实验", s) is None)
check("en_no_zeroapi", re.search(r"zero[\s-]?api", en, re.IGNORECASE) is None)

# ---- 4. SPEC v1.8.1 修正案
spec = (ROOT/"docs/SPEC_v1.8.md").read_text(encoding="utf-8")
check("spec_amendment", "v1.8.1" in spec and "E4" in spec and "设计缺陷" in spec)

# ---- 5. pytest 全绿
r = subprocess.run([sys.executable, "-m", "pytest", "tests/", "-q",
                    "-p", "no:cacheprovider"], cwd=ROOT, text=True, capture_output=True)
check("pytest_green", r.returncode == 0 and "134 passed" in r.stdout,
      r.stdout.strip().splitlines()[-1] if r.stdout else "")

# ---- 6. key 泄漏扫描（pattern 拼装避免自命中）
pat = "sk-" + "kimi-"
leak = []
for p in ROOT.rglob("*"):
    if ".git" in p.parts or not p.is_file() or p.suffix.lower() not in {
            ".py", ".md", ".json", ".txt", ".log", ".bib"}:
        continue
    try:
        t = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    if pat in t:
        leak.append(str(p.relative_to(ROOT)))
check("no_key_leak", not leak, ",".join(leak[:3]))

print(f"FAILS: {len(fails)}")
sys.exit(1 if fails else 0)
