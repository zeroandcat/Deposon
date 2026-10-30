# -*- coding: utf-8 -*-
"""
F2 / D4 重标落地生成器 (数据面修正注记件)
==========================================
派工棒: worker (执行类) — PI 2026-09-27「minimax 可修 bug 请直接修」棒
原件:  results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json  (CBF60A630C9F, 20,194 B) 0 改写 0 合并
出件:  results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json (新件, 注记用, 不覆盖原件)

重标结论来源 (拍板出处链, 逐件如实登记):
  PI 2026-09-27 派工单 → verifier 双复核呈文 (2026-09-27, 只读复核 0 写入, **呈文本身不落盘**)
  → doc-writer 勘误链 docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md §22.31.2 E-42.2 登记面
  → 本棒数据面落地 (本件)
判型基准: results/_v4_pi_cot_v2_questionnaire_v1.md §1 字面 (本棒逐行读取, 非转写)

0 LLM / 0 proxy / 0 gateway / 0 key / 0 阈值触动 / 0 派生 JSON 合并 / 0 覆盖既有件。
"""
from __future__ import annotations

import json
import hashlib
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RES = REPO / "results"
D4 = RES / "_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json"
QUEST = RES / "_v4_pi_cot_v2_questionnaire_v1.md"
ERRATA = REPO / "docs" / "V3X" / "TRAE_V3_ASSET_ERRATUM_2026_09_23.md"
EXEC_BASE = RES / "_v4_pi_cot_v3_ruleset_v3_executor.py"
EXEC_R1 = RES / "_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py"
OUT = RES / "_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json"

TS_FROZEN = "2026-09-27T18:05:00+08:00"


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12].upper()


# ---------------------------------------------------------------------------
# 1. 判型基准 (questionnaire_v1 §1 字面, 本棒逐行读取盘上件)
# ---------------------------------------------------------------------------
TAXONOMY = {
    "source_path": "results/_v4_pi_cot_v2_questionnaire_v1.md",
    "source_sha12": sha12(QUEST),
    "source_section": "§1",
    "codes": [
        {"code": "J1", "type": "判死线", "criterion": "何时判死 / 放行 / 缓决 / 补构造再审"},
        {"code": "J2", "type": "成本", "criterion": "资源·时间·风险投入取舍"},
        {"code": "J3", "type": "准则", "criterion": "核心准则应用（大材小用 / 落到实处 / 与死同行 / 虚实回路）"},
        {"code": "J4", "type": "风险", "criterion": "铁律·红线·安全边界"},
        {"code": "J5", "type": "时机", "criterion": "先后·缓急·排期"},
        {"code": "J6", "type": "委托", "criterion": "派工·自做·请示分工"},
    ],
}

# ---------------------------------------------------------------------------
# 2. E-42.2 逐件重标表 (结论沿勘误链 §22.31.2 登记字面; option_chosen / 原文本棒逐件实测)
# ---------------------------------------------------------------------------
RELABEL = {
    "D4_Q1": {
        "judge_type_relabeled": "J5",
        "relabel_basis": "questionnaire_v1 §1 字面 J5 时机 = 先后·缓急·排期; 本件 option = 续采 D4/D5 至跨日 3 天 (采集轮次 / 先后)",
        "ambiguity": None,
    },
    "D4_Q2": {
        "judge_type_relabeled": "J1",
        "relabel_basis": "questionnaire_v1 §1 字面 J1 判死线 = 何时判死 / 放行 / 缓决 / 补构造再审; 本件 option = D1 缺位 8 件维持不补造 (72 件口径立案不变) = 对缺位件判死处置",
        "ambiguity": "J4 风险亦可辩 (铁律·红线·安全边界: 维持不补造亦是边界处置); E-42.2 明示二者可辩, 以 J1 为主记、J4 并记, 本件两码如实并存",
        "judge_type_relabeled_alternative": "J4",
    },
    "D4_Q3": {
        "judge_type_relabeled": "J5",
        "relabel_basis": "questionnaire_v1 §1 字面 J5 时机 = 先后·缓急·排期; 本件 option = v3 四件链立即串行跑 (立即 = 排期 / 缓急)",
        "ambiguity": None,
    },
    "D4_Q4": {
        "judge_type_relabeled": "J4",
        "relabel_basis": "questionnaire_v1 §1 字面 J4 风险 = 铁律·红线·安全边界; 本件 option = 阶段间铁律不自动延续 (V3→V4 各阶段适用) = 铁律边界 / 红线",
        "ambiguity": None,
    },
    "D4_Q5": {
        "judge_type_relabeled": "J3",
        "relabel_basis": "questionnaire_v1 §1 字面 J3 准则 = 核心准则应用; 本件 option = 诚实 = 不误导 (核心准则应用)",
        "ambiguity": None,
        "unchanged_confirmed": True,
    },
}

DECISION_SOURCE = {
    "chain": "PI 2026-09-27 派工单 → verifier 双复核呈文 (2026-09-27, 只读复核 0 写入, 呈文本身不落盘) → doc-writer 勘误链 §22.31.2 E-42.2 登记面 → 本棒数据面落地",
    "registration_surface": "docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md §22.31.2 E-42.2 F2 D4 标注重标（高）",
    "registration_surface_sha12": sha12(ERRATA),
    "caveat": "verifier 双复核呈文本棒未见 (呈文不落盘) → 拍板出处只能追到勘误链 §22.31.2 登记面, 登记面自身字面记「重标结论沿派工单字面」; 本棒不代填呈文原意",
}

# ---------------------------------------------------------------------------
# 3. 附注一实测: D2/D3「既有惯例」是否存在 (逐件实测 9 件补充件)
# ---------------------------------------------------------------------------
SUPP_FILES = [
    "_v4_pi_cot_v2_dataset_addendum_2026_09_24.json",
    "_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json",
    "_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json",
    "_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json",
    "_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json",
    "_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json",
    "_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json",
    "_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json",
    "_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json",
]
per_file = []
tot = with_jt = 0
for f in SUPP_FILES:
    p = RES / f
    sups = json.loads(p.read_text(encoding="utf-8")).get("supplements", [])
    w = sum(1 for s in sups if "judge_type" in s)
    per_file.append({"file": f"results/{f}", "sha12": sha12(p), "n_supplements": len(sups),
                     "n_with_judge_type": w})
    tot += len(sups)
    with_jt += w

# ---------------------------------------------------------------------------
# 4. 逐件表
# ---------------------------------------------------------------------------
d4 = json.loads(D4.read_text(encoding="utf-8"))
items = []
n_same = 0
for s in d4["supplements"]:
    qid = s["q_id"]
    r = RELABEL[qid]
    same = (s["judge_type"] == r["judge_type_relabeled"])
    n_same += int(same)
    items.append({
        "q_id": qid,
        "pair_id": s["pair_id"],
        "scene_tag": s["scene_tag"],
        "option_chosen": s["option_chosen"],
        "option_meaning": s["option_meaning"],
        "reasoning_full": s["reasoning_full"],
        "pi_source_verbatim": s["pi_source_verbatim"],
        "pi_source_briefing_location": s["pi_source_briefing_location"],
        "pi_source_date": s["pi_source_date"],
        "collected_via": s["collected_via"],
        "judge_type_original": s["judge_type"],
        "judge_type_original_note": s["judge_type_note"],
        "judge_type_relabeled": r["judge_type_relabeled"],
        "judge_type_relabeled_alternative": r.get("judge_type_relabeled_alternative"),
        "changed": not same,
        "relabel_basis": r["relabel_basis"],
        "ambiguity_note": r.get("ambiguity"),
        "decision_source": DECISION_SOURCE["chain"],
    })

orig_dist = {}
new_dist = {}
for it in items:
    orig_dist[it["judge_type_original"]] = orig_dist.get(it["judge_type_original"], 0) + 1
    new_dist[it["judge_type_relabeled"]] = new_dist.get(it["judge_type_relabeled"], 0) + 1

# ---------------------------------------------------------------------------
# 5. 落盘 (两遍写 + fingerprint 自指, 沿 d4 / result_v3 / dataset v1.2 同一惯例)
# ---------------------------------------------------------------------------
result = {
    "schema": "v4_pi_cot_v3_dataset_addendum_d4_relabel/1",
    "task": "F2 D4 标注重标落地 (数据面修正注记件)",
    "formal_judgment": False,
    "type": "addendum_of_record_relabel_note",
    "purpose": "把 E-42.2 已登记的 5 件 judge_type 重标结论落成数据面可引用的注记件; 原 d4 件 0 改写 / 0 合并 / 0 覆盖",
    "generated_utc": TS_FROZEN,
    "base_file": {
        "path": "results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json",
        "sha12": sha12(D4),
        "bytes": D4.stat().st_size,
        "supplement_count": d4.get("supplement_count"),
        "fingerprint_self_hash_after_birth_in_base": d4.get("fingerprint_self_hash_after_birth"),
        "base_self_hash_drift": sha12(D4) != (d4.get("fingerprint_self_hash_after_birth") or "").upper(),
        "base_self_hash_drift_note": "沿 E-42.5 ③ 登记: 漂移未记因, 本件 0 代填原因, 仅如实并记 (base 件自指字段 B18FF4177289 vs 盘上实测 CBF60A630C9F)",
    },
    "anchor_sha_verification": {
        "errata": {"path": "docs/V3X/TRAE_V3_ASSET_ERRATUM_2026_09_23.md",
                   "sha12_actual": sha12(ERRATA), "bytes": ERRATA.stat().st_size},
        "questionnaire_v1": {"path": TAXONOMY["source_path"], "sha12_actual": TAXONOMY["source_sha12"]},
        "executor_base": {"path": "results/_v4_pi_cot_v3_ruleset_v3_executor.py",
                          "sha12_actual": sha12(EXEC_BASE), "bytes": EXEC_BASE.stat().st_size},
        "executor_r1": {"path": "results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py",
                        "sha12_actual": sha12(EXEC_R1), "bytes": EXEC_R1.stat().st_size},
    },
    "judge_type_taxonomy_basis": TAXONOMY,
    "decision_source": DECISION_SOURCE,
    "relabel_table": items,
    "accuracy": {
        "n_items": len(items),
        "n_unchanged": n_same,
        "n_changed": len(items) - n_same,
        "accuracy_original_vs_relabeled": f"{n_same}/{len(items)}",
        "accuracy_note": "仅 D4_Q5 (J3) 重标后与原标注一致 = 1/5; 与 E-42.2 登记字面一致 ✓",
    },
    "judge_type_distribution": {
        "before": orig_dist,
        "after_relabel": new_dist,
        "delta_note": "J5 0→2 (Q1,Q3); J6 3→0; J1 0→1 (Q2); J4 0→1 (Q4); J3 2→1 (Q5); J2 0→0",
    },
    "note_1_no_d2_d3_precedent": {
        "claim_under_test": "「判据类型 J1-J6 由 worker 按 D2/D3 既有惯例标注」是否有先例可依 (沿 E-42.2 附注一字面)",
        "claim_file": "results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json §supplements[*].judgment_axis_deferral / §verbatim_policy 字面",
        "measured": {"n_supplements_total": tot, "n_with_judge_type_field": with_jt, "per_file": per_file},
        "conclusion": "「D2/D3 既有惯例」**实测不存在**: 9 件 v2 补充件共 35 条, 带 judge_type 字段者 0 条 → executor 对无该字段者落 J_unknown",
        "counting_convention_note": "派工单 / verifier 呈文字面记 32 条 (D2/D3 8 波 × 4 条), 本棒实测 35 条 (含 D1_supp 3 条), 差额 3 = D1_supp 3 件; 两口径如实并记, 以本棒实测 35 条为全集 (沿 E-42.2 附注一字面)",
        "executor_fallback_line": "executor load_addendum_event_v3(): 无 judge_type 字段者 ev['judge_type'] = 'J_unknown'",
    },
    "note_2_briefing_transcription_error": {
        "item": "J4",
        "briefing_literal": "派工单曾将 J4 转写为「质量」",
        "authoritative_literal": "questionnaire_v1 §1 字面 J4 = 风险（铁律·红线·安全边界）",
        "resolution": "以 questionnaire_v1 §1 字面为准; 本条为转写错登记 (不改派工单原件, 不代填)",
        "registration_surface": "勘误链 §22.31.2 E-42.2 附注二",
    },
    "root_cause_note": {
        "statement": "原 D4 5 件 judge_type 准确率 1/5 的构造面根因 = 标注时声称依循的「D2/D3 既有惯例」实测不存在 (0/35 条带 judge_type), 故 5 件实为无先例的 worker 自行标注",
        "evidence": ["原 d4 §verbatim_policy 与 §supplements[*].judgment_axis_deferral 字面「判据类型 J1-J6 由 worker 按 D2/D3 既有惯例标注」",
                     "本棒实测 9 件 v2 补充件 35 条 0 条带 judge_type"],
        "grading": "本棒推断 (沿核心准则「诚实的根因是不误导」: 区分「标注错」与「无先例可依」两类死因, 不笼统计为标注质量问题)",
        "not_fabricated": "verifier 双复核呈文未落盘, 本棒未见其归因原文; 上列为本棒基于盘上字面 + 实测的推断, 非呈文转述",
    },
    "downstream_impact_not_executed": {
        "statement": "若本重标将来在 dataset v1.3 落地, 4/5 件 judge_type 变 → feats_v3 的 judge_type_J1/J4/J5/J6 特征值变 → 决策树训练面变 → result_v3 的 K-V3-* 读数与 verdict_v3 结论均可能变",
        "executed": False,
        "why_not_executed": "本棒派工单范围 = 出数据面修正注记件; 且铁律禁擅改既有 result_v3 / verdict_v3 (须 PI 拍板 + 新名件 + 重跑留痕)",
        "affected_feature_keys": ["judge_type_J1", "judge_type_J4", "judge_type_J5", "judge_type_J6"],
        "note": "E-42.3 已登记 judge_type_J5 为常量特征 (n_distinct=1, D4 无一启用 J5); 本重标落地后将使 D4 启用 J5 (2 件), 该死特征是否消解取决于是否重跑 —— 本棒 0 重跑, 0 预判数值",
    },
    "constraint": {
        "no_llm": True, "no_proxy": True, "no_gateway": True,
        "key_never_on_disk": True, "key_never_in_prompt_json_log": True,
        "no_v1_v2_v3_frozen_touch": True,
        "no_existing_file_overwritten": True,
        "no_derived_json_merge": True,
        "no_threshold_tampering": True,
        "no_rerun_of_result_v3": True,
        "explicit_boolean_naming": True,
        "s_40_discipline_followed": True,
    },
    "touch_policy_summary": {
        "d4_base_0_byte_change": True,
        "d4_base_sha12_unchanged": sha12(D4) == "CBF60A630C9F",
        "errata_0_byte_change": True,
        "questionnaire_v1_0_byte_change": True,
        "no_portrait_declaration": "本件为判据类型标注修正, 不做 PI 行为预测或个人模型 (沿 v3 dataset 非画像声明)",
    },
    "honesty_note": (
        "本件 = D4 重标的数据面注记件 (非 dataset v1.3, 非新实验跑, formal_judgment=false). "
        "已: (a) 原 d4 件 CBF60A630C9F / 20,194 B 实测 0 改写 0 合并 0 覆盖; "
        "(b) 判型基准取 questionnaire_v1 §1 盘上字面逐行读取 (非派工单转写); "
        "(c) 5 件逐件新旧标注 + option_chosen + PI 出处原文 + 拍板出处链 全登记; "
        "(d) 附注一「D2/D3 既有惯例不存在」本棒逐件实测复核 (9 件 35 条 0 条带 judge_type) ✓; "
        "(e) 附注二 转写错 (J4=风险 非「质量」) 已登记; "
        "(f) 归因段明确标为「本棒推断」并列出呈文不落盘这一边界. "
        "未触: d4 原件 / 勘误链 / questionnaire_v1 / v1·v2·v3 资产 / result_v3 / verdict_v3 任何既有件. "
        "0 LLM / 0 key 落盘 / 0 派生 JSON 合并 / 0 擅调阈值 / 0 重跑 / 0 覆盖既有件. "
        "老实交代: (i) 拍板出处只能追到勘误链 §22.31.2 登记面, verifier 双复核呈文本棒未见 (不落盘), 故本件不转述呈文原意; "
        "(ii) D4_Q2 的 J1/J4 二码可辩, 本件以 J1 为主记 + J4 并记 (沿 E-42.2 字面), 未代 PI 裁断; "
        "(iii) 归因「无先例可依」为本棒推断, 非呈文结论; "
        "(iv) 本件 0 执行落地重跑, 连带面只登记不预判数值. "
        "succeeded ≠ 跑完 = 以盘上 SHA-12 落盘核验为准."
    ),
    "fingerprint_self_hash_post_birth": "0" * 12,
    "metadata": {
        "author": "Mavis 团队 worker",
        "date": "2026-09-27",
        "encoding": "UTF-8 (no BOM)",
        "line_ending": "LF",
        "track": "Track 1 (0 LLM / 0 proxy / 0 gateway)",
        "type": "v3_dataset_addendum_d4_relabel_note",
        "agent": "worker (执行类)",
        "skill": "scientific-research-workflows:experimental-design (@scientific-research-workflows)",
        "plugin": "@scientific-research-workflows",
        "generator": ".tmp/_run_d4_relabel_addendum.py",
        "authored_by_branch_session": "mvs_9b81aec9bc834fe188f6b3850301bd8f",
        "signature_line": "Mavis 团队 worker 出件 | 2026-09-27",
    },
}

OUT.write_bytes(json.dumps(result, ensure_ascii=False, indent=2).encode("utf-8"))
sha_birth = sha12(OUT)
result["fingerprint_self_hash_post_birth"] = sha_birth
OUT.write_bytes(json.dumps(result, ensure_ascii=False, indent=2).encode("utf-8"))

print("=== D4 relabel addendum ===")
print("原 d4 SHA-12 :", sha12(D4), D4.stat().st_size, "B (须仍 = CBF60A630C9F / 20194)")
print("勘误链 SHA-12 :", sha12(ERRATA), ERRATA.stat().st_size, "B")
print("questionnaire_v1 :", TAXONOMY["source_sha12"])
print()
for it in items:
    flag = "同" if not it["changed"] else "改"
    print(f"  [{flag}] {it['q_id']:7s} {it['judge_type_original']} -> {it['judge_type_relabeled']}"
          f"{' (+' + it['judge_type_relabeled_alternative'] + ' 可辩)' if it['judge_type_relabeled_alternative'] else ''}")
print(f"  准确率: {n_same}/{len(items)}")
print("  分布 before:", orig_dist)
print("  分布 after :", new_dist)
print()
print("=== 出件 ===")
print("path      :", OUT)
print("bytes     :", OUT.stat().st_size)
print("sha12 birth:", sha_birth, " actual:", sha12(OUT))
print("DONE.")
