# KT-B1 50/类 × 3 类 = 150 总攻击(升级版 audit fixed, 2026-09-09)

## 1. 升级版 audit: 整体 diff vs original

| 攻击类型 | 检测 / 总数 | 攻击者成功率 |
|---|---|---|
| deletion | 50/50 | 0.0% |
| manifest_swap | 0/50 | 100.0% |
| chain_modify | 0/50 | 100.0% |

- 总检测: 50/150
- 总攻击者成功率: 66.7%
- 50% 阈值判死: FAIL

## 2. 升级版逻辑

attacker 每次改副本(用 random.seed(i) 保证可复现),然后:
- 整体 diff vs original → 检测破坏
- 简化版 check_conservation(只检查 audit 字段)→ 漏检

## 3. 仍存在的限制

- 整体 diff 不区分"破坏 T+R+A"和"无关字段改动"
- 真实"改后重算 T+R+A"需 DeposonMechanism 暴露 compute_residual 接口
- Phase B 完整版 = 改后调用 DeposonMechanism 算新 T+R+A, 与 2.2e-16 对比
