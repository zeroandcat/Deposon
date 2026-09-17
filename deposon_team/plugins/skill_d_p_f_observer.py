# -*- coding: utf-8 -*-
"""
skill_d_p_f_observer.py
========================
Deposon V3X 路径 ③ + ④ 合并:P-F 1 周判死 observer
  路径 ③:沿物理公式深化 (v3 §6 散射公式 S_eff(E) 投影 9 model × 30 cells 题目到 3 维 T/R/A)
  路径 ④:P-F 1 周判死 observer (2026-09-11 → 2026-09-18)

输入:
  D:\\私人资料\\deposon-repo\\verifier\\handoff\\P_F_PREDECISION_2026_09_11_V0.1.json
  D:\\私人资料\\deposon-repo\\verifier\\handoff\\KT_ABC1_anchors_sha256_12.json
  D:\\私人资料\\deposon-repo\\results\\deposon_v3_physical_opt_60cells_2026_09_11.json

输出:
  1. stdout 打印物理公式 S_eff(E) 投影 + canonical 5 值对比 + 1 周判死综合
  2. JSON 落盘到 results/skill_d_p_f_observer_result_2026_09_11.json

严守 7 铁律: 0 LLM / 0 proxy / 不动 5 锚 / 不动 scripts/ / 不动 verifier

作者: Mavis Worker (subagent of mvs_bbeb804b1a6a41109be740636eed1709)
日期: 2026-09-11
"""

import os
import json
import hashlib
import sys
import datetime

REPO_ROOT = r"D:\私人资料\deposon-repo"
P_F_V01_JSON = os.path.join(REPO_ROOT, "verifier", "handoff", "P_F_PREDECISION_2026_09_11_V0.1.json")
ANCHOR_JSON = os.path.join(REPO_ROOT, "verifier", "handoff", "KT_ABC1_anchors_sha256_12.json")
V3_PHYS_JSON = os.path.join(REPO_ROOT, "results", "deposon_v3_physical_opt_60cells_2026_09_11.json")
OUT_JSON = os.path.join(REPO_ROOT, "results", "skill_d_p_f_observer_result_2026_09_11.json")


def sha12_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# ===== D5 2026-09-15 1A 拍板:path_3 段升级 =====
# 1. S_eff metric 判别失效: 9/9 全破为数学必然(柯西下界 (T+R+A)/sqrt(3)=17.3 →
#    S_eff_cur >= 20.3 故 9/9 全破 1.20 是数学必然,Spearman≈1.000 零信息增量)
#    注释沿 fix_risk3_s_eff_normalization.py 的判定结论
# 2. D_fix2 = 1 - cos([T,A], [T_c,A_c]) 作为 path_3 段新 metric
#    (沿 fix_risk3 option_B_ADOPTED_D_fix2, R1 已验证, Spearman < 0.99)
# 3. strict 阈值(<0.05 / [0.05,0.15) / ≥0.15) 沿 fix_risk3 threshold_proposals
#    strict_0.05_0.15 (Trae 实算分布见 results/deposon_risk3_seff_decision_2026_09_11.json)
S_EFF_DISCRIMINATION_FAILED = (
    "S_eff(E) = ||(T,R,A)|| * (1 + α*log(E)) 判别失效: "
    "9/9 全破阈值 1.20 是数学必然 (柯西下界 (T+R+A)/sqrt(3) = 17.3 → S_eff >= 20.3), "
    "Spearman(S_eff, T_frac) ≈ 1.000 零信息增量。详见 "
    "fix_risk3_s_eff_normalization.py + results/deposon_risk3_seff_decision_2026_09_11.json"
)
S_EFF_THRESH_OLD = 1.05  # 旧 F-3 DELTA 阈值 (已推翻, 仅保留历史)
S_EFF_THRESH_NEW = 1.20  # 旧 S_eff 阈值 (已沿 fix_risk3 标 JUDGMENT_FAILED)

# D_fix2 阈值 (D5 1A 拍板 strict)
D_FIX2_THRESH_PASS_LT = 0.05    # < 0.05 = 高保真 (PASS)
D_FIX2_THRESH_GRAY_GE = 0.05    # [0.05, 0.15) = 偏离 (GRAY)
D_FIX2_THRESH_FAIL_GE = 0.15    # ≥ 0.15 = 显著失真 (FAIL)
D_FIX2_BASELINE_T_C = 0.8667    # glm-5.3 均衡代表
D_FIX2_BASELINE_A_C = 0.0333


def s_eff_projection(model_T, model_R, model_A, energy=1.0):
    """旧 S_eff(E) 投影 (1A 沿 fix_risk3 标 JUDGMENT_FAILED, 仅保留历史回放)"""
    import math
    norm = (model_T ** 2 + model_R ** 2 + model_A ** 2) ** 0.5
    alpha = 0.05
    return round(norm * (1.0 + alpha * math.log(max(energy, 1e-6))), 4)


def d_fix2_cosine(model_T_frac, model_A_frac):
    """D_fix2 = 1 - cos([T,A], [T_c,A_c]) (D5 1A path_3 段新 metric)
       沿 fix_risk3 option_B_ADOPTED_D_fix2:
       num = T*T_c + A*A_c
       den = ||[T,A]|| * ||[T_c,A_c]||
       return 1 - num/den
    """
    T_c, A_c = D_FIX2_BASELINE_T_C, D_FIX2_BASELINE_A_C
    T, A = model_T_frac, model_A_frac
    num = T * T_c + A * A_c
    den_norm = ((T * T + A * A) ** 0.5) * ((T_c * T_c + A_c * A_c) ** 0.5)
    if den_norm < 1e-12:
        return 0.0
    return round(1.0 - num / den_norm, 4)


def d_fix2_verdict(d_fix2_value):
    """D_fix2 strict 阈值: <0.05 PASS / [0.05, 0.15) GRAY / >=0.15 FAIL (D5 1A)"""
    if d_fix2_value < D_FIX2_THRESH_PASS_LT:
        return "PASS"
    if d_fix2_value < D_FIX2_THRESH_FAIL_GE:
        return "GRAY"
    return "FAIL"


def main():
    started = datetime.datetime.now().isoformat(timespec="seconds")

    iron = {
        "0_LLM_calls": True,
        "no_proxy": True,
        "no_OpenRouter_TeamoRouter_V41Flash_GPT6_agent_plan_WeChatAPI": True,
        "no_pip_install": True,
        "no_touch_verifier_mavis_builtin": True,
        "no_touch_scripts_dir": True,
        "no_touch_5anchor_4spec_v19_v21_corpus_v20_200plus_dump": True,
        "method": "纯 Python stdlib (json + hashlib + os + datetime + math), 0 numpy 依赖",
    }

    # ---------- 1. 5 锚 SHA-12 验证 ----------
    anchor_sha12 = sha12_file(ANCHOR_JSON)
    anchor_expected = "03c6c01f3697"
    anchor_pass = (anchor_sha12 == anchor_expected)

    # ---------- 2. P-F V0.1 JSON 加载 ----------
    pf = load_json(P_F_V01_JSON)
    pf_v01 = pf["P_F_PRE_DECISION_V01"]
    pf_metadata = pf["metadata"]
    pf_anchors_v01 = pf_v01["5_anchors_v01_true_values"]
    pf_anchors_v0 = pf_v01["5_anchors_v0_placeholders"]
    pf_boss_keys = pf_v01["5_boss_keys"]
    boss_anchor_v01 = pf["5_boss_anchor_spec_v01"]
    boss_anchor_v0_compat = pf["5_boss_anchor_spec_v0_compat"]
    erratum = pf["erratum_2026_09_11"]

    # ---------- 3. 物理公式路径 ③:D5 1A 拍板 S_eff → D_fix2 + strict 阈值 ----------
    # 沿 fix_risk3_s_eff_normalization.py 的判定:
    #   - S_eff 判别失效 (柯西下界 9/9 全破数学必然, Spearman ≈ 1.000 零信息)
    #   - D_fix2 = 1 - cos([T,A], [T_c,A_c]) 作为新 metric (Spearman < 0.99)
    #   - strict 阈值:<0.05 PASS / [0.05, 0.15) GRAY / ≥0.15 FAIL
    v3 = load_json(V3_PHYS_JSON)
    models = v3["input_data"]["9_models"]
    s_eff_table = []     # 旧 S_eff (D5 1A 后标 JUDGMENT_FAILED, 仅保留回放)
    d_fix2_table = []    # 新 D_fix2 metric (D5 1A 后实际生效)
    breakthrough_count = 0  # 旧 S_eff 1.20 阈值 (数学必然 9/9)
    dfx_pass_count = 0
    dfx_gray_count = 0
    dfx_fail_count = 0
    for m in models:
        # 旧 S_eff 投影 (30 cells + 60 cells, 仅历史回放)
        s_eff_30 = s_eff_projection(m["T"], m["R"], m["A"], energy=30.0)
        s_eff_60 = s_eff_projection(m["T"] * 2, m["R"] * 2, m["A"] * 2, energy=60.0)
        break_old = s_eff_30 > S_EFF_THRESH_OLD
        break_new = s_eff_30 > S_EFF_THRESH_NEW
        if break_new:
            breakthrough_count += 1
        s_eff_table.append({
            "model": m["name"],
            "T": m["T"], "R": m["R"], "A": m["A"],
            "T_frac": m["T_frac"],
            "S_eff_E30": s_eff_30,
            "S_eff_E60": s_eff_60,
            "break_old_1.05": break_old,
            "break_new_1.20": break_new,
            "status": "JUDGMENT_FAILED (D5 1A)",  # D5 拍板后失效标注
        })
        # 新 D_fix2 (30 cells 归一化, 沿 fix_risk3 算法:E=30 cells)
        # 输入 v3 物理 JSON 是 30 cells 数据 (skill_d 主源)
        dfx = d_fix2_cosine(m["T"] / 30.0, m["A"] / 30.0)
        dfx_verdict = d_fix2_verdict(dfx)
        if dfx_verdict == "PASS":
            dfx_pass_count += 1
        elif dfx_verdict == "GRAY":
            dfx_gray_count += 1
        else:
            dfx_fail_count += 1
        d_fix2_table.append({
            "model": m["name"],
            "T_frac": round(m["T"] / 30.0, 4),
            "A_frac": round(m["A"] / 30.0, 4),
            "D_fix2": dfx,
            "strict_verdict": dfx_verdict,
        })
    # 旧 path_3 verdict (S_eff 9/9 全破 → BREAKTHROUGH, 数学必然, 失效)
    old_path_3_verdict = "BREAKTHROUGH" if breakthrough_count >= 5 else "PARTIAL" if breakthrough_count >= 1 else "NOISE"
    # 新 path_3 verdict (D_fix2 strict, 9 model 上分布)
    new_path_3_verdict = "D_FIX2_MIXED" if (dfx_pass_count > 0 and (dfx_gray_count > 0 or dfx_fail_count > 0)) \
        else ("D_FIX2_PASS" if dfx_pass_count >= 9 else ("D_FIX2_FAIL" if dfx_fail_count >= 5 else "D_FIX2_GRAY"))
    path_3_verdict = new_path_3_verdict  # D5 1A 后新 verdict 生效

    # ---------- 4. P-F 1 周判死路径 ④: canonical 5 值 (56adce... 系) vs V0.1 JSON 5 锚真值 ----------
    # canonical 5 值 (沿 V7 §8.A, UNVERIFIED 标记, 详见 erratum)
    # V0.1 JSON 5 锚真值 (d78c42f7bab4 系, 100% 可复算)
    canonical_5 = [
        "56adce731089",  # 占位 (V7 §8.A 提及, repo 内无算法工件, 标 UNVERIFIED)
        "f7e1b3c40a92",
        "2c9d4e7f8156",
        "ab58d3c0e1f4",
        "e8f4a1b6c902",
    ]
    canonical_5_unverified_note = "V7 §8.A canonical 5 值在 repo 内无算法工件, 沿 erratum 标 UNVERIFIED; 真实可信源以 V0.1 JSON 值系 (d78c42f7bab4 系) 为准 (100% 可复算)"

    # canonical 5 值拼接锚 (沿 erratum 实算)
    canonical_5_concat_anchor = hashlib.sha256("|".join(canonical_5).encode("utf-8")).hexdigest()[:12]
    canonical_5_concat_expected = "ae80bbba4f7b"
    canonical_concat_match = (canonical_5_concat_anchor == canonical_5_concat_expected)

    # 5 BOSS V0.1 vs V0 对比
    boss_v0_to_v01_compare = []
    for key in pf_boss_keys:
        b_v01 = boss_anchor_v01[key]
        b_v0 = boss_anchor_v0_compat[key]
        boss_v0_to_v01_compare.append({
            "key": key,
            "value_v0": b_v0["value"][:20] + "...",
            "value_v01": b_v01["value_v01"],
            "verdict_v01": b_v01.get("verdict_v01", "N/A"),
        })

    # 1 周判死 (2026-09-11 → 2026-09-18) 状态
    today = datetime.date(2026, 9, 11)
    deadline = datetime.date(2026, 9, 18)
    days_remaining = (deadline - today).days
    one_week_status = {
        "start_date": "2026-09-11",
        "end_date": "2026-09-18",
        "days_remaining": days_remaining,
        "milestones": [
            "D1 (2026-09-12): 9 model 实际 API 抽样 (1 model × 5 cells 验证 B1 fingerprinting)",
            "D3 (2026-09-14): B3 Merkle P-D V0.1 3 根指纹 + 22 caption dual_24bit 链式核验",
            "D5 (2026-09-16): canonical 5 值工件补齐决策 (是否落盘 boss_f*.py 真实脚本)",
            "D7 (2026-09-18): 5 锚 PASS/FAIL 终极判死, 推 D0 末群内 + 王老师 WeChat",
        ],
        "current_phase": "V0.1 已落盘, 等 D1 启动",
    }

    # ---------- 5. 综合 verdict ----------
    overall_verdict = "OBSERVED" if path_3_verdict in ("BREAKTHROUGH", "PARTIAL") else "GRAY"
    if not anchor_pass:
        overall_verdict = "FAIL"
    if not canonical_concat_match:
        # 不强制失败 (canonical 5 拼接锚期望值在 erratum 中给出)
        overall_verdict += "+CANONICAL_CONCAT_DIVERGENT"

    # ---------- 6. 组装 result ----------
    result = {
        "skill": "skill_d_p_f_observer",
        "phase": "V3X 路径 ③ + ④:P-F 1 周判死 observer (D5 1A 拍板后 path_3 段 D_fix2 升级)",
        "date": "2026-09-15",
        "d5_decision": "1A:D_fix2 metric + strict 阈值 (<0.05 / [0.05,0.15) / >=0.15)",
        "started_at": started,
        "iron_rule_compliance": iron,
        "inputs": {
            "p_f_v01_json": os.path.relpath(P_F_V01_JSON, REPO_ROOT),
            "p_f_v01_json_size_B": os.path.getsize(P_F_V01_JSON),
            "anchor_json": os.path.relpath(ANCHOR_JSON, REPO_ROOT),
            "anchor_json_sha12_observed": anchor_sha12,
            "anchor_json_sha12_expected": anchor_expected,
            "anchor_pass": anchor_pass,
            "v3_phys_json": os.path.relpath(V3_PHYS_JSON, REPO_ROOT),
            "v3_phys_json_size_B": os.path.getsize(V3_PHYS_JSON),
        },
        "path_3_physical_formula": {
            "d5_2026_09_15_1A_pan": "S_eff 失效标注 + D_fix2 metric + strict 阈值",
            "old_s_eff_status": S_EFF_DISCRIMINATION_FAILED,
            "old_s_eff_table_judgment_failed": s_eff_table,
            "old_s_eff_breakthrough_count_9of9_mathematical_necessary": breakthrough_count,
            "old_path_3_verdict_s_eff_only": old_path_3_verdict,
            "new_metric_d_fix2": {
                "formula": "D_fix2 = 1 - cos([T,A], [T_c,A_c])",
                "baseline": [D_FIX2_BASELINE_T_C, D_FIX2_BASELINE_A_C],
                "thresholds_strict": {
                    "PASS_lt": D_FIX2_THRESH_PASS_LT,
                    "GRAY_ge": D_FIX2_THRESH_GRAY_GE,
                    "FAIL_ge": D_FIX2_THRESH_FAIL_GE,
                },
                "source_decision": "fix_risk3_s_eff_normalization.py option_B_ADOPTED_D_fix2 + threshold_proposals.strict_0.05_0.15",
                "per_model": d_fix2_table,
                "distribution": {
                    "PASS": dfx_pass_count,
                    "GRAY": dfx_gray_count,
                    "FAIL": dfx_fail_count,
                },
                "verdict": path_3_verdict,
            },
        },
        "path_4_pf_one_week_judge": {
            "canonical_5_unverified": canonical_5,
            "canonical_5_unverified_note": canonical_5_unverified_note,
            "canonical_5_concat_anchor_observed": canonical_5_concat_anchor,
            "canonical_5_concat_anchor_expected": canonical_5_concat_expected,
            "canonical_concat_match": canonical_concat_match,
            "v01_json_5_anchors_true_values": pf_anchors_v01,
            "v0_json_5_anchors_placeholders": pf_anchors_v0,
            "5_boss_v0_to_v01_compare": boss_v0_to_v01_compare,
            "one_week_status": one_week_status,
            "erratum_summary": {
                "verified_pass": erratum["verified_pass"],
                "issues": erratum["issues"],
                "trust_source_ruling": erratum["trust_source_ruling"],
            },
        },
        "verdict": overall_verdict,
    }

    # ---------- 7. stdout 打印 ----------
    print("=" * 72)
    print("skill_d_p_f_observer | V3X 路径 ③ + ④  P-F 1 周判死 observer (D5 1A 升级版)")
    print("=" * 72)
    print(f"5 锚 SHA-12 实算  : {anchor_sha12}  (期望 {anchor_expected}) -> {'PASS' if anchor_pass else 'FAIL'}")
    print(f"D5 1A 拍板: S_eff 失效(D5) → D_fix2 metric + strict 阈值")
    print(f"路径 ③ 物理公式 (D5 1A 后):")
    print(f"  [旧 S_eff 失效:JUDGMENT_FAILED 9/9 全破为数学必然]")
    print(f"  [新 D_fix2 = 1 - cos([T,A],[T_c,A_c]), strict 阈值 <0.05 / [0.05,0.15) / >=0.15]")
    print(f"  [D_fix2 实算 9 model:]")
    for r in d_fix2_table:
        print(f"    {r['model']:<24s}  T_frac={r['T_frac']:.4f}  A_frac={r['A_frac']:.4f}  D_fix2={r['D_fix2']:.4f}  strict_verdict={r['strict_verdict']}")
    print(f"  D_fix2 分布: PASS={dfx_pass_count}  GRAY={dfx_gray_count}  FAIL={dfx_fail_count}  -> verdict = {path_3_verdict}")
    print(f"路径 ④ P-F 1 周判死 (canonical 5 值 vs V0.1 JSON 5 锚真值):")
    print(f"  canonical 5 值 (UNVERIFIED)   = {canonical_5}")
    print(f"  canonical 拼接锚实算            = {canonical_5_concat_anchor}  (期望 {canonical_5_concat_expected})  match={canonical_concat_match}")
    print(f"  V0.1 JSON 5 锚真值 (可复算)     = {pf_anchors_v01}")
    print(f"  V0 JSON 5 锚占位                = {pf_anchors_v0}")
    print(f"  1 周判死 D1..D7 milestone:")
    for ms in one_week_status["milestones"]:
        print(f"    - {ms}")
    print(f"  今日 {today} -> 截止 {deadline} (剩 {days_remaining} 天)")
    print(f"erratum trust_source_ruling: {erratum['trust_source_ruling']}")
    print(f"综合 verdict: {overall_verdict}")
    print("=" * 72)

    # ---------- 8. JSON 落盘 ----------
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"已落盘: {os.path.relpath(OUT_JSON, REPO_ROOT)}  ({os.path.getsize(OUT_JSON)} B)")
    return 0 if "FAIL" not in overall_verdict else 1


if __name__ == "__main__":
    sys.exit(main())
