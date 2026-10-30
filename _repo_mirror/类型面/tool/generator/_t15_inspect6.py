import json
r = json.load(open('results/_v4_supp_t15_result.json', encoding='utf-8'))
print('=== updated result.json key sections ===')
print('  metadata.schema:', r['metadata']['schema'])
print('  metadata.constraint_locale_hard:', r['metadata']['constraint_locale_hard'][:100])
print('  same_caption_breakdown cells count:', len(r['same_caption_breakdown']))
print()
print('=== honesty_disclosures keys ===')
for k in r['honesty_disclosures']:
    print(f'  {k}')
print()
print('=== honesty_disclosures new entries (first 300 chars) ===')
for k in r['honesty_disclosures']:
    if 'same_caption' in k or 'N_min' in k or 'partial_completion' in k:
        print(f'  {k}:')
        print(f'    {r["honesty_disclosures"][k][:600]}')
        print()
print('=== overall_verdict ===')
for k,v in r['overall_verdict'].items():
    if isinstance(v,str):
        print(f'  {k}:')
        print(f'    {v[:400]}')
    else:
        print(f'  {k}: {v}')
print()
print('=== records_summary ===')
for k,v in r['records_summary'].items():
    print(f'  {k}: {v}')
print()
print('=== cross_temp_std_per_dim ===')
print(f'  all_pairs: {r["cross_temp_std_per_dim"]["all_pairs"]}')
print(f'  nonempty: {r["cross_temp_std_per_dim"]["nonempty_pairs"]}')