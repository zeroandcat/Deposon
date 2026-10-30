#!/usr/bin/env python3
import hashlib, os
files = {
    'L14+ prereg': 'results/_v4_supp_prereg_v02_add_L14V3_2026_09_24.md',
    'L14+ activation': 'results/_v4_supp_prereg_v02_add_L14V3_activation_2026_09_24.md',
    'L14V3 mapping': 'results/_v4_supp_l14v3_model_mapping_2026_09_24.md',
    'T15R2 verdict (format anchor)': 'results/_v4_supp_t15r2_verdict.md',
    'batch1 r6 result': 'results/_v4_supp_l14v3_batch1_r6_result.json',
    'batch2 r5 result': 'results/_v4_supp_l14v3_batch2_r5_result.json',
    'batch3 r5 result': 'results/_v4_supp_l14v3_batch3_r5_result.json',
    'batch4 r6 result': 'results/_v4_supp_l14v3_batch4_r6_result.json',
    'batch5 r5 result': 'results/_v4_supp_l14v3_batch5_r5_result.json',
    'batch6 r5 result': 'results/_v4_supp_l14v3_batch6_r5_result.json',
    'batch7 r5 result': 'results/_v4_supp_l14v3_batch7_r5_result.json',
    'batch8 r5 result': 'results/_v4_supp_l14v3_batch8_r5_result.json',
    'batch9 r5 result': 'results/_v4_supp_l14v3_batch9_r5_result.json',
    'batch10 r5 result': 'results/_v4_supp_l14v3_batch10_r5_result.json',
    'NEW: l14v3 n26 verdict': 'results/_v4_supp_l14v3_n26_verdict.md',
}
print(f'{"file":40s} {"SHA-12":12s} {"bytes":>8s} {"status":>10s}')
print('-' * 80)
for label, fp in files.items():
    if not os.path.exists(fp):
        print(f'{label:40s} MISSING')
        continue
    h = hashlib.sha256(open(fp, 'rb').read()).hexdigest()[:12]
    sz = os.path.getsize(fp)
    status = 'NEW' if 'NEW' in label else 'UNTOUCHED'
    print(f'{label:40s} {h:12s} {sz:8d} {status:>10s}')