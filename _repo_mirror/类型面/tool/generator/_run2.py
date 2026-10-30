from __future__ import annotations
import sys, json, hashlib
from pathlib import Path
from collections import Counter
import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "results"))

import importlib.util
spec = importlib.util.spec_from_file_location('exv3', str(REPO_ROOT / 'results' / '_v4_pi_cot_v3_ruleset_v3_executor.py'))
exv3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exv3)

# ============================================================================
# 1. 加载事件
# ============================================================================
events, load_meta = exv3.load_all_events_v3()
print(f"Loaded {load_meta['n_total']} events; correction={load_meta['n_correction']}; days={load_meta['distinct_days']}")

# ============================================================================
# 2. substrate 裁定 (per briefing)
# ============================================================================
# 区分 source_wave: v1.1 (无 _provenance.source_wave) + D1_supp + D2_* + D3_w1 + D3_w2 + D3_w3 + D4_w1
post_v2_events = []
v2_baseline_on_disk = []
d4_events = []
d3_w1_events = []
for i, ev in enumerate(events):
    prov = ev.get('_provenance', {}) or {}
    wave = prov.get('source_wave', '')
    qid = ev.get('q_id', '')
    eid = ev.get('event_id', '')
    if wave == 'D3_w2' or wave == 'D3_w3':
        post_v2_events.append({
            "event_id": eid,
            "q_id": qid,
            "source_wave": wave,
            "source_file": prov.get('source_file', ''),
            "exclude_reason": "substrate 裁定: post-v2 追补 (8 件 D3 wave2/3 三读稳定性探针) 仅记账不入正式跑"
        })
    elif wave == 'D4_w1':
        d4_events.append({"event_id": eid, "q_id": qid})
    elif wave == 'D3_w1':
        d3_w1_events.append({"event_id": eid, "q_id": qid})
    else:
        v2_baseline_on_disk.append({"event_id": eid, "q_id": qid, "source_wave": wave or 'v1.1'})

print(f"v2_baseline_on_disk: {len(v2_baseline_on_disk)}")
print(f"d3_w1 (third-read probe, v2 baseline): {len(d3_w1_events)}")
print(f"post_v2 (excluded ledger): {len(post_v2_events)}")
print(f"d4 (new): {len(d4_events)}")
print(f"TOTAL events loaded: {len(events)}")
print(f"SUBSTRATE_RUN (all 77): {len(events)}")
print(f"EXCLUDED LEDGER: {len(post_v2_events)}")
print(f"MISSING LEDGER (D1 缺位 8): 8 (declared by v2 verdict, not on disk)")

# ============================================================================
# 3. 跑 executor 全链 (沿 briefing substrate = 77 events)
# ============================================================================
import numpy as np
rng = np.random.RandomState(exv3.SEED)
held_idx = exv3.stratified_holdout_split_v3(events, exv3.HELD_OUT_RATIO, rng)
print(f"\nStratified held-out: {len(held_idx)} events (ratio={exv3.HELD_OUT_RATIO})")

# 12 项特征审查 (防退化)
n_dist = exv3.check_feature_degradation(events)
print(f"\nFeature degradation check (n_distinct per feature):")
for k, v in n_dist.items():
    flag = " [WARN<=3]" if v <= 3 else ""
    print(f"  {k}: {v}{flag}")

# 主计算
metrics = exv3.compute_metrics_v3(events, held_idx)
print(f"\nMain reading (主读法, n_held={metrics['n_held']}, n_corr_in_held={metrics['n_corr_in_held']}):")
print(f"  nw_sim_mean = {metrics['nw_sim_mean']:.4f}")
print(f"  nled_sim_mean = {metrics['nled_sim_mean']:.4f}")
print(f"  n_divergent = {metrics['n_divergent']}")
print(f"  n_critical_among_divergent = {metrics['n_critical_among_divergent']}")
print(f"  div_critical_coverage = {metrics['div_critical_coverage']:.4f}")
print(f"  n_agree = {metrics['n_agree']}, n_blind_obey = {metrics['n_blind_obey']}")
print(f"  blind_obey_rate = {metrics['blind_obey_rate']:.4f}")
print(f"  perm_p = {metrics['perm_p']:.4f} (n={metrics['perm_n']}, alpha={metrics['alpha']})")
print(f"  bootstrap_ci = [{metrics['bootstrap_ci'][0]:.4f}, {metrics['bootstrap_ci'][1]:.4f}] (n={metrics['bootstrap_n']})")
print(f"  tree_depth_observed = {metrics['tree_depth_observed']}")

# K-V3-* 判定
kill_lines, hit_bools = exv3.kill_line_check_v3(metrics)
print(f"\nK-V3-* 判定:")
for k in kill_lines:
    print(f"  {k['id']}: hit={k['hit']}, pass={k['pass']}, observed={k.get('observed', k.get('observed_ci', '?'))}, rule='{k['rule'][:80]}'")

print(f"\nHit bools dict: {hit_bools}")