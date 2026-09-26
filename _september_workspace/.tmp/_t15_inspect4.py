import json
import re

r = json.load(open('.tmp/_t15_records.json', encoding='utf-8'))

# Compute all per-teacher Jaccard pairs and break down by same-caption vs cross-caption
TOKEN_RE = re.compile(r'[a-z0-9]+|[一-鿿]')
def tokenize(text):
    return TOKEN_RE.findall(text.lower())
def jaccard(a, b):
    sa = set(tokenize(a))
    sb = set(tokenize(b))
    if not sa and not sb:
        return 0.0
    union = sa | sb
    inter = sa & sb
    return len(inter) / len(union) if union else 0.0

print('=== Per-teacher Jaccard distribution (all 6 cells, 5 teachers) ===')
print('    Per teacher: same_caption_pairs (J>0 count / total) + cross_caption_pairs (J>0 count / total)')
print()
for cell_idx in range(6):
    print(f'  cell {cell_idx}:')
    for teacher in ['kimi', 'GLM_1', 'GLM_2', 'coze', 'minimax']:
        recs = [rec for rec in r if rec['cell_idx'] == cell_idx and rec['teacher'] == teacher]
        if len(recs) < 2:
            continue
        same_pairs = []
        cross_pairs = []
        for i in range(len(recs)):
            for j in range(i+1, len(recs)):
                jv = jaccard(recs[i]['response_text'], recs[j]['response_text'])
                if recs[i]['caption_id'] == recs[j]['caption_id']:
                    same_pairs.append(jv)
                else:
                    cross_pairs.append(jv)
        n_same_nonzero = sum(1 for j in same_pairs if j > 0)
        n_cross_nonzero = sum(1 for j in cross_pairs if j > 0)
        print(f'    {teacher:8s}: same_caption={n_same_nonzero}/{len(same_pairs)} ({[round(x,3) for x in same_pairs]}), '
              f'cross_caption={n_cross_nonzero}/{len(cross_pairs)} ({[round(x,3) for x in cross_pairs]})')
    print()

# Summary
print('=== Aggregate: ALL 6 cells × 5 teachers ===')
all_same = []
all_cross = []
for cell_idx in range(6):
    for teacher in ['kimi', 'GLM_1', 'GLM_2', 'coze', 'minimax']:
        recs = [rec for rec in r if rec['cell_idx'] == cell_idx and rec['teacher'] == teacher]
        if len(recs) < 2:
            continue
        for i in range(len(recs)):
            for j in range(i+1, len(recs)):
                jv = jaccard(recs[i]['response_text'], recs[j]['response_text'])
                if recs[i]['caption_id'] == recs[j]['caption_id']:
                    all_same.append(jv)
                else:
                    all_cross.append(jv)
print(f'  same_caption pairs: {len(all_same)} total, nonzero={sum(1 for x in all_same if x>0)}, '
      f'mean={sum(all_same)/len(all_same):.4f}, median={sorted(all_same)[len(all_same)//2]:.4f}')
print(f'  cross_caption pairs: {len(all_cross)} total, nonzero={sum(1 for x in all_cross if x>0)}, '
      f'mean={sum(all_cross)/len(all_cross):.4f}, median={sorted(all_cross)[len(all_cross)//2]:.4f}')