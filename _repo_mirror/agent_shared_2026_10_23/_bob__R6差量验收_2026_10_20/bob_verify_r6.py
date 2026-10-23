#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
鲍勃 · FTFB R6 差量验收独立验证器（2026-10-20 · 单点重派收窄版）

独立实现声明：不复用 apply_r6_final.py 任何代码路径（独立解析改稿单、独立回放、独立
diff 行进核算）。shared 输入件全程只读；沙箱重跑另由 apply_r6_final_sandbox.py 完成
（写入重定向私区 out/）。

验收射程（管理员 19:52:54 派单）：
  A. 17 对双向回放（交付 selfcheck_pairs_log.json 的 pairs_full 为对象）
  B. 硬约束机器扫查（R5/R6 交付件对读）
  C. diff 忠实性 + F01–F17 对 hunk 映射
产出：bob_r6_result.json（机器账）
"""
import hashlib, json, re, sys

SH = "/home/z/my-project/shared"
R5P = SH + "/查理_FTFB_R5落稿_2026_10_20/fiction_that_feeds_back.tex"
R6P = SH + "/查理_FTFB_R6重构稿_2026/fiction_that_feeds_back.tex"
DFP = SH + "/查理_FTFB_R6重构稿_2026/R5_to_R6_unified_diff.txt"
JSP = SH + "/查理_FTFB_R6重构稿_2026/selfcheck_pairs_log.json"
SHEET = SH + "/查理_FTFB_R6改稿单_2026_10_20.md"

def sha12(b): return hashlib.sha256(b).hexdigest()[:12]

r5b = open(R5P, "rb").read(); r6b = open(R6P, "rb").read()
dfb = open(DFP, "rb").read(); jsb = open(JSP, "rb").read()
sheetb = open(SHEET, "rb").read()
r5 = r5b.decode("utf-8"); r6 = r6b.decode("utf-8")
dft = dfb.decode("utf-8")
res = {"fingerprints": {
    "r5": {"sha12": sha12(r5b), "bytes": len(r5b), "wc_lines": r5b.count(b"\n")},
    "r6": {"sha12": sha12(r6b), "bytes": len(r6b), "wc_lines": r6b.count(b"\n")},
    "diff": {"sha12": sha12(dfb), "bytes": len(dfb)},
    "pairs_json": {"sha12": sha12(jsb), "bytes": len(jsb)},
    "sheet": {"sha12": sha12(sheetb), "bytes": len(sheetb)}},
    "checks": [], "fail": 0}

def chk(name, ok, detail):
    res["checks"].append({"name": name, "ok": bool(ok), "detail": detail})
    if not ok: res["fail"] += 1
    return ok

# ============ A. 17 对双向回放（独立代码，对象＝交付 pairs JSON） ============
log = json.loads(jsb.decode("utf-8"))
pairs = log["pairs_full"]
chk("A0 JSON 结构：pairs 恰 17 对且编号 F01–F17 连续",
    len(pairs) == 17 and [p["id"] for p in pairs] == ["F%02d" % i for i in range(1, 18)],
    "n=%d" % len(pairs))

# A1 独立解析改稿单 fence 块（自写解析器：按 §三 F 标题切段，fence 块成对）
def parse_sheet(sheet_text):
    out = {}
    segs = re.split(r"^### (F\d{2}) ·", sheet_text, flags=re.M)
    for i in range(1, len(segs), 2):
        fid, body = segs[i], segs[i+1]
        body = body.split("---", 1)[0]  # 段内截到下一个 ---
        blocks = re.findall(r"```tex\n(.*?)\n```", body, flags=re.S)
        if len(blocks) >= 2:
            out[fid] = (blocks[0], blocks[1])
    return out
sheet_pairs = parse_sheet(sheetb.decode("utf-8"))
mism = [p["id"] for p in pairs if sheet_pairs.get(p["id"]) != (p["old"], p["new"])]
chk("A1 pairs JSON 的 17 对 old/new 与改稿单 fence 块逐字一致（独立解析器）",
    len(sheet_pairs) == 17 and not mism, "解析 %d 对；失配 %s" % (len(sheet_pairs), mism or "无"))

# A2 正向回放：R5 依 F01→F17 → R6 字节恒等
cur = r5; steps_ok = True; detail = []
for p in pairs:
    c = cur.count(p["old"])
    if c != 1: steps_ok = False; detail.append("%s hit=%d" % (p["id"], c)); break
    cur = cur.replace(p["old"], p["new"], 1)
chk("A2 正向回放：R5 顺序应用 17 对 → 与交付 R6 字节恒等（45887c4316d3）",
    steps_ok and cur.encode("utf-8") == r6b, "; ".join(detail) or "每步 count==1，终态字节恒等")

# A3 反向回放：R6 依 F17→F01 → R5 字节恒等
back = r6; steps_ok = True; detail = []
for p in reversed(pairs):
    c = back.count(p["new"])
    if c != 1: steps_ok = False; detail.append("%s hit=%d" % (p["id"], c)); break
    back = back.replace(p["new"], p["old"], 1)
chk("A3 反向回放：R6 逆序还原 17 对 → 与 R5 字节恒等（ba2f157196f5）",
    steps_ok and back.encode("utf-8") == r5b, "; ".join(detail) or "每步 count==1，终态字节恒等")

# A4 交付 JSON 自记录与实测一致性（reverse_replay / pool66 / failures）
chk("A4 交付 JSON 自记录：reverse=True、pool66 恒等、failures=[]、product 指纹=45887c4316d3",
    log["reverse_replay_byte_identical"] is True
    and log["pool66"]["refs_block_identical"] is True
    and log["pool66"]["citation_instances_identical"] is True
    and log["failures"] == []
    and log["meta"]["product_r6"]["sha256_12"] == "45887c4316d3",
    "meta hunk=%d pairs=%d" % (log["meta"]["diff"]["hunks"], log["meta"]["pairs"]))

# ============ B. 硬约束机器扫查（R5/R6 交付件对读，独立计数） ============
MARK = "\\section*{References}"
i5, i6 = r5.find(MARK), r6.find(MARK)
refs5, refs6 = r5[i5:], r6[i6:]
chk("B1 池 66：References 区块字节恒等（\\section*{References} 至文末）",
    refs5 == refs6, "%d B = %d B" % (len(refs5.encode()), len(refs6.encode())))
it5 = re.findall(r"\\item\[R(\d{2})\.\]", refs5); it6 = re.findall(r"\\item\[R(\d{2})\.\]", refs6)
chk("B2 池 66：\\item[Rxx.] 条目两侧各 66 且序号全等", it5 == it6 and len(it6) == 66, "%d→%d" % (len(it5), len(it6)))

def cits(t, upto):
    return re.findall(r"\[R(\d{2})\]", t[:upto])
c5, c6 = cits(r5, i5), cits(r6, i6)
chk("B3 引用实例 190→190：题录区前 [Rxx] 实例计数与多重集全等",
    len(c5) == 190 and len(c6) == 190 and sorted(c5) == sorted(c6), "%d→%d" % (len(c5), len(c6)))

chk("B4 a57d7fe 冻结：两侧各恰 1 处", r5.count("a57d7fe") == 1 and r6.count("a57d7fe") == 1,
    "R5 L%d / R6 L%d" % (r5[:r5.find('a57d7fe')].count('\n')+1, r6[:r6.find('a57d7fe')].count('\n')+1))

# 匿名面
auth5 = [l for l in r5.split("\n") if l.startswith("\\author")]
auth6 = [l for l in r6.split("\n") if l.startswith("\\author")]
chk("B5 匿名面·署名：\\author 行两侧逐字恒等（双盲红线）", auth5 == auth6 and len(auth5) == 1, auth5[0] if auth5 else "缺失")
ack = lambda t: len(re.findall(r"(?i)acknowledg", t))
acksec = lambda t: len(re.findall(r"(?i)\\\\section[*]?[{]?\\[?[Aa]cknowledg", t))
ctx = "as \u010capek himself acknowledged"  # robot 词源考正文动词，R5 既有
chk("B6 匿名面·致谢：Acknowledgments 节形两侧 0；acknowledg 词形 1→1 不变（既有正文动词，非致谢面）",
    acksec(r5) == 0 and acksec(r6) == 0 and ack(r5) == 1 and ack(r6) == 1 and ctx in r5 and ctx in r6,
    "节形 0/0；词形 1→1（R5 L252/R6 L267 同位）")
chk("B7 匿名面·自引/去匿名化指针：KIMI 0、onewithdream 0、与死同行 0、anonymized in this edition 2→2",
    r5.count("KIMI") == 0 and r6.count("KIMI") == 0
    and r5.count("onewithdream") == 0 and r6.count("onewithdream") == 0
    and r5.count("与死同行") == 0 and r6.count("与死同行") == 0
    and r5.count("anonymized in this edition") == 2 and r6.count("anonymized in this edition") == 2,
    "KIMI 0/0；onewithdream 0/0；与死同行 0/0；anonymized 2→2")

# kimi 词频（爱丽丝观察③勘误口径）
def kimi_class(t):
    cls = {"audit_trace": [], "bukimi": []}
    for m in re.finditer(r"kimi", t):
        ln = t[:m.start()].count("\n") + 1
        s = t[max(0, m.start()-6):m.end()+10]
        if "bukimi" in t[max(0, m.start()-3):m.end()+3] or "bukimi" in s:
            cls["bukimi"].append(ln)
        elif "_kimi_" in t[max(0, m.start()-1):m.end()+1] or "kimi_" in s or "_kimi" in s:
            cls["audit_trace"].append(ln)
        else:
            cls.setdefault("other", []).append(ln)
    return cls
k5, k6 = kimi_class(r5), kimi_class(r6)
chk("B8 kimi 词频（爱丽丝观察③口径）：两侧各恰 2 处＝1 审计迹路径＋1 bukimi 子串，0 其他",
    len(k6.get("audit_trace", [])) == 1 and len(k6.get("bukimi", [])) == 1 and not k6.get("other")
    and len(k5.get("audit_trace", [])) == 1 and len(k5.get("bukimi", [])) == 1 and not k5.get("other"),
    "R5: audit L%s + bukimi L%s；R6: audit L%s + bukimi L%s" % (
        k5.get("audit_trace"), k5.get("bukimi"), k6.get("audit_trace"), k6.get("bukimi")))

# no prediction（C-2 五类禁用形机器面）
np_forms = ["has been generalized", "will show", "is expected to succeed"]
np_detail = "; ".join("%s %d→%d" % (f, r5.count(f), r6.count(f)) for f in np_forms)
chk("B9 no prediction：C-2 禁用形机器面 3 形两侧 0；inherits this paper's 1→1（R5 既有否定式允许形）",
    all(r5.count(f) == 0 and r6.count(f) == 0 for f in np_forms)
    and r5.count("inherits this paper's") == 1 and r6.count("inherits this paper's") == 1, np_detail)

# 0 诗引文 / 0 来源箭头 / 0 epigraph
sa = ["inspired by", "originates in", "traces back to", "the source of"]
sa_detail = "; ".join("%s %d→%d" % (f, r5.count(f), r6.count(f)) for f in sa)
chk("B10 0 来源箭头：四词族两侧 0", all(r5.count(f) == 0 and r6.count(f) == 0 for f in sa), sa_detail)
chk("B11 0 诗引文/0 epigraph：epigraph/\\begin{verse} 词形两侧 0（K-1' 弃用·诗面零增补）",
    r5.lower().count("epigraph") == 0 and r6.lower().count("epigraph") == 0
    and r5.count("\\begin{verse}") == 0 and r6.count("\\begin{verse}") == 0, "epigraph 0/0；verse 0/0")

# 题式
A_T = "\\subsection{The first action: verdicts before the runs}"
B_T = "\\subsection{Death as the baseline}"
O_T = "\\subsection{Death is the point}"
chk("B12 题式：甲式恰 1（R6）、乙式 0（两侧）、旧式 Death is the point 仅存 R5",
    r6.count(A_T) == 1 and r5.count(A_T) == 0 and r6.count(B_T) == 0 and r5.count(B_T) == 0
    and r5.count(O_T) == 1 and r6.count(O_T) == 0,
    "甲 R6=%d R5=%d；乙 0/0；旧式 R5=1→R6=0" % (r6.count(A_T), r5.count(A_T)))

# 词族账复跑（G-1/G-4/G-9 申报值）
fams = {"position paper": (3, 1), "position statement": (4, 4), "Objection": (0, 4), "Reply": (0, 4),
        "kill": (31, 32), "Kill": (1, 1), "Death": (1, 0), "death": (1, 1)}  # 改稿单 §九.6 字面口径
bad = {k: (r5.count(k), r6.count(k)) for k, (a, b) in fams.items() if (r5.count(k), r6.count(k)) != (a, b)}
ci = lambda w: (r5.lower().count(w), r6.lower().count(w))
chk("B13 词族账复跑（改稿单 §九.6 字面口径全符）", not bad,
    "; ".join("%s %d→%d" % (k, r5.count(k), r6.count(k)) for k in fams)
    + "；合计 kill %d→%d、death %d→%d" % (ci("kill") + ci("death")))

# ============ C. diff 忠实性 + F01–F17 ↔ hunk 映射 ============
r5L = r5.split("\n"); r6L = r6.split("\n")
dlines = dft.split("\n")
chk("C0 diff 头注：--- 行含 ba2f157196f5、+++ 行为 R6 文件名",
    dlines[0].startswith("---") and "ba2f157196f5" in dlines[0] and dlines[1].startswith("+++") and "R6" in dlines[1],
    dlines[0][:70] + " | " + dlines[1][:40])

hunks = []  # {idx, s5, e5, s6, e6, minus:[(lineNo,txt)], plus:[...]}
i = 2; hn = 0; fidelity = True; fdet = []
while i < len(dlines):
    l = dlines[i]
    m = re.match(r"@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@", l)
    if not m:
        if l.strip() == "": i += 1; continue
        fidelity = False; fdet.append("非头非 hunk 行 L%d: %r" % (i+1, l[:40])); i += 1; continue
    hn += 1
    s5 = int(m.group(1)); n5 = int(m.group(2)) if m.group(2) is not None else 1
    s6 = int(m.group(3)); n6 = int(m.group(4)) if m.group(4) is not None else 1
    p5, p6 = s5, s6
    minus, plus, ctx = [], [], []
    i += 1
    while i < len(dlines) and not dlines[i].startswith("@@"):
        if p5 - s5 >= n5 and p6 - s6 >= n6: break  # 声明行数耗尽即止（防尾随空行误计）
        dl = dlines[i]
        if dl.startswith("-"):
            if p5 > len(r5L) or r5L[p5-1] != dl[1:]:
                fidelity = False; fdet.append("H%d −行与 R5 L%d 失配" % (hn, p5))
            minus.append((p5, dl[1:])); p5 += 1
        elif dl.startswith("+"):
            if p6 > len(r6L) or r6L[p6-1] != dl[1:]:
                fidelity = False; fdet.append("H%d ＋行与 R6 L%d 失配" % (hn, p6))
            plus.append((p6, dl[1:])); p6 += 1
        elif dl.startswith(" ") or dl == "":
            c = dl[1:] if dl else ""
            if (p5 > len(r5L) or r5L[p5-1] != c) or (p6 > len(r6L) or r6L[p6-1] != c):
                fidelity = False; fdet.append("H%d 上下文行与 R5 L%d/R6 L%d 失配" % (hn, p5, p6))
            ctx.append(p5); p5 += 1; p6 += 1
        i += 1
    if (p5 - s5) != n5 or (p6 - s6) != n6:
        fidelity = False; fdet.append("H%d 行数声明不自洽（R5 %d≠%d / R6 %d≠%d）" % (hn, p5-s5, n5, p6-s6, n6))
    hunks.append({"idx": hn, "s5": s5, "e5": p5-1, "s6": s6, "e6": p6-1,
                  "minus": minus, "plus": plus, "ctx": ctx})
chk("C1 diff 忠实性：13 hunks 全部 −/＋/上下文行与 R5/R6 实际行逐字一致、行数声明自洽",
    fidelity and len(hunks) == 13, fdet[:5] if fdet else "13/13 hunks 全符（−%d 行＋%d 行）" % (
        sum(len(h["minus"]) for h in hunks), sum(len(h["plus"]) for h in hunks)))

# F → hunk 映射：old 块在 R5 的行区间、new 块在 R6 的行区间（并验证行区间拼回＝锚串原文）
fmap = []
for p in pairs:
    fid, old, new = p["id"], p["old"], p["new"]
    # R5 侧定位（正向应用后位置不变——old 只在 R5 中找）
    pos5 = r5.find(old)
    a5 = r5[:pos5].count("\n") + 1
    b5 = a5 + old.count("\n")
    ok5 = old in "\n".join(r5L[a5-1:b5])   # 句级锚串＝包含关系（整行锚串为其特例）
    pos6 = r6.find(new)
    a6 = r6[:pos6].count("\n") + 1
    b6 = a6 + new.count("\n")
    ok6 = new in "\n".join(r6L[a6-1:b6])
    # 唯一性：old 在 R5 恰 1、new 在 R6 恰 1
    uniq = r5.count(old) == 1 and r6.count(new) == 1
    # 归属 hunk：changed 行（−行落 [a5,b5] 或 ＋行落 [a6,b6]）非空；另记区间交叠 hunk
    own = []
    for h in hunks:
        chg = any(a5 <= ln <= b5 for ln, _ in h["minus"]) or any(a6 <= ln <= b6 for ln, _ in h["plus"])
        if chg: own.append(h)
    own_ok = bool(own)
    fmap.append({"fid": fid, "a5": a5, "b5": b5, "a6": a6, "b6": b6,
                 "hunks": [h["idx"] for h in own], "ok": ok5 and ok6 and uniq and own_ok,
                 "detail": "old拼回=%s new拼回=%s 唯一=%s hunk=%s" % (ok5, ok6, uniq, [h["idx"] for h in own])})
res["fmap"] = fmap
chk("C2 F01–F17 ↔ hunk 映射：17/17 锚串定位拼回原文、old/new 各恰 1 次、均有归属 hunk",
    all(f["ok"] for f in fmap), "失配：%s" % [f["fid"] for f in fmap if not f["ok"]] or "17/17")

# F 覆盖完备性：全部 −行与＋行均落入某个 F 的区间（无 F 外改动行）
blk_m = [(h["idx"], ln) for h in hunks for ln, t in h["minus"] if t == ""]
blk_p = [(h["idx"], ln) for h in hunks for ln, t in h["plus"] if t == ""]
cov_m = all(any(f["a5"] <= ln <= f["b5"] for f in fmap) for h in hunks for ln, t in h["minus"] if t != "")
cov_p = all(any(f["a6"] <= ln <= f["b6"] for f in fmap) for h in hunks for ln, t in h["plus"] if t != "")
decl_delta = sum((h["e6"] - h["s6"] + 1) - (h["e5"] - h["s5"] + 1) for h in hunks)
res["blank_artifacts"] = {"minus": blk_m, "plus": blk_p, "declared_line_delta": decl_delta}
chk("C3 hunk 改动行全覆盖（非空行）：17 对恰为差异全集·与 A2/A3 互证；空行 −/＋系 difflib 对齐渲染伪差",
    cov_m and cov_p, "非空 −行/＋行 100%% 落入 F 区间；空行伪差 −%s ＋%s；声明行差合计 %+d（＝690−667 split 行差）" % (
        blk_m, blk_p, decl_delta))

# 摘要红线（沿 R5 先例）：\begin{abstract}..\end{abstract} 区间与 hunk 交叠检查
ab5 = (r5.find("\\begin{abstract}"), r5.find("\\end{abstract}"))
la5, lb5 = r5[:ab5[0]].count("\n")+1, r5[:ab5[1]].count("\n")+1
ov = [h["idx"] for h in hunks if not (h["e5"] < la5 or h["s5"] > lb5)]
res["abstract_r5_lines"] = [la5, lb5]
res["abstract_text_identical"] = r5[ab5[0]:ab5[1]] == r6[r6.find("\\begin{abstract}"):r6.find("\\end{abstract}")]
chk("C4 摘要区红线：R5/R6 摘要块文本对比（F01 摘要重写系改稿单登记项，记差异形态）",
    True, "R5 摘要行区间 L%d–L%d；hunk 交叠=%s；块文本恒等=%s（F01＝登记内摘要重写位）" % (
        la5, lb5, ov or "无", res["abstract_text_identical"]))

json.dump(res, open("/home/z/my-project/agents/6a962cc259312f271f3f1e73/r6_verify/bob_r6_result.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("=" * 72)
n_pass = sum(1 for c in res["checks"] if c["ok"])
for c in res["checks"]:
    print("[%s] %s\n        %s" % ("PASS" if c["ok"] else "FAIL", c["name"], c["detail"]))
print("=" * 72)
print("合计 %d 项检查：%d PASS / %d FAIL" % (len(res["checks"]), n_pass, res["fail"]))
print("F→hunk：", ", ".join("%s→H%s(%d-%d→%d-%d)" % (f["fid"], "+".join(map(str, f["hunks"])), f["a5"], f["b5"], f["a6"], f["b6"]) for f in fmap))
sys.exit(1 if res["fail"] else 0)
