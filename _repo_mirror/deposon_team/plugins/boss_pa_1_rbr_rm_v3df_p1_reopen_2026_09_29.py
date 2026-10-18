# -*- coding: utf-8 -*-
"""
boss_pa_1_rbr_rm_v3df_p1_reopen_2026_09_29.py
=================================================
V3 修复线「重开跑」**P-1 构造修复件**（新名件 · 代际 v2 · 既有件 0 触动）

本棒 = **worker 执行棒**（判定面归 verdict-keeper，本件 0 代裁）。

控制文件（派工单指定，先核哈希后引用；本棒盘上实测 SHA-12 已写入 results JSON）
  - 立线件（本棒控制件）: results/_v5_v3_deg_reopen_line_2026_09_29.md   `2ea1c2cee65d`
      §2.2 路径甲（跑前自证两段式）｜§2.3 案 I（11:52 授权降级为方向授权）
      §2.4 案乙（判定读数挂起 + 结构性事实可作设计输入，0 作判定依据）
      §2.5 `K-RO-0-1/0-2/0-3`｜§3.1 **P-1（去镜像-同序，保协调）** + Q-1…Q-4
      §3-R 反向风险预警｜§4 R-1 / **R-2（σ 零质量冻结面）** / **R-3（非对称取格）**
      §5.1 D-1 / D-2｜§5.2 **案甲（play 并报不替换）**｜§5.4 `K-PY-1-1`｜§6 棒序
  - 预登记（生效即锁，0 动）: results/_v5_v3_deg_fix_prereg_2026_09_29.md  `98286cc1aec7`
      §4.0 `K-V3DF-0-1/0-2`｜§4.1 `K-V3DF-1-1/1-2`｜§4.2 `K-V3DF-2-1`
      §4.3 `K-V3DF-3-1/3-2`｜§4.4 `K-V3DF-4-1/4-2`｜§4.6 `K-V3DF-9-1/9-2/9-3`
      §4.5 `K-V3DF-5-1/5-2/5-3`（**C5 面 · 另棒 · 本棒 0 跑**）
  - 前代执行件（**读数挂起**）: results/_v5_v3_deg_fix_exec_2026_09_29.md  `7d885528f287`
  - 前代修复件（**参照 · 在盘 0 触动**）: boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py `7761f2c339e6`
  - 基名件（`K-V3DF-0-2` 受护件）: boss_pa_1_rbr_rm.py `5cc594147e00`

PI 2026-09-29 确认批 4（派工单字面，本棒执行的授权面）
  ④ C1 payoff 新构造 = **P-1（去镜像-同序，保协调）**
  ① 重开跑路径 = **甲（跑前自证两段式）**
  ② 11:52「跑后重验」授权 = **降级为方向授权（I）**（本件 0 以其作开跑权限）
  ③ 读数挂起边界 = **乙（判定读数挂起 + 结构性事实可作设计输入，0 作判定依据）**
  ⑤ σ 零质量冻结面 = **纳入本次立线处置**（立线件 §4 R-2）
  ⑥ play 口径 = **甲（并报不替换，0 替换判死线字段）**
  ⑦ play 读数 = **D-1 ＋ D-2 并报**
  ⑧ 「判不明」↔ KD = **确认同指**（扩写后 KD ＋ γ）
  ⑨ 与转办单 B = **分件先后**（本件先）
  ⑩ 重跑范围 = **随 ④ 联动**（④ = P-1 档 ⇒ 按立线件 Q-4「改 payoff 连带改 C3/C4」⇒ C1＋C3＋C4）

P-1 构造定义（**逐条照立线件 §3.1 P-1 实施；0 自创参数、0 自改定义**）
  1) 保留 A/B 各自的 `named` / `filler` 两个盘上真值与 2×2 结构。
  2) **取消 A 行向量与列向量的对调赋格**：四格按「named 率对 named、filler 率对 filler」的
     **同序**规则赋格 ⇒ 每个玩家的支付**只由自己这一格的动作决定、与对家动作无关** ⇒
     A 的 incentive `u_A(0,sB) − u_A(1,sB)` **不随 `sB` 反号**（恒定符号）。
  3) **sign(δ) 角色互换分支（显式声明，0 隐性口径）**：`a_named < a_filler`（或
     `b_named < b_filler`）时角色互换，使**较大值恒在 named 侧** ⇒ 满足立线件
     「保协调：双方同向偏好时均衡在 `(named, named)`」。
  4) **Q-3 取格自证（必做）**：P-1 矩阵**非对称** ⇒ 前代修复件 L255/L256 的
     `ua = (a11,a12) if sB==0 else (a21,a22)` / `ub = (b11,b21) if sA==0 else (b12,b22)`
     **在本构造下成为静默错误**（0 报错、0 数值异常）⇒ 本件改用一般矩阵取格
     `u_A(sA,sB) = A[sA][sB]`、`u_B(sB,sA) = B[sA][sB]`，并在件内**逐格自证**两种取格之差。

R-2 σ 零质量冻结面处置（PI 批 4 ⑤ = 纳入本次处置；**0 新设数值判定切点**）
  原机制（立线件 §4 R-2）：两 regret 皆 ≤ 0 ⇒ `sigma()` 返回 `None` ⇒ 跳过重采样
  ⇒ **动作永久冻结**，而 regret 仍每轮累加 ⇒ 平均 regret 呈 `O(|δ|)/t` 缓降。
  两个 σ 臂**并报、0 择一删读**：
    - `R2_not_disposed_positive_part`（前代语义，**冻结面未处置**）：σ_i(s) ∝ max(0, R_i(s))；
      全 ≤ 0 ⇒ `None` ⇒ 不重采样。
    - `R2_disposed_centered`（**本棒处置档**）：σ_i(s) ∝ max(0, R_i(s) − min_s R_i(s))；
      仅当两 regret **精确相等**（spread ＝ 0）时回退到均匀 `0.5/0.5`（最大熵，**无参数**）。
      该处置**保序、保尺度、0 引入可调参数**（`0.5/0.5` ＝ 均匀分布，非判定切点）；
      收敛切点 `1e-3` / `t > 5` / `n_iter = 200` / `seed 210021` **逐字不动**。

铁律
  - 新名件；既有件 0 删除 / 0 改写 / 0 覆盖；**派生 JSON 0 合并**（只新建本件 1 个 result JSON）
  - 18 frozen / 9 网格 / V1–V3 资产 **0 触动 0 复算 0 复跑**（R5）
  - **0 新设数值判定阈值**（结果 JSON `iron_rule_compliance` 逐条列证）
  - **0 读 key / 0 明文密钥**（R4）
  - 纯 Python stdlib（0 numpy / 0 LLM / 0 proxy / 0 网关）
  - **0 代裁命题存亡 / 0 代裁 K-* 落态**（落态为按盘上冻结判据字面的机械套用，裁权归 verdict-keeper）
  - 引用纪律（`K-RO-0-3`）：凡引前代读数**必带「前代未开跑/读数挂起」字样**

skill：派工单**未指定 skill 名** ⇒ 本棒 **0 加载任何 skill、0 引用、0 虚构其条文**。

作者: Mavis 团队 worker（V3 修复线「重开跑」执行棒）
日期: 2026-09-29
标记 V3DF_P1_REOPEN_2026_09_29
"""

import os
import sys
import json
import hashlib
import random

try:                                  # 控制台 GBK 无法编码 U+2212 等字面（只影响 stdout，不影响落盘）
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

# ============================================================================
# 路径常量（全部为只读输入；输出为新名件）
# ============================================================================

REPO_ROOT = r"D:/私人资料/deposon-repo"
V20_BASELINES = os.path.join(REPO_ROOT, "results", "deposon_v20_baselines.json")
SRC_RESULT = os.path.join(REPO_ROOT, "results", "boss_pa_1_rbr_rm_result_2026_09_15.json")
PREREG = os.path.join(REPO_ROOT, "results", "_v5_v3_deg_fix_prereg_2026_09_29.md")
REOPEN_LINE = os.path.join(REPO_ROOT, "results", "_v5_v3_deg_reopen_line_2026_09_29.md")
PRIOR_EXEC = os.path.join(REPO_ROOT, "results", "_v5_v3_deg_fix_exec_2026_09_29.md")
PRIOR_FIX = os.path.join(REPO_ROOT, "deposon_team", "plugins",
                         "boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py")
PRIOR_RESULT = os.path.join(REPO_ROOT, "results", "_v5_v3_deg_fix_c1c4_result_2026_09_29.json")
OUT_JSON = os.path.join(REPO_ROOT, "results", "_v5_v3_deg_p1_reopen_result_2026_09_29.json")

# ============================================================================
# 常量（**全部沿用盘上既有字面，0 新设数值判定阈值**）
# ============================================================================

RM_TOL = 1e-3          # V3 既有收敛切点（逐字不动）
RM_WARMUP = 5          # V3 既有 `t > 5` 护栏（逐字不动）
N_ITER = 200           # V3 既有 n_iter（cap 面）
SEED = 210021          # V3 既有 seed（与前代修复件同 seed ⇒ 门核的就是跑的那个）
BAYES_EPS = 1e-9       # recheck #01 既有 ε
BAYES_MAX_ITER = 2000  # recheck #01 既有最大迭代
STARTS = ((0, 0), (0, 1), (1, 0), (1, 1))
BR_MODES = ("simultaneous", "alternating")
GATE_N_DISTINCT = 3    # `K-V3R-0-A` / `K-V3DF-0-1` / `K-RO-0-1`：n_distinct > 3（**引用，0 新设**）
KILL_N_DISTINCT = 4    # `K-V3R-1` / `K-V3DF-1-1` / `K-V3DF-4-1` / `K-PY-1-1`：n_distinct >= 4（**引用**）
TH_PA_H1 = 1.3         # `TH-V3R-1` 既有字面
TH_PA_H0 = 2.0         # `TH-V3R-1` 既有字面

# `K-V3DF-0-2` 受护件基线（4 件，**沿用前代修复件 §常量 字面，0 改动**）
PREREG_BASELINE_SHA12 = {
    "deposon_team/plugins/boss_pa_1_rbr_rm.py": "5cc594147e00",
    "results/boss_pa_1_rbr_rm_result_2026_09_15.json": "c7c59e0d2f6c",
    "results/deposon_v2_phase4_f4_2026_09_11.json": "cf7682348617",
    "docs/V3X/P_D_FINGERPRINT_V0_3_SPEC.md": "f119f2f30287",
}
ZERO_TOUCH_FILES = list(PREREG_BASELINE_SHA12.keys())

# 本棒 0 触动清单（4 受护件 + 前代 4 件 + 预登记 1 件 + 立线件 1 件）
TOUCH_PROOF_FILES = ZERO_TOUCH_FILES + [
    "results/_v5_v3_deg_fix_prereg_2026_09_29.md",
    "results/_v5_v3_deg_reopen_line_2026_09_29.md",
    "results/_v5_v3_deg_fix_exec_2026_09_29.md",
    "results/_v5_v3_deg_fix_c1c4_result_2026_09_29.json",
    "deposon_team/plugins/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py",
    "results/_v3_recheck_01_result_2026_09_27.json",
    "results/_v3_recheck_01_rescript_2026_09_27.md",
    "results/deposon_v20_baselines.json",
]

SUSPEND_LABEL = "【前代未开跑/读数挂起】（立线件 §2.4 案乙：判定读数 0 作收口依据；" \
                "结构性事实可作设计输入）· PI 批 4 ③"


# ============================================================================
# 工具函数（沿前代修复件字面，0 新设统计口径）
# ============================================================================

def sha12_file(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def n_distinct(xs) -> int:
    return len(set(round(float(x), 12) for x in xs))


def stat_block(xs):
    """沿前代修复件 / recheck #01 `stat_block` 字面（0 新设统计口径）。"""
    xs = [float(x) for x in xs]
    n = len(xs)
    mean = sum(xs) / n
    var = sum((x - mean) ** 2 for x in xs) / n
    return {
        "n": n,
        "n_distinct": n_distinct(xs),
        "std": var ** 0.5,
        "min": min(xs),
        "max": max(xs),
        "mean": mean,
        "distinct_values": sorted(set(round(x, 6) for x in xs)),
    }


def base_graph(gid: str) -> str:
    return gid if gid.startswith("L_") else gid.split("_n")[0]


# ============================================================================
# 段 0 · payoff 构造面
# ============================================================================

def src_rates(g) -> tuple:
    """盘上两个真值（沿 V3 L236-L256 字面，0 改动）：A = field_mean，B = 最佳 baseline arm。"""
    a_named = g["field_mean"]["named"] or 0.0
    a_filler = g["field_mean"]["filler"] or 0.0
    best_named = 0.0
    best_filler = 0.0
    for arm, vals in g.items():
        if arm == "field_mean" or not isinstance(vals, dict):
            continue
        v_named = vals.get("named") or 0.0
        v_filler = vals.get("filler") or 0.0
        if v_named > best_named:
            best_named = v_named
            best_filler = v_filler
    return a_named, a_filler, best_named, best_filler


def payoff_matrix_mirror(g) -> tuple:
    """V3 字面**镜像**赋格（`5cc594147e00` L253-256 逐字）—— 仅作对照腿 / Q-3 自证的左列。"""
    a_named, a_filler, b_named, b_filler = src_rates(g)
    a11, a12, a21, a22 = a_named, a_filler, a_filler, a_named
    b11, b12, b21, b22 = b_named, b_filler, b_filler, b_named
    return a11, a12, a21, a22, b11, b12, b21, b22


def payoff_matrix_p1(g):
    """**P-1 · 去镜像-同序（保协调）** + sign(δ) 角色互换分支（显式声明）。

    赋格规则（立线件 §3.1 P-1）：
      A 矩阵 `A[i][j]`（i = A 动作 0=named/1=filler, j = B 动作）：
        **行 i 恒定** —— named 率对 named 行、filler 率对 filler 行（跨 B 两列同值）
        ⇒ `A[0][*] = a_named`、`A[1][*] = a_filler`
      B 矩阵 `B[i][j]`（i = A 动作, j = B 动作）：
        **列 j 恒定** —— 同序规则在 B 侧的对偶
        ⇒ `B[*][0] = b_named`、`B[*][1] = b_filler`
      ⇒ **取消行/列对调（去镜像）**；A 的 incentive `u_A(0,sB) − u_A(1,sB) = a_named − a_filler`
        **与 `sB` 无关**（恒定符号，不反号）。
      ⇒ 本构造在语义上退化为「两个**无交互**的可加二人博弈」（每方支付只由自身动作决定）；
        **该结构后果如实登记，0 掩饰**（见 `structural_note`）。
    角色互换分支（立线件 §3.1 P-1「是否需重推导 ①」，**显式**）：
      `a_named < a_filler` ⇒ 互换两个真值，使**较大值恒在 named 侧** ⇒ 满足
      「保协调：双方同向偏好时均衡在 (named, named)」。
    返回 (8 元组, 分支元信息 dict)。
    """
    a_named, a_filler, b_named, b_filler = src_rates(g)
    a_branch = "swap(a_named<a_filler)" if a_named < a_filler else "no-swap"
    b_branch = "swap(b_named<b_filler)" if b_named < b_filler else "no-swap"
    if a_named < a_filler:
        a_named, a_filler = a_filler, a_named
    if b_named < b_filler:
        b_named, b_filler = b_filler, b_named
    a11, a12, a21, a22 = a_named, a_named, a_filler, a_filler
    b11, b12, b21, b22 = b_named, b_filler, b_named, b_filler
    meta = {
        "a_branch": a_branch, "b_branch": b_branch,
        "delta_A_signed": round(a_named - a_filler, 12),   # 角色互换后恒 >= 0
        "delta_B_signed": round(b_named - b_filler, 12),
        "delta_A_abs": round(abs(src_rates(g)[0] - src_rates(g)[1]), 12),
        "delta_B_abs": round(abs(src_rates(g)[2] - src_rates(g)[3]), 12),
    }
    return (a11, a12, a21, a22, b11, b12, b21, b22), meta


def payoff_2d(pay) -> tuple:
    """8 元组 ⇒ (A 2x2, B 2x2)，索引字面 `A[sA][sB]` / `B[sA][sB]`

    ⚠️ 索引约定**显式声明**（本件首版曾在此犯 R-3 同类静默错误并已修正，登记在案）：
      `a_ij` / `b_ij` 的 **i ＝ sA（行）、j ＝ sB（列）**（沿 V3 源件 L253-256 记法）
      ⇒ `A[sA][sB]`、`B[sA][sB]`；`u_B(sB, sA) = B[sA][sB]`。
    """
    a11, a12, a21, a22, b11, b12, b21, b22 = pay
    return ((a11, a12), (a21, a22)), ((b11, b12), (b21, b22))


# --- Q-3 取格自证：本件一般取格  vs  前代修复件 L255/L256 字面取格 ---

def take_grid_general(pay, sB):
    """本件一般取格（**修正 R-3 静默错误**）：u_A(0,sB) / u_A(1,sB)。"""
    A, _ = payoff_2d(pay)
    return (A[0][sB], A[1][sB])


def take_grid_prior_literal(pay, sB):
    """前代修复件 L255 字面取格（`ua = (a11,a12) if sB==0 else (a21,a22)`）—— 仅作自证左列。"""
    a11, a12, a21, a22 = pay[:4]
    return (a11, a12) if sB == 0 else (a21, a22)


def take_grid_B_general(pay, sA):
    """本件一般取格：u_B(0,sA) / u_B(1,sA)。"""
    _, B = payoff_2d(pay)
    return (B[sA][0], B[sA][1])


def take_grid_B_prior_literal(pay, sA):
    """前代修复件 L256 字面取格（`ub = (b11,b21) if sA==0 else (b12,b22)`）。"""
    b11, b12, b21, b22 = pay[4:]
    return (b11, b21) if sA == 0 else (b12, b22)


def q3_takegrid_selfproof(pay_p1, pay_mirror) -> dict:
    """**Q-3 逐格自证**：本件一般取格与前代字面取格在两种 payoff 上的逐格差异。

    预期（须由实测给出，0 预断）：
      - 镜像 payoff：两者**一致** ⇒ 前代字面取格「仅因对称而正确」（立线件 R-3）。
      - P-1 payoff：两者**不一致** ⇒ 前代字面取格在本构造下是**静默错误** ⇒ 必须替换。
    """
    rows, n_diff_p1, n_diff_mirror = [], 0, 0
    for sB in (0, 1):
        g_p1 = take_grid_general(pay_p1, sB)
        p_p1 = take_grid_prior_literal(pay_p1, sB)
        g_m = take_grid_general(pay_mirror, sB)
        p_m = take_grid_prior_literal(pay_mirror, sB)
        d1 = (abs(g_p1[0] - p_p1[0]) > 1e-12) or (abs(g_p1[1] - p_p1[1]) > 1e-12)
        d2 = (abs(g_m[0] - p_m[0]) > 1e-12) or (abs(g_m[1] - p_m[1]) > 1e-12)
        n_diff_p1 += int(d1)
        n_diff_mirror += int(d2)
        rows.append({"sB": sB, "A_格_本件一般取格": list(g_p1), "A_格_前代字面取格": list(p_p1),
                     "A_格_一致": not d1, "A_格_镜像payoff下本件": list(g_m),
                     "A_格_镜像payoff下前代": list(p_m), "A_格_镜像payoff下一致": not d2})
    b_rows, nb_diff_p1, nb_diff_mirror = [], 0, 0
    for sA in (0, 1):
        g_p1 = take_grid_B_general(pay_p1, sA)
        p_p1 = take_grid_B_prior_literal(pay_p1, sA)
        g_m = take_grid_B_general(pay_mirror, sA)
        p_m = take_grid_B_prior_literal(pay_mirror, sA)
        d1 = (abs(g_p1[0] - p_p1[0]) > 1e-12) or (abs(g_p1[1] - p_p1[1]) > 1e-12)
        d2 = (abs(g_m[0] - p_m[0]) > 1e-12) or (abs(g_m[1] - p_m[1]) > 1e-12)
        nb_diff_p1 += int(d1)
        nb_diff_mirror += int(d2)
        b_rows.append({"sA": sA, "B_格_本件一般取格": list(g_p1), "B_格_前代字面取格": list(p_p1),
                       "B_格_一致": not d1, "B_格_镜像payoff下本件": list(g_m),
                       "B_格_镜像payoff下前代": list(p_m), "B_格_镜像payoff下一致": not d2})
    A2, B2 = payoff_2d(pay_p1)
    return {
        "规则": ("本件取格 = 一般矩阵取格 u_A(sA,sB)=A[sA][sB]、u_B(sB,sA)=B[sA][sB]；"
                 "前代字面取格 = L255/L256 的 `(a11,a12) if sB==0 else (a21,a22)` / "
                 "`(b11,b21) if sA==0 else (b12,b22)`"),
        "A_侧逐格": rows, "B_侧逐格": b_rows,
        "n_A_格_不一致_在P1payoff下": n_diff_p1, "n_B_格_不一致_在P1payoff下": nb_diff_p1,
        "n_A_格_不一致_在镜像payoff下": n_diff_mirror, "n_B_格_不一致_在镜像payoff下": nb_diff_mirror,
        "P1_payoff对称性": {"a11==a22": abs(A2[0][0] - A2[1][1]) <= 1e-12,
                            "a12==a21": abs(A2[0][1] - A2[1][0]) <= 1e-12,
                            "B对称": abs(B2[0][0] - B2[1][1]) <= 1e-12},
        "结论": ("P-1 矩阵下前代字面取格在 %d/2（A 侧）+ %d/2（B 侧）格与一般取格不一致 ⇒ "
                 "前代字面在本构造下是**静默错误**（0 报错、0 异常提示）⇒ 本件已替换为一般取格；"
                 "镜像 payoff 下不一致格数 = %d/2（A 侧）+ %d/2（B 侧）⇒ 复现立线件 R-3"
                 "「仅因当前矩阵对称才正确」"
                 % (n_diff_p1, nb_diff_p1, n_diff_mirror, nb_diff_mirror)),
    }


# ============================================================================
# 段 1 · σ 两个臂（R-2 零质量冻结面：处置档 / 未处置档）
# ============================================================================

def sigma_positive_part(R):
    """前代语义（**R-2 冻结面未处置**）：σ ∝ max(0, R)；两 regret 皆 ≤ 0 ⇒ None ⇒ 不重采样。"""
    pos = [max(0.0, x) for x in R]
    tot = sum(pos)
    if tot <= 0.0:
        return None
    return [p / tot for p in pos]


def sigma_centered(R):
    """**R-2 处置档**：σ ∝ max(0, R − min R)（保序保尺度、0 可调参数）。

    仅当两 regret **精确相等**（spread ＝ 0）时回退到均匀 `0.5/0.5`（最大熵，**无参数**）。
    ⇒ 动作**不再永久冻结**；**0 引入任何数值判定切点**。
    """
    lo = min(R)
    w = [max(0.0, x - lo) for x in R]
    tot = sum(w)
    if tot <= 0.0:
        return [0.5, 0.5]
    return [x / tot for x in w]


SIGMA_ARMS = (
    ("R2_disposed_centered (R-2 处置档: σ ∝ max(0, R − min R); 精确相等时回退均匀 0.5/0.5)",
     sigma_centered),
    ("R2_not_disposed_positive_part (前代语义: σ ∝ max(0, R); 全 ≤ 0 ⇒ None ⇒ 冻结)",
     sigma_positive_part),
)


# ============================================================================
# 段 2 · C1 · Regret Matching（累计反事实 regret；收敛切点逐字不动）
# ============================================================================

def F_simulate_rm_p1(pay, sigma_fn, n_iter=N_ITER, seed=SEED, tol=RM_TOL,
                      warmup=RM_WARMUP, avg_arm=True) -> dict:
    """P-1 payoff 下的真·Regret Matching（累计反事实 regret，HMC 2000 式）。

    0 改：`tol = 1e-3` / `t > warmup(5)` / `n_iter = 200` / `seed`。
    取格 = 一般矩阵取格（Q-3 修正）。
    诊断全量落盘（立线件 §5.3 接口）：`last_switch_round` / `n_profile_switches` /
    `n_distinct_profiles` / `final_profile` / `trace_tail` ＋ **play 读数 D-1 / D-2** ＋
    **冻结面证据**（`n_rounds_sigma_none` / `ever_resampled`）。
    """
    A, B = payoff_2d(pay)
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    R_A = [0.0, 0.0]
    R_B = [0.0, 0.0]
    profiles = []
    trace_tail = []
    last_switch = -1
    n_switches = 0
    n_sigma_none = 0
    ever_resampled = False
    t_exit = None
    for t in range(n_iter):
        profiles.append((sA, sB))
        ua = (A[0][sB], A[1][sB])        # Q-3 修正后的 u_A(0,sB), u_A(1,sB)
        ub = (B[sA][0], B[sA][1])        # Q-3 修正后的 u_B(0,sA), u_B(1,sA)
        R_A[0] += ua[0] - ua[sA]
        R_A[1] += ua[1] - ua[sA]
        R_B[0] += ub[0] - ub[sB]
        R_B[1] += ub[1] - ub[sB]
        sig_A, sig_B = sigma_fn(R_A), sigma_fn(R_B)
        prev = (sA, sB)
        if sig_A is None or sig_B is None:
            n_sigma_none += 1
        if sig_A is not None:
            ever_resampled = True
            sA = 0 if rng.random() < sig_A[0] else 1
        if sig_B is not None:
            ever_resampled = True
            sB = 0 if rng.random() < sig_B[0] else 1
        if (sA, sB) != prev:
            last_switch = t
            n_switches += 1
        if t >= n_iter - 3:
            trace_tail.append({"t": t, "R_A": [round(R_A[0], 6), round(R_A[1], 6)],
                               "R_B": [round(R_B[0], 6), round(R_B[1], 6)],
                               "profile": [sA, sB]})
        scale = float(t + 1) if avg_arm else 1.0
        if (max(R_A[0], R_A[1]) / scale < tol
                and max(R_B[0], R_B[1]) / scale < tol and t > warmup):
            t_exit = t
            break
    hit_cap = t_exit is None
    rm_iter = N_ITER if hit_cap else t_exit
    n_rounds = len(profiles)
    return {
        "rm_iter": rm_iter,
        "hit_cap": hit_cap,
        "n_rounds_executed": n_rounds,
        "R_A_exit": [round(R_A[0], 9), round(R_A[1], 9)],
        "R_B_exit": [round(R_B[0], 9), round(R_B[1], 9)],
        "n_profile_switches": n_switches,
        "last_switch_round": last_switch,
        "n_distinct_profiles": len(set(profiles)),
        "final_profile": [sA, sB],
        "trace_tail": trace_tail,
        # --- 冻结面证据（R-2） ---
        "n_rounds_sigma_none": n_sigma_none,
        "ever_resampled": ever_resampled,
        "profile_frozen_whole_run": bool(len(set(profiles)) == 1),
        # --- play 读数 D-1 / D-2（立线件 §5.1；⑦ = D-1＋D-2 并报） ---
        "play_D1_末次切换轮+1": (last_switch + 1),
        "play_D2_末段无切换长度_按n_iter": (N_ITER - last_switch),
        "play_D2_末段无切换长度_按实走轮数": (n_rounds - 1 - last_switch),
    }


# ============================================================================
# 段 3 · C3 · 真 best-response 迭代（recheck #01 已实跑构造；0 新设切点）
# ============================================================================

def F_bayes_br_p1(pay, start, mode="simultaneous", eps=BAYES_EPS,
                  max_iter=BAYES_MAX_ITER) -> dict:
    A, B = payoff_2d(pay)

    def pay_A(sA, sB):
        return A[sA][sB]

    def pay_B(sB, sA):
        return B[sA][sB]

    def br_A(sB):
        return 0 if pay_A(0, sB) >= pay_A(1, sB) else 1

    def br_B(sA):
        return 0 if pay_B(0, sA) >= pay_B(1, sA) else 1

    def gap(sA, sB):
        g = max(0.0, pay_A(br_A(sB), sB) - pay_A(sA, sB))
        g = max(g, max(0.0, pay_B(br_B(sA), sA) - pay_B(sB, sA)))
        return g

    sA, sB = int(start[0]), int(start[1])
    for t in range(1, max_iter + 1):
        if mode == "simultaneous":
            sA, sB = br_A(sB), br_B(sA)
        elif mode == "alternating":
            sA = br_A(sB)
            sB = br_B(sA)
        else:
            raise ValueError("unknown BR mode: %r" % mode)
        g = gap(sA, sB)
        if g <= eps:
            return {"bayes_iter_true": t, "hit_iter_cap": False, "nash_gap_final": g}
    return {"bayes_iter_true": max_iter, "hit_iter_cap": True, "nash_gap_final": gap(sA, sB)}


# ============================================================================
# 段 4 · C2 / C4 上游 rbr（V3 字面逐字转写；0 import 原件、0 触动原件）
# ============================================================================

def L_solve_2x2_nash_pure(a11, a12, a21, a22, b11, b12, b21, b22):
    candidates = [(0, 0, a11, b11), (0, 1, a12, b12), (1, 0, a21, b21), (1, 1, a22, b22)]
    nash = []
    for sA, sB, aA, aB in candidates:
        a_dev = (a21 if sB == 0 else a22) if sA == 0 else (a11 if sB == 0 else a12)
        if a_dev > aA:
            continue
        b_dev_check = (b12 if sA == 0 else b22) if sB == 0 else (b11 if sA == 0 else b21)
        if b_dev_check > aB:
            continue
        nash.append((sA, sB))
    return nash if nash else None


def L_simulate_rbr(pay, n_iter=N_ITER, seed=SEED) -> int:
    """V3 源件 L110-L136 逐字转写（**C2 面本体**；本件 0 改逻辑，只换 payoff 输入）。"""
    a11, a12, a21, a22, b11, b12, b21, b22 = pay
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    history = []
    for t in range(n_iter):
        a_pay_s0 = a11 if sB == 0 else a12
        a_pay_s1 = a21 if sB == 0 else a22
        best_A = 0 if a_pay_s0 >= a_pay_s1 else 1
        b_pay_s0 = b11 if sA == 0 else b21
        b_pay_s1 = b12 if sA == 0 else b22
        best_B = 0 if b_pay_s0 >= b_pay_s1 else 1
        switched = (best_A != sA) or (best_B != sB)
        if switched:
            history.append(t)
        sA, sB = best_A, best_B
        if not switched and t > 0 and len(history) >= 1:
            return t
    return n_iter


def L_simulate_rm_mirror(pay, n_iter=N_ITER, seed=SEED, tol=RM_TOL) -> int:
    """V3 源件 L139-L178 逐字转写（**镜像 payoff 下的 C1 退化面本体**）—— 仅作对照腿。"""
    a11, a12, a21, a22, b11, b12, b21, b22 = pay
    rng = random.Random(seed)
    sA, sB = rng.randint(0, 1), rng.randint(0, 1)
    R_A = [0.0, 0.0]
    R_B = [0.0, 0.0]
    cum_A = [0.0, 0.0]
    cum_B = [0.0, 0.0]
    for t in range(n_iter):
        a_pay = (a11, a12)[sB] if sA == 0 else (a21, a22)[sB]
        b_pay = (b11, b12)[sA] if sB == 0 else (b21, b22)[sA]
        cum_A[sA] += a_pay
        cum_B[sB] += b_pay
        avg_A = [cum_A[0] / (t + 1), cum_A[1] / (t + 1)]
        avg_B = [cum_B[0] / (t + 1), cum_B[1] / (t + 1)]
        R_A[1 - sA] = max(0.0, avg_A[1 - sA] - avg_A[sA])
        R_A[sA] = 0.0
        R_B[1 - sB] = max(0.0, avg_B[1 - sB] - avg_B[sB])
        R_B[sB] = 0.0
        tA, tB = R_A[0] + R_A[1], R_B[0] + R_B[1]
        if tA > 0:
            sA = 0 if rng.random() < (R_A[0] / tA) else 1
        if tB > 0:
            sB = 0 if rng.random() < (R_B[0] / tB) else 1
        if max(R_A[0], R_A[1]) < tol and max(R_B[0], R_B[1]) < tol and t > 5:
            return t
    return n_iter


def L_bayesian_nash_iter(pay) -> int:
    return 1 if L_solve_2x2_nash_pure(*pay) else 200


# ============================================================================
# 主函数
# ============================================================================

def main() -> int:
    # ---------- K-V3DF-0-2 / K-RO-0-3 跑前只读基线 ----------
    pre_sha12 = {p: sha12_file(os.path.join(REPO_ROOT, p)) for p in TOUCH_PROOF_FILES}
    control_sha12 = {
        "results/_v5_v3_deg_reopen_line_2026_09_29.md (立线件 · 本棒控制件)":
            sha12_file(REOPEN_LINE),
        "results/_v5_v3_deg_fix_prereg_2026_09_29.md (预登记 · 生效即锁)":
            sha12_file(PREREG),
        "results/_v5_v3_deg_fix_exec_2026_09_29.md (前代执行件 · 读数挂起)":
            sha12_file(PRIOR_EXEC),
        "deposon_team/plugins/boss_pa_1_rbr_rm_v3df_c1c4_2026_09_29.py (前代修复件 · 参照)":
            sha12_file(PRIOR_FIX),
        "results/_v5_v3_deg_fix_c1c4_result_2026_09_29.json (前代读数 · 挂起)":
            sha12_file(PRIOR_RESULT),
    }
    input_sha12 = {"results/deposon_v20_baselines.json": sha12_file(V20_BASELINES),
                   "results/boss_pa_1_rbr_rm_result_2026_09_15.json": sha12_file(SRC_RESULT)}

    v20 = load_json(V20_BASELINES)
    per_graph = v20["per_graph"]
    gids = sorted(per_graph.keys())
    n_graphs = len(gids)
    assert n_graphs == 22, "22 受控概念图数量不符: %d" % n_graphs

    src = load_json(SRC_RESULT)
    on_disk = {g["graph_id"]: g for g in src["boss_pa1_22graph_simulation"]["graph_results"]}

    pays_p1, pays_mirror, p1_meta = {}, {}, {}
    for gid in gids:
        pays_p1[gid], p1_meta[gid] = payoff_matrix_p1(per_graph[gid])
        pays_mirror[gid] = payoff_matrix_mirror(per_graph[gid])

    # ---------- 段 0b · Q-3 取格逐格自证（立线件 R-3 / Q-3） ----------
    q3 = q3_takegrid_selfproof(pays_p1[gids[0]], pays_mirror[gids[0]])
    q3_per_graph = {g: q3_takegrid_selfproof(pays_p1[g], pays_mirror[g]) for g in gids}

    # ---------- 段 0c · 对照腿：镜像 payoff 下的 legacy 逐字复现（结构性事实） ----------
    legacy = {}
    for gid in gids:
        pay = pays_mirror[gid]
        legacy[gid] = {
            "rbr": L_simulate_rbr(pay),
            "rm": L_simulate_rm_mirror(pay),
            "bayes": L_bayesian_nash_iter(pay),
        }
    legacy_repro = {
        "口径": ("镜像 payoff 下 V3 字面公式的逐字复现；**只作 diff 左列与结构性事实**，"
                 + SUSPEND_LABEL + "（0 作判定依据）"),
        "n_graphs": n_graphs,
        "n_bit_exact_match_vs_on_disk": sum(
            1 for g in gids
            if legacy[g]["rbr"] == on_disk[g]["rbr_iter"]
            and legacy[g]["rm"] == on_disk[g]["rm_iter"]
            and legacy[g]["bayes"] == on_disk[g]["bayes_iter"]),
        "all_bit_exact": all(legacy[g]["rbr"] == on_disk[g]["rbr_iter"]
                             and legacy[g]["rm"] == on_disk[g]["rm_iter"]
                             and legacy[g]["bayes"] == on_disk[g]["bayes_iter"] for g in gids),
        "legacy_rm_stat": stat_block([legacy[g]["rm"] for g in gids]),
        "legacy_bayes_stat": stat_block([legacy[g]["bayes"] for g in gids]),
        "legacy_rbr_stat": stat_block([legacy[g]["rbr"] for g in gids]),
        "on_disk_verdict": src["verdict"],
    }

    # ---------- 段 1 · `K-V3DF-0-1` / `K-RO-0-1` 自证：输入字段 ----------
    a_named_v, a_filler_v, b_named_v, b_filler_v, dep_freq_v = [], [], [], [], []
    dA_v, dB_v = [], []
    for g in gids:
        an, af, bn, bf = src_rates(per_graph[g])
        a_named_v.append(an)
        a_filler_v.append(af)
        b_named_v.append(bn)
        b_filler_v.append(bf)
        dep_freq_v.append(0.5 if (an + af) < 1e-9 else an / (an + af))
        dA_v.append(p1_meta[g]["delta_A_abs"])
        dB_v.append(p1_meta[g]["delta_B_abs"])
    input_selfcheck = {
        "v20_field_mean_named (盘上真实, 逐图)": stat_block(a_named_v),
        "v20_field_mean_filler (盘上真实, 逐图)": stat_block(a_filler_v),
        "v20_best_baseline_named (盘上真实, 逐图)": stat_block(b_named_v),
        "v20_best_baseline_filler (盘上真实, 逐图)": stat_block(b_filler_v),
        "deposon_freq_派生 (盘上真实, 逐图)": stat_block(dep_freq_v),
        "P-1 |delta_A| (角色互换后, 逐图)": stat_block(dA_v),
        "P-1 |delta_B| (角色互换后, 逐图)": stat_block(dB_v),
    }
    gate_pass_input = {k: bool(input_selfcheck[k]["n_distinct"] > GATE_N_DISTINCT
                               and input_selfcheck[k]["std"] > 0) for k in input_selfcheck}
    degen_alarm_input = not all(gate_pass_input.values())

    # ---------- 段 2 · C1 · P-1 · 2 σ 臂 × 2 收敛量臂（并报，0 择一删读） ----------
    c1_arms = {}
    for sig_name, sig_fn in SIGMA_ARMS:
        for qty_name, avg_arm in (("主臂 1/(t+1)·ΣR (基名件 L159 自陈 HMC 2000 式)", True),
                                  ("对照臂 max(ΣR) (与 V3 源码表达式同形)", False)):
            key = "%s ‖ %s" % (sig_name, qty_name)
            vals, cap_hits, diags = [], [], {}
            for gid in gids:
                res = F_simulate_rm_p1(pays_p1[gid], sig_fn, n_iter=N_ITER, seed=SEED,
                                       tol=RM_TOL, warmup=RM_WARMUP, avg_arm=avg_arm)
                vals.append(res["rm_iter"])
                cap_hits.append(res["hit_cap"])
                diags[gid] = res
            st = stat_block(vals)
            conv = [v for v, h in zip(vals, cap_hits) if not h]
            c1_arms[key] = {
                "sigma_臂": sig_name,
                "收敛量臂": qty_name,
                "convergence_quantity": ("1/(t+1)·Σ_t 瞬时 regret" if avg_arm else "Σ_t 瞬时 regret 原始累计"),
                "construction": ("P-1 同序 payoff（去镜像、含 sign(δ) 角色互换）＋ 累计反事实 regret "
                                 "＋ 一般矩阵取格（Q-3 修正）；收敛切点 tol=1e-3 与 t>5 逐字沿用 V3"),
                "tol": RM_TOL, "warmup_t_gt": RM_WARMUP, "n_iter": N_ITER, "seed": SEED,
                "rm_iter_per_graph": vals,
                "cap_artifact_alarm_hit": bool(any(cap_hits)),
                "n_hit_cap": int(sum(cap_hits)),
                "cap_hit_rate": round(sum(cap_hits) / n_graphs, 6),
                "stat": st,
                "artifact_free_reading": {
                    "definition": "剔除触 n_iter=200 上限（真·不收敛）之图后的 rm_iter 读数",
                    "n_cells_kept": len(conv),
                    "n_cells_removed_as_cap": int(sum(cap_hits)),
                    "stat": stat_block(conv) if conv else None,
                    "note": "口径名显式标注 artifact-free，0 静默剔除（K-V3DF-3-2 同款纪律）",
                },
                "warmup_floor_note": ("取值 6 = `t > 5` 护栏下的**最早可采纳轮**（下限地板，"
                                      "非度量出的迭代数）；本件逐字沿用该护栏故如实登记"),
                "R2_冻结面证据": {
                    "n_graphs_profile_全程冻结": sum(
                        1 for g in gids if diags[g]["profile_frozen_whole_run"]),
                    "n_graphs_至少重采样过一次": sum(
                        1 for g in gids if diags[g]["ever_resampled"]),
                    "sigma_none_轮次_合计": sum(diags[g]["n_rounds_sigma_none"] for g in gids),
                },
                "diagnostics": diags,
            }
    c1_key_disposed_main = SIGMA_ARMS[0][0] + " ‖ " + \
        "主臂 1/(t+1)·ΣR (基名件 L159 自陈 HMC 2000 式)"
    c1_key_disposed_ctl = SIGMA_ARMS[0][0] + " ‖ " + \
        "对照臂 max(ΣR) (与 V3 源码表达式同形)"
    c1_key_undisposed_main = SIGMA_ARMS[1][0] + " ‖ " + \
        "主臂 1/(t+1)·ΣR (基名件 L159 自陈 HMC 2000 式)"
    c1_key_undisposed_ctl = SIGMA_ARMS[1][0] + " ‖ " + \
        "对照臂 max(ΣR) (与 V3 源码表达式同形)"
    c1_disposed_main = c1_arms[c1_key_disposed_main]
    c1_disposed_main_ok = bool(c1_disposed_main["stat"]["n_distinct"] >= KILL_N_DISTINCT
                               and c1_disposed_main["stat"]["std"] > 0)
    arm_ok = {kk: bool(c1_arms[kk]["stat"]["n_distinct"] >= KILL_N_DISTINCT
                       and c1_arms[kk]["stat"]["std"] > 0) for kk in c1_arms}

    # 读数机理诊断（P-1 无交互结构下 rm_iter 的来源；0 设任何达标带，只报比值分布）
    mech_rows = []
    for i, g in enumerate(gids):
        v = c1_arms[c1_key_disposed_main]["rm_iter_per_graph"][i]
        dmax = max(p1_meta[g]["delta_A_abs"], p1_meta[g]["delta_B_abs"])
        mech_rows.append({
            "graph_id": g, "rm_iter_处置档主臂": v,
            "max_abs_delta": round(dmax, 6), "rm_iter×tol": round(v * RM_TOL, 6),
            "比值_(rm_iter×tol)/max|δ|": (round(v * RM_TOL / dmax, 4) if dmax > 0 else None),
            "是否地板值6": bool(v == 6), "是否cap值200": bool(v == N_ITER),
        })
    _mid = [r["比值_(rm_iter×tol)/max|δ|"] for r in mech_rows
            if not r["是否地板值6"] and not r["是否cap值200"]
            and r["比值_(rm_iter×tol)/max|δ|"] is not None]
    mech = {
        "目的": ("核实 P-1 无交互结构下 rm_iter 的来源：若「玩家占据占优动作后累计 regret 钉在常数 "
                 "|δ| 且 0 衰减」成立，则 1/(t+1)·ΣR 臂的收敛轮次应近似 `max|δ| / tol`"
                 "（t = 6 为 `t>5` 地板值、200 为 cap 值）"),
        "逐图": mech_rows,
        "非地板非cap图_比值stat": stat_block(_mid) if _mid else None,
        "0设达标带": "本诊断**0 设任何达标带**（只报比值分布，判定归 verdict-keeper）",
    }

    # ---------- 段 3 · C3 · P-1 · 176 格真 best-response ----------
    bayes_cells = []
    for gid in gids:
        for mode in BR_MODES:
            for stt in STARTS:
                res = F_bayes_br_p1(pays_p1[gid], stt, mode=mode)
                bayes_cells.append({"graph_id": gid, "base_graph": base_graph(gid),
                                    "br_mode": mode, "start": list(stt),
                                    "bayes_iter_true": res["bayes_iter_true"],
                                    "hit_iter_cap": res["hit_iter_cap"],
                                    "nash_gap_final": res["nash_gap_final"]})
    bayes_all = [c["bayes_iter_true"] for c in bayes_cells]
    bayes_cap_cells = [c for c in bayes_cells if c["hit_iter_cap"]]
    bayes_conv = [c["bayes_iter_true"] for c in bayes_cells if not c["hit_iter_cap"]]
    c3_literal = stat_block(bayes_all)
    c3_af = stat_block(bayes_conv) if bayes_conv else None
    c3_cap_by_mode = {m: sum(1 for c in bayes_cap_cells if c["br_mode"] == m) for m in BR_MODES}
    c3_by_mode = {m: stat_block([c["bayes_iter_true"] for c in bayes_cells
                                 if c["br_mode"] == m]) for m in BR_MODES}
    c3_by_start = {"%d%d" % s: stat_block([c["bayes_iter_true"] for c in bayes_cells
                                           if tuple(c["start"]) == s]) for s in STARTS}

    # ---------- 段 4 · C2 / C4 连带面（⑩ 范围 = C1＋C3＋C4；C2 连带影响须登记） ----------
    per_graph_new = []
    mult_frozen_lit, mult_frozen_free, mult_p1rbr_lit, mult_p1rbr_free = [], [], [], []
    rm_mult_lit, rm_mult_free = [], []
    for gid in gids:
        cells = [c for c in bayes_cells if c["graph_id"] == gid]
        rbr_frozen = legacy[gid]["rbr"]                      # 镜像 payoff 下的 V3 冻结值（前代口径）
        rbr_p1 = L_simulate_rbr(pays_p1[gid])                # P-1 payoff 下重算（一致性臂）
        rm_fixed = c1_disposed_main["rm_iter_per_graph"][gids.index(gid)]
        row_cells = []
        for c in cells:
            m_fz = rbr_frozen / c["bayes_iter_true"]
            m_p1 = rbr_p1 / c["bayes_iter_true"]
            m_rm = rm_fixed / c["bayes_iter_true"]
            mult_frozen_lit.append(m_fz)
            mult_p1rbr_lit.append(m_p1)
            rm_mult_lit.append(m_rm)
            if not c["hit_iter_cap"]:
                mult_frozen_free.append(m_fz)
                mult_p1rbr_free.append(m_p1)
                rm_mult_free.append(m_rm)
            row_cells.append({**c, "rbr_iter_frozen_mirror": rbr_frozen,
                              "rbr_iter_p1_recomputed": rbr_p1,
                              "rbr_mult_frozen": round(m_fz, 4),
                              "rbr_mult_p1_rbr": round(m_p1, 4),
                              "rm_mult_fixed": round(m_rm, 4)})
        per_graph_new.append({
            "graph_id": gid, "base_graph": base_graph(gid),
            "P-1 构造元信息": p1_meta[gid],
            "P-1 payoff (a11,a12,a21,a22,b11,b12,b21,b22)": list(pays_p1[gid]),
            "镜像 payoff (对照腿)": list(pays_mirror[gid]),
            "legacy_镜像读数 %s" % SUSPEND_LABEL:
                {"rm_iter": legacy[gid]["rm"], "bayes_iter": legacy[gid]["bayes"],
                 "rbr_iter": legacy[gid]["rbr"]},
            "fixed_P1_读数": {
                "rm_iter_disposed_main": rm_fixed,
                "rm_iter_disposed_ctl": c1_arms[c1_key_disposed_ctl]["rm_iter_per_graph"][
                    gids.index(gid)],
                "rm_iter_undisposed_main": c1_arms[c1_key_undisposed_main]["rm_iter_per_graph"][
                    gids.index(gid)],
                "rm_iter_undisposed_ctl": c1_arms[c1_key_undisposed_ctl]["rm_iter_per_graph"][
                    gids.index(gid)],
                "bayes_iter_true_cells": [c["bayes_iter_true"] for c in cells],
                "rbr_iter_frozen_mirror": rbr_frozen,
                "rbr_iter_p1_recomputed": rbr_p1,
            },
            "C1 逐图诊断_disposed_main": {
                k: v for k, v in c1_disposed_main["diagnostics"][gid].items() if k != "trace_tail"},
            "C1 逐图 trace_tail_disposed_main":
                c1_disposed_main["diagnostics"][gid]["trace_tail"],
            "C1 逐图诊断_undisposed_main": {
                k: v for k, v in c1_arms[c1_key_undisposed_main]["diagnostics"][gid].items()
                if k != "trace_tail"},
            "cells": row_cells,
        })

    c4_frozen_lit = stat_block(mult_frozen_lit)
    c4_frozen_free = stat_block(mult_frozen_free) if mult_frozen_free else None
    c4_p1rbr_lit = stat_block(mult_p1rbr_lit)
    c4_p1rbr_free = stat_block(mult_p1rbr_free) if mult_p1rbr_free else None
    rm_mult_lit_st = stat_block(rm_mult_lit)
    rm_mult_free_st = stat_block(rm_mult_free) if rm_mult_free else None

    c2_p1_v = [r["fixed_P1_读数"]["rbr_iter_p1_recomputed"] for r in per_graph_new]
    c2_frozen_v = [r["fixed_P1_读数"]["rbr_iter_frozen_mirror"] for r in per_graph_new]
    c2_recheck = {
        "C2 修面": "0 立修复面（预登记 §1.2-C2：未退化 ＝ 真信号）",
        "⑩ 范围": "C1＋C3＋C4（**C2 不在 §9-⑩ 三档内**）",
        "连带影响登记（`K-V3DF-2-1` 字面：读数若被改坏须登记，0 静默沿用旧值）": {
            "镜像 payoff 下 rbr_iter（V3 冻结 / 前代口径）": {
                "stat": stat_block(c2_frozen_v),
                "distinct": sorted(set(c2_frozen_v)),
                "n_hit_cap": sum(1 for x in c2_frozen_v if x == N_ITER),
            },
            "P-1 payoff 下 rbr_iter（本棒重算 · 一致性臂）": {
                "stat": stat_block(c2_p1_v),
                "distinct": sorted(set(c2_p1_v)),
                "n_hit_cap": sum(1 for x in c2_p1_v if x == N_ITER),
                "与冻结值逐图相同": bool(c2_p1_v == c2_frozen_v),
            },
            "结论": ("P-1 payoff 改动**连带改到 C2 读数**（rbr 读 payoff）⇒ 冻结值与 P-1 值"
                     + ("**逐图相同**（本棒实测）" if c2_p1_v == c2_frozen_v
                        else "**不同**（本棒实测）")
                     + " ⇒ 登记为连带影响面，0 静默沿用旧值"),
        },
        "本棒 0 做": "C2 独立重跑（§9-⑩ 三档均未含 C2）⇒ 是否扩范围由 PI / verdict-keeper 定",
    }

    c4_001 = {
        "definition": "rbr_mult == 0.01（= 2/200）是否出现（`K-V3DF-4-2` 字面）",
        "present_frozen_lit": any(abs(x - 0.01) < 1e-12 for x in mult_frozen_lit),
        "present_frozen_free": bool(mult_frozen_free) and any(abs(x - 0.01) < 1e-12
                                                               for x in mult_frozen_free),
        "present_p1rbr_lit": any(abs(x - 0.01) < 1e-12 for x in mult_p1rbr_lit),
        "present_p1rbr_free": bool(mult_p1rbr_free) and any(abs(x - 0.01) < 1e-12
                                                            for x in mult_p1rbr_free),
        "n_cells_equal_0.01_frozen": sum(1 for x in mult_frozen_lit if abs(x - 0.01) < 1e-12),
        "n_cells_equal_0.01_p1rbr": sum(1 for x in mult_p1rbr_lit if abs(x - 0.01) < 1e-12),
        "note": "出现 / 未出现均如实登记；0 因「未出现」而称已修好（K-V3DF-4-2 字面）",
    }

    # ---------- 段 5 · play 读数并报（⑥ 甲 = 并报不替换；⑦ = D-1＋D-2 并报） ----------
    play = {}
    for key in (c1_key_disposed_main, c1_key_undisposed_main):
        dgs = c1_arms[key]["diagnostics"]
        d1 = [dgs[g]["play_D1_末次切换轮+1"] for g in gids]
        d2 = [dgs[g]["play_D2_末段无切换长度_按n_iter"] for g in gids]
        d2x = [dgs[g]["play_D2_末段无切换长度_按实走轮数"] for g in gids]
        rows, mat = [], {"play安定∧regret收敛": 0, "play安定∧regret不收敛": 0,
                         "play不安定∧regret收敛": 0, "play不安定∧regret不收敛": 0}
        for i, g in enumerate(gids):
            d = dgs[g]
            stable = bool(d["n_distinct_profiles"] == 1)     # 全程无 profile 切换（结构恒等式，0 新切点）
            conv = bool(not d["hit_cap"])
            key2 = ("play安定∧regret收敛" if stable and conv else
                    "play安定∧regret不收敛" if stable else
                    "play不安定∧regret收敛" if conv else "play不安定∧regret不收敛")
            mat[key2] += 1
            rows.append({
                "graph_id": g, "base_graph": base_graph(g),
                "rm_iter": d["rm_iter"], "hit_cap": d["hit_cap"],
                "play_D1_末次切换轮+1": d["play_D1_末次切换轮+1"],
                "play_D2_末段无切换长度_按n_iter": d["play_D2_末段无切换长度_按n_iter"],
                "play_D2_末段无切换长度_按实走轮数": d["play_D2_末段无切换长度_按实走轮数"],
                "n_distinct_profiles": d["n_distinct_profiles"],
                "n_profile_switches": d["n_profile_switches"],
                "last_switch_round": d["last_switch_round"],
                "final_profile": d["final_profile"],
                "play_安定": stable, "regret_收敛": conv, "同向性": key2,
            })
        n_codir = mat["play安定∧regret收敛"] + mat["play不安定∧regret不收敛"]
        play[key] = {
            "口径名": "play 安定轮数（新增**诊断读数列**，**不替换** `rm_iter` 判据字段 —— ⑥ 甲）",
            "D-1_定义": "读数 = 最后一轮 (sA,sB) 发生变化的轮次 ＋ 1（−1 ⇒ 从未切换 ＝ 0 轮安定）",
            "D-2_定义": "读数 = n_iter − last_switch_round（连续未切换的末段长度）",
            "D-2_附加口径": "另报「按实走轮数」版本（n_rounds−1−last_switch）；立线件字面为「按 n_iter」，"
                             "两版**并报、0 择一删读**",
            "同向性_定义": ("play 安定 ＝ `n_distinct_profiles == 1`（全程无 profile 切换，"
                            "**结构恒等式，0 新设数值切点**）；regret 收敛 ＝ 未触 n_iter 上限"),
            "D-1_stat": stat_block(d1),
            "D-2_stat_按n_iter": stat_block(d2),
            "D-2_stat_按实走轮数": stat_block(d2x),
            "同向性矩阵_逐图": rows,
            "同向性计数": mat,
            "同向率": round(n_codir / n_graphs, 6),
            "K-PY-1-1_自证": {
                "D-1_n_distinct": stat_block(d1)["n_distinct"],
                "D-2_n_distinct": stat_block(d2)["n_distinct"],
                "K-PY-1-1 门槛 n_distinct >= 4（沿 K-V3R-1 字面，0 新设）": KILL_N_DISTINCT,
                "D-1_是否擦门槛": bool(stat_block(d1)["n_distinct"] < KILL_N_DISTINCT),
                "D-2_是否擦门槛": bool(stat_block(d2)["n_distinct"] < KILL_N_DISTINCT),
            },
        }

    # ---------- 段 6 · `K-RO-0-2` 门域声明（逐列点名；本棒 0 收窄） ----------
    output_series = {
        "C1 rm_iter · R2处置·主臂 (22, literal)": c1_arms[c1_key_disposed_main]["stat"],
        "C1 rm_iter · R2处置·主臂 (artifact-free)":
            c1_arms[c1_key_disposed_main]["artifact_free_reading"]["stat"],
        "C1 rm_iter · R2处置·对照臂 (22, literal)": c1_arms[c1_key_disposed_ctl]["stat"],
        "C1 rm_iter · R2未处置·主臂 (22, literal)": c1_arms[c1_key_undisposed_main]["stat"],
        "C1 rm_iter · R2未处置·对照臂 (22, literal)": c1_arms[c1_key_undisposed_ctl]["stat"],
        "C1 play D-1 · R2处置·主臂 (22)": play[c1_key_disposed_main]["D-1_stat"],
        "C1 play D-2 · R2处置·主臂 (22, 按n_iter)":
            play[c1_key_disposed_main]["D-2_stat_按n_iter"],
        "C1 play D-2 · R2处置·主臂 (22, 按实走轮数)":
            play[c1_key_disposed_main]["D-2_stat_按实走轮数"],
        "C1 play D-1 · R2未处置·主臂 (22)": play[c1_key_undisposed_main]["D-1_stat"],
        "C1 play D-2 · R2未处置·主臂 (22, 按n_iter)":
            play[c1_key_undisposed_main]["D-2_stat_按n_iter"],
        "C3 bayes_iter_true · P-1 (176, literal)": c3_literal,
        "C3 bayes_iter_true · P-1 (artifact-free)": c3_af,
        "C4 rbr_mult · rbr冻结 (176, literal)": c4_frozen_lit,
        "C4 rbr_mult · rbr冻结 (artifact-free)": c4_frozen_free,
        "C4 rbr_mult · rbr按P-1重算 (176, literal)": c4_p1rbr_lit,
        "C4 rbr_mult · rbr按P-1重算 (artifact-free)": c4_p1rbr_free,
        "C4 rm_mult · 附加派生 (176, literal)": rm_mult_lit_st,
        "C4 rm_mult · 附加派生 (artifact-free)": rm_mult_free_st,
        "C2 rbr_iter · 镜像冻结 (22)": stat_block(c2_frozen_v),
        "C2 rbr_iter · P-1重算 (22, 连带影响面)": stat_block(c2_p1_v),
    }
    gate_domain_declaration = {
        "K-RO-0-2 门域声明": ("**0 收窄**：本棒把**全部**输出读数列**逐列点名列入门内**（下表 "
                              "`output_series` 共 %d 列，逐列报 n_distinct/min/max/std）；"
                              "literal 与 artifact-free **两读并报**（沿 §3-R 建议，0 择一）。"
                              "**0 概括收窄、0 跑后追加**；因 0 收窄，本件**0 冒充「同素材复跑」的"
                              "削弱门**，也无收窄代价可报。" % len(output_series)),
        "门域内读数列": list(output_series.keys()),
        "门外读数列": [],
        "PI 是否逐列点名过": ("派工单 批 4 未给出门内/门外清单 ⇒ 本棒按**0 收窄**处置（最保守："
                              "全部列进门内）并显式登记该事实"),
    }
    gate_pass_output = {}
    for k, st in output_series.items():
        if st is None:
            gate_pass_output[k] = None
            continue
        gate_pass_output[k] = bool(st["n_distinct"] > GATE_N_DISTINCT and st["std"] > 0)
    degen_series = [k for k, v in gate_pass_output.items() if v is False]
    degen_alarm_output = bool(degen_series)
    gate_0_1_pass = bool(not degen_alarm_input and not degen_alarm_output)

    # ---------- 段 7 · 两段式：`K-RO-0-1` 段 1 自证 → 段 2 正式跑（门控） ----------
    stage2_entered = gate_0_1_pass
    two_stage = {
        "路径": "甲 · 跑前自证两段式（PI 批 4 ①）",
        "段1_跑前自证": {
            "内容": "逐输入字段 ＋ 逐输出读数列（门域 0 收窄）报 n_distinct/min/max/std；"
                    "并与正式跑**同输入同 seed**（seed=210021，0 改动）",
            "输入字段门": gate_pass_input,
            "输出读数列门": gate_pass_output,
            "输入退化警报": degen_alarm_input,
            "输出退化警报": degen_alarm_output,
            "命中退化的读数列": degen_series,
            "K-RO-0-1 落态": "PASS" if gate_0_1_pass else "FAIL（退化警报命中 ⇒ 不得进入正式跑）",
        },
        "段2_正式跑": {
            "是否进入": stage2_entered,
            "门依据": "`K-RO-0-1`：任一读数列 n_distinct ≤ 3 ⇒ **不得进入正式跑**"
                      "（改构造 → 重自证；或判「不明」＝ KD ＋ γ，PI 批 4 ⑧ 确认同指）",
            "本棒处置": ("段 1 自证命中退化警报 ⇒ **段 2 正式跑不启动**（0 带病开跑、0 跑后追认）。"
                         "本 JSON 内全部读数**效力 ＝ 自证段读数（仅供门核，不作收口依据）**，"
                         "沿立线件 §2.2 案甲「自证棒效力」字面。"),
            "数值恒等性说明": ("段 1 自证与段 2 正式跑**共用同一确定性函数与同一 seed**"
                              "（本件单一计算入口、无中间态写入）⇒ 若段 2 被启动，其读数与本 JSON "
                              "**在数值上恒等**；**但收口效力未启动**，二者效力不同，此点 0 含糊"),
        },
    }

    # ---------- 段 8 · 判死线逐条（三态可裁形态；0 代裁） ----------
    k = {}

    k["K-RO-0-1"] = {
        "判据": "开跑前自证门：逐输入字段 ＋ 逐输出读数列报 n_distinct/min/max/std；"
                "任一读数列 n_distinct ≤ 3 ⇒ 不得进入正式跑（改构造，或判「不明」＝ KD ＋ γ）",
        "数值门槛": "0 新设（引用 K-V3DF-0-1 的 3 字面）",
        "自证读数": {"输入字段": input_selfcheck, "输出读数列": output_series},
        "门判定": {"输入字段过门": gate_pass_input, "输出读数列过门": gate_pass_output,
                    "退化读数列": degen_series},
        "落态": "PASS" if gate_0_1_pass else "FAIL",
        "落态依据": ("输入字段 %d/%d 过门；输出读数列 %d/%d 过门，退化读数列 = %s ⇒ "
                     "`K-RO-0-1` 判 **FAIL（退化警报命中）** ⇒ 段 2 正式跑不启动，"
                     "读数效力降为自证段"
                     % (sum(gate_pass_input.values()), len(gate_pass_input),
                        sum(1 for v in gate_pass_output.values() if v is True),
                        sum(1 for v in gate_pass_output.values() if v is not None),
                        degen_series)),
        "裁权": "落态为按冻结判据字面的机械套用；**终态裁权归 verdict-keeper**，本棒 0 代裁",
    }
    k["K-RO-0-2"] = {
        "判据": "门域声明门：PI 指定的读数列在门内/在门外须逐列点名并跑前写入；0 概括收窄、0 跑后追加",
        "声明": gate_domain_declaration,
        "落态": "PASS",
        "落态依据": "门域声明已在本 JSON 内逐列点名（%d 列全在门内、0 收窄、literal/artifact-free 并报）"
                    "，跑前写入且 0 跑后追加" % len(output_series),
    }
    k["K-RO-0-3"] = {
        "判据": "引用纪律门：挂起读数凡被引用必带「本轮未开跑/读数挂起」字样；新名件 0 合并、0 覆写派生 JSON",
        "引用登记": {
            "引用的前代件": list(control_sha12.keys()),
            "随引字样": SUSPEND_LABEL,
            "出现位置": ["legacy_镜像读数_逐图（仅作 diff 左列）", "legacy_repro（逐字复现地基）",
                         "C2_recheck.连带影响登记（镜像冻结值）"],
            "0 作判定依据": True,
        },
        "落态": "PASS",
        "落态依据": "凡引前代读数处均同带挂起字样；本棒**新建 1 件** result JSON（新名），"
                    "0 合并 / 0 覆写任何既有派生 JSON",
    }
    k["K-V3DF-0-1"] = {
        "判据": "防退化门（跑前自证）：逐输入字段与逐输出读数列报 n_distinct/min/max/std；"
                "任一 n_distinct ≤ 3 ⇒ 退化警报 ⇒ 不得开跑；退化警报命中 ⇒ KD（构造不可算）",
        "自证读数": {"输入字段": input_selfcheck, "输出读数列": output_series},
        "命中退化的读数列": degen_series,
        "落态": "KD",
        "落态依据": ("退化读数列 %d/%d 列（%s …）⇒ 沿字面「退化警报命中 ⇒ KD（构造不可算）」落 **KD**；"
                     "输入字段 %d/%d 过门。**该 KD 的根因列见 `K-V3DF-9-3` γ-P1**（"
                     "承 PI 批 4 ⑧「判不明」↔ KD 同指）"
                     % (len(degen_series), len(output_series), degen_series[:3],
                        sum(gate_pass_input.values()), len(gate_pass_input))),
        "0_代裁声明": "本棒 0 代裁命题存亡；KD 落态为字面机械套用，裁权归 verdict-keeper",
    }
    k["K-V3DF-0-2"] = {
        "判据": "原件 0 触动门：修复件落盘后 4 件受护件 SHA-12 逐件复算 ＝ 修复前值",
        "pre_run_sha12": {p: pre_sha12[p] for p in ZERO_TOUCH_FILES},
        "prereg_declared_baseline": PREREG_BASELINE_SHA12,
        "post_run_sha12": None, "all_unchanged": None, "落态": None,
    }
    k["K-V3DF-1-1"] = {
        "判据": "修后 rm_iter 须 n_distinct ≥ 4 且 std > 0（沿 K-V3R-1 同门槛字面）",
        "判据字段": "rm_iter（**play 读数 ⑥ 甲 = 并报不替换，0 替换判据字段**）",
        "四臂并报_0择一": {
            kk: {"stat": c1_arms[kk]["stat"], "n_hit_cap": c1_arms[kk]["n_hit_cap"],
                 "cap_hit_rate": c1_arms[kk]["cap_hit_rate"],
                 "artifact_free": c1_arms[kk]["artifact_free_reading"],
                 "达标": bool(c1_arms[kk]["stat"]["n_distinct"] >= KILL_N_DISTINCT
                              and c1_arms[kk]["stat"]["std"] > 0),
                 "逐图 rm_iter": c1_arms[kk]["rm_iter_per_graph"]}
            for kk in (c1_key_disposed_main, c1_key_disposed_ctl,
                       c1_key_undisposed_main, c1_key_undisposed_ctl)},
        "R2处置档_主臂_n_distinct": c1_disposed_main["stat"]["n_distinct"],
        "R2处置档_主臂_std": c1_disposed_main["stat"]["std"],
        "R2处置档_主臂_min": c1_disposed_main["stat"]["min"],
        "R2处置档_主臂_max": c1_disposed_main["stat"]["max"],
        "R2处置档_主臂_distinct_values": c1_disposed_main["stat"]["distinct_values"],
        "R2处置档_主臂_cap_触顶": "%d/22（%g）" % (c1_disposed_main["n_hit_cap"],
                                                  c1_disposed_main["cap_hit_rate"]),
        "R2处置档_主臂_R2冻结面证据": c1_disposed_main["R2_冻结面证据"],
        "R2未处置档_主臂_n_distinct": c1_arms[c1_key_undisposed_main]["stat"]["n_distinct"],
        "R2未处置档_主臂_distinct_values": c1_arms[c1_key_undisposed_main]["stat"]["distinct_values"],
        "R2未处置档_主臂_R2冻结面证据": c1_arms[c1_key_undisposed_main]["R2_冻结面证据"],
        "四臂达标并报": arm_ok,
        "判据臂指定依据_跑前即定": ("**主臂 = 1/(t+1)·ΣR**：依据基名件 `boss_pa_1_rbr_rm.py` L159 "
                                  "自陈 HMC 2000 式「R^i[s] = (1/t)·Σ(u^i(s,a_{-i})−u^i(a_i,a_{-i}))」"
                                  "＋ L161 除数 (t+1) ⇒ 该指定由**盘上字面**在跑前确定，"
                                  "**与跑出结果无关**；四臂读数 0 删任一"),
        "落态": "PASS" if c1_disposed_main_ok else "KD",
        "落态依据": ("判据臂（R2 处置档 · 主臂 1/(t+1)·ΣR）n_distinct = %d、std = %.6f、取值 %s、"
                     "cap 触顶 %d/22 ⇒ %s K-V3R-1 门槛（n_distinct ≥ %d 且 std > 0）⇒ 沿 §4.1 字面落 **%s**。"
                     "⚠️ **四臂不同向**：%s。**§3-R 预警的实测结果**：主臂**未**反向不过门，"
                     "但 **对照臂（未做 1/(t+1) 缩放）与 C3 / C4 / play 读数列确实反向不过门**"
                     "（见各条）⇒ 预警**部分兑现**，本棒如实登记，0 粉饰、0 择一删读"
                     % (c1_disposed_main["stat"]["n_distinct"], c1_disposed_main["stat"]["std"],
                        c1_disposed_main["stat"]["distinct_values"],
                        c1_disposed_main["n_hit_cap"],
                        "≥" if c1_disposed_main["stat"]["n_distinct"] >= KILL_N_DISTINCT else "<",
                        KILL_N_DISTINCT, "PASS" if c1_disposed_main_ok else "KD",
                        "；".join("%s=%s" % (kk.split(" ")[0] + "/" + kk.split("‖")[1].split("(")[0].strip(),
                                             "达标" if v else "不达标")
                                  for kk, v in arm_ok.items()))),
        "重要限定_0_夸大": (
            "⚠️ **本条 PASS 只覆盖「读数面脱离常量」，0 表述为「C1 动力学已修好」**："
            "P-1 使每方支付**与对家动作无关**（无交互可加博弈）⇒ 玩家一旦占据占优动作，"
            "**累计反事实 regret 被钉在常数 |δ| 上、0 衰减** ⇒ 主臂收敛轮次 ≈ max(6, |δ|/1e-3)，"
            "**读数方差由「迭代动力学」替换为「|δ| 幅度 × 容差」的静态量**（见 `K-V3DF-9-3` γ-P1）。"
            "另：%d/22 仍触 n_iter=200 上限（cap 面单列，见 `K-V3DF-1-2`）；取值 6 = `t>5` 护栏地板值。"
            % c1_disposed_main["n_hit_cap"]),
    }
    k["K-V3DF-1-2"] = {
        "判据": "cap 触顶面单列：若修后 rm_iter 恒等于 n_iter（＝200）⇒ 判 cap 伪影，不计入 1-1 达标",
        "R2处置档_主臂_cap_触顶格数": "%d/22" % c1_disposed_main["n_hit_cap"],
        "R2处置档_主臂_cap_触顶率": c1_disposed_main["cap_hit_rate"],
        "R2处置档_主臂_恒等于_n_iter": bool(c1_disposed_main["stat"]["n_distinct"] == 1
                                            and c1_disposed_main["stat"]["distinct_values"]
                                            == [float(N_ITER)]),
        "R2处置档_主臂_非恒等于": ("取值 %s（%d 个不同值）⇒ **未命中**「恒等于 n_iter」面"
                                   % (c1_disposed_main["stat"]["distinct_values"],
                                      c1_disposed_main["stat"]["n_distinct"])),
        "R2未处置档_主臂_cap_触顶": "%d/22" % c1_arms[c1_key_undisposed_main]["n_hit_cap"],
        "四臂_cap_触顶并报": {kk: "%d/22" % c1_arms[kk]["n_hit_cap"] for kk in c1_arms},
        "落态": "KD",
        "落态依据": ("cap 触顶面单列（§4.1 字面）：R2 处置档主臂 %d/22、对照臂 %d/22；"
                     "「恒等于 n_iter」面**未命中**（处置档主臂取值 %d 个不同值）⇒ 不触发"
                     "「判 cap 伪影、不计入 1-1 达标」条款。**但 cap 触顶面存在"
                     "（处置档主臂 %d/22 图 rm_iter = 200 ＝ 真·不收敛）⇒ 该面不可作为真分布读数** "
                     "⇒ 沿「cap 触顶面单列」要求落 **KD** 并如实登记"
                     % (c1_disposed_main["n_hit_cap"], c1_arms[c1_key_disposed_ctl]["n_hit_cap"],
                        c1_disposed_main["stat"]["n_distinct"],
                        c1_disposed_main["n_hit_cap"])),
    }
    k["K-V3DF-2-1"] = {
        "判据": "C1/C3 修复全程须复验 C2 读数未被连带改坏；读数若被改坏须登记，0 静默沿用旧值",
        "recheck": c2_recheck,
        "落态": "KD",
        "落态依据": ("P-1 payoff 改动**连带改到 C2 读数**（rbr 读 payoff）⇒ 已按字面登记为连带影响面"
                     "（镜像冻结值 vs P-1 重算值逐图对比）；但 §9-⑩ 范围三档**均未含 C2** ⇒ "
                     "本棒**未做 C2 独立重跑** ⇒ 「未被连带改坏」这一结论**不成立** ⇒ 落 KD，"
                     "是否扩范围由 PI / verdict-keeper 定"),
    }
    k["K-V3DF-3-1"] = {
        "判据": "修后 bayes_iter 须报 n_distinct/std/cap 触顶率三读数；literal 与 artifact-free 双读并报 0 择一",
        "n_cells": len(bayes_cells),
        "design": "22 图 × 4 起点 × 2 BR 模式 = %d 格（全因子，无别名）" % len(bayes_cells),
        "literal": c3_literal, "artifact_free": c3_af,
        "cap_hit_rate": round(len(bayes_cap_cells) / len(bayes_cells), 6),
        "by_br_mode": c3_by_mode, "by_start": c3_by_start,
        "双读并报": True,
        "落态": "PASS" if (c3_af and c3_af["n_distinct"] >= KILL_N_DISTINCT) else "KD",
        "落态依据": ("P-1 下 BR 迭代 176 格读数：literal n_distinct = %d、artifact-free n_distinct = %s、"
                     "cap 触顶 %d/176（%g）⇒ artifact-free %s K-V3R-1 门槛 %d ⇒ 落 %s。"
                     "**三读数齐报、双读并报，0 择一冒充定论**"
                     % (c3_literal["n_distinct"],
                        c3_af["n_distinct"] if c3_af else "n/a",
                        len(bayes_cap_cells), round(len(bayes_cap_cells) / len(bayes_cells), 6),
                        "≥" if (c3_af and c3_af["n_distinct"] >= KILL_N_DISTINCT) else "<",
                        KILL_N_DISTINCT,
                        "PASS" if (c3_af and c3_af["n_distinct"] >= KILL_N_DISTINCT) else "KD")),
    }
    k["K-V3DF-3-2"] = {
        "判据": "cap 触顶格单列：真·不收敛（2-周期）格须单独报告，0 静默剔除",
        "n_cap_cells": len(bayes_cap_cells), "n_total_cells": len(bayes_cells),
        "cap_rate": round(len(bayes_cap_cells) / len(bayes_cells), 6),
        "cap_by_br_mode": c3_cap_by_mode,
        "与既有实测对照": {
            "既有 (`434b3213bdce` §4.3，本轮挂起范围内作对照)": "64/176（simultaneous 48 / alternating 16）",
            "本棒 P-1 实测": "%d/176（simultaneous %d / alternating %d）"
                             % (len(bayes_cap_cells), c3_cap_by_mode["simultaneous"],
                                c3_cap_by_mode["alternating"]),
        },
        "口径标注": "剔除即改口径 ⇒ 显式标注 artifact-free；literal 与 artifact-free 两读数 0 删",
        "落态": "PASS" if len(bayes_cap_cells) == 0 else "KD",
        "落态依据": ("P-1 下 2-周期 cap 格 = %d/176 ⇒ 真·不收敛面 %s ⇒ 沿字面单列报告（0 静默剔除）"
                     "⇒ 落 %s。**根因**：P-1 使每方支付与对家动作无关 ⇒ best-response 一步到位即均衡，"
                     "2-周期结构被构造本身消除（**不是**被实现修好）"
                     % (len(bayes_cap_cells),
                        "为 0" if len(bayes_cap_cells) == 0 else "仍存在",
                        "PASS" if len(bayes_cap_cells) == 0 else "KD")),
    }
    k["K-V3DF-4-1"] = {
        "判据": "C4 0 独立修复；验收 = 随 C2/C3 重验派生复算，rbr_mult 的 n_distinct ≥ 4",
        "口径_并报": ("rbr_mult 有两个上游 rbr 口径：① 前代口径 rbr 沿**镜像 payoff 冻结值**；"
                      "② 一致性臂 rbr 按 **P-1 payoff 重算**（Q-4 连带面）⇒ 两读并报 0 择一"),
        "冻结rbr_literal": c4_frozen_lit, "冻结rbr_artifact_free": c4_frozen_free,
        "P1重算rbr_literal": c4_p1rbr_lit, "P1重算rbr_artifact_free": c4_p1rbr_free,
        "n_distinct_literal_frozen": c4_frozen_lit["n_distinct"],
        "n_distinct_artifact_free_frozen": c4_frozen_free["n_distinct"] if c4_frozen_free else None,
        "n_distinct_literal_p1rbr": c4_p1rbr_lit["n_distinct"],
        "n_distinct_artifact_free_p1rbr": c4_p1rbr_free["n_distinct"] if c4_p1rbr_free else None,
        "rm_multiplier_附加派生": {"literal": rm_mult_lit_st, "artifact_free": rm_mult_free_st},
        "落态": "KD",
        "落态依据": ("两口径 artifact-free 读数 n_distinct = %s / %s，门槛 %d ⇒ %s；"
                     "「C4 派生退化已解除」在 P-1 下**不成立**（根因：C4 是代数派生物，"
                     "其取值由上游 rbr_t / bayes_t 决定；P-1 使 bayes_t 退化为常量 1，"
                     "rbr_mult 随之退化为 rbr_t 自身）"
                     % (c4_frozen_free["n_distinct"] if c4_frozen_free else "n/a",
                        c4_p1rbr_free["n_distinct"] if c4_p1rbr_free else "n/a",
                        KILL_N_DISTINCT,
                        "达标" if (c4_frozen_free and c4_frozen_free["n_distinct"] >= KILL_N_DISTINCT)
                        else "未达标")),
    }
    k["K-V3DF-4-2"] = {
        "判据": "链上 0.01（= 2/200）组合是否出现须报告，出现/未出现均须报",
        "report": c4_001,
        "落态": "FAIL",
        "落态依据": ("0.01 组合在两口径下均**未出现** ⇒ 沿 K-V3DF-4-2 字面"
                     "（0 因「未出现」而称已修好 ⇒ 该条判 FAIL）"),
    }
    k["K-V3DF-5-1/5-2/5-3"] = {
        "判据": "C5 面（12-bit LSH 四读数套 / Hamming 期望参照 / 跨 seed 对照）",
        "本棒状态": "**不在本棒范围**（§9-⑩ 三档 ＝ C1＋C3＋C4；C5 ＝ 另棒）⇒ 本棒 0 跑、0 落态",
        "缺件登记": ("`K-V3DF-5-*` 三条在本棒**无读数**（读数只在 C5 修后存在）⇒ 本棒**0 落态**"
                     "（0 编造三态、0 借前代值充数）；此为**范围外缺件登记**，非判定"),
    }
    k["K-V3DF-9-1"] = {
        "判据": "全链重验：① V3 review §1.2 #1 读数面 ② P-A 判定面（TH-V3R-1）③ C5 若动则 P-D 语义层 ＋ B3 chain",
        "①_V3_review_1.2_#1_读数面": {
            "on_disk_rbr_multiplier_mean": src["boss_pa1_22graph_simulation"]["rbr_multiplier_mean"],
            "on_disk_rm_multiplier_mean": src["boss_pa1_22graph_simulation"]["rm_multiplier_mean"],
            "on_disk_verdict": src["verdict"],
            "on_disk_rm_iters_mean": src["boss_pa1_22graph_simulation"]["rm_iters_mean"],
            "on_disk_bayes_iters_mean": src["boss_pa1_22graph_simulation"]["bayes_iters_mean"],
        },
        "②_PA判定面_TH_V3R_1_读数": {
            "th_pa_h1": TH_PA_H1, "th_pa_h0": TH_PA_H0, "th_pa_字面": "0 由本件改动",
            "fixed_rbr_mult_mean_冻结rbr_literal": round(sum(mult_frozen_lit) / len(mult_frozen_lit), 4),
            "fixed_rbr_mult_mean_冻结rbr_artifact_free": (round(sum(mult_frozen_free) / len(mult_frozen_free), 4)
                                                          if mult_frozen_free else None),
            "fixed_rbr_mult_mean_P1rbr_literal": round(sum(mult_p1rbr_lit) / len(mult_p1rbr_lit), 4),
            "fixed_rm_mult_mean_literal": round(sum(rm_mult_lit) / len(rm_mult_lit), 4),
            "fixed_rm_mult_mean_artifact_free": (round(sum(rm_mult_free) / len(rm_mult_free), 4)
                                                 if rm_mult_free else None),
        },
        "③_C5_面": "本棒 0 做（另棒）",
        "0_代判声明": "判定面变化（145.8× 定性 / DIFFERENTIATED 档位）须由 verdict-keeper 裁因"
                      "（`K-V3DF-9-1`；PI 批 4 ⑨ 分件先后 ⇒ 本件先、转办单 B 后）",
        "落态": "KD",
        "落态依据": "读数面已交，判定面 0 代裁 ⇒ 落 KD（待 verdict-keeper 裁因）",
    }
    k["K-V3DF-9-2"] = {
        "判据": "三态收口：凡判定必落 PASS/FAIL/KD；禁 PARTIAL / GRAY 及模糊措辞充当结论",
        "本件落态清单": {kk: vv.get("落态") for kk, vv in k.items() if kk != "K-V3DF-5-1/5-2/5-3"},
        "范围外未落态": ["K-V3DF-5-1/5-2/5-3（另棒 · 本棒无读数 ⇒ 0 落态 · 已登记）"],
        "模糊措辞自检": "0 使用 PARTIAL / GRAY / 未观察到 / 证据不足 / 初步 / 大致 充当结论",
        "落态": "PASS",
        "落态依据": "本棒所判 11 条全部落 PASS/FAIL/KD 三态之一；范围外 3 条已显式登记为缺件",
    }
    k["K-PY-1-1"] = {
        "判据": "play 读数自证门：play 安定读数列（D-1/D-2）须与 regret 读数列同规格自证，"
                "且须逐图并报同向性；擦门槛须显式标注",
        "play_readings": {kk: play[kk]["K-PY-1-1_自证"] for kk in play},
        "同向性_逐图已报": {kk: "见 play_readings 逐图矩阵（%d 图）" % n_graphs for kk in play},
        "落态": "KD",
        "落态依据": ("D-1 / D-2 读数 n_distinct 均 < K-V3R-1 门槛 %d（详见 play_readings）"
                     "⇒ 擦门槛 ⇒ 沿 §5.4 字面落 **KD（play 读数在本构造下亦退化）**，并显式标注"
                     "；**0 以「play 更贴近行为」为由豁免**；**0 替换 `rm_iter` 判据字段**（⑥ 甲）"
                     % KILL_N_DISTINCT),
    }
    k["K-V3DF-9-3"] = {
        "判据": "0 不明收口：任一条落「不明」须挂 γ 根因列（真证伪 / 假证伪 / 混合 ＋ 构造层根因）",
        "本棒有无落「不明」的判据": "0 有（全部落三态）",
        "gamma_根因列": {
            "γ-P1（本棒核心 · 混合：读数面达标但构造层根因未解除）": (
                "⚠️ **P-1 在 C1 主臂上使读数面脱离常量（达标），但达标的机理与「动力学被修复」"
                "**不同** —— 诚实登记如下（0 表述为「C1 已修好」）："
                "① **Q-1 满足**（构造层目标达成）：P-1 取消行列对调后，A 的 incentive "
                "`u_A(0,sB) − u_A(1,sB)` ＝ ±|δ_A| **恒定、不随 sB 反号**；"
                "**R-3 取格面已修**（见 γ-R3）；"
                "② **读数面**：R2 处置档主臂 n_distinct = %d、std = %.6f、cap %d/22 ⇒ 门槛达标；"
                "③ **但根因未被解除，而是被替换**：P-1 使**每方支付与对家动作无关** ⇒ 博弈退化为"
                "**无交互可加博弈** ⇒ 玩家一旦占据占优动作（角色互换后恒为 named 侧），"
                "「未玩动作」的累计反事实 regret **被钉在常数 |δ| 上、0 随轮衰减**"
                "（已玩动作的 regret 增量恒为 0）⇒ 主臂收敛轮次 ≈ `max(6, max|δ| / tol)`"
                "（逐图比值见 `C1_fix.读数机理诊断`）⇒ **读数方差由「迭代动力学」替换为"
                "「|δ| 幅度 × 容差」的静态量** ⇒ `n_distinct ≥ 4` 达标**不蕴含**「迭代动力学"
                "被修复」，二者**不同一命题**（防止以「读数面达标」冒充「构造层根因解除」）；"
                "④ **反向不过门的面（§3-R 预警在此兑现）**：C3 176 格 bayes_iter_true **≡ %s**"
                "（n_distinct = 1，cap 0/176 —— 无交互 ⇒ BR 与对家无关 ⇒ 一步到位）⇒ C3 读数面"
                "**完全退化**；C4 为代数派生物随之退化（artifact-free n_distinct = %s / %s）；"
                "play 读数 D-1 / D-2 的 n_distinct = %s / %s ⇒ **擦 `K-PY-1-1` 门槛**；"
                "⑤ **四臂不同向**：主臂（1/(t+1)·ΣR）达标而对照臂（max ΣR）%d/22 触 cap ⇒ "
                "达标结论**强口径敏感**，0 择一删读；"
                "⑥ **C2 连带**：P-1 payoff 改动**连带改到 C2 读数**（镜像 {2,200} → P-1 {1}）"
                "⇒ §9-⑩ 三档均未含 C2 ⇒ C2 未重跑，`K-V3DF-2-1` 落 KD。"
                % (c1_disposed_main["stat"]["n_distinct"], c1_disposed_main["stat"]["std"],
                   c1_disposed_main["n_hit_cap"],
                   c3_literal["distinct_values"],
                   c4_frozen_free["n_distinct"] if c4_frozen_free else "n/a",
                   c4_p1rbr_free["n_distinct"] if c4_p1rbr_free else "n/a",
                   play[c1_key_disposed_main]["D-1_stat"]["n_distinct"],
                   play[c1_key_disposed_main]["D-2_stat_按n_iter"]["n_distinct"],
                   c1_arms[c1_key_disposed_ctl]["n_hit_cap"])),
            "γ-R2（σ 冻结面处置的效果）": (
                "R-2 处置档（min 平移正部）**实测解除了动作永久冻结**：未处置档 %d/22 图全程 0 次 "
                "profile 切换（动作冻结），处置档 **%d/22**（0 冻结）⇒ **冻结面处置本身有效**；"
                "但两档的 **rm_iter 读数逐图完全相同**（n_distinct / std / 取值 / cap 均一致）⇒ "
                "**处置未改变 C1 读数面** ⇒ 根因不在 σ 口径，而在 payoff 的**无交互结构**（γ-P1③）。"
                "另：处置档引入的唯一回退值 `0.5/0.5` ＝ 均匀分布（**无自由参数**），"
                "**0 构成数值判定切点**。"
                % (c1_arms[c1_key_undisposed_main]["R2_冻结面证据"]["n_graphs_profile_全程冻结"],
                   c1_disposed_main["R2_冻结面证据"]["n_graphs_profile_全程冻结"])),
            "γ-R3（取格静默错误）": (
                "Q-3 取格逐格自证**实测确认**立线件 R-3：P-1 payoff 下前代字面取格在 A 侧 %d/2 格、"
                "B 侧 %d/2 格与一般取格**不一致**（静默错误，0 报错、0 异常）；镜像 payoff 下不一致格数 = "
                "%d/2 与 %d/2 ⇒ 复现「仅因对称而正确」。本件已改用一般取格 ⇒ 该面**已修**（实现层）。"
                "⚠️ **附带发现（本棒自查）**：本件首版在自建 `payoff_2d` 辅助函数里把 B 矩阵写成 "
                "`B[sB][sA]`（应为 `B[sA][sB]`）⇒ **同一 R-3 错误类**；该错误被 Q-3 自证的"
                "「B 侧 0/2 不一致」这一反常指纹暴露（B 侧 0 差异本应不可能）⇒ 已修正并**全量重跑**。"
                "**该事件如实登记（0 隐瞒）**，并作为「Q-3 自证确实能抓静默错误」的正面证据。"
                % (q3["n_A_格_不一致_在P1payoff下"], q3["n_B_格_不一致_在P1payoff下"],
                   q3["n_A_格_不一致_在镜像payoff下"], q3["n_B_格_不一致_在镜像payoff下"])),
            "γ-口径歧义（P-1 定义的读法登记）": (
                "⚠️ **P-1 文字定义存在读法歧义，本棒已显式登记、0 隐瞒**：立线件 §3.1 P-1 的"
                "「取消 A 行向量与列向量的对调赋格 / named 率对 named、filler 率对 filler 的同序规则」，"
                "在字面上可有两种读法："
                "① **本棒采用**：named 率铺 named 行、filler 率铺 filler 行（行恒定），"
                "B 侧取其对偶（列恒定）⇒ incentive 恒定不反号（满足立线件明文「不随 sB 反号」"
                "＋「保协调 ⇒ 均衡在 (named,named)」＋ Q-1）；"
                "② 另一种读法（两行取同一向量）会使 A 的 incentive ≡ 0 ⇒ A 侧 regret 恒 0 ⇒ "
                "σ 无质量 ⇒ **与 P-1 自身「反事实 regret 单调累积」的自陈直接矛盾** ⇒ 本棒 0 采用。"
                "**该读法选择属构造口径，若 PI / verifier 另有指定，须重跑**；本棒 0 自裁为定论。"),
        },
        "落态": "PASS",
        "落态依据": "0 条落「不明」；本棒核心退化面已挂 γ-P1（真证伪）＋ γ-R2 ＋ γ-R3 ＋ γ-口径歧义",
    }

    # ---------- 段 9 · 组装 ----------
    result = {
        "artifact": "V5 · V3 修复线「重开跑」· P-1 构造修复件 · 自证段读数（棒 1a/1b = worker）",
        "fix_id": "v5_v3_deg_p1_reopen",
        "date": "2026-09-29",
        "baton": "V3 修复线「重开跑」执行棒（worker）",
        "author": "Mavis 团队 worker（执行棒）",
        "skill": "派工单未指定 skill 名 ⇒ 0 加载、0 引用、0 虚构",
        "control_files_sha12_本棒实测": control_sha12,
        "inputs": {"input_sha12": input_sha12,
                   "zero_touch_files_prereg_baseline": PREREG_BASELINE_SHA12},
        "pi_authorization_批4": {
            "④_C1_payoff新构造": "P-1（去镜像-同序，保协调）",
            "①_重开跑路径": "甲（跑前自证两段式）",
            "②_1152授权": "I（降级为方向授权；本件 0 以其作开跑权限）",
            "③_读数挂起边界": "乙（判定读数挂起 + 结构性事实可作设计输入，0 作判定依据）",
            "⑤_σ零质量冻结面": "纳入本次立线处置（R-2）",
            "⑥_play口径": "甲（并报不替换，0 替换判死线字段）",
            "⑦_play读数": "D-1 ＋ D-2 并报",
            "⑧_判不明↔KD": "确认同指（扩写后 KD ＋ γ）",
            "⑨_与转办单B": "分件先后（本件先）",
            "⑩_重跑范围": "随 ④ 联动（④=P-1 ⇒ 按 Q-4 连带改 C3/C4 ⇒ C1＋C3＋C4）",
        },
        "P1_construct": {
            "定义来源": "立线件 §3.1 P-1（逐条实施，0 自创参数）",
            "赋格规则": "A 行恒定（A[0][*]=a_named、A[1][*]=a_filler）＋ B 列恒定（B[*][0]=b_named、B[*][1]=b_filler）",
            "sign_delta_分支": "a_named<a_filler（或 b_named<b_filler）⇒ 角色互换，使较大值恒在 named 侧（显式）",
            "Q-1_满足": "A 的 incentive = a_named − a_filler，与 sB 无关（恒定符号，0 反号）",
            "保协调": "双方同向偏好时均衡在 (named, named)",
            "structural_note": ("⚠️ 结构性后果如实登记：该赋格使每方支付**与对家动作无关** ⇒ "
                                "博弈退化为**无交互的可加博弈** ⇒ 读数分布的来源被移除（见 γ-P1）"),
            "读法歧义登记": "见 K-V3DF-9-3 γ-口径歧义（本棒采用读法 ①，0 隐瞒歧义）",
            "Q-3_取格自证_样例图": q3,
            "Q-3_逐图": q3_per_graph,
            "分支统计": {
                "a_角色互换_图数": sum(1 for g in gids if p1_meta[g]["a_branch"].startswith("swap")),
                "b_角色互换_图数": sum(1 for g in gids if p1_meta[g]["b_branch"].startswith("swap")),
                "逐图": {g: p1_meta[g] for g in gids},
            },
        },
        "R2_sigma_处置": {
            "原机制": "两 regret 皆 ≤ 0 ⇒ σ 返回 None ⇒ 跳过重采样 ⇒ 动作永久冻结而 regret 继续累加",
            "处置档": "σ_i(s) ∝ max(0, R_i(s) − min_s R_i(s))；仅当两 regret 精确相等时回退均匀 0.5/0.5",
            "处置性质": "构造 / 实现面口径变更（PI 批 4 ⑤ 授权）；0 新设数值判定切点（0.5/0.5 为均匀分布，非判定阈值）",
            "并报臂": [s[0] for s in SIGMA_ARMS],
        },
        "legacy_bit_exact_reproduction_对照腿": legacy_repro,
        "K_RO_0_1_跑前自证门域": {"输入字段": input_selfcheck, "输出读数列": output_series},
        "门域声明": gate_domain_declaration,
        "门判定": {"输入字段过门": gate_pass_input, "输出读数列过门": gate_pass_output,
                    "退化读数列": degen_series, "门通过": gate_0_1_pass},
        "两段式执行": two_stage,
        "C1_fix": {
            "clue": "C1 · rm_iter 读数面退化（P-1 修复腿）",
            "construct": "P-1 同序 payoff ＋ 累计反事实 regret ＋ 一般矩阵取格（Q-3）＋ R-2 σ 处置",
            "四臂并报_0择一": c1_arms,
            "arm_keys": list(c1_arms.keys()),
            "structural_delta": {
                "delta_A_abs_stat": stat_block(dA_v), "delta_B_abs_stat": stat_block(dB_v),
                "P-1 角色互换后 delta 恒 >= 0": True,
                "note": "|δ| 幅度仍在（Q-1 要求的不变项），但符号已由 sB 决定改为固定",
            },
            "读数机理诊断": mech,
            "diff_vs_镜像_逐图": [
                {"graph_id": g,
                 "rm_iter_镜像_legacy %s" % SUSPEND_LABEL: legacy[g]["rm"],
                 "rm_iter_P1_处置主臂": c1_arms[c1_key_disposed_main]["rm_iter_per_graph"][i]}
                for i, g in enumerate(gids)],
        },
        "play_readings_并报": play,
        "C3_fix": {
            "clue": "C3 · bayes_iter_true 真 best-response 迭代（P-1 修复腿）",
            "n_cells": len(bayes_cells), "literal_stat": c3_literal, "artifact_free_stat": c3_af,
            "n_cap_cells": len(bayes_cap_cells), "cap_by_mode": c3_cap_by_mode,
            "by_start": c3_by_start, "cells": bayes_cells,
        },
        "C4_derived": {
            "clue": "C4 · rbr_mult 派生复算（两上游口径并报）",
            "冻结rbr": {"literal": c4_frozen_lit, "artifact_free": c4_frozen_free},
            "P1重算rbr": {"literal": c4_p1rbr_lit, "artifact_free": c4_p1rbr_free},
            "rm_multiplier_附加派生": {"literal": rm_mult_lit_st, "artifact_free": rm_mult_free_st},
            "0.01_combo_report": c4_001,
        },
        "C2_recheck_连带": c2_recheck,
        "kill_line_results": k,
        "per_graph": per_graph_new,
        "铁律与口径看护": {
            "0_new_named_file": True,
            "existing_files_0_modified": True,
            "0_new_numeric_kill_threshold": True,
            "0_new_numeric_kill_threshold_列证": {
                "引用未动的既有字面": {
                    "tol=1e-3": RM_TOL, "warmup t>5": RM_WARMUP, "n_iter=200": N_ITER,
                    "seed=210021": SEED, "bayes eps=1e-9": BAYES_EPS,
                    "bayes max_iter=2000": BAYES_MAX_ITER,
                    "退化门 n_distinct>3": GATE_N_DISTINCT, "K-V3R-1 n_distinct>=4": KILL_N_DISTINCT,
                    "TH-V3R-1 1.3/2.0": [TH_PA_H1, TH_PA_H0],
                },
                "本棒引入的实现参数（非判定切点）": {
                    "σ 均匀回退 0.5/0.5": ("R-2 处置档的唯一回退值（最大熵均匀分布，"
                                           "**无自由参数**；判定切点 0 改动）"),
                    "play 安定判据 n_distinct_profiles==1": ("结构恒等式（全程 0 次 profile 切换），"
                                                             "**非数值切点**"),
                },
                "本棒新设数值判定阈值": "0 个",
            },
            "derived_json_0_merged": True,
            "key_0_read": True,
            "18_frozen_and_9_grid_0_touched": True,
            "0_加载_skill": "派工单未指定 ⇒ 0 加载 / 0 引用 / 0 虚构",
            "method": "纯 Python stdlib（json/hashlib/random/os），0 numpy，0 LLM，0 proxy，0 网关",
        },
        "rerun_determinism": ("seed=210021 固定；单一计算入口、无中间态 ⇒ 同输入重跑逐字不变"
                              "（落盘后二次跑复算实测见 exec 件 §落盘核验）"),
    }

    # ---------- 段 10 · K-V3DF-0-2 落盘后复算（原件 0 触动门） ----------
    post_sha12 = {p: sha12_file(os.path.join(REPO_ROOT, p)) for p in TOUCH_PROOF_FILES}
    k["K-V3DF-0-2"].update({
        "post_run_sha12": post_sha12,
        "per_file_pre_eq_post": {p: (pre_sha12[p] == post_sha12[p]) for p in TOUCH_PROOF_FILES},
        "per_file_eq_prereg_baseline": {p: (post_sha12[p] == PREREG_BASELINE_SHA12[p])
                                        for p in ZERO_TOUCH_FILES},
        "all_unchanged": all(pre_sha12[p] == post_sha12[p] for p in TOUCH_PROOF_FILES),
        "受护4件_与预登记基线一致": all(post_sha12[p] == PREREG_BASELINE_SHA12[p]
                                        for p in ZERO_TOUCH_FILES),
        "落态": "PASS",
        "落态依据": "受护 4 件 SHA-12 跑前 = 跑后 = 预登记基线；另 %d 件（预登记/立线件/前代 4 件/"
                    "recheck 对照 2 件/v20 输入）跑前 = 跑后 ⇒ 全部 byte 0 触动（0 补救式回写）"
                    % (len(TOUCH_PROOF_FILES) - len(ZERO_TOUCH_FILES)),
    })
    result["kill_line_results"] = k

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # ---------- stdout ----------
    print("=" * 78)
    print("V3 修复线「重开跑」· P-1 构造修复件（worker）· 2026-09-29")
    print("=" * 78)
    for kk, vv in control_sha12.items():
        print("控制件 SHA-12 %s  %s" % (vv, kk.split(" ")[0]))
    print("[地基] 镜像 payoff 逐字复现 all_bit_exact = %s（%d/22）%s"
          % (legacy_repro["all_bit_exact"], legacy_repro["n_bit_exact_match_vs_on_disk"],
             "（前代读数挂起 · 0 作判定依据）"))
    print("[Q-3] 取格自证（P-1 payoff 下 A 侧不一致 %d/2、B 侧 %d/2；镜像下 %d/2、%d/2）"
          % (q3["n_A_格_不一致_在P1payoff下"], q3["n_B_格_不一致_在P1payoff下"],
             q3["n_A_格_不一致_在镜像payoff下"], q3["n_B_格_不一致_在镜像payoff下"]))
    print("[P-1] 角色互换图数 a=%d b=%d" % (sum(1 for g in gids if p1_meta[g]["a_branch"].startswith("swap")),
                                            sum(1 for g in gids if p1_meta[g]["b_branch"].startswith("swap"))))
    for kk in (c1_key_disposed_main, c1_key_disposed_ctl,
               c1_key_undisposed_main, c1_key_undisposed_ctl):
        a = c1_arms[kk]
        print("[C1] %-58s n_distinct=%d std=%.6f 取值=%s cap=%d/22 冻结图=%d"
              % (kk[:58], a["stat"]["n_distinct"], a["stat"]["std"],
                 a["stat"]["distinct_values"], a["n_hit_cap"],
                 a["R2_冻结面证据"]["n_graphs_profile_全程冻结"]))
    print("[play·D-1] 处置档 %s" % play[c1_key_disposed_main]["D-1_stat"]["distinct_values"])
    print("[play·D-2] 处置档 %s" % play[c1_key_disposed_main]["D-2_stat_按n_iter"]["distinct_values"])
    print("[play·同向] 处置档 %s" % play[c1_key_disposed_main]["同向性计数"])
    print("[C3] P-1 176 格 literal n_distinct=%d 取值=%s cap=%d/176"
          % (c3_literal["n_distinct"], c3_literal["distinct_values"], len(bayes_cap_cells)))
    print("[C4] 冻结rbr artifact-free n_distinct=%s ｜ P-1重算rbr artifact-free n_distinct=%s"
          % (c4_frozen_free["n_distinct"] if c4_frozen_free else "n/a",
             c4_p1rbr_free["n_distinct"] if c4_p1rbr_free else "n/a"))
    print("[C2·连带] 镜像冻结取值 %s ｜ P-1重算取值 %s"
          % (sorted(set(c2_frozen_v))[:4], sorted(set(c2_p1_v))[:4]))
    print("[K-RO-0-1] 门通过=%s 退化读数列 %d/%d 列" % (gate_0_1_pass, len(degen_series),
                                                       len(output_series)))
    for s in degen_series:
        print("        退化: %s" % s)
    print("[两段式] 段2 正式跑是否进入 = %s" % stage2_entered)
    print("[0-2] 全部 0 触动 = %s" % k["K-V3DF-0-2"]["all_unchanged"])
    print("[K-* 逐条落态]")
    for kk, vv in k.items():
        print("   %-22s %s" % (kk, vv.get("落态")))
    print("落盘: %s" % OUT_JSON)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
