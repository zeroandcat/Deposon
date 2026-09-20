"""V2 启动阶段 6 阶段输出验证"""
import hashlib, os, json

# 5 锚 SHA
anchor_path = r'D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json'
sha = hashlib.sha256(open(anchor_path,'rb').read()).hexdigest()[:12]
ok = 'OK' if sha == '03c6c01f3697' else 'FAIL'
print(f'5 锚 SHA-12: {sha} (期望 03c6c01f3697): {ok}')

# Corpus index SHA
idx_path = r'D:\私人资料\deposon-repo\corpus\v20\index.json'
sha2 = hashlib.sha256(open(idx_path,'rb').read()).hexdigest()[:12]
print(f'corpus/v20/index.json SHA-12: {sha2} (沿 V0.1 锁定)')

# Output files check
files = [
    r'D:\私人资料\deposon-repo\results\deposon_v2_phase1_60cells_2026_09_11.json',
    r'D:\私人资料\deposon-repo\results\deposon_v2_phase2_f2_2026_09_11.json',
    r'D:\私人资料\deposon-repo\results\deposon_v2_phase3_f3_2026_09_11.json',
    r'D:\私人资料\deposon-repo\results\deposon_v2_phase4_f4_2026_09_11.json',
    r'D:\私人资料\deposon-repo\results\deposon_v2_phase5_f5_2026_09_11.json',
    r'D:\私人资料\deposon-repo\docs\V3X\V2_PHASE1_60CELLS_2026_09_11.md',
    r'D:\私人资料\deposon-repo\docs\V3X\V2_PHASE2_F2_2026_09_11.md',
    r'D:\私人资料\deposon-repo\docs\V3X\V2_PHASE3_F3_2026_09_11.md',
    r'D:\私人资料\deposon-repo\docs\V3X\V2_PHASE5_F5_2026_09_11.md',
    r'D:\私人资料\deposon-repo\docs\V3X\V2_PHASE6_INTEGRATION_2026_09_11.md',
    r'D:\私人资料\deposon-repo\docs\V3X\PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md',
]
print()
for f in files:
    if os.path.isfile(f):
        sz = os.path.getsize(f)
        sha = hashlib.sha256(open(f,'rb').read()).hexdigest()[:12]
        print(f'  OK {sz:>7} bytes  {sha}  {os.path.basename(f)}')
    else:
        print(f'  MISSING: {f}')

# 5 阶段 summary
print()
print('=== 5 阶段 summary 摘要 ===')
for j in [1, 2, 3, 4, 5]:
    p = f'D:\私人资料\deposon-repo\results\deposon_v2_phase{j}_'
    if j == 1:
        p += '60cells_2026_09_11.json'
    elif j == 2:
        p += 'f2_2026_09_11.json'
    elif j == 3:
        p += 'f3_2026_09_11.json'
    elif j == 4:
        p += 'f4_2026_09_11.json'
    elif j == 5:
        p += 'f5_2026_09_11.json'
    if os.path.isfile(p):
        d = json.load(open(p, encoding='utf-8'))
        print(f'  阶段 {j}: {d.get("phase", "?")[:60]}')
        if 'summary' in d:
            s = d['summary']
            print(f'    summary keys: {list(s.keys())[:5]}')
            if 'verdict' in s:
                print(f'    verdict: {s["verdict"]}')
            if 'total_passed' in s:
                print(f'    pass_rate: {s.get("total_passed", "?")}/{s.get("total_cells", "?")} = {s.get("pass_rate", "?")}')
