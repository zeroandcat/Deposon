# -*- coding: utf-8 -*-
"""§26 探针七：逐节合规矩阵 + 真写调用直证（区分引文与执行）"""
import os, json, re, hashlib, datetime

TZ = datetime.timezone(datetime.timedelta(hours=8))
def ts(ms):
    return datetime.datetime.fromtimestamp(ms / 1000, TZ).strftime('%Y-%m-%d %H:%M:%S')

T = r'〔本地路径已脱敏〕'
b = open(T, 'rb').read()
txt = b.decode('utf-8', 'replace')
lines = txt.split('\n')
print('== TARGET ==', len(b), 'B', hashlib.sha256(b).hexdigest()[:12], len(lines), 'lines')

# 节界：以 '## §' 或 '### §' 标题切
heads = []
for i, l in enumerate(lines, 1):
    m = re.match(r'^(#{2,3})\s+§(\d+)(.*)$', l)
    if m:
        heads.append((i, m.group(2), m.group(1), m.group(3).strip()))
print('\n== SECTION HEADS (%d) ==' % len(heads))
for i, (ln, num, hashes, rest) in enumerate(heads):
    end = heads[i + 1][0] - 1 if i + 1 < len(heads) else len(lines)
    body = '\n'.join(lines[ln - 1:end])
    # 合规标记
    has_cheng = ('承' in body[:1200])
    has_cheng2 = bool(re.search(r'承\s*[`§]?\s*\d+', body[:1500]))
    has_bu = bool(re.search(r'PURE-APPEND|⛔\s*0\s*回改|0\s*回改|不改', body[:1500]))
    has_xin = bool(re.search(r'以本节为准|以本段为准|以新为准', body[:1500]))
    has_ju = ('不互抄' in body)
    has_yishou = ('一手' in body)
    has_bukede = ('不可得' in body)
    has_qiyin = ('其因' in body)
    has_laiyuan = ('来源' in body)
    has_bang = ('棒号' in body)
    has_sha = bool(re.search(r'SHA-?12|`[0-9a-f]{12}`', body))
    print('  L%-5d %-4s %-7s rows=%-5d 承=%d 不改=%d 以新=%d 不互抄=%d 一手=%d 不可得=%d 其因=%d 来源=%d 棒号=%d sha12=%d  | %s'
          % (ln, num, hashes + str(len(hashes)), end - ln + 1, has_cheng2, has_bu, has_xin, has_ju,
             has_yishou, has_bukede, has_qiyin, has_laiyuan, has_bang, has_sha, rest[:44]))

print('\n== 不互抄 occurrence lines ==')
for i, l in enumerate(lines, 1):
    if '不互抄' in l:
        print('  L%d %s' % (i, l.strip()[:150]))
print('== yishou count', txt.count('\u4e00\u624b'))

# 真写调用直证：解析两个在盘会话目录
print('\n== TRUE WRITE CALLS (assistant toolCall name=write) ==')
SESS = r'〔本地路径已脱敏〕'
for d in sorted(os.listdir(SESS)):
    mp = os.path.join(SESS, d, 'messages.jsonl')
    if not os.path.isfile(mp):
        continue
    print('  --- %s ---' % d[:14])
    with open(mp, 'rb') as f:
        for i, raw in enumerate(f, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                rec = json.loads(raw.decode('utf-8', 'replace'))
            except Exception:
                continue
            msg = rec.get('message') or {}
            role = msg.get('role')
            c = msg.get('content')
            if not isinstance(c, list):
                continue
            stamp = rec.get('timestamp') or msg.get('timestamp')
            for x in c:
                if not isinstance(x, dict):
                    continue
                if x.get('type') == 'toolCall' and x.get('name') in ('write', 'edit', 'bash'):
                    arg = x.get('arguments')
                    if isinstance(arg, dict):
                        if x.get('name') == 'write':
                            print('   L%-4d %s WRITE %s  (content %d chars)'
                                  % (i, ts(stamp) if stamp else '??', arg.get('filePath'), len(str(arg.get('content') or ''))))
                        elif x.get('name') == 'edit':
                            print('   L%-4d %s EDIT  %s' % (i, ts(stamp) if stamp else '??', arg.get('filePath')))
                        else:
                            cmd = str(arg.get('command') or '')[:120]
                            print('   L%-4d %s BASH  %s' % (i, ts(stamp) if stamp else '??', cmd))
