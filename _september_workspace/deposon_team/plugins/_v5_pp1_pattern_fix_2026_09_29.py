# -*- coding: utf-8 -*-
"""
V5 批 15 · M-Q6＝A · 短语模板实现截断 **修复实现件**（新名 executor）
==================================================================
件名: deposon_team/plugins/_v5_pp1_pattern_fix_2026_09_29.py
出证方: **worker（执行类·代码缺陷修复；本棒实际执行者）**。
        **不冒充** PI / protocol-keeper / verdict-keeper / doc-writer / evidence-auditor / verifier。

派工（沿派工单字面）:
  - 任务: 批 15 **M-Q6 ＝ A 执行面「实现截断修复」**（独立可先行；**重测棒另派**）。
  - 缺陷面（沿 `results/_v5_confirm_b14_b15_decisions_register_2026_09_29.md` §2.2 字面）:
      `ruleset_v3` 第 4/5 类 pattern 含 `/` ＝ **两个候选式**（全类共 **7 候选式**），
      **实现把「二选一」截成「只取首项」** ⇒ `万物理论` / `判据优先序` 在 77 件中 **0 命中**
      （**结构上永不可能命中**）。
  - 修法（PI 裁 A 字面）: 「**先单独修实现截断（`/` 两候选式都试）＝ 代码缺陷修复、0 动判死线**」。

⛔ 本件铁边界（逐条自守，0 放宽）:
  1. **0 改既有 executor**（沿 R5「frozen 只追加」）——既有
     `results/_v4_pi_cot_v3_ruleset_v3_executor.py`（`8a81d90c69ba`）与其 r1 修件
     （`ee8671a28c2f`）**byte 0 触动**，本件**只读 import / 只读 load** 作「修复前」对照。
  2. **0 回改 `ruleset_v3` 冻结字面**——`results/_v4_pi_cot_v3_ruleset_v3.json`（`9d77a5e2cbab`）
     **只读打开**；候选式**从冻结字面现场切分**得到，0 自拟词表、0 改 pattern 字符串。
  3. **0 跑重测**——本件**0 加载 77 件 substrate**、**0 计算覆盖率/命中率**、**0 判读**、
     **0 定档**、**0 引入任何达标线**（判读线待 PI 给值；重测棒另派，前置于 §2.1 硬门）。
  4. **0 新设阈值**、**0 改 K-V3-* 判死线**、**0 代裁**、**0 预判任何档位**。
  5. **R4 key 永不明文**——本件 0 读 key、0 落盘 key、0 入 prompt/JSON/log（0 LLM/0 proxy/0 gateway）。
  6. **0 掩盖不利读数**——沿源件 `_v3_s_phrasetemplate_prereg_v1_2026_09_27.md` L162 字面
     「**若报『扩词后达标』即为误导**」：**本件 0 报任何『达标』结论**（本件根本不测达标）。

自证口径（**机制层**，只测匹配函数行为）:
  - 「修复前」臂 = 既有 executor **自身**的 `PHRASE_PATTERNS_V3` + `extract_judgment_sequence_v3`
    （只读 import，0 复写、0 臆造）。
  - 「修复后」臂 = 本件 `extract_judgment_sequence_fixed()`（`/` 切分 ⇒ 候选式 OR 参与匹配）。
  - 自证 ＝ **夹具级**（fixture）：证明 `万物理论` / `判据优先序` 由「结构不可命中」变为「可命中」，
    且「首候选式」臂 0 回归、并与既有实现**逐件逐位一致**（把候选集退化为既有截断表时，
    本件输出 **== 既有 executor 输出**）⇒ **差异来源唯一 ＝ `/` 截断**。
  - **0 触碰 77 件 substrate**；自证外推边界 ＝ 构造域（匹配函数行为），**0 外推**为覆盖率读数。

双记沿用（沿 §2.2 字面）:
  **5 类 ＝ 分类数、7 候选式 ＝ 匹配式数，二者 0 是同一口径。**

依赖与运行:
  - Python 3 + numpy（**仅为 import 既有 executor**；本件新增逻辑 0 依赖 numpy 运算）。
  - 外部设 `PYTHONIOENCODING=utf-8`（沿 V3/V4 executor 先例）。
  - 运行: `python deposon_team/plugins/_v5_pp1_pattern_fix_2026_09_29.py` ⇒ stdout 打印自证 JSON；
    **本件 0 写盘**（产物仅本件自身 + 配套注记件 `results/_v5_b15_pp1_impl_fix_2026_09_29.md`）。
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

# 0 落 .pyc 到既有 results/ 目录（既有件 byte 0 触动 ＝ 目录内不新增任何副产物）
sys.dont_write_bytecode = True

# ============================================================================
# 0. 路径与冻结锚（**只读**；SHA-12 = hashlib.sha256(字节).hexdigest()[:12]，小写 12 位）
# ============================================================================
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
RESULTS_DIR = REPO_ROOT / "results"

FROZEN_RULESET_V3 = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3.json"
FROZEN_RULESET_V3_SHA12 = "9d77a5e2cbab"

FROZEN_EXECUTOR_V3 = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor.py"
FROZEN_EXECUTOR_V3_SHA12 = "8a81d90c69ba"

FROZEN_EXECUTOR_V3_R1 = RESULTS_DIR / "_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py"
FROZEN_EXECUTOR_V3_R1_SHA12 = "ee8671a28c2f"

# 依据件（只读引用，登记面 0 复算其读数）
PREREG_PP_V1 = RESULTS_DIR / "_v3_s_phrasetemplate_prereg_v1_2026_09_27.md"
PREREG_PP_V1_SHA12 = "7e1323b09030"

REGISTER_B14_B15 = RESULTS_DIR / "_v5_confirm_b14_b15_decisions_register_2026_09_29.md"
REGISTER_B14_B15_SHA12 = "e48276a8dd31"

CATALOGUE_R2H2 = RESULTS_DIR / "_v5_r2h2_residual_merged_catalogue_2026_09_29.md"
CATALOGUE_R2H2_SHA12 = "b62d19c1c7cc"

FROZEN_ANCHORS: Tuple[Tuple[Path, str], ...] = (
    (FROZEN_RULESET_V3, FROZEN_RULESET_V3_SHA12),
    (FROZEN_EXECUTOR_V3, FROZEN_EXECUTOR_V3_SHA12),
    (FROZEN_EXECUTOR_V3_R1, FROZEN_EXECUTOR_V3_R1_SHA12),
)

# 候选式分隔符（沿冻结字面「大一统定义 / 万物理论」的分隔形态，**0 改分隔符语义**）
CANDIDATE_SEPARATOR = "/"

# 时间戳冻结（re-entrancy-safe，沿 V3/V4 executor 先例）
TS_FROZEN = "2026-09-29T17:28:00+08:00"


# ============================================================================
# 1. 基础工具（sha12 / 只读加载 / 锚核验）
# ============================================================================
def sha12_bytes(data: bytes) -> str:
    """SHA-12 = hashlib.sha256(字节).hexdigest()[:12]（小写 12 位，盘上实测口径）。"""
    import hashlib

    return hashlib.sha256(data).hexdigest()[:12]


def sha12_file(p: Path) -> str:
    return sha12_bytes(p.read_bytes())


def load_frozen_executor(path: Path = FROZEN_EXECUTOR_V3):
    """**只读** import 既有 executor（module 顶层仅定义常量/函数，`__main__` 段不执行）。

    本函数**不修改**既有件：仅按路径加载其模块对象，供「修复前」对照臂使用。
    """
    spec = importlib.util.spec_from_file_location("_frozen_v3_executor_ro", str(path))
    if spec is None or spec.loader is None:  # pragma: no cover
        raise RuntimeError(f"无法只读加载冻结 executor: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def verify_frozen_anchors() -> List[Dict[str, Any]]:
    """核验冻结锚 SHA-12（**实测**）——证明本棒 0 触动既有件。"""
    out: List[Dict[str, Any]] = []
    for p, expected in FROZEN_ANCHORS:
        actual = sha12_file(p)
        out.append(
            {
                "path": p.name,
                "sha12_expected_lowercase": expected,
                "sha12_measured": actual,
                "match": actual == expected,
                "bytes": p.stat().st_size,
            }
        )
    return out


# ============================================================================
# 2. 候选式切分（**修法的机制核心**：`/` ⇒ 二选一 ⇒ 两候选式都试）
# ============================================================================
def load_frozen_phrase_patterns() -> List[Dict[str, Any]]:
    """**只读**载入 `ruleset_v3` 冻结字面 `phrase_patterns_v3`（0 改 1 字节）。

    Returns:
        冻结 pattern 字典列表（原样返回，0 规范化 / 0 改写 / 0 补词）。
    """
    data = json.loads(FROZEN_RULESET_V3.read_text(encoding="utf-8"))
    return list(data["phrase_patterns_v3"])


def ruleset_declared_class_count() -> int:
    """冻结字面 `phrase_patterns_count`（＝ 5，分类数）。"""
    data = json.loads(FROZEN_RULESET_V3.read_text(encoding="utf-8"))
    return int(data["phrase_patterns_count"])


def split_candidates(raw_pattern: str) -> List[str]:
    """把一个「类」字面切分为**候选式**列表（二选一 ⇒ 2 项；无 `/` ⇒ 1 项）。

    切分口径: 沿冻结字面的 ` / ` 分隔（此处按 `/` 切分后 strip，容忍分隔符两侧空白）。
    0 造词、0 改词、0 丢词：切分前后候选式**并集 ＝ 冻结字面的词面**。
    """
    parts = [seg.strip() for seg in raw_pattern.split(CANDIDATE_SEPARATOR)]
    return [p for p in parts if p]


def build_candidate_table(patterns: Sequence[Dict[str, Any]]
                          ) -> List[Dict[str, Any]]:
    """由冻结 pattern 表构造「类 → 候选式」表（双记：n_classes / n_candidates）。"""
    table: List[Dict[str, Any]] = []
    for idx, pat in enumerate(patterns, start=1):
        cands = split_candidates(pat["pattern"])
        table.append(
            {
                "class_index": idx,
                "class_literal_frozen": pat["pattern"],       # 冻结字面，原样
                "candidates": cands,                            # 匹配式（1 或 2 项）
                "n_candidates": len(cands),
                "target_seq": list(pat["target_seq"]),           # 冻结 target_seq，0 改
                "v2_anchor": pat.get("v2_anchor", ""),
            }
        )
    return table


def count_candidates(table: Sequence[Dict[str, Any]]) -> int:
    """匹配式总数（n_candidates；沿双记口径 ＝ 7）。"""
    return sum(int(c["n_candidates"]) for c in table)


def candidates_in_text(cands: Sequence[str], text: str) -> List[str]:
    """返回该类中在 text 内以 **exact substring** 命中的候选式（OR 语义）。"""
    return [c for c in cands if c in text]


# ============================================================================
# 3. 匹配函数（修复后 ＝ 修复前的唯一行为差异所在）
# ============================================================================
def match_phrase_patterns_fixed(
    text: str,
    table: Sequence[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    """**修复后**短语模式匹配：每类的**全部候选式都试**（任一 exact substring 命中 ⇒ 该类命中）。

    与既有 executor 的差异**唯一**：既有实现每类只有 1 个（被截断的）匹配式；
    本实现每类按 `n_candidates` 个候选式 OR 匹配。
    """
    hits: List[Dict[str, Any]] = []
    for cls in table:
        hit_cands = candidates_in_text(cls["candidates"], text)
        if hit_cands:
            hits.append(
                {
                    "class_index": cls["class_index"],
                    "class_literal_frozen": cls["class_literal_frozen"],
                    "hit_candidates": hit_cands,
                    "n_candidates": cls["n_candidates"],
                    "target_seq": list(cls["target_seq"]),
                }
            )
    return hits


def match_phrase_patterns_baseline(mod, text: str) -> List[Dict[str, Any]]:
    """**修复前**短语模式匹配：直接用既有 executor **自身**的表与 `in` 判定（只读复用）。"""
    hits: List[Dict[str, Any]] = []
    for pat in mod.PHRASE_PATTERNS_V3:
        if pat["pattern"] in text:
            hits.append(
                {
                    "class_index": None,
                    "class_literal_frozen": pat["pattern"],
                    "hit_candidates": [pat["pattern"]],
                    "n_candidates": 1,
                    "target_seq": list(pat["target_seq"]),
                }
            )
    return hits


def seq_base_from_keywords(text: str, keywords: Dict[str, Tuple[str, ...]]) -> List[str]:
    """关键词首现位置序 + dedup（**逐行沿既有 executor Step 1-2 逻辑**，0 改算法）。"""
    earliest: List[Tuple[int, str]] = []
    for jt, kws in keywords.items():
        pos = -1
        for kw in kws:
            idx = text.find(kw)
            if idx >= 0 and (pos < 0 or idx < pos):
                pos = idx
        if pos >= 0:
            earliest.append((pos, jt))
    earliest.sort(key=lambda x: x[0])
    seq: List[str] = []
    seen: set = set()
    for _, jt in earliest:
        if jt not in seen:
            seen.add(jt)
            seq.append(jt)
    return seq


def extract_judgment_sequence_fixed(
    text: str,
    table: Sequence[Dict[str, Any]],
    keywords: Dict[str, Tuple[str, ...]],
) -> List[str]:
    """**修复后**判据类型序列提取（全序列 + 短语模式 OR 匹配），drop-in 于既有函数。

    Step 1-2 与既有 executor 逐行同构；Step 3 改用候选式 OR 表。
    """
    if not text or not text.strip():
        return []
    seq = seq_base_from_keywords(text, keywords)
    seen = set(seq)
    for hit in match_phrase_patterns_fixed(text, table):
        for jt in hit["target_seq"]:
            if jt not in seen:
                seen.add(jt)
                seq.append(jt)
    return seq


# ============================================================================
# 4. 自证（机制层 · 夹具级 · 0 涉判读线 / 0 涉达标）
# ============================================================================
# 夹具字面（**构造面**，非语料截取；0 复制 77 件 substrate 任何 `reasoning_full`）
FIXTURES: Tuple[Dict[str, str], ...] = (
    {
        "fid": "F1_second_alt_daiwu",
        "text": "（构造夹具）此处只主张万物理论一语，不含统一定义字样。",
    },
    {
        "fid": "F2_second_alt_priority",
        "text": "（构造夹具）此处只主张判据优先序一语，不含序列字样。",
    },
    {
        "fid": "F3_first_alt_daiyi",
        "text": "（构造夹具）此处给出大一统定义一语，作为首候选式回归对照。",
    },
    {
        "fid": "F4_first_alt_panju",
        "text": "（构造夹具）此处给出判据序列一语，作为首候选式回归对照。",
    },
    {
        "fid": "F5_both_second_alts",
        "text": "（构造夹具）此处同时主张万物理论与判据优先序两处次候选式。",
    },
    {
        "fid": "F6_negative_control",
        "text": "（构造夹具）本段刻意不含任何五类短语候选式字样。",
    },
)

SECOND_ALTERNATIVES = ("万物理论", "判据优先序")


def self_check(verbose: bool = True) -> Dict[str, Any]:
    """跑「修复前 vs 修复后」对照自证（**只测匹配函数行为**，0 判读 / 0 定档 / 0 达标）。"""
    anchors = verify_frozen_anchors()
    mod = load_frozen_executor()
    frozen_patterns = load_frozen_phrase_patterns()
    table = build_candidate_table(frozen_patterns)

    n_classes_declared = ruleset_declared_class_count()
    n_classes = len(table)
    n_cands = count_candidates(table)

    # 截断表（由冻结表按「只取首项」退化而成）—— 用于证明差异来源唯一
    truncated_table = [
        {
            "class_index": cls["class_index"],
            "class_literal_frozen": cls["class_literal_frozen"],
            "candidates": cls["candidates"][:1],
            "n_candidates": 1,
            "target_seq": cls["target_seq"],
        }
        for cls in table
    ]

    per_fixture: List[Dict[str, Any]] = []
    parity_ok = True
    recovered: List[str] = []
    for fx in FIXTURES:
        text = fx["text"]
        base_hits = match_phrase_patterns_baseline(mod, text)
        fix_hits = match_phrase_patterns_fixed(text, table)
        base_seq = mod.extract_judgment_sequence_v3(text)
        fix_seq = extract_judgment_sequence_fixed(text, table, mod.KEYWORDS_V3)
        trunc_seq = extract_judgment_sequence_fixed(text, truncated_table, mod.KEYWORDS_V3)
        parity_here = (trunc_seq == base_seq)
        parity_ok = parity_ok and parity_here
        base_cands = {c for h in base_hits for c in h["hit_candidates"]}
        fix_cands = {c for h in fix_hits for c in h["hit_candidates"]}
        for cand in SECOND_ALTERNATIVES:
            # 该次候选式在「修复前」臂结构上不可命中（baseline_hit_candidates 永不含它），
            # 且在「修复后」臂变为可命中（fixed_hit_candidates 含它）⇒ 机制层截断已解除。
            if cand in text and cand not in base_cands and cand in fix_cands \
                    and cand not in recovered:
                recovered.append(cand)
        per_fixture.append(
            {
                "fid": fx["fid"],
                "baseline_hit_classes": [h["class_literal_frozen"] for h in base_hits],
                "baseline_hit_candidates": [
                    c for h in base_hits for c in h["hit_candidates"]
                ],
                "fixed_hit_classes": [h["class_literal_frozen"] for h in fix_hits],
                "fixed_hit_candidates": [c for h in fix_hits for c in h["hit_candidates"]],
                "baseline_seq_full": base_seq,
                "fixed_seq_full": fix_seq,
                "parity_truncated_table_equals_frozen_executor": parity_here,
            }
        )

    # 断言层（机制层硬校验，0 涉达标线）
    def _hits(f: str, side: str) -> List[str]:
        rec = next(r for r in per_fixture if r["fid"] == f)
        return rec[side]

    assertions = {
        "A1_frozen_anchors_untouched": all(a["match"] for a in anchors),
        "A2_class_count_is_5": n_classes == 5 == n_classes_declared,
        "A3_candidate_count_is_7": n_cands == 7,
        "A4_dual_record_consistent": (n_classes, n_cands) == (5, 7),
        "A5_second_alternatives_present_in_candidate_set": all(
            cand in {c for cls in table for c in cls["candidates"]}
            for cand in SECOND_ALTERNATIVES
        ),
        "A6_f1_wanwu_before_structurally_unreachable": "万物理论" not in _hits("F1_second_alt_daiwu", "baseline_hit_candidates"),
        "A6b_f1_class_level_zero_hit_before": not _hits("F1_second_alt_daiwu", "baseline_hit_classes"),
        "A7_f1_wanwu_after_hittable": "万物理论" in _hits("F1_second_alt_daiwu", "fixed_hit_candidates"),
        "A7b_f1_class_hit_after": "大一统定义 / 万物理论" in _hits("F1_second_alt_daiwu", "fixed_hit_classes"),
        "A8_f2_priority_before_structurally_unreachable": "判据优先序" not in _hits("F2_second_alt_priority", "baseline_hit_candidates"),
        "A8b_f2_class_level_zero_hit_before": not _hits("F2_second_alt_priority", "baseline_hit_classes"),
        "A9_f2_priority_after_hittable": "判据优先序" in _hits("F2_second_alt_priority", "fixed_hit_candidates"),
        "A9b_f2_class_hit_after": "判据序列 / 判据优先序" in _hits("F2_second_alt_priority", "fixed_hit_classes"),
        "A10_first_alternative_no_regression": (
            _hits("F3_first_alt_daiyi", "baseline_hit_candidates")
            == _hits("F3_first_alt_daiyi", "fixed_hit_candidates")
            and _hits("F4_first_alt_panju", "baseline_hit_candidates")
            == _hits("F4_first_alt_panju", "fixed_hit_candidates")
        ),
        "A11_negative_control_zero_hits_both_arms": (
            not _hits("F6_negative_control", "baseline_hit_candidates")
            and not _hits("F6_negative_control", "fixed_hit_candidates")
        ),
        "A12_parity_with_frozen_executor_when_truncated": parity_ok,
        "A13_no_kill_line_or_threshold_touched": True,  # 本件 0 引入阈值，构造性为真
    }

    report = {
        "piece": "deposon_team/plugins/_v5_pp1_pattern_fix_2026_09_29.py",
        "ts_frozen": TS_FROZEN,
        "author": "worker (执行类·代码缺陷修复)",
        "sha12_measure": "hashlib.sha256(字节).hexdigest()[:12] (小写 12 位, 盘上实测)",
        "defect": {
            "class_literal_4": table[3]["class_literal_frozen"],
            "class_literal_5": table[4]["class_literal_frozen"],
            "baseline_literal_4": mod.PHRASE_PATTERNS_V3[3]["pattern"],
            "baseline_literal_5": mod.PHRASE_PATTERNS_V3[4]["pattern"],
            "truncation": "二选一（两候选式）被实现截成只取首项 ⇒ 次候选式结构上永不可能命中",
            "frozen_ruleset": FROZEN_RULESET_V3.name,
            "frozen_executor": FROZEN_EXECUTOR_V3.name,
        },
        "fix": {
            "method": "每类 pattern 按冻结字面 `/` 切分为候选式集合；命中判据 = 任一候选式 exact substring 命中（OR）",
            "words_added": 0,
            "words_removed": 0,
            "thresholds_introduced": 0,
            "kill_lines_touched": 0,
            "frozen_files_written": 0,
        },
        "dual_record": {
            "n_classes": n_classes,
            "n_candidates": n_cands,
            "note": "5 类 ＝ 分类数、7 候选式 ＝ 匹配式数，二者 0 是同一口径（沿 §2.2 双记沿用）",
        },
        "candidate_table": [
            {
                "class_index": c["class_index"],
                "class_literal_frozen": c["class_literal_frozen"],
                "candidates": c["candidates"],
                "n_candidates": c["n_candidates"],
                "target_seq": c["target_seq"],
            }
            for c in table
        ],
        "frozen_anchor_check": anchors,
        "self_check_scope": {
            "level": "机制层（匹配函数行为）",
            "substrate_loaded": 0,
            "coverage_computed": 0,
            "judgment_line_touched": 0,
            "verdict_rendered": 0,
            "hit_rate_reported": False,
        },
        "per_fixture": per_fixture,
        "assertions": assertions,
        "all_assertions_pass": all(assertions.values()),
        "structurally_unreachable_now_hittable": recovered,
        "honest_boundary": [
            "本件只修实现（`/` 两候选式都试），0 动判死线、0 新设阈值、0 引入达标线。",
            "本件 0 跑重测、0 加载 77 件 substrate、0 报任何覆盖率/命中率读数、0 定档。",
            "自证读数只在构造夹具面成立，外推边界 ＝ 匹配函数行为（构造域），0 外推为语料命中率。",
            "既有 executor 与 ruleset_v3 冻结字面 byte 0 触动（见 frozen_anchor_check）。",
        ],
    }
    if verbose:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    return report


def main() -> Dict[str, Any]:
    return self_check(verbose=True)


if __name__ == "__main__":
    main()
