"""Inspect 22 captions in v41 RAG backup cache."""
import json

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


p = _dep_path("results/_v41_flash_rag_caption_embs.bak.json")
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
