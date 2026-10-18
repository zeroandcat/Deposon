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

V0.3 补造(T5, 2026-10-15, PI 2026-10-15 15:41 卡 Q2「授权补 T5 生成器」):
- 新增 T5 低资源博弈族 LowResourceTask(spec L54 逐字「低资源博弈 n=20,
  每决策只给 3 步推理, 最小信息情境」; 默认 n=20 取 spec 之声明值)
- task_families 由 4 族增为 5 族(T5 置末位 ⇒ T1-T4 之 prompt 生成序与
  seed 面逐字不变, 既有 12 格读数不受扰动)
- 判死线先冻(FTFB): KL-M41-1..3 与 kill_decision 之 2.0/0.3/1.5/1.8/0.1
  五切点逐字未动; ε*(H)=H/10 之 H_T5 锁值权属 PI(本棒只出候选)
- 锚漂移按授权漂移例外三要件落账(合法返工), 登记面见
  results/_t5_anchor_drift_authorized_register_2026_10_15.md
- 上方 V0 原字面(4 任务族 / 300 cells)历史留痕, 一字未改

V0.4 可答化(T3, 2026-10-15, PI 2026-10-15 17:03 卡 Q1「裁 B′」附带授权):
- 修复 T3_Trap 之构造缺陷 KD-3(M-41 b9feb5df8d44 §7: prompt 无可判据 ⇒
  10/15 拒答、读数不可解释为「模型失真」): prompt 改为携带两选项之实体
  含义与显式判准(净值两轮合计), 三型陷阱之正解均可自 prompt 推出
- options / correct / value / shuffle 四行逐字未动(仍为 2 选 1 ⇒ C1 类成员
  关系不变; greedy→Option A、deposit/cost→Option B 之映射未动; 0 新增随机数)
- T1/T2/T4/T5 之实现体一字未动 ⇒ 其 prompt digest 与既有 12 格读数不受扰动
- 判死线先冻(FTFB): KL-M41-1..3 与 kill_decision 之 2.0/0.3/1.5/1.8/0.1
  五切点逐字未动; H_T3=20 与 ε*(T3)=2 之锁值权属 PI(本棒只读, ⛔ 0 代改)
- 锚漂移按授权漂移例外三要件落账(合法返工), 登记面见
  results/_t3trap_answerable_drift_authorized_register_2026_10_15.md
- 新旧 prompt 属不同 treatment ⇒ 新旧读数不可直接可比(如实声明)
- 上方 V0/V0.2/V0.3 原字面历史留痕, 一字未改

V0.5 素材扩充 + Mixed 哨兵(2026-10-16, PI 2026-10-16 15:13 卡
  ask_3f46b6c6fc742839d88c8d54 Q2「授权增 Mixed 哨兵（推荐）」+ Q3「76 条全核准
  (推荐)」; 登记件 results/_pi_card_answers_register_2026_10_16_v25.md b682e95fba5e;
  候选件 results/_material_expansion_sourcing_2026_10_16.md afd1c0517a43):
- 素材扩充 76 条按族入库: T2 +35(20 联网 StrategyQA + 15 自制)、T3 +12 型、T4 +17
  博弈(5 联网 Nashpy + 12 自制)、T5 +12 情境 ⇒ 坍缩族 n_distinct 之目标面扩充
  (T4 均衡格 1→4 · T2 素材 4→35 · T3 型 3→15 · T5 情境 5→17)
- Mixed 哨兵: Matrix2x2Task 之 `nash` 由单一常量字符串改为逐博弈 `correct`;
  无纯策略纳什均衡之 2 博弈(T4-N05 Matching Pennies / T4-S06)之 `correct` 置为
  字面量 `Mixed`, `options` 增 `Mixed` 项(长度 3), `value` 另定(纯行动=安全水平,
  Mixed=博弈值; 平手以同格双方合计收益破平) ⇒ 贪心/反射通道 max 唯一(实算 17/17)
- 联网条目(T2 20 条 StrategyQA / T4 5 个 Nashpy 博弈)之许可面: 上游作者仓 LICENSE
  实测为 MIT ⇒ 嵌入 MIT 许可全文 + 出处署名于本文件(授权卡之条件)
- 判死线先冻(FTFB): 冻结件 .tmp/material_expansion_kill_freeze_2026_10_16.json
  (03a628456f0b) 落盘时点早于本文件之任何写入与坍缩族重测之任何 LLM 调用;
  KL-M41-1..3 与 kill_decision 之 2.0/0.3/1.5/1.8/0.1 五切点逐字未动;
  判死轨分母恒取该测量面 H_face/10(裁丙口径, O-1 生效件 30e0dee146ce)
- 锚漂移按授权漂移例外三要件落账(合法返工·第四层), 登记面见
  results/_material_expansion_drift_authorized_register_2026_10_16.md
- 上方 V0/V0.2/V0.3/V0.4 原字面历史留痕, 一字未改

V0.6 键面遮蔽(K-C3 遮蔽臂)(2026-10-17, PI 2026-10-17 23:19:08.583 卡
ask_af1c17ea9530032bd5a1669c Q3 opt1「键面走 K-C3 径——遮蔽 correct/value,
改 harness 构造, 使键面轴有方差」):
- 根因(逐字回读 results/_freeze_preexp_exec_2026_10_17.md §4-3): K-C1
  (singleton `correct`)与 K-C2(`{v＝best}`)于本素材面 15 格 × 3 seed 之
  270/270 prompt 实例化中逐格集合全等 ⇒ 二者在 `L` 构造上不可区分
  (`|K_t|≡1`)⇒ 键面轴 0 方差
- 新增「决策观测面之构造径」`build_decision_observation(p, mask_key_fields)`:
  默认关闭时原样返回传入之 prompt instance 对象本身(零复制 · 零改字 ·
  引用同一 ⇒ 输出与改造前逐字节同一); 开启时返回浅拷贝并剔除
  `correct`／`value` 两键 ⇒ K-C3 逐字「`K_t` 不暴露于决策之观测」
  (spec §3.5 之 LLM 信息瓶颈)
- 新增 `render_observation_text(观测)`: 按 `OBSERVATION_TEXT_ORDER` 逐键
  渲染观测面之 prompt 文本(遮蔽有效性之可测面); ⛔ 0 自造模板字面
- `ExperimentHarness` 新增可选参数 `mask_key_fields`(默认 `False`);`run()`
  之内新增一行观测面构造之分支(默认关闭 ⇒ 传入 `p` 本身 ⇒ 逐字节同一)
- 计分面仍读未遮蔽之 `p['correct']`(评分 ≠ 观测); ⛔ 0 以遮蔽态计分
- 判死线先冻(FTFB): .tmp/harness_mask_kill_freeze_2026_10_17.json
  (`5ecfe565fa1d`)落盘时点早于本文件之任何写入与本棒之任何验真测量;
  `KL-HM-1..6` 逐字载于该件, 事后 0 调
- 五切点面(`KL-M41-1..3` 与 `kill_decision` 之 2.0/0.3/1.5/1.8/0.1)与
  `U` 式之实施面不在本文件(实测 `U(M,T)`/`γ`/`τ_cert` 0 命中)⇒ 本棒 0 触碰
- 既有五族生成器体、机制体、五切点、`U` 式 ⛔ 0 一字未改;
  上方 V0/V0.2/V0.3/V0.4/V0.5 原字面历史留痕, 一字未改
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
V20_PATH = str(Path(__file__).resolve().parent.parent / 'results' / 'deposon_v20_baselines.json')
V21_PATH = str(Path(__file__).resolve().parent.parent / 'results' / 'deposon_v21_gtformal.json')

# V0.6 K-C3 键面遮蔽(见上方 V0.6 docstring): 决策观测面之构造径
# 被遮蔽之键面(逐字: K-C3「K_t 不暴露于决策之观测」)
MASKED_KEY_FIELDS = ('correct', 'value')
# 观测面渲染之键序(固定 ⇒ 渲染逐字节可复现; ⛔ 0 引入新模板字面)
OBSERVATION_TEXT_ORDER = ('prompt', 'options', 'correct', 'value')


def build_decision_observation(prompt_instance: Dict[str, Any],
                               mask_key_fields: bool = False) -> Dict[str, Any]:
    """决策观测面之构造(K-C3 遮蔽径之入口).

    mask_key_fields=False(默认 · 与改造前逐字同一之行为): 原样返回传入之
      prompt instance 对象本身 —— 零复制 · 零改字 · 引用同一 ⇒ 输出逐字节同一.
    mask_key_fields=True(K-C3 遮蔽臂): 返回浅拷贝, 其 `correct`／`value`
      两键被剔除 ⇒ 键面不暴露于决策之观测; 其余键逐字不动(引用同一对象,
      ⛔ 非重排 ⛔ 非改写 ⛔ 非重排选项序).
    """
    if not mask_key_fields:
        return prompt_instance
    observation = dict(prompt_instance)
    for key in MASKED_KEY_FIELDS:
        observation.pop(key, None)
    return observation


def render_observation_text(observation: Dict[str, Any]) -> str:
    """观测面之 prompt 文本渲染(遮蔽有效性之可测面).

    按 `OBSERVATION_TEXT_ORDER` 逐键渲染为 `<key>: <value>` 逐行文本;
    观测中不存在之键 0 渲染 ⇒ 遮蔽开启时 `correct`／`value` 两行 0 出现,
    而 `prompt`／`options` 两行之字面 0 受遮蔽开关影响.
    """
    lines = []
    for key in OBSERVATION_TEXT_ORDER:
        if key not in observation:
            continue
        lines.append('%s: %s' % (key, observation[key]))
    return '\n'.join(lines)


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
# ---------------------------------------------------------------------------
# T2 联网素材许可（嵌入 MIT 许可全文 + 出处署名；条件见 PI 2026-10-16 素材核准卡）
# 数据集: StrategyQA (TACL 2021) —— 上游作者仓 eladsegal/strategyqa
# 题面来源: https://github.com/eladsegal/strategyqa
# 许可（实测: 上游作者仓 LICENSE 全文直取, Copyright (c) 2021 Elad Segal）:
#   MIT License
#
#   Copyright (c) 2021 Elad Segal
#
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
#
#   The above copyright notice and this permission notice shall be included in
#   all copies or substantial portions of the Software.
#
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
# 旁证: allenai.org/data/strategyqa 元数据表载 MIT; 作者论文许可注
#       "StrategyQA under MIT License"。
# 出处署名: StrategyQA (Wai et al., TACL 2021); Elad Segal, Roy Schwartz, Riddell,
#           Alon Jacoby, Yoav Goldberg. "StrategyQA: A Dataset for Implicit
#           Multi-Step Reasoning". TACL 2021. MIT License.
# ---------------------------------------------------------------------------
        # V0.5.1 (T2 适配径 (b)「改模板」): PI 2026-10-16 15:54 卡
        # ask_4c35ce69603e7e0f776929f7 Q2 逐字「改裁 (b)（重测 T2 面）」
        #   ⇒ 本块 20 条联网项由 (a) 径（弃用 facts·提示内 0 证据面）改为 (b) 径：
        #     question 为 stem ＋ 官方 facts 压缩为 reason。
        # 依 找题件 afd1c0517a43 §1.1 适配注记之 (b) 义逐字：
        #     「(b) 改模板为 `{question}`＋`facts` 压缩为 `{reason}`」
        # facts 取自上游 wywy136/StrategyQA 之 strategyqa_train.json 全文本
        #   (raw 4,281,955 B / sha12 728e28b7d6bd / 2,290 题) 逐字直取；
        #   ⛔ 0 以找题件之「摘」面充全文（该摘面对 #19 有 1 字符伪影）。
        # 压缩式 ＝ ' ｜ '.join(facts)，机械拼接：⛔ 0 改写/摘要/翻译/重排任一字词，
        #   ⛔ 0 以 LLM 生成 reason（避正解泄漏与非确定），⛔ 0 令联网项 reason=None
        #   （reason=None 即 (a) 之形，⛔ 0 以 (a) 变体充 (b)）。
        # 许可见上方 MIT 全文。
        sqa_online = [
            ('Are more people today related to Genghis Khan than Julius Caesar?', 'Yes',
             ['Julius Caesar had three children.',
              'Genghis Khan had sixteen children.',
              'Modern geneticists have determined that  out of every 200 men today has DNA that can be traced to Genghis Khan.']),
            ('Could the members of The Police perform lawful arrests?', 'No',
             ['The members of The Police were musicians, not law enforcement officers.',
              'Only law enforcement officers can perform lawful arrests.']),
            ('Would a Monoamine Oxidase candy bar cheer up a depressed friend?', 'No',
             ['Depression is caused by low levels of serotonin, dopamine and norepinephrine.',
              'Monoamine Oxidase breaks down neurotransmitters and lowers levels of serotonin, dopamine and norepinephrine.']),
            ('Would a dog respond to bell before Grey seal?', 'Yes',
             ['Grey seals have no ear flaps and their ears canals are filled with wax.',
              'Grey seals hear better underwater when their ears open like a valve.',
              'Dogs have sensitive ears that can hear as far as a quarter of a mile away.']),
            ('Is a pound sterling valuable?', 'No',
             ['A pound sterling is fiat money.',
              'Fiat money is backed by government decree and has no intrinsic value.',
              'One pound sterling is worth about 1.24 US dollars by May of 2020.']),
            ('Is shrimp scampi definitely free of plastic?', 'No',
             ['Shrimp scampi is a dish made with shrimp.',
              'Shrimp have been found to contain microplastics.',
              'Microplastics are plastic material.']),
            ('Do the anchors on Rede Globo speak Chinese?', 'No',
             ['Rede Globo is a Brazilian television network.',
              'The official language of Brazil is Portuguese.']),
            ('Will the Albany in Georgia reach a hundred thousand occupants before the one in New York?', 'No',
             ['Albany, GA has around 75,000 people',
              'Albany, NY has almost 100,000 people']),
            ('Is a Boeing 737 cost covered by Wonder Woman (2017 film) box office receipts?', 'Yes',
             ['The average cost of a US Boeing 737 plane is 1.6 million dollars.',
              'Wonder Woman (2017 film) grossed over 800 million dollars at the box office.']),
            ('Is the language used in Saint Vincent and the Grenadines rooted in English?', 'Yes',
             ['The primary language spoken in Saint Vincent and the Grenadines is Vincentian Creole.',
              'Vincentian Creole is English-based, with elements of French, Antillean Creole, and indigenous South American and African languages.']),
            ('Can you buy Casio products at Petco?', 'No',
             ['Casio is a manufacturer of consumer electronics and watches',
              'Petco is a chain store that sells pet supplies like food, bowls, litter, toys, cages and grooming equipment']),
            ('Did the Space Race use relay batons?', 'No',
             ['The Space Race was a competition between the USA and USSR regarding spaceflight and exploration',
              'Relay batons are used in relay races',
              'Relay races are athletic track and field events']),
            ('Are Christmas trees dissimilar to deciduous trees?', 'Yes',
             ['Christmas trees are usually pine trees.',
              'Pine trees keep their needles all year round.']),
            ('Does Biochemistry study gluons?', 'No',
             ['Biochemistry studies role, function, and structure of biomolecules.',
              'Gluon, the so-called messenger particle of the strong nuclear force, which binds sub-atomic particles known as quarks within the protons and neutrons of stable matter as well as within heavier, short-lived particles created at high energies.',
              'biomolecules are comprised of atoms.']),
            ('Did land owners elect their rulers in the Kingdom of Hungary?', 'No',
             ['The Kingdom of Hungary was a monarchy.',
              'Monarchies do not allow citizens to elect their own rulers.']),
            ('Would Nancy Pelosi publicly denounce abortion?', 'No',
             ['Abortion is a topic that divides the Republican Party and the Democratic Party.',
              'Nancy Pelosi is a Democrat and appeals to that base.',
              'The Democratic base is largely pro-choice with abortion.']),
            ('Does Dragon Ball shows and movies fall short of Friday 13th number of projects?', 'Yes',
             ['Dragon Ball has 6 TV series, 3 TV specials, and 2 direct to video spinoffs as of 2020.',
              'Friday the 13th has 12 movies in the franchise and 1 TV series as of 2020.']),
            ('Would a student of the class of 2017 have amnesia about 9/11?', 'Yes',
             ['Childhood amnesia is common, with most adults not remembering their lives before 2 or 3 years of age',
              '9/11 occurred in 2001',
              'Students graduating high-school in 2017 would have been born in 1999']),
            ('Is greed the most prevalent of the Seven Deadly Sins?', 'No',
             ['Greed is a longing for wealth and power.',
              'White collar crime involves businesses stealing money or assets from people.',
              '5-10% of arrests per 100,000 arrests were for  white collar crime according to Department of Justice statistics.',
              'Gluttony is the overindulgence in food or similar things.',
              '39.8% of US adults were classified as overweight according to the National Center for Health Statistics.']),
            ('Would a psychic who admits to hot reading be trustworthy?', 'No',
             ['Hot reading is a technique used by people presenting themselves as psychics to acquire information about a subject prior to the psychic session.',
              'Hot reading is considered deception in the psychic community.']),
        ]
        facts = [
            ('A person is shivering in cold weather', 'Yes', 'They are cold'),
            ('A plant is wilting in the sun', 'Yes', 'It needs water'),
            ('A car is parked in a driveway', 'No', 'It is being driven'),
            ('A bird is flying south', 'Yes', 'It is migrating'),
            # V0.5 自制 15 条(同源构造: 隐含物理/生理机理须由情境推出)
            ('A kettle sits on a stove with its lid firmly closed',
             'Yes', 'Steam pressure is building inside it'),
            ('A metal spoon was left standing in a pot of soup on the stove',
             'Yes', 'The handle is hot enough to burn a hand'),
            ('A driver parks, removes the key and leaves the engine running',
             'Yes', 'The battery will eventually die'),
            ('A sealed jar of pickles sits in direct sunlight on a car seat',
             'Yes', 'The brine will spoil faster than it would in a cool cupboard'),
            ('A person crosses a carpeted room carrying a full glass of water',
             'Yes', 'They risk spilling it if they walk quickly'),
            ('A potted plant stands behind closed curtains on a windowsill in winter',
             'Yes', 'It is receiving very little light'),
            ('A bicycle is left unlocked in a busy city centre overnight',
             'Yes', 'It is likely to be stolen'),
            ('A person slices bread with a knife while holding it over a plugged-in '
             'toaster', 'Yes', 'They risk an electric shock'),
            ('A snowman is built in a sunny courtyard at midday',
             'Yes', 'It will be smaller by evening'),
            ('A sandwich is left on the dashboard of a parked car on a summer '
             'afternoon', 'Yes', 'The filling will spoil in the heat'),
            ('A person holds an umbrella indoors on a sunny day',
             'No', 'They are getting wet from rain'),
            ('A closed laptop is completely covered by a thick book',
             'No', 'The laptop is overheating from being covered'),
            ('A plant sits in soil that is soaking wet while the pot itself is bone dry',
             'No', 'The plant is severely dehydrated'),
            ('A person has just finished a large meal',
             'No', 'They will be starving again within ten minutes'),
            ('A refrigerator door is left standing wide open overnight',
             'No', 'The food inside will stay cold for longer'),
        ]
        n_online, n_self = len(sqa_online), len(facts)
        pool = n_online + n_self
        for i in range(n):
            k = i % pool
            if k < n_online:
                fact, label, sqa_facts = sqa_online[k]
                reason = ' ｜ '.join(sqa_facts)
            else:
                fact, label, reason = facts[k - n_online]
            options = ['Yes', 'No', 'Maybe', 'Always']
            random.shuffle(options)
            stem = (f'{fact}. Is the following statement true: {reason}?'
                    if reason is not None else f'{fact}')
            prompts.append({
                'prompt': stem,
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
        # V0.4 可答化: 三型陷阱之实体含义与显式判准(净值两轮合计之较高者);
        # 解: greedy→A(净6>净5)、deposit→B(净4>净3)、cost→B(净3>净2)
        clues = {
            'greedy': ('Two rounds remain. Option A: play the balanced line, gaining 2 '
                       'this round and 4 next round (net 6). Option B: play the greedy '
                       'line, gaining 5 this round and 0 next round (net 5). '),
            'deposit': ('Two rounds remain. Option A: deposit all 3 units into the growth '
                        'fund, which pays 3 this round and 0 next round (net 3). Option B: '
                        'keep 1 unit in the steady fund, which pays 2 this round and 2 '
                        'next round (net 4). '),
            'cost': ('Two rounds remain. Option A: take the fast route, which pays 4 this '
                     'round but charges a service cost of 1 in each of the two rounds '
                     '(net 2). Option B: take the slow route, which pays 3 this round '
                     'and charges no service cost (net 3). '),
            # V0.5 自制 12 型(正解皆自净值两轮合计实算; 0 平手)
            'greedy-fee': ('Two rounds remain. Option A: pays 5 this round and 2 next round, '
                           'but charges a service cost of 2 in each round (net 3). Option B: '
                           'pays 3 this round and 3 next round and charges no service cost '
                           '(net 6). '),
            'greedy-rev': ('Two rounds remain. Option A: pays 3 this round and 4 next round '
                           '(net 7). Option B: pays 6 this round and 0 next round (net 6). '),
            'deposit-rev': ('Two rounds remain. Option A: pays 2 this round and 3 next round '
                            '(net 5). Option B: pays 4 this round and 0 next round (net 4). '),
            'cost-rev': ('Two rounds remain. Option A: pays 5 this round but charges a service '
                         'cost of 1 (net 4). Option B: pays 2 this round and 1 next round and '
                         'charges no service cost (net 3). '),
            'compounding': ('Two rounds remain. Option A: pays 4 this round, which is invested '
                            'and returns 8 next round (net 12). Option B: pays 5 this round, '
                            'which is spent immediately (net 5). '),
            'resource-drain': ('Two rounds remain. Option A: pays 5 this round and then costs 3 '
                               'units of upkeep next round (net 2). Option B: pays 3 this round '
                               'and yields 2 units next round (net 5). '),
            'discount': ('Two rounds remain. Option A: pays 5 this round and 4 next round, and '
                         'next round counts for half (net 7). Option B: pays 6 this round and 0 '
                         'next round (net 6). '),
            'flat-vs-bonus': ('Two rounds remain. Option A: pays 2 this round and 2 next round, '
                              'plus a 3-unit completion bonus only if both rounds are played '
                              '(net 7). Option B: pays 4 this round and 1 next round with no '
                              'bonus (net 5). '),
            'guarantee': ('Two rounds remain. Option A: pays 5 this round but carries a 3-unit '
                          'penalty if the next round is missed (net 2). Option B: pays 4 this '
                          'round with no penalty in either round (net 4). '),
            'negative-both': ('Two rounds remain. Option A: pays 1 this round and costs 4 next '
                              'round (net -3). Option B: pays 0 this round and costs 2 next '
                              'round (net -2). '),
            'spend-now': ('Two rounds remain. Option A: pays 4 this round and 1 next round '
                          '(net 5). Option B: pays 5 this round but costs 3 in upkeep next '
                          'round (net 2). '),
            'hidden-carry': ('Two rounds remain. Option A: pays 3 this round and carries the '
                             'balance forward, earning 2 more next round (net 5). Option B: '
                             'pays 4 this round and nothing is carried forward (net 4). '),
        }
        # V0.5: 正解 = 净值较高者(实算, 逐型登记; 0 平手 ⇒ 0 平手判准)
        t3_answer = {
            'greedy': 'Option A', 'deposit': 'Option B', 'cost': 'Option B',
            'greedy-fee': 'Option B', 'greedy-rev': 'Option A',
            'deposit-rev': 'Option A', 'cost-rev': 'Option A',
            'compounding': 'Option A', 'resource-drain': 'Option B',
            'discount': 'Option A', 'flat-vs-bonus': 'Option A',
            'guarantee': 'Option B', 'negative-both': 'Option B',
            'spend-now': 'Option A', 'hidden-carry': 'Option A',
        }
        for i in range(n):
            trap = random.choice(sorted(t3_answer))
            options = ['Option A', 'Option B']
            correct = t3_answer[trap]
            random.shuffle(options)
            prompts.append({
                'prompt': f'Trap scenario {i+1} (type={trap}). {clues[trap]} Choose the '
                          f'option with the higher net total over the two rounds. '
                          f'Which option?',
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
        # T4 联网素材许可（嵌入 MIT 许可全文 + 出处署名）
        # 出处: https://github.com/drvinceknight/Nashpy
        #       docs/text-book/normal-form-games.rst（实取 status=OK · 12,381 B）
        # 许可（实测: 该仓 LICENSE 全文, MIT License）:
        #   MIT License
        #
        #   Copyright (c) 2016 Vince Knight
        #
        #   Permission is hereby granted, free of charge, to any person obtaining a
        #   copy of this software and associated documentation files (the
        #   "Software"), to deal in the Software without restriction, including
        #   without limitation the rights to use, copy, modify, merge, publish,
        #   distribute, sublicense, and/or sell copies of the Software, and to
        #   permit persons to whom the Software is furnished to do so, subject to
        #   the following conditions:
        #
        #   The above copyright notice and this permission notice shall be included
        #   in all copies or substantial portions of the Software.
        #
        #   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
        #   OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
        #   MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
        #   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
        #   CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
        #   TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
        #   SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
        # 出处署名: Nashpy normal-form games textbook, drvinceknight/Nashpy,
        #           Vince Knight. MIT License.
        # V0.5 博弈表 17 个: 5 联网(Nashpy·MIT, 见上方许可全文) + 12 自制.
        # 体例: (gid, 名称, 行方行动集, 列方行动集, A[4] 行方收益, B[4] 列方收益,
        #        均衡格(i,j), 判准, correct, value[3])
        # 均衡与正解皆由脚本实算(.tmp/me_t4_resolve_2026_10_16.py · 两实现交叉断言
        # 17/17 逐位一致), ⛔ 0 断言; Mixed 哨兵见 V0.5 docstring 与冻结件 rule_M1..M5。
        games = [
            ('T4-N01', "Prisoner's Dilemma", ('Cooperate', 'Defect'),
             ('Cooperate', 'Defect'), [3, 0, 5, 1], [3, 5, 0, 1], (1, 1), 'R3',
             'Defect', {'Cooperate': 0.0, 'Defect': 1.0}),
            ('T4-N02', 'Hawk Dove', ('Hawk', 'Dove'), ('Hawk', 'Dove'),
             [0, 3, 1, 2], [0, 1, 3, 2], (0, 1), 'R5', 'Dove',
             {'Hawk': 0.0, 'Dove': 1.0}),
            ('T4-N03', 'Pigs', ('Push', 'Do not push'), ('Push', 'Do not push'),
             [4, 2, 6, 0], [2, 3, -1, 0], (0, 0), 'R3', 'Push',
             {'Push': 2.0, 'Do not push': 0.0}),
            ('T4-N04', 'Coordination', ('Sport', 'Comedy'), ('Sport', 'Comedy'),
             [3, 1, 0, 2], [2, 1, 0, 3], (0, 0), 'R5', 'Sport',
             {'Sport': 3.0, 'Comedy': 0.0}),
            ('T4-N05', 'Matching Pennies', ('Heads', 'Tails'), ('Heads', 'Tails'),
             [1, -1, -1, 1], [-1, 1, 1, -1], None, 'R2', 'Mixed',
             {'Heads': -1.0, 'Tails': -1.0, 'Mixed': 0.0}),
            ('T4-S01', 'Stag Hunt', ('Stag', 'Hunt'), ('Stag', 'Hunt'),
             [4, 0, 3, 3], [4, 0, 3, 3], (0, 0), 'R4', 'Stag',
             {'Stag': 4.0, 'Hunt': 3.0}),
            ('T4-S02', 'Snowdrift', ('Cooperate', 'Defect'), ('Cooperate', 'Defect'),
             [4, 0, 3, 2], [4, 3, 0, 2], (0, 0), 'R4', 'Cooperate',
             {'Cooperate': 4.0, 'Defect': 3.0}),
            ('T4-S03', 'Asymmetric dominance', ('Offload', 'Keep'),
             ('Accept', 'Decline'), [1, 1, 3, 3], [4, 2, 4, 2], (1, 0), 'R3', 'Keep',
             {'Offload': 1.0, 'Keep': 3.0}),
            ('T4-S04', 'Anti-coordination', ('Home', 'Away'), ('Home', 'Away'),
             [0, 5, 4, 0], [0, 4, 6, 0], (1, 1), 'R4', 'Away',
             {'Home': 0.0, 'Away': 4.0}),
            ('T4-S05', 'Mutual dominance', ('Buy', 'Hold'), ('Enter', 'Exit'),
             [2, 1, 4, 3], [1, 3, 0, 2], (0, 1), 'R3', 'Hold',
             {'Buy': 1.0, 'Hold': 3.0}),
            ('T4-S06', 'No-pure-NE variant', ('Set A', 'Set B'), ('Set A', 'Set B'),
             [1, 0, 0, 1], [0, 1, 1, 0], None, 'R2', 'Mixed',
             {'Set A': 0.0, 'Set B': 0.0, 'Mixed': 0.5}),
            ('T4-S07', 'Investor / Founder', ('Fund', 'Withdraw'),
             ('Build', 'Pivot'), [3, 1, 4, 2], [2, 4, 1, 3], (1, 1), 'R3', 'Withdraw',
             {'Fund': 1.0, 'Withdraw': 2.0}),
            ('T4-S08', 'Loss-averse roles', ('Safe', 'Bold'), ('Safe', 'Bold'),
             [2, 3, 1, 2], [2, 3, 1, 2], (0, 1), 'R3', 'Safe',
             {'Safe': 3.0, 'Bold': 2.0}),
            ('T4-S09', 'Queue-jump', ('Queue', 'Jump'), ('Queue', 'Jump'),
             [0, 4, 3, 1], [0, 3, 4, 1], (1, 0), 'R5', 'Jump',
             {'Queue': 0.0, 'Jump': 3.0}),
            ('T4-S10', 'Volunteer dilemma', ('Volunteer', 'Free-ride'),
             ('Volunteer', 'Free-ride'), [1, 3, 2, 2], [1, 3, 2, 2], (0, 1), 'R4',
             'Volunteer', {'Volunteer': 3.0, 'Free-ride': 2.0}),
            ('T4-S11', 'Price war', ('Enter', 'Stay out'), ('Fight', 'Accommodate'),
             [2, 1, 3, 1], [1, 4, 0, 2], (0, 1), 'R4', 'Enter',
             {'Enter': 5.0, 'Stay out': 3.0}),
            ('T4-S12', 'Negative-payoff avoidance', ('Risk', 'Cede'),
             ('Risk', 'Cede'), [-1, 2, 0, 1], [-1, 2, 0, 1], (0, 1), 'R3', 'Risk',
             {'Risk': 2.0, 'Cede': 1.0}),
        ]
        n_games = len(games)
        prompts = []
        for i in range(n):
            gid, nm, ra, ca, A, B, cell, rule, correct, val = games[i % n_games]
            options = list(ra) + (['Mixed'] if cell is None else [])
            payoff_tbl = '; '.join(
                'you %s / they %s: (%d, %d)' % (ra[r], ca[c], A[r * 2 + c], B[r * 2 + c])
                for r in (0, 1) for c in (0, 1))
            prompts.append({
                'prompt': ('%s round %d. Payoff table (your payoff, their payoff): %s. '
                           'Choose your strategy.' % (nm, i + 1, payoff_tbl)),
                'options': options,
                'correct': correct,
                'value': {o: val[o] for o in options}
            })
        return prompts

    def name(self) -> str:
        return 'T4_2x2'


class LowResourceTask(TaskFamily):
    """T5: 低资源博弈(spec L54 逐字: n=20, 每决策只给 3 步推理, 最小信息情境)

    实现体例沿既有四族(T2 情境表轮转 + options 洗牌; T4 payoff 表定最优响应):
    每决策恰 3 步推理写进 prompt, 4 选 1(spec §3.1 统一决策空间),
    correct = payoff 最大之选项(理论最优响应, 供正典 D 计算),
    value = 逐选项 payoff(供 M1 反射通道 / M2 贪心读取)。
    """

    def generate_prompts(self, n: int = 20) -> List[Dict[str, Any]]:
        # 低资源博弈: 硬预算/限额约束下的最小信息决策情境
        # (情境, payoff 表, 3 步推理) —— 轮转取用, 保证每决策恰 3 步
        scenarios = [
            ('Water allocation', {'Dig well': 8, 'Cistern': 5, 'Truck': 6, 'Ration': 2},
             ['cap = 3 units, no extra data', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Power rationing', {'Diesel': 9, 'Rotate': 6, 'Shed': 4, 'Idle': 1},
             ['grid limit 3 units', 'only 3 steps may be spent',
              'higher payoff is better']),
            ('Clinic stock', {'Triage': 8, 'Borrow': 6, 'Bulk': 5, 'Wait': 2},
             ['shelf life 3 rounds', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Compute quota', {'Rent': 8, 'Cache': 7, 'Batch': 5, 'Idle': 1},
             ['quota = 3 units', 'only 3 steps may be spent',
              'higher payoff is better']),
            ('Food reserve', {'Swap': 7, 'Release': 6, 'Hold': 3, 'Waste': 1},
             ['reserve covers 3 days', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            # V0.5 自制 12 情境(四 payoff 值互异 ⇒ 贪心读取通道良定义, R-T5-3)
            ('Seed drill allocation',
             {'Sow deep': 8, 'Sow shallow': 6, 'Sow late': 4, 'Hold seed': 1},
             ['bag limit 3 units', 'only 3 steps may be spent',
              'yield is fixed per path']),
            ('Refrigerant charge',
             {'Top up': 9, 'Part charge': 6, 'Recover old': 4, 'Do nothing': 1},
             ['cylinder limit 3 units', 'only 3 steps may be spent',
              'higher payoff is better']),
            ('Antivenom vials',
             {'Two vials': 8, 'One vial': 6, 'Transfer stock': 5, 'Wait for resupply': 2},
             ['cold chain 3 hours', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Grid battery dispatch',
             {'Discharge now': 8, 'Hold for peak': 7, 'Trickle charge': 5, 'Idle': 1},
             ['reserve floor 3 units', 'only 3 steps may be spent',
              'higher payoff is better']),
            ('Lab pipette tips',
             {'Open new box': 8, 'Use reserves': 6, 'Substitute sizes': 5, 'Stop work': 2},
             ['budget cap 3 units', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Ferry rationing',
             {'Full load': 8, 'Half load': 6, 'Manifest only': 4, 'Delay sailing': 1},
             ['hold covers 3 days', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Upload bandwidth',
             {'Compress first': 8, 'Send raw': 6, 'Split over night': 5, 'Defer entirely': 2},
             ['uplink cap 3 units', 'only 3 steps may be spent',
              'higher payoff is better']),
            ('Purification tablets',
             {'Dose all now': 8, 'Dose at symptoms': 6, 'Test first': 4, 'No dose': 1},
             ['stock covers 3 days', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Generator fuel',
             {'Run full load': 8, 'Run part load': 7, 'Run intermittent': 4, 'Shut down': 1},
             ['fuel cap 3 units', 'only 3 steps may be spent',
              'higher payoff is better']),
            ('Cold-chain packs',
             {'Ship with packs': 8, 'Ship half packed': 6, 'Ship with ice': 5,
              'Ship nothing': 2},
             ['hold covers 3 days', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Sterile surgical kits',
             {'Open full kit': 8, 'Open partial kit': 6, 'Reuse tray': 3, 'Cancel list': 1},
             ['sterile stock 3 rounds', 'only 3 steps may be spent',
              'payoff is fixed per path']),
            ('Packet budget',
             {'Send full trace': 8, 'Send summary': 7, 'Send sampled trace': 5,
              'Send nothing': 1},
             ['link budget 3 units', 'only 3 steps may be spent',
              'higher payoff is better']),
        ]
        prompts = []
        for i in range(n):
            title, payoff, steps = scenarios[i % len(scenarios)]
            options = list(payoff.keys())
            random.shuffle(options)
            correct = max(payoff, key=payoff.get)
            prompts.append({
                'prompt': (f'{title} low-resource scenario {i+1}. '
                           f'Step 1: {steps[0]}. Step 2: {steps[1]}. '
                           f'Step 3: {steps[2]}. Which action maximizes payoff?'),
                'options': options,
                'correct': correct,
                'value': {o: payoff[o] for o in options}
            })
        return prompts

    def name(self) -> str:
        return 'T5_LowResource'


class ExperimentHarness:
    """实验 harness 调度"""

    def __init__(self, llm_client=None, seed: int | None = None,
                 mask_key_fields: bool = False):
        # seed 参数(V0.2 修复, KT_A1_SPEC §5.3 A3 种子复现: seed=42/123/456 三套;
        # 不传 seed 则沿用全局随机态, 保持向后兼容)
        # mask_key_fields(V0.6 K-C3 遮蔽径): 默认 False ⇒ 观测面与改造前逐字节
        # 同一; True ⇒ `correct`／`value` 不暴露于决策之观测
        self.seed = seed
        if seed is not None:
            random.seed(seed)
        self.mechanisms = [DeposonMechanism(), GreedyMechanism(), RandomMechanism()]
        self.task_families = [GSM8KTask(), StrategyQATask(), TrapTask(),
                              Matrix2x2Task(), LowResourceTask()]
        self.llm_client = llm_client
        self.mask_key_fields = mask_key_fields

    def run(self, n_decisions: int = 25) -> List[Dict[str, Any]]:
        """跑 3 机制 × 4 任务族 × 25 决策 = 300 cells"""
        results = []
        for mech in self.mechanisms:
            for task_fam in self.task_families:
                prompts = task_fam.generate_prompts(n_decisions)
                for i, p in enumerate(prompts):
                    # V0.6 K-C3 遮蔽: 默认关闭 ⇒ observation 即 p 本身(逐字节同一)
                    observation = build_decision_observation(p, self.mask_key_fields)
                    decision = mech.choose(p['options'], observation)
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
