#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""v156 裁答函独立复核验证器（鲍勃 · 2026-10-20）
纪律：0 改函一字 · 只读（仅磁盘字节回读）· 0 传出
派单：管理员 21:07:52【v156 裁答函·独立复核回执】
"""
import hashlib, json, os, re, subprocess

PATH = '〔本地路径已脱敏〕'
PRIV = '〔本地路径已脱敏〕'
OUT = os.path.join(PRIV, 'bob_v156_result.json')

data = open(PATH, 'rb').read()
text = data.decode('utf-8')  # strict 解码；若失败此处即抛错
R = {'object': PATH, 'mtime': None}

st = os.stat(PATH)
import datetime
R['mtime_local'] = datetime.datetime.fromtimestamp(st.st_mtime).isoformat(sep=' ')

# ---------- §1 终态实测 ----------
sha_full = hashlib.sha256(data).hexdigest()
R['terminal'] = dict(
    sha256_full=sha_full,
    sha12=sha_full[:12],
    bytes=len(data),
    lf=data.count(b'\n'),
    cr=data.count(b'\r'),
    tab=data.count(b'\t'),
    vt=data.count(b'\x0b'),
    bom=bool(data[:3] == b'\xef\xbb\xbf'),
    utf8_strict='OK',
    ufffd=text.count('\ufffd'),
)

lines = text.split('\n')
if lines and lines[-1] == '':
    lines = lines[:-1]  # 尾 LF
R['n_lines'] = len(lines)

# 行首偏移表
starts = [0]
pos = -1
while True:
    pos = data.find(b'\n', pos + 1)
    if pos == -1:
        break
    if pos + 1 < len(data):
        starts.append(pos + 1)
R['n_line_starts'] = len(starts)

# ---------- §2 append-only 验证 ----------
TARGET = 'b1045e7c7d4c'   # 函 §7-3 自报前态 SHA-12
T_BYTES = 28369
T_LF = 275

# (a) 定长切点（自报 bytes=28369 → 唯一候选位）
p = data[:T_BYTES]
exact = dict(
    kind='self-report-length', pos=T_BYTES, bytes=len(p),
    sha12=hashlib.sha256(p).hexdigest()[:12], lf=p.count(b'\n'),
    hit=(hashlib.sha256(p).hexdigest()[:12] == TARGET and len(p) == T_BYTES and p.count(b'\n') == T_LF),
)
R['cut_exact'] = exact

# (b) 节界切点试切（所有 # 起头行的行首位）
header_cuts = []
for off, ln in zip(starts, lines):
    if ln.startswith('#'):
        pre = data[:off]
        h12 = hashlib.sha256(pre).hexdigest()[:12]
        header_cuts.append(dict(
            line=ln[:46], pos=off, bytes=off, lf=pre.count(b'\n'),
            sha12=h12, hit=(h12 == TARGET),
        ))
R['header_cuts'] = header_cuts
R['header_cut_hits'] = [c for c in header_cuts if c['hit']]

# (c) 全行首位扫描（任意行首切点命中目标哈希，不论长度）
line_scan_hits = []
for off in starts:
    if hashlib.sha256(data[:off]).hexdigest()[:12] == TARGET:
        line_scan_hits.append(off)
R['line_start_scan_hits'] = line_scan_hits

if exact['hit']:
    # 前缀（首写面）补充实测
    ptext = data[:T_BYTES].decode('utf-8')
    R['prefix'] = dict(
        bytes=T_BYTES, sha12=TARGET, lf=T_LF,
        bom=bool(data[:3] == b'\xef\xbb\xbf'),
        cr=data[:T_BYTES].count(b'\r'),
        tab=data[:T_BYTES].count(b'\t'),
        vt=data[:T_BYTES].count(b'\x0b'),
        ufffd=ptext.count('\ufffd'),
        utf8_strict='OK',
        n_lines=T_LF,  # 每行恰一 LF → 行数=LF 数
        last_two_lines=ptext.split('\n')[-3:-1],
    )
    # 追加段（二写面）
    suf = data[T_BYTES:]
    suf_lines = suf.decode('utf-8').split('\n')
    if suf_lines and suf_lines[-1] == '':
        suf_lines = suf_lines[:-1]
    R['suffix'] = dict(
        bytes=len(suf), lf=suf.count(b'\n'),
        cr=suf.count(b'\r'), tab=suf.count(b'\t'), vt=suf.count(b'\x0b'),
        n_lines=len(suf_lines),
        first_line=suf_lines[0][:80],
        last_line=suf_lines[-1][:80],
        first_line_no=T_LF + 1,
        last_line_no=T_LF + len(suf_lines),
    )
    # 算术自洽
    R['arith'] = dict(
        bytes=(T_BYTES + len(suf) == len(data)),
        lf=(T_LF + suf.count(b'\n') == data.count(b'\n')),
    )

# ---------- §3 内部自洽 ----------
def section(name_from, name_to, lines):
    i0 = next(i for i, s in enumerate(lines) if s.startswith(name_from))
    i1 = next(i for i, s in enumerate(lines) if s.startswith(name_to)) if name_to else len(lines)
    return i0, i1

def data_rows(lines, i0, i1):
    rows = []
    for s in lines[i0:i1]:
        m = re.match(r'^\|\s*(\d+)\s*\|', s)
        if m:
            rows.append(int(m.group(1)))
    return rows

ranges = {
    '§1-1': ('### §1-1', '### §1-2'), '§1-2': ('### §1-2', '### §1-3'),
    '§1-3': ('### §1-3', '### §1-4'), '§1-4': ('### §1-4', '📌 **本函之转达声明**'),
    '§7-1': ('### §7-1', '### §7-2'),
}
tbl = {}
for k, (a, b) in ranges.items():
    i0, i1 = section(a, b, lines)
    rows = data_rows(lines, i0, i1)
    tbl[k] = dict(n=len(rows), nums=rows, span=(i0 + 1, i1))
R['tables'] = tbl
allnums = tbl['§1-1']['nums'] + tbl['§1-2']['nums'] + tbl['§1-3']['nums'] + tbl['§1-4']['nums']
R['tables']['§1_sum'] = dict(n=len(allnums), continuous=(allnums == list(range(1, 25))))

# 卷首编码声明 vs 实测
enc_line = next((s for s in lines[:20] if '编码' in s and 'UTF-8' in s), None)
R['enc_decl'] = dict(line=enc_line, line_no=lines.index(enc_line) + 1 if enc_line else None,
                     bom_no=not R['terminal']['bom'],
                     pure_lf=R['terminal']['cr'] == 0,
                     utf8_ok=R['terminal']['utf8_strict'] == 'OK')

# 附：卷首硬约束机械可核面（函 §7-1 自检行 2/3/4/6 之可机核子面）
R['scan'] = dict(
    full_urls=re.findall(r'https?://\S+|ftp://\S+', text),
    cred_forms=[m for m in re.findall(r'ghp_[A-Za-z0-9]{16,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|sk-[A-Za-z0-9]{18,}', text)],
    member_names=[w for w in ['查理', '爱丽丝', '鲍勃', '戴夫', '阿兰', '〔用户U〕', '〔用户U〕',
                              '〔当事人W〕', '〔W老师〕', 'zeroandcat', '6a962cc', '69bd2822', '6a59935e'] if w in text],
    agent_ids=re.findall(r'6a9[0-9a-f]{20,}|69bd[0-9a-f]{20,}|6a59[0-9a-f]{20,}', text),
)

# ---------- §4 边界登记：五源件本地可得性探测 ----------
STEMS = [
    '_glm_dualtrack_paper_reply_2026_10_18',
    '_pi_card_answers_register_2026_10_20_v156',
    '_commission_glm_dualtrack_paper_v0.7_2026_10_18',
    '_commission_glm_supplement_509_repair_v0.4_2026_10_18',
    '_stage5_glm_onhold_and_resume_directive_effect_2026_10_18',
]
roots = ['〔本地路径已脱敏〕', '〔本地路径已脱敏〕', '〔本地路径已脱敏〕']
found = {s: [] for s in STEMS}
pi_rulings_dirs = []
for root in roots:
    if not os.path.isdir(root):
        continue
    for dirpath, dirnames, filenames in os.walk(root):
        for d in dirnames:
            if 'pi_rulings' in d:
                pi_rulings_dirs.append(os.path.join(dirpath, d))
        for f in filenames:
            for s in STEMS:
                if s in f:
                    found[s].append(os.path.join(dirpath, f))
R['source_probe'] = dict(stems=STEMS, roots=roots, found=found, pi_rulings_dirs=pi_rulings_dirs)

try:
    head = subprocess.run(['git', '-C', '〔本地路径已脱敏〕', 'rev-parse', 'HEAD'],
                          capture_output=True, text=True, timeout=30).stdout.strip()
    R['repo_head'] = head
except Exception as e:
    R['repo_head'] = f'ERR {e}'

with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(R, f, ensure_ascii=False, indent=1)
print('=== DONE ===')
print(json.dumps({k: R[k] for k in ['terminal', 'n_lines', 'cut_exact', 'line_start_scan_hits',
                                    'arith', 'enc_decl', 'scan', 'repo_head']}, ensure_ascii=False, indent=1))
print('header_cut_hits =', json.dumps(R['header_cut_hits'], ensure_ascii=False))
print('suffix =', json.dumps(R.get('suffix'), ensure_ascii=False))
print('prefix.last_two_lines =', json.dumps(R.get('prefix', {}).get('last_two_lines'), ensure_ascii=False))
print('tables =', json.dumps(R['tables'], ensure_ascii=False))
print('source_probe.found =', json.dumps(R['source_probe']['found'], ensure_ascii=False))
print('pi_rulings_dirs =', R['source_probe']['pi_rulings_dirs'])
