# -*- coding: utf-8 -*-
import hashlib, os, re, json

files = ['_v4_rootcause_upgrade_review.md', '_v4_supplement_executor_2026_09_23.py',
         '_v4_exec_n29_constructed_verdict.json', '_v4_exec_n30_constructed_verdict.json',
         '_v4_exec_n31_constructed_verdict.json']

key_pats = [r'\bsk-[A-Za-z0-9]{16,}', r'\bsk_[A-Za-z0-9]{16,}',
            r'\bopenai-[A-Za-z0-9]{16,}', r'\bghp_[A-Za-z0-9]{16,}',
            r'\bgho_[A-Za-z0-9]{16,}', r'\bghu_[A-Za-z0-9]{9,}',
            r'\bghs_[A-Za-z0-9]{9,}', r'\bAKIA[0-9A-Z]{12,}',
            r'\bASIA[0-9A-Z]{12,}', r'\bxai-[A-Za-z0-9]{16,}',
            r'\bxai_[A-Za-z0-9]{16,}', r'\banthropic-[A-Za-z0-9]{16,}',
            r'\bclaude-[A-Za-z0-9]{16,}', r'\bgemini-[A-Za-z0-9]{16,}',
            r'\bhuggingface-[A-Za-z0-9]{16,}', r'\bhf_[A-Za-z0-9]{16,}',
            r'\bcoze-[A-Za-z0-9]{16,}', r'\bteamorouter-[A-Za-z0-9]{16,}']

print('FINAL VERIFICATION')
print('=' * 80)
all_clean = True
for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
        h = hashlib.sha256(content.encode('utf-8')).hexdigest()[:12]
        sz = os.path.getsize(f)
        hits = []
        for pat in key_pats:
            for m in re.finditer(pat, content):
                hits.append((pat, m.group(0)[:8]))
        status = 'clean' if not hits else 'FAIL'
        if hits:
            all_clean = False
        print(f'  {f}')
        print(f'    SHA-12={h}  bytes={sz}  key_scan={status}')

v4_frozen = ['_v4_manifest_distill_min_v1.json',
             '_v4_distill_min_measure_result_v1r2.json']
print('-' * 80)
print('V4 frozen (must be unchanged):')
for f in v4_frozen:
    if os.path.exists(f):
        with open(f, 'rb') as fp:
            h = hashlib.sha256(fp.read()).hexdigest()[:12]
        print(f'  {f}  SHA-12={h}')

print('-' * 80)
print('KEY SCAN: ' + ('CLEAN' if all_clean else 'FAIL'))
print('Verdicts summary:')
for f in ['_v4_exec_n29_constructed_verdict.json', '_v4_exec_n30_constructed_verdict.json', '_v4_exec_n31_constructed_verdict.json']:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as fp:
            j = json.load(fp)
        print(f'  {f}: verdict={j["verdict"]} root_cause_cat={j["root_cause_cat"]} confidence={j["confidence"]}')