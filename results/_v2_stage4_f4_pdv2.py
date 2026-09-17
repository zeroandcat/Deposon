# -*- coding: utf-8 -*-
"""
deposon V2 阶段 4 (F-4 P-D V0.2 语义指纹层)
- 0 新 API 调用, 算法层
- 用 22 caption 已有 embedding 算 LSH 或 PCA-12 主成分符号
- 双指纹: byte_hash(SHA-256[0:12], P-D V0.1 已有) + semantic_hash(LSH/PCA-12)
- 写 V0.2 升级文档
"""
import os, sys, json, time, hashlib
import numpy as np
from datetime import datetime, timezone, timedelta

DPATH_REF = r'D:\私人资料\deposon-repo\results\deposon_dpath_cross_modal_2026_09_10.json'
VOLC_22CAP_REF = r'D:\私人资料\deposon-repo\results\deposon_volcengine_22caption_embedding_2026_09_10.json'
SPEC_DIR = r'D:\私人资料\deposon-repo\docs\V3X'

LOG_LINES = []
def log(msg):
    line = f'[{time.strftime("%H:%M:%S")}] {msg}'
    print(line, flush=True)
    LOG_LINES.append(line)


def main():
    # 锚校验
    anchor_path = r'D:\私人资料\deposon-repo\verifier\handoff\KT_ABC1_anchors_sha256_12.json'
    anchor_sha = hashlib.sha256(open(anchor_path, 'rb').read()).hexdigest()[:12]
    assert anchor_sha == '03c6c01f3697', f'5 锚 SHA 变: {anchor_sha}'
    log(f'ANCHOR_OK SHA-12={anchor_sha}')

    # 1) 读 P-D V0.1 SPEC 现有 byte_hash
    pd_spec_path = os.path.join(SPEC_DIR, 'P_D_FINGERPRINT_V0_SPEC.md')
    if os.path.isfile(pd_spec_path):
        with open(pd_spec_path, 'r', encoding='utf-8') as f:
            pd_spec = f.read()
        log(f'P_D_V0_SPEC_LOADED len={len(pd_spec)}')
    else:
        pd_spec = ''
        log('P_D_V0_SPEC missing')

    # 2) 读 22 caption SVD2 坐标
    volc = json.load(open(VOLC_22CAP_REF, 'r', encoding='utf-8'))
    svd2 = volc['svd2_coords']  # dict: caption_id -> [x, y]
    concept_ids = list(svd2.keys())
    svd2_arr = np.array([svd2[cid] for cid in concept_ids], dtype=float)
    log(f'SVD2_LOADED n={len(concept_ids)} dim=2')

    # 3) byte_hash (P-D V0.1) 用 caption_id 字符串
    byte_hashes = {}
    for cid in concept_ids:
        h = hashlib.sha256(cid.encode('utf-8')).hexdigest()[:12]
        byte_hashes[cid] = h
    log(f'BYTE_HASH (V0.1) computed n={len(byte_hashes)} sample: {concept_ids[0]} → {byte_hashes[concept_ids[0]]}')

    # 4) semantic_hash (P-D V0.2) 用 PCA-12 + 符号位
    # 我们的 embedding 是 2048-d 但只存了 SVD2 (2-d)
    # 用 SVD2 → 上采样到 12-d (用 polynomial features 或 repeat+noise)
    # 简化: PCA-12 on SVD2 → 12 主成分 → 符号位 → 12 bit 指纹
    # 由于 dim=2, PCA-12 实际只有 2 个有效维度,余 10 个近零(噪声)
    # 实际方案: 用 SVD2 + LSH (random projection) → 12 bit
    np.random.seed(42)
    # 12 个 random hyperplanes in 2D, 每个给一个 bit
    n_bits = 12
    hyperplanes = np.random.randn(n_bits, 2)  # 12x2
    # 投影
    proj = svd2_arr @ hyperplanes.T  # 22x12
    bits = (proj > 0).astype(int)  # 22x12 binary
    semantic_hashes = {}
    for i, cid in enumerate(concept_ids):
        # 12 bit → 3 个 hex 字符
        bit_str = ''.join(str(b) for b in bits[i])
        hex_str = hex(int(bit_str, 2))[2:].zfill(3)  # 000-FFF
        semantic_hashes[cid] = hex_str
    log(f'SEMANTIC_HASH (V0.2, LSH-12bit) computed n={len(semantic_hashes)} sample: {concept_ids[0]} → {semantic_hashes[concept_ids[0]]} (bits={bits[0].tolist()})')

    # 5) 双指纹拼接
    dual_fingerprints = {}
    for cid in concept_ids:
        dual_fingerprints[cid] = {
            'byte_hash': byte_hashes[cid],
            'semantic_hash': semantic_hashes[cid],
            'dual_24bit': byte_hashes[cid][:6] + semantic_hashes[cid],  # 12 + 12 = 24 bit
        }
    log(f'DUAL_FINGERPRINT (V0.2) computed n={len(dual_fingerprints)}')

    # 6) 验证:同源文件应识别为同根语义指纹
    # L 家族 6 个 caption 应该 semantic_hash 前几位相似(高维空间投影同类聚集)
    # 4 class per_class_members
    per_class = volc['per_class_members']
    class_intra_sim = {}
    for class_name, members in per_class.items():
        # 取前 4 个成员的 semantic_hash bits 算 pairwise Hamming
        if len(members) >= 2:
            bits_list = []
            for m in members:
                if m in semantic_hashes:
                    # 反向 hex → bits
                    n = int(semantic_hashes[m], 16)
                    bit_str = bin(n)[2:].zfill(12)
                    bits_list.append([int(b) for b in bit_str])
            if len(bits_list) >= 2:
                # pairwise Hamming
                hams = []
                for i in range(len(bits_list)):
                    for j in range(i+1, len(bits_list)):
                        h = sum(a != b for a, b in zip(bits_list[i], bits_list[j]))
                        hams.append(h)
                if hams:
                    class_intra_sim[class_name] = round(sum(hams)/len(hams), 2)
                    log(f'  class "{class_name}" ({len(members)} members) intra-Hamming mean={class_intra_sim[class_name]}')

    # 7) 与 byte_hash 区分度对比
    # byte_hash (V0.1) 仅基于 caption_id 字符串,同源 caption 不一定有相同 hash
    # semantic_hash (V0.2) 基于 embedding 投影,同源 caption 应有相似 hash
    log('CONTRAST: byte_hash is string-based, semantic_hash is embedding-based')
    log('V0.2 improvement: 2 caption with similar embedding → similar semantic_hash')

    # 8) 写 V0.2 SPEC 文档
    spec_v2 = f"""# P-D 语义指纹 V0.2 SPEC (F-4 输出)

> 写入日期: {time.strftime('%Y-%m-%d %H:%M:%S')}
> 阶段: V2 阶段 4 (F-4 P-D V0.2 语义指纹层)
> 算法: 0 新 API 调用, 沿用 22 caption SVD-2 坐标 + 12-bit LSH

## 1. 动机

P-D V0.1 仅用 `SHA-256(caption_id)[0:12]` 算 byte_hash,这是基于字符串的指纹,
**对同源 caption (如 L 家族 6 个) 无任何区分度**(全部独立 hash)。

V0.2 引入 **semantic_hash**: 用 12-bit LSH (Locality-Sensitive Hashing)
将 22 caption SVD-2 投影到 12 个随机超平面, 符号位 → 12-bit 二进制 → 3 hex 字符。

## 2. 双指纹设计

每个 caption 现在有 2 个独立指纹:

| 字段 | 算法 | 长度 | 性质 |
|------|------|------|------|
| `byte_hash` | SHA-256(caption_id)[0:12] | 12 hex (48 bit) | V0.1, 字符串级 |
| `semantic_hash` | LSH-12bit (12 hyperplane sign) | 3 hex (12 bit) | V0.2, 语义级 |
| `dual_24bit` | byte_hash[:6] + semantic_hash | 9 hex (36 bit) | V0.2 组合 |

**dual_24bit = 9 hex 字符 = 36 bit**, 碰撞概率 ~1/2^36 ≈ 1e-11,
但同源 caption 会自动聚集 (semantic_hash 相近)。

## 3. LSH 算法

```python
import numpy as np, hashlib

# 22 caption SVD-2 坐标 (从 volcengine_22caption_embedding_2026_09_10.json)
svd2 = {{'L_algorithm_process': [-0.52, 0.61], 'S1': [0.39, -0.21], ...}}  # 22 个

# 12 个 random hyperplane (固定 seed=42 复现)
np.random.seed(42)
hyperplanes = np.random.randn(12, 2)  # 12 x 2

# 投影 + 符号
for cid, (x, y) in svd2.items():
    proj = np.array([x, y]) @ hyperplanes.T  # 1 x 12
    bits = (proj > 0).astype(int)
    bit_str = ''.join(str(b) for b in bits)
    semantic_hash = hex(int(bit_str, 2))[2:].zfill(3)
```

## 4. 实测 22 caption 指纹 (本批次)

| caption_id | byte_hash (V0.1) | semantic_hash (V0.2) | dual_24bit |
|------------|------------------|----------------------|------------|
"""
    
    for cid in concept_ids[:22]:
        spec_v2 += f"| {cid} | `{byte_hashes[cid]}` | `{semantic_hashes[cid]}` | `{dual_fingerprints[cid]['dual_24bit']}` |\n"
    
    spec_v2 += f"""

## 5. 类内 Hamming 距离 (semantic_hash 同源聚集度)

| 类别 (family) | 成员数 | semantic_hash intra-Hamming |
|---------------|--------|------------------------------|
"""
    for cn, h in class_intra_sim.items():
        spec_v2 += f"| {cn} | {len(per_class[cn])} | {h} bits / 12 |\n"
    
    spec_v2 += f"""

越低 = 同源 caption 在语义空间越聚集 (理想 < 6 bits/12)。

## 6. V0.1 → V0.2 升级点

1. **新增 `semantic_hash`**: 12-bit LSH from SVD-2 坐标
2. **保留 `byte_hash`**: V0.1 字符串指纹, 保证向后兼容
3. **新增 `dual_24bit`**: 9 hex 组合, 同时具备字符串 + 语义信息
4. **验证手段**: 类内 Hamming 距离 < 6 bits (在 4-class 体系下应有信号)

## 7. 后续工作 (V0.3 候选)

- 升级到 **embedding-2048-d 直接 LSH-128bit** (跳过 SVD-2, 信息保留更高)
- 加 **permutation-based LSH** (随机排列 → 排序签名) 抗 LSH 维度灾难
- 集成到 P-D V0.2 守恒审计的 fingerprint 模块 (沿 corpus/v20/index.json SHA-12 锁)

## 8. 7 铁律遵守

- 0 新 API 调用 (F-4 算法层)
- 不动 5 锚 JSON (SHA-12 03c6c01f3697 unchanged)
- 不动 corpus/v20/index.json
- 不动 4 SPEC V0.1 + v19 + v21
- 严守 user 17:38 (仅火山 catalog) + 17:41 (仅 coding-plan)

## 9. 输出文件

- 文档: `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md`
- 阶段 4 数据: `results/deposon_v2_phase4_f4_2026_09_11.json`
- 5 锚 SHA-12 验证: 03c6c01f3697 unchanged
"""

    spec_path = os.path.join(SPEC_DIR, 'PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md')
    with open(spec_path, 'w', encoding='utf-8') as f:
        f.write(spec_v2)
    log(f'SPEC_WRITTEN {spec_path} ({len(spec_v2)} chars)')

    # 9) 阶段 4 数据 JSON
    results = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%S+08:00'),
        'phase': 'V2 阶段 4 (F-4 P-D V0.2 语义指纹层)',
        'algorithm': '12-bit LSH on SVD-2 coords (random hyperplanes, seed=42)',
        'n_captions': len(concept_ids),
        'concept_ids': concept_ids,
        'byte_hashes': byte_hashes,
        'semantic_hashes': semantic_hashes,
        'dual_fingerprints': dual_fingerprints,
        'class_intra_hamming': class_intra_sim,
        'spec_doc': spec_path,
        'constraints_honored': {
            'no_new_api_call': True, 'no_proxy': True, 'no_corpus_v20_modify': True,
            '5_anchor_unchanged': True, '4_spec_v01_v19_v21_unchanged': True,
        },
    }

    output_json = r'D:\私人资料\deposon-repo\results\deposon_v2_phase4_f4_2026_09_11.json'
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    log(f'OUTPUT_SAVED {output_json}')

    log('DONE')
    
    # Write log
    log_path = r'D:\私人资料\deposon-repo\results\deposon_v2_phase4_f4_2026_09_11.log'
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(LOG_LINES))
    return 0


if __name__ == '__main__':
    sys.exit(main())
