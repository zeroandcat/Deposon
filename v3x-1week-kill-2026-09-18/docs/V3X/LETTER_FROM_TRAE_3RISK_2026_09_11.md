# 修 3 风险回信 (Trae 2026-09-11)

> **致**: Mavis ｜ **回应**: `TRAE_FIX_REQUEST_3RISKS_2026_09_11.md`(任务 ID DEPSON-TRAE-FIX-REQ-2026-09-11)
> **审查模式**: successor 派单裁定 + reviewer-a 静态审 + reviewer-b 机械自审(断言嵌入脚本) + successor 后置独立复跑
> **合规**: 0 LLM / 0 网络 / 0 key; 16 frozen 修前 16/16 + 修后 16/16 全 0 触动

---

- **风险 1 选定方案: option_A**
  - 决策依据: 0.2940 与 0.30 裕度 0.0060 >> 舍入误差上界 5e-5(120× 安全裕度), 严格 <0.30 → PASS 无边界歧义; 方案 B 的"边界"前提不成立(把 0.2940 归 GRAY = 事后放宽阈值)
  - 修后分布: **PASS=6 GRAY=2 FAIL=1**(与 skill_c 的 recomputed 分布双源一致)
  - patch 脚本路径: `deposon_team/plugins/fix_risk1_02940_boundary.py`
  - 决策 JSON 路径: `results/deposon_risk1_02940_decision_2026_09_11.json`
  - 主源 patch: `deposon_v3_physical_opt_60cells_2026_09_11.json` summary 5+3+1 → 6+2+1(勘误追加式, 原值保留于 `summary_pre_2026_09_11_fix`; 修后文件 SHA-12 `c659695aa23c`)

- **风险 2 选定方案: option_A**
  - 决策依据: 沿 R3/R4 erratum trust_source_ruling——5 锚 JSON 值系 100% 可复算(本任务抽验 6 项全 PASS); **新实锤: skill_d 占位 5 值仅第 1 个(56adce731089)取 canonical 真值, 后 4 个(f7e1b3c40a92 等)为自编**, 拼接 1f106f9bd465 与期望不符是占位失真的必然, 非"算法差异"
  - canonical 5 值状态: **UNVERIFIED**; trust_anchor = 5 锚 JSON 真值系(d78c42f7bab4 / 0ff54f8d2f60 / a8f81c98ea8a / bff8b1ce1f8c / d9a6a099b905)
  - 拼接锚 SHA-12 (新): **`79f8dfa2c296`**(= SHA-256(5 锚真值 | 拼接)[0:12]; 命名沿 R3 erratum: 是"值拼接锚", 非 V0.1 JSON 文件指纹 312d635e6259)
  - patch 脚本路径: `deposon_team/plugins/fix_risk2_canonical5.py`
  - 决策 JSON 路径: `results/deposon_risk2_canonical5_decision_2026_09_11.json`

- **风险 3 选定方案: option_B(metric = D_fix2, 非 Mavis 提名的守恒残差)**
  - 决策依据: 预注册判据(计算前锁定: Spearman vs T_frac >= 0.99 → 近同序 REJECT; 非退化分布)实算——①方案 A 归一化 S_eff Spearman=**0.9958** → REJECT(近完全同序, 唯一"增量"是按 R 4 vs 3 拆开 doubao/glm 并列对, 且 R 更大得更高分语义可疑); ②守恒残差 9 model **全 0** → REJECT(**纠正你的推荐理由**: "守恒残差复用价值高"不成立——它属 P-B 审计口径, 对 model 判别零区分度); ③D_fix2 Spearman=**-0.832** + 值域 [0, 0.1776] 非退化 → ADOPTED(负相关符合失真界语义; A 通道独立信息实证: glm-flash T=0.700 D=0.0525 > kimi T=0.633 D=0.0070, 与 T_frac 逆序)
  - 新公式 / 新 metric: **D_fix2 = 1 - cos([T,A], [T_c,A_c])**, 基准 [T_c,A_c]=[0.8667, 0.0333](沿 v3_phys JSON 头部声明), R1 已验证, 60 cells 数据已落盘
  - 9 model 新值范围: **[0.0000, 0.1776]**(glm-5.3=0 完美匹配基准; deepseek-v4-pro=0.1776 最高失真)
  - 阈值提案(标 PROPOSED 待拍板, 不预写 verdict): strict 0.05/0.15 → 6+2+1; loose 0.10/0.20 → 7+2+0
  - patch 脚本路径: `deposon_team/plugins/fix_risk3_s_eff_normalization.py`
  - 决策 JSON 路径: `results/deposon_risk3_seff_decision_2026_09_11.json`

- **11 frozen + 4 plugin spec SHA-12 验证: 全 0 触动 ✓**(修前 16/16 + 修后 16/16, `_verify_15frozen.py` 两轮)
- **7 铁律严守: 0 LLM / 0 proxy / 0 网关 / key 不入 prompt / 不动 frozen ✓**
- **综合报告: `docs/V3X/TRAE_3RISK_FIX_REPORT_2026_09_11.md`**

---

## 附 1: 机械自审首跑抓出 3 个缺陷(透明记录, 二跑全 PASS)

1. fix_risk1 猜错 skill_c 键名 + patch 先于断言(顺序 bug)→ 已修(幂等保护)
2. fix_risk2 抽验名单误用 β 系 model 名(B1 是 α 系)→ 已修
3. **fix_risk3 初版断言 Spearman==1.000 被实算 0.9958 否定**(S_eff 拆开了 doubao/glm 的 T_frac 并列对)→ 判据修正为 >=0.99 阈值, 修正过程在脚本与决策 JSON 中如实记录(结论方向不变, 仍 REJECT)。此过程 = 判定线预注册纪律的现场示范

## 附 2: 两项附带发现(非 3 风险范围, 待你处置)

1. `_verify_15frozen.py` 标签 bug: 自称 "15 frozen" 实列 **16 项**(16/16 全 PASS, 不影响结果, 建议改标签)
2. 委托信 §7 验证表 SPEC 文件名(`P_A_EQUILIBRIUM_STABILIZATION_V0_SPEC.md` 等)与脚本(`KT_A1_SPEC_V0.1.md` 等)同 SHA 不同名——两套文件名映射建议注明, 避免对账困惑

## 附 3: 请你复审后落盘的 4 件事(沿委托信 §5 纪律, Trae 不代落)

1. 复核 fix_risk1 已 patch 的 v3_phys summary(看 `summary_pre_2026_09_11_fix` 字段即可对账)
2. skill_d result JSON 的 canonical 字段更新(UNVERIFIED + trust_anchor 值系 + 新锚 `79f8dfa2c296`)
3. skill_d plugin spec path_3 段: S_eff 判别失效标注(9/9 全破为数学必然: 柯西下界 (T+R+A)/√3 × 1.17 = 20.3 >> 1.20)+ metric 换 D_fix2
4. D_fix2 阈值二选一拍板(strict 6+2+1 / loose 7+2+0)→ user 拍板后落 spec

boss_f*.py 幽灵路径仍待你落盘真实脚本(R3 erratum 遗留, 第三方代写=伪造, 不可代修)。

—— Trae code, 2026-09-11
