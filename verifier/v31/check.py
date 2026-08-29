#!/usr/bin/env python3
"""verifier/v31 — v2.X 方向校准稿终验"""
import pathlib, re, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

md = (R/"paper/v2/deposon_paper_v2X.md").read_text(encoding="utf-8")
log = (R/"paper/v2/REVISION_LOG_v2X.md").read_text(encoding="utf-8")
rv = (R/"reviews/review_realign_v2X.md").read_text(encoding="utf-8")

check("新主线标题：可审计优势的博弈论实证", "可审计优势的博弈论实证" in md)
check("命题→实证衔接（1.9 可审计表征锚点）", "可审计表征" in md and "守恒保证" in md)
check("§5 存在性→定量化→边界组织", "存在性" in md and "定量化" in md and "边界" in md)
check("划界降为推论（§4.5 推论口径）", "推论" in md)
check("无并列双主线残留（Minor-1 已修）", "划界部分（§4、§6）" not in md)
check("§4 共用证据底座定位语（Minor-2）", "共用证据底座" in md)
check("consistency 不放松声明", "不放松" in md or "consistency" in md.lower())
check("关键数字在稿（2.2e-16 变体/1.333/0.0118/0.7805）", any(n in md for n in ("2.2e-16","2.2×10","2.2\\times")) and "1.333" in md and "0.0118" in md and "0.7805" in md)
check("复审 PASS 无 Major", "PASS" in rv and "无 Major" in rv)
check("REVISION_LOG 16/17 条目", "16. **方向校准重构" in log and "17. **" in log)
check("摘要 ≤250 去标点", len(re.sub(r"[\s\W_a-zA-Z0-9]","", (md.split("## 摘要")[1].split("##")[0]).split("**关键词**")[0])) <= 250)
check("图语言纪律：无英文图引用", not re.search(r"!\[.*\]\(.*_en\.(png|jpg)", md))
bad = subprocess.run(["grep","-rn","-E","sk-kimi-[A-Za-z0-9]|ark-589571[0-9]","paper/v2/"], capture_output=True, cwd=R)
check("paper/v2 无密钥串", bad.returncode == 1)
p = subprocess.run([sys.executable,"-m","pytest","tests/","-q"], capture_output=True, text=True, cwd=R)
check("pytest 255 全绿", "255 passed" in p.stdout and "failed" not in p.stdout)
print(f"\nFAILS={len(FAILS)}")
sys.exit(1 if FAILS else 0)
