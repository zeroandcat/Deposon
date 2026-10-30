# P-D B3 Merkle 22 Caption dual_24bit 链式核验报告 (2026-09-16)

> **执行**: 委外执行代理 C (KIMI 派出)
> **方法**: 0 LLM / 0 网络 / 0 pip install, 纯 hashlib + numpy + json 确定性装配
> **runner**: `deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py` (一键复跑产出 1/2)
> **产出 1**: `corpus/v20/index_v2_2026_09_16.json` (24150 B)
> **产出 2**: `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` (18104 B)
> **结论**: 22 条 caption dual_24bit 按 spec 复算与两份既有实测 **22/22 全一致**; 链式连接 3 根 anchors **22/22 PASS**; frozen `corpus/v20/index.json` SHA-256 写入前后不变

---

## §1 口径裁定声明 (spec 优先, KIMI 裁定)

**本核验采用的 dual_24bit 口径** (依据 `docs/V3X/PD_V0.2_SEMANTIC_FINGERPRINT_SPEC.md` §2/§3):

| 字段 | 算法 | 长度 |
|---|---|---|
| `byte_hash` | `SHA-256(caption_id)[0:12]` | 12 hex (48 bit) |
| `semantic_hash` | 12-bit LSH: 22 caption SVD-2 坐标 × 12 随机超平面 (`np.random.seed(42)`), 符号位 → 3 hex | 3 hex (12 bit) |
| `dual_24bit` | `byte_hash[:6] + semantic_hash` | 9 hex (36 bit) |

SVD-2 坐标源: `results/deposon_volcengine_22caption_embedding_2026_09_10.json` (svd2_coords)。

**非标分歧声明**: `deposon_team/plugins/_p_o_stranger_verification_runner_2026_09_16.py` L172-197 的 `verify_22_caption_dual_24bit` 使用 `cap_sha[:6] + cap_sha[6:12]` 纯截段 (对 caption 文本 SHA-256 截 12 hex 再做 6+6 拼接, **无 semantic_hash 语义层**, 且 hash 输入为 caption 文本而非 caption_id), 与 spec 定义不符, **判为非标**。裁定依据: spec 文件为 P-D V0.2 指纹的唯一定义来源 (KIMI 已拍板), 故本报告全部数值以 spec 复算为准。

---

## §2 输入与 frozen 0 触动证明

全部输入只读; `corpus/v20/index.json` 为 frozen, 写入前后各重算一次 SHA-256:

| 时点 | SHA-256 (全值) |
|---|---|
| 写入前 | `8423ffe266afad008aa18744f74892f13bbb7d4d6a193d1ccac206c489c22d1c` |
| 写入后 | `8423ffe266afad008aa18744f74892f13bbb7d4d6a193d1ccac206c489c22d1c` |
| 判定 | **UNCHANGED ✅ (0 触动)** |

输入清单 (全部只读): `corpus/v20/index.json` / `corpus/v20/strip_captions_22.json` / `results/deposon_volcengine_22caption_embedding_2026_09_10.json` / `results/deposon_v2_phase4_f4_2026_09_11.json` / `results/deposon_v3_physical_opt_2026_09_11.json` / `results/deposon_v3_physical_opt_60cells_2026_09_11.json` / `results/deposon_game_theory_eval_2026_09_10.json` / `verifier/runs/2026-09-04_pd_v0.jsonl`。

---

## §3 id 一一对应核验

`corpus/v20/strip_captions_22.json` 的 22 个 `id` 与 `corpus/v20/index.json` 的 22 个 `graph_id`:

- 逐位 (positional) 比对: **22/22 一致 ✅**
- 集合 (set) 比对: **22/22 一致 ✅**
- 数量: graphs = 22, captions = 22; `index.json` 原文件 `captions` 字段整体缺失 (核实属实)

caption 文本 0 LLM 约束处理: **逐字复用** `strip_captions_22.json` 的 `text` 字段, 只做确定性装配, 未生成任何新文本。

---

## §4 22 条 dual_24bit 全量表 (spec 复算 vs 双既有实测)

一致率: vs `deposon_v2_phase4_f4_2026_09_11.json` dual_fingerprints = **22/22**; vs `deposon_v3_physical_opt_2026_09_11.json` P_D_semantic_fingerprint_V0_2.per_caption = **22/22**。复算与既有值逐条相同, 故直接沿用, 无差异表。

| caption_id | byte_hash | semantic_hash | dual_24bit | vs F4 | vs v3phys | 链式 node_state | verdict |
|---|---|---|---|---|---|---|---|
| L_algorithm_process | e07ebcfbf9ba | 498 | e07ebc498 | ✅ | ✅ | 9619b7c483d9 | PASS |
| L_biological_taxonomy | bff92145e971 | 2dd | bff9212dd | ✅ | ✅ | 193639d01938 | PASS |
| L_geography_world | 64ad5fc2c7e0 | 2fd | 64ad5f2fd | ✅ | ✅ | 2df95cb5b211 | PASS |
| L_historical_causality | fbfa04f1128c | 2dc | fbfa042dc | ✅ | ✅ | 6adad309cb25 | PASS |
| L_physics_concepts | dbe8caaa4bfd | 2fd | dbe8ca2fd | ✅ | ✅ | 7f3eaec5b7a7 | PASS |
| L_project_management | 5fe6baab5410 | 2fd | 5fe6ba2fd | ✅ | ✅ | 7d1c39ee86bc | PASS |
| S1 | 3696ad59777e | 6d8 | 3696ad6d8 | ✅ | ✅ | 37d7dec2ca5c | PASS |
| S1_n35 | 6d92596542c2 | 2fd | 6d92592fd | ✅ | ✅ | 4e0db27033f9 | PASS |
| S1_n45 | d22455b290c0 | 6d8 | d224556d8 | ✅ | ✅ | 10c19c8be196 | PASS |
| S1_n60 | a71ac717c393 | 2fd | a71ac72fd | ✅ | ✅ | ea938cc20d10 | PASS |
| S2 | adfa2b24c2d9 | 6dc | adfa2b6dc | ✅ | ✅ | 67bbc142e55e | PASS |
| S2_n20 | 6c76eaea53d5 | 2fd | 6c76ea2fd | ✅ | ✅ | 92dca5b512b2 | PASS |
| S2_n35 | 831a5b3a2c65 | 498 | 831a5b498 | ✅ | ✅ | a8a37611f547 | PASS |
| S2_n45 | 3174b72cf536 | 2dd | 3174b72dd | ✅ | ✅ | ac1a4255a615 | PASS |
| S2_n60 | 2242e1fb732a | 2dd | 2242e12dd | ✅ | ✅ | b03c65a94744 | PASS |
| S3 | 44d6a8a73edd | 2dd | 44d6a82dd | ✅ | ✅ | 6542ef61cf8b | PASS |
| S4 | b1d3eb8f3293 | 2dd | b1d3eb2dd | ✅ | ✅ | 9c56f2df59aa | PASS |
| S5 | 1cdcbd57e7e2 | 2dd | 1cdcbd2dd | ✅ | ✅ | 3407263cfa68 | PASS |
| S6 | b12f76a4b782 | 2fd | b12f762fd | ✅ | ✅ | 0080db043ca1 | PASS |
| S6_n20 | 803f0b9079ca | 2fd | 803f0b2fd | ✅ | ✅ | e20c7a655279 | PASS |
| S6_n35 | 0e89a90afea3 | 2fd | 0e89a92fd | ✅ | ✅ | f3a2a0b9eabf | PASS |
| S6_n60 | 6abc0c5ac060 | 2fd | 6abc0c2fd | ✅ | ✅ | bff2e2a039cc | PASS |

---

## §5 链式核验 (dual_24bit → SHA-256 链 → 3 根 anchors)

**3 根 fingerprint anchors (P-D V0.1)**: `7d6d3d39fad8` / `f88d855aaf83` / `e66e44e63f5a` (出处 `docs/V3X/P_F_V0_1_UPGRADE_2026_09_11.md` §2.3 B3 Merkle)。

**链式约定** (确定性, 任何人可用记录值独立复走):

```
state_0     = anchors[0]
state_i     = SHA-256(f"{state_(i-1)}|{caption_id}|{dual_24bit}")[0:12]   (i = 1..22)
ext_1       = SHA-256(f"{state_22}|anchor|{anchors[1]}")[0:12]
merkle_root = SHA-256(f"{ext_1}|anchor|{anchors[2]}")[0:12]
```

**链式 PASS 证据**:

1. **锚 0 衔接现存链**: `verifier/runs/2026-09-04_pd_v0.jsonl` 记录 `prev_hash=000000000000 → current_root=7d6d3d39fad8`, 与 `anchors[0]` 一致 ✅ (22 条 caption 链自现存链 current_root 延伸)。
2. **首链示例**: `SHA-256("7d6d3d39fad8|L_algorithm_process|e07ebc498")[0:12] = 9619b7c483d9` ✅。
3. **末链示例**: `SHA-256("f3a2a0b9eabf|S6_n60|6abc0c2fd")[0:12] = bff2e2a039cc` = state_22 ✅。
4. **锚延伸**: `ext_1 = f6a1e495e9dc`; **`b3_merkle_root = 75596bbabdb8`**。
5. **独立复走**: runner 仅用记录的 (caption_id, dual_24bit) 序列从 anchors[0] 重走全链, 22 个 node_state + ext_1 + merkle_root 全部吻合 ✅。
6. **逐条 verdict**: 每条 caption 的 PASS 条件 = spec 复算 = F4 = v3phys 三方一致 ∧ 链节复走吻合 → **22/22 PASS**。

**附带交叉确认**: 锚 hash 三件套中的 `SHA-256("7d6d3d39fad8|f88d855aaf83|e66e44e63f5a")` 全值为 `c4cae1ed9ee543a12bda58e82e3c9c35bd3aa4caef9bc26d3a42c8e60cf366f1`, 其前 12 位 **`c4cae1ed9ee5`** 与 P-F V0.1 5 锚 canonical 中 `PF_BOSS_03_merkle` 值逐字符相同 — B3 Merkle 锚的独立复算交叉确认。

---

## §6 双源稳健

### §6.1 主源: 9 model 表 (60 cells, in_bin 主档)

出处 `results/deposon_v3_physical_opt_60cells_2026_09_11.json` decision_lines_36.in_bin_36:

| model | T_frac | cos_sim | eps_sum | P_C verdict | P_E verdict |
|---|---|---|---|---|---|
| doubao-seed-2.0-lite | 0.8667 | 0.9993 | 0.0102 | PASS | PASS |
| glm-5.3 | 0.8667 | 1.0 | 0.0102 | PASS | PASS |
| deepseek-v4-flash | 0.7667 | 0.9988 | 0.1723 | PASS | PASS |
| doubao-seed-evolving | 0.7333 | 0.9986 | 0.2332 | PASS | PASS |
| minimax-m3 | 0.7 | 1.0 | 0.294 | PASS | PASS |
| glm-5.3-flash | 0.7 | 0.9475 | 0.294 | PASS | PASS |
| kimi-k2.7-code | 0.6333 | 0.993 | 0.4157 | PASS | GRAY |
| doubao-seed-2.1-turbo | 0.6 | 0.8922 | 0.4765 | PASS | GRAY |
| deepseek-v4-pro | 0.5333 | 0.8225 | 0.5982 | GRAY | FAIL |

### §6.2 交叉源: 2 model 26-cell v2 0.867 重合

出处 `results/deposon_game_theory_eval_2026_09_10.json` 字段 `5_candidates_evaluation.P-A_equilibrium_stabilization.note`, 逐字引用:

> "doubao-seed-2.0-lite (26/30=0.867) + glm-5.3 (26/30=0.867) form the v2 equilibrium cluster at exact T_frac=0.867. v3 §6 expected \"26-cell models\" — both are 26/30. deepseek-v4-flash (23/30=0.767) is just below. This is a fuzzy equilibrium cluster, not a fixed point (variance 0 in cluster)."

主源 9 model 表中 doubao-seed-2.0-lite 与 glm-5.3 的 T_frac = 0.8667 (26/30), 与交叉源 0.867 重合 — 双源互相印证。

---

## §7 36 档判定线对照 (替代声明)

**替代声明**: α×β=30 档 + δ×γ×ρ=216 档在仓内**无展开定义**; 本核验采用 `results/deposon_v3_physical_opt_60cells_2026_09_11.json` 的 `decision_lines_36` (9 model × 4 T_frac bins = 36 档, 9 in_bin + 27 out_of_bin) 作为落地版。

**判定线阈值** (沿该文件 thresholds):

- `P_C_cosine`: PASS ≥ 0.85 / GRAY [0.70, 0.85) / FAIL < 0.70
- `P_E_eps`: PASS < 0.30 / GRAY [0.30, 0.50) / FAIL ≥ 0.50

**in_bin 判定分布**: P_C = 8 PASS / 1 GRAY / 0 FAIL; P_E = 5 PASS / 3 GRAY / 1 FAIL (逐 model 见 §6.1 表)。P-D 维度沿 v0.2 评级: 22 caption 类内 Hamming < 6 bits/12, 4 档强聚集 (L 2.47 / S1 2.67 / S2 2.80 / S3-S6 0.57 bits), PASS 沿用。

---

## §8 三件套 hash (内容 + 路径 + 锚)

两产出文件各自的 integrity 块 (内容 hash 口径: `integrity.content_sha256` 置空后的全文 SHA-256, 可独立复算):

| 文件 | content_sha256 | path_sha256 | anchor_sha256 |
|---|---|---|---|
| `corpus/v20/index_v2_2026_09_16.json` | `d367cd379a1794c73d5c3c43863f047d0f1be4281fc1586a480ed5a0351d3255` | `ff56f6e78edfbb78767241ca8d645e58e5e4713fc5525c4318ba4d0759eaab80` | `c4cae1ed9ee543a12bda58e82e3c9c35bd3aa4caef9bc26d3a42c8e60cf366f1` |
| `results/deposon_p_d_b3_merkle_22_caption_2026_09_16.json` | `b65b813f65e313f1c9f60a85fea100d9b9736e5c473bb4b5c65946400417b55b` | `05651172716478b5ff0106e86532f4111c048d477aa5287df564f28447ea9c34` | `c4cae1ed9ee543a12bda58e82e3c9c35bd3aa4caef9bc26d3a42c8e60cf366f1` |

- path hash 输入: repo 相对 POSIX 路径字符串
- anchor hash 输入: `7d6d3d39fad8|f88d855aaf83|e66e44e63f5a`
- index_v2 另含 `index_v2_meta.base_index_sha256` = frozen `index.json` 全值 SHA-256 (见 §2)

---

## §9 自查声明

1. **frozen 0 触动**: `corpus/v20/index.json` SHA-256 写入前后重算不变 (§2); 全部既有文件只读。
2. **0 新建越界**: 本次仅新建 4 个文件 — 产出 1/产出 2/本报告/runner, 其余 0 新建 0 修改。
3. **0 LLM**: 产出代码纯 hashlib + numpy + json; caption 文本逐字复用既有素材; 不调网关, 不 pip install。
4. **术语红线**: 8 项禁用字符串词表 (见 runner `FORBIDDEN_TOKENS` 常量, 拼接构造) 对产出 1/产出 2 最终字节终扫 **0 命中**; 本报告同样规避。
5. **复跑**: `python deposon_team/plugins/_p_d_b3_merkle_22caption_runner_2026_09_16.py` 一键重产出 1 与 2, 内置 frozen 复算 / 双源比对 / 独立复走 / 红线终扫断言, 任一不过即非零退出。
