# -*- coding: utf-8 -*-
# GT-8c（领域鉴定器 v0 real_semantics 轴扩样，Ark 后端）回归测试：
#   1) SPEC_GT8C §2 冻结域名哨兵（manifest 稳定）；
#   2) 缓存缺失即停行为：ingest 缺缓存 → CacheMissingError 且报缺失路径；
#      eval 缺缓存 → 优雅跳过、verdict=inconclusive、如实列缺失域（不抛异常）；
#   3) verdict / 逐域阈值逻辑单测（2/2 支持 / 1/2 mixed / 0/2 判死 /
#      inconclusive / 阈值恰等边界值）；
#   4) 与族 L 特征口径一致性：合成缓存摄入的新图 real_semantics=1、
#      family="L"、named/filler 按 DAG 最长路径族口径、prompt_sha256 锚定；
#   5) sanitize 纪律与 Ark 端点钉定：fetch 脚本含 Ark 端点/vendor、
#      key 仅从 ARK_API_KEY 环境变量读取、无明文密钥，sanitize_secret
#      兜底剔除密钥串。
#   全部 stub/合成缓存，零真实 API。
import hashlib
import json
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from llm_fetch import sanitize_secret
from mindmap_corpus_v20 import (CacheMissingError, is_dag,
                                longest_path_family)
from run_v20_gt8c_eval import (GT8C_MARGIN, GT8C_MIN_DOMAINS, GT8C_PRIOR_MIN,
                               domain_satisfied, gt8c_verdict)
from run_v20_gt8c_fetch import (ARK_ENDPOINT, ARK_MAX_TOKENS, ARK_MODEL,
                                ARK_TIMEOUT, ARK_VENDOR, GT8C_DOMAINS,
                                GT8C_DOMAIN_BRIEF, GT8C_SPEC, HTTP_BUDGET,
                                build_gt8c_prompts, gt8c_prompt_manifest)
from run_v20_gt8c_ingest import ingest_domain

# SPEC_GT8C §2 冻结（逐字）
SPEC_DOMAINS = ("biological_taxonomy", "programming_concepts")


def _synthetic_cache(domain, cache_dir, prompt_sha256):
    """构造一张合法 30 节点 DAG 的假缓存（测试内合成，零 API）：
    主干链 0→…→14 + 叶 15+k → k+1（毛虫拓扑，合法 DAG）。"""
    nodes = [f"概念{i}" for i in range(30)]
    edges = [[i, i + 1] for i in range(14)] + [[15 + k, k + 1]
                                               for k in range(15)]
    response = json.dumps({"nodes": nodes, "edges": edges},
                          ensure_ascii=False)
    rec = {"domain": domain, "prompt_sha256": prompt_sha256,
           "model": "test-synthetic", "vendor": "test-vendor",
           "response_text": response}
    os.makedirs(cache_dir, exist_ok=True)
    path = os.path.join(cache_dir, f"{domain}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rec, f, ensure_ascii=False)
    return path


# ---------------------------------------------------------- 1) 冻结域名哨兵
def test_frozen_domains_sentinel():
    """SPEC_GT8C §2 冻结域名与 brief；方向语义关键词在案。"""
    assert GT8C_DOMAINS == SPEC_DOMAINS
    assert set(GT8C_DOMAIN_BRIEF) == set(SPEC_DOMAINS)
    assert "生物分类" in GT8C_DOMAIN_BRIEF["biological_taxonomy"]
    assert "界/门/纲/目/科/属/种" in GT8C_DOMAIN_BRIEF["biological_taxonomy"]
    assert "编程概念" in GT8C_DOMAIN_BRIEF["programming_concepts"]
    assert "类别指向其成员" in GT8C_DOMAIN_BRIEF["biological_taxonomy"]
    assert "概念指向其实例" in GT8C_DOMAIN_BRIEF["programming_concepts"]


def test_prompt_template_familyL_compatible():
    """生成 prompt 逐字沿用族 L 模板（只换域）：结构与 manifest 稳定。"""
    prompts = build_gt8c_prompts()
    manifest = gt8c_prompt_manifest()
    assert set(prompts) == set(SPEC_DOMAINS)
    for d, p in prompts.items():
        assert "有向无环概念脑图" in p and "30 到 45" in p
        assert GT8C_DOMAIN_BRIEF[d].split("（")[0] in p
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
    from run_v20_gt8c_eval import main as eval_main
    out = eval_main(cache_dir=str(tmp_path / "cache"),
                    graph_dir=str(tmp_path / "graphs"),
                    out_path=str(tmp_path / "out.json"))
    assert out["gt8c_verdict"]["verdict"] == "inconclusive"
    assert out["gt8c_verdict"]["n_valid_domains"] == 0
    assert sorted(out["cache_missing"]) == sorted(SPEC_DOMAINS)
    for d, msg in out["cache_missing"].items():
        assert f"L_{d}.json" in msg
    assert out["per_domain"] == {}


# ---------------------------------------------------------- 3) 判定逻辑单测
def test_domain_satisfied_thresholds():
    """逐域阈值：prior_named ≥ 0.6 且 > field_named + 0.2（含恰等边界）。"""
    ok = {"llm_prior": 0.6, "field_mean": 0.39}
    assert domain_satisfied(ok)
    assert not domain_satisfied({"llm_prior": 0.59, "field_mean": 0.0})
    # 阈值恰等：prior=0.6 满足下界；margin 恰等（0.6 > 0.4+0.2 为假）不满足
    assert not domain_satisfied({"llm_prior": 0.6, "field_mean": 0.4})
    assert not domain_satisfied({"llm_prior": 0.7, "field_mean": 0.5})
    assert not domain_satisfied({"llm_prior": None, "field_mean": 0.0})
    # 族 L 锚点口径自检：biological_taxonomy Kimi 先验 (1.0 vs 0.136)
    # 满足；physics_concepts (0.484) 不满足（SPEC_GT8B §1 边界例外声明）
    assert domain_satisfied({"llm_prior": 1.0, "field_mean": 0.136})
    assert not domain_satisfied({"llm_prior": 0.484, "field_mean": 0.097})


def test_gt8c_verdict_logic():
    """verdict：2/2 满足 ⇒ supports；1/2 ⇒ mixed；0/2 ⇒ dead；
    有效域 <2 ⇒ inconclusive（SPEC_GT8C §5 先承诺口径）。"""
    two_sat = [{"domain": "a", "satisfied": True},
               {"domain": "b", "satisfied": True}]
    assert gt8c_verdict(two_sat)["verdict"] == "supports_H_GT8C"
    assert gt8c_verdict(two_sat)["supported_H_GT8C"] is True
    two_dead = [{"domain": "a", "satisfied": False},
                {"domain": "b", "satisfied": False}]
    assert gt8c_verdict(two_dead)["verdict"] == "H_GT8C_dead"
    mixed = [{"domain": "a", "satisfied": True},
             {"domain": "b", "satisfied": False}]
    assert gt8c_verdict(mixed)["verdict"] == "mixed"
    # 单有效域（另一域 fetch_failed 不入列）无论满足与否均 inconclusive
    assert gt8c_verdict([{"domain": "a", "satisfied": True}])[
        "verdict"] == "inconclusive"
    assert gt8c_verdict([{"domain": "a", "satisfied": False}])[
        "verdict"] == "inconclusive"
    assert gt8c_verdict([])["verdict"] == "inconclusive"
    v = gt8c_verdict(two_sat)
    assert v["thresholds"] == {"prior_named_min": GT8C_PRIOR_MIN,
                               "margin_over_field": GT8C_MARGIN,
                               "min_domains": GT8C_MIN_DOMAINS}


# ---------------------------------------------------------- 4) 族 L 口径一致性
def test_ingest_synthetic_cache_familyL_consistency(tmp_path):
    """合成缓存摄入：real_semantics=1、family="L"、DAG、named/filler 按
    DAG 最长路径族口径、prompt_sha256 与预登记 manifest 一致锚定。"""
    cache_dir = str(tmp_path / "cache")
    graph_dir = str(tmp_path / "graphs")
    sha = gt8c_prompt_manifest()["biological_taxonomy"]["prompt_sha256"]
    _synthetic_cache("biological_taxonomy", cache_dir, sha)
    rec = ingest_domain("biological_taxonomy", cache_dir=cache_dir,
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
    # 默认图目录落在 results/gt8c_cache/graphs（独立目录，不在 corpus/v20，
    # 不动 gt8b_cache）
    from run_v20_gt8c_ingest import GRAPH_DIR
    assert "gt8c_cache" in GRAPH_DIR and "corpus" not in GRAPH_DIR
    assert "gt8b_cache" not in GRAPH_DIR


def test_ingest_prompt_sha_mismatch_flagged_not_blocked(tmp_path):
    """prompt_sha256 与预登记不一致：如实标记但不阻断摄入（族 L 同纪律）。"""
    cache_dir = str(tmp_path / "cache")
    graph_dir = str(tmp_path / "graphs")
    _synthetic_cache("programming_concepts", cache_dir, "0" * 64)
    rec = ingest_domain("programming_concepts", cache_dir=cache_dir,
                        graph_dir=graph_dir)
    assert rec["provenance"]["prompt_sha256_matches_preregistered"] is False


def test_eval_with_synthetic_caches_runs_offline(tmp_path):
    """端到端离线 eval：合成图缓存 + 合成先验缓存 → 产出结果 JSON，
    判定机械求值（零 API，仅本地确定性计算）。"""
    cache_dir = str(tmp_path / "cache")
    graph_dir = str(tmp_path / "graphs")
    manifest = gt8c_prompt_manifest()
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
                       "vendor": "test-vendor",
                       "response_text": json.dumps(prior_items)}, f)
    from run_v20_gt8c_eval import main as eval_main
    out = eval_main(cache_dir=cache_dir, graph_dir=graph_dir,
                    out_path=str(tmp_path / "out.json"))
    assert out["cache_missing"] == {}
    assert out["gt8c_verdict"]["n_valid_domains"] == 2
    # 完美先验 ⇒ prior_named 必为 1.0，满足 ≥0.6 阈值
    for gid, v in out["per_domain"].items():
        assert v["named_summary"]["llm_prior"] == 1.0
        assert v["real_semantics"] == 1
    assert out["gt8c_verdict"]["verdict"] in (
        "supports_H_GT8C", "H_GT8C_dead", "mixed", "inconclusive")
    assert os.path.exists(str(tmp_path / "out.json"))


# ---------------------------------------------------------- 5) sanitize 纪律与 Ark 端点
def test_ark_endpoint_spec_and_no_plaintext_key():
    """fetch 脚本钉定 Ark 端点/模型/vendor/预算参数；key 仅从 ARK_API_KEY
    环境变量读取；源码无明文密钥串。"""
    assert ARK_ENDPOINT == ("https://ark.cn-beijing.volces.com"
                            "/api/v3/chat/completions")
    assert ARK_MODEL == "doubao-seed-evolving"
    assert ARK_VENDOR == "volces_ark_bytedance"
    assert GT8C_SPEC.endpoint == ARK_ENDPOINT and GT8C_SPEC.model == ARK_MODEL
    # SPEC_GT8C §4 预登记：max_tokens=32000、timeout=300s（B3 教训）
    assert ARK_MAX_TOKENS == 32000 and ARK_TIMEOUT == 300.0
    assert GT8C_SPEC.max_tokens == 32000 and GT8C_SPEC.timeout == 300.0
    assert GT8C_SPEC.max_attempts == 2 and HTTP_BUDGET == 8
    import run_v20_gt8c_fetch as fetch_mod
    src = open(fetch_mod.__file__, encoding="utf-8").read()
    assert 'os.environ.get("ARK_API_KEY")' in src
    assert "KIMI_API_KEY" not in src
    # 无明文密钥模式（Bearer/sk-/硬编码 token）
    for token in ("sk-", "Bearer sk", "AKLT", "ark_api_key ="):
        assert token not in src, f"plaintext key-like token in fetch: {token}"


def test_sanitize_secret_discipline():
    """sanitize_secret：异常/回显中若意外含 key，一律剔除（不写入日志）。"""
    secret = "dummy-test-secret-123"
    msg = f"HTTP 401: unauthorized, key={secret} rejected"
    out = sanitize_secret(msg, secret)
    assert secret not in out and "***" in out
    # 空 secret 不改写消息
    assert sanitize_secret(msg, "") == msg
    # EndpointSpec 错误路径（fetch_text）同样经 sanitize：stub transport
    from llm_fetch import fetch_text

    class _R:
        status_code = 401
        text = f"unauthorized key={secret}"

    def fake_transport(url, headers=None, json=None, timeout=None):
        assert headers["Authorization"] == f"Bearer {secret}"  # 仅请求头用
        return _R()

    counter = {"n": 0}
    outcome = fetch_text(GT8C_SPEC, "p", secret, counter=counter,
                         transport=fake_transport)
    assert outcome.content is None
    assert secret not in (outcome.last_err or "")
    assert counter["n"] == GT8C_SPEC.max_attempts  # ≤ MAX_ATTEMPTS=2 次尝试
