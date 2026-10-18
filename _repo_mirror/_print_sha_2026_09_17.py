import hashlib
from pathlib import Path
files = [
    ('L30_OK', '_p_l_v3_robustness_qwen3_L30_20260917_140017.json'),
    ('L30_OK', '_p_l_v3_robustness_glm53_L30_20260917_142011.json'),
    ('L60_RW', '_p_l_v3_robustness_qwen3_L60_20260917_140017.json'),
    ('L60_RW', '_p_l_v3_robustness_glm53_L60_20260917_142011.json'),
    ('L60_RW', '_p_l_v3_robustness_mistral_L60_20260917_142748.json'),
    ('Beta', '_p_l_v3_phase2_beta_summary_20260917_142748.json'),
    ('MD', '_p_l_v3_phase2_report_20260917_142748.md'),
    ('EmbS', '_p_l_v3_vector_embedding_qwen3_L30_20260917_142748.json'),
    ('EmbS', '_p_l_v3_vector_embedding_glm53_L30_20260917_142748.json'),
    ('EmbS', '_p_l_v3_vector_embedding_mistral_L30_20260917_142748.json'),
    ('EmbS', '_p_l_v3_vector_embedding_doubao_L30_20260917_142748.json'),
]
print('%-10s %-14s %-10s %s' % ('Type', 'SHA-12', 'Size', 'Filename'))
print('-' * 110)
rd = Path('D:/私人资料/deposon-repo/results')
for label, name in files:
    p = rd / name
    if p.exists():
        h = hashlib.sha256(p.read_bytes()).hexdigest()[:12]
        sz = p.stat().st_size
        print('%-10s %-14s %-10s %s' % (label, h, sz, name))
    else:
        print('%-10s MISSING %s' % (label, name))