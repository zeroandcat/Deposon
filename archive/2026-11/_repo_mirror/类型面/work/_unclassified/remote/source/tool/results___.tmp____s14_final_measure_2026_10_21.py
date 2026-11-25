#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 · 末测：①同形异义编号对表（vNNN 双面）②key 形态自扫（⛔0 输出凭据明文）
③本棒自用工件清单 ④交付面逐件终表（落笔前基线）
"""
import os, io, re, glob, hashlib, datetime, collections

ROOT = r"_repo_mirror"
OUT = r"〔幽灵引用·原件已缺席·未上传:_s14_final_measure_2026_10_21.md〕"
WIN_START_MS = 1792482013000

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

def main():
    L = []
    L.append("# §14 · 末测（观测时点 %s）" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    L.append("")
    L.append("## 一、同形异义编号对表（token vNNN 之双面并存）")
    L.append("判据：同号 token 在两族面各有一件·指纹各异 ⇒ 引用必带族标＋宿主件指纹")
    idx = collections.defaultdict(list)
    for surf in ("results", "pi_rulings"):
        for dp, dn, fn in os.walk(os.path.join(ROOT, surf)):
            for n in fn:
                if "/.tmp/" in dp.replace("\\", "/"):
                    continue
                m = re.search(r"_v(\d{2,3})(?![0-9])", n)
                if not m:
                    continue
                p = os.path.join(dp, n)
                idx[m.group(1)].append((os.path.relpath(p, ROOT).replace("\\", "/"), sha12(p),
                                        os.path.getsize(p),
                                        datetime.datetime.fromtimestamp(os.path.getmtime(p)).strftime("%m-%d %H:%M:%S")))
    dual = 0
    for k in sorted(idx, key=lambda x: int(x)):
        rows = idx[k]
        fam = set(r[0].split("/")[0] for r in rows)
        if len(rows) >= 2 and len(fam) >= 2:
            dual += 1
            L.append("")
            L.append("### token `v%s`（双面并存）" % k)
            for rel, s, nb, mt in sorted(rows):
                L.append("- `%s` ｜ %s ｜ %d B ｜ %s" % (s, rel, nb, mt))
    L.append("")
    L.append("- 双面并存 token 数 = %d" % dual)
    L.append("")
    L.append("## 二、key 形态自扫（⛔0 读 key 本身·⛔0 输出任何凭据明文·仅形态命中计数）")
    pats = {
        "sk- 前缀": re.compile(r"\bsk-[A-Za-z0-9_\-]{16,}"),
        "ghp_ 前缀": re.compile(r"\bghp_[A-Za-z0-9]{20,}"),
        "github_pat": re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}"),
        "AKIA 前缀": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
        "AIza 前缀": re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}"),
        "赋值型 api key": re.compile(r"(?i)\b(api[_\- ]?key|secret[_\- ]?key|access[_\- ]?token)\b\s*[=:]\s*[\"']?[A-Za-z0-9_\-]{16,}"),
        "Bearer 令牌": re.compile(r"(?i)\bbearer\s+[A-Za-z0-9_\-\.=]{20,}"),
    }
    counts = collections.Counter()
    scanned = 0
    for surf in ("results", "pi_rulings", "letters", "docs", "tools"):
        for dp, dn, fn in os.walk(os.path.join(ROOT, surf)):
            for n in fn:
                p = os.path.join(dp, n)
                rel = os.path.relpath(p, ROOT).replace("\\", "/")
                if "/.tmp/" in rel:
                    continue
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime_ns // 1000000 < WIN_START_MS:
                    continue
                scanned += 1
                try:
                    txt = io.open(p, "r", encoding="utf-8", errors="replace").read()
                except Exception:
                    continue
                for nm, rx in pats.items():
                    c = len(rx.findall(txt))
                    if c:
                        counts[nm] += c
                        L.append("- 命中 %s ×%d ｜ 源件 %s" % (nm, c, rel))
    L.append("- 扫描窗内交付件数 = %d" % scanned)
    L.append("- 各形态命中合计 = %d" % sum(counts.values()))
    L.append("- 形态清单 = " + "；".join("%s:%d" % (k, v) for k, v in counts.items()) if counts else "- 形态清单 = （0 命中）")
    L.append("")
    L.append("## 三、本棒（§14 之棒）自用工件清单（results/.tmp/ · 如实登记·⛔0 删除）")
    mine = sorted(glob.glob(os.path.join(ROOT, "results", ".tmp", "_s14*")))
    for p in mine:
        L.append("- `%s` ｜ %d B ｜ %s ｜ mtime %s" % (
            sha12(p), os.path.getsize(p), os.path.basename(p),
            datetime.datetime.fromtimestamp(os.path.getmtime(p)).strftime("%m-%d %H:%M:%S")))
    L.append("- 本棒自用工件现值 = %d 件" % len(mine))
    L.append("")
    L.append("## 四、交付面终表（落笔前基线·逐件实测）")
    rows = []
    for surf in ("results", "pi_rulings", "letters", "docs", "tools"):
        for dp, dn, fn in os.walk(os.path.join(ROOT, surf)):
            for n in fn:
                p = os.path.join(dp, n)
                rel = os.path.relpath(p, ROOT).replace("\\", "/")
                if "/.tmp/" in rel:
                    continue
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime_ns // 1000000 < WIN_START_MS:
                    continue
                rows.append((st.st_mtime_ns // 1000000, rel, st.st_size, sha12(p)))
    rows.sort()
    for mt, rel, nb, s in rows:
        L.append("- %s ｜ %s ｜ %d B ｜ %s" % (
            datetime.datetime.fromtimestamp(mt / 1000).strftime("%m-%d %H:%M:%S"), s, nb, rel))
    L.append("- 交付面窗内件计数（除 .tmp）= %d" % len(rows))
    with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("ok ->", OUT, "| dual_tokens=", dual, "| mine=", len(mine), "| delivery=", len(rows))

if __name__ == "__main__":
    main()
