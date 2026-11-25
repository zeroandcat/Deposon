#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""results\\ 内「同内容异名」检测（只读·不删不移）2026-10-27
尺＝件数（PI 之令）。判：SHA-256 前 12 位相同者＝同内容。
输出：分组 CSV（组号／指纹／件数／合计字节／各路径）
"""
import csv
import hashlib
import os
from collections import defaultdict

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
ROOT = os.path.join(REPO, 'results')
OUT = os.path.join(ROOT, 'work', 'process', '_results_dupe_groups_2026_10_27.csv')


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


def main():
    g = defaultdict(list)
    n = 0
    for dp, dn, fn in os.walk(ROOT):
        for f in fn:
            p = os.path.join(dp, f)
            try:
                sz = os.path.getsize(p)
            except Exception:
                continue
            if sz == 0:
                continue
            h = sha12(p)
            n += 1
            if h:
                g[h].append((sz, os.path.relpath(p, REPO)))

    dup = {h: v for h, v in g.items() if len(v) > 1}
    rows = []
    extra_files = 0
    extra_bytes = 0
    idx = 0
    for h, v in sorted(dup.items(), key=lambda x: -len(x[1])):
        idx += 1
        v = sorted(v, key=lambda x: -x[0])
        extra_files += len(v) - 1
        extra_bytes += sum(x[0] for x in v[1:])
        for k, (sz, rel) in enumerate(v):
            rows.append([idx, h, len(v), sz, 'KEEP' if k == 0 else 'DUPE', rel])

    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh)
        w.writerow(['group', 'sha12', 'group_size', 'bytes', 'role', 'relpath'])
        w.writerows(rows)

    print('SCANNED   %d files under results\\' % n)
    print('DISTINCT  %d' % len(g))
    print('DUP_GROUP %d groups (size>=2)' % len(dup))
    print('EXTRA     %d redundant files (kept 1 per group)' % extra_files)
    print('EXTRA_BYTES %.1f MB' % (extra_bytes / 1048576.0))
    print('CSV       %s' % OUT)
    print('--- TOP 10 GROUPS ---')
    for h, v in sorted(dup.items(), key=lambda x: -len(x[1]))[:10]:
        print('  %s  x%d  %d B  %s' % (h, len(v), v[0][0], v[0][1]))


if __name__ == '__main__':
    main()
