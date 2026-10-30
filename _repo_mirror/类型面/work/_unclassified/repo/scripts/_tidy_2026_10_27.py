#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""整理文件夹 · 干跑优先脚本（2026-10-27）
尺＝件数（PI 之令）；默认干跑；--execute 只移入暂存目录（可逆），删由 PI 亲手 rm --
用法：
  python -P _tidy_2026_10_27.py --block tmp
  python -P _tidy_2026_10_27.py --block tmp --execute
"""
import argparse
import csv
import os
import shutil
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
BLOCKS = {
    'tmp': os.path.join(REPO, '.tmp'),
    'pullback': os.path.join(REPO, '_remote_pullback_2026_10_17'),
    'roots': REPO,  # 仅根层文件，不递归
    'results_tmp': os.path.join(REPO, 'results', '.tmp'),  # results 内之嵌套 tmp
}
# 白名单：当日仍在用的活工具与仪器，永不入选
WHITELIST = {
    '_bcheck.py', '_append_generic.py', '_fill_item16.py',
    '_scan_glm_minimax.py', '_read_k31.py', '_read_k31b.py', '_read_k31c.py',
    '_land_k31_replies.py', '_land_k31_C.py', '_extract_cards.py',
    '_extract_cards2.py', '_scan_questionnaires.py', '_read_k31_last.py',
    # 结构性/库面：永不入选（本部干跑后补）
    '.gitignore', 'README.md',
}
# 永远保留之模式（根层）：库面与文档
KEEP_PATTERNS = ('deposon_', 'README', 'fingerprint_v0', 'gt_common',
                 'llm_fetch', 'llm_prior', 'mindmap_', 'svg_mindmap_')
# 结构性目录：根层扫描时排除
SKIP_DIRS = {'.git', '.mavis', '.trae', '.vscode', 'results', 'pi_rulings',
             'letters', 'docs', 'tools', 'tests', 'scripts', 'corpus',
             'attacks', 'paper', 'deposon_team', 'verifier', '_field_sources'}


def collect(block, keep_days, now):
    root = BLOCKS[block]
    if not os.path.isdir(root):
        return [], root
    cut = now - keep_days * 86400
    out = []
    if block == 'roots':
        for f in sorted(os.listdir(root)):
            p = os.path.join(root, f)
            if not os.path.isfile(p):
                continue
            if f in WHITELIST:
                continue
            if any(f.startswith(x) for x in KEEP_PATTERNS):
                continue
            st = os.stat(p)
            if st.st_mtime < cut:
                out.append((p, st.st_size, st.st_mtime, f))
    else:
        for dp, dn, fn in os.walk(root):
            for f in fn:
                p = os.path.join(dp, f)
                if f in WHITELIST:
                    continue
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime < cut:
                    out.append((p, st.st_size, st.st_mtime, os.path.relpath(p, root)))
    return out, root


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--block', required=True, choices=['tmp', 'pullback', 'roots', 'results_tmp'])
    ap.add_argument('--keep-days', type=int, default=1)
    ap.add_argument('--execute', action='store_true')
    ap.add_argument('--repo', default=REPO)
    a = ap.parse_args()

    now = time.time()
    items, root = collect(a.block, a.keep_days, now)
    ts = time.strftime('%Y%m%d_%H%M%S')
    stage = os.path.join(a.repo, '_pending_trash_%s_%s' % (a.block, ts))

    print('BLOCK   %s' % a.block)
    print('ROOT    %s' % root)
    print('SELECT  %d files (mtime older than %d day(s), whitelist excluded)' % (len(items), a.keep_days))
    tot = sum(x[1] for x in items)
    print('BYTES   %d (%.1f MB)' % (tot, tot / 1048576.0))

    # 同名冲突检查
    names = {}
    for p, sz, mt, rel in items:
        names.setdefault(os.path.basename(p), []).append(rel)
    clash = {k: v for k, v in names.items() if len(v) > 1}
    print('NAME_CLASH %d name(s) collide -> will keep relative structure (no flatten)' % len(clash))

    if not a.execute:
        print('DRY-RUN  nothing moved. Re-run with --execute to stage them.')
        for p, sz, mt, rel in items[:15]:
            print('   %10d  %s  %s' % (sz, time.strftime('%m-%d %H:%M', time.localtime(mt)), rel))
        if len(items) > 15:
            print('   ... and %d more' % (len(items) - 15))
        return

    # 实做：按相对路径移入暂存目录（保留结构·防同名覆盖）
    os.makedirs(stage, exist_ok=True)
    moved = 0
    failed = []
    for p, sz, mt, rel in items:
        dest = os.path.join(stage, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        try:
            shutil.move(p, dest)
            moved += 1
        except Exception as e:
            failed.append((rel, str(e)))

    man = os.path.join(stage, '_manifest_%s_%s.csv' % (a.block, ts))
    with open(man, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['name', 'bytes', 'mtime', 'relpath'])
        for p, sz, mt, rel in items:
            w.writerow([os.path.basename(p), sz,
                        time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mt)), rel])

    print('STAGED  %d moved, %d failed' % (moved, len(failed)))
    for rel, e in failed[:10]:
        print('   FAIL %s :: %s' % (rel, e))
    print('MANIFEST %s' % man)
    print('NEXT (run this by yourself to delete, recoverable):')
    print('   rm -- "%s"' % stage)


if __name__ == '__main__':
    main()
