import collections
import json

d = json.load(open(r'.tmp\_b12_q1_refs_results_2026_09_29.json', encoding='utf-8'))
rows = sorted(d['rows'], key=lambda r: r['mtime'])
own = {'.tmp/_b12_q1_refs_2026_09_29.py'}

print('Cumulative referencing-file count over time (this stick own script excluded):')
n = collections.Counter()
slices38 = []
for r in rows:
    if r['rel'] in own:
        continue
    n[r['tree']] += 1
    tot = sum(n.values())
    if tot == 38:
        slices38.append((r['mtime'], dict(n)))
    print(f"  {r['mtime']}  total={tot:2d}  letters={n['letters']:2d} "
          f"results={n['results']:2d} docs={n['docs']:2d} tmp={n['.tmp']:2d}   +{r['rel']}")
print()
print('Time-slices where total == 38:')
if not slices38:
    print('   (NONE)')
for s in slices38:
    print('   ', s)
