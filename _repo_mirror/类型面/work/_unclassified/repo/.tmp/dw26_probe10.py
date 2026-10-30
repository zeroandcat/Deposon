# -*- coding: utf-8 -*-
"""§26 探针十：字符编码诊断／台账原值／PI 令原文／GBK 还原／§26 合规矩阵（顶层节）"""
import os, json, re, hashlib, sqlite3, datetime, collections

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
L = txt.split('\n')

print('== 1. CODEPOINT DIAGNOSIS of 不互X ==')
cnt = collections.Counter()
for i, l in enumerate(L, 1):
    for m in re.finditer('\u4e0d\u4e92', l):
        rest = l[m.start() + 2: m.start() + 3]
        cnt[rest] += 1
        if cnt[rest] == 1:
            print('   sample L%d rest=%r codepoints=%s' % (i, rest, [hex(ord(c)) for c in rest]))
print('   3rd-char distribution:', {repr(k): v for k, v in cnt.items()})
# 找出「不互抄」之正确码位
for i, l in enumerate(L, 1):
    m = re.search('\u4e0d\u4e92(.)', l)
    if m and m.group(1) != '\u770b':
        print('   NON-看 variant at L%d: %r' % (i, m.group(0)))
        break
target = '\u4e0d\u4e92\u62c4'
print('   count of 不互抄(U+62C4) =', txt.count(target))
for cand in ('\u4e0d\u4e92\u6284', '\u4e0d\u4e92\u62c4'):
    print('   candidate %r -> %d' % (cand, txt.count(cand)))

print('\n== 2. LEDGER RAW ms for the 7 rods ==')
LED = r'〔本地路径已脱敏〕'
con = sqlite3.connect('file:' + LED.replace('\\', '/') + '?mode=ro', uri=True)
cur = con.cursor()
TB = 'local_runtime_background_tasks'
rods = {}
for rid in ('bg_06f1b9dc', 'bg_8b9bdf59', 'bg_156b760e', 'bg_d53d8381', 'bg_7c16da20', 'bg_5b4fcb87', 'bg_eed597a7'):
    cur.execute("SELECT task_id,kind,status,created_at_ms,ended_at_ms,owner_session_id,record_json FROM %s WHERE task_id LIKE ?" % TB, (rid + '%',))
    row = cur.fetchone()
    if not row:
        print('  %s : NOT FOUND' % rid)
        continue
    rods[rid] = row
    rj = json.loads(row[6]) if row[6] else {}
    md = rj.get('metadata') or {}
    print('  %-12s %-8s %-10s created=%d(%s) ended=%s(%s) owner=%s child=%s exec=%s desc=%r'
          % (rid, row[1], row[2], row[3], ts(row[3]), row[4], ts(row[4]) if row[4] else 'NONE',
             row[5], md.get('childSessionId'), md.get('executionMode'), (rj.get('description') or '')[:46]))
    print('        finalResult_present=%s  error=%r' % (bool(rj.get('finalResult')), str(rj.get('lastError'))[:60]))
print('  ledger file mtime=%s size=%d' % (ts(os.path.getmtime(LED) * 1000), os.path.getsize(LED)))

print('\n== 3. PI ORDER RAW (L80) ==')
MAIN = r'〔本地路径已脱敏〕'
raw = open(MAIN, 'rb').read()
lines = raw.split(b'\n')
print('   file bytes=%d lines=%d sha12=%s mtime=%s' % (len(raw), len([x for x in lines if x.strip()]),
      hashlib.sha256(raw).hexdigest()[:12], ts(os.path.getmtime(MAIN) * 1000)))
l80 = lines[79]
rec = json.loads(l80.decode('utf-8', 'replace'))
print('   L80 timestamp=%s (%s)' % (rec.get('timestamp') or rec['message'].get('timestamp'),
                                ts(rec.get('timestamp') or rec['message'].get('timestamp'))))
txt80 = ''.join(x.get('text', '') for x in rec['message']['content'] if isinstance(x, dict))
for key in ('\u59d4\u6258\u51fd', '\u4e0a\u4f20\u65b9', '\u4f53\u4f8b\u4e4b\u6b63\u4fee\u4e09\u518c'):
    print('   ctrl %-12s count=%d' % (key, txt80.count(key)))
idx = txt80.find('\u4e0a\u4e0b\u6587\u5df2\u538b\u7f29')
print('   PI text tail: %r' % txt80[idx:idx + 120])

print('\n== 4. GBK RESTORE of hook context (raw bytes slice) ==')
m = re.search(rb'plugin-hook-context\\?"\s*:\s*\\?"(.{0,600}?)\\?"\s*,', l80, re.S)
if m:
    frag = m.group(1)
    for enc in ('gbk', 'gb18030', 'big5'):
        try:
            print('   %s -> %s' % (enc, frag.decode(enc)[:400]))
        except Exception as e:
            print('   %s fail: %s' % (enc, e))
else:
    print('   regex no match; searching raw occurrences:', raw.count(b'plugin-hook-context'))

print('\n== 5. TOP-LEVEL SECTION COMPLIANCE MATRIX (three duties in heading block) ==')
tops = [(i, int(re.match(r'^##\s+\u00a7(\d+)', l).group(1))) for i, l in enumerate(L, 1) if re.match(r'^##\s+\u00a7\d+', l)]
for k, (ln, num) in enumerate(tops):
    end = tops[k + 1][0] - 1 if k + 1 < len(tops) else len(L)
    block = '\n'.join(L[ln - 1:min(end, ln + 14)])       # 节首声明块（前 14 行）
    body = '\n'.join(L[ln - 1:end])
    cheng = bool(re.search('\u627f\s*[`\u00a7]?\s*\u00a7?\d+|\u627f\u300c?`?\u00a7\d+', block))
    bugai = bool(re.search('PURE-APPEND|\u56de\u6539|\u4e0d\u6539', block))
    xin = bool(re.search('\u4ee5\u672c\u8282\u4e3a\u51c6|\u4ee5\u672c\u6bb5\u4e3a\u51c6|\u4ee5\u65b0\u4e3a\u51c6|\u4ee5\u672c\u8282\u4e3a\u51c6', block))
    zibuchao = ('\u4e0d\u4e92\u62c4' in body) or ('\u4e0d\u4e92\u770b' in body)
    yishou = ('\u4e00\u624b' in body)
    bukede = ('\u4e0d\u53ef\u5f97' in body)
    qiyin = ('\u5176\u56e0' in body)
    laiyuan = ('\u6765\u6e90' in body)
    zhubang = ('\u68d2\u53f7' in body)
    print('   \u00a7%-3d L%-5d rows=%-5d \u627f=%d \u4e0d\u6539=%d \u4ee5\u65b0\u4e3a\u51c6=%d | \u81ea\u9648=%d \u4e00\u624b=%d \u4e0d\u53ef\u5f97=%d \u5176\u56e0=%d \u6765\u6e90=%d \u68d2\u53f7=%d'
          % (num, ln, end - ln + 1, cheng, bugai, xin, zibuchao, yishou, bukede, qiyin, laiyuan, zhubang))

print('\n== 6. README_external search by name (whole 〔本地路径已脱敏〕 name only) ==')
hits = []
for dp, dn, fn in os.walk(r'〔本地路径已脱敏〕'):
    dn[:] = [x for x in dn if x not in ('.git', 'node_modules', '__pycache__', '.venv', 'AppData')]
    for f in fn:
        if 'README_external' in f or 'README_external' in dp:
            hits.append(os.path.join(dp, f))
for h in hits[:20]:
    print('   ', h)
print('   total hits', len(hits))
con.close()
