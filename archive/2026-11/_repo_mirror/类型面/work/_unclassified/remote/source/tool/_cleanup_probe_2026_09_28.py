# -*- coding: utf-8 -*-
"""2026-09-28 每日收尾整理棒 · 归属复核探针 v2 (worker)
用途: 删除任何 .tmp 件之前, 逐件实测「内容是否已入权威件(results/*.md)」。
口径: SHA-12 = hashlib.sha256(data).hexdigest()[:12] 小写。
v2: 单次构建权威件语料, 避免重复读盘。
"""
import hashlib
import pathlib
import sys

ROOT = pathlib.Path(r"_repo_mirror")
TMP = ROOT / ".tmp"
RESULTS = ROOT / "results"

BLOBS = []


def build_corpus():
    parts = []
    for p in sorted(RESULTS.glob("*.md")):
        try:
            parts.append(p.read_text(encoding="utf-8", errors="replace"))
        except Exception as e:  # noqa: BLE001
            print(f"SKIP {p.name}: {e}")
    return "\n".join(parts)


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def substantive_lines(text, minlen=12):
    return [s for s in (ln.strip() for ln in text.splitlines()) if len(s) >= minlen]


def probe(name, blob):
    p = TMP / name
    if not p.exists():
        print(f"{name}\tMISSING")
        return
    lines = substantive_lines(p.read_text(encoding="utf-8", errors="replace"))
    miss = [ln for ln in lines if ln not in blob]
    print(f"{name}\tsha12={sha12(p)}\tbytes={p.stat().st_size}\t"
          f"lines={len(lines)}\thit={len(lines)-len(miss)}\tmiss={len(miss)}")
    for m in miss[:4]:
        print(f"    MISS: {m[:120]}")


def main():
    blob = build_corpus()
    print(f"[corpus] results/*.md 拼接 {len(blob)} chars\n")

    groups = {
        "A_md_segment_buffer": ["_e48_c1.md", "_e48_c2.md", "_e48_c3.md", "_e48_c4.md",
                                "_e48_c5.md", "_v1p4_append_section.md"],
        "B_stale_logs": ["_d4_relabel_run1.log", "_recheck_r1_run1.log", "_recheck_r1_runA.log",
                         "_recheck_r1_runB.log", "_recheck_r1_runC.log", "_recheck_r1_runD.log",
                         "_run_output.log", "_v3r1_run1.log", "_v3r1_run2.log"],
        "C_other_buffers": ["_audit3b.txt", "_audit_part3_out.txt", "_audit_part4.txt",
                            "_gaps.txt", "_gaps2.txt", "_r10.txt", "_r6_evidence.txt",
                            "_r11_ctx.txt", "_e3536.txt", "_final_sha.txt",
                            "_t15r2_checkpoint_warn.jsonl", "_postcheck_v16_alt_stdout.txt",
                            "_v16_tail_only.txt"],
    }
    for title, names in groups.items():
        print(f"=== {title} ===")
        for n in names:
            probe(n, blob)
        print()


if __name__ == "__main__":
    sys.exit(main())
