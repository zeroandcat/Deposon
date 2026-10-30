# -*- coding: utf-8 -*-
"""
distortion_calculator.py
========================
P-B V0 失真界计算器（G-E01 · 缺口 `G3` 之重建件）—— deposon ①段

来源件 (先核后用, 逐件登记; SHA-12 = hashlib.sha256 全文字节前 12 位, bytes 为全文字节数):
- docs/V3X/P_B_DISTORTION_BOUND_V0_SPEC.md
    正典 spec (活件)。**本棒 2026-10-14 逐字节测**: `423c84de20d5` / 15,457 B / CR=0 / TAB=0 / BOM=False
    本件引用之逐字节位:
      L10  锚定对象固定为 5 个冻结工件 … deposon 仓库 `tools/distortion_calculator.py`(D1 由 data 实现)
      L12  基线是 Bayesian 玩家(已知机制 + 支付 -> 失真 = 0)
      L30  锚行 `P_B_DISTORTION_CALC` | `tools/distortion_calculator.py` | SHA-256 全文 -> 前 12 位 | `version=2026-09-11`
      L32  任何 >= 1 锚漂移 -> 全 V0 撤回。
      L61  D(M, T) = E_pi[ Sum_t |u*(a_t) - u(a_t)| / max_u ]
      L66  max_u: 支付上界(任务族归一化常数)
      L68  失真倍数 = D_LLM(M, T) / max(D_Bayesian(M, T), eps)
      L88  distortion_multiplier(M, T) = D_LLM(M, T) / max(D_Bayesian(M, T), eps)
      L91  跨 (M, T) 算 mean + 95% bootstrap CI(10k resamples)。
      L103-L110  `kill_decision` 三分支 (本件**逐字转引, 0 改写**, 见 L3 核区)
      L116  A3 种子复现: seed=42, 123, 456 三套, 看 std/mean > 0.2 则报"种子敏感"
- results/_ge01_prereg_seven_requirements_draft_2026_10_13.md
    §6 四条正典口径。**本棒 2026-10-14 逐字节测**: `0a031a9795a9` / 39,337 B / CR=0
      §6 L170 ① 失真定义 D=E[Sum_t 1{A_t 不在 K_t}] = 期望被拒决策计数; 基数损失量级不入 D;
                 u_t(a;K_t)=1(a 在 K_t)/0(否则), 支付域 {0,1}
      §6 L171 ② 归一化常数 c = max_u = 1 (任务族归一化常数 = 每决策支付上界;
                 非任务名数值选择 / 非模型性能测量); 五族全 = 1
      §6 L172 ③ 守卫比值代数 (G_L/c)/max(G_B/c, eps) = G_L/max(G_B, c*eps);
                 无守卫支路(G_B >= c*eps)消去成立; 守卫支路(G_B=0 => G_L/(c*eps))保 c;
                 例 G_L=2, G_B=0, eps=0.1 => c=1 时 20 / c=2 时 10
      §6 L173 ④ eps 之冻结: eps 于 prereg 固定(须 PI 另给); 单一标量常数, 不随格变/不随 t 变
      §6 L177 0 以他方自报值为验收依据 —— 计算器自检须以本方精确枚举为准
      §6 L178 测试侧笔误须如实登记 —— 报出口径须容「测试侧修正留痕」栏位
- results/_ge01_calculator_rebuild_design_2026_10_14.md
    本件之实现规格来源(逐字回读, 本棒实测): `8ab699f017c8` / 46,007 B
    §3-1 五层结构 / §3-2 13 个函数签名 / §3-3 双轨算术 / §3-4 边界守卫 B1-B12 /
    §4-2 与 5 锚之同批流程 S1-S9 / §6 自测设计 T1-T9
- results/_r5_spec_pack_retrieved_2026_10_13/鲍勃_minimax实验委托规格包_2026_10_12.md
    `bb66c577673b` / 14,758 B (本棒逐字节测)。§1.3 表末行逐字:
    「D1 理论输入 u*(a_t)+L/U | **缺失(外部交付线)**——到位后由我方按 G-E02 落盘 calculator+5 锚 JSON 预登记」
    §5 之 1 逐字: 指纹一律 hashlib.sha256, 禁内建散列调用。

本件结构 (设计件 §3-1 之单文件五层, L0-L5):
    L0 文件头   本 docstring + 版本字段 + 锚 ID/路径字段
    L1 常量区   支付域 / 归一化常数 / bootstrap 参数 / 网格参数
    L2 守卫层   assert_eps / assert_weights_sum_one / assert_same_length  (+ 私有 _as_fraction)
    L3 精确核   distortion_indicator / distortion_gapwise / guarded_denominator /
                guarded_denominator_rescaled / distortion_multiplier / aggregate_cells /
                bootstrap_ci / kill_decision        —— **核内 0 float 运算**
    L4 产表轨   distortion_multiplier_float / cell_table_row (薄封装, 转换只在出口)
    L5 自测     self_test (T1-T9, 0 calls)

铁律 (设计件 §3-1 末 / §3-4 之 B11-B12):
    1. 0 网络调用 / 0 LLM 调用 / 0 读 key / 0 读 .env / 0 远端写。
    2. 0 写盘 —— 唯一输出面为 `--self-test` 之 stdout。
    3. 0 内建散列函数调用 —— 指纹面一律 hashlib.sha256 (探针见 _FORBIDDEN_CALL, 见 T8)。
    4. bootstrap 随机源固定 seed (BOOTSTRAP_SEED = 42), 0 无种子随机。
    5. kill_decision 函数体逐字转引 spec L103-L110, 0 改写。
    6. 归一化常数 c 保留于函数签名 (五族全 1, 但供正典代数自测 c=2 之 10 值),
       **0 作为网格轴**, 0 硬编码 H, 0 以过渡区间充锁定值。
    7. 0 以轨迹内决策数再加权 (否则 D 之量纲随 H 漂移)。

自测用法: `python tools/distortion_calculator.py --self-test`

作者: worker | 2026-10-14 (G-E01 `G3` 重建执行棒)
"""

from __future__ import annotations

import hashlib
import io
import math
import os
import random
import struct
import sys
from fractions import Fraction

# === L0 文件头 · 版本与锚字段 (spec L30 锚行字段之字面) ===

#: 锚 ID (spec L30 逐字)
ANCHOR_ID = "P_B_DISTORTION_CALC"
#: 锚路径 (spec L30 逐字)
ANCHOR_PATH = "tools/distortion_calculator.py"
#: 锚之「字段」栏所值 (spec L30 逐字 `version=2026-09-11`)
VERSION = "2026-09-11"
#: 同上, 别名 (设计件 §3-1 L0 要求字段名)
SUPPORTED_VERSION = "2026-09-11"

# ⚠ KD-7 (设计件 §3-5): 重建件沿用 `version=2026-09-11` 字面, 与「新写件 vs 该版本语义」
#   存在张力; 改之即改锚口径 (⛔ 0 自决) => 本件沿锚字段 0 改, 登记为 KD 待 PI 确认。

# === L1 常量区 ===

#: 支付域 {0,1} (0a031a9795a9 §6 ① L170 逐字: u_t(a;K_t)=1 / 0, 支付域 {0,1})
PAY_DOMAIN = (0, 1)

#: 归一化常数 c = max_u = 1 (0a031a9795a9 §6 ② L171 逐字; 五族全 = 1)
DEFAULT_C = Fraction(1)

#: bootstrap 重采样数 (spec L91 逐字 10k resamples; ⛔ 0 新设)
BOOTSTRAP_RESAMPLES = 10000
#: bootstrap 种子 (spec L116 之三套之首; ⛔ 0 新设)
BOOTSTRAP_SEED = 42
#: 种子敏感性三套 (spec L116 逐字 42, 123, 456; 本件提供取值, 报出口径在分析层)
BOOTSTRAP_SEEDS = (42, 123, 456)
#: 95% CI 之两端分位 (精确有理数: 1/40 与 39/40)
CI_LOWER_LEVEL = Fraction(1, 40)
CI_UPPER_LEVEL = Fraction(39, 40)
#: CI 之报出口径 (百分位 bootstrap + 最近秩法; ⛔ 0 以他法替换而不报)
CI_METHOD = "percentile-bootstrap-nearest-rank"

# === T3 代数恒等式网格 (设计件 §6 T3 之 `D2_identity_grid_10k` 面) ===
#: G_L 取值 25 档 (1..25)
GRID_G_L = tuple(Fraction(i) for i in range(1, 26))
#: G_B 取值 50 档 (k/4, k=0..49)
GRID_G_B = tuple(Fraction(k, 4) for k in range(50))
#: c 取值 2 档 (1, 2) —— B8: c 不作网格轴, 仅供正典代数自测之 c=2 之 10 值
GRID_C = (Fraction(1), Fraction(2))
#: eps 取值 4 档 (1/10, 1/4, 1/2, 1)
GRID_EPS = (Fraction(1, 10), Fraction(1, 4), Fraction(1, 2), Fraction(1))
#: 网格点数 (25 * 50 * 2 * 4 = 10_000, 与设计件 §6 T3 之项名 `D2_identity_grid_10k` 对齐)
GRID_SIZE = 10000

# === T5 枚举面 (设计件 §6 T5 之 A/C 对象) ===
#: A 对象: 15 键非空 —— 4 元动作集之非空子集恰 15 个
T5_ACTION_ALPHABET = (1, 2, 3, 4)
T5_EXPECTED_KEYSET_COUNT = 15
#: C 对象: 3H/4 之 H 扫描域 (H = 1..100)
T5_H_SCAN = range(1, 101)

# === T9 判死面边界点 (设计件 §6 T9) —— 以精确有理数给出 1.5 / 1.8 / 2.0 / 0.1 / 0.3 ===
T9_BOUNDARY_POINTS = (
    ("mean=1.5", Fraction(3, 2)),
    ("mean=1.8", Fraction(9, 5)),
    ("mean=2.0", Fraction(2)),
    ("ci_hi=1.8", Fraction(9, 5)),
    ("ci_hi=2.0", Fraction(2)),
    ("hit=0.1", Fraction(1, 10)),
    ("hit=0.3", Fraction(3, 10)),
)

#: B11 之探针 —— 由拼接构造, ⛔ 使源码内不出现内建散列调用的字面形态
_FORBIDDEN_CALL = "hash" + "("


# ---------------------------------------------------------------------------
# L2 守卫层
#   0 静默通过: 守卫失败即 raise, 不产出读数 (设计件 §3-2 头注)
#   类型不合 -> TypeError; 值不合 -> ValueError
# ---------------------------------------------------------------------------

def _as_fraction(value, name="value"):
    """精确化: int / Fraction / float 三型入 `Fraction`, 其余 raise TypeError。

    float 入参取其**精确二进制值** (Fraction(float) 之定义), ⛔ 0 静默替值;
    故 float 字面 `0.1` 精确化后为 3602879701896397/36028797018963968,
    **不等于** Fraction(1, 10) —— 须正典例向量一律以 Fraction 给 (见 T1 之留痕)。
    """
    if isinstance(value, Fraction):
        return value
    if isinstance(value, bool):
        raise TypeError(name + ": bool 非合法数值入参")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(name + ": 非有限 float 入参")
        return Fraction(value)
    raise TypeError(name + ": 仅接受 int / float / Fraction, 实得 " + type(value).__name__)


def assert_eps(eps) -> "Fraction":
    """B1: eps > 0 且有限; int/Float/Fraction 均精确化。非法者 raise, ⛔ 0 静默替值。

    依据: 0a031a9795a9 §6 ③ L172 (max 之语义) + §6 ④ L173 (eps 单一标量常数,
    须 PI 于 prereg 固定 —— 本件⛔ 0 给值, 仅提供入参口)。
    """
    value = _as_fraction(eps, "eps")
    if value <= 0:
        raise ValueError("eps 须 > 0, 实得 " + str(value))
    return value


def assert_weights_sum_one(weights) -> None:
    """B6: sum(w_tau) == 1 —— **Fraction 轨精确判定**, ⛔ 0 以 float 容差判定。

    依据: 0a031a9795a9 §3-3 依据栏 L87 逐字 (weights must be given and sum to 1;
    D is their weighted mean of the trajectory error counts)。
    """
    values = tuple(_as_fraction(w, "weights[%d]" % i) for i, w in enumerate(weights))
    if not values:
        raise ValueError("weights 为空: D 之加权平均无定义")
    total = Fraction(0)
    for w in values:
        total += w
    if total != Fraction(1):
        raise ValueError("权重和须精确 = 1, 实得 " + str(total))
    return None


def assert_same_length(seqs: tuple) -> int:
    """B7: 传入之序列组逐个等长, 返回该共同长度; 不等即 raise。

    依据: 0a031a9795a9 §6 ① L170 (A_t 与 K_t 按 t 逐位配对)。
    """
    if not seqs:
        raise ValueError("seqs 为空: 无长度可断言")
    lengths = tuple(len(s) for s in seqs)
    first = lengths[0]
    for idx, n in enumerate(lengths):
        if n != first:
            raise ValueError("序列长度不一致: 第 %d 项长 %d, 首项长 %d" % (idx, n, first))
    return first


def _resolve_weights(n_items, weights):
    """未给权重时取逐轨迹均匀权 (Fraction(1, n)); ⛔ 0 以轨迹内决策数再加权。"""
    if weights is None:
        return tuple(Fraction(1, n_items) for _ in range(n_items))
    values = tuple(_as_fraction(w, "weights[%d]" % i) for i, w in enumerate(weights))
    if len(values) != n_items:
        raise ValueError("权重个数 %d 与轨迹数 %d 不符" % (len(values), n_items))
    assert_weights_sum_one(values)
    return values


def _check_max_u(max_u) -> "Fraction":
    """B9: max_u = 每决策支付上界; 须 > 0。⛔ 非任务名数值选择 ⛔ 非模型性能测量。"""
    value = _as_fraction(max_u, "max_u")
    if value <= 0:
        raise ValueError("max_u 须 > 0, 实得 " + str(value))
    return value


# ---------------------------------------------------------------------------
# L3 精确核 (Fraction) —— 核内 0 float 运算
# ---------------------------------------------------------------------------

def distortion_indicator(choices, key_sets, weights=None) -> "Fraction":
    """正典口径 ① (0a031a9795a9 §6 L170):

        D = E[ Sum_t 1{A_t 不在 K_t} ]  = 期望被拒决策计数

    choices: 逐轨迹之实际选择序列 A_tau (外层逐 tau, 内层逐 t)
    key_sets: 逐轨迹之接受键序列 K_tau (每项为一个键容器, 按**集合**语义判 A_t 是否在其中)
    weights:  逐轨迹权重, 须精确和 = 1; 未给则逐轨迹均匀
    返回: Fraction 之 D。D 之量纲 = 计数 (可取值区间 [0, H]) —— B10: 基数损失量级不入 D,
          故本函数 **0 除以 H / 0 取对数 / 0 引入任何基数因子**。
    """
    traj_a = tuple(tuple(a) for a in choices)
    traj_k = tuple(tuple(k for k in tau) for tau in key_sets)
    n = len(traj_a)
    if n == 0:
        raise ValueError("轨迹集为空: D 无定义")
    if len(traj_k) != n:
        raise ValueError("A 与 K 之轨迹数不符: %d vs %d" % (n, len(traj_k)))
    w = _resolve_weights(n, weights)
    total = Fraction(0)
    for tau in range(n):
        h = assert_same_length((traj_a[tau], traj_k[tau]))
        err = 0
        for t in range(h):
            if traj_a[tau][t] not in traj_k[tau][t]:
                err += 1
        total += w[tau] * Fraction(err)
    return total


def distortion_gapwise(choices, optimal_payoffs, actual_payoffs,
                       max_u=DEFAULT_C, weights=None) -> "Fraction":
    """spec L61 逐字之差值式 (与口径 ① 并存, ⛔ 0 调和 —— KD-1/D 两口径未择定):

        D(M, T) = E_pi[ Sum_t |u*(a_t) - u(a_t)| / max_u ]

    choices/optimal_payoffs/actual_payoffs: 逐轨迹三条等长序列 (B7);
      choices 仅提供对齐之骨架 (决策位), 支付值逐位取自后二者。
    max_u: 支付上界, 任务族归一化常数 (spec L66) —— B9。
    weights: 同 distortion_indicator。
    ⚠ 在冻结之 c=1 与二元支付域 {0,1} 下本式与口径 ① 逐项均为 {0,1} (量纲同构之推断,
      候 PI 核准); 两族并存之择定权属 PI。
    """
    traj_c = tuple(tuple(x) for x in choices)
    traj_o = tuple(tuple(x) for x in optimal_payoffs)
    traj_a = tuple(tuple(x) for x in actual_payoffs)
    n = len(traj_c)
    if n == 0:
        raise ValueError("轨迹集为空: D 无定义")
    if len(traj_o) != n or len(traj_a) != n:
        raise ValueError("三条序列之轨迹数不符: %d / %d / %d" % (n, len(traj_o), len(traj_a)))
    cap = _check_max_u(max_u)
    w = _resolve_weights(n, weights)
    total = Fraction(0)
    for tau in range(n):
        h = assert_same_length((traj_c[tau], traj_o[tau], traj_a[tau]))
        acc = Fraction(0)
        for t in range(h):
            u_star = _as_fraction(traj_o[tau][t], "u*")
            u_act = _as_fraction(traj_a[tau][t], "u")
            acc += abs(u_star - u_act) / cap
        total += w[tau] * acc
    return total


def guarded_denominator(d_bayesian, eps, c=DEFAULT_C) -> "Fraction":
    """守卫分母: max(G_B, c * eps) —— 正典口径 ③ 之落法 (0a031a9795a9 §6 L172)。

    B1: 因 eps > 0 且 c > 0, 分母 >= c*eps > 0, 0 除零。
    B2: G_B == 0 之守卫支路 => 分母 = c*eps, **c 不得消去**。
    B3: G_B >= c*eps 之无守卫支路 => 分母 = G_B, **c 精确消去**。
    """
    g_b = _as_fraction(d_bayesian, "d_bayesian")
    e = assert_eps(eps)
    cc = _as_fraction(c, "c")
    if cc <= 0:
        raise ValueError("c 须 > 0, 实得 " + str(cc))
    if g_b < 0:
        raise ValueError("D_Bayesian 须 >= 0, 实得 " + str(g_b))
    if g_b >= cc * e:
        return g_b
    return cc * e


def guarded_denominator_rescaled(g_bayesian, eps, c=DEFAULT_C) -> "Fraction":
    """重标形式之守卫分母: max(G_B / c, eps)。

    与 guarded_denominator 恒等: max(G_B/c, eps) = (1/c) * max(G_B, c*eps)。
    供 T3 恒等式网格之两侧分别取值。
    """
    g_b = _as_fraction(g_bayesian, "g_bayesian")
    e = assert_eps(eps)
    cc = _as_fraction(c, "c")
    if cc <= 0:
        raise ValueError("c 须 > 0, 实得 " + str(cc))
    if g_b < 0:
        raise ValueError("G_B 须 >= 0, 实得 " + str(g_b))
    rescaled = g_b / cc
    if rescaled >= e:
        return rescaled
    return e


def distortion_multiplier(d_llm, d_bayesian, eps, c=DEFAULT_C) -> "Fraction":
    """失真倍数 —— spec L68 / L88 逐字:

        失真倍数 = D_LLM(M, T) / max(D_Bayesian(M, T), eps)

    c == 1 时退化为 spec 之原式; 一般 c 时为 G_L / max(G_B, c*eps) (口径 ③ 之落法)。
    ⚠ spec L12: Bayesian 基线失真按定义为 0 => D_Bayesian ≡ 0 => 分母恒为 c*eps,
      故 **eps 之值直接决定头条读数** —— 本件 ⛔ 0 给 eps 之值 (须 PI 于 prereg 固定)。
    """
    g_l = _as_fraction(d_llm, "d_llm")
    if g_l < 0:
        raise ValueError("D_LLM 须 >= 0, 实得 " + str(g_l))
    denom = guarded_denominator(d_bayesian, eps, c)
    return g_l / denom


def aggregate_cells(cell_readings, weights=None) -> "Fraction":
    """跨 cell 之加权聚合 (spec L91: 跨 (M, T) 算 mean)。

    cell_readings: 逐 cell 之 D 读数序列; weights: 逐 cell 权重 (须精确和 = 1),
    未给则逐 cell 均匀。⛔ 0 以 cell 内决策数再加权。
    """
    values = tuple(_as_fraction(v, "cell_readings[%d]" % i) for i, v in enumerate(cell_readings))
    n = len(values)
    if n == 0:
        raise ValueError("cell 读数序列为空: 聚合无定义")
    w = _resolve_weights(n, weights)
    total = Fraction(0)
    for i in range(n):
        total += w[i] * values[i]
    return total


def bootstrap_ci(values, resamples=BOOTSTRAP_RESAMPLES, seed=BOOTSTRAP_SEED):
    """95% 百分位 bootstrap CI (spec L91 逐字: 10k resamples)。

    随机源固定 seed (默认 BOOTSTRAP_SEED = 42, ⛔ 0 无种子随机);
    分位取**最近秩法** (nearest-rank), 两端 1/40 与 39/40 (精确有理数)。
    返回 dict: n / mean / ci_lo / ci_hi / resamples / seed / method / levels —— **全为 Fraction**。
    ⚠ 种子敏感性报出口径 (spec L116: seed 42/123/456, std/mean > 0.2 则报「种子敏感」)
      属**分析层**, 不在本件内作判定; 本件仅以 seed 字段供上层三套对跑 (BOOTSTRAP_SEEDS)。
    """
    vals = tuple(_as_fraction(v, "values[%d]" % i) for i, v in enumerate(values))
    n = len(vals)
    if n == 0:
        raise ValueError("样本为空: bootstrap 无定义")
    if resamples < 1:
        raise ValueError("resamples 须 >= 1, 实得 %d" % resamples)
    total = Fraction(0)
    for v in vals:
        total += v
    mean = total / Fraction(n)
    rng = random.Random(seed)
    means = []
    for _ in range(resamples):
        acc = Fraction(0)
        for _ in range(n):
            acc += vals[rng.randrange(n)]
        means.append(acc / Fraction(n))
    means.sort()
    lo_idx = int(math.floor(CI_LOWER_LEVEL * resamples))
    hi_idx = int(math.ceil(CI_UPPER_LEVEL * resamples)) - 1
    lo_idx = max(0, min(resamples - 1, lo_idx))
    hi_idx = max(0, min(resamples - 1, hi_idx))
    return {
        "n": n,
        "mean": mean,
        "ci_lo": means[lo_idx],
        "ci_hi": means[hi_idx],
        "resamples": resamples,
        "seed": seed,
        "method": CI_METHOD,
        "levels": (CI_LOWER_LEVEL, CI_UPPER_LEVEL),
    }


def kill_decision(mean_mult, ci_lo, ci_hi, theory_U_hit_rate) -> str:
    """判死裁定 —— **spec `423c84de20d5` L103-L110 逐字转引, ⛔ 0 改写**:

    ```python
    def kill_decision(mean_mult, ci_lo, ci_hi, theory_U_hit_rate):
        if mean_mult >= 2.0 or theory_U_hit_rate >= 0.3:
            return "FAIL_H0"  # 机制不可行 或 30%+ cell 超理论界
        elif mean_mult <= 1.5 and ci_hi <= 1.8 and theory_U_hit_rate <= 0.1:
            return "PASS_H1"  # 机制可商用
        else:
            return "GRAY"  # 1.5 < mean < 2.0 或 CI 跨边界
    ```

    比较面与字面 0 改 (⛔ 0 新设数值切点); 入参可为 float 或 Fraction ——
    Fraction 与 float 之比较在 Python 中按精确值进行, 故 T9 之边界点测试不失真。
    """
    if mean_mult >= 2.0 or theory_U_hit_rate >= 0.3:
        return "FAIL_H0"  # 机制不可行 或 30%+ cell 超理论界
    elif mean_mult <= 1.5 and ci_hi <= 1.8 and theory_U_hit_rate <= 0.1:
        return "PASS_H1"  # 机制可商用
    else:
        return "GRAY"  # 1.5 < mean < 2.0 或 CI 跨边界


# ---------------------------------------------------------------------------
# L3b `null-U` 读侧承载体 (P-2 · `K-D-14` 读侧改造 · 治理件 `4fdadf27b70c` §3-4)
#   ⛔ 0 改 `kill_decision` 之签名与函数体 (:419-:440 逐字保留 —— 本层之增量
#     **严格插于 :440 之后**, 故该 22 行之行号与字节皆不变)
#   ⛔ 0 动五切点 (其五字面 ⛔ 0 于本增量面复写 —— 沿 `K-D-14-R3`: 全件该五
#     字面之出现次数须 0 增); ⛔ 0 新设数值切点 (D-5)
#   改造之实质 = 第四实参**入参前**之处置: `:435`/`:437` 为裸数值比较、0 类型
#     分派, `inactive` 直入将抛 TypeError ⇒ ⛔ 0 于函数体内加分支 (沿
#     `K-D-14-R-NEW-4`)。故本层只新增「态 + 槽」二字段之承载体与 `ACTIVE`
#     把关, ⛔ 0 触碰既有判死面任一字节。
#   ⚠ 本层**未**登记于文件头之 L0-L5 结构表 (⛔ 0 改文件头一行 —— 改之即令
#     `:419`-`:440` 之行号漂移), 其归属为 L3 核区之读侧外围。
# ---------------------------------------------------------------------------

#: 态之在册词面 —— `ACTIVE` (唯一可入判之态; 沿 `30fed54c3d09` 之登记值,
#:   PI 2026-10-16 第八批卡 Q1, 生效 ms 1792155383737)。⛔ 0 造其同义词。
U_AXIS_STATE_ACTIVE = "ACTIVE"
#: 率槽为空 (`null-U`) 时之占位记号 —— **语义权威源 = 退役登记件 `1ba41ba3bbe9`
#:   之单一登记词** (PI 2026-10-17 卡 `ask_0676b2f68b0dc19dbad45ab1` Q1 opt1,
#   裁「丙为纲 · 甲为体」) ⇒ 本件之 `inactive` 与该登记词**为同一物**。
U_RATE_SLOT_INACTIVE = "inactive"
#: 取值面之声明 —— **开集** (限定③ · D-4): 态与槽之取值由**调用/报告面**按在册
#:   口径给值; ⛔ 0 于本件归并为封闭穷举集合、⛔ 0 映射改写 `inactive`、
#:   ⛔ 0 令既有 `inactive` 追溯失效。⛔ 0 在此声明 `inactive` 之归属穷举集。
U_AXIS_VALUE_SURFACE = "open"


def u_axis_carrier(theory_U_hit_rate, u_axis_state) -> dict:
    """`null-U` 之读侧承载体 —— **二字段**: `u_axis_state` (态) + `u_rate_slot` (槽)。

    落实 `K-D-14` 之三限定 (PI 2026-10-16 之裁 · 落账件 `141816a6aec9` §4-1):
      ① **态归 `U_axis_state` 元参**、`inactive` **仅作率槽之占位** ⇒ 二字段
         ⛔ 0 混同、⛔ 0 互代、⛔ 0 各造一态词汇 (D-2);
      ② `inactive` ⛔ 0 永作 `kill_decision` 之第四实参 ⇒ 入判须先经
         `u_axis_state == ACTIVE` 把关 (见 `kill_decision_gated`); 该把关之成立
         权 ⛔ 0 由本件断言 (`KD-NU-4` 仍开口);
      ③ `inactive` 须作**开集记号** ⇒ 取值面开集 (见 `U_AXIS_VALUE_SURFACE`),
         ⛔ 0 穷举、⛔ 0 映射改写、⛔ 0 追溯失效 (D-4)。

    `theory_U_hit_rate` 为 `None` (率槽为空 · `null-U`) 时, 槽位落占位记号
    `inactive`; ⛔ **0 以 `0.0` 充之** (沿 `1ba41ba3bbe9` §2-1 逐字「⛔ 0 赋实质
    值 `0.0`」—— `0.0` 在数值上等于「0 cell 超理论界」, 与「未测」**不同义**),
    亦 ⛔ 0 以 0 充之。

    ⛔ 0 代 PI 定 `U_axis_state` 之取值域 (沿 `K-D-14-R-NEW-2` 仍开口): 本函数
    ⛔ 0 校验其域、⛔ 0 设其枚举 —— 态**由调用面给**, 本件仅作等值把关。
    """
    if theory_U_hit_rate is None:
        slot = U_RATE_SLOT_INACTIVE
    else:
        slot = theory_U_hit_rate
    return {"u_axis_state": u_axis_state, "u_rate_slot": slot}


def kill_decision_gated(mean_mult, ci_lo, ci_hi, theory_U_hit_rate,
                        u_axis_state=U_AXIS_STATE_ACTIVE):
    """经 `u_axis_state == ACTIVE` 把关后之判死裁定 (限定② 之把关面 · D-3)。

    - 态 `== ACTIVE`: 第四实参方被求值并入判 ⇒ 输出与 `kill_decision` **逐字同**
      (含 `GRAY` 之可达性不变);
    - 态 `!= ACTIVE` (含 `null-U`): ⛔ 0 求值、⛔ 0 传入第四实参 ⇒ 返回 `None`
      (= **判死面不启用**, 沿 `1ba41ba3bbe9` 退役三面之第三面逐字) ⇒ ⛔ 0 抛
      TypeError、⛔ **0 落 `GRAY`** (`GRAY` 仅 `:439` 之 else 分支可达, 其义为
      「已测而未决」, ⛔ 0 充「未测」)。⛔ 0 造判死结论之新词 (故 ⛔ 0 产出
      `UNDECIDED` 之类字面)。

    ⚠ 态 ＝ `ACTIVE` 而率槽为空 (`null`) 者 ⇒ **输入自相矛盾** (声明可入判却
    无值可入) ⇒ 沿本件 L2 守卫体例「⛔ 0 静默通过: 守卫失败即 raise, 不产出读数」
    之纪律 **raise ValueError**, ⛔ 0 静默替值、⛔ 0 以 `0.0` 充之入判。
    ⛔ 0 由本件裁其处置 (候 PI 面, 登记于 P-2 验真报告)。
    """
    carrier = u_axis_carrier(theory_U_hit_rate, u_axis_state)
    if carrier["u_axis_state"] != U_AXIS_STATE_ACTIVE:
        return None
    if carrier["u_rate_slot"] == U_RATE_SLOT_INACTIVE:
        raise ValueError("u_axis_state=ACTIVE 与率槽为 null 自相矛盾: 入判之值"
                         " ⛔ 0 以占位记号充 (沿 v1 §2-2 ⛔ 0 注入 0.0/None 当作有效值)")
    return kill_decision(mean_mult, ci_lo, ci_hi, carrier["u_rate_slot"])


def u_axis_carrier_self_check() -> list:
    """承载体之防退化自证 (治理件 `4fdadf27b70c` §3-5) —— ⛔ **0 并入
    `self_test` 之 T1-T9** (⛔ 0 改既有默认路径之输出 ⇒ 须显式调用方可出读数)。

    逐项: ① **≥3 态** (n_distinct) 并报率槽读数之 min/max/std (⛔ 0 坍缩为常量、
    ⛔ 0 二值/常量返回之退化族); ② 槽为空 ⇒ 占位 `inactive` 且 ⛔ 0 == `0.0`;
    ③ 态 `== ACTIVE` 之**不变性** (与 `kill_decision` 直呼逐字同, 沿 T9 之 5 例,
    `GRAY` x2 之可达性成立 —— 防判据恒真/分支失活); ④ 态 `!= ACTIVE` ⇒ 返回
    ⛔ 0 为 `GRAY` 且**第四实参永不被求值** (以「比较即抛」之率值实测);
    ⑤ 自相矛盾之输入 ⇒ raise。

    返回: list of dict (`id` / `name` / `pass` / `detail` —— 体例同 `self_test`)。
    """

    class _ExplodingRate(object):
        """比较即抛之率值 —— 用于证「第四实参永不被求值」(若被求值即抛)。"""

        def __ge__(self, other):
            raise AssertionError("率槽之第四实参被求值: 把关失效")

        def __le__(self, other):
            raise AssertionError("率槽之第四实参被求值: 把关失效")

    results = []

    def add(tid, name, passed, detail):
        results.append({"id": tid, "name": name, "pass": bool(passed), "detail": detail})

    # ① 态之承载数 —— 开集之实测: 态由调用面给, 本件 0 枚举, 故以调用面自造之态测之
    probe_states = (U_AXIS_STATE_ACTIVE,) + tuple("CALLER_STATE_%d" % i for i in range(3))
    carried = [u_axis_carrier(None, st)["u_axis_state"] for st in probe_states]
    n_distinct = len(set(carried))
    add("C1", "态之承载: n_distinct>=3 (开集 · 0 枚举 · 防退化族)",
        n_distinct >= 3, "样态 %d / 去重 %d: %s" % (len(probe_states), n_distinct, ", ".join(carried)))

    # ② 率槽读数之 min/max/std (数值槽须逐字保留, ⛔ 0 坍缩为常量)
    vals = (Fraction(0), Fraction(1, 10), Fraction(3, 10), Fraction(1, 2), Fraction(1))
    slots = [u_axis_carrier(v, U_AXIS_STATE_ACTIVE)["u_rate_slot"] for v in vals]
    mean_s = sum(slots, Fraction(0)) / len(slots)
    var_s = sum((v - mean_s) ** 2 for v in slots) / len(slots)
    add("C2", "率槽读数: min/max/std 逐项报出 (⛔ 0 坍缩为常量)",
        slots == list(vals) and min(slots) != max(slots),
        "min=%s max=%s mean=%s std=%.6f n=%d" % (min(slots), max(slots), mean_s,
                                                 math.sqrt(float(var_s)), len(slots)))

    # ③ 槽为空 => 占位记号 inactive; ⛔ 0 以 0.0 充
    empty = u_axis_carrier(None, U_AXIS_STATE_ACTIVE)["u_rate_slot"]
    add("C3", "槽为空 => 占位记号 inactive 且 ⛔ 0 == 0.0",
        empty == U_RATE_SLOT_INACTIVE and not isinstance(empty, (int, float, Fraction)),
        "空槽得 %r (期望 %r)" % (empty, U_RATE_SLOT_INACTIVE))

    # ④ ACTIVE 之不变性 —— 沿 T9 之 5 例, 与 kill_decision 直呼逐字比
    #    ⛔ 0 于本件复写五切点之字面 (沿 `K-D-14-R3` 之全件计数 ⛔ 0 增) ⇒
    #    取 `T9_BOUNDARY_POINTS` 之既有登记值, 以位置索引之 (单一出处)
    p_m15, p_m18, p_m20, p_h18, p_h20, p_k01, p_k03 = (t[1] for t in T9_BOUNDARY_POINTS)
    t9_cases = (
        (p_m20, p_m15, p_h20, Fraction(0)),
        (Fraction(1), Fraction(3, 4), Fraction(5, 4), p_k03),
        (p_m15, Fraction(6, 5), p_h18, p_k01),
        (p_m18, p_m15, p_h20, Fraction(1, 5)),
        (Fraction(8, 5), Fraction(7, 5), Fraction(19, 10), Fraction(1, 5)),
    )
    gated = [kill_decision_gated(m, lo, hi, hit, U_AXIS_STATE_ACTIVE) for m, lo, hi, hit in t9_cases]
    direct = [kill_decision(m, lo, hi, hit) for m, lo, hi, hit in t9_cases]
    n_gray = sum(1 for g in gated if g == "GRAY")
    add("C4", "ACTIVE 之不变性: 与 kill_decision 直呼逐字同 (沿 T9 之 5 例)",
        gated == direct and n_gray == 2,
        "gated=%s / direct=%s; GRAY 可达 %d 例 (期望 2)" % (gated, direct, n_gray))

    # ⑤ 非 ACTIVE: 第四实参永不被求值, 且 ⛔ 0 落 GRAY
    got_nonactive, evaluated = [], False
    try:
        for st in probe_states[1:]:
            got_nonactive.append(
                kill_decision_gated(Fraction(1), Fraction(3, 4), Fraction(5, 4), _ExplodingRate(), st))
    except AssertionError:
        evaluated = True
    add("C5", "非 ACTIVE: 第四实参永不被求值 且 ⛔ 0 落 GRAY",
        (not evaluated) and got_nonactive == [None] * len(probe_states[1:]),
        "3 个非 ACTIVE 态之返回 %s (期望全 None); 比较即抛之率值未被求值=%s"
        % (got_nonactive, not evaluated))

    # ⑥ 自相矛盾之输入 (ACTIVE + 槽空) => raise, ⛔ 0 静默替值
    try:
        kill_decision_gated(Fraction(1), Fraction(3, 4), Fraction(5, 4), None, U_AXIS_STATE_ACTIVE)
        raised = False
    except ValueError:
        raised = True
    add("C6", "ACTIVE 且槽为空 => raise ValueError (⛔ 0 静默替值 · ⛔ 0 充 0.0)",
        raised, "raise=%s" % raised)

    return results


# ---------------------------------------------------------------------------
# L4 产表轨 (float) —— 薄封装: float 转换**只在出口**, 核内 0 float 运算
#   每处转换同时输出 exact_str (分数字面), ⛔ 0 以 float 列覆盖 exact 列
#   (0a031a9795a9 §6 L178: 报出口径须容「测试侧修正留痕」栏位)
# ---------------------------------------------------------------------------

def distortion_multiplier_float(d_llm, d_bayesian, eps, c=1.0) -> float:
    """产表轨之失真倍数: float(精确核读数)。仅出口一处转换。"""
    return float(distortion_multiplier(d_llm, d_bayesian, eps, c))


def cell_table_row(choice_readings, eps, c=1.0) -> dict:
    """产表行 (交付表之逐 cell 一行)。

    choice_readings: dict, 键如下 ——
      `choices`      (必需) 轨迹之实际选择序列
      `key_sets`     (必需) 轨迹之接受键序列
      `weights`      (可选) 逐轨迹权重, 默认均匀
      `h`            (可选) H 之入参 (G1 未锁 => 由入参传入, ⛔ 0 硬编码)
      `d_bayesian`   (可选) 该 cell 之基线失真读数; 给则并出倍数列
      `cell_id`      (可选) cell 标识
      `tests_side_correction_note` (可选) 「测试侧修正留痕」栏文本 (照录 0a031a9795a9 §6 L178)
    返回 dict: exact 列 (Fraction 及其字面) ＋ float 列 ＋ in_range 断言 ＋ 留痕栏。
    """
    if not isinstance(choice_readings, dict):
        raise TypeError("choice_readings 须为 dict, 实得 " + type(choice_readings).__name__)
    for key in ("choices", "key_sets"):
        if key not in choice_readings:
            raise ValueError("choice_readings 缺必需键: " + key)
    d_exact = distortion_indicator(
        choice_readings["choices"], choice_readings["key_sets"], choice_readings.get("weights")
    )
    row = {
        "cell_id": choice_readings.get("cell_id"),
        "d_exact": d_exact,
        "d_exact_str": str(d_exact),
        "d_float": float(d_exact),
        "in_range": None,
        "h": choice_readings.get("h"),
        "multiplier_exact": None,
        "multiplier_exact_str": None,
        "multiplier_float": None,
        "tests_side_correction_note": choice_readings.get("tests_side_correction_note", ""),
    }
    if row["h"] is not None:
        h_exact = _as_fraction(row["h"], "h")
        if h_exact < 0:
            raise ValueError("H 须 >= 0, 实得 " + str(h_exact))
        row["in_range"] = bool(Fraction(0) <= d_exact <= h_exact)
    if choice_readings.get("d_bayesian") is not None:
        mult = distortion_multiplier(d_exact, choice_readings["d_bayesian"], eps, c)
        row["multiplier_exact"] = mult
        row["multiplier_exact_str"] = str(mult)
        row["multiplier_float"] = float(mult)
    return row


# ---------------------------------------------------------------------------
# L5 自测 (T1-T9) —— 全部 0 calls / 0 网络 / 0 读 key / 0 写盘
# ---------------------------------------------------------------------------

def _build_trajectory(length, n_reject):
    """构造单条轨迹: 前 n_reject 位之键集为空集 (该位被判为拒绝), 其余位键集含所择。

    仅供自测之离线枚举, 不引入任何数值阈值。
    """
    actions = tuple(range(1, length + 1))
    keys = []
    for t in range(length):
        keys.append(frozenset() if t < n_reject else frozenset({actions[t]}))
    return (actions,), (tuple(keys),)


def _bit_identical(x, y):
    """两个 float 之 IEEE-754 双精度位面是否逐位相符 (⛔ 0 以容差判定)。"""
    return struct.pack("<d", x) == struct.pack("<d", y)


def _multiplier_float_impl(g_l, g_b, eps, c):
    """**独立** 之 float 实现 (纯 float 算术, ⛔ 不经 Fraction) —— 供 T7 之 S7 一致率对拍。"""
    den = g_b if g_b >= c * eps else c * eps
    return g_l / den


def self_test(verbose=True) -> dict:
    """执行 T1-T9, 返回逐项 pass/fail ＋ 留痕 (照录 0a031a9795a9 §6 L178 之留痕栏)。

    判据一律照录正典 (spec L68/L88/L91/L103-L110/L116, 0a031a9795a9 §6 ①-④ 与
    §3-3 依据栏) 或为代数恒等式; **⛔ 0 新拟数值阈值**。
    """
    results = []
    trail = []

    def record(tid, name, passed, detail, corrections=None):
        results.append({"id": tid, "name": name, "pass": bool(passed), "detail": detail})
        for line in (corrections or []):
            trail.append({"id": tid, "note": line})

    # ---- T1 正典例向量 (0a031a9795a9 §6 ③ L172 逐字) ----
    ok1, d1 = True, []
    try:
        got_c1 = distortion_multiplier(Fraction(2), Fraction(0), Fraction(1, 10), Fraction(1))
        got_c2 = distortion_multiplier(Fraction(2), Fraction(0), Fraction(1, 10), Fraction(2))
        ok1 = (got_c1 == Fraction(20)) and (got_c2 == Fraction(10))
        d1 = ["c=1 得 %s (期望 20)" % got_c1, "c=2 得 %s (期望 10)" % got_c2]
    except Exception as exc:  # noqa: BLE001 - 自测须报失败而非抛出
        ok1, d1 = False, ["异常: %r" % exc]
    record("T1", "正典例向量 G_L=2,G_B=0,eps=0.1 -> c=1 得 20 / c=2 得 10", ok1, "; ".join(d1),
           ["测试侧留痕: eps 以 Fraction(1,10) 给。若以 float 字面 0.1 给, "
            "assert_eps 精确化为 3602879701896397/36028797018963968, 倍数非 20 —— "
            "修正依据 = 精确有理枚举本身 (0a031a9795a9 §6 L178), 非对方数值"])

    # ---- T2 守卫两支路 (0a031a9795a9 §6 ③ L172) ----
    ok2, d2 = True, []
    try:
        # ① 无守卫支路: G_B >= c*eps => 分母 = G_B 且 c 精确消去
        den = guarded_denominator(Fraction(5), Fraction(1, 10), Fraction(2))
        cancel_lhs = (Fraction(8) / Fraction(2)) / (Fraction(5) / Fraction(2))
        cancel_rhs = Fraction(8) / Fraction(5)
        branch1 = (den == Fraction(5)) and (cancel_lhs == cancel_rhs)
        d2.append("无守卫支路 分母=%s c消去=%s" % (den, cancel_lhs == cancel_rhs))
        # ② 守卫支路: G_B = 0 => G_L/(c*eps) 且 c 不消去
        den0_c1 = guarded_denominator(Fraction(0), Fraction(1, 10), Fraction(1))
        den0_c2 = guarded_denominator(Fraction(0), Fraction(1, 10), Fraction(2))
        m_c1 = distortion_multiplier(Fraction(2), Fraction(0), Fraction(1, 10), Fraction(1))
        m_c2 = distortion_multiplier(Fraction(2), Fraction(0), Fraction(1, 10), Fraction(2))
        branch2 = (den0_c1 == Fraction(1, 10)) and (den0_c2 == Fraction(1, 5)) \
            and (m_c1 == Fraction(20)) and (m_c2 == Fraction(10))
        d2.append("守卫支路 c=1 分母=%s 倍数=%s / c=2 分母=%s 倍数=%s"
                  % (den0_c1, m_c1, den0_c2, m_c2))
        ok2 = branch1 and branch2
    except Exception as exc:  # noqa: BLE001
        ok2, d2 = False, ["异常: %r" % exc]
    record("T2", "守卫两支路: 无守卫支路 c 精确消去 / 守卫支路 c 不消去", ok2, "; ".join(d2))

    # ---- T3 代数恒等式网格 (D2_identity_grid_10k) ----
    ok3, d3, checked3 = True, [], 0
    try:
        for g_l in GRID_G_L:
            for g_b in GRID_G_B:
                for cc in GRID_C:
                    for e in GRID_EPS:
                        checked3 += 1
                        lhs = distortion_multiplier(g_l, g_b, e, cc)
                        den_rs = guarded_denominator_rescaled(g_b, e, cc)
                        rhs = (g_l / cc) / den_rs
                        if lhs != rhs:  # 逐点精确相等, ⛔ 0 用容差
                            ok3 = False
                            d3.append("失配于 G_L=%s G_B=%s c=%s eps=%s" % (g_l, g_b, cc, e))
                            break
                    if not ok3:
                        break
                if not ok3:
                    break
            if not ok3:
                break
        d3 = ["网格点数=%d (期望 %d)" % (checked3, GRID_SIZE)] + d3
        ok3 = ok3 and (checked3 == GRID_SIZE)
    except Exception as exc:  # noqa: BLE001
        ok3, d3 = False, ["异常: %r" % exc]
    record("T3", "代数恒等式网格 D2_identity_grid_10k: G_L/max(G_B,c*eps) == (G_L/c)/max(G_B/c,eps)",
           ok3, "; ".join(d3))

    # ---- T4 D ∈ [0,H] 边界 (0a031a9795a9 §5 L157; H 由入参传入, G1 未锁) ----
    ok4, d4 = True, []
    try:
        for h in (1, 4, 33):
            for n_rej in (0, h):
                (acts,), (keys,) = _build_trajectory(h, n_rej)
                d_val = distortion_indicator((acts,), (keys,))
                in_range = Fraction(0) <= d_val <= Fraction(h)
                if not in_range or d_val != Fraction(n_rej):
                    ok4 = False
                    d4.append("H=%d n_rej=%d 得 %s" % (h, n_rej, d_val))
        # B10: 基数损失量级不入 D —— 全拒之 D 须仍为计数 H, 非 1
        (acts33,), (keys33,) = _build_trajectory(33, 33)
        d_full = distortion_indicator((acts33,), (keys33,))
        if d_full != Fraction(33):
            ok4 = False
            d4.append("B10 失守: 全拒 D=%s 非 33" % d_full)
        d4.append("端点样例(H=1/4/33 × n_rej=0/H)全过; 全拒 D=%s" % d_full)
    except Exception as exc:  # noqa: BLE001
        ok4, d4 = False, ["异常: %r" % exc]
    record("T4", "D∈[0,H] 边界 + B10 基数不入 D", ok4, "; ".join(d4))

    # ---- T5 枚举面自检 (A 对象 15 键 / C 对象 3H/4 / D 对象 三处更正代数) ----
    ok5, d5, corr5 = True, [], []
    try:
        # A 对象: 4 元动作集之非空子集
        keysets = []
        for mask in range(1, 1 << len(T5_ACTION_ALPHABET)):
            sub = frozenset(T5_ACTION_ALPHABET[i]
                            for i in range(len(T5_ACTION_ALPHABET)) if mask >> i & 1)
            keysets.append(sub)
        a_ok = (len(keysets) == T5_EXPECTED_KEYSET_COUNT) and all(len(s) > 0 for s in keysets)
        ok5 = ok5 and a_ok
        d5.append("A 对象 非空键集=%d(期望 %d)" % (len(keysets), T5_EXPECTED_KEYSET_COUNT))
        # C 对象: 3H/4, H = 1..100
        reachable = 0
        unreachable = 0
        for h in T5_H_SCAN:
            target = Fraction(3 * h, 4)
            if target.denominator == 1:
                n_rej = int(target)
                (acts,), (keys,) = _build_trajectory(h, n_rej)
                d_val = distortion_indicator((acts,), (keys,))
                if d_val != target or not (Fraction(0) <= d_val <= Fraction(h)):
                    ok5 = False
                    d5.append("C 对象失配 H=%d 得 %s 期望 %s" % (h, d_val, target))
                reachable += 1
            else:
                unreachable += 1
        d5.append("C 对象 3H/4: 可达(H%%4==0) %d 例 / 非整除 %d 例"
                  % (reachable, unreachable))
        corr5.append("测试侧留痕: C 对象 3H/4 于 H%4!=0 时非整数, 非可达之拒绝计数, "
                     "如实登记不计入失败 (修正依据 = 精确有理枚举本身, 0 依赖对方数值)")
        # D 对象: 三处更正代数 —— 恒等式网格 + 例值 20/10
        d_ok = True
        for e in (Fraction(1, 10), Fraction(1, 2)):
            for cc in (Fraction(1), Fraction(2)):
                if distortion_multiplier(Fraction(2), Fraction(0), e, cc) != \
                        Fraction(2) / (cc * e):
                    d_ok = False
        if distortion_multiplier(Fraction(2), Fraction(0), Fraction(1, 10), Fraction(1)) != Fraction(20):
            d_ok = False
        if distortion_multiplier(Fraction(2), Fraction(0), Fraction(1, 10), Fraction(2)) != Fraction(10):
            d_ok = False
        ok5 = ok5 and d_ok
        d5.append("D 对象 三处更正代数(网格 + 例值 20/10) %s" % ("全过" if d_ok else "有失配"))
    except Exception as exc:  # noqa: BLE001
        ok5, d5 = False, ["异常: %r" % exc]
    record("T5", "枚举面: A(15 非空键集) / C(3H/4, H=1..100) / D(三处更正代数)", ok5,
           "; ".join(d5), corr5)

    # ---- T6 聚合面 (0a031a9795a9 §3-3 依据栏 L87) ----
    ok6, d6 = True, []
    corr6 = ["测试侧留痕: 首写用例取权重 (1/3, 1/3, 1/3), 而精确有理求和 1/3*3 == 1 "
             "⇒ 守卫正确地未 raise, 系**用例侧**之误, 非守卫失效; 已改用精确和为 11/12 的 "
             "非单位权重组 (1/3, 1/3, 1/4) 复测。修正依据 = 精确有理枚举本身, 0 依赖对方数值"]
    try:
        # ① 权重和须精确 = 1, 否则 raise
        raised = False
        try:
            assert_weights_sum_one((Fraction(1, 3), Fraction(1, 3), Fraction(1, 4)))
        except ValueError:
            raised = True
        if not raised:
            ok6 = False
            d6.append("权重和 11/12 未 raise")
        # 对照: 精确和恰为 1 之组须通过 (逐位判定, ⛔ 0 用容差)
        try:
            assert_weights_sum_one((Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)))
        except ValueError:
            ok6 = False
            d6.append("权重和精确 = 1 之组误报 raise")
        # ② err_tau 与手算逐例相符
        (a1,), (k1,) = _build_trajectory(4, 1)
        (a2,), (k2,) = _build_trajectory(4, 3)
        d_hand = Fraction(1, 2) * 1 + Fraction(1, 2) * 3
        d_got = distortion_indicator((a1, a2), (k1, k2))
        if d_got != d_hand:
            ok6 = False
            d6.append("手算 %s 与实现 %s 不符" % (d_hand, d_got))
        d6.append("手算 D=%s 实现 D=%s" % (d_hand, d_got))
        # ③ 0 以轨迹内决策数再加权 —— 异长轨迹下均匀权给出 1/2, 而决策数加权会给 1/3
        (a3,), (k3,) = _build_trajectory(2, 0)
        (a4,), (k4,) = _build_trajectory(1, 1)
        d_noreweight = distortion_indicator((a3, a4), (k3, k4))
        if d_noreweight != Fraction(1, 2):
            ok6 = False
            d6.append("再加权防线失守: 得 %s 期望 1/2" % d_noreweight)
        d6.append("异长轨迹(2,1)均匀权 D=%s (决策数加权将给 1/3)" % d_noreweight)
    except Exception as exc:  # noqa: BLE001
        ok6, d6 = False, ["异常: %r" % exc]
    record("T6", "聚合面: 权重和=1 raise / err 手算相符 / 0 以轨迹内决策数再加权", ok6,
           "; ".join(d6), corr6)

    # ---- T7 双轨一致率 S7 (照录 7551c47d3ece §2-5 之 S7) ----
    ok7, d7 = True, []
    corr7 = ["测试侧留痕: 双轨对照规则(容差有无及其值)盘上 0 候选 (KD-3/P3) => "
             "本件仅报实测一致率与最大相对偏差, ⛔ 0 代定判据"]
    try:
        total = 0
        identical = 0
        max_rel = Fraction(0)
        for g_l in GRID_G_L[::5]:
            for g_b in GRID_G_B[::10]:
                for cc in GRID_C:
                    for e in GRID_EPS:
                        exact = distortion_multiplier(g_l, g_b, e, cc)
                        via_float = float(exact)
                        independent = _multiplier_float_impl(
                            float(g_l), float(g_b), float(e), float(cc))
                        total += 1
                        if _bit_identical(via_float, independent):
                            identical += 1
                        else:
                            denom = float(exact) if exact != 0 else Fraction(1)
                            rel = abs(Fraction(independent) - exact) / abs(denom)
                            if rel > max_rel:
                                max_rel = rel
        rate = Fraction(identical, total)
        d7.append("逐位相符 %d/%d (一致率 %s); 最大相对偏差 %s"
                  % (identical, total, rate, max_rel))
        ok7 = (total > 0)
    except Exception as exc:  # noqa: BLE001
        ok7, d7 = False, ["异常: %r" % exc]
    record("T7", "双轨一致率 S7: Fraction 轨 float(exact) vs 独立 float 实现", ok7,
           "; ".join(d7), corr7)

    # ---- T8 指纹面自测 (spec 包 §5 之 1 / 0a031a9795a9 §3-6) ----
    ok8, d8 = True, []
    try:
        here = os.path.abspath(__file__)
        raw = io.open(here, "rb").read()
        sha12 = hashlib.sha256(raw).hexdigest()[:12]
        text = raw.decode("utf-8", errors="strict")
        n_forbidden = text.count(_FORBIDDEN_CALL)
        bom = raw[:3] == b"\xef\xbb\xbf"
        n_cr = raw.count(b"\r")
        n_tab = raw.count(b"\t")
        n_repl = text.count("\ufffd")
        d8.append("本件 sha256_12=%s bytes=%d; 内建散列调用出现 %d 次; BOM=%s CR=%d TAB=%d U+FFFD=%d"
                  % (sha12, len(raw), n_forbidden, bom, n_cr, n_tab, n_repl))
        ok8 = (n_forbidden == 0) and (not bom) and (n_cr == 0) and (n_tab == 0) and (n_repl == 0)
    except Exception as exc:  # noqa: BLE001
        ok8, d8 = False, ["异常: %r" % exc]
    record("T8", "指纹面: hashlib.sha256 算定 / 0 内建散列调用 / BOM=False CR=0 TAB=0",
           ok8, "; ".join(d8))

    # ---- T9 判死面转引测试 (spec L103-L110 逐字) ----
    ok9, d9 = True, []
    try:
        pt = dict(T9_BOUNDARY_POINTS)
        cases = (
            # (mean_mult, ci_lo, ci_hi, theory_U_hit_rate, 期望)
            # 分支一 FAIL_H0: mean >= 2.0
            (pt["mean=2.0"], pt["mean=1.5"], pt["ci_hi=2.0"], Fraction(0), "FAIL_H0"),
            # 分支一 FAIL_H0: theory_U_hit_rate >= 0.3
            (Fraction(1), Fraction(3, 4), Fraction(5, 4), pt["hit=0.3"], "FAIL_H0"),
            # 分支二 PASS_H1: mean <= 1.5 且 ci_hi <= 1.8 且 hit <= 0.1 (三项边界值齐取)
            (pt["mean=1.5"], Fraction(6, 5), pt["ci_hi=1.8"], pt["hit=0.1"], "PASS_H1"),
            # 分支三 GRAY: 1.5 < mean < 2.0
            (pt["mean=1.8"], pt["mean=1.5"], pt["ci_hi=2.0"], Fraction(1, 5), "GRAY"),
            # 分支三 GRAY: mean 合格但 ci_hi 越过 1.8
            (Fraction(8, 5), Fraction(7, 5), Fraction(19, 10), Fraction(1, 5), "GRAY"),
        )
        for mean_m, lo, hi, hit, expect in cases:
            got = kill_decision(mean_m, lo, hi, hit)
            if got != expect:
                ok9 = False
                d9.append("mean=%s lo=%s hi=%s hit=%s 得 %s 期望 %s"
                          % (mean_m, lo, hi, hit, got, expect))
        d9.append("五例逐字相符: FAIL_H0 ×2 / PASS_H1 ×1 / GRAY ×2; "
                  "边界点(mean 1.5/1.8/2.0, ci_hi 1.8/2.0, hit 0.1/0.3)全用")
    except Exception as exc:  # noqa: BLE001
        ok9, d9 = False, ["异常: %r" % exc]
    record("T9", "判死面转引测试: kill_decision 三分支边界点输出逐字相符", ok9, "; ".join(d9))

    summary = {
        "anchor_id": ANCHOR_ID,
        "anchor_path": ANCHOR_PATH,
        "version": VERSION,
        "c_default": str(DEFAULT_C),
        "total": len(results),
        "passed": sum(1 for r in results if r["pass"]),
        "failed": sum(1 for r in results if not r["pass"]),
        "all_pass": all(r["pass"] for r in results),
        "results": results,
        "trail": trail,
    }
    if verbose:
        _print_report(summary)
    return summary


def _print_report(summary) -> None:
    """stdout 报告 (唯一输出面; ⛔ 0 写盘)。"""
    write = sys.stdout.write
    write("=" * 78 + "\n")
    write("distortion_calculator 自测报告 (T1-T9) | 锚 %s @ %s | version=%s\n"
          % (summary["anchor_id"], summary["anchor_path"], summary["version"]))
    write("=" * 78 + "\n")
    for item in summary["results"]:
        write("[%s] %-4s %s\n" % ("PASS" if item["pass"] else "FAIL",
                                   item["id"], item["name"]))
        if item["detail"]:
            write("        %s\n" % item["detail"])
    write("-" * 78 + "\n")
    write("小计: %d/%d 通过; all_pass=%s\n"
          % (summary["passed"], summary["total"], summary["all_pass"]))
    if summary["trail"]:
        write("-" * 78 + "\n")
        write("测试侧修正留痕栏 (0a031a9795a9 §6 L178):\n")
        for note in summary["trail"]:
            write("  - [%s] %s\n" % (note["id"], note["note"]))
    write("=" * 78 + "\n")


def _reconfigure_stdout():
    """Windows 控制台之下保证 UTF-8 输出 (沿仓内既有体例)。"""
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def main(argv) -> int:
    _reconfigure_stdout()
    if "--self-test" in argv:
        summary = self_test(verbose=True)
        return 0 if summary["all_pass"] else 1
    sys.stdout.write("用法: python tools/distortion_calculator.py --self-test\n")
    sys.stdout.write("（本件 0 网络 0 读 key 0 写盘; 唯一输出面为 --self-test 之 stdout）\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
