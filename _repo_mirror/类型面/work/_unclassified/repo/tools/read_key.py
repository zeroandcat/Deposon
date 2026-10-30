"""Read the key file (GB18030) and extract sk-or-v1-... key without printing/logging it."""
import re
import sys

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


path = r'〔本地路径已脱敏〕'
with open(path, 'rb') as f:
    raw = f.read()
text = raw.decode('gb18030', errors='replace')

# Extract any sk-or-v1- followed by hex chars (OpenRouter key pattern)
matches = re.findall(r'sk-or-v1-[a-f0-9]{20,}', text, re.IGNORECASE)
if matches:
    # Don't print the full key — just confirm presence and length
    k = matches[0]
    print(f"FOUND_KEY len={len(k)} prefix={k[:12]}... suffix={k[-6:]}")
    # Write only a marker to a temp file for the next step to read
    with open(r_dep_path("tools/_key_marker.tmp"), 'w', encoding='utf-8') as mf:
        mf.write("KEY_PRESENT\n")
    # Save the key length so we can verify
    print(f"KEY_LEN={len(k)}")
else:
    print("NO_KEY_FOUND")
    # Print a tiny redacted sample to help debug if needed
    print("---FILE PREVIEW (first 500 chars)---")
    print(text[:500])
    print("---END---")
