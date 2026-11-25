#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""根层散件之逐件初判（只读·不删不移）2026-10-27
初判三类：MOVE_ARCHIVE（一次性/旧版·宜移归档）｜KEEP（库面或活件·宜留）｜HUMAN（须人判）
"""
import csv
import os
import re
import time

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


REPO = r_dep_path("")
OUT = os.path.join(REPO, 'results', 'work', 'process', '_roots_triage_2026_10_27.csv')
KEEP_DAYS = 1
WHITELIST = {'_bcheck.py', '_append_generic.py', '_fill_item16.py',
             '_scan_glm_minimax.py', '_read_k31.py', '_read_k31b.py',
             '_read_k31c.py', '_land_k31_replies.py', '_land_k31_C.py',
             '_extract_cards.py', '_extract_cards2.py',
             '_scan_questionnaires.py', '_read_k31_last.py',
             '.gitignore', 'README.md'}
KEEP_PATTERNS = ('deposon_', 'README', 'fingerprint_v0', 'gt_common',
                 'llm_fetch', 'llm_prior', 'mindmap_', 'svg_mindmap_')

# 一次性/旧版之形
ONESHOT = [
    (re.compile(r'^_tools_v\d+_'), '旧版工具（_tools_vNNN_ 系）'),
    (re.compile(r'^_kd_flip_|^_kdflipc_'), '一次性 kd 翻转普查脚本/数据'),
    (re.compile(r'^_tools_docwriter_'), '一次性 docwriter 盘点脚本'),
    (re.compile(r'^run_v\d+'), '旧版实验运行脚本（run_vNN_ 系）'),
    (re.compile(r'^_docwriter_|^_u5_inventory_tmp'), '一次性 scratch'),
    (re.compile(r'^_v4_pi_cot_'), '旧版 v4 签署件'),
    (re.compile(r'^_v5_gt_exec'), '旧版 v5 执行脚本'),
]
HUMAN_PAT = [
    (re.compile(r'^run_benchmark_|^run_g2_|^run_v1[5-9]_'), '基准/实验脚本（可能仍要复跑）'),
]


def triage(name):
    if name in WHITELIST:
        return 'KEEP', '白名单（活工具/结构件）'
    if any(name.startswith(x) for x in KEEP_PATTERNS):
        return 'KEEP', '库面或文档（%s）' % name.split('_')[0]
    for pat, why in ONESHOT:
        if pat.search(name):
            return 'MOVE_ARCHIVE', why
    for pat, why in HUMAN_PAT:
        if pat.search(name):
            return 'HUMAN', why
    if name.endswith(('.py',)):
        return 'HUMAN', '脚本·未归类（须认其是否活件）'
    if name.endswith(('.md', '.json', '.txt', '.csv', '.log')):
        return 'MOVE_ARCHIVE', '数据/文档散件（根层不宜存）'
    return 'HUMAN', '未归类'


def main():
    now = time.time()
    cut = now - KEEP_DAYS * 86400
    rows = []
    for f in sorted(os.listdir(REPO)):
        p = os.path.join(REPO, f)
        if not os.path.isfile(p):
            continue
        if f in WHITELIST or any(f.startswith(x) for x in KEEP_PATTERNS):
            v, why = triage(f)
            rows.append([f, os.path.getsize(p), time.strftime('%Y-%m-%d %H:%M', time.localtime(os.path.getmtime(p))), v, why])
            continue
        st = os.stat(p)
        if st.st_mtime >= cut:
            rows.append([f, st.st_size, time.strftime('%Y-%m-%d %H:%M', time.localtime(st.st_mtime)), 'KEEP', '当日件（mtime 新）'])
            continue
        v, why = triage(f)
        rows.append([f, st.st_size, time.strftime('%Y-%m-%d %H:%M', time.localtime(st.st_mtime)), v, why])

    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['name', 'bytes', 'mtime', 'triage', 'reason'])
        w.writerows(rows)

    from collections import Counter
    c = Counter(r[3] for r in rows)
    print('ROOT FILES %d' % len(rows))
    for k in ['MOVE_ARCHIVE', 'KEEP', 'HUMAN']:
        print('  %-14s %d' % (k, c.get(k, 0)))
    print('CSV %s' % OUT)
    print('--- MOVE_ARCHIVE (top 20 by size) ---')
    ma = sorted([r for r in rows if r[3] == 'MOVE_ARCHIVE'], key=lambda x: -x[1])
    for r in ma[:20]:
        print('  %9d  %s  :: %s' % (r[1], r[0], r[4]))
    print('--- HUMAN ---')
    for r in [x for x in rows if x[3] == 'HUMAN']:
        print('  %9d  %s  :: %s' % (r[1], r[0], r[4]))


if __name__ == '__main__':
    main()
