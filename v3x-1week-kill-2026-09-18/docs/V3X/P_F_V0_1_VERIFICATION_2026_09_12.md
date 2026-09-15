# R3 验证报告: P-F V0.1 5 锚复算 vs V7 §8.A canonical (2026-09-12)

> **作者**: Trae code (orchestrator/QA)
> **验证对象**: `LETTER_TO_TRAE_2026_09_11.md` §1.3 (R3) + `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json` + V7 §8.A
> **方法**: 0 LLM / 0 网络, 本地 SHA-256 实算(临时脚本, 用后删)

---

## §1 结论摘要

**R3 的真实问题比 Mavis 定性的"算法字符串格式差异"严重得多——是两套完全独立的值链**:

| 项 | V7 §8.A canonical(信中/summary 声明) | 落盘 P_F_PREDECISION V0.1 JSON | Trae 复算 |
|---|---|---|---|
| PF_BOSS_01_fingerprint | `56adce731089` | `d78c42f7bab4` | 落盘值 ✅ **100% 可复算** |
| PF_BOSS_02_tee | `0b4ac1d2df43` | `0ff54f8d2f60` | 落盘值 ✅ 可复算 |
| PF_BOSS_03_merkle | `c4cae1ed9ee5` | `a8f81c98ea8a` | 落盘值 ✅ 可复算 |
| PF_BOSS_04_zkml | `60300c5a0775` | `bff8b1ce1f8c` | 落盘值 ✅ 可复算 |
| PF_BOSS_05_cot | `2ce685e04f4b` | `d9a6a099b905` | 落盘值 ✅ 可复算 |
| "V0.1 JSON 总览 SHA-12" | `ae80bbba4f7b` | (JSON 文件实算 = `7126fb897eb7`) | 见 §3 |

**判定**: Mavis "算法字符串格式差异是预期行为, 下游以 V7 §8.A canonical 为准"的说法**不成立**——canonical 5 值在 repo 内无任何算法工件(无可复算输入串), 而落盘 JSON 值链 100% 可复算。**可信源应反转: 以落盘 V0.1 JSON 为准, canonical 5 值标记"来源未记录"待 P_F_IMPLEMENTATION 子代理补充工件。**

---

## §2 落盘 V0.1 JSON 可复算性验证(全部 PASS)

1. **B1 9 model per-model hash**: `SHA-256(fingerprint_str)[0:12]` 全部 9 个复算一致(如 `doubao-seed-2.0-lite|T_frac=0.8667|T=26|R=2|A=2` → `d059ffbc18f5` ✅)
2. **5 锚 value_v01 拼接规则**: `SHA-256(spec_hash + chain_hash)[0:12]`(字符串直连)全部 5 个复算一致 ✅
3. **B1 chain_hash 链式规则**: `SHA-256(h1|h2|...|h9)[0:12]`(9 个 per-model hash 以 `|` 拼接)复算 = `589e30c3e9c8` ✅
4. 顶层 `5_anchors_v01_true_values` 与内层 `value_v01` 一致 ✅

**不可复算项(2 个, 审计缺陷)**:
- **spec_hash 来源不明**: 5 个 spec_hash(如 B1 `85607bcde97f`)的输入串未记录; JSON 引用的 5 个 BOSS 脚本路径 `.mavis/scripts/p_f/boss_f*.py` **不存在**(目录 `.mavis/scripts/` 下只有 kt_a1/kt_b1/kt_c1)——幽灵路径
- **B2/B4/B5 per_fact_anchors**: 只有 key→hash 输出, 无输入串(事实文本), 无法独立复算

## §3 "总览 SHA-12 ae80bbba4f7b" 实锤

`SHA-256("56adce731089|0b4ac1d2df43|c4cae1ed9ee5|60300c5a0775|2ce685e04f4b")[0:12]` = **`ae80bbba4f7b`** ✅ 复现成功。

即: canonical 的"总览锚"恰是 canonical 5 值 pipe 拼接的 hash——canonical 值系是**先有 5 个(来源未记录的)值, 再拼总览**, 不是从落盘工件推导。同时落盘 V0.1 JSON 文件本身 SHA-12 = `7126fb897eb7` ≠ `ae80bbba4f7b`("V0.1 JSON 总览"名义上应指该文件)。

## §4 修复建议(给 Mavis)

> **状态: ✅ 2026-09-11 已由 Trae 按 user 指令直接执行**(勘误追加制, 见 `LETTER_FROM_TRAE_2026_09_11.md` §七): 第 1 条已执行(V7 MD/JSON 标 UNVERIFIED + 可信源裁定落盘 JSON); 第 3 条已执行(命名勘误); 第 2 条部分执行——JSON 已追加 erratum 记录全部缺口, 但 spec_hash 输入串与 per_fact 事实文本**原件只在 Mavis 侧**, boss_f*.py 幽灵路径待 Mavis 落盘真实脚本(第三方代写=伪造, 不可代修)。

1. **V7 §8.A canonical 5 值**: 追加来源工件(P_F_IMPLEMENTATION 子代理 11:45 的计算脚本/输入串)或显式改用落盘 JSON 值系; 在工件补齐前, V7 §8.A 该 5 行加 `UNVERIFIED` 标注
2. **落盘 V0.1 JSON**: 补记 5 个 spec_hash 的输入串与 B2/B4/B5 per_fact_anchors 的事实文本, 使全部 hash 可独立复算; `.mavis/scripts/p_f/` 幽灵路径修正(落盘脚本或改路径)
3. **overview 锚**: 明确 ae80bbba4f7b = "canonical 5 值拼接锚" 而非 "V0.1 JSON 文件锚"(后者实为 7126fb897eb7), 二者不可混称
4. 本次验证 0 触碰 frozen 文件(V0.1 JSON 与 V7 summary 均只读)

---

## §5 复算环境

- 脚本: `python -B` + hashlib, repo 内 0 新文件(本报告除外)
- 2026-09-11, Trae code
