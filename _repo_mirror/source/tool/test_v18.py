# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.8 API 补实验测试 (SPEC v1.8)
#   1. 三个 prompt 零泄漏: 只含标签行, 无任何边/图结构暗示
#   2. E1 确定性置换与 (perm[i],perm[j]) 映射/逆映射一致性
#   3. E2/E3 解析器: 容忍 markdown 围栏与杂质文本; 非法输入抛错
#   4. --dry-run 无 key 可运行、不发请求、不写任何文件
#   5. 融合复评分与 v1.7.1 逐位一致 (real 先验回归)
# 本文件全部使用 synthetic 数据测试机制; 不发起任何网络请求
# (mock 仅测解析/映射/dry-run 路径, mock 产出绝不写入 results/,
#  不假充真实实验结果)。
# ============================================================
import json
import os
import re
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from run_v15_experiment import reconstruct_mindmap
from deposon_diffusion import DiffusionConfig
from llm_prior import load_prior
import run_v18_api_supplements as v18


# ---------------------------------------------------------------
# 1. prompt 零泄漏 (E1/E2/E3 × 真实标签)
# ---------------------------------------------------------------
def _all_prompts():
    _N, _adj, _edges, labels, _meta = reconstruct_mindmap()
    return v18.build_all_prompts(labels), labels


def _assert_no_structure_hint(prompt: str, allow_recalled_edges_key: bool):
    # 无索引对 (u, v) 形式
    assert not re.search(r"\(\s*\d+\s*,\s*\d+\s*\)", prompt)
    # 无数字夹箭头 (3 -> 5 / 3 → 5); 与 v1.6 test_llm_prior 同口径 —
    # 「父 → 子」为方向占位说明, 非索引对 (llm_prior.py 已声明该约定)
    assert not re.search(r"\d+\s*->\s*\d+", prompt)
    assert not re.search(r"\d+\s*→\s*\d+", prompt)
    # 无 ASCII 箭头与边列表引入符
    assert "->" not in prompt
    assert "边：" not in prompt and "边:" not in prompt
    # "edge" 只允许出现在 SPEC 规定的 E2 schema 键 "recalled_edges" 中
    stripped = prompt.replace("recalled_edges", "")
    assert "edge" not in stripped.lower() or allow_recalled_edges_key
    if not allow_recalled_edges_key:
        assert "edge" not in prompt.lower()


def test_prompts_zero_leak_structure():
    prompts, _labels = _all_prompts()
    for tag in ("E1", "E2", "E3"):
        _assert_no_structure_hint(prompts[tag],
                                  allow_recalled_edges_key=(tag == "E2"))


def test_prompts_contain_all_label_lines():
    prompts, labels = _all_prompts()
    # E1 为打乱顺序, 逐标签检查其标签行存在 (索引随行号变)
    shuffled, perm = v18.shuffle_labels(labels)
    for i, lab in enumerate(shuffled):
        assert f"{i}: {lab}" in prompts["E1"]
    for tag in ("E2", "E3"):
        for i, lab in enumerate(labels):
            assert f"{i}: {lab}" in prompts[tag]


def test_prompts_no_gold_edge_cooccurrence():
    # 对全部 49 条金边 (u,v): 不存在同一行同时携带 u 与 v 两个索引行标记
    # (即没有任何两个标签行被同行共现/连接词暗示为一条边)。
    # 行标记用整词正则提取, 避免 "10: " 误含子串 "0: "。
    prompts, _labels = _all_prompts()
    _N, _adj, edges, _l, _m = reconstruct_mindmap()
    marker = re.compile(r"(?:^|\n)\s*(\d+):\s")
    for tag, prompt in prompts.items():
        for ln in prompt.split("\n"):
            idxs = {int(m) for m in re.findall(r"(?:^|(?<=\s))(\d+):\s", ln)}
            assert len(idxs) <= 1, f"{tag} prompt 行内含多个索引行标记: {ln!r}"
        idx_lines = marker.findall(prompt)
        assert len(idx_lines) == 45, f"{tag} prompt 应有 45 个标签行"
        for (u, v) in edges:
            for ln in prompt.split("\n"):
                idxs = {int(m) for m in re.findall(r"(?:^|(?<=\s))(\d+):\s", ln)}
                assert not (u in idxs and v in idxs), \
                    f"{tag} prompt 行内共现金边 ({u},{v}): {ln!r}"


def test_e1_prompt_is_prior_template_on_shuffled_labels():
    # E1 必须与 v1.6 使用同一模板 (build_prior_prompt), 仅输入为打乱标签
    prompts, labels = _all_prompts()
    shuffled, _perm = v18.shuffle_labels(labels)
    import llm_prior
    assert prompts["E1"] == llm_prior.build_prior_prompt(shuffled)
    assert prompts["E1"] != llm_prior.build_prior_prompt(labels)


def test_e3_prompt_adds_direction_definition_and_justification():
    prompts, labels = _all_prompts()
    import llm_prior
    assert prompts["E3"].startswith(llm_prior.build_prior_prompt(labels))
    assert "上位" in prompts["E3"] and "下位" in prompts["E3"]
    assert "justification" in prompts["E3"]


# ---------------------------------------------------------------
# 2. E1 置换映射正确性 (玩具 labels/perm)
# ---------------------------------------------------------------
def test_shuffle_deterministic_and_bijective():
    labels = [f"toy_{k}" for k in range(10)]
    s1, p1 = v18.shuffle_labels(labels)
    s2, p2 = v18.shuffle_labels(labels)
    assert s1 == s2 and list(p1) == list(p2)      # 确定性 (seed=188001)
    assert sorted(int(x) for x in p1) == list(range(10))  # 双射
    assert s1 == [labels[int(p1[i])] for i in range(10)]  # 构造约定


def test_map_shuffled_prior_toy():
    labels = ["a", "b", "c", "d", "e"]
    shuffled, perm = v18.shuffle_labels(labels)
    inv = np.empty(len(labels), dtype=int)
    inv[perm] = np.arange(len(labels))
    prior_sh = {(0, 1): 0.9, (2, 4): 0.5}
    mapped = v18.map_shuffled_prior(prior_sh, perm)
    # 显式映射: (i,j) → (perm[i], perm[j]), confidence 保留
    assert mapped == {(int(perm[0]), int(perm[1])): 0.9,
                      (int(perm[2]), int(perm[4])): 0.5}
    # 逆运算一致: 用 inv 映回打乱空间应还原原边
    back = {(int(inv[u]), int(inv[v])): c for (u, v), c in mapped.items()}
    assert back == prior_sh
    # 语义保持: 打乱空间边 (i,j) 连接的标签对 == 原空间边连接的标签对
    for (i, j) in prior_sh:
        u, v = int(perm[i]), int(perm[j])
        assert (labels[u], labels[v]) == (shuffled[i], shuffled[j])


# ---------------------------------------------------------------
# 3. 解析器 (synthetic 响应; 只测解析, 不写 results/)
# ---------------------------------------------------------------
def test_e2_parser_tolerates_fence_and_noise():
    text = ("好的，以下是结果：\n```json\n"
            '{"recognized": true, "confidence": 0.7, "basis": "标签风格熟悉", '
            '"recalled_edges": [{"parent": 0, "child": 1}, {"parent": 2, "child": 2}]}\n'
            "```\n希望有帮助。")
    out = v18.parse_contamination_response(text, 5)
    assert out["recognized"] is True
    assert out["confidence"] == pytest.approx(0.7)
    assert out["recalled_edges"] == [{"parent": 0, "child": 1}]  # 自指被忽略


def test_e2_parser_rejects_invalid():
    with pytest.raises(Exception):
        v18.parse_contamination_response("完全没有 JSON", 5)
    with pytest.raises(Exception):  # 缺字段
        v18.parse_contamination_response('{"recognized": true}', 5)
    with pytest.raises(Exception):  # 索引越界
        v18.parse_contamination_response(
            '{"recognized": true, "confidence": 0.5, "basis": "x", '
            '"recalled_edges": [{"parent": 0, "child": 99}]}', 5)
    with pytest.raises(Exception):  # recalled_edges 非数组
        v18.parse_contamination_response(
            '{"recognized": false, "confidence": 0.1, "basis": "x", '
            '"recalled_edges": {}}', 5)


def test_e3_parser_ignores_justification_and_fence():
    text = ('```json\n[{"parent": 0, "child": 1, "confidence": 0.95, '
            '"justification": "ROOT 是整体目标的上位"}, '
            '{"parent": 1, "child": 2, "confidence": 0.8, '
            '"justification": "路径原因到结果"}]\n``` 附加说明文字')
    prior, full = v18.parse_direction_response(text, 5)
    assert prior == {(0, 1): 0.95, (1, 2): 0.8}  # 只取 (parent,child,confidence)
    assert full[0]["justification"].startswith("ROOT")


def test_e3_parser_rejects_invalid():
    with pytest.raises(Exception):
        v18.parse_direction_response("不是 JSON 数组", 5)
    with pytest.raises(Exception):  # 索引越界
        v18.parse_direction_response(
            '[{"parent": 0, "child": 9, "confidence": 0.5}]', 5)
    with pytest.raises(Exception):  # 空数组
        v18.parse_direction_response("[]", 5)


def test_contamination_overlap_chance_math():
    # 45 节点: universe=1980; 抽 10 条期望重叠 49 金边 ≈ 0.2475
    _N, _adj, edges, _l, meta = reconstruct_mindmap()
    named = {tuple(e) for e in meta["path_edges_named"]}
    recalled = [{"parent": u, "child": v} for (u, v) in list(edges)[:10]]
    ov = v18.contamination_overlap(recalled, edges, named, 45)
    assert ov["n_recalled"] == 10 and ov["universe_directed_pairs"] == 1980
    assert ov["overlap_gold49"] == 10
    assert ov["expected_gold_chance"] == pytest.approx(10 * 49 / 1980, abs=1e-4)
    assert ov["expected_named_chance"] == pytest.approx(10 * 17 / 1980, abs=1e-4)


def test_direction_compare_toy():
    e3 = {(0, 1): 0.9, (2, 3): 0.8, (4, 5): 0.7}
    real = {(0, 1): 1.0, (3, 2): 0.9, (6, 7): 0.9}
    cmp16 = v18.direction_compare(e3, real)
    # 无向: 共有 {0,1} 与 {2,3} → jaccard = 2/4; 方向仅 {0,1} 一致 → 1/2
    assert cmp16["undirected_jaccard"] == pytest.approx(0.5)
    assert cmp16["direction_agreement"] == pytest.approx(0.5)


# ---------------------------------------------------------------
# 4. --dry-run: 无 key 可运行, 零请求, 零落盘
# ---------------------------------------------------------------
def test_dry_run_no_key_no_network_no_writes(monkeypatch, capsys, tmp_path):
    monkeypatch.delenv("KIMI_API_KEY", raising=False)

    def _boom(*a, **k):
        raise AssertionError("dry-run 不得发起任何网络请求")
    monkeypatch.setattr(v18.requests, "post", _boom)

    # 指向临时 results 目录, 断言 dry-run 不写任何文件
    out_path = os.path.join(tmp_path, "deposon_v18_api_supplements.json")
    monkeypatch.setattr(v18, "OUT_PATH", out_path)
    for tag, attr in (("E1", "CACHE_E1"), ("E2", "CACHE_E2"), ("E3", "CACHE_E3")):
        monkeypatch.setattr(v18, attr, os.path.join(tmp_path, f"{tag}.json"))

    rc = v18.main(["--dry-run"])
    assert rc == 0
    captured = capsys.readouterr().out
    assert "DRY-RUN" in captured and "sha256" in captured
    for tag in ("E1", "E2", "E3"):
        assert f"{tag} prompt" in captured
    assert not os.path.exists(out_path)
    assert os.listdir(tmp_path) == []


def test_dry_run_only_subset(monkeypatch, capsys):
    monkeypatch.delenv("KIMI_API_KEY", raising=False)
    monkeypatch.setattr(v18.requests, "post",
                        lambda *a, **k: (_ for _ in ()).throw(AssertionError()))
    rc = v18.main(["--dry-run", "--only", "E1,E3"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "E1 prompt" in out and "E3 prompt" in out and "E2 prompt" not in out


# ---------------------------------------------------------------
# 5. 融合复评分回归: real 先验臂逐位复现 v1.7.1
# ---------------------------------------------------------------
def test_fusion_reproduces_v171_real_prior():
    if not os.path.exists(v18.CACHE_V16) or not os.path.exists(v18.V171_PATH):
        pytest.skip("v1.6 先验缓存或 v1.7.1 结果缺失")
    prior = load_prior(v18.CACHE_V16)
    fusion = v18.score_loo(DiffusionConfig(), {"real": prior})
    assert fusion["denominators"] == {"overall": 49, "named": 17, "filler": 32}
    with open(v18.V171_PATH, "r", encoding="utf-8") as f:
        ref = json.load(f)["experiment_B"]["arms"]
    mapping = {"real_prior": "llm_prior",
               "real_hybrid_norm@0.5": "hybrid_norm@0.5",
               "real_hybrid_norm@2.0": "hybrid_norm@2.0",
               "real_hybrid_raw@0.5": "hybrid_raw@0.5",
               "real_hybrid_raw@2.0": "hybrid_raw@2.0"}
    for ours, theirs in mapping.items():
        for key in ("top3_hit", "top3_hit_named_path", "top3_hit_filler"):
            assert fusion["arms"][ours][key]["mean"] == pytest.approx(
                ref[theirs][key]["mean"], abs=1e-12), f"{ours}.{key}"


def test_score_loo_arm_naming_and_lambda_subset():
    toy_prior = {(0, 1): 0.9}
    fusion = v18.score_loo(DiffusionConfig(), {"toy": toy_prior})
    arms = fusion["arms"]
    assert "toy_prior" in arms
    assert "toy_hybrid_norm@0.5" in arms and "toy_hybrid_norm@2.0" in arms
    assert "toy_hybrid_raw@0.5" in arms and "toy_hybrid_raw@2.0" in arms
    assert "toy_hybrid_norm@1.0" not in arms  # λ 子集预登记为 {0.5, 2.0}


def test_e3_run_unpacks_parser_tuple_correctly(monkeypatch, tmp_path):
    """回归: run_e3 曾把 _post_prompt 的 (parsed, content) 误解包为 (prior, full)，
    而 parse_direction_response 本身返回 (prior, full) 二元组 → 二次包装导致
    direction_compare 处 'too many values to unpack'。本测试用 monkeypatch 的
    _post_prompt 验证解包路径与缓存结构（无网络）。"""
    labels = [f"lab{i}" for i in range(6)]
    real_prior = {(0, 1): 0.9, (1, 2): 0.8}
    toy_prior = {(0, 1): 0.95, (2, 3): 0.7}
    toy_full = [{"parent": 0, "child": 1, "confidence": 0.95,
                 "justification": "toy"},
                {"parent": 2, "child": 3, "confidence": 0.7,
                 "justification": "toy"}]

    def fake_post(prompt, key, parse_fn, counter):
        counter["http_attempts"] += 1
        return parse_fn("ignored"), "raw-content"

    monkeypatch.setattr(v18, "_post_prompt", fake_post)
    monkeypatch.setattr(v18, "parse_direction_response",
                        lambda t, n: (toy_prior, toy_full))
    cache = os.path.join(tmp_path, "e3.json")
    monkeypatch.setattr(v18, "CACHE_E3", cache)

    sec, prior = v18.run_e3(labels, real_prior, key="dummy", counter={"http_attempts": 0}, force=True)

    assert prior == toy_prior                      # 解包正确：不是 (prior, full) 元组
    assert sec["status"] == "ok" and sec["source"] == "live_api"
    assert sec["comparison_vs_v16_prior"]["n_e3_edges"] == 2
    saved = json.load(open(cache, encoding="utf-8"))
    assert isinstance(saved["prior"], list)        # 缓存结构良好：边列表而非原始字符串
    assert saved["prior"][0]["justification"] == "toy"


# ---------------------------------------------------------------- v1.8.1 E4

def test_e4_prompt_uses_contentless_tokens():
    labels = [f"真实语义标签{i}" for i in range(45)]
    p = v18.build_e4_prompt(labels)
    assert "item_00" in p and "item_44" in p
    for lab in labels:
        assert lab not in p                     # 语义内容被完全抹除
    # 与 v1.6 同模板: 结构指令保留
    assert "父 → 子" in p and "confidence" in p


def test_e4_prompt_differs_from_e1_and_real():
    labels = [f"lab{i}" for i in range(45)]
    assert v18.sha256_text(v18.build_e4_prompt(labels)) \
        != v18.sha256_text(v18.build_e1_prompt(labels))
    assert v18.sha256_text(v18.build_e4_prompt(labels)) \
        != v18.sha256_text(v18.build_prior_prompt(labels))


def test_e4_parser_empty_array_is_abstention():
    assert v18.parse_contentless_response("[]", 45) == {}
    assert v18.parse_contentless_response("```json\n[]\n```", 45) == {}


def test_e4_parser_nonempty_validates():
    out = v18.parse_contentless_response(
        '[{"parent": 0, "child": 3, "confidence": 0.9}]', 45)
    assert out == {(0, 3): 0.9}
    with pytest.raises(Exception):
        v18.parse_contentless_response('[{"parent": 0, "child": 99, "confidence": 0.5}]', 45)


def test_verdict_e4_abstention_supports():
    v = v18.verdict_e4(None, {"status": "abstained"}, {})
    assert v["status"] == "evaluated" and v["mode"] == "abstention"
    assert v["supports_semantic_claim"] is True


def test_verdict_e1_reinterpreted_permutation_invariance():
    sec = {"status": "ok",
           "permutation_invariance": {"e1_n_edges": 9, "real_n_edges": 9,
                                      "shared_edges": 9, "edge_set_identical": True,
                                      "confidence_pearson_on_shared": 0.98, "note": "x"}}
    v = v18.verdict_e1(sec)
    assert v["status"] == "evaluated" and v["permutation_invariant"] is True
    assert v["design_flaw_disclosed"] is True and "original_rule_voided" in v
    v2 = v18.verdict_e1({"status": "error"})
    assert v2["status"] == "pending"


def test_dry_run_includes_e4(monkeypatch, capsys, tmp_path):
    monkeypatch.delenv("KIMI_API_KEY", raising=False)
    monkeypatch.setattr(v18.requests, "post",
                        lambda *a, **k: (_ for _ in ()).throw(AssertionError()))
    monkeypatch.setattr(v18, "CACHE_E4", os.path.join(tmp_path, "e4.json"))
    rc = v18.main(["--dry-run", "--only", "E4"])
    assert rc == 0
    out = capsys.readouterr().out
    assert "E4 prompt" in out and "item_00" in out
    assert os.listdir(tmp_path) == []           # dry-run 不落盘
