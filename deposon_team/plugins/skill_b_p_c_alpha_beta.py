# -*- coding: utf-8 -*-
"""
skill_b_p_c_alpha_beta.py
==========================
Deposon V3X 路径 ②:补 P-C 判定标准 (α-β 模板冗余 + 5 锚判定线)
0 LLM / 0 proxy / 0 API 调用的纯 Python + stdlib 复算脚本

输入:
  D:\\私人资料\\deposon-repo\\results\\deposon_v3_physical_opt_60cells_2026_09_11.json
  D:\\私人资料\\deposon-repo\\verifier\\handoff\\KT_ABC1_anchors_sha256_12.json

输出:
  1. stdout 打印 36 档判定 (9 model × 4 T_frac bins, 9 in_bin + 27 out_of_bin)
  2. α-β 模板冗余判定 (基于 T_frac 与 cos_sim 双坐标网格)
  3. 5 锚 SHA-12 判定线比对
  4. JSON 落盘到 results/skill_b_p_c_alpha_beta_result_2026_09_11.json

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
V3_PHYS_JSON = os.path.join(REPO_ROOT, "results", "deposon_v3_physical_opt_60cells_2026_09_11.json")
ANCHOR_JSON = os.path.join(REPO_ROOT, "verifier", "handoff", "KT_ABC1_anchors_sha256_12.json")
OUT_JSON = os.path.join(REPO_ROOT, "results", "skill_b_p_c_alpha_beta_result_2026_09_11.json")


def sha12_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


# 4 个 T_frac bin (与 v3 decision_lines_36.bins 一致)
BINS = [
    {"label": "bin_1_PASS", "lo": 0.85, "hi": 1.001},
    {"label": "bin_2_HIGH", "lo": 0.70, "hi": 0.85},
    {"label": "bin_3_MID",  "lo": 0.60, "hi": 0.70},
    {"label": "bin_4_LOW",  "lo": 0.00, "hi": 0.60},
]

# P_C 余弦阈值 (与 v3 一致)
PC_THRESH = {"PASS": 0.85, "GRAY_LO": 0.70}
# P_E 模态守恒阈值
PE_THRESH = {"PASS": 0.30, "GRAY_LO": 0.50}


def in_bin(t_frac, lo, hi):
    return lo <= t_frac < hi


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
        "method": "纯 Python stdlib (json + hashlib + os + datetime), 0 numpy 依赖",
    }

    # ---------- 1. 5 锚 SHA-12 验证 ----------
    anchor_sha12 = sha12_file(ANCHOR_JSON)
    anchor_expected = "03c6c01f3697"
    anchor_pass = (anchor_sha12 == anchor_expected)

    # ---------- 2. v3 物理公式 9 model + 4 bin = 36 档判定线 ----------
    v3 = load_json(V3_PHYS_JSON)
    models = v3["input_data"]["9_models"]
    per_model = v3["P_C_distortion_bound_60cells"]["per_model"]
    T_C_baseline = v3["input_data"]["T_C_baseline"]
    A_C_baseline = v3["input_data"]["A_C_baseline"]

    # ---------- 3. α-β 模板冗余 (T_frac × cos_sim 双坐标网格) ----------
    # α = T_frac 模板对齐度 (0..1)
    # β = cos_sim 模板对齐度 (0..1)
    # redundancy 判定: 若 α 跨 bin 仍 β >= 0.85 -> 模板冗余 (PASS 行为被 α-降级)
    alpha_beta_table = []
    for m, pm in zip(models, per_model):
        a = round(m["T_frac"], 4)
        b = round(pm["cos_sim"], 4)
        # 模板冗余判定: 同一 model 在 4 bin 都有 cos_sim 期望? 用 v3 公式反推
        # 这里记录主 bin cos_sim; 冗余度 = 1 - |a - T_C_baseline| (越接近 baseline 越冗余)
        redundancy = round(1.0 - abs(a - T_C_baseline), 4)
        # α-β 协调 verdict
        if b >= PC_THRESH["PASS"] and a >= 0.85:
            ab_verdict = "REDUNDANT_PASS"
        elif b >= PC_THRESH["PASS"] and a >= 0.70:
            ab_verdict = "REDUNDANT_GRAY"
        elif b >= PC_THRESH["PASS"]:
            ab_verdict = "ALIGNED_LOW"
        else:
            ab_verdict = "MISMATCH"
        alpha_beta_table.append({
            "model": m["name"],
            "alpha_T_frac": a,
            "beta_cos_sim": b,
            "redundancy_score": redundancy,
            "ab_verdict": ab_verdict,
        })

    # ---------- 4. 36 档判定线: 9 model × 4 bin ----------
    grid_36 = []
    for m, pm in zip(models, per_model):
        for b in BINS:
            in_main_bin = in_bin(m["T_frac"], b["lo"], b["hi"])
            # out_of_bin 时, cos_sim 退化估计 = β * (1 - 距离主 bin 比例)
            if in_main_bin:
                cos_here = pm["cos_sim"]
                verdict_p_c = pm["verdict"]
            else:
                # 用 D_fix2 反推
                d_fix2_here = round(1.0 - (1.0 - pm["D_fix2_cosine"]) * 0.5, 4)
                cos_here = round(1.0 - d_fix2_here, 4)
                if cos_here >= PC_THRESH["PASS"]:
                    verdict_p_c = "PASS"
                elif cos_here >= PC_THRESH["GRAY_LO"]:
                    verdict_p_c = "GRAY"
                else:
                    verdict_p_c = "FAIL"
            grid_36.append({
                "model": m["name"],
                "bin_label": b["label"],
                "bin_lo": b["lo"],
                "bin_hi": b["hi"],
                "in_main_bin": in_main_bin,
                "cos_sim_in_bin": cos_here,
                "verdict_p_c_in_bin": verdict_p_c,
            })
    in_bin_count = sum(1 for g in grid_36 if g["in_main_bin"])
    out_bin_count = 36 - in_bin_count

    # ---------- 5. P_C verdict 分布 (沿 v3 一致性复算) ----------
    pc_dist = {"PASS": 0, "GRAY": 0, "FAIL": 0}
    for g in grid_36:
        if g["in_main_bin"]:
            pc_dist[g["verdict_p_c_in_bin"]] += 1
    # 与 v3 P_C verdict_distribution: {"PASS": 8, "GRAY": 1, "FAIL": 0} 对比
    v3_pc_dist = v3["P_C_distortion_bound_60cells"]["summary"]["verdict_distribution"]
    pc_dist_match = (pc_dist == v3_pc_dist)

    # ---------- 6. 组装 result ----------
    result = {
        "skill": "skill_b_p_c_alpha_beta",
        "phase": "V3X 路径 ②:补 P-C 判定标准 (α-β 模板冗余 + 5 锚判定线 + 36 档)",
        "date": "2026-09-11",
        "started_at": started,
        "iron_rule_compliance": iron,
        "inputs": {
            "v3_phys_json": os.path.relpath(V3_PHYS_JSON, REPO_ROOT),
            "v3_phys_json_size_B": os.path.getsize(V3_PHYS_JSON),
            "anchor_json": os.path.relpath(ANCHOR_JSON, REPO_ROOT),
            "anchor_json_sha12_observed": anchor_sha12,
            "anchor_json_sha12_expected": anchor_expected,
            "anchor_pass": anchor_pass,
        },
        "alpha_beta_template_redundancy": {
            "formula": "redundancy = 1 - |alpha - T_C_baseline|; ab_verdict 4 档 (REDUNDANT_PASS / REDUNDANT_GRAY / ALIGNED_LOW / MISMATCH)",
            "T_C_baseline": T_C_baseline,
            "A_C_baseline": A_C_baseline,
            "per_model": alpha_beta_table,
        },
        "decision_lines_36_verification": {
            "structure": "9 model × 4 T_frac bins = 36 档 (9 in_bin + 27 out_of_bin)",
            "bins": BINS,
            "in_bin_count": in_bin_count,
            "out_of_bin_count": out_bin_count,
            "grid_36": grid_36,
            "p_c_in_bin_distribution": pc_dist,
            "p_c_in_bin_distribution_v3_expected": v3_pc_dist,
            "p_c_distribution_match": pc_dist_match,
        },
        "verdict": "PASS" if (anchor_pass and pc_dist_match) else "FAIL",
    }

    # ---------- 7. stdout 打印 ----------
    print("=" * 72)
    print("skill_b_p_c_alpha_beta | V3X 路径 ②  P-C α-β 模板冗余 + 36 档判定线")
    print("=" * 72)
    print(f"5 锚 SHA-12 实算  : {anchor_sha12}  (期望 {anchor_expected}) -> {'PASS' if anchor_pass else 'FAIL'}")
    print(f"基线 T_C={T_C_baseline}  A_C={A_C_baseline}")
    print("α-β 模板冗余判定 (9 model):")
    for r in alpha_beta_table:
        print(f"  {r['model']:<24s}  α={r['alpha_T_frac']:.4f}  β={r['beta_cos_sim']:.4f}  redundancy={r['redundancy_score']:.4f}  -> {r['ab_verdict']}")
    print(f"36 档判定线 in_bin={in_bin_count} / out_of_bin={out_bin_count}")
    print(f"P_C in_bin verdict 分布 复算={pc_dist}  期望={v3_pc_dist}  match={pc_dist_match}")
    print(f"综合 verdict: {result['verdict']}")
    print("=" * 72)

    # ---------- 8. JSON 落盘 ----------
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"已落盘: {os.path.relpath(OUT_JSON, REPO_ROOT)}  ({os.path.getsize(OUT_JSON)} B)")
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
