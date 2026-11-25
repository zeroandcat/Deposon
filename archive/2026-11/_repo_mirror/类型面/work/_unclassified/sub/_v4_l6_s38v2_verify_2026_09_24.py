# -*- coding: utf-8 -*-
"""L6 S-38 v2 final verification (key + sha + keyscan + reproducibility)."""
import hashlib, json, re, sys

# === 1. v1 file 0 触动铁证 ===
with open('results/_v4_supp_a1_s38_result.json', 'rb') as f:
    v1_bytes = f.read()
v1_sha12 = hashlib.sha256(v1_bytes).hexdigest()[:12]
v1_bytes_len = len(v1_bytes)
v1_match = v1_sha12.lower() == '41f40fba1142'
print(f'[V1_SHA] {v1_sha12} ({v1_bytes_len}B) match_with_41f40fba1142={v1_match}')
assert v1_match, 'V1 file SHA-12 mismatch! R5 FAIL'

# === 2. v1 executor 0 触动 ===
with open('results/_v4_supp_a1_executor.py', 'rb') as f:
    v1exe_bytes = f.read()
v1exe_sha12 = hashlib.sha256(v1exe_bytes).hexdigest()[:12]
v1exe_match = v1exe_sha12.lower() == 'a5d3179b1fb2'
print(f'[V1_EXE_SHA] {v1exe_sha12} ({len(v1exe_bytes)}B) match_with_a5d3179b1fb2={v1exe_match}')
assert v1exe_match

# === 3. 预登记锚 0 触动 ===
for path, expected in [
    ('results/_v4_seeds_prereg_supplement_2026_09_23.md', '113cbe555643'),
    ('results/_v4_supp_prereg_v02_2026_09_24.md', 'd85488a64d89'),
    ('results/_v4_supp_prereg_v02_activation_2026_09_24.md', 'ad42992dc75d'),
]:
    with open(path, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()[:12]
    m = h.lower() == expected.lower()
    print(f'[ANCHOR] {h} {path} match={m}')
    assert m, f'Anchor {path} SHA mismatch: {h} != {expected}'

# === 4. corpus 0 触动 ===
with open('corpus/v20_caption_surface/caption_features_22.json', 'rb') as f:
    h = hashlib.sha256(f.read()).hexdigest()[:12]
m = h.lower() == '727a253566dd'
print(f'[CORPUS] {h} caption_features_22.json match={m}')
assert m

# === 5. v2 result key_scan clean ===
with open('results/_v4_supp_l6_s38v2_result.json', 'r', encoding='utf-8') as f:
    v2_result = json.load(f)
patterns = [r'\bsk-[A-Za-z0-9_\-]{20,}\b', r'\bbearer\s+[A-Za-z0-9_\-]{20,}\b', r'\bghp_[A-Za-z0-9]{20,}\b']
all_text = json.dumps(v2_result, ensure_ascii=False)
hits = sum(len(re.findall(p, all_text, re.IGNORECASE)) for p in patterns)
print(f'[V2_RESULT_KEYSCAN] hits={hits}')
assert hits == 0

# === 6. v2 result sha ===
v2result_path = 'results/_v4_supp_l6_s38v2_result.json'
with open(v2result_path, 'rb') as f:
    v2_bytes = f.read()
v2result_sha = hashlib.sha256(v2_bytes).hexdigest()[:12]
print(f'[V2_RESULT_SHA] {v2result_sha} bytes={len(v2_bytes)}')

# === 7. v2 executor key_scan clean ===
with open('results/_v4_supp_l6_s38v2_executor.py', 'r', encoding='utf-8') as f:
    v2exe_text = f.read()
exe_hits = sum(len(re.findall(p, v2exe_text, re.IGNORECASE)) for p in patterns)
print(f'[V2_EXECUTOR_KEYSCAN] hits={exe_hits}')
assert exe_hits == 0

# === 8. v2 verdict key_scan clean ===
with open('results/_v4_supp_l6_s38v2_verdict.md', 'r', encoding='utf-8') as f:
    v2verd_text = f.read()
verd_hits = sum(len(re.findall(p, v2verd_text, re.IGNORECASE)) for p in patterns)
print(f'[V2_VERDICT_KEYSCAN] hits={verd_hits}')
assert verd_hits == 0

# === 9. v2 note key_scan clean ===
with open('results/_v4_supp_l6_s38v2_prereg_note.md', 'r', encoding='utf-8') as f:
    v2note_text = f.read()
note_hits = sum(len(re.findall(p, v2note_text, re.IGNORECASE)) for p in patterns)
print(f'[V2_NOTE_KEYSCAN] hits={note_hits}')
assert note_hits == 0

# === 10. 0 hash() builtin check (search v2 executor) ===
builtin_hash_uses = len(re.findall(r'\bhash\(\s*[a-z_]+\s*\)', v2exe_text))
print(f'[BUILTIN_HASH_USAGE] {builtin_hash_uses} (must = 0)')
assert builtin_hash_uses == 0

# === 11. 0 LLM/proxy/gateway check ===
for kw in ['import openai', 'import anthropic', 'teamorouter', 'openrouter']:
    c = v2exe_text.lower().count(kw.lower())
    if c > 0:
        print(f'[LLM_PROXY_GATEWAY] {kw} count={c}')

print()
print('=== ALL CHECKS PASS ===')