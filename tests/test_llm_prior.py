# -*- coding: utf-8 -*-
# ============================================================
# Deposon v1.6 LLM 语义先验测试 (SPEC v1.6 §3, 5 组)
#   1. prompt 零泄漏: 只含标签, 不含任何边/结构信息 (无索引对形式)
#   2. 缓存往返一致 (synthetic 先验, 测机制不假充真实)
#   3. 无 key 报错路径 (RuntimeError, 不落盘)
#   4. synthetic 先验下 hybrid / llm_prior 臂分数正确性 (测机制)
#   5. 输出/缓存无 key 字样 (stub 传输层测管道; synthetic 响应绝不
#      写入 results/, 不假充真实调用结果)
# 本文件全部使用 synthetic 数据测试机制, 不产生任何真实 LLM 实验结论。
# ============================================================
import json
import os
import re
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import llm_prior
from llm_prior import build_prior_prompt, call_llm_prior, load_prior
import run_v16_llm_prior as v16


# ---------------------------------------------------------------
# 1. prompt 零泄漏: 只给标签, 无任何边/结构信息
# ---------------------------------------------------------------
def test_prompt_no_edge_leak():
    labels = ["ROOT", "GOAL_拓扑智能", "仿光子vsTDA", "组织记忆", "认知协议"]
    prompt = build_prior_prompt(labels)
    # 每个标签 (带索引) 都在 prompt 中 —— 标签是给 LLM 的唯一输入
    for i, lab in enumerate(labels):
        assert f"{i}: {lab}" in prompt
    # 无索引对形式的结构泄露: (u, v) / u->v / u→v
    assert not re.search(r"\(\s*\d+\s*,\s*\d+\s*\)", prompt)
    assert not re.search(r"\d+\s*->\s*\d+", prompt)
    assert not re.search(r"\d+\s*→\s*\d+", prompt)
    # schema 要求 JSON 数组输出
    assert '"parent"' in prompt and '"child"' in prompt
    assert '"confidence"' in prompt


def test_prompt_no_edge_leak_real_labels():
    # 用真实脑图标签 + 真实图的边集合逐边验证: 没有任何一条真实边
    # 以任何形式出现在 prompt 中 (prompt 仅由标签构造, 结构性保证)
    from run_v15_experiment import reconstruct_mindmap
    _N, _adj, edges, labels, _meta = reconstruct_mindmap()
    prompt = build_prior_prompt(labels)
    for (u, v) in edges:
        assert f"({u}, {v})" not in prompt
        assert f"{u}->{v}" not in prompt
        assert f"{u}→{v}" not in prompt


# ---------------------------------------------------------------
# 2. 缓存往返一致 (synthetic 先验 —— 手写 JSON, 测 load_prior 机制)
# ---------------------------------------------------------------
def test_cache_roundtrip(tmp_path):
    synthetic = {
        "spec_version": "v1.6",
        "prior": [{"parent": 0, "child": 1, "confidence": 0.9},
                  {"parent": 2, "child": 3, "confidence": 1.7},   # 越界截断到 1
                  {"parent": 4, "child": 5, "confidence": -0.2},  # 截断到 0
                  {"parent": 6, "child": 6, "confidence": 0.8}],  # 自指忽略
    }
    cache = tmp_path / "prior.json"
    cache.write_text(json.dumps(synthetic, ensure_ascii=False), encoding="utf-8")
    prior = load_prior(str(cache))
    assert prior[(0, 1)] == pytest.approx(0.9)
    assert prior[(2, 3)] == pytest.approx(1.0)
    assert prior[(4, 5)] == pytest.approx(0.0)
    assert (6, 6) not in prior
    assert len(prior) == 3


# ---------------------------------------------------------------
# 3. 无 key 报错路径: RuntimeError, 不产生缓存文件, 不 mock 冒充
# ---------------------------------------------------------------
def test_no_key_raises(tmp_path, monkeypatch):
    monkeypatch.delenv("KIMI_API_KEY", raising=False)
    cache = tmp_path / "prior.json"
    with pytest.raises(RuntimeError, match="KIMI_API_KEY 未设置"):
        call_llm_prior(str(cache), labels=["甲", "乙", "丙"])
    assert not cache.exists()


# ---------------------------------------------------------------
# 4. synthetic 先验下 hybrid / llm_prior 臂分数正确性 (测机制)
# ---------------------------------------------------------------
def test_hybrid_scores_synthetic():
    # synthetic: 4x4, 掩码行 u=0, 真边 (0,1), 候选 {1,2,3}
    shape = (4, 4)
    mask = np.zeros(shape, dtype=bool)
    mask[0, [1, 2, 3]] = True
    fg = np.full(shape, -np.inf)
    fg[0, 1] = 0.30   # field_guided 给真边的分
    fg[0, 2] = 0.50   # 物理场偏向候选 2
    fg[0, 3] = 0.20
    # synthetic 先验: 只覆盖 (0,1) 高置信 —— 纯测融合机制, 非真实 LLM 输出
    prior = {(0, 1): 0.9}
    P = v16.prior_score_matrix(prior, shape)
    assert P[0, 1] == pytest.approx(0.9)
    assert P[0, 2] == pytest.approx(0.0)

    # hybrid@λ=2: 0.30 + 2*0.9 = 2.10 > 0.50 + 2*0 → 排序翻转到真边
    h = v16.hybrid_scores(fg, P, mask, lam=2.0)
    assert h[0, 1] == pytest.approx(0.30 + 2.0 * 0.9)
    assert h[0, 2] == pytest.approx(0.50)
    assert np.isinf(h[1, 0]) and np.isinf(h[0, 0])  # 非掩码位置恒 -inf
    from run_v15_experiment import top3_hit_per_edge
    hit_fg = top3_hit_per_edge(fg, [(0, 1)], mask)[0]
    hit_hy = top3_hit_per_edge(h, [(0, 1)], mask)[0]
    assert hit_fg["rank"] == 1          # 物理场下真边排第 2 (候选2在前)
    assert hit_hy["rank"] == 0          # hybrid 后真边排第 1
    # λ=0.25 时先验不足以翻转: 0.30+0.225=0.525 > 0.50 仍翻转 → 用 λ=0.1 验证不翻转
    h_small = v16.hybrid_scores(fg, P, mask, lam=0.1)
    assert top3_hit_per_edge(h_small, [(0, 1)], mask)[0]["rank"] == 1

    # 纯先验臂: 未覆盖候选为 0, 覆盖者最高; 平局由 1e-6 级 tiebreak 确定性打破
    tiebreak = np.zeros(int(mask.sum()))
    s = v16.prior_arm_scores(P, mask, tiebreak)
    assert s[0, 1] == pytest.approx(0.9)
    assert s[0, 2] == pytest.approx(0.0)
    assert top3_hit_per_edge(s, [(0, 1)], mask)[0]["rank"] == 0
    assert np.isinf(s[2, 2])


# ---------------------------------------------------------------
# 5. 输出/缓存无 key 字样: stub 传输层测管道 (synthetic 响应,
#    仅写入 tmp_path, 绝不写入 results/, 不假充真实调用结果)
# ---------------------------------------------------------------
def test_no_key_string_in_outputs(tmp_path, monkeypatch):
    sentinel = "SENTINEL-TEST-VALUE-NOT-A-REAL-KEY"
    monkeypatch.setenv("KIMI_API_KEY", sentinel)

    class _FakeResp:  # synthetic 传输桩: 只测写盘/脱敏管道
        status_code = 200

        def json(self):
            return {"choices": [{"message": {"content":
                    '[{"parent": 0, "child": 1, "confidence": 0.5}]'}}]}

    monkeypatch.setattr(llm_prior.requests, "post",
                        lambda *a, **k: _FakeResp())
    cache = tmp_path / "prior.json"
    prior = call_llm_prior(str(cache), labels=["甲", "乙", "丙"])
    raw = cache.read_text(encoding="utf-8")
    assert sentinel not in raw          # key 字样绝不落盘
    assert "Authorization" not in raw
    assert prior[(0, 1)] == pytest.approx(0.5)
    # 缓存可被 load_prior 往返 (synthetic)
    assert load_prior(str(cache))[(0, 1)] == pytest.approx(0.5)

    # 错误路径同样脱敏: HTTP 回显里即便含 key, 异常消息也不得含
    class _ErrResp:
        status_code = 401
        text = f"invalid token: {sentinel} leaked?"

        def json(self):
            return {}

    monkeypatch.setattr(llm_prior.requests, "post",
                        lambda *a, **k: _ErrResp())
    with pytest.raises(RuntimeError) as excinfo:
        call_llm_prior(str(tmp_path / "p2.json"), labels=["甲", "乙", "丙"])
    assert sentinel not in str(excinfo.value)
    assert "***" in str(excinfo.value)
