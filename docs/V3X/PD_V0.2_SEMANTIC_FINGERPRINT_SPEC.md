# P-D 语义指纹 V0.2 SPEC (F-4 输出)

> 写入日期: 2026-09-11 11:17:21
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
svd2 = {'L_algorithm_process': [-0.52, 0.61], 'S1': [0.39, -0.21], ...}  # 22 个

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
| L_algorithm_process | `e07ebcfbf9ba` | `498` | `e07ebc498` |
| L_biological_taxonomy | `bff92145e971` | `2dd` | `bff9212dd` |
| L_geography_world | `64ad5fc2c7e0` | `2fd` | `64ad5f2fd` |
| L_historical_causality | `fbfa04f1128c` | `2dc` | `fbfa042dc` |
| L_physics_concepts | `dbe8caaa4bfd` | `2fd` | `dbe8ca2fd` |
| L_project_management | `5fe6baab5410` | `2fd` | `5fe6ba2fd` |
| S1 | `3696ad59777e` | `6d8` | `3696ad6d8` |
| S1_n35 | `6d92596542c2` | `2fd` | `6d92592fd` |
| S1_n45 | `d22455b290c0` | `6d8` | `d224556d8` |
| S1_n60 | `a71ac717c393` | `2fd` | `a71ac72fd` |
| S2 | `adfa2b24c2d9` | `6dc` | `adfa2b6dc` |
| S2_n20 | `6c76eaea53d5` | `2fd` | `6c76ea2fd` |
| S2_n35 | `831a5b3a2c65` | `498` | `831a5b498` |
| S2_n45 | `3174b72cf536` | `2dd` | `3174b72dd` |
| S2_n60 | `2242e1fb732a` | `2dd` | `2242e12dd` |
| S3 | `44d6a8a73edd` | `2dd` | `44d6a82dd` |
| S4 | `b1d3eb8f3293` | `2dd` | `b1d3eb2dd` |
| S5 | `1cdcbd57e7e2` | `2dd` | `1cdcbd2dd` |
| S6 | `b12f76a4b782` | `2fd` | `b12f762fd` |
| S6_n20 | `803f0b9079ca` | `2fd` | `803f0b2fd` |
| S6_n35 | `0e89a90afea3` | `2fd` | `0e89a92fd` |
| S6_n60 | `6abc0c5ac060` | `2fd` | `6abc0c2fd` |


## 5. 类内 Hamming 距离 (semantic_hash 同源聚集度)

| 类别 (family) | 成员数 | semantic_hash intra-Hamming |
|---------------|--------|------------------------------|
| L(llm_dag) | 6 | 2.47 bits / 12 |
| S1(chain) | 4 | 2.67 bits / 12 |
| S2(tree) | 5 | 2.8 bits / 12 |
| S3-S6(misc) | 7 | 0.57 bits / 12 |


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
