# Trae 修 3 风险 — 需求委托信 (2026-09-11)

> **致**: Trae AI 助手
> **发自**: Mavis (Mavis / Mavis, 沿 P_F_SPEC §5 / V7 §8.A / v3 §6)
> **任务 ID**: DEPSON-TRAE-FIX-REQ-2026-09-11
> **触发**: user 2026-09-11 17:13 选选项 A"解决 3 风险" → 17:23 user "写需求委托 trae 修"
> **紧迫**: 王老师 1 周判死窗口 2026-09-11 → 09-18, D7 终极判死 2026-09-18
> **严守**: 7 铁律 0 触动(0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 5 锚 0 触动 / 11 frozen 0 触动 / 不创建临时文件)
> **配套报告**:
> - `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` (3 风险实算 + 2 方案矛盾)
> - `results/deposon_3risk_v0_fixes_2026_09_11.json` (实算数据)

---

## §0 委托原则 (Trae 必读)

1. **0 LLM 严守**: 本次修 3 风险全程纯 Python stdlib (json + hashlib + math + numpy 已允许用于实算), **0 LLM 调用**, 不调 OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API / coding-plan。
2. **不动 5 锚 JSON**: `verifier/handoff/KT_ABC1_anchors_sha256_12.json` 全文 SHA-12 `03c6c01f3697` 严守 0 触动。
3. **不动 4 SPEC V0.1**: `KT_A1_SPEC_V0.1.md` / `KT_B1_SPEC_V0.1.md` / `KT_C1_SPEC_V0.1.md` / `KT_D0_SPEC_V0.1.md` 0 触动。
4. **不动 v19/v21/corpus_v20**: `results/deposon_v19_*.json` / `deposon_v21_gtformal.json` / `corpus/v20/index.json` 0 触动。
5. **不动 4 个 plugin spec**: `deposon_team/plugins/skill_a_p_a_60cells.py` (9078B `b1463bb24403`) / `skill_b_p_c_alpha_beta.py` (8699B `e5a299f69a22`) / `skill_c_p_e_3modality.py` (8915B `e19e76c5da7e`) / `skill_d_p_f_observer.py` (10981B `f4c68d146141`) 0 触动。
6. **不动现有 PDF/MD** (~70 份 docs/V3X/) + 200+ 已落盘 JSON。
7. **不动 .minimax/agents 下** verifier / mavis / .builtin / scripts/ 目录。
8. **修 3 风险** 在 `D:\私人资料\deposon-repo\deposon_team\plugins\fix_*.py` 新建(用户可选用),或 在 `/tmp/fix_*.py` 临时目录新建(不落盘)→ 修后让 Mavis 复审。
9. **key 永不入 prompt / JSON / 落盘**: 不读 `C:\Users\Administrator\Desktop\AI\新建文本文档.txt`, 如必须读,用 `Path().read_text()` runtime 读。
10. **0 触动声明**: Trae 修完后, 须 verify 11 frozen 文件 SHA-12 全 0 触动 (沿 §7 验证表)。

---

## §1 风险 1: skill_c v3 P_E 0.2940 边界归属

### 1.1 矛盾描述 (Mavis 已实算完整)

skill_c v3 P_E 文件内部存在 2 套 verdict 统计, Mavis 已沿 v3 §6 阈值口径实算, 0.2940 边界归属未定:

| 来源 | PASS | GRAY | FAIL |
|---|---|---|---|
| **per_model 列** (skill_c 实算, 9 model) | 6 | 2 | 1 |
| **v3 phys summary 统计** (v3_phys_json) | 5 | 3 | 1 |

阈值规则 (沿 v3 §6): `< 0.30 PASS / [0.30, 0.50) GRAY / >= 0.50 FAIL`

### 1.2 实算数据 (9 model × 60 cells, 沿 `results/deposon_v3_physical_opt_60cells_2026_09_11.json`)

| model | ε_3modal_sum | 严格 < 0.30 | >= 0.30 含边界 |
|---|---|---|---|
| doubao-seed-2.0-lite | 0.0102 | PASS | PASS |
| glm-5.3 | 0.0102 | PASS | PASS |
| deepseek-v4-flash | 0.1723 | PASS | PASS |
| doubao-seed-evolving | 0.2332 | PASS | PASS |
| **minimax-m3** | **0.2940** | **PASS (边界)** | **GRAY (边界)** |
| **glm-5.3-flash** | **0.2940** | **PASS (边界)** | **GRAY (边界)** |
| kimi-k2.7-code | 0.4157 | GRAY | GRAY |
| doubao-seed-2.1-turbo | 0.4765 | GRAY | GRAY |
| deepseek-v4-pro | 0.5982 | FAIL | FAIL |

### 1.3 2 方案矛盾 (Trae 修时必带方案选其一)

| 方案 | 内容 | 后果 | 触动范围 |
|---|---|---|---|
| **方案 A (推荐)** | 严格 < 0.30 → per_model 6+2+1 正确, **修正 v3 summary 5+3+1 → 6+2+1** | skill_c 沿用, v3 phys summary 修正, 报告统一 | 1 文件: `results/deposon_v3_physical_opt_60cells_2026_09_11.json` 改 summary 字段, 但 5 锚 JSON 0 触动 |
| **方案 B** | 0.2940 边界 GRAY → per_model 改 minimax-m3 / glm-5.3-flash 为 GRAY, 变 5+3+1 | skill_c 改 per_model 列, v3 phys 5+3+1 沿用 | 1 文件: `results/skill_c_p_e_3modality_result_2026_09_11.json` 改 per_model 字段 |

### 1.4 Trae 期望输出 (方案 A 或 B 二选一)

- 在 `deposon_team/plugins/fix_risk1_02940_boundary.py` 写 patch 脚本:
  - 输入: 9 model × 60 cells 实算 JSON (read-only)
  - 选择方案 A 或 B (Trae 自决, 但须在脚本顶部 `# DECISION: option_A` 或 `# DECISION: option_B` 标注)
  - 输出: `results/deposon_risk1_02940_decision_2026_09_11.json` 含:
    - 选定的方案
    - 修后 PASS/GRAY/FAIL 分布
    - 修后每个 model 的 verdict_strict
- 严守: 不改 4 个 plugin spec + 5 锚 JSON + 4 SPEC V0.1

### 1.5 user 决策建议 (供 Trae 参考, 不强制)

- 沿 v3 §6 阈值规则"严格 < 0.30 PASS" → 方案 A
- 沿"边界 GRAY 偏好保守" → 方案 B
- Mavis 推荐方案 A, 因 per_model 列已是实算结果, 6+2+1 正确, summary 5+3+1 是 v3 phys 之前的占位错

---

## §2 风险 2: skill_d canonical 5 值占位与 erratum 不一致

### 2.1 矛盾描述 (Mavis 已实算完整)

| 来源 | 5 值 | 拼接锚 SHA-12 |
|---|---|---|
| **skill_d 自选占位** (本次实算) | 56adce731089 / f7e1b3c40a92 / 2c9d4e7f8156 / ab58d3c0e1f4 / e8f4a1b6c902 | **1f106f9bd465** (实算) |
| **erratum 期望** (V7 §8.A, Trae R4) | (无 V7 §8.A 真实值工件) | **ae80bbba4f7b** |
| **5 锚 JSON 真值** (P_F V0.1, 100% 可复算) | d78c42f7bab4 / 0ff54f8d2f60 / a8f81c98ea8a / bff8b1ce1f8c / d9a6a099b905 | (d78c42f7bab4 系, 100% 可独立复算) |

### 2.2 实算验证 (0 LLM, 纯 SHA-256)

```
canonical 5 值 (skill_d 自选占位):
  1. 56adce731089
  2. f7e1b3c40a92
  3. 2c9d4e7f8156
  4. ab58d3c0e1f4
  5. e8f4a1b6c902
拼接串: 56adce731089|f7e1b3c40a92|2c9d4e7f8156|ab58d3c0e1f4|e8f4a1b6c902
拼接锚 SHA-12 实算: 1f106f9bd465
erratum 期望 (V7 §8.A):  ae80bbba4f7b
实算 == 期望: False
```

### 2.3 2 值链矛盾 (Trae 修时必带方案选其一)

| 值链 | 来源 | 可复算性 | 信任度 |
|---|---|---|---|
| **5 锚 JSON** (d78c42f7bab4 系) | P_F V0.1 JSON (本次实算 + Trae R4 复算 PASS) | 100% (B1 per-model + chain_hash + spec_hash 全部独立可复算) | **真值** |
| **canonical 5 值** (56adce731089 系) | skill_d 自选占位 (V7 §8.A 在 repo 内无算法工件) | 0% (我无 V7 §8.A 真实值, 拼接锚 ≠ erratum 期望) | **UNVERIFIED** |

### 2.4 2 方案矛盾 (Trae 修时必带方案选其一)

| 方案 | 内容 | 后果 | 触动范围 |
|---|---|---|---|
| **方案 A (推荐, 沿 Trae R4 erratum)** | canonical 5 值标 UNVERIFIED, **5 锚 JSON 作真值** | skill_d 输出报告沿 5 锚 JSON 真值, canonical 5 值标"未验证" | 0 文件触动(纯 spec 标注) |
| **方案 B** | user 提供 V7 §8.A canonical 5 真实 SHA-12 字符串, 重算拼接锚 → 比对 erratum | 重算后可能得到不同锚, 但 5 锚 JSON 仍为真值 | 0 文件触动(待 user 提供字符串) |

### 2.5 Trae 期望输出 (方案 A 或 B 二选一)

- 在 `deposon_team/plugins/fix_risk2_canonical5.py` 写 patch 脚本:
  - 方案 A:
    - 输出 `results/deposon_risk2_canonical5_decision_2026_09_11.json` 含:
      - canonical 5 值标 UNVERIFIED
      - 5 锚 JSON 真值系 (d78c42f7bab4 / 0ff54f8d2f60 / a8f81c98ea8a / bff8b1ce1f8c / d9a6a099b905) 作 trust_anchor
      - 拼接锚: 沿 5 锚 JSON 真值, 计算新拼接锚 SHA-12
  - 方案 B:
    - 留 placeholder, 等 user 提供 V7 §8.A 真实字符串
    - 写明"待 user 输入" + 拼接算法 ready
- 严守: 不改 V7 §8.A + 5 锚 JSON + canonical 5 值占位

### 2.6 user 决策建议 (供 Trae 参考, 不强制)

- 方案 A 立即可执行, 沿 5 锚 JSON 真值, 1 周判死窗口无延迟
- 方案 B 等 user 提供 V7 §8.A 真实字符串, 但 1 周判死窗口紧
- Mavis 推荐方案 A, 因 5 锚 JSON 100% 可复算, 1 周内足够

---

## §3 风险 3: S_eff 公式归一化

### 3.1 矛盾描述 (Mavis 已实算完整)

| 公式 / 阈值 | 数值范围 (E=30) | 9/9 全破 1.20? |
|---|---|---|
| **当前公式**: S_eff(E) = \|\|(T,R,A)\|\| * (1 + 0.05*log(E)) | [23.52, 30.78] | **是** (数学必然) |
| **归一化方案**: S_eff(E) = \|\|(T,R,A)\|\|/E * (1 + 0.05*log(E)) | [0.78, 1.03] | 否 (有判别力) |
| 阈值 1.05 (旧) / 1.20 (新) | [0, 1] 区间 | — |

### 3.2 实算数据 (9 model, E=30)

| model | T | R | A | S_eff 当前 | S_eff 归一化 |
|---|---|---|---|---|---|
| doubao-seed-2.0-lite | 26 | 4 | 0 | 30.78 | 1.026 |
| glm-5.3 | 26 | 3 | 1 | 30.65 | 1.022 |
| deepseek-v4-flash | 23 | 5 | 2 | 27.64 | 0.921 |
| doubao-seed-evolving | 22 | 6 | 2 | 26.78 | 0.893 |
| minimax-m3 | 21 | 8 | 1 | 26.32 | 0.877 |
| glm-5.3-flash | 21 | 1 | 8 | 26.32 | 0.877 |
| kimi-k2.7-code | 19 | 8 | 3 | 24.38 | 0.813 |
| doubao-seed-2.1-turbo | 18 | 2 | 10 | 24.21 | 0.807 |
| deepseek-v4-pro | 16 | 2 | 12 | 23.52 | 0.784 |

### 3.3 3 方案矛盾 (Trae 修时必带方案选其一)

| 方案 | 内容 | 后果 | 触动范围 |
|---|---|---|---|
| **方案 A** | 归一化: S_eff(E) = \|\|(T,R,A)\|\|/E * (1 + 0.05*log(E)) → [0, ~1.2] | 9 model S_eff 范围 [0.78, 1.03], 有判别力, 阈值 1.05/1.20 仍适用 (doubao/glm-5.3 破阈值, 其余 7/9 不破) | 重写 v3 §6 S_eff 公式 + 改 4 plugin spec (skill_d 为主) |
| **方案 B (推荐)** | 接受当前公式, S_eff 对 60 cells baseline 无判别力, **需换 metric** | 9/9 全破 1.20 是数学必然, S_eff 不适用判别, 建议换 D_fix2 / 守恒残差 / KL 散度等 | 改 v3 §6 标注 S_eff 不适用 + 4 plugin spec 换 metric |
| **方案 C** | 新公式 (待 user 提) | Trae 提新公式, user 评审 | 改 v3 §6 + 4 plugin spec |

### 3.4 Trae 期望输出 (方案 A / B / C 三选一)

- 在 `deposon_team/plugins/fix_risk3_s_eff_normalization.py` 写 patch 脚本:
  - 输入: 9 model 实算 (T, R, A) 沿 `results/skill_d_p_f_observer_result_2026_09_11.json`
  - 选择方案 A / B / C (Trae 自决, 须在脚本顶部 `# DECISION: option_A/B/C` 标注)
  - 方案 A: 输出新 S_eff 公式 + 9 model 归一化值 + PASS/GRAY/FAIL 分布
  - 方案 B: 输出新 metric (D_fix2 / 守恒残差 / KL 散度 / 其他) + 9 model 新 metric 值 + 阈值建议
  - 方案 C: 输出新公式定义 + 9 model 实算 + 阈值
- 输出: `results/deposon_risk3_seff_decision_2026_09_11.json`
- 严守: 不直接改 4 plugin spec (在 fix_*.py 新建 + 报告里写"待 Mavis 复审后落盘")

### 3.5 user 决策建议 (供 Trae 参考, 不强制)

- 方案 B 最实用: 1 周判死窗口不重写公式, 用现有守恒残差 / KL 散度换 metric, 立即可用
- 方案 A 数学漂亮, 但要重写 v3 §6, 1 周内可能赶不上 D7
- 方案 C 待 user 提公式, 但 1 周窗口紧
- Mavis 推荐方案 B, 因 1 周窗口紧 + 守恒残差是 P-B BOSS 之一, 复用价值高

---

## §4 Trae 修完后期望交付清单

| 项 | 路径 | 状态 |
|---|---|---|
| 修风险 1 patch 脚本 | `deposon_team/plugins/fix_risk1_02940_boundary.py` | 待 Trae 写 |
| 修风险 2 patch 脚本 | `deposon_team/plugins/fix_risk2_canonical5.py` | 待 Trae 写 |
| 修风险 3 patch 脚本 | `deposon_team/plugins/fix_risk3_s_eff_normalization.py` | 待 Trae 写 |
| 修风险 1 决策 JSON | `results/deposon_risk1_02940_decision_2026_09_11.json` | 待 Trae 输出 |
| 修风险 2 决策 JSON | `results/deposon_risk2_canonical5_decision_2026_09_11.json` | 待 Trae 输出 |
| 修风险 3 决策 JSON | `results/deposon_risk3_seff_decision_2026_09_11.json` | 待 Trae 输出 |
| 修后综合报告 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_11.md` | 待 Trae 输出 |
| 11 frozen SHA-12 验证 | (沿 §7 验证表, 全 0 触动) | 待 Trae verify |

---

## §5 Mavis 复审纪律 (修完后)

- 修完后, Mavis 派独立子代理(不调 LLM, 严守 7 铁律)双审:
  - **reviewer-a 静态**: 沿 plugin spec / V0.1 静态检查 3 风险 patch 脚本代码 + 决策 JSON
  - **reviewer-b /tmp 重跑**: 在 /tmp/ 临时目录新建完整 9 model × 60 cells 重跑脚本, 比对 Trae 输出 + Mavis 实算
- 复审 PASS 后, Mavis 落盘决策到 4 plugin spec (仍严守不擅自动, 等 user 拍板)
- 复审 FAIL → 退回 Trae 重修

---

## §6 4 路径 1 周判死时序 (Trae 修完 3 风险后的下游)

| 路径 | agent | 1 周判死时序 | 状态 |
|---|---|---|---|
| P-A deepen | deposon-pa-deepen | D1 (09-12) 启动 → D7 (09-18) 5 锚 PASS/FAIL | 等王老师选挂点 |
| P-C verify | deposon-pc-verify | D3 (09-14) 启动 → D7 (09-18) R^2 + b_CI 终极判死 | 等王老师选挂点 |
| P-E physics | deposon-physics-formula | D3 (09-14) 启动 → D7 (09-18) 9 model × 60 cells 复跑 + 阈值口径统一 | 等王老师选挂点 |
| P-F observer | deposon-pf-observer | D1 (09-12) 启动 → D5 (09-16) 1 model × 5 cells 验证 B1 fingerprinting | 等王老师选挂点 |

**3 风险修完是 4 路径启动的前置条件**, 王老师 1 周判死窗口 2026-09-11 → 09-18, 4 路径必须 D7 前出 5 锚 PASS/FAIL。

---

## §7 11 frozen SHA-12 验证表 (Trae 修后必 verify)

| 文件 | SHA-12 期望 | 0 触动声明 |
|---|---|---|
| `verifier/handoff/KT_ABC1_anchors_sha256_12.json` | `03c6c01f3697` | 全 5 锚 JSON 0 触动 |
| `docs/V3X/P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` | `78b71d404366` | 0 触动 |
| `docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md` | `0410ca0fbdae` | 0 触动 |
| `docs/V3X/P_C_TWO_PHASE_STRUCTURE_V0_SPEC.md` | `59d8f56347d5` | 0 触动 |
| `docs/V3X/P_D_FINGERPRINT_V0_SPEC.md` | `cce8e9a1b00e` | 0 触动 |
| `results/deposon_v19_benchmark_fixes.json` | `910c4333eead` | 0 触动 |
| `results/deposon_v21_gtformal.json` | `9d9ae5001c57` | 0 触动 |
| `corpus/v20/index.json` | `8423ffe266af` | 0 触动 |
| `verifier/handoff/P_F_PREDECISION_2026_09_09.json` (V0 占位) | `b41c98bf90cc` | 0 触动 |
| `docs/V3X/P_F_SPEC_V0.md` (P-F V0) | `de90faf362c5` | 0 触动 |
| `docs/V3X/P_F_RESEARCH_2026_09_09.md` (P-F research) | `98085df7811a` | 0 触动 |

**外加 4 plugin spec SHA-12 验证** (沿 `docs/V3X/RISK3_V0_FIXES_2026_09_11.md` §4 表):
- `deposon_team/plugins/skill_a_p_a_60cells.py` 9078B `b1463bb24403` 0 触动
- `deposon_team/plugins/skill_b_p_c_alpha_beta.py` 8699B `e5a299f69a22` 0 触动
- `deposon_team/plugins/skill_c_p_e_3modality.py` 8915B `e19e76c5da7e` 0 触动
- `deposon_team/plugins/skill_d_p_f_observer.py` 10981B `f4c68d146141` 0 触动

**合计 15 frozen 文件 0 触动** (11 报告列 + 4 plugin spec)。

---

## §8 Trae 修后回信模板

修完后, Trae 须回信以下信息给 Mavis:

```
修 3 风险回信 (Trae 2026-09-11 / 2026-09-12 ...)

- 风险 1 选定方案: option_A / option_B
  - 决策依据: <一行>
  - 修后分布: PASS=X GRAY=Y FAIL=Z
  - patch 脚本路径: deposon_team/plugins/fix_risk1_02940_boundary.py
  - 决策 JSON 路径: results/deposon_risk1_02940_decision_2026_09_11.json

- 风险 2 选定方案: option_A / option_B
  - 决策依据: <一行>
  - canonical 5 值状态: UNVERIFIED / 沿 5 锚 JSON 真值
  - 拼接锚 SHA-12 (新): <12 字符>
  - patch 脚本路径: deposon_team/plugins/fix_risk2_canonical5.py
  - 决策 JSON 路径: results/deposon_risk2_canonical5_decision_2026_09_11.json

- 风险 3 选定方案: option_A / option_B / option_C
  - 决策依据: <一行>
  - 新公式 / 新 metric: <一行>
  - 9 model 新值范围: [min, max]
  - patch 脚本路径: deposon_team/plugins/fix_risk3_s_eff_normalization.py
  - 决策 JSON 路径: results/deposon_risk3_seff_decision_2026_09_11.json

- 11 frozen + 4 plugin spec SHA-12 验证: 全 0 触动 ✓
- 7 铁律严守: 0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 不动 frozen ✓
- 综合报告: docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_11.md
```

---

## §9 总结

- 3 风险实算完整, Mavis 已老实实算 + 报告落盘
- Trae 修 3 风险 = 1 周判死窗口关键路径
- 严守 7 铁律 0 触动 15 frozen 文件
- 修完后 Mavis 复审 → user 拍板 → 4 路径 D1/D3/D5/D7 启动
- 1 周判死窗口: 2026-09-11 → 09-18, D7 (09-18) 5 锚 PASS/FAIL 终极判死

---

**委托信结束** | 严守 7 铁律 0 触动 15 frozen | 0 LLM 0 网关 0 临时文件
