# -*- coding: utf-8 -*-
"""Read-only side-by-side compliance audit of:
  audit3_extract = our locked pipeline output
  audit4_extract = current on-disk (MiniMax rewrite) tars
Checks the user's full requirement set. No files are modified."""
import os, re, sys

WORK = r'c:\Users\Administrator\.trae-cn\work\6a9a7e1c7578e46bf7c7f60c'
BS = chr(92)  # backslash

FORBID_XELUA = ['fontspec', 'xecjk', 'ctex', 'luatextra', 'luacode',
                'polyglossia', 'luatexbase', 'luaotfload', 'xeCJK']

def find_tex(root, langtag):
    hits = []
    for r, d, fs in os.walk(root):
        for f in fs:
            if f.endswith('.tex'):
                p = os.path.join(r, f)
                if (langtag == 'en' and f.endswith('_en.tex')) or \
                   (langtag == 'cn' and f.endswith('_cn.tex')):
                    hits.append(p)
    return sorted(hits)

def pkgdir_of(texpath):
    return os.path.dirname(texpath)

def audit(texpath, label):
    raw = open(texpath, 'rb').read()
    text = raw.decode('utf-8', errors='replace')
    lines = text.splitlines()
    pkgdir = pkgdir_of(texpath)
    R = {'label': label, 'path': texpath, 'size': len(raw)}

    # line1 pdfoutput
    l1 = lines[0].strip() if lines else ''
    R['line1'] = l1
    R['pdfoutput_line1'] = l1.replace(' ', '') == (BS + 'pdfoutput=1')

    # packages
    pkgs = re.findall(r'\\usepackage(?:\[[^\]]*\])?\{([^}]*)\}', text)
    pkglist = [p.strip() for grp in pkgs for p in grp.split(',')]
    R['packages'] = pkglist
    low = [p.lower() for p in pkglist]
    R['forbidden_xelua'] = [p for p in low if any(f in p for f in ['fontspec', 'xecjk', 'ctex', 'luatextra', 'luacode', 'polyglossia', 'luaotfload', 'luatexbase'])]
    R['cjk_pkg'] = [p for p in pkglist if 'CJK' in p or 'cjk' in p.lower()]
    R['cjk_begin'] = len(re.findall(r'\\begin\{CJK\}', text))
    R['cjk_end'] = len(re.findall(r'\\end\{CJK\}', text))

    # graphicspath + figures
    gm = re.search(r'\\graphicspath\s*\{((?:\{[^{}]*\}\s*)+)\}', text)
    gdirs = re.findall(r'\{([^{}]*)\}', gm.group(1)) if gm else []
    R['graphicspath'] = gdirs
    search_dirs = [pkgdir] + [os.path.join(pkgdir, d) for d in gdirs]
    inc = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}', text)
    R['includegraphics'] = inc
    missing_fig = []
    for name in inc:
        base = name
        found = False
        for sd in search_dirs:
            for cand in (base, base + '.png', base + '.pdf', base + '.jpg', base + '.jpeg'):
                if os.path.isfile(os.path.join(sd, cand)):
                    found = True
                    break
            if found:
                break
        if not found:
            missing_fig.append(name)
    R['missing_figures'] = missing_fig

    # external commands / includes
    R['bibliography_cmd'] = len(re.findall(r'\\bibliography\{', text))
    R['input_cmd'] = len(re.findall(r'\\input\{', text))
    R['include_cmd'] = len(re.findall(r'\\include\{', text))
    R['bibliography_env'] = len(re.findall(r'\\begin\{thebibliography\}', text))
    R['bibitems'] = len(re.findall(r'\\bibitem', text))

    # cite closure
    cited = set()
    for m in re.findall(r'\\cite\{([^}]*)\}', text):
        for k in m.split(','):
            cited.add(k.strip())
    defined = set(re.findall(r'\\bibitem(?:\[[^\]]*\])?\{([^}]*)\}', text))
    R['cited'] = len(cited)
    R['defined_bib'] = len(defined)
    R['missing_cites'] = sorted(cited - defined)

    R['labels'] = len(re.findall(r'\\label\{', text))
    R['refs'] = len(re.findall(r'\\ref\{', text))

    # sections
    secs = re.findall(r'\\(section|appendix)\*?\{([^}]*)\}', text)
    R['sections'] = [(c, t.strip()) for c, t in secs]
    R['has_appendix'] = BS + 'appendix' in text

    # abstract length excluding Keywords line
    abm = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', text, re.S)
    abs_chars = None
    abs_body = ''
    if abm:
        ab = abm.group(1)
        keep = []
        for ln in ab.splitlines():
            s = ln.strip()
            if s.startswith(BS + 'textbf{Keywords') or s.startswith(BS + 'textbf{关键词') or s.startswith('Keywords') or s.startswith('关键词'):
                continue
            keep.append(ln)
        abs_body = '\n'.join(keep)
        # strip latex commands/braces for a conservative visible-char count
        vis = re.sub(r'\\[a-zA-Z]+\*?(\[[^\]]*\])?', '', abs_body)
        vis = vis.replace('{', '').replace('}', '')
        vis = re.sub(r'\s+', '', vis)
        abs_chars = len(vis)
    R['abstract_chars_excl_keywords'] = abs_chars
    R['has_keywords_line'] = bool(abm and ('Keywords' in abm.group(1) or '关键词' in abm.group(1)))

    # footnotes
    fns = re.findall(r'\\footnote\{([^}]*)\}', text)
    R['footnotes'] = [f[:80] for f in fns]

    # quote env
    R['quote_begin'] = len(re.findall(r'\\begin\{quote\}', text))
    R['quote_end'] = len(re.findall(r'\\end\{quote\}', text))

    # content rules
    R['has_yuanqihao'] = ('袁祺皓' in text) or ('Qihao' in text) or ('Yuanqihao' in text) or ('Qihao Yuan' in text)
    R['has_ruc_chem'] = ('中国人民大学' in text and ('化学与生命资源' in text)) or ('Renmin University' in text)
    R['mentions_wangzihe'] = '王子贺' in text
    R['mentions_kimi'] = ('KIMI' in text) or ('Kimi' in text) or ('Moonshot' in text)
    R['fund_numbers'] = re.findall(r'(?:Grant|基金|NSFC|国家自然科学基金)[^\n]{0,40}', text)
    # AI residue outside the AI section (rough): count mentions of common AI names in whole doc
    R['ai_name_hits'] = {k: len(re.findall(k, text)) for k in ['KIMI', 'Kimi', 'ChatGPT', 'Claude', 'GPT', 'Moonshot', 'MiniMax', '豆包', 'Doubao']}

    # title/author
    tm = re.search(r'\\title\{([^}]*)\}', text)
    am = re.search(r'\\author\{([^}]*)\}', text)
    R['title'] = (tm.group(1)[:90] if tm else None)
    R['author'] = (am.group(1)[:120] if am else None)

    return R

def show(R):
    print('='*78)
    print('[%s]  size=%d  path=%s' % (R['label'], R['size'], R['path']))
    print('  line1            :', repr(R['line1']), '| pdfoutput_line1 =', R['pdfoutput_line1'])
    print('  packages         :', R['packages'])
    print('  FORBIDDEN xe/lua :', R['forbidden_xelua'])
    print('  CJK pkg/begin/end:', R['cjk_pkg'], R['cjk_begin'], R['cjk_end'])
    print('  graphicspath     :', R['graphicspath'])
    print('  includegraphics  :', R['includegraphics'])
    print('  missing figures  :', R['missing_figures'])
    print('  bib/input/include :', R['bibliography_cmd'], R['input_cmd'], R['include_cmd'], '| bibenv', R['bibliography_env'])
    print('  bibitems/cited   :', R['bibitems'], R['cited'], '| defined', R['defined_bib'], '| missing', R['missing_cites'])
    print('  label/ref        :', R['labels'], R['refs'])
    print('  has_appendix     :', R['has_appendix'])
    print('  abstract chars   :', R['abstract_chars_excl_keywords'], '(<1920)' if (R['abstract_chars_excl_keywords'] or 0) < 1920 else '(>=1920!)', '| keywords_line', R['has_keywords_line'])
    print('  footnotes        :', R['footnotes'])
    print('  quote begin/end  :', R['quote_begin'], R['quote_end'])
    print('  袁祺皓/RUC chem    :', R['has_yuanqihao'], R['has_ruc_chem'])
    print('  王子贺 present    :', R['mentions_wangzihe'], '| fund hits:', R['fund_numbers'])
    print('  KIMI/Moonshot    :', R['mentions_kimi'], '| ai_name_hits:', R['ai_name_hits'])
    print('  title            :', R['title'])
    print('  author           :', R['author'])
    print('  --- sections (in order) ---')
    for c, t in R['sections']:
        print('     %-9s %s' % (c, t[:70]))

pairs = []
for lang in ('en', 'cn'):
    a3 = find_tex(os.path.join(WORK, 'audit3_extract'), lang)
    a4 = find_tex(os.path.join(WORK, 'audit4_extract'), lang)
    if a3:
        pairs.append((audit(a3[0], 'OURS-audit3-' + lang),))
    if a4:
        pairs.append((audit(a4[0], 'MINIMAX-audit4-' + lang),))

for (R,) in pairs:
    show(R)
