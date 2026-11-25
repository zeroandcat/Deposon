#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
# Deposon Agents v1.4 —— 薄转发 shim (候选④合并, 2026-08-30)
# 实现已并入 deposon_agents.py (单模块 + version 配置);
# 本模块仅以单行类属性钉定 version="1.4", 与原 deposon_agents_v1_4.py
# (版本 1.4.0, GSM8K真实数据评测 + CoT基线) 的默认数值行为逐位一致。
# 全部方法为继承的同一实现。
# ============================================================
import deposon_agents as _core
from deposon_agents import (  # noqa: F401  (同名对象直接转发, `is` 同一)
    AgentConfig, DeposonState, EtherChannel, VectorizedDeposonScatter,
    PersistentCache, LLMBackend, ConceptDecomposer, deterministic_embedding,
    HundredQuestionBenchmark, TrapBenchmark,
    HIGH_COUPLE_GAIN, resolve_high_couple_config,
)


class KimiLLMBackend(_core.KimiLLMBackend):
    """v1.4 钉定: PROMPT_VERSION=1.3.2, max_tokens 默认 8000,
    LEGACY_PROMPT_VERSIONS=["1.3.1","1.3.0"], 英文 mini/steps 分解链,
    配额/空content 快速失败, cot_solve 基线。"""
    version = "1.4"


class DeposonField(_core.DeposonField):
    """v1.4 钉定: 运算节点 g_c/g_a=0.15/0.05 (v1.4 bugfix);
    high_couple 为 v1.9 E9.3 真修复 (g_aether=0 + g_couple x HIGH_COUPLE_GAIN)。"""
    version = "1.4"


class DeposonAgentSystem(_core.DeposonAgentSystem):
    """v1.4 钉定: ablation 的 high_couple 走 resolve_high_couple_config();
    内部 DeposonField 随 version="1.4"。"""
    version = "1.4"


class BenchmarkEvaluator(_core.BenchmarkEvaluator):
    """v1.4 钉定: 折叠去重连续操作数; computed_answer 兜底。"""
    version = "1.4"
