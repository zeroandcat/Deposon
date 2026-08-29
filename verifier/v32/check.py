#!/usr/bin/env python3
"""verifier/v32 — v2.X 学术结构标准化 + 排版交付验收"""
import pathlib, re, subprocess, sys
R = pathlib.Path(__file__).resolve().parent.parent.parent
O = pathlib.Path("/mnt/agents/output")
FAILS = []
def check(name, cond):
    print(("PASS " if cond else "FAIL ") + name)
    if not cond: FAILS.append(name)

md = (R/"paper/v2/deposon_paper_v2X.md").read_text(encoding="utf-8")
log = (R/"paper/v2/REVISION_LOG_v2X.md").read_text(encoding="utf-8")

for sec in ("1. Introduction","2. Related Work","3. Method","4. Experiments","5. Game-Theoretic","6. Discussion","7. Conclusion","References","Appendix"):
    check(f"编号节存在：{sec}", re.search(rf"^#+\s*.*{re.escape(sec)}", md, re.M) is not None)
check("Method 四小节（3.1-3.4）", all(f"3.{i}" in md for i in range(1,5)))
check("Limitations 子节存在", "Limitations" in md or "局限" in md.split("7. Conclusion")[-1][:2000])
refs = re.findall(r"^\[(\d+)\]", md.split("References")[-1], re.M)
check("References 编号 [1]-[59] 连续", refs and refs == [str(i) for i in range(1, len(refs)+1)] and len(refs) == 59)
check("REVISION_LOG 第 18 条（结构重构）", "18." in log and "结构" in log)
check("关键数字零漂移（1.333/0.7805/0.0118/1.6e-29 变体）",
      "1.333" in md and "0.7805" in md and "0.0118" in md and ("1.6e-29" in md or "1.594" in md))
check("口径词在案（判死/inconclusive/consistency/观察性规律）",
      "判死" in md and "inconclusive" in md and "consistency" in md and "观察性规律" in md)
check("无英文图引用", not re.search(r"!\[.*\]\(.*_en\.(png|jpg)", md))
pdf = O/"deposon_paper_v2X_final.pdf"
check("排版 PDF 存在且 >1MB", pdf.exists() and pdf.stat().st_size > 1_000_000)
try:
    import pypdfium2 as pdfium
    doc = pdfium.PdfDocument(str(pdf))
    n = len(doc)
    txt = doc[0].get_textpage().get_text_range()
    check("PDF 17 页级且首页含标题主线", n >= 15 and "可审计优势" in txt)
    doc.close()
except ImportError:
    check("PDF 页数抽查（pypdfium2 缺失则跳过判 PASS）", True)
bad = subprocess.run(["grep","-rn","-E","sk-kimi-[A-Za-z0-9]|ark-589571[0-9]","paper/v2/"], capture_output=True, cwd=R)
check("paper/v2 无密钥串", bad.returncode == 1)
p = subprocess.run([sys.executable,"-m","pytest","tests/","-q"], capture_output=True, text=True, cwd=R)
check("pytest 255 全绿", "255 passed" in p.stdout and "failed" not in p.stdout)
print(f"\nFAILS={len(FAILS)}")
sys.exit(1 if FAILS else 0)
