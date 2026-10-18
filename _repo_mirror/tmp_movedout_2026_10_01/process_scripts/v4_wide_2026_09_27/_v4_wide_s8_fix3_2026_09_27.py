# -*- coding: utf-8 -*-
"""_v4_wide_s8_fix3 — F3: track2 models_probe / reprobe 的 fetch_key 缺陷修复（幂等+后验证）"""
import hashlib, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'
def sha12(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

OLD_A = '''def fetch_key(idx):
    raw = open(KEY_SOURCE, "rb").read()
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc); break
        except: continue
    lines = text.splitlines()
    return lines[idx - 1].strip()
'''
NEW_A = '''def fetch_key(idx):
    # [F3 修复 2026-09-27 · 受托方 Trae code] 原实现三处缺陷：
    #   (1) 裸 `except:` 吞掉一切异常；(2) 三编码全失败时 `text` 未定义 ->
    #   UnboundLocalError（误报为变量错误，而非「解码失败」）；(3) 行号越界无检查。
    # 返回语义不变（仍返回第 idx 行 strip 结果）。
    raw = open(KEY_SOURCE, "rb").read()
    text = None
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        raise RuntimeError(f"KEY_SOURCE 无可用解码 (utf-8/gb18030/gbk): {KEY_SOURCE}")
    lines = text.splitlines()
    if not (1 <= idx <= len(lines)):
        raise IndexError(f"KEY_SOURCE 第 {idx} 行不存在 (共 {len(lines)} 行)")
    return lines[idx - 1].strip()
'''

OLD_B = '''def fetch_key(idx):
    raw = open(KEY_SOURCE, "rb").read()
    for enc in ("utf-8", "gb18030", "gbk"):
        try: text = raw.decode(enc); break
        except: continue
    return text.splitlines()[idx - 1].strip()
'''
NEW_B = '''def fetch_key(idx):
    # [F3 修复 2026-09-27 · 受托方 Trae code] 同 models_probe：灭裸 except + 修 text 未定义 + 加行界检查。
    raw = open(KEY_SOURCE, "rb").read()
    text = None
    for enc in ("utf-8", "gb18030", "gbk"):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        raise RuntimeError(f"KEY_SOURCE 无可用解码 (utf-8/gb18030/gbk): {KEY_SOURCE}")
    lines = text.splitlines()
    if not (1 <= idx <= len(lines)):
        raise IndexError(f"KEY_SOURCE 第 {idx} 行不存在 (共 {len(lines)} 行)")
    return lines[idx - 1].strip()
'''

for fn, OLD, NEW in (('_v4_track2_models_probe.py', OLD_A, NEW_A),
                     ('_v4_track2_reprobe.py', OLD_B, NEW_B)):
    p = RES / fn
    t = p.read_text(encoding='utf-8')
    print(f'--- {fn} 改前 sha12={sha12(p)} ---')
    n = t.count(OLD)
    print(f'    旧片段匹配 {n} 次')
    if n != 1:
        print('    !! 未按预期匹配，跳过（不改）'); continue
    t2 = t.replace(OLD, NEW)
    # 同时把 KEY_SOURCE 硬编码路径改为环境变量可覆盖
    t3, nk = re.subn(r'(KEY_SOURCE\s*=\s*)["\']C:/Users/Administrator/Desktop/AI/LLM API\.txt["\']',
                     r'\1os.environ.get("DEPOSON_KEY_FILE", "C:/Users/Administrator/Desktop/AI/LLM API.txt")', t2)
    if 'import os' not in t3:
        t3 = t3.replace('import sys', 'import os\nimport sys', 1)
    p.write_text(t3, encoding='utf-8')
    ok = True
    try: compile(p.read_bytes(), str(p), 'exec')
    except SyntaxError as e: ok = False; print(f'    COMPILE FAIL {e}')
    print(f'    KEY_SOURCE env 覆盖 {nk} 处；改后 sha12={sha12(p)}  编译 {"OK" if ok else "FAIL"}')
print('_wide_s8 DONE')
