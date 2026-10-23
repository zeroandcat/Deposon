#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""鲍勃 · FTFB R6-F18 独立验证器（0 改稿 · 只读 · 不复用查理任何代码路径）

对象：交付 selfcheck_f18_pairs_log.json 之 F18 对；F18 前态正本（归档 tar 内件）；
交付 F18 后态 tex；R5 基线＋17 对（复合链增量核对）。
方法：独立提取/独立回放/独立计数，仅以交付 JSON 为「待验断言」输入。
"""
import re, json, hashlib, sys

BASE = "/home/z/my-project/agents/6a962cc259312f271f3f1e73/f18_check_2026_10_20"
SNAP = BASE + "/snap"
PRE = BASE + "/pre_f18_from_tar/fiction_that_feeds_back.tex"
DAVE_FLAT = "/home/z/my-project/shared/戴夫_FTFB_R6编译打包_2026/归档_预F18_8f2c4731/fiction_that_feeds_back.tex"
OLD_SHEET = BASE + "/pre_f18_from_tar/arxiv_metadata.txt"

def rd(p): return open(p, encoding="utf-8").read()
def sha12b(b): return hashlib.sha256(b).hexdigest()[:12]
def sha12f(p): return sha12b(open(p, "rb").read())

pre = rd(PRE); post = rd(SNAP + "/delivered_f18.tex"); r5 = rd(SNAP + "/r5.tex")
log = json.loads(rd(SNAP + "/selfcheck_f18_pairs_log.json"))
log17 = json.loads(rd(SNAP + "/selfcheck_pairs_log.json"))
pairs17 = log17["pairs_full"]
OLD = log["pair"]["old_abstract"]; NEW = log["pair"]["new_abstract"]

res = {"checks": [], "fail": 0}
def chk(cid, name, ok, detail):
    res["checks"].append({"id": cid, "name": name, "ok": bool(ok), "detail": detail})
    if not ok: res["fail"] += 1
    print(("PASS " if ok else "FAIL ") + cid + " " + name + " | " + detail)

def line_of(t, sub):
    for i, l in enumerate(t.split("\n"), 1):
        if sub in l: return i
    return -1

# ============ A. 单锚验证（F18 对 · 独立回放） ============
chk("A0", "pairs JSON 指纹登记值＝实测（入 45887c4316d3·132,269 B／出 69125dd78382·132,173 B·689 行）",
    log["input_tex"]["sha12"] == sha12f(PRE) and log["input_tex"]["bytes"] == 132269
    and log["output_tex"]["sha12"] == sha12f(SNAP + "/delivered_f18.tex")
    and log["output_tex"]["bytes"] == 132173 and log["output_tex"]["lines"] == 689,
    "in %s·%dB → out %s·%dB·%d 行（登记＝实测）" % (
        log["input_tex"]["sha12"], log["input_tex"]["bytes"],
        log["output_tex"]["sha12"], log["output_tex"]["bytes"], log["output_tex"]["lines"]))

# A1/A2 独立提取（边界定位法：\begin{abstract} 与 \end{abstract} 之间原文，非查理正则复用）
def between(tex):
    b = tex.find("\\begin{abstract}"); e = tex.find("\\end{abstract}")
    assert b >= 0 and e > b
    return tex[b + len("\\begin{abstract}"):e]
bt_pre, bt_post = between(pre), between(post)
chk("A1", "前态摘要独立提取＝pair.old（结构：\\begin 行后恰 2 空行·摘要单行 L76·1 空行·\\end 行）",
    bt_pre == "\n\n\n" + OLD + "\n\n" and pre.split("\n")[75] == OLD,
    "between %d B；摘要行 L76" % len(bt_pre.encode()))
chk("A2", "后态摘要独立提取＝pair.new（同构）",
    bt_post == "\n\n\n" + NEW + "\n\n" and post.split("\n")[75] == NEW,
    "between %d B；摘要行 L76" % len(bt_post.encode()))

fwd = pre.replace(OLD, NEW, 1)
chk("A3", "正向回放：前态＋F18（old→new 单次替换）＝后态全文恒等",
    fwd == post, "重放全文＝交付 %s" % sha12f(SNAP + "/delivered_f18.tex"))
back = post.replace(NEW, OLD, 1)
chk("A4", "反向回放：后态－F18（new→old 单次替换）＝前态全文恒等",
    back == pre, "重放全文＝前态 %s" % sha12f(PRE))

chk("A5", "单锚恰 1 处：old 在前态 1 次·new 在后态 1 次；new 不见于前态·old 不见于后态",
    pre.count(OLD) == 1 and post.count(NEW) == 1 and pre.count(NEW) == 0 and post.count(OLD) == 0,
    "old(pre)=%d new(post)=%d new(pre)=%d old(post)=%d" % (
        pre.count(OLD), post.count(NEW), pre.count(NEW), post.count(OLD)))

pl, ql = pre.split("\n"), post.split("\n")
diffs = [i for i in range(len(pl)) if pl[i] != ql[i]]
chk("A6", "行级增量（其余文本零改动的直接证明）：690 行中恰 1 行差异＝L76 摘要行，其余 689 行逐行恒等",
    len(pl) == len(ql) == 690 and diffs == [75], "差行列=%s；行数 %d=%d" % (diffs, len(pl), len(ql)))

nl = len(NEW)
chk("A7", "字符账（paste 口径＝单距空格单行）：len 1,973→1,877（Δ=96≥53）；词 291→277；"
    "raw-between 1,978→1,882；canonical 单距形态两侧成立；≤1,880 且 ≤1,920",
    len(OLD) == 1973 and nl == 1877 and log["pair"]["delta"] == 96
    and len(OLD.split()) == 291 and len(NEW.split()) == 277
    and len(bt_pre) == 1978 and len(bt_post) == 1882
    and " ".join(OLD.split()) == OLD and " ".join(NEW.split()) == NEW
    and nl <= 1880 and nl <= 1920 and 96 >= 53,
    "实测 len(new)=%d（与 JSON 登记同值）" % nl)

# A8 粘贴值三角（元数据件＋旧表第四源：旧表为 reflow 折行版，拼接归一后比对）
meta_txt = rd(SNAP + "/arxiv_metadata_abstract_F18_2026_10_20.txt")
mk = "paste as one paragraph):\n\n"
i8 = meta_txt.find(mk)
mab_val = meta_txt[i8 + len(mk):].rstrip("\n") if i8 >= 0 else ""
old_sheet = rd(OLD_SHEET)
k8 = old_sheet.find("When may fiction count as an input to the exact sciences")
paste_lines = []
for l in old_sheet[k8:].split("\n"):
    if not l.strip(): break
    paste_lines.append(l)
old_paste_norm = " ".join(" ".join(paste_lines).split())
chk("A8", "摘要多源一致：pair.old＝旧表粘贴值（reflow 拼接归一；戴夫 20:02 阻断项 1,973 同源）；"
    "pair.new＝交付 tex 摘要行＝元数据粘贴值（单行直取）；新摘要 0 署名信息",
    old_paste_norm == OLD and mab_val == NEW and post.split("\n")[75] == NEW
    and ("Yuan" not in NEW) and ("Qihao" not in NEW),
    "old 双源（tex 提取＋旧表粘贴）＋new 三源全等；旧表登记 1,978/1,973；元数据粘贴值 %d 字符" % len(mab_val))

# A9 F18 diff 结构核对（自写解析器）
dl = rd(SNAP + "/F18_abstract_unified_diff.txt").split("\n")
hunks = [l for l in dl if l.startswith("@@")]
minus = [l for l in dl if l.startswith("-") and not l.startswith("---")]
plus = [l for l in dl if l.startswith("+") and not l.startswith("+++")]
ctx_ok = (dl[3] == " " and dl[4] == " " and dl[7] == " " and dl[8] == " \\end{abstract}")
chk("A9", "F18 diff 结构：恰 1 hunk（@@ -74,5 +74,5 @@）；−1 行＝old／＋1 行＝new；"
    "上下文 4 行（2 空＋1 空＋\\end{abstract}）与两 tex 实际行 L74–L78 逐行核对恒等；头注指纹对",
    len(hunks) == 1 and hunks[0] == "@@ -74,5 +74,5 @@" and len(minus) == 1 and len(plus) == 1
    and ctx_ok and minus[0] == "-" + OLD and plus[0] == "+" + NEW
    and pre.split("\n")[73:78] == ["", "", OLD, "", "\\end{abstract}"]
    and post.split("\n")[73:78] == ["", "", NEW, "", "\\end{abstract}"]
    and dl[0] == "--- fiction_that_feeds_back.tex (R6 pre-F18, sha12 45887c4316d3)"
    and dl[1] == "+++ fiction_that_feeds_back.tex (R6 F18, sha12 69125dd78382)",
    "1 hunk·−/+ 各 1 行·L74–L78 上下文恒等·头注 45887c4316d3→69125dd78382")

# A10 复合链（R5_to_R6 diff 增量核对：R5＋F01–F17＋F18＝终稿；反向全链回退＝R5）
sheet = rd(SNAP + "/查理_FTFB_R6改稿单_2026_10_20.md")
def parse_sheet(t):
    out = {}; segs = re.split(r"^### (F\d{2}) ·", t, flags=re.M)
    for k in range(1, len(segs), 2):
        body = segs[k + 1].split("---", 1)[0]
        blocks = re.findall(r"```tex\n(.*?)\n```", body, flags=re.S)
        if len(blocks) >= 2: out[segs[k]] = (blocks[0], blocks[1])
    return out
sh = parse_sheet(sheet)
sheet_ok = all(sh.get(p["id"]) == (p["old"], p["new"]) for p in pairs17) and len(sh) == 17
cur = r5; fwd_ok = True
for p in pairs17:
    if cur.count(p["old"]) != 1: fwd_ok = False; break
    cur = cur.replace(p["old"], p["new"], 1)
fwd_ok = fwd_ok and cur == pre
b1 = post.replace(NEW, OLD, 1); back_ok = True
for p in reversed(pairs17):
    if b1.count(p["new"]) != 1: back_ok = False; break
    b1 = b1.replace(p["new"], p["old"], 1)
back_ok = back_ok and b1 == r5
chk("A10", "复合链闭合（18 对全链＝审计链补全）：17 对 vs 改稿单 fence 逐字全等；"
    "R5＋F01–F17→45887c4316d3；＋F18→69125dd78382；反向 69125dd78382－F18－F01–F17→R5 ba2f157196f5",
    sheet_ok and fwd_ok and back_ok,
    "sheet 17/17 等同；正向链闭合；反向链闭合（每对恰单次替换）")

# ============ D. 语义保真抽验（独立重计） ============
pa = log["checks"]["preserved_anchors_count_1"]
pa_ok = len(pa) == 21 and all(NEW.count(a["anchor"]) == 1 and a["count"] == 1 for a in pa)
chk("D1", "保留锚串 21 段在 new 摘要各恰 1 次（独立重计＝JSON 登记值）；禁形 0：摘要内 kill/death 家族 0",
    pa_ok and NEW.lower().count("kill") == 0 and NEW.lower().count("death") == 0,
    "21 段全命中（含 F01 四要点与爱丽丝 5b 点逐字）")
nasc_old = sorted({"0x%x" % ord(c) for c in OLD if ord(c) > 127})
nasc_new = sorted({"0x%x" % ord(c) for c in NEW if ord(c) > 127})
chk("D2", "objection 小写在 new 摘要恰 1；数字集恰 {1,5,7.4}；非 ASCII 码点集合＝登记值（仅 U+00A7/U+2013/U+2014）",
    NEW.count("objection") == 1
    and set(re.findall(r"\d+(?:\.\d+)?", NEW)) == {"1", "5", "7.4"}
    and nasc_old == sorted(log["checks"]["non_ascii_old"])
    and nasc_new == sorted(log["checks"]["non_ascii_new"]),
    "objection=%d；nums=%s；码点集 old=%s new=%s" % (
        NEW.count("objection"), sorted(set(re.findall(r"\d+(?:\.\d+)?", NEW))),
        nasc_old, nasc_new))

# ============ B. 不变量抽检（前态↔后态，独立计数） ============
MARK = "\\section*{References}"
i5, i6 = pre.find(MARK), post.find(MARK)
refs5, refs6 = pre[i5:], post[i6:]
it5 = re.findall(r"\\item\[R(\d{2})\.\]", refs5); it6 = re.findall(r"\\item\[R(\d{2})\.\]", refs6)
chk("B1", "池 66：References 区块字节恒等；\\item[Rxx.] 两侧各 66 且序号 R01–R66 全等",
    refs5 == refs6 and it5 == it6 and len(it6) == 66 and it6 == ["%02d" % k for k in range(1, 67)],
    "区块 %d B 恒等；条目 %d→%d" % (len(refs5.encode()), len(it5), len(it6)))
c5 = re.findall(r"\[R(\d{2})\]", pre[:i5]); c6 = re.findall(r"\[R(\d{2})\]", post[:i6])
chk("B2", "引用实例 190→190（题录区前），多重集恒等",
    len(c5) == 190 and len(c6) == 190 and sorted(c5) == sorted(c6), "%d→%d" % (len(c5), len(c6)))
chk("B3", "a57d7fe 冻结恰 1（前＝后）",
    pre.count("a57d7fe") == 1 and post.count("a57d7fe") == 1,
    "1→1；后态位置 L%d" % line_of(post, "a57d7fe"))

au5 = re.findall(r"\\author\{[^}]*\}", pre); au6 = re.findall(r"\\author\{[^}]*\}", post)
occ = []
for m in re.finditer(r"[Kk]imi", post):
    ln = post[:m.start()].count("\n") + 1
    line = post.split("\n")[ln - 1]
    if "bukimi no tani" in line:
        kl = "bukimi 子串（Mori 术语罗马字）"
    elif "ftfb" in line and "s7" in line:
        kl = "审计迹（冻结路径 _kimi_ftfb_s7 之 TeX 转义形 \\\\_kimi\\\\_）"
    else:
        kl = "?"
    occ.append((ln, kl))
occ_pre = len(re.findall(r"[Kk]imi", pre))
det = ("kimi 位置：" + "＋".join("L%d（%s）" % o for o in occ)) if len(occ) >= 2 else "kimi 出现数异常"
klass_ok = (len(occ) == 2 and occ[0][1].startswith("bukimi") and occ[1][1].startswith("审计迹"))
chk("B4", "匿名面恒等：\\author 两侧同值（Qihao Yuan）；KIMI 大写 0/0；kimi 2/2＝1 审计迹＋1 bukimi 子串；"
    "onewithdream 0/0；anonymized in this edition 2/2；致谢节 0/0；acknowledg 词 1/1；新摘要 0 署名",
    au5 == au6 and au6 == ["\\author{Qihao Yuan}"]
    and pre.count("KIMI") == 0 == post.count("KIMI")
    and len(occ) == 2 and occ_pre == 2 and klass_ok
    and pre.count("onewithdream") == 0 == post.count("onewithdream")
    and pre.count("anonymized in this edition") == 2 == post.count("anonymized in this edition")
    and pre.count("Acknowledg") == 0 == post.count("Acknowledg")
    and len(re.findall(r"acknowledg", pre)) == 1 == len(re.findall(r"acknowledg", post))
    and ("Yuan" not in NEW) and ("Qihao" not in NEW),
    det)
chk("B5", "0 诗引文：epigraph 0/0；\\begin{verse} 0/0",
    pre.count("epigraph") == 0 == post.count("epigraph")
    and pre.count("\\begin{verse}") == 0 == post.count("\\begin{verse}"), "两侧均 0")
chk("B6", "题式：甲式恰 1（前＝后）；乙式 0；旧式 Death is the point 0",
    post.count("\\subsection{The first action: verdicts before the runs}") == 1
    and pre.count("\\subsection{The first action: verdicts before the runs}") == 1
    and post.count("\\subsection{Death as the baseline}") == 0
    and post.count("\\subsection{Death is the point}") == 0,
    "甲式 L%d；乙式 0；旧式 0" % line_of(post, "\\subsection{The first action: verdicts before the runs}"))
kill5 = len(re.findall(r"[Kk]ill", pre)); kill6 = len(re.findall(r"[Kk]ill", post))
dea5 = len(re.findall(r"[Dd]eath", pre)); dea6 = len(re.findall(r"[Dd]eath", post))
ob5 = len(re.findall(r"[Oo]bjection", pre)); ob6 = len(re.findall(r"[Oo]bjection", post))
chk("B7", "词族支撑账（前＝后，替换不外溢）：position paper 1/1；position statement 4/4；"
    "Objection 小节头 4/4；[Kk]ill、[Dd]eath、[Oo]bjection 词族全等",
    pre.count("position paper") == 1 == post.count("position paper")
    and pre.count("position statement") == 4 == post.count("position statement")
    and len(re.findall(r"Objection", post)) == 4
    and kill5 == kill6 and dea5 == dea6 and ob5 == ob6,
    "kill %d→%d；death %d→%d；objection %d→%d" % (kill5, kill6, dea5, dea6, ob5, ob6))
chk("B8", "体量与行数：132,269→132,173 B（Δ=−96＝摘要压缩量）；新行符 689→689（＝物理行，与登记口径同）；"
    "split 元素 690→690（含尾空元素）；末行换行收束两侧同构",
    len(pre.encode()) == 132269 and len(post.encode()) == 132173
    and pre.count("\n") == 689 == post.count("\n")
    and len(pl) == 690 == len(ql)
    and pre.endswith("\n") and post.endswith("\n"),
    "−96 B；689 新行符（wc 口径）＝690 split 元素（含尾空元素，与 R6 验收轮口径同）")

# ============ C. 零触碰与多源正本 ============
chk("C1", "预 F18 正本多源一致：归档 tar 内件＝归档平铺件＝R5＋17 对重构（45887c4316d3）",
    sha12f(DAVE_FLAT) == "45887c4316d3" and fwd_ok, "三源同指纹 45887c4316d3")

watch = [
    ("shared/查理_FTFB_R6重构稿_2026/fiction_that_feeds_back.tex", SNAP + "/delivered_f18.tex"),
    ("shared/查理_FTFB_R6重构稿_2026/selfcheck_f18_pairs_log.json", SNAP + "/selfcheck_f18_pairs_log.json"),
    ("shared/查理_FTFB_R6重构稿_2026/F18_abstract_unified_diff.txt", SNAP + "/F18_abstract_unified_diff.txt"),
    ("shared/查理_FTFB_R6重构稿_2026/arxiv_metadata_abstract_F18_2026_10_20.txt", SNAP + "/arxiv_metadata_abstract_F18_2026_10_20.txt"),
    ("shared/查理_FTFB_R6重构稿_2026/查理_FTFB_R6落稿自检记录_2026_10_20.md", SNAP + "/delivered_selfcheck_md.md"),
    ("shared/查理_FTFB_R6重构稿_2026/apply_r6_f18_abstract.py", SNAP + "/apply_r6_f18_abstract.py"),
    ("shared/查理_FTFB_R6重构稿_2026/selfcheck_pairs_log.json", SNAP + "/selfcheck_pairs_log.json"),
    ("shared/查理_FTFB_R6重构稿_2026/R5_to_R6_unified_diff.txt", SNAP + "/R5_to_R6_unified_diff.txt"),
    ("shared/查理_FTFB_R6改稿单_2026_10_20.md", SNAP + "/查理_FTFB_R6改稿单_2026_10_20.md"),
    ("shared/查理_FTFB_R5落稿_2026_10_20/fiction_that_feeds_back.tex", SNAP + "/r5.tex"),
]
base = "/home/z/my-project/"
unt = [rel for rel, sn in watch if sha12f(base + rel) != sha12f(sn)]
chk("C2", "零触碰：shared 全部只读件（查理 R6 目录 8 件＋改稿单＋R5 tex）指纹与开工快照全等"
    "（戴夫打包目录系其重打包轮活跃写入区，不在本方扫描范围）",
    not unt, "10 件全等" if not unt else "变更：" + ";".join(unt))

json.dump(res, open(BASE + "/verify/bob_f18_result.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
print("\n独立验证结果：%d/%d PASS" % (len(res["checks"]) - res["fail"], len(res["checks"])))
sys.exit(1 if res["fail"] else 0)
