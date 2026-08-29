# -*- coding: utf-8 -*-
# GT-8b（领域鉴定器 v0 real_semantics 轴预登记复现）回归测试：
#   1) SPEC_GT8B §2 冻结域名哨兵（与既有族 L 6 域全异、manifest 稳定）；
#   2) 缓存缺失即停行为：ingest 缺缓存 → CacheMissingError 且报缺失路径；
#      eval 缺缓存 → 优雅跳过、verdict=inconclusive、如实列缺失域（不抛异常）；
#   3) verdict / 逐域阈值逻辑单测（支持 / 判死 / inconclusive / 边界值）；
#   4) 与族 L 特征口径一致性：合成缓存摄入的新图 real_semantics=1、
#      family="L"、named/filler 按 DAG 最长路径族口径、prompt_sha256 锚定。
import hashlib
import json
import os

import pytest

from mindmap_corpus_v20 import (CacheMissingError, FAMILY_L_DOMAINS, is_dag,
                                longest_path_family, parse_familyL_response)
from run_v20_gt8b_eval import (GT8B_MARGIN, GT8B_MIN_DOMAINS, GT8B_PRIOR_MIN,
                               domain_satisfied, gt8b_verdict)
from run_v20_gt8b_fetch import (GT8B_DOMAINS, GT8B_DOMAIN_BRIEF,
                                build_gt8b_prompts, gt8b_prompt_manifest)
from run_v20_gt8b_ingest import ingest_domain

# SPEC_GT8B §2 冻结（逐字）
SPEC_DOMAINS = ("chemical_elements", "chinese_dynasties")


def _synthetic_cache(domain, cache_dir, prompt_sha256):
    """构造一张合法 30 节点 DAG 的假缓存（测试内合成，零 API）：
    主干链 0→…→14 + 叶 15+k → k+1（毛虫拓扑，合法 DAG）。"""
    nodes = [f"概念{i}" for i in range(30)]
    edges = [[i, i + 1] for i in range(14)] + [[15 + k, k + 1]
                                               for k in range(15)]
    response = json.dumps({"nodes": nodes, "edges": edges},
                          ensure_ascii=False)
    rec = {"domain": domain, "prompt_sha256": prompt_sha256,
           "model": "test-synthetic", "response_text": response}
    os.makedirs(cache_dir, exist_ok=True)
    path = os.path.join(cache_dir, f"{domain}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False)
    return path


# ---------------------------------------------------------- 1) 冻结域名哨兵
def test_frozen_domains_sentinel():
    """SPEC_GT8B §2 冻结域名与 brief；与既有族 L 全部 6 域全异。"""
    assert GT8B_DOMAINS == SPEC_DOMAINS
    assert set(GT8B_DOMAINS).isdisjoint(FAMILY_L_DOMAINS)
    assert set(GT8B_DOMAIN_BRIEF) == set(SPEC_DOMAINS)
    assert "化学元素" in GT8B_DOMAIN_BRIEF["chemical_elements"]
    assert "中国历史朝代" in GT8B_DOMAIN_BRIEF["chinese_dynasties"]


def test_prompt_template_familyL_compatible():
    """生成 prompt 逐字沿用族 L 模板（只换域）：结构与 manifest 稳定。"""
    prompts = build_gt8b_prompts()
    manifest = gt8b_prompt_manifest()
    assert set(prompts) == set(SPEC_DOMAINS)
    for d, p in prompts.items():
        assert "有向无环概念脑图" in p and "30 到 45" in p
        assert GT8B_DOMAIN_BRIEF[d].split("（")[0] in p
        assert manifest[d]["prompt_sha256"] == hashlib.sha256(
            p.encode("utf-8")).hexdigest()


# ---------------------------------------------------------- 2) 缓存缺失即停
def test_ingest_cache_missing_stops(tmp_path):
    """ingest：缓存缺失 → CacheMissingError，消息含缺失文件路径。"""
    for d in SPEC_DOMAINS:
        with pytest.raises(CacheMissingError) as exc:
            ingest_domain(d, cache_dir=str(tmp_path / "nope"),
                          graph_dir=str(tmp_path / "graphs"))
        assert f"{d}.json" in str(exc.value)


def test_eval_cache_missing_graceful(tmp_path):
    """eval：图与先验缓存全缺 → 不抛异常，verdict=inconclusive，
    缺失域逐字披露，n_valid_domains=0（fetch_failed 不计入分母）。"""
    from run_v20_gt8b_eval import main as eval_main
    out = eval_main(cache_dir=str(tmp_path / "cache"),
                    graph_dir=str(tmp_path / "graphs"),
                    out_path=str(tmp_path / "out.json"))
    assert out["gt8b_verdict"]["verdict"] == "inconclusive"
    assert out["gt8b_verdict"]["n_valid_domains"] == 0
    assert sorted(out["cache_missing"]) == sorted(SPEC_DOMAINS)
    for d, msg in out["cache_missing"].items():
        assert f"L_{d}.json" in msg
    assert out["per_domain"] == {}


# ---------------------------------------------------------- 3) 判定逻辑单测
def test_domain_satisfied_thresholds():
    """逐域阈值：prior_named ≥ 0.6 且 > field_named + 0.2（含边界值）。"""
    ok = {"llm_prior": 0.6, "field_mean": 0.39}
    assert domain_satisfied(ok)
    assert not domain_satisfied({"llm_prior": 0.59, "field_mean": 0.0})
    assert not domain_satisfied({"llm_prior": 0.6, "field_mean": 0.4})
    assert not domain_satisfied({"llm_prior": 0.7, "field_mean": 0.5})
    assert not domain_satisfied({"llm_prior": None, "field_mean": 0.0})
    # 族 L 锚点口径自检：biological_taxonomy (1.0 vs 0.136) 应满足，
    # physics_concepts (0.484) 不满足（SPEC_GT8B §1 边界例外声明）
    assert domain_satisfied({"llm_prior": 1.0, "field_mean": 0.136})
    assert not domain_satisfied({"llm_prior": 0.484, "field_mean": 0.097})


def test_gt8b_verdict_logic():
    """verdict：2/2 满足 ⇒ supports；2/2 全反 ⇒ dead；其余 inconclusive。"""
    two_sat = [{"domain": "a", "satisfied": True},
               {"domain": "b", "satisfied": True}]
    assert gt8b_verdict(two_sat)["verdict"] == "supports_H_GT8B"
    assert gt8b_verdict(two_sat)["supported_H_GT8B"] is True
    two_dead = [{"domain": "a", "satisfied": False},
                {"domain": "b", "satisfied": False}]
    assert gt8b_verdict(two_dead)["verdict"] == "H_GT8B_dead"
    mixed = [{"domain": "a", "satisfied": True},
             {"domain": "b", "satisfied": False}]
    assert gt8b_verdict(mixed)["verdict"] == "inconclusive"
    # 单有效域（另一域 fetch_failed 不入列）无论满足与否均 inconclusive
    assert gt8b_verdict([{"domain": "a", "satisfied": True}])[
        "verdict"] == "inconclusive"
    assert gt8b_verdict([{"domain": "a", "satisfied": False}])[
        "verdict"] == "inconclusive"
    assert gt8b_verdict([])["verdict"] == "inconclusive"
    v = gt8b_verdict(two_sat)
    assert v["thresholds"] == {"prior_named_min": GT8B_PRIOR_MIN,
                               "margin_over_field": GT8B_MARGIN,
                               "min_domains": GT8B_MIN_DOMAINS}


# ---------------------------------------------------------- 4) 族 L 口径一致性
def test_ingest_synthetic_cache_familyL_consistency(tmp_path):
    """合成缓存摄入：real_semantics=1、family="L"、DAG、named/filler 按
    DAG 最长路径族口径、prompt_sha256 与预登记 manifest 一致锚定。"""
    cache_dir = str(tmp_path / "cache")
    graph_dir = str(tmp_path / "graphs")
    sha = gt8b_prompt_manifest()["chemical_elements"]["prompt_sha256"]
    _synthetic_cache("chemical_elements", cache_dir, sha)
    rec = ingest_domain("chemical_elements", cache_dir=cache_dir,
                        graph_dir=graph_dir)
    assert rec["real_semantics"] == 1 and rec["family"] == "L"
    edges = [tuple(e) for e in rec["edges"]]
    assert is_dag(rec["N"], edges)
    named_expected, _L, start, end = longest_path_family(rec["N"], edges)
    assert {tuple(e) for e in rec["named_edges"]} == set(named_expected)
    assert {tuple(e) for e in rec["filler_edges"]} == (
        set(edges) - set(named_expected))
    assert (rec["source"], rec["target"]) == (int(start), int(end))
    prov = rec["provenance"]
    assert prov["prompt_sha256_matches_preregistered"] is True
    assert prov["prompt_sha256"] == sha
    # 默认图目录落在 results/gt8b_cache/graphs（独立目录，不在 corpus/v20）
    from run_v20_gt8b_ingest import GRAPH_DIR
    assert "gt8b_cache" in GRAPH_DIR and "corpus" not in GRAPH_DIR


def test_ingest_prompt_sha_mismatch_flagged_not_blocked(tmp_path):
    """prompt_sha256 与预登记不一致：如实标记但不阻断摄入（族 L 同纪律）。"""
    cache_dir = str(tmp_path / "cache")
    graph_dir = str(tmp_path / "graphs")
    _synthetic_cache("chinese_dynasties", cache_dir, "0" * 64)
    rec = ingest_domain("chinese_dynasties", cache_dir=cache_dir,
                        graph_dir=graph_dir)
    assert rec["provenance"]["prompt_sha256_matches_preregistered"] is False


def test_eval_with_synthetic_caches_runs_offline(tmp_path):
    """端到端离线 eval：合成图缓存 + 合成先验缓存 → 产出结果 JSON，
    判定机械求值（零 API，仅本地确定性计算）。"""
    cache_dir = str(tmp_path / "cache")
    graph_dir = str(tmp_path / "graphs")
    manifest = gt8b_prompt_manifest()
    for d in SPEC_DOMAINS:
        _synthetic_cache(d, cache_dir, manifest[d]["prompt_sha256"])
        g = ingest_domain(d, cache_dir=cache_dir, graph_dir=graph_dir)
        # 合成先验：金边全集 confidence=1（合法 labels-only 先验格式）
        prior_items = [{"parent": u, "child": v, "confidence": 1.0}
                       for u, v in g["edges"]]
        with open(os.path.join(cache_dir, f"prior_{d}.json"), "w",
                  encoding="utf-8") as f:
            json.dump({"domain": d, "kind": "labels_only_prior",
                       "prompt_sha256": "t" * 64, "model": "test-synthetic",
                       "response_text": json.dumps(prior_items)}, f)
    from run_v20_gt8b_eval import main as eval_main
    out = eval_main(cache_dir=cache_dir, graph_dir=graph_dir,
                    out_path=str(tmp_path / "out.json"))
    assert out["cache_missing"] == {}
    assert out["gt8b_verdict"]["n_valid_domains"] == 2
    # 完美先验 ⇒ prior_named 必为 1.0，满足 ≥0.6 阈值
    for gid, v in out["per_domain"].items():
        assert v["named_summary"]["llm_prior"] == 1.0
        assert v["real_semantics"] == 1
    assert out["gt8b_verdict"]["verdict"] in (
        "supports_H_GT8B", "H_GT8B_dead", "inconclusive")
    assert os.path.exists(str(tmp_path / "out.json"))