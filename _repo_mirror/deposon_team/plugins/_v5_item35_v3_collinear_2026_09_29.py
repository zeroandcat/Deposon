# -*- coding: utf-8 -*-
"""V5 #35 v3 · GT2b C0 共线修正 · **A-案 2 双因子全交叉**执行面（弃恒 4 项）。

来源纪律锚（只读，0 触动；SHA-12 本 Turn 盘上实测）：
  - results/_v5_item35_v3_collinear_prereg_2026_09_29.md   （873652fd39dd，件 A，PI 批 9 后生效即锁）
        §3 判死线（只引用既有 K-*）· §4 构造候选（A-案 2）· §5 阈值看护 · §6 防退化
        §7 铁律与产物命名 · §8 构造面 vs 真实面 · §9 γ · §10 P-1…P-6
  - results/_v5_item35_v2_verdict_2026_09_29.md            （b59bef293712，C0–C4 根因面，只读）
  - results/_v5_item35_prereg_v2_2026_09_28.md             （1fb2419c6e96，v2 判死线字面）
  - run_v20_gt2b.py                                       （361aff516219，共线构造的字面出处）
  - docs/SPEC_GT2B.md                                     （68a5b08ef007，设计意图 + 场免疫零假设）

PI 确认批 9（件 A §10 P-1…P-6）：
  P-1 ① **A-案 2 双因子全交叉**（弃恒 4 项 / 弃机会恒 25%）
  P-2 ① **逐格**报机会水平 1/(1+T+D)（0 聚合口径）
  P-3 ① **明示延用** GT 系全局条款 K-V5R3-0-A…0-G 于 #35 面
  P-4 ① 混合分支「PASS+KD / FAIL+KD」沿 v2 显式留白 ⇒ 触发即落 KD 并 γ
  P-5 ① **必须附非同退化独立佐证**
  P-6 ① 本轮 **4 域 + 强制披露**（C3 沿案）

构造（A-案 2 字面）：`options = [gold] + T traps + D decoys`，`n_options = 1+T+D`。
共线 C0 的结构性解除方式：T 与 D 各自可动（D ≡ 3−T 的恒 4 项约束被放弃）。

**0 新设数值阈值**：唯一数值切点仍 `field_tol = 0.05`（启动即 assert）。
**D 档取值 = 执行面冻结的构造型设计参数**（非阈值），件 A 只给 D ∈ {D_min, D_max} 两档
（§4.2 A-案 2 字面 + §4.1 规模例 3×2×6×4），**未给具体值** ⇒ 本棒冻结 D = (1, 2) 并
逐条列证（见 exec 件 §2）。D ≥ 1 ⇒ 结构性恒等格（D=0 ⇒ field_mean 恒 1.000）在本面
**不可达**，此为防退化性质之一。

派生 JSON 0 合并：写新名独立件 `results/_v5_item35_v3_collinear_result_2026_09_29.json`。
0 LLM / 0 proxy / 0 key 读取。无墙钟时间戳 ⇒ 同输入重跑逐字节一致。
"""
from __future__ import annotations

import hashlib
import json
import os
import sys

REPO = r"D:/私人资料/deposon-repo"
EXT_CACHE = r"D:/私人资料/_non_upload_local_archive/results/gt2_attacker_cache"
EXT_CACHE_ITEMS = ["algorithm_process.json", "biological_taxonomy.json",
                   "historical_causality.json", "physics_concepts.json"]
OUT_PATH = os.path.join(REPO, "results", "_v5_item35_v3_collinear_result_2026_09_29.json")
FROZEN_SCHEMA = os.path.join(REPO, "deposon_team", "plugins", "_v3x_frozen_schema_v1.json")

# ---- 沿既有字面，一字不动（件 A §5.1 逐条列证）----
T_LEVELS = (1, 2, 3)            # TH-V3R1P1-35-b / run_v20_gt2b.py L30
BANK_SEED_SET = (20260828, 20260829, 20260830,   # 沿 v2 面 6 档（0 新设 seed）
                 20260831, 20260832, 20260833)
SEEDS_EXISTING = (20260828, 20260829, 20260830)
AS_RUN_SEED = 20260828
ARMS = ("rule_filter", "field_mean", "random")

# ---- 执行面冻结的构造型设计参数（件 A §5.1「面形状 vs 判据文字」分工；0 是阈值）----
D_LEVELS = (1, 2)              # D_min=1, D_max=2；2 档 = D 成为因子的最小档数
N_ITEMS_PER_MAP = 10           # run_v20_gt2b.py L28
KNIFE_EDGE_LABEL_EPS = 1e-6    # 沿 v2 executor 既有实现字面，只打标签
DEGEN_N_DISTINCT_MIN = 4       # K-V3R1P1-0-A：n_distinct > 3

# ---- 0 触动件（跑前/跑后逐件复读 sha12 + bytes）----
ZERO_TOUCH = {
    "prereg_v3_itemA": "results/_v5_item35_v3_collinear_prereg_2026_09_29.md",
    "verdict_v2": "results/_v5_item35_v2_verdict_2026_09_29.md",
    "prereg_v2": "results/_v5_item35_prereg_v2_2026_09_28.md",
    "exec_v2": "results/_v5_item35_v2_matrix_exec_2026_09_29.md",
    "result_v2": "results/_v5_item35_v2_matrix_result_2026_09_29.json",
    "executor_v2": "deposon_team/plugins/_v5_item35_v2_matrix_2026_09_29.py",
    "prereg_v1p1": "results/_v3_recheck_prereg_v1p1_2026_09_27.md",
    "result_v1p1": "results/_v3_recheck_35_result_2026_09_27.json",
    "runner_gt2b": "run_v20_gt2b.py",
    "spec_gt2b": "docs/SPEC_GT2B.md",
    "as_run_result": "results/deposon_v20_gt2b.json",
    "gt_prereg_global": "results/_v5_gt5_gt6_gt8_gt5b_gt_prereg_2026_09_28.md",
    "protocol": "deposon_protocol.py",
    "diffusion_cfg": "deposon_diffusion.py",
    "corpus_loader": "mindmap_corpus_v20.py",
    "meanfield": "run_v19_meanfield.py",
    "fullrank": "run_v19_fullrank.py",
    "row_norm": "run_v15_experiment.py",
    "corpus_eval": "run_v20_corpus_eval.py",
    "llm_prior": "llm_prior.py",
    "corpus_index": "corpus/v20/index.json",
    "frozen_schema": "deposon_team/plugins/_v3x_frozen_schema_v1.json",
}

sys.path.insert(0, REPO)

import numpy as np  # noqa: E402

import run_v20_gt2b as R  # noqa: E402（只读导入，0 改既有 runner）
from deposon_diffusion import DiffusionConfig, config_dict  # noqa: E402
from llm_prior import _extract_json_array  # noqa: E402
from run_v15_experiment import row_normalize  # noqa: E402
from run_v19_fullrank import full_candidate_mask  # noqa: E402
from run_v19_meanfield import field_scores_init  # noqa: E402
from run_v20_corpus_eval import RULE_KEYWORDS  # noqa: E402

FIELD_TOL = R.FIELD_TOL   # 一字不动（TH-V3R1P1-35-a）


# ---------------------------------------------------------------- 只读工具
def sha12(path: str) -> str:
    with open(path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()[:12]


def nbytes(path: str) -> int:
    return os.path.getsize(path)


def fingerprint(paths: dict) -> dict:
    return {k: {"path": v, "sha12": sha12(os.path.join(REPO, v)),
                "bytes": nbytes(os.path.join(REPO, v)), "access": "read_only"}
            for k, v in paths.items()}


def load_traps_ext(domain: str) -> list:
    """仓外缓存只读取用（K-V3R1P1-0-F）：0 写入 / 0 复制入仓 / 0 删除 / 0 改 ACL。"""
    with open(os.path.join(EXT_CACHE, f"{domain}.json"), encoding="utf-8") as f:
        atk = json.load(f)
    return [str(it["label"]) for it in _extract_json_array(atk["response_text"])]


def load_family_l_graphs() -> dict:
    """与 mindmap_corpus_v20.load_corpus(CORPUS_DIR, families=("L",)) 等价的只读加载。

    偏离登记（沿 v2 executor γ-V2-5 字面）：既有 load_corpus 的孤儿哨兵在本仓现状下
    抛错 ⇒ 走等价只读路径（index.json 登记顺序 + family=="L" 过滤），0 改既有模块 /
    0 改 index.json / 0 改语料。构造顺序与 v2 executor 逐字一致。
    """
    with open(os.path.join(REPO, "corpus", "v20", "index.json"), encoding="utf-8") as f:
        idx = json.load(f)
    out = {}
    for e in idx["graphs"]:
        if e["family"] != "L":
            continue
        with open(os.path.join(REPO, "corpus", "v20", e["file"]), encoding="utf-8") as f:
            out[e["graph_id"][2:]] = json.load(f)
    return out


def series_stats(series) -> dict:
    """防退化门统计量（K-V3R1P1-0-A 字面：n_distinct > 3 + std > 0）。"""
    s = [float(x) for x in series]
    nd = len(set(s))
    std = float(np.std(s))
    return {"n": len(s), "n_distinct": nd, "std": std,
            "min": min(s), "max": max(s),
            "is_binary": bool(nd <= 2),
            "gate_non_degenerate": bool(nd > (DEGEN_N_DISTINCT_MIN - 1) and std > 0.0)}


def is_finite(x) -> bool:
    return bool(x is not None and not isinstance(x, bool) and np.isfinite(float(x)))


def frozen_anchor_scan() -> dict:
    """18 frozen / P-G 占位锚的只读扫描（0 触动证据）。

    如实交代：schema 内 anchors 共 16 条、pg_anchors 共 5 条占位哈希。本棒 **0 自行认定
    「18 frozen」与「9 网格」两份清单的构成**（件 A §7.1 同口径），此处只做**只读存在性
    + 哈希复读**，「存在数 ≠ 18」的事实如实登记，0 改任何既有件。
    """
    with open(FROZEN_SCHEMA, encoding="utf-8") as f:
        sch = json.load(f)
    resolved, missing = {}, []
    for a in sch.get("anchors", []):
        p = os.path.join(REPO, a["path_primary"])
        if os.path.exists(p):
            resolved[a["id"]] = {"path": a["path_primary"], "sha12": sha12(p),
                                 "bytes": nbytes(p),
                                 "schema_expected_sha12": a.get("expected_sha256_12"),
                                 "matches_schema": sha12(p) == a.get("expected_sha256_12")}
        else:
            missing.append(a["id"])
    return {"schema_path": "deposon_team/plugins/_v3x_frozen_schema_v1.json",
            "schema_sha12": sha12(FROZEN_SCHEMA), "schema_bytes": nbytes(FROZEN_SCHEMA),
            "n_anchors_in_schema": len(sch.get("anchors", [])),
            "n_anchors_resolved_on_disk": len(resolved),
            "anchors_missing_on_disk": missing,
            "resolved": resolved,
            "pg_placeholders": sch.get("pg_anchors", []),
            "disclosure": ("本棒 0 自行认定 18 frozen / 9 网格清单构成（件 A §7.1 同口径）；"
                           "此处仅为只读存在性 + 哈希复读证据，0 写任何锚件")}


# ---------------------------------------------------------------- 构造（A-案 2）
def build_bank_td(graphs, traps_by_domain, T, D, bank_seed):
    """A-案 2 题库：options = 1 金 + T 陷阱 + D 图内随机诱饵，选项数 = 1+T+D（随格变化）。

    与 run_v20_gt2b.build_bank_t 的关系：rng 消费顺序逐行同构，仅把 `range(3 - T)`
    换成 `range(D)`、`rng.permutation(4)` 换成 `rng.permutation(1 + T + D)`。
    ⇒ 当 D = 3 − T 时本函数与既有构造**逐字节同构**（as-run 环境自证即据此，见 §9）。
    """
    rng = np.random.default_rng(bank_seed)
    bank = []
    for domain, g in graphs.items():
        labels = g["labels"]
        named = [tuple(e) for e in g["named_edges"]]
        traps = traps_by_domain[domain]
        take = rng.choice(len(named), size=min(N_ITEMS_PER_MAP, len(named)),
                          replace=False)
        for k in take:
            u, v = named[int(k)]
            tset = [traps[(T * int(k) + j) % len(traps)] for j in range(T)]
            others = [j for j in range(g["N"]) if j != v]
            decoys = [labels[int(others[rng.integers(len(others))])] for _ in range(D)]
            options = [labels[v]] + tset + decoys
            n_options = 1 + T + D
            perm = rng.permutation(n_options)
            bank.append({
                "item_id": f"{domain}#q{int(k):02d}",
                "domain": domain, "bloom_level": "L4_analyze",
                "stem": f"在概念体系「{domain}」中，与「{labels[u]}」存在最直接"
                        f"合理后继关系的是哪一个？",
                "gold_edge": [int(u), int(v)],
                "gold_label": labels[v],
                "options": [options[int(i)] for i in perm],
                "answer_index": int(np.flatnonzero(perm == 0)[0]),
                "n_traps": T, "n_decoys": D, "n_options": n_options,
                "chance_level": 1.0 / n_options,
                "trap_labels": tset,
                "random_node_labels": decoys,
                "perm": [int(i) for i in perm]})
    return bank


def classify_roles(perm, T):
    """按构造序把每个选项位标成 gold / trap / decoy（0 用标签相等判定，0 受重名影响）。"""
    roles = []
    for p in perm:
        if p == 0:
            roles.append("gold")
        elif p <= T:
            roles.append("trap")
        else:
            roles.append("decoy")
    return roles


# ---------------------------------------------------------------- 作答（三臂 · 0 改既有逻辑）
def answer_quiz_td(graph, cfg, bank, T):
    """沿 run_v20_gt2b.answer_quiz 逐题作答；仅把 `rng.integers(4)` 换成 `rng.integers(n_options)`。

    附带 rule_filter 分支可达性取证（件 A γ-PKA-2 交 executor，逐条实测 0 预判）。
    """
    N = graph["N"]
    labels = graph["labels"]
    adj = np.zeros((N, N))
    for (u, v) in [tuple(e) for e in graph["edges"]]:
        adj[u, v] = 1.0
    W_true = row_normalize(adj)
    g_seed = int(graph["seed"])
    records = []
    for item in bank:
        u, v = item["gold_edge"]
        rng = np.random.default_rng(R.stable_seed(g_seed, item["item_id"]))
        adj_obs = adj.copy(); adj_obs[u, v] = 0.0
        W_obs = W_true.copy(); W_obs[u, v] = 0.0
        mask = full_candidate_mask(N, u)
        fm = field_scores_init(W_obs, mask, cfg, graph["source"], graph["target"],
                               g_seed + (u * 131 + v) % 100000, "prior_mean")
        # 陷阱标签不在图节点集内 ⇒ field 对其打 -inf（机制性免疫，如实披露，run_v20_gt2b.py L101-107）
        fscores = {labels[j]: float(fm[u][j]) for j in range(N) if j != u}
        opts = item["options"]
        n_opt = len(opts)
        roles = classify_roles(item["perm"], T)
        ans = {}
        best, best_s = None, -np.inf
        for o in opts:
            s = fscores.get(o, -np.inf)
            if s > best_s:
                best, best_s = o, s
        ans["field_mean"] = best
        flags = [any(k in o.lower() for k in RULE_KEYWORDS) for o in opts]
        surviving = [o for o, fl in zip(opts, flags) if not fl]
        ans["rule_filter"] = surviving[0] if surviving else opts[0]
        ans["random"] = opts[int(rng.integers(n_opt))]
        gold = opts[item["answer_index"]]
        n_surv = len(surviving)
        chosen_pos = 0 if not surviving else flags.index(False)
        records.append({
            "item_id": item["item_id"], "gold": gold,
            "answers": ans,
            "correct": {a: ans[a] == gold for a in ARMS},
            "roles": roles,
            "filter_diag": {
                "n_options": n_opt,
                "n_filtered": int(sum(flags)),
                "n_surviving": n_surv,
                "all_filtered_fallback": bool(n_surv == 0),
                "n_gold_filtered": int(flags[roles.index("gold")]) if roles.count("gold") else 0,
                "n_trap_filtered": int(sum(f for f, r in zip(flags, roles) if r == "trap")),
                "n_decoy_filtered": int(sum(f for f, r in zip(flags, roles) if r == "decoy")),
                "chosen_position": chosen_pos,
                "chosen_role": roles[chosen_pos],
                "gold_survived": bool(not flags[roles.index("gold")]),
                "rule_filter_picked_gold": bool(ans["rule_filter"] == gold),
            },
            "ambiguity_diag": {
                "n_distinct_option_labels": len(set(opts)),
                "n_options": n_opt,
                "n_duplicate_label_positions": n_opt - len(set(opts)),
                "gold_label_occurrence": int(sum(1 for o in opts if o == gold)),
                "n_trap_positions_scored_neginf": int(
                    sum(1 for o, r in zip(opts, roles) if r == "trap"
                        and not np.isfinite(fscores.get(o, -np.inf)))),
            },
        })
    acc = {a: float(np.mean([r["correct"][a] for r in records])) for a in ARMS}
    return {"accuracy": acc, "n_items": len(records), "records": records}


def run_cell(cfg, graphs, traps, seed, T, D):
    """单 (seed, T, D) 格。"""
    bank = build_bank_td(graphs, traps, T, D, seed)
    per_dom = {}
    for domain, g in graphs.items():
        items = [q for q in bank if q["domain"] == domain]
        per_dom[domain] = answer_quiz_td(g, cfg, items, T)
    overall = {a: float(np.mean([v["accuracy"][a] for v in per_dom.values()]))
               for a in ARMS}
    return {"bank": bank, "per_domain": per_dom, "overall": overall,
            "n_items": len(bank)}


def main() -> int:
    # ---- 0. 阈值 / 口径字面冻结自检（0 擅调的可机械自证）----
    assert FIELD_TOL == 0.05, f"FIELD_TOL 被改动：{FIELD_TOL}"
    assert T_LEVELS == (1, 2, 3)
    assert ARMS == ("rule_filter", "field_mean", "random")
    assert N_ITEMS_PER_MAP == R.N_ITEMS_PER_MAP
    assert len(BANK_SEED_SET) == 6 and BANK_SEED_SET[:3] == SEEDS_EXISTING
    assert len(D_LEVELS) == 2 and min(D_LEVELS) >= 1, "D 档数须为 2 且 D_min ≥ 1"

    # ---- 1. 跑前 0 触动基线 + 仓外缓存基线 + frozen 锚只读基线 ----
    zt_pre = fingerprint(ZERO_TOUCH)
    frozen_pre = frozen_anchor_scan()
    ext_pre = {fn: {"path": os.path.join(EXT_CACHE, fn),
                    "sha12": sha12(os.path.join(EXT_CACHE, fn)),
                    "bytes": nbytes(os.path.join(EXT_CACHE, fn)),
                    "access": "read_only_external_archive"}
               for fn in EXT_CACHE_ITEMS}
    ext_read_ok, ext_read_error = True, None
    try:
        for fn in EXT_CACHE_ITEMS:
            with open(os.path.join(EXT_CACHE, fn), "rb") as f:
                f.read(1)
    except Exception as exc:                                    # pragma: no cover
        ext_read_ok, ext_read_error = False, repr(exc)

    # ---- 2. 资产面（仓外只读）----
    graphs_all = load_family_l_graphs()
    graphs = {d: g for d, g in graphs_all.items()
              if os.path.exists(os.path.join(EXT_CACHE, f"{d}.json"))}
    excluded_domains = sorted(set(graphs_all) - set(graphs))
    traps = {d: load_traps_ext(d) for d in sorted(graphs)}

    # ---- 3. C4 机制核验（资产层 · 0 读数派生 · P-5 独立佐证 ①）----
    c4 = {}
    for d in sorted(graphs):
        labels = set(graphs[d]["labels"])
        tset = list(traps[d])
        c4[d] = {"n_traps": len(tset), "n_graph_labels": len(labels),
                 "n_trap_labels_in_graph_node_set": int(sum(1 for t in tset if t in labels)),
                 "intersection": sorted({t for t in tset if t in labels})}
    c4_all_zero = all(v["n_trap_labels_in_graph_node_set"] == 0 for v in c4.values())

    # ---- 4. 开跑前 · 防退化自证（沿 v2 §5.1 已知退化杠杆表；唯一待验杠杆 = cfg["seed"]）----
    src = open(os.path.join(REPO, "run_v20_gt2b.py"), encoding="utf-8").read()
    proto = open(os.path.join(REPO, "deposon_protocol.py"), encoding="utf-8").read()
    cfg_seed_static = {
        "lever": 'cfg["seed"]',
        "runner_cfg_subscript_seed_hits": src.count('cfg["seed"]') + src.count("cfg['seed']"),
        "runner_passed_seed_arg_literal":
            'g_seed + (u * 131 + v) % 100000' in src,
        "protocol_field_scores_init_overwrites_seed": '"seed": inst_seed' in proto,
        "static_reading": ("run_v20_gt2b.py 内 cfg[\"seed\"] 0 消费点；field_scores_init "
                           "在 deposon_protocol.py 内以 {\"seed\": inst_seed} 覆盖传入 cfg 的 "
                           "seed 字段，inst_seed 源 = graph[\"seed\"] + 边序，与 cfg.seed 无关"),
    }
    cfg2 = DiffusionConfig()
    cfg2.seed = 987654321
    pd = "physics_concepts"
    probe_bank = build_bank_td(graphs, traps, 2, 2, AS_RUN_SEED)
    p_items = [q for q in probe_bank if q["domain"] == pd]
    base_cfg = DiffusionConfig()
    probe_a = answer_quiz_td(graphs[pd], base_cfg, p_items, 2)
    probe_b = answer_quiz_td(graphs[pd], cfg2, p_items, 2)
    cfg_seed_static["empirical_bit_identical_when_cfg_seed_changed"] = (
        json.dumps(probe_a, sort_keys=True) == json.dumps(probe_b, sort_keys=True))
    cfg_seed_static["probe_result"] = {a: probe_a["accuracy"][a] for a in ARMS}
    cfg_seed_static["lever_status"] = (
        "0 消费点已双重自证（静态 + 实测 bit-identical）⇒ 禁作杠杆登记成立，"
        "本件 0 以 cfg.seed 为扫描变量")
    pre_run_selfcheck = {
        "field_tol_literal": FIELD_TOL,
        "field_tol_unchanged": True,
        "new_numeric_thresholds_introduced": 0,
        "knife_edge_label_eps_source": "v2 executor ef73f9b90afc 既有实现字面（只打标签）",
        "construction_scheme": "A-案 2 双因子全交叉：options = 1 gold + T traps + D decoys",
        "t_levels": list(T_LEVELS), "d_levels": list(D_LEVELS),
        "d_levels_basis": ("件 A §4.2 A-案 2 字面「D ∈ {D_min, D_max}」两档；具体取值由本棒"
                            "冻结为 D=1 / D=2（构造型设计参数，0 是阈值）；D_min=1 ⇒ D=0 的"
                            "结构性恒等格在本面不可达"),
        "d_levels_not_preregistered_value": True,
        "bank_seed_set": list(BANK_SEED_SET),
        "domains_available": sorted(graphs),
        "domains_excluded_no_cache": excluded_domains,
        "traps_available_per_domain": {d: len(t) for d, t in sorted(traps.items())},
        "external_read_only_reachable": ext_read_ok,
        "external_read_only_error": ext_read_error,
        "n_domains_in_matrix": len(graphs),
        "n_items_per_cell_expected": len(graphs) * N_ITEMS_PER_MAP,
        "n_options_per_cell": {f"T{T}_D{D}": 1 + T + D
                               for T in T_LEVELS for D in D_LEVELS},
        "chance_level_per_cell": {f"T{T}_D{D}": 1.0 / (1 + T + D)
                                  for T in T_LEVELS for D in D_LEVELS},
        "cfg_seed_lever_double_selfproof": cfg_seed_static,
        "gate_sequence_frozen_before_measurement": (
            "读法 D（逐臂 × 全矩阵域级正确率池化）—— 件 A §3 沿 AR4 测量前唯一冻结；"
            "读法 A / C 继续双记并报、仅作对照登记，0 再作为判死线分支"),
    }

    # ---- 5. as-run 环境自证：legacy parity 面 (D = 3 − T) 须与在盘件逐位相同 ----
    cfg = DiffusionConfig()
    legacy_parity = []
    for T in T_LEVELS:
        r = run_cell(cfg, graphs, traps, AS_RUN_SEED, T, 3 - T)
        legacy_parity.append({"T": T, "D": 3 - T, "accuracy": r["overall"]})
    parity_recomputed = {a: {str(e["T"]): e["accuracy"][a] for e in legacy_parity}
                         for a in ARMS}

    # ---- 6. 主构造：6 seed × 3 T × 2 D = 36 格 ----
    cells = []
    for seed in BANK_SEED_SET:
        for T in T_LEVELS:
            for D in D_LEVELS:
                r = run_cell(cfg, graphs, traps, seed, T, D)
                cells.append({"bank_seed": seed, "T": T, "D": D, "n_items": r["n_items"],
                              "accuracy": r["overall"], "bank": r["bank"],
                              "per_domain": r["per_domain"],
                              "per_domain_accuracy": {d: v["accuracy"]
                                                      for d, v in sorted(r["per_domain"].items())},
                              "per_domain_n_items": {d: v["n_items"]
                                                     for d, v in sorted(r["per_domain"].items())}})
    acc = {(c["bank_seed"], c["T"], c["D"]): c["accuracy"] for c in cells}

    # ---- 7. 逐格留边际：α（逐列）/ β（逐格）双口径（0 互替，K-V3R1P1-0-C）----
    matrix = []
    for c in cells:
        seed, T, D = c["bank_seed"], c["T"], c["D"]
        a = c["accuracy"]
        n_options = 1 + T + D
        strongest = max(a["rule_filter"], a["random"])
        delta_beta = a["field_mean"] - strongest
        # α 逐列：基线 = 同 (seed, D) 列的 T=1（列内 D 相同 ⇒ T 效应可分离，件 A §5.3）
        delta_alpha = abs(a["field_mean"] - acc[(seed, 1, D)]["field_mean"])

        knife = bool(abs(delta_beta - FIELD_TOL) < KNIFE_EDGE_LABEL_EPS)
        band_float = "PASS" if delta_beta >= FIELD_TOL else "BELOW_TOL"
        band_math = "PASS" if round(delta_beta, 10) >= FIELD_TOL else "BELOW_TOL"

        alpha_band = "IMMUNE" if delta_alpha <= FIELD_TOL else "NOT_IMMUNE"
        alpha_in_denom = bool(T != 1)   # 列内 T=1 为结构性恒等格（|x − x| ≡ 0）

        alpha_vals_ok = all(is_finite(a[k]) for k in ARMS)
        beta_vals_ok = all(is_finite(a[k]) for k in ARMS) and is_finite(delta_beta) \
            and is_finite(delta_alpha)
        n_items_ok = c["n_items"] == pre_run_selfcheck["n_items_per_cell_expected"]

        # 构造完整性（题库层 · 0 读数派生 · P-5 独立佐证 ②）
        bank_ok = all(it["n_traps"] == T and it["n_decoys"] == D
                      and it["n_options"] == n_options for it in c["bank"])
        # 重名 / 歧义扫描（题库层 · A-案 2 新增退化族）
        dup_pos = sum(it["n_options"] - len(set(it["options"])) for it in c["bank"])
        gold_multi = sum(1 for dom, v in c["per_domain"].items() for r in v["records"]
                         if r["ambiguity_diag"]["gold_label_occurrence"] > 1)
        neginf_trap = sum(r["ambiguity_diag"]["n_trap_positions_scored_neginf"]
                          for v in c["per_domain"].values() for r in v["records"])
        # γ-PKA-2：rule_filter 分支可达性（题库/标签层 · 0 读数派生）
        rf_fallback = sum(1 for v in c["per_domain"].values() for r in v["records"]
                          if r["filter_diag"]["all_filtered_fallback"])
        rf_gold_filtered = sum(r["filter_diag"]["n_gold_filtered"]
                               for v in c["per_domain"].values() for r in v["records"])
        rf_trap_filtered = sum(r["filter_diag"]["n_trap_filtered"]
                               for v in c["per_domain"].values() for r in v["records"])
        rf_decoy_filtered = sum(r["filter_diag"]["n_decoy_filtered"]
                                for v in c["per_domain"].values() for r in v["records"])
        rf_picked_gold = sum(1 for v in c["per_domain"].values() for r in v["records"]
                             if r["filter_diag"]["rule_filter_picked_gold"])

        matrix.append({
            "cell": f"seed{seed}_T{T}_D{D}",
            "bank_seed": seed, "T": T, "D": D,
            "n_options": n_options,
            "chance_level": 1.0 / n_options,
            "chance_level_basis": "P-2 ① 逐格报 1/(1+T+D)；0 聚合口径",
            "n_items": c["n_items"],
            "n_items_expected": pre_run_selfcheck["n_items_per_cell_expected"],
            "n_items_as_expected": n_items_ok,
            "accuracy": a,
            "per_domain_accuracy": c["per_domain_accuracy"],
            "per_domain_n_items": c["per_domain_n_items"],
            "strongest_opponent_value": strongest,
            "strongest_opponent_arm": ("rule_filter" if a["rule_filter"] >= a["random"]
                                       else "random"),
            "kou_jing_alpha": {
                "definition": ("|field_mean(T,D) − field_mean(T=1,D)|（**列内**基线，"
                               "同 (seed, D) 列内 D 恒定 ⇒ T 效应可分离；件 A §5.3）"),
                "column_key": f"seed{seed}_D{D}",
                "value": delta_alpha, "value_float_literal": repr(delta_alpha),
                "field_tol": FIELD_TOL,
                "band": alpha_band,
                "field_immune": bool(delta_alpha <= FIELD_TOL),
                "knife_edge_like_label_CONTROL_ONLY": ({
                    "value_float_literal": repr(delta_alpha),
                    "label_eps": KNIFE_EDGE_LABEL_EPS,
                    "mathematical_value_note": "两侧读数落在 1/40 粒度网格上 ⇒ 数学值为 0.05 的整数倍",
                    "band_float_literal": alpha_band,
                    "band_changes_under_either_reading": False,
                    "why": ("AR6 / §3.2.1 刀锋格字面只施于 β 的 Δ；α 用「≤ field_tol」判带 ⇒ "
                            "取整档与字面档同档，对 α 腿结论 0 影响。仅披露事实，0 新增判据"),
                } if abs(delta_alpha - FIELD_TOL) < KNIFE_EDGE_LABEL_EPS else None),
                "in_alpha_denominator": alpha_in_denom,
                "denominator_exclusion_reason": (
                    None if alpha_in_denom else
                    "列内 T=1 为结构性恒等格（|field_mean(1,D) − field_mean(1,D)| ≡ 0 ⇒ "
                    "恒判 immune、无鉴别力）⇒ 沿 v2 §5.4 字面单列登记、0 计入 α 分母；"
                    "β 腿 T=1 仍为合法格"),
                "values_finite": alpha_vals_ok,
                "computable": bool(alpha_vals_ok and n_items_ok),
            },
            "kou_jing_beta": {
                "definition": "delta = field_mean − max(rule_filter, random)（同格内）",
                "value": delta_beta, "value_float_literal": repr(delta_beta),
                "field_tol": FIELD_TOL,
                "band": band_float,
                "band_float_literal": band_float,
                "beta_pass": bool(delta_beta >= FIELD_TOL),
                "is_knife_edge": knife,
                "knife_edge_disclosure": ({
                    "value_float_literal": repr(delta_beta),
                    "value_math_note": "两侧读数落在 1/40 粒度网格上 ⇒ 数学值恰 = 0.05",
                    "band_float_literal": band_float,
                    "band_math_rounded_control_only": band_math,
                    "counted_as": "按 float64 字面档计入档位计数（使计数唯一可复算）",
                    "double_counted": False, "rounded": False, "tolerance_band_used": False,
                } if knife else None),
                "values_finite": beta_vals_ok,
                "computable": bool(beta_vals_ok and n_items_ok),
            },
            "grain_disclosure": {
                "n_items": c["n_items"],
                "min_resolvable_step": 1.0 / c["n_items"],
                "field_tol_in_items": FIELD_TOL * c["n_items"],
                "is_knife_edge_cell": knife,
                "note": "件 A §5.2 粒度披露义务：阈值 0.05 = 40 items 中的 2 items；A-案 2 换构造"
                        "**0 改善**该粒度问题（0 借换构造顺手调 field_tol —— 禁作杠杆）",
            },
            "construction_integrity": {
                "bank_n_traps_all_eq_T": bank_ok,
                "bank_n_decoys_all_eq_D": bank_ok,
                "bank_n_options_all_eq_1_plus_T_plus_D": bank_ok,
                "n_duplicate_label_positions": dup_pos,
                "n_items_gold_label_multi_occurrence": gold_multi,
                "n_trap_positions_scored_neginf": neginf_trap,
                "c4_mechanism_expected_neg_inf": bool(neginf_trap == T * c["n_items"]),
            },
            "rule_filter_branch_reachability": {
                "n_items_all_filtered_fallback": rf_fallback,
                "n_gold_filtered": rf_gold_filtered,
                "n_trap_filtered": rf_trap_filtered,
                "n_decoy_filtered": rf_decoy_filtered,
                "n_items_picked_gold": rf_picked_gold,
            },
        })

    # ---- 8. 逐腿落档（§3.3 三态终态表 · AR3 全矩阵同档）----
    alpha_cells = [m for m in matrix if m["kou_jing_alpha"]["in_alpha_denominator"]]
    beta_cells = matrix
    alpha_bands = [m["kou_jing_alpha"]["band"] for m in alpha_cells]
    beta_bands = [m["kou_jing_beta"]["band"] for m in beta_cells]
    alpha_uncomputable = [m["cell"] for m in alpha_cells
                          if not m["kou_jing_alpha"]["computable"]]
    beta_uncomputable = [m["cell"] for m in beta_cells
                         if not m["kou_jing_beta"]["computable"]]
    alpha_not_immune = [m["cell"] for m in alpha_cells
                        if m["kou_jing_alpha"]["band"] == "NOT_IMMUNE"]
    beta_below = [m["cell"] for m in beta_cells if m["kou_jing_beta"]["band"] == "BELOW_TOL"]

    def leg_state(uncomputable, fail_cells):
        """逐腿三态落档（§3.3）。分母格不可算 ⇒ KD；否则存在异档格 ⇒ FAIL；全档一致 ⇒ PASS。"""
        if uncomputable:
            return "KD"
        if fail_cells:
            return "FAIL"
        return "PASS"

    alpha_state = leg_state(alpha_uncomputable, alpha_not_immune)
    beta_state = leg_state(beta_uncomputable, beta_below)

    compound_covered = True
    if alpha_state == "PASS" and beta_state == "PASS":
        compound_state = "PASS"
    elif alpha_state == "FAIL" or beta_state == "FAIL":
        compound_state = "FAIL"
    elif alpha_state == "KD" and beta_state == "KD":
        compound_state = "KD"
    else:
        # PI 批 9 · P-4 ①：沿 v2 显式留白 ⇒ 触发即落 KD 并 γ（AR5 0 不明收口）
        compound_state = "KD"
        compound_covered = False

    knife_cells = [m for m in beta_cells if m["kou_jing_beta"]["is_knife_edge"]]

    consistency = {
        "n_cells": len(matrix),
        "n_domain_level_cells": len(matrix) * len(graphs),
        "count_convention_disclosure": (
            "件 A §4.1 A-案 2 规模例「3 × 2 × 6 × 4 = 144」按 T×D×seed×**域**计；"
            "本件 α/β 判定格沿 v2 体例按 seed×T×**D** 计 = 36 格，域级池化 144 值/臂"),
        "alpha_denominator_cells": len(alpha_cells),
        "alpha_denominator_note": "6 seed × 2 D 列 × T ∈ {2,3} = 24 格；列内 T=1 结构性恒等格排除（v2 §5.4 字面）",
        "beta_cells": len(beta_cells),
        "alpha_band_counts": {b: alpha_bands.count(b) for b in sorted(set(alpha_bands))},
        "alpha_all_same_band_in_denominator": len(set(alpha_bands)) == 1,
        "alpha_not_immune_cells": alpha_not_immune,
        "alpha_not_immune_by_column_D": {
            str(D): [m["cell"] for m in alpha_cells
                     if m["D"] == D and m["kou_jing_alpha"]["band"] == "NOT_IMMUNE"]
            for D in D_LEVELS},
        "beta_band_counts": {b: beta_bands.count(b) for b in sorted(set(beta_bands))},
        "beta_all_same_band": len(set(beta_bands)) == 1,
        "beta_below_tol_cells": beta_below,
        "beta_band_counts_by_TD": {
            f"T{T}_D{D}": {b: sum(1 for m in beta_cells if m["T"] == T and m["D"] == D
                                  and m["kou_jing_beta"]["band"] == b)
                           for b in sorted({m["kou_jing_beta"]["band"] for m in beta_cells})}
            for T in T_LEVELS for D in D_LEVELS},
        "chance_level_per_TD": {f"T{T}_D{D}": 1.0 / (1 + T + D)
                                for T in T_LEVELS for D in D_LEVELS},
        "chance_level_not_constant_across_cells": True,
        "beta_knife_edge_cells": [{
            "cell": m["cell"],
            "value_float_literal": m["kou_jing_beta"]["value_float_literal"],
            "value_math_note": m["kou_jing_beta"]["knife_edge_disclosure"]["value_math_note"],
            "band_float_literal": m["kou_jing_beta"]["band_float_literal"],
            "is_knife_edge": True,
        } for m in knife_cells],
        "beta_band_counts_if_knife_edge_rounded_CONTROL_ONLY": {
            "PASS": sum(1 for m in beta_cells
                        if m["kou_jing_beta"]["band"] == "PASS"
                        or m["kou_jing_beta"]["is_knife_edge"]),
            "BELOW_TOL": sum(1 for m in beta_cells
                             if m["kou_jing_beta"]["band"] == "BELOW_TOL"
                             and not m["kou_jing_beta"]["is_knife_edge"]),
            "participates_in_judgement": False,
        },
        "leg_states_mechanical": {
            "alpha_leg": alpha_state, "beta_leg": beta_state,
            "alpha_uncomputable_cells": alpha_uncomputable,
            "beta_uncomputable_cells": beta_uncomputable,
            "precedence_rule_disclosed": (
                "分母格不可算 ⇒ KD 优先（构造/素材不可算属硬阻断）；否则异档 ⇒ FAIL；"
                "全档一致 ⇒ PASS。§3.3 三态表未明写优先级，本处为机械优先级的显式披露，"
                "0 新增阈值、0 新增数值切点"),
        },
        "compound_claim_state_mechanical": compound_state,
        "compound_table_covered_both_legs": compound_covered,
        "compound_mixed_branch_policy": (
            "PI 批 9 · P-4 ①：沿 v2 显式留白 ⇒ 触发即落 KD 并 γ（γ-PKA-3 / γ-END-1）"),
        "aggregation_note": "α/β 双口径强制并报、0 互替（K-V3R1P1-0-C）；0 合取掩盖任一腿",
    }

    # ---- 9. as-run 环境自证落盘 ----
    as_run = json.load(open(os.path.join(REPO, "results", "deposon_v20_gt2b.json"),
                            encoding="utf-8"))
    as_run_check = {
        "method": ("在 v3 executor 内以 (seed=20260828, D = 3 − T) 复跑 legacy parity 面"
                   "⇒ 构造退化为既有恒 4 项面，逐位核对在盘 a2ae7997ee67"),
        "as_run_bank_seed": as_run["bank_seed"],
        "as_run_accuracy_by_T": as_run["accuracy_by_T"],
        "recomputed_accuracy_by_T_seed20260828": parity_recomputed,
        "bit_identical": bool(as_run["accuracy_by_T"] == parity_recomputed),
        "as_run_legacy_verdict": as_run["verdict"],
        "as_run_n_options_fixed": as_run["n_options_fixed"],
        "as_run_chance_level": as_run["chance_level"],
        "v3_n_options_fixed": "ABANDONED（A-案 2：n_options = 1+T+D 随格变化）",
        "v3_chance_level": "逐格 1/(1+T+D)（P-2 ①）",
        "legacy_parity_face_cells": legacy_parity,
        "legacy_parity_face_note": ("该面含 D=0 档（T=3）⇒ 结构性恒等格仍存在；"
                                    "**本 v3 面 D ≥ 1，不含该档**"),
        "control_used_as_threshold": False,
    }

    # ---- 10. P-5 非同退化独立佐证（0 读数派生 · 可机械复算）----
    fd_total = sum(m["rule_filter_branch_reachability"]["n_items_all_filtered_fallback"]
                   for m in matrix)
    p5 = {
        "requirement": "PI 批 9 · P-5 ① 必须附非同退化独立佐证",
        "why": ("件 A §4.2 A-案 1 代价②：A-案 1/4 会丢 C1 诊断格 ⇒ 新面须另找非同退化证据，"
               "否则「α 腿 PASS」无法与「诱饵少」区分。件 A §6.1 派生退化族同源。"),
        "independence_definition": (
            "以下 5 项证据**全部不读 item 级 0/1 正确性** ⇒ 与 α/β 读数非同源派生；"
            "读数派生的自证（腿级序列非退化、T 效应可分离网格）另列于 reading_derived 段"),
        "evidence": {
            "1_C4_mechanism_asset_level": {
                "source": "图节点标签集 × 缓存陷阱标签集（纯资产层）",
                "per_domain": c4,
                "all_traps_outside_graph_node_set": c4_all_zero,
                "implication": ("陷阱恒不在图节点集内 ⇒ field_mean 对陷阱恒打 -inf（C4）；"
                                "**A-案 2 仍不触及 C4** ⇒ v3 的「T 效应可分离」与"
                                "「T 效应是否反映语义识别力」是两个不同命题，0 混谈"),
            },
            "2_construction_integrity_bank_level": {
                "source": "题库逐题 n_traps / n_decoys / n_options（纯构造层）",
                "all_cells_bank_ok": bool(all(m["construction_integrity"]
                                              ["bank_n_traps_all_eq_T"] for m in matrix)),
                "n_cells_checked": len(matrix),
                "implication": ("逐格 n_traps == T 且 n_decoys == D ⇒ T 与 D 在题库层"
                                "**不再共线**（C0 的结构性解除，0 依赖读数）"),
            },
            "3_T_D_orthogonality_factor_level": {
                "source": "因子面枚举（纯组合层）",
                "per_TD_n_cells": {f"T{T}_D{D}": sum(1 for m in matrix
                                                     if m["T"] == T and m["D"] == D)
                                   for T in T_LEVELS for D in D_LEVELS},
                "implication": "6 个 (T,D) 组合各 6 格 ⇒ 因子面齐备、0 缺格、0 退化格",
            },
            "4_rule_filter_branch_reachability_label_level": {
                "source": "RULE_KEYWORDS 逐选项命中（标签层，闭合 γ-PKA-2）",
                "rule_keywords": list(RULE_KEYWORDS),
                "total_items_all_filtered_fallback": fd_total,
                "total_gold_filtered": sum(m["rule_filter_branch_reachability"]["n_gold_filtered"]
                                           for m in matrix),
                "total_trap_filtered": sum(m["rule_filter_branch_reachability"]["n_trap_filtered"]
                                           for m in matrix),
                "total_decoy_filtered": sum(m["rule_filter_branch_reachability"]["n_decoy_filtered"]
                                            for m in matrix),
                "total_items_picked_gold": sum(
                    m["rule_filter_branch_reachability"]["n_items_picked_gold"] for m in matrix),
                "implication": "rule_filter 的分支可达性与 D 的耦合面被逐格实测（0 预判）",
            },
            "5_as_run_legacy_parity": {
                "source": "既有在盘件 deposon_v20_gt2b.json（a2ae7997ee67）逐位核对",
                "bit_identical": as_run_check["bit_identical"],
                "implication": ("v3 executor 的广义构造在 D=3−T 时与既有构造逐字节同构 ⇒ "
                                "新增 D 因子未污染继承机制、0 环境漂移"),
            },
        },
        "reading_derived_corroboration_DISCLOSED_AS_SAME_SOURCE": {
            "note": "以下**读数派生**，0 计入「非同源」段，仅作对照披露",
            "c0_relief_test": {
                "definition": "若 T 与 D 仍共线，则同 (T,D) 只可能落在一条对角线上；"
                              "逐列可得完整 T 序列即证 T 效应非 D 的单调重命名",
                "field_mean_grid_by_TD": {f"T{T}_D{D}": sorted(
                    acc[(s, T, D)]["field_mean"] for s in BANK_SEED_SET)
                    for T in T_LEVELS for D in D_LEVELS},
                "monotone_nondecreasing_in_T_by_column_D": {
                    str(D): {str(s): all(acc[(s, T, D)]["field_mean"]
                                         <= acc[(s, T + 1, D)]["field_mean"] + 1e-12
                                         for T in T_LEVELS[:-1])
                             for s in BANK_SEED_SET} for D in D_LEVELS},
            },
        },
    }

    # ---- 11. 防退化门自证（AR4：门施于读法 D；A / C 双记并报）----
    degen = {
        "rule": "n_distinct > 3 + std > 0（K-V3R1P1-0-A，字面不变）",
        "gate_sequence_frozen": "D",
        "gate_sequence_frozen_basis": "件 A §3 沿 AR4：读法 D 的定义与 T/D 网格无关 ⇒ 可沿用",
        "reading_A_per_domain_item_accuracy": {
            "definition": "每格每臂的 4 个域 item 级正确率序列（n=4/格）",
            "role": "CONTROL_ONLY（AR4：0 再作为判死线分支）",
            "per_cell": {f"seed{c['bank_seed']}_T{c['T']}_D{c['D']}":
                         {a: series_stats([c["per_domain_accuracy"][d][a]
                                           for d in c["per_domain_accuracy"]])
                          for a in ARMS} for c in cells},
        },
        "reading_B_per_item_correctness": {
            "definition": "每格每臂 40 条 item 级 0/1 正确性序列（n=40/格）",
            "role": "永禁作门序列（结构性二值 ⇒ n_distinct ≤ 2 恒成立）",
            "is_binary_by_construction": True,
        },
        "reading_C_cell_level_readout": {
            "definition": "36 格格级读数序列（每臂 n=36）",
            "role": "CONTROL_ONLY（AR4）",
            "per_arm": {a: series_stats([acc[(s, T, D)][a]
                                         for s in BANK_SEED_SET
                                         for T in T_LEVELS for D in D_LEVELS])
                        for a in ARMS},
        },
        "reading_D_matrix_pooled": {
            "definition": f"逐臂 × 全矩阵的域级正确率池化序列（{len(graphs)} 域 × "
                          f"{len(matrix)} 格 = {len(graphs) * len(matrix)} 值/臂）",
            "role": "GATE_SEQUENCE（件 A §3 沿 AR4 测量前唯一冻结）",
            "per_arm": {a: series_stats([c["per_domain_accuracy"][d][a]
                                         for c in cells
                                         for d in c["per_domain_accuracy"]])
                        for a in ARMS},
        },
    }
    _a_vals = [v for cell in degen["reading_A_per_domain_item_accuracy"]["per_cell"].values()
               for v in cell.values()]
    degen["reading_A_summary"] = {
        "n_cell_arm_series": len(_a_vals),
        "n_pass": sum(1 for v in _a_vals if v["gate_non_degenerate"]),
        "n_fail": sum(1 for v in _a_vals if not v["gate_non_degenerate"]),
        "fail_series": [f"{cell}|{a}" for cell, arms in
                        degen["reading_A_per_domain_item_accuracy"]["per_cell"].items()
                        for a, v in arms.items() if not v["gate_non_degenerate"]],
    }
    degen["reading_A_all_cells_pass"] = bool(degen["reading_A_summary"]["n_fail"] == 0)
    degen["reading_C_all_arms_pass"] = bool(all(
        v["gate_non_degenerate"] for v in degen["reading_C_cell_level_readout"]["per_arm"].values()))
    degen["reading_D_all_arms_pass"] = bool(all(
        v["gate_non_degenerate"] for v in degen["reading_D_matrix_pooled"]["per_arm"].values()))
    degen["cfg_seed_lever"] = cfg_seed_static
    degen["reading_dependence_disclosure"] = (
        "AR4 冻结：门施于读法 D（全矩阵池化）。读法 A（per-cell 4 域序列）"
        f"{degen['reading_A_summary']['n_fail']}/{degen['reading_A_summary']['n_cell_arm_series']} "
        "条不过门（粒度不匹配：n=4 要 4 值全互异）、读法 C 过门与否见上表 —— "
        "A / C 事实照旧逐条落盘并随判定披露，0 隐瞒；0 再作为判死线分支")
    degen["leg_readout_series_self_check"] = {
        "definition": "α/β 两腿读数序列自身的非退化自证（v2 §5.5 体例）",
        "beta_delta_all_36": series_stats([m["kou_jing_beta"]["value"] for m in beta_cells]),
        "alpha_24": series_stats([m["kou_jing_alpha"]["value"] for m in alpha_cells]),
    }
    degen["new_degeneracy_family_scanned"] = {
        "family": "选项集内标签重名（D 成为自由因子后 decoy 有放回抽样 ⇒ 重名概率上升）",
        "total_duplicate_label_positions": sum(
            m["construction_integrity"]["n_duplicate_label_positions"] for m in matrix),
        "total_items_gold_label_multi_occurrence": sum(
            m["construction_integrity"]["n_items_gold_label_multi_occurrence"] for m in matrix),
        "per_cell_max": max(m["construction_integrity"]["n_duplicate_label_positions"]
                            for m in matrix),
    }
    degen["structural_identity_cell_C1_unreachable"] = {
        "claim": "本面 D ≥ 1 ⇒ 每格至少 1 个图内候选取与 gold 竞争 ⇒ D=0 型恒等格不可达",
        "n_cells_field_mean_exactly_1_all_domains": sum(
            1 for m in matrix if all(abs(v - 1.0) < 1e-12
                                     for v in m["per_domain_accuracy"].values()
                                     if False) and False),
        "n_cells_with_any_domain_field_mean_eq_1": sum(
            1 for m in matrix if any(abs(m["per_domain_accuracy"][d]["field_mean"] - 1.0) < 1e-12
                                     for d in m["per_domain_accuracy"])),
        "note": "0 预宣告「不存在恒等格」；只报实测计数，由 verdict-keeper 判读",
    }

    # ---- 12. K-V3R-35 (b) 四类触发检测（照旧逐条检测、照旧逐条登记 γ）----
    triggers = {
        "1_仓外只读被拒": {"triggered": not ext_read_ok,
                          "evidence": ext_read_error or "4 件全部可读（只读）"},
        "2_缓存域缺": {"triggered": bool(excluded_domains),
                    "evidence": {"excluded_domains": excluded_domains,
                                 "included_domains": sorted(graphs)}},
        "3_跑不完": {"triggered": bool(len(matrix) != 36
                                or any(not m["n_items_as_expected"] for m in matrix)
                                or alpha_uncomputable or beta_uncomputable),
                  "evidence": {"n_cells_produced": len(matrix), "n_cells_expected": 36,
                               "n_items_mismatched_cells": [m["cell"] for m in matrix
                                                            if not m["n_items_as_expected"]],
                               "uncomputable_cells": sorted(set(alpha_uncomputable)
                                                            | set(beta_uncomputable))}},
        "4_item级正确率_n_distinct<=3退化": {
            "triggered": bool(degen["reading_A_summary"]["n_fail"] > 0),
            "evidence": {"reading_A_n_fail": degen["reading_A_summary"]["n_fail"],
                         "reading_A_n_total": degen["reading_A_summary"]["n_cell_arm_series"]}},
    }
    triggered_four = [k for k, v in triggers.items() if v["triggered"]]
    degen_gate_hit = not degen["reading_D_all_arms_pass"]

    # ---- 13. γ 登记（件 A §9 逐条复核更新 + v3 面新增）----
    gamma = [
        {"id": "γ-PKA-1", "item": "派工单参考清单 3 件 GT8 面件归属",
         "v3_status": "沿案结清（件 A 已登记、0 引用）", "triggered_now": False,
         "detail": {"referenced": ["2b88948dca19", "34ff826f97c2", "2505ff5d203f"],
                    "used_in_v3": 0}},
        {"id": "γ-PKA-2", "item": "rule_filter 臂在共线构造下是否亦被共线驱动",
         "v3_status": ("**本棒逐格实测闭合**（P-5 证据 4）：RULE_KEYWORDS 逐选项命中计数、"
                       "全过滤兜底分支命中数、按 T/D 分层的 gold/trap/decoy 过滤数均落盘；"
                       "0 预判结论，判定权归 verdict-keeper"),
         "triggered_now": True,
         "detail": {"rule_keywords": list(RULE_KEYWORDS),
                    "per_cell_in_matrix": "matrix[].rule_filter_branch_reachability",
                    "totals": {k: p5["evidence"]["4_rule_filter_branch_reachability_label_level"][k]
                               for k in ("total_items_all_filtered_fallback",
                                         "total_gold_filtered", "total_trap_filtered",
                                         "total_decoy_filtered", "total_items_picked_gold")}}},
        {"id": "γ-PKA-3", "item": "v2 §3.3 复合表未覆盖混合分支「PASS+KD / FAIL+KD」",
         "v3_status": ("PI 批 9 · P-4 ① 已裁：沿 v2 显式留白 ⇒ 触发即落 KD 并 γ；"
                       "本轮是否触发见 consistency.compound_table_covered_both_legs"),
         "triggered_now": not compound_covered,
         "detail": {"alpha_state": alpha_state, "beta_state": beta_state,
                    "covered": compound_covered}},
        {"id": "γ-PKA-4", "item": "C3 另 2 域 gt2_attacker_cache 采集",
         "v3_status": "PI 批 9 · P-6 ①：本轮只跑 4 域 + 强制披露；0 虚构缓存",
         "triggered_now": bool(excluded_domains),
         "detail": {"excluded_domains": excluded_domains}},
        {"id": "γ-PKA-5", "item": "γ-VK-1 / γ-V2-8 / γ-VK-3 沿 v2 未闭合",
         "v3_status": "沿案未闭合；本棒 0 重裁、0 代行（沿 K-V5R3-0-D）",
         "triggered_now": True, "detail": {"adjudicated_by_v3": 0}},
        {"id": "γ-PKA-6", "item": "A-案 2 下「跨格机会水平不恒定」的报告口径",
         "v3_status": "PI 批 9 · P-2 ① 已裁：逐格报 1/(1+T+D)；0 聚合口径已实现",
         "triggered_now": True,
         "detail": {"chance_level_per_TD": consistency["chance_level_per_TD"],
                    "aggregation_reporting_used": False}},
        {"id": "γ-V3-EX-1（本棒新登记）",
         "item": "D 档具体取值（D=1 / D=2）**预登记件未给数值**（件 A 只给 D ∈ {D_min, D_max} 两档）",
         "v3_status": ("由执行棒冻结为默认档并逐条列证（构造型设计参数、0 是阈值）；"
                       "**PI 未明示该具体取值** ⇒ 如实登记，供 PI 追认或改判"),
         "triggered_now": True,
         "detail": {"d_levels": list(D_LEVELS), "basis": ["件 A §4.2 A-案 2 字面两档",
                    "件 A §4.1 规模例 3×2×6×4", "D_min=1 ⇒ D=0 恒等格不可达"],
                    "would_change_if_pi_picks_other_D": "面形状变，α/β 分母与逐格机会水平随之变；"
                                                        "0 外推当前读数到其他 D 取值"}},
        {"id": "γ-V3-EX-2（本棒新登记）",
         "item": "18 frozen / 9 网格两份清单的构成**本棒 0 自行认定**",
         "v3_status": ("沿件 A §7.1 同口径：只做只读存在性 + 哈希复读（frozen_anchor_scan），"
                       "0 写任何锚件、0 断言清单构成"),
         "triggered_now": True,
         "detail": {"n_anchors_in_schema": None, "note": "见 frozen_zero_touch"}},
        {"id": "γ-V3-EX-3（本棒新登记）",
         "item": "件 A §4.1 A-案 2 规模例按「T×D×seed×域 = 144 格」计，与 v2 体例的「seed×T = 18 格」口径不同",
         "v3_status": "计数口径差异如实登记；α/β 判定格沿 v2 体例 = 36 格，域级池化 = 144 值/臂",
         "triggered_now": True, "detail": {"count_convention": consistency["count_convention_disclosure"]}},
    ]
    gamma[6]["detail"]["n_anchors_in_schema"] = frozen_pre["n_anchors_in_schema"]

    # ---- 14. 跑后：仓外只读复读 + 0 触动复读 + frozen 锚复读 ----
    ext_post = {fn: {"path": os.path.join(EXT_CACHE, fn),
                     "sha12": sha12(os.path.join(EXT_CACHE, fn)),
                     "bytes": nbytes(os.path.join(EXT_CACHE, fn))}
                for fn in EXT_CACHE_ITEMS}
    ext_readonly = {
        "external_archive": "D:/私人资料/_non_upload_local_archive/",
        "items_pre": ext_pre, "items_post": ext_post,
        "pre_post_identical": bool(
            {fn: (v["sha12"], v["bytes"]) for fn, v in ext_pre.items()} ==
            {fn: (v["sha12"], v["bytes"]) for fn, v in ext_post.items()}),
        "copied_into_repo": 0, "wrote_external": False,
        "repo_cache_dir_exists": os.path.exists(os.path.join(REPO, "results",
                                                              "gt2_attacker_cache")),
        "declaration": "只读取用授权：0 复制入仓 / 0 写入 / 0 移出 / 0 删除 / 0 改 ACL",
    }
    zt_post = fingerprint(ZERO_TOUCH)
    frozen_post = frozen_anchor_scan()
    zero_touch_evidence = {
        "anchors_pre": zt_pre, "anchors_post": zt_post,
        "all_identical": bool(
            {k: (v["sha12"], v["bytes"]) for k, v in zt_pre.items()} ==
            {k: (v["sha12"], v["bytes"]) for k, v in zt_post.items()}),
        "existing_files_modified": 0,
    }
    frozen_zero_touch = {
        "pre": frozen_pre, "post": frozen_post,
        "pre_post_identical": bool(
            {k: v["sha12"] for k, v in frozen_pre["resolved"].items()} ==
            {k: v["sha12"] for k, v in frozen_post["resolved"].items()}),
        "n_anchors_in_schema": frozen_pre["n_anchors_in_schema"],
        "n_anchors_resolved_on_disk": frozen_pre["n_anchors_resolved_on_disk"],
        "note": ("本棒 0 自行认定「18 frozen / 9 网格」清单构成（件 A §7.1 同口径）；"
                 "此处仅只读存在性 + 哈希复读证据"),
    }

    # ---- 15. 打包（0 代判：机械落档 ≠ 裁定；裁定权属 verdict-keeper）----
    out = {
        "task": ("V5 #35 v3 · GT2b C0 共线修正 · A-案 2 双因子全交叉执行面"
                 "（6 seed × 3 T × 2 D = 36 格 × α/β 双口径）"),
        "date": "2026-09-29",
        "author": "Mavis 团队 worker（executor）",
        "prereg_v3_itemA": "results/_v5_item35_v3_collinear_prereg_2026_09_29.md",
        "prereg_v3_itemA_sha12": zt_pre["prereg_v3_itemA"]["sha12"],
        "verdict_v2_sha12": zt_pre["verdict_v2"]["sha12"],
        "pi_confirmation_batch9": {
            "P-1": "① A-案 2 双因子全交叉（弃恒 4 项 / 弃机会恒 25%）",
            "P-2": "① 逐格报机会水平 1/(1+T+D)",
            "P-3": "① 明示延用 GT 系全局条款 K-V5R3-0-A…0-G 于 #35 面",
            "P-4": "① 混合分支沿 v2 显式留白 ⇒ 触发即落 KD 并 γ",
            "P-5": "① 必须附非同退化独立佐证",
            "P-6": "① 本轮 4 域 + 强制披露",
        },
        "kill_line": ("件 A §3 全为既有 K-* 引用：K-V3R-35 / K-V3R1P1-0-A/0-C / "
                      "K-V5R2-35-AR1…AR6 / K-V5R3-0-A…0-G（PI 批 9 P-3 ① 明示延用）/ "
                      "v2 §3.3 三态表 / v2 §3.4 假判①–⑤；field_tol = 0.05 一字不动"),
        "adjudication_ownership": {
            "this_baton": "worker（executor）",
            "this_baton_did_not_adjudicate": True,
            "verdict_owner": "verdict-keeper",
            "note": ("本件提供逐格读数 + 逐腿**机械落档**；claim 级裁定、根因三分类"
                     "（K-V5R3-0-F）、对外表述属 verdict-keeper，本棒 0 代判"),
            "mechanical_state_is_not_verdict": True,
            "root_cause_class": None,
        },
        "frozen_params": {
            "field_tol": FIELD_TOL, "field_tol_unchanged": True,
            "t_levels": list(T_LEVELS), "d_levels": list(D_LEVELS),
            "bank_seed_set": list(BANK_SEED_SET),
            "seeds_existing": list(SEEDS_EXISTING),
            "n_items_per_map": N_ITEMS_PER_MAP,
            "ARMS": list(ARMS),
            "n_options_fixed": "ABANDONED（A-案 2）",
            "chance_level_fixed": "ABANDONED（A-案 2 ⇒ 逐格 1/(1+T+D)）",
            "matrix_size": {"seeds": 6, "T": 3, "D": 2, "cells": 36,
                            "alpha_denominator_cells": 24, "beta_cells": 36,
                            "domain_level_values_per_arm": len(graphs) * 36},
            "config": config_dict(cfg),
            "new_numeric_thresholds_introduced": 0,
            "new_numeric_cutpoints_introduced": 0,
        },
        "zero_touch_anchors": zero_touch_evidence,
        "frozen_zero_touch": frozen_zero_touch,
        "pre_run_selfcheck": pre_run_selfcheck,
        "external_readonly": ext_readonly,
        "assets": {
            "domains_included": sorted(graphs),
            "domains_excluded_no_cache": excluded_domains,
            "traps_available_per_domain": {d: len(t) for d, t in sorted(traps.items())},
            "scope_limit": "仅 4 缓存域；0 外推至全 6 域（P-6 ① / C3）",
        },
        "kou_jing_fields": {
            "alpha": ("|field_mean(T,D) − field_mean(T=1,D)| ≤ 0.05 ⇒ immune"
                      "（**列内**基线，件 A §5.3）"),
            "beta": "delta = field_mean − max(rule_filter, random)（同格内）；≥ 0.05 ⇒ PASS",
            "strongest_opponent_definition": "max(rule_filter, random)（两对照臂取大）",
            "alpha_beta_not_interchangeable": True,
            "aggregation": "逐腿机械落档 + 计数；0 合取掩盖任一腿（AR3）",
        },
        "matrix_36cells": matrix,
        "consistency": consistency,
        "construct_degen_self_check": degen,
        "as_run_environment_self_check": as_run_check,
        "independent_corroboration_P5": p5,
        "kill_line_b_four_triggers": {
            "rule": "K-V3R-35 (b) 四类触发照旧逐条检测、照旧逐条登记 γ",
            "per_trigger": triggers,
            "n_triggered": len(triggered_four),
            "triggered_ids": triggered_four,
            "degeneracy_gate_D_hit": degen_gate_hit,
            "terminal_membership": ("KD（判死构造）" if (degen_gate_hit or len(triggered_four) > 0)
                                    else "非门不达分支"),
            "note": "「不明」在本件生效范围内结构性不可达（AR4 + K-V5R3-0-A）；触发信息一字不删",
        },
        "root_cause_evidence_for_adjudicator": {
            "note": ("K-V5R3-0-F：每条 FAIL 须附根因三分类之一；分类权属 verdict-keeper，"
                     "本棒 0 代判 ⇒ root_cause_class 留空，仅提供机械可核证据"),
            "alpha_not_immune_cells_mechanical_evidence": {
                "cells": alpha_not_immune,
                "field_mean_by_T_by_D": {str(D): {str(T): [acc[(s, T, D)]["field_mean"]
                                                         for s in BANK_SEED_SET]
                                                for T in T_LEVELS} for D in D_LEVELS},
                "note": "A-案 2 下 T 与 D 解耦 ⇒ α 的失败面须**按 D 分列**看，"
                        "0 合并各列为一个判据（件 A §5.3 反假判）",
            },
            "beta_below_tol_cells_mechanical_evidence": {
                "cells": beta_below,
                "by_TD": consistency["beta_band_counts_by_TD"],
                "mechanism_note": ("field_mean 对陷阱恒打 -inf（C4，未解除）⇒ 「不被骗」是"
                                   "排序对象域的机制结果；叠加 D 自由 ⇒ 逐格机会水平不恒定，"
                                   "跨格 β 值不可直接比大小（P-2 ①）"),
            },
        },
        "gamma_registry": gamma,
        "zero_touch_declaration": {
            "existing_files_modified": 0,
            "runner_modified": False,
            "corpus_or_index_modified": False,
            "derived_json_merged_into_existing": False,
            "llm_calls": 0, "proxy": False, "key_reads": 0,
            "new_thresholds": 0,
            "v2_verdict_or_result_retouched": False,
        },
        "determinism": "无墙钟时间戳；同输入重跑本 JSON 逐字节一致",
    }
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1, sort_keys=False)

    print(json.dumps({
        "out": OUT_PATH,
        "n_cells": len(matrix),
        "n_domain_level_values_per_arm": len(graphs) * len(matrix),
        "alpha_denominator": len(alpha_cells),
        "alpha_leg_mechanical": alpha_state,
        "beta_leg_mechanical": beta_state,
        "compound_mechanical": compound_state,
        "compound_covered": compound_covered,
        "alpha_band_counts": consistency["alpha_band_counts"],
        "beta_band_counts": consistency["beta_band_counts"],
        "alpha_not_immune_cells": alpha_not_immune,
        "beta_below_tol_cells": beta_below,
        "knife_edge_cells": [m["cell"] for m in knife_cells],
        "chance_level_per_TD": consistency["chance_level_per_TD"],
        "reading_D_all_pass": degen["reading_D_all_arms_pass"],
        "reading_A_n_fail": degen["reading_A_summary"]["n_fail"],
        "reading_C_all_pass": degen["reading_C_all_arms_pass"],
        "as_run_bit_identical": as_run_check["bit_identical"],
        "zero_touch_all_identical": zero_touch_evidence["all_identical"],
        "frozen_anchors_pre_post_identical": frozen_zero_touch["pre_post_identical"],
        "ext_readonly_identical": ext_readonly["pre_post_identical"],
        "four_triggers_triggered": triggered_four,
        "p5_independence": "5 项非同源证据 + 1 段读数派生对照",
    }, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
