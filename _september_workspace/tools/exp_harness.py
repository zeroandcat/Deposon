"""
实验 Harness (V1 折中补 8-10 天真实工作量)
===========================================

按 P-A V0 spec §3 + KT_A1_SPEC_V0 §3:
- 3 机制: M1 Deposon T+R+A / M2 Greedy / M3 Random
- 4 任务族: T1 GSM8K 风格 / T2 StrategyQA 风格 / T3 合成陷阱 / T4 2x2 矩阵
- 25 决策/任务
- 总 cell = 3 × 4 × 25 = 300 cells
- 沿用 v20 frozen 22 受控概念图(锚 6edb2aec1660)

实现:
- Mechanism 抽象基类(M1/M2/M3)
- TaskFamily 抽象基类(T1/T2/T3/T4)
- ExperimentHarness 调度

V0.2 修复(P1, 2026-09-09):
- ExperimentHarness 接受 seed 参数(KT_A1_SPEC §5.3 A3 种子复现:
  seed=42/123/456 三套, 原实现缺失导致实验不可复现)
- DeposonMechanism(M1) 在任务族无 scatter_weight 时退化为纯随机,
  四个任务族均不生成该键 → M1 与 M3 全程同分布, 机制对比失效;
  修复: 无 scatter_weight 时按 value 做三通道 T+R+A 合成权重
  (透射盯最优 + 反射按 value 耦合 + 耗散均匀底), eta/g_couple/g_aether 生效
"""

from __future__ import annotations

import os
import json
import random
import time
from abc import ABC, abstractmethod
from pathlib import Path
from typing import List, Dict, Any

# frozen data
V20_PATH = 'D:/私人资料/deposon-repo/results/deposon_v20_baselines.json'
V21_PATH = 'D:/私人资料/deposon-repo/results/deposon_v21_gtformal.json'


class Mechanism(ABC):
    """机制抽象基类"""

    @abstractmethod
    def choose(self, options: List[str], context: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class DeposonMechanism(Mechanism):
    """M1: Deposon T+R+A 三通道散射层"""

    def __init__(self, eta: float = 0.5, g_couple: float = 1.0, g_aether: float = 0.1):
        self.eta = eta
        self.g_couple = g_couple
        self.g_aether = g_aether

    def choose(self, options: List[str], context: Dict[str, Any]) -> str:
        # 三通道 T+R+A 合成权重(V0.2 修复: 无 scatter_weight 时不再退化为纯随机,
        # 否则 M1 与 M3 完全同分布, 机制对比失效; g_couple/g_aether 参数此前从未生效):
        #   透射 T: 直答通道, 权重集中在当前最优(有 scatter_weight 时直接按其加权)
        #   反射 R: 耦合通道, 按 value 相对量级加权(g_couple 调节耦合强度)
        #   耗散 A: 均匀底(g_aether), 保证非零探索
        # 实际实现需调 v21 frozen r_ga0.1 + T+R+A 守恒
        scatter = context.get('scatter_weight')
        if scatter:
            # 按权重采样
            weights = [scatter.get(o, 0.25) for o in options]
        else:
            values = context.get('value', {})
            if not values:
                # 无任何先验信息: 均匀采样(显式声明, 不冒充三通道)
                return random.choice(options)
            best = max(values.get(o, 0.0) for o in options)
            weights = []
            for o in options:
                v = values.get(o, 0.0)
                t = 1.0 if v == best else 0.0          # 透射: 最优直达
                r = (v / best) if best > 0 else 0.0    # 反射: 价值耦合(归一化)
                a = self.g_aether                       # 耗散: 均匀底
                weights.append((1.0 - self.eta) * t + self.eta * self.g_couple * r + a)
        total = sum(weights)
        if total <= 0:
            return random.choice(options)
        r = random.random() * total
        cum = 0
        for o, w in zip(options, weights):
            cum += w
            if r <= cum:
                return o
        return options[-1]

    def name(self) -> str:
        return 'M1_Deposon_TRA'


class GreedyMechanism(Mechanism):
    """M2: 纯 Greedy 贪心(无场,无守恒约束)"""

    def choose(self, options: List[str], context: Dict[str, Any]) -> str:
        # Greedy: 选 context['value'] 最高的 option
        values = context.get('value', {})
        if not values:
            return options[0]
        return max(options, key=lambda o: values.get(o, 0))

    def name(self) -> str:
        return 'M2_Greedy'


class RandomMechanism(Mechanism):
    """M3: Random 随机基线"""

    def choose(self, options: List[str], context: Dict[str, Any]) -> str:
        return random.choice(options)

    def name(self) -> str:
        return 'M3_Random'


class TaskFamily(ABC):
    """任务族抽象基类"""

    @abstractmethod
    def generate_prompts(self, n: int = 25) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class GSM8KTask(TaskFamily):
    """T1: GSM8K 风格多步算术"""

    def generate_prompts(self, n: int = 25) -> List[Dict[str, Any]]:
        prompts = []
        for i in range(n):
            a = random.randint(10, 99)
            b = random.randint(10, 99)
            c = random.randint(1, 9)
            correct = a + b * c
            options = [str(correct), str(correct + random.randint(1, 5)),
                       str(correct - random.randint(1, 5)), str(correct + random.randint(6, 10))]
            random.shuffle(options)
            prompts.append({
                'prompt': f'What is {a} + {b} * {c}?',
                'options': options,
                'correct': str(correct),
                'value': {o: 1.0 if o == str(correct) else 0.0 for o in options}
            })
        return prompts

    def name(self) -> str:
        return 'T1_GSM8K'


class StrategyQATask(TaskFamily):
    """T2: StrategyQA 风格隐式推理"""

    def generate_prompts(self, n: int = 25) -> List[Dict[str, Any]]:
        prompts = []
        facts = [
            ('A person is shivering in cold weather', 'Yes', 'They are cold'),
            ('A plant is wilting in the sun', 'Yes', 'It needs water'),
            ('A car is parked in a driveway', 'No', 'It is being driven'),
            ('A bird is flying south', 'Yes', 'It is migrating'),
        ]
        for i in range(n):
            fact, label, reason = facts[i % len(facts)]
            options = ['Yes', 'No', 'Maybe', 'Always']
            random.shuffle(options)
            prompts.append({
                'prompt': f'{fact}. Is the following statement true: {reason}?',
                'options': options,
                'correct': label,
                'value': {o: 1.0 if o == label else 0.0 for o in options}
            })
        return prompts

    def name(self) -> str:
        return 'T2_StrategyQA'


class TrapTask(TaskFamily):
    """T3: 合成陷阱(2 选 1 迷惑)"""

    def generate_prompts(self, n: int = 25) -> List[Dict[str, Any]]:
        prompts = []
        for i in range(n):
            trap = random.choice(['greedy', 'deposit', 'cost'])
            options = ['Option A', 'Option B']
            correct = 'Option A' if trap == 'greedy' else 'Option B'
            random.shuffle(options)
            prompts.append({
                'prompt': f'Trap scenario {i+1} (type={trap}). Which option?',
                'options': options,
                'correct': correct,
                'value': {o: 1.0 if o == correct else 0.5 for o in options}
            })
        return prompts

    def name(self) -> str:
        return 'T3_Trap'


class Matrix2x2Task(TaskFamily):
    """T4: 2x2 矩阵博弈(明确纳什均衡)"""

    def generate_prompts(self, n: int = 25) -> List[Dict[str, Any]]:
        # Prisoner's Dilemma: T>R>P>S
        payoff = {
            ('Cooperate', 'Cooperate'): (3, 3),
            ('Cooperate', 'Defect'): (0, 5),
            ('Defect', 'Cooperate'): (5, 0),
            ('Defect', 'Defect'): (1, 1)
        }
        nash = 'Defect'
        prompts = []
        for i in range(n):
            options = ['Cooperate', 'Defect']
            prompts.append({
                'prompt': f"Prisoner's Dilemma round {i+1}. Choose your strategy.",
                'options': options,
                'correct': nash,
                'value': {o: payoff[(o, 'Defect')][0] for o in options}
            })
        return prompts

    def name(self) -> str:
        return 'T4_2x2'


class ExperimentHarness:
    """实验 harness 调度"""

    def __init__(self, llm_client=None, seed: int | None = None):
        # seed 参数(V0.2 修复, KT_A1_SPEC §5.3 A3 种子复现: seed=42/123/456 三套;
        # 不传 seed 则沿用全局随机态, 保持向后兼容)
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.mechanisms = [DeposonMechanism(), GreedyMechanism(), RandomMechanism()]
        self.task_families = [GSM8KTask(), StrategyQATask(), TrapTask(), Matrix2x2Task()]
        self.llm_client = llm_client

    def run(self, n_decisions: int = 25) -> List[Dict[str, Any]]:
        """跑 3 机制 × 4 任务族 × 25 决策 = 300 cells"""
        results = []
        for mech in self.mechanisms:
            for task_fam in self.task_families:
                prompts = task_fam.generate_prompts(n_decisions)
                for i, p in enumerate(prompts):
                    decision = mech.choose(p['options'], p)
                    is_correct = decision == p['correct']
                    results.append({
                        'mechanism': mech.name(),
                        'task_family': task_fam.name(),
                        'decision_idx': i,
                        'decision': decision,
                        'correct': p['correct'],
                        'is_correct': is_correct
                    })
        return results


if __name__ == '__main__':
    # 自检: 跑 mini test (不调 LLM), seed=42 保证可复现
    harness = ExperimentHarness(llm_client=None, seed=42)
    results = harness.run(n_decisions=2)
    print(f'OK: ran {len(results)} cells (mini test, seed=42)')
    print(f'Sample: {results[0]}')
    # 同 seed 重跑结果一致(可复现性验证)
    harness2 = ExperimentHarness(llm_client=None, seed=42)
    results2 = harness2.run(n_decisions=2)
    assert results == results2, '同 seed 两次运行结果不一致'
    print('OK: 同 seed 两次运行结果完全一致(可复现)')
