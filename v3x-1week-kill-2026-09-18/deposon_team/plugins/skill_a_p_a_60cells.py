# -*- coding: utf-8 -*-
"""
skill_a_p_a_60cells.py
======================
Deposon V3X 路径 ①:深耕 P-A 均衡稳定化
0 LLM / 0 proxy / 0 API 调用的纯 Python + stdlib 复算脚本
(沿 V2 阶段 1-3.5 9 model × 60 cells 守恒 540/540 baseline 验算)

输入:
  D:\\私人资料\\deposon-repo\\results\\deposon_v2_phase1_60cells_2026_09_11.json
  D:\\私人资料\\deposon-repo\\results\\deposon_v3_physical_opt_60cells_2026_09_11.json
  D:\\私人资料\\deposon-repo\\verifier\\handoff\\KT_ABC1_anchors_sha256_12.json

输出(两件):
  1. stdout 打印 60 cells + 9 model × 60 cells = 540 守恒明细
  2. JSON 落盘到 results/skill_a_p_a_60cells_result_2026_09_11.json

严守 7 铁律:
  - 0 LLM calls / 0 proxy / 0 网关 (OpenRouter / TeamoRouter / V4.1-Flash / GPT-6 / agent-plan / WeChat API)
  - 不动 5 锚 + 4 SPEC V0.1 + v19/v21 + corpus/v20 + 200+ 已落盘 + 现有 PDF/MD 报告
  - 不动 V3X 项目内 scripts/ 目录
  - 不动 .minimax/agents 下 verifier / mavis / .builtin 目录
  - 不创建临时文件 (除 results/ 下的最终 dump)

作者: Mavis Worker (subagent of mvs_bbeb804b1a6a41109be740636eed1709)
日期: 2026-09-11
"""

import os
import json
import hashlib
import sys
import datetime

# ---------- 路径常量(绝对,严守不动 scripts/) ----------
REPO_ROOT = r"D:\私人资料\deposon-repo"
PHASE1_JSON = os.path.join(REPO_ROOT, "results", "deposon_v2_phase1_60cells_2026_09_11.json")
V3_PHYS_JSON = os.path.join(REPO_ROOT, "results", "deposon_v3_physical_opt_60cells_2026_09_11.json")
ANCHOR_JSON = os.path.join(REPO_ROOT, "verifier", "handoff", "KT_ABC1_anchors_sha256_12.json")
OUT_JSON = os.path.join(REPO_ROOT, "results", "skill_a_p_a_60cells_result_2026_09_11.json")


def sha12_file(path):
    """读全文 SHA-256[0:12],与既有 5 锚 SHA-12 判定线对齐。"""
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def count_t_r_a_from_cells(cells):
    """对 60 cells 列表逐 cell 计 T/R/A:
       T = llm_extracted 与 gold 严格相等 (含数值/字符串全等)
       R = 不等
       A = 缺失或显式 abstain (此处不出现, 占 0)
    """
    T, R, A = 0, 0, 0
    for c in cells:
        ex, go = c.get("llm_extracted"), c.get("gold")
        if ex is None or go is None:
            A += 1
        elif ex == go:
            T += 1
        else:
            R += 1
    return T, R, A


def main():
    started = datetime.datetime.now().isoformat(timespec="seconds")

    # ---------- 0 LLM 工具链自证 ----------
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

    # ---------- 1. 5 锚 SHA-12 实算验证 (期望 03c6c01f3697) ----------
    anchor_sha12 = sha12_file(ANCHOR_JSON)
    anchor_expected = "03c6c01f3697"
    anchor_pass = (anchor_sha12 == anchor_expected)

    # ---------- 2. v2 phase1 60 cells 实测明细 ----------
    phase1 = load_json(PHASE1_JSON)
    existing30 = phase1.get("existing_30_cells", [])
    new30 = phase1.get("new_30_cells", [])
    n_existing = len(existing30)
    n_new = len(new30)
    n_60 = n_existing + n_new
    T60_e, R60_e, A60_e = count_t_r_a_from_cells(existing30)
    T60_n, R60_n, A60_n = count_t_r_a_from_cells(new30)
    T60 = T60_e + T60_n
    R60 = R60_e + R60_n
    A60 = A60_e + A60_n

    # ---------- 3. v3 physical opt 9 models × 60 cells = 540 守恒复算 ----------
    v3 = load_json(V3_PHYS_JSON)
    per_model = v3["P_C_distortion_bound_60cells"]["per_model"]
    n_models = len(per_model)
    n_540 = n_models * 60
    T540 = sum(pm["T60"] for pm in per_model)
    R540 = sum(pm["R60"] for pm in per_model)
    A540 = sum(pm["A60"] for pm in per_model)
    # 守恒律: T + R + A = 60 (每 model)
    residuals = [(pm["T60"] + pm["R60"] + pm["A60"]) - 60 for pm in per_model]
    conservation_pass = (max(residuals) == 0 and min(residuals) == 0)
    n_540_total_residual = T540 + R540 + A540 - n_540

    # ---------- 4. T_frac 60 加权均值复算 ----------
    T_frac60_total = sum(pm["T_frac60"] * 60 for pm in per_model)
    T_frac60_mean = round(T_frac60_total / n_540, 4)

    # ---------- 5. D_fix2 余弦均值复算 ----------
    D_fix2_mean = round(sum(pm["D_fix2_cosine"] for pm in per_model) / n_models, 4)
    cos_sim_mean = round(sum(pm["cos_sim"] for pm in per_model) / n_models, 4)

    # ---------- 6. V2 阶段 5 D 路径基线 (从 v3 input_data 取) ----------
    dpath_sim = v3["input_data"]["v2_stage5_dpath_sim"]
    modal_means = v3["input_data"]["modal_means_baseline"]

    # ---------- 7. 组装 result ----------
    result = {
        "skill": "skill_a_p_a_60cells",
        "phase": "V3X 路径 ①:深耕 P-A 均衡稳定化 (9 model × 60 cells 守恒 540/540 baseline 验算)",
        "date": "2026-09-11",
        "started_at": started,
        "iron_rule_compliance": iron,
        "inputs": {
            "phase1_json": os.path.relpath(PHASE1_JSON, REPO_ROOT),
            "phase1_json_size_B": os.path.getsize(PHASE1_JSON),
            "v3_phys_json": os.path.relpath(V3_PHYS_JSON, REPO_ROOT),
            "v3_phys_json_size_B": os.path.getsize(V3_PHYS_JSON),
            "anchor_json": os.path.relpath(ANCHOR_JSON, REPO_ROOT),
            "anchor_json_sha12_observed": anchor_sha12,
            "anchor_json_sha12_expected": anchor_expected,
            "anchor_pass": anchor_pass,
        },
        "v2_phase1_60cells_breakdown": {
            "existing_30_cells_count": n_existing,
            "new_30_cells_count": n_new,
            "total_60_cells": n_60,
            "T60_existing30": T60_e,
            "R60_existing30": R60_e,
            "A60_existing30": A60_e,
            "T60_new30": T60_n,
            "R60_new30": R60_n,
            "A60_new30": A60_n,
            "T60_total": T60,
            "R60_total": R60,
            "A60_total": A60,
            "conservation_residual_60": (T60 + R60 + A60) - 60,
        },
        "v3_540cells_9model_x_60_verification": {
            "n_models": n_models,
            "cells_per_model": 60,
            "n_540_total": n_540,
            "T540_sum": T540,
            "R540_sum": R540,
            "A540_sum": A540,
            "conservation_residual_540": n_540_total_residual,
            "conservation_pass": conservation_pass,
            "per_model_residuals": residuals,
            "T_frac60_total_weighted": T_frac60_total,
            "T_frac60_mean": T_frac60_mean,
            "D_fix2_mean": D_fix2_mean,
            "cos_sim_mean": cos_sim_mean,
            "v2_stage5_dpath_baseline": dpath_sim,
            "modal_means_baseline": modal_means,
        },
        "verdict": "PASS" if (anchor_pass and conservation_pass and n_540_total_residual == 0) else "FAIL",
    }

    # ---------- 8. stdout 明细打印 ----------
    print("=" * 72)
    print("skill_a_p_a_60cells | V3X 路径 ①  P-A 均衡稳定化 9 model × 60 cells 守恒验算")
    print("=" * 72)
    print(f"5 锚 SHA-12 实算  : {anchor_sha12}  (期望 {anchor_expected}) -> {'PASS' if anchor_pass else 'FAIL'}")
    print(f"v2 phase1 60 cells 拆分:")
    print(f"  existing_30 = {n_existing:>2d}  T={T60_e:>2d} R={R60_e:>2d} A={A60_e:>2d}")
    print(f"  new_30      = {n_new:>2d}  T={T60_n:>2d} R={R60_n:>2d} A={A60_n:>2d}")
    print(f"  total_60    = {n_60:>2d}  T={T60:>2d} R={R60:>2d} A={A60:>2d}  residual={result['v2_phase1_60cells_breakdown']['conservation_residual_60']}")
    print(f"v3 9 model × 60 cells = 540 守恒复算:")
    print(f"  n_models      = {n_models}")
    print(f"  T540+R540+A540= {T540}+{R540}+{A540} = {T540 + R540 + A540}  (期望 540)  residual={n_540_total_residual}")
    print(f"  每 model 60 cells residual max/min = {max(residuals)}/{min(residuals)}  -> {'PASS' if conservation_pass else 'FAIL'}")
    print(f"  T_frac60 加权均值 = {T_frac60_mean}")
    print(f"  D_fix2 余弦均值   = {D_fix2_mean}   cos_sim 均值 = {cos_sim_mean}")
    print(f"V2 阶段 5 D 路径基线 (input_data): tt_off={dpath_sim['tt_off']} ii_off={dpath_sim['ii_off']} ti_off={dpath_sim['ti_off']}")
    print(f"模态均值: text={modal_means['text']} image={modal_means['image']} cross={modal_means['cross_modal']}")
    print(f"综合 verdict: {result['verdict']}")
    print("=" * 72)

    # ---------- 9. JSON 落盘 (仅 results/, 不在 scripts/) ----------
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"已落盘: {os.path.relpath(OUT_JSON, REPO_ROOT)}  ({os.path.getsize(OUT_JSON)} B)")
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
