#!/usr/bin/env python3
# v6 md -> LaTeX 转换器（0 编辑性改动：仅渲染层映射）
# 输入: src/body_v6_stripped.md (sha256[:12]=7df37af24168)
# 输出: build/main.tex
import re, sys, hashlib

SRC = '〔本地路径已脱敏〕'
OUT = '〔本地路径已脱敏〕'

# ---------- Unicode 渲染映射（忠实字形/语义，pdflatex 宏） ----------
UNI = {
    '\u2014': r'\textemdash{}', '\u2013': r'\textendash{}',
    '\u00a7': r'\S{}', '\u00b7': r'\textperiodcentered{}',
    '\u2026': r'\textellipsis{}', '\u00e9': r"\'e", '\u00e8': r"\`e",
    '\u2265': r'\ensuremath{\geq}', '\u2264': r'\ensuremath{\leq}',
    '\u2248': r'\ensuremath{\approx}', '\u2212': r'\ensuremath{-}',
    '\u00d7': r'\ensuremath{\times}', '\u00b1': r'\ensuremath{\pm}',
    '\u221e': r'\ensuremath{\infty}', '\u226b': r'\ensuremath{\gg}',
    '\u2261': r'\ensuremath{\equiv}', '\u2016': r'\ensuremath{\|}',
    '\u2192': r'\ensuremath{\to}', '\u21d2': r'\ensuremath{\Rightarrow}',
    '\u2194': r'\ensuremath{\leftrightarrow}',
    '\u03b1': r'\ensuremath{\alpha}', '\u03b2': r'\ensuremath{\beta}',
    '\u03b3': r'\ensuremath{\gamma}', '\u03b4': r'\ensuremath{\delta}',
    '\u03b7': r'\ensuremath{\eta}',   '\u03bb': r'\ensuremath{\lambda}',
    '\u03c4': r'\ensuremath{\tau}',
    '\u039b': r'\ensuremath{\Lambda}', '\u03a6': r'\ensuremath{\Phi}',
    '\u03a3': r'\ensuremath{\Sigma}', '\u03a0': r'\ensuremath{\Pi}',
    '\u0394': r'\ensuremath{\Delta}',
    '\u00b2': r'\textsuperscript{2}', '\u2080': r'\textsubscript{0}',
    '\u207d': r'\textsuperscript{(}', '\u207e': r'\textsuperscript{)}',
    '\u207f': r'\textsuperscript{n}', '\u2070': r'\textsuperscript{0}',
    '\u1d62': r'\textsubscript{i}', '\u2c7c': r'\textsubscript{j}',
    '\u2714': r'\ding{52}', '\u2705': r'\ding{51}',
    '\U0001F52C': r'\scopeicon{}',
    '\u2460': r'\ding{182}', '\u2461': r'\ding{183}',
    '\u2462': r'\ding{184}', '\u2463': r'\ding{185}',
}

ESC = {'&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#', '_': r'\_',
       '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
       '^': r'\textasciicircum{}'}

# ---------- inline 流水线 ----------
def esc_latex(s):
    return ''.join(ESC.get(ch, ch) for ch in s)

def esc_code_texttt(s):
    # \texttt 内转义（_ 等；code span 内唯一非 ASCII = 截断 sha 的 …）
    s = s.replace('\u2026', r'\textellipsis{}')
    return ''.join(ESC.get(ch, ch) for ch in s)

def quotes_dir(s):
    # 直引号方向机（成对交替）
    out, open_q = [], True
    for ch in s:
        if ch == '"':
            out.append('``' if open_q else "''")
            open_q = not open_q
        else:
            out.append(ch)
    return ''.join(out), open_q  # 末态须闭合

_code_store = []
def extract_code(s):
    global _code_store
    def rep(m):
        _code_store.append(m.group(1))
        return f'\x00{len(_code_store)-1}\x00'
    return re.sub(r'`([^`]+)`', rep, s)

def fill_code(s, table_cell=False):
    def rep(m):
        c = _code_store[int(m.group(1))]
        if ' ' in c or ('/' not in c and len(c) <= 24):
            return r'\texttt{' + esc_code_texttt(c) + '}'
        return r'\path{' + c + '}'
    return re.sub('\x00(\\d+)\x00', rep, s)

def unimap(s):
    for k, v in UNI.items():
        s = s.replace(k, v)
    return s

def inline(s, in_quote=False, table_cell=False):
    s = extract_code(s)
    s, closed = quotes_dir(s)
    assert closed, 'unbalanced quotes: ' + s[:80]
    s = ''.join(ESC.get(ch, ch) for ch in s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'(?<![\w\\])\*([^*\n]+?)\*(?!\*)', r'\\emph{\1}', s)
    s = unimap(s)
    if table_cell:
        # cell 内长 token（无空格，非 code）在 / _ = . - 处插零宽断点（须在 code 回填前，
        # 否则会把宏注入 \path{} 参数内被当字面排版）
        def _brk(m):
            t = m.group(0)
            buf = []
            for ch in t:
                buf.append(ch)
                if ch in '/_.=-':
                    buf.append('\\penalty-100 ')
            return ''.join(buf)
        s = re.sub(r'[A-Za-z0-9\\_/=.\-]{16,}', _brk, s)
    s = fill_code(s, table_cell)
    return s

# ---------- 表格 -> longtable ----------
def col_widths(header, rows, total=13.7):
    n = len(header)
    maxlen = [max(len(header[i]), *(len(r[i]) for r in rows)) if rows else len(header[i]) for i in range(n)]
    # 压缩极长列的影响（log 尺度加权）
    w = [max(0.9, min(12.0, m) ** 0.62) for m in maxlen]
    scale = total / sum(w)
    return [round(wi * scale, 2) for wi in w]

def md_table_to_longtable(block, tid):
    lines = [l for l in block]
    sep_i = next(i for i, l in enumerate(lines) if re.match(r'^\|[\〔本机路径〕\-|]+\|$', l))
    header = [c.strip() for c in lines[0].strip('|').split('|')]
    rows = []
    for l in lines[sep_i+1:]:
        cells = [c.strip() for c in l.strip('|').split('|')]
        assert len(cells) == len(header), f'col mismatch @ {l[:60]}'
        rows.append(cells)
    nrow = len(rows)
    ws = col_widths(header, rows)
    size = r'\footnotesize' if nrow >= 20 else r'\small'
    cols = ' '.join(r'>{%s\arraybackslash}p{%.2fcm}' % (r'\RaggedRight', w) for w in ws)
    hdr = ' & '.join(inline(h, table_cell=True) for h in header) + r' \\'
    out = [r'{%s\begin{longtable}{%s}' % (size, cols),
           r'\toprule', hdr, r'\midrule', r'\endfirsthead',
           r'\toprule', hdr, r'\midrule', r'\endhead',
           r'\endfoot',
           r'\bottomrule', r'\endlastfoot']
    for r in rows:
        out.append(' & '.join(inline(c, table_cell=True) for c in r) + r' \\')
    out.append(r'\end{longtable}}')
    return '\n'.join(out), nrow, len(header), ws

# ---------- 主解析 ----------
raw = open(SRC, encoding='utf-8').read()
assert hashlib.sha256(raw.encode('utf-8')).hexdigest()[:12] == '7df37af24168'
lines = raw.split('\n')

TITLE = re.match(r'^# (.+)$', lines[0]).group(1)
assert TITLE.startswith('Deposon: ')

out = []           # LaTeX body 行
bm = [0]           # bookmark counter
def bookmark(level, text):
    bm[0] += 1
    safe = text.replace('{','').replace('}','').replace('—','-').replace('–','-').replace('…','...')
    for k, v in UNI.items():
        safe = safe.replace(k, '')
    safe = re.sub(r'[^\x20-\x7e\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]', '', safe)
    return r'\pdfbookmark[%d]{%s}{bm%d}' % (level, safe, bm[0])

i = 1  # 行 0=题名; 1=空行; 2=正文首段（evidence-strength convention，题名与 Abstract 之间）
abstract_text = None
keywords_text = None

def flush_para(buf):
    if buf:
        out.append(inline(' '.join(buf)))
        out.append('')
        buf.clear()

# -- 题名后、Abstract 前的段落（evidence-strength convention）--
pre_abs = []
while i < len(lines) and not lines[i].startswith('## '):
    if lines[i].strip() and lines[i].strip() != '---':
        pre_abs.append(lines[i].strip())
    i += 1
pre_abs_tex = '\n\n'.join(inline(t) for t in pre_abs)

mode = 'body'   # body | refs
ref_items = []
ref_tail = []

para = []
tables_meta = []
ti = 0
while i < len(lines):
    ln = lines[i]
    if ln.startswith('## '):
        flush_para(para)
        head = ln[3:].strip()
        if head == 'Abstract':
            # 摘要段与 Keywords 行
            abs_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('## ') and lines[i] != '---':
                if lines[i].strip():
                    abs_lines.append(lines[i].strip())
                i += 1
            abstract_text = abs_lines[0]
            for extra in abs_lines[1:]:
                if extra.startswith('**Keywords:**'):
                    keywords_text = extra
                else:
                    abstract_text += ' ' + extra
            continue
        if head == 'References':
            mode = 'refs'
            i += 1
            continue
        out.append(bookmark(0, head))
        out.append(r'\section*{%s}' % inline(head))
        out.append('')
        i += 1
        continue
    if ln.startswith('### '):
        flush_para(para)
        head = ln[4:].strip()
        out.append(bookmark(1, head))
        out.append(r'\subsection*{%s}' % inline(head))
        out.append('')
        i += 1
        continue
    if ln.startswith('> '):
        flush_para(para)
        qt = ln[2:]
        while i + 1 < len(lines) and lines[i+1].startswith('> '):
            i += 1; qt += ' ' + lines[i][2:]
        out.append(r'\begin{quote}')
        out.append(inline(qt))
        out.append(r'\end{quote}')
        out.append('')
        i += 1
        continue
    if ln.startswith('|'):
        flush_para(para)
        block = []
        while i < len(lines) and lines[i].startswith('|'):
            block.append(lines[i]); i += 1
        tbl, nrow, ncol, ws = md_table_to_longtable(block, ti)
        ti += 1
        tables_meta.append((nrow, ncol, ws))
        out.append(tbl)
        out.append('')
        continue
    if ln.strip() == '---':
        flush_para(para)
        i += 1
        continue
    if mode == 'refs':
        m = re.match(r'^- \[(R\d+)\] (.*)$', ln)
        if m:
            flush_para(para)
            ref_items.append((m.group(1), m.group(2)))
            i += 1
            continue
        if ln.strip():
            para.append(ln.strip())
        else:
            flush_para(para)
        i += 1
        continue
    if ln.startswith('- '):
        flush_para(para)
        out.append(r'\begin{itemize}')
        while i < len(lines) and lines[i].startswith('- '):
            out.append(r'\item ' + inline(lines[i][2:]))
            i += 1
        out.append(r'\end{itemize}')
        out.append('')
        continue
    if ln.strip() == '':
        flush_para(para)
        i += 1
        continue
    para.append(ln.strip())
    i += 1
flush_para(para)

# ---------- 组装 ----------
title_tex = inline(TITLE)
abs_tex = inline(abstract_text)
kw_tex = inline(keywords_text)

bibs = '\n'.join(
    r'\bibitem[%s]{%s} %s' % (rid, rid, inline(body_txt))
    for rid, body_txt in ref_items)
ref_tail_tex = '\n\n'.join(inline(t) for t in ref_tail) if ref_tail else ''

preamble = r'''% Generated by Dave (format specialist) from body_v6_stripped.md
% sha256[:12]=7df37af24168 (body, header-stripped); source v6 = b6fde709970a
% 0 editorial changes: rendering-layer mappings only (see format report)
\documentclass[11pt,letterpaper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[letterpaper,margin=1in]{geometry}
\usepackage{amsmath,amssymb}
\usepackage{textcomp}
\usepackage{pifont}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
% ragged2e unavailable in local TL2026 tree; finite-stretch RaggedRight
% (keeps hyphenation, unlike \raggedright)
\newcommand{\RaggedRight}{\rightskip=0pt plus2em\relax}
\usepackage[hyphens,spaces]{url}
\urlstyle{tt}
\makeatletter
\def\UrlBreaks{\do\.\do\-\do\/\do\_\do\=}
\makeatother
\usepackage{CJKutf8}
\usepackage[unicode]{hyperref}
\tolerance=9999
\emergencystretch=3em
\setlength{\LTpre}{6pt}\setlength{\LTpost}{6pt}
\setcounter{LTchunksize}{300}
% \scopeicon: rendering glyph for U+1F52C (microscope emoji, README literal)
% built with the zero-dependency LaTeX picture environment
\newcommand{\scopeicon}{%
\setlength{\unitlength}{0.26em}%
\begin{picture}(9,6.4)(-3.2,-3.0)
\put(-2.6,-2.8){\line(1,0){5.0}}
\put(2.0,-2.8){\line(0,1){4.6}}
\put(2.0,1.8){\line(-1,0){1.0}}
\put(1.0,1.8){\line(0,1){0.8}}
\put(-1.9,1.0){\framebox(1.2,1.0){}}
\put(-1.8,2.0){\line(0,1){0.6}}
\put(-0.8,2.0){\line(0,1){0.6}}
\put(-1.8,2.6){\line(1,0){1.0}}
\put(-1.6,0.0){\line(0,1){1.0}}
\put(-1.0,0.0){\line(0,1){1.0}}
\put(-1.75,0.0){\line(1,0){0.9}}
\put(-2.6,0.2){\line(1,0){4.6}}
\end{picture}}
\hypersetup{pdftitle={TITLE_MACRO},pdfsubject={arXiv preprint, primary classification cs.AI}}
\begin{document}
\begin{CJK}{UTF8}{gbsn}
\begin{center}
{\LARGE\bfseries TITLE_MACRO\par}
\end{center}
\vspace{0.8em}
'''

def subst(s):
    return s.replace('TITLE_MACRO', title_tex)

preamble = subst(preamble)

mid = r'''PRE_ABS_MACRO

\begin{abstract}
ABSTRACT_MACRO

\noindent KW_MACRO
\end{abstract}

'''
mid = mid.replace('PRE_ABS_MACRO', pre_abs_tex).replace('ABSTRACT_MACRO', abs_tex).replace('KW_MACRO', kw_tex)

refs_env = r'''\pdfbookmark[0]{References}{bmrefs}
\begin{thebibliography}{99}
BIBS
\end{thebibliography}
REF_TAIL
'''.replace('BIBS', bibs).replace('REF_TAIL', ('\n' + ref_tail_tex + '\n') if ref_tail_tex else '')

tail = r'''\end{CJK}
\end{document}
'''

tex = preamble + mid + '\n'.join(out) + '\n' + refs_env + tail
open(OUT, 'w', encoding='utf-8').write(tex)

# 断言：转换后残留非 ASCII 仅 CJK
resid = set(ch for ch in tex if ord(ch) > 127 and not
            ('\u4e00' <= ch <= '\u9fff' or '\u3000' <= ch <= '\u303f' or '\uff00' <= ch <= '\uffef'))
print('main.tex written:', len(tex), 'chars')
print('residual non-CJK non-ascii:', resid if resid else 'NONE')
print('tables:', ti, tables_meta)
print('bibitems:', len(ref_items))
print('bookmarks:', bm[0])
