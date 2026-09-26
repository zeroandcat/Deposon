import json
import re

r = json.load(open('.tmp/_t15_records.json', encoding='utf-8'))
print(f'total records: {len(r)}')
print()

print('=== sample responses from cell 0 (L2/temp=0.0) kimi teacher ===')
shown = 0
for rec in r:
    if rec['cell_idx'] == 0 and rec['teacher'] == 'kimi':
        print(f'  caption={rec["caption_id"]}, r={rec["reask_idx"]}: len={rec["response_text_len"]}')
        print(f'    text={rec["response_text"][:200]!r}')
        shown += 1
        if shown >= 4:
            break
print()

print('=== sample responses from cell 5 (L14/temp=0.5) kimi teacher ===')
shown = 0
for rec in r:
    if rec['cell_idx'] == 5 and rec['teacher'] == 'kimi':
        print(f'  caption={rec["caption_id"]}, r={rec["reask_idx"]}: len={rec["response_text_len"]}')
        print(f'    text={rec["response_text"][:200]!r}')
        shown += 1
        if shown >= 4:
            break
print()

print('=== tokenization test ===')
TOKEN_RE = re.compile(r'[a-z0-9]+|[一-鿿]')
for rec in r[:5]:
    text = rec['response_text']
    tokens = TOKEN_RE.findall(text.lower())
    print(f'  text[:80]={text[:80]!r}')
    print(f'  tokens={tokens[:15]}')
    print()

print('=== jaccard test on first 4 responses in cell 0, kimi teacher ===')
kimi_cell0 = [rec for rec in r if rec['cell_idx'] == 0 and rec['teacher'] == 'kimi']
print(f'  found {len(kimi_cell0)} records')
if len(kimi_cell0) >= 2:
    texts = [rec['response_text'] for rec in kimi_cell0]
    print(f'  text1[:60]={texts[0][:60]!r}')
    print(f'  text2[:60]={texts[1][:60]!r}')
    tok1 = set(TOKEN_RE.findall(texts[0].lower()))
    tok2 = set(TOKEN_RE.findall(texts[1].lower()))
    print(f'  tokens1 (unique) = {sorted(tok1)[:15]}')
    print(f'  tokens2 (unique) = {sorted(tok2)[:15]}')
    print(f'  intersection = {sorted(tok1 & tok2)[:15]}')
    print(f'  union = {sorted(tok1 | tok2)[:15]}')
    if tok1 | tok2:
        print(f'  J = {len(tok1 & tok2) / len(tok1 | tok2)}')