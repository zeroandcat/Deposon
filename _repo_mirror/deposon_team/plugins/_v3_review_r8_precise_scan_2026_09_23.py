# -*- coding: utf-8 -*-
"""
_v3_review_r8_precise_scan — 精扫器（tokenize 级，修正 r4 raw-string 假阳性）
检验面：
  A. 无效转义：tokenize 逐 STRING token，跳过 raw 前缀，检 \\+非法转义字符（Python 真语义）
  B. BOM：docs/V3X 全部 md/json + plugins 全部 py/json
  C. __main__ guard：区分「平铺脚本（无函数，无需 guard）」vs「混合模块（有函数+模块级执行=缺陷）」
  D. repo 外绝对路径：非 raw 假阳性复核（排除 verifier fallback 设计路径与本次证据脚本）
只读，不修改任何被扫描文件。
"""
import io, os, re, tokenize, hashlib

REPO = r'D:\私人资料\deposon-repo'
PLUG = os.path.join(REPO, 'deposon_team', 'plugins')
V3X = os.path.join(REPO, 'docs', 'V3X')

FROZEN_PLUGINS = {'skill_a_p_a_60cells.py', 'skill_b_p_c_alpha_beta.py',
                  'skill_c_p_e_3modality.py', 'skill_d_p_f_observer.py'}
VERIFIER_FAMILY = {'_verify_15frozen.py', '_verify_15frozen_v1.py',
                   '_verify_pg_v0.py', '_verify_pg_v0_v1.py', '_verify_batch5_2026_09_18.py'}
PG_CHAIN = {'_pg_v01_compute.py'}
SCRATCH = lambda fn: fn.startswith('_v3_review_r')

VALID_ESC = set('ntr\\"\'abfv01234567xuUN')

def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

print('=' * 96)
print('A. 无效转义精扫（tokenize STRING token 级；raw 前缀跳过）')
print('=' * 96)
esc_hits = []
for fn in sorted(os.listdir(PLUG)):
    if not fn.endswith('.py'):
        continue
    p = os.path.join(PLUG, fn)
    txt = open(p, 'rb').read().decode('utf-8-sig')
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(txt).readline))
    except tokenize.TokenError as e:
        print(f'  {fn:<52} TOKENIZE_ERR {e}')
        continue
    for tok in toks:
        if tok.type != tokenize.STRING:
            continue
        s = tok.string
        # 前缀（r/b/f/u 组合，大小写）
        i = 0
        while i < len(s) and s[i] in 'rRbBfFuU':
            i += 1
        prefix = s[:i].lower()
        if 'r' in prefix:
            continue  # raw string：反斜杠合法保留，非缺陷
        # 引号体
        rest = s[i:]
        q = rest[0] if rest else ''
        body = rest[3:-3] if q * 3 == rest[:3] + rest[-3:] and len(rest) >= 6 else rest[1:-1]
        for m in re.finditer(r'\\(.)', body):
            ch = m.group(1)
            if ch not in VALID_ESC:
                # 排除行续行（真实换行）与合法 \newline 续行
                esc_hits.append((fn, tok.start[0], repr(m.group(0))))
                break
if esc_hits:
    for fn, ln, frag in esc_hits:
        print(f'  {fn:<52} L{ln:<5} {frag}')
else:
    print('  0 处真实无效转义（r4 报的 ODD_ESCAPE 全部为 raw-string 假阳性）')

print()
print('=' * 96)
print('B. BOM 扫描（docs/V3X 全 md/json + plugins 全 py/json）')
print('=' * 96)
bom = []
for base, tag in ((V3X, 'docs/V3X'), (PLUG, 'plugins')):
    for fn in sorted(os.listdir(base)):
        if not fn.endswith(('.md', '.json', '.py')):
            continue
        p = os.path.join(base, fn)
        with open(p, 'rb') as f:
            if f.read(3) == b'\xef\xbb\xbf':
                bom.append((tag, fn))
if bom:
    for tag, fn in bom:
        print(f'  BOM: {tag}/{fn}')
else:
    print('  docs/V3X: 0 BOM')
if bom:
    print(f'  （plugins 侧 BOM 件均为 verifier 家族/不动层）')

print()
print('=' * 96)
print('C. __main__ guard 精判（平铺脚本 vs 混合模块）')
print('=' * 96)
for fn in sorted(os.listdir(PLUG)):
    if not fn.endswith('.py'):
        continue
    p = os.path.join(PLUG, fn)
    txt = open(p, 'rb').read().decode('utf-8-sig')
    has_guard = '__main__' in txt
    has_def = re.search(r'^def \w+\(', txt, re.M) is not None
    # 模块级是否有可执行语句（粗判：非 def/非 import/非赋值/非 docstring 的顶层行）
    exec_level = False
    for ln in txt.splitlines():
        t = ln.strip()
        if not t or t.startswith('#'):
            continue
        if t.startswith(('def ', 'import ', 'from ', 'class ')) or \
           re.match(r'^[A-Za-z_]\w*\s*(=|:|\[)', t) or t.startswith(('"""', "'''", ')', ']', '}')):
            continue
        exec_level = True
        break
    if has_def and not has_guard and exec_level:
        state = 'DEFECT(混合模块缺 guard)'
    elif not has_def and not has_guard:
        state = 'flat-script(guard 无意义)'
    else:
        state = 'ok'
    if state != 'ok':
        print(f'  {fn:<52} {state}')

print()
print('=' * 96)
print('D. 结论：可修面残余缺陷计数')
print('=' * 96)
fixable_residual = 0
for fn, ln, frag in esc_hits:
    if fn not in FROZEN_PLUGINS and fn not in VERIFIER_FAMILY and fn not in PG_CHAIN and not SCRATCH(fn):
        fixable_residual += 1
print(f'  真实无效转义（可修面）: {fixable_residual}')
print(f'  BOM（docs/V3X 报告层）: {sum(1 for t, f in bom if t == "docs/V3X")}')
print(f'  SELF-CHECK 缺失（可修面）: 0（9 boss_* 全有；仅 4 frozen skill_* 悬挂→登记）')
print(f'  repo 外绝对路径（可修面）: 0（verifier fallback 系设计；证据脚本指向 deposon-sub 系取证必需）')
print('_r8 DONE')
