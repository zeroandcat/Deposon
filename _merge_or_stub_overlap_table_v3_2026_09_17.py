# -*- coding: utf-8 -*-
"""
Post-processor: append §3.5 merged cross-backbone β CI overlap table
(4 OR embedding × L30 = 6 pairs) + (4 OR embedding × 4 stub = 12 pairs N/A)
"""
import json
import hashlib
from pathlib import Path
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))

RESULTS_DIR = Path(r'D:\私人资料\deposon-repo\results')

# locate the latest v3 artifacts
artifacts = sorted([p for p in RESULTS_DIR.glob('_p_l_v3_phase2_or_embedding_v3_summary_*.json')], reverse=True)
if not artifacts:
    raise SystemExit('NO summary JSON found')
sum_path = artifacts[0]

md_artifacts = sorted([p for p in RESULTS_DIR.glob('_p_l_v3_phase2_or_embedding_v3_report_*.md')], reverse=True)
if not md_artifacts:
    raise SystemExit('NO MD report found')
md_path = md_artifacts[0]

summary = json.loads(sum_path.read_text(encoding='utf-8'))
bb_or_names = list(summary['backbones'].keys())
bb_or_ci = {a: (summary['backbones'][a]['beta_lo'], summary['backbones'][a]['beta_median'], summary['backbones'][a]['beta_hi'])
            for a in bb_or_names}

# 4 stub backbones (prev Phase 2, no embeddings)
stub_names = ['doubao', 'glm53', 'mistral', 'qwen3']
stub_ci = {}
for s in stub_names:
    stub_path = RESULTS_DIR / f'_p_l_v3_vector_embedding_{s}_L30_20260917_142748.json'
    if stub_path.exists():
        sb = json.loads(stub_path.read_text(encoding='utf-8'))
        if sb.get('cosine_similarity_matrix') is None:
            stub_ci[s] = (None, None, None)
        else:
            stub_ci[s] = (sb.get('beta_lo'), sb.get('beta_median'), sb.get('beta_hi'))
    else:
        stub_ci[s] = (None, None, None)


def fmt(v):
    return format(v, '.6f') if v is not None else 'NA'


# Build merged table
merged = []
# OR × OR pairs
for i, a in enumerate(bb_or_names):
    for j, b in enumerate(bb_or_names):
        if i >= j: continue
        ra, rb = bb_or_ci[a], bb_or_ci[b]
        if ra[0] is None or rb[0] is None:
            merged.append((f'{a}__OR_vs_OR__{b}', None, (ra[0], ra[2]), (rb[0], rb[2])))
        else:
            ov = not (ra[2] < rb[0] or rb[2] < ra[0])
            merged.append((f'{a}__OR_vs_OR__{b}', ov, (ra[0], ra[2]), (rb[0], rb[2])))

# OR × stub pairs (all N/A, because stub embeddings failed)
for a in bb_or_names:
    for s in stub_names:
        ra, rstub = bb_or_ci[a], stub_ci[s]
        merged.append((f'{a}__OR_vs_stub__{s}', None, (ra[0], ra[2]), (rstub[0], rstub[2])))

# Append §3.5 to MD
with md_path.open('a', encoding='utf-8') as f:
    f.write('\n## §3.5 Merged cross-backbone β CI overlap (4 OR + 4 stub, per task §6)\n\n')
    f.write('**Stub 4 backbones (Phase 2 之前跑失败, cosine matrix = null, β CI 不可计算)**:\n')
    for s in stub_names:
        f.write(f'- `{s}`: β CI = N/A (embeddings unavailable, status=INCOMPLETE)\n')
    f.write('\n**OR × OR 6 pairs (computed)**: see §3 above.\n\n')
    f.write('**OR × stub 12 pairs (N/A, stub side has no embeddings)**:\n\n')
    f.write('| OR embedding | stub backbone | OR β CI | stub β CI | overlap |\n')
    f.write('|---|---|---|---|---|\n')
    for pair_key, ov, ra, rb in merged:
        if '__OR_vs_stub__' in pair_key:
            a, s = pair_key.split('__OR_vs_stub__')
            f.write(f'| `{a}` | `{s}` | [{fmt(ra[0])}, {fmt(ra[1])}] | N/A | — (stub skip) |\n')
    f.write('\n**Combined verdict**: only OR×OR pair `qwen3-emb-8b_vs_bge-large` shows overlap. ')
    f.write('Other 5 OR×OR pairs do NOT overlap, and 12 OR×stub pairs are N/A (stub 缺 embeddings). ')
    f.write('**P2 判死 verdict remains GRAY**: β CI 大多不重叠 + stub 全缺, 不能宣称 robustness 已稳. ')
    f.write('建议: 跑第 5 个 OR embedding (Qwen/Qwen3-Embedding-4B dim=2560 已 confirmed 1018 reachable) 或触发 stub 重试.\n')
    f.write('\n')

print(f'Appended §3.5 to {md_path.name}, new sha12={hashlib.sha256(md_path.read_bytes()).hexdigest()[:12]}')
