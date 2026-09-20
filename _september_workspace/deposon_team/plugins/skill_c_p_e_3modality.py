# -*- coding: utf-8 -*-
"""
skill_c_p_e_3modality.py
=========================
Deposon V3X 路径 ② 扩展:三模态守恒 ε 检测
(沿 V2 阶段 5 F-5: 9 model × 30 cells 三模态 text/image/text×image 守恒检测)

输入:
  D:\\私人资料\\deposon-repo\\results\\deposon_dpath_cross_modal_2026_09_10.json
  D:\\私人资料\\deposon-repo\\results\\deposon_v3_physical_opt_60cells_2026_09_11.json
  D:\\私人资料\\deposon-repo\\verifier\\handoff\\KT_ABC1_anchors_sha256_12.json

输出:
  1. stdout 打印三模态 ε 分布 (text/image/cross) + 9 model ε 60 cells
  2. JSON 落盘到 results/skill_c_p_e_3modality_result_2026_09_11.json

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
DPATH_JSON = os.path.join(REPO_ROOT, "results", "deposon_dpath_cross_modal_2026_09_10.json")
V3_PHYS_JSON = os.path.join(REPO_ROOT, "results", "deposon_v3_physical_opt_60cells_2026_09_11.json")
ANCHOR_JSON = os.path.join(REPO_ROOT, "verifier", "handoff", "KT_ABC1_anchors_sha256_12.json")
OUT_JSON = os.path.join(REPO_ROOT, "results", "skill_c_p_e_3modality_result_2026_09_11.json")


def sha12_file(path):
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


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

    # ---------- 2. dpath cross modal 实测 (单 model: doubao-seed-2.0-lite) ----------
    dpath = load_json(DPATH_JSON)
    sim = dpath["sim_matrix"]
    cells = dpath["cells"]
    n_cells = len(cells)

    # 每 cell 计算 text_frac / image_frac / cross_frac (top-1 sim_score)
    cell_modals = []
    for c in cells:
        top_text = c.get("top_text", [])
        top_image = c.get("top_image", [])
        top_cross = c.get("top_cross", [])
        text_frac = top_text[0]["sim_score"] if top_text else 0.0
        image_frac = top_image[0]["sim_score"] if top_image else 0.0
        cross_frac = top_cross[0]["sim_score"] if top_cross else (
            # 若无 top_cross, 用 top_text 与 top_image 均值
            (text_frac + image_frac) / 2.0 if (top_text and top_image) else 0.0
        )
        # 三模态 ε
        eps_ti = abs(text_frac - image_frac)
        eps_ic = abs(image_frac - cross_frac)
        eps_ct = abs(cross_frac - text_frac)
        eps_3modal_sum = round(eps_ti + eps_ic + eps_ct, 6)
        cell_modals.append({
            "cell_id": c["cell_id"],
            "task": c["task"],
            "text_frac": round(text_frac, 4),
            "image_frac": round(image_frac, 4),
            "cross_frac": round(cross_frac, 4),
            "eps_ti": round(eps_ti, 4),
            "eps_ic": round(eps_ic, 4),
            "eps_ct": round(eps_ct, 4),
            "eps_3modal_sum": eps_3modal_sum,
        })

    # dpath 单 model 均值
    mean_t = round(sum(c["text_frac"] for c in cell_modals) / max(1, len(cell_modals)), 4)
    mean_i = round(sum(c["image_frac"] for c in cell_modals) / max(1, len(cell_modals)), 4)
    mean_x = round(sum(c["cross_frac"] for c in cell_modals) / max(1, len(cell_modals)), 4)
    mean_eps = round(sum(c["eps_3modal_sum"] for c in cell_modals) / max(1, len(cell_modals)), 4)

    # ---------- 3. v3 P_E 9 model × 60 cells ε 分布复算 ----------
    v3 = load_json(V3_PHYS_JSON)
    pe_per_model = v3["P_E_3modal_conservation_60cells"]["per_model"]
    pe_summary = v3["P_E_3modal_conservation_60cells"]["summary"]

    # verdict 阈值 (与 v3 一致)
    def pe_verdict(eps_sum):
        if eps_sum < 0.30:
            return "PASS"
        elif eps_sum < 0.50:
            return "GRAY"
        else:
            return "FAIL"

    pe_dist = {"PASS": 0, "GRAY": 0, "FAIL": 0}
    pe_recomputed = []
    for pm in pe_per_model:
        eps = pm["eps_3modal_sum"]
        v = pe_verdict(eps)
        pe_dist[v] += 1
        pe_recomputed.append({
            "model": pm["model"],
            "T_frac": pm["T_frac"],
            "image_frac": pm["image_frac"],
            "cross_frac": pm["cross_frac"],
            "eps_ti": pm["eps_ti"],
            "eps_ic": pm["eps_ic"],
            "eps_ct": pm["eps_ct"],
            "eps_3modal_sum": eps,
            "verdict_recomputed": v,
            "verdict_v3": pm["verdict"],
            "verdict_match": v == pm["verdict"],
        })
    pe_match = (pe_dist == pe_summary["verdict_distribution"])

    # ---------- 4. 阈值漂移链 (沿 Trae R4 勘误) ----------
    thresh_chain = "0.10 -> 0.50 -> 0.30 (V2 阶段 5 FAIL 判定未被同口径推翻, P-E 维持 GRAY)"

    # ---------- 5. 组装 result ----------
    result = {
        "skill": "skill_c_p_e_3modality",
        "phase": "V3X 路径 ② 扩展:P-E 三模态守恒 ε 检测 (9 model × 60 cells)",
        "date": "2026-09-11",
        "started_at": started,
        "iron_rule_compliance": iron,
        "inputs": {
            "dpath_json": os.path.relpath(DPATH_JSON, REPO_ROOT),
            "dpath_json_size_B": os.path.getsize(DPATH_JSON),
            "v3_phys_json": os.path.relpath(V3_PHYS_JSON, REPO_ROOT),
            "v3_phys_json_size_B": os.path.getsize(V3_PHYS_JSON),
            "anchor_json": os.path.relpath(ANCHOR_JSON, REPO_ROOT),
            "anchor_json_sha12_observed": anchor_sha12,
            "anchor_json_sha12_expected": anchor_expected,
            "anchor_pass": anchor_pass,
        },
        "dpath_single_model_30cells": {
            "n_cells_observed": n_cells,
            "sim_matrix_observed": {
                "text_text_offdiag_mean": sim["text_text_offdiag_mean"],
                "image_image_offdiag_mean": sim["image_image_offdiag_mean"],
                "text_image_offdiag_mean": sim["text_image_offdiag_mean"],
            },
            "per_cell_top1_sim": {
                "text_mean": mean_t,
                "image_mean": mean_i,
                "cross_mean": mean_x,
                "eps_3modal_mean": mean_eps,
            },
        },
        "v3_pe_9model_60cells_verification": {
            "n_models": len(pe_per_model),
            "per_model": pe_recomputed,
            "p_e_verdict_distribution_recomputed": pe_dist,
            "p_e_verdict_distribution_v3_expected": pe_summary["verdict_distribution"],
            "p_e_distribution_match": pe_match,
            "eps_60cells_mean_v3": pe_summary["eps_60cells_mean"],
            "eps_60cells_min_v3": pe_summary["eps_60cells_min"],
            "eps_60cells_max_v3": pe_summary["eps_60cells_max"],
            "thresh_chain": thresh_chain,
        },
        "verdict": "PASS" if (anchor_pass and pe_match) else "FAIL",
    }

    # ---------- 6. stdout 打印 ----------
    print("=" * 72)
    print("skill_c_p_e_3modality | V3X 路径 ② 扩展  P-E 三模态守恒 ε 检测")
    print("=" * 72)
    print(f"5 锚 SHA-12 实算  : {anchor_sha12}  (期望 {anchor_expected}) -> {'PASS' if anchor_pass else 'FAIL'}")
    print(f"dpath 单 model (doubao-seed-2.0-lite) cells={n_cells}")
    print(f"  text_mean={mean_t}  image_mean={mean_i}  cross_mean={mean_x}  eps_3modal_mean={mean_eps}")
    print(f"  sim_matrix: tt_off={sim['text_text_offdiag_mean']}  ii_off={sim['image_image_offdiag_mean']}  ti_off={sim['text_image_offdiag_mean']}")
    print(f"v3 P_E 9 model × 60 cells 复算:")
    for r in pe_recomputed:
        print(f"  {r['model']:<24s}  eps_sum={r['eps_3modal_sum']:.4f}  复算={r['verdict_recomputed']:<4s}  v3={r['verdict_v3']:<4s}  match={r['verdict_match']}")
    print(f"P_E 分布 复算={pe_dist}  v3={pe_summary['verdict_distribution']}  match={pe_match}")
    print(f"阈值漂移链: {thresh_chain}")
    print(f"综合 verdict: {result['verdict']}")
    print("=" * 72)

    # ---------- 7. JSON 落盘 ----------
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"已落盘: {os.path.relpath(OUT_JSON, REPO_ROOT)}  ({os.path.getsize(OUT_JSON)} B)")
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
