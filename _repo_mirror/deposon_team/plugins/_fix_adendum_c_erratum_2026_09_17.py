# -*- coding: utf-8 -*-
"""Fix: Adendum C v2 P-M contradiction recurrence — append erratum field (no original values changed).
Reads both JSON files, appends erratum_2026_09_17 note, records before/after SHA-12."""
import json, hashlib, os

FILES = [
    r'D:\私人资料\deposon-repo\results\_adendum_C_pm_attack_surface_v2_20260917_133852.json',
    r'D:\私人资料\deposon-repo\results\_adendum_C_pm_attack_surface_v2_20260917_133726.json',
]
ERRATUM = {
    'erratum_2026_09_17': {
        'raised_by': 'Trae code co-audit (KIMI push batch-3 degeneration precheck)',
        'issue': 'detection_rate=0.0 across all budgets coexists with caught_rate_mean=1.0 and verdict=PASS; verdict_reason claims ">=0.5" threshold satisfied — same counting-semantics inversion as the original P-M 2026-09-16 defect',
        'status': 'UNVERIFIED until producer (Mavis/worker) reconciles detection_rate vs caught_rate field semantics',
        'original_verdict_preserved': True,
        'note': 'appended read-only annotation; no original field values modified'
    }
}

for p in FILES:
    with open(p, 'rb') as f:
        before = hashlib.sha256(f.read()).hexdigest()[:12]
    if not os.path.exists(p):
        print('MISSING', p); continue
    with open(p, 'r', encoding='utf-8') as f:
        d = json.load(f)
    if 'erratum_2026_09_17' in d:
        with open(p, 'rb') as f:
            after = hashlib.sha256(f.read()).hexdigest()[:12]
        print('skip(idempotent)', os.path.basename(p), before, '->', after)
        continue
    d.update(ERRATUM)
    with open(p, 'w', encoding='utf-8') as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    with open(p, 'rb') as f:
        after = hashlib.sha256(f.read()).hexdigest()[:12]
    print('patched', os.path.basename(p), before, '->', after)

print('done')
