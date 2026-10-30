import json
import re

r = json.load(open('.tmp/_t15_records.json', encoding='utf-8'))

# Show raw bytes for all 4 records of kimi in cell 0
print('--- raw bytes (utf-8) of each cell 0 kimi record ---')
for rec in r:
    if rec['cell_idx'] == 0 and rec['teacher'] == 'kimi':
        print(f'  caption={rec["caption_id"]}, r={rec["reask_idx"]}: bytes={rec["response_text"].encode("utf-8")}, len={rec["response_text_len"]}')

# Now compute jaccard properly per the executor's logic
print()
print('--- computing per-teacher jaccard pairs ---')
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

for cell_idx in [0, 5]:
    for teacher in ['kimi', 'minimax']:
        recs = [rec for rec in r if rec['cell_idx'] == cell_idx and rec['teacher'] == teacher]
        if len(recs) < 2:
            continue
        print(f'\n  cell {cell_idx} / teacher {teacher}: {len(recs)} records')
        for i in range(len(recs)):
            for j in range(i+1, len(recs)):
                ti = recs[i]['response_text']
                tj = recs[j]['response_text']
                jv = jaccard(ti, tj)
                sa = set(tokenize(ti))
                sb = set(tokenize(tj))
                print(f'    rec{i} (cap={recs[i]["caption_id"]}, r={recs[i]["reask_idx"]}) vs '
                      f'rec{j} (cap={recs[j]["caption_id"]}, r={recs[j]["reask_idx"]}): '
                      f'ti bytes={ti.encode("utf-8")}, tj bytes={tj.encode("utf-8")}, '
                      f'|ti_tok|={len(sa)}, |tj_tok|={len(sb)}, |inter|={len(sa&sb)}, |union|={len(sa|sb)}, J={jv}')
        break  # just first teacher per cell
    break  # just cell 0