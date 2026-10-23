#!/usr/bin/env python3
# visual_gate.py — FTFB 视觉语义层质量门「abstract 块止于第 1 页」（2026-09-17，戴夫）
# 背景：R2 元审 T-1 阻断项——v1/v2 交付 tex 的 \end{abstract} 错位（v2 L409/v1 L392），
#   摘要段+全部正文+AI 披露段被排入 abstract 环境渲染；Z1–Z4/S1–S6 均为文本层/日志层
#   检查，结构性无法捕获。本门补齐视觉语义层，双实现：
#   G1 tex 结构检查：abstract 环境闭合必须先于首个编号 \section；环境内不得含任何
#      结构块（\section/\subsection/\begin{table}/\begin{itemize}/\begin{enumerate}/\item）。
#      注意 preamble 含 \renewcommand\section{\@startsection...，故首个 \section 搜索
#      必须从 \begin{document} 之后起算。
#   G2 PDF 页面级探针：第 2 页起不得处于 abstract 排版。article 类 abstract 环境 =
#   \small + quotation：左右各缩进 \leftmargini（11pt 下 27.3pt），文本块从
#   [72.0, 523.3]pt 缩为 [99.3, 496.0]pt（A4/1in 边距实测）。探针逐页提取词级
#   bbox（pdftotext -bbox），按 y 中心聚类重建文本行，统计「窄栏签名行」：
#      行左缘 ∈ [94,105]pt 且 行右缘 ∈ [491,501]pt 且 行宽 ≥ 180pt。
#   表格浮动体不受 quotation 缩进影响（实测左缘 75.4pt），无法伪造该双条件签名，
#   故含表页不漏报；References 页（环境外，右缘 523.3pt）不误报。页 ≥2 且签名行
#   ≥3 → 判该页处于 abstract 排版 → ALARM（阈值 3 防零星巧合；缺陷页实测 19–46 行）。
# 用法：python3 visual_gate.py <tex> <pdf>    （两门全过 exit 0 并打印 PASS；任一失败 exit 1）
import re, subprocess, sys

def gate(name, cond, detail):
    tag = 'PASS' if cond else 'FAIL'
    print('[%s] %s: %s' % (tag, name, detail))
    return cond

tex = open(sys.argv[1], encoding='utf-8').read()
pdf = sys.argv[2]

# ---- G1: tex 结构 ----
g1 = True
n_begin, n_end = tex.count('\\begin{abstract}'), tex.count('\\end{abstract}')
g1 &= gate('G1a-环境配对', n_begin == 1 and n_end == 1,
           '\\begin{abstract}=%d, \\end{abstract}=%d（期望 1/1）' % (n_begin, n_end))
if g1:
    ab = tex.index('\\begin{abstract}'); ae = tex.index('\\end{abstract}')
    doc = tex.index('\\begin{document}')
    fs = tex.find('\\section{', doc)
    lb, le, lf = (tex[:i].count('\n') + 1 for i in (ab, ae, fs))
    g1 &= gate('G1b-闭合先于首节', ab < ae < fs,
               'begin L%d → end L%d → 首个 \\section L%d（要求 end < section）' % (lb, le, lf))
    inner = tex[ab + len('\\begin{abstract}'):ae]
    bad = [k for k in ['\\section', '\\subsection', '\\begin{table}',
                       '\\begin{itemize}', '\\begin{enumerate}', '\\item'] if k in inner]
    g1 &= gate('G1c-环境内无结构块', not bad, 'abstract 内部结构块: %s' % (bad or '无'))
else:
    print('[FAIL] G1b/G1c: 跳过（G1a 未过）')

# ---- G2: PDF 页面级探针 ----
xml = subprocess.run(['pdftotext', '-bbox', pdf, '-'], capture_output=True, text=True).stdout
pages = re.findall(r'<page width="([\d.]+)" height="([\d.]+)">(.*?)</page>', xml, re.S)
alarmed, per_page = [], []
for idx, (w, h, body) in enumerate(pages, 1):
    words = [(float(a), float(b), float(c), float(d)) for a, b, c, d in
             re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)"[^>]*>', body)]
    if not words:
        per_page.append((idx, 0, 0)); continue
    ws = sorted(words, key=lambda t: ((t[1] + t[3]) / 2, t[0]))
    lines, cur, cury = [], [], None
    for wd in ws:
        yc = (wd[1] + wd[3]) / 2
        if cury is None or abs(yc - cury) <= 3.0:
            cur.append(wd); cury = yc if cury is None else (cury * (len(cur) - 1) + yc) / len(cur)
        else:
            lines.append(cur); cur, cury = [wd], yc
    if cur: lines.append(cur)
    narrow = 0
    for ln in lines:
        left = min(x[0] for x in ln); right = max(x[2] for x in ln)
        if 94 <= left <= 105 and 491 <= right <= 501 and right - left >= 180: narrow += 1
    per_page.append((idx, len(lines), narrow))
    if idx >= 2 and narrow >= 3: alarmed.append(idx)
stats = ' '.join('p%d:%d行/窄%d' % p for p in per_page)
g2 = gate('G2-第2页起无abstract排版', not alarmed,
          '总页数=%d；报警页=%s；逐页(页:行数/窄栏签名行数) %s' % (len(pages), alarmed or '无', stats))

print('VISUAL GATE RESULT:', 'PASS' if (g1 and g2) else 'FAIL')
sys.exit(0 if (g1 and g2) else 1)
