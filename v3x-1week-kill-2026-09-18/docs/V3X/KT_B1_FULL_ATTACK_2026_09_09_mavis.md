# KT-B1 50/类 × 3 类 = 150 总攻击 (2026-09-09)

> **作者**: Mavis(root session, V1 折中补 8-10 天)
> **位置**: `docs/V3X/KT_B1_FULL_ATTACK_2026_09_09_mavis.md`

## 1. 一句话结果

**FAIL** (整体攻击者成功率 100.0%)

## 2. 关键数字

| 攻击类型 | 检测 / 总数 | 攻击者成功率 |
|---|---|---|
| deletion | 0/50 | 100.0% |
| manifest_swap | 0/50 | 100.0% |
| chain_modify | 0/50 | 100.0% |

- 总检测: 0/150
- 总攻击者成功率: 100.0%
- 50% 阈值判死: FAIL

## 3. 已知边界(诚实声明)

- check_conservation 简化版: 只检查改后 JSON 字段, 没"改后重算 T+R+A" → 攻击者漏检率高
- 真实 200 次/类攻击需"改后重算 deposon 散射层"(Phase B 完整版)
- 完整 200/类 = 600 总攻击留 D3-D4

## 4. 与 7 条铁律的兼容性

- 数据从冻结 JSON 字段路径引
- /tmp 副本可重跑
- 不碰 HANDOFF_MACHINE_READABLE.json
