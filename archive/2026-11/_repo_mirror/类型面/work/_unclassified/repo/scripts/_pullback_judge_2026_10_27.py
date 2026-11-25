#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pullback 218 件之比对判（只读·不删不移）2026-10-27
判：每件按其 SHA-256 前 12 位，在 results\\ 与归档区中找同指纹者。
  已并入  = results 内命中
  仅在归档= 仅归档区命中
  两处皆无= 未命中（须另判）
输出：CSV + 控制台摘要
"""
import csv
import hashlib
import os
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
SRC = os.path.join(REPO, '_remote_pullback_2026_10_17')
RESULTS = os.path.join(REPO, 'results')
ARCHIVE = r'〔归档区〕'
OUT = os.path.join(REPO, 'results', 'work', 'process',
                   '_pullback_inmerge_judgement_2026_10_27.csv')


def sha12(p):
    h = hashlib.sha256()
    try:
        with open(p, 'rb') as f:
            while True:
                b = f.read(1024 * 1024)
                if not b:
                    break
                h.update(b)
        return h.hexdigest()[:12]
    except Exception:
        return None


def index(root, cap=0):
    """建 指纹 -> 路径 之索引"""
    idx = {}
    n = 0
    if not os.path.isdir(root):
        return idx, 0
    for dp, dn, fn in os.walk(root):
        for f in fn:
            p = os.path.join(dp, f)
            try:
                if os.path.getsize(p) == 0:
                    continue
            except Exception:
                continue
            h = sha12(p)
            n += 1
            if h:
                idx.setdefault(h, p)
            if cap and n >= cap:
                return idx, n
    return idx, n


def main():
    t0 = time.time()
    print('INDEX results ...')
    idx_r, n_r = index(RESULTS)
    print('  results: %d files, %d distinct fingerprints' % (n_r, len(idx_r)))
    print('INDEX archive ...')
    idx_a, n_a = index(ARCHIVE)
    print('  archive: %d files, %d distinct fingerprints' % (n_a, len(idx_a)))

    rows = []
    for dp, dn, fn in os.walk(SRC):
        for f in fn:
            p = os.path.join(dp, f)
            h = sha12(p)
            rel = os.path.relpath(p, SRC)
            if h is None:
                rows.append((rel, '', 'READ_FAIL', '', ''))
                continue
            if h in idx_r:
                rows.append((rel, h, 'ALREADY_IN_RESULTS', os.path.relpath(idx_r[h], REPO), ''))
            elif h in idx_a:
                rows.append((rel, h, 'ONLY_IN_ARCHIVE', '', idx_a[h]))
            else:
                rows.append((rel, h, 'NOT_FOUND', '', ''))

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['relpath', 'sha12', 'verdict', 'in_results', 'in_archive'])
        w.writerows(rows)

    from collections import Counter
    c = Counter(r[2] for r in rows)
    print('')
    print('PULLBACK total %d' % len(rows))
    for k in ['ALREADY_IN_RESULTS', 'ONLY_IN_ARCHIVE', 'NOT_FOUND', 'READ_FAIL']:
        print('  %-20s %d' % (k, c.get(k, 0)))
    print('CSV %s' % OUT)
    print('ELAPSED %.1fs' % (time.time() - t0))


if __name__ == '__main__':
    main()
