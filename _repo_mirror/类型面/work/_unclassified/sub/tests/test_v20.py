# -*- coding: utf-8 -*-
# tests/test_v20.py — SPEC v2.0 语料生成器 / 族 L 解析器 / GT 判定规则测试
import json
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from deposon_diffusion import DiffusionConfig
from mindmap_corpus_v20 import (CORPUS_DIR, DEFAULT_N, FAMILY_L_DOMAINS,
                                ONTOLOGY_POOL, SCAN_SIZES, CacheMissingError,
                                FamilyLParseError, build_corpus,
                                build_familyL_prompts, corpus_plan,
                                familyL_prompt_manifest, generate_graph,
                                is_dag, load_corpus, longest_path_family)
from run_v20_corpus_eval import eval_graph, holm_adjust
from run_v20_familyL_ingest import ingest_domain
from run_v20_gt import gt1_verdict, gt4_verdict

ALL_FAMILIES = ("S1", "S2", "S3", "S4", "S5", "S6")


def _edge_set(g):
    return {tuple(e) for e in g["edges"]}


def _degrees(g):
    indeg = {i: 0 for i in range(g["N"])}
    outdeg = {i: 0 for i in range(g["N"])}
    for u, v in g["edges"]:
        outdeg[u] += 1
        indeg[v] += 1
    return indeg, outdeg


# ---------------------------------------------------------------- 确定性
def test_generator_deterministic_same_seed_same_sha256():
    for fam in ALL_FAMILIES:
        a = generate_graph(fam)
        b = generate_graph(fam)
        assert a == b
        assert a["sha256"] == b["sha256"]
        assert len(a["sha256"]) == 64


def test_generator_scan_variants_deterministic():
    for fam in ("S1", "S2", "S6"):
        for N in SCAN_SIZES:
            a = generate_graph(fam, N)
            b = generate_graph(fam, N)
            assert a["sha256"] == b["sha256"]
            assert a["N"] == N


def test_corpus_build_roundtrip(tmp_path):
    d = str(tmp_path / "corpus")
    s1 = build_corpus(d)
    idx1 = json.load(open(os.path.join(d, "index.json"), encoding="utf-8"))
    hashes1 = {g["graph_id"]: g["sha256"] for g in idx1["graphs"]}
    s2 = build_corpus(d)
    idx2 = json.load(open(os.path.join(d, "index.json"), encoding="utf-8"))
    hashes2 = {g["graph_id"]: g["sha256"] for g in idx2["graphs"]}
    assert hashes1 == hashes2
    assert s1["n_graphs"] == s2["n_graphs"] == len(corpus_plan())


def test_corpus_plan_composition():
    plan = corpus_plan()
    ids = [generate_graph(f, N)["graph_id"] for f, N in plan]
    assert len(ids) == len(set(ids)) == 16
    for fam in ALL_FAMILIES:
        assert fam in ids  # 6 主档
    for fam in ("S1", "S2", "S6"):
        for N in SCAN_SIZES:
            if N != DEFAULT_N[fam]:
                assert f"{fam}_n{N}" in ids


# ---------------------------------------------------------------- 结构不变式
def test_s1_is_single_chain():
    g = generate_graph("S1")
    indeg, outdeg = _degrees(g)
    assert g["edges"] == [[i, i + 1] for i in range(g["N"] - 1)]
    assert all(outdeg[i] <= 1 and indeg[i] <= 1 for i in range(g["N"]))
    assert outdeg[0] == 1 and indeg[0] == 0        # 链头
    assert outdeg[g["N"] - 1] == 0 and indeg[g["N"] - 1] == 1  # 链尾
    assert len(g["named_edges"]) == g["N"] - 1  # 全链 named
    assert g["filler_edges"] == []              # 纯链无 filler（如实披露）


def test_s2_is_tree():
    for N in (31, 20, 35, 45, 60):
        g = generate_graph("S2", N)
        indeg, outdeg = _degrees(g)
        assert len(g["edges"]) == N - 1                      # 树：N−1 边
        assert sum(1 for i in range(N) if indeg[i] == 0) == 1  # 单根
        assert all(indeg[i] <= 1 for i in range(N))
        assert is_dag(N, [tuple(e) for e in g["edges"]])
        # 平衡性：堆序完全二叉树 ⇒ 任意叶深度差 ≤1
        depth = {0: 0}
        for i in range(1, N):
            depth[i] = depth[(i - 1) // 2] + 1
        leaves = [i for i in range(N) if outdeg[i] == 0]
        assert max(depth[i] for i in leaves) - min(depth[i] for i in leaves) <= 1


def test_s3_has_exactly_three_hubs():
    g = generate_graph("S3")
    indeg, _ = _degrees(g)
    hubs = [i for i in range(g["N"]) if indeg[i] >= 2]
    assert sorted(hubs) == [1, 2, 3]          # 三个 GOAL 式汇聚点
    assert g["N"] == 30
    assert is_dag(g["N"], [tuple(e) for e in g["edges"]])


def test_s6_mirrors_v19_anchor_structure():
    from run_v15_experiment import reconstruct_mindmap
    Nv, adv, edgesv, _labels, meta = reconstruct_mindmap()
    g = generate_graph("S6")
    assert g["N"] == Nv == 45
    assert _edge_set(g) == {tuple(e) for e in edgesv}      # 边集同型
    assert {tuple(e) for e in g["named_edges"]} == {
        tuple(e) for e in meta["path_edges_named"]}        # named 同型 17 边
    assert g["labels"] != list(_labels)                    # 新标签


@pytest.mark.parametrize("fam", ALL_FAMILIES)
def test_named_filler_partition_and_dag(fam):
    g = generate_graph(fam)
    named = {tuple(e) for e in g["named_edges"]}
    filler = {tuple(e) for e in g["filler_edges"]}
    edges = _edge_set(g)
    assert named.isdisjoint(filler)                        # 不重叠
    assert named | filler == edges                         # 并集 = 边集
    assert len(edges) == len(g["edges"])                   # 无重复边
    assert is_dag(g["N"], list(edges))                     # 全部 DAG
    assert len(set(g["labels"])) == g["N"]                 # 标签图内唯一
    assert all(lab in ONTOLOGY_POOL for lab in g["labels"])  # 真实词本体
    assert g["source"] != g["target"]


@pytest.mark.parametrize("fam", ALL_FAMILIES)
def test_seed_on_disk_and_sizes(fam):
    g = generate_graph(fam)
    assert g["seed"] > 0 and g["N"] == DEFAULT_N[fam]
    assert g["nodes"] == list(range(g["N"]))


def test_longest_path_family_toy():
    # 菱形 DAG：0→1→3 与 0→2→3 等长（族=全部 4 边）；加短边 0→3 非族成员
    edges = [(0, 1), (1, 3), (0, 2), (2, 3), (0, 3)]
    named, L, start, end = longest_path_family(4, edges)
    assert L == 2
    assert named == {(0, 1), (1, 3), (0, 2), (2, 3)}
    assert (start, end) == (0, 3)


# ---------------------------------------------------------------- 族 L prompt / 解析器
def test_familyL_prompts_four_domains_with_constraints():
    prompts = build_familyL_prompts()
    assert set(prompts) == set(FAMILY_L_DOMAINS)
    manifest = familyL_prompt_manifest()
    for d, p in prompts.items():
        assert "30" in p and "45" in p and "JSON" in p  # 节点数约束 + JSON 输出
        assert len(manifest[d]["prompt_sha256"]) == 64
    # prompt 内容稳定 ⇒ manifest 稳定
    assert familyL_prompt_manifest() == manifest


def _valid_response(n=32):
    nodes = [f"概念{i}" for i in range(n)]
    edges = [[(i - 1) // 2, i] for i in range(1, n)]  # 树，必为 DAG
    return json.dumps({"nodes": nodes, "edges": edges}, ensure_ascii=False)


def test_familyL_parser_accepts_valid_and_fenced():
    from mindmap_corpus_v20 import parse_familyL_response
    r = parse_familyL_response(_valid_response())
    assert len(r["nodes"]) == 32 and len(r["edges"]) == 31
    r2 = parse_familyL_response(f"前言\n```json\n{_valid_response()}\n```\n后记")
    assert r2 == r


def test_familyL_parser_rejects_bad_inputs():
    from mindmap_corpus_v20 import parse_familyL_response
    with pytest.raises(FamilyLParseError):       # 非 JSON
        parse_familyL_response("not a json at all")
    with pytest.raises(FamilyLParseError):       # 节点数不足
        parse_familyL_response(_valid_response(10))
    with pytest.raises(FamilyLParseError):       # 索引越界
        parse_familyL_response(json.dumps(
            {"nodes": [f"n{i}" for i in range(30)],
             "edges": [[0, 30]]}, ensure_ascii=False))
    with pytest.raises(FamilyLParseError):       # 自环
        parse_familyL_response(json.dumps(
            {"nodes": [f"n{i}" for i in range(30)],
             "edges": [[5, 5]]}, ensure_ascii=False))
    with pytest.raises(FamilyLParseError):       # 有向环
        parse_familyL_response(json.dumps(
            {"nodes": [f"n{i}" for i in range(30)],
             "edges": [[0, 1], [1, 2], [2, 0]]}, ensure_ascii=False))
    with pytest.raises(FamilyLParseError):       # 标签重复
        parse_familyL_response(json.dumps(
            {"nodes": ["x"] * 30, "edges": [[0, 1]]}, ensure_ascii=False))
    with pytest.raises(FamilyLParseError):       # 缺键
        parse_familyL_response(json.dumps({"nodes": ["x"] * 30}))


# ---------------------------------------------------------------- 族 L 摄入
def test_ingest_missing_cache_raises(tmp_path):
    with pytest.raises(CacheMissingError):
        ingest_domain("physics_concepts", cache_dir=str(tmp_path / "none"),
                      corpus_dir=str(tmp_path / "corpus"))


def test_ingest_valid_cache_roundtrip(tmp_path):
    cache_dir = tmp_path / "cache"
    corpus_dir = tmp_path / "corpus"
    cache_dir.mkdir()
    manifest = familyL_prompt_manifest()
    for d in FAMILY_L_DOMAINS:
        cache_dir.joinpath(f"{d}.json").write_text(json.dumps({
            "domain": d, "attempt": 1,
            "prompt_sha256": manifest[d]["prompt_sha256"],
            "model": "test-double", "response_text": _valid_response(33)},
            ensure_ascii=False), encoding="utf-8")
    rec = ingest_domain("physics_concepts", cache_dir=str(cache_dir),
                        corpus_dir=str(corpus_dir))
    assert rec["graph_id"] == "L_physics_concepts" and rec["family"] == "L"
    assert rec["N"] == 33 and rec["structure"] == "llm_generated_dag"
    named = {tuple(e) for e in rec["named_edges"]}
    filler = {tuple(e) for e in rec["filler_edges"]}
    assert named.isdisjoint(filler)
    assert named | filler == _edge_set(rec)
    assert rec["provenance"]["prompt_sha256_matches_preregistered"]
    # 幂等：同缓存 ⇒ 同 sha256
    rec2 = ingest_domain("physics_concepts", cache_dir=str(cache_dir),
                         corpus_dir=str(corpus_dir))
    assert rec["sha256"] == rec2["sha256"]


# ---------------------------------------------------------------- GT 判定规则重算
def test_gt1_verdict_rule_recompute():
    # 全部 20 运行 0.5，mean-field 0.8：差 0.3 ≥0.2 且 20 ≥15 → 支持
    v = gt1_verdict([0.5] * 20, 0.8)
    assert v["supported_potential_game"] and v["n_runs_below_meanfield"] == 20
    # 差不足 0.2 → 判死（即使全部劣于）
    assert not gt1_verdict([0.7] * 20, 0.8)["supported_potential_game"]
    # 差够但只有 14 运行劣于 → 判死
    rates = [0.0] * 14 + [0.9] * 6  # 均值 0.27 < 0.8-0.2，但 6 个不劣于
    v = gt1_verdict(rates, 0.8)
    assert not v["supported_potential_game"] and v["n_runs_below_meanfield"] == 14
    # 打平（不严格劣于）不计
    assert not gt1_verdict([0.8] * 20, 0.8)["supported_potential_game"]


def test_gt4_verdict_rule_recompute():
    v = gt4_verdict({"g1": 1.5, "g2": 1.3, "g3": 2.0})
    assert v["median_poa"] == pytest.approx(1.5)
    assert v["verdict"] == "field_coordination_value_supported"
    assert gt4_verdict({"g1": 1.0, "g2": 0.9})["verdict"] == "GT4_dead"
    assert gt4_verdict({"g1": 1.1, "g2": 1.15})["verdict"].startswith("inconclusive")
    # inf 不进入 median，单独计数
    v = gt4_verdict({"g1": float("inf"), "g2": 0.5, "g3": None})
    assert v["n_poa_inf"] == 1 and v["n_poa_undefined"] == 1
    assert v["median_poa"] == pytest.approx(0.5)


def test_holm_adjust_recompute():
    out = holm_adjust({"a": 0.001, "b": 0.02})
    assert out["a"]["holm_threshold"] == pytest.approx(0.05 / 4)
    assert out["b"]["holm_threshold"] == pytest.approx(0.05 / 3)
    assert out["a"]["significant_holm"] and not out["b"]["significant_holm"]
    # 顺序停止：最小 p 不显著 ⇒ 后续一律不显著
    out = holm_adjust({"a": 0.02, "b": 0.6})
    assert not out["a"]["significant_holm"] and not out["b"]["significant_holm"]
    # 最小 p 显著但次小 p 未过其阈值 ⇒ 次小不显著
    out = holm_adjust({"a": 0.001, "b": 0.02})
    assert out["a"]["significant_holm"] and not out["b"]["significant_holm"]


# ---------------------------------------------------------------- 评估集成（小图冒烟）
def test_eval_graph_smoke_s1():
    g = generate_graph("S1")
    res = eval_graph(g, DiffusionConfig())
    assert res["n_edges"] == 19 and res["n_named"] == 19
    for arm in ("field_mean", "field_guided", "random", "degree",
                "adamic_adar", "jaccard", "rule_filter"):
        m = res["arms"][arm]["named"]
        assert m["n"] == 19
        assert 0.0 <= m["hits@3"] <= 1.0 and 0.0 <= m["mrr"] <= 1.0
        assert res["arms"][arm]["filler"]["n"] == 0  # 纯链 filler=∅
        assert res["arms"][arm]["filler"]["hits@3"] is None


def test_on_disk_corpus_index_consistent():
    # 交付物落盘状态自检（corpus/v20 已由生成器写出）
    if not os.path.exists(os.path.join(CORPUS_DIR, "index.json")):
        pytest.skip("corpus not built on disk")
    graphs = load_corpus(CORPUS_DIR, families=("S",))
    assert len(graphs) == 16
    for g in graphs:
        fresh = generate_graph(
            g["graph_id"].split("_n")[0], g["N"], seed=g["seed"])
        assert fresh["sha256"] == g["sha256"]
