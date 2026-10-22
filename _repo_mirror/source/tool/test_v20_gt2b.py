# -*- coding: utf-8 -*-
"""GT-2B（docs/SPEC_GT2B.md）哨兵与判定逻辑单测。"""
import json
import os
import subprocess
import sys

import pytest

from mindmap_corpus_v20 import CORPUS_DIR, load_corpus
from run_v20_gt2b import (BANK_SEED, OUT_PATH, T_LEVELS, build_bank_t,
                          load_traps, verdict)

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _graphs():
    return {d: g for d, g in
            ((x["graph_id"][2:], x)
             for x in load_corpus(CORPUS_DIR, families=("L",)))
            if os.path.exists(os.path.join(HERE, "results",
                                           "gt2_attacker_cache", f"{d}.json"))}


@pytest.fixture(scope="module")
def graphs():
    return _graphs()


@pytest.fixture(scope="module")
def traps(graphs):
    return {d: load_traps(d) for d in graphs}


def test_options_always_four(graphs, traps):
    """哨兵：任意 T 下每题选项数恒 4（机会水平恒 25%）。"""
    for T in T_LEVELS:
        bank = build_bank_t(graphs, traps, T)
        assert len(bank) == 40
        for item in bank:
            assert len(item["options"]) == 4
            assert item["n_traps"] == T
            assert len(item["trap_labels"]) == T
            assert len(item["random_node_labels"]) == 3 - T
            assert len(set(item["trap_labels"])) == T  # 题内陷阱互不重复


def test_traps_not_in_graph_nodes(graphs, traps):
    """哨兵：陷阱标签不在图节点集内（field/prior -inf 机制免疫的前提）。"""
    for T in T_LEVELS:
        bank = build_bank_t(graphs, traps, T)
        for item in bank:
            labset = set(graphs[item["domain"]]["labels"])
            for t in item["trap_labels"]:
                assert t not in labset
            assert item["gold_label"] in labset
            for d in item["random_node_labels"]:
                assert d in labset


def test_verdict_supports():
    acc = {"rule_filter": {1: 0.5, 2: 0.4, 3: 0.3},
           "field_mean": {1: 0.9, 2: 0.92, 3: 0.88},
           "random": {1: 0.25, 2: 0.25, 3: 0.25}}
    v, detail = verdict(acc)
    assert v == "supports_H_GT2B" and detail["field_immunity_ok"]


def test_verdict_inconclusive_reversal():
    acc = {"rule_filter": {1: 0.5, 2: 0.3, 3: 0.4},  # 一级反转
           "field_mean": {1: 0.9, 2: 0.9, 3: 0.9},
           "random": {1: 0.25, 2: 0.25, 3: 0.25}}
    v, _ = verdict(acc)
    assert v == "inconclusive"


def test_verdict_inconclusive_tie():
    acc = {"rule_filter": {1: 0.4, 2: 0.4, 3: 0.3},  # 持平非严格递减
           "field_mean": {1: 0.9, 2: 0.9, 3: 0.9},
           "random": {1: 0.25, 2: 0.25, 3: 0.25}}
    v, _ = verdict(acc)
    assert v == "inconclusive"


def test_verdict_dead_monotone_up():
    acc = {"rule_filter": {1: 0.2, 2: 0.3, 3: 0.4},  # 单调上升 ⇒ 判死
           "field_mean": {1: 0.9, 2: 0.9, 3: 0.9},
           "random": {1: 0.25, 2: 0.25, 3: 0.25}}
    v, _ = verdict(acc)
    assert v == "H_GT2B_dead"


def test_verdict_field_immunity_flagged():
    acc = {"rule_filter": {1: 0.5, 2: 0.4, 3: 0.3},
           "field_mean": {1: 0.9, 2: 0.9, 3: 1.0},  # 超容差带
           "random": {1: 0.25, 2: 0.25, 3: 0.25}}
    v, detail = verdict(acc)
    assert v == "supports_H_GT2B" and not detail["field_immunity_ok"]


def test_deterministic_rebuild(graphs, traps):
    """同种子两次建库逐字节一致（进程内）。"""
    for T in T_LEVELS:
        a = json.dumps(build_bank_t(graphs, traps, T),
                       ensure_ascii=False, sort_keys=True)
        b = json.dumps(build_bank_t(graphs, traps, T),
                       ensure_ascii=False, sort_keys=True)
        assert a == b


def test_deterministic_across_processes():
    """跨进程确定性：独立子进程重跑 run() 与落盘 JSON 逐字节一致。"""
    code = ("import json,run_v20_gt2b;"
            "print(json.dumps(run_v20_gt2b.run(),ensure_ascii=False,indent=1))")
    outs = []
    for _ in range(2):
        r = subprocess.run([sys.executable, "-c", code], cwd=HERE,
                           capture_output=True, text=True)
        assert r.returncode == 0, r.stderr
        outs.append(r.stdout)
    assert outs[0] == outs[1]
    on_disk = open(OUT_PATH, encoding="utf-8").read()
    assert outs[0].strip() == on_disk.strip()
