import json
import re
import statistics

r = json.load(open('.tmp/_t15_records.json', encoding='utf-8'))

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

# Compute per-cell same-caption J (the real signal) vs all-pairs J
per_cell_same_caption = {}
for cell_idx in range(6):
    cell_j_same = []
    cell_j_cross = []
    cell_j_all = []
    cell_n_pairs_same = 0
    cell_n_pairs_cross = 0
    for teacher in ['kimi', 'GLM_1', 'GLM_2', 'coze', 'minimax']:
        recs = [rec for rec in r if rec['cell_idx'] == cell_idx and rec['teacher'] == teacher]
        if len(recs) < 2:
            continue
        for i in range(len(recs)):
            for j in range(i+1, len(recs)):
                jv = jaccard(recs[i]['response_text'], recs[j]['response_text'])
                cell_j_all.append(jv)
                if recs[i]['caption_id'] == recs[j]['caption_id']:
                    cell_j_same.append(jv)
                    cell_n_pairs_same += 1
                else:
                    cell_j_cross.append(jv)
                    cell_n_pairs_cross += 1
    per_cell_same_caption[cell_idx] = {
        'n_pairs_same': cell_n_pairs_same,
        'n_pairs_cross': cell_n_pairs_cross,
        'n_pairs_total': cell_n_pairs_same + cell_n_pairs_cross,
        'j_median_same': (round(statistics.median(cell_j_same), 4) if cell_j_same else None),
        'j_median_cross': (round(statistics.median(cell_j_cross), 4) if cell_j_cross else None),
        'j_median_all': (round(statistics.median(cell_j_all), 4) if cell_j_all else None),
        'j_mean_same': (round(statistics.mean(cell_j_same), 4) if cell_j_same else None),
        'j_mean_cross': (round(statistics.mean(cell_j_cross), 4) if cell_j_cross else None),
        'j_mean_all': (round(statistics.mean(cell_j_all), 4) if cell_j_all else None),
    }

print('=== Per-cell breakdown: same_caption vs cross_caption (the real signal vs pooled all) ===')
for cell_idx in range(6):
    d = per_cell_same_caption[cell_idx]
    cs = None
    for c in r['per_cell_summary'].values() if False else []:
        pass  # placeholder
    print(f'  cell {cell_idx}: '
          f'same J median={d["j_median_same"]}, mean={d["j_mean_same"]}; '
          f'cross J median={d["j_median_cross"]}, mean={d["j_mean_cross"]}; '
          f'all J median={d["j_median_all"]}, mean={d["j_mean_all"]}; '
          f'pair counts same={d["n_pairs_same"]}/cross={d["n_pairs_cross"]}/total={d["n_pairs_total"]}')