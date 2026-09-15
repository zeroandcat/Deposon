# KT-B1 200/类 × 3 类 = 600 总攻击(完整版, 2026-09-09)

> **作者**: Mavis(root session, V1 折中补 8-10 天 Phase B)
> **位置**: `docs/V3X/KT_B1_FULL_ATTACK_200_2026_09_09_mavis.md`

## 1. 一句话结果

**PASS** (整体攻击者成功率 0.0%)

## 2. 关键数字

| 攻击类型 | 检测 / 总数 | 攻击者成功率 |
|---|---|---|
| deletion | 200/200 | 0.0% |
| manifest_swap | 200/200 | 0.0% |
| chain_modify | 200/200 | 0.0% |

- 总检测: 600/600
- 总攻击者成功率: 0.0%
- 50% 阈值判死: PASS

## 3. 升级版 audit 逻辑

attacker 每次改副本 (用 random.seed(i) 保证可复现), 然后:
- 整体 diff vs original → 检测破坏
- dict swap 兜底: 顶层无 list 字段时, swap 2 个 dict 字段 value
- chain_modify 兜底: 改 dict 字段 value (随机加 _attacked 后缀)

## 4. 已知边界

- 整体 diff 不区分"破坏 T+R+A"和"无关字段改动"
- 真实"改后重算"需 DeposonMechanism 暴露 compute_residual 接口
- Phase B 完整版 = 改后调用 DeposonMechanism 算新 T+R+A, 与 2.2e-16 对比
