#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
anchor-guard secret audit script (2026-09-20) — extended scope
==============================================================
严守 9 铁律: 仅打印文件名 + 已发生 key 计数 + 脱敏预览 (前 4 + *** + 后 4),
不把 keys 全文写到 stdout / log / prompt。
"""

import hashlib
import json
import re
import sys
from pathlib import Path

WORKSPACE = Path(r"D:\私人资料\deposon-repo")

# 5 regex 模式 (沿派工 brief Step 2)
PATTERNS = [
    ("api_key", re.compile(r"api[_-]?key", re.IGNORECASE)),
    ("sk_xxx", re.compile(r"sk-[a-zA-Z0-9]{8,}")),
    ("gpt_xxx", re.compile(r"gpt-[a-zA-Z0-9]{20,}")),
    ("claude_xxx", re.compile(r"claude-[a-zA-Z0-9]{20,}")),
    ("ark_xxx", re.compile(r"ark-[a-zA-Z0-9]{8,}")),
]

# Step 2 audit: 8 个 D+0.5 文件 (不含已 trash 1 件)
STEP2_FILES = [
    r"results\_d05_main_run_results_20260918_100853.json",
    r"results\_d05_main_run_results_qwen3_failed_20260918_100853.json",
    r"results\_d05_main_run_results_nemotron_3.5_20260918_100853.json",
    r"results\_d05_backbone_robustness_beta_20260918_100853.json",
    r"results\_d05_opt_5_directions_results_20260918_100853.json",
    r"results\_d05_i1i5_invariants_check_20260918_100853.json",
    r"results\_d05_combined_report_20260918_100853.md",
    r"results\_D05_DATA_RESCUE_NOTE_2026_09_18.md",
]

# Step 3 audit: corpus 5 制品 (frozen)
STEP3_FILES = [
    r"corpus\v20\by_model\KIMI\index_v2_2026_09_16.json",
    r"corpus\v20\by_model\GLM_1\three_way_glm_slot_blind_test_2026_09_16.json",
    r"corpus\v20\by_model\GLM_2\glm_artifact_v_2026_09_16.json",
    r"corpus\v20\by_model\coze\coze_artifact_v_2026_09_16.json",
    r"corpus\v20\by_model\minimax\artifact_v_2026_09_16.json",
]

# 9-18 后新增 audit
STEP4_FILES = [
    # results/ 09-18 / 09-20 后新增
    r"results\_kimi_push_v3_manifest_batch11_7d6a7c8f.json",
    r"results\_kimi_push_v3_manifest_batch12_a2853574.json",
    r"results\_kimi_push_v3_manifest_batch13_83f895f9.json",
    r"results\_kimi_push_v3_manifest_batch14_e5952130.json",
    r"results\_kimi_push_v3_manifest_batch15_0e65fe2f.json",
    r"results\_kimi_push_v3_manifest_verifier21_cc3c92d0.json",
    r"results\_kimi_safe_batch_push_v3_full_2026_09_17.json",
    r"results\_kimi_ftfb_s7_independent_recompute_2026_09_18.json",
    r"results\_deposon_v2scripts_kimi7_audit_20260918_105219.json",
    r"results\_deposon_v2scripts_reverify_20260918_105219.json",
    r"results\_deposon_v2scripts_reverify_20260918_105219.md",
    r"results\_deposon_v2scripts_summary_挂点回扣_20260918_105219.json",
    r"results\_letter_to_coze_wechat_v2_2026_09_18.md",
    r"results\_letter_to_kimi_upload_requirements_2026_09_18.md",
    r"results\_coze_wechat_v3_2026_09_18.md",
    r"results\_coze_wechat_v3_d7format_2026_09_18.md",
    r"results\_coze_wechat_v3_final_2026_09_18.md",
    r"results\_ftfb_v3_pass1_audit_2026_09_18_corrected.md",
    r"results\_ftfb_v3_pass2_audit_2026_09_18_corrected.md",
    r"results\_glm_response_v2_template_2026_09_18.md",
    r"results\_glm_v3_双审报告_2026_09_18.md",
    r"results\_mavis_skill_inventory_2026_09_18.md",
    # deposon_team/plugins/ 09-18 新增 (自检重点)
    r"deposon_team\plugins\mavis_trash_2026_09_18.py",
    r"deposon_team\plugins\_deposon_v2scripts_reverify_worker_2026_09_18.py",
    r"deposon_team\plugins\_final_sha_2026_09_18.py",
    r"deposon_team\plugins\_fix_batch2_2026_09_18.py",
    r"deposon_team\plugins\_fix_batch3_2026_09_18.py",
    r"deposon_team\plugins\_fix_batch4_2026_09_18.py",
    r"deposon_team\plugins\_fix_batch6_2026_09_18.py",
    r"deposon_team\plugins\_fix_batch7_2026_09_18.py",
    r"deposon_team\plugins\_fix_batch8_2026_09_18.py",
    r"deposon_team\plugins\_fix_d05_rescue_2026_09_18.py",
    r"deposon_team\plugins\_verify_batch5_2026_09_18.py",
]


def redact(match: str) -> str:
    """脱敏: 保留前 4 + *** + 后 4 字符"""
    if len(match) <= 10:
        return match[:3] + "***"
    return match[:4] + "***" + match[-4:]


def audit_file(rel_path: str) -> dict:
    abs_path = WORKSPACE / rel_path
    result = {
        "rel_path": rel_path,
        "exists": abs_path.exists(),
        "size": abs_path.stat().st_size if abs_path.exists() else 0,
        "found": False,
        "total_hits": 0,
        "by_pattern": {},
        "redacted_samples": [],
    }

    if not abs_path.exists() or not abs_path.is_file():
        return result

    try:
        content = abs_path.read_bytes()
        try:
            text = content.decode("utf-8", errors="replace")
        except Exception:
            text = content.decode("latin-1", errors="replace")

        for label, pat in PATTERNS:
            hits = pat.findall(text)
            if hits:
                result["by_pattern"][label] = len(hits)
                result["total_hits"] += len(hits)
                for h in hits[:3]:
                    result["redacted_samples"].append(f"{label}={redact(h)}")

        result["found"] = result["total_hits"] > 0
    except Exception as e:
        result["error"] = str(e)

    return result


def main():
    target_step = sys.argv[1] if len(sys.argv) > 1 else "all"

    results = {"step2": [], "step3": [], "step4": []}

    if target_step in ("step2", "all"):
        for rel in STEP2_FILES:
            results["step2"].append(audit_file(rel))

    if target_step in ("step3", "all"):
        for rel in STEP3_FILES:
            results["step3"].append(audit_file(rel))

    if target_step in ("step4", "all"):
        for rel in STEP4_FILES:
            results["step4"].append(audit_file(rel))

    # 摘要: 含密钥文件列表
    summary = {
        "step2_total_hits": sum(r["total_hits"] for r in results["step2"]),
        "step2_files_with_keys": [r["rel_path"] for r in results["step2"] if r["found"]],
        "step3_total_hits": sum(r["total_hits"] for r in results["step3"]),
        "step3_files_with_keys": [r["rel_path"] for r in results["step3"] if r["found"]],
        "step4_total_hits": sum(r["total_hits"] for r in results["step4"]),
        "step4_files_with_keys": [r["rel_path"] for r in results["step4"] if r["found"]],
    }

    print("=== SUMMARY ===")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print()
    print("=== FULL DETAIL ===")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()