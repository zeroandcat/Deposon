#!/usr/bin/env python3
"""verifier/v30 — v2.X 质量跃升稿终验（重写+润色+复审收尾后）"""
import pathlib, re, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

md = (R/"paper/v2/deposon_paper_v2X.md").read_text(encoding="utf-8")
log = (R/"paper/v2/REVISION_LOG_v2X.md").read_text(encoding="utf-8")
r2 = (R/"reviews/review_coach_v2X_draft_r2.md").read_text(encoding="utf-8")

abstract = (md.split("## 摘要")[1].split("##")[0] if "## 摘要" in md else md.split("##")[0]).split("**关键词**")[0]
zh_chars = len(re.sub(r"[\s\W_a-zA-Z0-9]", "", abstract))
check("摘要去标点 ≤250 字", zh_chars <= 250)
check("摘要数字 ≤6", len(re.findall(r"\d+\.?\d*", abstract)) <= 6)
check("修订记录已移出论文（仅指引行）", md.count("修订记录") <= 2 and "REVISION_LOG_v2X" in md)
check("REVISION_LOG 含 13/14/15 条目", "第 13 条" in log and "14." in log and "15." in log and "复审收尾" in log)
check("复审四维 ≥7（7/8/8/7）", all(x in r2 for x in ("7", "8")))
check("「正交互补」正文零残留", "正交互补" not in md)
check("鉴定器=观察性规律口径", "观察性规律" in md)
check("GT-8b 入稿 inconclusive + 0.7805", "GT-8b" in md and "0.7805" in md and "inconclusive" in md)
check("超几何 p=0.187/0.046 入稿", "0.187" in md and "0.046" in md)
check("homophily §2.2 存在且待核标注", "homophily" in md.lower() and "[待核" in md)
check("先验映射规则 §3.2 存在", "映射" in md)
check("H-A1 判死 + p=0.0118 保留", "判死" in md and "0.0118" in md)
check("GT-3b 口径保留", "跨厂商" in md and "中文优化" in md)
check("PoA 全 17 图 median 1.333 + 族 L 0.5/0.75", "1.333" in md and "0.5" in md and "0.75" in md)
check("无英文图引用（图语言纪律）", not re.search(r"!\[.*\]\(.*_en\.(png|jpg)", md))
ai = [w for w in ("值得注意的是","综上所述","赋能","抓手","至关重要") if w in md]
check("AI 腔高频词零残留", not ai)
bad = subprocess.run(["grep","-rn","-E","sk-kimi-[A-Za-z0-9]|ark-589571[0-9]","paper/v2/"], capture_output=True, cwd=R)
check("paper/v2 无密钥串", bad.returncode == 1)
p = subprocess.run([sys.executable,"-m","pytest","tests/","-q"], capture_output=True, text=True, cwd=R)
check("pytest 255 全绿", "255 passed" in p.stdout and "failed" not in p.stdout)
print(f"\nFAILS={len(FAILS)}")
sys.exit(1 if FAILS else 0)
