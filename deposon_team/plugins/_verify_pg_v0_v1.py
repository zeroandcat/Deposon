# -*- coding: utf-8 -*-
"""V3X 16 frozen + P-G v0 verify v1 (2026-09-17, B2.2 task)
Reads schema from _v3x_frozen_schema_v1.json.
"""
import hashlib, json, os

REPO_BASE = r'D:\私人资料\deposon-repo'
ARCHIVE_BASE = r'D:\私人资料\_archive_deposon_2026_09_17'
SCHEMA_PATH = os.path.join(REPO_BASE, 'deposon_team', 'plugins', '_v3x_frozen_schema_v1.json')

with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
    schema = json.load(f)

def resolve(path):
    p = os.path.join(REPO_BASE, path)
    if os.path.exists(p):
        return p
    p = os.path.join(ARCHIVE_BASE, path.replace('\\', '/'))
    return p if os.path.exists(p) else None

ok, fail = 0, 0
print('SCHEMA: ' + schema['schema_version'])
print('16 frozen files verify (with archive fallback):')
print('ID'.ljust(40) + ' EXPECTED'.ljust(15) + ' OBSERVED'.ljust(15) + ' MATCH'.ljust(7) + 'NAME')
print('-' * 130)
for a in schema['anchors']:
    p = resolve(a['path_primary'])
    if not p:
        print(a['id'].ljust(40) + ' MISSING'.ljust(15) + ' -'.ljust(15) + ' FAIL'.ljust(7) + a['name'])
        fail += 1
        continue
    with open(p, 'rb') as f:
        data = f.read()
    sha12 = hashlib.sha256(data).hexdigest()[:12]
    match = (sha12 == a['expected_sha256_12'])
    print(a['id'].ljust(40) + ' ' + a['expected_sha256_12'].ljust(15) + ' ' + sha12.ljust(15) + ' ' + str(match).ljust(7) + a['name'])
    if match:
        ok += 1
    else:
        fail += 1

print('-' * 130)
print('16 frozen TOTAL: OK: {} | FAIL: {}'.format(ok, fail))
print('0-touch declaration: {}'.format('PASS' if fail == 0 else 'FAIL'))
print()

# P-G V0 spec
pg_path = os.path.join(REPO_BASE, 'docs/V3X/P_G_NON_EUCLIDEAN_SCATTERING_V0_SPEC.md')
print('P-G V0 spec:')
print('  path:', pg_path)
print('  size:', os.path.getsize(pg_path), 'bytes')
with open(pg_path, 'rb') as f:
    pg_data = f.read()
pg_sha12 = hashlib.sha256(pg_data).hexdigest()[:12]
pg_sha256 = hashlib.sha256(pg_data).hexdigest()
print('  SHA-12:', pg_sha12)
print('  SHA-256 full:', pg_sha256)
print()

# P-G 5 anchors
print('P-G 5 anchors (from schema v1):')
print('ANCHOR_ID'.ljust(35) + ' PLACEHOLDER SHA-12'.ljust(20) + ' RECOMPUTED'.ljust(15) + ' MATCH')
print('-' * 80)
for a in schema['pg_anchors']:
    seed = ('P_G_V0_PLACEHOLDER_{}_2026_09_15'.format(a['id'])).encode()
    recomputed = hashlib.sha256(seed).hexdigest()[:12]
    match = (recomputed == a['placeholder'])
    print(a['id'].ljust(35) + ' ' + a['placeholder'].ljust(20) + ' ' + recomputed.ljust(15) + ' ' + str(match))
