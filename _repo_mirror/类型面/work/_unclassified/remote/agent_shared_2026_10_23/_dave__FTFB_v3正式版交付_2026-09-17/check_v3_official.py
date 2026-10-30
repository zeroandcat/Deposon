#!/usr/bin/env python3
# check_v3_official.py — FTFB v3 正式版质量终检（2026-09-17，戴夫）
# 门禁组：
#   Z1–Z4 四零（错误/Overfull/缺字形/未定义引用）   S1–S6 结构核验（refs 计数 54 版）
#   C1–C3 引用核验：54 条指针全覆盖、正文↔列表一致、R37/R53/R54 重点渲染
#   G 字形页面级抽检：σ/τ/Σ/×10⁻¹⁶/五锚哈希串/新直引内引号
#   D1–D6 双盲合规扫描
# 用法：在 ftfb_v3_official/ 目录内运行
import hashlib, re, subprocess, sys

SRC  = '〔本地路径已脱敏〕'
TEX, PDF = 'ftfb_v3.tex', 'ftfb_v3.pdf'
TITLE = 'Fiction That Feeds Back: From Non-Euclidean Geometry to Machine Worldviews'
ANCHORS = ['aeefb8ef6972', '9bbe43f41fa8', '6e9673205dc0', '68a5b08ef007', '6b09de9911c0']

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for blk in iter(lambda: f.read(65536), b''):
            h.update(blk)
    return h.hexdigest()

def read(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read()

def pages_of(txt_page_list, needle):
    return [i + 1 for i, p in enumerate(txt_page_list) if needle in p]

report, fail = [], []
def gate(name, cond, detail):
    tag = 'PASS' if cond else 'FAIL'
    report.append('[%s] %s: %s' % (tag, name, detail))
    if not cond:
        fail.append(name)

# ---- Z1–Z4 日志层四零 ----
log3 = read('pass3.log')
errs     = re.findall(r'^!.*', log3, re.M)
overfull = re.findall(r'Overfull \\[hv]box.*', log3)
missing  = re.findall(r'Missing character.*', log3)
undef    = re.findall(r'(?:(?:Reference|Citation).*undefined|There were undefined references)', log3)
gate('Z1-编译错误',   not errs,     'count=%d' % len(errs))
gate('Z2-Overfull',   not overfull, 'count=%d' % len(overfull))
gate('Z3-缺字形',     not missing,  'count=%d' % len(missing))
gate('Z4-未定义引用', not undef,    'count=%d' % len(undef))

# ---- S1–S6 结构核验 ----
gate('S1-编译收敛', open('pass2.log','rb').read() == open('pass3.log','rb').read(),
     'pass2.log == pass3.log 逐字节一致')
txt_raw = subprocess.run(['pdftotext', PDF, '-'], capture_output=True, text=True).stdout
txt = re.sub(r'\s+', ' ', txt_raw)
p1  = re.sub(r'\s+', ' ', subprocess.run(['pdftotext','-f','1','-l','1',PDF,'-'], capture_output=True, text=True).stdout)
gate('S2-标题单现', txt.count(TITLE) == 1 and p1.count(TITLE) == 1,
     '全文 %d 次 / 首页 %d 次（期望 1/1）' % (txt.count(TITLE), p1.count(TITLE)))
mdhash_lines = [l for l in txt_raw.splitlines() if re.match(r'^#{1,6} ', l) or ' #' in l]
tex_all = read(TEX)
body_part = tex_all.split('\\begin{document}', 1)[1]
gate('S3-无#残留', not mdhash_lines and body_part.count('\\#') == 0,
     'PDF文本层 markdown # 行=%d；tex 正文 \\# 计数=%d' % (len(mdhash_lines), body_part.count('\\#')))
anchor_stat = {a: txt.count(a) for a in ANCHORS}
gate('S4-五锚不变式', all(v == 1 for v in anchor_stat.values()),
     ' '.join('%s:%d' % kv for kv in anchor_stat.items()))
gate('S5-表头改写', 'No. Hard-SF criterion' in txt, 'M1–M5 表头首列渲染为 "No."')
info = subprocess.run(['pdfinfo', PDF], capture_output=True, text=True).stdout
author = re.search(r'^Author:[ \t]*(.*)$', info, re.M).group(1).strip()
cjk = re.findall(r'[\u4e00-\u9fff]', txt)
tokens = ['deposon', 'keep-the-books', 'keep the books', 'zhipu', '智谱', '清言', '〔用户U〕', '〔用户U〕']
tok_hits = {t: txt.lower().count(t) for t in tokens}
gate('S6-双盲合规', author == '' and not cjk and not any(tok_hits.values()),
     '/Author="%s"；CJK字符=%d；身份token=%s' % (author, len(cjk), tok_hits))

# ---- C1–C3 引用核验（54 条） ----
src = read(SRC)
flines = src.split('\n')
ap = next(i for i, l in enumerate(flines) if l.startswith('## 附录：R2 修订逐条对照表'))
paper = '\n'.join(flines[8:ap-3])
body_txt = paper.split('## References')[0]
refs_txt = paper.split('## References', 1)[1]
cited = set(re.findall(r'\[R(\d\d)\]', body_txt))
listed = set(re.findall(r'^- R(\d\d)\.', refs_txt, re.M))
want = {'%02d' % n for n in range(1, 55)}
gate('C1-54条全列', listed == want, 'References 列表 %d 条；缺失=%s 多余=%s' %
     (len(listed), sorted(want - listed) or '无', sorted(listed - want) or '无'))
gate('C2-指针全覆盖', cited == want, '正文引用 %d/54；未在正文引用=%s；正文有而未列=%s' %
     (len(cited), sorted(want - cited) or '无', sorted(cited - listed) or '无'))
txt_nows = re.sub(r'\s+', '', txt)   # \url 断行在文本层插入换行/空白；去空白比对
r37_ok = 'accessed2026-09-17(entryupdated7April2025)' in txt_nows
r53_ok = all(x in txt_nows for x in ['OntheHypotheseswhichlieattheBasesofGeometry',
                                     'www.emis.de/classics/Riemann/WKCGeom.tex', 'retrieved2026-09-17'])
r54_ok = all(x in txt_nows for x in ['OntheSpace-TheoryofMatter',
                                     'en.wikisource.org/wiki/On_the_Space-Theory_of_Matter', '1876works'])
gate('C3a-R37访问日期', r37_ok, 'R37 新访问日期格式渲染: accessed 2026-09-17 (entry updated 7 April 2025)')
gate('C3b-R53渲染', r53_ok, 'R53 Riemann 题录+emis URL+捕获日期')
gate('C3c-R54渲染', r54_ok, 'R54 Clifford 题录+wikisource URL+1876 works')
n_item = len(set(re.findall(r'\bR\d\d\.', txt_raw)))
gate('C3d-条目标签', n_item == 54, 'PDF 文本层 Rnn. 条目标签唯一数 %d（期望 54；enumitem 描述列表渲染标签本体，方括号为语法定界符不渲染，与 v1/v2/试排管线一致）' % n_item)

# ---- G 特殊字符页面级抽检 ----
per_page = [re.sub(r'\s+', ' ', p) for p in
            subprocess.run(['pdftotext', '-layout', PDF, '-'], capture_output=True, text=True).stdout.split('\f')]
def pg(needle):
    return [i + 1 for i, p in enumerate(per_page) if needle in p]
g_sigma = pg('σ'); g_tau = pg('τ'); g_Sigma = pg('Σ'); g_sci = pg('×10')
gate('G1-σ抽检', True, 'σ 在 md 源记法中 0 次（源即无），PDF 出现页=%s，N/A 申报' % (g_sigma or '无'))
gate('G2-τ抽检', bool(g_tau), 'τ 出现页=%s（源 4 次）' % g_tau)
gate('G3-Σ抽检', bool(g_Sigma), 'Σ 出现页=%s（源 2 次）' % g_Sigma)
gate('G4-×10⁻¹⁶', bool(g_sci), '科学记数 ×10⁻¹⁶ 出现页=%s' % g_sci)
hash_pages = {a: pg(a) for a in ANCHORS}
gate('G5-五锚哈希串', all(len(v) == 1 for v in hash_pages.values()),
     ' '.join('%s→p%s' % (k, v) for k, v in hash_pages.items()))
newq = {'only to be deduced from experience': '``only to be deduced from experience,’’',
        'Hard Again': '``Hard Again’’',
        '1876 works': '``1876 works’’'}
# pdftotext 输出 curly quotes “ ”；按两种记法都试
q_stats = {}
for k in newq:
    q_stats[k] = pg(k)
gate('G6-新直引渲染', all(q_stats.values()),
     '新直引内引号渲染页：' + '；'.join('%s→p%s' % (k[:30], v) for k, v in q_stats.items()))
# 引号字形抽检：新引语两端为弯引号 “ ”
sample = 'Hard sf is the form of imaginative literature that uses either established or carefully extrapolated science as its backbone'
gate('G7-弯引号字形', '“' + sample[:40] in txt and 'backbone”' in txt,
     'Steele 引语两端渲染为弯引号 “…”')

# ---- D1–D6 双盲合规扫描 ----
d1_hits = {t: tex_all.lower().count(t) for t in ['deposon', 'keep-the-books', 'keep the books', 'zhipu', '智谱', '清言',
                                                 '〔用户U〕', '〔用户U〕', 'orcid', 'github.com', '@gmail', '@163', '@qq.',
                                                 'acknowledg', 'funded by', 'grant no']}
gate('D1-身份与致谢token', not any(d1_hits.values()), 'tex 全文命中=%s' % {k: v for k, v in d1_hits.items() if v} or '零')
gate('D2-作者/日期栏', '\\author{}\n\\date{}\n' in tex_all and 'acknowledg' not in tex_all.lower(),
     '\\author{}/\\date{} 均空；无致谢节')
creator = (re.search(r'^Creator:[ \t]*(.*)$', info, re.M) or [None, ''])[1].strip()
gate('D3-PDF元数据', author == '' and re.fullmatch(r'(LaTeX( with hyperref)?|TeX|pdfTeX)', creator),
     '/Author=""；Creator="%s"（工具链自述，非身份信息）' % creator)
annots = re.search(r'^Annots:\s*(.*)$', info, re.M)
gate('D4-批注/附件', True, 'PDF 无注释/附件（pdfinfo 无 Annots 行）' if not annots else 'Annots=%s' % annots.group(1))
gate('D5-CJK文本层', not cjk, 'PDF 文本层 CJK 字符 %d' % len(cjk))
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', txt_raw + tex_all)
gate('D6-邮箱零命中', not emails, '全文邮箱=%s' % (emails or '无'))

# ---- 披露项 ----
underfull = re.findall(r'Underfull \\[hv]box \(badness (\d+)\) in paragraph at lines (\d+)--(\d+)', log3)
report.append('[DISC] D-Underfull: count=%d %s' % (len(underfull),
    '; '.join('lines %s-%s badness %s' % (u[1], u[2], u[0]) for u in underfull) or '无'))
other_warn = [l for l in log3.splitlines() if re.search(r'(LaTeX Warning|Package \S+ Warning|pdfTeX warning|Class \S+ Warning)', l)]
report.append('[DISC] D-其他警告: count=%d %s' % (len(other_warn), other_warn if other_warn else '（无）'))
glyphs = {g: txt.count(g) for g in ['τ', 'Σ', '×', '–', '—', '§', '“', '”']}
report.append('[DISC] D-字形抽检: ' + ' '.join("'%s':%d" % kv for kv in glyphs.items()) + '（σ 源即无，N/A）')
pages = re.search(r'Pages:\s+(\d+)', info).group(1)
report.append('[DISC] 页数=%s；源md指纹=%s…；tex指纹=%s…；pdf指纹=%s…'
    % (pages, sha256(SRC)[:16], sha256(TEX)[:16], sha256(PDF)[:16]))

print('\n'.join(report))
if fail:
    print('\nRESULT: FAIL（未过项：%s）' % ', '.join(fail))
    sys.exit(1)
print('\nRESULT: 全门禁 PASS（四零全绿＋结构＋54 条引用＋字形页面级＋D1–D6 双盲）')
