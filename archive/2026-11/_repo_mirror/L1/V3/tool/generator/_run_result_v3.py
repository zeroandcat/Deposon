# -*- coding: utf-8 -*-
"""
V4 _v4_pi_cot_v3_result_v3 runner (棒 C)
- 沿 executor 函数调用; 0 LLM; 0 触动既有件
- 仅产 result_v3.json (本棒输出件); 0 派生合并
"""
from __future__ import annotations
import sys, json, hashlib
from pathlib import Path
from collections import Counter

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "results"))

import importlib.util
spec = importlib.util.spec_from_file_location('exv3', str(REPO_ROOT / 'results' / '_v4_pi_cot_v3_ruleset_v3_executor.py'))
exv3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(exv3)

# ============================================================================
# 0. 锚 SHA-12 验真 (不写盘, 仅返报)
# ============================================================================
ANCHORS = {
    "prereg_v3":              ("_v4_pi_cot_v3_prereg.md",                              "B7547329AF2E"),
    "ruleset_v3":             ("_v4_pi_cot_v3_ruleset_v3.json",                        "9D77A5E2CBAB"),
    "ruleset_v3_executor":    ("_v4_pi_cot_v3_ruleset_v3_executor.py",                 "8A81D90C69BA"),
    "dataset_v3":             ("_v4_pi_cot_v3_dataset.json",                           "5118F5B44F17"),
    "dataset_v2_v11":         ("_v4_pi_cot_v2_dataset.json",                           "7B01CD835A41"),
    "coding_review_v2":       ("_v4_pi_cot_v2_coding_review_2026_09_26.md",            "5FBEC21E0AD2"),
    "ruleset_v2_ref":         ("_v4_pi_cot_v2_ruleset_v2.json",                        "C5B3DD141655"),
    "executor_v2_ref":        ("_v4_pi_cot_v2_ruleset_v2_executor.py",                 "EB22F13D571C"),
    "addendum_d1":            ("_v4_pi_cot_v2_dataset_addendum_2026_09_24.json",       "172093A23E4B"),
    "addendum_d2":            ("_v4_pi_cot_v2_dataset_addendum_d2_2026_09_26.json",     "439721007AAF"),
    "addendum_d2b":           ("_v4_pi_cot_v2_dataset_addendum_d2b_2026_09_26.json",    "41D6C28CA87C"),
    "addendum_d2c":           ("_v4_pi_cot_v2_dataset_addendum_d2c_2026_09_26.json",    "99C58906F792"),
    "addendum_d2d":           ("_v4_pi_cot_v2_dataset_addendum_d2d_2026_09_26.json",    "C6D092F77932"),
    "addendum_d2e":           ("_v4_pi_cot_v2_dataset_addendum_d2e_2026_09_26.json",    "26F110A6E571"),
    "addendum_d3a":           ("_v4_pi_cot_v2_dataset_addendum_d3a_2026_09_26.json",    "6E104E2DB038"),
    "addendum_d3b":           ("_v4_pi_cot_v2_dataset_addendum_d3b_2026_09_26.json",    "D96B747BFC6C"),
    "addendum_d3c":           ("_v4_pi_cot_v2_dataset_addendum_d3c_2026_09_26.json",    "401BD614CDF7"),
    "addendum_d4":            ("_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json",     "B18FF4177289"),  # anchor expected
}

RESULTS_DIR = REPO_ROOT / "results"

anchor_results = {}
for k, (fname, expected_sha) in ANCHORS.items():
    p = RESULTS_DIR / fname
    actual = hashlib.sha256(p.read_bytes()).hexdigest()[:12].upper()
    drift = actual != expected_sha.upper()
    anchor_results[k] = {"expected": expected_sha.upper(), "actual": actual, "drift": drift}

# 报告漂移 (老实交代)
print("=== Anchor SHA-12 验真 ===")
for k, v in anchor_results.items():
    flag = " [DRIFT]" if v["drift"] else ""
    print(f"  {k}: expected={v['expected']} actual={v['actual']}{flag}")