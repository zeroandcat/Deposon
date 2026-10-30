# Canonical 5 值 UNVERIFIED 标注定(2026-09-11)

> **作者**:Mavis Worker(subagent of mvs_bbeb804b1a6a41109be740636eed1709)
> **触发**:Trae 2026-09-11 §三 R3 修复指示
> **位置**:`docs/V3X/CANONICAL_5_UNVERIFIED_NOTE_2026_09_11.md`
> **关联**:V7 综合报告 §8.A(54ffd2f400d1) + 落盘 JSON `verifier/handoff/P_F_PREDECISION_2026_09_11_V0.1.json`(312d635e6259)

---

## §1 Trae §三 R3 修复说明(可信源反转)

**Trae 2026-09-11 R3 复算**推翻 V7 §8.A 默认"canonical 5 值为 P-F 锚真值"的设定,明确**可信源反转**:

1. **沿用 V7 §8.A canonical 5 值(56adce731089 系)**:
   - `PF_BOSS_01_fingerprint` = `56adce731089`
   - `PF_BOSS_02_tee` = `0b4ac1d2df43`
   - `PF_BOSS_03_merkle` = `c4cae1ed9ee5`
   - `PF_BOSS_04_zkml` = `60300c5a0775`
   - `PF_BOSS_05_cot` = `2ce685e04f4b`
   - 总览:`ae80bbba4f7b` = SHA-256(canonical 5 值以 `|` 拼接)[0:12](**命名勘误** = canonical 5 值拼接锚,非 V0.1 JSON 文件指纹)

2. **沿用 `P_F_PREDECISION_2026_09_11_V0.1.json`(落盘 JSON)**:
   - 5 锚 V0.1 真值 = `d78c42f7bab4` / `0ff54f8d2f60` / `a8f81c98ea8a` / `bff8b1ce1f8c` / `d9a6a099b905`
   - 5 spec hash = `85607bcde97f` / `6768ca7d15ae` / `811c67ca31ff` / `724cd532a2d8` / `c77aaf2f6f99`
   - 5 chain hash = `589e30c3e9c8` / `1b0b88a07dc7` / `5e61566ca583` / `a2e97b4b43a8` / `2c9eac8cb809`
   - 文件 SHA-12 = `312d635e6259`(erratum 追加后)
   - B1 9 model per-model hash 全部复算 PASS(独立 sha256(fingerprint_str)[0:12])

**关键区分**:canonical 5 值(56adce731089 系)与落盘 JSON 值系(d78c42f7bab4 系)是**两套独立值链**,各自有自己的拼接锚。Trae R3 决定**沿用两套并存**,但分别打标。

---

## §2 Canonical 5 值(56adce731089 系)= [UNVERIFIED]

**标 UNVERIFIED 原因**(Trae 2026-09-11 复算确认):

| # | 项 | 实测 |
|---|---|---|
| 1 | canonical 5 值在 repo 内的算法工件 | **无**(V7 §8.A 直接列出,无对应计算脚本) |
| 2 | canonical 5 值拼接锚 `ae80bbba4f7b` | Trae 复算 PASS(SHA-256 拼接正确) |
| 3 | 5 个 spec_hash 的输入字符串 | **未记录**,无法独立复算 spec_hash |
| 4 | 引用路径 `.mavis/scripts/p_f/boss_f*.py` | 仓库 `.mavis/scripts/` 下**无 p_f 目录**(幽灵路径) |
| 5 | P-F canonical = V0.1 锚真值? | **否**(两套独立值链) |

**5 个 [UNVERIFIED] canonical 值**(沿 V7 §8.A):
- `PF_BOSS_01_fingerprint` = `56adce731089` **[UNVERIFIED]** — 落盘 JSON 对应值 `d78c42f7bab4`
- `PF_BOSS_02_tee` = `0b4ac1d2df43` **[UNVERIFIED]** — 落盘 JSON 对应值 `0ff54f8d2f60`
- `PF_BOSS_03_merkle` = `c4cae1ed9ee5` **[UNVERIFIED]** — 落盘 JSON 对应值 `a8f81c98ea8a`
- `PF_BOSS_04_zkml` = `60300c5a0775` **[UNVERIFIED]** — 落盘 JSON 对应值 `bff8b1ce1f8c`
- `PF_BOSS_05_cot` = `2ce685e04f4b` **[UNVERIFIED]** — 落盘 JSON 对应值 `d9a6a099b905`

**结论**:canonical 5 值在工件补齐前一律标 [UNVERIFIED],**不作为** P-F 1 周判死的可信源。

---

## §3 落盘 JSON(312d635e6259 系)= 100% 可复算

**沿 `P_F_PREDECISION_2026_09_11_V0.1.json` 100% 可复算**的项目(Trae R3 verified_pass):

1. **B1 9 model per-model sha256_12 全部独立复算一致** — `sha256(fingerprint_str)[0:12]` 9 条全 PASS
   - 例:`doubao-seed-2.0-lite` fingerprint_str = `doubao-seed-2.0-lite|T_frac=0.8667|T=26|R=2|A=2` → `d059ffbc18f5`
2. **5 锚 value_v01 = SHA-256(spec_hash + chain_hash)[0:12](字符串直连)全部复算一致**
3. **B1 chain_hash = SHA-256(9 个 per-model hash 以 `|` 拼接)[0:12] = `589e30c3e9c8` 复算一致**

**已知不可复算项**(Trae R3 issues,落盘 JSON 5 个):
- 5 个 spec_hash 的**输入字符串**未记录(试算 `'PF_BOSS_01_fingerprint'` / `'P_F_SPEC_V0.md'` / `'boss_f1_model_fingerprinting.py'` 等均不匹配 `85607bcde97f`)
- B2/B4/B5 的 per_fact_anchors 仅含 key→hash 映射,无事实文本输入串
- boss_f*.py 引用路径幽灵(`.mavis/scripts/p_f/` 不存在)

**落盘 JSON 100% 可复算** = Trae 复算 PASS 的部分(spec_hash / chain_hash 拼接链)可作为 P-F 1 周判死的**可信源**(canonical 5 值 UNVERIFIED 之前)。

---

## §4 工件待补(canonical 计算脚本落盘或 5 值标 fallback)

**待补工件**(Mavis 不可代写,任何第三方代写 = 伪造):

| # | 待补工件 | 位置 | 性质 |
|---|---|---|---|
| 1 | `boss_f1_model_fingerprinting.py` 真实脚本 | `.mavis/scripts/p_f/` | 计算 spec_hash `85607bcde97f` 的输入 |
| 2 | `boss_f2_tee_sgx.py` 真实脚本 | `.mavis/scripts/p_f/` | 计算 spec_hash `6768ca7d15ae` 的输入 |
| 3 | `boss_f3_merkle_inference_log.py` 真实脚本 | `.mavis/scripts/p_f/` | 计算 spec_hash `811c67ca31ff` 的输入 |
| 4 | `boss_f4_zkml.py` 真实脚本 | `.mavis/scripts/p_f/` | 计算 spec_hash `724cd532a2d8` 的输入 |
| 5 | `boss_f5_cot_transparency.py` 真实脚本 | `.mavis/scripts/p_f/` | 计算 spec_hash `c77aaf2f6f99` 的输入 |

**或 fallback 选项**:5 个 canonical 值改用落盘 JSON 5 个 value_v01 替代(标 `FALLBACK_TO_V0.1`),但这会**改变 V7 §8.A 的措辞**,需 user 批准。

---

## §5 Mavis 不擅自补(7 铁律严守 scripts/ 不动)

**7 铁律"不创建 boss_f*.py 真实脚本" = Mavis 严守**:

- 任何代写 boss_f*.py 都会构成**伪造**(Trae R3 已明确)
- Mavis 仅负责**报告层**(canonical 5 值标 UNVERIFIED + 落盘 JSON 100% 可复算 = 两套并存)
- 落盘 JSON 已沿 V7 + V0.1 升级,**不动**(SHA-12 = 312d635e6259 沿用)
- 5 锚 JSON `verifier/handoff/KT_ABC1_anchors_sha256_12.json` SHA-12 = `03c6c01f3697` 沿用未动

**Mavis 当前动作** = 仅 1 标注定文件(本文件,新增)+ 0 脚本创建。

---

## §6 7 铁律严守声明

| # | 铁律 | 本文件状态 |
|---|---|---|
| 1 | 0 LLM 调用 | ✅ 本文件纯文本,0 LLM |
| 2 | 不设 proxy | ✅ 0 网络调用 |
| 3 | 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan | ✅ 0 LLM |
| 4 | key 永不入 prompt / JSON / disk | ✅ 0 key 读取 |
| 5 | 节省原则 | ✅ 0 API 调用 |
| 6 | 不动 5 锚 JSON `03c6c01f3697` | ✅ 实算验证未动 |
| 7 | 不动 4 SPEC V0.1 + v19/v21 + corpus/v20 + 现有 JSON | ✅ 全部 SHA-12 实算沿用 |
| 8 | 不创建 boss_f*.py 真实脚本 | ✅ 0 脚本创建(本文件 §5 严守) |

**5 锚 JSON 总览** SHA-12 实算 = `03c6c01f3697`(完整 SHA-256 = `03c6c01f3697151b32b86c9016434a17c43e2c1f6db89be7641fee778b74e98a`)

**P_F_PREDECISION_2026_09_11_V0.1.json** SHA-12 实算 = `312d635e6259`(沿用,本文件未触动)

---

**VERDICT**:`CANONICAL_5_UNVERIFIED_NOTED` — canonical 5 值(56adce731089 系)在工件补齐前标 [UNVERIFIED];落盘 JSON(312d635e6259 系)5 锚 V0.1 真值 = 100% 可复算可信源;Mavis 不擅自补 boss_f*.py 真实脚本(7 铁律严守 scripts/ 不动)。

**Mavis / Deposon 项目组 / 2026-09-11**
