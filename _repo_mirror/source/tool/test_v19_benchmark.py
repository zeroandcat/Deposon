# -*- coding: utf-8 -*-
# SPEC v1.9 Part B 测试: E9.3 修复开关 / E9.4 等权中性化 / E9.5 规则基线 /
# 缓存缺失显式报错。全部离线: no LLM API calls issued; inputs read from cache.
import os
import sys
import json
import hashlib

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.pop('KIMI_API_KEY', None)
os.environ.pop('DEPOSON_V14_HIGH_COUPLE_ALIAS', None)

import deposon_agents_v1_4 as core
from deposon_agents_v1_4 import (DeposonField, DeposonAgentSystem,
                                 resolve_high_couple_config, HIGH_COUPLE_GAIN)
import run_v19_benchmark_fixes as v19

RESULT_FILE = os.path.join(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__))), 'results', 'deposon_v19_benchmark_fixes.json')


def _toy_graph():
    return {
        'nodes': {
            'N1': {'energy': 0.3, 'type': 'number', 'value': 6.0},
            'N2': {'energy': 0.35, 'type': 'number', 'value': 2.0},
            'OP1': {'energy': 0.4, 'type': 'operation', 'op_type': 'multiplication'},
            'Goal': {'energy': 0.0, 'type': 'answer'},
            'Trap_X': {'energy': 0.1, 'type': 'trap', 'trap_type': 'wrong_op'},
        },
        'edges': {
            ('N1', 'OP1'): {'weight': 0.6, 'migration_barrier': 0.3},
            ('N2', 'OP1'): {'weight': 0.6, 'migration_barrier': 0.3},
            ('OP1', 'Goal'): {'weight': 0.8, 'migration_barrier': 0.2},
            ('N1', 'Trap_X'): {'weight': 0.9, 'migration_barrier': 0.1},
            ('Trap_X', 'Goal'): {'weight': 0.55, 'migration_barrier': 0.3},
        },
    }


# ---------------------------------------------------------------- E9.3
class TestHighCoupleFix:
    def test_default_is_true_fix(self):
        cfg = resolve_high_couple_config()
        assert cfg == {'mode': 'high_couple', 'use_deposon': True}

    def test_legacy_alias_only_with_explicit_switch(self, monkeypatch):
        monkeypatch.setenv('DEPOSON_V14_HIGH_COUPLE_ALIAS', '1')
        assert resolve_high_couple_config() == {'mode': 'v1_blocking',
                                                'use_deposon': True}
        monkeypatch.delenv('DEPOSON_V14_HIGH_COUPLE_ALIAS')
        assert resolve_high_couple_config()['mode'] == 'high_couple'

    def test_legacy_switch_off_values_not_alias(self, monkeypatch):
        for val in ('0', 'true', 'yes', ''):
            monkeypatch.setenv('DEPOSON_V14_HIGH_COUPLE_ALIAS', val)
            assert resolve_high_couple_config()['mode'] == 'high_couple'

    def test_spawn_actually_scales_g_couple(self):
        f_fix = DeposonField()
        f_fix.spawn_from_graph(_toy_graph(), mode='high_couple')
        f_blk = DeposonField()
        f_blk.spawn_from_graph(_toy_graph(), mode='v1_blocking')
        g_fix = f_fix.deposons['OP1'].g_couple
        g_blk = f_blk.deposons['OP1'].g_couple
        assert g_fix == pytest.approx(g_blk * HIGH_COUPLE_GAIN)
        assert g_fix != g_blk  # 不再是别名
        # blocking 语义保留
        assert all(d.g_aether == 0.0 for d in f_fix.deposons.values())

    def test_high_couple_changes_physics_not_identity(self):
        f_fix = DeposonField()
        f_fix.spawn_from_graph(_toy_graph(), mode='high_couple')
        f_blk = DeposonField()
        f_blk.spawn_from_graph(_toy_graph(), mode='v1_blocking')
        path = ['N1', 'OP1', 'Goal']
        t_fix = f_fix.process_path(path)['transmitted']
        t_blk = f_blk.process_path(path)['transmitted']
        assert t_fix != pytest.approx(t_blk)


# ---------------------------------------------------------------- E9.4
class TestEqualWeightControl:
    def test_flatten_sets_all_weights_equal(self):
        g = v19.flatten_graph_weights(_toy_graph(), weight=0.7)
        assert all(a['weight'] == 0.7 for a in g['edges'].values())
        # migration_barrier 不动, 原图不被修改
        assert g['edges'][('N1', 'Trap_X')]['migration_barrier'] == 0.1

    def test_flatten_does_not_mutate_original(self):
        g = _toy_graph()
        v19.flatten_graph_weights(g)
        assert g['edges'][('N1', 'Trap_X')]['weight'] == 0.9

    def test_verdict_matches_preregistered_rule(self):
        """从输出 JSON 重算判定, 验证与预登记规则一致 (不预设 PASS/FAIL)。"""
        if not os.path.exists(RESULT_FILE):
            pytest.skip('results json 尚未生成')
        out = json.load(open(RESULT_FILE, encoding='utf-8'))
        e = out['experiments']['E9.4_equal_weight_decoy_control']
        ok = True
        for b in e['benchmarks'].values():
            gap = b['accuracy_gap']
            p = b['mcnemar_unified_vs_no_deposon']['p_value']
            ok = ok and gap < 0.10 and p > 0.05
        assert (e['verdict'] == 'PASS') == ok


# ---------------------------------------------------------------- E9.5
class TestRuleBaseline:
    def test_keyword_matching(self):
        assert v19.label_hits_rule('Trap_DeadEnd')
        assert v19.label_hits_rule('Trap_guess')
        assert v19.label_hits_rule('trap_wrong_order')
        assert not v19.label_hits_rule('OP1')
        assert not v19.label_hits_rule('Goal')

    def test_rule_baseline_deterministic(self):
        prov = v19.Provenance()
        llm = v19.make_offline_backend()
        sample = v19.load_gsm8k_sample(prov)
        entry = sample[0]
        r1 = v19.eval_math_rule_baseline(llm, entry, v19.Provenance())
        r2 = v19.eval_math_rule_baseline(llm, entry, v19.Provenance())
        assert r1 == r2

    def test_no_api_key_anywhere(self):
        llm = v19.make_offline_backend()
        assert llm.api_key is None
        assert os.environ.get('KIMI_API_KEY') is None


# ---------------------------------------------------------------- 缓存纪律
class TestCacheDiscipline:
    def test_missing_math_cache_raises(self):
        llm = v19.make_offline_backend()
        with pytest.raises(v19.CacheMissingError):
            v19.offline_decompose_math(
                llm, '这道题绝不可能存在于任何缓存中 zzzqqq999', v19.Provenance())

    def test_missing_yesno_cache_raises(self):
        llm = v19.make_offline_backend()
        with pytest.raises(v19.CacheMissingError):
            v19.offline_decompose_yesno(
                llm, 'Is zzzqqq999 a real cached question?', v19.Provenance())

    def test_missing_input_file_raises(self):
        prov = v19.Provenance()
        with pytest.raises(v19.CacheMissingError):
            prov.record('/nonexistent/definitely_missing_cache.json')

    def test_provenance_sha256_correct(self):
        if not os.path.exists(RESULT_FILE):
            pytest.skip('results json 尚未生成')
        out = json.load(open(RESULT_FILE, encoding='utf-8'))
        prov = out['cache_provenance']
        assert len(prov) > 0
        for path, digest in prov.items():
            assert os.path.exists(path), path
            assert v19.sha256_file(path) == digest

    def test_run_was_cache_only(self):
        if not os.path.exists(RESULT_FILE):
            pytest.skip('results json 尚未生成')
        out = json.load(open(RESULT_FILE, encoding='utf-8'))
        stats = out['llm_stats']
        assert stats['fallbacks'] == 0
        assert stats['errors'] == 0
        assert stats['tokens_used'] == 0
        assert stats['cache_hits'] == stats['calls']
        assert out['physics_audit']['passed']
