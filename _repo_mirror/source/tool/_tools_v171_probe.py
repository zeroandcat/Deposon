# -*- coding: utf-8 -*-
"""v171 落账件探针：源件字节面自测 + 长名式探测 + 关键语汇全文命中数。
纪律：路径原始字符串；控制台仅 ASCII；结果落 UTF-8 文件。
"""
import hashlib
import io
import json
import os
import re

ROOT = r"_repo_mirror"

SOURCES = [
    ("register_v171", r"pi_rulings\_pi_card_answers_register_2026_10_20_v171.md"),
    ("exemplar_v170", r"results\_v170_adoption_effect_2026_10_20.md"),
    ("exemplar_v169", r"results\_v169_adoption_effect_2026_10_20.md"),
    ("verdict_clearance", r"results\_kd_mda8a24_clearance_verdict_2026_10_20.md"),
    ("caliber_q0", r"results\_kd_identified_defect_attribution_caliber_2026_10_20.md"),
    ("proposals_release", r"results\_mda8a24_release_trigger_proposals_2026_10_20.md"),
    ("comparison_two_gates", r"results\_kd_two_gates_comparison_2026_10_20.md"),
    ("construct_new", r"results\_preexp_design_new_construct_mda8a24_2026_10_20.md"),
    ("verdict_sepcal7", r"results\_kd_sepcal7_final_verdict_2026_10_20.md"),
    ("proposals_fkd", r"results\_kd_false9_remedy_proposals_2026_10_20.md"),
]

PHRASES = [
    "读甲",
    "读丙",
    "射程",
    "甲-C5",
    "退化门",
    "触发态",
    "挂账",
    "三候选",
    "释-甲",
    "可逆",
    "归因层",
    "射程边界",
    "存在",
    "形态",
    "另议",
    "并存明层级",
    "静默落空",
    "K-MDA8A2-4",
    "K-FKD-2-1",
    "K-IDAC-1-1",
    "K-SEPCAL-7",
    "Q0",
]


def sha12(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12]


def full_sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def stat_of(path):
    b = open(path, "rb").read()
    txt = b.decode("utf-8")
    st = os.stat(path)
    import datetime
    mt = datetime.datetime.fromtimestamp(st.st_mtime).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    return {
        "path": path,
        "rel": os.path.relpath(path, ROOT),
        "sha12": sha12(path),
        "bytes": len(b),
        "lf": b.count(b"\x0a"),
        "cr": b.count(b"\x0d"),
        "tab": b.count(b"\x09"),
        "vt": b.count(b"\x0b"),
        "bom": 1 if b[:3] == b"\xef\xbb\xbf" else 0,
        "ufffd": txt.count("\ufffd"),
        "lines": txt.count("\n"),
        "ends_with_lf": b.endswith(b"\x0a"),
        "mtime": mt,
        "crlf_pairs": b.count(b"\x0d\x0a"),
    }


def longname_probe():
    pats = ["*v171*", "*adoption_effect*", "*_v171_adoption_effect*", "*_kd_mda8a24*", "*_mda8a24*"]
    res = {}
    allf = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "node_modules", "__pycache__")]
        for n in fn:
            allf.append(os.path.join(dp, n))
    for p in pats:
        hits = [os.path.relpath(x, ROOT) for x in allf if p.strip("*").lower() in os.path.basename(x).lower()]
        res[p] = {"count": len(hits), "hits": sorted(hits)[:60]}
    # per-dir counts
    per = {}
    for x in allf:
        d = os.path.relpath(os.path.dirname(x), ROOT)
        per[d] = per.get(d, 0) + 1
    res["_dir_counts"] = dict(sorted(per.items(), key=lambda kv: -kv[1]))
    res["_total"] = len(allf)
    return res


def phrase_scan():
    counts = {p: {"hits": 0, "files": 0, "sample_files": []} for p in PHRASES}
    exts = (".md", ".json", ".txt")
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "node_modules", "__pycache__")]
        for n in fn:
            if not n.lower().endswith(exts):
                continue
            p = os.path.join(dp, n)
            try:
                t = open(p, "r", encoding="utf-8", errors="replace").read()
            except Exception:
                continue
            for ph in PHRASES:
                c = t.count(ph)
                if c:
                    counts[ph]["hits"] += c
                    counts[ph]["files"] += 1
                    if len(counts[ph]["sample_files"]) < 6:
                        counts[ph]["sample_files"].append(os.path.relpath(p, ROOT))
    return counts


def main():
    out = {}
    out["sources"] = {}
    for key, rel in SOURCES:
        p = os.path.join(ROOT, rel)
        out["sources"][key] = stat_of(p) if os.path.exists(p) else {"rel": rel, "missing": True}
    out["probe"] = longname_probe()
    out["phrases"] = phrase_scan()
    # full sha for the delivery target check
    tgt = os.path.join(ROOT, r"results\_v171_adoption_effect_2026_10_20.md")
    out["target_exists_before"] = os.path.exists(tgt)
    dst = os.path.join(ROOT, "_tools_v171_probe_out.json")
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("PROBE_OK sources=" + str(len(out["sources"])) + " total_files=" + str(out["probe"]["_total"]))
    print("TARGET_EXISTS_BEFORE=" + str(out["target_exists_before"]))
    for p in ["*v171*", "*_v171_adoption_effect*"]:
        print(p + " -> " + str(out["probe"][p]["count"]))


if __name__ == "__main__":
    main()
