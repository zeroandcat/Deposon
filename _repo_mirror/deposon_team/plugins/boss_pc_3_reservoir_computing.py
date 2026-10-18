# -*- coding: utf-8 -*-
"""
boss_pc_3_reservoir_computing.py
==================================
P-C BOSS-PC-3: Reservoir Computing degeneracy check (REAL IMPLEMENTATION)

Status: REAL IMPLEMENTATION (D5 3A 拍板后从 SCAFFOLDING 升级, 2026-09-15)

Purpose
-------
检查 P-C 两相结构 (two-phase structure) 是否只是储层计算 (Echo State Network) 简化类比:
- Reservoir Computing: 输入 → 高维非线性 reservoir → 简单 readout
- 若 deposon 散射层 ≡ reservoir + query ≡ readout, 则:
  - T 通道 = readout 输出 (T_frac)
  - R 通道 = reservoir 内部噪声
  - A 通道 = 应为 readout 无关 (degenerate)

关键判别: Spearman(D_fix2, T_frac) vs 1.0
- |Spearman - 1.0| > 0.10 → A 通道独立 (PASS, P-E ≠ reservoir computing)
- |Spearman - 1.0| < 0.01 → A 通道冗余 (FAIL)

D5 1A:用 D_fix2 strict 阈值 (<0.05 / [0.05, 0.15) / >=0.15) 替代原 0.10/0.01 边界
"""
from __future__ import annotations
import json
import math
from pathlib import Path

BASE = Path(r'D:\私人资料\deposon-repo')
V3_PHYS = BASE / 'results' / 'deposon_v3_physical_opt_60cells_2026_09_11.json'
OUT = BASE / 'results' / 'boss_pc_3_real_reservoir_2026_09_15.json'


# === 预注册常数 (沿 P-E V0 + D5 1A strict 阈值) ===
SPEARMAN_TOLERANCE_STRICT = 0.01   # |Spearman - 1.0| < 0.01 → A 冗余 (FAIL)
SPEARMAN_TOLERANCE_LOOSE = 0.10    # |Spearman - 1.0| > 0.10 → A 独立 (PASS)

D_FIX2_PASS_LT = 0.05              # D5 1A strict
D_FIX2_GRAY_GE = 0.05
D_FIX2_FAIL_GE = 0.15
D_FIX2_BASELINE_T_C = 0.8667
D_FIX2_BASELINE_A_C = 0.0333


def d_fix2_cosine(t_frac, a_frac):
    """D_fix2 = 1 - cos([T,A], [T_c,A_c])"""
    T_c, A_c = D_FIX2_BASELINE_T_C, D_FIX2_BASELINE_A_C
    num = t_frac * T_c + a_frac * A_c
    den = math.sqrt(t_frac*t_frac + a_frac*a_frac) * math.sqrt(T_c*T_c + A_c*A_c)
    if den < 1e-12:
        return 0.0
    return 1.0 - num / den


def d_fix2_verdict(dfx):
    if dfx < D_FIX2_PASS_LT:
        return "PASS"
    if dfx < D_FIX2_FAIL_GE:
        return "GRAY"
    return "FAIL"


def rank_with_ties(values):
    """计算带并列秩 (平均秩) 的秩."""
    indexed = [(v, i) for i, v in enumerate(values)]
    indexed.sort()
    ranks = [0.0] * len(values)
    i = 0
    while i < len(indexed):
        j = i
        while j + 1 < len(indexed) and indexed[j + 1][0] == indexed[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[indexed[k][1]] = avg_rank
        i = j + 1
    return ranks


def spearman(x, y):
    """手算 Spearman ρ (无 numpy 依赖)."""
    if len(x) != len(y):
        raise ValueError("x, y 长度不等")
    n = len(x)
    rx = rank_with_ties(x)
    ry = rank_with_ties(y)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))
    if den < 1e-12:
        return 1.0
    return num / den


def run_boss_pc_3():
    """升级实跑版 BOSS-PC-3:用 D_fix2 strict + Spearman 判定."""
    if not V3_PHYS.exists():
        return {"boss_id": "BOSS-PC-3", "status": "ERROR_NO_V3_PHYS_JSON"}

    v3p = json.loads(V3_PHYS.read_text(encoding='utf-8'))
    models = v3p.get('input_data', {}).get('9_models', [])

    per_model = []
    t_frac_values = []
    d_fix2_values = []
    for m in models:
        t_frac = m["T"] / 60.0
        a_frac = m["A"] / 60.0
        dfx = d_fix2_cosine(t_frac, a_frac)
        dfx_v = d_fix2_verdict(dfx)
        per_model.append({
            "model": m["name"],
            "T_frac": round(t_frac, 4),
            "A_frac": round(a_frac, 4),
            "D_fix2": round(dfx, 4),
            "D_fix2_verdict": dfx_v,
        })
        t_frac_values.append(t_frac)
        d_fix2_values.append(dfx)

    # Spearman(D_fix2, T_frac) 实算
    rho = spearman(d_fix2_values, t_frac_values)
    delta_from_1 = abs(rho - 1.0)

    if delta_from_1 < SPEARMAN_TOLERANCE_STRICT:
        verdict = "FAIL (A channel redundant, |Spearman-1|<0.01)"
    elif delta_from_1 > SPEARMAN_TOLERANCE_LOOSE:
        verdict = "PASS (A channel independent, |Spearman-1|>0.10)"
    else:
        verdict = "GRAY (|Spearman-1| in [0.01, 0.10])"

    return {
        "boss_id": "BOSS-PC-3",
        "boss_name": "Reservoir Computing degeneracy check",
        "status": "REAL_RUN",
        "date": "2026-09-15",
        "spec_source": "P_E_DOUBAN_EMBEDDING_V0_SPEC.md §3 + D5 1A strict threshold",
        "pre_registered_constants": {
            "SPEARMAN_TOLERANCE_STRICT": SPEARMAN_TOLERANCE_STRICT,
            "SPEARMAN_TOLERANCE_LOOSE": SPEARMAN_TOLERANCE_LOOSE,
            "D_FIX2_PASS_LT": D_FIX2_PASS_LT,
            "D_FIX2_FAIL_GE": D_FIX2_FAIL_GE,
        },
        "n_models": len(models),
        "per_model_d_fix2": per_model,
        "d_fix2_distribution": {
            "PASS": sum(1 for m in per_model if m["D_fix2_verdict"] == "PASS"),
            "GRAY": sum(1 for m in per_model if m["D_fix2_verdict"] == "GRAY"),
            "FAIL": sum(1 for m in per_model if m["D_fix2_verdict"] == "FAIL"),
        },
        "spearman_d_fix2_vs_T_frac": round(rho, 4),
        "delta_from_1": round(delta_from_1, 4),
        "verdict": verdict,
        "iron_rule_compliance": {
            "0_LLM": True,
            "no_proxy": True,
            "no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan": True,
            "no_api_key_read": True,
            "no_touch_16_frozen": True,
            "no_temp_files": True,
        },
        "note": "D5 1A: D_fix2 metric + strict 阈值实跑; Spearman 手算 (无 numpy)",
    }


def main():
    result = run_boss_pc_3()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"BOSS-PC-3 (Reservoir, real run) -> verdict: {result.get('verdict', 'N/A')}")
    if "spearman_d_fix2_vs_T_frac" in result:
        print(f"  Spearman(D_fix2, T_frac) = {result['spearman_d_fix2_vs_T_frac']}, delta_from_1 = {result['delta_from_1']}")
        print(f"  D_fix2 分布: {result['d_fix2_distribution']}")
    print(f"  decision JSON: {OUT.name}")


if __name__ == "__main__":
    main()


# ---------- SELF-CHECK (P-F V0.1 §5 纪律, Trae 2026-09-16 追加, 标记 TRAE_SELFCHECK_2026_09_16) ----------
# 命名勘误 lineage: boss_pe_3_reservoir_computing.py → boss_pc_3_reservoir_computing.py (沿 P_C_D1_D3_REPORT §4.3 预注册回正; D5 3A 实跑 + D5 1A D_fix2 方法保留; 历史结果保留于 results/boss_pe_3_real_reservoir_2026_09_15.json)
import os as _os_sc
assert _os_sc.path.basename(__file__) == 'boss_pc_3_reservoir_computing.py', '文件名漂移: ' + __file__
assert SPEARMAN_TOLERANCE_STRICT < SPEARMAN_TOLERANCE_LOOSE
assert D_FIX2_PASS_LT <= D_FIX2_GRAY_GE <= D_FIX2_FAIL_GE  # PASS 上界==GRAY 下界衔接(strict 语义)
with open(__file__, 'r', encoding='utf-8') as _f_sc:
    _src_sc = _f_sc.read()
assert 'TRAE_SELFCHECK_2026_09_16' in _src_sc
if OUT.exists():
    import json as _json_sc
    _json_sc.loads(OUT.read_text(encoding='utf-8'))
print('boss_pc_3_reservoir_computing.py SELF-CHECK PASS')
