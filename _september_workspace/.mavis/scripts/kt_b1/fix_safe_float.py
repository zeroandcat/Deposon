import re
import os

DIR = r'D:\私人资料\deposon-repo\.mavis\scripts\kt_b1'
for fn in ['boss_b1_sinkhorn_ot.py', 'boss_b2_kd.py', 'boss_b3_llmlingua.py']:
    fn = os.path.join(DIR, fn)
    with open(fn, 'r', encoding='utf-8') as f:
        content = f.read()
    new_helper = '''def _safe_float(x, default=0.0):
    """Tolerate None / string in float conversion."""
    if x is None:
        return default
    try:
        return float(x)
    except (TypeError, ValueError):
        return default


'''
    pattern = re.compile(r'(def _extract_200_questions\(v19_data: dict\) -> list\[dict\]:\n)')
    content = pattern.sub(new_helper + r'\1', content, count=1)
    content = content.replace("float(p.get('predicted', 0.0))", "_safe_float(p.get('predicted'), 0.0)")
    content = content.replace("float(p.get('answer', 0.0))", "_safe_float(p.get('answer'), 0.0)")
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed:', fn)