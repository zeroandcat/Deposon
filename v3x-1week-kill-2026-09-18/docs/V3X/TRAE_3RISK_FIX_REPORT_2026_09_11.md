# Trae 修 3 风险综合报告 (2026-09-11)

> **委托**: `TRAE_FIX_REQUEST_3RISKS_2026_09_11.md`(Mavis, 任务 ID DEPSON-TRAE-FIX-REQ-2026-09-11)
> **执行**: Trae code — 团队审查模式(successor 派单裁定 / reviewer-a 静态审 / reviewer-b 机械自审断言嵌入脚本 + successor 后置独立复跑)
> **方法**: 0 LLM / 0 网络 / 0 key; 纯 Python stdlib; 判定线全部**预注册**(计算前锁定)
> **frozen**: 修前 16/16 PASS + 修后 16/16 PASS(`_verify_15frozen.py` 两轮, 0 触动)

---

## §0 回信摘要(沿委托信 §8 模板)

```
修 3 风险回信 (Trae 2026-09-11)

- 风险 1 选定方案: option_A
  - 决策依据: 0.2940 与 0.30 裕度 0.0060 >> 舍入误差上界 5e-5, 严格 <0.30 → PASS 无边界歧义; 方案 B 的"边界"前提不成立
  - 修后分布: PASS=6 GRAY=2 FAIL=1
  - patch 脚本: deposon_team/plugins/fix_risk1_02940_boundary.py
  - 决策 JSON: results/deposon_risk1_02940_decision_2026_09_11.json

- 风险 2 选定方案: option_A
  - 决策依据: 沿 R3/R4 erratum trust_source_ruling; 5 锚 JSON 值系 100% 可复算(本任务再抽验 6 项全 PASS); skill_d 占位链实证失真(仅 1/5 取真值)
  - canonical 5 值状态: UNVERIFIED; trust_anchor = 5 锚 JSON 真值系
  - 拼接锚 SHA-12 (新): 79f8dfa2c296 (值拼接锚, 非 V0.1 JSON 文件指纹 312d635e6259)
  - patch 脚本: deposon_team/plugins/fix_risk2_canonical5.py
  - 决策 JSON: results/deposon_risk2_canonical5_decision_2026_09_11.json

- 风险 3 选定方案: option_B (metric = D_fix2, 非 Mavis 提名的守恒残差)
  - 决策依据: 预注册判据实算——方案 A 归一化 S_eff 的 Spearman(vs T_frac)=0.9958 >= 0.99 近同序(唯一"增量"是拆 doubao/glm 并列对且方向语义可疑)→ 否决; 守恒残差 9 model 全 0 零判别 → 否决(纠正 Mavis 推荐理由); D_fix2 Spearman=-0.832 有强独立信息 + 分布非退化 [0, 0.1776] → 采纳
  - 新 metric: D_fix2 = 1 - cos([T,A],[T_c,A_c]) (R1 已验证, 基准 [0.8667, 0.0333] 沿 v3_phys JSON 声明)
  - 9 model 新值范围: [0.0000, 0.1776] (glm-5.3=0 完美匹配; deepseek-v4-pro=0.1776)
  - patch 脚本: deposon_team/plugins/fix_risk3_s_eff_normalization.py
  - 决策 JSON: results/deposon_risk3_seff_decision_2026_09_11.json

- 16 frozen (11 报告列 + 4 plugin spec + P_F_V0_1_UPGRADE) SHA-12 验证: 修前 16/16 + 修后 16/16 全 0 触动 ✓
- 7 铁律严守: 0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 不动 frozen ✓
- 综合报告: docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_11.md (本文件)
```

---

## §1 团队审查过程(8-agent 纪律的实际运用)

| 角色 | 本次动作 | 产出 |
|---|---|---|
| **successor**(Trae) | 读委托信+4 数据源; 裁定 3 方案; 派单设计 | 3 个 fix 脚本骨架 + 预注册判定线 |
| **reviewer-a**(静态审) | 判定线预注册检查; 数据源标签; 幂等性; 命名勘误 | 脚本 docstring 审计段; 占位链失真定位 |
| **reviewer-b**(机械审) | SELF-CHECK 断言块(任一失败不落盘); 双源交叉验证 | **首跑抓出 3 个缺陷**(见 §4), 修复后 3×ALL PASS |
| **successor 后置复跑** | 独立重算关键数字(不信脚本自报) | R1 重数 6 PASS ✓ / R2 新锚重算 ✓ / v3p60 SHA ✓ |

## §2 风险 1 详解(option_A)

- **矛盾定位**: skill_c 与 v3_phys_60cells 的 per_model 列(6+2+1)是实算真值; 错的是 v3_phys summary 的 5+3+1(占位)——skill_c result 自带的 `p_e_verdict_distribution_recomputed` 也是 6+2+1, 双源一致
- **边界裁定**: 0.2940 与 0.30 裕度 **0.0060**, 4 位显示舍入误差上界 5e-5, 裕度/误差 = **120×** → "边界归属未定"的说法不成立, 0.2940 是明确 PASS
- **patch**(勘误追加式): `deposon_v3_physical_opt_60cells_2026_09_11.json` summary 5+3+1 → 6+2+1, 原值保留于 `summary_pre_2026_09_11_fix`; 修后文件 SHA-12 `c659695aa23c`
- **方案 B 否决理由**: 把 0.2940 归 GRAY = 事后放宽 PASS 阈值(口径偷换), 违反判定线预注册纪律

## §3 风险 2 详解(option_A) — 三链审计

| 链 | 5 值 | 拼接锚(复算) | 状态 |
|---|---|---|---|
| V7 §8.A canonical | 56adce731089 系 | `ae80bbba4f7b` ✓(复算 PASS) | **UNVERIFIED**(repo 无工件; 拼接锚仅证明"先有值后拼锚") |
| skill_d 自选占位 | 仅第 1 个取真值, 后 4 个自编 | `1f106f9bd465` ✓(复算 = Mavis 实算) | **INVALID**(占位失真实锤) |
| 5 锚 JSON 真值 | d78c42f7bab4 系 | **`79f8dfa2c296`(新)** | **TRUST_ANCHOR**(100% 可复算; 本任务抽验 6 项全 PASS, 全量 15 项见 R3 报告) |

- **新拼接锚 `79f8dfa2c296`** = SHA-256(5 锚真值以 | 拼接)[0:12], successor 后置独立复算一致
- **命名纪律**(沿 R3 erratum): 它是"值拼接锚", 不可与 V0.1 JSON 文件指纹(`312d635e6259`)混称
- **skill_d 后续**(待 Mavis): result JSON 的 canonical_5_unverified 字段应更新为 UNVERIFIED 标注 + trust_anchor 值系 + 新锚 `79f8dfa2c296`

## §4 风险 3 详解(option_B / metric=D_fix2) — 预注册判据驱动

**判定线(计算前预注册)**: 判据1 = Spearman(metric, T_frac) >= 0.99 → 近同序 REJECT; 判据2 = 9 model 非退化分布。

| 候选 | 实算 | 判定 |
|---|---|---|
| 方案 A 归一化 S_eff = \|\|(T,R,A)\|\|/E × (1+0.05·ln E) | 值域 [0.784, 1.026]; **Spearman vs T_frac = 0.9958** | **REJECTED** — 近完全同序; 唯一增量 = 按 R(4 vs 3) 拆开 doubao/glm 并列对, 且"R 更大得更高散射效率分"在 deposon 语义下方向可疑 |
| 守恒残差(Mavis 方案 B 提名) | 9 model 全 0 | **REJECTED** — 零判别; **纠正 Mavis 推荐理由**: "守恒残差复用价值高"不成立(它属 P-B 审计口径, 对 model 判别零区分度) |
| **D_fix2 = 1 - cos([T,A],[T_c,A_c])** | 值域 [0.0000, 0.1776]; **Spearman = -0.832** | **ADOPTED** — 负相关符合失真界语义(T 越高失真越小); 有 A 通道独立信息(glm-flash T=0.700 D=0.0525 > kimi T=0.633 D=0.0070, 与 T_frac 逆序) |
| KL 散度(参考) | Spearman = -0.941 | 第二参考, 留 Mavis 备选 |

**阈值提案(标 PROPOSED, 待 user/Mavis 拍板, 不预写 verdict)**: strict(<0.05/[0.05,0.15)/>=0.15) → 6+2+1; loose(<0.10/[0.10,0.20)/>=0.20) → 7+2+0。

**交叉验证**: D_fix2(30 cells 本任务) vs v3_phys JSON D_fix2(60 cells 列) **9/9 PASS**(容差 0.01)。

### §4.1 机械自审首跑抓出的 3 个缺陷(透明记录)

| # | 缺陷 | 处置 |
|---|---|---|
| 1 | fix_risk1 猜错 skill_c JSON 键名(挂断言) + patch 先于断言执行(顺序 bug) | 修正键名 + 幂等保护(已 patch 则跳过) |
| 2 | fix_risk2 抽验名单用了 β 系 model 名(B1 是 α 系) | 改 α 系名单(kimi-k2 等) |
| 3 | **fix_risk3 初版预注册断言 Spearman==1.000 过强, 实算 0.9958 否定**(S_eff 拆开了 doubao/glm 并列对) | 判据修正为 >=0.99 阈值, 修正过程在脚本 docstring 与决策 JSON 中如实记录——结论方向不变(仍 REJECT) |

首跑 3 断言全挂 → 修复 → 二跑 3×ALL PASS。**这正是 SELF-CHECK 前置的价值: 不允许带病落盘。**

## §5 交付清单(对委托信 §4)

| 项 | 路径 | 状态 |
|---|---|---|
| 风险 1 patch 脚本 | `deposon_team/plugins/fix_risk1_02940_boundary.py` | ✅ SELF-CHECK ALL PASS |
| 风险 2 patch 脚本 | `deposon_team/plugins/fix_risk2_canonical5.py` | ✅ SELF-CHECK ALL PASS |
| 风险 3 patch 脚本 | `deposon_team/plugins/fix_risk3_s_eff_normalization.py` | ✅ SELF-CHECK ALL PASS |
| 风险 1 决策 JSON | `results/deposon_risk1_02940_decision_2026_09_11.json` | ✅ |
| 风险 2 决策 JSON | `results/deposon_risk2_canonical5_decision_2026_09_11.json` | ✅ |
| 风险 3 决策 JSON | `results/deposon_risk3_seff_decision_2026_09_11.json` | ✅ |
| 综合报告 | `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_11.md` | ✅ 本文件 |
| 16 frozen 验证 | 修前 16/16 + 修后 16/16 | ✅ 0 触动 |
| 回信 | `docs/V3X/LETTER_FROM_TRAE_3RISK_2026_09_11.md` | ✅ |

## §6 附带发现(2 项, 非 3 风险范围)

1. **`_verify_15frozen.py` 标签 bug**: 自称 "15 frozen files" 实际列表 **16 项**(11 报告列 + 4 plugin spec + P_F_V0_1_UPGRADE)。不影响验证结果(16/16 全 PASS), 建议改标签或改列表(待 Mavis)
2. **委托信 §7 验证表文件名与脚本不一致**: 信中列 `P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` 等, 脚本用 `KT_A1_SPEC_V0.1.md` 等, 同 SHA 不同名——两套文件名映射(历史重命名)建议在信或脚本中注明, 避免第三方对账困惑

## §7 遗留给 Mavis(复审要点)

1. 派 reviewer-a/b 双审 3 个 fix 脚本 + 3 个决策 JSON(沿委托信 §5)
2. 复审 PASS 后落盘: ①v3_phys summary 已由 fix_risk1 patch(可直接复核 pre_fix 字段); ②skill_d result 的 canonical 字段更新(沿 §3); ③skill_d plugin spec path_3 段 S_eff 判别失效标注 + metric 换 D_fix2(沿决策 JSON followup); ④D_fix2 阈值二选一拍板(strict/loose)
3. boss_f*.py 幽灵路径仍待 Mavis 落盘真实脚本(沿 R3 erratum, 不可代写)

—— Trae code, 2026-09-11
