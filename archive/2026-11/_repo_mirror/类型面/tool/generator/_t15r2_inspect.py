# -*- coding: utf-8 -*-
"""Inspect T1.5 records for T1.5r2 planning."""
import json
from collections import defaultdict
from pathlib import Path

def _dep_path(rel=""):
    """按名搜索：先在仓内候选根按相对路径找，再按件名全树找；皆不中则回原样。"""
    import os as _os
    from pathlib import Path as _P
    base = _P(__file__).resolve()
    roots = []
    for _i in range(1, 8):
        try:
            roots.append(base.parents[_i])
        except IndexError:
            break
    rel = rel.replace("\\", "/").lstrip("/")
    for _c in roots:
        if rel:
            _p = _c / rel
            if _p.exists():
                return str(_p)
    _name = rel.split("/")[-1] if rel else ""
    if _name:
        for _c in roots:
            for _dp, _dn, _fn in _os.walk(str(_c)):
                if _name in _fn:
                    return _os.path.join(_dp, _name)
    return rel


ROOT = Path(_dep_path(""))
records_path = ROOT / ".tmp" / "_t15_records.json"

with open(records_path, encoding="utf-8") as f:
    records = json.load(f)

print(f"Total records: {len(records)}")
ok_n = sum(1 for r in records if r.get("ok"))
fail_n = sum(1 for r in records if not r.get("ok"))
print(f"ok={ok_n} fail={fail_n}")
print()

by_cell = defaultdict(lambda: [0, 0])
for r in records:
    by_cell[r["cell_idx"]][0 if r.get("ok") else 1] += 1
print("cell ok fail")
for c in sorted(by_cell):
    print(f"{c:4d} {by_cell[c][0]:3d} {by_cell[c][1]:3d}")
print()

print("Failed records:")
for r in records:
    if not r.get("ok"):
        print(f"  cell={r['cell_idx']} teacher={r['teacher']} caption={r['caption_id']} reask={r['reask_idx']} temp={r['temperature']} cat={r.get('error_category')} lat={r.get('latency_ms')}")
print()

print("Successful keys set (teacher, caption, reask, temp) by cell:")
ok_keys_by_cell = defaultdict(set)
for r in records:
    if r.get("ok"):
        ok_keys_by_cell[r["cell_idx"]].add((r["teacher"], r["caption_id"], r["reask_idx"], r["temperature"]))
for c in sorted(ok_keys_by_cell):
    keys = ok_keys_by_cell[c]
    teachers = set(k[0] for k in keys)
    captions = set(k[1] for k in keys)
    reasks = set(k[2] for k in keys)
    print(f"cell {c}: {len(keys)} ok tuples | teachers={sorted(teachers)} | captions={sorted(captions)} | reasks={sorted(reasks)}")
print()

# Compute plan: missing tuples
TEACHER_NAMES = ["kimi", "GLM_1", "GLM_2", "coze", "minimax"]
L2_PROMPTS = ["L_biological_taxonomy", "S5"]
L14_PROMPTS = ["L_geography_world", "L_historical_causality"]
TEMPERATURES = [0.0, 0.3, 0.5]
DIM_OF_CELL = {0: "L2", 1: "L2", 2: "L2", 3: "L14", 4: "L14", 5: "L14"}
TEMP_OF_CELL = {0: 0.0, 1: 0.3, 2: 0.5, 3: 0.0, 4: 0.3, 5: 0.5}
PROMPTS_OF_CELL = {i: (L2_PROMPTS if DIM_OF_CELL[i] == "L2" else L14_PROMPTS) for i in range(6)}
N_REASKS_T15R2 = 3

print("=" * 60)
print(f"T1.5r2 plan vs current state (N_REASKS={N_REASKS_T15R2}):")
print("=" * 60)
total_new = 0
for cell_idx in range(6):
    dim = DIM_OF_CELL[cell_idx]
    temp = TEMP_OF_CELL[cell_idx]
    prompts = PROMPTS_OF_CELL[cell_idx]
    expected_full = set()
    for t in TEACHER_NAMES:
        for p in prompts:
            for r in range(N_REASKS_T15R2):
                expected_full.add((t, p, r, temp))
    existing_ok = ok_keys_by_cell[cell_idx]
    missing = expected_full - existing_ok
    extra = existing_ok - expected_full
    print(f"cell {cell_idx} ({dim}/t={temp}): expected_full={len(expected_full)}, existing_ok={len(existing_ok)}, missing_to_run={len(missing)}")
    if extra:
        print(f"  WARNING: extra ok tuples (reask_idx >= {N_REASKS_T15R2}): {extra}")
    if missing:
        # group by (teacher, caption)
        per_pair = defaultdict(list)
        for tup in missing:
            per_pair[(tup[0], tup[1])].append(tup[2])
        for (t, p), rs in sorted(per_pair.items()):
            print(f"    need: teacher={t} cap={p} reasks={sorted(rs)}")
    total_new += len(missing)
print()
print(f"TOTAL missing (new) calls to make: {total_new}")
print(f"Cell breakdown:")
for cell_idx in range(6):
    dim = DIM_OF_CELL[cell_idx]
    temp = TEMP_OF_CELL[cell_idx]
    prompts = PROMPTS_OF_CELL[cell_idx]
    expected_full = set()
    for t in TEACHER_NAMES:
        for p in prompts:
            for r in range(N_REASKS_T15R2):
                expected_full.add((t, p, r, temp))
    existing_ok = ok_keys_by_cell[cell_idx]
    missing = expected_full - existing_ok
    print(f"  cell {cell_idx} ({dim}/t={temp}): +{len(missing)} calls")
