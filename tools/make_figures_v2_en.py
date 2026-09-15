#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Deposon v2X 论文附录 D 五图中文版制作脚本。

纪律：
- 全部数据机械读取自 results/ 下冻结 JSON / CSV，不手写任何数字；
- 不修改 rcParams 的 font.family / axes.unicode_minus / font.sans-serif
  （运行环境需已配置中文字体，本工作区已配置）；
- 每张图出图前做数据点计数自检，口径与论文正文/附录 A 对齐，不符即 assert 失败。

运行：python3 tools/make_figures_v2.py
输出：figures/fig1_boundary_map_en.png … fig5_poa_distribution_en.png（300 dpi）
自检台账打印到 stdout（同步誊入 docs/FIGURES_v2.md）。
"""
import csv
import json
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / "results"
OUT = ROOT / "figures"
OUT.mkdir(exist_ok=True)

CHECKS = []  # (figure, item, observed, expected)


def check(fig, item, observed, expected):
    ok = observed == expected
    CHECKS.append((fig, item, observed, expected, ok))
    assert ok, f"[{fig}] {item}: observed={observed!r} != expected={expected!r}"


def load_json(name):
    with open(RES / name, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- 数据源
ce = load_json("deposon_v20_corpus_eval.json")      # 图 1/2/5
cv = load_json("deposon_v20_crossval.json")         # 图 1（先验臂）
g7 = load_json("deposon_v20_gt7.json")              # 图 4
gt = load_json("deposon_v20_gt.json")               # 图 5（冻结 GT-4 PoA）
reg = load_json("v20_regression_field_v2.json")     # 图 3 注释
with open(RES / "v20_graph_features.csv", encoding="utf-8") as f:
    feat_rows = list(csv.DictReader(f))             # 图 3

named = ce["graph_level"]["named_hits3"]            # gid -> arm -> named Hits@3
per_graph_meta = {g["graph_id"]: g for g in ce["per_graph"]}  # family 等
prior_named = {g: float(v["llm_prior"]["named"])
               for g, v in cv["prior_arm_eval"].items()}       # 族 L 四图

# 低饱和度配色（避免蓝紫渐变与高饱和背景）
C_FIELD = "#5F8D86"    # 场臂：灰青
C_PRIOR = "#C08552"    # 先验臂：灰赭
C_RANDOM = "#9C9C9C"   # random：中灰
C_DEGREE = "#7D8CA3"   # degree：灰蓝
C_L = "#C08552"        # 族 L
C_S = "#5F8D86"        # 族 S
C_INF = "#B5B5B5"      # ∞ 条
C_PHI = "#A26769"      # Φ 轴
GRID = dict(axis="y", color="#DDDDDD", lw=0.7, zorder=0)


def graph_order():
    """族 L 在前（字母序），族 S 按子族→规模 N 排序。"""
    def key(gid):
        fam = per_graph_meta[gid]["family"]
        if fam == "L":
            return (0, gid)
        sub = gid.split("_")[0]          # S1 / S2 / ... / S6
        return (1, sub, per_graph_meta[gid]["N"])
    return sorted(named.keys(), key=key)


# ================================================================ 图 1
def fig1():
    gids = graph_order()
    check("fig1", "图数（22 图语料）", len(gids), 22)
    check("fig1", "先验臂图数（族 L 主报）", len(prior_named), 4)
    # 先验臂必须全部落在族 L
    check("fig1", "先验臂全部属于族 L",
          all(per_graph_meta[g]["family"] == "L" for g in prior_named), True)

    x = np.arange(len(gids))
    w = 0.38
    fm = [named[g]["field_mean"] for g in gids]
    fig, ax = plt.subplots(figsize=(13.5, 5.6))
    n_L = sum(1 for g in gids if per_graph_meta[g]["family"] == "L")
    ax.axvspan(-0.6, n_L - 0.4, color="#F4EDE4", zorder=0)   # 族 L 区
    ax.axvspan(n_L - 0.4, len(gids) - 0.4 + 0.6, color="#EDF2F0", zorder=0)
    ax.text((n_L - 1) / 2, 1.13, "Family L (real-semantic graphs; prior arm reported here)",
            ha="center", fontsize=10, color=C_L)
    ax.text(n_L + (len(gids) - n_L - 1) / 2, 1.13,
            "Family S (synthetic structural graphs; prior arm unavailable, pre-registered)",
            ha="center", fontsize=10, color=C_S)

    ax.bar(x - w / 2, fm, w, color=C_FIELD, label="field_mean", zorder=3)
    prior_x, prior_y = [], []
    for i, g in enumerate(gids):
        if g in prior_named:
            prior_x.append(i + w / 2)
            prior_y.append(prior_named[g])
    ax.bar(prior_x, prior_y, w, color=C_PRIOR,
           label="llm_prior (family L only)", zorder=3)
    ax.scatter(x, [named[g]["random"] for g in gids], marker="v", s=34,
               color=C_RANDOM, label="random (reference)", zorder=4)
    ax.scatter(x, [named[g]["degree"] for g in gids], marker="^", s=34,
               color=C_DEGREE, label="degree (reference)", zorder=4)

    # 胜负标记：每图在 {场, 先验?, random, degree} 中的第一名
    arms_of = lambda g: {"field": named[g]["field_mean"],
                         "random": named[g]["random"],
                         "degree": named[g]["degree"],
                         **({"prior": prior_named[g]} if g in prior_named else {})}
    for i, g in enumerate(gids):
        a = arms_of(g)
        win_arm = max(a, key=a.get)
        win_val = a[win_arm]
        if win_val <= 0:
            continue
        star_color = {"field": C_FIELD, "prior": C_PRIOR}.get(win_arm, "#666666")
        ax.scatter([i], [win_val + 0.035], marker="*", s=110,
                   color=star_color, zorder=5)
    ax.scatter([], [], marker="*", s=110, color="#666666",
               label="* per-graph winner (colored = field/prior, gray = baseline)")

    ax.set_xticks(x)
    ax.set_xticklabels(gids, rotation=55, ha="right", fontsize=8.5)
    ax.set_ylabel("named Hits@3")
    ax.set_ylim(0, 1.22)
    ax.grid(**GRID)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.9)
    ax.set_title("Fig. 1: Division-of-labor boundary overview: 22-graph field vs prior win map (named Hits@3)",
                 fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT / "fig1_boundary_map_en.png", dpi=300)
    plt.close(fig)


# ================================================================ 图 2
def fig2():
    st = ce["verdicts"]["H_A1_field_mean_gt_random"]["sign_test"]
    kl = ce["verdicts"]["kill_lines"]["H_A_dead"]
    gids = graph_order()
    check("fig2", "图数（22 图语料）", len(gids), 22)

    xr = [named[g]["random"] for g in gids]
    yf = [named[g]["field_mean"] for g in gids]
    n_pos = sum(1 for r, f in zip(xr, yf) if f > r)
    n_neg = sum(1 for r, f in zip(xr, yf) if f < r)
    n_tie = sum(1 for r, f in zip(xr, yf) if f == r)
    check("fig2", "符号检验 n+", n_pos, st["n_pos"])
    check("fig2", "符号检验 n−", n_neg, st["n_neg"])
    check("fig2", "符号检验 平", n_tie, st["n_tie"])
    check("fig2", "斩杀线触发", kl["triggered"], True)
    rev = set(kl["reversals_vs_random"])
    check("fig2", "反转图数", len(rev), 4)
    check("fig2", "反转图与 n− 图集合一致",
          rev, {g for g, r, f in zip(gids, xr, yf) if f < r})

    fig, ax = plt.subplots(figsize=(7.6, 7.0))
    lim = max(max(xr), max(yf)) * 1.12
    ax.plot([0, lim], [0, lim], ls="--", color="#888888", lw=1.2,
            label="kill line: field = random")
    for g, r, f in zip(gids, xr, yf):
        fam = per_graph_meta[g]["family"]
        col = C_L if fam == "L" else C_S
        mk = "s" if fam == "L" else "o"
        edge = "#B03030" if g in rev else "white"
        lw = 1.8 if g in rev else 0.6
        ax.scatter([r], [f], marker=mk, s=72, color=col,
                   edgecolor=edge, linewidth=lw, zorder=3)
    offsets = {"L_historical_causality": (-4, -14),
               "L_physics_concepts": (6, 8),
               "L_project_management": (8, -3),
               "S2_n45": (8, -13)}
    for g in sorted(rev):  # 反转图标注
        ax.annotate(g, (named[g]["random"], named[g]["field_mean"]),
                    textcoords="offset points", xytext=offsets.get(g, (7, -11)),
                    fontsize=8, color="#B03030")
    ax.scatter([], [], marker="o", s=72, color=C_S, label="Family S (synthetic structural)")
    ax.scatter([], [], marker="s", s=72, color=C_L, label="Family L (real-semantic)")
    ax.scatter([], [], marker="o", s=90, facecolor="none",
               edgecolor="#B03030", linewidth=1.8,
               label=f"reversed graphs (field<random, n={len(rev)})")
    ax.text(0.03, 0.97,
            f"sign test: {st['n_pos']}+ / {st['n_neg']}- / {st['n_tie']} ties\n"
            f"p_exact = {st['p_exact']:.4f} (Holm passed)\n"
            f"reversals >= 3 => H_A_dead.triggered = true (H-A1 killed)",
            transform=ax.transAxes, va="top", fontsize=10,
            bbox=dict(boxstyle="round,pad=0.4", fc="#F7F4EF", ec="#CCCCCC"))
    ax.set_xlabel("random arm named Hits@3")
    ax.set_ylabel("field_mean arm named Hits@3")
    ax.set_xlim(-0.01, lim)
    ax.set_ylim(-0.01, lim)
    ax.set_aspect("equal")
    ax.grid(color="#E8E8E8", lw=0.6, zorder=0)
    ax.legend(loc="lower right", fontsize=9, framealpha=0.9)
    ax.set_title("Fig. 2: H-A1 kill line and reversed-graph distribution (22-graph sign-test scatter)",
                 fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT / "fig2_killsign_scatter_en.png", dpi=300)
    plt.close(fig)


# ================================================================ 图 3
def fig3():
    check("fig3", "特征行数 = 回归 n_observations",
          len(feat_rows), reg["n_observations"])
    check("fig3", "回归 n_observations（论文口径 n=20）",
          reg["n_observations"], 20)

    hub = np.array([float(r["hub_concentration"]) for r in feat_rows])
    sem = np.array([float(r["real_semantics"]) for r in feat_rows])
    fld = np.array([float(r["field_named"]) for r in feat_rows])
    fam = [r["family"] for r in feat_rows]
    gids = [r["graph_id"] for r in feat_rows]

    rng = np.random.default_rng(0)  # 仅用于 y 向抖动（修饰性，非数据）
    jit = rng.uniform(-0.045, 0.045, size=len(feat_rows))

    fig, ax = plt.subplots(figsize=(9.2, 6.2))
    for m, f in zip(["o", "s"], ["S", "L"]):
        sel = [i for i, fa in enumerate(fam) if fa == f]
        sc = ax.scatter(hub[sel], sem[sel] + jit[sel], c=fld[sel],
                        cmap="cividis", vmin=0.0, vmax=float(fld.max()),
                        marker=m, s=110, edgecolor="#444444", linewidth=0.6,
                        zorder=3)
    for i, g in enumerate(gids):
        ax.annotate(g, (hub[i], sem[i] + jit[i]),
                    textcoords="offset points", xytext=(6, 6), fontsize=7,
                    color="#555555")
    cb = fig.colorbar(sc, ax=ax, pad=0.02)
    cb.set_label("field_named (named Hits@3)")
    co = reg["coefficients"]
    ax.text(0.985, 0.03,
            f"exploratory regression field_named ~ density + hub + sem (n={reg['n_observations']})\n"
            f"R^2={reg['r_squared']:.3f}; "
            f"b_hub=+{co['hub_concentration']['coefficient']:.2f}"
            f" (p={co['hub_concentration']['p_value']:.2e}); "
            f"b_sem={co['real_semantics']['coefficient']:.2f}"
            f" (p={co['real_semantics']['p_value']:.4f})",
            transform=ax.transAxes, va="bottom", ha="right", fontsize=9,
            bbox=dict(boxstyle="round,pad=0.4", fc="#F7F4EF", ec="#CCCCCC"))
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["0 (synthetic structural)", "1 (real semantic)"])
    ax.set_ylim(-0.28, 1.28)
    ax.set_xlabel("hub_concentration")
    ax.set_ylabel("real_semantics")
    ax.grid(color="#E8E8E8", lw=0.6, zorder=0)
    ax.legend([plt.Line2D([], [], marker="o", ls="", color="#777777",
                          markeredgecolor="#444444", markersize=9),
               plt.Line2D([], [], marker="s", ls="", color="#777777",
                          markeredgecolor="#444444", markersize=9)],
              ["Family S (synthetic structural)", "Family L (real-semantic)"],
              loc="upper right", fontsize=10, framealpha=0.9)
    ax.set_title("Fig. 3: Division-of-labor scatter (hub_concentration x real_semantics, "
                 "colored by field_named)", fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_division_scatter_en.png", dpi=300)
    plt.close(fig)


# ================================================================ 图 4
def fig4():
    alphas = g7["temperature_knob"]["alphas"]
    graphs = g7["preregistered"]["graphs"]
    n_seed = g7["preregistered"]["seeds_per_temperature"]
    check("fig4", "预登记图数", len(graphs), 4)
    check("fig4", "per_graph 覆盖预登记图", sorted(g7["per_graph"]), sorted(graphs))
    check("fig4", "温度档数", len(alphas), 6)
    for g in graphs:
        temps = g7["per_graph"][g]["temperatures"]
        check(f"fig4:{g}", "温度档与 alphas 一致",
              sorted(t["alpha"] for t in temps.values()), sorted(alphas))
        check(f"fig4:{g}", "每档 seed 数",
              {t["n_seeds"] for t in temps.values()}, {n_seed})
        check(f"fig4:{g}", "seed 数 = 5", n_seed, 5)
    check("fig4", "verdict = mixed", g7["verdict"]["verdict"], "mixed")

    fig, axes = plt.subplots(2, 2, figsize=(12.5, 8.6), sharex=True)
    for ax, g in zip(axes.flat, graphs):
        pg = g7["per_graph"][g]
        temps = sorted(pg["temperatures"].values(), key=lambda t: t["alpha"])
        a = [t["alpha"] for t in temps]
        h = [t["hits_mean"] for t in temps]
        hs = [t["hits_std"] for t in temps]
        p = [t["phi_mean"] for t in temps]
        ps = [t["phi_std"] for t in temps]
        mf = pg["meanfield"]
        ax.errorbar(a, h, yerr=hs, marker="o", ms=5, lw=1.6, color=C_FIELD,
                    capsize=3, label="hit rate (dirichlet, mean±std over 5 seeds)",
                    zorder=3)
        ax.axhline(mf["hits"], ls="--", color=C_FIELD, lw=1.1,
                   label="mean-field hit rate (T=0)")
        ax.set_ylabel("named Hits@3", color=C_FIELD)
        ax.tick_params(axis="y", labelcolor=C_FIELD)
        ax.set_ylim(-0.05, max(max(h) + max(hs), mf["hits"]) * 1.35 + 0.05)
        ax2 = ax.twinx()
        ax2.errorbar(a, p, yerr=ps, marker="s", ms=5, lw=1.6, color=C_PHI,
                     capsize=3, label="terminal Phi (mean±std)", zorder=3)
        ax2.axhline(mf["phi"], ls=":", color=C_PHI, lw=1.1,
                    label="mean-field Phi (T=0)")
        ax2.set_ylabel("terminal Phi", color=C_PHI)
        ax2.tick_params(axis="y", labelcolor=C_PHI)
        ax.set_xscale("log")
        ax.set_xticks(alphas)
        ax.set_xticklabels([str(x) for x in alphas])
        d = g7["verdict"]["per_graph_direction"][g]
        ft = d["frontier_temps"]
        ax.set_title(f"{g} (frontier temps: {len(ft)}"
                     f"{': alpha=' + ', '.join(ft) if ft else ''})", fontsize=10.5)
        ax.grid(color="#ECECEC", lw=0.6, zorder=0)
        ax.set_xlabel("dirichlet concentration alpha (effective temperature: alpha->0 hot, alpha->inf cold)")
    handles, labels = axes.flat[0].get_legend_handles_labels()
    fig.legend(handles + [plt.Line2D([], [], marker="s", color=C_PHI, lw=1.6),
                          plt.Line2D([], [], ls=":", color=C_PHI, lw=1.1)],
               labels + ["terminal Phi (mean±std)", "mean-field Phi (T=0)"],
               loc="lower center", ncol=3, fontsize=9, frameon=False,
               bbox_to_anchor=(0.5, -0.005))
    fig.suptitle("Fig. 4: GT-7 temperature frontier per graph (dual axes: hit rate and Phi; "
                 "verdict = mixed)", fontsize=13)
    fig.tight_layout(rect=(0, 0.045, 1, 1))
    fig.savefig(OUT / "fig4_gt7_frontier_en.png", dpi=300)
    plt.close(fig)


# ================================================================ 图 5
def fig5():
    g4 = gt["GT4_price_of_anarchy"]
    frozen = g4["poa_per_graph"]           # 冻结 GT-4：17 有限 + 3 "Infinity"
    fv = g4["verdict"]
    finite = fv["poa_per_graph_finite"]
    check("fig5", "冻结有限值图数（论文口径 17）", len(finite), 17)
    check("fig5", "冻结 ∞ 图数（论文口径 3）", len(frozen) - len(finite),
          fv["n_poa_inf"])
    check("fig5", "冻结 ∞ 计数 = 3", fv["n_poa_inf"], 3)
    check("fig5", "中位 PoA（17 有限值图）",
          round(float(np.median(list(finite.values()))), 9),
          round(fv["median_poa"], 9))
    check("fig5", "族 L PoA<1 两图在案",
          {"L_historical_causality", "L_physics_concepts"}
          <= {g for g, v in finite.items() if v < 1}, True)

    # 按 GT-4 预登记公式（run_v20_gt.py: fm / max(random, degree)）对
    # corpus_eval 22 图机械复算；冻结 20 图必须逐值吻合，余下 2 图（族 L
    # 扩展图，冻结时未入 GT-4）以同公式补充、斜纹区分。
    recomputed = {}
    for g, arms in named.items():
        fm = arms["field_mean"]
        selfish = max(arms["random"], arms["degree"])
        if selfish > 0:
            recomputed[g] = fm / selfish
        else:
            recomputed[g] = float("inf") if fm > 0 else None
    check("fig5", "语料图数（22）", len(recomputed), 22)
    for g, v in frozen.items():
        rv = recomputed[g]
        if v == "Infinity":
            check(f"fig5:{g}", "冻结 ∞ 与复算一致", rv, float("inf"))
        else:
            check(f"fig5:{g}", "冻结值与复算一致",
                  round(rv, 9), round(v, 9))
    supplementary = sorted(set(recomputed) - set(frozen))
    check("fig5", "冻结外补充图数", len(supplementary), 2)
    check("fig5", "总条形数（全 22 图）", len(recomputed), 22)

    bars = []  # (gid, value or inf, kind)  kind ∈ {frozen, supp, inf}
    finite_all = sorted(
        [(g, v) for g, v in recomputed.items() if np.isfinite(v)],
        key=lambda t: -t[1])
    for g, v in finite_all:
        bars.append((g, v, "frozen" if g in frozen else "supp"))
    inf_gs = sorted(g for g, v in recomputed.items() if v == float("inf"))
    for g in inf_gs:
        bars.append((g, float("inf"), "inf"))

    fig, ax = plt.subplots(figsize=(13.0, 5.8))
    top = max(v for _, v, k in bars if np.isfinite(v))
    inf_h = top * 1.18
    for i, (g, v, k) in enumerate(bars):
        fam = per_graph_meta[g]["family"]
        col = C_L if fam == "L" else C_S
        if k == "inf":
            ax.bar(i, inf_h, 0.62, color=C_INF, hatch="//",
                   edgecolor="#888888", zorder=3)
            ax.text(i, inf_h + 0.05, "∞", ha="center", fontsize=13,
                    color="#666666")
        elif k == "supp":
            ax.bar(i, v, 0.62, color=col, alpha=0.45, hatch="..",
                   edgecolor="#555555", zorder=3)
        else:
            ec = "#B03030" if v < 1 else "#444444"
            lw = 1.8 if v < 1 else 0.5
            ax.bar(i, v, 0.62, color=col, edgecolor=ec, linewidth=lw,
                   zorder=3)
    ax.axhline(fv["pass_threshold"], ls="--", color="#7A7A7A", lw=1.2)
    ax.text(15.5, fv["pass_threshold"] - 0.18,
            f"pre-registered pass line {fv['pass_threshold']}", ha="center", fontsize=9,
            color="#555555")
    ax.axhline(fv["median_poa"], ls="-.", color="#8C7B3C", lw=1.2)
    ax.text(15.5, fv["median_poa"] + 0.05,
            f"frozen median over 17 finite graphs {fv['median_poa']:.3f}", ha="center",
            fontsize=9, color="#8C7B3C")
    ax.set_xticks(range(len(bars)))
    ax.set_xticklabels([g for g, _, _ in bars], rotation=55, ha="right",
                       fontsize=8.5)
    ax.set_ylabel("ECR = field_mean / max(random, degree) (named Hits@3; distribution-level, not classical worst-case PoA)")
    ax.set_ylim(0, inf_h * 1.18)
    ax.grid(**GRID)
    handles = [
        plt.Rectangle((0, 0), 1, 1, fc=C_S, ec="#444444", lw=0.5),
        plt.Rectangle((0, 0), 1, 1, fc=C_L, ec="#444444", lw=0.5),
        plt.Rectangle((0, 0), 1, 1, fc=C_S, ec="#B03030", lw=1.8),
        plt.Rectangle((0, 0), 1, 1, fc=C_INF, ec="#888888", hatch="//"),
        plt.Rectangle((0, 0), 1, 1, fc=C_L, ec="#555555", alpha=0.45,
                      hatch=".."),
    ]
    ax.legend(handles, [
        "Family S (frozen GT-4; one of 17 finite graphs)",
        "Family L (frozen GT-4)",
        "red box: ECR<1 (negative coordination; two family-L graphs in frozen set)",
        f"ECR=inf (selfish arm named=0 while field>0; {fv['n_poa_inf']} graphs counted separately)",
        "dotted hatch: 2 family-L extension graphs outside the frozen set (same pre-registered formula, excluded from median)",
    ], loc="upper right", fontsize=8.5, framealpha=0.92)
    ax.set_title("Fig. 5: Distribution of the empirical coordination ratio (ECR) — all 22 graphs (incl. ECR<1 graphs and inf count; not classical worst-case PoA)",
                 fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT / "fig5_poa_distribution_en.png", dpi=300)
    plt.close(fig)


# ================================================================ main
if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    print("== 数据点计数自检台账 ==")
    for fig, item, obs, exp, ok in CHECKS:
        print(f"[{'PASS' if ok else 'FAIL'}] {fig} | {item} | "
              f"observed={obs!r} | expected={exp!r}")
    print(f"共 {len(CHECKS)} 项自检全部通过。")
    for p in sorted(OUT.glob("fig*.png")):
        print(p, p.stat().st_size, "bytes")
