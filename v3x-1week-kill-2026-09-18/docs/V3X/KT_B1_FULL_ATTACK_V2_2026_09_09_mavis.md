# KT-B1 50/类 × 3 类 = 150 总攻击(升级版 audit, 2026-09-09)

## 1. 升级版 audit(整体 diff vs 原数据)

| 攻击类型 | 无差异 / 总数 | 攻击者成功率 |
|---|---|---|
| deletion | 50/50 | 0.0% |
| manifest_swap | 50/50 | 0.0% |
| chain_modify | 50/50 | 0.0% |

- 总无差异: 150/150
- 总攻击者成功率: 0.0%
- 50% 阈值判死: PASS

## 2. 升级版 vs 简化版对比

- 简化版 check_conservation (Phase A): 0/150 检出, 100% 攻击者成功率
- 升级版 check_conservation (Phase B 起步): 通过整体 diff 检测(改后数据与原数据有差异 → 报警)

## 3. 仍存在的限制

- 整体 diff 不区分"破坏 T+R+A"和"无关字段改动"
- 真实"改后重算 T+R+A"需 DeposonMechanism 暴露 compute_residual 接口(Phase B 完整版)
