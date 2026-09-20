# -*- coding: utf-8 -*-
"""Read-only inspection: extract CURRENT on-disk tars to a fresh audit4 dir,
list members, hash tex, and compare against last-known-good audit3_extract.
Does NOT modify anything in the paper folder."""
import os, sys, tarfile, hashlib, shutil

WORK = r'c:\Users\Administrator\.trae-cn\work\6a9a7e1c7578e46bf7c7f60c'
PAPER = r'd:\私人资料\deposon-repo\paper'
A4 = os.path.join(WORK, 'audit4_extract')
A3 = os.path.join(WORK, 'audit3_extract')

def sha(b):
    return hashlib.sha256(b).hexdigest()

if os.path.exists(A4):
    shutil.rmtree(A4)
os.makedirs(A4, exist_ok=True)

targets = [('en', 'deposon_arxiv_en.tar.gz'), ('cn', 'deposon_arxiv_cn.tar.gz')]
for tag, fn in targets:
    tp = os.path.join(PAPER, fn)
    raw = open(tp, 'rb').read()
    print('='*70)
    print('TAR', fn, 'size', len(raw), 'sha', sha(raw)[:16])
    out = os.path.join(A4, tag)
    os.makedirs(out, exist_ok=True)
    with tarfile.open(tp, 'r:gz') as tf:
        members = tf.getmembers()
        print('members:', len(members))
        for m in members:
            kind = 'DIR ' if m.isdir() else ('FILE' if m.isfile() else 'LINK')
            print('  [%s] %10d  %s' % (kind, m.size, m.name))
        tf.extractall(out)
    # find .tex files
    for root, dirs, files in os.walk(out):
        for f in files:
            if f.endswith('.tex'):
                p = os.path.join(root, f)
                b = open(p, 'rb').read()
                rel = os.path.relpath(p, out)
                print('  TEX', rel, 'size', len(b), 'sha', sha(b)[:16])
    # compare with audit3 tex
    for root, dirs, files in os.walk(A3):
        for f in files:
            if f.endswith('.tex'):
                p3 = os.path.join(root, f)
                b3 = open(p3, 'rb').read()
                # match by basename + lang
                if (tag == 'en' and f.endswith('_en.tex')) or (tag == 'cn' and f.endswith('_cn.tex')):
                    p4 = None
                    for r2, d2, f2 in os.walk(out):
                        for x in f2:
                            if x == f and x.endswith('.tex'):
                                p4 = os.path.join(r2, x)
                    if p4:
                        b4 = open(p4, 'rb').read()
                        same = (sha(b4) == sha(b3))
                        print('  COMPARE vs audit3', f, 'IDENTICAL' if same else 'DIFFERENT',
                              '(a4 %d bytes vs a3 %d bytes)' % (len(b4), len(b3)))
print('='*70)
print('extracted to', A4)
