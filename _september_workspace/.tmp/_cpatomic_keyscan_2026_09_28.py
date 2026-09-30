# -*- coding: utf-8 -*-
"""CLEAN-A棒 · 本棒新出件 key 明文自扫（0 明文铁律自证）。

扫 6 件本棒新出件 + 2 件修复源件（源件 0 触动面, 顺带登记）。
0 LLM / 纯 hashlib+re 本地扫。
"""
import hashlib
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path("D:/私人资料/deposon-repo")

PATS = {
    "sk-ant": re.compile(r"sk-ant-[A-Za-z0-9_\-]{16,}"),
    "sk-plain": re.compile(r"\bsk-[A-Za-z0-9]{20,}"),
    "uuid_like": re.compile(r"\b[a-zA-Z0-9]{8}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{4}-[a-zA-Z0-9]{12}\b"),
    "bearer_lit": re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}"),
    "key_assign": re.compile(
        r"(?:api[_-]?key|ARK_API_KEY|OPENAI_API_KEY|ANTHROPIC_API_KEY)\s*[=:]\s*"
        r"[\"'][A-Za-z0-9._\-]{16,}[\"']"
    ),
}

NEW = [
    "results/_v4_supp_t15r2_executor_r2_atomic_2026_09_28.py",
    "results/_v4_supp_t15_executor_r2_atomic_2026_09_28.py",
    ".tmp/_cpatomic_pycache_pre_2026_09_28.py",
    ".tmp/_cpatomic_pycache_post_2026_09_28.py",
    ".tmp/_cpatomic_make_fix_2026_09_28.py",
    ".tmp/_cpatomic_verify_2026_09_28.py",
]
SRC_READONLY = [
    "results/_v4_supp_t15r2_executor_r1_2026_09_28.py",
    "results/_v4_supp_t15_executor_r1_2026_09_27.py",
]


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def scan(paths):
    rows, total = [], 0
    for rel in paths:
        p = ROOT / rel
        txt = p.read_text(encoding="utf-8")
        hits = {k: len(v.findall(txt)) for k, v in PATS.items()}
        n = sum(hits.values())
        total += n
        rows.append({"path": rel, "bytes": p.stat().st_size, "sha12": sha12(p),
                     "hits": hits, "n_hits": n})
        print(f"{rel}\n    {p.stat().st_size:7d} B  sha12={sha12(p)}  key_hits={n} {hits}")
    return rows, total


def main():
    print("=== 本棒新出件 ===")
    new_rows, n_new = scan(NEW)
    print("\n=== 修复源件（只读登记, 0 触动）===")
    src_rows, n_src = scan(SRC_READONLY)

    print("\n--- key 引用口径抽样（应只见 runtime env 表述, 0 值）---")
    for rel in NEW[:2]:
        for ln in (ROOT / rel).read_text(encoding="utf-8").splitlines():
            if "key_source" in ln or "不落盘" in ln:
                print(f"  {Path(rel).name} | {ln.strip()[:160]}")

    rep = {"schema": "v4_cpatomic_keyscan/1", "date": "2026-09-28",
           "new_files": new_rows, "src_readonly_files": src_rows,
           "n_hits_new_total": n_new, "n_hits_src_total": n_src,
           "key_plaintext_found": (n_new + n_src) > 0,
           "method": "re pattern scan (5 类), 0 LLM, 纯本地"}
    out = ROOT / ".tmp/_cpatomic_keyscan_2026_09_28.json"
    out.write_text(json.dumps(rep, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nkey 明文命中总计 = {n_new + n_src}  (新出件 {n_new} / 源件 {n_src})")
    print(f"OUT -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
