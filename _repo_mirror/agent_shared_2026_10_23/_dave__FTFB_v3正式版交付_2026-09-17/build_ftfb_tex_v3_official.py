#!/usr/bin/env python3
# build_ftfb_tex_v3_official.py — FTFB md→tex v3 正式版（R2 修订链头；内容零改动）
# 基线管线 = ftfb_v3_trial/build_ftfb_tex_v3.py（T-1 abstract 闭合修复版），差异仅三处（均为
# 内容层适配，排版逻辑零改动）：
#   [A] 链头切换：SRC=鲍勃_FTFB全稿R2修订版_2026-09-17.md，SHA-256 全量锁
#       7a0a98289588dded5c0543bd3d0267fad4a387e24e42c2cff5e33f457ae38f1b。
#   [B] 编辑工件剥离（送审纪律，源头声明）：首部「R2 修订版说明」块（L1–L7 + 空行 L8）
#       与尾部「## 附录：R2 修订逐条对照表」整节（含其前 '---' 分隔行）不进入正文；
#       剥离边界用行级断言钉死（标题行/首尾标记/末条 R54 均精确匹配），剥离后正文
#       383 行 = 论文全文（# Fiction … 起至 - R54. 条目止）。
#   [C] inline 管线 URL 保护前置一条规则：https?://<非空白> 整体入 \url{}（R2 新增
#       R53/R54 三条 https 源 URL；旧规则只护裸 .com 域）。若不护，R54 URL 内
#       "of_Matter" 会落入 snake_case 规则被 \texttt 局部包裹（渲染层破坏）。
#   [D] 引用计数断言 52 → 54（R53/R54 新池）。
# 纪律：断言失败即停；不写源文件；T-1 结构断言沿用试验版。
import hashlib, re, sys

SRC = '/home/z/my-project/shared/鲍勃_FTFB全稿R2修订版_2026-09-17.md'
OUT = '/home/z/my-project/agents/6a962cc259312f271f3f1e75/ftfb_v3_official/ftfb_v3.tex'
EXPECT_SHA = '7a0a98289588dded5c0543bd3d0267fad4a387e24e42c2cff5e33f457ae38f1b'

raw_bytes = open(SRC, 'rb').read()
assert hashlib.sha256(raw_bytes).hexdigest() == EXPECT_SHA, 'chain head sha256 mismatch'
raw_full = raw_bytes.decode('utf-8')

TITLE = 'Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews'

# ---------- [B] editorial artifact strip (line-anchored, asserted) ----------
flines = raw_full.split('\n')
assert flines[0].startswith('> **R2 修订版说明'), 'unexpected head: ' + flines[0][:40]
assert '编辑工件' in flines[0], 'head artifact self-declaration missing'
assert flines[6] == '---' and flines[7] == '', 'head artifact boundary (L7/L8)'
assert flines[8] == '# ' + TITLE, 'paper title not at L9'
# tail artifact: '---' + blank + '## 附录：...' after last reference entry
ap = next(i for i, l in enumerate(flines) if l.startswith('## 附录：R2 修订逐条对照表'))
assert '编辑工件' in flines[ap], 'tail artifact self-declaration missing'
assert flines[ap - 1] == '' and flines[ap - 2] == '---' and flines[ap - 3] == '', 'tail artifact boundary'
assert flines[ap - 4].startswith('- R54.'), 'last body line must be R54 entry: ' + flines[ap - 4][:30]
body_lines = flines[8:ap - 3]
raw = '\n'.join(body_lines) + '\n'
print('artifact strip: head L1-L8 (%d chars), tail L%d-L%d (%d chars); body %d lines'
      % (len('\n'.join(flines[:8])), ap + 1, len(flines), len('\n'.join(flines[ap - 2:])), len(body_lines)))
print('body sha256:', hashlib.sha256(raw.encode('utf-8')).hexdigest())

if raw.count('```') or re.search(r'!\[', raw) or re.search(r'\^\[', raw):
    sys.exit('STOP: unexpected markdown structure (code block / image / footnote)')
assert raw.split('\n', 1)[0] == '# ' + TITLE, 'body must start with the H1 title'

# ---------- inline pipeline ----------
store = []

def url_repl(m):
    tok = m.group(0)
    assert not re.search(r'[%#$&{}\\]', tok), 'unsafe char in url: ' + tok
    store.append(r'\url{' + tok + '}')
    return '\x00%d\x00' % (len(store) - 1)

def tt_repl(m):
    tok = m.group(0)
    assert '\\' not in tok and '#' not in tok and '%' not in tok and '&' not in tok and '$' not in tok
    body = tok.replace('_', r'\_\allowbreak ')          # F3': break after _
    body = re.sub(r'(/)', r'\1\\allowbreak ', body)     # F3': break after / ; NOT after . —
    store.append(r'\texttt{' + body + '}')              #   name.ext 保持原子
    return '\x00%d\x00' % (len(store) - 1)

def doi_repl(m):
    body = m.group(1)
    assert '\\' not in body and '#' not in body and '%' not in body and '&' not in body \
        and '$' not in body and '{' not in body and '}' not in body and '_' not in body
    body = re.sub(r'([./:-])', r'\1\\allowbreak ', body)  # F3: break after . / : -
    store.append('DOI:' + body)
    return '\x00%d\x00' % (len(store) - 1)

def inline(s):
    # 0) backslash must not exist in source
    assert '\\' not in s, 'backslash in md: ' + s[:60]
    # 1) protect URLs — [C] full https URLs first (R53/R54 new sources), then legacy bare .com
    s = re.sub(r'https?://\S+', url_repl, s)
    s = re.sub(r'\b[a-z0-9][a-z0-9.-]*\.com/[A-Za-z0-9_/-]+', url_repl, s)
    # 2) file paths (results/... or bare) with json/py/md extension
    s = re.sub(r'\b(?:results/)?[A-Za-z0-9][A-Za-z0-9_]*\.(?:json|py|md)\b', tt_repl, s)
    # 3) dotted field chains containing underscore
    s = re.sub(r'\b[A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)+\b',
               lambda m: tt_repl(m) if '_' in m.group(0) else m.group(0), s)
    # 4) bare snake_case fields
    s = re.sub(r'\b[a-z][a-z0-9]*(?:_[A-Za-z0-9]+)+\b', tt_repl, s)
    # 4.5) DOI identifiers (F3)
    s = re.sub(r'\bDOI:([0-9A-Za-z./-]+)', doi_repl, s)
    # 5) escape specials
    for a, b in [('&', r'\&'), ('%', r'\%'), ('$', r'\$'), ('#', r'\#'), ('{', r'\{'), ('}', r'\}'), ('_', r'\_')]:
        s = s.replace(a, b)
    # 6) straight quotes -> TeX curly (pairwise; assert even count)
    if s.count('"') % 2:
        sys.exit('STOP: odd double-quote count in: ' + s[:80])
    s = re.sub(r'"([^"]*)"', lambda m: '``' + m.group(1) + "''", s)
    # 7) bold then italic
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'\*([^*]+?)\*', r'\\textit{\1}', s)
    # 8) restore placeholders
    s = re.sub('\x00(\\d+)\x00', lambda m: store[int(m.group(1))], s)
    return s

# ---------- parse blocks ----------
out = []
i = 0
body = raw.split('\n')
sec_no = 0
sub_no = {}
in_abstract = False
in_refs = False
para_buf = []
list_mode = None
hdr_fix_count = 0

def flush_para():
    global para_buf
    if para_buf:
        out.append(inline(' '.join(para_buf)))
        out.append('')
        para_buf = []

def close_list():
    global list_mode
    if list_mode:
        out.append('\\end{' + ('itemize' if list_mode == 'item' else 'enumerate') + '}')
        out.append('')
        list_mode = None

def new_list(kind):
    global list_mode
    if list_mode != kind:
        close_list()
        list_mode = kind
        out.append('\\begin{' + ('itemize' if kind == 'item' else 'enumerate') + '}[leftmargin=1.6em,itemsep=2pt,parsep=0pt,topsep=3pt]')

def match_table(lines, idx):
    rows = []
    j = idx
    while j < len(lines) and lines[j].startswith('|'):
        rows.append([c.strip() for c in lines[j].strip().strip('|').split('|')])
        j += 1
    if len(rows) >= 3 and set(''.join(rows[1])) <= set('-: '):
        return rows, j
    return None, idx

TABLE_SPECS = {
    ('#', 'Hard-SF criterion (pool source)'): dict(
        size='\\small',
        colspec='@{}>{\\raggedright\\arraybackslash}p{0.045\\textwidth}>{\\raggedright\\arraybackslash}X>{\\raggedright\\arraybackslash}X>{\\raggedright\\arraybackslash}p{0.155\\textwidth}@{}',
        bold_first=False),
    ('Row (section)', 'T (temporal priority)'): dict(
        size='\\footnotesize',
        colspec='@{}>{\\raggedright\\arraybackslash}p{0.185\\textwidth}>{\\raggedright\\arraybackslash}X>{\\raggedright\\arraybackslash}X>{\\raggedright\\arraybackslash}X@{}',
        bold_first=False),
}

while i < len(body):
    ln = body[i]
    st = ln.strip()
    # F1: consume the H1 title line
    if st.startswith('# ') and not st.startswith('## '):
        assert i == 0 and st == '# ' + TITLE, 'unexpected H1 heading at line %d: %s' % (i + 1, st[:60])
        flush_para(); close_list()
        i += 1; continue
    if not st:
        flush_para(); close_list(); i += 1; continue
    m = re.match(r'^## (.*)$', st)
    if m:
        flush_para(); close_list()
        h = m.group(1)
        if h == 'Abstract':
            in_abstract = True; in_refs = False
            out.append('\\begin{abstract}'); out.append('')
        else:
            if in_abstract:
                # T-1 FIX: close the abstract environment at the first ## heading after Abstract
                out.append('\\end{abstract}'); out.append('')
                in_abstract = False
            if h == 'References':
                in_refs = True
                out.append('\\section*{References}')
            else:
                in_refs = False
                m2 = re.match(r'^(\d+)\.\s+(.*)$', h)
                assert m2, 'unexpected ## heading: ' + h
                n = int(m2.group(1)); assert n == sec_no + 1, 'section seq: ' + h
                sec_no = n; sub_no[n] = 0
                out.append('\\section{' + inline(m2.group(2)) + '}')
        out.append(''); i += 1; continue
    m = re.match(r'^### (.*)$', st)
    if m:
        flush_para(); close_list()
        m2 = re.match(r'^(\d+)\.(\d+)\s+(.*)$', m.group(1))
        assert m2, 'unexpected ### heading: ' + m.group(1)
        n, k = int(m2.group(1)), int(m2.group(2))
        assert n == sec_no and k == sub_no.get(n, 0) + 1, 'subsection seq: ' + m.group(1)
        sub_no[n] = k
        out.append('\\subsection{' + inline(m2.group(3)) + '}')
        out.append(''); i += 1; continue
    rows, j = match_table(body, i)
    if rows:
        flush_para(); close_list()
        spec = TABLE_SPECS.get((rows[0][0], rows[0][1]))
        assert spec, 'unknown table at line %d' % (i + 1)
        out.append('\\begin{table}[htbp]')
        out.append('\\centering')
        out.append(spec['size'])
        out.append('\\setlength{\\tabcolsep}{3.5pt}')
        out.append('\\renewcommand{\\arraystretch}{1.18}')
        out.append('\\begin{tabularx}{0.985\\textwidth}{' + spec['colspec'] + '}')
        out.append('\\toprule')
        hdr_cells = [('No.' if c == '#' else c) for c in rows[0]]   # F2
        hdr_fix_count += sum(1 for c in rows[0] if c == '#')
        hdr = ' & '.join('\\textbf{' + inline(c) + '}' for c in hdr_cells)
        out.append(hdr + ' \\\\')
        out.append('\\midrule')
        for r in rows[2:]:
            assert len(r) == len(rows[0]), 'ragged table row: ' + str(r)
            out.append(' & '.join(inline(c) for c in r) + ' \\\\')
        out.append('\\bottomrule')
        out.append('\\end{tabularx}')
        out.append('\\end{table}')
        out.append('')
        i = j; continue
    m = re.match(r'^\*\*(Pool .*)\*\*$', st)
    if m and in_refs:
        flush_para(); close_list()
        out.append('\\medskip')
        out.append('\\noindent\\textbf{' + inline(m.group(1)) + '}\\par\\addvspace{2pt}')
        out.append(''); i += 1; continue
    m = re.match(r'^- (.*)$', st)
    if m:
        flush_para()
        new_list('item')
        if in_refs:
            m2 = re.match(r'^(R\d\d)\.\s+(.*)$', m.group(1))
            assert m2, 'ref entry format: ' + m.group(1)[:40]
            out.append('\\item[' + m2.group(1) + '.] ' + inline(m2.group(2)))
        else:
            out.append('\\item ' + inline(m.group(1)))
        i += 1; continue
    m = re.match(r'^(\d+)\.\s+(.*)$', st)
    if m and not in_refs and int(m.group(1)) < 10:
        flush_para()
        new_list('enum')
        out.append('\\item ' + inline(m.group(2)))
        i += 1; continue
    close_list()
    if in_abstract:
        out.append(inline(st)); out.append('')
    else:
        para_buf.append(st)
    i += 1

flush_para(); close_list()
if in_abstract:
    out.append('\\end{abstract}'); out.append('')

PREAMBLE = r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{pifont}% Zapf Dingbats circled digits (pdflatex-safe)
\usepackage{newunicodechar}
% --- engine-compatibility layer: pdflatex; text body unchanged (v9 system) ---
\newunicodechar{①}{\texorpdfstring{\ding{172}}{1}}
\newunicodechar{②}{\texorpdfstring{\ding{173}}{2}}
\newunicodechar{③}{\texorpdfstring{\ding{174}}{3}}
\newunicodechar{④}{\texorpdfstring{\ding{175}}{4}}
\newunicodechar{⑤}{\texorpdfstring{\ding{176}}{5}}
\newunicodechar{⑥}{\texorpdfstring{\ding{177}}{6}}
% Greek letters in running text -> math
\newunicodechar{τ}{\ensuremath{\tau}}
\newunicodechar{κ}{\ensuremath{\kappa}}
\newunicodechar{Φ}{\ensuremath{\Phi}}
\newunicodechar{Δ}{\ensuremath{\Delta}}
\newunicodechar{λ}{\ensuremath{\lambda}}
\newunicodechar{Σ}{\ensuremath{\Sigma}}
% operators in running text
\newunicodechar{≠}{\ensuremath{\neq}}
\newunicodechar{≤}{\ensuremath{\leq}}
\newunicodechar{∈}{\ensuremath{\in}}
\newunicodechar{∗}{\textasteriskcentered}
\newunicodechar{−}{\ensuremath{-}}
\DeclareUnicodeCharacter{2192}{\textrightarrow}% F4: silent redefine (utf8 default exists)
% superscript digits/minus (scientific notation) -> text superscript
\newunicodechar{⁻}{\textsuperscript{\textminus}}
\newunicodechar{⁴}{\textsuperscript{4}}
\newunicodechar{⁶}{\textsuperscript{6}}
\newunicodechar{⁹}{\textsuperscript{9}}
\DeclareUnicodeCharacter{00B9}{\textsuperscript{1}}% F4: style-unified with \textsuperscript
\DeclareUnicodeCharacter{00B2}{\textsuperscript{2}}% F4: style-unified with \textsuperscript
% XeTeX allows line breaks after en/em dashes; restore that for pdflatex
\DeclareUnicodeCharacter{2013}{\texorpdfstring{\textendash\allowbreak}{\textendash}}% F4
\DeclareUnicodeCharacter{2014}{\texorpdfstring{\textemdash\allowbreak}{\textemdash}}% F4
\usepackage{amsmath,amssymb}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\PassOptionsToPackage{hyphens}{url}% F8: \url 允许在连字符后断行（R37 长条目 Underfull 根因）
\usepackage[pdftitle={Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews},pdfauthor={}]{hyperref}
\usepackage{url}
\usepackage{enumitem}
\usepackage[margin=1in]{geometry}
% F7: 节/小节标题 raggedright（标准惯例；仅换行标题受影响——消除 §8 两行标题的两端拉伸，字形零变化）
\makeatletter
\renewcommand\section{\@startsection{section}{1}{\z@}%
  {-3.5ex \@plus -1ex \@minus -.2ex}{2.3ex \@plus .2ex}%
  {\normalfont\Large\bfseries\raggedright}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
  {-3.25ex\@plus -1ex \@minus -.2ex}{1.5ex \@plus .2ex}%
  {\normalfont\large\bfseries\raggedright}}
\makeatother
\tolerance=900% F10（申报）：残余 badness 1092/1331 两行系内容层固有错配（下一词差 1-2pt 塞不进，
%        改词被禁、microtype 不可用）；降 tolerance 触发 emergencystretch 第二次机会——
%        版面断行不变，报告 badness 计入 3em 应急伸展后降至阈值内。TeX 标准机制，非 \hbadness 掩蔽。
\emergencystretch=3em

% Double-blind local final: no author block, no date, clean PDF metadata (D1--D6).
\title{Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews}
\author{}
\date{}
\begin{document}
\maketitle
\thispagestyle{empty}
'''

tex = PREAMBLE + '\n' + '\n'.join(out).rstrip() + '\n\n\\end{document}\n'
open(OUT, 'w', encoding='utf-8').write(tex)

# ---------- content-zero assertions (on stripped paper body) ----------
md_cites = sorted(re.findall(r'\[R\d\d\]', raw))
tx_cites = sorted(re.findall(r'\[R\d\d\]', tex))
assert md_cites == tx_cites, 'citation token multiset mismatch'
md_fc = sorted(re.findall(r'F-C\d', raw)); tx_fc = sorted(re.findall(r'F-C\d', tex))
assert md_fc == tx_fc, 'F-C multiset mismatch'
md_refs = len(re.findall(r'^- R\d\d\.', raw, re.M))
tx_refs = len(re.findall(r'\\item\[R\d\d\.\]', tex))
assert md_refs == tx_refs == 54, 'reference entry count %d/%d' % (md_refs, tx_refs)   # [D]
md_secs = re.findall(r'^## (.+)$', raw, re.M)
assert hdr_fix_count == 1, 'header # -> No. transform count %d' % hdr_fix_count   # F5
assert tex.count('\\#') == 0, 'escaped # residue in tex'                            # F5
body_part = '\n'.join(out)
assert TITLE not in body_part, 'title leaked into body'                             # F5
for anchor in ['aeefb8ef6972', '9bbe43f41fa8', '6e9673205dc0', '68a5b08ef007', '6b09de9911c0']:
    assert raw.count(anchor) == tex.count(anchor) == 1, 'anchor invariant: ' + anchor
# editorial artifact must be fully stripped
for tok in ['修订版说明', '逐条对照表', 'META_REVIEW_REPORT', 'REVIEW_RB', '编辑工件']:
    assert tok not in tex, 'artifact token leaked into tex: ' + tok
# new-source URL protection (rendering-layer): R53/R54 https URLs inside \url{}
for u in ['https://www.emis.de/classics/Riemann/WKCGeom.tex',
          'https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Geom/',
          'https://en.wikisource.org/wiki/On_the_Space-Theory_of_Matter']:
    assert '\\url{' + u + '}' in tex, 'unprotected new URL: ' + u
assert '\\texttt{of' not in tex and '\\texttt{of\\_' not in tex, 'snake-case leak on URL fragment'
# ---- T-1 structural assertions (visual-semantics layer, generation-time) ----
assert tex.count('\\begin{abstract}') == 1 and tex.count('\\end{abstract}') == 1, 'abstract env count != 1'
ab = tex.index('\\begin{abstract}'); ae = tex.index('\\end{abstract}')
fs = tex.index('\\section{', tex.index('\\begin{document}'))
assert ab < ae < fs, 'T-1: \\end{abstract} (pos %d) must precede first \\section (pos %d)' % (ae, fs)
inner = tex[ab + len('\\begin{abstract}'):ae]
for forbidden in ['\\section', '\\subsection', '\\begin{table}', '\\begin{itemize}', '\\begin{enumerate}', '\\item']:
    assert forbidden not in inner, 'T-1: structural block %s inside abstract env' % forbidden
print('T-1 gate: abstract env spans chars [%d,%d); first \\section at %d; inner blocks: none' % (ab, ae, fs))
print('OK: cites %d, F-C %d, refs %d, sections %d' % (len(md_cites), len(md_fc), tx_refs, len(md_secs)))
print('placeholders used:', len(store))
print('first-appearance order:', ', '.join('R' + k for k in dict.fromkeys(re.findall(r'\[R(\d\d)\]', raw)).keys()))
