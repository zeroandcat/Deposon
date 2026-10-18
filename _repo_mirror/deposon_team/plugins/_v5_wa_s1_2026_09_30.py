# -*- coding: utf-8 -*-
"""
_v5_wa_s1 — 09-30 走读审计 S1：边界复算 + 锚件核验 + 574 件机扫（compile/BOM/转义/key/绝对路径）
只读，仅 stdout。
"""
import hashlib, os, re, io, tokenize
from datetime import datetime
from pathlib import Path

B0 = datetime(2026, 9, 27, 20, 28, 20).timestamp()
AREAS = [r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub', r'D:\私人资料\_non_upload_local_archive']
SKIP = {'__pycache__', '.git', '.trae', '.mavis'}
VALID_ESC = set('ntr\\"\'abfv01234567xuUN')

def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

print('=== 0. 锚件核验（委托 §A.1 三件）===')
ANCHORS = [
 ('letters/TRAE_V4_WALKTHROUGH_BUGFIX_REQUEST_2026_09_27.md', '6ac3cb09567b', 105136),
 ('letters/_v4_walkthrough_bugfix_reply_trae_code_2026_09_27.md', 'f86b8b6c8ed2', 60139),
 ('letters/_v4_wide_walkthrough_reply_trae_code_2026_09_27.md', '9a98abf3119a', 20610),
]
REPO = Path(AREAS[0])
for rel, exp, sz in ANCHORS:
    p = REPO / rel
    ok = p.exists() and sha12(p) == exp and p.stat().st_size == sz
    print(f'  {"OK " if ok else "DIFF"} {sha12(p) if p.exists() else "-"} {p.stat().st_size if p.exists() else 0} (记 {exp}/{sz}) {rel}')

print()
print('=== 1. 边界复算（mtime > B0，三区；排除备份/转移双计面）===')
EXCL = ('.evidence_backup_2026_09_28', '.evidence_backup_2026_09_30', '_movedout_scratch_2026_09_30')
allf = []
for area in AREAS:
    n = 0
    for dp, dns, fns in os.walk(area):
        dns[:] = [d for d in dns if d not in SKIP]
        if any(x in dp for x in EXCL): continue
        for fn in fns:
            q = os.path.join(dp, fn)
            try: st = os.stat(q)
            except OSError: continue
            if st.st_mtime > B0:
                allf.append((st.st_mtime, st.st_size, q)); n += 1
    print(f'  {area}  n={n}')
print(f'  合计 = {len(allf)} （委托记 574）')

print()
print('=== 2. .py 机扫（compile / BOM / 无效转义 / 裸 except / 密钥样式 / 仓外路径）===')
pys = [(m, s, q) for m, s, q in allf if q.endswith('.py')]
print(f'  .py 共 {len(pys)} 件（委托记 181；差异 = 边界亚秒 + 快照漂移，见回函）')
bad = {'syntax': [], 'bom': [], 'esc': [], 'bare': [], 'key': [], 'absp': []}
KEYPAT = re.compile(r'(?<![A-Za-z])sk-[A-Za-z0-9_\-]{16,}|sk-teamo-[A-Za-z0-9]{8,}|(?<![A-Za-z])tp-[A-Za-z0-9]{16,}|Bearer\s+[A-Za-z0-9_\-\.]{30,}')
for mt, sz, q in sorted(pys):
    rel = q.replace(r'D:\私人资料' + os.sep, '')
    raw = open(q, 'rb').read()
    try:
        compile(raw, q, 'exec')
    except SyntaxError as e:
        bad['syntax'].append((rel, f'L{e.lineno}: {e.msg}')); continue
    if raw[:3] == b'\xef\xbb\xbf': bad['bom'].append(rel)
    t = raw.decode('utf-8', 'ignore')
    try:
        for tok in tokenize.generate_tokens(io.StringIO(t).readline):
            if tok.type != tokenize.STRING: continue
            s_ = tok.string; i = 0
            while i < len(s_) and s_[i] in 'rRbBfFuU': i += 1
            if 'r' in s_[:i].lower(): continue
            rest = s_[i:]
            body = rest[3:-3] if len(rest) >= 6 and rest[:3] == rest[0]*3 and rest[-3:] == rest[0]*3 else rest[1:-1]
            for m in re.finditer(r'\\(.)', body):
                if m.group(1) not in VALID_ESC:
                    bad['esc'].append((rel, tok.start[0], repr(m.group(0)))); break
    except Exception: pass
    if re.search(r'except\s*:\s*(pass|continue)\b', t): bad['bare'].append(rel)
    m = KEYPAT.search(t)
    if m: bad['key'].append((rel, m.group(0)[:10]))
    m = re.search(r'["\']C:/Users/Administrator/Desktop/AI/LLM API\.txt["\']', t)
    if m: bad['absp'].append(rel)

for k, v in bad.items():
    print(f'  {k}: {len(v)}')
    for it in v[:25]:
        print(f'      {it}')
print()
print('=== 3. 非 .py 密钥样式扫（md/json/txt/xml/html/jsonl）===')
nonpy = [q for _, _, q in allf if not q.endswith('.py') and not q.endswith('.pyc')]
keyhits = []
for q in nonpy:
    try:
        if os.path.getsize(q) > 12_000_000: continue
        t = open(q, 'rb').read().decode('utf-8', 'ignore')
    except Exception: continue
    m = KEYPAT.search(t)
    if m:
        keyhits.append((q.replace(r'D:\私人资料'+os.sep,''), m.group(0)[:10]))
print(f'  命中 {len(keyhits)}')
for h in keyhits[:20]: print(f'      {h}')
print()
print('_wa_s1 DONE')
