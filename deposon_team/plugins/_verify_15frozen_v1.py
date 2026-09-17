# -*- coding: utf-8 -*-
"""V3X 16 frozen verify v1 (2026-09-17, B2.2 task)
Reads schema from _v3x_frozen_schema_v1.json instead of hardcoded tuple.
"""
import hashlib, json, os

REPO_BASE = r'D:\私人资料\deposon-repo'
ARCHIVE_BASE = r'D:\私人资料\_archive_deposon_2026_09_17'
SCHEMA_PATH = os.path.join(REPO_BASE, 'deposon_team', 'plugins', '_v3x_frozen_schema_v1.json')

with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
    schema = json.load(f)

def resolve(path):
    """Try primary, fallback to archive mirror."""
    p = os.path.join(REPO_BASE, path)
    if os.path.exists(p):
        return p, 'repo'
    p = os.path.join(ARCHIVE_BASE, path.replace('\\', '/'))
    if os.path.exists(p):
        return p, 'archive'
    return None, 'MISSING'

ok, fail = 0, 0
print('SCHEMA: ' + schema['schema_version'] + ' (generated ' + schema['schema_generated_at'] + ')')
print('AUTHOR: ' + schema['schema_author'])
print('CHANGELOG:')
for cl in schema['schema_changelog']:
    print('  - ' + cl)
print()
print('ANCHORS (' + str(len(schema['anchors'])) + ' total):')
print('ID'.ljust(40) + ' EXPECTED'.ljust(15) + ' OBSERVED'.ljust(15) + ' MATCH'.ljust(7) + 'SOURCE'.ljust(8) + ' TYPE'.ljust(12) + 'NAME')
print('-' * 130)
for a in schema['anchors']:
    p, source = resolve(a['path_primary'])
    if not p:
        print(a['id'].ljust(40) + ' MISSING'.ljust(15) + ' -'.ljust(15) + ' FAIL'.ljust(7) + source.ljust(8) + ' ' + a['anchor_type'].ljust(12) + a['name'])
        fail += 1
        continue
    with open(p, 'rb') as f:
        data = f.read()
    sha12 = hashlib.sha256(data).hexdigest()[:12]
    match = (sha12 == a['expected_sha256_12'])
    print(a['id'].ljust(40) + ' ' + a['expected_sha256_12'].ljust(15) + ' ' + sha12.ljust(15) + ' ' + str(match).ljust(7) + ' ' + source.ljust(8) + ' ' + a['anchor_type'].ljust(12) + a['name'])
    if match:
        ok += 1
    else:
        fail += 1

print('-' * 130)
print('TOTAL: {} frozen files | OK: {} | FAIL: {}'.format(len(schema['anchors']), ok, fail))
print('0-touch declaration: {}'.format('PASS' if fail == 0 else 'FAIL'))
