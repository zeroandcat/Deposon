# -*- coding: utf-8 -*-
"""
_v4_wide_s7_fix — 对「未被任何新件引用」的目标件执行原地修复（幂等 + 后验证）
修复项：
 F1  _v4_supp_t1_executor.py            : load_checkpoint 静默 `return []` → 响亮告警（不改返回语义）
 F2  .tmp/_pk_probe*.py (8 件)          : 去 UTF-8 BOM
 F3  _v4_track2_models_probe.py / _reprobe.py : 裸 `except:` → 具名异常 + 修 fetch_key 未定义 text 路径
 F4  KEYPATH_ABS 件（未被引用者）        : 硬编码仓外 key 路径 → 环境变量可覆盖（默认值不变）
每件记 改前/改后 SHA-12，并 compile 后验证。
"""
import hashlib, os, re, sys
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'; TMP = REPO / '.tmp'
SUB = Path(r'D:\私人资料\deposon-sub')

def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]
def readb(p): return Path(p).read_bytes()
def writeb(p, b):
    Path(p).write_bytes(b)
def compile_ok(p):
    try:
        compile(readb(p), str(p), 'exec'); return True, ''
    except SyntaxError as e:
        return False, f'L{e.lineno}: {e.msg}'

LOG = []
def apply(p, new_bytes, tag):
    p = Path(p)
    before = readb(p)
    if before == new_bytes:
        LOG.append((tag, p, sha12(p), 'no-change(已修)'))
        return False
    writeb(p, new_bytes)
    ok, err = compile_ok(p)
    LOG.append((tag, p, f'{sha12(p)}', 'OK' if ok else f'COMPILE_FAIL {err}'))
    return True

print('=' * 104)
print('F1 · _v4_supp_t1_executor.py : load_checkpoint 静默返回 [] → 响亮告警')
print('=' * 104)
p = RES / '_v4_supp_t1_executor.py'
b = readb(p); t = b.decode('utf-8')
print(f'  改前 sha12={sha12(p)}')
assert 'import sys' in t, 'F1: 该件未 import sys，中止'
OLD = '''        except Exception:
            return []
    return []
'''
NEW = '''        except Exception as _ckpt_err:
            # [F1 修复 2026-09-27 · 受托方 Trae code]
            # 原为静默 `return []`：checkpoint 半写/损坏时被静默重置为空，
            # 续跑会为已记录 caption 重发 calls（配额/样本重复）且无任何日志。此处改为响亮告警；
            # 返回语义保持不变（仍重置为空），故不影响任何历史读数。
            import sys as _sys
            print(f"[WARN] checkpoint unreadable at {CHECKPOINT_PATH}: {_ckpt_err!r} "
                  f"-> reset to empty; re-run will re-issue calls", file=_sys.stderr)
            return []
    return []
'''
assert t.count(OLD) == 1, f'F1: 目标片段出现 {t.count(OLD)} 次（应 1），中止'
apply(p, t.replace(OLD, NEW).encode('utf-8'), 'F1')
print(f'  改后 sha12={sha12(p)}')

print()
print('=' * 104)
print('F2 · .tmp/_pk_probe*.py（8 件）：去 UTF-8 BOM')
print('=' * 104)
for i in ['', '2', '3', '4', '5', '6', '7', '8']:
    q = TMP / f'_pk_probe{i}.py'
    if not q.exists(): continue
    raw = readb(q)
    if raw[:3] == b'\xef\xbb\xbf':
        apply(q, raw[3:], f'F2:{q.name}')
        print(f'  {q.name:<16} sha12={sha12(q)}  BOM stripped')
    else:
        print(f'  {q.name:<16} 无 BOM（跳过）')

print()
print('=' * 104)
print('F3 · track2 models_probe / reprobe：裸 except / 未定义 text')
print('=' * 104)
for fn in ('_v4_track2_models_probe.py', '_v4_track2_reprobe.py'):
    p = RES / fn
    if not p.exists():
        print(f'  MISSING {fn}'); continue
    t = readb(p).decode('utf-8')
    print(f'  --- {fn}  改前 sha12={sha12(p)} ---')
    # 打印 fetch_key 段
    m = re.search(r'def fetch_key[\s\S]{0,900}', t)
    if m:
        for l in m.group(0).splitlines()[:30]:
            print(f'      {l[:150]}')
print()
print('（F3 采用人工确认后单独修；本脚本先只展示）')

print()
print('=' * 104)
print('F4 · KEYPATH_ABS 件（未被引用者）：硬编码仓外 key 路径 → 环境变量可覆盖')
print('=' * 104)
KEYVARS = ['C:/Users/Administrator/Desktop/AI/LLM API.txt']
TARGETS = [
 RES / '_v4_supp_l14v3_batch10_r5_executor.py', RES / '_v4_supp_l14v3_batch2_r5_executor.py',
 RES / '_v4_supp_l14v3_batch2_r6_executor.py', RES / '_v4_supp_l14v3_batch3_r1_executor.py',
 RES / '_v4_supp_l14v3_batch3_r2_executor.py', RES / '_v4_supp_l14v3_batch3_r3_executor.py',
 RES / '_v4_supp_l14v3_batch3_r5_executor.py', RES / '_v4_supp_l14v3_batch5_r1_executor.py',
 RES / '_v4_supp_l14v3_batch5_r2_executor.py', RES / '_v4_supp_l14v3_batch5_r3_executor.py',
 RES / '_v4_supp_l14v3_batch7_r5_executor.py', RES / '_v4_supp_l14v3_batch9_r5_executor.py',
 RES / '_v4_supp_l14v3_batch2_r2_models_probe.py',
 RES / '_v4_track2_endpoints_probe.py', RES / '_v4_track2_models_probe.py',
 RES / '_v4_track2_multimodel_rerun.py', RES / '_v4_track2_reprobe.py',
 RES / '_archive_2026_09_24' / '_l13_latency_test.py',
 SUB / 'results' / '_track2_qwen_check_2026_09_23.py',
]
n_done = 0
for p in TARGETS:
    if not p.exists():
        print(f'  MISSING {p}'); continue
    t = readb(p).decode('utf-8')
    orig = t
    # 覆盖 KEY_SOURCE_PATH = "..." / Path("...")
    t2, n1 = re.subn(
        r'(KEY_SOURCE_PATH\s*=\s*)Path\(\s*["\']' + re.escape(KEYVARS[0]) + r'["\']\s*\)',
        lambda m: m.group(1) + 'Path(os.environ.get("DEPOSON_KEY_FILE", "' + KEYVARS[0] + '"))', t)
    t3, n2 = re.subn(
        r'(KEY_SOURCE_PATH\s*=\s*)["\']' + re.escape(KEYVARS[0]) + r'["\']',
        lambda m: m.group(1) + 'os.environ.get("DEPOSON_KEY_FILE", "' + KEYVARS[0] + '")', t2)
    changed = (n1 + n2)
    if changed and ('import os' in t3 or 'import os,' in t3 or re.search(r'^import .*\bos\b', t3, re.M)):
        apply(p, t3.encode('utf-8'), f'F4:{p.name}')
        print(f'  {p.name:<52} n={changed} sha12={sha12(p)}')
        n_done += 1
    else:
        print(f'  {p.name:<52} 未改（匹配 {changed} 处；os 导入 {"有" if "import os" in t3 else "无"}）')

print()
print('=' * 104)
print('汇总：本次实际写入的件')
print('=' * 104)
for tag, p, s, st in LOG:
    print(f'  {tag:<28} {s}  {st:<10} {str(p).replace(chr(92)+"私人资料"+chr(92), "")}')
print(f'\n  写入/确认 {len(LOG)} 件')
print('_wide_s7 DONE')
