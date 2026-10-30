#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# η 五值择优·环五纯计算续跑——执行脚本（鲍勃-实验分析师·2026-10-23）
# 纪律：0 GPU / 0 API / 0 联网 —— 纯本地计算；既有件只读零改（harness 仅 import，0 改字节）
# 构造式（照录 d52a5d94a002 L77-L78，经 #20 §3.1 照录）：
#   w(o) = (1 - eta) * 1{v(o)=best} + eta * g_couple * (v(o)/best) + g_aether
#   P(o) = w(o) / sum_o w(o)   if the sum is positive
# 计数面①（R2 §2-0 照录）：逐格 15 项（3 机制 × 5 族）· 种子 42/123/456 · 各档 n = 20/20/20/10/20
# η 注入面（PI Q4 照录）：仅 M1 格注入（M2/M3 十格未注入）
# T4_2x2#04（best=0）已按 PI 2026-10-20 卡答排除（#20 §3 委-1 / 鲍勃 10-22 报告 §1-2 照录）
import sys, json, random
from fractions import Fraction

sys.path.insert(0, '〔本地路径已脱敏〕')
import exp_harness  # 只读导入（0 改字节）

SEEDS = [42, 123, 456]
FAMILY_ORDER = ['T1_GSM8K', 'T2_StrategyQA', 'T3_Trap', 'T4_2x2', 'T5_LowResource']
N_PER_FAMILY = [20, 20, 20, 10, 20]  # spec §3.3（R2 §2-0 照录）
TIERS = {
    'ETAC-D1': (Fraction(1, 2), Fraction(1, 1), Fraction(1, 10)),
    'ETAC-D2': (Fraction(1, 4), Fraction(2, 1), Fraction(0, 1)),
    'ETAC-D3': (Fraction(3, 4), Fraction(1, 5), Fraction(2, 1)),
    'ETAC-D4': (Fraction(9, 10), Fraction(1, 2), Fraction(1, 2)),
}

def gen_cells():
    """按 R2 口径生成逐族实例（逐 seed）。返回 {seed: {family: [cell,...]}}。"""
    out = {}
    for seed in SEEDS:
        random.seed(seed)
        fams = [exp_harness.GSM8KTask(), exp_harness.StrategyQATask(),
                exp_harness.TrapTask(), exp_harness.Matrix2x2Task(),
                exp_harness.LowResourceTask()]
        cells = {}
        for fam, n in zip(fams, N_PER_FAMILY):
            cells[fam.name()] = fam.generate_prompts(n)
        out[seed] = cells
    return out

def w_and_pmiss(value_map, eta, gc, ga):
    """单格构造级取值：逐选项 w(o) 与 P(miss)。返回 None 表示该格被排除（best=0）。"""
    vm = {o: Fraction(v).limit_denominator(10**9) for o, v in value_map.items()}
    best = max(vm.values())
    if best == 0:
        return None  # T4_2x2#04 排除口径（PI 2026-10-20 卡答）
    n = len(vm)
    best_opts = [o for o, v in vm.items() if v == best]
    assert len(best_opts) == 1, 'best 不唯一（本适用格集内不应发生）'
    w = {}
    for o, v in vm.items():
        w[o] = (1 - eta) * (1 if v == best else 0) + eta * gc * (v / best) + ga
    assert min(w.values()) >= 0, 'K-ETAC-3 w(o)>=0 违例'
    assert sum(w.values()) > 0, 'K-ETAC-3 sum w > 0 违例'
    p_miss = sum(wv for o, wv in w.items() if vm[o] != best) / sum(w.values())
    w_best = w[best_opts[0]]
    return {'w_best': w_best, 'w_nonbest': {o: w[o] for o in w if vm[o] != best},
            'p_miss': p_miss, 'n': n, 'best': best}

def fmt(fr):
    """Fraction -> '分数(≈6位小数)' 字符串。"""
    return '%s(≈%.6f)' % (fr, float(fr))

def main():
    cells_by_seed = gen_cells()
    # ── 三 seed 逐格全同校验（值结构面）────────────────────────────
    struct_sig = {seed: {} for seed in SEEDS}
    for seed in SEEDS:
        for fam in FAMILY_ORDER:
            sig = []
            for c in cells_by_seed[seed][fam]:
                vals = sorted(Fraction(v).limit_denominator(10**9) for v in c['value'].values())
                sig.append((len(c['value']), tuple(vals)))
            struct_sig[seed][fam] = sig
    seed_identical = all(struct_sig[s] == struct_sig[42] for s in SEEDS)

    report = {'seed_struct_identical': seed_identical, 'tiers': {}, 'meta': {}}

    # ── 逐档逐格实例化（K-ETAC-3 认证 + P(miss) 读数）──────────────
    for tname, (eta, gc, ga) in TIERS.items():
        tier = {'eta': str(eta), 'g_couple': str(gc), 'g_aether': str(ga), 'families': {}}
        ketac3_ok, excluded = True, []
        per_family_psets = {}
        for fam in FAMILY_ORDER:
            cells = cells_by_seed[42][fam]  # 值结构三 seed 全同 ⇒ 以 42 为代表（校验已过）
            pvals, details = [], []
            for idx, c in enumerate(cells):
                r = w_and_pmiss(c['value'], eta, gc, ga)
                if r is None:
                    excluded.append('%s#%02d' % (fam, idx))
                    continue
                ketac3_ok = ketac3_ok and (min(list(r['w_nonbest'].values()) + [r['w_best']]) >= 0)
                pvals.append(r['p_miss'])
                if fam in ('T4_2x2', 'T5_LowResource'):
                    details.append({'idx': idx, 'p_miss': fmt(r['p_miss']),
                                    'w_best': str(r['w_best']),
                                    'w_nonbest': {o: str(x) for o, x in r['w_nonbest'].items()}})
            pset = sorted(set(pvals))
            per_family_psets[fam] = set(pvals)
            tier['families'][fam] = {
                'n_instances': len(cells), 'n_countable': len(pvals),
                'n_distinct_p_miss': len(pset),
                'p_miss_set': [fmt(x) for x in pset],
                'w_best_options': sorted(set(str(w_and_pmiss(c['value'], eta, gc, ga)['w_best'])
                                              for c in cells
                                              if w_and_pmiss(c['value'], eta, gc, ga) is not None))
                                              if fam in ('T1_GSM8K', 'T2_StrategyQA', 'T3_Trap') else None,
                'details': details}
        # 跨族（R-A 构造级·层内判别式 J-6 面）：无材料投影之跨族取值集合
        cross = set()
        for fam in FAMILY_ORDER:
            cross |= per_family_psets[fam]
        # R-A+（构造级·含格材料量口径）：材料量按族相异 ⇒ 族间不坍缩 ⇒ 逐族计数之和
        raplus_count = sum(len(per_family_psets[f]) for f in FAMILY_ORDER)
        tier['K-ETAC-3'] = 'PASS' if ketac3_ok else 'VIOLATION'
        tier['excluded_cells'] = excluded
        tier['layer_R-A_cross_family_n_distinct'] = len(cross)
        tier['layer_R-A_cross_family_set'] = [fmt(x) for x in sorted(cross)]
        tier['layer_R-Aplus_n_distinct'] = raplus_count
        report['tiers'][tname] = tier

    # ── 主判据（冻结 R-A+·注入值口径）与辅判据 sep ──────────────────
    # R-A+ 定义（R2 §2-0 逐字）：x_g =（该面逐格注入值·|A|·支付向量·prompt 哈希）· ⛔0 含 M_g/T_g
    # η 面注入（R2 §2-5 照录）：{三元组@M1 五格, 未注入@M2/M3 十格} ⇒ R-A = 2（在册）
    # ⇒ R-A+ 全格口径 = 5(三元组,材料) + 5(未注入,材料) = 10／档；M1-only 口径 = 5／档
    for tname in TIERS:
        report['tiers'][tname]['main_R-Aplus_injected_full15'] = 10
        report['tiers'][tname]['main_R-Aplus_injected_M1only_variant'] = 5
    # sep（CMP-2 定义照录）：sep(v)=|{w∈同面在册候选: w 值向量≠v 值向量}|；四档三元组两两互异 ⇒ 各 3
    triplets = {t: (str(TIERS[t][0]), str(TIERS[t][1]), str(TIERS[t][2])) for t in TIERS}
    for t in TIERS:
        report['tiers'][t]['sep'] = sum(1 for u in TIERS if triplets[u] != triplets[t])
    # 哑火门（K-ETAC-13）：四档主判据恒同一常量？
    main_readings = {t: report['tiers'][t]['main_R-Aplus_injected_full15'] for t in TIERS}
    dud = len(set(main_readings.values())) == 1
    report['K-ETAC-13_dud'] = dud
    report['K-ETAC-13_note'] = ('四档主判据恒同一常量(10; 变体口径 5) ⇒ 哑火 ⇒ 判「不明」+停手报回'
                                 if dud else '主判据非常量 ⇒ 哑火门不触发')

    # ── E-C1 校准（对 R2 §2-5 在册读数）────────────────────────────
    cal = {'T1_expected': '3/14(≈0.214286)', 'T3_expected': '7/29(≈0.241379)',
           'T4_expected_R2口径(incl N05)': ['1/12(≈0.083333)', '8/41(≈0.195122)',
                                            '1/4(≈0.250000)', '19/63(≈0.301587)'],
           'T5_expected': ['≈0.453039', '≈0.45679', '≈0.473054', '≈0.47973',
                           '≈0.488372', '≈0.502825']}
    d1 = report['tiers']['ETAC-D1']['families']
    cal['T1_measured'] = d1['T1_GSM8K']['p_miss_set']
    cal['T2_measured'] = d1['T2_StrategyQA']['p_miss_set']
    cal['T3_measured'] = d1['T3_Trap']['p_miss_set']
    cal['T4_measured(排除N05后)'] = d1['T4_2x2']['p_miss_set']
    cal['T5_measured'] = d1['T5_LowResource']['p_miss_set']
    report['E-C1_calibration_vs_R2'] = cal
    report['meta'] = {
        'harness_sha12': 'ce64b9b97489(只读导入·0 改字节)',
        'seeds': SEEDS, 'n_per_family': dict(zip(FAMILY_ORDER, N_PER_FAMILY)),
        'construction': 'w(o)=(1-eta)*1{v(o)=best}+eta*g_couple*(v(o)/best)+g_aether (d52a5d94a002 L77-L78 照录)',
        'eta_injection': 'M1 only (PI Q4; R2 §2-5 照录)',
        'T4_N05': 'best=0 ⇒ 排除（PI 2026-10-20 卡答; #20 §3 委-1 照录）',
    }
    print(json.dumps(report, ensure_ascii=False, indent=1, default=str))

if __name__ == '__main__':
    main()
