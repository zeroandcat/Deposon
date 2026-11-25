import hashlib, os
p = 'results/_v4_pi_cot_v2_coding_review_2026_09_26.md'
data = open(p, 'rb').read()
print('FINAL')
print('  path:', p)
print('  bytes:', len(data))
print('  sha12:', hashlib.sha256(data).hexdigest()[:12])
print()
tmps = [f for f in os.listdir('results/') if f.startswith('_tmp')]
print('results/ _tmp cleanup:', 'OK (no _tmp)' if not tmps else f'REMAINING: {tmps}')