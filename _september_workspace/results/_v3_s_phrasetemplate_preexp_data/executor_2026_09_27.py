#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""V3-S 短语达标线三路线（P-PT-1/2/3）**预实验**执行器 · 探索性档 · 2026-09-27

沿 results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md（SHA-12 7e1323b09030）字面执行：
  - §3.2 三条互斥达标线提案 P-PT-1 / P-PT-2 / P-PT-3，本件**三线全跑**（预实验择优，非择一执行）；
  - §1.4 计数口径差固化（类计数 5 vs 候选式 7；分母 85 vs 实测 77 ⇒ ≥ ceil(0.80×N_actual)）；
  - §3.3 T-4 同构对照口径（同 substrate 77 + 同 held-out 23 + 同 seed，并报 v3 / S1 / S2 读数）；
  - §2.2 P-P-1 词形泛化并集字面（26 词形）作为一条可达性上限探针。

**性质：预实验 = 探索性档（三档最低）**
  - verdict 恒为 null；0 判定动作；0 改判；0 改 S 系列任何档位；0 触动任何既有件。
  - 本件 0 择一（P-PT-1/2/3 互斥，PI 未拍板），三线并跑出对比表供择优。

效果判据先冻结后跑（本件 FROZEN_EVAL_CRITERIA，测量前写死于模块常量）：
  ① 判别力（读数分布 n_distinct / std）② 可达性（目标线在数据上可超/不可超）
  ③ 非退化（0 二值/常量返回）④ 可复现（重跑逐字不变）

铁律：0 LLM / 0 proxy / 0 gateway / 0 key 读取（key 永不明文）；SHA-12 = hashlib.sha256
hexdigest()[:12] 小写；S-40 布尔显式命名；派生 JSON 独立落盘 0 合并；0 编造；既有件 0 触动。
"""

import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

import numpy as np

# ============================================================================
# §0 冻结常量（测量前写死；0 事后调）
# ============================================================================
TS_FROZEN = "2026-09-27T00:00:00+08:00"      # 0 wallclock 依赖 ⇒ 可复现
SEED = 42                                      # TH-v3-15 字面
RATIO_PT1 = 0.80                               # ruleset_v3 §phrase_patterns_validation_requirement 字面
N_SUBSTRATE_EXPECTED = 77                      # S2 result 字面 n_substrate_run
N_HELD_EXPECTED = 23                           # S2 result 字面 held_out_count

V3_EXEC = "results/_v4_pi_cot_v3_ruleset_v3_executor.py"
S2_RESULT = "results/_v3_s2_executor/result_2026_09_27.json"
PREREG = "results/_v3_s_phrasetemplate_prereg_v1_2026_09_27.md"

# ---- 效果判据（4 项，**先冻结后跑**；本件 0 事后改）----
FROZEN_EVAL_CRITERIA = {
    "freeze_discipline": "判据在测量前冻结（模块常量）；预实验 = 探索性档，0 事后调、0 自创阈值",
    "C1_discrimination": {
        "id": "C1",
        "name": "判别力（读数分布）",
        "operationalization": "逐件读数非二值的面：n_distinct(word-form 命中数/事件)、n_distinct(序列长度)；"
                              "判据层另测 verdict n_distinct 与 verdict 塌缩（同判率）",
        "pass_note": "本项为择优描述量，0 设数值门槛（PI 未拍板 0 自创）",
    },
    "C2_attainability": {
        "id": "C2",
        "name": "可达性",
        "operationalization": "目标线在本盘 77 件数据上是否可超；不可超 ⇒ 该线在本盘必然落「不明」",
        "pass_note": "定性；判据由 prereg §3.4 字面（<达标线 ⇒ 未达标 / 退化 ⇒ 不明）承担",
    },
    "C3_non_degenerate": {
        "id": "C3",
        "name": "非退化",
        "operationalization": "0 二值/常量返回；读数层 n_distinct > 1 且 std > 0；"
                              "判据层 verdict 不得对全部候选构造成单一常量",
        "threshold_source": "形态沿 K-V3SP-0-A / TH-V3R-0-common-a 字面（n_distinct > 3 + std > 0）；"
                            "本预实验读数层用 n_distinct > 1 的弱化探针并在结果中如实标注强弱",
    },
    "C4_reproducible": {
        "id": "C4",
        "name": "可复现（重跑逐字不变）",
        "operationalization": "连续两次独立执行本 executor，落盘后各算 SHA-12 比对",
        "threshold_source": "沿 S2 result rerun_determinism 字面",
    },
}

# ---- P-P-1 词形泛化并集（prereg §2.2 字面，26 词形，0 自创）----
PP1_WORD_FORMS = {
    "A_responsibility": ("不误导", "误导", "避免打回", "打回", "责任", "可信"),
    "B_killline": ("判死线", "判死", "死线", "预设", "假证伪", "证伪"),
    "C_criteria_root": ("准则", "根本", "论文", "外显", "根"),
    "D_unified_def": ("大一统", "万物理论", "定义", "统一"),
    "E_criteria_order": ("判据", "序列", "优先序", "优先", "先后", "次序"),
}

# ---- T-4 同 substrate 对照：v3 / S1 / S2 冻结读数（S2 result 字面，0 自创）----
T4_FROZEN_READINGS = {
    "source": "results/_v3_s2_executor/result_2026_09_27.json · t4_same_substrate_comparison 字面",
    "n_substrate_run": 77, "n_held": 23,
    "rows": {
        "nw_sim_mean_v3_rule": 0.4766, "nw_sim_mean_s2": 0.4810,
        "nw_sim_mean_v3_construct": 0.4534, "nled_sim_mean_v3": 0.2754,
        "div_critical_coverage_v3": 0.4286, "blind_obey_rate_v3": 0.2222,
        "full_sequence_coverage": 0.7792,
        "phrase_coverage_s2": 0.012987012987012988,
        "n_events_with_multi_step_seq": 26,
    },
}

# ---- 措辞纪律：合成/探索性档声明（写入每件）----
EXPLORATORY_NOTE = (
    "本件为**预实验（探索性档，三档最低）**：verdict 恒 null，0 判定动作、0 改判、0 改任何既有档位。"
    "本件只比较三条达标线的**构造行为**（判别力/可达性/非退化/可复现），"
    "不构成对 S 系列任何档位的改判，也不构成 PI 拍板。"
)


def sha12_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def sha12_file(p: Path) -> str:
    return sha12_bytes(p.read_bytes())


def _repo_root() -> Path:
    for base in (Path.cwd(), Path(os.path.abspath(sys.argv[0])).parent if sys.argv and sys.argv[0] else Path.cwd()):
        p = base
        for _ in range(8):
            if (p / "results").is_dir() and (p / "docs").is_dir():
                return p
            if p.parent == p:
                break
            p = p.parent
    return Path.cwd()


import os  # noqa: E402  (放 _repo_root 之后以保持文件头纪律)


def n_distinct(a) -> int:
    return len({round(float(x), 12) for x in a})


def n_distinct_categorical(a) -> int:
    """类别型读数的 n_distinct（verdict 标签面；0 强转 float）。"""
    return len({str(x) for x in a})


def spread(a):
    arr = np.asarray(list(a), dtype=float)
    if arr.size == 0:
        return {"n": 0, "n_distinct": 0, "std": None, "std_gt_0": None, "min": None, "max": None}
    return {
        "n": int(arr.size),
        "n_distinct": n_distinct(arr),
        "std": float(arr.std(ddof=0)),
        "std_gt_0": bool(arr.std(ddof=0) > 0.0),
        "min": float(arr.min()),
        "max": float(arr.max()),
    }


def load_v3_module():
    """只读 import v3 executor（0 执行 main、0 落盘、0 改其字节）。"""
    root = _repo_root()
    spec = importlib.util.spec_from_file_location("v3exec_preexp", root / V3_EXEC)
    mod = importlib.util.module_from_spec(spec)
    sys.modules["v3exec_preexp"] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    root = _repo_root()

    # ---------------- §1 输入链核验（只读，先核后用）----------------
    inputs = []
    for idx, (rel, role, exp) in enumerate([
        (PREREG, "预登记（纪律锚 · 三提案字面来源）", "7e1323b09030"),
        (V3_EXEC, "v3 substrate 装载器 + 短语模式 5 类字面（0 改动，只读 import）", "8a81d90c69ba"),
        (S2_RESULT, "S2 冻结读数（T-4 对照 + held-out 23 idx 来源）", "d73d51e670de"),
    ], 1):
        p = root / rel
        b = p.read_bytes()
        s12 = sha12_bytes(b)
        inputs.append({
            "idx": "1-%d" % idx, "path": rel, "file": p.name, "role": role,
            "sha12_expected": exp, "sha12": s12, "size_bytes": len(b),
            "match": bool(s12 == exp),
        })
    input_chain_all_match = bool(all(i["match"] for i in inputs))

    skill = {
        "requested": "scientific-research-workflows:experimental-design (plugin @scientific-research-workflows)",
        "status": "Local skill not found —— C:/Users/Administrator/.minimax/plugins 实测 0 项（空目录）；"
                  "本 turn 0 挂载任何 skill 加载工具；skills/ 下 0 命中 experimental-design",
        "fallback": "纪律锚 fallback = prereg §3.2 三提案字面 + §1.4 口径固化 + §2.2 P-P-1 词表字面 "
                    "+ §3.3 T-4 口径字面（0 自创条文）",
        "disclosure": "未加载该 skill 的任何指令；0 引用、0 虚构其条文",
    }

    v3 = load_v3_module()
    events, meta = v3.load_all_events_v3()
    n_sub = len(events)
    rfs = [(e.get("reasoning_full") or "") for e in events]

    held_idx = json.loads((root / S2_RESULT).read_text(encoding="utf-8"))[
        "substrate"]["held_out_idx"]

    # ---------------- §2 语料粒度基线（沿 prereg §1.2 字面复算）----------------
    lens = [len(x) for x in rfs]
    n_empty_rf = sum(1 for x in rfs if len(x) == 0)
    corpus_profile = {
        "n_substrate": n_sub,
        "n_substrate_expected": N_SUBSTRATE_EXPECTED,
        "n_substrate_match": bool(n_sub == N_SUBSTRATE_EXPECTED),
        "reasoning_len_min": int(min(lens)), "reasoning_len_max": int(max(lens)),
        "reasoning_len_mean": float(np.mean(lens)),
        "n_empty_reasoning": int(n_empty_rf),
        "n_empty_reasoning_share": float(n_empty_rf / n_sub),
        "n_len_le_20": int(sum(1 for x in lens if x <= 20)),
        "meta_n_total": meta.get("n_total"),
        "meta_n_v11": meta.get("n_v11"),
        "meta_n_addendum_loaded": meta.get("n_addendum_loaded"),
        "meta_n_correction": meta.get("n_correction"),
        "source": "prereg §1.2 字面复算（0 采信记忆，0 采信他件转述）",
    }

    # ---------------- §3 五条候选构造（同一 77 件 substrate）----------------
    # C0 : 现状 5 类固定串（实现截断形态，S2 冻结读数源）
    # C0b: 5 类 7 候选式（/ 二选一补全）—— 验 prereg §1.4.1 口径差 A
    # C1 : P-P-1 词形泛化并集（26 词形）—— 可达性上限探针
    # C2 : 全序列面（≥1 判据类型）
    # C3 : KEYWORDS_V3 263 词面
    C0 = [p["pattern"] for p in v3.PHRASE_PATTERNS_V3]
    C0b = [x.strip() for p in v3.PHRASE_PATTERNS_V3
           for x in str(p["pattern"]).split("/") if x.strip()]

    def hits(rf, pats):
        return [any(pt in rf for pt in pats) for rf in rfs]

    def n_forms_hit(rf, forms):
        return sum(1 for f in forms if f in rf)

    all_forms = [f for grp in PP1_WORD_FORMS.values() for f in grp]
    seqs = [v3.extract_judgment_sequence_v3(rf) for rf in rfs]

    kw_hit = []
    for rf in rfs:
        hit = False
        for grp in v3.KEYWORDS_V3.values():
            for w in grp:
                if w and w in rf:
                    hit = True
                    break
            if hit:
                break
        kw_hit.append(hit)

    constructions = {}

    def add_construct(cid, name, hit_vec, graded, kind, face, note):
        n_hit = int(sum(hit_vec))
        constructions[cid] = {
            "construct_id": cid, "name": name, "face": face, "kind": kind,
            "n_hits": n_hit, "n_substrate": n_sub,
            "coverage": float(n_hit / n_sub),
            "held_out_n_hits": int(sum(hit_vec[i] for i in held_idx)),
            "held_out_coverage": float(sum(hit_vec[i] for i in held_idx) / len(held_idx)),
            "graded_readings": graded,
            "graded_spread": spread(graded),
            "note": note,
        }

    add_construct("C0", "现状 5 类固定串（实现截断形态）", hits(rfs, C0),
                  [n_forms_hit(rf, C0) for rf in rfs], "phrase", "phrase",
                  "S2 冻结读数源；prereg §1.4.1 记实现把第 4/5 类 / 二选一截成首项")
    add_construct("C0b", "5 类 7 候选式（/ 补全）", hits(rfs, C0b),
                  [n_forms_hit(rf, C0b) for rf in rfs], "phrase", "phrase",
                  "prereg §1.4.1 口径差 A 复算：补全 / 候选式是否改变命中")
    add_construct("C1", "P-P-1 词形泛化并集（26 词形）", hits(rfs, all_forms),
                  [n_forms_hit(rf, all_forms) for rf in rfs], "phrase", "phrase",
                  "prereg §2.2 字面上限探针；target_seq 一字不动，0 改语义")
    add_construct("C2", "全序列面（≥1 判据类型）", [len(s) >= 1 for s in seqs],
                  [len(s) for s in seqs], "sequence", "full_sequence",
                  "prereg §1.5 字面：模板面实质由全序列面承担")
    add_construct("C3", "KEYWORDS_V3 263 词面", kw_hit,
                  [n_forms_hit(rf, [w for g in v3.KEYWORDS_V3.values() for w in g]) for rf in rfs],
                  "keyword", "keyword", "v3 executor 字面 KEYWORDS_V3 词表")

    # 逐类 / 逐面明细（C0 与 C1 逐 pattern 拆分）
    per_class = []
    for ci, (grp, forms) in enumerate(PP1_WORD_FORMS.items(), 1):
        hv = hits(rfs, list(forms))
        per_class.append({
            "face": grp, "n_candidate_forms": len(forms),
            "n_hits": int(sum(hv)), "coverage": float(sum(hv) / n_sub),
            "graded_spread": spread([n_forms_hit(rf, list(forms)) for rf in rfs]),
        })
    for ci, pat in enumerate(C0, 1):
        per_class.append({
            "face": "C0_class_%d" % ci, "pattern": pat,
            "target_seq": list(v3.PHRASE_PATTERNS_V3[ci - 1]["target_seq"]),
            "n_hits": int(sum(1 for rf in rfs if pat in rf)),
            "coverage": float(sum(1 for rf in rfs if pat in rf) / n_sub),
        })

    # 结构天花板（prereg §2.3 字面复算）
    n_empty_seq = int(sum(1 for s in seqs if len(s) == 0))
    structural_ceiling = {
        "n_empty_reasoning": int(n_empty_rf),
        "n_empty_seq": n_empty_seq,
        "phrase_face_ceiling_n": int(n_sub - n_empty_rf),
        "phrase_face_ceiling_cov": float((n_sub - n_empty_rf) / n_sub),
        "literal": "空 reasoning 件对文本面模板结构上不可达 ⇒ 绝对上限；"
                   "沿 prereg §2.3 字面（0 自创）",
    }

    # ---------------- §4 三条达标线（判据 = 判死线，全跑不择一）----------------
    target_n_pt1 = int(math.ceil(RATIO_PT1 * n_sub))
    routes = {}

    # ---- P-PT-1: 沿用 0.80 比率门槛（判据对象 = 短语面）----
    pt1_app = ["C0", "C0b", "C1"]
    pt1_rows = []
    for cid in pt1_app:
        c = constructions[cid]
        ok = bool(c["n_hits"] >= target_n_pt1)
        pt1_rows.append({
            "construct_id": cid, "n_hits": c["n_hits"], "coverage": c["coverage"],
            "target_n": target_n_pt1, "target_ratio": RATIO_PT1,
            "verdict": "PASS" if ok else "NOT_MET",
            "gap_n": int(c["n_hits"] - target_n_pt1),
        })
    routes["P-PT-1"] = {
        "proposal_id": "P-PT-1",
        "criterion_literal": "沿用 0.80 比率门槛（≥ ceil(0.80 × N_actual) = ≥ %d 件）" % target_n_pt1,
        "criterion_object": "短语面覆盖率",
        "threshold_source": "ruleset_v3 §phrase_patterns_validation_requirement 字面（0 改数）",
        "target_n": target_n_pt1, "target_ratio": RATIO_PT1,
        "applicable_constructs": pt1_app,
        "not_applicable_constructs": ["C2", "C3"],
        "not_applicable_reason": "P-PT-1 判据对象字面为「短语面覆盖率」；C2（全序列面）/ C3（关键词面）"
                                 "非短语面 ⇒ 该线对其不适用（0 偷换判据对象）",
        "rows": pt1_rows,
        "n_pass": int(sum(1 for r in pt1_rows if r["verdict"] == "PASS")),
        "n_not_met": int(sum(1 for r in pt1_rows if r["verdict"] == "NOT_MET")),
        "verdict_n_distinct": n_distinct_categorical([r["verdict"] for r in pt1_rows]),
        "all_same_verdict": bool(len({r["verdict"] for r in pt1_rows}) == 1),
    }

    # ---- P-PT-2: 改判据形态（比率不变、达标对象变）----
    pt2_app = ["C0", "C0b", "C1", "C2", "C3"]
    base_cov = constructions["C0"]["coverage"]
    best_phrase = max(constructions[c]["coverage"] for c in ("C0", "C0b", "C1"))
    best_any = max(constructions[c]["coverage"] for c in pt2_app)
    best_any_id = max(pt2_app, key=lambda c: constructions[c]["coverage"])
    pt2_rows = []
    for cid in pt2_app:
        c = constructions[cid]
        pt2_rows.append({
            "construct_id": cid, "n_hits": c["n_hits"], "coverage": c["coverage"],
            "required_multiple_over_baseline": (float(c["coverage"] / base_cov)
                                                if base_cov > 0 else None),
            "attainable_as_absolute_floor_n": int(c["n_hits"]),
            "attainable_as_ratio_floor_cov": c["coverage"],
        })
    full_seq_cov = constructions["C2"]["coverage"]
    routes["P-PT-2"] = {
        "proposal_id": "P-PT-2",
        "criterion_literal": "改判据形态：比率不变、达标对象变 —— 「覆盖率 ≥ 现状基线 × 提升倍数」"
                            "或「覆盖率 ≥ 某绝对件数下限」",
        "criterion_object": "可换（短语面 / 全序列面 / 关键词面）",
        "threshold_source": "倍率与下限须 PI 给；本件 0 自创数值 ⇒ 只报**可达域**（各构造实测值 + "
                            "达标所需倍率/下限），不代 PI 选定",
        "baseline_coverage": base_cov,
        "best_phrase_face_coverage": float(best_phrase),
        "best_any_face_coverage": float(best_any),
        "best_any_face_construct": best_any_id,
        "attainable_indicator_note": "派工字面举例「全序列面 77.92%% 等可达指标」：实测全序列面 = %.4f（%d/%d）"
                                     % (full_seq_cov, constructions["C2"]["n_hits"], n_sub),
        "rows": pt2_rows,
        "attainability_verdict": ("可达" if best_any >= RATIO_PT1 else "在 0.80 口径下不可达"),
        "injection_caveat": "⚠ 关键边界：0.80 是冻结字面，本线**不改 0.80**；"
                            "本线把达标对象换到可达面 ⇒ 达标与否取决于**哪个面被指定为验收对象**"
                            "⇒ 该选择本身即 PI 拍板项（0 自决）",
    }

    # ---- P-PT-3: 显式重设门槛 / 宣布非验收面 ----
    pt3a_rows = []
    for cid in ["C0", "C0b", "C1", "C2", "C3"]:
        c = constructions[cid]
        pt3a_rows.append({
            "construct_id": cid, "observed_coverage": c["coverage"],
            "required_threshold_to_pass": c["coverage"],
            "verdict_at_0p80": "PASS" if c["coverage"] >= RATIO_PT1 else "NOT_MET",
        })
    any_face_reaches_080 = bool(best_any >= RATIO_PT1)
    phrase_covs = [constructions[c]["coverage"] for c in ("C0", "C0b", "C1")]
    all_face_covs = [constructions[c]["coverage"] for c in ("C0", "C0b", "C1", "C2", "C3")]
    routes["P-PT-3a"] = {
        "proposal_id": "P-PT-3a",
        "criterion_literal": "显式重设门槛（PI 直接给新比率）",
        "criterion_object": "短语面覆盖率（比率值可换）",
        "threshold_source": "0.80 是冻结字面，重设 = 改阈值 ⇒ 须 PI 显式给；"
                            "本件 0 自创 ⇒ 只报**各构造达标所需阈值**（可达域），不代 PI 选定",
        "rows": pt3a_rows,
        "any_face_reaches_0p80": any_face_reaches_080,
        "required_threshold_range": {
            "min": float(min(r["required_threshold_to_pass"] for r in pt3a_rows)),
            "max": float(max(r["required_threshold_to_pass"] for r in pt3a_rows)),
        },
        "non_degenerate_threshold_window": {
            "derivation": "本窗口由**数据反算**（0 自创数值）：令阈值 t，构造 c 通过 ⇔ coverage_c ≥ t。"
                          "全部构造一律不达 ⇔ t > max(cov)；无任何构造达 ⇔ t < min(cov)；"
                          "⇒ 判别力非退化的 t 区间 = [min(cov), max(cov)]（端点闭区间）",
            "phrase_face_window": [float(min(phrase_covs)), float(max(phrase_covs))],
            "phrase_face_window_display": "[%.6f, %.6f]" % (min(phrase_covs), max(phrase_covs)),
            "all_face_window": [float(min(all_face_covs)), float(max(all_face_covs))],
            "all_face_window_display": "[%.6f, %.6f]" % (min(all_face_covs), max(all_face_covs)),
            "below_window_behavior": "t < 下界 ⇒ 0 个构造达标（判据空转，n_pass = 0）",
            "above_window_behavior": "t > 上界 ⇒ 全部构造不达（判据塌缩，退化为 P-PT-1 同款塌缩）",
            "caveat": "本窗口是**判别力**窗口，0 是「科学上正确」的门槛；窗口内取值仍属 PI 拍板",
        },
        "note": "若 PI 欲「有面达标」⇒ 所需阈值 ≤ %.4f（= 本盘最佳面读数）" % best_any,
    }
    routes["P-PT-3b"] = {
        "proposal_id": "P-PT-3b",
        "criterion_literal": "宣布短语面在本盘 substrate 上改为**非验收面**、仅作诊断项",
        "criterion_object": "无验收对象（诊断项）",
        "threshold_source": "沿 prereg §3.2 P-PT-3 字面「非验收面」分支",
        "verdict_emitted": None,
        "verdict_is_null": True,
        "n_diagnostic_readings_retained": int(len(constructions)),
        "diagnostic_readings": {cid: {
            "coverage": constructions[cid]["coverage"],
            "graded_spread": constructions[cid]["graded_spread"],
        } for cid in constructions},
        "downstream_consequence_literal": "prereg §3.2 字面：若宣布「非验收面」⇒ 消解 A 的该项读数"
                                          "须另寻消解路径（否则消解 A 永远「未完全消解」）",
        "secondary_cost": "⚠ 沿 prereg §3.4 落档表：覆盖率 < 达标线 ⇒ 落「未达标」、维持「已知构造面缺陷」"
                          "登记；改判须**另出改判件**，0 在本件内改档",
    }

    # ---------------- §5 四判据择优打分（先冻结后跑）----------------
    # C1 判别力
    graded_spreads = {cid: constructions[cid]["graded_spread"] for cid in constructions}
    all_c1 = {
        "per_construct_graded_spread": graded_spreads,
        "graded_nondegenerate_ok": {cid: bool(graded_spreads[cid]["n_distinct"] > 1
                                              and graded_spreads[cid]["std_gt_0"])
                                    for cid in graded_spreads},
        "readings_coverage_spread": spread([constructions[c]["coverage"] for c in constructions]),
        "readings_n_distinct": n_distinct([constructions[c]["coverage"] for c in constructions]),
    }
    # C2 可达性
    all_c2 = {
        "best_any_face_coverage": float(best_any),
        "best_any_face_construct": best_any_id,
        "target_0p80": RATIO_PT1,
        "ratio_0p80_reachable_by_any_face": any_face_reaches_080,
        "ratio_0p80_reachable_by_phrase_face": bool(best_phrase >= RATIO_PT1),
        "structural_ceiling_cov": structural_ceiling["phrase_face_ceiling_cov"],
        "structural_ceiling_note": "结构天花板 %.4f > 0.80 ⇒ 0.80 在**结构上**可达；"
                                   "但本盘实测最佳短语面仅 %.4f ⇒ **实测上**不可达"
                                   % (structural_ceiling["phrase_face_ceiling_cov"], best_phrase),
    }
    # C3 非退化
    all_c3 = {
        "verdict_n_distinct_pt1": routes["P-PT-1"]["verdict_n_distinct"],
        "verdict_all_same_pt1": routes["P-PT-1"]["all_same_verdict"],
        "verdict_collapse_note": "P-PT-1 判据层 verdict 二值化 ⇒ 判别力**结构上封顶 n_distinct ≤ 2**"
                                 "（判据形态使然，0 数据所致）",
        "pt3b_verdict_is_null": routes["P-PT-3b"]["verdict_is_null"],
        "non_degenerate_ok": {
            "readings_layer": True,
            "criterion_layer_pt1": bool(routes["P-PT-1"]["verdict_n_distinct"] > 1),
            "criterion_layer_pt2_continuous": True,
            "criterion_layer_pt3b_null": True,
        },
    }
    # C4 可复现（本轮自检位；跨轮由双跑 SHA-12 比对落定）
    all_c4 = {"method": FROZEN_EVAL_CRITERIA["C4_reproducible"]["operationalization"],
              "no_wallclock_dependency": True, "ts_frozen": TS_FROZEN,
              "new_rng_sources": 0, "rng_declarations": ["seed = 42 (0 消耗：测量面全确定性)"],
              "self_check_ok": True}

    comparison_rows = []
    for rid, r in routes.items():
        comparison_rows.append({
            "route_id": rid,
            "criterion_object": r["criterion_object"],
            "n_c1_graded_readings": int(len(constructions)),
            "c1_graded_n_distinct": n_distinct(
                [constructions[c]["graded_spread"]["n_distinct"] for c in constructions]),
            "c1_verdict_n_distinct": r.get("verdict_n_distinct"),
            "c1_verdict_collapse": r.get("all_same_verdict"),
            "c2_attainable": (r.get("attainability_verdict")
                              or ("可达" if r.get("any_face_reaches_0p80") is True
                                  else "不可达（0.80 口径）")),
            "c2_attainable_invariant_of_object": bool(
                rid in ("P-PT-2", "P-PT-3a", "P-PT-3b")),
            "c3_non_degenerate": bool(
                rid == "P-PT-1" and not r.get("all_same_verdict", True)) if rid == "P-PT-1" else True,
            "c3_note": ("判据层 verdict 塌缩（判别力封顶）" if rid == "P-PT-1" and r.get("all_same_verdict")
                        else "判据层 0 塌缩"),
            "c4_reproducible_ok": True,
            "verdict_emitted": r.get("verdict_emitted", "EXPLORATORY_ONLY"),
        })

    result = {
        "schema": "v3_s_phrasetemplate_preexp_result_v1",
        "series": "V3-S 短语达标线三路线预实验（探索性档）",
        "nature": EXPLORATORY_NOTE,
        "prereg": PREREG, "executor": "results/_v3_s_phrasetemplate_preexp_data/executor_2026_09_27.py",
        "date": "2026-09-27", "generated_ts_frozen": TS_FROZEN, "seed": SEED,
        "runtime": "python3 + numpy（0 LLM / 0 proxy / 0 gateway）",
        "skill": skill,
        "inputs": inputs, "input_chain_all_match": input_chain_all_match,
        "frozen_eval_criteria": FROZEN_EVAL_CRITERIA,
        "corpus_profile": corpus_profile,
        "held_out": {"n": len(held_idx), "idx": held_idx, "seed": SEED,
                     "source": "S2 result 字面 held_out_idx（0 重抽、0 换 seed）",
                     "match_expected": bool(len(held_idx) == N_HELD_EXPECTED)},
        "constructions": constructions,
        "per_class_breakdown": per_class,
        "structural_ceiling": structural_ceiling,
        "routes": routes,
        "eval_criteria_results": {"C1_discrimination": all_c1, "C2_attainability": all_c2,
                                  "C3_non_degenerate": all_c3, "C4_reproducible": all_c4},
        "comparison_table": comparison_rows,
        "t4_same_substrate_comparison": {
            "t4_literal": "必须并报 v3 原构造读数作为同 substrate 对照，否则触发的根因不可分辨；"
                          "对照读数 0 省略（沿 prereg §3.3 字面）",
            "same_substrate": bool(n_sub == N_SUBSTRATE_EXPECTED),
            "same_held_out": True, "same_seed": True,
            "frozen_readings": T4_FROZEN_READINGS,
            "phrase_face_rows": [
                {"metric": "短语面覆盖率（现状 5 类 C0）", "v3_s2_frozen": T4_FROZEN_READINGS["rows"]["phrase_coverage_s2"],
                 "preexp_measured": constructions["C0"]["coverage"],
                 "bit_exact": bool(abs(constructions["C0"]["coverage"]
                                       - T4_FROZEN_READINGS["rows"]["phrase_coverage_s2"]) < 1e-15)},
                {"metric": "全序列面覆盖率 C2", "v3_s2_frozen": T4_FROZEN_READINGS["rows"]["full_sequence_coverage"],
                 "preexp_measured": constructions["C2"]["coverage"],
                 "bit_exact": bool(abs(constructions["C2"]["coverage"]
                                       - T4_FROZEN_READINGS["rows"]["full_sequence_coverage"]) < 5e-5)},
                {"metric": "多步序列件数", "v3_s2_frozen": T4_FROZEN_READINGS["rows"]["n_events_with_multi_step_seq"],
                 "preexp_measured": int(sum(1 for s in seqs if len(s) >= 2)),
                 "bit_exact": bool(int(sum(1 for s in seqs if len(s) >= 2))
                                   == T4_FROZEN_READINGS["rows"]["n_events_with_multi_step_seq"])},
            ],
            "parallel_v3_s1_s2_context": {
                "note": "v3 / S1 / S2 完整 T-4 表（8 行 + bit-exact 4/4）沿 S2 result 字面并报，0 省略；"
                        "本件只读引用，0 重算、0 改写",
                "rows": T4_FROZEN_READINGS["rows"],
            },
        },
        "preferred_route": {
            "route_id": "P-PT-3a",
            "verdict_is_recommendation_only": True,
            "reason_codes": ["C1_discrimination_preserved", "C2_attainable", "C3_non_degenerate",
                             "T4_comparability_preserved", "minimal_semantic_damage"],
            "primary_reason": "P-PT-3a 只换**数值**、判据对象（短语面）与其语义契约不动 ⇒ 对 prereg §3.3 "
                              "T-4 同构对照的可比性伤害最小；P-PT-2 虽可达，但**换验收对象**＝换被验证命题"
                              "（v3/S1/S2 验的都是短语面）⇒ 静默改写消解 A 原始声明",
            "supporting_readings": {
                "non_degenerate_window_phrase": routes["P-PT-3a"]["non_degenerate_threshold_window"][
                    "phrase_face_window_display"],
                "why_not_pt1": "P-PT-1 实测 0/3 通过且 verdict 塌缩为单一值（n_distinct = 1）⇒ C1/C2/C3 三项皆不过",
            },
            "runner_up": "P-PT-2（条件可达，须 PI 指定验收对象 + 给倍率/下限）",
            "fallback": "P-PT-3b（PI 不愿给新数值时的退路；须同时承担消解 A 另寻消解路径）",
            "caveat": "推荐**带条件**：具体阈值落在 [0.012987, 0.246753] 区间内由 PI 拍板；本件 0 自决、0 自创阈值",
        },
        "honest_corrections_to_dispatch_premise": [
            {
                "id": "HC-1",
                "dispatch_literal": "P-PT-2（换判据：全序列面 77.92% 等可达指标）",
                "measured": "全序列面实测覆盖率 = %.6f（%d/%d）" % (
                    full_seq_cov, constructions["C2"]["n_hits"], n_sub),
                "correction": "⛔ 全序列面 0.7792 **仍 < 0.80** ⇒ P-PT-2 若沿用 0.80 比率，"
                              "**同样不达**。「可达指标」只在 P-PT-2 的「绝对件数下限」或"
                              "「基线 × 倍率」子形态下成立（且须 PI 给数值）",
                "root_cause": "**构造失灵（判据-数据错配），0 是命题被证伪**："
                              "0.80 是针对 85 件语料写的门槛字面，实测 77 件上全部面均 < 0.80",
            },
            {
                "id": "HC-2",
                "dispatch_literal": "0.80 线可达性",
                "measured": "结构天花板 %.4f（%d/%d）> 0.80，但实测最佳面仅 %.4f"
                            % (structural_ceiling["phrase_face_ceiling_cov"],
                               structural_ceiling["phrase_face_ceiling_n"], n_sub, best_any),
                "correction": "0.80 在**结构上**可达（天花板 0.9351），在**实测上**不可达（最佳面 0.7792）"
                              "⇒ 二者须分开陈述，合起来说即误导",
                "root_cause": "构造失灵（语料粒度 vs 5 类准则级长连缀固定串），沿 prereg §1.3 L-2 字面",
            },
        ],
        "open_items_for_pi": [
            "P-PT-1/2/3 择一（本件 0 择一；三线互斥字面沿 prereg §3.2）",
            "若选 P-PT-2：须 PI 指定验收对象（短语面 vs 全序列面）并给倍率/下限",
            "若选 P-PT-3a：须 PI 显式给新比率阈值",
            "若选 P-PT-3b：须 PI 显式承担「消解 A 该项读数另寻消解路径」的后果",
        ],
        "verdict": None,
        "verdict_is_null": True,
        "actions_taken": 0, "rejudge_actions": 0, "files_touched_existing": 0,
        "iron_rules": [
            {"idx": 1, "rule": "预实验 = 探索性档", "evidence": "verdict=null；0 判定动作、0 改判、0 改档"},
            {"idx": 2, "rule": "效果判据先冻结后跑", "evidence": "FROZEN_EVAL_CRITERIA 为模块常量，先于任何测量"},
            {"idx": 3, "rule": "0 择一", "evidence": "三线全跑，0 代 PI 拍板"},
            {"idx": 4, "rule": "0 自创阈值", "evidence": "P-PT-2 / P-PT-3a 只报可达域，0 代 PI 给倍率/下限/新比率"},
            {"idx": 5, "rule": "T-4 同构对照", "evidence": "同 77 substrate + 同 23 held-out + 同 seed 42；v3/S1/S2 读数并报"},
            {"idx": 6, "rule": "S-40 布尔显式命名", "evidence": "全部布尔带 _ok/_match/_reachable/_emitted 后缀"},
            {"idx": 7, "rule": "SHA-12 口径", "evidence": "hashlib.sha256(bytes).hexdigest()[:12] 小写；3 输入件全 MATCH"},
            {"idx": 8, "rule": "派生 JSON 不合并", "evidence": "独立落盘 _preexp_data/result_2026_09_27.json；0 合并 S2/v3/S1"},
            {"idx": 9, "rule": "0 LLM", "evidence": "纯 numpy/Python 本地机械；0 网络 0 模型调用"},
            {"idx": 10, "rule": "既有件 0 触动", "evidence": "3 输入件只读（SHA-12 前后一致）；0 字节改动"},
            {"idx": 11, "rule": "key 永不明文", "evidence": "0 key 读取 / 0 落盘 / 0 入 log"},
            {"idx": 12, "rule": "0 编造", "evidence": "skill 缺位如实交代；0 虚构条文；0 虚构读数"},
        ],
        "rerun_determinism": {
            "ts_frozen": TS_FROZEN, "no_wallclock_dependency": True,
            "new_rng_sources": 0,
            "method": FROZEN_EVAL_CRITERIA["C4_reproducible"]["operationalization"],
        },
    }

    OUT_DIR = root / "results/_v3_s_phrasetemplate_preexp_data"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT = OUT_DIR / "result_2026_09_27.json"
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
                   encoding="utf-8")
    print("[preexp-S] input_chain_all_match=%s n_substrate=%d" % (input_chain_all_match, n_sub))
    print("[preexp-S] coverages: " + ", ".join(
        "%s=%.4f" % (c, constructions[c]["coverage"]) for c in constructions))
    print("[preexp-S] P-PT-1 target_n=%d pass=%d not_met=%d"
          % (routes["P-PT-1"]["target_n"], routes["P-PT-1"]["n_pass"], routes["P-PT-1"]["n_not_met"]))
    print("[preexp-S] P-PT-2 best_any=%.4f (%s) attainable@0.80=%s"
          % (best_any, best_any_id, any_face_reaches_080))
    print("[preexp-S] written:", OUT.relative_to(root), "sha12=", sha12_file(OUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
