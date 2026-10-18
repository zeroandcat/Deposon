"""
T+R+A=1 守恒审计函数 (V0.3 真守恒重算检测器)
=============================================

按 KT_B1_SPEC_V0 §3.4 + 工单#14 升级(2026-09-09, Option A 返工):
- 层1 顶锚: physics_audit.t_plus_r_plus_a_max_deviation 分级阈值判定
  (残差 <1e-15 PASS / <1e-12 GRAY / >=1e-12 FAIL);
  顶锚字段被删/类型坏/NaN, 或 physics_audit 键集较原件缺键 → 破坏
- 层2 per_problem 真重算: 遍历 experiments → benchmarks → per_problem
  (兼容 FORM_A dict{条件名:[记录]} / FORM_B list[记录] 两形态), 逐记录:
  * 显式 t/r/a 数值字段 → 直接验和(伪字段注入必检出; 账本残缺/类型坏 → 破坏)
  * 无显式字段 → parse_pred + tra_decomposition 从 pred/predicted 合成验和
    (v19 记录无显式 T/R/A 字段, 合成恒守恒, 可检出信号 = NaN/inf 合成异常)
  * 审计链不变量交叉对账(下列各项均经 v19 全量 1592 条实测零违例后才启用,
    is_correct⟺命中答案 / is_correct⟺无Trap 等 v19 自身不成立的检查一律不启用,
    避免对原始数据误报):
      - trap_hit 为真 ⟺ 推理链含 Trap 前缀节点
      - trap_hit 为字符串 ⟹ 必为推理链节点之一
      - 容器内 id 严格递增(manifest 对账)
      - 推理链末节点收口为 Goal
  * 结构完整性 vs original_data: 容器集/记录数/记录键集一致
    (记录被删/字段被删必检出)
- 检测器召回背景(工单#14): 上版只查顶层锚, per_problem 层攻击
  (manifest_swap / chain_modify) 0% 召回; 本版账平审计以
  "真 T+R+A 重算 + 审计链账本交叉对账"为准
- 空数据(空 dict / 无 experiments 键 / 空 per_problem / 零记录) = 无可破坏 → PASS;
  任何 edge case 输入不抛异常(0 异常纪律)
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

V19_PATH = Path('D:/私人资料/deposon-repo/results/deposon_v19_benchmark_fixes.json')

# 分级阈值(工单#14): 残差 <1e-15 → PASS; <1e-12 → GRAY; >=1e-12 → FAIL
PASS_THRESHOLD = 1e-15
GRAY_THRESHOLD = 1e-12

# 上版判死线常量(保留旧名防外部引用断裂; 分级判定以 PASS/GRAY_THRESHOLD 为准)
CONSERVATION_THRESHOLD = 1e-10


def parse_pred(v) -> float:
    """记录预测值统一归一化到 [0,1](5 文件共用统一定义, 与
    tools/exp_harness.py / tools/llm_client.py 保持一致, 勿单独改动):
    - bool → 1.0/0.0; 数值 → clamp 到 [0,1]
    - 'yes'/'y'/'true'/'1' → 1.0; 'no'/'n'/'false'/'0' → 0.0
    - 数值字符串 → clamp; 其余(含 None/非法串/未知类型) → 0.0
    """
    if v is None:
        return 0.0
    if isinstance(v, bool):
        return 1.0 if v else 0.0
    if isinstance(v, (int, float)):
        return max(0.0, min(1.0, float(v)))
    if isinstance(v, str):
        s = v.strip().lower()
        if s in ('yes', 'y', 'true', '1'):
            return 1.0
        if s in ('no', 'n', 'false', '0'):
            return 0.0
        try:
            return max(0.0, min(1.0, float(v)))
        except ValueError:
            return 0.0
    return 0.0


def tra_decomposition(pred_value, eta=0.5, g_couple=1.0):
    """T+R+A 三相分解, 严格恒等和=1: T=(1-eta)v, R=eta*g_couple*(1-v), A=1-T-R.

    5 文件共用统一定义(与 tools/exp_harness.py / tools/llm_client.py 一致).
    """
    v = parse_pred(pred_value)
    T = (1.0 - eta) * v
    R = eta * g_couple * (1.0 - v)
    A = 1.0 - T - R
    return T, R, A


def load_v19():
    """只读加载 v19 冻结基准(绝不写回)"""
    with open(V19_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# 层2 遍历与逐记录检查
# ---------------------------------------------------------------------------

def _iter_containers(data):
    """枚举 per_problem 记录容器(兼容 FORM_A/FORM_B).

    yield (路径元组, 记录列表); 路径元组 = (experiment, benchmark, condition|None).
    任何一层类型异常均安全跳过(容器集对比会兜住"容器被删/改类型"的破坏).
    """
    if not isinstance(data, dict):
        return
    exps = data.get('experiments')
    if not isinstance(exps, dict):
        return
    for ename, exp in exps.items():
        if not isinstance(exp, dict):
            continue
        bms = exp.get('benchmarks')
        if not isinstance(bms, dict):
            continue
        for bm, b in bms.items():
            if not isinstance(b, dict):
                continue
            pp = b.get('per_problem')
            if isinstance(pp, dict):
                # 形态 A: {条件名: [记录]}
                for cond, recs in pp.items():
                    if isinstance(recs, list):
                        yield (ename, bm, cond), recs
            elif isinstance(pp, list):
                # 形态 B: 直接 [记录]
                yield (ename, bm, None), pp


def _is_plain_number(x) -> bool:
    """纯数值判定(int/float 且非 bool; bool 是 int 子类, 显式账本里视为类型坏)"""
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _check_record(rec, orig_rec, reasons, prefix):
    """单记录守恒重算, 返回 |T+R+A-1| 残差(float).

    结构破坏(账本残缺/类型坏/NaN/字段被删) → 记 reason 并返回 inf.
    """
    # 结构完整性: 记录键集与原件一致(字段被删/新增键均检出)
    if orig_rec is not None and set(rec.keys()) != set(orig_rec.keys()):
        reasons.append(f'{prefix}: 记录键集与原件不一致(字段被删/注入)')
        return math.inf

    # 显式 t/r/a 数值字段(大小写两变体) → 直接验和(攻击可注入和≠1 的伪字段)
    vals = {}
    for lower, upper in (('t', 'T'), ('r', 'R'), ('a', 'A')):
        if lower in rec:
            vals[lower] = rec[lower]
        elif upper in rec:
            vals[lower] = rec[upper]
    if vals:
        if len(vals) != 3 or not all(_is_plain_number(x) for x in vals.values()):
            reasons.append(f'{prefix}: 显式 t/r/a 账本残缺或类型坏')
            return math.inf
        s = math.fsum([float(vals['t']), float(vals['r']), float(vals['a'])])
        if not math.isfinite(s):
            reasons.append(f'{prefix}: 显式 t/r/a 含 NaN/inf')
            return math.inf
        return abs(s - 1.0)

    # 无显式字段 → 从 pred/predicted 合成(v19 两种记录变体)
    pv = None
    has_pred_field = False
    for f in ('predicted', 'pred'):
        if f in rec:
            pv = rec[f]
            has_pred_field = True
            break
    if not has_pred_field:
        # 记录缺失预测字段(键不在): 原件对应位置有 → 被删 → 破坏; 双方都缺 → 无可合成
        # (注意: 键在而值为 None 是合法记录, 走 parse_pred(None)=0.0 合成路径)
        if orig_rec is not None and any(f in orig_rec for f in ('predicted', 'pred')):
            reasons.append(f'{prefix}: 预测字段缺失(原件对应位置有)')
            return math.inf
        return 0.0
    if isinstance(pv, float) and not math.isfinite(pv):
        reasons.append(f'{prefix}: 预测值 NaN/inf(合成异常)')
        return math.inf
    T, R, A = tra_decomposition(pv)
    return abs(math.fsum([T, R, A]) - 1.0)


def _check_invariants(rec, reasons, prefix) -> bool:
    """审计链不变量交叉对账(v19 全量实测零违例项才启用; 账平=多账本互证).

    返回 False = 不变量破坏(检出); 记录缺推理链字段时不适用, 返回 True.
    """
    path = rec.get('best_path') if 'best_path' in rec else rec.get('path')
    if not (isinstance(path, list) and path):
        return True
    trap_nodes = [x for x in path if isinstance(x, str) and x.startswith('Trap')]
    th = rec.get('trap_hit')
    if bool(th) != (len(trap_nodes) > 0):
        reasons.append(f'{prefix}: trap_hit 与推理链 Trap 节点不一致')
        return False
    if isinstance(th, str) and th not in path:
        reasons.append(f'{prefix}: trap_hit 串不在推理链节点中')
        return False
    if path[-1] != 'Goal':
        reasons.append(f'{prefix}: 推理链末节点未收口 Goal')
        return False
    return True


def _check_id_seq(recs, reasons, prefix) -> bool:
    """容器内 id 严格递增(manifest 对账; 交换任意两条 id 必破坏递增)."""
    if not recs or not all(isinstance(r, dict) for r in recs):
        return True  # 无 id 可对账(不适用, 不误伤)
    ids = [r.get('id') for r in recs]
    if not all(_is_plain_number(x) for x in ids):
        return True  # id 类型不适用, 跳过(键集/类型检查另行兜底)
    for a, b in zip(ids, ids[1:]):
        if not (float(b) > float(a)):
            reasons.append(f'{prefix}: id 序非严格递增(manifest 对账失败)')
            return False
    return True


def _layer1_audit(data, original):
    """层1 顶锚: physics_audit.t_plus_r_plus_a_max_deviation 分级判定.

    返回 (deviation|None, broken, reasons); deviation=None 表示无锚可判.
    """
    reasons = []
    audit = data.get('physics_audit') if isinstance(data, dict) else None
    o_audit = original.get('physics_audit') if isinstance(original, dict) else None
    if not isinstance(audit, dict):
        if isinstance(o_audit, dict):
            reasons.append('层1: physics_audit 缺失或类型坏(原件有)')
            return None, True, reasons
        return None, False, reasons  # 双方均无锚 → 无可判(空数据)
    if isinstance(o_audit, dict):
        for k in o_audit:
            if k not in audit:
                reasons.append(f'层1: physics_audit 键 {k!r} 被删(原件有)')
                return None, True, reasons
    v = audit.get('t_plus_r_plus_a_max_deviation')
    if v is None:
        if isinstance(o_audit, dict) and \
                o_audit.get('t_plus_r_plus_a_max_deviation') is not None:
            reasons.append('层1: 顶锚字段 t_plus_r_plus_a_max_deviation 被删(原件有)')
            return None, True, reasons
        return None, False, reasons
    if not _is_plain_number(v):
        reasons.append('层1: 顶锚字段类型坏')
        return None, True, reasons
    fv = float(v)
    if not math.isfinite(fv):
        reasons.append('层1: 顶锚字段 NaN/inf')
        return None, True, reasons
    return abs(fv), False, reasons


def _layer2_audit(data, original):
    """层2 per_problem 真重算.

    返回 (数值残差最大值, 检查记录数, 结构是否破坏, reasons).
    """
    reasons = []
    max_dev = 0.0
    n_checked = 0
    broken = False

    orig_containers = {}
    if original is not None:
        for path_t, recs in _iter_containers(original):
            orig_containers[path_t] = recs

    seen = set()
    for path_t, recs in _iter_containers(data):
        seen.add(path_t)
        prefix = '.'.join(str(x) for x in path_t)
        if original is not None:
            orecs = orig_containers.get(path_t)
            if orecs is None:
                reasons.append(f'{prefix}: 容器在原件中不存在(新增容器)')
                broken = True
                continue
            if len(recs) != len(orecs):
                reasons.append(f'{prefix}: 记录数与原件不一致(记录被删/增)')
                broken = True
                continue
        if not _check_id_seq(recs, reasons, prefix):
            broken = True
        for i, rec in enumerate(recs):
            if not isinstance(rec, dict):
                reasons.append(f'{prefix}[{i}]: 记录非 dict(类型坏)')
                broken = True
                continue
            n_checked += 1
            orig_rec = orig_containers[path_t][i] if original is not None else None
            dev = _check_record(rec, orig_rec, reasons, f'{prefix}[{i}]')
            if not math.isfinite(dev):
                broken = True
            else:
                max_dev = max(max_dev, dev)
            if not _check_invariants(rec, reasons, f'{prefix}[{i}]'):
                broken = True

    if original is not None:
        for path_t in orig_containers:
            if path_t not in seen:
                reasons.append(
                    '.'.join(str(x) for x in path_t) + ': 容器被删(原件有)')
                broken = True
    return max_dev, n_checked, broken, reasons


def check_conservation_graded(data, original_data=None) -> dict:
    """分级守恒审计(工单#14 接口).

    返回: {'verdict': 'PASS'|'GRAY'|'FAIL', 'max_deviation': float,
           'n_records_checked': int, 'layer1_deviation': float,
           'layer2_max_deviation': float, 'reasons': list}
    - 结构破坏(锚被删/记录被删/字段残缺/NaN) → verdict=FAIL, max_deviation=inf
    - 数值残差 <1e-15 → PASS; <1e-12 → GRAY; >=1e-12 → FAIL
    - 空数据(空 dict/无 experiments/空 per_problem/零记录) → PASS, n_records_checked=0
    - 任何输入不抛异常(0 异常纪律)
    """
    empty = {'verdict': 'PASS', 'max_deviation': 0.0, 'n_records_checked': 0,
             'layer1_deviation': 0.0, 'layer2_max_deviation': 0.0, 'reasons': []}
    if data is None:
        return dict(empty)
    if not isinstance(data, dict):
        # 非 dict 结构(类型坏): 显式处理, 不抛 TypeError
        r = dict(empty)
        r['verdict'] = 'FAIL'
        r['max_deviation'] = math.inf
        r['reasons'] = [f'输入类型坏: {type(data).__name__}(非 dict)']
        return r
    if not data:
        return dict(empty)  # 空 dict = 无可破坏

    l1_dev, l1_broken, l1_reasons = _layer1_audit(data, original_data)
    l2_dev, n_checked, l2_broken, l2_reasons = _layer2_audit(data, original_data)
    reasons = l1_reasons + l2_reasons

    if l1_broken or l2_broken:
        return {'verdict': 'FAIL', 'max_deviation': math.inf,
                'n_records_checked': n_checked,
                'layer1_deviation': l1_dev if l1_dev is not None else math.inf,
                'layer2_max_deviation': l2_dev, 'reasons': reasons[:50]}

    devs = [d for d in (l1_dev, l2_dev) if d is not None]
    max_dev = max(devs) if devs else 0.0
    if max_dev < PASS_THRESHOLD:
        verdict = 'PASS'
    elif max_dev < GRAY_THRESHOLD:
        verdict = 'GRAY'
    else:
        verdict = 'FAIL'
    return {'verdict': verdict, 'max_deviation': max_dev,
            'n_records_checked': n_checked,
            'layer1_deviation': l1_dev if l1_dev is not None else 0.0,
            'layer2_max_deviation': l2_dev, 'reasons': reasons[:50]}


def check_conservation(data: dict, original_data: dict = None) -> bool:
    """T+R+A=1 守恒审计(升级版 V0.3 真重算; 签名与上版兼容).

    双层检测(层1 顶锚 + 层2 per_problem 真重算), 详见模块 docstring.
    返回: True = 守恒(PASS/GRAY), False = 破坏(FAIL).
    """
    graded = check_conservation_graded(data, original_data)
    return graded['verdict'] in ('PASS', 'GRAY')


def run_audit(attacked_data: dict) -> dict:
    """跑审计, 返回详细结果(graded)"""
    graded = check_conservation_graded(attacked_data)
    return {
        'conserved': graded['verdict'] in ('PASS', 'GRAY'),
        'broken': graded['verdict'] == 'FAIL',
        'verdict': graded['verdict'],
        'max_deviation': graded['max_deviation'],
        'n_records_checked': graded['n_records_checked'],
    }


# ---------------------------------------------------------------------------
# --test_edge_cases: 工单#14 要求的 edge case 自检(全部显式处理, 0 异常)
# ---------------------------------------------------------------------------

def _mini_dataset():
    """构造满足全部审计不变量的最小数据集(edge case 测试夹具, FORM_A + FORM_B 混合)"""
    return {
        'spec_version': 'test',
        'physics_audit': {'t_plus_r_plus_a_max_deviation': 0.0,
                          'tolerance': 1e-06, 'passed': True},
        'experiments': {
            'exp1': {'benchmarks': {'gsm8k': {'per_problem': {
                'cond_a': [
                    {'id': 1, 'predicted': 18.0, 'answer': 18.0, 'is_correct': True,
                     'best_path': ['N1', 'OP1', 'Goal'], 'trap_hit': None},
                    {'id': 2, 'pred': 'No', 'is_correct': False,
                     'path': ['S1', 'Trap_guess', 'Goal'], 'trap_hit': True},
                ]}}}},
            'exp2': {'benchmarks': {'sqa': {'per_problem': [
                {'id': 1, 'pred': 'Yes', 'is_correct': True,
                 'path': ['S1', 'S2', 'Goal'], 'trap_hit': False},
            ]}}},
        },
    }


def _run_edge_cases() -> int:
    """至少 8 个 edge case, 全部显式处理 0 异常; 返回失败 case 数."""
    import copy as _copy

    cases = []

    # 01 空 dict
    cases.append(('empty_dict', {}, None, 'PASS'))
    # 02 无 experiments 键(仅 physics_audit)
    cases.append(('no_experiments_key',
                  {'physics_audit': {'t_plus_r_plus_a_max_deviation': 0.0}},
                  None, 'PASS'))
    # 03 空 experiments
    cases.append(('empty_experiments', {'experiments': {}}, None, 'PASS'))
    # 04 空 per_problem(FORM_B 空列表 / FORM_A 空字典)
    cases.append(('empty_per_problem',
                  {'experiments': {'e': {'benchmarks': {
                      'b1': {'per_problem': []},
                      'b2': {'per_problem': {}}}}}},
                  None, 'PASS'))
    # 05 记录 pred=None(显式处理, 合成守恒)
    d = _mini_dataset()
    d['experiments']['exp2']['benchmarks']['sqa']['per_problem'][0]['pred'] = None
    cases.append(('pred_none', d, None, 'PASS'))
    # 06 记录 pred=非法字符串(解析为 0.0, 合成守恒, 不抛异常)
    d = _mini_dataset()
    d['experiments']['exp2']['benchmarks']['sqa']['per_problem'][0]['pred'] = 'garbage!!'
    cases.append(('pred_illegal_string', d, None, 'PASS'))
    # 07 记录被删(original 有 4 条, data 只剩 3 条)→ FAIL
    d = _mini_dataset()
    del d['experiments']['exp1']['benchmarks']['gsm8k']['per_problem']['cond_a'][1]
    cases.append(('record_deleted', d, _mini_dataset(), 'FAIL'))
    # 08 显式 t/r/a 和≠1 注入(伪字段)→ FAIL
    d = _mini_dataset()
    d['experiments']['exp2']['benchmarks']['sqa']['per_problem'][0].update(
        {'t': 0.4, 'r': 0.4, 'a': 0.4})
    cases.append(('explicit_tra_sum_ne_1', d, _mini_dataset(), 'FAIL'))
    # 09 pred 注入 NaN → FAIL
    d = _mini_dataset()
    d['experiments']['exp2']['benchmarks']['sqa']['per_problem'][0]['pred'] = float('nan')
    cases.append(('pred_nan', d, _mini_dataset(), 'FAIL'))
    # 10 顶锚字段被删(original 有)→ FAIL
    d = _mini_dataset()
    del d['physics_audit']['t_plus_r_plus_a_max_deviation']
    cases.append(('anchor_deleted', d, _mini_dataset(), 'FAIL'))
    # 11 physics_audit 其他键被删(tolerance)→ FAIL(锚账本完整性)
    d = _mini_dataset()
    del d['physics_audit']['tolerance']
    cases.append(('physics_audit_key_deleted', d, _mini_dataset(), 'FAIL'))
    # 12 manifest_swap 模拟(容器内交换两条 id)→ FAIL
    d = _mini_dataset()
    recs = d['experiments']['exp1']['benchmarks']['gsm8k']['per_problem']['cond_a']
    recs[0]['id'], recs[1]['id'] = recs[1]['id'], recs[0]['id']
    cases.append(('id_swapped_manifest', d, _mini_dataset(), 'FAIL'))
    # 13 chain_modify 模拟(推理链末节点 Goal 被改)→ FAIL
    d = _mini_dataset()
    d['experiments']['exp1']['benchmarks']['gsm8k']['per_problem']['cond_a'][0][
        'best_path'][-1] = 'Goal_tampered'
    cases.append(('chain_goal_tampered', d, _mini_dataset(), 'FAIL'))
    # 14 mini 原件自身 → PASS(不变量零误报自证)
    cases.append(('mini_self', _mini_dataset(), _copy.deepcopy(_mini_dataset()), 'PASS'))
    # 15 None 输入(不抛 TypeError)
    cases.append(('none_input', None, None, 'PASS'))

    n_fail = 0
    n_exc = 0
    for i, (name, data, orig, expected) in enumerate(cases, 1):
        try:
            g = check_conservation_graded(data, orig)
            b = check_conservation(data, orig)
            got = g['verdict']
            ok = (got == expected) and (b == (expected in ('PASS', 'GRAY')))
            status = 'OK' if ok else 'MISMATCH'
            if not ok:
                n_fail += 1
            print(f'[edge_case {i:02d}] {name}: verdict={got} (expected={expected}) '
                  f'bool={b} n_records={g["n_records_checked"]} '
                  f'layer1_dev={g["layer1_deviation"]} layer2_dev={g["layer2_max_deviation"]}'
                  f' -> {status}')
            if g['reasons']:
                print(f'           reasons: {g["reasons"][:3]}')
        except Exception as e:  # noqa: BLE001 — edge case 纪律: 显式处理, 0 异常
            n_exc += 1
            n_fail += 1
            print(f'[edge_case {i:02d}] {name}: EXCEPTION {type(e).__name__}: {e} -> FAIL')

    # 16 v19 真件自检(全量 1592 记录, 原件必须守恒 PASS)
    try:
        v19 = load_v19()
        g = check_conservation_graded(v19, v19)
        ok = g['verdict'] == 'PASS' and g['n_records_checked'] == 1592
        if not ok:
            n_fail += 1
        print(f'[edge_case 16] v19_original_self: verdict={g["verdict"]} '
              f'n_records={g["n_records_checked"]} '
              f'layer1_dev={g["layer1_deviation"]} layer2_dev={g["layer2_max_deviation"]}'
              f' -> {"OK" if ok else "MISMATCH"}')
    except Exception as e:  # noqa: BLE001
        n_exc += 1
        n_fail += 1
        print(f'[edge_case 16] v19_original_self: EXCEPTION {type(e).__name__}: {e} -> FAIL')

    print(f'EDGE_CASES: {len(cases) + 1} cases, failures={n_fail}, exceptions={n_exc}')
    return n_fail


if __name__ == '__main__':
    if '--test_edge_cases' in sys.argv:
        sys.exit(0 if _run_edge_cases() == 0 else 1)
    data = load_v19()
    result = run_audit(data)
    print(f'Original v19: conserved={result["conserved"]}, '
          f'verdict={result["verdict"]}, max_dev={result["max_deviation"]}, '
          f'n_records_checked={result["n_records_checked"]}')
