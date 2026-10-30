#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""§14 · 锚链核验 v2：区分 MATCH／内容已变（同名异指纹）／仓内无同名件
并抽取主会话窗内事件锚（修正窗下界）。只读。
"""
import os, io, re, json, hashlib, datetime, collections

ROOT = r"_repo_mirror"
SESS = r"〔本地绝对路径·脱敏略:2026〕"
MAIN = os.path.join(SESS, "09", "01", "02-38-47-809-session_bXZzX2JiZWI4MDRiMWE2YTQxMTA5YmU3NDA2MzZlZWQxNzA5")
OUTA = r"〔幽灵引用·原件已缺席·未上传:_s14_anchorchain2_2026_10_21.md〕"
OUTB = r"〔幽灵引用·原件已缺席·未上传:_s14_main_events_2026_10_21.md〕"
WIN_START_MS = 1792482013000

def sha12(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()[:12].upper()

def build_index():
    by_hash = collections.defaultdict(list)
    by_name = collections.defaultdict(list)
    for dp, dn, fn in os.walk(ROOT):
        for n in fn:
            p = os.path.join(dp, n)
            try:
                sz = os.path.getsize(p)
                if sz > 40 * 1024 * 1024:
                    continue
                s = sha12(p)
            except OSError:
                continue
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            by_hash[s].append(rel)
            by_name[n.lower()].append((rel, s))
    return by_hash, by_name

def anchor_chain():
    by_hash, by_name = build_index()
    L = []
    L.append("# §14 · 锚链核验 v2（观测时点 %s）" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    L.append("# 全仓长名式递归索引：唯一指纹 %d · 文件名 %d" % (len(by_hash), len(by_name)))
    L.append("# 判据：MATCH＝所引指纹在仓内现存件上实测命中；")
    L.append("#       NAME_DIFF＝仓内存在同名件但指纹不同（内容已变／已覆写）；")
    L.append("#       NAME_ABSENT＝仓内 0 同名件（仓外引用或已移出）")
    L.append("")
    srcs = []
    for surf in ("pi_rulings", "results"):
        for dp, dn, fn in os.walk(os.path.join(ROOT, surf)):
            for n in fn:
                p = os.path.join(dp, n)
                try:
                    st = os.stat(p)
                except OSError:
                    continue
                if st.st_mtime_ns // 1000000 < WIN_START_MS:
                    continue
                rel = os.path.relpath(p, ROOT).replace("\\", "/")
                if "/.tmp/" in rel:
                    continue
                srcs.append(p)
    srcs.sort()
    pat = re.compile(r"\b([0-9A-Fa-f]{12})\b")
    # 名称上下文：取指纹前 120 字符中的文件名 token
    namepat = re.compile(r"([A-Za-z0-9_\-一-鿿]{4,}\.(?:md|json|py|ps1|jsonl|txt))")
    tot = collections.Counter()
    details = []
    for p in srcs:
        rel = os.path.relpath(p, ROOT).replace("\\", "/")
        txt = io.open(p, "r", encoding="utf-8", errors="replace").read()
        seen = []
        for m in pat.finditer(txt):
            t = m.group(1).upper()
            if t not in [x[0] for x in seen]:
                ctx = txt[max(0, m.start() - 160):m.start()]
                nm = namepat.findall(ctx)
                seen.append((t, nm[-1] if nm else ""))
        if not seen:
            continue
        cm = collections.Counter()
        rows = []
        for t, nm in seen:
            if t in by_hash:
                cm["MATCH"] += 1
                rows.append((t, "MATCH", nm, by_hash[t]))
            elif nm and nm.lower() in by_name:
                cm["NAME_DIFF"] += 1
                rows.append((t, "NAME_DIFF", nm, by_name[nm.lower()]))
            else:
                cm["NAME_ABSENT"] += 1
                rows.append((t, "NAME_ABSENT", nm, []))
        tot.update(cm)
        details.append((rel, len(seen), cm, rows))
    L.append("## 逐件摘要（源件＝窗内 pi_rulings/ ＋ results/ 交付件）")
    for rel, n, cm, rows in details:
        L.append("- %-72s 引用 %4d ｜ MATCH %4d ｜ NAME_DIFF %3d ｜ NAME_ABSENT %4d" % (
            rel[-72:], n, cm["MATCH"], cm["NAME_DIFF"], cm["NAME_ABSENT"]))
    L.append("")
    L.append("## 合计（唯一指纹引用）")
    L.append("- 源件数 = %d" % len(details))
    for k in ("MATCH", "NAME_DIFF", "NAME_ABSENT"):
        L.append("- %s = %d" % (k, tot[k]))
    L.append("- 合计 = %d" % sum(tot.values()))
    L.append("")
    L.append("## NAME_DIFF 逐件明细（内容已变之可查面）")
    for rel, n, cm, rows in details:
        for t, stt, nm, paths in rows:
            if stt == "NAME_DIFF":
                L.append("- 源件 %s ｜ 引 %s ｜ 名 %s" % (rel, t, nm))
                for pr in paths[:2]:
                    L.append("    → 仓内同名件 %s ｜ 现值指纹 %s" % (pr[0], pr[1]))
    with io.open(OUTA, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("anchorchain2 ->", OUTA, dict(tot))

def main_events():
    p = os.path.join(MAIN, "messages.jsonl")
    rows = []
    with io.open(p, "r", encoding="utf-8", errors="replace") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:
                continue
            m = o.get("message") if isinstance(o.get("message"), dict) else o
            t = m.get("timestamp")
            if not isinstance(t, (int, float)) or t < WIN_START_MS:
                continue
            role = m.get("role")
            c = m.get("content")
            txt = c if isinstance(c, str) else ""
            if not txt and isinstance(m.get("summary"), str):
                txt = m["summary"]
            rows.append((int(t), ln, role, txt, m))
    rows.sort(key=lambda r: (r[0], r[1]))
    L = []
    L.append("# §14 · 主会话窗内事件锚（修正窗下界 2026-10-20 15:40:13 CST）· 观测时点 %s" % datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    L.append("# 源 = %s · 窗内记录数 = %d" % (p, len(rows)))
    L.append("")
    for t, ln, role, txt, m in rows:
        stamp = datetime.datetime.fromtimestamp(t / 1000).strftime("%m-%d %H:%M:%S")
        flat = " ".join(txt.split())
        ctype = m.get("customType") or (m.get("details") or {}).get("version") or ""
        if role == "assistant" and flat:
            L.append("[%s] L%d assistant :: %s" % (stamp, ln, flat[:600]))
        elif role == "toolResult" and ("wrote" in flat.lower() or "SHA12" in flat or "bytes" in flat.lower() or "success" == flat.lower()):
            L.append("[%s] L%d toolResult :: %s" % (stamp, ln, flat[:300]))
        elif role == "user" and ("background-task-finished" in flat):
            L.append("[%s] L%d user(bg-finished) :: %s" % (stamp, ln, flat[:300]))
    with io.open(OUTB, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L) + "\n")
    print("main_events ->", OUTB, "records=", len(rows))

if __name__ == "__main__":
    anchor_chain()
    main_events()
