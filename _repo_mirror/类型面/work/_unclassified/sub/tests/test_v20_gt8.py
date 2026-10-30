# -*- coding: utf-8 -*-
# GT-8（领域鉴定器 v0 hub 轴语料外预登记复现）回归测试：
#   1) 新图与语料图不同构哨兵（不变量 (N, E, 入度/出度多重集) 全异）；
#   2) 特征公式一致性：hub_concentration 对语料 S1/S2/S3 重算应逐值等于
#      results/v20_graph_features.csv 锚点（0.0526 / 0.0333 / 0.0625）；
#   3) 新图合法性（DAG、named⊆edges、real_semantics=0、hub 高低排序符合
#      SPEC_GT8 §3 预登记）；
#   4) verdict 逻辑单测（支持 / 判死 / inconclusive / 持平）。
import numpy as np
import pytest

from mindmap_corpus_v20 import CORPUS_DIR, is_dag, load_corpus
from run_v20_gt8 import (GT8_MIN_PAIRS, GT8_PAIRS, build_gt8_graph,
                         graph_invariant, gt8_verdict, hub_concentration)

# SPEC_GT8 §2 锚点（results/v20_graph_features.csv 逐字）
CSV_ANCHORS = {"S1": 0.0526, "S2": 0.0333, "S3": 0.0625}
# SPEC_GT8 §3 预登记的预计算 hub_concentration
SPEC_HUBS = {"GT8_A_high": 15 / 30, "GT8_A_low": 2 / 30,
             "GT8_B_high": 19 / 39, "GT8_B_low": 1 / 39}
ALL_GT8 = tuple(sorted(_GT8 for pair in GT8_PAIRS for _GT8 in pair))


def _corpus_graphs():
    return load_corpus(CORPUS_DIR, families=("S", "L"))


def test_new_graphs_not_isomorphic_to_corpus():
    """不同构哨兵：4 张新图的不变量与全部 22 张语料图（族 S+L）全异。"""
    corpus_invariants = {
        g["graph_id"]: graph_invariant(g["N"], [tuple(e) for e in g["edges"]])
        for g in _corpus_graphs()}
    assert len(corpus_invariants) == 22
    for gid in ALL_GT8:
        g = build_gt8_graph(gid)
        inv = graph_invariant(g["N"], [tuple(e) for e in g["edges"]])
        assert inv not in corpus_invariants.values(), (
            f"{gid} 与语料图不变量撞车（疑似同构）")


def test_new_graphs_pairwise_distinct():
    invs = [graph_invariant(g["N"], [tuple(e) for e in g["edges"]])
            for g in (build_gt8_graph(gid) for gid in ALL_GT8)]
    assert len(set(invs)) == len(invs)


def test_feature_formula_matches_csv_anchors():
    """hub_concentration = max_in_degree / n_edges：对 S1/S2/S3 重算
    应等于 CSV 锚点（0.0526 / 0.0333 / 0.0625，4 位小数口径）。"""
    corpus = {g["graph_id"]: g for g in _corpus_graphs()}
    for gid, anchor in CSV_ANCHORS.items():
        g = corpus[gid]
        val = hub_concentration(g["N"], [tuple(e) for e in g["edges"]])
        assert round(val, 4) == pytest.approx(anchor)


def test_new_graphs_legality_and_preregistration():
    """新图 DAG、named⊆edges、N/E 与 SPEC_GT8 §3 冻结值一致、hub 高低
    排序符合预登记（每对 high > low）、real_semantics=0 族 S。"""
    spec_ne = {"GT8_A_high": (31, 30), "GT8_A_low": (31, 30),
               "GT8_B_high": (40, 39), "GT8_B_low": (40, 39)}
    hubs = {}
    for gid in ALL_GT8:
        g = build_gt8_graph(gid)
        edges = [tuple(e) for e in g["edges"]]
        assert g["family"] == "S"               # real_semantics = 0
        assert (g["N"], len(edges)) == spec_ne[gid]
        assert is_dag(g["N"], edges)
        assert {tuple(e) for e in g["named_edges"]} <= set(edges)
        assert len(g["labels"]) == g["N"] and len(set(g["labels"])) == g["N"]
        hubs[gid] = hub_concentration(g["N"], edges)
        assert hubs[gid] == pytest.approx(SPEC_HUBS[gid])
    for high, low in GT8_PAIRS:
        assert hubs[high] > hubs[low]
        # N 与 n_edges 完全对配（SPEC_GT8 §3）
        gh, gl = build_gt8_graph(high), build_gt8_graph(low)
        assert gh["N"] == gl["N"]
        assert len(gh["edges"]) == len(gl["edges"])


def _pp(diffs):
    return [{"pair": f"p{i}", "high": f"h{i}", "low": f"l{i}",
             "diff_high": d[0], "diff_low": d[1]} for i, d in enumerate(diffs)]


def test_verdict_supports_when_all_pairs_concordant():
    v = gt8_verdict(_pp([(0.4, 0.1), (0.3, 0.05)]))
    assert v["verdict"] == "supports_H_GT8"
    assert v["supported_H_GT8"] is True
    assert len(v["pairs_concordant"]) == 2


def test_verdict_dead_when_all_pairs_reversed():
    v = gt8_verdict(_pp([(0.05, 0.2), (0.0, 0.1)]))
    assert v["verdict"] == "H_GT8_dead"
    assert v["supported_H_GT8"] is False


def test_verdict_inconclusive_on_split_or_tie():
    v = gt8_verdict(_pp([(0.4, 0.1), (0.05, 0.2)]))
    assert v["verdict"] == "inconclusive_preregistered_undefined_band"
    v2 = gt8_verdict(_pp([(0.4, 0.1), (0.2, 0.2)]))
    assert v2["verdict"] == "inconclusive_preregistered_undefined_band"
    assert v2["pairs_tied"] == ["p1"]


def test_verdict_requires_min_pairs():
    v = gt8_verdict(_pp([(0.4, 0.1)]))
    assert v["verdict"] == "inconclusive_preregistered_undefined_band"
    assert GT8_MIN_PAIRS == 2


def test_hub_concentration_definition_explicit():
    """显式锚点：单链 1/19、单汇聚 2/32（与 SPEC_GT8 §2 分数锚一致）。"""
    chain = [(i, i + 1) for i in range(19)]
    assert hub_concentration(20, chain) == pytest.approx(1 / 19)
    edges = [(0, 1), (2, 1)] + [(3, 4)]  # E=3, max_indeg=2
    assert hub_concentration(5, edges) == pytest.approx(2 / 3)
