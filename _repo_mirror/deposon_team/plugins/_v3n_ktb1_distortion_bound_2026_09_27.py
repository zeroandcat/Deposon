# -*- coding: utf-8 -*-
"""
_v3n_ktb1_distortion_bound_2026_09_27.py
=========================================
V3-N #21 KT-B1 BOSS-B1/B2/B3 失真上界真测 (Trae 回函 §1.2 #21「不明」的补齐)

来源件 (先核后用, 逐件登记):
- docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md
    §三 表: B1 Sinkhorn OT 失真上界 0.0004 / deposon 0.5(占位) -> GRAY_BOTH_BELOW
            B2 KD 0.0028 / 0.5(占位) -> GRAY_BOTH_BELOW
            B3 LLMLingua 0.4634 / 0.05(占位) -> GRAY_BOTH_ABOVE
    §六.2 遗留事项 2 字面(本条真测的**唯一仓内可算测法锚**):
            「如需真正判定差异化, **需从 v19 守恒残差(2.22e-16)反向估计 deposon 失真上界**」
- docs/V3X/KT_B1_SPEC_V0.1.md
    §1.1 内部判死线: 失真上界 >= 0.95 (即失真度 <= 0.05); 失真上界 = 1 - 保真度
    §4.1/§4.2/§4.3 BOSS-B1/B2/B3 测法字面 + 真实脚本 SHA (脚本本仓已缺失, 见下)
- verifier/audit/conservation.py  (v19 守恒残差检测器, 只读引用)
- results/deposon_v19_benchmark_fixes.json  (v19 1592 条)

**诚实交代 (3 项仓内实测事实)**:
1. BOSS-B1/B2/B3 真实脚本(anchor SHA 19325960b8be / 1781ea2f742d / c0b55e0385a4)在**本仓不存在**;
   `.mavis/scripts/kt_b1/` 现仅存 fix_safe_float.py。
2. P-B V0 spec §7 列的 5 锚之一 `tools/distortion_calculator.py`(D1 由 data 实现)**本仓不存在**;
   tools/ 下仅 exp_harness.py / llm_client.py / make_figures_v2*.py / read_key.py。
3. 故原始 D(M,T)=E_pi[sum_t |u*(a_t)-u(a_t)|/max_u] 失真度**无法在仓内复算**(u*/u/max_u
   无实现载体)。本件执行 KT_B1_REWORK §六.2 写明的 fallback 测法(从 v19 守恒残差反向估计),
   这是仓内唯一有字面依据的真测路径; 0 新设阈值。

判定: 沿 KT-B1 原判据字面 —— 失真上界 vs 0.95 内部判死线 + GRAY_BOTH_BELOW/ABOVE 相对判读。
      0 新设阈值。

铁律: 0 LLM / 0 proxy / 0 网关 / 0 key 读 / 既有件 0 触动 (只写新 JSON)
作者: Mavis 团队 worker | 2026-09-27
"""
from __future__ import annotations

import io
import json
import math
import os
import sys
from datetime import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

REPO = r"D:\私人资料\deposon-repo"
V19 = os.path.join(REPO, "results", "deposon_v19_benchmark_fixes.json")
OUT_JSON = os.path.join(REPO, "results", "_v3_n_ktb1_distortion_bound_data_2026_09_27.json")

# === KT-B1 原判据常量 (逐字取自源件, 0 新设) ===
INTERNAL_KILL_LINE = 0.95   # KT_B1_SPEC_V0.1 §1.1/§2.5: 失真上界 >= 0.95 达标
# §六.2 记的占位值 (被本件实测值替换)
PLACEHOLDER = {"B1_Sinkhorn_OT": 0.5, "B2_KD": 0.5, "B3_LLMLingua": 0.05}
# §三 表记的通用基线失真上界(原脚本缺失, 只能沿报告值引用, 不可复算)
GENERIC_BOUND = {"B1_Sinkhorn_OT": 0.0004, "B2_KD": 0.0028, "B3_LLMLingua": 0.4634}
ORIG_VERDICT = {"B1_Sinkhorn_OT": "GRAY_BOTH_BELOW", "B2_KD": "GRAY_BOTH_BELOW",
                "B3_LLMLingua": "GRAY_BOTH_ABOVE"}


def main() -> int:
    t0 = datetime.now().isoformat(timespec="seconds")
    sys.path.insert(0, os.path.join(REPO, "verifier", "audit"))
    import conservation as C  # noqa: E402

    v19 = json.load(open(V19, encoding="utf-8"))
    stored_pa = v19["physics_audit"]
    graded = C.check_conservation_graded(v19, v19)

    # === 真测: 从 v19 守恒残差反向估计 deposon 失真上界 (KT_B1_REWORK §六.2 字面) ===
    measured_bound = graded["max_deviation"]
    is_machine_eps = measured_bound == float.fromhex("0x1.0p-52")

    out = {
        "task": "V3-N #21 KT-B1 BOSS-B1/B2/B3 失真上界真测 (补齐 Trae 回函 §1.2 #21「不明」)",
        "date": "2026-09-27",
        "author": "Mavis 团队 worker",
        "started": t0,
        "method": "KT_B1_REWORK_2026_09_10 §六.2 字面: 从 v19 守恒残差反向估计 deposon 失真上界",
        "input_chain": {},
        "missing_assets_registered": [],
        "measured_deposon_distortion_bound": {
            "value": measured_bound,
            "hex": float(measured_bound).hex(),
            "equals_ieee754_double_eps_2^-52": bool(is_machine_eps),
            "derivation": "conservation.check_conservation_graded(v19, v19).max_deviation "
                          "= max(layer1_deviation, layer2_max_deviation)",
            "n_records_checked": graded["n_records_checked"],
            "conservation_graded_verdict": graded["verdict"],
            "layer1_deviation": graded["layer1_deviation"],
            "layer2_max_deviation": graded["layer2_max_deviation"],
            "stored_physics_audit": stored_pa,
            "stored_vs_recomputed_match": bool(
                stored_pa["t_plus_r_plus_a_max_deviation"] == measured_bound),
        },
        "criteria_literal": {
            "internal_kill_line": f"失真上界 >= {INTERNAL_KILL_LINE} (KT_B1_SPEC_V0.1 §1.1)",
            "new_thresholds_introduced": 0,
        },
        "boss_rejudgment": {},
        "discriminating_power_audit": {},
    }

    for k, v in {
        "v19": "results/deposon_v19_benchmark_fixes.json",
        "conservation_py": "verifier/audit/conservation.py",
        "kt_b1_spec": "docs/V3X/KT_B1_SPEC_V0.1.md",
        "kt_b1_rework": "docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md",
        "p_b_spec": "docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md",
    }.items():
        p = os.path.join(REPO, v.replace("/", os.sep))
        out["input_chain"][k] = {"path": v, "exists": os.path.exists(p),
                                 "bytes": os.path.getsize(p) if os.path.exists(p) else None}

    # 仓内缺失件(逐件登记, 老实交代)
    for rel, why, anchor in [
        (".mavis/scripts/kt_b1/boss_b1_sinkhorn_ot.py", "BOSS-B1 真实脚本本仓缺失", "19325960b8be"),
        (".mavis/scripts/kt_b1/boss_b2_kd.py", "BOSS-B2 真实脚本本仓缺失", "1781ea2f742d"),
        (".mavis/scripts/kt_b1/boss_b3_llmlingua.py", "BOSS-B3 真实脚本本仓缺失", "c0b55e0385a4"),
        ("tools/distortion_calculator.py", "P-B V0 §7 五锚之一 (D1 由 data 实现) 本仓缺失", "n/a"),
    ]:
        p = os.path.join(REPO, rel.replace("/", os.sep))
        out["missing_assets_registered"].append({
            "path": rel, "exists": os.path.exists(p), "anchor_sha12": anchor, "why": why,
        })

    # === GRAY_BOTH_ABOVE/BELOW 语义识别 ===
    # 两种候选读法, 用原报告 §三 表的 3 行原始标签做**自识别**(不择一冒充):
    #   读法 A: ABOVE/BELOW = 两者相对 0.95 内部判死线的位置
    #   读法 B: ABOVE/BELOW = 通用基线值相对 **deposon 值** 的高低
    # 哪个读法能复现原报告 3 行全部标签, 就是原脚本实际采用的语义。
    def label_under_mapping(name, deposon_value):
        g = GENERIC_BOUND[name]
        below_g = g < INTERNAL_KILL_LINE
        below_d = deposon_value < INTERNAL_KILL_LINE
        A = "GRAY_BOTH_BELOW" if (below_g and below_d) else (
            "PASS_BOTH_ABOVE" if (not below_g and not below_d) else "SPLIT")
        B = ("GRAY_BOTH_ABOVE" if g > deposon_value else "GRAY_BOTH_BELOW") \
            if g < INTERNAL_KILL_LINE else "FAIL"
        return A, B

    ident = {}
    for tag, idx in (("A_both_vs_kill_line", 0), ("B_both_vs_deposon", 1)):
        ok = 0
        for name in GENERIC_BOUND:
            ph = PLACEHOLDER[name]
            got = label_under_mapping(name, ph)[idx]
            if got == ORIG_VERDICT[name]:
                ok += 1
        ident[tag] = {"reproduces_original_labels": f"{ok}/3", "identified": ok == 3}
    identified = [k for k, val in ident.items() if val["identified"]]
    out["gray_label_semantics_identification"] = {
        "method": "用原报告 §三 表 3 行的 (通用基线, deposon 占位, 原标签) 三元组做自识别",
        "candidates": ident,
        "identified_mapping": identified[0] if len(identified) == 1 else None,
        "unique": len(identified) == 1,
        "conclusion": ("唯一读法 B 被识别: ABOVE/BELOW 指**通用基线值相对 deposon 值**的高低"
                       if identified == ["B_both_vs_deposon"] else
                       f"未唯一识别 (候选: {identified})"),
    }
    sem = out["gray_label_semantics_identification"]["identified_mapping"] or "B_both_vs_deposon"

    # === 按识别出的语义重判 ===
    for name, generic in GENERIC_BOUND.items():
        ph = PLACEHOLDER[name]
        below_line_g = generic < INTERNAL_KILL_LINE
        below_line_d = measured_bound < INTERNAL_KILL_LINE
        label_A, label_B = label_under_mapping(name, measured_bound)
        out["boss_rejudgment"][name] = {
            "generic_bound_from_report": generic,
            "generic_bound_recomputable": False,
            "deposon_placeholder": ph,
            "deposon_measured": measured_bound,
            "deposon_replaced": True,
            "vs_internal_kill_line": {
                "generic_below_0.95": below_line_g, "deposon_below_0.95": below_line_d,
                "deposon_verdict": "FAIL (失真上界 << 0.95)" if below_line_d else "PASS",
            },
            "verdict_under_identified_mapping": label_B if sem == "B_both_vs_deposon" else label_A,
            "verdict_mapping_A_both_vs_kill_line": label_A,
            "verdict_mapping_B_both_vs_deposon": label_B,
            "original_verdict_in_report": ORIG_VERDICT[name],
            "flipped_vs_original": (label_B if sem == "B_both_vs_deposon" else label_A)
                                   != ORIG_VERDICT[name],
        }

    # === 鉴别力审计(诚实的根因: 测法轴退化) ===
    out["discriminating_power_audit"] = {
        "measured_bound_is_ieee754_eps": bool(is_machine_eps),
        "structural_identity": "T=(1-eta)v, R=eta*g_couple*(1-v), A=1-T-R → T+R+A ≡ 1 为构造恒等; "
                               "conservation.py 层2 由 pred 合成验和, 对 v19 无显式 T/R/A 字段者"
                               "「合成恒守恒」(源件 L13 自述)",
        "consequence": "残差 2.22e-16 = 2^-52 双精度舍入极限, 不含任何关于 deposon 相对"
                       "Bayesian 基线信息失真的证据 → 该测法轴无鉴别力",
        "verdict_on_evidence_quality": "占位 0.5 已被**实测值**替换(占位问题解除), "
                                       "但 BOSS-B1/B2/B3 仍**未被真正受审**(测法轴问题未解除)",
        "parallel_to_trae_item_5": "与 Trae 回函 §1.2 #5「540 cells 守恒 STRICT_CONSERVATION = "
                                   "结构性恒等, 不构成实验证据」为同一根因",
    }
    out["outcome"] = {
        "status": "COMPLETED_WITH_LIMITATION",
        "placeholder_replaced": True,
        "general_baseline_truly_audited": False,
        "item_21_recommendation": "仍标「不明」, 但根因从「占位值未真测」收敛为"
                                  "「测法轴结构性恒等 → 真测也无法受审」",
    }
    out["finished"] = datetime.now().isoformat(timespec="seconds")

    print("=" * 74)
    print("V3-N #21 KT-B1 失真上界真测 (0 LLM, 0 proxy, 0 key)")
    print("=" * 74)
    print("测法锚: KT_B1_REWORK §六.2「从 v19 守恒残差反向估计 deposon 失真上界」")
    m = out["measured_deposon_distortion_bound"]
    print(f"实测 deposon 失真上界 = {m['value']!r}  ({m['hex']}, n={m['n_records_checked']})")
    print(f"  = 2^-52 (IEEE 754 双精度 epsilon): {m['equals_ieee754_double_eps_2^-52']}")
    print(f"  stored vs recomputed 一致: {m['stored_vs_recomputed_match']}")
    print()
    print(f"占位值替换: B1/B2 0.5 → {measured_bound!r};  B3 0.05 → {measured_bound!r}")
    ident = out["gray_label_semantics_identification"]
    print(f"GRAY 标签语义自识别: {ident['conclusion']}")
    print(f"  读法A 复现 {ident['candidates']['A_both_vs_kill_line']['reproduces_original_labels']}, "
          f"读法B 复现 {ident['candidates']['B_both_vs_deposon']['reproduces_original_labels']}")
    print()
    print(f"{'BOSS':<16}{'通用基线':>10}{'deposon实测':>16}{'识别语义重判':>20}{'原报告':>20}")
    for name, r in out["boss_rejudgment"].items():
        print(f"{name:<16}{r['generic_bound_from_report']:>10}"
              f"{r['deposon_measured']:>16.3e}"
              f"{r['verdict_under_identified_mapping']:>20}"
              f"{r['original_verdict_in_report']:>20}"
              + ("   <-- FLIP" if r["flipped_vs_original"] else ""))
    print()
    print(f"鉴别力审计: 残差 = 构造恒等的舍入极限 → 测法轴无鉴别力")
    print(f"  占位问题已解除; BOSS-B1/B2/B3 仍非真正受审")
    print()
    print("仓内缺失件:")
    for m2 in out["missing_assets_registered"]:
        print(f"  - {m2['path']}  exists={m2['exists']}  anchor={m2['anchor_sha12']}")
    json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"OUT: {OUT_JSON}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
