# -*- coding: utf-8 -*-
"""2026-09-28 每日收尾整理棒 · .tmp 三分类终判探针 (worker)

判据(按派工单):
  垃圾 = (未被任何权威件按路径引用) AND (内容已入权威件 OR 可证完全重复 OR 可证环境派生物)
  留痕 = 被权威件按路径引用(引证件) 或 内容未完整入权威件 或 可复算脚手架
  证据 = 落盘权威产物本体/登记件本体

权威件语料 = results/*.md + results/*.json + letters/*.md  (不含 .tmp 自身, 防自指)
SHA-12 = hashlib.sha256(data).hexdigest()[:12] 小写
"""
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(r"D:/私人资料/deposon-repo")
TMP = ROOT / ".tmp"
AUTH_GLOBS = ["results/*.md", "results/*.json", "letters/*.md"]


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def build_corpus():
    parts, n = [], 0
    for g in AUTH_GLOBS:
        for p in sorted(ROOT.glob(g)):
            parts.append(p.read_text(encoding="utf-8", errors="replace"))
            n += 1
    return "\n".join(parts), n


def main():
    corpus, nfiles = build_corpus()
    print(f"[corpus] 权威件 {nfiles} 件 / {len(corpus)} chars\n")

    me = pathlib.Path(__file__).name
    files = sorted(p for p in TMP.rglob("*")
                   if p.is_file() and p.name != me
                   and not p.name.startswith("_cleanup_probe"))
    print(f"[tmp] 待判 {len(files)} 件\n")

    cited, absorbed, dupmap = [], [], {}
    # 先算全 .tmp 内容重复组
    h = {}
    for p in files:
        h.setdefault(sha12(p), []).append(p)

    for p in files:
        name = p.name
        rel = p.as_posix().replace(".tmp/", ".tmp/")
        is_cited = name in corpus or rel in corpus or f".tmp/{name}" in corpus
        if is_cited:
            cited.append((p, sha12(p), len(h[sha12(p)])))
            continue
        if p.suffix == ".pyc":
            absorbed.append((p, sha12(p), "ENV_DERIVATIVE_PYC"))
            continue
        if len(h[sha12(p)]) > 1:
            absorbed.append((p, sha12(p), f"EXACT_DUP_OF_{len(h[sha12(p)])-1}"))
            continue
        # 内容吸收探测
        try:
            lines = [s for s in (ln.strip() for ln in
                                 p.read_text(encoding="utf-8", errors="replace").splitlines())
                     if len(s) >= 12]
        except Exception:
            continue
        if not lines:
            continue
        miss = [ln for ln in lines if ln not in corpus]
        if not miss:
            absorbed.append((p, sha12(p), "CONTENT_FULLY_ABSORBED"))

    print("=== 候选垃圾(未被权威件按路径引用 且 已证可清) ===")
    tot = 0
    for p, s12, why in absorbed:
        print(f"{p.as_posix()}\t{s12}\t{p.stat().st_size}\t{why}")
        tot += p.stat().st_size
    print(f"--> 候选垃圾 {len(absorbed)} 件 / {tot} bytes\n")

    print("=== 被权威件按路径引用 => 引证件/留痕, 不清 ===")
    for p, s12, grp in cited:
        tag = f"dupgroup={grp}" if grp > 1 else "unique"
        print(f"{p.as_posix()}\t{s12}\t{p.stat().st_size}\t{tag}")
    print(f"--> 引用件 {len(cited)} 件")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
