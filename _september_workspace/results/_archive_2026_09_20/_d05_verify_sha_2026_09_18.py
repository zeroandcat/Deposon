# -*- coding: utf-8 -*-
"""D05 产物 SHA-12 校验器 — Trae 2026-09-18 走读改进 #2 修复版 (TRAE_FIXED_2026_09_18)

原版缺陷 (修复依据):
1. 路径拼接 `r'D:\\...\\results\\\\' + f`: raw string 以双反斜杠结尾 + 相对拼接,
   且校验列表引用的 2 个文件 (deepseek 主跑 / qwen3 failed) 已随 bg_21191cee
   任务 trash 化移位 — 原版现在重跑必 FileNotFoundError。
2. 无 β _meta 交叉核对, 无 trash 副本对照。

本版: pathlib 绝对路径 + 7 件校验 (含 2 件救援副本) + β _meta 三声称值实算核对
     + trash 双胞胎一致性对照。直跑校验器 (无 main() 属设计内)。
"""
import hashlib
import json
from pathlib import Path

RESULTS = Path(r'D:\私人资料\deposon-repo\results')
TRASH = Path(r'D:\私人资料\deposon-repo\_d05_bg_21191cee_trash_2026_09_18\results')
TS = '20260918_100853'

FILES = [
    f'_d05_main_run_results_{TS}.json',                 # deepseek_v4 主跑 (救援副本)
    f'_d05_main_run_results_qwen3_failed_{TS}.json',    # qwen3 FAIL 证据 (救援副本)
    f'_d05_main_run_results_nemotron_3.5_{TS}.json',
    f'_d05_opt_5_directions_results_{TS}.json',
    f'_d05_backbone_robustness_beta_{TS}.json',
    f'_d05_i1i5_invariants_check_{TS}.json',
    f'_d05_combined_report_{TS}.md',
]


def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]


ok = True
for f in FILES:
    p = RESULTS / f
    if not p.exists():
        print(f'MISSING  {f}')
        ok = False
        continue
    s = sha12(p)
    t = TRASH / f
    twin = ''
    if t.exists():
        twin = ' | trash-twin ' + ('==' if sha12(t) == s else '!= ' + sha12(t))
    print(f'OK  {f} | size={p.stat().st_size} | sha12={s}{twin}')

beta = RESULTS / f'_d05_backbone_robustness_beta_{TS}.json'
if beta.exists():
    meta = json.loads(beta.read_text(encoding='utf-8')).get('_meta', {})
    for key, fname in [('deepseek_v4_main_sha12', FILES[0]),
                       ('qwen3_32b_main_sha12', FILES[1]),
                       ('nemotron_main_sha12', FILES[2])]:
        expect = meta.get(key)
        actual = sha12(RESULTS / fname) if (RESULTS / fname).exists() else 'MISSING'
        match = expect == actual
        ok = ok and match
        print(f'beta._meta.{key}: claimed={expect} actual={actual} -> {"MATCH" if match else "DRIFT"}')
else:
    ok = False
    print('MISSING beta JSON — cross-check skipped')

print('VERIFY', 'ALL-PASS' if ok else 'HAS-FAIL')

# ---------- SELF-CHECK (P-F V0.1 §5 纪律, 沿 Trae 2026-09-16 起格式) ----------
import os as _os_sc
assert _os_sc.path.basename(__file__) == '_d05_verify_sha_2026_09_18.py', '文件名漂移: ' + __file__
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_FIXED_2026_09_18' in _src_sc
assert 'RESULTS = Path' in _src_sc and 'TRASH = Path' in _src_sc
print('_d05_verify_sha_2026_09_18.py SELF-CHECK PASS')
