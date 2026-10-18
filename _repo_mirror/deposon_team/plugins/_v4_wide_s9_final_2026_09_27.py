# -*- coding: utf-8 -*-
"""_v4_wide_s9_final — 重建 F2/F4 改前 SHA-12（逆变换）+ 终验（只读）"""
import hashlib, os, re
from pathlib import Path
REPO = Path(r'D:\私人资料\deposon-repo'); RES = REPO / 'results'; TMP = REPO / '.tmp'
SUB = Path(r'D:\私人资料\deposon-sub')
KEY = 'C:/Users/Administrator/Desktop/AI/LLM API.txt'
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]

print('=== F2 重建：当前字节前加回 BOM = 改前 ===')
for i in ['', '2', '3', '4', '5', '6', '7', '8']:
    q = TMP / f'_pk_probe{i}.py'
    if not q.exists(): continue
    cur = q.read_bytes()
    before = b'\xef\xbb\xbf' + cur
    print(f'  {q.name:<16} 改前(重建)={sha12b(before)}  ->  改后={sha12b(cur)}')

print()
print('=== F4 重建：把 env 覆盖式换回硬编码 = 改前 ===')
TARGETS = [RES/f'_v4_supp_l14v3_batch{b}_{r}_executor.py'
           for b, r in [('10','r5'),('2','r5'),('2','r6'),('3','r1'),('3','r2'),('3','r3'),('3','r5'),
                        ('5','r1'),('5','r2'),('5','r3'),('7','r5'),('9','r5')]] + [
    RES/'_v4_supp_l14v3_batch2_r2_models_probe.py',
    RES/'_v4_track2_endpoints_probe.py', RES/'_v4_track2_multimodel_rerun.py',
    RES/'_v4_track2_models_probe.py', RES/'_v4_track2_reprobe.py',
]
for q in TARGETS:
    if not q.exists(): continue
    cur = q.read_text(encoding='utf-8')
    # 逆 F4
    b1 = cur.replace(f'os.environ.get("DEPOSON_KEY_FILE", "{KEY}")', f'"{KEY}"')
    b1 = b1.replace(f'Path(os.environ.get("DEPOSON_KEY_FILE", "{KEY}"))', f'Path("{KEY}")')
    # 逆 F3（若适用）
    b1 = re.sub(r'def fetch_key\(idx\):\n    # \[F3 修复[\s\S]*?\n    return lines\[idx - 1\]\.strip\(\)\n',
                'PLACEHOLDER_F3', b1, count=1)
    mark = ' (含 F3 逆变换，值不精确)' if 'PLACEHOLDER_F3' in b1 else ''
    print(f'  {q.name:<50} 改前(重建)={sha12b(b1.encode("utf-8"))}{mark}  ->  改后={sha12b(q.read_bytes())}')

print()
print('=== 终验：修复件当前 SHA-12 与编译 ===')
FIXED = [RES/'_v4_supp_t1_executor.py'] + [TMP/f'_pk_probe{i}.py' for i in ['','2','3','4','5','6','7','8']] + TARGETS
ok = 0
for q in FIXED:
    if not q.exists(): print(f'  MISSING {q}'); continue
    b = q.read_bytes()
    try: compile(b, str(q), 'exec'); c = 'compile OK'
    except SyntaxError as e: c = f'COMPILE FAIL {e}'
    bom = ' BOM!' if b[:3] == b'\xef\xbb\xbf' else ''
    ok += (c == 'compile OK' and not bom)
    print(f'  {sha12b(b)}  {c}{bom}  {q.name}')
print(f'  ⇒ 全部 OK = {ok}/{len(FIXED)}')

print()
print('=== 冻结链 / 关键既有件 0 触动核验 ===')
GUARD = [('verifier/handoff/KT_ABC1_anchors_sha256_12.json','03c6c01f3697'),
         ('results/_v4_pi_cot_v3_ruleset_v3_executor.py','8a81d90c69ba'),
         ('results/_v4_pi_cot_v3_result_v3.json','585714f9660c'),
         ('results/_v4_pi_cot_v3_ruleset_v3.json','9d77a5e2cbab'),
         ('deposon_team/plugins/skill_a_p_a_60cells.py','b1463bb24403')]
for rel, exp in GUARD:
    p = REPO / rel.replace('/', os.sep)
    a = sha12b(p.read_bytes()) if p.exists() else 'MISSING'
    print(f'  {"OK " if a==exp else "CHG"}  {a} (记 {exp})  {rel}')

print()
print('=== 交付件 SHA-12 ===')
for rel in ['letters/_v4_wide_walkthrough_reply_trae_code_2026_09_27.md']:
    p = REPO / rel.replace('/', os.sep)
    if p.exists(): print(f'  {sha12b(p.read_bytes()).upper()}  {p.stat().st_size:,}B  {rel}')
print('_wide_s9 DONE')
