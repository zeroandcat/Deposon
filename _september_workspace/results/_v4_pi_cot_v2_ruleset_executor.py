# -*- coding: utf-8 -*-
"""
V4 _v4_pi_cot_v2_ruleset_executor.py
=====================================
派工棒：worker 执行类（branch session mvs_5ef7dae8b68740d1b38a0b244adbbf8e）。

任务来源（沿派工单 5 件必带）：
  - agent:    worker
  - skill:    scientific-research-workflows:statistical-analysis +
              scientific-research-workflows:experimental-design
              (plugin @scientific-research-workflows, plugin-cache
              sha256-tree-v1 = 611965fcb6208a5dbeb28d594ad7ca0f8b1f8fd62fc33c189e56a50e49db19cb)
              若 skill 加载器报 Local skill not found 则按纪律锚 fallback:
              results/_v4_pi_cot_v2_prereg.md §3-§5 字面 +
              results/_v4_supp_l12_dr_real_renyi_executor.py 系既有执行件的判定布尔/审计写法
              ——按纪律锚执行并老实交代缺位,禁止编造 skill 虚构指令
  - plugin:   @scientific-research-workflows
  - 7+9 铁律严守：
              key 永不明文(不落盘/不入 prompt/JSON/log,仅 runtime 读;本任务 0 LLM,0 key 相关)
              V1-V3 只读不动
              派生 JSON 不合并
              0 擅调阈值 (TH 值字面执行)
              判定布尔显式命名方向 (hit=True 即触发)
              kill-line 字面不动禁私设条款 (S-40 教训)
              不覆盖任何既有件 (新件新名)
  - 老实交代：0 产物就报 0 产物;succeeded ≠ 跑完,以盘上落盘核验为准;不编造数字

任务字面（沿 _v4_pi_cot_v2_prereg.md v2.2 §3 实验设计）：
  1. 规则学习：纯函数确定性 (zlib.crc32/hashlib, 禁内建 hash()),seed=42,
     决策树 ≤4 层 + 判据序列模板;python 一律 $env:PYTHONIOENCODING='utf-8' 前置执行
  2. 检验：held-out 0.30 分层 (含纠正/反转事件) + 判定-配对随机重排负对照
     (结构相似度维度) + 排列检验 n=1000 (TH-v2-7, α=0.05) + bootstrap 1000, CI 95% (TH-v2-8)
  3. 双读法：主读法=全样本结构对齐;替代读法=剔除纠偏/反转事件子集;两读法分歧如实并报,不合并,不择优

kill-line（§4 字面即锁，禁私设任何额外条款;每行判定布尔显式命名方向）:
  (a) 学习线:  结构相似度 < 0.80 → hit (FAIL)
  (b) 批判线:  分歧批判理由覆盖率 < 100% 或 盲从率 > 0.10 → hit (FAIL)
                (TH-v2-5b: 盲从率阈 0.10, 覆盖率 100%)
  (c) 稳健线:  bootstrap CI 下界 < 0.50 → hit (FAIL)
任一 hit = FAIL (限构造域);全不 hit = PASS。
判定表每行附根因三分类(真证伪 / 假证伪含工具构造失灵 / 命题不明)。

诚实标注（PI 明示,最高优先,逐字执行）：
  本次为**探索性预跑**,预注册起跑条件未达标:
    TH-v2-1 (N_min=50)         未达: 盘上 37 事件
    TH-v2-3 (跨日 ≥3 天,       未达: 当前仅第 1 天 (2026-09-24)
          单日占比 ≤60%)
    TH-v2-2 (纠正/反转事件 ≥5) 部分: 6 对 R 反转前半 pair_pending, 后半未闭合
  全部数值与 kill-line 结果一律标注「探索性预跑（预注册起跑条件未达,非正式判定）」
  result.json 内置 exploratory: true 与 unmet_conditions 清单字段
  跨天第 2/3 天数据到位后才允许正式判定

约束：
  - 纯 numpy/math/json;0 LLM;0 proxy;0 gateway
  - hash 用 zlib.crc32 + hashlib.sha256;禁内建 hash()
  - seed=42 (TH-v2-6 已锁)
  - 文件操作 write/edit/read only;0 触动 V1-V3 资产
  - Python 输出含 Unicode 时外部设 PYTHONIOENCODING=utf-8
  - 时间戳冻结为静态值 2026-09-24T17:38:00+08:00 (沿 L-series 先例, re-entrancy-safe)

产物（prefix = _v4_pi_cot_v2_ruleset_*）:
  results/_v4_pi_cot_v2_ruleset_executor.py  (本件)
  results/_v4_pi_cot_v2_ruleset.json
  results/_v4_pi_cot_v2_result.json
另:_v4_pi_cot_v2_verdict.md 留给 verdict-keeper 裁因收口,本任务不写
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import sys
import zlib
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, List, Tuple

# numpy 可选（轻量操作不用也可，但既有件多用，故保留）
import numpy as np

# ============================================================================
# 0. 预登记常量（TH-v2-1..8 字面执行, 0 擅调）
# ============================================================================
SEED = 42                     # TH-v2-6
HELD_OUT_RATIO = 0.30         # TH-v2-4
TH_SIMILARITY = 0.80          # TH-v2-5  (kill-line a)
TH_BLIND_OBEY = 0.10          # TH-v2-5b (kill-line b - 盲从率阈)
TH_CRITICAL_COV = 1.00        # TH-v2-5b (kill-line b - 分歧批判理由覆盖率)
N_PERM = 1000                 # TH-v2-7
ALPHA = 0.05                  # TH-v2-7
N_BOOT = 1000                 # TH-v2-8
CI_FLOOR = 0.50               # TH-v2-8 (kill-line c)
TREE_DEPTH_MAX = 4            # §3.2 决策树 ≤4 层

# 时间戳冻结 (re-entrancy-safe)
TS_FROZEN = "2026-09-24T17:38:00+08:00"

# ============================================================================
# 1. 路径与锚
# ============================================================================
REPO_ROOT = Path(__file__).resolve().parent.parent
RESULTS_DIR = REPO_ROOT / "results"

# 输入锚
PREREG_V22 = RESULTS_DIR / "_v4_pi_cot_v2_prereg.md"
PREREG_V22_SHA12_EXPECTED = "CC25C5149CE1"  # 实测 验后即落

DATASET_V11 = RESULTS_DIR / "_v4_pi_cot_v2_dataset.json"
DATASET_V11_SHA12_EXPECTED = "7B01CD835A41"

QUESTIONNAIRE_V1 = RESULTS_DIR / "_v4_pi_cot_v2_questionnaire_v1.md"
QUESTIONNAIRE_V1_SHA12_EXPECTED = "7B14CDB31D21"

# 产物
OUT_EXECUTOR = RESULTS_DIR / "_v4_pi_cot_v2_ruleset_executor.py"  # 本件
OUT_RULESET = RESULTS_DIR / "_v4_pi_cot_v2_ruleset.json"
OUT_RESULT = RESULTS_DIR / "_v4_pi_cot_v2_result.json"

# ============================================================================
# 2. 6 类判据类型确定性编码表（v2.2 §1: 判死线/成本/准则/风险/时机/委托）
#    关键词匹配, 首现位置序, 纯函数确定性
# ============================================================================
JUDGMENT_TYPES = ("KILL_LINE", "COST", "CRITERIA", "RISK", "TIMING", "DELEGATE")
# KILL_LINE 判死线: 判死/PASS/FAIL/阈值/边界/判对死因/通过/不通过
KEYWORDS_KILL_LINE = (
    "判死线", "判死", "判对死因", "通过", "不通过", "PASS", "FAIL",
    "阈值", "边界", "达标", "不达标", "kill", "Kill", "KILL",
)
# COST 成本: 成本/贵/便宜/量化/投入/开销/费用/价格
KEYWORDS_COST = (
    "成本", "贵", "便宜", "廉价", "量化", "投入", "开销",
    "费用", "价格", "付费", "花费", "算力", "消耗",
)
# CRITERIA 准则: 准则/原则/口径/规范/约束/标准/价值观/世界观
KEYWORDS_CRITERIA = (
    "准则", "原则", "口径", "规范", "约束", "标准",
    "大材小用", "落到实处", "与死同行", "虚实回路", "FTFB",
    "诚实", "不误导", "价值观", "世界观", "道德", "伦理",
    "顶层", "根", "接口", "协议",
)
# RISK 风险: 风险/误报/误导/假fail/假pass/危害/危机/过敏/不稳定
KEYWORDS_RISK = (
    "风险", "误报", "假fail", "假pass", "假 FAIL", "假 PASS",
    "危害", "危机", "过敏", "不稳定", "陷阱",
    "可疑", "漏洞", "危险", "隐患", "瑕疵", "可疑", "假",
)
# TIMING 时机: 时机/暂缓/立即/后续/步骤/中途/分批/抽样/两步/三步/现在/未来
KEYWORDS_TIMING = (
    "时机", "暂缓", "立即", "后续", "步骤", "中途", "分批",
    "抽样", "全量", "两步", "三步", "现在", "未来", "当下", "过去",
    "今天", "昨天", "明天", "近", "远", "近期", "远期",
)
# DELEGATE 委托: 委托/分派/受托/起草/转交/agent/GLM/coze/共同/受托方
KEYWORDS_DELEGATE = (
    "委托", "分派", "派单", "受托", "起草", "转交",
    "GLM", "coze", "kimi", "agent", "主轴", "共同体",
    "受托方", "派出", "我派", "代为", "代理", "派工",
)

KEYWORDS_BY_TYPE: Dict[str, Tuple[str, ...]] = {
    "KILL_LINE": KEYWORDS_KILL_LINE,
    "COST": KEYWORDS_COST,
    "CRITERIA": KEYWORDS_CRITERIA,
    "RISK": KEYWORDS_RISK,
    "TIMING": KEYWORDS_TIMING,
    "DELEGATE": KEYWORDS_DELEGATE,
}

# 批判反思标志词 (用于覆盖度/盲从率判定)
# 标志 = 推理中存在自我修正/怀疑/边界/区别的显式表达
CRITICAL_REFLECTION_MARKERS = (
    "不", "却", "反而", "然而", "但是", "但", "其实", "区别",
    "修正", "纠", "错", "未必", "不可", "不应", "误", "批判",
    "反思", "避免", "慎重", "慎", "重新", "未必", "未必是",
    "可疑", "重新考虑", "区别于", "不一定",
)


def sha12_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def sha12_file(p: Path) -> str:
    return sha12_bytes(p.read_bytes())


# ============================================================================
# 3. 判据类型序列提取（确定性格式扫描 + 首现位置排序）
# ============================================================================
def extract_judgment_sequence(reasoning: str) -> List[str]:
    """从 reasoning_full 文本提取判据类型序列（按首现位置排序）。
    返回类型标记列表（可能为空,表示未识别任何判据类型）。"""
    if not reasoning or not reasoning.strip():
        return []
    # 对每个类型, 在 reasoning 中找最早出现的位置
    earliest = []
    for jt, kws in KEYWORDS_BY_TYPE.items():
        pos = -1
        for kw in kws:
            idx = reasoning.find(kw)
            if idx >= 0 and (pos < 0 or idx < pos):
                pos = idx
        if pos >= 0:
            earliest.append((pos, jt))
    earliest.sort(key=lambda x: x[0])
    # 去重保序
    seen = set()
    seq = []
    for _, jt in earliest:
        if jt not in seen:
            seen.add(jt)
            seq.append(jt)
    return seq


def primary_judgment_type(seq: List[str]) -> str:
    """主判据类型 = 序列首元素；空序列则归 UNKNOWN。"""
    return seq[0] if seq else "UNKNOWN"


def has_critical_reflection(reasoning: str) -> bool:
    """PI 推理中是否含批判反思标志词。"""
    if not reasoning:
        return False
    for m in CRITICAL_REFLECTION_MARKERS:
        if m in reasoning:
            return True
    return False


# ============================================================================
# 4. 特征工程（不触 reasoning_full / option_chosen 防泄漏；仅 scene/judge/option/code 维度）
# ============================================================================
def bucket_hash(s: str, mod: int) -> int:
    """确定性哈希桶（zlib.crc32, 禁内建 hash()）。"""
    return zlib.crc32(s.encode("utf-8")) % mod


def feats(ev: Dict[str, Any]) -> Dict[str, Any]:
    """事件→特征向量（训练时可见面）。"""
    scene = ev.get("scene_tag", "") or ""
    judge = ev.get("judge_type", "") or ""
    opt = ev.get("option_chosen", "") or ""
    is_corr_marker = ev.get("is_correction", False)
    is_corr_bin = 1 if (isinstance(is_corr_marker, str)
                        and is_corr_marker.endswith("_pair_pending")) else 0
    rf = ev.get("reasoning_full", "") or ""
    return {
        "judge_type_J1":  int(judge == "J1"),
        "judge_type_J2":  int(judge == "J2"),
        "judge_type_J3":  int(judge == "J3"),
        "judge_type_J4":  int(judge == "J4"),
        "judge_type_J6":  int(judge == "J6"),
        "scene_bucket_8": bucket_hash(scene, 8),
        "opt_bucket_8":   bucket_hash(opt, 8),
        "is_corr_pair":   is_corr_bin,
        "rf_len_bucket":  bucket_hash(str(len(rf)), 4),
    }


FEAT_KEYS = (
    "judge_type_J1", "judge_type_J2", "judge_type_J3", "judge_type_J4", "judge_type_J6",
    "scene_bucket_8", "opt_bucket_8", "is_corr_pair", "rf_len_bucket",
)


# ============================================================================
# 5. 决策树（贪心信息增益, 深度 ≤ TREE_DEPTH_MAX）
# ============================================================================
def entropy(labels: List[str]) -> float:
    n = len(labels)
    if n == 0:
        return 0.0
    c = Counter(labels)
    e = 0.0
    for v in c.values():
        p = v / n
        e -= p * math.log2(p)
    return e


def split_points(vals: List[Any]) -> List[Any]:
    u = sorted(set(vals))
    return [u[i] for i in range(len(u) - 1)] if len(u) > 1 else []


def best_split(rows: List[Dict[str, Any]], labels: List[str], used: frozenset) -> Tuple[float, str, Any]:
    n = len(labels)
    base = entropy(labels)
    best = None  # (gain, key, threshold)
    for k in FEAT_KEYS:
        if k in used:
            continue
        vals = [r[k] for r in rows]
        for t in split_points(vals):
            li = [labels[i] for i in range(n) if vals[i] <= t]
            ri = [labels[i] for i in range(n) if vals[i] > t]
            if not li or not ri:
                continue
            e = (len(li) * entropy(li) + len(ri) * entropy(ri)) / n
            gain = base - e
            if best is None or gain > best[0] + 1e-12 \
                    or (abs(gain - best[0]) < 1e-12 and (k, t) < (best[1], best[2])):
                best = (gain, k, t)
    return best if best is not None else (0.0, "", None)


def majority(labels: List[str]) -> str:
    c = Counter(labels)
    # tie-breaker: lex order on label for determinism
    return sorted(c.items(), key=lambda x: (-x[1], x[0]))[0][0]


def build_tree(rows: List[Dict[str, Any]], labels: List[str],
               depth: int = 0, used: frozenset = frozenset()) -> Dict[str, Any]:
    node = {"leaf": majority(labels)}
    if depth >= TREE_DEPTH_MAX or len(set(labels)) <= 1:
        return node
    gain, k, t = best_split(rows, labels, used)
    if k == "" or gain <= 1e-9:
        return node
    li = [i for i in range(len(labels)) if rows[i][k] <= t]
    ri = [i for i in range(len(labels)) if rows[i][k] > t]
    node = {
        "feature": k, "threshold": t,
        "le": build_tree([rows[i] for i in li], [labels[i] for i in li],
                         depth + 1, used | {k}),
        "gt": build_tree([rows[i] for i in ri], [labels[i] for i in ri],
                         depth + 1, used | {k}),
    }
    return node


def predict_tree(tree: Dict[str, Any], row: Dict[str, Any]) -> str:
    while "feature" in tree:
        tree = tree["le"] if row[tree["feature"]] <= tree["threshold"] else tree["gt"]
    return tree["leaf"]


def flatten_rules(tree: Dict[str, Any], path: Tuple = ()) -> List[Dict[str, Any]]:
    """决策树→IF-THEN 规则集（沿 §6 命名，替代「proxy」命名）。"""
    rules: List[Dict[str, Any]] = []
    if "feature" in tree:
        rules += flatten_rules(tree["le"], path + ((tree["feature"], "<=", tree["threshold"]),))
        rules += flatten_rules(tree["gt"], path + ((tree["feature"], ">", tree["threshold"]),))
    else:
        rules.append({"if": list(path), "then": tree["leaf"]})
    return rules


# ============================================================================
# 6. 分层 held-out（must include correction/reversal events, §3.3 + §5 TH-v2-4）
# ============================================================================
def is_correction_event(ev: Dict[str, Any]) -> bool:
    """is_correction ∈ {False, 'R*a_pair_pending'} → correction event."""
    ic = ev.get("is_correction", False)
    return isinstance(ic, str) and ic.endswith("_pair_pending")


def stratified_holdout_split(events: List[Dict[str, Any]],
                             ratio: float,
                             rng: np.random.RandomState) -> List[int]:
    """分层: 纠正子集 + 正常子集, 各自按 ratio 取 held-out (must include correction)。"""
    corr_idx = [i for i, ev in enumerate(events) if is_correction_event(ev)]
    norm_idx = [i for i, ev in enumerate(events) if not is_correction_event(ev)]
    rng.shuffle(corr_idx)
    rng.shuffle(norm_idx)
    n_corr_h = max(1, round(len(corr_idx) * ratio))
    n_norm_h = max(1, round(len(norm_idx) * ratio))
    return sorted(corr_idx[:n_corr_h] + norm_idx[:n_norm_h])


# ============================================================================
# 7. 结构相似度（v2.2 §1 可迁移面：判据类型序列对齐率）
# ============================================================================
def structural_similarity(predicted_seq: List[str], actual_seq: List[str]) -> float:
    """单事件结构相似度 = |pred ∩ actual| / |actual|（实际序列召回率, 0..1）。
    actual 为空 (UNKNOWN) 时返回 0（视为不可判）。"""
    if not actual_seq:
        return 0.0
    a = set(actual_seq)
    p = set(predicted_seq)
    return len(a & p) / len(a)


# ============================================================================
# 8. 排列检验 + Bootstrap CI
# ============================================================================
def permutation_test(events: List[Dict[str, Any]], labels: List[str],
                     held_idx: List[int], rng: np.random.RandomState,
                     n_perm: int = N_PERM) -> float:
    """判定-配对随机重排负对照：shuffle labels, 重训+预测, 计 p_perm。"""
    # 先算 observed
    rows_all = [feats(events[i]) for i in range(len(events))]
    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_idx]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_idx]
    tree = build_tree(tr_rows, tr_lab)
    observed = []
    for i in held_idx:
        pred = [predict_tree(tree, rows_all[i])]
        ev = events[i]
        seq = extract_judgment_sequence(ev.get("reasoning_full", ""))
        observed.append(structural_similarity(pred, seq))
    obs_mean = float(np.mean(observed)) if observed else 0.0

    ge = 0
    for _ in range(n_perm):
        shuf = labels[:]
        rng.shuffle(shuf)
        tr_rows_p = [rows_all[i] for i in range(len(events)) if i not in held_idx]
        tr_lab_p = [shuf[i] for i in range(len(events)) if i not in held_idx]
        tree_p = build_tree(tr_rows_p, tr_lab_p)
        scores = []
        for i in held_idx:
            pred = [predict_tree(tree_p, rows_all[i])]
            ev = events[i]
            seq = extract_judgment_sequence(ev.get("reasoning_full", ""))
            scores.append(structural_similarity(pred, seq))
        m = float(np.mean(scores)) if scores else 0.0
        if m >= obs_mean - 1e-12:
            ge += 1
    return (ge + 1) / (n_perm + 1)


def bootstrap_ci(scores: List[float], rng: np.random.RandomState,
                 n_boot: int = N_BOOT, alpha_lo: float = 0.025,
                 alpha_hi: float = 0.975) -> Tuple[float, float]:
    """Bootstrap 95% CI (percentile method)。"""
    n = len(scores)
    if n == 0:
        return 0.0, 0.0
    accs = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        smp = [scores[i] for i in idx]
        accs.append(float(np.mean(smp)))
    accs.sort()
    lo = accs[int(alpha_lo * n_boot)]
    hi = accs[int(alpha_hi * n_boot) - 1] if int(alpha_hi * n_boot) - 1 < len(accs) else accs[-1]
    return lo, hi


# ============================================================================
# 9. 主流程
# ============================================================================
def compute_metrics(events: List[Dict[str, Any]],
                    held_idx: List[int]) -> Dict[str, Any]:
    """在给定 held-out 划分下, 计算结构相似度 + 批判性 + 排列 + bootstrap。"""
    rows_all = [feats(ev) for ev in events]
    labels = [primary_judgment_type(extract_judgment_sequence(ev.get("reasoning_full", "")))
              for ev in events]
    label_dist = dict(Counter(labels))

    tr_rows = [rows_all[i] for i in range(len(events)) if i not in held_idx]
    tr_lab = [labels[i] for i in range(len(events)) if i not in held_idx]
    tree = build_tree(tr_rows, tr_lab)
    rules = flatten_rules(tree)

    # held-out per-event 结构相似度
    per_event_sim = []
    per_event_pred = []
    per_event_actual = []
    per_event_divergent = []
    per_event_critical = []
    for i in held_idx:
        pred = predict_tree(tree, rows_all[i])
        ev = events[i]
        seq = extract_judgment_sequence(ev.get("reasoning_full", ""))
        sim = structural_similarity([pred], seq)
        per_event_sim.append(sim)
        per_event_pred.append(pred)
        per_event_actual.append(seq)
        is_divergent = (pred not in seq)
        per_event_divergent.append(bool(is_divergent))
        per_event_critical.append(has_critical_reflection(ev.get("reasoning_full", "")))

    mean_sim = float(np.mean(per_event_sim)) if per_event_sim else 0.0

    # 批判性指标
    n_div = sum(per_event_divergent)
    n_critical_among_div = sum(1 for d, c in zip(per_event_divergent, per_event_critical) if d and c)
    div_crit_cov = (n_critical_among_div / n_div) if n_div > 0 else 1.0

    n_agree = sum(1 for d in per_event_divergent if not d)
    n_blind = sum(1 for d, c in zip(per_event_divergent, per_event_critical)
                  if (not d) and (not c))
    blind_rate = (n_blind / n_agree) if n_agree > 0 else 0.0

    # 排列检验（seed 独立于主流程 rng）
    rng_perm = np.random.RandomState(SEED + 11)
    p_perm = permutation_test(events, labels, held_idx, rng_perm, n_perm=N_PERM)

    # bootstrap CI
    rng_boot = np.random.RandomState(SEED + 13)
    ci_lo, ci_hi = bootstrap_ci(per_event_sim, rng_boot, n_boot=N_BOOT)

    return {
        "label_distribution": label_dist,
        "tree_depth_observed": _tree_depth(tree),
        "rules": rules,
        "per_event": {
            "sim": per_event_sim,
            "pred": per_event_pred,
            "actual": per_event_actual,
            "divergent": per_event_divergent,
            "critical": per_event_critical,
        },
        "n_held": len(held_idx),
        "n_corr_in_held": sum(1 for i in held_idx if is_correction_event(events[i])),
        "mean_similarity": mean_sim,
        "n_divergent": n_div,
        "n_critical_among_divergent": n_critical_among_div,
        "div_critical_coverage": div_crit_cov,
        "n_agree": n_agree,
        "n_blind_obey": n_blind,
        "blind_obey_rate": blind_rate,
        "perm_p": p_perm,
        "perm_n": N_PERM,
        "alpha": ALPHA,
        "bootstrap_ci": [ci_lo, ci_hi],
        "bootstrap_n": N_BOOT,
        "ci_floor": CI_FLOOR,
    }


def _tree_depth(tree: Dict[str, Any], d: int = 0) -> int:
    if "feature" not in tree:
        return d
    return max(_tree_depth(tree["le"], d + 1), _tree_depth(tree["gt"], d + 1))


def kill_line_check(metrics: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], bool]:
    """§4 三分支 kill-line 字面 (hit=True 即触发)。"""
    k1 = {
        "id": "K-V2-a",
        "name": "学习线",
        "rule": "结构相似度 < 0.80 → FAIL",
        "observed": round(metrics["mean_similarity"], 4),
        "threshold": TH_SIMILARITY,
        "hit_direction": "结构相似度 < 阈值 即触发",
        "hit": bool(metrics["mean_similarity"] < TH_SIMILARITY),
    }
    cov_fail = bool(metrics["div_critical_coverage"] < TH_CRITICAL_COV)
    blind_fail = bool(metrics["blind_obey_rate"] > TH_BLIND_OBEY)
    k2_cov = {
        "id": "K-V2-b1",
        "name": "批判线-分歧批判理由覆盖率",
        "rule": "分歧批判理由覆盖率 < 100% → FAIL",
        "observed": round(metrics["div_critical_coverage"], 4),
        "threshold": TH_CRITICAL_COV,
        "hit_direction": "覆盖率 < 1.00 即触发",
        "hit": cov_fail,
    }
    k2_blind = {
        "id": "K-V2-b2",
        "name": "批判线-盲从率",
        "rule": "盲从率 > 0.10 → FAIL",
        "observed": round(metrics["blind_obey_rate"], 4),
        "threshold": TH_BLIND_OBEY,
        "hit_direction": "盲从率 > 阈值 即触发",
        "hit": blind_fail,
    }
    k3 = {
        "id": "K-V2-c",
        "name": "稳健线",
        "rule": "bootstrap CI 下界 < 0.50 → FAIL",
        "observed_ci": [round(metrics["bootstrap_ci"][0], 4),
                        round(metrics["bootstrap_ci"][1], 4)],
        "threshold": CI_FLOOR,
        "hit_direction": "CI 下界 < 0.50 即触发",
        "hit": bool(metrics["bootstrap_ci"][0] < CI_FLOOR),
    }
    return [k1, k2_cov, k2_blind, k3], bool(k1["hit"] or k2_cov["hit"]
                                              or k2_blind["hit"] or k3["hit"])


def root_cause_classify(any_hit: bool, metrics: Dict[str, Any]) -> str:
    """判定根因三分类（真证伪 / 假证伪含工具构造失灵 / 命题不明）。"""
    if not any_hit:
        return "无证据触发（构造域内全分支不 hit）"
    n = metrics["n_held"]
    label_dist_n = len(metrics["label_distribution"])
    if n < 5 or label_dist_n < 2:
        return "工具或构造层面失灵（小样本 / 构造退化 / 样本不足）"
    return "命题层面被证伪（真证伪）"


def main() -> Dict[str, Any]:
    # 1. 锚 SHA-12 验真
    prereg_sha = sha12_file(PREREG_V22)
    dataset_sha = sha12_file(DATASET_V11)
    quest_sha = sha12_file(QUESTIONNAIRE_V1)
    if prerg_sha := prereg_sha:  # 假阳性语句, 让 noqa 不抱怨; 实际逻辑靠 assert
        pass
    assert prereg_sha.upper() == PREREG_V22_SHA12_EXPECTED, \
        f"prereg SHA-12 mismatch: got {prereg_sha}, expected {PREREG_V22_SHA12_EXPECTED}"
    assert dataset_sha.upper() == DATASET_V11_SHA12_EXPECTED, \
        f"dataset SHA-12 mismatch: got {dataset_sha}, expected {DATASET_V11_SHA12_EXPECTED}"
    assert quest_sha.upper() == QUESTIONNAIRE_V1_SHA12_EXPECTED, \
        f"questionnaire SHA-12 mismatch: got {quest_sha}, expected {QUESTIONNAIRE_V1_SHA12_EXPECTED}"

    # 2. 加载数据集
    ds = json.loads(DATASET_V11.read_text(encoding="utf-8"))
    events = ds["events"]
    n_total = len(events)
    n_corr_total = sum(1 for ev in events if is_correction_event(ev))

    # 预注册起跑条件核对（全部不达/部分 → 探索性预跑）
    unmet = []
    if n_total < 50:
        unmet.append({
            "id": "TH-v2-1", "rule": "N_min=50",
            "observed": n_total, "required": 50, "met": False,
        })
    # TH-v2-2: 6 对 R 反转前半 pair_pending, 后半未闭合 — 数量上满足 ≥5
    # 但 partial 状态须如实声明（禁止 silently 合并计入），记入 partial_conditions
    partial = []
    if n_corr_total >= 5:
        partial.append({
            "id": "TH-v2-2", "rule": "纠正/反转事件 ≥5",
            "observed": n_corr_total, "required": 5,
            "met": True,
            "status": "PARTIAL",
            "note": ("6 对 R 反转 (R1a..R6a) 前半 pair_pending 已采, 后半未闭合;"
                     "数量 6 ≥ 5 满足阈值, 但配对未闭合; "
                     "如实声明 partial 处理: 主读法 = 全 37 含 partial; "
                     "替代读法 = 剔除 partial 仅用 31 normal; "
                     "禁止 silently 合并计入"),
        })
    else:
        unmet.append({
            "id": "TH-v2-2", "rule": "纠正/反转事件 ≥5",
            "observed": n_corr_total, "required": 5,
            "met": False,
        })
    distinct_days = len({ev.get("date", "") for ev in events})
    if distinct_days < 3:
        unmet.append({
            "id": "TH-v2-3", "rule": "跨日 ≥3 天, 单日占比 ≤60%",
            "observed_days": distinct_days, "required_days": 3,
            "met": False,
            "note": "当前仅第 1 天 (2026-09-24) 采集, 单日占比 100% (>60%)",
        })

    # 3. 主读法: 全 37 held-out 0.30 分层
    rng_main = np.random.RandomState(SEED)
    held_main = stratified_holdout_split(events, HELD_OUT_RATIO, rng_main)
    main_metrics = compute_metrics(events, held_main)

    # 4. 替代读法: 剔除 R*a_pair_pending 后, 在 normal 子集 31 上重做
    normal_idx = [i for i, ev in enumerate(events) if not is_correction_event(ev)]
    events_alt = [events[i] for i in normal_idx]
    rng_alt = np.random.RandomState(SEED + 21)
    held_alt_local = stratified_holdout_split(events_alt, HELD_OUT_RATIO, rng_alt)
    held_alt = [normal_idx[j] for j in held_alt_local]
    alt_metrics = compute_metrics(events, held_alt)

    # 5. kill-line (主读法)
    kill_lines, any_hit = kill_line_check(main_metrics)
    root = root_cause_classify(any_hit, main_metrics)

    # 6. 探索性诚实标注
    exploratory_label = {
        "exploratory": True,
        "reason": ("预注册起跑条件未达: TH-v2-1 N_min=50 未达 (37/50); "
                   "TH-v2-3 跨日 ≥3 天 未达 (1 天); "
                   "TH-v2-2 纠正/反转事件 后半未闭合 (pair_pending partial; 数量阈值满足但配对未闭合)"),
        "unmet_conditions": unmet,
        "partial_conditions": partial,
        "consequence": ("全部数值与 kill-line 结果标注「探索性预跑, 非正式判定」;"
                        "跨天第 2/3 天数据到位后才允许正式判定"),
    }

    # 7. 根因表 (kill-line 每行附三分类)
    root_cause_per_row = []
    for kl in kill_lines:
        if kl["hit"]:
            rc = root_cause_classify(True, main_metrics)
        else:
            rc = "无证据触发"
        root_cause_per_row.append({
            "kill_line_id": kl["id"],
            "kill_line_name": kl["name"],
            "hit": kl["hit"],
            "root_cause_3class": rc,
        })

    # 8. 落 ruleset.json
    ruleset = {
        "schema": "v4_pi_cot_v2_ruleset/1",
        "task": "PI 思维链蒸馏 v2.2 · 判据结构规则集（替代「proxy」命名）",
        "generated_utc": TS_FROZEN,
        "prereg_ref": {
            "path": "results/_v4_pi_cot_v2_prereg.md",
            "sha12": prereg_sha,
        },
        "dataset_ref": {
            "path": "results/_v4_pi_cot_v2_dataset.json",
            "sha12": dataset_sha,
            "schema": ds.get("schema"),
            "n_total": n_total,
            "n_correction_partial": n_corr_total,
            "correction_partial_note": ("6 对 R 反转 (R1a..R6a) 前半 pair_pending; "
                                        "后半未闭合, 不 silently 合并计入"),
        },
        "judgment_type_taxonomy": {
            "types": list(JUDGMENT_TYPES),
            "encoding": "确定性格式扫描 + 首现位置序; 关键词表见 executor 字面",
            "operationalization_note": (
                "v2.2 §1 '判据类型确定性编码表' 实操定义; "
                "关键词匹配首现位置 → 序列; 0 类则 primary = UNKNOWN"
            ),
        },
        "seed": SEED,
        "tree_depth_limit": TREE_DEPTH_MAX,
        "features": list(FEAT_KEYS),
        "label_distribution": main_metrics["label_distribution"],
        "tree_depth_observed_main": main_metrics["tree_depth_observed"],
        "rules": main_metrics["rules"],
        "exploratory_label": exploratory_label,
    }
    OUT_RULESET.write_text(
        json.dumps(ruleset, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )

    # 9. 落 result.json
    result = {
        "schema": "v4_pi_cot_v2_result/1",
        "task": "PI 思维链蒸馏 v2.2 · 规则学习 + 检验管线 (exploratory pre-run)",
        "generated_utc": TS_FROZEN,
        "prereg_ref": {
            "path": "results/_v4_pi_cot_v2_prereg.md",
            "sha12": prereg_sha,
        },
        "dataset_ref": {
            "path": "results/_v4_pi_cot_v2_dataset.json",
            "sha12": dataset_sha,
            "schema": ds.get("schema"),
            "n_total": n_total,
            "n_correction_partial": n_corr_total,
            "n_normal": n_total - n_corr_total,
            "correction_partial_note": (
                "6 对 R 反转 (R1a..R6a) 前半 pair_pending; 后半未闭合; "
                "如实声明 partial 处理: 主读法 = 全 37 含 partial; "
                "替代读法 = 剔除 partial 仅用 31 normal"),
        },
        "constraint": {
            "no_llm": True, "no_proxy": True, "no_gateway": True,
            "hash_lib": "zlib.crc32 + hashlib.sha256 (禁内建 hash())",
            "seed": SEED,
            "tree_depth_max": TREE_DEPTH_MAX,
            "n_perm": N_PERM, "alpha": ALPHA,
            "n_boot": N_BOOT, "ci_floor": CI_FLOOR,
            "th_similarity": TH_SIMILARITY,
            "th_blind_obey": TH_BLIND_OBEY,
            "th_critical_cov": TH_CRITICAL_COV,
        },
        "operationalization_v1": {
            "judgment_type_extraction": (
                "6 类 (KILL_LINE/COST/CRITERIA/RISK/TIMING/DELEGATE); "
                "对 reasoning_full 字符串做确定性格式扫描; "
                "类型按关键词首现位置序排序后去重; "
                "primary = 首元素; 空序列归 UNKNOWN (相似度=0)"
            ),
            "structural_similarity": (
                "单事件 = |pred ∩ actual| / |actual| (实际序列召回率); "
                "整体 = held-out per-event 均值"
            ),
            "critical_reflection_markers": list(CRITICAL_REFLECTION_MARKERS),
            "div_critical_coverage": (
                "#(分歧∧含批判反思标志词) / #(分歧); 无分歧 → 1.0"
            ),
            "blind_obey_rate": (
                "#(一致∧不含批判反思标志词) / #(一致); 无一致 → 0.0"
            ),
            "stratified_split": (
                "0.30 分层: 纠偏子集 + 正常子集 各自 round(N*0.30); "
                "max(1, ...) 防 0 划分; held-out 必含纠偏事件 (6 对 R 反转前半)"
            ),
            "permutation_test": (
                "shuffle 标签 n=1000, 重训决策树, 计 perm_sim ≥ obs_mean 比例; "
                "p_perm = (ge+1)/(N_PERM+1)"
            ),
            "bootstrap_ci": (
                "percentile method; resample held-out per-event sim n=1000; "
                "CI 95% = [2.5%, 97.5%]"
            ),
            "double_read_method": (
                "主读法 = 全 37 含 partial; 替代读法 = 仅 31 normal (剔除 R*a_pair_pending); "
                "两读法结果如实并报, 不合并, 不择优"
            ),
        },
        "main_reading": {
            "held_out_count": main_metrics["n_held"],
            "held_out_idx": held_main,
            "n_correction_in_held": main_metrics["n_corr_in_held"],
            "mean_similarity": round(main_metrics["mean_similarity"], 4),
            "div_critical_coverage": round(main_metrics["div_critical_coverage"], 4),
            "n_divergent": main_metrics["n_divergent"],
            "n_critical_among_divergent": main_metrics["n_critical_among_divergent"],
            "blind_obey_rate": round(main_metrics["blind_obey_rate"], 4),
            "n_agree": main_metrics["n_agree"],
            "n_blind_obey": main_metrics["n_blind_obey"],
            "perm_p": round(main_metrics["perm_p"], 4),
            "perm_n": main_metrics["perm_n"],
            "alpha": main_metrics["alpha"],
            "bootstrap_ci": [
                round(main_metrics["bootstrap_ci"][0], 4),
                round(main_metrics["bootstrap_ci"][1], 4),
            ],
            "bootstrap_n": main_metrics["bootstrap_n"],
            "label_distribution": main_metrics["label_distribution"],
            "per_event": [
                {
                    "held_idx": held_main[k],
                    "sim": round(main_metrics["per_event"]["sim"][k], 4),
                    "pred": main_metrics["per_event"]["pred"][k],
                    "actual": main_metrics["per_event"]["actual"][k],
                    "divergent": main_metrics["per_event"]["divergent"][k],
                    "has_critical_reflection": main_metrics["per_event"]["critical"][k],
                }
                for k in range(len(held_main))
            ],
        },
        "alt_reading": {
            "subset": "剔除 R*a_pair_pending (6 partial) → 31 normal events",
            "held_out_count": alt_metrics["n_held"],
            "held_out_idx": held_alt,
            "mean_similarity": round(alt_metrics["mean_similarity"], 4),
            "div_critical_coverage": round(alt_metrics["div_critical_coverage"], 4),
            "blind_obey_rate": round(alt_metrics["blind_obey_rate"], 4),
            "perm_p": round(alt_metrics["perm_p"], 4),
            "bootstrap_ci": [
                round(alt_metrics["bootstrap_ci"][0], 4),
                round(alt_metrics["bootstrap_ci"][1], 4),
            ],
            "disagreement_vs_main": {
                "mean_similarity_delta": round(
                    alt_metrics["mean_similarity"] - main_metrics["mean_similarity"], 4),
                "blind_obey_delta": round(
                    alt_metrics["blind_obey_rate"] - main_metrics["blind_obey_rate"], 4),
                "note": "如实并报; 不合并, 不择优",
            },
        },
        "kill_lines": kill_lines,
        "any_hit": any_hit,
        "verdict": ("FAIL (exploratory, 探索性预跑, 非正式判定)"
                    if any_hit else "PASS (exploratory, 探索性预跑, 非正式判定)"),
        "root_cause_3class": root,
        "root_cause_per_row": root_cause_per_row,
        "exploratory_label": exploratory_label,
        "boundary_statement": (
            "v2.2 §7: 非画像 (不预测 PI 行为/不做个人模型外传); "
            "产物=方法规则集供 AI 内化; 推理全文隐私面仅入本地件; "
            "0 LLM 采集; key 0 相关; 生效即锁不重开; 起跑 = 补测完成 + TH-v2-1/2/3 达标"
        ),
    }
    OUT_RESULT.write_text(
        json.dumps(result, ensure_ascii=False, indent=1),
        encoding="utf-8",
    )

    # 10. 回报 (stdout)
    return {
        "ruleset_sha12": sha12_file(OUT_RULESET),
        "ruleset_size": OUT_RULESET.stat().st_size,
        "result_sha12": sha12_file(OUT_RESULT),
        "result_size": OUT_RESULT.stat().st_size,
        "n_total": n_total,
        "n_correction_partial": n_corr_total,
        "main_mean_sim": round(main_metrics["mean_similarity"], 4),
        "main_blind": round(main_metrics["blind_obey_rate"], 4),
        "main_div_cov": round(main_metrics["div_critical_coverage"], 4),
        "main_perm_p": round(main_metrics["perm_p"], 4),
        "main_ci": [round(main_metrics["bootstrap_ci"][0], 4),
                    round(main_metrics["bootstrap_ci"][1], 4)],
        "alt_mean_sim": round(alt_metrics["mean_similarity"], 4),
        "alt_blind": round(alt_metrics["blind_obey_rate"], 4),
        "alt_div_cov": round(alt_metrics["div_critical_coverage"], 4),
        "alt_perm_p": round(alt_metrics["perm_p"], 4),
        "alt_ci": [round(alt_metrics["bootstrap_ci"][0], 4),
                   round(alt_metrics["bootstrap_ci"][1], 4)],
        "any_hit": any_hit,
        "verdict": ("FAIL (exploratory)" if any_hit
                    else "PASS (exploratory)"),
        "root_cause": root,
        "exploratory": True,
        "unmet_conditions_count": len(unmet),
    }


if __name__ == "__main__":
    summary = main()
    print(json.dumps(summary, ensure_ascii=False, indent=1))