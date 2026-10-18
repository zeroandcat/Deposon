"""Inspect 22 captions in v41 RAG backup cache."""
import json

p = 'D:/私人资料/deposon-repo/results/_v41_flash_rag_caption_embs.bak.json'
with open(p, 'r', encoding='utf-8') as f:
    data = json.load(f)

ce = data['caption_embs']
print(f"caption_count = {len(ce)}")
print(f"embedding_model = {data.get('embedding_model')}")
print(f"sanity = {data.get('sanity')}")
print(f"batch = {data.get('batch')}")
print("---all 22 object fields---")
for i, item in enumerate(ce):
    obj = item['object']
    emb_dim = len(item['embedding'])
    print(f"[{i:02d}] dim={emb_dim:4d}  obj={obj!r}")
