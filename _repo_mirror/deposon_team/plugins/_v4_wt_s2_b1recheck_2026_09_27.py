# -*- coding: utf-8 -*-
"""
_v4_wt_s2_b1recheck — B1 独立重跑复核（受托方 Trae code 独立实现，只读 + 只 stdout，0 写盘）
目的：独立验证 §B.1 B1 修复面 ——
  (a) 母件 executor 复现已落盘 result_v3.json 的 main/alt 读数（证明本复核管线与出件管线同口径）；
  (b) 修复件 executor_r1 的 K-V3-B / K-V3-C 修后读数（覆盖率 / hit 方向）；
  (c) 六条 kill-line 修前/修后 hit 向量逐项对比。
方法：importlib 直接加载两个 executor 模块，调用其公开函数重跑管线段；不 import worker 的 runner。
"""
from __future__ import annotations
import hashlib, importlib.util, json, os, sys
from pathlib import Path

REPO = Path(r'D:\私人资料\deposon-repo')
RES = REPO / 'results'
BASE = RES / '_v4_pi_cot_v3_ruleset_v3_executor.py'
R1 = RES / '_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py'
RV3 = RES / '_v4_pi_cot_v3_result_v3.json'

def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m

print('=== 0. 锚件实测 SHA-12 ===')
print(f'  base executor : {sha12(BASE)}  (受托方实算; 委托记 8a81d90c69ba)')
print(f'  r1   executor : {sha12(R1)}  (委托记 ee8671a28c2f)')
print(f'  result_v3     : {sha12(RV3)}  (委托记 585714f9660c)')

exb = load('v4wt_base', BASE)
exr = load('v4wt_r1', R1)
import numpy as np

def run(ex, tag):
    events, load_meta = ex.load_all_events_v3()
    rng = np.random.RandomState(ex.SEED)
    held = ex.stratified_holdout_split_v3(events, ex.HELD_OUT_RATIO, rng)
    m = ex.compute_metrics_v3(events, held)
    kl, hit = ex.kill_line_check_v3(m)
    held_nc = [i for i in held if not ex.is_correction_event_v3(events[i])]
    alt = ex.compute_metrics_v3(events, held_nc) if held_nc else {}
    return dict(tag=tag, n=len(events), held=held, held_nc=held_nc, m=m, kl=kl, hit=hit, alt=alt, events=events)

base = run(exb, 'base'); r1 = run(exr, 'r1')
rv3 = json.loads(RV3.read_text(encoding='utf-8'))
rm, ra = rv3['main_reading'], rv3['alt_reading_corr_excluded']

print()
print('=== 1. 母件复现自校验（vs 盘上 result_v3.json）===')
checks = {
  'main_held_idx': base['held'] == rm['held_out_idx'],
  'main_nw_sim_mean': base['m']['nw_sim_mean'] == rm['nw_sim_mean'],
  'main_nled_sim_mean': base['m']['nled_sim_mean'] == rm['nled_sim_mean'],
  'main_n_divergent': base['m']['n_divergent'] == rm['n_divergent'],
  'main_n_crit_among_div': base['m']['n_critical_among_divergent'] == rm['n_critical_among_divergent'],
  'main_div_crit_cov': base['m']['div_critical_coverage'] == rm['div_critical_coverage'],
  'main_n_blind': base['m']['n_blind_obey'] == rm['n_blind_obey'],
  'main_blind_rate': base['m']['blind_obey_rate'] == rm['blind_obey_rate'],
  'main_bootstrap_ci': base['m']['bootstrap_ci'] == rm['bootstrap_ci'],
  'main_perm_p': base['m']['perm_p'] == rm['perm_p'],
  'alt_held_count': len(base['held_nc']) == ra['held_out_count'],
  'alt_nw_sim_mean': base['alt']['nw_sim_mean'] == ra['nw_sim_mean'],
  'alt_nled_sim_mean': base['alt']['nled_sim_mean'] == ra['nled_sim_mean'],
  'alt_div_crit_cov': base['alt']['div_critical_coverage'] == ra['div_critical_coverage'],
  'alt_blind_rate': base['alt']['blind_obey_rate'] == ra['blind_obey_rate'],
  'alt_bootstrap_ci': base['alt']['bootstrap_ci'] == ra['bootstrap_ci'],
  'alt_n_divergent': base['alt']['n_divergent'] == ra['n_divergent'],
  'alt_n_crit_among_div': base['alt']['n_critical_among_divergent'] == ra['n_critical_among_divergent'],
}
for k, v in checks.items():
    print(f'  {"OK " if v else "FAIL"}  {k}')
print(f'  ⇒ 全 {len(checks)} 项逐字相同: {all(checks.values())}')

print()
print('=== 2. B1 修复效果：母件 vs r1 ===')
mb, mr = base['m'], r1['m']
print(f'  K-V3-B 覆盖率: {mb["div_critical_coverage"]} -> {mr["div_critical_coverage"]}   (thr {exr.TH_CRITICAL_COV})')
print(f'     分歧数 n_divergent: {mb["n_divergent"]} -> {mr["n_divergent"]} ; 其中含批判词: {mb["n_critical_among_divergent"]} -> {mr["n_critical_among_divergent"]}')
print(f'  K-V3-C 盲从率: {mb["blind_obey_rate"]} -> {mr["blind_obey_rate"]}   (thr {exr.TH_BLIND_OBEY})')
print(f'     n_agree: {mb["n_agree"]} -> {mr["n_agree"]} ; n_blind: {mb["n_blind_obey"]} -> {mr["n_blind_obey"]}')
print(f'  E-42.1 敏感性登记值 0.6000 实测吻合: {mr["div_critical_coverage"] == 0.6}')
print(f'  held 集 母件==r1: {base["held"] == r1["held"]}')

print()
print('=== 3. 六条 kill-line hit 向量（修前 -> 修后）===')
km = {k['id']: k for k in base['kl']}; kr = {k['id']: k for k in r1['kl']}
n_chg = 0
for kid in ["K-V3-A", "K-V3-A'", "K-V3-B", "K-V3-C", "K-V3-D", "K-V3-E"]:
    hb, hr = km[kid]['hit'], kr[kid]['hit']
    ob, orr = km[kid].get('observed'), kr[kid].get('observed')
    chg = (hb != hr)
    n_chg += 1 if chg else 0
    print(f'  {kid:<9} obs {ob} -> {orr}   hit {hb} -> {hr}   {"★方向变化" if chg else "无"}')
print(f'  ⇒ 方向变化总数 = {n_chg}')

print()
print('=== 4. 受影响 3 件 D1_supp 事件（改前/改后 reasoning_full 长度 + 批判词）===')
def d1rows(p):
    out = []
    for ev in p['events']:
        if ev.get('_provenance', {}).get('source_wave') == 'D1_supp':
            rf = ev.get('reasoning_full', '') or ''
            out.append((ev.get('q_id'), len(rf), exr.has_critical_reflection_v3(rf)))
    return out
print(f'  before: {d1rows(base)}')
print(f'  after : {d1rows(r1)}')

print()
print('_wt_s2_b1recheck DONE')
