#!/usr/bin/env python3
"""R4 key plaintext scan — scoped to this棒's 4 new files (2026-09-27 worker 棒).

Reuses the key-form patterns of .tmp/_r4_key_scan_2026_09_24.py (沿 R4「key 永不明文·无例外」铁律).
Output: file path + encoding + key 4-char prefix + key SHA-12 (NEVER echo key text).
Scope: 4 件本棒新出件 + 3 件本棒引用只读件 (只读件仅作「0 触动」旁证, 非本棒产出).
"""
import re
import json
import hashlib
from pathlib import Path

REPO = Path(r"D:\私人资料\deposon-repo")

TARGETS_NEW = [
    "results/_v4_pi_cot_v3_ruleset_v3_executor_r1_2026_09_27.py",
    "results/_v4_pi_cot_v3_k3b_recheck_r1_2026_09_27.json",
    "results/_v4_pi_cot_v3_dataset_addendum_d4_relabel_2026_09_27.json",
    "results/_v4_pi_cot_v3_alt_reading_definition_2026_09_27.md",
]
TARGETS_READONLY = [
    "results/_v4_pi_cot_v3_ruleset_v3_executor.py",
    "results/_v4_pi_cot_v3_result_v3.json",
    "results/_v4_pi_cot_v3_dataset_addendum_d4_2026_09_27.json",
    ".tmp/_run_final.py",
    ".tmp/_run_recheck_r1.py",
    ".tmp/_run_d4_relabel_addendum.py",
]

KEY_PATTERNS = [
    r"sk-or-v1-[A-Za-z0-9]{16,}",
    r"sk-teamo-[A-Za-z0-9]{16,}",
    r"sk-ad9b[A-Za-z0-9]{16,}",
    r"sk-[A-Za-z0-9]{20,}",
    r"ark-[A-Za-z0-9]{16,}-[A-Za-z0-9]{8,}",
    r"AKIA[A-Z0-9]{16}",
    r"AIza[A-Za-z0-9_-]{35}",
    r"ghp_[A-Za-z0-9]{36}",
    r"gho_[A-Za-z0-9]{36}",
    r"xoxb-[A-Za-z0-9-]{20,}",
    r"xoxp-[A-Za-z0-9-]{20,}",
    # 本棒自扫追加: 裸长 base64/hex 串误报面收敛 (仅登记长度+SHA, 不回显)
    r"(?i)\b(?:api[_-]?key|secret|token|password|bearer)\b\s*[:=]\s*[\"'][^\"']{16,}[\"']",
]
ENCODINGS = ["utf-8", "gb18030", "gbk", "utf-16-le", "utf-16-be", "big5"]


def key_sha12(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()[:12].upper()


def scan_file(path: Path):
    out = []
    try:
        data = path.read_bytes()
    except OSError:
        return out
    if not data:
        return out
    for enc in ENCODINGS:
        try:
            text = data.decode(enc, errors="strict")
        except (UnicodeDecodeError, LookupError):
            continue
        for pat in KEY_PATTERNS:
            for m in re.finditer(pat, text):
                out.append({"encoding": enc,
                            "line_no": text.count("\n", 0, m.start()) + 1,
                            "key_prefix4": m.group(0)[:4],
                            "key_sha12": key_sha12(m.group(0)),
                            "key_len": len(m.group(0))})
    return out


if __name__ == "__main__":
    report = {"scope_new": TARGETS_NEW, "scope_readonly": TARGETS_READONLY,
              "pattern_count": len(KEY_PATTERNS), "encodings": ENCODINGS,
              "new_files": [], "readonly_files": [], "n_hits_total": 0}
    for rel in TARGETS_NEW:
        p = REPO / rel
        hits = scan_file(p)
        report["new_files"].append({"path": rel, "exists": p.exists(),
                                    "bytes": p.stat().st_size if p.exists() else None,
                                    "sha12": hashlib.sha256(p.read_bytes()).hexdigest()[:12].upper()
                                    if p.exists() else None,
                                    "n_key_hits": len(hits), "hits": hits})
        report["n_hits_total"] += len(hits)
    for rel in TARGETS_READONLY:
        p = REPO / rel
        hits = scan_file(p)
        report["readonly_files"].append({"path": rel, "n_key_hits": len(hits), "hits": hits})
        report["n_hits_total"] += len(hits)
    out = REPO / ".tmp" / "_r4_key_scan_r1_files_2026_09_27.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print("=== R4 key self-scan (scoped) ===")
    for f in report["new_files"]:
        print(f"  NEW      {f['path']:66s} {f['bytes']} B  sha12={f['sha12']}  key_hits={f['n_key_hits']}")
    for f in report["readonly_files"]:
        print(f"  READONLY {f['path']:66s} key_hits={f['n_key_hits']}")
    print(f"  total key-form hits = {report['n_hits_total']}")
    print(f"  out = {out}")
