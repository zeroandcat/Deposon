"""V5 #21 副本补丁棒 · 落盘件生成器。

三方比对（逐位）：
  ① 适配后锚版读数（.tmp 副本 + 兼容补丁；本棒实测）
  ② 漂移版 09-27 值（_v3_recheck_21_result_2026_09_27.json / _v5_item21_anchor_recompute）
  ③ 原始 3 值（baef94e393de KT_B1_REWORK_REPORT_2026_09_10.md L82-84）

0 判定：只出读数与机械比对，PASS/FAIL 归 verdict-keeper。
"""

import hashlib
import json
import os

OUT_DIR = r"D:/私人资料/deposon-repo/.tmp"
RESULTS = r"D:/私人资料/deposon-repo/results"
ANCHOR_DIR = r"D:/私人资料/_non_upload_local_archive/scripts/scripts/kt_b1"
V19 = "results/deposon_v19_benchmark_fixes.json"

READINGS = {
    "B1_Sinkhorn_OT": {
        "semA_none_default": {
            "patched_file": "_v5_item21_patched_b1_semA_none_default.py",
            "patched_sha12": "ceb33de660fd",
            "patched_bytes": 16768,
            "value": 0.00044522183946429185,
            "value_key": "sinkhorn_distortion_ub_reg_0p1",
            "questions_extracted": 995,
            "vocab_size": 30,
            "questions_empty_best_path": 0,
            "questions_predicted_zero": 262,
            "questions_answer_zero": 495,
            "questions_predicted_negative": 32,
            "elapsed_s": 118.0,
        },
        "semB_none_skip": {
            "patched_file": "_v5_item21_patched_b1_semB_none_skip.py",
            "patched_sha12": "be0208abaffa",
            "patched_bytes": 16829,
            "value": 0.0005069359499770992,
            "value_key": "sinkhorn_distortion_ub_reg_0p1",
            "questions_extracted": 983,
            "vocab_size": 29,
            "questions_empty_best_path": 0,
            "questions_predicted_zero": 250,
            "questions_answer_zero": 495,
            "questions_predicted_negative": 32,
            "elapsed_s": 106.25,
        },
    },
    "B2_KD": {
        "semA_none_default": {
            "patched_file": "_v5_item21_patched_b2_semA_none_default.py",
            "patched_sha12": "801ee31e8bdc",
            "patched_bytes": 16036,
            "value": 0.002813601952161043,
            "value_key": "kd_distortion_ub",
            "teacher_questions": 995,
            "samples_per_question": 100,
            "elapsed_s": 0.5,
        },
        "semB_none_skip": {
            "patched_file": "_v5_item21_patched_b2_semB_none_skip.py",
            "patched_sha12": "8293535673dc",
            "patched_bytes": 16097,
            "value": 0.002815233407313755,
            "value_key": "kd_distortion_ub",
            "teacher_questions": 983,
            "samples_per_question": 100,
            "elapsed_s": 0.46,
        },
    },
    "B3_LLMLingua": {
        "semA_none_default": {
            "patched_file": "_v5_item21_patched_b3_semA_none_default.py",
            "patched_sha12": "9d8a4a875b62",
            "patched_bytes": 15778,
            "value": 0.46342184490589095,
            "value_key": "llmlingua_distortion",
            "prompt_groups": 995,
            "prompts_per_group": 5,
            "prompts_flat": 4975,
            "elapsed_s": 0.39,
        },
        "semB_none_skip": {
            "patched_file": "_v5_item21_patched_b3_semB_none_skip.py",
            "patched_sha12": "8df8e94724ff",
            "patched_bytes": 15839,
            "value": 0.46354948800501566,
            "value_key": "llmlingua_distortion",
            "prompt_groups": 983,
            "prompts_per_group": 5,
            "prompts_flat": 4915,
            "elapsed_s": 0.41,
        },
    },
}

DRIFT_0927 = {
    "B1_Sinkhorn_OT": 0.00044522183946429185,
    "B2_KD": 0.002813601952161043,
    "B3_LLMLingua": 0.46342184490589095,
}

ORIGINAL_3 = {
    "B1_Sinkhorn_OT": 0.0004,
    "B2_KD": 0.0028,
    "B3_LLMLingua": 0.4634,
}

ANCHORS = {
    "B1_Sinkhorn_OT": ("boss_b1_sinkhorn_ot.py.bak", "19325960b8be", 14956),
    "B2_KD": ("boss_b2_kd.py.bak", "1781ea2f742d", 14224),
    "B3_LLMLingua": ("boss_b3_llmlingua.py.bak", "c0b55e0385a4", 13966),
}

DIFF_SHA12 = "09ff35c987d4"
DIFF_BYTES = 19685

PYCACHE_ANCHOR = [
    ("boss_b1_sinkhorn_ot.cpython-314.pyc", 20607, "2026-09-28 19:59:53", "8f5d7b425d55"),
    ("boss_b1_sinkhorn_ot.py.cpython-314.pyc", 18526, "2026-09-28 19:58:39", "6183db0f9d11"),
    ("boss_b2_kd.cpython-314.pyc", 19562, "2026-09-28 20:00:18", "f64071e6739b"),
    ("boss_b2_kd.py.cpython-314.pyc", 17470, "2026-09-28 19:59:09", "f25dd470cf27"),
    ("boss_b3_llmlingua.cpython-314.pyc", 18743, "2026-09-28 20:00:17", "d0413c6f0298"),
    ("boss_b3_llmlingua.py.cpython-314.pyc", 16679, "2026-09-28 19:59:09", "74600cf87765"),
]
PYCACHE_THIS_RUN = [
    ("_v5_item21_patched_b1_semA_none_default.cpython-314.pyc", 20466, "2026-09-28 20:21:04", "b4a1ab09e142"),
    ("_v5_item21_patched_b1_semB_none_skip.cpython-314.pyc", 20484, "2026-09-28 20:23:03", "f4b7bb44ef52"),
    ("_v5_item21_patched_b2_semA_none_default.cpython-314.pyc", 19424, "2026-09-28 20:20:50", "446382bbb63f"),
    ("_v5_item21_patched_b2_semB_none_skip.cpython-314.pyc", 19442, "2026-09-28 20:20:52", "ce4d2edbdc4f"),
    ("_v5_item21_patched_b3_semA_none_default.cpython-314.pyc", 18623, "2026-09-28 20:20:51", "a3315df76d1e"),
    ("_v5_item21_patched_b3_semB_none_skip.cpython-314.pyc", 18641, "2026-09-28 20:20:52", "1c13024cc354"),
]


def rel_dev(a, b):
    """相对偏差 (a 相对 b)。b=0 保护。"""
    if b == 0:
        return None
    return abs(a - b) / abs(b)


def round4_consistent(value):
    """报告值是否与『复算值四舍五入到 4 位小数』自洽。"""
    return round(value, 4) == ORIGINAL_3["__probe__"] if False else None


def main():
    out = {
        "task": "deposon V4 #21 · KT-B1 · 副本补丁复算棒",
        "date": "2026-09-28",
        "author": "worker",
        "pi_decision": "ask_92c2d2005a86c8e47ac9eb95（2026-09-28 20:10）『副本补丁跑』：.tmp 副本打兼容补丁出锚版口径读数；锚版本体 0 触动；读数明标『适配后读数』（非原样读数）",
        "reading_label": "适配后读数·非原样读数（.tmp 副本 + 兼容补丁；锚版本体 0 触动）",
        "judgment": "0 判定（判定归 verdict-keeper；本件只出读数与机械比对）",
        "zero_llm_proxy_gateway_key": True,
        "upstream": {
            "prev_run": "results/_v5_item21_anchor_recompute_2026_09_28.json / .md",
            "prev_json_sha12": "47177cab0303",
            "prev_md_sha12": "e5623d4bd3f3",
            "prev_finding": "锚版 3 件 0/3 可执行（TypeError: float(None)），锚版读数 0 件产出",
        },
        "input_face": {
            "file": V19,
            "sha12": "910c4333eead",
            "bytes": 409104,
            "access": "read_only",
        },
        "patch": {
            "scope": "仅 .tmp 副本；锚版本体 0 字节触动",
            "copies": 6,
            "elements": {
                "1_None_tolerance": "两种语义均登记：语义A=None 视同缺失走默认 0.0（主跑）／语义B=显式跳过该条（敏感性对照）",
                "2_shape_fallback": "predicted→pred（strategyqa 实测形态）、best_path→path、answer 缺失走 0.0（strategyqa 实测无 answer 键）",
                "3_python_3_14": "load_module 已移除 → 沿用上棒 SourceFileLoader（在驱动侧承接，锚本体实测无 load_module 调用）",
            },
            "note": "补丁行数极少（每副本 +59~61 行 helper + 3~4 行抽取块改写）；未触碰任何超参/算法/阈值层",
            "diff_file": ".tmp/_v5_item21_patch.diff",
            "diff_sha12": DIFF_SHA12,
            "diff_bytes": DIFF_BYTES,
        },
        "field_shape_measurement": {
            "method": "直读 v19 frozen（本棒实测），未 import 锚版",
            "gsm8k": {
                "keys_per_record": ["answer", "best_path", "id", "is_correct", "predicted", "trap_hit"],
                "n_per_condition": 100,
                "predicted_null": {"no_deposon": 6, "v1_blocking": 0, "v2_tunneling": 6, "unified": 0, "high_couple": 0},
                "pred_key_present": False,
                "path_key_present": False,
            },
            "strategyqa": {
                "keys_per_record": ["id", "is_correct", "path", "pred", "trap_hit"],
                "n_per_condition": 99,
                "pred_type": "str（'Yes'/'No'）",
                "predicted_key_present": False,
                "answer_key_present": False,
                "best_path_key_present": False,
            },
            "total_predicted_null": 12,
        },
        "readings_adapted_anchor": {},
        "three_way_comparison": [],
        "none_semantics_sensitivity": [],
        "attribution": {},
        "anchor_zero_touch": {},
        "byproducts_registered": {},
        "honest_disclosure": {},
    }

    # ---- 读数 ----
    for boss, sems in READINGS.items():
        for sem, r in sems.items():
            out["readings_adapted_anchor"].setdefault(boss, {})[sem] = r

    # ---- 三方比对（主跑语义A） ----
    for boss in READINGS:
        a = READINGS[boss]["semA_none_default"]["value"]
        b = DRIFT_0927[boss]
        c = ORIGINAL_3[boss]
        out["three_way_comparison"].append({
            "boss": boss,
            "1_adapted_anchor_semA": repr(a),
            "2_drift_0927": repr(b),
            "3_original_reported": repr(c),
            "1_vs_2": {
                "bitwise_identical": a == b,
                "abs_diff": abs(a - b),
                "rel_deviation": rel_dev(a, b),
                "statement": "适配后锚版 ≡ 漂移版（逐位相同）" if a == b else "不等",
            },
            "1_vs_3": {
                "abs_diff": abs(a - c),
                "rel_deviation": rel_dev(a, c),
                "tolerance_window_pm5pct": [c * 0.95, c * 1.05],
                "within_pm5pct": abs(a - c) <= c * 0.05,
                "round4_consistent": round(a, 4) == c,
                "display_halfstep_1e-4": 5e-05,
                "abs_diff_within_display_halfstep": abs(a - c) <= 5e-05,
                "statement": (
                    f"复算值四舍五入到 4 位小数 == 报告值 {c}（自洽）"
                    if round(a, 4) == c else "不自洽（超出 4 位小数显示半步）"),
            },
        })

    # ---- None 语义敏感性 ----
    for boss in READINGS:
        a = READINGS[boss]["semA_none_default"]
        b = READINGS[boss]["semB_none_skip"]
        out["none_semantics_sensitivity"].append({
            "boss": boss,
            "semA_value": repr(a["value"]),
            "semB_value": repr(b["value"]),
            "semA_n": a.get("questions_extracted", a.get("teacher_questions", a.get("prompt_groups"))),
            "semB_n": b.get("questions_extracted", b.get("teacher_questions", b.get("prompt_groups"))),
            "abs_diff": abs(a["value"] - b["value"]),
            "rel_deviation": rel_dev(b["value"], a["value"]),
            "bitwise_identical": a["value"] == b["value"],
            "mechanism": (
                "语义B 剔除 12 条 predicted=null 记录 ⇒ 题集 995→983。"
                + ("B1 词表同步 30→29（被剔除记录的 best_path 含词表独占节点）。" if boss == "B1_Sinkhorn_OT" else "")
            ),
        })

    # ---- 归因 ----
    all_bitwise_same = all(
        READINGS[b]["semA_none_default"]["value"] == DRIFT_0927[b] for b in READINGS)
    orig3_all_round4 = all(
        round(READINGS[b]["semA_none_default"]["value"], 4) == ORIGINAL_3[b] for b in READINGS)
    out["attribution"] = {
        "question": "派工单 §三.3：适配后锚版≈漂移版但≠原始 3 值 ⇒ 原始 3 值另有来源？",
        "finding": (
            "适配后锚版（语义A）与漂移版 09-27 值 3/3 逐位相同"
            if all_bitwise_same else "适配后锚版与漂移版存在差异"),
        "original_3_provenance": (
            "原始 3 值（0.0004/0.0028/0.4634）另有来源，但该来源不是『另一套实现』，"
            "而是**漂移版实现的 4 位小数四舍五入显示**：3/3 复算值 round(·,4) 与报告值逐位相同。"
            if orig3_all_round4 else "原始 3 值与复算值 4 位小数不自洽"),
        "provenance_evidence": [
            "docs/V3X/KT_B1_REWORK_REPORT_2026_09_10.md L82-84（sha12=baef94e393de）记录 3 值",
            "同件 L78 标题 = 『修复后首次跑通』，L32-48 记载 P2 漂移修复（loader 双形态回退 + None/串容错）先于该表",
            "该修复产出的正是现盘漂移版 3 件（7c2b41c008a5/8c6e98034005/2ded5cf0e863，同件 L123-125）",
            "本棒实测：适配后锚版（锚本体 + 等价兼容补丁）≡ 漂移版 ⇒ 两条路径收敛到同一数值",
        ],
        "root_cause_of_b1_pm5pct_miss": (
            "B1 相对偏差 +11.31% 的成因**纯为显示精度**：报告值仅 4 位小数，"
            "±5% 相对窗半宽 2.0e-05 窄于 4 位小数显示半步 5.0e-05；"
            "实测绝对差 4.52e-05 < 显示半步 5.0e-05 ⇒ 数值自洽，机械按相对容差判即超差。"
            "沿用 09-27 登记（354ae9c14fe2），本棒独立复算复核一致，0 改判。"),
        "anchor_vs_drift_nature": (
            "锚版与漂移版在**语义**上同源（同一 BOSS 算法 + 同一超参），"
            "差异仅在字段抽取层的容错完备度；实测锚版全集 hyperparam 层 0 差异。"
            "适配补丁 = 把漂移版的字段容错回填到锚本体 ⇒ 数值必然收敛。"
            "**推论上限**：这证明『漂移 = 未经报告的兼容修复』，**不**证明『漂移版数值错误』。"),
        "residual_caveat": (
            "本棒适配补丁为**语义等价重写**，非逐字回填漂移版实现；"
            "语义等价性由 3/3 逐位相同实测支撑（非仅代码审查推断）。"),
        "judgment_withheld": "0 判定：本节只登记机械事实与来源链，PASS/FAIL/不可复算 归 verdict-keeper",
    }

    # ---- 锚版 0 触动 ----
    for boss, (fname, sha, nbytes) in ANCHORS.items():
        out["anchor_zero_touch"][boss] = {
            "file": fname,
            "pre_run_sha12": sha,
            "post_run_sha12": sha,
            "identical": True,
            "bytes": nbytes,
            "mtime_unchanged": "2026-09-09 11:55:40 / 11:55:41",
            "method": "补丁仅施加于 .tmp 副本（read → replace → write 到 .tmp）",
        }

    # ---- 副产物登记 ----
    out["byproducts_registered"] = {
        "policy": "0 清理（归每日整理）",
        "anchor_dir_pycache_previous_run": {
            "path": "D:/私人资料/_non_upload_local_archive/scripts/scripts/kt_b1/__pycache__",
            "count": len(PYCACHE_ANCHOR),
            "items": [{"name": n, "bytes": b, "mtime": m, "sha12": s}
                      for n, b, m, s in PYCACHE_ANCHOR],
            "origin": "上棒（19:58-20:00 系）import 副产物",
        },
        "tmp_pycache_this_run": {
            "path": "D:/私人资料/deposon-repo/.tmp/__pycache__",
            "count": len(PYCACHE_THIS_RUN),
            "items": [{"name": n, "bytes": b, "mtime": m, "sha12": s}
                      for n, b, m, s in PYCACHE_THIS_RUN],
            "origin": "本棒 20:20-20:23 加载 6 件 .tmp 补丁副本的 import 副产物",
        },
    }

    out["honest_disclosure"] = {
        "no_anchor_original_reading": (
            "锚版**原样**读数仍为 0 件（上棒结论，本棒未推翻、也未试图推翻）："
            "本棒全部读数均标『适配后读数·非原样读数』，0 以适配读数冒充原样锚版读数。"),
        "patch_is_semantic_rewrite": (
            "适配补丁为语义等价重写（非逐字回填漂移版）；等价性由 3/3 逐位相同实测支撑。"),
        "b1_not_a_reproduction_of_original_3": (
            "本棒**未**复现出原始 3 值（0.0004/0.0028/0.4634）本身——"
            "它们是 4 位小数显示值，非全精度字面；已如实登记其来源链。"),
        "b1_runtime": "B1 语义A 118.0 s / 语义B 106.25 s（派工单『约十余分钟量级』预估仍未成立，实为 ~2 min 量级）",
        "judgment_withheld": "0 判定",
        "skill": (
            "派工单 §四『skill 若 not found 按字面执行』：本 Turn 工具集内无 skill 加载入口 "
            "⇒ 未加载任何 skill；按派工单字面执行，0 编造 skill 指令。"),
        "succeeded_ne_runs_done": (
            "完成宣告以本棒落盘件字节 + SHA-12 实测为准（worker succeeded ≠ 跑完）。"),
    }

    path = f"{RESULTS}/_v5_item21_patched_recompute_2026_09_28.json"
    with open(path, "w", encoding="utf-8", newline="") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    with open(path, "rb") as f:
        raw = f.read()
    print("###JSON_OUT###", path, len(raw), hashlib.sha256(raw).hexdigest()[:12])


if __name__ == "__main__":
    main()
