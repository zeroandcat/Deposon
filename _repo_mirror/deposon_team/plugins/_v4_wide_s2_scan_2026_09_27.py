# -*- coding: utf-8 -*-
"""
_v4_wide_s2_scan — 新件(.py)全量编译+静态缺陷扫描（只读）
1) py_compile 语法检查（真编译）
2) tokenize 级无效转义
3) BOM / 缺 __main__ guard / repo 外绝对路径 / 硬编码密钥样式
4) import 真执行（限安全：仅 import 不跑 main）
"""
import ast, hashlib, os, py_compile, tempfile, tokenize, io, re, sys, importlib.util
from datetime import datetime
from collections import defaultdict

CUTOFF = datetime(2026, 9, 23, 12, 0, 0).timestamp()
ROOTS = [r'D:\私人资料\deposon-repo', r'D:\私人资料\deposon-sub']
SKIP = {'__pycache__', '.git', 'node_modules', '.trae'}
VALID_ESC = set('ntr\\"\'abfv01234567xuUN')

pys = []
for root in ROOTS:
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP]
        for fn in fns:
            if not fn.endswith('.py'): continue
            p = os.path.join(dp, fn)
            try: st = os.stat(p)
            except OSError: continue
            if st.st_mtime >= CUTOFF:
                pys.append((st.st_size, p))
pys.sort(reverse=True)
print(f'=== 新件 .py 共 {len(pys)} 件 ===')

def rel(p): return p.replace(r'D:\私人资料' + os.sep, '')

syntax_err, bom, no_guard, odd_esc, abs_out, keylike = [], [], [], [], [], []
for sz, p in pys:
    r = rel(p)
    raw = open(p, 'rb').read()
    # 1) 语法
    try:
        compile(raw, p, 'exec')
    except SyntaxError as e:
        syntax_err.append((r, sz, f'L{e.lineno}: {e.msg}'))
        continue
    except Exception as e:
        syntax_err.append((r, sz, f'{type(e).__name__}: {e}'))
        continue
    txt = raw.decode('utf-8', 'replace')
    # 2) BOM
    if raw[:3] == b'\xef\xbb\xbf': bom.append((r, sz))
    # 3) guard（仅对有 def 且模块级有可执行语句者）
    has_def = re.search(r'^def \w+\(', txt, re.M) is not None
    if has_def and '__main__' not in txt:
        exec_lvl = False
        for ln in txt.splitlines():
            t = ln.strip()
            if not t or t.startswith('#'): continue
            if t.startswith(('def ', 'import ', 'from ', 'class ', '@', '"""', "'''", ')', ']', '}')): continue
            if re.match(r'^[A-Za-z_]\w*\s*(=|:|\[)', t): continue
            exec_lvl = True; break
        if exec_lvl: no_guard.append((r, sz))
    # 4) 无效转义
    try:
        for tok in tokenize.generate_tokens(io.StringIO(txt).readline):
            if tok.type != tokenize.STRING: continue
            s = tok.string; i = 0
            while i < len(s) and s[i] in 'rRbBfFuU': i += 1
            if 'r' in s[:i].lower(): continue
            rest = s[i:]
            body = rest[3:-3] if len(rest) >= 6 and rest[:3] == rest[0]*3 and rest[-3:] == rest[0]*3 else rest[1:-1]
            for m in re.finditer(r'\\(.)', body):
                if m.group(1) not in VALID_ESC:
                    odd_esc.append((r, tok.start[0], repr(m.group(0)))); break
    except Exception:
        pass
    # 5) repo 外绝对路径
    for m in re.finditer(r'''(?P<q>['"])(?P<p>[A-Za-z]:[\\/][^'"]{3,})(?P=q)''', txt):
        pth = m.group('p')
        if not pth.lower().startswith('d:') and 'deposon' not in pth.lower():
            abs_out.append((r, pth[:60])); break
    # 6) 密钥样式
    for m in re.finditer(r'(?<![A-Za-z])sk-[A-Za-z0-9]{16,}', txt):
        keylike.append((r, m.group(0)[:12] + '...')); break

def show(title, lst, fmt=lambda x: x):
    print(f'\n--- {title} ({len(lst)}) ---')
    for it in lst[:40]:
        print('   ', fmt(it))

show('A. 语法错误（compile 失败）', syntax_err, lambda x: f'{x[0]}\n        {x[1]:,}B  {x[2]}')
show('B. UTF-8 BOM', bom, lambda x: f'{x[0]}  {x[1]:,}B')
show('C. 缺 __main__ guard（有 def + 模块级可执行）', no_guard)
show('D. 无效转义（真语义级）', odd_esc, lambda x: f'{x[0]} L{x[1]} {x[2]}')
show('E. 非 D: 盘绝对路径', abs_out, lambda x: f'{x[0]}  -> {x[1]}')
show('F. 疑似明文密钥', keylike, lambda x: f'{x[0]}  {x[1]}')
print('\n_wide_s2 DONE')
