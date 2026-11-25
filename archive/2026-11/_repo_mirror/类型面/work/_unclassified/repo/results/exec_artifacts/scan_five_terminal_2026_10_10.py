# -*- coding: utf-8 -*-
"""五终判口径更新 · 全域核检索脚本（只读扫描，0 写盘业务件）
产出：.tmp/five_terminal_scan_2026_10_10.json
纪律：0 网络 / 0 key / 0 LLM；排除 .git；仅读 *.md *.py *.json *.txt
"""
import os, json, re, sys

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


ROOT = r_dep_path("")
OUT = os.path.join(ROOT, ".tmp", "five_terminal_scan_2026_10_10.json")
EXTS = (".md", ".py", ".json", ".txt")

# 主检索式（精确子串 / 正则）
PATTERNS = {
    "P01_三态":            {"kind": "sub", "p": "三态"},
    "P02_三态收口":         {"kind": "sub", "p": "三态收口"},
    "P03_三态纪律":         {"kind": "sub", "p": "三态纪律"},
    "P04_三态落档":         {"kind": "sub", "p": "三态落档"},
    "P05_三态可裁":         {"kind": "sub", "p": "三态可裁"},
    "P06_终点必须且只能是":   {"kind": "sub", "p": "终点必须且只能是"},
    "P07_终态只出":         {"kind": "sub", "p": "终态只出"},
    "P08_0不明收口":        {"kind": "sub", "p": "0 不明收口"},
    "P09_0不明收口_无空格":   {"kind": "sub", "p": "0不明收口"},
    "P10_PARTIAL_PASS":   {"kind": "sub", "p": "PARTIAL_PASS"},
    # PASS/FAIL/KD 族（含全角／、顿号、斜杠、空格变体；顺序含正反）
    "P11_PASS_FAIL_KD族":  {"kind": "rx",
        "p": r"PASS\s*[／/、,，·|]\s*FAIL\s*[／/、,，·|]\s*KD|KD\s*[／/、,，·|]\s*PASS\s*[／/、,，·|]\s*FAIL|FAIL\s*[／/、,，·|]\s*KD|PASS\s*[／/、,，·|]\s*KD"},
    "P12_PASS_FAIL族":     {"kind": "rx", "p": r"PASS\s*[／/]\s*FAIL"},
    "P13_五终判":          {"kind": "sub", "p": "五终判"},
    "P14_give-up":         {"kind": "sub", "p": "give-up"},
    "P15_artifact-free":   {"kind": "sub", "p": "artifact-free"},
    "P16_artifact_free":   {"kind": "sub", "p": "artifact_free"},
    "P17_判af":            {"kind": "sub", "p": "判af"},
    "P18_终判":            {"kind": "sub", "p": "终判"},
    # 同形异义探测（须剔除）
    "P19_三态裁决_物理":    {"kind": "sub", "p": "三态裁决"},
    "P20_三判断棒":        {"kind": "sub", "p": "三判断棒"},
    "P21_三判据":          {"kind": "sub", "p": "三判据"},
    "P22_三判项":          {"kind": "sub", "p": "三判项"},
    "P23_合规不合规须裁":    {"kind": "rx", "p": r"合规／不合规／须裁|合规/不合规/须裁"},
    "P24_五类悬置态":      {"kind": "sub", "p": "五类悬置态"},
}

results = {k: {"total": 0, "files": {}} for k in PATTERNS}
filecount = 0
read_err = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    dirnames[:] = [d for d in dirnames if d != ".git"]
    for fn in filenames:
        if not fn.lower().endswith(EXTS):
            continue
        fp = os.path.join(dirpath, fn)
        try:
            with open(fp, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            read_err.append([os.path.relpath(fp, ROOT).replace("\\", "/"), str(e)][:])
            continue
        if "\x00" in text[:2048]:
            continue  # 非 UTF-8 文本/二进制，跳过
        filecount += 1
        rel = os.path.relpath(fp, ROOT).replace("\\", "/")
        lines = text.split("\n")
        for key, spec in PATTERNS.items():
            if spec["kind"] == "sub":
                n = text.count(spec["p"])
                if n:
                    ln = [i + 1 for i, l in enumerate(lines) if spec["p"] in l]
                    results[key]["total"] += n
                    results[key]["files"][rel] = {"count": n, "lines": ln}
            else:
                rx = re.compile(spec["p"])
                hits = rx.findall(text)
                if hits:
                    ln = [i + 1 for i, l in enumerate(lines) if rx.search(l)]
                    results[key]["total"] += len(hits)
                    results[key]["files"][rel] = {"count": len(hits), "lines": ln}

out = {
    "root": ROOT,
    "files_scanned": filecount,
    "read_errors": read_err,
    "results": results,
}
with open(OUT, "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)

# 控制台摘要
for k, v in results.items():
    print("%-24s total=%-5d files=%d" % (k, v["total"], len(v["files"])))
print("scanned_files=%d  read_errors=%d" % (filecount, len(read_err)))