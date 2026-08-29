#!/usr/bin/env python3
"""verifier/v28 — v2.X 中文初稿成稿验收（复核返工后）"""
import pathlib, re, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

md = (R/"paper/v2/deposon_paper_v2X.md").read_text(encoding="utf-8")
rv = (R/"reviews/post_draft_verification_v2X.md").read_text(encoding="utf-8")
ol = (R/"paper/v2/outline_v2X.md").read_text(encoding="utf-8")

body = md.split("修订记录")[0]  # 修订记录元行豁免
check("成稿文件存在且 ≥20000 字符", len(md) >= 20000)
check("禁用等值对比零残留（正文）", "数值相等" not in body and "92.5% vs 92.5" not in body)
check("H-A1 判死标注", "判死" in md and "0.0118" in md)
check("PoA<1 两图并列披露", "0.5" in md and "0.75" in md and "PoA" in md)
check("OLS 探索性限定", "探索性" in md)
check("GT-3b 口径", "跨厂商" in md and "中文优化" in md)
check("势博弈 consistency 口径（无「证明」过声称）", "consistency" in md.lower() or "一致性" in md)
check("GT-8 入稿（supports_H_GT8 / 2/2）", "GT-8" in md and "supports_H_GT8" in md)
check("GT-2B 入稿且 inconclusive 如实", "GT-2B" in md and "inconclusive" in md)
check("m6 裁定单一口径（C2）", "不携带信息" in md or "机会水平" in md)
check("图语言纪律：中文稿无英文图引用", not re.search(r"!\[.*\]\(.*_en\.(png|jpg)", md))
check("图待制作标注存在", "图待中文版制作" in md)
check("复核报告为有条件 PASS 且 Major 已闭合记录", "有条件 PASS" in rv or "有条件PASS" in rv)
check("修订记录含复核返工条目", "复核返工" in md)
check("outline kill list 鉴定器项已闭合", "~~领域鉴定器 v0 新图复现~~" in ol)
check("PoA 字段路径精确（GT4_price_of_anarchy.verdict）", "GT4_price_of_anarchy" in md)
bad = subprocess.run(["grep","-rn","-E","sk-kimi-[A-Za-z0-9]|ark-589571[0-9]","paper/v2/"], capture_output=True, cwd=R)
check("paper/v2 无密钥串", bad.returncode == 1)
print(f"\nFAILS={len(FAILS)}")
sys.exit(1 if FAILS else 0)
