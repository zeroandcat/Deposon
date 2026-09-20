"""
KT-B1 4 档判死裁定函数
========================

按 KT_B1_SPEC_V0 §3.4 + §4.3 判死裁定:
- 4 档: PASS_KT_B1 / GRAY_DOWN / GRAY_UP / FAIL_KT_B1
- 输入: KT-B1 攻击成功率(attacker_success_rate)
- 阈值: 50% (RATE_THRESHOLD)

判死矩阵:
- 攻击者成功率 < 50% → PASS_KT_B1(守恒即检测力, 升级为正面结果)
- 攻击者成功率 >= 50% → FAIL_KT_B1(守恒≠检测力, 退守复合协议分支)
- 攻击者成功率 in [40%, 50%) → GRAY_DOWN(下游检查)
- 攻击者成功率 in [50%, 60%) → GRAY_UP(下游检查)
"""

from __future__ import annotations

# KT_B1 判死阈值(沿用 v3 提案 KT-B1 行)
RATE_THRESHOLD = 0.50
GRAY_DOWN_UPPER = 0.50  # 攻击者成功率 < 50% 进入 GRAY_DOWN
GRAY_UP_LOWER = 0.50    # 攻击者成功率 >= 50% 进入 GRAY_UP
GRAY_UP_UPPER = 0.60    # GRAY_UP 上界


def kill_decision(attacker_success_rate: float) -> str:
    """4 档判死裁定

    Args:
        attacker_success_rate: 攻击者成功率(0-1)

    Returns:
        'PASS_KT_B1' | 'GRAY_DOWN' | 'GRAY_UP' | 'FAIL_KT_B1'
    """
    if attacker_success_rate < 0:
        raise ValueError(f'attacker_success_rate must be >= 0, got {attacker_success_rate}')
    if attacker_success_rate > 1:
        raise ValueError(f'attacker_success_rate must be <= 1, got {attacker_success_rate}')

    if attacker_success_rate < RATE_THRESHOLD:
        if attacker_success_rate >= GRAY_DOWN_UPPER - 0.10:  # [40%, 50%)
            return 'GRAY_DOWN'
        return 'PASS_KT_B1'
    else:  # >= 50%
        if attacker_success_rate < GRAY_UP_UPPER:  # [50%, 60%)
            return 'GRAY_UP'
        return 'FAIL_KT_B1'


def kill_decision_4_field(attacker_success_rate: float) -> dict:
    """详细 4 档判死 + 解释"""
    verdict = kill_decision(attacker_success_rate)
    if verdict == 'PASS_KT_B1':
        explanation = '守恒即检测力 (attacker_success_rate < 50%)'
        downstream = '升级为正面结果归档'
    elif verdict == 'GRAY_DOWN':
        explanation = '下游检查 (attacker_success_rate in [40%, 50%))'
        downstream = '扩 cell 重测'
    elif verdict == 'GRAY_UP':
        explanation = '下游检查 (attacker_success_rate in [50%, 60%))'
        downstream = '扩 cell 重测'
    else:  # FAIL_KT_B1
        explanation = '守恒≠检测力 (attacker_success_rate >= 60%)'
        downstream = '退守复合协议分支'

    return {
        'verdict': verdict,
        'rate': attacker_success_rate,
        'explanation': explanation,
        'downstream_action': downstream
    }


if __name__ == '__main__':
    # 自检: 4 档边界
    for r in [0.0, 0.30, 0.45, 0.50, 0.55, 0.70, 1.0]:
        d = kill_decision_4_field(r)
        print(f'rate={r}: {d["verdict"]} - {d["explanation"]}')
