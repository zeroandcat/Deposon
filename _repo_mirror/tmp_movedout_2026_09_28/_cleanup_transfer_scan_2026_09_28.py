# -*- coding: utf-8 -*-
"""2026-09-28 每日收尾整理棒 · 第 4 动作「转移两方向」候选筛选 (worker)

候选池 = .tmp/ 中 LastWriteTime 落在 2026-09-28 的件 (今日产生的衍生/次要件)
分流判据:
  cited_letters  : 件名出现在 letters/*.md            -> 移动会令 PI 面委托材料所引路径落空 -> 不转移
  cited_results  : 件名出现在 results/*.md (排除两份「按名枚举 .tmp」性质的清单)
                   = 噪声清单 _v4_noise_cleanup_manifest_v4_2026_09_27.md
                   = 盘上计数清单 _v4_day_inventory_2026_09_27.md
                   -> 移动会令权威件所引路径落空 -> 不转移
  in_flight      : 在途链段缓冲 (E-48 段 .md, 内容尚未并入权威改判总表) -> 不转移
  其余 -> 转移候选 (项目衍生件 -> deposon-sub)
SHA-12 = hashlib.sha256(data).hexdigest()[:12] 小写
"""
import datetime
import hashlib
import pathlib
import sys

REPO = pathlib.Path(r"D:/私人资料/deposon-repo")
TMP = REPO / ".tmp"
DAY = datetime.date(2026, 9, 28)
EXCLUDE_RESULTS = {"_v4_noise_cleanup_manifest_v4_2026_09_27.md",
                   "_v4_day_inventory_2026_09_27.md"}
IN_FLIGHT = {"_e48_c1.md", "_e48_c2.md", "_e48_c3.md", "_e48_c4.md", "_e48_c5.md",
             "_e48_apply.py", "_e48_docwriter_chain.py", "_e48_docwriter_enum.py",
             "_e48_docwriter_hash.py", "_e48_docwriter_hash2.py", "_e48_probe_register.py"}


def sha12(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def load(patterns, drop=()):
    parts = []
    for pat in patterns:
        for p in sorted(REPO.glob(pat)):
            if p.name in drop:
                continue
            parts.append(p.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(parts)


def main():
    letters = load(["letters/*.md"])
    results = load(["results/*.md"], drop=EXCLUDE_RESULTS)
    self_tmp = load([".tmp/*.py", ".tmp/*.txt"])

    cands = [p for p in sorted(TMP.iterdir())
             if p.is_file()
             and datetime.date.fromtimestamp(p.stat().st_mtime) == DAY
             and not p.name.startswith("_cleanup_")]

    rows = []
    for p in cands:
        n = p.name
        rows.append({
            "name": n, "sha12": sha12(p), "size": p.stat().st_size,
            "L": n in letters, "R": n in results, "S": n in self_tmp,
            "F": n in IN_FLIGHT,
        })

    def verdict(r):
        if r["L"]:
            return "KEEP_letters_cited"
        if r["R"]:
            return "KEEP_results_cited"
        if r["F"]:
            return "KEEP_in_flight"
        return "TRANSFER"

    print(f"[today] .tmp/ 今日产生件 {len(cands)} 件\n")
    print(f"{'verdict':24} {'L':2} {'R':2} {'F':2}  name")
    for r in sorted(rows, key=lambda x: (verdict(x), x["name"])):
        print(f"{verdict(r):24} {str(r['L'])[0]:2} {str(r['R'])[0]:2} {str(r['F'])[0]:2}  "
              f"{r['name']}\t{r['sha12']}\t{r['size']}")
    tr = [r for r in rows if verdict(r) == "TRANSFER"]
    print(f"\n[TRANSFER] {len(tr)} 件 / {sum(r['size'] for r in tr)} B")
    print(f"[KEEP] {len(rows)-len(tr)} 件")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
