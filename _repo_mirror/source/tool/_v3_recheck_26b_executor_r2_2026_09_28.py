#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
V3-R #26 P-J 收敛盆地 — 三本体正式实验 executor（**26b r2 修订版** · worker · 2026-09-28）

**r2 修订说明（PI 2026-09-28 22:40 授权改实现 · ask_c6721836fb0a2e1af6c12f37 q1）**：
  源件 `results/_v3_recheck_26b_executor_2026_09_27.py`（`5c906113a210`）**byte 0 触动**，本件为**新名修订件**。
  唯一修改面 = `judge_K_V3R_26` 的 `UNDECIDED_BY_LITERAL_GAP` 分支：按**归属终局表**
  `results/_v5_item26b_attribution_effective_2026_09_28.md`（`c353fbcdc753` §3.1）第 2 / 4 行
  改落 **FAIL + γ 双口径成对**（分支 A / 分支 B 各落不同强制 γ 根因）。
  **0 新设阈值**（终局表所用数值 1 / 3 / 4 / 0.05 / 100 全部为既有值）、**0 私设切点**、
  **0 新增第四态**（C3 + `R-∧` 属判据结构 / 判据适用面定义，0 引入任何数值）。

性质：**正式判定档**（区别于 26 系列 preexp = 探索性档）。本件出 K-V3R-26 逐本体正式 verdict。
  触发自 PI 2026-09-27 问卷 ask_75126c38abf2c134a1591672 Q1「三本体全跑」——
  O5（3 态 replicator ODE＋软竞争，主推）+ O1（离散 cell 重分配，基线）+ O3（logit 正规形，交叉校验）。

**0 覆盖不改判预实验件**：preexp 三件（data 177c88e1bd82 / report 0a2b5c837c83 / executor 775217a462f5）
  只作只读输入 + 一致性核对面，0 字节触动；26 系列第一梯队三件（46c326c756c3 / eb6a99dd46dd /
  3d9ad5f1540d）同样只读。

形式锚（字面沿用，0 擅调）：
  K-V3R-26（prereg §2.2 字面）= P-J 重构造（真 convergence_rate 定义 + 真 perturbation ±0.05×100）后
    convergence_rate n_distinct > 3 + std > 0 → PASS（改判）；仍 n_distinct ≤ 1 → FAIL（维持假证伪）
  TH-V3R-26（prereg §2.4 字面）= convergence_rate 形式 n_iter / n_budget；本件冻结
    convergence_rate_m = mean_j(n_iter_j) / n_budget, n_budget = 100
  jitter = ±0.05 uniform on T_frac60（clip [0,1]）；seed = 20260927

  **kill-line 字面空档 → 终局归属（r2 改）**：K-V3R-26 字面只定义 n_distinct ≥ 4（PASS）与 n_distinct ≤ 1（FAIL）
  两端，**2 ≤ n_distinct ≤ 3 落在字面空档**。**源件**对空档输出 `UNDECIDED_BY_LITERAL_GAP`（该字面 =
  「不明」形态，已被 PI 2026-09-28 20:02 封死）；**r2 依归属终局表 `c353fbcdc753` §3.1 改落 FAIL + 强制 γ**：
    · 分支 A（`2 ≤ n_distinct ≤ 3`，任意 std）→ **FAIL**，γ = 「弱分布 / 退化警报域」；
    · 分支 B（`n_distinct ≥ 4 ∧ std = 0`）→ **FAIL**，γ = 「方差恒同 ⇒ 判据退化」（R-∧ 合取完整性）。
  其余两域（`n_distinct ≤ 1` FAIL / `n_distinct > 3 ∧ std > 0` PASS）**逐字 0 改动**；
  **0 新设阈值、0 私设切点**（沿 K-V3R-0-B / 预登记 §2.2 9 条不动声明）。

本体（3 个 = PI 拍板，构造字面逐字沿 preexp executor，0 改动实现常数）：
  O1 discrete_cell_redistribution   离散 cell 重分配（基线 = 第一梯队已落地）
  O3 logit_normal_form             logit 正规形（交叉校验）
  O5 replicator_ode_softlimit      连续时间 replicator ODE + 软竞争（3 态，主推）
  排除的 O2 / O4 不在本次正式跑范围（preexp §6 结构性排除，本件 0 重议）。

**双口径（K-V3R-0-C）**：new_verdict（沿新构造，本体逐个）+ legacy_verdict（沿原 V3 阈值字面 = 盘上
  P-J JSON 的 9/9 ≡ 0.1，判据退化 ⇒ UNVERIFIED；该面本体无关，逐本体共享同一读数）。

**三本体汇总（派工单字面）**：同向 ⇒ 改判建议按同向给；分歧 ⇒ 维持原标注 + 登记分歧 + γ。

**O5 保留意见处置（硬）**：同报逐 model 最小目标分量 f_target_min_component + ρ(最小分量, n_iter_mean)，
  并把「最小份额瓶颈」这一**机制性成分**与「T_frac60 / 盆地深度」成分显式拆开登记（诊断面，0 判据）。

S-40 布尔显式命名（方向显式；r2 扩到 judge 返回字典）：`*_hit = True` = **触发**（触发警报/失败）；
  `*_pass = True` = **未触发**（合格/存活）。judge 返回字段名一律自带方向（`kill_line_fail_hit` /
  `kill_line_pass`），0 出现无方向的 `hit` / `flag` 类命名。
"""

import hashlib
import json
import os
import sys
from pathlib import Path

import numpy as np

# ---- 冻结构造常量（沿 preexp executor / TH-V3R-26 字面，0 新设判定阈值）----
SEED = 20260927
N_BUDGET = 100
JITTER = 0.05
N_CELLS = 60
CLASSES = ("T", "R", "A")
PRIORITY = "surplus_first"

# ---- K-V3R-26 字面阈值（沿 prereg §2.2，0 擅调）----
KV3R_26_PASS_N_DISTINCT_MIN = 4       # n_distinct > 3
KV3R_26_FAIL_N_DISTINCT_MAX = 1       # n_distinct ≤ 1
# 字面空档（r2 终局化）：2 ≤ n_distinct ≤ 3 = 分支 A；n_distinct ≥ 4 ∧ std = 0 = 分支 B
#   两者均落 FAIL 但 γ 根因不同（沿 c353fbcdc753 §3.1 第 2 / 4 行；0 私设条款、0 新设数值）

# ---- 强制 γ 根因字面（逐字沿 c353fbcdc753 §3.1 终局表；0 改写、0 新造）----
GAMMA_ROOT_CAUSE_N_LE_1 = "构造常量"            # 终局表第 1 行
GAMMA_ROOT_CAUSE_GAP_A = "弱分布 / 退化警报域"  # 终局表第 2 行（分支 A）
GAMMA_ROOT_CAUSE_GAP_B = "方差恒同 ⇒ 判据退化"  # 终局表第 4 行（分支 B）

# ---- 防退化门 K-V3R-0-A 字面（n_distinct > 3 且 std > 0）----
DEGEN_N_DISTINCT_MIN = 4
DEGEN_STD_MIN_EXCL = 0.0

# ---- 各本体实现常数（逐字沿 preexp executor；实现自由度，非判据）----
TOL = 1e-6
O1_MAX_STEP = 60
O3_S, O3_CAP = 0.25, 100000
O5_DT, O5_CAP, O5_C = 0.05, 200000, 0.5

ONTOLOGIES = ("O1_discrete_cell_redistribution",
              "O3_logit_normal_form",
              "O5_replicator_ode_softlimit")
O1 = "O1_discrete_cell_redistribution"
O3 = "O3_logit_normal_form"
O5 = "O5_replicator_ode_softlimit"

KILL_LINE_LITERAL = ("K-V3R-26: P-J 重构造（真 convergence_rate 定义 + 真 perturbation ±0.05×100）后 "
                    "convergence_rate n_distinct > 3 + std > 0 → PASS（改判）；"
                    "仍 n_distinct ≤ 1 → FAIL（维持假证伪）")
TH_LITERAL = ("TH-V3R-26: convergence_rate 形式（无预注册阈值，由 K-V3R-26 重定义）"
              "= n_iter / n_budget")


def _repo_root() -> Path:
    starts = [Path(os.getcwd()), Path(os.path.abspath(sys.argv[0])).parent]
    for base in starts:
        p = base
        for _ in range(6):
            if (p / "results/_v3_recheck_prereg_v1_2026_09_27.md").exists():
                return p
            p = p.parent
    raise SystemExit("repo root not found (cwd=%s)" % os.getcwd())


REPO = _repo_root()
PREREG = REPO / "results/_v3_recheck_prereg_v1_2026_09_27.md"
EXEC_BASE = REPO / "results/_v3_recheck_26_executor_2026_09_27.py"
BASE_RESULT = REPO / "results/_v3_recheck_26_result_2026_09_27.json"
BASE_RESCRIPT = REPO / "results/_v3_recheck_26_rescript_2026_09_27.md"
PREEXP_DATA = REPO / "results/_v3_recheck_26_preexp_data_2026_09_27.json"
PREEXP_REPORT = REPO / "results/_v3_recheck_26_preexp_report_2026_09_27.md"
PREEXP_EXEC = REPO / "results/_v3_recheck_26_preexp_executor_2026_09_27.py"
SRC_PJ = REPO / "results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json"
SRC_60 = REPO / "results/deposon_v3_physical_opt_60cells_2026_09_11.json"
# r2：本件落**新名**派生件，0 覆写 26b 原派生件（沿 K-V3R-0-D 派生 JSON 不合并）
OUT = REPO / "results/_v3_recheck_26b_r2_result_2026_09_28.json"


def sha12(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:12]


def canon_sha12(obj) -> str:
    return sha12(json.dumps(obj, ensure_ascii=False, sort_keys=True,
                            separators=(",", ":")).encode("utf-8"))


def n_distinct(xs) -> int:
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    a = np.asarray(xs, dtype=float)
    q1, q3 = (float(v) for v in np.percentile(a, [25, 75]))
    mean = float(a.mean())
    std = float(a.std(ddof=0))
    return {
        "n": int(a.size),
        "n_distinct": n_distinct(a),
        "std": std,
        "rel_std": float(std / mean) if mean != 0.0 else None,
        "min": float(a.min()),
        "max": float(a.max()),
        "mean": mean,
        "median": float(np.median(a)),
        "iqr": q3 - q1,
    }


def spearman(x, y):
    """秩相关（并列取平均秩）。任一侧零方差 -> None（无定义）。"""
    a, b = np.asarray(x, float), np.asarray(y, float)
    if a.std() == 0 or b.std() == 0:
        return None

    def rank(v):
        order = np.argsort(v, kind="mergesort")
        r = np.empty(len(v), float)
        s = v[order]
        i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and s[j + 1] == s[i]:
                j += 1
            r[order[i:j + 1]] = (i + j) / 2.0 + 1.0
            i = j + 1
        return r

    ra, rb = rank(a) - rank(a).mean(), rank(b) - rank(b).mean()
    return float((ra * rb).sum() / np.sqrt((ra ** 2).sum() * (rb ** 2).sum()))


def ols_r2(y, *predictors):
    """最小二乘 R²（闭式 lstsq，无随机性）。k=0 预测器 -> 0.0。"""
    yv = np.asarray(y, float)
    if not predictors:
        return 0.0
    X = np.column_stack([np.ones(len(yv))] + [np.asarray(p, float) for p in predictors])
    beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
    resid = yv - X @ beta
    ss_tot = float(((yv - yv.mean()) ** 2).sum())
    if ss_tot == 0.0:
        return None
    return float(1.0 - (resid ** 2).sum() / ss_tot)


# ======================================================================
# 扰动抽样面：与第一梯队 / preexp 同一 rng 流 => 配对抽样沿预实验约定
# ======================================================================
def draw_perturbation(models, t_frac60):
    rng = np.random.default_rng(SEED)
    table = []
    for idx in range(len(models)):
        t60 = float(t_frac60[idx])
        row = [float(np.clip(t60 + rng.uniform(-JITTER, JITTER), 0.0, 1.0))
               for _ in range(N_BUDGET)]
        table.append(row)
    return table


def target_triple(t0, r0, a0, t_target):
    """第一梯队 executor 字面：R/A 按盘上真实 r0:a0 比例吸收 T 份额差额。"""
    rest = N_CELLS - int(t_target)
    denom = r0 + a0
    if denom == 0:
        return {"T": int(t_target), "R": rest, "A": 0}
    r_target = int(round(rest * r0 / denom))
    return {"T": int(t_target), "R": r_target, "A": rest - r_target}


# ======================================================================
# O1 离散 cell 重分配（基线，逐字沿 preexp / 第一梯队 redistribute_n_iter）
# ======================================================================
def redistribute_n_iter(t0: int, r0: int, a0: int, t_target: int, priority: str) -> int:
    t, r, a = int(t0), int(r0), int(a0)
    tgt = target_triple(t0, r0, a0, t_target)
    for step in range(1, O1_MAX_STEP + 1):
        cur = {"T": t, "R": r, "A": a}
        if cur == tgt:
            return step - 1
        if priority == "surplus_first":
            src = max(CLASSES, key=lambda c: (cur[c] - tgt[c], -CLASSES.index(c)))
            dst = max((c for c in CLASSES if c != src),
                      key=lambda c: (tgt[c] - cur[c], -CLASSES.index(c)))
        else:
            order = ("T", "R", "A") if priority == "class_order_TRA" else ("A", "R", "T")
            src = next(c for c in order if cur[c] > tgt[c])
            dst = next(c for c in reversed(order) if cur[c] < tgt[c])
        if src == dst:
            return step - 1
        cur[src] -= 1
        cur[dst] += 1
        t, r, a = cur["T"], cur["R"], cur["A"]
    return O1_MAX_STEP


# ======================================================================
# 向量化首达时求解器（逐字沿 preexp executor；已命中的抽冻结）
# ======================================================================
def run_vec(step_fn, hit_fn, state, cap, params=()):
    n = len(state)
    n_iter = np.full(n, -1, dtype=np.int64)
    final = np.array(state, dtype=float, copy=True)
    act = np.arange(n)
    ps = [np.asarray(p, float) for p in params]
    h = hit_fn(state, ps)
    if bool(h.any()):
        n_iter[act[h]] = 0
        keep = ~h
        act, state, ps = act[keep], state[keep], [p[keep] for p in ps]
    for k in range(1, cap + 1):
        if act.size == 0:
            break
        state = step_fn(state, ps)
        final[act] = state
        h = hit_fn(state, ps)
        if bool(h.any()):
            n_iter[act[h]] = k
            keep = ~h
            act, state, ps = act[keep], state[keep], [p[keep] for p in ps]
    n_iter[n_iter < 0] = cap
    return n_iter, final


# ======================================================================
# O3 logit 正规形（逐字沿 preexp executor；已含 PR-1 修正后的 params 字面）
#   logit(x_{k+1}) = (1−s)·logit(x_k) + s·(f_T − f_A)，f_T − f_A = logit(x0)
#   内点不动点 = x0；命中判据 |x − x0| <= TOL
# ======================================================================
def o3_run(x_start, x_target):
    x_target = np.asarray(x_target, float)
    lg_target = np.log(x_target / (1.0 - x_target))

    def step(x, ps):
        lg = np.log(x / (1.0 - x))
        return 1.0 / (1.0 + np.exp(-((1.0 - O3_S) * lg + O3_S * ps[1])))

    def hit(x, ps):
        return np.abs(x - ps[0]) <= TOL

    return run_vec(step, hit, np.asarray(x_start, float).copy(), O3_CAP,
                   (x_target, lg_target))


# ======================================================================
# O5 连续时间 replicator ODE + 软竞争（逐字沿 preexp executor）
#   ẋ_i = x_i(g_i − ḡ)，g_i = c·(f_i − x_i)，c=0.5，RK4 dt=0.05
#   内点不动点 = f（3 态归一化份额）；命中判据 max_i |x_i − f_i| <= TOL
# ======================================================================
def o5_run(x_start3, f_target3):
    f = np.asarray(f_target3, float).copy()

    def rhs(x, ps):
        g = O5_C * (ps[0] - x)
        gbar = (x * g).sum(axis=1)
        return x * (g - gbar[:, None])

    def step(x, ps):
        k1 = rhs(x, ps)
        k2 = rhs(x + 0.5 * O5_DT * k1, ps)
        k3 = rhs(x + 0.5 * O5_DT * k2, ps)
        k4 = rhs(x + O5_DT * k3, ps)
        xn = x + (O5_DT / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
        return np.clip(xn, 0.0, 1.0)

    def hit(x, ps):
        return np.max(np.abs(x - ps[0]), axis=1) <= TOL

    return run_vec(step, hit, np.asarray(x_start3, float).copy(), O5_CAP, (f,))


# ======================================================================
# K-V3R-26 判定器（r2：字面空档按归属终局表终局化为 FAIL + 强制 γ 根因）
#   授权 = PI 2026-09-28 22:40（ask_c6721836fb0a2e1af6c12f37 q1）授权改实现
#   依据 = 归属终局表 c353fbcdc753 §3.1（0 新设阈值、0 私设切点、0 新增第四态）
# ======================================================================
def judge_K_V3R_26(nd: int, std: float) -> dict:
    """沿 prereg §2.2 K-V3R-26 字面 + 归属终局表（c353fbcdc753 §3.1）逐行判定。

    返回字典；**布尔字段名自带方向**（沿 S-40 纪律：`kill_line_fail_hit = True` = 触发 FAIL 警报；
    `kill_line_pass = True` = 合格/存活），不出现无方向的 `hit` / `flag` 命名。
    γ 双口径成对（K-V3R-0-C / K-V5R2-26B-0-F）：本函数只出 new 面，
    `legacy_verdict` 由调用方与本结果并排给出，缺任一腿 = 无效登记。
    """
    if nd > 3 and std > 0.0:
        return {
            "new_verdict": "PASS",
            "kill_line_fail_hit": False,
            "kill_line_pass": True,
            "branch_id": "ND_GT_3_AND_STD_GT_0",
            "kill_line_branch_literal": "n_distinct>3 且 std>0 → PASS（改判）",
            "gamma_root_cause": None,               # 终局表第 3 行：0 强制 γ
            "gamma_source_row": 3,
        }
    if nd <= 1:
        return {
            "new_verdict": "FAIL",
            "kill_line_fail_hit": True,
            "kill_line_pass": False,
            "branch_id": "ND_LE_1",
            "kill_line_branch_literal": "n_distinct ≤ 1 → FAIL（维持假证伪）",
            "gamma_root_cause": GAMMA_ROOT_CAUSE_N_LE_1,
            "gamma_source_row": 1,
        }
    if nd <= 3:
        # 分支 A（字面空档 · C3 端点连续性枝）：2 ≤ n_distinct ≤ 3
        #   开区间 (2,3) 内 0 端点（端点为整数 1 与 4）⇒ V(2) = V(3) ⇒ 连续于 FAIL 端点 ⇒ 全归 FAIL
        return {
            "new_verdict": "FAIL",
            "kill_line_fail_hit": True,
            "kill_line_pass": False,
            "branch_id": "GAP_A_ND_2_TO_3",
            "kill_line_branch_literal": ("2 ≤ n_distinct ≤ 3（字面空档 · 分支 A）→ FAIL（归属终局表 §3.1 "
                                         "第 2 行；依据 C3 端点连续性：与 n_distinct=1 的 FAIL 锚同侧，"
                                         "与 n_distinct ≤ 3 退化警报域同向）"),
            "gamma_root_cause": GAMMA_ROOT_CAUSE_GAP_A,
            "gamma_source_row": 2,
        }
    if std == 0.0:
        # 分支 B（R-∧ 合取完整性枝）：n_distinct ≥ 4 但 std = 0
        #   PASS 合取项 std > 0 不成立 ⇒ 0 落 PASS ⇒ 落 FAIL 侧（FAIL 侧无合取约束）
        return {
            "new_verdict": "FAIL",
            "kill_line_fail_hit": True,
            "kill_line_pass": False,
            "branch_id": "GAP_B_ND_GE_4_AND_STD_EQ_0",
            "kill_line_branch_literal": ("n_distinct ≥ 4 且 std = 0（分支 B）→ FAIL（归属终局表 §3.1 "
                                         "第 4 行；依据 R-∧ 合取完整性：PASS 合取项 std>0 不成立）"),
            "gamma_root_cause": GAMMA_ROOT_CAUSE_GAP_B,
            "gamma_source_row": 4,
        }
    # 终局表第 5 行（KD：读数不可算/非有限/构造跑不完）—— 本件 0 新增第四/第五态，
    # 改为显式拦截：0 静默落入分支 B（否则 γ 根因会被误标；诚实 = 0 误导）。
    raise SystemExit("终局表第 5 行（KD：读数不可算/非有限）未实现于本件：n=%r, std=%r —— 0 静默归入分支 B"
                     % (nd, std))


def draw_block(by_model, cap):
    flat = np.concatenate(by_model)
    return {
        "n": int(flat.size),
        "n_iter_n_distinct": n_distinct(flat),
        "floor_share_n_iter_eq_0": float((flat == 0).mean()),
        "cap_hit_share_n_iter_eq_cap": float((flat == cap).mean()),
        "rail_share_0_or_cap": float(((flat == 0) | (flat == cap)).mean()),
        "n_iter_mean": float(flat.mean()),
        "n_iter_median": float(np.median(flat)),
        "n_iter_max": int(flat.max()),
        "total_steps": int(flat.sum()),
    }


def main() -> int:
    pj = json.loads(SRC_PJ.read_text(encoding="utf-8"))
    s60 = json.loads(SRC_60.read_text(encoding="utf-8"))
    base = json.loads(BASE_RESULT.read_text(encoding="utf-8"))
    preexp = json.loads(PREEXP_DATA.read_text(encoding="utf-8"))

    pj_all = pj["all_results"]
    s60_by_name = {m["model"]: m for m in s60["P_C_distortion_bound_60cells"]["per_model"]}
    models = list(pj_all["convergence_rates"].keys())
    t_frac60 = list(pj_all["T_frac60"])
    assert len(models) == len(t_frac60) == 9, "输入不是 9 model"
    for m in models:
        rec = s60_by_name[m]
        assert rec["T60"] + rec["R60"] + rec["A60"] == N_CELLS, "60-cell 守恒被破坏: %s" % m

    # ==============================================================
    # §0 K-V3R-0-A 防退化门跑前自证（对盘上输入字段；先于任何正式跑）
    # ==============================================================
    pre_run_gate = {
        "gate_literal": "K-V3R-0-A：n_distinct > 3 + std > 0；任一输入字段 n_distinct ≤ 3 = 退化警报",
        "fields": {},
    }
    gate_alarm = False
    in_t = stat_block(t_frac60)
    pre_run_gate["fields"]["pj_T_frac60"] = {
        "n": in_t["n"], "n_distinct": in_t["n_distinct"], "std": in_t["std"],
        "gate_pass": bool(in_t["n_distinct"] >= DEGEN_N_DISTINCT_MIN
                          and in_t["std"] > DEGEN_STD_MIN_EXCL)}
    gate_alarm = gate_alarm or not pre_run_gate["fields"]["pj_T_frac60"]["gate_pass"]
    for fld in ("cos_sim", "D_fix2_cosine", "T30"):
        v = [s60_by_name[m][fld] for m in models]
        s = stat_block(v)
        pre_run_gate["fields"]["60cells_" + fld] = {
            "n": s["n"], "n_distinct": s["n_distinct"], "std": s["std"],
            "gate_pass": bool(s["n_distinct"] >= DEGEN_N_DISTINCT_MIN
                              and s["std"] > DEGEN_STD_MIN_EXCL)}
        gate_alarm = gate_alarm or not pre_run_gate["fields"]["60cells_" + fld]["gate_pass"]
    legacy = [float(pj_all["convergence_rates"][m]) for m in models]
    s = stat_block(legacy)
    pre_run_gate["fields"]["pj_legacy_convergence_rates_CONTROL"] = {
        "n": s["n"], "n_distinct": s["n_distinct"], "std": s["std"],
        "gate_pass": bool(s["n_distinct"] >= DEGEN_N_DISTINCT_MIN
                          and s["std"] > DEGEN_STD_MIN_EXCL),
        "note": "对照组：原 V3 判据输入预期退化（沿 prereg §2.2 K-V3R-26「仍 n_distinct ≤ 1 → FAIL」"
                "的预期对象），不计入 gate_alarm（K-V3R-0-A 的自证对象是新构造的输入面，非原标注面）"}
    pre_run_gate["degenerate_alarm_hit"] = bool(gate_alarm)
    if gate_alarm:
        raise SystemExit("K-V3R-0-A 退化警报触发：输入面退化，不许带病开跑")

    # ==============================================================
    # §1 扰动抽样（配对：3 本体共用同一批抽样，沿预实验约定）
    # ==============================================================
    pert = draw_perturbation(models, t_frac60)
    pert_sha12 = canon_sha12(pert)
    pert_matches_preexp = bool(pert_sha12 == preexp["construct"]["perturbation_table_sha12"])

    # ---------------- O1 离散 cell 重分配（基线） ----------------
    o1_by_model = []
    o1_info = []
    for idx, m in enumerate(models):
        rec = s60_by_name[m]
        t0, r0, a0 = int(rec["T60"]), int(rec["R60"]), int(rec["A60"])
        it = np.asarray([redistribute_n_iter(t0, r0, a0,
                                             int(round(pert[idx][j] * N_CELLS)),
                                             PRIORITY) for j in range(N_BUDGET)], float)
        o1_by_model.append(it)
        o1_info.append({"model": m, "start_triple_TRA": [t0, r0, a0],
                        "n_iter_mean": float(it.mean()), "n_iter_min": int(it.min()),
                        "n_iter_max": int(it.max()), "n_iter_distinct": n_distinct(it),
                        "convergence_rate": float(it.mean() / N_BUDGET)})

    # ---------------- O3 logit 正规形（2 态） ----------------
    x_start2 = [float(s60_by_name[m]["T60"]) / N_CELLS for m in models]
    o3_by_model, o3_final = [], []
    for idx, m in enumerate(models):
        st = np.full(N_BUDGET, x_start2[idx], float)
        it, fin = o3_run(st, np.asarray(pert[idx], float))
        o3_by_model.append(it.astype(float))
        o3_final.append(fin)
    o3_info = [{"model": models[idx], "T_frac60_real": t_frac60[idx],
                "n_iter_mean": float(o3_by_model[idx].mean()),
                "n_iter_min": int(o3_by_model[idx].min()),
                "n_iter_max": int(o3_by_model[idx].max()),
                "n_iter_distinct": n_distinct(o3_by_model[idx]),
                "convergence_rate": float(o3_by_model[idx].mean() / N_BUDGET)}
               for idx in range(len(models))]

    # ---------------- O5 3 态 replicator ODE + 软竞争（主推） ----------------
    o5_by_model, o5_info, o5_f3, o5_final = [], [], [], []
    for idx, m in enumerate(models):
        rec = s60_by_name[m]
        t0, r0, a0 = int(rec["T60"]), int(rec["R60"]), int(rec["A60"])
        denom = r0 + a0
        f3 = np.zeros((N_BUDGET, 3), float)
        for j, x0 in enumerate(pert[idx]):
            rest = 1.0 - x0
            if denom == 0:
                f3[j] = (x0, rest, 0.0)
            else:
                rc = rest * r0 / denom
                f3[j] = (x0, rc, rest - rc)
        st3 = np.tile(np.asarray([t0, r0, a0], float) / N_CELLS, (N_BUDGET, 1))
        it, fin = o5_run(st3, f3)
        o5_by_model.append(it.astype(float))
        o5_final.append(fin)
        o5_f3.append(f3)
        o5_info.append({"model": m, "start_triple_TRA": [t0, r0, a0],
                        "f_target_min_component": float(f3.min(axis=1).min()),
                        "f_target_min_component_class": CLASSES[int(np.argmin(f3.min(axis=0)))],
                        "f_target_min_component_draw_index": int(np.argmin(f3.min(axis=1))),
                        "f_target_triple_at_min_draw": [float(v) for v in f3[int(np.argmin(f3.min(axis=1)))]],
                        "f_target_per_component_minima_over_draws": [float(v) for v in f3.min(axis=0)],
                        "f_target_field_note": ("f_target_min_component = 逐抽三元组最小分量的最小值；"
                                                "f_target_triple_at_min_draw = 取得该全局最小值的那一抽的"
                                                "完整三元组；f_target_per_component_minima_over_draws = "
                                                "每个分量各自在 100 抽上的最小值（**不是**同一抽的三元组，"
                                                "两字段口径不同，不得混读）"),
                        "n_iter_mean": float(it.mean()), "n_iter_min": int(it.min()),
                        "n_iter_max": int(it.max()), "n_iter_distinct": n_distinct(it),
                        "convergence_rate": float(it.mean() / N_BUDGET)})

    by_model = {O1: o1_by_model, O3: o3_by_model, O5: o5_by_model}
    per_model_info = {O1: o1_info, O3: o3_info, O5: o5_info}
    caps = {O1: O1_MAX_STEP, O3: O3_CAP, O5: O5_CAP}

    # 终态到扰动目标的距离（语义对题性诊断，不作判据）
    tgt_dist = {}
    o1_resid = []
    for idx, m in enumerate(models):
        t0 = int(s60_by_name[m]["T60"])
        it = by_model[O1][idx]
        o1_resid.extend([0.0 if v < O1_MAX_STEP else float(abs(t0 - int(round(x * N_CELLS))))
                         for v, x in zip(it, pert[idx])])
    tgt_dist[O1] = {"metric": "|T_final − T*|（cell）", "mean": float(np.mean(o1_resid)),
                    "median": float(np.median(o1_resid)), "max": float(np.max(o1_resid))}
    d3 = np.concatenate([np.abs(f - np.asarray(p, float))
                         for f, p in zip(o3_final, pert)])
    tgt_dist[O3] = {"metric": "|x_final − x0|（T 份额）", "mean": float(d3.mean()),
                    "median": float(np.median(d3)), "max": float(d3.max())}
    d5 = np.concatenate([np.max(np.abs(f - t), axis=1) for f, t in zip(o5_final, o5_f3)])
    tgt_dist[O5] = {"metric": "max_i |x_i − f_i|（三元组份额）", "mean": float(d5.mean()),
                    "median": float(np.median(d5)), "max": float(d5.max())}

    # ==============================================================
    # §2 逐本体 K-V3R-26 正式判定 + 双口径
    # ==============================================================
    legacy_nd = n_distinct(legacy)
    legacy_std = float(np.std(np.asarray(legacy, float), ddof=0))
    legacy_verdict = ("UNVERIFIED（判据退化）" if legacy_nd <= 1
                      else "原口径非退化（与首跑实测不符，须人工复核）")

    ontologies = {}
    for name in ONTOLOGIES:
        rates = [p["convergence_rate"] for p in per_model_info[name]]
        rs = stat_block(rates)
        jd = judge_K_V3R_26(rs["n_distinct"], rs["std"])
        verdict = jd["new_verdict"]
        db = draw_block(by_model[name], caps[name])
        # T_frac60 相同的配对内 rate 差（信息量诊断）
        gaps = [abs(rates[i] - rates[j]) / ((rates[i] + rates[j]) / 2.0)
                for i in range(len(models)) for j in range(i + 1, len(models))
                if abs(t_frac60[i] - t_frac60[j]) < 1e-12 and rates[i] > 0 and rates[j] > 0]
        ontologies[name] = {
            "n_iter_cap": caps[name],
            "new_verdict": verdict,
            "kill_line_fail_hit": jd["kill_line_fail_hit"],   # True = 触发 FAIL（方向显式命名）
            "kill_line_pass": jd["kill_line_pass"],           # True = 合格/存活
            "kill_line_branch_id": jd["branch_id"],
            "kill_line_branch_literal": jd["kill_line_branch_literal"],
            "gamma_root_cause": jd["gamma_root_cause"],
            "gamma_source": ("K-V3R-26 字面（88052d7db895 L118：n_distinct ≤ 1 / >3 且 std>0）"
                             if jd["gamma_source_row"] in (1, 3)
                             else ("归属终局表 c353fbcdc753 §3.1 第 %d 行（PI 2026-09-28 22:15 拍板 ①+②；"
                                   "PI 2026-09-28 22:40 ask_c6721836fb0a2e1af6c12f37 q1 授权改实现）"
                                   % jd["gamma_source_row"])),
            "criteria_evidence": {"rates": rs, "draw_level": db},
            "legacy_verdict": legacy_verdict,
            "dual_caliber_pair_complete": bool(verdict is not None and legacy_verdict is not None),
            "dual_caliber_consistency": ("不一致（new PASS vs legacy UNVERIFIED/判据退化）"
                                         if verdict == "PASS" and legacy_nd <= 1
                                         else ("一致" if verdict != "PASS" and legacy_nd > 1
                                               else "不一致")),
            "diagnostics_not_criteria": {
                "final_target_distance": tgt_dist[name],
                "spearman_rho_T_frac60_vs_rate": spearman(t_frac60, rates),
                "n_same_Tfrac60_pairs": len(gaps),
                "same_Tfrac60_pair_max_relative_rate_gap": (max(gaps) if gaps else None),
                "total_iteration_steps": db["total_steps"],
                "ols_r2_rate_on_T_frac60": ols_r2(rates, t_frac60),
            },
            "per_model": per_model_info[name],
        }

    # ==============================================================
    # §3 O5 保留意见：逐 model 最小目标分量 + ρ + 机制性成分拆分
    # ==============================================================
    o5_minf = [p["f_target_min_component"] for p in o5_info]
    o5_nit = [p["n_iter_mean"] for p in o5_info]
    o5_rates = [p["convergence_rate"] for p in o5_info]
    rho_minf_nit = spearman(o5_minf, o5_nit)
    rho_minf_rate = spearman(o5_minf, o5_rates)
    rho_tfrac_rate = spearman(t_frac60, o5_rates)
    r2_minf = ols_r2(o5_rates, o5_minf)
    r2_tfrac = ols_r2(o5_rates, t_frac60)
    r2_both = ols_r2(o5_rates, o5_minf, t_frac60)
    # 机制性成分：T_frac60 相同但最小分量不同的配对 => 纯机制对比
    mech_pairs = []
    for i in range(len(models)):
        for j in range(i + 1, len(models)):
            if abs(t_frac60[i] - t_frac60[j]) < 1e-12:
                mech_pairs.append({
                    "model_a": models[i], "model_b": models[j],
                    "T_frac60_shared": t_frac60[i],
                    "start_triple_a": o5_info[i]["start_triple_TRA"],
                    "start_triple_b": o5_info[j]["start_triple_TRA"],
                    "f_target_min_component_a": o5_minf[i],
                    "f_target_min_component_b": o5_minf[j],
                    "convergence_rate_a": o5_rates[i],
                    "convergence_rate_b": o5_rates[j],
                    "rate_relative_gap": (abs(o5_rates[i] - o5_rates[j])
                                          / ((o5_rates[i] + o5_rates[j]) / 2.0)),
                    "reading": "T_frac60 完全相同 => 差值不可归因于 T_frac60 / 盆地深度；"
                               "只能来自起始三元组结构与最小目标份额（机制性成分）",
                })
    ontologies[O5]["o5_min_target_component_split"] = {
        "note": "派工单硬要求：O5 保留意见（离散度含机制性成分）须正式跑同报逐 model 最小目标分量 + "
                "ρ(最小分量, n_iter_mean)。以下全为诊断面，0 判据（不进入 K-V3R-26 判定）。",
        "per_model_min_target_component": [
            {"model": p["model"], "start_triple_TRA": p["start_triple_TRA"],
             "f_target_min_component": p["f_target_min_component"],
             "f_target_min_component_class": p["f_target_min_component_class"],
             "f_target_min_component_draw_index": p["f_target_min_component_draw_index"],
             "f_target_triple_at_min_draw": p["f_target_triple_at_min_draw"],
             "f_target_per_component_minima_over_draws":
                 p["f_target_per_component_minima_over_draws"],
             "field_note": p["f_target_field_note"],
             "n_iter_mean": p["n_iter_mean"], "convergence_rate": p["convergence_rate"],
             "n_iter_distinct": p["n_iter_distinct"]}
            for p in o5_info],
        "spearman_rho_min_target_component_vs_n_iter_mean": rho_minf_nit,
        "spearman_rho_min_target_component_vs_convergence_rate": rho_minf_rate,
        "spearman_rho_T_frac60_vs_convergence_rate": rho_tfrac_rate,
        "ols_variance_decomposition_of_rate": {
            "r2_on_min_target_component_alone": r2_minf,
            "r2_on_T_frac60_alone": r2_tfrac,
            "r2_on_both_together": r2_both,
            "residual_share_unexplained": (None if r2_both is None else float(1.0 - r2_both)),
            "reading": "r2_on_both − r2_on_T_frac60 = 最小目标份额在 T_frac60 之外带来的**增量**解释力"
                       " = 机制性成分的可量化下界（2 预测最小二乘，9 点，诊断量非判据）"},
        "matched_pair_mechanism_contrast": mech_pairs,
        "mechanism_component_statement": None,   # 跑后据实测填，见 main 末尾
    }

    # ==============================================================
    # §4 三本体汇总（同向 / 分歧）
    # ==============================================================
    verdicts = {n: ontologies[n]["new_verdict"] for n in ONTOLOGIES}
    distinct_verdict_set = sorted(set(verdicts.values()))
    same_direction = bool(len(distinct_verdict_set) == 1)
    if same_direction:
        agreement = "同向（3/3 本体新构造 verdict 一致 = %s）" % distinct_verdict_set[0]
        if distinct_verdict_set[0] == "PASS":
            summary_branch = ("三本体同向 PASS ⇒ 改判建议按同向给：新构造下 P-J 收敛盆地非退化，"
                              "沿 §2.3 第 2 行（PASS + 沿原 V3 阈值字面不一致）⇒ 维持原 V3 标注"
                              "（UNVERIFIED，不动）+ 显式登记新构造 verdict + 归「不明」分支 + γ")
        elif distinct_verdict_set[0] == "FAIL":
            summary_branch = ("三本体同向 FAIL ⇒ 0 改判动作；原 V3 标注（UNVERIFIED/假证伪）维持，"
                              "V3 原报告 byte 0 触动")
        else:
            # r2：字面空档已终局化为 FAIL（终局表 §3.1 第 2 / 4 行）⇒ 本分支不再由空档触发；
            # 仅当 new_verdict 落到 {PASS, FAIL} 表外时到达，显式登记为异常取值（0 静默归类）。
            summary_branch = ("三本体同向但 verdict 不在 {PASS, FAIL} 表内 ⇒ 显式登记为异常取值，"
                              "0 静默归类；按终局表第 5 行面（读数不可算/非有限/构造跑不完）交 KD 处置")
    else:
        agreement = "分歧（本体间 verdict 不一致：%s）" % " / ".join(
            "%s=%s" % (n, verdicts[n]) for n in ONTOLOGIES)
        summary_branch = ("分歧 ⇒ **维持原标注 + 登记分歧 + γ**；不择优、不聚合掩盖，逐本体并报"
                          "（K-V3R-26 逐本体独立判定）")

    # ==============================================================
    # §5 C4 可复现：进程内二次全量重算自比
    # ==============================================================
    o1b = []
    for idx, m in enumerate(models):
        rec = s60_by_name[m]
        t0, r0, a0 = int(rec["T60"]), int(rec["R60"]), int(rec["A60"])
        o1b.append(np.asarray([redistribute_n_iter(t0, r0, a0,
                                                   int(round(pert[idx][j] * N_CELLS)),
                                                   PRIORITY) for j in range(N_BUDGET)], float))
    o3b, o5b = [], []
    for idx, m in enumerate(models):
        rec = s60_by_name[m]
        t0, r0, a0 = int(rec["T60"]), int(rec["R60"]), int(rec["A60"])
        st = np.full(N_BUDGET, x_start2[idx], float)
        o3b.append(o3_run(st, np.asarray(pert[idx], float))[0].astype(float))
        denom = r0 + a0
        f3 = np.zeros((N_BUDGET, 3), float)
        for j, x0 in enumerate(pert[idx]):
            rest = 1.0 - x0
            if denom == 0:
                f3[j] = (x0, rest, 0.0)
            else:
                rc = rest * r0 / denom
                f3[j] = (x0, rc, rest - rc)
        st3 = np.tile(np.asarray([t0, r0, a0], float) / N_CELLS, (N_BUDGET, 1))
        o5b.append(o5_run(st3, f3)[0].astype(float))
    raw2 = {O1: [[int(v) for v in a] for a in o1b],
            O3: [[int(v) for v in a] for a in o3b],
            O5: [[int(v) for v in a] for a in o5b]}
    raw1 = {n: [[int(v) for v in a] for a in by_model[n]] for n in ONTOLOGIES}
    c4_in_process = {n: bool(canon_sha12(raw1[n]) == canon_sha12(raw2[n])) for n in ONTOLOGIES}
    c4_all = bool(all(c4_in_process.values()))

    # ---------------- 一致性核对：O1 vs 26 落地件 / preexp ----------------
    base_by_model = {p["model"]: p["convergence_rate"] for p in base["per_model"]}
    o1_identical_26 = bool(all(base_by_model.get(p["model"]) == p["convergence_rate"]
                               for p in o1_info))
    pre_by_ont = preexp["per_ontology"]
    consistency = {}
    for name in ONTOLOGIES:
        pe = {p["model"]: p["convergence_rate"] for p in pre_by_ont[name]["per_model"]}
        consistency[name] = {
            "vs_preexp_per_model_rate_identical":
                bool(all(pe.get(p["model"]) == p["convergence_rate"] for p in per_model_info[name])),
            "vs_preexp_rates_n_distinct": pre_by_ont[name]["criteria_evidence"]["rates"]["n_distinct"],
            "vs_preexp_verdict": "n/a（preexp 探索性档，verdict = null）",
        }
    consistency[O1]["vs_26_landed_result_identical"] = o1_identical_26
    consistency[O1]["note"] = ("派工单硬要求：O1 应与 26 落地件逐字同 —— 沿同一 rng 流 + 同一构造字面 "
                              "复算，9/9 convergence_rate 逐字相同")

    # ==============================================================
    # §6 落盘
    # ==============================================================
    ontologies[O5]["o5_min_target_component_split"]["mechanism_component_statement"] = (
        "实测拆解：ρ(最小目标分量, n_iter_mean) = %.4f，ρ(最小目标分量, convergence_rate) = %.4f，"
        "ρ(T_frac60, convergence_rate) = %.4f。方差分解（OLS，9 点，诊断量非判据）："
        "rate ~ 最小分量 R² = %.4f；rate ~ T_frac60 R² = %.4f；两者同入 R² = %.4f"
        "（未解释残余份额 %.4f）。⇒ **T_frac60 之外的增量解释力 = %.4f** 即「最小份额瓶颈」"
        "这一机制性成分的可量化下界；T_frac60 相同的配对（%s）给出纯机制对比：同 T_frac60 下 rate 仍差 "
        "%.1f%%，该差值**不可**归因于盆地深度。结论：O5 跨 model 离散度**同时**含 "
        "「T_frac60 / 盆地深度」与「最小目标份额机制」两类成分，且残余份额 %.1f%% 无法由两者解释 —— "
        "O5 的离散度不可全部归因于任一类（preexp §6 保留意见在正式跑中**维持**）。"
        % (rho_minf_nit, rho_minf_rate, rho_tfrac_rate, r2_minf, r2_tfrac, r2_both,
           1.0 - r2_both, r2_both - r2_tfrac,
           "; ".join("%s vs %s" % (p["model_a"], p["model_b"]) for p in mech_pairs),
           max(p["rate_relative_gap"] for p in mech_pairs) * 100.0,
           (1.0 - r2_both) * 100.0))

    payload_core = {
        "schema": "v3_recheck_formal_data/26b_p_j_three_ontology/1",
        "nature": "正式判定档：逐本体出 K-V3R-26 正式 verdict（区别于 26 preexp = 探索性档 verdict=null）",
        "date": "2026-09-27",
        "date_r2": "2026-09-28",
        "revision": ("r2 · 字面空档归属终局化（PI 2026-09-28 22:40 ask_c6721836fb0a2e1af6c12f37 q1 授权改实现；"
                     "依据归属终局表 c353fbcdc753 §3.1；0 新设阈值）"),
        "revision_of": {
            "path": "results/_v3_recheck_26b_executor_2026_09_27.py",
            "sha12": "5c906113a210",
            "byte_0_touched": True,
            "changed_surface": ("仅 judge_K_V3R_26 的字面空档分支（UNDECIDED_BY_LITERAL_GAP → FAIL + γ）"
                                "+ 随之失效的登记表述（summary/tiers 的「不明（字面空档）」分支）与"
                                "kill_line 元数据；判死线字面、构造常数、本体实现、种子/预算/抖动全未触动"),
        },
        "produced_by_r2": "Mavis 团队 worker（session mvs_6ba609043dce4685988f510045254e8e；"
                          "PI 2026-09-28 22:40 ask_c6721836fb0a2e1af6c12f37 q1 授权改实现；"
                          "如实署名，不冒充 protocol-keeper / verdict-keeper / PI）",
        "produced_by": "Mavis 团队 worker（Mavis root session 派工；PI 2026-09-27 问卷 "
                       "ask_75126c38abf2c134a1591672 Q1 拍板「三本体全跑」）",
        "dispatch_inputs": [
            {"path": "results/_v3_recheck_prereg_v1_2026_09_27.md",
             "sha12_measured": sha12(PREREG.read_bytes()),
             "role": "K-V3R-26 / TH-V3R-26 / §2.3 四档 改判规则表 字面锚（0 擅调）"},
            {"path": "results/_v3_recheck_26_preexp_data_2026_09_27.json",
             "sha12_measured": sha12(PREEXP_DATA.read_bytes()),
             "role": "预实验数据件（只读；扰动表 SHA-12 + 逐本体率 一致性核对面）"},
            {"path": "results/_v3_recheck_26_preexp_report_2026_09_27.md",
             "sha12_measured": sha12(PREEXP_REPORT.read_bytes()),
             "role": "预实验报告（只读；§6 择优段 = 本件三本体选择依据）"},
            {"path": "results/_v3_recheck_26_preexp_executor_2026_09_27.py",
             "sha12_measured": sha12(PREEXP_EXEC.read_bytes()),
             "role": "fallback 纪律锚 = 本件 O1/O3/O5 构造字面来源（逐字沿用）"},
            {"path": "results/_v3_recheck_26_executor_2026_09_27.py",
             "sha12_measured": sha12(EXEC_BASE.read_bytes()),
             "role": "第一梯队 executor（只读；O1 基线连续性锚）"},
            {"path": "results/_v3_recheck_26_result_2026_09_27.json",
             "sha12_measured": sha12(BASE_RESULT.read_bytes()),
             "role": "第一梯队落地件（只读；O1 逐字复现对照面）"},
            {"path": "results/_v3_recheck_26_rescript_2026_09_27.md",
             "sha12_measured": sha12(BASE_RESCRIPT.read_bytes()),
             "role": "第一梯队改判件（只读；原 V3 标注 + 档位字面来源）"},
            {"path": "results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json",
             "sha12_measured": sha12(SRC_PJ.read_bytes()),
             "role": "9 model T_frac60 真分布 + legacy 面 9/9 ≡ 0.1 原读数"},
            {"path": "results/deposon_v3_physical_opt_60cells_2026_09_11.json",
             "sha12_measured": sha12(SRC_60.read_bytes()),
             "role": "9 model 真实起始三元组 (T60,R60,A60)"},
        ],
        "kill_line": {
            "id": "K-V3R-26",
            "literal": KILL_LINE_LITERAL,
            "th_literal": TH_LITERAL,
            "th_form_frozen": "convergence_rate_m = mean_j(n_iter_j) / n_budget, j=1..100",
            "per_ontology_independent": True,
            "literal_gap_2_to_3": ("K-V3R-26 字面只定义 n_distinct ≥ 4（PASS）与 n_distinct ≤ 1（FAIL）；"
                                   "2 ≤ n_distinct ≤ 3 为字面空档。**r2 修订**：本件 0 再输出 "
                                   "UNDECIDED_BY_LITERAL_GAP（该字面 = 「不明」形态，已被 PI 2026-09-28 20:02 "
                                   "封死）；改按归属终局表 §3.1 落 FAIL + 强制 γ 根因 —— 分支 A"
                                   "（2 ≤ n ≤ 3）γ=弱分布/退化警报域；分支 B（n ≥ 4 ∧ std=0）γ=方差恒同⇒判据退化。"),
            "literal_gap_attribution_source": {
                "terminal_table_path": "results/_v5_item26b_attribution_effective_2026_09_28.md",
                "terminal_table_sha12": "c353fbcdc753",
                "terminal_table_section": "§3.1 归属终局表（终局版 · 冻结）",
                "pi_decision_pin": "PI 2026-09-28 22:15 拍板（① 端点归属 = C3 ② R-∧ 采纳）",
                "worker_authorization": ("PI 2026-09-28 22:40 授权改实现（ask_c6721836fb0a2e1af6c12f37 q1）"
                                         "—— 源件 5c906113a210 byte 0 触动，改以新名件落"),
                "source_executor_untouched_sha12": "5c906113a210",
                "no_new_numeric_threshold": True,
                "no_new_fourth_state": True,
            },
            "no_private_clause_added": True,
        },
        "construct": {
            "n_budget": N_BUDGET,
            "jitter": "+-0.05 uniform on T_frac60 (clip [0,1])",
            "seed": SEED,
            "priority": PRIORITY,
            "tolerance": "TOL = 1e-6（O3/O5 统一；O1 为整数精确命中）",
            "paired_sampling": ("3 本体共用同一批扰动抽样（rng 流与第一梯队 / preexp 逐字同）"
                                "=> 配对比较成立"),
            "perturbation_table_sha12": pert_sha12,
            "perturbation_stream_matches_preexp": pert_matches_preexp,
            "models": models,
            "t_frac60_real": t_frac60,
            "literal_source": "O1/O3/O5 构造与实现常数逐字沿 "
                              "results/_v3_recheck_26_preexp_executor_2026_09_27.py（775217a462f5）",
        },
        "pre_run_degenerate_gate": pre_run_gate,
        "legacy_face": {
            "source": "results/_p_j_convergence_basin_2026_09_16/p_j_convergence_basin_results_2026_09_16.json",
            "convergence_rates": legacy,
            "n_distinct": legacy_nd,
            "std": legacy_std,
            "verdict": legacy_verdict,
            "ontology_independent": True,
            "note": "沿原 V3 阈值字面（K-V3R-0-C 双口径第二口径）；本体无关，3 本体共享同一读数",
        },
        "per_ontology": ontologies,
        "three_ontology_summary": {
            "verdicts": verdicts,
            "same_direction": same_direction,
            "agreement_statement": agreement,
            "summary_branch": summary_branch,
            "rule_literal": "派工单：三本体同向 ⇒ 改判建议按同向给；分歧 ⇒ 维持原标注＋登记分歧＋γ"
                            "（不择优不聚合掩盖，逐本体并报）",
            "revise_tier_4_docket": [
                "档1：PASS + 一致 ⇒ 原 V3 报告不动；立改判件入勘误链 E-41.x 系",
                "档2：PASS + 不一致 ⇒ 维持原 V3 标注（不动）+ 显式登记新构造 verdict；归「不明」分支",
                "档3：FAIL（即原标注维持）⇒ 0 改判动作；原报告 byte 0 触动",
                "档4：不明（构造不可行 / 素材不足）⇒ 维持原标注 + 显式登记 γ；归「V4 收尾整理」桶",
            ],
            "hit_tier": None,   # 跑后据实测填
        },
        "consistency_with_preexp_and_26": consistency,
        "reproducibility_in_process": {
            "c4_in_process_full_recompute_identical": c4_all,
            "per_ontology": c4_in_process,
            "note": "进程内全量二次重算逐字自比；进程外双跑比对（两次落盘件 SHA-12 逐字相同）"
                    "由 worker 核验并登记于报告",
        },
        "runtime": ("0 LLM; numpy + hashlib + json only; no network; read-only inputs; 0 改动既有件"
                    "（r2：源件 5c906113a210 与 26b 原派生件均 byte 0 触动，r2 落新名派生件）"),
        "iron_rules": {
            "kill_line_K_V3R_26_literal_untouched": True,   # r2：K-V3R-26 判死线**字面**逐字 0 改动
            "source_executor_byte_0_touched": True,        # 源件 5c906113a210 byte 0 触动
            "literal_gap_attribution_applied": True,        # r2：空档两枝按终局表 §3.1 落 FAIL + 强制 γ
            "no_private_clause_no_threshold_tuning": True,
            "0_new_numeric_threshold": True,
            "0_LLM": True, "no_proxy": True, "no_key_in_prompt_json_disk": True,
            "read_only_inputs": True, "derived_json_not_merged": True,
            "existing_26_and_preexp_series_untouched": True,
            "formal_verdict_this_piece": True,
        },
        "verdict": {n: ontologies[n]["new_verdict"] for n in ONTOLOGIES},
        "verdict_note": "正式判定档：本件出 K-V3R-26 逐本体正式 verdict（3 本体独立判定）+ 双口径并报。",
    }

    # 命中的改判档位（沿 prereg §2.3 四档，逐本体 + 汇总）
    tiers = []
    for n in ONTOLOGIES:
        if ontologies[n]["new_verdict"] == "PASS":
            tiers.append("档2：PASS + 不一致" if legacy_nd <= 1 else "档1：PASS + 一致")
        elif ontologies[n]["new_verdict"] == "FAIL":
            tiers.append("档3：FAIL（原标注维持）")
        else:
            # r2：字面空档已终局化为 FAIL ⇒ 不再由本分支进入（0 新增「不明」形态）
            tiers.append("档4：KD（读数不可算/非有限/构造跑不完；终局表第 5 行）")
    payload_core["three_ontology_summary"]["hit_tier"] = tiers
    payload_core["three_ontology_summary"]["hit_tier_all_same"] = bool(len(set(tiers)) == 1)

    payload_sha12 = canon_sha12(payload_core)
    payload = dict(payload_core)
    payload["reproducibility"] = {
        "payload_sha12": payload_sha12,
        "note": "payload_sha12 = hashlib.sha256(canonical json of payload_core).hexdigest()[:12]",
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print("[26b-r2] written:", OUT.relative_to(REPO))
    print("[26b-r2] pre-run degenerate gate alarm_hit:", pre_run_gate["degenerate_alarm_hit"])
    print("[26b-r2] perturbation_table_sha12 =", pert_sha12, "matches_preexp:", pert_matches_preexp)
    print("[26b-r2] legacy face: n_distinct=%d std=%.6g verdict=%s" % (legacy_nd, legacy_std, legacy_verdict))
    for name in ONTOLOGIES:
        o = ontologies[name]
        r = o["criteria_evidence"]["rates"]
        print("[26b-r2] %-34s n_dist=%d std=%.6g rel_std=%.4g -> %s  kill_line_fail_hit=%s  gamma=%s"
              % (name, r["n_distinct"], r["std"], r["rel_std"] or 0.0,
                 o["new_verdict"], o["kill_line_fail_hit"], o["gamma_root_cause"]))
    print("[26b-r2] same_direction:", same_direction, "|", agreement)
    print("[26b-r2] hit_tier:", tiers)
    print("[26b-r2] O1 identical to landed 26 result:", o1_identical_26)
    print("[26b-r2] consistency vs preexp:",
          {n: consistency[n]["vs_preexp_per_model_rate_identical"] for n in ONTOLOGIES})
    print("[26b-r2] C4 in-process full recompute identical:", c4_all, c4_in_process)
    print("[26b-r2] O5 rho(min_component, n_iter_mean) =", rho_minf_nit)
    return 0


if __name__ == "__main__":
    sys.exit(main())
