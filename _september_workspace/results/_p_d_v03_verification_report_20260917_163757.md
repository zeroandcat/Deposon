# P-D V0.3 SPEC 22 caption dual_24bit 实测验证报告 (2026-09-17)

> **执行**: worker (Mavis 派出)
> **方法**: 0 LLM / 0 网络 / 0 pip install, 纯 hashlib + numpy + json
> **口径**: V0.3 spec §2.2 / §2.3 (沿 KIMI 报告 §1 裁定)
> **runner**: 沿 `_p_d_b3_merkle_22caption_runner_2026_09_16.py` 算法, 新写本验证脚本 (本脚本不入仓)
> **结论**: 22 caption dual_24bit 22/22 PASS, b3_merkle_root = `75596bbabdb8`, canonical 锚链 = `c4cae1ed9ee5`, 7 铁律 0 触动

**时间戳**: 20260917_163757
**产物 1**: `results/_p_d_v03_22caption_verification_20260917_163757.json` (13775 B)
**产物 2**: `results/_p_d_v03_verification_report_20260917_163757.md` (本文件)

---

## §1 验证口径 (V0.3 SPEC §2.2 / §2.3)

| 字段 | 算法 | 长度 | 性质 |
|---|---|---|---|
| `byte_hash` | `SHA-256(caption_id)[0:12]` | 12 hex (48 bit) | V0.2 §2 字符串级 |
| `semantic_hash` | 12-bit LSH (SVD-2 × 12 hyperplanes, `np.random.seed(42)`) → 符号位 | 3 hex (12 bit) | V0.2 §3 语义级 |
| `dual_24bit` | `byte_hash[:6] + semantic_hash` | 9 hex (36 bit) | V0.2 组合 (**名 24 实 36**, V0.3 §3.2 N2) |

**B3 sequential chain (V0.3 §2.3)**:

```
state_0     = anchors[0]                                                     = 7d6d3d39fad8
state_i     = SHA-256(f"{state_(i-1)}|{caption_id}|{dual_24bit}")[0:12]    i=1..22
ext_1       = SHA-256(f"{state_22}|anchor|{anchors[1]}")[0:12]            = f6a1e495e9dc
merkle_root = SHA-256(f"{ext_1}|anchor|{anchors[2]}")[0:12]               = 75596bbabdb8
```

**实测 ext_1 = `f6a1e495e9dc` (期望 `f6a1e495e9dc`, match: True)**
**实测 b3_merkle_root = `75596bbabdb8` (期望 `75596bbabdb8`, match: True)**
**独立复走**: rewalk_ok = True

---

## §2 22 caption dual_24bit 全表 (spec 复算 vs KIMI 报告 2026-09-16)

一致率: vs F4 = **22/22**; vs v3phys = **22/22**; vs KIMI 报告 = **22/22**.

| caption_id | byte_hash | semantic_hash | dual_24bit | node_state | vs F4 | vs v3phys | vs KIMI | verdict |
|---|---|---|---|---|---|---|---|---|
| L_algorithm_process | e07ebcfbf9ba | 498 | e07ebc498 | 9619b7c483d9 | ✅ | ✅ | ✅ | PASS |
| L_biological_taxonomy | bff92145e971 | 2dd | bff9212dd | 193639d01938 | ✅ | ✅ | ✅ | PASS |
| L_geography_world | 64ad5fc2c7e0 | 2fd | 64ad5f2fd | 2df95cb5b211 | ✅ | ✅ | ✅ | PASS |
| L_historical_causality | fbfa04f1128c | 2dc | fbfa042dc | 6adad309cb25 | ✅ | ✅ | ✅ | PASS |
| L_physics_concepts | dbe8caaa4bfd | 2fd | dbe8ca2fd | 7f3eaec5b7a7 | ✅ | ✅ | ✅ | PASS |
| L_project_management | 5fe6baab5410 | 2fd | 5fe6ba2fd | 7d1c39ee86bc | ✅ | ✅ | ✅ | PASS |
| S1 | 3696ad59777e | 6d8 | 3696ad6d8 | 37d7dec2ca5c | ✅ | ✅ | ✅ | PASS |
| S1_n35 | 6d92596542c2 | 2fd | 6d92592fd | 4e0db27033f9 | ✅ | ✅ | ✅ | PASS |
| S1_n45 | d22455b290c0 | 6d8 | d224556d8 | 10c19c8be196 | ✅ | ✅ | ✅ | PASS |
| S1_n60 | a71ac717c393 | 2fd | a71ac72fd | ea938cc20d10 | ✅ | ✅ | ✅ | PASS |
| S2 | adfa2b24c2d9 | 6dc | adfa2b6dc | 67bbc142e55e | ✅ | ✅ | ✅ | PASS |
| S2_n20 | 6c76eaea53d5 | 2fd | 6c76ea2fd | 92dca5b512b2 | ✅ | ✅ | ✅ | PASS |
| S2_n35 | 831a5b3a2c65 | 498 | 831a5b498 | a8a37611f547 | ✅ | ✅ | ✅ | PASS |
| S2_n45 | 3174b72cf536 | 2dd | 3174b72dd | ac1a4255a615 | ✅ | ✅ | ✅ | PASS |
| S2_n60 | 2242e1fb732a | 2dd | 2242e12dd | b03c65a94744 | ✅ | ✅ | ✅ | PASS |
| S3 | 44d6a8a73edd | 2dd | 44d6a82dd | 6542ef61cf8b | ✅ | ✅ | ✅ | PASS |
| S4 | b1d3eb8f3293 | 2dd | b1d3eb2dd | 9c56f2df59aa | ✅ | ✅ | ✅ | PASS |
| S5 | 1cdcbd57e7e2 | 2dd | 1cdcbd2dd | 3407263cfa68 | ✅ | ✅ | ✅ | PASS |
| S6 | b12f76a4b782 | 2fd | b12f762fd | 0080db043ca1 | ✅ | ✅ | ✅ | PASS |
| S6_n20 | 803f0b9079ca | 2fd | 803f0b2fd | e20c7a655279 | ✅ | ✅ | ✅ | PASS |
| S6_n35 | 0e89a90afea3 | 2fd | 0e89a92fd | f3a2a0b9eabf | ✅ | ✅ | ✅ | PASS |
| S6_n60 | 6abc0c5ac060 | 2fd | 6abc0c2fd | bff2e2a039cc | ✅ | ✅ | ✅ | PASS |

---

## §3 chain summary

| 项 | 实测 | KIMI 报告 | V0.3 SPEC | match |
|---|---|---|---|---|
| state_22 | `bff2e2a039cc` | `bff2e2a039cc` | (链式末节) | True |
| ext_1 | `f6a1e495e9dc` | `f6a1e495e9dc` | `f6a1e495e9dc` | True |
| b3_merkle_root | `75596bbabdb8` | `75596bbabdb8` | `75596bbabdb8` | True |
| 独立复走 | OK | OK | (沿) | True |
| chain_pass_count | 22/22 | 22/22 | (沿) | True |

---

## §4 5 anchor check

| 锚 ID | 期望 | 实测 | match | 出处 |
|---|---|---|---|---|
| V0.1 主 (anchor0) | `7d6d3d39fad8` | `7d6d3d39fad8` | ✅ | V0 spec R3 根指纹 (5 锚 manifest) |
| PD2 复现 (anchor1) | `f88d855aaf83` | `f88d855aaf83` | ✅ | KIMI 报告 §5 PD2 复现产物 |
| EIS 独立 (anchor2) | `e66e44e63f5a` | `e66e44e63f5a` | ✅ | KIMI 报告 §5 EIS 独立产物 |
| canonical 锚链 (前 12) | `c4cae1ed9ee5` | `c4cae1ed9ee5` | True | SHA-256('7d6d3d39fad8\|f88d855aaf83\|e66e44e63f5a')[0:12] |
| B3 merkle_root (前 12) | `75596bbabdb8` | `75596bbabdb8` | True | V0.3 §2.3 B3 sequential chain |
| 既有 P-D V0.1 链 current_root | `7d6d3d39fad8` | (jsonl 缺失) | ⚠️ N/A | verifier/runs/2026-09-04_pd_v0.jsonl |

**canonical 锚链 全值**: `c4cae1ed9ee543a12bda58e82e3c9c35bd3aa4caef9bc26d3a42c8e60cf366f1`
**期望 全值**: `c4cae1ed9ee543a12bda58e82e3c9c35bd3aa4caef9bc26d3a42c8e60cf366f1`

---

## §5 链序声明 (V0.3 §3.3 N3 文档化)

严守链序 = `corpus/v20/strip_captions_22.json` **文件位置序** (22 caption 按 strip_captions_22.json `id` 字段位置序遍历):

   1. `L_algorithm_process`
   2. `L_biological_taxonomy`
   3. `L_geography_world`
   4. `L_historical_causality`
   5. `L_physics_concepts`
   6. `L_project_management`
   7. `S1`
   8. `S1_n35`
   9. `S1_n45`
  10. `S1_n60`
  11. `S2`
  12. `S2_n20`
  13. `S2_n35`
  14. `S2_n45`
  15. `S2_n60`
  16. `S3`
  17. `S4`
  18. `S5`
  19. `S6`
  20. `S6_n20`
  21. `S6_n35`
  22. `S6_n60`

**B3 sequential chain 是 sequential chain + 2 级 anchor 延伸 (非 RFC6962 二叉 Merkle 树)**:

- 顺序链: `state_i` 依赖 `state_(i-1)`; 22 节顺序唯一, 节点插入顺序决定链结构
- 1 级 anchor 延伸: `ext_1` 锚 `anchors[1]` 延伸
- 2 级 anchor 延伸: `merkle_root` 锚 `anchors[2]` 延伸
- **无 RFC6962 树形结构、无 inclusion proof** (V0.3 §3.3 N2 裁定)

---

## §6 frozen 0 触动证明

| 文件 | 期望 SHA-256 | 实测 SHA-256 | match |
|---|---|---|---|
| `corpus/v20/index.json` (frozen v0) | `8423ffe266afad008aa18744f74892f13bbb7d4d6a193d1ccac206c489c22d1c` | `8423ffe266afad008aa18744f74892f13bbb7d4d6a193d1ccac206c489c22d1c` | True |
| `corpus/v20/index_v2_2026_09_16.json` (KIMI 报告产物) | (任务文案: 8423ffe2... ❌ 笔误) | `efe05ad775de239883c908d6a603754f86cfab578c2543a63b16e5188dc79261` | ❌ 任务文案笔误 |
| `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` (KIMI 报告产物) | (KIMI 完整性) | `b5873afb9d295b14632defddb01f37f82aca3cf3f8dcc4efb1cadaaa40e48530` | (读, 不写) |

**frozen v0 (index.json) 0 触动**: ✅ PASS

**index_v2 SHA 笔误披露** (如实):

> 任务文案声称 `corpus/v20/index_v2_2026_09_16.json` frozen SHA-256 = `8423ffe2...`, 实际 SHA-256 = `efe05ad775de239883c908d6a603754f86cfab578c2543a63b16e5188dc79261`. 经核, `8423ffe2...` 实为 `corpus/v20/index.json` (v0) 的 SHA-256, 与任务文案笔误位置一致. `index_v2` 是 KIMI 报告 2026-09-16 跑出的产物, 非 frozen 文件; KIMI 报告 §8 给出其 `content_sha256 = d367cd37...`. 实测 SHA 与之是否一致需下游审计.

---

## §7 7 铁律 0 触动声明

| 铁律 | 严守声明 | 状态 |
|---|---|---|
| no_llm | 纯 hashlib + numpy + json, 0 LLM 调用 | ✅ |
| no_proxy | 0 网关调用 | ✅ |
| no_gateway | 0 volcengine / doubao / kimi / minimax 等网关调用 | ✅ |
| no_key | 0 API key 引用 | ✅ |
| no_18_frozen_anchor_touch | 18 frozen anchors 全部 0 触动 (含 5 anchors: V0.1 主 + PD2 复现 + EIS 独立 + canonical 锚链 + B3 root) | ✅ |
| no_5_artifact_json_touch | 5 制品 JSON (index.json / strip_captions_22.json / embedding / f4 / v3phys) 仅 `sha256_file()` 只读, 0 写入 | ✅ |
| no_4_plugin_spec_touch | 4 plugin spec (V0/V0.2/V0.3 spec + 22 caption runner) 0 触动 | ✅ |
| no_verifier_mavis_builtin_scripts_touch | verifier/ 当前为空, mavis/ .builtin/ scripts/ 三目录未访问 | ✅ |

---

## §F Blockers / Disclosures (老实披露)

1. **verifier/runs/2026-09-04_pd_v0.jsonl 缺失**: verifier/ 目录当前为空, 无法独立核验 anchor[0] == 既有 P-D V0.1 链 current_root. 沿 V0 spec R1 5 锚 manifest 根指纹 = 7d6d3d39fad8, 本验证仅声明 anchor[0] = 7d6d3d39fad8 与 KIMI 报告 §5 一致, 不复走原 jsonl. (非阻断, 沿 V0 spec 5 锚 manifest 根指纹即可交叉)

2. **任务文案 index_v2 SHA 笔误**: 任务声称 `corpus/v20/index_v2_2026_09_16.json` frozen SHA-256 = `8423ffe2...`, 但 `8423ffe2...` 实为 `corpus/v20/index.json` (v0, frozen) SHA-256. `index_v2` 是 KIMI 报告 2026-09-16 跑出的产物, 非 frozen 文件. 本验证严守不写不动 index_v2 (V0.3 §1.2 '不包含任何对 frozen 文件的触动'), 但 index_v2 实际是否曾被改动需下游审计. (非阻断, index_v2 不在 7 铁律 / V0.3 §1.2 触动清单)

---

## §8 产物路径 + SHA-12

- **JSON**: `results/_p_d_v03_22caption_verification_20260917_163757.json` (13775 B), SHA-12 = `dfbcc5d6fc34`
- **MD**: `results/_p_d_v03_verification_report_20260917_163757.md` (9791 B, 已落)

---

**结论**: 22 caption dual_24bit 22/22 PASS, b3_merkle_root = `75596bbabdb8` (= KIMI 报告 §5 + V0.3 §2.3), canonical 锚链 = `c4cae1ed9ee5`, 7 铁律 0 触动.
