# -*- coding: utf-8 -*-
"""_v3_review_r5_anchor_probe — 5 锚根件在盘/归档双副本核对（只读）"""
import hashlib, os, json

REPO = r'D:\私人资料\deposon-repo'
ARCH = r'D:\私人资料\_archive_deposon_2026_09_17'
REL = r'verifier\handoff\KT_ABC1_anchors_sha256_12.json'

def sha12(p):
    with open(p, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]

for base, tag in ((REPO, 'repo'), (ARCH, 'archive')):
    p = os.path.join(base, REL)
    if os.path.exists(p):
        sz = os.path.getsize(p)
        raw = open(p, 'rb').read()
        bom = raw[:3] == b'\xef\xbb\xbf'
        try:
            j = json.loads(raw.decode('utf-8-sig'))
            keys = list(j.keys()) if isinstance(j, dict) else f'list[{len(j)}]'
        except Exception as e:
            keys = 'PARSE_ERR:' + str(e)
        print(f'[{tag}] exists=YES size={sz} sha12={sha12(p)} bom={bom}')
        print(f'        keys={keys}')
        # 打印锚值（不打印密钥类字段，此件为 sha 锚）
        if isinstance(j, dict):
            for k, v in list(j.items())[:20]:
                s = json.dumps(v, ensure_ascii=False)
                print(f'          {k} = {s[:110]}')
    else:
        print(f'[{tag}] exists=NO  path={p}')
    print()

# 顺带核 §4 真缺件是否在 archive
print('--- 真缺件在 archive 的存在性 ---')
for f in ('results/deposon_v17_fusion_fix.json',
          'results/deposon_v18_api_supplements.json',
          'results/deposon_v20_baselines.json'):
    for base, tag in ((REPO, 'repo'), (ARCH, 'archive'), (r'D:\私人资料\deposon-sub', 'sub')):
        p = os.path.join(base, f.replace('/', os.sep))
        print(f'  {tag:<8} {f:<48} {"YES sha12="+sha12(p) if os.path.exists(p) else "NO"}')
    print()

print('--- 全盘 KT_ABC1* 副本 SHA-12（追 03c6c01f3697）---')
CANDS = [
    r'd:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json',
    r'd:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json',
    r'd:\私人资料\_non_upload_local_archive\verifier\handoff\KT_ABC1_anchors_sha256_12.json',
    r'd:\私人资料\_non_upload_local_archive\verifier\handoff\KT_ABC1_anchors_sha256_12_V3X_P_A_PATCH_2026_09_15.json',
]
for p in CANDS:
    if os.path.exists(p):
        s = sha12(p)
        hit = '  <== TARGET 03c6c01f3697' if s == '03c6c01f3697' else ''
        print(f'  {s}  {os.path.getsize(p):>7}B  {p}{hit}')
    else:
        print(f'  MISSING           {p}')

print()
print('--- 目标值出现处（文本扫描 repo/docs 与 results 中记载 03c6c01f3697 的文件数）---')
print('_r5 DONE')
